"""Handwritten Wave B MP operations."""
# ruff: noqa: B008, E501, F405  # Immutable MP defaults and exported public names are intentional.

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import Protocol, cast

from briosa.operation_models import *  # noqa: F403
from briosa.operation_values import *  # noqa: F403
from briosa.wave_b_operation_models import *  # noqa: F403
from briosa.wave_b_operation_values import *  # noqa: F403


class _WaveBClient(Protocol):
    async def _invoke_mp_operation(
        self,
        service: str,
        rpc: str,
        operation_id: str,
        values: dict[str, object],
        result_type: type[object] | None,
    ) -> object: ...


class WaveBOperationsMixin(_WaveBClient):
    async def cloud_display_control(
        self,
        *,
        thin_draw_increment: int = 1,
        point_size: int = 1,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "CloudDisplayControl",
            "cloud_and_mesh_operations.cloud_display_control",
            {
                "thin_draw_increment": thin_draw_increment,
                "point_size": point_size,
            },
            None,
        )
        return None

    async def reset_cloud_bounding_box(
        self,
        cloud_name: CollectionObjectName,
        *,
        cloud_box_type: CloudBoxType = CloudBoxType.WORLD_AXIS_ALIGNED_BOX,
        show_bounding_box: bool = True,
        use_all_points: bool = False,
        desired_point_count: int = 1000,
    ) -> ResetCloudBoundingBoxResult:
        return cast(
            ResetCloudBoundingBoxResult,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "ResetCloudBoundingBox",
                "cloud_and_mesh_operations.reset_cloud_bounding_box",
                {
                    "cloud_name": cloud_name,
                    "cloud_box_type": cloud_box_type,
                    "show_bounding_box": show_bounding_box,
                    "use_all_points": use_all_points,
                    "desired_point_count": desired_point_count,
                },
                ResetCloudBoundingBoxResult,
            ),
        )

    async def get_cloud_point_count(
        self,
        cloud_name: CollectionObjectName,
    ) -> GetCloudPointCountResult:
        return cast(
            GetCloudPointCountResult,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "GetCloudPointCount",
                "cloud_and_mesh_operations.get_cloud_point_count",
                {
                    "cloud_name": cloud_name,
                },
                GetCloudPointCountResult,
            ),
        )

    async def set_cloud_default_clipping_plane(
        self,
        *,
        enable_cloud_clipping: bool = False,
        reference_object: CollectionObjectName | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "SetCloudDefaultClippingPlane",
            "cloud_and_mesh_operations.set_cloud_default_clipping_plane",
            {
                "enable_cloud_clipping": enable_cloud_clipping,
                "reference_object": reference_object,
            },
            None,
        )
        return None

    async def raster_scan_edge_inspection(
        self,
        cloud_names: Iterable[CollectionObjectName],
        edge_surface_name: CollectionObjectName,
        b_spline_edge_list: Iterable[CollectionObjectName],
        prefix_for_output_groups: CollectionObjectName,
        *,
        tolerance: float = 0.0,
        minimum_good_points_per_unit_length: int = 0,
        maximum_bad_points_percentage: float = 0.0,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "RasterScanEdgeInspection",
                "cloud_and_mesh_operations.raster_scan_edge_inspection",
                {
                    "cloud_names": cloud_names,
                    "edge_surface_name": edge_surface_name,
                    "b_spline_edge_list": b_spline_edge_list,
                    "prefix_for_output_groups": prefix_for_output_groups,
                    "tolerance": tolerance,
                    "minimum_good_points_per_unit_length": minimum_good_points_per_unit_length,
                    "maximum_bad_points_percentage": maximum_bad_points_percentage,
                },
                None,
            ),
        )

    async def new_raster_scan_edge_inspection(
        self,
        edge_cloud_names: Iterable[CollectionObjectName],
        edge_surface_name: CollectionObjectName,
        edge_b_spline_name: CollectionObjectName,
        output_prefix: CollectionObjectName,
        *,
        inspection_increment: float = 0.0,
        proximity_filter_distance: float = 0.0,
        edge_bias_value: float = 0.0,
        error_tolerance: float = 0.0,
        use_cosine_projection_method: bool = False,
        minimum_edge_points_per_segment: int = 0,
        intermediate_calculation_results_file: FileReference | None = None,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "NewRasterScanEdgeInspection",
                "cloud_and_mesh_operations.new_raster_scan_edge_inspection",
                {
                    "edge_cloud_names": edge_cloud_names,
                    "edge_surface_name": edge_surface_name,
                    "edge_b_spline_name": edge_b_spline_name,
                    "output_prefix": output_prefix,
                    "inspection_increment": inspection_increment,
                    "proximity_filter_distance": proximity_filter_distance,
                    "edge_bias_value": edge_bias_value,
                    "error_tolerance": error_tolerance,
                    "use_cosine_projection_method": use_cosine_projection_method,
                    "minimum_edge_points_per_segment": minimum_edge_points_per_segment,
                    "intermediate_calculation_results_file": intermediate_calculation_results_file,
                },
                None,
            ),
        )

    async def clear_cloud_point_deviations(
        self,
        cloud_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "ClearCloudPointDeviations",
            "cloud_and_mesh_operations.clear_cloud_point_deviations",
            {
                "cloud_name": cloud_name,
            },
            None,
        )
        return None

    async def enable_all_cloud_cross_sections(
        self,
        cross_section_cloud_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "EnableAllCloudCrossSections",
            "cloud_and_mesh_operations.enable_all_cloud_cross_sections",
            {
                "cross_section_cloud_name": cross_section_cloud_name,
            },
            None,
        )
        return None

    async def enable_disable_cloud_cross_sections(
        self,
        cross_section_cloud_name: CollectionObjectName,
        *,
        cross_section_id: int = 0,
        enable: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "EnableDisableCloudCrossSections",
            "cloud_and_mesh_operations.enable_disable_cloud_cross_sections",
            {
                "cross_section_cloud_name": cross_section_cloud_name,
                "cross_section_id": cross_section_id,
                "enable": enable,
            },
            None,
        )
        return None

    async def enable_single_cloud_cross_section(
        self,
        cross_section_cloud_name: CollectionObjectName,
        *,
        cross_section_id: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "EnableSingleCloudCrossSection",
            "cloud_and_mesh_operations.enable_single_cloud_cross_section",
            {
                "cross_section_cloud_name": cross_section_cloud_name,
                "cross_section_id": cross_section_id,
            },
            None,
        )
        return None

    async def get_number_of_cross_sections_in_cross_section_cloud(
        self,
        cross_section_cloud_name: CollectionObjectName,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "GetNumberOfCrossSectionsInCrossSectionCloud",
                "cloud_and_mesh_operations.get_number_of_cross_sections_in_cross_section_cloud",
                {
                    "cross_section_cloud_name": cross_section_cloud_name,
                },
                None,
            ),
        )

    async def filter_clouds_to_plane(
        self,
        cloud_names: Iterable[CollectionObjectName],
        filter_plane_name: CollectionObjectName,
        output_group_name: CollectionObjectName,
        *,
        proximity: float = 0.0,
        allowable_offset_direction: OffsetDirectionType = OffsetDirectionType.BOTH,
        output_type: PointOutputType = PointOutputType.POINTS,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToPlane",
            "cloud_and_mesh_operations.filter_clouds_to_plane",
            {
                "cloud_names": cloud_names,
                "filter_plane_name": filter_plane_name,
                "output_group_name": output_group_name,
                "proximity": proximity,
                "allowable_offset_direction": allowable_offset_direction,
                "output_type": output_type,
            },
            None,
        )
        return None

    async def filter_clouds_to_group(
        self,
        cloud_names: Iterable[CollectionObjectName],
        filter_group_name: CollectionObjectName,
        output_group_name: CollectionObjectName,
        *,
        proximity: float = 0.0,
        maximum_number_of_points: int = 0,
        output_type: PointOutputType = PointOutputType.POINTS,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToGroup",
            "cloud_and_mesh_operations.filter_clouds_to_group",
            {
                "cloud_names": cloud_names,
                "filter_group_name": filter_group_name,
                "output_group_name": output_group_name,
                "proximity": proximity,
                "maximum_number_of_points": maximum_number_of_points,
                "output_type": output_type,
            },
            None,
        )
        return None

    async def filter_clouds_to_surface(
        self,
        cloud_names: Iterable[CollectionObjectName],
        filter_surface_name: CollectionObjectName,
        output_group_name: CollectionObjectName,
        *,
        low_proximity: float = 0.0,
        high_proximity: float = 0.0,
        skip_factor: int = 0,
        output_type: PointOutputType = PointOutputType.POINTS,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToSurface",
            "cloud_and_mesh_operations.filter_clouds_to_surface",
            {
                "cloud_names": cloud_names,
                "filter_surface_name": filter_surface_name,
                "output_group_name": output_group_name,
                "low_proximity": low_proximity,
                "high_proximity": high_proximity,
                "skip_factor": skip_factor,
                "output_type": output_type,
            },
            None,
        )
        return None

    async def filter_clouds_to_bsplines(
        self,
        cloud_names: Iterable[CollectionObjectName],
        filter_b_spline_names: Iterable[CollectionObjectName],
        output_group_name: CollectionObjectName,
        *,
        minimum_proximity: float = 0.0,
        maximum_proximity: float = 0.0,
        output_type: PointOutputType = PointOutputType.POINTS,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToBSplines",
            "cloud_and_mesh_operations.filter_clouds_to_bsplines",
            {
                "cloud_names": cloud_names,
                "filter_b_spline_names": filter_b_spline_names,
                "output_group_name": output_group_name,
                "minimum_proximity": minimum_proximity,
                "maximum_proximity": maximum_proximity,
                "output_type": output_type,
            },
            None,
        )
        return None

    async def filter_clouds_to_line_segment(
        self,
        cloud_names: Iterable[CollectionObjectName],
        first_line_end_point: PointName,
        second_line_end_point: PointName,
        output_group_name: CollectionObjectName,
        *,
        minimum_proximity: float = 0.0,
        maximum_proximity: float = 0.0,
        output_type: PointOutputType = PointOutputType.POINTS,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToLineSegment",
            "cloud_and_mesh_operations.filter_clouds_to_line_segment",
            {
                "cloud_names": cloud_names,
                "first_line_end_point": first_line_end_point,
                "second_line_end_point": second_line_end_point,
                "output_group_name": output_group_name,
                "minimum_proximity": minimum_proximity,
                "maximum_proximity": maximum_proximity,
                "output_type": output_type,
            },
            None,
        )
        return None

    async def filter_clouds_to_vector_groups_resolve_points(
        self,
        cloud_names: Iterable[CollectionObjectName],
        vector_group_names: Iterable[CollectionObjectName],
        output_group_name: CollectionObjectName,
        *,
        minimum_proximity: float = 0.0,
        maximum_proximity: float = 0.0,
        maximum_distance_from_vector_begin: float = 0.0,
        minimum_number_of_required_points: int = 0,
        output_type: PointOutputType = PointOutputType.POINTS,
        include_proximity_points: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "FilterCloudsToVectorGroupsResolvePoints",
            "cloud_and_mesh_operations.filter_clouds_to_vector_groups_resolve_points",
            {
                "cloud_names": cloud_names,
                "vector_group_names": vector_group_names,
                "output_group_name": output_group_name,
                "minimum_proximity": minimum_proximity,
                "maximum_proximity": maximum_proximity,
                "maximum_distance_from_vector_begin": maximum_distance_from_vector_begin,
                "minimum_number_of_required_points": minimum_number_of_required_points,
                "output_type": output_type,
                "include_proximity_points": include_proximity_points,
            },
            None,
        )
        return None

    async def filter_clouds_to_vector_groups_resolve_clouds(
        self,
        cloud_names: Iterable[CollectionObjectName],
        vector_group_names: Iterable[CollectionObjectName],
        output_collection_name: str,
        *,
        radial_cutoff: float = 0.1,
        lower_cutoff: float = -0.1,
        upper_cutoff: float = 0.1,
    ) -> tuple[CollectionObjectName, ...]:
        return cast(
            tuple[CollectionObjectName, ...],
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "FilterCloudsToVectorGroupsResolveClouds",
                "cloud_and_mesh_operations.filter_clouds_to_vector_groups_resolve_clouds",
                {
                    "cloud_names": cloud_names,
                    "vector_group_names": vector_group_names,
                    "radial_cutoff": radial_cutoff,
                    "lower_cutoff": lower_cutoff,
                    "upper_cutoff": upper_cutoff,
                    "output_collection_name": output_collection_name,
                },
                None,
            ),
        )

    async def rgb_cloud_point_filter(
        self,
        clouds_to_be_filtered: Iterable[CollectionObjectName],
        *,
        filter_name: str = "Default Filter",
        red_enabled: bool = True,
        red_high_enabled: bool = False,
        red_high_threshold: int = 255,
        red_low_enabled: bool = False,
        red_low_threshold: int = 0,
        green_enabled: bool = True,
        green_high_enabled: bool = False,
        green_high_threshold: int = 255,
        green_low_enabled: bool = False,
        green_low_threshold: int = 0,
        blue_enabled: bool = True,
        blue_high_enabled: bool = False,
        blue_high_threshold: int = 255,
        blue_low_enabled: bool = False,
        blue_low_threshold: int = 0,
        gray_scale_enabled: bool = False,
        gray_scale_high_enabled: bool = False,
        gray_scale_high_threshold: int = 255,
        gray_scale_low_enabled: bool = False,
        gray_scale_low_threshold: int = 0,
        rgb_filter_operation: RGBFilterOperation = RGBFilterOperation.RESET_AND_APPLY_FILTER,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "RGBCloudPointFilter",
            "cloud_and_mesh_operations.rgb_cloud_point_filter",
            {
                "filter_name": filter_name,
                "clouds_to_be_filtered": clouds_to_be_filtered,
                "red_enabled": red_enabled,
                "red_high_enabled": red_high_enabled,
                "red_high_threshold": red_high_threshold,
                "red_low_enabled": red_low_enabled,
                "red_low_threshold": red_low_threshold,
                "green_enabled": green_enabled,
                "green_high_enabled": green_high_enabled,
                "green_high_threshold": green_high_threshold,
                "green_low_enabled": green_low_enabled,
                "green_low_threshold": green_low_threshold,
                "blue_enabled": blue_enabled,
                "blue_high_enabled": blue_high_enabled,
                "blue_high_threshold": blue_high_threshold,
                "blue_low_enabled": blue_low_enabled,
                "blue_low_threshold": blue_low_threshold,
                "gray_scale_enabled": gray_scale_enabled,
                "gray_scale_high_enabled": gray_scale_high_enabled,
                "gray_scale_high_threshold": gray_scale_high_threshold,
                "gray_scale_low_enabled": gray_scale_low_enabled,
                "gray_scale_low_threshold": gray_scale_low_threshold,
                "rgb_filter_operation": rgb_filter_operation,
            },
            None,
        )
        return None

    async def get_cloud_rgb_values(
        self,
        source_cloud_name: CollectionObjectName,
        *,
        rgb_color_channel: RGBColorChannel = RGBColorChannel.INTENSITY,
    ) -> GetCloudRGBValuesResult:
        return cast(
            GetCloudRGBValuesResult,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "GetCloudRGBValues",
                "cloud_and_mesh_operations.get_cloud_rgb_values",
                {
                    "source_cloud_name": source_cloud_name,
                    "rgb_color_channel": rgb_color_channel,
                },
                GetCloudRGBValuesResult,
            ),
        )

    async def get_cloud_rgb_values_near_point(
        self,
        source_cloud_name: CollectionObjectName,
        single_point: PointName,
        *,
        diameter: float = 10.0,
        rgb_color_channel: RGBColorChannel = RGBColorChannel.INTENSITY,
    ) -> GetCloudRGBValuesNearPointResult:
        return cast(
            GetCloudRGBValuesNearPointResult,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "GetCloudRGBValuesNearPoint",
                "cloud_and_mesh_operations.get_cloud_rgb_values_near_point",
                {
                    "source_cloud_name": source_cloud_name,
                    "single_point": single_point,
                    "diameter": diameter,
                    "rgb_color_channel": rgb_color_channel,
                },
                GetCloudRGBValuesNearPointResult,
            ),
        )

    async def subdivide_cloud_by_point_spacing(
        self,
        source_cloud_name: CollectionObjectName,
        new_cloud_name: CollectionObjectName,
        *,
        point_spacing: float = 0.0,
        minimum_points_per_group: int = 0,
        keep_all_groups: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "SubdivideCloudByPointSpacing",
            "cloud_and_mesh_operations.subdivide_cloud_by_point_spacing",
            {
                "source_cloud_name": source_cloud_name,
                "point_spacing": point_spacing,
                "minimum_points_per_group": minimum_points_per_group,
                "new_cloud_name": new_cloud_name,
                "keep_all_groups": keep_all_groups,
            },
            None,
        )
        return None

    async def delete_cloud_points_by_radial_distance_from_points(
        self,
        cloud_names: Iterable[CollectionObjectName],
        points: Iterable[PointName],
        *,
        radius: float = 0.0,
        delete_inside: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "DeleteCloudPointsByRadialDistanceFromPoints",
            "cloud_and_mesh_operations.delete_cloud_points_by_radial_distance_from_points",
            {
                "cloud_names": cloud_names,
                "points": points,
                "radius": radius,
                "delete_inside": delete_inside,
            },
            None,
        )
        return None

    async def delete_cloud_points_by_x_y_z_range(
        self,
        cloud_names: Iterable[CollectionObjectName],
        *,
        x_min: float | None = None,
        x_max: float | None = None,
        y_min: float | None = None,
        y_max: float | None = None,
        z_min: float | None = None,
        z_max: float | None = None,
        delete_inside: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "DeleteCloudPointsByXYZRange",
            "cloud_and_mesh_operations.delete_cloud_points_by_xyz_range",
            {
                "cloud_names": cloud_names,
                "x_min": x_min,
                "x_max": x_max,
                "y_min": y_min,
                "y_max": y_max,
                "z_min": z_min,
                "z_max": z_max,
                "delete_inside": delete_inside,
            },
            None,
        )
        return None

    async def generate_general_mesh(
        self,
        output_mesh_name: CollectionObjectName,
        clouds_to_mesh: Iterable[CollectionObjectName],
        *,
        maximum_triangle_size: float = 0.05,
        smallest_hole_diameter: float = 0.25,
        finalize: bool = True,
        use_scan_direction_for_point_normal: bool = True,
        json_file: FileReference | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "GenerateGeneralMesh",
            "cloud_and_mesh_operations.generate_general_mesh",
            {
                "output_mesh_name": output_mesh_name,
                "clouds_to_mesh": clouds_to_mesh,
                "maximum_triangle_size": maximum_triangle_size,
                "smallest_hole_diameter": smallest_hole_diameter,
                "finalize": finalize,
                "use_scan_direction_for_point_normal": use_scan_direction_for_point_normal,
                "json_file": json_file,
            },
            None,
        )
        return None

    async def consolidate_mesh(
        self,
        mesh: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "ConsolidateMesh",
            "cloud_and_mesh_operations.consolidate_mesh",
            {
                "mesh": mesh,
            },
            None,
        )
        return None

    async def mesh_volume(
        self,
        mesh: CollectionObjectName,
        plane: CollectionObjectName,
    ) -> MeshVolumeResult:
        return cast(
            MeshVolumeResult,
            await self._invoke_mp_operation(
                "briosa.CloudAndMeshOperations",
                "MeshVolume",
                "cloud_and_mesh_operations.mesh_volume",
                {
                    "mesh": mesh,
                    "plane": plane,
                },
                MeshVolumeResult,
            ),
        )

    async def mesh_fill_holes(
        self,
        mesh: CollectionObjectName,
        *,
        maximum_triangle_length: float = -1.0,
        tension: float = 0.0,
        unconditional_filling: bool = False,
        fill_all_holes: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.CloudAndMeshOperations",
            "MeshFillHoles",
            "cloud_and_mesh_operations.mesh_fill_holes",
            {
                "mesh": mesh,
                "maximum_triangle_length": maximum_triangle_length,
                "tension": tension,
                "unconditional_filling": unconditional_filling,
                "fill_all_holes": fill_all_holes,
            },
            None,
        )
        return None

    async def copy_object(
        self,
        source_object: CollectionObjectName,
        new_object_name: CollectionObjectName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CopyObject",
            "construction_operations.copy_object",
            {
                "source_object": source_object,
                "new_object_name": new_object_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def copy_objects_point_to_point_delta(
        self,
        objects_to_copy: Iterable[CollectionObjectName],
        first_delta_point: PointName,
        second_delta_point: PointName,
        *,
        destination_collection_name: CollectionName | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CopyObjectsPointToPointDelta",
            "construction_operations.copy_objects_point_to_point_delta",
            {
                "objects_to_copy": objects_to_copy,
                "first_delta_point": first_delta_point,
                "second_delta_point": second_delta_point,
                "destination_collection_name": destination_collection_name,
            },
            None,
        )
        return None

    async def copy_objects_to_a_collection(
        self,
        source_objects: Iterable[CollectionObjectName],
        destination_collection_name: CollectionName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CopyObjectsToACollection",
            "construction_operations.copy_objects_to_a_collection",
            {
                "source_objects": source_objects,
                "destination_collection_name": destination_collection_name,
            },
            None,
        )
        return None

    async def delete_points(
        self,
        point_names: Iterable[PointName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "DeletePoints",
            "construction_operations.delete_points",
            {
                "point_names": point_names,
            },
            None,
        )
        return None

    async def delete_points_wildcard_selection(
        self,
        groups_to_delete_from: Iterable[CollectionObjectName],
        wildcard_selection_names: PointName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "DeletePointsWildcardSelection",
            "construction_operations.delete_points_wildcard_selection",
            {
                "groups_to_delete_from": groups_to_delete_from,
                "wildcard_selection_names": wildcard_selection_names,
            },
            None,
        )
        return None

    async def mirror_objects(
        self,
        objects: Iterable[CollectionObjectName],
        frame_name: CollectionObjectName,
        frame_plane_to_mirror_around: MirrorFramePlane,
        *,
        copy: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "MirrorObjects",
            "construction_operations.mirror_objects",
            {
                "objects": objects,
                "frame_name": frame_name,
                "frame_plane_to_mirror_around": frame_plane_to_mirror_around,
                "copy": copy,
            },
            None,
        )
        return None

    async def move_objects_point_to_point_delta(
        self,
        objects_to_move: Iterable[CollectionObjectName],
        first_delta_point: PointName,
        second_delta_point: PointName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "MoveObjectsPointToPointDelta",
            "construction_operations.move_objects_point_to_point_delta",
            {
                "objects_to_move": objects_to_move,
                "first_delta_point": first_delta_point,
                "second_delta_point": second_delta_point,
            },
            None,
        )
        return None

    async def move_objects_to_a_collection(
        self,
        source_objects: Iterable[CollectionObjectName],
        destination_collection_name: CollectionName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "MoveObjectsToACollection",
            "construction_operations.move_objects_to_a_collection",
            {
                "source_objects": source_objects,
                "destination_collection_name": destination_collection_name,
            },
            None,
        )
        return None

    async def rename_collection(
        self,
        original_collection_name: CollectionName,
        new_collection_name: CollectionName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenameCollection",
            "construction_operations.rename_collection",
            {
                "original_collection_name": original_collection_name,
                "new_collection_name": new_collection_name,
            },
            None,
        )
        return None

    async def rename_item(
        self,
        original_item_name: CollectionItemName,
        new_item_name: CollectionItemName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenameItem",
            "construction_operations.rename_item",
            {
                "original_item_name": original_item_name,
                "new_item_name": new_item_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def rename_object(
        self,
        original_object_name: CollectionObjectName,
        new_object_name: CollectionObjectName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenameObject",
            "construction_operations.rename_object",
            {
                "original_object_name": original_object_name,
                "new_object_name": new_object_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def rename_point(
        self,
        original_point_name: PointName,
        new_point_name: PointName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenamePoint",
            "construction_operations.rename_point",
            {
                "original_point_name": original_point_name,
                "new_point_name": new_point_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def rename_points_with_name_pattern(
        self,
        point_names: Iterable[PointName],
        *,
        name_pattern: str = "NewName_%d",
        start_value: int = 1,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenamePointsWithNamePattern",
            "construction_operations.rename_points_with_name_pattern",
            {
                "point_names": point_names,
                "name_pattern": name_pattern,
                "start_value": start_value,
            },
            None,
        )
        return None

    async def construct_objects_from_surface_faces_runtime_select(
        self,
        object_type: ConstructObjectType,
        *,
        point_offset: float = 0.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructObjectsFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_objects_from_surface_faces_runtime_select",
            {
                "object_type": object_type,
                "point_offset": point_offset,
            },
            None,
        )
        return None

    async def auto_filter_clouds_to_nominal_geometry_2d(
        self,
        auto_filter_target_relationships: Iterable[CollectionItemName],
        clouds: Iterable[CollectionObjectName],
        *,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        filter_proximity_settings_2d: FilterProximitySettings | None = None,
        geometry_extraction_tolerance: float = 0.01,
        use_feature_specific_filter_settings: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "AutoFilterCloudsToNominalGeometry2D",
            "relationship_operations.auto_filter_clouds_to_nominal_geometry_2d",
            {
                "auto_filter_target_relationships": auto_filter_target_relationships,
                "clouds": clouds,
                "cloud_thinning_settings": cloud_thinning_settings,
                "filter_proximity_settings_2d": filter_proximity_settings_2d,
                "geometry_extraction_tolerance": geometry_extraction_tolerance,
                "use_feature_specific_filter_settings": use_feature_specific_filter_settings,
            },
            None,
        )
        return None

    async def auto_filter_clouds_to_nominal_geometry_3d(
        self,
        auto_filter_target_relationships: Iterable[CollectionItemName],
        clouds: Iterable[CollectionObjectName],
        *,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        filter_proximity_settings_3d: FilterProximitySettings | None = None,
        use_feature_specific_filter_settings: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "AutoFilterCloudsToNominalGeometry3D",
            "relationship_operations.auto_filter_clouds_to_nominal_geometry_3d",
            {
                "auto_filter_target_relationships": auto_filter_target_relationships,
                "clouds": clouds,
                "cloud_thinning_settings": cloud_thinning_settings,
                "filter_proximity_settings_3d": filter_proximity_settings_3d,
                "use_feature_specific_filter_settings": use_feature_specific_filter_settings,
            },
            None,
        )
        return None

    async def auto_filter_points_groups_clouds_to_surface_faces(
        self,
        surfaces: Iterable[CollectionObjectName],
        *,
        points: Iterable[PointName] | None = None,
        groups: Iterable[CollectionObjectName] | None = None,
        clouds: Iterable[CollectionObjectName] | None = None,
        surface_offset: float = 0.1,
        edge_offset: float = 0.1,
        offset_direction: OffsetDirectionType = OffsetDirectionType.BOTH,
        enforce_max_points_per_face_in_output: bool = False,
        max_points_per_face: int = 0,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        output_cloud_base_name: str = "InspAutoFilteredCloud",
        use_face_ids_for_suffix: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "AutoFilterPointsGroupsCloudsToSurfaceFaces",
            "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
            {
                "points": points,
                "groups": groups,
                "clouds": clouds,
                "surface_offset": surface_offset,
                "edge_offset": edge_offset,
                "offset_direction": offset_direction,
                "enforce_max_points_per_face_in_output": enforce_max_points_per_face_in_output,
                "max_points_per_face": max_points_per_face,
                "surfaces": surfaces,
                "cloud_thinning_settings": cloud_thinning_settings,
                "output_cloud_base_name": output_cloud_base_name,
                "use_face_ids_for_suffix": use_face_ids_for_suffix,
            },
            None,
        )
        return None

    async def auto_filter_points_to_nominal_geometry_3d(
        self,
        auto_filter_target_relationships: Iterable[CollectionItemName],
        points: Iterable[PointName],
        *,
        filter_proximity_settings_3d: FilterProximitySettings | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "AutoFilterPointsToNominalGeometry3D",
            "relationship_operations.auto_filter_points_to_nominal_geometry_3d",
            {
                "auto_filter_target_relationships": auto_filter_target_relationships,
                "points": points,
                "filter_proximity_settings_3d": filter_proximity_settings_3d,
            },
            None,
        )
        return None

    async def compute_geometry_relationship_uncertainties(
        self,
        relationship_name: CollectionItemName,
        *,
        display_results: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "ComputeGeometryRelationshipUncertainties",
            "relationship_operations.compute_geometry_relationship_uncertainties",
            {
                "relationship_name": relationship_name,
                "display_results": display_results,
            },
            None,
        )
        return None

    async def create_points_to_objects_map(
        self,
        points_to_objects_map_name: str,
        objects: Iterable[CollectionObjectName],
        *,
        points: Iterable[PointName] | None = None,
        groups: Iterable[CollectionObjectName] | None = None,
        proximity_tolerance: float = 0.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "CreatePointsToObjectsMap",
            "relationship_operations.create_points_to_objects_map",
            {
                "points": points,
                "groups": groups,
                "objects": objects,
                "proximity_tolerance": proximity_tolerance,
                "points_to_objects_map_name": points_to_objects_map_name,
            },
            None,
        )
        return None

    async def delete_relationship(
        self,
        relationship_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "DeleteRelationship",
            "relationship_operations.delete_relationship",
            {
                "relationship_name": relationship_name,
            },
            None,
        )
        return None

    async def do_relationship_fit(
        self,
        collection_containing_relationships: str,
        objects_to_move: Iterable[CollectionObjectName],
        instruments_to_move: Iterable[CollectionInstrumentId],
        *,
        solver_mode: SolverMode = SolverMode.GAUSS_NEWTON,
        motion_to_allow: FitDofOptions | None = None,
        enable_randomized_start: bool = False,
        use_fit_dialog: bool = False,
    ) -> RelationshipFitResult:
        return cast(
            RelationshipFitResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "DoRelationshipFit",
                "relationship_operations.do_relationship_fit",
                {
                    "collection_containing_relationships": collection_containing_relationships,
                    "objects_to_move": objects_to_move,
                    "instruments_to_move": instruments_to_move,
                    "solver_mode": solver_mode,
                    "motion_to_allow": motion_to_allow,
                    "enable_randomized_start": enable_randomized_start,
                    "use_fit_dialog": use_fit_dialog,
                },
                RelationshipFitResult,
            ),
        )

    async def extract_geometry_from_point_clouds(
        self,
        relationship_name: CollectionItemName,
        cloud_name: CollectionObjectName,
        seed_points: Iterable[PointName],
        *,
        geometry_type: GeometryType = GeometryType.CIRCLE,
        bounding_points: Iterable[PointName] | None = None,
        tolerance: float = 0.1,
        reverse_normal: bool = False,
        planar_point_count: int = 1000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "ExtractGeometryFromPointClouds",
            "relationship_operations.extract_geometry_from_point_clouds",
            {
                "relationship_name": relationship_name,
                "geometry_type": geometry_type,
                "cloud_name": cloud_name,
                "bounding_points": bounding_points,
                "seed_points": seed_points,
                "tolerance": tolerance,
                "reverse_normal": reverse_normal,
                "planar_point_count": planar_point_count,
            },
            None,
        )
        return None

    async def filter_geometry_relationship_outlier_cloud_points(
        self,
        relationship_name: CollectionObjectName,
        *,
        sigma_threshold: float = 3.0,
        modify_existing_input_clouds: bool = False,
    ) -> GeometryRelationshipOutlierFilterMetrics:
        return cast(
            GeometryRelationshipOutlierFilterMetrics,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "FilterGeometryRelationshipOutlierCloudPoints",
                "relationship_operations.filter_geometry_relationship_outlier_cloud_points",
                {
                    "relationship_name": relationship_name,
                    "sigma_threshold": sigma_threshold,
                    "modify_existing_input_clouds": modify_existing_input_clouds,
                },
                None,
            ),
        )

    async def generate_geometry_relationship_summary(
        self,
        relationship_ref_list: Iterable[CollectionItemName],
        *,
        summary_table_name: str = "Geometry Relationship Summary",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "GenerateGeometryRelationshipSummary",
            "relationship_operations.generate_geometry_relationship_summary",
            {
                "relationship_ref_list": relationship_ref_list,
                "summary_table_name": summary_table_name,
            },
            None,
        )
        return None

    async def get_general_relationship_statistics(
        self,
        relationship_name: CollectionObjectName,
    ) -> GeneralRelationshipStatistics:
        return cast(
            GeneralRelationshipStatistics,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeneralRelationshipStatistics",
                "relationship_operations.get_general_relationship_statistics",
                {
                    "relationship_name": relationship_name,
                },
                GeneralRelationshipStatistics,
            ),
        )

    async def get_geom_relationship_criteria_name_list(
        self,
        relationship_name: CollectionItemName,
        *,
        include_all_criteria: bool = False,
    ) -> tuple[str, ...]:
        return cast(
            tuple[str, ...],
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipCriteriaNameList",
                "relationship_operations.get_geom_relationship_criteria_name_list",
                {
                    "relationship_name": relationship_name,
                    "include_all_criteria": include_all_criteria,
                },
                None,
            ),
        )

    async def get_objects_from_points_to_objects_map_point_list(
        self,
        points_to_objects_map_name: str,
        points: Iterable[PointName],
    ) -> tuple[CollectionObjectName, ...]:
        return cast(
            tuple[CollectionObjectName, ...],
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetObjectsFromPointsToObjectsMapPointList",
                "relationship_operations.get_objects_from_points_to_objects_map_point_list",
                {
                    "points_to_objects_map_name": points_to_objects_map_name,
                    "points": points,
                },
                None,
            ),
        )

    async def get_point_to_point_relationship_statistics(
        self,
        relationship_name: CollectionObjectName,
    ) -> PointToPointRelationshipStatistics:
        return cast(
            PointToPointRelationshipStatistics,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPointToPointRelationshipStatistics",
                "relationship_operations.get_point_to_point_relationship_statistics",
                {
                    "relationship_name": relationship_name,
                },
                PointToPointRelationshipStatistics,
            ),
        )

    async def get_points_to_objects_relationship_statistics(
        self,
        relationship_name: CollectionObjectName,
    ) -> PointsToObjectsRelationshipStatistics:
        return cast(
            PointsToObjectsRelationshipStatistics,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPointsToObjectsRelationshipStatistics",
                "relationship_operations.get_points_to_objects_relationship_statistics",
                {
                    "relationship_name": relationship_name,
                },
                PointsToObjectsRelationshipStatistics,
            ),
        )

    async def get_points_to_points_relationship_associated_data(
        self,
        relationship_name: CollectionItemName,
    ) -> PointsToPointsRelationshipAssociatedData:
        return cast(
            PointsToPointsRelationshipAssociatedData,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPointsToPointsRelationshipAssociatedData",
                "relationship_operations.get_points_to_points_relationship_associated_data",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_relationship_associated_data(
        self,
        relationship_name: CollectionItemName,
    ) -> RelationshipAssociatedData:
        return cast(
            RelationshipAssociatedData,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipAssociatedData",
                "relationship_operations.get_relationship_associated_data",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_relationship_status(
        self,
        relationship_name: CollectionItemName,
    ) -> RelationshipStatusFlags:
        return cast(
            RelationshipStatusFlags,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipStatus",
                "relationship_operations.get_relationship_status",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def make_average_point_relationship(
        self,
        relationship_name: CollectionObjectName,
        points_in_relationship: Iterable[PointName],
        *,
        average_point_name: PointName | None = None,
        nominal_point_name: PointName | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeAveragePointRelationship",
            "relationship_operations.make_average_point_relationship",
            {
                "relationship_name": relationship_name,
                "points_in_relationship": points_in_relationship,
                "average_point_name": average_point_name,
                "nominal_point_name": nominal_point_name,
            },
            None,
        )
        return None

    async def make_cloud_to_swatch_relationship(
        self,
        relationship_name: CollectionItemName,
        input_cloud_name: CollectionObjectName,
        surface_face_list: str,
        reference_point: PointName,
        cardinal_point_group_name: CollectionObjectName,
        *,
        maximum_radial_offset: float = 0.125,
        minimum_axial_offset: float = -0.125,
        maximum_axial_offset: float = 0.125,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeCloudToSwatchRelationship",
            "relationship_operations.make_cloud_to_swatch_relationship",
            {
                "relationship_name": relationship_name,
                "input_cloud_name": input_cloud_name,
                "surface_face_list": surface_face_list,
                "reference_point": reference_point,
                "maximum_radial_offset": maximum_radial_offset,
                "minimum_axial_offset": minimum_axial_offset,
                "maximum_axial_offset": maximum_axial_offset,
                "cardinal_point_group_name": cardinal_point_group_name,
            },
            None,
        )
        return None

    async def make_dynamic_circle_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_reference_geometry: CollectionObjectName,
        second_reference_geometry: CollectionObjectName,
        *,
        construction_mode: DynamicCircleMode = DynamicCircleMode.CYLINDER_AND_PLANE_HOLD_PLANE_NORMAL,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeDynamicCircleRelationship",
            "relationship_operations.make_dynamic_circle_relationship",
            {
                "relationship_name": relationship_name,
                "construction_mode": construction_mode,
                "first_reference_geometry": first_reference_geometry,
                "second_reference_geometry": second_reference_geometry,
            },
            None,
        )
        return None

    async def make_dynamic_ellipse_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_reference_geometry: CollectionObjectName,
        second_reference_geometry: CollectionObjectName,
        *,
        construction_mode: DynamicEllipseMode = DynamicEllipseMode.CYLINDER_AND_PLANE_INTERSECTION,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeDynamicEllipseRelationship",
            "relationship_operations.make_dynamic_ellipse_relationship",
            {
                "relationship_name": relationship_name,
                "construction_mode": construction_mode,
                "first_reference_geometry": first_reference_geometry,
                "second_reference_geometry": second_reference_geometry,
            },
            None,
        )
        return None

    async def make_dynamic_line_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_reference_geometry: CollectionObjectName,
        second_reference_geometry: CollectionObjectName,
        *,
        construction_mode: DynamicLineMode = DynamicLineMode.INTERSECTION_OF_TWO_PLANES,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeDynamicLineRelationship",
            "relationship_operations.make_dynamic_line_relationship",
            {
                "relationship_name": relationship_name,
                "construction_mode": construction_mode,
                "first_reference_geometry": first_reference_geometry,
                "second_reference_geometry": second_reference_geometry,
            },
            None,
        )
        return None

    async def make_dynamic_plane_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_reference_geometry: CollectionObjectName,
        second_reference_geometry: CollectionObjectName,
        *,
        construction_mode: DynamicPlaneMode = DynamicPlaneMode.BISECT_TWO_PLANES,
        offset_plane_offset: float = 0.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeDynamicPlaneRelationship",
            "relationship_operations.make_dynamic_plane_relationship",
            {
                "relationship_name": relationship_name,
                "construction_mode": construction_mode,
                "first_reference_geometry": first_reference_geometry,
                "second_reference_geometry": second_reference_geometry,
                "offset_plane_offset": offset_plane_offset,
            },
            None,
        )
        return None

    async def make_dynamic_point_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_reference_geometry: CollectionObjectName,
        second_reference_geometry: CollectionObjectName,
        *,
        construction_mode: DynamicPointMode = DynamicPointMode.INTERSECTION_LINE_AND_PLANE,
        third_reference_geometry: CollectionObjectName | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeDynamicPointRelationship",
            "relationship_operations.make_dynamic_point_relationship",
            {
                "relationship_name": relationship_name,
                "construction_mode": construction_mode,
                "first_reference_geometry": first_reference_geometry,
                "second_reference_geometry": second_reference_geometry,
                "third_reference_geometry": third_reference_geometry,
            },
            None,
        )
        return None

    async def make_frame_to_frame_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_frame_name: CollectionObjectName,
        second_frame_name: CollectionObjectName,
        *,
        orientation_tolerance: ToleranceScalarOptions | None = None,
        position_tolerance: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeFrameToFrameRelationship",
            "relationship_operations.make_frame_to_frame_relationship",
            {
                "relationship_name": relationship_name,
                "first_frame_name": first_frame_name,
                "second_frame_name": second_frame_name,
                "orientation_tolerance": orientation_tolerance,
                "position_tolerance": position_tolerance,
            },
            None,
        )
        return None

    async def make_geometry_compare_only_relationship(
        self,
        relationship_name: CollectionObjectName,
        nominal_geometry: CollectionObjectName,
        measured_geometry: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGeometryCompareOnlyRelationship",
            "relationship_operations.make_geometry_compare_only_relationship",
            {
                "relationship_name": relationship_name,
                "nominal_geometry": nominal_geometry,
                "measured_geometry": measured_geometry,
            },
            None,
        )
        return None

    async def make_geometry_fit_and_compare_to_nominal_relationship(
        self,
        relationship_name: CollectionObjectName,
        nominal_geometry: CollectionObjectName,
        point_groups_to_fit: Iterable[CollectionObjectName],
        *,
        resulting_object_name: CollectionObjectName | None = None,
        fit_profile_name: str | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGeometryFitAndCompareToNominalRelationship",
            "relationship_operations.make_geometry_fit_and_compare_to_nominal_relationship",
            {
                "relationship_name": relationship_name,
                "nominal_geometry": nominal_geometry,
                "point_groups_to_fit": point_groups_to_fit,
                "resulting_object_name": resulting_object_name,
                "fit_profile_name": fit_profile_name,
            },
            None,
        )
        return None

    async def make_geometry_fit_only_relationship(
        self,
        relationship_name: CollectionObjectName,
        point_groups_to_fit: Iterable[CollectionObjectName],
        geometry_type: GeometryType,
        *,
        resulting_object_name: CollectionObjectName | None = None,
        fit_profile_name: str | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGeometryFitOnlyRelationship",
            "relationship_operations.make_geometry_fit_only_relationship",
            {
                "relationship_name": relationship_name,
                "point_groups_to_fit": point_groups_to_fit,
                "geometry_type": geometry_type,
                "resulting_object_name": resulting_object_name,
                "fit_profile_name": fit_profile_name,
            },
            None,
        )
        return None

    async def make_group_to_group_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_group_name: CollectionObjectName,
        second_group_name: CollectionObjectName,
        *,
        auto_update_a_vector_group: bool = False,
        tolerance: ToleranceVectorOptions | None = None,
        constraint: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGroupToGroupRelationship",
            "relationship_operations.make_group_to_group_relationship",
            {
                "relationship_name": relationship_name,
                "first_group_name": first_group_name,
                "second_group_name": second_group_name,
                "auto_update_a_vector_group": auto_update_a_vector_group,
                "tolerance": tolerance,
                "constraint": constraint,
            },
            None,
        )
        return None

    async def make_group_to_nominal_group_relationship(
        self,
        relationship_name: CollectionObjectName,
        nominal_group_name: CollectionObjectName,
        measured_group_name: CollectionObjectName,
        *,
        auto_update_a_vector_group: bool = False,
        use_closest_point: bool = True,
        display_closest_point_watch_window: bool = False,
        use_view_zooming_with_proximity: bool = False,
        ignore_points_beyond_threshold: bool = False,
        proximity_threshold: float = 0.01,
        tolerance: ToleranceVectorOptions | None = None,
        constraint: ToleranceVectorOptions | None = None,
        fit_weight: float = 1.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGroupToNominalGroupRelationship",
            "relationship_operations.make_group_to_nominal_group_relationship",
            {
                "relationship_name": relationship_name,
                "nominal_group_name": nominal_group_name,
                "measured_group_name": measured_group_name,
                "auto_update_a_vector_group": auto_update_a_vector_group,
                "use_closest_point": use_closest_point,
                "display_closest_point_watch_window": display_closest_point_watch_window,
                "use_view_zooming_with_proximity": use_view_zooming_with_proximity,
                "ignore_points_beyond_threshold": ignore_points_beyond_threshold,
                "proximity_threshold": proximity_threshold,
                "tolerance": tolerance,
                "constraint": constraint,
                "fit_weight": fit_weight,
            },
            None,
        )
        return None

    async def make_groups_to_objects_relationship(
        self,
        relationship_name: CollectionObjectName,
        point_groups_in_relationship: Iterable[CollectionObjectName],
        objects_in_relationship: Iterable[CollectionObjectName],
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        auto_update_a_vector_group: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeGroupsToObjectsRelationship",
            "relationship_operations.make_groups_to_objects_relationship",
            {
                "relationship_name": relationship_name,
                "point_groups_in_relationship": point_groups_in_relationship,
                "objects_in_relationship": objects_in_relationship,
                "projection_options": projection_options,
                "auto_update_a_vector_group": auto_update_a_vector_group,
            },
            None,
        )
        return None

    async def make_object_to_object_direction_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_object_in_relationship: CollectionObjectName,
        second_object_in_relationship: CollectionObjectName,
        *,
        nominal_angle: float = 0.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeObjectToObjectDirectionRelationship",
            "relationship_operations.make_object_to_object_direction_relationship",
            {
                "relationship_name": relationship_name,
                "first_object_in_relationship": first_object_in_relationship,
                "second_object_in_relationship": second_object_in_relationship,
                "nominal_angle": nominal_angle,
            },
            None,
        )
        return None

    async def make_point_clouds_to_objects_relationship(
        self,
        relationship_name: CollectionObjectName,
        point_clouds_in_relationship: Iterable[CollectionObjectName],
        objects_in_relationship: Iterable[CollectionObjectName],
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        auto_update_a_vector_group: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePointCloudsToObjectsRelationship",
            "relationship_operations.make_point_clouds_to_objects_relationship",
            {
                "relationship_name": relationship_name,
                "point_clouds_in_relationship": point_clouds_in_relationship,
                "objects_in_relationship": objects_in_relationship,
                "projection_options": projection_options,
                "auto_update_a_vector_group": auto_update_a_vector_group,
            },
            None,
        )
        return None

    async def make_point_to_point_relationship(
        self,
        relationship_name: CollectionObjectName,
        first_point_name: PointName,
        second_point_name: PointName,
        *,
        tolerance: ToleranceVectorOptions | None = None,
        constraint: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePointToPointRelationship",
            "relationship_operations.make_point_to_point_relationship",
            {
                "relationship_name": relationship_name,
                "first_point_name": first_point_name,
                "second_point_name": second_point_name,
                "tolerance": tolerance,
                "constraint": constraint,
            },
            None,
        )
        return None

    async def make_points_to_objects_relationship(
        self,
        relationship_name: CollectionObjectName,
        points_in_relationship: Iterable[PointName],
        objects_in_relationship: Iterable[CollectionObjectName],
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        auto_update_a_vector_group: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePointsToObjectsRelationship",
            "relationship_operations.make_points_to_objects_relationship",
            {
                "relationship_name": relationship_name,
                "points_in_relationship": points_in_relationship,
                "objects_in_relationship": objects_in_relationship,
                "projection_options": projection_options,
                "auto_update_a_vector_group": auto_update_a_vector_group,
            },
            None,
        )
        return None

    async def make_points_to_points_relationship(
        self,
        relationship_name: CollectionObjectName,
        nominal_points: Iterable[PointName],
        measured_points: Iterable[PointName],
        *,
        auto_update_a_vector_group: bool = False,
        tolerance: ToleranceVectorOptions | None = None,
        constraint: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePointsToPointsRelationship",
            "relationship_operations.make_points_to_points_relationship",
            {
                "relationship_name": relationship_name,
                "nominal_points": nominal_points,
                "measured_points": measured_points,
                "auto_update_a_vector_group": auto_update_a_vector_group,
                "tolerance": tolerance,
                "constraint": constraint,
            },
            None,
        )
        return None

    async def make_vector_group_to_vector_group_relationship(
        self,
        new_vg_to_vg_relationship: CollectionObjectName,
        reference_vector_group: CollectionObjectName,
        corresponding_vector_group: CollectionObjectName,
        *,
        set_opposing_vector_group_polarity: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakeVectorGroupToVectorGroupRelationship",
            "relationship_operations.make_vector_group_to_vector_group_relationship",
            {
                "new_vg_to_vg_relationship": new_vg_to_vg_relationship,
                "reference_vector_group": reference_vector_group,
                "corresponding_vector_group": corresponding_vector_group,
                "set_opposing_vector_group_polarity": set_opposing_vector_group_polarity,
            },
            None,
        )
        return None

    async def move_collections_by_minimizing_relationships(
        self,
        collections_to_move: Iterable[str],
        relationships_to_minimize: Iterable[CollectionObjectName],
        *,
        solver_mode: SolverMode = SolverMode.GAUSS_NEWTON,
        motion_to_allow: FitDofOptions | None = None,
        use_fit_dialog: bool = False,
        convergence_threshold: float = 0.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MoveCollectionsByMinimizingRelationships",
            "relationship_operations.move_collections_by_minimizing_relationships",
            {
                "collections_to_move": collections_to_move,
                "relationships_to_minimize": relationships_to_minimize,
                "solver_mode": solver_mode,
                "motion_to_allow": motion_to_allow,
                "use_fit_dialog": use_fit_dialog,
                "convergence_threshold": convergence_threshold,
            },
            None,
        )
        return None

    async def relationship_watch_window_template(
        self,
        *,
        watch_window_template_name: CollectionObjectName | None = None,
        options: RelationshipWatchWindowTemplateOptions | None = None,
    ) -> None:
        options = options or RelationshipWatchWindowTemplateOptions()
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "RelationshipWatchWindowTemplate",
            "relationship_operations.relationship_watch_window_template",
            {
                "watch_window_template_name": watch_window_template_name,
                "linear_precision": options.linear_precision,
                "angular_precision": options.angular_precision,
                "font": options.font,
                "text_color": options.text_color,
                "background_color": options.background_color,
                "highlight_color": options.highlight_color,
                "show_deviation_x_rx": options.show_deviation_x_rx,
                "show_deviation_y_ry": options.show_deviation_y_ry,
                "show_deviation_z_rz": options.show_deviation_z_rz,
                "show_deviation_magnitude": options.show_deviation_magnitude,
                "udp_network_transmit_settings": options.udp_network_transmit_settings,
                "transparent_background": options.transparent_background,
                "hide_units": options.hide_units,
            },
            None,
        )
        return None

    async def set_group_to_nominal_group_view_zooming(
        self,
        relationship_name: CollectionObjectName,
        *,
        use_closest_point: bool = True,
        show_closest_point_watch_window: bool = False,
        use_view_zooming: bool = True,
        ignore_points_beyond_threshold: bool = True,
        proximity_threshold: float = 0.01,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGroupToNominalGroupViewZooming",
            "relationship_operations.set_group_to_nominal_group_view_zooming",
            {
                "relationship_name": relationship_name,
                "use_closest_point": use_closest_point,
                "show_closest_point_watch_window": show_closest_point_watch_window,
                "use_view_zooming": use_view_zooming,
                "ignore_points_beyond_threshold": ignore_points_beyond_threshold,
                "proximity_threshold": proximity_threshold,
            },
            None,
        )
        return None

    async def set_object_to_object_direction_relationship_tolerances(
        self,
        relationship_name: CollectionItemName,
        *,
        angle_between_vectors_tolerances: ToleranceScalarOptions | None = None,
        mutual_perpendicular_length_tolerances: ToleranceScalarOptions | None = None,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetObjectToObjectDirectionRelationshipTolerances",
            "relationship_operations.set_object_to_object_direction_relationship_tolerances",
            {
                "relationship_name": relationship_name,
                "angle_between_vectors_tolerances": angle_between_vectors_tolerances,
                "mutual_perpendicular_length_tolerances": mutual_perpendicular_length_tolerances,
            },
            None,
        )
        return None

    async def set_optimization_perturbation_parameters(
        self,
        *,
        length_perturbation: float = 0.0001,
        angular_perturbation: float = 0.0001,
        damping: float = 1.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetOptimizationPerturbationParameters",
            "relationship_operations.set_optimization_perturbation_parameters",
            {
                "length_perturbation": length_perturbation,
                "angular_perturbation": angular_perturbation,
                "damping": damping,
            },
            None,
        )
        return None

    async def set_optimization_search_options(
        self,
        *,
        max_number_of_step_size_reduction: int = 5,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetOptimizationSearchOptions",
            "relationship_operations.set_optimization_search_options",
            {
                "max_number_of_step_size_reduction": max_number_of_step_size_reduction,
            },
            None,
        )
        return None

    async def set_points_to_points_relationship_associated_data(
        self,
        relationship_name: CollectionItemName,
        *,
        nominal_points: Iterable[PointName] | None = None,
        actual_points: Iterable[PointName] | None = None,
        ignore_empty_arguments: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetPointsToPointsRelationshipAssociatedData",
            "relationship_operations.set_points_to_points_relationship_associated_data",
            {
                "relationship_name": relationship_name,
                "nominal_points": nominal_points,
                "actual_points": actual_points,
                "ignore_empty_arguments": ignore_empty_arguments,
            },
            None,
        )
        return None

    async def set_relationship_associated_data(
        self,
        relationship_name: CollectionItemName,
        *,
        individual_points: Iterable[PointName] | None = None,
        point_groups: Iterable[CollectionObjectName] | None = None,
        point_clouds: Iterable[CollectionObjectName] | None = None,
        objects: Iterable[CollectionObjectName] | None = None,
        ignore_empty_arguments: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipAssociatedData",
            "relationship_operations.set_relationship_associated_data",
            {
                "relationship_name": relationship_name,
                "individual_points": individual_points,
                "point_groups": point_groups,
                "point_clouds": point_clouds,
                "objects": objects,
                "ignore_empty_arguments": ignore_empty_arguments,
            },
            None,
        )
        return None

    async def set_vector_group_to_vector_group_cylindrical_zone(
        self,
        vg_to_vg_relationship: CollectionObjectName,
        *,
        radial_offset: float = 1.0,
        minimum_axial_offset: float = -10.0,
        maximum_axial_offset: float = 10.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetVectorGroupToVectorGroupCylindricalZone",
            "relationship_operations.set_vector_group_to_vector_group_cylindrical_zone",
            {
                "vg_to_vg_relationship": vg_to_vg_relationship,
                "radial_offset": radial_offset,
                "minimum_axial_offset": minimum_axial_offset,
                "maximum_axial_offset": maximum_axial_offset,
            },
            None,
        )
        return None

    async def set_vector_group_to_vector_group_fit_gradient_factor(
        self,
        vg_to_vg_relationship: CollectionObjectName,
        *,
        fit_gradient_factor: float = 50.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetVectorGroupToVectorGroupFitGradientFactor",
            "relationship_operations.set_vector_group_to_vector_group_fit_gradient_factor",
            {
                "vg_to_vg_relationship": vg_to_vg_relationship,
                "fit_gradient_factor": fit_gradient_factor,
            },
            None,
        )
        return None

    async def set_vector_group_to_vector_group_fit_weights(
        self,
        vg_to_vg_relationship: CollectionObjectName,
        *,
        minimum_gap: float = 0.0,
        minimum_gap_fit_weight: float = 10.0,
        maximum_gap: float = 0.0,
        maximum_gap_fit_weight: float = 10.0,
        nominal_gap: float = 0.0,
        nominal_gap_fit_weight: float = 1.0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetVectorGroupToVectorGroupFitWeights",
            "relationship_operations.set_vector_group_to_vector_group_fit_weights",
            {
                "vg_to_vg_relationship": vg_to_vg_relationship,
                "minimum_gap": minimum_gap,
                "minimum_gap_fit_weight": minimum_gap,
                "maximum_gap": maximum_gap,
                "maximum_gap_fit_weight": maximum_gap,
                "nominal_gap": nominal_gap,
                "nominal_gap_fit_weight": nominal_gap,
            },
            None,
        )
        return None

    async def set_vector_group_to_vector_group_relative_polarity(
        self,
        vg_to_vg_relationship: CollectionObjectName,
        *,
        set_opposing_vector_group_polarity: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetVectorGroupToVectorGroupRelativePolarity",
            "relationship_operations.set_vector_group_to_vector_group_relative_polarity",
            {
                "vg_to_vg_relationship": vg_to_vg_relationship,
                "set_opposing_vector_group_polarity": set_opposing_vector_group_polarity,
            },
            None,
        )
        return None

    async def start_stop_relationship_trapping(
        self,
        relationship_name: CollectionObjectName,
        instrument_id: CollectionInstrumentId,
        *,
        start_trapping: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "StartStopRelationshipTrapping",
            "relationship_operations.start_stop_relationship_trapping",
            {
                "relationship_name": relationship_name,
                "instrument_id": instrument_id,
                "start_trapping": start_trapping,
            },
            None,
        )
        return None

    async def edit_geometry_relationship_point_list(
        self,
        relationship_name: CollectionObjectName,
        *,
        point_edit_mode: GeometryRelationshipPointEditMode = GeometryRelationshipPointEditMode.POINT_LIST,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "EditGeometryRelationshipPointList",
            "relationship_operations.edit_geometry_relationship_point_list",
            {
                "relationship_name": relationship_name,
                "point_edit_mode": point_edit_mode,
            },
            None,
        )
        return None

    async def get_relationship_sigmoidal_gap_fit_constraints(
        self,
        relationship_name: CollectionItemName,
    ) -> SigmoidalGapFitConstraints:
        return cast(
            SigmoidalGapFitConstraints,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipSigmoidalGapFitConstraints",
                "relationship_operations.get_relationship_sigmoidal_gap_fit_constraints",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )


class ConstructionOperations:
    def __init__(self, client: _WaveBClient) -> None:
        self._client = client

    async def add_surface_to_mesh_offset_along_reference_direction(
        self,
        reference_frame_names: Iterable[CollectionObjectName],
        surface_for_offset_distance_computation: CollectionObjectName,
        collection_for_result_frames: str,
        object_providing_direction_reference: CollectionObjectName,
        mesh_serving_as_projection_target: CollectionObjectName,
        *,
        surface_offset_range: float = 10,
        bi_directional_projection: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "AddSurfaceToMeshOffsetAlongReferenceDirection",
            "construction_operations.add_surface_to_mesh_offset_along_reference_direction",
            {
                "reference_frame_names": reference_frame_names,
                "surface_for_offset_distance_computation": surface_for_offset_distance_computation,
                "surface_offset_range": surface_offset_range,
                "collection_for_result_frames": collection_for_result_frames,
                "object_providing_direction_reference": object_providing_direction_reference,
                "bi_directional_projection": bi_directional_projection,
                "mesh_serving_as_projection_target": mesh_serving_as_projection_target,
            },
            None,
        )
        return None

    async def auto_arrange_callout_view(
        self,
        callout_view: CollectionItemName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "AutoArrangeCalloutView",
            "construction_operations.auto_arrange_callout_view",
            {
                "callout_view": callout_view,
            },
            None,
        )
        return None

    async def clear_hidden_point_bar_database(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ClearHiddenPointBarDatabase",
            "construction_operations.clear_hidden_point_bar_database",
            {},
            None,
        )
        return None

    async def construct_b_spline_from_intersection_of_plane_and_surface(
        self,
        resulting_b_spline_name: CollectionObjectName,
        plane_name: CollectionObjectName,
        surface_name: CollectionObjectName,
        *,
        approximation_tolerance: float = 0.0001,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBSplineFromIntersectionOfPlaneAndSurface",
            "construction_operations.construct_b_spline_from_intersection_of_plane_and_surface",
            {
                "resulting_b_spline_name": resulting_b_spline_name,
                "plane_name": plane_name,
                "surface_name": surface_name,
                "approximation_tolerance": approximation_tolerance,
            },
            None,
        )
        return None

    async def construct_b_spline_from_intersection_of_surfaces(
        self,
        resulting_b_spline_name: CollectionObjectName,
        first_surface_name: CollectionObjectName,
        second_surface_name: CollectionObjectName,
        *,
        approximation_tolerance: float = 0.0001,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBSplineFromIntersectionOfSurfaces",
            "construction_operations.construct_b_spline_from_intersection_of_surfaces",
            {
                "resulting_b_spline_name": resulting_b_spline_name,
                "first_surface_name": first_surface_name,
                "second_surface_name": second_surface_name,
                "approximation_tolerance": approximation_tolerance,
            },
            None,
        )
        return None

    async def construct_b_spline_from_point_set(
        self,
        resulting_b_spline_name: CollectionObjectName,
        point_set_container: CollectionObjectName,
        *,
        b_spline_fit_options: BSplineFitOptions | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBSplineFromPointSet",
            "construction_operations.construct_b_spline_from_point_set",
            {
                "resulting_b_spline_name": resulting_b_spline_name,
                "b_spline_fit_options": b_spline_fit_options,
                "point_set_container": point_set_container,
            },
            None,
        )
        return None

    async def construct_b_spline_from_points(
        self,
        resulting_b_spline_name: CollectionObjectName,
        point_list: Iterable[PointName],
        *,
        b_spline_fit_options: BSplineFitOptions | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBSplineFromPoints",
            "construction_operations.construct_b_spline_from_points",
            {
                "resulting_b_spline_name": resulting_b_spline_name,
                "b_spline_fit_options": b_spline_fit_options,
                "point_list": point_list,
            },
            None,
        )
        return None

    async def construct_b_spline_from_several_b_splines(
        self,
        resulting_b_spline_name: CollectionObjectName,
        b_spline_list: Iterable[CollectionObjectName],
        *,
        close_resulting_b_spline: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBSplineFromSeveralBSplines",
            "construction_operations.construct_b_spline_from_several_b_splines",
            {
                "resulting_b_spline_name": resulting_b_spline_name,
                "b_spline_list": b_spline_list,
                "close_resulting_b_spline": close_resulting_b_spline,
            },
            None,
        )
        return None

    async def construct_b_splines_from_intersection_of_plane_and_mesh(
        self,
        resulting_b_spline_name: CollectionObjectName,
        plane_name: CollectionObjectName,
        mesh_name: CollectionObjectName,
        *,
        closed_line_segment_limit: int = 3,
        unclosed_line_segment_limit: int = 3,
        create_intersection_points: bool = True,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructBSplinesFromIntersectionOfPlaneAndMesh",
                "construction_operations.construct_b_splines_from_intersection_of_plane_and_mesh",
                {
                    "resulting_b_spline_name": resulting_b_spline_name,
                    "plane_name": plane_name,
                    "mesh_name": mesh_name,
                    "closed_line_segment_limit": closed_line_segment_limit,
                    "unclosed_line_segment_limit": unclosed_line_segment_limit,
                    "create_intersection_points": create_intersection_points,
                },
                None,
            ),
        )

    async def construct_b_splines_from_lines(
        self,
        line_list: Iterable[CollectionObjectName],
        *,
        resulting_b_spline_name_prefix: str | None = None,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructBSplinesFromLines",
                "construction_operations.construct_b_splines_from_lines",
                {
                    "resulting_b_spline_name_prefix": resulting_b_spline_name_prefix,
                    "line_list": line_list,
                },
                None,
            ),
        )

    async def construct_b_splines_from_surfaces(
        self,
        surface_list: Iterable[CollectionObjectName],
        *,
        resulting_b_spline_name_prefix: str | None = None,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructBSplinesFromSurfaces",
                "construction_operations.construct_b_splines_from_surfaces",
                {
                    "resulting_b_spline_name_prefix": resulting_b_spline_name_prefix,
                    "surface_list": surface_list,
                },
                None,
            ),
        )

    async def construct_boundary_points_from_cloud(
        self,
        source_cloud_name: CollectionObjectName,
        destination_cloud_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructBoundaryPointsFromCloud",
            "construction_operations.construct_boundary_points_from_cloud",
            {
                "source_cloud_name": source_cloud_name,
                "destination_cloud_name": destination_cloud_name,
            },
            None,
        )
        return None

    async def construct_circle(
        self,
        circle_name: CollectionObjectName,
        circle_center: Vector,
        circle_normal: Vector,
        circle_radius: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCircle",
            "construction_operations.construct_circle",
            {
                "circle_name": circle_name,
                "circle_center": circle_center,
                "circle_normal": circle_normal,
                "circle_radius": circle_radius,
            },
            None,
        )
        return None

    async def construct_circles_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCirclesFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_circles_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_circles_lines_from_surfaces(
        self,
        surfaces: Iterable[CollectionObjectName],
        circle_line_mode: CircleLineMode,
        *,
        minimum_diameter: float = 0.0,
        maximum_diameter: float = 0.0,
        tolerance: float = 0.02,
        single_surface: bool = False,
        destination_collection_name: CollectionName | None = None,
        base_name: str = "Geometry Object",
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructCirclesLinesFromSurfaces",
                "construction_operations.construct_circles_lines_from_surfaces",
                {
                    "surfaces": surfaces,
                    "minimum_diameter": minimum_diameter,
                    "maximum_diameter": maximum_diameter,
                    "tolerance": tolerance,
                    "single_surface": single_surface,
                    "circle_line_mode": circle_line_mode,
                    "destination_collection_name": destination_collection_name,
                    "base_name": base_name,
                },
                None,
            ),
        )

    async def construct_collection(
        self,
        collection_name: CollectionName,
        *,
        folder_path: str = "",
        make_default_collection: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCollection",
            "construction_operations.construct_collection",
            {
                "collection_name": collection_name,
                "folder_path": folder_path,
                "make_default_collection": make_default_collection,
            },
            None,
        )
        return None

    async def construct_cone(
        self,
        cone_name: CollectionObjectName,
        cone_end_point: Vector,
        cone_axis: Vector,
        cone_length: float,
        cone_theta_start: float,
        cone_theta_span: float,
        cone_included_angle: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCone",
            "construction_operations.construct_cone",
            {
                "cone_name": cone_name,
                "cone_end_point": cone_end_point,
                "cone_axis": cone_axis,
                "cone_length": cone_length,
                "cone_theta_start": cone_theta_start,
                "cone_theta_span": cone_theta_span,
                "cone_included_angle": cone_included_angle,
            },
            None,
        )
        return None

    async def construct_cones_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructConesFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_cones_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_cross_section_cloud(
        self,
        cross_section_cloud_name: CollectionObjectName,
        input_clouds: Iterable[CollectionObjectName],
        *,
        cylindrical_cross_section_mode: bool = False,
        start_distance: float = 0.0,
        section_spacing: float = 0.0,
        proximity_threshold: float = 0.0,
        maximum_section_count: int = 0,
        limit_cross_section_extent: bool = False,
        radius_limit: float = 0.0,
        project_to_reference_surface: bool = False,
        reference_object: CollectionObjectName | None = None,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        update_existing_cloud: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCrossSectionCloud",
            "construction_operations.construct_cross_section_cloud",
            {
                "cross_section_cloud_name": cross_section_cloud_name,
                "cylindrical_cross_section_mode": cylindrical_cross_section_mode,
                "start_distance": start_distance,
                "section_spacing": section_spacing,
                "proximity_threshold": proximity_threshold,
                "maximum_section_count": maximum_section_count,
                "limit_cross_section_extent": limit_cross_section_extent,
                "radius_limit": radius_limit,
                "project_to_reference_surface": project_to_reference_surface,
                "reference_object": reference_object,
                "input_clouds": input_clouds,
                "cloud_thinning_settings": cloud_thinning_settings,
                "update_existing_cloud": update_existing_cloud,
            },
            None,
        )
        return None

    async def construct_cross_section_cloud_user_select(
        self,
        cross_section_cloud_name: CollectionObjectName,
        reference_planes: Iterable[CollectionObjectName],
        input_clouds: Iterable[CollectionObjectName],
        *,
        proximity_threshold: float = 0.0,
        limit_cross_section_extent: bool = False,
        radius_limit: float = 0.0,
        project_to_reference_surface: bool = False,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        update_existing_cloud: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCrossSectionCloudUserSelect",
            "construction_operations.construct_cross_section_cloud_user_select",
            {
                "cross_section_cloud_name": cross_section_cloud_name,
                "proximity_threshold": proximity_threshold,
                "limit_cross_section_extent": limit_cross_section_extent,
                "radius_limit": radius_limit,
                "project_to_reference_surface": project_to_reference_surface,
                "reference_planes": reference_planes,
                "input_clouds": input_clouds,
                "cloud_thinning_settings": cloud_thinning_settings,
                "update_existing_cloud": update_existing_cloud,
            },
            None,
        )
        return None

    async def construct_cylinder(
        self,
        cylinder_name: CollectionObjectName,
        cylinder_end_point: Vector,
        cylinder_axis: Vector,
        cylinder_diameter: float,
        cylinder_length: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCylinder",
            "construction_operations.construct_cylinder",
            {
                "cylinder_name": cylinder_name,
                "cylinder_end_point": cylinder_end_point,
                "cylinder_axis": cylinder_axis,
                "cylinder_diameter": cylinder_diameter,
                "cylinder_length": cylinder_length,
            },
            None,
        )
        return None

    async def construct_cylinder_from_end_points(
        self,
        cylinder_name: CollectionObjectName,
        cylinder_end_point_a: Vector,
        cylinder_end_point_b: Vector,
        cylinder_diameter: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCylinderFromEndPoints",
            "construction_operations.construct_cylinder_from_end_points",
            {
                "cylinder_name": cylinder_name,
                "cylinder_end_point_a": cylinder_end_point_a,
                "cylinder_end_point_b": cylinder_end_point_b,
                "cylinder_diameter": cylinder_diameter,
            },
            None,
        )
        return None

    async def construct_cylinders_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructCylindersFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_cylinders_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_ellipse(
        self,
        ellipse_name: CollectionObjectName,
        center_coordinate: Vector,
        normal_direction: Vector,
        major_axis_radius: float,
        minor_axis_radius: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructEllipse",
            "construction_operations.construct_ellipse",
            {
                "ellipse_name": ellipse_name,
                "center_coordinate": center_coordinate,
                "normal_direction": normal_direction,
                "major_axis_radius": major_axis_radius,
                "minor_axis_radius": minor_axis_radius,
            },
            None,
        )
        return None

    async def construct_ellipsoid(
        self,
        ellipse_name: CollectionObjectName,
        *,
        x_axis_radius: float = 5.0,
        y_axis_radius: float = 4.0,
        z_axis_radius: float = 3.0,
        magnification: float = 1.0,
        uncertainty_ellipsoid: bool = False,
        transform_in_working_coordinates: Transform | None = None,
        ellipse_color: Color | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructEllipsoid",
            "construction_operations.construct_ellipsoid",
            {
                "ellipse_name": ellipse_name,
                "x_axis_radius": x_axis_radius,
                "y_axis_radius": y_axis_radius,
                "z_axis_radius": z_axis_radius,
                "magnification": magnification,
                "uncertainty_ellipsoid": uncertainty_ellipsoid,
                "transform_in_working_coordinates": transform_in_working_coordinates,
                "ellipse_color": ellipse_color,
            },
            None,
        )
        return None

    async def construct_folders(
        self,
        folder_path: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFolders",
            "construction_operations.construct_folders",
            {
                "folder_path": folder_path,
            },
            None,
        )
        return None

    async def construct_frame(
        self,
        new_frame_name: CollectionObjectName,
        *,
        transform_in_working_coordinates: Transform | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrame",
            "construction_operations.construct_frame",
            {
                "new_frame_name": new_frame_name,
                "transform_in_working_coordinates": transform_in_working_coordinates,
            },
            None,
        )
        return None

    async def construct_frame_at_point_with_working_z_and_clocked_axis(
        self,
        origin_point: PointName,
        clocked_axis: AxisIdentifier,
        clocking_point: PointName,
        *,
        frame_name: str | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameAtPointWithWorkingZAndClockedAxis",
            "construction_operations.construct_frame_at_point_with_working_z_and_clocked_axis",
            {
                "origin_point": origin_point,
                "clocked_axis": clocked_axis,
                "clocking_point": clocking_point,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_at_robot_link(
        self,
        machine_id: CollectionMachineId,
        link_name: str,
        resulting_frame: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameAtRobotLink",
            "construction_operations.construct_frame_at_robot_link",
            {
                "machine_id": machine_id,
                "link_name": link_name,
                "resulting_frame": resulting_frame,
            },
            None,
        )
        return None

    async def construct_frame_average_of_other_object_frames(
        self,
        objects: Iterable[CollectionObjectName],
        *,
        frame_name: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameAverageOfOtherObjectFrames",
            "construction_operations.construct_frame_average_of_other_object_frames",
            {
                "objects": objects,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_copy_and_make_left_handed(
        self,
        reference_frame: CollectionObjectName,
        axis_to_reverse: FrameAxis,
        *,
        frame_name: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameCopyAndMakeLeftHanded",
            "construction_operations.construct_frame_copy_and_make_left_handed",
            {
                "reference_frame": reference_frame,
                "frame_name": frame_name,
                "axis_to_reverse": axis_to_reverse,
            },
            None,
        )
        return None

    async def construct_frame_from_point_measurement_probing_frames(
        self,
        point_list: Iterable[PointName],
        *,
        show_frame: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameFromPointMeasurementProbingFrames",
            "construction_operations.construct_frame_from_point_measurement_probing_frames",
            {
                "point_list": point_list,
                "show_frame": show_frame,
            },
            None,
        )
        return None

    async def construct_frame_from_transform_in_world(
        self,
        new_frame_name: CollectionObjectName,
        *,
        transform_in_world_coordinates: Transform | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameFromTransformInWorld",
            "construction_operations.construct_frame_from_transform_in_world",
            {
                "new_frame_name": new_frame_name,
                "transform_in_world_coordinates": transform_in_world_coordinates,
            },
            None,
        )
        return None

    async def construct_frame_known_origin_object_direction_object_direction(
        self,
        known_point: PointName,
        known_point_value_in_new_frame: Vector,
        primary_axis_object: CollectionObjectName,
        primary_axis_defines_which_axis: AxisIdentifier,
        secondary_axis_object: CollectionObjectName,
        secondary_axis_defines_which_axis: AxisIdentifier,
        *,
        frame_name: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameKnownOriginObjectDirectionObjectDirection",
            "construction_operations.construct_frame_known_origin_object_direction_object_direction",
            {
                "known_point": known_point,
                "known_point_value_in_new_frame": known_point,
                "primary_axis_object": primary_axis_object,
                "primary_axis_defines_which_axis": primary_axis_defines_which_axis,
                "secondary_axis_object": secondary_axis_object,
                "secondary_axis_defines_which_axis": secondary_axis_defines_which_axis,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_on_instrument_base(
        self,
        instrument_id: CollectionInstrumentId,
        *,
        frame_name: str | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameOnInstrumentBase",
            "construction_operations.construct_frame_on_instrument_base",
            {
                "instrument_id": instrument_id,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_on_object(
        self,
        reference_object: CollectionObjectName,
        *,
        frame_name: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameOnObject",
            "construction_operations.construct_frame_on_object",
            {
                "reference_object": reference_object,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_pick_origin_and_point_on_x_axis_clock_z_along_working_z(
        self,
        origin_point: PointName,
        point_on_x_axis: PointName,
        *,
        frame_name: str | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFramePickOriginAndPointOnXAxisClockZAlongWorkingZ",
            "construction_operations.construct_frame_pick_origin_and_point_on_x_axis_clock_z_along_working_z",
            {
                "origin_point": origin_point,
                "point_on_x_axis": point_on_x_axis,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_three_planes(
        self,
        x_plane: CollectionObjectName,
        x_value_on_plane: float,
        y_plane: CollectionObjectName,
        y_value_on_plane: float,
        z_plane: CollectionObjectName,
        z_value_on_plane: float,
        *,
        frame_name: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameThreePlanes",
            "construction_operations.construct_frame_three_planes",
            {
                "x_plane": x_plane,
                "x_value_on_plane": x_value_on_plane,
                "y_plane": y_plane,
                "y_value_on_plane": y_value_on_plane,
                "z_plane": z_plane,
                "z_value_on_plane": z_value_on_plane,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_three_points(
        self,
        construction_method: FrameConstructionMethod,
        origin_point: PointName,
        primary_axis_point: PointName,
        secondary_axis_point: PointName,
        *,
        frame_name: str | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameThreePoints",
            "construction_operations.construct_frame_three_points",
            {
                "construction_method": construction_method,
                "origin_point": origin_point,
                "primary_axis_point": primary_axis_point,
                "secondary_axis_point": secondary_axis_point,
                "frame_name": frame_name,
            },
            None,
        )
        return None

    async def construct_frame_with_wizard(
        self,
        new_frame_name: CollectionObjectName,
        *,
        wait_for_completion: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructFrameWithWizard",
            "construction_operations.construct_frame_with_wizard",
            {
                "new_frame_name": new_frame_name,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def construct_frames_by_projecting_frames_on_mesh_along_frame_direction(
        self,
        reference_frame_names: Iterable[CollectionObjectName],
        base_name_for_projected_frames: CollectionObjectName,
        mesh_serving_as_projection_target: CollectionObjectName,
        *,
        bi_directional_projection: bool = True,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructFramesByProjectingFramesOnMeshAlongFrameDirection",
                "construction_operations.construct_frames_by_projecting_frames_on_mesh_along_frame_direction",
                {
                    "reference_frame_names": reference_frame_names,
                    "base_name_for_projected_frames": base_name_for_projected_frames,
                    "bi_directional_projection": bi_directional_projection,
                    "mesh_serving_as_projection_target": mesh_serving_as_projection_target,
                },
                None,
            ),
        )

    async def construct_frames_by_projecting_frames_on_mesh_along_reference_direction(
        self,
        reference_frame_names: Iterable[CollectionObjectName],
        base_name_for_projected_frames: CollectionObjectName,
        object_providing_direction_reference: CollectionObjectName,
        mesh_serving_as_projection_target: CollectionObjectName,
        *,
        bi_directional_projection: bool = True,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructFramesByProjectingFramesOnMeshAlongReferenceDirection",
                "construction_operations.construct_frames_by_projecting_frames_on_mesh_along_reference_direction",
                {
                    "reference_frame_names": reference_frame_names,
                    "base_name_for_projected_frames": base_name_for_projected_frames,
                    "object_providing_direction_reference": object_providing_direction_reference,
                    "bi_directional_projection": bi_directional_projection,
                    "mesh_serving_as_projection_target": mesh_serving_as_projection_target,
                },
                None,
            ),
        )

    async def construct_line_center_of_slot(
        self,
        line_name: CollectionObjectName,
        slot_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineCenterOfSlot",
            "construction_operations.construct_line_center_of_slot",
            {
                "line_name": line_name,
                "slot_name": slot_name,
            },
            None,
        )
        return None

    async def construct_line_from_instrument_shot(
        self,
        point_name: PointName,
        line_name: CollectionObjectName,
        *,
        observation_index: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineFromInstrumentShot",
            "construction_operations.construct_line_from_instrument_shot",
            {
                "point_name": point_name,
                "observation_index": observation_index,
                "line_name": line_name,
            },
            None,
        )
        return None

    async def construct_line_normal_to_object(
        self,
        line_name: CollectionObjectName,
        object: CollectionObjectName,
        *,
        line_length: float = 1,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineNormalToObject",
            "construction_operations.construct_line_normal_to_object",
            {
                "line_name": line_name,
                "line_length": line_length,
                "object": object,
            },
            None,
        )
        return None

    async def construct_line_normal_to_object_through_point(
        self,
        line_to_create: CollectionObjectName,
        object_name: CollectionObjectName,
        point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineNormalToObjectThroughPoint",
            "construction_operations.construct_line_normal_to_object_through_point",
            {
                "line_to_create": line_to_create,
                "object_name": object_name,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_line_project_line_to_object_reference_plane(
        self,
        line_to_create: CollectionObjectName,
        line_to_project: CollectionObjectName,
        object_to_project_to: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineProjectLineToObjectReferencePlane",
            "construction_operations.construct_line_project_line_to_object_reference_plane",
            {
                "line_to_create": line_to_create,
                "line_to_project": line_to_project,
                "object_to_project_to": object_to_project_to,
            },
            None,
        )
        return None

    async def construct_line_two_plane_intersection(
        self,
        line_name: CollectionObjectName,
        first_plane: CollectionObjectName,
        second_plane: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineTwoPlaneIntersection",
            "construction_operations.construct_line_two_plane_intersection",
            {
                "line_name": line_name,
                "first_plane": first_plane,
                "second_plane": second_plane,
            },
            None,
        )
        return None

    async def construct_line_two_points(
        self,
        line_name: CollectionObjectName,
        first_point: PointName,
        second_point: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineTwoPoints",
            "construction_operations.construct_line_two_points",
            {
                "line_name": line_name,
                "first_point": first_point,
                "second_point": second_point,
            },
            None,
        )
        return None

    async def construct_line_two_points_vector_notation(
        self,
        line_name: CollectionObjectName,
        first_vector: Vector,
        second_vector: Vector,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLineTwoPointsVectorNotation",
            "construction_operations.construct_line_two_points_vector_notation",
            {
                "line_name": line_name,
                "first_vector": first_vector,
                "second_vector": second_vector,
            },
            None,
        )
        return None

    async def construct_lines_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructLinesFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_lines_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_mirror_cube_frame(
        self,
        mirror_cube_frame_name: CollectionObjectName,
        point_name: PointName,
        *,
        use_current_measurements_marked_as_mirror_shots: bool = True,
        nominal_cube_face_angle: float = 90,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructMirrorCubeFrame",
                "construction_operations.construct_mirror_cube_frame",
                {
                    "mirror_cube_frame_name": mirror_cube_frame_name,
                    "point_name": point_name,
                    "use_current_measurements_marked_as_mirror_shots": use_current_measurements_marked_as_mirror_shots,
                    "nominal_cube_face_angle": nominal_cube_face_angle,
                },
                None,
            ),
        )

    async def construct_perimeter_from_points(
        self,
        resulting_perimeter_name: CollectionObjectName,
        point_list: Iterable[PointName],
        *,
        open_perimeter: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPerimeterFromPoints",
            "construction_operations.construct_perimeter_from_points",
            {
                "resulting_perimeter_name": resulting_perimeter_name,
                "point_list": point_list,
                "open_perimeter": open_perimeter,
            },
            None,
        )
        return None

    async def construct_plane(
        self,
        plane_name: CollectionObjectName,
        plane_center: Vector,
        plane_normal: Vector,
        *,
        plane_edge_dimension: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPlane",
            "construction_operations.construct_plane",
            {
                "plane_name": plane_name,
                "plane_center": plane_center,
                "plane_normal": plane_normal,
                "plane_edge_dimension": plane_edge_dimension,
            },
            None,
        )
        return None

    async def construct_plane_normal_to_object_through_point(
        self,
        resultant_plane_name: CollectionObjectName,
        normal_to_object_name: CollectionObjectName,
        through_point_name: PointName,
        *,
        plane_edge_dimension: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPlaneNormalToObjectThroughPoint",
            "construction_operations.construct_plane_normal_to_object_through_point",
            {
                "resultant_plane_name": resultant_plane_name,
                "normal_to_object_name": normal_to_object_name,
                "through_point_name": through_point_name,
                "plane_edge_dimension": plane_edge_dimension,
            },
            None,
        )
        return None

    async def construct_planes_bisect_two_planes(
        self,
        resultant_plane_name: CollectionObjectName,
        first_plane: CollectionObjectName,
        second_plane: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPlanesBisectTwoPlanes",
            "construction_operations.construct_planes_bisect_two_planes",
            {
                "resultant_plane_name": resultant_plane_name,
                "first_plane": first_plane,
                "second_plane": second_plane,
            },
            None,
        )
        return None

    async def construct_planes_bounding_point_group(
        self,
        reference_plane_name: CollectionObjectName,
        group_to_bound: CollectionObjectName,
        *,
        resulting_high_plane_name: CollectionObjectName | None = None,
        resulting_low_plane_name: CollectionObjectName | None = None,
        override_target_point_offsets: bool = False,
        offset_value: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPlanesBoundingPointGroup",
            "construction_operations.construct_planes_bounding_point_group",
            {
                "reference_plane_name": reference_plane_name,
                "group_to_bound": group_to_bound,
                "resulting_high_plane_name": resulting_high_plane_name,
                "resulting_low_plane_name": resulting_low_plane_name,
                "override_target_point_offsets": override_target_point_offsets,
                "offset_value": offset_value,
            },
            None,
        )
        return None

    async def construct_planes_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPlanesFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_planes_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_point_at_circle_center(
        self,
        circle_name: CollectionObjectName,
        point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtCircleCenter",
            "construction_operations.construct_point_at_circle_center",
            {
                "circle_name": circle_name,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_point_at_intersection_of_b_spline_and_surfaces(
        self,
        b_spline_name: CollectionObjectName,
        surface_list: Iterable[CollectionObjectName],
        point_name: PointName,
        *,
        approximation_tolerance: float = 0.001,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtIntersectionOfBSplineAndSurfaces",
            "construction_operations.construct_point_at_intersection_of_b_spline_and_surfaces",
            {
                "b_spline_name": b_spline_name,
                "surface_list": surface_list,
                "approximation_tolerance": approximation_tolerance,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_point_at_intersection_of_plane_and_line(
        self,
        plane_name: CollectionObjectName,
        line_name: CollectionObjectName,
        resulting_point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtIntersectionOfPlaneAndLine",
            "construction_operations.construct_point_at_intersection_of_plane_and_line",
            {
                "plane_name": plane_name,
                "line_name": line_name,
                "resulting_point_name": resulting_point_name,
            },
            None,
        )
        return None

    async def construct_point_at_intersection_of_planes(
        self,
        plane_1_name: CollectionObjectName,
        plane_2_name: CollectionObjectName,
        plane_3_name: CollectionObjectName,
        point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtIntersectionOfPlanes",
            "construction_operations.construct_point_at_intersection_of_planes",
            {
                "plane_1_name": plane_1_name,
                "plane_2_name": plane_2_name,
                "plane_3_name": plane_3_name,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_point_at_intersection_of_two_b_splines(
        self,
        first_b_spline_name: CollectionObjectName,
        second_b_spline_name: CollectionObjectName,
        point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtIntersectionOfTwoBSplines",
            "construction_operations.construct_point_at_intersection_of_two_b_splines",
            {
                "first_b_spline_name": first_b_spline_name,
                "second_b_spline_name": second_b_spline_name,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_point_at_intersection_of_two_lines(
        self,
        first_line_name: CollectionObjectName,
        second_line_name: CollectionObjectName,
        resulting_point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtIntersectionOfTwoLines",
            "construction_operations.construct_point_at_intersection_of_two_lines",
            {
                "first_line_name": first_line_name,
                "second_line_name": second_line_name,
                "resulting_point_name": resulting_point_name,
            },
            None,
        )
        return None

    async def construct_point_at_line_midpoint(
        self,
        line_name: CollectionObjectName,
        point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtLineMidpoint",
            "construction_operations.construct_point_at_line_midpoint",
            {
                "line_name": line_name,
                "point_name": point_name,
            },
            None,
        )
        return None

    async def construct_point_at_projection_of_point_onto_object(
        self,
        point_to_project: PointName,
        object_name: CollectionObjectName,
        resulting_point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointAtProjectionOfPointOntoObject",
            "construction_operations.construct_point_at_projection_of_point_onto_object",
            {
                "point_to_project": point_to_project,
                "object_name": object_name,
                "resulting_point_name": resulting_point_name,
            },
            None,
        )
        return None

    async def construct_point_cloud_from_existing_clouds(
        self,
        existing_point_cloud_list: Iterable[CollectionObjectName],
        new_cloud_name: CollectionObjectName,
        *,
        cloud_thinning_settings: CloudThinningOptions | None = None,
        hide_original_point_clouds: bool = True,
        set_cloud_point_rgb_from_voxels: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudFromExistingClouds",
            "construction_operations.construct_point_cloud_from_existing_clouds",
            {
                "existing_point_cloud_list": existing_point_cloud_list,
                "new_cloud_name": new_cloud_name,
                "cloud_thinning_settings": cloud_thinning_settings,
                "hide_original_point_clouds": hide_original_point_clouds,
                "set_cloud_point_rgb_from_voxels": set_cloud_point_rgb_from_voxels,
            },
            None,
        )
        return None

    async def construct_point_cloud_from_visible_cloud_points(
        self,
        source_clouds: Iterable[CollectionObjectName],
        destination_cloud_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudFromVisibleCloudPoints",
            "construction_operations.construct_point_cloud_from_visible_cloud_points",
            {
                "source_clouds": source_clouds,
                "destination_cloud_name": destination_cloud_name,
            },
            None,
        )
        return None

    async def construct_point_cloud_limiting_probing_directions(
        self,
        source_cloud_name: CollectionObjectName,
        normal_to_object_name: CollectionObjectName,
        destination_cloud_name: CollectionObjectName,
        *,
        acceptance_angle: float = 30.0,
        hide_source_cloud: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudLimitingProbingDirections",
            "construction_operations.construct_point_cloud_limiting_probing_directions",
            {
                "source_cloud_name": source_cloud_name,
                "normal_to_object_name": normal_to_object_name,
                "acceptance_angle": acceptance_angle,
                "destination_cloud_name": destination_cloud_name,
                "hide_source_cloud": hide_source_cloud,
            },
            None,
        )
        return None

    async def construct_point_clouds_from_existing_cloud_points_runtime_select(
        self,
        cloud_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudsFromExistingCloudPointsRuntimeSelect",
            "construction_operations.construct_point_clouds_from_existing_cloud_points_runtime_select",
            {
                "cloud_name": cloud_name,
            },
            None,
        )
        return None

    async def construct_point_clouds_from_existing_clouds_uniform_spacing(
        self,
        existing_point_cloud_list: Iterable[CollectionObjectName],
        new_cloud_name: CollectionObjectName,
        *,
        desired_point_spacing: float = 0.02,
        minimum_points_per_output_point: int = 3,
        hide_original_point_clouds: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudsFromExistingCloudsUniformSpacing",
            "construction_operations.construct_point_clouds_from_existing_clouds_uniform_spacing",
            {
                "existing_point_cloud_list": existing_point_cloud_list,
                "desired_point_spacing": desired_point_spacing,
                "minimum_points_per_output_point": minimum_points_per_output_point,
                "new_cloud_name": new_cloud_name,
                "hide_original_point_clouds": hide_original_point_clouds,
            },
            None,
        )
        return None

    async def construct_point_clouds_from_existing_point_group(
        self,
        point_group_name: CollectionObjectName,
        cloud_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointCloudsFromExistingPointGroup",
            "construction_operations.construct_point_clouds_from_existing_point_group",
            {
                "point_group_name": point_group_name,
                "cloud_name": cloud_name,
            },
            None,
        )
        return None

    async def construct_point_fit_to_points(
        self,
        point_names: Iterable[PointName],
        resulting_point_name: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointFitToPoints",
            "construction_operations.construct_point_fit_to_points",
            {
                "point_names": point_names,
                "resulting_point_name": resulting_point_name,
            },
            None,
        )
        return None

    async def construct_point_from_cloud_point_runtime_select(
        self,
        *,
        selection_prompt: str = "Select cloud point",
        construct_point: bool = False,
        constructed_point_name: PointName | None = None,
    ) -> Vector:
        return cast(
            Vector,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructPointFromCloudPointRuntimeSelect",
                "construction_operations.construct_point_from_cloud_point_runtime_select",
                {
                    "selection_prompt": selection_prompt,
                    "construct_point": construct_point,
                    "constructed_point_name": constructed_point_name,
                },
                None,
            ),
        )

    async def construct_point_from_survey_target_center(
        self,
        cloud_containing_target: CollectionObjectName,
        reference_seed_point: PointName,
        result_center_point_name: PointName,
        *,
        survey_target_type: SurveyTargetType = SurveyTargetType.TRIANGLE,
        search_diameter: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointFromSurveyTargetCenter",
            "construction_operations.construct_point_from_survey_target_center",
            {
                "cloud_containing_target": cloud_containing_target,
                "reference_seed_point": reference_seed_point,
                "survey_target_type": survey_target_type,
                "search_diameter": search_diameter,
                "result_center_point_name": result_center_point_name,
            },
            None,
        )
        return None

    async def construct_point_group_from_point_cloud(
        self,
        cloud_name: CollectionObjectName,
        point_group_name: CollectionObjectName,
        *,
        point_prefix: str = "pt",
        starting_point_number: int = 0,
        point_offset: float = 0.0,
        sub_sampling: bool = False,
        sub_sampling_distance: float = 0.5,
        show_progress: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointGroupFromPointCloud",
            "construction_operations.construct_point_group_from_point_cloud",
            {
                "cloud_name": cloud_name,
                "point_group_name": point_group_name,
                "point_prefix": point_prefix,
                "starting_point_number": starting_point_number,
                "point_offset": point_offset,
                "sub_sampling": sub_sampling,
                "sub_sampling_distance": sub_sampling,
                "show_progress": show_progress,
            },
            None,
        )
        return None

    async def construct_point_group_from_point_name_ref_list(
        self,
        point_name_list: Iterable[PointName],
        group_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointGroupFromPointNameRefList",
            "construction_operations.construct_point_group_from_point_name_ref_list",
            {
                "point_name_list": point_name_list,
                "group_name": group_name,
            },
            None,
        )
        return None

    async def construct_point_groups_from_vector_groups(
        self,
        vector_groups: Iterable[CollectionObjectName],
        *,
        optional_group_name_suffix: str = "",
        make_vector_begin_points: bool = False,
        make_vector_end_points: bool = False,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructPointGroupsFromVectorGroups",
                "construction_operations.construct_point_groups_from_vector_groups",
                {
                    "vector_groups": vector_groups,
                    "optional_group_name_suffix": optional_group_name_suffix,
                    "make_vector_begin_points": make_vector_begin_points,
                    "make_vector_end_points": make_vector_end_points,
                },
                None,
            ),
        )

    async def construct_point_in_working_coordinates(
        self,
        point_name: PointName,
        working_coordinates: Vector,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointInWorkingCoordinates",
            "construction_operations.construct_point_in_working_coordinates",
            {
                "point_name": point_name,
                "working_coordinates": working_coordinates,
            },
            None,
        )
        return None

    async def construct_points_at_intersection_of_circle_and_line(
        self,
        circle_name: CollectionObjectName,
        line_name: CollectionObjectName,
        base_point_name_for_results: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAtIntersectionOfCircleAndLine",
            "construction_operations.construct_points_at_intersection_of_circle_and_line",
            {
                "circle_name": circle_name,
                "line_name": line_name,
                "base_point_name_for_results": base_point_name_for_results,
            },
            None,
        )
        return None

    async def construct_points_at_intersection_of_principal_object_axes_and_surfaces(
        self,
        axis_object_list: Iterable[CollectionObjectName],
        surface_list: Iterable[CollectionObjectName],
        resultant_group_name: CollectionObjectName,
        *,
        point_suffix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAtIntersectionOfPrincipalObjectAxesAndSurfaces",
            "construction_operations.construct_points_at_intersection_of_principal_object_axes_and_surfaces",
            {
                "axis_object_list": axis_object_list,
                "surface_list": surface_list,
                "point_suffix": point_suffix,
                "resultant_group_name": resultant_group_name,
            },
            None,
        )
        return None

    async def construct_points_at_projection_on_surfaces_parallel_to_wcf_axis(
        self,
        surface_list: Iterable[CollectionObjectName],
        point_names: Iterable[PointName],
        axis: WcfAxis,
        *,
        group_name_to_contain_new_points: str = "",
        point_name_prefix: str = "",
        point_name_suffix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAtProjectionOnSurfacesParallelToWcfAxis",
            "construction_operations.construct_points_at_projection_on_surfaces_parallel_to_wcf_axis",
            {
                "surface_list": surface_list,
                "point_names": point_names,
                "group_name_to_contain_new_points": group_name_to_contain_new_points,
                "point_name_prefix": point_name_prefix,
                "point_name_suffix": point_names,
                "axis": axis,
            },
            None,
        )
        return None

    async def construct_points_at_projection_on_surfaces_radial_from_wcf_axis(
        self,
        surface_list: Iterable[CollectionObjectName],
        point_names: Iterable[PointName],
        axis: WcfAxis,
        *,
        group_name_to_contain_new_points: str = "",
        point_name_prefix: str = "",
        point_name_suffix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAtProjectionOnSurfacesRadialFromWcfAxis",
            "construction_operations.construct_points_at_projection_on_surfaces_radial_from_wcf_axis",
            {
                "surface_list": surface_list,
                "point_names": point_names,
                "group_name_to_contain_new_points": group_name_to_contain_new_points,
                "point_name_prefix": point_name_prefix,
                "point_name_suffix": point_names,
                "axis": axis,
            },
            None,
        )
        return None

    async def construct_points_at_projection_on_surfaces_spherical_from_wcf_origin(
        self,
        surface_list: Iterable[CollectionObjectName],
        point_names: Iterable[PointName],
        *,
        group_name_to_contain_new_points: str = "",
        point_name_prefix: str = "",
        point_name_suffix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAtProjectionOnSurfacesSphericalFromWcfOrigin",
            "construction_operations.construct_points_at_projection_on_surfaces_spherical_from_wcf_origin",
            {
                "surface_list": surface_list,
                "point_names": point_names,
                "group_name_to_contain_new_points": group_name_to_contain_new_points,
                "point_name_prefix": point_name_prefix,
                "point_name_suffix": point_names,
            },
            None,
        )
        return None

    async def construct_points_auto_correspond_two_groups_inter_point_distance(
        self,
        reference_group: CollectionObjectName,
        group_to_be_copied: CollectionObjectName,
        group_to_contain_matched_points: CollectionObjectName,
        *,
        same_point_tolerance: float = 0.1,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAutoCorrespondTwoGroupsInterPointDistance",
            "construction_operations.construct_points_auto_correspond_two_groups_inter_point_distance",
            {
                "reference_group": reference_group,
                "group_to_be_copied": group_to_be_copied,
                "same_point_tolerance": same_point_tolerance,
                "group_to_contain_matched_points": group_to_contain_matched_points,
            },
            None,
        )
        return None

    async def construct_points_auto_correspond_two_groups_proximity(
        self,
        reference_group: CollectionObjectName,
        group_to_be_copied: CollectionObjectName,
        group_to_contain_matched_points: CollectionObjectName,
        *,
        same_point_tolerance: float = 0.25,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsAutoCorrespondTwoGroupsProximity",
            "construction_operations.construct_points_auto_correspond_two_groups_proximity",
            {
                "reference_group": reference_group,
                "group_to_be_copied": group_to_be_copied,
                "same_point_tolerance": same_point_tolerance,
                "group_to_contain_matched_points": group_to_contain_matched_points,
            },
            None,
        )
        return None

    async def construct_points_by_projecting_points_on_mesh_along_direction(
        self,
        reference_point_names: Iterable[PointName],
        group_name_for_projected_points: CollectionObjectName,
        object_providing_direction_reference: CollectionObjectName,
        mesh_serving_as_projection_target: CollectionObjectName,
        *,
        bi_directional_projection: bool = True,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructPointsByProjectingPointsOnMeshAlongDirection",
                "construction_operations.construct_points_by_projecting_points_on_mesh_along_direction",
                {
                    "reference_point_names": reference_point_names,
                    "group_name_for_projected_points": group_name_for_projected_points,
                    "object_providing_direction_reference": object_providing_direction_reference,
                    "bi_directional_projection": bi_directional_projection,
                    "mesh_serving_as_projection_target": mesh_serving_as_projection_target,
                },
                None,
            ),
        )

    async def construct_points_cylindrically_shifted(
        self,
        reference_object_name: CollectionObjectName,
        original_points: Iterable[PointName],
        group_for_new_points: CollectionObjectName,
        *,
        radial_shift: float = 0.0,
        theta_shift_degrees: float = 0.0,
        planar_shift: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsCylindricallyShifted",
            "construction_operations.construct_points_cylindrically_shifted",
            {
                "reference_object_name": reference_object_name,
                "original_points": original_points,
                "group_for_new_points": group_for_new_points,
                "radial_shift": radial_shift,
                "theta_shift_degrees": theta_shift_degrees,
                "planar_shift": planar_shift,
            },
            None,
        )
        return None

    async def construct_points_from_cylinder(
        self,
        cylinder_name: CollectionObjectName,
        group_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsFromCylinder",
            "construction_operations.construct_points_from_cylinder",
            {
                "cylinder_name": cylinder_name,
                "group_name": group_name,
            },
            None,
        )
        return None

    async def construct_points_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_points_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_points_from_surfaces_on_uv_grid(
        self,
        surface_list: Iterable[CollectionObjectName],
        *,
        uv_point_group_base_name: str = "UV Points",
        make_each_line_separate_group: bool = False,
        number_of_u_grids: int = 5,
        number_of_v_grids: int = 5,
        edge_point_mode: EdgePointMode = EdgePointMode.INCLUDE_EDGES,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsFromSurfacesOnUvGrid",
            "construction_operations.construct_points_from_surfaces_on_uv_grid",
            {
                "surface_list": surface_list,
                "uv_point_group_base_name": uv_point_group_base_name,
                "make_each_line_separate_group": make_each_line_separate_group,
                "number_of_u_grids": number_of_u_grids,
                "number_of_v_grids": number_of_v_grids,
                "edge_point_mode": edge_point_mode,
            },
            None,
        )
        return None

    async def construct_points_layout_on_grid(
        self,
        group_name: CollectionObjectName,
        *,
        point_prefix: str = "p",
        x_min: float = 0.0,
        x_max: float = 100.0,
        x_count: int = 10,
        y_min: float = 0.0,
        y_max: float = 50.0,
        y_count: int = 10,
        z_min: float = 0.0,
        z_max: float = 0.0,
        z_count: int = 1,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsLayoutOnGrid",
            "construction_operations.construct_points_layout_on_grid",
            {
                "group_name": group_name,
                "point_prefix": point_prefix,
                "x_min": x_min,
                "x_max": x_max,
                "x_count": x_count,
                "y_min": y_min,
                "y_max": y_max,
                "y_count": y_count,
                "z_min": z_min,
                "z_max": z_max,
                "z_count": z_count,
            },
            None,
        )
        return None

    async def construct_points_n_spaced_on_curves(
        self,
        b_spline_list: Iterable[CollectionObjectName],
        resultant_group_name: CollectionObjectName,
        *,
        number_of_evenly_spaced_points: int = 10,
        resultant_point_name_prefix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsNSpacedOnCurves",
            "construction_operations.construct_points_n_spaced_on_curves",
            {
                "b_spline_list": b_spline_list,
                "number_of_evenly_spaced_points": number_of_evenly_spaced_points,
                "resultant_group_name": resultant_group_name,
                "resultant_point_name_prefix": resultant_point_name_prefix,
            },
            None,
        )
        return None

    async def construct_points_on_curves_using_max_chordal_deviation(
        self,
        b_spline_list: Iterable[CollectionObjectName],
        resultant_group_name: CollectionObjectName,
        *,
        maximum_chordal_deviation: float = 0.05,
        maximum_trim_edge_angle: float = 15.0,
        maximum_chord_length: float = 0.0,
        resultant_point_name_prefix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsOnCurvesUsingMaxChordalDeviation",
            "construction_operations.construct_points_on_curves_using_max_chordal_deviation",
            {
                "b_spline_list": b_spline_list,
                "maximum_chordal_deviation": maximum_chordal_deviation,
                "maximum_trim_edge_angle": maximum_trim_edge_angle,
                "maximum_chord_length": maximum_chord_length,
                "resultant_group_name": resultant_group_name,
                "resultant_point_name_prefix": resultant_point_name_prefix,
            },
            None,
        )
        return None

    async def construct_points_on_object_vertices(
        self,
        object_name_list: Iterable[CollectionObjectName],
        resultant_group_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsOnObjectVertices",
            "construction_operations.construct_points_on_object_vertices",
            {
                "object_name_list": object_name_list,
                "resultant_group_name": resultant_group_name,
            },
            None,
        )
        return None

    async def construct_points_on_surfaces_by_clicking(
        self,
        group_name_for_points: CollectionObjectName,
        *,
        first_point_name: str = "p0",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsOnSurfacesByClicking",
            "construction_operations.construct_points_on_surfaces_by_clicking",
            {
                "group_name_for_points": group_name_for_points,
                "first_point_name": first_point_name,
            },
            None,
        )
        return None

    async def construct_points_shifted_in_working_frame(
        self,
        original_points: Iterable[PointName],
        group_for_new_points: CollectionObjectName,
        *,
        shift_vector: Vector | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsShiftedInWorkingFrame",
            "construction_operations.construct_points_shifted_in_working_frame",
            {
                "original_points": original_points,
                "group_for_new_points": group_for_new_points,
                "shift_vector": shift_vector,
            },
            None,
        )
        return None

    async def construct_points_spaced_at_distance_on_curves(
        self,
        b_spline_list: Iterable[CollectionObjectName],
        resultant_group_name: CollectionObjectName,
        *,
        distance_between_points: float = 0.5,
        resultant_point_name_prefix: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsSpacedAtDistanceOnCurves",
            "construction_operations.construct_points_spaced_at_distance_on_curves",
            {
                "b_spline_list": b_spline_list,
                "distance_between_points": distance_between_points,
                "resultant_group_name": resultant_group_name,
                "resultant_point_name_prefix": resultant_point_name_prefix,
            },
            None,
        )
        return None

    async def construct_points_subset_with_greatest_spacing(
        self,
        points_to_subsample: Iterable[PointName],
        *,
        subset_size: int = 10,
        group_for_subset: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsSubsetWithGreatestSpacing",
            "construction_operations.construct_points_subset_with_greatest_spacing",
            {
                "points_to_subsample": points_to_subsample,
                "subset_size": subset_size,
                "group_for_subset": group_for_subset,
            },
            None,
        )
        return None

    async def construct_points_wildcard_selection(
        self,
        groups_to_select_from: Iterable[CollectionObjectName],
        wildcard_selection_names: PointName,
        group_for_new_points: CollectionObjectName,
        *,
        include_prior_complete_name: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPointsWildcardSelection",
            "construction_operations.construct_points_wildcard_selection",
            {
                "groups_to_select_from": groups_to_select_from,
                "wildcard_selection_names": wildcard_selection_names,
                "group_for_new_points": group_for_new_points,
                "include_prior_complete_name": include_prior_complete_name,
            },
            None,
        )
        return None

    async def construct_sphere(
        self,
        sphere_name: CollectionObjectName,
        sphere_center_in_working_coordinates: Vector,
        sphere_radius: float,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSphere",
            "construction_operations.construct_sphere",
            {
                "sphere_name": sphere_name,
                "sphere_center_in_working_coordinates": sphere_center_in_working_coordinates,
                "sphere_radius": sphere_radius,
            },
            None,
        )
        return None

    async def construct_spheres_from_surface_faces_runtime_select(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSpheresFromSurfaceFacesRuntimeSelect",
            "construction_operations.construct_spheres_from_surface_faces_runtime_select",
            {},
            None,
        )
        return None

    async def construct_surface_by_dissecting_surfaces(
        self,
        dissection_mode: SurfaceDissectionMode,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructSurfaceByDissectingSurfaces",
                "construction_operations.construct_surface_by_dissecting_surfaces",
                {
                    "dissection_mode": dissection_mode,
                },
                None,
            ),
        )

    async def construct_surface_by_offsetting_surface(
        self,
        reference_surface: Iterable[CollectionObjectName],
        *,
        surface_offset: float = 0.0,
        hide_original_surface: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceByOffsettingSurface",
            "construction_operations.construct_surface_by_offsetting_surface",
            {
                "reference_surface": reference_surface,
                "surface_offset": surface_offset,
                "hide_original_surface": hide_original_surface,
            },
            None,
        )
        return None

    async def construct_surface_fit_from_nominal_surfaces_and_actual_data(
        self,
        nominal_surface: CollectionObjectName,
        actual_data_point_list: Iterable[PointName],
        resulting_surface_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFitFromNominalSurfacesAndActualData",
            "construction_operations.construct_surface_fit_from_nominal_surfaces_and_actual_data",
            {
                "nominal_surface": nominal_surface,
                "actual_data_point_list": actual_data_point_list,
                "resulting_surface_name": resulting_surface_name,
            },
            None,
        )
        return None

    async def construct_surface_from_annotation_links(
        self,
        annotation_list: Iterable[CollectionObjectName],
        resulting_surface_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromAnnotationLinks",
            "construction_operations.construct_surface_from_annotation_links",
            {
                "annotation_list": annotation_list,
                "resulting_surface_name": resulting_surface_name,
            },
            None,
        )
        return None

    async def construct_surface_from_b_splines(
        self,
        resulting_surface_name: CollectionObjectName,
        b_spline_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromBSplines",
            "construction_operations.construct_surface_from_b_splines",
            {
                "resulting_surface_name": resulting_surface_name,
                "b_spline_list": b_spline_list,
            },
            None,
        )
        return None

    async def construct_surface_from_collection_of_surfaces(
        self,
        surfaces_to_combine: Iterable[CollectionObjectName],
        resulting_surface_name: CollectionObjectName,
        *,
        hide_original_surfaces: bool = True,
        delete_original_surfaces: bool = False,
        enable_sewing_tolerance: bool = False,
        sewing_tolerance: float = -1.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromCollectionOfSurfaces",
            "construction_operations.construct_surface_from_collection_of_surfaces",
            {
                "surfaces_to_combine": surfaces_to_combine,
                "resulting_surface_name": resulting_surface_name,
                "hide_original_surfaces": hide_original_surfaces,
                "delete_original_surfaces": delete_original_surfaces,
                "enable_sewing_tolerance": enable_sewing_tolerance,
                "sewing_tolerance": sewing_tolerance,
            },
            None,
        )
        return None

    async def construct_surface_from_cone(
        self,
        resulting_surface_name: CollectionObjectName,
        cone_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromCone",
            "construction_operations.construct_surface_from_cone",
            {
                "resulting_surface_name": resulting_surface_name,
                "cone_name": cone_name,
            },
            None,
        )
        return None

    async def construct_surface_from_cylinder(
        self,
        resulting_surface_name: CollectionObjectName,
        cylinder_name: CollectionObjectName,
        *,
        internal_cylinder: bool = True,
        use_theta_extent_mode: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromCylinder",
            "construction_operations.construct_surface_from_cylinder",
            {
                "resulting_surface_name": resulting_surface_name,
                "cylinder_name": cylinder_name,
                "internal_cylinder": internal_cylinder,
                "use_theta_extent_mode": use_theta_extent_mode,
            },
            None,
        )
        return None

    async def construct_surface_from_plane(
        self,
        resulting_surface_name: CollectionObjectName,
        plane_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromPlane",
            "construction_operations.construct_surface_from_plane",
            {
                "resulting_surface_name": resulting_surface_name,
                "plane_name": plane_name,
            },
            None,
        )
        return None

    async def construct_surface_from_point_groups(
        self,
        group_name_list: Iterable[CollectionObjectName],
        resulting_surface_name: CollectionObjectName,
        *,
        b_spline_fit_options: BSplineFitOptions | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromPointGroups",
            "construction_operations.construct_surface_from_point_groups",
            {
                "group_name_list": group_name_list,
                "b_spline_fit_options": b_spline_fit_options,
                "resulting_surface_name": resulting_surface_name,
            },
            None,
        )
        return None

    async def construct_surface_from_sphere(
        self,
        resulting_surface_name: CollectionObjectName,
        sphere_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfaceFromSphere",
            "construction_operations.construct_surface_from_sphere",
            {
                "resulting_surface_name": resulting_surface_name,
                "sphere_name": sphere_name,
            },
            None,
        )
        return None

    async def construct_surfaces_by_dissecting_surfaces_from_ref_list(
        self,
        surfaces_to_dissect: Iterable[CollectionObjectName],
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructSurfacesByDissectingSurfacesFromRefList",
                "construction_operations.construct_surfaces_by_dissecting_surfaces_from_ref_list",
                {
                    "surfaces_to_dissect": surfaces_to_dissect,
                },
                None,
            ),
        )

    async def construct_surfaces_by_projecting_points(
        self,
        projection_target_name_list: Iterable[CollectionObjectName],
        point_list: Iterable[PointName],
        resulting_surface_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfacesByProjectingPoints",
            "construction_operations.construct_surfaces_by_projecting_points",
            {
                "projection_target_name_list": projection_target_name_list,
                "point_list": point_list,
                "resulting_surface_name": resulting_surface_name,
            },
            None,
        )
        return None

    async def construct_surfaces_from_objects(
        self,
        objects: Iterable[CollectionObjectName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructSurfacesFromObjects",
            "construction_operations.construct_surfaces_from_objects",
            {
                "objects": objects,
            },
            None,
        )
        return None

    async def construct_vector_group_area_profile_check(
        self,
        reference_vectors: Iterable[VectorName],
        vector_groups_to_check: Iterable[CollectionVectorGroupName],
        resultant_vector_group_name: CollectionVectorGroupName,
        *,
        area_radius: float = 0.0,
        area_tolerance: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructVectorGroupAreaProfileCheck",
            "construction_operations.construct_vector_group_area_profile_check",
            {
                "reference_vectors": reference_vectors,
                "vector_groups_to_check": vector_groups_to_check,
                "area_radius": area_radius,
                "area_tolerance": area_tolerance,
                "resultant_vector_group_name": resultant_vector_group_name,
            },
            None,
        )
        return None

    async def construct_vector_group_from_relationship(
        self,
        relationship_name: CollectionObjectName,
        vector_group_name: CollectionVectorGroupName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructVectorGroupFromRelationship",
            "construction_operations.construct_vector_group_from_relationship",
            {
                "relationship_name": relationship_name,
                "vector_group_name": vector_group_name,
            },
            None,
        )
        return None

    async def construct_vector_group_from_vector_name_ref_list(
        self,
        vector_name_list: Iterable[VectorName],
        resultant_vector_group_name: CollectionVectorGroupName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructVectorGroupFromVectorNameRefList",
            "construction_operations.construct_vector_group_from_vector_name_ref_list",
            {
                "vector_name_list": vector_name_list,
                "resultant_vector_group_name": resultant_vector_group_name,
            },
            None,
        )
        return None

    async def construct_vector_group_group_to_group_compare(
        self,
        vector_group_name: CollectionObjectName,
        group_a: CollectionObjectName,
        group_b: CollectionObjectName,
        *,
        rms_deviation_tolerance: float = 0.0,
        max_absolute_deviation_tolerance: float = 0.0,
        average_deviation_tolerance: float = 0.0,
    ) -> ConstructVectorGroupGroupToGroupCompareResult:
        return cast(
            ConstructVectorGroupGroupToGroupCompareResult,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructVectorGroupGroupToGroupCompare",
                "construction_operations.construct_vector_group_group_to_group_compare",
                {
                    "vector_group_name": vector_group_name,
                    "group_a": group_a,
                    "group_b": group_b,
                    "rms_deviation_tolerance": rms_deviation_tolerance,
                    "max_absolute_deviation_tolerance": max_absolute_deviation_tolerance,
                    "average_deviation_tolerance": average_deviation_tolerance,
                },
                ConstructVectorGroupGroupToGroupCompareResult,
            ),
        )

    async def construct_vector_in_working_coordinates_begin_delta(
        self,
        vector_group_name: CollectionObjectName,
        new_vector_name: str,
        begin_in_working_coordinates: Vector,
        delta_in_working_coordinates: Vector,
        *,
        is_magnitude_negative: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructVectorInWorkingCoordinatesBeginDelta",
            "construction_operations.construct_vector_in_working_coordinates_begin_delta",
            {
                "vector_group_name": vector_group_name,
                "new_vector_name": new_vector_name,
                "begin_in_working_coordinates": begin_in_working_coordinates,
                "delta_in_working_coordinates": delta_in_working_coordinates,
                "is_magnitude_negative": is_magnitude_negative,
            },
            None,
        )
        return None

    async def construct_vector_in_working_coordinates_begin_direction_magnitude(
        self,
        vector_group_name: CollectionObjectName,
        new_vector_name: str,
        begin_in_working_coordinates: Vector,
        direction_in_working_coordinates: Vector,
        *,
        signed_magnitude: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructVectorInWorkingCoordinatesBeginDirectionMagnitude",
            "construction_operations.construct_vector_in_working_coordinates_begin_direction_magnitude",
            {
                "vector_group_name": vector_group_name,
                "new_vector_name": new_vector_name,
                "begin_in_working_coordinates": begin_in_working_coordinates,
                "direction_in_working_coordinates": direction_in_working_coordinates,
                "signed_magnitude": signed_magnitude,
            },
            None,
        )
        return None

    async def copy_groups_excluding_obscured_points(
        self,
        instrument_id: CollectionInstrumentId,
        group_names: Iterable[CollectionObjectName],
        new_collection_name: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CopyGroupsExcludingObscuredPoints",
            "construction_operations.copy_groups_excluding_obscured_points",
            {
                "instrument_id": instrument_id,
                "group_names": group_names,
                "new_collection_name": new_collection_name,
            },
            None,
        )
        return None

    async def create_hidden_point(
        self,
        end_a_point_name: PointName,
        end_b_point_name: PointName,
        point_name_to_create: PointName,
        *,
        hidden_point_rod_index: int = 0,
        overwrite_existing_point: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreateHiddenPoint",
            "construction_operations.create_hidden_point",
            {
                "end_a_point_name": end_a_point_name,
                "end_b_point_name": end_b_point_name,
                "hidden_point_rod_index": hidden_point_rod_index,
                "overwrite_existing_point": overwrite_existing_point,
                "point_name_to_create": point_name_to_create,
            },
            None,
        )
        return None

    async def create_hidden_point_rod(
        self,
        hidden_point_rod_name: str,
        *,
        target_to_target_distance: float = 0.0,
        target_to_tip_distance: float = 0.0,
        inter_point_tolerance: float = 0.0,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "CreateHiddenPointRod",
                "construction_operations.create_hidden_point_rod",
                {
                    "hidden_point_rod_name": hidden_point_rod_name,
                    "target_to_target_distance": target_to_target_distance,
                    "target_to_tip_distance": target_to_tip_distance,
                    "inter_point_tolerance": inter_point_tolerance,
                },
                None,
            ),
        )

    async def create_min_max_vector_group_callout(
        self,
        destination_callout_view: CollectionItemName,
        vector_group_name: CollectionObjectName,
        *,
        number_of_vectors_with_highest_mag: int = 1,
        number_of_vectors_with_lowest_mag: int = 1,
        show_collection: bool = False,
        show_vector_group: bool = False,
        show_vector_name: bool = True,
        show_dx: bool = False,
        show_dy: bool = False,
        show_dz: bool = False,
        show_d_mag: bool = True,
        show_tolerance_color: bool = True,
        tolerance_color_blue_green_red: bool = False,
        show_out_of_tolerance_value: bool = True,
        show_tolerance_range: bool = False,
        show_vector_color: bool = True,
        show_start_point: bool = False,
        show_end_point: bool = False,
        show_units: bool = False,
        attach_callout_to_end_point: bool = True,
        use_default_placement: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreateMinMaxVectorGroupCallout",
            "construction_operations.create_min_max_vector_group_callout",
            {
                "destination_callout_view": destination_callout_view,
                "vector_group_name": vector_group_name,
                "number_of_vectors_with_highest_mag": number_of_vectors_with_highest_mag,
                "number_of_vectors_with_lowest_mag": number_of_vectors_with_lowest_mag,
                "show_collection": show_collection,
                "show_vector_group": show_vector_group,
                "show_vector_name": show_vector_name,
                "show_dx": show_dx,
                "show_dy": show_dy,
                "show_dz": show_dz,
                "show_d_mag": show_d_mag,
                "show_tolerance_color": show_tolerance_color,
                "tolerance_color_blue_green_red": tolerance_color_blue_green_red,
                "show_out_of_tolerance_value": show_out_of_tolerance_value,
                "show_tolerance_range": show_tolerance_range,
                "show_vector_color": show_vector_color,
                "show_start_point": show_start_point,
                "show_end_point": show_end_point,
                "show_units": show_units,
                "attach_callout_to_end_point": attach_callout_to_end_point,
                "use_default_placement": use_default_placement,
            },
            None,
        )
        return None

    async def create_picture_callout(
        self,
        destination_callout_view: CollectionItemName,
        picture_name: CollectionItemName,
        *,
        view_x_position: float = 0.4,
        view_y_position: float = 0.6,
        scale_image_percent: int = 100,
        object_for_callout_anchor_point: CollectionObjectName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreatePictureCallout",
            "construction_operations.create_picture_callout",
            {
                "destination_callout_view": destination_callout_view,
                "picture_name": picture_name,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "scale_image_percent": scale_image_percent,
                "object_for_callout_anchor_point": object_for_callout_anchor_point,
            },
            None,
        )
        return None

    async def create_point_callout(
        self,
        destination_callout_view: CollectionItemName,
        point: PointName,
        *,
        view_x_position: float = 0.0,
        view_y_position: float = 0.0,
        show_point_collection: bool = False,
        show_point_group: bool = True,
        show_point_target: bool = True,
        show_x: bool = True,
        show_y: bool = True,
        show_z: bool = True,
        show_units: bool = False,
        show_ux: bool = False,
        show_uy: bool = False,
        show_uz: bool = False,
        show_u_mag: bool = False,
        desired_coordinate_system: CoordinateSystemType = CoordinateSystemType.CARTESIAN,
        notes: Iterable[str] | None = None,
        use_default_placement: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreatePointCallout",
            "construction_operations.create_point_callout",
            {
                "destination_callout_view": destination_callout_view,
                "point": point,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "show_point_collection": show_point_collection,
                "show_point_group": show_point_group,
                "show_point_target": show_point_target,
                "show_x_r": show_x,
                "show_y_theta": show_y,
                "show_z_phi": show_z,
                "show_units": show_units,
                "show_ux_ur": show_ux,
                "show_uy_utheta": show_uy,
                "show_uz_uphi": show_uz,
                "show_umag": show_u_mag,
                "desired_coordinate_system": desired_coordinate_system,
                "notes": notes,
                "use_default_placement": use_default_placement,
            },
            None,
        )
        return None

    async def create_point_comparison_callout(
        self,
        destination_callout_view: CollectionItemName,
        first_point: PointName,
        second_point: PointName,
        *,
        view_x_position: float = 0.0,
        view_y_position: float = 0.0,
        show_first_point_collection: bool = False,
        show_first_point_group: bool = True,
        show_first_point_target: bool = True,
        show_first_point_coordinates: bool = False,
        show_second_point_collection: bool = False,
        show_second_point_group: bool = True,
        show_second_point_target: bool = True,
        show_second_point_coordinates: bool = False,
        show_dx: bool = True,
        show_dy: bool = True,
        show_dz: bool = True,
        show_d_mag: bool = True,
        additional_x_comments: str | None = None,
        additional_y_comments: str | None = None,
        additional_z_comments: str | None = None,
        additional_notes: Iterable[str] | None = None,
        use_default_placement: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreatePointComparisonCallout",
            "construction_operations.create_point_comparison_callout",
            {
                "destination_callout_view": destination_callout_view,
                "first_point": first_point,
                "second_point": second_point,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "show_first_point_collection": show_first_point_collection,
                "show_first_point_group": show_first_point_group,
                "show_first_point_target": show_first_point_target,
                "show_first_point_coordinates": show_first_point_coordinates,
                "show_second_point_collection": show_second_point_collection,
                "show_second_point_group": show_second_point_group,
                "show_second_point_target": show_second_point_target,
                "show_second_point_coordinates": show_second_point_coordinates,
                "show_dx": show_dx,
                "show_dy": show_dy,
                "show_dz": show_dz,
                "show_d_mag": show_d_mag,
                "additional_x_comments": additional_x_comments,
                "additional_y_comments": additional_y_comments,
                "additional_z_comments": additional_z_comments,
                "additional_notes": additional_notes,
                "use_default_placement": use_default_placement,
            },
            None,
        )
        return None

    async def create_relationship_callout(
        self,
        destination_callout_view: CollectionItemName,
        relationship_name: CollectionItemName,
        *,
        view_x_position: float = 0.0,
        view_y_position: float = 0.0,
        additional_notes: Iterable[str] | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreateRelationshipCallout",
            "construction_operations.create_relationship_callout",
            {
                "destination_callout_view": destination_callout_view,
                "relationship_name": relationship_name,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "additional_notes": additional_notes,
            },
            None,
        )
        return None

    async def create_text_callout(
        self,
        destination_callout_view: CollectionItemName,
        text: Iterable[str],
        *,
        view_x_position: float = 0.4,
        view_y_position: float = 0.6,
        callout_anchor_point: PointName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreateTextCallout",
            "construction_operations.create_text_callout",
            {
                "destination_callout_view": destination_callout_view,
                "text": text,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "callout_anchor_point": callout_anchor_point,
            },
            None,
        )
        return None

    async def create_vector_callout(
        self,
        destination_callout_view: CollectionItemName,
        vector_group_name: CollectionObjectName,
        vector_name: str,
        *,
        view_x_position: float = 0.0,
        view_y_position: float = 0.0,
        show_collection: bool = False,
        show_vector_group: bool = False,
        show_vector_name: bool = True,
        show_dx: bool = True,
        show_dy: bool = True,
        show_dz: bool = True,
        show_d_mag: bool = True,
        show_tolerance_color: bool = True,
        show_out_of_tolerance_value: bool = False,
        show_tolerance_range: bool = False,
        show_vector_color: bool = False,
        show_start_point: bool = False,
        show_end_point: bool = False,
        show_units: bool = False,
        additional_notes: Iterable[str] | None = None,
        attach_callout_to_end_point: bool = False,
        use_default_placement: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "CreateVectorCallout",
            "construction_operations.create_vector_callout",
            {
                "destination_callout_view": destination_callout_view,
                "vector_group_name": vector_group_name,
                "vector_name": vector_name,
                "view_x_position": view_x_position,
                "view_y_position": view_y_position,
                "show_collection": show_collection,
                "show_vector_group": show_vector_group,
                "show_vector_name": show_vector_name,
                "show_dx": show_dx,
                "show_dy": show_dy,
                "show_dz": show_dz,
                "show_d_mag": show_d_mag,
                "show_tolerance_color": show_tolerance_color,
                "show_out_of_tolerance_value": show_out_of_tolerance_value,
                "show_tolerance_range": show_tolerance_range,
                "show_vector_color": show_vector_color,
                "show_start_point": show_start_point,
                "show_end_point": show_end_point,
                "show_units": show_units,
                "additional_notes": additional_notes,
                "attach_callout_to_end_point": attach_callout_to_end_point,
                "use_default_placement": use_default_placement,
            },
            None,
        )
        return None

    async def decompose_transform_into_doubles_euler_xyz(
        self,
        input_transform: Transform,
    ) -> EulerXyzTransformComponents:
        return cast(
            EulerXyzTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoDoublesEulerXyz",
                "construction_operations.decompose_transform_into_doubles_euler_xyz",
                {
                    "input_transform": input_transform,
                },
                EulerXyzTransformComponents,
            ),
        )

    async def decompose_transform_into_doubles_euler_zxz(
        self,
        input_transform: Transform,
    ) -> EulerZxzTransformComponents:
        return cast(
            EulerZxzTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoDoublesEulerZxz",
                "construction_operations.decompose_transform_into_doubles_euler_zxz",
                {
                    "input_transform": input_transform,
                },
                EulerZxzTransformComponents,
            ),
        )

    async def decompose_transform_into_doubles_euler_zyx(
        self,
        input_transform: Transform,
    ) -> EulerZyxTransformComponents:
        return cast(
            EulerZyxTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoDoublesEulerZyx",
                "construction_operations.decompose_transform_into_doubles_euler_zyx",
                {
                    "input_transform": input_transform,
                },
                EulerZyxTransformComponents,
            ),
        )

    async def decompose_transform_into_doubles_euler_zyz(
        self,
        input_transform: Transform,
    ) -> EulerZyzTransformComponents:
        return cast(
            EulerZyzTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoDoublesEulerZyz",
                "construction_operations.decompose_transform_into_doubles_euler_zyz",
                {
                    "input_transform": input_transform,
                },
                EulerZyzTransformComponents,
            ),
        )

    async def decompose_transform_into_doubles_fixed_xyz(
        self,
        input_transform: Transform,
    ) -> FixedXyzTransformComponents:
        return cast(
            FixedXyzTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoDoublesFixedXyz",
                "construction_operations.decompose_transform_into_doubles_fixed_xyz",
                {
                    "input_transform": input_transform,
                },
                FixedXyzTransformComponents,
            ),
        )

    async def decompose_transform_into_vectors_fixed_xyz(
        self,
        input_transform: Transform,
    ) -> FixedXyzTransformVectors:
        return cast(
            FixedXyzTransformVectors,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoVectorsFixedXyz",
                "construction_operations.decompose_transform_into_vectors_fixed_xyz",
                {
                    "input_transform": input_transform,
                },
                FixedXyzTransformVectors,
            ),
        )

    async def decompose_transform_into_vectors_origin_and_axes(
        self,
        transform: Transform,
    ) -> TransformAxes:
        return cast(
            TransformAxes,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeTransformIntoVectorsOriginAndAxes",
                "construction_operations.decompose_transform_into_vectors_origin_and_axes",
                {
                    "transform": transform,
                },
                TransformAxes,
            ),
        )

    async def decompose_world_transform_operator_into_doubles_fixed_xyz_in_world(
        self,
        input_world_transform_operator: WorldTransform,
    ) -> WorldFixedXyzTransformComponents:
        return cast(
            WorldFixedXyzTransformComponents,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeWorldTransformOperatorIntoDoublesFixedXyzInWorld",
                "construction_operations.decompose_world_transform_operator_into_doubles_fixed_xyz_in_world",
                {
                    "input_world_transform_operator": input_world_transform_operator,
                },
                WorldFixedXyzTransformComponents,
            ),
        )

    async def decompose_world_transform_operator_into_vectors_fixed_xyz_in_world(
        self,
        input_world_transform_operator: WorldTransform,
    ) -> WorldFixedXyzTransformVectors:
        return cast(
            WorldFixedXyzTransformVectors,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DecomposeWorldTransformOperatorIntoVectorsFixedXyzInWorld",
                "construction_operations.decompose_world_transform_operator_into_vectors_fixed_xyz_in_world",
                {
                    "input_world_transform_operator": input_world_transform_operator,
                },
                WorldFixedXyzTransformVectors,
            ),
        )

    async def delete_callout_view(
        self,
        callout_view: CollectionItemName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "DeleteCalloutView",
            "construction_operations.delete_callout_view",
            {
                "callout_view": callout_view,
            },
            None,
        )
        return None

    async def delete_collection(
        self,
        collection_name: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "DeleteCollection",
            "construction_operations.delete_collection",
            {
                "collection_name": collection_name,
            },
            None,
        )
        return None

    async def delete_collections_by_wildcard(
        self,
        search_string: str,
        *,
        case_sensitive_search: bool = True,
        allow_deleting_all_collections: bool = False,
    ) -> DeleteCollectionsByWildcardResult:
        return cast(
            DeleteCollectionsByWildcardResult,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DeleteCollectionsByWildcard",
                "construction_operations.delete_collections_by_wildcard",
                {
                    "search_string": search_string,
                    "case_sensitive_search": case_sensitive_search,
                    "allow_deleting_all_collections": allow_deleting_all_collections,
                },
                DeleteCollectionsByWildcardResult,
            ),
        )

    async def delete_folders_by_wildcard(
        self,
        search_string: str,
        *,
        case_sensitive_search: bool = True,
        allow_deleting_all_folders: bool = False,
    ) -> DeleteFoldersByWildcardResult:
        return cast(
            DeleteFoldersByWildcardResult,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "DeleteFoldersByWildcard",
                "construction_operations.delete_folders_by_wildcard",
                {
                    "search_string": search_string,
                    "case_sensitive_search": case_sensitive_search,
                    "allow_deleting_all_folders": allow_deleting_all_folders,
                },
                DeleteFoldersByWildcardResult,
            ),
        )

    async def delete_hidden_point_rod(
        self,
        *,
        hidden_point_rod_index: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "DeleteHiddenPointRod",
            "construction_operations.delete_hidden_point_rod",
            {
                "hidden_point_rod_index": hidden_point_rod_index,
            },
            None,
        )
        return None

    async def extract_sphere_centers_from_point_cloud(
        self,
        cloud_name: CollectionObjectName,
        group_name_for_points: CollectionObjectName,
        *,
        desired_diameter: float = 0.0,
        extraction_tolerance: float = 0.0,
        minimum_point_count: int = 50,
        perform_final_fit: bool = True,
        final_fit_cone_angle: float = 120.0,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ExtractSphereCentersFromPointCloud",
                "construction_operations.extract_sphere_centers_from_point_cloud",
                {
                    "cloud_name": cloud_name,
                    "desired_diameter": desired_diameter,
                    "extraction_tolerance": extraction_tolerance,
                    "minimum_point_count": minimum_point_count,
                    "group_name_for_points": group_name_for_points,
                    "perform_final_fit": perform_final_fit,
                    "final_fit_cone_angle": final_fit_cone_angle,
                },
                None,
            ),
        )

    async def get_collection_instrument_ref_list_variable(
        self,
        name: str,
    ) -> list[CollectionInstrumentId]:
        return cast(
            list[CollectionInstrumentId],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetCollectionInstrumentRefListVariable",
                "construction_operations.get_collection_instrument_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_hidden_point_rod_index_by_name(
        self,
        hidden_point_rod_name: str,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetHiddenPointRodIndexByName",
                "construction_operations.get_hidden_point_rod_index_by_name",
                {
                    "hidden_point_rod_name": hidden_point_rod_name,
                },
                None,
            ),
        )

    async def get_ith_callout_position_in_callout_view(
        self,
        callout_view: CollectionItemName,
        callout_view_index: int,
    ) -> CalloutPosition:
        return cast(
            CalloutPosition,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetIthCalloutPositionInCalloutView",
                "construction_operations.get_ith_callout_position_in_callout_view",
                {
                    "callout_view": callout_view,
                    "callout_view_index": callout_view,
                },
                CalloutPosition,
            ),
        )

    async def get_number_of_callouts_in_callout_view(
        self,
        callout_view: CollectionItemName,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetNumberOfCalloutsInCalloutView",
                "construction_operations.get_number_of_callouts_in_callout_view",
                {
                    "callout_view": callout_view,
                },
                None,
            ),
        )

    async def get_working_transform_of_object_fixed_xyz(
        self,
        object_name: CollectionObjectName,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetWorkingTransformOfObjectFixedXyz",
                "construction_operations.get_working_transform_of_object_fixed_xyz",
                {
                    "object_name": object_name,
                },
                None,
            ),
        )

    async def invert_transform(
        self,
        transform: Transform,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "InvertTransform",
                "construction_operations.invert_transform",
                {
                    "transform": transform,
                },
                None,
            ),
        )

    async def make_collection_instrument_id_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> CollectionInstrumentId:
        return cast(
            CollectionInstrumentId,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionInstrumentIdRuntimeSelect",
                "construction_operations.make_collection_instrument_id_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_collection_instrument_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[CollectionInstrumentId]:
        return cast(
            list[CollectionInstrumentId],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionInstrumentRefListRuntimeSelect",
                "construction_operations.make_collection_instrument_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_collection_item_name_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        item_wildcard_criteria: str = "*",
        item_type: ItemType = ItemType.ANY,
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionItemNameRefListWildcardSelection",
                "construction_operations.make_collection_item_name_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "item_wildcard_criteria": item_wildcard_criteria,
                    "item_type": item_type,
                },
                None,
            ),
        )

    async def make_collection_name_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> CollectionName:
        return cast(
            CollectionName,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionNameRuntimeSelect",
                "construction_operations.make_collection_name_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_by_type(
        self,
        collection: str,
        *,
        object_type: ObjectType = ObjectType.ANY,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRefListByType",
                "construction_operations.make_collection_object_name_ref_list_by_type",
                {
                    "collection": collection,
                    "object_type": object_type,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_by_type_and_color(
        self,
        collection: str,
        *,
        object_type: ObjectType = ObjectType.ANY,
        object_color: Color = Color(255, 0, 0),
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRefListByTypeAndColor",
                "construction_operations.make_collection_object_name_ref_list_by_type_and_color",
                {
                    "collection": collection,
                    "object_type": object_type,
                    "object_color": object_color,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_from_all_groups_in_collection(
        self,
        collection_name: CollectionName,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRefListFromAllGroupsInCollection",
                "construction_operations.make_collection_object_name_ref_list_from_all_groups_in_collection",
                {
                    "collection_name": collection_name,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
        object_type: ObjectType = ObjectType.ANY,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRefListRuntimeSelect",
                "construction_operations.make_collection_object_name_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                    "object_type": object_type,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        object_wildcard_criteria: str = "*",
        object_type: ObjectType = ObjectType.ANY,
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRefListWildcardSelection",
                "construction_operations.make_collection_object_name_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "object_wildcard_criteria": object_wildcard_criteria,
                    "object_type": object_type,
                },
                None,
            ),
        )

    async def make_collection_object_name_runtime_select(
        self,
        *,
        user_prompt: str = "",
        object_type: ObjectType = ObjectType.ANY,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameRuntimeSelect",
                "construction_operations.make_collection_object_name_runtime_select",
                {
                    "user_prompt": user_prompt,
                    "object_type": object_type,
                },
                None,
            ),
        )

    async def make_collection_vector_group_name_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[CollectionVectorGroupName]:
        return cast(
            list[CollectionVectorGroupName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionVectorGroupNameRefListRuntimeSelect",
                "construction_operations.make_collection_vector_group_name_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_event_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        event_wildcard_criteria: str = "*",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeEventRefListWildcardSelection",
                "construction_operations.make_event_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "event_wildcard_criteria": event_wildcard_criteria,
                },
                None,
            ),
        )

    async def make_picture_name_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePictureNameRefListRuntimeSelect",
                "construction_operations.make_picture_name_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_point_name_ref_list_from_group(
        self,
        group_name: CollectionObjectName,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePointNameRefListFromGroup",
                "construction_operations.make_point_name_ref_list_from_group",
                {
                    "group_name": group_name,
                },
                None,
            ),
        )

    async def make_point_name_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePointNameRefListRuntimeSelect",
                "construction_operations.make_point_name_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_point_name_ref_list_wildcard_select(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        group_name_wildcard_criteria: str = "*",
        point_name_wildcard_criteria: str = "*",
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePointNameRefListWildcardSelect",
                "construction_operations.make_point_name_ref_list_wildcard_select",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "group_name_wildcard_criteria": group_name_wildcard_criteria,
                    "point_name_wildcard_criteria": point_name_wildcard_criteria,
                },
                None,
            ),
        )

    async def make_point_name_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> PointName:
        return cast(
            PointName,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePointNameRuntimeSelect",
                "construction_operations.make_point_name_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_report_ref_list_from_collection(
        self,
        collection_name: CollectionName,
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeReportRefListFromCollection",
                "construction_operations.make_report_ref_list_from_collection",
                {
                    "collection_name": collection_name,
                },
                None,
            ),
        )

    async def make_report_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeReportRefListRuntimeSelect",
                "construction_operations.make_report_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_system_string(
        self,
        string_content: SystemString,
        *,
        format_string: str | None = None,
    ) -> str:
        return cast(
            str,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeSystemString",
                "construction_operations.make_system_string",
                {
                    "string_content": string_content,
                    "format_string": format_string,
                },
                None,
            ),
        )

    async def make_transform_from_doubles_euler_parameters(
        self,
        *,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        e1: float = 0,
        e2: float = 0,
        e3: float = 0,
        e4: float = 0,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeTransformFromDoublesEulerParameters",
                "construction_operations.make_transform_from_doubles_euler_parameters",
                {
                    "x": x,
                    "y": y,
                    "z": z,
                    "e1": e1,
                    "e2": e2,
                    "e3": e3,
                    "e4": e4,
                },
                None,
            ),
        )

    async def make_transform_from_doubles_fixed_xyz(
        self,
        *,
        x: float = 0,
        y: float = 0,
        z: float = 0,
        rx: float = 0,
        ry: float = 0,
        rz: float = 0,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeTransformFromDoublesFixedXyz",
                "construction_operations.make_transform_from_doubles_fixed_xyz",
                {
                    "x": x,
                    "y": y,
                    "z": z,
                    "rx": rx,
                    "ry": ry,
                    "rz": rz,
                },
                None,
            ),
        )

    async def make_vector_name_ref_list_from_vector_group(
        self,
        vector_group_name: CollectionObjectName,
    ) -> list[VectorName]:
        return cast(
            list[VectorName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeVectorNameRefListFromVectorGroup",
                "construction_operations.make_vector_name_ref_list_from_vector_group",
                {
                    "vector_group_name": vector_group_name,
                },
                None,
            ),
        )

    async def make_vector_name_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = " Select Vectors (ENTER when done) ",
    ) -> list[VectorName]:
        return cast(
            list[VectorName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeVectorNameRefListRuntimeSelect",
                "construction_operations.make_vector_name_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_vector_names_unique_in_vector_group(
        self,
        vector_group_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "MakeVectorNamesUniqueInVectorGroup",
            "construction_operations.make_vector_names_unique_in_vector_group",
            {
                "vector_group_name": vector_group_name,
            },
            None,
        )
        return None

    async def rename_callout_view(
        self,
        original_callout_view_name: CollectionItemName,
        new_callout_view_name: CollectionItemName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "RenameCalloutView",
            "construction_operations.rename_callout_view",
            {
                "original_callout_view_name": original_callout_view_name,
                "new_callout_view_name": new_callout_view_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def set_collection_instrument_ref_list_variable(
        self,
        name: str,
        value: Iterable[CollectionInstrumentId],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetCollectionInstrumentRefListVariable",
            "construction_operations.set_collection_instrument_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_ith_callout_position_in_callout_view(
        self,
        callout_view: CollectionItemName,
        callout_view_index: int,
        x_position: int,
        y_position: int,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetIthCalloutPositionInCalloutView",
            "construction_operations.set_ith_callout_position_in_callout_view",
            {
                "callout_view": callout_view,
                "callout_view_index": callout_view,
                "x_position": x_position,
                "y_position": y_position,
            },
            None,
        )
        return None

    async def set_or_construct_default_collection(
        self,
        collection_name: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetOrConstructDefaultCollection",
            "construction_operations.set_or_construct_default_collection",
            {
                "collection_name": collection_name,
            },
            None,
        )
        return None

    async def set_point_position_in_working_coordinates(
        self,
        point_name: PointName,
        position_in_working_coordinates: Vector,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetPointPositionInWorkingCoordinates",
            "construction_operations.set_point_position_in_working_coordinates",
            {
                "point_name": point_name,
                "position_in_working_coordinates": position_in_working_coordinates,
            },
            None,
        )
        return None

    async def shift_plane(
        self,
        plane: CollectionObjectName,
        *,
        shift_along_normal: float = 0.0,
        grow_bounds_by_factor: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ShiftPlane",
            "construction_operations.shift_plane",
            {
                "plane": plane,
                "shift_along_normal": shift_along_normal,
                "grow_bounds_by_factor": grow_bounds_by_factor,
            },
            None,
        )
        return None

    async def transform_points_by_delta_about_working_frame(
        self,
        point_name_list: Iterable[PointName],
        delta_in_working_coordinates: Vector,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "TransformPointsByDeltaAboutWorkingFrame",
            "construction_operations.transform_points_by_delta_about_working_frame",
            {
                "point_name_list": point_name_list,
                "delta_in_working_coordinates": delta_in_working_coordinates,
            },
            None,
        )
        return None

    async def add_collection_instruments_to_ref_list_wildcard_selection(
        self,
        collection_instrument_ref_list: Iterable[CollectionInstrumentId],
        *,
        collection_wildcard_criteria: str = "*",
        instrument_wildcard_criteria: str = "*",
    ) -> list[CollectionInstrumentId]:
        return cast(
            list[CollectionInstrumentId],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "AddCollectionInstrumentsToRefListWildcardSelection",
                "construction_operations.add_collection_instruments_to_ref_list_wildcard_selection",
                {
                    "collection_instrument_ref_list": collection_instrument_ref_list,
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "instrument_wildcard_criteria": instrument_wildcard_criteria,
                },
                None,
            ),
        )

    async def average_set_of_groups(
        self,
        group_names: Iterable[CollectionObjectName],
        resulting_group_name: CollectionObjectName,
        *,
        rms_tolerance: float = 0.0,
        maximum_absolute_tolerance: float = 0.0,
        maximum_average_tolerance: float = 0.0,
    ) -> GroupAverageResult:
        return cast(
            GroupAverageResult,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "AverageSetOfGroups",
                "construction_operations.average_set_of_groups",
                {
                    "group_names": group_names,
                    "resulting_group_name": resulting_group_name,
                    "rms_tolerance": rms_tolerance,
                    "maximum_absolute_tolerance": maximum_absolute_tolerance,
                    "maximum_average_tolerance": maximum_average_tolerance,
                },
                None,
            ),
        )

    async def construct_geometry_from_surfaces(
        self,
        surfaces: Iterable[CollectionObjectName],
        *,
        minimum_diameter: float = 0.0,
        maximum_diameter: float = 0.0,
        reference_frame: CollectionObjectName | None = None,
        destination_collection_name: CollectionName | None = None,
        base_name: str = "Geometry Object",
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructGeometryFromSurfaces",
                "construction_operations.construct_geometry_from_surfaces",
                {
                    "surfaces": surfaces,
                    "minimum_diameter": minimum_diameter,
                    "maximum_diameter": maximum_diameter,
                    "reference_frame": reference_frame,
                    "destination_collection_name": destination_collection_name,
                    "base_name": base_name,
                },
                None,
            ),
        )

    async def construct_point_at_object_origin(
        self,
        object_name: CollectionObjectName,
        resultant_point_name: PointName,
    ) -> ObjectOriginResult:
        return cast(
            ObjectOriginResult,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "ConstructPointAtObjectOrigin",
                "construction_operations.construct_point_at_object_origin",
                {
                    "object_name": object_name,
                    "resultant_point_name": resultant_point_name,
                },
                None,
            ),
        )

    async def get_gradient_at_projected_point_on_surface(
        self,
        point_to_project: PointName,
        surface_name: CollectionObjectName,
        *,
        generate_output_vector_lines: bool = False,
    ) -> ProjectedPointGradient:
        return cast(
            ProjectedPointGradient,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetGradientAtProjectedPointOnSurface",
                "construction_operations.get_gradient_at_projected_point_on_surface",
                {
                    "point_to_project": point_to_project,
                    "surface_name": surface_name,
                    "generate_output_vector_lines": generate_output_vector_lines,
                },
                None,
            ),
        )

    async def get_gradient_at_projected_point_on_surface_edge(
        self,
        point_to_project: PointName,
        surface_edge_b_spline: CollectionObjectName,
        surface_name: CollectionObjectName,
        *,
        edge_offset_direction: Vector | None = None,
        edge_offset_distance: float = 0.01,
        generate_output_vector_lines: bool = False,
    ) -> ProjectedPointGradient:
        return cast(
            ProjectedPointGradient,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "GetGradientAtProjectedPointOnSurfaceEdge",
                "construction_operations.get_gradient_at_projected_point_on_surface_edge",
                {
                    "point_to_project": point_to_project,
                    "surface_edge_b_spline": surface_edge_b_spline,
                    "surface_name": surface_name,
                    "edge_offset_direction": edge_offset_direction,
                    "edge_offset_distance": edge_offset_distance,
                    "generate_output_vector_lines": generate_output_vector_lines,
                },
                None,
            ),
        )

    async def make_callout_view_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        callout_view_wildcard_criteria: str = "*",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCalloutViewRefListWildcardSelection",
                "construction_operations.make_callout_view_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "callout_view_wildcard_criteria": callout_view_wildcard_criteria,
                },
                None,
            ),
        )

    async def make_collection_object_name_ensure_unique(
        self,
        collection_object_name: CollectionObjectName,
        *,
        use_number_suffix: bool = False,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeCollectionObjectNameEnsureUnique",
                "construction_operations.make_collection_object_name_ensure_unique",
                {
                    "collection_object_name": collection_object_name,
                    "use_number_suffix": use_number_suffix,
                },
                None,
            ),
        )

    async def make_point_name_ensure_unique(
        self,
        point_name: PointName,
        *,
        use_number_suffix: bool = False,
    ) -> PointName:
        return cast(
            PointName,
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakePointNameEnsureUnique",
                "construction_operations.make_point_name_ensure_unique",
                {
                    "point_name": point_name,
                    "use_number_suffix": use_number_suffix,
                },
                None,
            ),
        )

    async def make_relationship_ref_list_runtime_select(
        self,
        *,
        user_prompt: str = "",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeRelationshipRefListRuntimeSelect",
                "construction_operations.make_relationship_ref_list_runtime_select",
                {
                    "user_prompt": user_prompt,
                },
                None,
            ),
        )

    async def make_relationship_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        relationship_wildcard_criteria: str = "*",
    ) -> list[CollectionItemName]:
        return cast(
            list[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.ConstructionOperations",
                "MakeRelationshipRefListWildcardSelection",
                "construction_operations.make_relationship_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "relationship_wildcard_criteria": relationship_wildcard_criteria,
                },
                None,
            ),
        )

    async def set_default_callout_view_properties(
        self,
        *,
        default_callout_view_name: str = "Callout 1",
        properties: CalloutViewProperties | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetDefaultCalloutViewProperties",
            "construction_operations.set_default_callout_view_properties",
            {
                "default_callout_view_name": default_callout_view_name,
                "properties": properties,
            },
            None,
        )
        return None

    async def set_callout_view_properties(
        self,
        callout_views: Iterable[CollectionItemName],
        *,
        properties: CalloutViewProperties | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "SetCalloutViewProperties",
            "construction_operations.set_callout_view_properties",
            {
                "callout_views": callout_views,
                "properties": properties,
            },
            None,
        )
        return None

    async def construct_polygonized_surface_from_point_clouds(
        self,
        point_cloud_list: Iterable[CollectionObjectName],
        mesh_orientation: MeshOrientationType,
        polygonized_surface_name: CollectionObjectName,
        *,
        grid_resolution: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructPolygonizedSurfaceFromPointClouds",
            "construction_operations.construct_polygonized_surface_from_point_clouds",
            {
                "point_cloud_list": point_cloud_list,
                "mesh_orientation": mesh_orientation,
                "grid_resolution": grid_resolution,
                "polygonized_surface_name": polygonized_surface_name,
            },
            None,
        )
        return None

    async def construct_scale_bar(
        self,
        scale_bar_name: CollectionItemName,
        begin_target: PointName,
        end_target: PointName,
        *,
        length: float = 0.0,
        uncertainty: float = 0.0,
        use_relative_tolerances: bool = True,
        use_high_tolerances: bool = False,
        use_low_tolerances: bool = False,
        high_tolerance: float = 0.0,
        low_tolerance: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.ConstructionOperations",
            "ConstructScaleBar",
            "construction_operations.construct_scale_bar",
            {
                "scale_bar_name": scale_bar_name,
                "begin_target": begin_target,
                "end_target": end_target,
                "length": length,
                "uncertainty": uncertainty,
                "use_relative_tolerances": use_relative_tolerances,
                "use_high_tolerances": use_high_tolerances,
                "use_low_tolerances": use_low_tolerances,
                "high_tolerance": high_tolerance,
                "low_tolerance": low_tolerance,
            },
            None,
        )
        return None


class GdtOperations:
    def __init__(self, client: _WaveBClient) -> None:
        self._client = client

    async def datum_alignment(
        self,
        feature_check: CollectionItemName,
        objects_to_move: Iterable[CollectionObjectName],
        instruments_to_move: Iterable[CollectionInstrumentId],
        *,
        apply_feature_check_transform: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "DatumAlignment",
            "gdt_operations.datum_alignment",
            {
                "feature_check": feature_check,
                "objects_to_move": objects_to_move,
                "instruments_to_move": instruments_to_move,
                "apply_feature_check_transform": apply_feature_check_transform,
            },
            None,
        )
        return None

    async def delete_feature_checks(
        self,
        feature_checks: Sequence[CollectionItemName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "DeleteFeatureChecks",
            "gdt_operations.delete_feature_checks",
            {
                "feature_checks": feature_checks,
            },
            None,
        )
        return None

    async def enable_disable_datum_alignment_for_feature_check(
        self,
        feature_check: CollectionItemName,
        *,
        enable_datum_alignment: bool = True,
        enable_custom_initial_alignment: bool = False,
        enable_initial_datum_alignment: bool = True,
        alignment: CollectionItemName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "EnableDisableDatumAlignmentForFeatureCheck",
            "gdt_operations.enable_disable_datum_alignment_for_feature_check",
            {
                "feature_check": feature_check,
                "enable_datum_alignment": enable_datum_alignment,
                "enable_custom_initial_alignment": enable_custom_initial_alignment,
                "enable_initial_datum_alignment": enable_initial_datum_alignment,
                "alignment": alignment,
            },
            None,
        )
        return None

    async def evaluate_feature_check(
        self,
        feature_check: CollectionItemName,
        *,
        perform_evaluation: bool = True,
        simultaneous_evaluation: bool = False,
    ) -> EvaluateFeatureCheckResult:
        return cast(
            EvaluateFeatureCheckResult,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "EvaluateFeatureCheck",
                "gdt_operations.evaluate_feature_check",
                {
                    "feature_check": feature_check,
                    "perform_evaluation": perform_evaluation,
                    "simultaneous_evaluation": simultaneous_evaluation,
                },
                EvaluateFeatureCheckResult,
            ),
        )

    async def evaluate_feature_checks(
        self,
        feature_check_list: Iterable[CollectionItemName],
        *,
        simultaneous_evaluation: bool = False,
        restrict_evaluations_to_listed_checks: bool = False,
    ) -> EvaluateFeatureChecksResult:
        return cast(
            EvaluateFeatureChecksResult,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "EvaluateFeatureChecks",
                "gdt_operations.evaluate_feature_checks",
                {
                    "feature_check_list": feature_check_list,
                    "simultaneous_evaluation": simultaneous_evaluation,
                    "restrict_evaluations_to_listed_checks": restrict_evaluations_to_listed_checks,
                },
                EvaluateFeatureChecksResult,
            ),
        )

    async def feature_inspection_auto_filter(
        self,
        *,
        point_names: Iterable[PointName] | None = None,
        group_names: Iterable[CollectionObjectName] | None = None,
        cloud_names: Iterable[CollectionObjectName] | None = None,
        surface_offset: float = 0.1,
        edge_offset: float = 0.1,
        offset_direction: OffsetDirectionType = OffsetDirectionType.BOTH,
        include_points_within_cylinder_axis_proximity: bool = False,
        enforce_max_points_per_face_in_output: bool = False,
        max_points_per_face: int = 0,
        feature_check_name_list: Iterable[CollectionItemName] | None = None,
        include_datums: bool = True,
        create_cloud_for_each_datum_or_check: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "FeatureInspectionAutoFilter",
            "gdt_operations.feature_inspection_auto_filter",
            {
                "point_names": point_names,
                "group_names": group_names,
                "cloud_names": cloud_names,
                "surface_offset": surface_offset,
                "edge_offset": edge_offset,
                "offset_direction": offset_direction,
                "include_points_within_cylinder_axis_proximity": include_points_within_cylinder_axis_proximity,
                "enforce_max_points_per_face_in_output": enforce_max_points_per_face_in_output,
                "max_points_per_face": max_points_per_face,
                "feature_check_name_list": feature_check_name_list,
                "include_datums": include_datums,
                "create_cloud_for_each_datum_or_check": create_cloud_for_each_datum_or_check,
            },
            None,
        )
        return None

    async def generate_feature_check_summary(
        self,
        feature_check_list: Iterable[CollectionItemName],
        *,
        summary_table_name: str = "GDT Feature Check Summary",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "GenerateFeatureCheckSummary",
            "gdt_operations.generate_feature_check_summary",
            {
                "feature_check_list": feature_check_list,
                "summary_table_name": summary_table_name,
            },
            None,
        )
        return None

    async def get_datum_measurements(
        self,
        datum: CollectionItemName,
    ) -> GdtMeasurements:
        return cast(
            GdtMeasurements,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetDatumMeasurements",
                "gdt_operations.get_datum_measurements",
                {
                    "datum": datum,
                },
                None,
            ),
        )

    async def get_feature_check_cylinder_eval_options(
        self,
        feature_check: CollectionItemName,
    ) -> FeatureCheckCylinderEvalOptions:
        return cast(
            FeatureCheckCylinderEvalOptions,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetFeatureCheckCylinderEvalOptions",
                "gdt_operations.get_feature_check_cylinder_eval_options",
                {
                    "feature_check": feature_check,
                },
                None,
            ),
        )

    async def get_feature_check_datum_references(
        self,
        feature_check: CollectionItemName,
    ) -> FeatureCheckDatumReferencesResult:
        return cast(
            FeatureCheckDatumReferencesResult,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetFeatureCheckDatumReferences",
                "gdt_operations.get_feature_check_datum_references",
                {
                    "feature_check": feature_check,
                },
                FeatureCheckDatumReferencesResult,
            ),
        )

    async def get_feature_check_measurements(
        self,
        feature_check: CollectionItemName,
    ) -> GdtMeasurements:
        return cast(
            GdtMeasurements,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetFeatureCheckMeasurements",
                "gdt_operations.get_feature_check_measurements",
                {
                    "feature_check": feature_check,
                },
                None,
            ),
        )

    async def get_feature_check_reporting_frame(
        self,
        feature_check: CollectionItemName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetFeatureCheckReportingFrame",
                "gdt_operations.get_feature_check_reporting_frame",
                {
                    "feature_check": feature_check,
                },
                None,
            ),
        )

    async def get_gdt_extended_options(
        self,
    ) -> bool:
        return cast(
            bool,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetGdtExtendedOptions",
                "gdt_operations.get_gdt_extended_options",
                {},
                None,
            ),
        )

    async def make_annotation_ref_list_from_collection(
        self,
        collection: CollectionName,
    ) -> Sequence[CollectionItemName]:
        return cast(
            Sequence[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeAnnotationRefListFromCollection",
                "gdt_operations.make_annotation_ref_list_from_collection",
                {
                    "collection": collection,
                },
                None,
            ),
        )

    async def make_annotation_ref_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        annotation_wildcard_criteria: str = "*",
    ) -> Sequence[CollectionItemName]:
        return cast(
            Sequence[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeAnnotationRefListWildcardSelection",
                "gdt_operations.make_annotation_ref_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "annotation_wildcard_criteria": annotation_wildcard_criteria,
                },
                None,
            ),
        )

    async def make_datum_ref_list_from_collection(
        self,
        collection: CollectionName,
    ) -> Sequence[CollectionObjectName]:
        return cast(
            Sequence[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeDatumRefListFromCollection",
                "gdt_operations.make_datum_ref_list_from_collection",
                {
                    "collection": collection,
                },
                None,
            ),
        )

    async def make_feature_check_ref_list_from_collection(
        self,
        collection: CollectionName,
    ) -> Sequence[CollectionItemName]:
        return cast(
            Sequence[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeFeatureCheckRefListFromCollection",
                "gdt_operations.make_feature_check_ref_list_from_collection",
                {
                    "collection": collection,
                },
                None,
            ),
        )

    async def make_feature_check_reference_list_wildcard_selection(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        feature_check_wildcard_criteria: str = "*",
    ) -> Sequence[CollectionItemName]:
        return cast(
            Sequence[CollectionItemName],
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeFeatureCheckReferenceListWildcardSelection",
                "gdt_operations.make_feature_check_reference_list_wildcard_selection",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "feature_check_wildcard_criteria": feature_check_wildcard_criteria,
                },
                None,
            ),
        )

    async def make_feature_checks(
        self,
        collection: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "MakeFeatureChecks",
            "gdt_operations.make_feature_checks",
            {
                "collection": collection,
            },
            None,
        )
        return None

    async def make_gdt_datum_annotation(
        self,
        options: MakeGdtDatumAnnotationOptions,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "MakeGdtDatumAnnotation",
            "gdt_operations.make_gdt_datum_annotation",
            {
                "datum_name": options.datum_name,
                "objects": options.objects,
                "geometry_relationships": options.geometry_relationships,
                "surface_faces": options.surface_faces,
                "auxiliary_object": options.auxiliary_object,
                "auxiliary_geometry_relationship": options.auxiliary_geometry_relationship,
                "is_slot": options.is_slot,
                "force_surface_feature": options.force_surface_feature,
            },
            None,
        )
        return None

    async def make_gdt_feature_check_annotation(
        self,
        options: MakeGdtFeatureCheckAnnotationOptions,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "MakeGdtFeatureCheckAnnotation",
            "gdt_operations.make_gdt_feature_check_annotation",
            {
                "feature_annotation_name": options.feature_annotation_name,
                "feature_type": options.feature_type,
                "objects": options.objects,
                "geometry_relationships": options.geometry_relationships,
                "surface_faces": options.surface_faces,
                "decompose_multiple_features": options.decompose_multiple_features,
                "auto_create_diameter_checks": options.auto_create_diameter_checks,
                "auto_create_slot_width_checks": options.auto_create_slot_width_checks,
                "auto_create_slot_length_checks": options.auto_create_slot_length_checks,
                "datum_references": options.datum_references,
                "tolerance": options.tolerance,
                "is_slot": options.is_slot,
                "per_unit_length_or_area": options.per_unit_length_or_area,
                "circular_area": options.circular_area,
                "per_unit_area_length_distance": options.per_unit_area_length_distance,
                "per_unit_area_length_step_over_percent": options.per_unit_area_length_step_over_percent,
                "per_unit_area_width_distance": options.per_unit_area_width_distance,
                "per_unit_area_width_step_over_percent": options.per_unit_area_width_step_over_percent,
                "per_unit_area_circle_diameter": options.per_unit_area_circle_diameter,
                "per_unit_area_diameter_step_over": options.per_unit_area_diameter_step_over,
                "auxiliary_object": options.auxiliary_object,
                "auxiliary_geometry_relationship": options.auxiliary_geometry_relationship,
                "use_nominal_for_dimension_tolerance": options.use_nominal_for_dimension_tolerance,
                "use_reference_object_for_nominal": options.use_reference_object_for_nominal,
                "nominal_dimension_tolerance": options.nominal_dimension_tolerance,
                "low_dimension_tolerance": options.low_dimension_tolerance,
                "high_dimension_tolerance": options.high_dimension_tolerance,
                "tolerance_zone_type": options.tolerance_zone_type,
                "use_projected_tolerance_zone": options.use_projected_tolerance_zone,
                "projected_tolerance_zone": options.projected_tolerance_zone,
            },
            None,
        )
        return None

    async def make_surface_face_list_from_surface(
        self,
        surface: CollectionObjectName,
    ) -> SurfaceFaceList:
        return cast(
            SurfaceFaceList,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeSurfaceFaceListFromSurface",
                "gdt_operations.make_surface_face_list_from_surface",
                {
                    "surface": surface,
                },
                None,
            ),
        )

    async def make_surface_face_list_runtime_select(
        self,
    ) -> SurfaceFaceList:
        return cast(
            SurfaceFaceList,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "MakeSurfaceFaceListRuntimeSelect",
                "gdt_operations.make_surface_face_list_runtime_select",
                {},
                None,
            ),
        )

    async def refresh_datums_feature_checks_from_annotations(
        self,
        collection: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "RefreshDatumsFeatureChecksFromAnnotations",
            "gdt_operations.refresh_datums_feature_checks_from_annotations",
            {
                "collection": collection,
            },
            None,
        )
        return None

    async def set_datum_measurements(
        self,
        datum: CollectionItemName,
        point_names: Iterable[PointName],
        cloud_names: Iterable[CollectionObjectName],
        *,
        replace_existing_measurements: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetDatumMeasurements",
            "gdt_operations.set_datum_measurements",
            {
                "datum": datum,
                "point_names": point_names,
                "cloud_names": cloud_names,
                "replace_existing_measurements": replace_existing_measurements,
            },
            None,
        )
        return None

    async def set_feature_check_cylinder_eval_options(
        self,
        feature_check: CollectionItemName,
        *,
        enable_actual_diameter_override: bool = False,
        actual_diameter_override: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetFeatureCheckCylinderEvalOptions",
            "gdt_operations.set_feature_check_cylinder_eval_options",
            {
                "feature_check": feature_check,
                "enable_actual_diameter_override": enable_actual_diameter_override,
                "actual_diameter_override": actual_diameter_override,
            },
            None,
        )
        return None

    async def set_feature_check_measurements(
        self,
        feature_check: CollectionItemName,
        point_names: Iterable[PointName],
        cloud_names: Iterable[CollectionObjectName],
        *,
        replace_existing_measurements: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetFeatureCheckMeasurements",
            "gdt_operations.set_feature_check_measurements",
            {
                "feature_check": feature_check,
                "point_names": point_names,
                "cloud_names": cloud_names,
                "replace_existing_measurements": replace_existing_measurements,
            },
            None,
        )
        return None

    async def set_feature_check_reporting_frame(
        self,
        feature_check: CollectionItemName,
        reporting_frame: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetFeatureCheckReportingFrame",
            "gdt_operations.set_feature_check_reporting_frame",
            {
                "feature_check": feature_check,
                "reporting_frame": reporting_frame,
            },
            None,
        )
        return None

    async def set_gdt_extended_options(
        self,
        *,
        use_extended_options: bool = True,
        circle: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        cone: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        cylinder: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        ellipse: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        line: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        open_slot: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        plane: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        slot: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
        sphere: GdtExtendedEvaluationMethod = GdtExtendedEvaluationMethod.LEAST_SQUARES,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetGdtExtendedOptions",
            "gdt_operations.set_gdt_extended_options",
            {
                "use_extended_options": use_extended_options,
                "circle_extended_options": circle,
                "cone_extended_options": cone,
                "cylinder_extended_options": cylinder,
                "ellipse_extended_options": ellipse,
                "line_extended_options": line,
                "open_slot_extended_options": open_slot,
                "plane_extended_options": plane,
                "slot_extended_options": slot,
                "sphere_extended_options": sphere,
            },
            None,
        )
        return None

    async def set_gdt_options(
        self,
        *,
        use_high_points: bool = False,
        extrapolate_axial_extent: bool = True,
        exclude_from_auto_evaluation: bool = True,
        distance_between_mode: GdtDistanceBetweenMode = GdtDistanceBetweenMode.CENTROID,
        evaluation_method: GdtEvaluationMethod = GdtEvaluationMethod.NONE,
        create_actual_features: bool = False,
        create_solved_points: bool = False,
        cross_section_criteria: float = 0.039370,
        enable_auto_feature_detection: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetGdtOptions",
            "gdt_operations.set_gdt_options",
            {
                "use_high_points": use_high_points,
                "extrapolate_axial_extent": extrapolate_axial_extent,
                "exclude_from_auto_evaluation": exclude_from_auto_evaluation,
                "distance_between_mode": distance_between_mode,
                "evaluation_method": evaluation_method,
                "create_actual_features": create_actual_features,
                "create_solved_points": create_solved_points,
                "cross_section_criteria": cross_section_criteria,
                "enable_auto_feature_detection": enable_auto_feature_detection,
            },
            None,
        )
        return None

    async def set_global_force_simultaneous_evaluation(
        self,
        *,
        global_simultaneous_evaluation: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetGlobalForceSimultaneousEvaluation",
            "gdt_operations.set_global_force_simultaneous_evaluation",
            {
                "global_simultaneous_evaluation": global_simultaneous_evaluation,
            },
            None,
        )
        return None

    async def start_stop_feature_check_trapping(
        self,
        feature_check: CollectionItemName,
        instrument_id: CollectionInstrumentId,
        *,
        start_trapping: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "StartStopFeatureCheckTrapping",
            "gdt_operations.start_stop_feature_check_trapping",
            {
                "feature_check": feature_check,
                "instrument_id": instrument_id,
                "start_trapping": start_trapping,
            },
            None,
        )
        return None

    async def get_feature_check_reporting_options(
        self,
        feature_check: CollectionItemName,
    ) -> FeatureCheckReportingOptions:
        return cast(
            FeatureCheckReportingOptions,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetFeatureCheckReportingOptions",
                "gdt_operations.get_feature_check_reporting_options",
                {
                    "feature_check": feature_check,
                },
                None,
            ),
        )

    async def get_gdt_options(
        self,
    ) -> GdtOptions:
        return cast(
            GdtOptions,
            await self._client._invoke_mp_operation(
                "briosa.GdtOperations",
                "GetGdtOptions",
                "gdt_operations.get_gdt_options",
                {},
                None,
            ),
        )

    async def set_feature_check_reporting_options(
        self,
        feature_check: CollectionItemName,
        *,
        show_feature_control_frame_summary: bool = True,
        include_title: bool = False,
        show_datum_and_tolerance_summary: bool = False,
        show_feature_summary: bool = False,
        only_create_failed_vectors: bool = False,
        show_point_details_summary: bool = False,
        show_lower_tier_tables: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.GdtOperations",
            "SetFeatureCheckReportingOptions",
            "gdt_operations.set_feature_check_reporting_options",
            {
                "feature_check": feature_check,
                "show_feature_control_frame_summary": show_feature_control_frame_summary,
                "include_title": include_title,
                "show_datum_and_tolerance_summary": show_datum_and_tolerance_summary,
                "show_feature_summary": show_feature_summary,
                "only_create_failed_vectors": only_create_failed_vectors,
                "show_point_details_summary": show_point_details_summary,
                "show_lower_tier_tables": show_lower_tier_tables,
            },
            None,
        )
        return None


class InstrumentOperations:
    def __init__(self, client: _WaveBClient) -> None:
        self._client = client

    async def activate_deactivate_instrument_toolbar(
        self,
        instrument: CollectionInstrumentId,
        *,
        deactivate_toolbar: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ActivateDeactivateInstrumentToolbar",
            "instrument_operations.activate_deactivate_instrument_toolbar",
            {
                "instrument": instrument,
                "deactivate_toolbar": deactivate_toolbar,
            },
            None,
        )
        return None

    async def add_new_instrument(
        self,
        instrument_type: InstrumentTypeName,
    ) -> CollectionInstrumentId:
        return cast(
            CollectionInstrumentId,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "AddNewInstrument",
                "instrument_operations.add_new_instrument",
                {
                    "instrument_type": instrument_type,
                },
                None,
            ),
        )

    async def add_nominal_point_to_tcp_fixture(
        self,
        tcp_fixture: CollectionObjectName,
        nominal_point_name: str,
        nominal_point_location: Vector,
        *,
        var_xx: float = 0.0,
        var_yy: float = 0.0,
        var_zz: float = 0.0,
        covar_xy: float = 0.0,
        covar_xz: float = 0.0,
        covar_yz: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AddNominalPointToTcpFixture",
            "instrument_operations.add_nominal_point_to_tcp_fixture",
            {
                "tcp_fixture": tcp_fixture,
                "nominal_point_name": nominal_point_name,
                "nominal_point_location": nominal_point_location,
                "var_xx": var_xx,
                "var_yy": var_yy,
                "var_zz": var_zz,
                "covar_xy": covar_xy,
                "covar_xz": covar_xz,
                "covar_yz": covar_yz,
            },
            None,
        )
        return None

    async def align_cloud_to_cad(
        self,
        cloud: CollectionObjectName,
        surfaces: Iterable[CollectionObjectName],
        *,
        maximum_coarse_cad_mesh_edge_length: float = 0.0,
        use_fine_cad_mesh: bool = False,
        execute_alignment: bool = True,
    ) -> CloudToCadAlignmentResult:
        return cast(
            CloudToCadAlignmentResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "AlignCloudToCad",
                "instrument_operations.align_cloud_to_cad",
                {
                    "cloud": cloud,
                    "surfaces": surfaces,
                    "maximum_coarse_cad_mesh_edge_length": maximum_coarse_cad_mesh_edge_length,
                    "use_fine_cad_mesh": use_fine_cad_mesh,
                    "execute_alignment": execute_alignment,
                },
                None,
            ),
        )

    async def align_laser_projector(
        self,
        instrument: CollectionInstrumentId,
        group: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AlignLaserProjector",
            "instrument_operations.align_laser_projector",
            {
                "instrument": instrument,
                "group": group,
            },
            None,
        )
        return None

    async def align_two_targets_with_axis_wcf_x(
        self,
        instrument: CollectionInstrumentId,
        first_point_on_axis: PointName,
        second_point_on_axis: PointName,
        initial_measured_group: CollectionObjectName,
        *,
        rotational_tolerance: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AlignTwoTargetsWithAxisWcfX",
            "instrument_operations.align_two_targets_with_axis_wcf_x",
            {
                "instrument": instrument,
                "first_point_on_axis": first_point_on_axis,
                "second_point_on_axis": second_point_on_axis,
                "initial_measured_group": initial_measured_group,
                "rotational_tolerance": rotational_tolerance,
            },
            None,
        )
        return None

    async def associate_objects_with_instrument(
        self,
        instrument: CollectionInstrumentId,
        objects: Iterable[CollectionObjectName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AssociateObjectsWithInstrument",
            "instrument_operations.associate_objects_with_instrument",
            {
                "instrument": instrument,
                "objects": objects,
            },
            None,
        )
        return None

    async def auto_correspond_closest_point(
        self,
        instrument: CollectionInstrumentId,
        reference_group: CollectionObjectName,
        actuals_group: CollectionObjectName,
        *,
        wait_for_completion: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoCorrespondClosestPoint",
            "instrument_operations.auto_correspond_closest_point",
            {
                "instrument": instrument,
                "reference_group": reference_group,
                "actuals_group": actuals_group,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def auto_correspond_with_proximity_trigger(
        self,
        instrument: CollectionInstrumentId,
        nominal_group: CollectionObjectName,
        results_group: CollectionObjectName,
        *,
        point_distance_threshold: float = 0.5,
        vector_axis_threshold: float = 0.25,
        project_results_to_nominal_vector: bool = False,
        warbler_ramp_start_distance: float = 12.0,
        show_watch_window: bool = False,
        deviation_vector_group_name: str | None = None,
        make_unmeasured_group: bool = False,
        measure_each_point_only_once: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoCorrespondWithProximityTrigger",
            "instrument_operations.auto_correspond_with_proximity_trigger",
            {
                "instrument": instrument,
                "nominal_group": nominal_group,
                "results_group": results_group,
                "point_distance_threshold": point_distance_threshold,
                "vector_axis_threshold": vector_axis_threshold,
                "project_results_to_nominal_vector": project_results_to_nominal_vector,
                "warbler_ramp_start_distance": warbler_ramp_start_distance,
                "show_watch_window": show_watch_window,
                "deviation_vector_group_name": deviation_vector_group_name,
                "make_unmeasured_group": make_unmeasured_group,
                "measure_each_point_only_once": measure_each_point_only_once,
            },
            None,
        )
        return None

    async def auto_measure_batch_of_features(
        self,
        instrument: CollectionInstrumentId,
        features: Iterable[CollectionItemName],
        *,
        wait_for_complete: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoMeasureBatchOfFeatures",
            "instrument_operations.auto_measure_batch_of_features",
            {
                "instrument": instrument,
                "features": features,
                "wait_for_complete": wait_for_complete,
            },
            None,
        )
        return None

    async def auto_measure_points(
        self,
        instrument: CollectionInstrumentId,
        reference_group: CollectionObjectName,
        actuals_group: CollectionObjectName,
        *,
        force_existing_group: bool = False,
        show_complete_dialog: bool = False,
        wait_for_completion: bool = True,
        auto_start: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoMeasurePoints",
            "instrument_operations.auto_measure_points",
            {
                "instrument": instrument,
                "reference_group": reference_group,
                "actuals_group": actuals_group,
                "force_existing_group": force_existing_group,
                "show_complete_dialog": show_complete_dialog,
                "wait_for_completion": wait_for_completion,
                "auto_start": auto_start,
            },
            None,
        )
        return None

    async def auto_measure_specified_geometry(
        self,
        instrument: CollectionInstrumentId,
        geometry: CollectionObjectName,
        mode_profile: str,
        *,
        wait_for_complete: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoMeasureSpecifiedGeometry",
            "instrument_operations.auto_measure_specified_geometry",
            {
                "instrument": instrument,
                "geometry": geometry,
                "mode_profile": mode_profile,
                "wait_for_complete": wait_for_complete,
            },
            None,
        )
        return None

    async def auto_measure_surface_vector_intersections(
        self,
        instrument: CollectionInstrumentId,
        vector_group: CollectionObjectName,
        resultant_group: CollectionObjectName,
        *,
        wait_for_complete: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoMeasureSurfaceVectorIntersections",
            "instrument_operations.auto_measure_surface_vector_intersections",
            {
                "instrument": instrument,
                "vector_group": vector_group,
                "resultant_group": resultant_group,
                "wait_for_complete": wait_for_complete,
            },
            None,
        )
        return None

    async def auto_measure_vectors(
        self,
        instrument: CollectionInstrumentId,
        vector_group: CollectionObjectName,
        actuals_group: CollectionObjectName,
        *,
        project_point_to_vector: bool = False,
        angle_tolerance: float = 0.0,
        high_tolerance: float = 0.0,
        low_tolerance: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "AutoMeasureVectors",
            "instrument_operations.auto_measure_vectors",
            {
                "instrument": instrument,
                "vector_group": vector_group,
                "actuals_group": actuals_group,
                "project_point_to_vector": project_point_to_vector,
                "angle_tolerance": angle_tolerance,
                "high_tolerance": high_tolerance,
                "low_tolerance": low_tolerance,
            },
            None,
        )
        return None

    async def build_target(
        self,
        instrument: CollectionInstrumentId,
        output_target_name: PointName,
        nominal_point: PointName,
        *,
        tolerance: ToleranceVectorOptions | None = None,
        html_prompt_file: FileReference | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "BuildTarget",
            "instrument_operations.build_target",
            {
                "instrument": instrument,
                "output_target_name": output_target_name,
                "nominal_point": nominal_point,
                "tolerance": tolerance,
                "html_prompt_file": html_prompt_file,
            },
            None,
        )
        return None

    async def calculate_tcp_fixture_uncertainties(
        self,
        tcp_fixture: CollectionObjectName,
        tcp_measurements: Iterable[PointName],
        *,
        tcp_in_working: Transform | None = None,
    ) -> TcpFixtureUncertainties:
        return cast(
            TcpFixtureUncertainties,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "CalculateTcpFixtureUncertainties",
                "instrument_operations.calculate_tcp_fixture_uncertainties",
                {
                    "tcp_fixture": tcp_fixture,
                    "tcp_in_working": tcp_in_working,
                    "tcp_measurements": tcp_measurements,
                },
                None,
            ),
        )

    async def clear_cloud_viewer(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ClearCloudViewer",
            "instrument_operations.clear_cloud_viewer",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def close_auto_correspond_closest_point_dialog(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "CloseAutoCorrespondClosestPointDialog",
            "instrument_operations.close_auto_correspond_closest_point_dialog",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def collimation(
        self,
        stationary_instrument: CollectionInstrumentId,
        moving_instrument: CollectionInstrumentId,
        collimation_point: PointName,
        *,
        zero_moving_instrument: bool = False,
        tilt_mode: CollimationTiltMode = CollimationTiltMode.FULL_COLLIMATION,
        baseline_method: CollimationBaselineMethod = CollimationBaselineMethod.DETERMINED_BY_VALUE,
        baseline_distance: float = 0.0,
        scale_point_1: PointName | None = None,
        scale_point_2: PointName | None = None,
        not_measured_by_moving_instrument: PointName | None = None,
        as_measured_by_moving_instrument: PointName | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "Collimation",
            "instrument_operations.collimation",
            {
                "stationary_instrument": stationary_instrument,
                "moving_instrument": moving_instrument,
                "collimation_point": collimation_point,
                "zero_moving_instrument": zero_moving_instrument,
                "tilt_mode": tilt_mode,
                "baseline_method": baseline_method,
                "baseline_distance": baseline_distance,
                "scale_point_1": scale_point_1,
                "scale_point_2": scale_point_2,
                "not_measured_by_moving_instrument": not_measured_by_moving_instrument,
                "as_measured_by_moving_instrument": as_measured_by_moving_instrument,
            },
            None,
        )
        return None

    async def combine_point_groups(
        self,
        groups_to_combine: Iterable[CollectionObjectName],
        combined_point_group: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "CombinePointGroups",
            "instrument_operations.combine_point_groups",
            {
                "groups_to_combine": groups_to_combine,
                "combined_point_group": combined_point_group,
            },
            None,
        )
        return None

    async def compute_cte_scale_factor(
        self,
        *,
        material_cte_per_degree_fahrenheit: float = 0.0,
        initial_temperature_fahrenheit: float = 0.0,
        final_temperature_fahrenheit: float = 0.0,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "ComputeCteScaleFactor",
                "instrument_operations.compute_cte_scale_factor",
                {
                    "material_cte_per_degree_fahrenheit": material_cte_per_degree_fahrenheit,
                    "initial_temperature_fahrenheit": initial_temperature_fahrenheit,
                    "final_temperature_fahrenheit": final_temperature_fahrenheit,
                },
                None,
            ),
        )

    async def configure_and_measure(
        self,
        instrument: CollectionInstrumentId,
        target: PointName,
        measurement_mode: str,
        *,
        measure_immediately: bool = False,
        wait_for_completion: bool = True,
        timeout_seconds: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ConfigureAndMeasure",
            "instrument_operations.configure_and_measure",
            {
                "instrument": instrument,
                "target": target,
                "measurement_mode": measurement_mode,
                "measure_immediately": measure_immediately,
                "wait_for_completion": wait_for_completion,
                "timeout_seconds": timeout_seconds,
            },
            None,
        )
        return None

    async def construct_measured_point_uncertainty_ellipsoids(
        self,
        measurements: Iterable[PointName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ConstructMeasuredPointUncertaintyEllipsoids",
            "instrument_operations.construct_measured_point_uncertainty_ellipsoids",
            {
                "measurements": measurements,
            },
            None,
        )
        return None

    async def construct_mirror_from_plane(
        self,
        instrument: CollectionInstrumentId,
        mirror_name: str,
        plane: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ConstructMirrorFromPlane",
            "instrument_operations.construct_mirror_from_plane",
            {
                "instrument": instrument,
                "mirror_name": mirror_name,
                "plane": plane,
            },
            None,
        )
        return None

    async def construct_mirror_from_two_points(
        self,
        instrument: CollectionInstrumentId,
        mirror_name: str,
        point_measured_directly: PointName,
        point_measured_through_mirror: PointName,
        *,
        send_mirror_to_instrument: bool = True,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "ConstructMirrorFromTwoPoints",
                "instrument_operations.construct_mirror_from_two_points",
                {
                    "instrument": instrument,
                    "mirror_name": mirror_name,
                    "point_measured_directly": point_measured_directly,
                    "point_measured_through_mirror": point_measured_through_mirror,
                    "send_mirror_to_instrument": send_mirror_to_instrument,
                },
                None,
            ),
        )

    async def construct_perimeters_from_surface_face_list(
        self,
        surface_faces: SurfaceFaceList,
    ) -> PerimeterLists:
        return cast(
            PerimeterLists,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "ConstructPerimetersFromSurfaceFaceList",
                "instrument_operations.construct_perimeters_from_surface_face_list",
                {
                    "surface_faces": surface_faces,
                },
                None,
            ),
        )

    async def construct_tcp_fixture(
        self,
        requested_tcp_fixture: CollectionObjectName,
        *,
        point_match_threshold: float = 0.0,
        replace_existing_tcp_fixture: bool = False,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "ConstructTcpFixture",
                "instrument_operations.construct_tcp_fixture",
                {
                    "requested_tcp_fixture": requested_tcp_fixture,
                    "point_match_threshold": point_match_threshold,
                    "replace_existing_tcp_fixture": replace_existing_tcp_fixture,
                },
                None,
            ),
        )

    async def create_new_dynamic_reference(
        self,
        instrument: CollectionInstrumentId,
        points_defining_dynamic_reference: Iterable[PointName],
        dynamic_reference_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "CreateNewDynamicReference",
            "instrument_operations.create_new_dynamic_reference",
            {
                "instrument": instrument,
                "points_defining_dynamic_reference": points_defining_dynamic_reference,
                "dynamic_reference_name": dynamic_reference_name,
            },
            None,
        )
        return None

    async def create_templated_instrument_usmn(
        self,
        instrument_template_name: CollectionObjectName,
        instrument: CollectionInstrumentId,
        *,
        overall_instrument_weight: float = 1.0,
        moving: bool = True,
        enable_x: bool = True,
        enable_y: bool = True,
        enable_z: bool = True,
        enable_rx: bool = True,
        enable_ry: bool = True,
        enable_rz: bool = True,
        enable_scale: bool = False,
        enable_component_weights: bool = True,
        azimuth_weight: float = 1.0,
        elevation_weight: float = 1.0,
        distance_weight: float = 1.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "CreateTemplatedInstrumentUsmn",
            "instrument_operations.create_templated_instrument_usmn",
            {
                "instrument_template_name": instrument_template_name,
                "instrument": instrument,
                "overall_instrument_weight": overall_instrument_weight,
                "moving": moving,
                "enable_x": enable_x,
                "enable_y": enable_y,
                "enable_z": enable_z,
                "enable_rx": enable_rx,
                "enable_ry": enable_ry,
                "enable_rz": enable_rz,
                "enable_scale": enable_scale,
                "enable_component_weights": enable_component_weights,
                "azimuth_weight": azimuth_weight,
                "elevation_weight": elevation_weight,
                "distance_weight": distance_weight,
            },
            None,
        )
        return None

    async def delete_instrument(
        self,
        instrument: CollectionInstrumentId,
        *,
        prompt_user_to_confirm: bool = False,
        keep_resulting_points: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DeleteInstrument",
            "instrument_operations.delete_instrument",
            {
                "instrument": instrument,
                "prompt_user_to_confirm": prompt_user_to_confirm,
                "keep_resulting_points": keep_resulting_points,
            },
            None,
        )
        return None

    async def delete_measurement_observation(
        self,
        point_name: PointName,
        *,
        observation_index: int = 0,
        delete_point_if_no_measurements_remain: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DeleteMeasurementObservation",
            "instrument_operations.delete_measurement_observation",
            {
                "point_name": point_name,
                "observation_index": observation_index,
                "delete_point_if_no_measurements_remain": delete_point_if_no_measurements_remain,
            },
            None,
        )
        return None

    async def delete_measurements(
        self,
        instrument: CollectionInstrumentId,
        point_name: PointName,
        *,
        delete_point_if_no_measurements_remain: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DeleteMeasurements",
            "instrument_operations.delete_measurements",
            {
                "instrument": instrument,
                "point_name": point_name,
                "delete_point_if_no_measurements_remain": delete_point_if_no_measurements_remain,
            },
            None,
        )
        return None

    async def disassociate_objects_from_instrument(
        self,
        objects: Iterable[CollectionObjectName],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DisassociateObjectsFromInstrument",
            "instrument_operations.disassociate_objects_from_instrument",
            {
                "objects": objects,
            },
            None,
        )
        return None

    async def dissect_point_group(
        self,
        group_to_dissect: CollectionObjectName,
        base_name_for_dissected_groups: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DissectPointGroup",
            "instrument_operations.dissect_point_group",
            {
                "group_to_dissect": group_to_dissect,
                "base_name_for_dissected_groups": base_name_for_dissected_groups,
            },
            None,
        )
        return None

    async def dock_instrument_interface(
        self,
        instrument: CollectionInstrumentId,
        *,
        dock_interface: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "DockInstrumentInterface",
            "instrument_operations.dock_instrument_interface",
            {
                "instrument": instrument,
                "dock_interface": dock_interface,
            },
            None,
        )
        return None

    async def drift_check(
        self,
        instrument: CollectionInstrumentId,
        reference_group: CollectionObjectName,
        actuals_group: CollectionObjectName,
        *,
        tolerance: float = 0.0,
        minimum_point_count: int = 0,
        use_closest_reference_point: bool = True,
    ) -> DriftCheckResult:
        return cast(
            DriftCheckResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "DriftCheck",
                "instrument_operations.drift_check",
                {
                    "instrument": instrument,
                    "reference_group": reference_group,
                    "actuals_group": actuals_group,
                    "tolerance": tolerance,
                    "minimum_point_count": minimum_point_count,
                    "use_closest_reference_point": use_closest_reference_point,
                },
                DriftCheckResult,
            ),
        )

    async def edge_scan_measurement(
        self,
        instrument: CollectionInstrumentId,
        point_near_edge: PointName,
        edge_search_direction_point: PointName,
        parameter_set_name: str,
        point_group: CollectionObjectName,
        target_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "EdgeScanMeasurement",
            "instrument_operations.edge_scan_measurement",
            {
                "instrument": instrument,
                "point_near_edge": point_near_edge,
                "edge_search_direction_point": edge_search_direction_point,
                "parameter_set_name": parameter_set_name,
                "point_group": point_group,
                "target_name": target_name,
            },
            None,
        )
        return None

    async def edit_scan_perimeter_profile(
        self,
        instrument: CollectionInstrumentId,
        scan_perimeters: Sequence[CollectionObjectName],
        exclusion_perimeters: Sequence[CollectionObjectName],
        parameter_set_name: str,
        profile_name: str,
        *,
        clear_profile: bool = True,
        create_new_profile: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "EditScanPerimeterProfile",
            "instrument_operations.edit_scan_perimeter_profile",
            {
                "instrument": instrument,
                "scan_perimeters": scan_perimeters,
                "exclusion_perimeters": exclusion_perimeters,
                "parameter_set_name": parameter_set_name,
                "profile_name": profile_name,
                "clear_profile": clear_profile,
                "create_new_profile": create_new_profile,
            },
            None,
        )
        return None

    async def enable_disable_frame_set_scan_mode_all_instruments(
        self,
        *,
        enable_frame_set_scan_mode: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "EnableDisableFrameSetScanModeAllInstruments",
            "instrument_operations.enable_disable_frame_set_scan_mode_all_instruments",
            {
                "enable_frame_set_scan_mode": enable_frame_set_scan_mode,
            },
            None,
        )
        return None

    async def enable_disable_frame_set_scan_mode_by_instrument(
        self,
        instrument: CollectionInstrumentId,
        *,
        enable_frame_set_scan_mode: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "EnableDisableFrameSetScanModeByInstrument",
            "instrument_operations.enable_disable_frame_set_scan_mode_by_instrument",
            {
                "instrument": instrument,
                "enable_frame_set_scan_mode": enable_frame_set_scan_mode,
            },
            None,
        )
        return None

    async def enable_disable_point_set_scan_mode(
        self,
        instrument: CollectionInstrumentId,
        *,
        enable_point_set_scan_mode: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "EnableDisablePointSetScanMode",
            "instrument_operations.enable_disable_point_set_scan_mode",
            {
                "instrument": instrument,
                "enable_point_set_scan_mode": enable_point_set_scan_mode,
            },
            None,
        )
        return None

    async def export_instrument_history_to_xml_file(
        self,
        instrument: CollectionInstrumentId,
        file_path: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ExportInstrumentHistoryToXmlFile",
            "instrument_operations.export_instrument_history_to_xml_file",
            {
                "instrument": instrument,
                "file_path": file_path,
            },
            None,
        )
        return None

    async def fabricate_observations(
        self,
        instrument: CollectionInstrumentId,
        point_group: CollectionObjectName,
        *,
        introduce_instrument_error: bool = False,
        limit_distance: bool = False,
        minimum_distance: float = 0.0,
        maximum_distance: float = 1000000.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "FabricateObservations",
            "instrument_operations.fabricate_observations",
            {
                "instrument": instrument,
                "point_group": point_group,
                "introduce_instrument_error": introduce_instrument_error,
                "limit_distance": limit_distance,
                "minimum_distance": minimum_distance,
                "maximum_distance": maximum_distance,
            },
            None,
        )
        return None

    async def get_current_instrument_position_update(
        self,
        instrument: CollectionInstrumentId,
        *,
        reporting_frame: InstrumentPositionReportingFrame = InstrumentPositionReportingFrame.INSTRUMENT_BASE,
        polar_coordinates: bool = False,
    ) -> InstrumentPositionUpdate:
        return cast(
            InstrumentPositionUpdate,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetCurrentInstrumentPositionUpdate",
                "instrument_operations.get_current_instrument_position_update",
                {
                    "instrument": instrument,
                    "reporting_frame": reporting_frame,
                    "polar_coordinates": polar_coordinates,
                },
                InstrumentPositionUpdate,
            ),
        )

    async def get_current_trapping_status(
        self,
    ) -> CurrentTrappingStatus:
        return cast(
            CurrentTrappingStatus,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetCurrentTrappingStatus",
                "instrument_operations.get_current_trapping_status",
                {},
                None,
            ),
        )

    async def get_estimated_scan_time(
        self,
        instrument: CollectionInstrumentId,
        profile_name: str,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetEstimatedScanTime",
                "instrument_operations.get_estimated_scan_time",
                {
                    "instrument": instrument,
                    "profile_name": profile_name,
                },
                None,
            ),
        )

    async def get_inspection_verification_mode(
        self,
    ) -> bool:
        return cast(
            bool,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInspectionVerificationMode",
                "instrument_operations.get_inspection_verification_mode",
                {},
                None,
            ),
        )

    async def get_instrument_base_uncertainty_covariance_matrix_wrt_world(
        self,
        instrument: CollectionInstrumentId,
    ) -> UncertaintyCovarianceMatrix:
        return cast(
            UncertaintyCovarianceMatrix,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentBaseUncertaintyCovarianceMatrixWrtWorld",
                "instrument_operations.get_instrument_base_uncertainty_covariance_matrix_wrt_world",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_group_and_target(
        self,
        instrument: CollectionInstrumentId,
    ) -> PointName:
        return cast(
            PointName,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentGroupAndTarget",
                "instrument_operations.get_instrument_group_and_target",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_id_from_name(
        self,
        name: str,
    ) -> CollectionInstrumentId:
        return cast(
            CollectionInstrumentId,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentIdFromName",
                "instrument_operations.get_instrument_id_from_name",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_instrument_interface_response_timeout(
        self,
        instrument: CollectionInstrumentId,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentInterfaceResponseTimeout",
                "instrument_operations.get_instrument_interface_response_timeout",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_measurement_mode_profile(
        self,
        instrument: CollectionInstrumentId,
    ) -> str:
        return cast(
            str,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentMeasurementModeProfile",
                "instrument_operations.get_instrument_measurement_mode_profile",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_model(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentModelResult:
        return cast(
            InstrumentModelResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentModel",
                "instrument_operations.get_instrument_model",
                {
                    "instrument": instrument,
                },
                InstrumentModelResult,
            ),
        )

    async def get_instrument_part_temperature(
        self,
        instrument: CollectionInstrumentId,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentPartTemperature",
                "instrument_operations.get_instrument_part_temperature",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_scale_factor(
        self,
        instrument: CollectionInstrumentId,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentScaleFactor",
                "instrument_operations.get_instrument_scale_factor",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_target_status(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentTargetStatus:
        return cast(
            InstrumentTargetStatus,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentTargetStatus",
                "instrument_operations.get_instrument_target_status",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_targeting(
        self,
        instrument: CollectionInstrumentId,
    ) -> str:
        return cast(
            str,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentTargeting",
                "instrument_operations.get_instrument_targeting",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_instrument_targets_and_mode_profiles(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentTargetsAndModeProfiles:
        return cast(
            InstrumentTargetsAndModeProfiles,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentTargetsAndModeProfiles",
                "instrument_operations.get_instrument_targets_and_mode_profiles",
                {
                    "instrument": instrument,
                },
                InstrumentTargetsAndModeProfiles,
            ),
        )

    async def get_instrument_transform(
        self,
        instrument: CollectionInstrumentId,
        reference_frame: CollectionObjectName,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentTransform",
                "instrument_operations.get_instrument_transform",
                {
                    "instrument": instrument,
                    "reference_frame": reference_frame,
                },
                None,
            ),
        )

    async def get_instrument_weather_setting(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentWeatherSetting:
        return cast(
            InstrumentWeatherSetting,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentWeatherSetting",
                "instrument_operations.get_instrument_weather_setting",
                {
                    "instrument": instrument,
                },
                InstrumentWeatherSetting,
            ),
        )

    async def get_instruments_with_observations_on_target(
        self,
        point: PointName,
    ) -> list[CollectionInstrumentId]:
        return cast(
            list[CollectionInstrumentId],
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetInstrumentsWithObservationsOnTarget",
                "instrument_operations.get_instruments_with_observations_on_target",
                {
                    "point": point,
                },
                None,
            ),
        )

    async def get_last_instrument_index(
        self,
    ) -> LastInstrumentIndexResult:
        return cast(
            LastInstrumentIndexResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetLastInstrumentIndex",
                "instrument_operations.get_last_instrument_index",
                {},
                LastInstrumentIndexResult,
            ),
        )

    async def get_last_solved_tcp_fixture_uncertainty_covariance_matrix(
        self,
        tcp_fixture: CollectionObjectName,
    ) -> UncertaintyCovarianceMatrix:
        return cast(
            UncertaintyCovarianceMatrix,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetLastSolvedTcpFixtureUncertaintyCovarianceMatrix",
                "instrument_operations.get_last_solved_tcp_fixture_uncertainty_covariance_matrix",
                {
                    "tcp_fixture": tcp_fixture,
                },
                None,
            ),
        )

    async def get_number_of_observations_on_target(
        self,
        point: PointName,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetNumberOfObservationsOnTarget",
                "instrument_operations.get_number_of_observations_on_target",
                {
                    "point": point,
                },
                None,
            ),
        )

    async def get_obscured_points_from_instrument(
        self,
        instrument: CollectionInstrumentId,
        candidate_points: Sequence[PointName],
        *,
        show_obscured_shots: bool = False,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetObscuredPointsFromInstrument",
                "instrument_operations.get_obscured_points_from_instrument",
                {
                    "instrument": instrument,
                    "candidate_points": candidate_points,
                    "show_obscured_shots": show_obscured_shots,
                },
                None,
            ),
        )

    async def get_observation_info(
        self,
        point: PointName,
        *,
        observation_index: int = 0,
    ) -> ObservationInfo:
        return cast(
            ObservationInfo,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetObservationInfo",
                "instrument_operations.get_observation_info",
                {
                    "point": point,
                    "observation_index": observation_index,
                },
                None,
            ),
        )

    async def get_pcmm_instrument_xyz_uncertainties(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentXyzUncertainties:
        return cast(
            InstrumentXyzUncertainties,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetPcmmInstrumentXyzUncertainties",
                "instrument_operations.get_pcmm_instrument_xyz_uncertainties",
                {
                    "instrument": instrument,
                },
                InstrumentXyzUncertainties,
            ),
        )

    async def get_targets_measured_by_instrument(
        self,
        instrument: CollectionInstrumentId,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetTargetsMeasuredByInstrument",
                "instrument_operations.get_targets_measured_by_instrument",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_tracker_edm_theodolite_uncertainties(
        self,
        instrument: CollectionInstrumentId,
    ) -> TrackerEdmTheodoliteUncertainties:
        return cast(
            TrackerEdmTheodoliteUncertainties,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetTrackerEdmTheodoliteUncertainties",
                "instrument_operations.get_tracker_edm_theodolite_uncertainties",
                {
                    "instrument": instrument,
                },
                TrackerEdmTheodoliteUncertainties,
            ),
        )

    async def get_wrtl_channel_and_status(
        self,
        instrument: CollectionInstrumentId,
    ) -> WrtlChannelStatus:
        return cast(
            WrtlChannelStatus,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetWrtlChannelAndStatus",
                "instrument_operations.get_wrtl_channel_and_status",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def get_xyz_instrument_uncertainties(
        self,
        instrument: CollectionInstrumentId,
    ) -> InstrumentXyzUncertainties:
        return cast(
            InstrumentXyzUncertainties,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "GetXyzInstrumentUncertainties",
                "instrument_operations.get_xyz_instrument_uncertainties",
                {
                    "instrument": instrument,
                },
                InstrumentXyzUncertainties,
            ),
        )

    async def guide_objects_in_6d_based_on_point_measurements(
        self,
        instrument: CollectionInstrumentId,
        destination_group: CollectionObjectName,
        moving_reference_group: CollectionObjectName,
        objects_to_move: Iterable[CollectionObjectName],
        *,
        initial_survey_group: CollectionObjectName | None = None,
        positional_tolerance: ToleranceVectorOptions | None = None,
        rotational_tolerance: ToleranceVectorOptions | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "GuideObjectsIn6dBasedOnPointMeasurements",
            "instrument_operations.guide_objects_in_6d_based_on_point_measurements",
            {
                "instrument": instrument,
                "destination_group": destination_group,
                "moving_reference_group": moving_reference_group,
                "objects_to_move": objects_to_move,
                "initial_survey_group": initial_survey_group,
                "positional_tolerance": positional_tolerance,
                "rotational_tolerance": rotational_tolerance,
            },
            None,
        )
        return None

    async def initiate_servo_guide(
        self,
        instrument: CollectionInstrumentId,
        nominal_points: Sequence[PointName],
        *,
        group_name_suffix: str = "",
        target_name_suffix: str = "",
        tolerance: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "InitiateServoGuide",
            "instrument_operations.initiate_servo_guide",
            {
                "instrument": instrument,
                "nominal_points": nominal_points,
                "group_name_suffix": group_name_suffix,
                "target_name_suffix": target_name_suffix,
                "tolerance": tolerance,
            },
            None,
        )
        return None

    async def instrument_operational_check(
        self,
        instrument: CollectionInstrumentId,
        check_type: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "InstrumentOperationalCheck",
            "instrument_operations.instrument_operational_check",
            {
                "instrument": instrument,
                "check_type": check_type,
            },
            None,
        )
        return None

    async def issue_instrument_actuator_command(
        self,
        instrument: CollectionInstrumentId,
        command: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "IssueInstrumentActuatorCommand",
            "instrument_operations.issue_instrument_actuator_command",
            {
                "instrument": instrument,
                "command": command,
            },
            None,
        )
        return None

    async def jump_instrument_to_new_location(
        self,
        live_instrument: CollectionInstrumentId,
        *,
        hide_previous_instrument: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "JumpInstrumentToNewLocation",
            "instrument_operations.jump_instrument_to_new_location",
            {
                "live_instrument": live_instrument,
                "hide_previous_instrument": hide_previous_instrument,
            },
            None,
        )
        return None

    async def load_cloud_viewer_point_cloud_file(
        self,
        instrument: CollectionInstrumentId,
        file_path: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LoadCloudViewerPointCloudFile",
            "instrument_operations.load_cloud_viewer_point_cloud_file",
            {
                "instrument": instrument,
                "file_path": file_path,
            },
            None,
        )
        return None

    async def load_instrument_configuration(
        self,
        instrument: CollectionInstrumentId,
        configuration_file: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LoadInstrumentConfiguration",
            "instrument_operations.load_instrument_configuration",
            {
                "instrument": instrument,
                "configuration_file": configuration_file,
            },
            None,
        )
        return None

    async def locate_instrument_best_fit_group_to_group(
        self,
        reference_group: CollectionObjectName,
        corresponding_group: CollectionObjectName,
        *,
        show_interface: bool = False,
        rms_tolerance: float = 0.0,
        maximum_absolute_tolerance: float = 0.0,
        allow_scale: bool = False,
        allow_x: bool = True,
        allow_y: bool = True,
        allow_z: bool = True,
        allow_rx: bool = True,
        allow_ry: bool = True,
        allow_rz: bool = True,
        lock_degrees_of_freedom: bool = False,
        generate_event: bool = False,
        csv_report: FileReference | None = None,
    ) -> InstrumentBestFitResult:
        return cast(
            InstrumentBestFitResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LocateInstrumentBestFitGroupToGroup",
                "instrument_operations.locate_instrument_best_fit_group_to_group",
                {
                    "reference_group": reference_group,
                    "corresponding_group": corresponding_group,
                    "show_interface": show_interface,
                    "rms_tolerance": rms_tolerance,
                    "maximum_absolute_tolerance": maximum_absolute_tolerance,
                    "allow_scale": allow_scale,
                    "allow_x": allow_x,
                    "allow_y": allow_y,
                    "allow_z": allow_z,
                    "allow_rx": allow_rx,
                    "allow_ry": allow_ry,
                    "allow_rz": allow_rz,
                    "lock_degrees_of_freedom": lock_degrees_of_freedom,
                    "generate_event": generate_event,
                    "csv_report": csv_report,
                },
                InstrumentBestFitResult,
            ),
        )

    async def locate_instrument_best_fit_nominal_geometry(
        self,
        instrument: CollectionInstrumentId,
        geometry_relationships: Sequence[CollectionObjectName],
        *,
        show_interface: bool = False,
        rms_tolerance: float = 0.0,
        maximum_absolute_tolerance: float = 0.0,
        allow_scale: bool = False,
        allow_x: bool = True,
        allow_y: bool = True,
        allow_z: bool = True,
        allow_rx: bool = True,
        allow_ry: bool = True,
        allow_rz: bool = True,
        lock_degrees_of_freedom: bool = False,
        generate_event: bool = False,
        csv_report: FileReference | None = None,
    ) -> InstrumentBestFitResult:
        return cast(
            InstrumentBestFitResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LocateInstrumentBestFitNominalGeometry",
                "instrument_operations.locate_instrument_best_fit_nominal_geometry",
                {
                    "instrument": instrument,
                    "geometry_relationships": geometry_relationships,
                    "show_interface": show_interface,
                    "rms_tolerance": rms_tolerance,
                    "maximum_absolute_tolerance": maximum_absolute_tolerance,
                    "allow_scale": allow_scale,
                    "allow_x": allow_x,
                    "allow_y": allow_y,
                    "allow_z": allow_z,
                    "allow_rx": allow_rx,
                    "allow_ry": allow_ry,
                    "allow_rz": allow_rz,
                    "lock_degrees_of_freedom": lock_degrees_of_freedom,
                    "generate_event": generate_event,
                    "csv_report": csv_report,
                },
                InstrumentBestFitResult,
            ),
        )

    async def locate_instrument_group_to_surface_quick_fit(
        self,
        instrument: CollectionInstrumentId,
        measured_group: CollectionObjectName,
        surface_points_group: CollectionObjectName,
        surface_to_fit: CollectionObjectName,
        *,
        other_objects_to_transform: Sequence[CollectionObjectName] = (),
        rms_tolerance: float = 0.0,
        maximum_absolute_tolerance: float = 0.0,
    ) -> FitErrorResult:
        return cast(
            FitErrorResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LocateInstrumentGroupToSurfaceQuickFit",
                "instrument_operations.locate_instrument_group_to_surface_quick_fit",
                {
                    "instrument": instrument,
                    "measured_group": measured_group,
                    "surface_points_group": surface_points_group,
                    "surface_to_fit": surface_to_fit,
                    "other_objects_to_transform": other_objects_to_transform,
                    "rms_tolerance": rms_tolerance,
                    "maximum_absolute_tolerance": maximum_absolute_tolerance,
                },
                FitErrorResult,
            ),
        )

    async def locate_instrument_ref_tie_in(
        self,
        instrument: CollectionInstrumentId,
        reference_group: CollectionObjectName,
        actuals_group: CollectionObjectName,
        *,
        tolerance: float = 0.0,
        auto_survey: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LocateInstrumentRefTieIn",
            "instrument_operations.locate_instrument_ref_tie_in",
            {
                "instrument": instrument,
                "reference_group": reference_group,
                "actuals_group": actuals_group,
                "tolerance": tolerance,
                "auto_survey": auto_survey,
            },
            None,
        )
        return None

    async def locate_instruments_usmn(
        self,
        instruments: Sequence[CollectionInstrumentId],
        output_group: CollectionObjectName,
        *,
        nominals_group: CollectionObjectName | None = None,
        move_in_working_frame: bool = False,
        auto_reject_outliers_and_resolve: bool = False,
        show_usmn_dialog: ShowUsmnDialog = ShowUsmnDialog.NO,
        maximum_acceptable_rms_error: float = 0.0,
        maximum_acceptable_error: float = 0.0,
        excluded_groups: Sequence[CollectionObjectName] = (),
        exclude_single_instrument_points: bool = False,
        run_uncertainty_field_analysis: bool = False,
        analysis_samples: int = 300,
        analysis_time_limit_minutes: float = 4.0,
    ) -> FitErrorResult:
        return cast(
            FitErrorResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LocateInstrumentsUsmn",
                "instrument_operations.locate_instruments_usmn",
                {
                    "instruments": instruments,
                    "nominals_group": nominals_group,
                    "output_group": output_group,
                    "move_in_working_frame": move_in_working_frame,
                    "auto_reject_outliers_and_resolve": auto_reject_outliers_and_resolve,
                    "show_usmn_dialog": show_usmn_dialog,
                    "maximum_acceptable_rms_error": maximum_acceptable_rms_error,
                    "maximum_acceptable_error": maximum_acceptable_error,
                    "excluded_groups": excluded_groups,
                    "exclude_single_instrument_points": exclude_single_instrument_points,
                    "run_uncertainty_field_analysis": run_uncertainty_field_analysis,
                    "analysis_samples": analysis_samples,
                    "analysis_time_limit_minutes": analysis_time_limit_minutes,
                },
                FitErrorResult,
            ),
        )

    async def lr_apdis_activate_mcm_calibration(
        self,
        instrument: CollectionInstrumentId,
        *,
        calibration_name: str = "",
        calibration_id: int = -1,
    ) -> str:
        return cast(
            str,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrApdisActivateMcmCalibration",
                "instrument_operations.lr_apdis_activate_mcm_calibration",
                {
                    "instrument": instrument,
                    "calibration_name": calibration_name,
                    "calibration_id": calibration_id,
                },
                None,
            ),
        )

    async def lr_apdis_get_active_mcm_calibration(
        self,
        instrument: CollectionInstrumentId,
    ) -> str:
        return cast(
            str,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrApdisGetActiveMcmCalibration",
                "instrument_operations.lr_apdis_get_active_mcm_calibration",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def lr_apdis_perform_mcm_calibration(
        self,
        instrument: CollectionInstrumentId,
        nominal_group: CollectionObjectName,
        *,
        use_matte_tooling_ball: bool = True,
        new_calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LrApdisPerformMcmCalibration",
            "instrument_operations.lr_apdis_perform_mcm_calibration",
            {
                "instrument": instrument,
                "nominal_group": nominal_group,
                "use_matte_tooling_ball": use_matte_tooling_ball,
                "new_calibration_name": new_calibration_name,
            },
            None,
        )
        return None

    async def lr_get_most_recent_snr_info(
        self,
        instrument: CollectionInstrumentId,
    ) -> LrSnrInfo:
        return cast(
            LrSnrInfo,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrGetMostRecentSnrInfo",
                "instrument_operations.lr_get_most_recent_snr_info",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def lr_hardware_connect(
        self,
        instrument: CollectionInstrumentId,
        host: str,
        port: int,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LrHardwareConnect",
            "instrument_operations.lr_hardware_connect",
            {
                "instrument": instrument,
                "host": host,
                "port": port,
            },
            None,
        )
        return None

    async def lr_hardware_disconnect(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LrHardwareDisconnect",
            "instrument_operations.lr_hardware_disconnect",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def lr_self_test(
        self,
        instrument: CollectionInstrumentId,
    ) -> LrSelfTestResult:
        return cast(
            LrSelfTestResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrSelfTest",
                "instrument_operations.lr_self_test",
                {
                    "instrument": instrument,
                },
                LrSelfTestResult,
            ),
        )

    async def lr_self_test_flip_test(
        self,
        instrument: CollectionInstrumentId,
    ) -> LrFlipTestResult:
        return cast(
            LrFlipTestResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrSelfTestFlipTest",
                "instrument_operations.lr_self_test_flip_test",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def lr_self_test_linearization(
        self,
        instrument: CollectionInstrumentId,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrSelfTestLinearization",
                "instrument_operations.lr_self_test_linearization",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def lr_self_test_lo_sep(
        self,
        instrument: CollectionInstrumentId,
        *,
        region: int = 0,
        num_range_measurements: int = 0,
    ) -> LrLoSeparationTestResult:
        return cast(
            LrLoSeparationTestResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrSelfTestLoSep",
                "instrument_operations.lr_self_test_lo_sep",
                {
                    "instrument": instrument,
                    "region": region,
                    "num_range_measurements": num_range_measurements,
                },
                None,
            ),
        )

    async def lr_set_red_laser_intensity(
        self,
        instrument: CollectionInstrumentId,
        *,
        intensity: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "LrSetRedLaserIntensity",
            "instrument_operations.lr_set_red_laser_intensity",
            {
                "instrument": instrument,
                "intensity": intensity,
            },
            None,
        )
        return None

    async def lr_verify_hardware_connection(
        self,
        instrument: CollectionInstrumentId,
    ) -> bool:
        return cast(
            bool,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "LrVerifyHardwareConnection",
                "instrument_operations.lr_verify_hardware_connection",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def make_collection_object_name_ref_list_from_objects_associated_with_instruments(
        self,
        instruments: Iterable[CollectionInstrumentId],
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "MakeCollectionObjectNameRefListFromObjectsAssociatedWithInstruments",
                "instrument_operations.make_collection_object_name_ref_list_from_objects_associated_with_instruments",
                {
                    "instruments": instruments,
                },
                None,
            ),
        )

    async def make_surface_face_list_from_point_proximity(
        self,
        measured_points: Sequence[PointName],
    ) -> SurfaceFaceList:
        return cast(
            SurfaceFaceList,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "MakeSurfaceFaceListFromPointProximity",
                "instrument_operations.make_surface_face_list_from_point_proximity",
                {
                    "measured_points": measured_points,
                },
                None,
            ),
        )

    async def measure(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "Measure",
            "instrument_operations.measure",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def measure_existing_single_point(
        self,
        instrument: CollectionInstrumentId,
        existing_target_id: PointName,
        group_name_for_new_point: CollectionObjectName,
        *,
        measure_immediately: bool = False,
        html_prompt_file: FileReference | None = None,
    ) -> PointName:
        return cast(
            PointName,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "MeasureExistingSinglePoint",
                "instrument_operations.measure_existing_single_point",
                {
                    "instrument": instrument,
                    "existing_target_id": existing_target_id,
                    "group_name_for_new_point": group_name_for_new_point,
                    "measure_immediately": measure_immediately,
                    "html_prompt_file": html_prompt_file,
                },
                None,
            ),
        )

    async def measure_existing_single_point_and_compare(
        self,
        instrument: CollectionInstrumentId,
        existing_target_id: PointName,
        group_name_for_new_point: CollectionObjectName,
        *,
        measure_immediately: bool = False,
        html_prompt_file: FileReference | None = None,
        tolerance: float = 0.0,
    ) -> PointComparisonResult:
        return cast(
            PointComparisonResult,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "MeasureExistingSinglePointAndCompare",
                "instrument_operations.measure_existing_single_point_and_compare",
                {
                    "instrument": instrument,
                    "existing_target_id": existing_target_id,
                    "group_name_for_new_point": group_name_for_new_point,
                    "measure_immediately": measure_immediately,
                    "html_prompt_file": html_prompt_file,
                    "tolerance": tolerance,
                },
                PointComparisonResult,
            ),
        )

    async def measure_existing_single_point_manual_guide(
        self,
        instrument: CollectionInstrumentId,
        existing_target_id: PointName,
        group_name_for_new_point: CollectionObjectName,
        *,
        measure_immediately: bool = False,
        html_prompt_file: FileReference | None = None,
    ) -> PointName:
        return cast(
            PointName,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "MeasureExistingSinglePointManualGuide",
                "instrument_operations.measure_existing_single_point_manual_guide",
                {
                    "instrument": instrument,
                    "existing_target_id": existing_target_id,
                    "group_name_for_new_point": group_name_for_new_point,
                    "measure_immediately": measure_immediately,
                    "html_prompt_file": html_prompt_file,
                },
                None,
            ),
        )

    async def measure_nominal_feature(
        self,
        instrument: CollectionInstrumentId,
        feature: CollectionObjectName,
        resulting_point: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MeasureNominalFeature",
            "instrument_operations.measure_nominal_feature",
            {
                "instrument": instrument,
                "feature": feature,
                "resulting_point": resulting_point,
            },
            None,
        )
        return None

    async def measure_single_point_here(
        self,
        instrument: CollectionInstrumentId,
        target_id: PointName,
        *,
        measure_immediately: bool = False,
        html_prompt_file: FileReference | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MeasureSinglePointHere",
            "instrument_operations.measure_single_point_here",
            {
                "instrument": instrument,
                "target_id": target_id,
                "measure_immediately": measure_immediately,
                "html_prompt_file": html_prompt_file,
            },
            None,
        )
        return None

    async def move_instrument_to_another_collection(
        self,
        instrument: CollectionInstrumentId,
        collection_name: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MoveInstrumentToAnotherCollection",
            "instrument_operations.move_instrument_to_another_collection",
            {
                "instrument": instrument,
                "collection_name": collection_name,
            },
            None,
        )
        return None

    async def move_measurement_observation(
        self,
        source_point_name: PointName,
        destination_point_name: PointName,
        *,
        observation_index: int = 0,
        delete_point_if_no_measurements_remain: bool = False,
        force_observation_active: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MoveMeasurementObservation",
            "instrument_operations.move_measurement_observation",
            {
                "source_point_name": source_point_name,
                "observation_index": observation_index,
                "delete_point_if_no_measurements_remain": delete_point_if_no_measurements_remain,
                "destination_point_name": destination_point_name,
                "force_observation_active": force_observation_active,
            },
            None,
        )
        return None

    async def move_objects_in_6d_using_instrument_updates(
        self,
        instrument: CollectionInstrumentId,
        objects_to_move: Iterable[CollectionObjectName],
        measurement_mode: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MoveObjectsIn6dUsingInstrumentUpdates",
            "instrument_operations.move_objects_in_6d_using_instrument_updates",
            {
                "instrument": instrument,
                "objects_to_move": objects_to_move,
                "measurement_mode": measurement_mode,
            },
            None,
        )
        return None

    async def multi_measurement_initiate(
        self,
        instruments: Sequence[CollectionInstrumentId],
        measurement_mode: str,
        *,
        wait_for_completion: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MultiMeasurementInitiate",
            "instrument_operations.multi_measurement_initiate",
            {
                "instruments": instruments,
                "measurement_mode": measurement_mode,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def multi_measurement_stop(
        self,
        instruments: Sequence[CollectionInstrumentId],
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "MultiMeasurementStop",
            "instrument_operations.multi_measurement_stop",
            {
                "instruments": instruments,
            },
            None,
        )
        return None

    async def point_at_target(
        self,
        instrument: CollectionInstrumentId,
        target_id: PointName,
        *,
        html_prompt_file: FileReference | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "PointAtTarget",
            "instrument_operations.point_at_target",
            {
                "instrument": instrument,
                "target_id": target_id,
                "html_prompt_file": html_prompt_file,
            },
            None,
        )
        return None

    async def quick_align(
        self,
        instruments: Iterable[CollectionInstrumentId],
        objects: Iterable[CollectionObjectName],
        *,
        nominal_points: Iterable[PointName] | None = None,
        nominal_point_of_view_names: Iterable[str] | None = None,
        align_to_individual_faces_only: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "QuickAlign",
            "instrument_operations.quick_align",
            {
                "instruments": instruments,
                "objects": objects,
                "nominal_points": nominal_points,
                "nominal_point_of_view_names": nominal_point_of_view_names,
                "align_to_individual_faces_only": align_to_individual_faces_only,
            },
            None,
        )
        return None

    async def rename_instrument(
        self,
        instrument: CollectionInstrumentId,
        new_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "RenameInstrument",
            "instrument_operations.rename_instrument",
            {
                "instrument": instrument,
                "new_name": new_name,
            },
            None,
        )
        return None

    async def save_cloud_viewer_point_cloud_file(
        self,
        instrument: CollectionInstrumentId,
        file_path: str,
        *,
        save_as_ascii: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SaveCloudViewerPointCloudFile",
            "instrument_operations.save_cloud_viewer_point_cloud_file",
            {
                "instrument": instrument,
                "file_path": file_path,
                "save_as_ascii": save_as_ascii,
            },
            None,
        )
        return None

    async def save_instrument_configuration(
        self,
        instrument: CollectionInstrumentId,
        configuration_file: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SaveInstrumentConfiguration",
            "instrument_operations.save_instrument_configuration",
            {
                "instrument": instrument,
                "configuration_file": configuration_file,
            },
            None,
        )
        return None

    async def scan_cad_faces(
        self,
        instrument: CollectionInstrumentId,
        surface_faces: SurfaceFaceList,
        parameter_set_name: str,
        *,
        enable_exclusions: bool = True,
        wait_for_completion: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ScanCadFaces",
            "instrument_operations.scan_cad_faces",
            {
                "instrument": instrument,
                "surface_faces": surface_faces,
                "parameter_set_name": parameter_set_name,
                "enable_exclusions": enable_exclusions,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def scan_within_perimeter(
        self,
        instrument: CollectionInstrumentId,
        scan_perimeters: Sequence[CollectionObjectName],
        exclusion_perimeters: Sequence[CollectionObjectName],
        parameter_set_name: str,
        point_group: CollectionObjectName,
        *,
        wait_for_completion: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "ScanWithinPerimeter",
            "instrument_operations.scan_within_perimeter",
            {
                "instrument": instrument,
                "scan_perimeters": scan_perimeters,
                "exclusion_perimeters": exclusion_perimeters,
                "parameter_set_name": parameter_set_name,
                "point_group": point_group,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def send_cloud_to_sa(
        self,
        instrument: CollectionInstrumentId,
        cloud_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SendCloudToSa",
            "instrument_operations.send_cloud_to_sa",
            {
                "instrument": instrument,
                "cloud_name": cloud_name,
            },
            None,
        )
        return None

    async def set_absolute_instrument_scale_factor(
        self,
        instrument: CollectionInstrumentId,
        *,
        scale_factor: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetAbsoluteInstrumentScaleFactor",
            "instrument_operations.set_absolute_instrument_scale_factor",
            {
                "instrument": instrument,
                "scale_factor": scale_factor,
            },
            None,
        )
        return None

    async def set_alignment_projector(
        self,
        instrument: CollectionInstrumentId,
        projector_profile: str,
        *,
        user_prompt: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetAlignmentProjector",
            "instrument_operations.set_alignment_projector",
            {
                "instrument": instrument,
                "projector_profile": projector_profile,
                "user_prompt": user_prompt,
            },
            None,
        )
        return None

    async def set_cloud_viewer_filter(
        self,
        instrument: CollectionInstrumentId,
        *,
        filter_value: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetCloudViewerFilter",
            "instrument_operations.set_cloud_viewer_filter",
            {
                "instrument": instrument,
                "filter_value": filter_value,
            },
            None,
        )
        return None

    async def set_inspection_verification_mode(
        self,
        *,
        verification_enabled: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInspectionVerificationMode",
            "instrument_operations.set_inspection_verification_mode",
            {
                "verification_enabled": verification_enabled,
            },
            None,
        )
        return None

    async def set_instrument_axes(
        self,
        instrument_to_adjust: CollectionInstrumentId,
        axis_values: Iterable[float],
        *,
        number_of_steps: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentAxes",
            "instrument_operations.set_instrument_axes",
            {
                "instrument_to_adjust": instrument_to_adjust,
                "axis_values": axis_values,
                "number_of_steps": number_of_steps,
            },
            None,
        )
        return None

    async def set_instrument_base_uncertainty_covariance_matrix_wrt_base(
        self,
        instrument: CollectionInstrumentId,
        covariance_matrix: UncertaintyCovarianceMatrix,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentBaseUncertaintyCovarianceMatrixWrtBase",
            "instrument_operations.set_instrument_base_uncertainty_covariance_matrix_wrt_base",
            {
                "instrument": instrument,
                "covariance_matrix": covariance_matrix,
            },
            None,
        )
        return None

    async def set_instrument_base_uncertainty_covariance_matrix_wrt_world(
        self,
        instrument: CollectionInstrumentId,
        covariance_matrix: UncertaintyCovarianceMatrix,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentBaseUncertaintyCovarianceMatrixWrtWorld",
            "instrument_operations.set_instrument_base_uncertainty_covariance_matrix_wrt_world",
            {
                "instrument": instrument,
                "covariance_matrix": covariance_matrix,
            },
            None,
        )
        return None

    async def set_instrument_group_and_target(
        self,
        instrument: CollectionInstrumentId,
        point: PointName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentGroupAndTarget",
            "instrument_operations.set_instrument_group_and_target",
            {
                "instrument": instrument,
                "point": point,
            },
            None,
        )
        return None

    async def set_instrument_interface_response_timeout(
        self,
        instrument: CollectionInstrumentId,
        *,
        timeout_seconds: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentInterfaceResponseTimeout",
            "instrument_operations.set_instrument_interface_response_timeout",
            {
                "instrument": instrument,
                "timeout_seconds": timeout_seconds,
            },
            None,
        )
        return None

    async def set_instrument_measurement_mode_profile(
        self,
        instrument: CollectionInstrumentId,
        mode_profile: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentMeasurementModeProfile",
            "instrument_operations.set_instrument_measurement_mode_profile",
            {
                "instrument": instrument,
                "mode_profile": mode_profile,
            },
            None,
        )
        return None

    async def set_instrument_targeting(
        self,
        instrument: CollectionInstrumentId,
        targeting_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentTargeting",
            "instrument_operations.set_instrument_targeting",
            {
                "instrument": instrument,
                "targeting_name": targeting_name,
            },
            None,
        )
        return None

    async def set_instrument_transform(
        self,
        instrument: CollectionInstrumentId,
        destination_transform: Transform,
        reference_frame: CollectionObjectName,
        *,
        number_of_steps: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentTransform",
            "instrument_operations.set_instrument_transform",
            {
                "instrument": instrument,
                "destination_transform": destination_transform,
                "reference_frame": reference_frame,
                "number_of_steps": number_of_steps,
            },
            None,
        )
        return None

    async def set_instrument_weather_setting(
        self,
        instrument: CollectionInstrumentId,
        *,
        temperature_fahrenheit: float = 0.0,
        pressure_mmhg: float = 0.0,
        relative_humidity_percent: float = 0.0,
        set_automatically: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetInstrumentWeatherSetting",
            "instrument_operations.set_instrument_weather_setting",
            {
                "instrument": instrument,
                "temperature_fahrenheit": temperature_fahrenheit,
                "pressure_mmhg": pressure_mmhg,
                "relative_humidity_percent": relative_humidity_percent,
                "set_automatically": set_automatically,
            },
            None,
        )
        return None

    async def set_ladar_auto_meas_point(
        self,
        instrument: CollectionInstrumentId,
        *,
        sample_time_milliseconds: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarAutoMeasPoint",
            "instrument_operations.set_ladar_auto_meas_point",
            {
                "instrument": instrument,
                "sample_time_milliseconds": sample_time_milliseconds,
            },
            None,
        )
        return None

    async def set_ladar_auto_meas_sphere(
        self,
        instrument: CollectionInstrumentId,
        *,
        sphere_radius: float = 1.1875,
        scan_line_spacing: float = 0.05,
        send_center_point: bool = True,
        send_sphere: bool = False,
        send_measured_cloud: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarAutoMeasSphere",
            "instrument_operations.set_ladar_auto_meas_sphere",
            {
                "instrument": instrument,
                "sphere_radius": sphere_radius,
                "scan_line_spacing": scan_line_spacing,
                "send_center_point": send_center_point,
                "send_sphere": send_sphere,
                "send_measured_cloud": send_measured_cloud,
            },
            None,
        )
        return None

    async def set_ladar_feature_meas_circle(
        self,
        instrument: CollectionInstrumentId,
        *,
        scan_line_spacing: float = 0.05,
        width_of_extra_area_around_scan: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarFeatureMeasCircle",
            "instrument_operations.set_ladar_feature_meas_circle",
            {
                "instrument": instrument,
                "scan_line_spacing": scan_line_spacing,
                "width_of_extra_area_around_scan": width_of_extra_area_around_scan,
            },
            None,
        )
        return None

    async def set_ladar_feature_meas_cylinder(
        self,
        instrument: CollectionInstrumentId,
        *,
        scan_line_spacing: float = 0.05,
        width_of_extra_area_around_scan: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarFeatureMeasCylinder",
            "instrument_operations.set_ladar_feature_meas_cylinder",
            {
                "instrument": instrument,
                "scan_line_spacing": scan_line_spacing,
                "width_of_extra_area_around_scan": width_of_extra_area_around_scan,
            },
            None,
        )
        return None

    async def set_ladar_feature_meas_slot(
        self,
        instrument: CollectionInstrumentId,
        *,
        scan_line_spacing: float = 0.05,
        width_of_extra_area_around_scan: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarFeatureMeasSlot",
            "instrument_operations.set_ladar_feature_meas_slot",
            {
                "instrument": instrument,
                "scan_line_spacing": scan_line_spacing,
                "width_of_extra_area_around_scan": width_of_extra_area_around_scan,
            },
            None,
        )
        return None

    async def set_ladar_feature_meas_sphere(
        self,
        instrument: CollectionInstrumentId,
        *,
        scan_line_spacing: float = 0.05,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetLadarFeatureMeasSphere",
            "instrument_operations.set_ladar_feature_meas_sphere",
            {
                "instrument": instrument,
                "scan_line_spacing": scan_line_spacing,
            },
            None,
        )
        return None

    async def set_multiply_instrument_scale_factor(
        self,
        instrument: CollectionInstrumentId,
        *,
        scale_factor: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetMultiplyInstrumentScaleFactor",
            "instrument_operations.set_multiply_instrument_scale_factor",
            {
                "instrument": instrument,
                "scale_factor": scale_factor,
            },
            None,
        )
        return None

    async def set_observation_collimation_shot_options(
        self,
        point: PointName,
        *,
        observation_index: int = 0,
        is_collimation_shot: bool = False,
        targeted_instrument: CollectionInstrumentId | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetObservationCollimationShotOptions",
            "instrument_operations.set_observation_collimation_shot_options",
            {
                "point": point,
                "observation_index": observation_index,
                "is_collimation_shot": is_collimation_shot,
                "targeted_instrument": targeted_instrument,
            },
            None,
        )
        return None

    async def set_observation_mirror_cube_shot_face(
        self,
        point: PointName,
        *,
        observation_index: int = 0,
        is_mirror_cube_shot: bool = False,
        mirror_cube_shot_face: int = 1,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetObservationMirrorCubeShotFace",
            "instrument_operations.set_observation_mirror_cube_shot_face",
            {
                "point": point,
                "observation_index": observation_index,
                "is_mirror_cube_shot": is_mirror_cube_shot,
                "mirror_cube_shot_face": mirror_cube_shot_face,
            },
            None,
        )
        return None

    async def set_observation_status(
        self,
        point: PointName,
        *,
        observation_index: int = 0,
        active: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetObservationStatus",
            "instrument_operations.set_observation_status",
            {
                "point": point,
                "observation_index": observation_index,
                "active": active,
            },
            None,
        )
        return None

    async def set_pcmm_instrument_xyz_uncertainties(
        self,
        instrument: CollectionInstrumentId,
        *,
        x_uncertainty: float = 0.001,
        y_uncertainty: float = 0.001,
        z_uncertainty: float = 0.001,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetPcmmInstrumentXyzUncertainties",
            "instrument_operations.set_pcmm_instrument_xyz_uncertainties",
            {
                "instrument": instrument,
                "x_uncertainty": x_uncertainty,
                "y_uncertainty": y_uncertainty,
                "z_uncertainty": z_uncertainty,
            },
            None,
        )
        return None

    async def set_probe_offset_frame_offline(
        self,
        instrument: CollectionInstrumentId,
        probe_name: str,
        raw_measured_frame: CollectionObjectName,
        offset_frame: CollectionObjectName,
        *,
        face_id: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetProbeOffsetFrameOffline",
            "instrument_operations.set_probe_offset_frame_offline",
            {
                "instrument": instrument,
                "probe_name": probe_name,
                "face_id": face_id,
                "raw_measured_frame": raw_measured_frame,
                "offset_frame": offset_frame,
            },
            None,
        )
        return None

    async def set_probe_offset_frame_online(
        self,
        instrument: CollectionInstrumentId,
        probe_name: str,
        offset_frame: CollectionObjectName,
        *,
        face_id: int = 0,
        measure_profile_name: str = "",
        timeout_seconds: float = 15.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetProbeOffsetFrameOnline",
            "instrument_operations.set_probe_offset_frame_online",
            {
                "instrument": instrument,
                "probe_name": probe_name,
                "face_id": face_id,
                "measure_profile_name": measure_profile_name,
                "timeout_seconds": timeout_seconds,
                "offset_frame": offset_frame,
            },
            None,
        )
        return None

    async def set_remeasure_failed_checks_only(
        self,
        collection: CollectionName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetRemeasureFailedChecksOnly",
            "instrument_operations.set_remeasure_failed_checks_only",
            {
                "collection": collection,
            },
            None,
        )
        return None

    async def set_target_computation_options(
        self,
        *,
        computation_method: TargetComputationMethod = TargetComputationMethod.USE_MOST_RECENT_SHOT_FROM_EACH_FACE,
        ignore_distance_measurements: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetTargetComputationOptions",
            "instrument_operations.set_target_computation_options",
            {
                "computation_method": computation_method,
                "ignore_distance_measurements": ignore_distance_measurements,
            },
            None,
        )
        return None

    async def set_tracker_edm_theodolite_uncertainties(
        self,
        instrument: CollectionInstrumentId,
        *,
        theta_dispersion_arcseconds: float = 1.0,
        theta_threshold: float = 0.001,
        phi_dispersion_arcseconds: float = 1.0,
        phi_threshold: float = 0.001,
        distance_ppm: float = 2.5,
        distance_threshold: float = 0.0003,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetTrackerEdmTheodoliteUncertainties",
            "instrument_operations.set_tracker_edm_theodolite_uncertainties",
            {
                "instrument": instrument,
                "theta_dispersion_arcseconds": theta_dispersion_arcseconds,
                "theta_threshold": theta_threshold,
                "phi_dispersion_arcseconds": phi_dispersion_arcseconds,
                "phi_threshold": phi_threshold,
                "distance_ppm": distance_ppm,
                "distance_threshold": distance_threshold,
            },
            None,
        )
        return None

    async def set_wrtl_channel(
        self,
        instrument: CollectionInstrumentId,
        *,
        channel: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetWrtlChannel",
            "instrument_operations.set_wrtl_channel",
            {
                "instrument": instrument,
                "channel": channel,
            },
            None,
        )
        return None

    async def set_xyz_instrument_uncertainties(
        self,
        instrument: CollectionInstrumentId,
        *,
        x_uncertainty: float = 0.0005,
        y_uncertainty: float = 0.0005,
        z_uncertainty: float = 0.0005,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetXyzInstrumentUncertainties",
            "instrument_operations.set_xyz_instrument_uncertainties",
            {
                "instrument": instrument,
                "x_uncertainty": x_uncertainty,
                "y_uncertainty": y_uncertainty,
                "z_uncertainty": z_uncertainty,
            },
            None,
        )
        return None

    async def set_xyz_reference_frame_instrument_base_anchor_frame(
        self,
        instrument: CollectionInstrumentId,
        anchor_frame: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SetXyzReferenceFrameInstrumentBaseAnchorFrame",
            "instrument_operations.set_xyz_reference_frame_instrument_base_anchor_frame",
            {
                "instrument": instrument,
                "anchor_frame": anchor_frame,
            },
            None,
        )
        return None

    async def start_gdt_inspection(
        self,
        instrument: CollectionInstrumentId,
        collection: CollectionName,
        *,
        filter: InspectionFilter = InspectionFilter.ALL,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StartGdtInspection",
            "instrument_operations.start_gdt_inspection",
            {
                "instrument": instrument,
                "collection": collection,
                "filter": filter,
            },
            None,
        )
        return None

    async def start_gdt_inspection_design(
        self,
        collection: CollectionName,
        *,
        filter: InspectionFilter = InspectionFilter.ALL,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StartGdtInspectionDesign",
            "instrument_operations.start_gdt_inspection_design",
            {
                "collection": collection,
                "filter": filter,
            },
            None,
        )
        return None

    async def start_gdt_inspection_rehearse(
        self,
        collection: CollectionName,
        *,
        filter: InspectionFilter = InspectionFilter.ALL,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StartGdtInspectionRehearse",
            "instrument_operations.start_gdt_inspection_rehearse",
            {
                "collection": collection,
                "filter": filter,
            },
            None,
        )
        return None

    async def start_instrument_interface(
        self,
        instrument: CollectionInstrumentId,
        *,
        initialize_at_startup: bool = False,
        device_ip_address: str | None = None,
        interface_type: int = 0,
        run_in_simulation: bool = False,
        allow_start_without_initialization_requirements: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StartInstrumentInterface",
            "instrument_operations.start_instrument_interface",
            {
                "instrument": instrument,
                "initialize_at_startup": initialize_at_startup,
                "device_ip_address": device_ip_address,
                "interface_type": interface_type,
                "run_in_simulation": run_in_simulation,
                "allow_start_without_initialization_requirements": allow_start_without_initialization_requirements,
            },
            None,
        )
        return None

    async def start_theodolite_interface(
        self,
        instrument: CollectionInstrumentId,
        theodolite_type: str,
        *,
        comm_port: int = 0,
        device_ip_address: str | None = None,
        simulation: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StartTheodoliteInterface",
            "instrument_operations.start_theodolite_interface",
            {
                "instrument": instrument,
                "theodolite_type": theodolite_type,
                "comm_port": comm_port,
                "device_ip_address": device_ip_address,
                "simulation": simulation,
            },
            None,
        )
        return None

    async def stop_active_measurement_mode(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StopActiveMeasurementMode",
            "instrument_operations.stop_active_measurement_mode",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def stop_instrument_interface(
        self,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "StopInstrumentInterface",
            "instrument_operations.stop_instrument_interface",
            {
                "instrument": instrument,
            },
            None,
        )
        return None

    async def synchronized_measurement_master_slave(
        self,
        master_instrument: CollectionInstrumentId,
        slave_instrument: CollectionInstrumentId,
        *,
        slave_group_suffix: str = "_Slave",
        locate_one_of_the_instruments: bool = True,
        locate_master: bool = False,
        wait_for_completion: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "SynchronizedMeasurementMasterSlave",
            "instrument_operations.synchronized_measurement_master_slave",
            {
                "master_instrument": master_instrument,
                "slave_instrument": slave_instrument,
                "slave_group_suffix": slave_group_suffix,
                "locate_one_of_the_instruments": locate_one_of_the_instruments,
                "locate_master": locate_master,
                "wait_for_completion": wait_for_completion,
            },
            None,
        )
        return None

    async def track_tape_measurement(
        self,
        instrument: CollectionInstrumentId,
        point_on_tape: PointName,
        point_on_part: PointName,
        direction_point: PointName,
        termination_point: PointName,
        parameter_set_name: str,
        point_group: CollectionObjectName,
        initial_target_name: str,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "TrackTapeMeasurement",
            "instrument_operations.track_tape_measurement",
            {
                "instrument": instrument,
                "point_on_tape": point_on_tape,
                "point_on_part": point_on_part,
                "direction_point": direction_point,
                "termination_point": termination_point,
                "parameter_set_name": parameter_set_name,
                "point_group": point_group,
                "initial_target_name": initial_target_name,
            },
            None,
        )
        return None

    async def transform_instrument_by_delta(
        self,
        instrument: CollectionInstrumentId,
        delta_transform: WorldTransform,
        *,
        apply_scale_to_instrument: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "TransformInstrumentByDelta",
            "instrument_operations.transform_instrument_by_delta",
            {
                "instrument": instrument,
                "delta_transform": delta_transform,
                "apply_scale_to_instrument": apply_scale_to_instrument,
            },
            None,
        )
        return None

    async def transform_instrument_frame_to_frame(
        self,
        instrument: CollectionInstrumentId,
        initial_frame: CollectionObjectName,
        destination_frame: CollectionObjectName,
        *,
        number_of_steps: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "TransformInstrumentFrameToFrame",
            "instrument_operations.transform_instrument_frame_to_frame",
            {
                "instrument": instrument,
                "initial_frame": initial_frame,
                "destination_frame": destination_frame,
                "number_of_steps": number_of_steps,
            },
            None,
        )
        return None

    async def transform_multiple_instruments_by_delta(
        self,
        instruments: Sequence[CollectionInstrumentId],
        delta_transform: WorldTransform,
        *,
        apply_scale_to_instruments: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "TransformMultipleInstrumentsByDelta",
            "instrument_operations.transform_multiple_instruments_by_delta",
            {
                "instruments": instruments,
                "delta_transform": delta_transform,
                "apply_scale_to_instruments": apply_scale_to_instruments,
            },
            None,
        )
        return None

    async def verify_instrument_connection(
        self,
        instrument: CollectionInstrumentId,
    ) -> bool:
        return cast(
            bool,
            await self._client._invoke_mp_operation(
                "briosa.InstrumentOperations",
                "VerifyInstrumentConnection",
                "instrument_operations.verify_instrument_connection",
                {
                    "instrument": instrument,
                },
                None,
            ),
        )

    async def wait_for_trapping_to_complete(
        self,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WaitForTrappingToComplete",
            "instrument_operations.wait_for_trapping_to_complete",
            {},
            None,
        )
        return None

    async def watch_closest_point(
        self,
        instrument: CollectionInstrumentId,
        groups_to_consider: Iterable[CollectionObjectName],
        watch_window_properties: CollectionObjectName,
        *,
        measurement_mode: str = "",
        pause_mp_until_closed: bool = False,
        window_top_left_x: int = 0,
        window_top_left_y: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchClosestPoint",
            "instrument_operations.watch_closest_point",
            {
                "instrument": instrument,
                "groups_to_consider": groups_to_consider,
                "watch_window_properties": watch_window_properties,
                "measurement_mode": measurement_mode,
                "pause_mp_until_closed": pause_mp_until_closed,
                "window_top_left_x": window_top_left_x,
                "window_top_left_y": window_top_left_y,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None

    async def watch_instrument(
        self,
        instrument: CollectionInstrumentId,
        watch_window_properties: CollectionObjectName,
        *,
        pause_mp_until_closed: bool = False,
        window_top_left_x: int = 0,
        window_top_left_y: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchInstrument",
            "instrument_operations.watch_instrument",
            {
                "instrument": instrument,
                "pause_mp_until_closed": pause_mp_until_closed,
                "watch_window_properties": watch_window_properties,
                "window_top_left_x": window_top_left_x,
                "window_top_left_y": window_top_left_y,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None

    async def watch_point_to_edge(
        self,
        instrument: CollectionInstrumentId,
        projection_reference_objects: Iterable[CollectionObjectName],
        measurement_reference_objects: Iterable[CollectionObjectName],
        projection_options: ProjectionOptions,
        watch_window_properties: CollectionObjectName,
        *,
        measurement_mode: str = "",
        pause_mp_until_closed: bool = False,
        window_top_left_x: int = 0,
        window_top_left_y: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchPointToEdge",
            "instrument_operations.watch_point_to_edge",
            {
                "instrument": instrument,
                "projection_reference_objects": projection_reference_objects,
                "measurement_reference_objects": measurement_reference_objects,
                "projection_options": projection_options,
                "watch_window_properties": watch_window_properties,
                "measurement_mode": measurement_mode,
                "pause_mp_until_closed": pause_mp_until_closed,
                "window_top_left_x": window_top_left_x,
                "window_top_left_y": window_top_left_y,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None

    async def watch_point_to_objects(
        self,
        instrument: CollectionInstrumentId,
        objects_to_consider: Iterable[CollectionObjectName],
        projection_options: ProjectionOptions,
        watch_window_properties: CollectionObjectName,
        *,
        measurement_mode: str = "",
        pause_mp_until_closed: bool = False,
        window_top_left_x: int = 0,
        window_top_left_y: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchPointToObjects",
            "instrument_operations.watch_point_to_objects",
            {
                "instrument": instrument,
                "objects_to_consider": objects_to_consider,
                "projection_options": projection_options,
                "watch_window_properties": watch_window_properties,
                "measurement_mode": measurement_mode,
                "pause_mp_until_closed": pause_mp_until_closed,
                "window_top_left_x": window_top_left_x,
                "window_top_left_y": window_top_left_y,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None

    async def watch_point_to_point(
        self,
        instrument: CollectionInstrumentId,
        reference_point: PointName,
        watch_window_properties: CollectionObjectName,
        *,
        measurement_mode: str = "",
        pause_mp_until_closed: bool = False,
        window_top_left_x: int = 0,
        window_top_left_y: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchPointToPoint",
            "instrument_operations.watch_point_to_point",
            {
                "instrument": instrument,
                "reference_point": reference_point,
                "watch_window_properties": watch_window_properties,
                "measurement_mode": measurement_mode,
                "pause_mp_until_closed": pause_mp_until_closed,
                "window_top_left_x": window_top_left_x,
                "window_top_left_y": window_top_left_y,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None

    async def watch_point_to_point_with_view_zooming(
        self,
        instrument: CollectionInstrumentId,
        reference_point: PointName,
        *,
        update: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.InstrumentOperations",
            "WatchPointToPointWithViewZooming",
            "instrument_operations.watch_point_to_point_with_view_zooming",
            {
                "instrument": instrument,
                "reference_point": reference_point,
                "update": update,
            },
            None,
        )
        return None


class RobotCalibrationApplianceNodeOperations:
    def __init__(self, client: _WaveBClient) -> None:
        self._client = client

    async def add_calibration_appliance_node(
        self,
        calibration_appliance_node_to_add: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "AddCalibrationApplianceNode",
            "robot_calibration_appliance_node_operations.add_calibration_appliance_node",
            {
                "calibration_appliance_node_to_add": calibration_appliance_node_to_add,
            },
            None,
        )
        return None

    async def clear_calibration_appliance_node_trap_manager_requests(
        self,
        calibration_appliance_node: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "ClearCalibrationApplianceNodeTrapManagerRequests",
            "robot_calibration_appliance_node_operations.clear_calibration_appliance_node_trap_manager_requests",
            {
                "calibration_appliance_node": calibration_appliance_node,
            },
            None,
        )
        return None

    async def connect_disconnect_calibration_appliance_node(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        connect: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "ConnectDisconnectCalibrationApplianceNode",
            "robot_calibration_appliance_node_operations.connect_disconnect_calibration_appliance_node",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "connect": connect,
            },
            None,
        )
        return None

    async def delete_calibration_appliance_node(
        self,
        calibration_appliance_node_to_delete: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "DeleteCalibrationApplianceNode",
            "robot_calibration_appliance_node_operations.delete_calibration_appliance_node",
            {
                "calibration_appliance_node_to_delete": calibration_appliance_node_to_delete,
            },
            None,
        )
        return None

    async def enable_disable_calibration_appliance_node_instrument_auto_point(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        enable_instrument_auto_point: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "EnableDisableCalibrationApplianceNodeInstrumentAutoPoint",
            "robot_calibration_appliance_node_operations.enable_disable_calibration_appliance_node_instrument_auto_point",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "enable_instrument_auto_point": enable_instrument_auto_point,
            },
            None,
        )
        return None

    async def enable_disable_calibration_appliance_node_trap_manager(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        enable: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "EnableDisableCalibrationApplianceNodeTrapManager",
            "robot_calibration_appliance_node_operations.enable_disable_calibration_appliance_node_trap_manager",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "enable": enable,
            },
            None,
        )
        return None

    async def get_calibration_appliance_node_data(
        self,
        calibration_appliance_node: CollectionObjectName,
        real_value_count: int,
    ) -> list[float]:
        return cast(
            list[float],
            await self._client._invoke_mp_operation(
                "briosa.RobotCalibrationApplianceNodeOperations",
                "GetCalibrationApplianceNodeData",
                "robot_calibration_appliance_node_operations.get_calibration_appliance_node_data",
                {
                    "calibration_appliance_node": calibration_appliance_node,
                    "real_value_count": real_value_count,
                },
                None,
            ),
        )

    async def get_calibration_appliance_node_integer_value(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        index_offset: int = 0,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.RobotCalibrationApplianceNodeOperations",
                "GetCalibrationApplianceNodeIntegerValue",
                "robot_calibration_appliance_node_operations.get_calibration_appliance_node_integer_value",
                {
                    "calibration_appliance_node": calibration_appliance_node,
                    "index_offset": index_offset,
                },
                None,
            ),
        )

    async def get_calibration_appliance_node_real_value(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        index_offset: int = 0,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.RobotCalibrationApplianceNodeOperations",
                "GetCalibrationApplianceNodeRealValue",
                "robot_calibration_appliance_node_operations.get_calibration_appliance_node_real_value",
                {
                    "calibration_appliance_node": calibration_appliance_node,
                    "index_offset": index_offset,
                },
                None,
            ),
        )

    async def get_calibration_appliance_node_status(
        self,
        calibration_appliance_node: CollectionObjectName,
    ) -> CalibrationApplianceNodeStatus:
        return cast(
            CalibrationApplianceNodeStatus,
            await self._client._invoke_mp_operation(
                "briosa.RobotCalibrationApplianceNodeOperations",
                "GetCalibrationApplianceNodeStatus",
                "robot_calibration_appliance_node_operations.get_calibration_appliance_node_status",
                {
                    "calibration_appliance_node": calibration_appliance_node,
                },
                CalibrationApplianceNodeStatus,
            ),
        )

    async def set_calibration_appliance_node_calibration_appliance_ip_address(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        calibration_appliance_ip_address: str = "0.0.0.0",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeCalibrationApplianceIpAddress",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_calibration_appliance_ip_address",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "calibration_appliance_ip_address": calibration_appliance_ip_address,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_display_robot(
        self,
        calibration_appliance_node: CollectionObjectName,
        machine_id: CollectionMachineId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeDisplayRobot",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_display_robot",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "machine_id": machine_id,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_instrument(
        self,
        calibration_appliance_node: CollectionObjectName,
        instrument: CollectionInstrumentId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeInstrument",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_instrument",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "instrument": instrument,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_instrument_dwell_time(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        measurement_dwell_time_seconds: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeInstrumentDwellTime",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_instrument_dwell_time",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "measurement_dwell_time_seconds": measurement_dwell_time_seconds,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_integer_value(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        index_offset: int = 0,
        integer_value: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeIntegerValue",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_integer_value",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "index_offset": index_offset,
                "integer_value": integer_value,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_measurement_frame(
        self,
        calibration_appliance_node: CollectionObjectName,
        measurement_reference_frame: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeMeasurementFrame",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_frame",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "measurement_reference_frame": measurement_reference_frame,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_measurement_offset_transform(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        measurement_offset_transform: Transform | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeMeasurementOffsetTransform",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_offset_transform",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "measurement_offset_transform": measurement_offset_transform,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_measurement_point_group(
        self,
        calibration_appliance_node: CollectionObjectName,
        point_group_name: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeMeasurementPointGroup",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_point_group",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "point_group_name": point_group_name,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_measurement_profile(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        measurement_profile: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeMeasurementProfile",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_profile",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "measurement_profile": measurement_profile,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_measurement_target(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        measurement_target: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeMeasurementTarget",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_target",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "measurement_target": measurement_target,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_real_value(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        index_offset: int = 0,
        real_value: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeRealValue",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_real_value",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "index_offset": index_offset,
                "real_value": real_value,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_trapping_node_id(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        trapping_node_id: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeTrappingNodeId",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_trapping_node_id",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "trapping_node_id": trapping_node_id,
            },
            None,
        )
        return None

    async def skip_calibration_appliance_node_measurement(
        self,
        calibration_appliance_node: CollectionObjectName,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SkipCalibrationApplianceNodeMeasurement",
            "robot_calibration_appliance_node_operations.skip_calibration_appliance_node_measurement",
            {
                "calibration_appliance_node": calibration_appliance_node,
            },
            None,
        )
        return None

    async def update_calibration_appliance_node_display_robot_joints(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        enable_display_robot_joint_updates: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "UpdateCalibrationApplianceNodeDisplayRobotJoints",
            "robot_calibration_appliance_node_operations.update_calibration_appliance_node_display_robot_joints",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "enable_display_robot_joint_updates": enable_display_robot_joint_updates,
            },
            None,
        )
        return None

    async def set_calibration_appliance_node_data(
        self,
        calibration_appliance_node: CollectionObjectName,
        *,
        real_values: Iterable[float] = (),
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotCalibrationApplianceNodeOperations",
            "SetCalibrationApplianceNodeData",
            "robot_calibration_appliance_node_operations.set_calibration_appliance_node_data",
            {
                "calibration_appliance_node": calibration_appliance_node,
                "real_values": real_values,
            },
            None,
        )
        return None


class RobotOperations:
    def __init__(self, client: _WaveBClient) -> None:
        self._client = client

    async def add_robot_machine_manip_kin(
        self,
        manip_kin_file: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "AddRobotMachineManipKin",
            "robot_operations.add_robot_machine_manip_kin",
            {
                "manip_kin_file": manip_kin_file,
            },
            None,
        )
        return None

    async def add_robot_machine_sa_machine(
        self,
        sa_machine_file: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "AddRobotMachineSaMachine",
            "robot_operations.add_robot_machine_sa_machine",
            {
                "sa_machine_file": sa_machine_file,
            },
            None,
        )
        return None

    async def compute_robot_machine_adjusted_goal_frame(
        self,
        original_goal_frame: CollectionObjectName,
        last_adjusted_goal_frame: CollectionObjectName,
        actual_measured_frame: CollectionObjectName,
        modified_goal_frame: CollectionObjectName,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "ComputeRobotMachineAdjustedGoalFrame",
                "robot_operations.compute_robot_machine_adjusted_goal_frame",
                {
                    "original_goal_frame": original_goal_frame,
                    "last_adjusted_goal_frame": last_adjusted_goal_frame,
                    "actual_measured_frame": actual_measured_frame,
                    "modified_goal_frame": modified_goal_frame,
                },
                None,
            ),
        )

    async def create_robot_calibration(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "CreateRobotCalibration",
            "robot_operations.create_robot_calibration",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
            },
            None,
        )
        return None

    async def delete_robot_calibration(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "DeleteRobotCalibration",
            "robot_operations.delete_robot_calibration",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
            },
            None,
        )
        return None

    async def delete_robot_machine(
        self,
        machine_id: CollectionMachineId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "DeleteRobotMachine",
            "robot_operations.delete_robot_machine",
            {
                "machine_id": machine_id,
            },
            None,
        )
        return None

    async def get_calibration_appliance_data(
        self,
        real_value_count: int,
    ) -> list[float]:
        return cast(
            list[float],
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetCalibrationApplianceData",
                "robot_operations.get_calibration_appliance_data",
                {
                    "real_value_count": real_value_count,
                },
                None,
            ),
        )

    async def get_calibration_appliance_integer_value(
        self,
        *,
        index_offset: int = 0,
    ) -> int:
        return cast(
            int,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetCalibrationApplianceIntegerValue",
                "robot_operations.get_calibration_appliance_integer_value",
                {
                    "index_offset": index_offset,
                },
                None,
            ),
        )

    async def get_calibration_appliance_real_value(
        self,
        *,
        index_offset: int = 0,
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetCalibrationApplianceRealValue",
                "robot_operations.get_calibration_appliance_real_value",
                {
                    "index_offset": index_offset,
                },
                None,
            ),
        )

    async def get_robot_machine_model_link_parameters(
        self,
        machine_id: CollectionMachineId,
        *,
        link_name: str = "",
    ) -> RobotModelLinkParameters:
        return cast(
            RobotModelLinkParameters,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetRobotMachineModelLinkParameters",
                "robot_operations.get_robot_machine_model_link_parameters",
                {
                    "machine_id": machine_id,
                    "link_name": link_name,
                },
                RobotModelLinkParameters,
            ),
        )

    async def get_robot_machine_parameter(
        self,
        machine_id: CollectionMachineId,
        *,
        parameter_name: str = "",
    ) -> float:
        return cast(
            float,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetRobotMachineParameter",
                "robot_operations.get_robot_machine_parameter",
                {
                    "machine_id": machine_id,
                    "parameter_name": parameter_name,
                },
                None,
            ),
        )

    async def import_poses_match_to_frames(
        self,
        machine_id: CollectionMachineId,
        frame_names: Iterable[CollectionObjectName],
        csv_joint_set_file: FileReference,
        *,
        calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "ImportPosesMatchToFrames",
            "robot_operations.import_poses_match_to_frames",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
                "frame_names": frame_names,
                "csv_joint_set_file": csv_joint_set_file,
            },
            None,
        )
        return None

    async def import_poses_match_to_measurements(
        self,
        machine_id: CollectionMachineId,
        point_names: Iterable[PointName],
        csv_joint_set_file: FileReference,
        *,
        calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "ImportPosesMatchToMeasurements",
            "robot_operations.import_poses_match_to_measurements",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
                "point_names": point_names,
                "csv_joint_set_file": csv_joint_set_file,
            },
            None,
        )
        return None

    async def move_robot_machine_through_path(
        self,
        machine_id: CollectionMachineId,
        path_frames: Iterable[CollectionObjectName],
        *,
        use_sa_kinematics: bool = True,
        linear_segments: bool = False,
        acknowledge_arrival: bool = True,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "MoveRobotMachineThroughPath",
            "robot_operations.move_robot_machine_through_path",
            {
                "machine_id": machine_id,
                "path_frames": path_frames,
                "use_sa_kinematics": use_sa_kinematics,
                "linear_segments": linear_segments,
                "acknowledge_arrival": acknowledge_arrival,
            },
            None,
        )
        return None

    async def move_robot_machine_to_frame(
        self,
        machine_id: CollectionMachineId,
        destination_frame: CollectionObjectName,
        *,
        use_sa_kinematics: bool = False,
        acknowledge_arrival: bool = False,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "MoveRobotMachineToFrame",
                "robot_operations.move_robot_machine_to_frame",
                {
                    "machine_id": machine_id,
                    "destination_frame": destination_frame,
                    "use_sa_kinematics": use_sa_kinematics,
                    "acknowledge_arrival": acknowledge_arrival,
                },
                None,
            ),
        )

    async def move_robot_machine_to_joint_pose_six_dof(
        self,
        machine_id: CollectionMachineId,
        *,
        joint_1: float = 0.0,
        joint_2: float = 0.0,
        joint_3: float = 0.0,
        joint_4: float = 0.0,
        joint_5: float = 0.0,
        joint_6: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "MoveRobotMachineToJointPoseSixDof",
            "robot_operations.move_robot_machine_to_joint_pose_six_dof",
            {
                "machine_id": machine_id,
                "joint_1": joint_1,
                "joint_2": joint_2,
                "joint_3": joint_3,
                "joint_4": joint_4,
                "joint_5": joint_5,
                "joint_6": joint_6,
            },
            None,
        )
        return None

    async def move_robot_machine_to_named_destination(
        self,
        machine_id: CollectionMachineId,
        *,
        destination_name: str = "",
        acknowledge_arrival: bool = False,
    ) -> Transform:
        return cast(
            Transform,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "MoveRobotMachineToNamedDestination",
                "robot_operations.move_robot_machine_to_named_destination",
                {
                    "machine_id": machine_id,
                    "destination_name": destination_name,
                    "acknowledge_arrival": acknowledge_arrival,
                },
                None,
            ),
        )

    async def perform_robot_calibration_alternate(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
        set_current_base_as_nominal: bool = False,
        base_degrees_of_freedom: str = "",
        robot_degrees_of_freedom: str = "",
        tool_degrees_of_freedom: str = "",
        show_interface: bool = False,
        allowed_outlier_rejection_count: int = 0,
        allowable_maximum_error: float = 0.0,
        allowable_average_error: float = 0.0,
    ) -> RobotCalibrationMetrics:
        return cast(
            RobotCalibrationMetrics,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "PerformRobotCalibrationAlternate",
                "robot_operations.perform_robot_calibration_alternate",
                {
                    "machine_id": machine_id,
                    "calibration_name": calibration_name,
                    "set_current_base_as_nominal": set_current_base_as_nominal,
                    "base_degrees_of_freedom": base_degrees_of_freedom,
                    "robot_degrees_of_freedom": robot_degrees_of_freedom,
                    "tool_degrees_of_freedom": tool_degrees_of_freedom,
                    "show_interface": show_interface,
                    "allowed_outlier_rejection_count": allowed_outlier_rejection_count,
                    "allowable_maximum_error": allowable_maximum_error,
                    "allowable_average_error": allowable_average_error,
                },
                None,
            ),
        )

    async def set_active_robot_calibration(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetActiveRobotCalibration",
            "robot_operations.set_active_robot_calibration",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
            },
            None,
        )
        return None

    async def set_calibration_appliance_integer_value(
        self,
        *,
        index_offset: int = 0,
        integer_value: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetCalibrationApplianceIntegerValue",
            "robot_operations.set_calibration_appliance_integer_value",
            {
                "index_offset": index_offset,
                "integer_value": integer_value,
            },
            None,
        )
        return None

    async def set_calibration_appliance_real_value(
        self,
        *,
        index_offset: int = 0,
        real_value: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetCalibrationApplianceRealValue",
            "robot_operations.set_calibration_appliance_real_value",
            {
                "index_offset": index_offset,
                "real_value": real_value,
            },
            None,
        )
        return None

    async def set_robot_calibration_measurement_offset_in_tool_frame(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
        measurement_frame_relative_to_tool: Transform | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetRobotCalibrationMeasurementOffsetInToolFrame",
            "robot_operations.set_robot_calibration_measurement_offset_in_tool_frame",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
                "measurement_frame_relative_to_tool": measurement_frame_relative_to_tool,
            },
            None,
        )
        return None

    async def set_robot_calibration_tool_frame(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
        tool_frame_relative_to_flange: Transform | None = None,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetRobotCalibrationToolFrame",
            "robot_operations.set_robot_calibration_tool_frame",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
                "tool_frame_relative_to_flange": tool_frame_relative_to_flange,
            },
            None,
        )
        return None

    async def set_robot_machine_base_transform(
        self,
        machine_id: CollectionMachineId,
        reference_frame: CollectionObjectName,
        *,
        destination_transform: Transform | None = None,
        number_of_steps: int = 0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetRobotMachineBaseTransform",
            "robot_operations.set_robot_machine_base_transform",
            {
                "machine_id": machine_id,
                "destination_transform": destination_transform,
                "reference_frame": reference_frame,
                "number_of_steps": number_of_steps,
            },
            None,
        )
        return None

    async def set_robot_machine_model_link_parameters(
        self,
        machine_id: CollectionMachineId,
        *,
        link_name: str = "",
        configuration: RobotModelLinkConfiguration | None = None,
    ) -> None:
        configuration = configuration or RobotModelLinkConfiguration()
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetRobotMachineModelLinkParameters",
            "robot_operations.set_robot_machine_model_link_parameters",
            {
                "machine_id": machine_id,
                "link_name": link_name,
                "link_type": configuration.link_type,
                "dh_alpha_component": configuration.dh_alpha_component,
                "dh_a_component": configuration.dh_a_component,
                "dh_d_component": configuration.dh_d_component,
                "dh_theta_component": configuration.dh_theta_component,
                "dh_x_axis_deflection_factor": configuration.dh_x_axis_deflection_factor,
                "dh_y_axis_deflection_factor": configuration.dh_y_axis_deflection_factor,
                "dh_z_axis_deflection_factor": configuration.dh_z_axis_deflection_factor,
                "six_dof_x_component": configuration.six_dof_x_component,
                "six_dof_y_component": configuration.six_dof_y_component,
                "six_dof_z_component": configuration.six_dof_z_component,
                "six_dof_rx_component": configuration.six_dof_rx_component,
                "six_dof_ry_component": configuration.six_dof_ry_component,
                "six_dof_rz_component": configuration.six_dof_rz_component,
                "active_joint_component": configuration.active_joint_component,
                "encoder_offset_value": configuration.encoder_offset_value,
                "minimum_encoder_limit": configuration.minimum_encoder_limit,
                "maximum_encoder_limit": configuration.maximum_encoder_limit,
                "encoder_sense_negative": configuration.encoder_sense_negative,
                "include_additional_encoder": configuration.include_additional_encoder,
                "additional_encoder_index_offset": configuration.additional_encoder_index_offset,
                "additional_encoder_sense_negative": configuration.additional_encoder_sense_negative,
                "segment_origin_mass_kg": configuration.segment_origin_mass_kg,
                "segment_cg_mass_kg": configuration.segment_cg_mass_kg,
                "segment_cg_in_segment": configuration.segment_cg_in_segment,
            },
            None,
        )
        return None

    async def set_robot_machine_parameter(
        self,
        machine_id: CollectionMachineId,
        *,
        parameter_name: str = "",
        parameter_value: float = 0.0,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetRobotMachineParameter",
            "robot_operations.set_robot_machine_parameter",
            {
                "machine_id": machine_id,
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            },
            None,
        )
        return None

    async def simulate_robot_machine_path_output_csv_file(
        self,
        machine_id: CollectionMachineId,
        path_frames: Iterable[CollectionObjectName],
        output_csv_file: FileReference,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SimulateRobotMachinePathOutputCsvFile",
            "robot_operations.simulate_robot_machine_path_output_csv_file",
            {
                "machine_id": machine_id,
                "path_frames": path_frames,
                "output_csv_file": output_csv_file,
            },
            None,
        )
        return None

    async def start_robot_machine_interface(
        self,
        machine_id: CollectionMachineId,
        *,
        interface_type: int = 0,
        run_in_simulation: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "StartRobotMachineInterface",
            "robot_operations.start_robot_machine_interface",
            {
                "machine_id": machine_id,
                "interface_type": interface_type,
                "run_in_simulation": run_in_simulation,
            },
            None,
        )
        return None

    async def start_stop_robot_calibration_trapping(
        self,
        machine_id: CollectionMachineId,
        instrument_id: CollectionInstrumentId,
        *,
        calibration_name: str = "",
        start_trapping: bool = False,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "StartStopRobotCalibrationTrapping",
            "robot_operations.start_stop_robot_calibration_trapping",
            {
                "machine_id": machine_id,
                "calibration_name": calibration_name,
                "instrument_id": instrument_id,
                "start_trapping": start_trapping,
            },
            None,
        )
        return None

    async def stop_robot_machine_interface(
        self,
        machine_id: CollectionMachineId,
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "StopRobotMachineInterface",
            "robot_operations.stop_robot_machine_interface",
            {
                "machine_id": machine_id,
            },
            None,
        )
        return None

    async def get_robot_pose_for_a_frame(
        self,
        machine_id: CollectionMachineId,
        goal_frame: CollectionObjectName,
        goal_pose_count: int,
        *,
        reference_pose: Iterable[float] = (),
    ) -> list[float]:
        return cast(
            list[float],
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "GetRobotPoseForAFrame",
                "robot_operations.get_robot_pose_for_a_frame",
                {
                    "machine_id": machine_id,
                    "goal_frame": goal_frame,
                    "reference_pose": reference_pose,
                    "goal_pose_count": goal_pose_count,
                },
                None,
            ),
        )

    async def perform_robot_calibration(
        self,
        machine_id: CollectionMachineId,
        *,
        calibration_name: str = "",
        set_current_base_as_nominal: bool = False,
        show_interface: bool = False,
        allowed_outlier_rejection_count: int = 0,
        allowable_maximum_error: float = 0.0,
        allowable_average_error: float = 0.0,
    ) -> RobotCalibrationMetrics:
        return cast(
            RobotCalibrationMetrics,
            await self._client._invoke_mp_operation(
                "briosa.RobotOperations",
                "PerformRobotCalibration",
                "robot_operations.perform_robot_calibration",
                {
                    "machine_id": machine_id,
                    "calibration_name": calibration_name,
                    "set_current_base_as_nominal": set_current_base_as_nominal,
                    "show_interface": show_interface,
                    "allowed_outlier_rejection_count": allowed_outlier_rejection_count,
                    "allowable_maximum_error": allowable_maximum_error,
                    "allowable_average_error": allowable_average_error,
                },
                None,
            ),
        )

    async def set_calibration_appliance_data(
        self,
        *,
        real_values: Iterable[float] = (),
    ) -> None:
        await self._client._invoke_mp_operation(
            "briosa.RobotOperations",
            "SetCalibrationApplianceData",
            "robot_operations.set_calibration_appliance_data",
            {
                "real_values": real_values,
            },
            None,
        )
        return None


WAVE_B_OPERATIONS = (
    "cloud_and_mesh_operations.cloud_display_control",
    "cloud_and_mesh_operations.reset_cloud_bounding_box",
    "cloud_and_mesh_operations.get_cloud_point_count",
    "cloud_and_mesh_operations.set_cloud_default_clipping_plane",
    "cloud_and_mesh_operations.raster_scan_edge_inspection",
    "cloud_and_mesh_operations.new_raster_scan_edge_inspection",
    "cloud_and_mesh_operations.clear_cloud_point_deviations",
    "cloud_and_mesh_operations.enable_all_cloud_cross_sections",
    "cloud_and_mesh_operations.enable_disable_cloud_cross_sections",
    "cloud_and_mesh_operations.enable_single_cloud_cross_section",
    "cloud_and_mesh_operations.get_number_of_cross_sections_in_cross_section_cloud",
    "cloud_and_mesh_operations.filter_clouds_to_plane",
    "cloud_and_mesh_operations.filter_clouds_to_group",
    "cloud_and_mesh_operations.filter_clouds_to_surface",
    "cloud_and_mesh_operations.filter_clouds_to_bsplines",
    "cloud_and_mesh_operations.filter_clouds_to_line_segment",
    "cloud_and_mesh_operations.filter_clouds_to_vector_groups_resolve_points",
    "cloud_and_mesh_operations.filter_clouds_to_vector_groups_resolve_clouds",
    "cloud_and_mesh_operations.rgb_cloud_point_filter",
    "cloud_and_mesh_operations.get_cloud_rgb_values",
    "cloud_and_mesh_operations.get_cloud_rgb_values_near_point",
    "cloud_and_mesh_operations.subdivide_cloud_by_point_spacing",
    "cloud_and_mesh_operations.delete_cloud_points_by_radial_distance_from_points",
    "cloud_and_mesh_operations.delete_cloud_points_by_xyz_range",
    "cloud_and_mesh_operations.generate_general_mesh",
    "cloud_and_mesh_operations.consolidate_mesh",
    "cloud_and_mesh_operations.mesh_volume",
    "cloud_and_mesh_operations.mesh_fill_holes",
    "construction_operations.add_surface_to_mesh_offset_along_reference_direction",
    "construction_operations.auto_arrange_callout_view",
    "construction_operations.clear_hidden_point_bar_database",
    "construction_operations.construct_b_spline_from_intersection_of_plane_and_surface",
    "construction_operations.construct_b_spline_from_intersection_of_surfaces",
    "construction_operations.construct_b_spline_from_point_set",
    "construction_operations.construct_b_spline_from_points",
    "construction_operations.construct_b_spline_from_several_b_splines",
    "construction_operations.construct_b_splines_from_intersection_of_plane_and_mesh",
    "construction_operations.construct_b_splines_from_lines",
    "construction_operations.construct_b_splines_from_surfaces",
    "construction_operations.construct_boundary_points_from_cloud",
    "construction_operations.construct_circle",
    "construction_operations.construct_circles_from_surface_faces_runtime_select",
    "construction_operations.construct_circles_lines_from_surfaces",
    "construction_operations.construct_collection",
    "construction_operations.construct_cone",
    "construction_operations.construct_cones_from_surface_faces_runtime_select",
    "construction_operations.construct_cross_section_cloud",
    "construction_operations.construct_cross_section_cloud_user_select",
    "construction_operations.construct_cylinder",
    "construction_operations.construct_cylinder_from_end_points",
    "construction_operations.construct_cylinders_from_surface_faces_runtime_select",
    "construction_operations.construct_ellipse",
    "construction_operations.construct_ellipsoid",
    "construction_operations.construct_folders",
    "construction_operations.construct_frame",
    "construction_operations.construct_frame_at_point_with_working_z_and_clocked_axis",
    "construction_operations.construct_frame_at_robot_link",
    "construction_operations.construct_frame_average_of_other_object_frames",
    "construction_operations.construct_frame_copy_and_make_left_handed",
    "construction_operations.construct_frame_from_point_measurement_probing_frames",
    "construction_operations.construct_frame_from_transform_in_world",
    "construction_operations.construct_frame_known_origin_object_direction_object_direction",
    "construction_operations.construct_frame_on_instrument_base",
    "construction_operations.construct_frame_on_object",
    "construction_operations.construct_frame_pick_origin_and_point_on_x_axis_clock_z_along_working_z",
    "construction_operations.construct_frame_three_planes",
    "construction_operations.construct_frame_three_points",
    "construction_operations.construct_frame_with_wizard",
    "construction_operations.construct_frames_by_projecting_frames_on_mesh_along_frame_direction",
    "construction_operations.construct_frames_by_projecting_frames_on_mesh_along_reference_direction",
    "construction_operations.construct_line_center_of_slot",
    "construction_operations.construct_line_from_instrument_shot",
    "construction_operations.construct_line_normal_to_object",
    "construction_operations.construct_line_normal_to_object_through_point",
    "construction_operations.construct_line_project_line_to_object_reference_plane",
    "construction_operations.construct_line_two_plane_intersection",
    "construction_operations.construct_line_two_points",
    "construction_operations.construct_line_two_points_vector_notation",
    "construction_operations.construct_lines_from_surface_faces_runtime_select",
    "construction_operations.construct_mirror_cube_frame",
    "construction_operations.construct_perimeter_from_points",
    "construction_operations.construct_plane",
    "construction_operations.construct_plane_normal_to_object_through_point",
    "construction_operations.construct_planes_bisect_two_planes",
    "construction_operations.construct_planes_bounding_point_group",
    "construction_operations.construct_planes_from_surface_faces_runtime_select",
    "construction_operations.construct_point_at_circle_center",
    "construction_operations.construct_point_at_intersection_of_b_spline_and_surfaces",
    "construction_operations.construct_point_at_intersection_of_plane_and_line",
    "construction_operations.construct_point_at_intersection_of_planes",
    "construction_operations.construct_point_at_intersection_of_two_b_splines",
    "construction_operations.construct_point_at_intersection_of_two_lines",
    "construction_operations.construct_point_at_line_midpoint",
    "construction_operations.construct_point_at_projection_of_point_onto_object",
    "construction_operations.construct_point_cloud_from_existing_clouds",
    "construction_operations.construct_point_cloud_from_visible_cloud_points",
    "construction_operations.construct_point_cloud_limiting_probing_directions",
    "construction_operations.construct_point_clouds_from_existing_cloud_points_runtime_select",
    "construction_operations.construct_point_clouds_from_existing_clouds_uniform_spacing",
    "construction_operations.construct_point_clouds_from_existing_point_group",
    "construction_operations.construct_point_fit_to_points",
    "construction_operations.construct_point_from_cloud_point_runtime_select",
    "construction_operations.construct_point_from_survey_target_center",
    "construction_operations.construct_point_group_from_point_cloud",
    "construction_operations.construct_point_group_from_point_name_ref_list",
    "construction_operations.construct_point_groups_from_vector_groups",
    "construction_operations.construct_point_in_working_coordinates",
    "construction_operations.construct_points_at_intersection_of_circle_and_line",
    "construction_operations.construct_points_at_intersection_of_principal_object_axes_and_surfaces",
    "construction_operations.construct_points_at_projection_on_surfaces_parallel_to_wcf_axis",
    "construction_operations.construct_points_at_projection_on_surfaces_radial_from_wcf_axis",
    "construction_operations.construct_points_at_projection_on_surfaces_spherical_from_wcf_origin",
    "construction_operations.construct_points_auto_correspond_two_groups_inter_point_distance",
    "construction_operations.construct_points_auto_correspond_two_groups_proximity",
    "construction_operations.construct_points_by_projecting_points_on_mesh_along_direction",
    "construction_operations.construct_points_cylindrically_shifted",
    "construction_operations.construct_points_from_cylinder",
    "construction_operations.construct_points_from_surface_faces_runtime_select",
    "construction_operations.construct_points_from_surfaces_on_uv_grid",
    "construction_operations.construct_points_layout_on_grid",
    "construction_operations.construct_points_n_spaced_on_curves",
    "construction_operations.construct_points_on_curves_using_max_chordal_deviation",
    "construction_operations.construct_points_on_object_vertices",
    "construction_operations.construct_points_on_surfaces_by_clicking",
    "construction_operations.construct_points_shifted_in_working_frame",
    "construction_operations.construct_points_spaced_at_distance_on_curves",
    "construction_operations.construct_points_subset_with_greatest_spacing",
    "construction_operations.construct_points_wildcard_selection",
    "construction_operations.construct_sphere",
    "construction_operations.construct_spheres_from_surface_faces_runtime_select",
    "construction_operations.construct_surface_by_dissecting_surfaces",
    "construction_operations.construct_surface_by_offsetting_surface",
    "construction_operations.construct_surface_fit_from_nominal_surfaces_and_actual_data",
    "construction_operations.construct_surface_from_annotation_links",
    "construction_operations.construct_surface_from_b_splines",
    "construction_operations.construct_surface_from_collection_of_surfaces",
    "construction_operations.construct_surface_from_cone",
    "construction_operations.construct_surface_from_cylinder",
    "construction_operations.construct_surface_from_plane",
    "construction_operations.construct_surface_from_point_groups",
    "construction_operations.construct_surface_from_sphere",
    "construction_operations.construct_surfaces_by_dissecting_surfaces_from_ref_list",
    "construction_operations.construct_surfaces_by_projecting_points",
    "construction_operations.construct_surfaces_from_objects",
    "construction_operations.construct_vector_group_area_profile_check",
    "construction_operations.construct_vector_group_from_relationship",
    "construction_operations.construct_vector_group_from_vector_name_ref_list",
    "construction_operations.construct_vector_group_group_to_group_compare",
    "construction_operations.construct_vector_in_working_coordinates_begin_delta",
    "construction_operations.construct_vector_in_working_coordinates_begin_direction_magnitude",
    "construction_operations.copy_groups_excluding_obscured_points",
    "construction_operations.copy_object",
    "construction_operations.copy_objects_point_to_point_delta",
    "construction_operations.copy_objects_to_a_collection",
    "construction_operations.create_hidden_point",
    "construction_operations.create_hidden_point_rod",
    "construction_operations.create_min_max_vector_group_callout",
    "construction_operations.create_picture_callout",
    "construction_operations.create_point_callout",
    "construction_operations.create_point_comparison_callout",
    "construction_operations.create_relationship_callout",
    "construction_operations.create_text_callout",
    "construction_operations.create_vector_callout",
    "construction_operations.decompose_transform_into_doubles_euler_xyz",
    "construction_operations.decompose_transform_into_doubles_euler_zxz",
    "construction_operations.decompose_transform_into_doubles_euler_zyx",
    "construction_operations.decompose_transform_into_doubles_euler_zyz",
    "construction_operations.decompose_transform_into_doubles_fixed_xyz",
    "construction_operations.decompose_transform_into_vectors_fixed_xyz",
    "construction_operations.decompose_transform_into_vectors_origin_and_axes",
    "construction_operations.decompose_world_transform_operator_into_doubles_fixed_xyz_in_world",
    "construction_operations.decompose_world_transform_operator_into_vectors_fixed_xyz_in_world",
    "construction_operations.delete_callout_view",
    "construction_operations.delete_collection",
    "construction_operations.delete_collections_by_wildcard",
    "construction_operations.delete_folders_by_wildcard",
    "construction_operations.delete_hidden_point_rod",
    "construction_operations.delete_points",
    "construction_operations.delete_points_wildcard_selection",
    "construction_operations.extract_sphere_centers_from_point_cloud",
    "construction_operations.get_collection_instrument_ref_list_variable",
    "construction_operations.get_hidden_point_rod_index_by_name",
    "construction_operations.get_ith_callout_position_in_callout_view",
    "construction_operations.get_number_of_callouts_in_callout_view",
    "construction_operations.get_working_transform_of_object_fixed_xyz",
    "construction_operations.invert_transform",
    "construction_operations.make_collection_instrument_id_runtime_select",
    "construction_operations.make_collection_instrument_ref_list_runtime_select",
    "construction_operations.make_collection_item_name_ref_list_wildcard_selection",
    "construction_operations.make_collection_name_runtime_select",
    "construction_operations.make_collection_object_name_ref_list_by_type",
    "construction_operations.make_collection_object_name_ref_list_by_type_and_color",
    "construction_operations.make_collection_object_name_ref_list_from_all_groups_in_collection",
    "construction_operations.make_collection_object_name_ref_list_runtime_select",
    "construction_operations.make_collection_object_name_ref_list_wildcard_selection",
    "construction_operations.make_collection_object_name_runtime_select",
    "construction_operations.make_collection_vector_group_name_ref_list_runtime_select",
    "construction_operations.make_event_ref_list_wildcard_selection",
    "construction_operations.make_picture_name_ref_list_runtime_select",
    "construction_operations.make_point_name_ref_list_from_group",
    "construction_operations.make_point_name_ref_list_runtime_select",
    "construction_operations.make_point_name_ref_list_wildcard_select",
    "construction_operations.make_point_name_runtime_select",
    "construction_operations.make_report_ref_list_from_collection",
    "construction_operations.make_report_ref_list_runtime_select",
    "construction_operations.make_system_string",
    "construction_operations.make_transform_from_doubles_euler_parameters",
    "construction_operations.make_transform_from_doubles_fixed_xyz",
    "construction_operations.make_vector_name_ref_list_from_vector_group",
    "construction_operations.make_vector_name_ref_list_runtime_select",
    "construction_operations.make_vector_names_unique_in_vector_group",
    "construction_operations.mirror_objects",
    "construction_operations.move_objects_point_to_point_delta",
    "construction_operations.move_objects_to_a_collection",
    "construction_operations.rename_callout_view",
    "construction_operations.rename_collection",
    "construction_operations.rename_item",
    "construction_operations.rename_object",
    "construction_operations.rename_point",
    "construction_operations.rename_points_with_name_pattern",
    "construction_operations.set_collection_instrument_ref_list_variable",
    "construction_operations.set_ith_callout_position_in_callout_view",
    "construction_operations.set_or_construct_default_collection",
    "construction_operations.set_point_position_in_working_coordinates",
    "construction_operations.shift_plane",
    "construction_operations.transform_points_by_delta_about_working_frame",
    "construction_operations.add_collection_instruments_to_ref_list_wildcard_selection",
    "construction_operations.average_set_of_groups",
    "construction_operations.construct_geometry_from_surfaces",
    "construction_operations.construct_objects_from_surface_faces_runtime_select",
    "construction_operations.construct_point_at_object_origin",
    "construction_operations.get_gradient_at_projected_point_on_surface",
    "construction_operations.get_gradient_at_projected_point_on_surface_edge",
    "construction_operations.make_callout_view_ref_list_wildcard_selection",
    "construction_operations.make_collection_object_name_ensure_unique",
    "construction_operations.make_point_name_ensure_unique",
    "construction_operations.make_relationship_ref_list_runtime_select",
    "construction_operations.make_relationship_ref_list_wildcard_selection",
    "construction_operations.set_default_callout_view_properties",
    "construction_operations.set_callout_view_properties",
    "construction_operations.construct_polygonized_surface_from_point_clouds",
    "construction_operations.construct_scale_bar",
    "gdt_operations.datum_alignment",
    "gdt_operations.delete_feature_checks",
    "gdt_operations.enable_disable_datum_alignment_for_feature_check",
    "gdt_operations.evaluate_feature_check",
    "gdt_operations.evaluate_feature_checks",
    "gdt_operations.feature_inspection_auto_filter",
    "gdt_operations.generate_feature_check_summary",
    "gdt_operations.get_datum_measurements",
    "gdt_operations.get_feature_check_cylinder_eval_options",
    "gdt_operations.get_feature_check_datum_references",
    "gdt_operations.get_feature_check_measurements",
    "gdt_operations.get_feature_check_reporting_frame",
    "gdt_operations.get_gdt_extended_options",
    "gdt_operations.make_annotation_ref_list_from_collection",
    "gdt_operations.make_annotation_ref_list_wildcard_selection",
    "gdt_operations.make_datum_ref_list_from_collection",
    "gdt_operations.make_feature_check_ref_list_from_collection",
    "gdt_operations.make_feature_check_reference_list_wildcard_selection",
    "gdt_operations.make_feature_checks",
    "gdt_operations.make_gdt_datum_annotation",
    "gdt_operations.make_gdt_feature_check_annotation",
    "gdt_operations.make_surface_face_list_from_surface",
    "gdt_operations.make_surface_face_list_runtime_select",
    "gdt_operations.refresh_datums_feature_checks_from_annotations",
    "gdt_operations.set_datum_measurements",
    "gdt_operations.set_feature_check_cylinder_eval_options",
    "gdt_operations.set_feature_check_measurements",
    "gdt_operations.set_feature_check_reporting_frame",
    "gdt_operations.set_gdt_extended_options",
    "gdt_operations.set_gdt_options",
    "gdt_operations.set_global_force_simultaneous_evaluation",
    "gdt_operations.start_stop_feature_check_trapping",
    "gdt_operations.get_feature_check_reporting_options",
    "gdt_operations.get_gdt_options",
    "gdt_operations.set_feature_check_reporting_options",
    "instrument_operations.activate_deactivate_instrument_toolbar",
    "instrument_operations.add_new_instrument",
    "instrument_operations.add_nominal_point_to_tcp_fixture",
    "instrument_operations.align_cloud_to_cad",
    "instrument_operations.align_laser_projector",
    "instrument_operations.align_two_targets_with_axis_wcf_x",
    "instrument_operations.associate_objects_with_instrument",
    "instrument_operations.auto_correspond_closest_point",
    "instrument_operations.auto_correspond_with_proximity_trigger",
    "instrument_operations.auto_measure_batch_of_features",
    "instrument_operations.auto_measure_points",
    "instrument_operations.auto_measure_specified_geometry",
    "instrument_operations.auto_measure_surface_vector_intersections",
    "instrument_operations.auto_measure_vectors",
    "instrument_operations.build_target",
    "instrument_operations.calculate_tcp_fixture_uncertainties",
    "instrument_operations.clear_cloud_viewer",
    "instrument_operations.close_auto_correspond_closest_point_dialog",
    "instrument_operations.collimation",
    "instrument_operations.combine_point_groups",
    "instrument_operations.compute_cte_scale_factor",
    "instrument_operations.configure_and_measure",
    "instrument_operations.construct_measured_point_uncertainty_ellipsoids",
    "instrument_operations.construct_mirror_from_plane",
    "instrument_operations.construct_mirror_from_two_points",
    "instrument_operations.construct_perimeters_from_surface_face_list",
    "instrument_operations.construct_tcp_fixture",
    "instrument_operations.create_new_dynamic_reference",
    "instrument_operations.create_templated_instrument_usmn",
    "instrument_operations.delete_instrument",
    "instrument_operations.delete_measurement_observation",
    "instrument_operations.delete_measurements",
    "instrument_operations.disassociate_objects_from_instrument",
    "instrument_operations.dissect_point_group",
    "instrument_operations.dock_instrument_interface",
    "instrument_operations.drift_check",
    "instrument_operations.edge_scan_measurement",
    "instrument_operations.edit_scan_perimeter_profile",
    "instrument_operations.enable_disable_frame_set_scan_mode_all_instruments",
    "instrument_operations.enable_disable_frame_set_scan_mode_by_instrument",
    "instrument_operations.enable_disable_point_set_scan_mode",
    "instrument_operations.export_instrument_history_to_xml_file",
    "instrument_operations.fabricate_observations",
    "instrument_operations.get_current_instrument_position_update",
    "instrument_operations.get_current_trapping_status",
    "instrument_operations.get_estimated_scan_time",
    "instrument_operations.get_inspection_verification_mode",
    "instrument_operations.get_instrument_base_uncertainty_covariance_matrix_wrt_world",
    "instrument_operations.get_instrument_group_and_target",
    "instrument_operations.get_instrument_id_from_name",
    "instrument_operations.get_instrument_interface_response_timeout",
    "instrument_operations.get_instrument_measurement_mode_profile",
    "instrument_operations.get_instrument_model",
    "instrument_operations.get_instrument_part_temperature",
    "instrument_operations.get_instrument_scale_factor",
    "instrument_operations.get_instrument_target_status",
    "instrument_operations.get_instrument_targeting",
    "instrument_operations.get_instrument_targets_and_mode_profiles",
    "instrument_operations.get_instrument_transform",
    "instrument_operations.get_instrument_weather_setting",
    "instrument_operations.get_instruments_with_observations_on_target",
    "instrument_operations.get_last_instrument_index",
    "instrument_operations.get_last_solved_tcp_fixture_uncertainty_covariance_matrix",
    "instrument_operations.get_number_of_observations_on_target",
    "instrument_operations.get_obscured_points_from_instrument",
    "instrument_operations.get_observation_info",
    "instrument_operations.get_pcmm_instrument_xyz_uncertainties",
    "instrument_operations.get_targets_measured_by_instrument",
    "instrument_operations.get_tracker_edm_theodolite_uncertainties",
    "instrument_operations.get_wrtl_channel_and_status",
    "instrument_operations.get_xyz_instrument_uncertainties",
    "instrument_operations.guide_objects_in_6d_based_on_point_measurements",
    "instrument_operations.initiate_servo_guide",
    "instrument_operations.instrument_operational_check",
    "instrument_operations.issue_instrument_actuator_command",
    "instrument_operations.jump_instrument_to_new_location",
    "instrument_operations.load_cloud_viewer_point_cloud_file",
    "instrument_operations.load_instrument_configuration",
    "instrument_operations.locate_instrument_best_fit_group_to_group",
    "instrument_operations.locate_instrument_best_fit_nominal_geometry",
    "instrument_operations.locate_instrument_group_to_surface_quick_fit",
    "instrument_operations.locate_instrument_ref_tie_in",
    "instrument_operations.locate_instruments_usmn",
    "instrument_operations.lr_apdis_activate_mcm_calibration",
    "instrument_operations.lr_apdis_get_active_mcm_calibration",
    "instrument_operations.lr_apdis_perform_mcm_calibration",
    "instrument_operations.lr_get_most_recent_snr_info",
    "instrument_operations.lr_hardware_connect",
    "instrument_operations.lr_hardware_disconnect",
    "instrument_operations.lr_self_test",
    "instrument_operations.lr_self_test_flip_test",
    "instrument_operations.lr_self_test_linearization",
    "instrument_operations.lr_self_test_lo_sep",
    "instrument_operations.lr_set_red_laser_intensity",
    "instrument_operations.lr_verify_hardware_connection",
    "instrument_operations.make_collection_object_name_ref_list_from_objects_associated_with_instruments",
    "instrument_operations.make_surface_face_list_from_point_proximity",
    "instrument_operations.measure",
    "instrument_operations.measure_existing_single_point",
    "instrument_operations.measure_existing_single_point_and_compare",
    "instrument_operations.measure_existing_single_point_manual_guide",
    "instrument_operations.measure_nominal_feature",
    "instrument_operations.measure_single_point_here",
    "instrument_operations.move_instrument_to_another_collection",
    "instrument_operations.move_measurement_observation",
    "instrument_operations.move_objects_in_6d_using_instrument_updates",
    "instrument_operations.multi_measurement_initiate",
    "instrument_operations.multi_measurement_stop",
    "instrument_operations.point_at_target",
    "instrument_operations.quick_align",
    "instrument_operations.rename_instrument",
    "instrument_operations.save_cloud_viewer_point_cloud_file",
    "instrument_operations.save_instrument_configuration",
    "instrument_operations.scan_cad_faces",
    "instrument_operations.scan_within_perimeter",
    "instrument_operations.send_cloud_to_sa",
    "instrument_operations.set_absolute_instrument_scale_factor",
    "instrument_operations.set_alignment_projector",
    "instrument_operations.set_cloud_viewer_filter",
    "instrument_operations.set_inspection_verification_mode",
    "instrument_operations.set_instrument_axes",
    "instrument_operations.set_instrument_base_uncertainty_covariance_matrix_wrt_base",
    "instrument_operations.set_instrument_base_uncertainty_covariance_matrix_wrt_world",
    "instrument_operations.set_instrument_group_and_target",
    "instrument_operations.set_instrument_interface_response_timeout",
    "instrument_operations.set_instrument_measurement_mode_profile",
    "instrument_operations.set_instrument_targeting",
    "instrument_operations.set_instrument_transform",
    "instrument_operations.set_instrument_weather_setting",
    "instrument_operations.set_ladar_auto_meas_point",
    "instrument_operations.set_ladar_auto_meas_sphere",
    "instrument_operations.set_ladar_feature_meas_circle",
    "instrument_operations.set_ladar_feature_meas_cylinder",
    "instrument_operations.set_ladar_feature_meas_slot",
    "instrument_operations.set_ladar_feature_meas_sphere",
    "instrument_operations.set_multiply_instrument_scale_factor",
    "instrument_operations.set_observation_collimation_shot_options",
    "instrument_operations.set_observation_mirror_cube_shot_face",
    "instrument_operations.set_observation_status",
    "instrument_operations.set_pcmm_instrument_xyz_uncertainties",
    "instrument_operations.set_probe_offset_frame_offline",
    "instrument_operations.set_probe_offset_frame_online",
    "instrument_operations.set_remeasure_failed_checks_only",
    "instrument_operations.set_target_computation_options",
    "instrument_operations.set_tracker_edm_theodolite_uncertainties",
    "instrument_operations.set_wrtl_channel",
    "instrument_operations.set_xyz_instrument_uncertainties",
    "instrument_operations.set_xyz_reference_frame_instrument_base_anchor_frame",
    "instrument_operations.start_gdt_inspection",
    "instrument_operations.start_gdt_inspection_design",
    "instrument_operations.start_gdt_inspection_rehearse",
    "instrument_operations.start_instrument_interface",
    "instrument_operations.start_theodolite_interface",
    "instrument_operations.stop_active_measurement_mode",
    "instrument_operations.stop_instrument_interface",
    "instrument_operations.synchronized_measurement_master_slave",
    "instrument_operations.track_tape_measurement",
    "instrument_operations.transform_instrument_by_delta",
    "instrument_operations.transform_instrument_frame_to_frame",
    "instrument_operations.transform_multiple_instruments_by_delta",
    "instrument_operations.verify_instrument_connection",
    "instrument_operations.wait_for_trapping_to_complete",
    "instrument_operations.watch_closest_point",
    "instrument_operations.watch_instrument",
    "instrument_operations.watch_point_to_edge",
    "instrument_operations.watch_point_to_objects",
    "instrument_operations.watch_point_to_point",
    "instrument_operations.watch_point_to_point_with_view_zooming",
    "relationship_operations.auto_filter_clouds_to_nominal_geometry_2d",
    "relationship_operations.auto_filter_clouds_to_nominal_geometry_3d",
    "relationship_operations.auto_filter_points_groups_clouds_to_surface_faces",
    "relationship_operations.auto_filter_points_to_nominal_geometry_3d",
    "relationship_operations.compute_geometry_relationship_uncertainties",
    "relationship_operations.create_points_to_objects_map",
    "relationship_operations.delete_relationship",
    "relationship_operations.do_relationship_fit",
    "relationship_operations.extract_geometry_from_point_clouds",
    "relationship_operations.filter_geometry_relationship_outlier_cloud_points",
    "relationship_operations.generate_geometry_relationship_summary",
    "relationship_operations.get_general_relationship_statistics",
    "relationship_operations.get_geom_relationship_criteria_name_list",
    "relationship_operations.get_objects_from_points_to_objects_map_point_list",
    "relationship_operations.get_point_to_point_relationship_statistics",
    "relationship_operations.get_points_to_objects_relationship_statistics",
    "relationship_operations.get_points_to_points_relationship_associated_data",
    "relationship_operations.get_relationship_associated_data",
    "relationship_operations.get_relationship_status",
    "relationship_operations.make_average_point_relationship",
    "relationship_operations.make_cloud_to_swatch_relationship",
    "relationship_operations.make_dynamic_circle_relationship",
    "relationship_operations.make_dynamic_ellipse_relationship",
    "relationship_operations.make_dynamic_line_relationship",
    "relationship_operations.make_dynamic_plane_relationship",
    "relationship_operations.make_dynamic_point_relationship",
    "relationship_operations.make_frame_to_frame_relationship",
    "relationship_operations.make_geometry_compare_only_relationship",
    "relationship_operations.make_geometry_fit_and_compare_to_nominal_relationship",
    "relationship_operations.make_geometry_fit_only_relationship",
    "relationship_operations.make_group_to_group_relationship",
    "relationship_operations.make_group_to_nominal_group_relationship",
    "relationship_operations.make_groups_to_objects_relationship",
    "relationship_operations.make_object_to_object_direction_relationship",
    "relationship_operations.make_point_clouds_to_objects_relationship",
    "relationship_operations.make_point_to_point_relationship",
    "relationship_operations.make_points_to_objects_relationship",
    "relationship_operations.make_points_to_points_relationship",
    "relationship_operations.make_vector_group_to_vector_group_relationship",
    "relationship_operations.move_collections_by_minimizing_relationships",
    "relationship_operations.relationship_watch_window_template",
    "relationship_operations.set_group_to_nominal_group_view_zooming",
    "relationship_operations.set_object_to_object_direction_relationship_tolerances",
    "relationship_operations.set_optimization_perturbation_parameters",
    "relationship_operations.set_optimization_search_options",
    "relationship_operations.set_points_to_points_relationship_associated_data",
    "relationship_operations.set_relationship_associated_data",
    "relationship_operations.set_vector_group_to_vector_group_cylindrical_zone",
    "relationship_operations.set_vector_group_to_vector_group_fit_gradient_factor",
    "relationship_operations.set_vector_group_to_vector_group_fit_weights",
    "relationship_operations.set_vector_group_to_vector_group_relative_polarity",
    "relationship_operations.start_stop_relationship_trapping",
    "relationship_operations.edit_geometry_relationship_point_list",
    "relationship_operations.get_relationship_sigmoidal_gap_fit_constraints",
    "robot_calibration_appliance_node_operations.add_calibration_appliance_node",
    "robot_calibration_appliance_node_operations.clear_calibration_appliance_node_trap_manager_requests",
    "robot_calibration_appliance_node_operations.connect_disconnect_calibration_appliance_node",
    "robot_calibration_appliance_node_operations.delete_calibration_appliance_node",
    "robot_calibration_appliance_node_operations.enable_disable_calibration_appliance_node_instrument_auto_point",
    "robot_calibration_appliance_node_operations.enable_disable_calibration_appliance_node_trap_manager",
    "robot_calibration_appliance_node_operations.get_calibration_appliance_node_data",
    "robot_calibration_appliance_node_operations.get_calibration_appliance_node_integer_value",
    "robot_calibration_appliance_node_operations.get_calibration_appliance_node_real_value",
    "robot_calibration_appliance_node_operations.get_calibration_appliance_node_status",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_calibration_appliance_ip_address",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_display_robot",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_instrument",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_instrument_dwell_time",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_integer_value",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_frame",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_offset_transform",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_point_group",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_profile",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_measurement_target",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_real_value",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_trapping_node_id",
    "robot_calibration_appliance_node_operations.skip_calibration_appliance_node_measurement",
    "robot_calibration_appliance_node_operations.update_calibration_appliance_node_display_robot_joints",
    "robot_calibration_appliance_node_operations.set_calibration_appliance_node_data",
    "robot_operations.add_robot_machine_manip_kin",
    "robot_operations.add_robot_machine_sa_machine",
    "robot_operations.compute_robot_machine_adjusted_goal_frame",
    "robot_operations.create_robot_calibration",
    "robot_operations.delete_robot_calibration",
    "robot_operations.delete_robot_machine",
    "robot_operations.get_calibration_appliance_data",
    "robot_operations.get_calibration_appliance_integer_value",
    "robot_operations.get_calibration_appliance_real_value",
    "robot_operations.get_robot_machine_model_link_parameters",
    "robot_operations.get_robot_machine_parameter",
    "robot_operations.import_poses_match_to_frames",
    "robot_operations.import_poses_match_to_measurements",
    "robot_operations.move_robot_machine_through_path",
    "robot_operations.move_robot_machine_to_frame",
    "robot_operations.move_robot_machine_to_joint_pose_six_dof",
    "robot_operations.move_robot_machine_to_named_destination",
    "robot_operations.perform_robot_calibration_alternate",
    "robot_operations.set_active_robot_calibration",
    "robot_operations.set_calibration_appliance_integer_value",
    "robot_operations.set_calibration_appliance_real_value",
    "robot_operations.set_robot_calibration_measurement_offset_in_tool_frame",
    "robot_operations.set_robot_calibration_tool_frame",
    "robot_operations.set_robot_machine_base_transform",
    "robot_operations.set_robot_machine_model_link_parameters",
    "robot_operations.set_robot_machine_parameter",
    "robot_operations.simulate_robot_machine_path_output_csv_file",
    "robot_operations.start_robot_machine_interface",
    "robot_operations.start_stop_robot_calibration_trapping",
    "robot_operations.stop_robot_machine_interface",
    "robot_operations.get_robot_pose_for_a_frame",
    "robot_operations.perform_robot_calibration",
    "robot_operations.set_calibration_appliance_data",
)
