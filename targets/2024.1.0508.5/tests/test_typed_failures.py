"""Typed failure mapping for contract major 3 (#294, #313, #351, #305)."""

from __future__ import annotations

import asyncio
import re
from enum import Enum

import grpc
import pytest
from google.protobuf import descriptor_pool

from briosa import (
    BriosaOperationError,
    BriosaSpatialAnalyzerError,
    BriosaSpatialAnalyzerSdkError,
    BriosaTransportError,
    ExecutionDisposition,
    LifecycleRecoveryGuidance,
    MpExecutionDetails,
    MpExecutionState,
    OperationFailureKind,
    OutputRetrievalDetails,
    OutputRetrievalState,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    RpcStatusCode,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerConnectionState,
    SpatialAnalyzerExecutionReadinessState,
    SpatialAnalyzerLifecycleFailureKind,
    SpatialAnalyzerOwnership,
    SpatialAnalyzerSdkLifecycleFailureKind,
    SpatialAnalyzerSdkRecoveryState,
    SpatialAnalyzerSdkState,
    SpatialAnalyzerSdkTerminationKind,
    lifecycle_pb2,
    operation_outcomes_pb2,
)
from briosa.transport import map_rpc_error

OPERATION_TRAILER = "briosa-operation-error-bin"
SDK_TRAILER = "briosa-spatial-analyzer-sdk-lifecycle-error-bin"
APPLICATION_TRAILER = "briosa-spatial-analyzer-lifecycle-error-bin"

# Enums the client maps by wire number. Each public member list must mirror
# the wire enum exactly, so a value appended in a later revision lands on a
# new member instead of shifting or folding into a neighbour.
POSITIONAL_ENUMS: tuple[type[Enum], ...] = (
    ExecutionDisposition,
    LifecycleRecoveryGuidance,
    MpExecutionState,
    OperationFailureKind,
    OutputRetrievalState,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerConnectionState,
    SpatialAnalyzerExecutionReadinessState,
    SpatialAnalyzerLifecycleFailureKind,
    SpatialAnalyzerOwnership,
    SpatialAnalyzerSdkLifecycleFailureKind,
    SpatialAnalyzerSdkRecoveryState,
    SpatialAnalyzerSdkState,
    SpatialAnalyzerSdkTerminationKind,
)


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


def operation_error(
    status: grpc.StatusCode, detail: operation_outcomes_pb2.OperationError
) -> BriosaOperationError:
    mapped = map_rpc_error(
        FakeRpcError(status, ((OPERATION_TRAILER, detail.SerializeToString()),))
    )
    assert isinstance(mapped, BriosaOperationError)
    return mapped


def sdk_detail(
    kind: int, diagnostic_code: str, guidance: int
) -> lifecycle_pb2.SpatialAnalyzerSdkLifecycleError:
    return lifecycle_pb2.SpatialAnalyzerSdkLifecycleError(
        rpc="ConnectToSpatialAnalyzer",
        kind=kind,  # type: ignore[arg-type]
        diagnostic_code=diagnostic_code,
        recovery_guidance=guidance,  # type: ignore[arg-type]
        state=lifecycle_pb2.SpatialAnalyzerSdkLifecycleState(
            state_revision=4,
            sdk_state=lifecycle_pb2.SPATIAL_ANALYZER_SDK_STATE_VERIFYING,
            sdk_generation=2,
        ),
    )


@pytest.mark.parametrize(
    "public_enum", POSITIONAL_ENUMS, ids=lambda item: item.__name__
)
def test_public_enums_mirror_the_wire_enum_in_wire_order(
    public_enum: type[Enum],
) -> None:
    wire = descriptor_pool.Default().FindEnumTypeByName(  # type: ignore[no-untyped-call]
        f"briosa.{public_enum.__name__}"
    )
    prefix = re.sub(r"(?<!^)(?=[A-Z])", "_", public_enum.__name__).upper() + "_"
    values = sorted(wire.values, key=lambda value: value.number)
    assert [value.number for value in values] == list(range(len(values)))
    assert [member.name for member in public_enum] == [
        value.name.removeprefix(prefix) for value in values
    ]


def test_every_operation_failure_kind_maps_to_its_own_member() -> None:
    seen = set()
    for value in operation_outcomes_pb2.OperationFailureKind.DESCRIPTOR.values:
        if value.number == 0:
            continue
        mapped = operation_error(
            grpc.StatusCode.INTERNAL,
            operation_outcomes_pb2.OperationError(
                operation_id="file_operations.get_working_directory",
                kind=value.number,  # type: ignore[arg-type]
                diagnostic_code="diagnostic",
            ),
        )
        expected = value.name.removeprefix("OPERATION_FAILURE_KIND_")
        assert mapped.failure.kind.name == expected
        seen.add(mapped.failure.kind)
    assert OperationFailureKind.SDK_CALL_FAULTED in seen
    assert len(seen) == len(OperationFailureKind) - 1


@pytest.mark.parametrize(
    ("disposition", "replay", "state", "code"),
    [
        (
            operation_outcomes_pb2.EXECUTION_DISPOSITION_NOT_STARTED,
            operation_outcomes_pb2.REPLAY_GUIDANCE_DO_NOT_REPLAY,
            None,
            None,
        ),
        (
            operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN,
            operation_outcomes_pb2.REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY,
            operation_outcomes_pb2.MP_EXECUTION_STATE_RESULT_UNAVAILABLE,
            None,
        ),
        (
            operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED,
            operation_outcomes_pb2.REPLAY_GUIDANCE_DO_NOT_REPLAY,
            operation_outcomes_pb2.MP_EXECUTION_STATE_SUCCEEDED,
            2,
        ),
    ],
)
def test_sdk_call_fault_keeps_its_own_kind_and_reads_the_phase_from_disposition(
    disposition: int, replay: int, state: int | None, code: int | None
) -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.get_working_directory",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_SDK_CALL_FAULTED,
        diagnostic_code="sdk-execute-step-faulted",
        worker_generation=3,
        execution_disposition=disposition,  # type: ignore[arg-type]
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_NONE,
        replay_guidance=replay,  # type: ignore[arg-type]
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_SAFE,
    )
    if state is not None:
        detail.mp_execution.state = state  # type: ignore[assignment]
        if code is not None:
            detail.mp_execution.mp_result_code = code
        if disposition == operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED:
            detail.mp_execution.output_retrievals.add(
                field_name="directory",
                state=operation_outcomes_pb2.OUTPUT_RETRIEVAL_STATE_FAILED,
                diagnostic_code="sdk-output-getter-faulted",
            )
    failure = operation_error(grpc.StatusCode.INTERNAL, detail).failure

    assert failure.kind is OperationFailureKind.SDK_CALL_FAULTED
    assert failure.kind not in {
        OperationFailureKind.INTERNAL,
        OperationFailureKind.MP_RESULT_RETRIEVAL_FAILURE,
        OperationFailureKind.OUTPUT_RETRIEVAL_FAILURE,
    }
    assert failure.execution_disposition is ExecutionDisposition(
        operation_outcomes_pb2.ExecutionDisposition.Name(disposition)  # type: ignore[arg-type]
        .removeprefix("EXECUTION_DISPOSITION_")
        .lower()
    )
    assert failure.worker_generation == 3
    if state is None:
        assert failure.mp_execution is None
    elif disposition == operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED:
        assert failure.mp_execution == MpExecutionDetails(
            state=MpExecutionState.SUCCEEDED,
            mp_result_code=2,
            output_retrievals=(
                OutputRetrievalDetails(
                    field_name="directory",
                    state=OutputRetrievalState.FAILED,
                    diagnostic_code="sdk-output-getter-faulted",
                ),
            ),
        )
    else:
        assert failure.mp_execution == MpExecutionDetails(
            state=MpExecutionState.RESULT_UNAVAILABLE,
            mp_result_code=None,
            output_retrievals=(),
        )


def test_partial_success_stays_distinct_inside_a_typed_failure() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.get_working_directory",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_OUTPUT_RETRIEVAL_FAILURE,
        diagnostic_code="output-retrieval-failed",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_NONE,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_DO_NOT_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_SAFE,
        mp_execution=operation_outcomes_pb2.MpExecutionDetails(
            state=operation_outcomes_pb2.MP_EXECUTION_STATE_PARTIAL_SUCCESS,
            mp_result_code=4,
            output_retrievals=[
                operation_outcomes_pb2.OutputRetrievalDetails(
                    field_name="directory",
                    state=operation_outcomes_pb2.OUTPUT_RETRIEVAL_STATE_FAILED,
                )
            ],
        ),
    )
    error = operation_error(grpc.StatusCode.DATA_LOSS, detail)

    assert error.status_code is RpcStatusCode.DATA_LOSS
    assert error.failure.kind is OperationFailureKind.OUTPUT_RETRIEVAL_FAILURE
    assert error.failure.execution_disposition is ExecutionDisposition.COMPLETED
    assert error.failure.replay_guidance is ReplayGuidance.DO_NOT_REPLAY
    execution = error.failure.mp_execution
    assert execution is not None
    assert execution.state is MpExecutionState.PARTIAL_SUCCESS
    assert execution.state is not MpExecutionState.SUCCEEDED
    assert execution.mp_result_code == 4
    assert execution.output_retrievals == (
        OutputRetrievalDetails(
            field_name="directory",
            state=OutputRetrievalState.FAILED,
            diagnostic_code=None,
        ),
    )


def test_code_4_from_an_excepted_operation_stays_an_ordinary_mp_failure() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.open_sa_file",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_MP_FAILURE,
        diagnostic_code="mp-failed",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_NONE,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_DO_NOT_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_UNSAFE,
        mp_execution=operation_outcomes_pb2.MpExecutionDetails(
            state=operation_outcomes_pb2.MP_EXECUTION_STATE_FAILED,
            mp_result_code=4,
        ),
    )
    failure = operation_error(grpc.StatusCode.FAILED_PRECONDITION, detail).failure

    assert failure.kind is OperationFailureKind.MP_FAILURE
    assert failure.mp_execution == MpExecutionDetails(
        state=MpExecutionState.FAILED, mp_result_code=4, output_retrievals=()
    )


def test_unknown_mp_execution_state_is_a_malformed_detail() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.get_working_directory",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_MP_FAILURE,
        diagnostic_code="mp-failed",
        mp_execution=operation_outcomes_pb2.MpExecutionDetails(state=99),  # type: ignore[arg-type]
    )
    mapped = map_rpc_error(
        FakeRpcError(
            grpc.StatusCode.FAILED_PRECONDITION,
            ((OPERATION_TRAILER, detail.SerializeToString()),),
        )
    )
    assert isinstance(mapped, BriosaTransportError)
    assert mapped.diagnostic_code == "typed-error-malformed"


def test_modal_dialog_watchdog_failure_is_surfaced_as_is() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="reporting_operations.make_a_chart",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_WORKER_WATCHDOG_TIMEOUT,
        diagnostic_code="sa-modal-dialog-open",
        worker_generation=5,
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_OPERATOR_INTERVENTION_REQUIRED,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_UNSAFE,
    )
    error = operation_error(grpc.StatusCode.UNAVAILABLE, detail)

    assert error.failure.kind is OperationFailureKind.WORKER_WATCHDOG_TIMEOUT
    assert error.failure.diagnostic_code == "sa-modal-dialog-open"
    assert (
        error.failure.recovery_guidance
        is RecoveryGuidance.OPERATOR_INTERVENTION_REQUIRED
    )
    assert error.failure.recovery_guidance is not RecoveryGuidance.WORKER_REPLACEMENT
    assert error.reconciliation_required is True


def test_modal_dialog_readiness_failure_is_surfaced_as_is() -> None:
    detail = sdk_detail(
        lifecycle_pb2.SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_TIMEOUT,
        "sa-modal-dialog-open",
        lifecycle_pb2.LIFECYCLE_RECOVERY_GUIDANCE_OPERATOR_ACTION_REQUIRED,
    )
    mapped = map_rpc_error(
        FakeRpcError(
            grpc.StatusCode.DEADLINE_EXCEEDED,
            ((SDK_TRAILER, detail.SerializeToString()),),
        )
    )
    assert isinstance(mapped, BriosaSpatialAnalyzerSdkError)
    assert mapped.kind is SpatialAnalyzerSdkLifecycleFailureKind.TIMEOUT
    assert mapped.diagnostic_code == "sa-modal-dialog-open"
    assert (
        mapped.recovery_guidance is LifecycleRecoveryGuidance.OPERATOR_ACTION_REQUIRED
    )


@pytest.mark.parametrize(
    ("status", "wire_kind", "diagnostic_code", "guidance", "expected"),
    [
        (
            grpc.StatusCode.CANCELLED,
            lifecycle_pb2.SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_CALLER_CANCELLED,
            "sdk-lifecycle-request-withdrawn",
            lifecycle_pb2.LIFECYCLE_RECOVERY_GUIDANCE_NONE,
            SpatialAnalyzerSdkLifecycleFailureKind.CALLER_CANCELLED,
        ),
        (
            grpc.StatusCode.DEADLINE_EXCEEDED,
            lifecycle_pb2.SPATIAL_ANALYZER_SDK_LIFECYCLE_FAILURE_KIND_CALLER_DEADLINE_EXCEEDED,
            "sdk-lifecycle-caller-stopped-waiting",
            lifecycle_pb2.LIFECYCLE_RECOVERY_GUIDANCE_REFRESH_STATE,
            SpatialAnalyzerSdkLifecycleFailureKind.CALLER_DEADLINE_EXCEEDED,
        ),
    ],
)
def test_sdk_lifecycle_caller_kinds_are_distinct_from_a_state_conflict(
    status: grpc.StatusCode,
    wire_kind: int,
    diagnostic_code: str,
    guidance: int,
    expected: SpatialAnalyzerSdkLifecycleFailureKind,
) -> None:
    detail = sdk_detail(wire_kind, diagnostic_code, guidance)
    mapped = map_rpc_error(
        FakeRpcError(status, ((SDK_TRAILER, detail.SerializeToString()),))
    )

    assert isinstance(mapped, BriosaSpatialAnalyzerSdkError)
    assert mapped.kind is expected
    assert mapped.kind is not SpatialAnalyzerSdkLifecycleFailureKind.STATE_CONFLICT
    assert mapped.diagnostic_code == diagnostic_code
    assert mapped.state.sdk_generation == 2


@pytest.mark.parametrize(
    ("status", "wire_kind", "diagnostic_code", "expected"),
    [
        (
            grpc.StatusCode.CANCELLED,
            lifecycle_pb2.SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_CALLER_CANCELLED,
            "application-lifecycle-request-withdrawn",
            SpatialAnalyzerLifecycleFailureKind.CALLER_CANCELLED,
        ),
        (
            grpc.StatusCode.DEADLINE_EXCEEDED,
            lifecycle_pb2.SPATIAL_ANALYZER_LIFECYCLE_FAILURE_KIND_CALLER_DEADLINE_EXCEEDED,
            "application-lifecycle-caller-stopped-waiting",
            SpatialAnalyzerLifecycleFailureKind.CALLER_DEADLINE_EXCEEDED,
        ),
    ],
)
def test_application_lifecycle_caller_kinds_are_distinct_from_a_state_conflict(
    status: grpc.StatusCode,
    wire_kind: int,
    diagnostic_code: str,
    expected: SpatialAnalyzerLifecycleFailureKind,
) -> None:
    detail = lifecycle_pb2.SpatialAnalyzerLifecycleError(
        rpc="LaunchSpatialAnalyzer",
        kind=wire_kind,  # type: ignore[arg-type]
        diagnostic_code=diagnostic_code,
        recovery_guidance=lifecycle_pb2.LIFECYCLE_RECOVERY_GUIDANCE_REFRESH_STATE,
        state=lifecycle_pb2.SpatialAnalyzerLifecycleState(
            state_revision=2,
            application_state=lifecycle_pb2.SPATIAL_ANALYZER_APPLICATION_STATE_STARTING,
            ownership=lifecycle_pb2.SPATIAL_ANALYZER_OWNERSHIP_SERVER_LAUNCHED,
        ),
    )
    mapped = map_rpc_error(
        FakeRpcError(status, ((APPLICATION_TRAILER, detail.SerializeToString()),))
    )

    assert isinstance(mapped, BriosaSpatialAnalyzerError)
    assert mapped.kind is expected
    assert mapped.kind is not SpatialAnalyzerLifecycleFailureKind.STATE_CONFLICT
    assert mapped.diagnostic_code == diagnostic_code
    assert mapped.recovery_guidance is LifecycleRecoveryGuidance.REFRESH_STATE


def test_lifecycle_caller_interruption_without_detail_stays_language_native() -> None:
    cancelled = map_rpc_error(FakeRpcError(grpc.StatusCode.CANCELLED))
    assert isinstance(cancelled, asyncio.CancelledError)
    deadline = map_rpc_error(FakeRpcError(grpc.StatusCode.DEADLINE_EXCEEDED))
    assert isinstance(deadline, BriosaTransportError)
    assert deadline.status_code is RpcStatusCode.DEADLINE_EXCEEDED
    assert deadline.diagnostic_code == "transport-deadline-exceeded"
