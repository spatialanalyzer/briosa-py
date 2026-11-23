"""Handwritten public lifecycle and discovery types."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import timedelta
from enum import Enum
from pathlib import Path
from typing import cast

from briosa.installation_models import BriosaServerSelection
from briosa.logging_options import BriosaLoggingOptions


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
    OVERLOADED = "overloaded"
    SDK_CALL_FAULTED = "sdk_call_faulted"


class MpExecutionState(_StrEnum):
    """What happened to the MP command itself (MP execution details)."""

    UNSPECIFIED = "unspecified"
    SUCCEEDED = "succeeded"
    EXECUTE_STEP_REJECTED = "execute_step_rejected"
    FAILED = "failed"
    RESULT_UNAVAILABLE = "result_unavailable"
    ARGUMENT_REJECTED = "argument_rejected"
    PARTIAL_SUCCESS = "partial_success"


class OutputRetrievalState(_StrEnum):
    UNSPECIFIED = "unspecified"
    RETRIEVED = "retrieved"
    NOT_ATTEMPTED = "not_attempted"
    FAILED = "failed"


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
    CALLER_CANCELLED = "caller_cancelled"
    CALLER_DEADLINE_EXCEEDED = "caller_deadline_exceeded"


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
    CALLER_CANCELLED = "caller_cancelled"
    CALLER_DEADLINE_EXCEEDED = "caller_deadline_exceeded"


class LifecycleRecoveryGuidance(_StrEnum):
    UNSPECIFIED = "unspecified"
    NONE = "none"
    REFRESH_STATE = "refresh_state"
    RETRY_AFTER_STATE_CHANGE = "retry_after_state_change"
    CORRECT_ENVIRONMENT = "correct_environment"
    STOP_SDK_FIRST = "stop_sdk_first"
    RECOVER_SDK_WITHOUT_REPLAY = "recover_sdk_without_replay"
    OPERATOR_ACTION_REQUIRED = "operator_action_required"


class OperationRiskFlag(_StrEnum):
    """A reviewed risk on an operation's classification row (#242)."""

    UNSPECIFIED = "unspecified"
    FILESYSTEM_METADATA = "filesystem_metadata"
    FILESYSTEM_READ = "filesystem_read"
    FILESYSTEM_WRITE = "filesystem_write"
    FILESYSTEM_DELETE = "filesystem_delete"
    DESTRUCTIVE = "destructive"
    CODE_EXECUTION = "code_execution"
    PHYSICAL_MOTION = "physical_motion"
    DEVICE_SESSION = "device_session"
    DEVICE_CONFIG = "device_config"
    INTERACTIVE_UI = "interactive_ui"
    EXTERNAL_IO = "external_io"
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class OperationDurationClass(_StrEnum):
    """The reviewed duration class, which selects the server execution budget."""

    UNSPECIFIED = "unspecified"
    QUICK = "quick"
    LONG_RUNNING = "long_running"
    INTERACTIVE = "interactive"
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class OperationValidationStatus(_StrEnum):
    """The recorded validation gap. It is informational and never gates a call."""

    UNSPECIFIED = "unspecified"
    NO_RECORDED_GAP = "no_recorded_gap"
    FIXTURE_PENDING = "fixture_pending"
    AT_RISK_UNVALIDATED = "at_risk_unvalidated"
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class OperationAdmission(_StrEnum):
    """The active policy's decision for an operation, as the server reports it."""

    UNSPECIFIED = "unspecified"
    ADMITTED = "admitted"
    DENIED_PROFILE = "denied_profile"
    DENIED_FLAG = "denied_flag"
    DENIED_OVERRIDE = "denied_override"
    DENIED_EXCLUSIVE = "denied_exclusive"
    DENIED_UNREVIEWED = "denied_unreviewed"
    UNKNOWN = "unknown"
    """A value from a later compatible server release; it never admits the operation."""


class PolicyDenialRule(_StrEnum):
    """The policy step that denied a call, a capability, or a request option.

    Each rule names the same step as the denied ``OperationAdmission`` value of
    the same name, for example ``FLAG`` and ``DENIED_FLAG``.
    """

    UNSPECIFIED = "unspecified"
    PROFILE = "profile"
    """The admission profile, widened by flags set to allow, doesn't admit every
    risk flag, or the read-only profile excludes the operation."""
    FLAG = "flag"
    """A risk flag is set to deny."""
    OVERRIDE = "override"
    """A per-operation override is set to deny."""
    EXCLUSIVE = "exclusive"
    """An exclusive workflow, which no setting admits in the current isolation
    mode."""
    UNREVIEWED = "unreviewed"
    """The operation's classification is not reviewed, or the request couldn't be
    read against its reviewed request options."""
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize. It is metadata only and never admits anything."""


class OperationRequestOptionEffect(_StrEnum):
    """What a request option turns on."""

    UNSPECIFIED = "unspecified"
    INTERACTIVE_UI = "interactive_ui"
    """The request opens or blocks on operator UI."""
    BACKGROUND_WORK = "background_work"
    """The call returns while device or operator work keeps running."""
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class OperationRequestOptionCondition(_StrEnum):
    """Which values of a request option's field turn its effect on."""

    UNSPECIFIED = "unspecified"
    WHEN_TRUE = "when_true"
    """A Boolean field set to true."""
    WHEN_FALSE = "when_false"
    """A Boolean field set to false."""
    WHEN_PRESENT = "when_present"
    """A message field that is present."""
    WHEN_NON_EMPTY = "when_non_empty"
    """A string field that is present and not empty."""
    WHEN_ONE_OF = "when_one_of"
    """An enum field set to one of ``enabling_enum_values``, or to a number the
    server doesn't recognize."""
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class OperationRequestOptionOmission(_StrEnum):
    """What omitting a request option's field does."""

    UNSPECIFIED = "unspecified"
    DOES_NOT_ACTIVATE = "does_not_activate"
    """Omitting the field doesn't turn the effect on."""
    ACTIVATES = "activates"
    """Omitting the field turns the effect on."""
    REQUIRED = "required"
    """The server's request mapping requires the field: omitting it fails
    validation before the call reaches SpatialAnalyzer."""
    UNKNOWN = "unknown"
    """A value from a later compatible server release that this client doesn't
    recognize."""


class ConfiguredSpatialAnalyzerInteractionMode(_StrEnum):
    """The SpatialAnalyzer interaction mode the server is configured to set.

    This is the server's configuration (``Briosa:SpatialAnalyzer:InteractionMode``),
    which it applies after each verified Connect. It is never SpatialAnalyzer's
    live mode: SpatialAnalyzer has no getter for it, and an operator or a
    ``set_interaction_mode`` call can change it at any time.
    """

    UNKNOWN = "unknown"
    """Not reported, as with Server 0.10.0, or a value from a later compatible
    server release that this client doesn't recognize."""
    UNCHANGED = "unchanged"
    """The server never sets the mode and leaves SpatialAnalyzer's mode as it is."""
    SILENT = "silent"
    AUTOMATIC = "automatic"
    MANUAL = "manual"


class GracefulShutdownBoundKind(_StrEnum):
    """Whether the server host's graceful shutdown wait is known, and how."""

    UNAVAILABLE = "unavailable"
    """The server reported no usable bound. This never means unbounded."""
    FINITE = "finite"
    UNBOUNDED = "unbounded"
    """The server host is configured with no graceful shutdown time limit."""


@dataclass(frozen=True, slots=True, kw_only=True)
class GracefulShutdownBound:
    """The server host's graceful shutdown wait.

    ``duration`` is present exactly when ``kind`` is ``FINITE``. The bound is the
    most a graceful stop of the server host may wait before it cancels the
    remaining shutdown work; it doesn't promise that any process exits.
    """

    kind: GracefulShutdownBoundKind = GracefulShutdownBoundKind.UNAVAILABLE
    duration: timedelta | None = None

    def __post_init__(self) -> None:
        if (self.kind is GracefulShutdownBoundKind.FINITE) != (
            self.duration is not None
        ):
            raise ValueError("duration must be present exactly when kind is FINITE")
        if self.duration is not None and self.duration <= timedelta(0):
            raise ValueError("duration must be positive")


@dataclass(frozen=True, slots=True, kw_only=True)
class BriosaLifecycleBounds:
    """The lifecycle wait allowances the server computes from its own settings.

    Server 0.10.1 and later publish them; ``BriosaServerSnapshot.lifecycle_bounds``
    is ``None`` against Server 0.10.0. Each allowance is ``None`` when the server
    reported it absent or zero, which means unavailable, never unbounded. Each
    covers only the server's own work for that request, without transport time;
    none promises that a response arrives or a process exits within it.
    ``startup_with_launch`` and ``startup_without_launch`` size a startup of
    several requests and are not server deadlines; the client sizes its default
    startup budget from them.
    """

    start_sdk: timedelta | None = None
    launch_spatial_analyzer: timedelta | None = None
    connect_spatial_analyzer: timedelta | None = None
    recover_sdk: timedelta | None = None
    stop_sdk: timedelta | None = None
    close_owned_spatial_analyzer: timedelta | None = None
    startup_with_launch: timedelta | None = None
    startup_without_launch: timedelta | None = None
    host_graceful_shutdown: GracefulShutdownBound = field(
        default_factory=GracefulShutdownBound
    )


@dataclass(frozen=True, slots=True, kw_only=True)
class PolicyDenialDetails:
    """Which policy step denied a call, a capability, or a request option.

    Server 0.10.1 and later send it; against Server 0.10.0 it is absent.
    ``denied_flag`` is present for a ``FLAG`` denial and is
    ``OperationRiskFlag.UNKNOWN`` for a flag this client doesn't know.
    ``admission_profile`` is present for a ``PROFILE`` denial.
    ``request_option_field`` is the protobuf field name of the request option the
    server attributed the denial to, never a request value. The client reports
    the detail as the server sent it: it never changes the failure or the
    capability's admission, and the client never pre-validates a request from it.
    """

    rule: PolicyDenialRule
    denied_flag: OperationRiskFlag | None = None
    admission_profile: str | None = None
    request_option_field: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class OperationRequestOption:
    """One reviewed request option that opens operator UI or leaves work running.

    ``field_name`` is the protobuf field name in the operation's request, and
    ``enabling_enum_values`` holds protobuf enum value names for ``WHEN_ONE_OF``.
    ``admission`` and ``policy_denial`` answer one question: what the active
    policy decides for a request that turns on this option alone. The server
    still decides every actual request, so the client never pre-validates a
    request from this description.
    """

    field_name: str
    effect: OperationRequestOptionEffect
    condition: OperationRequestOptionCondition
    enabling_enum_values: tuple[str, ...] = ()
    omission: OperationRequestOptionOmission
    admission: OperationAdmission
    policy_denial: PolicyDenialDetails | None = None


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


class _DefaultStartupTimeout(float):
    """The omitted ``startup_timeout``: 120 seconds that may adopt the server's
    published startup allowance. An explicit number, even 120, never does."""

    __slots__ = ()


_DEFAULT_STARTUP_TIMEOUT: float = _DefaultStartupTimeout(120.0)


def _startup_timeout_omitted(options: BriosaStartOptions) -> bool:
    """Whether ``options`` left ``startup_timeout`` at its default."""
    return type(options.startup_timeout) is _DefaultStartupTimeout


@dataclass(frozen=True, slots=True)
class BriosaStartOptions:
    """Selects the phases of one client-owned server startup.

    ``startup_timeout`` is one overall budget, in seconds, for the whole
    ``start()``, whichever phases are selected. Expiry raises
    ``BriosaStartupError`` with ``startup-timeout``. Omitted, it is two minutes,
    which covers the server's default worst case of 100 seconds (SDK start 10 s,
    SpatialAnalyzer launch 30 s, Connect with readiness probe and application
    association 60 s) plus 20 seconds for server host startup, process
    observation, and round trips. With Server 0.10.1 and later, an omitted budget
    follows the server's own settings: once the client has verified the server,
    the budget becomes the server's published startup allowance for the selected
    phases plus 20 seconds, counted from the start of ``start()``, and never less
    than two minutes. Against Server 0.10.0, which publishes no allowance, it stays
    at two minutes, so raise it when you raise that server's lifecycle bounds. An
    explicit value, including ``120.0``, is always used as given.

    Expiry during an in-flight RPC is reported the same way; cancelling the
    caller's task only stops that caller from waiting. The server finishes an SDK
    start or connection it has accepted after the client stops waiting
    (spatialanalyzer/briosa#315), so refresh SDK state before retrying.
    """

    server_selection: BriosaServerSelection = field(
        default_factory=BriosaServerSelection
    )
    start_spatial_analyzer_sdk: bool = True
    launch_spatial_analyzer: bool = True
    connect_to_spatial_analyzer: bool = True
    launch_options: SpatialAnalyzerLaunchOptions = field(
        default_factory=SpatialAnalyzerLaunchOptions
    )
    startup_timeout: float = _DEFAULT_STARTUP_TIMEOUT
    logging: BriosaLoggingOptions | None = None

    def __post_init__(self) -> None:
        if self.logging is not None:
            self.logging.to_arguments()
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
class OutputRetrievalDetails:
    """Retrieval of one result field, named by its public result field name."""

    field_name: str
    state: OutputRetrievalState
    diagnostic_code: str | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class MpExecutionDetails:
    """What the server proved about the MP command inside a typed failure.

    ``state`` keeps ``PARTIAL_SUCCESS`` (MP code 4) distinct from
    ``SUCCEEDED``. ``mp_result_code`` is the raw MP code when SpatialAnalyzer
    returned one.
    """

    state: MpExecutionState
    mp_result_code: int | None = None
    output_retrievals: tuple[OutputRetrievalDetails, ...] = ()


@dataclass(frozen=True, slots=True, kw_only=True)
class MpCompletion:
    """How one successful MP call completed.

    ``state`` is ``SUCCEEDED`` with ``mp_result_code`` 2, or ``PARTIAL_SUCCESS``
    with code 4. A partial success did its work, but did not have its full
    intended effect. It is still a success, so the call returns its outputs when
    all of them are retrieved, and never retries. If an output can't be
    retrieved, the call raises ``BriosaOperationError`` instead and reports no
    completion. The client checks the state and code of every MP success,
    observed or not: a success without valid execution details is
    ``BriosaProtocolError`` (``mp-completion-invalid``).
    """

    state: MpExecutionState
    mp_result_code: int


MpCompletionObserver = Callable[[MpCompletion], object]
"""A per-call callback that receives the call's ``MpCompletion``.

The client calls it once, after checking the completion and before mapping the
outputs, so it hears of a success even when the outputs then fail to map.
"""


@dataclass(frozen=True, slots=True, kw_only=True)
class OperationFailure:
    """A typed operation failure as the server reported it.

    ``policy_denial`` is the denial detail of a ``POLICY_DENIED`` failure, sent
    by Server 0.10.1 and later. It is ``None`` against Server 0.10.0 and never
    changes the other fields.
    """

    operation_id: str
    kind: OperationFailureKind
    diagnostic_code: str
    execution_disposition: ExecutionDisposition
    recovery_guidance: RecoveryGuidance
    replay_guidance: ReplayGuidance
    replay_safety: ReplaySafety
    mp_execution: MpExecutionDetails | None = None
    worker_generation: int | None = None
    policy_denial: PolicyDenialDetails | None = None


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
    """One operation's reviewed classification row and its admission.

    ``risk_flags`` is an ordered set; empty means no reviewed risk applies. A
    request option can still open operator UI or leave work running, and the
    server can deny that request; the client doesn't pre-validate it.

    With Server 0.10.1 and later, ``policy_denial`` says which policy step denied
    a denied operation, and ``request_options`` describes the operation's
    reviewed request options; an empty tuple means none apply. Against Server
    0.10.0 both are ``None``: the server doesn't describe them. Neither changes
    ``admission``.
    """

    operation_id: str
    grpc_service: str
    rpc: str
    fully_qualified_method: str
    risk_flags: tuple[OperationRiskFlag, ...] = ()
    duration_class: OperationDurationClass = OperationDurationClass.UNSPECIFIED
    validation_status: OperationValidationStatus = OperationValidationStatus.UNSPECIFIED
    admission: OperationAdmission = OperationAdmission.UNSPECIFIED
    policy_denial: PolicyDenialDetails | None = None
    request_options: tuple[OperationRequestOption, ...] | None = None


@dataclass(frozen=True, slots=True)
class BriosaServerSnapshot:
    """The verified server identity and the generation's admitted operations.

    ``operations`` holds only capabilities the server admitted.
    ``policy_fingerprint`` is opaque: compare it only for equality, for example
    to tell whether a replacement generation runs under the same policy.

    ``lifecycle_bounds`` holds the server's published lifecycle wait allowances,
    and ``configured_interaction_mode`` the SpatialAnalyzer interaction mode the
    server is configured to set after each Connect, never SpatialAnalyzer's live
    mode. Server 0.10.1 and later report both; against Server 0.10.0
    ``lifecycle_bounds`` is ``None`` and the mode is ``UNKNOWN``.
    """

    briosa_version: str
    source_revision: str
    protocol_package: str
    spatial_analyzer_target: str
    ready_for_mp: bool
    operations: tuple[BriosaOperationCapability, ...]
    admission_profile: str
    policy_fingerprint: str
    lifecycle_bounds: BriosaLifecycleBounds | None = None
    configured_interaction_mode: ConfiguredSpatialAnalyzerInteractionMode = (
        ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN
    )

    def supports(self, fully_qualified_method: str) -> bool:
        return any(
            operation.fully_qualified_method == fully_qualified_method
            and operation.admission is OperationAdmission.ADMITTED
            for operation in self.operations
        )


@dataclass(frozen=True, slots=True, kw_only=True)
class BriosaCapabilityListing:
    """A diagnostic capability listing, optionally with denied operations.

    Denied entries carry their denial reason in ``admission``, and with Server
    0.10.1 and later the denial detail in ``policy_denial``. They never enter the
    generation's admitted set and never make an operation callable.
    """

    admission_profile: str
    policy_fingerprint: str
    operations: tuple[BriosaOperationCapability, ...]

    @property
    def admitted(self) -> tuple[BriosaOperationCapability, ...]:
        return tuple(
            item
            for item in self.operations
            if item.admission is OperationAdmission.ADMITTED
        )

    @property
    def denied(self) -> tuple[BriosaOperationCapability, ...]:
        return tuple(
            item
            for item in self.operations
            if item.admission is not OperationAdmission.ADMITTED
        )
