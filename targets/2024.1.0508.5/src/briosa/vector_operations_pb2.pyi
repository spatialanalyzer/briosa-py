from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddAVectorToVectorNameRefListRequest(_message.Message):
    __slots__ = ("vector_group_name", "vector_name", "vector_name_list")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_name: str
    vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_name: _Optional[str] = ..., vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ...) -> None: ...

class AddAVectorToVectorNameRefListResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoRangeAndSetVectorGroupColorizationAllRequest(_message.Message):
    __slots__ = ("treat_individually", "colorization_options_uses_mode_only")
    TREAT_INDIVIDUALLY_FIELD_NUMBER: _ClassVar[int]
    COLORIZATION_OPTIONS_USES_MODE_ONLY_FIELD_NUMBER: _ClassVar[int]
    treat_individually: bool
    colorization_options_uses_mode_only: _spatial_analyzer_values_pb2.ColorizationOptions
    def __init__(self, treat_individually: bool = ..., colorization_options_uses_mode_only: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ...) -> None: ...

class AutoRangeAndSetVectorGroupColorizationAllResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AutoRangeAndSetVectorGroupColorizationSelectedRequest(_message.Message):
    __slots__ = ("vector_groups_to_be_set", "treat_individually", "colorization_options_uses_mode_only")
    VECTOR_GROUPS_TO_BE_SET_FIELD_NUMBER: _ClassVar[int]
    TREAT_INDIVIDUALLY_FIELD_NUMBER: _ClassVar[int]
    COLORIZATION_OPTIONS_USES_MODE_ONLY_FIELD_NUMBER: _ClassVar[int]
    vector_groups_to_be_set: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionVectorGroupName]
    treat_individually: bool
    colorization_options_uses_mode_only: _spatial_analyzer_values_pb2.ColorizationOptions
    def __init__(self, vector_groups_to_be_set: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]]] = ..., treat_individually: bool = ..., colorization_options_uses_mode_only: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ...) -> None: ...

class AutoRangeAndSetVectorGroupColorizationSelectedResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteIthVectorFromVectorGroupRequest(_message.Message):
    __slots__ = ("vector_group_name", "vector_index")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_index: int
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_index: _Optional[int] = ...) -> None: ...

class DeleteIthVectorFromVectorGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteVectorByNameRequest(_message.Message):
    __slots__ = ("vector_group_name", "vector_name")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_name: str
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_name: _Optional[str] = ...) -> None: ...

class DeleteVectorByNameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteVectorsRequest(_message.Message):
    __slots__ = ("vector_name_list",)
    VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    def __init__(self, vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ...) -> None: ...

class DeleteVectorsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthVectorFromVectorGroupRequest(_message.Message):
    __slots__ = ("vector_group_name", "vector_index")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_index: int
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_index: _Optional[int] = ...) -> None: ...

class GetIthVectorFromVectorGroupResult(_message.Message):
    __slots__ = ("vector_name", "begin_in_working", "end_in_working", "total_delta_in_working", "ijk_unit_vector_in_working", "magnitude", "execution")
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    END_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELTA_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    IJK_UNIT_VECTOR_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_name: str
    begin_in_working: _spatial_analyzer_values_pb2.Vector
    end_in_working: _spatial_analyzer_values_pb2.Vector
    total_delta_in_working: _spatial_analyzer_values_pb2.Vector
    ijk_unit_vector_in_working: _spatial_analyzer_values_pb2.Vector
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_name: _Optional[str] = ..., begin_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., total_delta_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., ijk_unit_vector_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetIthVectorFromVectorNameRefListRequest(_message.Message):
    __slots__ = ("vector_name_list", "vector_index")
    VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    VECTOR_INDEX_FIELD_NUMBER: _ClassVar[int]
    vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    vector_index: int
    def __init__(self, vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., vector_index: _Optional[int] = ...) -> None: ...

class GetIthVectorFromVectorNameRefListResult(_message.Message):
    __slots__ = ("vector_group_name", "vector_name", "begin_in_working", "end_in_working", "total_delta_in_working", "ijk_unit_vector_in_working", "magnitude", "execution")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    BEGIN_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    END_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELTA_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    IJK_UNIT_VECTOR_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_name: str
    begin_in_working: _spatial_analyzer_values_pb2.Vector
    end_in_working: _spatial_analyzer_values_pb2.Vector
    total_delta_in_working: _spatial_analyzer_values_pb2.Vector
    ijk_unit_vector_in_working: _spatial_analyzer_values_pb2.Vector
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_name: _Optional[str] = ..., begin_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., total_delta_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., ijk_unit_vector_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfVectorsInVectorGroupRequest(_message.Message):
    __slots__ = ("vector_group_name",)
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetNumberOfVectorsInVectorGroupResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetNumberOfVectorsInVectorNameRefListRequest(_message.Message):
    __slots__ = ("vector_name_list",)
    VECTOR_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    vector_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    def __init__(self, vector_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ...) -> None: ...

class GetNumberOfVectorsInVectorNameRefListResult(_message.Message):
    __slots__ = ("total_count", "execution")
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_count: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_count: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetVectorFromVectorGroupByNameRequest(_message.Message):
    __slots__ = ("vector_group_name", "vector_name")
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    vector_name: str
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., vector_name: _Optional[str] = ...) -> None: ...

class GetVectorFromVectorGroupByNameResult(_message.Message):
    __slots__ = ("begin_in_working", "end_in_working", "total_delta_in_working", "ijk_unit_vector_in_working", "magnitude", "execution")
    BEGIN_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    END_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DELTA_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    IJK_UNIT_VECTOR_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    begin_in_working: _spatial_analyzer_values_pb2.Vector
    end_in_working: _spatial_analyzer_values_pb2.Vector
    total_delta_in_working: _spatial_analyzer_values_pb2.Vector
    ijk_unit_vector_in_working: _spatial_analyzer_values_pb2.Vector
    magnitude: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, begin_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., end_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., total_delta_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., ijk_unit_vector_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., magnitude: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetVectorGroupPropertiesRequest(_message.Message):
    __slots__ = ("vector_group_name",)
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetVectorGroupPropertiesResult(_message.Message):
    __slots__ = ("total_vectors", "vectors_in_tolerance", "vectors_out_of_tolerance", "invalid_vectors", "vectors_in_tolerance_2", "vectors_out_of_tolerance_2", "absolute_max_magnitude", "absolute_min_magnitude", "max_magnitude", "min_magnitude", "standard_deviation_from_zero", "standard_deviation_from_mean", "avg_magnitude", "avg_of_abs_magnitude", "high_tolerance_value", "low_tolerance_value", "rms_value", "execution")
    TOTAL_VECTORS_FIELD_NUMBER: _ClassVar[int]
    VECTORS_IN_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    VECTORS_OUT_OF_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    INVALID_VECTORS_FIELD_NUMBER: _ClassVar[int]
    VECTORS_IN_TOLERANCE_2_FIELD_NUMBER: _ClassVar[int]
    VECTORS_OUT_OF_TOLERANCE_2_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_MAX_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_MIN_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    MAX_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    MIN_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FROM_ZERO_FIELD_NUMBER: _ClassVar[int]
    STANDARD_DEVIATION_FROM_MEAN_FIELD_NUMBER: _ClassVar[int]
    AVG_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    AVG_OF_ABS_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    HIGH_TOLERANCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    LOW_TOLERANCE_VALUE_FIELD_NUMBER: _ClassVar[int]
    RMS_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    total_vectors: int
    vectors_in_tolerance: int
    vectors_out_of_tolerance: int
    invalid_vectors: int
    vectors_in_tolerance_2: float
    vectors_out_of_tolerance_2: float
    absolute_max_magnitude: float
    absolute_min_magnitude: float
    max_magnitude: float
    min_magnitude: float
    standard_deviation_from_zero: float
    standard_deviation_from_mean: float
    avg_magnitude: float
    avg_of_abs_magnitude: float
    high_tolerance_value: float
    low_tolerance_value: float
    rms_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, total_vectors: _Optional[int] = ..., vectors_in_tolerance: _Optional[int] = ..., vectors_out_of_tolerance: _Optional[int] = ..., invalid_vectors: _Optional[int] = ..., vectors_in_tolerance_2: _Optional[float] = ..., vectors_out_of_tolerance_2: _Optional[float] = ..., absolute_max_magnitude: _Optional[float] = ..., absolute_min_magnitude: _Optional[float] = ..., max_magnitude: _Optional[float] = ..., min_magnitude: _Optional[float] = ..., standard_deviation_from_zero: _Optional[float] = ..., standard_deviation_from_mean: _Optional[float] = ..., avg_magnitude: _Optional[float] = ..., avg_of_abs_magnitude: _Optional[float] = ..., high_tolerance_value: _Optional[float] = ..., low_tolerance_value: _Optional[float] = ..., rms_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupColorizationOptionsAllRequest(_message.Message):
    __slots__ = ("colorization_options",)
    COLORIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    colorization_options: _spatial_analyzer_values_pb2.ColorizationOptions
    def __init__(self, colorization_options: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ...) -> None: ...

class SetVectorGroupColorizationOptionsAllResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupColorizationOptionsSelectedRequest(_message.Message):
    __slots__ = ("vector_groups_to_be_set", "colorization_options")
    VECTOR_GROUPS_TO_BE_SET_FIELD_NUMBER: _ClassVar[int]
    COLORIZATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    vector_groups_to_be_set: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionVectorGroupName]
    colorization_options: _spatial_analyzer_values_pb2.ColorizationOptions
    def __init__(self, vector_groups_to_be_set: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionVectorGroupName, _Mapping]]] = ..., colorization_options: _Optional[_Union[_spatial_analyzer_values_pb2.ColorizationOptions, _Mapping]] = ...) -> None: ...

class SetVectorGroupColorizationOptionsSelectedResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SortVectorsRequest(_message.Message):
    __slots__ = ("source_vectors", "sort_method", "coordinate_system", "primary_sort_coordinate", "secondary_sort_coordinate", "tertiary_sort_coordinate", "primary_coordinate_granularity", "secondary_coordinate_granularity", "tertiary_coordinate_granularity", "ascending")
    SOURCE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    SORT_METHOD_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_SORT_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_SORT_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    TERTIARY_SORT_COORDINATE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_COORDINATE_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_COORDINATE_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    TERTIARY_COORDINATE_GRANULARITY_FIELD_NUMBER: _ClassVar[int]
    ASCENDING_FIELD_NUMBER: _ClassVar[int]
    source_vectors: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    sort_method: str
    coordinate_system: _spatial_analyzer_values_pb2.CoordinateSystemType
    primary_sort_coordinate: str
    secondary_sort_coordinate: str
    tertiary_sort_coordinate: str
    primary_coordinate_granularity: float
    secondary_coordinate_granularity: float
    tertiary_coordinate_granularity: float
    ascending: bool
    def __init__(self, source_vectors: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., sort_method: _Optional[str] = ..., coordinate_system: _Optional[_Union[_spatial_analyzer_values_pb2.CoordinateSystemType, str]] = ..., primary_sort_coordinate: _Optional[str] = ..., secondary_sort_coordinate: _Optional[str] = ..., tertiary_sort_coordinate: _Optional[str] = ..., primary_coordinate_granularity: _Optional[float] = ..., secondary_coordinate_granularity: _Optional[float] = ..., tertiary_coordinate_granularity: _Optional[float] = ..., ascending: bool = ...) -> None: ...

class SortVectorsResult(_message.Message):
    __slots__ = ("sorted_vectors", "execution")
    SORTED_VECTORS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    sorted_vectors: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.VectorName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, sorted_vectors: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.VectorName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
