from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteEventRequest(_message.Message):
    __slots__ = ("event_name",)
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    event_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, event_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteEventResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ExportEventRefListRequest(_message.Message):
    __slots__ = ("event_list", "file_path", "decimal_precision", "overwrite_existing_file")
    EVENT_LIST_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FILE_FIELD_NUMBER: _ClassVar[int]
    event_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    file_path: _spatial_analyzer_values_pb2.FileReference
    decimal_precision: int
    overwrite_existing_file: bool
    def __init__(self, event_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., decimal_precision: _Optional[int] = ..., overwrite_existing_file: bool = ...) -> None: ...

class ExportEventRefListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthEventFromEventRefListRequest(_message.Message):
    __slots__ = ("event_list", "event_index")
    EVENT_LIST_FIELD_NUMBER: _ClassVar[int]
    EVENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    event_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    event_index: int
    def __init__(self, event_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., event_index: _Optional[int] = ...) -> None: ...

class GetIthEventFromEventRefListResult(_message.Message):
    __slots__ = ("resultant_item", "execution")
    RESULTANT_ITEM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_item: _spatial_analyzer_values_pb2.CollectionItemName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_item: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfEventsInEventRefListRequest(_message.Message):
    __slots__ = ("event_list",)
    EVENT_LIST_FIELD_NUMBER: _ClassVar[int]
    event_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, event_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class GetNumberOfEventsInEventRefListResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenameEventRequest(_message.Message):
    __slots__ = ("original_event_name", "new_event_name", "overwrite_if_exists")
    ORIGINAL_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_event_name: _spatial_analyzer_values_pb2.CollectionObjectName
    new_event_name: _spatial_analyzer_values_pb2.CollectionObjectName
    overwrite_if_exists: bool
    def __init__(self, original_event_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., new_event_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenameEventResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
