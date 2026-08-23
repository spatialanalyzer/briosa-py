"""Handwritten domain values added for Wave B."""

# ruff: noqa: F405, RUF009  # Reviewed immutable defaults mirror the API contract.
from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import Enum

from briosa.operation_values import *  # noqa: F403


class AxisIdentifier(Enum):
    POSITIVE_X = "+X"
    NEGATIVE_X = "-X"
    POSITIVE_Y = "+Y"
    NEGATIVE_Y = "-Y"
    POSITIVE_Z = "+Z"
    NEGATIVE_Z = "-Z"


class BSplinePointSortMode(str, Enum):
    USE_SELECTION_ORDER = "use_selection_order"
    CLOSEST_NEIGHBORS_FROM_FIRST_SELECTION = "closest_neighbors_from_first_selection"
    CLOSEST_NEIGHBORS_IN_CURVE_DIRECTION = "closest_neighbors_in_curve_direction"


class CircleLineMode(str, Enum):
    CIRCLE = "circle"
    LINE = "line"


class CloudBoxType(str, Enum):
    WORLD_AXIS_ALIGNED_BOX = "worldAxisAlignedBox"
    WORK_AXIS_ALIGNED_BOX = "workAxisAlignedBox"
    MINIMUM_ORIENTED_BOX_UNCONDITIONAL = "minimumOrientedBoxUnconditional"
    MINIMUM_ORIENTED_BOX_VERIFY_VOLUME = "minimumOrientedBoxVerifyVolume"


class CloudThinningMode(str, Enum):
    NONE = "None"
    RANDOM = "Random"
    NTH_POINT = "Nth Point"


class CollimationBaselineMethod(str, Enum):
    DETERMINED_BY_VALUE = "Determined By Value"
    DETERMINED_FROM_SCALE = "Determined From Scale"
    DETERMINED_FROM_KNOWN_POINT = "Determined From Known Point"


class CollimationTiltMode(str, Enum):
    FULL_COLLIMATION = "Full Collimation"
    NO_TILT_COLLIMATION = "No-Tilt Collimation"


class ConstructObjectType(str, Enum):
    ANY = "any"
    CIRCLES = "circles"
    CONES = "cones"
    CYLINDERS = "cylinders"
    LINES = "lines"
    PLANES = "planes"
    SLOTS = "slots"
    SPHERES = "spheres"
    CENTER_POINTS = "center_points"
    SURFACE_POINTS = "surface_points"
    VERTEX_POINTS = "vertex_points"


class DynamicCircleMode(str, Enum):
    CYLINDER_AND_PLANE_HOLD_PLANE_NORMAL = (
        "Cylinder and Plane Intersection - Hold Plane Normal"
    )
    CYLINDER_AND_PLANE_HOLD_CYLINDER_AXIS = (
        "Cylinder and Plane Intersection - Hold Cylinder Axis"
    )
    CONE_AND_PLANE_HOLD_PLANE_NORMAL = "Cone and Plane Intersection - Hold Plane Normal"
    CONE_AND_PLANE_HOLD_CONE_AXIS = "Cone and Plane Intersection - Hold Cone Axis"
    SPHERE_AND_PLANE_INTERSECTION = "Sphere and Plane Intersection"
    TWO_CONES_INTERSECTION = "Two Cones Intersection"
    CONE_AND_CYLINDER_INTERSECTION = "Cone and Cylinder Intersection"


class DynamicEllipseMode(str, Enum):
    CYLINDER_AND_PLANE_INTERSECTION = "Cylinder and Plane Intersection"
    CONE_AND_PLANE_INTERSECTION = "Cone and Plane Intersection"


class DynamicLineMode(str, Enum):
    CONE_AXIS = "Cone Axis"
    CYLINDER_AXIS = "Cylinder Axis"
    INTERSECTION_OF_TWO_PLANES = "Intersection of Two Planes"
    BISECT_TWO_LINES = "Bisect Two Lines"
    SLOT_CENTERLINE_ALONG_LENGTH = "Slot Centerline Along Length"


class DynamicPlaneMode(str, Enum):
    BISECT_TWO_PLANES = "Bisect Two Planes"
    TWO_CONES_HOLD_NORMAL_TO_BEST_FIT_PLANE = (
        "Two Cones Intersection - Hold Normal to Best-Fit Plane"
    )
    TWO_CONES_HOLD_NORMAL_TO_FIRST_CONE_AXIS = (
        "Two Cones Intersection - Hold Normal to First Cone Axis"
    )
    TWO_CONES_HOLD_NORMAL_TO_SECOND_CONE_AXIS = (
        "Two Cones Intersection - Hold Normal to Second Cone Axis"
    )
    CONE_AND_CYLINDER_HOLD_NORMAL_TO_BEST_FIT_PLANE = (
        "Cone and Cylinder Intersection - Hold Normal to Best-Fit Plane"
    )
    CONE_AND_CYLINDER_HOLD_NORMAL_TO_CONE_AXIS = (
        "Cone and Cylinder Intersection - Hold Normal to Cone Axis"
    )
    CONE_AND_CYLINDER_HOLD_NORMAL_TO_CYLINDER_AXIS = (
        "Cone and Cylinder Intersection - Hold Normal to Cylinder Axis"
    )
    OFFSET_PLANE_FROM_PLANE = "Offset Plane From Plane"


class DynamicPointMode(str, Enum):
    INTERSECTION_LINE_AND_PLANE = "Intersection of Line and Plane"
    INTERSECTION_CYLINDER_AND_PLANE = "Intersection of Cylinder and Plane"
    INTERSECTION_CONE_AND_PLANE = "Intersection of Cone and Plane"
    INTERSECTION_THREE_PLANES = "Intersection of Three Planes"
    MID_POINT_PERPENDICULAR_TO_TWO_LINES = "Mid-Point of Perpendicular to Two Lines"


class EdgePointMode(str, Enum):
    INCLUDE_EDGES = "Include Edges"
    EXCLUDE_EDGES = "Exclude Edges"
    EDGES_ONLY = "Edges Only"


class FrameAxis(Enum):
    X = "X"
    Y = "Y"
    Z = "Z"


class FrameConstructionMethod(Enum):
    ORIGIN_X_XY = "Origin,X,XY"
    ORIGIN_X_XZ = "Origin,X,XZ"
    ORIGIN_Y_YX = "Origin,Y,YX"
    ORIGIN_Y_YZ = "Origin,Y,YZ"
    ORIGIN_Z_ZX = "Origin,Z,ZX"
    ORIGIN_X_ZY = "Origin,X,ZY"


class GdtDistanceBetweenMode(Enum):
    CENTROID = "Centroid"
    MIN_MAX = "Min/Max"


class GdtEvaluationMethod(Enum):
    NONE = "None"
    ASME_1994 = "ASME 1994"
    ASME_2009 = "ASME 2009"
    ASME_2018 = "ASME 2018"
    ISO_1983 = "ISO 1983"
    ISO_2004 = "ISO 2004"
    ISO_2017 = "ISO 2017"


class GdtExtendedEvaluationMethod(Enum):
    LEAST_SQUARES = "Least Squares"
    HIGH_POINT = "High Point"
    MINIMUM_SEPARATION = "Minimum Separation"
    LEAST_SQUARES_HIGH_POINT = "Least Squares High Point"
    LEAST_SQUARES_3D = "Least Squares 3D"
    LEAST_SQUARES_HIGH_POINT_1_STD_DEV = "Least Squares High Point 1 STD DEV"
    LEAST_SQUARES_HIGH_POINT_2_STD_DEV = "Least Squares High Point 2 STD DEV"
    LEAST_SQUARES_HIGH_POINT_HALFWAY = "Least Squares High Point Halfway"
    MINIMUM_SEPARATION_HIGH_POINT = "Minimum Separation High Point"
    EQUALIZED_HIGH_POINT = "Equalized High Point"
    EQUALIZED_LSQ_HIGH_POINT = "Equalized LSQ High Point"


class GdtFeatureType(Enum):
    DIAMETER = "diameter"
    RADIUS = "radius"
    DISTANCE_BETWEEN = "distance_between"
    WIDTH = "width"
    LENGTH = "length"
    ANGLE_BETWEEN = "angle_between"
    ANGULARITY = "angularity"
    PERPENDICULARITY = "perpendicularity"
    PARALLELISM = "parallelism"
    CIRCULARITY = "circularity"
    CONCENTRICITY = "concentricity"
    CYLINDRICITY = "cylindricity"
    STRAIGHTNESS = "straightness"
    SURFACE_PROFILE = "surface_profile"
    LINE_PROFILE = "line_profile"
    COMPOSITE_SURFACE_PROFILE = "composite_surface_profile"
    FLATNESS = "flatness"
    TRUE_POSITION = "true_position"
    COMPOSITE_TRUE_POSITION = "composite_true_position"
    CIRCULAR_RUNOUT = "circular_runout"
    TOTAL_RUNOUT = "total_runout"


class GdtToleranceZoneType(Enum):
    NONE = "none"
    CYLINDRICAL = "cylindrical"
    PLANAR = "planar"
    SPHERICAL = "spherical"
    RADIAL_ARC = "radial_arc"
    RADIAL_PLANAR = "radial_planar"
    BOUNDARY = "boundary"
    PLANAR_MEDIAN = "planar_median"
    SURFACE = "surface"


class GeometryRelationshipPointEditMode(str, Enum):
    POINT_LIST = "Point List"
    POINT_GRAPH = "Point Graph"
    SUB_SAMPLER_SETTINGS = "Sub-Sampler Settings"


class InspectionFilter(str, Enum):
    ALL = "ALL"
    CHECKS = "CHECKS"
    DATUMS = "DATUMS"


class InstrumentPositionReportingFrame(str, Enum):
    INSTRUMENT_BASE = "Instrument Base"
    WORLD = "World"
    WORKING = "Working"


class MeshOrientationType(str, Enum):
    USE_CURRENT_POINT_OF_VIEW = "Use Current Point of View"
    USE_CURRENT_WORKING_FRAME = "Use Current Working Frame"


class MirrorFramePlane(str, Enum):
    XY = "xy"
    XZ = "xz"
    YZ = "yz"


class OffsetDirectionType(str, Enum):
    BOTH = "both"
    POSITIVE_ONLY = "positiveOnly"
    NEGATIVE_ONLY = "negativeOnly"


class PointOutputType(str, Enum):
    POINTS = "points"
    CLOUD_POINTS = "cloudPoints"


class RGBColorChannel(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    INTENSITY = "intensity"


class RGBFilterOperation(str, Enum):
    INCREMENTALLY_APPLY_FILTER = "incrementallyApplyFilter"
    RESET_AND_APPLY_FILTER = "resetAndApplyFilter"
    RESET_ALL_CLOUD_POINTS_VISIBLE = "resetAllCloudPointsVisible"


class RobotActiveJointComponent(str, Enum):
    NONE = "NONE"
    X = "X"
    Y = "Y"
    Z = "Z"
    RX = "Rx"
    RY = "Ry"
    RZ = "Rz"
    ALPHA = "Alpha"
    A = "A"
    D = "D"
    THETA = "THETA"


class RobotModelLinkType(str, Enum):
    DH = "DH"
    SIX_DOF = "6DOF"


class ShowUsmnDialog(str, Enum):
    NO = "No"
    YES = "Yes"
    ON_TOLERANCE_VIOLATION = "On Tolerance Violation"


class SolverMode(str, Enum):
    GAUSS_NEWTON = "Gauss-Newton"
    LEVENBERG_MARQUARDT = "Levenberg-Marquardt"
    GAUSS_NEWTON_WITH_GRADIENT_SEARCH = "Gauss-Newton /w Gradient Search"
    DIRECT_SEARCH = "Direct Search"


class SurfaceDissectionMode(Enum):
    ENTIRE_SOLID = "Entire Solid"
    SELECT_FACES = "Select Faces"


class SurveyTargetType(str, Enum):
    TRIANGLE = "Triangle"
    CIRCLE = "Circle"


class SystemString(str, Enum):
    SA_VERSION = "SA Version"
    XIT_FILENAME = "XIT Filename"
    MP_FILENAME = "MP Filename"
    MP_FILENAME_FULL_PATH = "MP Filename (Full Path)"
    DATE_AND_TIME = "Date & Time"
    DATE = "Date"
    DATE_SHORT = "Date (Short)"
    TIME = "Time"
    KEY_SERIAL_NUMBER = "Key Serial Number"
    COMPANY_NAME = "Company Name"
    USER_NAME = "User Name"
    LICENSE_USER_NAME = "License User Name"
    WINDOWS_USER_NAME = "Windows User Name"
    COMPUTER_NAME = "Computer Name"


class TargetComputationMethod(str, Enum):
    USE_MOST_RECENT_SHOT_FROM_EACH_FACE = "Use most recent shot from each face"
    USE_ONLY_MOST_RECENT_SHOT = "Use only most recent shot"
    DO_NOT_CHANGE_PRIOR_MEASUREMENTS = "Do not change prior measurements at all"
    FORCE_NEW_POINT_FOR_EACH_MEASUREMENT = "Force a new point for each measurement"
    REMOVE_ALL_PRIOR_SHOTS = "Remove all prior shots"
    DEACTIVATE_ALL_PRIOR_SHOTS = "Deactivate all prior shots"


class WcfAxis(str, Enum):
    X = "X Axis"
    Y = "Y Axis"
    Z = "Z Axis"


@dataclass(frozen=True, slots=True)
class BSplineFitOptions:
    open_curve: bool = True
    use_interpolation_for_fit: bool = True
    number_of_control_points: int = 8
    degree_of_curve: int = 3
    sort_method: BSplinePointSortMode = BSplinePointSortMode.USE_SELECTION_ORDER
    span_any_gap: bool = True
    termination_gap_length: float = 0.0
    ignore_proximate_points: bool = False
    proximate_point_threshold: float = 0.0
    use_global_tessellation_options: bool = True
    maximum_chordal_deviation: float = 0.05
    maximum_trim_edge_angle: float = 15.0
    termination_average_multiplier: float = 10.0
    extension: float = 0.0


@dataclass(frozen=True, slots=True)
class CalloutViewProperties:
    lock_view_point: bool = False
    recall_working_frame: bool = False
    recall_visible_layer: bool = False
    callout_leader_thickness: int = 2
    callout_leader_color: Color = Color(128, 128, 128)
    callout_border_thickness: int = 2
    callout_border_color: Color = Color(0, 0, 255)
    divide_text_with_lines: bool = False
    font: Font = Font()


@dataclass(frozen=True)
class CloudThinningOptions:
    mode: CloudThinningMode = CloudThinningMode.NTH_POINT
    point_increment: int = 5
    minimum_number_of_points: int = 100
    maximum_number_of_points: int = 20000


@dataclass(frozen=True, slots=True, kw_only=True)
class CloudToCadAlignmentResult:
    rms_deviation: float
    average_deviation: float
    maximum_absolute_deviation: float
    resultant_transform_in_working: Transform


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionMachineId:
    collection_name: str
    machine_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class CurrentTrappingStatus:
    active: bool
    focused_item: CollectionItemName | None
    instrument: CollectionInstrumentId | None


@dataclass(frozen=True, slots=True, kw_only=True)
class DoubleVector6:
    values: list[float]


@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureCheckCylinderEvalOptions:
    enable_actual_diameter_override: bool
    actual_diameter_override: float


@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureCheckDatumReference:
    reference_string: str
    cad_faces: str
    sa_objects: list[CollectionObjectName]
    auxiliary_sa_objects: list[CollectionObjectName]
    geometry_relationships: list[CollectionItemName]
    auxiliary_geometry_relationships: list[CollectionItemName]


@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureCheckReportingOptions:
    show_feature_control_frame_summary: bool
    include_title: bool
    show_datum_and_tolerance_summary: bool
    show_feature_summary: bool
    only_create_failed_vectors: bool
    show_point_details: bool
    show_lower_tier_tables: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class FilterProximitySettings:
    surface_inclusion_proximity: float = 0.1
    edge_exclusion_proximity: float = 0.1
    planar_inclusion_proximity: float = 0.5
    planar_exclusion_proximity: float = 0.1
    radial_inclusion_proximity: float = 0.1
    geometry_extraction_tolerance: float = 0.01
    surface_proximity_mode: OffsetDirectionType = OffsetDirectionType.BOTH
    planar_proximity_mode: OffsetDirectionType = OffsetDirectionType.BOTH
    radial_proximity_mode: OffsetDirectionType = OffsetDirectionType.BOTH
    project_to_plane: bool = True
    assert_plane_boundaries: bool = False


@dataclass(frozen=True, slots=True, kw_only=True)
class FitDofOptions:
    allow_x: bool = True
    allow_y: bool = True
    allow_z: bool = True
    allow_rx: bool = True
    allow_ry: bool = True
    allow_rz: bool = True
    rotate_about_centroid: bool = True


@dataclass(frozen=True, slots=True, kw_only=True)
class GdtMeasurements:
    point_names: list[PointName]
    cloud_names: list[CollectionObjectName]


@dataclass(frozen=True, slots=True, kw_only=True)
class GdtOptions:
    use_high_points: bool
    extrapolate_axial_extent: bool
    exclude_from_auto_evaluation: bool
    distance_between_mode: GdtDistanceBetweenMode | None
    evaluation_method: GdtEvaluationMethod | None
    create_actual_features: bool
    create_solved_points: bool
    cross_section_criteria: float
    enable_auto_feature_detection: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class GeometryRelationshipOutlierFilterMetrics:
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


@dataclass(frozen=True)
class GroupAverageResult:
    rms_deviation: float
    max_absolute_deviation: float
    average_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class InstrumentTargetStatus:
    is_locked: bool
    name: str
    number_of_faces: int
    locked_face: int


@dataclass(frozen=True, slots=True)
class InstrumentTypeName:
    value: str


@dataclass(frozen=True, slots=True, kw_only=True)
class LrFlipTestResult:
    front_range_inches: float
    front_azimuth_degrees: float
    front_elevation_degrees: float
    front_quality: float
    back_range_inches: float
    back_azimuth_degrees: float
    back_elevation_degrees: float
    back_quality: float
    front_back_difference_range_inches: float
    front_back_difference_azimuth_degrees: float
    front_back_difference_elevation_degrees: float


@dataclass(frozen=True, slots=True, kw_only=True)
class LrLoSeparationTestResult:
    primary_lo_index: int
    secondary_lo_index: int
    primary_lo_measurement_count: int
    primary_lo_range_mean_inches: float
    primary_lo_range_standard_deviation_inches: float
    primary_lo_quality_mean: float
    primary_lo_quality_standard_deviation: float
    secondary_lo_measurement_count: int
    secondary_lo_range_mean_inches: float
    secondary_lo_range_standard_deviation_inches: float
    secondary_lo_quality_mean: float
    secondary_lo_quality_standard_deviation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class LrSnrInfo:
    snr: float
    size_of_data_array: int
    peak_value_index: int
    peak_value_db: float
    measured_range_meters: float


@dataclass(frozen=True)
class ObjectOriginResult:
    vector_representation: Vector
    x_value: float
    y_value: float
    z_value: float


@dataclass(frozen=True, slots=True, kw_only=True)
class ObservationInfo:
    instrument: CollectionInstrumentId
    spherical_values: ObservationSphericalValues
    active: bool
    timestamp: str
    rms_error: float
    temperature_fahrenheit: float
    pressure_in_hg: float
    relative_humidity_percent: float
    info_data: str


@dataclass(frozen=True, slots=True, kw_only=True)
class ObservationSphericalValues:
    distance: float
    azimuth: float
    elevation: float


@dataclass(frozen=True, slots=True, kw_only=True)
class PerimeterLists:
    scan_perimeters: list[CollectionObjectName]
    exclusion_perimeters: list[CollectionObjectName]


@dataclass(frozen=True, slots=True, kw_only=True)
class PointsToPointsRelationshipAssociatedData:
    nominal_points: tuple[PointName, ...]
    actual_points: tuple[PointName, ...]


@dataclass(frozen=True)
class ProjectedPointGradient:
    projected_point: Vector
    normal_vector: Vector
    u_direction: Vector
    v_direction: Vector


@dataclass(frozen=True, slots=True, kw_only=True)
class RelationshipAssociatedData:
    relationship_type: str
    individual_points: tuple[PointName, ...]
    point_groups: tuple[CollectionObjectName, ...]
    point_clouds: tuple[CollectionObjectName, ...]
    objects: tuple[CollectionObjectName, ...]


@dataclass(frozen=True, slots=True, kw_only=True)
class RelationshipStatusFlags:
    dormant: bool
    success: bool
    measured: bool
    failed: bool
    unmeasured: bool


@dataclass(frozen=True, slots=True, kw_only=True)
class RelationshipWatchWindowUdpSettings:
    enabled: bool = False
    broadcast: bool = True
    ip_address: str = ""
    port: int = 10000


@dataclass(frozen=True, slots=True, kw_only=True)
class RobotCalibrationMetrics:
    xyz_max: float
    xyz_average: float
    xyz_rms: float
    orient_max: float
    orient_average: float
    orient_rms: float
    robustness: float


@dataclass(frozen=True, slots=True, kw_only=True)
class SigmoidalGapFitConstraints:
    use_sigmoidal_gap_constraints: bool
    minimum_gap_boundary: float
    minimum_gap_weight: float
    maximum_gap_boundary: float
    maximum_gap_weight: float
    nominal_gap: float
    nominal_gap_weight: float
    gradient_steepness_factor: float


@dataclass(frozen=True)
class SurfaceFaceList:
    value: str


@dataclass(frozen=True, slots=True, kw_only=True)
class TcpFixtureUncertainties:
    solution_valid: bool
    refined_tcp_in_working: Transform
    uncertainties_in_tcp_fixture_frame: DoubleVector6
    uncertainties_in_working_frame: DoubleVector6
    rms_error: float
    maximum_absolute_error: float
    goodness_of_fit: float
    robustness: float
    result_notes: list[str]


@dataclass(frozen=True, slots=True, kw_only=True)
class UncertaintyCovarianceMatrix:
    row_1: DoubleVector6
    row_2: DoubleVector6
    row_3: DoubleVector6
    row_4: DoubleVector6
    row_5: DoubleVector6
    row_6: DoubleVector6


@dataclass(frozen=True, slots=True, kw_only=True)
class WrtlChannelStatus:
    connection_status: bool
    active_channel: int


@dataclass(frozen=True)
class MakeGdtDatumAnnotationOptions:
    datum_name: str
    objects: Sequence[CollectionObjectName] = field(default_factory=tuple)
    geometry_relationships: Sequence[CollectionItemName] = field(default_factory=tuple)
    surface_faces: SurfaceFaceList | None = None
    auxiliary_object: CollectionObjectName | None = None
    auxiliary_geometry_relationship: CollectionItemName | None = None
    is_slot: bool = False
    force_surface_feature: bool = False


@dataclass(frozen=True)
class MakeGdtFeatureCheckAnnotationOptions:
    feature_annotation_name: str
    feature_type: GdtFeatureType = GdtFeatureType.TRUE_POSITION
    objects: Sequence[CollectionObjectName] = field(default_factory=tuple)
    geometry_relationships: Sequence[CollectionItemName] = field(default_factory=tuple)
    surface_faces: SurfaceFaceList | None = None
    decompose_multiple_features: bool = False
    auto_create_diameter_checks: bool = False
    auto_create_slot_width_checks: bool = False
    auto_create_slot_length_checks: bool = False
    datum_references: str = ""
    tolerance: str = ""
    is_slot: bool = False
    per_unit_length_or_area: bool = False
    circular_area: bool = False
    per_unit_area_length_distance: float = 0.0
    per_unit_area_length_step_over_percent: float = 50.0
    per_unit_area_width_distance: float = 0.0
    per_unit_area_width_step_over_percent: float = 50.0
    per_unit_area_circle_diameter: float = 0.0
    per_unit_area_diameter_step_over: float = 50.0
    auxiliary_object: CollectionObjectName | None = None
    auxiliary_geometry_relationship: CollectionItemName | None = None
    use_nominal_for_dimension_tolerance: bool = True
    use_reference_object_for_nominal: bool = True
    nominal_dimension_tolerance: float = 0.0
    low_dimension_tolerance: float = -0.1
    high_dimension_tolerance: float = 0.1
    tolerance_zone_type: GdtToleranceZoneType = GdtToleranceZoneType.NONE
    use_projected_tolerance_zone: bool = False
    projected_tolerance_zone: float = 0.0


@dataclass(frozen=True, slots=True, kw_only=True)
class RelationshipWatchWindowTemplateOptions:
    linear_precision: int = 4
    angular_precision: int = 3
    font: Font = Font()
    text_color: Color = Color(red=0, green=0, blue=255)
    background_color: Color = Color(red=255, green=255, blue=255)
    highlight_color: Color = Color(red=255, green=0, blue=0)
    show_deviation_x_rx: bool = True
    show_deviation_y_ry: bool = True
    show_deviation_z_rz: bool = True
    show_deviation_magnitude: bool = True
    udp_network_transmit_settings: RelationshipWatchWindowUdpSettings = (
        RelationshipWatchWindowUdpSettings()
    )
    transparent_background: bool = False
    hide_units: bool = False


@dataclass(frozen=True, slots=True, kw_only=True)
class RobotModelLinkConfiguration:
    link_type: RobotModelLinkType = RobotModelLinkType.DH
    dh_alpha_component: float = 0.0
    dh_a_component: float = 0.0
    dh_d_component: float = 0.0
    dh_theta_component: float = 0.0
    dh_x_axis_deflection_factor: float = 0.0
    dh_y_axis_deflection_factor: float = 0.0
    dh_z_axis_deflection_factor: float = 0.0
    six_dof_x_component: float = 0.0
    six_dof_y_component: float = 0.0
    six_dof_z_component: float = 0.0
    six_dof_rx_component: float = 0.0
    six_dof_ry_component: float = 0.0
    six_dof_rz_component: float = 0.0
    active_joint_component: RobotActiveJointComponent = RobotActiveJointComponent.NONE
    encoder_offset_value: float = 0.0
    minimum_encoder_limit: float = 0.0
    maximum_encoder_limit: float = 0.0
    encoder_sense_negative: bool = False
    include_additional_encoder: bool = False
    additional_encoder_index_offset: int = 0
    additional_encoder_sense_negative: bool = False
    segment_origin_mass_kg: float = 0.0
    segment_cg_mass_kg: float = 0.0
    segment_cg_in_segment: Vector = Vector(0.0, 0.0, 0.0)


__all__ = [
    "AxisIdentifier",
    "BSplineFitOptions",
    "BSplinePointSortMode",
    "CalloutViewProperties",
    "CircleLineMode",
    "CloudBoxType",
    "CloudThinningMode",
    "CloudThinningOptions",
    "CloudToCadAlignmentResult",
    "CollectionMachineId",
    "CollimationBaselineMethod",
    "CollimationTiltMode",
    "ConstructObjectType",
    "CurrentTrappingStatus",
    "DoubleVector6",
    "DynamicCircleMode",
    "DynamicEllipseMode",
    "DynamicLineMode",
    "DynamicPlaneMode",
    "DynamicPointMode",
    "EdgePointMode",
    "FeatureCheckCylinderEvalOptions",
    "FeatureCheckDatumReference",
    "FeatureCheckReportingOptions",
    "FilterProximitySettings",
    "FitDofOptions",
    "FrameAxis",
    "FrameConstructionMethod",
    "GdtDistanceBetweenMode",
    "GdtEvaluationMethod",
    "GdtExtendedEvaluationMethod",
    "GdtFeatureType",
    "GdtMeasurements",
    "GdtOptions",
    "GdtToleranceZoneType",
    "GeometryRelationshipOutlierFilterMetrics",
    "GeometryRelationshipPointEditMode",
    "GroupAverageResult",
    "InspectionFilter",
    "InstrumentPositionReportingFrame",
    "InstrumentTargetStatus",
    "InstrumentTypeName",
    "LrFlipTestResult",
    "LrLoSeparationTestResult",
    "LrSnrInfo",
    "MakeGdtDatumAnnotationOptions",
    "MakeGdtFeatureCheckAnnotationOptions",
    "MeshOrientationType",
    "MirrorFramePlane",
    "ObjectOriginResult",
    "ObservationInfo",
    "ObservationSphericalValues",
    "OffsetDirectionType",
    "PerimeterLists",
    "PointOutputType",
    "PointsToPointsRelationshipAssociatedData",
    "ProjectedPointGradient",
    "RGBColorChannel",
    "RGBFilterOperation",
    "RelationshipAssociatedData",
    "RelationshipStatusFlags",
    "RelationshipWatchWindowTemplateOptions",
    "RelationshipWatchWindowUdpSettings",
    "RobotActiveJointComponent",
    "RobotCalibrationMetrics",
    "RobotModelLinkConfiguration",
    "RobotModelLinkType",
    "ShowUsmnDialog",
    "SigmoidalGapFitConstraints",
    "SolverMode",
    "SurfaceDissectionMode",
    "SurfaceFaceList",
    "SurveyTargetType",
    "SystemString",
    "TargetComputationMethod",
    "TcpFixtureUncertainties",
    "UncertaintyCovarianceMatrix",
    "WcfAxis",
    "WrtlChannelStatus",
]
