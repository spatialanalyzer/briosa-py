from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AngularUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANGULAR_UNITS_UNSPECIFIED: _ClassVar[AngularUnits]
    ANGULAR_UNITS_DEGREES: _ClassVar[AngularUnits]
    ANGULAR_UNITS_DEGREES_MINUTES_SECONDS: _ClassVar[AngularUnits]
    ANGULAR_UNITS_RADIANS: _ClassVar[AngularUnits]
    ANGULAR_UNITS_MILLIRADIANS: _ClassVar[AngularUnits]
    ANGULAR_UNITS_GONS_GRAD: _ClassVar[AngularUnits]
    ANGULAR_UNITS_MILS: _ClassVar[AngularUnits]
    ANGULAR_UNITS_ARCSECONDS: _ClassVar[AngularUnits]
    ANGULAR_UNITS_DEGREES_MINUTES: _ClassVar[AngularUnits]

class AsciiFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASCII_FILE_FORMAT_UNSPECIFIED: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_X_Y_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_X_Y_Z_NOTES: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_RADIUS_THETA_PHI: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_RADIUS_THETA_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_NOTES: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_UX_UY_UZ: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_WMAG: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD_WX_WY_WZ: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_TX_TY_TZ_TD: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE_WX_WY_WZ: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_HIGH_LOW_TOLERANCE: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_RADIUS_THETA_PHI: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_RADIUS_THETA_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_GROUP_NAME: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_POINT_NAME_Y_X_Z_GROUP_NAME: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_NOTES: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_UX_UY_UZ: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_PHI: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z_NOTES: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_PHI: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_Z: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_X_Y_Z_I_J_K: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_VECTOR_NAME_X_Y_Z_I_J_K: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_I_J_K: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: _ClassVar[AsciiFileFormat]
    ASCII_FILE_FORMAT_PLANE_NAME_X_Y_Z_DX_DY_DZ_PLANE_SIZE: _ClassVar[AsciiFileFormat]

class ChartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHART_TYPE_UNSPECIFIED: _ClassVar[ChartType]
    CHART_TYPE_RUN_CHART: _ClassVar[ChartType]
    CHART_TYPE_INDIVIDUAL_X_MOVING_RANGE: _ClassVar[ChartType]
    CHART_TYPE_BULLSEYE_CHART: _ClassVar[ChartType]

class CoordinateSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COORDINATE_SYSTEM_TYPE_UNSPECIFIED: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_CARTESIAN: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_CYLINDRIC: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_POLAR: _ClassVar[CoordinateSystemType]

class DatasetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATASET_TYPE_UNSPECIFIED: _ClassVar[DatasetType]
    DATASET_TYPE_X: _ClassVar[DatasetType]
    DATASET_TYPE_Y: _ClassVar[DatasetType]
    DATASET_TYPE_Z: _ClassVar[DatasetType]
    DATASET_TYPE_MAGNITUDE: _ClassVar[DatasetType]

class DistanceUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISTANCE_UNITS_UNSPECIFIED: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_METERS: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_CENTIMETERS: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_MILLIMETERS: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_FEET: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_INCHES: _ClassVar[DistanceUnits]
    DISTANCE_UNITS_US_SURVEY_FEET: _ClassVar[DistanceUnits]

class ExportDataDelimeterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_DATA_DELIMETER_TYPE_UNSPECIFIED: _ClassVar[ExportDataDelimeterType]
    EXPORT_DATA_DELIMETER_TYPE_SPACE: _ClassVar[ExportDataDelimeterType]
    EXPORT_DATA_DELIMETER_TYPE_COMMA: _ClassVar[ExportDataDelimeterType]
    EXPORT_DATA_DELIMETER_TYPE_TAB: _ClassVar[ExportDataDelimeterType]

class ExportTargetNameFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_TARGET_NAME_FORMAT_UNSPECIFIED: _ClassVar[ExportTargetNameFormat]
    EXPORT_TARGET_NAME_FORMAT_COLLECTION_GROUP_TARGET: _ClassVar[ExportTargetNameFormat]
    EXPORT_TARGET_NAME_FORMAT_GROUP_TARGET: _ClassVar[ExportTargetNameFormat]
    EXPORT_TARGET_NAME_FORMAT_TARGET: _ClassVar[ExportTargetNameFormat]
    EXPORT_TARGET_NAME_FORMAT_NONE: _ClassVar[ExportTargetNameFormat]

class ExportVectorNameFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_VECTOR_NAME_FORMAT_UNSPECIFIED: _ClassVar[ExportVectorNameFormat]
    EXPORT_VECTOR_NAME_FORMAT_COLLECTION_GROUP_VECTOR: _ClassVar[ExportVectorNameFormat]
    EXPORT_VECTOR_NAME_FORMAT_GROUP_VECTOR: _ClassVar[ExportVectorNameFormat]
    EXPORT_VECTOR_NAME_FORMAT_VECTOR: _ClassVar[ExportVectorNameFormat]
    EXPORT_VECTOR_NAME_FORMAT_NONE: _ClassVar[ExportVectorNameFormat]

class BaseColorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASE_COLOR_TYPE_UNSPECIFIED: _ClassVar[BaseColorType]
    BASE_COLOR_TYPE_RED: _ClassVar[BaseColorType]
    BASE_COLOR_TYPE_GREEN: _ClassVar[BaseColorType]
    BASE_COLOR_TYPE_BLUE: _ClassVar[BaseColorType]

class BaseMidColorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASE_MID_COLOR_TYPE_UNSPECIFIED: _ClassVar[BaseMidColorType]
    BASE_MID_COLOR_TYPE_RED: _ClassVar[BaseMidColorType]
    BASE_MID_COLOR_TYPE_GREEN: _ClassVar[BaseMidColorType]
    BASE_MID_COLOR_TYPE_GRAY: _ClassVar[BaseMidColorType]
    BASE_MID_COLOR_TYPE_BLUE: _ClassVar[BaseMidColorType]

class ColorRangeMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLOR_RANGE_METHOD_UNSPECIFIED: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_SINGLE_COLOR: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_CONTINUOUS: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_CONTINUOUS: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO_WITH_WARNING: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_DISCRETE_COLORS: _ClassVar[ColorRangeMethod]

class GeometryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GEOMETRY_TYPE_UNSPECIFIED: _ClassVar[GeometryType]
    GEOMETRY_TYPE_LINE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_PLANE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_CIRCLE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_SPHERE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_CYLINDER: _ClassVar[GeometryType]
    GEOMETRY_TYPE_CONE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_PARABOLOID: _ClassVar[GeometryType]
    GEOMETRY_TYPE_ELLIPSE: _ClassVar[GeometryType]
    GEOMETRY_TYPE_SLOT: _ClassVar[GeometryType]
    GEOMETRY_TYPE_TORUS: _ClassVar[GeometryType]

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_TYPE_UNSPECIFIED: _ClassVar[ObjectType]
    OBJECT_TYPE_ANY: _ClassVar[ObjectType]
    OBJECT_TYPE_B_SPLINE: _ClassVar[ObjectType]
    OBJECT_TYPE_CIRCLE: _ClassVar[ObjectType]
    OBJECT_TYPE_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_ENHANCED_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_SCAN_STRIPE_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_CROSS_SECTION_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_CONE: _ClassVar[ObjectType]
    OBJECT_TYPE_CYLINDER: _ClassVar[ObjectType]
    OBJECT_TYPE_DATUM: _ClassVar[ObjectType]
    OBJECT_TYPE_ELLIPSE: _ClassVar[ObjectType]
    OBJECT_TYPE_FRAME: _ClassVar[ObjectType]
    OBJECT_TYPE_FRAME_SET: _ClassVar[ObjectType]
    OBJECT_TYPE_LINE: _ClassVar[ObjectType]
    OBJECT_TYPE_PARABOLOID: _ClassVar[ObjectType]
    OBJECT_TYPE_PERIMETER: _ClassVar[ObjectType]
    OBJECT_TYPE_PLANE: _ClassVar[ObjectType]
    OBJECT_TYPE_POINT_GROUP: _ClassVar[ObjectType]
    OBJECT_TYPE_POINT_SET: _ClassVar[ObjectType]
    OBJECT_TYPE_POLY_SURFACE: _ClassVar[ObjectType]
    OBJECT_TYPE_SCAN_STRIPE_MESH: _ClassVar[ObjectType]
    OBJECT_TYPE_SLOT: _ClassVar[ObjectType]
    OBJECT_TYPE_SPHERE: _ClassVar[ObjectType]
    OBJECT_TYPE_SURFACE: _ClassVar[ObjectType]
    OBJECT_TYPE_TORUS: _ClassVar[ObjectType]
    OBJECT_TYPE_VECTOR_GROUP: _ClassVar[ObjectType]

class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ITEM_TYPE_UNSPECIFIED: _ClassVar[ItemType]
    ITEM_TYPE_ANY: _ClassVar[ItemType]
    ITEM_TYPE_ALIGNMENT: _ClassVar[ItemType]
    ITEM_TYPE_ANNOTATION: _ClassVar[ItemType]
    ITEM_TYPE_B_SPLINE: _ClassVar[ItemType]
    ITEM_TYPE_CALIBRATION_APPLIANCE_NODE: _ClassVar[ItemType]
    ITEM_TYPE_CALLOUT_VIEW: _ClassVar[ItemType]
    ITEM_TYPE_CHART: _ClassVar[ItemType]
    ITEM_TYPE_CIRCLE: _ClassVar[ItemType]
    ITEM_TYPE_CLOUD: _ClassVar[ItemType]
    ITEM_TYPE_ENHANCED_CLOUD: _ClassVar[ItemType]
    ITEM_TYPE_SCAN_STRIPE_CLOUD: _ClassVar[ItemType]
    ITEM_TYPE_CROSS_SECTION_CLOUD: _ClassVar[ItemType]
    ITEM_TYPE_CONE: _ClassVar[ItemType]
    ITEM_TYPE_CYLINDER: _ClassVar[ItemType]
    ITEM_TYPE_DATUM: _ClassVar[ItemType]
    ITEM_TYPE_DIMENSION: _ClassVar[ItemType]
    ITEM_TYPE_ELLIPSE: _ClassVar[ItemType]
    ITEM_TYPE_EVENT: _ClassVar[ItemType]
    ITEM_TYPE_FEATURE_CHECK: _ClassVar[ItemType]
    ITEM_TYPE_FRAME: _ClassVar[ItemType]
    ITEM_TYPE_FRAME_SET: _ClassVar[ItemType]
    ITEM_TYPE_LINE: _ClassVar[ItemType]
    ITEM_TYPE_PARABOLOID: _ClassVar[ItemType]
    ITEM_TYPE_PERIMETER: _ClassVar[ItemType]
    ITEM_TYPE_PICTURE: _ClassVar[ItemType]
    ITEM_TYPE_PLANE: _ClassVar[ItemType]
    ITEM_TYPE_POINT_GROUP: _ClassVar[ItemType]
    ITEM_TYPE_POINT_SET: _ClassVar[ItemType]
    ITEM_TYPE_POLY_SURFACE: _ClassVar[ItemType]
    ITEM_TYPE_RELATIONSHIP: _ClassVar[ItemType]
    ITEM_TYPE_SA_DOC: _ClassVar[ItemType]
    ITEM_TYPE_SA_REPORT: _ClassVar[ItemType]
    ITEM_TYPE_SA_REPORT_TEMPLATE: _ClassVar[ItemType]
    ITEM_TYPE_SCALE_BAR: _ClassVar[ItemType]
    ITEM_TYPE_SCAN_STRIPE_MESH: _ClassVar[ItemType]
    ITEM_TYPE_SLOT: _ClassVar[ItemType]
    ITEM_TYPE_SPHERE: _ClassVar[ItemType]
    ITEM_TYPE_SURFACE: _ClassVar[ItemType]
    ITEM_TYPE_TABLE: _ClassVar[ItemType]
    ITEM_TYPE_TCP_FIXTURE: _ClassVar[ItemType]
    ITEM_TYPE_TORUS: _ClassVar[ItemType]
    ITEM_TYPE_VECTOR_GROUP: _ClassVar[ItemType]

class PointFilterInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POINT_FILTER_INPUT_TYPE_UNSPECIFIED: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_CARDINAL_POINTS: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_INPUT_POINTS: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_NOMINAL_CARDINAL_POINTS: _ClassVar[PointFilterInputType]

class RelWeightingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REL_WEIGHTING_MODE_UNSPECIFIED: _ClassVar[RelWeightingMode]
    REL_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT: _ClassVar[RelWeightingMode]
    REL_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT_AND_TOLERANCE_WIDTH: _ClassVar[RelWeightingMode]
    REL_WEIGHTING_MODE_RESET_ALL_WEIGHTS: _ClassVar[RelWeightingMode]
    REL_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_EQUATION_COUNT: _ClassVar[RelWeightingMode]
    REL_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_AND_TOLERANCE_WIDTH: _ClassVar[RelWeightingMode]

class RenderModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RENDER_MODE_TYPE_UNSPECIFIED: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_WIREFRAME: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_HIDDEN_LINE_REMOVED: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_SOLID_AND_EDGES: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_SOLID: _ClassVar[RenderModeType]

class ReportOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_OUTPUT_TYPE_UNSPECIFIED: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_NONE: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_SA_REPORT: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_SA_DOCUMENT: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_PDF: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_RTF: _ClassVar[ReportOutputType]

class ReportPageSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_PAGE_SETTINGS_UNSPECIFIED: _ClassVar[ReportPageSettings]
    REPORT_PAGE_SETTINGS_PORTRAIT: _ClassVar[ReportPageSettings]
    REPORT_PAGE_SETTINGS_LANDSCAPE: _ClassVar[ReportPageSettings]

class ReportViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_VIEW_TYPE_UNSPECIFIED: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_NONE: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_CURRENT_VIEW: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_CALLOUT_VIEW: _ClassVar[ReportViewType]

class SurfaceAnalysisMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SURFACE_ANALYSIS_MODE_UNSPECIFIED: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_NONE: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_RELATIONSHIP: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_NORMALS: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_CURVATURE: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_RMS: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_MAX: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_AVERAGE: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_MIN: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_MAX_ABSOLUTE: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_DEVIATION_MAX_DELTA: _ClassVar[SurfaceAnalysisMode]
    SURFACE_ANALYSIS_MODE_PSEUDO_SURFACE: _ClassVar[SurfaceAnalysisMode]

class TemperatureUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE_UNITS_UNSPECIFIED: _ClassVar[TemperatureUnits]
    TEMPERATURE_UNITS_FAHRENHEIT: _ClassVar[TemperatureUnits]
    TEMPERATURE_UNITS_CELSIUS: _ClassVar[TemperatureUnits]

class TranslucencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSLUCENCY_TYPE_UNSPECIFIED: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_SOLID: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_TRANSLUCENT: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_WIREFRAME: _ClassVar[TranslucencyType]

class CompTechnique(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMP_TECHNIQUE_UNSPECIFIED: _ClassVar[CompTechnique]
    COMP_TECHNIQUE_STANDARD: _ClassVar[CompTechnique]
    COMP_TECHNIQUE_MAX_INSCRIBED: _ClassVar[CompTechnique]
    COMP_TECHNIQUE_MIN_CIRCUMSCRIBED: _ClassVar[CompTechnique]

class DegreeOfFreedom(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEGREE_OF_FREEDOM_UNSPECIFIED: _ClassVar[DegreeOfFreedom]
    DEGREE_OF_FREEDOM_ANY: _ClassVar[DegreeOfFreedom]
    DEGREE_OF_FREEDOM_LOCK_FOCUS_LOCATION: _ClassVar[DegreeOfFreedom]
    DEGREE_OF_FREEDOM_LOCK_VERTEX_LOCATION: _ClassVar[DegreeOfFreedom]

class FitMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FIT_METHOD_UNSPECIFIED: _ClassVar[FitMethod]
    FIT_METHOD_MINIMUM_RMS: _ClassVar[FitMethod]
    FIT_METHOD_BEST_AXIS: _ClassVar[FitMethod]

class MeasuredSideForPlanarOffset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEASURED_SIDE_FOR_PLANAR_OFFSET_UNSPECIFIED: _ClassVar[MeasuredSideForPlanarOffset]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_ABOVE_PLANE: _ClassVar[MeasuredSideForPlanarOffset]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_PROBE_CENTER: _ClassVar[MeasuredSideForPlanarOffset]
    MEASURED_SIDE_FOR_PLANAR_OFFSET_BELOW_PLANE: _ClassVar[MeasuredSideForPlanarOffset]

class MeasuredSideForRadialOffset(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MEASURED_SIDE_FOR_RADIAL_OFFSET_UNSPECIFIED: _ClassVar[MeasuredSideForRadialOffset]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_INSIDE: _ClassVar[MeasuredSideForRadialOffset]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_PROBE_CENTER: _ClassVar[MeasuredSideForRadialOffset]
    MEASURED_SIDE_FOR_RADIAL_OFFSET_OUTSIDE: _ClassVar[MeasuredSideForRadialOffset]

class MpDialogInteractionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP_DIALOG_INTERACTION_MODE_UNSPECIFIED: _ClassVar[MpDialogInteractionMode]
    MP_DIALOG_INTERACTION_MODE_BLOCK_APPLICATION_INTERACTION: _ClassVar[MpDialogInteractionMode]
    MP_DIALOG_INTERACTION_MODE_ALLOW_APPLICATION_INTERACTION: _ClassVar[MpDialogInteractionMode]

class MpInteractionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MP_INTERACTION_MODE_UNSPECIFIED: _ClassVar[MpInteractionMode]
    MP_INTERACTION_MODE_HALT_ON_FAILURE_ONLY: _ClassVar[MpInteractionMode]
    MP_INTERACTION_MODE_HALT_ON_FAILURE_OR_PARTIAL_SUCCESS: _ClassVar[MpInteractionMode]
    MP_INTERACTION_MODE_NEVER_HALT: _ClassVar[MpInteractionMode]

class NormalDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NORMAL_DIRECTION_UNSPECIFIED: _ClassVar[NormalDirection]
    NORMAL_DIRECTION_PROBING_DIRECTION: _ClassVar[NormalDirection]
    NORMAL_DIRECTION_WORKING_ORIGIN_POSITIVE: _ClassVar[NormalDirection]
    NORMAL_DIRECTION_RIGHT_HAND_RULE: _ClassVar[NormalDirection]

class SaInteractionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SA_INTERACTION_MODE_UNSPECIFIED: _ClassVar[SaInteractionMode]
    SA_INTERACTION_MODE_MANUAL: _ClassVar[SaInteractionMode]
    SA_INTERACTION_MODE_AUTOMATIC: _ClassVar[SaInteractionMode]
    SA_INTERACTION_MODE_SILENT: _ClassVar[SaInteractionMode]

class SlotType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SLOT_TYPE_UNSPECIFIED: _ClassVar[SlotType]
    SLOT_TYPE_ROUND: _ClassVar[SlotType]
    SLOT_TYPE_SQUARE: _ClassVar[SlotType]

class SphereFitComputationMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPHERE_FIT_COMPUTATION_MODE_UNSPECIFIED: _ClassVar[SphereFitComputationMode]
    SPHERE_FIT_COMPUTATION_MODE_STANDARD: _ClassVar[SphereFitComputationMode]
    SPHERE_FIT_COMPUTATION_MODE_MAX_INSCRIBED: _ClassVar[SphereFitComputationMode]
    SPHERE_FIT_COMPUTATION_MODE_MIN_CIRCUMSCRIBED: _ClassVar[SphereFitComputationMode]

class WindowState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WINDOW_STATE_UNSPECIFIED: _ClassVar[WindowState]
    WINDOW_STATE_MAXIMIZE: _ClassVar[WindowState]
    WINDOW_STATE_MINIMIZE: _ClassVar[WindowState]
    WINDOW_STATE_RESTORE: _ClassVar[WindowState]
    WINDOW_STATE_SHOW: _ClassVar[WindowState]
    WINDOW_STATE_HIDE: _ClassVar[WindowState]
ANGULAR_UNITS_UNSPECIFIED: AngularUnits
ANGULAR_UNITS_DEGREES: AngularUnits
ANGULAR_UNITS_DEGREES_MINUTES_SECONDS: AngularUnits
ANGULAR_UNITS_RADIANS: AngularUnits
ANGULAR_UNITS_MILLIRADIANS: AngularUnits
ANGULAR_UNITS_GONS_GRAD: AngularUnits
ANGULAR_UNITS_MILS: AngularUnits
ANGULAR_UNITS_ARCSECONDS: AngularUnits
ANGULAR_UNITS_DEGREES_MINUTES: AngularUnits
ASCII_FILE_FORMAT_UNSPECIFIED: AsciiFileFormat
ASCII_FILE_FORMAT_X_Y_Z: AsciiFileFormat
ASCII_FILE_FORMAT_X_Y_Z_OFFSET_OFFSET2: AsciiFileFormat
ASCII_FILE_FORMAT_X_Y_Z_NOTES: AsciiFileFormat
ASCII_FILE_FORMAT_RADIUS_THETA_PHI: AsciiFileFormat
ASCII_FILE_FORMAT_RADIUS_THETA_Z: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_NOTES: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_UX_UY_UZ: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_WMAG: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD_WX_WY_WZ: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_TX_TY_TZ_TD: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE_WX_WY_WZ: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_HIGH_LOW_TOLERANCE: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_RADIUS_THETA_PHI: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_RADIUS_THETA_Z: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_X_Y_Z_GROUP_NAME: AsciiFileFormat
ASCII_FILE_FORMAT_POINT_NAME_Y_X_Z_GROUP_NAME: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_NOTES: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_UX_UY_UZ: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_PHI: AsciiFileFormat
ASCII_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_Z: AsciiFileFormat
ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z: AsciiFileFormat
ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z_NOTES: AsciiFileFormat
ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_PHI: AsciiFileFormat
ASCII_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_Z: AsciiFileFormat
ASCII_FILE_FORMAT_X_Y_Z_I_J_K: AsciiFileFormat
ASCII_FILE_FORMAT_VECTOR_NAME_X_Y_Z_I_J_K: AsciiFileFormat
ASCII_FILE_FORMAT_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: AsciiFileFormat
ASCII_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_I_J_K: AsciiFileFormat
ASCII_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: AsciiFileFormat
ASCII_FILE_FORMAT_PLANE_NAME_X_Y_Z_DX_DY_DZ_PLANE_SIZE: AsciiFileFormat
CHART_TYPE_UNSPECIFIED: ChartType
CHART_TYPE_RUN_CHART: ChartType
CHART_TYPE_INDIVIDUAL_X_MOVING_RANGE: ChartType
CHART_TYPE_BULLSEYE_CHART: ChartType
COORDINATE_SYSTEM_TYPE_UNSPECIFIED: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_CARTESIAN: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_CYLINDRIC: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_POLAR: CoordinateSystemType
DATASET_TYPE_UNSPECIFIED: DatasetType
DATASET_TYPE_X: DatasetType
DATASET_TYPE_Y: DatasetType
DATASET_TYPE_Z: DatasetType
DATASET_TYPE_MAGNITUDE: DatasetType
DISTANCE_UNITS_UNSPECIFIED: DistanceUnits
DISTANCE_UNITS_METERS: DistanceUnits
DISTANCE_UNITS_CENTIMETERS: DistanceUnits
DISTANCE_UNITS_MILLIMETERS: DistanceUnits
DISTANCE_UNITS_FEET: DistanceUnits
DISTANCE_UNITS_INCHES: DistanceUnits
DISTANCE_UNITS_US_SURVEY_FEET: DistanceUnits
EXPORT_DATA_DELIMETER_TYPE_UNSPECIFIED: ExportDataDelimeterType
EXPORT_DATA_DELIMETER_TYPE_SPACE: ExportDataDelimeterType
EXPORT_DATA_DELIMETER_TYPE_COMMA: ExportDataDelimeterType
EXPORT_DATA_DELIMETER_TYPE_TAB: ExportDataDelimeterType
EXPORT_TARGET_NAME_FORMAT_UNSPECIFIED: ExportTargetNameFormat
EXPORT_TARGET_NAME_FORMAT_COLLECTION_GROUP_TARGET: ExportTargetNameFormat
EXPORT_TARGET_NAME_FORMAT_GROUP_TARGET: ExportTargetNameFormat
EXPORT_TARGET_NAME_FORMAT_TARGET: ExportTargetNameFormat
EXPORT_TARGET_NAME_FORMAT_NONE: ExportTargetNameFormat
EXPORT_VECTOR_NAME_FORMAT_UNSPECIFIED: ExportVectorNameFormat
EXPORT_VECTOR_NAME_FORMAT_COLLECTION_GROUP_VECTOR: ExportVectorNameFormat
EXPORT_VECTOR_NAME_FORMAT_GROUP_VECTOR: ExportVectorNameFormat
EXPORT_VECTOR_NAME_FORMAT_VECTOR: ExportVectorNameFormat
EXPORT_VECTOR_NAME_FORMAT_NONE: ExportVectorNameFormat
BASE_COLOR_TYPE_UNSPECIFIED: BaseColorType
BASE_COLOR_TYPE_RED: BaseColorType
BASE_COLOR_TYPE_GREEN: BaseColorType
BASE_COLOR_TYPE_BLUE: BaseColorType
BASE_MID_COLOR_TYPE_UNSPECIFIED: BaseMidColorType
BASE_MID_COLOR_TYPE_RED: BaseMidColorType
BASE_MID_COLOR_TYPE_GREEN: BaseMidColorType
BASE_MID_COLOR_TYPE_GRAY: BaseMidColorType
BASE_MID_COLOR_TYPE_BLUE: BaseMidColorType
COLOR_RANGE_METHOD_UNSPECIFIED: ColorRangeMethod
COLOR_RANGE_METHOD_SINGLE_COLOR: ColorRangeMethod
COLOR_RANGE_METHOD_CONTINUOUS: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_CONTINUOUS: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO_WITH_WARNING: ColorRangeMethod
COLOR_RANGE_METHOD_DISCRETE_COLORS: ColorRangeMethod
GEOMETRY_TYPE_UNSPECIFIED: GeometryType
GEOMETRY_TYPE_LINE: GeometryType
GEOMETRY_TYPE_PLANE: GeometryType
GEOMETRY_TYPE_CIRCLE: GeometryType
GEOMETRY_TYPE_SPHERE: GeometryType
GEOMETRY_TYPE_CYLINDER: GeometryType
GEOMETRY_TYPE_CONE: GeometryType
GEOMETRY_TYPE_PARABOLOID: GeometryType
GEOMETRY_TYPE_ELLIPSE: GeometryType
GEOMETRY_TYPE_SLOT: GeometryType
GEOMETRY_TYPE_TORUS: GeometryType
OBJECT_TYPE_UNSPECIFIED: ObjectType
OBJECT_TYPE_ANY: ObjectType
OBJECT_TYPE_B_SPLINE: ObjectType
OBJECT_TYPE_CIRCLE: ObjectType
OBJECT_TYPE_CLOUD: ObjectType
OBJECT_TYPE_ENHANCED_CLOUD: ObjectType
OBJECT_TYPE_SCAN_STRIPE_CLOUD: ObjectType
OBJECT_TYPE_CROSS_SECTION_CLOUD: ObjectType
OBJECT_TYPE_CONE: ObjectType
OBJECT_TYPE_CYLINDER: ObjectType
OBJECT_TYPE_DATUM: ObjectType
OBJECT_TYPE_ELLIPSE: ObjectType
OBJECT_TYPE_FRAME: ObjectType
OBJECT_TYPE_FRAME_SET: ObjectType
OBJECT_TYPE_LINE: ObjectType
OBJECT_TYPE_PARABOLOID: ObjectType
OBJECT_TYPE_PERIMETER: ObjectType
OBJECT_TYPE_PLANE: ObjectType
OBJECT_TYPE_POINT_GROUP: ObjectType
OBJECT_TYPE_POINT_SET: ObjectType
OBJECT_TYPE_POLY_SURFACE: ObjectType
OBJECT_TYPE_SCAN_STRIPE_MESH: ObjectType
OBJECT_TYPE_SLOT: ObjectType
OBJECT_TYPE_SPHERE: ObjectType
OBJECT_TYPE_SURFACE: ObjectType
OBJECT_TYPE_TORUS: ObjectType
OBJECT_TYPE_VECTOR_GROUP: ObjectType
ITEM_TYPE_UNSPECIFIED: ItemType
ITEM_TYPE_ANY: ItemType
ITEM_TYPE_ALIGNMENT: ItemType
ITEM_TYPE_ANNOTATION: ItemType
ITEM_TYPE_B_SPLINE: ItemType
ITEM_TYPE_CALIBRATION_APPLIANCE_NODE: ItemType
ITEM_TYPE_CALLOUT_VIEW: ItemType
ITEM_TYPE_CHART: ItemType
ITEM_TYPE_CIRCLE: ItemType
ITEM_TYPE_CLOUD: ItemType
ITEM_TYPE_ENHANCED_CLOUD: ItemType
ITEM_TYPE_SCAN_STRIPE_CLOUD: ItemType
ITEM_TYPE_CROSS_SECTION_CLOUD: ItemType
ITEM_TYPE_CONE: ItemType
ITEM_TYPE_CYLINDER: ItemType
ITEM_TYPE_DATUM: ItemType
ITEM_TYPE_DIMENSION: ItemType
ITEM_TYPE_ELLIPSE: ItemType
ITEM_TYPE_EVENT: ItemType
ITEM_TYPE_FEATURE_CHECK: ItemType
ITEM_TYPE_FRAME: ItemType
ITEM_TYPE_FRAME_SET: ItemType
ITEM_TYPE_LINE: ItemType
ITEM_TYPE_PARABOLOID: ItemType
ITEM_TYPE_PERIMETER: ItemType
ITEM_TYPE_PICTURE: ItemType
ITEM_TYPE_PLANE: ItemType
ITEM_TYPE_POINT_GROUP: ItemType
ITEM_TYPE_POINT_SET: ItemType
ITEM_TYPE_POLY_SURFACE: ItemType
ITEM_TYPE_RELATIONSHIP: ItemType
ITEM_TYPE_SA_DOC: ItemType
ITEM_TYPE_SA_REPORT: ItemType
ITEM_TYPE_SA_REPORT_TEMPLATE: ItemType
ITEM_TYPE_SCALE_BAR: ItemType
ITEM_TYPE_SCAN_STRIPE_MESH: ItemType
ITEM_TYPE_SLOT: ItemType
ITEM_TYPE_SPHERE: ItemType
ITEM_TYPE_SURFACE: ItemType
ITEM_TYPE_TABLE: ItemType
ITEM_TYPE_TCP_FIXTURE: ItemType
ITEM_TYPE_TORUS: ItemType
ITEM_TYPE_VECTOR_GROUP: ItemType
POINT_FILTER_INPUT_TYPE_UNSPECIFIED: PointFilterInputType
POINT_FILTER_INPUT_TYPE_CARDINAL_POINTS: PointFilterInputType
POINT_FILTER_INPUT_TYPE_INPUT_POINTS: PointFilterInputType
POINT_FILTER_INPUT_TYPE_NOMINAL_CARDINAL_POINTS: PointFilterInputType
REL_WEIGHTING_MODE_UNSPECIFIED: RelWeightingMode
REL_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT: RelWeightingMode
REL_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT_AND_TOLERANCE_WIDTH: RelWeightingMode
REL_WEIGHTING_MODE_RESET_ALL_WEIGHTS: RelWeightingMode
REL_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_EQUATION_COUNT: RelWeightingMode
REL_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_AND_TOLERANCE_WIDTH: RelWeightingMode
RENDER_MODE_TYPE_UNSPECIFIED: RenderModeType
RENDER_MODE_TYPE_WIREFRAME: RenderModeType
RENDER_MODE_TYPE_HIDDEN_LINE_REMOVED: RenderModeType
RENDER_MODE_TYPE_SOLID_AND_EDGES: RenderModeType
RENDER_MODE_TYPE_SOLID: RenderModeType
REPORT_OUTPUT_TYPE_UNSPECIFIED: ReportOutputType
REPORT_OUTPUT_TYPE_NONE: ReportOutputType
REPORT_OUTPUT_TYPE_SA_REPORT: ReportOutputType
REPORT_OUTPUT_TYPE_SA_DOCUMENT: ReportOutputType
REPORT_OUTPUT_TYPE_PDF: ReportOutputType
REPORT_OUTPUT_TYPE_RTF: ReportOutputType
REPORT_PAGE_SETTINGS_UNSPECIFIED: ReportPageSettings
REPORT_PAGE_SETTINGS_PORTRAIT: ReportPageSettings
REPORT_PAGE_SETTINGS_LANDSCAPE: ReportPageSettings
REPORT_VIEW_TYPE_UNSPECIFIED: ReportViewType
REPORT_VIEW_TYPE_NONE: ReportViewType
REPORT_VIEW_TYPE_CURRENT_VIEW: ReportViewType
REPORT_VIEW_TYPE_CALLOUT_VIEW: ReportViewType
SURFACE_ANALYSIS_MODE_UNSPECIFIED: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_NONE: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_RELATIONSHIP: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_NORMALS: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_CURVATURE: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_RMS: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_MAX: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_AVERAGE: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_MIN: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_MAX_ABSOLUTE: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_DEVIATION_MAX_DELTA: SurfaceAnalysisMode
SURFACE_ANALYSIS_MODE_PSEUDO_SURFACE: SurfaceAnalysisMode
TEMPERATURE_UNITS_UNSPECIFIED: TemperatureUnits
TEMPERATURE_UNITS_FAHRENHEIT: TemperatureUnits
TEMPERATURE_UNITS_CELSIUS: TemperatureUnits
TRANSLUCENCY_TYPE_UNSPECIFIED: TranslucencyType
TRANSLUCENCY_TYPE_SOLID: TranslucencyType
TRANSLUCENCY_TYPE_TRANSLUCENT: TranslucencyType
TRANSLUCENCY_TYPE_WIREFRAME: TranslucencyType
COMP_TECHNIQUE_UNSPECIFIED: CompTechnique
COMP_TECHNIQUE_STANDARD: CompTechnique
COMP_TECHNIQUE_MAX_INSCRIBED: CompTechnique
COMP_TECHNIQUE_MIN_CIRCUMSCRIBED: CompTechnique
DEGREE_OF_FREEDOM_UNSPECIFIED: DegreeOfFreedom
DEGREE_OF_FREEDOM_ANY: DegreeOfFreedom
DEGREE_OF_FREEDOM_LOCK_FOCUS_LOCATION: DegreeOfFreedom
DEGREE_OF_FREEDOM_LOCK_VERTEX_LOCATION: DegreeOfFreedom
FIT_METHOD_UNSPECIFIED: FitMethod
FIT_METHOD_MINIMUM_RMS: FitMethod
FIT_METHOD_BEST_AXIS: FitMethod
MEASURED_SIDE_FOR_PLANAR_OFFSET_UNSPECIFIED: MeasuredSideForPlanarOffset
MEASURED_SIDE_FOR_PLANAR_OFFSET_ABOVE_PLANE: MeasuredSideForPlanarOffset
MEASURED_SIDE_FOR_PLANAR_OFFSET_PROBE_CENTER: MeasuredSideForPlanarOffset
MEASURED_SIDE_FOR_PLANAR_OFFSET_BELOW_PLANE: MeasuredSideForPlanarOffset
MEASURED_SIDE_FOR_RADIAL_OFFSET_UNSPECIFIED: MeasuredSideForRadialOffset
MEASURED_SIDE_FOR_RADIAL_OFFSET_INSIDE: MeasuredSideForRadialOffset
MEASURED_SIDE_FOR_RADIAL_OFFSET_PROBE_CENTER: MeasuredSideForRadialOffset
MEASURED_SIDE_FOR_RADIAL_OFFSET_OUTSIDE: MeasuredSideForRadialOffset
MP_DIALOG_INTERACTION_MODE_UNSPECIFIED: MpDialogInteractionMode
MP_DIALOG_INTERACTION_MODE_BLOCK_APPLICATION_INTERACTION: MpDialogInteractionMode
MP_DIALOG_INTERACTION_MODE_ALLOW_APPLICATION_INTERACTION: MpDialogInteractionMode
MP_INTERACTION_MODE_UNSPECIFIED: MpInteractionMode
MP_INTERACTION_MODE_HALT_ON_FAILURE_ONLY: MpInteractionMode
MP_INTERACTION_MODE_HALT_ON_FAILURE_OR_PARTIAL_SUCCESS: MpInteractionMode
MP_INTERACTION_MODE_NEVER_HALT: MpInteractionMode
NORMAL_DIRECTION_UNSPECIFIED: NormalDirection
NORMAL_DIRECTION_PROBING_DIRECTION: NormalDirection
NORMAL_DIRECTION_WORKING_ORIGIN_POSITIVE: NormalDirection
NORMAL_DIRECTION_RIGHT_HAND_RULE: NormalDirection
SA_INTERACTION_MODE_UNSPECIFIED: SaInteractionMode
SA_INTERACTION_MODE_MANUAL: SaInteractionMode
SA_INTERACTION_MODE_AUTOMATIC: SaInteractionMode
SA_INTERACTION_MODE_SILENT: SaInteractionMode
SLOT_TYPE_UNSPECIFIED: SlotType
SLOT_TYPE_ROUND: SlotType
SLOT_TYPE_SQUARE: SlotType
SPHERE_FIT_COMPUTATION_MODE_UNSPECIFIED: SphereFitComputationMode
SPHERE_FIT_COMPUTATION_MODE_STANDARD: SphereFitComputationMode
SPHERE_FIT_COMPUTATION_MODE_MAX_INSCRIBED: SphereFitComputationMode
SPHERE_FIT_COMPUTATION_MODE_MIN_CIRCUMSCRIBED: SphereFitComputationMode
WINDOW_STATE_UNSPECIFIED: WindowState
WINDOW_STATE_MAXIMIZE: WindowState
WINDOW_STATE_MINIMIZE: WindowState
WINDOW_STATE_RESTORE: WindowState
WINDOW_STATE_SHOW: WindowState
WINDOW_STATE_HIDE: WindowState

class ChartName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CollectionName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class FrameName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ViewName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class PointName(_message.Message):
    __slots__ = ("collection_name", "group_name", "target_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    target_name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ..., target_name: _Optional[str] = ...) -> None: ...

class CollectionInstrumentId(_message.Message):
    __slots__ = ("collection_name", "instrument_id")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    instrument_id: int
    def __init__(self, collection_name: _Optional[str] = ..., instrument_id: _Optional[int] = ...) -> None: ...

class CollectionGroupName(_message.Message):
    __slots__ = ("collection_name", "group_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...

class CollectionObjectName(_message.Message):
    __slots__ = ("collection_name", "object_name", "object_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    object_name: str
    object_type: ObjectType
    def __init__(self, collection_name: _Optional[str] = ..., object_name: _Optional[str] = ..., object_type: _Optional[_Union[ObjectType, str]] = ...) -> None: ...

class CollectionItemName(_message.Message):
    __slots__ = ("collection_name", "item_name", "item_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    item_name: str
    item_type: ItemType
    def __init__(self, collection_name: _Optional[str] = ..., item_name: _Optional[str] = ..., item_type: _Optional[_Union[ItemType, str]] = ...) -> None: ...

class CollectionVectorGroupName(_message.Message):
    __slots__ = ("collection_name", "vector_group_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    vector_group_name: str
    def __init__(self, collection_name: _Optional[str] = ..., vector_group_name: _Optional[str] = ...) -> None: ...

class VectorName(_message.Message):
    __slots__ = ("collection_name", "group_name", "name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class Vector(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class Transform(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class WorldTransform(_message.Message):
    __slots__ = ("transform", "scale_factor")
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    transform: Transform
    scale_factor: float
    def __init__(self, transform: _Optional[_Union[Transform, _Mapping]] = ..., scale_factor: _Optional[float] = ...) -> None: ...

class Color(_message.Message):
    __slots__ = ("red", "green", "blue")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class ColorizationOptions(_message.Message):
    __slots__ = ("color_range_method", "base_high_color", "base_mid_color", "base_low_color", "draw_tubes", "draw_arrowheads", "indicate_values", "vector_magnification", "vector_width", "draw_blotches", "blotch_size", "show_out_of_tolerance_only", "show_color_bar_in_view", "show_color_bar_percentages", "show_color_bar_fractions", "high_saturation_limit", "low_saturation_limit", "high_tolerance", "low_tolerance")
    COLOR_RANGE_METHOD_FIELD_NUMBER: _ClassVar[int]
    BASE_HIGH_COLOR_FIELD_NUMBER: _ClassVar[int]
    BASE_MID_COLOR_FIELD_NUMBER: _ClassVar[int]
    BASE_LOW_COLOR_FIELD_NUMBER: _ClassVar[int]
    DRAW_TUBES_FIELD_NUMBER: _ClassVar[int]
    DRAW_ARROWHEADS_FIELD_NUMBER: _ClassVar[int]
    INDICATE_VALUES_FIELD_NUMBER: _ClassVar[int]
    VECTOR_MAGNIFICATION_FIELD_NUMBER: _ClassVar[int]
    VECTOR_WIDTH_FIELD_NUMBER: _ClassVar[int]
    DRAW_BLOTCHES_FIELD_NUMBER: _ClassVar[int]
    BLOTCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    SHOW_OUT_OF_TOLERANCE_ONLY_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLOR_BAR_IN_VIEW_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLOR_BAR_PERCENTAGES_FIELD_NUMBER: _ClassVar[int]
    SHOW_COLOR_BAR_FRACTIONS_FIELD_NUMBER: _ClassVar[int]
    HIGH_SATURATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    LOW_SATURATION_LIMIT_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    color_range_method: ColorRangeMethod
    base_high_color: BaseColorType
    base_mid_color: BaseMidColorType
    base_low_color: BaseColorType
    draw_tubes: bool
    draw_arrowheads: bool
    indicate_values: bool
    vector_magnification: float
    vector_width: int
    draw_blotches: bool
    blotch_size: float
    show_out_of_tolerance_only: bool
    show_color_bar_in_view: bool
    show_color_bar_percentages: bool
    show_color_bar_fractions: bool
    high_saturation_limit: float
    low_saturation_limit: float
    high_tolerance: float
    low_tolerance: float
    def __init__(self, color_range_method: _Optional[_Union[ColorRangeMethod, str]] = ..., base_high_color: _Optional[_Union[BaseColorType, str]] = ..., base_mid_color: _Optional[_Union[BaseMidColorType, str]] = ..., base_low_color: _Optional[_Union[BaseColorType, str]] = ..., draw_tubes: bool = ..., draw_arrowheads: bool = ..., indicate_values: bool = ..., vector_magnification: _Optional[float] = ..., vector_width: _Optional[int] = ..., draw_blotches: bool = ..., blotch_size: _Optional[float] = ..., show_out_of_tolerance_only: bool = ..., show_color_bar_in_view: bool = ..., show_color_bar_percentages: bool = ..., show_color_bar_fractions: bool = ..., high_saturation_limit: _Optional[float] = ..., low_saturation_limit: _Optional[float] = ..., high_tolerance: _Optional[float] = ..., low_tolerance: _Optional[float] = ...) -> None: ...

class FileReference(_message.Message):
    __slots__ = ("path", "embedded_file")
    PATH_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_FILE_FIELD_NUMBER: _ClassVar[int]
    path: str
    embedded_file: bool
    def __init__(self, path: _Optional[str] = ..., embedded_file: bool = ...) -> None: ...

class Font(_message.Message):
    __slots__ = ("font_name", "size", "color")
    FONT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    font_name: str
    size: int
    color: Color
    def __init__(self, font_name: _Optional[str] = ..., size: _Optional[int] = ..., color: _Optional[_Union[Color, _Mapping]] = ...) -> None: ...

class ScalarToleranceLimit(_message.Message):
    __slots__ = ("enabled", "value")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    value: float
    def __init__(self, enabled: bool = ..., value: _Optional[float] = ...) -> None: ...

class ToleranceLimit(_message.Message):
    __slots__ = ("enabled", "value")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    value: float
    def __init__(self, enabled: bool = ..., value: _Optional[float] = ...) -> None: ...

class ToleranceVectorOptions(_message.Message):
    __slots__ = ("high_x", "high_y", "high_z", "high_magnitude", "low_x", "low_y", "low_z", "low_magnitude")
    HIGH_X_FIELD_NUMBER: _ClassVar[int]
    HIGH_Y_FIELD_NUMBER: _ClassVar[int]
    HIGH_Z_FIELD_NUMBER: _ClassVar[int]
    HIGH_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    LOW_X_FIELD_NUMBER: _ClassVar[int]
    LOW_Y_FIELD_NUMBER: _ClassVar[int]
    LOW_Z_FIELD_NUMBER: _ClassVar[int]
    LOW_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    high_x: ToleranceLimit
    high_y: ToleranceLimit
    high_z: ToleranceLimit
    high_magnitude: ToleranceLimit
    low_x: ToleranceLimit
    low_y: ToleranceLimit
    low_z: ToleranceLimit
    low_magnitude: ToleranceLimit
    def __init__(self, high_x: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_y: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_z: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_magnitude: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_x: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_y: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_z: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_magnitude: _Optional[_Union[ToleranceLimit, _Mapping]] = ...) -> None: ...

class FitConstraintScalarOptions(_message.Message):
    __slots__ = ("high", "low")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: ScalarToleranceLimit
    low: ScalarToleranceLimit
    def __init__(self, high: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ..., low: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ...) -> None: ...

class ToleranceScalarOptions(_message.Message):
    __slots__ = ("high", "low")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: ScalarToleranceLimit
    low: ScalarToleranceLimit
    def __init__(self, high: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ..., low: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ...) -> None: ...

class EmbeddedReportFile(_message.Message):
    __slots__ = ("collection_name", "file_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    file_name: str
    def __init__(self, collection_name: _Optional[str] = ..., file_name: _Optional[str] = ...) -> None: ...

class ReportOutputOptions(_message.Message):
    __slots__ = ("output_type", "external_path", "embedded_file")
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_PATH_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_FILE_FIELD_NUMBER: _ClassVar[int]
    output_type: ReportOutputType
    external_path: str
    embedded_file: EmbeddedReportFile
    def __init__(self, output_type: _Optional[_Union[ReportOutputType, str]] = ..., external_path: _Optional[str] = ..., embedded_file: _Optional[_Union[EmbeddedReportFile, _Mapping]] = ...) -> None: ...

class ReportViewOptions(_message.Message):
    __slots__ = ("view_type", "collection_name", "callout_name")
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_NAME_FIELD_NUMBER: _ClassVar[int]
    view_type: ReportViewType
    collection_name: str
    callout_name: str
    def __init__(self, view_type: _Optional[_Union[ReportViewType, str]] = ..., collection_name: _Optional[str] = ..., callout_name: _Optional[str] = ...) -> None: ...

class ProjectionOptions(_message.Message):
    __slots__ = ("projection_type", "ignore_edge_projections", "override_target_offsets", "override_target_offsets_value", "add_extra_material_thickness", "extra_material_thickness_value")
    PROJECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_EDGE_PROJECTIONS_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TARGET_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_TARGET_OFFSETS_VALUE_FIELD_NUMBER: _ClassVar[int]
    ADD_EXTRA_MATERIAL_THICKNESS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_MATERIAL_THICKNESS_VALUE_FIELD_NUMBER: _ClassVar[int]
    projection_type: str
    ignore_edge_projections: bool
    override_target_offsets: bool
    override_target_offsets_value: float
    add_extra_material_thickness: bool
    extra_material_thickness_value: float
    def __init__(self, projection_type: _Optional[str] = ..., ignore_edge_projections: bool = ..., override_target_offsets: bool = ..., override_target_offsets_value: _Optional[float] = ..., add_extra_material_thickness: bool = ..., extra_material_thickness_value: _Optional[float] = ...) -> None: ...

class PointDeltaReportOptions(_message.Message):
    __slots__ = ("coordinate_system", "details_format", "show_point_a", "show_point_b", "show_delta", "show_magnitude", "show_component_1", "show_component_2", "show_component_3", "sort_point_names", "show_tolerance_fields", "colorize_in_tolerance_fields")
    COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_A_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_B_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELTA_FIELD_NUMBER: _ClassVar[int]
    SHOW_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    SHOW_COMPONENT_1_FIELD_NUMBER: _ClassVar[int]
    SHOW_COMPONENT_2_FIELD_NUMBER: _ClassVar[int]
    SHOW_COMPONENT_3_FIELD_NUMBER: _ClassVar[int]
    SORT_POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    SHOW_TOLERANCE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    COLORIZE_IN_TOLERANCE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    coordinate_system: CoordinateSystemType
    details_format: str
    show_point_a: bool
    show_point_b: bool
    show_delta: bool
    show_magnitude: bool
    show_component_1: bool
    show_component_2: bool
    show_component_3: bool
    sort_point_names: bool
    show_tolerance_fields: bool
    colorize_in_tolerance_fields: bool
    def __init__(self, coordinate_system: _Optional[_Union[CoordinateSystemType, str]] = ..., details_format: _Optional[str] = ..., show_point_a: bool = ..., show_point_b: bool = ..., show_delta: bool = ..., show_magnitude: bool = ..., show_component_1: bool = ..., show_component_2: bool = ..., show_component_3: bool = ..., sort_point_names: bool = ..., show_tolerance_fields: bool = ..., colorize_in_tolerance_fields: bool = ...) -> None: ...
