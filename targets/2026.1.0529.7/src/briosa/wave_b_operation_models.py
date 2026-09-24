"""Named detached Wave B operation results."""

# ruff: noqa: F405  # Public names come from explicit module export lists.
from __future__ import annotations

from dataclasses import dataclass

from briosa.operation_values import *  # noqa: F403
from briosa.wave_b_operation_values import *  # noqa: F403


@dataclass(frozen=True, slots=True, kw_only=True)
class CalibrationApplianceNodeStatus:
    instrument_connected: bool
    calibration_appliance_connected: bool


@dataclass(frozen=True, slots=True)
class CalloutPosition:
    x_position: int
    y_position: int
    x_anchor_position: int
    y_anchor_position: int
    callout_width: int
    callout_height: int


@dataclass(frozen=True, slots=True, kw_only=True)
class ConstructVectorGroupGroupToGroupCompareResult:
    vector_count: int
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float


@dataclass(frozen=True)
class DeleteCollectionsByWildcardResult:
    num_deleted: int
    num_failed: int


@dataclass(frozen=True)
class DeleteFoldersByWildcardResult:
    num_deleted: int
    num_failed: int


@dataclass(frozen=True, slots=True, kw_only=True)
class DriftCheckResult:
    maximum_error: float
    rms_error: float
    instrument_added: bool
    new_instrument: CollectionInstrumentId | None


@dataclass(frozen=True)
class EulerXyzTransformComponents:
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float


@dataclass(frozen=True)
class EulerZxzTransformComponents:
    x: float
    y: float
    z: float
    first_rz: float
    rx: float
    second_rz: float


@dataclass(frozen=True)
class EulerZyxTransformComponents:
    x: float
    y: float
    z: float
    rz: float
    ry: float
    rx: float


@dataclass(frozen=True)
class EulerZyzTransformComponents:
    x: float
    y: float
    z: float
    first_rz: float
    ry: float
    second_rz: float


@dataclass(frozen=True, slots=True, kw_only=True)
class EvaluateFeatureCheckResult:
    check_evaluated: bool
    check_result: str
    non_unique_result: bool
    measured_deviation_upper: float
    distance_out_of_tolerance_upper: float
    eval_delta_transform_upper: WorldTransform
    measured_deviation_lower: float
    distance_out_of_tolerance_lower: float
    eval_delta_transform_lower: WorldTransform
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


@dataclass(frozen=True, slots=True, kw_only=True)
class EvaluateFeatureChecksResult:
    total_passed: int
    total_failed: int
    total_incomplete: int


@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureCheckDatumReferencesResult:
    datum_1: FeatureCheckDatumReference
    datum_2: FeatureCheckDatumReference
    datum_3: FeatureCheckDatumReference


@dataclass(frozen=True, slots=True, kw_only=True)
class FitErrorResult:
    rms_error: float
    maximum_error: float


@dataclass(frozen=True)
class FixedXyzTransformComponents:
    x: float
    y: float
    z: float
    rx: float
    ry: float
    rz: float


@dataclass(frozen=True)
class FixedXyzTransformVectors:
    position_in_working: Vector
    orientation_in_working: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class GeneralRelationshipStatistics:
    absolute_max_deviation: float
    rms: float
    has_signed_deviation: bool
    signed_max_deviation: float
    signed_min_deviation: float


@dataclass(frozen=True, slots=True)
class GetCloudPointCountResult:
    points_count: int
    planar_offset: float
    radial_offset: float
    active_clipping_planes: int


@dataclass(frozen=True, slots=True)
class GetCloudRGBValuesNearPointResult:
    low_value: int
    high_value: int
    average_value: int
    standard_deviation: int


@dataclass(frozen=True, slots=True)
class GetCloudRGBValuesResult:
    low_value: int
    high_value: int
    average_value: int
    standard_deviation: int


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentBestFitResult:
    transform_in_working: Transform
    optimum_transform: WorldTransform
    rms_deviation: float
    maximum_absolute_deviation: float
    number_of_unknowns: int
    number_of_equations: int
    robustness: float


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentModelResult:
    name: str
    model: str


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentPositionUpdate:
    x_or_r: float
    # Angle in degrees.
    y_or_theta: float
    # Angle in degrees.
    z_or_phi: float
    # Time in seconds.
    time_since_update: float
    # MP qualifier: Approximate.
    timestamp: str


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTargetsAndModeProfiles:
    mode_profiles: list[str]
    target_names: list[str]


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentWeatherSetting:
    # Temperature in degrees Fahrenheit.
    temperature: float
    # Pressure in millimeters of mercury.
    pressure: float
    # Relative humidity in percent.
    relative_humidity: float
    set_automatically: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentXyzUncertainties:
    x_uncertainty: float
    y_uncertainty: float
    z_uncertainty: float


@dataclass(frozen=True, slots=True, kw_only=True)
class LastInstrumentIndexResult:
    instrument_index: int
    instrument: CollectionInstrumentId


@dataclass(frozen=True, slots=True, kw_only=True)
class LrSelfTestResult:
    # Length in inches.
    reference_arm_length: float
    reference_arm_quality: float
    mirror_measurement_count: int
    # Length in inches.
    mirror_measurement_range_mean: float
    # Length in inches.
    mirror_measurement_range_standard_deviation: float
    mirror_measurement_quality_mean: float
    mirror_measurement_quality_standard_deviation: float
    passed_reference_arm_quality_threshold: bool
    passed_mirror_offset_delta_threshold: bool
    passed_mirror_offset_standard_deviation_threshold: bool
    passed_mirror_mean_quality_threshold: bool
    passed_overall: bool


@dataclass(frozen=True, slots=True)
class MeshVolumeResult:
    above: float
    below: float


@dataclass(frozen=True, slots=True, kw_only=True)
class PointComparisonResult:
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float
    magnitude: float
    resulting_point_name: PointName


@dataclass(frozen=True, slots=True, kw_only=True)
class PointToPointRelationshipStatistics:
    delta_x: float
    delta_y: float
    delta_z: float
    delta_magnitude: float
    reference_frame: CollectionObjectName


@dataclass(frozen=True, slots=True, kw_only=True)
class PointsToObjectsRelationshipStatistics:
    absolute_max_deviation: float
    max_deviation: float
    min_deviation: float
    avg_deviation: float
    rms: float
    candidate_point_count: int
    sampled_point_count: int
    rejected_point_count: int
    used_point_count: int
    out_of_tolerance_point_count: int


@dataclass(frozen=True, slots=True, kw_only=True)
class RelationshipFitResult:
    transform_in_reference: Transform
    transform_in_working: WorldTransform
    transform_in_world: WorldTransform
    fit_objective_value: float


@dataclass(frozen=True, slots=True)
class ResetCloudBoundingBoxResult:
    x_axis_dimension: float
    y_axis_dimension: float
    z_axis_dimension: float
    x_axis_in_world: Vector
    y_axis_in_world: Vector
    z_axis_in_world: Vector
    centroid_in_world: Vector
    reference_transform_in_world: Transform
    reference_transform_in_working: Transform
    points_used_for_bounding_box: int


@dataclass(frozen=True, slots=True, kw_only=True)
class RobotModelLinkParameters:
    configuration: RobotModelLinkConfiguration
    encoder_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class TrackerEdmTheodoliteUncertainties:
    # Angle in arcseconds.
    theta_dispersion: float
    theta_threshold: float
    # Angle in arcseconds.
    phi_dispersion: float
    phi_threshold: float
    # Value in parts per million.
    distance: float
    distance_threshold: float


@dataclass(frozen=True)
class TransformAxes:
    origin: Vector
    x_axis: Vector
    y_axis: Vector
    z_axis: Vector


@dataclass(frozen=True)
class WorldFixedXyzTransformComponents(FixedXyzTransformComponents):
    scale: float


@dataclass(frozen=True)
class WorldFixedXyzTransformVectors:
    position_in_working: Vector
    orientation_in_working: Vector
    scale: float


__all__ = [
    "CalibrationApplianceNodeStatus",
    "CalloutPosition",
    "ConstructVectorGroupGroupToGroupCompareResult",
    "DeleteCollectionsByWildcardResult",
    "DeleteFoldersByWildcardResult",
    "DriftCheckResult",
    "EulerXyzTransformComponents",
    "EulerZxzTransformComponents",
    "EulerZyxTransformComponents",
    "EulerZyzTransformComponents",
    "EvaluateFeatureCheckResult",
    "EvaluateFeatureChecksResult",
    "FeatureCheckDatumReferencesResult",
    "FitErrorResult",
    "FixedXyzTransformComponents",
    "FixedXyzTransformVectors",
    "GeneralRelationshipStatistics",
    "GetCloudPointCountResult",
    "GetCloudRGBValuesNearPointResult",
    "GetCloudRGBValuesResult",
    "InstrumentBestFitResult",
    "InstrumentModelResult",
    "InstrumentPositionUpdate",
    "InstrumentTargetsAndModeProfiles",
    "InstrumentWeatherSetting",
    "InstrumentXyzUncertainties",
    "LastInstrumentIndexResult",
    "LrSelfTestResult",
    "MeshVolumeResult",
    "PointComparisonResult",
    "PointToPointRelationshipStatistics",
    "PointsToObjectsRelationshipStatistics",
    "RelationshipFitResult",
    "ResetCloudBoundingBoxResult",
    "RobotModelLinkParameters",
    "TrackerEdmTheodoliteUncertainties",
    "TransformAxes",
    "WorldFixedXyzTransformComponents",
    "WorldFixedXyzTransformVectors",
]
