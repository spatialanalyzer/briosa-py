from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VersionCoordinates(_message.Message):
    __slots__ = ("briosa_version", "protocol_package", "spatial_analyzer_target", "interop_fingerprint", "source_revision")
    BRIOSA_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SPATIAL_ANALYZER_TARGET_FIELD_NUMBER: _ClassVar[int]
    INTEROP_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_REVISION_FIELD_NUMBER: _ClassVar[int]
    briosa_version: str
    protocol_package: str
    spatial_analyzer_target: str
    interop_fingerprint: str
    source_revision: str
    def __init__(self, briosa_version: _Optional[str] = ..., protocol_package: _Optional[str] = ..., spatial_analyzer_target: _Optional[str] = ..., interop_fingerprint: _Optional[str] = ..., source_revision: _Optional[str] = ...) -> None: ...
