from briosa.sa.v2026_1_0529_7.v1alpha1 import specialized_values_pb2 as _specialized_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AngularUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ANGULAR_UNIT_UNSPECIFIED: _ClassVar[AngularUnit]
    ANGULAR_UNIT_DEGREES: _ClassVar[AngularUnit]
    ANGULAR_UNIT_DEGREES_MINUTES_SECONDS: _ClassVar[AngularUnit]
    ANGULAR_UNIT_RADIANS: _ClassVar[AngularUnit]
    ANGULAR_UNIT_MILLIRADIANS: _ClassVar[AngularUnit]
    ANGULAR_UNIT_GONS_GRAD: _ClassVar[AngularUnit]
    ANGULAR_UNIT_MILS: _ClassVar[AngularUnit]
    ANGULAR_UNIT_ARCSECONDS: _ClassVar[AngularUnit]
    ANGULAR_UNIT_DEGREES_MINUTES: _ClassVar[AngularUnit]

class DistanceUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DISTANCE_UNIT_UNSPECIFIED: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_METERS: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_CENTIMETERS: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_MILLIMETERS: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_FEET: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_INCHES: _ClassVar[DistanceUnit]
    DISTANCE_UNIT_US_SURVEY_FEET: _ClassVar[DistanceUnit]

class TemperatureUnit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEMPERATURE_UNIT_UNSPECIFIED: _ClassVar[TemperatureUnit]
    TEMPERATURE_UNIT_FAHRENHEIT: _ClassVar[TemperatureUnit]
    TEMPERATURE_UNIT_CELSIUS: _ClassVar[TemperatureUnit]
ANGULAR_UNIT_UNSPECIFIED: AngularUnit
ANGULAR_UNIT_DEGREES: AngularUnit
ANGULAR_UNIT_DEGREES_MINUTES_SECONDS: AngularUnit
ANGULAR_UNIT_RADIANS: AngularUnit
ANGULAR_UNIT_MILLIRADIANS: AngularUnit
ANGULAR_UNIT_GONS_GRAD: AngularUnit
ANGULAR_UNIT_MILS: AngularUnit
ANGULAR_UNIT_ARCSECONDS: AngularUnit
ANGULAR_UNIT_DEGREES_MINUTES: AngularUnit
DISTANCE_UNIT_UNSPECIFIED: DistanceUnit
DISTANCE_UNIT_METERS: DistanceUnit
DISTANCE_UNIT_CENTIMETERS: DistanceUnit
DISTANCE_UNIT_MILLIMETERS: DistanceUnit
DISTANCE_UNIT_FEET: DistanceUnit
DISTANCE_UNIT_INCHES: DistanceUnit
DISTANCE_UNIT_US_SURVEY_FEET: DistanceUnit
TEMPERATURE_UNIT_UNSPECIFIED: TemperatureUnit
TEMPERATURE_UNIT_FAHRENHEIT: TemperatureUnit
TEMPERATURE_UNIT_CELSIUS: TemperatureUnit

class PointName(_message.Message):
    __slots__ = ("collection_name", "group_name", "target_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    target_name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ..., target_name: _Optional[str] = ...) -> None: ...

class CollectionInstrumentId(_message.Message):
    __slots__ = ("collection_name", "instrument_id")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    instrument_id: int
    def __init__(self, collection_name: _Optional[str] = ..., instrument_id: _Optional[int] = ...) -> None: ...

class CollectionMachineId(_message.Message):
    __slots__ = ("collection_name", "machine_id")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    machine_id: int
    def __init__(self, collection_name: _Optional[str] = ..., machine_id: _Optional[int] = ...) -> None: ...

class CollectionObjectName(_message.Message):
    __slots__ = ("collection_name", "object_name", "object_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    object_name: str
    object_type: _specialized_values_pb2.ObjectType
    def __init__(self, collection_name: _Optional[str] = ..., object_name: _Optional[str] = ..., object_type: _Optional[_Union[_specialized_values_pb2.ObjectType, str]] = ...) -> None: ...

class CollectionItemName(_message.Message):
    __slots__ = ("collection_name", "item_name", "item_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    item_name: str
    item_type: _specialized_values_pb2.ItemType
    def __init__(self, collection_name: _Optional[str] = ..., item_name: _Optional[str] = ..., item_type: _Optional[_Union[_specialized_values_pb2.ItemType, str]] = ...) -> None: ...

class CollectionGroupName(_message.Message):
    __slots__ = ("collection_name", "group_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ...) -> None: ...

class CollectionVectorGroupName(_message.Message):
    __slots__ = ("collection_name", "vector_group_name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    vector_group_name: str
    def __init__(self, collection_name: _Optional[str] = ..., vector_group_name: _Optional[str] = ...) -> None: ...

class VectorName(_message.Message):
    __slots__ = ("collection_name", "group_name", "name")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    group_name: str
    name: str
    def __init__(self, collection_name: _Optional[str] = ..., group_name: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CollectionInstrumentIdList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CollectionInstrumentId]
    def __init__(self, values: _Optional[_Iterable[_Union[CollectionInstrumentId, _Mapping]]] = ...) -> None: ...

class CollectionGroupNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CollectionGroupName]
    def __init__(self, values: _Optional[_Iterable[_Union[CollectionGroupName, _Mapping]]] = ...) -> None: ...

class CollectionObjectNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CollectionObjectName]
    def __init__(self, values: _Optional[_Iterable[_Union[CollectionObjectName, _Mapping]]] = ...) -> None: ...

class CollectionItemNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CollectionItemName]
    def __init__(self, values: _Optional[_Iterable[_Union[CollectionItemName, _Mapping]]] = ...) -> None: ...

class CollectionVectorGroupNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[CollectionVectorGroupName]
    def __init__(self, values: _Optional[_Iterable[_Union[CollectionVectorGroupName, _Mapping]]] = ...) -> None: ...

class PointNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[PointName]
    def __init__(self, values: _Optional[_Iterable[_Union[PointName, _Mapping]]] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class DoubleArray(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class Transform(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, values: _Optional[_Iterable[float]] = ...) -> None: ...

class WorldTransform(_message.Message):
    __slots__ = ("transform", "scale_factor")
    TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    transform: Transform
    scale_factor: float
    def __init__(self, transform: _Optional[_Union[Transform, _Mapping]] = ..., scale_factor: _Optional[float] = ...) -> None: ...

class RgbColor(_message.Message):
    __slots__ = ("red", "green", "blue")
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class FileReference(_message.Message):
    __slots__ = ("path", "embedded_file")
    PATH_FIELD_NUMBER: _ClassVar[int]
    EMBEDDED_FILE_FIELD_NUMBER: _ClassVar[int]
    path: str
    embedded_file: bool
    def __init__(self, path: _Optional[str] = ..., embedded_file: bool = ...) -> None: ...

class Font(_message.Message):
    __slots__ = ("font_name", "size", "color")
    FONT_NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    font_name: str
    size: int
    color: RgbColor
    def __init__(self, font_name: _Optional[str] = ..., size: _Optional[int] = ..., color: _Optional[_Union[RgbColor, _Mapping]] = ...) -> None: ...

class VectorNameList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[VectorName]
    def __init__(self, values: _Optional[_Iterable[_Union[VectorName, _Mapping]]] = ...) -> None: ...

class Vector3(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class ToleranceLimit(_message.Message):
    __slots__ = ("enabled", "value")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    value: float
    def __init__(self, enabled: bool = ..., value: _Optional[float] = ...) -> None: ...

class ToleranceVectorOptions(_message.Message):
    __slots__ = ("high_x", "high_y", "high_z", "high_magnitude", "low_x", "low_y", "low_z", "low_magnitude")
    HIGH_X_FIELD_NUMBER: _ClassVar[int]
    HIGH_Y_FIELD_NUMBER: _ClassVar[int]
    HIGH_Z_FIELD_NUMBER: _ClassVar[int]
    HIGH_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    LOW_X_FIELD_NUMBER: _ClassVar[int]
    LOW_Y_FIELD_NUMBER: _ClassVar[int]
    LOW_Z_FIELD_NUMBER: _ClassVar[int]
    LOW_MAGNITUDE_FIELD_NUMBER: _ClassVar[int]
    high_x: ToleranceLimit
    high_y: ToleranceLimit
    high_z: ToleranceLimit
    high_magnitude: ToleranceLimit
    low_x: ToleranceLimit
    low_y: ToleranceLimit
    low_z: ToleranceLimit
    low_magnitude: ToleranceLimit
    def __init__(self, high_x: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_y: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_z: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., high_magnitude: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_x: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_y: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_z: _Optional[_Union[ToleranceLimit, _Mapping]] = ..., low_magnitude: _Optional[_Union[ToleranceLimit, _Mapping]] = ...) -> None: ...
