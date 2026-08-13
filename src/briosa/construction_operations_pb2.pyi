from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetActiveCollectionNameRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActiveCollectionNameResult(_message.Message):
    __slots__ = ("currently_active_collection_name", "execution")
    CURRENTLY_ACTIVE_COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    currently_active_collection_name: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, currently_active_collection_name: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
