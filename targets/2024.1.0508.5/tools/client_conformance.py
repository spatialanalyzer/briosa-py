"""Run one shared Briosa conformance scenario through the public Python API."""

from __future__ import annotations

import argparse
import asyncio
import inspect
import json
import os
from collections.abc import Awaitable, Callable
from dataclasses import replace
from pathlib import Path
from typing import Any, TypeVar, cast

from briosa import (
    BriosaClient,
    BriosaClientOptions,
    BriosaCompatibilityError,
    BriosaOperationError,
    BriosaServerSelection,
    BriosaSpatialAnalyzerSdkError,
    BriosaStartOptions,
    BriosaStartupError,
    BriosaTransportError,
    ExecutionDisposition,
    LifecycleRecoveryGuidance,
    MpCompletion,
    MpExecutionState,
    OperationAdmission,
    OperationDurationClass,
    OperationFailureKind,
    OperationValidationStatus,
    OutputRetrievalState,
    RecoveryGuidance,
    ReplayGuidance,
    ReplaySafety,
    RpcStatusCode,
    SpatialAnalyzerApplicationState,
    SpatialAnalyzerConnectionState,
    SpatialAnalyzerExecutionReadinessState,
    SpatialAnalyzerOwnership,
    SpatialAnalyzerSdkLifecycleFailureKind,
    SpatialAnalyzerSdkLifecycleState,
    SpatialAnalyzerSdkRecoveryMode,
    SpatialAnalyzerSdkRecoveryState,
    SpatialAnalyzerSdkState,
    SpatialAnalyzerSdkTerminationKind,
    discover_installations,
)

CONTRACT_ID = "briosa.first-party-client.v1"
WORKING_DIRECTORY_METHOD = "/briosa.FileOperations/GetWorkingDirectory"
WORKING_DIRECTORY_OPERATION = "file_operations.get_working_directory"
# lifecycle-cancellation: the fake worker holds its first Connect reply for 3 s.
INTERRUPTED_CONNECT_DEADLINE = 1.0
DETACHED_CONNECT_READINESS_LIMIT = 20.0
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
    if os.environ.get("BRIOSA_CONFORMANCE_EXPECT_INCOMPATIBLE") == "1":
        _require(
            scenario == "control-plane-only",
            "Rejection must run without SDK or application startup.",
        )
        selection = BriosaServerSelection(
            executable_path=Path(os.environ["BRIOSA_SERVER_PATH"]),
            allow_prerelease=True,
        )
        report = discover_installations(selection)
        _require(
            report.selected is None
            and report.diagnostic_code == "server-installation-incompatible",
            "The packaged server was not rejected for contract incompatibility.",
        )
        rejected = BriosaClient()
        try:
            error = await _expect_raises(
                BriosaStartupError,
                lambda: rejected.start(
                    BriosaStartOptions(
                        server_selection=selection,
                        start_spatial_analyzer_sdk=False,
                        launch_spatial_analyzer=False,
                        connect_to_spatial_analyzer=False,
                    )
                ),
            )
            _require(
                error.diagnostic_code == "server-installation-incompatible",
                "Startup failed for a reason other than contract incompatibility.",
            )
        finally:
            await rejected.aclose()
        return

    command_timeout = 0.25 if scenario == "deadline" else None
    briosa = BriosaClient(BriosaClientOptions(command_timeout=command_timeout))
    startup_succeeded = False
    try:
        if scenario in {"control-plane-only", "lifecycle-cancellation"}:
            start_options = BriosaStartOptions(
                start_spatial_analyzer_sdk=False,
                launch_spatial_analyzer=False,
                connect_to_spatial_analyzer=False,
            )
        elif scenario == "attach-existing":
            start_options = BriosaStartOptions(launch_spatial_analyzer=False)
        else:
            start_options = BriosaStartOptions()

        start_options = replace(
            start_options,
            server_selection=BriosaServerSelection(
                executable_path=Path(os.environ["BRIOSA_SERVER_PATH"]),
                allow_prerelease=True,
            ),
        )

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
        elif scenario == "sdk-call-faulted":
            await _assert_sdk_call_faulted(briosa)
        elif scenario == "mp-partial-success":
            await _assert_mp_partial_success(briosa)
        elif scenario == "lifecycle-cancellation":
            await _assert_lifecycle_cancellation(briosa)
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
    # Retained packages have the old keyword; test their actual public surface.
    parameters = inspect.signature(briosa.cloud_display_control).parameters
    key = "thin" if "thin" in parameters else "thin_draw_increment"
    arguments: dict[str, Any] = {key: 3, "point_size": 2}
    await briosa.cloud_display_control(**arguments)


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
    _require(
        snapshot.admission_profile == "standard",
        "The packaged admission profile was not reported.",
    )
    _require(
        snapshot.policy_fingerprint.startswith("sha256:"),
        "The policy fingerprint was not reported.",
    )
    _require(
        bool(snapshot.operations)
        and all(
            item.admission is OperationAdmission.ADMITTED
            and item.duration_class
            not in {OperationDurationClass.UNSPECIFIED, OperationDurationClass.UNKNOWN}
            and item.validation_status
            not in {
                OperationValidationStatus.UNSPECIFIED,
                OperationValidationStatus.UNKNOWN,
            }
            for item in snapshot.operations
        ),
        "An admitted capability lacks its reviewed classification.",
    )
    listing = await briosa.list_capabilities(include_denied=True)
    denied = [
        item
        for item in listing.denied
        if item.operation_id == WORKING_DIRECTORY_OPERATION
    ]
    _require(
        len(denied) == 1 and denied[0].admission is OperationAdmission.DENIED_OVERRIDE,
        "The denied listing did not report the override denial.",
    )
    _require(
        listing.policy_fingerprint == snapshot.policy_fingerprint,
        "The diagnostic listing reported a different policy.",
    )
    refreshed = await briosa.get_server_snapshot()
    _require(
        not refreshed.supports(WORKING_DIRECTORY_METHOD),
        "The denied listing made a denied operation callable.",
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


async def _assert_sdk_call_faulted(briosa: BriosaClient) -> None:
    error = await _expect_raises(BriosaOperationError, briosa.get_working_directory)
    failure = error.failure
    _require(
        error.status_code is RpcStatusCode.INTERNAL,
        "The SDK call fault did not keep its gRPC status.",
    )
    _require(
        failure.kind is OperationFailureKind.SDK_CALL_FAULTED,
        "The SDK call fault was folded into another failure kind.",
    )
    _require(
        failure.diagnostic_code == "sdk-execute-step-faulted"
        and failure.operation_id == WORKING_DIRECTORY_OPERATION,
        "The SDK call fault identity was not preserved.",
    )
    _require(
        failure.execution_disposition is ExecutionDisposition.STARTED_OUTCOME_UNKNOWN
        and failure.recovery_guidance is RecoveryGuidance.NONE
        and failure.replay_guidance is ReplayGuidance.RECONCILE_BEFORE_REPLAY,
        "The SDK call fault phase or guidance was not preserved.",
    )
    _require(
        failure.mp_execution is not None
        and failure.mp_execution.state is MpExecutionState.RESULT_UNAVAILABLE
        and failure.mp_execution.mp_result_code is None,
        "The SDK call fault lost its MP execution details.",
    )
    # A per-call SDK fault keeps the worker generation in service.
    await briosa.get_working_directory()


async def _assert_mp_partial_success(briosa: BriosaClient) -> None:
    first: list[MpCompletion] = []
    second: list[MpCompletion] = []
    partial = await briosa.get_working_directory(on_mp_completion=first.append)
    succeeded = await briosa.get_working_directory(on_mp_completion=second.append)
    _require(
        bool(partial) and bool(succeeded),
        "A partial success did not return its output.",
    )
    _require(
        first
        == [MpCompletion(state=MpExecutionState.PARTIAL_SUCCESS, mp_result_code=4)],
        "The partial success completion was not reported for its call.",
    )
    _require(
        second == [MpCompletion(state=MpExecutionState.SUCCEEDED, mp_result_code=2)],
        "The next call did not report its own completion.",
    )
    third: list[MpCompletion] = []
    error = await _expect_raises(
        BriosaOperationError,
        lambda: briosa.get_working_directory(on_mp_completion=third.append),
    )
    failure = error.failure
    _require(
        error.status_code is RpcStatusCode.DATA_LOSS
        and failure.kind is OperationFailureKind.OUTPUT_RETRIEVAL_FAILURE
        and failure.execution_disposition is ExecutionDisposition.COMPLETED
        and failure.replay_guidance is ReplayGuidance.DO_NOT_REPLAY,
        "The partial success without output did not fail as an output failure.",
    )
    execution = failure.mp_execution
    _require(
        execution is not None
        and execution.state is MpExecutionState.PARTIAL_SUCCESS
        and execution.mp_result_code == 4
        and len(execution.output_retrievals) == 1
        and execution.output_retrievals[0].state is OutputRetrievalState.FAILED,
        "The typed failure did not keep PartialSuccess distinct.",
    )
    _require(third == [], "A failed call reported an MP completion.")


async def _assert_lifecycle_cancellation(briosa: BriosaClient) -> None:
    application = await briosa.get_spatial_analyzer_state()
    _require(
        application.application_state is SpatialAnalyzerApplicationState.RUNNING
        and application.ownership is SpatialAnalyzerOwnership.EXTERNAL
        and application.application_generation is not None,
        "The scenario requires the external SpatialAnalyzer.",
    )
    started = await briosa.start_spatial_analyzer_sdk()
    generation = started.sdk_generation
    if (
        generation is None
        or started.sdk_state is not SpatialAnalyzerSdkState.RUNNING
        or started.connection_state is not SpatialAnalyzerConnectionState.DISCONNECTED
        or started.ready_for_mp
    ):
        raise RuntimeError("The SDK did not start disconnected.")

    # 1. The deadline ends only this caller's wait: the language-native deadline
    #    outcome, with no invented disposition and no retry.
    deadline = await _expect_raises(
        BriosaTransportError,
        lambda: briosa.connect_to_spatial_analyzer(
            timeout=INTERRUPTED_CONNECT_DEADLINE
        ),
    )
    _require(
        deadline.status_code is RpcStatusCode.DEADLINE_EXCEEDED
        and deadline.diagnostic_code == "transport-deadline-exceeded",
        "The interrupted Connect did not surface as the caller's deadline.",
    )

    # 2. The accepted Connect still holds the lifecycle.
    in_progress = await _expect_raises(
        BriosaSpatialAnalyzerSdkError, briosa.connect_to_spatial_analyzer
    )
    _require(
        in_progress.kind is SpatialAnalyzerSdkLifecycleFailureKind.STATE_CONFLICT
        and in_progress.diagnostic_code == "sdk-lifecycle-transition-in-progress"
        and in_progress.recovery_guidance is LifecycleRecoveryGuidance.REFRESH_STATE,
        "A second Connect was not rejected as a transition in progress.",
    )
    _require(
        in_progress.state.sdk_generation == generation
        and in_progress.state.sdk_state
        in {SpatialAnalyzerSdkState.CONNECTING, SpatialAnalyzerSdkState.VERIFYING},
        "The transition in progress reported another generation or phase.",
    )

    # 3. Refreshing state shows the detached Connect finish on the same generation.
    ready = await _wait_for_detached_connect(briosa, generation)
    _require(
        ready.ready_for_mp
        and ready.connection_state is SpatialAnalyzerConnectionState.CONNECTED
        and ready.execution_readiness_state
        is SpatialAnalyzerExecutionReadinessState.EXECUTION_READY
        and ready.recovery_state is SpatialAnalyzerSdkRecoveryState.NOT_REQUIRED
        and ready.last_incident is None
        and ready.application_generation == application.application_generation,
        "The detached Connect did not leave the generation ready.",
    )

    # 4. MP work runs on that generation once discovery confirms readiness.
    snapshot = await briosa.get_server_snapshot()
    _require(snapshot.ready_for_mp, "Discovery did not report MP readiness.")
    await briosa.get_working_directory()

    # 5. A clean stop leaves the external application running.
    stopped = await briosa.stop_spatial_analyzer_sdk()
    after = await briosa.get_spatial_analyzer_state()
    _require(
        stopped.sdk_state is SpatialAnalyzerSdkState.STOPPED
        and not stopped.ready_for_mp
        and after.application_state is SpatialAnalyzerApplicationState.RUNNING
        and after.ownership is SpatialAnalyzerOwnership.EXTERNAL
        and after.application_generation == application.application_generation,
        "The lifecycle shutdown was not clean.",
    )


async def _wait_for_detached_connect(
    briosa: BriosaClient, generation: int
) -> SpatialAnalyzerSdkLifecycleState:
    loop = asyncio.get_running_loop()
    deadline = loop.time() + DETACHED_CONNECT_READINESS_LIMIT
    while True:
        state = await briosa.get_spatial_analyzer_sdk_state()
        _require(
            state.sdk_generation == generation,
            "The detached Connect changed the SDK generation.",
        )
        if state.sdk_state is SpatialAnalyzerSdkState.READY:
            return state
        _require(
            state.sdk_state
            in {SpatialAnalyzerSdkState.CONNECTING, SpatialAnalyzerSdkState.VERIFYING},
            "The detached Connect ended without readiness.",
        )
        if loop.time() >= deadline:
            raise TimeoutError("Timed out waiting for the detached Connect.")
        await asyncio.sleep(0.05)


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
