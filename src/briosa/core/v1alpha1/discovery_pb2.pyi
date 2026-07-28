from briosa.core.v1alpha1 import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa.core.v1alpha1 import version_coordinates_pb2 as _version_coordinates_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TargetIsolationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_ISOLATION_MODE_UNSPECIFIED: _ClassVar[TargetIsolationMode]
    TARGET_ISOLATION_MODE_SINGLE_TENANT: _ClassVar[TargetIsolationMode]
    TARGET_ISOLATION_MODE_LEASE_ISOLATED: _ClassVar[TargetIsolationMode]

class WorkerRuntimeState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKER_RUNTIME_STATE_UNSPECIFIED: _ClassVar[WorkerRuntimeState]
    WORKER_RUNTIME_STATE_STOPPED: _ClassVar[WorkerRuntimeState]
    WORKER_RUNTIME_STATE_STARTING: _ClassVar[WorkerRuntimeState]
    WORKER_RUNTIME_STATE_READY: _ClassVar[WorkerRuntimeState]
    WORKER_RUNTIME_STATE_DEGRADED: _ClassVar[WorkerRuntimeState]

class SpatialAnalyzerConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_CONNECTION_STATE_UNSPECIFIED: _ClassVar[SpatialAnalyzerConnectionState]
    SPATIAL_ANALYZER_CONNECTION_STATE_DISCONNECTED: _ClassVar[SpatialAnalyzerConnectionState]
    SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTING: _ClassVar[SpatialAnalyzerConnectionState]
    SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED: _ClassVar[SpatialAnalyzerConnectionState]
    SPATIAL_ANALYZER_CONNECTION_STATE_FAULTED: _ClassVar[SpatialAnalyzerConnectionState]
    SPATIAL_ANALYZER_CONNECTION_STATE_STOPPING: _ClassVar[SpatialAnalyzerConnectionState]

class SpatialAnalyzerExecutionReadinessState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNSPECIFIED: _ClassVar[SpatialAnalyzerExecutionReadinessState]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNVERIFIED: _ClassVar[SpatialAnalyzerExecutionReadinessState]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_VERIFYING: _ClassVar[SpatialAnalyzerExecutionReadinessState]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY: _ClassVar[SpatialAnalyzerExecutionReadinessState]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_COMPETING_CLIENT_SUSPECTED: _ClassVar[SpatialAnalyzerExecutionReadinessState]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_OPERATOR_RECOVERY_REQUIRED: _ClassVar[SpatialAnalyzerExecutionReadinessState]

class ConnectedSpatialAnalyzerVersionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_UNSPECIFIED: _ClassVar[ConnectedSpatialAnalyzerVersionState]
    CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_UNAVAILABLE: _ClassVar[ConnectedSpatialAnalyzerVersionState]
    CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_VERIFIED_MATCH: _ClassVar[ConnectedSpatialAnalyzerVersionState]
    CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_VERIFIED_MISMATCH: _ClassVar[ConnectedSpatialAnalyzerVersionState]

class OperationExecutionScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_EXECUTION_SCOPE_UNSPECIFIED: _ClassVar[OperationExecutionScope]
    OPERATION_EXECUTION_SCOPE_SELF_CONTAINED: _ClassVar[OperationExecutionScope]
    OPERATION_EXECUTION_SCOPE_GLOBAL_STATE_READ: _ClassVar[OperationExecutionScope]
    OPERATION_EXECUTION_SCOPE_GLOBAL_STATE_MUTATION: _ClassVar[OperationExecutionScope]
    OPERATION_EXECUTION_SCOPE_EXCLUSIVE_WORKFLOW: _ClassVar[OperationExecutionScope]
    OPERATION_EXECUTION_SCOPE_UNKNOWN: _ClassVar[OperationExecutionScope]

class OperationEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_EFFECT_UNSPECIFIED: _ClassVar[OperationEffect]
    OPERATION_EFFECT_READ_ONLY: _ClassVar[OperationEffect]
    OPERATION_EFFECT_MUTATING: _ClassVar[OperationEffect]
    OPERATION_EFFECT_UNKNOWN: _ClassVar[OperationEffect]
TARGET_ISOLATION_MODE_UNSPECIFIED: TargetIsolationMode
TARGET_ISOLATION_MODE_SINGLE_TENANT: TargetIsolationMode
TARGET_ISOLATION_MODE_LEASE_ISOLATED: TargetIsolationMode
WORKER_RUNTIME_STATE_UNSPECIFIED: WorkerRuntimeState
WORKER_RUNTIME_STATE_STOPPED: WorkerRuntimeState
WORKER_RUNTIME_STATE_STARTING: WorkerRuntimeState
WORKER_RUNTIME_STATE_READY: WorkerRuntimeState
WORKER_RUNTIME_STATE_DEGRADED: WorkerRuntimeState
SPATIAL_ANALYZER_CONNECTION_STATE_UNSPECIFIED: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_CONNECTION_STATE_DISCONNECTED: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTING: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_CONNECTION_STATE_CONNECTED: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_CONNECTION_STATE_FAULTED: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_CONNECTION_STATE_STOPPING: SpatialAnalyzerConnectionState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNSPECIFIED: SpatialAnalyzerExecutionReadinessState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_UNVERIFIED: SpatialAnalyzerExecutionReadinessState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_VERIFYING: SpatialAnalyzerExecutionReadinessState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY: SpatialAnalyzerExecutionReadinessState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_COMPETING_CLIENT_SUSPECTED: SpatialAnalyzerExecutionReadinessState
SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_OPERATOR_RECOVERY_REQUIRED: SpatialAnalyzerExecutionReadinessState
CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_UNSPECIFIED: ConnectedSpatialAnalyzerVersionState
CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_UNAVAILABLE: ConnectedSpatialAnalyzerVersionState
CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_VERIFIED_MATCH: ConnectedSpatialAnalyzerVersionState
CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_VERIFIED_MISMATCH: ConnectedSpatialAnalyzerVersionState
OPERATION_EXECUTION_SCOPE_UNSPECIFIED: OperationExecutionScope
OPERATION_EXECUTION_SCOPE_SELF_CONTAINED: OperationExecutionScope
OPERATION_EXECUTION_SCOPE_GLOBAL_STATE_READ: OperationExecutionScope
OPERATION_EXECUTION_SCOPE_GLOBAL_STATE_MUTATION: OperationExecutionScope
OPERATION_EXECUTION_SCOPE_EXCLUSIVE_WORKFLOW: OperationExecutionScope
OPERATION_EXECUTION_SCOPE_UNKNOWN: OperationExecutionScope
OPERATION_EFFECT_UNSPECIFIED: OperationEffect
OPERATION_EFFECT_READ_ONLY: OperationEffect
OPERATION_EFFECT_MUTATING: OperationEffect
OPERATION_EFFECT_UNKNOWN: OperationEffect

class GetServerInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetServerInfoResponse(_message.Message):
    __slots__ = ("version", "worker_state", "spatial_analyzer_connection_state", "ready_for_mp", "connected_spatial_analyzer_version", "connected_spatial_analyzer_version_state", "spatial_analyzer_execution_readiness_state", "target_isolation_mode")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WORKER_STATE_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_ANALYZER_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    READY_FOR_MP_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_SPATIAL_ANALYZER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_SPATIAL_ANALYZER_VERSION_STATE_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_FIELD_NUMBER: _ClassVar[int]
    TARGET_ISOLATION_MODE_FIELD_NUMBER: _ClassVar[int]
    version: _version_coordinates_pb2.VersionCoordinates
    worker_state: WorkerRuntimeState
    spatial_analyzer_connection_state: SpatialAnalyzerConnectionState
    ready_for_mp: bool
    connected_spatial_analyzer_version: str
    connected_spatial_analyzer_version_state: ConnectedSpatialAnalyzerVersionState
    spatial_analyzer_execution_readiness_state: SpatialAnalyzerExecutionReadinessState
    target_isolation_mode: TargetIsolationMode
    def __init__(self, version: _Optional[_Union[_version_coordinates_pb2.VersionCoordinates, _Mapping]] = ..., worker_state: _Optional[_Union[WorkerRuntimeState, str]] = ..., spatial_analyzer_connection_state: _Optional[_Union[SpatialAnalyzerConnectionState, str]] = ..., ready_for_mp: bool = ..., connected_spatial_analyzer_version: _Optional[str] = ..., connected_spatial_analyzer_version_state: _Optional[_Union[ConnectedSpatialAnalyzerVersionState, str]] = ..., spatial_analyzer_execution_readiness_state: _Optional[_Union[SpatialAnalyzerExecutionReadinessState, str]] = ..., target_isolation_mode: _Optional[_Union[TargetIsolationMode, str]] = ...) -> None: ...

class ListCapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListCapabilitiesResponse(_message.Message):
    __slots__ = ("catalog_id", "catalog_revision", "spatial_analyzer_target", "target_protocol_package", "operations")
    CATALOG_ID_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REVISION_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_ANALYZER_TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    catalog_id: str
    catalog_revision: str
    spatial_analyzer_target: str
    target_protocol_package: str
    operations: _containers.RepeatedCompositeFieldContainer[OperationCapability]
    def __init__(self, catalog_id: _Optional[str] = ..., catalog_revision: _Optional[str] = ..., spatial_analyzer_target: _Optional[str] = ..., target_protocol_package: _Optional[str] = ..., operations: _Optional[_Iterable[_Union[OperationCapability, _Mapping]]] = ...) -> None: ...

class OperationCapability(_message.Message):
    __slots__ = ("operation_id", "grpc_service", "rpc", "fully_qualified_method", "effect", "replay_safety", "execution_scope")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    GRPC_SERVICE_FIELD_NUMBER: _ClassVar[int]
    RPC_FIELD_NUMBER: _ClassVar[int]
    FULLY_QUALIFIED_METHOD_FIELD_NUMBER: _ClassVar[int]
    EFFECT_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SAFETY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    grpc_service: str
    rpc: str
    fully_qualified_method: str
    effect: OperationEffect
    replay_safety: _operation_outcomes_pb2.ReplaySafety
    execution_scope: OperationExecutionScope
    def __init__(self, operation_id: _Optional[str] = ..., grpc_service: _Optional[str] = ..., rpc: _Optional[str] = ..., fully_qualified_method: _Optional[str] = ..., effect: _Optional[_Union[OperationEffect, str]] = ..., replay_safety: _Optional[_Union[_operation_outcomes_pb2.ReplaySafety, str]] = ..., execution_scope: _Optional[_Union[OperationExecutionScope, str]] = ...) -> None: ...
