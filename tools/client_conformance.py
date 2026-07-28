"""Language adapter for Briosa's shared client conformance fixtures."""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any, NoReturn, cast

import grpc

from briosa import BriosaCallError, BriosaClient, BriosaCompatibilityError
from briosa.client import GET_WORKING_DIRECTORY_METHOD
from briosa.core.v1alpha1 import operation_outcomes_pb2
from briosa.sa.v2026_1_0529_7.v1alpha1 import operations_pb2


def _require(condition: bool, failure: str) -> None:
    if not condition:
        raise RuntimeError(failure)


def _required_string(value: dict[str, Any], key: str) -> str:
    result = value.get(key)
    if not isinstance(result, str):
        raise ValueError(f"{key!r} must be a string")
    return result


def _enum_number(message: Any, field_name: str, enum_name: str) -> int:
    field = message.DESCRIPTOR.fields_by_name[field_name]
    value = field.enum_type.values_by_name.get(enum_name)
    if value is None:
        raise ValueError(f"Unknown protobuf enum name {enum_name!r}")
    return int(value.number)


class _FixtureRpcError(grpc.RpcError):
    def __init__(
        self, status_code: grpc.StatusCode, metadata: tuple[tuple[str, bytes], ...]
    ) -> None:
        super().__init__()
        self._status_code = status_code
        self._metadata = metadata

    def code(self) -> grpc.StatusCode:
        return self._status_code

    def trailing_metadata(self) -> tuple[tuple[str, bytes], ...]:  # type: ignore[override]
        return self._metadata


def _operation_error(value: dict[str, Any]) -> operation_outcomes_pb2.OperationError:
    error = operation_outcomes_pb2.OperationError(
        operation_id=_required_string(value, "operation_id"),
        diagnostic_code=_required_string(value, "diagnostic_code"),
    )
    for field_name in (
        "kind",
        "execution_disposition",
        "recovery_guidance",
        "replay_guidance",
        "replay_safety",
    ):
        setattr(
            error,
            field_name,
            _enum_number(error, field_name, _required_string(value, field_name)),
        )
    mp_value = value.get("mp_execution")
    if isinstance(mp_value, dict):
        execution = error.mp_execution
        execution.state = cast(
            Any,
            _enum_number(execution, "state", _required_string(mp_value, "state")),
        )
        if bool(mp_value.get("mp_result_code_present")):
            execution.mp_result_code = 2
        retrieval = execution.output_retrievals.add(field_name="directory")
        retrieval.state = cast(
            Any,
            _enum_number(
                retrieval,
                "state",
                _required_string(mp_value, "output_retrieval_state"),
            ),
        )
    return error


def verify_error_fixtures(fixture_path: Path) -> None:
    root = json.loads(fixture_path.read_text(encoding="utf-8"))
    _require(
        root.get("fixture_set_id") == "briosa.client.operation-errors.v1",
        "error-fixture-identity",
    )
    for item in root["cases"]:
        error = _operation_error(item["operation_error"])
        status = grpc.StatusCode[_required_string(item, "grpc_status")]
        rpc_error = _FixtureRpcError(
            status, (("briosa-operation-error-bin", error.SerializeToString()),)
        )
        mapped = BriosaCallError.from_rpc_error(rpc_error)
        behavior = item["client_behavior"]
        _require(mapped.status_code is status, "offline-status-mismatch")
        _require(mapped.operation_error == error, "offline-error-mismatch")
        _require(
            mapped.completion_unknown
            == (
                error.execution_disposition
                == operation_outcomes_pb2.EXECUTION_DISPOSITION_STARTED_OUTCOME_UNKNOWN
            ),
            "offline-disposition-mismatch",
        )
        _require(
            mapped.reconciliation_required == bool(behavior["reconciliation_required"]),
            "offline-reconciliation-mismatch",
        )
        _require(not bool(behavior["automatic_replay"]), "automatic-replay-prohibited")


def _validate_success(result: operations_pb2.GetWorkingDirectoryResult) -> None:
    _require(result.HasField("directory"), "directory-presence-missing")
    _require(result.HasField("execution"), "mp-execution-missing")
    _require(
        result.execution.state == operation_outcomes_pb2.MP_EXECUTION_STATE_SUCCEEDED,
        "mp-execution-not-successful",
    )
    _require(
        len(result.execution.output_retrievals) == 1
        and result.execution.output_retrievals[0].state
        == operation_outcomes_pb2.OUTPUT_RETRIEVAL_STATE_RETRIEVED,
        "output-retrieval-not-successful",
    )


async def _unsupported_status(address: str) -> grpc.StatusCode:
    target = address.removeprefix("http://").removeprefix("https://")
    channel = grpc.aio.insecure_channel(target)
    try:
        call = channel.unary_unary(
            "/briosa.sa.v1900_1_0000_0.v1alpha1.FileOperations/GetWorkingDirectory",
            request_serializer=lambda value: value,
            response_deserializer=lambda value: value,
        )
        try:
            await call(b"", timeout=15.0)
        except grpc.RpcError as error:
            return error.code()
        raise RuntimeError("Unsupported method succeeded")
    finally:
        await channel.close(None)


async def run_live_scenario(address: str, fixture_path: Path, scenario_id: str) -> None:
    root = json.loads(fixture_path.read_text(encoding="utf-8"))
    _require(root.get("fixture_set_id") == "briosa.client.live.v1", "fixture-identity")
    scenario = next(item for item in root["scenarios"] if item["id"] == scenario_id)
    expected = scenario["expected"]
    operation_succeeded = False
    recovery_succeeded = False
    typed_error_observed = False
    failure_kind: str | None = None
    status = grpc.StatusCode.OK

    async with BriosaClient(address, default_timeout=15.0) as client:
        snapshot = await client.get_server_snapshot()
        _require(
            snapshot.ready_for_mp == expected["ready_for_mp"], "readiness-mismatch"
        )
        _require(
            snapshot.supports(GET_WORKING_DIRECTORY_METHOD)
            == expected["operation_advertised"],
            "capability-mismatch",
        )
        if scenario_id == "unsupported-version":
            status = await _unsupported_status(address)
            failure_kind = "OPERATION_FAILURE_KIND_UNSUPPORTED"
        else:
            try:
                if scenario_id == "deadline":
                    await client.get_working_directory(timeout=0.05)
                elif scenario_id == "cancellation":
                    task = asyncio.create_task(client.get_working_directory())
                    await asyncio.sleep(0.05)
                    task.cancel()
                    try:
                        await task
                    except asyncio.CancelledError:
                        status = grpc.StatusCode.CANCELLED
                else:
                    result = await client.get_working_directory()
                    _validate_success(result)
                    operation_succeeded = True
            except BriosaCallError as error:
                status = error.status_code
                typed_error_observed = error.operation_error is not None
                if error.operation_error is not None:
                    failure_kind = operation_outcomes_pb2.OperationFailureKind.Name(
                        error.operation_error.kind
                    )

            if scenario_id in {"deadline", "cancellation", "watchdog-recovery"}:
                recovery = await client.get_working_directory()
                _validate_success(recovery)
                recovery_succeeded = True

    _require(status.name == expected["grpc_status"], "grpc-status-mismatch")
    _require(
        operation_succeeded == expected["operation_succeeded"],
        "operation-outcome-mismatch",
    )
    _require(
        recovery_succeeded == expected["recovery_succeeded"],
        "recovery-outcome-mismatch",
    )
    _require(
        typed_error_observed == expected["typed_error_required"],
        "typed-error-presence-mismatch",
    )
    expected_kinds = expected["failure_kinds"]
    _require(
        (failure_kind is None and not expected_kinds) or failure_kind in expected_kinds,
        "failure-kind-mismatch",
    )


def _fail(error: Exception) -> NoReturn:
    print(
        json.dumps(
            {"schema_version": 1, "success": False, "failure": type(error).__name__}
        ),
        file=sys.stderr,
    )
    raise SystemExit(1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--error-fixture", type=Path)
    parser.add_argument("--address")
    parser.add_argument("--scenario")
    parser.add_argument("--fixture", type=Path)
    args = parser.parse_args()
    try:
        if args.error_fixture is not None:
            verify_error_fixtures(args.error_fixture)
            scenario = "typed-errors"
        elif args.address and args.scenario and args.fixture:
            asyncio.run(run_live_scenario(args.address, args.fixture, args.scenario))
            scenario = args.scenario
        else:
            raise ValueError("Supply --error-fixture or all live scenario arguments")
        print(json.dumps({"schema_version": 1, "success": True, "scenario": scenario}))
        return 0
    except (
        BriosaCallError,
        BriosaCompatibilityError,
        RuntimeError,
        ValueError,
    ) as error:
        _fail(error)


if __name__ == "__main__":
    raise SystemExit(main())
