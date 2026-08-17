"""Private mapping between handwritten Wave A values and generated protobuf."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import MISSING, fields, is_dataclass
from enum import Enum
from typing import Any, cast

from google.protobuf import descriptor_pool, message_factory
from google.protobuf.descriptor import FieldDescriptor, MethodDescriptor
from google.protobuf.message import Message

from briosa import (
    analysis_operations_pb2,
    dimension_operations_pb2,
    event_operations_pb2,
    file_operations_pb2,
    mp_subroutines_pb2,
    mp_task_overview_pb2,
    process_flow_operations_pb2,
    relationship_operations_pb2,
    reporting_operations_pb2,
    scale_bar_operations_pb2,
    utility_operations_pb2,
    variables_pb2,
    vector_operations_pb2,
    view_control_pb2,
)
from briosa import operation_values as public_values
from briosa.errors import BriosaProtocolError

# Imports above intentionally register every Wave A descriptor in the default pool.
_REGISTERED_MODULES = (
    analysis_operations_pb2,
    dimension_operations_pb2,
    event_operations_pb2,
    file_operations_pb2,
    mp_subroutines_pb2,
    mp_task_overview_pb2,
    process_flow_operations_pb2,
    relationship_operations_pb2,
    reporting_operations_pb2,
    scale_bar_operations_pb2,
    utility_operations_pb2,
    variables_pb2,
    vector_operations_pb2,
    view_control_pb2,
)
_DESCRIPTORS = descriptor_pool.Default()  # type: ignore[no-untyped-call]


def operation_method(service: str, rpc: str) -> MethodDescriptor:
    return cast(
        MethodDescriptor,
        _DESCRIPTORS.FindServiceByName(service).FindMethodByName(rpc),
    )


def build_request(method: MethodDescriptor, values: Mapping[str, object]) -> Message:
    request_type = message_factory.GetMessageClass(method.input_type)
    request = request_type()
    expected = {field.name for field in method.input_type.fields}
    if set(values) != expected:
        raise BriosaProtocolError("operation-request-field-drift")
    for field in method.input_type.fields:
        _assign_field(request, field, values[field.name])
    return request


def response_type(method: MethodDescriptor) -> type[Message]:
    return message_factory.GetMessageClass(method.output_type)


def map_response(
    method: MethodDescriptor,
    response: Message,
    result_type: type[Any] | None,
) -> Any:
    outputs = [
        field for field in method.output_type.fields if field.name != "execution"
    ]
    mapped = {field.name: _read_field(response, field) for field in outputs}
    if not mapped:
        return None
    if len(mapped) == 1:
        return next(iter(mapped.values()))
    if result_type is None:
        raise BriosaProtocolError("operation-result-type-missing")
    return result_type(**mapped)


def _assign_field(message: Message, field: FieldDescriptor, value: object) -> None:
    if value is None:
        raise TypeError(f"{field.name} cannot be None")
    if field.is_repeated:
        if isinstance(value, str | bytes | bytearray) or not isinstance(
            value, Iterable
        ):
            raise TypeError(f"{field.name} must be a finite non-string iterable")
        materialized = list(value)
        target = getattr(message, field.name)
        if field.type == FieldDescriptor.TYPE_MESSAGE:
            for item in materialized:
                target.add().CopyFrom(
                    _to_wire_message(field.message_type.full_name, item)
                )
        elif field.type == FieldDescriptor.TYPE_ENUM:
            target.extend(_to_wire_enum(field, item) for item in materialized)
        else:
            target.extend(materialized)
        return
    if field.type == FieldDescriptor.TYPE_MESSAGE:
        getattr(message, field.name).CopyFrom(
            _to_wire_message(field.message_type.full_name, value)
        )
    elif field.type == FieldDescriptor.TYPE_ENUM:
        setattr(message, field.name, _to_wire_enum(field, value))
    else:
        setattr(message, field.name, value)


def _to_wire_message(full_name: str, value: object) -> Message:
    if not is_dataclass(value) or isinstance(value, type):
        raise TypeError(f"{full_name} requires its handwritten Briosa value")
    descriptor = _DESCRIPTORS.FindMessageTypeByName(full_name)
    message_type = message_factory.GetMessageClass(descriptor)
    message = message_type()
    public_field_names = {item.name for item in fields(value)}
    for field in descriptor.fields:
        if field.name not in public_field_names:
            raise BriosaProtocolError("domain-value-field-drift")
        field_value = getattr(value, field.name)
        if field_value is None:
            continue
        _assign_field(message, field, field_value)
    return message


def _to_wire_enum(field: FieldDescriptor, value: object) -> int:
    if not isinstance(value, Enum):
        raise TypeError(f"{field.name} requires its handwritten Briosa enum")
    suffix = f"_{value.name}"
    match = next(
        (item.number for item in field.enum_type.values if item.name.endswith(suffix)),
        None,
    )
    if match is None or match == 0:
        raise ValueError(f"{value!r} is not valid for {field.enum_type.full_name}")
    return cast(int, match)


def _read_field(message: Message, field: FieldDescriptor) -> object:
    if field.is_repeated:
        values = getattr(message, field.name)
        mapped = [_from_wire_value(field, item) for item in values]
        return mapped
    if field.has_presence and not message.HasField(field.name):
        raise BriosaProtocolError(f"required-output-missing:{field.name}")
    return _from_wire_value(field, getattr(message, field.name))


def _from_wire_value(field: FieldDescriptor, value: object) -> object:
    if field.type == FieldDescriptor.TYPE_MESSAGE:
        if not isinstance(value, Message):
            raise BriosaProtocolError(f"invalid-message-value:{field.full_name}")
        return _from_wire_message(value)
    if field.type == FieldDescriptor.TYPE_ENUM:
        enum_class = getattr(public_values, field.enum_type.name)
        if not isinstance(value, int):
            raise BriosaProtocolError(f"invalid-enum-value:{field.full_name}")
        wire_value = field.enum_type.values_by_number.get(value)
        if wire_value is None or wire_value.number == 0:
            raise BriosaProtocolError(f"unknown-enum-value:{field.enum_type.full_name}")
        prefix = _enum_prefix(field.enum_type.name)
        return enum_class[wire_value.name.removeprefix(prefix)]
    return value


def _from_wire_message(message: Message) -> object:
    value_type = getattr(public_values, message.DESCRIPTOR.name, None)
    if value_type is None:
        raise BriosaProtocolError(
            f"unsupported-domain-value:{message.DESCRIPTOR.full_name}"
        )
    defaults = {item.name: item for item in fields(value_type)}
    values: dict[str, object] = {}
    for field in message.DESCRIPTOR.fields:
        if field.is_repeated:
            converted = [
                _from_wire_value(field, item) for item in getattr(message, field.name)
            ]
            values[field.name] = (
                tuple(converted) if value_type is public_values.Transform else converted
            )
            continue
        if field.has_presence and not message.HasField(field.name):
            dataclass_field = defaults[field.name]
            if dataclass_field.default is not MISSING:
                values[field.name] = dataclass_field.default
                continue
            if dataclass_field.default_factory is not MISSING:
                values[field.name] = dataclass_field.default_factory()
                continue
            raise BriosaProtocolError(f"required-domain-field-missing:{field.name}")
        values[field.name] = _from_wire_value(field, getattr(message, field.name))
    return value_type(**values)


def _enum_prefix(name: str) -> str:
    return re_sub_pascal(name).upper() + "_"


def re_sub_pascal(value: str) -> str:
    import re

    return re.sub(r"(?<!^)(?=[A-Z])", "_", value)


__all__ = ["build_request", "map_response", "operation_method", "response_type"]
