from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DynamicCircleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_CIRCLE_MODE_UNSPECIFIED: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CYLINDER_AND_PLANE_HOLD_PLANE_NORMAL: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CYLINDER_AND_PLANE_HOLD_CYLINDER_AXIS: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_AND_PLANE_HOLD_PLANE_NORMAL: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_AND_PLANE_HOLD_CONE_AXIS: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_SPHERE_AND_PLANE_INTERSECTION: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_TWO_CONES_INTERSECTION: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_AND_CYLINDER_INTERSECTION: _ClassVar[DynamicCircleMode]

class DynamicEllipseMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_ELLIPSE_MODE_UNSPECIFIED: _ClassVar[DynamicEllipseMode]
    DYNAMIC_ELLIPSE_MODE_CYLINDER_AND_PLANE_INTERSECTION: _ClassVar[DynamicEllipseMode]
    DYNAMIC_ELLIPSE_MODE_CONE_AND_PLANE_INTERSECTION: _ClassVar[DynamicEllipseMode]

class DynamicLineMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_LINE_MODE_UNSPECIFIED: _ClassVar[DynamicLineMode]
    DYNAMIC_LINE_MODE_CONE_AXIS: _ClassVar[DynamicLineMode]
    DYNAMIC_LINE_MODE_CYLINDER_AXIS: _ClassVar[DynamicLineMode]
    DYNAMIC_LINE_MODE_INTERSECTION_OF_TWO_PLANES: _ClassVar[DynamicLineMode]
    DYNAMIC_LINE_MODE_BISECT_TWO_LINES: _ClassVar[DynamicLineMode]
    DYNAMIC_LINE_MODE_SLOT_CENTERLINE_ALONG_LENGTH: _ClassVar[DynamicLineMode]

class DynamicPlaneMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_PLANE_MODE_UNSPECIFIED: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_BISECT_TWO_PLANES: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_BEST_FIT_PLANE: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_FIRST_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_SECOND_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_BEST_FIT_PLANE: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_CYLINDER_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_OFFSET_PLANE_FROM_PLANE: _ClassVar[DynamicPlaneMode]

class DynamicPointMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_POINT_MODE_UNSPECIFIED: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_LINE_AND_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_CYLINDER_AND_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_CONE_AND_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_THREE_PLANES: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_MID_POINT_PERPENDICULAR_TO_TWO_LINES: _ClassVar[DynamicPointMode]

class GeometryRelationshipPointEditMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_UNSPECIFIED: _ClassVar[GeometryRelationshipPointEditMode]
    GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_POINT_LIST: _ClassVar[GeometryRelationshipPointEditMode]
    GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_POINT_GRAPH: _ClassVar[GeometryRelationshipPointEditMode]
    GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_SUB_SAMPLER_SETTINGS: _ClassVar[GeometryRelationshipPointEditMode]

class SolverMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOLVER_MODE_UNSPECIFIED: _ClassVar[SolverMode]
    SOLVER_MODE_GAUSS_NEWTON: _ClassVar[SolverMode]
    SOLVER_MODE_LEVENBERG_MARQUARDT: _ClassVar[SolverMode]
    SOLVER_MODE_GAUSS_NEWTON_WITH_GRADIENT_SEARCH: _ClassVar[SolverMode]
    SOLVER_MODE_DIRECT_SEARCH: _ClassVar[SolverMode]
DYNAMIC_CIRCLE_MODE_UNSPECIFIED: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CYLINDER_AND_PLANE_HOLD_PLANE_NORMAL: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CYLINDER_AND_PLANE_HOLD_CYLINDER_AXIS: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_AND_PLANE_HOLD_PLANE_NORMAL: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_AND_PLANE_HOLD_CONE_AXIS: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_SPHERE_AND_PLANE_INTERSECTION: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_TWO_CONES_INTERSECTION: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_AND_CYLINDER_INTERSECTION: DynamicCircleMode
DYNAMIC_ELLIPSE_MODE_UNSPECIFIED: DynamicEllipseMode
DYNAMIC_ELLIPSE_MODE_CYLINDER_AND_PLANE_INTERSECTION: DynamicEllipseMode
DYNAMIC_ELLIPSE_MODE_CONE_AND_PLANE_INTERSECTION: DynamicEllipseMode
DYNAMIC_LINE_MODE_UNSPECIFIED: DynamicLineMode
DYNAMIC_LINE_MODE_CONE_AXIS: DynamicLineMode
DYNAMIC_LINE_MODE_CYLINDER_AXIS: DynamicLineMode
DYNAMIC_LINE_MODE_INTERSECTION_OF_TWO_PLANES: DynamicLineMode
DYNAMIC_LINE_MODE_BISECT_TWO_LINES: DynamicLineMode
DYNAMIC_LINE_MODE_SLOT_CENTERLINE_ALONG_LENGTH: DynamicLineMode
DYNAMIC_PLANE_MODE_UNSPECIFIED: DynamicPlaneMode
DYNAMIC_PLANE_MODE_BISECT_TWO_PLANES: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_BEST_FIT_PLANE: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_FIRST_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_HOLD_NORMAL_TO_SECOND_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_BEST_FIT_PLANE: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_AND_CYLINDER_HOLD_NORMAL_TO_CYLINDER_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_OFFSET_PLANE_FROM_PLANE: DynamicPlaneMode
DYNAMIC_POINT_MODE_UNSPECIFIED: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_LINE_AND_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_CYLINDER_AND_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_CONE_AND_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_THREE_PLANES: DynamicPointMode
DYNAMIC_POINT_MODE_MID_POINT_PERPENDICULAR_TO_TWO_LINES: DynamicPointMode
GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_UNSPECIFIED: GeometryRelationshipPointEditMode
GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_POINT_LIST: GeometryRelationshipPointEditMode
GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_POINT_GRAPH: GeometryRelationshipPointEditMode
GEOMETRY_RELATIONSHIP_POINT_EDIT_MODE_SUB_SAMPLER_SETTINGS: GeometryRelationshipPointEditMode
SOLVER_MODE_UNSPECIFIED: SolverMode
SOLVER_MODE_GAUSS_NEWTON: SolverMode
SOLVER_MODE_LEVENBERG_MARQUARDT: SolverMode
SOLVER_MODE_GAUSS_NEWTON_WITH_GRADIENT_SEARCH: SolverMode
SOLVER_MODE_DIRECT_SEARCH: SolverMode

class EnableDisableRelationshipsForOptimizationRequest(_message.Message):
    __slots__ = ("relationships", "enable")
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    enable: bool
    def __init__(self, relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., enable: bool = ...) -> None: ...

class EnableDisableRelationshipsForOptimizationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GeomRelationshipIgnoreInputPointsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GeomRelationshipIgnoreInputPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GeomRelationshipReuseIgnoredInputPointsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GeomRelationshipReuseIgnoredInputPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipAutoVectorsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipAutoVectorsResult(_message.Message):
    __slots__ = ("auto_vectors_nominal_avn_enabled", "auto_vectors_nominal_avn_name", "auto_vectors_fit_avf_enabled", "auto_vectors_fit_avf_name", "points_type", "execution")
    AUTO_VECTORS_NOMINAL_AVN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_VECTORS_NOMINAL_AVN_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_VECTORS_FIT_AVF_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTO_VECTORS_FIT_AVF_NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    auto_vectors_nominal_avn_enabled: bool
    auto_vectors_nominal_avn_name: _spatial_analyzer_values_pb2.CollectionObjectName
    auto_vectors_fit_avf_enabled: bool
    auto_vectors_fit_avf_name: _spatial_analyzer_values_pb2.CollectionObjectName
    points_type: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, auto_vectors_nominal_avn_enabled: bool = ..., auto_vectors_nominal_avn_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., auto_vectors_fit_avf_enabled: bool = ..., auto_vectors_fit_avf_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., points_type: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipCardinalPointsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipCardinalPointsResult(_message.Message):
    __slots__ = ("cardinal_point_name_list", "execution")
    CARDINAL_POINT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    cardinal_point_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, cardinal_point_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipCriteriaRequest(_message.Message):
    __slots__ = ("relationship_name", "criteria")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    criteria: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., criteria: _Optional[str] = ...) -> None: ...

class GetGeomRelationshipCriteriaResult(_message.Message):
    __slots__ = ("nominal", "measured", "delta", "low_tolerance", "high_tolerance", "optimization_delta_weight", "optimization_out_of_tolerance_weight", "is_within_tolerance", "has_uncertainty", "uncertainty", "execution")
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    MEASURED_FIELD_NUMBER: _ClassVar[int]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_DELTA_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OUT_OF_TOLERANCE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    IS_WITHIN_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HAS_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    nominal: float
    measured: float
    delta: float
    low_tolerance: float
    high_tolerance: float
    optimization_delta_weight: float
    optimization_out_of_tolerance_weight: float
    is_within_tolerance: str
    has_uncertainty: bool
    uncertainty: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, nominal: _Optional[float] = ..., measured: _Optional[float] = ..., delta: _Optional[float] = ..., low_tolerance: _Optional[float] = ..., high_tolerance: _Optional[float] = ..., optimization_delta_weight: _Optional[float] = ..., optimization_out_of_tolerance_weight: _Optional[float] = ..., is_within_tolerance: _Optional[str] = ..., has_uncertainty: bool = ..., uncertainty: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipMeasuredAvgPointRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipMeasuredAvgPointResult(_message.Message):
    __slots__ = ("measured_average_point", "execution")
    MEASURED_AVERAGE_POINT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    measured_average_point: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, measured_average_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipMeasuredGeometryRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipMeasuredGeometryResult(_message.Message):
    __slots__ = ("measured_geometry", "execution")
    MEASURED_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    measured_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, measured_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipNominalAvgPointRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipNominalAvgPointResult(_message.Message):
    __slots__ = ("nominal_average_point", "execution")
    NOMINAL_AVERAGE_POINT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    nominal_average_point: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, nominal_average_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipNominalGeometryRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipNominalGeometryResult(_message.Message):
    __slots__ = ("nominal_geometry", "execution")
    NOMINAL_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    nominal_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, nominal_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipPointListRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipPointListResult(_message.Message):
    __slots__ = ("all_points", "used_points", "ignored_points", "execution")
    ALL_POINTS_FIELD_NUMBER: _ClassVar[int]
    USED_POINTS_FIELD_NUMBER: _ClassVar[int]
    IGNORED_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    all_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    used_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    ignored_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, all_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., used_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., ignored_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipProjectionPlaneRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipProjectionPlaneResult(_message.Message):
    __slots__ = ("projection_plane_name", "execution")
    PROJECTION_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    projection_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, projection_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipCutStatusRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipCutStatusResult(_message.Message):
    __slots__ = ("pipe_1_cut_available", "pipe_1_cut_active", "pipe_2_cut_available", "pipe_2_cut_active", "execution")
    PIPE_1_CUT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CUT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    pipe_1_cut_available: bool
    pipe_1_cut_active: bool
    pipe_2_cut_available: bool
    pipe_2_cut_active: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, pipe_1_cut_available: bool = ..., pipe_1_cut_active: bool = ..., pipe_2_cut_available: bool = ..., pipe_2_cut_active: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipPropertiesRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipPropertiesResult(_message.Message):
    __slots__ = ("pipe_1_object_name", "pipe_1_inner_diameter", "pipe_1_outer_diameter", "pipe_1_cut_begin", "pipe_1_cut_end", "pipe_2_object_name", "pipe_2_inner_diameter", "pipe_2_outer_diameter", "pipe_2_cut_begin", "pipe_2_cut_end", "execution")
    PIPE_1_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_INNER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_OUTER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CUT_BEGIN_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CUT_END_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_INNER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_OUTER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_BEGIN_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_END_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    pipe_1_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_1_inner_diameter: float
    pipe_1_outer_diameter: float
    pipe_1_cut_begin: float
    pipe_1_cut_end: float
    pipe_2_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_2_inner_diameter: float
    pipe_2_outer_diameter: float
    pipe_2_cut_begin: float
    pipe_2_cut_end: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, pipe_1_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_1_inner_diameter: _Optional[float] = ..., pipe_1_outer_diameter: _Optional[float] = ..., pipe_1_cut_begin: _Optional[float] = ..., pipe_1_cut_end: _Optional[float] = ..., pipe_2_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_2_inner_diameter: _Optional[float] = ..., pipe_2_outer_diameter: _Optional[float] = ..., pipe_2_cut_begin: _Optional[float] = ..., pipe_2_cut_end: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipWeightsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetPipeRelationshipWeightsResult(_message.Message):
    __slots__ = ("overall_weight", "axis_offset", "axis_alignment", "center_pull", "out_of_material_weight", "out_of_material_static_offset", "constrain_region_at_od", "constrain_id_od_overlap", "execution")
    OVERALL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    AXIS_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AXIS_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CENTER_PULL_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_MATERIAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_MATERIAL_STATIC_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_REGION_AT_OD_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_ID_OD_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    overall_weight: float
    axis_offset: float
    axis_alignment: float
    center_pull: float
    out_of_material_weight: float
    out_of_material_static_offset: float
    constrain_region_at_od: bool
    constrain_id_od_overlap: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, overall_weight: _Optional[float] = ..., axis_offset: _Optional[float] = ..., axis_alignment: _Optional[float] = ..., center_pull: _Optional[float] = ..., out_of_material_weight: _Optional[float] = ..., out_of_material_static_offset: _Optional[float] = ..., constrain_region_at_od: bool = ..., constrain_id_od_overlap: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipFitConstraintsScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipFitConstraintsScalarTypeResult(_message.Message):
    __slots__ = ("use_high_tolerance", "high_tolerance", "use_low_tolerance", "low_tolerance", "fit_constraint_options", "execution")
    USE_HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    FIT_CONSTRAINT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_high_tolerance: bool
    high_tolerance: float
    use_low_tolerance: bool
    low_tolerance: float
    fit_constraint_options: _spatial_analyzer_values_pb2.FitConstraintScalarOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_high_tolerance: bool = ..., high_tolerance: _Optional[float] = ..., use_low_tolerance: bool = ..., low_tolerance: _Optional[float] = ..., fit_constraint_options: _Optional[_Union[_spatial_analyzer_values_pb2.FitConstraintScalarOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipOutlierRejectionScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipOutlierRejectionScalarTypeResult(_message.Message):
    __slots__ = ("use_high_limit", "high_limit", "use_low_limit", "low_limit", "execution")
    USE_HIGH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HIGH_LIMIT_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_high_limit: bool
    high_limit: float
    use_low_limit: bool
    low_limit: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_high_limit: bool = ..., high_limit: _Optional[float] = ..., use_low_limit: bool = ..., low_limit: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipProjectionOptionsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipProjectionOptionsResult(_message.Message):
    __slots__ = ("ignore_edge_projections", "probe_offsets_override_target_values", "probe_offsets_override_value", "add_extra_material", "extra_material_thickness", "execution")
    IGNORE_EDGE_PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    PROBE_OFFSETS_OVERRIDE_TARGET_VALUES_FIELD_NUMBER: _ClassVar[int]
    PROBE_OFFSETS_OVERRIDE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADD_EXTRA_MATERIAL_FIELD_NUMBER: _ClassVar[int]
    EXTRA_MATERIAL_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ignore_edge_projections: bool
    probe_offsets_override_target_values: bool
    probe_offsets_override_value: float
    add_extra_material: bool
    extra_material_thickness: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, ignore_edge_projections: bool = ..., probe_offsets_override_target_values: bool = ..., probe_offsets_override_value: _Optional[float] = ..., add_extra_material: bool = ..., extra_material_thickness: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipReportingFrameRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipReportingFrameResult(_message.Message):
    __slots__ = ("reporting_frame", "execution")
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipSubSamplingOptionsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipSubSamplingOptionsResult(_message.Message):
    __slots__ = ("use_every_ith_point", "i_value", "use_no_more_than_n_points", "n_value", "execution")
    USE_EVERY_ITH_POINT_FIELD_NUMBER: _ClassVar[int]
    I_VALUE_FIELD_NUMBER: _ClassVar[int]
    USE_NO_MORE_THAN_N_POINTS_FIELD_NUMBER: _ClassVar[int]
    N_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_every_ith_point: bool
    i_value: int
    use_no_more_than_n_points: bool
    n_value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_every_ith_point: bool = ..., i_value: _Optional[int] = ..., use_no_more_than_n_points: bool = ..., n_value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipToleranceScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipToleranceScalarTypeResult(_message.Message):
    __slots__ = ("use_high_tolerance", "high_tolerance", "use_low_tolerance", "low_tolerance", "tolerance_options", "execution")
    USE_HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_high_tolerance: bool
    high_tolerance: float
    use_low_tolerance: bool
    low_tolerance: float
    tolerance_options: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_high_tolerance: bool = ..., high_tolerance: _Optional[float] = ..., use_low_tolerance: bool = ..., low_tolerance: _Optional[float] = ..., tolerance_options: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipToleranceVectorTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipToleranceVectorTypeResult(_message.Message):
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

class GetRelationshipTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipTypeResult(_message.Message):
    __slots__ = ("relationship_type", "execution")
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    relationship_type: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, relationship_type: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipWeightingRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetRelationshipWeightingResult(_message.Message):
    __slots__ = ("weight", "execution")
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    weight: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, weight: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePipeFittingRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "pipe_1_object_name", "pipe_2_object_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_1_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_2_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_1_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_2_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakePipeFittingRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePipeRelationshipCutRequest(_message.Message):
    __slots__ = ("relationship_name", "pipe_1_make_cut", "pipe_1_create_frame", "pipe_1_frame_name", "pipe_2_make_cut", "pipe_2_create_frame", "pipe_2_frame_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_MAKE_CUT_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CREATE_FRAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_MAKE_CUT_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CREATE_FRAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_1_make_cut: bool
    pipe_1_create_frame: bool
    pipe_1_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_2_make_cut: bool
    pipe_2_create_frame: bool
    pipe_2_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_1_make_cut: bool = ..., pipe_1_create_frame: bool = ..., pipe_1_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_2_make_cut: bool = ..., pipe_2_create_frame: bool = ..., pipe_2_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakePipeRelationshipCutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PipeRelationshipForceCutToFrameRequest(_message.Message):
    __slots__ = ("relationship_name", "pipe_1_force_cut_to_frame", "pipe_1_frame_name", "pipe_2_force_cut_to_frame", "pipe_2_frame_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_FORCE_CUT_TO_FRAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_FORCE_CUT_TO_FRAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_1_force_cut_to_frame: bool
    pipe_1_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_2_force_cut_to_frame: bool
    pipe_2_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_1_force_cut_to_frame: bool = ..., pipe_1_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_2_force_cut_to_frame: bool = ..., pipe_2_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class PipeRelationshipForceCutToFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipAutoVectorsNominalAvnRequest(_message.Message):
    __slots__ = ("relationship_name", "create_auto_vectors_avn", "points_type")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_AUTO_VECTORS_AVN_FIELD_NUMBER: _ClassVar[int]
    POINTS_TYPE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    create_auto_vectors_avn: bool
    points_type: _spatial_analyzer_values_pb2.PointFilterInputType
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., create_auto_vectors_avn: bool = ..., points_type: _Optional[_Union[_spatial_analyzer_values_pb2.PointFilterInputType, str]] = ...) -> None: ...

class SetGeomRelationshipAutoVectorsNominalAvnResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipCardinalPointsRequest(_message.Message):
    __slots__ = ("relationship_name", "create_cardinal_pts_when_fitting", "prefix_cardinal_pts_name_with_rel_name", "cardinal_pts_group_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_CARDINAL_PTS_WHEN_FITTING_FIELD_NUMBER: _ClassVar[int]
    PREFIX_CARDINAL_PTS_NAME_WITH_REL_NAME_FIELD_NUMBER: _ClassVar[int]
    CARDINAL_PTS_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    create_cardinal_pts_when_fitting: bool
    prefix_cardinal_pts_name_with_rel_name: bool
    cardinal_pts_group_name: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., create_cardinal_pts_when_fitting: bool = ..., prefix_cardinal_pts_name_with_rel_name: bool = ..., cardinal_pts_group_name: _Optional[str] = ...) -> None: ...

class SetGeomRelationshipCardinalPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipCriteriaRequest(_message.Message):
    __slots__ = ("relationship_name", "criteria", "show_in_report", "tolerance_options", "optimization_delta_weight", "optimization_out_of_tolerance_weight")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    SHOW_IN_REPORT_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_DELTA_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATION_OUT_OF_TOLERANCE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    criteria: str
    show_in_report: bool
    tolerance_options: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    optimization_delta_weight: float
    optimization_out_of_tolerance_weight: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., criteria: _Optional[str] = ..., show_in_report: bool = ..., tolerance_options: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ..., optimization_delta_weight: _Optional[float] = ..., optimization_out_of_tolerance_weight: _Optional[float] = ...) -> None: ...

class SetGeomRelationshipCriteriaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipMeasuredGeometryRequest(_message.Message):
    __slots__ = ("relationship_name", "measured_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    measured_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measured_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipMeasuredGeometryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipNominalAvgPointRequest(_message.Message):
    __slots__ = ("relationship_name", "compare_to_nominal", "nominal_average_point")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARE_TO_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_AVERAGE_POINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    compare_to_nominal: bool
    nominal_average_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., compare_to_nominal: bool = ..., nominal_average_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipNominalAvgPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipNominalGeometryRequest(_message.Message):
    __slots__ = ("relationship_name", "compare_to_nominal", "nominal_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPARE_TO_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    compare_to_nominal: bool
    nominal_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., compare_to_nominal: bool = ..., nominal_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipNominalGeometryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipProjectionPlaneRequest(_message.Message):
    __slots__ = ("relationship_name", "project_to_plane", "projection_plane_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TO_PLANE_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_PLANE_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    project_to_plane: bool
    projection_plane_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., project_to_plane: bool = ..., projection_plane_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipProjectionPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectToObjectDirectionRelationshipFitConstraintsRequest(_message.Message):
    __slots__ = ("relationship_name", "angle_between_vectors_fit_constraints", "mutual_perpendicular_length_fit_constraints")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    ANGLE_BETWEEN_VECTORS_FIT_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_PERPENDICULAR_LENGTH_FIT_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    angle_between_vectors_fit_constraints: _spatial_analyzer_values_pb2.FitConstraintScalarOptions
    mutual_perpendicular_length_fit_constraints: _spatial_analyzer_values_pb2.FitConstraintScalarOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., angle_between_vectors_fit_constraints: _Optional[_Union[_spatial_analyzer_values_pb2.FitConstraintScalarOptions, _Mapping]] = ..., mutual_perpendicular_length_fit_constraints: _Optional[_Union[_spatial_analyzer_values_pb2.FitConstraintScalarOptions, _Mapping]] = ...) -> None: ...

class SetObjectToObjectDirectionRelationshipFitConstraintsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPipeRelationshipSegmentPropertiesRequest(_message.Message):
    __slots__ = ("relationship_name", "pipe_1_inner_diameter", "pipe_1_outer_diameter", "pipe_1_cut_begin", "pipe_1_cut_end", "pipe_2_inner_diameter", "pipe_2_outer_diameter", "pipe_2_cut_begin", "pipe_2_cut_end")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_INNER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_OUTER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CUT_BEGIN_FIELD_NUMBER: _ClassVar[int]
    PIPE_1_CUT_END_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_INNER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_OUTER_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_BEGIN_FIELD_NUMBER: _ClassVar[int]
    PIPE_2_CUT_END_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    pipe_1_inner_diameter: float
    pipe_1_outer_diameter: float
    pipe_1_cut_begin: float
    pipe_1_cut_end: float
    pipe_2_inner_diameter: float
    pipe_2_outer_diameter: float
    pipe_2_cut_begin: float
    pipe_2_cut_end: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., pipe_1_inner_diameter: _Optional[float] = ..., pipe_1_outer_diameter: _Optional[float] = ..., pipe_1_cut_begin: _Optional[float] = ..., pipe_1_cut_end: _Optional[float] = ..., pipe_2_inner_diameter: _Optional[float] = ..., pipe_2_outer_diameter: _Optional[float] = ..., pipe_2_cut_begin: _Optional[float] = ..., pipe_2_cut_end: _Optional[float] = ...) -> None: ...

class SetPipeRelationshipSegmentPropertiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPipeRelationshipWeightsRequest(_message.Message):
    __slots__ = ("relationship_name", "overall_weight", "axis_offset", "axis_alignment", "center_pull", "out_of_material_weight", "out_of_material_offset", "constrain_region_at_od", "constrain_id_od_overlap")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERALL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    AXIS_OFFSET_FIELD_NUMBER: _ClassVar[int]
    AXIS_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CENTER_PULL_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_MATERIAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_MATERIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_REGION_AT_OD_FIELD_NUMBER: _ClassVar[int]
    CONSTRAIN_ID_OD_OVERLAP_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    overall_weight: float
    axis_offset: float
    axis_alignment: float
    center_pull: float
    out_of_material_weight: float
    out_of_material_offset: float
    constrain_region_at_od: bool
    constrain_id_od_overlap: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., overall_weight: _Optional[float] = ..., axis_offset: _Optional[float] = ..., axis_alignment: _Optional[float] = ..., center_pull: _Optional[float] = ..., out_of_material_weight: _Optional[float] = ..., out_of_material_offset: _Optional[float] = ..., constrain_region_at_od: bool = ..., constrain_id_od_overlap: bool = ...) -> None: ...

class SetPipeRelationshipWeightsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipAutoVectorsFitAvfRequest(_message.Message):
    __slots__ = ("relationship_name", "create_auto_vectors_avf")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_AUTO_VECTORS_AVF_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    create_auto_vectors_avf: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., create_auto_vectors_avf: bool = ...) -> None: ...

class SetRelationshipAutoVectorsFitAvfResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipDesiredMeasCountRequest(_message.Message):
    __slots__ = ("relationship_name", "desired_measurement_count")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    DESIRED_MEASUREMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    desired_measurement_count: int
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., desired_measurement_count: _Optional[int] = ...) -> None: ...

class SetRelationshipDesiredMeasCountResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipDormantStatusRequest(_message.Message):
    __slots__ = ("relationships", "dormant_status")
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    DORMANT_STATUS_FIELD_NUMBER: _ClassVar[int]
    relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    dormant_status: bool
    def __init__(self, relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., dormant_status: bool = ...) -> None: ...

class SetRelationshipDormantStatusResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipFitConstraintsScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name", "fit_constraint_options")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_CONSTRAINT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_constraint_options: _spatial_analyzer_values_pb2.FitConstraintScalarOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_constraint_options: _Optional[_Union[_spatial_analyzer_values_pb2.FitConstraintScalarOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipFitConstraintsScalarTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipOrientationFitConstraintsVectorTypeRequest(_message.Message):
    __slots__ = ("relationship_name", "orientation_vector_constraint")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_VECTOR_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    orientation_vector_constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., orientation_vector_constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipOrientationFitConstraintsVectorTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipOutlierRejectionScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetRelationshipOutlierRejectionScalarTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipPositionFitConstraintsVectorTypeRequest(_message.Message):
    __slots__ = ("relationship_name", "position_vector_constraint")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_VECTOR_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    position_vector_constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., position_vector_constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipPositionFitConstraintsVectorTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipProjectionOptionsRequest(_message.Message):
    __slots__ = ("relationship_name", "projection_options")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipProjectionOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipReportingFrameRequest(_message.Message):
    __slots__ = ("relationship_name", "reporting_frame")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetRelationshipReportingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipSubSamplingOptionsRequest(_message.Message):
    __slots__ = ("relationship_name", "use_every_ith_point", "i_value", "use_no_more_than_n_points", "n_value")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_EVERY_ITH_POINT_FIELD_NUMBER: _ClassVar[int]
    I_VALUE_FIELD_NUMBER: _ClassVar[int]
    USE_NO_MORE_THAN_N_POINTS_FIELD_NUMBER: _ClassVar[int]
    N_VALUE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    use_every_ith_point: bool
    i_value: int
    use_no_more_than_n_points: bool
    n_value: int
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_every_ith_point: bool = ..., i_value: _Optional[int] = ..., use_no_more_than_n_points: bool = ..., n_value: _Optional[int] = ...) -> None: ...

class SetRelationshipSubSamplingOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipToleranceScalarTypeRequest(_message.Message):
    __slots__ = ("relationship_name", "tolerance_options")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    tolerance_options: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., tolerance_options: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipToleranceScalarTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipToleranceVectorTypeRequest(_message.Message):
    __slots__ = ("relationship_name", "vector_tolerance")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipToleranceVectorTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipVoxelCloudDisplayRequest(_message.Message):
    __slots__ = ("relationship_name", "enable_voxel_cloud_display", "voxel_size_1_0_autodetect", "min_pts_count_per_voxel", "voxel_rendering_diameter_1_0_fast", "surface_analysis_mode", "colorization_options", "show_color_bar_in_view")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_VOXEL_CLOUD_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    VOXEL_SIZE_1_0_AUTODETECT_FIELD_NUMBER: _ClassVar[int]
    MIN_PTS_COUNT_PER_VOXEL_FIELD_NUMBER: _ClassVar[int]
    VOXEL_RENDERING_DIAMETER_1_0_FAST_FIELD_NUMBER: _ClassVar[int]
    SURFACE_ANALYSIS_MODE_FIELD_NUMBER: _ClassVar[int]
    COLORIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLOR_BAR_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    enable_voxel_cloud_display: bool
    voxel_size_1_0_autodetect: float
    min_pts_count_per_voxel: int
    voxel_rendering_diameter_1_0_fast: float
    surface_analysis_mode: _spatial_analyzer_values_pb2.SurfaceAnalysisMode
    colorization_options: _spatial_analyzer_values_pb2.ColorizationOptions
    show_color_bar_in_view: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., enable_voxel_cloud_display: bool = ..., voxel_size_1_0_autodetect: _Optional[float] = ..., min_pts_count_per_voxel: _Optional[int] = ..., voxel_rendering_diameter_1_0_fast: _Optional[float] = ..., surface_analysis_mode: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceAnalysisMode, str]] = ..., colorization_options: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ..., show_color_bar_in_view: bool = ...) -> None: ...

class SetRelationshipVoxelCloudDisplayResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipWeightingRequest(_message.Message):
    __slots__ = ("relationship_name", "weight")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    weight: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., weight: _Optional[float] = ...) -> None: ...

class SetRelationshipWeightingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipWeightsNormalizedRequest(_message.Message):
    __slots__ = ("collection_name", "pick_weighting_mode")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    PICK_WEIGHTING_MODE_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    pick_weighting_mode: _spatial_analyzer_values_pb2.RelWeightingMode
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., pick_weighting_mode: _Optional[_Union[_spatial_analyzer_values_pb2.RelWeightingMode, str]] = ...) -> None: ...

class SetRelationshipWeightsNormalizedResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoFilterCloudsToNominalGeometry2DRequest(_message.Message):
    __slots__ = ("auto_filter_target_relationships", "clouds", "cloud_thinning_settings", "filter_proximity_settings_2d", "geometry_extraction_tolerance")
    AUTO_FILTER_TARGET_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    CLOUDS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROXIMITY_SETTINGS_2D_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_EXTRACTION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    auto_filter_target_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    filter_proximity_settings_2d: FilterProximitySettings
    geometry_extraction_tolerance: float
    def __init__(self, auto_filter_target_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., filter_proximity_settings_2d: _Optional[_Union[FilterProximitySettings, _Mapping]] = ..., geometry_extraction_tolerance: _Optional[float] = ...) -> None: ...

class AutoFilterCloudsToNominalGeometry2DResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoFilterCloudsToNominalGeometry3DRequest(_message.Message):
    __slots__ = ("auto_filter_target_relationships", "clouds", "cloud_thinning_settings", "filter_proximity_settings_3d")
    AUTO_FILTER_TARGET_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    CLOUDS_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROXIMITY_SETTINGS_3D_FIELD_NUMBER: _ClassVar[int]
    auto_filter_target_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    filter_proximity_settings_3d: FilterProximitySettings
    def __init__(self, auto_filter_target_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., filter_proximity_settings_3d: _Optional[_Union[FilterProximitySettings, _Mapping]] = ...) -> None: ...

class AutoFilterCloudsToNominalGeometry3DResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoFilterPointsGroupsCloudsToSurfaceFacesRequest(_message.Message):
    __slots__ = ("points", "groups", "clouds", "surface_offset", "edge_offset", "offset_direction", "enforce_max_points_per_face_in_output", "max_points_per_face", "surfaces", "cloud_thinning_settings", "output_cloud_base_name", "use_face_ids_for_suffix")
    POINTS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    CLOUDS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EDGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MAX_POINTS_PER_FACE_IN_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_PER_FACE_FIELD_NUMBER: _ClassVar[int]
    SURFACES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_THINNING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CLOUD_BASE_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_FACE_IDS_FOR_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    points: PointNameList
    groups: CollectionObjectNameList
    clouds: CollectionObjectNameList
    surface_offset: float
    edge_offset: float
    offset_direction: _spatial_analyzer_values_pb2.OffsetDirectionType
    enforce_max_points_per_face_in_output: bool
    max_points_per_face: int
    surfaces: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_thinning_settings: _spatial_analyzer_values_pb2.CloudThinningOptions
    output_cloud_base_name: str
    use_face_ids_for_suffix: bool
    def __init__(self, points: _Optional[_Union[PointNameList, _Mapping]] = ..., groups: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., clouds: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., surface_offset: _Optional[float] = ..., edge_offset: _Optional[float] = ..., offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., enforce_max_points_per_face_in_output: bool = ..., max_points_per_face: _Optional[int] = ..., surfaces: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_thinning_settings: _Optional[_Union[_spatial_analyzer_values_pb2.CloudThinningOptions, _Mapping]] = ..., output_cloud_base_name: _Optional[str] = ..., use_face_ids_for_suffix: bool = ...) -> None: ...

class AutoFilterPointsGroupsCloudsToSurfaceFacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoFilterPointsToNominalGeometry3DRequest(_message.Message):
    __slots__ = ("auto_filter_target_relationships", "points", "filter_proximity_settings_3d")
    AUTO_FILTER_TARGET_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    FILTER_PROXIMITY_SETTINGS_3D_FIELD_NUMBER: _ClassVar[int]
    auto_filter_target_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    filter_proximity_settings_3d: FilterProximitySettings
    def __init__(self, auto_filter_target_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., filter_proximity_settings_3d: _Optional[_Union[FilterProximitySettings, _Mapping]] = ...) -> None: ...

class AutoFilterPointsToNominalGeometry3DResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CollectionObjectNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, values: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ComputeGeometryRelationshipUncertaintiesRequest(_message.Message):
    __slots__ = ("relationship_name", "display_results")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    display_results: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., display_results: bool = ...) -> None: ...

class ComputeGeometryRelationshipUncertaintiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreatePointsToObjectsMapRequest(_message.Message):
    __slots__ = ("points", "groups", "objects", "proximity_tolerance", "points_to_objects_map_name")
    POINTS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    POINTS_TO_OBJECTS_MAP_NAME_FIELD_NUMBER: _ClassVar[int]
    points: PointNameList
    groups: CollectionObjectNameList
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    proximity_tolerance: float
    points_to_objects_map_name: str
    def __init__(self, points: _Optional[_Union[PointNameList, _Mapping]] = ..., groups: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., proximity_tolerance: _Optional[float] = ..., points_to_objects_map_name: _Optional[str] = ...) -> None: ...

class CreatePointsToObjectsMapResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class DeleteRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DoRelationshipFitRequest(_message.Message):
    __slots__ = ("collection_containing_relationships", "objects_to_move", "instruments_to_move", "solver_mode", "motion_to_allow", "use_fit_dialog")
    COLLECTION_CONTAINING_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    SOLVER_MODE_FIELD_NUMBER: _ClassVar[int]
    MOTION_TO_ALLOW_FIELD_NUMBER: _ClassVar[int]
    USE_FIT_DIALOG_FIELD_NUMBER: _ClassVar[int]
    collection_containing_relationships: str
    objects_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    instruments_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    solver_mode: SolverMode
    motion_to_allow: FitDofOptions
    use_fit_dialog: bool
    def __init__(self, collection_containing_relationships: _Optional[str] = ..., objects_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., instruments_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., solver_mode: _Optional[_Union[SolverMode, str]] = ..., motion_to_allow: _Optional[_Union[FitDofOptions, _Mapping]] = ..., use_fit_dialog: bool = ...) -> None: ...

class DoRelationshipFitResult(_message.Message):
    __slots__ = ("transform_in_reference", "transform_in_working", "transform_in_world", "fit_objective_value", "execution")
    TRANSFORM_IN_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_IN_WORLD_FIELD_NUMBER: _ClassVar[int]
    FIT_OBJECTIVE_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform_in_reference: _spatial_analyzer_values_pb2.Transform
    transform_in_working: _spatial_analyzer_values_pb2.WorldTransform
    transform_in_world: _spatial_analyzer_values_pb2.WorldTransform
    fit_objective_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform_in_reference: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., transform_in_world: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., fit_objective_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EditGeometryRelationshipPointListRequest(_message.Message):
    __slots__ = ("relationship_name", "point_edit_mode")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_EDIT_MODE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    point_edit_mode: GeometryRelationshipPointEditMode
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_edit_mode: _Optional[_Union[GeometryRelationshipPointEditMode, str]] = ...) -> None: ...

class EditGeometryRelationshipPointListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterGeometryRelationshipOutlierCloudPointsRequest(_message.Message):
    __slots__ = ("relationship_name", "sigma_threshold", "modify_existing_input_clouds")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGMA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    MODIFY_EXISTING_INPUT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    sigma_threshold: float
    modify_existing_input_clouds: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., sigma_threshold: _Optional[float] = ..., modify_existing_input_clouds: bool = ...) -> None: ...

class FilterGeometryRelationshipOutlierCloudPointsResult(_message.Message):
    __slots__ = ("metrics", "execution")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    metrics: GeometryRelationshipOutlierFilterMetrics
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, metrics: _Optional[_Union[GeometryRelationshipOutlierFilterMetrics, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FilterProximitySettings(_message.Message):
    __slots__ = ("surface_inclusion_proximity", "edge_exclusion_proximity", "planar_inclusion_proximity", "planar_exclusion_proximity", "radial_inclusion_proximity", "geometry_extraction_tolerance", "surface_proximity_mode", "planar_proximity_mode", "radial_proximity_mode", "project_to_plane", "assert_plane_boundaries")
    SURFACE_INCLUSION_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    EDGE_EXCLUSION_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    PLANAR_INCLUSION_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    PLANAR_EXCLUSION_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    RADIAL_INCLUSION_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_EXTRACTION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    SURFACE_PROXIMITY_MODE_FIELD_NUMBER: _ClassVar[int]
    PLANAR_PROXIMITY_MODE_FIELD_NUMBER: _ClassVar[int]
    RADIAL_PROXIMITY_MODE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_TO_PLANE_FIELD_NUMBER: _ClassVar[int]
    ASSERT_PLANE_BOUNDARIES_FIELD_NUMBER: _ClassVar[int]
    surface_inclusion_proximity: float
    edge_exclusion_proximity: float
    planar_inclusion_proximity: float
    planar_exclusion_proximity: float
    radial_inclusion_proximity: float
    geometry_extraction_tolerance: float
    surface_proximity_mode: _spatial_analyzer_values_pb2.OffsetDirectionType
    planar_proximity_mode: _spatial_analyzer_values_pb2.OffsetDirectionType
    radial_proximity_mode: _spatial_analyzer_values_pb2.OffsetDirectionType
    project_to_plane: bool
    assert_plane_boundaries: bool
    def __init__(self, surface_inclusion_proximity: _Optional[float] = ..., edge_exclusion_proximity: _Optional[float] = ..., planar_inclusion_proximity: _Optional[float] = ..., planar_exclusion_proximity: _Optional[float] = ..., radial_inclusion_proximity: _Optional[float] = ..., geometry_extraction_tolerance: _Optional[float] = ..., surface_proximity_mode: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., planar_proximity_mode: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., radial_proximity_mode: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., project_to_plane: bool = ..., assert_plane_boundaries: bool = ...) -> None: ...

class FitDofOptions(_message.Message):
    __slots__ = ("allow_x", "allow_y", "allow_z", "allow_rx", "allow_ry", "allow_rz", "rotate_about_centroid")
    ALLOW_X_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Y_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Z_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RZ_FIELD_NUMBER: _ClassVar[int]
    ROTATE_ABOUT_CENTROID_FIELD_NUMBER: _ClassVar[int]
    allow_x: bool
    allow_y: bool
    allow_z: bool
    allow_rx: bool
    allow_ry: bool
    allow_rz: bool
    rotate_about_centroid: bool
    def __init__(self, allow_x: bool = ..., allow_y: bool = ..., allow_z: bool = ..., allow_rx: bool = ..., allow_ry: bool = ..., allow_rz: bool = ..., rotate_about_centroid: bool = ...) -> None: ...

class GenerateGeometryRelationshipSummaryRequest(_message.Message):
    __slots__ = ("relationship_ref_list", "summary_table_name")
    RELATIONSHIP_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    summary_table_name: str
    def __init__(self, relationship_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., summary_table_name: _Optional[str] = ...) -> None: ...

class GenerateGeometryRelationshipSummaryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GeometryRelationshipOutlierFilterMetrics(_message.Message):
    __slots__ = ("first_pass_rms_error", "first_pass_maximum_error", "first_pass_minimum_error", "first_pass_average_error", "final_pass_rms_error", "final_pass_maximum_error", "final_pass_minimum_error", "final_pass_average_error", "total_input_point_count", "exclude_point_count")
    FIRST_PASS_RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    FIRST_PASS_MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    FIRST_PASS_MINIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    FIRST_PASS_AVERAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    FINAL_PASS_RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    FINAL_PASS_MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    FINAL_PASS_MINIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    FINAL_PASS_AVERAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INPUT_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    first_pass_rms_error: float
    first_pass_maximum_error: float
    first_pass_minimum_error: float
    first_pass_average_error: float
    final_pass_rms_error: float
    final_pass_maximum_error: float
    final_pass_minimum_error: float
    final_pass_average_error: float
    total_input_point_count: int
    exclude_point_count: int
    def __init__(self, first_pass_rms_error: _Optional[float] = ..., first_pass_maximum_error: _Optional[float] = ..., first_pass_minimum_error: _Optional[float] = ..., first_pass_average_error: _Optional[float] = ..., final_pass_rms_error: _Optional[float] = ..., final_pass_maximum_error: _Optional[float] = ..., final_pass_minimum_error: _Optional[float] = ..., final_pass_average_error: _Optional[float] = ..., total_input_point_count: _Optional[int] = ..., exclude_point_count: _Optional[int] = ...) -> None: ...

class GetGeneralRelationshipStatisticsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetGeneralRelationshipStatisticsResult(_message.Message):
    __slots__ = ("max_deviation", "rms", "has_signed_deviation", "signed_max_deviation", "signed_min_deviation", "execution")
    MAX_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    RMS_FIELD_NUMBER: _ClassVar[int]
    HAS_SIGNED_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SIGNED_MAX_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SIGNED_MIN_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    max_deviation: float
    rms: float
    has_signed_deviation: bool
    signed_max_deviation: float
    signed_min_deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, max_deviation: _Optional[float] = ..., rms: _Optional[float] = ..., has_signed_deviation: bool = ..., signed_max_deviation: _Optional[float] = ..., signed_min_deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGeomRelationshipCriteriaNameListRequest(_message.Message):
    __slots__ = ("relationship_name", "include_all_criteria")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ALL_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    include_all_criteria: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., include_all_criteria: bool = ...) -> None: ...

class GetGeomRelationshipCriteriaNameListResult(_message.Message):
    __slots__ = ("criteria_name_list", "execution")
    CRITERIA_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    criteria_name_list: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, criteria_name_list: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetObjectsFromPointsToObjectsMapPointListRequest(_message.Message):
    __slots__ = ("points_to_objects_map_name", "points")
    POINTS_TO_OBJECTS_MAP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points_to_objects_map_name: str
    points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, points_to_objects_map_name: _Optional[str] = ..., points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class GetObjectsFromPointsToObjectsMapPointListResult(_message.Message):
    __slots__ = ("objects", "execution")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointsToObjectsRelationshipStatisticsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetPointsToObjectsRelationshipStatisticsResult(_message.Message):
    __slots__ = ("absolute_max_deviation", "max_deviation", "min_deviation", "rms", "candidate_point_count", "sampled_point_count", "rejected_point_count", "used_point_count", "out_of_tolerance_point_count", "execution")
    ABSOLUTE_MAX_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAX_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MIN_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    RMS_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SAMPLED_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    REJECTED_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    USED_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    OUT_OF_TOLERANCE_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    absolute_max_deviation: float
    max_deviation: float
    min_deviation: float
    rms: float
    candidate_point_count: int
    sampled_point_count: int
    rejected_point_count: int
    used_point_count: int
    out_of_tolerance_point_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, absolute_max_deviation: _Optional[float] = ..., max_deviation: _Optional[float] = ..., min_deviation: _Optional[float] = ..., rms: _Optional[float] = ..., candidate_point_count: _Optional[int] = ..., sampled_point_count: _Optional[int] = ..., rejected_point_count: _Optional[int] = ..., used_point_count: _Optional[int] = ..., out_of_tolerance_point_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointsToPointsRelationshipAssociatedDataRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetPointsToPointsRelationshipAssociatedDataResult(_message.Message):
    __slots__ = ("associated_data", "execution")
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    associated_data: PointsToPointsRelationshipAssociatedData
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, associated_data: _Optional[_Union[PointsToPointsRelationshipAssociatedData, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointToPointRelationshipStatisticsRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetPointToPointRelationshipStatisticsResult(_message.Message):
    __slots__ = ("delta_x", "delta_y", "delta_z", "delta_magnitude", "reference_frame", "execution")
    DELTA_X_FIELD_NUMBER: _ClassVar[int]
    DELTA_Y_FIELD_NUMBER: _ClassVar[int]
    DELTA_Z_FIELD_NUMBER: _ClassVar[int]
    DELTA_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    delta_x: float
    delta_y: float
    delta_z: float
    delta_magnitude: float
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, delta_x: _Optional[float] = ..., delta_y: _Optional[float] = ..., delta_z: _Optional[float] = ..., delta_magnitude: _Optional[float] = ..., reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipAssociatedDataRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetRelationshipAssociatedDataResult(_message.Message):
    __slots__ = ("associated_data", "execution")
    ASSOCIATED_DATA_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    associated_data: RelationshipAssociatedData
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, associated_data: _Optional[_Union[RelationshipAssociatedData, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipStatusRequest(_message.Message):
    __slots__ = ("relationship_name",)
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetRelationshipStatusResult(_message.Message):
    __slots__ = ("status", "execution")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    status: RelationshipStatusFlags
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, status: _Optional[_Union[RelationshipStatusFlags, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeAveragePointRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "points_in_relationship", "average_point_name", "nominal_point_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    points_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    average_point_name: _spatial_analyzer_values_pb2.PointName
    nominal_point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., points_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., average_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., nominal_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class MakeAveragePointRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDynamicCircleRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "construction_mode", "first_reference_geometry", "second_reference_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    SECOND_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    construction_mode: DynamicCircleMode
    first_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    second_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., construction_mode: _Optional[_Union[DynamicCircleMode, str]] = ..., first_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeDynamicCircleRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDynamicEllipseRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "construction_mode", "first_reference_geometry", "second_reference_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    SECOND_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    construction_mode: DynamicEllipseMode
    first_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    second_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., construction_mode: _Optional[_Union[DynamicEllipseMode, str]] = ..., first_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeDynamicEllipseRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDynamicLineRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "construction_mode", "first_reference_geometry", "second_reference_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    SECOND_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    construction_mode: DynamicLineMode
    first_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    second_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., construction_mode: _Optional[_Union[DynamicLineMode, str]] = ..., first_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeDynamicLineRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDynamicPlaneRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "construction_mode", "first_reference_geometry", "second_reference_geometry", "offset_plane_offset")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    SECOND_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    OFFSET_PLANE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    construction_mode: DynamicPlaneMode
    first_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    second_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    offset_plane_offset: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., construction_mode: _Optional[_Union[DynamicPlaneMode, str]] = ..., first_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., offset_plane_offset: _Optional[float] = ...) -> None: ...

class MakeDynamicPlaneRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDynamicPointRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "construction_mode", "first_reference_geometry", "second_reference_geometry", "third_reference_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSTRUCTION_MODE_FIELD_NUMBER: _ClassVar[int]
    FIRST_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    SECOND_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    THIRD_REFERENCE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    construction_mode: DynamicPointMode
    first_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    second_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    third_reference_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., construction_mode: _Optional[_Union[DynamicPointMode, str]] = ..., first_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., third_reference_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeDynamicPointRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeFrameToFrameRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "first_frame_name", "second_frame_name", "orientation_tolerance", "position_tolerance")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    POSITION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    first_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    second_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    orientation_tolerance: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    position_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., first_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., orientation_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ..., position_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class MakeFrameToFrameRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGeometryCompareOnlyRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "nominal_geometry", "measured_geometry")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    MEASURED_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    nominal_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    measured_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., nominal_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measured_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeGeometryCompareOnlyRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGeometryFitAndCompareToNominalRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "nominal_geometry", "point_groups_to_fit", "resulting_object_name", "fit_profile_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUPS_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    nominal_geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    point_groups_to_fit: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_profile_name: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., nominal_geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_groups_to_fit: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_profile_name: _Optional[str] = ...) -> None: ...

class MakeGeometryFitAndCompareToNominalRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGeometryFitOnlyRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "point_groups_to_fit", "geometry_type", "resulting_object_name", "fit_profile_name")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUPS_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESULTING_OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    FIT_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    point_groups_to_fit: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    geometry_type: _spatial_analyzer_values_pb2.GeometryType
    resulting_object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    fit_profile_name: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_groups_to_fit: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., geometry_type: _Optional[_Union[_spatial_analyzer_values_pb2.GeometryType, str]] = ..., resulting_object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., fit_profile_name: _Optional[str] = ...) -> None: ...

class MakeGeometryFitOnlyRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGroupsToObjectsRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "point_groups_in_relationship", "objects_in_relationship", "projection_options", "auto_update_a_vector_group")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUPS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    point_groups_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    objects_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    auto_update_a_vector_group: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_groups_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., objects_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., auto_update_a_vector_group: bool = ...) -> None: ...

class MakeGroupsToObjectsRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGroupToGroupRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "first_group_name", "second_group_name", "auto_update_a_vector_group", "tolerance", "constraint")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    first_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    second_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    auto_update_a_vector_group: bool
    tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., first_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., auto_update_a_vector_group: bool = ..., tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class MakeGroupToGroupRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGroupToNominalGroupRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "nominal_group_name", "measured_group_name", "auto_update_a_vector_group", "use_closest_point", "display_closest_point_watch_window", "use_view_zooming_with_proximity", "ignore_points_beyond_threshold", "proximity_threshold", "tolerance", "constraint", "fit_weight")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASURED_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    USE_CLOSEST_POINT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_CLOSEST_POINT_WATCH_WINDOW_FIELD_NUMBER: _ClassVar[int]
    USE_VIEW_ZOOMING_WITH_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    IGNORE_POINTS_BEYOND_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    FIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    nominal_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    measured_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    auto_update_a_vector_group: bool
    use_closest_point: bool
    display_closest_point_watch_window: bool
    use_view_zooming_with_proximity: bool
    ignore_points_beyond_threshold: bool
    proximity_threshold: float
    tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    fit_weight: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., nominal_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measured_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., auto_update_a_vector_group: bool = ..., use_closest_point: bool = ..., display_closest_point_watch_window: bool = ..., use_view_zooming_with_proximity: bool = ..., ignore_points_beyond_threshold: bool = ..., proximity_threshold: _Optional[float] = ..., tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., fit_weight: _Optional[float] = ...) -> None: ...

class MakeGroupToNominalGroupRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeObjectToObjectDirectionRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "first_object_in_relationship", "second_object_in_relationship", "nominal_angle")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_OBJECT_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    SECOND_OBJECT_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_ANGLE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    first_object_in_relationship: _spatial_analyzer_values_pb2.CollectionObjectName
    second_object_in_relationship: _spatial_analyzer_values_pb2.CollectionObjectName
    nominal_angle: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., first_object_in_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., second_object_in_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., nominal_angle: _Optional[float] = ...) -> None: ...

class MakeObjectToObjectDirectionRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointCloudsToObjectsRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "point_clouds_in_relationship", "objects_in_relationship", "projection_options", "auto_update_a_vector_group")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUDS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    point_clouds_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    objects_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    auto_update_a_vector_group: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_clouds_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., objects_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., auto_update_a_vector_group: bool = ...) -> None: ...

class MakePointCloudsToObjectsRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointsToObjectsRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "points_in_relationship", "objects_in_relationship", "projection_options", "auto_update_a_vector_group")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    POINTS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_IN_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    points_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    objects_in_relationship: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    auto_update_a_vector_group: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., points_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., objects_in_relationship: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., auto_update_a_vector_group: bool = ...) -> None: ...

class MakePointsToObjectsRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointsToPointsRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "nominal_points", "measured_points", "auto_update_a_vector_group", "tolerance", "constraint")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    MEASURED_POINTS_FIELD_NUMBER: _ClassVar[int]
    AUTO_UPDATE_A_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    nominal_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    measured_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    auto_update_a_vector_group: bool
    tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., nominal_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., measured_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., auto_update_a_vector_group: bool = ..., tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class MakePointsToPointsRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakePointToPointRelationshipRequest(_message.Message):
    __slots__ = ("relationship_name", "first_point_name", "second_point_name", "tolerance", "constraint")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    SECOND_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    first_point_name: _spatial_analyzer_values_pb2.PointName
    second_point_name: _spatial_analyzer_values_pb2.PointName
    tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    constraint: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., first_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., constraint: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class MakePointToPointRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeVectorGroupToVectorGroupRelationshipRequest(_message.Message):
    __slots__ = ("new_vg_to_vg_relationship", "reference_vector_group", "corresponding_vector_group", "set_opposing_vector_group_polarity")
    NEW_VG_TO_VG_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    SET_OPPOSING_VECTOR_GROUP_POLARITY_FIELD_NUMBER: _ClassVar[int]
    new_vg_to_vg_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    reference_vector_group: _spatial_analyzer_values_pb2.CollectionObjectName
    corresponding_vector_group: _spatial_analyzer_values_pb2.CollectionObjectName
    set_opposing_vector_group_polarity: bool
    def __init__(self, new_vg_to_vg_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., reference_vector_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., corresponding_vector_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., set_opposing_vector_group_polarity: bool = ...) -> None: ...

class MakeVectorGroupToVectorGroupRelationshipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveCollectionsByMinimizingRelationshipsRequest(_message.Message):
    __slots__ = ("collections_to_move", "relationships_to_minimize", "solver_mode", "motion_to_allow", "use_fit_dialog", "convergence_threshold")
    COLLECTIONS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_TO_MINIMIZE_FIELD_NUMBER: _ClassVar[int]
    SOLVER_MODE_FIELD_NUMBER: _ClassVar[int]
    MOTION_TO_ALLOW_FIELD_NUMBER: _ClassVar[int]
    USE_FIT_DIALOG_FIELD_NUMBER: _ClassVar[int]
    CONVERGENCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    collections_to_move: _containers.RepeatedScalarFieldContainer[str]
    relationships_to_minimize: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    solver_mode: SolverMode
    motion_to_allow: FitDofOptions
    use_fit_dialog: bool
    convergence_threshold: float
    def __init__(self, collections_to_move: _Optional[_Iterable[str]] = ..., relationships_to_minimize: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., solver_mode: _Optional[_Union[SolverMode, str]] = ..., motion_to_allow: _Optional[_Union[FitDofOptions, _Mapping]] = ..., use_fit_dialog: bool = ..., convergence_threshold: _Optional[float] = ...) -> None: ...

class MoveCollectionsByMinimizingRelationshipsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PointNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, values: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class PointsToPointsRelationshipAssociatedData(_message.Message):
    __slots__ = ("nominal_points", "actual_points")
    NOMINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    nominal_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    actual_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, nominal_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., actual_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class RelationshipAssociatedData(_message.Message):
    __slots__ = ("relationship_type", "individual_points", "point_groups", "point_clouds", "objects")
    RELATIONSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    relationship_type: str
    individual_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    point_groups: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    point_clouds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, relationship_type: _Optional[str] = ..., individual_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., point_groups: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., point_clouds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class RelationshipStatusFlags(_message.Message):
    __slots__ = ("dormant", "success", "measured", "failed", "unmeasured")
    DORMANT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MEASURED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    UNMEASURED_FIELD_NUMBER: _ClassVar[int]
    dormant: bool
    success: bool
    measured: bool
    failed: bool
    unmeasured: bool
    def __init__(self, dormant: bool = ..., success: bool = ..., measured: bool = ..., failed: bool = ..., unmeasured: bool = ...) -> None: ...

class RelationshipWatchWindowTemplateRequest(_message.Message):
    __slots__ = ("watch_window_template_name", "linear_precision", "angular_precision", "font", "text_color", "background_color", "highlight_color", "show_deviation_x_rx", "show_deviation_y_ry", "show_deviation_z_rz", "show_deviation_magnitude", "udp_network_transmit_settings", "transparent_background", "hide_units")
    WATCH_WINDOW_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    LINEAR_PRECISION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_PRECISION_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_COLOR_FIELD_NUMBER: _ClassVar[int]
    SHOW_DEVIATION_X_RX_FIELD_NUMBER: _ClassVar[int]
    SHOW_DEVIATION_Y_RY_FIELD_NUMBER: _ClassVar[int]
    SHOW_DEVIATION_Z_RZ_FIELD_NUMBER: _ClassVar[int]
    SHOW_DEVIATION_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    UDP_NETWORK_TRANSMIT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TRANSPARENT_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    HIDE_UNITS_FIELD_NUMBER: _ClassVar[int]
    watch_window_template_name: _spatial_analyzer_values_pb2.CollectionObjectName
    linear_precision: int
    angular_precision: int
    font: _spatial_analyzer_values_pb2.Font
    text_color: _spatial_analyzer_values_pb2.Color
    background_color: _spatial_analyzer_values_pb2.Color
    highlight_color: _spatial_analyzer_values_pb2.Color
    show_deviation_x_rx: bool
    show_deviation_y_ry: bool
    show_deviation_z_rz: bool
    show_deviation_magnitude: bool
    udp_network_transmit_settings: RelationshipWatchWindowUdpSettings
    transparent_background: bool
    hide_units: bool
    def __init__(self, watch_window_template_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., linear_precision: _Optional[int] = ..., angular_precision: _Optional[int] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., text_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., background_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., highlight_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., show_deviation_x_rx: bool = ..., show_deviation_y_ry: bool = ..., show_deviation_z_rz: bool = ..., show_deviation_magnitude: bool = ..., udp_network_transmit_settings: _Optional[_Union[RelationshipWatchWindowUdpSettings, _Mapping]] = ..., transparent_background: bool = ..., hide_units: bool = ...) -> None: ...

class RelationshipWatchWindowTemplateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RelationshipWatchWindowUdpSettings(_message.Message):
    __slots__ = ("enabled", "broadcast", "ip_address", "port")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BROADCAST_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    broadcast: bool
    ip_address: str
    port: int
    def __init__(self, enabled: bool = ..., broadcast: bool = ..., ip_address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class SetGroupToNominalGroupViewZoomingRequest(_message.Message):
    __slots__ = ("relationship_name", "use_closest_point", "show_closest_point_watch_window", "use_view_zooming", "ignore_points_beyond_threshold", "proximity_threshold")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_CLOSEST_POINT_FIELD_NUMBER: _ClassVar[int]
    SHOW_CLOSEST_POINT_WATCH_WINDOW_FIELD_NUMBER: _ClassVar[int]
    USE_VIEW_ZOOMING_FIELD_NUMBER: _ClassVar[int]
    IGNORE_POINTS_BEYOND_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PROXIMITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    use_closest_point: bool
    show_closest_point_watch_window: bool
    use_view_zooming: bool
    ignore_points_beyond_threshold: bool
    proximity_threshold: float
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., use_closest_point: bool = ..., show_closest_point_watch_window: bool = ..., use_view_zooming: bool = ..., ignore_points_beyond_threshold: bool = ..., proximity_threshold: _Optional[float] = ...) -> None: ...

class SetGroupToNominalGroupViewZoomingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectToObjectDirectionRelationshipTolerancesRequest(_message.Message):
    __slots__ = ("relationship_name", "angle_between_vectors_tolerances", "mutual_perpendicular_length_tolerances")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    ANGLE_BETWEEN_VECTORS_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    MUTUAL_PERPENDICULAR_LENGTH_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    angle_between_vectors_tolerances: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    mutual_perpendicular_length_tolerances: _spatial_analyzer_values_pb2.ToleranceScalarOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., angle_between_vectors_tolerances: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ..., mutual_perpendicular_length_tolerances: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceScalarOptions, _Mapping]] = ...) -> None: ...

class SetObjectToObjectDirectionRelationshipTolerancesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOptimizationPerturbationParametersRequest(_message.Message):
    __slots__ = ("length_perturbation", "angular_perturbation", "damping")
    LENGTH_PERTURBATION_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_PERTURBATION_FIELD_NUMBER: _ClassVar[int]
    DAMPING_FIELD_NUMBER: _ClassVar[int]
    length_perturbation: float
    angular_perturbation: float
    damping: float
    def __init__(self, length_perturbation: _Optional[float] = ..., angular_perturbation: _Optional[float] = ..., damping: _Optional[float] = ...) -> None: ...

class SetOptimizationPerturbationParametersResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOptimizationSearchOptionsRequest(_message.Message):
    __slots__ = ("max_number_of_step_size_reduction",)
    MAX_NUMBER_OF_STEP_SIZE_REDUCTION_FIELD_NUMBER: _ClassVar[int]
    max_number_of_step_size_reduction: int
    def __init__(self, max_number_of_step_size_reduction: _Optional[int] = ...) -> None: ...

class SetOptimizationSearchOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointsToPointsRelationshipAssociatedDataRequest(_message.Message):
    __slots__ = ("relationship_name", "nominal_points", "actual_points", "ignore_empty_arguments")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_EMPTY_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    nominal_points: PointNameList
    actual_points: PointNameList
    ignore_empty_arguments: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., nominal_points: _Optional[_Union[PointNameList, _Mapping]] = ..., actual_points: _Optional[_Union[PointNameList, _Mapping]] = ..., ignore_empty_arguments: bool = ...) -> None: ...

class SetPointsToPointsRelationshipAssociatedDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipAssociatedDataRequest(_message.Message):
    __slots__ = ("relationship_name", "individual_points", "point_groups", "point_clouds", "objects", "ignore_empty_arguments")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    INDIVIDUAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUPS_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    IGNORE_EMPTY_ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    individual_points: PointNameList
    point_groups: CollectionObjectNameList
    point_clouds: CollectionObjectNameList
    objects: CollectionObjectNameList
    ignore_empty_arguments: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., individual_points: _Optional[_Union[PointNameList, _Mapping]] = ..., point_groups: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., point_clouds: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., objects: _Optional[_Union[CollectionObjectNameList, _Mapping]] = ..., ignore_empty_arguments: bool = ...) -> None: ...

class SetRelationshipAssociatedDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupToVectorGroupCylindricalZoneRequest(_message.Message):
    __slots__ = ("vg_to_vg_relationship", "radial_offset", "minimum_axial_offset", "maximum_axial_offset")
    VG_TO_VG_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    RADIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_AXIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_AXIAL_OFFSET_FIELD_NUMBER: _ClassVar[int]
    vg_to_vg_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    radial_offset: float
    minimum_axial_offset: float
    maximum_axial_offset: float
    def __init__(self, vg_to_vg_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., radial_offset: _Optional[float] = ..., minimum_axial_offset: _Optional[float] = ..., maximum_axial_offset: _Optional[float] = ...) -> None: ...

class SetVectorGroupToVectorGroupCylindricalZoneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupToVectorGroupFitGradientFactorRequest(_message.Message):
    __slots__ = ("vg_to_vg_relationship", "fit_gradient_factor")
    VG_TO_VG_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    FIT_GRADIENT_FACTOR_FIELD_NUMBER: _ClassVar[int]
    vg_to_vg_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    fit_gradient_factor: float
    def __init__(self, vg_to_vg_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., fit_gradient_factor: _Optional[float] = ...) -> None: ...

class SetVectorGroupToVectorGroupFitGradientFactorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupToVectorGroupFitWeightsRequest(_message.Message):
    __slots__ = ("vg_to_vg_relationship", "minimum_gap", "minimum_gap_fit_weight", "maximum_gap", "maximum_gap_fit_weight", "nominal_gap", "nominal_gap_fit_weight")
    VG_TO_VG_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_GAP_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_GAP_FIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_GAP_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_GAP_FIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GAP_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GAP_FIT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    vg_to_vg_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    minimum_gap: float
    minimum_gap_fit_weight: float
    maximum_gap: float
    maximum_gap_fit_weight: float
    nominal_gap: float
    nominal_gap_fit_weight: float
    def __init__(self, vg_to_vg_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., minimum_gap: _Optional[float] = ..., minimum_gap_fit_weight: _Optional[float] = ..., maximum_gap: _Optional[float] = ..., maximum_gap_fit_weight: _Optional[float] = ..., nominal_gap: _Optional[float] = ..., nominal_gap_fit_weight: _Optional[float] = ...) -> None: ...

class SetVectorGroupToVectorGroupFitWeightsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupToVectorGroupRelativePolarityRequest(_message.Message):
    __slots__ = ("vg_to_vg_relationship", "set_opposing_vector_group_polarity")
    VG_TO_VG_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    SET_OPPOSING_VECTOR_GROUP_POLARITY_FIELD_NUMBER: _ClassVar[int]
    vg_to_vg_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    set_opposing_vector_group_polarity: bool
    def __init__(self, vg_to_vg_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., set_opposing_vector_group_polarity: bool = ...) -> None: ...

class SetVectorGroupToVectorGroupRelativePolarityResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SigmoidalGapFitConstraints(_message.Message):
    __slots__ = ("use_sigmoidal_gap_constraints", "minimum_gap_boundary", "minimum_gap_weight", "maximum_gap_boundary", "maximum_gap_weight", "nominal_gap", "nominal_gap_weight", "gradient_steepness_factor")
    USE_SIGMOIDAL_GAP_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_GAP_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_GAP_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_GAP_BOUNDARY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_GAP_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GAP_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GAP_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_STEEPNESS_FACTOR_FIELD_NUMBER: _ClassVar[int]
    use_sigmoidal_gap_constraints: bool
    minimum_gap_boundary: float
    minimum_gap_weight: float
    maximum_gap_boundary: float
    maximum_gap_weight: float
    nominal_gap: float
    nominal_gap_weight: float
    gradient_steepness_factor: float
    def __init__(self, use_sigmoidal_gap_constraints: bool = ..., minimum_gap_boundary: _Optional[float] = ..., minimum_gap_weight: _Optional[float] = ..., maximum_gap_boundary: _Optional[float] = ..., maximum_gap_weight: _Optional[float] = ..., nominal_gap: _Optional[float] = ..., nominal_gap_weight: _Optional[float] = ..., gradient_steepness_factor: _Optional[float] = ...) -> None: ...

class StartStopRelationshipTrappingRequest(_message.Message):
    __slots__ = ("relationship_name", "instrument_id", "start_trapping")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TRAPPING_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionItemName
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    start_trapping: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., start_trapping: bool = ...) -> None: ...

class StartStopRelationshipTrappingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
