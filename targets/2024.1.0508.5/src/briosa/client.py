"""Idiomatic asynchronous orchestration over Briosa's private gRPC transport."""

from __future__ import annotations

import asyncio
import math
import os
import socket
import subprocess
from collections.abc import Awaitable, Callable
from contextlib import suppress
from dataclasses import dataclass, field
from datetime import timedelta
from types import TracebackType
from typing import Any, NoReturn, Protocol, TypeVar, cast

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


class _TimerHandle(Protocol):
    def cancel(self) -> None: ...


class _StartupClock(Protocol):
    """The monotonic clock and timer of one startup: the event loop's."""

    def time(self) -> float: ...

    def call_at(self, when: float, callback: Callable[[], None]) -> _TimerHandle: ...


class _EventLoopClock:
    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self._loop = loop

    def time(self) -> float:
        return self._loop.time()

    def call_at(self, when: float, callback: Callable[[], None]) -> _TimerHandle:
        return self._loop.call_at(when, callback)


class _StartupBudgetExpired(Exception):
    """Adoption found the startup budget already spent."""


def _schedulable(delay: float) -> bool:
    """Whether the event loop can schedule a timer ``delay`` seconds ahead.

    asyncio schedules any finite loop time; a non-finite one would never fire.
    """
    return math.isfinite(delay)


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


class _StartupDeadline:
    """The deadline of one ``start()``, reschedulable in place.

    It runs on the event loop's monotonic clock, from one start instant, and
    cancels the startup task when it expires. Lengthening it replaces only the
    timer, so the startup is never cancelled and relaunched.
    """

    def __init__(
        self, clock: _StartupClock, task: asyncio.Task[Any], budget: float
    ) -> None:
        self._clock = clock
        self._task = task
        self.started_at = clock.time()
        self.deadline = self.started_at + budget
        self.expired = False
        self._finished = False
        self._adopted = False
        self._handle = clock.call_at(self.deadline, self._expire)

    def _expire(self) -> None:
        if self._finished or self.expired:
            return
        self.expired = True
        self._task.cancel()

    def _expire_now(self) -> NoReturn:
        self.expired = True
        self._handle.cancel()
        raise _StartupBudgetExpired

    def finish(self) -> None:
        self._finished = True
        self._handle.cancel()

    def adopt(self, allowance: float | None) -> None:
        """Lengthen the omitted budget once from the server's published allowance.

        Only the first validated snapshot counts. Adoption never revives a
        startup that has expired, even if the timer has not fired yet, and keeps
        the current deadline when the new one cannot be scheduled.
        """
        if self._adopted:
            return
        self._adopted = True
        if allowance is None or self._finished or self.expired:
            return
        cancelling = getattr(self._task, "cancelling", None)
        if cancelling is not None and cancelling() > 0:
            return
        now = self._clock.time()
        if now >= self.deadline:
            self._expire_now()
        deadline = self.started_at + max(
            _STARTUP_BUDGET_FLOOR_SECONDS, allowance + _STARTUP_BUDGET_MARGIN_SECONDS
        )
        if deadline <= now:
            self._expire_now()
        if deadline <= self.deadline or not _schedulable(deadline - now):
            return
        handle = self._clock.call_at(deadline, self._expire)
        self._handle.cancel()
        self._handle = handle
        self.deadline = deadline


def _withdraw_budget_cancellation(task: asyncio.Task[Any]) -> bool:
    """Withdraw the budget's own cancellation request from ``task``.

    Returns whether no other cancellation is pending. Python 3.10 tasks don't
    count cancellation requests, so there the budget's expiry decides alone.
    """
    uncancel = getattr(task, "uncancel", None)
    return uncancel is None or uncancel() == 0


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
        _startup_clock: Callable[[asyncio.AbstractEventLoop], _StartupClock]
        | None = None,
    ) -> None:
        self._options = options or BriosaClientOptions()
        self._server_launcher = _server_launcher or _LocalServerLauncher()
        self._transport_factory = _transport_factory or GrpcClientTransport
        self._startup_clock = _startup_clock or _EventLoopClock
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
        # discovery. The budget's timer cancels this task when it expires.
        task = asyncio.current_task()
        if task is None:  # pragma: no cover - start() always runs this in a task
            raise BriosaLifecycleError("client-start-unavailable")
        deadline = _StartupDeadline(
            self._startup_clock(asyncio.get_running_loop()),
            task,
            options.startup_timeout,
        )
        try:
            await self._start_inner(options, deadline)
        except _StartupBudgetExpired:
            raise _startup_timeout(None)  # noqa: B904 - chained in the helper
        except asyncio.CancelledError as cancelled:
            if deadline.expired and _withdraw_budget_cancellation(task):
                raise _startup_timeout(cancelled)  # noqa: B904 - chained in the helper
            raise
        finally:
            deadline.finish()

    async def _start_inner(
        self, options: BriosaStartOptions, deadline: _StartupDeadline
    ) -> None:
        server: OwnedServer | None = None
        transport: ClientTransport | None = None
        session: _Session | None = None
        try:
            server = await self._server_launcher.launch(
                options.logging, options.server_selection
            )
            transport = self._transport_factory(server.target)
            snapshot = await self._wait_for_server(server, transport)
            # The first validated snapshot is the only adoption point; an
            # explicit startup_timeout always wins.
            if _startup_timeout_omitted(options):
                deadline.adopt(
                    _published_startup_allowance(snapshot.lifecycle_bounds, options)
                )
            session = _Session(server, transport, snapshot)
            lock = self._required_lock()
            async with lock:
                self._ensure_open()
                self._session = session
            server = None
            transport = None

            if options.start_spatial_analyzer_sdk:
                session.update_sdk_state(
                    map_sdk_state(await session.transport.start_sdk())
                )
            if options.launch_spatial_analyzer:
                session.application_state = map_application_state(
                    await session.transport.launch_application(options.launch_options)
                )
            if options.connect_to_spatial_analyzer:
                sdk = await self._ensure_sdk_state(session, None)
                generation = _require_generation(
                    sdk.sdk_generation, "sdk-generation-unavailable"
                )
                connected_state = map_sdk_state(
                    await session.transport.connect_sdk(generation, reconnect=False)
                )
                session.update_sdk_state(connected_state)
                session.update_snapshot(
                    map_snapshot(*(await session.transport.get_server_snapshot()))
                )
                if (
                    not session.snapshot.ready_for_mp
                    or not connected_state.ready_for_mp
                ):
                    raise BriosaLifecycleError("startup-readiness-not-established")
            session.publish_startup()
        except grpc.RpcError as error:
            raise map_rpc_error(
                error, session.application_state if session is not None else None
            ) from error
        finally:
            if session is None:
                if transport is not None:
                    await transport.close()
                if server is not None:
                    await server.close()

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


def _startup_timeout(cause: BaseException | None) -> BriosaStartupError:
    """The startup timeout error, chained as 0.5.0 chained it to its timeout."""
    timeout = TimeoutError()
    timeout.__cause__ = cause
    error = BriosaStartupError("startup-timeout")
    error.__cause__ = timeout
    error.__suppress_context__ = True
    return error


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
