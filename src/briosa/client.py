"""Idiomatic asynchronous orchestration over Briosa's private gRPC transport."""

from __future__ import annotations

import asyncio
import os
import socket
import subprocess
from collections.abc import Awaitable, Callable
from contextlib import suppress
from dataclasses import dataclass, field
from pathlib import Path
from types import TracebackType
from typing import Any, Protocol, TypeVar

import grpc

from briosa.errors import (
    BriosaError,
    BriosaLifecycleError,
    BriosaStartupError,
)
from briosa.models import (
    BriosaClientOptions,
    BriosaServerSnapshot,
    BriosaStartOptions,
    SpatialAnalyzerLaunchOptions,
    SpatialAnalyzerLifecycleState,
    SpatialAnalyzerSdkLifecycleState,
    SpatialAnalyzerSdkRecoveryMode,
    SpatialAnalyzerSdkState,
)
from briosa.operation_protocol import (
    build_request,
    map_response,
    operation_method,
    response_type,
)
from briosa.protocol_identity import BRIOSA_VERSION, SPATIAL_ANALYZER_TARGET
from briosa.transport import (
    ClientTransport,
    GrpcClientTransport,
    map_application_state,
    map_rpc_error,
    map_sdk_state,
    map_snapshot,
)
from briosa.wave_a_operations import WaveAOperationsMixin

_SERVER_PATH_ENVIRONMENT_VARIABLE = "BRIOSA_SERVER_PATH"
_Result = TypeVar("_Result")


class OwnedServer(Protocol):
    @property
    def target(self) -> str: ...

    @property
    def has_exited(self) -> bool: ...

    async def close(self) -> None: ...


class ServerLauncher(Protocol):
    async def launch(self) -> OwnedServer: ...


@dataclass(slots=True)
class _SubprocessServer:
    process: asyncio.subprocess.Process
    target: str

    @property
    def has_exited(self) -> bool:
        return self.process.returncode is not None

    async def close(self) -> None:
        if self.process.returncode is None:
            self.process.kill()
            await self.process.wait()


class _LocalServerLauncher:
    async def launch(self) -> OwnedServer:
        executable = _resolve_server_executable()
        port = _reserve_loopback_port()
        creation_flags = subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0
        try:
            process = await asyncio.create_subprocess_exec(
                str(executable),
                f"--Briosa:Endpoint:Port={port}",
                cwd=str(executable.parent),
                creationflags=creation_flags,
            )
        except OSError as error:
            raise BriosaStartupError("server-process-start-failed") from error
        return _SubprocessServer(process, f"127.0.0.1:{port}")


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


class BriosaClient(WaveAOperationsMixin):
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

    async def get_working_directory(self) -> str:
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
            return await session.transport.get_working_directory(
                self._options.command_timeout
            )
        except grpc.RpcError as error:
            raise map_rpc_error(error, session.application_state) from error
        finally:
            await asyncio.shield(self._exit_command(session))

    async def _invoke_mp_operation(
        self,
        service: str,
        rpc: str,
        operation_id: str,
        values: dict[str, Any],
        result_type: type[Any] | None,
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
        try:
            await asyncio.wait_for(
                self._start_inner(options), timeout=options.startup_timeout
            )
        except TimeoutError as error:
            raise BriosaStartupError("startup-timeout") from error

    async def _start_inner(self, options: BriosaStartOptions) -> None:
        server: OwnedServer | None = None
        transport: ClientTransport | None = None
        session: _Session | None = None
        try:
            server = await self._server_launcher.launch()
            transport = self._transport_factory(server.target)
            snapshot = await self._wait_for_server(server, transport)
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
                return map_snapshot(*(await transport.get_server_snapshot()))
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


def _resolve_server_executable() -> Path:
    configured = os.environ.get(_SERVER_PATH_ENVIRONMENT_VARIABLE)
    local_app_data = Path(
        os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")
    )
    candidates = (
        Path(configured) if configured else None,
        Path(__file__).resolve().parent / "briosa-server" / "Briosa.Server.exe",
        local_app_data
        / "Briosa"
        / "servers"
        / BRIOSA_VERSION
        / f"sa-{SPATIAL_ANALYZER_TARGET}"
        / "Briosa.Server.exe",
    )
    for candidate in candidates:
        if (
            candidate is not None
            and candidate.name.lower() == "briosa.server.exe"
            and candidate.is_file()
        ):
            return candidate.resolve()
    raise BriosaStartupError("server-distribution-not-found")


def _reserve_loopback_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.bind(("127.0.0.1", 0))
        return int(listener.getsockname()[1])
