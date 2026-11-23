"""Startup budget and lifecycle deadline tests.

Pins the client startup budget against the server's default lifecycle bounds
(spatialanalyzer/briosa main 0c7ff7a; #298 and #315), pins that budget expiry is
reported as startup-timeout whichever phase it interrupts, and pins that
lifecycle calls carry no client-imposed per-call deadline.

The adoption tests drive a controllable startup clock through every branch of
the shared rule "Startup budget from published lifecycle bounds"
(docs/architecture/client-library-behavioral-contract.md, briosa#400).
"""

from __future__ import annotations

import asyncio
import copy
import inspect
import pickle
from collections.abc import Callable
from dataclasses import replace
from typing import Any

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
from briosa.client import (
    OwnedServer,
    _schedulable,
    _StartupBudgetExpired,
    _StartupDeadline,
)
from briosa.models import _startup_timeout_omitted
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
    assert isinstance(BriosaStartOptions().startup_timeout, float)
    assert repr(BriosaStartOptions().startup_timeout) == "120.0"


def test_an_omitted_budget_is_told_apart_from_an_explicit_one() -> None:
    omitted = BriosaStartOptions()
    assert _startup_timeout_omitted(omitted)
    assert _startup_timeout_omitted(replace(omitted, launch_spatial_analyzer=False))
    assert _startup_timeout_omitted(copy.deepcopy(omitted))
    assert _startup_timeout_omitted(pickle.loads(pickle.dumps(omitted)))
    for explicit in (120.0, 120, 300.0, 0.5):
        options = BriosaStartOptions(startup_timeout=explicit)
        assert not _startup_timeout_omitted(options)
        assert options.startup_timeout == explicit
        assert not _startup_timeout_omitted(replace(omitted, startup_timeout=explicit))


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
    transport: RecordingTransport,
    options: BriosaClientOptions | None = None,
    clock: FakeClock | None = None,
) -> BriosaClient:
    return BriosaClient(
        options,
        _server_launcher=RecordingLauncher(),
        _transport_factory=lambda _target: transport,
        _startup_clock=clock,
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

    async def list_capabilities(
        self, *, include_denied: bool = False, timeout: float | None = None
    ) -> discovery_pb2.ListCapabilitiesResponse:
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


# --- Adoption of the published startup allowance (Server 0.10.1 and later) ---


class FakeTimer:
    def __init__(self, when: float, callback: Callable[[], None]) -> None:
        self.when = when
        self.callback = callback
        self.cancelled = False
        self.fired = False

    def cancel(self) -> None:
        self.cancelled = True


class FakeClock:
    """A controllable monotonic startup clock.

    Due timers run through the event loop, as the loop's own timers do, so a
    timer never fires in the middle of the startup task's synchronous work.
    """

    def __init__(self, now: float = 0.0) -> None:
        self.now = now
        self.timers: list[FakeTimer] = []

    def __call__(self, _loop: asyncio.AbstractEventLoop) -> FakeClock:
        return self

    def time(self) -> float:
        return self.now

    def call_at(self, when: float, callback: Callable[[], None]) -> FakeTimer:
        timer = FakeTimer(when, callback)
        self.timers.append(timer)
        return timer

    def set(self, now: float) -> None:
        """Move the clock without running due timers yet."""
        self.now = now

    def advance(self, now: float) -> None:
        self.now = now
        loop = asyncio.get_running_loop()
        for timer in self.timers:
            if not timer.cancelled and not timer.fired and timer.when <= now:
                timer.fired = True
                loop.call_soon(timer.callback)

    @property
    def armed(self) -> list[float]:
        return [t.when for t in self.timers if not t.cancelled and not t.fired]

    @property
    def scheduled(self) -> list[float]:
        return [timer.when for timer in self.timers]


def bounds(**milliseconds: int) -> discovery_pb2.LifecycleBounds:
    return discovery_pb2.LifecycleBounds(
        **{f"{name}_milliseconds": value for name, value in milliseconds.items()}  # type: ignore[arg-type]
    )


class ClockedTransport(RecordingTransport):
    """A Server 0.10.1-like transport whose RPCs suspend and can move the clock."""

    def __init__(
        self,
        clock: FakeClock,
        *,
        published: discovery_pb2.LifecycleBounds | None = None,
        later: discovery_pb2.LifecycleBounds | None = None,
        revision: int = 1,
        hang_at: str | None = None,
        on: dict[str, Callable[[], None]] | None = None,
    ) -> None:
        super().__init__(hang_at=hang_at)
        self.hang_at = hang_at
        self._clock = clock
        self._published = published
        self._later = later
        self._revision = revision
        self._on = dict(on or {})
        self._snapshots = 0

    async def _record(self, name: str, timeout: float | None) -> None:
        action = self._on.pop(name, None)
        if action is not None:
            action()
        if self._recording:
            self.calls.append((name, timeout))
        # A real RPC suspends the task, which lets a due timer run first.
        await asyncio.sleep(0)
        if name == self.hang_at:
            await asyncio.Event().wait()

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        await self._record("snapshot", timeout)
        self._snapshots += 1
        published = self._published if self._snapshots == 1 else self._later
        return snapshot(self._connected, published, self._revision)


async def settle(condition: Callable[[], bool]) -> None:
    for _ in range(200):
        if condition():
            return
        await asyncio.sleep(0)
    raise AssertionError("The startup did not reach the expected point.")


async def start_until_hang(
    transport: ClockedTransport,
    clock: FakeClock,
    options: BriosaStartOptions | None = None,
) -> tuple[BriosaClient, asyncio.Task[None]]:
    client = create_client(transport, clock=clock)
    task = asyncio.create_task(client.start(options))
    hang = transport.hang_at
    await settle(lambda: bool(transport.calls) and transport.calls[-1][0] == hang)
    return client, task


async def expect_expiry_at(
    clock: FakeClock, task: asyncio.Task[None], deadline: float
) -> None:
    clock.advance(deadline - 0.001)
    for _ in range(20):
        await asyncio.sleep(0)
    assert not task.done(), "The startup expired before its deadline."
    clock.advance(deadline)
    with pytest.raises(BriosaStartupError) as raised:
        await task
    assert raised.value.diagnostic_code == "startup-timeout"
    assert isinstance(raised.value.__cause__, TimeoutError)


SERVER_0_10_1_DEFAULTS = bounds(
    start_sdk=45_000,
    launch_spatial_analyzer=30_000,
    connect_spatial_analyzer=60_000,
    startup_with_launch=100_000,
    startup_without_launch=70_000,
)


async def test_server_0_10_0_keeps_the_fixed_two_minute_budget() -> None:
    clock = FakeClock()
    transport = ClockedTransport(clock, revision=0, hang_at="connect-sdk")
    client, task = await start_until_hang(transport, clock)
    try:
        assert clock.scheduled == [120.0]
        await expect_expiry_at(clock, task, 120.0)
        assert [name for name, _ in transport.calls] == [
            "snapshot",
            "start-sdk",
            "launch-sa",
            "connect-sdk",
        ]
    finally:
        await client.stop()


async def test_server_0_10_1_defaults_keep_the_two_minute_floor() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock, published=SERVER_0_10_1_DEFAULTS, hang_at="connect-sdk"
    )
    client, task = await start_until_hang(transport, clock)
    try:
        # 100 s + 20 s is exactly the floor, so the bootstrap timer stays.
        assert clock.scheduled == [120.0]
        await expect_expiry_at(clock, task, 120.0)
    finally:
        await client.stop()


async def test_a_larger_published_allowance_lengthens_an_omitted_budget() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock, published=bounds(startup_with_launch=300_000), hang_at="connect-sdk"
    )
    client, task = await start_until_hang(transport, clock)
    try:
        assert clock.armed == [320.0]
        await expect_expiry_at(clock, task, 320.0)
    finally:
        await client.stop()


async def test_the_new_deadline_counts_from_the_start_instant() -> None:
    clock = FakeClock(now=1_000.0)
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        hang_at="connect-sdk",
        on={"snapshot": lambda: clock.advance(1_010.0)},
    )
    client, task = await start_until_hang(transport, clock)
    try:
        # t0 + max(120, 300 + 20), not the time of discovery + 320.
        assert clock.armed == [1_320.0]
        await expect_expiry_at(clock, task, 1_320.0)
    finally:
        await client.stop()


@pytest.mark.parametrize("explicit", [120.0, 200.0, 30.0])
async def test_an_explicit_timeout_always_wins(explicit: float) -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock, published=bounds(startup_with_launch=300_000), hang_at="connect-sdk"
    )
    client, task = await start_until_hang(
        transport, clock, BriosaStartOptions(startup_timeout=explicit)
    )
    try:
        assert clock.scheduled == [explicit]
        await expect_expiry_at(clock, task, explicit)
    finally:
        await client.stop()


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
async def test_the_allowance_follows_the_selected_actions(
    start: bool, launch: bool, connect: bool, hang_at: str, deadline: float
) -> None:
    clock = FakeClock()
    transport = ClockedTransport(clock, published=ALLOWANCES, hang_at=hang_at)
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=start,
        launch_spatial_analyzer=launch,
        connect_to_spatial_analyzer=connect,
    )
    client, task = await start_until_hang(transport, clock, options)
    try:
        assert clock.armed == [deadline]
        await expect_expiry_at(clock, task, deadline)
    finally:
        await client.stop()


async def test_no_selected_server_phase_keeps_the_bootstrap_deadline() -> None:
    clock = FakeClock()
    transport = ClockedTransport(clock, published=ALLOWANCES)
    client = create_client(transport, clock=clock)
    await client.start(
        BriosaStartOptions(
            start_spatial_analyzer_sdk=False,
            launch_spatial_analyzer=False,
            connect_to_spatial_analyzer=False,
        )
    )
    try:
        assert clock.scheduled == [120.0]
        assert clock.armed == []
    finally:
        await client.stop()


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
async def test_a_missing_or_zero_allowance_keeps_the_bootstrap_deadline(
    published: discovery_pb2.LifecycleBounds,
    start: bool,
    launch: bool,
    connect: bool,
    hang_at: str,
) -> None:
    clock = FakeClock()
    transport = ClockedTransport(clock, published=published, hang_at=hang_at)
    options = BriosaStartOptions(
        start_spatial_analyzer_sdk=start,
        launch_spatial_analyzer=launch,
        connect_to_spatial_analyzer=connect,
    )
    client, task = await start_until_hang(transport, clock, options)
    try:
        assert clock.scheduled == [120.0]
        await expect_expiry_at(clock, task, 120.0)
    finally:
        await client.stop()


async def test_late_discovery_never_revives_an_expired_startup() -> None:
    # The snapshot arrives at 121 s, before the 120 s timer has run. A 300 s
    # allowance must not extend the budget, and no phase is submitted.
    clock = FakeClock()
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        on={"snapshot": lambda: clock.set(121.0)},
    )
    client = create_client(transport, clock=clock)
    try:
        with pytest.raises(BriosaStartupError) as raised:
            await client.start()
        assert raised.value.diagnostic_code == "startup-timeout"
        assert isinstance(raised.value.__cause__, TimeoutError)
        assert [name for name, _ in transport.calls] == ["snapshot"]
        assert clock.armed == []
        assert len(clock.scheduled) == 1
    finally:
        await client.stop()


async def test_discovery_exactly_at_the_deadline_has_expired() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        on={"snapshot": lambda: clock.set(120.0)},
    )
    client = create_client(transport, clock=clock)
    try:
        with pytest.raises(BriosaStartupError, match="startup-timeout"):
            await client.start()
        assert [name for name, _ in transport.calls] == ["snapshot"]
    finally:
        await client.stop()


async def test_a_timer_that_already_fired_is_not_undone_by_adoption() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        on={"snapshot": lambda: clock.advance(121.0)},
    )
    client = create_client(transport, clock=clock)
    try:
        with pytest.raises(BriosaStartupError, match="startup-timeout"):
            await client.start()
        assert [name for name, _ in transport.calls] == ["snapshot"]
        assert len(clock.scheduled) == 1
    finally:
        await client.stop()


async def test_an_unschedulable_deadline_keeps_the_bootstrap_deadline(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    delays: list[float] = []

    def refuse(delay: float) -> bool:
        delays.append(delay)
        return False

    monkeypatch.setattr("briosa.client._schedulable", refuse)
    clock = FakeClock()
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        hang_at="connect-sdk",
        on={"snapshot": lambda: clock.advance(5.0)},
    )
    client, task = await start_until_hang(transport, clock)
    try:
        # The check sees deadline - now, and no clamped timer is scheduled.
        assert delays == [315.0]
        assert clock.scheduled == [120.0]
        await expect_expiry_at(clock, task, 120.0)
    finally:
        await client.stop()


def test_only_a_finite_delay_can_be_scheduled() -> None:
    assert _schedulable(4_294_987.295)
    assert not _schedulable(float("inf"))
    assert not _schedulable(float("nan"))


async def test_adoption_happens_once_and_not_at_the_post_connect_refresh() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock,
        published=bounds(startup_with_launch=300_000),
        later=bounds(startup_with_launch=900_000),
    )
    client = create_client(transport, clock=clock)
    await client.start()
    try:
        assert [name for name, _ in transport.calls] == [
            "snapshot",
            "start-sdk",
            "launch-sa",
            "connect-sdk",
            "snapshot",
        ]
        assert clock.scheduled == [120.0, 320.0]
        assert clock.armed == []
        assert all(timeout is None for _, timeout in transport.calls)
    finally:
        await client.stop()


async def test_a_completed_startup_cancels_its_timer() -> None:
    clock = FakeClock()
    transport = ClockedTransport(clock, published=bounds(startup_with_launch=300_000))
    client = create_client(transport, clock=clock)
    await client.start()
    try:
        assert all(timer.cancelled for timer in clock.timers)
        clock.advance(10_000.0)
        await asyncio.sleep(0)
        assert (await client.get_server_snapshot()).ready_for_mp
    finally:
        await client.stop()


async def test_caller_cancellation_stays_independent_of_an_adopted_budget() -> None:
    clock = FakeClock()
    transport = ClockedTransport(
        clock, published=bounds(startup_with_launch=300_000), hang_at="connect-sdk"
    )
    client = create_client(transport, clock=clock)
    caller = asyncio.create_task(client.start())
    await settle(
        lambda: bool(transport.calls) and transport.calls[-1][0] == "connect-sdk"
    )
    caller.cancel()
    with pytest.raises(asyncio.CancelledError):
        await caller
    try:
        # The startup itself continues under its adopted deadline.
        waiter = asyncio.create_task(client.start())
        await asyncio.sleep(0)
        assert clock.armed == [320.0]
        await expect_expiry_at(clock, waiter, 320.0)
    finally:
        await client.stop()


async def test_an_unknown_mode_and_no_host_bound_still_adopt_the_allowance() -> None:
    clock = FakeClock()
    published = bounds(startup_without_launch=250_000)
    transport = ClockedTransport(clock, published=published, hang_at="connect-sdk")
    client, task = await start_until_hang(
        transport, clock, BriosaStartOptions(launch_spatial_analyzer=False)
    )
    try:
        assert clock.armed == [270.0]
        await expect_expiry_at(clock, task, 270.0)
    finally:
        await client.stop()


class DeadlineTask:
    def __init__(self) -> None:
        self.cancel_requests = 0

    def cancel(self) -> bool:
        self.cancel_requests += 1
        return True


def deadline_for(clock: FakeClock, budget: float) -> tuple[Any, DeadlineTask]:
    task = DeadlineTask()
    return _StartupDeadline(clock, task, budget), task  # type: ignore[arg-type]


def test_a_new_deadline_already_past_expires_immediately() -> None:
    clock = FakeClock()
    deadline, _task = deadline_for(clock, 500.0)
    clock.set(130.0)
    with pytest.raises(_StartupBudgetExpired):
        deadline.adopt(50.0)
    assert deadline.expired
    assert clock.armed == []


def test_adoption_never_shortens_or_touches_a_finished_or_expired_budget() -> None:
    clock = FakeClock()
    longer, _ = deadline_for(clock, 500.0)
    longer.adopt(200.0)
    assert longer.deadline == 500.0
    finished, _ = deadline_for(clock, 120.0)
    finished.finish()
    finished.adopt(300.0)
    assert finished.deadline == 120.0
    expired, task = deadline_for(clock, 120.0)
    expired._expire()
    assert task.cancel_requests == 1
    expired.adopt(300.0)
    expired._expire()
    assert expired.deadline == 120.0
    assert task.cancel_requests == 1
    once, _ = deadline_for(clock, 120.0)
    once.adopt(None)
    once.adopt(300.0)
    assert once.deadline == 120.0
    assert [timer.when for timer in clock.timers] == [500.0, 120.0, 120.0, 120.0]
