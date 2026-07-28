"""Typed failures exposed by the Briosa client."""

from __future__ import annotations

from collections.abc import Iterable
from typing import Protocol, cast

import grpc
from google.protobuf.message import DecodeError

from briosa.core.v1alpha1 import operation_outcomes_pb2

_ERROR_TRAILER = "briosa-operation-error-bin"


class _RpcFailure(Protocol):
    def code(self) -> grpc.StatusCode: ...

    def trailing_metadata(self) -> Iterable[tuple[str, str | bytes]] | None: ...


class BriosaCompatibilityError(Exception):
    """Reports a mismatch with this package's pinned protocol identity."""

    def __init__(self, diagnostic_code: str) -> None:
        super().__init__(
            f"The Briosa server is incompatible with this client ({diagnostic_code})."
        )
        self.diagnostic_code = diagnostic_code


class BriosaCallError(Exception):
    """A failed gRPC call with an optional typed, value-free operation detail."""

    def __init__(
        self,
        status_code: grpc.StatusCode,
        operation_error: operation_outcomes_pb2.OperationError | None,
        *,
        operation_error_malformed: bool,
    ) -> None:
        super().__init__(f"Briosa call failed with gRPC status {status_code.name}.")
        self.status_code = status_code
        self.operation_error = operation_error
        self.operation_error_malformed = operation_error_malformed

    @property
    def completion_unknown(self) -> bool:
        """Whether execution started but the outcome is unknown."""
        return (
            self.operation_error is not None
            and self.operation_error.execution_disposition
            == operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN
        )

    @property
    def reconciliation_required(self) -> bool:
        """Whether reconciliation is required before any manual replay."""
        return (
            self.completion_unknown
            and self.operation_error is not None
            and self.operation_error.replay_guidance
            == operation_outcomes_pb2.REPLAY_GUIDANCE_RECONCILE_BEFORE_REPLAY
        )

    @classmethod
    def from_rpc_error(cls, error: grpc.RpcError) -> BriosaCallError:
        """Decode a typed operation detail without inspecting status text."""
        failure = cast(_RpcFailure, error)
        operation_error = None
        malformed = False
        metadata = failure.trailing_metadata() or ()
        for key, value in metadata:
            if key != _ERROR_TRAILER:
                continue
            if not isinstance(value, bytes):
                malformed = True
                break
            try:
                operation_error = operation_outcomes_pb2.OperationError.FromString(
                    value
                )
            except DecodeError:
                malformed = True
            break
        return cls(
            failure.code(),
            operation_error,
            operation_error_malformed=malformed,
        )
