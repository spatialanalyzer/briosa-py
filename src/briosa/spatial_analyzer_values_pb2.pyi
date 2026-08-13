from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OBJECT_TYPE_UNSPECIFIED: _ClassVar[ObjectType]
    OBJECT_TYPE_ANY: _ClassVar[ObjectType]
    OBJECT_TYPE_B_SPLINE: _ClassVar[ObjectType]
    OBJECT_TYPE_CIRCLE: _ClassVar[ObjectType]
    OBJECT_TYPE_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_ENHANCED_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_SCAN_STRIPE_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_CROSS_SECTION_CLOUD: _ClassVar[ObjectType]
    OBJECT_TYPE_CONE: _ClassVar[ObjectType]
    OBJECT_TYPE_CYLINDER: _ClassVar[ObjectType]
    OBJECT_TYPE_DATUM: _ClassVar[ObjectType]
    OBJECT_TYPE_ELLIPSE: _ClassVar[ObjectType]
    OBJECT_TYPE_FRAME: _ClassVar[ObjectType]
    OBJECT_TYPE_FRAME_SET: _ClassVar[ObjectType]
    OBJECT_TYPE_LINE: _ClassVar[ObjectType]
    OBJECT_TYPE_PARABOLOID: _ClassVar[ObjectType]
    OBJECT_TYPE_PERIMETER: _ClassVar[ObjectType]
    OBJECT_TYPE_PLANE: _ClassVar[ObjectType]
    OBJECT_TYPE_POINT_GROUP: _ClassVar[ObjectType]
    OBJECT_TYPE_POINT_SET: _ClassVar[ObjectType]
    OBJECT_TYPE_POLY_SURFACE: _ClassVar[ObjectType]
    OBJECT_TYPE_SCAN_STRIPE_MESH: _ClassVar[ObjectType]
    OBJECT_TYPE_SLOT: _ClassVar[ObjectType]
    OBJECT_TYPE_SPHERE: _ClassVar[ObjectType]
    OBJECT_TYPE_SURFACE: _ClassVar[ObjectType]
    OBJECT_TYPE_TORUS: _ClassVar[ObjectType]
    OBJECT_TYPE_VECTOR_GROUP: _ClassVar[ObjectType]
OBJECT_TYPE_UNSPECIFIED: ObjectType
OBJECT_TYPE_ANY: ObjectType
OBJECT_TYPE_B_SPLINE: ObjectType
OBJECT_TYPE_CIRCLE: ObjectType
OBJECT_TYPE_CLOUD: ObjectType
OBJECT_TYPE_ENHANCED_CLOUD: ObjectType
OBJECT_TYPE_SCAN_STRIPE_CLOUD: ObjectType
OBJECT_TYPE_CROSS_SECTION_CLOUD: ObjectType
OBJECT_TYPE_CONE: ObjectType
OBJECT_TYPE_CYLINDER: ObjectType
OBJECT_TYPE_DATUM: ObjectType
OBJECT_TYPE_ELLIPSE: ObjectType
OBJECT_TYPE_FRAME: ObjectType
OBJECT_TYPE_FRAME_SET: ObjectType
OBJECT_TYPE_LINE: ObjectType
OBJECT_TYPE_PARABOLOID: ObjectType
OBJECT_TYPE_PERIMETER: ObjectType
OBJECT_TYPE_PLANE: ObjectType
OBJECT_TYPE_POINT_GROUP: ObjectType
OBJECT_TYPE_POINT_SET: ObjectType
OBJECT_TYPE_POLY_SURFACE: ObjectType
OBJECT_TYPE_SCAN_STRIPE_MESH: ObjectType
OBJECT_TYPE_SLOT: ObjectType
OBJECT_TYPE_SPHERE: ObjectType
OBJECT_TYPE_SURFACE: ObjectType
OBJECT_TYPE_TORUS: ObjectType
OBJECT_TYPE_VECTOR_GROUP: ObjectType

class CollectionObjectName(_message.Message):
    __slots__ = ("collection_name", "object_name", "object_type")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    collection_name: str
    object_name: str
    object_type: ObjectType
    def __init__(self, collection_name: _Optional[str] = ..., object_name: _Optional[str] = ..., object_type: _Optional[_Union[ObjectType, str]] = ...) -> None: ...
