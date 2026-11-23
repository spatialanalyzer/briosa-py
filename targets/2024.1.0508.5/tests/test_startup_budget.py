"""Startup budget and lifecycle deadline tests.

Pins the client startup budget against the server's default lifecycle bounds
(spatialanalyzer/briosa main 0c7ff7a; #298 and #315), pins that budget expiry is
reported as startup-timeout whichever phase it interrupts, and pins that
lifecycle calls carry no client-imposed per-call deadline.

The virtual-clock tests drive every branch of the shared rule "Startup budget
from published lifecycle bounds"
(docs/architecture/client-library-behavioral-contract.md, briosa#400) through
the real asyncio timers: asyncio.timeout from Python 3.12, and the waiter that
Python 3.10 and 3.11 use, as their asyncio.wait_for did for client 0.5.0.
"""

from __future__ import annotations

import asyncio
import copy
import dataclasses
import inspect
import json
import os
import pickle
import subprocess
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, cast

import grpc
import guarded_launch_probe
import pytest
from facade_support import bound_facades, facade_functions, required_arguments
from google.protobuf.message import Message
from virtual_clock import VirtualClockLoop, run_virtual

import briosa
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
from briosa.client import (
    OwnedServer,
    _published_startup_allowance,
    _startup_timeout_error,
)
from briosa.models import _startup_timeout_omitted
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)
from briosa.transport import StartupCheckpoint, map_lifecycle_bounds

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
    assert isinstance(BriosaStartOptions().startup_timeout, float)
    assert repr(BriosaStartOptions().startup_timeout) == "120.0"


def test_only_leaving_the_argument_out_omits_the_budget() -> None:
    omitted = BriosaStartOptions()
    assert _startup_timeout_omitted(omitted)
    # Reading it gives a plain float, and passing that value back is explicit.
    assert type(omitted.startup_timeout) is float
    forwarded = BriosaStartOptions(startup_timeout=omitted.startup_timeout)
    assert not _startup_timeout_omitted(forwarded)
    for explicit in (120.0, 120, 300.0, 0.5, float(omitted.startup_timeout)):
        options = BriosaStartOptions(startup_timeout=explicit)
        assert not _startup_timeout_omitted(options)
        assert options.startup_timeout == explicit
        assert not _startup_timeout_omitted(replace(omitted, startup_timeout=explicit))
    # replace() passes every current value, including the budget.
    assert not _startup_timeout_omitted(replace(omitted, launch_spatial_analyzer=False))


def test_copies_and_pickles_keep_whether_the_budget_was_omitted() -> None:
    explicit = BriosaStartOptions(startup_timeout=120.0)

    def repickle(options: BriosaStartOptions) -> BriosaStartOptions:
        return cast(BriosaStartOptions, pickle.loads(pickle.dumps(options)))

    clones: tuple[Callable[[BriosaStartOptions], BriosaStartOptions], ...] = (
        copy.copy,
        copy.deepcopy,
        repickle,
    )
    for clone in clones:
        assert _startup_timeout_omitted(clone(BriosaStartOptions()))
        assert not _startup_timeout_omitted(clone(explicit))


def test_equality_and_hashing_compare_values_as_in_0_5_0() -> None:
    omitted = BriosaStartOptions()
    explicit = BriosaStartOptions(startup_timeout=120.0)
    assert omitted == explicit
    assert hash(omitted) == hash(explicit)
    assert repr(omitted) == repr(explicit)
    assert BriosaStartOptions(startup_timeout=121.0) != omitted


def test_the_field_list_and_signature_are_unchanged_from_0_5_0() -> None:
    from dataclasses import asdict, fields

    assert [item.name for item in fields(BriosaStartOptions)] == [
        "server_selection",
        "start_spatial_analyzer_sdk",
        "launch_spatial_analyzer",
        "connect_to_spatial_analyzer",
        "launch_options",
        "startup_timeout",
        "logging",
    ]
    parameter = inspect.signature(BriosaStartOptions).parameters["startup_timeout"]
    assert parameter.default == 120.0
    assert repr(parameter.default) == "120.0"
    assert type(asdict(BriosaStartOptions())["startup_timeout"]) is float


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

    async def get_server_info(
        self,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> discovery_pb2.GetServerInfoResponse:
        if checkpoint is not None:
            await checkpoint()
        await self._record("server-info", timeout)
        return snapshot(self._connected)[0]

    async def list_capabilities(
        self,
        *,
        include_denied: bool = False,
        timeout: float | None = None,
        checkpoint: StartupCheckpoint | None = None,
    ) -> discovery_pb2.ListCapabilitiesResponse:
        if checkpoint is not None:
            await checkpoint()
        await self._record("list-capabilities", timeout)
        return snapshot(self._connected)[1]

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        await self._record("get-sa-state", timeout)
        return application(running=True)

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        if checkpoint is not None:
            await checkpoint()
        await self._record("launch-sa", timeout)
        return application(running=True)

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        await self._record("close-sa", timeout)
        return application(running=False)

    async def get_sdk_state(
        self,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        if checkpoint is not None:
            await checkpoint()
        await self._record("get-sdk-state", timeout)
        return self._sdk_state()

    async def start_sdk(
        self,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        if checkpoint is not None:
            await checkpoint()
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
        checkpoint: StartupCheckpoint | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        if checkpoint is not None:
            await checkpoint()
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
    bounds: discovery_pb2.LifecycleBounds | None = None,
    revision: int = 0,
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
        compatibility=discovery_pb2.CompatibilityContract(major=3, revision=revision),
    )
    if bounds is not None:
        server.lifecycle_bounds.CopyFrom(bounds)
    capabilities = discovery_pb2.ListCapabilitiesResponse(
        protocol_package=PROTOCOL_PACKAGE,
        spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
    )
    return server, capabilities


# --- The startup budget on a virtual clock -------------------------------------
#
# These run on VirtualClockLoop, so each deadline is exact: when a startup
# expires, loop.time() is the instant its budget ran out. The startup begins at
# T0 and the loop never moves time unless every task is waiting.

T0 = 1000.0


def bounds(**milliseconds: int) -> discovery_pb2.LifecycleBounds:
    return discovery_pb2.LifecycleBounds(
        **{f"{name}_milliseconds": value for name, value in milliseconds.items()}  # type: ignore[arg-type]
    )


class ClockedTransport(RecordingTransport):
    """A fake server whose RPCs suspend, as real ones do, and can move the clock.

    ``published`` is the first snapshot's lifecycle bounds (``None`` for Server
    0.10.0); ``later`` is every later snapshot's. ``on`` runs an action the first
    time an RPC is called, before it suspends; ``hang_snapshot`` makes the
    snapshot with that ordinal never answer.
    """

    def __init__(
        self,
        loop: VirtualClockLoop,
        *,
        published: discovery_pb2.LifecycleBounds | None = None,
        later: discovery_pb2.LifecycleBounds | None = None,
        revision: int = 1,
        hang_at: str | None = None,
        hang_snapshot: int | None = None,
        on: dict[str, Callable[[], None]] | None = None,
        yields: int = 1,
    ) -> None:
        super().__init__(hang_at=hang_at)
        self.hang_at = hang_at
        self.loop = loop
        self._published = published
        self._later = later
        self._revision = revision
        self._hang_snapshot = hang_snapshot
        self._on = dict(on or {})
        self._yields = yields
        self._snapshots = 0
        self.closed = False

    async def _record(self, name: str, timeout: float | None) -> None:
        action = self._on.pop(name, None)
        if action is not None:
            action()
        if self._recording:
            self.calls.append((name, timeout))
        for _ in range(self._yields):
            await asyncio.sleep(0)
        if name == self.hang_at:
            await asyncio.Event().wait()

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        self._snapshots += 1
        await self._record("snapshot", timeout)
        if self._snapshots == self._hang_snapshot:
            await asyncio.Event().wait()
        published = self._published if self._snapshots == 1 else self._later
        return snapshot(self._connected, published, self._revision)

    async def get_server_info(
        self,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> discovery_pb2.GetServerInfoResponse:
        if checkpoint is not None:
            await checkpoint()
        # A guarded startup's post-Connect discovery, which it checks before
        # each of its two calls.
        self._snapshots += 1
        await self._record("server-info", timeout)
        if self._snapshots == self._hang_snapshot:
            await asyncio.Event().wait()
        return snapshot(self._connected, self._later, self._revision)[0]

    async def close(self) -> None:
        self.closed = True
        await super().close()


def names(transport: RecordingTransport) -> list[str]:
    return [name for name, _ in transport.calls]


async def expect_startup_timeout(
    client: BriosaClient, options: BriosaStartOptions | None = None
) -> BriosaStartupError:
    with pytest.raises(BriosaStartupError) as raised:
        await client.start(options)
    assert raised.value.diagnostic_code == "startup-timeout"
    return raised.value


def expiry(
    *,
    published: discovery_pb2.LifecycleBounds | None,
    options: BriosaStartOptions | None = None,
    hang_at: str = "connect-sdk",
    revision: int = 1,
    timer_limit: float | None = None,
    **transport: Any,
) -> tuple[float, list[str]]:
    """Start against a fake server that hangs; return when the budget ran out."""

    async def body(loop: VirtualClockLoop) -> tuple[float, list[str]]:
        fake = ClockedTransport(
            loop, published=published, revision=revision, hang_at=hang_at, **transport
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client, options)
            return loop.time() - T0, names(fake)
        finally:
            await client.stop()

    return run_virtual(body, now=T0, timer_limit=timer_limit)


SERVER_0_10_1_DEFAULTS = bounds(
    start_sdk=45_000,
    launch_spatial_analyzer=30_000,
    connect_spatial_analyzer=60_000,
    startup_with_launch=100_000,
    startup_without_launch=70_000,
)


def test_server_0_10_0_keeps_the_fixed_two_minute_budget() -> None:
    elapsed, calls = expiry(published=None, revision=0)
    assert elapsed == 120.0
    assert calls == ["snapshot", "start-sdk", "launch-sa", "connect-sdk"]


def test_server_0_10_1_defaults_keep_the_two_minute_floor() -> None:
    # 100 s + 20 s is exactly the floor.
    assert expiry(published=SERVER_0_10_1_DEFAULTS)[0] == 120.0


def test_a_larger_published_allowance_lengthens_an_omitted_budget() -> None:
    assert expiry(published=bounds(startup_with_launch=300_000))[0] == 320.0


def test_the_new_deadline_counts_from_the_start_instant() -> None:
    def later(loop: VirtualClockLoop) -> Callable[[], None]:
        return lambda: setattr(loop, "now", T0 + 10.0)

    async def body(loop: VirtualClockLoop) -> float:
        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at="connect-sdk",
            on={"snapshot": later(loop)},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client)
            return loop.time() - T0
        finally:
            await client.stop()

    # t0 + max(120, 300 + 20), not the time of discovery + 320.
    assert run_virtual(body, now=T0) == 320.0


@pytest.mark.parametrize("explicit", [120.0, 200.0, 30.0, 120])
def test_an_explicit_timeout_always_wins(explicit: float) -> None:
    elapsed, _ = expiry(
        published=bounds(startup_with_launch=300_000),
        options=BriosaStartOptions(startup_timeout=explicit),
    )
    assert elapsed == explicit


def test_a_forwarded_default_is_an_explicit_timeout() -> None:
    forwarded = BriosaStartOptions(startup_timeout=BriosaStartOptions().startup_timeout)
    elapsed, _ = expiry(
        published=bounds(startup_with_launch=300_000), options=forwarded
    )
    assert elapsed == 120.0


def test_replace_passes_the_budget_explicitly() -> None:
    options = replace(BriosaStartOptions(), launch_spatial_analyzer=False)
    elapsed, _ = expiry(
        published=bounds(startup_without_launch=300_000), options=options
    )
    assert elapsed == 120.0


def test_copies_and_pickles_keep_an_omitted_budget() -> None:
    for options in (
        copy.copy(BriosaStartOptions()),
        copy.deepcopy(BriosaStartOptions()),
        pickle.loads(pickle.dumps(BriosaStartOptions())),
    ):
        elapsed, _ = expiry(
            published=bounds(startup_with_launch=300_000), options=options
        )
        assert elapsed == 320.0


ALLOWANCES = bounds(
    start_sdk=200_000,
    launch_spatial_analyzer=150_000,
    startup_with_launch=400_000,
    startup_without_launch=300_000,
)


@pytest.mark.parametrize(
    ("start", "launch", "connect", "hang_at", "deadline"),
    [
        (True, True, True, "connect-sdk", 420.0),
        (True, False, True, "connect-sdk", 320.0),
        (True, True, False, "launch-sa", 370.0),
        (True, False, False, "start-sdk", 220.0),
        (False, True, False, "launch-sa", 170.0),
    ],
    ids=["start-launch-connect", "start-connect", "start-launch", "start", "launch"],
)
def test_the_allowance_follows_the_selected_actions(
    start: bool, launch: bool, connect: bool, hang_at: str, deadline: float
) -> None:
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=start,
        launch_spatial_analyzer=launch,
        connect_to_spatial_analyzer=connect,
    )
    elapsed, _ = expiry(published=ALLOWANCES, options=options, hang_at=hang_at)
    assert elapsed == deadline


def test_no_selected_server_phase_has_no_allowance_to_adopt() -> None:
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=False,
        launch_spatial_analyzer=False,
        connect_to_spatial_analyzer=False,
    )
    published = map_lifecycle_bounds(snapshot(False, ALLOWANCES, 1)[0])
    assert published is not None
    assert _published_startup_allowance(published, options) is None

    async def body(loop: VirtualClockLoop) -> list[float]:
        client = create_client(ClockedTransport(loop, published=ALLOWANCES))
        await client.start(options)
        try:
            return loop.armed()
        finally:
            await client.stop()

    assert run_virtual(body, now=T0) == []


@pytest.mark.parametrize(
    ("published", "start", "launch", "connect", "hang_at"),
    [
        # Start SDK and Launch need both; one alone is never summed.
        (bounds(start_sdk=200_000), True, True, False, "launch-sa"),
        (bounds(launch_spatial_analyzer=200_000), True, True, False, "launch-sa"),
        (
            bounds(start_sdk=200_000, launch_spatial_analyzer=0),
            True,
            True,
            False,
            "launch-sa",
        ),
        # The combined allowance is never rebuilt from the per-phase ones.
        (
            bounds(
                start_sdk=200_000,
                launch_spatial_analyzer=150_000,
                connect_spatial_analyzer=100_000,
            ),
            True,
            True,
            True,
            "connect-sdk",
        ),
        (bounds(startup_with_launch=0), True, True, True, "connect-sdk"),
        (bounds(startup_with_launch=300_000), True, False, True, "connect-sdk"),
        (bounds(), True, True, True, "connect-sdk"),
    ],
    ids=[
        "launch-missing",
        "start-missing",
        "launch-zero",
        "no-combined",
        "combined-zero",
        "without-launch-missing",
        "empty",
    ],
)
def test_a_missing_or_zero_allowance_keeps_the_bootstrap_deadline(
    published: discovery_pb2.LifecycleBounds,
    start: bool,
    launch: bool,
    connect: bool,
    hang_at: str,
) -> None:
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=start,
        launch_spatial_analyzer=launch,
        connect_to_spatial_analyzer=connect,
    )
    elapsed, _ = expiry(published=published, options=options, hang_at=hang_at)
    assert elapsed == 120.0


def late(
    *,
    published: discovery_pb2.LifecycleBounds | None,
    at: str = "snapshot",
    to: float = 121.0,
    options: BriosaStartOptions | None = None,
    revision: int = 1,
    yields: int = 1,
) -> tuple[list[str], bool]:
    """Block the loop inside one RPC until ``to`` seconds; return the RPCs sent.

    With one yield the budget's timer is due but has not run when the startup
    continues; with two it has already run.
    """

    async def body(loop: VirtualClockLoop) -> tuple[list[str], bool]:
        fake = ClockedTransport(
            loop,
            published=published,
            revision=revision,
            hang_at="connect-sdk",
            on={at: lambda: setattr(loop, "now", T0 + to)},
            yields=yields,
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client, options)
            return names(fake), fake.closed
        finally:
            await client.stop()

    return run_virtual(body, now=T0)


@pytest.mark.parametrize(
    "published",
    [
        bounds(startup_with_launch=300_000),
        bounds(start_sdk=200_000),
        bounds(),
    ],
    ids=["usable-allowance", "partial-bounds", "empty-bounds"],
)
@pytest.mark.parametrize("to", [120.0, 120.001, 121.0])
def test_late_discovery_never_revives_or_continues_an_expired_startup(
    published: discovery_pb2.LifecycleBounds, to: float
) -> None:
    calls, closed = late(published=published, to=to)
    # Only the snapshot was sent, and the owned server was cleaned up.
    assert calls == ["snapshot"]
    assert closed


def test_late_discovery_with_an_explicit_timeout_submits_no_phase() -> None:
    calls, _ = late(
        published=bounds(startup_with_launch=300_000),
        to=120.001,
        options=BriosaStartOptions(startup_timeout=120.0),
    )
    assert calls == ["snapshot"]


def test_a_timer_that_already_ran_is_not_undone_by_adoption() -> None:
    calls, _ = late(published=bounds(startup_with_launch=300_000), yields=2)
    assert calls == ["snapshot"]


@pytest.mark.parametrize(
    ("at", "sent"),
    [
        ("start-sdk", ["snapshot", "start-sdk"]),
        ("launch-sa", ["snapshot", "start-sdk", "launch-sa"]),
    ],
)
def test_no_later_phase_starts_after_the_budget_ran_out(
    at: str, sent: list[str]
) -> None:
    calls, _ = late(published=bounds(startup_with_launch=300_000), at=at, to=321.0)
    assert calls == sent


def test_server_0_10_0_late_discovery_behaves_as_0_5_0() -> None:
    # Client 0.5.0 sent the next phases before its timer ran; the published
    # 0.5.0 wheel does the same, so this path is unchanged.
    calls, _ = late(published=None, revision=0, to=120.001)
    assert calls[:2] == ["snapshot", "start-sdk"]


def test_an_unschedulable_deadline_keeps_the_bootstrap_deadline() -> None:
    # The loop refuses timers more than 200 s ahead, as Qt's range would.
    elapsed, _ = expiry(
        published=bounds(startup_with_launch=300_000), timer_limit=200.0
    )
    assert elapsed == 120.0


def test_the_largest_allowance_is_armed_when_the_loop_accepts_it() -> None:
    elapsed, _ = expiry(published=bounds(startup_with_launch=4_294_967_295))
    assert elapsed == pytest.approx(4_294_967.295 + 20.0)


def test_adoption_happens_once_and_not_at_the_post_connect_refresh() -> None:
    elapsed, calls = expiry(
        published=bounds(startup_with_launch=300_000),
        later=bounds(startup_with_launch=900_000),
        hang_at="none",
        hang_snapshot=2,
    )
    assert elapsed == 320.0
    assert calls == ["snapshot", "start-sdk", "launch-sa", "connect-sdk", "server-info"]


def test_a_completed_startup_leaves_no_timer_armed() -> None:
    async def body(loop: VirtualClockLoop) -> list[float]:
        fake = ClockedTransport(loop, published=bounds(startup_with_launch=300_000))
        client = create_client(fake)
        await client.start()
        try:
            assert all(timeout is None for _, timeout in fake.calls)
            return loop.armed()
        finally:
            await client.stop()

    assert run_virtual(body, now=T0) == []


def test_caller_cancellation_stays_independent_of_an_adopted_budget() -> None:
    async def body(loop: VirtualClockLoop) -> float:
        fake = ClockedTransport(
            loop, published=bounds(startup_with_launch=300_000), hang_at="connect-sdk"
        )
        client = create_client(fake)
        caller = asyncio.ensure_future(client.start())
        while names(fake)[-1:] != ["connect-sdk"]:
            await asyncio.sleep(0)
        caller.cancel()
        with pytest.raises(asyncio.CancelledError):
            await caller
        try:
            # The startup itself continues under its adopted deadline.
            await expect_startup_timeout(client)
            return loop.time() - T0
        finally:
            await client.stop()

    assert run_virtual(body, now=T0) == 320.0


def test_an_unknown_mode_and_no_host_bound_still_adopt_the_allowance() -> None:
    elapsed, _ = expiry(
        published=bounds(startup_without_launch=250_000),
        options=BriosaStartOptions(launch_spatial_analyzer=False),
    )
    assert elapsed == 270.0


@pytest.mark.parametrize("published", [None, bounds(startup_with_launch=300_000)])
def test_independent_cancellation_in_the_expiry_turn_stays_cancellation(
    published: discovery_pb2.LifecycleBounds | None,
) -> None:
    async def body(loop: VirtualClockLoop) -> None:
        fake = ClockedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            hang_at="connect-sdk",
        )
        client = create_client(fake)
        caller = asyncio.ensure_future(client.start())
        while names(fake)[-1:] != ["connect-sdk"]:
            await asyncio.sleep(0)
        task = client._start_task
        assert task is not None
        deadline = loop.armed()[-1]
        loop.call_at(deadline, task.cancel)
        try:
            with pytest.raises(asyncio.CancelledError):
                await caller
        finally:
            await client.stop()

    run_virtual(body, now=T0)


def test_a_timeout_raised_inside_discovery_is_a_startup_timeout() -> None:
    class Raising(ClockedTransport):
        async def get_server_snapshot(
            self, timeout: float | None = None
        ) -> tuple[
            discovery_pb2.GetServerInfoResponse,
            discovery_pb2.ListCapabilitiesResponse,
        ]:
            raise TimeoutError("raised inside the transport")

    async def body(loop: VirtualClockLoop) -> BriosaStartupError:
        client = create_client(Raising(loop))
        try:
            return await expect_startup_timeout(client)
        finally:
            await client.stop()

    error = run_virtual(body, now=T0)
    assert type(error.__cause__) is TimeoutError
    assert str(error.__cause__) == "raised inside the transport"


def startup_expiry_error() -> BriosaStartupError:
    async def body(loop: VirtualClockLoop) -> BriosaStartupError:
        client = create_client(ClockedTransport(loop, hang_at="connect-sdk"))
        try:
            return await expect_startup_timeout(client)
        finally:
            await client.stop()

    return run_virtual(body, now=T0)


@pytest.mark.skipif(sys.version_info < (3, 11), reason="Python 3.11 and later")
def test_budget_expiry_keeps_the_native_timeout_chain() -> None:
    error = startup_expiry_error()
    assert type(error) is BriosaStartupError
    timeout = error.__cause__
    assert type(timeout) is TimeoutError
    assert error.__context__ is timeout
    assert timeout.__traceback__ is not None
    assert isinstance(timeout.__cause__, asyncio.CancelledError)


@pytest.mark.skipif(sys.version_info >= (3, 11), reason="Python 3.10 only")
def test_python_3_10_expiry_is_both_startup_error_and_asyncio_timeout() -> None:
    error = startup_expiry_error()
    assert isinstance(error, BriosaStartupError)
    assert isinstance(error, asyncio.TimeoutError)
    assert type(error) is not BriosaStartupError
    assert isinstance(error.__cause__, asyncio.CancelledError)
    assert error.diagnostic_code == "startup-timeout"
    assert type(error).__name__ not in briosa.__all__

    async def handled(loop: VirtualClockLoop) -> list[str]:
        caught = []
        for handler in (asyncio.TimeoutError, BriosaStartupError):
            client = create_client(ClockedTransport(loop, hang_at="connect-sdk"))
            try:
                await client.start()
            except handler:
                caught.append(handler.__name__)
            finally:
                await client.stop()
        return caught

    assert run_virtual(handled, now=T0) == ["TimeoutError", "BriosaStartupError"]


def test_stop_during_a_hung_startup_cleans_up_on_the_first_call() -> None:
    async def body(loop: VirtualClockLoop) -> tuple[bool, list[str]]:
        fake = ClockedTransport(loop, hang_at="connect-sdk")
        client = create_client(fake)
        caller = asyncio.ensure_future(client.start())
        while names(fake)[-1:] != ["connect-sdk"]:
            await asyncio.sleep(0)
        await client.stop()
        with pytest.raises(BriosaStartupError):
            await caller
        return fake.closed, names(fake)

    closed, calls = run_virtual(body, now=T0)
    assert closed
    assert calls[-1] == "stop-sdk"


def test_real_loop_blocked_discovery_submits_no_phase_after_expiry() -> None:
    class Blocking(ClockedTransport):
        async def get_server_snapshot(
            self, timeout: float | None = None
        ) -> tuple[
            discovery_pb2.GetServerInfoResponse,
            discovery_pb2.ListCapabilitiesResponse,
        ]:
            self.calls.append(("snapshot", timeout))
            time.sleep(0.05)  # blocks the loop past the 10 ms budget
            return snapshot(False, self._published, self._revision)

    async def body(published: discovery_pb2.LifecycleBounds | None) -> list[str]:
        fake = Blocking(
            asyncio.get_running_loop(),  # type: ignore[arg-type]
            published=published,
            revision=0 if published is None else 1,
            hang_at="connect-sdk",
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(
                client, BriosaStartOptions(startup_timeout=0.01)
            )
            return names(fake)
        finally:
            await client.stop()

    # A server that publishes bounds: no phase after the budget ran out.
    assert asyncio.run(body(bounds(startup_with_launch=300_000))) == ["snapshot"]
    # Server 0.10.0: as client 0.5.0, the next phase is sent before the timer runs.
    assert asyncio.run(body(None))[:2] == ["snapshot", "start-sdk"]


# --- Every handoff of a guarded startup checks the budget ----------------------
#
# A server that publishes lifecycle bounds guards the startup: the client reads
# the clock and the startup task's cancellation before it takes ownership of the
# session, before each request it hands to the transport and before it reports
# success. Against Server 0.10.0 the same sequences run as client 0.5.0's did.

EMPTY = bounds()


class FakeRpcError(grpc.RpcError):
    def __init__(self, status_code: grpc.StatusCode) -> None:
        super().__init__()
        self._status_code = status_code

    def code(self) -> grpc.StatusCode:
        return self._status_code

    def trailing_metadata(self) -> tuple[()]:
        return ()


class GuardedTransport(ClockedTransport):
    """A clocked fake that can reply malformed, stay silent, or count MP calls."""

    def __init__(
        self,
        loop: VirtualClockLoop,
        *,
        silent: frozenset[str] = frozenset(),
        malformed: frozenset[str] = frozenset(),
        **options: Any,
    ) -> None:
        super().__init__(loop, **options)
        # These RPCs return right after their action, without yielding.
        self._silent = silent
        self._malformed = malformed
        self.invocations = 0

    async def _record(self, name: str, timeout: float | None) -> None:
        if name not in self._silent:
            await super()._record(name, timeout)
            return
        self.calls.append((name, timeout))
        action = self._on.pop(name, None)
        if action is not None:
            action()

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
        *,
        checkpoint: StartupCheckpoint | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        if checkpoint is not None:
            await checkpoint()
        state = await super().launch_application(
            options, timeout, checkpoint=checkpoint
        )
        if "launch-sa" in self._malformed:
            state.application_generation = 0
        return state

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message:
        self.invocations += 1
        raise NotImplementedError


def at(loop: VirtualClockLoop, seconds: float) -> Callable[[], None]:
    return lambda: setattr(loop, "now", T0 + seconds)


GUARDED_ORDER = [
    "snapshot",
    "start-sdk",
    "launch-sa",
    "connect-sdk",
    "server-info",
    "list-capabilities",
]


@pytest.mark.parametrize("returns_late", GUARDED_ORDER[1:])
def test_no_request_follows_one_that_returns_after_the_deadline(
    returns_late: str,
) -> None:
    async def body(loop: VirtualClockLoop) -> tuple[list[str], bool, int]:
        fake = GuardedTransport(
            loop,
            published=EMPTY,
            silent=frozenset({returns_late}),
            on={returns_late: at(loop, 121.0)},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client)
            session = client._session
            completed = session is not None and session.startup_completed
            # An MP command right after the rejected start never reaches the
            # transport.
            with pytest.raises(briosa.BriosaLifecycleError) as refused:
                await client.get_active_collection_name()
            assert refused.value.diagnostic_code == "mp-command-admission-closed"
            return names(fake), completed, fake.invocations
        finally:
            await client.stop()

    calls, completed, invocations = run_virtual(body, now=T0)
    assert calls == GUARDED_ORDER[: GUARDED_ORDER.index(returns_late) + 1]
    assert not completed
    assert invocations == 0


def test_server_0_10_0_continues_after_a_late_reply_as_0_5_0() -> None:
    async def body(loop: VirtualClockLoop) -> list[str]:
        fake = GuardedTransport(
            loop,
            published=None,
            revision=0,
            silent=frozenset({"connect-sdk", "snapshot"}),
            on={"connect-sdk": at(loop, 121.0)},
        )
        client = create_client(fake)
        try:
            # Client 0.5.0 sends the post-Connect discovery and reports success.
            await client.start()
            session = client._session
            assert session is not None
            assert session.startup_completed
            return names(fake)
        finally:
            await client.stop()

    calls = run_virtual(body, now=T0)
    assert calls[:5] == [
        "snapshot",
        "start-sdk",
        "launch-sa",
        "connect-sdk",
        "snapshot",
    ]


def test_real_loop_final_request_blocking_past_the_budget_is_a_timeout() -> None:
    async def body() -> bool:
        loop = cast(VirtualClockLoop, asyncio.get_running_loop())
        fake = GuardedTransport(
            loop,
            published=EMPTY,
            silent=frozenset({"list-capabilities"}),
            on={"list-capabilities": lambda: time.sleep(0.05)},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(
                client, BriosaStartOptions(startup_timeout=0.01)
            )
            session = client._session
            return session is not None and session.startup_completed
        finally:
            await client.stop()

    assert not asyncio.run(body())


@pytest.mark.parametrize("published", [EMPTY, None], ids=["guarded", "0.10.0"])
def test_a_lock_released_after_the_deadline_never_takes_ownership(
    published: discovery_pb2.LifecycleBounds | None,
) -> None:
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=False,
        launch_spatial_analyzer=False,
        connect_to_spatial_analyzer=False,
        startup_timeout=10.0,
    )

    async def body(loop: VirtualClockLoop) -> tuple[str, bool, bool]:
        holder: list[BriosaClient] = []
        holders: list[asyncio.Future[None]] = []

        async def hold_lock_past_the_deadline() -> None:
            lock = holder[0]._required_lock()
            await lock.acquire()
            for _ in range(3):
                await asyncio.sleep(0)
            # Released after the deadline, before its timer runs.
            loop.now = T0 + 11.0
            lock.release()

        def hold() -> None:
            holders.append(asyncio.ensure_future(hold_lock_past_the_deadline()))

        fake = GuardedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            on={"snapshot": hold},
        )
        client = create_client(fake)
        holder.append(client)
        try:
            try:
                await client.start(options)
                outcome = "started"
            except BriosaStartupError as error:
                outcome = error.diagnostic_code
            return outcome, client._session is not None, fake.closed
        finally:
            await client.stop()

    outcome, owned, closed = run_virtual(body, now=T0)
    if published is None:
        # Client 0.5.0 published the session and reported success.
        assert (outcome, owned) == ("started", True)
    else:
        # The transport and the owned server close; the client never owned them.
        assert (outcome, owned, closed) == ("startup-timeout", False, True)


@pytest.mark.parametrize("seconds", [181.0, 179.0], ids=["after", "before"])
@pytest.mark.parametrize("failure", ["unavailable", "malformed"])
def test_a_phase_failing_after_the_deadline_is_a_startup_timeout(
    failure: str, seconds: float
) -> None:
    async def body(loop: VirtualClockLoop) -> BaseException:
        def fail() -> None:
            loop.now = T0 + seconds
            if failure == "unavailable":
                raise FakeRpcError(grpc.StatusCode.UNAVAILABLE)

        malformed = frozenset({"launch-sa"} if failure == "malformed" else set())
        fake = GuardedTransport(
            loop,
            published=bounds(startup_with_launch=160_000),
            silent=frozenset({"launch-sa"}),
            malformed=malformed,
            on={"launch-sa": fail},
        )
        client = create_client(fake)
        try:
            with pytest.raises(briosa.BriosaError) as raised:
                await client.start()
            assert names(fake) == ["snapshot", "start-sdk", "launch-sa"]
            return raised.value
        finally:
            await client.stop()

    error = run_virtual(body, now=T0)
    own: type[BaseException] = (
        briosa.BriosaTransportError
        if failure == "unavailable"
        else briosa.BriosaProtocolError
    )
    cause = error
    if seconds < 180.0:
        # Before the adopted 180 s deadline, the failure keeps its own error.
        assert type(error) is own
    else:
        assert isinstance(error, BriosaStartupError)
        assert error.diagnostic_code == "startup-timeout"
        assert error.__cause__ is not None
        cause = error.__cause__
        assert type(cause) is own
    if failure == "unavailable":
        assert isinstance(cause.__cause__, FakeRpcError)


def test_a_failed_transfer_closes_the_transport_and_the_server() -> None:
    class ClosingServer(RecordingServer):
        closed = False

        async def close(self) -> None:
            ClosingServer.closed = True

    class ClosingLauncher:
        async def launch(
            self,
            logging: BriosaLoggingOptions | None = None,
            selection: BriosaServerSelection | None = None,
        ) -> OwnedServer:
            return ClosingServer()

    async def body(loop: VirtualClockLoop) -> tuple[str, bool, bool]:
        closing: list[asyncio.Future[None]] = []
        holder: list[BriosaClient] = []

        def close_client() -> None:
            # aclose() during discovery: the client is finally closed before
            # the startup can take ownership.
            closing.append(asyncio.ensure_future(holder[0].aclose()))

        fake = GuardedTransport(loop, published=EMPTY, on={"snapshot": close_client})
        client = BriosaClient(
            _server_launcher=ClosingLauncher(), _transport_factory=lambda _target: fake
        )
        holder.append(client)
        with pytest.raises(briosa.BriosaLifecycleError) as refused:
            await client.start()
        await closing[0]
        return refused.value.diagnostic_code, fake.closed, client._session is None

    code, transport_closed, unowned = run_virtual(body, now=T0)
    assert code == "client-finally-closed"
    assert transport_closed
    assert unowned
    assert ClosingServer.closed


def cancel_start(client: BriosaClient) -> None:
    task = client._start_task
    assert task is not None
    task.cancel()


@pytest.mark.parametrize("published", [EMPTY, None], ids=["guarded", "0.10.0"])
def test_a_cancellation_queued_before_discovery_resumes(
    published: discovery_pb2.LifecycleBounds | None,
) -> None:
    async def body(loop: VirtualClockLoop) -> tuple[list[str], bool]:
        holder: list[BriosaClient] = []

        def queue() -> None:
            # Queued now, so it runs once discovery's reply is due.
            loop.call_soon(cancel_start, holder[0])

        fake = GuardedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            hang_at="connect-sdk",
            on={"snapshot": queue},
        )
        client = create_client(fake)
        holder.append(client)
        try:
            with pytest.raises(asyncio.CancelledError):
                await client.start()
            return names(fake), client._session is not None
        finally:
            await client.stop()

    calls, owned = run_virtual(body, now=T0)
    if published is not None or sys.version_info >= (3, 12):
        assert (calls, owned) == (["snapshot"], False)
    else:
        # Client 0.5.0 on Python 3.10 and 3.11 sent Start SDK first.
        assert (calls, owned) == (["snapshot", "start-sdk"], True)


@pytest.mark.parametrize("effect", ["cancel", "clock"])
@pytest.mark.parametrize("published", [EMPTY, None], ids=["guarded", "0.10.0"])
def test_reading_the_launch_options_cannot_act_after_the_last_check(
    published: discovery_pb2.LifecycleBounds | None, effect: str
) -> None:
    async def body(loop: VirtualClockLoop) -> list[str]:
        holder: list[BriosaClient] = []
        armed: list[bool] = []

        class Options(BriosaStartOptions):
            @property
            def launch_options(self) -> SpatialAnalyzerLaunchOptions:
                if armed:
                    armed.clear()
                    if effect == "cancel":
                        cancel_start(holder[0])
                    else:
                        loop.now = T0 + 121.0
                return cast(SpatialAnalyzerLaunchOptions, self.__dict__["launch"])

            @launch_options.setter
            def launch_options(self, value: SpatialAnalyzerLaunchOptions) -> None:
                self.__dict__["launch"] = value

        options = Options()
        armed.append(True)
        fake = GuardedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            hang_at="connect-sdk",
        )
        client = create_client(fake)
        holder.append(client)
        try:
            with pytest.raises((asyncio.CancelledError, BriosaStartupError)):
                await client.start(options)
            return names(fake)
        finally:
            await client.stop()

    calls = run_virtual(body, now=T0)
    if published is None:
        assert "launch-sa" in calls
    else:
        assert calls == ["snapshot", "start-sdk"]


LAUNCH_FIELDS = ["job_file_path", "quick_start_instrument_name", "start_minimized"]


def test_subclassed_launch_options_are_read_once_before_the_check() -> None:
    reads: list[str] = []

    @dataclass(frozen=True)
    class Counted(SpatialAnalyzerLaunchOptions):
        def __getattribute__(self, name: str) -> Any:
            if name in LAUNCH_FIELDS:
                reads.append(name)
            return super().__getattribute__(name)

    received: list[SpatialAnalyzerLaunchOptions] = []

    class Receiving(GuardedTransport):
        async def launch_application(
            self,
            options: SpatialAnalyzerLaunchOptions,
            timeout: float | None = None,
            *,
            checkpoint: StartupCheckpoint | None = None,
        ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
            if checkpoint is not None:
                await checkpoint()
            received.append(options)
            return await super().launch_application(
                options, timeout, checkpoint=checkpoint
            )

    async def body(loop: VirtualClockLoop) -> None:
        client = create_client(Receiving(loop, published=EMPTY))
        try:
            launch = Counted(start_minimized=True)
            reads.clear()
            await client.start(BriosaStartOptions(launch_options=launch))
        finally:
            await client.stop()

    run_virtual(body, now=T0)
    assert sorted(reads) == sorted(LAUNCH_FIELDS)
    assert type(received[0]) is SpatialAnalyzerLaunchOptions
    assert received[0] == SpatialAnalyzerLaunchOptions(start_minimized=True)


def test_a_reflected_default_is_an_explicit_timeout() -> None:
    reflected = inspect.signature(BriosaStartOptions).parameters["startup_timeout"]
    field_default = next(
        item.default
        for item in dataclasses.fields(BriosaStartOptions)
        if item.name == "startup_timeout"
    )
    for value in (reflected.default, field_default):
        assert type(value) is float
        assert value == 120.0
        elapsed, _ = expiry(
            published=bounds(startup_with_launch=300_000),
            options=BriosaStartOptions(startup_timeout=value),
        )
        assert elapsed == 120.0


def fail_registrations(loop: VirtualClockLoop, which: str) -> Callable[[], None]:
    """From discovery on, make the chosen timer registrations raise."""

    def arm() -> None:
        count = [0]

        def hook(when: float) -> None:
            count[0] += 1
            if which == "every" or str(count[0]) == which:
                raise OSError("the loop cannot arm this timer")

        loop.on_call_at = hook

    return arm


@pytest.mark.parametrize(
    ("which", "deadline"), [("1", 120.0), ("2", 320.0), ("every", 120.0)]
)
def test_a_failed_registration_keeps_the_bootstrap_deadline(
    which: str, deadline: float
) -> None:
    async def body(loop: VirtualClockLoop) -> tuple[float, list[float]]:
        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at="connect-sdk",
            on={"snapshot": fail_registrations(loop, which)},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client)
            return loop.time() - T0, loop.armed()
        finally:
            loop.on_call_at = None
            await client.stop()

    elapsed, armed = run_virtual(body, now=T0)
    assert elapsed == deadline
    assert armed == []


def test_adoption_registers_one_timer_and_then_drops_the_bootstrap() -> None:
    async def body(loop: VirtualClockLoop) -> tuple[int, list[float]]:
        registered: list[int] = []

        def count() -> None:
            registered.append(loop.registrations)

        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at="connect-sdk",
            on={"snapshot": count, "start-sdk": count},
        )
        client = create_client(fake)
        caller = asyncio.ensure_future(client.start())
        while names(fake)[-1:] != ["connect-sdk"]:
            await asyncio.sleep(0)
        armed = loop.armed()
        with pytest.raises(BriosaStartupError):
            await caller
        await client.stop()
        return registered[1] - registered[0], armed

    added, armed = run_virtual(body, now=T0)
    # One registration, for the adopted deadline; the bootstrap timer is gone.
    assert added == 1
    assert armed == [T0 + 320.0]


def test_a_clock_that_passes_the_deadline_during_registration_never_revives() -> None:
    async def body(loop: VirtualClockLoop) -> tuple[float, list[str], bool, bool]:
        def arm() -> None:
            loop.on_call_at = lambda when: setattr(loop, "now", T0 + 121.0)

        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at="connect-sdk",
            on={"snapshot": arm},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client)
            loop.on_call_at = None
            return loop.time() - T0, names(fake), client._session is None, fake.closed
        finally:
            loop.on_call_at = None
            await client.stop()

    elapsed, calls, unowned, closed = run_virtual(body, now=T0)
    assert elapsed == 121.0
    assert calls == ["snapshot"]
    assert unowned
    assert closed


@pytest.mark.parametrize("end", ["success", "timeout", "stop"])
def test_no_timer_is_left_armed_after_an_adopted_startup(end: str) -> None:
    async def body(loop: VirtualClockLoop) -> list[float]:
        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at=None if end == "success" else "connect-sdk",
        )
        client = create_client(fake)
        if end == "success":
            await client.start()
        elif end == "timeout":
            await expect_startup_timeout(client)
        else:
            caller = asyncio.ensure_future(client.start())
            while names(fake)[-1:] != ["connect-sdk"]:
                await asyncio.sleep(0)
            await client.stop()
            with pytest.raises(BriosaStartupError):
                await caller
        await client.stop()
        return loop.armed()

    assert run_virtual(body, now=T0) == []


class WrittenOnPython310:
    """Reduces as the Python 3.10 startup-timeout error does."""

    def __reduce__(self) -> tuple[Any, ...]:
        return (
            _startup_timeout_error,
            ("startup-timeout",),
            {"diagnostic_code": "startup-timeout"},
        )


def test_a_python_3_10_expiry_pickle_loads_on_every_version() -> None:
    loaded = pickle.loads(pickle.dumps(WrittenOnPython310(), protocol=4))
    assert isinstance(loaded, BriosaStartupError)
    assert str(loaded) == "Briosa startup failed (startup-timeout)."
    assert loaded.args == ("Briosa startup failed (startup-timeout).",)
    assert loaded.diagnostic_code == "startup-timeout"
    assert loaded.__cause__ is None
    if sys.version_info >= (3, 11):
        assert type(loaded) is BriosaStartupError
    else:
        assert isinstance(loaded, asyncio.TimeoutError)


@pytest.mark.skipif(sys.version_info >= (3, 11), reason="Python 3.10 only")
def test_python_3_10_expiry_round_trips_through_pickle_and_copy() -> None:
    error = startup_expiry_error()
    assert pickle.dumps(error, protocol=4) == pickle.dumps(
        WrittenOnPython310(), protocol=4
    )
    clones: tuple[BriosaStartupError, ...] = (
        pickle.loads(pickle.dumps(error)),
        copy.copy(error),
        copy.deepcopy(error),
    )
    for clone in clones:
        assert type(clone) is type(error)
        assert isinstance(cast(object, clone), asyncio.TimeoutError)
        assert str(clone) == str(error) == "Briosa startup failed (startup-timeout)."
        assert clone.args == error.args
        assert clone.diagnostic_code == "startup-timeout"
        assert clone.__cause__ is None


# --- A guarded startup's failures, requests and cleanup ------------------------


def test_a_failed_guarded_startup_admits_no_mp_command_for_its_session() -> None:
    functions = facade_functions()

    async def body(loop: VirtualClockLoop) -> tuple[int, int, int]:
        fake = GuardedTransport(
            loop,
            published=EMPTY,
            silent=frozenset({"list-capabilities"}),
            on={"list-capabilities": at(loop, 121.0)},
        )
        client = create_client(fake)
        await expect_startup_timeout(client)
        # Every diagnostic read succeeds and reports a ready server and SDK,
        # and none of them reopens MP admission.
        snapshot = await client.get_server_snapshot()
        sdk = await client.get_spatial_analyzer_sdk_state()
        await client.get_spatial_analyzer_state()
        await client.list_capabilities()
        await client.list_capabilities(include_denied=True)
        assert snapshot.ready_for_mp
        assert sdk.ready_for_mp
        refused = 0
        for operation_id, facade in bound_facades(client).items():
            with pytest.raises(briosa.BriosaLifecycleError) as raised:
                await facade(**required_arguments(functions[operation_id]))
            assert raised.value.diagnostic_code == "mp-command-admission-closed"
            refused += 1
        before = fake.invocations
        # Only a new session admits commands again.
        await client.stop()
        await client.start()
        with pytest.raises(NotImplementedError):
            await client.get_active_collection_name()
        after = fake.invocations
        await client.stop()
        return refused, before, after

    refused, before, after = run_virtual(body, now=T0)
    assert refused == len(functions)
    assert before == 0
    assert after == 1


def run_launch_probe(*, pure_python: bool) -> dict[str, Any]:
    if not pure_python:
        return guarded_launch_probe.probe()
    environment = dict(os.environ, PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION="python")
    completed = subprocess.run(
        [sys.executable, str(Path(guarded_launch_probe.__file__))],
        capture_output=True,
        check=True,
        env=environment,
        text=True,
        timeout=300,
    )
    return cast(dict[str, Any], json.loads(completed.stdout))


@pytest.mark.parametrize("pure_python", [True, False], ids=["python", "default"])
def test_a_launch_request_is_built_before_the_last_check(pure_python: bool) -> None:
    result = run_launch_probe(pure_python=pure_python)
    if pure_python:
        assert result["protobuf"] == "python"
    # A str subclass value is copied before the request is built, so neither
    # building nor serializing it runs its encode().
    text = result["text"]
    assert text["ran"] == []
    assert text["outcome"] == "started"
    assert "LaunchSpatialAnalyzer@0" in text["calls"]
    assert text["instrument_types"] == ["str"]
    # A value that runs code while the request is built, and spends the budget
    # there, is caught by the check that follows: Launch never reaches the stub.
    flag = result["bool"]
    assert flag["ran"] == ["bool"]
    assert flag["outcome"] == "BriosaStartupError(startup-timeout)"
    assert not any(call.startswith("LaunchSpatialAnalyzer") for call in flag["calls"])


@pytest.mark.parametrize("published", [EMPTY, None], ids=["guarded", "0.10.0"])
def test_cancelling_the_running_task_from_a_launch_options_getter(
    published: discovery_pb2.LifecycleBounds | None,
) -> None:
    async def body(loop: VirtualClockLoop) -> list[str]:
        armed: list[bool] = []

        class Options(BriosaStartOptions):
            @property
            def launch_options(self) -> SpatialAnalyzerLaunchOptions:
                if armed:
                    armed.clear()
                    task = asyncio.current_task()
                    assert task is not None
                    task.cancel()
                return cast(SpatialAnalyzerLaunchOptions, self.__dict__["launch"])

            @launch_options.setter
            def launch_options(self, value: SpatialAnalyzerLaunchOptions) -> None:
                self.__dict__["launch"] = value

        options = Options()
        armed.append(True)
        fake = GuardedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            hang_at="connect-sdk",
        )
        client = create_client(fake)
        try:
            with pytest.raises(asyncio.CancelledError):
                await client.start(options)
            return names(fake)
        finally:
            await client.stop()

    calls = run_virtual(body, now=T0)
    if published is None:
        # Client 0.5.0 sends Launch before the cancellation arrives.
        assert calls[:3] == ["snapshot", "start-sdk", "launch-sa"]
    else:
        assert calls == ["snapshot", "start-sdk"]


class ClosingServer(RecordingServer):
    def __init__(self, raises: bool) -> None:
        self.raises = raises
        self.closed = False

    async def close(self) -> None:
        self.closed = True
        if self.raises:
            raise OSError("the owned server could not be closed")


@pytest.mark.parametrize(
    ("transport_raises", "server_raises"),
    [(True, False), (False, True), (True, True)],
    ids=["transport", "server", "both"],
)
def test_a_failed_cleanup_never_replaces_the_startup_failure(
    transport_raises: bool, server_raises: bool
) -> None:
    server = ClosingServer(server_raises)

    class Launcher:
        async def launch(
            self,
            logging: BriosaLoggingOptions | None = None,
            selection: BriosaServerSelection | None = None,
        ) -> OwnedServer:
            return server

    class Failing(GuardedTransport):
        async def close(self) -> None:
            await super().close()
            if transport_raises:
                raise OSError("the transport could not be closed")

    async def body(loop: VirtualClockLoop) -> tuple[BriosaStartupError, bool]:
        # Discovery returns after the deadline, so the startup fails before
        # the client takes ownership.
        fake = Failing(
            loop,
            published=EMPTY,
            silent=frozenset({"snapshot"}),
            on={"snapshot": at(loop, 121.0)},
        )
        client = BriosaClient(
            _server_launcher=Launcher(), _transport_factory=lambda _target: fake
        )
        error = await expect_startup_timeout(client)
        assert client._session is None
        await client.stop()
        return error, fake.closed

    error, transport_closed = run_virtual(body, now=T0)
    assert transport_closed
    assert server.closed
    notes = list(getattr(error, "__notes__", ()))
    expected = []
    if transport_raises:
        expected.append(
            "Closing the transport after this startup failure also failed (OSError)."
        )
    if server_raises:
        expected.append(
            "Closing the owned server after this startup failure also failed (OSError)."
        )
    assert notes == expected


@pytest.mark.parametrize(
    "error", [OSError, RuntimeError, ValueError, OverflowError, KeyError]
)
def test_any_registration_failure_keeps_the_bootstrap_deadline(
    error: type[Exception],
) -> None:
    async def body(loop: VirtualClockLoop) -> tuple[float, list[str]]:
        def arm() -> None:
            def hook(when: float) -> None:
                raise error("this loop cannot arm the timer")

            loop.on_call_at = hook

        fake = ClockedTransport(
            loop,
            published=bounds(startup_with_launch=300_000),
            hang_at="connect-sdk",
            on={"snapshot": arm},
        )
        client = create_client(fake)
        try:
            await expect_startup_timeout(client)
            return loop.time() - T0, names(fake)
        finally:
            loop.on_call_at = None
            await client.stop()

    elapsed, calls = run_virtual(body, now=T0)
    assert elapsed == 120.0
    assert calls == ["snapshot", "start-sdk", "launch-sa", "connect-sdk"]


@pytest.mark.parametrize(
    ("published", "seconds"),
    [
        (bounds(startup_with_launch=160_000), 0.0),
        (bounds(startup_with_launch=160_000), 181.0),
        (None, 0.0),
    ],
    ids=["guarded-before", "guarded-after", "0.10.0"],
)
def test_a_phase_timeout_is_a_startup_timeout_only_once_the_budget_ran_out(
    published: discovery_pb2.LifecycleBounds | None, seconds: float
) -> None:
    raised = TimeoutError("raised by the launch transport")

    async def body(loop: VirtualClockLoop) -> BaseException:
        def fail() -> None:
            loop.now = T0 + seconds
            raise raised

        fake = GuardedTransport(
            loop,
            published=published,
            revision=0 if published is None else 1,
            silent=frozenset({"launch-sa"}),
            on={"launch-sa": fail},
        )
        client = create_client(fake)
        try:
            with pytest.raises(Exception) as caught:
                await client.start()
            return caught.value
        finally:
            await client.stop()

    error = run_virtual(body, now=T0)
    if published is not None and seconds < 180.0:
        # Before the adopted 180 s deadline the phase keeps its own error.
        assert error is raised
    else:
        # After the deadline, and against Server 0.10.0 as with client 0.5.0,
        # it is a startup timeout caused by the phase's TimeoutError.
        assert isinstance(error, BriosaStartupError)
        assert error.diagnostic_code == "startup-timeout"
        assert error.__cause__ is raised
