from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteScaleBarRequest(_message.Message):
    __slots__ = ("scale_bar_name",)
    SCALE_BAR_NAME_FIELD_NUMBER: _ClassVar[int]
    scale_bar_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, scale_bar_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteScaleBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetScaleBarStatsRequest(_message.Message):
    __slots__ = ("scale_bar_name",)
    SCALE_BAR_NAME_FIELD_NUMBER: _ClassVar[int]
    scale_bar_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, scale_bar_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetScaleBarStatsResult(_message.Message):
    __slots__ = ("nominal_length", "actual_length", "deviation", "execution")
    NOMINAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_LENGTH_FIELD_NUMBER: _ClassVar[int]
    DEVIATION_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    nominal_length: float
    actual_length: float
    deviation: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, nominal_length: _Optional[float] = ..., actual_length: _Optional[float] = ..., deviation: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ScaleBarCheckRequest(_message.Message):
    __slots__ = ("scale_bar_point_a", "scale_bar_point_b", "current_temperature_f", "length_of_bar_at_68f", "material_cte_ppm_f", "tolerance")
    SCALE_BAR_POINT_A_FIELD_NUMBER: _ClassVar[int]
    SCALE_BAR_POINT_B_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TEMPERATURE_F_FIELD_NUMBER: _ClassVar[int]
    LENGTH_OF_BAR_AT_68F_FIELD_NUMBER: _ClassVar[int]
    MATERIAL_CTE_PPM_F_FIELD_NUMBER: _ClassVar[int]
    TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    scale_bar_point_a: _spatial_analyzer_values_pb2.PointName
    scale_bar_point_b: _spatial_analyzer_values_pb2.PointName
    current_temperature_f: float
    length_of_bar_at_68f: float
    material_cte_ppm_f: float
    tolerance: float
    def __init__(self, scale_bar_point_a: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., scale_bar_point_b: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., current_temperature_f: _Optional[float] = ..., length_of_bar_at_68f: _Optional[float] = ..., material_cte_ppm_f: _Optional[float] = ..., tolerance: _Optional[float] = ...) -> None: ...

class ScaleBarCheckResult(_message.Message):
    __slots__ = ("deviation_at_68f", "execution")
    DEVIATION_AT_68F_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    deviation_at_68f: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, deviation_at_68f: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetInwardPositiveNormalRequest(_message.Message):
    __slots__ = ("object_name", "inward_positive")
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    INWARD_POSITIVE_FIELD_NUMBER: _ClassVar[int]
    object_name: _spatial_analyzer_values_pb2.CollectionObjectName
    inward_positive: bool
    def __init__(self, object_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., inward_positive: bool = ...) -> None: ...

class SetInwardPositiveNormalResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
