"""Startup budget and lifecycle deadline tests.

Pins the client startup budget against the server's default lifecycle bounds
(spatialanalyzer/briosa main 0c7ff7a; #298 and #315), pins that budget expiry is
reported as startup-timeout whichever phase it interrupts, and pins that
lifecycle calls carry no client-imposed per-call deadline.
"""

from __future__ import annotations

import asyncio
import inspect

import pytest
from google.protobuf.message import Message

from briosa import (
    BriosaClient,
    BriosaClientOptions,
    BriosaLoggingOptions,
    BriosaServerSelection,
    BriosaStartOptions,
    BriosaStartupError,
    SpatialAnalyzerLaunchOptions,
    SpatialAnalyzerSdkRecoveryMode,
    discovery_pb2,
    lifecycle_pb2,
)
from briosa.client import OwnedServer
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)

# Server defaults, identical in both targets (seconds).
# Briosa:Worker:StartupTimeout: worker launch, COM activation, Ready, ConnectEx,
# and the application association after a successful readiness probe.
SERVER_STARTUP_TIMEOUT = 10.0
# Briosa:Worker:ReadinessProbeTimeout: the private readiness probe inside Connect.
SERVER_READINESS_PROBE_TIMEOUT = 30.0
# Briosa:SpatialAnalyzer:ApplicationStartupTimeout: LaunchSpatialAnalyzer's wait.
SERVER_APPLICATION_STARTUP_TIMEOUT = 30.0
# Fixed heartbeat timeout: Connect's liveness recheck after the association.
SERVER_HEARTBEAT_TIMEOUT = 5.0
# Fixed worker shutdown bound: forced cleanup before a failed Connect is reported.
SERVER_WORKER_SHUTDOWN_TIMEOUT = 5.0
# Server host startup, process observations, discovery, and round trips.
MARGIN = 20.0

LIFECYCLE_METHODS = (
    "get_server_snapshot",
    "get_spatial_analyzer_state",
    "launch_spatial_analyzer",
    "close_owned_spatial_analyzer",
    "get_spatial_analyzer_sdk_state",
    "start_spatial_analyzer_sdk",
    "connect_to_spatial_analyzer",
    "reconnect_to_spatial_analyzer",
    "stop_spatial_analyzer_sdk",
    "recover_spatial_analyzer_sdk",
)


def test_default_startup_budget_is_two_minutes() -> None:
    assert BriosaStartOptions().startup_timeout == 120.0


def test_default_startup_budget_covers_server_worst_case_with_margin() -> None:
    start_sdk = SERVER_STARTUP_TIMEOUT
    launch_application = SERVER_APPLICATION_STARTUP_TIMEOUT
    connect = (
        SERVER_STARTUP_TIMEOUT
        + SERVER_READINESS_PROBE_TIMEOUT
        + SERVER_STARTUP_TIMEOUT
        + SERVER_HEARTBEAT_TIMEOUT
        + SERVER_WORKER_SHUTDOWN_TIMEOUT
    )
    server_worst_case = start_sdk + launch_application + connect

    assert server_worst_case == 100.0
    assert BriosaStartOptions().startup_timeout >= server_worst_case + MARGIN


def test_lifecycle_methods_default_to_no_deadline() -> None:
    for name in LIFECYCLE_METHODS:
        parameter = inspect.signature(getattr(BriosaClient, name)).parameters["timeout"]
        assert parameter.kind is inspect.Parameter.KEYWORD_ONLY, name
        assert parameter.default is None, name


async def test_startup_phases_run_inside_one_overall_budget() -> None:
    transport = RecordingTransport()
    client = create_client(transport)
    await client.start()
    try:
        assert [name for name, _ in transport.calls] == [
            "snapshot",
            "start-sdk",
            "launch-sa",
            "connect-sdk",
            "snapshot",
        ]
        assert all(timeout is None for _, timeout in transport.calls)
    finally:
        await client.stop()


@pytest.mark.parametrize("phase", ["snapshot", "start-sdk", "launch-sa", "connect-sdk"])
async def test_budget_expiry_during_any_startup_rpc_is_a_startup_timeout(
    phase: str,
) -> None:
    transport = RecordingTransport(hang_at=phase)
    client = create_client(transport)
    try:
        with pytest.raises(BriosaStartupError) as raised:
            await client.start(BriosaStartOptions(startup_timeout=0.1))
        assert raised.value.diagnostic_code == "startup-timeout"
        assert transport.calls[-1][0] == phase
    finally:
        await client.stop()


async def test_caller_cancellation_during_startup_stays_cancellation() -> None:
    transport = RecordingTransport(hang_at="connect-sdk")
    client = create_client(transport)
    try:
        caller = asyncio.create_task(
            client.start(BriosaStartOptions(startup_timeout=1.0))
        )
        await asyncio.sleep(0.05)
        caller.cancel()
        with pytest.raises(asyncio.CancelledError):
            await caller
    finally:
        await client.stop()


async def test_lifecycle_calls_carry_no_client_deadline() -> None:
    transport = RecordingTransport()
    client = create_client(transport, BriosaClientOptions(command_timeout=1.0))
    await client.start()
    try:
        transport.calls.clear()

        await client.get_server_snapshot()
        await client.get_spatial_analyzer_state()
        await client.get_spatial_analyzer_sdk_state()
        await client.reconnect_to_spatial_analyzer()
        await client.recover_spatial_analyzer_sdk(
            SpatialAnalyzerSdkRecoveryMode.REPLACE_WITHOUT_REPLAY
        )
        await client.connect_to_spatial_analyzer()
        await client.stop_spatial_analyzer_sdk()
        await client.start_spatial_analyzer_sdk()
        await client.launch_spatial_analyzer()
        await client.close_owned_spatial_analyzer()

        assert [name for name, _ in transport.calls] == [
            "snapshot",
            "get-sa-state",
            "get-sdk-state",
            "reconnect-sdk",
            "recover-sdk",
            "connect-sdk",
            "stop-sdk",
            "start-sdk",
            "launch-sa",
            "close-sa",
        ]
        assert all(timeout is None for _, timeout in transport.calls)
    finally:
        await client.stop()


class RecordingServer:
    target = "127.0.0.1:49152"
    has_exited = False

    async def close(self) -> None:
        return None


class RecordingLauncher:
    async def launch(
        self,
        logging: BriosaLoggingOptions | None = None,
        selection: BriosaServerSelection | None = None,
    ) -> OwnedServer:
        return RecordingServer()


def create_client(
    transport: RecordingTransport, options: BriosaClientOptions | None = None
) -> BriosaClient:
    return BriosaClient(
        options,
        _server_launcher=RecordingLauncher(),
        _transport_factory=lambda _target: transport,
    )


class RecordingTransport:
    def __init__(self, hang_at: str | None = None) -> None:
        self.calls: list[tuple[str, float | None]] = []
        # The RPC that never answers until its task is cancelled, as a grpc.aio
        # call is when the startup budget expires.
        self._hang_at = hang_at
        self._sdk_generation = 0
        self._connected = False
        self._recording = True

    async def _record(self, name: str, timeout: float | None) -> None:
        if self._recording:
            self.calls.append((name, timeout))
        if name == self._hang_at:
            await asyncio.Event().wait()

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        await self._record("snapshot", timeout)
        return snapshot(self._connected)

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        await self._record("get-sa-state", timeout)
        return application(running=True)

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        await self._record("launch-sa", timeout)
        return application(running=True)

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        await self._record("close-sa", timeout)
        return application(running=False)

    async def get_sdk_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        await self._record("get-sdk-state", timeout)
        return self._sdk_state()

    async def start_sdk(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        await self._record("start-sdk", timeout)
        self._sdk_generation += 1
        self._connected = False
        return self._sdk_state()

    async def connect_sdk(
        self,
        expected_generation: int,
        *,
        reconnect: bool,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        await self._record("reconnect-sdk" if reconnect else "connect-sdk", timeout)
        self._connected = True
        return self._sdk_state()

    async def stop_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        await self._record("stop-sdk", timeout)
        self._sdk_generation = 0
        self._connected = False
        return self._sdk_state()

    async def recover_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        await self._record("recover-sdk", timeout)
        self._sdk_generation += 1
        self._connected = False
        return self._sdk_state()

    async def get_working_directory(self, timeout: float | None = None) -> str:
        raise NotImplementedError

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message:
        raise NotImplementedError

    async def close(self) -> None:
        self._recording = False

    def _sdk_state(self) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        state = lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
            state_revision=1,
            sdk_state=(
                lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_STOPPED
                if self._sdk_generation == 0
                else lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_READY
                if self._connected
                else lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_RUNNING
            ),
            connection_state=(
                discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED
                if self._connected
                else discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_DISCONNECTED
            ),
            execution_readiness_state=(
                discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
                if self._connected
                else discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNVERIFIED
            ),
            ready_for_mp=self._connected,
            recovery_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED,
        )
        if self._sdk_generation > 0:
            state.sdk_generation = self._sdk_generation
        return state


def application(*, running: bool) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
    if running:
        return lifecycle_pb2.SpatialAnalyzerLifecycleState(
            state_revision=1,
            application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING,
            ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED,
            application_generation=1,
        )
    return lifecycle_pb2.SpatialAnalyzerLifecycleState(
        state_revision=1,
        application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_NOT_RUNNING,
        ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_NONE,
    )


def snapshot(
    ready: bool,
) -> tuple[
    discovery_pb2.GetServerInfoResponse,
    discovery_pb2.ListCapabilitiesResponse,
]:
    server = discovery_pb2.GetServerInfoResponse(
        version={
            "briosa_version": BRIOSA_VERSION,
            "source_revision": SOURCE_REVISION,
            "protocol_package": PROTOCOL_PACKAGE,
            "spatial_analyzer_target": SPATIAL_ANALYZER_TARGET,
        },
        worker_state=discovery_pb2.WORKER_RUNTIME_STATE_READY,
        spatial_analyzer_connection_state=(
            discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED
            if ready
            else discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_DISCONNECTED
        ),
        spatial_analyzer_execution_readiness_state=(
            discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
            if ready
            else discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNVERIFIED
        ),
        ready_for_mp=ready,
        target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
        compatibility=discovery_pb2.CompatibilityContract(major=2),
    )
    capabilities = discovery_pb2.ListCapabilitiesResponse(
        protocol_package=PROTOCOL_PACKAGE,
        spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
    )
    return server, capabilities
