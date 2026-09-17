from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RunSubroutineRequest(_message.Message):
    __slots__ = ("mp_subroutine_file_path", "share_parent_variables")
    MP_SUBROUTINE_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    SHARE_PARENT_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    mp_subroutine_file_path: _spatial_analyzer_values_pb2.FileReference
    share_parent_variables: bool
    def __init__(self, mp_subroutine_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., share_parent_variables: bool = ...) -> None: ...

class RunSubroutineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
