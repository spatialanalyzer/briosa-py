from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetIThCollectionNameRequest(_message.Message):
    __slots__ = ("collection_index",)
    COLLECTION_INDEX_FIELD_NUMBER: _ClassVar[int]
    collection_index: int
    def __init__(self, collection_index: _Optional[int] = ...) -> None: ...

class GetIThCollectionNameResult(_message.Message):
    __slots__ = ("resultant_name", "execution")
    RESULTANT_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    resultant_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, resultant_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfCollectionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetNumberOfCollectionsResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
