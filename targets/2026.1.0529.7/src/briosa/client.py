"""Idiomatic asynchronous orchestration over Briosa's private gRPC transport."""

from __future__ import annotations

import asyncio
import math
import os
import socket
import subprocess
import sys
from collections.abc import Awaitable, Callable
from contextlib import suppress
from dataclasses import dataclass, field
from datetime import timedelta
from types import TracebackType
from typing import Any, Protocol, TypeVar, cast

import grpc

from briosa.errors import (
    BriosaError,
    BriosaLifecycleError,
    BriosaStartupError,
)
from briosa.installation_discovery import read_installation, resolve_installation
from briosa.installation_models import BriosaInstallation, BriosaServerSelection
from briosa.logging_options import BriosaLoggingOptions
from briosa.models import (
    BriosaCapabilityListing,
    BriosaClientOptions,
    BriosaLifecycleBounds,
    BriosaServerSnapshot,
    BriosaStartOptions,
    MpCompletionObserver,
    SpatialAnalyzerLaunchOptions,
    SpatialAnalyzerLifecycleState,
    SpatialAnalyzerSdkLifecycleState,
    SpatialAnalyzerSdkRecoveryMode,
    SpatialAnalyzerSdkState,
    _startup_timeout_omitted,
)
from briosa.operation_protocol import (
    build_request,
    map_mp_completion,
    map_response,
    operation_method,
    response_type,
)
from briosa.transport import (
    ClientTransport,
    GrpcClientTransport,
    map_application_state,
    map_capability_listing,
    map_rpc_error,
    map_sdk_state,
    map_snapshot,
    validate_installation,
)
from briosa.wave_a_operations import WaveAOperationsMixin
from briosa.wave_b_operations import (
    ConstructionOperations,
    GdtOperations,
    InstrumentOperations,
    RobotCalibrationApplianceNodeOperations,
    RobotOperations,
    WaveBOperationsMixin,
)

_Result = TypeVar("_Result")

# An omitted startup budget never ends sooner than the 0.5.0 default, and a
# published allowance gains the client's margin for its own server startup,
# discovery, and round trips.
_STARTUP_BUDGET_FLOOR_SECONDS = 120.0
_STARTUP_BUDGET_MARGIN_SECONDS = 20.0
# What an event loop raises for a timer it cannot arm, for example qasync's
# OverflowError for a delay beyond Qt's timer range.
_TIMER_REJECTIONS = (OverflowError, ValueError, OSError)


def _startup_timeout_error(
    diagnostic_code: str = "startup-timeout",
) -> BriosaStartupError:
    """The startup-budget expiry this Python version raises.

    Pickles of the Python 3.10 class load through this function, so they load
    on every version: as that class on Python 3.10, and as plain
    ``BriosaStartupError`` from Python 3.11.
    """
    if sys.version_info < (3, 11):
        return _StartupBudgetTimeout(diagnostic_code)
    return BriosaStartupError(diagnostic_code)


if sys.version_info < (3, 11):

    class _StartupBudgetTimeout(BriosaStartupError, asyncio.TimeoutError):
        """Startup-budget expiry on Python 3.10.

        It is ``BriosaStartupError`` with ``startup-timeout``, as on every
        version, and also ``asyncio.TimeoutError``, which client 0.5.0 raised
        on Python 3.10.
        """

        def __reduce__(self) -> tuple[Any, ...]:
            return (_startup_timeout_error, (self.diagnostic_code,), self.__dict__)


class _StartupBudgetExpired(Exception):
    """A budget check found the startup budget spent before its timer ran."""


def _published_startup_allowance(
    bounds: BriosaLifecycleBounds | None, options: BriosaStartOptions
) -> float | None:
    """The server's allowance, in seconds, for the selected startup phases.

    ``None`` when the server published no bounds, when no server phase is
    selected, or when any allowance the selection needs is unavailable: a partial
    budget is never summed.
    """
    if bounds is None:
        return None
    start = options.start_spatial_analyzer_sdk
    launch = options.launch_spatial_analyzer
    connect = options.connect_to_spatial_analyzer
    parts: tuple[timedelta | None, ...]
    if start and launch and connect:
        parts = (bounds.startup_with_launch,)
    elif start and connect:
        parts = (bounds.startup_without_launch,)
    elif start and launch:
        parts = (bounds.start_sdk, bounds.launch_spatial_analyzer)
    elif start:
        parts = (bounds.start_sdk,)
    elif launch:
        parts = (bounds.launch_spatial_analyzer,)
    else:
        return None
    if any(part is None for part in parts):
        return None
    return sum(part.total_seconds() for part in parts if part is not None)


def _resolved_launch_options(
    options: SpatialAnalyzerLaunchOptions,
) -> SpatialAnalyzerLaunchOptions:
    """Read every launch option once, before a guarded startup's last check.

    The exact type holds plain values. A subclass's attributes are read here, so
    nothing they run can act after that check.
    """
    if type(options) is SpatialAnalyzerLaunchOptions:
        return options
    return SpatialAnalyzerLaunchOptions(
        job_file_path=options.job_file_path,
        quick_start_instrument_name=options.quick_start_instrument_name,
        start_minimized=options.start_minimized,
    )


class _Deadline(Protocol):
    @property
    def when(self) -> float: ...

    @property
    def expired(self) -> bool: ...

    def replace(self, when: float) -> bool: ...

    def cancel(self) -> None: ...


class _NativeDeadline:
    """The deadline of an ``asyncio.timeout`` (Python 3.12 and later).

    The timeout's own timer is the bootstrap deadline. An adopted deadline runs
    on a timer of this object's, registered while the bootstrap timer is still
    armed; when it runs, it expires the timeout as the timeout's own timer would.
    """

    def __init__(
        self, loop: asyncio.AbstractEventLoop, timeout: Any, when: float
    ) -> None:
        self._loop = loop
        self._timeout = timeout
        self._when = when
        self._handle: asyncio.TimerHandle | None = None

    @property
    def when(self) -> float:
        return self._when

    @property
    def expired(self) -> bool:
        return cast(bool, self._timeout.expired())

    def replace(self, when: float) -> bool:
        original = self._when
        try:
            handle = self._loop.call_at(when, self._expire)
        except _TIMER_REJECTIONS:
            return False
        if self._loop.time() >= original:
            # The budget ran out while the timer was registered: never revive it.
            handle.cancel()
            return False
        # Only now that the new timer is armed does the bootstrap timer go;
        # reschedule(None) registers nothing.
        self._timeout.reschedule(None)
        self._handle = handle
        self._when = when
        return True

    def _expire(self) -> None:
        self._handle = None
        # A deadline already due runs the timeout's expiry on the next turn,
        # without registering a timer.
        self._timeout.reschedule(self._loop.time())

    def cancel(self) -> None:
        if self._handle is not None:
            self._handle.cancel()
            self._handle = None


class _LoopDeadline:
    """A deadline on one event loop timer (Python 3.10 and 3.11)."""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        when: float,
        on_expire: Callable[[], None],
    ) -> None:
        self._loop = loop
        self._when = when
        self._on_expire = on_expire
        self._expired = False
        self._handle = loop.call_at(when, self._expire)

    @property
    def when(self) -> float:
        return self._when

    @property
    def expired(self) -> bool:
        return self._expired

    def _expire(self) -> None:
        if not self._expired:
            self._expired = True
            self._on_expire()

    def replace(self, when: float) -> bool:
        original = self._when
        try:
            handle = self._loop.call_at(when, self._expire)
        except _TIMER_REJECTIONS:
            return False
        if self._loop.time() >= original:
            # The budget ran out while the timer was registered: never revive it.
            handle.cancel()
            return False
        self._handle.cancel()
        self._handle = handle
        self._when = when
        return True

    def cancel(self) -> None:
        self._handle.cancel()


class _StartupBudget:
    """Apply the shared startup-budget rule to one ``start()``'s deadline.

    The budget runs on the loop's monotonic clock from one start instant. With a
    server that publishes lifecycle bounds, the startup is guarded: before it
    takes ownership of the session, before each request it hands to the
    transport and before it reports success, it reads the clock and the startup
    task's cancellation, so a startup whose budget ran out or that was cancelled
    stops there, even if its timer or cancellation has not been delivered yet.
    With a server that publishes none, such as Server 0.10.0, the startup
    proceeds exactly as client 0.5.0's did.
    """

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        started_at: float,
        deadline: _Deadline,
        cancel_requested: Callable[[], bool],
    ) -> None:
        self._loop = loop
        self.started_at = started_at
        self._deadline = deadline
        self._cancel_requested = cancel_requested
        self.guarded = False
        self._adopted = False

    def guard(self) -> None:
        self.guarded = True

    def spent(self) -> bool:
        """Whether the deadline has passed, read from the clock."""
        return self._deadline.expired or self._loop.time() >= self._deadline.when

    def adopt(self, allowance: float | None) -> None:
        """Lengthen the omitted budget once from the server's published allowance.

        Only the first validated snapshot counts. Adoption never revives a
        startup whose budget has run out, even if its timer has not run yet, and
        keeps the current deadline when the loop cannot arm the new one.
        """
        if self._adopted:
            return
        self._adopted = True
        if allowance is None or self._cancel_requested() or self.spent():
            return
        now = self._loop.time()
        current = self._deadline.when
        deadline = self.started_at + max(
            _STARTUP_BUDGET_FLOOR_SECONDS, allowance + _STARTUP_BUDGET_MARGIN_SECONDS
        )
        if deadline <= current or not math.isfinite(deadline - now):
            return
        self._deadline.replace(deadline)

    async def check(self) -> None:
        """Stop a guarded startup that was cancelled or whose budget is spent."""
        if not self.guarded:
            return
        if self._cancel_requested():
            # A cancellation of this task arrives at this yield. On Python 3.10
            # and 3.11 the cancelled task is the one waiting on this startup, so
            # stop here whether or not it has cancelled this one yet.
            await asyncio.sleep(0)
            raise asyncio.CancelledError
        if self.spent():
            raise _StartupBudgetExpired


async def _cancel_and_wait(
    task: asyncio.Task[Any], loop: asyncio.AbstractEventLoop
) -> None:
    waiter = loop.create_future()

    def release(_: object) -> None:
        if not waiter.done():
            waiter.set_result(None)

    task.add_done_callback(release)
    try:
        task.cancel()
        await waiter
    finally:
        task.remove_done_callback(release)


class OwnedServer(Protocol):
    @property
    def target(self) -> str: ...

    @property
    def has_exited(self) -> bool: ...

    async def close(self) -> None: ...


class ServerLauncher(Protocol):
    async def launch(
        self,
        logging: BriosaLoggingOptions | None = None,
        selection: BriosaServerSelection | None = None,
    ) -> OwnedServer: ...


@dataclass(slots=True)
class _SubprocessServer:
    process: asyncio.subprocess.Process
    target: str
    installation: BriosaInstallation

    @property
    def has_exited(self) -> bool:
        return self.process.returncode is not None

    async def close(self) -> None:
        if self.process.returncode is None:
            self.process.kill()
            await self.process.wait()


class _LocalServerLauncher:
    async def launch(
        self,
        logging: BriosaLoggingOptions | None = None,
        selection: BriosaServerSelection | None = None,
    ) -> OwnedServer:
        options = selection or BriosaServerSelection()
        installation = await asyncio.to_thread(resolve_installation, options)
        verified = await asyncio.to_thread(
            read_installation, installation.executable_path, installation.scope
        )
        if verified != installation:
            raise BriosaStartupError("server-installation-changed")
        executable = installation.executable_path
        sa_arguments = (
            [
                f"--Briosa:SpatialAnalyzer:ExecutablePath={options.spatial_analyzer_executable_path}"
            ]
            if options.spatial_analyzer_executable_path is not None
            else []
        )
        port = _reserve_loopback_port()
        creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        try:
            process = await asyncio.create_subprocess_exec(
                str(executable),
                f"--Briosa:Endpoint:Port={port}",
                *sa_arguments,
                *(logging.to_arguments() if logging is not None else []),
                cwd=str(executable.parent),
                creationflags=creation_flags,
            )
        except OSError as error:
            raise BriosaStartupError("server-process-start-failed") from error
        return _SubprocessServer(process, f"127.0.0.1:{port}", installation)


@dataclass(slots=True)
class _Session:
    server: OwnedServer
    transport: ClientTransport
    snapshot: BriosaServerSnapshot
    application_state: SpatialAnalyzerLifecycleState | None = None
    sdk_state: SpatialAnalyzerSdkLifecycleState | None = None
    startup_completed: bool = False
    command_admission_open: bool = False
    active_commands: int = 0
    commands_drained: asyncio.Event = field(default_factory=asyncio.Event)

    def __post_init__(self) -> None:
        self.commands_drained.set()

    def update_sdk_state(self, state: SpatialAnalyzerSdkLifecycleState) -> None:
        self.sdk_state = state
        self._refresh_command_admission()

    def update_snapshot(self, snapshot: BriosaServerSnapshot) -> None:
        self.snapshot = snapshot
        self._refresh_command_admission()

    def publish_startup(self) -> None:
        self.startup_completed = True
        self._refresh_command_admission()

    def _refresh_command_admission(self) -> None:
        self.command_admission_open = bool(
            self.snapshot.ready_for_mp
            and self.sdk_state is not None
            and self.sdk_state.ready_for_mp
        )


class BriosaClient(WaveBOperationsMixin, WaveAOperationsMixin):
    """One reusable, event-loop-bound owner of a local Briosa server session."""

    def __init__(
        self,
        options: BriosaClientOptions | None = None,
        *,
        _server_launcher: ServerLauncher | None = None,
        _transport_factory: Callable[[str], ClientTransport] | None = None,
    ) -> None:
        self._options = options or BriosaClientOptions()
        self._server_launcher = _server_launcher or _LocalServerLauncher()
        self._transport_factory = _transport_factory or GrpcClientTransport
        self._loop: asyncio.AbstractEventLoop | None = None
        self._lock: asyncio.Lock | None = None
        self._session: _Session | None = None
        self.construction_operations = ConstructionOperations(self)
        self.gdt_operations = GdtOperations(self)
        self.instrument_operations = InstrumentOperations(self)
        self.robot_calibration_appliance_node_operations = (
            RobotCalibrationApplianceNodeOperations(self)
        )
        self.robot_operations = RobotOperations(self)
        self._start_task: asyncio.Task[None] | None = None
        self._stop_task: asyncio.Task[None] | None = None
        self._finally_closed = False

    async def __aenter__(self) -> BriosaClient:
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def start(self, options: BriosaStartOptions | None = None) -> None:
        """Start one owned local server and the selected lifecycle phases."""
        selected = options or BriosaStartOptions()
        lock = self._bind_loop()
        async with lock:
            self._ensure_open()
            if self._session is not None and self._session.startup_completed:
                return
            if self._start_task is not None:
                task = self._start_task
            elif self._session is not None:
                raise BriosaLifecycleError("startup-partially-completed")
            elif self._stop_task is not None:
                raise BriosaLifecycleError("client-stop-in-progress")
            else:
                task = asyncio.create_task(self._run_start(selected))
                self._start_task = task
                task.add_done_callback(self._observe_start)
        await asyncio.shield(task)

    async def get_server_snapshot(
        self, *, timeout: float | None = None
    ) -> BriosaServerSnapshot:
        async def operation(session: _Session) -> BriosaServerSnapshot:
            try:
                raw = await session.transport.get_server_snapshot(
                    _validate_timeout(timeout)
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            snapshot = map_snapshot(*raw)
            session.update_snapshot(snapshot)
            return snapshot

        return await self._run_lifecycle(operation)

    async def list_capabilities(
        self, *, include_denied: bool = False, timeout: float | None = None
    ) -> BriosaCapabilityListing:
        """List the server's capabilities for diagnosis.

        With ``include_denied``, the listing also reports every registered
        operation the active policy denies, each with its denial reason in
        ``admission`` and, with Server 0.10.1 and later, its denial detail in
        ``policy_denial``. The listing never changes the generation's admitted set.
        """

        async def operation(session: _Session) -> BriosaCapabilityListing:
            try:
                raw = await session.transport.list_capabilities(
                    include_denied=include_denied, timeout=_validate_timeout(timeout)
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            return map_capability_listing(raw)

        return await self._run_lifecycle(operation)

    async def get_spatial_analyzer_state(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerLifecycleState:
            return await self._refresh_application_state(session, timeout)

        return await self._run_lifecycle(operation)

    async def launch_spatial_analyzer(
        self,
        options: SpatialAnalyzerLaunchOptions | None = None,
        *,
        timeout: float | None = None,
    ) -> SpatialAnalyzerLifecycleState:
        selected = options or SpatialAnalyzerLaunchOptions()

        async def operation(session: _Session) -> SpatialAnalyzerLifecycleState:
            try:
                state = map_application_state(
                    await session.transport.launch_application(
                        selected, _validate_timeout(timeout)
                    )
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            session.application_state = state
            return state

        return await self._run_lifecycle(operation)

    async def close_owned_spatial_analyzer(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerLifecycleState:
            current = await self._ensure_application_state(session, timeout)
            generation = _require_generation(
                current.application_generation, "application-generation-unavailable"
            )
            try:
                state = map_application_state(
                    await session.transport.close_application(
                        generation, _validate_timeout(timeout)
                    )
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, current) from error
            session.application_state = state
            return state

        return await self._run_lifecycle(operation)

    async def get_spatial_analyzer_sdk_state(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerSdkLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerSdkLifecycleState:
            return await self._refresh_sdk_state(session, timeout)

        return await self._run_lifecycle(operation)

    async def start_spatial_analyzer_sdk(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerSdkLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerSdkLifecycleState:
            try:
                state = map_sdk_state(
                    await session.transport.start_sdk(_validate_timeout(timeout))
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            session.update_sdk_state(state)
            return state

        return await self._run_lifecycle(operation)

    async def connect_to_spatial_analyzer(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerSdkLifecycleState:
        return await self._connect_sdk(reconnect=False, timeout=timeout)

    async def reconnect_to_spatial_analyzer(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerSdkLifecycleState:
        return await self._connect_sdk(reconnect=True, timeout=timeout)

    async def stop_spatial_analyzer_sdk(
        self, *, timeout: float | None = None
    ) -> SpatialAnalyzerSdkLifecycleState:
        return await self._sdk_generation_transition(
            lambda transport, generation: transport.stop_sdk(
                generation, _validate_timeout(timeout)
            )
        )

    async def recover_spatial_analyzer_sdk(
        self,
        mode: SpatialAnalyzerSdkRecoveryMode,
        *,
        timeout: float | None = None,
    ) -> SpatialAnalyzerSdkLifecycleState:
        if mode is not SpatialAnalyzerSdkRecoveryMode.REPLACE_WITHOUT_REPLAY:
            raise ValueError("mode must be REPLACE_WITHOUT_REPLAY")
        return await self._sdk_generation_transition(
            lambda transport, generation: transport.recover_sdk(
                generation, _validate_timeout(timeout)
            )
        )

    async def get_working_directory(
        self, *, on_mp_completion: MpCompletionObserver | None = None
    ) -> str:
        """Return SpatialAnalyzer's working directory."""
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetWorkingDirectory",
                "file_operations.get_working_directory",
                {},
                None,
                on_mp_completion=on_mp_completion,
            ),
        )

    async def get_active_collection_name(
        self, *, on_mp_completion: MpCompletionObserver | None = None
    ) -> str:
        """Return the name of the active SpatialAnalyzer collection."""
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetActiveCollectionName",
                "construction_operations.get_active_collection_name",
                {},
                None,
                on_mp_completion=on_mp_completion,
            ),
        )

    async def _invoke_mp_operation(
        self,
        service: str,
        rpc: str,
        operation_id: str,
        values: dict[str, Any],
        result_type: type[Any] | None,
        *,
        on_mp_completion: MpCompletionObserver | None = None,
    ) -> Any:
        method = operation_method(service, rpc)
        request = build_request(method, values)
        path = f"/{service}/{rpc}"
        lock = self._bind_loop()
        async with lock:
            self._ensure_open()
            if self._start_task is not None:
                raise BriosaLifecycleError("client-start-in-progress")
            session = self._require_session()
            if not session.command_admission_open:
                raise BriosaLifecycleError("mp-command-admission-closed")
            session.active_commands += 1
            session.commands_drained.clear()
        try:
            response = await session.transport.invoke_operation(
                path,
                request,
                response_type(method),
                self._options.command_timeout,
            )
            # C1: every success is checked, observed or not, and the observer
            # hears of it before the outputs are mapped.
            completion = map_mp_completion(response)
            if on_mp_completion is not None:
                on_mp_completion(completion)
            return map_response(method, response, result_type)
        except grpc.RpcError as error:
            raise map_rpc_error(error, session.application_state) from error
        finally:
            await asyncio.shield(self._exit_command(session))

    async def stop(self) -> None:
        lock = self._bind_loop()
        async with lock:
            self._ensure_open()
            task = self._get_or_create_stop_task()
        await asyncio.shield(task)

    async def aclose(self) -> None:
        lock = self._bind_loop()
        async with lock:
            if self._finally_closed:
                return
            self._finally_closed = True
            task = self._get_or_create_stop_task()
        await asyncio.shield(task)

    async def _run_start(self, options: BriosaStartOptions) -> None:
        # One start instant on the loop's monotonic clock, before host launch or
        # discovery. Each Python version times the startup the way its
        # asyncio.wait_for timed it for client 0.5.0: asyncio.timeout from
        # Python 3.12, and a waiter on Python 3.10 and 3.11.
        loop = asyncio.get_running_loop()
        started_at = loop.time()
        try:
            if sys.version_info >= (3, 12):
                task = asyncio.current_task()
                assert task is not None
                when = started_at + options.startup_timeout
                async with asyncio.timeout_at(when) as timeout:
                    deadline = _NativeDeadline(loop, timeout, when)
                    try:
                        await self._start_inner(
                            options,
                            _StartupBudget(
                                loop,
                                started_at,
                                deadline,
                                lambda: task.cancelling() > 0,
                            ),
                        )
                    finally:
                        deadline.cancel()
            else:
                await self._run_start_with_waiter(options, loop, started_at)
        except TimeoutError as error:
            raise BriosaStartupError("startup-timeout") from error

    async def _run_start_with_waiter(
        self,
        options: BriosaStartOptions,
        loop: asyncio.AbstractEventLoop,
        started_at: float,
    ) -> None:
        """Time the startup the way ``asyncio.wait_for`` does on Python 3.10-3.11.

        The startup runs in its own task while this one waits on a future that
        the deadline or the startup's completion resolves. Cancelling this task
        therefore stays a cancellation, distinct from the budget's expiry. It
        cancels that future at once, which is how a guarded startup sees the
        cancellation before this task has run to pass it on.
        """
        waiter: asyncio.Future[None] = loop.create_future()

        def release(_: object = None) -> None:
            if not waiter.done():
                waiter.set_result(None)

        deadline = _LoopDeadline(loop, started_at + options.startup_timeout, release)
        startup = loop.create_task(
            self._start_inner(
                options,
                _StartupBudget(loop, started_at, deadline, waiter.cancelled),
            )
        )
        startup.add_done_callback(release)
        try:
            try:
                await waiter
            except asyncio.CancelledError:
                if startup.done():
                    return startup.result()
                startup.remove_done_callback(release)
                await _cancel_and_wait(startup, loop)
                raise
            if startup.done():
                return startup.result()
            startup.remove_done_callback(release)
            await _cancel_and_wait(startup, loop)
            try:
                return startup.result()
            except asyncio.CancelledError as cancelled:
                if sys.version_info < (3, 11):
                    raise _startup_timeout_error() from cancelled
                raise TimeoutError from cancelled
        finally:
            deadline.cancel()

    async def _start_inner(
        self, options: BriosaStartOptions, budget: _StartupBudget
    ) -> None:
        server: OwnedServer | None = None
        transport: ClientTransport | None = None
        session: _Session | None = None
        try:
            try:
                server = await self._server_launcher.launch(
                    options.logging, options.server_selection
                )
                transport = self._transport_factory(server.target)
                snapshot = await self._wait_for_server(server, transport)
                # A server that publishes lifecycle bounds (Server 0.10.1 and
                # later) guards the rest of the startup. The first validated
                # snapshot is the only adoption point, and an explicit
                # startup_timeout always wins.
                if snapshot.lifecycle_bounds is not None:
                    budget.guard()
                if _startup_timeout_omitted(options):
                    budget.adopt(
                        _published_startup_allowance(snapshot.lifecycle_bounds, options)
                    )
                await budget.check()
                candidate = _Session(server, transport, snapshot)
                if not budget.guarded:
                    # As client 0.5.0: the session owns the server from here.
                    session = candidate
                lock = self._required_lock()
                async with lock:
                    self._ensure_open()
                    # The last check before the client takes ownership: until
                    # then, a failure closes the transport and the server.
                    await budget.check()
                    self._session = candidate
                    session = candidate
                server = None
                transport = None
                await self._start_phases(options, session, budget)
                await budget.check()
                session.publish_startup()
            except grpc.RpcError as error:
                raise map_rpc_error(
                    error, session.application_state if session is not None else None
                ) from error
        except _StartupBudgetExpired:
            self._close_admission(session, budget)
            raise _startup_timeout_error() from None
        except Exception as failure:
            self._close_admission(session, budget)
            if budget.guarded and budget.spent():
                # A phase that fails once the budget has run out, even before
                # its timer runs, ends the startup as a timeout.
                raise _startup_timeout_error() from failure
            raise
        except BaseException:
            self._close_admission(session, budget)
            raise
        finally:
            if session is None:
                if transport is not None:
                    await transport.close()
                if server is not None:
                    await server.close()

    async def _start_phases(
        self, options: BriosaStartOptions, session: _Session, budget: _StartupBudget
    ) -> None:
        """Run the selected startup phases; a guarded startup checks each handoff.

        A guarded startup reads every argument of a request before its last
        check, so nothing it calls can spend the budget or cancel the startup
        after that check. Unguarded, the phases run as client 0.5.0's did.
        """
        if options.start_spatial_analyzer_sdk:
            await budget.check()
            session.update_sdk_state(map_sdk_state(await session.transport.start_sdk()))
        if options.launch_spatial_analyzer:
            launch_options = options.launch_options
            if budget.guarded:
                launch_options = _resolved_launch_options(launch_options)
                await budget.check()
            session.application_state = map_application_state(
                await session.transport.launch_application(launch_options)
            )
        if options.connect_to_spatial_analyzer:
            if session.sdk_state is None:
                await budget.check()
            sdk = await self._ensure_sdk_state(session, None)
            generation = _require_generation(
                sdk.sdk_generation, "sdk-generation-unavailable"
            )
            await budget.check()
            connected_state = map_sdk_state(
                await session.transport.connect_sdk(generation, reconnect=False)
            )
            session.update_sdk_state(connected_state)
            if budget.guarded:
                await budget.check()
                server = await session.transport.get_server_info()
                await budget.check()
                refreshed = map_snapshot(
                    server, await session.transport.list_capabilities()
                )
            else:
                refreshed = map_snapshot(
                    *(await session.transport.get_server_snapshot())
                )
            session.update_snapshot(refreshed)
            if not session.snapshot.ready_for_mp or not connected_state.ready_for_mp:
                raise BriosaLifecycleError("startup-readiness-not-established")

    @staticmethod
    def _close_admission(session: _Session | None, budget: _StartupBudget) -> None:
        # A guarded startup that fails after taking ownership admits no MP
        # command until a later lifecycle call refreshes the session's state.
        if session is not None and budget.guarded:
            session.command_admission_open = False

    async def _wait_for_server(
        self, server: OwnedServer, transport: ClientTransport
    ) -> BriosaServerSnapshot:
        while True:
            if server.has_exited:
                raise BriosaStartupError("server-process-exited")
            try:
                snapshot = await transport.get_server_snapshot()
                validate_installation(
                    snapshot[0], getattr(server, "installation", None)
                )
                return map_snapshot(*snapshot)
            except grpc.RpcError as error:
                if error.code() is not grpc.StatusCode.UNAVAILABLE:
                    raise map_rpc_error(error) from error
                await asyncio.sleep(0.05)

    async def _connect_sdk(
        self, *, reconnect: bool, timeout: float | None
    ) -> SpatialAnalyzerSdkLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerSdkLifecycleState:
            current = await self._ensure_sdk_state(session, timeout)
            generation = _require_generation(
                current.sdk_generation, "sdk-generation-unavailable"
            )
            try:
                state = map_sdk_state(
                    await session.transport.connect_sdk(
                        generation,
                        reconnect=reconnect,
                        timeout=_validate_timeout(timeout),
                    )
                )
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            session.update_sdk_state(state)
            return state

        return await self._run_lifecycle(operation)

    async def _sdk_generation_transition(
        self,
        transition: Callable[
            [ClientTransport, int],
            Awaitable[Any],
        ],
    ) -> SpatialAnalyzerSdkLifecycleState:
        async def operation(session: _Session) -> SpatialAnalyzerSdkLifecycleState:
            current = await self._ensure_sdk_state(session, None)
            generation = _require_generation(
                current.sdk_generation, "sdk-generation-unavailable"
            )
            try:
                state = map_sdk_state(await transition(session.transport, generation))
            except grpc.RpcError as error:
                raise map_rpc_error(error, session.application_state) from error
            session.update_sdk_state(state)
            return state

        return await self._run_lifecycle(operation)

    async def _run_lifecycle(
        self,
        operation: Callable[[_Session], Awaitable[_Result]],
    ) -> _Result:
        lock = self._bind_loop()
        async with lock:
            self._ensure_open()
            if self._start_task is not None:
                raise BriosaLifecycleError("client-start-in-progress")
            if self._stop_task is not None:
                raise BriosaLifecycleError("client-stop-in-progress")
            return await operation(self._require_session())

    async def _refresh_application_state(
        self, session: _Session, timeout: float | None
    ) -> SpatialAnalyzerLifecycleState:
        try:
            state = map_application_state(
                await session.transport.get_application_state(
                    _validate_timeout(timeout)
                )
            )
        except grpc.RpcError as error:
            raise map_rpc_error(error, session.application_state) from error
        session.application_state = state
        return state

    async def _ensure_application_state(
        self, session: _Session, timeout: float | None
    ) -> SpatialAnalyzerLifecycleState:
        return session.application_state or await self._refresh_application_state(
            session, timeout
        )

    async def _refresh_sdk_state(
        self, session: _Session, timeout: float | None
    ) -> SpatialAnalyzerSdkLifecycleState:
        try:
            state = map_sdk_state(
                await session.transport.get_sdk_state(_validate_timeout(timeout))
            )
        except grpc.RpcError as error:
            raise map_rpc_error(error, session.application_state) from error
        session.update_sdk_state(state)
        return state

    async def _ensure_sdk_state(
        self, session: _Session, timeout: float | None
    ) -> SpatialAnalyzerSdkLifecycleState:
        return session.sdk_state or await self._refresh_sdk_state(session, timeout)

    async def _exit_command(self, session: _Session) -> None:
        lock = self._required_lock()
        async with lock:
            session.active_commands -= 1
            if session.active_commands == 0:
                session.commands_drained.set()

    def _get_or_create_stop_task(self) -> asyncio.Task[None]:
        if self._stop_task is None:
            self._stop_task = asyncio.create_task(self._stop_inner(self._start_task))
            self._stop_task.add_done_callback(self._observe_stop)
        return self._stop_task

    async def _stop_inner(self, pending_start: asyncio.Task[None] | None) -> None:
        if pending_start is not None:
            with suppress(BriosaError, TimeoutError):
                await asyncio.shield(pending_start)
        lock = self._required_lock()
        async with lock:
            session = self._session
            self._session = None
            if session is not None:
                session.command_admission_open = False
                if session.active_commands == 0:
                    session.commands_drained.set()
        if session is None:
            return
        await session.commands_drained.wait()
        await self._stop_sdk_best_effort(session)
        await session.transport.close()
        await session.server.close()

    async def _stop_sdk_best_effort(self, session: _Session) -> None:
        try:
            state = await self._ensure_sdk_state(session, None)
            if (
                state.sdk_generation is not None
                and state.sdk_state is not SpatialAnalyzerSdkState.STOPPED
            ):
                await session.transport.stop_sdk(state.sdk_generation)
        except (BriosaError, grpc.RpcError):
            pass

    def _observe_start(self, task: asyncio.Task[None]) -> None:
        if not task.cancelled():
            task.exception()
        if self._start_task is task:
            self._start_task = None

    def _observe_stop(self, task: asyncio.Task[None]) -> None:
        if not task.cancelled():
            task.exception()
        if self._stop_task is task:
            self._stop_task = None

    def _bind_loop(self) -> asyncio.Lock:
        loop = asyncio.get_running_loop()
        if self._loop is None:
            self._loop = loop
            self._lock = asyncio.Lock()
        elif self._loop is not loop:
            raise BriosaLifecycleError("different-event-loop")
        return self._required_lock()

    def _required_lock(self) -> asyncio.Lock:
        if self._lock is None:
            raise BriosaLifecycleError("client-not-bound")
        return self._lock

    def _require_session(self) -> _Session:
        if self._session is None:
            raise BriosaLifecycleError("client-not-started")
        return self._session

    def _ensure_open(self) -> None:
        if self._finally_closed:
            raise BriosaLifecycleError("client-finally-closed")


def _validate_timeout(timeout: float | None) -> float | None:
    if timeout is not None and timeout <= 0:
        raise ValueError("timeout must be positive when supplied")
    return timeout


def _require_generation(generation: int | None, diagnostic_code: str) -> int:
    if generation is None or generation <= 0:
        raise BriosaLifecycleError(diagnostic_code)
    return generation


def _reserve_loopback_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])
