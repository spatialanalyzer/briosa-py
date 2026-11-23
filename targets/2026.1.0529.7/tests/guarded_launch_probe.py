"""Launch through the real GrpcClientTransport while launch values run code.

``test_startup_budget.py`` runs this in its own process with the pure-Python
protobuf runtime, which calls a ``str`` value's ``encode()`` while it builds and
serializes a request, and imports it to run with the default runtime. The gRPC
stubs are replaced by recorders, so no channel is ever used. Run directly, it
prints the outcome as JSON.
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Callable
from typing import Any

from google.protobuf.internal import api_implementation
from virtual_clock import VirtualClockLoop, run_virtual

from briosa import (
    BriosaClient,
    BriosaLoggingOptions,
    BriosaServerSelection,
    BriosaStartOptions,
    BriosaStartupError,
    SpatialAnalyzerLaunchOptions,
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
from briosa.transport import GrpcClientTransport

T0 = 1000.0


class Server:
    target = "127.0.0.1:9"
    has_exited = False

    async def close(self) -> None:
        return None


class Launcher:
    async def launch(
        self,
        logging: BriosaLoggingOptions | None = None,
        selection: BriosaServerSelection | None = None,
    ) -> OwnedServer:
        return Server()


def sdk_state(generation: int) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
    state = lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
        state_revision=1,
        sdk_state=(
            lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_RUNNING
            if generation
            else lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_STOPPED
        ),
        recovery_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED,
    )
    if generation:
        state.sdk_generation = generation
    return state


class Stub:
    """Records each generated-stub call with the time it was made."""

    def __init__(self, loop: VirtualClockLoop, calls: list[tuple[str, float, Any]]):
        self._loop = loop
        self._calls = calls
        self._generation = 0

    def __getattr__(self, name: str) -> Callable[..., Any]:
        async def call(request: Any, timeout: float | None = None) -> Any:
            self._calls.append((name, self._loop.time() - T0, request))
            await asyncio.sleep(0)
            return self._response(name)

        return call

    def _response(self, name: str) -> Any:
        if name == "GetServerInfo":
            server = discovery_pb2.GetServerInfoResponse(
                version={
                    "briosa_version": BRIOSA_VERSION,
                    "source_revision": SOURCE_REVISION,
                    "protocol_package": PROTOCOL_PACKAGE,
                    "spatial_analyzer_target": SPATIAL_ANALYZER_TARGET,
                },
                worker_state=discovery_pb2.WORKER_RUNTIME_STATE_READY,
                target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
                compatibility=discovery_pb2.CompatibilityContract(major=3, revision=1),
            )
            # Published bounds guard the startup.
            server.lifecycle_bounds.SetInParent()
            return server
        if name == "ListCapabilities":
            return discovery_pb2.ListCapabilitiesResponse(
                protocol_package=PROTOCOL_PACKAGE,
                spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
            )
        if name == "StartSpatialAnalyzerSdk":
            self._generation += 1
            return lifecycle_pb2.StartSpatialAnalyzerSdkResponse(
                state=sdk_state(self._generation)
            )
        if name == "StopSpatialAnalyzerSdk":
            self._generation = 0
            return lifecycle_pb2.StopSpatialAnalyzerSdkResponse(state=sdk_state(0))
        if name == "LaunchSpatialAnalyzer":
            return lifecycle_pb2.LaunchSpatialAnalyzerResponse(
                state=lifecycle_pb2.SpatialAnalyzerLifecycleState(
                    state_revision=1,
                    application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING,
                    ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED,
                    application_generation=1,
                )
            )
        raise AssertionError(name)


class Effects:
    """Moves the clock past the 120 s budget when a launch value runs code."""

    loop: VirtualClockLoop | None = None
    ran: list[str] = []  # noqa: RUF012

    @classmethod
    def run(cls, what: str) -> None:
        if cls.loop is not None:
            cls.ran.append(what)
            cls.loop.now = T0 + 121.0


class Text(str):
    __slots__ = ()

    def encode(self, *args: Any, **kwargs: Any) -> bytes:
        Effects.run("encode")
        return str.__str__(self).encode(*args, **kwargs)


class Flag:
    def __bool__(self) -> bool:
        Effects.run("bool")
        return True


async def launch(loop: VirtualClockLoop, value: str) -> dict[str, Any]:
    calls: list[tuple[str, float, Any]] = []
    transport = GrpcClientTransport("127.0.0.1:9")
    stub = Stub(loop, calls)
    transport._discovery = stub  # type: ignore[assignment]
    transport._application = stub  # type: ignore[assignment]
    transport._sdk = stub  # type: ignore[assignment]
    client = BriosaClient(
        _server_launcher=Launcher(), _transport_factory=lambda _target: transport
    )
    launch_options = (
        SpatialAnalyzerLaunchOptions(quick_start_instrument_name=Text("Tracker"))
        if value == "text"
        else SpatialAnalyzerLaunchOptions(start_minimized=Flag())  # type: ignore[arg-type]
    )
    options = BriosaStartOptions(
        connect_to_spatial_analyzer=False, launch_options=launch_options
    )
    Effects.ran = []
    Effects.loop = loop
    outcome = "started"
    try:
        await client.start(options)
    except Exception as error:
        # On Python 3.10 the expiry is a private BriosaStartupError subclass.
        kind = (
            "BriosaStartupError"
            if isinstance(error, BriosaStartupError)
            else type(error).__name__
        )
        outcome = f"{kind}({getattr(error, 'diagnostic_code', '')})"
    finally:
        Effects.loop = None
    launched = [
        request for name, _, request in calls if name == "LaunchSpatialAnalyzer"
    ]
    await client.stop()
    return {
        "outcome": outcome,
        "ran": list(Effects.ran),
        "calls": [f"{name}@{at:g}" for name, at, _ in calls],
        "instrument_types": [
            type(request.quick_start_instrument_name).__name__ for request in launched
        ],
    }


def probe() -> dict[str, Any]:
    async def body(loop: VirtualClockLoop) -> dict[str, Any]:
        return {value: await launch(loop, value) for value in ("text", "bool")}

    return {
        "protobuf": api_implementation.Type(),
        **run_virtual(body, now=T0),
    }


if __name__ == "__main__":
    print(json.dumps(probe()))
