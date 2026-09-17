"""Private generated-protocol transport and handwritten public mapping."""

from __future__ import annotations

import asyncio
from collections.abc import Iterable
from typing import Any, Protocol, TypeVar, cast

import grpc
from google.protobuf.message import DecodeError, Message

from briosa import (
    discovery_pb2,
    discovery_pb2_grpc,
    file_operations_pb2,
    file_operations_pb2_grpc,
    lifecycle_pb2,
    lifecycle_pb2_grpc,
    operation_outcomes_pb2,
)
from briosa.errors import (
    BriosaCompatibilityError,
    BriosaOperationError,
    BriosaProtocolError,
    BriosaSpatialAnalyzerError,
    BriosaSpatialAnalyzerSdkError,
    BriosaTransportError,
)
from briosa.models import (
    BriosaOperationCapability,
    BriosaServerSnapshot,
    ExecutionDisposition,
    LifecycleRecoveryGuidance,
    OperationFailure,
    OperationFailureKind,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    RpcStatusCode,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerConnectionState,
    SpatialAnalyzerExecutionReadinessState,
    SpatialAnalyzerLaunchOptions,
    SpatialAnalyzerLifecycleFailureKind,
    SpatialAnalyzerLifecycleState,
    SpatialAnalyzerOwnership,
    SpatialAnalyzerSdkIncident,
    SpatialAnalyzerSdkLifecycleFailureKind,
    SpatialAnalyzerSdkLifecycleState,
    SpatialAnalyzerSdkRecoveryState,
    SpatialAnalyzerSdkState,
    SpatialAnalyzerSdkTerminationKind,
)
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)

_APPLICATION_ERROR_TRAILER = "briosa-spatial-analyzer-lifecycle-error-bin"
_SDK_ERROR_TRAILER = "briosa-spatial-analyzer-sdk-lifecycle-error-bin"
_OPERATION_ERROR_TRAILER = "briosa-operation-error-bin"

_EnumValue = TypeVar("_EnumValue")


class ClientTransport(Protocol):
    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]: ...

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState: ...

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState: ...

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState: ...

    async def get_sdk_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState: ...

    async def start_sdk(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState: ...

    async def connect_sdk(
        self,
        expected_generation: int,
        *,
        reconnect: bool,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState: ...

    async def stop_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState: ...

    async def recover_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState: ...

    async def get_working_directory(self, timeout: float | None = None) -> str: ...

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message: ...

    async def close(self) -> None: ...


class GrpcClientTransport:
    def __init__(self, target: str) -> None:
        self._channel = grpc.aio.insecure_channel(target)
        self._discovery = discovery_pb2_grpc.DiscoveryServiceStub(  # type: ignore[no-untyped-call]
            self._channel
        )
        self._application = lifecycle_pb2_grpc.SpatialAnalyzerLifecycleStub(
            self._channel  # type: ignore[no-untyped-call]
        )
        self._sdk = lifecycle_pb2_grpc.SpatialAnalyzerSdkLifecycleStub(  # type: ignore[no-untyped-call]
            self._channel
        )
        self._file_operations = file_operations_pb2_grpc.FileOperationsStub(
            self._channel  # type: ignore[no-untyped-call]
        )

    async def get_server_snapshot(
        self, timeout: float | None = None
    ) -> tuple[
        discovery_pb2.GetServerInfoResponse,
        discovery_pb2.ListCapabilitiesResponse,
    ]:
        server = await self._discovery.GetServerInfo(
            discovery_pb2.GetServerInfoRequest(), timeout=timeout
        )
        capabilities = await self._discovery.ListCapabilities(
            discovery_pb2.ListCapabilitiesRequest(), timeout=timeout
        )
        return cast(discovery_pb2.GetServerInfoResponse, server), cast(
            discovery_pb2.ListCapabilitiesResponse, capabilities
        )

    async def get_application_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        response = await self._application.GetSpatialAnalyzerState(
            lifecycle_pb2.GetSpatialAnalyzerStateRequest(), timeout=timeout
        )
        return cast(lifecycle_pb2.GetSpatialAnalyzerStateResponse, response).state

    async def launch_application(
        self,
        options: SpatialAnalyzerLaunchOptions,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        request = lifecycle_pb2.LaunchSpatialAnalyzerRequest(
            start_minimized=options.start_minimized
        )
        if options.job_file_path is not None:
            request.job_file_path = options.job_file_path
        elif options.quick_start_instrument_name is not None:
            request.quick_start_instrument_name = options.quick_start_instrument_name
        response = await self._application.LaunchSpatialAnalyzer(
            request, timeout=timeout
        )
        return cast(lifecycle_pb2.LaunchSpatialAnalyzerResponse, response).state

    async def close_application(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerLifecycleState:
        response = await self._application.CloseOwnedSpatialAnalyzer(
            lifecycle_pb2.CloseOwnedSpatialAnalyzerRequest(
                expected_application_generation=expected_generation
            ),
            timeout=timeout,
        )
        return cast(lifecycle_pb2.CloseOwnedSpatialAnalyzerResponse, response).state

    async def get_sdk_state(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        response = await self._sdk.GetSpatialAnalyzerSdkState(
            lifecycle_pb2.GetSpatialAnalyzerSdkStateRequest(), timeout=timeout
        )
        return cast(lifecycle_pb2.GetSpatialAnalyzerSdkStateResponse, response).state

    async def start_sdk(
        self, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        response = await self._sdk.StartSpatialAnalyzerSdk(
            lifecycle_pb2.StartSpatialAnalyzerSdkRequest(), timeout=timeout
        )
        return cast(lifecycle_pb2.StartSpatialAnalyzerSdkResponse, response).state

    async def connect_sdk(
        self,
        expected_generation: int,
        *,
        reconnect: bool,
        timeout: float | None = None,
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        if reconnect:
            response = await self._sdk.ReconnectToSpatialAnalyzer(
                lifecycle_pb2.ReconnectToSpatialAnalyzerRequest(
                    expected_sdk_generation=expected_generation
                ),
                timeout=timeout,
            )
            return cast(
                lifecycle_pb2.ReconnectToSpatialAnalyzerResponse, response
            ).state
        response = await self._sdk.ConnectToSpatialAnalyzer(
            lifecycle_pb2.ConnectToSpatialAnalyzerRequest(
                expected_sdk_generation=expected_generation
            ),
            timeout=timeout,
        )
        return cast(lifecycle_pb2.ConnectToSpatialAnalyzerResponse, response).state

    async def stop_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        response = await self._sdk.StopSpatialAnalyzerSdk(
            lifecycle_pb2.StopSpatialAnalyzerSdkRequest(
                expected_sdk_generation=expected_generation
            ),
            timeout=timeout,
        )
        return cast(lifecycle_pb2.StopSpatialAnalyzerSdkResponse, response).state

    async def recover_sdk(
        self, expected_generation: int, timeout: float | None = None
    ) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleState:
        response = await self._sdk.RecoverSpatialAnalyzerSdk(
            lifecycle_pb2.RecoverSpatialAnalyzerSdkRequest(
                expected_sdk_generation=expected_generation,
                mode=lifecycle_pb2.SPATIAL_ANALYZER_SDK_RECOVERY_MODE_REPLACE_WITHOUT_REPLAY,
            ),
            timeout=timeout,
        )
        return cast(lifecycle_pb2.RecoverSpatialAnalyzerSdkResponse, response).state

    async def get_working_directory(self, timeout: float | None = None) -> str:
        response = cast(
            file_operations_pb2.GetWorkingDirectoryResult,
            await self._file_operations.GetWorkingDirectory(
                file_operations_pb2.GetWorkingDirectoryRequest(), timeout=timeout
            ),
        )
        if not response.HasField("directory"):
            raise BriosaProtocolError("working-directory-missing")
        return response.directory

    async def invoke_operation(
        self,
        path: str,
        request: Message,
        response_type: type[Message],
        timeout: float | None = None,
    ) -> Message:
        call = self._channel.unary_unary(
            path,
            request_serializer=lambda value: value.SerializeToString(),
            response_deserializer=response_type.FromString,
        )
        return cast(Message, await call(request, timeout=timeout))

    async def close(self) -> None:
        await self._channel.close(None)


def map_snapshot(
    server: discovery_pb2.GetServerInfoResponse,
    capabilities: discovery_pb2.ListCapabilitiesResponse,
) -> BriosaServerSnapshot:
    _validate_compatibility(server, capabilities)
    version = server.version
    return BriosaServerSnapshot(
        briosa_version=version.briosa_version,
        source_revision=version.source_revision,
        protocol_package=version.protocol_package,
        spatial_analyzer_target=version.spatial_analyzer_target,
        ready_for_mp=server.ready_for_mp,
        operations=tuple(
            BriosaOperationCapability(
                operation_id=item.operation_id,
                grpc_service=item.grpc_service,
                rpc=item.rpc,
                fully_qualified_method=item.fully_qualified_method,
            )
            for item in capabilities.operations
        ),
    )


def map_application_state(
    state: lifecycle_pb2.SpatialAnalyzerLifecycleState,
) -> SpatialAnalyzerLifecycleState:
    generation = (
        _require_generation(
            state.application_generation, "application-generation-invalid"
        )
        if state.HasField("application_generation")
        else None
    )
    return SpatialAnalyzerLifecycleState(
        state_revision=state.state_revision,
        application_state=_enum_at(
            tuple(SpatialAnalyzerApplicationState), state.application_state
        ),
        ownership=_enum_at(tuple(SpatialAnalyzerOwnership), state.ownership),
        application_generation=generation,
        diagnostic_code=(
            state.diagnostic_code if state.HasField("diagnostic_code") else None
        ),
    )


def map_sdk_state(
    state: lifecycle_pb2.SpatialAnalyzerSdkLifecycleState,
) -> SpatialAnalyzerSdkLifecycleState:
    incident = None
    if state.HasField("last_incident"):
        raw = state.last_incident
        incident = SpatialAnalyzerSdkIncident(
            sdk_generation=_require_generation(
                raw.sdk_generation, "incident-generation-invalid"
            ),
            termination_kind=_enum_at(
                tuple(SpatialAnalyzerSdkTerminationKind), raw.termination_kind
            ),
            execution_disposition=(
                _enum_at(tuple(ExecutionDisposition), raw.execution_disposition)
                if raw.HasField("execution_disposition")
                else None
            ),
            operation_id=raw.operation_id if raw.HasField("operation_id") else None,
            diagnostic_code=(
                raw.diagnostic_code if raw.HasField("diagnostic_code") else None
            ),
        )
    return SpatialAnalyzerSdkLifecycleState(
        state_revision=state.state_revision,
        sdk_state=_enum_at(tuple(SpatialAnalyzerSdkState), state.sdk_state),
        sdk_generation=(
            _require_generation(state.sdk_generation, "sdk-generation-invalid")
            if state.HasField("sdk_generation")
            else None
        ),
        application_generation=(
            _require_generation(
                state.application_generation, "sdk-application-generation-invalid"
            )
            if state.HasField("application_generation")
            else None
        ),
        connection_state=_enum_at(
            tuple(SpatialAnalyzerConnectionState), state.connection_state
        ),
        execution_readiness_state=_enum_at(
            tuple(SpatialAnalyzerExecutionReadinessState),
            state.execution_readiness_state,
        ),
        ready_for_mp=state.ready_for_mp,
        recovery_state=_enum_at(
            tuple(SpatialAnalyzerSdkRecoveryState), state.recovery_state
        ),
        last_incident=incident,
        diagnostic_code=(
            state.diagnostic_code if state.HasField("diagnostic_code") else None
        ),
    )


def map_rpc_error(
    error: grpc.RpcError,
    application_state: SpatialAnalyzerLifecycleState | None = None,
) -> BaseException:
    status = error.code()
    status_code = _rpc_status_code(status)

    application_detail = _parse_trailer(
        error, _APPLICATION_ERROR_TRAILER, lifecycle_pb2.SpatialAnalyzerLifecycleError
    )
    if application_detail is not None:
        return BriosaSpatialAnalyzerError(
            _enum_at(
                tuple(SpatialAnalyzerLifecycleFailureKind), application_detail.kind
            ),
            application_detail.diagnostic_code,
            _enum_at(
                tuple(LifecycleRecoveryGuidance),
                application_detail.recovery_guidance,
            ),
            map_application_state(application_detail.state),
        )

    sdk_detail = _parse_trailer(
        error, _SDK_ERROR_TRAILER, lifecycle_pb2.SpatialAnalyzerSdkLifecycleError
    )
    if sdk_detail is not None:
        kind = _enum_at(tuple(SpatialAnalyzerSdkLifecycleFailureKind), sdk_detail.kind)
        if kind is SpatialAnalyzerSdkLifecycleFailureKind.IDENTITY_MISMATCH:
            return BriosaCompatibilityError(sdk_detail.diagnostic_code)
        if kind in {
            SpatialAnalyzerSdkLifecycleFailureKind.APPLICATION_NOT_FOUND,
            SpatialAnalyzerSdkLifecycleFailureKind.APPLICATION_AMBIGUOUS,
        }:
            return BriosaSpatialAnalyzerError(
                SpatialAnalyzerLifecycleFailureKind.APPLICATION_NOT_FOUND
                if kind is SpatialAnalyzerSdkLifecycleFailureKind.APPLICATION_NOT_FOUND
                else SpatialAnalyzerLifecycleFailureKind.APPLICATION_AMBIGUOUS,
                sdk_detail.diagnostic_code,
                _enum_at(
                    tuple(LifecycleRecoveryGuidance), sdk_detail.recovery_guidance
                ),
                application_state or _synthetic_application_state(kind),
            )
        return BriosaSpatialAnalyzerSdkError(
            kind,
            sdk_detail.diagnostic_code,
            _enum_at(tuple(LifecycleRecoveryGuidance), sdk_detail.recovery_guidance),
            map_sdk_state(sdk_detail.state),
        )

    try:
        operation = _parse_trailer(
            error, _OPERATION_ERROR_TRAILER, operation_outcomes_pb2.OperationError
        )
    except BriosaProtocolError:
        return BriosaTransportError(status_code, "typed-error-malformed")
    if operation is not None:
        if not operation.operation_id.strip() or not operation.diagnostic_code.strip():
            return BriosaTransportError(status_code, "typed-error-malformed")
        try:
            failure = OperationFailure(
                operation_id=operation.operation_id,
                kind=_enum_at(tuple(OperationFailureKind), operation.kind),
                diagnostic_code=operation.diagnostic_code,
                execution_disposition=_enum_at(
                    tuple(ExecutionDisposition), operation.execution_disposition
                ),
                recovery_guidance=_enum_at(
                    tuple(RecoveryGuidance), operation.recovery_guidance
                ),
                replay_guidance=_enum_at(
                    tuple(ReplayGuidance), operation.replay_guidance
                ),
                replay_safety=_enum_at(tuple(ReplaySafety), operation.replay_safety),
            )
        except BriosaProtocolError:
            return BriosaTransportError(status_code, "typed-error-malformed")
        return BriosaOperationError(status_code, failure)

    if status is grpc.StatusCode.CANCELLED:
        return asyncio.CancelledError()
    return BriosaTransportError(
        status_code, f"transport-{status_code.value.replace('_', '-')}"
    )


def _validate_compatibility(
    server: discovery_pb2.GetServerInfoResponse,
    capabilities: discovery_pb2.ListCapabilitiesResponse,
) -> None:
    if not server.HasField("version"):
        raise BriosaCompatibilityError("server-version-missing")
    version = server.version
    checks = (
        (version.briosa_version, BRIOSA_VERSION, "server-version-mismatch"),
        (version.source_revision, SOURCE_REVISION, "server-source-revision-mismatch"),
        (
            version.protocol_package,
            PROTOCOL_PACKAGE,
            "server-protocol-package-mismatch",
        ),
        (
            version.spatial_analyzer_target,
            SPATIAL_ANALYZER_TARGET,
            "server-sa-target-mismatch",
        ),
        (
            capabilities.protocol_package,
            PROTOCOL_PACKAGE,
            "capability-protocol-package-mismatch",
        ),
        (
            capabilities.spatial_analyzer_target,
            SPATIAL_ANALYZER_TARGET,
            "capability-sa-target-mismatch",
        ),
    )
    for actual, expected, diagnostic_code in checks:
        if actual != expected:
            raise BriosaCompatibilityError(diagnostic_code)
    if (
        server.target_isolation_mode
        != discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT
    ):
        raise BriosaCompatibilityError("target-isolation-mode-mismatch")


def _parse_trailer(error: grpc.RpcError, key: str, message_type: Any) -> Any | None:
    metadata = cast(Iterable[tuple[str, str | bytes]] | None, error.trailing_metadata())
    for item_key, value in metadata or ():
        if item_key != key:
            continue
        if not isinstance(value, bytes):
            raise BriosaProtocolError("typed-error-malformed")
        try:
            return message_type.FromString(value)
        except DecodeError as decode_error:
            raise BriosaProtocolError("typed-error-malformed") from decode_error
    return None


def _rpc_status_code(status: grpc.StatusCode) -> RpcStatusCode:
    try:
        return RpcStatusCode[status.name]
    except KeyError as error:
        raise BriosaProtocolError("unknown-rpc-status") from error


def _synthetic_application_state(
    kind: SpatialAnalyzerSdkLifecycleFailureKind,
) -> SpatialAnalyzerLifecycleState:
    return SpatialAnalyzerLifecycleState(
        state_revision=0,
        application_state=(
            SpatialAnalyzerApplicationState.NOT_RUNNING
            if kind is SpatialAnalyzerSdkLifecycleFailureKind.APPLICATION_NOT_FOUND
            else SpatialAnalyzerApplicationState.AMBIGUOUS
        ),
        ownership=SpatialAnalyzerOwnership.NONE,
        application_generation=None,
        diagnostic_code=None,
    )


def _require_generation(value: int, diagnostic_code: str) -> int:
    if value <= 0:
        raise BriosaProtocolError(diagnostic_code)
    return value


def _enum_at(values: tuple[_EnumValue, ...], number: int) -> _EnumValue:
    try:
        return values[number]
    except IndexError as error:
        raise BriosaProtocolError("unknown-enum-value") from error
