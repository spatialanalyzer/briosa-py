from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteDimensionRequest(_message.Message):
    __slots__ = ("dimension_name",)
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    dimension_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, dimension_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteDimensionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetDimensionValueRequest(_message.Message):
    __slots__ = ("dimension_name",)
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    dimension_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, dimension_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetDimensionValueResult(_message.Message):
    __slots__ = ("dimensions_value", "nominal_value_enabled", "high_tolerance_enabled", "low_tolerance_enabled", "nominal_value", "high_tolerance", "low_tolerance", "execution")
    DIMENSIONS_VALUE_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_VALUE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    dimensions_value: float
    nominal_value_enabled: bool
    high_tolerance_enabled: bool
    low_tolerance_enabled: bool
    nominal_value: float
    high_tolerance: float
    low_tolerance: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, dimensions_value: _Optional[float] = ..., nominal_value_enabled: bool = ..., high_tolerance_enabled: bool = ..., low_tolerance_enabled: bool = ..., nominal_value: _Optional[float] = ..., high_tolerance: _Optional[float] = ..., low_tolerance: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDimensionToleranceRequest(_message.Message):
    __slots__ = ("dimension_name", "enable_nominal", "enable_high", "enable_low", "nominal", "high_tolerance", "low_tolerance")
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLE_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_HIGH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_LOW_FIELD_NUMBER: _ClassVar[int]
    NOMINAL_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    dimension_name: _spatial_analyzer_values_pb2.CollectionItemName
    enable_nominal: bool
    enable_high: bool
    enable_low: bool
    nominal: float
    high_tolerance: float
    low_tolerance: float
    def __init__(self, dimension_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., enable_nominal: bool = ..., enable_high: bool = ..., enable_low: bool = ..., nominal: _Optional[float] = ..., high_tolerance: _Optional[float] = ..., low_tolerance: _Optional[float] = ...) -> None: ...

class SetDimensionToleranceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
