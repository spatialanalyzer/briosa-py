from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MpExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP_EXECUTION_STATE_UNSPECIFIED: _ClassVar[MpExecutionState]
    MP_EXECUTION_STATE_SUCCEEDED: _ClassVar[MpExecutionState]
    MP_EXECUTION_STATE_EXECUTE_STEP_REJECTED: _ClassVar[MpExecutionState]
    MP_EXECUTION_STATE_FAILED: _ClassVar[MpExecutionState]
    MP_EXECUTION_STATE_RESULT_UNAVAILABLE: _ClassVar[MpExecutionState]
    MP_EXECUTION_STATE_ARGUMENT_REJECTED: _ClassVar[MpExecutionState]

class OutputRetrievalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OUTPUT_RETRIEVAL_STATE_UNSPECIFIED: _ClassVar[OutputRetrievalState]
    OUTPUT_RETRIEVAL_STATE_RETRIEVED: _ClassVar[OutputRetrievalState]
    OUTPUT_RETRIEVAL_STATE_NOT_ATTEMPTED: _ClassVar[OutputRetrievalState]
    OUTPUT_RETRIEVAL_STATE_FAILED: _ClassVar[OutputRetrievalState]

class ExecutionDisposition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXECUTION_DISPOSITION_UNSPECIFIED: _ClassVar[ExecutionDisposition]
    EXECUTION_DISPOSITION_NOT_STARTED: _ClassVar[ExecutionDisposition]
    EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN: _ClassVar[ExecutionDisposition]
    EXECUTION_DISPOSITION_COMPLETED: _ClassVar[ExecutionDisposition]

class RecoveryGuidance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECOVERY_GUIDANCE_UNSPECIFIED: _ClassVar[RecoveryGuidance]
    RECOVERY_GUIDANCE_NONE: _ClassVar[RecoveryGuidance]
    RECOVERY_GUIDANCE_WAIT_FOR_READINESS: _ClassVar[RecoveryGuidance]
    RECOVERY_GUIDANCE_WORKER_REPLACEMENT: _ClassVar[RecoveryGuidance]
    RECOVERY_GUIDANCE_OPERATOR_INTERVENTION_REQUIRED: _ClassVar[RecoveryGuidance]

class ReplayGuidance(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLAY_GUIDANCE_UNSPECIFIED: _ClassVar[ReplayGuidance]
    REPLAY_GUIDANCE_DO_NOT_REPLAY: _ClassVar[ReplayGuidance]
    REPLAY_GUIDANCE_MAY_REPLAY: _ClassVar[ReplayGuidance]
    REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY: _ClassVar[ReplayGuidance]

class ReplaySafety(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLAY_SAFETY_UNSPECIFIED: _ClassVar[ReplaySafety]
    REPLAY_SAFETY_SAFE: _ClassVar[ReplaySafety]
    REPLAY_SAFETY_UNSAFE: _ClassVar[ReplaySafety]
    REPLAY_SAFETY_UNKNOWN: _ClassVar[ReplaySafety]

class OperationFailureKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATION_FAILURE_KIND_UNSPECIFIED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_VALIDATION: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_UNSUPPORTED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_SPATIAL_ANALYZER_UNAVAILABLE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_WORKER_UNAVAILABLE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_CALLER_CANCELLED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_CALLER_DEADLINE_EXCEEDED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_WORKER_WATCHDOG_TIMEOUT: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_WORKER_FAILURE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_EXECUTE_STEP_REJECTED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_MP_FAILURE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_OUTPUT_RETRIEVAL_FAILURE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_INTERNAL: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_POLICY_DENIED: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_MP_RESULT_RETRIEVAL_FAILURE: _ClassVar[OperationFailureKind]
    OPERATION_FAILURE_KIND_SDK_ARGUMENT_REJECTED: _ClassVar[OperationFailureKind]
MP_EXECUTION_STATE_UNSPECIFIED: MpExecutionState
MP_EXECUTION_STATE_SUCCEEDED: MpExecutionState
MP_EXECUTION_STATE_EXECUTE_STEP_REJECTED: MpExecutionState
MP_EXECUTION_STATE_FAILED: MpExecutionState
MP_EXECUTION_STATE_RESULT_UNAVAILABLE: MpExecutionState
MP_EXECUTION_STATE_ARGUMENT_REJECTED: MpExecutionState
OUTPUT_RETRIEVAL_STATE_UNSPECIFIED: OutputRetrievalState
OUTPUT_RETRIEVAL_STATE_RETRIEVED: OutputRetrievalState
OUTPUT_RETRIEVAL_STATE_NOT_ATTEMPTED: OutputRetrievalState
OUTPUT_RETRIEVAL_STATE_FAILED: OutputRetrievalState
EXECUTION_DISPOSITION_UNSPECIFIED: ExecutionDisposition
EXECUTION_DISPOSITION_NOT_STARTED: ExecutionDisposition
EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN: ExecutionDisposition
EXECUTION_DISPOSITION_COMPLETED: ExecutionDisposition
RECOVERY_GUIDANCE_UNSPECIFIED: RecoveryGuidance
RECOVERY_GUIDANCE_NONE: RecoveryGuidance
RECOVERY_GUIDANCE_WAIT_FOR_READINESS: RecoveryGuidance
RECOVERY_GUIDANCE_WORKER_REPLACEMENT: RecoveryGuidance
RECOVERY_GUIDANCE_OPERATOR_INTERVENTION_REQUIRED: RecoveryGuidance
REPLAY_GUIDANCE_UNSPECIFIED: ReplayGuidance
REPLAY_GUIDANCE_DO_NOT_REPLAY: ReplayGuidance
REPLAY_GUIDANCE_MAY_REPLAY: ReplayGuidance
REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY: ReplayGuidance
REPLAY_SAFETY_UNSPECIFIED: ReplaySafety
REPLAY_SAFETY_SAFE: ReplaySafety
REPLAY_SAFETY_UNSAFE: ReplaySafety
REPLAY_SAFETY_UNKNOWN: ReplaySafety
OPERATION_FAILURE_KIND_UNSPECIFIED: OperationFailureKind
OPERATION_FAILURE_KIND_VALIDATION: OperationFailureKind
OPERATION_FAILURE_KIND_UNSUPPORTED: OperationFailureKind
OPERATION_FAILURE_KIND_SPATIAL_ANALYZER_UNAVAILABLE: OperationFailureKind
OPERATION_FAILURE_KIND_WORKER_UNAVAILABLE: OperationFailureKind
OPERATION_FAILURE_KIND_CALLER_CANCELLED: OperationFailureKind
OPERATION_FAILURE_KIND_CALLER_DEADLINE_EXCEEDED: OperationFailureKind
OPERATION_FAILURE_KIND_WORKER_WATCHDOG_TIMEOUT: OperationFailureKind
OPERATION_FAILURE_KIND_WORKER_FAILURE: OperationFailureKind
OPERATION_FAILURE_KIND_EXECUTE_STEP_REJECTED: OperationFailureKind
OPERATION_FAILURE_KIND_MP_FAILURE: OperationFailureKind
OPERATION_FAILURE_KIND_OUTPUT_RETRIEVAL_FAILURE: OperationFailureKind
OPERATION_FAILURE_KIND_INTERNAL: OperationFailureKind
OPERATION_FAILURE_KIND_POLICY_DENIED: OperationFailureKind
OPERATION_FAILURE_KIND_MP_RESULT_RETRIEVAL_FAILURE: OperationFailureKind
OPERATION_FAILURE_KIND_SDK_ARGUMENT_REJECTED: OperationFailureKind

class OutputRetrievalDetails(_message.Message):
    __slots__ = ("field_name", "state", "diagnostic_code")
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    state: OutputRetrievalState
    diagnostic_code: str
    def __init__(self, field_name: _Optional[str] = ..., state: _Optional[_Union[OutputRetrievalState, str]] = ..., diagnostic_code: _Optional[str] = ...) -> None: ...

class MpExecutionDetails(_message.Message):
    __slots__ = ("state", "mp_result_code", "output_retrievals")
    STATE_FIELD_NUMBER: _ClassVar[int]
    MP_RESULT_CODE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_RETRIEVALS_FIELD_NUMBER: _ClassVar[int]
    state: MpExecutionState
    mp_result_code: int
    output_retrievals: _containers.RepeatedCompositeFieldContainer[OutputRetrievalDetails]
    def __init__(self, state: _Optional[_Union[MpExecutionState, str]] = ..., mp_result_code: _Optional[int] = ..., output_retrievals: _Optional[_Iterable[_Union[OutputRetrievalDetails, _Mapping]]] = ...) -> None: ...

class OperationError(_message.Message):
    __slots__ = ("operation_id", "kind", "diagnostic_code", "worker_generation", "mp_execution", "execution_disposition", "recovery_guidance", "replay_guidance", "replay_safety")
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_CODE_FIELD_NUMBER: _ClassVar[int]
    WORKER_GENERATION_FIELD_NUMBER: _ClassVar[int]
    MP_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_DISPOSITION_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    REPLAY_SAFETY_FIELD_NUMBER: _ClassVar[int]
    operation_id: str
    kind: OperationFailureKind
    diagnostic_code: str
    worker_generation: int
    mp_execution: MpExecutionDetails
    execution_disposition: ExecutionDisposition
    recovery_guidance: RecoveryGuidance
    replay_guidance: ReplayGuidance
    replay_safety: ReplaySafety
    def __init__(self, operation_id: _Optional[str] = ..., kind: _Optional[_Union[OperationFailureKind, str]] = ..., diagnostic_code: _Optional[str] = ..., worker_generation: _Optional[int] = ..., mp_execution: _Optional[_Union[MpExecutionDetails, _Mapping]] = ..., execution_disposition: _Optional[_Union[ExecutionDisposition, str]] = ..., recovery_guidance: _Optional[_Union[RecoveryGuidance, str]] = ..., replay_guidance: _Optional[_Union[ReplayGuidance, str]] = ..., replay_safety: _Optional[_Union[ReplaySafety, str]] = ...) -> None: ...
