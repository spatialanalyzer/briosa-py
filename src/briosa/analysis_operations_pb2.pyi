from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AngleBetweenLineAndPlaneRequest(_message.Message):
    __slots__ = ("selected_line", "selected_plane", "nominal_angle", "angle_tolerance_0_0_for_none")
    SELECTED_LINE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_PLANE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    selected_line: _spatial_analyzer_values_pb2.CollectionObjectName
    selected_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    nominal_angle: float
    angle_tolerance_0_0_for_none: float
    def __init__(self, selected_line: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., selected_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., nominal_angle: _Optional[float] = ..., angle_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class AngleBetweenLineAndPlaneResult(_message.Message):
    __slots__ = ("angle", "execution")
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    angle: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, angle: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AngleBetweenTwoLinesRequest(_message.Message):
    __slots__ = ("line_1", "line_2", "nominal_angle", "angle_tolerance_0_0_for_none")
    LINE_1_FIELD_NUMBER: _ClassVar[int]
    LINE_2_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    line_1: _spatial_analyzer_values_pb2.CollectionObjectName
    line_2: _spatial_analyzer_values_pb2.CollectionObjectName
    nominal_angle: float
    angle_tolerance_0_0_for_none: float
    def __init__(self, line_1: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., line_2: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., nominal_angle: _Optional[float] = ..., angle_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class AngleBetweenTwoLinesResult(_message.Message):
    __slots__ = ("angle", "execution")
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    angle: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, angle: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AngleBetweenTwoPlanesNormalsRequest(_message.Message):
    __slots__ = ("plane_a", "plane_b", "nominal_angle", "angle_tolerance_0_0_for_none")
    PLANE_A_FIELD_NUMBER: _ClassVar[int]
    PLANE_B_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    plane_a: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_b: _spatial_analyzer_values_pb2.CollectionObjectName
    nominal_angle: float
    angle_tolerance_0_0_for_none: float
    def __init__(self, plane_a: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_b: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., nominal_angle: _Optional[float] = ..., angle_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class AngleBetweenTwoPlanesNormalsResult(_message.Message):
    __slots__ = ("angle", "execution")
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    angle: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, angle: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class BestFitTransformationGroupToGroupRequest(_message.Message):
    __slots__ = ("reference_group", "corresponding_group", "show_interface", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none", "allow_scale", "allow_x", "allow_y", "allow_z", "allow_rx", "allow_ry", "allow_rz", "lock_degrees_of_freedom", "generate_event", "file_path_for_csv_text_report_requires_show_interface_true")
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCALE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_X_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Y_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Z_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RZ_FIELD_NUMBER: _ClassVar[int]
    LOCK_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    GENERATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FOR_CSV_TEXT_REPORT_REQUIRES_SHOW_INTERFACE_TRUE_FIELD_NUMBER: _ClassVar[int]
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    corresponding_group: _spatial_analyzer_values_pb2.CollectionObjectName
    show_interface: bool
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    allow_scale: bool
    allow_x: bool
    allow_y: bool
    allow_z: bool
    allow_rx: bool
    allow_ry: bool
    allow_rz: bool
    lock_degrees_of_freedom: bool
    generate_event: bool
    file_path_for_csv_text_report_requires_show_interface_true: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., corresponding_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., show_interface: bool = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ..., allow_scale: bool = ..., allow_x: bool = ..., allow_y: bool = ..., allow_z: bool = ..., allow_rx: bool = ..., allow_ry: bool = ..., allow_rz: bool = ..., lock_degrees_of_freedom: bool = ..., generate_event: bool = ..., file_path_for_csv_text_report_requires_show_interface_true: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class BestFitTransformationGroupToGroupResult(_message.Message):
    __slots__ = ("transform_in_working", "optimum_transform", "rms_deviation", "maximum_absolute_deviation", "number_of_unknowns", "number_of_equations", "robustness", "execution")
    TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    OPTIMUM_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_UNKNOWNS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_EQUATIONS_FIELD_NUMBER: _ClassVar[int]
    ROBUSTNESS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform_in_working: _spatial_analyzer_values_pb2.Transform
    optimum_transform: _spatial_analyzer_values_pb2.WorldTransform
    rms_deviation: float
    maximum_absolute_deviation: float
    number_of_unknowns: int
    number_of_equations: int
    robustness: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., optimum_transform: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., rms_deviation: _Optional[float] = ..., maximum_absolute_deviation: _Optional[float] = ..., number_of_unknowns: _Optional[int] = ..., number_of_equations: _Optional[int] = ..., robustness: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ComputeGroupToGroupOrientationRxRyRzRequest(_message.Message):
    __slots__ = ("reference_group", "corresponding_group")
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_GROUP_FIELD_NUMBER: _ClassVar[int]
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    corresponding_group: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., corresponding_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ComputeGroupToGroupOrientationRxRyRzResult(_message.Message):
    __slots__ = ("rx", "ry", "rz", "execution")
    RX_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rx: float
    ry: float
    rz: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rx: _Optional[float] = ..., ry: _Optional[float] = ..., rz: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePointUncertaintyCloudPointSetsRequest(_message.Message):
    __slots__ = ("point_name_list", "number_of_samples", "uncertainty_reference_frame_mode", "grouping_mode", "point_set_mode")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTY_REFERENCE_FRAME_MODE_FIELD_NUMBER: _ClassVar[int]
    GROUPING_MODE_FIELD_NUMBER: _ClassVar[int]
    POINT_SET_MODE_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    number_of_samples: int
    uncertainty_reference_frame_mode: str
    grouping_mode: str
    point_set_mode: str
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., number_of_samples: _Optional[int] = ..., uncertainty_reference_frame_mode: _Optional[str] = ..., grouping_mode: _Optional[str] = ..., point_set_mode: _Optional[str] = ...) -> None: ...

class CreatePointUncertaintyCloudPointSetsResult(_message.Message):
    __slots__ = ("point_groups", "point_sets", "point_clouds", "execution")
    POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    POINT_SETS_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    point_groups: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_sets: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, point_groups: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_sets: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePointUncertaintyFieldsRequest(_message.Message):
    __slots__ = ("point_name_list", "number_of_samples")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    number_of_samples: int
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., number_of_samples: _Optional[int] = ...) -> None: ...

class CreatePointUncertaintyFieldsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FitGeometryToPointGroupRequest(_message.Message):
    __slots__ = ("geometry_type", "group_to_fit", "resulting_object_name", "fit_profile_name", "report_deviations", "fit_interface_tolerance_1_0_use_profile", "ignore_out_of_tolerance_points", "starting_condition_geometry_optional")
    GEOMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEVIATIONS_FIELD_NUMBER: _ClassVar[int]
    FIT_INTERFACE_TOLERANCE_1_0_USE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_OUT_OF_TOLERANCE_POINTS_FIELD_NUMBER: _ClassVar[int]
    STARTING_CONDITION_GEOMETRY_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    geometry_type: _spatial_analyzer_values_pb2.GeometryType
    group_to_fit: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_profile_name: str
    report_deviations: bool
    fit_interface_tolerance_1_0_use_profile: float
    ignore_out_of_tolerance_points: bool
    starting_condition_geometry_optional: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, geometry_type: _Optional[_Union[_spatial_analyzer_values_pb2.GeometryType, str]] = ..., group_to_fit: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_profile_name: _Optional[str] = ..., report_deviations: bool = ..., fit_interface_tolerance_1_0_use_profile: _Optional[float] = ..., ignore_out_of_tolerance_points: bool = ..., starting_condition_geometry_optional: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class FitGeometryToPointGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FitGeometryToPointGroupProjectedToPlaneRequest(_message.Message):
    __slots__ = ("geometry_type", "group_to_fit", "plane_name", "resulting_object_name", "fit_profile_name", "report_deviations", "fit_interface_tolerance_1_0_use_profile", "ignore_out_of_tolerance_points", "starting_condition_geometry_optional")
    GEOMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEVIATIONS_FIELD_NUMBER: _ClassVar[int]
    FIT_INTERFACE_TOLERANCE_1_0_USE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_OUT_OF_TOLERANCE_POINTS_FIELD_NUMBER: _ClassVar[int]
    STARTING_CONDITION_GEOMETRY_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    geometry_type: _spatial_analyzer_values_pb2.GeometryType
    group_to_fit: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_profile_name: str
    report_deviations: bool
    fit_interface_tolerance_1_0_use_profile: float
    ignore_out_of_tolerance_points: bool
    starting_condition_geometry_optional: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, geometry_type: _Optional[_Union[_spatial_analyzer_values_pb2.GeometryType, str]] = ..., group_to_fit: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_profile_name: _Optional[str] = ..., report_deviations: bool = ..., fit_interface_tolerance_1_0_use_profile: _Optional[float] = ..., ignore_out_of_tolerance_points: bool = ..., starting_condition_geometry_optional: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class FitGeometryToPointGroupProjectedToPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FitGeometryToPointsRequest(_message.Message):
    __slots__ = ("geometry_type", "points_to_fit", "resulting_object_name", "fit_profile_name", "report_deviations", "fit_interface_tolerance_1_0_use_profile", "ignore_out_of_tolerance_points", "starting_condition_geometry_optional")
    GEOMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    POINTS_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_DEVIATIONS_FIELD_NUMBER: _ClassVar[int]
    FIT_INTERFACE_TOLERANCE_1_0_USE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_OUT_OF_TOLERANCE_POINTS_FIELD_NUMBER: _ClassVar[int]
    STARTING_CONDITION_GEOMETRY_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    geometry_type: _spatial_analyzer_values_pb2.GeometryType
    points_to_fit: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_profile_name: str
    report_deviations: bool
    fit_interface_tolerance_1_0_use_profile: float
    ignore_out_of_tolerance_points: bool
    starting_condition_geometry_optional: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, geometry_type: _Optional[_Union[_spatial_analyzer_values_pb2.GeometryType, str]] = ..., points_to_fit: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_profile_name: _Optional[str] = ..., report_deviations: bool = ..., fit_interface_tolerance_1_0_use_profile: _Optional[float] = ..., ignore_out_of_tolerance_points: bool = ..., starting_condition_geometry_optional: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class FitGeometryToPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetBSplinePropertiesRequest(_message.Message):
    __slots__ = ("b_spline_name",)
    B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetBSplinePropertiesResult(_message.Message):
    __slots__ = ("degree", "knots", "control_points", "range_min", "range_max", "length", "execution")
    DEGREE_FIELD_NUMBER: _ClassVar[int]
    KNOTS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_POINTS_FIELD_NUMBER: _ClassVar[int]
    RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
    RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    degree: int
    knots: int
    control_points: int
    range_min: float
    range_max: float
    length: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, degree: _Optional[int] = ..., knots: _Optional[int] = ..., control_points: _Optional[int] = ..., range_min: _Optional[float] = ..., range_max: _Optional[float] = ..., length: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCirclePropertiesRequest(_message.Message):
    __slots__ = ("circle_name",)
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetCirclePropertiesResult(_message.Message):
    __slots__ = ("center_coordinate", "normal_direction", "radius", "diameter", "execution")
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    normal_direction: _spatial_analyzer_values_pb2.Vector
    radius: float
    diameter: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., radius: _Optional[float] = ..., diameter: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetConePropertiesRequest(_message.Message):
    __slots__ = ("cone_name",)
    CONE_NAME_FIELD_NUMBER: _ClassVar[int]
    cone_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cone_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetConePropertiesResult(_message.Message):
    __slots__ = ("cone_end_point_in_working_coordinates", "cone_axis_in_working_coordinates", "cone_length", "cone_theta_start", "cone_theta_span", "cone_included_angle", "cut_length_from_apex", "execution")
    CONE_END_POINT_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CONE_AXIS_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CONE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_START_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_SPAN_FIELD_NUMBER: _ClassVar[int]
    CONE_INCLUDED_ANGLE_FIELD_NUMBER: _ClassVar[int]
    CUT_LENGTH_FROM_APEX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    cone_end_point_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    cone_axis_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    cone_length: float
    cone_theta_start: float
    cone_theta_span: float
    cone_included_angle: float
    cut_length_from_apex: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, cone_end_point_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_axis_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_length: _Optional[float] = ..., cone_theta_start: _Optional[float] = ..., cone_theta_span: _Optional[float] = ..., cone_included_angle: _Optional[float] = ..., cut_length_from_apex: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCoordinateForIthPointInPointSetRequest(_message.Message):
    __slots__ = ("point_set", "point_set_index")
    POINT_SET_FIELD_NUMBER: _ClassVar[int]
    POINT_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    point_set: _spatial_analyzer_values_pb2.CollectionObjectName
    point_set_index: int
    def __init__(self, point_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_set_index: _Optional[int] = ...) -> None: ...

class GetCoordinateForIthPointInPointSetResult(_message.Message):
    __slots__ = ("point_name", "point_coordinates", "execution")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    point_name: str
    point_coordinates: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, point_name: _Optional[str] = ..., point_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCylinderPropertiesRequest(_message.Message):
    __slots__ = ("cylinder_name",)
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetCylinderPropertiesResult(_message.Message):
    __slots__ = ("begin_coordinate", "end_coordinate", "axis_direction", "length", "radius", "diameter", "nominals_point_inward", "facets", "enable_theta_extent_display_mode", "theta_start_in_degrees", "theta_span_in_degrees", "execution")
    BEGIN_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    END_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    AXIS_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    NOMINALS_POINT_INWARD_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_THETA_EXTENT_DISPLAY_MODE_FIELD_NUMBER: _ClassVar[int]
    THETA_START_IN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    THETA_SPAN_IN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    begin_coordinate: _spatial_analyzer_values_pb2.Vector
    end_coordinate: _spatial_analyzer_values_pb2.Vector
    axis_direction: _spatial_analyzer_values_pb2.Vector
    length: float
    radius: float
    diameter: float
    nominals_point_inward: bool
    facets: int
    enable_theta_extent_display_mode: bool
    theta_start_in_degrees: float
    theta_span_in_degrees: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, begin_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., axis_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., length: _Optional[float] = ..., radius: _Optional[float] = ..., diameter: _Optional[float] = ..., nominals_point_inward: bool = ..., facets: _Optional[int] = ..., enable_theta_extent_display_mode: bool = ..., theta_start_in_degrees: _Optional[float] = ..., theta_span_in_degrees: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetEllipsePropertiesRequest(_message.Message):
    __slots__ = ("ellipse_name",)
    ELLIPSE_NAME_FIELD_NUMBER: _ClassVar[int]
    ellipse_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, ellipse_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetEllipsePropertiesResult(_message.Message):
    __slots__ = ("center_coordinate", "normal_direction", "major_axis_radius", "minor_axis_radius", "execution")
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MAJOR_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MINOR_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    normal_direction: _spatial_analyzer_values_pb2.Vector
    major_axis_radius: float
    minor_axis_radius: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., major_axis_radius: _Optional[float] = ..., minor_axis_radius: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetEulerParametersForFrameRequest(_message.Message):
    __slots__ = ("frame",)
    FRAME_FIELD_NUMBER: _ClassVar[int]
    frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetEulerParametersForFrameResult(_message.Message):
    __slots__ = ("x", "y", "z", "e1", "e2", "e3", "e4", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    E1_FIELD_NUMBER: _ClassVar[int]
    E2_FIELD_NUMBER: _ClassVar[int]
    E3_FIELD_NUMBER: _ClassVar[int]
    E4_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    e1: float
    e2: float
    e3: float
    e4: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., e1: _Optional[float] = ..., e2: _Optional[float] = ..., e3: _Optional[float] = ..., e4: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetEulerParametersForIthFrameInFrameSetRequest(_message.Message):
    __slots__ = ("frame_set", "frame_set_index")
    FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    frame_set: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_set_index: int
    def __init__(self, frame_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_set_index: _Optional[int] = ...) -> None: ...

class GetEulerParametersForIthFrameInFrameSetResult(_message.Message):
    __slots__ = ("x", "y", "z", "e1", "e2", "e3", "e4", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    E1_FIELD_NUMBER: _ClassVar[int]
    E2_FIELD_NUMBER: _ClassVar[int]
    E3_FIELD_NUMBER: _ClassVar[int]
    E4_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    e1: float
    e2: float
    e3: float
    e4: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., e1: _Optional[float] = ..., e2: _Optional[float] = ..., e3: _Optional[float] = ..., e4: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthCollectionNameRequest(_message.Message):
    __slots__ = ("collection_index",)
    COLLECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    collection_index: int
    def __init__(self, collection_index: _Optional[int] = ...) -> None: ...

class GetIthCollectionNameResult(_message.Message):
    __slots__ = ("resultant_name", "execution")
    RESULTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthPointFromGroupRequest(_message.Message):
    __slots__ = ("group_name", "point_index")
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_INDEX_FIELD_NUMBER: _ClassVar[int]
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_index: int
    def __init__(self, group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_index: _Optional[int] = ...) -> None: ...

class GetIthPointFromGroupResult(_message.Message):
    __slots__ = ("complete_point_name", "point_name_only", "vector_in_working", "execution")
    COMPLETE_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_ONLY_FIELD_NUMBER: _ClassVar[int]
    VECTOR_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    complete_point_name: _spatial_analyzer_values_pb2.PointName
    point_name_only: str
    vector_in_working: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, complete_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., point_name_only: _Optional[str] = ..., vector_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetLinePropertiesRequest(_message.Message):
    __slots__ = ("line_name",)
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetLinePropertiesResult(_message.Message):
    __slots__ = ("begin_coordinate", "end_coordinate", "delta_components", "length", "angle_about_x_from_y_in_yz_plane", "angle_about_y_from_z_in_xz_plane", "angle_about_z_from_x_in_xy_plane", "execution")
    BEGIN_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    END_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    DELTA_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    ANGLE_ABOUT_X_FROM_Y_IN_YZ_PLANE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_ABOUT_Y_FROM_Z_IN_XZ_PLANE_FIELD_NUMBER: _ClassVar[int]
    ANGLE_ABOUT_Z_FROM_X_IN_XY_PLANE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    begin_coordinate: _spatial_analyzer_values_pb2.Vector
    end_coordinate: _spatial_analyzer_values_pb2.Vector
    delta_components: _spatial_analyzer_values_pb2.Vector
    length: float
    angle_about_x_from_y_in_yz_plane: float
    angle_about_y_from_z_in_xz_plane: float
    angle_about_z_from_x_in_xy_plane: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, begin_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., delta_components: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., length: _Optional[float] = ..., angle_about_x_from_y_in_yz_plane: _Optional[float] = ..., angle_about_y_from_z_in_xz_plane: _Optional[float] = ..., angle_about_z_from_x_in_xy_plane: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetMeasurementAuxiliaryDataRequest(_message.Message):
    __slots__ = ("point_name", "auxiliary_name")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    auxiliary_name: str
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., auxiliary_name: _Optional[str] = ...) -> None: ...

class GetMeasurementAuxiliaryDataResult(_message.Message):
    __slots__ = ("value", "units", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    units: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[float] = ..., units: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetMeasurementInfoDataRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetMeasurementInfoDataResult(_message.Message):
    __slots__ = ("info_data", "execution")
    INFO_DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    info_data: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, info_data: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetMeasurementWeatherDataRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetMeasurementWeatherDataResult(_message.Message):
    __slots__ = ("temperature_deg_f", "pressure_in_hg", "humidity_rh", "execution")
    TEMPERATURE_DEG_F_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_IN_HG_FIELD_NUMBER: _ClassVar[int]
    HUMIDITY_RH_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    temperature_deg_f: float
    pressure_in_hg: float
    humidity_rh: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, temperature_deg_f: _Optional[float] = ..., pressure_in_hg: _Optional[float] = ..., humidity_rh: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfCollectionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNumberOfCollectionsResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfFramesInFrameSetRequest(_message.Message):
    __slots__ = ("frame_set_container",)
    FRAME_SET_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    frame_set_container: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, frame_set_container: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetNumberOfFramesInFrameSetResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfPointsInGroupRequest(_message.Message):
    __slots__ = ("group_name",)
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetNumberOfPointsInGroupResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfPointsInPointSetRequest(_message.Message):
    __slots__ = ("point_set_container",)
    POINT_SET_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    point_set_container: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_set_container: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetNumberOfPointsInPointSetResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetObjectReportingFrameRequest(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetObjectReportingFrameResult(_message.Message):
    __slots__ = ("reporting_frame", "execution")
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPlanePropertiesRequest(_message.Message):
    __slots__ = ("plane_name",)
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetPlanePropertiesResult(_message.Message):
    __slots__ = ("normal_direction", "point_on_plane", "d_parameter", "execution")
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    POINT_ON_PLANE_FIELD_NUMBER: _ClassVar[int]
    D_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    normal_direction: _spatial_analyzer_values_pb2.Vector
    point_on_plane: _spatial_analyzer_values_pb2.Vector
    d_parameter: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., point_on_plane: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., d_parameter: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointCoordinateRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointCoordinateResult(_message.Message):
    __slots__ = ("vector_representation", "x_value", "y_value", "z_value", "execution")
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointCoordinateCylindricalRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointCoordinateCylindricalResult(_message.Message):
    __slots__ = ("radius_value", "theta_value", "z_value", "execution")
    RADIUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    THETA_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    radius_value: float
    theta_value: float
    z_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, radius_value: _Optional[float] = ..., theta_value: _Optional[float] = ..., z_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointCoordinatePolarRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointCoordinatePolarResult(_message.Message):
    __slots__ = ("radius_value", "theta_value", "phi_value", "execution")
    RADIUS_VALUE_FIELD_NUMBER: _ClassVar[int]
    THETA_VALUE_FIELD_NUMBER: _ClassVar[int]
    PHI_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    radius_value: float
    theta_value: float
    phi_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, radius_value: _Optional[float] = ..., theta_value: _Optional[float] = ..., phi_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointPropertiesRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointPropertiesResult(_message.Message):
    __slots__ = ("planar_offset", "radial_offset", "ux", "uy", "uz", "umag", "position_tolerance", "component_weights", "execution")
    PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    UX_FIELD_NUMBER: _ClassVar[int]
    UY_FIELD_NUMBER: _ClassVar[int]
    UZ_FIELD_NUMBER: _ClassVar[int]
    UMAG_FIELD_NUMBER: _ClassVar[int]
    POSITION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    planar_offset: float
    radial_offset: float
    ux: float
    uy: float
    uz: float
    umag: float
    position_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    component_weights: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, planar_offset: _Optional[float] = ..., radial_offset: _Optional[float] = ..., ux: _Optional[float] = ..., uy: _Optional[float] = ..., uz: _Optional[float] = ..., umag: _Optional[float] = ..., position_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., component_weights: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointToLineDistanceRequest(_message.Message):
    __slots__ = ("point", "line")
    POINT_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    line: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., line: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetPointToLineDistanceResult(_message.Message):
    __slots__ = ("vector_representation", "x_value", "y_value", "z_value", "magnitude", "execution")
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointToPointDistanceRequest(_message.Message):
    __slots__ = ("first_point", "second_point")
    FIRST_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_POINT_FIELD_NUMBER: _ClassVar[int]
    first_point: _spatial_analyzer_values_pb2.PointName
    second_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, first_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointToPointDistanceResult(_message.Message):
    __slots__ = ("vector_representation", "x_value", "y_value", "z_value", "magnitude", "execution")
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointToleranceRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointToleranceResult(_message.Message):
    __slots__ = ("use_high_x_tolerance", "high_x_tolerance", "use_high_y_tolerance", "high_y_tolerance", "use_high_z_tolerance", "high_z_tolerance", "use_high_mag_tolerance", "high_mag_tolerance", "use_low_x_tolerance", "low_x_tolerance", "use_low_y_tolerance", "low_y_tolerance", "use_low_z_tolerance", "low_z_tolerance", "use_low_mag_tolerance", "low_mag_tolerance", "vector_tolerance", "execution")
    USE_HIGH_X_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_X_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_HIGH_Y_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_Y_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_HIGH_Z_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_Z_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_HIGH_MAG_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_MAG_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_X_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_X_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_Y_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_Y_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_Z_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_Z_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_MAG_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_MAG_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    VECTOR_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_high_x_tolerance: bool
    high_x_tolerance: float
    use_high_y_tolerance: bool
    high_y_tolerance: float
    use_high_z_tolerance: bool
    high_z_tolerance: float
    use_high_mag_tolerance: bool
    high_mag_tolerance: float
    use_low_x_tolerance: bool
    low_x_tolerance: float
    use_low_y_tolerance: bool
    low_y_tolerance: float
    use_low_z_tolerance: bool
    low_z_tolerance: float
    use_low_mag_tolerance: bool
    low_mag_tolerance: float
    vector_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_high_x_tolerance: bool = ..., high_x_tolerance: _Optional[float] = ..., use_high_y_tolerance: bool = ..., high_y_tolerance: _Optional[float] = ..., use_high_z_tolerance: bool = ..., high_z_tolerance: _Optional[float] = ..., use_high_mag_tolerance: bool = ..., high_mag_tolerance: _Optional[float] = ..., use_low_x_tolerance: bool = ..., low_x_tolerance: _Optional[float] = ..., use_low_y_tolerance: bool = ..., low_y_tolerance: _Optional[float] = ..., use_low_z_tolerance: bool = ..., low_z_tolerance: _Optional[float] = ..., use_low_mag_tolerance: bool = ..., low_mag_tolerance: _Optional[float] = ..., vector_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetSlotPropertiesRequest(_message.Message):
    __slots__ = ("slot_name",)
    SLOT_NAME_FIELD_NUMBER: _ClassVar[int]
    slot_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, slot_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetSlotPropertiesResult(_message.Message):
    __slots__ = ("slot_transform_in_working_coordinates", "center_in_working_coordinates", "normal_direction_in_working_coordinates", "slot_length", "slot_width", "round_slot_type", "centerline_pt_1_in_working_coordinates", "centerline_pt_2_in_working_coordinates", "execution")
    SLOT_TRANSFORM_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CENTER_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    SLOT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    SLOT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    ROUND_SLOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CENTERLINE_PT_1_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CENTERLINE_PT_2_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    slot_transform_in_working_coordinates: _spatial_analyzer_values_pb2.Transform
    center_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    normal_direction_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    slot_length: float
    slot_width: float
    round_slot_type: bool
    centerline_pt_1_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    centerline_pt_2_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, slot_transform_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., center_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., slot_length: _Optional[float] = ..., slot_width: _Optional[float] = ..., round_slot_type: bool = ..., centerline_pt_1_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., centerline_pt_2_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetSpherePropertiesRequest(_message.Message):
    __slots__ = ("sphere_name",)
    SPHERE_NAME_FIELD_NUMBER: _ClassVar[int]
    sphere_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, sphere_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetSpherePropertiesResult(_message.Message):
    __slots__ = ("center_coordinate", "radius", "diameter", "execution")
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    radius: float
    diameter: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., radius: _Optional[float] = ..., diameter: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetSurfacePhysicalStatsRequest(_message.Message):
    __slots__ = ("surface_name",)
    SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetSurfacePhysicalStatsResult(_message.Message):
    __slots__ = ("volume", "area", "execution")
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    volume: float
    area: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, volume: _Optional[float] = ..., area: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTimestampForIthFrameInFrameSetRequest(_message.Message):
    __slots__ = ("frame_set", "frame_set_index")
    FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    frame_set: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_set_index: int
    def __init__(self, frame_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_set_index: _Optional[int] = ...) -> None: ...

class GetTimestampForIthFrameInFrameSetResult(_message.Message):
    __slots__ = ("timestamp", "execution")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    timestamp: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, timestamp: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTimestampForIthPointInPointSetRequest(_message.Message):
    __slots__ = ("point_set", "point_set_index")
    POINT_SET_FIELD_NUMBER: _ClassVar[int]
    POINT_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    point_set: _spatial_analyzer_values_pb2.CollectionObjectName
    point_set_index: int
    def __init__(self, point_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_set_index: _Optional[int] = ...) -> None: ...

class GetTimestampForIthPointInPointSetResult(_message.Message):
    __slots__ = ("timestamp", "execution")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    timestamp: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, timestamp: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTorusPropertiesRequest(_message.Message):
    __slots__ = ("torus_name",)
    TORUS_NAME_FIELD_NUMBER: _ClassVar[int]
    torus_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, torus_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetTorusPropertiesResult(_message.Message):
    __slots__ = ("center_coordinate", "normal_direction", "major_radius", "minor_radius", "execution")
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MAJOR_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MINOR_RADIUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    normal_direction: _spatial_analyzer_values_pb2.Vector
    major_radius: float
    minor_radius: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., major_radius: _Optional[float] = ..., minor_radius: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTransformForIthFrameInFrameSetRequest(_message.Message):
    __slots__ = ("frame_set", "frame_set_index")
    FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    frame_set: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_set_index: int
    def __init__(self, frame_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_set_index: _Optional[int] = ...) -> None: ...

class GetTransformForIthFrameInFrameSetResult(_message.Message):
    __slots__ = ("transform_in_working", "execution")
    TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform_in_working: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GroupToSurfaceFitRequest(_message.Message):
    __slots__ = ("group_to_fit", "surface", "do_conventional_fit", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none")
    GROUP_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FIELD_NUMBER: _ClassVar[int]
    DO_CONVENTIONAL_FIT_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    group_to_fit: _spatial_analyzer_values_pb2.CollectionObjectName
    surface: _spatial_analyzer_values_pb2.CollectionObjectName
    do_conventional_fit: bool
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    def __init__(self, group_to_fit: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., do_conventional_fit: bool = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class GroupToSurfaceFitResult(_message.Message):
    __slots__ = ("optimum_transform", "rms_deviation", "maximum_absolute_deviation", "execution")
    OPTIMUM_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    optimum_transform: _spatial_analyzer_values_pb2.WorldTransform
    rms_deviation: float
    maximum_absolute_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, optimum_transform: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., rms_deviation: _Optional[float] = ..., maximum_absolute_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportGeometryFitProfilesRequest(_message.Message):
    __slots__ = ("geometry_fit_profiles_file_path", "overwrite_profiles_with_same_name")
    GEOMETRY_FIT_PROFILES_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_PROFILES_WITH_SAME_NAME_FIELD_NUMBER: _ClassVar[int]
    geometry_fit_profiles_file_path: _spatial_analyzer_values_pb2.FileReference
    overwrite_profiles_with_same_name: bool
    def __init__(self, geometry_fit_profiles_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., overwrite_profiles_with_same_name: bool = ...) -> None: ...

class ImportGeometryFitProfilesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class IsObjectOfTypeRequest(_message.Message):
    __slots__ = ("object_name", "object_type")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    object_type: _spatial_analyzer_values_pb2.ObjectType
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ...) -> None: ...

class IsObjectOfTypeResult(_message.Message):
    __slots__ = ("resultant", "execution")
    RESULTANT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCircleFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "measured_side_for_planar_offset", "override_planar_offset_1_0_use_current", "planar_offset_direction", "lock_radius_1_0_do_not_lock", "circle_computation_technique", "reverse_normal_vector_after_fit", "make_cardinal_points", "cardinal_pt_1_center", "cardinal_pt_2_point_on_normal")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PLANAR_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LOCK_RADIUS_1_0_DO_NOT_LOCK_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_COMPUTATION_TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_NORMAL_VECTOR_AFTER_FIT_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_CENTER_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_ON_NORMAL_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    measured_side_for_planar_offset: _spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset
    override_planar_offset_1_0_use_current: float
    planar_offset_direction: _spatial_analyzer_values_pb2.NormalDirection
    lock_radius_1_0_do_not_lock: float
    circle_computation_technique: _spatial_analyzer_values_pb2.CompTechnique
    reverse_normal_vector_after_fit: bool
    make_cardinal_points: bool
    cardinal_pt_1_center: bool
    cardinal_pt_2_point_on_normal: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., measured_side_for_planar_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset, str]] = ..., override_planar_offset_1_0_use_current: _Optional[float] = ..., planar_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.NormalDirection, str]] = ..., lock_radius_1_0_do_not_lock: _Optional[float] = ..., circle_computation_technique: _Optional[_Union[_spatial_analyzer_values_pb2.CompTechnique, str]] = ..., reverse_normal_vector_after_fit: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_center: bool = ..., cardinal_pt_2_point_on_normal: bool = ...) -> None: ...

class MakeCircleFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeConeFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "lock_angle_in_degrees_1_0_do_not_lock", "use_exhaustive_search", "make_cardinal_points", "cardinal_pt_1_vertex", "cardinal_pt_2_point_on_axis", "cardinal_pt_3_cut_point_on_axis")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LOCK_ANGLE_IN_DEGREES_1_0_DO_NOT_LOCK_FIELD_NUMBER: _ClassVar[int]
    USE_EXHAUSTIVE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_VERTEX_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_ON_AXIS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_3_CUT_POINT_ON_AXIS_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    lock_angle_in_degrees_1_0_do_not_lock: float
    use_exhaustive_search: bool
    make_cardinal_points: bool
    cardinal_pt_1_vertex: bool
    cardinal_pt_2_point_on_axis: bool
    cardinal_pt_3_cut_point_on_axis: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., lock_angle_in_degrees_1_0_do_not_lock: _Optional[float] = ..., use_exhaustive_search: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_vertex: bool = ..., cardinal_pt_2_point_on_axis: bool = ..., cardinal_pt_3_cut_point_on_axis: bool = ...) -> None: ...

class MakeConeFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCylinderFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "lock_radius_1_0_do_not_lock", "locked_radius_fit_method", "constrain_to_nominal_axis", "constrain_to_nominal_orientation", "align_with_nominal", "reverse_axis", "set_axis_first_to_last_point", "cylinder_computation_technique", "use_exhaustive_search", "make_cardinal_points", "cardinal_pt_1_begin_pt", "cardinal_pt_2_end_pt", "cardinal_pt_3_center")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LOCK_RADIUS_1_0_DO_NOT_LOCK_FIELD_NUMBER: _ClassVar[int]
    LOCKED_RADIUS_FIT_METHOD_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_TO_NOMINAL_AXIS_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_TO_NOMINAL_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    ALIGN_WITH_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    REVERSE_AXIS_FIELD_NUMBER: _ClassVar[int]
    SET_AXIS_FIRST_TO_LAST_POINT_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_COMPUTATION_TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    USE_EXHAUSTIVE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_BEGIN_PT_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_END_PT_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_3_CENTER_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    lock_radius_1_0_do_not_lock: float
    locked_radius_fit_method: _spatial_analyzer_values_pb2.FitMethod
    constrain_to_nominal_axis: bool
    constrain_to_nominal_orientation: bool
    align_with_nominal: bool
    reverse_axis: bool
    set_axis_first_to_last_point: bool
    cylinder_computation_technique: _spatial_analyzer_values_pb2.CompTechnique
    use_exhaustive_search: bool
    make_cardinal_points: bool
    cardinal_pt_1_begin_pt: bool
    cardinal_pt_2_end_pt: bool
    cardinal_pt_3_center: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., lock_radius_1_0_do_not_lock: _Optional[float] = ..., locked_radius_fit_method: _Optional[_Union[_spatial_analyzer_values_pb2.FitMethod, str]] = ..., constrain_to_nominal_axis: bool = ..., constrain_to_nominal_orientation: bool = ..., align_with_nominal: bool = ..., reverse_axis: bool = ..., set_axis_first_to_last_point: bool = ..., cylinder_computation_technique: _Optional[_Union[_spatial_analyzer_values_pb2.CompTechnique, str]] = ..., use_exhaustive_search: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_begin_pt: bool = ..., cardinal_pt_2_end_pt: bool = ..., cardinal_pt_3_center: bool = ...) -> None: ...

class MakeCylinderFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeEllipseFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "measured_side_for_planar_offset", "override_planar_offset_1_0_use_current", "planar_offset_direction", "reverse_normal_vector_after_fit", "make_cardinal_points", "cardinal_pt_1_center", "cardinal_pt_2_point_on_normal", "cardinal_pt_3_focal_pt_1", "cardinal_pt_4_focal_pt_2")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PLANAR_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    REVERSE_NORMAL_VECTOR_AFTER_FIT_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_CENTER_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_ON_NORMAL_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_3_FOCAL_PT_1_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_4_FOCAL_PT_2_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    measured_side_for_planar_offset: _spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset
    override_planar_offset_1_0_use_current: float
    planar_offset_direction: _spatial_analyzer_values_pb2.NormalDirection
    reverse_normal_vector_after_fit: bool
    make_cardinal_points: bool
    cardinal_pt_1_center: bool
    cardinal_pt_2_point_on_normal: bool
    cardinal_pt_3_focal_pt_1: bool
    cardinal_pt_4_focal_pt_2: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., measured_side_for_planar_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset, str]] = ..., override_planar_offset_1_0_use_current: _Optional[float] = ..., planar_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.NormalDirection, str]] = ..., reverse_normal_vector_after_fit: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_center: bool = ..., cardinal_pt_2_point_on_normal: bool = ..., cardinal_pt_3_focal_pt_1: bool = ..., cardinal_pt_4_focal_pt_2: bool = ...) -> None: ...

class MakeEllipseFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeLineFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "reverse_normal_vector_after_fit", "make_cardinal_points", "cardinal_pt_1_point_a", "cardinal_pt_2_point_b", "cardinal_pt_3_mid_point")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REVERSE_NORMAL_VECTOR_AFTER_FIT_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_POINT_A_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_B_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_3_MID_POINT_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    reverse_normal_vector_after_fit: bool
    make_cardinal_points: bool
    cardinal_pt_1_point_a: bool
    cardinal_pt_2_point_b: bool
    cardinal_pt_3_mid_point: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., reverse_normal_vector_after_fit: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_point_a: bool = ..., cardinal_pt_2_point_b: bool = ..., cardinal_pt_3_mid_point: bool = ...) -> None: ...

class MakeLineFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeParaboloidFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "lock_focal_length_1_0_do_not_lock", "degree_of_freedom", "make_cardinal_points", "cardinal_pt_1_vertex", "cardinal_pt_2_focal_point")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LOCK_FOCAL_LENGTH_1_0_DO_NOT_LOCK_FIELD_NUMBER: _ClassVar[int]
    DEGREE_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_VERTEX_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_FOCAL_POINT_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    lock_focal_length_1_0_do_not_lock: float
    degree_of_freedom: _spatial_analyzer_values_pb2.DegreeOfFreedom
    make_cardinal_points: bool
    cardinal_pt_1_vertex: bool
    cardinal_pt_2_focal_point: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., lock_focal_length_1_0_do_not_lock: _Optional[float] = ..., degree_of_freedom: _Optional[_Union[_spatial_analyzer_values_pb2.DegreeOfFreedom, str]] = ..., make_cardinal_points: bool = ..., cardinal_pt_1_vertex: bool = ..., cardinal_pt_2_focal_point: bool = ...) -> None: ...

class MakeParaboloidFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePlaneFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_planar_offset", "override_planar_offset_1_0_use_current", "planar_offset_direction", "reverse_normal_vector_after_fit", "make_cardinal_points", "cardinal_pt_1_centroid", "cardinal_pt_2_point_on_normal")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PLANAR_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    REVERSE_NORMAL_VECTOR_AFTER_FIT_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_CENTROID_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_ON_NORMAL_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_planar_offset: _spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset
    override_planar_offset_1_0_use_current: float
    planar_offset_direction: _spatial_analyzer_values_pb2.NormalDirection
    reverse_normal_vector_after_fit: bool
    make_cardinal_points: bool
    cardinal_pt_1_centroid: bool
    cardinal_pt_2_point_on_normal: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_planar_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset, str]] = ..., override_planar_offset_1_0_use_current: _Optional[float] = ..., planar_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.NormalDirection, str]] = ..., reverse_normal_vector_after_fit: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_centroid: bool = ..., cardinal_pt_2_point_on_normal: bool = ...) -> None: ...

class MakePlaneFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSlotFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "measured_side_for_planar_offset", "override_planar_offset_1_0_use_current", "planar_offset_direction", "slot_type", "slot_computation_technique", "reverse_normal_vector_after_fit", "make_cardinal_points", "cardinal_pt_1_center", "cardinal_pt_2_point_on_normal", "cardinal_pt_3_centerline_pt_1", "cardinal_pt_4_centerline_pt_2")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_PLANAR_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SLOT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_COMPUTATION_TECHNIQUE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_NORMAL_VECTOR_AFTER_FIT_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_CENTER_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_2_POINT_ON_NORMAL_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_3_CENTERLINE_PT_1_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_4_CENTERLINE_PT_2_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    measured_side_for_planar_offset: _spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset
    override_planar_offset_1_0_use_current: float
    planar_offset_direction: _spatial_analyzer_values_pb2.NormalDirection
    slot_type: _spatial_analyzer_values_pb2.SlotType
    slot_computation_technique: _spatial_analyzer_values_pb2.CompTechnique
    reverse_normal_vector_after_fit: bool
    make_cardinal_points: bool
    cardinal_pt_1_center: bool
    cardinal_pt_2_point_on_normal: bool
    cardinal_pt_3_centerline_pt_1: bool
    cardinal_pt_4_centerline_pt_2: bool
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., measured_side_for_planar_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForPlanarOffset, str]] = ..., override_planar_offset_1_0_use_current: _Optional[float] = ..., planar_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.NormalDirection, str]] = ..., slot_type: _Optional[_Union[_spatial_analyzer_values_pb2.SlotType, str]] = ..., slot_computation_technique: _Optional[_Union[_spatial_analyzer_values_pb2.CompTechnique, str]] = ..., reverse_normal_vector_after_fit: bool = ..., make_cardinal_points: bool = ..., cardinal_pt_1_center: bool = ..., cardinal_pt_2_point_on_normal: bool = ..., cardinal_pt_3_centerline_pt_1: bool = ..., cardinal_pt_4_centerline_pt_2: bool = ...) -> None: ...

class MakeSlotFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSphereFitProfileRequest(_message.Message):
    __slots__ = ("fit_profile_name", "measured_side_for_radial_offset", "override_radial_offset_1_0_use_current", "lock_radius_1_0_do_not_lock", "make_cardinal_points", "cardinal_pt_1_center", "computation_method")
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_RADIAL_OFFSET_1_0_USE_CURRENT_FIELD_NUMBER: _ClassVar[int]
    LOCK_RADIUS_1_0_DO_NOT_LOCK_FIELD_NUMBER: _ClassVar[int]
    MAKE_CARDINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PT_1_CENTER_FIELD_NUMBER: _ClassVar[int]
    COMPUTATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    fit_profile_name: str
    measured_side_for_radial_offset: _spatial_analyzer_values_pb2.MeasuredSideForRadialOffset
    override_radial_offset_1_0_use_current: float
    lock_radius_1_0_do_not_lock: float
    make_cardinal_points: bool
    cardinal_pt_1_center: bool
    computation_method: _spatial_analyzer_values_pb2.SphereFitComputationMode
    def __init__(self, fit_profile_name: _Optional[str] = ..., measured_side_for_radial_offset: _Optional[_Union[_spatial_analyzer_values_pb2.MeasuredSideForRadialOffset, str]] = ..., override_radial_offset_1_0_use_current: _Optional[float] = ..., lock_radius_1_0_do_not_lock: _Optional[float] = ..., make_cardinal_points: bool = ..., cardinal_pt_1_center: bool = ..., computation_method: _Optional[_Union[_spatial_analyzer_values_pb2.SphereFitComputationMode, str]] = ...) -> None: ...

class MakeSphereFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MushroomTargetHoleInspectionRequest(_message.Message):
    __slots__ = ("name_prefix_for_intermediate_constructions", "sphere_points_group_name", "sphere_target_radius", "target_contact_plane", "point_to_create_at_hole")
    NAME_PREFIX_FOR_INTERMEDIATE_CONSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    SPHERE_POINTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SPHERE_TARGET_RADIUS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CONTACT_PLANE_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_CREATE_AT_HOLE_FIELD_NUMBER: _ClassVar[int]
    name_prefix_for_intermediate_constructions: str
    sphere_points_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    sphere_target_radius: float
    target_contact_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    point_to_create_at_hole: _spatial_analyzer_values_pb2.PointName
    def __init__(self, name_prefix_for_intermediate_constructions: _Optional[str] = ..., sphere_points_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., sphere_target_radius: _Optional[float] = ..., target_contact_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_to_create_at_hole: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class MushroomTargetHoleInspectionResult(_message.Message):
    __slots__ = ("sphere_fit_rms_error", "sphere_fit_max_error", "execution")
    SPHERE_FIT_RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    SPHERE_FIT_MAX_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    sphere_fit_rms_error: float
    sphere_fit_max_error: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, sphere_fit_rms_error: _Optional[float] = ..., sphere_fit_max_error: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PatchNormalShiftHolePinRequest(_message.Message):
    __slots__ = ("plane_points_group_name", "perimeter_points_group_name", "resulting_point_name", "additional_material_thickness")
    PLANE_POINTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_POINTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_MATERIAL_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    plane_points_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    perimeter_points_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    additional_material_thickness: float
    def __init__(self, plane_points_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., perimeter_points_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., additional_material_thickness: _Optional[float] = ...) -> None: ...

class PatchNormalShiftHolePinResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PatchNormalShiftPointRequest(_message.Message):
    __slots__ = ("plane_points_group_name", "point_to_shift", "resulting_point_name", "additional_material_thickness")
    PLANE_POINTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_SHIFT_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_MATERIAL_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    plane_points_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_to_shift: _spatial_analyzer_values_pb2.PointName
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    additional_material_thickness: float
    def __init__(self, plane_points_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_to_shift: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., additional_material_thickness: _Optional[float] = ...) -> None: ...

class PatchNormalShiftPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryCloudsToObjectsRequest(_message.Message):
    __slots__ = ("cloud_names", "object_names", "resulting_object_name", "projection_options", "proximity", "skip_factor", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAMES_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FACTOR_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    object_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    proximity: float
    skip_factor: int
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., object_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., proximity: _Optional[float] = ..., skip_factor: _Optional[int] = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class QueryCloudsToObjectsResult(_message.Message):
    __slots__ = ("rms_deviation", "maximum_absolute_deviation", "execution")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    maximum_absolute_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_deviation: _Optional[float] = ..., maximum_absolute_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryCloudsToSurfaceRequest(_message.Message):
    __slots__ = ("cloud_names", "filter_surface_name", "resulting_object_name", "projection_options", "proximity", "skip_factor", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FACTOR_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    filter_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    proximity: float
    skip_factor: int
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., filter_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., proximity: _Optional[float] = ..., skip_factor: _Optional[int] = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ...) -> None: ...

class QueryCloudsToSurfaceResult(_message.Message):
    __slots__ = ("rms_deviation", "maximum_absolute_deviation", "execution")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    maximum_absolute_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_deviation: _Optional[float] = ..., maximum_absolute_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryFrameToFrameRequest(_message.Message):
    __slots__ = ("reference_frame_name", "corresponding_frame_name")
    REFERENCE_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    reference_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    corresponding_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., corresponding_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class QueryFrameToFrameResult(_message.Message):
    __slots__ = ("x", "y", "z", "rx_roll", "ry_pitch", "rz_yaw", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RX_ROLL_FIELD_NUMBER: _ClassVar[int]
    RY_PITCH_FIELD_NUMBER: _ClassVar[int]
    RZ_YAW_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rx_roll: float
    ry_pitch: float
    rz_yaw: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rx_roll: _Optional[float] = ..., ry_pitch: _Optional[float] = ..., rz_yaw: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryGroupsToObjectsRequest(_message.Message):
    __slots__ = ("group_name_list_groups_to_project", "object_name_list_objects_to_project_to", "resulting_object_name", "projection_options", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none", "show_results_dialog")
    GROUP_NAME_LIST_GROUPS_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_LIST_OBJECTS_TO_PROJECT_TO_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESULTS_DIALOG_FIELD_NUMBER: _ClassVar[int]
    group_name_list_groups_to_project: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    object_name_list_objects_to_project_to: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    show_results_dialog: bool
    def __init__(self, group_name_list_groups_to_project: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., object_name_list_objects_to_project_to: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ..., show_results_dialog: bool = ...) -> None: ...

class QueryGroupsToObjectsResult(_message.Message):
    __slots__ = ("rms_deviation", "max_absolute_deviation", "average_deviation", "standard_deviation", "execution")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAX_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    standard_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_deviation: _Optional[float] = ..., max_absolute_deviation: _Optional[float] = ..., average_deviation: _Optional[float] = ..., standard_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryPointToObjectsRequest(_message.Message):
    __slots__ = ("point_name", "objects", "ignore_target_offset")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_TARGET_OFFSET_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    ignore_target_offset: bool
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., ignore_target_offset: bool = ...) -> None: ...

class QueryPointToObjectsResult(_message.Message):
    __slots__ = ("d_x", "d_y", "d_z", "d_mag", "resultant_object", "execution")
    D_X_FIELD_NUMBER: _ClassVar[int]
    D_Y_FIELD_NUMBER: _ClassVar[int]
    D_Z_FIELD_NUMBER: _ClassVar[int]
    D_MAG_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_OBJECT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    d_x: float
    d_y: float
    d_z: float
    d_mag: float
    resultant_object: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, d_x: _Optional[float] = ..., d_y: _Optional[float] = ..., d_z: _Optional[float] = ..., d_mag: _Optional[float] = ..., resultant_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryPointToPointAlongCurveRequest(_message.Message):
    __slots__ = ("value_1st_point", "value_2nd_point", "curve")
    VALUE_1ST_POINT_FIELD_NUMBER: _ClassVar[int]
    VALUE_2ND_POINT_FIELD_NUMBER: _ClassVar[int]
    CURVE_FIELD_NUMBER: _ClassVar[int]
    value_1st_point: _spatial_analyzer_values_pb2.PointName
    value_2nd_point: _spatial_analyzer_values_pb2.PointName
    curve: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, value_1st_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., value_2nd_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., curve: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class QueryPointToPointAlongCurveResult(_message.Message):
    __slots__ = ("distance_along_curve", "execution")
    DISTANCE_ALONG_CURVE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    distance_along_curve: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, distance_along_curve: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryPointsToCircleRequest(_message.Message):
    __slots__ = ("circle_name", "point_group_name", "is_inside_measurement", "auto_scale_vectors_to_of_radius", "vector_group_name_for_radial", "vector_group_name_for_planar", "vector_group_name_for_combined")
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_INSIDE_MEASUREMENT_FIELD_NUMBER: _ClassVar[int]
    AUTO_SCALE_VECTORS_TO_OF_RADIUS_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FOR_RADIAL_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FOR_PLANAR_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FOR_COMBINED_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    is_inside_measurement: bool
    auto_scale_vectors_to_of_radius: int
    vector_group_name_for_radial: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_group_name_for_planar: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_group_name_for_combined: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., is_inside_measurement: bool = ..., auto_scale_vectors_to_of_radius: _Optional[int] = ..., vector_group_name_for_radial: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_group_name_for_planar: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_group_name_for_combined: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class QueryPointsToCircleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryPointsToObjectsRequest(_message.Message):
    __slots__ = ("point_names", "object_name_list_objects_to_project_to", "resulting_object_name", "projection_options", "rms_tolerance_0_0_for_none", "maximum_absolute_tolerance_0_0_for_none", "show_results_dialog")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_LIST_OBJECTS_TO_PROJECT_TO_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_0_0_FOR_NONE_FIELD_NUMBER: _ClassVar[int]
    SHOW_RESULTS_DIALOG_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    object_name_list_objects_to_project_to: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    rms_tolerance_0_0_for_none: float
    maximum_absolute_tolerance_0_0_for_none: float
    show_results_dialog: bool
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., object_name_list_objects_to_project_to: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., rms_tolerance_0_0_for_none: _Optional[float] = ..., maximum_absolute_tolerance_0_0_for_none: _Optional[float] = ..., show_results_dialog: bool = ...) -> None: ...

class QueryPointsToObjectsResult(_message.Message):
    __slots__ = ("rms_deviation", "max_absolute_deviation", "average_deviation", "standard_deviation", "execution")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAX_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    standard_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_deviation: _Optional[float] = ..., max_absolute_deviation: _Optional[float] = ..., average_deviation: _Optional[float] = ..., standard_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QueryPointsToSinglePointRequest(_message.Message):
    __slots__ = ("point_names", "single_point", "show_vector_properties")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    SINGLE_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    single_point: _spatial_analyzer_values_pb2.PointName
    show_vector_properties: bool
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., single_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., show_vector_properties: bool = ...) -> None: ...

class QueryPointsToSinglePointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ReComputeCalculatedItemsRequest(_message.Message):
    __slots__ = ("targets_from_shots", "hidden_points", "relationships", "refresh_filtered_cloud_data")
    TARGETS_FROM_SHOTS_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_POINTS_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FILTERED_CLOUD_DATA_FIELD_NUMBER: _ClassVar[int]
    targets_from_shots: bool
    hidden_points: bool
    relationships: bool
    refresh_filtered_cloud_data: bool
    def __init__(self, targets_from_shots: bool = ..., hidden_points: bool = ..., relationships: bool = ..., refresh_filtered_cloud_data: bool = ...) -> None: ...

class ReComputeCalculatedItemsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenamePointsBasedOnInterPointDistanceToReferencePointsRequest(_message.Message):
    __slots__ = ("reference_group_name", "group_to_rename_points", "distance_threshold", "verify_results")
    REFERENCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_RENAME_POINTS_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VERIFY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    reference_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    group_to_rename_points: _spatial_analyzer_values_pb2.CollectionObjectName
    distance_threshold: float
    verify_results: bool
    def __init__(self, reference_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_to_rename_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., distance_threshold: _Optional[float] = ..., verify_results: bool = ...) -> None: ...

class RenamePointsBasedOnInterPointDistanceToReferencePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenamePointsBasedOnProximityToReferencePointsRequest(_message.Message):
    __slots__ = ("reference_group_name", "group_to_rename_points", "proximity_threshold", "verify_results", "rename_all_proximate_points")
    REFERENCE_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_RENAME_POINTS_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VERIFY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    RENAME_ALL_PROXIMATE_POINTS_FIELD_NUMBER: _ClassVar[int]
    reference_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    group_to_rename_points: _spatial_analyzer_values_pb2.CollectionObjectName
    proximity_threshold: float
    verify_results: bool
    rename_all_proximate_points: bool
    def __init__(self, reference_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_to_rename_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., proximity_threshold: _Optional[float] = ..., verify_results: bool = ..., rename_all_proximate_points: bool = ...) -> None: ...

class RenamePointsBasedOnProximityToReferencePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ReverseBSplinesRequest(_message.Message):
    __slots__ = ("b_spline_list",)
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ReverseBSplinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ReversePlaneNormalsRequest(_message.Message):
    __slots__ = ("plane_list",)
    PLANE_LIST_FIELD_NUMBER: _ClassVar[int]
    plane_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, plane_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ReversePlaneNormalsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ReverseSurfaceNormalsRequest(_message.Message):
    __slots__ = ("surface_list",)
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ReverseSurfaceNormalsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCirclePropertiesRequest(_message.Message):
    __slots__ = ("circle_name", "center_coordinate", "normal_direction", "radius")
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    normal_direction: _spatial_analyzer_values_pb2.Vector
    radius: float
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., radius: _Optional[float] = ...) -> None: ...

class SetCirclePropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetConePropertiesRequest(_message.Message):
    __slots__ = ("cone_name", "cone_end_point_in_working_coordinates", "cone_axis_in_working_coordinates", "cone_length", "cone_theta_start", "cone_theta_span", "cone_included_angle", "cut_length_from_apex")
    CONE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONE_END_POINT_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CONE_AXIS_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    CONE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_START_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_SPAN_FIELD_NUMBER: _ClassVar[int]
    CONE_INCLUDED_ANGLE_FIELD_NUMBER: _ClassVar[int]
    CUT_LENGTH_FROM_APEX_FIELD_NUMBER: _ClassVar[int]
    cone_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cone_end_point_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    cone_axis_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    cone_length: float
    cone_theta_start: float
    cone_theta_span: float
    cone_included_angle: float
    cut_length_from_apex: float
    def __init__(self, cone_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cone_end_point_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_axis_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_length: _Optional[float] = ..., cone_theta_start: _Optional[float] = ..., cone_theta_span: _Optional[float] = ..., cone_included_angle: _Optional[float] = ..., cut_length_from_apex: _Optional[float] = ...) -> None: ...

class SetConePropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCylinderPropertiesRequest(_message.Message):
    __slots__ = ("cylinder_name", "begin_coordinate", "axis_direction", "length", "diameter", "nominals_point_inward", "facets", "enable_theta_extent_display_mode", "theta_start_in_degrees", "theta_span_in_degrees")
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    AXIS_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    NOMINALS_POINT_INWARD_FIELD_NUMBER: _ClassVar[int]
    FACETS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_THETA_EXTENT_DISPLAY_MODE_FIELD_NUMBER: _ClassVar[int]
    THETA_START_IN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    THETA_SPAN_IN_DEGREES_FIELD_NUMBER: _ClassVar[int]
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    begin_coordinate: _spatial_analyzer_values_pb2.Vector
    axis_direction: _spatial_analyzer_values_pb2.Vector
    length: float
    diameter: float
    nominals_point_inward: bool
    facets: int
    enable_theta_extent_display_mode: bool
    theta_start_in_degrees: float
    theta_span_in_degrees: float
    def __init__(self, cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., begin_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., axis_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., length: _Optional[float] = ..., diameter: _Optional[float] = ..., nominals_point_inward: bool = ..., facets: _Optional[int] = ..., enable_theta_extent_display_mode: bool = ..., theta_start_in_degrees: _Optional[float] = ..., theta_span_in_degrees: _Optional[float] = ...) -> None: ...

class SetCylinderPropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDefaultColorizationOptionsRequest(_message.Message):
    __slots__ = ("colorization_options",)
    COLORIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    colorization_options: _spatial_analyzer_values_pb2.ColorizationOptions
    def __init__(self, colorization_options: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ...) -> None: ...

class SetDefaultColorizationOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetEllipsePropertiesRequest(_message.Message):
    __slots__ = ("ellipse_name", "center_coordinate", "normal_direction", "major_axis_radius", "minor_axis_radius")
    ELLIPSE_NAME_FIELD_NUMBER: _ClassVar[int]
    CENTER_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    NORMAL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    MAJOR_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MINOR_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    ellipse_name: _spatial_analyzer_values_pb2.CollectionObjectName
    center_coordinate: _spatial_analyzer_values_pb2.Vector
    normal_direction: _spatial_analyzer_values_pb2.Vector
    major_axis_radius: float
    minor_axis_radius: float
    def __init__(self, ellipse_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., center_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., major_axis_radius: _Optional[float] = ..., minor_axis_radius: _Optional[float] = ...) -> None: ...

class SetEllipsePropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeometryRelationshipFitProfileRequest(_message.Message):
    __slots__ = ("geometry_type", "relationship_ref_list", "fit_profile_name", "apply_cardinal_point_settings")
    GEOMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPLY_CARDINAL_POINT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    geometry_type: _spatial_analyzer_values_pb2.GeometryType
    relationship_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    fit_profile_name: str
    apply_cardinal_point_settings: bool
    def __init__(self, geometry_type: _Optional[_Union[_spatial_analyzer_values_pb2.GeometryType, str]] = ..., relationship_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., fit_profile_name: _Optional[str] = ..., apply_cardinal_point_settings: bool = ...) -> None: ...

class SetGeometryRelationshipFitProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLinePropertiesRequest(_message.Message):
    __slots__ = ("line_name", "begin_coordinate", "end_coordinate", "length_optional")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    END_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    LENGTH_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    begin_coordinate: _spatial_analyzer_values_pb2.Vector
    end_coordinate: _spatial_analyzer_values_pb2.Vector
    length_optional: float
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., begin_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_coordinate: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., length_optional: _Optional[float] = ...) -> None: ...

class SetLinePropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetMeasurementAuxiliaryDataRequest(_message.Message):
    __slots__ = ("point_name", "auxiliary_name", "value", "units")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    auxiliary_name: str
    value: float
    units: str
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., auxiliary_name: _Optional[str] = ..., value: _Optional[float] = ..., units: _Optional[str] = ...) -> None: ...

class SetMeasurementAuxiliaryDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectReportingFrameRequest(_message.Message):
    __slots__ = ("object_name", "reporting_frame")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetObjectReportingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointPropertiesRequest(_message.Message):
    __slots__ = ("point_name_list", "planar_offset", "radial_offset", "position_tolerance", "component_weights")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    POSITION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    planar_offset: float
    radial_offset: float
    position_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    component_weights: _spatial_analyzer_values_pb2.Vector
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., planar_offset: _Optional[float] = ..., radial_offset: _Optional[float] = ..., position_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., component_weights: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class SetPointPropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointWeightsFromUncertaintiesRequest(_message.Message):
    __slots__ = ("point_name_list", "uncertainty_reference_frame_mode", "reporting_frame", "weight_normalization_mode", "fixed_weight_value", "output_weighted_point_group")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTY_REFERENCE_FRAME_MODE_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_NORMALIZATION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIXED_WEIGHT_VALUE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_WEIGHTED_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    uncertainty_reference_frame_mode: str
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    weight_normalization_mode: str
    fixed_weight_value: float
    output_weighted_point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., uncertainty_reference_frame_mode: _Optional[str] = ..., reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., weight_normalization_mode: _Optional[str] = ..., fixed_weight_value: _Optional[float] = ..., output_weighted_point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetPointWeightsFromUncertaintiesResult(_message.Message):
    __slots__ = ("output_weighted_point_list", "execution")
    OUTPUT_WEIGHTED_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    output_weighted_point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, output_weighted_point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTransformForIthFrameInFrameSetRequest(_message.Message):
    __slots__ = ("frame_set", "frame_set_index", "transform_in_working")
    FRAME_SET_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_INDEX_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    frame_set: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_set_index: int
    transform_in_working: _spatial_analyzer_values_pb2.Transform
    def __init__(self, frame_set: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_set_index: _Optional[int] = ..., transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetTransformForIthFrameInFrameSetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SphereAxisCheckRequest(_message.Message):
    __slots__ = ("sphere_points_group_name", "sphere_target_radius", "point_to_create_at_sphere_center", "line_defining_the_axis")
    SPHERE_POINTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SPHERE_TARGET_RADIUS_FIELD_NUMBER: _ClassVar[int]
    POINT_TO_CREATE_AT_SPHERE_CENTER_FIELD_NUMBER: _ClassVar[int]
    LINE_DEFINING_THE_AXIS_FIELD_NUMBER: _ClassVar[int]
    sphere_points_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    sphere_target_radius: float
    point_to_create_at_sphere_center: _spatial_analyzer_values_pb2.PointName
    line_defining_the_axis: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, sphere_points_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., sphere_target_radius: _Optional[float] = ..., point_to_create_at_sphere_center: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., line_defining_the_axis: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SphereAxisCheckResult(_message.Message):
    __slots__ = ("sphere_fit_rms_error", "sphere_fit_max_error", "vector_representation", "x_value", "y_value", "z_value", "magnitude", "execution")
    SPHERE_FIT_RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    SPHERE_FIT_MAX_ERROR_FIELD_NUMBER: _ClassVar[int]
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    sphere_fit_rms_error: float
    sphere_fit_max_error: float
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, sphere_fit_rms_error: _Optional[float] = ..., sphere_fit_max_error: _Optional[float] = ..., vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TemperatureCompensateAGroupRequest(_message.Message):
    __slots__ = ("original_group", "scaling_origin_coordinate_frame", "material_cte_1_deg_f", "initial_temperature_f", "final_temperature_f", "scaled_group_name")
    ORIGINAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    SCALING_ORIGIN_COORDINATE_FRAME_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_CTE_1_DEG_F_FIELD_NUMBER: _ClassVar[int]
    INITIAL_TEMPERATURE_F_FIELD_NUMBER: _ClassVar[int]
    FINAL_TEMPERATURE_F_FIELD_NUMBER: _ClassVar[int]
    SCALED_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    original_group: _spatial_analyzer_values_pb2.CollectionObjectName
    scaling_origin_coordinate_frame: _spatial_analyzer_values_pb2.FrameName
    material_cte_1_deg_f: float
    initial_temperature_f: float
    final_temperature_f: float
    scaled_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, original_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., scaling_origin_coordinate_frame: _Optional[_Union[_spatial_analyzer_values_pb2.FrameName, _Mapping]] = ..., material_cte_1_deg_f: _Optional[float] = ..., initial_temperature_f: _Optional[float] = ..., final_temperature_f: _Optional[float] = ..., scaled_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class TemperatureCompensateAGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformObjectsFrameToFrameRequest(_message.Message):
    __slots__ = ("object_name_list", "initial_frame_name", "destination_frame_name", "number_of_steps")
    OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_STEPS_FIELD_NUMBER: _ClassVar[int]
    object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    initial_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    destination_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    number_of_steps: int
    def __init__(self, object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., initial_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., destination_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., number_of_steps: _Optional[int] = ...) -> None: ...

class TransformObjectsFrameToFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformObjectsByDeltaAboutWorkingFrameRequest(_message.Message):
    __slots__ = ("objects_to_transform", "delta_transform")
    OBJECTS_TO_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    DELTA_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    objects_to_transform: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    delta_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, objects_to_transform: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., delta_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class TransformObjectsByDeltaAboutWorkingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformObjectsByDeltaWorldTransformOperatorRequest(_message.Message):
    __slots__ = ("objects_to_transform", "delta_transform")
    OBJECTS_TO_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    DELTA_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    objects_to_transform: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    delta_transform: _spatial_analyzer_values_pb2.WorldTransform
    def __init__(self, objects_to_transform: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., delta_transform: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ...) -> None: ...

class TransformObjectsByDeltaWorldTransformOperatorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TranslateObjectsByDeltaRequest(_message.Message):
    __slots__ = ("objects_to_translate", "delta_translation")
    OBJECTS_TO_TRANSLATE_FIELD_NUMBER: _ClassVar[int]
    DELTA_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
    objects_to_translate: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    delta_translation: _spatial_analyzer_values_pb2.Vector
    def __init__(self, objects_to_translate: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., delta_translation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class TranslateObjectsByDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
