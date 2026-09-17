from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GdtDistanceBetweenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GDT_DISTANCE_BETWEEN_MODE_UNSPECIFIED: _ClassVar[GdtDistanceBetweenMode]
    GDT_DISTANCE_BETWEEN_MODE_CENTROID: _ClassVar[GdtDistanceBetweenMode]
    GDT_DISTANCE_BETWEEN_MODE_MIN_MAX: _ClassVar[GdtDistanceBetweenMode]

class GdtEvaluationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GDT_EVALUATION_METHOD_UNSPECIFIED: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_NONE: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ASME_1994: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ASME_2009: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ASME_2018: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ISO_1983: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ISO_2004: _ClassVar[GdtEvaluationMethod]
    GDT_EVALUATION_METHOD_ISO_2017: _ClassVar[GdtEvaluationMethod]

class GdtExtendedEvaluationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GDT_EXTENDED_EVALUATION_METHOD_UNSPECIFIED: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_HIGH_POINT: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_MINIMUM_SEPARATION: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_3D: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_1_STD_DEV: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_2_STD_DEV: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_HALFWAY: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_MINIMUM_SEPARATION_HIGH_POINT: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_EQUALIZED_HIGH_POINT: _ClassVar[GdtExtendedEvaluationMethod]
    GDT_EXTENDED_EVALUATION_METHOD_EQUALIZED_LSQ_HIGH_POINT: _ClassVar[GdtExtendedEvaluationMethod]

class GdtFeatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GDT_FEATURE_TYPE_UNSPECIFIED: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_DIAMETER: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_RADIUS: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_DISTANCE_BETWEEN: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_WIDTH: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_LENGTH: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_ANGLE_BETWEEN: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_ANGULARITY: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_PERPENDICULARITY: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_PARALLELISM: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_CIRCULARITY: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_CONCENTRICITY: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_CYLINDRICITY: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_STRAIGHTNESS: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_SURFACE_PROFILE: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_LINE_PROFILE: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_COMPOSITE_SURFACE_PROFILE: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_FLATNESS: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_TRUE_POSITION: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_COMPOSITE_TRUE_POSITION: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_CIRCULAR_RUNOUT: _ClassVar[GdtFeatureType]
    GDT_FEATURE_TYPE_TOTAL_RUNOUT: _ClassVar[GdtFeatureType]

class GdtToleranceZoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GDT_TOLERANCE_ZONE_TYPE_UNSPECIFIED: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_NONE: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_CYLINDRICAL: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_PLANAR: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_SPHERICAL: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_RADIAL_ARC: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_RADIAL_PLANAR: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_BOUNDARY: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_PLANAR_MEDIAN: _ClassVar[GdtToleranceZoneType]
    GDT_TOLERANCE_ZONE_TYPE_SURFACE: _ClassVar[GdtToleranceZoneType]
GDT_DISTANCE_BETWEEN_MODE_UNSPECIFIED: GdtDistanceBetweenMode
GDT_DISTANCE_BETWEEN_MODE_CENTROID: GdtDistanceBetweenMode
GDT_DISTANCE_BETWEEN_MODE_MIN_MAX: GdtDistanceBetweenMode
GDT_EVALUATION_METHOD_UNSPECIFIED: GdtEvaluationMethod
GDT_EVALUATION_METHOD_NONE: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ASME_1994: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ASME_2009: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ASME_2018: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ISO_1983: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ISO_2004: GdtEvaluationMethod
GDT_EVALUATION_METHOD_ISO_2017: GdtEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_UNSPECIFIED: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_HIGH_POINT: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_MINIMUM_SEPARATION: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_3D: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_1_STD_DEV: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_2_STD_DEV: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_LEAST_SQUARES_HIGH_POINT_HALFWAY: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_MINIMUM_SEPARATION_HIGH_POINT: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_EQUALIZED_HIGH_POINT: GdtExtendedEvaluationMethod
GDT_EXTENDED_EVALUATION_METHOD_EQUALIZED_LSQ_HIGH_POINT: GdtExtendedEvaluationMethod
GDT_FEATURE_TYPE_UNSPECIFIED: GdtFeatureType
GDT_FEATURE_TYPE_DIAMETER: GdtFeatureType
GDT_FEATURE_TYPE_RADIUS: GdtFeatureType
GDT_FEATURE_TYPE_DISTANCE_BETWEEN: GdtFeatureType
GDT_FEATURE_TYPE_WIDTH: GdtFeatureType
GDT_FEATURE_TYPE_LENGTH: GdtFeatureType
GDT_FEATURE_TYPE_ANGLE_BETWEEN: GdtFeatureType
GDT_FEATURE_TYPE_ANGULARITY: GdtFeatureType
GDT_FEATURE_TYPE_PERPENDICULARITY: GdtFeatureType
GDT_FEATURE_TYPE_PARALLELISM: GdtFeatureType
GDT_FEATURE_TYPE_CIRCULARITY: GdtFeatureType
GDT_FEATURE_TYPE_CONCENTRICITY: GdtFeatureType
GDT_FEATURE_TYPE_CYLINDRICITY: GdtFeatureType
GDT_FEATURE_TYPE_STRAIGHTNESS: GdtFeatureType
GDT_FEATURE_TYPE_SURFACE_PROFILE: GdtFeatureType
GDT_FEATURE_TYPE_LINE_PROFILE: GdtFeatureType
GDT_FEATURE_TYPE_COMPOSITE_SURFACE_PROFILE: GdtFeatureType
GDT_FEATURE_TYPE_FLATNESS: GdtFeatureType
GDT_FEATURE_TYPE_TRUE_POSITION: GdtFeatureType
GDT_FEATURE_TYPE_COMPOSITE_TRUE_POSITION: GdtFeatureType
GDT_FEATURE_TYPE_CIRCULAR_RUNOUT: GdtFeatureType
GDT_FEATURE_TYPE_TOTAL_RUNOUT: GdtFeatureType
GDT_TOLERANCE_ZONE_TYPE_UNSPECIFIED: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_NONE: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_CYLINDRICAL: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_PLANAR: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_SPHERICAL: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_RADIAL_ARC: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_RADIAL_PLANAR: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_BOUNDARY: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_PLANAR_MEDIAN: GdtToleranceZoneType
GDT_TOLERANCE_ZONE_TYPE_SURFACE: GdtToleranceZoneType

class DatumAlignmentRequest(_message.Message):
    __slots__ = ("feature_check", "objects_to_move", "instruments_to_move", "apply_feature_check_transform")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    APPLY_FEATURE_CHECK_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    objects_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    instruments_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    apply_feature_check_transform: bool
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., objects_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., instruments_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., apply_feature_check_transform: bool = ...) -> None: ...

class DatumAlignmentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteFeatureChecksRequest(_message.Message):
    __slots__ = ("feature_checks",)
    FEATURE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    feature_checks: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, feature_checks: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class DeleteFeatureChecksResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableDatumAlignmentForFeatureCheckRequest(_message.Message):
    __slots__ = ("feature_check", "enable_datum_alignment", "enable_custom_initial_alignment", "enable_initial_datum_alignment", "alignment")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DATUM_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CUSTOM_INITIAL_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INITIAL_DATUM_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    enable_datum_alignment: bool
    enable_custom_initial_alignment: bool
    enable_initial_datum_alignment: bool
    alignment: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., enable_datum_alignment: bool = ..., enable_custom_initial_alignment: bool = ..., enable_initial_datum_alignment: bool = ..., alignment: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class EnableDisableDatumAlignmentForFeatureCheckResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EvaluateFeatureCheckRequest(_message.Message):
    __slots__ = ("feature_check", "perform_evaluation", "simultaneous_evaluation")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    PERFORM_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    SIMULTANEOUS_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    perform_evaluation: bool
    simultaneous_evaluation: bool
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., perform_evaluation: bool = ..., simultaneous_evaluation: bool = ...) -> None: ...

class EvaluateFeatureCheckResult(_message.Message):
    __slots__ = ("check_evaluated", "check_result", "non_unique_result", "measured_deviation_upper", "distance_out_of_tolerance_upper", "eval_delta_transform_upper", "measured_deviation_lower", "distance_out_of_tolerance_lower", "eval_delta_transform_lower", "check_type", "tolerance_type", "tolerance_simple", "tolerance_composite_upper", "tolerance_composite_lower", "tolerance_range_min", "tolerance_range_max", "tolerance_nominal_plus_minus_nominal", "tolerance_nominal_plus_minus_minus", "tolerance_nominal_plus_minus_plus", "execution")
    CHECK_EVALUATED_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESULT_FIELD_NUMBER: _ClassVar[int]
    NON_UNIQUE_RESULT_FIELD_NUMBER: _ClassVar[int]
    MEASURED_DEVIATION_UPPER_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_OUT_OF_TOLERANCE_UPPER_FIELD_NUMBER: _ClassVar[int]
    EVAL_DELTA_TRANSFORM_UPPER_FIELD_NUMBER: _ClassVar[int]
    MEASURED_DEVIATION_LOWER_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_OUT_OF_TOLERANCE_LOWER_FIELD_NUMBER: _ClassVar[int]
    EVAL_DELTA_TRANSFORM_LOWER_FIELD_NUMBER: _ClassVar[int]
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_COMPOSITE_UPPER_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_COMPOSITE_LOWER_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_RANGE_MIN_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_RANGE_MAX_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_NOMINAL_PLUS_MINUS_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_NOMINAL_PLUS_MINUS_MINUS_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_NOMINAL_PLUS_MINUS_PLUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    check_evaluated: bool
    check_result: str
    non_unique_result: bool
    measured_deviation_upper: float
    distance_out_of_tolerance_upper: float
    eval_delta_transform_upper: _spatial_analyzer_values_pb2.WorldTransform
    measured_deviation_lower: float
    distance_out_of_tolerance_lower: float
    eval_delta_transform_lower: _spatial_analyzer_values_pb2.WorldTransform
    check_type: str
    tolerance_type: str
    tolerance_simple: float
    tolerance_composite_upper: float
    tolerance_composite_lower: float
    tolerance_range_min: float
    tolerance_range_max: float
    tolerance_nominal_plus_minus_nominal: float
    tolerance_nominal_plus_minus_minus: float
    tolerance_nominal_plus_minus_plus: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, check_evaluated: bool = ..., check_result: _Optional[str] = ..., non_unique_result: bool = ..., measured_deviation_upper: _Optional[float] = ..., distance_out_of_tolerance_upper: _Optional[float] = ..., eval_delta_transform_upper: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., measured_deviation_lower: _Optional[float] = ..., distance_out_of_tolerance_lower: _Optional[float] = ..., eval_delta_transform_lower: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., check_type: _Optional[str] = ..., tolerance_type: _Optional[str] = ..., tolerance_simple: _Optional[float] = ..., tolerance_composite_upper: _Optional[float] = ..., tolerance_composite_lower: _Optional[float] = ..., tolerance_range_min: _Optional[float] = ..., tolerance_range_max: _Optional[float] = ..., tolerance_nominal_plus_minus_nominal: _Optional[float] = ..., tolerance_nominal_plus_minus_minus: _Optional[float] = ..., tolerance_nominal_plus_minus_plus: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EvaluateFeatureChecksRequest(_message.Message):
    __slots__ = ("feature_check_list", "simultaneous_evaluation", "restrict_evaluations_to_listed_checks")
    FEATURE_CHECK_LIST_FIELD_NUMBER: _ClassVar[int]
    SIMULTANEOUS_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    RESTRICT_EVALUATIONS_TO_LISTED_CHECKS_FIELD_NUMBER: _ClassVar[int]
    feature_check_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    simultaneous_evaluation: bool
    restrict_evaluations_to_listed_checks: bool
    def __init__(self, feature_check_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., simultaneous_evaluation: bool = ..., restrict_evaluations_to_listed_checks: bool = ...) -> None: ...

class EvaluateFeatureChecksResult(_message.Message):
    __slots__ = ("total_passed", "total_failed", "total_incomplete", "execution")
    TOTAL_PASSED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INCOMPLETE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_passed: int
    total_failed: int
    total_incomplete: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_passed: _Optional[int] = ..., total_failed: _Optional[int] = ..., total_incomplete: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FeatureCheckCylinderEvalOptions(_message.Message):
    __slots__ = ("enable_actual_diameter_override", "actual_diameter_override")
    ENABLE_ACTUAL_DIAMETER_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DIAMETER_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    enable_actual_diameter_override: bool
    actual_diameter_override: float
    def __init__(self, enable_actual_diameter_override: bool = ..., actual_diameter_override: _Optional[float] = ...) -> None: ...

class FeatureCheckDatumReference(_message.Message):
    __slots__ = ("reference_string", "cad_faces", "sa_objects", "auxiliary_sa_objects", "geometry_relationships", "auxiliary_geometry_relationships")
    REFERENCE_STRING_FIELD_NUMBER: _ClassVar[int]
    CAD_FACES_FIELD_NUMBER: _ClassVar[int]
    SA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_SA_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_GEOMETRY_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    reference_string: str
    cad_faces: str
    sa_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    auxiliary_sa_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    geometry_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    auxiliary_geometry_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, reference_string: _Optional[str] = ..., cad_faces: _Optional[str] = ..., sa_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., auxiliary_sa_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., geometry_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., auxiliary_geometry_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class FeatureCheckReportingOptions(_message.Message):
    __slots__ = ("show_feature_control_frame_summary", "include_title", "show_datum_and_tolerance_summary", "show_feature_summary", "only_create_failed_vectors", "show_point_details", "show_lower_tier_tables")
    SHOW_FEATURE_CONTROL_FRAME_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SHOW_DATUM_AND_TOLERANCE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SHOW_FEATURE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ONLY_CREATE_FAILED_VECTORS_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SHOW_LOWER_TIER_TABLES_FIELD_NUMBER: _ClassVar[int]
    show_feature_control_frame_summary: bool
    include_title: bool
    show_datum_and_tolerance_summary: bool
    show_feature_summary: bool
    only_create_failed_vectors: bool
    show_point_details: bool
    show_lower_tier_tables: bool
    def __init__(self, show_feature_control_frame_summary: bool = ..., include_title: bool = ..., show_datum_and_tolerance_summary: bool = ..., show_feature_summary: bool = ..., only_create_failed_vectors: bool = ..., show_point_details: bool = ..., show_lower_tier_tables: bool = ...) -> None: ...

class FeatureInspectionAutoFilterRequest(_message.Message):
    __slots__ = ("point_names", "group_names", "cloud_names", "surface_offset", "edge_offset", "offset_direction", "include_points_within_cylinder_axis_proximity", "enforce_max_points_per_face_in_output", "max_points_per_face", "feature_check_name_list", "include_datums", "create_cloud_for_each_datum_or_check")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    SURFACE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    EDGE_OFFSET_FIELD_NUMBER: _ClassVar[int]
    OFFSET_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_POINTS_WITHIN_CYLINDER_AXIS_PROXIMITY_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MAX_POINTS_PER_FACE_IN_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    MAX_POINTS_PER_FACE_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECK_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DATUMS_FIELD_NUMBER: _ClassVar[int]
    CREATE_CLOUD_FOR_EACH_DATUM_OR_CHECK_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    surface_offset: float
    edge_offset: float
    offset_direction: _spatial_analyzer_values_pb2.OffsetDirectionType
    include_points_within_cylinder_axis_proximity: bool
    enforce_max_points_per_face_in_output: bool
    max_points_per_face: int
    feature_check_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    include_datums: bool
    create_cloud_for_each_datum_or_check: bool
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., surface_offset: _Optional[float] = ..., edge_offset: _Optional[float] = ..., offset_direction: _Optional[_Union[_spatial_analyzer_values_pb2.OffsetDirectionType, str]] = ..., include_points_within_cylinder_axis_proximity: bool = ..., enforce_max_points_per_face_in_output: bool = ..., max_points_per_face: _Optional[int] = ..., feature_check_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., include_datums: bool = ..., create_cloud_for_each_datum_or_check: bool = ...) -> None: ...

class FeatureInspectionAutoFilterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GdtMeasurements(_message.Message):
    __slots__ = ("point_names", "cloud_names")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class GdtOptions(_message.Message):
    __slots__ = ("use_high_points", "extrapolate_axial_extent", "exclude_from_auto_evaluation", "distance_between_mode", "evaluation_method", "create_actual_features", "create_solved_points", "cross_section_criteria", "enable_auto_feature_detection")
    USE_HIGH_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXTRAPOLATE_AXIAL_EXTENT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FROM_AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_BETWEEN_MODE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACTUAL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SOLVED_POINTS_FIELD_NUMBER: _ClassVar[int]
    CROSS_SECTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTO_FEATURE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    use_high_points: bool
    extrapolate_axial_extent: bool
    exclude_from_auto_evaluation: bool
    distance_between_mode: GdtDistanceBetweenMode
    evaluation_method: GdtEvaluationMethod
    create_actual_features: bool
    create_solved_points: bool
    cross_section_criteria: float
    enable_auto_feature_detection: bool
    def __init__(self, use_high_points: bool = ..., extrapolate_axial_extent: bool = ..., exclude_from_auto_evaluation: bool = ..., distance_between_mode: _Optional[_Union[GdtDistanceBetweenMode, str]] = ..., evaluation_method: _Optional[_Union[GdtEvaluationMethod, str]] = ..., create_actual_features: bool = ..., create_solved_points: bool = ..., cross_section_criteria: _Optional[float] = ..., enable_auto_feature_detection: bool = ...) -> None: ...

class GenerateFeatureCheckSummaryRequest(_message.Message):
    __slots__ = ("feature_check_list", "summary_table_name")
    FEATURE_CHECK_LIST_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    feature_check_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    summary_table_name: str
    def __init__(self, feature_check_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., summary_table_name: _Optional[str] = ...) -> None: ...

class GenerateFeatureCheckSummaryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetDatumMeasurementsRequest(_message.Message):
    __slots__ = ("datum",)
    DATUM_FIELD_NUMBER: _ClassVar[int]
    datum: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, datum: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetDatumMeasurementsResult(_message.Message):
    __slots__ = ("measurements", "execution")
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    measurements: GdtMeasurements
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, measurements: _Optional[_Union[GdtMeasurements, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFeatureCheckCylinderEvalOptionsRequest(_message.Message):
    __slots__ = ("feature_check",)
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetFeatureCheckCylinderEvalOptionsResult(_message.Message):
    __slots__ = ("options", "execution")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    options: FeatureCheckCylinderEvalOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, options: _Optional[_Union[FeatureCheckCylinderEvalOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFeatureCheckDatumReferencesRequest(_message.Message):
    __slots__ = ("feature_check",)
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetFeatureCheckDatumReferencesResult(_message.Message):
    __slots__ = ("datum_1", "datum_2", "datum_3", "execution")
    DATUM_1_FIELD_NUMBER: _ClassVar[int]
    DATUM_2_FIELD_NUMBER: _ClassVar[int]
    DATUM_3_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    datum_1: FeatureCheckDatumReference
    datum_2: FeatureCheckDatumReference
    datum_3: FeatureCheckDatumReference
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, datum_1: _Optional[_Union[FeatureCheckDatumReference, _Mapping]] = ..., datum_2: _Optional[_Union[FeatureCheckDatumReference, _Mapping]] = ..., datum_3: _Optional[_Union[FeatureCheckDatumReference, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFeatureCheckMeasurementsRequest(_message.Message):
    __slots__ = ("feature_check",)
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetFeatureCheckMeasurementsResult(_message.Message):
    __slots__ = ("measurements", "execution")
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    measurements: GdtMeasurements
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, measurements: _Optional[_Union[GdtMeasurements, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFeatureCheckReportingFrameRequest(_message.Message):
    __slots__ = ("feature_check",)
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetFeatureCheckReportingFrameResult(_message.Message):
    __slots__ = ("reporting_frame", "execution")
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFeatureCheckReportingOptionsRequest(_message.Message):
    __slots__ = ("feature_check",)
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class GetFeatureCheckReportingOptionsResult(_message.Message):
    __slots__ = ("options", "execution")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    options: FeatureCheckReportingOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, options: _Optional[_Union[FeatureCheckReportingOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGdtExtendedOptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGdtExtendedOptionsResult(_message.Message):
    __slots__ = ("use_extended_options", "execution")
    USE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    use_extended_options: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, use_extended_options: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetGdtOptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGdtOptionsResult(_message.Message):
    __slots__ = ("options", "execution")
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    options: GdtOptions
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, options: _Optional[_Union[GdtOptions, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeAnnotationRefListFromCollectionRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeAnnotationRefListFromCollectionResult(_message.Message):
    __slots__ = ("annotations", "execution")
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, annotations: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeAnnotationRefListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "annotation_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    annotation_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., annotation_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakeAnnotationRefListWildcardSelectionResult(_message.Message):
    __slots__ = ("annotations", "execution")
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, annotations: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeDatumRefListFromCollectionRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeDatumRefListFromCollectionResult(_message.Message):
    __slots__ = ("datums", "execution")
    DATUMS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    datums: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, datums: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeFeatureCheckReferenceListWildcardSelectionRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "feature_check_wildcard_criteria")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECK_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    feature_check_wildcard_criteria: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., feature_check_wildcard_criteria: _Optional[str] = ...) -> None: ...

class MakeFeatureCheckReferenceListWildcardSelectionResult(_message.Message):
    __slots__ = ("feature_checks", "execution")
    FEATURE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    feature_checks: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, feature_checks: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeFeatureCheckRefListFromCollectionRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeFeatureCheckRefListFromCollectionResult(_message.Message):
    __slots__ = ("feature_checks", "execution")
    FEATURE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    feature_checks: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, feature_checks: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeFeatureChecksRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MakeFeatureChecksResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGdtDatumAnnotationRequest(_message.Message):
    __slots__ = ("datum_name", "objects", "geometry_relationships", "surface_faces", "auxiliary_object", "auxiliary_geometry_relationship", "is_slot", "force_surface_feature")
    DATUM_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_OBJECT_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_GEOMETRY_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    IS_SLOT_FIELD_NUMBER: _ClassVar[int]
    FORCE_SURFACE_FEATURE_FIELD_NUMBER: _ClassVar[int]
    datum_name: str
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    geometry_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    auxiliary_object: _spatial_analyzer_values_pb2.CollectionObjectName
    auxiliary_geometry_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    is_slot: bool
    force_surface_feature: bool
    def __init__(self, datum_name: _Optional[str] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., geometry_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., auxiliary_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., auxiliary_geometry_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., is_slot: bool = ..., force_surface_feature: bool = ...) -> None: ...

class MakeGdtDatumAnnotationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeGdtFeatureCheckAnnotationRequest(_message.Message):
    __slots__ = ("feature_annotation_name", "feature_type", "objects", "geometry_relationships", "surface_faces", "decompose_multiple_features", "auto_create_diameter_checks", "auto_create_slot_width_checks", "auto_create_slot_length_checks", "datum_references", "tolerance", "is_slot", "per_unit_length_or_area", "circular_area", "per_unit_area_length_distance", "per_unit_area_length_step_over_percent", "per_unit_area_width_distance", "per_unit_area_width_step_over_percent", "per_unit_area_circle_diameter", "per_unit_area_diameter_step_over", "auxiliary_object", "auxiliary_geometry_relationship", "use_nominal_for_dimension_tolerance", "use_reference_object_for_nominal", "nominal_dimension_tolerance", "low_dimension_tolerance", "high_dimension_tolerance", "tolerance_zone_type", "use_projected_tolerance_zone", "projected_tolerance_zone")
    FEATURE_ANNOTATION_NAME_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    DECOMPOSE_MULTIPLE_FEATURES_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_DIAMETER_CHECKS_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_SLOT_WIDTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
    AUTO_CREATE_SLOT_LENGTH_CHECKS_FIELD_NUMBER: _ClassVar[int]
    DATUM_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    IS_SLOT_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_LENGTH_OR_AREA_FIELD_NUMBER: _ClassVar[int]
    CIRCULAR_AREA_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_LENGTH_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_LENGTH_STEP_OVER_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_WIDTH_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_WIDTH_STEP_OVER_PERCENT_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_CIRCLE_DIAMETER_FIELD_NUMBER: _ClassVar[int]
    PER_UNIT_AREA_DIAMETER_STEP_OVER_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_OBJECT_FIELD_NUMBER: _ClassVar[int]
    AUXILIARY_GEOMETRY_RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    USE_NOMINAL_FOR_DIMENSION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    USE_REFERENCE_OBJECT_FOR_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_DIMENSION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_DIMENSION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_DIMENSION_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_ZONE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_PROJECTED_TOLERANCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    PROJECTED_TOLERANCE_ZONE_FIELD_NUMBER: _ClassVar[int]
    feature_annotation_name: str
    feature_type: GdtFeatureType
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    geometry_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    decompose_multiple_features: bool
    auto_create_diameter_checks: bool
    auto_create_slot_width_checks: bool
    auto_create_slot_length_checks: bool
    datum_references: str
    tolerance: str
    is_slot: bool
    per_unit_length_or_area: bool
    circular_area: bool
    per_unit_area_length_distance: float
    per_unit_area_length_step_over_percent: float
    per_unit_area_width_distance: float
    per_unit_area_width_step_over_percent: float
    per_unit_area_circle_diameter: float
    per_unit_area_diameter_step_over: float
    auxiliary_object: _spatial_analyzer_values_pb2.CollectionObjectName
    auxiliary_geometry_relationship: _spatial_analyzer_values_pb2.CollectionItemName
    use_nominal_for_dimension_tolerance: bool
    use_reference_object_for_nominal: bool
    nominal_dimension_tolerance: float
    low_dimension_tolerance: float
    high_dimension_tolerance: float
    tolerance_zone_type: GdtToleranceZoneType
    use_projected_tolerance_zone: bool
    projected_tolerance_zone: float
    def __init__(self, feature_annotation_name: _Optional[str] = ..., feature_type: _Optional[_Union[GdtFeatureType, str]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., geometry_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., decompose_multiple_features: bool = ..., auto_create_diameter_checks: bool = ..., auto_create_slot_width_checks: bool = ..., auto_create_slot_length_checks: bool = ..., datum_references: _Optional[str] = ..., tolerance: _Optional[str] = ..., is_slot: bool = ..., per_unit_length_or_area: bool = ..., circular_area: bool = ..., per_unit_area_length_distance: _Optional[float] = ..., per_unit_area_length_step_over_percent: _Optional[float] = ..., per_unit_area_width_distance: _Optional[float] = ..., per_unit_area_width_step_over_percent: _Optional[float] = ..., per_unit_area_circle_diameter: _Optional[float] = ..., per_unit_area_diameter_step_over: _Optional[float] = ..., auxiliary_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., auxiliary_geometry_relationship: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., use_nominal_for_dimension_tolerance: bool = ..., use_reference_object_for_nominal: bool = ..., nominal_dimension_tolerance: _Optional[float] = ..., low_dimension_tolerance: _Optional[float] = ..., high_dimension_tolerance: _Optional[float] = ..., tolerance_zone_type: _Optional[_Union[GdtToleranceZoneType, str]] = ..., use_projected_tolerance_zone: bool = ..., projected_tolerance_zone: _Optional[float] = ...) -> None: ...

class MakeGdtFeatureCheckAnnotationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSurfaceFaceListFromSurfaceRequest(_message.Message):
    __slots__ = ("surface",)
    SURFACE_FIELD_NUMBER: _ClassVar[int]
    surface: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, surface: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeSurfaceFaceListFromSurfaceResult(_message.Message):
    __slots__ = ("surface_faces", "execution")
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSurfaceFaceListRuntimeSelectRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MakeSurfaceFaceListRuntimeSelectResult(_message.Message):
    __slots__ = ("surface_faces", "execution")
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RefreshDatumsFeatureChecksFromAnnotationsRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class RefreshDatumsFeatureChecksFromAnnotationsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDatumMeasurementsRequest(_message.Message):
    __slots__ = ("datum", "point_names", "cloud_names", "replace_existing_measurements")
    DATUM_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    datum: _spatial_analyzer_values_pb2.CollectionItemName
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    replace_existing_measurements: bool
    def __init__(self, datum: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., replace_existing_measurements: bool = ...) -> None: ...

class SetDatumMeasurementsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFeatureCheckCylinderEvalOptionsRequest(_message.Message):
    __slots__ = ("feature_check", "enable_actual_diameter_override", "actual_diameter_override")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_ACTUAL_DIAMETER_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_DIAMETER_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    enable_actual_diameter_override: bool
    actual_diameter_override: float
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., enable_actual_diameter_override: bool = ..., actual_diameter_override: _Optional[float] = ...) -> None: ...

class SetFeatureCheckCylinderEvalOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFeatureCheckMeasurementsRequest(_message.Message):
    __slots__ = ("feature_check", "point_names", "cloud_names", "replace_existing_measurements")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    replace_existing_measurements: bool
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., replace_existing_measurements: bool = ...) -> None: ...

class SetFeatureCheckMeasurementsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFeatureCheckReportingFrameRequest(_message.Message):
    __slots__ = ("feature_check", "reporting_frame")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    reporting_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., reporting_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetFeatureCheckReportingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFeatureCheckReportingOptionsRequest(_message.Message):
    __slots__ = ("feature_check", "show_feature_control_frame_summary", "include_title", "show_datum_and_tolerance_summary", "show_feature_summary", "only_create_failed_vectors", "show_point_details_summary", "show_lower_tier_tables")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    SHOW_FEATURE_CONTROL_FRAME_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SHOW_DATUM_AND_TOLERANCE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SHOW_FEATURE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    ONLY_CREATE_FAILED_VECTORS_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_DETAILS_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SHOW_LOWER_TIER_TABLES_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    show_feature_control_frame_summary: bool
    include_title: bool
    show_datum_and_tolerance_summary: bool
    show_feature_summary: bool
    only_create_failed_vectors: bool
    show_point_details_summary: bool
    show_lower_tier_tables: bool
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., show_feature_control_frame_summary: bool = ..., include_title: bool = ..., show_datum_and_tolerance_summary: bool = ..., show_feature_summary: bool = ..., only_create_failed_vectors: bool = ..., show_point_details_summary: bool = ..., show_lower_tier_tables: bool = ...) -> None: ...

class SetFeatureCheckReportingOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGdtExtendedOptionsRequest(_message.Message):
    __slots__ = ("use_extended_options", "circle_extended_options", "cone_extended_options", "cylinder_extended_options", "ellipse_extended_options", "line_extended_options", "open_slot_extended_options", "plane_extended_options", "slot_extended_options", "sphere_extended_options")
    USE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CONE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CYLINDER_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ELLIPSE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LINE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPEN_SLOT_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PLANE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SLOT_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SPHERE_EXTENDED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    use_extended_options: bool
    circle_extended_options: GdtExtendedEvaluationMethod
    cone_extended_options: GdtExtendedEvaluationMethod
    cylinder_extended_options: GdtExtendedEvaluationMethod
    ellipse_extended_options: GdtExtendedEvaluationMethod
    line_extended_options: GdtExtendedEvaluationMethod
    open_slot_extended_options: GdtExtendedEvaluationMethod
    plane_extended_options: GdtExtendedEvaluationMethod
    slot_extended_options: GdtExtendedEvaluationMethod
    sphere_extended_options: GdtExtendedEvaluationMethod
    def __init__(self, use_extended_options: bool = ..., circle_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., cone_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., cylinder_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., ellipse_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., line_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., open_slot_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., plane_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., slot_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ..., sphere_extended_options: _Optional[_Union[GdtExtendedEvaluationMethod, str]] = ...) -> None: ...

class SetGdtExtendedOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGdtOptionsRequest(_message.Message):
    __slots__ = ("use_high_points", "extrapolate_axial_extent", "exclude_from_auto_evaluation", "distance_between_mode", "evaluation_method", "create_actual_features", "create_solved_points", "cross_section_criteria", "enable_auto_feature_detection")
    USE_HIGH_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXTRAPOLATE_AXIAL_EXTENT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FROM_AUTO_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_BETWEEN_MODE_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    CREATE_ACTUAL_FEATURES_FIELD_NUMBER: _ClassVar[int]
    CREATE_SOLVED_POINTS_FIELD_NUMBER: _ClassVar[int]
    CROSS_SECTION_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUTO_FEATURE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    use_high_points: bool
    extrapolate_axial_extent: bool
    exclude_from_auto_evaluation: bool
    distance_between_mode: GdtDistanceBetweenMode
    evaluation_method: GdtEvaluationMethod
    create_actual_features: bool
    create_solved_points: bool
    cross_section_criteria: float
    enable_auto_feature_detection: bool
    def __init__(self, use_high_points: bool = ..., extrapolate_axial_extent: bool = ..., exclude_from_auto_evaluation: bool = ..., distance_between_mode: _Optional[_Union[GdtDistanceBetweenMode, str]] = ..., evaluation_method: _Optional[_Union[GdtEvaluationMethod, str]] = ..., create_actual_features: bool = ..., create_solved_points: bool = ..., cross_section_criteria: _Optional[float] = ..., enable_auto_feature_detection: bool = ...) -> None: ...

class SetGdtOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetGlobalForceSimultaneousEvaluationRequest(_message.Message):
    __slots__ = ("global_simultaneous_evaluation",)
    GLOBAL_SIMULTANEOUS_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    global_simultaneous_evaluation: bool
    def __init__(self, global_simultaneous_evaluation: bool = ...) -> None: ...

class SetGlobalForceSimultaneousEvaluationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartStopFeatureCheckTrappingRequest(_message.Message):
    __slots__ = ("feature_check", "instrument_id", "start_trapping")
    FEATURE_CHECK_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TRAPPING_FIELD_NUMBER: _ClassVar[int]
    feature_check: _spatial_analyzer_values_pb2.CollectionItemName
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    start_trapping: bool
    def __init__(self, feature_check: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., start_trapping: bool = ...) -> None: ...

class StartStopFeatureCheckTrappingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
