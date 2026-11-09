"""Per-call MP completion for every operation (#351, #360).

Every MP success is checked, observed or not: the execution details must be
present and pair SUCCEEDED with MP code 2 or PARTIAL_SUCCESS with code 4 (C1).
"""

from __future__ import annotations

import asyncio
import inspect
import typing

import grpc
import pytest
from facade_support import (
    FakeRpcError,
    RecordingTransport,
    facade_functions,
    started_client,
)

from briosa import (
    BriosaOperationError,
    BriosaProtocolError,
    MpCompletion,
    MpExecutionState,
    analysis_operations_pb2,
    construction_operations_pb2,
    file_operations_pb2,
    operation_outcomes_pb2,
)

WORKING_DIRECTORY = "/briosa.FileOperations/GetWorkingDirectory"
COLLECTION_COUNT = "/briosa.AnalysisOperations/GetNumberOfCollections"


def execution(
    state: int, code: int | None
) -> operation_outcomes_pb2.MpExecutionDetails:
    details = operation_outcomes_pb2.MpExecutionDetails(state=state)  # type: ignore[arg-type]
    if code is not None:
        details.mp_result_code = code
    return details


def directory(
    state: int, code: int | None
) -> file_operations_pb2.GetWorkingDirectoryResult:
    return file_operations_pb2.GetWorkingDirectoryResult(
        directory=r"C:\Jobs", execution=execution(state, code)
    )


PARTIAL = operation_outcomes_pb2.MP_EXECUTION_STATE_PARTIAL_SUCCESS
SUCCEEDED = operation_outcomes_pb2.MP_EXECUTION_STATE_SUCCEEDED


def test_every_mp_operation_takes_a_keyword_only_completion_observer() -> None:
    functions = facade_functions()
    assert len(functions) == len(set(functions))
    for operation_id, function in functions.items():
        parameter = inspect.signature(function).parameters.get("on_mp_completion")
        assert parameter is not None, operation_id
        assert parameter.kind is inspect.Parameter.KEYWORD_ONLY, operation_id
        assert parameter.default is None, operation_id


def test_a_completion_always_carries_its_mp_code() -> None:
    assert typing.get_type_hints(MpCompletion)["mp_result_code"] is int
    with pytest.raises(TypeError):
        typing.cast(typing.Any, MpCompletion)(state=MpExecutionState.SUCCEEDED)


async def test_partial_success_returns_its_outputs_and_reports_its_completion() -> None:
    transport = RecordingTransport()
    transport.queue(WORKING_DIRECTORY, directory(PARTIAL, 4), directory(SUCCEEDED, 2))
    client = await started_client(transport)
    first: list[MpCompletion] = []
    second: list[MpCompletion] = []

    assert await client.get_working_directory(on_mp_completion=first.append) == (
        r"C:\Jobs"
    )
    assert await client.get_working_directory(on_mp_completion=second.append) == (
        r"C:\Jobs"
    )

    assert first == [
        MpCompletion(state=MpExecutionState.PARTIAL_SUCCESS, mp_result_code=4)
    ]
    assert second == [MpCompletion(state=MpExecutionState.SUCCEEDED, mp_result_code=2)]
    await client.aclose()


async def test_partial_success_without_an_observer_still_returns_the_outputs() -> None:
    transport = RecordingTransport()
    transport.queue(WORKING_DIRECTORY, directory(PARTIAL, 4))
    transport.queue(
        COLLECTION_COUNT,
        analysis_operations_pb2.GetNumberOfCollectionsResult(
            total_count=3, execution=execution(PARTIAL, 4)
        ),
    )
    client = await started_client(transport)

    assert await client.get_working_directory() == r"C:\Jobs"
    assert await client.get_number_of_collections() == 3
    assert len(transport.requests) == 2
    await client.aclose()


async def test_generated_facades_report_the_completion_of_their_own_call() -> None:
    transport = RecordingTransport()
    transport.queue(
        COLLECTION_COUNT,
        analysis_operations_pb2.GetNumberOfCollectionsResult(
            total_count=5, execution=execution(PARTIAL, 4)
        ),
    )
    transport.queue(
        "/briosa.ConstructionOperations/GetActiveCollectionName",
        construction_operations_pb2.GetActiveCollectionNameResult(
            currently_active_collection_name="Inspection",
            execution=execution(SUCCEEDED, 2),
        ),
    )
    client = await started_client(transport)
    completions: list[MpCompletion] = []

    count = await client.get_number_of_collections(on_mp_completion=completions.append)
    await client.get_active_collection_name(on_mp_completion=completions.append)

    assert count == 5
    assert completions == [
        MpCompletion(state=MpExecutionState.PARTIAL_SUCCESS, mp_result_code=4),
        MpCompletion(state=MpExecutionState.SUCCEEDED, mp_result_code=2),
    ]
    await client.aclose()


async def test_concurrent_calls_keep_their_completions_apart() -> None:
    transport = RecordingTransport()
    transport.queue(WORKING_DIRECTORY, directory(PARTIAL, 4), directory(SUCCEEDED, 2))
    client = await started_client(transport)
    first: list[MpCompletion] = []
    second: list[MpCompletion] = []

    await asyncio.gather(
        client.get_working_directory(on_mp_completion=first.append),
        client.get_working_directory(on_mp_completion=second.append),
    )

    assert len(first) == len(second) == 1
    assert {first[0].state, second[0].state} == {
        MpExecutionState.PARTIAL_SUCCESS,
        MpExecutionState.SUCCEEDED,
    }
    await client.aclose()


async def test_a_failed_call_reports_no_completion() -> None:
    detail = operation_outcomes_pb2.OperationError(
        operation_id="file_operations.get_working_directory",
        kind=operation_outcomes_pb2.OPERATION_FAILURE_KIND_OUTPUT_RETRIEVAL_FAILURE,
        diagnostic_code="output-retrieval-failed",
        execution_disposition=operation_outcomes_pb2.EXECUTION_DISPOSITION_COMPLETED,
        mp_execution=execution(PARTIAL, 4),
    )
    transport = RecordingTransport()
    transport.queue(
        WORKING_DIRECTORY,
        FakeRpcError(
            grpc.StatusCode.DATA_LOSS,
            (("briosa-operation-error-bin", detail.SerializeToString()),),
        ),
    )
    client = await started_client(transport)
    completions: list[MpCompletion] = []

    with pytest.raises(BriosaOperationError) as captured:
        await client.get_working_directory(on_mp_completion=completions.append)

    assert completions == []
    assert captured.value.failure.mp_execution is not None
    assert captured.value.failure.mp_execution.state is MpExecutionState.PARTIAL_SUCCESS
    await client.aclose()


@pytest.mark.parametrize("observed", [True, False], ids=["observed", "unobserved"])
@pytest.mark.parametrize(
    "response",
    [
        file_operations_pb2.GetWorkingDirectoryResult(directory=r"C:\Jobs"),
        directory(operation_outcomes_pb2.MP_EXECUTION_STATE_FAILED, 3),
        directory(operation_outcomes_pb2.MP_EXECUTION_STATE_UNSPECIFIED, 2),
        directory(99, 2),
        directory(SUCCEEDED, None),
        directory(PARTIAL, None),
        directory(SUCCEEDED, 4),
        directory(PARTIAL, 2),
        directory(SUCCEEDED, 3),
    ],
    ids=[
        "missing",
        "failed",
        "unspecified",
        "unknown",
        "succeeded-without-code",
        "partial-without-code",
        "succeeded-with-code-4",
        "partial-with-code-2",
        "succeeded-with-code-3",
    ],
)
async def test_a_success_without_a_valid_completion_is_a_protocol_failure(
    response: file_operations_pb2.GetWorkingDirectoryResult, observed: bool
) -> None:
    transport = RecordingTransport()
    transport.queue(WORKING_DIRECTORY, response)
    client = await started_client(transport)
    completions: list[MpCompletion] = []
    observer = {"on_mp_completion": completions.append} if observed else {}

    with pytest.raises(BriosaProtocolError, match="mp-completion-invalid"):
        await client.get_working_directory(**observer)

    assert completions == []
    await client.aclose()


async def test_a_generated_facade_checks_its_completion_without_an_observer() -> None:
    transport = RecordingTransport()
    transport.queue(
        COLLECTION_COUNT,
        analysis_operations_pb2.GetNumberOfCollectionsResult(
            total_count=3, execution=execution(SUCCEEDED, None)
        ),
    )
    client = await started_client(transport)

    with pytest.raises(BriosaProtocolError, match="mp-completion-invalid"):
        await client.get_number_of_collections()

    await client.aclose()


async def test_a_success_whose_outputs_fail_to_map_still_reports_its_completion() -> (
    None
):
    transport = RecordingTransport()
    transport.queue(
        COLLECTION_COUNT,
        analysis_operations_pb2.GetNumberOfCollectionsResult(
            execution=execution(PARTIAL, 4)
        ),
    )
    client = await started_client(transport)
    completions: list[MpCompletion] = []

    with pytest.raises(BriosaProtocolError, match="required-output-missing"):
        await client.get_number_of_collections(on_mp_completion=completions.append)

    assert completions == [
        MpCompletion(state=MpExecutionState.PARTIAL_SUCCESS, mp_result_code=4)
    ]
    await client.aclose()
