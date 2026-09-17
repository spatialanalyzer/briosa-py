"""Handwritten failures exposed by the Briosa Python client."""

from __future__ import annotations

from briosa.models import (
    ExecutionDisposition,
    LifecycleRecoveryGuidance,
    OperationFailure,
    RpcStatusCode,
    SpatialAnalyzerLifecycleFailureKind,
    SpatialAnalyzerLifecycleState,
    SpatialAnalyzerSdkLifecycleFailureKind,
    SpatialAnalyzerSdkLifecycleState,
)


class BriosaError(Exception):
    """Base class for Briosa client failures."""


class BriosaStartupError(BriosaError):
    """Reports failure to establish an owned local server session."""

    def __init__(self, diagnostic_code: str) -> None:
        super().__init__(f"Briosa startup failed ({diagnostic_code}).")
        self.diagnostic_code = diagnostic_code


class BriosaLifecycleError(BriosaError):
    """Reports invalid client lifecycle use or a competing transition."""

    def __init__(self, diagnostic_code: str) -> None:
        super().__init__(
            f"Briosa lifecycle operation is unavailable ({diagnostic_code})."
        )
        self.diagnostic_code = diagnostic_code


class BriosaProtocolError(BriosaError):
    """Reports an invalid value or shape returned by the server."""

    def __init__(self, diagnostic_code: str) -> None:
        super().__init__(f"Briosa returned invalid protocol data ({diagnostic_code}).")
        self.diagnostic_code = diagnostic_code


class BriosaCompatibilityError(BriosaError):
    """Reports a mismatch with this package's pinned protocol identity."""

    def __init__(self, diagnostic_code: str) -> None:
        super().__init__(
            f"The Briosa server is incompatible with this client ({diagnostic_code})."
        )
        self.diagnostic_code = diagnostic_code


class BriosaSpatialAnalyzerError(BriosaError):
    """Reports a typed SpatialAnalyzer application lifecycle failure."""

    def __init__(
        self,
        kind: SpatialAnalyzerLifecycleFailureKind,
        diagnostic_code: str,
        recovery_guidance: LifecycleRecoveryGuidance,
        state: SpatialAnalyzerLifecycleState,
    ) -> None:
        super().__init__(
            f"SpatialAnalyzer lifecycle operation failed ({diagnostic_code})."
        )
        self.kind = kind
        self.diagnostic_code = diagnostic_code
        self.recovery_guidance = recovery_guidance
        self.state = state


class BriosaSpatialAnalyzerSdkError(BriosaError):
    """Reports a typed SpatialAnalyzer SDK lifecycle failure."""

    def __init__(
        self,
        kind: SpatialAnalyzerSdkLifecycleFailureKind,
        diagnostic_code: str,
        recovery_guidance: LifecycleRecoveryGuidance,
        state: SpatialAnalyzerSdkLifecycleState,
    ) -> None:
        super().__init__(
            f"SpatialAnalyzer SDK lifecycle operation failed ({diagnostic_code})."
        )
        self.kind = kind
        self.diagnostic_code = diagnostic_code
        self.recovery_guidance = recovery_guidance
        self.state = state


class BriosaOperationError(BriosaError):
    """Reports a valid typed Briosa operation failure."""

    def __init__(
        self,
        status_code: RpcStatusCode,
        failure: OperationFailure,
    ) -> None:
        super().__init__(
            f"Briosa operation '{failure.operation_id}' failed "
            f"({failure.diagnostic_code})."
        )
        self.status_code = status_code
        self.failure = failure

    @property
    def completion_unknown(self) -> bool:
        return (
            self.failure.execution_disposition
            is ExecutionDisposition.STARTED_OUTCOME_UNKNOWN
        )

    @property
    def reconciliation_required(self) -> bool:
        return (
            self.completion_unknown
            and self.failure.replay_guidance.value == "reconcile_before_replay"
        )


class BriosaTransportError(BriosaError):
    """Reports a transport failure without a valid typed operation detail."""

    def __init__(self, status_code: RpcStatusCode, diagnostic_code: str) -> None:
        super().__init__(f"Briosa transport failed ({diagnostic_code}).")
        self.status_code = status_code
        self.diagnostic_code = diagnostic_code
