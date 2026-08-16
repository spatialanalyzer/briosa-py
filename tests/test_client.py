from __future__ import annotations

import asyncio
from typing import cast

import grpc
import pytest
from google.protobuf.message import Message

from briosa import (
    BriosaClient,
    BriosaClientOptions,
    BriosaLifecycleError,
    BriosaOperationError,
    BriosaProtocolError,
    BriosaSpatialAnalyzerError,
    BriosaStartOptions,
    BriosaTransportError,
    Color,
    OperationFailureKind,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    RpcStatusCode,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerLaunchOptions,
    SpatialAnalyzerLifecycleFailureKind,
    analysis_operations_pb2,
    discovery_pb2,
    lifecycle_pb2,
    operation_outcomes_pb2,
    view_control_pb2,
)
from briosa.client import OwnedServer
from briosa.protocol_identity import (
    ARTIFACT_NAME,
    BRIOSA_VERSION,
    CLIENT_GENERATION_CONTRACT,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)
from briosa.transport import ClientTransport, map_rpc_error, map_sdk_state
from briosa.wave_a_operations import WAVE_A_OPERATIONS


class FakeRpcError(grpc.RpcError):
    def __init__(
        self,
        status_code: grpc.StatusCode,
        metadata: tuple[tuple[str, str | bytes], ...] = (),
    ) -> None:
        super().__init__()
        self._status_code = status_code
        self._metadata = metadata

    def code(self) -> grpc.StatusCode:
        return self._status_code

    def trailing_metadata(  # type: ignore[override]
        self,
    ) -> tuple[tuple[str, str | bytes], ...]:
        return self._metadata


class FakeOwnedServer:
    target = "127.0.0.1:49152"
    has_exited = False

    def __init__(self) -> None:
        self.closed = False

    async def close(self) -> None:
        self.closed = True


class FakeServerLauncher:
    def __init__(self) -> None:
        self.server = FakeOwnedServer()
        self.launch_count = 0

    async def launch(self) -> OwnedServer:
        self.launch_count += 1
        return self.server


class FakeTransport:
    def __init__(self) -> None:
        self.calls: list[str] = []
        self.sdk_generation = 0
        self.connected = False
        self.launch_failure: grpc.RpcError | None = None
        self.publish_ready_snapshot = True
        self.connect_generations: list[int] = []
        self.stop_generations: list[int] = []
        self.close_generations: list[int] = []
        self.close_application_count = 0
        self.operation_requests: list[tuple[str, Message]] = []
        self.operation_responses: dict[str, Message] = {}

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        self.calls.append("snapshot")
        return matching_snapshot(self.connected and self.publish_ready_snapshot)

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        self.calls.append("get-sa-state")
        return application_not_running()

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        self.calls.append("launch-sa")
        if self.launch_failure is not None:
            raise self.launch_failure
        return lifecycle_pb2.SpatialAnalyzerLifecycleState(
            state_revision=2,
            application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING,
            ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED,
            application_generation=2,
        )

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        self.calls.append("close-sa")
        self.close_application_count += 1
        self.close_generations.append(expected_generation)
        return application_not_running()

    async def get_sdk_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        self.calls.append("get-sdk-state")
        return self._sdk_state()

    async def start_sdk(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        self.calls.append("start-sdk")
        self.sdk_generation += 1
        self.connected = False
        return self._sdk_state()

    async def connect_sdk(
        self,
        expected_generation: int,
        *,
        reconnect: bool,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        self.calls.append("reconnect-sdk" if reconnect else "connect-sdk")
        self.connect_generations.append(expected_generation)
        self.connected = True
        return self._sdk_state()

    async def stop_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        self.calls.append("stop-sdk")
        self.stop_generations.append(expected_generation)
        self.connected = False
        self.sdk_generation = 0
        return self._sdk_state()

    async def recover_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        self.calls.append("recover-sdk")
        self.sdk_generation += 1
        self.connected = False
        return self._sdk_state()

    async def get_working_directory(self, timeout: float | None = None) -> str:
        self.calls.append("get-working-directory")
        return r"C:\Working"

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message:
        self.calls.append(path)
        self.operation_requests.append((path, request))
        if path in self.operation_responses:
            return self.operation_responses[path]
        if path == "/briosa.AnalysisOperations/GetNumberOfCollections":
            return analysis_operations_pb2.GetNumberOfCollectionsResult(total_count=3)
        return response_type()

    async def close(self) -> None:
        self.calls.append("close-transport")

    def _sdk_state(self) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        state = lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
            state_revision=3,
            sdk_state=(
                lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_STOPPED
                if self.sdk_generation == 0
                else lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_READY
                if self.connected
                else lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_RUNNING
            ),
            connection_state=(
                discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED
                if self.connected
                else discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_DISCONNECTED
            ),
            execution_readiness_state=(
                discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
                if self.connected
                else discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNVERIFIED
            ),
            ready_for_mp=self.connected,
            recovery_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED,
        )
        if self.sdk_generation > 0:
            state.sdk_generation = self.sdk_generation
        return state


def create_client(
    launcher: FakeServerLauncher,
    transport: FakeTransport,
    options: BriosaClientOptions | None = None,
) -> BriosaClient:
    return BriosaClient(
        options,
        _server_launcher=launcher,
        _transport_factory=lambda _target: transport,
    )


def application_not_running() -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
    return lifecycle_pb2.SpatialAnalyzerLifecycleState(
        state_revision=1,
        application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_NOT_RUNNING,
        ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_NONE,
    )


def matching_snapshot(
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
    )
    capabilities = discovery_pb2.ListCapabilitiesResponse(
        protocol_package=PROTOCOL_PACKAGE,
        spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
        operations=[
            {
                "operation_id": operation_id,
                "grpc_service": service,
                "rpc": rpc,
                "fully_qualified_method": f"/{service}/{rpc}",
            }
            for _method, service, rpc, operation_id in WAVE_A_OPERATIONS
        ],
    )
    return server, capabilities


def application_lifecycle_failure() -> FakeRpcError:
    detail = lifecycle_pb2.SpatialAnalyzerLifecycleError(
        rpc="LaunchSpatialAnalyzer",
        kind=lifecycle_pb2.SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_LAUNCH_FAILED,
        diagnostic_code="sa-launch-failed",
        recovery_guidance=lifecycle_pb2.LIFECYCLE_RECOVERY_GUIDANCE_CORRECT_ENVIRONMENT,
        state=application_not_running(),
    )
    return FakeRpcError(
        grpc.StatusCode.FAILED_PRECONDITION,
        (("briosa-spatial-analyzer-lifecycle-error-bin", detail.SerializeToString()),),
    )


def test_protocol_identity_matches_merged_lifecycle_artifact() -> None:
    assert ARTIFACT_NAME == "briosa-protocol-0.2.0-sa-2026.1.0529.7"
    assert SOURCE_REVISION == "a009d95c1a5d293bdcbe3edb2edfe9cd99081c2e"
    assert PROTOCOL_PACKAGE == "briosa"
    assert CLIENT_GENERATION_CONTRACT == "standard-protobuf-grpc"
    assert SPATIAL_ANALYZER_TARGET == "2026.1.0529.7"


def test_wave_a_surface_matches_the_published_capability_set() -> None:
    assert len(WAVE_A_OPERATIONS) == 469
    assert len({item[3] for item in WAVE_A_OPERATIONS}) == 469
    assert all(hasattr(BriosaClient, item[0]) for item in WAVE_A_OPERATIONS)


@pytest.mark.asyncio
async def test_wave_a_scalar_and_domain_value_operations_use_generic_transport() -> (
    None
):
    transport = FakeTransport()
    client = create_client(FakeServerLauncher(), transport)
    await client.start()

    assert await client.get_number_of_collections() == 3
    await client.set_background_color(
        Color(red=1, green=2, blue=3),
        Color(red=4, green=5, blue=6),
        Color(red=7, green=8, blue=9),
        Color(red=10, green=11, blue=12),
    )

    _, raw_request = transport.operation_requests[-1]
    request = cast(view_control_pb2.SetBackgroundColorRequest, raw_request)
    assert request.DESCRIPTOR.full_name == "briosa.SetBackgroundColorRequest"
    assert request.solid_color_name.red == 1
    assert request.highlight_color.blue == 12
    await client.aclose()


@pytest.mark.asyncio
async def test_wave_a_missing_required_output_fails_through_public_boundary() -> None:
    transport = FakeTransport()
    transport.operation_responses[
        "/briosa.AnalysisOperations/GetNumberOfCollections"
    ] = analysis_operations_pb2.GetNumberOfCollectionsResult()
    client = create_client(FakeServerLauncher(), transport)
    await client.start()

    with pytest.raises(BriosaProtocolError, match="required-output-missing"):
        await client.get_number_of_collections()

    await client.aclose()


def test_construction_is_dormant_and_options_fail_closed() -> None:
    launcher = FakeServerLauncher()
    _ = create_client(launcher, FakeTransport())
    assert launcher.launch_count == 0
    with pytest.raises(ValueError):
        BriosaClientOptions(command_timeout=0)
    with pytest.raises(ValueError):
        BriosaStartOptions(start_spatial_analyzer_sdk=False)
    with pytest.raises(ValueError):
        BriosaStartOptions(
            launch_spatial_analyzer=False,
            launch_options=SpatialAnalyzerLaunchOptions(start_minimized=True),
        )


@pytest.mark.asyncio
async def test_default_startup_and_stop_leave_spatial_analyzer_running() -> None:
    launcher = FakeServerLauncher()
    transport = FakeTransport()
    client = create_client(launcher, transport)

    await client.start()
    directory = await client.get_working_directory()
    await client.stop()

    assert directory == r"C:\Working"
    assert transport.calls == [
        "snapshot",
        "start-sdk",
        "launch-sa",
        "connect-sdk",
        "snapshot",
        "get-working-directory",
        "stop-sdk",
        "close-transport",
    ]
    assert launcher.server.closed
    assert transport.close_application_count == 0
    await client.aclose()


@pytest.mark.asyncio
async def test_control_plane_only_startup_does_not_create_sdk_or_sa() -> None:
    transport = FakeTransport()
    client = create_client(FakeServerLauncher(), transport)
    await client.start(
        BriosaStartOptions(
            start_spatial_analyzer_sdk=False,
            launch_spatial_analyzer=False,
            connect_to_spatial_analyzer=False,
        )
    )
    snapshot = await client.get_server_snapshot()
    assert not snapshot.ready_for_mp
    with pytest.raises(BriosaLifecycleError):
        await client.get_working_directory()
    assert transport.calls == ["snapshot", "snapshot"]
    await client.aclose()


@pytest.mark.asyncio
async def test_partial_failure_preserves_diagnostic_control_plane() -> None:
    launcher = FakeServerLauncher()
    transport = FakeTransport()
    transport.launch_failure = application_lifecycle_failure()
    client = create_client(launcher, transport)

    with pytest.raises(BriosaSpatialAnalyzerError) as captured:
        await client.start()
    state = await client.get_spatial_analyzer_state()

    assert captured.value.kind is SpatialAnalyzerLifecycleFailureKind.LAUNCH_FAILED
    assert captured.value.diagnostic_code == "sa-launch-failed"
    assert state.application_state is SpatialAnalyzerApplicationState.NOT_RUNNING
    assert not launcher.server.closed
    await client.stop()
    assert launcher.server.closed
    await client.aclose()


@pytest.mark.asyncio
async def test_failed_final_readiness_does_not_publish_mp_admission() -> None:
    transport = FakeTransport()
    transport.publish_ready_snapshot = False
    client = create_client(FakeServerLauncher(), transport)

    with pytest.raises(BriosaLifecycleError):
        await client.start()
    assert (await client.get_spatial_analyzer_sdk_state()).ready_for_mp
    with pytest.raises(BriosaLifecycleError):
        await client.get_working_directory()
    await client.aclose()


@pytest.mark.asyncio
async def test_concurrent_starts_share_one_server_and_generation_guards() -> None:
    launcher = FakeServerLauncher()
    transport = FakeTransport()
    client = create_client(launcher, transport)

    await asyncio.gather(client.start(), client.start())
    await client.reconnect_to_spatial_analyzer()
    await client.stop_spatial_analyzer_sdk()
    await client.start_spatial_analyzer_sdk()
    await client.close_owned_spatial_analyzer()

    assert launcher.launch_count == 1
    assert transport.connect_generations == [1, 1]
    assert transport.stop_generations[0] == 1
    assert transport.close_generations == [2]
    await client.aclose()


@pytest.mark.asyncio
async def test_async_context_starts_and_finally_closes_only_owned_resources() -> None:
    launcher = FakeServerLauncher()
    transport = FakeTransport()
    client = create_client(launcher, transport)

    async with client as entered:
        assert entered is client
        assert await entered.get_working_directory() == r"C:\Working"

    assert launcher.server.closed
    assert transport.close_application_count == 0
    with pytest.raises(BriosaLifecycleError):
        await client.start()


def test_incident_preserves_string_operation_id() -> None:
    mapped = map_sdk_state(
        lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
            sdk_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_FAULTED,
            connection_state=discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_FAULTED,
            execution_readiness_state=(
                discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_OPERATOR_RECOVERY_REQUIRED
            ),
            recovery_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_STATE_RECOVERY_AVAILABLE,
            last_incident={
                "sdk_generation": 4,
                "termination_kind": (
                    lifecycle_pb2.SPATIAL_ANALYZER_SDK_TERMINATION_KIND_WATCHDOG_TERMINATED
                ),
                "operation_id": "file_operations.get_working_directory",
            },
        )
    )
    assert mapped.last_incident is not None
    assert mapped.last_incident.operation_id == "file_operations.get_working_directory"


def test_operation_error_is_detached_and_preserves_unknown_completion() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="construction_operations.mutating_operation",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_WORKER_WATCHDOG_TIMEOUT,
        diagnostic_code="worker-execution-watchdog-timeout",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_WORKER_REPLACEMENT,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_UNKNOWN,
    )
    mapped = map_rpc_error(
        FakeRpcError(
            grpc.StatusCode.UNAVAILABLE,
            (("briosa-operation-error-bin", detail.SerializeToString()),),
        )
    )
    assert isinstance(mapped, BriosaOperationError)
    assert mapped.status_code is RpcStatusCode.UNAVAILABLE
    assert mapped.failure.kind is OperationFailureKind.WORKER_WATCHDOG_TIMEOUT
    assert mapped.failure.recovery_guidance is RecoveryGuidance.WORKER_REPLACEMENT
    assert mapped.failure.replay_guidance is ReplayGuidance.RECONCILE_BEFORE_REPLAY
    assert mapped.failure.replay_safety is ReplaySafety.UNKNOWN
    assert mapped.completion_unknown is True
    assert mapped.reconciliation_required is True


def test_transport_error_uses_handwritten_status() -> None:
    error = FakeRpcError(grpc.StatusCode.UNAVAILABLE)
    mapped = map_rpc_error(error)
    assert isinstance(mapped, BriosaTransportError)
    assert mapped.status_code is RpcStatusCode.UNAVAILABLE
    assert mapped.diagnostic_code == "transport-unavailable"


def test_fake_transport_satisfies_private_protocol() -> None:
    transport: ClientTransport = FakeTransport()
    assert transport is not None
