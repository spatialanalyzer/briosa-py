from __future__ import annotations

from typing import Any, cast

import grpc
import pytest

from briosa import BriosaCallError, BriosaClient, BriosaCompatibilityError
from briosa.client import _validate_compatibility
from briosa.core.v1alpha1 import (
    discovery_pb2,
    operation_outcomes_pb2,
    version_coordinates_pb2,
)
from briosa.protocol_identity import (
    ARTIFACT_NAME,
    ARTIFACT_SHA256,
    BRIOSA_VERSION,
    CATALOG_ID,
    CATALOG_REVISION,
    CORE_PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
    TARGET_PROTOCOL_PACKAGE,
)
from briosa.sa.v2026_1_0529_7.v1alpha1 import operations_pb2


class FakeRpcError(grpc.RpcError):
    def __init__(
        self,
        status_code: grpc.StatusCode,
        metadata: tuple[tuple[str, str | bytes], ...] = (),
    ) -> None:
        super().__init__()
        self._status_code = status_code
        self._metadata = metadata

    def code(self) -> grpc.StatusCode:
        return self._status_code

    def trailing_metadata(  # type: ignore[override]
        self,
    ) -> tuple[tuple[str, str | bytes], ...]:
        return self._metadata


def matching_identity() -> tuple[
    discovery_pb2.GetServerInfoResponse, discovery_pb2.ListCapabilitiesResponse
]:
    return (
        discovery_pb2.GetServerInfoResponse(
            version=version_coordinates_pb2.VersionCoordinates(
                core_protocol_package=CORE_PROTOCOL_PACKAGE,
                spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
                target_protocol_package=TARGET_PROTOCOL_PACKAGE,
                catalog_revision=CATALOG_REVISION,
            ),
            target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
        ),
        discovery_pb2.ListCapabilitiesResponse(
            catalog_id=CATALOG_ID,
            catalog_revision=CATALOG_REVISION,
            spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
            target_protocol_package=TARGET_PROTOCOL_PACKAGE,
        ),
    )


def test_protocol_identity_matches_pinned_artifact() -> None:
    assert ARTIFACT_NAME == "briosa-protocol-0.2.0-dev.2-sa-2026.1.0529.7-catalog-5"
    assert (
        ARTIFACT_SHA256
        == "4ce33ac6ecc9db382e870aa2c005f90a25128ad863fcf007c855d00470ea3e39"
    )
    assert BRIOSA_VERSION == "0.2.0-dev.2"
    assert SOURCE_REVISION == "1a0714345981592b37e26a90ffc4db0de32fe388"
    assert SPATIAL_ANALYZER_TARGET == "2026.1.0529.7"
    assert CATALOG_REVISION == "5"


def test_compatibility_accepts_exact_identity() -> None:
    _validate_compatibility(*matching_identity())


def test_compatibility_rejects_catalog_and_isolation_drift() -> None:
    server_info, capabilities = matching_identity()
    capabilities.catalog_revision = "different"
    with pytest.raises(BriosaCompatibilityError) as catalog_error:
        _validate_compatibility(server_info, capabilities)
    assert catalog_error.value.diagnostic_code == "capability-catalog-revision-mismatch"

    server_info, capabilities = matching_identity()
    server_info.target_isolation_mode = (
        discovery_pb2.TARGET_ISOLATION_MODE_LEASE_ISOLATED
    )
    with pytest.raises(BriosaCompatibilityError) as isolation_error:
        _validate_compatibility(server_info, capabilities)
    assert isolation_error.value.diagnostic_code == "target-isolation-mode-mismatch"


def test_typed_error_preserves_unknown_completion_and_reconciliation() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="conformance.mutating_operation",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_WORKER_WATCHDOG_TIMEOUT,
        diagnostic_code="worker-execution-watchdog-timeout",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN,
        recovery_guidance=operation_outcomes_pb2.RECOVERY_GUIDANCE_WORKER_REPLACEMENT,
        replay_guidance=operation_outcomes_pb2.REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY,
        replay_safety=operation_outcomes_pb2.REPLAY_SAFETY_UNSAFE,
    )
    error = FakeRpcError(
        grpc.StatusCode.UNAVAILABLE,
        (("briosa-operation-error-bin", detail.SerializeToString()),),
    )

    mapped = BriosaCallError.from_rpc_error(error)

    assert mapped.status_code is grpc.StatusCode.UNAVAILABLE
    assert mapped.operation_error == detail
    assert mapped.completion_unknown
    assert mapped.reconciliation_required
    assert not mapped.operation_error_malformed


def test_malformed_typed_error_does_not_parse_status_text() -> None:
    error = FakeRpcError(
        grpc.StatusCode.DATA_LOSS, (("briosa-operation-error-bin", b"\xff"),)
    )
    mapped = BriosaCallError.from_rpc_error(error)
    assert mapped.status_code is grpc.StatusCode.DATA_LOSS
    assert mapped.operation_error is None
    assert mapped.operation_error_malformed
    assert "untrusted detail" not in str(mapped)


def test_optional_string_preserves_absent_and_default_like_presence() -> None:
    absent = operations_pb2.GetWorkingDirectoryResult()
    present_empty = operations_pb2.GetWorkingDirectoryResult(directory="")
    assert not absent.HasField("directory")
    assert present_empty.HasField("directory")
    assert present_empty.directory == ""


@pytest.mark.asyncio
async def test_failed_operation_is_not_automatically_replayed() -> None:
    class FailingOperations:
        calls = 0

        async def GetWorkingDirectory(self, request: Any, *, timeout: float) -> None:
            self.calls += 1
            raise FakeRpcError(grpc.StatusCode.UNAVAILABLE)

    client = BriosaClient("http://127.0.0.1:50051")
    operations = FailingOperations()
    cast(Any, client)._file_operations = operations
    try:
        with pytest.raises(BriosaCallError):
            await client.get_working_directory()
        assert operations.calls == 1
    finally:
        await client.close()


def test_address_and_timeouts_fail_closed() -> None:
    with pytest.raises(ValueError):
        BriosaClient("ftp://localhost:50051")
    with pytest.raises(ValueError):
        BriosaClient("http://localhost:50051/path")
    with pytest.raises(ValueError):
        BriosaClient("http://localhost:50051", default_timeout=0)
