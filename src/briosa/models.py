"""Handwritten public lifecycle and discovery types."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import cast


class _StrEnum(str, Enum):
    def __str__(self) -> str:
        return cast(str, self.value)


class SpatialAnalyzerApplicationState(_StrEnum):
    UNSPECIFIED = "unspecified"
    NOT_RUNNING = "not_running"
    STARTING = "starting"
    RUNNING = "running"
    CLOSING = "closing"
    EXITED = "exited"
    AMBIGUOUS = "ambiguous"
    FAULTED = "faulted"


class SpatialAnalyzerOwnership(_StrEnum):
    UNSPECIFIED = "unspecified"
    NONE = "none"
    EXTERNAL = "external"
    SERVER_LAUNCHED = "server_launched"


class SpatialAnalyzerSdkState(_StrEnum):
    UNSPECIFIED = "unspecified"
    STOPPED = "stopped"
    STARTING = "starting"
    RUNNING = "running"
    CONNECTING = "connecting"
    VERIFYING = "verifying"
    READY = "ready"
    STOPPING = "stopping"
    RECOVERING = "recovering"
    FAULTED = "faulted"


class SpatialAnalyzerSdkRecoveryState(_StrEnum):
    UNSPECIFIED = "unspecified"
    NOT_REQUIRED = "not_required"
    RECOVERY_AVAILABLE = "recovery_available"
    OPERATOR_ACTION_REQUIRED = "operator_action_required"
    BLOCKED = "blocked"


class SpatialAnalyzerSdkTerminationKind(_StrEnum):
    UNSPECIFIED = "unspecified"
    START_FAILED = "start_failed"
    SDK_PROCESS_EXITED = "sdk_process_exited"
    SDK_CONNECTION_LOST = "sdk_connection_lost"
    WORKER_PROCESS_EXITED = "worker_process_exited"
    CONTROL_CHANNEL_LOST = "control_channel_lost"
    WATCHDOG_TERMINATED = "watchdog_terminated"


class SpatialAnalyzerSdkRecoveryMode(_StrEnum):
    REPLACE_WITHOUT_REPLAY = "replace_without_replay"


class SpatialAnalyzerConnectionState(_StrEnum):
    UNSPECIFIED = "unspecified"
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    FAULTED = "faulted"
    STOPPING = "stopping"


class SpatialAnalyzerExecutionReadinessState(_StrEnum):
    UNSPECIFIED = "unspecified"
    UNVERIFIED = "unverified"
    VERIFYING = "verifying"
    EXECUTION_READY = "execution_ready"
    COMPETING_CLIENT_SUSPECTED = "competing_client_suspected"
    OPERATOR_RECOVERY_REQUIRED = "operator_recovery_required"


class ExecutionDisposition(_StrEnum):
    UNSPECIFIED = "unspecified"
    NOT_STARTED = "not_started"
    STARTED_OUTCOME_UNKNOWN = "started_outcome_unknown"
    COMPLETED = "completed"


class OperationFailureKind(_StrEnum):
    UNSPECIFIED = "unspecified"
    VALIDATION = "validation"
    UNSUPPORTED = "unsupported"
    SPATIAL_ANALYZER_UNAVAILABLE = "spatial_analyzer_unavailable"
    WORKER_UNAVAILABLE = "worker_unavailable"
    CALLER_CANCELLED = "caller_cancelled"
    CALLER_DEADLINE_EXCEEDED = "caller_deadline_exceeded"
    WORKER_WATCHDOG_TIMEOUT = "worker_watchdog_timeout"
    WORKER_FAILURE = "worker_failure"
    EXECUTE_STEP_REJECTED = "execute_step_rejected"
    MP_FAILURE = "mp_failure"
    OUTPUT_RETRIEVAL_FAILURE = "output_retrieval_failure"
    INTERNAL = "internal"
    POLICY_DENIED = "policy_denied"
    MP_RESULT_RETRIEVAL_FAILURE = "mp_result_retrieval_failure"
    SDK_ARGUMENT_REJECTED = "sdk_argument_rejected"


class RecoveryGuidance(_StrEnum):
    UNSPECIFIED = "unspecified"
    NONE = "none"
    WAIT_FOR_READINESS = "wait_for_readiness"
    WORKER_REPLACEMENT = "worker_replacement"
    OPERATOR_INTERVENTION_REQUIRED = "operator_intervention_required"


class ReplayGuidance(_StrEnum):
    UNSPECIFIED = "unspecified"
    DO_NOT_REPLAY = "do_not_replay"
    MAY_REPLAY = "may_replay"
    RECONCILE_BEFORE_REPLAY = "reconcile_before_replay"


class ReplaySafety(_StrEnum):
    UNSPECIFIED = "unspecified"
    SAFE = "safe"
    UNSAFE = "unsafe"
    UNKNOWN = "unknown"


class RpcStatusCode(_StrEnum):
    OK = "ok"
    CANCELLED = "cancelled"
    UNKNOWN = "unknown"
    INVALID_ARGUMENT = "invalid_argument"
    DEADLINE_EXCEEDED = "deadline_exceeded"
    NOT_FOUND = "not_found"
    ALREADY_EXISTS = "already_exists"
    PERMISSION_DENIED = "permission_denied"
    RESOURCE_EXHAUSTED = "resource_exhausted"
    FAILED_PRECONDITION = "failed_precondition"
    ABORTED = "aborted"
    OUT_OF_RANGE = "out_of_range"
    UNIMPLEMENTED = "unimplemented"
    INTERNAL = "internal"
    UNAVAILABLE = "unavailable"
    DATA_LOSS = "data_loss"
    UNAUTHENTICATED = "unauthenticated"


class SpatialAnalyzerLifecycleFailureKind(_StrEnum):
    UNSPECIFIED = "unspecified"
    VALIDATION = "validation"
    STATE_CONFLICT = "state_conflict"
    APPLICATION_NOT_FOUND = "application_not_found"
    APPLICATION_AMBIGUOUS = "application_ambiguous"
    LAUNCH_FAILED = "launch_failed"
    NOT_OWNED = "not_owned"
    SDK_NOT_STOPPED = "sdk_not_stopped"
    TIMEOUT = "timeout"
    INTERNAL = "internal"


class SpatialAnalyzerSdkLifecycleFailureKind(_StrEnum):
    UNSPECIFIED = "unspecified"
    VALIDATION = "validation"
    STATE_CONFLICT = "state_conflict"
    APPLICATION_NOT_FOUND = "application_not_found"
    APPLICATION_AMBIGUOUS = "application_ambiguous"
    SDK_ALREADY_ACTIVE = "sdk_already_active"
    SDK_NOT_RUNNING = "sdk_not_running"
    SDK_START_FAILED = "sdk_start_failed"
    SDK_STOP_FAILED = "sdk_stop_failed"
    RECOVERY_NOT_REQUIRED = "recovery_not_required"
    SDK_RECOVERY_FAILED = "sdk_recovery_failed"
    IDENTITY_MISMATCH = "identity_mismatch"
    OPERATOR_ACTION_REQUIRED = "operator_action_required"
    TIMEOUT = "timeout"
    INTERNAL = "internal"
    SDK_ALREADY_CONNECTED = "sdk_already_connected"
    SDK_CONNECTION_FAILED = "sdk_connection_failed"
    RECONNECT_NOT_REQUIRED = "reconnect_not_required"
    SDK_RECOVERY_REQUIRED = "sdk_recovery_required"


class LifecycleRecoveryGuidance(_StrEnum):
    UNSPECIFIED = "unspecified"
    NONE = "none"
    REFRESH_STATE = "refresh_state"
    RETRY_AFTER_STATE_CHANGE = "retry_after_state_change"
    CORRECT_ENVIRONMENT = "correct_environment"
    STOP_SDK_FIRST = "stop_sdk_first"
    RECOVER_SDK_WITHOUT_REPLAY = "recover_sdk_without_replay"
    OPERATOR_ACTION_REQUIRED = "operator_action_required"


@dataclass(frozen=True, slots=True)
class BriosaClientOptions:
    command_timeout: float | None = None

    def __post_init__(self) -> None:
        if self.command_timeout is not None and self.command_timeout <= 0:
            raise ValueError("command_timeout must be positive when supplied")


@dataclass(frozen=True, slots=True)
class SpatialAnalyzerLaunchOptions:
    job_file_path: str | None = None
    quick_start_instrument_name: str | None = None
    start_minimized: bool = False

    def __post_init__(self) -> None:
        if (
            self.job_file_path is not None
            and self.quick_start_instrument_name is not None
        ):
            raise ValueError(
                "job_file_path and quick_start_instrument_name are mutually exclusive"
            )
        if self.job_file_path is not None and (
            not self.job_file_path.strip() or not Path(self.job_file_path).is_absolute()
        ):
            raise ValueError("job_file_path must be an absolute non-empty path")
        instrument = self.quick_start_instrument_name
        if instrument is not None and (
            not instrument.strip()
            or len(instrument) > 256
            or any(ord(character) < 32 for character in instrument)
        ):
            raise ValueError("quick_start_instrument_name is invalid")

    @property
    def is_default(self) -> bool:
        return (
            self.job_file_path is None
            and self.quick_start_instrument_name is None
            and not self.start_minimized
        )


@dataclass(frozen=True, slots=True)
class BriosaStartOptions:
    start_spatial_analyzer_sdk: bool = True
    launch_spatial_analyzer: bool = True
    connect_to_spatial_analyzer: bool = True
    launch_options: SpatialAnalyzerLaunchOptions = field(
        default_factory=SpatialAnalyzerLaunchOptions
    )
    startup_timeout: float = 30.0

    def __post_init__(self) -> None:
        if self.startup_timeout <= 0:
            raise ValueError("startup_timeout must be positive")
        if self.connect_to_spatial_analyzer and not self.start_spatial_analyzer_sdk:
            raise ValueError(
                "connect_to_spatial_analyzer requires start_spatial_analyzer_sdk"
            )
        if not self.launch_spatial_analyzer and not self.launch_options.is_default:
            raise ValueError(
                "launch_options must be default when launch_spatial_analyzer is false"
            )


@dataclass(frozen=True, slots=True, kw_only=True)
class OperationFailure:
    operation_id: str
    kind: OperationFailureKind
    diagnostic_code: str
    execution_disposition: ExecutionDisposition
    recovery_guidance: RecoveryGuidance
    replay_guidance: ReplayGuidance
    replay_safety: ReplaySafety


@dataclass(frozen=True, slots=True)
class SpatialAnalyzerLifecycleState:
    state_revision: int
    application_state: SpatialAnalyzerApplicationState
    ownership: SpatialAnalyzerOwnership
    application_generation: int | None
    diagnostic_code: str | None


@dataclass(frozen=True, slots=True)
class SpatialAnalyzerSdkIncident:
    sdk_generation: int
    termination_kind: SpatialAnalyzerSdkTerminationKind
    execution_disposition: ExecutionDisposition | None
    operation_id: str | None
    diagnostic_code: str | None


@dataclass(frozen=True, slots=True)
class SpatialAnalyzerSdkLifecycleState:
    state_revision: int
    sdk_state: SpatialAnalyzerSdkState
    sdk_generation: int | None
    application_generation: int | None
    connection_state: SpatialAnalyzerConnectionState
    execution_readiness_state: SpatialAnalyzerExecutionReadinessState
    ready_for_mp: bool
    recovery_state: SpatialAnalyzerSdkRecoveryState
    last_incident: SpatialAnalyzerSdkIncident | None
    diagnostic_code: str | None


@dataclass(frozen=True, slots=True)
class BriosaOperationCapability:
    operation_id: str
    grpc_service: str
    rpc: str
    fully_qualified_method: str


@dataclass(frozen=True, slots=True)
class BriosaServerSnapshot:
    briosa_version: str
    source_revision: str
    protocol_package: str
    spatial_analyzer_target: str
    ready_for_mp: bool
    operations: tuple[BriosaOperationCapability, ...]

    def supports(self, fully_qualified_method: str) -> bool:
        return any(
            operation.fully_qualified_method == fully_qualified_method
            for operation in self.operations
        )
