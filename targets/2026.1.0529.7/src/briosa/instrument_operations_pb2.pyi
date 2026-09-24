from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollimationBaselineMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLIMATION_BASELINE_METHOD_UNSPECIFIED: _ClassVar[CollimationBaselineMethod]
    COLLIMATION_BASELINE_METHOD_DETERMINED_BY_VALUE: _ClassVar[CollimationBaselineMethod]
    COLLIMATION_BASELINE_METHOD_DETERMINED_FROM_SCALE: _ClassVar[CollimationBaselineMethod]
    COLLIMATION_BASELINE_METHOD_DETERMINED_FROM_KNOWN_POINT: _ClassVar[CollimationBaselineMethod]

class CollimationTiltMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLIMATION_TILT_MODE_UNSPECIFIED: _ClassVar[CollimationTiltMode]
    COLLIMATION_TILT_MODE_FULL_COLLIMATION: _ClassVar[CollimationTiltMode]
    COLLIMATION_TILT_MODE_NO_TILT_COLLIMATION: _ClassVar[CollimationTiltMode]

class InspectionFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSPECTION_FILTER_UNSPECIFIED: _ClassVar[InspectionFilter]
    INSPECTION_FILTER_ALL: _ClassVar[InspectionFilter]
    INSPECTION_FILTER_CHECKS: _ClassVar[InspectionFilter]
    INSPECTION_FILTER_DATUMS: _ClassVar[InspectionFilter]

class InstrumentPositionReportingFrame(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_POSITION_REPORTING_FRAME_UNSPECIFIED: _ClassVar[InstrumentPositionReportingFrame]
    INSTRUMENT_POSITION_REPORTING_FRAME_INSTRUMENT_BASE: _ClassVar[InstrumentPositionReportingFrame]
    INSTRUMENT_POSITION_REPORTING_FRAME_WORLD: _ClassVar[InstrumentPositionReportingFrame]
    INSTRUMENT_POSITION_REPORTING_FRAME_WORKING: _ClassVar[InstrumentPositionReportingFrame]

class ShowUsmnDialog(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHOW_USMN_DIALOG_UNSPECIFIED: _ClassVar[ShowUsmnDialog]
    SHOW_USMN_DIALOG_NO: _ClassVar[ShowUsmnDialog]
    SHOW_USMN_DIALOG_YES: _ClassVar[ShowUsmnDialog]
    SHOW_USMN_DIALOG_ON_TOLERANCE_VIOLATION: _ClassVar[ShowUsmnDialog]

class TargetComputationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_COMPUTATION_METHOD_UNSPECIFIED: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_USE_MOST_RECENT_SHOT_FROM_EACH_FACE: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_USE_ONLY_MOST_RECENT_SHOT: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_DO_NOT_CHANGE_PRIOR_MEASUREMENTS: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_FORCE_NEW_POINT_FOR_EACH_MEASUREMENT: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_REMOVE_ALL_PRIOR_SHOTS: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_DEACTIVATE_ALL_PRIOR_SHOTS: _ClassVar[TargetComputationMethod]
COLLIMATION_BASELINE_METHOD_UNSPECIFIED: CollimationBaselineMethod
COLLIMATION_BASELINE_METHOD_DETERMINED_BY_VALUE: CollimationBaselineMethod
COLLIMATION_BASELINE_METHOD_DETERMINED_FROM_SCALE: CollimationBaselineMethod
COLLIMATION_BASELINE_METHOD_DETERMINED_FROM_KNOWN_POINT: CollimationBaselineMethod
COLLIMATION_TILT_MODE_UNSPECIFIED: CollimationTiltMode
COLLIMATION_TILT_MODE_FULL_COLLIMATION: CollimationTiltMode
COLLIMATION_TILT_MODE_NO_TILT_COLLIMATION: CollimationTiltMode
INSPECTION_FILTER_UNSPECIFIED: InspectionFilter
INSPECTION_FILTER_ALL: InspectionFilter
INSPECTION_FILTER_CHECKS: InspectionFilter
INSPECTION_FILTER_DATUMS: InspectionFilter
INSTRUMENT_POSITION_REPORTING_FRAME_UNSPECIFIED: InstrumentPositionReportingFrame
INSTRUMENT_POSITION_REPORTING_FRAME_INSTRUMENT_BASE: InstrumentPositionReportingFrame
INSTRUMENT_POSITION_REPORTING_FRAME_WORLD: InstrumentPositionReportingFrame
INSTRUMENT_POSITION_REPORTING_FRAME_WORKING: InstrumentPositionReportingFrame
SHOW_USMN_DIALOG_UNSPECIFIED: ShowUsmnDialog
SHOW_USMN_DIALOG_NO: ShowUsmnDialog
SHOW_USMN_DIALOG_YES: ShowUsmnDialog
SHOW_USMN_DIALOG_ON_TOLERANCE_VIOLATION: ShowUsmnDialog
TARGET_COMPUTATION_METHOD_UNSPECIFIED: TargetComputationMethod
TARGET_COMPUTATION_METHOD_USE_MOST_RECENT_SHOT_FROM_EACH_FACE: TargetComputationMethod
TARGET_COMPUTATION_METHOD_USE_ONLY_MOST_RECENT_SHOT: TargetComputationMethod
TARGET_COMPUTATION_METHOD_DO_NOT_CHANGE_PRIOR_MEASUREMENTS: TargetComputationMethod
TARGET_COMPUTATION_METHOD_FORCE_NEW_POINT_FOR_EACH_MEASUREMENT: TargetComputationMethod
TARGET_COMPUTATION_METHOD_REMOVE_ALL_PRIOR_SHOTS: TargetComputationMethod
TARGET_COMPUTATION_METHOD_DEACTIVATE_ALL_PRIOR_SHOTS: TargetComputationMethod

class ActivateDeactivateInstrumentToolbarRequest(_message.Message):
    __slots__ = ("instrument", "deactivate_toolbar")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATE_TOOLBAR_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    deactivate_toolbar: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., deactivate_toolbar: bool = ...) -> None: ...

class ActivateDeactivateInstrumentToolbarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddNewInstrumentRequest(_message.Message):
    __slots__ = ("instrument_type",)
    INSTRUMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    instrument_type: InstrumentTypeName
    def __init__(self, instrument_type: _Optional[_Union[InstrumentTypeName, _Mapping]] = ...) -> None: ...

class AddNewInstrumentResult(_message.Message):
    __slots__ = ("instrument_added", "execution")
    INSTRUMENT_ADDED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instrument_added: _spatial_analyzer_values_pb2.CollectionInstrumentId
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instrument_added: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddNominalPointToTcpFixtureRequest(_message.Message):
    __slots__ = ("tcp_fixture", "nominal_point_name", "nominal_point_location", "var_xx", "var_yy", "var_zz", "covar_xy", "covar_xz", "covar_yz")
    TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VAR_XX_FIELD_NUMBER: _ClassVar[int]
    VAR_YY_FIELD_NUMBER: _ClassVar[int]
    VAR_ZZ_FIELD_NUMBER: _ClassVar[int]
    COVAR_XY_FIELD_NUMBER: _ClassVar[int]
    COVAR_XZ_FIELD_NUMBER: _ClassVar[int]
    COVAR_YZ_FIELD_NUMBER: _ClassVar[int]
    tcp_fixture: _spatial_analyzer_values_pb2.CollectionObjectName
    nominal_point_name: str
    nominal_point_location: _spatial_analyzer_values_pb2.Vector
    var_xx: float
    var_yy: float
    var_zz: float
    covar_xy: float
    covar_xz: float
    covar_yz: float
    def __init__(self, tcp_fixture: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., nominal_point_name: _Optional[str] = ..., nominal_point_location: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., var_xx: _Optional[float] = ..., var_yy: _Optional[float] = ..., var_zz: _Optional[float] = ..., covar_xy: _Optional[float] = ..., covar_xz: _Optional[float] = ..., covar_yz: _Optional[float] = ...) -> None: ...

class AddNominalPointToTcpFixtureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AlignCloudToCadRequest(_message.Message):
    __slots__ = ("cloud", "surfaces", "maximum_coarse_cad_mesh_edge_length", "use_fine_cad_mesh", "execute_alignment")
    CLOUD_FIELD_NUMBER: _ClassVar[int]
    SURFACES_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_COARSE_CAD_MESH_EDGE_LENGTH_FIELD_NUMBER: _ClassVar[int]
    USE_FINE_CAD_MESH_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    cloud: _spatial_analyzer_values_pb2.CollectionObjectName
    surfaces: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    maximum_coarse_cad_mesh_edge_length: float
    use_fine_cad_mesh: bool
    execute_alignment: bool
    def __init__(self, cloud: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surfaces: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., maximum_coarse_cad_mesh_edge_length: _Optional[float] = ..., use_fine_cad_mesh: bool = ..., execute_alignment: bool = ...) -> None: ...

class AlignCloudToCadResult(_message.Message):
    __slots__ = ("alignment", "execution")
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    alignment: CloudToCadAlignmentResult
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, alignment: _Optional[_Union[CloudToCadAlignmentResult, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AlignLaserProjectorRequest(_message.Message):
    __slots__ = ("instrument", "group")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    group: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class AlignLaserProjectorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AlignTwoTargetsWithAxisWcfXRequest(_message.Message):
    __slots__ = ("instrument", "first_point_on_axis", "second_point_on_axis", "initial_measured_group", "rotational_tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FIRST_POINT_ON_AXIS_FIELD_NUMBER: _ClassVar[int]
    SECOND_POINT_ON_AXIS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MEASURED_GROUP_FIELD_NUMBER: _ClassVar[int]
    ROTATIONAL_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    first_point_on_axis: _spatial_analyzer_values_pb2.PointName
    second_point_on_axis: _spatial_analyzer_values_pb2.PointName
    initial_measured_group: _spatial_analyzer_values_pb2.CollectionObjectName
    rotational_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., first_point_on_axis: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., second_point_on_axis: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., initial_measured_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., rotational_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class AlignTwoTargetsWithAxisWcfXResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AssociateObjectsWithInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "objects")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class AssociateObjectsWithInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoCorrespondClosestPointRequest(_message.Message):
    __slots__ = ("instrument", "reference_group", "actuals_group", "wait_for_completion")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTUALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    actuals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    wait_for_completion: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actuals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., wait_for_completion: bool = ...) -> None: ...

class AutoCorrespondClosestPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoCorrespondWithProximityTriggerRequest(_message.Message):
    __slots__ = ("instrument", "nominal_group", "results_group", "point_distance_threshold", "vector_axis_threshold", "project_results_to_nominal_vector", "warbler_ramp_start_distance", "show_watch_window", "deviation_vector_group_name", "make_unmeasured_group", "measure_each_point_only_once")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESULTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    POINT_DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    VECTOR_AXIS_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_RESULTS_TO_NOMINAL_VECTOR_FIELD_NUMBER: _ClassVar[int]
    WARBLER_RAMP_START_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SHOW_WATCH_WINDOW_FIELD_NUMBER: _ClassVar[int]
    DEVIATION_VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    MAKE_UNMEASURED_GROUP_FIELD_NUMBER: _ClassVar[int]
    MEASURE_EACH_POINT_ONLY_ONCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    nominal_group: _spatial_analyzer_values_pb2.CollectionObjectName
    results_group: _spatial_analyzer_values_pb2.CollectionObjectName
    point_distance_threshold: float
    vector_axis_threshold: float
    project_results_to_nominal_vector: bool
    warbler_ramp_start_distance: float
    show_watch_window: bool
    deviation_vector_group_name: str
    make_unmeasured_group: bool
    measure_each_point_only_once: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., nominal_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., results_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_distance_threshold: _Optional[float] = ..., vector_axis_threshold: _Optional[float] = ..., project_results_to_nominal_vector: bool = ..., warbler_ramp_start_distance: _Optional[float] = ..., show_watch_window: bool = ..., deviation_vector_group_name: _Optional[str] = ..., make_unmeasured_group: bool = ..., measure_each_point_only_once: bool = ...) -> None: ...

class AutoCorrespondWithProximityTriggerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoMeasureBatchOfFeaturesRequest(_message.Message):
    __slots__ = ("instrument", "features", "wait_for_complete")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    features: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    wait_for_complete: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., features: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., wait_for_complete: bool = ...) -> None: ...

class AutoMeasureBatchOfFeaturesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoMeasurePointsRequest(_message.Message):
    __slots__ = ("instrument", "reference_group", "actuals_group", "force_existing_group", "show_complete_dialog", "wait_for_completion", "auto_start")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTUALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    FORCE_EXISTING_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_COMPLETE_DIALOG_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    AUTO_START_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    actuals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    force_existing_group: bool
    show_complete_dialog: bool
    wait_for_completion: bool
    auto_start: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actuals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., force_existing_group: bool = ..., show_complete_dialog: bool = ..., wait_for_completion: bool = ..., auto_start: bool = ...) -> None: ...

class AutoMeasurePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoMeasureSpecifiedGeometryRequest(_message.Message):
    __slots__ = ("instrument", "geometry", "mode_profile", "wait_for_complete")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    MODE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    geometry: _spatial_analyzer_values_pb2.CollectionObjectName
    mode_profile: str
    wait_for_complete: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., geometry: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., mode_profile: _Optional[str] = ..., wait_for_complete: bool = ...) -> None: ...

class AutoMeasureSpecifiedGeometryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoMeasureSurfaceVectorIntersectionsRequest(_message.Message):
    __slots__ = ("instrument", "vector_group", "resultant_group", "wait_for_complete")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_GROUP_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    vector_group: _spatial_analyzer_values_pb2.CollectionObjectName
    resultant_group: _spatial_analyzer_values_pb2.CollectionObjectName
    wait_for_complete: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., vector_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resultant_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., wait_for_complete: bool = ...) -> None: ...

class AutoMeasureSurfaceVectorIntersectionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoMeasureVectorsRequest(_message.Message):
    __slots__ = ("instrument", "vector_group", "actuals_group", "project_point_to_vector", "angle_tolerance", "high_tolerance", "low_tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTUALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    PROJECT_POINT_TO_VECTOR_FIELD_NUMBER: _ClassVar[int]
    ANGLE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    vector_group: _spatial_analyzer_values_pb2.CollectionObjectName
    actuals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    project_point_to_vector: bool
    angle_tolerance: float
    high_tolerance: float
    low_tolerance: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., vector_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actuals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., project_point_to_vector: bool = ..., angle_tolerance: _Optional[float] = ..., high_tolerance: _Optional[float] = ..., low_tolerance: _Optional[float] = ...) -> None: ...

class AutoMeasureVectorsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class BuildTargetRequest(_message.Message):
    __slots__ = ("instrument", "output_target_name", "nominal_point", "tolerance", "html_prompt_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINT_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    output_target_name: _spatial_analyzer_values_pb2.PointName
    nominal_point: _spatial_analyzer_values_pb2.PointName
    tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., output_target_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., nominal_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class BuildTargetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CalculateTcpFixtureUncertaintiesRequest(_message.Message):
    __slots__ = ("tcp_fixture", "tcp_in_working", "tcp_measurements")
    TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    TCP_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    TCP_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    tcp_fixture: _spatial_analyzer_values_pb2.CollectionObjectName
    tcp_in_working: _spatial_analyzer_values_pb2.Transform
    tcp_measurements: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, tcp_fixture: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., tcp_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., tcp_measurements: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class CalculateTcpFixtureUncertaintiesResult(_message.Message):
    __slots__ = ("uncertainties", "execution")
    UNCERTAINTIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    uncertainties: TcpFixtureUncertainties
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, uncertainties: _Optional[_Union[TcpFixtureUncertainties, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearCloudViewerRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class ClearCloudViewerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CloseAutoCorrespondClosestPointDialogRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class CloseAutoCorrespondClosestPointDialogResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CloudToCadAlignmentResult(_message.Message):
    __slots__ = ("rms_deviation", "average_deviation", "maximum_absolute_deviation", "resultant_transform_in_working")
    RMS_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    RESULTANT_TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    rms_deviation: float
    average_deviation: float
    maximum_absolute_deviation: float
    resultant_transform_in_working: _spatial_analyzer_values_pb2.Transform
    def __init__(self, rms_deviation: _Optional[float] = ..., average_deviation: _Optional[float] = ..., maximum_absolute_deviation: _Optional[float] = ..., resultant_transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class CollimationRequest(_message.Message):
    __slots__ = ("stationary_instrument", "moving_instrument", "collimation_point", "zero_moving_instrument", "tilt_mode", "baseline_method", "baseline_distance", "scale_point_1", "scale_point_2", "not_measured_by_moving_instrument", "as_measured_by_moving_instrument")
    STATIONARY_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MOVING_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COLLIMATION_POINT_FIELD_NUMBER: _ClassVar[int]
    ZERO_MOVING_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TILT_MODE_FIELD_NUMBER: _ClassVar[int]
    BASELINE_METHOD_FIELD_NUMBER: _ClassVar[int]
    BASELINE_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    SCALE_POINT_1_FIELD_NUMBER: _ClassVar[int]
    SCALE_POINT_2_FIELD_NUMBER: _ClassVar[int]
    NOT_MEASURED_BY_MOVING_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    AS_MEASURED_BY_MOVING_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    stationary_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    moving_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    collimation_point: _spatial_analyzer_values_pb2.PointName
    zero_moving_instrument: bool
    tilt_mode: CollimationTiltMode
    baseline_method: CollimationBaselineMethod
    baseline_distance: float
    scale_point_1: _spatial_analyzer_values_pb2.PointName
    scale_point_2: _spatial_analyzer_values_pb2.PointName
    not_measured_by_moving_instrument: _spatial_analyzer_values_pb2.PointName
    as_measured_by_moving_instrument: _spatial_analyzer_values_pb2.PointName
    def __init__(self, stationary_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., moving_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., collimation_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., zero_moving_instrument: bool = ..., tilt_mode: _Optional[_Union[CollimationTiltMode, str]] = ..., baseline_method: _Optional[_Union[CollimationBaselineMethod, str]] = ..., baseline_distance: _Optional[float] = ..., scale_point_1: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., scale_point_2: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., not_measured_by_moving_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., as_measured_by_moving_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class CollimationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CombinePointGroupsRequest(_message.Message):
    __slots__ = ("groups_to_combine", "combined_point_group")
    GROUPS_TO_COMBINE_FIELD_NUMBER: _ClassVar[int]
    COMBINED_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    groups_to_combine: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    combined_point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, groups_to_combine: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., combined_point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class CombinePointGroupsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ComputeCteScaleFactorRequest(_message.Message):
    __slots__ = ("material_cte", "initial_temperature", "final_temperature")
    MATERIAL_CTE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    FINAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    material_cte: float
    initial_temperature: float
    final_temperature: float
    def __init__(self, material_cte: _Optional[float] = ..., initial_temperature: _Optional[float] = ..., final_temperature: _Optional[float] = ...) -> None: ...

class ComputeCteScaleFactorResult(_message.Message):
    __slots__ = ("scale_factor", "execution")
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    scale_factor: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, scale_factor: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConfigureAndMeasureRequest(_message.Message):
    __slots__ = ("instrument", "target", "measurement_mode", "measure_immediately", "wait_for_completion", "timeout_seconds")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    MEASURE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    target: _spatial_analyzer_values_pb2.PointName
    measurement_mode: str
    measure_immediately: bool
    wait_for_completion: bool
    timeout_seconds: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., target: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., measurement_mode: _Optional[str] = ..., measure_immediately: bool = ..., wait_for_completion: bool = ..., timeout_seconds: _Optional[float] = ...) -> None: ...

class ConfigureAndMeasureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructMeasuredPointUncertaintyEllipsoidsRequest(_message.Message):
    __slots__ = ("measurements",)
    MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    measurements: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, measurements: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class ConstructMeasuredPointUncertaintyEllipsoidsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructMirrorFromPlaneRequest(_message.Message):
    __slots__ = ("instrument", "mirror_name", "plane")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MIRROR_NAME_FIELD_NUMBER: _ClassVar[int]
    PLANE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    mirror_name: str
    plane: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., mirror_name: _Optional[str] = ..., plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ConstructMirrorFromPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructMirrorFromTwoPointsRequest(_message.Message):
    __slots__ = ("instrument", "mirror_name", "point_measured_directly", "point_measured_through_mirror", "send_mirror_to_instrument")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MIRROR_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_MEASURED_DIRECTLY_FIELD_NUMBER: _ClassVar[int]
    POINT_MEASURED_THROUGH_MIRROR_FIELD_NUMBER: _ClassVar[int]
    SEND_MIRROR_TO_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    mirror_name: str
    point_measured_directly: _spatial_analyzer_values_pb2.PointName
    point_measured_through_mirror: _spatial_analyzer_values_pb2.PointName
    send_mirror_to_instrument: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., mirror_name: _Optional[str] = ..., point_measured_directly: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., point_measured_through_mirror: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., send_mirror_to_instrument: bool = ...) -> None: ...

class ConstructMirrorFromTwoPointsResult(_message.Message):
    __slots__ = ("mirror_plane", "execution")
    MIRROR_PLANE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    mirror_plane: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, mirror_plane: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructPerimetersFromSurfaceFaceListRequest(_message.Message):
    __slots__ = ("surface_faces",)
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    def __init__(self, surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ...) -> None: ...

class ConstructPerimetersFromSurfaceFaceListResult(_message.Message):
    __slots__ = ("perimeters", "execution")
    PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    perimeters: PerimeterLists
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, perimeters: _Optional[_Union[PerimeterLists, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConstructTcpFixtureRequest(_message.Message):
    __slots__ = ("requested_tcp_fixture", "point_match_threshold", "replace_existing_tcp_fixture")
    REQUESTED_TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    POINT_MATCH_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    requested_tcp_fixture: _spatial_analyzer_values_pb2.CollectionObjectName
    point_match_threshold: float
    replace_existing_tcp_fixture: bool
    def __init__(self, requested_tcp_fixture: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_match_threshold: _Optional[float] = ..., replace_existing_tcp_fixture: bool = ...) -> None: ...

class ConstructTcpFixtureResult(_message.Message):
    __slots__ = ("resulting_tcp_fixture", "execution")
    RESULTING_TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resulting_tcp_fixture: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resulting_tcp_fixture: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateNewDynamicReferenceRequest(_message.Message):
    __slots__ = ("instrument", "points_defining_dynamic_reference", "dynamic_reference_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINTS_DEFINING_DYNAMIC_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_REFERENCE_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    points_defining_dynamic_reference: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    dynamic_reference_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., points_defining_dynamic_reference: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., dynamic_reference_name: _Optional[str] = ...) -> None: ...

class CreateNewDynamicReferenceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateTemplatedInstrumentUsmnRequest(_message.Message):
    __slots__ = ("instrument_template_name", "instrument", "overall_instrument_weight", "moving", "enable_x", "enable_y", "enable_z", "enable_rx", "enable_ry", "enable_rz", "enable_scale", "enable_component_weights", "component_1_weight", "component_2_weight", "component_3_weight")
    INSTRUMENT_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OVERALL_INSTRUMENT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    MOVING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_X_FIELD_NUMBER: _ClassVar[int]
    ENABLE_Y_FIELD_NUMBER: _ClassVar[int]
    ENABLE_Z_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RX_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RY_FIELD_NUMBER: _ClassVar[int]
    ENABLE_RZ_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SCALE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_COMPONENT_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_1_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_2_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    COMPONENT_3_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument_template_name: _spatial_analyzer_values_pb2.CollectionObjectName
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    overall_instrument_weight: float
    moving: bool
    enable_x: bool
    enable_y: bool
    enable_z: bool
    enable_rx: bool
    enable_ry: bool
    enable_rz: bool
    enable_scale: bool
    enable_component_weights: bool
    component_1_weight: float
    component_2_weight: float
    component_3_weight: float
    def __init__(self, instrument_template_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., overall_instrument_weight: _Optional[float] = ..., moving: bool = ..., enable_x: bool = ..., enable_y: bool = ..., enable_z: bool = ..., enable_rx: bool = ..., enable_ry: bool = ..., enable_rz: bool = ..., enable_scale: bool = ..., enable_component_weights: bool = ..., component_1_weight: _Optional[float] = ..., component_2_weight: _Optional[float] = ..., component_3_weight: _Optional[float] = ...) -> None: ...

class CreateTemplatedInstrumentUsmnResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CurrentTrappingStatus(_message.Message):
    __slots__ = ("active", "focused_item", "instrument")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FOCUSED_ITEM_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    active: bool
    focused_item: _spatial_analyzer_values_pb2.CollectionItemName
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, active: bool = ..., focused_item: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class DeleteInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "prompt_user_to_confirm", "keep_resulting_points")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROMPT_USER_TO_CONFIRM_FIELD_NUMBER: _ClassVar[int]
    KEEP_RESULTING_POINTS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    prompt_user_to_confirm: bool
    keep_resulting_points: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., prompt_user_to_confirm: bool = ..., keep_resulting_points: bool = ...) -> None: ...

class DeleteInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteMeasurementObservationRequest(_message.Message):
    __slots__ = ("point_name", "observation_index", "delete_point_if_no_measurements_remain")
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    DELETE_POINT_IF_NO_MEASUREMENTS_REMAIN_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    delete_point_if_no_measurements_remain: bool
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., delete_point_if_no_measurements_remain: bool = ...) -> None: ...

class DeleteMeasurementObservationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteMeasurementsRequest(_message.Message):
    __slots__ = ("instrument", "point_name", "delete_point_if_no_measurements_remain")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    DELETE_POINT_IF_NO_MEASUREMENTS_REMAIN_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    point_name: _spatial_analyzer_values_pb2.PointName
    delete_point_if_no_measurements_remain: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., delete_point_if_no_measurements_remain: bool = ...) -> None: ...

class DeleteMeasurementsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DisassociateObjectsFromInstrumentRequest(_message.Message):
    __slots__ = ("objects",)
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class DisassociateObjectsFromInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DissectPointGroupRequest(_message.Message):
    __slots__ = ("group_to_dissect", "base_name_for_dissected_groups")
    GROUP_TO_DISSECT_FIELD_NUMBER: _ClassVar[int]
    BASE_NAME_FOR_DISSECTED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    group_to_dissect: _spatial_analyzer_values_pb2.CollectionObjectName
    base_name_for_dissected_groups: str
    def __init__(self, group_to_dissect: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., base_name_for_dissected_groups: _Optional[str] = ...) -> None: ...

class DissectPointGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DockInstrumentInterfaceRequest(_message.Message):
    __slots__ = ("instrument", "dock_interface")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    DOCK_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    dock_interface: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., dock_interface: bool = ...) -> None: ...

class DockInstrumentInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DoubleVector6(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class DriftCheckRequest(_message.Message):
    __slots__ = ("instrument", "reference_group", "actuals_group", "tolerance", "minimum_point_count", "use_closest_reference_point")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTUALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_POINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    USE_CLOSEST_REFERENCE_POINT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    actuals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    tolerance: float
    minimum_point_count: int
    use_closest_reference_point: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actuals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., tolerance: _Optional[float] = ..., minimum_point_count: _Optional[int] = ..., use_closest_reference_point: bool = ...) -> None: ...

class DriftCheckResult(_message.Message):
    __slots__ = ("maximum_error", "rms_error", "instrument_added", "new_instrument", "execution")
    MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ADDED_FIELD_NUMBER: _ClassVar[int]
    NEW_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    maximum_error: float
    rms_error: float
    instrument_added: bool
    new_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, maximum_error: _Optional[float] = ..., rms_error: _Optional[float] = ..., instrument_added: bool = ..., new_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EdgeScanMeasurementRequest(_message.Message):
    __slots__ = ("instrument", "point_near_edge", "edge_search_direction_point", "parameter_set_name", "point_group", "target_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_NEAR_EDGE_FIELD_NUMBER: _ClassVar[int]
    EDGE_SEARCH_DIRECTION_POINT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    point_near_edge: _spatial_analyzer_values_pb2.PointName
    edge_search_direction_point: _spatial_analyzer_values_pb2.PointName
    parameter_set_name: str
    point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    target_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., point_near_edge: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., edge_search_direction_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., parameter_set_name: _Optional[str] = ..., point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., target_name: _Optional[str] = ...) -> None: ...

class EdgeScanMeasurementResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EditScanPerimeterProfileRequest(_message.Message):
    __slots__ = ("instrument", "scan_perimeters", "exclusion_perimeters", "parameter_set_name", "profile_name", "clear_profile", "create_new_profile")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PROFILE_FIELD_NUMBER: _ClassVar[int]
    CREATE_NEW_PROFILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    exclusion_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    parameter_set_name: str
    profile_name: str
    clear_profile: bool
    create_new_profile: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., exclusion_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., parameter_set_name: _Optional[str] = ..., profile_name: _Optional[str] = ..., clear_profile: bool = ..., create_new_profile: bool = ...) -> None: ...

class EditScanPerimeterProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableFrameSetScanModeAllInstrumentsRequest(_message.Message):
    __slots__ = ("enable_frame_set_scan_mode",)
    ENABLE_FRAME_SET_SCAN_MODE_FIELD_NUMBER: _ClassVar[int]
    enable_frame_set_scan_mode: bool
    def __init__(self, enable_frame_set_scan_mode: bool = ...) -> None: ...

class EnableDisableFrameSetScanModeAllInstrumentsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableFrameSetScanModeByInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "enable_frame_set_scan_mode")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FRAME_SET_SCAN_MODE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    enable_frame_set_scan_mode: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., enable_frame_set_scan_mode: bool = ...) -> None: ...

class EnableDisableFrameSetScanModeByInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisablePointSetScanModeRequest(_message.Message):
    __slots__ = ("instrument", "enable_point_set_scan_mode")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_POINT_SET_SCAN_MODE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    enable_point_set_scan_mode: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., enable_point_set_scan_mode: bool = ...) -> None: ...

class EnableDisablePointSetScanModeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportInstrumentHistoryToXmlFileRequest(_message.Message):
    __slots__ = ("instrument", "file_path")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportInstrumentHistoryToXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FabricateObservationsRequest(_message.Message):
    __slots__ = ("instrument", "point_group", "introduce_instrument_error", "limit_distance", "minimum_distance", "maximum_distance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INTRODUCE_INSTRUMENT_ERROR_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    introduce_instrument_error: bool
    limit_distance: bool
    minimum_distance: float
    maximum_distance: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., introduce_instrument_error: bool = ..., limit_distance: bool = ..., minimum_distance: _Optional[float] = ..., maximum_distance: _Optional[float] = ...) -> None: ...

class FabricateObservationsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCurrentInstrumentPositionUpdateRequest(_message.Message):
    __slots__ = ("instrument", "reporting_frame", "polar_coordinates")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REPORTING_FRAME_FIELD_NUMBER: _ClassVar[int]
    POLAR_COORDINATES_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reporting_frame: InstrumentPositionReportingFrame
    polar_coordinates: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reporting_frame: _Optional[_Union[InstrumentPositionReportingFrame, str]] = ..., polar_coordinates: bool = ...) -> None: ...

class GetCurrentInstrumentPositionUpdateResult(_message.Message):
    __slots__ = ("x_or_r", "y_or_theta", "z_or_phi", "time_since_update", "timestamp", "execution")
    X_OR_R_FIELD_NUMBER: _ClassVar[int]
    Y_OR_THETA_FIELD_NUMBER: _ClassVar[int]
    Z_OR_PHI_FIELD_NUMBER: _ClassVar[int]
    TIME_SINCE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x_or_r: float
    y_or_theta: float
    z_or_phi: float
    time_since_update: float
    timestamp: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x_or_r: _Optional[float] = ..., y_or_theta: _Optional[float] = ..., z_or_phi: _Optional[float] = ..., time_since_update: _Optional[float] = ..., timestamp: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCurrentTrappingStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCurrentTrappingStatusResult(_message.Message):
    __slots__ = ("status", "execution")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    status: CurrentTrappingStatus
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, status: _Optional[_Union[CurrentTrappingStatus, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetEstimatedScanTimeRequest(_message.Message):
    __slots__ = ("instrument", "profile_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    profile_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., profile_name: _Optional[str] = ...) -> None: ...

class GetEstimatedScanTimeResult(_message.Message):
    __slots__ = ("estimated_scan_time", "execution")
    ESTIMATED_SCAN_TIME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    estimated_scan_time: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, estimated_scan_time: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInspectionVerificationModeRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetInspectionVerificationModeResult(_message.Message):
    __slots__ = ("verification_enabled", "execution")
    VERIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    verification_enabled: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, verification_enabled: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentBaseUncertaintyCovarianceMatrixWrtWorldRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentBaseUncertaintyCovarianceMatrixWrtWorldResult(_message.Message):
    __slots__ = ("covariance_matrix", "execution")
    COVARIANCE_MATRIX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    covariance_matrix: UncertaintyCovarianceMatrix
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, covariance_matrix: _Optional[_Union[UncertaintyCovarianceMatrix, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentGroupAndTargetRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentGroupAndTargetResult(_message.Message):
    __slots__ = ("point", "execution")
    POINT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentIdFromNameRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetInstrumentIdFromNameResult(_message.Message):
    __slots__ = ("instrument", "execution")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentInterfaceResponseTimeoutRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentInterfaceResponseTimeoutResult(_message.Message):
    __slots__ = ("timeout", "execution")
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    timeout: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, timeout: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentMeasurementModeProfileRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentMeasurementModeProfileResult(_message.Message):
    __slots__ = ("mode_profile", "execution")
    MODE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    mode_profile: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, mode_profile: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentModelRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentModelResult(_message.Message):
    __slots__ = ("name", "model", "execution")
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    model: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, name: _Optional[str] = ..., model: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentPartTemperatureRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentPartTemperatureResult(_message.Message):
    __slots__ = ("part_temperature", "execution")
    PART_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    part_temperature: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, part_temperature: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentScaleFactorRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentScaleFactorResult(_message.Message):
    __slots__ = ("scale_factor", "execution")
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    scale_factor: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, scale_factor: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentsWithObservationsOnTargetRequest(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetInstrumentsWithObservationsOnTargetResult(_message.Message):
    __slots__ = ("instruments", "execution")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetingRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetingResult(_message.Message):
    __slots__ = ("targeting_name", "execution")
    TARGETING_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    targeting_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, targeting_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetsAndModeProfilesRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetsAndModeProfilesResult(_message.Message):
    __slots__ = ("mode_profiles", "target_names", "execution")
    MODE_PROFILES_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAMES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    mode_profiles: _containers.RepeatedScalarFieldContainer[str]
    target_names: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, mode_profiles: _Optional[_Iterable[str]] = ..., target_names: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetStatusRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentTargetStatusResult(_message.Message):
    __slots__ = ("status", "execution")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    status: InstrumentTargetStatus
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, status: _Optional[_Union[InstrumentTargetStatus, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentTransformRequest(_message.Message):
    __slots__ = ("instrument", "reference_frame")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetInstrumentTransformResult(_message.Message):
    __slots__ = ("transform", "execution")
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetInstrumentWeatherSettingRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetInstrumentWeatherSettingResult(_message.Message):
    __slots__ = ("temperature", "pressure", "relative_humidity", "set_automatically", "execution")
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    SET_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    temperature: float
    pressure: float
    relative_humidity: float
    set_automatically: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., relative_humidity: _Optional[float] = ..., set_automatically: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetLastInstrumentIndexRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetLastInstrumentIndexResult(_message.Message):
    __slots__ = ("instrument_index", "instrument", "execution")
    INSTRUMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instrument_index: int
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instrument_index: _Optional[int] = ..., instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetLastSolvedTcpFixtureUncertaintyCovarianceMatrixRequest(_message.Message):
    __slots__ = ("tcp_fixture",)
    TCP_FIXTURE_FIELD_NUMBER: _ClassVar[int]
    tcp_fixture: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, tcp_fixture: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetLastSolvedTcpFixtureUncertaintyCovarianceMatrixResult(_message.Message):
    __slots__ = ("covariance_matrix", "execution")
    COVARIANCE_MATRIX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    covariance_matrix: UncertaintyCovarianceMatrix
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, covariance_matrix: _Optional[_Union[UncertaintyCovarianceMatrix, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfObservationsOnTargetRequest(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetNumberOfObservationsOnTargetResult(_message.Message):
    __slots__ = ("observation_count", "execution")
    OBSERVATION_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    observation_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, observation_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetObscuredPointsFromInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "candidate_points", "show_obscured_shots")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_POINTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_OBSCURED_SHOTS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    candidate_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    show_obscured_shots: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., candidate_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., show_obscured_shots: bool = ...) -> None: ...

class GetObscuredPointsFromInstrumentResult(_message.Message):
    __slots__ = ("obscured_points", "execution")
    OBSCURED_POINTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    obscured_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, obscured_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetObservationInfoRequest(_message.Message):
    __slots__ = ("point", "observation_index")
    POINT_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ...) -> None: ...

class GetObservationInfoResult(_message.Message):
    __slots__ = ("observation", "execution")
    OBSERVATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    observation: ObservationInfo
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, observation: _Optional[_Union[ObservationInfo, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPcmmInstrumentXyzUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetPcmmInstrumentXyzUncertaintiesResult(_message.Message):
    __slots__ = ("x_uncertainty", "y_uncertainty", "z_uncertainty", "execution")
    X_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Y_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Z_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x_uncertainty: float
    y_uncertainty: float
    z_uncertainty: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x_uncertainty: _Optional[float] = ..., y_uncertainty: _Optional[float] = ..., z_uncertainty: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTargetsMeasuredByInstrumentRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetTargetsMeasuredByInstrumentResult(_message.Message):
    __slots__ = ("targets", "execution")
    TARGETS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, targets: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTrackerEdmTheodoliteUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetTrackerEdmTheodoliteUncertaintiesResult(_message.Message):
    __slots__ = ("theta_dispersion", "theta_threshold", "phi_dispersion", "phi_threshold", "distance", "distance_threshold", "execution")
    THETA_DISPERSION_FIELD_NUMBER: _ClassVar[int]
    THETA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PHI_DISPERSION_FIELD_NUMBER: _ClassVar[int]
    PHI_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    theta_dispersion: float
    theta_threshold: float
    phi_dispersion: float
    phi_threshold: float
    distance: float
    distance_threshold: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, theta_dispersion: _Optional[float] = ..., theta_threshold: _Optional[float] = ..., phi_dispersion: _Optional[float] = ..., phi_threshold: _Optional[float] = ..., distance: _Optional[float] = ..., distance_threshold: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetWrtlChannelAndStatusRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetWrtlChannelAndStatusResult(_message.Message):
    __slots__ = ("status", "execution")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    status: WrtlChannelStatus
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, status: _Optional[_Union[WrtlChannelStatus, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetXyzInstrumentUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class GetXyzInstrumentUncertaintiesResult(_message.Message):
    __slots__ = ("x_uncertainty", "y_uncertainty", "z_uncertainty", "execution")
    X_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Y_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Z_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    x_uncertainty: float
    y_uncertainty: float
    z_uncertainty: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, x_uncertainty: _Optional[float] = ..., y_uncertainty: _Optional[float] = ..., z_uncertainty: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GuideObjectsIn6dBasedOnPointMeasurementsRequest(_message.Message):
    __slots__ = ("instrument", "destination_group", "moving_reference_group", "objects_to_move", "initial_survey_group", "positional_tolerance", "rotational_tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    MOVING_REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_SURVEY_GROUP_FIELD_NUMBER: _ClassVar[int]
    POSITIONAL_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    ROTATIONAL_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    destination_group: _spatial_analyzer_values_pb2.CollectionObjectName
    moving_reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    objects_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    initial_survey_group: _spatial_analyzer_values_pb2.CollectionObjectName
    positional_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    rotational_tolerance: _spatial_analyzer_values_pb2.ToleranceVectorOptions
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., destination_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., moving_reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., objects_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., initial_survey_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., positional_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ..., rotational_tolerance: _Optional[_Union[_spatial_analyzer_values_pb2.ToleranceVectorOptions, _Mapping]] = ...) -> None: ...

class GuideObjectsIn6dBasedOnPointMeasurementsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class InitiateServoGuideRequest(_message.Message):
    __slots__ = ("instrument", "nominal_points", "group_name_suffix", "target_name_suffix", "tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    nominal_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    group_name_suffix: str
    target_name_suffix: str
    tolerance: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., nominal_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., group_name_suffix: _Optional[str] = ..., target_name_suffix: _Optional[str] = ..., tolerance: _Optional[float] = ...) -> None: ...

class InitiateServoGuideResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class InstrumentOperationalCheckRequest(_message.Message):
    __slots__ = ("instrument", "check_type")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CHECK_TYPE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    check_type: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., check_type: _Optional[str] = ...) -> None: ...

class InstrumentOperationalCheckResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class InstrumentTargetStatus(_message.Message):
    __slots__ = ("is_locked", "name", "number_of_faces", "locked_face")
    IS_LOCKED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_FACES_FIELD_NUMBER: _ClassVar[int]
    LOCKED_FACE_FIELD_NUMBER: _ClassVar[int]
    is_locked: bool
    name: str
    number_of_faces: int
    locked_face: int
    def __init__(self, is_locked: bool = ..., name: _Optional[str] = ..., number_of_faces: _Optional[int] = ..., locked_face: _Optional[int] = ...) -> None: ...

class InstrumentTypeName(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class IssueInstrumentActuatorCommandRequest(_message.Message):
    __slots__ = ("instrument", "command")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    command: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., command: _Optional[str] = ...) -> None: ...

class IssueInstrumentActuatorCommandResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class JumpInstrumentToNewLocationRequest(_message.Message):
    __slots__ = ("live_instrument", "hide_previous_instrument")
    LIVE_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    HIDE_PREVIOUS_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    live_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    hide_previous_instrument: bool
    def __init__(self, live_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., hide_previous_instrument: bool = ...) -> None: ...

class JumpInstrumentToNewLocationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LoadCloudViewerPointCloudFileRequest(_message.Message):
    __slots__ = ("instrument", "file_path")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    file_path: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., file_path: _Optional[str] = ...) -> None: ...

class LoadCloudViewerPointCloudFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LoadInstrumentConfigurationRequest(_message.Message):
    __slots__ = ("instrument", "configuration_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    configuration_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., configuration_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class LoadInstrumentConfigurationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LocateInstrumentBestFitGroupToGroupRequest(_message.Message):
    __slots__ = ("reference_group", "corresponding_group", "show_interface", "rms_tolerance", "maximum_absolute_tolerance", "allow_scale", "allow_x", "allow_y", "allow_z", "allow_rx", "allow_ry", "allow_rz", "lock_degrees_of_freedom", "generate_event", "csv_report")
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    CORRESPONDING_GROUP_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCALE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_X_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Y_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Z_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RZ_FIELD_NUMBER: _ClassVar[int]
    LOCK_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    GENERATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    CSV_REPORT_FIELD_NUMBER: _ClassVar[int]
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    corresponding_group: _spatial_analyzer_values_pb2.CollectionObjectName
    show_interface: bool
    rms_tolerance: float
    maximum_absolute_tolerance: float
    allow_scale: bool
    allow_x: bool
    allow_y: bool
    allow_z: bool
    allow_rx: bool
    allow_ry: bool
    allow_rz: bool
    lock_degrees_of_freedom: bool
    generate_event: bool
    csv_report: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., corresponding_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., show_interface: bool = ..., rms_tolerance: _Optional[float] = ..., maximum_absolute_tolerance: _Optional[float] = ..., allow_scale: bool = ..., allow_x: bool = ..., allow_y: bool = ..., allow_z: bool = ..., allow_rx: bool = ..., allow_ry: bool = ..., allow_rz: bool = ..., lock_degrees_of_freedom: bool = ..., generate_event: bool = ..., csv_report: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class LocateInstrumentBestFitGroupToGroupResult(_message.Message):
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

class LocateInstrumentBestFitNominalGeometryRequest(_message.Message):
    __slots__ = ("instrument", "geometry_relationships", "show_interface", "rms_tolerance", "maximum_absolute_tolerance", "allow_scale", "allow_x", "allow_y", "allow_z", "allow_rx", "allow_ry", "allow_rz", "lock_degrees_of_freedom", "generate_event", "csv_report")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    GEOMETRY_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SCALE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_X_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Y_FIELD_NUMBER: _ClassVar[int]
    ALLOW_Z_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RX_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RY_FIELD_NUMBER: _ClassVar[int]
    ALLOW_RZ_FIELD_NUMBER: _ClassVar[int]
    LOCK_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    GENERATE_EVENT_FIELD_NUMBER: _ClassVar[int]
    CSV_REPORT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    geometry_relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    show_interface: bool
    rms_tolerance: float
    maximum_absolute_tolerance: float
    allow_scale: bool
    allow_x: bool
    allow_y: bool
    allow_z: bool
    allow_rx: bool
    allow_ry: bool
    allow_rz: bool
    lock_degrees_of_freedom: bool
    generate_event: bool
    csv_report: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., geometry_relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., show_interface: bool = ..., rms_tolerance: _Optional[float] = ..., maximum_absolute_tolerance: _Optional[float] = ..., allow_scale: bool = ..., allow_x: bool = ..., allow_y: bool = ..., allow_z: bool = ..., allow_rx: bool = ..., allow_ry: bool = ..., allow_rz: bool = ..., lock_degrees_of_freedom: bool = ..., generate_event: bool = ..., csv_report: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class LocateInstrumentBestFitNominalGeometryResult(_message.Message):
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

class LocateInstrumentGroupToSurfaceQuickFitRequest(_message.Message):
    __slots__ = ("instrument", "measured_group", "surface_points_group", "surface_to_fit", "other_objects_to_transform", "rms_tolerance", "maximum_absolute_tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MEASURED_GROUP_FIELD_NUMBER: _ClassVar[int]
    SURFACE_POINTS_GROUP_FIELD_NUMBER: _ClassVar[int]
    SURFACE_TO_FIT_FIELD_NUMBER: _ClassVar[int]
    OTHER_OBJECTS_TO_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    RMS_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    measured_group: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_points_group: _spatial_analyzer_values_pb2.CollectionObjectName
    surface_to_fit: _spatial_analyzer_values_pb2.CollectionObjectName
    other_objects_to_transform: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    rms_tolerance: float
    maximum_absolute_tolerance: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., measured_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_points_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., surface_to_fit: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., other_objects_to_transform: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., rms_tolerance: _Optional[float] = ..., maximum_absolute_tolerance: _Optional[float] = ...) -> None: ...

class LocateInstrumentGroupToSurfaceQuickFitResult(_message.Message):
    __slots__ = ("rms_error", "maximum_absolute_error", "execution")
    RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_error: float
    maximum_absolute_error: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_error: _Optional[float] = ..., maximum_absolute_error: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LocateInstrumentRefTieInRequest(_message.Message):
    __slots__ = ("instrument", "reference_group", "actuals_group", "tolerance", "auto_survey")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTUALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    AUTO_SURVEY_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_group: _spatial_analyzer_values_pb2.CollectionObjectName
    actuals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    tolerance: float
    auto_survey: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actuals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., tolerance: _Optional[float] = ..., auto_survey: bool = ...) -> None: ...

class LocateInstrumentRefTieInResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LocateInstrumentsUsmnRequest(_message.Message):
    __slots__ = ("instruments", "nominals_group", "output_group", "move_in_working_frame", "auto_reject_outliers_and_resolve", "show_usmn_dialog", "maximum_acceptable_rms_error", "maximum_acceptable_error", "excluded_groups", "exclude_single_instrument_points", "run_uncertainty_field_analysis", "analysis_samples", "analysis_time_limit")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    NOMINALS_GROUP_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_GROUP_FIELD_NUMBER: _ClassVar[int]
    MOVE_IN_WORKING_FRAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_REJECT_OUTLIERS_AND_RESOLVE_FIELD_NUMBER: _ClassVar[int]
    SHOW_USMN_DIALOG_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ACCEPTABLE_RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ACCEPTABLE_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_GROUPS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_SINGLE_INSTRUMENT_POINTS_FIELD_NUMBER: _ClassVar[int]
    RUN_UNCERTAINTY_FIELD_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_TIME_LIMIT_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    nominals_group: _spatial_analyzer_values_pb2.CollectionObjectName
    output_group: _spatial_analyzer_values_pb2.CollectionObjectName
    move_in_working_frame: bool
    auto_reject_outliers_and_resolve: bool
    show_usmn_dialog: ShowUsmnDialog
    maximum_acceptable_rms_error: float
    maximum_acceptable_error: float
    excluded_groups: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    exclude_single_instrument_points: bool
    run_uncertainty_field_analysis: bool
    analysis_samples: int
    analysis_time_limit: float
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., nominals_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., output_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., move_in_working_frame: bool = ..., auto_reject_outliers_and_resolve: bool = ..., show_usmn_dialog: _Optional[_Union[ShowUsmnDialog, str]] = ..., maximum_acceptable_rms_error: _Optional[float] = ..., maximum_acceptable_error: _Optional[float] = ..., excluded_groups: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., exclude_single_instrument_points: bool = ..., run_uncertainty_field_analysis: bool = ..., analysis_samples: _Optional[int] = ..., analysis_time_limit: _Optional[float] = ...) -> None: ...

class LocateInstrumentsUsmnResult(_message.Message):
    __slots__ = ("rms_error", "maximum_error", "execution")
    RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rms_error: float
    maximum_error: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rms_error: _Optional[float] = ..., maximum_error: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrApdisActivateMcmCalibrationRequest(_message.Message):
    __slots__ = ("instrument", "calibration_name", "calibration_id")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_ID_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    calibration_name: str
    calibration_id: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., calibration_id: _Optional[int] = ...) -> None: ...

class LrApdisActivateMcmCalibrationResult(_message.Message):
    __slots__ = ("active_mcm_name", "execution")
    ACTIVE_MCM_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    active_mcm_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, active_mcm_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrApdisGetActiveMcmCalibrationRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrApdisGetActiveMcmCalibrationResult(_message.Message):
    __slots__ = ("active_mcm_name", "execution")
    ACTIVE_MCM_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    active_mcm_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, active_mcm_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrApdisPerformMcmCalibrationRequest(_message.Message):
    __slots__ = ("instrument", "nominal_group", "use_matte_tooling_ball", "new_calibration_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_GROUP_FIELD_NUMBER: _ClassVar[int]
    USE_MATTE_TOOLING_BALL_FIELD_NUMBER: _ClassVar[int]
    NEW_CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    nominal_group: _spatial_analyzer_values_pb2.CollectionObjectName
    use_matte_tooling_ball: bool
    new_calibration_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., nominal_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_matte_tooling_ball: bool = ..., new_calibration_name: _Optional[str] = ...) -> None: ...

class LrApdisPerformMcmCalibrationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrFlipTestResult(_message.Message):
    __slots__ = ("front_range", "front_azimuth", "front_elevation", "front_quality", "back_range", "back_azimuth", "back_elevation", "back_quality", "front_back_difference_range", "front_back_difference_azimuth", "front_back_difference_elevation")
    FRONT_RANGE_FIELD_NUMBER: _ClassVar[int]
    FRONT_AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    FRONT_ELEVATION_FIELD_NUMBER: _ClassVar[int]
    FRONT_QUALITY_FIELD_NUMBER: _ClassVar[int]
    BACK_RANGE_FIELD_NUMBER: _ClassVar[int]
    BACK_AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    BACK_ELEVATION_FIELD_NUMBER: _ClassVar[int]
    BACK_QUALITY_FIELD_NUMBER: _ClassVar[int]
    FRONT_BACK_DIFFERENCE_RANGE_FIELD_NUMBER: _ClassVar[int]
    FRONT_BACK_DIFFERENCE_AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    FRONT_BACK_DIFFERENCE_ELEVATION_FIELD_NUMBER: _ClassVar[int]
    front_range: float
    front_azimuth: float
    front_elevation: float
    front_quality: float
    back_range: float
    back_azimuth: float
    back_elevation: float
    back_quality: float
    front_back_difference_range: float
    front_back_difference_azimuth: float
    front_back_difference_elevation: float
    def __init__(self, front_range: _Optional[float] = ..., front_azimuth: _Optional[float] = ..., front_elevation: _Optional[float] = ..., front_quality: _Optional[float] = ..., back_range: _Optional[float] = ..., back_azimuth: _Optional[float] = ..., back_elevation: _Optional[float] = ..., back_quality: _Optional[float] = ..., front_back_difference_range: _Optional[float] = ..., front_back_difference_azimuth: _Optional[float] = ..., front_back_difference_elevation: _Optional[float] = ...) -> None: ...

class LrGetMostRecentSnrInfoRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrGetMostRecentSnrInfoResult(_message.Message):
    __slots__ = ("info", "execution")
    INFO_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    info: LrSnrInfo
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, info: _Optional[_Union[LrSnrInfo, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrHardwareConnectRequest(_message.Message):
    __slots__ = ("instrument", "host", "port")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    host: str
    port: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., host: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class LrHardwareConnectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrHardwareDisconnectRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrHardwareDisconnectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrLoSeparationTestResult(_message.Message):
    __slots__ = ("primary_lo", "secondary_lo", "primary_lo_measurement_count", "primary_lo_range_mean", "primary_lo_range_standard_deviation", "primary_lo_quality_mean", "primary_lo_quality_standard_deviation", "secondary_lo_measurement_count", "secondary_lo_range_mean", "secondary_lo_range_standard_deviation", "secondary_lo_quality_mean", "secondary_lo_quality_standard_deviation")
    PRIMARY_LO_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LO_MEASUREMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LO_RANGE_MEAN_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LO_RANGE_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LO_QUALITY_MEAN_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LO_QUALITY_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_MEASUREMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_RANGE_MEAN_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_RANGE_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_QUALITY_MEAN_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_LO_QUALITY_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    primary_lo: int
    secondary_lo: int
    primary_lo_measurement_count: int
    primary_lo_range_mean: float
    primary_lo_range_standard_deviation: float
    primary_lo_quality_mean: float
    primary_lo_quality_standard_deviation: float
    secondary_lo_measurement_count: int
    secondary_lo_range_mean: float
    secondary_lo_range_standard_deviation: float
    secondary_lo_quality_mean: float
    secondary_lo_quality_standard_deviation: float
    def __init__(self, primary_lo: _Optional[int] = ..., secondary_lo: _Optional[int] = ..., primary_lo_measurement_count: _Optional[int] = ..., primary_lo_range_mean: _Optional[float] = ..., primary_lo_range_standard_deviation: _Optional[float] = ..., primary_lo_quality_mean: _Optional[float] = ..., primary_lo_quality_standard_deviation: _Optional[float] = ..., secondary_lo_measurement_count: _Optional[int] = ..., secondary_lo_range_mean: _Optional[float] = ..., secondary_lo_range_standard_deviation: _Optional[float] = ..., secondary_lo_quality_mean: _Optional[float] = ..., secondary_lo_quality_standard_deviation: _Optional[float] = ...) -> None: ...

class LrSelfTestFlipTestRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrSelfTestFlipTestResult(_message.Message):
    __slots__ = ("result", "execution")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    result: LrFlipTestResult
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, result: _Optional[_Union[LrFlipTestResult, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrSelfTestLinearizationRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrSelfTestLinearizationResult(_message.Message):
    __slots__ = ("linearity", "execution")
    LINEARITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    linearity: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, linearity: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrSelfTestLoSepRequest(_message.Message):
    __slots__ = ("instrument", "region", "num_range_measurements")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    NUM_RANGE_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    region: int
    num_range_measurements: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., region: _Optional[int] = ..., num_range_measurements: _Optional[int] = ...) -> None: ...

class LrSelfTestLoSepResult(_message.Message):
    __slots__ = ("result", "execution")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    result: LrLoSeparationTestResult
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, result: _Optional[_Union[LrLoSeparationTestResult, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrSelfTestRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrSelfTestResult(_message.Message):
    __slots__ = ("reference_arm_length", "reference_arm_quality", "mirror_measurement_count", "mirror_measurement_range_mean", "mirror_measurement_range_standard_deviation", "mirror_measurement_quality_mean", "mirror_measurement_quality_standard_deviation", "passed_reference_arm_quality_threshold", "passed_mirror_offset_delta_threshold", "passed_mirror_offset_standard_deviation_threshold", "passed_mirror_mean_quality_threshold", "passed_overall", "execution")
    REFERENCE_ARM_LENGTH_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_ARM_QUALITY_FIELD_NUMBER: _ClassVar[int]
    MIRROR_MEASUREMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIRROR_MEASUREMENT_RANGE_MEAN_FIELD_NUMBER: _ClassVar[int]
    MIRROR_MEASUREMENT_RANGE_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    MIRROR_MEASUREMENT_QUALITY_MEAN_FIELD_NUMBER: _ClassVar[int]
    MIRROR_MEASUREMENT_QUALITY_STANDARD_DEVIATION_FIELD_NUMBER: _ClassVar[int]
    PASSED_REFERENCE_ARM_QUALITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PASSED_MIRROR_OFFSET_DELTA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PASSED_MIRROR_OFFSET_STANDARD_DEVIATION_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PASSED_MIRROR_MEAN_QUALITY_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PASSED_OVERALL_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    reference_arm_length: float
    reference_arm_quality: float
    mirror_measurement_count: int
    mirror_measurement_range_mean: float
    mirror_measurement_range_standard_deviation: float
    mirror_measurement_quality_mean: float
    mirror_measurement_quality_standard_deviation: float
    passed_reference_arm_quality_threshold: bool
    passed_mirror_offset_delta_threshold: bool
    passed_mirror_offset_standard_deviation_threshold: bool
    passed_mirror_mean_quality_threshold: bool
    passed_overall: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, reference_arm_length: _Optional[float] = ..., reference_arm_quality: _Optional[float] = ..., mirror_measurement_count: _Optional[int] = ..., mirror_measurement_range_mean: _Optional[float] = ..., mirror_measurement_range_standard_deviation: _Optional[float] = ..., mirror_measurement_quality_mean: _Optional[float] = ..., mirror_measurement_quality_standard_deviation: _Optional[float] = ..., passed_reference_arm_quality_threshold: bool = ..., passed_mirror_offset_delta_threshold: bool = ..., passed_mirror_offset_standard_deviation_threshold: bool = ..., passed_mirror_mean_quality_threshold: bool = ..., passed_overall: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrSetRedLaserIntensityRequest(_message.Message):
    __slots__ = ("instrument", "intensity")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    intensity: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., intensity: _Optional[int] = ...) -> None: ...

class LrSetRedLaserIntensityResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LrSnrInfo(_message.Message):
    __slots__ = ("snr", "size_of_data_array", "peak_value_index", "peak_value", "measured_range")
    SNR_FIELD_NUMBER: _ClassVar[int]
    SIZE_OF_DATA_ARRAY_FIELD_NUMBER: _ClassVar[int]
    PEAK_VALUE_INDEX_FIELD_NUMBER: _ClassVar[int]
    PEAK_VALUE_FIELD_NUMBER: _ClassVar[int]
    MEASURED_RANGE_FIELD_NUMBER: _ClassVar[int]
    snr: float
    size_of_data_array: int
    peak_value_index: int
    peak_value: float
    measured_range: float
    def __init__(self, snr: _Optional[float] = ..., size_of_data_array: _Optional[int] = ..., peak_value_index: _Optional[int] = ..., peak_value: _Optional[float] = ..., measured_range: _Optional[float] = ...) -> None: ...

class LrVerifyHardwareConnectionRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class LrVerifyHardwareConnectionResult(_message.Message):
    __slots__ = ("connected_to_hardware", "execution")
    CONNECTED_TO_HARDWARE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    connected_to_hardware: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, connected_to_hardware: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCollectionObjectNameRefListFromObjectsAssociatedWithInstrumentsRequest(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ...) -> None: ...

class MakeCollectionObjectNameRefListFromObjectsAssociatedWithInstrumentsResult(_message.Message):
    __slots__ = ("objects", "execution")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeSurfaceFaceListFromPointProximityRequest(_message.Message):
    __slots__ = ("measured_points",)
    MEASURED_POINTS_FIELD_NUMBER: _ClassVar[int]
    measured_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, measured_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class MakeSurfaceFaceListFromPointProximityResult(_message.Message):
    __slots__ = ("surface_faces", "execution")
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureExistingSinglePointAndCompareRequest(_message.Message):
    __slots__ = ("instrument", "existing_target_id", "group_name_for_new_point", "measure_immediately", "html_prompt_file", "tolerance")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FOR_NEW_POINT_FIELD_NUMBER: _ClassVar[int]
    MEASURE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    existing_target_id: _spatial_analyzer_values_pb2.PointName
    group_name_for_new_point: _spatial_analyzer_values_pb2.CollectionObjectName
    measure_immediately: bool
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    tolerance: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., existing_target_id: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., group_name_for_new_point: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measure_immediately: bool = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., tolerance: _Optional[float] = ...) -> None: ...

class MeasureExistingSinglePointAndCompareResult(_message.Message):
    __slots__ = ("vector_representation", "x_value", "y_value", "z_value", "magnitude", "resulting_point_name", "execution")
    VECTOR_REPRESENTATION_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    Z_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_representation: _spatial_analyzer_values_pb2.Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_representation: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ..., z_value: _Optional[float] = ..., magnitude: _Optional[float] = ..., resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureExistingSinglePointManualGuideRequest(_message.Message):
    __slots__ = ("instrument", "existing_target_id", "group_name_for_new_point", "measure_immediately", "html_prompt_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FOR_NEW_POINT_FIELD_NUMBER: _ClassVar[int]
    MEASURE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    existing_target_id: _spatial_analyzer_values_pb2.PointName
    group_name_for_new_point: _spatial_analyzer_values_pb2.CollectionObjectName
    measure_immediately: bool
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., existing_target_id: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., group_name_for_new_point: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measure_immediately: bool = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class MeasureExistingSinglePointManualGuideResult(_message.Message):
    __slots__ = ("resulting_point_name", "execution")
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureExistingSinglePointRequest(_message.Message):
    __slots__ = ("instrument", "existing_target_id", "group_name_for_new_point", "measure_immediately", "html_prompt_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    EXISTING_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FOR_NEW_POINT_FIELD_NUMBER: _ClassVar[int]
    MEASURE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    existing_target_id: _spatial_analyzer_values_pb2.PointName
    group_name_for_new_point: _spatial_analyzer_values_pb2.CollectionObjectName
    measure_immediately: bool
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., existing_target_id: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., group_name_for_new_point: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measure_immediately: bool = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class MeasureExistingSinglePointResult(_message.Message):
    __slots__ = ("resulting_point_name", "execution")
    RESULTING_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resulting_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resulting_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureNominalFeatureRequest(_message.Message):
    __slots__ = ("instrument", "feature", "resulting_point")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    RESULTING_POINT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    feature: _spatial_analyzer_values_pb2.CollectionObjectName
    resulting_point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., feature: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., resulting_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class MeasureNominalFeatureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class MeasureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MeasureSinglePointHereRequest(_message.Message):
    __slots__ = ("instrument", "target_id", "measure_immediately", "html_prompt_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    MEASURE_IMMEDIATELY_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    target_id: _spatial_analyzer_values_pb2.PointName
    measure_immediately: bool
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., target_id: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., measure_immediately: bool = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class MeasureSinglePointHereResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveInstrumentToAnotherCollectionRequest(_message.Message):
    __slots__ = ("instrument", "collection_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class MoveInstrumentToAnotherCollectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveMeasurementObservationRequest(_message.Message):
    __slots__ = ("source_point_name", "observation_index", "delete_point_if_no_measurements_remain", "destination_point_name", "force_observation_active")
    SOURCE_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    DELETE_POINT_IF_NO_MEASUREMENTS_REMAIN_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_OBSERVATION_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    source_point_name: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    delete_point_if_no_measurements_remain: bool
    destination_point_name: _spatial_analyzer_values_pb2.PointName
    force_observation_active: bool
    def __init__(self, source_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., delete_point_if_no_measurements_remain: bool = ..., destination_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., force_observation_active: bool = ...) -> None: ...

class MoveMeasurementObservationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveObjectsIn6dUsingInstrumentUpdatesRequest(_message.Message):
    __slots__ = ("instrument", "objects_to_move", "measurement_mode")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_MOVE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    objects_to_move: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    measurement_mode: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., objects_to_move: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., measurement_mode: _Optional[str] = ...) -> None: ...

class MoveObjectsIn6dUsingInstrumentUpdatesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MultiMeasurementInitiateRequest(_message.Message):
    __slots__ = ("instruments", "measurement_mode", "wait_for_completion")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    measurement_mode: str
    wait_for_completion: bool
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., measurement_mode: _Optional[str] = ..., wait_for_completion: bool = ...) -> None: ...

class MultiMeasurementInitiateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MultiMeasurementStopRequest(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ...) -> None: ...

class MultiMeasurementStopResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ObservationInfo(_message.Message):
    __slots__ = ("instrument", "spherical_values", "active", "timestamp", "rms_error", "temperature", "pressure", "relative_humidity", "info_data")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SPHERICAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    INFO_DATA_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    spherical_values: ObservationSphericalValues
    active: bool
    timestamp: str
    rms_error: float
    temperature: float
    pressure: float
    relative_humidity: float
    info_data: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., spherical_values: _Optional[_Union[ObservationSphericalValues, _Mapping]] = ..., active: bool = ..., timestamp: _Optional[str] = ..., rms_error: _Optional[float] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., relative_humidity: _Optional[float] = ..., info_data: _Optional[str] = ...) -> None: ...

class ObservationSphericalValues(_message.Message):
    __slots__ = ("distance", "azimuth", "elevation")
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    AZIMUTH_FIELD_NUMBER: _ClassVar[int]
    ELEVATION_FIELD_NUMBER: _ClassVar[int]
    distance: float
    azimuth: float
    elevation: float
    def __init__(self, distance: _Optional[float] = ..., azimuth: _Optional[float] = ..., elevation: _Optional[float] = ...) -> None: ...

class PerimeterLists(_message.Message):
    __slots__ = ("scan_perimeters", "exclusion_perimeters")
    SCAN_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    scan_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    exclusion_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, scan_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., exclusion_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class PointAtTargetRequest(_message.Message):
    __slots__ = ("instrument", "target_id", "html_prompt_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    HTML_PROMPT_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    target_id: _spatial_analyzer_values_pb2.PointName
    html_prompt_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., target_id: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., html_prompt_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class PointAtTargetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ProjectObjectsRequest(_message.Message):
    __slots__ = ("instrument", "objects_to_project")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_PROJECT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    objects_to_project: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., objects_to_project: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ProjectObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QuickAlignRequest(_message.Message):
    __slots__ = ("instruments", "objects", "nominal_points", "nominal_point_of_view_names", "align_to_individual_faces_only")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINTS_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_POINT_OF_VIEW_NAMES_FIELD_NUMBER: _ClassVar[int]
    ALIGN_TO_INDIVIDUAL_FACES_ONLY_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    nominal_points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    nominal_point_of_view_names: _containers.RepeatedScalarFieldContainer[str]
    align_to_individual_faces_only: bool
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., nominal_points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., nominal_point_of_view_names: _Optional[_Iterable[str]] = ..., align_to_individual_faces_only: bool = ...) -> None: ...

class QuickAlignResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "new_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    new_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., new_name: _Optional[str] = ...) -> None: ...

class RenameInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RunCribSheetRequest(_message.Message):
    __slots__ = ("collection", "crib_sheet_name", "instrument")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    CRIB_SHEET_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    crib_sheet_name: str
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., crib_sheet_name: _Optional[str] = ..., instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class RunCribSheetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveCloudViewerPointCloudFileRequest(_message.Message):
    __slots__ = ("instrument", "file_path", "save_as_ascii")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SAVE_AS_ASCII_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    file_path: str
    save_as_ascii: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., file_path: _Optional[str] = ..., save_as_ascii: bool = ...) -> None: ...

class SaveCloudViewerPointCloudFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveInstrumentConfigurationRequest(_message.Message):
    __slots__ = ("instrument", "configuration_file")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    configuration_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., configuration_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SaveInstrumentConfigurationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ScanCadFacesRequest(_message.Message):
    __slots__ = ("instrument", "surface_faces", "parameter_set_name", "enable_exclusions", "wait_for_completion")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SURFACE_FACES_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    surface_faces: _spatial_analyzer_values_pb2.SurfaceFaceList
    parameter_set_name: str
    enable_exclusions: bool
    wait_for_completion: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., surface_faces: _Optional[_Union[_spatial_analyzer_values_pb2.SurfaceFaceList, _Mapping]] = ..., parameter_set_name: _Optional[str] = ..., enable_exclusions: bool = ..., wait_for_completion: bool = ...) -> None: ...

class ScanCadFacesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ScanWithinPerimeterRequest(_message.Message):
    __slots__ = ("instrument", "scan_perimeters", "exclusion_perimeters", "parameter_set_name", "point_group", "wait_for_completion")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUSION_PERIMETERS_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    exclusion_perimeters: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    parameter_set_name: str
    point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    wait_for_completion: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., exclusion_perimeters: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., parameter_set_name: _Optional[str] = ..., point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., wait_for_completion: bool = ...) -> None: ...

class ScanWithinPerimeterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SendCloudToSaRequest(_message.Message):
    __slots__ = ("instrument", "cloud_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    cloud_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., cloud_name: _Optional[str] = ...) -> None: ...

class SendCloudToSaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAbsoluteInstrumentScaleFactorRequest(_message.Message):
    __slots__ = ("instrument", "scale_factor")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scale_factor: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scale_factor: _Optional[float] = ...) -> None: ...

class SetAbsoluteInstrumentScaleFactorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAlignmentProjectorRequest(_message.Message):
    __slots__ = ("instrument", "projector_profile", "user_prompt")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROJECTOR_PROFILE_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    projector_profile: str
    user_prompt: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., projector_profile: _Optional[str] = ..., user_prompt: _Optional[str] = ...) -> None: ...

class SetAlignmentProjectorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCloudViewerFilterRequest(_message.Message):
    __slots__ = ("instrument", "filter_value")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_VALUE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    filter_value: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., filter_value: _Optional[int] = ...) -> None: ...

class SetCloudViewerFilterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInspectionVerificationModeRequest(_message.Message):
    __slots__ = ("verification_enabled",)
    VERIFICATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    verification_enabled: bool
    def __init__(self, verification_enabled: bool = ...) -> None: ...

class SetInspectionVerificationModeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentAxesRequest(_message.Message):
    __slots__ = ("instrument_to_adjust", "axis_values", "number_of_steps")
    INSTRUMENT_TO_ADJUST_FIELD_NUMBER: _ClassVar[int]
    AXIS_VALUES_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_STEPS_FIELD_NUMBER: _ClassVar[int]
    instrument_to_adjust: _spatial_analyzer_values_pb2.CollectionInstrumentId
    axis_values: _containers.RepeatedScalarFieldContainer[float]
    number_of_steps: int
    def __init__(self, instrument_to_adjust: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., axis_values: _Optional[_Iterable[float]] = ..., number_of_steps: _Optional[int] = ...) -> None: ...

class SetInstrumentAxesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentBaseUncertaintyCovarianceMatrixWrtBaseRequest(_message.Message):
    __slots__ = ("instrument", "covariance_matrix")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_MATRIX_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    covariance_matrix: UncertaintyCovarianceMatrix
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., covariance_matrix: _Optional[_Union[UncertaintyCovarianceMatrix, _Mapping]] = ...) -> None: ...

class SetInstrumentBaseUncertaintyCovarianceMatrixWrtBaseResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentBaseUncertaintyCovarianceMatrixWrtWorldRequest(_message.Message):
    __slots__ = ("instrument", "covariance_matrix")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COVARIANCE_MATRIX_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    covariance_matrix: UncertaintyCovarianceMatrix
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., covariance_matrix: _Optional[_Union[UncertaintyCovarianceMatrix, _Mapping]] = ...) -> None: ...

class SetInstrumentBaseUncertaintyCovarianceMatrixWrtWorldResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentGroupAndTargetRequest(_message.Message):
    __slots__ = ("instrument", "point")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class SetInstrumentGroupAndTargetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentInterfaceResponseTimeoutRequest(_message.Message):
    __slots__ = ("instrument", "timeout")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    timeout: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., timeout: _Optional[float] = ...) -> None: ...

class SetInstrumentInterfaceResponseTimeoutResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentMeasurementModeProfileRequest(_message.Message):
    __slots__ = ("instrument", "mode_profile")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    MODE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    mode_profile: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., mode_profile: _Optional[str] = ...) -> None: ...

class SetInstrumentMeasurementModeProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentTargetingRequest(_message.Message):
    __slots__ = ("instrument", "targeting_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TARGETING_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    targeting_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., targeting_name: _Optional[str] = ...) -> None: ...

class SetInstrumentTargetingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentTransformRequest(_message.Message):
    __slots__ = ("instrument", "destination_transform", "reference_frame", "number_of_steps")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_STEPS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    destination_transform: _spatial_analyzer_values_pb2.Transform
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    number_of_steps: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., destination_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., number_of_steps: _Optional[int] = ...) -> None: ...

class SetInstrumentTransformResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInstrumentWeatherSettingRequest(_message.Message):
    __slots__ = ("instrument", "temperature", "pressure", "relative_humidity", "set_automatically")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    PRESSURE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    SET_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    temperature: float
    pressure: float
    relative_humidity: float
    set_automatically: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., temperature: _Optional[float] = ..., pressure: _Optional[float] = ..., relative_humidity: _Optional[float] = ..., set_automatically: bool = ...) -> None: ...

class SetInstrumentWeatherSettingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarAutoMeasPointRequest(_message.Message):
    __slots__ = ("instrument", "sample_time_milliseconds")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_TIME_MILLISECONDS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    sample_time_milliseconds: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., sample_time_milliseconds: _Optional[int] = ...) -> None: ...

class SetLadarAutoMeasPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarAutoMeasSphereRequest(_message.Message):
    __slots__ = ("instrument", "sphere_radius", "scan_line_spacing", "send_center_point", "send_sphere", "send_measured_cloud")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SPHERE_RADIUS_FIELD_NUMBER: _ClassVar[int]
    SCAN_LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    SEND_CENTER_POINT_FIELD_NUMBER: _ClassVar[int]
    SEND_SPHERE_FIELD_NUMBER: _ClassVar[int]
    SEND_MEASURED_CLOUD_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    sphere_radius: float
    scan_line_spacing: float
    send_center_point: bool
    send_sphere: bool
    send_measured_cloud: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., sphere_radius: _Optional[float] = ..., scan_line_spacing: _Optional[float] = ..., send_center_point: bool = ..., send_sphere: bool = ..., send_measured_cloud: bool = ...) -> None: ...

class SetLadarAutoMeasSphereResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarFeatureMeasCircleRequest(_message.Message):
    __slots__ = ("instrument", "scan_line_spacing", "width_of_extra_area_around_scan")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    WIDTH_OF_EXTRA_AREA_AROUND_SCAN_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_line_spacing: float
    width_of_extra_area_around_scan: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_line_spacing: _Optional[float] = ..., width_of_extra_area_around_scan: _Optional[float] = ...) -> None: ...

class SetLadarFeatureMeasCircleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarFeatureMeasCylinderRequest(_message.Message):
    __slots__ = ("instrument", "scan_line_spacing", "width_of_extra_area_around_scan")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    WIDTH_OF_EXTRA_AREA_AROUND_SCAN_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_line_spacing: float
    width_of_extra_area_around_scan: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_line_spacing: _Optional[float] = ..., width_of_extra_area_around_scan: _Optional[float] = ...) -> None: ...

class SetLadarFeatureMeasCylinderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarFeatureMeasSlotRequest(_message.Message):
    __slots__ = ("instrument", "scan_line_spacing", "width_of_extra_area_around_scan")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    WIDTH_OF_EXTRA_AREA_AROUND_SCAN_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_line_spacing: float
    width_of_extra_area_around_scan: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_line_spacing: _Optional[float] = ..., width_of_extra_area_around_scan: _Optional[float] = ...) -> None: ...

class SetLadarFeatureMeasSlotResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLadarFeatureMeasSphereRequest(_message.Message):
    __slots__ = ("instrument", "scan_line_spacing")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCAN_LINE_SPACING_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_line_spacing: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_line_spacing: _Optional[float] = ...) -> None: ...

class SetLadarFeatureMeasSphereResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetMultiplyInstrumentScaleFactorRequest(_message.Message):
    __slots__ = ("instrument", "scale_factor")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scale_factor: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scale_factor: _Optional[float] = ...) -> None: ...

class SetMultiplyInstrumentScaleFactorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObservationCollimationShotOptionsRequest(_message.Message):
    __slots__ = ("point", "observation_index", "is_collimation_shot", "targeted_instrument")
    POINT_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_COLLIMATION_SHOT_FIELD_NUMBER: _ClassVar[int]
    TARGETED_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    is_collimation_shot: bool
    targeted_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., is_collimation_shot: bool = ..., targeted_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class SetObservationCollimationShotOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObservationMirrorCubeShotFaceRequest(_message.Message):
    __slots__ = ("point", "observation_index", "is_mirror_cube_shot", "mirror_cube_shot_face")
    POINT_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    IS_MIRROR_CUBE_SHOT_FIELD_NUMBER: _ClassVar[int]
    MIRROR_CUBE_SHOT_FACE_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    is_mirror_cube_shot: bool
    mirror_cube_shot_face: int
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., is_mirror_cube_shot: bool = ..., mirror_cube_shot_face: _Optional[int] = ...) -> None: ...

class SetObservationMirrorCubeShotFaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObservationStatusRequest(_message.Message):
    __slots__ = ("point", "observation_index", "active")
    POINT_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_INDEX_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    observation_index: int
    active: bool
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., observation_index: _Optional[int] = ..., active: bool = ...) -> None: ...

class SetObservationStatusResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPcmmInstrumentXyzUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument", "x_uncertainty", "y_uncertainty", "z_uncertainty")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    X_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Y_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Z_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    x_uncertainty: float
    y_uncertainty: float
    z_uncertainty: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., x_uncertainty: _Optional[float] = ..., y_uncertainty: _Optional[float] = ..., z_uncertainty: _Optional[float] = ...) -> None: ...

class SetPcmmInstrumentXyzUncertaintiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetProbeOffsetFrameOfflineRequest(_message.Message):
    __slots__ = ("instrument", "probe_name", "face_id", "raw_measured_frame", "offset_frame")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROBE_NAME_FIELD_NUMBER: _ClassVar[int]
    FACE_ID_FIELD_NUMBER: _ClassVar[int]
    RAW_MEASURED_FRAME_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FRAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    probe_name: str
    face_id: int
    raw_measured_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    offset_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., probe_name: _Optional[str] = ..., face_id: _Optional[int] = ..., raw_measured_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., offset_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetProbeOffsetFrameOfflineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetProbeOffsetFrameOnlineRequest(_message.Message):
    __slots__ = ("instrument", "probe_name", "face_id", "measure_profile_name", "timeout_seconds", "offset_frame")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROBE_NAME_FIELD_NUMBER: _ClassVar[int]
    FACE_ID_FIELD_NUMBER: _ClassVar[int]
    MEASURE_PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_SECONDS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FRAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    probe_name: str
    face_id: int
    measure_profile_name: str
    timeout_seconds: float
    offset_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., probe_name: _Optional[str] = ..., face_id: _Optional[int] = ..., measure_profile_name: _Optional[str] = ..., timeout_seconds: _Optional[float] = ..., offset_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetProbeOffsetFrameOnlineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRemeasureFailedChecksOnlyRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class SetRemeasureFailedChecksOnlyResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTargetComputationOptionsRequest(_message.Message):
    __slots__ = ("computation_method", "ignore_distance_measurements")
    COMPUTATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    IGNORE_DISTANCE_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    computation_method: TargetComputationMethod
    ignore_distance_measurements: bool
    def __init__(self, computation_method: _Optional[_Union[TargetComputationMethod, str]] = ..., ignore_distance_measurements: bool = ...) -> None: ...

class SetTargetComputationOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTrackerEdmTheodoliteUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument", "theta_dispersion", "theta_threshold", "phi_dispersion", "phi_threshold", "distance", "distance_threshold")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    THETA_DISPERSION_FIELD_NUMBER: _ClassVar[int]
    THETA_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    PHI_DISPERSION_FIELD_NUMBER: _ClassVar[int]
    PHI_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_FIELD_NUMBER: _ClassVar[int]
    DISTANCE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    theta_dispersion: float
    theta_threshold: float
    phi_dispersion: float
    phi_threshold: float
    distance: float
    distance_threshold: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., theta_dispersion: _Optional[float] = ..., theta_threshold: _Optional[float] = ..., phi_dispersion: _Optional[float] = ..., phi_threshold: _Optional[float] = ..., distance: _Optional[float] = ..., distance_threshold: _Optional[float] = ...) -> None: ...

class SetTrackerEdmTheodoliteUncertaintiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetWrtlChannelRequest(_message.Message):
    __slots__ = ("instrument", "channel")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    channel: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., channel: _Optional[int] = ...) -> None: ...

class SetWrtlChannelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetXyzInstrumentUncertaintiesRequest(_message.Message):
    __slots__ = ("instrument", "x_uncertainty", "y_uncertainty", "z_uncertainty")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    X_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Y_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    Z_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    x_uncertainty: float
    y_uncertainty: float
    z_uncertainty: float
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., x_uncertainty: _Optional[float] = ..., y_uncertainty: _Optional[float] = ..., z_uncertainty: _Optional[float] = ...) -> None: ...

class SetXyzInstrumentUncertaintiesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetXyzReferenceFrameInstrumentBaseAnchorFrameRequest(_message.Message):
    __slots__ = ("instrument", "anchor_frame")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    ANCHOR_FRAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    anchor_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., anchor_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetXyzReferenceFrameInstrumentBaseAnchorFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartGdtInspectionDesignRequest(_message.Message):
    __slots__ = ("collection", "filter")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    filter: InspectionFilter
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., filter: _Optional[_Union[InspectionFilter, str]] = ...) -> None: ...

class StartGdtInspectionDesignResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartGdtInspectionRehearseRequest(_message.Message):
    __slots__ = ("collection", "filter")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    filter: InspectionFilter
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., filter: _Optional[_Union[InspectionFilter, str]] = ...) -> None: ...

class StartGdtInspectionRehearseResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartGdtInspectionRequest(_message.Message):
    __slots__ = ("instrument", "collection", "filter")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    collection: _spatial_analyzer_values_pb2.CollectionName
    filter: InspectionFilter
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., filter: _Optional[_Union[InspectionFilter, str]] = ...) -> None: ...

class StartGdtInspectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartInstrumentInterfaceRequest(_message.Message):
    __slots__ = ("instrument", "initialize_at_startup", "device_ip_address", "interface_type", "run_in_simulation", "allow_start_without_initialization_requirements")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    INITIALIZE_AT_STARTUP_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUN_IN_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    ALLOW_START_WITHOUT_INITIALIZATION_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    initialize_at_startup: bool
    device_ip_address: str
    interface_type: int
    run_in_simulation: bool
    allow_start_without_initialization_requirements: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., initialize_at_startup: bool = ..., device_ip_address: _Optional[str] = ..., interface_type: _Optional[int] = ..., run_in_simulation: bool = ..., allow_start_without_initialization_requirements: bool = ...) -> None: ...

class StartInstrumentInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartTheodoliteInterfaceRequest(_message.Message):
    __slots__ = ("instrument", "theodolite_type", "comm_port", "device_ip_address", "simulation")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    THEODOLITE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMM_PORT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SIMULATION_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    theodolite_type: str
    comm_port: int
    device_ip_address: str
    simulation: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., theodolite_type: _Optional[str] = ..., comm_port: _Optional[int] = ..., device_ip_address: _Optional[str] = ..., simulation: bool = ...) -> None: ...

class StartTheodoliteInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StopActiveMeasurementModeRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class StopActiveMeasurementModeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StopInstrumentInterfaceRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class StopInstrumentInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StopProjectionRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class StopProjectionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SynchronizedMeasurementMasterSlaveRequest(_message.Message):
    __slots__ = ("master_instrument", "slave_instrument", "slave_group_suffix", "locate_one_of_the_instruments", "locate_master", "wait_for_completion")
    MASTER_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SLAVE_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    SLAVE_GROUP_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    LOCATE_ONE_OF_THE_INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    LOCATE_MASTER_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    master_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    slave_instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    slave_group_suffix: str
    locate_one_of_the_instruments: bool
    locate_master: bool
    wait_for_completion: bool
    def __init__(self, master_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., slave_instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., slave_group_suffix: _Optional[str] = ..., locate_one_of_the_instruments: bool = ..., locate_master: bool = ..., wait_for_completion: bool = ...) -> None: ...

class SynchronizedMeasurementMasterSlaveResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TcpFixtureUncertainties(_message.Message):
    __slots__ = ("solution_valid", "refined_tcp_in_working", "uncertainties_in_tcp_fixture_frame", "uncertainties_in_working_frame", "rms_error", "maximum_absolute_error", "goodness_of_fit", "robustness", "result_notes")
    SOLUTION_VALID_FIELD_NUMBER: _ClassVar[int]
    REFINED_TCP_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTIES_IN_TCP_FIXTURE_FRAME_FIELD_NUMBER: _ClassVar[int]
    UNCERTAINTIES_IN_WORKING_FRAME_FIELD_NUMBER: _ClassVar[int]
    RMS_ERROR_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ABSOLUTE_ERROR_FIELD_NUMBER: _ClassVar[int]
    GOODNESS_OF_FIT_FIELD_NUMBER: _ClassVar[int]
    ROBUSTNESS_FIELD_NUMBER: _ClassVar[int]
    RESULT_NOTES_FIELD_NUMBER: _ClassVar[int]
    solution_valid: bool
    refined_tcp_in_working: _spatial_analyzer_values_pb2.Transform
    uncertainties_in_tcp_fixture_frame: DoubleVector6
    uncertainties_in_working_frame: DoubleVector6
    rms_error: float
    maximum_absolute_error: float
    goodness_of_fit: float
    robustness: float
    result_notes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, solution_valid: bool = ..., refined_tcp_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., uncertainties_in_tcp_fixture_frame: _Optional[_Union[DoubleVector6, _Mapping]] = ..., uncertainties_in_working_frame: _Optional[_Union[DoubleVector6, _Mapping]] = ..., rms_error: _Optional[float] = ..., maximum_absolute_error: _Optional[float] = ..., goodness_of_fit: _Optional[float] = ..., robustness: _Optional[float] = ..., result_notes: _Optional[_Iterable[str]] = ...) -> None: ...

class TrackTapeMeasurementRequest(_message.Message):
    __slots__ = ("instrument", "point_on_tape", "point_on_part", "direction_point", "termination_point", "parameter_set_name", "point_group", "initial_target_name")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    POINT_ON_TAPE_FIELD_NUMBER: _ClassVar[int]
    POINT_ON_PART_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_POINT_FIELD_NUMBER: _ClassVar[int]
    TERMINATION_POINT_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    INITIAL_TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    point_on_tape: _spatial_analyzer_values_pb2.PointName
    point_on_part: _spatial_analyzer_values_pb2.PointName
    direction_point: _spatial_analyzer_values_pb2.PointName
    termination_point: _spatial_analyzer_values_pb2.PointName
    parameter_set_name: str
    point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    initial_target_name: str
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., point_on_tape: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., point_on_part: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., direction_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., termination_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., parameter_set_name: _Optional[str] = ..., point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., initial_target_name: _Optional[str] = ...) -> None: ...

class TrackTapeMeasurementResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformInstrumentByDeltaRequest(_message.Message):
    __slots__ = ("instrument", "delta_transform", "apply_scale_to_instrument")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    DELTA_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    APPLY_SCALE_TO_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    delta_transform: _spatial_analyzer_values_pb2.WorldTransform
    apply_scale_to_instrument: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., delta_transform: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., apply_scale_to_instrument: bool = ...) -> None: ...

class TransformInstrumentByDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformInstrumentFrameToFrameRequest(_message.Message):
    __slots__ = ("instrument", "initial_frame", "destination_frame", "number_of_steps")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    INITIAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FRAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_STEPS_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    initial_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    destination_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    number_of_steps: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., initial_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., destination_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., number_of_steps: _Optional[int] = ...) -> None: ...

class TransformInstrumentFrameToFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TransformMultipleInstrumentsByDeltaRequest(_message.Message):
    __slots__ = ("instruments", "delta_transform", "apply_scale_to_instruments")
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    DELTA_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    APPLY_SCALE_TO_INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    delta_transform: _spatial_analyzer_values_pb2.WorldTransform
    apply_scale_to_instruments: bool
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., delta_transform: _Optional[_Union[_spatial_analyzer_values_pb2.WorldTransform, _Mapping]] = ..., apply_scale_to_instruments: bool = ...) -> None: ...

class TransformMultipleInstrumentsByDeltaResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class UncertaintyCovarianceMatrix(_message.Message):
    __slots__ = ("row_1", "row_2", "row_3", "row_4", "row_5", "row_6")
    ROW_1_FIELD_NUMBER: _ClassVar[int]
    ROW_2_FIELD_NUMBER: _ClassVar[int]
    ROW_3_FIELD_NUMBER: _ClassVar[int]
    ROW_4_FIELD_NUMBER: _ClassVar[int]
    ROW_5_FIELD_NUMBER: _ClassVar[int]
    ROW_6_FIELD_NUMBER: _ClassVar[int]
    row_1: DoubleVector6
    row_2: DoubleVector6
    row_3: DoubleVector6
    row_4: DoubleVector6
    row_5: DoubleVector6
    row_6: DoubleVector6
    def __init__(self, row_1: _Optional[_Union[DoubleVector6, _Mapping]] = ..., row_2: _Optional[_Union[DoubleVector6, _Mapping]] = ..., row_3: _Optional[_Union[DoubleVector6, _Mapping]] = ..., row_4: _Optional[_Union[DoubleVector6, _Mapping]] = ..., row_5: _Optional[_Union[DoubleVector6, _Mapping]] = ..., row_6: _Optional[_Union[DoubleVector6, _Mapping]] = ...) -> None: ...

class VerifyInstrumentConnectionRequest(_message.Message):
    __slots__ = ("instrument",)
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class VerifyInstrumentConnectionResult(_message.Message):
    __slots__ = ("connected", "execution")
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    connected: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, connected: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WaitForTrappingToCompleteRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class WaitForTrappingToCompleteResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchClosestPointRequest(_message.Message):
    __slots__ = ("instrument", "groups_to_consider", "watch_window_properties", "measurement_mode", "pause_mp_until_closed", "window_top_left_x", "window_top_left_y", "window_width", "window_height")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    GROUPS_TO_CONSIDER_FIELD_NUMBER: _ClassVar[int]
    WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_MP_UNTIL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    groups_to_consider: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_mode: str
    pause_mp_until_closed: bool
    window_top_left_x: int
    window_top_left_y: int
    window_width: int
    window_height: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., groups_to_consider: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_mode: _Optional[str] = ..., pause_mp_until_closed: bool = ..., window_top_left_x: _Optional[int] = ..., window_top_left_y: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class WatchClosestPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchInstrumentRequest(_message.Message):
    __slots__ = ("instrument", "pause_mp_until_closed", "watch_window_properties", "window_top_left_x", "window_top_left_y", "window_width", "window_height")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PAUSE_MP_UNTIL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    pause_mp_until_closed: bool
    watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    window_top_left_x: int
    window_top_left_y: int
    window_width: int
    window_height: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., pause_mp_until_closed: bool = ..., watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., window_top_left_x: _Optional[int] = ..., window_top_left_y: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class WatchInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchPointToEdgeRequest(_message.Message):
    __slots__ = ("instrument", "projection_reference_objects", "measurement_reference_objects", "projection_options", "watch_window_properties", "measurement_mode", "pause_mp_until_closed", "window_top_left_x", "window_top_left_y", "window_width", "window_height")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_REFERENCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_REFERENCE_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_MP_UNTIL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    projection_reference_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    measurement_reference_objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_mode: str
    pause_mp_until_closed: bool
    window_top_left_x: int
    window_top_left_y: int
    window_width: int
    window_height: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., projection_reference_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., measurement_reference_objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_mode: _Optional[str] = ..., pause_mp_until_closed: bool = ..., window_top_left_x: _Optional[int] = ..., window_top_left_y: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class WatchPointToEdgeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchPointToObjectsRequest(_message.Message):
    __slots__ = ("instrument", "objects_to_consider", "projection_options", "watch_window_properties", "measurement_mode", "pause_mp_until_closed", "window_top_left_x", "window_top_left_y", "window_width", "window_height")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_TO_CONSIDER_FIELD_NUMBER: _ClassVar[int]
    PROJECTION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_MP_UNTIL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    objects_to_consider: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    projection_options: _spatial_analyzer_values_pb2.ProjectionOptions
    watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_mode: str
    pause_mp_until_closed: bool
    window_top_left_x: int
    window_top_left_y: int
    window_width: int
    window_height: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., objects_to_consider: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., projection_options: _Optional[_Union[_spatial_analyzer_values_pb2.ProjectionOptions, _Mapping]] = ..., watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_mode: _Optional[str] = ..., pause_mp_until_closed: bool = ..., window_top_left_x: _Optional[int] = ..., window_top_left_y: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class WatchPointToObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchPointToPointRequest(_message.Message):
    __slots__ = ("instrument", "reference_point", "watch_window_properties", "measurement_mode", "pause_mp_until_closed", "window_top_left_x", "window_top_left_y", "window_width", "window_height")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_POINT_FIELD_NUMBER: _ClassVar[int]
    WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    PAUSE_MP_UNTIL_CLOSED_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_point: _spatial_analyzer_values_pb2.PointName
    watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_mode: str
    pause_mp_until_closed: bool
    window_top_left_x: int
    window_top_left_y: int
    window_width: int
    window_height: int
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_mode: _Optional[str] = ..., pause_mp_until_closed: bool = ..., window_top_left_x: _Optional[int] = ..., window_top_left_y: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class WatchPointToPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WatchPointToPointWithViewZoomingRequest(_message.Message):
    __slots__ = ("instrument", "reference_point", "update")
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_POINT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    reference_point: _spatial_analyzer_values_pb2.PointName
    update: bool
    def __init__(self, instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., reference_point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., update: bool = ...) -> None: ...

class WatchPointToPointWithViewZoomingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WrtlChannelStatus(_message.Message):
    __slots__ = ("connection_status", "active_channel")
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    connection_status: bool
    active_channel: int
    def __init__(self, connection_status: bool = ..., active_channel: _Optional[int] = ...) -> None: ...
