"""Request defaults and D2 argument rules at contract major 3 (freeze plan 8.4)."""

from __future__ import annotations

import inspect
import typing

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

from briosa import RobotModelLinkConfiguration, ToleranceLimit, ToleranceVectorOptions

# Reviewed fixed defaults that major 3 flips (#297): the old values make the
# server deny the request, so the facades send the new value explicitly.
FLIPPED_DEFAULTS = [
    ("instrument_operations.measure_single_point_here", "measure_immediately", True),
    ("instrument_operations.configure_and_measure", "measure_immediately", True),
    (
        "instrument_operations.measure_existing_single_point",
        "measure_immediately",
        True,
    ),
    (
        "instrument_operations.measure_existing_single_point_and_compare",
        "measure_immediately",
        True,
    ),
    (
        "instrument_operations.measure_existing_single_point_manual_guide",
        "measure_immediately",
        True,
    ),
    ("instrument_operations.auto_measure_points", "auto_start", True),
    (
        "instrument_operations.auto_measure_specified_geometry",
        "wait_for_complete",
        True,
    ),
    ("robot_operations.move_robot_machine_to_frame", "acknowledge_arrival", True),
    (
        "robot_operations.move_robot_machine_to_named_destination",
        "acknowledge_arrival",
        True,
    ),
    ("file_operations.direct_cad_access", "prompt_on_missing_components", False),
]

# D2 rule 2 (#325) and the fit seed (#357): optional with no default value;
# an omitted argument leaves the field unset. The USMN nominals group and the
# bounding plane names were already optional and stay that way.
OMITTED_UNSET = [
    ("reporting_operations.create_chart_from_vector_group", "template_chart_name"),
    ("utility_operations.set_user_interface_profile", "profile_file_name"),
    ("analysis_operations.fit_geometry_to_point_group", "starting_condition_geometry"),
    ("analysis_operations.fit_geometry_to_points", "starting_condition_geometry"),
    (
        "analysis_operations.fit_geometry_to_point_group_projected_to_plane",
        "starting_condition_geometry",
    ),
    ("instrument_operations.locate_instruments_usmn", "nominals_group"),
    (
        "construction_operations.construct_planes_bounding_point_group",
        "resulting_high_plane_name",
    ),
    (
        "construction_operations.construct_planes_bounding_point_group",
        "resulting_low_plane_name",
    ),
    ("instrument_operations.set_instrument_weather_setting", "temperature"),
    ("instrument_operations.set_instrument_weather_setting", "pressure"),
    ("instrument_operations.set_instrument_weather_setting", "relative_humidity"),
]

RELATIONSHIPS = [
    "relationship_operations.make_group_to_group_relationship",
    "relationship_operations.make_group_to_nominal_group_relationship",
    "relationship_operations.make_point_to_point_relationship",
    "relationship_operations.make_points_to_points_relationship",
]

# D2 rule 4 (relationship tolerance and constraint, Q4) and rule 6 (R1 to R7,
# Q6): required, with no default. Omitting one fails before any call.
REQUIRED = [
    *((operation, "tolerance") for operation in RELATIONSHIPS),
    *((operation, "constraint") for operation in RELATIONSHIPS),
    *(
        ("robot_operations.move_robot_machine_to_joint_pose_six_dof", f"joint_{index}")
        for index in range(1, 7)
    ),
    ("instrument_operations.set_instrument_weather_setting", "set_automatically"),
    ("utility_operations.scale_objects", "scale_factor"),
    ("instrument_operations.set_absolute_instrument_scale_factor", "scale_factor"),
    ("instrument_operations.set_multiply_instrument_scale_factor", "scale_factor"),
    ("robot_operations.set_robot_machine_model_link_parameters", "configuration"),
    ("robot_operations.set_robot_machine_parameter", "parameter_value"),
    ("instrument_operations.delete_measurement_observation", "observation_index"),
    ("instrument_operations.move_measurement_observation", "observation_index"),
    ("vector_operations.delete_ith_vector_from_vector_group", "vector_index"),
    ("utility_operations.delete_folder", "folder_path"),
    ("variables.delete_variable", "name"),
    ("variables.delete_variables_wildcard_match", "variable_wildcard_criteria"),
    ("vector_operations.delete_vector_by_name", "vector_name"),
    ("construction_operations.delete_collections_by_wildcard", "search_string"),
    ("construction_operations.delete_folders_by_wildcard", "search_string"),
    ("robot_operations.delete_robot_calibration", "calibration_name"),
    ("reporting_operations.remove_report_tag", "tag_name"),
]


def parameter(operation_id: str, name: str) -> inspect.Parameter:
    return inspect.signature(facade_functions()[operation_id]).parameters[name]


@pytest.mark.parametrize(("operation_id", "name", "value"), FLIPPED_DEFAULTS)
async def test_a_flipped_default_is_sent_explicitly(
    operation_id: str, name: str, value: bool
) -> None:
    assert parameter(operation_id, name).default is value
    transport = rejecting_transport()
    client = await started_client(transport)
    facade = bound_facades(client)[operation_id]
    arguments = required_arguments(facade_functions()[operation_id])

    default_call = await sent(transport, facade, **arguments)
    explicit_call = await sent(transport, facade, **arguments, **{name: not value})

    assert default_call.HasField(name)
    assert getattr(default_call, name) is value
    assert explicit_call.HasField(name)
    assert getattr(explicit_call, name) is (not value)
    await client.aclose()


@pytest.mark.parametrize(("operation_id", "name"), OMITTED_UNSET)
async def test_an_omitted_optional_argument_leaves_its_field_unset(
    operation_id: str, name: str
) -> None:
    declared = parameter(operation_id, name)
    assert declared.kind is inspect.Parameter.KEYWORD_ONLY
    assert declared.default is None
    transport = rejecting_transport()
    client = await started_client(transport)
    function = facade_functions()[operation_id]
    facade = bound_facades(client)[operation_id]
    arguments = required_arguments(function)

    omitted = await sent(transport, facade, **arguments)
    supplied_value = argument(typing.get_type_hints(function)[name])
    supplied = await sent(transport, facade, **arguments, **{name: supplied_value})

    assert not omitted.HasField(name)
    assert supplied.HasField(name)
    await client.aclose()


@pytest.mark.parametrize("set_automatically", [False, True])
async def test_weather_values_stay_unset_whatever_set_automatically_is(
    set_automatically: bool,
) -> None:
    operation_id = "instrument_operations.set_instrument_weather_setting"
    transport = rejecting_transport()
    client = await started_client(transport)
    facade = bound_facades(client)[operation_id]
    arguments = {
        **required_arguments(facade_functions()[operation_id]),
        "set_automatically": set_automatically,
    }

    request = await sent(transport, facade, **arguments)

    assert request.HasField("set_automatically")
    assert typing.cast(typing.Any, request).set_automatically is set_automatically
    for name in ("temperature", "pressure", "relative_humidity"):
        assert not request.HasField(name)
    await client.aclose()


@pytest.mark.parametrize(("operation_id", "name"), REQUIRED)
async def test_a_required_argument_has_no_default_and_fails_before_any_call(
    operation_id: str, name: str
) -> None:
    declared = parameter(operation_id, name)
    assert declared.default is inspect.Parameter.empty
    assert "None" not in str(declared.annotation)
    transport = rejecting_transport()
    client = await started_client(transport)
    function = facade_functions()[operation_id]
    facade = bound_facades(client)[operation_id]
    arguments = required_arguments(function)

    with pytest.raises(TypeError):
        await facade(**{key: value for key, value in arguments.items() if key != name})
    assert transport.requests == []
    await sent(transport, facade, **arguments)
    await client.aclose()


@pytest.mark.parametrize("operation_id", RELATIONSHIPS)
async def test_relationship_limits_are_sent_only_as_the_caller_passes_them(
    operation_id: str,
) -> None:
    transport = rejecting_transport()
    client = await started_client(transport)
    facade = bound_facades(client)[operation_id]
    arguments = required_arguments(facade_functions()[operation_id])
    tolerance = ToleranceVectorOptions(high_x=ToleranceLimit(enabled=True, value=0.5))

    request = typing.cast(
        typing.Any,
        await sent(
            transport,
            facade,
            **{
                **arguments,
                "tolerance": tolerance,
                "constraint": ToleranceVectorOptions.NO_LIMITS,
            },
        ),
    )

    assert request.tolerance.high_x.enabled is True
    assert request.tolerance.high_x.value == 0.5
    assert request.HasField("constraint")
    assert not any(
        getattr(request.constraint, limit).enabled
        for limit in (
            "high_x",
            "high_y",
            "high_z",
            "high_magnitude",
            "low_x",
            "low_y",
            "low_z",
            "low_magnitude",
        )
    )
    await client.aclose()


def test_the_named_no_limits_value_disables_every_limit() -> None:
    assert ToleranceVectorOptions() == ToleranceVectorOptions.NO_LIMITS
    assert ToleranceVectorOptions.NO_LIMITS.high_magnitude == ToleranceLimit()


def test_the_model_link_configuration_has_no_member_defaults() -> None:
    with pytest.raises(TypeError):
        RobotModelLinkConfiguration()  # type: ignore[call-arg]
    required = [
        item
        for item in inspect.signature(RobotModelLinkConfiguration).parameters.values()
        if item.default is inspect.Parameter.empty
    ]
    assert len(required) == len(
        inspect.signature(RobotModelLinkConfiguration).parameters
    )
