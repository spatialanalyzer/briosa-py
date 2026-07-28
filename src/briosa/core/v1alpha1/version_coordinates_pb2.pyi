from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersionCoordinates(_message.Message):
    __slots__ = ("briosa_version", "core_protocol_package", "spatial_analyzer_target", "target_protocol_package", "catalog_revision", "interop_fingerprint", "source_revision")
    BRIOSA_VERSION_FIELD_NUMBER: _ClassVar[int]
    CORE_PROTOCOL_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_ANALYZER_TARGET_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROTOCOL_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CATALOG_REVISION_FIELD_NUMBER: _ClassVar[int]
    INTEROP_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REVISION_FIELD_NUMBER: _ClassVar[int]
    briosa_version: str
    core_protocol_package: str
    spatial_analyzer_target: str
    target_protocol_package: str
    catalog_revision: str
    interop_fingerprint: str
    source_revision: str
    def __init__(self, briosa_version: _Optional[str] = ..., core_protocol_package: _Optional[str] = ..., spatial_analyzer_target: _Optional[str] = ..., target_protocol_package: _Optional[str] = ..., catalog_revision: _Optional[str] = ..., interop_fingerprint: _Optional[str] = ..., source_revision: _Optional[str] = ...) -> None: ...
