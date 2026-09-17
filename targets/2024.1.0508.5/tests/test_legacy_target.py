from __future__ import annotations

import inspect
from collections.abc import Iterator
from typing import cast

import pytest
from test_client import FakeServerLauncher, FakeTransport, create_client

from briosa import (
    BriosaClient,
    BriosaCompatibilityError,
    BriosaProtocolError,
    CollectionInstrumentId,
    CollectionItemName,
    CollectionName,
    CollectionObjectName,
    ItemType,
    ObjectType,
    SystemString,
    construction_operations_pb2,
    instrument_operations_pb2,
    relationship_operations_pb2,
)
from briosa.transport import map_snapshot
from briosa.wave_b_operations import ConstructionOperations, GdtOperations


@pytest.mark.parametrize(
    ("method", "removed"),
    [
        ("filter_clouds_to_vector_groups_resolve_points", "include_proximity_points"),
        ("re_compute_calculated_items", "refresh_filtered_cloud_data"),
        ("make_cylinder_fit_profile", "constrain_to_nominal_axis"),
        ("make_cylinder_fit_profile", "align_with_nominal"),
        ("do_relationship_fit", "enable_randomized_start"),
        (
            "auto_filter_clouds_to_nominal_geometry_2d",
            "use_feature_specific_filter_settings",
        ),
        (
            "auto_filter_clouds_to_nominal_geometry_3d",
            "use_feature_specific_filter_settings",
        ),
        (
            "set_geom_relationship_auto_vectors_nominal_avn",
            "vector_group_custom_prefix",
        ),
        ("set_relationship_auto_vectors_fit_avf", "vector_group_custom_prefix"),
        (
            "construct_point_cloud_from_existing_clouds",
            "set_cloud_point_rgb_from_voxels",
        ),
        ("export_ascii_point_clouds", "include_cloud_point_labeling"),
        ("set_feature_check_reporting_options", "only_create_failed_vectors"),
    ],
)
def test_legacy_signatures_omit_later_inputs(method: str, removed: str) -> None:
    owner = next(
        cls
        for cls in (BriosaClient, ConstructionOperations, GdtOperations)
        if hasattr(cls, method)
    )
    assert removed not in inspect.signature(getattr(owner, method)).parameters


async def test_legacy_surface_construction_preserves_seven_explicit_false_values() -> (
    None
):
    transport = FakeTransport()
    client = create_client(FakeServerLauncher(), transport)
    await client.start()
    await client.construct_objects_from_surface_faces_runtime_select(
        construct_planes=False,
        construct_cylinders=False,
        construct_spheres=False,
        construct_cones=False,
        construct_lines=False,
        construct_points=False,
        construct_circles=False,
    )
    request = cast(
        construction_operations_pb2.ConstructObjectsFromSurfaceFacesRuntimeSelectRequest,
        transport.operation_requests[-1][1],
    )
    assert len(request.ListFields()) == 7
    assert all(value is False for _, value in request.ListFields())
    parameters = inspect.signature(
        client.construct_objects_from_surface_faces_runtime_select
    ).parameters
    assert all(p.default is inspect.Parameter.empty for p in parameters.values())
    await client.aclose()


async def test_legacy_instruments_preserve_iteration_and_empty_values() -> None:
    transport = FakeTransport()
    client = create_client(FakeServerLauncher(), transport)
    await client.start()
    instrument = CollectionInstrumentId(collection_name="Inspection", instrument_id=2)
    await client.run_crib_sheet(CollectionName(name="Inspection"), "", instrument)
    crib = cast(
        instrument_operations_pb2.RunCribSheetRequest,
        transport.operation_requests[-1][1],
    )
    assert crib.HasField("crib_sheet_name") and crib.crib_sheet_name == ""
    assert crib.instrument.instrument_id == 2
    iterations = 0

    def objects() -> Iterator[CollectionObjectName]:
        nonlocal iterations
        iterations += 1
        frame = CollectionObjectName(
            collection_name="Inspection", object_name="F1", object_type=ObjectType.FRAME
        )
        yield frame
        yield frame

    await client.project_objects(instrument, objects())
    projection = cast(
        instrument_operations_pb2.ProjectObjectsRequest,
        transport.operation_requests[-1][1],
    )
    assert iterations == 1
    assert len(projection.objects_to_project) == 2
    assert projection.objects_to_project[0] == projection.objects_to_project[1]
    await client.project_objects(instrument, [])
    projection = cast(
        instrument_operations_pb2.ProjectObjectsRequest,
        transport.operation_requests[-1][1],
    )
    assert len(projection.objects_to_project) == 0
    await client.stop_projection(instrument)
    assert (
        transport.operation_requests[-1][0]
        == "/briosa.InstrumentOperations/StopProjection"
    )
    await client.aclose()


async def test_legacy_statistics_preserve_signed_max_and_require_output() -> None:
    transport = FakeTransport()
    path = "/briosa.RelationshipOperations/GetGeneralRelationshipStatistics"
    transport.operation_responses[path] = (
        relationship_operations_pb2.GetGeneralRelationshipStatisticsResult(
            max_deviation=-2,
            rms=1,
            has_signed_deviation=False,
            signed_max_deviation=0,
            signed_min_deviation=0,
        )
    )
    client = create_client(FakeServerLauncher(), transport)
    await client.start()
    name = CollectionItemName(collection_name="Inspection", item_name="R1")
    result = await client.get_general_relationship_statistics(name)
    assert result.max_deviation == -2
    transport.operation_responses[path] = (
        relationship_operations_pb2.GetGeneralRelationshipStatisticsResult(rms=1)
    )
    with pytest.raises(BriosaProtocolError, match="required-output-missing"):
        await client.get_general_relationship_statistics(name)
    await client.aclose()


def test_legacy_choices_and_required_presence() -> None:
    assert "ENHANCED_CLOUD" not in ObjectType.__members__
    assert "ENHANCED_CLOUD" not in ItemType.__members__
    assert "LICENSE_USER_NAME" not in SystemString.__members__
    assert SystemString.USER_NAME.value == "User Name"
    for method, parameter in [
        ("direct_cad_access", "surface_compatibility_mode"),
        ("export_qdas_characteristics", "k0004_date_time_stamp"),
    ]:
        assert (
            inspect.signature(getattr(BriosaClient, method))
            .parameters[parameter]
            .default
            is inspect.Parameter.empty
        )


async def test_legacy_client_rejects_2026_discovery() -> None:
    server, capabilities = await FakeTransport().get_server_snapshot()
    server.version.spatial_analyzer_target = "2026.1.0529.7"
    with pytest.raises(BriosaCompatibilityError, match="server-sa-target-mismatch"):
        map_snapshot(server, capabilities)
