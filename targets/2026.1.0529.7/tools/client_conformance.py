"""Run one shared Briosa conformance scenario through the public Python API."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Any, TypeVar, cast

from briosa import (
    BriosaClient,
    BriosaClientOptions,
    BriosaCompatibilityError,
    BriosaOperationError,
    BriosaStartOptions,
    BriosaTransportError,
    ExecutionDisposition,
    OperationFailureKind,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerConnectionState,
    SpatialAnalyzerOwnership,
    SpatialAnalyzerSdkLifecycleState,
    SpatialAnalyzerSdkRecoveryMode,
    SpatialAnalyzerSdkState,
    SpatialAnalyzerSdkTerminationKind,
)

CONTRACT_ID = "briosa.first-party-client.v1"
WORKING_DIRECTORY_METHOD = "/briosa.FileOperations/GetWorkingDirectory"
_Error = TypeVar("_Error", bound=BaseException)


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    parser.add_argument("--contract", required=True)
    return parser.parse_args()


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


async def _expect_raises(
    error_type: type[_Error], operation: Callable[[], Awaitable[object]]
) -> _Error:
    try:
        await operation()
    except error_type as error:
        return error
    raise RuntimeError(f"Expected {error_type.__name__}.")


async def _run_scenario(scenario: str) -> None:
    command_timeout = 0.25 if scenario == "deadline" else None
    briosa = BriosaClient(BriosaClientOptions(command_timeout=command_timeout))
    startup_succeeded = False
    try:
        if scenario == "control-plane-only":
            start_options = BriosaStartOptions(
                start_spatial_analyzer_sdk=False,
                launch_spatial_analyzer=False,
                connect_to_spatial_analyzer=False,
            )
        elif scenario == "attach-existing":
            start_options = BriosaStartOptions(launch_spatial_analyzer=False)
        else:
            start_options = BriosaStartOptions()

        if scenario == "identity-mismatch":
            await _expect_raises(
                BriosaCompatibilityError, lambda: briosa.start(start_options)
            )
            await _cleanup_application(briosa)
            return

        await briosa.start(start_options)
        startup_succeeded = True

        if scenario == "control-plane-only":
            await _assert_control_plane_only(briosa)
        elif scenario == "default-ready":
            await _assert_default_ready(briosa)
        elif scenario == "attach-existing":
            await _assert_attach_existing(briosa)
        elif scenario == "capability-denied":
            await _assert_capability_denied(briosa)
        elif scenario == "mp-failure":
            await _assert_operation_failure(
                briosa,
                OperationFailureKind.MP_FAILURE,
                ExecutionDisposition.COMPLETED,
            )
        elif scenario == "output-failure":
            await _assert_operation_failure(
                briosa,
                OperationFailureKind.OUTPUT_RETRIEVAL_FAILURE,
                ExecutionDisposition.COMPLETED,
            )
        elif scenario == "deadline":
            await _assert_deadline(briosa)
        elif scenario == "cancellation":
            await _assert_cancellation(briosa)
        elif scenario == "watchdog-recovery":
            await _assert_watchdog_recovery(briosa)
        elif scenario == "sdk-loss-recovery":
            await _assert_sdk_loss_recovery(briosa)
        elif scenario == "owned-cleanup":
            await _assert_default_ready(briosa)
        else:
            raise RuntimeError(f"Unsupported conformance scenario '{scenario}'.")

        await _cleanup_application(briosa)
    finally:
        if startup_succeeded or scenario == "identity-mismatch":
            await briosa.stop()


async def _assert_control_plane_only(briosa: BriosaClient) -> None:
    snapshot = await briosa.get_server_snapshot()
    sdk = await briosa.get_spatial_analyzer_sdk_state()
    application = await briosa.get_spatial_analyzer_state()
    _require(not snapshot.ready_for_mp, "An inert server reported MP readiness.")
    _require(
        sdk.sdk_state is SpatialAnalyzerSdkState.STOPPED,
        "The SDK started implicitly.",
    )
    _require(
        application.application_state is SpatialAnalyzerApplicationState.NOT_RUNNING,
        "SpatialAnalyzer started implicitly.",
    )


async def _assert_default_ready(briosa: BriosaClient) -> None:
    snapshot = await briosa.get_server_snapshot()
    sdk = await briosa.get_spatial_analyzer_sdk_state()
    application = await briosa.get_spatial_analyzer_state()
    _require(snapshot.ready_for_mp, "Default startup did not establish readiness.")
    _require(
        snapshot.supports(WORKING_DIRECTORY_METHOD),
        "The expected operation is absent.",
    )
    _require(
        sdk.sdk_state is SpatialAnalyzerSdkState.READY and sdk.ready_for_mp,
        "The SDK is not ready after default startup.",
    )
    _require(
        application.ownership is SpatialAnalyzerOwnership.SERVER_LAUNCHED,
        "Default startup did not launch an owned application.",
    )
    await briosa.get_working_directory()


async def _assert_attach_existing(briosa: BriosaClient) -> None:
    application = await briosa.get_spatial_analyzer_state()
    sdk = await briosa.get_spatial_analyzer_sdk_state()
    _require(
        application.ownership is SpatialAnalyzerOwnership.EXTERNAL,
        "The pre-existing application was incorrectly claimed as owned.",
    )
    _require(sdk.ready_for_mp, "Attach-existing did not establish readiness.")


async def _assert_capability_denied(briosa: BriosaClient) -> None:
    snapshot = await briosa.get_server_snapshot()
    _require(
        not snapshot.supports(WORKING_DIRECTORY_METHOD),
        "A policy-denied operation remained advertised.",
    )
    error = await _expect_raises(BriosaOperationError, briosa.get_working_directory)
    _require(
        error.failure.kind is OperationFailureKind.POLICY_DENIED,
        "Policy denial did not map to the public error.",
    )
    _require(
        error.failure.execution_disposition is ExecutionDisposition.NOT_STARTED,
        "Policy denial reported an invalid execution disposition.",
    )


async def _assert_operation_failure(
    briosa: BriosaClient,
    expected_kind: OperationFailureKind,
    expected_disposition: ExecutionDisposition,
) -> None:
    error = await _expect_raises(BriosaOperationError, briosa.get_working_directory)
    _require(error.failure.kind is expected_kind, "The failure kind was not preserved.")
    _require(
        error.failure.execution_disposition is expected_disposition,
        "The execution disposition was not preserved.",
    )
    _require(
        error.failure.operation_id == "file_operations.get_working_directory",
        "The operation identity was not preserved.",
    )


async def _assert_deadline(briosa: BriosaClient) -> None:
    error = await _expect_raises(BriosaTransportError, briosa.get_working_directory)
    _require(
        error.diagnostic_code == "transport-deadline-exceeded",
        "The caller deadline did not remain a transport outcome.",
    )
    await asyncio.sleep(0.4)
    try:
        await briosa.get_working_directory()
    except BriosaTransportError as recovery_error:
        if recovery_error.diagnostic_code != "transport-deadline-exceeded":
            raise
        # If the initial deadline expired before worker dispatch, this call consumes
        # the one scripted delay. A final caller-initiated read verifies recovery.
        await asyncio.sleep(0.4)
        await briosa.get_working_directory()


async def _assert_cancellation(briosa: BriosaClient) -> None:
    operation = asyncio.create_task(briosa.get_working_directory())
    await asyncio.sleep(0.05)
    operation.cancel()
    await _expect_raises(asyncio.CancelledError, lambda: operation)
    await briosa.get_working_directory()


async def _assert_watchdog_recovery(briosa: BriosaClient) -> None:
    error = await _expect_raises(BriosaOperationError, briosa.get_working_directory)
    failure = error.failure
    _require(
        failure.kind is OperationFailureKind.WORKER_WATCHDOG_TIMEOUT,
        "The watchdog failure kind was not preserved.",
    )
    _require(
        failure.execution_disposition is ExecutionDisposition.STARTED_OUTCOME_UNKNOWN,
        "The watchdog outcome was not preserved as ambiguous.",
    )
    _require(
        failure.recovery_guidance is RecoveryGuidance.WORKER_REPLACEMENT,
        "The watchdog recovery guidance was not preserved.",
    )
    _require(
        failure.replay_guidance is ReplayGuidance.MAY_REPLAY
        and failure.replay_safety is ReplaySafety.SAFE,
        "The operation-specific replay guidance was not preserved.",
    )
    faulted = await _wait_for_sdk(
        briosa, lambda state: state.sdk_state is SpatialAnalyzerSdkState.FAULTED
    )
    _require(
        faulted.last_incident is not None
        and faulted.last_incident.termination_kind
        is SpatialAnalyzerSdkTerminationKind.WATCHDOG_TERMINATED,
        "The watchdog incident was not retained.",
    )
    await _recover_and_reconnect(briosa)


async def _assert_sdk_loss_recovery(briosa: BriosaClient) -> None:
    signal = os.environ.get("BRIOSA_CONFORMANCE_WORKER_EXIT_SIGNAL_PATH")
    _require(bool(signal), "The shared host did not provide a worker-loss signal.")
    signal_path = Path(cast(str, signal))
    signal_path.write_text("exit", encoding="utf-8")
    faulted = await _wait_for_sdk(
        briosa, lambda state: state.sdk_state is SpatialAnalyzerSdkState.FAULTED
    )
    _require(
        faulted.last_incident is not None
        and faulted.last_incident.termination_kind
        is SpatialAnalyzerSdkTerminationKind.WORKER_PROCESS_EXITED,
        "Unexpected worker loss was not diagnosed.",
    )
    signal_path.unlink(missing_ok=True)
    await _recover_and_reconnect(briosa)


async def _recover_and_reconnect(briosa: BriosaClient) -> None:
    recovered = await briosa.recover_spatial_analyzer_sdk(
        SpatialAnalyzerSdkRecoveryMode.REPLACE_WITHOUT_REPLAY
    )
    _require(
        recovered.sdk_state is SpatialAnalyzerSdkState.RUNNING
        and recovered.connection_state is SpatialAnalyzerConnectionState.DISCONNECTED,
        "SDK replacement did not create a disconnected generation.",
    )
    connected = await briosa.connect_to_spatial_analyzer()
    _require(connected.ready_for_mp, "The replacement SDK did not restore readiness.")
    await briosa.get_working_directory()


async def _wait_for_sdk(
    briosa: BriosaClient,
    predicate: Callable[[SpatialAnalyzerSdkLifecycleState], bool],
) -> SpatialAnalyzerSdkLifecycleState:
    deadline = asyncio.get_running_loop().time() + 10
    while True:
        if asyncio.get_running_loop().time() >= deadline:
            raise TimeoutError("Timed out waiting for the SDK state.")
        state = await briosa.get_spatial_analyzer_sdk_state()
        if predicate(state):
            return state
        await asyncio.sleep(0.05)


async def _cleanup_application(briosa: BriosaClient) -> None:
    sdk = await briosa.get_spatial_analyzer_sdk_state()
    if (
        sdk.sdk_generation is not None
        and sdk.sdk_state is not SpatialAnalyzerSdkState.STOPPED
    ):
        await briosa.stop_spatial_analyzer_sdk()
    application = await briosa.get_spatial_analyzer_state()
    if (
        application.ownership is SpatialAnalyzerOwnership.SERVER_LAUNCHED
        and application.application_generation is not None
        and application.application_state
        not in {
            SpatialAnalyzerApplicationState.EXITED,
            SpatialAnalyzerApplicationState.NOT_RUNNING,
        }
    ):
        await briosa.close_owned_spatial_analyzer()


async def _main() -> int:
    arguments = _parse_arguments()
    contract = cast(
        dict[str, Any],
        json.loads(Path(arguments.contract).read_text(encoding="utf-8")),
    )
    _require(
        contract.get("contract_id") == CONTRACT_ID,
        "The fixture received an unsupported conformance contract.",
    )
    scenarios = cast(list[dict[str, Any]], contract.get("scenarios", []))
    _require(
        any(item.get("id") == arguments.scenario for item in scenarios),
        "The requested scenario is absent from the conformance contract.",
    )
    await _run_scenario(cast(str, arguments.scenario))
    print(
        json.dumps(
            {
                "schema_version": 1,
                "contract_id": CONTRACT_ID,
                "scenario": arguments.scenario,
                "success": True,
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(_main()))
