from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class SetGeomRelationshipAutoMeasureNominalFeatureRequest(_message.Message):
    __slots__ = ("relationship_name", "trap_clouds_false_geometry", "instrument_id", "measurement_mode")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAP_CLOUDS_FALSE_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    trap_clouds_false_geometry: bool
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    measurement_mode: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., trap_clouds_false_geometry: bool = ..., instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., measurement_mode: _Optional[str] = ...) -> None: ...

class SetGeomRelationshipAutoMeasureNominalFeatureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGeomRelationshipAutoVectorsNominalAvnRequest(_message.Message):
    __slots__ = ("relationship_name", "create_auto_vectors_avn", "points_type", "use_vector_group_custom_prefix", "vector_group_custom_prefix")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_AUTO_VECTORS_AVN_FIELD_NUMBER: _ClassVar[int]
    POINTS_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_VECTOR_GROUP_CUSTOM_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_CUSTOM_PREFIX_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    create_auto_vectors_avn: bool
    points_type: _spatial_analyzer_values_pb2.PointFilterInputType
    use_vector_group_custom_prefix: bool
    vector_group_custom_prefix: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., create_auto_vectors_avn: bool = ..., points_type: _Optional[_Union[_spatial_analyzer_values_pb2.PointFilterInputType, str]] = ..., use_vector_group_custom_prefix: bool = ..., vector_group_custom_prefix: _Optional[str] = ...) -> None: ...

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
    __slots__ = ("relationship_name", "create_auto_vectors_avf", "use_vector_group_custom_prefix", "vector_group_custom_prefix")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_AUTO_VECTORS_AVF_FIELD_NUMBER: _ClassVar[int]
    USE_VECTOR_GROUP_CUSTOM_PREFIX_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_CUSTOM_PREFIX_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    create_auto_vectors_avf: bool
    use_vector_group_custom_prefix: bool
    vector_group_custom_prefix: str
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., create_auto_vectors_avf: bool = ..., use_vector_group_custom_prefix: bool = ..., vector_group_custom_prefix: _Optional[str] = ...) -> None: ...

class SetRelationshipAutoVectorsFitAvfResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipAutoVectorsGroupDefaultPrefixRequest(_message.Message):
    __slots__ = ("geom_rel_avn_vg_default_prefix", "geom_rel_avf_vg_default_prefix", "non_geom_rel_vg_default_prefix")
    GEOM_REL_AVN_VG_DEFAULT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    GEOM_REL_AVF_VG_DEFAULT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    NON_GEOM_REL_VG_DEFAULT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    geom_rel_avn_vg_default_prefix: str
    geom_rel_avf_vg_default_prefix: str
    non_geom_rel_vg_default_prefix: str
    def __init__(self, geom_rel_avn_vg_default_prefix: _Optional[str] = ..., geom_rel_avf_vg_default_prefix: _Optional[str] = ..., non_geom_rel_vg_default_prefix: _Optional[str] = ...) -> None: ...

class SetRelationshipAutoVectorsGroupDefaultPrefixResult(_message.Message):
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

class SetRelationshipSigmoidalGapFitConstraintsRequest(_message.Message):
    __slots__ = ("relationship_name", "use_sigmoidal_gap_constraints")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    USE_SIGMOIDAL_GAP_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    use_sigmoidal_gap_constraints: bool
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_sigmoidal_gap_constraints: bool = ...) -> None: ...

class SetRelationshipSigmoidalGapFitConstraintsResult(_message.Message):
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
