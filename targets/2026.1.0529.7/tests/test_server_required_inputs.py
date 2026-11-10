"""Inputs the server requires are required, with no fill-ins (C2, C3).

The major-3 client consistency rules make every input the server requires on
either target required in the public API: anything the server passes through a
Required* mapper, and anything an explicit check rejects when it is absent or
empty. The client never fills one in (no identity transform, no default
settings value, no empty list, no default choice), so omitting one fails before
any call. The table comes from the audit of every optional parameter and option
member against the server mappers at briosa 2960705e.
"""

from __future__ import annotations

import dataclasses
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

from briosa import (
    EmbeddedReportFile,
    FilterProximitySettings,
    MakeGdtDatumAnnotationOptions,
    MakeGdtFeatureCheckAnnotationOptions,
    RelationshipWatchWindowTemplateOptions,
    ReportOutputOptions,
    ReportOutputType,
    robot_operations_pb2,
)
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET

# C2: the robot parameter name, like its value.
ROBOT_PARAMETER = ("robot_operations.set_robot_machine_parameter", "parameter_name")

# C3: every facade input the server requires on either target.
SERVER_REQUIRED = [
    ROBOT_PARAMETER,
    ("construction_operations.construct_cross_section_cloud", "reference_object"),
    ("construction_operations.construct_ellipsoid", "transform_in_working_coordinates"),
    ("construction_operations.construct_frame", "transform_in_working_coordinates"),
    (
        "construction_operations.construct_frame_from_transform_in_world",
        "transform_in_world_coordinates",
    ),
    (
        "construction_operations.construct_point_from_cloud_point_runtime_select",
        "constructed_point_name",
    ),
    (
        "construction_operations.construct_points_from_surfaces_on_uv_grid",
        "edge_point_mode",
    ),
    (
        "construction_operations.construct_points_shifted_in_working_frame",
        "shift_vector",
    ),
    (
        "construction_operations.construct_points_subset_with_greatest_spacing",
        "group_for_subset",
    ),
    ("construction_operations.create_point_callout", "desired_coordinate_system"),
    (
        "construction_operations.get_gradient_at_projected_point_on_surface_edge",
        "edge_offset_direction",
    ),
    (
        "construction_operations.make_collection_item_name_ref_list_wildcard_selection",
        "item_type",
    ),
    (
        "construction_operations.make_collection_object_name_ref_list_by_type",
        "object_type",
    ),
    (
        "construction_operations.make_collection_object_name_ref_list_by_type_and_color",
        "object_type",
    ),
    (
        "construction_operations.make_collection_object_name_ref_list_runtime_select",
        "object_type",
    ),
    (
        "construction_operations.make_collection_object_name_ref_list_wildcard_selection",
        "object_type",
    ),
    (
        "construction_operations.make_collection_object_name_runtime_select",
        "object_type",
    ),
    ("file_operations.export_qdas_characteristics", "k0004_date_time_stamp"),
    ("file_operations.prepare_qdas_data_list", "k0004_date_time_stamp"),
    ("gdt_operations.enable_disable_datum_alignment_for_feature_check", "alignment"),
    ("gdt_operations.feature_inspection_auto_filter", "offset_direction"),
    ("gdt_operations.set_gdt_options", "distance_between_mode"),
    ("gdt_operations.set_gdt_options", "evaluation_method"),
    (
        "instrument_operations.auto_correspond_with_proximity_trigger",
        "deviation_vector_group_name",
    ),
    ("instrument_operations.build_target", "tolerance"),
    ("instrument_operations.calculate_tcp_fixture_uncertainties", "tcp_in_working"),
    ("instrument_operations.collimation", "as_measured_by_moving_instrument"),
    ("instrument_operations.collimation", "baseline_method"),
    ("instrument_operations.collimation", "not_measured_by_moving_instrument"),
    ("instrument_operations.collimation", "scale_point_1"),
    ("instrument_operations.collimation", "scale_point_2"),
    ("instrument_operations.collimation", "tilt_mode"),
    ("instrument_operations.locate_instruments_usmn", "show_usmn_dialog"),
    (
        "instrument_operations.set_observation_collimation_shot_options",
        "targeted_instrument",
    ),
    ("instrument_operations.set_target_computation_options", "computation_method"),
    (
        "relationship_operations.auto_filter_clouds_to_nominal_geometry_2d",
        "filter_proximity_settings_2d",
    ),
    (
        "relationship_operations.auto_filter_clouds_to_nominal_geometry_3d",
        "filter_proximity_settings_3d",
    ),
    (
        "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
        "clouds",
    ),
    (
        "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
        "groups",
    ),
    (
        "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
        "offset_direction",
    ),
    (
        "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
        "points",
    ),
    (
        "relationship_operations.auto_filter_points_to_nominal_geometry_3d",
        "filter_proximity_settings_3d",
    ),
    ("relationship_operations.create_points_to_objects_map", "groups"),
    ("relationship_operations.create_points_to_objects_map", "points"),
    ("relationship_operations.do_relationship_fit", "motion_to_allow"),
    ("relationship_operations.extract_geometry_from_point_clouds", "bounding_points"),
    ("relationship_operations.extract_geometry_from_point_clouds", "geometry_type"),
    ("relationship_operations.make_dynamic_circle_relationship", "construction_mode"),
    ("relationship_operations.make_dynamic_ellipse_relationship", "construction_mode"),
    ("relationship_operations.make_dynamic_line_relationship", "construction_mode"),
    ("relationship_operations.make_dynamic_plane_relationship", "construction_mode"),
    ("relationship_operations.make_dynamic_point_relationship", "construction_mode"),
    (
        "relationship_operations.make_dynamic_point_relationship",
        "third_reference_geometry",
    ),
    (
        "relationship_operations.make_frame_to_frame_relationship",
        "orientation_tolerance",
    ),
    ("relationship_operations.make_frame_to_frame_relationship", "position_tolerance"),
    (
        "relationship_operations.make_groups_to_objects_relationship",
        "projection_options",
    ),
    (
        "relationship_operations.make_point_clouds_to_objects_relationship",
        "projection_options",
    ),
    (
        "relationship_operations.make_points_to_objects_relationship",
        "projection_options",
    ),
    (
        "relationship_operations.move_collections_by_minimizing_relationships",
        "motion_to_allow",
    ),
    ("relationship_operations.relationship_watch_window_template", "options"),
    (
        "relationship_operations.relationship_watch_window_template",
        "watch_window_template_name",
    ),
    (
        "relationship_operations.set_object_to_object_direction_relationship_tolerances",
        "angle_between_vectors_tolerances",
    ),
    (
        "relationship_operations.set_object_to_object_direction_relationship_tolerances",
        "mutual_perpendicular_length_tolerances",
    ),
    (
        "relationship_operations.set_points_to_points_relationship_associated_data",
        "actual_points",
    ),
    (
        "relationship_operations.set_points_to_points_relationship_associated_data",
        "nominal_points",
    ),
    ("relationship_operations.set_relationship_associated_data", "individual_points"),
    ("relationship_operations.set_relationship_associated_data", "objects"),
    ("relationship_operations.set_relationship_associated_data", "point_clouds"),
    ("relationship_operations.set_relationship_associated_data", "point_groups"),
    (
        "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_offset_transform",
        "measurement_offset_transform",
    ),
    (
        "robot_operations.set_robot_calibration_measurement_offset_in_tool_frame",
        "measurement_frame",
    ),
    ("robot_operations.set_robot_calibration_tool_frame", "tool_frame"),
    ("robot_operations.set_robot_machine_base_transform", "destination_transform"),
]

# Operations that exist on one target only.
TARGET_ONLY = {
    "relationship_operations.extract_geometry_from_point_clouds": "2026.1.0529.7",
}

# The maintainer's decision of 2026-11-09: every FilterProximitySettings member
# is required. The server reads the six distances and two Booleans without
# checking presence, so an absent one would reach SA as 0 or false, and a
# default distance would mean a different length in each job's units.
PROXIMITY_MEMBERS = (
    "surface_inclusion_proximity",
    "edge_exclusion_proximity",
    "planar_inclusion_proximity",
    "planar_exclusion_proximity",
    "radial_inclusion_proximity",
    "geometry_extraction_tolerance",
    "project_to_plane",
    "assert_plane_boundaries",
)

# C3: option members the server requires whenever their value is sent, and the
# proximity members above.
SERVER_REQUIRED_MEMBERS = [
    (FilterProximitySettings, "surface_proximity_mode"),
    (FilterProximitySettings, "planar_proximity_mode"),
    (FilterProximitySettings, "radial_proximity_mode"),
    *((FilterProximitySettings, name) for name in PROXIMITY_MEMBERS),
    (RelationshipWatchWindowTemplateOptions, "udp_network_transmit_settings"),
    *(
        (options, name)
        for options in (
            MakeGdtDatumAnnotationOptions,
            MakeGdtFeatureCheckAnnotationOptions,
        )
        for name in (
            "objects",
            "geometry_relationships",
            "auxiliary_object",
            "auxiliary_geometry_relationship",
        )
    ),
]


def facade_for(operation_id: str) -> typing.Callable[..., typing.Any]:
    functions = facade_functions()
    owner = TARGET_ONLY.get(operation_id)
    if owner is not None and owner != SPATIAL_ANALYZER_TARGET:
        assert operation_id not in functions
        pytest.skip(f"{operation_id} exists only on {owner}")
    return functions[operation_id]


@pytest.mark.parametrize(("operation_id", "name"), SERVER_REQUIRED)
async def test_a_server_required_input_has_no_default_and_fails_before_any_call(
    operation_id: str, name: str
) -> None:
    function = facade_for(operation_id)
    declared = inspect.signature(function).parameters[name]
    assert declared.default is inspect.Parameter.empty
    assert type(None) not in typing.get_args(typing.get_type_hints(function)[name])
    transport = rejecting_transport()
    client = await started_client(transport)
    facade = bound_facades(client)[operation_id]
    arguments = required_arguments(function)

    with pytest.raises(TypeError):
        await facade(**{key: value for key, value in arguments.items() if key != name})
    assert transport.requests == []
    await sent(transport, facade, **arguments)
    await client.aclose()


async def test_an_explicit_robot_parameter_name_is_sent_unchanged() -> None:
    operation_id, name = ROBOT_PARAMETER
    transport = rejecting_transport()
    client = await started_client(transport)
    facade = bound_facades(client)[operation_id]
    arguments = {**required_arguments(facade_functions()[operation_id]), name: ""}

    request = await sent(transport, facade, **arguments)

    message = typing.cast(robot_operations_pb2.SetRobotMachineParameterRequest, request)
    assert message.parameter_name == ""
    await client.aclose()


@pytest.mark.parametrize(
    ("value_type", "name"),
    SERVER_REQUIRED_MEMBERS,
    ids=[
        f"{value_type.__name__}.{name}" for value_type, name in SERVER_REQUIRED_MEMBERS
    ],
)
def test_a_server_required_member_has_no_default(
    value_type: type[typing.Any], name: str
) -> None:
    member = {item.name: item for item in dataclasses.fields(value_type)}[name]
    assert member.default is dataclasses.MISSING
    assert member.default_factory is dataclasses.MISSING
    hints = typing.get_type_hints(value_type)
    assert type(None) not in typing.get_args(hints[name])
    arguments = {
        item.name: argument(hints[item.name])
        for item in dataclasses.fields(value_type)
        if item.default is dataclasses.MISSING
        and item.default_factory is dataclasses.MISSING
    }

    with pytest.raises(TypeError):
        value_type(**{key: value for key, value in arguments.items() if key != name})
    value_type(**arguments)


def test_every_proximity_member_is_required() -> None:
    fields = {item.name for item in dataclasses.fields(FilterProximitySettings)}
    required = {
        name
        for value_type, name in SERVER_REQUIRED_MEMBERS
        if value_type is FilterProximitySettings
    }
    assert required == fields
    assert len(fields) == 11


def test_report_output_options_need_exactly_one_destination() -> None:
    with pytest.raises(ValueError):
        ReportOutputOptions(output_type=ReportOutputType.SA_REPORT)
    with pytest.raises(ValueError):
        ReportOutputOptions(
            output_type=ReportOutputType.SA_REPORT,
            external_path=r"C:\Reports\a.pdf",
            embedded_file=EmbeddedReportFile(collection_name="", file_name="My Report"),
        )
    assert ReportOutputOptions.DEFAULT.embedded_file is not None
    ReportOutputOptions(
        output_type=ReportOutputType.SA_REPORT, external_path=r"C:\Reports\a.pdf"
    )
