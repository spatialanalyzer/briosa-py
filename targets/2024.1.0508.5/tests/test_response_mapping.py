"""Every operation maps a fully populated response (#45, freeze plan 8.8)."""

from __future__ import annotations

import dataclasses
import typing

import pytest
from facade_support import (
    RecordingTransport,
    bound_facades,
    facade_functions,
    populated,
    required_arguments,
    started_client,
)
from test_operation_surface import protocol_methods

from briosa import (
    BriosaProtocolError,
    CollectionInstrumentId,
    CollectionObjectName,
    FitErrorResult,
    MpCompletion,
    MpExecutionState,
    ObjectType,
    instrument_operations_pb2,
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
