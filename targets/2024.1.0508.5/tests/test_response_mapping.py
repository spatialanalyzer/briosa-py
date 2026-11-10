"""Every operation maps a fully populated response (#45, freeze plan 8.8)."""

from __future__ import annotations

import collections.abc
import dataclasses
import types
import typing

import pytest
from facade_support import (
    RecordingTransport,
    bound_facades,
    facade_functions,
    populated,
    required_arguments,
    started_client,
    succeeded,
)
from test_operation_surface import protocol_methods

from briosa import (
    BriosaProtocolError,
    CollectionInstrumentId,
    CollectionItemName,
    CollectionObjectName,
    FitErrorResult,
    ItemType,
    MpCompletion,
    MpExecutionState,
    ObjectType,
    instrument_operations_pb2,
    spatial_analyzer_values_pb2,
    variables_pb2,
)
from briosa.operation_protocol import map_response, operation_method

QUICK_FIT = "/briosa.InstrumentOperations/LocateInstrumentGroupToSurfaceQuickFit"


def frame(name: str) -> CollectionObjectName:
    return CollectionObjectName(
        collection_name="Inspection", object_name=name, object_type=ObjectType.FRAME
    )


async def test_every_operation_maps_a_fully_populated_response() -> None:
    transport = RecordingTransport()
    transport.default_response = lambda _path, response_type: populated(response_type)
    client = await started_client(transport)
    failures: dict[str, str] = {}
    completions: list[MpCompletion] = []

    functions = facade_functions()
    for operation_id, facade in bound_facades(client).items():
        before = len(completions)
        try:
            await facade(
                **required_arguments(functions[operation_id]),
                on_mp_completion=completions.append,
            )
        except Exception as error:  # Collect every failure at once.
            failures[operation_id] = f"{type(error).__name__}: {error}"
            continue
        if len(completions) != before + 1:
            failures[operation_id] = "no MP completion reported"

    assert failures == {}
    assert {completion.state for completion in completions} == {
        MpExecutionState.SUCCEEDED
    }
    assert {path for path, _request, _timeout in transport.requests} == (
        protocol_methods()
    )
    await client.aclose()


async def test_quick_fit_maps_maximum_absolute_error_to_maximum_error() -> None:
    transport = RecordingTransport()
    response = populated(
        instrument_operations_pb2.LocateInstrumentGroupToSurfaceQuickFitResult
    )
    response_message = typing.cast(
        instrument_operations_pb2.LocateInstrumentGroupToSurfaceQuickFitResult,
        response,
    )
    response_message.rms_error = 0.012
    response_message.maximum_absolute_error = 0.034
    transport.queue(QUICK_FIT, response)
    client = await started_client(transport)

    result = (
        await client.instrument_operations.locate_instrument_group_to_surface_quick_fit(
            CollectionInstrumentId(collection_name="Inspection", instrument_id=1),
            frame("Measured"),
            frame("Surface Points"),
            frame("Surface"),
            other_objects_to_transform=[frame("Fixture")],
        )
    )

    assert result == FitErrorResult(rms_error=0.012, maximum_error=0.034)
    await client.aclose()


@dataclasses.dataclass(frozen=True, slots=True, kw_only=True)
class DriftedFitResult:
    rms_error: float
    unexpected_error: float


def test_a_result_type_that_drifts_from_the_wire_is_a_protocol_failure() -> None:
    method = operation_method("briosa.InstrumentOperations", "LocateInstrumentsUsmn")
    response = populated(instrument_operations_pb2.LocateInstrumentsUsmnResult)

    with pytest.raises(BriosaProtocolError, match="operation-result-field-drift"):
        map_response(method, response, DriftedFitResult)


def mismatches(value: object, annotation: object, path: str = "value") -> list[str]:
    """Return where a mapped value differs from its public annotation."""
    origin = typing.get_origin(annotation)
    arguments = typing.get_args(annotation)
    if annotation is typing.Any:
        return []
    if annotation is None or annotation is type(None):
        return [] if value is None else [f"{path}: {value!r} is not None"]
    if origin in (types.UnionType, typing.Union):
        if any(not mismatches(value, option, path) for option in arguments):
            return []
        return [f"{path}: {type(value).__name__} matches no part of {annotation}"]
    if origin in (list, tuple, collections.abc.Sequence):
        if not isinstance(value, list | tuple):
            return [f"{path}: {type(value).__name__} is not a sequence"]
        return [
            problem
            for index, item in enumerate(value)
            for problem in mismatches(item, arguments[0], f"{path}[{index}]")
        ]
    if annotation in (int, float):
        number = isinstance(value, int | float) and not isinstance(value, bool)
        if number and (annotation is float or isinstance(value, int)):
            return []
        return [f"{path}: {type(value).__name__} is not {annotation}"]
    if not isinstance(annotation, type):
        return [f"{path}: unsupported annotation {annotation!r}"]
    if not isinstance(value, annotation):
        return [f"{path}: {type(value).__name__} is not {annotation.__name__}"]
    if not dataclasses.is_dataclass(annotation):
        return []
    hints = typing.get_type_hints(annotation)
    return [
        problem
        for item in dataclasses.fields(annotation)
        for problem in mismatches(
            getattr(value, item.name), hints[item.name], f"{path}.{item.name}"
        )
    ]


async def test_every_facade_returns_what_its_annotation_says() -> None:
    transport = RecordingTransport()
    transport.default_response = lambda _path, response_type: populated(response_type)
    client = await started_client(transport)
    functions = facade_functions()
    problems: dict[str, list[str]] = {}

    for operation_id, facade in bound_facades(client).items():
        function = functions[operation_id]
        result = await facade(**required_arguments(function))
        found = mismatches(result, typing.get_type_hints(function)["return"])
        if found:
            problems[operation_id] = found

    assert problems == {}
    await client.aclose()


@pytest.mark.parametrize(
    ("rpc", "operation_id"),
    [
        (
            "GetRelationshipRefListVariable",
            "variables.get_relationship_ref_list_variable",
        ),
        (
            "GetReportItemsReferenceListVariable",
            "variables.get_report_items_reference_list_variable",
        ),
    ],
)
async def test_the_ref_list_getters_return_collection_item_names(
    rpc: str, operation_id: str
) -> None:
    function = facade_functions()[operation_id]
    assert typing.get_type_hints(function)["return"] == list[CollectionItemName]
    reply = typing.cast(
        typing.Any, getattr(variables_pb2, f"{rpc}Result")(execution=succeeded())
    )
    reply.value.add(
        collection_name="Inspection",
        item_name="Hole Fit",
        item_type=spatial_analyzer_values_pb2.ITEM_TYPE_RELATIONSHIP,
    )
    transport = RecordingTransport()
    transport.queue(f"/briosa.Variables/{rpc}", reply)
    client = await started_client(transport)

    values = await bound_facades(client)[operation_id](name="Relationships")

    assert values == [
        CollectionItemName(
            collection_name="Inspection",
            item_name="Hole Fit",
            item_type=ItemType.RELATIONSHIP,
        )
    ]
    await client.aclose()
