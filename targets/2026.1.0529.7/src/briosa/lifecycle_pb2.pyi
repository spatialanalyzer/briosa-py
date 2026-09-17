from briosa import discovery_pb2 as _discovery_pb2
from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpatialAnalyzerApplicationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_APPLICATION_STATE_UNSPECIFIED: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_NOT_RUNNING: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_STARTING: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_CLOSING: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_EXITED: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_AMBIGUOUS: _ClassVar[SpatialAnalyzerApplicationState]
    SPATIAL_ANALYZER_APPLICATION_STATE_FAULTED: _ClassVar[SpatialAnalyzerApplicationState]

class SpatialAnalyzerOwnership(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_OWNERSHIP_UNSPECIFIED: _ClassVar[SpatialAnalyzerOwnership]
    SPATIAL_ANALYZER_OWNERSHIP_NONE: _ClassVar[SpatialAnalyzerOwnership]
    SPATIAL_ANALYZER_OWNERSHIP_EXTERNAL: _ClassVar[SpatialAnalyzerOwnership]
    SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED: _ClassVar[SpatialAnalyzerOwnership]

class SpatialAnalyzerSdkState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_SDK_STATE_UNSPECIFIED: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_STOPPED: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_STARTING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_RUNNING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_CONNECTING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_VERIFYING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_READY: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_STOPPING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_RECOVERING: _ClassVar[SpatialAnalyzerSdkState]
    SPATIAL_ANALYZER_SDK_STATE_FAULTED: _ClassVar[SpatialAnalyzerSdkState]

class SpatialAnalyzerSdkRecoveryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_SDK_RECOVERY_STATE_UNSPECIFIED: _ClassVar[SpatialAnalyzerSdkRecoveryState]
    SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED: _ClassVar[SpatialAnalyzerSdkRecoveryState]
    SPATIAL_ANALYZER_SDK_RECOVERY_STATE_RECOVERY_AVAILABLE: _ClassVar[SpatialAnalyzerSdkRecoveryState]
    SPATIAL_ANALYZER_SDK_RECOVERY_STATE_OPERATOR_ACTION_REQUIRED: _ClassVar[SpatialAnalyzerSdkRecoveryState]
    SPATIAL_ANALYZER_SDK_RECOVERY_STATE_BLOCKED: _ClassVar[SpatialAnalyzerSdkRecoveryState]

class SpatialAnalyzerSdkTerminationKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_UNSPECIFIED: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_START_FAILED: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_SDK_PROCESS_EXITED: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_SDK_CONNECTION_LOST: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_WORKER_PROCESS_EXITED: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_CONTROL_CHANNEL_LOST: _ClassVar[SpatialAnalyzerSdkTerminationKind]
    SPATIAL_ANALYZER_SDK_TERMINATION_KIND_WATCHDOG_TERMINATED: _ClassVar[SpatialAnalyzerSdkTerminationKind]

class SpatialAnalyzerSdkRecoveryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_SDK_RECOVERY_MODE_UNSPECIFIED: _ClassVar[SpatialAnalyzerSdkRecoveryMode]
    SPATIAL_ANALYZER_SDK_RECOVERY_MODE_REPLACE_WITHOUT_REPLAY: _ClassVar[SpatialAnalyzerSdkRecoveryMode]

class SpatialAnalyzerLifecycleFailureKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_UNSPECIFIED: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_VALIDATION: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_STATE_CONFLICT: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_APPLICATION_NOT_FOUND: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_APPLICATION_AMBIGUOUS: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_LAUNCH_FAILED: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_NOT_OWNED: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_SDK_NOT_STOPPED: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_TIMEOUT: _ClassVar[SpatialAnalyzerLifecycleFailureKind]
    SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_INTERNAL: _ClassVar[SpatialAnalyzerLifecycleFailureKind]

class SpatialAnalyzerSdkLifecycleFailureKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_UNSPECIFIED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_VALIDATION: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_STATE_CONFLICT: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_APPLICATION_NOT_FOUND: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_APPLICATION_AMBIGUOUS: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_ALREADY_ACTIVE: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_NOT_RUNNING: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_START_FAILED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_STOP_FAILED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_RECOVERY_NOT_REQUIRED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_RECOVERY_FAILED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_IDENTITY_MISMATCH: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_OPERATOR_ACTION_REQUIRED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_TIMEOUT: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_INTERNAL: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_ALREADY_CONNECTED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_CONNECTION_FAILED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_RECONNECT_NOT_REQUIRED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]
    SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_RECOVERY_REQUIRED: _ClassVar[SpatialAnalyzerSdkLifecycleFailureKind]

class LifecycleRecoveryGuidance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFECYCLE_RECOVERY_GUIDANCE_UNSPECIFIED: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_NONE: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_REFRESH_STATE: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_RETRY_AFTER_STATE_CHANGE: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_CORRECT_ENVIRONMENT: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_STOP_SDK_FIRST: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_RECOVER_SDK_WITHOUT_REPLAY: _ClassVar[LifecycleRecoveryGuidance]
    LIFECYCLE_RECOVERY_GUIDANCE_OPERATOR_ACTION_REQUIRED: _ClassVar[LifecycleRecoveryGuidance]
SPATIAL_ANALYZER_APPLICATION_STATE_UNSPECIFIED: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_NOT_RUNNING: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_STARTING: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_RUNNING: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_CLOSING: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_EXITED: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_AMBIGUOUS: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_APPLICATION_STATE_FAULTED: SpatialAnalyzerApplicationState
SPATIAL_ANALYZER_OWNERSHIP_UNSPECIFIED: SpatialAnalyzerOwnership
SPATIAL_ANALYZER_OWNERSHIP_NONE: SpatialAnalyzerOwnership
SPATIAL_ANALYZER_OWNERSHIP_EXTERNAL: SpatialAnalyzerOwnership
SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED: SpatialAnalyzerOwnership
SPATIAL_ANALYZER_SDK_STATE_UNSPECIFIED: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_STOPPED: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_STARTING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_RUNNING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_CONNECTING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_VERIFYING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_READY: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_STOPPING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_RECOVERING: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_STATE_FAULTED: SpatialAnalyzerSdkState
SPATIAL_ANALYZER_SDK_RECOVERY_STATE_UNSPECIFIED: SpatialAnalyzerSdkRecoveryState
SPATIAL_ANALYZER_SDK_RECOVERY_STATE_NOT_REQUIRED: SpatialAnalyzerSdkRecoveryState
SPATIAL_ANALYZER_SDK_RECOVERY_STATE_RECOVERY_AVAILABLE: SpatialAnalyzerSdkRecoveryState
SPATIAL_ANALYZER_SDK_RECOVERY_STATE_OPERATOR_ACTION_REQUIRED: SpatialAnalyzerSdkRecoveryState
SPATIAL_ANALYZER_SDK_RECOVERY_STATE_BLOCKED: SpatialAnalyzerSdkRecoveryState
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_UNSPECIFIED: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_START_FAILED: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_SDK_PROCESS_EXITED: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_SDK_CONNECTION_LOST: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_WORKER_PROCESS_EXITED: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_CONTROL_CHANNEL_LOST: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_TERMINATION_KIND_WATCHDOG_TERMINATED: SpatialAnalyzerSdkTerminationKind
SPATIAL_ANALYZER_SDK_RECOVERY_MODE_UNSPECIFIED: SpatialAnalyzerSdkRecoveryMode
SPATIAL_ANALYZER_SDK_RECOVERY_MODE_REPLACE_WITHOUT_REPLAY: SpatialAnalyzerSdkRecoveryMode
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_UNSPECIFIED: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_VALIDATION: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_STATE_CONFLICT: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_APPLICATION_NOT_FOUND: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_APPLICATION_AMBIGUOUS: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_LAUNCH_FAILED: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_NOT_OWNED: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_SDK_NOT_STOPPED: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_TIMEOUT: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_INTERNAL: SpatialAnalyzerLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_UNSPECIFIED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_VALIDATION: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_STATE_CONFLICT: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_APPLICATION_NOT_FOUND: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_APPLICATION_AMBIGUOUS: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_ALREADY_ACTIVE: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_NOT_RUNNING: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_START_FAILED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_STOP_FAILED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_RECOVERY_NOT_REQUIRED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_RECOVERY_FAILED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_IDENTITY_MISMATCH: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_OPERATOR_ACTION_REQUIRED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_TIMEOUT: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_INTERNAL: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_ALREADY_CONNECTED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_CONNECTION_FAILED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_RECONNECT_NOT_REQUIRED: SpatialAnalyzerSdkLifecycleFailureKind
SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_SDK_RECOVERY_REQUIRED: SpatialAnalyzerSdkLifecycleFailureKind
LIFECYCLE_RECOVERY_GUIDANCE_UNSPECIFIED: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_NONE: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_REFRESH_STATE: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_RETRY_AFTER_STATE_CHANGE: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_CORRECT_ENVIRONMENT: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_STOP_SDK_FIRST: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_RECOVER_SDK_WITHOUT_REPLAY: LifecycleRecoveryGuidance
LIFECYCLE_RECOVERY_GUIDANCE_OPERATOR_ACTION_REQUIRED: LifecycleRecoveryGuidance

class GetSpatialAnalyzerStateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpatialAnalyzerStateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerLifecycleState, _Mapping]] = ...) -> None: ...

class LaunchSpatialAnalyzerRequest(_message.Message):
    __slots__ = ("job_file_path", "quick_start_instrument_name", "start_minimized")
    JOB_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    QUICK_START_INSTRUMENT_NAME_FIELD_NUMBER: _ClassVar[int]
    START_MINIMIZED_FIELD_NUMBER: _ClassVar[int]
    job_file_path: str
    quick_start_instrument_name: str
    start_minimized: bool
    def __init__(self, job_file_path: _Optional[str] = ..., quick_start_instrument_name: _Optional[str] = ..., start_minimized: bool = ...) -> None: ...

class LaunchSpatialAnalyzerResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerLifecycleState, _Mapping]] = ...) -> None: ...

class CloseOwnedSpatialAnalyzerRequest(_message.Message):
    __slots__ = ("expected_application_generation",)
    EXPECTED_APPLICATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    expected_application_generation: int
    def __init__(self, expected_application_generation: _Optional[int] = ...) -> None: ...

class CloseOwnedSpatialAnalyzerResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerLifecycleState, _Mapping]] = ...) -> None: ...

class SpatialAnalyzerLifecycleState(_message.Message):
    __slots__ = ("state_revision", "application_state", "ownership", "application_generation", "diagnostic_code")
    STATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_STATE_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    state_revision: int
    application_state: SpatialAnalyzerApplicationState
    ownership: SpatialAnalyzerOwnership
    application_generation: int
    diagnostic_code: str
    def __init__(self, state_revision: _Optional[int] = ..., application_state: _Optional[_Union[SpatialAnalyzerApplicationState, str]] = ..., ownership: _Optional[_Union[SpatialAnalyzerOwnership, str]] = ..., application_generation: _Optional[int] = ..., diagnostic_code: _Optional[str] = ...) -> None: ...

class GetSpatialAnalyzerSdkStateRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSpatialAnalyzerSdkStateResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class StartSpatialAnalyzerSdkRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StartSpatialAnalyzerSdkResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class ConnectToSpatialAnalyzerRequest(_message.Message):
    __slots__ = ("expected_sdk_generation",)
    EXPECTED_SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    expected_sdk_generation: int
    def __init__(self, expected_sdk_generation: _Optional[int] = ...) -> None: ...

class ConnectToSpatialAnalyzerResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class ReconnectToSpatialAnalyzerRequest(_message.Message):
    __slots__ = ("expected_sdk_generation",)
    EXPECTED_SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    expected_sdk_generation: int
    def __init__(self, expected_sdk_generation: _Optional[int] = ...) -> None: ...

class ReconnectToSpatialAnalyzerResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class StopSpatialAnalyzerSdkRequest(_message.Message):
    __slots__ = ("expected_sdk_generation",)
    EXPECTED_SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    expected_sdk_generation: int
    def __init__(self, expected_sdk_generation: _Optional[int] = ...) -> None: ...

class StopSpatialAnalyzerSdkResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class RecoverSpatialAnalyzerSdkRequest(_message.Message):
    __slots__ = ("expected_sdk_generation", "mode")
    EXPECTED_SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    expected_sdk_generation: int
    mode: SpatialAnalyzerSdkRecoveryMode
    def __init__(self, expected_sdk_generation: _Optional[int] = ..., mode: _Optional[_Union[SpatialAnalyzerSdkRecoveryMode, str]] = ...) -> None: ...

class RecoverSpatialAnalyzerSdkResponse(_message.Message):
    __slots__ = ("state",)
    STATE_FIELD_NUMBER: _ClassVar[int]
    state: SpatialAnalyzerSdkLifecycleState
    def __init__(self, state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ...) -> None: ...

class SpatialAnalyzerSdkLifecycleState(_message.Message):
    __slots__ = ("state_revision", "sdk_state", "sdk_generation", "application_generation", "connection_state", "execution_readiness_state", "ready_for_mp", "recovery_state", "last_incident", "diagnostic_code")
    STATE_REVISION_FIELD_NUMBER: _ClassVar[int]
    SDK_STATE_FIELD_NUMBER: _ClassVar[int]
    SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_GENERATION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_READINESS_STATE_FIELD_NUMBER: _ClassVar[int]
    READY_FOR_MP_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_INCIDENT_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    state_revision: int
    sdk_state: SpatialAnalyzerSdkState
    sdk_generation: int
    application_generation: int
    connection_state: _discovery_pb2.SpatialAnalyzerConnectionState
    execution_readiness_state: _discovery_pb2.SpatialAnalyzerExecutionReadinessState
    ready_for_mp: bool
    recovery_state: SpatialAnalyzerSdkRecoveryState
    last_incident: SpatialAnalyzerSdkIncident
    diagnostic_code: str
    def __init__(self, state_revision: _Optional[int] = ..., sdk_state: _Optional[_Union[SpatialAnalyzerSdkState, str]] = ..., sdk_generation: _Optional[int] = ..., application_generation: _Optional[int] = ..., connection_state: _Optional[_Union[_discovery_pb2.SpatialAnalyzerConnectionState, str]] = ..., execution_readiness_state: _Optional[_Union[_discovery_pb2.SpatialAnalyzerExecutionReadinessState, str]] = ..., ready_for_mp: bool = ..., recovery_state: _Optional[_Union[SpatialAnalyzerSdkRecoveryState, str]] = ..., last_incident: _Optional[_Union[SpatialAnalyzerSdkIncident, _Mapping]] = ..., diagnostic_code: _Optional[str] = ...) -> None: ...

class SpatialAnalyzerSdkIncident(_message.Message):
    __slots__ = ("sdk_generation", "termination_kind", "execution_disposition", "operation_id", "diagnostic_code")
    SDK_GENERATION_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_KIND_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    sdk_generation: int
    termination_kind: SpatialAnalyzerSdkTerminationKind
    execution_disposition: _operation_outcomes_pb2.ExecutionDisposition
    operation_id: str
    diagnostic_code: str
    def __init__(self, sdk_generation: _Optional[int] = ..., termination_kind: _Optional[_Union[SpatialAnalyzerSdkTerminationKind, str]] = ..., execution_disposition: _Optional[_Union[_operation_outcomes_pb2.ExecutionDisposition, str]] = ..., operation_id: _Optional[str] = ..., diagnostic_code: _Optional[str] = ...) -> None: ...

class SpatialAnalyzerLifecycleError(_message.Message):
    __slots__ = ("rpc", "kind", "diagnostic_code", "state", "recovery_guidance")
    RPC_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    rpc: str
    kind: SpatialAnalyzerLifecycleFailureKind
    diagnostic_code: str
    state: SpatialAnalyzerLifecycleState
    recovery_guidance: LifecycleRecoveryGuidance
    def __init__(self, rpc: _Optional[str] = ..., kind: _Optional[_Union[SpatialAnalyzerLifecycleFailureKind, str]] = ..., diagnostic_code: _Optional[str] = ..., state: _Optional[_Union[SpatialAnalyzerLifecycleState, _Mapping]] = ..., recovery_guidance: _Optional[_Union[LifecycleRecoveryGuidance, str]] = ...) -> None: ...

class SpatialAnalyzerSdkLifecycleError(_message.Message):
    __slots__ = ("rpc", "kind", "diagnostic_code", "state", "recovery_guidance")
    RPC_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    rpc: str
    kind: SpatialAnalyzerSdkLifecycleFailureKind
    diagnostic_code: str
    state: SpatialAnalyzerSdkLifecycleState
    recovery_guidance: LifecycleRecoveryGuidance
    def __init__(self, rpc: _Optional[str] = ..., kind: _Optional[_Union[SpatialAnalyzerSdkLifecycleFailureKind, str]] = ..., diagnostic_code: _Optional[str] = ..., state: _Optional[_Union[SpatialAnalyzerSdkLifecycleState, _Mapping]] = ..., recovery_guidance: _Optional[_Union[LifecycleRecoveryGuidance, str]] = ...) -> None: ...
