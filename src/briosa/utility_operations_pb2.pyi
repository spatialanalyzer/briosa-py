from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
