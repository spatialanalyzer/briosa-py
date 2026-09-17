from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddTaskOverviewItemRequest(_message.Message):
    __slots__ = ("task_name", "comment_text", "effort_index")
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    EFFORT_INDEX_FIELD_NUMBER: _ClassVar[int]
    task_name: str
    comment_text: str
    effort_index: float
    def __init__(self, task_name: _Optional[str] = ..., comment_text: _Optional[str] = ..., effort_index: _Optional[float] = ...) -> None: ...

class AddTaskOverviewItemResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateClearTaskOverviewListRequest(_message.Message):
    __slots__ = ("task_name_font", "task_comment_font")
    TASK_NAME_FONT_FIELD_NUMBER: _ClassVar[int]
    TASK_COMMENT_FONT_FIELD_NUMBER: _ClassVar[int]
    task_name_font: _spatial_analyzer_values_pb2.Font
    task_comment_font: _spatial_analyzer_values_pb2.Font
    def __init__(self, task_name_font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., task_comment_font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class CreateClearTaskOverviewListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCurrentTaskRequest(_message.Message):
    __slots__ = ("task_index",)
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    task_index: int
    def __init__(self, task_index: _Optional[int] = ...) -> None: ...

class SetCurrentTaskResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOverviewImageRequest(_message.Message):
    __slots__ = ("image_path",)
    IMAGE_PATH_FIELD_NUMBER: _ClassVar[int]
    image_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, image_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SetOverviewImageResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetOverviewTitleRequest(_message.Message):
    __slots__ = ("overview_title",)
    OVERVIEW_TITLE_FIELD_NUMBER: _ClassVar[int]
    overview_title: str
    def __init__(self, overview_title: _Optional[str] = ...) -> None: ...

class SetOverviewTitleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTaskItemCommentRequest(_message.Message):
    __slots__ = ("task_index", "task_comment")
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    TASK_COMMENT_FIELD_NUMBER: _ClassVar[int]
    task_index: int
    task_comment: str
    def __init__(self, task_index: _Optional[int] = ..., task_comment: _Optional[str] = ...) -> None: ...

class SetTaskItemCommentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTaskItemCompletionValuesRequest(_message.Message):
    __slots__ = ("task_index", "increments_completed", "total_increments")
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    INCREMENTS_COMPLETED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_INCREMENTS_FIELD_NUMBER: _ClassVar[int]
    task_index: int
    increments_completed: int
    total_increments: int
    def __init__(self, task_index: _Optional[int] = ..., increments_completed: _Optional[int] = ..., total_increments: _Optional[int] = ...) -> None: ...

class SetTaskItemCompletionValuesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTaskItemNameRequest(_message.Message):
    __slots__ = ("task_item_index", "task_name")
    TASK_ITEM_INDEX_FIELD_NUMBER: _ClassVar[int]
    TASK_NAME_FIELD_NUMBER: _ClassVar[int]
    task_item_index: int
    task_name: str
    def __init__(self, task_item_index: _Optional[int] = ..., task_name: _Optional[str] = ...) -> None: ...

class SetTaskItemNameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowProgressForTaskItemRequest(_message.Message):
    __slots__ = ("task_index", "show_progress")
    TASK_INDEX_FIELD_NUMBER: _ClassVar[int]
    SHOW_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    task_index: int
    show_progress: bool
    def __init__(self, task_index: _Optional[int] = ..., show_progress: bool = ...) -> None: ...

class ShowProgressForTaskItemResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowTaskOverviewListRequest(_message.Message):
    __slots__ = ("show",)
    SHOW_FIELD_NUMBER: _ClassVar[int]
    show: bool
    def __init__(self, show: bool = ...) -> None: ...

class ShowTaskOverviewListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
