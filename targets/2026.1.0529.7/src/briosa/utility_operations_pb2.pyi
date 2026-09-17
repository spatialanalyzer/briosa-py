from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CloseAllWatchWindowsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseAllWatchWindowsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteFolderRequest(_message.Message):
    __slots__ = ("folder_path",)
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    def __init__(self, folder_path: _Optional[str] = ...) -> None: ...

class DeleteFolderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteItemsRequest(_message.Message):
    __slots__ = ("item_list",)
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, item_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class DeleteItemsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteObjectsRequest(_message.Message):
    __slots__ = ("object_names",)
    OBJECT_NAMES_FIELD_NUMBER: _ClassVar[int]
    object_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, object_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class DeleteObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetActiveLanguageRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActiveLanguageResult(_message.Message):
    __slots__ = ("language_file_name", "custom_language", "execution")
    LANGUAGE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    language_file_name: _spatial_analyzer_values_pb2.FileReference
    custom_language: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, language_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., custom_language: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetActiveUnitsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActiveUnitsResult(_message.Message):
    __slots__ = ("length", "angular", "temperature", "execution")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    length: str
    angular: str
    temperature: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, length: _Optional[str] = ..., angular: _Optional[str] = ..., temperature: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetAngularRepresentationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetAngularRepresentationResult(_message.Message):
    __slots__ = ("value_0_360_false_180", "execution")
    VALUE_0_360_FALSE_180_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value_0_360_false_180: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value_0_360_false_180: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCollectionNotesRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ...) -> None: ...

class GetCollectionNotesResult(_message.Message):
    __slots__ = ("notes", "execution")
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, notes: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFolderCollectionsRequest(_message.Message):
    __slots__ = ("folder_path",)
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    def __init__(self, folder_path: _Optional[str] = ...) -> None: ...

class GetFolderCollectionsResult(_message.Message):
    __slots__ = ("collection_list", "execution")
    COLLECTION_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    collection_list: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, collection_list: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFolderNotesRequest(_message.Message):
    __slots__ = ("folder_path",)
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    def __init__(self, folder_path: _Optional[str] = ...) -> None: ...

class GetFolderNotesResult(_message.Message):
    __slots__ = ("notes", "execution")
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, notes: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetFoldersByWildcardRequest(_message.Message):
    __slots__ = ("search_string", "case_sensitive_search")
    SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    CASE_SENSITIVE_SEARCH_FIELD_NUMBER: _ClassVar[int]
    search_string: str
    case_sensitive_search: bool
    def __init__(self, search_string: _Optional[str] = ..., case_sensitive_search: bool = ...) -> None: ...

class GetFoldersByWildcardResult(_message.Message):
    __slots__ = ("folder_list", "execution")
    FOLDER_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    folder_list: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, folder_list: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetObjectNotesRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetObjectNotesResult(_message.Message):
    __slots__ = ("notes", "execution")
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, notes: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetOpcDaTagValueDoubleRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name",)
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ...) -> None: ...

class GetOpcDaTagValueDoubleResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetOpcDaTagValueIntegerRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name",)
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ...) -> None: ...

class GetOpcDaTagValueIntegerResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetOpcDaTagValueStringRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name",)
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ...) -> None: ...

class GetOpcDaTagValueStringResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointNotesRequest(_message.Message):
    __slots__ = ("point",)
    POINT_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class GetPointNotesResult(_message.Message):
    __slots__ = ("notes", "execution")
    NOTES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, notes: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetScreenResolutionRequest(_message.Message):
    __slots__ = ("display_1_primary",)
    DISPLAY_1_PRIMARY_FIELD_NUMBER: _ClassVar[int]
    display_1_primary: int
    def __init__(self, display_1_primary: _Optional[int] = ...) -> None: ...

class GetScreenResolutionResult(_message.Message):
    __slots__ = ("integer_window_top_left_x_position", "integer_window_top_left_y_position", "integer_width", "integer_height", "view_width", "view_height", "execution")
    INTEGER_WINDOW_TOP_LEFT_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    INTEGER_WINDOW_TOP_LEFT_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    INTEGER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    INTEGER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    VIEW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    VIEW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    integer_window_top_left_x_position: int
    integer_window_top_left_y_position: int
    integer_width: int
    integer_height: int
    view_width: int
    view_height: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, integer_window_top_left_x_position: _Optional[int] = ..., integer_window_top_left_y_position: _Optional[int] = ..., integer_width: _Optional[int] = ..., integer_height: _Optional[int] = ..., view_width: _Optional[int] = ..., view_height: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetWorkingFramePropertiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetWorkingFramePropertiesResult(_message.Message):
    __slots__ = ("frame_name", "collection_name", "working_frame", "execution")
    FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKING_FRAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    frame_name: str
    collection_name: str
    working_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, frame_name: _Optional[str] = ..., collection_name: _Optional[str] = ..., working_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class IncrementPointNameRequest(_message.Message):
    __slots__ = ("base_point_name", "increment")
    BASE_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    base_point_name: _spatial_analyzer_values_pb2.PointName
    increment: int
    def __init__(self, base_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., increment: _Optional[int] = ...) -> None: ...

class IncrementPointNameResult(_message.Message):
    __slots__ = ("resultant_point_name", "execution")
    RESULTANT_POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_point_name: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LockImportedItemsRequest(_message.Message):
    __slots__ = ("lock_items",)
    LOCK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    lock_items: bool
    def __init__(self, lock_items: bool = ...) -> None: ...

class LockImportedItemsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LockUnlockSelectedItemsRequest(_message.Message):
    __slots__ = ("item_list", "instruments", "lock_items")
    ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    LOCK_ITEMS_FIELD_NUMBER: _ClassVar[int]
    item_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    lock_items: bool
    def __init__(self, item_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., lock_items: bool = ...) -> None: ...

class LockUnlockSelectedItemsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LockUnlockTrappingControlRequest(_message.Message):
    __slots__ = ("relationship_ref_list", "feature_check_ref_list", "datum_ref_list", "lock_out_trapping")
    RELATIONSHIP_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECK_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    DATUM_REF_LIST_FIELD_NUMBER: _ClassVar[int]
    LOCK_OUT_TRAPPING_FIELD_NUMBER: _ClassVar[int]
    relationship_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    feature_check_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    datum_ref_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    lock_out_trapping: bool
    def __init__(self, relationship_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., feature_check_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., datum_ref_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., lock_out_trapping: bool = ...) -> None: ...

class LockUnlockTrappingControlResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveCollectionToFolderRequest(_message.Message):
    __slots__ = ("collection", "folder_path")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    folder_path: str
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., folder_path: _Optional[str] = ...) -> None: ...

class MoveCollectionToFolderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveFolderToFolderRequest(_message.Message):
    __slots__ = ("source_folder_path", "destination_folder_path")
    SOURCE_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    source_folder_path: str
    destination_folder_path: str
    def __init__(self, source_folder_path: _Optional[str] = ..., destination_folder_path: _Optional[str] = ...) -> None: ...

class MoveFolderToFolderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveInstrumentsDragGraphicallyRequest(_message.Message):
    __slots__ = ("instruments",)
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    def __init__(self, instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ...) -> None: ...

class MoveInstrumentsDragGraphicallyResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveObjectsDragGraphicallyRequest(_message.Message):
    __slots__ = ("objects",)
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class MoveObjectsDragGraphicallyResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ScaleObjectsRequest(_message.Message):
    __slots__ = ("objects", "scale_factor")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    scale_factor: float
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., scale_factor: _Optional[float] = ...) -> None: ...

class ScaleObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetActiveCustomLanguageRequest(_message.Message):
    __slots__ = ("language_file_name", "font")
    LANGUAGE_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    language_file_name: _spatial_analyzer_values_pb2.FileReference
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, language_file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class SetActiveCustomLanguageResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetActiveUnitsRequest(_message.Message):
    __slots__ = ("length", "display_inch_fractions", "inch_fraction_denominator", "simplify_inch_fraction", "temperature", "angular")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_INCH_FRACTIONS_FIELD_NUMBER: _ClassVar[int]
    INCH_FRACTION_DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
    SIMPLIFY_INCH_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    ANGULAR_FIELD_NUMBER: _ClassVar[int]
    length: _spatial_analyzer_values_pb2.DistanceUnits
    display_inch_fractions: bool
    inch_fraction_denominator: float
    simplify_inch_fraction: bool
    temperature: _spatial_analyzer_values_pb2.TemperatureUnits
    angular: _spatial_analyzer_values_pb2.AngularUnits
    def __init__(self, length: _Optional[_Union[_spatial_analyzer_values_pb2.DistanceUnits, str]] = ..., display_inch_fractions: bool = ..., inch_fraction_denominator: _Optional[float] = ..., simplify_inch_fraction: bool = ..., temperature: _Optional[_Union[_spatial_analyzer_values_pb2.TemperatureUnits, str]] = ..., angular: _Optional[_Union[_spatial_analyzer_values_pb2.AngularUnits, str]] = ...) -> None: ...

class SetActiveUnitsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAngularRepresentationRequest(_message.Message):
    __slots__ = ("value_0_360_false_180",)
    VALUE_0_360_FALSE_180_FIELD_NUMBER: _ClassVar[int]
    value_0_360_false_180: bool
    def __init__(self, value_0_360_false_180: bool = ...) -> None: ...

class SetAngularRepresentationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAutoEventCreationRequest(_message.Message):
    __slots__ = ("active",)
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    def __init__(self, active: bool = ...) -> None: ...

class SetAutoEventCreationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAutomaticBackupStateRequest(_message.Message):
    __slots__ = ("auto_job_file_restore_points_active", "auto_measurements_backup_active")
    AUTO_JOB_FILE_RESTORE_POINTS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    AUTO_MEASUREMENTS_BACKUP_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    auto_job_file_restore_points_active: bool
    auto_measurements_backup_active: bool
    def __init__(self, auto_job_file_restore_points_active: bool = ..., auto_measurements_backup_active: bool = ...) -> None: ...

class SetAutomaticBackupStateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetAutomaticRelationshipConstructionStateRequest(_message.Message):
    __slots__ = ("active",)
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    def __init__(self, active: bool = ...) -> None: ...

class SetAutomaticRelationshipConstructionStateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCollectionNotesRequest(_message.Message):
    __slots__ = ("collection", "notes", "append_false_overwrite")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    APPEND_FALSE_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    collection: _spatial_analyzer_values_pb2.CollectionName
    notes: _containers.RepeatedScalarFieldContainer[str]
    append_false_overwrite: bool
    def __init__(self, collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., notes: _Optional[_Iterable[str]] = ..., append_false_overwrite: bool = ...) -> None: ...

class SetCollectionNotesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDecimalDigitsForDisplayRequest(_message.Message):
    __slots__ = ("length", "angle", "scale", "unit_vector", "weight")
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    UNIT_VECTOR_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    length: int
    angle: int
    scale: int
    unit_vector: int
    weight: int
    def __init__(self, length: _Optional[int] = ..., angle: _Optional[int] = ..., scale: _Optional[int] = ..., unit_vector: _Optional[int] = ..., weight: _Optional[int] = ...) -> None: ...

class SetDecimalDigitsForDisplayResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFolderNotesRequest(_message.Message):
    __slots__ = ("folder_path", "notes", "append_false_overwrite")
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    APPEND_FALSE_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    notes: _containers.RepeatedScalarFieldContainer[str]
    append_false_overwrite: bool
    def __init__(self, folder_path: _Optional[str] = ..., notes: _Optional[_Iterable[str]] = ..., append_false_overwrite: bool = ...) -> None: ...

class SetFolderNotesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInteractionModeRequest(_message.Message):
    __slots__ = ("sa_interaction_mode", "measurement_plan_interaction_mode", "measurement_plan_dialog_interaction_mode")
    SA_INTERACTION_MODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_PLAN_INTERACTION_MODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_PLAN_DIALOG_INTERACTION_MODE_FIELD_NUMBER: _ClassVar[int]
    sa_interaction_mode: _spatial_analyzer_values_pb2.SaInteractionMode
    measurement_plan_interaction_mode: _spatial_analyzer_values_pb2.MpInteractionMode
    measurement_plan_dialog_interaction_mode: _spatial_analyzer_values_pb2.MpDialogInteractionMode
    def __init__(self, sa_interaction_mode: _Optional[_Union[_spatial_analyzer_values_pb2.SaInteractionMode, str]] = ..., measurement_plan_interaction_mode: _Optional[_Union[_spatial_analyzer_values_pb2.MpInteractionMode, str]] = ..., measurement_plan_dialog_interaction_mode: _Optional[_Union[_spatial_analyzer_values_pb2.MpDialogInteractionMode, str]] = ...) -> None: ...

class SetInteractionModeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetLoggingStateRequest(_message.Message):
    __slots__ = ("active",)
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    active: bool
    def __init__(self, active: bool = ...) -> None: ...

class SetLoggingStateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetNotificationCancelOverrideRequest(_message.Message):
    __slots__ = ("prohibit_cancel",)
    PROHIBIT_CANCEL_FIELD_NUMBER: _ClassVar[int]
    prohibit_cancel: bool
    def __init__(self, prohibit_cancel: bool = ...) -> None: ...

class SetNotificationCancelOverrideResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectNotesRequest(_message.Message):
    __slots__ = ("object", "notes", "append_false_overwrite")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    APPEND_FALSE_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    object: _spatial_analyzer_values_pb2.CollectionObjectName
    notes: _containers.RepeatedScalarFieldContainer[str]
    append_false_overwrite: bool
    def __init__(self, object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., notes: _Optional[_Iterable[str]] = ..., append_false_overwrite: bool = ...) -> None: ...

class SetObjectNotesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOpcDaTagValueDoubleRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name", "value")
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    value: float
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class SetOpcDaTagValueDoubleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOpcDaTagValueIntegerRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name", "value")
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    value: int
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class SetOpcDaTagValueIntegerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOpcDaTagValueStringRequest(_message.Message):
    __slots__ = ("opc_server_da_tag_name", "value")
    OPC_SERVER_DA_TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    opc_server_da_tag_name: str
    value: str
    def __init__(self, opc_server_da_tag_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetOpcDaTagValueStringResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointNotesRequest(_message.Message):
    __slots__ = ("point", "notes", "append_false_overwrite")
    POINT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    APPEND_FALSE_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    point: _spatial_analyzer_values_pb2.PointName
    notes: _containers.RepeatedScalarFieldContainer[str]
    append_false_overwrite: bool
    def __init__(self, point: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., notes: _Optional[_Iterable[str]] = ..., append_false_overwrite: bool = ...) -> None: ...

class SetPointNotesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetUserInterfaceProfileRequest(_message.Message):
    __slots__ = ("profile_name", "profile_file_name_optional")
    PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FILE_NAME_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    profile_name: str
    profile_file_name_optional: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, profile_name: _Optional[str] = ..., profile_file_name_optional: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SetUserInterfaceProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetViewIdleUpdateFrequencyRequest(_message.Message):
    __slots__ = ("idle_count",)
    IDLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    idle_count: int
    def __init__(self, idle_count: _Optional[int] = ...) -> None: ...

class SetViewIdleUpdateFrequencyResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetWildCardAsteriskModeRequest(_message.Message):
    __slots__ = ("auto_wrap_search_string",)
    AUTO_WRAP_SEARCH_STRING_FIELD_NUMBER: _ClassVar[int]
    auto_wrap_search_string: bool
    def __init__(self, auto_wrap_search_string: bool = ...) -> None: ...

class SetWildCardAsteriskModeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetWorkingFrameRequest(_message.Message):
    __slots__ = ("new_working_frame_name",)
    NEW_WORKING_FRAME_NAME_FIELD_NUMBER: _ClassVar[int]
    new_working_frame_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, new_working_frame_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetWorkingFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StatusDialogRequest(_message.Message):
    __slots__ = ("dialog_title", "text_message", "current_position", "upper_limit", "suppress_time_remaining", "close_dialog")
    DIALOG_TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    UPPER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
    CLOSE_DIALOG_FIELD_NUMBER: _ClassVar[int]
    dialog_title: str
    text_message: str
    current_position: int
    upper_limit: int
    suppress_time_remaining: bool
    close_dialog: bool
    def __init__(self, dialog_title: _Optional[str] = ..., text_message: _Optional[str] = ..., current_position: _Optional[int] = ..., upper_limit: _Optional[int] = ..., suppress_time_remaining: bool = ..., close_dialog: bool = ...) -> None: ...

class StatusDialogResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class TrimLogFileRequest(_message.Message):
    __slots__ = ("number_of_entries_to_keep",)
    NUMBER_OF_ENTRIES_TO_KEEP_FIELD_NUMBER: _ClassVar[int]
    number_of_entries_to_keep: int
    def __init__(self, number_of_entries_to_keep: _Optional[int] = ...) -> None: ...

class TrimLogFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class WriteToLogRequest(_message.Message):
    __slots__ = ("log_entry",)
    LOG_ENTRY_FIELD_NUMBER: _ClassVar[int]
    log_entry: str
    def __init__(self, log_entry: _Optional[str] = ...) -> None: ...

class WriteToLogResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
