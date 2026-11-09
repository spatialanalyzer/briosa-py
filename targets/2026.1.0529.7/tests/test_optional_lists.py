"""Optional and server-required list inputs (#44, freeze plan 8.7)."""

from __future__ import annotations

import inspect
import typing
from typing import cast

import grpc
import pytest
from facade_support import (
    FakeRpcError,
    RecordingTransport,
    argument,
    bound_facades,
    facade_functions,
    required_arguments,
    started_client,
)
from google.protobuf.message import Message

from briosa import BriosaOperationError, operation_outcomes_pb2

# Optional lists that map to plain repeated fields. An omitted list, or None,
# is sent as an empty repeated field, which is the absent value on the wire.
OPTIONAL_LISTS = {
    "construction_operations.create_point_callout": ("notes",),
    "construction_operations.create_point_comparison_callout": ("additional_notes",),
    "construction_operations.create_relationship_callout": ("additional_notes",),
    "construction_operations.create_vector_callout": ("additional_notes",),
    "instrument_operations.quick_align": (
        "nominal_points",
        "nominal_point_of_view_names",
    ),
    # The server skips the USMN setter for an empty list (licensed session 3).
    "instrument_operations.locate_instruments_usmn": ("excluded_groups",),
}

# Lists the server rejects when empty. They are required, with no default.
REQUIRED_LISTS = {
    "gdt_operations.feature_inspection_auto_filter": (
        "point_names",
        "group_names",
        "cloud_names",
        "feature_check_name_list",
    ),
    "instrument_operations.locate_instrument_group_to_surface_quick_fit": (
        "other_objects_to_transform",
    ),
}


def rejecting_transport() -> RecordingTransport:
    """Record each request, then fail it as an MP failure after dispatch."""
    transport = RecordingTransport()
    detail = operation_outcomes_pb2.OperationError(
        operation_id="request-shape-test",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_MP_FAILURE,
        diagnostic_code="mp-failed",
    )

    def reject(_path: str, _response_type: type[Message]) -> Message:
        raise FakeRpcError(
            grpc.StatusCode.FAILED_PRECONDITION,
            (("briosa-operation-error-bin", detail.SerializeToString()),),
        )

    transport.default_response = reject
    return transport


async def sent(
    transport: RecordingTransport, facade: typing.Any, **arguments: object
) -> Message:
    count = len(transport.requests)
    with pytest.raises(BriosaOperationError):
        await facade(**arguments)
    assert len(transport.requests) == count + 1
    return transport.requests[-1][1]


@pytest.mark.parametrize(
    ("operation_id", "names"), OPTIONAL_LISTS.items(), ids=list(OPTIONAL_LISTS)
)
async def test_an_omitted_optional_list_is_sent_empty(
    operation_id: str, names: tuple[str, ...]
) -> None:
    transport = rejecting_transport()
    client = await started_client(transport)
    function = facade_functions()[operation_id]
    facade = bound_facades(client)[operation_id]
    for name in names:
        assert inspect.signature(function).parameters[name].default is not (
            inspect.Parameter.empty
        )

    omitted = await sent(transport, facade, **required_arguments(function))
    for name in names:
        assert list(getattr(omitted, name)) == []

    if all(
        inspect.signature(function).parameters[name].default is None for name in names
    ):
        explicit_none = await sent(
            transport, facade, **required_arguments(function), **dict.fromkeys(names)
        )
        for name in names:
            assert list(getattr(explicit_none, name)) == []
    await client.aclose()


@pytest.mark.parametrize(
    ("operation_id", "names"), OPTIONAL_LISTS.items(), ids=list(OPTIONAL_LISTS)
)
async def test_a_supplied_optional_list_is_sent_unchanged(
    operation_id: str, names: tuple[str, ...]
) -> None:
    transport = rejecting_transport()
    client = await started_client(transport)
    function = facade_functions()[operation_id]
    hints = typing.get_type_hints(function)
    supplied = {name: cast(list[object], argument(hints[name])) * 2 for name in names}

    request = await sent(
        transport,
        bound_facades(client)[operation_id],
        **required_arguments(function),
        **supplied,
    )
    for name in names:
        assert len(getattr(request, name)) == 2
    await client.aclose()


@pytest.mark.parametrize(
    ("operation_id", "names"), REQUIRED_LISTS.items(), ids=list(REQUIRED_LISTS)
)
async def test_a_list_the_server_requires_is_required_before_any_call(
    operation_id: str, names: tuple[str, ...]
) -> None:
    transport = rejecting_transport()
    client = await started_client(transport)
    function = facade_functions()[operation_id]
    facade = bound_facades(client)[operation_id]
    parameters = inspect.signature(function).parameters
    for name in names:
        assert parameters[name].default is inspect.Parameter.empty, name
        assert "None" not in str(parameters[name].annotation), name

    arguments = required_arguments(function)
    for name in names:
        omitted = {key: value for key, value in arguments.items() if key != name}
        with pytest.raises(TypeError):
            await facade(**omitted)
        with pytest.raises(TypeError):
            await facade(**{**arguments, name: None})
    assert transport.requests == []

    request = await sent(transport, facade, **arguments)
    for name in names:
        assert len(getattr(request, name)) == 1
    await client.aclose()
