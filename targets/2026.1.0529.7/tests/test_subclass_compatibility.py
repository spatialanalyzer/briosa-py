"""Subclasses of the dataclasses 0.5.1 grew, and of BriosaStartOptions, keep working.

``fixtures/pickled-0.5.0-subclasses.json`` holds values of the subclasses in
``pickled_subclasses.py`` as the published 0.5.0 wheel of this target pickled
them, with protocol 4, on Python 3.10 and on Python 3.14, and the startup-timeout
exception that 0.5.0 raised on each. Each type has an ordinary and a slotted
subclass, so both the base's pickle hooks and the ones dataclasses generates
for a slotted subclass are covered.
"""

from __future__ import annotations

import asyncio
import base64
import copy
import dataclasses
import json
import pickle
import sys
from pathlib import Path
from typing import Any, cast

import pickled_subclasses as sub
import pytest
from test_startup_budget import bounds, expiry, startup_expiry_error

from briosa import (
    BriosaLifecycleBounds,
    BriosaOperationCapability,
    BriosaServerSelection,
    BriosaServerSnapshot,
    BriosaStartOptions,
    BriosaStartupError,
    ConfiguredSpatialAnalyzerInteractionMode,
    ExecutionDisposition,
    MpExecutionDetails,
    MpExecutionState,
    OperationAdmission,
    OperationDurationClass,
    OperationFailure,
    OperationFailureKind,
    OperationRiskFlag,
    OperationValidationStatus,
    PolicyDenialDetails,
    PolicyDenialRule,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    SpatialAnalyzerLaunchOptions,
)
from briosa.models import _startup_timeout_omitted
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET

FIXTURE = json.loads(
    (Path(__file__).parent / "fixtures/pickled-0.5.0-subclasses.json").read_text(
        encoding="utf-8"
    )
)
RUNS: list[dict[str, Any]] = FIXTURE["runs"]

FAILURE: dict[str, Any] = {
    "operation_id": "file_operations.get_working_directory",
    "kind": OperationFailureKind.POLICY_DENIED,
    "diagnostic_code": "policy-denied",
    "execution_disposition": ExecutionDisposition.NOT_STARTED,
    "recovery_guidance": RecoveryGuidance.NONE,
    "replay_guidance": ReplayGuidance.DO_NOT_REPLAY,
    "replay_safety": ReplaySafety.SAFE,
    "mp_execution": MpExecutionDetails(
        state=MpExecutionState.SUCCEEDED, mp_result_code=2
    ),
    "worker_generation": 3,
}
CAPABILITY: tuple[
    str,
    str,
    str,
    str,
    tuple[OperationRiskFlag, ...],
    OperationDurationClass,
    OperationValidationStatus,
    OperationAdmission,
] = (
    "file_operations.get_working_directory",
    "briosa.FileOperations",
    "GetWorkingDirectory",
    "/briosa.FileOperations/GetWorkingDirectory",
    (OperationRiskFlag.FILESYSTEM_METADATA,),
    OperationDurationClass.QUICK,
    OperationValidationStatus.NO_RECORDED_GAP,
    OperationAdmission.DENIED_OVERRIDE,
)
SNAPSHOT: tuple[
    str, str, str, str, bool, tuple[BriosaOperationCapability, ...], str, str
] = (
    "0.10.0",
    "a" * 40,
    "briosa",
    SPATIAL_ANALYZER_TARGET,
    True,
    (sub.OrdinaryCapability(*CAPABILITY),),
    "standard",
    "sha256:" + "ab" * 32,
)
# The same values the 0.5.0 wheel pickled, built with 0.5.1, positional
# arguments included.
FRESH: dict[str, Any] = {
    "ordinary_start_options": sub.OrdinaryStartOptions(
        startup_timeout=300.0, tag="tagged"
    ),
    "slotted_start_options": sub.SlottedStartOptions(tag="tagged"),
    "ordinary_failure": sub.OrdinaryFailure(tag="tagged", **FAILURE),
    "slotted_failure": sub.SlottedFailure(tag="tagged", **FAILURE),
    "ordinary_capability": sub.OrdinaryCapability(*CAPABILITY, "tagged"),
    "slotted_capability": sub.SlottedCapability(*CAPABILITY, "tagged"),
    "ordinary_snapshot": sub.OrdinarySnapshot(*SNAPSHOT, "tagged"),
    "slotted_snapshot": sub.SlottedSnapshot(*SNAPSHOT, "tagged"),
}
# What each 0.5.1 field holds when a 0.5.0 value didn't carry it.
ADDED_DEFAULTS: dict[type[Any], dict[str, Any]] = {
    OperationFailure: {"policy_denial": None},
    BriosaOperationCapability: {"policy_denial": None, "request_options": None},
    BriosaServerSnapshot: {
        "lifecycle_bounds": None,
        "configured_interaction_mode": ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN,
    },
}
# __match_args__ as 0.5.0 defined it.
MATCH_ARGS_0_5_0: dict[type[Any], tuple[str, ...]] = {
    BriosaStartOptions: (
        "server_selection",
        "start_spatial_analyzer_sdk",
        "launch_spatial_analyzer",
        "connect_to_spatial_analyzer",
        "launch_options",
        "startup_timeout",
        "logging",
    ),
    OperationFailure: (),
    BriosaOperationCapability: (
        "operation_id",
        "grpc_service",
        "rpc",
        "fully_qualified_method",
        "risk_flags",
        "duration_class",
        "validation_status",
        "admission",
    ),
    BriosaServerSnapshot: (
        "briosa_version",
        "source_revision",
        "protocol_package",
        "spatial_analyzer_target",
        "ready_for_mp",
        "operations",
        "admission_profile",
        "policy_fingerprint",
    ),
}


def loaded(run: dict[str, Any], name: str) -> Any:
    return pickle.loads(base64.b64decode(run["values"][name]["pickle"]))


def added_defaults(value: Any) -> dict[str, Any]:
    for base, defaults in ADDED_DEFAULTS.items():
        if isinstance(value, base):
            return defaults
    return {}


def run_id(run: dict[str, Any]) -> str:
    return f"python-{run['python']}"


def test_the_fixture_was_written_by_the_published_0_5_0_wheel() -> None:
    assert [run["briosa"] for run in RUNS] == ["0.5.0", "0.5.0"]
    assert [run["python"].rsplit(".", 1)[0] for run in RUNS] == ["3.10", "3.14"]
    for run in RUNS:
        assert set(run["values"]) == set(FRESH)


@pytest.mark.parametrize("name", sorted(FRESH))
@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_a_0_5_0_subclass_pickle_loads_into_its_0_5_0_fields(
    run: dict[str, Any], name: str
) -> None:
    value = loaded(run, name)
    assert type(value) is type(FRESH[name])
    assert value.tag == "tagged"
    assert repr(value) == run["values"][name]["repr"]
    assert value == FRESH[name]
    assert hash(value) == hash(FRESH[name])
    for field_name, default in added_defaults(value).items():
        assert getattr(value, field_name) == default, field_name
    again = pickle.loads(pickle.dumps(value))
    assert again == value
    assert again.tag == "tagged"


@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_0_5_0_subclassed_start_options_keep_their_fixed_budget(
    run: dict[str, Any],
) -> None:
    ordinary = loaded(run, "ordinary_start_options")
    slotted = loaded(run, "slotted_start_options")
    assert ordinary.startup_timeout == 300.0
    assert slotted.startup_timeout == 120.0
    # Client 0.5.0 had no automatic budget, so its options load as explicit.
    assert not _startup_timeout_omitted(ordinary)
    assert not _startup_timeout_omitted(slotted)


@pytest.mark.parametrize("name", sorted(FRESH))
def test_a_fresh_subclass_value_prints_as_0_5_0_printed_it(name: str) -> None:
    for run in RUNS:
        assert repr(FRESH[name]) == run["values"][name]["repr"]


def test_match_args_are_those_of_0_5_0() -> None:
    for cls, names in MATCH_ARGS_0_5_0.items():
        assert cls.__match_args__ == names, cls.__name__
    # A subclass's own fields follow the 0.5.0 ones, as with 0.5.0.
    assert sub.OrdinarySnapshot.__match_args__ == (
        *MATCH_ARGS_0_5_0[BriosaServerSnapshot],
        "tag",
    )
    assert sub.SlottedCapability.__match_args__ == (
        *MATCH_ARGS_0_5_0[BriosaOperationCapability],
        "tag",
    )
    assert sub.OrdinaryFailure.__match_args__ == ("tag",)


def describe(value: object) -> str:
    match value:
        case BriosaServerSnapshot(version, _, _, target, ready, operations):
            return f"snapshot {version} {target} {ready} {len(operations)}"
        case BriosaOperationCapability(operation, _, rpc):
            return f"capability {operation} {rpc}"
        case _:
            return "other"


def test_a_0_5_0_positional_match_still_matches() -> None:
    snapshot = FRESH["ordinary_snapshot"]
    assert describe(snapshot) == f"snapshot 0.10.0 {SPATIAL_ANALYZER_TARGET} True 1"
    assert describe(
        dataclasses.replace(snapshot, lifecycle_bounds=BriosaLifecycleBounds())
    ) == describe(snapshot)
    assert describe(FRESH["slotted_capability"]) == (
        "capability file_operations.get_working_directory GetWorkingDirectory"
    )


def test_the_0_5_1_fields_are_keyword_only() -> None:
    # A positional value beyond the 0.5.0 fields is the subclass's own field.
    for name in ("ordinary_capability", "slotted_capability"):
        assert FRESH[name].tag == "tagged"
        assert FRESH[name].policy_denial is None
    for name in ("ordinary_snapshot", "slotted_snapshot"):
        assert FRESH[name].tag == "tagged"
        assert FRESH[name].lifecycle_bounds is None
    with pytest.raises(TypeError):
        BriosaServerSnapshot(*SNAPSHOT, BriosaLifecycleBounds())  # type: ignore[misc]
    snapshot = BriosaServerSnapshot(*SNAPSHOT, lifecycle_bounds=BriosaLifecycleBounds())
    assert snapshot.lifecycle_bounds == BriosaLifecycleBounds()


def with_0_5_1_fields(value: Any) -> Any:
    denial = PolicyDenialDetails(rule=PolicyDenialRule.OVERRIDE)
    if isinstance(value, OperationFailure):
        return dataclasses.replace(value, policy_denial=denial)
    if isinstance(value, BriosaOperationCapability):
        return dataclasses.replace(value, policy_denial=denial, request_options=())
    if isinstance(value, BriosaServerSnapshot):
        return dataclasses.replace(
            value,
            lifecycle_bounds=BriosaLifecycleBounds(),
            configured_interaction_mode=ConfiguredSpatialAnalyzerInteractionMode.SILENT,
        )
    return value


def clones(value: Any) -> list[Any]:
    return [
        copy.copy(value),
        copy.deepcopy(value),
        *(
            pickle.loads(pickle.dumps(value, protocol=protocol))
            for protocol in range(pickle.HIGHEST_PROTOCOL + 1)
        ),
    ]


@pytest.mark.parametrize("name", sorted(FRESH))
def test_copies_and_pickles_of_a_subclass_keep_every_field(name: str) -> None:
    value = with_0_5_1_fields(FRESH[name])
    for clone in clones(value):
        assert type(clone) is type(value)
        for item in dataclasses.fields(value):
            assert getattr(clone, item.name) == getattr(value, item.name), item.name


START_OPTIONS_SUBCLASSES: list[type[BriosaStartOptions]] = [
    sub.OrdinaryStartOptions,
    sub.SlottedStartOptions,
]


class PlainStartOptions(BriosaStartOptions):
    """A subclass that is not itself a dataclass."""


@pytest.mark.parametrize(
    "cls",
    [*START_OPTIONS_SUBCLASSES, PlainStartOptions],
    ids=["ordinary", "slotted", "plain"],
)
def test_subclassed_start_options_record_the_omission(
    cls: type[BriosaStartOptions],
) -> None:
    omitted = cls()
    assert _startup_timeout_omitted(omitted)
    assert omitted.startup_timeout == 120.0
    for clone in clones(omitted):
        assert _startup_timeout_omitted(clone)
    positional = cls(
        BriosaServerSelection(), True, True, True, SpatialAnalyzerLaunchOptions(), 120.0
    )
    for explicit in (
        cls(startup_timeout=120.0),
        cls(startup_timeout=omitted.startup_timeout),
        positional,
        dataclasses.replace(omitted),
    ):
        assert not _startup_timeout_omitted(explicit)
        for clone in clones(explicit):
            assert not _startup_timeout_omitted(clone)
    assert omitted == cls(startup_timeout=120.0)
    assert hash(omitted) == hash(cls(startup_timeout=120.0))


@pytest.mark.parametrize("cls", START_OPTIONS_SUBCLASSES, ids=["ordinary", "slotted"])
def test_subclassed_start_options_adopt_like_the_base(
    cls: type[BriosaStartOptions],
) -> None:
    published = bounds(startup_with_launch=300_000)
    assert expiry(published=published, options=cls())[0] == 320.0
    assert expiry(published=published, options=copy.copy(cls()))[0] == 320.0
    explicit = cls(startup_timeout=120.0)
    assert expiry(published=published, options=explicit)[0] == 120.0


def test_a_subclass_constructor_without_the_parameter_gives_an_explicit_budget() -> (
    None
):
    class Budgeted(BriosaStartOptions):
        def __init__(self, budget: float | None = None) -> None:
            if budget is None:
                super().__init__()
            else:
                super().__init__(startup_timeout=budget)

    assert not _startup_timeout_omitted(Budgeted())
    assert not _startup_timeout_omitted(Budgeted(300.0))
    assert Budgeted(300.0).startup_timeout == 300.0


def exceptions(run: dict[str, Any]) -> dict[str, Any]:
    return cast(dict[str, Any], run["exceptions"])


@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_the_startup_timeout_pickles_as_0_5_0s_did(run: dict[str, Any]) -> None:
    written = exceptions(run)["startup_timeout"]
    theirs = pickle.loads(base64.b64decode(written["pickle"]))
    ours = startup_expiry_error()
    mine = pickle.loads(pickle.dumps(ours, protocol=4))
    # Pickling never carries a cause, so neither load has one.
    assert theirs.__cause__ is None
    assert mine.__cause__ is None
    assert mine.diagnostic_code == "startup-timeout"
    if run["python"].startswith("3.10."):
        # 0.5.0 raised a bare asyncio.TimeoutError on Python 3.10.
        assert written["type"] == "asyncio.exceptions.TimeoutError"
        assert type(theirs) is asyncio.TimeoutError
        if sys.version_info < (3, 11):
            # Its replacement is still an asyncio.TimeoutError, after a load too.
            assert isinstance(mine, asyncio.TimeoutError)
            assert str(mine) == "Briosa startup failed (startup-timeout)."
            assert mine.args == ("Briosa startup failed (startup-timeout).",)
        return
    assert written["type"] == "briosa.errors.BriosaStartupError"
    if sys.version_info >= (3, 11):
        # From Python 3.11 the expiry is the 0.5.0 exception, byte for byte.
        assert pickle.dumps(ours, protocol=4) == base64.b64decode(written["pickle"])
        assert type(mine) is type(theirs) is BriosaStartupError
        assert str(mine) == str(theirs)
        assert mine.args == theirs.args
        assert mine.diagnostic_code == theirs.diagnostic_code


@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_a_0_5_0_startup_error_loads_as_it_did(run: dict[str, Any]) -> None:
    written = exceptions(run)["startup_error"]
    theirs = pickle.loads(base64.b64decode(written["pickle"]))
    assert type(theirs) is BriosaStartupError
    assert theirs.diagnostic_code == "startup-timeout"
    # BriosaStartupError pickles as in 0.5.0, so 0.5.1 writes the same bytes.
    assert pickle.dumps(BriosaStartupError("startup-timeout"), protocol=4) == (
        base64.b64decode(written["pickle"])
    )
