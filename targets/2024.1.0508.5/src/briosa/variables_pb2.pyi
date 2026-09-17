from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddDoubleToNamedDoubleListVariableRequest(_message.Message):
    __slots__ = ("name", "double_value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    double_value: float
    def __init__(self, name: _Optional[str] = ..., double_value: _Optional[float] = ...) -> None: ...

class AddDoubleToNamedDoubleListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearNamedDoubleListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ClearNamedDoubleListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class DeleteVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteVariablesWildcardMatchRequest(_message.Message):
    __slots__ = ("variable_wildcard_criteria",)
    VARIABLE_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    variable_wildcard_criteria: str
    def __init__(self, variable_wildcard_criteria: _Optional[str] = ...) -> None: ...

class DeleteVariablesWildcardMatchResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetBooleanVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetBooleanVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCollectionObjectNameVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCollectionObjectNameVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _spatial_analyzer_values_pb2.CollectionObjectName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCollectionObjectRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetCollectionObjectRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetDoubleVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetDoubleVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIntegerVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetIntegerVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNamedDoubleListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNamedDoubleListVariableResult(_message.Message):
    __slots__ = ("double_list_variable", "execution")
    DOUBLE_LIST_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    double_list_variable: _containers.RepeatedScalarFieldContainer[float]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, double_list_variable: _Optional[_Iterable[float]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNamedDoubleListVariableMinMaxRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetNamedDoubleListVariableMinMaxResult(_message.Message):
    __slots__ = ("minimum_value", "maximum_value", "execution")
    MINIMUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    minimum_value: float
    maximum_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, minimum_value: _Optional[float] = ..., maximum_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointNameRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPointNameRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointNameVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPointNameVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _spatial_analyzer_values_pb2.PointName
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRelationshipRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetRelationshipRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetReportItemsReferenceListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetReportItemsReferenceListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetStringRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetStringRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetStringVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetStringVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetTransformVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTransformVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetVectorNameRefListVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetVectorNameRefListVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetVectorVariableRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetVectorVariableResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetBooleanVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: bool
    def __init__(self, name: _Optional[str] = ..., value: bool = ...) -> None: ...

class SetBooleanVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCollectionObjectNameVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetCollectionObjectNameVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCollectionObjectRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class SetCollectionObjectRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetDoubleVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: float
    def __init__(self, name: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...

class SetDoubleVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetFontVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _spatial_analyzer_values_pb2.Font
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class SetFontVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetIntegerVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: int
    def __init__(self, name: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...

class SetIntegerVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetNamedDoubleListVariableRequest(_message.Message):
    __slots__ = ("name", "double_list_variable")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_LIST_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    name: str
    double_list_variable: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, name: _Optional[str] = ..., double_list_variable: _Optional[_Iterable[float]] = ...) -> None: ...

class SetNamedDoubleListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointNameRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ...) -> None: ...

class SetPointNameRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointNameVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _spatial_analyzer_values_pb2.PointName
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class SetPointNameVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class SetRelationshipRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportItemsReferenceListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ...) -> None: ...

class SetReportItemsReferenceListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetStringRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class SetStringRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetStringVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SetStringVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTransformVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _spatial_analyzer_values_pb2.Transform
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetTransformVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorNameRefListVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ...) -> None: ...

class SetVectorNameRefListVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorVariableRequest(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _spatial_analyzer_values_pb2.Vector
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class SetVectorVariableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
