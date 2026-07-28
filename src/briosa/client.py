"""Idiomatic asynchronous adapters over generated Briosa gRPC clients."""

from __future__ import annotations

from dataclasses import dataclass
from types import TracebackType
from typing import cast
from urllib.parse import urlsplit

import grpc

from briosa.core.v1alpha1 import discovery_pb2, discovery_pb2_grpc
from briosa.errors import BriosaCallError, BriosaCompatibilityError
from briosa.protocol_identity import (
    CATALOG_ID,
    CATALOG_REVISION,
    CORE_PROTOCOL_PACKAGE,
    SPATIAL_ANALYZER_TARGET,
    TARGET_PROTOCOL_PACKAGE,
)
from briosa.sa.v2026_1_0529_7.v1alpha1 import operations_pb2, operations_pb2_grpc

GET_WORKING_DIRECTORY_METHOD = (
    "/briosa.sa.v2026_1_0529_7.v1alpha1.FileOperations/GetWorkingDirectory"
)


@dataclass(frozen=True)
class BriosaServerSnapshot:
    """One compatible discovery and capability snapshot."""

    server_info: discovery_pb2.GetServerInfoResponse
    capabilities: discovery_pb2.ListCapabilitiesResponse

    @property
    def ready_for_mp(self) -> bool:
        """Whether this worker owns a verified MP execution channel."""
        return (
            self.server_info.ready_for_mp
            and self.server_info.spatial_analyzer_execution_readiness_state
            == discovery_pb2.SPATIAL_ANALYZER_EXECUTION_READINESS_STATE_EXECUTION_READY
        )

    def supports(self, fully_qualified_method: str) -> bool:
        """Whether the exact operation is currently advertised."""
        return any(
            operation.fully_qualified_method == fully_qualified_method
            for operation in self.capabilities.operations
        )


class BriosaClient:
    """Thin asynchronous Briosa client that never retries operations."""

    def __init__(self, address: str, *, default_timeout: float = 30.0) -> None:
        if default_timeout <= 0:
            raise ValueError("default_timeout must be positive")
        target, secure = _parse_address(address)
        self._default_timeout = default_timeout
        self._channel = (
            grpc.aio.secure_channel(target, grpc.ssl_channel_credentials())
            if secure
            else grpc.aio.insecure_channel(target)
        )
        self._discovery = discovery_pb2_grpc.DiscoveryServiceStub(  # type: ignore[no-untyped-call]
            self._channel
        )
        self._file_operations = operations_pb2_grpc.FileOperationsStub(  # type: ignore[no-untyped-call]
            self._channel
        )

    async def __aenter__(self) -> BriosaClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        """Close this client's gRPC channel."""
        await self._channel.close(None)

    async def get_server_snapshot(
        self, *, timeout: float | None = None
    ) -> BriosaServerSnapshot:
        """Read discovery state and validate the exact pinned target identity."""
        effective_timeout = self._resolve_timeout(timeout)
        try:
            server_info = await self._discovery.GetServerInfo(
                discovery_pb2.GetServerInfoRequest(), timeout=effective_timeout
            )
            capabilities = await self._discovery.ListCapabilities(
                discovery_pb2.ListCapabilitiesRequest(), timeout=effective_timeout
            )
        except grpc.RpcError as error:
            raise BriosaCallError.from_rpc_error(error) from error
        _validate_compatibility(server_info, capabilities)
        return BriosaServerSnapshot(server_info, capabilities)

    async def get_working_directory(
        self, *, timeout: float | None = None
    ) -> operations_pb2.GetWorkingDirectoryResult:
        """Execute exact-target Get Working Directory once, without replay."""
        try:
            result = await self._file_operations.GetWorkingDirectory(
                operations_pb2.GetWorkingDirectoryRequest(),
                timeout=self._resolve_timeout(timeout),
            )
            return cast(operations_pb2.GetWorkingDirectoryResult, result)
        except grpc.RpcError as error:
            raise BriosaCallError.from_rpc_error(error) from error

    def _resolve_timeout(self, timeout: float | None) -> float:
        effective = self._default_timeout if timeout is None else timeout
        if effective <= 0:
            raise ValueError("timeout must be positive")
        return effective


def _parse_address(address: str) -> tuple[str, bool]:
    parsed = urlsplit(address)
    if parsed.scheme not in {"http", "https"}:
        raise ValueError("address must be an absolute HTTP or HTTPS URL")
    if (
        not parsed.netloc
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("address must contain only an HTTP(S) authority")
    return parsed.netloc, parsed.scheme == "https"


def _validate_compatibility(
    server_info: discovery_pb2.GetServerInfoResponse,
    capabilities: discovery_pb2.ListCapabilitiesResponse,
) -> None:
    if not server_info.HasField("version"):
        raise BriosaCompatibilityError("server-version-missing")
    version = server_info.version
    checks = (
        (
            version.core_protocol_package,
            CORE_PROTOCOL_PACKAGE,
            "core-protocol-package-mismatch",
        ),
        (
            version.spatial_analyzer_target,
            SPATIAL_ANALYZER_TARGET,
            "server-sa-target-mismatch",
        ),
        (
            version.target_protocol_package,
            TARGET_PROTOCOL_PACKAGE,
            "server-target-package-mismatch",
        ),
        (
            version.catalog_revision,
            CATALOG_REVISION,
            "server-catalog-revision-mismatch",
        ),
        (capabilities.catalog_id, CATALOG_ID, "capability-catalog-id-mismatch"),
        (
            capabilities.catalog_revision,
            CATALOG_REVISION,
            "capability-catalog-revision-mismatch",
        ),
        (
            capabilities.spatial_analyzer_target,
            SPATIAL_ANALYZER_TARGET,
            "capability-sa-target-mismatch",
        ),
        (
            capabilities.target_protocol_package,
            TARGET_PROTOCOL_PACKAGE,
            "capability-target-package-mismatch",
        ),
    )
    for actual, expected, diagnostic_code in checks:
        if actual != expected:
            raise BriosaCompatibilityError(diagnostic_code)
    if (
        server_info.target_isolation_mode
        != discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT
    ):
        raise BriosaCompatibilityError("target-isolation-mode-mismatch")
