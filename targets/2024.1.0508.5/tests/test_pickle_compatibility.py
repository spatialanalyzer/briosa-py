"""Values from client 0.5.0 keep working in 0.5.1.

``fixtures/pickled-0.5.0.json`` was written by the published 0.5.0 wheel of this
target (see its ``generated_by``): each value pickled with protocol 4, and its
``repr()``. The 0.5.1 fields take their defaults on load, and ``repr()``,
equality and hashing cover only the fields 0.5.0 had.
"""

from __future__ import annotations

import base64
import dataclasses
import json
import pickle
from pathlib import Path
from typing import Any

import pytest

from briosa import (
    BriosaLifecycleBounds,
    BriosaOperationCapability,
    BriosaServerSnapshot,
    BriosaStartOptions,
    ConfiguredSpatialAnalyzerInteractionMode,
    ExecutionDisposition,
    MpExecutionDetails,
    MpExecutionState,
    OperationAdmission,
    OperationDurationClass,
    OperationFailure,
    OperationFailureKind,
    OperationRequestOption,
    OperationRequestOptionCondition,
    OperationRequestOptionEffect,
    OperationRequestOptionOmission,
    OperationRiskFlag,
    OperationValidationStatus,
    PolicyDenialDetails,
    PolicyDenialRule,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
)
from briosa.models import _startup_timeout_omitted
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET

FIXTURE = json.loads(
    (Path(__file__).parent / "fixtures/pickled-0.5.0.json").read_text(encoding="utf-8")
)
VALUES: dict[str, dict[str, Any]] = FIXTURE["values"]

CAPABILITY = BriosaOperationCapability(
    "file_operations.get_working_directory",
    "briosa.FileOperations",
    "GetWorkingDirectory",
    "/briosa.FileOperations/GetWorkingDirectory",
    (OperationRiskFlag.FILESYSTEM_METADATA,),
    OperationDurationClass.QUICK,
    OperationValidationStatus.NO_RECORDED_GAP,
    OperationAdmission.DENIED_OVERRIDE,
)
# The same values the 0.5.0 wheel pickled, built with 0.5.1.
FRESH: dict[str, Any] = {
    "failure": OperationFailure(
        operation_id="file_operations.get_working_directory",
        kind=OperationFailureKind.POLICY_DENIED,
        diagnostic_code="policy-denied",
        execution_disposition=ExecutionDisposition.NOT_STARTED,
        recovery_guidance=RecoveryGuidance.NONE,
        replay_guidance=ReplayGuidance.DO_NOT_REPLAY,
        replay_safety=ReplaySafety.SAFE,
        mp_execution=MpExecutionDetails(
            state=MpExecutionState.SUCCEEDED, mp_result_code=2
        ),
        worker_generation=3,
    ),
    "capability": CAPABILITY,
    "snapshot": BriosaServerSnapshot(
        "0.10.0",
        "a" * 40,
        "briosa",
        SPATIAL_ANALYZER_TARGET,
        True,
        (CAPABILITY,),
        "standard",
        "sha256:" + "ab" * 32,
    ),
    "start_options": BriosaStartOptions(),
    "start_options_explicit": BriosaStartOptions(startup_timeout=120.0),
}


def loaded(name: str) -> Any:
    return pickle.loads(base64.b64decode(VALUES[name]["pickle"]))


def test_the_fixture_was_written_by_the_published_0_5_0_wheel() -> None:
    assert FIXTURE["generated_by"].startswith("briosa 0.5.0, ")
    assert set(VALUES) == set(FRESH)


@pytest.mark.parametrize("name", sorted(FRESH))
def test_a_0_5_0_pickle_loads_prints_compares_and_hashes(name: str) -> None:
    value = loaded(name)
    assert repr(value) == VALUES[name]["repr"]
    assert value == FRESH[name]
    assert hash(value) == hash(FRESH[name])
    assert dataclasses.replace(value) == value
    # Pickling again under 0.5.1 round-trips.
    assert pickle.loads(pickle.dumps(value)) == value


@pytest.mark.parametrize("name", sorted(FRESH))
def test_a_fresh_value_prints_as_0_5_0_printed_it(name: str) -> None:
    assert repr(FRESH[name]) == VALUES[name]["repr"]


def test_the_0_5_1_fields_take_their_defaults_on_a_0_5_0_load() -> None:
    failure = loaded("failure")
    assert failure.policy_denial is None
    capability = loaded("capability")
    assert capability.policy_denial is None
    assert capability.request_options is None
    snapshot = loaded("snapshot")
    assert snapshot.lifecycle_bounds is None
    assert (
        snapshot.configured_interaction_mode
        is ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN
    )
    assert snapshot.operations[0].request_options is None


def test_0_5_0_start_options_keep_the_fixed_budget() -> None:
    # Client 0.5.0 had no automatic budget, so its options load as explicit.
    for name in ("start_options", "start_options_explicit"):
        options = loaded(name)
        assert options.startup_timeout == 120.0
        assert not _startup_timeout_omitted(options)


def test_the_0_5_1_fields_stay_out_of_repr_equality_and_hash() -> None:
    denial = PolicyDenialDetails(rule=PolicyDenialRule.OVERRIDE)
    failure = FRESH["failure"]
    detailed = dataclasses.replace(failure, policy_denial=denial)
    assert detailed == failure
    assert hash(detailed) == hash(failure)
    assert repr(detailed) == repr(failure)
    assert detailed.policy_denial == denial

    option = OperationRequestOption(
        field_name="show_results_dialog",
        effect=OperationRequestOptionEffect.INTERACTIVE_UI,
        condition=OperationRequestOptionCondition.WHEN_TRUE,
        omission=OperationRequestOptionOmission.DOES_NOT_ACTIVATE,
        admission=OperationAdmission.ADMITTED,
    )
    described = dataclasses.replace(
        CAPABILITY, policy_denial=denial, request_options=(option,)
    )
    assert described == CAPABILITY
    assert repr(described) == repr(CAPABILITY)

    snapshot = FRESH["snapshot"]
    bounded = dataclasses.replace(
        snapshot,
        lifecycle_bounds=BriosaLifecycleBounds(),
        configured_interaction_mode=ConfiguredSpatialAnalyzerInteractionMode.SILENT,
    )
    assert bounded == snapshot
    assert hash(bounded) == hash(snapshot)
    assert repr(bounded) == repr(snapshot)


def test_a_0_5_1_pickle_keeps_the_0_5_1_fields() -> None:
    denial = PolicyDenialDetails(rule=PolicyDenialRule.FLAG, denied_flag=None)
    failure = dataclasses.replace(FRESH["failure"], policy_denial=denial)
    assert pickle.loads(pickle.dumps(failure)).policy_denial == denial
    snapshot = dataclasses.replace(
        FRESH["snapshot"],
        lifecycle_bounds=BriosaLifecycleBounds(),
        configured_interaction_mode=ConfiguredSpatialAnalyzerInteractionMode.MANUAL,
    )
    restored = pickle.loads(pickle.dumps(snapshot))
    assert restored.lifecycle_bounds == BriosaLifecycleBounds()
    assert (
        restored.configured_interaction_mode
        is ConfiguredSpatialAnalyzerInteractionMode.MANUAL
    )
