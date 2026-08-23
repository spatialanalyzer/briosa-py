from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloudBoxType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_BOX_TYPE_UNSPECIFIED: _ClassVar[CloudBoxType]
    CLOUD_BOX_TYPE_WORLD_AXIS_ALIGNED_BOX: _ClassVar[CloudBoxType]
    CLOUD_BOX_TYPE_WORK_AXIS_ALIGNED_BOX: _ClassVar[CloudBoxType]
    CLOUD_BOX_TYPE_MINIMUM_ORIENTED_BOX_UNCONDITIONAL: _ClassVar[CloudBoxType]
    CLOUD_BOX_TYPE_MINIMUM_ORIENTED_BOX_VERIFY_VOLUME: _ClassVar[CloudBoxType]

class PointOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POINT_OUTPUT_TYPE_UNSPECIFIED: _ClassVar[PointOutputType]
    POINT_OUTPUT_TYPE_POINTS: _ClassVar[PointOutputType]
    POINT_OUTPUT_TYPE_CLOUD_POINTS: _ClassVar[PointOutputType]

class RGBFilterOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RGB_FILTER_OPERATION_UNSPECIFIED: _ClassVar[RGBFilterOperation]
    RGB_FILTER_OPERATION_INCREMENTALLY_APPLY_FILTER: _ClassVar[RGBFilterOperation]
    RGB_FILTER_OPERATION_RESET_AND_APPLY_FILTER: _ClassVar[RGBFilterOperation]
    RGB_FILTER_OPERATION_RESET_ALL_CLOUD_POINTS_VISIBLE: _ClassVar[RGBFilterOperation]

class RGBColorChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RGB_COLOR_CHANNEL_UNSPECIFIED: _ClassVar[RGBColorChannel]
    RGB_COLOR_CHANNEL_RED: _ClassVar[RGBColorChannel]
    RGB_COLOR_CHANNEL_GREEN: _ClassVar[RGBColorChannel]
    RGB_COLOR_CHANNEL_BLUE: _ClassVar[RGBColorChannel]
    RGB_COLOR_CHANNEL_INTENSITY: _ClassVar[RGBColorChannel]
CLOUD_BOX_TYPE_UNSPECIFIED: CloudBoxType
CLOUD_BOX_TYPE_WORLD_AXIS_ALIGNED_BOX: CloudBoxType
CLOUD_BOX_TYPE_WORK_AXIS_ALIGNED_BOX: CloudBoxType
CLOUD_BOX_TYPE_MINIMUM_ORIENTED_BOX_UNCONDITIONAL: CloudBoxType
CLOUD_BOX_TYPE_MINIMUM_ORIENTED_BOX_VERIFY_VOLUME: CloudBoxType
POINT_OUTPUT_TYPE_UNSPECIFIED: PointOutputType
POINT_OUTPUT_TYPE_POINTS: PointOutputType
POINT_OUTPUT_TYPE_CLOUD_POINTS: PointOutputType
RGB_FILTER_OPERATION_UNSPECIFIED: RGBFilterOperation
RGB_FILTER_OPERATION_INCREMENTALLY_APPLY_FILTER: RGBFilterOperation
RGB_FILTER_OPERATION_RESET_AND_APPLY_FILTER: RGBFilterOperation
RGB_FILTER_OPERATION_RESET_ALL_CLOUD_POINTS_VISIBLE: RGBFilterOperation
RGB_COLOR_CHANNEL_UNSPECIFIED: RGBColorChannel
RGB_COLOR_CHANNEL_RED: RGBColorChannel
RGB_COLOR_CHANNEL_GREEN: RGBColorChannel
RGB_COLOR_CHANNEL_BLUE: RGBColorChannel
RGB_COLOR_CHANNEL_INTENSITY: RGBColorChannel

class CloudDisplayControlRequest(_message.Message):
    __slots__ = ("thin_draw_increment", "point_size")
    THIN_DRAW_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_SIZE_FIELD_NUMBER: _ClassVar[int]
    thin_draw_increment: int
    point_size: int
    def __init__(self, thin_draw_increment: _Optional[int] = ..., point_size: _Optional[int] = ...) -> None: ...

class CloudDisplayControlResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ResetCloudBoundingBoxRequest(_message.Message):
    __slots__ = ("cloud_name", "cloud_box_type", "show_bounding_box", "use_all_points", "desired_point_count")
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHOW_BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    USE_ALL_POINTS_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cloud_box_type: CloudBoxType
    show_bounding_box: bool
    use_all_points: bool
    desired_point_count: int
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cloud_box_type: _Optional[_Union[CloudBoxType, str]] = ..., show_bounding_box: bool = ..., use_all_points: bool = ..., desired_point_count: _Optional[int] = ...) -> None: ...

class ResetCloudBoundingBoxResult(_message.Message):
    __slots__ = ("x_axis_dimension", "y_axis_dimension", "z_axis_dimension", "x_axis_in_world", "y_axis_in_world", "z_axis_in_world", "centroid_in_world", "reference_transform_in_world", "reference_transform_in_working", "points_used_for_bounding_box", "execution")
    X_AXIS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    Z_AXIS_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    X_AXIS_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    Z_AXIS_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    CENTROID_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRANSFORM_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    POINTS_USED_FOR_BOUNDING_BOX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x_axis_dimension: float
    y_axis_dimension: float
    z_axis_dimension: float
    x_axis_in_world: _spatial_analyzer_values_pb2.Vector
    y_axis_in_world: _spatial_analyzer_values_pb2.Vector
    z_axis_in_world: _spatial_analyzer_values_pb2.Vector
    centroid_in_world: _spatial_analyzer_values_pb2.Vector
    reference_transform_in_world: _spatial_analyzer_values_pb2.Transform
    reference_transform_in_working: _spatial_analyzer_values_pb2.Transform
    points_used_for_bounding_box: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x_axis_dimension: _Optional[float] = ..., y_axis_dimension: _Optional[float] = ..., z_axis_dimension: _Optional[float] = ..., x_axis_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., y_axis_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., z_axis_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., centroid_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., reference_transform_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., reference_transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., points_used_for_bounding_box: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCloudPointCountRequest(_message.Message):
    __slots__ = ("cloud_name",)
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetCloudPointCountResult(_message.Message):
    __slots__ = ("points_count", "planar_offset", "radial_offset", "active_clipping_planes", "execution")
    POINTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_OFFSET_FIELD_NUMBER: _ClassVar[int]
    RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLIPPING_PLANES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    points_count: int
    planar_offset: float
    radial_offset: float
    active_clipping_planes: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, points_count: _Optional[int] = ..., planar_offset: _Optional[float] = ..., radial_offset: _Optional[float] = ..., active_clipping_planes: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCloudDefaultClippingPlaneRequest(_message.Message):
    __slots__ = ("enable_cloud_clipping", "reference_object")
    ENABLE_CLOUD_CLIPPING_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    enable_cloud_clipping: bool
    reference_object: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, enable_cloud_clipping: bool = ..., reference_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetCloudDefaultClippingPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RasterScanEdgeInspectionRequest(_message.Message):
    __slots__ = ("cloud_names", "edge_surface_name", "b_spline_edge_list", "prefix_for_output_groups", "tolerance", "minimum_good_points_per_unit_length", "maximum_bad_points_percentage")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    EDGE_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_EDGE_LIST_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FOR_OUTPUT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_GOOD_POINTS_PER_UNIT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_BAD_POINTS_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    edge_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    b_spline_edge_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    prefix_for_output_groups: _spatial_analyzer_values_pb2.CollectionObjectName
    tolerance: float
    minimum_good_points_per_unit_length: int
    maximum_bad_points_percentage: float
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., edge_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., b_spline_edge_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., prefix_for_output_groups: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., tolerance: _Optional[float] = ..., minimum_good_points_per_unit_length: _Optional[int] = ..., maximum_bad_points_percentage: _Optional[float] = ...) -> None: ...

class RasterScanEdgeInspectionResult(_message.Message):
    __slots__ = ("summary_result", "execution")
    SUMMARY_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    summary_result: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, summary_result: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NewRasterScanEdgeInspectionRequest(_message.Message):
    __slots__ = ("edge_cloud_names", "edge_surface_name", "edge_b_spline_name", "output_prefix", "inspection_increment", "proximity_filter_distance", "edge_bias_value", "error_tolerance", "use_cosine_projection_method", "minimum_edge_points_per_segment", "intermediate_calculation_results_file")
    EDGE_CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    EDGE_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    EDGE_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    INSPECTION_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FILTER_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    EDGE_BIAS_VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_COSINE_PROJECTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_EDGE_POINTS_PER_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    INTERMEDIATE_CALCULATION_RESULTS_FILE_FIELD_NUMBER: _ClassVar[int]
    edge_cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    edge_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    edge_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    output_prefix: _spatial_analyzer_values_pb2.CollectionObjectName
    inspection_increment: float
    proximity_filter_distance: float
    edge_bias_value: float
    error_tolerance: float
    use_cosine_projection_method: bool
    minimum_edge_points_per_segment: int
    intermediate_calculation_results_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, edge_cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., edge_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., edge_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., output_prefix: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., inspection_increment: _Optional[float] = ..., proximity_filter_distance: _Optional[float] = ..., edge_bias_value: _Optional[float] = ..., error_tolerance: _Optional[float] = ..., use_cosine_projection_method: bool = ..., minimum_edge_points_per_segment: _Optional[int] = ..., intermediate_calculation_results_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class NewRasterScanEdgeInspectionResult(_message.Message):
    __slots__ = ("summary_result", "execution")
    SUMMARY_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    summary_result: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, summary_result: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearCloudPointDeviationsRequest(_message.Message):
    __slots__ = ("cloud_name",)
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ClearCloudPointDeviationsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableAllCloudCrossSectionsRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name",)
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class EnableAllCloudCrossSectionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableCloudCrossSectionsRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name", "cross_section_id", "enable")
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    CROSS_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cross_section_id: int
    enable: bool
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cross_section_id: _Optional[int] = ..., enable: bool = ...) -> None: ...

class EnableDisableCloudCrossSectionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableSingleCloudCrossSectionRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name", "cross_section_id")
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    CROSS_SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cross_section_id: int
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cross_section_id: _Optional[int] = ...) -> None: ...

class EnableSingleCloudCrossSectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfCrossSectionsInCrossSectionCloudRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name",)
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetNumberOfCrossSectionsInCrossSectionCloudResult(_message.Message):
    __slots__ = ("cross_section_count", "execution")
    CROSS_SECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    cross_section_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, cross_section_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToPlaneRequest(_message.Message):
    __slots__ = ("cloud_names", "filter_plane_name", "output_group_name", "proximity", "allowable_offset_direction", "output_type")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    ALLOWABLE_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    filter_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    proximity: float
    allowable_offset_direction: _spatial_analyzer_values_pb2.OffsetDirectionType
    output_type: PointOutputType
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., filter_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., proximity: _Optional[float] = ..., allowable_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ...) -> None: ...

class FilterCloudsToPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToGroupRequest(_message.Message):
    __slots__ = ("cloud_names", "filter_group_name", "output_group_name", "proximity", "maximum_number_of_points", "output_type")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_NUMBER_OF_POINTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    filter_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    proximity: float
    maximum_number_of_points: int
    output_type: PointOutputType
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., filter_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., proximity: _Optional[float] = ..., maximum_number_of_points: _Optional[int] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ...) -> None: ...

class FilterCloudsToGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToSurfaceRequest(_message.Message):
    __slots__ = ("cloud_names", "filter_surface_name", "output_group_name", "low_proximity", "high_proximity", "skip_factor", "output_type")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    LOW_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    HIGH_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FACTOR_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    filter_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    low_proximity: float
    high_proximity: float
    skip_factor: int
    output_type: PointOutputType
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., filter_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., low_proximity: _Optional[float] = ..., high_proximity: _Optional[float] = ..., skip_factor: _Optional[int] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ...) -> None: ...

class FilterCloudsToSurfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToBSplinesRequest(_message.Message):
    __slots__ = ("cloud_names", "filter_b_spline_names", "output_group_name", "minimum_proximity", "maximum_proximity", "output_type")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FILTER_B_SPLINE_NAMES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    filter_b_spline_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    minimum_proximity: float
    maximum_proximity: float
    output_type: PointOutputType
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., filter_b_spline_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., minimum_proximity: _Optional[float] = ..., maximum_proximity: _Optional[float] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ...) -> None: ...

class FilterCloudsToBSplinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToLineSegmentRequest(_message.Message):
    __slots__ = ("cloud_names", "first_line_end_point", "second_line_end_point", "output_group_name", "minimum_proximity", "maximum_proximity", "output_type")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    FIRST_LINE_END_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_LINE_END_POINT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    first_line_end_point: _spatial_analyzer_values_pb2.PointName
    second_line_end_point: _spatial_analyzer_values_pb2.PointName
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    minimum_proximity: float
    maximum_proximity: float
    output_type: PointOutputType
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., first_line_end_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_line_end_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., minimum_proximity: _Optional[float] = ..., maximum_proximity: _Optional[float] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ...) -> None: ...

class FilterCloudsToLineSegmentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToVectorGroupsResolvePointsRequest(_message.Message):
    __slots__ = ("cloud_names", "vector_group_names", "output_group_name", "minimum_proximity", "maximum_proximity", "maximum_distance_from_vector_begin", "minimum_number_of_required_points", "output_type", "include_proximity_points")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DISTANCE_FROM_VECTOR_BEGIN_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_NUMBER_OF_REQUIRED_POINTS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PROXIMITY_POINTS_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    vector_group_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    output_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    minimum_proximity: float
    maximum_proximity: float
    maximum_distance_from_vector_begin: float
    minimum_number_of_required_points: int
    output_type: PointOutputType
    include_proximity_points: bool
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., vector_group_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., output_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., minimum_proximity: _Optional[float] = ..., maximum_proximity: _Optional[float] = ..., maximum_distance_from_vector_begin: _Optional[float] = ..., minimum_number_of_required_points: _Optional[int] = ..., output_type: _Optional[_Union[PointOutputType, str]] = ..., include_proximity_points: bool = ...) -> None: ...

class FilterCloudsToVectorGroupsResolvePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterCloudsToVectorGroupsResolveCloudsRequest(_message.Message):
    __slots__ = ("cloud_names", "vector_group_names", "radial_cutoff", "lower_cutoff", "upper_cutoff", "output_collection_name")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    RADIAL_CUTOFF_FIELD_NUMBER: _ClassVar[int]
    LOWER_CUTOFF_FIELD_NUMBER: _ClassVar[int]
    UPPER_CUTOFF_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    vector_group_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    radial_cutoff: float
    lower_cutoff: float
    upper_cutoff: float
    output_collection_name: str
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., vector_group_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., radial_cutoff: _Optional[float] = ..., lower_cutoff: _Optional[float] = ..., upper_cutoff: _Optional[float] = ..., output_collection_name: _Optional[str] = ...) -> None: ...

class FilterCloudsToVectorGroupsResolveCloudsResult(_message.Message):
    __slots__ = ("filtered_clouds", "execution")
    FILTERED_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    filtered_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, filtered_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RGBCloudPointFilterRequest(_message.Message):
    __slots__ = ("filter_name", "clouds_to_be_filtered", "red_enabled", "red_high_enabled", "red_high_threshold", "red_low_enabled", "red_low_threshold", "green_enabled", "green_high_enabled", "green_high_threshold", "green_low_enabled", "green_low_threshold", "blue_enabled", "blue_high_enabled", "blue_high_threshold", "blue_low_enabled", "blue_low_threshold", "gray_scale_enabled", "gray_scale_high_enabled", "gray_scale_high_threshold", "gray_scale_low_enabled", "gray_scale_low_threshold", "rgb_filter_operation")
    FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUDS_TO_BE_FILTERED_FIELD_NUMBER: _ClassVar[int]
    RED_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RED_HIGH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RED_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RED_LOW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    RED_LOW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GREEN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GREEN_HIGH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GREEN_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GREEN_LOW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GREEN_LOW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BLUE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLUE_HIGH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLUE_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    BLUE_LOW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLUE_LOW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GRAY_SCALE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GRAY_SCALE_HIGH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GRAY_SCALE_HIGH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    GRAY_SCALE_LOW_ENABLED_FIELD_NUMBER: _ClassVar[int]
    GRAY_SCALE_LOW_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    RGB_FILTER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    filter_name: str
    clouds_to_be_filtered: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    red_enabled: bool
    red_high_enabled: bool
    red_high_threshold: int
    red_low_enabled: bool
    red_low_threshold: int
    green_enabled: bool
    green_high_enabled: bool
    green_high_threshold: int
    green_low_enabled: bool
    green_low_threshold: int
    blue_enabled: bool
    blue_high_enabled: bool
    blue_high_threshold: int
    blue_low_enabled: bool
    blue_low_threshold: int
    gray_scale_enabled: bool
    gray_scale_high_enabled: bool
    gray_scale_high_threshold: int
    gray_scale_low_enabled: bool
    gray_scale_low_threshold: int
    rgb_filter_operation: RGBFilterOperation
    def __init__(self, filter_name: _Optional[str] = ..., clouds_to_be_filtered: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., red_enabled: bool = ..., red_high_enabled: bool = ..., red_high_threshold: _Optional[int] = ..., red_low_enabled: bool = ..., red_low_threshold: _Optional[int] = ..., green_enabled: bool = ..., green_high_enabled: bool = ..., green_high_threshold: _Optional[int] = ..., green_low_enabled: bool = ..., green_low_threshold: _Optional[int] = ..., blue_enabled: bool = ..., blue_high_enabled: bool = ..., blue_high_threshold: _Optional[int] = ..., blue_low_enabled: bool = ..., blue_low_threshold: _Optional[int] = ..., gray_scale_enabled: bool = ..., gray_scale_high_enabled: bool = ..., gray_scale_high_threshold: _Optional[int] = ..., gray_scale_low_enabled: bool = ..., gray_scale_low_threshold: _Optional[int] = ..., rgb_filter_operation: _Optional[_Union[RGBFilterOperation, str]] = ...) -> None: ...

class RGBCloudPointFilterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCloudRGBValuesRequest(_message.Message):
    __slots__ = ("source_cloud_name", "rgb_color_channel")
    SOURCE_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    RGB_COLOR_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    source_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    rgb_color_channel: RGBColorChannel
    def __init__(self, source_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., rgb_color_channel: _Optional[_Union[RGBColorChannel, str]] = ...) -> None: ...

class GetCloudRGBValuesResult(_message.Message):
    __slots__ = ("low_value", "high_value", "average_value", "standard_deviation", "execution")
    LOW_VALUE_FIELD_NUMBER: _ClassVar[int]
    HIGH_VALUE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    low_value: int
    high_value: int
    average_value: int
    standard_deviation: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, low_value: _Optional[int] = ..., high_value: _Optional[int] = ..., average_value: _Optional[int] = ..., standard_deviation: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCloudRGBValuesNearPointRequest(_message.Message):
    __slots__ = ("source_cloud_name", "single_point", "diameter", "rgb_color_channel")
    SOURCE_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    SINGLE_POINT_FIELD_NUMBER: _ClassVar[int]
    DIAMETER_FIELD_NUMBER: _ClassVar[int]
    RGB_COLOR_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    source_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    single_point: _spatial_analyzer_values_pb2.PointName
    diameter: float
    rgb_color_channel: RGBColorChannel
    def __init__(self, source_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., single_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., diameter: _Optional[float] = ..., rgb_color_channel: _Optional[_Union[RGBColorChannel, str]] = ...) -> None: ...

class GetCloudRGBValuesNearPointResult(_message.Message):
    __slots__ = ("low_value", "high_value", "average_value", "standard_deviation", "execution")
    LOW_VALUE_FIELD_NUMBER: _ClassVar[int]
    HIGH_VALUE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    low_value: int
    high_value: int
    average_value: int
    standard_deviation: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, low_value: _Optional[int] = ..., high_value: _Optional[int] = ..., average_value: _Optional[int] = ..., standard_deviation: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SubdivideCloudByPointSpacingRequest(_message.Message):
    __slots__ = ("source_cloud_name", "point_spacing", "minimum_points_per_group", "new_cloud_name", "keep_all_groups")
    SOURCE_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_SPACING_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_POINTS_PER_GROUP_FIELD_NUMBER: _ClassVar[int]
    NEW_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALL_GROUPS_FIELD_NUMBER: _ClassVar[int]
    source_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_spacing: float
    minimum_points_per_group: int
    new_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    keep_all_groups: bool
    def __init__(self, source_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_spacing: _Optional[float] = ..., minimum_points_per_group: _Optional[int] = ..., new_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., keep_all_groups: bool = ...) -> None: ...

class SubdivideCloudByPointSpacingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCloudPointsByRadialDistanceFromPointsRequest(_message.Message):
    __slots__ = ("cloud_names", "points", "radius", "delete_inside")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    DELETE_INSIDE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    radius: float
    delete_inside: bool
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., radius: _Optional[float] = ..., delete_inside: bool = ...) -> None: ...

class DeleteCloudPointsByRadialDistanceFromPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCloudPointsByXYZRangeRequest(_message.Message):
    __slots__ = ("cloud_names", "x_min", "x_max", "y_min", "y_max", "z_min", "z_max", "delete_inside")
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    X_MIN_FIELD_NUMBER: _ClassVar[int]
    X_MAX_FIELD_NUMBER: _ClassVar[int]
    Y_MIN_FIELD_NUMBER: _ClassVar[int]
    Y_MAX_FIELD_NUMBER: _ClassVar[int]
    Z_MIN_FIELD_NUMBER: _ClassVar[int]
    Z_MAX_FIELD_NUMBER: _ClassVar[int]
    DELETE_INSIDE_FIELD_NUMBER: _ClassVar[int]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    z_min: float
    z_max: float
    delete_inside: bool
    def __init__(self, cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., x_min: _Optional[float] = ..., x_max: _Optional[float] = ..., y_min: _Optional[float] = ..., y_max: _Optional[float] = ..., z_min: _Optional[float] = ..., z_max: _Optional[float] = ..., delete_inside: bool = ...) -> None: ...

class DeleteCloudPointsByXYZRangeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GenerateGeneralMeshRequest(_message.Message):
    __slots__ = ("output_mesh_name", "clouds_to_mesh", "maximum_triangle_size", "smallest_hole_diameter", "finalize", "use_scan_direction_for_point_normal", "json_file")
    OUTPUT_MESH_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUDS_TO_MESH_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_TRIANGLE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SMALLEST_HOLE_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    FINALIZE_FIELD_NUMBER: _ClassVar[int]
    USE_SCAN_DIRECTION_FOR_POINT_NORMAL_FIELD_NUMBER: _ClassVar[int]
    JSON_FILE_FIELD_NUMBER: _ClassVar[int]
    output_mesh_name: _spatial_analyzer_values_pb2.CollectionObjectName
    clouds_to_mesh: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    maximum_triangle_size: float
    smallest_hole_diameter: float
    finalize: bool
    use_scan_direction_for_point_normal: bool
    json_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, output_mesh_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., clouds_to_mesh: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., maximum_triangle_size: _Optional[float] = ..., smallest_hole_diameter: _Optional[float] = ..., finalize: bool = ..., use_scan_direction_for_point_normal: bool = ..., json_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class GenerateGeneralMeshResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConsolidateMeshRequest(_message.Message):
    __slots__ = ("mesh",)
    MESH_FIELD_NUMBER: _ClassVar[int]
    mesh: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, mesh: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConsolidateMeshResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeshVolumeRequest(_message.Message):
    __slots__ = ("mesh", "plane")
    MESH_FIELD_NUMBER: _ClassVar[int]
    PLANE_FIELD_NUMBER: _ClassVar[int]
    mesh: _spatial_analyzer_values_pb2.CollectionObjectName
    plane: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, mesh: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MeshVolumeResult(_message.Message):
    __slots__ = ("above", "below", "execution")
    ABOVE_FIELD_NUMBER: _ClassVar[int]
    BELOW_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    above: float
    below: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, above: _Optional[float] = ..., below: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeshFillHolesRequest(_message.Message):
    __slots__ = ("mesh", "maximum_triangle_length", "tension", "unconditional_filling", "fill_all_holes")
    MESH_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_TRIANGLE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    TENSION_FIELD_NUMBER: _ClassVar[int]
    UNCONDITIONAL_FILLING_FIELD_NUMBER: _ClassVar[int]
    FILL_ALL_HOLES_FIELD_NUMBER: _ClassVar[int]
    mesh: _spatial_analyzer_values_pb2.CollectionObjectName
    maximum_triangle_length: float
    tension: float
    unconditional_filling: bool
    fill_all_holes: bool
    def __init__(self, mesh: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., maximum_triangle_length: _Optional[float] = ..., tension: _Optional[float] = ..., unconditional_filling: bool = ..., fill_all_holes: bool = ...) -> None: ...

class MeshFillHolesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
