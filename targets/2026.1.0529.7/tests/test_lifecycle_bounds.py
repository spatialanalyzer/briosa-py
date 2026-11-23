"""Published lifecycle bounds and the configured interaction mode (briosa#400).

Server 0.10.1 and later publish them in GetServerInfo; Server 0.10.0 does not.
An absent or zero allowance is unavailable, the host shutdown bound is read from
its ``limit`` case and never inferred unbounded, and an unknown mode or a missing
host bound leaves the other values usable.
"""

from __future__ import annotations

from datetime import timedelta

import pytest
from google.protobuf import descriptor_pool

from briosa import (
    BriosaLifecycleBounds,
    ConfiguredSpatialAnalyzerInteractionMode,
    GracefulShutdownBound,
    GracefulShutdownBoundKind,
    discovery_pb2,
    version_coordinates_pb2,
)
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET
from briosa.transport import map_snapshot

# Server 0.10.1 defaults: 45, 30, 60, 55, 15 and 30 s per operation, 100 and
# 70 s for a startup with and without launch, and a 105 s host bound.
DEFAULT_BOUNDS = {
    "start_sdk_milliseconds": 45_000,
    "launch_spatial_analyzer_milliseconds": 30_000,
    "connect_spatial_analyzer_milliseconds": 60_000,
    "recover_sdk_milliseconds": 55_000,
    "stop_sdk_milliseconds": 15_000,
    "close_owned_spatial_analyzer_milliseconds": 30_000,
    "startup_with_launch_milliseconds": 100_000,
    "startup_without_launch_milliseconds": 70_000,
}


def server_info(
    bounds: discovery_pb2.LifecycleBounds | None = None,
    mode: int = discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_UNSPECIFIED,
) -> discovery_pb2.GetServerInfoResponse:
    server = discovery_pb2.GetServerInfoResponse(
        version=version_coordinates_pb2.VersionCoordinates(
            briosa_version="0.10.1",
            source_revision="a" * 40,
            protocol_package="briosa",
            spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
        ),
        compatibility=discovery_pb2.CompatibilityContract(major=3, revision=1),
        target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
        configured_spatial_analyzer_interaction_mode=mode,  # type: ignore[arg-type]
    )
    if bounds is not None:
        server.lifecycle_bounds.CopyFrom(bounds)
    return server


def capabilities() -> discovery_pb2.ListCapabilitiesResponse:
    return discovery_pb2.ListCapabilitiesResponse(
        protocol_package="briosa", spatial_analyzer_target=SPATIAL_ANALYZER_TARGET
    )


def mapped(server: discovery_pb2.GetServerInfoResponse) -> BriosaLifecycleBounds:
    bounds = map_snapshot(server, capabilities()).lifecycle_bounds
    assert bounds is not None
    return bounds


def test_server_0_10_0_publishes_no_bounds_and_no_mode() -> None:
    server = server_info()
    server.compatibility.revision = 0
    server.version.briosa_version = "0.10.0"
    snapshot = map_snapshot(server, capabilities())
    assert snapshot.lifecycle_bounds is None
    assert (
        snapshot.configured_interaction_mode
        is ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN
    )


def test_every_published_allowance_is_an_optional_duration() -> None:
    raw = discovery_pb2.LifecycleBounds(**DEFAULT_BOUNDS)  # type: ignore[arg-type]
    raw.host_graceful_shutdown.finite_milliseconds = 105_000
    assert mapped(server_info(raw)) == BriosaLifecycleBounds(
        start_sdk=timedelta(seconds=45),
        launch_spatial_analyzer=timedelta(seconds=30),
        connect_spatial_analyzer=timedelta(seconds=60),
        recover_sdk=timedelta(seconds=55),
        stop_sdk=timedelta(seconds=15),
        close_owned_spatial_analyzer=timedelta(seconds=30),
        startup_with_launch=timedelta(seconds=100),
        startup_without_launch=timedelta(seconds=70),
        host_graceful_shutdown=GracefulShutdownBound(
            kind=GracefulShutdownBoundKind.FINITE, duration=timedelta(seconds=105)
        ),
    )


def test_a_millisecond_and_the_largest_allowance_are_exact() -> None:
    raw = discovery_pb2.LifecycleBounds(
        start_sdk_milliseconds=1, startup_with_launch_milliseconds=4_294_967_295
    )
    bounds = mapped(server_info(raw))
    assert bounds.start_sdk == timedelta(milliseconds=1)
    assert bounds.startup_with_launch == timedelta(milliseconds=4_294_967_295)


@pytest.mark.parametrize("name", sorted(DEFAULT_BOUNDS))
def test_an_absent_or_zero_allowance_is_unavailable(name: str) -> None:
    public = name.removesuffix("_milliseconds")
    absent = discovery_pb2.LifecycleBounds(
        **{key: value for key, value in DEFAULT_BOUNDS.items() if key != name}  # type: ignore[arg-type]
    )
    zero = discovery_pb2.LifecycleBounds(**{**DEFAULT_BOUNDS, name: 0})  # type: ignore[arg-type]
    assert zero.HasField(name)
    for raw in (absent, zero):
        bounds = mapped(server_info(raw))
        assert getattr(bounds, public) is None
        others = [key for key in DEFAULT_BOUNDS if key != name]
        assert all(
            getattr(bounds, key.removesuffix("_milliseconds")) is not None
            for key in others
        )


def test_the_wire_fields_and_the_public_allowances_correspond() -> None:
    wire = descriptor_pool.Default().FindMessageTypeByName(  # type: ignore[no-untyped-call]
        "briosa.LifecycleBounds"
    )
    names = [field.name for field in wire.fields]
    assert names == [*DEFAULT_BOUNDS, "host_graceful_shutdown"]
    assert set(BriosaLifecycleBounds.__dataclass_fields__) == {
        name.removesuffix("_milliseconds") for name in names
    }


def shutdown(raw: discovery_pb2.LifecycleBounds) -> GracefulShutdownBound:
    return mapped(server_info(raw)).host_graceful_shutdown


def test_host_shutdown_bound_absent_is_unavailable() -> None:
    assert shutdown(discovery_pb2.LifecycleBounds()) == GracefulShutdownBound(
        kind=GracefulShutdownBoundKind.UNAVAILABLE
    )


def test_host_shutdown_bound_without_a_limit_case_is_unavailable() -> None:
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.SetInParent()
    assert raw.HasField("host_graceful_shutdown")
    assert shutdown(raw).kind is GracefulShutdownBoundKind.UNAVAILABLE


def test_host_shutdown_bound_of_zero_is_unavailable_never_unbounded() -> None:
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.finite_milliseconds = 0
    assert raw.host_graceful_shutdown.WhichOneof("limit") == "finite_milliseconds"
    assert shutdown(raw).kind is GracefulShutdownBoundKind.UNAVAILABLE


def test_host_shutdown_bound_explicitly_unbounded() -> None:
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.unbounded.SetInParent()
    assert shutdown(raw) == GracefulShutdownBound(
        kind=GracefulShutdownBoundKind.UNBOUNDED
    )


def test_host_shutdown_bound_finite() -> None:
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.finite_milliseconds = 4_294_967_294
    assert shutdown(raw) == GracefulShutdownBound(
        kind=GracefulShutdownBoundKind.FINITE,
        duration=timedelta(milliseconds=4_294_967_294),
    )


def test_a_finite_bound_too_large_to_represent_is_unavailable() -> None:
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.finite_milliseconds = 2**64 - 1
    assert shutdown(raw).kind is GracefulShutdownBoundKind.UNAVAILABLE


def test_a_limit_case_from_a_later_release_is_unavailable() -> None:
    # GracefulShutdownBound field 3, a case this client doesn't know.
    later = discovery_pb2.GracefulShutdownBound.FromString(bytes([0x18, 7]))
    raw = discovery_pb2.LifecycleBounds()
    raw.host_graceful_shutdown.CopyFrom(later)
    assert raw.HasField("host_graceful_shutdown")
    assert shutdown(raw).kind is GracefulShutdownBoundKind.UNAVAILABLE


def test_graceful_shutdown_bound_keeps_its_cases_consistent() -> None:
    with pytest.raises(ValueError, match="exactly when kind is FINITE"):
        GracefulShutdownBound(kind=GracefulShutdownBoundKind.FINITE)
    with pytest.raises(ValueError, match="exactly when kind is FINITE"):
        GracefulShutdownBound(
            kind=GracefulShutdownBoundKind.UNBOUNDED, duration=timedelta(seconds=1)
        )
    with pytest.raises(ValueError, match="positive"):
        GracefulShutdownBound(
            kind=GracefulShutdownBoundKind.FINITE, duration=timedelta(0)
        )


@pytest.mark.parametrize(
    ("wire", "expected"),
    [
        (
            discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_UNSPECIFIED,
            ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN,
        ),
        (
            discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_UNCHANGED,
            ConfiguredSpatialAnalyzerInteractionMode.UNCHANGED,
        ),
        (
            discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_SILENT,
            ConfiguredSpatialAnalyzerInteractionMode.SILENT,
        ),
        (
            discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_AUTOMATIC,
            ConfiguredSpatialAnalyzerInteractionMode.AUTOMATIC,
        ),
        (
            discovery_pb2.CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_MANUAL,
            ConfiguredSpatialAnalyzerInteractionMode.MANUAL,
        ),
        (99, ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN),
        (-1, ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN),
    ],
)
def test_the_configured_interaction_mode_maps_by_name(
    wire: int, expected: ConfiguredSpatialAnalyzerInteractionMode
) -> None:
    snapshot = map_snapshot(server_info(mode=wire), capabilities())
    assert snapshot.configured_interaction_mode is expected


def test_the_mode_enum_covers_every_wire_name_and_unknown_replaces_unspecified() -> (
    None
):
    wire = descriptor_pool.Default().FindEnumTypeByName(  # type: ignore[no-untyped-call]
        "briosa.ConfiguredSpatialAnalyzerInteractionMode"
    )
    prefix = "CONFIGURED_SPATIAL_ANALYZER_INTERACTION_MODE_"
    names = [value.name.removeprefix(prefix) for value in wire.values]
    assert names[0] == "UNSPECIFIED"
    assert [member.name for member in ConfiguredSpatialAnalyzerInteractionMode] == [
        "UNKNOWN",
        *names[1:],
    ]


def test_fallback_is_per_purpose_not_per_reply() -> None:
    raw = discovery_pb2.LifecycleBounds(startup_with_launch_milliseconds=300_000)
    snapshot = map_snapshot(server_info(raw, mode=42), capabilities())
    bounds = snapshot.lifecycle_bounds
    assert bounds is not None
    assert (
        snapshot.configured_interaction_mode
        is ConfiguredSpatialAnalyzerInteractionMode.UNKNOWN
    )
    assert bounds.host_graceful_shutdown.kind is GracefulShutdownBoundKind.UNAVAILABLE
    assert bounds.startup_with_launch == timedelta(seconds=300)
