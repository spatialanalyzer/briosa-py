from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BSplinePointSortMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    B_SPLINE_POINT_SORT_MODE_UNSPECIFIED: _ClassVar[BSplinePointSortMode]
    B_SPLINE_POINT_SORT_MODE_USE_SELECTION_ORDER: _ClassVar[BSplinePointSortMode]
    B_SPLINE_POINT_SORT_MODE_CLOSEST_NEIGHBORS_FROM_FIRST_SELECTION: _ClassVar[BSplinePointSortMode]
    B_SPLINE_POINT_SORT_MODE_CLOSEST_NEIGHBORS_IN_CURVE_DIRECTION: _ClassVar[BSplinePointSortMode]

class CircleLineMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CIRCLE_LINE_MODE_UNSPECIFIED: _ClassVar[CircleLineMode]
    CIRCLE_LINE_MODE_CIRCLE: _ClassVar[CircleLineMode]
    CIRCLE_LINE_MODE_LINE: _ClassVar[CircleLineMode]

class FrameConstructionMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAME_CONSTRUCTION_METHOD_UNSPECIFIED: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_X_XY: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_X_XZ: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_Y_YX: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_Y_YZ: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_Z_ZX: _ClassVar[FrameConstructionMethod]
    FRAME_CONSTRUCTION_METHOD_ORIGIN_X_ZY: _ClassVar[FrameConstructionMethod]

class AxisIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AXIS_IDENTIFIER_UNSPECIFIED: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_X: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_X: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_Y: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_Y: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_Z: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_Z: _ClassVar[AxisIdentifier]

class FrameAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAME_AXIS_UNSPECIFIED: _ClassVar[FrameAxis]
    FRAME_AXIS_X: _ClassVar[FrameAxis]
    FRAME_AXIS_Y: _ClassVar[FrameAxis]
    FRAME_AXIS_Z: _ClassVar[FrameAxis]

class SystemString(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYSTEM_STRING_UNSPECIFIED: _ClassVar[SystemString]
    SYSTEM_STRING_SA_VERSION: _ClassVar[SystemString]
    SYSTEM_STRING_XIT_FILENAME: _ClassVar[SystemString]
    SYSTEM_STRING_MP_FILENAME: _ClassVar[SystemString]
    SYSTEM_STRING_MP_FILENAME_FULL_PATH: _ClassVar[SystemString]
    SYSTEM_STRING_DATE_AND_TIME: _ClassVar[SystemString]
    SYSTEM_STRING_DATE: _ClassVar[SystemString]
    SYSTEM_STRING_DATE_SHORT: _ClassVar[SystemString]
    SYSTEM_STRING_TIME: _ClassVar[SystemString]
    SYSTEM_STRING_KEY_SERIAL_NUMBER: _ClassVar[SystemString]
    SYSTEM_STRING_COMPANY_NAME: _ClassVar[SystemString]
    SYSTEM_STRING_USER_NAME: _ClassVar[SystemString]

class SurveyTargetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SURVEY_TARGET_TYPE_UNSPECIFIED: _ClassVar[SurveyTargetType]
    SURVEY_TARGET_TYPE_TRIANGLE: _ClassVar[SurveyTargetType]
    SURVEY_TARGET_TYPE_CIRCLE: _ClassVar[SurveyTargetType]

class WcfAxis(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WCF_AXIS_UNSPECIFIED: _ClassVar[WcfAxis]
    WCF_AXIS_X: _ClassVar[WcfAxis]
    WCF_AXIS_Y: _ClassVar[WcfAxis]
    WCF_AXIS_Z: _ClassVar[WcfAxis]

class EdgePointMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDGE_POINT_MODE_UNSPECIFIED: _ClassVar[EdgePointMode]
    EDGE_POINT_MODE_INCLUDE_EDGES: _ClassVar[EdgePointMode]
    EDGE_POINT_MODE_EXCLUDE_EDGES: _ClassVar[EdgePointMode]
    EDGE_POINT_MODE_EDGES_ONLY: _ClassVar[EdgePointMode]

class MeshOrientationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESH_ORIENTATION_TYPE_UNSPECIFIED: _ClassVar[MeshOrientationType]
    MESH_ORIENTATION_TYPE_USE_CURRENT_POINT_OF_VIEW: _ClassVar[MeshOrientationType]
    MESH_ORIENTATION_TYPE_USE_CURRENT_WORKING_FRAME: _ClassVar[MeshOrientationType]

class SurfaceDissectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SURFACE_DISSECTION_MODE_UNSPECIFIED: _ClassVar[SurfaceDissectionMode]
    SURFACE_DISSECTION_MODE_ENTIRE_SOLID: _ClassVar[SurfaceDissectionMode]
    SURFACE_DISSECTION_MODE_SELECT_FACES: _ClassVar[SurfaceDissectionMode]

class MirrorFramePlane(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MIRROR_FRAME_PLANE_UNSPECIFIED: _ClassVar[MirrorFramePlane]
    MIRROR_FRAME_PLANE_XY: _ClassVar[MirrorFramePlane]
    MIRROR_FRAME_PLANE_XZ: _ClassVar[MirrorFramePlane]
    MIRROR_FRAME_PLANE_YZ: _ClassVar[MirrorFramePlane]

class ConstructObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONSTRUCT_OBJECT_TYPE_UNSPECIFIED: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_ANY: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_CIRCLES: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_CONES: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_CYLINDERS: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_LINES: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_PLANES: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_SLOTS: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_SPHERES: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_CENTER_POINTS: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_SURFACE_POINTS: _ClassVar[ConstructObjectType]
    CONSTRUCT_OBJECT_TYPE_VERTEX_POINTS: _ClassVar[ConstructObjectType]
B_SPLINE_POINT_SORT_MODE_UNSPECIFIED: BSplinePointSortMode
B_SPLINE_POINT_SORT_MODE_USE_SELECTION_ORDER: BSplinePointSortMode
B_SPLINE_POINT_SORT_MODE_CLOSEST_NEIGHBORS_FROM_FIRST_SELECTION: BSplinePointSortMode
B_SPLINE_POINT_SORT_MODE_CLOSEST_NEIGHBORS_IN_CURVE_DIRECTION: BSplinePointSortMode
CIRCLE_LINE_MODE_UNSPECIFIED: CircleLineMode
CIRCLE_LINE_MODE_CIRCLE: CircleLineMode
CIRCLE_LINE_MODE_LINE: CircleLineMode
FRAME_CONSTRUCTION_METHOD_UNSPECIFIED: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_X_XY: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_X_XZ: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_Y_YX: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_Y_YZ: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_Z_ZX: FrameConstructionMethod
FRAME_CONSTRUCTION_METHOD_ORIGIN_X_ZY: FrameConstructionMethod
AXIS_IDENTIFIER_UNSPECIFIED: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_X: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_X: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_Y: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_Y: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_Z: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_Z: AxisIdentifier
FRAME_AXIS_UNSPECIFIED: FrameAxis
FRAME_AXIS_X: FrameAxis
FRAME_AXIS_Y: FrameAxis
FRAME_AXIS_Z: FrameAxis
SYSTEM_STRING_UNSPECIFIED: SystemString
SYSTEM_STRING_SA_VERSION: SystemString
SYSTEM_STRING_XIT_FILENAME: SystemString
SYSTEM_STRING_MP_FILENAME: SystemString
SYSTEM_STRING_MP_FILENAME_FULL_PATH: SystemString
SYSTEM_STRING_DATE_AND_TIME: SystemString
SYSTEM_STRING_DATE: SystemString
SYSTEM_STRING_DATE_SHORT: SystemString
SYSTEM_STRING_TIME: SystemString
SYSTEM_STRING_KEY_SERIAL_NUMBER: SystemString
SYSTEM_STRING_COMPANY_NAME: SystemString
SYSTEM_STRING_USER_NAME: SystemString
SURVEY_TARGET_TYPE_UNSPECIFIED: SurveyTargetType
SURVEY_TARGET_TYPE_TRIANGLE: SurveyTargetType
SURVEY_TARGET_TYPE_CIRCLE: SurveyTargetType
WCF_AXIS_UNSPECIFIED: WcfAxis
WCF_AXIS_X: WcfAxis
WCF_AXIS_Y: WcfAxis
WCF_AXIS_Z: WcfAxis
EDGE_POINT_MODE_UNSPECIFIED: EdgePointMode
EDGE_POINT_MODE_INCLUDE_EDGES: EdgePointMode
EDGE_POINT_MODE_EXCLUDE_EDGES: EdgePointMode
EDGE_POINT_MODE_EDGES_ONLY: EdgePointMode
MESH_ORIENTATION_TYPE_UNSPECIFIED: MeshOrientationType
MESH_ORIENTATION_TYPE_USE_CURRENT_POINT_OF_VIEW: MeshOrientationType
MESH_ORIENTATION_TYPE_USE_CURRENT_WORKING_FRAME: MeshOrientationType
SURFACE_DISSECTION_MODE_UNSPECIFIED: SurfaceDissectionMode
SURFACE_DISSECTION_MODE_ENTIRE_SOLID: SurfaceDissectionMode
SURFACE_DISSECTION_MODE_SELECT_FACES: SurfaceDissectionMode
MIRROR_FRAME_PLANE_UNSPECIFIED: MirrorFramePlane
MIRROR_FRAME_PLANE_XY: MirrorFramePlane
MIRROR_FRAME_PLANE_XZ: MirrorFramePlane
MIRROR_FRAME_PLANE_YZ: MirrorFramePlane
CONSTRUCT_OBJECT_TYPE_UNSPECIFIED: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_ANY: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_CIRCLES: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_CONES: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_CYLINDERS: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_LINES: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_PLANES: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_SLOTS: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_SPHERES: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_CENTER_POINTS: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_SURFACE_POINTS: ConstructObjectType
CONSTRUCT_OBJECT_TYPE_VERTEX_POINTS: ConstructObjectType

class GetActiveCollectionNameRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActiveCollectionNameResult(_message.Message):
    __slots__ = ("currently_active_collection_name", "execution")
    CURRENTLY_ACTIVE_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    currently_active_collection_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, currently_active_collection_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCirclesFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructCirclesFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructConesFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructConesFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCylindersFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructCylindersFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateVectorCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "vector_group_name", "vector_name", "view_x_position", "view_y_position", "show_collection", "show_vector_group", "show_vector_name", "show_dx", "show_dy", "show_dz", "show_d_mag", "show_tolerance_color", "show_out_of_tolerance_value", "show_tolerance_range", "show_vector_color", "show_start_point", "show_end_point", "show_units", "additional_notes", "attach_callout_to_end_point", "use_default_placement")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_DX_FIELD_NUMBER: _ClassVar[int]
    SHOW_DY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DZ_FIELD_NUMBER: _ClassVar[int]
    SHOW_D_MAG_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOLERANCE_COLOR_FIELD_NUMBER: _ClassVar[int]
    SHOW_OUT_OF_TOLERANCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOLERANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_COLOR_FIELD_NUMBER: _ClassVar[int]
    SHOW_START_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_END_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_UNITS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NOTES_FIELD_NUMBER: _ClassVar[int]
    ATTACH_CALLOUT_TO_END_POINT_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_name: str
    view_x_position: float
    view_y_position: float
    show_collection: bool
    show_vector_group: bool
    show_vector_name: bool
    show_dx: bool
    show_dy: bool
    show_dz: bool
    show_d_mag: bool
    show_tolerance_color: bool
    show_out_of_tolerance_value: bool
    show_tolerance_range: bool
    show_vector_color: bool
    show_start_point: bool
    show_end_point: bool
    show_units: bool
    additional_notes: _containers.RepeatedScalarFieldContainer[str]
    attach_callout_to_end_point: bool
    use_default_placement: bool
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_name: _Optional[str] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., show_collection: bool = ..., show_vector_group: bool = ..., show_vector_name: bool = ..., show_dx: bool = ..., show_dy: bool = ..., show_dz: bool = ..., show_d_mag: bool = ..., show_tolerance_color: bool = ..., show_out_of_tolerance_value: bool = ..., show_tolerance_range: bool = ..., show_vector_color: bool = ..., show_start_point: bool = ..., show_end_point: bool = ..., show_units: bool = ..., additional_notes: _Optional[_Iterable[str]] = ..., attach_callout_to_end_point: bool = ..., use_default_placement: bool = ...) -> None: ...

class CreateVectorCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateMinMaxVectorGroupCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "vector_group_name", "number_of_vectors_with_highest_mag", "number_of_vectors_with_lowest_mag", "show_collection", "show_vector_group", "show_vector_name", "show_dx", "show_dy", "show_dz", "show_d_mag", "show_tolerance_color", "tolerance_color_blue_green_red", "show_out_of_tolerance_value", "show_tolerance_range", "show_vector_color", "show_start_point", "show_end_point", "show_units", "attach_callout_to_end_point", "use_default_placement")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_VECTORS_WITH_HIGHEST_MAG_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_VECTORS_WITH_LOWEST_MAG_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_DX_FIELD_NUMBER: _ClassVar[int]
    SHOW_DY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DZ_FIELD_NUMBER: _ClassVar[int]
    SHOW_D_MAG_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOLERANCE_COLOR_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_COLOR_BLUE_GREEN_RED_FIELD_NUMBER: _ClassVar[int]
    SHOW_OUT_OF_TOLERANCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOLERANCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    SHOW_VECTOR_COLOR_FIELD_NUMBER: _ClassVar[int]
    SHOW_START_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_END_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_UNITS_FIELD_NUMBER: _ClassVar[int]
    ATTACH_CALLOUT_TO_END_POINT_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    number_of_vectors_with_highest_mag: int
    number_of_vectors_with_lowest_mag: int
    show_collection: bool
    show_vector_group: bool
    show_vector_name: bool
    show_dx: bool
    show_dy: bool
    show_dz: bool
    show_d_mag: bool
    show_tolerance_color: bool
    tolerance_color_blue_green_red: bool
    show_out_of_tolerance_value: bool
    show_tolerance_range: bool
    show_vector_color: bool
    show_start_point: bool
    show_end_point: bool
    show_units: bool
    attach_callout_to_end_point: bool
    use_default_placement: bool
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., number_of_vectors_with_highest_mag: _Optional[int] = ..., number_of_vectors_with_lowest_mag: _Optional[int] = ..., show_collection: bool = ..., show_vector_group: bool = ..., show_vector_name: bool = ..., show_dx: bool = ..., show_dy: bool = ..., show_dz: bool = ..., show_d_mag: bool = ..., show_tolerance_color: bool = ..., tolerance_color_blue_green_red: bool = ..., show_out_of_tolerance_value: bool = ..., show_tolerance_range: bool = ..., show_vector_color: bool = ..., show_start_point: bool = ..., show_end_point: bool = ..., show_units: bool = ..., attach_callout_to_end_point: bool = ..., use_default_placement: bool = ...) -> None: ...

class CreateMinMaxVectorGroupCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePointCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "point", "view_x_position", "view_y_position", "show_point_collection", "show_point_group", "show_point_target", "show_x", "show_y", "show_z", "show_units", "show_ux", "show_uy", "show_uz", "show_umag", "desired_coordinate_system", "notes", "use_default_placement")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_TARGET_FIELD_NUMBER: _ClassVar[int]
    SHOW_X_FIELD_NUMBER: _ClassVar[int]
    SHOW_Y_FIELD_NUMBER: _ClassVar[int]
    SHOW_Z_FIELD_NUMBER: _ClassVar[int]
    SHOW_UNITS_FIELD_NUMBER: _ClassVar[int]
    SHOW_UX_FIELD_NUMBER: _ClassVar[int]
    SHOW_UY_FIELD_NUMBER: _ClassVar[int]
    SHOW_UZ_FIELD_NUMBER: _ClassVar[int]
    SHOW_UMAG_FIELD_NUMBER: _ClassVar[int]
    DESIRED_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    point: _spatial_analyzer_values_pb2.PointName
    view_x_position: float
    view_y_position: float
    show_point_collection: bool
    show_point_group: bool
    show_point_target: bool
    show_x: bool
    show_y: bool
    show_z: bool
    show_units: bool
    show_ux: bool
    show_uy: bool
    show_uz: bool
    show_umag: bool
    desired_coordinate_system: _spatial_analyzer_values_pb2.CoordinateSystemType
    notes: _containers.RepeatedScalarFieldContainer[str]
    use_default_placement: bool
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., show_point_collection: bool = ..., show_point_group: bool = ..., show_point_target: bool = ..., show_x: bool = ..., show_y: bool = ..., show_z: bool = ..., show_units: bool = ..., show_ux: bool = ..., show_uy: bool = ..., show_uz: bool = ..., show_umag: bool = ..., desired_coordinate_system: _Optional[_Union[_spatial_analyzer_values_pb2.CoordinateSystemType, str]] = ..., notes: _Optional[_Iterable[str]] = ..., use_default_placement: bool = ...) -> None: ...

class CreatePointCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePointComparisonCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "first_point", "second_point", "view_x_position", "view_y_position", "show_first_point_collection", "show_first_point_group", "show_first_point_target", "show_first_point_coordinates", "show_second_point_collection", "show_second_point_group", "show_second_point_target", "show_second_point_coordinates", "show_dx", "show_dy", "show_dz", "show_d_mag", "additional_x_comments", "additional_y_comments", "additional_z_comments", "additional_notes", "use_default_placement")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    FIRST_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_POINT_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIRST_POINT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIRST_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIRST_POINT_TARGET_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIRST_POINT_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    SHOW_SECOND_POINT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    SHOW_SECOND_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_SECOND_POINT_TARGET_FIELD_NUMBER: _ClassVar[int]
    SHOW_SECOND_POINT_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    SHOW_DX_FIELD_NUMBER: _ClassVar[int]
    SHOW_DY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DZ_FIELD_NUMBER: _ClassVar[int]
    SHOW_D_MAG_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_X_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_Y_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_Z_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NOTES_FIELD_NUMBER: _ClassVar[int]
    USE_DEFAULT_PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    first_point: _spatial_analyzer_values_pb2.PointName
    second_point: _spatial_analyzer_values_pb2.PointName
    view_x_position: float
    view_y_position: float
    show_first_point_collection: bool
    show_first_point_group: bool
    show_first_point_target: bool
    show_first_point_coordinates: bool
    show_second_point_collection: bool
    show_second_point_group: bool
    show_second_point_target: bool
    show_second_point_coordinates: bool
    show_dx: bool
    show_dy: bool
    show_dz: bool
    show_d_mag: bool
    additional_x_comments: str
    additional_y_comments: str
    additional_z_comments: str
    additional_notes: _containers.RepeatedScalarFieldContainer[str]
    use_default_placement: bool
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., first_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., show_first_point_collection: bool = ..., show_first_point_group: bool = ..., show_first_point_target: bool = ..., show_first_point_coordinates: bool = ..., show_second_point_collection: bool = ..., show_second_point_group: bool = ..., show_second_point_target: bool = ..., show_second_point_coordinates: bool = ..., show_dx: bool = ..., show_dy: bool = ..., show_dz: bool = ..., show_d_mag: bool = ..., additional_x_comments: _Optional[str] = ..., additional_y_comments: _Optional[str] = ..., additional_z_comments: _Optional[str] = ..., additional_notes: _Optional[_Iterable[str]] = ..., use_default_placement: bool = ...) -> None: ...

class CreatePointComparisonCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateRelationshipCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "relationship_name", "view_x_position", "view_y_position", "additional_notes")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_NOTES_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    view_x_position: float
    view_y_position: float
    additional_notes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., additional_notes: _Optional[_Iterable[str]] = ...) -> None: ...

class CreateRelationshipCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePictureCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "picture_name", "view_x_position", "view_y_position", "scale_image_percent", "object_for_callout_anchor_point")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    SCALE_IMAGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FOR_CALLOUT_ANCHOR_POINT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    view_x_position: float
    view_y_position: float
    scale_image_percent: int
    object_for_callout_anchor_point: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., scale_image_percent: _Optional[int] = ..., object_for_callout_anchor_point: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class CreatePictureCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateTextCalloutRequest(_message.Message):
    __slots__ = ("destination_callout_view", "text", "view_x_position", "view_y_position", "callout_anchor_point")
    DESTINATION_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIEW_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    VIEW_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_ANCHOR_POINT_FIELD_NUMBER: _ClassVar[int]
    destination_callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    text: _containers.RepeatedScalarFieldContainer[str]
    view_x_position: float
    view_y_position: float
    callout_anchor_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, destination_callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., text: _Optional[_Iterable[str]] = ..., view_x_position: _Optional[float] = ..., view_y_position: _Optional[float] = ..., callout_anchor_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class CreateTextCalloutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDefaultCalloutViewPropertiesRequest(_message.Message):
    __slots__ = ("default_callout_view_name", "properties")
    DEFAULT_CALLOUT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    default_callout_view_name: str
    properties: CalloutViewProperties
    def __init__(self, default_callout_view_name: _Optional[str] = ..., properties: _Optional[_Union[CalloutViewProperties, _Mapping]] = ...) -> None: ...

class SetDefaultCalloutViewPropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalloutViewPropertiesRequest(_message.Message):
    __slots__ = ("callout_views", "properties")
    CALLOUT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    callout_views: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    properties: CalloutViewProperties
    def __init__(self, callout_views: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., properties: _Optional[_Union[CalloutViewProperties, _Mapping]] = ...) -> None: ...

class SetCalloutViewPropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view",)
    CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class DeleteCalloutViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameCalloutViewRequest(_message.Message):
    __slots__ = ("original_callout_view_name", "new_callout_view_name", "overwrite_if_exists")
    ORIGINAL_CALLOUT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_CALLOUT_VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_callout_view_name: _spatial_analyzer_values_pb2.CollectionItemName
    new_callout_view_name: _spatial_analyzer_values_pb2.CollectionItemName
    overwrite_if_exists: bool
    def __init__(self, original_callout_view_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., new_callout_view_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenameCalloutViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoArrangeCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view",)
    CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class AutoArrangeCalloutViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfCalloutsInCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view",)
    CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetNumberOfCalloutsInCalloutViewResult(_message.Message):
    __slots__ = ("callouts_count", "execution")
    CALLOUTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    callouts_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, callouts_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthCalloutPositionInCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view", "callout_view_index")
    CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
    callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    callout_view_index: int
    def __init__(self, callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., callout_view_index: _Optional[int] = ...) -> None: ...

class GetIthCalloutPositionInCalloutViewResult(_message.Message):
    __slots__ = ("x_position", "y_position", "x_anchor_position", "y_anchor_position", "callout_width", "callout_height", "execution")
    X_POSITION_FIELD_NUMBER: _ClassVar[int]
    Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    X_ANCHOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    Y_ANCHOR_POSITION_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_WIDTH_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x_position: int
    y_position: int
    x_anchor_position: int
    y_anchor_position: int
    callout_width: int
    callout_height: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x_position: _Optional[int] = ..., y_position: _Optional[int] = ..., x_anchor_position: _Optional[int] = ..., y_anchor_position: _Optional[int] = ..., callout_width: _Optional[int] = ..., callout_height: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetIthCalloutPositionInCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view", "callout_view_index", "x_position", "y_position")
    CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_VIEW_INDEX_FIELD_NUMBER: _ClassVar[int]
    X_POSITION_FIELD_NUMBER: _ClassVar[int]
    Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    callout_view: _spatial_analyzer_values_pb2.CollectionItemName
    callout_view_index: int
    x_position: int
    y_position: int
    def __init__(self, callout_view: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., callout_view_index: _Optional[int] = ..., x_position: _Optional[int] = ..., y_position: _Optional[int] = ...) -> None: ...

class SetIthCalloutPositionInCalloutViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class BSplineFitOptions(_message.Message):
    __slots__ = ("open_curve", "use_interpolation_for_fit", "number_of_control_points", "degree_of_curve", "sort_method", "span_any_gap", "termination_gap_length", "ignore_proximate_points", "proximate_point_threshold", "use_global_tessellation_options", "maximum_chordal_deviation", "maximum_trim_edge_angle", "termination_average_multiplier", "extension")
    OPEN_CURVE_FIELD_NUMBER: _ClassVar[int]
    USE_INTERPOLATION_FOR_FIT_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_CONTROL_POINTS_FIELD_NUMBER: _ClassVar[int]
    DEGREE_OF_CURVE_FIELD_NUMBER: _ClassVar[int]
    SORT_METHOD_FIELD_NUMBER: _ClassVar[int]
    SPAN_ANY_GAP_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_GAP_LENGTH_FIELD_NUMBER: _ClassVar[int]
    IGNORE_PROXIMATE_POINTS_FIELD_NUMBER: _ClassVar[int]
    PROXIMATE_POINT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    USE_GLOBAL_TESSELLATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_CHORDAL_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_TRIM_EDGE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_AVERAGE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    EXTENSION_FIELD_NUMBER: _ClassVar[int]
    open_curve: bool
    use_interpolation_for_fit: bool
    number_of_control_points: int
    degree_of_curve: int
    sort_method: BSplinePointSortMode
    span_any_gap: bool
    termination_gap_length: float
    ignore_proximate_points: bool
    proximate_point_threshold: float
    use_global_tessellation_options: bool
    maximum_chordal_deviation: float
    maximum_trim_edge_angle: float
    termination_average_multiplier: float
    extension: float
    def __init__(self, open_curve: bool = ..., use_interpolation_for_fit: bool = ..., number_of_control_points: _Optional[int] = ..., degree_of_curve: _Optional[int] = ..., sort_method: _Optional[_Union[BSplinePointSortMode, str]] = ..., span_any_gap: bool = ..., termination_gap_length: _Optional[float] = ..., ignore_proximate_points: bool = ..., proximate_point_threshold: _Optional[float] = ..., use_global_tessellation_options: bool = ..., maximum_chordal_deviation: _Optional[float] = ..., maximum_trim_edge_angle: _Optional[float] = ..., termination_average_multiplier: _Optional[float] = ..., extension: _Optional[float] = ...) -> None: ...

class ConstructBSplineFromPointsRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "b_spline_fit_options", "point_list")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_FIT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    b_spline_fit_options: BSplineFitOptions
    point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., b_spline_fit_options: _Optional[_Union[BSplineFitOptions, _Mapping]] = ..., point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class ConstructBSplineFromPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplineFromPointSetRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "b_spline_fit_options", "point_set_container")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_FIT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    POINT_SET_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    b_spline_fit_options: BSplineFitOptions
    point_set_container: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., b_spline_fit_options: _Optional[_Union[BSplineFitOptions, _Mapping]] = ..., point_set_container: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructBSplineFromPointSetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplineFromSeveralBSplinesRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "b_spline_list", "close_resulting_b_spline")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    CLOSE_RESULTING_B_SPLINE_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    close_resulting_b_spline: bool
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., close_resulting_b_spline: bool = ...) -> None: ...

class ConstructBSplineFromSeveralBSplinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplineFromIntersectionOfPlaneAndSurfaceRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "plane_name", "surface_name", "approximation_tolerance")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    approximation_tolerance: float
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., approximation_tolerance: _Optional[float] = ...) -> None: ...

class ConstructBSplineFromIntersectionOfPlaneAndSurfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplineFromIntersectionOfSurfacesRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "first_surface_name", "second_surface_name", "approximation_tolerance")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    first_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    second_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    approximation_tolerance: float
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., approximation_tolerance: _Optional[float] = ...) -> None: ...

class ConstructBSplineFromIntersectionOfSurfacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplinesFromSurfacesRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name_prefix", "surface_list")
    RESULTING_B_SPLINE_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name_prefix: str
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, resulting_b_spline_name_prefix: _Optional[str] = ..., surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ConstructBSplinesFromSurfacesResult(_message.Message):
    __slots__ = ("b_spline_list", "execution")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplinesFromLinesRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name_prefix", "line_list")
    RESULTING_B_SPLINE_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    LINE_LIST_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name_prefix: str
    line_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, resulting_b_spline_name_prefix: _Optional[str] = ..., line_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ConstructBSplinesFromLinesResult(_message.Message):
    __slots__ = ("b_spline_list", "execution")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBSplinesFromIntersectionOfPlaneAndMeshRequest(_message.Message):
    __slots__ = ("resulting_b_spline_name", "plane_name", "mesh_name", "closed_line_segment_limit", "unclosed_line_segment_limit", "create_intersection_points")
    RESULTING_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    MESH_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOSED_LINE_SEGMENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    UNCLOSED_LINE_SEGMENT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CREATE_INTERSECTION_POINTS_FIELD_NUMBER: _ClassVar[int]
    resulting_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    mesh_name: _spatial_analyzer_values_pb2.CollectionObjectName
    closed_line_segment_limit: int
    unclosed_line_segment_limit: int
    create_intersection_points: bool
    def __init__(self, resulting_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., mesh_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., closed_line_segment_limit: _Optional[int] = ..., unclosed_line_segment_limit: _Optional[int] = ..., create_intersection_points: bool = ...) -> None: ...

class ConstructBSplinesFromIntersectionOfPlaneAndMeshResult(_message.Message):
    __slots__ = ("b_spline_list", "execution")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CalloutViewProperties(_message.Message):
    __slots__ = ("lock_view_point", "recall_working_frame", "recall_visible_layer", "callout_leader_thickness", "callout_leader_color", "callout_border_thickness", "callout_border_color", "divide_text_with_lines", "font")
    LOCK_VIEW_POINT_FIELD_NUMBER: _ClassVar[int]
    RECALL_WORKING_FRAME_FIELD_NUMBER: _ClassVar[int]
    RECALL_VISIBLE_LAYER_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_LEADER_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_LEADER_COLOR_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_BORDER_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_BORDER_COLOR_FIELD_NUMBER: _ClassVar[int]
    DIVIDE_TEXT_WITH_LINES_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    lock_view_point: bool
    recall_working_frame: bool
    recall_visible_layer: bool
    callout_leader_thickness: int
    callout_leader_color: _spatial_analyzer_values_pb2.Color
    callout_border_thickness: int
    callout_border_color: _spatial_analyzer_values_pb2.Color
    divide_text_with_lines: bool
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, lock_view_point: bool = ..., recall_working_frame: bool = ..., recall_visible_layer: bool = ..., callout_leader_thickness: _Optional[int] = ..., callout_leader_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., callout_border_thickness: _Optional[int] = ..., callout_border_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., divide_text_with_lines: bool = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class MakeCalloutViewRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "callout_view_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_VIEW_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    callout_view_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., callout_view_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakeCalloutViewRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("callout_views", "execution")
    CALLOUT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    callout_views: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, callout_views: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCircleRequest(_message.Message):
    __slots__ = ("circle_name", "circle_center", "circle_normal", "circle_radius")
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_CENTER_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_NORMAL_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    circle_center: _spatial_analyzer_values_pb2.Vector
    circle_normal: _spatial_analyzer_values_pb2.Vector
    circle_radius: float
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., circle_center: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., circle_normal: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., circle_radius: _Optional[float] = ...) -> None: ...

class ConstructCircleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCirclesLinesFromSurfacesRequest(_message.Message):
    __slots__ = ("surfaces", "minimum_diameter", "maximum_diameter", "tolerance", "single_surface", "circle_line_mode", "destination_collection_name", "base_name")
    SURFACES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    SINGLE_SURFACE_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_LINE_MODE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FIELD_NUMBER: _ClassVar[int]
    surfaces: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    minimum_diameter: float
    maximum_diameter: float
    tolerance: float
    single_surface: bool
    circle_line_mode: CircleLineMode
    destination_collection_name: _spatial_analyzer_values_pb2.CollectionName
    base_name: str
    def __init__(self, surfaces: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., minimum_diameter: _Optional[float] = ..., maximum_diameter: _Optional[float] = ..., tolerance: _Optional[float] = ..., single_surface: bool = ..., circle_line_mode: _Optional[_Union[CircleLineMode, str]] = ..., destination_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., base_name: _Optional[str] = ...) -> None: ...

class ConstructCirclesLinesFromSurfacesResult(_message.Message):
    __slots__ = ("geometry_objects", "execution")
    GEOMETRY_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    geometry_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, geometry_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOrConstructDefaultCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class SetOrConstructDefaultCollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCollectionRequest(_message.Message):
    __slots__ = ("collection_name", "folder_path", "make_default_collection")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    MAKE_DEFAULT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    folder_path: str
    make_default_collection: bool
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., folder_path: _Optional[str] = ..., make_default_collection: bool = ...) -> None: ...

class ConstructCollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class DeleteCollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCollectionsByWildcardRequest(_message.Message):
    __slots__ = ("search_string", "case_sensitive_search", "allow_deleting_all_collections")
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DELETING_ALL_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    case_sensitive_search: bool
    allow_deleting_all_collections: bool
    def __init__(self, search_string: _Optional[str] = ..., case_sensitive_search: bool = ..., allow_deleting_all_collections: bool = ...) -> None: ...

class DeleteCollectionsByWildcardResult(_message.Message):
    __slots__ = ("num_deleted", "num_failed", "execution")
    NUM_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    num_deleted: int
    num_failed: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, num_deleted: _Optional[int] = ..., num_failed: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructConeRequest(_message.Message):
    __slots__ = ("cone_name", "cone_end_point", "cone_axis", "cone_length", "cone_theta_start", "cone_theta_span", "cone_included_angle")
    CONE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONE_END_POINT_FIELD_NUMBER: _ClassVar[int]
    CONE_AXIS_FIELD_NUMBER: _ClassVar[int]
    CONE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_START_FIELD_NUMBER: _ClassVar[int]
    CONE_THETA_SPAN_FIELD_NUMBER: _ClassVar[int]
    CONE_INCLUDED_ANGLE_FIELD_NUMBER: _ClassVar[int]
    cone_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cone_end_point: _spatial_analyzer_values_pb2.Vector
    cone_axis: _spatial_analyzer_values_pb2.Vector
    cone_length: float
    cone_theta_start: float
    cone_theta_span: float
    cone_included_angle: float
    def __init__(self, cone_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cone_end_point: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_axis: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cone_length: _Optional[float] = ..., cone_theta_start: _Optional[float] = ..., cone_theta_span: _Optional[float] = ..., cone_included_angle: _Optional[float] = ...) -> None: ...

class ConstructConeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCylinderRequest(_message.Message):
    __slots__ = ("cylinder_name", "cylinder_end_point", "cylinder_axis", "cylinder_diameter", "cylinder_length")
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_END_POINT_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_AXIS_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cylinder_end_point: _spatial_analyzer_values_pb2.Vector
    cylinder_axis: _spatial_analyzer_values_pb2.Vector
    cylinder_diameter: float
    cylinder_length: float
    def __init__(self, cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cylinder_end_point: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cylinder_axis: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cylinder_diameter: _Optional[float] = ..., cylinder_length: _Optional[float] = ...) -> None: ...

class ConstructCylinderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCylinderFromEndPointsRequest(_message.Message):
    __slots__ = ("cylinder_name", "cylinder_end_point_a", "cylinder_end_point_b", "cylinder_diameter")
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_END_POINT_A_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_END_POINT_B_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cylinder_end_point_a: _spatial_analyzer_values_pb2.Vector
    cylinder_end_point_b: _spatial_analyzer_values_pb2.Vector
    cylinder_diameter: float
    def __init__(self, cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cylinder_end_point_a: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cylinder_end_point_b: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., cylinder_diameter: _Optional[float] = ...) -> None: ...

class ConstructCylinderFromEndPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructEllipsoidRequest(_message.Message):
    __slots__ = ("ellipse_name", "x_axis_radius", "y_axis_radius", "z_axis_radius", "magnification", "uncertainty_ellipsoid", "transform_in_working_coordinates", "ellipse_color")
    ELLIPSE_NAME_FIELD_NUMBER: _ClassVar[int]
    X_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    Z_AXIS_RADIUS_FIELD_NUMBER: _ClassVar[int]
    MAGNIFICATION_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTY_ELLIPSOID_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    ELLIPSE_COLOR_FIELD_NUMBER: _ClassVar[int]
    ellipse_name: _spatial_analyzer_values_pb2.CollectionObjectName
    x_axis_radius: float
    y_axis_radius: float
    z_axis_radius: float
    magnification: float
    uncertainty_ellipsoid: bool
    transform_in_working_coordinates: _spatial_analyzer_values_pb2.Transform
    ellipse_color: _spatial_analyzer_values_pb2.Color
    def __init__(self, ellipse_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., x_axis_radius: _Optional[float] = ..., y_axis_radius: _Optional[float] = ..., z_axis_radius: _Optional[float] = ..., magnification: _Optional[float] = ..., uncertainty_ellipsoid: bool = ..., transform_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., ellipse_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ...) -> None: ...

class ConstructEllipsoidResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFoldersRequest(_message.Message):
    __slots__ = ("folder_path",)
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    def __init__(self, folder_path: _Optional[str] = ...) -> None: ...

class ConstructFoldersResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteFoldersByWildcardRequest(_message.Message):
    __slots__ = ("search_string", "case_sensitive_search", "allow_deleting_all_folders")
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    ALLOW_DELETING_ALL_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    case_sensitive_search: bool
    allow_deleting_all_folders: bool
    def __init__(self, search_string: _Optional[str] = ..., case_sensitive_search: bool = ..., allow_deleting_all_folders: bool = ...) -> None: ...

class DeleteFoldersByWildcardResult(_message.Message):
    __slots__ = ("num_deleted", "num_failed", "execution")
    NUM_DELETED_FIELD_NUMBER: _ClassVar[int]
    NUM_FAILED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    num_deleted: int
    num_failed: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, num_deleted: _Optional[int] = ..., num_failed: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameWithWizardRequest(_message.Message):
    __slots__ = ("new_frame_name", "wait_for_completion")
    NEW_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    new_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    wait_for_completion: bool
    def __init__(self, new_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., wait_for_completion: bool = ...) -> None: ...

class ConstructFrameWithWizardResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameRequest(_message.Message):
    __slots__ = ("new_frame_name", "transform_in_working_coordinates")
    NEW_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    new_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    transform_in_working_coordinates: _spatial_analyzer_values_pb2.Transform
    def __init__(self, new_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., transform_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class ConstructFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameFromTransformInWorldRequest(_message.Message):
    __slots__ = ("new_frame_name", "transform_in_world_coordinates")
    NEW_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORLD_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    new_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    transform_in_world_coordinates: _spatial_analyzer_values_pb2.Transform
    def __init__(self, new_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., transform_in_world_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class ConstructFrameFromTransformInWorldResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameOnInstrumentBaseRequest(_message.Message):
    __slots__ = ("instrument_id", "frame_name")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    frame_name: str
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., frame_name: _Optional[str] = ...) -> None: ...

class ConstructFrameOnInstrumentBaseResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameOnObjectRequest(_message.Message):
    __slots__ = ("reference_object", "frame_name")
    REFERENCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    reference_object: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFrameOnObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameThreePointsRequest(_message.Message):
    __slots__ = ("construction_method", "origin_point", "primary_axis_point", "secondary_axis_point", "frame_name")
    CONSTRUCTION_METHOD_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_POINT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_AXIS_POINT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AXIS_POINT_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    construction_method: FrameConstructionMethod
    origin_point: _spatial_analyzer_values_pb2.PointName
    primary_axis_point: _spatial_analyzer_values_pb2.PointName
    secondary_axis_point: _spatial_analyzer_values_pb2.PointName
    frame_name: str
    def __init__(self, construction_method: _Optional[_Union[FrameConstructionMethod, str]] = ..., origin_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., primary_axis_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., secondary_axis_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., frame_name: _Optional[str] = ...) -> None: ...

class ConstructFrameThreePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameAtPointWithWorkingZAndClockedAxisRequest(_message.Message):
    __slots__ = ("origin_point", "clocked_axis", "clocking_point", "frame_name")
    ORIGIN_POINT_FIELD_NUMBER: _ClassVar[int]
    CLOCKED_AXIS_FIELD_NUMBER: _ClassVar[int]
    CLOCKING_POINT_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    origin_point: _spatial_analyzer_values_pb2.PointName
    clocked_axis: AxisIdentifier
    clocking_point: _spatial_analyzer_values_pb2.PointName
    frame_name: str
    def __init__(self, origin_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., clocked_axis: _Optional[_Union[AxisIdentifier, str]] = ..., clocking_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., frame_name: _Optional[str] = ...) -> None: ...

class ConstructFrameAtPointWithWorkingZAndClockedAxisResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFramePickOriginAndPointOnXAxisClockZAlongWorkingZRequest(_message.Message):
    __slots__ = ("origin_point", "point_on_x_axis", "frame_name")
    ORIGIN_POINT_FIELD_NUMBER: _ClassVar[int]
    POINT_ON_X_AXIS_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    origin_point: _spatial_analyzer_values_pb2.PointName
    point_on_x_axis: _spatial_analyzer_values_pb2.PointName
    frame_name: str
    def __init__(self, origin_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., point_on_x_axis: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., frame_name: _Optional[str] = ...) -> None: ...

class ConstructFramePickOriginAndPointOnXAxisClockZAlongWorkingZResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameKnownOriginObjectDirectionObjectDirectionRequest(_message.Message):
    __slots__ = ("known_point", "known_point_value_in_new_frame", "primary_axis_object", "primary_axis_defines_which_axis", "secondary_axis_object", "secondary_axis_defines_which_axis", "frame_name")
    KNOWN_POINT_FIELD_NUMBER: _ClassVar[int]
    KNOWN_POINT_VALUE_IN_NEW_FRAME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_AXIS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_AXIS_DEFINES_WHICH_AXIS_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AXIS_OBJECT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_AXIS_DEFINES_WHICH_AXIS_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    known_point: _spatial_analyzer_values_pb2.PointName
    known_point_value_in_new_frame: _spatial_analyzer_values_pb2.Vector
    primary_axis_object: _spatial_analyzer_values_pb2.CollectionObjectName
    primary_axis_defines_which_axis: AxisIdentifier
    secondary_axis_object: _spatial_analyzer_values_pb2.CollectionObjectName
    secondary_axis_defines_which_axis: AxisIdentifier
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, known_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., known_point_value_in_new_frame: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., primary_axis_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., primary_axis_defines_which_axis: _Optional[_Union[AxisIdentifier, str]] = ..., secondary_axis_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., secondary_axis_defines_which_axis: _Optional[_Union[AxisIdentifier, str]] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFrameKnownOriginObjectDirectionObjectDirectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameThreePlanesRequest(_message.Message):
    __slots__ = ("x_plane", "x_value_on_plane", "y_plane", "y_value_on_plane", "z_plane", "z_value_on_plane", "frame_name")
    X_PLANE_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_ON_PLANE_FIELD_NUMBER: _ClassVar[int]
    Y_PLANE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_ON_PLANE_FIELD_NUMBER: _ClassVar[int]
    Z_PLANE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_ON_PLANE_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    x_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    x_value_on_plane: float
    y_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    y_value_on_plane: float
    z_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    z_value_on_plane: float
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, x_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., x_value_on_plane: _Optional[float] = ..., y_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., y_value_on_plane: _Optional[float] = ..., z_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., z_value_on_plane: _Optional[float] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFrameThreePlanesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameCopyAndMakeLeftHandedRequest(_message.Message):
    __slots__ = ("reference_frame", "frame_name", "axis_to_reverse")
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    AXIS_TO_REVERSE_FIELD_NUMBER: _ClassVar[int]
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    axis_to_reverse: FrameAxis
    def __init__(self, reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., axis_to_reverse: _Optional[_Union[FrameAxis, str]] = ...) -> None: ...

class ConstructFrameCopyAndMakeLeftHandedResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameAverageOfOtherObjectFramesRequest(_message.Message):
    __slots__ = ("objects", "frame_name")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFrameAverageOfOtherObjectFramesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameAtRobotLinkRequest(_message.Message):
    __slots__ = ("machine_id", "link_name", "resulting_frame")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    link_name: str
    resulting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., link_name: _Optional[str] = ..., resulting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFrameAtRobotLinkResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFrameFromPointMeasurementProbingFramesRequest(_message.Message):
    __slots__ = ("point_list", "show_frame")
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOW_FRAME_FIELD_NUMBER: _ClassVar[int]
    point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    show_frame: bool
    def __init__(self, point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., show_frame: bool = ...) -> None: ...

class ConstructFrameFromPointMeasurementProbingFramesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructMirrorCubeFrameRequest(_message.Message):
    __slots__ = ("mirror_cube_frame_name", "point_name", "use_current_measurements_marked_as_mirror_shots", "nominal_cube_face_angle")
    MIRROR_CUBE_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_CURRENT_MEASUREMENTS_MARKED_AS_MIRROR_SHOTS_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_CUBE_FACE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    mirror_cube_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    use_current_measurements_marked_as_mirror_shots: bool
    nominal_cube_face_angle: float
    def __init__(self, mirror_cube_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., use_current_measurements_marked_as_mirror_shots: bool = ..., nominal_cube_face_angle: _Optional[float] = ...) -> None: ...

class ConstructMirrorCubeFrameResult(_message.Message):
    __slots__ = ("total_angular_error", "execution")
    TOTAL_ANGULAR_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_angular_error: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_angular_error: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFramesByProjectingFramesOnMeshAlongFrameDirectionRequest(_message.Message):
    __slots__ = ("reference_frame_names", "base_name_for_projected_frames", "bi_directional_projection", "mesh_serving_as_projection_target")
    REFERENCE_FRAME_NAMES_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FOR_PROJECTED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    BI_DIRECTIONAL_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    MESH_SERVING_AS_PROJECTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    reference_frame_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    base_name_for_projected_frames: _spatial_analyzer_values_pb2.CollectionObjectName
    bi_directional_projection: bool
    mesh_serving_as_projection_target: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_frame_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., base_name_for_projected_frames: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., bi_directional_projection: bool = ..., mesh_serving_as_projection_target: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFramesByProjectingFramesOnMeshAlongFrameDirectionResult(_message.Message):
    __slots__ = ("resultant_frame_name_list", "execution")
    RESULTANT_FRAME_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_frame_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_frame_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructFramesByProjectingFramesOnMeshAlongReferenceDirectionRequest(_message.Message):
    __slots__ = ("reference_frame_names", "base_name_for_projected_frames", "object_providing_direction_reference", "bi_directional_projection", "mesh_serving_as_projection_target")
    REFERENCE_FRAME_NAMES_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FOR_PROJECTED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDING_DIRECTION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    BI_DIRECTIONAL_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    MESH_SERVING_AS_PROJECTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    reference_frame_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    base_name_for_projected_frames: _spatial_analyzer_values_pb2.CollectionObjectName
    object_providing_direction_reference: _spatial_analyzer_values_pb2.CollectionObjectName
    bi_directional_projection: bool
    mesh_serving_as_projection_target: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_frame_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., base_name_for_projected_frames: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., object_providing_direction_reference: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., bi_directional_projection: bool = ..., mesh_serving_as_projection_target: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructFramesByProjectingFramesOnMeshAlongReferenceDirectionResult(_message.Message):
    __slots__ = ("resultant_frame_name_list", "execution")
    RESULTANT_FRAME_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_frame_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_frame_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddSurfaceToMeshOffsetAlongReferenceDirectionRequest(_message.Message):
    __slots__ = ("reference_frame_names", "surface_for_offset_distance_computation", "surface_offset_range", "collection_for_result_frames", "object_providing_direction_reference", "bi_directional_projection", "mesh_serving_as_projection_target")
    REFERENCE_FRAME_NAMES_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FOR_OFFSET_DISTANCE_COMPUTATION_FIELD_NUMBER: _ClassVar[int]
    SURFACE_OFFSET_RANGE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FOR_RESULT_FRAMES_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDING_DIRECTION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    BI_DIRECTIONAL_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    MESH_SERVING_AS_PROJECTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    reference_frame_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    surface_for_offset_distance_computation: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_offset_range: float
    collection_for_result_frames: str
    object_providing_direction_reference: _spatial_analyzer_values_pb2.CollectionObjectName
    bi_directional_projection: bool
    mesh_serving_as_projection_target: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_frame_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., surface_for_offset_distance_computation: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_offset_range: _Optional[float] = ..., collection_for_result_frames: _Optional[str] = ..., object_providing_direction_reference: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., bi_directional_projection: bool = ..., mesh_serving_as_projection_target: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class AddSurfaceToMeshOffsetAlongReferenceDirectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPointsRequest(_message.Message):
    __slots__ = ("line_name", "first_point", "second_point")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_POINT_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    first_point: _spatial_analyzer_values_pb2.PointName
    second_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPointsVectorNotationRequest(_message.Message):
    __slots__ = ("line_name", "first_vector", "second_vector")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_VECTOR_FIELD_NUMBER: _ClassVar[int]
    SECOND_VECTOR_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    first_vector: _spatial_analyzer_values_pb2.Vector
    second_vector: _spatial_analyzer_values_pb2.Vector
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_vector: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., second_vector: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPointsVectorNotationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineNormalToObjectRequest(_message.Message):
    __slots__ = ("line_name", "line_length", "object")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    line_length: float
    object: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., line_length: _Optional[float] = ..., object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructLineNormalToObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineProjectLineToObjectReferencePlaneRequest(_message.Message):
    __slots__ = ("line_to_create", "line_to_project", "object_to_project_to")
    LINE_TO_CREATE_FIELD_NUMBER: _ClassVar[int]
    LINE_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TO_PROJECT_TO_FIELD_NUMBER: _ClassVar[int]
    line_to_create: _spatial_analyzer_values_pb2.CollectionObjectName
    line_to_project: _spatial_analyzer_values_pb2.CollectionObjectName
    object_to_project_to: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, line_to_create: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., line_to_project: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., object_to_project_to: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructLineProjectLineToObjectReferencePlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineNormalToObjectThroughPointRequest(_message.Message):
    __slots__ = ("line_to_create", "object_name", "point_name")
    LINE_TO_CREATE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    line_to_create: _spatial_analyzer_values_pb2.CollectionObjectName
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, line_to_create: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructLineNormalToObjectThroughPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPlaneIntersectionRequest(_message.Message):
    __slots__ = ("line_name", "first_plane", "second_plane")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_PLANE_FIELD_NUMBER: _ClassVar[int]
    SECOND_PLANE_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    first_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    second_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructLineTwoPlaneIntersectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLinesFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructLinesFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineCenterOfSlotRequest(_message.Message):
    __slots__ = ("line_name", "slot_name")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    SLOT_NAME_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    slot_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., slot_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructLineCenterOfSlotResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructLineFromInstrumentShotRequest(_message.Message):
    __slots__ = ("point_name", "observation_index", "line_name")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructLineFromInstrumentShotResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSystemStringRequest(_message.Message):
    __slots__ = ("string_content", "format_string")
    STRING_CONTENT_FIELD_NUMBER: _ClassVar[int]
    FORMAT_STRING_FIELD_NUMBER: _ClassVar[int]
    string_content: SystemString
    format_string: str
    def __init__(self, string_content: _Optional[_Union[SystemString, str]] = ..., format_string: _Optional[str] = ...) -> None: ...

class MakeSystemStringResult(_message.Message):
    __slots__ = ("resultant_string", "execution")
    RESULTANT_STRING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_string: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_string: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionNameRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeCollectionNameRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_collection_name", "execution")
    RESULTANT_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_name: _spatial_analyzer_values_pb2.CollectionName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionItemNameRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "item_wildcard_criteria", "item_type")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ITEM_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    item_wildcard_criteria: str
    item_type: _spatial_analyzer_values_pb2.ItemType
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., item_wildcard_criteria: _Optional[str] = ..., item_type: _Optional[_Union[_spatial_analyzer_values_pb2.ItemType, str]] = ...) -> None: ...

class MakeCollectionItemNameRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("resultant_collection_item_name_ref_list", "execution")
    RESULTANT_COLLECTION_ITEM_NAME_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_item_name_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_item_name_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt", "object_type")
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    object_type: _spatial_analyzer_values_pb2.ObjectType
    def __init__(self, user_prompt: _Optional[str] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ...) -> None: ...

class MakeCollectionObjectNameRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_collection_object_name", "execution")
    RESULTANT_COLLECTION_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameEnsureUniqueRequest(_message.Message):
    __slots__ = ("collection_object_name", "use_number_suffix")
    COLLECTION_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_NUMBER_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    collection_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    use_number_suffix: bool
    def __init__(self, collection_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_number_suffix: bool = ...) -> None: ...

class MakeCollectionObjectNameEnsureUniqueResult(_message.Message):
    __slots__ = ("collection_object_name", "execution")
    COLLECTION_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    collection_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, collection_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt", "object_type")
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    object_type: _spatial_analyzer_values_pb2.ObjectType
    def __init__(self, user_prompt: _Optional[str] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ...) -> None: ...

class MakeCollectionObjectNameRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_collection_object_name_ref_list", "execution")
    RESULTANT_COLLECTION_OBJECT_NAME_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_object_name_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_object_name_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "object_wildcard_criteria", "object_type")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    object_wildcard_criteria: str
    object_type: _spatial_analyzer_values_pb2.ObjectType
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., object_wildcard_criteria: _Optional[str] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ...) -> None: ...

class MakeCollectionObjectNameRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("resultant_collection_object_name_ref_list", "execution")
    RESULTANT_COLLECTION_OBJECT_NAME_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_object_name_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_object_name_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListByTypeRequest(_message.Message):
    __slots__ = ("collection", "object_type")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection: str
    object_type: _spatial_analyzer_values_pb2.ObjectType
    def __init__(self, collection: _Optional[str] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ...) -> None: ...

class MakeCollectionObjectNameRefListByTypeResult(_message.Message):
    __slots__ = ("resultant_collection_object_name_list", "execution")
    RESULTANT_COLLECTION_OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListByTypeAndColorRequest(_message.Message):
    __slots__ = ("collection", "object_type", "object_color")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_COLOR_FIELD_NUMBER: _ClassVar[int]
    collection: str
    object_type: _spatial_analyzer_values_pb2.ObjectType
    object_color: _spatial_analyzer_values_pb2.Color
    def __init__(self, collection: _Optional[str] = ..., object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ..., object_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListByTypeAndColorResult(_message.Message):
    __slots__ = ("resultant_collection_object_name_list", "execution")
    RESULTANT_COLLECTION_OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListFromAllGroupsInCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListFromAllGroupsInCollectionResult(_message.Message):
    __slots__ = ("collection_object_name_list", "execution")
    COLLECTION_OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    collection_object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, collection_object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCollectionInstrumentRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCollectionInstrumentRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCollectionInstrumentRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ...) -> None: ...

class SetCollectionInstrumentRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddCollectionInstrumentsToRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_instrument_ref_list", "collection_wildcard_criteria", "instrument_wildcard_criteria")
    COLLECTION_INSTRUMENT_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_instrument_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    collection_wildcard_criteria: str
    instrument_wildcard_criteria: str
    def __init__(self, collection_instrument_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., collection_wildcard_criteria: _Optional[str] = ..., instrument_wildcard_criteria: _Optional[str] = ...) -> None: ...

class AddCollectionInstrumentsToRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("collection_instrument_ref_list", "execution")
    COLLECTION_INSTRUMENT_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    collection_instrument_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, collection_instrument_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionInstrumentRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeCollectionInstrumentRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_collection_instrument_ref_list", "execution")
    RESULTANT_COLLECTION_INSTRUMENT_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_instrument_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_instrument_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeRelationshipRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "relationship_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    relationship_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., relationship_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakeRelationshipRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("resultant_relationship_ref_list", "execution")
    RESULTANT_RELATIONSHIP_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_relationship_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_relationship_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeRelationshipRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeRelationshipRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_relationship_ref_list", "execution")
    RESULTANT_RELATIONSHIP_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_relationship_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_relationship_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeEventRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "event_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    EVENT_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    event_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., event_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakeEventRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("resultant_event_ref_list", "execution")
    RESULTANT_EVENT_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_event_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_event_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionInstrumentIdRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeCollectionInstrumentIdRuntimeSelectResult(_message.Message):
    __slots__ = ("instrument_id", "execution")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeReportRefListFromCollectionRequest(_message.Message):
    __slots__ = ("collection_name",)
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeReportRefListFromCollectionResult(_message.Message):
    __slots__ = ("report_list", "execution")
    REPORT_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    report_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, report_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeReportRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeReportRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("report_list", "execution")
    REPORT_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    report_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, report_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePictureNameRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakePictureNameRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("picture_name_list", "execution")
    PICTURE_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    picture_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, picture_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeTransformFromDoublesFixedXyzRequest(_message.Message):
    __slots__ = ("x", "y", "z", "rx", "ry", "rz")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rx: _Optional[float] = ..., ry: _Optional[float] = ..., rz: _Optional[float] = ...) -> None: ...

class MakeTransformFromDoublesFixedXyzResult(_message.Message):
    __slots__ = ("resultant_transform", "execution")
    RESULTANT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_transform: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeTransformFromDoublesEulerParametersRequest(_message.Message):
    __slots__ = ("x", "y", "z", "e1", "e2", "e3", "e4")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    E1_FIELD_NUMBER: _ClassVar[int]
    E2_FIELD_NUMBER: _ClassVar[int]
    E3_FIELD_NUMBER: _ClassVar[int]
    E4_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    e1: float
    e2: float
    e3: float
    e4: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., e1: _Optional[float] = ..., e2: _Optional[float] = ..., e3: _Optional[float] = ..., e4: _Optional[float] = ...) -> None: ...

class MakeTransformFromDoublesEulerParametersResult(_message.Message):
    __slots__ = ("resultant_transform", "execution")
    RESULTANT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_transform: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetWorkingTransformOfObjectFixedXyzRequest(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetWorkingTransformOfObjectFixedXyzResult(_message.Message):
    __slots__ = ("transform", "execution")
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class InvertTransformRequest(_message.Message):
    __slots__ = ("transform",)
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class InvertTransformResult(_message.Message):
    __slots__ = ("inverse_transform", "execution")
    INVERSE_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    inverse_transform: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, inverse_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesFixedXyzRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesFixedXyzResult(_message.Message):
    __slots__ = ("x", "y", "z", "rx", "ry", "rz", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rx: _Optional[float] = ..., ry: _Optional[float] = ..., rz: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoVectorsFixedXyzRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoVectorsFixedXyzResult(_message.Message):
    __slots__ = ("position_in_working", "orientation_in_working", "execution")
    POSITION_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    position_in_working: _spatial_analyzer_values_pb2.Vector
    orientation_in_working: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, position_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., orientation_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoVectorsOriginAndAxesRequest(_message.Message):
    __slots__ = ("transform",)
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoVectorsOriginAndAxesResult(_message.Message):
    __slots__ = ("origin", "x_axis", "y_axis", "z_axis", "execution")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    X_AXIS_FIELD_NUMBER: _ClassVar[int]
    Y_AXIS_FIELD_NUMBER: _ClassVar[int]
    Z_AXIS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    origin: _spatial_analyzer_values_pb2.Vector
    x_axis: _spatial_analyzer_values_pb2.Vector
    y_axis: _spatial_analyzer_values_pb2.Vector
    z_axis: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, origin: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_axis: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., y_axis: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., z_axis: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeWorldTransformOperatorIntoDoublesFixedXyzInWorldRequest(_message.Message):
    __slots__ = ("input_world_transform_operator",)
    INPUT_WORLD_TRANSFORM_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    input_world_transform_operator: _spatial_analyzer_values_pb2.WorldTransform
    def __init__(self, input_world_transform_operator: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ...) -> None: ...

class DecomposeWorldTransformOperatorIntoDoublesFixedXyzInWorldResult(_message.Message):
    __slots__ = ("x", "y", "z", "rx", "ry", "rz", "scale", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float
    scale: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rx: _Optional[float] = ..., ry: _Optional[float] = ..., rz: _Optional[float] = ..., scale: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerXyzRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerXyzResult(_message.Message):
    __slots__ = ("x", "y", "z", "rx", "ry", "rz", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rx: _Optional[float] = ..., ry: _Optional[float] = ..., rz: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZyxRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZyxResult(_message.Message):
    __slots__ = ("x", "y", "z", "rz", "ry", "rx", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    RZ_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    rz: float
    ry: float
    rx: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., rz: _Optional[float] = ..., ry: _Optional[float] = ..., rx: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZyzRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZyzResult(_message.Message):
    __slots__ = ("x", "y", "z", "first_rz", "ry", "second_rz", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    FIRST_RZ_FIELD_NUMBER: _ClassVar[int]
    RY_FIELD_NUMBER: _ClassVar[int]
    SECOND_RZ_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    first_rz: float
    ry: float
    second_rz: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., first_rz: _Optional[float] = ..., ry: _Optional[float] = ..., second_rz: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZxzRequest(_message.Message):
    __slots__ = ("input_transform",)
    INPUT_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    input_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, input_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class DecomposeTransformIntoDoublesEulerZxzResult(_message.Message):
    __slots__ = ("x", "y", "z", "first_rz", "rx", "second_rz", "execution")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    FIRST_RZ_FIELD_NUMBER: _ClassVar[int]
    RX_FIELD_NUMBER: _ClassVar[int]
    SECOND_RZ_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    first_rz: float
    rx: float
    second_rz: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ..., first_rz: _Optional[float] = ..., rx: _Optional[float] = ..., second_rz: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DecomposeWorldTransformOperatorIntoVectorsFixedXyzInWorldRequest(_message.Message):
    __slots__ = ("input_world_transform_operator",)
    INPUT_WORLD_TRANSFORM_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    input_world_transform_operator: _spatial_analyzer_values_pb2.WorldTransform
    def __init__(self, input_world_transform_operator: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ...) -> None: ...

class DecomposeWorldTransformOperatorIntoVectorsFixedXyzInWorldResult(_message.Message):
    __slots__ = ("position_in_working", "orientation_in_working", "scale", "execution")
    POSITION_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    position_in_working: _spatial_analyzer_values_pb2.Vector
    orientation_in_working: _spatial_analyzer_values_pb2.Vector
    scale: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, position_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., orientation_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., scale: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPerimeterFromPointsRequest(_message.Message):
    __slots__ = ("resulting_perimeter_name", "point_list", "open_perimeter")
    RESULTING_PERIMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    OPEN_PERIMETER_FIELD_NUMBER: _ClassVar[int]
    resulting_perimeter_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    open_perimeter: bool
    def __init__(self, resulting_perimeter_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., open_perimeter: bool = ...) -> None: ...

class ConstructPerimeterFromPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPlaneRequest(_message.Message):
    __slots__ = ("plane_name", "plane_center", "plane_normal", "plane_edge_dimension")
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_CENTER_FIELD_NUMBER: _ClassVar[int]
    PLANE_NORMAL_FIELD_NUMBER: _ClassVar[int]
    PLANE_EDGE_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_center: _spatial_analyzer_values_pb2.Vector
    plane_normal: _spatial_analyzer_values_pb2.Vector
    plane_edge_dimension: float
    def __init__(self, plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_center: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., plane_normal: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., plane_edge_dimension: _Optional[float] = ...) -> None: ...

class ConstructPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPlaneNormalToObjectThroughPointRequest(_message.Message):
    __slots__ = ("resultant_plane_name", "normal_to_object_name", "through_point_name", "plane_edge_dimension")
    RESULTANT_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    NORMAL_TO_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    THROUGH_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_EDGE_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    resultant_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    normal_to_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    through_point_name: _spatial_analyzer_values_pb2.PointName
    plane_edge_dimension: float
    def __init__(self, resultant_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., normal_to_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., through_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., plane_edge_dimension: _Optional[float] = ...) -> None: ...

class ConstructPlaneNormalToObjectThroughPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPlanesBoundingPointGroupRequest(_message.Message):
    __slots__ = ("reference_plane_name", "group_to_bound", "resulting_high_plane_name", "resulting_low_plane_name", "override_target_point_offsets", "offset_value")
    REFERENCE_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_BOUND_FIELD_NUMBER: _ClassVar[int]
    RESULTING_HIGH_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_LOW_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TARGET_POINT_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_VALUE_FIELD_NUMBER: _ClassVar[int]
    reference_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    group_to_bound: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_high_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_low_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    override_target_point_offsets: bool
    offset_value: float
    def __init__(self, reference_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_to_bound: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_high_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_low_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., override_target_point_offsets: bool = ..., offset_value: _Optional[float] = ...) -> None: ...

class ConstructPlanesBoundingPointGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPlanesBisectTwoPlanesRequest(_message.Message):
    __slots__ = ("resultant_plane_name", "first_plane", "second_plane")
    RESULTANT_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_PLANE_FIELD_NUMBER: _ClassVar[int]
    SECOND_PLANE_FIELD_NUMBER: _ClassVar[int]
    resultant_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    first_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    second_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, resultant_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPlanesBisectTwoPlanesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShiftPlaneRequest(_message.Message):
    __slots__ = ("plane", "shift_along_normal", "grow_bounds_by_factor")
    PLANE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_ALONG_NORMAL_FIELD_NUMBER: _ClassVar[int]
    GROW_BOUNDS_BY_FACTOR_FIELD_NUMBER: _ClassVar[int]
    plane: _spatial_analyzer_values_pb2.CollectionObjectName
    shift_along_normal: float
    grow_bounds_by_factor: float
    def __init__(self, plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., shift_along_normal: _Optional[float] = ..., grow_bounds_by_factor: _Optional[float] = ...) -> None: ...

class ShiftPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPlanesFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructPlanesFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudsFromExistingPointGroupRequest(_message.Message):
    __slots__ = ("point_group_name", "cloud_name")
    POINT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    point_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointCloudsFromExistingPointGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudsFromExistingCloudPointsRuntimeSelectRequest(_message.Message):
    __slots__ = ("cloud_name",)
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointCloudsFromExistingCloudPointsRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudsFromExistingCloudsUniformSpacingRequest(_message.Message):
    __slots__ = ("existing_point_cloud_list", "desired_point_spacing", "minimum_points_per_output_point", "new_cloud_name", "hide_original_point_clouds")
    EXISTING_POINT_CLOUD_LIST_FIELD_NUMBER: _ClassVar[int]
    DESIRED_POINT_SPACING_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_POINTS_PER_OUTPUT_POINT_FIELD_NUMBER: _ClassVar[int]
    NEW_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    HIDE_ORIGINAL_POINT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    existing_point_cloud_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    desired_point_spacing: float
    minimum_points_per_output_point: int
    new_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    hide_original_point_clouds: bool
    def __init__(self, existing_point_cloud_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., desired_point_spacing: _Optional[float] = ..., minimum_points_per_output_point: _Optional[int] = ..., new_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., hide_original_point_clouds: bool = ...) -> None: ...

class ConstructPointCloudsFromExistingCloudsUniformSpacingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudFromExistingCloudsRequest(_message.Message):
    __slots__ = ("existing_point_cloud_list", "new_cloud_name", "cloud_thinning_settings", "hide_original_point_clouds")
    EXISTING_POINT_CLOUD_LIST_FIELD_NUMBER: _ClassVar[int]
    NEW_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    HIDE_ORIGINAL_POINT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    existing_point_cloud_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    new_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    hide_original_point_clouds: bool
    def __init__(self, existing_point_cloud_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., new_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., hide_original_point_clouds: bool = ...) -> None: ...

class ConstructPointCloudFromExistingCloudsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudFromVisibleCloudPointsRequest(_message.Message):
    __slots__ = ("source_clouds", "destination_cloud_name")
    SOURCE_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    source_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    destination_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, source_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., destination_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointCloudFromVisibleCloudPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructBoundaryPointsFromCloudRequest(_message.Message):
    __slots__ = ("source_cloud_name", "destination_cloud_name")
    SOURCE_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    source_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    destination_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, source_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., destination_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructBoundaryPointsFromCloudResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointCloudLimitingProbingDirectionsRequest(_message.Message):
    __slots__ = ("source_cloud_name", "normal_to_object_name", "acceptance_angle", "destination_cloud_name", "hide_source_cloud")
    SOURCE_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    NORMAL_TO_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCEPTANCE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    HIDE_SOURCE_CLOUD_FIELD_NUMBER: _ClassVar[int]
    source_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    normal_to_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    acceptance_angle: float
    destination_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    hide_source_cloud: bool
    def __init__(self, source_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., normal_to_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., acceptance_angle: _Optional[float] = ..., destination_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., hide_source_cloud: bool = ...) -> None: ...

class ConstructPointCloudLimitingProbingDirectionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCrossSectionCloudRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name", "cylindrical_cross_section_mode", "start_distance", "section_spacing", "proximity_threshold", "maximum_section_count", "limit_cross_section_extent", "radius_limit", "project_to_reference_surface", "reference_object", "input_clouds", "cloud_thinning_settings", "update_existing_cloud")
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    CYLINDRICAL_CROSS_SECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    START_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SECTION_SPACING_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_SECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_CROSS_SECTION_EXTENT_FIELD_NUMBER: _ClassVar[int]
    RADIUS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TO_REFERENCE_SURFACE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EXISTING_CLOUD_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cylindrical_cross_section_mode: bool
    start_distance: float
    section_spacing: float
    proximity_threshold: float
    maximum_section_count: int
    limit_cross_section_extent: bool
    radius_limit: float
    project_to_reference_surface: bool
    reference_object: _spatial_analyzer_values_pb2.CollectionObjectName
    input_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    update_existing_cloud: bool
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cylindrical_cross_section_mode: bool = ..., start_distance: _Optional[float] = ..., section_spacing: _Optional[float] = ..., proximity_threshold: _Optional[float] = ..., maximum_section_count: _Optional[int] = ..., limit_cross_section_extent: bool = ..., radius_limit: _Optional[float] = ..., project_to_reference_surface: bool = ..., reference_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., input_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., update_existing_cloud: bool = ...) -> None: ...

class ConstructCrossSectionCloudResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructCrossSectionCloudUserSelectRequest(_message.Message):
    __slots__ = ("cross_section_cloud_name", "proximity_threshold", "limit_cross_section_extent", "radius_limit", "project_to_reference_surface", "reference_planes", "input_clouds", "cloud_thinning_settings", "update_existing_cloud")
    CROSS_SECTION_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_CROSS_SECTION_EXTENT_FIELD_NUMBER: _ClassVar[int]
    RADIUS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TO_REFERENCE_SURFACE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_PLANES_FIELD_NUMBER: _ClassVar[int]
    INPUT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EXISTING_CLOUD_FIELD_NUMBER: _ClassVar[int]
    cross_section_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    proximity_threshold: float
    limit_cross_section_extent: bool
    radius_limit: float
    project_to_reference_surface: bool
    reference_planes: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    input_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    update_existing_cloud: bool
    def __init__(self, cross_section_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., proximity_threshold: _Optional[float] = ..., limit_cross_section_extent: bool = ..., radius_limit: _Optional[float] = ..., project_to_reference_surface: bool = ..., reference_planes: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., input_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., update_existing_cloud: bool = ...) -> None: ...

class ConstructCrossSectionCloudUserSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExtractSphereCentersFromPointCloudRequest(_message.Message):
    __slots__ = ("cloud_name", "desired_diameter", "extraction_tolerance", "minimum_point_count", "group_name_for_points", "perform_final_fit", "final_fit_cone_angle")
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    EXTRACTION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FOR_POINTS_FIELD_NUMBER: _ClassVar[int]
    PERFORM_FINAL_FIT_FIELD_NUMBER: _ClassVar[int]
    FINAL_FIT_CONE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    desired_diameter: float
    extraction_tolerance: float
    minimum_point_count: int
    group_name_for_points: _spatial_analyzer_values_pb2.CollectionObjectName
    perform_final_fit: bool
    final_fit_cone_angle: float
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., desired_diameter: _Optional[float] = ..., extraction_tolerance: _Optional[float] = ..., minimum_point_count: _Optional[int] = ..., group_name_for_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., perform_final_fit: bool = ..., final_fit_cone_angle: _Optional[float] = ...) -> None: ...

class ExtractSphereCentersFromPointCloudResult(_message.Message):
    __slots__ = ("number_of_points_extracted", "execution")
    NUMBER_OF_POINTS_EXTRACTED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    number_of_points_extracted: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, number_of_points_extracted: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ProjectedPointGradient(_message.Message):
    __slots__ = ("projected_point", "normal_vector", "u_direction", "v_direction")
    PROJECTED_POINT_FIELD_NUMBER: _ClassVar[int]
    NORMAL_VECTOR_FIELD_NUMBER: _ClassVar[int]
    U_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    V_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    projected_point: _spatial_analyzer_values_pb2.Vector
    normal_vector: _spatial_analyzer_values_pb2.Vector
    u_direction: _spatial_analyzer_values_pb2.Vector
    v_direction: _spatial_analyzer_values_pb2.Vector
    def __init__(self, projected_point: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., normal_vector: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., u_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., v_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class ObjectOriginResult(_message.Message):
    __slots__ = ("vector_representation", "x_value", "y_value", "z_value")
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    def __init__(self, vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ...) -> None: ...

class GroupAverageResult(_message.Message):
    __slots__ = ("rms_deviation", "max_absolute_deviation", "average_deviation")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAX_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    def __init__(self, rms_deviation: _Optional[float] = ..., max_absolute_deviation: _Optional[float] = ..., average_deviation: _Optional[float] = ...) -> None: ...

class ConstructPointFitToPointsRequest(_message.Message):
    __slots__ = ("point_names", "resulting_point_name")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointFitToPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointInWorkingCoordinatesRequest(_message.Message):
    __slots__ = ("point_name", "working_coordinates")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    working_coordinates: _spatial_analyzer_values_pb2.Vector
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class ConstructPointInWorkingCoordinatesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointFromSurveyTargetCenterRequest(_message.Message):
    __slots__ = ("cloud_containing_target", "reference_seed_point", "survey_target_type", "search_diameter", "result_center_point_name")
    CLOUD_CONTAINING_TARGET_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_SEED_POINT_FIELD_NUMBER: _ClassVar[int]
    SURVEY_TARGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    RESULT_CENTER_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    cloud_containing_target: _spatial_analyzer_values_pb2.CollectionObjectName
    reference_seed_point: _spatial_analyzer_values_pb2.PointName
    survey_target_type: SurveyTargetType
    search_diameter: float
    result_center_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, cloud_containing_target: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., reference_seed_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., survey_target_type: _Optional[_Union[SurveyTargetType, str]] = ..., search_diameter: _Optional[float] = ..., result_center_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointFromSurveyTargetCenterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointPositionInWorkingCoordinatesRequest(_message.Message):
    __slots__ = ("point_name", "position_in_working_coordinates")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    position_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., position_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class SetPointPositionInWorkingCoordinatesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformPointsByDeltaAboutWorkingFrameRequest(_message.Message):
    __slots__ = ("point_name_list", "delta_in_working_coordinates")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    DELTA_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    delta_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., delta_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class TransformPointsByDeltaAboutWorkingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtLineMidpointRequest(_message.Message):
    __slots__ = ("line_name", "point_name")
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtLineMidpointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointGroupFromPointNameRefListRequest(_message.Message):
    __slots__ = ("point_name_list", "group_name")
    POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointGroupFromPointNameRefListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointGroupsFromVectorGroupsRequest(_message.Message):
    __slots__ = ("vector_groups", "optional_group_name_suffix", "make_vector_begin_points", "make_vector_end_points")
    VECTOR_GROUPS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_GROUP_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    MAKE_VECTOR_BEGIN_POINTS_FIELD_NUMBER: _ClassVar[int]
    MAKE_VECTOR_END_POINTS_FIELD_NUMBER: _ClassVar[int]
    vector_groups: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    optional_group_name_suffix: str
    make_vector_begin_points: bool
    make_vector_end_points: bool
    def __init__(self, vector_groups: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., optional_group_name_suffix: _Optional[str] = ..., make_vector_begin_points: bool = ..., make_vector_end_points: bool = ...) -> None: ...

class ConstructPointGroupsFromVectorGroupsResult(_message.Message):
    __slots__ = ("point_groups", "execution")
    POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    point_groups: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, point_groups: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointGroupFromPointCloudRequest(_message.Message):
    __slots__ = ("cloud_name", "point_group_name", "point_prefix", "starting_point_number", "point_offset", "sub_sampling", "sub_sampling_distance", "show_progress")
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    STARTING_POINT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    POINT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    SUB_SAMPLING_FIELD_NUMBER: _ClassVar[int]
    SUB_SAMPLING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SHOW_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_prefix: str
    starting_point_number: int
    point_offset: float
    sub_sampling: bool
    sub_sampling_distance: float
    show_progress: bool
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_prefix: _Optional[str] = ..., starting_point_number: _Optional[int] = ..., point_offset: _Optional[float] = ..., sub_sampling: bool = ..., sub_sampling_distance: _Optional[float] = ..., show_progress: bool = ...) -> None: ...

class ConstructPointGroupFromPointCloudResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointFromCloudPointRuntimeSelectRequest(_message.Message):
    __slots__ = ("selection_prompt", "construct_point", "constructed_point_name")
    SELECTION_PROMPT_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_POINT_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTED_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    selection_prompt: str
    construct_point: bool
    constructed_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, selection_prompt: _Optional[str] = ..., construct_point: bool = ..., constructed_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointFromCloudPointRuntimeSelectResult(_message.Message):
    __slots__ = ("selection_cloud_point_coordinates", "execution")
    SELECTION_CLOUD_POINT_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    selection_cloud_point_coordinates: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, selection_cloud_point_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtCircleCenterRequest(_message.Message):
    __slots__ = ("circle_name", "point_name")
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtCircleCenterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfPlanesRequest(_message.Message):
    __slots__ = ("plane_1_name", "plane_2_name", "plane_3_name", "point_name")
    PLANE_1_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_2_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_3_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    plane_1_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_2_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_3_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, plane_1_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_2_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_3_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfPlanesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfTwoLinesRequest(_message.Message):
    __slots__ = ("first_line_name", "second_line_name", "resulting_point_name")
    FIRST_LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    first_line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    second_line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, first_line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfTwoLinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfPlaneAndLineRequest(_message.Message):
    __slots__ = ("plane_name", "line_name", "resulting_point_name")
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfPlaneAndLineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfTwoBSplinesRequest(_message.Message):
    __slots__ = ("first_b_spline_name", "second_b_spline_name", "point_name")
    FIRST_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    first_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    second_b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, first_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfTwoBSplinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfBSplineAndSurfacesRequest(_message.Message):
    __slots__ = ("b_spline_name", "surface_list", "approximation_tolerance", "point_name")
    B_SPLINE_NAME_FIELD_NUMBER: _ClassVar[int]
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    APPROXIMATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    b_spline_name: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    approximation_tolerance: float
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, b_spline_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., approximation_tolerance: _Optional[float] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtIntersectionOfBSplineAndSurfacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAtIntersectionOfCircleAndLineRequest(_message.Message):
    __slots__ = ("circle_name", "line_name", "base_point_name_for_results")
    CIRCLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINE_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_POINT_NAME_FOR_RESULTS_FIELD_NUMBER: _ClassVar[int]
    circle_name: _spatial_analyzer_values_pb2.CollectionObjectName
    line_name: _spatial_analyzer_values_pb2.CollectionObjectName
    base_point_name_for_results: _spatial_analyzer_values_pb2.PointName
    def __init__(self, circle_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., line_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., base_point_name_for_results: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointsAtIntersectionOfCircleAndLineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAtIntersectionOfPrincipalObjectAxesAndSurfacesRequest(_message.Message):
    __slots__ = ("axis_object_list", "surface_list", "point_suffix", "resultant_group_name")
    AXIS_OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    axis_object_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_suffix: str
    resultant_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, axis_object_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_suffix: _Optional[str] = ..., resultant_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsAtIntersectionOfPrincipalObjectAxesAndSurfacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsFromCylinderRequest(_message.Message):
    __slots__ = ("cylinder_name", "group_name")
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsFromCylinderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtProjectionOfPointOntoObjectRequest(_message.Message):
    __slots__ = ("point_to_project", "object_name", "resulting_point_name")
    POINT_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_to_project: _spatial_analyzer_values_pb2.PointName
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_to_project: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtProjectionOfPointOntoObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesParallelToWcfAxisRequest(_message.Message):
    __slots__ = ("surface_list", "point_names", "group_name_to_contain_new_points", "point_name_prefix", "point_name_suffix", "axis")
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_TO_CONTAIN_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    AXIS_FIELD_NUMBER: _ClassVar[int]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name_to_contain_new_points: str
    point_name_prefix: str
    point_name_suffix: str
    axis: WcfAxis
    def __init__(self, surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name_to_contain_new_points: _Optional[str] = ..., point_name_prefix: _Optional[str] = ..., point_name_suffix: _Optional[str] = ..., axis: _Optional[_Union[WcfAxis, str]] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesParallelToWcfAxisResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesRadialFromWcfAxisRequest(_message.Message):
    __slots__ = ("surface_list", "point_names", "group_name_to_contain_new_points", "point_name_prefix", "point_name_suffix", "axis")
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_TO_CONTAIN_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    AXIS_FIELD_NUMBER: _ClassVar[int]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name_to_contain_new_points: str
    point_name_prefix: str
    point_name_suffix: str
    axis: WcfAxis
    def __init__(self, surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name_to_contain_new_points: _Optional[str] = ..., point_name_prefix: _Optional[str] = ..., point_name_suffix: _Optional[str] = ..., axis: _Optional[_Union[WcfAxis, str]] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesRadialFromWcfAxisResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesSphericalFromWcfOriginRequest(_message.Message):
    __slots__ = ("surface_list", "point_names", "group_name_to_contain_new_points", "point_name_prefix", "point_name_suffix")
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_TO_CONTAIN_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name_to_contain_new_points: str
    point_name_prefix: str
    point_name_suffix: str
    def __init__(self, surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name_to_contain_new_points: _Optional[str] = ..., point_name_prefix: _Optional[str] = ..., point_name_suffix: _Optional[str] = ...) -> None: ...

class ConstructPointsAtProjectionOnSurfacesSphericalFromWcfOriginResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGradientAtProjectedPointOnSurfaceRequest(_message.Message):
    __slots__ = ("point_to_project", "surface_name", "generate_output_vector_lines")
    POINT_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    GENERATE_OUTPUT_VECTOR_LINES_FIELD_NUMBER: _ClassVar[int]
    point_to_project: _spatial_analyzer_values_pb2.PointName
    surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    generate_output_vector_lines: bool
    def __init__(self, point_to_project: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., generate_output_vector_lines: bool = ...) -> None: ...

class GetGradientAtProjectedPointOnSurfaceResult(_message.Message):
    __slots__ = ("gradient", "execution")
    GRADIENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    gradient: ProjectedPointGradient
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, gradient: _Optional[_Union[ProjectedPointGradient, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGradientAtProjectedPointOnSurfaceEdgeRequest(_message.Message):
    __slots__ = ("point_to_project", "surface_edge", "surface_name", "edge_offset_direction", "edge_offset_distance", "generate_output_vector_lines")
    POINT_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    SURFACE_EDGE_FIELD_NUMBER: _ClassVar[int]
    SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    EDGE_OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    EDGE_OFFSET_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    GENERATE_OUTPUT_VECTOR_LINES_FIELD_NUMBER: _ClassVar[int]
    point_to_project: _spatial_analyzer_values_pb2.PointName
    surface_edge: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    edge_offset_direction: _spatial_analyzer_values_pb2.Vector
    edge_offset_distance: float
    generate_output_vector_lines: bool
    def __init__(self, point_to_project: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., surface_edge: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., edge_offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., edge_offset_distance: _Optional[float] = ..., generate_output_vector_lines: bool = ...) -> None: ...

class GetGradientAtProjectedPointOnSurfaceEdgeResult(_message.Message):
    __slots__ = ("gradient", "execution")
    GRADIENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    gradient: ProjectedPointGradient
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, gradient: _Optional[_Union[ProjectedPointGradient, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsByProjectingPointsOnMeshAlongDirectionRequest(_message.Message):
    __slots__ = ("reference_point_names", "group_name_for_projected_points", "object_providing_direction_reference", "bi_directional_projection", "mesh_serving_as_projection_target")
    REFERENCE_POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FOR_PROJECTED_POINTS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_PROVIDING_DIRECTION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    BI_DIRECTIONAL_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    MESH_SERVING_AS_PROJECTION_TARGET_FIELD_NUMBER: _ClassVar[int]
    reference_point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name_for_projected_points: _spatial_analyzer_values_pb2.CollectionObjectName
    object_providing_direction_reference: _spatial_analyzer_values_pb2.CollectionObjectName
    bi_directional_projection: bool
    mesh_serving_as_projection_target: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name_for_projected_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., object_providing_direction_reference: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., bi_directional_projection: bool = ..., mesh_serving_as_projection_target: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsByProjectingPointsOnMeshAlongDirectionResult(_message.Message):
    __slots__ = ("resultant_point_name_list", "execution")
    RESULTANT_POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsSpacedAtDistanceOnCurvesRequest(_message.Message):
    __slots__ = ("b_spline_list", "distance_between_points", "resultant_group_name", "resultant_point_name_prefix")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_BETWEEN_POINTS_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    distance_between_points: float
    resultant_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resultant_point_name_prefix: str
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., distance_between_points: _Optional[float] = ..., resultant_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resultant_point_name_prefix: _Optional[str] = ...) -> None: ...

class ConstructPointsSpacedAtDistanceOnCurvesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsNSpacedOnCurvesRequest(_message.Message):
    __slots__ = ("b_spline_list", "number_of_evenly_spaced_points", "resultant_group_name", "resultant_point_name_prefix")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_EVENLY_SPACED_POINTS_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    number_of_evenly_spaced_points: int
    resultant_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resultant_point_name_prefix: str
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., number_of_evenly_spaced_points: _Optional[int] = ..., resultant_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resultant_point_name_prefix: _Optional[str] = ...) -> None: ...

class ConstructPointsNSpacedOnCurvesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsOnCurvesUsingMaxChordalDeviationRequest(_message.Message):
    __slots__ = ("b_spline_list", "maximum_chordal_deviation", "maximum_trim_edge_angle", "maximum_chord_length", "resultant_group_name", "resultant_point_name_prefix")
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_CHORDAL_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_TRIM_EDGE_ANGLE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_CHORD_LENGTH_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_POINT_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    maximum_chordal_deviation: float
    maximum_trim_edge_angle: float
    maximum_chord_length: float
    resultant_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resultant_point_name_prefix: str
    def __init__(self, b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., maximum_chordal_deviation: _Optional[float] = ..., maximum_trim_edge_angle: _Optional[float] = ..., maximum_chord_length: _Optional[float] = ..., resultant_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resultant_point_name_prefix: _Optional[str] = ...) -> None: ...

class ConstructPointsOnCurvesUsingMaxChordalDeviationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsOnObjectVerticesRequest(_message.Message):
    __slots__ = ("object_name_list", "resultant_group_name")
    OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resultant_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resultant_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsOnObjectVerticesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsOnSurfacesByClickingRequest(_message.Message):
    __slots__ = ("group_name_for_points", "first_point_name")
    GROUP_NAME_FOR_POINTS_FIELD_NUMBER: _ClassVar[int]
    FIRST_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name_for_points: _spatial_analyzer_values_pb2.CollectionObjectName
    first_point_name: str
    def __init__(self, group_name_for_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., first_point_name: _Optional[str] = ...) -> None: ...

class ConstructPointsOnSurfacesByClickingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructPointsFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsFromSurfacesOnUvGridRequest(_message.Message):
    __slots__ = ("surface_list", "uv_point_group_base_name", "make_each_line_separate_group", "number_of_u_grids", "number_of_v_grids", "edge_point_mode")
    SURFACE_LIST_FIELD_NUMBER: _ClassVar[int]
    UV_POINT_GROUP_BASE_NAME_FIELD_NUMBER: _ClassVar[int]
    MAKE_EACH_LINE_SEPARATE_GROUP_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_U_GRIDS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_V_GRIDS_FIELD_NUMBER: _ClassVar[int]
    EDGE_POINT_MODE_FIELD_NUMBER: _ClassVar[int]
    surface_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    uv_point_group_base_name: str
    make_each_line_separate_group: bool
    number_of_u_grids: int
    number_of_v_grids: int
    edge_point_mode: EdgePointMode
    def __init__(self, surface_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., uv_point_group_base_name: _Optional[str] = ..., make_each_line_separate_group: bool = ..., number_of_u_grids: _Optional[int] = ..., number_of_v_grids: _Optional[int] = ..., edge_point_mode: _Optional[_Union[EdgePointMode, str]] = ...) -> None: ...

class ConstructPointsFromSurfacesOnUvGridResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointAtObjectOriginRequest(_message.Message):
    __slots__ = ("object_name", "resultant_point_name")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    resultant_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resultant_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class ConstructPointAtObjectOriginResult(_message.Message):
    __slots__ = ("origin", "execution")
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    origin: ObjectOriginResult
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, origin: _Optional[_Union[ObjectOriginResult, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsShiftedInWorkingFrameRequest(_message.Message):
    __slots__ = ("original_points", "group_for_new_points", "shift_vector")
    ORIGINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FOR_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    SHIFT_VECTOR_FIELD_NUMBER: _ClassVar[int]
    original_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_for_new_points: _spatial_analyzer_values_pb2.CollectionObjectName
    shift_vector: _spatial_analyzer_values_pb2.Vector
    def __init__(self, original_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_for_new_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., shift_vector: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class ConstructPointsShiftedInWorkingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsCylindricallyShiftedRequest(_message.Message):
    __slots__ = ("reference_object_name", "original_points", "group_for_new_points", "radial_shift", "theta_shift", "planar_shift")
    REFERENCE_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_FOR_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    RADIAL_SHIFT_FIELD_NUMBER: _ClassVar[int]
    THETA_SHIFT_FIELD_NUMBER: _ClassVar[int]
    PLANAR_SHIFT_FIELD_NUMBER: _ClassVar[int]
    reference_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    original_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_for_new_points: _spatial_analyzer_values_pb2.CollectionObjectName
    radial_shift: float
    theta_shift: float
    planar_shift: float
    def __init__(self, reference_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., original_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_for_new_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., radial_shift: _Optional[float] = ..., theta_shift: _Optional[float] = ..., planar_shift: _Optional[float] = ...) -> None: ...

class ConstructPointsCylindricallyShiftedResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsWildcardSelectionRequest(_message.Message):
    __slots__ = ("groups_to_select_from", "wildcard_selection_names", "group_for_new_points", "include_prior_complete_name")
    GROUPS_TO_SELECT_FROM_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_SELECTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_FOR_NEW_POINTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PRIOR_COMPLETE_NAME_FIELD_NUMBER: _ClassVar[int]
    groups_to_select_from: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    wildcard_selection_names: _spatial_analyzer_values_pb2.PointName
    group_for_new_points: _spatial_analyzer_values_pb2.CollectionObjectName
    include_prior_complete_name: bool
    def __init__(self, groups_to_select_from: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., wildcard_selection_names: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., group_for_new_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., include_prior_complete_name: bool = ...) -> None: ...

class ConstructPointsWildcardSelectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsSubsetWithGreatestSpacingRequest(_message.Message):
    __slots__ = ("points_to_subsample", "subset_size", "group_for_subset")
    POINTS_TO_SUBSAMPLE_FIELD_NUMBER: _ClassVar[int]
    SUBSET_SIZE_FIELD_NUMBER: _ClassVar[int]
    GROUP_FOR_SUBSET_FIELD_NUMBER: _ClassVar[int]
    points_to_subsample: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    subset_size: int
    group_for_subset: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, points_to_subsample: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., subset_size: _Optional[int] = ..., group_for_subset: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsSubsetWithGreatestSpacingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsLayoutOnGridRequest(_message.Message):
    __slots__ = ("group_name", "point_prefix", "x_min", "x_max", "x_count", "y_min", "y_max", "y_count", "z_min", "z_max", "z_count")
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    X_MIN_FIELD_NUMBER: _ClassVar[int]
    X_MAX_FIELD_NUMBER: _ClassVar[int]
    X_COUNT_FIELD_NUMBER: _ClassVar[int]
    Y_MIN_FIELD_NUMBER: _ClassVar[int]
    Y_MAX_FIELD_NUMBER: _ClassVar[int]
    Y_COUNT_FIELD_NUMBER: _ClassVar[int]
    Z_MIN_FIELD_NUMBER: _ClassVar[int]
    Z_MAX_FIELD_NUMBER: _ClassVar[int]
    Z_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    point_prefix: str
    x_min: float
    x_max: float
    x_count: int
    y_min: float
    y_max: float
    y_count: int
    z_min: float
    z_max: float
    z_count: int
    def __init__(self, group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_prefix: _Optional[str] = ..., x_min: _Optional[float] = ..., x_max: _Optional[float] = ..., x_count: _Optional[int] = ..., y_min: _Optional[float] = ..., y_max: _Optional[float] = ..., y_count: _Optional[int] = ..., z_min: _Optional[float] = ..., z_max: _Optional[float] = ..., z_count: _Optional[int] = ...) -> None: ...

class ConstructPointsLayoutOnGridResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAutoCorrespondTwoGroupsProximityRequest(_message.Message):
    __slots__ = ("reference_group", "group_to_be_copied", "same_point_tolerance", "group_to_contain_matched_points")
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_BE_COPIED_FIELD_NUMBER: _ClassVar[int]
    SAME_POINT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_CONTAIN_MATCHED_POINTS_FIELD_NUMBER: _ClassVar[int]
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    group_to_be_copied: _spatial_analyzer_values_pb2.CollectionObjectName
    same_point_tolerance: float
    group_to_contain_matched_points: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_to_be_copied: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., same_point_tolerance: _Optional[float] = ..., group_to_contain_matched_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsAutoCorrespondTwoGroupsProximityResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPointsAutoCorrespondTwoGroupsInterPointDistanceRequest(_message.Message):
    __slots__ = ("reference_group", "group_to_be_copied", "same_point_tolerance", "group_to_contain_matched_points")
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_BE_COPIED_FIELD_NUMBER: _ClassVar[int]
    SAME_POINT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TO_CONTAIN_MATCHED_POINTS_FIELD_NUMBER: _ClassVar[int]
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    group_to_be_copied: _spatial_analyzer_values_pb2.CollectionObjectName
    same_point_tolerance: float
    group_to_contain_matched_points: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_to_be_copied: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., same_point_tolerance: _Optional[float] = ..., group_to_contain_matched_points: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPointsAutoCorrespondTwoGroupsInterPointDistanceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AverageSetOfGroupsRequest(_message.Message):
    __slots__ = ("group_names", "resulting_group_name", "rms_tolerance", "maximum_absolute_tolerance", "maximum_average_tolerance")
    GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    RESULTING_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_AVERAGE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    group_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    rms_tolerance: float
    maximum_absolute_tolerance: float
    maximum_average_tolerance: float
    def __init__(self, group_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., rms_tolerance: _Optional[float] = ..., maximum_absolute_tolerance: _Optional[float] = ..., maximum_average_tolerance: _Optional[float] = ...) -> None: ...

class AverageSetOfGroupsResult(_message.Message):
    __slots__ = ("statistics", "execution")
    STATISTICS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    statistics: GroupAverageResult
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, statistics: _Optional[_Union[GroupAverageResult, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CopyGroupsExcludingObscuredPointsRequest(_message.Message):
    __slots__ = ("instrument_id", "group_names", "new_collection_name")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    NEW_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    group_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    new_collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., group_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., new_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class CopyGroupsExcludingObscuredPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointNameRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakePointNameRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_point_name", "execution")
    RESULTANT_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointNameEnsureUniqueRequest(_message.Message):
    __slots__ = ("point_name", "use_number_suffix")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_NUMBER_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    use_number_suffix: bool
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., use_number_suffix: bool = ...) -> None: ...

class MakePointNameEnsureUniqueResult(_message.Message):
    __slots__ = ("resultant_point_name", "execution")
    RESULTANT_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointNameRefListFromGroupRequest(_message.Message):
    __slots__ = ("group_name",)
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakePointNameRefListFromGroupResult(_message.Message):
    __slots__ = ("resultant_point_name_list", "execution")
    RESULTANT_POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointNameRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakePointNameRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_point_name_list", "execution")
    RESULTANT_POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointNameRefListWildcardSelectRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "group_name_wildcard_criteria", "point_name_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    group_name_wildcard_criteria: str
    point_name_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., group_name_wildcard_criteria: _Optional[str] = ..., point_name_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakePointNameRefListWildcardSelectResult(_message.Message):
    __slots__ = ("resultant_point_name_list", "execution")
    RESULTANT_POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearHiddenPointBarDatabaseRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ClearHiddenPointBarDatabaseResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateHiddenPointRodRequest(_message.Message):
    __slots__ = ("hidden_point_rod_name", "a_to_b_distance", "a_to_c_distance", "inter_point_tolerance")
    HIDDEN_POINT_ROD_NAME_FIELD_NUMBER: _ClassVar[int]
    A_TO_B_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    A_TO_C_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    INTER_POINT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    hidden_point_rod_name: str
    a_to_b_distance: float
    a_to_c_distance: float
    inter_point_tolerance: float
    def __init__(self, hidden_point_rod_name: _Optional[str] = ..., a_to_b_distance: _Optional[float] = ..., a_to_c_distance: _Optional[float] = ..., inter_point_tolerance: _Optional[float] = ...) -> None: ...

class CreateHiddenPointRodResult(_message.Message):
    __slots__ = ("hidden_point_rod_index", "execution")
    HIDDEN_POINT_ROD_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    hidden_point_rod_index: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, hidden_point_rod_index: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetHiddenPointRodIndexByNameRequest(_message.Message):
    __slots__ = ("hidden_point_rod_name",)
    HIDDEN_POINT_ROD_NAME_FIELD_NUMBER: _ClassVar[int]
    hidden_point_rod_name: str
    def __init__(self, hidden_point_rod_name: _Optional[str] = ...) -> None: ...

class GetHiddenPointRodIndexByNameResult(_message.Message):
    __slots__ = ("hidden_point_rod_index", "execution")
    HIDDEN_POINT_ROD_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    hidden_point_rod_index: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, hidden_point_rod_index: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteHiddenPointRodRequest(_message.Message):
    __slots__ = ("hidden_point_rod_index",)
    HIDDEN_POINT_ROD_INDEX_FIELD_NUMBER: _ClassVar[int]
    hidden_point_rod_index: int
    def __init__(self, hidden_point_rod_index: _Optional[int] = ...) -> None: ...

class DeleteHiddenPointRodResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateHiddenPointRequest(_message.Message):
    __slots__ = ("end_a_point_name", "end_b_point_name", "hidden_point_rod_index", "overwrite_existing_point", "point_name_to_create")
    END_A_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    END_B_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_POINT_ROD_INDEX_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_POINT_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_TO_CREATE_FIELD_NUMBER: _ClassVar[int]
    end_a_point_name: _spatial_analyzer_values_pb2.PointName
    end_b_point_name: _spatial_analyzer_values_pb2.PointName
    hidden_point_rod_index: int
    overwrite_existing_point: bool
    point_name_to_create: _spatial_analyzer_values_pb2.PointName
    def __init__(self, end_a_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., end_b_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., hidden_point_rod_index: _Optional[int] = ..., overwrite_existing_point: bool = ..., point_name_to_create: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class CreateHiddenPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPolygonizedSurfaceFromPointCloudsRequest(_message.Message):
    __slots__ = ("point_cloud_list", "mesh_orientation", "grid_resolution", "polygonized_surface_name")
    POINT_CLOUD_LIST_FIELD_NUMBER: _ClassVar[int]
    MESH_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    GRID_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    POLYGONIZED_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    point_cloud_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    mesh_orientation: MeshOrientationType
    grid_resolution: float
    polygonized_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, point_cloud_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., mesh_orientation: _Optional[_Union[MeshOrientationType, str]] = ..., grid_resolution: _Optional[float] = ..., polygonized_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructPolygonizedSurfaceFromPointCloudsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructScaleBarRequest(_message.Message):
    __slots__ = ("scale_bar_name", "begin_target", "end_target", "length", "uncertainty", "use_relative_tolerances", "use_high_tolerances", "use_low_tolerances", "high_tolerance", "low_tolerance")
    SCALE_BAR_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_TARGET_FIELD_NUMBER: _ClassVar[int]
    END_TARGET_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    USE_RELATIVE_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    USE_HIGH_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    scale_bar_name: _spatial_analyzer_values_pb2.CollectionItemName
    begin_target: _spatial_analyzer_values_pb2.PointName
    end_target: _spatial_analyzer_values_pb2.PointName
    length: float
    uncertainty: float
    use_relative_tolerances: bool
    use_high_tolerances: bool
    use_low_tolerances: bool
    high_tolerance: float
    low_tolerance: float
    def __init__(self, scale_bar_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., begin_target: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., end_target: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., length: _Optional[float] = ..., uncertainty: _Optional[float] = ..., use_relative_tolerances: bool = ..., use_high_tolerances: bool = ..., use_low_tolerances: bool = ..., high_tolerance: _Optional[float] = ..., low_tolerance: _Optional[float] = ...) -> None: ...

class ConstructScaleBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSphereRequest(_message.Message):
    __slots__ = ("sphere_name", "sphere_center", "sphere_radius")
    SPHERE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPHERE_CENTER_FIELD_NUMBER: _ClassVar[int]
    SPHERE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    sphere_name: _spatial_analyzer_values_pb2.CollectionObjectName
    sphere_center: _spatial_analyzer_values_pb2.Vector
    sphere_radius: float
    def __init__(self, sphere_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., sphere_center: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., sphere_radius: _Optional[float] = ...) -> None: ...

class ConstructSphereResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSpheresFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConstructSpheresFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfacesFromObjectsRequest(_message.Message):
    __slots__ = ("objects",)
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ConstructSurfacesFromObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromBSplinesRequest(_message.Message):
    __slots__ = ("resulting_surface_name", "b_spline_list")
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_LIST_FIELD_NUMBER: _ClassVar[int]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    b_spline_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., b_spline_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ConstructSurfaceFromBSplinesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromCylinderRequest(_message.Message):
    __slots__ = ("resulting_surface_name", "cylinder_name", "internal_cylinder", "use_theta_extent_mode")
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_NAME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_CYLINDER_FIELD_NUMBER: _ClassVar[int]
    USE_THETA_EXTENT_MODE_FIELD_NUMBER: _ClassVar[int]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cylinder_name: _spatial_analyzer_values_pb2.CollectionObjectName
    internal_cylinder: bool
    use_theta_extent_mode: bool
    def __init__(self, resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cylinder_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., internal_cylinder: bool = ..., use_theta_extent_mode: bool = ...) -> None: ...

class ConstructSurfaceFromCylinderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromPlaneRequest(_message.Message):
    __slots__ = ("resulting_surface_name", "plane_name")
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromSphereRequest(_message.Message):
    __slots__ = ("resulting_surface_name", "sphere_name")
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    SPHERE_NAME_FIELD_NUMBER: _ClassVar[int]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    sphere_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., sphere_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromSphereResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromConeRequest(_message.Message):
    __slots__ = ("resulting_surface_name", "cone_name")
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    CONE_NAME_FIELD_NUMBER: _ClassVar[int]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    cone_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., cone_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromConeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromCollectionOfSurfacesRequest(_message.Message):
    __slots__ = ("surfaces_to_combine", "resulting_surface_name", "hide_original_surfaces", "delete_original_surfaces", "enable_sewing_tolerance", "sewing_tolerance")
    SURFACES_TO_COMBINE_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    HIDE_ORIGINAL_SURFACES_FIELD_NUMBER: _ClassVar[int]
    DELETE_ORIGINAL_SURFACES_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SEWING_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    SEWING_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    surfaces_to_combine: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    hide_original_surfaces: bool
    delete_original_surfaces: bool
    enable_sewing_tolerance: bool
    sewing_tolerance: float
    def __init__(self, surfaces_to_combine: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., hide_original_surfaces: bool = ..., delete_original_surfaces: bool = ..., enable_sewing_tolerance: bool = ..., sewing_tolerance: _Optional[float] = ...) -> None: ...

class ConstructSurfaceFromCollectionOfSurfacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFitFromNominalSurfacesAndActualDataRequest(_message.Message):
    __slots__ = ("nominal_surface", "actual_data_point_list", "resulting_surface_name")
    NOMINAL_SURFACE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DATA_POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    nominal_surface: _spatial_analyzer_values_pb2.CollectionObjectName
    actual_data_point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, nominal_surface: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actual_data_point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFitFromNominalSurfacesAndActualDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceByDissectingSurfacesRequest(_message.Message):
    __slots__ = ("dissection_mode",)
    DISSECTION_MODE_FIELD_NUMBER: _ClassVar[int]
    dissection_mode: SurfaceDissectionMode
    def __init__(self, dissection_mode: _Optional[_Union[SurfaceDissectionMode, str]] = ...) -> None: ...

class ConstructSurfaceByDissectingSurfacesResult(_message.Message):
    __slots__ = ("resultant_surfaces_list", "execution")
    RESULTANT_SURFACES_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_surfaces_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_surfaces_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfacesByDissectingSurfacesFromRefListRequest(_message.Message):
    __slots__ = ("surfaces_to_dissect",)
    SURFACES_TO_DISSECT_FIELD_NUMBER: _ClassVar[int]
    surfaces_to_dissect: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, surfaces_to_dissect: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ConstructSurfacesByDissectingSurfacesFromRefListResult(_message.Message):
    __slots__ = ("resultant_surfaces_list", "execution")
    RESULTANT_SURFACES_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_surfaces_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_surfaces_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromPointGroupsRequest(_message.Message):
    __slots__ = ("group_name_list", "b_spline_fit_options", "resulting_surface_name")
    GROUP_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    B_SPLINE_FIT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    group_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    b_spline_fit_options: BSplineFitOptions
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, group_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., b_spline_fit_options: _Optional[_Union[BSplineFitOptions, _Mapping]] = ..., resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromPointGroupsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfacesByProjectingPointsRequest(_message.Message):
    __slots__ = ("projection_target_name_list", "point_list", "resulting_surface_name")
    PROJECTION_TARGET_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    POINT_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    projection_target_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, projection_target_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfacesByProjectingPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceByOffsettingSurfaceRequest(_message.Message):
    __slots__ = ("reference_surface", "surface_offset", "hide_original_surface")
    REFERENCE_SURFACE_FIELD_NUMBER: _ClassVar[int]
    SURFACE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    HIDE_ORIGINAL_SURFACE_FIELD_NUMBER: _ClassVar[int]
    reference_surface: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    surface_offset: float
    hide_original_surface: bool
    def __init__(self, reference_surface: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., surface_offset: _Optional[float] = ..., hide_original_surface: bool = ...) -> None: ...

class ConstructSurfaceByOffsettingSurfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromAnnotationLinksRequest(_message.Message):
    __slots__ = ("annotation_list", "resulting_surface_name")
    ANNOTATION_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULTING_SURFACE_NAME_FIELD_NUMBER: _ClassVar[int]
    annotation_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_surface_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, annotation_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_surface_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructSurfaceFromAnnotationLinksResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructGeometryFromSurfacesRequest(_message.Message):
    __slots__ = ("surfaces", "minimum_diameter", "maximum_diameter", "reference_frame", "destination_collection_name", "base_name")
    SURFACES_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FIELD_NUMBER: _ClassVar[int]
    surfaces: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    minimum_diameter: float
    maximum_diameter: float
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    destination_collection_name: _spatial_analyzer_values_pb2.CollectionName
    base_name: str
    def __init__(self, surfaces: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., minimum_diameter: _Optional[float] = ..., maximum_diameter: _Optional[float] = ..., reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., destination_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., base_name: _Optional[str] = ...) -> None: ...

class ConstructGeometryFromSurfacesResult(_message.Message):
    __slots__ = ("geometry_objects", "execution")
    GEOMETRY_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    geometry_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, geometry_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupGroupToGroupCompareRequest(_message.Message):
    __slots__ = ("vector_group_name", "group_a", "group_b", "rms_deviation_tolerance", "max_absolute_deviation_tolerance", "average_deviation_tolerance")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_A_FIELD_NUMBER: _ClassVar[int]
    GROUP_B_FIELD_NUMBER: _ClassVar[int]
    RMS_DEVIATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAX_ABSOLUTE_DEVIATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    group_a: _spatial_analyzer_values_pb2.CollectionObjectName
    group_b: _spatial_analyzer_values_pb2.CollectionObjectName
    rms_deviation_tolerance: float
    max_absolute_deviation_tolerance: float
    average_deviation_tolerance: float
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_a: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., group_b: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., rms_deviation_tolerance: _Optional[float] = ..., max_absolute_deviation_tolerance: _Optional[float] = ..., average_deviation_tolerance: _Optional[float] = ...) -> None: ...

class ConstructVectorGroupGroupToGroupCompareResult(_message.Message):
    __slots__ = ("vector_count", "rms_deviation", "max_absolute_deviation", "average_deviation", "execution")
    VECTOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAX_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_count: int
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_count: _Optional[int] = ..., rms_deviation: _Optional[float] = ..., max_absolute_deviation: _Optional[float] = ..., average_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupAreaProfileCheckRequest(_message.Message):
    __slots__ = ("reference_vectors", "vector_groups_to_check", "area_radius", "area_tolerance", "resultant_vector_group_name")
    REFERENCE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUPS_TO_CHECK_FIELD_NUMBER: _ClassVar[int]
    AREA_RADIUS_FIELD_NUMBER: _ClassVar[int]
    AREA_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    reference_vectors: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    vector_groups_to_check: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionVectorGroupName]
    area_radius: float
    area_tolerance: float
    resultant_vector_group_name: _spatial_analyzer_values_pb2.CollectionVectorGroupName
    def __init__(self, reference_vectors: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., vector_groups_to_check: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]]] = ..., area_radius: _Optional[float] = ..., area_tolerance: _Optional[float] = ..., resultant_vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupAreaProfileCheckResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupFromVectorNameRefListRequest(_message.Message):
    __slots__ = ("vector_name_list", "resultant_vector_group_name")
    VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    resultant_vector_group_name: _spatial_analyzer_values_pb2.CollectionVectorGroupName
    def __init__(self, vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., resultant_vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupFromVectorNameRefListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorInWorkingCoordinatesBeginDeltaRequest(_message.Message):
    __slots__ = ("vector_group_name", "new_vector_name", "begin_in_working_coordinates", "delta_in_working_coordinates", "is_magnitude_negative")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    DELTA_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    IS_MAGNITUDE_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    new_vector_name: str
    begin_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    delta_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    is_magnitude_negative: bool
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., new_vector_name: _Optional[str] = ..., begin_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., delta_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., is_magnitude_negative: bool = ...) -> None: ...

class ConstructVectorInWorkingCoordinatesBeginDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorInWorkingCoordinatesBeginDirectionMagnitudeRequest(_message.Message):
    __slots__ = ("vector_group_name", "new_vector_name", "begin_in_working_coordinates", "direction_in_working_coordinates", "signed_magnitude")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_IN_WORKING_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    SIGNED_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    new_vector_name: str
    begin_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    direction_in_working_coordinates: _spatial_analyzer_values_pb2.Vector
    signed_magnitude: float
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., new_vector_name: _Optional[str] = ..., begin_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., direction_in_working_coordinates: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., signed_magnitude: _Optional[float] = ...) -> None: ...

class ConstructVectorInWorkingCoordinatesBeginDirectionMagnitudeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupFromRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "vector_group_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_group_name: _spatial_analyzer_values_pb2.CollectionVectorGroupName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]] = ...) -> None: ...

class ConstructVectorGroupFromRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeVectorNameRefListFromVectorGroupRequest(_message.Message):
    __slots__ = ("vector_group_name",)
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeVectorNameRefListFromVectorGroupResult(_message.Message):
    __slots__ = ("resultant_vector_name_list", "execution")
    RESULTANT_VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeVectorNameRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeVectorNameRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_vector_name_list", "execution")
    RESULTANT_VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionVectorGroupNameRefListRuntimeSelectRequest(_message.Message):
    __slots__ = ("user_prompt",)
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    user_prompt: str
    def __init__(self, user_prompt: _Optional[str] = ...) -> None: ...

class MakeCollectionVectorGroupNameRefListRuntimeSelectResult(_message.Message):
    __slots__ = ("resultant_collection_vector_group_name_reference_list", "execution")
    RESULTANT_COLLECTION_VECTOR_GROUP_NAME_REFERENCE_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_collection_vector_group_name_reference_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionVectorGroupName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_collection_vector_group_name_reference_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeVectorNamesUniqueInVectorGroupRequest(_message.Message):
    __slots__ = ("vector_group_name",)
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeVectorNamesUniqueInVectorGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MirrorObjectsRequest(_message.Message):
    __slots__ = ("objects", "frame_name", "frame_plane_to_mirror_around", "copy")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    FRAME_PLANE_TO_MIRROR_AROUND_FIELD_NUMBER: _ClassVar[int]
    COPY_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    frame_plane_to_mirror_around: MirrorFramePlane
    copy: bool
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., frame_plane_to_mirror_around: _Optional[_Union[MirrorFramePlane, str]] = ..., copy: bool = ...) -> None: ...

class MirrorObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CopyObjectRequest(_message.Message):
    __slots__ = ("source_object", "new_object_name", "overwrite_if_exists")
    SOURCE_OBJECT_FIELD_NUMBER: _ClassVar[int]
    NEW_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    source_object: _spatial_analyzer_values_pb2.CollectionObjectName
    new_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    overwrite_if_exists: bool
    def __init__(self, source_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., new_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class CopyObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CopyObjectsToACollectionRequest(_message.Message):
    __slots__ = ("source_objects", "destination_collection_name")
    SOURCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    source_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    destination_collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, source_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., destination_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class CopyObjectsToACollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveObjectsToACollectionRequest(_message.Message):
    __slots__ = ("source_objects", "destination_collection_name")
    SOURCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    source_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    destination_collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, source_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., destination_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MoveObjectsToACollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CopyObjectsPointToPointDeltaRequest(_message.Message):
    __slots__ = ("objects_to_copy", "first_delta_point", "second_delta_point", "destination_collection_name")
    OBJECTS_TO_COPY_FIELD_NUMBER: _ClassVar[int]
    FIRST_DELTA_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_DELTA_POINT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    objects_to_copy: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    first_delta_point: _spatial_analyzer_values_pb2.PointName
    second_delta_point: _spatial_analyzer_values_pb2.PointName
    destination_collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, objects_to_copy: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., first_delta_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_delta_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., destination_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class CopyObjectsPointToPointDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveObjectsPointToPointDeltaRequest(_message.Message):
    __slots__ = ("objects_to_move", "first_delta_point", "second_delta_point")
    OBJECTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    FIRST_DELTA_POINT_FIELD_NUMBER: _ClassVar[int]
    SECOND_DELTA_POINT_FIELD_NUMBER: _ClassVar[int]
    objects_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    first_delta_point: _spatial_analyzer_values_pb2.PointName
    second_delta_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, objects_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., first_delta_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_delta_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class MoveObjectsPointToPointDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenamePointRequest(_message.Message):
    __slots__ = ("original_point_name", "new_point_name", "overwrite_if_exists")
    ORIGINAL_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_point_name: _spatial_analyzer_values_pb2.PointName
    new_point_name: _spatial_analyzer_values_pb2.PointName
    overwrite_if_exists: bool
    def __init__(self, original_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., new_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenamePointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenamePointsWithNamePatternRequest(_message.Message):
    __slots__ = ("point_names", "name_pattern", "start_value")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    START_VALUE_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    name_pattern: str
    start_value: int
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., name_pattern: _Optional[str] = ..., start_value: _Optional[int] = ...) -> None: ...

class RenamePointsWithNamePatternResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameCollectionRequest(_message.Message):
    __slots__ = ("original_collection_name", "new_collection_name")
    ORIGINAL_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    original_collection_name: _spatial_analyzer_values_pb2.CollectionName
    new_collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, original_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., new_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class RenameCollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameObjectRequest(_message.Message):
    __slots__ = ("original_object_name", "new_object_name", "overwrite_if_exists")
    ORIGINAL_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    new_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    overwrite_if_exists: bool
    def __init__(self, original_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., new_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenameObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameItemRequest(_message.Message):
    __slots__ = ("original_item_name", "new_item_name", "overwrite_if_exists")
    ORIGINAL_ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_item_name: _spatial_analyzer_values_pb2.CollectionItemName
    new_item_name: _spatial_analyzer_values_pb2.CollectionItemName
    overwrite_if_exists: bool
    def __init__(self, original_item_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., new_item_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenameItemResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeletePointsRequest(_message.Message):
    __slots__ = ("point_names",)
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class DeletePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeletePointsWildcardSelectionRequest(_message.Message):
    __slots__ = ("groups_to_delete_from", "wildcard_selection_names")
    GROUPS_TO_DELETE_FROM_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_SELECTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    groups_to_delete_from: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    wildcard_selection_names: _spatial_analyzer_values_pb2.PointName
    def __init__(self, groups_to_delete_from: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., wildcard_selection_names: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class DeletePointsWildcardSelectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructObjectsFromSurfaceFacesRuntimeSelectRequest(_message.Message):
    __slots__ = ("construct_planes", "construct_cylinders", "construct_spheres", "construct_cones", "construct_lines", "construct_points", "construct_circles")
    CONSTRUCT_PLANES_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_CYLINDERS_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_SPHERES_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_CONES_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_LINES_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_POINTS_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCT_CIRCLES_FIELD_NUMBER: _ClassVar[int]
    construct_planes: bool
    construct_cylinders: bool
    construct_spheres: bool
    construct_cones: bool
    construct_lines: bool
    construct_points: bool
    construct_circles: bool
    def __init__(self, construct_planes: bool = ..., construct_cylinders: bool = ..., construct_spheres: bool = ..., construct_cones: bool = ..., construct_lines: bool = ..., construct_points: bool = ..., construct_circles: bool = ...) -> None: ...

class ConstructObjectsFromSurfaceFacesRuntimeSelectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
