from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AskForDoubleRequest(_message.Message):
    __slots__ = ("question_to_ask", "initial_value", "enforce_min_max_values", "min_value", "max_value", "font")
    QUESTION_TO_ASK_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MIN_MAX_VALUES_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    question_to_ask: str
    initial_value: float
    enforce_min_max_values: bool
    min_value: float
    max_value: float
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, question_to_ask: _Optional[str] = ..., initial_value: _Optional[float] = ..., enforce_min_max_values: bool = ..., min_value: _Optional[float] = ..., max_value: _Optional[float] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class AskForDoubleResult(_message.Message):
    __slots__ = ("answer", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForIntegerRequest(_message.Message):
    __slots__ = ("question_to_ask", "initial_value", "enforce_min_max_values", "min_value", "max_value", "font")
    QUESTION_TO_ASK_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENFORCE_MIN_MAX_VALUES_FIELD_NUMBER: _ClassVar[int]
    MIN_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    question_to_ask: str
    initial_value: int
    enforce_min_max_values: bool
    min_value: int
    max_value: int
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, question_to_ask: _Optional[str] = ..., initial_value: _Optional[int] = ..., enforce_min_max_values: bool = ..., min_value: _Optional[int] = ..., max_value: _Optional[int] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class AskForIntegerResult(_message.Message):
    __slots__ = ("answer", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForPointNameRequest(_message.Message):
    __slots__ = ("question_to_ask", "initial_value", "font")
    QUESTION_TO_ASK_FIELD_NUMBER: _ClassVar[int]
    INITIAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    question_to_ask: str
    initial_value: _spatial_analyzer_values_pb2.PointName
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, question_to_ask: _Optional[str] = ..., initial_value: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class AskForPointNameResult(_message.Message):
    __slots__ = ("answer", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForStringRequest(_message.Message):
    __slots__ = ("question_to_ask", "password_entry", "initial_answer", "font")
    QUESTION_TO_ASK_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_ENTRY_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ANSWER_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    question_to_ask: str
    password_entry: bool
    initial_answer: str
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, question_to_ask: _Optional[str] = ..., password_entry: bool = ..., initial_answer: _Optional[str] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class AskForStringResult(_message.Message):
    __slots__ = ("answer", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForStringPullDownVersionRequest(_message.Message):
    __slots__ = ("question_or_statement", "possible_answers", "font")
    QUESTION_OR_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    POSSIBLE_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    question_or_statement: _containers.RepeatedScalarFieldContainer[str]
    possible_answers: _containers.RepeatedScalarFieldContainer[str]
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, question_or_statement: _Optional[_Iterable[str]] = ..., possible_answers: _Optional[_Iterable[str]] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class AskForStringPullDownVersionResult(_message.Message):
    __slots__ = ("answer", "answer_index", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_INDEX_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: str
    answer_index: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[str] = ..., answer_index: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForUserDecisionFromImageRequest(_message.Message):
    __slots__ = ("image_file", "image_map_xml_file", "window_caption", "window_width_0_default", "window_height_0_default")
    IMAGE_FILE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_MAP_XML_FILE_FIELD_NUMBER: _ClassVar[int]
    WINDOW_CAPTION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_0_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_0_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    image_file: _spatial_analyzer_values_pb2.FileReference
    image_map_xml_file: _spatial_analyzer_values_pb2.FileReference
    window_caption: str
    window_width_0_default: int
    window_height_0_default: int
    def __init__(self, image_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., image_map_xml_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., window_caption: _Optional[str] = ..., window_width_0_default: _Optional[int] = ..., window_height_0_default: _Optional[int] = ...) -> None: ...

class AskForUserDecisionFromImageResult(_message.Message):
    __slots__ = ("user_choice", "execution")
    USER_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    user_choice: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, user_choice: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AskForUserDecisionFromStringsRequest(_message.Message):
    __slots__ = ("question_or_statement", "font", "button1_text_empty_to_hide_button", "button2_text_empty_to_hide_button", "button3_text_empty_to_hide_button")
    QUESTION_OR_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    BUTTON1_TEXT_EMPTY_TO_HIDE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    BUTTON2_TEXT_EMPTY_TO_HIDE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    BUTTON3_TEXT_EMPTY_TO_HIDE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    question_or_statement: _containers.RepeatedScalarFieldContainer[str]
    font: _spatial_analyzer_values_pb2.Font
    button1_text_empty_to_hide_button: str
    button2_text_empty_to_hide_button: str
    button3_text_empty_to_hide_button: str
    def __init__(self, question_or_statement: _Optional[_Iterable[str]] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., button1_text_empty_to_hide_button: _Optional[str] = ..., button2_text_empty_to_hide_button: _Optional[str] = ..., button3_text_empty_to_hide_button: _Optional[str] = ...) -> None: ...

class AskForUserDecisionFromStringsResult(_message.Message):
    __slots__ = ("answer", "execution")
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    answer: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, answer: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ObjectExistenceTestCheckOnlyRequest(_message.Message):
    __slots__ = ("object_name",)
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ObjectExistenceTestCheckOnlyResult(_message.Message):
    __slots__ = ("exists", "execution")
    EXISTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    exists: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, exists: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
