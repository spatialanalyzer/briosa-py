"""Optional and server-required list inputs (#44, freeze plan 8.7)."""

from __future__ import annotations

import inspect
import typing
from typing import cast

import pytest
from facade_support import (
    argument,
    bound_facades,
    facade_functions,
    rejecting_transport,
    required_arguments,
    sent,
    started_client,
)

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
