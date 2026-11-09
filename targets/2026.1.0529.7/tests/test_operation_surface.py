"""Pin the public MP operation surface to the locked protocol artifact."""

from __future__ import annotations

import ast
from pathlib import Path

import briosa
from briosa import BriosaClient, wave_a_operations, wave_b_operations
from briosa import client as client_module
from briosa.operation_protocol import _REGISTERED_MODULES
from briosa.wave_a_operations import WAVE_A_OPERATIONS
from briosa.wave_b_operations import (
    WAVE_B_OPERATIONS,
    ConstructionOperations,
    GdtOperations,
    InstrumentOperations,
    RobotCalibrationApplianceNodeOperations,
    RobotOperations,
)

# Retired at contract major 3 (spatialanalyzer/briosa#320, #357 and #363):
# SA rejects the first eight on both exact targets, and no operator could
# complete the vector-name-list runtime select in licensed session 3.
RETIRED_OPERATIONS = (
    ("mirror_objects", "construction_operations.mirror_objects"),
    (
        "delete_cloud_points_by_x_y_z_range",
        "cloud_and_mesh_operations.delete_cloud_points_by_xyz_range",
    ),
    (
        "construct_circles_lines_from_surfaces",
        "construction_operations.construct_circles_lines_from_surfaces",
    ),
    (
        "add_collection_instruments_to_ref_list_wildcard_selection",
        "construction_operations.add_collection_instruments_to_ref_list_wildcard_selection",
    ),
    (
        "make_callout_view_ref_list_wildcard_selection",
        "construction_operations.make_callout_view_ref_list_wildcard_selection",
    ),
    (
        "set_callout_view_properties",
        "construction_operations.set_callout_view_properties",
    ),
    (
        "construct_polygonized_surface_from_point_clouds",
        "construction_operations.construct_polygonized_surface_from_point_clouds",
    ),
    (
        "make_collection_vector_group_name_ref_list_runtime_select",
        "construction_operations.make_collection_vector_group_name_ref_list_runtime_select",
    ),
    (
        "make_vector_name_ref_list_runtime_select",
        "construction_operations.make_vector_name_ref_list_runtime_select",
    ),
)
RETIRED_VALUE_TYPES = ("CircleLineMode", "MirrorFramePlane", "MeshOrientationType")
PUBLIC_SURFACES = (
    BriosaClient,
    ConstructionOperations,
    GdtOperations,
    InstrumentOperations,
    RobotCalibrationApplianceNodeOperations,
    RobotOperations,
)


def facade_rpcs() -> dict[str, tuple[str, str]]:
    """Map each facade's operation ID to the service and RPC it invokes."""
    found: dict[str, tuple[str, str]] = {}
    for module in (client_module, wave_a_operations, wave_b_operations):
        tree = ast.parse(Path(str(module.__file__)).read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "_invoke_mp_operation"
            ):
                continue
            literals = [
                argument.value
                for argument in node.args[:3]
                if isinstance(argument, ast.Constant)
                and isinstance(argument.value, str)
            ]
            assert len(literals) == 3, ast.unparse(node)
            service, rpc, operation_id = literals
            assert operation_id not in found, operation_id
            found[operation_id] = (service, rpc)
    return found


def protocol_methods() -> set[str]:
    return {
        f"/{service.full_name}/{method.name}"
        for module in _REGISTERED_MODULES
        for service in module.DESCRIPTOR.services_by_name.values()
        for method in service.methods
    }


def test_every_protocol_operation_has_exactly_one_facade() -> None:
    facades = facade_rpcs()
    invoked = [f"/{service}/{rpc}" for service, rpc in facades.values()]
    assert len(invoked) == len(set(invoked))
    assert set(invoked) == protocol_methods()
    assert set(facades) == (
        {item[3] for item in WAVE_A_OPERATIONS}
        | set(WAVE_B_OPERATIONS)
        | {"construction_operations.get_active_collection_name"}
    )


def test_operations_retired_at_major_3_are_gone_from_the_public_surface() -> None:
    operation_ids = {item[3] for item in WAVE_A_OPERATIONS} | set(WAVE_B_OPERATIONS)
    for method_name, operation_id in RETIRED_OPERATIONS:
        assert operation_id not in operation_ids
        assert not any(hasattr(surface, method_name) for surface in PUBLIC_SURFACES)
    for name in RETIRED_VALUE_TYPES:
        assert not hasattr(briosa, name)
        assert name not in briosa.__all__


def facade_calls() -> list[tuple[str, ast.AsyncFunctionDef, ast.Call]]:
    found = []
    for module in (client_module, wave_a_operations, wave_b_operations):
        tree = ast.parse(Path(str(module.__file__)).read_text(encoding="utf-8"))
        for function in ast.walk(tree):
            if not isinstance(function, ast.AsyncFunctionDef):
                continue
            for node in ast.walk(function):
                if (
                    isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == "_invoke_mp_operation"
                ):
                    found.append((function.name, function, node))
    return found


def test_every_facade_sends_each_argument_once() -> None:
    problems = []
    for name, function, call in facade_calls():
        parameters = {
            argument.arg
            for argument in (*function.args.args, *function.args.kwonlyargs)
            if argument.arg not in {"self", "on_mp_completion"}
        }
        values = call.args[3]
        assert isinstance(values, ast.Dict), name
        bare = [value.id for value in values.values if isinstance(value, ast.Name)]
        used = {
            node.id
            for value in values.values
            for node in ast.walk(value)
            if isinstance(node, ast.Name)
        }
        problems.extend(
            f"{name}: {item} sent {bare.count(item)} times"
            for item in sorted(set(bare))
            if bare.count(item) > 1
        )
        problems.extend(
            f"{name}: {item} never sent" for item in sorted(parameters - used)
        )
    assert problems == []
