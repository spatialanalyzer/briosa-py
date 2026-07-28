from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AsciiImportFileFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASCII_IMPORT_FILE_FORMAT_UNSPECIFIED: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_X_Y_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_X_Y_Z_NOTES: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_RADIUS_THETA_PHI: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_RADIUS_THETA_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_NOTES: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_UX_UY_UZ: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_WMAG: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD_WX_WY_WZ: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_TX_TY_TZ_TD: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE_WX_WY_WZ: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_HIGH_LOW_TOLERANCE: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_RADIUS_THETA_PHI: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_RADIUS_THETA_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_GROUP_NAME: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_POINT_NAME_Y_X_Z_GROUP_NAME: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_NOTES: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_UX_UY_UZ: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_PHI: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z_NOTES: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_PHI: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_Z: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_X_Y_Z_I_J_K: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_VECTOR_NAME_X_Y_Z_I_J_K: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_I_J_K: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: _ClassVar[AsciiImportFileFormat]
    ASCII_IMPORT_FILE_FORMAT_PLANE_NAME_X_Y_Z_DX_DY_DZ_PLANE_SIZE: _ClassVar[AsciiImportFileFormat]

class AsciiFrameSetFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASCII_FRAME_SET_FORMAT_UNSPECIFIED: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]
    ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: _ClassVar[AsciiFrameSetFormat]

class AxisIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AXIS_IDENTIFIER_UNSPECIFIED: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_X: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_X: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_Y: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_Y: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_POSITIVE_Z: _ClassVar[AxisIdentifier]
    AXIS_IDENTIFIER_NEGATIVE_Z: _ClassVar[AxisIdentifier]

class WcfAxisIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WCF_AXIS_IDENTIFIER_UNSPECIFIED: _ClassVar[WcfAxisIdentifier]
    WCF_AXIS_IDENTIFIER_X: _ClassVar[WcfAxisIdentifier]
    WCF_AXIS_IDENTIFIER_Y: _ClassVar[WcfAxisIdentifier]
    WCF_AXIS_IDENTIFIER_Z: _ClassVar[WcfAxisIdentifier]

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

class ChartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHART_TYPE_UNSPECIFIED: _ClassVar[ChartType]
    CHART_TYPE_RUN_CHART: _ClassVar[ChartType]
    CHART_TYPE_INDIVIDUAL_X_MOVING_RANGE: _ClassVar[ChartType]
    CHART_TYPE_BULLSEYE_CHART: _ClassVar[ChartType]

class CollimationBaselineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLIMATION_BASELINE_TYPE_UNSPECIFIED: _ClassVar[CollimationBaselineType]
    COLLIMATION_BASELINE_TYPE_DETERMINED_BY_VALUE: _ClassVar[CollimationBaselineType]
    COLLIMATION_BASELINE_TYPE_DETERMINED_FROM_SCALE: _ClassVar[CollimationBaselineType]
    COLLIMATION_BASELINE_TYPE_DETERMINED_FROM_KNOWN_POINT: _ClassVar[CollimationBaselineType]

class CollimationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLLIMATION_TYPE_UNSPECIFIED: _ClassVar[CollimationType]
    COLLIMATION_TYPE_FULL: _ClassVar[CollimationType]
    COLLIMATION_TYPE_NO_TILT: _ClassVar[CollimationType]

class ColorRangeMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COLOR_RANGE_METHOD_UNSPECIFIED: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_SINGLE_COLOR: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_CONTINUOUS: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_CONTINUOUS: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO_WITH_WARNING: _ClassVar[ColorRangeMethod]
    COLOR_RANGE_METHOD_DISCRETE_COLORS: _ClassVar[ColorRangeMethod]

class CoordinateSystemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COORDINATE_SYSTEM_TYPE_UNSPECIFIED: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_CARTESIAN: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_CYLINDRIC: _ClassVar[CoordinateSystemType]
    COORDINATE_SYSTEM_TYPE_POLAR: _ClassVar[CoordinateSystemType]

class VectorComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VECTOR_COMPONENT_UNSPECIFIED: _ClassVar[VectorComponent]
    VECTOR_COMPONENT_X: _ClassVar[VectorComponent]
    VECTOR_COMPONENT_Y: _ClassVar[VectorComponent]
    VECTOR_COMPONENT_Z: _ClassVar[VectorComponent]
    VECTOR_COMPONENT_MAGNITUDE: _ClassVar[VectorComponent]

class DynamicCircleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_CIRCLE_MODE_UNSPECIFIED: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CYLINDER_PLANE_HOLD_PLANE_NORMAL: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CYLINDER_PLANE_HOLD_CYLINDER_AXIS: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_PLANE_HOLD_PLANE_NORMAL: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_PLANE_HOLD_CONE_AXIS: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_SPHERE_PLANE_INTERSECTION: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_TWO_CONES_INTERSECTION: _ClassVar[DynamicCircleMode]
    DYNAMIC_CIRCLE_MODE_CONE_CYLINDER_INTERSECTION: _ClassVar[DynamicCircleMode]

class DynamicEllipseMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_ELLIPSE_MODE_UNSPECIFIED: _ClassVar[DynamicEllipseMode]
    DYNAMIC_ELLIPSE_MODE_CYLINDER_PLANE_INTERSECTION: _ClassVar[DynamicEllipseMode]
    DYNAMIC_ELLIPSE_MODE_CONE_PLANE_INTERSECTION: _ClassVar[DynamicEllipseMode]

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
    DYNAMIC_PLANE_MODE_TWO_CONES_BEST_FIT_PLANE: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_TWO_CONES_FIRST_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_TWO_CONES_SECOND_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_CYLINDER_BEST_FIT_PLANE: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_CYLINDER_CONE_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_CONE_CYLINDER_CYLINDER_AXIS: _ClassVar[DynamicPlaneMode]
    DYNAMIC_PLANE_MODE_OFFSET_PLANE_FROM_PLANE: _ClassVar[DynamicPlaneMode]

class DynamicPointMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DYNAMIC_POINT_MODE_UNSPECIFIED: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_LINE_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_CYLINDER_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_CONE_PLANE: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_INTERSECTION_THREE_PLANES: _ClassVar[DynamicPointMode]
    DYNAMIC_POINT_MODE_MID_POINT_PERPENDICULAR_TWO_LINES: _ClassVar[DynamicPointMode]

class EdgeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EDGE_MODE_UNSPECIFIED: _ClassVar[EdgeMode]
    EDGE_MODE_INCLUDE_EDGES: _ClassVar[EdgeMode]
    EDGE_MODE_EXCLUDE_EDGES: _ClassVar[EdgeMode]
    EDGE_MODE_EDGES_ONLY: _ClassVar[EdgeMode]

class ExportDataDelimiterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXPORT_DATA_DELIMITER_TYPE_UNSPECIFIED: _ClassVar[ExportDataDelimiterType]
    EXPORT_DATA_DELIMITER_TYPE_SPACE: _ClassVar[ExportDataDelimiterType]
    EXPORT_DATA_DELIMITER_TYPE_COMMA: _ClassVar[ExportDataDelimiterType]
    EXPORT_DATA_DELIMITER_TYPE_TAB: _ClassVar[ExportDataDelimiterType]

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

class InstrumentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INSTRUMENT_TYPE_UNSPECIFIED: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AICON_DPA: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AICON_MOVE_INSPECT: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_ILT: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ASSEMBLY_GUIDANCE_LASER_PROJECTOR: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CREAFORM_VX_ELEMENTS: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_DIGITAL_NETWORK_LEVEL: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_1_5M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_2_5M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_2_5M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_2M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_2M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_3_5M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_3_5M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_3M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_3M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_4M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_4M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_SCANNER_PHOTON_LS_FOCUS_3D: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_GENERIC_AUX_DEVICE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_GENERIC_AUX_DEVICE_2: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_GENERIC_PHOTOGRAMMETRY_SYSTEM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_GENERIC_PHOTOGRAMMETRY_SYSTEM_2: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LAP_CAD_PRO_LASER_PROJECTOR: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_GEOSYSTEMS_RTC360: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_GEOSYSTEMS_SCAN_STATION_PXX: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_T1200_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TM6100A_THEODOLITE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TS09_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TS15_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TS16_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TS20_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TS30_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LPT_LASER_PROJECTOR: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SA_OPEN_AUXILIARY_INSTRUMENT: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SA_OPEN_INSTRUMENT: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SA_PIPELINE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SURPHASER_10_SCANNER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SURPHASER_SCANNER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_VICON_TRACKER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_XYZ_REFERENCE_FRAME: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AICON_PROCAM_3D_PROBE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_LADAR: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_LASER_RAIL: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_OMNITRAC: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_OMNITRAC2: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_RADIAN: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_RADIAN_PLUS_CORE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_RADIAN_PRO: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_TRACKER_DEVICE_INTERFACE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_TRACKER_II: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_API_TRACKER_III: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AXXIS_6_100_ARM_2_6M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AXXIS_6_200_ARM_3_2M_6_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AXXIS_7_100_ARM_PROBE_2_6M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_AXXIS_7_100_ARM_SCANNER_2_6M_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_1024: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_1028: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_1030: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_2200: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_2500: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3012I_5012_1_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3018I_5018_1_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3024I_5024_2_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3028I_5028_2_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3036I_5036_3_6M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5112_1_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5118_1_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5124_2_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5128_2_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5130_3_0M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5136_3_6M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5012SC_3012_1_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5018SC_3018_1_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5024SC_3024_2_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5028SC_3028_2_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5030SC_3030_3_0M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5036SC_3036_3_6M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5112SC_1_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5118SC_1_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5124SC_2_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5128SC_2_8M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5130SC_3_0M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5136SC_3_6M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_CUBIC_KIT_THEODOLITE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_DAVIS_PERCEPTION_II_WEATHER_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G04: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G04_05_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G08: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G08_05_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G12: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_G12_05_7_DOF: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_S08: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_S12: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_10_FT_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_10_FT_7_DOF_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_12_FT_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_12_FT_7_DOF_EDGE_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_4_FT_QUANTUM_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_4_FT_7_DOF_QUANTUM_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_6_FT_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_6_FT_7_DOF_EDGE_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_8_FT_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_8_FT_7_DOF_QUANTUM_FUSION_PRIME_PLATINUM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ARM_USB_9_FT_7_DOF_EDGE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_ION_TRACKER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_TRACKER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_FARO_VANTAGE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_GSI_V_STARS_PHOTOGRAMMETRY_SYSTEM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_1_2M_COMPACT: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_2_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_3_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_3M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_4_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_2_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_2M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_3_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_3M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_4_5M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_4M: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_HEXAGON_HANDHELD_3D_SCANNER: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_IMPORTED_MEASUREMENTS_WITH_UNCERTAINTY: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KERN_E2_THEODOLITE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_20: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_25: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_30: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_35: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_40: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_6_45: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_20: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_25: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_30: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_35: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_40: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_KREON_API_ACE_7_45: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_AT500: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_AT960_930: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_ATS600: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_ATS800: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_EMSCON_ABSOLUTE_TRACKER_AT901_SERIES: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_EMSCON_AT401: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_EMSCON_AT402: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_EMSCON_AT403: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_EMSCON_TRACKER_LT500_800_SERIES: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_NOVA_MS50_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_NOVA_MS60_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TDA5005_TOTAL_STATION_GEOCOM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TDRA6000_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TOTAL_STATION_TC2000_TC2002: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TPS_THEODOLITE_1800: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TPS_THEODOLITE_5100: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TPS_TOTAL_STATION_2003_5000_5005: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_TRACKER_TP_LINK: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_LEICA_WILD_THEODOLITES_T2000_T2002_T3000: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_METRONOR_PORTABLE_MEASUREMENT_SYSTEM: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_A: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_AI: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_AP: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_NIKON_METROLOGY_APDIS_MV400: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_NIKON_METROLOGY_LASER_RADAR_MV200: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_NIKON_METROLOGY_LASER_RADAR_MV300: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_NIKON_METROLOGY_SURVEYOR_V2: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_NIVEL_20_TWO_AXIS_LEVEL: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ON_TRAK_LASER_LINE_SYSTEM_OT_4040_OT_6000: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7315: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X20: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X20SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X25: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X25SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X30: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X30SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X35: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X35SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X40: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X40SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X45: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X45SI_SE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ROMER_MULTI_GAGE: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SOKKIA_NET_1_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SOKKIA_NET_2_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SOKKIA_NET05AX_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SOKKIA_NET05X_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_SOKKIA_SETX_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_THOMMEN_HM30_WEATHER_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_TOPCON_MS_AX_SERIES_TOTAL_STATION: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ULTRASONIC_THICKNESS_GAUGE_CL400: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_VIRTEK_LASER_PROJECTOR: _ClassVar[InstrumentType]
    INSTRUMENT_TYPE_ZEISS_ETH_2_THEODOLITE: _ClassVar[InstrumentType]

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

class OffsetDirectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OFFSET_DIRECTION_TYPE_UNSPECIFIED: _ClassVar[OffsetDirectionType]
    OFFSET_DIRECTION_TYPE_BOTH: _ClassVar[OffsetDirectionType]
    OFFSET_DIRECTION_TYPE_POSITIVE_ONLY: _ClassVar[OffsetDirectionType]
    OFFSET_DIRECTION_TYPE_NEGATIVE_ONLY: _ClassVar[OffsetDirectionType]

class PointFilterInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    POINT_FILTER_INPUT_TYPE_UNSPECIFIED: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_CARDINAL_POINTS: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_INPUT_POINTS: _ClassVar[PointFilterInputType]
    POINT_FILTER_INPUT_TYPE_NOMINAL_CARDINAL_POINTS: _ClassVar[PointFilterInputType]

class RelationshipWeightingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RELATIONSHIP_WEIGHTING_MODE_UNSPECIFIED: _ClassVar[RelationshipWeightingMode]
    RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT: _ClassVar[RelationshipWeightingMode]
    RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT_AND_TOLERANCE_WIDTH: _ClassVar[RelationshipWeightingMode]
    RELATIONSHIP_WEIGHTING_MODE_RESET_ALL_WEIGHTS: _ClassVar[RelationshipWeightingMode]
    RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_EQUATION_COUNT: _ClassVar[RelationshipWeightingMode]
    RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_AND_TOLERANCE_WIDTH: _ClassVar[RelationshipWeightingMode]

class RenderModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RENDER_MODE_TYPE_UNSPECIFIED: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_WIREFRAME: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_HIDDEN_LINE_REMOVED: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_SOLID_AND_EDGES: _ClassVar[RenderModeType]
    RENDER_MODE_TYPE_SOLID: _ClassVar[RenderModeType]

class ReportPageOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_PAGE_ORIENTATION_UNSPECIFIED: _ClassVar[ReportPageOrientation]
    REPORT_PAGE_ORIENTATION_PORTRAIT: _ClassVar[ReportPageOrientation]
    REPORT_PAGE_ORIENTATION_LANDSCAPE: _ClassVar[ReportPageOrientation]

class SaturationLimitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SATURATION_LIMIT_TYPE_UNSPECIFIED: _ClassVar[SaturationLimitType]
    SATURATION_LIMIT_TYPE_DEVIATION: _ClassVar[SaturationLimitType]
    SATURATION_LIMIT_TYPE_SIGMA_RULE: _ClassVar[SaturationLimitType]
    SATURATION_LIMIT_TYPE_CUSTOM: _ClassVar[SaturationLimitType]

class ShowUsmnDialogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHOW_USMN_DIALOG_TYPE_UNSPECIFIED: _ClassVar[ShowUsmnDialogType]
    SHOW_USMN_DIALOG_TYPE_NO: _ClassVar[ShowUsmnDialogType]
    SHOW_USMN_DIALOG_TYPE_YES: _ClassVar[ShowUsmnDialogType]
    SHOW_USMN_DIALOG_TYPE_ON_TOLERANCE_VIOLATION: _ClassVar[ShowUsmnDialogType]

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

class SurfaceDissectionModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SURFACE_DISSECTION_MODE_TYPE_UNSPECIFIED: _ClassVar[SurfaceDissectionModeType]
    SURFACE_DISSECTION_MODE_TYPE_ENTIRE_SOLID: _ClassVar[SurfaceDissectionModeType]
    SURFACE_DISSECTION_MODE_TYPE_SELECT_FACES: _ClassVar[SurfaceDissectionModeType]

class TargetComputationMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_COMPUTATION_METHOD_UNSPECIFIED: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_USE_MOST_RECENT_SHOT_FROM_EACH_FACE: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_USE_ONLY_MOST_RECENT_SHOT: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_DO_NOT_CHANGE_PRIOR_MEASUREMENTS: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_FORCE_NEW_POINT_FOR_EACH_MEASUREMENT: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_REMOVE_ALL_PRIOR_SHOTS: _ClassVar[TargetComputationMethod]
    TARGET_COMPUTATION_METHOD_DEACTIVATE_ALL_PRIOR_SHOTS: _ClassVar[TargetComputationMethod]

class TranslucencyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSLUCENCY_TYPE_UNSPECIFIED: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_SOLID: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_TRANSLUCENT: _ClassVar[TranslucencyType]
    TRANSLUCENCY_TYPE_WIREFRAME: _ClassVar[TranslucencyType]

class CloudThinningMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_THINNING_MODE_UNSPECIFIED: _ClassVar[CloudThinningMode]
    CLOUD_THINNING_MODE_NONE: _ClassVar[CloudThinningMode]
    CLOUD_THINNING_MODE_RANDOM: _ClassVar[CloudThinningMode]
    CLOUD_THINNING_MODE_NTH_POINT: _ClassVar[CloudThinningMode]

class ReportOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_OUTPUT_TYPE_UNSPECIFIED: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_NONE: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_SA_REPORT: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_SA_DOCUMENT: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_PDF: _ClassVar[ReportOutputType]
    REPORT_OUTPUT_TYPE_RTF: _ClassVar[ReportOutputType]

class ReportViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_VIEW_TYPE_UNSPECIFIED: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_NONE: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_CURRENT_VIEW: _ClassVar[ReportViewType]
    REPORT_VIEW_TYPE_CALLOUT_VIEW: _ClassVar[ReportViewType]
ASCII_IMPORT_FILE_FORMAT_UNSPECIFIED: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_X_Y_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_X_Y_Z_OFFSET_OFFSET2: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_X_Y_Z_NOTES: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_RADIUS_THETA_PHI: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_RADIUS_THETA_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_NOTES: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_UX_UY_UZ: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_WMAG: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_TX_TY_TZ_TD_WX_WY_WZ: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_TX_TY_TZ_TD: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_HIGH_LOW_TOLERANCE_WX_WY_WZ: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_WX_WY_WZ_HIGH_LOW_TOLERANCE: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_RADIUS_THETA_PHI: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_RADIUS_THETA_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_X_Y_Z_GROUP_NAME: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_POINT_NAME_Y_X_Z_GROUP_NAME: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_OFFSET_OFFSET2: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_NOTES: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_X_Y_Z_UX_UY_UZ: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_PHI: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_GROUP_NAME_POINT_NAME_RADIUS_THETA_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_X_Y_Z_NOTES: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_PHI: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_COLLECTION_GROUP_POINT_RADIUS_THETA_Z: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_X_Y_Z_I_J_K: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_VECTOR_NAME_X_Y_Z_I_J_K: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_I_J_K: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_VECTOR_GROUP_NAME_VECTOR_NAME_X_Y_Z_DX_DY_DZ_SIGNED_MAGNITUDE: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: AsciiImportFileFormat
ASCII_IMPORT_FILE_FORMAT_PLANE_NAME_X_Y_Z_DX_DY_DZ_PLANE_SIZE: AsciiImportFileFormat
ASCII_FRAME_SET_FORMAT_UNSPECIFIED: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_RX_RY_RZ_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_X_Y_Z_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_X_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_Y_Z_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_EULER_Z_X_Z_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_TRANSFORMATION_MATRIX_TIMESTAMP: AsciiFrameSetFormat
ASCII_FRAME_SET_FORMAT_FRAME_NAME_X_Y_Z_QUATERNION_TIMESTAMP: AsciiFrameSetFormat
AXIS_IDENTIFIER_UNSPECIFIED: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_X: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_X: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_Y: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_Y: AxisIdentifier
AXIS_IDENTIFIER_POSITIVE_Z: AxisIdentifier
AXIS_IDENTIFIER_NEGATIVE_Z: AxisIdentifier
WCF_AXIS_IDENTIFIER_UNSPECIFIED: WcfAxisIdentifier
WCF_AXIS_IDENTIFIER_X: WcfAxisIdentifier
WCF_AXIS_IDENTIFIER_Y: WcfAxisIdentifier
WCF_AXIS_IDENTIFIER_Z: WcfAxisIdentifier
BASE_COLOR_TYPE_UNSPECIFIED: BaseColorType
BASE_COLOR_TYPE_RED: BaseColorType
BASE_COLOR_TYPE_GREEN: BaseColorType
BASE_COLOR_TYPE_BLUE: BaseColorType
BASE_MID_COLOR_TYPE_UNSPECIFIED: BaseMidColorType
BASE_MID_COLOR_TYPE_RED: BaseMidColorType
BASE_MID_COLOR_TYPE_GREEN: BaseMidColorType
BASE_MID_COLOR_TYPE_GRAY: BaseMidColorType
BASE_MID_COLOR_TYPE_BLUE: BaseMidColorType
CHART_TYPE_UNSPECIFIED: ChartType
CHART_TYPE_RUN_CHART: ChartType
CHART_TYPE_INDIVIDUAL_X_MOVING_RANGE: ChartType
CHART_TYPE_BULLSEYE_CHART: ChartType
COLLIMATION_BASELINE_TYPE_UNSPECIFIED: CollimationBaselineType
COLLIMATION_BASELINE_TYPE_DETERMINED_BY_VALUE: CollimationBaselineType
COLLIMATION_BASELINE_TYPE_DETERMINED_FROM_SCALE: CollimationBaselineType
COLLIMATION_BASELINE_TYPE_DETERMINED_FROM_KNOWN_POINT: CollimationBaselineType
COLLIMATION_TYPE_UNSPECIFIED: CollimationType
COLLIMATION_TYPE_FULL: CollimationType
COLLIMATION_TYPE_NO_TILT: CollimationType
COLOR_RANGE_METHOD_UNSPECIFIED: ColorRangeMethod
COLOR_RANGE_METHOD_SINGLE_COLOR: ColorRangeMethod
COLOR_RANGE_METHOD_CONTINUOUS: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_CONTINUOUS: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO: ColorRangeMethod
COLOR_RANGE_METHOD_TOLERANCED_GO_NO_GO_WITH_WARNING: ColorRangeMethod
COLOR_RANGE_METHOD_DISCRETE_COLORS: ColorRangeMethod
COORDINATE_SYSTEM_TYPE_UNSPECIFIED: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_CARTESIAN: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_CYLINDRIC: CoordinateSystemType
COORDINATE_SYSTEM_TYPE_POLAR: CoordinateSystemType
VECTOR_COMPONENT_UNSPECIFIED: VectorComponent
VECTOR_COMPONENT_X: VectorComponent
VECTOR_COMPONENT_Y: VectorComponent
VECTOR_COMPONENT_Z: VectorComponent
VECTOR_COMPONENT_MAGNITUDE: VectorComponent
DYNAMIC_CIRCLE_MODE_UNSPECIFIED: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CYLINDER_PLANE_HOLD_PLANE_NORMAL: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CYLINDER_PLANE_HOLD_CYLINDER_AXIS: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_PLANE_HOLD_PLANE_NORMAL: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_PLANE_HOLD_CONE_AXIS: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_SPHERE_PLANE_INTERSECTION: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_TWO_CONES_INTERSECTION: DynamicCircleMode
DYNAMIC_CIRCLE_MODE_CONE_CYLINDER_INTERSECTION: DynamicCircleMode
DYNAMIC_ELLIPSE_MODE_UNSPECIFIED: DynamicEllipseMode
DYNAMIC_ELLIPSE_MODE_CYLINDER_PLANE_INTERSECTION: DynamicEllipseMode
DYNAMIC_ELLIPSE_MODE_CONE_PLANE_INTERSECTION: DynamicEllipseMode
DYNAMIC_LINE_MODE_UNSPECIFIED: DynamicLineMode
DYNAMIC_LINE_MODE_CONE_AXIS: DynamicLineMode
DYNAMIC_LINE_MODE_CYLINDER_AXIS: DynamicLineMode
DYNAMIC_LINE_MODE_INTERSECTION_OF_TWO_PLANES: DynamicLineMode
DYNAMIC_LINE_MODE_BISECT_TWO_LINES: DynamicLineMode
DYNAMIC_LINE_MODE_SLOT_CENTERLINE_ALONG_LENGTH: DynamicLineMode
DYNAMIC_PLANE_MODE_UNSPECIFIED: DynamicPlaneMode
DYNAMIC_PLANE_MODE_BISECT_TWO_PLANES: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_BEST_FIT_PLANE: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_FIRST_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_TWO_CONES_SECOND_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_CYLINDER_BEST_FIT_PLANE: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_CYLINDER_CONE_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_CONE_CYLINDER_CYLINDER_AXIS: DynamicPlaneMode
DYNAMIC_PLANE_MODE_OFFSET_PLANE_FROM_PLANE: DynamicPlaneMode
DYNAMIC_POINT_MODE_UNSPECIFIED: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_LINE_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_CYLINDER_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_CONE_PLANE: DynamicPointMode
DYNAMIC_POINT_MODE_INTERSECTION_THREE_PLANES: DynamicPointMode
DYNAMIC_POINT_MODE_MID_POINT_PERPENDICULAR_TWO_LINES: DynamicPointMode
EDGE_MODE_UNSPECIFIED: EdgeMode
EDGE_MODE_INCLUDE_EDGES: EdgeMode
EDGE_MODE_EXCLUDE_EDGES: EdgeMode
EDGE_MODE_EDGES_ONLY: EdgeMode
EXPORT_DATA_DELIMITER_TYPE_UNSPECIFIED: ExportDataDelimiterType
EXPORT_DATA_DELIMITER_TYPE_SPACE: ExportDataDelimiterType
EXPORT_DATA_DELIMITER_TYPE_COMMA: ExportDataDelimiterType
EXPORT_DATA_DELIMITER_TYPE_TAB: ExportDataDelimiterType
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
INSTRUMENT_TYPE_UNSPECIFIED: InstrumentType
INSTRUMENT_TYPE_AICON_DPA: InstrumentType
INSTRUMENT_TYPE_AICON_MOVE_INSPECT: InstrumentType
INSTRUMENT_TYPE_API_ILT: InstrumentType
INSTRUMENT_TYPE_ASSEMBLY_GUIDANCE_LASER_PROJECTOR: InstrumentType
INSTRUMENT_TYPE_CREAFORM_VX_ELEMENTS: InstrumentType
INSTRUMENT_TYPE_DIGITAL_NETWORK_LEVEL: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_1_5M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_2_5M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_2_5M_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_2M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_2M_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_3_5M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_3_5M_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_3M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_3M_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_4M_6_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_4M_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_SCANNER_PHOTON_LS_FOCUS_3D: InstrumentType
INSTRUMENT_TYPE_GENERIC_AUX_DEVICE: InstrumentType
INSTRUMENT_TYPE_GENERIC_AUX_DEVICE_2: InstrumentType
INSTRUMENT_TYPE_GENERIC_PHOTOGRAMMETRY_SYSTEM: InstrumentType
INSTRUMENT_TYPE_GENERIC_PHOTOGRAMMETRY_SYSTEM_2: InstrumentType
INSTRUMENT_TYPE_LAP_CAD_PRO_LASER_PROJECTOR: InstrumentType
INSTRUMENT_TYPE_LEICA_GEOSYSTEMS_RTC360: InstrumentType
INSTRUMENT_TYPE_LEICA_GEOSYSTEMS_SCAN_STATION_PXX: InstrumentType
INSTRUMENT_TYPE_LEICA_T1200_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TM6100A_THEODOLITE: InstrumentType
INSTRUMENT_TYPE_LEICA_TS09_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TS15_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TS16_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TS20_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TS30_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LPT_LASER_PROJECTOR: InstrumentType
INSTRUMENT_TYPE_SA_OPEN_AUXILIARY_INSTRUMENT: InstrumentType
INSTRUMENT_TYPE_SA_OPEN_INSTRUMENT: InstrumentType
INSTRUMENT_TYPE_SA_PIPELINE: InstrumentType
INSTRUMENT_TYPE_SURPHASER_10_SCANNER: InstrumentType
INSTRUMENT_TYPE_SURPHASER_SCANNER: InstrumentType
INSTRUMENT_TYPE_VICON_TRACKER: InstrumentType
INSTRUMENT_TYPE_XYZ_REFERENCE_FRAME: InstrumentType
INSTRUMENT_TYPE_AICON_PROCAM_3D_PROBE: InstrumentType
INSTRUMENT_TYPE_API_LADAR: InstrumentType
INSTRUMENT_TYPE_API_LASER_RAIL: InstrumentType
INSTRUMENT_TYPE_API_OMNITRAC: InstrumentType
INSTRUMENT_TYPE_API_OMNITRAC2: InstrumentType
INSTRUMENT_TYPE_API_RADIAN: InstrumentType
INSTRUMENT_TYPE_API_RADIAN_PLUS_CORE: InstrumentType
INSTRUMENT_TYPE_API_RADIAN_PRO: InstrumentType
INSTRUMENT_TYPE_API_TRACKER_DEVICE_INTERFACE: InstrumentType
INSTRUMENT_TYPE_API_TRACKER_II: InstrumentType
INSTRUMENT_TYPE_API_TRACKER_III: InstrumentType
INSTRUMENT_TYPE_AXXIS_6_100_ARM_2_6M_6_DOF: InstrumentType
INSTRUMENT_TYPE_AXXIS_6_200_ARM_3_2M_6_DOF: InstrumentType
INSTRUMENT_TYPE_AXXIS_7_100_ARM_PROBE_2_6M_7_DOF: InstrumentType
INSTRUMENT_TYPE_AXXIS_7_100_ARM_SCANNER_2_6M_7_DOF: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_1024: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_1028: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_1030: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_2200: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_2500: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3012I_5012_1_2M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3018I_5018_1_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3024I_5024_2_4M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3028I_5028_2_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_3036I_5036_3_6M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5112_1_2M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5118_1_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5124_2_4M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5128_2_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5130_3_0M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_6_DOF_5136_3_6M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5012SC_3012_1_2M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5018SC_3018_1_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5024SC_3024_2_4M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5028SC_3028_2_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5030SC_3030_3_0M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5036SC_3036_3_6M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5112SC_1_2M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5118SC_1_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5124SC_2_4M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5128SC_2_8M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5130SC_3_0M: InstrumentType
INSTRUMENT_TYPE_CIMCORE_ARM_7_DOF_5136SC_3_6M: InstrumentType
INSTRUMENT_TYPE_CUBIC_KIT_THEODOLITE: InstrumentType
INSTRUMENT_TYPE_DAVIS_PERCEPTION_II_WEATHER_STATION: InstrumentType
INSTRUMENT_TYPE_FARO_ARM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G04: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G04_05_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G08: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G08_05_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G12: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_G12_05_7_DOF: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_S08: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_S12: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_10_FT_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_10_FT_7_DOF_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_12_FT_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_12_FT_7_DOF_EDGE_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_4_FT_QUANTUM_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_4_FT_7_DOF_QUANTUM_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_6_FT_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_6_FT_7_DOF_EDGE_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_8_FT_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_8_FT_7_DOF_QUANTUM_FUSION_PRIME_PLATINUM: InstrumentType
INSTRUMENT_TYPE_FARO_ARM_USB_9_FT_7_DOF_EDGE: InstrumentType
INSTRUMENT_TYPE_FARO_ION_TRACKER: InstrumentType
INSTRUMENT_TYPE_FARO_TRACKER: InstrumentType
INSTRUMENT_TYPE_FARO_VANTAGE: InstrumentType
INSTRUMENT_TYPE_GSI_V_STARS_PHOTOGRAMMETRY_SYSTEM: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_1_2M_COMPACT: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_2_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_2M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_3_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_3M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_4_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_6_DOF_4M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_2_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_2M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_3_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_3M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_4_5M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_ABSOLUTE_8_7_DOF_4M: InstrumentType
INSTRUMENT_TYPE_HEXAGON_HANDHELD_3D_SCANNER: InstrumentType
INSTRUMENT_TYPE_IMPORTED_MEASUREMENTS_WITH_UNCERTAINTY: InstrumentType
INSTRUMENT_TYPE_KERN_E2_THEODOLITE: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_20: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_25: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_30: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_35: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_40: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_6_45: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_20: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_25: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_30: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_35: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_40: InstrumentType
INSTRUMENT_TYPE_KREON_API_ACE_7_45: InstrumentType
INSTRUMENT_TYPE_LEICA_AT500: InstrumentType
INSTRUMENT_TYPE_LEICA_AT960_930: InstrumentType
INSTRUMENT_TYPE_LEICA_ATS600: InstrumentType
INSTRUMENT_TYPE_LEICA_ATS800: InstrumentType
INSTRUMENT_TYPE_LEICA_EMSCON_ABSOLUTE_TRACKER_AT901_SERIES: InstrumentType
INSTRUMENT_TYPE_LEICA_EMSCON_AT401: InstrumentType
INSTRUMENT_TYPE_LEICA_EMSCON_AT402: InstrumentType
INSTRUMENT_TYPE_LEICA_EMSCON_AT403: InstrumentType
INSTRUMENT_TYPE_LEICA_EMSCON_TRACKER_LT500_800_SERIES: InstrumentType
INSTRUMENT_TYPE_LEICA_NOVA_MS50_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_NOVA_MS60_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TDA5005_TOTAL_STATION_GEOCOM: InstrumentType
INSTRUMENT_TYPE_LEICA_TDRA6000_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_LEICA_TOTAL_STATION_TC2000_TC2002: InstrumentType
INSTRUMENT_TYPE_LEICA_TPS_THEODOLITE_1800: InstrumentType
INSTRUMENT_TYPE_LEICA_TPS_THEODOLITE_5100: InstrumentType
INSTRUMENT_TYPE_LEICA_TPS_TOTAL_STATION_2003_5000_5005: InstrumentType
INSTRUMENT_TYPE_LEICA_TRACKER_TP_LINK: InstrumentType
INSTRUMENT_TYPE_LEICA_WILD_THEODOLITES_T2000_T2002_T3000: InstrumentType
INSTRUMENT_TYPE_METRONOR_PORTABLE_MEASUREMENT_SYSTEM: InstrumentType
INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_A: InstrumentType
INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_AI: InstrumentType
INSTRUMENT_TYPE_MITUTOYO_SPACETRAC_AP: InstrumentType
INSTRUMENT_TYPE_NIKON_METROLOGY_APDIS_MV400: InstrumentType
INSTRUMENT_TYPE_NIKON_METROLOGY_LASER_RADAR_MV200: InstrumentType
INSTRUMENT_TYPE_NIKON_METROLOGY_LASER_RADAR_MV300: InstrumentType
INSTRUMENT_TYPE_NIKON_METROLOGY_SURVEYOR_V2: InstrumentType
INSTRUMENT_TYPE_NIVEL_20_TWO_AXIS_LEVEL: InstrumentType
INSTRUMENT_TYPE_ON_TRAK_LASER_LINE_SYSTEM_OT_4040_OT_6000: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7315: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X20: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X20SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X25: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X25SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X30: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X30SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X35: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X35SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X40: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X40SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X45: InstrumentType
INSTRUMENT_TYPE_ROMER_ABSOLUTE_7X45SI_SE: InstrumentType
INSTRUMENT_TYPE_ROMER_MULTI_GAGE: InstrumentType
INSTRUMENT_TYPE_SOKKIA_NET_1_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_SOKKIA_NET_2_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_SOKKIA_NET05AX_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_SOKKIA_NET05X_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_SOKKIA_SETX_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_THOMMEN_HM30_WEATHER_STATION: InstrumentType
INSTRUMENT_TYPE_TOPCON_MS_AX_SERIES_TOTAL_STATION: InstrumentType
INSTRUMENT_TYPE_ULTRASONIC_THICKNESS_GAUGE_CL400: InstrumentType
INSTRUMENT_TYPE_VIRTEK_LASER_PROJECTOR: InstrumentType
INSTRUMENT_TYPE_ZEISS_ETH_2_THEODOLITE: InstrumentType
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
OFFSET_DIRECTION_TYPE_UNSPECIFIED: OffsetDirectionType
OFFSET_DIRECTION_TYPE_BOTH: OffsetDirectionType
OFFSET_DIRECTION_TYPE_POSITIVE_ONLY: OffsetDirectionType
OFFSET_DIRECTION_TYPE_NEGATIVE_ONLY: OffsetDirectionType
POINT_FILTER_INPUT_TYPE_UNSPECIFIED: PointFilterInputType
POINT_FILTER_INPUT_TYPE_CARDINAL_POINTS: PointFilterInputType
POINT_FILTER_INPUT_TYPE_INPUT_POINTS: PointFilterInputType
POINT_FILTER_INPUT_TYPE_NOMINAL_CARDINAL_POINTS: PointFilterInputType
RELATIONSHIP_WEIGHTING_MODE_UNSPECIFIED: RelationshipWeightingMode
RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT: RelationshipWeightingMode
RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_EQUATION_COUNT_AND_TOLERANCE_WIDTH: RelationshipWeightingMode
RELATIONSHIP_WEIGHTING_MODE_RESET_ALL_WEIGHTS: RelationshipWeightingMode
RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_EQUATION_COUNT: RelationshipWeightingMode
RELATIONSHIP_WEIGHTING_MODE_NORMALIZE_SQUARE_ROOT_AND_TOLERANCE_WIDTH: RelationshipWeightingMode
RENDER_MODE_TYPE_UNSPECIFIED: RenderModeType
RENDER_MODE_TYPE_WIREFRAME: RenderModeType
RENDER_MODE_TYPE_HIDDEN_LINE_REMOVED: RenderModeType
RENDER_MODE_TYPE_SOLID_AND_EDGES: RenderModeType
RENDER_MODE_TYPE_SOLID: RenderModeType
REPORT_PAGE_ORIENTATION_UNSPECIFIED: ReportPageOrientation
REPORT_PAGE_ORIENTATION_PORTRAIT: ReportPageOrientation
REPORT_PAGE_ORIENTATION_LANDSCAPE: ReportPageOrientation
SATURATION_LIMIT_TYPE_UNSPECIFIED: SaturationLimitType
SATURATION_LIMIT_TYPE_DEVIATION: SaturationLimitType
SATURATION_LIMIT_TYPE_SIGMA_RULE: SaturationLimitType
SATURATION_LIMIT_TYPE_CUSTOM: SaturationLimitType
SHOW_USMN_DIALOG_TYPE_UNSPECIFIED: ShowUsmnDialogType
SHOW_USMN_DIALOG_TYPE_NO: ShowUsmnDialogType
SHOW_USMN_DIALOG_TYPE_YES: ShowUsmnDialogType
SHOW_USMN_DIALOG_TYPE_ON_TOLERANCE_VIOLATION: ShowUsmnDialogType
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
SURFACE_DISSECTION_MODE_TYPE_UNSPECIFIED: SurfaceDissectionModeType
SURFACE_DISSECTION_MODE_TYPE_ENTIRE_SOLID: SurfaceDissectionModeType
SURFACE_DISSECTION_MODE_TYPE_SELECT_FACES: SurfaceDissectionModeType
TARGET_COMPUTATION_METHOD_UNSPECIFIED: TargetComputationMethod
TARGET_COMPUTATION_METHOD_USE_MOST_RECENT_SHOT_FROM_EACH_FACE: TargetComputationMethod
TARGET_COMPUTATION_METHOD_USE_ONLY_MOST_RECENT_SHOT: TargetComputationMethod
TARGET_COMPUTATION_METHOD_DO_NOT_CHANGE_PRIOR_MEASUREMENTS: TargetComputationMethod
TARGET_COMPUTATION_METHOD_FORCE_NEW_POINT_FOR_EACH_MEASUREMENT: TargetComputationMethod
TARGET_COMPUTATION_METHOD_REMOVE_ALL_PRIOR_SHOTS: TargetComputationMethod
TARGET_COMPUTATION_METHOD_DEACTIVATE_ALL_PRIOR_SHOTS: TargetComputationMethod
TRANSLUCENCY_TYPE_UNSPECIFIED: TranslucencyType
TRANSLUCENCY_TYPE_SOLID: TranslucencyType
TRANSLUCENCY_TYPE_TRANSLUCENT: TranslucencyType
TRANSLUCENCY_TYPE_WIREFRAME: TranslucencyType
CLOUD_THINNING_MODE_UNSPECIFIED: CloudThinningMode
CLOUD_THINNING_MODE_NONE: CloudThinningMode
CLOUD_THINNING_MODE_RANDOM: CloudThinningMode
CLOUD_THINNING_MODE_NTH_POINT: CloudThinningMode
REPORT_OUTPUT_TYPE_UNSPECIFIED: ReportOutputType
REPORT_OUTPUT_TYPE_NONE: ReportOutputType
REPORT_OUTPUT_TYPE_SA_REPORT: ReportOutputType
REPORT_OUTPUT_TYPE_SA_DOCUMENT: ReportOutputType
REPORT_OUTPUT_TYPE_PDF: ReportOutputType
REPORT_OUTPUT_TYPE_RTF: ReportOutputType
REPORT_VIEW_TYPE_UNSPECIFIED: ReportViewType
REPORT_VIEW_TYPE_NONE: ReportViewType
REPORT_VIEW_TYPE_CURRENT_VIEW: ReportViewType
REPORT_VIEW_TYPE_CALLOUT_VIEW: ReportViewType

class AutoFilterProximitySettings(_message.Message):
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
    surface_proximity_mode: OffsetDirectionType
    planar_proximity_mode: OffsetDirectionType
    radial_proximity_mode: OffsetDirectionType
    project_to_plane: bool
    assert_plane_boundaries: bool
    def __init__(self, surface_inclusion_proximity: _Optional[float] = ..., edge_exclusion_proximity: _Optional[float] = ..., planar_inclusion_proximity: _Optional[float] = ..., planar_exclusion_proximity: _Optional[float] = ..., radial_inclusion_proximity: _Optional[float] = ..., geometry_extraction_tolerance: _Optional[float] = ..., surface_proximity_mode: _Optional[_Union[OffsetDirectionType, str]] = ..., planar_proximity_mode: _Optional[_Union[OffsetDirectionType, str]] = ..., radial_proximity_mode: _Optional[_Union[OffsetDirectionType, str]] = ..., project_to_plane: bool = ..., assert_plane_boundaries: bool = ...) -> None: ...

class CloudThinningOptions(_message.Message):
    __slots__ = ("mode", "point_increment", "minimum_number_of_points", "maximum_number_of_points")
    MODE_FIELD_NUMBER: _ClassVar[int]
    POINT_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_NUMBER_OF_POINTS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_NUMBER_OF_POINTS_FIELD_NUMBER: _ClassVar[int]
    mode: CloudThinningMode
    point_increment: int
    minimum_number_of_points: int
    maximum_number_of_points: int
    def __init__(self, mode: _Optional[_Union[CloudThinningMode, str]] = ..., point_increment: _Optional[int] = ..., minimum_number_of_points: _Optional[int] = ..., maximum_number_of_points: _Optional[int] = ...) -> None: ...

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

class ScalarToleranceLimit(_message.Message):
    __slots__ = ("enabled", "value")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    value: float
    def __init__(self, enabled: bool = ..., value: _Optional[float] = ...) -> None: ...

class FitConstraintScalarOptions(_message.Message):
    __slots__ = ("high", "low")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: ScalarToleranceLimit
    low: ScalarToleranceLimit
    def __init__(self, high: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ..., low: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ...) -> None: ...

class FitDegreeOfFreedomOptions(_message.Message):
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

class ToleranceScalarOptions(_message.Message):
    __slots__ = ("high", "low")
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    high: ScalarToleranceLimit
    low: ScalarToleranceLimit
    def __init__(self, high: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ..., low: _Optional[_Union[ScalarToleranceLimit, _Mapping]] = ...) -> None: ...
