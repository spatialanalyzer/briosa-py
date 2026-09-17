"""Handwritten Wave A facade methods matching the published Python contract."""
# ruff: noqa: E501  # MP-compatible names are intentionally preserved.

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, cast

from briosa.operation_models import (
    ActiveUnits,
    AskForStringPullDownVersionResult,
    BestFitTransformationGroupToGroupResult,
    ComputeGroupToGroupOrientationRxRyRzResult,
    CreatePointUncertaintyCloudPointSetsResult,
    DirectCadAccessResult,
    GetActiveLanguageResult,
    GetBSplinePropertiesResult,
    GetCirclePropertiesResult,
    GetConePropertiesResult,
    GetCoordinateForIthPointInPointSetResult,
    GetCylinderPropertiesResult,
    GetDimensionValueResult,
    GetEllipsePropertiesResult,
    GetEulerParametersForFrameResult,
    GetEulerParametersForIthFrameInFrameSetResult,
    GetGeomRelationshipAutoVectorsResult,
    GetGeomRelationshipCriteriaResult,
    GetGeomRelationshipPointListResult,
    GetIthPointFromGroupResult,
    GetIthVectorFromVectorGroupResult,
    GetIthVectorFromVectorNameRefListResult,
    GetLinePropertiesResult,
    GetMeasurementAuxiliaryDataResult,
    GetMeasurementWeatherDataResult,
    GetNamedDoubleListVariableMinMaxResult,
    GetPipeRelationshipCutStatusResult,
    GetPipeRelationshipPropertiesResult,
    GetPipeRelationshipWeightsResult,
    GetPlanePropertiesResult,
    GetPointCoordinateCylindricalResult,
    GetPointCoordinatePolarResult,
    GetPointCoordinateResult,
    GetPointOfViewParametersResult,
    GetPointPropertiesResult,
    GetPointToleranceResult,
    GetPointToLineDistanceResult,
    GetPointToPointDistanceResult,
    GetRelationshipFitConstraintsScalarTypeResult,
    GetRelationshipOutlierRejectionScalarTypeResult,
    GetRelationshipProjectionOptionsResult,
    GetRelationshipSubSamplingOptionsResult,
    GetRelationshipToleranceScalarTypeResult,
    GetRelationshipToleranceVectorTypeResult,
    GetReportTagValueResult,
    GetScaleBarStatsResult,
    GetScreenResolutionResult,
    GetSlotPropertiesResult,
    GetSpherePropertiesResult,
    GetSurfacePhysicalStatsResult,
    GetTorusPropertiesResult,
    GetVectorFromVectorGroupByNameResult,
    GetVectorGroupPropertiesResult,
    GroupToSurfaceFitResult,
    MushroomTargetHoleInspectionResult,
    QueryCloudsToObjectsResult,
    QueryCloudsToSurfaceResult,
    QueryFrameToFrameResult,
    QueryGroupsToObjectsResult,
    QueryPointsToObjectsResult,
    QueryPointToObjectsResult,
    SphereAxisCheckResult,
    WorkingFrameProperties,
)
from briosa.operation_values import (
    AngularUnits,
    AsciiFileFormat,
    ChartName,
    ChartType,
    CollectionGroupName,
    CollectionInstrumentId,
    CollectionItemName,
    CollectionName,
    CollectionObjectName,
    CollectionVectorGroupName,
    Color,
    ColorizationOptions,
    CompTechnique,
    CoordinateSystemType,
    DatasetType,
    DegreeOfFreedom,
    DistanceUnits,
    ExportDataDelimeterType,
    ExportTargetNameFormat,
    ExportVectorNameFormat,
    FileReference,
    FitConstraintScalarOptions,
    FitMethod,
    Font,
    FrameName,
    GeometryType,
    MeasuredSideForPlanarOffset,
    MeasuredSideForRadialOffset,
    MpDialogInteractionMode,
    MpInteractionMode,
    NormalDirection,
    ObjectType,
    PointDeltaReportOptions,
    PointFilterInputType,
    PointName,
    ProjectionOptions,
    RelWeightingMode,
    RenderModeType,
    ReportOutputOptions,
    ReportPageSettings,
    ReportViewOptions,
    SaInteractionMode,
    SlotType,
    SphereFitComputationMode,
    SurfaceAnalysisMode,
    TemperatureUnits,
    ToleranceScalarOptions,
    ToleranceVectorOptions,
    Transform,
    TranslucencyType,
    Vector,
    VectorName,
    ViewName,
    WindowState,
    WorldTransform,
)


class WaveAOperationsMixin:
    async def _invoke_mp_operation(
        self,
        service: str,
        rpc: str,
        operation_id: str,
        values: dict[str, Any],
        result_type: type[Any] | None,
    ) -> Any:
        raise NotImplementedError

    async def angle_between_line_and_plane(
        self,
        selected_line: CollectionObjectName,
        selected_plane: CollectionObjectName,
        *,
        nominal_angle: float = 0.000000,
        angle_tolerance_0_0_for_none: float = 0.000000,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "AngleBetweenLineAndPlane",
                "analysis_operations.angle_between_line_and_plane",
                {
                    "selected_line": selected_line,
                    "selected_plane": selected_plane,
                    "nominal_angle": nominal_angle,
                    "angle_tolerance_0_0_for_none": angle_tolerance_0_0_for_none,
                },
                None,
            ),
        )

    async def angle_between_two_lines(
        self,
        line_1: CollectionObjectName,
        line_2: CollectionObjectName,
        *,
        nominal_angle: float = 0.000000,
        angle_tolerance_0_0_for_none: float = 0.000000,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "AngleBetweenTwoLines",
                "analysis_operations.angle_between_two_lines",
                {
                    "line_1": line_1,
                    "line_2": line_2,
                    "nominal_angle": nominal_angle,
                    "angle_tolerance_0_0_for_none": angle_tolerance_0_0_for_none,
                },
                None,
            ),
        )

    async def angle_between_two_planes_normals(
        self,
        plane_a: CollectionObjectName,
        plane_b: CollectionObjectName,
        *,
        nominal_angle: float = 0.000000,
        angle_tolerance_0_0_for_none: float = 0.000000,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "AngleBetweenTwoPlanesNormals",
                "analysis_operations.angle_between_two_planes_normals",
                {
                    "plane_a": plane_a,
                    "plane_b": plane_b,
                    "nominal_angle": nominal_angle,
                    "angle_tolerance_0_0_for_none": angle_tolerance_0_0_for_none,
                },
                None,
            ),
        )

    async def best_fit_transformation_group_to_group(
        self,
        reference_group: CollectionObjectName,
        corresponding_group: CollectionObjectName,
        *,
        show_interface: bool = False,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
        allow_scale: bool = False,
        allow_x: bool = True,
        allow_y: bool = True,
        allow_z: bool = True,
        allow_rx: bool = True,
        allow_ry: bool = True,
        allow_rz: bool = True,
        lock_degrees_of_freedom: bool = False,
        generate_event: bool = False,
        file_path_for_csv_text_report_requires_show_interface_true: FileReference,
    ) -> BestFitTransformationGroupToGroupResult:
        return cast(
            BestFitTransformationGroupToGroupResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "BestFitTransformationGroupToGroup",
                "analysis_operations.best_fit_transformation_group_to_group",
                {
                    "reference_group": reference_group,
                    "corresponding_group": corresponding_group,
                    "show_interface": show_interface,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                    "allow_scale": allow_scale,
                    "allow_x": allow_x,
                    "allow_y": allow_y,
                    "allow_z": allow_z,
                    "allow_rx": allow_rx,
                    "allow_ry": allow_ry,
                    "allow_rz": allow_rz,
                    "lock_degrees_of_freedom": lock_degrees_of_freedom,
                    "generate_event": generate_event,
                    "file_path_for_csv_text_report_requires_show_interface_true": file_path_for_csv_text_report_requires_show_interface_true,
                },
                BestFitTransformationGroupToGroupResult,
            ),
        )

    async def compute_group_to_group_orientation_rx_ry_rz(
        self,
        reference_group: CollectionObjectName,
        corresponding_group: CollectionObjectName,
    ) -> ComputeGroupToGroupOrientationRxRyRzResult:
        return cast(
            ComputeGroupToGroupOrientationRxRyRzResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "ComputeGroupToGroupOrientationRxRyRz",
                "analysis_operations.compute_group_to_group_orientation_rx_ry_rz",
                {
                    "reference_group": reference_group,
                    "corresponding_group": corresponding_group,
                },
                ComputeGroupToGroupOrientationRxRyRzResult,
            ),
        )

    async def create_point_uncertainty_cloud_point_sets(
        self,
        point_name_list: Iterable[PointName],
        *,
        number_of_samples: int = 1000,
        uncertainty_reference_frame_mode: str = "With respect to WORLD",
        grouping_mode: str = "Group per point",
        point_set_mode: str = "Point clouds",
    ) -> CreatePointUncertaintyCloudPointSetsResult:
        return cast(
            CreatePointUncertaintyCloudPointSetsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "CreatePointUncertaintyCloudPointSets",
                "analysis_operations.create_point_uncertainty_cloud_point_sets",
                {
                    "point_name_list": point_name_list,
                    "number_of_samples": number_of_samples,
                    "uncertainty_reference_frame_mode": uncertainty_reference_frame_mode,
                    "grouping_mode": grouping_mode,
                    "point_set_mode": point_set_mode,
                },
                CreatePointUncertaintyCloudPointSetsResult,
            ),
        )

    async def create_point_uncertainty_fields(
        self,
        point_name_list: Iterable[PointName],
        *,
        number_of_samples: int = 1000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "CreatePointUncertaintyFields",
            "analysis_operations.create_point_uncertainty_fields",
            {
                "point_name_list": point_name_list,
                "number_of_samples": number_of_samples,
            },
            None,
        )
        return None

    async def fit_geometry_to_point_group(
        self,
        geometry_type: GeometryType,
        group_to_fit: CollectionObjectName,
        resulting_object_name: CollectionObjectName,
        *,
        fit_profile_name: str = "",
        report_deviations: bool = False,
        fit_interface_tolerance_1_0_use_profile: float = -1.000000,
        ignore_out_of_tolerance_points: bool = False,
        starting_condition_geometry_optional: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "FitGeometryToPointGroup",
            "analysis_operations.fit_geometry_to_point_group",
            {
                "geometry_type": geometry_type,
                "group_to_fit": group_to_fit,
                "resulting_object_name": resulting_object_name,
                "fit_profile_name": fit_profile_name,
                "report_deviations": report_deviations,
                "fit_interface_tolerance_1_0_use_profile": fit_interface_tolerance_1_0_use_profile,
                "ignore_out_of_tolerance_points": ignore_out_of_tolerance_points,
                "starting_condition_geometry_optional": starting_condition_geometry_optional,
            },
            None,
        )
        return None

    async def fit_geometry_to_point_group_projected_to_plane(
        self,
        geometry_type: GeometryType,
        group_to_fit: CollectionObjectName,
        plane_name: CollectionObjectName,
        resulting_object_name: CollectionObjectName,
        *,
        fit_profile_name: str = "",
        report_deviations: bool = False,
        fit_interface_tolerance_1_0_use_profile: float = -1.000000,
        ignore_out_of_tolerance_points: bool = False,
        starting_condition_geometry_optional: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "FitGeometryToPointGroupProjectedToPlane",
            "analysis_operations.fit_geometry_to_point_group_projected_to_plane",
            {
                "geometry_type": geometry_type,
                "group_to_fit": group_to_fit,
                "plane_name": plane_name,
                "resulting_object_name": resulting_object_name,
                "fit_profile_name": fit_profile_name,
                "report_deviations": report_deviations,
                "fit_interface_tolerance_1_0_use_profile": fit_interface_tolerance_1_0_use_profile,
                "ignore_out_of_tolerance_points": ignore_out_of_tolerance_points,
                "starting_condition_geometry_optional": starting_condition_geometry_optional,
            },
            None,
        )
        return None

    async def fit_geometry_to_points(
        self,
        geometry_type: GeometryType,
        points_to_fit: Iterable[PointName],
        resulting_object_name: CollectionObjectName,
        *,
        fit_profile_name: str = "",
        report_deviations: bool = False,
        fit_interface_tolerance_1_0_use_profile: float = -1.000000,
        ignore_out_of_tolerance_points: bool = False,
        starting_condition_geometry_optional: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "FitGeometryToPoints",
            "analysis_operations.fit_geometry_to_points",
            {
                "geometry_type": geometry_type,
                "points_to_fit": points_to_fit,
                "resulting_object_name": resulting_object_name,
                "fit_profile_name": fit_profile_name,
                "report_deviations": report_deviations,
                "fit_interface_tolerance_1_0_use_profile": fit_interface_tolerance_1_0_use_profile,
                "ignore_out_of_tolerance_points": ignore_out_of_tolerance_points,
                "starting_condition_geometry_optional": starting_condition_geometry_optional,
            },
            None,
        )
        return None

    async def get_bspline_properties(
        self,
        b_spline_name: CollectionObjectName,
    ) -> GetBSplinePropertiesResult:
        return cast(
            GetBSplinePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetBSplineProperties",
                "analysis_operations.get_bspline_properties",
                {
                    "b_spline_name": b_spline_name,
                },
                GetBSplinePropertiesResult,
            ),
        )

    async def get_circle_properties(
        self,
        circle_name: CollectionObjectName,
    ) -> GetCirclePropertiesResult:
        return cast(
            GetCirclePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetCircleProperties",
                "analysis_operations.get_circle_properties",
                {
                    "circle_name": circle_name,
                },
                GetCirclePropertiesResult,
            ),
        )

    async def get_cone_properties(
        self,
        cone_name: CollectionObjectName,
    ) -> GetConePropertiesResult:
        return cast(
            GetConePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetConeProperties",
                "analysis_operations.get_cone_properties",
                {
                    "cone_name": cone_name,
                },
                GetConePropertiesResult,
            ),
        )

    async def get_coordinate_for_ith_point_in_point_set(
        self,
        point_set: CollectionObjectName,
        *,
        point_set_index: int = 0,
    ) -> GetCoordinateForIthPointInPointSetResult:
        return cast(
            GetCoordinateForIthPointInPointSetResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetCoordinateForIthPointInPointSet",
                "analysis_operations.get_coordinate_for_ith_point_in_point_set",
                {
                    "point_set": point_set,
                    "point_set_index": point_set_index,
                },
                GetCoordinateForIthPointInPointSetResult,
            ),
        )

    async def get_cylinder_properties(
        self,
        cylinder_name: CollectionObjectName,
    ) -> GetCylinderPropertiesResult:
        return cast(
            GetCylinderPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetCylinderProperties",
                "analysis_operations.get_cylinder_properties",
                {
                    "cylinder_name": cylinder_name,
                },
                GetCylinderPropertiesResult,
            ),
        )

    async def get_ellipse_properties(
        self,
        ellipse_name: CollectionObjectName,
    ) -> GetEllipsePropertiesResult:
        return cast(
            GetEllipsePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetEllipseProperties",
                "analysis_operations.get_ellipse_properties",
                {
                    "ellipse_name": ellipse_name,
                },
                GetEllipsePropertiesResult,
            ),
        )

    async def get_euler_parameters_for_frame(
        self,
        frame: CollectionObjectName,
    ) -> GetEulerParametersForFrameResult:
        return cast(
            GetEulerParametersForFrameResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetEulerParametersForFrame",
                "analysis_operations.get_euler_parameters_for_frame",
                {
                    "frame": frame,
                },
                GetEulerParametersForFrameResult,
            ),
        )

    async def get_euler_parameters_for_ith_frame_in_frame_set(
        self,
        frame_set: CollectionObjectName,
        *,
        frame_set_index: int = 0,
    ) -> GetEulerParametersForIthFrameInFrameSetResult:
        return cast(
            GetEulerParametersForIthFrameInFrameSetResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetEulerParametersForIthFrameInFrameSet",
                "analysis_operations.get_euler_parameters_for_ith_frame_in_frame_set",
                {
                    "frame_set": frame_set,
                    "frame_set_index": frame_set_index,
                },
                GetEulerParametersForIthFrameInFrameSetResult,
            ),
        )

    async def get_ith_collection_name(
        self,
        *,
        collection_index: int = 0,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetIthCollectionName",
                "analysis_operations.get_ith_collection_name",
                {
                    "collection_index": collection_index,
                },
                None,
            ),
        )

    async def get_ith_point_from_group(
        self,
        group_name: CollectionObjectName,
        *,
        point_index: int = 0,
    ) -> GetIthPointFromGroupResult:
        return cast(
            GetIthPointFromGroupResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetIthPointFromGroup",
                "analysis_operations.get_ith_point_from_group",
                {
                    "group_name": group_name,
                    "point_index": point_index,
                },
                GetIthPointFromGroupResult,
            ),
        )

    async def get_line_properties(
        self,
        line_name: CollectionObjectName,
    ) -> GetLinePropertiesResult:
        return cast(
            GetLinePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetLineProperties",
                "analysis_operations.get_line_properties",
                {
                    "line_name": line_name,
                },
                GetLinePropertiesResult,
            ),
        )

    async def get_measurement_auxiliary_data(
        self,
        point_name: PointName,
        *,
        auxiliary_name: str = "",
    ) -> GetMeasurementAuxiliaryDataResult:
        return cast(
            GetMeasurementAuxiliaryDataResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetMeasurementAuxiliaryData",
                "analysis_operations.get_measurement_auxiliary_data",
                {
                    "point_name": point_name,
                    "auxiliary_name": auxiliary_name,
                },
                GetMeasurementAuxiliaryDataResult,
            ),
        )

    async def get_measurement_info_data(
        self,
        point_name: PointName,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetMeasurementInfoData",
                "analysis_operations.get_measurement_info_data",
                {
                    "point_name": point_name,
                },
                None,
            ),
        )

    async def get_measurement_weather_data(
        self,
        point_name: PointName,
    ) -> GetMeasurementWeatherDataResult:
        return cast(
            GetMeasurementWeatherDataResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetMeasurementWeatherData",
                "analysis_operations.get_measurement_weather_data",
                {
                    "point_name": point_name,
                },
                GetMeasurementWeatherDataResult,
            ),
        )

    async def get_number_of_collections(self) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetNumberOfCollections",
                "analysis_operations.get_number_of_collections",
                {},
                None,
            ),
        )

    async def get_number_of_frames_in_frame_set(
        self,
        frame_set_container: CollectionObjectName,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetNumberOfFramesInFrameSet",
                "analysis_operations.get_number_of_frames_in_frame_set",
                {
                    "frame_set_container": frame_set_container,
                },
                None,
            ),
        )

    async def get_number_of_points_in_group(
        self,
        group_name: CollectionObjectName,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetNumberOfPointsInGroup",
                "analysis_operations.get_number_of_points_in_group",
                {
                    "group_name": group_name,
                },
                None,
            ),
        )

    async def get_number_of_points_in_point_set(
        self,
        point_set_container: CollectionObjectName,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetNumberOfPointsInPointSet",
                "analysis_operations.get_number_of_points_in_point_set",
                {
                    "point_set_container": point_set_container,
                },
                None,
            ),
        )

    async def get_object_reporting_frame(
        self,
        object_name: CollectionObjectName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetObjectReportingFrame",
                "analysis_operations.get_object_reporting_frame",
                {
                    "object_name": object_name,
                },
                None,
            ),
        )

    async def get_plane_properties(
        self,
        plane_name: CollectionObjectName,
    ) -> GetPlanePropertiesResult:
        return cast(
            GetPlanePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPlaneProperties",
                "analysis_operations.get_plane_properties",
                {
                    "plane_name": plane_name,
                },
                GetPlanePropertiesResult,
            ),
        )

    async def get_point_coordinate(
        self,
        point_name: PointName,
    ) -> GetPointCoordinateResult:
        return cast(
            GetPointCoordinateResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointCoordinate",
                "analysis_operations.get_point_coordinate",
                {
                    "point_name": point_name,
                },
                GetPointCoordinateResult,
            ),
        )

    async def get_point_coordinate_cylindrical(
        self,
        point_name: PointName,
    ) -> GetPointCoordinateCylindricalResult:
        return cast(
            GetPointCoordinateCylindricalResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointCoordinateCylindrical",
                "analysis_operations.get_point_coordinate_cylindrical",
                {
                    "point_name": point_name,
                },
                GetPointCoordinateCylindricalResult,
            ),
        )

    async def get_point_coordinate_polar(
        self,
        point_name: PointName,
    ) -> GetPointCoordinatePolarResult:
        return cast(
            GetPointCoordinatePolarResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointCoordinatePolar",
                "analysis_operations.get_point_coordinate_polar",
                {
                    "point_name": point_name,
                },
                GetPointCoordinatePolarResult,
            ),
        )

    async def get_point_properties(
        self,
        point_name: PointName,
    ) -> GetPointPropertiesResult:
        return cast(
            GetPointPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointProperties",
                "analysis_operations.get_point_properties",
                {
                    "point_name": point_name,
                },
                GetPointPropertiesResult,
            ),
        )

    async def get_point_to_line_distance(
        self,
        point: PointName,
        line: CollectionObjectName,
    ) -> GetPointToLineDistanceResult:
        return cast(
            GetPointToLineDistanceResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointToLineDistance",
                "analysis_operations.get_point_to_line_distance",
                {
                    "point": point,
                    "line": line,
                },
                GetPointToLineDistanceResult,
            ),
        )

    async def get_point_to_point_distance(
        self,
        first_point: PointName,
        second_point: PointName,
    ) -> GetPointToPointDistanceResult:
        return cast(
            GetPointToPointDistanceResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointToPointDistance",
                "analysis_operations.get_point_to_point_distance",
                {
                    "first_point": first_point,
                    "second_point": second_point,
                },
                GetPointToPointDistanceResult,
            ),
        )

    async def get_point_tolerance(
        self,
        point_name: PointName,
    ) -> GetPointToleranceResult:
        return cast(
            GetPointToleranceResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetPointTolerance",
                "analysis_operations.get_point_tolerance",
                {
                    "point_name": point_name,
                },
                GetPointToleranceResult,
            ),
        )

    async def get_slot_properties(
        self,
        slot_name: CollectionObjectName,
    ) -> GetSlotPropertiesResult:
        return cast(
            GetSlotPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetSlotProperties",
                "analysis_operations.get_slot_properties",
                {
                    "slot_name": slot_name,
                },
                GetSlotPropertiesResult,
            ),
        )

    async def get_sphere_properties(
        self,
        sphere_name: CollectionObjectName,
    ) -> GetSpherePropertiesResult:
        return cast(
            GetSpherePropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetSphereProperties",
                "analysis_operations.get_sphere_properties",
                {
                    "sphere_name": sphere_name,
                },
                GetSpherePropertiesResult,
            ),
        )

    async def get_surface_physical_stats(
        self,
        surface_name: CollectionObjectName,
    ) -> GetSurfacePhysicalStatsResult:
        return cast(
            GetSurfacePhysicalStatsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetSurfacePhysicalStats",
                "analysis_operations.get_surface_physical_stats",
                {
                    "surface_name": surface_name,
                },
                GetSurfacePhysicalStatsResult,
            ),
        )

    async def get_timestamp_for_ith_frame_in_frame_set(
        self,
        frame_set: CollectionObjectName,
        *,
        frame_set_index: int = 0,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetTimestampForIthFrameInFrameSet",
                "analysis_operations.get_timestamp_for_ith_frame_in_frame_set",
                {
                    "frame_set": frame_set,
                    "frame_set_index": frame_set_index,
                },
                None,
            ),
        )

    async def get_timestamp_for_ith_point_in_point_set(
        self,
        point_set: CollectionObjectName,
        *,
        point_set_index: int = 0,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetTimestampForIthPointInPointSet",
                "analysis_operations.get_timestamp_for_ith_point_in_point_set",
                {
                    "point_set": point_set,
                    "point_set_index": point_set_index,
                },
                None,
            ),
        )

    async def get_torus_properties(
        self,
        torus_name: CollectionObjectName,
    ) -> GetTorusPropertiesResult:
        return cast(
            GetTorusPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetTorusProperties",
                "analysis_operations.get_torus_properties",
                {
                    "torus_name": torus_name,
                },
                GetTorusPropertiesResult,
            ),
        )

    async def get_transform_for_ith_frame_in_frame_set(
        self,
        frame_set: CollectionObjectName,
        *,
        frame_set_index: int = 0,
    ) -> Transform:
        return cast(
            Transform,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GetTransformForIthFrameInFrameSet",
                "analysis_operations.get_transform_for_ith_frame_in_frame_set",
                {
                    "frame_set": frame_set,
                    "frame_set_index": frame_set_index,
                },
                None,
            ),
        )

    async def group_to_surface_fit(
        self,
        group_to_fit: CollectionObjectName,
        surface: CollectionObjectName,
        *,
        do_conventional_fit: bool = False,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
    ) -> GroupToSurfaceFitResult:
        return cast(
            GroupToSurfaceFitResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "GroupToSurfaceFit",
                "analysis_operations.group_to_surface_fit",
                {
                    "group_to_fit": group_to_fit,
                    "surface": surface,
                    "do_conventional_fit": do_conventional_fit,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                },
                GroupToSurfaceFitResult,
            ),
        )

    async def import_geometry_fit_profiles(
        self,
        geometry_fit_profiles_file_path: FileReference,
        *,
        overwrite_profiles_with_same_name: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "ImportGeometryFitProfiles",
            "analysis_operations.import_geometry_fit_profiles",
            {
                "geometry_fit_profiles_file_path": geometry_fit_profiles_file_path,
                "overwrite_profiles_with_same_name": overwrite_profiles_with_same_name,
            },
            None,
        )
        return None

    async def is_object_of_type(
        self,
        object_name: CollectionObjectName,
        *,
        object_type: ObjectType = ObjectType.ANY,
    ) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "IsObjectOfType",
                "analysis_operations.is_object_of_type",
                {
                    "object_name": object_name,
                    "object_type": object_type,
                },
                None,
            ),
        )

    async def make_circle_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        measured_side_for_planar_offset: MeasuredSideForPlanarOffset = MeasuredSideForPlanarOffset.ABOVE_PLANE,
        override_planar_offset_1_0_use_current: float = -1.000000,
        planar_offset_direction: NormalDirection = NormalDirection.PROBING_DIRECTION,
        lock_radius_1_0_do_not_lock: float = -1.000000,
        circle_computation_technique: CompTechnique = CompTechnique.STANDARD,
        reverse_normal_vector_after_fit: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_center: bool = True,
        cardinal_pt_2_point_on_normal: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeCircleFitProfile",
            "analysis_operations.make_circle_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "measured_side_for_planar_offset": measured_side_for_planar_offset,
                "override_planar_offset_1_0_use_current": override_planar_offset_1_0_use_current,
                "planar_offset_direction": planar_offset_direction,
                "lock_radius_1_0_do_not_lock": lock_radius_1_0_do_not_lock,
                "circle_computation_technique": circle_computation_technique,
                "reverse_normal_vector_after_fit": reverse_normal_vector_after_fit,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_center": cardinal_pt_1_center,
                "cardinal_pt_2_point_on_normal": cardinal_pt_2_point_on_normal,
            },
            None,
        )
        return None

    async def make_cone_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        lock_angle_in_degrees_1_0_do_not_lock: float = -1.000000,
        use_exhaustive_search: bool = True,
        make_cardinal_points: bool = True,
        cardinal_pt_1_vertex: bool = True,
        cardinal_pt_2_point_on_axis: bool = True,
        cardinal_pt_3_cut_point_on_axis: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeConeFitProfile",
            "analysis_operations.make_cone_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "lock_angle_in_degrees_1_0_do_not_lock": lock_angle_in_degrees_1_0_do_not_lock,
                "use_exhaustive_search": use_exhaustive_search,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_vertex": cardinal_pt_1_vertex,
                "cardinal_pt_2_point_on_axis": cardinal_pt_2_point_on_axis,
                "cardinal_pt_3_cut_point_on_axis": cardinal_pt_3_cut_point_on_axis,
            },
            None,
        )
        return None

    async def make_cylinder_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        lock_radius_1_0_do_not_lock: float = -1.000000,
        locked_radius_fit_method: FitMethod = FitMethod.MINIMUM_RMS,
        constrain_to_nominal_axis: bool = False,
        constrain_to_nominal_orientation: bool = False,
        align_with_nominal: bool = False,
        reverse_axis: bool = False,
        set_axis_first_to_last_point: bool = False,
        cylinder_computation_technique: CompTechnique = CompTechnique.STANDARD,
        use_exhaustive_search: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_begin_pt: bool = True,
        cardinal_pt_2_end_pt: bool = True,
        cardinal_pt_3_center: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeCylinderFitProfile",
            "analysis_operations.make_cylinder_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "lock_radius_1_0_do_not_lock": lock_radius_1_0_do_not_lock,
                "locked_radius_fit_method": locked_radius_fit_method,
                "constrain_to_nominal_axis": constrain_to_nominal_axis,
                "constrain_to_nominal_orientation": constrain_to_nominal_orientation,
                "align_with_nominal": align_with_nominal,
                "reverse_axis": reverse_axis,
                "set_axis_first_to_last_point": set_axis_first_to_last_point,
                "cylinder_computation_technique": cylinder_computation_technique,
                "use_exhaustive_search": use_exhaustive_search,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_begin_pt": cardinal_pt_1_begin_pt,
                "cardinal_pt_2_end_pt": cardinal_pt_2_end_pt,
                "cardinal_pt_3_center": cardinal_pt_3_center,
            },
            None,
        )
        return None

    async def make_ellipse_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        measured_side_for_planar_offset: MeasuredSideForPlanarOffset = MeasuredSideForPlanarOffset.ABOVE_PLANE,
        override_planar_offset_1_0_use_current: float = -1.000000,
        planar_offset_direction: NormalDirection = NormalDirection.PROBING_DIRECTION,
        reverse_normal_vector_after_fit: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_center: bool = True,
        cardinal_pt_2_point_on_normal: bool = True,
        cardinal_pt_3_focal_pt_1: bool = True,
        cardinal_pt_4_focal_pt_2: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeEllipseFitProfile",
            "analysis_operations.make_ellipse_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "measured_side_for_planar_offset": measured_side_for_planar_offset,
                "override_planar_offset_1_0_use_current": override_planar_offset_1_0_use_current,
                "planar_offset_direction": planar_offset_direction,
                "reverse_normal_vector_after_fit": reverse_normal_vector_after_fit,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_center": cardinal_pt_1_center,
                "cardinal_pt_2_point_on_normal": cardinal_pt_2_point_on_normal,
                "cardinal_pt_3_focal_pt_1": cardinal_pt_3_focal_pt_1,
                "cardinal_pt_4_focal_pt_2": cardinal_pt_4_focal_pt_2,
            },
            None,
        )
        return None

    async def make_line_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        reverse_normal_vector_after_fit: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_point_a: bool = True,
        cardinal_pt_2_point_b: bool = True,
        cardinal_pt_3_mid_point: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeLineFitProfile",
            "analysis_operations.make_line_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "reverse_normal_vector_after_fit": reverse_normal_vector_after_fit,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_point_a": cardinal_pt_1_point_a,
                "cardinal_pt_2_point_b": cardinal_pt_2_point_b,
                "cardinal_pt_3_mid_point": cardinal_pt_3_mid_point,
            },
            None,
        )
        return None

    async def make_paraboloid_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        lock_focal_length_1_0_do_not_lock: float = -1.000000,
        degree_of_freedom: DegreeOfFreedom = DegreeOfFreedom.ANY,
        make_cardinal_points: bool = True,
        cardinal_pt_1_vertex: bool = True,
        cardinal_pt_2_focal_point: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeParaboloidFitProfile",
            "analysis_operations.make_paraboloid_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "lock_focal_length_1_0_do_not_lock": lock_focal_length_1_0_do_not_lock,
                "degree_of_freedom": degree_of_freedom,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_vertex": cardinal_pt_1_vertex,
                "cardinal_pt_2_focal_point": cardinal_pt_2_focal_point,
            },
            None,
        )
        return None

    async def make_plane_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_planar_offset: MeasuredSideForPlanarOffset = MeasuredSideForPlanarOffset.ABOVE_PLANE,
        override_planar_offset_1_0_use_current: float = -1.000000,
        planar_offset_direction: NormalDirection = NormalDirection.PROBING_DIRECTION,
        reverse_normal_vector_after_fit: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_centroid: bool = True,
        cardinal_pt_2_point_on_normal: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakePlaneFitProfile",
            "analysis_operations.make_plane_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_planar_offset": measured_side_for_planar_offset,
                "override_planar_offset_1_0_use_current": override_planar_offset_1_0_use_current,
                "planar_offset_direction": planar_offset_direction,
                "reverse_normal_vector_after_fit": reverse_normal_vector_after_fit,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_centroid": cardinal_pt_1_centroid,
                "cardinal_pt_2_point_on_normal": cardinal_pt_2_point_on_normal,
            },
            None,
        )
        return None

    async def make_slot_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        measured_side_for_planar_offset: MeasuredSideForPlanarOffset = MeasuredSideForPlanarOffset.ABOVE_PLANE,
        override_planar_offset_1_0_use_current: float = -1.000000,
        planar_offset_direction: NormalDirection = NormalDirection.PROBING_DIRECTION,
        slot_type: SlotType = SlotType.ROUND,
        slot_computation_technique: CompTechnique = CompTechnique.STANDARD,
        reverse_normal_vector_after_fit: bool = False,
        make_cardinal_points: bool = True,
        cardinal_pt_1_center: bool = True,
        cardinal_pt_2_point_on_normal: bool = True,
        cardinal_pt_3_centerline_pt_1: bool = True,
        cardinal_pt_4_centerline_pt_2: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeSlotFitProfile",
            "analysis_operations.make_slot_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "measured_side_for_planar_offset": measured_side_for_planar_offset,
                "override_planar_offset_1_0_use_current": override_planar_offset_1_0_use_current,
                "planar_offset_direction": planar_offset_direction,
                "slot_type": slot_type,
                "slot_computation_technique": slot_computation_technique,
                "reverse_normal_vector_after_fit": reverse_normal_vector_after_fit,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_center": cardinal_pt_1_center,
                "cardinal_pt_2_point_on_normal": cardinal_pt_2_point_on_normal,
                "cardinal_pt_3_centerline_pt_1": cardinal_pt_3_centerline_pt_1,
                "cardinal_pt_4_centerline_pt_2": cardinal_pt_4_centerline_pt_2,
            },
            None,
        )
        return None

    async def make_sphere_fit_profile(
        self,
        *,
        fit_profile_name: str = "",
        measured_side_for_radial_offset: MeasuredSideForRadialOffset = MeasuredSideForRadialOffset.OUTSIDE,
        override_radial_offset_1_0_use_current: float = -1.000000,
        lock_radius_1_0_do_not_lock: float = -1.000000,
        make_cardinal_points: bool = True,
        cardinal_pt_1_center: bool = True,
        computation_method: SphereFitComputationMode = SphereFitComputationMode.STANDARD,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "MakeSphereFitProfile",
            "analysis_operations.make_sphere_fit_profile",
            {
                "fit_profile_name": fit_profile_name,
                "measured_side_for_radial_offset": measured_side_for_radial_offset,
                "override_radial_offset_1_0_use_current": override_radial_offset_1_0_use_current,
                "lock_radius_1_0_do_not_lock": lock_radius_1_0_do_not_lock,
                "make_cardinal_points": make_cardinal_points,
                "cardinal_pt_1_center": cardinal_pt_1_center,
                "computation_method": computation_method,
            },
            None,
        )
        return None

    async def mushroom_target_hole_inspection(
        self,
        *,
        name_prefix_for_intermediate_constructions: str = "",
        sphere_points_group_name: CollectionObjectName,
        sphere_target_radius: float = 0.000000,
        target_contact_plane: CollectionObjectName,
        point_to_create_at_hole: PointName,
    ) -> MushroomTargetHoleInspectionResult:
        return cast(
            MushroomTargetHoleInspectionResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "MushroomTargetHoleInspection",
                "analysis_operations.mushroom_target_hole_inspection",
                {
                    "name_prefix_for_intermediate_constructions": name_prefix_for_intermediate_constructions,
                    "sphere_points_group_name": sphere_points_group_name,
                    "sphere_target_radius": sphere_target_radius,
                    "target_contact_plane": target_contact_plane,
                    "point_to_create_at_hole": point_to_create_at_hole,
                },
                MushroomTargetHoleInspectionResult,
            ),
        )

    async def patch_normal_shift_hole_pin(
        self,
        plane_points_group_name: CollectionObjectName,
        perimeter_points_group_name: CollectionObjectName,
        resulting_point_name: PointName,
        *,
        additional_material_thickness: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "PatchNormalShiftHolePin",
            "analysis_operations.patch_normal_shift_hole_pin",
            {
                "plane_points_group_name": plane_points_group_name,
                "perimeter_points_group_name": perimeter_points_group_name,
                "resulting_point_name": resulting_point_name,
                "additional_material_thickness": additional_material_thickness,
            },
            None,
        )
        return None

    async def patch_normal_shift_point(
        self,
        plane_points_group_name: CollectionObjectName,
        point_to_shift: PointName,
        resulting_point_name: PointName,
        *,
        additional_material_thickness: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "PatchNormalShiftPoint",
            "analysis_operations.patch_normal_shift_point",
            {
                "plane_points_group_name": plane_points_group_name,
                "point_to_shift": point_to_shift,
                "resulting_point_name": resulting_point_name,
                "additional_material_thickness": additional_material_thickness,
            },
            None,
        )
        return None

    async def query_clouds_to_objects(
        self,
        cloud_names: Iterable[CollectionObjectName],
        object_names: Iterable[CollectionObjectName],
        resulting_object_name: CollectionObjectName,
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        proximity: float = 0.000000,
        skip_factor: int = 0,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
    ) -> QueryCloudsToObjectsResult:
        return cast(
            QueryCloudsToObjectsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryCloudsToObjects",
                "analysis_operations.query_clouds_to_objects",
                {
                    "cloud_names": cloud_names,
                    "object_names": object_names,
                    "resulting_object_name": resulting_object_name,
                    "projection_options": projection_options,
                    "proximity": proximity,
                    "skip_factor": skip_factor,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                },
                QueryCloudsToObjectsResult,
            ),
        )

    async def query_clouds_to_surface(
        self,
        cloud_names: Iterable[CollectionObjectName],
        filter_surface_name: CollectionObjectName,
        resulting_object_name: CollectionObjectName,
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        proximity: float = 0.000000,
        skip_factor: int = 0,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
    ) -> QueryCloudsToSurfaceResult:
        return cast(
            QueryCloudsToSurfaceResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryCloudsToSurface",
                "analysis_operations.query_clouds_to_surface",
                {
                    "cloud_names": cloud_names,
                    "filter_surface_name": filter_surface_name,
                    "resulting_object_name": resulting_object_name,
                    "projection_options": projection_options,
                    "proximity": proximity,
                    "skip_factor": skip_factor,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                },
                QueryCloudsToSurfaceResult,
            ),
        )

    async def query_frame_to_frame(
        self,
        reference_frame_name: CollectionObjectName,
        corresponding_frame_name: CollectionObjectName,
    ) -> QueryFrameToFrameResult:
        return cast(
            QueryFrameToFrameResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryFrameToFrame",
                "analysis_operations.query_frame_to_frame",
                {
                    "reference_frame_name": reference_frame_name,
                    "corresponding_frame_name": corresponding_frame_name,
                },
                QueryFrameToFrameResult,
            ),
        )

    async def query_groups_to_objects(
        self,
        group_name_list_groups_to_project: Iterable[CollectionObjectName],
        object_name_list_objects_to_project_to: Iterable[CollectionObjectName],
        resulting_object_name: CollectionObjectName,
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
        show_results_dialog: bool = False,
    ) -> QueryGroupsToObjectsResult:
        return cast(
            QueryGroupsToObjectsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryGroupsToObjects",
                "analysis_operations.query_groups_to_objects",
                {
                    "group_name_list_groups_to_project": group_name_list_groups_to_project,
                    "object_name_list_objects_to_project_to": object_name_list_objects_to_project_to,
                    "resulting_object_name": resulting_object_name,
                    "projection_options": projection_options,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                    "show_results_dialog": show_results_dialog,
                },
                QueryGroupsToObjectsResult,
            ),
        )

    async def query_point_to_objects(
        self,
        point_name: PointName,
        objects: Iterable[CollectionObjectName],
        *,
        ignore_target_offset: bool = False,
    ) -> QueryPointToObjectsResult:
        return cast(
            QueryPointToObjectsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryPointToObjects",
                "analysis_operations.query_point_to_objects",
                {
                    "point_name": point_name,
                    "objects": objects,
                    "ignore_target_offset": ignore_target_offset,
                },
                QueryPointToObjectsResult,
            ),
        )

    async def query_point_to_point_along_curve(
        self,
        value_1st_point: PointName,
        value_2nd_point: PointName,
        curve: CollectionObjectName,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryPointToPointAlongCurve",
                "analysis_operations.query_point_to_point_along_curve",
                {
                    "value_1st_point": value_1st_point,
                    "value_2nd_point": value_2nd_point,
                    "curve": curve,
                },
                None,
            ),
        )

    async def query_points_to_circle(
        self,
        circle_name: CollectionObjectName,
        point_group_name: CollectionObjectName,
        *,
        is_inside_measurement: bool = True,
        auto_scale_vectors_to_of_radius: int = 40,
        vector_group_name_for_radial: CollectionObjectName,
        vector_group_name_for_planar: CollectionObjectName,
        vector_group_name_for_combined: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "QueryPointsToCircle",
            "analysis_operations.query_points_to_circle",
            {
                "circle_name": circle_name,
                "point_group_name": point_group_name,
                "is_inside_measurement": is_inside_measurement,
                "auto_scale_vectors_to_of_radius": auto_scale_vectors_to_of_radius,
                "vector_group_name_for_radial": vector_group_name_for_radial,
                "vector_group_name_for_planar": vector_group_name_for_planar,
                "vector_group_name_for_combined": vector_group_name_for_combined,
            },
            None,
        )
        return None

    async def query_points_to_objects(
        self,
        point_names: Iterable[PointName],
        object_name_list_objects_to_project_to: Iterable[CollectionObjectName],
        resulting_object_name: CollectionObjectName,
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
        rms_tolerance_0_0_for_none: float = 0.000000,
        maximum_absolute_tolerance_0_0_for_none: float = 0.000000,
        show_results_dialog: bool = False,
    ) -> QueryPointsToObjectsResult:
        return cast(
            QueryPointsToObjectsResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "QueryPointsToObjects",
                "analysis_operations.query_points_to_objects",
                {
                    "point_names": point_names,
                    "object_name_list_objects_to_project_to": object_name_list_objects_to_project_to,
                    "resulting_object_name": resulting_object_name,
                    "projection_options": projection_options,
                    "rms_tolerance_0_0_for_none": rms_tolerance_0_0_for_none,
                    "maximum_absolute_tolerance_0_0_for_none": maximum_absolute_tolerance_0_0_for_none,
                    "show_results_dialog": show_results_dialog,
                },
                QueryPointsToObjectsResult,
            ),
        )

    async def query_points_to_single_point(
        self,
        point_names: Iterable[PointName],
        single_point: PointName,
        *,
        show_vector_properties: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "QueryPointsToSinglePoint",
            "analysis_operations.query_points_to_single_point",
            {
                "point_names": point_names,
                "single_point": single_point,
                "show_vector_properties": show_vector_properties,
            },
            None,
        )
        return None

    async def re_compute_calculated_items(
        self,
        *,
        targets_from_shots: bool = False,
        hidden_points: bool = False,
        relationships: bool = False,
        refresh_filtered_cloud_data: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "ReComputeCalculatedItems",
            "analysis_operations.re_compute_calculated_items",
            {
                "targets_from_shots": targets_from_shots,
                "hidden_points": hidden_points,
                "relationships": relationships,
                "refresh_filtered_cloud_data": refresh_filtered_cloud_data,
            },
            None,
        )
        return None

    async def rename_points_based_on_inter_point_distance_to_reference_points(
        self,
        reference_group_name: CollectionObjectName,
        group_to_rename_points: CollectionObjectName,
        *,
        distance_threshold: float = 0.000000,
        verify_results: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "RenamePointsBasedOnInterPointDistanceToReferencePoints",
            "analysis_operations.rename_points_based_on_inter_point_distance_to_reference_points",
            {
                "reference_group_name": reference_group_name,
                "group_to_rename_points": group_to_rename_points,
                "distance_threshold": distance_threshold,
                "verify_results": verify_results,
            },
            None,
        )
        return None

    async def rename_points_based_on_proximity_to_reference_points(
        self,
        reference_group_name: CollectionObjectName,
        group_to_rename_points: CollectionObjectName,
        *,
        proximity_threshold: float = 0.000000,
        verify_results: bool = False,
        rename_all_proximate_points: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "RenamePointsBasedOnProximityToReferencePoints",
            "analysis_operations.rename_points_based_on_proximity_to_reference_points",
            {
                "reference_group_name": reference_group_name,
                "group_to_rename_points": group_to_rename_points,
                "proximity_threshold": proximity_threshold,
                "verify_results": verify_results,
                "rename_all_proximate_points": rename_all_proximate_points,
            },
            None,
        )
        return None

    async def reverse_bsplines(
        self,
        b_spline_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "ReverseBSplines",
            "analysis_operations.reverse_bsplines",
            {
                "b_spline_list": b_spline_list,
            },
            None,
        )
        return None

    async def reverse_plane_normals(
        self,
        plane_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "ReversePlaneNormals",
            "analysis_operations.reverse_plane_normals",
            {
                "plane_list": plane_list,
            },
            None,
        )
        return None

    async def reverse_surface_normals(
        self,
        surface_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "ReverseSurfaceNormals",
            "analysis_operations.reverse_surface_normals",
            {
                "surface_list": surface_list,
            },
            None,
        )
        return None

    async def set_circle_properties(
        self,
        circle_name: CollectionObjectName,
        center_coordinate: Vector,
        normal_direction: Vector,
        *,
        radius: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetCircleProperties",
            "analysis_operations.set_circle_properties",
            {
                "circle_name": circle_name,
                "center_coordinate": center_coordinate,
                "normal_direction": normal_direction,
                "radius": radius,
            },
            None,
        )
        return None

    async def set_cone_properties(
        self,
        cone_name: CollectionObjectName,
        cone_end_point_in_working_coordinates: Vector,
        cone_axis_in_working_coordinates: Vector,
        *,
        cone_length: float = 0.000000,
        cone_theta_start: float = 0.000000,
        cone_theta_span: float = 0.000000,
        cone_included_angle: float = 0.000000,
        cut_length_from_apex: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetConeProperties",
            "analysis_operations.set_cone_properties",
            {
                "cone_name": cone_name,
                "cone_end_point_in_working_coordinates": cone_end_point_in_working_coordinates,
                "cone_axis_in_working_coordinates": cone_axis_in_working_coordinates,
                "cone_length": cone_length,
                "cone_theta_start": cone_theta_start,
                "cone_theta_span": cone_theta_span,
                "cone_included_angle": cone_included_angle,
                "cut_length_from_apex": cut_length_from_apex,
            },
            None,
        )
        return None

    async def set_cylinder_properties(
        self,
        cylinder_name: CollectionObjectName,
        begin_coordinate: Vector,
        axis_direction: Vector,
        *,
        length: float = 0.000000,
        diameter: float = 0.000000,
        nominals_point_inward: bool = True,
        facets: int = 32,
        enable_theta_extent_display_mode: bool = True,
        theta_start_in_degrees: float = 0.000000,
        theta_span_in_degrees: float = 360.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetCylinderProperties",
            "analysis_operations.set_cylinder_properties",
            {
                "cylinder_name": cylinder_name,
                "begin_coordinate": begin_coordinate,
                "axis_direction": axis_direction,
                "length": length,
                "diameter": diameter,
                "nominals_point_inward": nominals_point_inward,
                "facets": facets,
                "enable_theta_extent_display_mode": enable_theta_extent_display_mode,
                "theta_start_in_degrees": theta_start_in_degrees,
                "theta_span_in_degrees": theta_span_in_degrees,
            },
            None,
        )
        return None

    async def set_default_colorization_options(
        self,
        *,
        colorization_options: ColorizationOptions = ColorizationOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetDefaultColorizationOptions",
            "analysis_operations.set_default_colorization_options",
            {
                "colorization_options": colorization_options,
            },
            None,
        )
        return None

    async def set_ellipse_properties(
        self,
        ellipse_name: CollectionObjectName,
        center_coordinate: Vector,
        normal_direction: Vector,
        *,
        major_axis_radius: float = 0.000000,
        minor_axis_radius: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetEllipseProperties",
            "analysis_operations.set_ellipse_properties",
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

    async def set_geometry_relationship_fit_profile(
        self,
        geometry_type: GeometryType,
        relationship_ref_list: Iterable[CollectionItemName],
        *,
        fit_profile_name: str = "",
        apply_cardinal_point_settings: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetGeometryRelationshipFitProfile",
            "analysis_operations.set_geometry_relationship_fit_profile",
            {
                "geometry_type": geometry_type,
                "relationship_ref_list": relationship_ref_list,
                "fit_profile_name": fit_profile_name,
                "apply_cardinal_point_settings": apply_cardinal_point_settings,
            },
            None,
        )
        return None

    async def set_line_properties(
        self,
        line_name: CollectionObjectName,
        begin_coordinate: Vector,
        end_coordinate: Vector,
        *,
        length_optional: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetLineProperties",
            "analysis_operations.set_line_properties",
            {
                "line_name": line_name,
                "begin_coordinate": begin_coordinate,
                "end_coordinate": end_coordinate,
                "length_optional": length_optional,
            },
            None,
        )
        return None

    async def set_measurement_auxiliary_data(
        self,
        point_name: PointName,
        *,
        auxiliary_name: str = "",
        value: float = 0.000000,
        units: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetMeasurementAuxiliaryData",
            "analysis_operations.set_measurement_auxiliary_data",
            {
                "point_name": point_name,
                "auxiliary_name": auxiliary_name,
                "value": value,
                "units": units,
            },
            None,
        )
        return None

    async def set_object_reporting_frame(
        self,
        object_name: CollectionObjectName,
        reporting_frame: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetObjectReportingFrame",
            "analysis_operations.set_object_reporting_frame",
            {
                "object_name": object_name,
                "reporting_frame": reporting_frame,
            },
            None,
        )
        return None

    async def set_point_properties(
        self,
        point_name_list: Iterable[PointName],
        *,
        planar_offset: float = 0.000000,
        radial_offset: float = 0.000000,
        position_tolerance: ToleranceVectorOptions,
        component_weights: Vector,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetPointProperties",
            "analysis_operations.set_point_properties",
            {
                "point_name_list": point_name_list,
                "planar_offset": planar_offset,
                "radial_offset": radial_offset,
                "position_tolerance": position_tolerance,
                "component_weights": component_weights,
            },
            None,
        )
        return None

    async def set_point_weights_from_uncertainties(
        self,
        point_name_list: Iterable[PointName],
        *,
        uncertainty_reference_frame_mode: str = "With respect to WORLD",
        reporting_frame: CollectionObjectName,
        weight_normalization_mode: str = "Set to fixed value",
        fixed_weight_value: float = 1.000000,
        output_weighted_point_group: CollectionObjectName,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "SetPointWeightsFromUncertainties",
                "analysis_operations.set_point_weights_from_uncertainties",
                {
                    "point_name_list": point_name_list,
                    "uncertainty_reference_frame_mode": uncertainty_reference_frame_mode,
                    "reporting_frame": reporting_frame,
                    "weight_normalization_mode": weight_normalization_mode,
                    "fixed_weight_value": fixed_weight_value,
                    "output_weighted_point_group": output_weighted_point_group,
                },
                None,
            ),
        )

    async def set_transform_for_ith_frame_in_frame_set(
        self,
        frame_set: CollectionObjectName,
        *,
        frame_set_index: int = 0,
        transform_in_working: Transform,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "SetTransformForIthFrameInFrameSet",
            "analysis_operations.set_transform_for_ith_frame_in_frame_set",
            {
                "frame_set": frame_set,
                "frame_set_index": frame_set_index,
                "transform_in_working": transform_in_working,
            },
            None,
        )
        return None

    async def sphere_axis_check(
        self,
        sphere_points_group_name: CollectionObjectName,
        *,
        sphere_target_radius: float = 0.000000,
        point_to_create_at_sphere_center: PointName,
        line_defining_the_axis: CollectionObjectName,
    ) -> SphereAxisCheckResult:
        return cast(
            SphereAxisCheckResult,
            await self._invoke_mp_operation(
                "briosa.AnalysisOperations",
                "SphereAxisCheck",
                "analysis_operations.sphere_axis_check",
                {
                    "sphere_points_group_name": sphere_points_group_name,
                    "sphere_target_radius": sphere_target_radius,
                    "point_to_create_at_sphere_center": point_to_create_at_sphere_center,
                    "line_defining_the_axis": line_defining_the_axis,
                },
                SphereAxisCheckResult,
            ),
        )

    async def temperature_compensate_a_group(
        self,
        original_group: CollectionObjectName,
        scaling_origin_coordinate_frame: FrameName,
        *,
        material_cte_1_deg_f: float = 0.000000,
        initial_temperature_f: float = 0.000000,
        final_temperature_f: float = 0.000000,
        scaled_group_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "TemperatureCompensateAGroup",
            "analysis_operations.temperature_compensate_a_group",
            {
                "original_group": original_group,
                "scaling_origin_coordinate_frame": scaling_origin_coordinate_frame,
                "material_cte_1_deg_f": material_cte_1_deg_f,
                "initial_temperature_f": initial_temperature_f,
                "final_temperature_f": final_temperature_f,
                "scaled_group_name": scaled_group_name,
            },
            None,
        )
        return None

    async def transform_objects_frame_to_frame(
        self,
        object_name_list: Iterable[CollectionObjectName],
        initial_frame_name: CollectionObjectName,
        destination_frame_name: CollectionObjectName,
        *,
        number_of_steps: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "TransformObjectsFrameToFrame",
            "analysis_operations.transform_objects_frame_to_frame",
            {
                "object_name_list": object_name_list,
                "initial_frame_name": initial_frame_name,
                "destination_frame_name": destination_frame_name,
                "number_of_steps": number_of_steps,
            },
            None,
        )
        return None

    async def transform_objects_by_delta_about_working_frame(
        self,
        objects_to_transform: Iterable[CollectionObjectName],
        delta_transform: Transform,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "TransformObjectsByDeltaAboutWorkingFrame",
            "analysis_operations.transform_objects_by_delta_about_working_frame",
            {
                "objects_to_transform": objects_to_transform,
                "delta_transform": delta_transform,
            },
            None,
        )
        return None

    async def transform_objects_by_delta_world_transform_operator(
        self,
        objects_to_transform: Iterable[CollectionObjectName],
        delta_transform: WorldTransform,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "TransformObjectsByDeltaWorldTransformOperator",
            "analysis_operations.transform_objects_by_delta_world_transform_operator",
            {
                "objects_to_transform": objects_to_transform,
                "delta_transform": delta_transform,
            },
            None,
        )
        return None

    async def translate_objects_by_delta(
        self,
        objects_to_translate: Iterable[CollectionObjectName],
        delta_translation: Vector,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.AnalysisOperations",
            "TranslateObjectsByDelta",
            "analysis_operations.translate_objects_by_delta",
            {
                "objects_to_translate": objects_to_translate,
                "delta_translation": delta_translation,
            },
            None,
        )
        return None

    async def delete_dimension(
        self,
        dimension_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.DimensionOperations",
            "DeleteDimension",
            "dimension_operations.delete_dimension",
            {
                "dimension_name": dimension_name,
            },
            None,
        )
        return None

    async def get_dimension_value(
        self,
        dimension_name: CollectionObjectName,
    ) -> GetDimensionValueResult:
        return cast(
            GetDimensionValueResult,
            await self._invoke_mp_operation(
                "briosa.DimensionOperations",
                "GetDimensionValue",
                "dimension_operations.get_dimension_value",
                {
                    "dimension_name": dimension_name,
                },
                GetDimensionValueResult,
            ),
        )

    async def set_dimension_tolerance(
        self,
        dimension_name: CollectionItemName,
        *,
        enable_nominal: bool = False,
        enable_high: bool = False,
        enable_low: bool = False,
        nominal: float = 0.000000,
        high_tolerance: float = 0.000000,
        low_tolerance: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.DimensionOperations",
            "SetDimensionTolerance",
            "dimension_operations.set_dimension_tolerance",
            {
                "dimension_name": dimension_name,
                "enable_nominal": enable_nominal,
                "enable_high": enable_high,
                "enable_low": enable_low,
                "nominal": nominal,
                "high_tolerance": high_tolerance,
                "low_tolerance": low_tolerance,
            },
            None,
        )
        return None

    async def delete_event(
        self,
        event_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.EventOperations",
            "DeleteEvent",
            "event_operations.delete_event",
            {
                "event_name": event_name,
            },
            None,
        )
        return None

    async def export_event_ref_list(
        self,
        event_list: Iterable[CollectionItemName],
        file_path: FileReference,
        *,
        decimal_precision: int = 6,
        overwrite_existing_file: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.EventOperations",
            "ExportEventRefList",
            "event_operations.export_event_ref_list",
            {
                "event_list": event_list,
                "file_path": file_path,
                "decimal_precision": decimal_precision,
                "overwrite_existing_file": overwrite_existing_file,
            },
            None,
        )
        return None

    async def get_ith_event_from_event_ref_list(
        self,
        event_list: Iterable[CollectionItemName],
        *,
        event_index: int = 0,
    ) -> CollectionItemName:
        return cast(
            CollectionItemName,
            await self._invoke_mp_operation(
                "briosa.EventOperations",
                "GetIthEventFromEventRefList",
                "event_operations.get_ith_event_from_event_ref_list",
                {
                    "event_list": event_list,
                    "event_index": event_index,
                },
                None,
            ),
        )

    async def get_number_of_events_in_event_ref_list(
        self,
        event_list: Iterable[CollectionItemName],
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.EventOperations",
                "GetNumberOfEventsInEventRefList",
                "event_operations.get_number_of_events_in_event_ref_list",
                {
                    "event_list": event_list,
                },
                None,
            ),
        )

    async def rename_event(
        self,
        original_event_name: CollectionObjectName,
        new_event_name: CollectionObjectName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.EventOperations",
            "RenameEvent",
            "event_operations.rename_event",
            {
                "original_event_name": original_event_name,
                "new_event_name": new_event_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def backup_now(self) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "BackupNow",
            "file_operations.backup_now",
            {},
            None,
        )
        return None

    async def copy_general_file(
        self,
        source_file_name: FileReference,
        destination_file_name: FileReference,
        *,
        overwrite: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "CopyGeneralFile",
            "file_operations.copy_general_file",
            {
                "source_file_name": source_file_name,
                "destination_file_name": destination_file_name,
                "overwrite": overwrite,
            },
            None,
        )
        return None

    async def delete_general_file(
        self,
        file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "DeleteGeneralFile",
            "file_operations.delete_general_file",
            {
                "file_name": file_name,
            },
            None,
        )
        return None

    async def direct_cad_access(
        self,
        cad_file_name: FileReference,
        *,
        import_solids: bool = True,
        import_surfaces: bool = True,
        import_polygonized_surfaces: bool = True,
        import_annotations: bool = True,
        import_vectors: bool = True,
        import_points: bool = True,
        point_group_name: str = "CAD pts",
        import_attributes_metadata: bool = True,
        import_cooordinate_frames: bool = True,
        import_planes: bool = True,
        import_3d_curves_lines: bool = True,
        import_3d_curves_circles: bool = True,
        import_3d_curves_general_curves: bool = True,
        import_construction_geometry: bool = False,
        import_hidden_entities: bool = False,
        import_all_surfaces_as_mesh_graphical_entities: bool = False,
        do_not_import_fillets: bool = False,
        do_not_import_dittos: bool = False,
        ditto_threshold: int = 1,
        center_view_on_imported_objects: bool = True,
        import_into_folders_matching_cad_file_hierarchy: bool = False,
        remove_empty_folders: bool = True,
        surface_normals_mode_1_or_2: int = 1,
        prompt_on_missing_components: bool = True,
        selective_import: bool = False,
        surface_compatibility_mode: bool = True,
        explode_surfaces: bool = False,
        cad_file_units_leave_blank_to_use_the_units_specified_in_the_file: str = "",
        build_callout_views: bool = True,
    ) -> DirectCadAccessResult:
        return cast(
            DirectCadAccessResult,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "DirectCadAccess",
                "file_operations.direct_cad_access",
                {
                    "cad_file_name": cad_file_name,
                    "import_solids": import_solids,
                    "import_surfaces": import_surfaces,
                    "import_polygonized_surfaces": import_polygonized_surfaces,
                    "import_annotations": import_annotations,
                    "import_vectors": import_vectors,
                    "import_points": import_points,
                    "point_group_name": point_group_name,
                    "import_attributes_metadata": import_attributes_metadata,
                    "import_cooordinate_frames": import_cooordinate_frames,
                    "import_planes": import_planes,
                    "import_3d_curves_lines": import_3d_curves_lines,
                    "import_3d_curves_circles": import_3d_curves_circles,
                    "import_3d_curves_general_curves": import_3d_curves_general_curves,
                    "import_construction_geometry": import_construction_geometry,
                    "import_hidden_entities": import_hidden_entities,
                    "import_all_surfaces_as_mesh_graphical_entities": import_all_surfaces_as_mesh_graphical_entities,
                    "do_not_import_fillets": do_not_import_fillets,
                    "do_not_import_dittos": do_not_import_dittos,
                    "ditto_threshold": ditto_threshold,
                    "center_view_on_imported_objects": center_view_on_imported_objects,
                    "import_into_folders_matching_cad_file_hierarchy": import_into_folders_matching_cad_file_hierarchy,
                    "remove_empty_folders": remove_empty_folders,
                    "surface_normals_mode_1_or_2": surface_normals_mode_1_or_2,
                    "prompt_on_missing_components": prompt_on_missing_components,
                    "selective_import": selective_import,
                    "surface_compatibility_mode": surface_compatibility_mode,
                    "explode_surfaces": explode_surfaces,
                    "cad_file_units_leave_blank_to_use_the_units_specified_in_the_file": cad_file_units_leave_blank_to_use_the_units_specified_in_the_file,
                    "build_callout_views": build_callout_views,
                },
                DirectCadAccessResult,
            ),
        )

    async def export_ascii_frame_set(
        self,
        ascii_file_path: FileReference,
        frame_set_container: CollectionObjectName,
        data_delimiter: ExportDataDelimeterType,
        file_format: AsciiFileFormat,
        *,
        include_export_format_info: bool = False,
        decimal_precision: int = 6,
        append: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportAsciiFrameSet",
            "file_operations.export_ascii_frame_set",
            {
                "ascii_file_path": ascii_file_path,
                "frame_set_container": frame_set_container,
                "data_delimiter": data_delimiter,
                "file_format": file_format,
                "include_export_format_info": include_export_format_info,
                "decimal_precision": decimal_precision,
                "append": append,
            },
            None,
        )
        return None

    async def export_ascii_frames(
        self,
        ascii_file_path: FileReference,
        object_list: Iterable[CollectionObjectName],
        *,
        export_frame_mode: str = "Fixed XYZ",
        overwrite_existing_file: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportAsciiFrames",
            "file_operations.export_ascii_frames",
            {
                "ascii_file_path": ascii_file_path,
                "object_list": object_list,
                "export_frame_mode": export_frame_mode,
                "overwrite_existing_file": overwrite_existing_file,
            },
            None,
        )
        return None

    async def export_ascii_point_clouds(
        self,
        ascii_file_path: FileReference,
        point_cloud_list: Iterable[CollectionObjectName],
        data_delimiter: ExportDataDelimeterType,
        *,
        overwrite_existing_file: bool = False,
        show_progress_dialog: bool = False,
        include_cloud_point_labeling: bool = False,
        include_scan_direction_vector: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportAsciiPointClouds",
            "file_operations.export_ascii_point_clouds",
            {
                "ascii_file_path": ascii_file_path,
                "point_cloud_list": point_cloud_list,
                "data_delimiter": data_delimiter,
                "overwrite_existing_file": overwrite_existing_file,
                "show_progress_dialog": show_progress_dialog,
                "include_cloud_point_labeling": include_cloud_point_labeling,
                "include_scan_direction_vector": include_scan_direction_vector,
            },
            None,
        )
        return None

    async def export_ascii_point_set(
        self,
        ascii_file_path: FileReference,
        point_set_container: CollectionObjectName,
        data_delimiter: ExportDataDelimeterType,
        target_name_format: ExportTargetNameFormat,
        desired_coordinate_system: CoordinateSystemType,
        *,
        include_target_offsets: bool = False,
        include_timestamps: bool = False,
        include_sa_version_and_frame_comments: bool = False,
        include_axis_comments: bool = False,
        include_export_format_info: bool = False,
        maximum_precision_scientific_notation: bool = False,
        decimal_precision: int = 6,
        append: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportAsciiPointSet",
            "file_operations.export_ascii_point_set",
            {
                "ascii_file_path": ascii_file_path,
                "point_set_container": point_set_container,
                "data_delimiter": data_delimiter,
                "target_name_format": target_name_format,
                "desired_coordinate_system": desired_coordinate_system,
                "include_target_offsets": include_target_offsets,
                "include_timestamps": include_timestamps,
                "include_sa_version_and_frame_comments": include_sa_version_and_frame_comments,
                "include_axis_comments": include_axis_comments,
                "include_export_format_info": include_export_format_info,
                "maximum_precision_scientific_notation": maximum_precision_scientific_notation,
                "decimal_precision": decimal_precision,
                "append": append,
            },
            None,
        )
        return None

    async def export_ascii_points(
        self,
        ascii_file_path: FileReference,
        group_names_to_export: Iterable[CollectionGroupName],
        data_delimiter: ExportDataDelimeterType,
        target_name_format: ExportTargetNameFormat,
        desired_coordinate_system: CoordinateSystemType,
        *,
        include_target_offsets: bool = False,
        include_target_comments: bool = False,
        include_timestamps: bool = False,
        include_tolerances: bool = False,
        include_coordinate_uncertainties: bool = False,
        include_sa_version_and_frame_comments: bool = False,
        include_axis_comments: bool = False,
        include_export_format_info: bool = False,
        include_weights: bool = False,
        include_measurement_details: bool = False,
        maximum_precision_scientific_notation: bool = False,
        decimal_precision: int = 6,
        append: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportAsciiPoints",
            "file_operations.export_ascii_points",
            {
                "ascii_file_path": ascii_file_path,
                "group_names_to_export": group_names_to_export,
                "data_delimiter": data_delimiter,
                "target_name_format": target_name_format,
                "desired_coordinate_system": desired_coordinate_system,
                "include_target_offsets": include_target_offsets,
                "include_target_comments": include_target_comments,
                "include_timestamps": include_timestamps,
                "include_tolerances": include_tolerances,
                "include_coordinate_uncertainties": include_coordinate_uncertainties,
                "include_sa_version_and_frame_comments": include_sa_version_and_frame_comments,
                "include_axis_comments": include_axis_comments,
                "include_export_format_info": include_export_format_info,
                "include_weights": include_weights,
                "include_measurement_details": include_measurement_details,
                "maximum_precision_scientific_notation": maximum_precision_scientific_notation,
                "decimal_precision": decimal_precision,
                "append": append,
            },
            None,
        )
        return None

    async def export_dxf(
        self,
        dxf_file_path: FileReference,
        point_names: Iterable[PointName],
        cloud_names: Iterable[CollectionObjectName],
        *,
        include_point_labels: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportDxf",
            "file_operations.export_dxf",
            {
                "dxf_file_path": dxf_file_path,
                "point_names": point_names,
                "cloud_names": cloud_names,
                "include_point_labels": include_point_labels,
            },
            None,
        )
        return None

    async def export_embedded_file(
        self,
        embedded_file_collection_name: CollectionName,
        *,
        embedded_file_name: str = "",
        external_file_name: FileReference,
        replace_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportEmbeddedFile",
            "file_operations.export_embedded_file",
            {
                "embedded_file_collection_name": embedded_file_collection_name,
                "embedded_file_name": embedded_file_name,
                "external_file_name": external_file_name,
                "replace_existing": replace_existing,
            },
            None,
        )
        return None

    async def export_hidden_point_bar_xml_file(
        self,
        xml_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportHiddenPointBarXmlFile",
            "file_operations.export_hidden_point_bar_xml_file",
            {
                "xml_file_path": xml_file_path,
            },
            None,
        )
        return None

    async def export_iges_file_entire_model(
        self,
        iges_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportIgesFileEntireModel",
            "file_operations.export_iges_file_entire_model",
            {
                "iges_file_path": iges_file_path,
            },
            None,
        )
        return None

    async def export_iges_file_partial_model(
        self,
        iges_file_path: FileReference,
        object_name_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportIgesFilePartialModel",
            "file_operations.export_iges_file_partial_model",
            {
                "iges_file_path": iges_file_path,
                "object_name_list": object_name_list,
            },
            None,
        )
        return None

    async def export_ptx_point_clouds(
        self,
        ptx_file_path: FileReference,
        point_cloud_list: Iterable[CollectionObjectName],
        *,
        overwrite_existing_file: bool = False,
        show_progress_dialog: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportPtxPointClouds",
            "file_operations.export_ptx_point_clouds",
            {
                "ptx_file_path": ptx_file_path,
                "point_cloud_list": point_cloud_list,
                "overwrite_existing_file": overwrite_existing_file,
                "show_progress_dialog": show_progress_dialog,
            },
            None,
        )
        return None

    async def export_qdas_characteristics(
        self,
        qdas_export_file_path: FileReference,
        *,
        k1001_part_number: str = "",
        k1002_part_description: str = "",
        k1071_supplier_number: str = "",
        k1072_supplier_description: str = "",
        k1203_reason_for_test: str = "",
        k1303_plant: str = "",
        k1900_part_remark: str = "",
        k0006_batch_number: str = "",
        k0014_part_id: str = "",
        k0053_order_number: str = "",
        k0004_date_time_stamp: str = "2026-07-20/16:32:22",
        k0008_operator_identifier: int = -1,
        k0010_machine_identifier: int = -1,
        k0012_gage_identifier: int = -1,
        relationship_list: Iterable[CollectionItemName],
        feature_check_list: Iterable[CollectionItemName],
        vector_group_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportQdasCharacteristics",
            "file_operations.export_qdas_characteristics",
            {
                "qdas_export_file_path": qdas_export_file_path,
                "k1001_part_number": k1001_part_number,
                "k1002_part_description": k1002_part_description,
                "k1071_supplier_number": k1071_supplier_number,
                "k1072_supplier_description": k1072_supplier_description,
                "k1203_reason_for_test": k1203_reason_for_test,
                "k1303_plant": k1303_plant,
                "k1900_part_remark": k1900_part_remark,
                "k0006_batch_number": k0006_batch_number,
                "k0014_part_id": k0014_part_id,
                "k0053_order_number": k0053_order_number,
                "k0004_date_time_stamp": k0004_date_time_stamp,
                "k0008_operator_identifier": k0008_operator_identifier,
                "k0010_machine_identifier": k0010_machine_identifier,
                "k0012_gage_identifier": k0012_gage_identifier,
                "relationship_list": relationship_list,
                "feature_check_list": feature_check_list,
                "vector_group_list": vector_group_list,
            },
            None,
        )
        return None

    async def export_qdas_data_list(
        self,
        qdas_export_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportQdasDataList",
            "file_operations.export_qdas_data_list",
            {
                "qdas_export_file_path": qdas_export_file_path,
            },
            None,
        )
        return None

    async def export_scan_stripe_mesh_to_stl_file(
        self,
        stl_file_path: FileReference,
        mesh: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportScanStripeMeshToStlFile",
            "file_operations.export_scan_stripe_mesh_to_stl_file",
            {
                "stl_file_path": stl_file_path,
                "mesh": mesh,
            },
            None,
        )
        return None

    async def export_step_file_entire_model(
        self,
        step_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportStepFileEntireModel",
            "file_operations.export_step_file_entire_model",
            {
                "step_file_path": step_file_path,
            },
            None,
        )
        return None

    async def export_step_file_partial_model(
        self,
        step_file_path: FileReference,
        object_name_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportStepFilePartialModel",
            "file_operations.export_step_file_partial_model",
            {
                "step_file_path": step_file_path,
                "object_name_list": object_name_list,
            },
            None,
        )
        return None

    async def export_vda_fs_file_entire_model(
        self,
        vda_fs_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportVdaFsFileEntireModel",
            "file_operations.export_vda_fs_file_entire_model",
            {
                "vda_fs_file_path": vda_fs_file_path,
            },
            None,
        )
        return None

    async def export_vda_fs_file_partial_model(
        self,
        vda_fs_file_path: FileReference,
        object_name_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportVdaFsFilePartialModel",
            "file_operations.export_vda_fs_file_partial_model",
            {
                "vda_fs_file_path": vda_fs_file_path,
                "object_name_list": object_name_list,
            },
            None,
        )
        return None

    async def export_vector_container_to_ascii_file(
        self,
        ascii_file_path: FileReference,
        vector_groups_to_export: Iterable[CollectionVectorGroupName],
        *,
        overwrite_existing_file_false_append: bool = True,
        use_full_precision_scientific_notation: bool = False,
        vector_name_format: ExportVectorNameFormat,
        include_vector_length: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ExportVectorContainerToAsciiFile",
            "file_operations.export_vector_container_to_ascii_file",
            {
                "ascii_file_path": ascii_file_path,
                "vector_groups_to_export": vector_groups_to_export,
                "overwrite_existing_file_false_append": overwrite_existing_file_false_append,
                "use_full_precision_scientific_notation": use_full_precision_scientific_notation,
                "vector_name_format": vector_name_format,
                "include_vector_length": include_vector_length,
            },
            None,
        )
        return None

    async def find_files_in_directory(
        self,
        *,
        directory: str = "",
        file_name_pattern: str = "*.*",
        recursive: bool = False,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "FindFilesInDirectory",
                "file_operations.find_files_in_directory",
                {
                    "directory": directory,
                    "file_name_pattern": file_name_pattern,
                    "recursive": recursive,
                },
                None,
            ),
        )

    async def find_sub_directories_in_directory(
        self,
        *,
        directory: str = "",
        recursive: bool = False,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "FindSubDirectoriesInDirectory",
                "file_operations.find_sub_directories_in_directory",
                {
                    "directory": directory,
                    "recursive": recursive,
                },
                None,
            ),
        )

    async def get_boolean_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        boolean_name: str = "",
    ) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetBooleanFromDataShareFile",
                "file_operations.get_boolean_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "boolean_name": boolean_name,
                },
                None,
            ),
        )

    async def get_double_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        double_name: str = "",
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetDoubleFromDataShareFile",
                "file_operations.get_double_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "double_name": double_name,
                },
                None,
            ),
        )

    async def get_integer_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        integer_name: str = "",
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetIntegerFromDataShareFile",
                "file_operations.get_integer_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "integer_name": integer_name,
                },
                None,
            ),
        )

    async def get_qdas_catalog_entries(
        self,
        *,
        k_field_target: str = "",
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetQdasCatalogEntries",
                "file_operations.get_qdas_catalog_entries",
                {
                    "k_field_target": k_field_target,
                },
                None,
            ),
        )

    async def get_string_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        string_name: str = "",
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetStringFromDataShareFile",
                "file_operations.get_string_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "string_name": string_name,
                },
                None,
            ),
        )

    async def get_transform_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        transform_name: str = "",
    ) -> Transform:
        return cast(
            Transform,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetTransformFromDataShareFile",
                "file_operations.get_transform_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "transform_name": transform_name,
                },
                None,
            ),
        )

    async def get_vector_from_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        vector_name: str = "",
    ) -> Vector:
        return cast(
            Vector,
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "GetVectorFromDataShareFile",
                "file_operations.get_vector_from_data_share_file",
                {
                    "data_share_file_path": data_share_file_path,
                    "vector_name": vector_name,
                },
                None,
            ),
        )

    async def import_ascii_predefined_formats(
        self,
        ascii_file_path: FileReference,
        file_format: AsciiFileFormat,
        *,
        units: DistanceUnits = DistanceUnits.INCHES,
        angular_units: AngularUnits = AngularUnits.DEGREES,
        group_name: CollectionObjectName,
        import_as_cloud: bool = False,
        ensure_new_point_group: bool = True,
        ensure_unique_names: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportAsciiPredefinedFormats",
            "file_operations.import_ascii_predefined_formats",
            {
                "ascii_file_path": ascii_file_path,
                "file_format": file_format,
                "units": units,
                "angular_units": angular_units,
                "group_name": group_name,
                "import_as_cloud": import_as_cloud,
                "ensure_new_point_group": ensure_new_point_group,
                "ensure_unique_names": ensure_unique_names,
            },
            None,
        )
        return None

    async def import_ascii_predefined_frame_set_formats(
        self,
        ascii_file_path: FileReference,
        file_format: AsciiFileFormat,
        *,
        units: DistanceUnits = DistanceUnits.INCHES,
        angular_units: AngularUnits = AngularUnits.DEGREES,
        frame_set_container_name: CollectionObjectName,
        ensure_unique_name: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportAsciiPredefinedFrameSetFormats",
            "file_operations.import_ascii_predefined_frame_set_formats",
            {
                "ascii_file_path": ascii_file_path,
                "file_format": file_format,
                "units": units,
                "angular_units": angular_units,
                "frame_set_container_name": frame_set_container_name,
                "ensure_unique_name": ensure_unique_name,
            },
            None,
        )
        return None

    async def import_e57_file(
        self,
        e57_file_path: FileReference,
        *,
        save_converted_file: bool = False,
        use_square_root_of_intensity: bool = True,
        automatically_close_converter: bool = True,
        prioritize_color_over_intensity: bool = True,
        import_scan_blocks_as_separate_clouds: bool = False,
        units: DistanceUnits = DistanceUnits.INCHES,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportE57File",
            "file_operations.import_e57_file",
            {
                "e57_file_path": e57_file_path,
                "save_converted_file": save_converted_file,
                "use_square_root_of_intensity": use_square_root_of_intensity,
                "automatically_close_converter": automatically_close_converter,
                "prioritize_color_over_intensity": prioritize_color_over_intensity,
                "import_scan_blocks_as_separate_clouds": import_scan_blocks_as_separate_clouds,
                "units": units,
            },
            None,
        )
        return None

    async def import_file_as_embedded_file(
        self,
        external_file_name: FileReference,
        *,
        replace_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportFileAsEmbeddedFile",
            "file_operations.import_file_as_embedded_file",
            {
                "external_file_name": external_file_name,
                "replace_existing": replace_existing,
            },
            None,
        )
        return None

    async def import_file_as_picture(
        self,
        external_file_name: FileReference,
        *,
        replace_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportFileAsPicture",
            "file_operations.import_file_as_picture",
            {
                "external_file_name": external_file_name,
                "replace_existing": replace_existing,
            },
            None,
        )
        return None

    async def import_hidden_point_bar_xml_file(
        self,
        xml_file_path: FileReference,
        *,
        replace_existing_entries: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportHiddenPointBarXmlFile",
            "file_operations.import_hidden_point_bar_xml_file",
            {
                "xml_file_path": xml_file_path,
                "replace_existing_entries": replace_existing_entries,
            },
            None,
        )
        return None

    async def import_iges_file(
        self,
        iges_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportIgesFile",
            "file_operations.import_iges_file",
            {
                "iges_file_path": iges_file_path,
            },
            None,
        )
        return None

    async def import_leica_gsi_file(
        self,
        instrument_id: CollectionInstrumentId,
        group_name: CollectionObjectName,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportLeicaGsiFile",
            "file_operations.import_leica_gsi_file",
            {
                "instrument_id": instrument_id,
                "group_name": group_name,
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_leica_sdb_file(
        self,
        instrument_id: CollectionInstrumentId,
        scan_cloud_name: CollectionObjectName,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportLeicaSdbFile",
            "file_operations.import_leica_sdb_file",
            {
                "instrument_id": instrument_id,
                "scan_cloud_name": scan_cloud_name,
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_mp_file_as_embedded_mp(
        self,
        external_mp_file_name: FileReference,
        *,
        replace_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportMpFileAsEmbeddedMp",
            "file_operations.import_mp_file_as_embedded_mp",
            {
                "external_mp_file_name": external_mp_file_name,
                "replace_existing": replace_existing,
            },
            None,
        )
        return None

    async def import_nominals_from_xml_file(
        self,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportNominalsFromXmlFile",
            "file_operations.import_nominals_from_xml_file",
            {
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_polyworks_file(
        self,
        cloud_name: CollectionObjectName,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportPolyworksFile",
            "file_operations.import_polyworks_file",
            {
                "cloud_name": cloud_name,
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_qdas_catalog_file(
        self,
        qdas_dfd_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportQdasCatalogFile",
            "file_operations.import_qdas_catalog_file",
            {
                "qdas_dfd_file_path": qdas_dfd_file_path,
            },
            None,
        )
        return None

    async def import_sa_file(
        self,
        sa_file_name: FileReference,
        *,
        allow_operator_selections: bool = False,
        selected_collections_optional: Iterable[str],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportSaFile",
            "file_operations.import_sa_file",
            {
                "sa_file_name": sa_file_name,
                "allow_operator_selections": allow_operator_selections,
                "selected_collections_optional": selected_collections_optional,
            },
            None,
        )
        return None

    async def import_sa_windows_placement(
        self,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportSaWindowsPlacement",
            "file_operations.import_sa_windows_placement",
            {
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_sat_file(
        self,
        sat_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportSatFile",
            "file_operations.import_sat_file",
            {
                "sat_file_path": sat_file_path,
            },
            None,
        )
        return None

    async def import_step_file(
        self,
        step_file_path: FileReference,
        *,
        display_entity_filters: bool = False,
        display_residuals: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportStepFile",
            "file_operations.import_step_file",
            {
                "step_file_path": step_file_path,
                "display_entity_filters": display_entity_filters,
                "display_residuals": display_residuals,
            },
            None,
        )
        return None

    async def import_stl_file(
        self,
        stl_file_path: FileReference,
        *,
        units: DistanceUnits = DistanceUnits.MILLIMETERS,
        import_mesh: bool = True,
        import_point_cloud: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportStlFile",
            "file_operations.import_stl_file",
            {
                "stl_file_path": stl_file_path,
                "units": units,
                "import_mesh": import_mesh,
                "import_point_cloud": import_point_cloud,
            },
            None,
        )
        return None

    async def import_vda_fs_file(
        self,
        vda_fs_file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportVdaFsFile",
            "file_operations.import_vda_fs_file",
            {
                "vda_fs_file_path": vda_fs_file_path,
            },
            None,
        )
        return None

    async def import_vstars_xyz_file(
        self,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportVstarsXyzFile",
            "file_operations.import_vstars_xyz_file",
            {
                "file_path": file_path,
            },
            None,
        )
        return None

    async def import_vstars_cameras(
        self,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "ImportVstarsCameras",
            "file_operations.import_vstars_cameras",
            {
                "file_path": file_path,
            },
            None,
        )
        return None

    async def load_html_form(
        self,
        input_html_form_path: FileReference,
        *,
        window_width: int = 1000,
        window_height: int = 800,
        input_data_share_file_path: FileReference,
        output_data_share_file_path: FileReference,
        save_in_binary_format: bool = False,
        save_button_text: str = "Save",
        cancel_button_text: str = "Cancel",
        hide_save_and_cancel_buttons: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "LoadHtmlForm",
            "file_operations.load_html_form",
            {
                "input_html_form_path": input_html_form_path,
                "window_width": window_width,
                "window_height": window_height,
                "input_data_share_file_path": input_data_share_file_path,
                "output_data_share_file_path": output_data_share_file_path,
                "save_in_binary_format": save_in_binary_format,
                "save_button_text": save_button_text,
                "cancel_button_text": cancel_button_text,
                "hide_save_and_cancel_buttons": hide_save_and_cancel_buttons,
            },
            None,
        )
        return None

    async def load_html_form_in_edge_browser(
        self,
        input_html_form_path: FileReference,
        *,
        window_width: int = 1000,
        window_height: int = 800,
        input_data_share_file_path: FileReference,
        output_data_share_file_path: FileReference,
        save_in_binary_format: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "LoadHtmlFormInEdgeBrowser",
            "file_operations.load_html_form_in_edge_browser",
            {
                "input_html_form_path": input_html_form_path,
                "window_width": window_width,
                "window_height": window_height,
                "input_data_share_file_path": input_data_share_file_path,
                "output_data_share_file_path": output_data_share_file_path,
                "save_in_binary_format": save_in_binary_format,
            },
            None,
        )
        return None

    async def make_embedded_file_name_list(
        self,
        *,
        collection_wildcard_criteria: str = "*",
        file_name_pattern: str = "*.*",
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.FileOperations",
                "MakeEmbeddedFileNameList",
                "file_operations.make_embedded_file_name_list",
                {
                    "collection_wildcard_criteria": collection_wildcard_criteria,
                    "file_name_pattern": file_name_pattern,
                },
                None,
            ),
        )

    async def merge_measurements_into_xml_file(
        self,
        file_path: FileReference,
        group_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "MergeMeasurementsIntoXmlFile",
            "file_operations.merge_measurements_into_xml_file",
            {
                "file_path": file_path,
                "group_name": group_name,
            },
            None,
        )
        return None

    async def new_sa_file(self) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "NewSaFile",
            "file_operations.new_sa_file",
            {},
            None,
        )
        return None

    async def open_sa_file(
        self,
        sa_file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "OpenSaFile",
            "file_operations.open_sa_file",
            {
                "sa_file_name": sa_file_name,
            },
            None,
        )
        return None

    async def open_template_file(
        self,
        template_file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "OpenTemplateFile",
            "file_operations.open_template_file",
            {
                "template_file_name": template_file_name,
            },
            None,
        )
        return None

    async def pop_poly_bay_analysis_window(
        self,
        *,
        materials_file_path: str = "",
        bay_file_path: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "PopPolyBayAnalysisWindow",
            "file_operations.pop_poly_bay_analysis_window",
            {
                "materials_file_path": materials_file_path,
                "bay_file_path": bay_file_path,
            },
            None,
        )
        return None

    async def prepare_qdas_data_list(
        self,
        *,
        k1001_part_number: str = "",
        k1002_part_description: str = "",
        k1071_supplier_number: str = "",
        k1072_supplier_description: str = "",
        k1203_reason_for_test: str = "",
        k1303_plant: str = "",
        k1900_part_remark: str = "",
        k0006_batch_number: str = "",
        k0014_part_id: str = "",
        k0053_order_number: str = "",
        k0004_date_time_stamp: str = "2026-07-20/16:32:22",
        k0008_operator_identifier: int = -1,
        k0010_machine_identifier: int = -1,
        k0012_gage_identifier: int = -1,
        relationship_list: Iterable[CollectionItemName],
        feature_check_list: Iterable[CollectionItemName],
        vector_group_list: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "PrepareQdasDataList",
            "file_operations.prepare_qdas_data_list",
            {
                "k1001_part_number": k1001_part_number,
                "k1002_part_description": k1002_part_description,
                "k1071_supplier_number": k1071_supplier_number,
                "k1072_supplier_description": k1072_supplier_description,
                "k1203_reason_for_test": k1203_reason_for_test,
                "k1303_plant": k1303_plant,
                "k1900_part_remark": k1900_part_remark,
                "k0006_batch_number": k0006_batch_number,
                "k0014_part_id": k0014_part_id,
                "k0053_order_number": k0053_order_number,
                "k0004_date_time_stamp": k0004_date_time_stamp,
                "k0008_operator_identifier": k0008_operator_identifier,
                "k0010_machine_identifier": k0010_machine_identifier,
                "k0012_gage_identifier": k0012_gage_identifier,
                "relationship_list": relationship_list,
                "feature_check_list": feature_check_list,
                "vector_group_list": vector_group_list,
            },
            None,
        )
        return None

    async def rename_general_file(
        self,
        source_file_name: FileReference,
        destination_file_name: FileReference,
        *,
        overwrite: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "RenameGeneralFile",
            "file_operations.rename_general_file",
            {
                "source_file_name": source_file_name,
                "destination_file_name": destination_file_name,
                "overwrite": overwrite,
            },
            None,
        )
        return None

    async def save(self) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "Save",
            "file_operations.save",
            {},
            None,
        )
        return None

    async def save_as_read_only_template(
        self,
        template_file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SaveAsReadOnlyTemplate",
            "file_operations.save_as_read_only_template",
            {
                "template_file_name": template_file_name,
            },
            None,
        )
        return None

    async def save_as(
        self,
        file_name: FileReference,
        *,
        add_serial_number: bool = False,
        optional_number: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SaveAs",
            "file_operations.save_as",
            {
                "file_name": file_name,
                "add_serial_number": add_serial_number,
                "optional_number": optional_number,
            },
            None,
        )
        return None

    async def set_boolean_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        boolean_name: str = "",
        boolean_value: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetBooleanInDataShareFile",
            "file_operations.set_boolean_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "boolean_name": boolean_name,
                "boolean_value": boolean_value,
            },
            None,
        )
        return None

    async def set_double_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        double_name: str = "",
        double_value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetDoubleInDataShareFile",
            "file_operations.set_double_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "double_name": double_name,
                "double_value": double_value,
            },
            None,
        )
        return None

    async def set_integer_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        integer_name: str = "",
        integer_value: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetIntegerInDataShareFile",
            "file_operations.set_integer_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "integer_name": integer_name,
                "integer_value": integer_value,
            },
            None,
        )
        return None

    async def set_string_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        string_name: str = "",
        string_value: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetStringInDataShareFile",
            "file_operations.set_string_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "string_name": string_name,
                "string_value": string_value,
            },
            None,
        )
        return None

    async def set_transform_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        transform_name: str = "",
        transform_value: Transform,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetTransformInDataShareFile",
            "file_operations.set_transform_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "transform_name": transform_name,
                "transform_value": transform_value,
            },
            None,
        )
        return None

    async def set_vector_in_data_share_file(
        self,
        data_share_file_path: FileReference,
        *,
        vector_name: str = "",
        vector_value: Vector,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "SetVectorInDataShareFile",
            "file_operations.set_vector_in_data_share_file",
            {
                "data_share_file_path": data_share_file_path,
                "vector_name": vector_name,
                "vector_value": vector_value,
            },
            None,
        )
        return None

    async def terminate_all_running_mps(self) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "TerminateAllRunningMPs",
            "file_operations.terminate_all_running_mps",
            {},
            None,
        )
        return None

    async def use_nrkxml_library(
        self,
        *,
        use_library: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "UseNrkxmlLibrary",
            "file_operations.use_nrkxml_library",
            {
                "use_library": use_library,
            },
            None,
        )
        return None

    async def verify_general_file_exists(
        self,
        file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "VerifyGeneralFileExists",
            "file_operations.verify_general_file_exists",
            {
                "file_name": file_name,
            },
            None,
        )
        return None

    async def verify_mp_file_exists(
        self,
        mp_file_name: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.FileOperations",
            "VerifyMpFileExists",
            "file_operations.verify_mp_file_exists",
            {
                "mp_file_name": mp_file_name,
            },
            None,
        )
        return None

    async def run_subroutine(
        self,
        mp_subroutine_file_path: FileReference,
        *,
        share_parent_variables: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpSubroutines",
            "RunSubroutine",
            "mp_subroutines.run_subroutine",
            {
                "mp_subroutine_file_path": mp_subroutine_file_path,
                "share_parent_variables": share_parent_variables,
            },
            None,
        )
        return None

    async def add_task_overview_item(
        self,
        *,
        task_name: str = "",
        comment_text: str = "",
        effort_index: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "AddTaskOverviewItem",
            "mp_task_overview.add_task_overview_item",
            {
                "task_name": task_name,
                "comment_text": comment_text,
                "effort_index": effort_index,
            },
            None,
        )
        return None

    async def create_clear_task_overview_list(
        self,
        *,
        task_name_font: Font = Font.DEFAULT,
        task_comment_font: Font = Font.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "CreateClearTaskOverviewList",
            "mp_task_overview.create_clear_task_overview_list",
            {
                "task_name_font": task_name_font,
                "task_comment_font": task_comment_font,
            },
            None,
        )
        return None

    async def set_current_task(
        self,
        *,
        task_index: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetCurrentTask",
            "mp_task_overview.set_current_task",
            {
                "task_index": task_index,
            },
            None,
        )
        return None

    async def set_overview_image(
        self,
        image_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetOverviewImage",
            "mp_task_overview.set_overview_image",
            {
                "image_path": image_path,
            },
            None,
        )
        return None

    async def set_overview_title(
        self,
        *,
        overview_title: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetOverviewTitle",
            "mp_task_overview.set_overview_title",
            {
                "overview_title": overview_title,
            },
            None,
        )
        return None

    async def set_task_item_comment(
        self,
        *,
        task_index: int = 0,
        task_comment: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetTaskItemComment",
            "mp_task_overview.set_task_item_comment",
            {
                "task_index": task_index,
                "task_comment": task_comment,
            },
            None,
        )
        return None

    async def set_task_item_completion_values(
        self,
        *,
        task_index: int = 0,
        increments_completed: int = 0,
        total_increments: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetTaskItemCompletionValues",
            "mp_task_overview.set_task_item_completion_values",
            {
                "task_index": task_index,
                "increments_completed": increments_completed,
                "total_increments": total_increments,
            },
            None,
        )
        return None

    async def set_task_item_name(
        self,
        *,
        task_item_index: int = 0,
        task_name: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "SetTaskItemName",
            "mp_task_overview.set_task_item_name",
            {
                "task_item_index": task_item_index,
                "task_name": task_name,
            },
            None,
        )
        return None

    async def show_progress_for_task_item(
        self,
        *,
        task_index: int = 0,
        show_progress: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "ShowProgressForTaskItem",
            "mp_task_overview.show_progress_for_task_item",
            {
                "task_index": task_index,
                "show_progress": show_progress,
            },
            None,
        )
        return None

    async def show_task_overview_list(
        self,
        *,
        show: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.MpTaskOverview",
            "ShowTaskOverviewList",
            "mp_task_overview.show_task_overview_list",
            {
                "show": show,
            },
            None,
        )
        return None

    async def ask_for_double(
        self,
        *,
        question_to_ask: str = "",
        initial_value: float = 0.000000,
        enforce_min_max_values: bool = False,
        min_value: float = 0.000000,
        max_value: float = 0.000000,
        font: Font = Font.DEFAULT,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForDouble",
                "process_flow_operations.ask_for_double",
                {
                    "question_to_ask": question_to_ask,
                    "initial_value": initial_value,
                    "enforce_min_max_values": enforce_min_max_values,
                    "min_value": min_value,
                    "max_value": max_value,
                    "font": font,
                },
                None,
            ),
        )

    async def ask_for_integer(
        self,
        *,
        question_to_ask: str = "",
        initial_value: int = 0,
        enforce_min_max_values: bool = False,
        min_value: int = 0,
        max_value: int = 0,
        font: Font = Font.DEFAULT,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForInteger",
                "process_flow_operations.ask_for_integer",
                {
                    "question_to_ask": question_to_ask,
                    "initial_value": initial_value,
                    "enforce_min_max_values": enforce_min_max_values,
                    "min_value": min_value,
                    "max_value": max_value,
                    "font": font,
                },
                None,
            ),
        )

    async def ask_for_point_name(
        self,
        *,
        question_to_ask: str = "",
        initial_value: PointName,
        font: Font = Font.DEFAULT,
    ) -> PointName:
        return cast(
            PointName,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForPointName",
                "process_flow_operations.ask_for_point_name",
                {
                    "question_to_ask": question_to_ask,
                    "initial_value": initial_value,
                    "font": font,
                },
                None,
            ),
        )

    async def ask_for_string(
        self,
        *,
        question_to_ask: str = "",
        password_entry: bool = False,
        initial_answer: str = "",
        font: Font = Font.DEFAULT,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForString",
                "process_flow_operations.ask_for_string",
                {
                    "question_to_ask": question_to_ask,
                    "password_entry": password_entry,
                    "initial_answer": initial_answer,
                    "font": font,
                },
                None,
            ),
        )

    async def ask_for_string_pull_down_version(
        self,
        question_or_statement: Iterable[str],
        possible_answers: Iterable[str],
        *,
        font: Font = Font.DEFAULT,
    ) -> AskForStringPullDownVersionResult:
        return cast(
            AskForStringPullDownVersionResult,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForStringPullDownVersion",
                "process_flow_operations.ask_for_string_pull_down_version",
                {
                    "question_or_statement": question_or_statement,
                    "possible_answers": possible_answers,
                    "font": font,
                },
                AskForStringPullDownVersionResult,
            ),
        )

    async def ask_for_user_decision_from_image(
        self,
        image_file: FileReference,
        image_map_xml_file: FileReference,
        *,
        window_caption: str = "",
        window_width_0_default: int = 0,
        window_height_0_default: int = 0,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForUserDecisionFromImage",
                "process_flow_operations.ask_for_user_decision_from_image",
                {
                    "image_file": image_file,
                    "image_map_xml_file": image_map_xml_file,
                    "window_caption": window_caption,
                    "window_width_0_default": window_width_0_default,
                    "window_height_0_default": window_height_0_default,
                },
                None,
            ),
        )

    async def ask_for_user_decision_from_strings(
        self,
        question_or_statement: Iterable[str],
        *,
        font: Font = Font.DEFAULT,
        button1_text_empty_to_hide_button: str = "",
        button2_text_empty_to_hide_button: str = "",
        button3_text_empty_to_hide_button: str = "",
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "AskForUserDecisionFromStrings",
                "process_flow_operations.ask_for_user_decision_from_strings",
                {
                    "question_or_statement": question_or_statement,
                    "font": font,
                    "button1_text_empty_to_hide_button": button1_text_empty_to_hide_button,
                    "button2_text_empty_to_hide_button": button2_text_empty_to_hide_button,
                    "button3_text_empty_to_hide_button": button3_text_empty_to_hide_button,
                },
                None,
            ),
        )

    async def object_existence_test_check_only(
        self,
        object_name: CollectionObjectName,
    ) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.ProcessFlowOperations",
                "ObjectExistenceTestCheckOnly",
                "process_flow_operations.object_existence_test_check_only",
                {
                    "object_name": object_name,
                },
                None,
            ),
        )

    async def enable_disable_relationships_for_optimization(
        self,
        relationships: Iterable[CollectionItemName],
        *,
        enable: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "EnableDisableRelationshipsForOptimization",
            "relationship_operations.enable_disable_relationships_for_optimization",
            {
                "relationships": relationships,
                "enable": enable,
            },
            None,
        )
        return None

    async def geom_relationship_ignore_input_points(
        self,
        relationship_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "GeomRelationshipIgnoreInputPoints",
            "relationship_operations.geom_relationship_ignore_input_points",
            {
                "relationship_name": relationship_name,
            },
            None,
        )
        return None

    async def geom_relationship_reuse_ignored_input_points(
        self,
        relationship_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "GeomRelationshipReuseIgnoredInputPoints",
            "relationship_operations.geom_relationship_reuse_ignored_input_points",
            {
                "relationship_name": relationship_name,
            },
            None,
        )
        return None

    async def get_geom_relationship_auto_vectors(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetGeomRelationshipAutoVectorsResult:
        return cast(
            GetGeomRelationshipAutoVectorsResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipAutoVectors",
                "relationship_operations.get_geom_relationship_auto_vectors",
                {
                    "relationship_name": relationship_name,
                },
                GetGeomRelationshipAutoVectorsResult,
            ),
        )

    async def get_geom_relationship_cardinal_points(
        self,
        relationship_name: CollectionObjectName,
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipCardinalPoints",
                "relationship_operations.get_geom_relationship_cardinal_points",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_geom_relationship_criteria(
        self,
        relationship_name: CollectionObjectName,
        *,
        criteria: str = "",
    ) -> GetGeomRelationshipCriteriaResult:
        return cast(
            GetGeomRelationshipCriteriaResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipCriteria",
                "relationship_operations.get_geom_relationship_criteria",
                {
                    "relationship_name": relationship_name,
                    "criteria": criteria,
                },
                GetGeomRelationshipCriteriaResult,
            ),
        )

    async def get_geom_relationship_measured_avg_point(
        self,
        relationship_name: CollectionObjectName,
    ) -> PointName:
        return cast(
            PointName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipMeasuredAvgPoint",
                "relationship_operations.get_geom_relationship_measured_avg_point",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_geom_relationship_measured_geometry(
        self,
        relationship_name: CollectionObjectName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipMeasuredGeometry",
                "relationship_operations.get_geom_relationship_measured_geometry",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_geom_relationship_nominal_avg_point(
        self,
        relationship_name: CollectionObjectName,
    ) -> PointName:
        return cast(
            PointName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipNominalAvgPoint",
                "relationship_operations.get_geom_relationship_nominal_avg_point",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_geom_relationship_nominal_geometry(
        self,
        relationship_name: CollectionObjectName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipNominalGeometry",
                "relationship_operations.get_geom_relationship_nominal_geometry",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_geom_relationship_point_list(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetGeomRelationshipPointListResult:
        return cast(
            GetGeomRelationshipPointListResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipPointList",
                "relationship_operations.get_geom_relationship_point_list",
                {
                    "relationship_name": relationship_name,
                },
                GetGeomRelationshipPointListResult,
            ),
        )

    async def get_geom_relationship_projection_plane(
        self,
        relationship_name: CollectionObjectName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetGeomRelationshipProjectionPlane",
                "relationship_operations.get_geom_relationship_projection_plane",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_pipe_relationship_cut_status(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetPipeRelationshipCutStatusResult:
        return cast(
            GetPipeRelationshipCutStatusResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPipeRelationshipCutStatus",
                "relationship_operations.get_pipe_relationship_cut_status",
                {
                    "relationship_name": relationship_name,
                },
                GetPipeRelationshipCutStatusResult,
            ),
        )

    async def get_pipe_relationship_properties(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetPipeRelationshipPropertiesResult:
        return cast(
            GetPipeRelationshipPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPipeRelationshipProperties",
                "relationship_operations.get_pipe_relationship_properties",
                {
                    "relationship_name": relationship_name,
                },
                GetPipeRelationshipPropertiesResult,
            ),
        )

    async def get_pipe_relationship_weights(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetPipeRelationshipWeightsResult:
        return cast(
            GetPipeRelationshipWeightsResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetPipeRelationshipWeights",
                "relationship_operations.get_pipe_relationship_weights",
                {
                    "relationship_name": relationship_name,
                },
                GetPipeRelationshipWeightsResult,
            ),
        )

    async def get_relationship_fit_constraints_scalar_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipFitConstraintsScalarTypeResult:
        return cast(
            GetRelationshipFitConstraintsScalarTypeResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipFitConstraintsScalarType",
                "relationship_operations.get_relationship_fit_constraints_scalar_type",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipFitConstraintsScalarTypeResult,
            ),
        )

    async def get_relationship_outlier_rejection_scalar_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipOutlierRejectionScalarTypeResult:
        return cast(
            GetRelationshipOutlierRejectionScalarTypeResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipOutlierRejectionScalarType",
                "relationship_operations.get_relationship_outlier_rejection_scalar_type",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipOutlierRejectionScalarTypeResult,
            ),
        )

    async def get_relationship_projection_options(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipProjectionOptionsResult:
        return cast(
            GetRelationshipProjectionOptionsResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipProjectionOptions",
                "relationship_operations.get_relationship_projection_options",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipProjectionOptionsResult,
            ),
        )

    async def get_relationship_reporting_frame(
        self,
        relationship_name: CollectionObjectName,
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipReportingFrame",
                "relationship_operations.get_relationship_reporting_frame",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_relationship_sub_sampling_options(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipSubSamplingOptionsResult:
        return cast(
            GetRelationshipSubSamplingOptionsResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipSubSamplingOptions",
                "relationship_operations.get_relationship_sub_sampling_options",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipSubSamplingOptionsResult,
            ),
        )

    async def get_relationship_tolerance_scalar_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipToleranceScalarTypeResult:
        return cast(
            GetRelationshipToleranceScalarTypeResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipToleranceScalarType",
                "relationship_operations.get_relationship_tolerance_scalar_type",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipToleranceScalarTypeResult,
            ),
        )

    async def get_relationship_tolerance_vector_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> GetRelationshipToleranceVectorTypeResult:
        return cast(
            GetRelationshipToleranceVectorTypeResult,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipToleranceVectorType",
                "relationship_operations.get_relationship_tolerance_vector_type",
                {
                    "relationship_name": relationship_name,
                },
                GetRelationshipToleranceVectorTypeResult,
            ),
        )

    async def get_relationship_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipType",
                "relationship_operations.get_relationship_type",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def get_relationship_weighting(
        self,
        relationship_name: CollectionObjectName,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.RelationshipOperations",
                "GetRelationshipWeighting",
                "relationship_operations.get_relationship_weighting",
                {
                    "relationship_name": relationship_name,
                },
                None,
            ),
        )

    async def make_pipe_fitting_relationship(
        self,
        relationship_name: CollectionObjectName,
        pipe_1_object_name: CollectionObjectName,
        pipe_2_object_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePipeFittingRelationship",
            "relationship_operations.make_pipe_fitting_relationship",
            {
                "relationship_name": relationship_name,
                "pipe_1_object_name": pipe_1_object_name,
                "pipe_2_object_name": pipe_2_object_name,
            },
            None,
        )
        return None

    async def make_pipe_relationship_cut(
        self,
        relationship_name: CollectionObjectName,
        *,
        pipe_1_make_cut: bool = True,
        pipe_1_create_frame: bool = False,
        pipe_1_frame_name: CollectionObjectName,
        pipe_2_make_cut: bool = True,
        pipe_2_create_frame: bool = False,
        pipe_2_frame_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "MakePipeRelationshipCut",
            "relationship_operations.make_pipe_relationship_cut",
            {
                "relationship_name": relationship_name,
                "pipe_1_make_cut": pipe_1_make_cut,
                "pipe_1_create_frame": pipe_1_create_frame,
                "pipe_1_frame_name": pipe_1_frame_name,
                "pipe_2_make_cut": pipe_2_make_cut,
                "pipe_2_create_frame": pipe_2_create_frame,
                "pipe_2_frame_name": pipe_2_frame_name,
            },
            None,
        )
        return None

    async def pipe_relationship_force_cut_to_frame(
        self,
        relationship_name: CollectionObjectName,
        *,
        pipe_1_force_cut_to_frame: bool = True,
        pipe_1_frame_name: CollectionObjectName,
        pipe_2_force_cut_to_frame: bool = True,
        pipe_2_frame_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "PipeRelationshipForceCutToFrame",
            "relationship_operations.pipe_relationship_force_cut_to_frame",
            {
                "relationship_name": relationship_name,
                "pipe_1_force_cut_to_frame": pipe_1_force_cut_to_frame,
                "pipe_1_frame_name": pipe_1_frame_name,
                "pipe_2_force_cut_to_frame": pipe_2_force_cut_to_frame,
                "pipe_2_frame_name": pipe_2_frame_name,
            },
            None,
        )
        return None

    async def set_geom_relationship_auto_measure_nominal_feature(
        self,
        relationship_name: CollectionObjectName,
        *,
        trap_clouds_false_geometry: bool = True,
        instrument_id: CollectionInstrumentId,
        measurement_mode: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipAutoMeasureNominalFeature",
            "relationship_operations.set_geom_relationship_auto_measure_nominal_feature",
            {
                "relationship_name": relationship_name,
                "trap_clouds_false_geometry": trap_clouds_false_geometry,
                "instrument_id": instrument_id,
                "measurement_mode": measurement_mode,
            },
            None,
        )
        return None

    async def set_geom_relationship_auto_vectors_nominal_avn(
        self,
        relationship_name: CollectionObjectName,
        *,
        create_auto_vectors_avn: bool = False,
        points_type: PointFilterInputType = PointFilterInputType.CARDINAL_POINTS,
        use_vector_group_custom_prefix: bool = False,
        vector_group_custom_prefix: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipAutoVectorsNominalAvn",
            "relationship_operations.set_geom_relationship_auto_vectors_nominal_avn",
            {
                "relationship_name": relationship_name,
                "create_auto_vectors_avn": create_auto_vectors_avn,
                "points_type": points_type,
                "use_vector_group_custom_prefix": use_vector_group_custom_prefix,
                "vector_group_custom_prefix": vector_group_custom_prefix,
            },
            None,
        )
        return None

    async def set_geom_relationship_cardinal_points(
        self,
        relationship_name: CollectionObjectName,
        *,
        create_cardinal_pts_when_fitting: bool = True,
        prefix_cardinal_pts_name_with_rel_name: bool = True,
        cardinal_pts_group_name: str = "GR-Cardinal Pts",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipCardinalPoints",
            "relationship_operations.set_geom_relationship_cardinal_points",
            {
                "relationship_name": relationship_name,
                "create_cardinal_pts_when_fitting": create_cardinal_pts_when_fitting,
                "prefix_cardinal_pts_name_with_rel_name": prefix_cardinal_pts_name_with_rel_name,
                "cardinal_pts_group_name": cardinal_pts_group_name,
            },
            None,
        )
        return None

    async def set_geom_relationship_criteria(
        self,
        relationship_name: CollectionObjectName,
        *,
        criteria: str = "",
        show_in_report: bool = True,
        tolerance_options: ToleranceScalarOptions = ToleranceScalarOptions.DEFAULT,
        optimization_delta_weight: float = 0.000000,
        optimization_out_of_tolerance_weight: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipCriteria",
            "relationship_operations.set_geom_relationship_criteria",
            {
                "relationship_name": relationship_name,
                "criteria": criteria,
                "show_in_report": show_in_report,
                "tolerance_options": tolerance_options,
                "optimization_delta_weight": optimization_delta_weight,
                "optimization_out_of_tolerance_weight": optimization_out_of_tolerance_weight,
            },
            None,
        )
        return None

    async def set_geom_relationship_measured_geometry(
        self,
        relationship_name: CollectionObjectName,
        measured_geometry: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipMeasuredGeometry",
            "relationship_operations.set_geom_relationship_measured_geometry",
            {
                "relationship_name": relationship_name,
                "measured_geometry": measured_geometry,
            },
            None,
        )
        return None

    async def set_geom_relationship_nominal_avg_point(
        self,
        relationship_name: CollectionObjectName,
        *,
        compare_to_nominal: bool = True,
        nominal_average_point: PointName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipNominalAvgPoint",
            "relationship_operations.set_geom_relationship_nominal_avg_point",
            {
                "relationship_name": relationship_name,
                "compare_to_nominal": compare_to_nominal,
                "nominal_average_point": nominal_average_point,
            },
            None,
        )
        return None

    async def set_geom_relationship_nominal_geometry(
        self,
        relationship_name: CollectionObjectName,
        *,
        compare_to_nominal: bool = True,
        nominal_geometry: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipNominalGeometry",
            "relationship_operations.set_geom_relationship_nominal_geometry",
            {
                "relationship_name": relationship_name,
                "compare_to_nominal": compare_to_nominal,
                "nominal_geometry": nominal_geometry,
            },
            None,
        )
        return None

    async def set_geom_relationship_projection_plane(
        self,
        relationship_name: CollectionObjectName,
        *,
        project_to_plane: bool = True,
        projection_plane_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetGeomRelationshipProjectionPlane",
            "relationship_operations.set_geom_relationship_projection_plane",
            {
                "relationship_name": relationship_name,
                "project_to_plane": project_to_plane,
                "projection_plane_name": projection_plane_name,
            },
            None,
        )
        return None

    async def set_object_to_object_direction_relationship_fit_constraints(
        self,
        relationship_name: CollectionObjectName,
        *,
        angle_between_vectors_fit_constraints: FitConstraintScalarOptions = FitConstraintScalarOptions.DEFAULT,
        mutual_perpendicular_length_fit_constraints: FitConstraintScalarOptions = FitConstraintScalarOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetObjectToObjectDirectionRelationshipFitConstraints",
            "relationship_operations.set_object_to_object_direction_relationship_fit_constraints",
            {
                "relationship_name": relationship_name,
                "angle_between_vectors_fit_constraints": angle_between_vectors_fit_constraints,
                "mutual_perpendicular_length_fit_constraints": mutual_perpendicular_length_fit_constraints,
            },
            None,
        )
        return None

    async def set_pipe_relationship_segment_properties(
        self,
        relationship_name: CollectionObjectName,
        *,
        pipe_1_inner_diameter: float = 0.000000,
        pipe_1_outer_diameter: float = 0.000000,
        pipe_1_cut_begin: float = 0.000000,
        pipe_1_cut_end: float = 0.000000,
        pipe_2_inner_diameter: float = 0.000000,
        pipe_2_outer_diameter: float = 0.000000,
        pipe_2_cut_begin: float = 0.000000,
        pipe_2_cut_end: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetPipeRelationshipSegmentProperties",
            "relationship_operations.set_pipe_relationship_segment_properties",
            {
                "relationship_name": relationship_name,
                "pipe_1_inner_diameter": pipe_1_inner_diameter,
                "pipe_1_outer_diameter": pipe_1_outer_diameter,
                "pipe_1_cut_begin": pipe_1_cut_begin,
                "pipe_1_cut_end": pipe_1_cut_end,
                "pipe_2_inner_diameter": pipe_2_inner_diameter,
                "pipe_2_outer_diameter": pipe_2_outer_diameter,
                "pipe_2_cut_begin": pipe_2_cut_begin,
                "pipe_2_cut_end": pipe_2_cut_end,
            },
            None,
        )
        return None

    async def set_pipe_relationship_weights(
        self,
        relationship_name: CollectionObjectName,
        *,
        overall_weight: float = 1.000000,
        axis_offset: float = 2.000000,
        axis_alignment: float = 1.000000,
        center_pull: float = 0.100000,
        out_of_material_weight: float = 10.000000,
        out_of_material_offset: float = 1.000000,
        constrain_region_at_od: bool = False,
        constrain_id_od_overlap: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetPipeRelationshipWeights",
            "relationship_operations.set_pipe_relationship_weights",
            {
                "relationship_name": relationship_name,
                "overall_weight": overall_weight,
                "axis_offset": axis_offset,
                "axis_alignment": axis_alignment,
                "center_pull": center_pull,
                "out_of_material_weight": out_of_material_weight,
                "out_of_material_offset": out_of_material_offset,
                "constrain_region_at_od": constrain_region_at_od,
                "constrain_id_od_overlap": constrain_id_od_overlap,
            },
            None,
        )
        return None

    async def set_relationship_auto_vectors_fit_avf(
        self,
        relationship_name: CollectionObjectName,
        *,
        create_auto_vectors_avf: bool = False,
        use_vector_group_custom_prefix: bool = False,
        vector_group_custom_prefix: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipAutoVectorsFitAvf",
            "relationship_operations.set_relationship_auto_vectors_fit_avf",
            {
                "relationship_name": relationship_name,
                "create_auto_vectors_avf": create_auto_vectors_avf,
                "use_vector_group_custom_prefix": use_vector_group_custom_prefix,
                "vector_group_custom_prefix": vector_group_custom_prefix,
            },
            None,
        )
        return None

    async def set_relationship_auto_vectors_group_default_prefix(
        self,
        *,
        geom_rel_avn_vg_default_prefix: str = "GR-AVN-",
        geom_rel_avf_vg_default_prefix: str = "GR-AVF-",
        non_geom_rel_vg_default_prefix: str = "Auto Vectors: ",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipAutoVectorsGroupDefaultPrefix",
            "relationship_operations.set_relationship_auto_vectors_group_default_prefix",
            {
                "geom_rel_avn_vg_default_prefix": geom_rel_avn_vg_default_prefix,
                "geom_rel_avf_vg_default_prefix": geom_rel_avf_vg_default_prefix,
                "non_geom_rel_vg_default_prefix": non_geom_rel_vg_default_prefix,
            },
            None,
        )
        return None

    async def set_relationship_desired_meas_count(
        self,
        relationship_name: CollectionObjectName,
        *,
        desired_measurement_count: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipDesiredMeasCount",
            "relationship_operations.set_relationship_desired_meas_count",
            {
                "relationship_name": relationship_name,
                "desired_measurement_count": desired_measurement_count,
            },
            None,
        )
        return None

    async def set_relationship_dormant_status(
        self,
        relationships: Iterable[CollectionItemName],
        *,
        dormant_status: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipDormantStatus",
            "relationship_operations.set_relationship_dormant_status",
            {
                "relationships": relationships,
                "dormant_status": dormant_status,
            },
            None,
        )
        return None

    async def set_relationship_fit_constraints_scalar_type(
        self,
        relationship_name: CollectionObjectName,
        *,
        fit_constraint_options: FitConstraintScalarOptions = FitConstraintScalarOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipFitConstraintsScalarType",
            "relationship_operations.set_relationship_fit_constraints_scalar_type",
            {
                "relationship_name": relationship_name,
                "fit_constraint_options": fit_constraint_options,
            },
            None,
        )
        return None

    async def set_relationship_orientation_fit_constraints_vector_type(
        self,
        relationship_name: CollectionObjectName,
        orientation_vector_constraint: ToleranceVectorOptions,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipOrientationFitConstraintsVectorType",
            "relationship_operations.set_relationship_orientation_fit_constraints_vector_type",
            {
                "relationship_name": relationship_name,
                "orientation_vector_constraint": orientation_vector_constraint,
            },
            None,
        )
        return None

    async def set_relationship_outlier_rejection_scalar_type(
        self,
        relationship_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipOutlierRejectionScalarType",
            "relationship_operations.set_relationship_outlier_rejection_scalar_type",
            {
                "relationship_name": relationship_name,
            },
            None,
        )
        return None

    async def set_relationship_position_fit_constraints_vector_type(
        self,
        relationship_name: CollectionObjectName,
        position_vector_constraint: ToleranceVectorOptions,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipPositionFitConstraintsVectorType",
            "relationship_operations.set_relationship_position_fit_constraints_vector_type",
            {
                "relationship_name": relationship_name,
                "position_vector_constraint": position_vector_constraint,
            },
            None,
        )
        return None

    async def set_relationship_projection_options(
        self,
        relationship_name: CollectionObjectName,
        *,
        projection_options: ProjectionOptions = ProjectionOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipProjectionOptions",
            "relationship_operations.set_relationship_projection_options",
            {
                "relationship_name": relationship_name,
                "projection_options": projection_options,
            },
            None,
        )
        return None

    async def set_relationship_reporting_frame(
        self,
        relationship_name: CollectionObjectName,
        reporting_frame: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipReportingFrame",
            "relationship_operations.set_relationship_reporting_frame",
            {
                "relationship_name": relationship_name,
                "reporting_frame": reporting_frame,
            },
            None,
        )
        return None

    async def set_relationship_sigmoidal_gap_fit_constraints(
        self,
        relationship_name: CollectionObjectName,
        *,
        use_sigmoidal_gap_constraints: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipSigmoidalGapFitConstraints",
            "relationship_operations.set_relationship_sigmoidal_gap_fit_constraints",
            {
                "relationship_name": relationship_name,
                "use_sigmoidal_gap_constraints": use_sigmoidal_gap_constraints,
            },
            None,
        )
        return None

    async def set_relationship_sub_sampling_options(
        self,
        relationship_name: CollectionObjectName,
        *,
        use_every_ith_point: bool = False,
        i_value: int = 20,
        use_no_more_than_n_points: bool = True,
        n_value: int = 10000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipSubSamplingOptions",
            "relationship_operations.set_relationship_sub_sampling_options",
            {
                "relationship_name": relationship_name,
                "use_every_ith_point": use_every_ith_point,
                "i_value": i_value,
                "use_no_more_than_n_points": use_no_more_than_n_points,
                "n_value": n_value,
            },
            None,
        )
        return None

    async def set_relationship_tolerance_scalar_type(
        self,
        relationship_name: CollectionObjectName,
        *,
        tolerance_options: ToleranceScalarOptions = ToleranceScalarOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipToleranceScalarType",
            "relationship_operations.set_relationship_tolerance_scalar_type",
            {
                "relationship_name": relationship_name,
                "tolerance_options": tolerance_options,
            },
            None,
        )
        return None

    async def set_relationship_tolerance_vector_type(
        self,
        relationship_name: CollectionObjectName,
        vector_tolerance: ToleranceVectorOptions,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipToleranceVectorType",
            "relationship_operations.set_relationship_tolerance_vector_type",
            {
                "relationship_name": relationship_name,
                "vector_tolerance": vector_tolerance,
            },
            None,
        )
        return None

    async def set_relationship_voxel_cloud_display(
        self,
        relationship_name: CollectionObjectName,
        *,
        enable_voxel_cloud_display: bool = True,
        voxel_size_1_0_autodetect: float = -1.000000,
        min_pts_count_per_voxel: int = 3,
        voxel_rendering_diameter_1_0_fast: float = 125.000000,
        surface_analysis_mode: SurfaceAnalysisMode = SurfaceAnalysisMode.RELATIONSHIP,
        colorization_options: ColorizationOptions = ColorizationOptions.DEFAULT,
        show_color_bar_in_view: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipVoxelCloudDisplay",
            "relationship_operations.set_relationship_voxel_cloud_display",
            {
                "relationship_name": relationship_name,
                "enable_voxel_cloud_display": enable_voxel_cloud_display,
                "voxel_size_1_0_autodetect": voxel_size_1_0_autodetect,
                "min_pts_count_per_voxel": min_pts_count_per_voxel,
                "voxel_rendering_diameter_1_0_fast": voxel_rendering_diameter_1_0_fast,
                "surface_analysis_mode": surface_analysis_mode,
                "colorization_options": colorization_options,
                "show_color_bar_in_view": show_color_bar_in_view,
            },
            None,
        )
        return None

    async def set_relationship_weighting(
        self,
        relationship_name: CollectionObjectName,
        *,
        weight: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipWeighting",
            "relationship_operations.set_relationship_weighting",
            {
                "relationship_name": relationship_name,
                "weight": weight,
            },
            None,
        )
        return None

    async def set_relationship_weights_normalized(
        self,
        collection_name: CollectionName,
        *,
        pick_weighting_mode: RelWeightingMode = RelWeightingMode.NORMALIZE_EQUATION_COUNT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.RelationshipOperations",
            "SetRelationshipWeightsNormalized",
            "relationship_operations.set_relationship_weights_normalized",
            {
                "collection_name": collection_name,
                "pick_weighting_mode": pick_weighting_mode,
            },
            None,
        )
        return None

    async def add_charts_to_report_bar(
        self,
        charts: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddChartsToReportBar",
            "reporting_operations.add_charts_to_report_bar",
            {
                "charts": charts,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_custom_table_to_sa_report(
        self,
        table_name: CollectionObjectName,
        report_name: CollectionObjectName,
        *,
        show_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddCustomTableToSaReport",
            "reporting_operations.add_custom_table_to_sa_report",
            {
                "table_name": table_name,
                "report_name": report_name,
                "show_report": show_report,
            },
            None,
        )
        return None

    async def add_custom_tables_to_report_bar(
        self,
        custom_tables_to_report: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddCustomTablesToReportBar",
            "reporting_operations.add_custom_tables_to_report_bar",
            {
                "custom_tables_to_report": custom_tables_to_report,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_datums_to_report_bar(
        self,
        datums: Iterable[CollectionObjectName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddDatumsToReportBar",
            "reporting_operations.add_datums_to_report_bar",
            {
                "datums": datums,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_events_to_report_bar(
        self,
        events: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddEventsToReportBar",
            "reporting_operations.add_events_to_report_bar",
            {
                "events": events,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_feature_checks_to_report_bar(
        self,
        feature_checks: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddFeatureChecksToReportBar",
            "reporting_operations.add_feature_checks_to_report_bar",
            {
                "feature_checks": feature_checks,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_item_to_sa_report_at_location(
        self,
        report_name: CollectionObjectName,
        item_name: CollectionObjectName,
        *,
        page_number: int = 0,
        horizontal_location: float = 1.000000,
        vertical_location: float = 1.000000,
        show_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddItemToSaReportAtLocation",
            "reporting_operations.add_item_to_sa_report_at_location",
            {
                "report_name": report_name,
                "item_name": item_name,
                "page_number": page_number,
                "horizontal_location": horizontal_location,
                "vertical_location": vertical_location,
                "show_report": show_report,
            },
            None,
        )
        return None

    async def add_objects_to_report_bar(
        self,
        objects: Iterable[CollectionObjectName],
        *,
        clear_existing: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddObjectsToReportBar",
            "reporting_operations.add_objects_to_report_bar",
            {
                "objects": objects,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_pictures_to_report_bar(
        self,
        pictures: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddPicturesToReportBar",
            "reporting_operations.add_pictures_to_report_bar",
            {
                "pictures": pictures,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def add_relationships_to_report_bar(
        self,
        relationships: Iterable[CollectionItemName],
        *,
        clear_existing: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AddRelationshipsToReportBar",
            "reporting_operations.add_relationships_to_report_bar",
            {
                "relationships": relationships,
                "clear_existing": clear_existing,
            },
            None,
        )
        return None

    async def append_items_to_sa_report(
        self,
        report_name: CollectionObjectName,
        items_to_report: Iterable[CollectionObjectName],
        *,
        show_report: bool = False,
        begin_on_new_page: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "AppendItemsToSaReport",
            "reporting_operations.append_items_to_sa_report",
            {
                "report_name": report_name,
                "items_to_report": items_to_report,
                "show_report": show_report,
                "begin_on_new_page": begin_on_new_page,
            },
            None,
        )
        return None

    async def capture_current_view(
        self,
        picture_name: CollectionItemName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CaptureCurrentView",
            "reporting_operations.capture_current_view",
            {
                "picture_name": picture_name,
            },
            None,
        )
        return None

    async def capture_screen_to_file_bmp_jpg_png_gif_tiff(
        self,
        file_to_save_to: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CaptureScreenToFileBmpJpgPngGifTiff",
            "reporting_operations.capture_screen_to_file_bmp_jpg_png_gif_tiff",
            {
                "file_to_save_to": file_to_save_to,
            },
            None,
        )
        return None

    async def clear_custom_table(
        self,
        table_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "ClearCustomTable",
            "reporting_operations.clear_custom_table",
            {
                "table_name": table_name,
            },
            None,
        )
        return None

    async def close_all_reports(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CloseAllReports",
            "reporting_operations.close_all_reports",
            {},
            None,
        )
        return None

    async def close_html_display_board(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CloseHtmlDisplayBoard",
            "reporting_operations.close_html_display_board",
            {},
            None,
        )
        return None

    async def combine_sa_reports(
        self,
        sa_reports_to_combine: Iterable[CollectionItemName],
        output_sa_report_name: CollectionObjectName,
        *,
        show_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CombineSaReports",
            "reporting_operations.combine_sa_reports",
            {
                "sa_reports_to_combine": sa_reports_to_combine,
                "output_sa_report_name": output_sa_report_name,
                "show_report": show_report,
            },
            None,
        )
        return None

    async def create_chart_from_vector_group(
        self,
        new_chart_name: ChartName,
        vector_group_name: CollectionObjectName,
        chart_type: ChartType,
        data_set_to_chart: DatasetType,
        aux_data_set_to_chart: DatasetType,
        template_chart_name_optional: ChartName,
        *,
        show_interface: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "CreateChartFromVectorGroup",
            "reporting_operations.create_chart_from_vector_group",
            {
                "new_chart_name": new_chart_name,
                "vector_group_name": vector_group_name,
                "chart_type": chart_type,
                "data_set_to_chart": data_set_to_chart,
                "aux_data_set_to_chart": aux_data_set_to_chart,
                "template_chart_name_optional": template_chart_name_optional,
                "show_interface": show_interface,
            },
            None,
        )
        return None

    async def define_report_template(
        self,
        report_template_name: CollectionObjectName,
        title: Iterable[str],
        graphical_view_options: ReportViewOptions,
        items_to_report: Iterable[CollectionObjectName],
        relationships_to_report: Iterable[CollectionItemName],
        events_to_report: Iterable[CollectionItemName],
        *,
        report_output_options: ReportOutputOptions = ReportOutputOptions.DEFAULT,
        report_page_settings_sa_report_only: ReportPageSettings = ReportPageSettings.PORTRAIT,
        generate_now: bool = False,
        show_generated_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DefineReportTemplate",
            "reporting_operations.define_report_template",
            {
                "report_template_name": report_template_name,
                "title": title,
                "graphical_view_options": graphical_view_options,
                "items_to_report": items_to_report,
                "relationships_to_report": relationships_to_report,
                "events_to_report": events_to_report,
                "report_output_options": report_output_options,
                "report_page_settings_sa_report_only": report_page_settings_sa_report_only,
                "generate_now": generate_now,
                "show_generated_report": show_generated_report,
            },
            None,
        )
        return None

    async def delete_chart(
        self,
        chart_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeleteChart",
            "reporting_operations.delete_chart",
            {
                "chart_name": chart_name,
            },
            None,
        )
        return None

    async def delete_custom_table(
        self,
        table_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeleteCustomTable",
            "reporting_operations.delete_custom_table",
            {
                "table_name": table_name,
            },
            None,
        )
        return None

    async def delete_picture(
        self,
        picture_name: CollectionItemName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeletePicture",
            "reporting_operations.delete_picture",
            {
                "picture_name": picture_name,
            },
            None,
        )
        return None

    async def delete_sa_doc(
        self,
        doc_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeleteSaDoc",
            "reporting_operations.delete_sa_doc",
            {
                "doc_name": doc_name,
            },
            None,
        )
        return None

    async def delete_sa_report(
        self,
        report_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeleteSaReport",
            "reporting_operations.delete_sa_report",
            {
                "report_name": report_name,
            },
            None,
        )
        return None

    async def delete_sa_report_template(
        self,
        report_template_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "DeleteSaReportTemplate",
            "reporting_operations.delete_sa_report_template",
            {
                "report_template_name": report_template_name,
            },
            None,
        )
        return None

    async def generate_quick_report_from_tab_order(
        self,
        *,
        report_output_options: ReportOutputOptions = ReportOutputOptions.DEFAULT,
        open_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "GenerateQuickReportFromTabOrder",
            "reporting_operations.generate_quick_report_from_tab_order",
            {
                "report_output_options": report_output_options,
                "open_report": open_report,
            },
            None,
        )
        return None

    async def generate_standard_html_report(
        self,
        html_output_file: FileReference,
        *,
        decimal_precision: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "GenerateStandardHtmlReport",
            "reporting_operations.generate_standard_html_report",
            {
                "html_output_file": html_output_file,
                "decimal_precision": decimal_precision,
            },
            None,
        )
        return None

    async def generate_update_templated_report(
        self,
        report_template: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "GenerateUpdateTemplatedReport",
            "reporting_operations.generate_update_templated_report",
            {
                "report_template": report_template,
            },
            None,
        )
        return None

    async def get_custom_table_cell_double(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.ReportingOperations",
                "GetCustomTableCellDouble",
                "reporting_operations.get_custom_table_cell_double",
                {
                    "table_name": table_name,
                    "row": row,
                    "column": column,
                },
                None,
            ),
        )

    async def get_custom_table_cell_string(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.ReportingOperations",
                "GetCustomTableCellString",
                "reporting_operations.get_custom_table_cell_string",
                {
                    "table_name": table_name,
                    "row": row,
                    "column": column,
                },
                None,
            ),
        )

    async def get_defined_report_tags(self) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.ReportingOperations",
                "GetDefinedReportTags",
                "reporting_operations.get_defined_report_tags",
                {},
                None,
            ),
        )

    async def get_report_tag_value(
        self,
        *,
        tag_name: str = "",
    ) -> GetReportTagValueResult:
        return cast(
            GetReportTagValueResult,
            await self._invoke_mp_operation(
                "briosa.ReportingOperations",
                "GetReportTagValue",
                "reporting_operations.get_report_tag_value",
                {
                    "tag_name": tag_name,
                },
                GetReportTagValueResult,
            ),
        )

    async def html_display_board(
        self,
        input_html_file: FileReference,
        *,
        show_board: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "HtmlDisplayBoard",
            "reporting_operations.html_display_board",
            {
                "input_html_file": input_html_file,
                "show_board": show_board,
            },
            None,
        )
        return None

    async def make_custom_table(
        self,
        table_name: CollectionObjectName,
        *,
        decimal_precision: int = 6,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "MakeCustomTable",
            "reporting_operations.make_custom_table",
            {
                "table_name": table_name,
                "decimal_precision": decimal_precision,
            },
            None,
        )
        return None

    async def make_new_sa_report(
        self,
        new_sa_report_name: CollectionObjectName,
        sa_report_template_optional: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "MakeNewSaReport",
            "reporting_operations.make_new_sa_report",
            {
                "new_sa_report_name": new_sa_report_name,
                "sa_report_template_optional": sa_report_template_optional,
            },
            None,
        )
        return None

    async def make_utility_chart(
        self,
        ascii_file_path: FileReference,
        *,
        chart_title_override: str = "",
        output_picture_name: CollectionItemName,
        show_chart_dialog: bool = False,
        plot_additional_xy_value: bool = False,
        x_value: float = 0.000000,
        y_value: float = 0.000000,
    ) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.ReportingOperations",
                "MakeUtilityChart",
                "reporting_operations.make_utility_chart",
                {
                    "ascii_file_path": ascii_file_path,
                    "chart_title_override": chart_title_override,
                    "output_picture_name": output_picture_name,
                    "show_chart_dialog": show_chart_dialog,
                    "plot_additional_xy_value": plot_additional_xy_value,
                    "x_value": x_value,
                    "y_value": y_value,
                },
                None,
            ),
        )

    async def notify_user_double(
        self,
        *,
        leading_text: str = "",
        font: Font = Font.DEFAULT,
        reported_value: float = 0.000000,
        decimal_precision: int = 0,
        display_timeout: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "NotifyUserDouble",
            "reporting_operations.notify_user_double",
            {
                "leading_text": leading_text,
                "font": font,
                "reported_value": reported_value,
                "decimal_precision": decimal_precision,
                "display_timeout": display_timeout,
            },
            None,
        )
        return None

    async def notify_user_html(
        self,
        html_file: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "NotifyUserHtml",
            "reporting_operations.notify_user_html",
            {
                "html_file": html_file,
            },
            None,
        )
        return None

    async def notify_user_integer(
        self,
        *,
        leading_text: str = "",
        font: Font = Font.DEFAULT,
        reported_value: int = 0,
        display_timeout: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "NotifyUserInteger",
            "reporting_operations.notify_user_integer",
            {
                "leading_text": leading_text,
                "font": font,
                "reported_value": reported_value,
                "display_timeout": display_timeout,
            },
            None,
        )
        return None

    async def notify_user_text_array(
        self,
        notification_text: Iterable[str],
        *,
        font: Font = Font.DEFAULT,
        auto_expand_to_fit_text: bool = False,
        display_timeout: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "NotifyUserTextArray",
            "reporting_operations.notify_user_text_array",
            {
                "notification_text": notification_text,
                "font": font,
                "auto_expand_to_fit_text": auto_expand_to_fit_text,
                "display_timeout": display_timeout,
            },
            None,
        )
        return None

    async def output_sa_report_to_excel(
        self,
        report_name: CollectionObjectName,
        file_name: FileReference,
        *,
        show_file: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "OutputSaReportToExcel",
            "reporting_operations.output_sa_report_to_excel",
            {
                "report_name": report_name,
                "file_name": file_name,
                "show_file": show_file,
            },
            None,
        )
        return None

    async def output_sa_report_to_pdf(
        self,
        report_name: CollectionObjectName,
        file_name: FileReference,
        *,
        show_pdf: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "OutputSaReportToPdf",
            "reporting_operations.output_sa_report_to_pdf",
            {
                "report_name": report_name,
                "file_name": file_name,
                "show_pdf": show_pdf,
            },
            None,
        )
        return None

    async def quick_report(
        self,
        item_name: CollectionObjectName,
        *,
        report_name_optional: str = "",
        open_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "QuickReport",
            "reporting_operations.quick_report",
            {
                "item_name": item_name,
                "report_name_optional": report_name_optional,
                "open_report": open_report,
            },
            None,
        )
        return None

    async def refresh_callout_views_in_sa_report(
        self,
        report_name: CollectionItemName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "RefreshCalloutViewsInSaReport",
            "reporting_operations.refresh_callout_views_in_sa_report",
            {
                "report_name": report_name,
            },
            None,
        )
        return None

    async def refresh_report_bar(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "RefreshReportBar",
            "reporting_operations.refresh_report_bar",
            {},
            None,
        )
        return None

    async def remove_report_tag(
        self,
        *,
        tag_name: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "RemoveReportTag",
            "reporting_operations.remove_report_tag",
            {
                "tag_name": tag_name,
            },
            None,
        )
        return None

    async def rename_picture(
        self,
        original_picture_name: CollectionItemName,
        new_picture_name: CollectionItemName,
        *,
        overwrite_if_exists: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "RenamePicture",
            "reporting_operations.rename_picture",
            {
                "original_picture_name": original_picture_name,
                "new_picture_name": new_picture_name,
                "overwrite_if_exists": overwrite_if_exists,
            },
            None,
        )
        return None

    async def save_chart_to_jpeg_file(
        self,
        chart_to_save: ChartName,
        file_to_save_to: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SaveChartToJPegFile",
            "reporting_operations.save_chart_to_jpeg_file",
            {
                "chart_to_save": chart_to_save,
                "file_to_save_to": file_to_save_to,
            },
            None,
        )
        return None

    async def save_current_view_bmp_jpg_png_gif_tiff(
        self,
        file_to_save_to: FileReference,
        *,
        render_scale_factor_1_0_uses_window_size: float = 1.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SaveCurrentViewBmpJpgPngGifTiff",
            "reporting_operations.save_current_view_bmp_jpg_png_gif_tiff",
            {
                "file_to_save_to": file_to_save_to,
                "render_scale_factor_1_0_uses_window_size": render_scale_factor_1_0_uses_window_size,
            },
            None,
        )
        return None

    async def set_custom_table_cell_color(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
        foreground_color_name: Color,
        background_color_name: Color,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableCellColor",
            "reporting_operations.set_custom_table_cell_color",
            {
                "table_name": table_name,
                "row": row,
                "column": column,
                "foreground_color_name": foreground_color_name,
                "background_color_name": background_color_name,
            },
            None,
        )
        return None

    async def set_custom_table_cell_double(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
        value: float = 0.000000,
        span: int = 1,
        decimal_precision: int = -1,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableCellDouble",
            "reporting_operations.set_custom_table_cell_double",
            {
                "table_name": table_name,
                "row": row,
                "column": column,
                "value": value,
                "span": span,
                "decimal_precision": decimal_precision,
            },
            None,
        )
        return None

    async def set_custom_table_cell_font(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
        font: Font = Font.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableCellFont",
            "reporting_operations.set_custom_table_cell_font",
            {
                "table_name": table_name,
                "row": row,
                "column": column,
                "font": font,
            },
            None,
        )
        return None

    async def set_custom_table_cell_string(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
        value: str = "",
        span: int = 1,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableCellString",
            "reporting_operations.set_custom_table_cell_string",
            {
                "table_name": table_name,
                "row": row,
                "column": column,
                "value": value,
                "span": span,
            },
            None,
        )
        return None

    async def set_custom_table_header_cell(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        column: int = 0,
        header_text: str = "",
        span: int = 1,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableHeaderCell",
            "reporting_operations.set_custom_table_header_cell",
            {
                "table_name": table_name,
                "row": row,
                "column": column,
                "header_text": header_text,
                "span": span,
            },
            None,
        )
        return None

    async def set_custom_table_header_row(
        self,
        table_name: CollectionObjectName,
        *,
        row: int = 0,
        value: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableHeaderRow",
            "reporting_operations.set_custom_table_header_row",
            {
                "table_name": table_name,
                "row": row,
                "value": value,
            },
            None,
        )
        return None

    async def set_custom_table_title(
        self,
        table_name: CollectionObjectName,
        *,
        title_line_1: str = "",
        title_line_2: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetCustomTableTitle",
            "reporting_operations.set_custom_table_title",
            {
                "table_name": table_name,
                "title_line_1": title_line_1,
                "title_line_2": title_line_2,
            },
            None,
        )
        return None

    async def set_point_group_report_options(
        self,
        point_group: CollectionObjectName,
        *,
        coordinate_system: CoordinateSystemType = CoordinateSystemType.CARTESIAN,
        show_x_component: bool = True,
        show_y_component: bool = True,
        show_z_component: bool = True,
        show_offsets: bool = False,
        show_uncertainty: bool = True,
        show_notes: bool = False,
        show_measurements: bool = False,
        show_measurement_details: bool = False,
        show_pointing_error_worst_angle: bool = False,
        sort_by_point_names: bool = True,
        make_default: bool = False,
        apply_to_all: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetPointGroupReportOptions",
            "reporting_operations.set_point_group_report_options",
            {
                "point_group": point_group,
                "coordinate_system": coordinate_system,
                "show_x_component": show_x_component,
                "show_y_component": show_y_component,
                "show_z_component": show_z_component,
                "show_offsets": show_offsets,
                "show_uncertainty": show_uncertainty,
                "show_notes": show_notes,
                "show_measurements": show_measurements,
                "show_measurement_details": show_measurement_details,
                "show_pointing_error_worst_angle": show_pointing_error_worst_angle,
                "sort_by_point_names": sort_by_point_names,
                "make_default": make_default,
                "apply_to_all": apply_to_all,
            },
            None,
        )
        return None

    async def set_relationship_report_options(
        self,
        relationship_name: CollectionObjectName,
        *,
        report_options: PointDeltaReportOptions = PointDeltaReportOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetRelationshipReportOptions",
            "reporting_operations.set_relationship_report_options",
            {
                "relationship_name": relationship_name,
                "report_options": report_options,
            },
            None,
        )
        return None

    async def set_report_bar_visibility(
        self,
        *,
        show_report_bar: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetReportBarVisibility",
            "reporting_operations.set_report_bar_visibility",
            {
                "show_report_bar": show_report_bar,
            },
            None,
        )
        return None

    async def set_report_options_for_object(
        self,
        object: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetReportOptionsForObject",
            "reporting_operations.set_report_options_for_object",
            {
                "object": object,
            },
            None,
        )
        return None

    async def set_report_tag_value_from_double(
        self,
        *,
        tag_name: str = "",
        tag_value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetReportTagValueFromDouble",
            "reporting_operations.set_report_tag_value_from_double",
            {
                "tag_name": tag_name,
                "tag_value": tag_value,
            },
            None,
        )
        return None

    async def set_report_tag_value_from_integer(
        self,
        *,
        tag_name: str = "",
        tag_value: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetReportTagValueFromInteger",
            "reporting_operations.set_report_tag_value_from_integer",
            {
                "tag_name": tag_name,
                "tag_value": tag_value,
            },
            None,
        )
        return None

    async def set_report_tag_value_from_string(
        self,
        *,
        tag_name: str = "",
        tag_value: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetReportTagValueFromString",
            "reporting_operations.set_report_tag_value_from_string",
            {
                "tag_name": tag_name,
                "tag_value": tag_value,
            },
            None,
        )
        return None

    async def set_scale_for_picture(
        self,
        picture_name: CollectionItemName,
        *,
        scale: float = 100.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetScaleForPicture",
            "reporting_operations.set_scale_for_picture",
            {
                "picture_name": picture_name,
                "scale": scale,
            },
            None,
        )
        return None

    async def set_vector_group_report_options(
        self,
        vector_group: CollectionObjectName,
        *,
        report_options: PointDeltaReportOptions = PointDeltaReportOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ReportingOperations",
            "SetVectorGroupReportOptions",
            "reporting_operations.set_vector_group_report_options",
            {
                "vector_group": vector_group,
                "report_options": report_options,
            },
            None,
        )
        return None

    async def delete_scale_bar(
        self,
        scale_bar_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ScaleBarOperations",
            "DeleteScaleBar",
            "scale_bar_operations.delete_scale_bar",
            {
                "scale_bar_name": scale_bar_name,
            },
            None,
        )
        return None

    async def get_scale_bar_stats(
        self,
        scale_bar_name: CollectionObjectName,
    ) -> GetScaleBarStatsResult:
        return cast(
            GetScaleBarStatsResult,
            await self._invoke_mp_operation(
                "briosa.ScaleBarOperations",
                "GetScaleBarStats",
                "scale_bar_operations.get_scale_bar_stats",
                {
                    "scale_bar_name": scale_bar_name,
                },
                GetScaleBarStatsResult,
            ),
        )

    async def scale_bar_check(
        self,
        scale_bar_point_a: PointName,
        scale_bar_point_b: PointName,
        *,
        current_temperature_f: float = 0.000000,
        length_of_bar_at_68f: float = 0.000000,
        material_cte_ppm_f: float = 0.000000,
        tolerance: float = 0.000000,
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.ScaleBarOperations",
                "ScaleBarCheck",
                "scale_bar_operations.scale_bar_check",
                {
                    "scale_bar_point_a": scale_bar_point_a,
                    "scale_bar_point_b": scale_bar_point_b,
                    "current_temperature_f": current_temperature_f,
                    "length_of_bar_at_68f": length_of_bar_at_68f,
                    "material_cte_ppm_f": material_cte_ppm_f,
                    "tolerance": tolerance,
                },
                None,
            ),
        )

    async def set_inward_positive_normal(
        self,
        object_name: CollectionObjectName,
        *,
        inward_positive: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ScaleBarOperations",
            "SetInwardPositiveNormal",
            "scale_bar_operations.set_inward_positive_normal",
            {
                "object_name": object_name,
                "inward_positive": inward_positive,
            },
            None,
        )
        return None

    async def close_all_watch_windows(self) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "CloseAllWatchWindows",
            "utility_operations.close_all_watch_windows",
            {},
            None,
        )
        return None

    async def delete_folder(
        self,
        *,
        folder_path: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "DeleteFolder",
            "utility_operations.delete_folder",
            {
                "folder_path": folder_path,
            },
            None,
        )
        return None

    async def delete_items(
        self,
        item_list: Iterable[CollectionItemName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "DeleteItems",
            "utility_operations.delete_items",
            {
                "item_list": item_list,
            },
            None,
        )
        return None

    async def delete_objects(
        self,
        object_names: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "DeleteObjects",
            "utility_operations.delete_objects",
            {
                "object_names": object_names,
            },
            None,
        )
        return None

    async def get_active_language(self) -> GetActiveLanguageResult:
        return cast(
            GetActiveLanguageResult,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetActiveLanguage",
                "utility_operations.get_active_language",
                {},
                GetActiveLanguageResult,
            ),
        )

    async def get_active_units(self) -> ActiveUnits:
        return cast(
            ActiveUnits,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetActiveUnits",
                "utility_operations.get_active_units",
                {},
                ActiveUnits,
            ),
        )

    async def get_angular_representation(self) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetAngularRepresentation",
                "utility_operations.get_angular_representation",
                {},
                None,
            ),
        )

    async def get_collection_notes(
        self,
        collection: CollectionName,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetCollectionNotes",
                "utility_operations.get_collection_notes",
                {
                    "collection": collection,
                },
                None,
            ),
        )

    async def get_folder_collections(
        self,
        *,
        folder_path: str = "",
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetFolderCollections",
                "utility_operations.get_folder_collections",
                {
                    "folder_path": folder_path,
                },
                None,
            ),
        )

    async def get_folder_notes(
        self,
        *,
        folder_path: str = "",
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetFolderNotes",
                "utility_operations.get_folder_notes",
                {
                    "folder_path": folder_path,
                },
                None,
            ),
        )

    async def get_folders_by_wildcard(
        self,
        *,
        search_string: str = "",
        case_sensitive_search: bool = True,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetFoldersByWildcard",
                "utility_operations.get_folders_by_wildcard",
                {
                    "search_string": search_string,
                    "case_sensitive_search": case_sensitive_search,
                },
                None,
            ),
        )

    async def get_object_notes(
        self,
        object: CollectionObjectName,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetObjectNotes",
                "utility_operations.get_object_notes",
                {
                    "object": object,
                },
                None,
            ),
        )

    async def get_opc_da_tag_value_double(
        self,
        *,
        opc_server_da_tag_name: str = "",
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetOpcDaTagValueDouble",
                "utility_operations.get_opc_da_tag_value_double",
                {
                    "opc_server_da_tag_name": opc_server_da_tag_name,
                },
                None,
            ),
        )

    async def get_opc_da_tag_value_integer(
        self,
        *,
        opc_server_da_tag_name: str = "",
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetOpcDaTagValueInteger",
                "utility_operations.get_opc_da_tag_value_integer",
                {
                    "opc_server_da_tag_name": opc_server_da_tag_name,
                },
                None,
            ),
        )

    async def get_opc_da_tag_value_string(
        self,
        *,
        opc_server_da_tag_name: str = "",
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetOpcDaTagValueString",
                "utility_operations.get_opc_da_tag_value_string",
                {
                    "opc_server_da_tag_name": opc_server_da_tag_name,
                },
                None,
            ),
        )

    async def get_point_notes(
        self,
        point: PointName,
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetPointNotes",
                "utility_operations.get_point_notes",
                {
                    "point": point,
                },
                None,
            ),
        )

    async def get_screen_resolution(
        self,
        *,
        display_1_primary: int = -1,
    ) -> GetScreenResolutionResult:
        return cast(
            GetScreenResolutionResult,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetScreenResolution",
                "utility_operations.get_screen_resolution",
                {
                    "display_1_primary": display_1_primary,
                },
                GetScreenResolutionResult,
            ),
        )

    async def get_working_frame_properties(self) -> WorkingFrameProperties:
        return cast(
            WorkingFrameProperties,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "GetWorkingFrameProperties",
                "utility_operations.get_working_frame_properties",
                {},
                WorkingFrameProperties,
            ),
        )

    async def increment_point_name(
        self,
        base_point_name: PointName,
        *,
        increment: int = 0,
    ) -> PointName:
        return cast(
            PointName,
            await self._invoke_mp_operation(
                "briosa.UtilityOperations",
                "IncrementPointName",
                "utility_operations.increment_point_name",
                {
                    "base_point_name": base_point_name,
                    "increment": increment,
                },
                None,
            ),
        )

    async def lock_imported_items(
        self,
        *,
        lock_items: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "LockImportedItems",
            "utility_operations.lock_imported_items",
            {
                "lock_items": lock_items,
            },
            None,
        )
        return None

    async def lock_unlock_selected_items(
        self,
        item_list: Iterable[CollectionItemName],
        instruments: Iterable[CollectionInstrumentId],
        *,
        lock_items: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "LockUnlockSelectedItems",
            "utility_operations.lock_unlock_selected_items",
            {
                "item_list": item_list,
                "instruments": instruments,
                "lock_items": lock_items,
            },
            None,
        )
        return None

    async def lock_unlock_trapping_control(
        self,
        relationship_ref_list: Iterable[CollectionItemName],
        feature_check_ref_list: Iterable[CollectionItemName],
        datum_ref_list: Iterable[CollectionObjectName],
        *,
        lock_out_trapping: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "LockUnlockTrappingControl",
            "utility_operations.lock_unlock_trapping_control",
            {
                "relationship_ref_list": relationship_ref_list,
                "feature_check_ref_list": feature_check_ref_list,
                "datum_ref_list": datum_ref_list,
                "lock_out_trapping": lock_out_trapping,
            },
            None,
        )
        return None

    async def move_collection_to_folder(
        self,
        collection: CollectionName,
        *,
        folder_path: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "MoveCollectionToFolder",
            "utility_operations.move_collection_to_folder",
            {
                "collection": collection,
                "folder_path": folder_path,
            },
            None,
        )
        return None

    async def move_folder_to_folder(
        self,
        *,
        source_folder_path: str = "",
        destination_folder_path: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "MoveFolderToFolder",
            "utility_operations.move_folder_to_folder",
            {
                "source_folder_path": source_folder_path,
                "destination_folder_path": destination_folder_path,
            },
            None,
        )
        return None

    async def move_instruments_drag_graphically(
        self,
        instruments: Iterable[CollectionInstrumentId],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "MoveInstrumentsDragGraphically",
            "utility_operations.move_instruments_drag_graphically",
            {
                "instruments": instruments,
            },
            None,
        )
        return None

    async def move_objects_drag_graphically(
        self,
        objects: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "MoveObjectsDragGraphically",
            "utility_operations.move_objects_drag_graphically",
            {
                "objects": objects,
            },
            None,
        )
        return None

    async def scale_objects(
        self,
        objects: Iterable[CollectionObjectName],
        *,
        scale_factor: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "ScaleObjects",
            "utility_operations.scale_objects",
            {
                "objects": objects,
                "scale_factor": scale_factor,
            },
            None,
        )
        return None

    async def set_active_custom_language(
        self,
        language_file_name: FileReference,
        *,
        font: Font = Font.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetActiveCustomLanguage",
            "utility_operations.set_active_custom_language",
            {
                "language_file_name": language_file_name,
                "font": font,
            },
            None,
        )
        return None

    async def set_active_units(
        self,
        *,
        length: DistanceUnits = DistanceUnits.INCHES,
        display_inch_fractions: bool = False,
        inch_fraction_denominator: float = 16.000000,
        simplify_inch_fraction: bool = True,
        temperature: TemperatureUnits = TemperatureUnits.FAHRENHEIT,
        angular: AngularUnits = AngularUnits.DEGREES,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetActiveUnits",
            "utility_operations.set_active_units",
            {
                "length": length,
                "display_inch_fractions": display_inch_fractions,
                "inch_fraction_denominator": inch_fraction_denominator,
                "simplify_inch_fraction": simplify_inch_fraction,
                "temperature": temperature,
                "angular": angular,
            },
            None,
        )
        return None

    async def set_angular_representation(
        self,
        *,
        value_0_360_false_180: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetAngularRepresentation",
            "utility_operations.set_angular_representation",
            {
                "value_0_360_false_180": value_0_360_false_180,
            },
            None,
        )
        return None

    async def set_auto_event_creation(
        self,
        *,
        active: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetAutoEventCreation",
            "utility_operations.set_auto_event_creation",
            {
                "active": active,
            },
            None,
        )
        return None

    async def set_automatic_backup_state(
        self,
        *,
        auto_job_file_restore_points_active: bool = True,
        auto_measurements_backup_active: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetAutomaticBackupState",
            "utility_operations.set_automatic_backup_state",
            {
                "auto_job_file_restore_points_active": auto_job_file_restore_points_active,
                "auto_measurements_backup_active": auto_measurements_backup_active,
            },
            None,
        )
        return None

    async def set_automatic_relationship_construction_state(
        self,
        *,
        active: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetAutomaticRelationshipConstructionState",
            "utility_operations.set_automatic_relationship_construction_state",
            {
                "active": active,
            },
            None,
        )
        return None

    async def set_collection_notes(
        self,
        collection: CollectionName,
        notes: Iterable[str],
        *,
        append_false_overwrite: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetCollectionNotes",
            "utility_operations.set_collection_notes",
            {
                "collection": collection,
                "notes": notes,
                "append_false_overwrite": append_false_overwrite,
            },
            None,
        )
        return None

    async def set_decimal_digits_for_display(
        self,
        *,
        length: int = 4,
        angle: int = 4,
        scale: int = 6,
        unit_vector: int = 6,
        weight: int = 3,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetDecimalDigitsForDisplay",
            "utility_operations.set_decimal_digits_for_display",
            {
                "length": length,
                "angle": angle,
                "scale": scale,
                "unit_vector": unit_vector,
                "weight": weight,
            },
            None,
        )
        return None

    async def set_folder_notes(
        self,
        *,
        folder_path: str = "",
        notes: Iterable[str],
        append_false_overwrite: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetFolderNotes",
            "utility_operations.set_folder_notes",
            {
                "folder_path": folder_path,
                "notes": notes,
                "append_false_overwrite": append_false_overwrite,
            },
            None,
        )
        return None

    async def set_interaction_mode(
        self,
        sa_interaction_mode: SaInteractionMode,
        measurement_plan_interaction_mode: MpInteractionMode,
        measurement_plan_dialog_interaction_mode: MpDialogInteractionMode,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetInteractionMode",
            "utility_operations.set_interaction_mode",
            {
                "sa_interaction_mode": sa_interaction_mode,
                "measurement_plan_interaction_mode": measurement_plan_interaction_mode,
                "measurement_plan_dialog_interaction_mode": measurement_plan_dialog_interaction_mode,
            },
            None,
        )
        return None

    async def set_logging_state(
        self,
        *,
        active: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetLoggingState",
            "utility_operations.set_logging_state",
            {
                "active": active,
            },
            None,
        )
        return None

    async def set_notification_cancel_override(
        self,
        *,
        prohibit_cancel: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetNotificationCancelOverride",
            "utility_operations.set_notification_cancel_override",
            {
                "prohibit_cancel": prohibit_cancel,
            },
            None,
        )
        return None

    async def set_object_notes(
        self,
        object: CollectionObjectName,
        notes: Iterable[str],
        *,
        append_false_overwrite: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetObjectNotes",
            "utility_operations.set_object_notes",
            {
                "object": object,
                "notes": notes,
                "append_false_overwrite": append_false_overwrite,
            },
            None,
        )
        return None

    async def set_opc_da_tag_value_double(
        self,
        *,
        opc_server_da_tag_name: str = "",
        value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetOpcDaTagValueDouble",
            "utility_operations.set_opc_da_tag_value_double",
            {
                "opc_server_da_tag_name": opc_server_da_tag_name,
                "value": value,
            },
            None,
        )
        return None

    async def set_opc_da_tag_value_integer(
        self,
        *,
        opc_server_da_tag_name: str = "",
        value: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetOpcDaTagValueInteger",
            "utility_operations.set_opc_da_tag_value_integer",
            {
                "opc_server_da_tag_name": opc_server_da_tag_name,
                "value": value,
            },
            None,
        )
        return None

    async def set_opc_da_tag_value_string(
        self,
        *,
        opc_server_da_tag_name: str = "",
        value: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetOpcDaTagValueString",
            "utility_operations.set_opc_da_tag_value_string",
            {
                "opc_server_da_tag_name": opc_server_da_tag_name,
                "value": value,
            },
            None,
        )
        return None

    async def set_point_notes(
        self,
        point: PointName,
        notes: Iterable[str],
        *,
        append_false_overwrite: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetPointNotes",
            "utility_operations.set_point_notes",
            {
                "point": point,
                "notes": notes,
                "append_false_overwrite": append_false_overwrite,
            },
            None,
        )
        return None

    async def set_user_interface_profile(
        self,
        *,
        profile_name: str = "Default",
        profile_file_name_optional: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetUserInterfaceProfile",
            "utility_operations.set_user_interface_profile",
            {
                "profile_name": profile_name,
                "profile_file_name_optional": profile_file_name_optional,
            },
            None,
        )
        return None

    async def set_view_idle_update_frequency(
        self,
        *,
        idle_count: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetViewIdleUpdateFrequency",
            "utility_operations.set_view_idle_update_frequency",
            {
                "idle_count": idle_count,
            },
            None,
        )
        return None

    async def set_wild_card_asterisk_mode(
        self,
        *,
        auto_wrap_search_string: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetWildCardAsteriskMode",
            "utility_operations.set_wild_card_asterisk_mode",
            {
                "auto_wrap_search_string": auto_wrap_search_string,
            },
            None,
        )
        return None

    async def set_working_frame(
        self,
        new_working_frame_name: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "SetWorkingFrame",
            "utility_operations.set_working_frame",
            {
                "new_working_frame_name": new_working_frame_name,
            },
            None,
        )
        return None

    async def status_dialog(
        self,
        *,
        dialog_title: str = "",
        text_message: str = "",
        current_position: int = 0,
        upper_limit: int = 0,
        suppress_time_remaining: bool = True,
        close_dialog: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "StatusDialog",
            "utility_operations.status_dialog",
            {
                "dialog_title": dialog_title,
                "text_message": text_message,
                "current_position": current_position,
                "upper_limit": upper_limit,
                "suppress_time_remaining": suppress_time_remaining,
                "close_dialog": close_dialog,
            },
            None,
        )
        return None

    async def trim_log_file(
        self,
        *,
        number_of_entries_to_keep: int = 10,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "TrimLogFile",
            "utility_operations.trim_log_file",
            {
                "number_of_entries_to_keep": number_of_entries_to_keep,
            },
            None,
        )
        return None

    async def write_to_log(
        self,
        *,
        log_entry: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.UtilityOperations",
            "WriteToLog",
            "utility_operations.write_to_log",
            {
                "log_entry": log_entry,
            },
            None,
        )
        return None

    async def add_double_to_named_double_list_variable(
        self,
        *,
        name: str = "",
        double_value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "AddDoubleToNamedDoubleListVariable",
            "variables.add_double_to_named_double_list_variable",
            {
                "name": name,
                "double_value": double_value,
            },
            None,
        )
        return None

    async def clear_named_double_list_variable(
        self,
        *,
        name: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "ClearNamedDoubleListVariable",
            "variables.clear_named_double_list_variable",
            {
                "name": name,
            },
            None,
        )
        return None

    async def delete_variable(
        self,
        *,
        name: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "DeleteVariable",
            "variables.delete_variable",
            {
                "name": name,
            },
            None,
        )
        return None

    async def delete_variables_wildcard_match(
        self,
        *,
        variable_wildcard_criteria: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "DeleteVariablesWildcardMatch",
            "variables.delete_variables_wildcard_match",
            {
                "variable_wildcard_criteria": variable_wildcard_criteria,
            },
            None,
        )
        return None

    async def get_boolean_variable(
        self,
        *,
        name: str = "",
    ) -> bool:
        return cast(
            bool,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetBooleanVariable",
                "variables.get_boolean_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_collection_object_name_variable(
        self,
        *,
        name: str = "",
    ) -> CollectionObjectName:
        return cast(
            CollectionObjectName,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetCollectionObjectNameVariable",
                "variables.get_collection_object_name_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_collection_object_ref_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetCollectionObjectRefListVariable",
                "variables.get_collection_object_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_double_variable(
        self,
        *,
        name: str = "",
    ) -> float:
        return cast(
            float,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetDoubleVariable",
                "variables.get_double_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_integer_variable(
        self,
        *,
        name: str = "",
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetIntegerVariable",
                "variables.get_integer_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_named_double_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[float]:
        return cast(
            list[float],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetNamedDoubleListVariable",
                "variables.get_named_double_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_named_double_list_variable_min_max(
        self,
        *,
        name: str = "",
    ) -> GetNamedDoubleListVariableMinMaxResult:
        return cast(
            GetNamedDoubleListVariableMinMaxResult,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetNamedDoubleListVariableMinMax",
                "variables.get_named_double_list_variable_min_max",
                {
                    "name": name,
                },
                GetNamedDoubleListVariableMinMaxResult,
            ),
        )

    async def get_point_name_ref_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[PointName]:
        return cast(
            list[PointName],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetPointNameRefListVariable",
                "variables.get_point_name_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_point_name_variable(
        self,
        *,
        name: str = "",
    ) -> PointName:
        return cast(
            PointName,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetPointNameVariable",
                "variables.get_point_name_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_relationship_ref_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetRelationshipRefListVariable",
                "variables.get_relationship_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_report_items_reference_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetReportItemsReferenceListVariable",
                "variables.get_report_items_reference_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_string_ref_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[str]:
        return cast(
            list[str],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetStringRefListVariable",
                "variables.get_string_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_string_variable(
        self,
        *,
        name: str = "",
    ) -> str:
        return cast(
            str,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetStringVariable",
                "variables.get_string_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_transform_variable(
        self,
        *,
        name: str = "",
    ) -> Transform:
        return cast(
            Transform,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetTransformVariable",
                "variables.get_transform_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_vector_name_ref_list_variable(
        self,
        *,
        name: str = "",
    ) -> list[VectorName]:
        return cast(
            list[VectorName],
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetVectorNameRefListVariable",
                "variables.get_vector_name_ref_list_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def get_vector_variable(
        self,
        *,
        name: str = "",
    ) -> Vector:
        return cast(
            Vector,
            await self._invoke_mp_operation(
                "briosa.Variables",
                "GetVectorVariable",
                "variables.get_vector_variable",
                {
                    "name": name,
                },
                None,
            ),
        )

    async def set_boolean_variable(
        self,
        *,
        name: str = "",
        value: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetBooleanVariable",
            "variables.set_boolean_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_collection_object_name_variable(
        self,
        *,
        name: str = "",
        value: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetCollectionObjectNameVariable",
            "variables.set_collection_object_name_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_collection_object_ref_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetCollectionObjectRefListVariable",
            "variables.set_collection_object_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_double_variable(
        self,
        *,
        name: str = "",
        value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetDoubleVariable",
            "variables.set_double_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_font_variable(
        self,
        *,
        name: str = "",
        value: Font = Font.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetFontVariable",
            "variables.set_font_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_integer_variable(
        self,
        *,
        name: str = "",
        value: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetIntegerVariable",
            "variables.set_integer_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_named_double_list_variable(
        self,
        *,
        name: str = "",
        double_list_variable: Iterable[float],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetNamedDoubleListVariable",
            "variables.set_named_double_list_variable",
            {
                "name": name,
                "double_list_variable": double_list_variable,
            },
            None,
        )
        return None

    async def set_point_name_ref_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[PointName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetPointNameRefListVariable",
            "variables.set_point_name_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_point_name_variable(
        self,
        *,
        name: str = "",
        value: PointName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetPointNameVariable",
            "variables.set_point_name_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_relationship_ref_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[CollectionItemName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetRelationshipRefListVariable",
            "variables.set_relationship_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_report_items_reference_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[CollectionItemName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetReportItemsReferenceListVariable",
            "variables.set_report_items_reference_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_string_ref_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[str],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetStringRefListVariable",
            "variables.set_string_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_string_variable(
        self,
        *,
        name: str = "",
        value: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetStringVariable",
            "variables.set_string_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_transform_variable(
        self,
        *,
        name: str = "",
        value: Transform,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetTransformVariable",
            "variables.set_transform_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_vector_name_ref_list_variable(
        self,
        *,
        name: str = "",
        value: Iterable[VectorName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetVectorNameRefListVariable",
            "variables.set_vector_name_ref_list_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def set_vector_variable(
        self,
        *,
        name: str = "",
        value: Vector,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.Variables",
            "SetVectorVariable",
            "variables.set_vector_variable",
            {
                "name": name,
                "value": value,
            },
            None,
        )
        return None

    async def add_a_vector_to_vector_name_ref_list(
        self,
        vector_group_name: CollectionObjectName,
        *,
        vector_name: str = "",
        vector_name_list: Iterable[VectorName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "AddAVectorToVectorNameRefList",
            "vector_operations.add_a_vector_to_vector_name_ref_list",
            {
                "vector_group_name": vector_group_name,
                "vector_name": vector_name,
                "vector_name_list": vector_name_list,
            },
            None,
        )
        return None

    async def auto_range_and_set_vector_group_colorization_all(
        self,
        *,
        treat_individually: bool = False,
        colorization_options_uses_mode_only: ColorizationOptions = ColorizationOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "AutoRangeAndSetVectorGroupColorizationAll",
            "vector_operations.auto_range_and_set_vector_group_colorization_all",
            {
                "treat_individually": treat_individually,
                "colorization_options_uses_mode_only": colorization_options_uses_mode_only,
            },
            None,
        )
        return None

    async def auto_range_and_set_vector_group_colorization_selected(
        self,
        vector_groups_to_be_set: Iterable[CollectionVectorGroupName],
        *,
        treat_individually: bool = False,
        colorization_options_uses_mode_only: ColorizationOptions = ColorizationOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "AutoRangeAndSetVectorGroupColorizationSelected",
            "vector_operations.auto_range_and_set_vector_group_colorization_selected",
            {
                "vector_groups_to_be_set": vector_groups_to_be_set,
                "treat_individually": treat_individually,
                "colorization_options_uses_mode_only": colorization_options_uses_mode_only,
            },
            None,
        )
        return None

    async def delete_ith_vector_from_vector_group(
        self,
        vector_group_name: CollectionObjectName,
        *,
        vector_index: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "DeleteIthVectorFromVectorGroup",
            "vector_operations.delete_ith_vector_from_vector_group",
            {
                "vector_group_name": vector_group_name,
                "vector_index": vector_index,
            },
            None,
        )
        return None

    async def delete_vector_by_name(
        self,
        vector_group_name: CollectionObjectName,
        *,
        vector_name: str = "",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "DeleteVectorByName",
            "vector_operations.delete_vector_by_name",
            {
                "vector_group_name": vector_group_name,
                "vector_name": vector_name,
            },
            None,
        )
        return None

    async def delete_vectors(
        self,
        vector_name_list: Iterable[VectorName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "DeleteVectors",
            "vector_operations.delete_vectors",
            {
                "vector_name_list": vector_name_list,
            },
            None,
        )
        return None

    async def get_ith_vector_from_vector_group(
        self,
        vector_group_name: CollectionObjectName,
        *,
        vector_index: int = 0,
    ) -> GetIthVectorFromVectorGroupResult:
        return cast(
            GetIthVectorFromVectorGroupResult,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetIthVectorFromVectorGroup",
                "vector_operations.get_ith_vector_from_vector_group",
                {
                    "vector_group_name": vector_group_name,
                    "vector_index": vector_index,
                },
                GetIthVectorFromVectorGroupResult,
            ),
        )

    async def get_ith_vector_from_vector_name_ref_list(
        self,
        vector_name_list: Iterable[VectorName],
        *,
        vector_index: int = 0,
    ) -> GetIthVectorFromVectorNameRefListResult:
        return cast(
            GetIthVectorFromVectorNameRefListResult,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetIthVectorFromVectorNameRefList",
                "vector_operations.get_ith_vector_from_vector_name_ref_list",
                {
                    "vector_name_list": vector_name_list,
                    "vector_index": vector_index,
                },
                GetIthVectorFromVectorNameRefListResult,
            ),
        )

    async def get_number_of_vectors_in_vector_group(
        self,
        vector_group_name: CollectionObjectName,
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetNumberOfVectorsInVectorGroup",
                "vector_operations.get_number_of_vectors_in_vector_group",
                {
                    "vector_group_name": vector_group_name,
                },
                None,
            ),
        )

    async def get_number_of_vectors_in_vector_name_ref_list(
        self,
        vector_name_list: Iterable[VectorName],
    ) -> int:
        return cast(
            int,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetNumberOfVectorsInVectorNameRefList",
                "vector_operations.get_number_of_vectors_in_vector_name_ref_list",
                {
                    "vector_name_list": vector_name_list,
                },
                None,
            ),
        )

    async def get_vector_from_vector_group_by_name(
        self,
        vector_group_name: CollectionObjectName,
        *,
        vector_name: str = "",
    ) -> GetVectorFromVectorGroupByNameResult:
        return cast(
            GetVectorFromVectorGroupByNameResult,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetVectorFromVectorGroupByName",
                "vector_operations.get_vector_from_vector_group_by_name",
                {
                    "vector_group_name": vector_group_name,
                    "vector_name": vector_name,
                },
                GetVectorFromVectorGroupByNameResult,
            ),
        )

    async def get_vector_group_properties(
        self,
        vector_group_name: CollectionObjectName,
    ) -> GetVectorGroupPropertiesResult:
        return cast(
            GetVectorGroupPropertiesResult,
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "GetVectorGroupProperties",
                "vector_operations.get_vector_group_properties",
                {
                    "vector_group_name": vector_group_name,
                },
                GetVectorGroupPropertiesResult,
            ),
        )

    async def set_vector_group_colorization_options_all(
        self,
        *,
        colorization_options: ColorizationOptions = ColorizationOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "SetVectorGroupColorizationOptionsAll",
            "vector_operations.set_vector_group_colorization_options_all",
            {
                "colorization_options": colorization_options,
            },
            None,
        )
        return None

    async def set_vector_group_colorization_options_selected(
        self,
        vector_groups_to_be_set: Iterable[CollectionVectorGroupName],
        *,
        colorization_options: ColorizationOptions = ColorizationOptions.DEFAULT,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.VectorOperations",
            "SetVectorGroupColorizationOptionsSelected",
            "vector_operations.set_vector_group_colorization_options_selected",
            {
                "vector_groups_to_be_set": vector_groups_to_be_set,
                "colorization_options": colorization_options,
            },
            None,
        )
        return None

    async def sort_vectors(
        self,
        source_vectors: Iterable[VectorName],
        *,
        sort_method: str = "Magnitude",
        coordinate_system: CoordinateSystemType = CoordinateSystemType.CARTESIAN,
        primary_sort_coordinate: str = "X (R)",
        secondary_sort_coordinate: str = "Y (Theta)",
        tertiary_sort_coordinate: str = "Z (Phi)",
        primary_coordinate_granularity: float = 0.000000,
        secondary_coordinate_granularity: float = 0.000000,
        tertiary_coordinate_granularity: float = 0.000000,
        ascending: bool = False,
    ) -> list[VectorName]:
        return cast(
            list[VectorName],
            await self._invoke_mp_operation(
                "briosa.VectorOperations",
                "SortVectors",
                "vector_operations.sort_vectors",
                {
                    "source_vectors": source_vectors,
                    "sort_method": sort_method,
                    "coordinate_system": coordinate_system,
                    "primary_sort_coordinate": primary_sort_coordinate,
                    "secondary_sort_coordinate": secondary_sort_coordinate,
                    "tertiary_sort_coordinate": tertiary_sort_coordinate,
                    "primary_coordinate_granularity": primary_coordinate_granularity,
                    "secondary_coordinate_granularity": secondary_coordinate_granularity,
                    "tertiary_coordinate_granularity": tertiary_coordinate_granularity,
                    "ascending": ascending,
                },
                None,
            ),
        )

    async def auto_scale(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "AutoScale",
            "view_control.auto_scale",
            {},
            None,
        )
        return None

    async def center_graphics_about_objects(
        self,
        *,
        object_type: ObjectType = ObjectType.ANY,
        collection_wildcard_criteria: str = "*",
        object_wildcard_criteria: str = "*",
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "CenterGraphicsAboutObjects",
            "view_control.center_graphics_about_objects",
            {
                "object_type": object_type,
                "collection_wildcard_criteria": collection_wildcard_criteria,
                "object_wildcard_criteria": object_wildcard_criteria,
            },
            None,
        )
        return None

    async def center_graphics_about_point(
        self,
        point_name: PointName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "CenterGraphicsAboutPoint",
            "view_control.center_graphics_about_point",
            {
                "point_name": point_name,
            },
            None,
        )
        return None

    async def define_point_of_view(
        self,
        view_name: ViewName,
        *,
        rotation_x: float = 0.000000,
        rotation_y: float = 0.000000,
        rotation_z: float = 0.000000,
        restore_zoom_settings: bool = False,
        scale_factor: float = 1.000000,
        origin_x: float = 0.000000,
        origin_y: float = 0.000000,
        restore_render_mode: bool = False,
        rendering_mode: RenderModeType = RenderModeType.WIREFRAME,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "DefinePointOfView",
            "view_control.define_point_of_view",
            {
                "view_name": view_name,
                "rotation_x": rotation_x,
                "rotation_y": rotation_y,
                "rotation_z": rotation_z,
                "restore_zoom_settings": restore_zoom_settings,
                "scale_factor": scale_factor,
                "origin_x": origin_x,
                "origin_y": origin_y,
                "restore_render_mode": restore_render_mode,
                "rendering_mode": rendering_mode,
            },
            None,
        )
        return None

    async def get_active_clipping_planes(self) -> list[CollectionObjectName]:
        return cast(
            list[CollectionObjectName],
            await self._invoke_mp_operation(
                "briosa.ViewControl",
                "GetActiveClippingPlanes",
                "view_control.get_active_clipping_planes",
                {},
                None,
            ),
        )

    async def get_point_of_view_parameters(
        self,
        view_name: ViewName,
    ) -> GetPointOfViewParametersResult:
        return cast(
            GetPointOfViewParametersResult,
            await self._invoke_mp_operation(
                "briosa.ViewControl",
                "GetPointOfViewParameters",
                "view_control.get_point_of_view_parameters",
                {
                    "view_name": view_name,
                },
                GetPointOfViewParametersResult,
            ),
        )

    async def hide_all_callout_views(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "HideAllCalloutViews",
            "view_control.hide_all_callout_views",
            {},
            None,
        )
        return None

    async def hide_objects(
        self,
        objects_to_hide: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "HideObjects",
            "view_control.hide_objects",
            {
                "objects_to_hide": objects_to_hide,
            },
            None,
        )
        return None

    async def highlight_objects(
        self,
        object_names_empty_to_clear_all: Iterable[CollectionObjectName],
        *,
        high_light_objects: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "HighlightObjects",
            "view_control.highlight_objects",
            {
                "object_names_empty_to_clear_all": object_names_empty_to_clear_all,
                "high_light_objects": high_light_objects,
            },
            None,
        )
        return None

    async def highlight_point(
        self,
        point_name_empty_to_clear_all: PointName,
        *,
        show_point: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "HighlightPoint",
            "view_control.highlight_point",
            {
                "point_name_empty_to_clear_all": point_name_empty_to_clear_all,
                "show_point": show_point,
            },
            None,
        )
        return None

    async def highlight_relationships(
        self,
        relationships_empty_to_clear_all: Iterable[CollectionItemName],
        *,
        high_light_relationships: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "HighlightRelationships",
            "view_control.highlight_relationships",
            {
                "relationships_empty_to_clear_all": relationships_empty_to_clear_all,
                "high_light_relationships": high_light_relationships,
            },
            None,
        )
        return None

    async def load_ribbon_bar_from_xml_file(
        self,
        file_path: FileReference,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "LoadRibbonBarFromXmlFile",
            "view_control.load_ribbon_bar_from_xml_file",
            {
                "file_path": file_path,
            },
            None,
        )
        return None

    async def refresh_views(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "RefreshViews",
            "view_control.refresh_views",
            {},
            None,
        )
        return None

    async def reset_ribbon_bar_to_default(self) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ResetRibbonBarToDefault",
            "view_control.reset_ribbon_bar_to_default",
            {},
            None,
        )
        return None

    async def save_point_of_view(
        self,
        view_name: ViewName,
        *,
        restore_zoom_settings: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SavePointOfView",
            "view_control.save_point_of_view",
            {
                "view_name": view_name,
                "restore_zoom_settings": restore_zoom_settings,
            },
            None,
        )
        return None

    async def set_background_color(
        self,
        solid_color_name: Color,
        gradient_start_color_name: Color,
        gradient_end_color_name: Color,
        highlight_color: Color,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetBackgroundColor",
            "view_control.set_background_color",
            {
                "solid_color_name": solid_color_name,
                "gradient_start_color_name": gradient_start_color_name,
                "gradient_end_color_name": gradient_end_color_name,
                "highlight_color": highlight_color,
            },
            None,
        )
        return None

    async def set_mp_window_state(
        self,
        mp_window_state: WindowState,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetMpWindowState",
            "view_control.set_mp_window_state",
            {
                "mp_window_state": mp_window_state,
            },
            None,
        )
        return None

    async def set_objects_color(
        self,
        objects_to_change: Iterable[CollectionObjectName],
        new_working_color_name: Color,
        *,
        auto_increment: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetObjectsColor",
            "view_control.set_objects_color",
            {
                "objects_to_change": objects_to_change,
                "new_working_color_name": new_working_color_name,
                "auto_increment": auto_increment,
            },
            None,
        )
        return None

    async def set_objects_translucency(
        self,
        objects_to_change: Iterable[CollectionObjectName],
        rendering_type: TranslucencyType,
        *,
        opacity_value: float = 0.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetObjectsTranslucency",
            "view_control.set_objects_translucency",
            {
                "objects_to_change": objects_to_change,
                "rendering_type": rendering_type,
                "opacity_value": opacity_value,
            },
            None,
        )
        return None

    async def set_point_of_view(
        self,
        view_name: ViewName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetPointOfView",
            "view_control.set_point_of_view",
            {
                "view_name": view_name,
            },
            None,
        )
        return None

    async def set_point_of_view_from_frame(
        self,
        frame: CollectionObjectName,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetPointOfViewFromFrame",
            "view_control.set_point_of_view_from_frame",
            {
                "frame": frame,
            },
            None,
        )
        return None

    async def set_point_of_view_from_instrument_updates(
        self,
        instrument_id: CollectionInstrumentId,
        *,
        display_view_control: bool = True,
        enable_set_viewpoint_from_instrument_updates: bool = False,
        update_view_percent: float = 75.000000,
        clip_behind_probe: bool = False,
        automatic_zoom_when_trapping: bool = False,
        enable_directional_cloud_points: bool = False,
        angle_reset_threshold: float = 45.000000,
        animation_steps: int = 8,
        reference_frame_object: CollectionObjectName,
        use_scan_stripe_for_view_focus: bool = True,
        zoom_factor: float = 1.000000,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetPointOfViewFromInstrumentUpdates",
            "view_control.set_point_of_view_from_instrument_updates",
            {
                "instrument_id": instrument_id,
                "display_view_control": display_view_control,
                "enable_set_viewpoint_from_instrument_updates": enable_set_viewpoint_from_instrument_updates,
                "update_view_percent": update_view_percent,
                "clip_behind_probe": clip_behind_probe,
                "automatic_zoom_when_trapping": automatic_zoom_when_trapping,
                "enable_directional_cloud_points": enable_directional_cloud_points,
                "angle_reset_threshold": angle_reset_threshold,
                "animation_steps": animation_steps,
                "reference_frame_object": reference_frame_object,
                "use_scan_stripe_for_view_focus": use_scan_stripe_for_view_focus,
                "zoom_factor": zoom_factor,
            },
            None,
        )
        return None

    async def set_render_mode_type(
        self,
        rendering_mode: RenderModeType,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetRenderModeType",
            "view_control.set_render_mode_type",
            {
                "rendering_mode": rendering_mode,
            },
            None,
        )
        return None

    async def set_sa_window_pos(
        self,
        *,
        pos_x: int = 0,
        pos_y: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetSaWindowPos",
            "view_control.set_sa_window_pos",
            {
                "pos_x": pos_x,
                "pos_y": pos_y,
            },
            None,
        )
        return None

    async def set_sa_window_size(
        self,
        *,
        width: int = 0,
        height: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetSaWindowSize",
            "view_control.set_sa_window_size",
            {
                "width": width,
                "height": height,
            },
            None,
        )
        return None

    async def set_sa_window_state(
        self,
        sa_window_state: WindowState,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetSaWindowState",
            "view_control.set_sa_window_state",
            {
                "sa_window_state": sa_window_state,
            },
            None,
        )
        return None

    async def set_target_labels_use_full_names(
        self,
        *,
        use_full_names: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetTargetLabelsUseFullNames",
            "view_control.set_target_labels_use_full_names",
            {
                "use_full_names": use_full_names,
            },
            None,
        )
        return None

    async def set_toolkit_visibility(
        self,
        *,
        show_toolkit: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetToolkitVisibility",
            "view_control.set_toolkit_visibility",
            {
                "show_toolkit": show_toolkit,
            },
            None,
        )
        return None

    async def set_view_clipping_plane(
        self,
        object: CollectionObjectName,
        *,
        remove_clipping_plane: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetViewClippingPlane",
            "view_control.set_view_clipping_plane",
            {
                "object": object,
                "remove_clipping_plane": remove_clipping_plane,
            },
            None,
        )
        return None

    async def set_working_color(
        self,
        new_working_color_name: Color,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetWorkingColor",
            "view_control.set_working_color",
            {
                "new_working_color_name": new_working_color_name,
            },
            None,
        )
        return None

    async def set_working_color_auto_increment(
        self,
        *,
        auto_increment: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "SetWorkingColorAutoIncrement",
            "view_control.set_working_color_auto_increment",
            {
                "auto_increment": auto_increment,
            },
            None,
        )
        return None

    async def show_hide_by_object_type(
        self,
        *,
        all_collections: bool = False,
        specific_collection: CollectionName,
        object_type_to_show_hide: ObjectType = ObjectType.ANY,
        hide_show_false: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideByObjectType",
            "view_control.show_hide_by_object_type",
            {
                "all_collections": all_collections,
                "specific_collection": specific_collection,
                "object_type_to_show_hide": object_type_to_show_hide,
                "hide_show_false": hide_show_false,
            },
            None,
        )
        return None

    async def show_hide_callout_view(
        self,
        callout_view_to_show: CollectionItemName,
        *,
        show_callout_view: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideCalloutView",
            "view_control.show_hide_callout_view",
            {
                "callout_view_to_show": callout_view_to_show,
                "show_callout_view": show_callout_view,
            },
            None,
        )
        return None

    async def show_hide_dimension(
        self,
        dimension_name: CollectionItemName,
        *,
        show_dimension: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideDimension",
            "view_control.show_hide_dimension",
            {
                "dimension_name": dimension_name,
                "show_dimension": show_dimension,
            },
            None,
        )
        return None

    async def show_hide_points(
        self,
        point_names: Iterable[PointName],
        *,
        show_hide_false: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHidePoints",
            "view_control.show_hide_points",
            {
                "point_names": point_names,
                "show_hide_false": show_hide_false,
            },
            None,
        )
        return None

    async def show_by_object_type(
        self,
        object_type_to_show: CollectionObjectName,
        *,
        all_collections: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowByObjectType",
            "view_control.show_by_object_type",
            {
                "object_type_to_show": object_type_to_show,
                "all_collections": all_collections,
            },
            None,
        )
        return None

    async def show_items_in_tree(
        self,
        *,
        collapse_all_other_items: bool = True,
        points: Iterable[PointName],
        objects: Iterable[CollectionObjectName],
        instruments: Iterable[CollectionInstrumentId],
        feature_checks: Iterable[CollectionItemName],
        datums: Iterable[CollectionObjectName],
        collections: Iterable[str],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowItemsInTree",
            "view_control.show_items_in_tree",
            {
                "collapse_all_other_items": collapse_all_other_items,
                "points": points,
                "objects": objects,
                "instruments": instruments,
                "feature_checks": feature_checks,
                "datums": datums,
                "collections": collections,
            },
            None,
        )
        return None

    async def show_labels(
        self,
        *,
        point_labels_on: bool = False,
        objects_labels_on: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowLabels",
            "view_control.show_labels",
            {
                "point_labels_on": point_labels_on,
                "objects_labels_on": objects_labels_on,
            },
            None,
        )
        return None

    async def show_objects(
        self,
        objects_to_show: Iterable[CollectionObjectName],
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowObjects",
            "view_control.show_objects",
            {
                "objects_to_show": objects_to_show,
            },
            None,
        )
        return None

    async def show_hide_annotations_for_datums(
        self,
        datum_name_list: Iterable[CollectionObjectName],
        *,
        show: bool = False,
        highlight: bool = False,
        set_inspection_view: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideAnnotationsForDatums",
            "view_control.show_hide_annotations_for_datums",
            {
                "datum_name_list": datum_name_list,
                "show": show,
                "highlight": highlight,
                "set_inspection_view": set_inspection_view,
            },
            None,
        )
        return None

    async def show_hide_annotations_for_feature_checks(
        self,
        feature_check_name_list: Iterable[CollectionItemName],
        *,
        show: bool = False,
        highlight: bool = False,
        set_inspection_view: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideAnnotationsForFeatureChecks",
            "view_control.show_hide_annotations_for_feature_checks",
            {
                "feature_check_name_list": feature_check_name_list,
                "show": show,
                "highlight": highlight,
                "set_inspection_view": set_inspection_view,
            },
            None,
        )
        return None

    async def show_hide_inspection_bar(
        self,
        *,
        show_inspection_bar: bool = True,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideInspectionBar",
            "view_control.show_hide_inspection_bar",
            {
                "show_inspection_bar": show_inspection_bar,
            },
            None,
        )
        return None

    async def show_hide_instrument_interface(
        self,
        instrument_id: CollectionInstrumentId,
        *,
        minimize_interface: bool = False,
        hide_interface: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideInstrumentInterface",
            "view_control.show_hide_instrument_interface",
            {
                "instrument_id": instrument_id,
                "minimize_interface": minimize_interface,
                "hide_interface": hide_interface,
            },
            None,
        )
        return None

    async def show_hide_instrument_probe_tip(
        self,
        *,
        show_instrument_probe_tip: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideInstrumentProbeTip",
            "view_control.show_hide_instrument_probe_tip",
            {
                "show_instrument_probe_tip": show_instrument_probe_tip,
            },
            None,
        )
        return None

    async def show_hide_instruments(
        self,
        instrument_i_ds: Iterable[CollectionInstrumentId],
        *,
        show_instruments: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideInstruments",
            "view_control.show_hide_instruments",
            {
                "instrument_i_ds": instrument_i_ds,
                "show_instruments": show_instruments,
            },
            None,
        )
        return None

    async def show_hide_relationship_report(
        self,
        collection_name: CollectionName,
        *,
        show_relationship_report: bool = False,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideRelationshipReport",
            "view_control.show_hide_relationship_report",
            {
                "collection_name": collection_name,
                "show_relationship_report": show_relationship_report,
            },
            None,
        )
        return None

    async def show_hide_relationship_watch(
        self,
        relationship_name: CollectionObjectName,
        *,
        show_relationship_watch: bool = False,
        relationship_watch_window_properties: CollectionObjectName,
        window_top_left_x_position: int = 0,
        window_top_left_y_position: int = 0,
        window_width: int = 0,
        window_height: int = 0,
    ) -> None:
        await self._invoke_mp_operation(
            "briosa.ViewControl",
            "ShowHideRelationshipWatch",
            "view_control.show_hide_relationship_watch",
            {
                "relationship_name": relationship_name,
                "show_relationship_watch": show_relationship_watch,
                "relationship_watch_window_properties": relationship_watch_window_properties,
                "window_top_left_x_position": window_top_left_x_position,
                "window_top_left_y_position": window_top_left_y_position,
                "window_width": window_width,
                "window_height": window_height,
            },
            None,
        )
        return None


WAVE_A_OPERATIONS = (
    (
        "angle_between_line_and_plane",
        "briosa.AnalysisOperations",
        "AngleBetweenLineAndPlane",
        "analysis_operations.angle_between_line_and_plane",
    ),
    (
        "angle_between_two_lines",
        "briosa.AnalysisOperations",
        "AngleBetweenTwoLines",
        "analysis_operations.angle_between_two_lines",
    ),
    (
        "angle_between_two_planes_normals",
        "briosa.AnalysisOperations",
        "AngleBetweenTwoPlanesNormals",
        "analysis_operations.angle_between_two_planes_normals",
    ),
    (
        "best_fit_transformation_group_to_group",
        "briosa.AnalysisOperations",
        "BestFitTransformationGroupToGroup",
        "analysis_operations.best_fit_transformation_group_to_group",
    ),
    (
        "compute_group_to_group_orientation_rx_ry_rz",
        "briosa.AnalysisOperations",
        "ComputeGroupToGroupOrientationRxRyRz",
        "analysis_operations.compute_group_to_group_orientation_rx_ry_rz",
    ),
    (
        "create_point_uncertainty_cloud_point_sets",
        "briosa.AnalysisOperations",
        "CreatePointUncertaintyCloudPointSets",
        "analysis_operations.create_point_uncertainty_cloud_point_sets",
    ),
    (
        "create_point_uncertainty_fields",
        "briosa.AnalysisOperations",
        "CreatePointUncertaintyFields",
        "analysis_operations.create_point_uncertainty_fields",
    ),
    (
        "fit_geometry_to_point_group",
        "briosa.AnalysisOperations",
        "FitGeometryToPointGroup",
        "analysis_operations.fit_geometry_to_point_group",
    ),
    (
        "fit_geometry_to_point_group_projected_to_plane",
        "briosa.AnalysisOperations",
        "FitGeometryToPointGroupProjectedToPlane",
        "analysis_operations.fit_geometry_to_point_group_projected_to_plane",
    ),
    (
        "fit_geometry_to_points",
        "briosa.AnalysisOperations",
        "FitGeometryToPoints",
        "analysis_operations.fit_geometry_to_points",
    ),
    (
        "get_bspline_properties",
        "briosa.AnalysisOperations",
        "GetBSplineProperties",
        "analysis_operations.get_bspline_properties",
    ),
    (
        "get_circle_properties",
        "briosa.AnalysisOperations",
        "GetCircleProperties",
        "analysis_operations.get_circle_properties",
    ),
    (
        "get_cone_properties",
        "briosa.AnalysisOperations",
        "GetConeProperties",
        "analysis_operations.get_cone_properties",
    ),
    (
        "get_coordinate_for_ith_point_in_point_set",
        "briosa.AnalysisOperations",
        "GetCoordinateForIthPointInPointSet",
        "analysis_operations.get_coordinate_for_ith_point_in_point_set",
    ),
    (
        "get_cylinder_properties",
        "briosa.AnalysisOperations",
        "GetCylinderProperties",
        "analysis_operations.get_cylinder_properties",
    ),
    (
        "get_ellipse_properties",
        "briosa.AnalysisOperations",
        "GetEllipseProperties",
        "analysis_operations.get_ellipse_properties",
    ),
    (
        "get_euler_parameters_for_frame",
        "briosa.AnalysisOperations",
        "GetEulerParametersForFrame",
        "analysis_operations.get_euler_parameters_for_frame",
    ),
    (
        "get_euler_parameters_for_ith_frame_in_frame_set",
        "briosa.AnalysisOperations",
        "GetEulerParametersForIthFrameInFrameSet",
        "analysis_operations.get_euler_parameters_for_ith_frame_in_frame_set",
    ),
    (
        "get_ith_collection_name",
        "briosa.AnalysisOperations",
        "GetIthCollectionName",
        "analysis_operations.get_ith_collection_name",
    ),
    (
        "get_ith_point_from_group",
        "briosa.AnalysisOperations",
        "GetIthPointFromGroup",
        "analysis_operations.get_ith_point_from_group",
    ),
    (
        "get_line_properties",
        "briosa.AnalysisOperations",
        "GetLineProperties",
        "analysis_operations.get_line_properties",
    ),
    (
        "get_measurement_auxiliary_data",
        "briosa.AnalysisOperations",
        "GetMeasurementAuxiliaryData",
        "analysis_operations.get_measurement_auxiliary_data",
    ),
    (
        "get_measurement_info_data",
        "briosa.AnalysisOperations",
        "GetMeasurementInfoData",
        "analysis_operations.get_measurement_info_data",
    ),
    (
        "get_measurement_weather_data",
        "briosa.AnalysisOperations",
        "GetMeasurementWeatherData",
        "analysis_operations.get_measurement_weather_data",
    ),
    (
        "get_number_of_collections",
        "briosa.AnalysisOperations",
        "GetNumberOfCollections",
        "analysis_operations.get_number_of_collections",
    ),
    (
        "get_number_of_frames_in_frame_set",
        "briosa.AnalysisOperations",
        "GetNumberOfFramesInFrameSet",
        "analysis_operations.get_number_of_frames_in_frame_set",
    ),
    (
        "get_number_of_points_in_group",
        "briosa.AnalysisOperations",
        "GetNumberOfPointsInGroup",
        "analysis_operations.get_number_of_points_in_group",
    ),
    (
        "get_number_of_points_in_point_set",
        "briosa.AnalysisOperations",
        "GetNumberOfPointsInPointSet",
        "analysis_operations.get_number_of_points_in_point_set",
    ),
    (
        "get_object_reporting_frame",
        "briosa.AnalysisOperations",
        "GetObjectReportingFrame",
        "analysis_operations.get_object_reporting_frame",
    ),
    (
        "get_plane_properties",
        "briosa.AnalysisOperations",
        "GetPlaneProperties",
        "analysis_operations.get_plane_properties",
    ),
    (
        "get_point_coordinate",
        "briosa.AnalysisOperations",
        "GetPointCoordinate",
        "analysis_operations.get_point_coordinate",
    ),
    (
        "get_point_coordinate_cylindrical",
        "briosa.AnalysisOperations",
        "GetPointCoordinateCylindrical",
        "analysis_operations.get_point_coordinate_cylindrical",
    ),
    (
        "get_point_coordinate_polar",
        "briosa.AnalysisOperations",
        "GetPointCoordinatePolar",
        "analysis_operations.get_point_coordinate_polar",
    ),
    (
        "get_point_properties",
        "briosa.AnalysisOperations",
        "GetPointProperties",
        "analysis_operations.get_point_properties",
    ),
    (
        "get_point_to_line_distance",
        "briosa.AnalysisOperations",
        "GetPointToLineDistance",
        "analysis_operations.get_point_to_line_distance",
    ),
    (
        "get_point_to_point_distance",
        "briosa.AnalysisOperations",
        "GetPointToPointDistance",
        "analysis_operations.get_point_to_point_distance",
    ),
    (
        "get_point_tolerance",
        "briosa.AnalysisOperations",
        "GetPointTolerance",
        "analysis_operations.get_point_tolerance",
    ),
    (
        "get_slot_properties",
        "briosa.AnalysisOperations",
        "GetSlotProperties",
        "analysis_operations.get_slot_properties",
    ),
    (
        "get_sphere_properties",
        "briosa.AnalysisOperations",
        "GetSphereProperties",
        "analysis_operations.get_sphere_properties",
    ),
    (
        "get_surface_physical_stats",
        "briosa.AnalysisOperations",
        "GetSurfacePhysicalStats",
        "analysis_operations.get_surface_physical_stats",
    ),
    (
        "get_timestamp_for_ith_frame_in_frame_set",
        "briosa.AnalysisOperations",
        "GetTimestampForIthFrameInFrameSet",
        "analysis_operations.get_timestamp_for_ith_frame_in_frame_set",
    ),
    (
        "get_timestamp_for_ith_point_in_point_set",
        "briosa.AnalysisOperations",
        "GetTimestampForIthPointInPointSet",
        "analysis_operations.get_timestamp_for_ith_point_in_point_set",
    ),
    (
        "get_torus_properties",
        "briosa.AnalysisOperations",
        "GetTorusProperties",
        "analysis_operations.get_torus_properties",
    ),
    (
        "get_transform_for_ith_frame_in_frame_set",
        "briosa.AnalysisOperations",
        "GetTransformForIthFrameInFrameSet",
        "analysis_operations.get_transform_for_ith_frame_in_frame_set",
    ),
    (
        "group_to_surface_fit",
        "briosa.AnalysisOperations",
        "GroupToSurfaceFit",
        "analysis_operations.group_to_surface_fit",
    ),
    (
        "import_geometry_fit_profiles",
        "briosa.AnalysisOperations",
        "ImportGeometryFitProfiles",
        "analysis_operations.import_geometry_fit_profiles",
    ),
    (
        "is_object_of_type",
        "briosa.AnalysisOperations",
        "IsObjectOfType",
        "analysis_operations.is_object_of_type",
    ),
    (
        "make_circle_fit_profile",
        "briosa.AnalysisOperations",
        "MakeCircleFitProfile",
        "analysis_operations.make_circle_fit_profile",
    ),
    (
        "make_cone_fit_profile",
        "briosa.AnalysisOperations",
        "MakeConeFitProfile",
        "analysis_operations.make_cone_fit_profile",
    ),
    (
        "make_cylinder_fit_profile",
        "briosa.AnalysisOperations",
        "MakeCylinderFitProfile",
        "analysis_operations.make_cylinder_fit_profile",
    ),
    (
        "make_ellipse_fit_profile",
        "briosa.AnalysisOperations",
        "MakeEllipseFitProfile",
        "analysis_operations.make_ellipse_fit_profile",
    ),
    (
        "make_line_fit_profile",
        "briosa.AnalysisOperations",
        "MakeLineFitProfile",
        "analysis_operations.make_line_fit_profile",
    ),
    (
        "make_paraboloid_fit_profile",
        "briosa.AnalysisOperations",
        "MakeParaboloidFitProfile",
        "analysis_operations.make_paraboloid_fit_profile",
    ),
    (
        "make_plane_fit_profile",
        "briosa.AnalysisOperations",
        "MakePlaneFitProfile",
        "analysis_operations.make_plane_fit_profile",
    ),
    (
        "make_slot_fit_profile",
        "briosa.AnalysisOperations",
        "MakeSlotFitProfile",
        "analysis_operations.make_slot_fit_profile",
    ),
    (
        "make_sphere_fit_profile",
        "briosa.AnalysisOperations",
        "MakeSphereFitProfile",
        "analysis_operations.make_sphere_fit_profile",
    ),
    (
        "mushroom_target_hole_inspection",
        "briosa.AnalysisOperations",
        "MushroomTargetHoleInspection",
        "analysis_operations.mushroom_target_hole_inspection",
    ),
    (
        "patch_normal_shift_hole_pin",
        "briosa.AnalysisOperations",
        "PatchNormalShiftHolePin",
        "analysis_operations.patch_normal_shift_hole_pin",
    ),
    (
        "patch_normal_shift_point",
        "briosa.AnalysisOperations",
        "PatchNormalShiftPoint",
        "analysis_operations.patch_normal_shift_point",
    ),
    (
        "query_clouds_to_objects",
        "briosa.AnalysisOperations",
        "QueryCloudsToObjects",
        "analysis_operations.query_clouds_to_objects",
    ),
    (
        "query_clouds_to_surface",
        "briosa.AnalysisOperations",
        "QueryCloudsToSurface",
        "analysis_operations.query_clouds_to_surface",
    ),
    (
        "query_frame_to_frame",
        "briosa.AnalysisOperations",
        "QueryFrameToFrame",
        "analysis_operations.query_frame_to_frame",
    ),
    (
        "query_groups_to_objects",
        "briosa.AnalysisOperations",
        "QueryGroupsToObjects",
        "analysis_operations.query_groups_to_objects",
    ),
    (
        "query_point_to_objects",
        "briosa.AnalysisOperations",
        "QueryPointToObjects",
        "analysis_operations.query_point_to_objects",
    ),
    (
        "query_point_to_point_along_curve",
        "briosa.AnalysisOperations",
        "QueryPointToPointAlongCurve",
        "analysis_operations.query_point_to_point_along_curve",
    ),
    (
        "query_points_to_circle",
        "briosa.AnalysisOperations",
        "QueryPointsToCircle",
        "analysis_operations.query_points_to_circle",
    ),
    (
        "query_points_to_objects",
        "briosa.AnalysisOperations",
        "QueryPointsToObjects",
        "analysis_operations.query_points_to_objects",
    ),
    (
        "query_points_to_single_point",
        "briosa.AnalysisOperations",
        "QueryPointsToSinglePoint",
        "analysis_operations.query_points_to_single_point",
    ),
    (
        "re_compute_calculated_items",
        "briosa.AnalysisOperations",
        "ReComputeCalculatedItems",
        "analysis_operations.re_compute_calculated_items",
    ),
    (
        "rename_points_based_on_inter_point_distance_to_reference_points",
        "briosa.AnalysisOperations",
        "RenamePointsBasedOnInterPointDistanceToReferencePoints",
        "analysis_operations.rename_points_based_on_inter_point_distance_to_reference_points",
    ),
    (
        "rename_points_based_on_proximity_to_reference_points",
        "briosa.AnalysisOperations",
        "RenamePointsBasedOnProximityToReferencePoints",
        "analysis_operations.rename_points_based_on_proximity_to_reference_points",
    ),
    (
        "reverse_bsplines",
        "briosa.AnalysisOperations",
        "ReverseBSplines",
        "analysis_operations.reverse_bsplines",
    ),
    (
        "reverse_plane_normals",
        "briosa.AnalysisOperations",
        "ReversePlaneNormals",
        "analysis_operations.reverse_plane_normals",
    ),
    (
        "reverse_surface_normals",
        "briosa.AnalysisOperations",
        "ReverseSurfaceNormals",
        "analysis_operations.reverse_surface_normals",
    ),
    (
        "set_circle_properties",
        "briosa.AnalysisOperations",
        "SetCircleProperties",
        "analysis_operations.set_circle_properties",
    ),
    (
        "set_cone_properties",
        "briosa.AnalysisOperations",
        "SetConeProperties",
        "analysis_operations.set_cone_properties",
    ),
    (
        "set_cylinder_properties",
        "briosa.AnalysisOperations",
        "SetCylinderProperties",
        "analysis_operations.set_cylinder_properties",
    ),
    (
        "set_default_colorization_options",
        "briosa.AnalysisOperations",
        "SetDefaultColorizationOptions",
        "analysis_operations.set_default_colorization_options",
    ),
    (
        "set_ellipse_properties",
        "briosa.AnalysisOperations",
        "SetEllipseProperties",
        "analysis_operations.set_ellipse_properties",
    ),
    (
        "set_geometry_relationship_fit_profile",
        "briosa.AnalysisOperations",
        "SetGeometryRelationshipFitProfile",
        "analysis_operations.set_geometry_relationship_fit_profile",
    ),
    (
        "set_line_properties",
        "briosa.AnalysisOperations",
        "SetLineProperties",
        "analysis_operations.set_line_properties",
    ),
    (
        "set_measurement_auxiliary_data",
        "briosa.AnalysisOperations",
        "SetMeasurementAuxiliaryData",
        "analysis_operations.set_measurement_auxiliary_data",
    ),
    (
        "set_object_reporting_frame",
        "briosa.AnalysisOperations",
        "SetObjectReportingFrame",
        "analysis_operations.set_object_reporting_frame",
    ),
    (
        "set_point_properties",
        "briosa.AnalysisOperations",
        "SetPointProperties",
        "analysis_operations.set_point_properties",
    ),
    (
        "set_point_weights_from_uncertainties",
        "briosa.AnalysisOperations",
        "SetPointWeightsFromUncertainties",
        "analysis_operations.set_point_weights_from_uncertainties",
    ),
    (
        "set_transform_for_ith_frame_in_frame_set",
        "briosa.AnalysisOperations",
        "SetTransformForIthFrameInFrameSet",
        "analysis_operations.set_transform_for_ith_frame_in_frame_set",
    ),
    (
        "sphere_axis_check",
        "briosa.AnalysisOperations",
        "SphereAxisCheck",
        "analysis_operations.sphere_axis_check",
    ),
    (
        "temperature_compensate_a_group",
        "briosa.AnalysisOperations",
        "TemperatureCompensateAGroup",
        "analysis_operations.temperature_compensate_a_group",
    ),
    (
        "transform_objects_frame_to_frame",
        "briosa.AnalysisOperations",
        "TransformObjectsFrameToFrame",
        "analysis_operations.transform_objects_frame_to_frame",
    ),
    (
        "transform_objects_by_delta_about_working_frame",
        "briosa.AnalysisOperations",
        "TransformObjectsByDeltaAboutWorkingFrame",
        "analysis_operations.transform_objects_by_delta_about_working_frame",
    ),
    (
        "transform_objects_by_delta_world_transform_operator",
        "briosa.AnalysisOperations",
        "TransformObjectsByDeltaWorldTransformOperator",
        "analysis_operations.transform_objects_by_delta_world_transform_operator",
    ),
    (
        "translate_objects_by_delta",
        "briosa.AnalysisOperations",
        "TranslateObjectsByDelta",
        "analysis_operations.translate_objects_by_delta",
    ),
    (
        "delete_dimension",
        "briosa.DimensionOperations",
        "DeleteDimension",
        "dimension_operations.delete_dimension",
    ),
    (
        "get_dimension_value",
        "briosa.DimensionOperations",
        "GetDimensionValue",
        "dimension_operations.get_dimension_value",
    ),
    (
        "set_dimension_tolerance",
        "briosa.DimensionOperations",
        "SetDimensionTolerance",
        "dimension_operations.set_dimension_tolerance",
    ),
    (
        "delete_event",
        "briosa.EventOperations",
        "DeleteEvent",
        "event_operations.delete_event",
    ),
    (
        "export_event_ref_list",
        "briosa.EventOperations",
        "ExportEventRefList",
        "event_operations.export_event_ref_list",
    ),
    (
        "get_ith_event_from_event_ref_list",
        "briosa.EventOperations",
        "GetIthEventFromEventRefList",
        "event_operations.get_ith_event_from_event_ref_list",
    ),
    (
        "get_number_of_events_in_event_ref_list",
        "briosa.EventOperations",
        "GetNumberOfEventsInEventRefList",
        "event_operations.get_number_of_events_in_event_ref_list",
    ),
    (
        "rename_event",
        "briosa.EventOperations",
        "RenameEvent",
        "event_operations.rename_event",
    ),
    ("backup_now", "briosa.FileOperations", "BackupNow", "file_operations.backup_now"),
    (
        "copy_general_file",
        "briosa.FileOperations",
        "CopyGeneralFile",
        "file_operations.copy_general_file",
    ),
    (
        "delete_general_file",
        "briosa.FileOperations",
        "DeleteGeneralFile",
        "file_operations.delete_general_file",
    ),
    (
        "direct_cad_access",
        "briosa.FileOperations",
        "DirectCadAccess",
        "file_operations.direct_cad_access",
    ),
    (
        "export_ascii_frame_set",
        "briosa.FileOperations",
        "ExportAsciiFrameSet",
        "file_operations.export_ascii_frame_set",
    ),
    (
        "export_ascii_frames",
        "briosa.FileOperations",
        "ExportAsciiFrames",
        "file_operations.export_ascii_frames",
    ),
    (
        "export_ascii_point_clouds",
        "briosa.FileOperations",
        "ExportAsciiPointClouds",
        "file_operations.export_ascii_point_clouds",
    ),
    (
        "export_ascii_point_set",
        "briosa.FileOperations",
        "ExportAsciiPointSet",
        "file_operations.export_ascii_point_set",
    ),
    (
        "export_ascii_points",
        "briosa.FileOperations",
        "ExportAsciiPoints",
        "file_operations.export_ascii_points",
    ),
    ("export_dxf", "briosa.FileOperations", "ExportDxf", "file_operations.export_dxf"),
    (
        "export_embedded_file",
        "briosa.FileOperations",
        "ExportEmbeddedFile",
        "file_operations.export_embedded_file",
    ),
    (
        "export_hidden_point_bar_xml_file",
        "briosa.FileOperations",
        "ExportHiddenPointBarXmlFile",
        "file_operations.export_hidden_point_bar_xml_file",
    ),
    (
        "export_iges_file_entire_model",
        "briosa.FileOperations",
        "ExportIgesFileEntireModel",
        "file_operations.export_iges_file_entire_model",
    ),
    (
        "export_iges_file_partial_model",
        "briosa.FileOperations",
        "ExportIgesFilePartialModel",
        "file_operations.export_iges_file_partial_model",
    ),
    (
        "export_ptx_point_clouds",
        "briosa.FileOperations",
        "ExportPtxPointClouds",
        "file_operations.export_ptx_point_clouds",
    ),
    (
        "export_qdas_characteristics",
        "briosa.FileOperations",
        "ExportQdasCharacteristics",
        "file_operations.export_qdas_characteristics",
    ),
    (
        "export_qdas_data_list",
        "briosa.FileOperations",
        "ExportQdasDataList",
        "file_operations.export_qdas_data_list",
    ),
    (
        "export_scan_stripe_mesh_to_stl_file",
        "briosa.FileOperations",
        "ExportScanStripeMeshToStlFile",
        "file_operations.export_scan_stripe_mesh_to_stl_file",
    ),
    (
        "export_step_file_entire_model",
        "briosa.FileOperations",
        "ExportStepFileEntireModel",
        "file_operations.export_step_file_entire_model",
    ),
    (
        "export_step_file_partial_model",
        "briosa.FileOperations",
        "ExportStepFilePartialModel",
        "file_operations.export_step_file_partial_model",
    ),
    (
        "export_vda_fs_file_entire_model",
        "briosa.FileOperations",
        "ExportVdaFsFileEntireModel",
        "file_operations.export_vda_fs_file_entire_model",
    ),
    (
        "export_vda_fs_file_partial_model",
        "briosa.FileOperations",
        "ExportVdaFsFilePartialModel",
        "file_operations.export_vda_fs_file_partial_model",
    ),
    (
        "export_vector_container_to_ascii_file",
        "briosa.FileOperations",
        "ExportVectorContainerToAsciiFile",
        "file_operations.export_vector_container_to_ascii_file",
    ),
    (
        "find_files_in_directory",
        "briosa.FileOperations",
        "FindFilesInDirectory",
        "file_operations.find_files_in_directory",
    ),
    (
        "find_sub_directories_in_directory",
        "briosa.FileOperations",
        "FindSubDirectoriesInDirectory",
        "file_operations.find_sub_directories_in_directory",
    ),
    (
        "get_boolean_from_data_share_file",
        "briosa.FileOperations",
        "GetBooleanFromDataShareFile",
        "file_operations.get_boolean_from_data_share_file",
    ),
    (
        "get_double_from_data_share_file",
        "briosa.FileOperations",
        "GetDoubleFromDataShareFile",
        "file_operations.get_double_from_data_share_file",
    ),
    (
        "get_integer_from_data_share_file",
        "briosa.FileOperations",
        "GetIntegerFromDataShareFile",
        "file_operations.get_integer_from_data_share_file",
    ),
    (
        "get_qdas_catalog_entries",
        "briosa.FileOperations",
        "GetQdasCatalogEntries",
        "file_operations.get_qdas_catalog_entries",
    ),
    (
        "get_string_from_data_share_file",
        "briosa.FileOperations",
        "GetStringFromDataShareFile",
        "file_operations.get_string_from_data_share_file",
    ),
    (
        "get_transform_from_data_share_file",
        "briosa.FileOperations",
        "GetTransformFromDataShareFile",
        "file_operations.get_transform_from_data_share_file",
    ),
    (
        "get_vector_from_data_share_file",
        "briosa.FileOperations",
        "GetVectorFromDataShareFile",
        "file_operations.get_vector_from_data_share_file",
    ),
    (
        "get_working_directory",
        "briosa.FileOperations",
        "GetWorkingDirectory",
        "file_operations.get_working_directory",
    ),
    (
        "import_ascii_predefined_formats",
        "briosa.FileOperations",
        "ImportAsciiPredefinedFormats",
        "file_operations.import_ascii_predefined_formats",
    ),
    (
        "import_ascii_predefined_frame_set_formats",
        "briosa.FileOperations",
        "ImportAsciiPredefinedFrameSetFormats",
        "file_operations.import_ascii_predefined_frame_set_formats",
    ),
    (
        "import_e57_file",
        "briosa.FileOperations",
        "ImportE57File",
        "file_operations.import_e57_file",
    ),
    (
        "import_file_as_embedded_file",
        "briosa.FileOperations",
        "ImportFileAsEmbeddedFile",
        "file_operations.import_file_as_embedded_file",
    ),
    (
        "import_file_as_picture",
        "briosa.FileOperations",
        "ImportFileAsPicture",
        "file_operations.import_file_as_picture",
    ),
    (
        "import_hidden_point_bar_xml_file",
        "briosa.FileOperations",
        "ImportHiddenPointBarXmlFile",
        "file_operations.import_hidden_point_bar_xml_file",
    ),
    (
        "import_iges_file",
        "briosa.FileOperations",
        "ImportIgesFile",
        "file_operations.import_iges_file",
    ),
    (
        "import_leica_gsi_file",
        "briosa.FileOperations",
        "ImportLeicaGsiFile",
        "file_operations.import_leica_gsi_file",
    ),
    (
        "import_leica_sdb_file",
        "briosa.FileOperations",
        "ImportLeicaSdbFile",
        "file_operations.import_leica_sdb_file",
    ),
    (
        "import_mp_file_as_embedded_mp",
        "briosa.FileOperations",
        "ImportMpFileAsEmbeddedMp",
        "file_operations.import_mp_file_as_embedded_mp",
    ),
    (
        "import_nominals_from_xml_file",
        "briosa.FileOperations",
        "ImportNominalsFromXmlFile",
        "file_operations.import_nominals_from_xml_file",
    ),
    (
        "import_polyworks_file",
        "briosa.FileOperations",
        "ImportPolyworksFile",
        "file_operations.import_polyworks_file",
    ),
    (
        "import_qdas_catalog_file",
        "briosa.FileOperations",
        "ImportQdasCatalogFile",
        "file_operations.import_qdas_catalog_file",
    ),
    (
        "import_sa_file",
        "briosa.FileOperations",
        "ImportSaFile",
        "file_operations.import_sa_file",
    ),
    (
        "import_sa_windows_placement",
        "briosa.FileOperations",
        "ImportSaWindowsPlacement",
        "file_operations.import_sa_windows_placement",
    ),
    (
        "import_sat_file",
        "briosa.FileOperations",
        "ImportSatFile",
        "file_operations.import_sat_file",
    ),
    (
        "import_step_file",
        "briosa.FileOperations",
        "ImportStepFile",
        "file_operations.import_step_file",
    ),
    (
        "import_stl_file",
        "briosa.FileOperations",
        "ImportStlFile",
        "file_operations.import_stl_file",
    ),
    (
        "import_vda_fs_file",
        "briosa.FileOperations",
        "ImportVdaFsFile",
        "file_operations.import_vda_fs_file",
    ),
    (
        "import_vstars_xyz_file",
        "briosa.FileOperations",
        "ImportVstarsXyzFile",
        "file_operations.import_vstars_xyz_file",
    ),
    (
        "import_vstars_cameras",
        "briosa.FileOperations",
        "ImportVstarsCameras",
        "file_operations.import_vstars_cameras",
    ),
    (
        "load_html_form",
        "briosa.FileOperations",
        "LoadHtmlForm",
        "file_operations.load_html_form",
    ),
    (
        "load_html_form_in_edge_browser",
        "briosa.FileOperations",
        "LoadHtmlFormInEdgeBrowser",
        "file_operations.load_html_form_in_edge_browser",
    ),
    (
        "make_embedded_file_name_list",
        "briosa.FileOperations",
        "MakeEmbeddedFileNameList",
        "file_operations.make_embedded_file_name_list",
    ),
    (
        "merge_measurements_into_xml_file",
        "briosa.FileOperations",
        "MergeMeasurementsIntoXmlFile",
        "file_operations.merge_measurements_into_xml_file",
    ),
    (
        "new_sa_file",
        "briosa.FileOperations",
        "NewSaFile",
        "file_operations.new_sa_file",
    ),
    (
        "open_sa_file",
        "briosa.FileOperations",
        "OpenSaFile",
        "file_operations.open_sa_file",
    ),
    (
        "open_template_file",
        "briosa.FileOperations",
        "OpenTemplateFile",
        "file_operations.open_template_file",
    ),
    (
        "pop_poly_bay_analysis_window",
        "briosa.FileOperations",
        "PopPolyBayAnalysisWindow",
        "file_operations.pop_poly_bay_analysis_window",
    ),
    (
        "prepare_qdas_data_list",
        "briosa.FileOperations",
        "PrepareQdasDataList",
        "file_operations.prepare_qdas_data_list",
    ),
    (
        "rename_general_file",
        "briosa.FileOperations",
        "RenameGeneralFile",
        "file_operations.rename_general_file",
    ),
    ("save", "briosa.FileOperations", "Save", "file_operations.save"),
    (
        "save_as_read_only_template",
        "briosa.FileOperations",
        "SaveAsReadOnlyTemplate",
        "file_operations.save_as_read_only_template",
    ),
    ("save_as", "briosa.FileOperations", "SaveAs", "file_operations.save_as"),
    (
        "set_boolean_in_data_share_file",
        "briosa.FileOperations",
        "SetBooleanInDataShareFile",
        "file_operations.set_boolean_in_data_share_file",
    ),
    (
        "set_double_in_data_share_file",
        "briosa.FileOperations",
        "SetDoubleInDataShareFile",
        "file_operations.set_double_in_data_share_file",
    ),
    (
        "set_integer_in_data_share_file",
        "briosa.FileOperations",
        "SetIntegerInDataShareFile",
        "file_operations.set_integer_in_data_share_file",
    ),
    (
        "set_string_in_data_share_file",
        "briosa.FileOperations",
        "SetStringInDataShareFile",
        "file_operations.set_string_in_data_share_file",
    ),
    (
        "set_transform_in_data_share_file",
        "briosa.FileOperations",
        "SetTransformInDataShareFile",
        "file_operations.set_transform_in_data_share_file",
    ),
    (
        "set_vector_in_data_share_file",
        "briosa.FileOperations",
        "SetVectorInDataShareFile",
        "file_operations.set_vector_in_data_share_file",
    ),
    (
        "terminate_all_running_mps",
        "briosa.FileOperations",
        "TerminateAllRunningMPs",
        "file_operations.terminate_all_running_mps",
    ),
    (
        "use_nrkxml_library",
        "briosa.FileOperations",
        "UseNrkxmlLibrary",
        "file_operations.use_nrkxml_library",
    ),
    (
        "verify_general_file_exists",
        "briosa.FileOperations",
        "VerifyGeneralFileExists",
        "file_operations.verify_general_file_exists",
    ),
    (
        "verify_mp_file_exists",
        "briosa.FileOperations",
        "VerifyMpFileExists",
        "file_operations.verify_mp_file_exists",
    ),
    (
        "run_subroutine",
        "briosa.MpSubroutines",
        "RunSubroutine",
        "mp_subroutines.run_subroutine",
    ),
    (
        "add_task_overview_item",
        "briosa.MpTaskOverview",
        "AddTaskOverviewItem",
        "mp_task_overview.add_task_overview_item",
    ),
    (
        "create_clear_task_overview_list",
        "briosa.MpTaskOverview",
        "CreateClearTaskOverviewList",
        "mp_task_overview.create_clear_task_overview_list",
    ),
    (
        "set_current_task",
        "briosa.MpTaskOverview",
        "SetCurrentTask",
        "mp_task_overview.set_current_task",
    ),
    (
        "set_overview_image",
        "briosa.MpTaskOverview",
        "SetOverviewImage",
        "mp_task_overview.set_overview_image",
    ),
    (
        "set_overview_title",
        "briosa.MpTaskOverview",
        "SetOverviewTitle",
        "mp_task_overview.set_overview_title",
    ),
    (
        "set_task_item_comment",
        "briosa.MpTaskOverview",
        "SetTaskItemComment",
        "mp_task_overview.set_task_item_comment",
    ),
    (
        "set_task_item_completion_values",
        "briosa.MpTaskOverview",
        "SetTaskItemCompletionValues",
        "mp_task_overview.set_task_item_completion_values",
    ),
    (
        "set_task_item_name",
        "briosa.MpTaskOverview",
        "SetTaskItemName",
        "mp_task_overview.set_task_item_name",
    ),
    (
        "show_progress_for_task_item",
        "briosa.MpTaskOverview",
        "ShowProgressForTaskItem",
        "mp_task_overview.show_progress_for_task_item",
    ),
    (
        "show_task_overview_list",
        "briosa.MpTaskOverview",
        "ShowTaskOverviewList",
        "mp_task_overview.show_task_overview_list",
    ),
    (
        "ask_for_double",
        "briosa.ProcessFlowOperations",
        "AskForDouble",
        "process_flow_operations.ask_for_double",
    ),
    (
        "ask_for_integer",
        "briosa.ProcessFlowOperations",
        "AskForInteger",
        "process_flow_operations.ask_for_integer",
    ),
    (
        "ask_for_point_name",
        "briosa.ProcessFlowOperations",
        "AskForPointName",
        "process_flow_operations.ask_for_point_name",
    ),
    (
        "ask_for_string",
        "briosa.ProcessFlowOperations",
        "AskForString",
        "process_flow_operations.ask_for_string",
    ),
    (
        "ask_for_string_pull_down_version",
        "briosa.ProcessFlowOperations",
        "AskForStringPullDownVersion",
        "process_flow_operations.ask_for_string_pull_down_version",
    ),
    (
        "ask_for_user_decision_from_image",
        "briosa.ProcessFlowOperations",
        "AskForUserDecisionFromImage",
        "process_flow_operations.ask_for_user_decision_from_image",
    ),
    (
        "ask_for_user_decision_from_strings",
        "briosa.ProcessFlowOperations",
        "AskForUserDecisionFromStrings",
        "process_flow_operations.ask_for_user_decision_from_strings",
    ),
    (
        "object_existence_test_check_only",
        "briosa.ProcessFlowOperations",
        "ObjectExistenceTestCheckOnly",
        "process_flow_operations.object_existence_test_check_only",
    ),
    (
        "enable_disable_relationships_for_optimization",
        "briosa.RelationshipOperations",
        "EnableDisableRelationshipsForOptimization",
        "relationship_operations.enable_disable_relationships_for_optimization",
    ),
    (
        "geom_relationship_ignore_input_points",
        "briosa.RelationshipOperations",
        "GeomRelationshipIgnoreInputPoints",
        "relationship_operations.geom_relationship_ignore_input_points",
    ),
    (
        "geom_relationship_reuse_ignored_input_points",
        "briosa.RelationshipOperations",
        "GeomRelationshipReuseIgnoredInputPoints",
        "relationship_operations.geom_relationship_reuse_ignored_input_points",
    ),
    (
        "get_geom_relationship_auto_vectors",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipAutoVectors",
        "relationship_operations.get_geom_relationship_auto_vectors",
    ),
    (
        "get_geom_relationship_cardinal_points",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipCardinalPoints",
        "relationship_operations.get_geom_relationship_cardinal_points",
    ),
    (
        "get_geom_relationship_criteria",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipCriteria",
        "relationship_operations.get_geom_relationship_criteria",
    ),
    (
        "get_geom_relationship_measured_avg_point",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipMeasuredAvgPoint",
        "relationship_operations.get_geom_relationship_measured_avg_point",
    ),
    (
        "get_geom_relationship_measured_geometry",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipMeasuredGeometry",
        "relationship_operations.get_geom_relationship_measured_geometry",
    ),
    (
        "get_geom_relationship_nominal_avg_point",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipNominalAvgPoint",
        "relationship_operations.get_geom_relationship_nominal_avg_point",
    ),
    (
        "get_geom_relationship_nominal_geometry",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipNominalGeometry",
        "relationship_operations.get_geom_relationship_nominal_geometry",
    ),
    (
        "get_geom_relationship_point_list",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipPointList",
        "relationship_operations.get_geom_relationship_point_list",
    ),
    (
        "get_geom_relationship_projection_plane",
        "briosa.RelationshipOperations",
        "GetGeomRelationshipProjectionPlane",
        "relationship_operations.get_geom_relationship_projection_plane",
    ),
    (
        "get_pipe_relationship_cut_status",
        "briosa.RelationshipOperations",
        "GetPipeRelationshipCutStatus",
        "relationship_operations.get_pipe_relationship_cut_status",
    ),
    (
        "get_pipe_relationship_properties",
        "briosa.RelationshipOperations",
        "GetPipeRelationshipProperties",
        "relationship_operations.get_pipe_relationship_properties",
    ),
    (
        "get_pipe_relationship_weights",
        "briosa.RelationshipOperations",
        "GetPipeRelationshipWeights",
        "relationship_operations.get_pipe_relationship_weights",
    ),
    (
        "get_relationship_fit_constraints_scalar_type",
        "briosa.RelationshipOperations",
        "GetRelationshipFitConstraintsScalarType",
        "relationship_operations.get_relationship_fit_constraints_scalar_type",
    ),
    (
        "get_relationship_outlier_rejection_scalar_type",
        "briosa.RelationshipOperations",
        "GetRelationshipOutlierRejectionScalarType",
        "relationship_operations.get_relationship_outlier_rejection_scalar_type",
    ),
    (
        "get_relationship_projection_options",
        "briosa.RelationshipOperations",
        "GetRelationshipProjectionOptions",
        "relationship_operations.get_relationship_projection_options",
    ),
    (
        "get_relationship_reporting_frame",
        "briosa.RelationshipOperations",
        "GetRelationshipReportingFrame",
        "relationship_operations.get_relationship_reporting_frame",
    ),
    (
        "get_relationship_sub_sampling_options",
        "briosa.RelationshipOperations",
        "GetRelationshipSubSamplingOptions",
        "relationship_operations.get_relationship_sub_sampling_options",
    ),
    (
        "get_relationship_tolerance_scalar_type",
        "briosa.RelationshipOperations",
        "GetRelationshipToleranceScalarType",
        "relationship_operations.get_relationship_tolerance_scalar_type",
    ),
    (
        "get_relationship_tolerance_vector_type",
        "briosa.RelationshipOperations",
        "GetRelationshipToleranceVectorType",
        "relationship_operations.get_relationship_tolerance_vector_type",
    ),
    (
        "get_relationship_type",
        "briosa.RelationshipOperations",
        "GetRelationshipType",
        "relationship_operations.get_relationship_type",
    ),
    (
        "get_relationship_weighting",
        "briosa.RelationshipOperations",
        "GetRelationshipWeighting",
        "relationship_operations.get_relationship_weighting",
    ),
    (
        "make_pipe_fitting_relationship",
        "briosa.RelationshipOperations",
        "MakePipeFittingRelationship",
        "relationship_operations.make_pipe_fitting_relationship",
    ),
    (
        "make_pipe_relationship_cut",
        "briosa.RelationshipOperations",
        "MakePipeRelationshipCut",
        "relationship_operations.make_pipe_relationship_cut",
    ),
    (
        "pipe_relationship_force_cut_to_frame",
        "briosa.RelationshipOperations",
        "PipeRelationshipForceCutToFrame",
        "relationship_operations.pipe_relationship_force_cut_to_frame",
    ),
    (
        "set_geom_relationship_auto_measure_nominal_feature",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipAutoMeasureNominalFeature",
        "relationship_operations.set_geom_relationship_auto_measure_nominal_feature",
    ),
    (
        "set_geom_relationship_auto_vectors_nominal_avn",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipAutoVectorsNominalAvn",
        "relationship_operations.set_geom_relationship_auto_vectors_nominal_avn",
    ),
    (
        "set_geom_relationship_cardinal_points",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipCardinalPoints",
        "relationship_operations.set_geom_relationship_cardinal_points",
    ),
    (
        "set_geom_relationship_criteria",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipCriteria",
        "relationship_operations.set_geom_relationship_criteria",
    ),
    (
        "set_geom_relationship_measured_geometry",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipMeasuredGeometry",
        "relationship_operations.set_geom_relationship_measured_geometry",
    ),
    (
        "set_geom_relationship_nominal_avg_point",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipNominalAvgPoint",
        "relationship_operations.set_geom_relationship_nominal_avg_point",
    ),
    (
        "set_geom_relationship_nominal_geometry",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipNominalGeometry",
        "relationship_operations.set_geom_relationship_nominal_geometry",
    ),
    (
        "set_geom_relationship_projection_plane",
        "briosa.RelationshipOperations",
        "SetGeomRelationshipProjectionPlane",
        "relationship_operations.set_geom_relationship_projection_plane",
    ),
    (
        "set_object_to_object_direction_relationship_fit_constraints",
        "briosa.RelationshipOperations",
        "SetObjectToObjectDirectionRelationshipFitConstraints",
        "relationship_operations.set_object_to_object_direction_relationship_fit_constraints",
    ),
    (
        "set_pipe_relationship_segment_properties",
        "briosa.RelationshipOperations",
        "SetPipeRelationshipSegmentProperties",
        "relationship_operations.set_pipe_relationship_segment_properties",
    ),
    (
        "set_pipe_relationship_weights",
        "briosa.RelationshipOperations",
        "SetPipeRelationshipWeights",
        "relationship_operations.set_pipe_relationship_weights",
    ),
    (
        "set_relationship_auto_vectors_fit_avf",
        "briosa.RelationshipOperations",
        "SetRelationshipAutoVectorsFitAvf",
        "relationship_operations.set_relationship_auto_vectors_fit_avf",
    ),
    (
        "set_relationship_auto_vectors_group_default_prefix",
        "briosa.RelationshipOperations",
        "SetRelationshipAutoVectorsGroupDefaultPrefix",
        "relationship_operations.set_relationship_auto_vectors_group_default_prefix",
    ),
    (
        "set_relationship_desired_meas_count",
        "briosa.RelationshipOperations",
        "SetRelationshipDesiredMeasCount",
        "relationship_operations.set_relationship_desired_meas_count",
    ),
    (
        "set_relationship_dormant_status",
        "briosa.RelationshipOperations",
        "SetRelationshipDormantStatus",
        "relationship_operations.set_relationship_dormant_status",
    ),
    (
        "set_relationship_fit_constraints_scalar_type",
        "briosa.RelationshipOperations",
        "SetRelationshipFitConstraintsScalarType",
        "relationship_operations.set_relationship_fit_constraints_scalar_type",
    ),
    (
        "set_relationship_orientation_fit_constraints_vector_type",
        "briosa.RelationshipOperations",
        "SetRelationshipOrientationFitConstraintsVectorType",
        "relationship_operations.set_relationship_orientation_fit_constraints_vector_type",
    ),
    (
        "set_relationship_outlier_rejection_scalar_type",
        "briosa.RelationshipOperations",
        "SetRelationshipOutlierRejectionScalarType",
        "relationship_operations.set_relationship_outlier_rejection_scalar_type",
    ),
    (
        "set_relationship_position_fit_constraints_vector_type",
        "briosa.RelationshipOperations",
        "SetRelationshipPositionFitConstraintsVectorType",
        "relationship_operations.set_relationship_position_fit_constraints_vector_type",
    ),
    (
        "set_relationship_projection_options",
        "briosa.RelationshipOperations",
        "SetRelationshipProjectionOptions",
        "relationship_operations.set_relationship_projection_options",
    ),
    (
        "set_relationship_reporting_frame",
        "briosa.RelationshipOperations",
        "SetRelationshipReportingFrame",
        "relationship_operations.set_relationship_reporting_frame",
    ),
    (
        "set_relationship_sigmoidal_gap_fit_constraints",
        "briosa.RelationshipOperations",
        "SetRelationshipSigmoidalGapFitConstraints",
        "relationship_operations.set_relationship_sigmoidal_gap_fit_constraints",
    ),
    (
        "set_relationship_sub_sampling_options",
        "briosa.RelationshipOperations",
        "SetRelationshipSubSamplingOptions",
        "relationship_operations.set_relationship_sub_sampling_options",
    ),
    (
        "set_relationship_tolerance_scalar_type",
        "briosa.RelationshipOperations",
        "SetRelationshipToleranceScalarType",
        "relationship_operations.set_relationship_tolerance_scalar_type",
    ),
    (
        "set_relationship_tolerance_vector_type",
        "briosa.RelationshipOperations",
        "SetRelationshipToleranceVectorType",
        "relationship_operations.set_relationship_tolerance_vector_type",
    ),
    (
        "set_relationship_voxel_cloud_display",
        "briosa.RelationshipOperations",
        "SetRelationshipVoxelCloudDisplay",
        "relationship_operations.set_relationship_voxel_cloud_display",
    ),
    (
        "set_relationship_weighting",
        "briosa.RelationshipOperations",
        "SetRelationshipWeighting",
        "relationship_operations.set_relationship_weighting",
    ),
    (
        "set_relationship_weights_normalized",
        "briosa.RelationshipOperations",
        "SetRelationshipWeightsNormalized",
        "relationship_operations.set_relationship_weights_normalized",
    ),
    (
        "add_charts_to_report_bar",
        "briosa.ReportingOperations",
        "AddChartsToReportBar",
        "reporting_operations.add_charts_to_report_bar",
    ),
    (
        "add_custom_table_to_sa_report",
        "briosa.ReportingOperations",
        "AddCustomTableToSaReport",
        "reporting_operations.add_custom_table_to_sa_report",
    ),
    (
        "add_custom_tables_to_report_bar",
        "briosa.ReportingOperations",
        "AddCustomTablesToReportBar",
        "reporting_operations.add_custom_tables_to_report_bar",
    ),
    (
        "add_datums_to_report_bar",
        "briosa.ReportingOperations",
        "AddDatumsToReportBar",
        "reporting_operations.add_datums_to_report_bar",
    ),
    (
        "add_events_to_report_bar",
        "briosa.ReportingOperations",
        "AddEventsToReportBar",
        "reporting_operations.add_events_to_report_bar",
    ),
    (
        "add_feature_checks_to_report_bar",
        "briosa.ReportingOperations",
        "AddFeatureChecksToReportBar",
        "reporting_operations.add_feature_checks_to_report_bar",
    ),
    (
        "add_item_to_sa_report_at_location",
        "briosa.ReportingOperations",
        "AddItemToSaReportAtLocation",
        "reporting_operations.add_item_to_sa_report_at_location",
    ),
    (
        "add_objects_to_report_bar",
        "briosa.ReportingOperations",
        "AddObjectsToReportBar",
        "reporting_operations.add_objects_to_report_bar",
    ),
    (
        "add_pictures_to_report_bar",
        "briosa.ReportingOperations",
        "AddPicturesToReportBar",
        "reporting_operations.add_pictures_to_report_bar",
    ),
    (
        "add_relationships_to_report_bar",
        "briosa.ReportingOperations",
        "AddRelationshipsToReportBar",
        "reporting_operations.add_relationships_to_report_bar",
    ),
    (
        "append_items_to_sa_report",
        "briosa.ReportingOperations",
        "AppendItemsToSaReport",
        "reporting_operations.append_items_to_sa_report",
    ),
    (
        "capture_current_view",
        "briosa.ReportingOperations",
        "CaptureCurrentView",
        "reporting_operations.capture_current_view",
    ),
    (
        "capture_screen_to_file_bmp_jpg_png_gif_tiff",
        "briosa.ReportingOperations",
        "CaptureScreenToFileBmpJpgPngGifTiff",
        "reporting_operations.capture_screen_to_file_bmp_jpg_png_gif_tiff",
    ),
    (
        "clear_custom_table",
        "briosa.ReportingOperations",
        "ClearCustomTable",
        "reporting_operations.clear_custom_table",
    ),
    (
        "close_all_reports",
        "briosa.ReportingOperations",
        "CloseAllReports",
        "reporting_operations.close_all_reports",
    ),
    (
        "close_html_display_board",
        "briosa.ReportingOperations",
        "CloseHtmlDisplayBoard",
        "reporting_operations.close_html_display_board",
    ),
    (
        "combine_sa_reports",
        "briosa.ReportingOperations",
        "CombineSaReports",
        "reporting_operations.combine_sa_reports",
    ),
    (
        "create_chart_from_vector_group",
        "briosa.ReportingOperations",
        "CreateChartFromVectorGroup",
        "reporting_operations.create_chart_from_vector_group",
    ),
    (
        "define_report_template",
        "briosa.ReportingOperations",
        "DefineReportTemplate",
        "reporting_operations.define_report_template",
    ),
    (
        "delete_chart",
        "briosa.ReportingOperations",
        "DeleteChart",
        "reporting_operations.delete_chart",
    ),
    (
        "delete_custom_table",
        "briosa.ReportingOperations",
        "DeleteCustomTable",
        "reporting_operations.delete_custom_table",
    ),
    (
        "delete_picture",
        "briosa.ReportingOperations",
        "DeletePicture",
        "reporting_operations.delete_picture",
    ),
    (
        "delete_sa_doc",
        "briosa.ReportingOperations",
        "DeleteSaDoc",
        "reporting_operations.delete_sa_doc",
    ),
    (
        "delete_sa_report",
        "briosa.ReportingOperations",
        "DeleteSaReport",
        "reporting_operations.delete_sa_report",
    ),
    (
        "delete_sa_report_template",
        "briosa.ReportingOperations",
        "DeleteSaReportTemplate",
        "reporting_operations.delete_sa_report_template",
    ),
    (
        "generate_quick_report_from_tab_order",
        "briosa.ReportingOperations",
        "GenerateQuickReportFromTabOrder",
        "reporting_operations.generate_quick_report_from_tab_order",
    ),
    (
        "generate_standard_html_report",
        "briosa.ReportingOperations",
        "GenerateStandardHtmlReport",
        "reporting_operations.generate_standard_html_report",
    ),
    (
        "generate_update_templated_report",
        "briosa.ReportingOperations",
        "GenerateUpdateTemplatedReport",
        "reporting_operations.generate_update_templated_report",
    ),
    (
        "get_custom_table_cell_double",
        "briosa.ReportingOperations",
        "GetCustomTableCellDouble",
        "reporting_operations.get_custom_table_cell_double",
    ),
    (
        "get_custom_table_cell_string",
        "briosa.ReportingOperations",
        "GetCustomTableCellString",
        "reporting_operations.get_custom_table_cell_string",
    ),
    (
        "get_defined_report_tags",
        "briosa.ReportingOperations",
        "GetDefinedReportTags",
        "reporting_operations.get_defined_report_tags",
    ),
    (
        "get_report_tag_value",
        "briosa.ReportingOperations",
        "GetReportTagValue",
        "reporting_operations.get_report_tag_value",
    ),
    (
        "html_display_board",
        "briosa.ReportingOperations",
        "HtmlDisplayBoard",
        "reporting_operations.html_display_board",
    ),
    (
        "make_custom_table",
        "briosa.ReportingOperations",
        "MakeCustomTable",
        "reporting_operations.make_custom_table",
    ),
    (
        "make_new_sa_report",
        "briosa.ReportingOperations",
        "MakeNewSaReport",
        "reporting_operations.make_new_sa_report",
    ),
    (
        "make_utility_chart",
        "briosa.ReportingOperations",
        "MakeUtilityChart",
        "reporting_operations.make_utility_chart",
    ),
    (
        "notify_user_double",
        "briosa.ReportingOperations",
        "NotifyUserDouble",
        "reporting_operations.notify_user_double",
    ),
    (
        "notify_user_html",
        "briosa.ReportingOperations",
        "NotifyUserHtml",
        "reporting_operations.notify_user_html",
    ),
    (
        "notify_user_integer",
        "briosa.ReportingOperations",
        "NotifyUserInteger",
        "reporting_operations.notify_user_integer",
    ),
    (
        "notify_user_text_array",
        "briosa.ReportingOperations",
        "NotifyUserTextArray",
        "reporting_operations.notify_user_text_array",
    ),
    (
        "output_sa_report_to_excel",
        "briosa.ReportingOperations",
        "OutputSaReportToExcel",
        "reporting_operations.output_sa_report_to_excel",
    ),
    (
        "output_sa_report_to_pdf",
        "briosa.ReportingOperations",
        "OutputSaReportToPdf",
        "reporting_operations.output_sa_report_to_pdf",
    ),
    (
        "quick_report",
        "briosa.ReportingOperations",
        "QuickReport",
        "reporting_operations.quick_report",
    ),
    (
        "refresh_callout_views_in_sa_report",
        "briosa.ReportingOperations",
        "RefreshCalloutViewsInSaReport",
        "reporting_operations.refresh_callout_views_in_sa_report",
    ),
    (
        "refresh_report_bar",
        "briosa.ReportingOperations",
        "RefreshReportBar",
        "reporting_operations.refresh_report_bar",
    ),
    (
        "remove_report_tag",
        "briosa.ReportingOperations",
        "RemoveReportTag",
        "reporting_operations.remove_report_tag",
    ),
    (
        "rename_picture",
        "briosa.ReportingOperations",
        "RenamePicture",
        "reporting_operations.rename_picture",
    ),
    (
        "save_chart_to_jpeg_file",
        "briosa.ReportingOperations",
        "SaveChartToJPegFile",
        "reporting_operations.save_chart_to_jpeg_file",
    ),
    (
        "save_current_view_bmp_jpg_png_gif_tiff",
        "briosa.ReportingOperations",
        "SaveCurrentViewBmpJpgPngGifTiff",
        "reporting_operations.save_current_view_bmp_jpg_png_gif_tiff",
    ),
    (
        "set_custom_table_cell_color",
        "briosa.ReportingOperations",
        "SetCustomTableCellColor",
        "reporting_operations.set_custom_table_cell_color",
    ),
    (
        "set_custom_table_cell_double",
        "briosa.ReportingOperations",
        "SetCustomTableCellDouble",
        "reporting_operations.set_custom_table_cell_double",
    ),
    (
        "set_custom_table_cell_font",
        "briosa.ReportingOperations",
        "SetCustomTableCellFont",
        "reporting_operations.set_custom_table_cell_font",
    ),
    (
        "set_custom_table_cell_string",
        "briosa.ReportingOperations",
        "SetCustomTableCellString",
        "reporting_operations.set_custom_table_cell_string",
    ),
    (
        "set_custom_table_header_cell",
        "briosa.ReportingOperations",
        "SetCustomTableHeaderCell",
        "reporting_operations.set_custom_table_header_cell",
    ),
    (
        "set_custom_table_header_row",
        "briosa.ReportingOperations",
        "SetCustomTableHeaderRow",
        "reporting_operations.set_custom_table_header_row",
    ),
    (
        "set_custom_table_title",
        "briosa.ReportingOperations",
        "SetCustomTableTitle",
        "reporting_operations.set_custom_table_title",
    ),
    (
        "set_point_group_report_options",
        "briosa.ReportingOperations",
        "SetPointGroupReportOptions",
        "reporting_operations.set_point_group_report_options",
    ),
    (
        "set_relationship_report_options",
        "briosa.ReportingOperations",
        "SetRelationshipReportOptions",
        "reporting_operations.set_relationship_report_options",
    ),
    (
        "set_report_bar_visibility",
        "briosa.ReportingOperations",
        "SetReportBarVisibility",
        "reporting_operations.set_report_bar_visibility",
    ),
    (
        "set_report_options_for_object",
        "briosa.ReportingOperations",
        "SetReportOptionsForObject",
        "reporting_operations.set_report_options_for_object",
    ),
    (
        "set_report_tag_value_from_double",
        "briosa.ReportingOperations",
        "SetReportTagValueFromDouble",
        "reporting_operations.set_report_tag_value_from_double",
    ),
    (
        "set_report_tag_value_from_integer",
        "briosa.ReportingOperations",
        "SetReportTagValueFromInteger",
        "reporting_operations.set_report_tag_value_from_integer",
    ),
    (
        "set_report_tag_value_from_string",
        "briosa.ReportingOperations",
        "SetReportTagValueFromString",
        "reporting_operations.set_report_tag_value_from_string",
    ),
    (
        "set_scale_for_picture",
        "briosa.ReportingOperations",
        "SetScaleForPicture",
        "reporting_operations.set_scale_for_picture",
    ),
    (
        "set_vector_group_report_options",
        "briosa.ReportingOperations",
        "SetVectorGroupReportOptions",
        "reporting_operations.set_vector_group_report_options",
    ),
    (
        "delete_scale_bar",
        "briosa.ScaleBarOperations",
        "DeleteScaleBar",
        "scale_bar_operations.delete_scale_bar",
    ),
    (
        "get_scale_bar_stats",
        "briosa.ScaleBarOperations",
        "GetScaleBarStats",
        "scale_bar_operations.get_scale_bar_stats",
    ),
    (
        "scale_bar_check",
        "briosa.ScaleBarOperations",
        "ScaleBarCheck",
        "scale_bar_operations.scale_bar_check",
    ),
    (
        "set_inward_positive_normal",
        "briosa.ScaleBarOperations",
        "SetInwardPositiveNormal",
        "scale_bar_operations.set_inward_positive_normal",
    ),
    (
        "close_all_watch_windows",
        "briosa.UtilityOperations",
        "CloseAllWatchWindows",
        "utility_operations.close_all_watch_windows",
    ),
    (
        "delete_folder",
        "briosa.UtilityOperations",
        "DeleteFolder",
        "utility_operations.delete_folder",
    ),
    (
        "delete_items",
        "briosa.UtilityOperations",
        "DeleteItems",
        "utility_operations.delete_items",
    ),
    (
        "delete_objects",
        "briosa.UtilityOperations",
        "DeleteObjects",
        "utility_operations.delete_objects",
    ),
    (
        "get_active_language",
        "briosa.UtilityOperations",
        "GetActiveLanguage",
        "utility_operations.get_active_language",
    ),
    (
        "get_active_units",
        "briosa.UtilityOperations",
        "GetActiveUnits",
        "utility_operations.get_active_units",
    ),
    (
        "get_angular_representation",
        "briosa.UtilityOperations",
        "GetAngularRepresentation",
        "utility_operations.get_angular_representation",
    ),
    (
        "get_collection_notes",
        "briosa.UtilityOperations",
        "GetCollectionNotes",
        "utility_operations.get_collection_notes",
    ),
    (
        "get_folder_collections",
        "briosa.UtilityOperations",
        "GetFolderCollections",
        "utility_operations.get_folder_collections",
    ),
    (
        "get_folder_notes",
        "briosa.UtilityOperations",
        "GetFolderNotes",
        "utility_operations.get_folder_notes",
    ),
    (
        "get_folders_by_wildcard",
        "briosa.UtilityOperations",
        "GetFoldersByWildcard",
        "utility_operations.get_folders_by_wildcard",
    ),
    (
        "get_object_notes",
        "briosa.UtilityOperations",
        "GetObjectNotes",
        "utility_operations.get_object_notes",
    ),
    (
        "get_opc_da_tag_value_double",
        "briosa.UtilityOperations",
        "GetOpcDaTagValueDouble",
        "utility_operations.get_opc_da_tag_value_double",
    ),
    (
        "get_opc_da_tag_value_integer",
        "briosa.UtilityOperations",
        "GetOpcDaTagValueInteger",
        "utility_operations.get_opc_da_tag_value_integer",
    ),
    (
        "get_opc_da_tag_value_string",
        "briosa.UtilityOperations",
        "GetOpcDaTagValueString",
        "utility_operations.get_opc_da_tag_value_string",
    ),
    (
        "get_point_notes",
        "briosa.UtilityOperations",
        "GetPointNotes",
        "utility_operations.get_point_notes",
    ),
    (
        "get_screen_resolution",
        "briosa.UtilityOperations",
        "GetScreenResolution",
        "utility_operations.get_screen_resolution",
    ),
    (
        "get_working_frame_properties",
        "briosa.UtilityOperations",
        "GetWorkingFrameProperties",
        "utility_operations.get_working_frame_properties",
    ),
    (
        "increment_point_name",
        "briosa.UtilityOperations",
        "IncrementPointName",
        "utility_operations.increment_point_name",
    ),
    (
        "lock_imported_items",
        "briosa.UtilityOperations",
        "LockImportedItems",
        "utility_operations.lock_imported_items",
    ),
    (
        "lock_unlock_selected_items",
        "briosa.UtilityOperations",
        "LockUnlockSelectedItems",
        "utility_operations.lock_unlock_selected_items",
    ),
    (
        "lock_unlock_trapping_control",
        "briosa.UtilityOperations",
        "LockUnlockTrappingControl",
        "utility_operations.lock_unlock_trapping_control",
    ),
    (
        "move_collection_to_folder",
        "briosa.UtilityOperations",
        "MoveCollectionToFolder",
        "utility_operations.move_collection_to_folder",
    ),
    (
        "move_folder_to_folder",
        "briosa.UtilityOperations",
        "MoveFolderToFolder",
        "utility_operations.move_folder_to_folder",
    ),
    (
        "move_instruments_drag_graphically",
        "briosa.UtilityOperations",
        "MoveInstrumentsDragGraphically",
        "utility_operations.move_instruments_drag_graphically",
    ),
    (
        "move_objects_drag_graphically",
        "briosa.UtilityOperations",
        "MoveObjectsDragGraphically",
        "utility_operations.move_objects_drag_graphically",
    ),
    (
        "scale_objects",
        "briosa.UtilityOperations",
        "ScaleObjects",
        "utility_operations.scale_objects",
    ),
    (
        "set_active_custom_language",
        "briosa.UtilityOperations",
        "SetActiveCustomLanguage",
        "utility_operations.set_active_custom_language",
    ),
    (
        "set_active_units",
        "briosa.UtilityOperations",
        "SetActiveUnits",
        "utility_operations.set_active_units",
    ),
    (
        "set_angular_representation",
        "briosa.UtilityOperations",
        "SetAngularRepresentation",
        "utility_operations.set_angular_representation",
    ),
    (
        "set_auto_event_creation",
        "briosa.UtilityOperations",
        "SetAutoEventCreation",
        "utility_operations.set_auto_event_creation",
    ),
    (
        "set_automatic_backup_state",
        "briosa.UtilityOperations",
        "SetAutomaticBackupState",
        "utility_operations.set_automatic_backup_state",
    ),
    (
        "set_automatic_relationship_construction_state",
        "briosa.UtilityOperations",
        "SetAutomaticRelationshipConstructionState",
        "utility_operations.set_automatic_relationship_construction_state",
    ),
    (
        "set_collection_notes",
        "briosa.UtilityOperations",
        "SetCollectionNotes",
        "utility_operations.set_collection_notes",
    ),
    (
        "set_decimal_digits_for_display",
        "briosa.UtilityOperations",
        "SetDecimalDigitsForDisplay",
        "utility_operations.set_decimal_digits_for_display",
    ),
    (
        "set_folder_notes",
        "briosa.UtilityOperations",
        "SetFolderNotes",
        "utility_operations.set_folder_notes",
    ),
    (
        "set_interaction_mode",
        "briosa.UtilityOperations",
        "SetInteractionMode",
        "utility_operations.set_interaction_mode",
    ),
    (
        "set_logging_state",
        "briosa.UtilityOperations",
        "SetLoggingState",
        "utility_operations.set_logging_state",
    ),
    (
        "set_notification_cancel_override",
        "briosa.UtilityOperations",
        "SetNotificationCancelOverride",
        "utility_operations.set_notification_cancel_override",
    ),
    (
        "set_object_notes",
        "briosa.UtilityOperations",
        "SetObjectNotes",
        "utility_operations.set_object_notes",
    ),
    (
        "set_opc_da_tag_value_double",
        "briosa.UtilityOperations",
        "SetOpcDaTagValueDouble",
        "utility_operations.set_opc_da_tag_value_double",
    ),
    (
        "set_opc_da_tag_value_integer",
        "briosa.UtilityOperations",
        "SetOpcDaTagValueInteger",
        "utility_operations.set_opc_da_tag_value_integer",
    ),
    (
        "set_opc_da_tag_value_string",
        "briosa.UtilityOperations",
        "SetOpcDaTagValueString",
        "utility_operations.set_opc_da_tag_value_string",
    ),
    (
        "set_point_notes",
        "briosa.UtilityOperations",
        "SetPointNotes",
        "utility_operations.set_point_notes",
    ),
    (
        "set_user_interface_profile",
        "briosa.UtilityOperations",
        "SetUserInterfaceProfile",
        "utility_operations.set_user_interface_profile",
    ),
    (
        "set_view_idle_update_frequency",
        "briosa.UtilityOperations",
        "SetViewIdleUpdateFrequency",
        "utility_operations.set_view_idle_update_frequency",
    ),
    (
        "set_wild_card_asterisk_mode",
        "briosa.UtilityOperations",
        "SetWildCardAsteriskMode",
        "utility_operations.set_wild_card_asterisk_mode",
    ),
    (
        "set_working_frame",
        "briosa.UtilityOperations",
        "SetWorkingFrame",
        "utility_operations.set_working_frame",
    ),
    (
        "status_dialog",
        "briosa.UtilityOperations",
        "StatusDialog",
        "utility_operations.status_dialog",
    ),
    (
        "trim_log_file",
        "briosa.UtilityOperations",
        "TrimLogFile",
        "utility_operations.trim_log_file",
    ),
    (
        "write_to_log",
        "briosa.UtilityOperations",
        "WriteToLog",
        "utility_operations.write_to_log",
    ),
    (
        "add_double_to_named_double_list_variable",
        "briosa.Variables",
        "AddDoubleToNamedDoubleListVariable",
        "variables.add_double_to_named_double_list_variable",
    ),
    (
        "clear_named_double_list_variable",
        "briosa.Variables",
        "ClearNamedDoubleListVariable",
        "variables.clear_named_double_list_variable",
    ),
    (
        "delete_variable",
        "briosa.Variables",
        "DeleteVariable",
        "variables.delete_variable",
    ),
    (
        "delete_variables_wildcard_match",
        "briosa.Variables",
        "DeleteVariablesWildcardMatch",
        "variables.delete_variables_wildcard_match",
    ),
    (
        "get_boolean_variable",
        "briosa.Variables",
        "GetBooleanVariable",
        "variables.get_boolean_variable",
    ),
    (
        "get_collection_object_name_variable",
        "briosa.Variables",
        "GetCollectionObjectNameVariable",
        "variables.get_collection_object_name_variable",
    ),
    (
        "get_collection_object_ref_list_variable",
        "briosa.Variables",
        "GetCollectionObjectRefListVariable",
        "variables.get_collection_object_ref_list_variable",
    ),
    (
        "get_double_variable",
        "briosa.Variables",
        "GetDoubleVariable",
        "variables.get_double_variable",
    ),
    (
        "get_integer_variable",
        "briosa.Variables",
        "GetIntegerVariable",
        "variables.get_integer_variable",
    ),
    (
        "get_named_double_list_variable",
        "briosa.Variables",
        "GetNamedDoubleListVariable",
        "variables.get_named_double_list_variable",
    ),
    (
        "get_named_double_list_variable_min_max",
        "briosa.Variables",
        "GetNamedDoubleListVariableMinMax",
        "variables.get_named_double_list_variable_min_max",
    ),
    (
        "get_point_name_ref_list_variable",
        "briosa.Variables",
        "GetPointNameRefListVariable",
        "variables.get_point_name_ref_list_variable",
    ),
    (
        "get_point_name_variable",
        "briosa.Variables",
        "GetPointNameVariable",
        "variables.get_point_name_variable",
    ),
    (
        "get_relationship_ref_list_variable",
        "briosa.Variables",
        "GetRelationshipRefListVariable",
        "variables.get_relationship_ref_list_variable",
    ),
    (
        "get_report_items_reference_list_variable",
        "briosa.Variables",
        "GetReportItemsReferenceListVariable",
        "variables.get_report_items_reference_list_variable",
    ),
    (
        "get_string_ref_list_variable",
        "briosa.Variables",
        "GetStringRefListVariable",
        "variables.get_string_ref_list_variable",
    ),
    (
        "get_string_variable",
        "briosa.Variables",
        "GetStringVariable",
        "variables.get_string_variable",
    ),
    (
        "get_transform_variable",
        "briosa.Variables",
        "GetTransformVariable",
        "variables.get_transform_variable",
    ),
    (
        "get_vector_name_ref_list_variable",
        "briosa.Variables",
        "GetVectorNameRefListVariable",
        "variables.get_vector_name_ref_list_variable",
    ),
    (
        "get_vector_variable",
        "briosa.Variables",
        "GetVectorVariable",
        "variables.get_vector_variable",
    ),
    (
        "set_boolean_variable",
        "briosa.Variables",
        "SetBooleanVariable",
        "variables.set_boolean_variable",
    ),
    (
        "set_collection_object_name_variable",
        "briosa.Variables",
        "SetCollectionObjectNameVariable",
        "variables.set_collection_object_name_variable",
    ),
    (
        "set_collection_object_ref_list_variable",
        "briosa.Variables",
        "SetCollectionObjectRefListVariable",
        "variables.set_collection_object_ref_list_variable",
    ),
    (
        "set_double_variable",
        "briosa.Variables",
        "SetDoubleVariable",
        "variables.set_double_variable",
    ),
    (
        "set_font_variable",
        "briosa.Variables",
        "SetFontVariable",
        "variables.set_font_variable",
    ),
    (
        "set_integer_variable",
        "briosa.Variables",
        "SetIntegerVariable",
        "variables.set_integer_variable",
    ),
    (
        "set_named_double_list_variable",
        "briosa.Variables",
        "SetNamedDoubleListVariable",
        "variables.set_named_double_list_variable",
    ),
    (
        "set_point_name_ref_list_variable",
        "briosa.Variables",
        "SetPointNameRefListVariable",
        "variables.set_point_name_ref_list_variable",
    ),
    (
        "set_point_name_variable",
        "briosa.Variables",
        "SetPointNameVariable",
        "variables.set_point_name_variable",
    ),
    (
        "set_relationship_ref_list_variable",
        "briosa.Variables",
        "SetRelationshipRefListVariable",
        "variables.set_relationship_ref_list_variable",
    ),
    (
        "set_report_items_reference_list_variable",
        "briosa.Variables",
        "SetReportItemsReferenceListVariable",
        "variables.set_report_items_reference_list_variable",
    ),
    (
        "set_string_ref_list_variable",
        "briosa.Variables",
        "SetStringRefListVariable",
        "variables.set_string_ref_list_variable",
    ),
    (
        "set_string_variable",
        "briosa.Variables",
        "SetStringVariable",
        "variables.set_string_variable",
    ),
    (
        "set_transform_variable",
        "briosa.Variables",
        "SetTransformVariable",
        "variables.set_transform_variable",
    ),
    (
        "set_vector_name_ref_list_variable",
        "briosa.Variables",
        "SetVectorNameRefListVariable",
        "variables.set_vector_name_ref_list_variable",
    ),
    (
        "set_vector_variable",
        "briosa.Variables",
        "SetVectorVariable",
        "variables.set_vector_variable",
    ),
    (
        "add_a_vector_to_vector_name_ref_list",
        "briosa.VectorOperations",
        "AddAVectorToVectorNameRefList",
        "vector_operations.add_a_vector_to_vector_name_ref_list",
    ),
    (
        "auto_range_and_set_vector_group_colorization_all",
        "briosa.VectorOperations",
        "AutoRangeAndSetVectorGroupColorizationAll",
        "vector_operations.auto_range_and_set_vector_group_colorization_all",
    ),
    (
        "auto_range_and_set_vector_group_colorization_selected",
        "briosa.VectorOperations",
        "AutoRangeAndSetVectorGroupColorizationSelected",
        "vector_operations.auto_range_and_set_vector_group_colorization_selected",
    ),
    (
        "delete_ith_vector_from_vector_group",
        "briosa.VectorOperations",
        "DeleteIthVectorFromVectorGroup",
        "vector_operations.delete_ith_vector_from_vector_group",
    ),
    (
        "delete_vector_by_name",
        "briosa.VectorOperations",
        "DeleteVectorByName",
        "vector_operations.delete_vector_by_name",
    ),
    (
        "delete_vectors",
        "briosa.VectorOperations",
        "DeleteVectors",
        "vector_operations.delete_vectors",
    ),
    (
        "get_ith_vector_from_vector_group",
        "briosa.VectorOperations",
        "GetIthVectorFromVectorGroup",
        "vector_operations.get_ith_vector_from_vector_group",
    ),
    (
        "get_ith_vector_from_vector_name_ref_list",
        "briosa.VectorOperations",
        "GetIthVectorFromVectorNameRefList",
        "vector_operations.get_ith_vector_from_vector_name_ref_list",
    ),
    (
        "get_number_of_vectors_in_vector_group",
        "briosa.VectorOperations",
        "GetNumberOfVectorsInVectorGroup",
        "vector_operations.get_number_of_vectors_in_vector_group",
    ),
    (
        "get_number_of_vectors_in_vector_name_ref_list",
        "briosa.VectorOperations",
        "GetNumberOfVectorsInVectorNameRefList",
        "vector_operations.get_number_of_vectors_in_vector_name_ref_list",
    ),
    (
        "get_vector_from_vector_group_by_name",
        "briosa.VectorOperations",
        "GetVectorFromVectorGroupByName",
        "vector_operations.get_vector_from_vector_group_by_name",
    ),
    (
        "get_vector_group_properties",
        "briosa.VectorOperations",
        "GetVectorGroupProperties",
        "vector_operations.get_vector_group_properties",
    ),
    (
        "set_vector_group_colorization_options_all",
        "briosa.VectorOperations",
        "SetVectorGroupColorizationOptionsAll",
        "vector_operations.set_vector_group_colorization_options_all",
    ),
    (
        "set_vector_group_colorization_options_selected",
        "briosa.VectorOperations",
        "SetVectorGroupColorizationOptionsSelected",
        "vector_operations.set_vector_group_colorization_options_selected",
    ),
    (
        "sort_vectors",
        "briosa.VectorOperations",
        "SortVectors",
        "vector_operations.sort_vectors",
    ),
    ("auto_scale", "briosa.ViewControl", "AutoScale", "view_control.auto_scale"),
    (
        "center_graphics_about_objects",
        "briosa.ViewControl",
        "CenterGraphicsAboutObjects",
        "view_control.center_graphics_about_objects",
    ),
    (
        "center_graphics_about_point",
        "briosa.ViewControl",
        "CenterGraphicsAboutPoint",
        "view_control.center_graphics_about_point",
    ),
    (
        "define_point_of_view",
        "briosa.ViewControl",
        "DefinePointOfView",
        "view_control.define_point_of_view",
    ),
    (
        "get_active_clipping_planes",
        "briosa.ViewControl",
        "GetActiveClippingPlanes",
        "view_control.get_active_clipping_planes",
    ),
    (
        "get_point_of_view_parameters",
        "briosa.ViewControl",
        "GetPointOfViewParameters",
        "view_control.get_point_of_view_parameters",
    ),
    (
        "hide_all_callout_views",
        "briosa.ViewControl",
        "HideAllCalloutViews",
        "view_control.hide_all_callout_views",
    ),
    ("hide_objects", "briosa.ViewControl", "HideObjects", "view_control.hide_objects"),
    (
        "highlight_objects",
        "briosa.ViewControl",
        "HighlightObjects",
        "view_control.highlight_objects",
    ),
    (
        "highlight_point",
        "briosa.ViewControl",
        "HighlightPoint",
        "view_control.highlight_point",
    ),
    (
        "highlight_relationships",
        "briosa.ViewControl",
        "HighlightRelationships",
        "view_control.highlight_relationships",
    ),
    (
        "load_ribbon_bar_from_xml_file",
        "briosa.ViewControl",
        "LoadRibbonBarFromXmlFile",
        "view_control.load_ribbon_bar_from_xml_file",
    ),
    (
        "refresh_views",
        "briosa.ViewControl",
        "RefreshViews",
        "view_control.refresh_views",
    ),
    (
        "reset_ribbon_bar_to_default",
        "briosa.ViewControl",
        "ResetRibbonBarToDefault",
        "view_control.reset_ribbon_bar_to_default",
    ),
    (
        "save_point_of_view",
        "briosa.ViewControl",
        "SavePointOfView",
        "view_control.save_point_of_view",
    ),
    (
        "set_background_color",
        "briosa.ViewControl",
        "SetBackgroundColor",
        "view_control.set_background_color",
    ),
    (
        "set_mp_window_state",
        "briosa.ViewControl",
        "SetMpWindowState",
        "view_control.set_mp_window_state",
    ),
    (
        "set_objects_color",
        "briosa.ViewControl",
        "SetObjectsColor",
        "view_control.set_objects_color",
    ),
    (
        "set_objects_translucency",
        "briosa.ViewControl",
        "SetObjectsTranslucency",
        "view_control.set_objects_translucency",
    ),
    (
        "set_point_of_view",
        "briosa.ViewControl",
        "SetPointOfView",
        "view_control.set_point_of_view",
    ),
    (
        "set_point_of_view_from_frame",
        "briosa.ViewControl",
        "SetPointOfViewFromFrame",
        "view_control.set_point_of_view_from_frame",
    ),
    (
        "set_point_of_view_from_instrument_updates",
        "briosa.ViewControl",
        "SetPointOfViewFromInstrumentUpdates",
        "view_control.set_point_of_view_from_instrument_updates",
    ),
    (
        "set_render_mode_type",
        "briosa.ViewControl",
        "SetRenderModeType",
        "view_control.set_render_mode_type",
    ),
    (
        "set_sa_window_pos",
        "briosa.ViewControl",
        "SetSaWindowPos",
        "view_control.set_sa_window_pos",
    ),
    (
        "set_sa_window_size",
        "briosa.ViewControl",
        "SetSaWindowSize",
        "view_control.set_sa_window_size",
    ),
    (
        "set_sa_window_state",
        "briosa.ViewControl",
        "SetSaWindowState",
        "view_control.set_sa_window_state",
    ),
    (
        "set_target_labels_use_full_names",
        "briosa.ViewControl",
        "SetTargetLabelsUseFullNames",
        "view_control.set_target_labels_use_full_names",
    ),
    (
        "set_toolkit_visibility",
        "briosa.ViewControl",
        "SetToolkitVisibility",
        "view_control.set_toolkit_visibility",
    ),
    (
        "set_view_clipping_plane",
        "briosa.ViewControl",
        "SetViewClippingPlane",
        "view_control.set_view_clipping_plane",
    ),
    (
        "set_working_color",
        "briosa.ViewControl",
        "SetWorkingColor",
        "view_control.set_working_color",
    ),
    (
        "set_working_color_auto_increment",
        "briosa.ViewControl",
        "SetWorkingColorAutoIncrement",
        "view_control.set_working_color_auto_increment",
    ),
    (
        "show_hide_by_object_type",
        "briosa.ViewControl",
        "ShowHideByObjectType",
        "view_control.show_hide_by_object_type",
    ),
    (
        "show_hide_callout_view",
        "briosa.ViewControl",
        "ShowHideCalloutView",
        "view_control.show_hide_callout_view",
    ),
    (
        "show_hide_dimension",
        "briosa.ViewControl",
        "ShowHideDimension",
        "view_control.show_hide_dimension",
    ),
    (
        "show_hide_points",
        "briosa.ViewControl",
        "ShowHidePoints",
        "view_control.show_hide_points",
    ),
    (
        "show_by_object_type",
        "briosa.ViewControl",
        "ShowByObjectType",
        "view_control.show_by_object_type",
    ),
    (
        "show_items_in_tree",
        "briosa.ViewControl",
        "ShowItemsInTree",
        "view_control.show_items_in_tree",
    ),
    ("show_labels", "briosa.ViewControl", "ShowLabels", "view_control.show_labels"),
    ("show_objects", "briosa.ViewControl", "ShowObjects", "view_control.show_objects"),
    (
        "show_hide_annotations_for_datums",
        "briosa.ViewControl",
        "ShowHideAnnotationsForDatums",
        "view_control.show_hide_annotations_for_datums",
    ),
    (
        "show_hide_annotations_for_feature_checks",
        "briosa.ViewControl",
        "ShowHideAnnotationsForFeatureChecks",
        "view_control.show_hide_annotations_for_feature_checks",
    ),
    (
        "show_hide_inspection_bar",
        "briosa.ViewControl",
        "ShowHideInspectionBar",
        "view_control.show_hide_inspection_bar",
    ),
    (
        "show_hide_instrument_interface",
        "briosa.ViewControl",
        "ShowHideInstrumentInterface",
        "view_control.show_hide_instrument_interface",
    ),
    (
        "show_hide_instrument_probe_tip",
        "briosa.ViewControl",
        "ShowHideInstrumentProbeTip",
        "view_control.show_hide_instrument_probe_tip",
    ),
    (
        "show_hide_instruments",
        "briosa.ViewControl",
        "ShowHideInstruments",
        "view_control.show_hide_instruments",
    ),
    (
        "show_hide_relationship_report",
        "briosa.ViewControl",
        "ShowHideRelationshipReport",
        "view_control.show_hide_relationship_report",
    ),
    (
        "show_hide_relationship_watch",
        "briosa.ViewControl",
        "ShowHideRelationshipWatch",
        "view_control.show_hide_relationship_watch",
    ),
)

__all__ = ["WAVE_A_OPERATIONS", "WaveAOperationsMixin"]
