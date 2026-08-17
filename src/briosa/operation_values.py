"""Handwritten MP-native values used by the Wave A public API."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import ClassVar


class _StringEnum(str, Enum):
    pass


class AngularUnits(_StringEnum):
    DEGREES = "degrees"
    DEGREES_MINUTES_SECONDS = "degrees_minutes_seconds"
    RADIANS = "radians"
    MILLIRADIANS = "milliradians"
    GONS_GRAD = "gons_grad"
    MILS = "mils"
    ARCSECONDS = "arcseconds"
    DEGREES_MINUTES = "degrees_minutes"
    DEFAULT = DEGREES


class AsciiFileFormat(_StringEnum):
    X_Y_Z = "x_y_z"
    X_Y_Z_OFFSET_OFFSET2 = "x_y_z_offset_offset2"
    X_Y_Z_NOTES = "x_y_z_notes"
    RADIUS_THETA_PHI = "radius_theta_phi"
    RADIUS_THETA_Z = "radius_theta_z"
    POINT_NAME_X_Y_Z = "point_name_x_y_z"
    POINT_NAME_X_Y_Z_NOTES = "point_name_x_y_z_notes"
    POINT_NAME_X_Y_Z_OFFSET_OFFSET2 = "point_name_x_y_z_offset_offset2"
    POINT_NAME_X_Y_Z_UX_UY_UZ = "point_name_x_y_z_ux_uy_uz"
    POINT_NAME_X_Y_Z_TX_TY_TZ_TD = "point_name_x_y_z_tx_ty_tz_td"
    POINT_NAME_X_Y_Z_WX_WY_WZ_WMAG = "point_name_x_y_z_wx_wy_wz_wmag"
    POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE = "point_name_x_y_z_high_low_tolerance"
    POINT_NAME_X_Y_Z_TX_TY_TZ_TD_WX_WY_WZ = "point_name_x_y_z_tx_ty_tz_td_wx_wy_wz"
    POINT_NAME_X_Y_Z_WX_WY_WZ_TX_TY_TZ_TD = "point_name_x_y_z_wx_wy_wz_tx_ty_tz_td"
    POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE_WX_WY_WZ = (
        "point_name_x_y_z_high_low_tolerance_wx_wy_wz"
    )
    POINT_NAME_X_Y_Z_WX_WY_WZ_HIGH_LOW_TOLERANCE = (
        "point_name_x_y_z_wx_wy_wz_high_low_tolerance"
    )
    POINT_NAME_RADIUS_THETA_PHI = "point_name_radius_theta_phi"
    POINT_NAME_RADIUS_THETA_Z = "point_name_radius_theta_z"
    POINT_NAME_X_Y_Z_GROUP_NAME = "point_name_x_y_z_group_name"
    POINT_NAME_Y_X_Z_GROUP_NAME = "point_name_y_x_z_group_name"
    GROUP_NAME_POINT_NAME_X_Y_Z = "group_name_point_name_x_y_z"
    GROUP_NAME_POINT_NAME_X_Y_Z_OFFSET_OFFSET2 = (
        "group_name_point_name_x_y_z_offset_offset2"
    )
    GROUP_NAME_POINT_NAME_X_Y_Z_NOTES = "group_name_point_name_x_y_z_notes"
    GROUP_NAME_POINT_NAME_X_Y_Z_UX_UY_UZ = "group_name_point_name_x_y_z_ux_uy_uz"
    GROUP_NAME_POINT_NAME_RADIUS_THETA_PHI = "group_name_point_name_radius_theta_phi"
    GROUP_NAME_POINT_NAME_RADIUS_THETA_Z = "group_name_point_name_radius_theta_z"
    COLLECTION_GROUP_POINT_X_Y_Z = "collection_group_point_x_y_z"
    COLLECTION_GROUP_POINT_X_Y_Z_NOTES = "collection_group_point_x_y_z_notes"
    COLLECTION_GROUP_POINT_RADIUS_THETA_PHI = "collection_group_point_radius_theta_phi"
    COLLECTION_GROUP_POINT_RADIUS_THETA_Z = "collection_group_point_radius_theta_z"
    X_Y_Z_I_J_K = "x_y_z_i_j_k"
    VECTOR_NAME_X_Y_Z_I_J_K = "vector_name_x_y_z_i_j_k"
    VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE = (
        "vector_name_x_y_z_dx_dy_dz_signed_magnitude"
    )
    VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_I_J_K = (
        "vector_group_name_vector_name_x_y_z_i_j_k"
    )
    VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE = (
        "vector_group_name_vector_name_x_y_z_dx_dy_dz_signed_magnitude"
    )
    FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP = "frame_name_x_y_z_rx_ry_rz_timestamp"
    FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP = "frame_name_x_y_z_euler_x_y_z_timestamp"
    FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP = "frame_name_x_y_z_euler_z_y_x_timestamp"
    FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP = "frame_name_x_y_z_euler_z_y_z_timestamp"
    FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP = "frame_name_x_y_z_euler_z_x_z_timestamp"
    FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP = (
        "frame_name_transformation_matrix_timestamp"
    )
    TRANSFORMATION_MATRIX_TIMESTAMP = "transformation_matrix_timestamp"
    FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP = "frame_name_x_y_z_quaternion_timestamp"
    PLANE_NAME_X_Y_Z_DX_DY_DZ_PLANE_SIZE = "plane_name_x_y_z_dx_dy_dz_plane_size"


class ChartType(_StringEnum):
    RUN_CHART = "run_chart"
    INDIVIDUAL_X_MOVING_RANGE = "individual_x_moving_range"
    BULLSEYE_CHART = "bullseye_chart"


class CoordinateSystemType(_StringEnum):
    CARTESIAN = "cartesian"
    CYLINDRIC = "cylindric"
    POLAR = "polar"
    DEFAULT = CARTESIAN


class DatasetType(_StringEnum):
    X = "x"
    Y = "y"
    Z = "z"
    MAGNITUDE = "magnitude"


class DistanceUnits(_StringEnum):
    METERS = "meters"
    CENTIMETERS = "centimeters"
    MILLIMETERS = "millimeters"
    FEET = "feet"
    INCHES = "inches"
    US_SURVEY_FEET = "us_survey_feet"


class ExportDataDelimeterType(_StringEnum):
    SPACE = "space"
    COMMA = "comma"
    TAB = "tab"


class ExportTargetNameFormat(_StringEnum):
    COLLECTION_GROUP_TARGET = "collection_group_target"
    GROUP_TARGET = "group_target"
    TARGET = "target"
    NONE = "none"


class ExportVectorNameFormat(_StringEnum):
    COLLECTION_GROUP_VECTOR = "collection_group_vector"
    GROUP_VECTOR = "group_vector"
    VECTOR = "vector"
    NONE = "none"


class BaseColorType(_StringEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class BaseMidColorType(_StringEnum):
    RED = "red"
    GREEN = "green"
    GRAY = "gray"
    BLUE = "blue"


class ColorRangeMethod(_StringEnum):
    SINGLE_COLOR = "single_color"
    CONTINUOUS = "continuous"
    TOLERANCED_CONTINUOUS = "toleranced_continuous"
    TOLERANCED_GO_NO_GO = "toleranced_go_no_go"
    TOLERANCED_GO_NO_GO_WITH_WARNING = "toleranced_go_no_go_with_warning"
    DISCRETE_COLORS = "discrete_colors"


class GeometryType(_StringEnum):
    LINE = "line"
    PLANE = "plane"
    CIRCLE = "circle"
    SPHERE = "sphere"
    CYLINDER = "cylinder"
    CONE = "cone"
    PARABOLOID = "paraboloid"
    ELLIPSE = "ellipse"
    SLOT = "slot"
    TORUS = "torus"


class ObjectType(_StringEnum):
    ANY = "any"
    B_SPLINE = "b_spline"
    CIRCLE = "circle"
    CLOUD = "cloud"
    ENHANCED_CLOUD = "enhanced_cloud"
    SCAN_STRIPE_CLOUD = "scan_stripe_cloud"
    CROSS_SECTION_CLOUD = "cross_section_cloud"
    CONE = "cone"
    CYLINDER = "cylinder"
    DATUM = "datum"
    ELLIPSE = "ellipse"
    FRAME = "frame"
    FRAME_SET = "frame_set"
    LINE = "line"
    PARABOLOID = "paraboloid"
    PERIMETER = "perimeter"
    PLANE = "plane"
    POINT_GROUP = "point_group"
    POINT_SET = "point_set"
    POLY_SURFACE = "poly_surface"
    SCAN_STRIPE_MESH = "scan_stripe_mesh"
    SLOT = "slot"
    SPHERE = "sphere"
    SURFACE = "surface"
    TORUS = "torus"
    VECTOR_GROUP = "vector_group"
    DEFAULT = ANY


class ItemType(_StringEnum):
    ANY = "any"
    ALIGNMENT = "alignment"
    ANNOTATION = "annotation"
    B_SPLINE = "b_spline"
    CALIBRATION_APPLIANCE_NODE = "calibration_appliance_node"
    CALLOUT_VIEW = "callout_view"
    CHART = "chart"
    CIRCLE = "circle"
    CLOUD = "cloud"
    ENHANCED_CLOUD = "enhanced_cloud"
    SCAN_STRIPE_CLOUD = "scan_stripe_cloud"
    CROSS_SECTION_CLOUD = "cross_section_cloud"
    CONE = "cone"
    CYLINDER = "cylinder"
    DATUM = "datum"
    DIMENSION = "dimension"
    ELLIPSE = "ellipse"
    EVENT = "event"
    FEATURE_CHECK = "feature_check"
    FRAME = "frame"
    FRAME_SET = "frame_set"
    LINE = "line"
    PARABOLOID = "paraboloid"
    PERIMETER = "perimeter"
    PICTURE = "picture"
    PLANE = "plane"
    POINT_GROUP = "point_group"
    POINT_SET = "point_set"
    POLY_SURFACE = "poly_surface"
    RELATIONSHIP = "relationship"
    SA_DOC = "sa_doc"
    SA_REPORT = "sa_report"
    SA_REPORT_TEMPLATE = "sa_report_template"
    SCALE_BAR = "scale_bar"
    SCAN_STRIPE_MESH = "scan_stripe_mesh"
    SLOT = "slot"
    SPHERE = "sphere"
    SURFACE = "surface"
    TABLE = "table"
    TCP_FIXTURE = "tcp_fixture"
    TORUS = "torus"
    VECTOR_GROUP = "vector_group"


class PointFilterInputType(_StringEnum):
    CARDINAL_POINTS = "cardinal_points"
    INPUT_POINTS = "input_points"
    NOMINAL_CARDINAL_POINTS = "nominal_cardinal_points"
    DEFAULT = CARDINAL_POINTS


class RelWeightingMode(_StringEnum):
    NORMALIZE_EQUATION_COUNT = "normalize_equation_count"
    NORMALIZE_EQUATION_COUNT_AND_TOLERANCE_WIDTH = (
        "normalize_equation_count_and_tolerance_width"
    )
    RESET_ALL_WEIGHTS = "reset_all_weights"
    NORMALIZE_SQUARE_ROOT_EQUATION_COUNT = "normalize_square_root_equation_count"
    NORMALIZE_SQUARE_ROOT_AND_TOLERANCE_WIDTH = (
        "normalize_square_root_and_tolerance_width"
    )
    DEFAULT = NORMALIZE_EQUATION_COUNT


class RenderModeType(_StringEnum):
    WIREFRAME = "wireframe"
    HIDDEN_LINE_REMOVED = "hidden_line_removed"
    SOLID_AND_EDGES = "solid_and_edges"
    SOLID = "solid"
    DEFAULT = WIREFRAME


class ReportOutputType(_StringEnum):
    NONE = "none"
    SA_REPORT = "sa_report"
    SA_DOCUMENT = "sa_document"
    PDF = "pdf"
    RTF = "rtf"


class ReportPageSettings(_StringEnum):
    PORTRAIT = "portrait"
    LANDSCAPE = "landscape"
    DEFAULT = PORTRAIT


class ReportViewType(_StringEnum):
    NONE = "none"
    CURRENT_VIEW = "current_view"
    CALLOUT_VIEW = "callout_view"


class SurfaceAnalysisMode(_StringEnum):
    NONE = "none"
    RELATIONSHIP = "relationship"
    NORMALS = "normals"
    CURVATURE = "curvature"
    DEVIATION_RMS = "deviation_rms"
    DEVIATION_MAX = "deviation_max"
    DEVIATION_AVERAGE = "deviation_average"
    DEVIATION_MIN = "deviation_min"
    DEVIATION_MAX_ABSOLUTE = "deviation_max_absolute"
    DEVIATION_MAX_DELTA = "deviation_max_delta"
    PSEUDO_SURFACE = "pseudo_surface"
    DEFAULT = RELATIONSHIP


class TemperatureUnits(_StringEnum):
    FAHRENHEIT = "fahrenheit"
    CELSIUS = "celsius"
    DEFAULT = FAHRENHEIT


class TranslucencyType(_StringEnum):
    SOLID = "solid"
    TRANSLUCENT = "translucent"
    WIREFRAME = "wireframe"


class CompTechnique(_StringEnum):
    STANDARD = "standard"
    MAX_INSCRIBED = "max_inscribed"
    MIN_CIRCUMSCRIBED = "min_circumscribed"
    DEFAULT = STANDARD


class DegreeOfFreedom(_StringEnum):
    ANY = "any"
    LOCK_FOCUS_LOCATION = "lock_focus_location"
    LOCK_VERTEX_LOCATION = "lock_vertex_location"
    DEFAULT = ANY


class FitMethod(_StringEnum):
    MINIMUM_RMS = "minimum_rms"
    BEST_AXIS = "best_axis"
    DEFAULT = MINIMUM_RMS


class MeasuredSideForPlanarOffset(_StringEnum):
    ABOVE_PLANE = "above_plane"
    PROBE_CENTER = "probe_center"
    BELOW_PLANE = "below_plane"
    DEFAULT = ABOVE_PLANE


class MeasuredSideForRadialOffset(_StringEnum):
    INSIDE = "inside"
    PROBE_CENTER = "probe_center"
    OUTSIDE = "outside"
    DEFAULT = OUTSIDE


class MpDialogInteractionMode(_StringEnum):
    BLOCK_APPLICATION_INTERACTION = "block_application_interaction"
    ALLOW_APPLICATION_INTERACTION = "allow_application_interaction"


class MpInteractionMode(_StringEnum):
    HALT_ON_FAILURE_ONLY = "halt_on_failure_only"
    HALT_ON_FAILURE_OR_PARTIAL_SUCCESS = "halt_on_failure_or_partial_success"
    NEVER_HALT = "never_halt"


class NormalDirection(_StringEnum):
    PROBING_DIRECTION = "probing_direction"
    WORKING_ORIGIN_POSITIVE = "working_origin_positive"
    RIGHT_HAND_RULE = "right_hand_rule"
    DEFAULT = PROBING_DIRECTION


class SaInteractionMode(_StringEnum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    SILENT = "silent"


class SlotType(_StringEnum):
    ROUND = "round"
    SQUARE = "square"
    DEFAULT = ROUND


class SphereFitComputationMode(_StringEnum):
    STANDARD = "standard"
    MAX_INSCRIBED = "max_inscribed"
    MIN_CIRCUMSCRIBED = "min_circumscribed"
    DEFAULT = STANDARD


class WindowState(_StringEnum):
    MAXIMIZE = "maximize"
    MINIMIZE = "minimize"
    RESTORE = "restore"
    SHOW = "show"
    HIDE = "hide"


@dataclass(frozen=True, slots=True, kw_only=True)
class ChartName:
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionName:
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class FrameName:
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class ViewName:
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class PointName:
    collection_name: str
    group_name: str
    target_name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionInstrumentId:
    collection_name: str
    instrument_id: int


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionGroupName:
    collection_name: str
    group_name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionObjectName:
    collection_name: str
    object_name: str
    object_type: ObjectType


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionItemName:
    collection_name: str
    item_name: str
    item_type: ItemType | None = None


@dataclass(frozen=True, slots=True, kw_only=True)
class CollectionVectorGroupName:
    collection_name: str
    vector_group_name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class VectorName:
    collection_name: str
    group_name: str
    name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class Vector:
    x: float
    y: float
    z: float


@dataclass(frozen=True, slots=True, kw_only=True)
class Transform:
    values: tuple[float, ...]

    def __post_init__(self) -> None:
        if len(self.values) != 16:
            raise ValueError("Transform.values must contain exactly 16 values")


@dataclass(frozen=True, slots=True, kw_only=True)
class WorldTransform:
    transform: Transform
    scale_factor: float


@dataclass(frozen=True, slots=True, kw_only=True)
class Color:
    red: int
    green: int
    blue: int

    def __post_init__(self) -> None:
        if any(value < 0 or value > 255 for value in (self.red, self.green, self.blue)):
            raise ValueError("Color channels must be in 0..255")


@dataclass(frozen=True, slots=True, kw_only=True)
class ColorizationOptions:
    color_range_method: ColorRangeMethod = ColorRangeMethod.CONTINUOUS
    base_high_color: BaseColorType = BaseColorType.BLUE
    base_mid_color: BaseMidColorType = BaseMidColorType.GREEN
    base_low_color: BaseColorType = BaseColorType.RED
    draw_tubes: bool = False
    draw_arrowheads: bool = True
    indicate_values: bool = False
    vector_magnification: float = 100.0
    vector_width: int = 1
    draw_blotches: bool = False
    blotch_size: float = 0.1
    show_out_of_tolerance_only: bool = False
    show_color_bar_in_view: bool = False
    show_color_bar_percentages: bool = True
    show_color_bar_fractions: bool = False
    high_saturation_limit: float = 0.5
    low_saturation_limit: float = -0.5
    high_tolerance: float = 0.03
    low_tolerance: float = -0.03
    DEFAULT: ClassVar[ColorizationOptions]


@dataclass(frozen=True, slots=True, kw_only=True)
class FileReference:
    path: str
    embedded_file: bool = False


@dataclass(frozen=True, slots=True, kw_only=True)
class Font:
    font_name: str = "MS Shell Dlg"
    size: int = 8
    color: Color = field(default_factory=lambda: Color(red=0, green=0, blue=0))
    DEFAULT: ClassVar[Font]


@dataclass(frozen=True, slots=True, kw_only=True)
class ScalarToleranceLimit:
    enabled: bool = False
    value: float = 0.0


@dataclass(frozen=True, slots=True, kw_only=True)
class ToleranceLimit:
    enabled: bool = False
    value: float = 0.0


@dataclass(frozen=True, slots=True, kw_only=True)
class ToleranceVectorOptions:
    high_x: ToleranceLimit = field(default_factory=ToleranceLimit)
    high_y: ToleranceLimit = field(default_factory=ToleranceLimit)
    high_z: ToleranceLimit = field(default_factory=ToleranceLimit)
    high_magnitude: ToleranceLimit = field(default_factory=ToleranceLimit)
    low_x: ToleranceLimit = field(default_factory=ToleranceLimit)
    low_y: ToleranceLimit = field(default_factory=ToleranceLimit)
    low_z: ToleranceLimit = field(default_factory=ToleranceLimit)
    low_magnitude: ToleranceLimit = field(default_factory=ToleranceLimit)


@dataclass(frozen=True, slots=True, kw_only=True)
class FitConstraintScalarOptions:
    high: ScalarToleranceLimit = field(default_factory=ScalarToleranceLimit)
    low: ScalarToleranceLimit = field(default_factory=ScalarToleranceLimit)
    DEFAULT: ClassVar[FitConstraintScalarOptions]


@dataclass(frozen=True, slots=True, kw_only=True)
class ToleranceScalarOptions:
    high: ScalarToleranceLimit = field(default_factory=ScalarToleranceLimit)
    low: ScalarToleranceLimit = field(default_factory=ScalarToleranceLimit)
    DEFAULT: ClassVar[ToleranceScalarOptions]


@dataclass(frozen=True, slots=True, kw_only=True)
class EmbeddedReportFile:
    collection_name: str
    file_name: str


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportOutputOptions:
    output_type: ReportOutputType
    external_path: str | None = None
    embedded_file: EmbeddedReportFile | None = None
    DEFAULT: ClassVar[ReportOutputOptions]

    def __post_init__(self) -> None:
        if self.external_path is not None and self.embedded_file is not None:
            raise ValueError("Only one report-output destination may be supplied")


@dataclass(frozen=True, slots=True, kw_only=True)
class ReportViewOptions:
    view_type: ReportViewType
    collection_name: str = ""
    callout_name: str = ""


@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectionOptions:
    projection_type: str = "Object To Probe Vectors"
    ignore_edge_projections: bool = False
    override_target_offsets: bool = False
    override_target_offsets_value: float = 0.0
    add_extra_material_thickness: bool = False
    extra_material_thickness_value: float = 0.0
    DEFAULT: ClassVar[ProjectionOptions]


@dataclass(frozen=True, slots=True, kw_only=True)
class PointDeltaReportOptions:
    coordinate_system: CoordinateSystemType = CoordinateSystemType.CARTESIAN
    details_format: str = "Single"
    show_point_a: bool = True
    show_point_b: bool = True
    show_delta: bool = True
    show_magnitude: bool = True
    show_component_1: bool = True
    show_component_2: bool = True
    show_component_3: bool = True
    sort_point_names: bool = False
    show_tolerance_fields: bool = True
    colorize_in_tolerance_fields: bool = True
    DEFAULT: ClassVar[PointDeltaReportOptions]


ColorizationOptions.DEFAULT = ColorizationOptions()
Font.DEFAULT = Font()
FitConstraintScalarOptions.DEFAULT = FitConstraintScalarOptions()
ToleranceScalarOptions.DEFAULT = ToleranceScalarOptions()
ProjectionOptions.DEFAULT = ProjectionOptions()
PointDeltaReportOptions.DEFAULT = PointDeltaReportOptions()
ReportOutputOptions.DEFAULT = ReportOutputOptions(
    output_type=ReportOutputType.SA_REPORT,
    embedded_file=EmbeddedReportFile(collection_name="", file_name="My Report"),
)

__all__ = [
    "AngularUnits",
    "AsciiFileFormat",
    "BaseColorType",
    "BaseMidColorType",
    "ChartName",
    "ChartType",
    "CollectionGroupName",
    "CollectionInstrumentId",
    "CollectionItemName",
    "CollectionName",
    "CollectionObjectName",
    "CollectionVectorGroupName",
    "Color",
    "ColorRangeMethod",
    "ColorizationOptions",
    "CompTechnique",
    "CoordinateSystemType",
    "DatasetType",
    "DegreeOfFreedom",
    "DistanceUnits",
    "EmbeddedReportFile",
    "ExportDataDelimeterType",
    "ExportTargetNameFormat",
    "ExportVectorNameFormat",
    "FileReference",
    "FitConstraintScalarOptions",
    "FitMethod",
    "Font",
    "FrameName",
    "GeometryType",
    "ItemType",
    "MeasuredSideForPlanarOffset",
    "MeasuredSideForRadialOffset",
    "MpDialogInteractionMode",
    "MpInteractionMode",
    "NormalDirection",
    "ObjectType",
    "PointDeltaReportOptions",
    "PointFilterInputType",
    "PointName",
    "ProjectionOptions",
    "RelWeightingMode",
    "RenderModeType",
    "ReportOutputOptions",
    "ReportOutputType",
    "ReportPageSettings",
    "ReportViewOptions",
    "ReportViewType",
    "SaInteractionMode",
    "ScalarToleranceLimit",
    "SlotType",
    "SphereFitComputationMode",
    "SurfaceAnalysisMode",
    "TemperatureUnits",
    "ToleranceLimit",
    "ToleranceScalarOptions",
    "ToleranceVectorOptions",
    "Transform",
    "TranslucencyType",
    "Vector",
    "VectorName",
    "ViewName",
    "WindowState",
    "WorldTransform",
]
