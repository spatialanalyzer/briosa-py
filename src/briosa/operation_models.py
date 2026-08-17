"""Named detached results for Wave A operations."""

from __future__ import annotations

from dataclasses import dataclass

from briosa.operation_values import (
    CollectionObjectName,
    FileReference,
    FitConstraintScalarOptions,
    PointName,
    ToleranceScalarOptions,
    ToleranceVectorOptions,
    Transform,
    Vector,
    WorldTransform,
)


@dataclass(frozen=True, slots=True, kw_only=True)
class BestFitTransformationGroupToGroupResult:
    transform_in_working: Transform
    optimum_transform: WorldTransform
    rms_deviation: float
    maximum_absolute_deviation: float
    number_of_unknowns: int
    number_of_equations: int
    robustness: float


@dataclass(frozen=True, slots=True, kw_only=True)
class ComputeGroupToGroupOrientationRxRyRzResult:
    rx: float
    ry: float
    rz: float


@dataclass(frozen=True, slots=True, kw_only=True)
class CreatePointUncertaintyCloudPointSetsResult:
    point_groups: list[CollectionObjectName]
    point_sets: list[CollectionObjectName]
    point_clouds: list[CollectionObjectName]


@dataclass(frozen=True, slots=True, kw_only=True)
class GetBSplinePropertiesResult:
    degree: int
    knots: int
    control_points: int
    range_min: float
    range_max: float
    length: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetCirclePropertiesResult:
    center_coordinate: Vector
    normal_direction: Vector
    radius: float
    diameter: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetConePropertiesResult:
    cone_end_point_in_working_coordinates: Vector
    cone_axis_in_working_coordinates: Vector
    cone_length: float
    cone_theta_start: float
    cone_theta_span: float
    cone_included_angle: float
    cut_length_from_apex: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetCoordinateForIthPointInPointSetResult:
    point_name: str
    point_coordinates: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class GetCylinderPropertiesResult:
    begin_coordinate: Vector
    end_coordinate: Vector
    axis_direction: Vector
    length: float
    radius: float
    diameter: float
    nominals_point_inward: bool
    facets: int
    enable_theta_extent_display_mode: bool
    theta_start_in_degrees: float
    theta_span_in_degrees: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetEllipsePropertiesResult:
    center_coordinate: Vector
    normal_direction: Vector
    major_axis_radius: float
    minor_axis_radius: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetEulerParametersForFrameResult:
    x: float
    y: float
    z: float
    e1: float
    e2: float
    e3: float
    e4: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetEulerParametersForIthFrameInFrameSetResult:
    x: float
    y: float
    z: float
    e1: float
    e2: float
    e3: float
    e4: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetIthPointFromGroupResult:
    complete_point_name: PointName
    point_name_only: str
    vector_in_working: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class GetLinePropertiesResult:
    begin_coordinate: Vector
    end_coordinate: Vector
    delta_components: Vector
    length: float
    angle_about_x_from_y_in_yz_plane: float
    angle_about_y_from_z_in_xz_plane: float
    angle_about_z_from_x_in_xy_plane: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetMeasurementAuxiliaryDataResult:
    value: float
    units: str


@dataclass(frozen=True, slots=True, kw_only=True)
class GetMeasurementWeatherDataResult:
    temperature_deg_f: float
    pressure_in_hg: float
    humidity_rh: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPlanePropertiesResult:
    normal_direction: Vector
    point_on_plane: Vector
    d_parameter: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointCoordinateResult:
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointCoordinateCylindricalResult:
    radius_value: float
    theta_value: float
    z_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointCoordinatePolarResult:
    radius_value: float
    theta_value: float
    phi_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointPropertiesResult:
    planar_offset: float
    radial_offset: float
    ux: float
    uy: float
    uz: float
    umag: float
    position_tolerance: ToleranceVectorOptions
    component_weights: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointToLineDistanceResult:
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointToPointDistanceResult:
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointToleranceResult:
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
    vector_tolerance: ToleranceVectorOptions


@dataclass(frozen=True, slots=True, kw_only=True)
class GetSlotPropertiesResult:
    slot_transform_in_working_coordinates: Transform
    center_in_working_coordinates: Vector
    normal_direction_in_working_coordinates: Vector
    slot_length: float
    slot_width: float
    round_slot_type: bool
    centerline_pt_1_in_working_coordinates: Vector
    centerline_pt_2_in_working_coordinates: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class GetSpherePropertiesResult:
    center_coordinate: Vector
    radius: float
    diameter: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetSurfacePhysicalStatsResult:
    volume: float
    area: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetTorusPropertiesResult:
    center_coordinate: Vector
    normal_direction: Vector
    major_radius: float
    minor_radius: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GroupToSurfaceFitResult:
    optimum_transform: WorldTransform
    rms_deviation: float
    maximum_absolute_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class MushroomTargetHoleInspectionResult:
    sphere_fit_rms_error: float
    sphere_fit_max_error: float


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryCloudsToObjectsResult:
    rms_deviation: float
    maximum_absolute_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryCloudsToSurfaceResult:
    rms_deviation: float
    maximum_absolute_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryFrameToFrameResult:
    x: float
    y: float
    z: float
    rx_roll: float
    ry_pitch: float
    rz_yaw: float


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryGroupsToObjectsResult:
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    standard_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryPointToObjectsResult:
    d_x: float
    d_y: float
    d_z: float
    d_mag: float
    resultant_object: CollectionObjectName


@dataclass(frozen=True, slots=True, kw_only=True)
class QueryPointsToObjectsResult:
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float
    standard_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class SphereAxisCheckResult:
    sphere_fit_rms_error: float
    sphere_fit_max_error: float
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetDimensionValueResult:
    dimensions_value: float
    nominal_value_enabled: bool
    high_tolerance_enabled: bool
    low_tolerance_enabled: bool
    nominal_value: float
    high_tolerance: float
    low_tolerance: float


@dataclass(frozen=True, slots=True, kw_only=True)
class DirectCadAccessResult:
    import_warnings: bool
    import_warning_messages: str
    extents_min: Vector
    extents_max: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class AskForStringPullDownVersionResult:
    answer: str
    answer_index: int


@dataclass(frozen=True, slots=True, kw_only=True)
class GetGeomRelationshipAutoVectorsResult:
    auto_vectors_nominal_avn_enabled: bool
    auto_vectors_nominal_avn_name: CollectionObjectName
    auto_vectors_fit_avf_enabled: bool
    auto_vectors_fit_avf_name: CollectionObjectName
    points_type: str


@dataclass(frozen=True, slots=True, kw_only=True)
class GetGeomRelationshipCriteriaResult:
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


@dataclass(frozen=True, slots=True, kw_only=True)
class GetGeomRelationshipPointListResult:
    all_points: list[PointName]
    used_points: list[PointName]
    ignored_points: list[PointName]


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPipeRelationshipCutStatusResult:
    pipe_1_cut_available: bool
    pipe_1_cut_active: bool
    pipe_2_cut_available: bool
    pipe_2_cut_active: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPipeRelationshipPropertiesResult:
    pipe_1_object_name: CollectionObjectName
    pipe_1_inner_diameter: float
    pipe_1_outer_diameter: float
    pipe_1_cut_begin: float
    pipe_1_cut_end: float
    pipe_2_object_name: CollectionObjectName
    pipe_2_inner_diameter: float
    pipe_2_outer_diameter: float
    pipe_2_cut_begin: float
    pipe_2_cut_end: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPipeRelationshipWeightsResult:
    overall_weight: float
    axis_offset: float
    axis_alignment: float
    center_pull: float
    out_of_material_weight: float
    out_of_material_static_offset: float
    constrain_region_at_od: bool
    constrain_id_od_overlap: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipFitConstraintsScalarTypeResult:
    use_high_tolerance: bool
    high_tolerance: float
    use_low_tolerance: bool
    low_tolerance: float
    fit_constraint_options: FitConstraintScalarOptions


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipOutlierRejectionScalarTypeResult:
    use_high_limit: bool
    high_limit: float
    use_low_limit: bool
    low_limit: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipProjectionOptionsResult:
    ignore_edge_projections: bool
    probe_offsets_override_target_values: bool
    probe_offsets_override_value: float
    add_extra_material: bool
    extra_material_thickness: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipSubSamplingOptionsResult:
    use_every_ith_point: bool
    i_value: int
    use_no_more_than_n_points: bool
    n_value: int


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipToleranceScalarTypeResult:
    use_high_tolerance: bool
    high_tolerance: float
    use_low_tolerance: bool
    low_tolerance: float
    tolerance_options: ToleranceScalarOptions


@dataclass(frozen=True, slots=True, kw_only=True)
class GetRelationshipToleranceVectorTypeResult:
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
    vector_tolerance: ToleranceVectorOptions


@dataclass(frozen=True, slots=True, kw_only=True)
class GetReportTagValueResult:
    tag_value_as_string: str
    tag_value_as_integer: int
    tag_value_as_double: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetScaleBarStatsResult:
    nominal_length: float
    actual_length: float
    deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetActiveLanguageResult:
    language_file_name: FileReference
    custom_language: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class ActiveUnits:
    length: str
    angular: str
    temperature: str


@dataclass(frozen=True, slots=True, kw_only=True)
class GetScreenResolutionResult:
    integer_window_top_left_x_position: int
    integer_window_top_left_y_position: int
    integer_width: int
    integer_height: int
    view_width: int
    view_height: int


@dataclass(frozen=True, slots=True, kw_only=True)
class WorkingFrameProperties:
    frame_name: str
    collection_name: str
    working_frame: CollectionObjectName


@dataclass(frozen=True, slots=True, kw_only=True)
class GetNamedDoubleListVariableMinMaxResult:
    minimum_value: float
    maximum_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetIthVectorFromVectorGroupResult:
    vector_name: str
    begin_in_working: Vector
    end_in_working: Vector
    total_delta_in_working: Vector
    ijk_unit_vector_in_working: Vector
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetIthVectorFromVectorNameRefListResult:
    vector_group_name: CollectionObjectName
    vector_name: str
    begin_in_working: Vector
    end_in_working: Vector
    total_delta_in_working: Vector
    ijk_unit_vector_in_working: Vector
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetVectorFromVectorGroupByNameResult:
    begin_in_working: Vector
    end_in_working: Vector
    total_delta_in_working: Vector
    ijk_unit_vector_in_working: Vector
    magnitude: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetVectorGroupPropertiesResult:
    total_vectors: int
    vectors_in_tolerance: int
    vectors_out_of_tolerance: int
    invalid_vectors: int
    vectors_in_tolerance_2: float
    vectors_out_of_tolerance_2: float
    absolute_max_magnitude: float
    absolute_min_magnitude: float
    max_magnitude: float
    min_magnitude: float
    standard_deviation_from_zero: float
    standard_deviation_from_mean: float
    avg_magnitude: float
    avg_of_abs_magnitude: float
    high_tolerance_value: float
    low_tolerance_value: float
    rms_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class GetPointOfViewParametersResult:
    rotation_x: float
    rotation_y: float
    rotation_z: float
    restore_zoom_settings: bool
    scale_factor: float
    origin_x: float
    origin_y: float
    restore_render_mode: bool


__all__ = [
    "ActiveUnits",
    "AskForStringPullDownVersionResult",
    "BestFitTransformationGroupToGroupResult",
    "ComputeGroupToGroupOrientationRxRyRzResult",
    "CreatePointUncertaintyCloudPointSetsResult",
    "DirectCadAccessResult",
    "GetActiveLanguageResult",
    "GetBSplinePropertiesResult",
    "GetCirclePropertiesResult",
    "GetConePropertiesResult",
    "GetCoordinateForIthPointInPointSetResult",
    "GetCylinderPropertiesResult",
    "GetDimensionValueResult",
    "GetEllipsePropertiesResult",
    "GetEulerParametersForFrameResult",
    "GetEulerParametersForIthFrameInFrameSetResult",
    "GetGeomRelationshipAutoVectorsResult",
    "GetGeomRelationshipCriteriaResult",
    "GetGeomRelationshipPointListResult",
    "GetIthPointFromGroupResult",
    "GetIthVectorFromVectorGroupResult",
    "GetIthVectorFromVectorNameRefListResult",
    "GetLinePropertiesResult",
    "GetMeasurementAuxiliaryDataResult",
    "GetMeasurementWeatherDataResult",
    "GetNamedDoubleListVariableMinMaxResult",
    "GetPipeRelationshipCutStatusResult",
    "GetPipeRelationshipPropertiesResult",
    "GetPipeRelationshipWeightsResult",
    "GetPlanePropertiesResult",
    "GetPointCoordinateCylindricalResult",
    "GetPointCoordinatePolarResult",
    "GetPointCoordinateResult",
    "GetPointOfViewParametersResult",
    "GetPointPropertiesResult",
    "GetPointToLineDistanceResult",
    "GetPointToPointDistanceResult",
    "GetPointToleranceResult",
    "GetRelationshipFitConstraintsScalarTypeResult",
    "GetRelationshipOutlierRejectionScalarTypeResult",
    "GetRelationshipProjectionOptionsResult",
    "GetRelationshipSubSamplingOptionsResult",
    "GetRelationshipToleranceScalarTypeResult",
    "GetRelationshipToleranceVectorTypeResult",
    "GetReportTagValueResult",
    "GetScaleBarStatsResult",
    "GetScreenResolutionResult",
    "GetSlotPropertiesResult",
    "GetSpherePropertiesResult",
    "GetSurfacePhysicalStatsResult",
    "GetTorusPropertiesResult",
    "GetVectorFromVectorGroupByNameResult",
    "GetVectorGroupPropertiesResult",
    "GroupToSurfaceFitResult",
    "MushroomTargetHoleInspectionResult",
    "QueryCloudsToObjectsResult",
    "QueryCloudsToSurfaceResult",
    "QueryFrameToFrameResult",
    "QueryGroupsToObjectsResult",
    "QueryPointToObjectsResult",
    "QueryPointsToObjectsResult",
    "SphereAxisCheckResult",
    "WorkingFrameProperties",
]
