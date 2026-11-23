"""Applications' own subclasses, against the stated 0.5.0 compatibility guarantee.

Subclasses of ``BriosaStartOptions`` behave as in 0.5.0, which is guaranteed.
For subclasses of ``OperationFailure``, ``BriosaOperationCapability`` and
``BriosaServerSnapshot``, and for reflection on those three types, the README
lists known differences from 0.5.0. Each has one test here, named
``test_documented_difference_...``, that pins the current behaviour so that a
later change to it is noticed.

``fixtures/pickled-0.5.0-subclasses.json`` holds values of the subclasses in
``pickled_subclasses.py`` as the published 0.5.0 wheel of this target pickled
them, with protocol 4, on Python 3.10 and on Python 3.14, and the startup-timeout
exception that 0.5.0 raised on each. ``fixtures/options-reflection-0.5.0.json``
holds what ``options_reflection.describe()`` returned with that wheel on each
Python version from 3.10 to 3.14.
"""

from __future__ import annotations

import asyncio
import base64
import copy
import dataclasses
import json
import pickle
import pickletools
import sys
import typing
from collections.abc import Callable
from pathlib import Path
from typing import Any, cast

import options_reflection
import pickled_subclasses as sub
import pytest
from test_startup_budget import bounds, expiry, startup_expiry_error

from briosa import (
    BriosaLifecycleBounds,
    BriosaLoggingOptions,
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
REFLECTION = json.loads(
    (Path(__file__).parent / "fixtures/options-reflection-0.5.0.json").read_text(
        encoding="utf-8"
    )
)

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


START_OPTIONS_PICKLES = ["ordinary_start_options", "slotted_start_options"]


@pytest.mark.parametrize("name", START_OPTIONS_PICKLES)
@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_a_0_5_0_pickle_of_a_start_options_subclass_loads_as_in_0_5_0(
    run: dict[str, Any], name: str
) -> None:
    value = loaded(run, name)
    assert type(value) is type(FRESH[name])
    assert value.tag == "tagged"
    assert repr(value) == run["values"][name]["repr"]
    assert value == FRESH[name]
    assert hash(value) == hash(FRESH[name])
    assert not _startup_timeout_omitted(value)
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
    assert not _startup_timeout_omitted(ordinary)
    assert not _startup_timeout_omitted(slotted)


GROWN_SUBCLASSES = [name for name in sorted(FRESH) if name not in START_OPTIONS_PICKLES]


@pytest.mark.parametrize("name", GROWN_SUBCLASSES)
@pytest.mark.parametrize("run", RUNS, ids=run_id)
def test_documented_difference_0_5_0_pickles_of_subclasses_of_grown_types(
    run: dict[str, Any], name: str
) -> None:
    """Documented difference from 0.5.0: these pickles are not guaranteed to load.

    Today a subclass declared without ``slots=True`` loads correctly, with the
    0.5.1 fields at their defaults. One declared with ``slots=True`` restores its
    saved values by position: the subclass's own value lands in the first field
    0.5.1 added, and the subclass's field is left unset.
    """
    value = loaded(run, name)
    assert type(value) is type(FRESH[name])
    added = list(added_defaults(value))
    if name.startswith("ordinary_"):
        assert value == FRESH[name]
        assert value.tag == "tagged"
        assert repr(value) == run["values"][name]["repr"]
        for field_name, default in added_defaults(value).items():
            assert getattr(value, field_name) == default, field_name
        return
    assert getattr(value, added[0]) == "tagged"
    for field_name in ("tag", *added[1:]):
        with pytest.raises(AttributeError):
            getattr(value, field_name)
    with pytest.raises(AttributeError):
        repr(value)


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
def test_subclassed_start_options_behave_as_in_0_5_0(
    cls: type[BriosaStartOptions],
) -> None:
    # A subclass's budget is always explicit, as every budget was with 0.5.0.
    left_out = cls()
    assert not _startup_timeout_omitted(left_out)
    assert left_out.startup_timeout == 120.0
    assert type(left_out.startup_timeout) is float
    positional = cls(
        BriosaServerSelection(), True, True, True, SpatialAnalyzerLaunchOptions(), 120
    )
    assert positional.startup_timeout == 120
    assert type(positional.startup_timeout) is int
    for value in (left_out, cls(startup_timeout=300.0), dataclasses.replace(left_out)):
        assert not _startup_timeout_omitted(value)
        for clone in clones(value):
            assert type(clone) is cls
            assert clone == value
            assert not _startup_timeout_omitted(clone)
    assert left_out == cls(startup_timeout=120.0)
    assert hash(left_out) == hash(cls(startup_timeout=120.0))


@pytest.mark.parametrize("cls", START_OPTIONS_SUBCLASSES, ids=["ordinary", "slotted"])
def test_a_subclass_startup_uses_its_own_budget(
    cls: type[BriosaStartOptions],
) -> None:
    # Never the server's published allowance.
    published = bounds(startup_with_launch=300_000)
    assert expiry(published=published, options=cls())[0] == 120.0
    assert expiry(published=published, options=copy.copy(cls()))[0] == 120.0
    assert expiry(published=published, options=cls(startup_timeout=200.0))[0] == 200.0
    # The exact class adopts it.
    assert expiry(published=published, options=BriosaStartOptions())[0] == 320.0


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


class DelegatingNew(BriosaStartOptions):
    def __new__(cls, *args: Any, **kwargs: Any) -> DelegatingNew:
        return super().__new__(cls)


@dataclasses.dataclass(frozen=True, slots=True)
class FieldNamedLikeAPrivateOne(BriosaStartOptions):
    _briosa_startup_timeout_omission: str = "mine"


@dataclasses.dataclass(frozen=True)
class OwnPostInit(BriosaStartOptions):
    tag: str = "untagged"

    def __post_init__(self) -> None:
        # Never calls the base, so the base's checks are skipped, as in 0.5.0.
        pass


@dataclasses.dataclass(frozen=True, slots=True)
class NewArguments(BriosaStartOptions):
    tag: str = dataclasses.field(kw_only=True)

    def __new__(cls, *args: Any, tag: str, **kwargs: Any) -> NewArguments:
        # Named explicitly: Python 3.10 can't use a bare super() in a slotted
        # dataclass, with 0.5.0 too.
        return BriosaStartOptions.__new__(cls)

    def __getnewargs_ex__(self) -> tuple[tuple[Any, ...], dict[str, Any]]:
        return (), {"tag": self.tag}


SUBCLASS_SHAPES: dict[str, Callable[[], BriosaStartOptions]] = {
    "delegating-new": lambda: DelegatingNew(startup_timeout=120.0),
    "field-named-like-a-private-one": lambda: FieldNamedLikeAPrivateOne(
        _briosa_startup_timeout_omission="x"
    ),
    "own-post-init": lambda: OwnPostInit(start_spatial_analyzer_sdk=False),
    "new-arguments": lambda: NewArguments(tag="x"),
}


@pytest.mark.parametrize("shape", sorted(SUBCLASS_SHAPES))
def test_options_subclass_shapes_construct_copy_and_pickle_as_in_0_5_0(
    shape: str,
) -> None:
    value = SUBCLASS_SHAPES[shape]()
    assert value.startup_timeout == 120.0
    assert not _startup_timeout_omitted(value)
    if shape == "own-post-init":
        # The base's checks never ran, as in 0.5.0.
        assert value.connect_to_spatial_analyzer
        assert not value.start_spatial_analyzer_sdk
    for clone in (
        copy.copy(value),
        copy.deepcopy(value),
        pickle.loads(pickle.dumps(value)),
    ):
        assert type(clone) is type(value)
        assert clone == value
        assert repr(clone) == repr(value)
        assert not _startup_timeout_omitted(clone)
    assert expiry(
        published=bounds(startup_with_launch=300_000),
        options=value,
        hang_at="launch-sa" if shape == "own-post-init" else "connect-sdk",
    )[0] == (120.0)


def test_the_reflection_fixture_was_written_by_the_published_0_5_0_wheel() -> None:
    assert [run["briosa"] for run in REFLECTION["runs"]] == ["0.5.0"] * 5
    assert [run["python"].rsplit(".", 1)[0] for run in REFLECTION["runs"]] == [
        "3.10",
        "3.11",
        "3.12",
        "3.13",
        "3.14",
    ]


def test_the_options_constructor_reflects_as_in_0_5_0() -> None:
    """``inspect.signature``, ``inspect.getfullargspec``, ``typing.get_type_hints``
    and the constructor's attributes, for ``BriosaStartOptions`` and a subclass
    that inherits its constructor, against the published 0.5.0 wheel on the same
    Python version."""
    minor = ".".join(map(str, sys.version_info[:2]))
    recorded = {
        run["python"].rsplit(".", 1)[0]: run["reflection"] for run in REFLECTION["runs"]
    }
    if minor not in recorded:
        pytest.skip(f"0.5.0 reflection was recorded on Python 3.10-3.14, not {minor}")
    expected = copy.deepcopy(recorded[minor])
    actual = options_reflection.describe()
    if sys.version_info < (3, 11):
        # Python 3.10's get_type_hints adds Optional for a None default that it
        # finds through the function's own positional parameters. The
        # constructor's are *args and **kwargs, so on 3.10 the hint keeps the
        # annotation's spelling. Both hints are the same type and compare equal.
        for name in expected:
            hints = expected[name]["type-hints-init"]
            assert hints["logging"] == (
                "typing.Optional[briosa.logging_options.BriosaLoggingOptions]"
            )
            hints["logging"] = "briosa.logging_options.BriosaLoggingOptions | None"
        logging = typing.get_type_hints(BriosaStartOptions.__init__)["logging"]
        assert logging == typing.Optional[BriosaLoggingOptions]  # noqa: UP045
    assert actual == expected


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


def test_documented_difference_reflection_includes_the_new_fields() -> None:
    """Documented difference from 0.5.0: fields(), astuple() and asdict().

    They include the fields 0.5.1 added, on the three types and on their
    subclasses, so code that unpacks an exact number of values needs updating.
    """
    expected = {
        OperationFailure: (9, ["policy_denial"]),
        BriosaOperationCapability: (8, ["policy_denial", "request_options"]),
        BriosaServerSnapshot: (
            8,
            ["lifecycle_bounds", "configured_interaction_mode"],
        ),
    }
    values: list[Any] = [
        OperationFailure(**FAILURE),
        BriosaOperationCapability(*CAPABILITY),
        BriosaServerSnapshot(*SNAPSHOT),
        *(FRESH[name] for name in GROWN_SUBCLASSES),
    ]
    for value in values:
        base = next(cls for cls in expected if isinstance(value, cls))
        count_0_5_0, added = expected[base]
        own = 1 if type(value) is not base else 0
        names = [item.name for item in dataclasses.fields(value)]
        assert len(names) == count_0_5_0 + len(added) + own
        assert names[count_0_5_0 : count_0_5_0 + len(added)] == added
        assert len(dataclasses.astuple(value)) == len(names)
        assert list(dataclasses.asdict(value)) == names


def test_documented_difference_a_name_of_a_new_field_in_a_subclass() -> None:
    """Documented difference from 0.5.0: a subclass that uses a new field's name.

    A read-only property with that name makes construction fail, because the
    class sets the field. A field with that name replaces the new one and keeps
    the position it had with 0.5.0.
    """

    class Reads(BriosaServerSnapshot):
        @property
        def lifecycle_bounds(self) -> str:  # type: ignore[override]
            return "mine"

    with pytest.raises(AttributeError):
        Reads(*SNAPSHOT)

    @dataclasses.dataclass(frozen=True)
    class Declares(BriosaServerSnapshot):
        lifecycle_bounds: str = "mine"  # type: ignore[assignment]

    declared = Declares(*SNAPSHOT, "positional")
    assert declared.lifecycle_bounds == "positional"
    assert Declares.__match_args__[-1] == "lifecycle_bounds"
    assert [item.name for item in dataclasses.fields(Declares)][-1] == (
        "configured_interaction_mode"
    )


def global_names(value: object) -> set[str]:
    return {
        str(argument)
        for opcode, argument, _ in pickletools.genops(pickle.dumps(value, protocol=4))
        if opcode.name in {"SHORT_BINUNICODE", "BINUNICODE"}
    }


def test_documented_difference_0_5_1_pickles_and_client_0_5_0() -> None:
    """Documented difference from 0.5.0: 0.5.1 pickles may not load in 0.5.0.

    A pickle names every class it holds, and client 0.5.0 has none of the
    classes 0.5.1 added: a ``BriosaServerSnapshot`` always holds one, and the
    other two types do once a 0.5.1 field is set.
    """
    added = {
        "ConfiguredSpatialAnalyzerInteractionMode",
        "PolicyDenialDetails",
        "PolicyDenialRule",
        "BriosaLifecycleBounds",
    }
    assert "ConfiguredSpatialAnalyzerInteractionMode" in global_names(
        BriosaServerSnapshot(*SNAPSHOT)
    )
    assert not added & global_names(OperationFailure(**FAILURE))
    assert not added & global_names(BriosaOperationCapability(*CAPABILITY))
    denial = PolicyDenialDetails(rule=PolicyDenialRule.OVERRIDE)
    assert "PolicyDenialDetails" in global_names(
        OperationFailure(**FAILURE, policy_denial=denial)
    )
    capability = BriosaOperationCapability(*CAPABILITY)
    assert not added & global_names(dataclasses.replace(capability, request_options=()))
    option = OperationRequestOption(
        field_name="show_results_dialog",
        effect=OperationRequestOptionEffect.INTERACTIVE_UI,
        condition=OperationRequestOptionCondition.WHEN_TRUE,
        omission=OperationRequestOptionOmission.DOES_NOT_ACTIVATE,
        admission=OperationAdmission.ADMITTED,
    )
    assert "OperationRequestOption" in global_names(
        dataclasses.replace(capability, request_options=(option,))
    )
