"""Typed policy denial detail and request options (spatialanalyzer/briosa#397).

Server 0.10.1 and later send them; Server 0.10.0 sends neither. When the
enclosing message decodes, the detail never changes the typed failure or a
capability's admission, and unknown values are unknown metadata, never
permission.
"""

from __future__ import annotations

import re
from dataclasses import replace
from enum import Enum

import grpc
import pytest
from facade_support import RecordingTransport, started_client
from google.protobuf import descriptor_pool
from test_typed_failures import OPERATION_TRAILER, FakeRpcError, operation_error

from briosa import (
    BriosaOperationCapability,
    BriosaTransportError,
    ExecutionDisposition,
    OperationAdmission,
    OperationFailure,
    OperationFailureKind,
    OperationRequestOption,
    OperationRequestOptionCondition,
    OperationRequestOptionEffect,
    OperationRequestOptionOmission,
    OperationRiskFlag,
    PolicyDenialDetails,
    PolicyDenialRule,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    RpcStatusCode,
    discovery_pb2,
    operation_outcomes_pb2,
)
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET
from briosa.transport import map_capability_listing, map_rpc_error, risk_flag_from_name

FINGERPRINT = "sha256:" + "cd" * 32
OPEN_ENUMS: tuple[type[Enum], ...] = (
    PolicyDenialRule,
    OperationRequestOptionEffect,
    OperationRequestOptionCondition,
    OperationRequestOptionOmission,
)


def denied_call(
    detail: operation_outcomes_pb2.PolicyDenialDetails | None = None,
    *,
    kind: int = operation_outcomes_pb2.OPERATION_FAILURE_KIND_POLICY_DENIED,
) -> operation_outcomes_pb2.OperationError:
    error = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.get_working_directory",
        kind=kind,  # type: ignore[arg-type]
        diagnostic_code="policy-denied",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_NOT_STARTED,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_NONE,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_DO_NOT_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_SAFE,
        worker_generation=3,
    )
    if detail is not None:
        error.policy_denial.CopyFrom(detail)
    return error


def detail(
    rule: int,
    *,
    denied_flag: str | None = None,
    admission_profile: str | None = None,
    request_option_field: str | None = None,
) -> operation_outcomes_pb2.PolicyDenialDetails:
    value = operation_outcomes_pb2.PolicyDenialDetails(rule=rule)  # type: ignore[arg-type]
    if denied_flag is not None:
        value.denied_flag = denied_flag
    if admission_profile is not None:
        value.admission_profile = admission_profile
    if request_option_field is not None:
        value.request_option_field = request_option_field
    return value


@pytest.mark.parametrize("public_enum", OPEN_ENUMS, ids=lambda item: item.__name__)
def test_denial_and_option_enums_mirror_the_wire_enum_and_add_unknown(
    public_enum: type[Enum],
) -> None:
    wire = descriptor_pool.Default().FindEnumTypeByName(  # type: ignore[no-untyped-call]
        f"briosa.{public_enum.__name__}"
    )
    prefix = re.sub(r"(?<!^)(?=[A-Z])", "_", public_enum.__name__).upper() + "_"
    values = sorted(wire.values, key=lambda value: value.number)
    assert [member.name for member in public_enum] == [
        *(value.name.removeprefix(prefix) for value in values),
        "UNKNOWN",
    ]


def test_every_canonical_flag_name_maps_to_its_risk_flag() -> None:
    wire = descriptor_pool.Default().FindEnumTypeByName(  # type: ignore[no-untyped-call]
        "briosa.OperationRiskFlag"
    )
    names = [
        value.name.removeprefix("OPERATION_RISK_FLAG_").lower()
        for value in wire.values
        if value.number != 0
    ]
    assert len(names) == 11
    for name in names:
        flag = risk_flag_from_name(name)
        assert flag.name.lower() == name
        assert flag not in {OperationRiskFlag.UNSPECIFIED, OperationRiskFlag.UNKNOWN}


@pytest.mark.parametrize(
    "name",
    ["unspecified", "unknown", "", "Physical_Motion", "PHYSICAL_MOTION", "future_x"],
)
def test_a_flag_name_the_client_does_not_know_is_unknown(name: str) -> None:
    assert risk_flag_from_name(name) is OperationRiskFlag.UNKNOWN


def test_server_0_10_0_failure_has_no_denial_detail() -> None:
    mapped = operation_error(grpc.StatusCode.PERMISSION_DENIED, denied_call())
    assert mapped.status_code is RpcStatusCode.PERMISSION_DENIED
    assert mapped.failure.kind is OperationFailureKind.POLICY_DENIED
    assert mapped.failure.policy_denial is None


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        (
            detail(
                operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG,
                denied_flag="physical_motion",
            ),
            PolicyDenialDetails(
                rule=PolicyDenialRule.FLAG,
                denied_flag=OperationRiskFlag.PHYSICAL_MOTION,
            ),
        ),
        (
            detail(
                operation_outcomes_pb2.POLICY_DENIAL_RULE_PROFILE,
                admission_profile="standard",
                request_option_field="show_results_dialog",
            ),
            PolicyDenialDetails(
                rule=PolicyDenialRule.PROFILE,
                admission_profile="standard",
                request_option_field="show_results_dialog",
            ),
        ),
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_OVERRIDE),
            PolicyDenialDetails(rule=PolicyDenialRule.OVERRIDE),
        ),
        (
            detail(
                operation_outcomes_pb2.POLICY_DENIAL_RULE_EXCLUSIVE,
                request_option_field="acknowledge_arrival",
            ),
            PolicyDenialDetails(
                rule=PolicyDenialRule.EXCLUSIVE,
                request_option_field="acknowledge_arrival",
            ),
        ),
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_UNREVIEWED),
            PolicyDenialDetails(rule=PolicyDenialRule.UNREVIEWED),
        ),
    ],
    ids=["flag", "profile", "override", "exclusive", "unreviewed"],
)
def test_a_denied_call_exposes_its_typed_detail_and_nothing_else_changes(
    wire: operation_outcomes_pb2.PolicyDenialDetails, expected: PolicyDenialDetails
) -> None:
    without = operation_error(grpc.StatusCode.PERMISSION_DENIED, denied_call())
    mapped = operation_error(grpc.StatusCode.PERMISSION_DENIED, denied_call(wire))

    assert mapped.failure.policy_denial == expected
    assert mapped.status_code is without.status_code
    assert mapped.failure == _with_detail(without.failure, expected)
    assert mapped.failure.execution_disposition is ExecutionDisposition.NOT_STARTED
    assert mapped.failure.recovery_guidance is RecoveryGuidance.NONE
    assert mapped.failure.replay_guidance is ReplayGuidance.DO_NOT_REPLAY
    assert mapped.failure.replay_safety is ReplaySafety.SAFE
    assert mapped.failure.worker_generation == 3


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        # A rule from a later release is unknown metadata.
        (detail(99), PolicyDenialDetails(rule=PolicyDenialRule.UNKNOWN)),
        # A flag a later release adds is UNKNOWN, never another flag.
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG, denied_flag="radio"),
            PolicyDenialDetails(
                rule=PolicyDenialRule.FLAG, denied_flag=OperationRiskFlag.UNKNOWN
            ),
        ),
        # Inconsistent detail is reported as sent, never repaired.
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG),
            PolicyDenialDetails(rule=PolicyDenialRule.FLAG),
        ),
        (
            detail(
                operation_outcomes_pb2.POLICY_DENIAL_RULE_PROFILE,
                denied_flag="destructive",
            ),
            PolicyDenialDetails(
                rule=PolicyDenialRule.PROFILE,
                denied_flag=OperationRiskFlag.DESTRUCTIVE,
            ),
        ),
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_UNSPECIFIED),
            PolicyDenialDetails(rule=PolicyDenialRule.UNSPECIFIED),
        ),
        (
            detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG, denied_flag=""),
            PolicyDenialDetails(
                rule=PolicyDenialRule.FLAG, denied_flag=OperationRiskFlag.UNKNOWN
            ),
        ),
    ],
    ids=[
        "unknown-rule",
        "unknown-flag",
        "flag-without-flag",
        "profile-with-flag",
        "unspecified",
        "empty-flag",
    ],
)
def test_unknown_or_inconsistent_detail_never_changes_the_failure(
    wire: operation_outcomes_pb2.PolicyDenialDetails, expected: PolicyDenialDetails
) -> None:
    without = operation_error(grpc.StatusCode.PERMISSION_DENIED, denied_call())
    mapped = operation_error(grpc.StatusCode.PERMISSION_DENIED, denied_call(wire))
    assert mapped.failure == _with_detail(without.failure, expected)


@pytest.mark.parametrize(
    "kind",
    [
        value.number
        for value in operation_outcomes_pb2.OperationFailureKind.DESCRIPTOR.values
        if value.name != "OPERATION_FAILURE_KIND_POLICY_DENIED"
    ],
)
def test_denial_detail_appears_only_on_a_policy_denial(kind: int) -> None:
    # A validation or any other failure never appears to name a policy step,
    # and its kind and status are unchanged by the detail it carried.
    wire = detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_OVERRIDE)
    without = operation_error(
        grpc.StatusCode.FAILED_PRECONDITION, denied_call(kind=kind)
    )
    mapped = operation_error(
        grpc.StatusCode.FAILED_PRECONDITION, denied_call(wire, kind=kind)
    )
    assert mapped.failure.policy_denial is None
    assert mapped.failure.kind is without.failure.kind
    assert mapped.failure.kind is not OperationFailureKind.POLICY_DENIED
    assert mapped.status_code is RpcStatusCode.FAILED_PRECONDITION
    assert mapped.failure == without.failure


def test_an_undecodable_detail_keeps_the_existing_malformed_handling() -> None:
    # Field 11, a PolicyDenialDetails whose denied_flag (field 2) is not UTF-8:
    # the enclosing OperationError cannot be decoded at all.
    payload = denied_call().SerializeToString() + bytes([0x5A, 3, 0x12, 1, 0xFF])
    mapped = map_rpc_error(
        FakeRpcError(grpc.StatusCode.PERMISSION_DENIED, ((OPERATION_TRAILER, payload),))
    )
    assert isinstance(mapped, BriosaTransportError)
    assert mapped.diagnostic_code == "typed-error-malformed"
    assert mapped.status_code is RpcStatusCode.PERMISSION_DENIED


def option(
    field_name: str = "show_results_dialog",
    *,
    effect: int = discovery_pb2.OPERATION_REQUEST_OPTION_EFFECT_INTERACTIVE_UI,
    condition: int = discovery_pb2.OPERATION_REQUEST_OPTION_CONDITION_WHEN_TRUE,
    enabling: tuple[str, ...] = (),
    omission: int = discovery_pb2.OPERATION_REQUEST_OPTION_OMISSION_DOES_NOT_ACTIVATE,
    admission: int = discovery_pb2.OPERATION_ADMISSION_ADMITTED,
    denial: operation_outcomes_pb2.PolicyDenialDetails | None = None,
) -> discovery_pb2.OperationRequestOption:
    value = discovery_pb2.OperationRequestOption(
        field_name=field_name,
        effect=effect,  # type: ignore[arg-type]
        condition=condition,  # type: ignore[arg-type]
        enabling_enum_values=enabling,
        omission=omission,  # type: ignore[arg-type]
        admission=admission,  # type: ignore[arg-type]
    )
    if denial is not None:
        value.policy_denial.CopyFrom(denial)
    return value


def capability(
    *,
    admission: int = discovery_pb2.OPERATION_ADMISSION_ADMITTED,
    denial: operation_outcomes_pb2.PolicyDenialDetails | None = None,
    options: tuple[discovery_pb2.OperationRequestOption, ...] | None = None,
) -> discovery_pb2.OperationCapability:
    value = discovery_pb2.OperationCapability(
        operation_id="file_operations.get_working_directory",
        grpc_service="briosa.FileOperations",
        rpc="GetWorkingDirectory",
        fully_qualified_method="/briosa.FileOperations/GetWorkingDirectory",
        duration_class=discovery_pb2.OPERATION_DURATION_CLASS_QUICK,
        validation_status=discovery_pb2.OPERATION_VALIDATION_STATUS_NO_RECORDED_GAP,
        admission=admission,  # type: ignore[arg-type]
    )
    if denial is not None:
        value.policy_denial.CopyFrom(denial)
    if options is not None:
        value.request_options.SetInParent()
        value.request_options.options.extend(options)
    return value


def mapped_capability(
    item: discovery_pb2.OperationCapability,
) -> BriosaOperationCapability:
    listing = map_capability_listing(
        discovery_pb2.ListCapabilitiesResponse(
            protocol_package="briosa",
            spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
            operations=[item],
            admission_profile="standard",
            policy_fingerprint=FINGERPRINT,
        )
    )
    (mapped,) = listing.operations
    return mapped


def test_server_0_10_0_does_not_describe_request_options_or_denials() -> None:
    mapped = mapped_capability(capability())
    assert mapped.request_options is None
    assert mapped.policy_denial is None
    assert mapped.admission is OperationAdmission.ADMITTED


def test_present_and_empty_request_options_mean_none_apply() -> None:
    mapped = mapped_capability(capability(options=()))
    assert mapped.request_options == ()
    assert mapped.request_options is not None


def test_each_request_option_is_described_with_its_single_option_admission() -> None:
    mapped = mapped_capability(
        capability(
            options=(
                option(),
                option(
                    "auto_measure_mode",
                    effect=discovery_pb2.OPERATION_REQUEST_OPTION_EFFECT_BACKGROUND_WORK,
                    condition=discovery_pb2.OPERATION_REQUEST_OPTION_CONDITION_WHEN_ONE_OF,
                    enabling=(
                        "AUTO_MEASURE_MODE_CONTINUOUS",
                        "AUTO_MEASURE_MODE_TIMED",
                    ),
                    omission=discovery_pb2.OPERATION_REQUEST_OPTION_OMISSION_ACTIVATES,
                    admission=discovery_pb2.OPERATION_ADMISSION_DENIED_EXCLUSIVE,
                    denial=detail(
                        operation_outcomes_pb2.POLICY_DENIAL_RULE_EXCLUSIVE,
                        request_option_field="auto_measure_mode",
                    ),
                ),
                option(
                    "display_view_control",
                    condition=discovery_pb2.OPERATION_REQUEST_OPTION_CONDITION_WHEN_PRESENT,
                    omission=discovery_pb2.OPERATION_REQUEST_OPTION_OMISSION_REQUIRED,
                    admission=discovery_pb2.OPERATION_ADMISSION_DENIED_FLAG,
                    denial=detail(
                        operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG,
                        denied_flag="interactive_ui",
                        request_option_field="display_view_control",
                    ),
                ),
            )
        )
    )
    assert mapped.request_options == (
        OperationRequestOption(
            field_name="show_results_dialog",
            effect=OperationRequestOptionEffect.INTERACTIVE_UI,
            condition=OperationRequestOptionCondition.WHEN_TRUE,
            omission=OperationRequestOptionOmission.DOES_NOT_ACTIVATE,
            admission=OperationAdmission.ADMITTED,
        ),
        OperationRequestOption(
            field_name="auto_measure_mode",
            effect=OperationRequestOptionEffect.BACKGROUND_WORK,
            condition=OperationRequestOptionCondition.WHEN_ONE_OF,
            enabling_enum_values=(
                "AUTO_MEASURE_MODE_CONTINUOUS",
                "AUTO_MEASURE_MODE_TIMED",
            ),
            omission=OperationRequestOptionOmission.ACTIVATES,
            admission=OperationAdmission.DENIED_EXCLUSIVE,
            policy_denial=PolicyDenialDetails(
                rule=PolicyDenialRule.EXCLUSIVE,
                request_option_field="auto_measure_mode",
            ),
        ),
        OperationRequestOption(
            field_name="display_view_control",
            effect=OperationRequestOptionEffect.INTERACTIVE_UI,
            condition=OperationRequestOptionCondition.WHEN_PRESENT,
            omission=OperationRequestOptionOmission.REQUIRED,
            admission=OperationAdmission.DENIED_FLAG,
            policy_denial=PolicyDenialDetails(
                rule=PolicyDenialRule.FLAG,
                denied_flag=OperationRiskFlag.INTERACTIVE_UI,
                request_option_field="display_view_control",
            ),
        ),
    )
    # A denied option never changes the operation's own admission.
    assert mapped.admission is OperationAdmission.ADMITTED


def test_unknown_option_values_are_unknown_metadata_and_never_permission() -> None:
    mapped = mapped_capability(
        capability(
            options=(
                option(effect=99, condition=98, omission=97, admission=96),
                option(
                    effect=discovery_pb2.OPERATION_REQUEST_OPTION_EFFECT_UNSPECIFIED,
                    condition=discovery_pb2.OPERATION_REQUEST_OPTION_CONDITION_UNSPECIFIED,
                    omission=discovery_pb2.OPERATION_REQUEST_OPTION_OMISSION_UNSPECIFIED,
                    admission=discovery_pb2.OPERATION_ADMISSION_UNSPECIFIED,
                ),
            )
        )
    )
    assert mapped.request_options is not None
    unknown, unspecified = mapped.request_options
    assert unknown.effect is OperationRequestOptionEffect.UNKNOWN
    assert unknown.condition is OperationRequestOptionCondition.UNKNOWN
    assert unknown.omission is OperationRequestOptionOmission.UNKNOWN
    assert unknown.admission is OperationAdmission.UNKNOWN
    assert unspecified.effect is OperationRequestOptionEffect.UNSPECIFIED
    assert unspecified.condition is OperationRequestOptionCondition.UNSPECIFIED
    assert unspecified.omission is OperationRequestOptionOmission.UNSPECIFIED
    assert unspecified.admission is OperationAdmission.UNSPECIFIED


def test_a_denied_capability_exposes_its_detail() -> None:
    mapped = mapped_capability(
        capability(
            admission=discovery_pb2.OPERATION_ADMISSION_DENIED_OVERRIDE,
            denial=detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_OVERRIDE),
            options=(),
        )
    )
    assert mapped.admission is OperationAdmission.DENIED_OVERRIDE
    assert mapped.policy_denial == PolicyDenialDetails(rule=PolicyDenialRule.OVERRIDE)


@pytest.mark.parametrize(
    "wire",
    [
        detail(99, denied_flag="radio"),
        detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG),
        detail(operation_outcomes_pb2.POLICY_DENIAL_RULE_OVERRIDE),
    ],
    ids=["unknown", "inconsistent", "on-admitted"],
)
def test_denial_detail_never_changes_admission(
    wire: operation_outcomes_pb2.PolicyDenialDetails,
) -> None:
    admitted = mapped_capability(capability(denial=wire))
    assert admitted.admission is OperationAdmission.ADMITTED
    assert admitted.policy_denial is not None
    denied = mapped_capability(
        capability(admission=discovery_pb2.OPERATION_ADMISSION_DENIED_FLAG, denial=wire)
    )
    assert denied.admission is OperationAdmission.DENIED_FLAG


async def test_the_diagnostic_listing_returns_the_detail_of_each_denied_operation() -> (
    None
):
    transport = RecordingTransport()
    denied = capability(
        admission=discovery_pb2.OPERATION_ADMISSION_DENIED_FLAG,
        denial=detail(
            operation_outcomes_pb2.POLICY_DENIAL_RULE_FLAG,
            denied_flag="filesystem_delete",
        ),
        options=(),
    )
    denied.operation_id = "file_operations.delete_files"
    denied.rpc = "DeleteFiles"
    denied.fully_qualified_method = "/briosa.FileOperations/DeleteFiles"
    transport.capabilities = [capability(options=(option(),))]
    transport.denied_capabilities = [denied]
    client = await started_client(transport)

    listing = await client.list_capabilities(include_denied=True)
    snapshot = await client.get_server_snapshot()

    (denied_item,) = listing.denied
    assert denied_item.policy_denial == PolicyDenialDetails(
        rule=PolicyDenialRule.FLAG, denied_flag=OperationRiskFlag.FILESYSTEM_DELETE
    )
    assert denied_item.request_options == ()
    (admitted_item,) = snapshot.operations
    assert admitted_item.request_options is not None
    assert [item.field_name for item in admitted_item.request_options] == [
        "show_results_dialog"
    ]
    assert not snapshot.supports("/briosa.FileOperations/DeleteFiles")
    await client.aclose()


def _with_detail(
    failure: OperationFailure, value: PolicyDenialDetails
) -> OperationFailure:
    return replace(failure, policy_denial=value)
