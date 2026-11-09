"""Shared fakes for facade tests: a ready server and a recording transport."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import grpc
from google.protobuf.message import Message

from briosa import (
    BriosaClient,
    BriosaLoggingOptions,
    BriosaServerSelection,
    SpatialAnalyzerLaunchOptions,
    discovery_pb2,
    lifecycle_pb2,
    operation_outcomes_pb2,
)
from briosa.client import OwnedServer
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)
from briosa.wave_a_operations import WAVE_A_OPERATIONS
from briosa.wave_b_operations import (
    WAVE_B_OPERATIONS,
    ConstructionOperations,
    GdtOperations,
    InstrumentOperations,
    RobotCalibrationApplianceNodeOperations,
    RobotOperations,
)

GROUPED_SURFACES = {
    "construction_operations": ConstructionOperations,
    "gdt_operations": GdtOperations,
    "instrument_operations": InstrumentOperations,
    "robot_calibration_appliance_node_operations": (
        RobotCalibrationApplianceNodeOperations
    ),
    "robot_operations": RobotOperations,
}
ACTIVE_COLLECTION_OPERATION = "construction_operations.get_active_collection_name"


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


class ReadyServer:
    target = "127.0.0.1:49152"
    has_exited = False

    async def close(self) -> None:
        return None


class ReadyLauncher:
    async def launch(
        self,
        logging: BriosaLoggingOptions | None = None,
        selection: BriosaServerSelection | None = None,
    ) -> OwnedServer:
        return ReadyServer()


def succeeded(code: int = 2) -> operation_outcomes_pb2.MpExecutionDetails:
    return operation_outcomes_pb2.MpExecutionDetails(
        state=operation_outcomes_pb2.MP_EXECUTION_STATE_SUCCEEDED,
        mp_result_code=code,
    )


class RecordingTransport:
    """A ready server whose MP calls answer with queued or default responses."""

    def __init__(self) -> None:
        self.requests: list[tuple[str, Message, float | None]] = []
        self.queued: dict[str, list[Message | grpc.RpcError]] = {}
        self.default_response: Callable[[str, type[Message]], Message] = (
            lambda _path, response_type: response_type(execution=succeeded())
        )
        self.capabilities: list[discovery_pb2.OperationCapability] = []
        self.denied_capabilities: list[discovery_pb2.OperationCapability] = []
        self.admission_profile = "standard"
        self.policy_fingerprint = "sha256:" + "0" * 64
        self.include_denied_requests: list[bool] = []

    def queue(self, path: str, *responses: Message | grpc.RpcError) -> None:
        self.queued.setdefault(path, []).extend(responses)

    def last_request(self, path: str | None = None) -> Message:
        matching = [item for item in self.requests if path in (None, item[0])]
        assert matching, f"no request recorded for {path}"
        return matching[-1][1]

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        return self.server_info(), await self.list_capabilities(timeout=timeout)

    async def list_capabilities(
        self, *, include_denied: bool = False, timeout: float | None = None
    ) -> discovery_pb2.ListCapabilitiesResponse:
        self.include_denied_requests.append(include_denied)
        operations = [*self.capabilities]
        if include_denied:
            operations.extend(self.denied_capabilities)
        operations.sort(key=lambda item: item.operation_id)
        return discovery_pb2.ListCapabilitiesResponse(
            protocol_package=PROTOCOL_PACKAGE,
            spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
            operations=operations,
            admission_profile=self.admission_profile,
            policy_fingerprint=self.policy_fingerprint,
        )

    def server_info(self) -> discovery_pb2.GetServerInfoResponse:
        return discovery_pb2.GetServerInfoResponse(
            version={
                "briosa_version": BRIOSA_VERSION,
                "source_revision": SOURCE_REVISION,
                "protocol_package": PROTOCOL_PACKAGE,
                "spatial_analyzer_target": SPATIAL_ANALYZER_TARGET,
            },
            worker_state=discovery_pb2.WORKER_RUNTIME_STATE_READY,
            spatial_analyzer_connection_state=(
                discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED
            ),
            spatial_analyzer_execution_readiness_state=(
                discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
            ),
            ready_for_mp=True,
            target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
            compatibility=discovery_pb2.CompatibilityContract(major=3),
        )

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        return self._application_state()

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        return self._application_state()

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        return self._application_state()

    async def get_sdk_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return self._sdk_state()

    async def start_sdk(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return self._sdk_state()

    async def connect_sdk(
        self,
        expected_generation: int,
        *,
        reconnect: bool,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return self._sdk_state()

    async def stop_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return self._sdk_state()

    async def recover_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return self._sdk_state()

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message:
        self.requests.append((path, request, timeout))
        queued = self.queued.get(path)
        if queued:
            response = queued.pop(0)
            if isinstance(response, grpc.RpcError):
                raise response
            return response
        return self.default_response(path, response_type)

    async def close(self) -> None:
        return None

    @staticmethod
    def _application_state() -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        return lifecycle_pb2.SpatialAnalyzerLifecycleState(
            state_revision=1,
            application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING,
            ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_EXTERNAL,
            application_generation=1,
        )

    @staticmethod
    def _sdk_state() -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        return lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
            state_revision=2,
            sdk_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_READY,
            sdk_generation=1,
            application_generation=1,
            connection_state=discovery_pb2.SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED,
            execution_readiness_state=(
                discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
            ),
            ready_for_mp=True,
            recovery_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED,
        )


async def started_client(transport: RecordingTransport) -> BriosaClient:
    client = BriosaClient(
        _server_launcher=ReadyLauncher(),
        _transport_factory=lambda _target: transport,
    )
    await client.start()
    return client


def facade_functions() -> dict[str, Callable[..., Any]]:
    """Return the unbound facade function of every MP operation by ID."""
    functions: dict[str, Callable[..., Any]] = {
        operation_id: getattr(BriosaClient, method_name)
        for method_name, _service, _rpc, operation_id in WAVE_A_OPERATIONS
    }
    functions[ACTIVE_COLLECTION_OPERATION] = BriosaClient.get_active_collection_name
    for operation_id in WAVE_B_OPERATIONS:
        method_name = operation_id.split(".", maxsplit=1)[1]
        owners = [
            surface
            for surface in (BriosaClient, *GROUPED_SURFACES.values())
            if hasattr(surface, method_name)
        ]
        assert len(owners) == 1, operation_id
        functions[operation_id] = getattr(owners[0], method_name)
    return functions


def bound_facades(client: BriosaClient) -> dict[str, Callable[..., Any]]:
    """Return the bound facade method of every MP operation by ID."""
    bound: dict[str, Callable[..., Any]] = {}
    for operation_id, function in facade_functions().items():
        owner = function.__qualname__.split(".", maxsplit=1)[0]
        attribute = next(
            (
                name
                for name, surface in GROUPED_SURFACES.items()
                if surface.__name__ == owner
            ),
            None,
        )
        target = client if attribute is None else getattr(client, attribute)
        bound[operation_id] = getattr(target, function.__name__)
    return bound
