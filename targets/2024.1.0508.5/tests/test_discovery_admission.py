"""Admission profile and per-operation classification in discovery (#314)."""

from __future__ import annotations

import re
from enum import Enum

import pytest
from facade_support import RecordingTransport, populated, started_client
from google.protobuf import descriptor_pool

from briosa import (
    BriosaCapabilityListing,
    BriosaOperationCapability,
    OperationAdmission,
    OperationDurationClass,
    OperationRiskFlag,
    OperationValidationStatus,
    discovery_pb2,
    file_operations_pb2,
)
from briosa.transport import map_snapshot

WORKING_DIRECTORY = "/briosa.FileOperations/GetWorkingDirectory"
FINGERPRINT = "sha256:" + "ab" * 32

# Open enums: a value a later 3.x revision adds maps to UNKNOWN, never to a
# known member, and never fails discovery.
OPEN_ENUMS: tuple[type[Enum], ...] = (
    OperationRiskFlag,
    OperationDurationClass,
    OperationValidationStatus,
    OperationAdmission,
)


def capability(
    operation_id: str,
    *,
    risk_flags: tuple[int, ...] = (),
    duration_class: int = discovery_pb2.OPERATION_DURATION_CLASS_QUICK,
    validation_status: int = discovery_pb2.OPERATION_VALIDATION_STATUS_NO_RECORDED_GAP,
    admission: int = discovery_pb2.OPERATION_ADMISSION_ADMITTED,
) -> discovery_pb2.OperationCapability:
    service, rpc = {
        "file_operations.get_working_directory": (
            "briosa.FileOperations",
            "GetWorkingDirectory",
        ),
        "file_operations.delete_files": ("briosa.FileOperations", "DeleteFiles"),
        "utility_operations.run_subroutine": (
            "briosa.UtilityOperations",
            "RunSubroutine",
        ),
    }[operation_id]
    return discovery_pb2.OperationCapability(
        operation_id=operation_id,
        grpc_service=service,
        rpc=rpc,
        fully_qualified_method=f"/{service}/{rpc}",
        risk_flags=risk_flags,  # type: ignore[arg-type]
        duration_class=duration_class,  # type: ignore[arg-type]
        validation_status=validation_status,  # type: ignore[arg-type]
        admission=admission,  # type: ignore[arg-type]
    )


@pytest.mark.parametrize("public_enum", OPEN_ENUMS, ids=lambda item: item.__name__)
def test_open_enums_mirror_the_wire_enum_and_add_unknown(
    public_enum: type[Enum],
) -> None:
    wire = descriptor_pool.Default().FindEnumTypeByName(  # type: ignore[no-untyped-call]
        f"briosa.{public_enum.__name__}"
    )
    prefix = re.sub(r"(?<!^)(?=[A-Z])", "_", public_enum.__name__).upper() + "_"
    values = sorted(wire.values, key=lambda value: value.number)
    assert [member.name for member in public_enum] == [
        *(value.name.removeprefix(prefix) for value in values),
        "UNKNOWN",
    ]


async def test_snapshot_exposes_the_admission_profile_and_policy_fingerprint() -> None:
    transport = RecordingTransport()
    transport.admission_profile = "device"
    transport.policy_fingerprint = FINGERPRINT
    client = await started_client(transport)

    snapshot = await client.get_server_snapshot()

    assert snapshot.admission_profile == "device"
    assert snapshot.policy_fingerprint == FINGERPRINT
    await client.aclose()


async def test_capabilities_carry_the_reviewed_classification() -> None:
    transport = RecordingTransport()
    transport.capabilities = [
        capability("file_operations.get_working_directory"),
        capability(
            "file_operations.delete_files",
            risk_flags=(
                discovery_pb2.OPERATION_RISK_FLAG_FILESYSTEM_DELETE,
                discovery_pb2.OPERATION_RISK_FLAG_DESTRUCTIVE,
            ),
            duration_class=discovery_pb2.OPERATION_DURATION_CLASS_LONG_RUNNING,
            validation_status=discovery_pb2.OPERATION_VALIDATION_STATUS_FIXTURE_PENDING,
        ),
    ]
    client = await started_client(transport)

    snapshot = await client.get_server_snapshot()

    by_id = {item.operation_id: item for item in snapshot.operations}
    working = by_id["file_operations.get_working_directory"]
    assert working.risk_flags == ()
    assert working.duration_class is OperationDurationClass.QUICK
    assert working.validation_status is OperationValidationStatus.NO_RECORDED_GAP
    assert working.admission is OperationAdmission.ADMITTED
    delete = by_id["file_operations.delete_files"]
    assert delete.risk_flags == (
        OperationRiskFlag.FILESYSTEM_DELETE,
        OperationRiskFlag.DESTRUCTIVE,
    )
    assert delete.duration_class is OperationDurationClass.LONG_RUNNING
    assert delete.validation_status is OperationValidationStatus.FIXTURE_PENDING
    assert snapshot.supports(WORKING_DIRECTORY)
    await client.aclose()


def test_values_from_a_later_revision_map_to_unknown_without_failing() -> None:
    transport = RecordingTransport()
    transport.capabilities = [
        capability(
            "file_operations.get_working_directory",
            risk_flags=(discovery_pb2.OPERATION_RISK_FLAG_FILESYSTEM_READ, 97, 98),
            duration_class=99,
            validation_status=99,
        ),
        capability("file_operations.delete_files", admission=99),
    ]
    server = transport.server_info()
    response = discovery_pb2.ListCapabilitiesResponse(
        protocol_package=server.version.protocol_package,
        spatial_analyzer_target=server.version.spatial_analyzer_target,
        operations=transport.capabilities,
        admission_profile="standard",
        policy_fingerprint=FINGERPRINT,
    )

    snapshot = map_snapshot(server, response)

    (working,) = snapshot.operations
    assert working.risk_flags == (
        OperationRiskFlag.FILESYSTEM_READ,
        OperationRiskFlag.UNKNOWN,
    )
    assert working.duration_class is OperationDurationClass.UNKNOWN
    assert working.validation_status is OperationValidationStatus.UNKNOWN
    # An admission value the client doesn't know never admits the operation.
    assert not snapshot.supports("/briosa.FileOperations/DeleteFiles")


async def test_include_denied_lists_denials_without_admitting_them() -> None:
    transport = RecordingTransport()
    transport.capabilities = [capability("file_operations.get_working_directory")]
    transport.denied_capabilities = [
        capability(
            "file_operations.delete_files",
            risk_flags=(discovery_pb2.OPERATION_RISK_FLAG_FILESYSTEM_DELETE,),
            admission=discovery_pb2.OPERATION_ADMISSION_DENIED_PROFILE,
        ),
        capability(
            "utility_operations.run_subroutine",
            risk_flags=(discovery_pb2.OPERATION_RISK_FLAG_CODE_EXECUTION,),
            admission=discovery_pb2.OPERATION_ADMISSION_DENIED_OVERRIDE,
        ),
    ]
    client = await started_client(transport)

    listing = await client.list_capabilities(include_denied=True)

    assert isinstance(listing, BriosaCapabilityListing)
    assert transport.include_denied_requests[-1] is True
    assert listing.admission_profile == "standard"
    assert [item.operation_id for item in listing.denied] == [
        "file_operations.delete_files",
        "utility_operations.run_subroutine",
    ]
    assert [item.admission for item in listing.denied] == [
        OperationAdmission.DENIED_PROFILE,
        OperationAdmission.DENIED_OVERRIDE,
    ]
    assert [item.operation_id for item in listing.admitted] == [
        "file_operations.get_working_directory"
    ]
    assert all(
        isinstance(item, BriosaOperationCapability) for item in listing.operations
    )

    snapshot = await client.get_server_snapshot()
    assert transport.include_denied_requests[-1] is False
    assert [item.operation_id for item in snapshot.operations] == [
        "file_operations.get_working_directory"
    ]
    assert not snapshot.supports("/briosa.FileOperations/DeleteFiles")
    await client.aclose()


async def test_the_default_listing_requests_only_admitted_operations() -> None:
    transport = RecordingTransport()
    client = await started_client(transport)

    listing = await client.list_capabilities()

    assert transport.include_denied_requests[-1] is False
    assert listing.denied == ()
    await client.aclose()


async def test_a_denied_operation_is_still_sent_to_the_server() -> None:
    transport = RecordingTransport()
    transport.capabilities = []
    client = await started_client(transport)

    snapshot = await client.get_server_snapshot()
    assert not snapshot.supports(WORKING_DIRECTORY)
    transport.queue(
        WORKING_DIRECTORY, populated(file_operations_pb2.GetWorkingDirectoryResult)
    )

    # The client doesn't pre-validate admission: the server decides.
    assert await client.get_working_directory() == "x"
    await client.aclose()
