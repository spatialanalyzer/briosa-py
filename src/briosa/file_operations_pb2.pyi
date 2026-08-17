from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BackupNowRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BackupNowResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CopyGeneralFileRequest(_message.Message):
    __slots__ = ("source_file_name", "destination_file_name", "overwrite")
    SOURCE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    source_file_name: _spatial_analyzer_values_pb2.FileReference
    destination_file_name: _spatial_analyzer_values_pb2.FileReference
    overwrite: bool
    def __init__(self, source_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., destination_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., overwrite: bool = ...) -> None: ...

class CopyGeneralFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteGeneralFileRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class DeleteGeneralFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DirectCadAccessRequest(_message.Message):
    __slots__ = ("cad_file_name", "import_solids", "import_surfaces", "import_polygonized_surfaces", "import_annotations", "import_vectors", "import_points", "point_group_name", "import_attributes_metadata", "import_cooordinate_frames", "import_planes", "import_3d_curves_lines", "import_3d_curves_circles", "import_3d_curves_general_curves", "import_construction_geometry", "import_hidden_entities", "import_all_surfaces_as_mesh_graphical_entities", "do_not_import_fillets", "do_not_import_dittos", "ditto_threshold", "center_view_on_imported_objects", "import_into_folders_matching_cad_file_hierarchy", "remove_empty_folders", "surface_normals_mode_1_or_2", "prompt_on_missing_components", "selective_import", "surface_compatibility_mode", "explode_surfaces", "cad_file_units_leave_blank_to_use_the_units_specified_in_the_file", "build_callout_views")
    CAD_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SOLIDS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SURFACES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_POLYGONIZED_SURFACES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_VECTORS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_POINTS_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ATTRIBUTES_METADATA_FIELD_NUMBER: _ClassVar[int]
    IMPORT_COOORDINATE_FRAMES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PLANES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_3D_CURVES_LINES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_3D_CURVES_CIRCLES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_3D_CURVES_GENERAL_CURVES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CONSTRUCTION_GEOMETRY_FIELD_NUMBER: _ClassVar[int]
    IMPORT_HIDDEN_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    IMPORT_ALL_SURFACES_AS_MESH_GRAPHICAL_ENTITIES_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_IMPORT_FILLETS_FIELD_NUMBER: _ClassVar[int]
    DO_NOT_IMPORT_DITTOS_FIELD_NUMBER: _ClassVar[int]
    DITTO_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    CENTER_VIEW_ON_IMPORTED_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_INTO_FOLDERS_MATCHING_CAD_FILE_HIERARCHY_FIELD_NUMBER: _ClassVar[int]
    REMOVE_EMPTY_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    SURFACE_NORMALS_MODE_1_OR_2_FIELD_NUMBER: _ClassVar[int]
    PROMPT_ON_MISSING_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
    SELECTIVE_IMPORT_FIELD_NUMBER: _ClassVar[int]
    SURFACE_COMPATIBILITY_MODE_FIELD_NUMBER: _ClassVar[int]
    EXPLODE_SURFACES_FIELD_NUMBER: _ClassVar[int]
    CAD_FILE_UNITS_LEAVE_BLANK_TO_USE_THE_UNITS_SPECIFIED_IN_THE_FILE_FIELD_NUMBER: _ClassVar[int]
    BUILD_CALLOUT_VIEWS_FIELD_NUMBER: _ClassVar[int]
    cad_file_name: _spatial_analyzer_values_pb2.FileReference
    import_solids: bool
    import_surfaces: bool
    import_polygonized_surfaces: bool
    import_annotations: bool
    import_vectors: bool
    import_points: bool
    point_group_name: str
    import_attributes_metadata: bool
    import_cooordinate_frames: bool
    import_planes: bool
    import_3d_curves_lines: bool
    import_3d_curves_circles: bool
    import_3d_curves_general_curves: bool
    import_construction_geometry: bool
    import_hidden_entities: bool
    import_all_surfaces_as_mesh_graphical_entities: bool
    do_not_import_fillets: bool
    do_not_import_dittos: bool
    ditto_threshold: int
    center_view_on_imported_objects: bool
    import_into_folders_matching_cad_file_hierarchy: bool
    remove_empty_folders: bool
    surface_normals_mode_1_or_2: int
    prompt_on_missing_components: bool
    selective_import: bool
    surface_compatibility_mode: bool
    explode_surfaces: bool
    cad_file_units_leave_blank_to_use_the_units_specified_in_the_file: str
    build_callout_views: bool
    def __init__(self, cad_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., import_solids: bool = ..., import_surfaces: bool = ..., import_polygonized_surfaces: bool = ..., import_annotations: bool = ..., import_vectors: bool = ..., import_points: bool = ..., point_group_name: _Optional[str] = ..., import_attributes_metadata: bool = ..., import_cooordinate_frames: bool = ..., import_planes: bool = ..., import_3d_curves_lines: bool = ..., import_3d_curves_circles: bool = ..., import_3d_curves_general_curves: bool = ..., import_construction_geometry: bool = ..., import_hidden_entities: bool = ..., import_all_surfaces_as_mesh_graphical_entities: bool = ..., do_not_import_fillets: bool = ..., do_not_import_dittos: bool = ..., ditto_threshold: _Optional[int] = ..., center_view_on_imported_objects: bool = ..., import_into_folders_matching_cad_file_hierarchy: bool = ..., remove_empty_folders: bool = ..., surface_normals_mode_1_or_2: _Optional[int] = ..., prompt_on_missing_components: bool = ..., selective_import: bool = ..., surface_compatibility_mode: bool = ..., explode_surfaces: bool = ..., cad_file_units_leave_blank_to_use_the_units_specified_in_the_file: _Optional[str] = ..., build_callout_views: bool = ...) -> None: ...

class DirectCadAccessResult(_message.Message):
    __slots__ = ("import_warnings", "import_warning_messages", "extents_min", "extents_max", "execution")
    IMPORT_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_WARNING_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    EXTENTS_MIN_FIELD_NUMBER: _ClassVar[int]
    EXTENTS_MAX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    import_warnings: bool
    import_warning_messages: str
    extents_min: _spatial_analyzer_values_pb2.Vector
    extents_max: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, import_warnings: bool = ..., import_warning_messages: _Optional[str] = ..., extents_min: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., extents_max: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportAsciiFrameSetRequest(_message.Message):
    __slots__ = ("ascii_file_path", "frame_set_container", "data_delimiter", "file_format", "include_export_format_info", "decimal_precision", "append")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    DATA_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_FORMAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    frame_set_container: _spatial_analyzer_values_pb2.CollectionObjectName
    data_delimiter: _spatial_analyzer_values_pb2.ExportDataDelimeterType
    file_format: _spatial_analyzer_values_pb2.AsciiFileFormat
    include_export_format_info: bool
    decimal_precision: int
    append: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., frame_set_container: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., data_delimiter: _Optional[_Union[_spatial_analyzer_values_pb2.ExportDataDelimeterType, str]] = ..., file_format: _Optional[_Union[_spatial_analyzer_values_pb2.AsciiFileFormat, str]] = ..., include_export_format_info: bool = ..., decimal_precision: _Optional[int] = ..., append: bool = ...) -> None: ...

class ExportAsciiFrameSetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportAsciiFramesRequest(_message.Message):
    __slots__ = ("ascii_file_path", "object_list", "export_frame_mode", "overwrite_existing_file")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_LIST_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FRAME_MODE_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    object_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    export_frame_mode: str
    overwrite_existing_file: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., object_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., export_frame_mode: _Optional[str] = ..., overwrite_existing_file: bool = ...) -> None: ...

class ExportAsciiFramesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportAsciiPointCloudsRequest(_message.Message):
    __slots__ = ("ascii_file_path", "point_cloud_list", "data_delimiter", "overwrite_existing_file", "show_progress_dialog", "include_cloud_point_labeling", "include_scan_direction_vector")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUD_LIST_FIELD_NUMBER: _ClassVar[int]
    DATA_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    SHOW_PROGRESS_DIALOG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOUD_POINT_LABELING_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SCAN_DIRECTION_VECTOR_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    point_cloud_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    data_delimiter: _spatial_analyzer_values_pb2.ExportDataDelimeterType
    overwrite_existing_file: bool
    show_progress_dialog: bool
    include_cloud_point_labeling: bool
    include_scan_direction_vector: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., point_cloud_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., data_delimiter: _Optional[_Union[_spatial_analyzer_values_pb2.ExportDataDelimeterType, str]] = ..., overwrite_existing_file: bool = ..., show_progress_dialog: bool = ..., include_cloud_point_labeling: bool = ..., include_scan_direction_vector: bool = ...) -> None: ...

class ExportAsciiPointCloudsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportAsciiPointSetRequest(_message.Message):
    __slots__ = ("ascii_file_path", "point_set_container", "data_delimiter", "target_name_format", "desired_coordinate_system", "include_target_offsets", "include_timestamps", "include_sa_version_and_frame_comments", "include_axis_comments", "include_export_format_info", "maximum_precision_scientific_notation", "decimal_precision", "append")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    POINT_SET_CONTAINER_FIELD_NUMBER: _ClassVar[int]
    DATA_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TARGET_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SA_VERSION_AND_FRAME_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AXIS_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_FORMAT_INFO_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PRECISION_SCIENTIFIC_NOTATION_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    point_set_container: _spatial_analyzer_values_pb2.CollectionObjectName
    data_delimiter: _spatial_analyzer_values_pb2.ExportDataDelimeterType
    target_name_format: _spatial_analyzer_values_pb2.ExportTargetNameFormat
    desired_coordinate_system: _spatial_analyzer_values_pb2.CoordinateSystemType
    include_target_offsets: bool
    include_timestamps: bool
    include_sa_version_and_frame_comments: bool
    include_axis_comments: bool
    include_export_format_info: bool
    maximum_precision_scientific_notation: bool
    decimal_precision: int
    append: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., point_set_container: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., data_delimiter: _Optional[_Union[_spatial_analyzer_values_pb2.ExportDataDelimeterType, str]] = ..., target_name_format: _Optional[_Union[_spatial_analyzer_values_pb2.ExportTargetNameFormat, str]] = ..., desired_coordinate_system: _Optional[_Union[_spatial_analyzer_values_pb2.CoordinateSystemType, str]] = ..., include_target_offsets: bool = ..., include_timestamps: bool = ..., include_sa_version_and_frame_comments: bool = ..., include_axis_comments: bool = ..., include_export_format_info: bool = ..., maximum_precision_scientific_notation: bool = ..., decimal_precision: _Optional[int] = ..., append: bool = ...) -> None: ...

class ExportAsciiPointSetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportAsciiPointsRequest(_message.Message):
    __slots__ = ("ascii_file_path", "group_names_to_export", "data_delimiter", "target_name_format", "desired_coordinate_system", "include_target_offsets", "include_target_comments", "include_timestamps", "include_tolerances", "include_coordinate_uncertainties", "include_sa_version_and_frame_comments", "include_axis_comments", "include_export_format_info", "include_weights", "include_measurement_details", "maximum_precision_scientific_notation", "decimal_precision", "append")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAMES_TO_EXPORT_FIELD_NUMBER: _ClassVar[int]
    DATA_DELIMITER_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    DESIRED_COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TARGET_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TARGET_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TOLERANCES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_COORDINATE_UNCERTAINTIES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_SA_VERSION_AND_FRAME_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AXIS_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EXPORT_FORMAT_INFO_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_WEIGHTS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MEASUREMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_PRECISION_SCIENTIFIC_NOTATION_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    APPEND_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    group_names_to_export: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionGroupName]
    data_delimiter: _spatial_analyzer_values_pb2.ExportDataDelimeterType
    target_name_format: _spatial_analyzer_values_pb2.ExportTargetNameFormat
    desired_coordinate_system: _spatial_analyzer_values_pb2.CoordinateSystemType
    include_target_offsets: bool
    include_target_comments: bool
    include_timestamps: bool
    include_tolerances: bool
    include_coordinate_uncertainties: bool
    include_sa_version_and_frame_comments: bool
    include_axis_comments: bool
    include_export_format_info: bool
    include_weights: bool
    include_measurement_details: bool
    maximum_precision_scientific_notation: bool
    decimal_precision: int
    append: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., group_names_to_export: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionGroupName, _Mapping]]] = ..., data_delimiter: _Optional[_Union[_spatial_analyzer_values_pb2.ExportDataDelimeterType, str]] = ..., target_name_format: _Optional[_Union[_spatial_analyzer_values_pb2.ExportTargetNameFormat, str]] = ..., desired_coordinate_system: _Optional[_Union[_spatial_analyzer_values_pb2.CoordinateSystemType, str]] = ..., include_target_offsets: bool = ..., include_target_comments: bool = ..., include_timestamps: bool = ..., include_tolerances: bool = ..., include_coordinate_uncertainties: bool = ..., include_sa_version_and_frame_comments: bool = ..., include_axis_comments: bool = ..., include_export_format_info: bool = ..., include_weights: bool = ..., include_measurement_details: bool = ..., maximum_precision_scientific_notation: bool = ..., decimal_precision: _Optional[int] = ..., append: bool = ...) -> None: ...

class ExportAsciiPointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportDxfRequest(_message.Message):
    __slots__ = ("dxf_file_path", "point_names", "cloud_names", "include_point_labels")
    DXF_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    CLOUD_NAMES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_POINT_LABELS_FIELD_NUMBER: _ClassVar[int]
    dxf_file_path: _spatial_analyzer_values_pb2.FileReference
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    cloud_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    include_point_labels: bool
    def __init__(self, dxf_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., cloud_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., include_point_labels: bool = ...) -> None: ...

class ExportDxfResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportEmbeddedFileRequest(_message.Message):
    __slots__ = ("embedded_file_collection_name", "embedded_file_name", "external_file_name", "replace_existing")
    EMBEDDED_FILE_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    embedded_file_collection_name: _spatial_analyzer_values_pb2.CollectionName
    embedded_file_name: str
    external_file_name: _spatial_analyzer_values_pb2.FileReference
    replace_existing: bool
    def __init__(self, embedded_file_collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., embedded_file_name: _Optional[str] = ..., external_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., replace_existing: bool = ...) -> None: ...

class ExportEmbeddedFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportHiddenPointBarXmlFileRequest(_message.Message):
    __slots__ = ("xml_file_path",)
    XML_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    xml_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, xml_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportHiddenPointBarXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportIgesFileEntireModelRequest(_message.Message):
    __slots__ = ("iges_file_path",)
    IGES_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    iges_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, iges_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportIgesFileEntireModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportIgesFilePartialModelRequest(_message.Message):
    __slots__ = ("iges_file_path", "object_name_list")
    IGES_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    iges_file_path: _spatial_analyzer_values_pb2.FileReference
    object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, iges_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ExportIgesFilePartialModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportPtxPointCloudsRequest(_message.Message):
    __slots__ = ("ptx_file_path", "point_cloud_list", "overwrite_existing_file", "show_progress_dialog")
    PTX_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    POINT_CLOUD_LIST_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    SHOW_PROGRESS_DIALOG_FIELD_NUMBER: _ClassVar[int]
    ptx_file_path: _spatial_analyzer_values_pb2.FileReference
    point_cloud_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    overwrite_existing_file: bool
    show_progress_dialog: bool
    def __init__(self, ptx_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., point_cloud_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., overwrite_existing_file: bool = ..., show_progress_dialog: bool = ...) -> None: ...

class ExportPtxPointCloudsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportQdasCharacteristicsRequest(_message.Message):
    __slots__ = ("qdas_export_file_path", "k1001_part_number", "k1002_part_description", "k1071_supplier_number", "k1072_supplier_description", "k1203_reason_for_test", "k1303_plant", "k1900_part_remark", "k0006_batch_number", "k0014_part_id", "k0053_order_number", "k0004_date_time_stamp", "k0008_operator_identifier", "k0010_machine_identifier", "k0012_gage_identifier", "relationship_list", "feature_check_list", "vector_group_list")
    QDAS_EXPORT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    K1001_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K1002_PART_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    K1071_SUPPLIER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K1072_SUPPLIER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    K1203_REASON_FOR_TEST_FIELD_NUMBER: _ClassVar[int]
    K1303_PLANT_FIELD_NUMBER: _ClassVar[int]
    K1900_PART_REMARK_FIELD_NUMBER: _ClassVar[int]
    K0006_BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K0014_PART_ID_FIELD_NUMBER: _ClassVar[int]
    K0053_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K0004_DATE_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    K0008_OPERATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    K0010_MACHINE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    K0012_GAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_LIST_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECK_LIST_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    qdas_export_file_path: _spatial_analyzer_values_pb2.FileReference
    k1001_part_number: str
    k1002_part_description: str
    k1071_supplier_number: str
    k1072_supplier_description: str
    k1203_reason_for_test: str
    k1303_plant: str
    k1900_part_remark: str
    k0006_batch_number: str
    k0014_part_id: str
    k0053_order_number: str
    k0004_date_time_stamp: str
    k0008_operator_identifier: int
    k0010_machine_identifier: int
    k0012_gage_identifier: int
    relationship_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    feature_check_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    vector_group_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, qdas_export_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., k1001_part_number: _Optional[str] = ..., k1002_part_description: _Optional[str] = ..., k1071_supplier_number: _Optional[str] = ..., k1072_supplier_description: _Optional[str] = ..., k1203_reason_for_test: _Optional[str] = ..., k1303_plant: _Optional[str] = ..., k1900_part_remark: _Optional[str] = ..., k0006_batch_number: _Optional[str] = ..., k0014_part_id: _Optional[str] = ..., k0053_order_number: _Optional[str] = ..., k0004_date_time_stamp: _Optional[str] = ..., k0008_operator_identifier: _Optional[int] = ..., k0010_machine_identifier: _Optional[int] = ..., k0012_gage_identifier: _Optional[int] = ..., relationship_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., feature_check_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., vector_group_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ExportQdasCharacteristicsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportQdasDataListRequest(_message.Message):
    __slots__ = ("qdas_export_file_path",)
    QDAS_EXPORT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    qdas_export_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, qdas_export_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportQdasDataListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportScanStripeMeshToStlFileRequest(_message.Message):
    __slots__ = ("stl_file_path", "mesh")
    STL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    MESH_FIELD_NUMBER: _ClassVar[int]
    stl_file_path: _spatial_analyzer_values_pb2.FileReference
    mesh: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, stl_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., mesh: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ExportScanStripeMeshToStlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportStepFileEntireModelRequest(_message.Message):
    __slots__ = ("step_file_path",)
    STEP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    step_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, step_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportStepFileEntireModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportStepFilePartialModelRequest(_message.Message):
    __slots__ = ("step_file_path", "object_name_list")
    STEP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    step_file_path: _spatial_analyzer_values_pb2.FileReference
    object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, step_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ExportStepFilePartialModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportVdaFsFileEntireModelRequest(_message.Message):
    __slots__ = ("vda_fs_file_path",)
    VDA_FS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    vda_fs_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, vda_fs_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ExportVdaFsFileEntireModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportVdaFsFilePartialModelRequest(_message.Message):
    __slots__ = ("vda_fs_file_path", "object_name_list")
    VDA_FS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    vda_fs_file_path: _spatial_analyzer_values_pb2.FileReference
    object_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, vda_fs_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., object_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ExportVdaFsFilePartialModelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportVectorContainerToAsciiFileRequest(_message.Message):
    __slots__ = ("ascii_file_path", "vector_groups_to_export", "overwrite_existing_file_false_append", "use_full_precision_scientific_notation", "vector_name_format", "include_vector_length")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUPS_TO_EXPORT_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FALSE_APPEND_FIELD_NUMBER: _ClassVar[int]
    USE_FULL_PRECISION_SCIENTIFIC_NOTATION_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FORMAT_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VECTOR_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    vector_groups_to_export: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionVectorGroupName]
    overwrite_existing_file_false_append: bool
    use_full_precision_scientific_notation: bool
    vector_name_format: _spatial_analyzer_values_pb2.ExportVectorNameFormat
    include_vector_length: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., vector_groups_to_export: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]]] = ..., overwrite_existing_file_false_append: bool = ..., use_full_precision_scientific_notation: bool = ..., vector_name_format: _Optional[_Union[_spatial_analyzer_values_pb2.ExportVectorNameFormat, str]] = ..., include_vector_length: bool = ...) -> None: ...

class ExportVectorContainerToAsciiFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FindFilesInDirectoryRequest(_message.Message):
    __slots__ = ("directory", "file_name_pattern", "recursive")
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    directory: str
    file_name_pattern: str
    recursive: bool
    def __init__(self, directory: _Optional[str] = ..., file_name_pattern: _Optional[str] = ..., recursive: bool = ...) -> None: ...

class FindFilesInDirectoryResult(_message.Message):
    __slots__ = ("files", "execution")
    FILES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, files: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class FindSubDirectoriesInDirectoryRequest(_message.Message):
    __slots__ = ("directory", "recursive")
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    directory: str
    recursive: bool
    def __init__(self, directory: _Optional[str] = ..., recursive: bool = ...) -> None: ...

class FindSubDirectoriesInDirectoryResult(_message.Message):
    __slots__ = ("sub_directories", "execution")
    SUB_DIRECTORIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    sub_directories: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, sub_directories: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetBooleanFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "boolean_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    boolean_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., boolean_name: _Optional[str] = ...) -> None: ...

class GetBooleanFromDataShareFileResult(_message.Message):
    __slots__ = ("boolean_value", "execution")
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    boolean_value: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, boolean_value: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetDoubleFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "double_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    double_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., double_name: _Optional[str] = ...) -> None: ...

class GetDoubleFromDataShareFileResult(_message.Message):
    __slots__ = ("double_value", "execution")
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    double_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, double_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIntegerFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "integer_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INTEGER_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    integer_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., integer_name: _Optional[str] = ...) -> None: ...

class GetIntegerFromDataShareFileResult(_message.Message):
    __slots__ = ("integer_value", "execution")
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    integer_value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, integer_value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetQdasCatalogEntriesRequest(_message.Message):
    __slots__ = ("k_field_target",)
    K_FIELD_TARGET_FIELD_NUMBER: _ClassVar[int]
    k_field_target: str
    def __init__(self, k_field_target: _Optional[str] = ...) -> None: ...

class GetQdasCatalogEntriesResult(_message.Message):
    __slots__ = ("catalog_entries", "execution")
    CATALOG_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    catalog_entries: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, catalog_entries: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetStringFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "string_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    STRING_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    string_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., string_name: _Optional[str] = ...) -> None: ...

class GetStringFromDataShareFileResult(_message.Message):
    __slots__ = ("string_value", "execution")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, string_value: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTransformFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "transform_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    transform_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., transform_name: _Optional[str] = ...) -> None: ...

class GetTransformFromDataShareFileResult(_message.Message):
    __slots__ = ("transform_value", "execution")
    TRANSFORM_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform_value: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform_value: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetVectorFromDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "vector_name")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    vector_name: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., vector_name: _Optional[str] = ...) -> None: ...

class GetVectorFromDataShareFileResult(_message.Message):
    __slots__ = ("vector_value", "execution")
    VECTOR_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_value: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_value: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetWorkingDirectoryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWorkingDirectoryResult(_message.Message):
    __slots__ = ("directory", "execution")
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    directory: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, directory: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportAsciiPredefinedFormatsRequest(_message.Message):
    __slots__ = ("ascii_file_path", "file_format", "units", "angular_units", "group_name", "import_as_cloud", "ensure_new_point_group", "ensure_unique_names")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_UNITS_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_AS_CLOUD_FIELD_NUMBER: _ClassVar[int]
    ENSURE_NEW_POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    ENSURE_UNIQUE_NAMES_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    file_format: _spatial_analyzer_values_pb2.AsciiFileFormat
    units: _spatial_analyzer_values_pb2.DistanceUnits
    angular_units: _spatial_analyzer_values_pb2.AngularUnits
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    import_as_cloud: bool
    ensure_new_point_group: bool
    ensure_unique_names: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., file_format: _Optional[_Union[_spatial_analyzer_values_pb2.AsciiFileFormat, str]] = ..., units: _Optional[_Union[_spatial_analyzer_values_pb2.DistanceUnits, str]] = ..., angular_units: _Optional[_Union[_spatial_analyzer_values_pb2.AngularUnits, str]] = ..., group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., import_as_cloud: bool = ..., ensure_new_point_group: bool = ..., ensure_unique_names: bool = ...) -> None: ...

class ImportAsciiPredefinedFormatsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportAsciiPredefinedFrameSetFormatsRequest(_message.Message):
    __slots__ = ("ascii_file_path", "file_format", "units", "angular_units", "frame_set_container_name", "ensure_unique_name")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_UNITS_FIELD_NUMBER: _ClassVar[int]
    FRAME_SET_CONTAINER_NAME_FIELD_NUMBER: _ClassVar[int]
    ENSURE_UNIQUE_NAME_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    file_format: _spatial_analyzer_values_pb2.AsciiFileFormat
    units: _spatial_analyzer_values_pb2.DistanceUnits
    angular_units: _spatial_analyzer_values_pb2.AngularUnits
    frame_set_container_name: _spatial_analyzer_values_pb2.CollectionObjectName
    ensure_unique_name: bool
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., file_format: _Optional[_Union[_spatial_analyzer_values_pb2.AsciiFileFormat, str]] = ..., units: _Optional[_Union[_spatial_analyzer_values_pb2.DistanceUnits, str]] = ..., angular_units: _Optional[_Union[_spatial_analyzer_values_pb2.AngularUnits, str]] = ..., frame_set_container_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., ensure_unique_name: bool = ...) -> None: ...

class ImportAsciiPredefinedFrameSetFormatsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportE57FileRequest(_message.Message):
    __slots__ = ("e57_file_path", "save_converted_file", "use_square_root_of_intensity", "automatically_close_converter", "prioritize_color_over_intensity", "import_scan_blocks_as_separate_clouds", "units")
    E57_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SAVE_CONVERTED_FILE_FIELD_NUMBER: _ClassVar[int]
    USE_SQUARE_ROOT_OF_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    AUTOMATICALLY_CLOSE_CONVERTER_FIELD_NUMBER: _ClassVar[int]
    PRIORITIZE_COLOR_OVER_INTENSITY_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SCAN_BLOCKS_AS_SEPARATE_CLOUDS_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    e57_file_path: _spatial_analyzer_values_pb2.FileReference
    save_converted_file: bool
    use_square_root_of_intensity: bool
    automatically_close_converter: bool
    prioritize_color_over_intensity: bool
    import_scan_blocks_as_separate_clouds: bool
    units: _spatial_analyzer_values_pb2.DistanceUnits
    def __init__(self, e57_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., save_converted_file: bool = ..., use_square_root_of_intensity: bool = ..., automatically_close_converter: bool = ..., prioritize_color_over_intensity: bool = ..., import_scan_blocks_as_separate_clouds: bool = ..., units: _Optional[_Union[_spatial_analyzer_values_pb2.DistanceUnits, str]] = ...) -> None: ...

class ImportE57FileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportFileAsEmbeddedFileRequest(_message.Message):
    __slots__ = ("external_file_name", "replace_existing")
    EXTERNAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    external_file_name: _spatial_analyzer_values_pb2.FileReference
    replace_existing: bool
    def __init__(self, external_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., replace_existing: bool = ...) -> None: ...

class ImportFileAsEmbeddedFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportFileAsPictureRequest(_message.Message):
    __slots__ = ("external_file_name", "replace_existing")
    EXTERNAL_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    external_file_name: _spatial_analyzer_values_pb2.FileReference
    replace_existing: bool
    def __init__(self, external_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., replace_existing: bool = ...) -> None: ...

class ImportFileAsPictureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportHiddenPointBarXmlFileRequest(_message.Message):
    __slots__ = ("xml_file_path", "replace_existing_entries")
    XML_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    xml_file_path: _spatial_analyzer_values_pb2.FileReference
    replace_existing_entries: bool
    def __init__(self, xml_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., replace_existing_entries: bool = ...) -> None: ...

class ImportHiddenPointBarXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportIgesFileRequest(_message.Message):
    __slots__ = ("iges_file_path",)
    IGES_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    iges_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, iges_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportIgesFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportLeicaGsiFileRequest(_message.Message):
    __slots__ = ("instrument_id", "group_name", "file_path")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportLeicaGsiFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportLeicaSdbFileRequest(_message.Message):
    __slots__ = ("instrument_id", "scan_cloud_name", "file_path")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCAN_CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    scan_cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., scan_cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportLeicaSdbFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportMpFileAsEmbeddedMpRequest(_message.Message):
    __slots__ = ("external_mp_file_name", "replace_existing")
    EXTERNAL_MP_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPLACE_EXISTING_FIELD_NUMBER: _ClassVar[int]
    external_mp_file_name: _spatial_analyzer_values_pb2.FileReference
    replace_existing: bool
    def __init__(self, external_mp_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., replace_existing: bool = ...) -> None: ...

class ImportMpFileAsEmbeddedMpResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportNominalsFromXmlFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportNominalsFromXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportPolyworksFileRequest(_message.Message):
    __slots__ = ("cloud_name", "file_path")
    CLOUD_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    cloud_name: _spatial_analyzer_values_pb2.CollectionObjectName
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, cloud_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportPolyworksFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportQdasCatalogFileRequest(_message.Message):
    __slots__ = ("qdas_dfd_file_path",)
    QDAS_DFD_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    qdas_dfd_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, qdas_dfd_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportQdasCatalogFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportSaFileRequest(_message.Message):
    __slots__ = ("sa_file_name", "allow_operator_selections", "selected_collections_optional")
    SA_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_OPERATOR_SELECTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_COLLECTIONS_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    sa_file_name: _spatial_analyzer_values_pb2.FileReference
    allow_operator_selections: bool
    selected_collections_optional: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sa_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., allow_operator_selections: bool = ..., selected_collections_optional: _Optional[_Iterable[str]] = ...) -> None: ...

class ImportSaFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportSaWindowsPlacementRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportSaWindowsPlacementResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportSatFileRequest(_message.Message):
    __slots__ = ("sat_file_path",)
    SAT_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    sat_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, sat_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportSatFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportStepFileRequest(_message.Message):
    __slots__ = ("step_file_path", "display_entity_filters", "display_residuals")
    STEP_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_ENTITY_FILTERS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_RESIDUALS_FIELD_NUMBER: _ClassVar[int]
    step_file_path: _spatial_analyzer_values_pb2.FileReference
    display_entity_filters: bool
    display_residuals: bool
    def __init__(self, step_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., display_entity_filters: bool = ..., display_residuals: bool = ...) -> None: ...

class ImportStepFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportStlFileRequest(_message.Message):
    __slots__ = ("stl_file_path", "units", "import_mesh", "import_point_cloud")
    STL_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    UNITS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_MESH_FIELD_NUMBER: _ClassVar[int]
    IMPORT_POINT_CLOUD_FIELD_NUMBER: _ClassVar[int]
    stl_file_path: _spatial_analyzer_values_pb2.FileReference
    units: _spatial_analyzer_values_pb2.DistanceUnits
    import_mesh: bool
    import_point_cloud: bool
    def __init__(self, stl_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., units: _Optional[_Union[_spatial_analyzer_values_pb2.DistanceUnits, str]] = ..., import_mesh: bool = ..., import_point_cloud: bool = ...) -> None: ...

class ImportStlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportVdaFsFileRequest(_message.Message):
    __slots__ = ("vda_fs_file_path",)
    VDA_FS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    vda_fs_file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, vda_fs_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportVdaFsFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportVstarsXyzFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportVstarsXyzFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportVstarsCamerasRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportVstarsCamerasResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LoadHtmlFormRequest(_message.Message):
    __slots__ = ("input_html_form_path", "window_width", "window_height", "input_data_share_file_path", "output_data_share_file_path", "save_in_binary_format", "save_button_text", "cancel_button_text", "hide_save_and_cancel_buttons")
    INPUT_HTML_FORM_PATH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SAVE_IN_BINARY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    SAVE_BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
    CANCEL_BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
    HIDE_SAVE_AND_CANCEL_BUTTONS_FIELD_NUMBER: _ClassVar[int]
    input_html_form_path: _spatial_analyzer_values_pb2.FileReference
    window_width: int
    window_height: int
    input_data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    output_data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    save_in_binary_format: bool
    save_button_text: str
    cancel_button_text: str
    hide_save_and_cancel_buttons: bool
    def __init__(self, input_html_form_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ..., input_data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., output_data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., save_in_binary_format: bool = ..., save_button_text: _Optional[str] = ..., cancel_button_text: _Optional[str] = ..., hide_save_and_cancel_buttons: bool = ...) -> None: ...

class LoadHtmlFormResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LoadHtmlFormInEdgeBrowserRequest(_message.Message):
    __slots__ = ("input_html_form_path", "window_width", "window_height", "input_data_share_file_path", "output_data_share_file_path", "save_in_binary_format")
    INPUT_HTML_FORM_PATH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    INPUT_DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SAVE_IN_BINARY_FORMAT_FIELD_NUMBER: _ClassVar[int]
    input_html_form_path: _spatial_analyzer_values_pb2.FileReference
    window_width: int
    window_height: int
    input_data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    output_data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    save_in_binary_format: bool
    def __init__(self, input_html_form_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ..., input_data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., output_data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., save_in_binary_format: bool = ...) -> None: ...

class LoadHtmlFormInEdgeBrowserResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeEmbeddedFileNameListRequest(_message.Message):
    __slots__ = ("collection_wildcard_criteria", "file_name_pattern")
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_PATTERN_FIELD_NUMBER: _ClassVar[int]
    collection_wildcard_criteria: str
    file_name_pattern: str
    def __init__(self, collection_wildcard_criteria: _Optional[str] = ..., file_name_pattern: _Optional[str] = ...) -> None: ...

class MakeEmbeddedFileNameListResult(_message.Message):
    __slots__ = ("embedded_files", "execution")
    EMBEDDED_FILES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    embedded_files: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, embedded_files: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MergeMeasurementsIntoXmlFileRequest(_message.Message):
    __slots__ = ("file_path", "group_name")
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MergeMeasurementsIntoXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NewSaFileRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NewSaFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class OpenSaFileRequest(_message.Message):
    __slots__ = ("sa_file_name",)
    SA_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    sa_file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, sa_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class OpenSaFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class OpenTemplateFileRequest(_message.Message):
    __slots__ = ("template_file_name",)
    TEMPLATE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, template_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class OpenTemplateFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PopPolyBayAnalysisWindowRequest(_message.Message):
    __slots__ = ("materials_file_path", "bay_file_path")
    MATERIALS_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BAY_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    materials_file_path: str
    bay_file_path: str
    def __init__(self, materials_file_path: _Optional[str] = ..., bay_file_path: _Optional[str] = ...) -> None: ...

class PopPolyBayAnalysisWindowResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PrepareQdasDataListRequest(_message.Message):
    __slots__ = ("k1001_part_number", "k1002_part_description", "k1071_supplier_number", "k1072_supplier_description", "k1203_reason_for_test", "k1303_plant", "k1900_part_remark", "k0006_batch_number", "k0014_part_id", "k0053_order_number", "k0004_date_time_stamp", "k0008_operator_identifier", "k0010_machine_identifier", "k0012_gage_identifier", "relationship_list", "feature_check_list", "vector_group_list")
    K1001_PART_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K1002_PART_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    K1071_SUPPLIER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K1072_SUPPLIER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    K1203_REASON_FOR_TEST_FIELD_NUMBER: _ClassVar[int]
    K1303_PLANT_FIELD_NUMBER: _ClassVar[int]
    K1900_PART_REMARK_FIELD_NUMBER: _ClassVar[int]
    K0006_BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K0014_PART_ID_FIELD_NUMBER: _ClassVar[int]
    K0053_ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    K0004_DATE_TIME_STAMP_FIELD_NUMBER: _ClassVar[int]
    K0008_OPERATOR_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    K0010_MACHINE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    K0012_GAGE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_LIST_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECK_LIST_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_LIST_FIELD_NUMBER: _ClassVar[int]
    k1001_part_number: str
    k1002_part_description: str
    k1071_supplier_number: str
    k1072_supplier_description: str
    k1203_reason_for_test: str
    k1303_plant: str
    k1900_part_remark: str
    k0006_batch_number: str
    k0014_part_id: str
    k0053_order_number: str
    k0004_date_time_stamp: str
    k0008_operator_identifier: int
    k0010_machine_identifier: int
    k0012_gage_identifier: int
    relationship_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    feature_check_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    vector_group_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, k1001_part_number: _Optional[str] = ..., k1002_part_description: _Optional[str] = ..., k1071_supplier_number: _Optional[str] = ..., k1072_supplier_description: _Optional[str] = ..., k1203_reason_for_test: _Optional[str] = ..., k1303_plant: _Optional[str] = ..., k1900_part_remark: _Optional[str] = ..., k0006_batch_number: _Optional[str] = ..., k0014_part_id: _Optional[str] = ..., k0053_order_number: _Optional[str] = ..., k0004_date_time_stamp: _Optional[str] = ..., k0008_operator_identifier: _Optional[int] = ..., k0010_machine_identifier: _Optional[int] = ..., k0012_gage_identifier: _Optional[int] = ..., relationship_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., feature_check_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., vector_group_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class PrepareQdasDataListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameGeneralFileRequest(_message.Message):
    __slots__ = ("source_file_name", "destination_file_name", "overwrite")
    SOURCE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    source_file_name: _spatial_analyzer_values_pb2.FileReference
    destination_file_name: _spatial_analyzer_values_pb2.FileReference
    overwrite: bool
    def __init__(self, source_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., destination_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., overwrite: bool = ...) -> None: ...

class RenameGeneralFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SaveResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveAsReadOnlyTemplateRequest(_message.Message):
    __slots__ = ("template_file_name",)
    TEMPLATE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, template_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SaveAsReadOnlyTemplateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveAsRequest(_message.Message):
    __slots__ = ("file_name", "add_serial_number", "optional_number")
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ADD_SERIAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    file_name: _spatial_analyzer_values_pb2.FileReference
    add_serial_number: bool
    optional_number: int
    def __init__(self, file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., add_serial_number: bool = ..., optional_number: _Optional[int] = ...) -> None: ...

class SaveAsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetBooleanInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "boolean_name", "boolean_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_NAME_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    boolean_name: str
    boolean_value: bool
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., boolean_name: _Optional[str] = ..., boolean_value: bool = ...) -> None: ...

class SetBooleanInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDoubleInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "double_name", "double_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    double_name: str
    double_value: float
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., double_name: _Optional[str] = ..., double_value: _Optional[float] = ...) -> None: ...

class SetDoubleInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetIntegerInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "integer_name", "integer_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INTEGER_NAME_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    integer_name: str
    integer_value: int
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., integer_name: _Optional[str] = ..., integer_value: _Optional[int] = ...) -> None: ...

class SetIntegerInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetStringInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "string_name", "string_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    STRING_NAME_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    string_name: str
    string_value: str
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., string_name: _Optional[str] = ..., string_value: _Optional[str] = ...) -> None: ...

class SetStringInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTransformInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "transform_name", "transform_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSFORM_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    transform_name: str
    transform_value: _spatial_analyzer_values_pb2.Transform
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., transform_name: _Optional[str] = ..., transform_value: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetTransformInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorInDataShareFileRequest(_message.Message):
    __slots__ = ("data_share_file_path", "vector_name", "vector_value")
    DATA_SHARE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_VALUE_FIELD_NUMBER: _ClassVar[int]
    data_share_file_path: _spatial_analyzer_values_pb2.FileReference
    vector_name: str
    vector_value: _spatial_analyzer_values_pb2.Vector
    def __init__(self, data_share_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., vector_name: _Optional[str] = ..., vector_value: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class SetVectorInDataShareFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TerminateAllRunningMPsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TerminateAllRunningMPsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class UseNrkxmlLibraryRequest(_message.Message):
    __slots__ = ("use_library",)
    USE_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    use_library: bool
    def __init__(self, use_library: bool = ...) -> None: ...

class UseNrkxmlLibraryResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class VerifyGeneralFileExistsRequest(_message.Message):
    __slots__ = ("file_name",)
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class VerifyGeneralFileExistsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class VerifyMpFileExistsRequest(_message.Message):
    __slots__ = ("mp_file_name",)
    MP_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    mp_file_name: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, mp_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class VerifyMpFileExistsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
