from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoScaleRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoScaleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CenterGraphicsAboutObjectsRequest(_message.Message):
    __slots__ = ("object_type", "collection_wildcard_criteria", "object_wildcard_criteria")
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    OBJECT_WILDCARD_CRITERIA_FIELD_NUMBER: _ClassVar[int]
    object_type: _spatial_analyzer_values_pb2.ObjectType
    collection_wildcard_criteria: str
    object_wildcard_criteria: str
    def __init__(self, object_type: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ..., collection_wildcard_criteria: _Optional[str] = ..., object_wildcard_criteria: _Optional[str] = ...) -> None: ...

class CenterGraphicsAboutObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CenterGraphicsAboutPointRequest(_message.Message):
    __slots__ = ("point_name",)
    POINT_NAME_FIELD_NUMBER: _ClassVar[int]
    point_name: _spatial_analyzer_values_pb2.PointName
    def __init__(self, point_name: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ...) -> None: ...

class CenterGraphicsAboutPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DefinePointOfViewRequest(_message.Message):
    __slots__ = ("view_name", "rotation_x", "rotation_y", "rotation_z", "restore_zoom_settings", "scale_factor", "origin_x", "origin_y", "restore_render_mode", "rendering_mode")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    ROTATION_X_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Y_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Z_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ZOOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_X_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_Y_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RENDER_MODE_FIELD_NUMBER: _ClassVar[int]
    RENDERING_MODE_FIELD_NUMBER: _ClassVar[int]
    view_name: _spatial_analyzer_values_pb2.ViewName
    rotation_x: float
    rotation_y: float
    rotation_z: float
    restore_zoom_settings: bool
    scale_factor: float
    origin_x: float
    origin_y: float
    restore_render_mode: bool
    rendering_mode: _spatial_analyzer_values_pb2.RenderModeType
    def __init__(self, view_name: _Optional[_Union[_spatial_analyzer_values_pb2.ViewName, _Mapping]] = ..., rotation_x: _Optional[float] = ..., rotation_y: _Optional[float] = ..., rotation_z: _Optional[float] = ..., restore_zoom_settings: bool = ..., scale_factor: _Optional[float] = ..., origin_x: _Optional[float] = ..., origin_y: _Optional[float] = ..., restore_render_mode: bool = ..., rendering_mode: _Optional[_Union[_spatial_analyzer_values_pb2.RenderModeType, str]] = ...) -> None: ...

class DefinePointOfViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetActiveClippingPlanesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetActiveClippingPlanesResult(_message.Message):
    __slots__ = ("objects", "execution")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetPointOfViewParametersRequest(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: _spatial_analyzer_values_pb2.ViewName
    def __init__(self, view_name: _Optional[_Union[_spatial_analyzer_values_pb2.ViewName, _Mapping]] = ...) -> None: ...

class GetPointOfViewParametersResult(_message.Message):
    __slots__ = ("rotation_x", "rotation_y", "rotation_z", "restore_zoom_settings", "scale_factor", "origin_x", "origin_y", "restore_render_mode", "execution")
    ROTATION_X_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Y_FIELD_NUMBER: _ClassVar[int]
    ROTATION_Z_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ZOOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SCALE_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_X_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_Y_FIELD_NUMBER: _ClassVar[int]
    RESTORE_RENDER_MODE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    rotation_x: float
    rotation_y: float
    rotation_z: float
    restore_zoom_settings: bool
    scale_factor: float
    origin_x: float
    origin_y: float
    restore_render_mode: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, rotation_x: _Optional[float] = ..., rotation_y: _Optional[float] = ..., rotation_z: _Optional[float] = ..., restore_zoom_settings: bool = ..., scale_factor: _Optional[float] = ..., origin_x: _Optional[float] = ..., origin_y: _Optional[float] = ..., restore_render_mode: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HideAllCalloutViewsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HideAllCalloutViewsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HideObjectsRequest(_message.Message):
    __slots__ = ("objects_to_hide",)
    OBJECTS_TO_HIDE_FIELD_NUMBER: _ClassVar[int]
    objects_to_hide: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, objects_to_hide: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class HideObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HighlightObjectsRequest(_message.Message):
    __slots__ = ("object_names_empty_to_clear_all", "high_light_objects")
    OBJECT_NAMES_EMPTY_TO_CLEAR_ALL_FIELD_NUMBER: _ClassVar[int]
    HIGH_LIGHT_OBJECTS_FIELD_NUMBER: _ClassVar[int]
    object_names_empty_to_clear_all: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    high_light_objects: bool
    def __init__(self, object_names_empty_to_clear_all: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., high_light_objects: bool = ...) -> None: ...

class HighlightObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HighlightPointRequest(_message.Message):
    __slots__ = ("point_name_empty_to_clear_all", "show_point")
    POINT_NAME_EMPTY_TO_CLEAR_ALL_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINT_FIELD_NUMBER: _ClassVar[int]
    point_name_empty_to_clear_all: _spatial_analyzer_values_pb2.PointName
    show_point: bool
    def __init__(self, point_name_empty_to_clear_all: _Optional[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]] = ..., show_point: bool = ...) -> None: ...

class HighlightPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HighlightRelationshipsRequest(_message.Message):
    __slots__ = ("relationships_empty_to_clear_all", "high_light_relationships")
    RELATIONSHIPS_EMPTY_TO_CLEAR_ALL_FIELD_NUMBER: _ClassVar[int]
    HIGH_LIGHT_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    relationships_empty_to_clear_all: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    high_light_relationships: bool
    def __init__(self, relationships_empty_to_clear_all: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., high_light_relationships: bool = ...) -> None: ...

class HighlightRelationshipsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class LoadRibbonBarFromXmlFileRequest(_message.Message):
    __slots__ = ("file_path",)
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    file_path: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class LoadRibbonBarFromXmlFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RefreshViewsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshViewsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ResetRibbonBarToDefaultRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetRibbonBarToDefaultResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SavePointOfViewRequest(_message.Message):
    __slots__ = ("view_name", "restore_zoom_settings")
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    RESTORE_ZOOM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    view_name: _spatial_analyzer_values_pb2.ViewName
    restore_zoom_settings: bool
    def __init__(self, view_name: _Optional[_Union[_spatial_analyzer_values_pb2.ViewName, _Mapping]] = ..., restore_zoom_settings: bool = ...) -> None: ...

class SavePointOfViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetBackgroundColorRequest(_message.Message):
    __slots__ = ("solid_color_name", "gradient_start_color_name", "gradient_end_color_name", "highlight_color")
    SOLID_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_START_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    GRADIENT_END_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_COLOR_FIELD_NUMBER: _ClassVar[int]
    solid_color_name: _spatial_analyzer_values_pb2.Color
    gradient_start_color_name: _spatial_analyzer_values_pb2.Color
    gradient_end_color_name: _spatial_analyzer_values_pb2.Color
    highlight_color: _spatial_analyzer_values_pb2.Color
    def __init__(self, solid_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., gradient_start_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., gradient_end_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., highlight_color: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ...) -> None: ...

class SetBackgroundColorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetMpWindowStateRequest(_message.Message):
    __slots__ = ("mp_window_state",)
    MP_WINDOW_STATE_FIELD_NUMBER: _ClassVar[int]
    mp_window_state: _spatial_analyzer_values_pb2.WindowState
    def __init__(self, mp_window_state: _Optional[_Union[_spatial_analyzer_values_pb2.WindowState, str]] = ...) -> None: ...

class SetMpWindowStateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectsColorRequest(_message.Message):
    __slots__ = ("objects_to_change", "new_working_color_name", "auto_increment")
    OBJECTS_TO_CHANGE_FIELD_NUMBER: _ClassVar[int]
    NEW_WORKING_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTO_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    objects_to_change: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    new_working_color_name: _spatial_analyzer_values_pb2.Color
    auto_increment: bool
    def __init__(self, objects_to_change: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., new_working_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., auto_increment: bool = ...) -> None: ...

class SetObjectsColorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetObjectsTranslucencyRequest(_message.Message):
    __slots__ = ("objects_to_change", "rendering_type", "opacity_value")
    OBJECTS_TO_CHANGE_FIELD_NUMBER: _ClassVar[int]
    RENDERING_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPACITY_VALUE_FIELD_NUMBER: _ClassVar[int]
    objects_to_change: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    rendering_type: _spatial_analyzer_values_pb2.TranslucencyType
    opacity_value: float
    def __init__(self, objects_to_change: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., rendering_type: _Optional[_Union[_spatial_analyzer_values_pb2.TranslucencyType, str]] = ..., opacity_value: _Optional[float] = ...) -> None: ...

class SetObjectsTranslucencyResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointOfViewRequest(_message.Message):
    __slots__ = ("view_name",)
    VIEW_NAME_FIELD_NUMBER: _ClassVar[int]
    view_name: _spatial_analyzer_values_pb2.ViewName
    def __init__(self, view_name: _Optional[_Union[_spatial_analyzer_values_pb2.ViewName, _Mapping]] = ...) -> None: ...

class SetPointOfViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointOfViewFromFrameRequest(_message.Message):
    __slots__ = ("frame",)
    FRAME_FIELD_NUMBER: _ClassVar[int]
    frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetPointOfViewFromFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointOfViewFromInstrumentUpdatesRequest(_message.Message):
    __slots__ = ("instrument_id", "display_view_control", "enable_set_viewpoint_from_instrument_updates", "update_view_percent", "clip_behind_probe", "automatic_zoom_when_trapping", "enable_directional_cloud_points", "angle_reset_threshold", "animation_steps", "reference_frame_object", "use_scan_stripe_for_view_focus", "zoom_factor")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_VIEW_CONTROL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SET_VIEWPOINT_FROM_INSTRUMENT_UPDATES_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VIEW_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CLIP_BEHIND_PROBE_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_ZOOM_WHEN_TRAPPING_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DIRECTIONAL_CLOUD_POINTS_FIELD_NUMBER: _ClassVar[int]
    ANGLE_RESET_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_STEPS_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_OBJECT_FIELD_NUMBER: _ClassVar[int]
    USE_SCAN_STRIPE_FOR_VIEW_FOCUS_FIELD_NUMBER: _ClassVar[int]
    ZOOM_FACTOR_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    display_view_control: bool
    enable_set_viewpoint_from_instrument_updates: bool
    update_view_percent: float
    clip_behind_probe: bool
    automatic_zoom_when_trapping: bool
    enable_directional_cloud_points: bool
    angle_reset_threshold: float
    animation_steps: int
    reference_frame_object: _spatial_analyzer_values_pb2.CollectionObjectName
    use_scan_stripe_for_view_focus: bool
    zoom_factor: float
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., display_view_control: bool = ..., enable_set_viewpoint_from_instrument_updates: bool = ..., update_view_percent: _Optional[float] = ..., clip_behind_probe: bool = ..., automatic_zoom_when_trapping: bool = ..., enable_directional_cloud_points: bool = ..., angle_reset_threshold: _Optional[float] = ..., animation_steps: _Optional[int] = ..., reference_frame_object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_scan_stripe_for_view_focus: bool = ..., zoom_factor: _Optional[float] = ...) -> None: ...

class SetPointOfViewFromInstrumentUpdatesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRenderModeTypeRequest(_message.Message):
    __slots__ = ("rendering_mode",)
    RENDERING_MODE_FIELD_NUMBER: _ClassVar[int]
    rendering_mode: _spatial_analyzer_values_pb2.RenderModeType
    def __init__(self, rendering_mode: _Optional[_Union[_spatial_analyzer_values_pb2.RenderModeType, str]] = ...) -> None: ...

class SetRenderModeTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetSaWindowPosRequest(_message.Message):
    __slots__ = ("pos_x", "pos_y")
    POS_X_FIELD_NUMBER: _ClassVar[int]
    POS_Y_FIELD_NUMBER: _ClassVar[int]
    pos_x: int
    pos_y: int
    def __init__(self, pos_x: _Optional[int] = ..., pos_y: _Optional[int] = ...) -> None: ...

class SetSaWindowPosResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetSaWindowSizeRequest(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class SetSaWindowSizeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetSaWindowStateRequest(_message.Message):
    __slots__ = ("sa_window_state",)
    SA_WINDOW_STATE_FIELD_NUMBER: _ClassVar[int]
    sa_window_state: _spatial_analyzer_values_pb2.WindowState
    def __init__(self, sa_window_state: _Optional[_Union[_spatial_analyzer_values_pb2.WindowState, str]] = ...) -> None: ...

class SetSaWindowStateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetTargetLabelsUseFullNamesRequest(_message.Message):
    __slots__ = ("use_full_names",)
    USE_FULL_NAMES_FIELD_NUMBER: _ClassVar[int]
    use_full_names: bool
    def __init__(self, use_full_names: bool = ...) -> None: ...

class SetTargetLabelsUseFullNamesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetToolkitVisibilityRequest(_message.Message):
    __slots__ = ("show_toolkit",)
    SHOW_TOOLKIT_FIELD_NUMBER: _ClassVar[int]
    show_toolkit: bool
    def __init__(self, show_toolkit: bool = ...) -> None: ...

class SetToolkitVisibilityResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetViewClippingPlaneRequest(_message.Message):
    __slots__ = ("object", "remove_clipping_plane")
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    REMOVE_CLIPPING_PLANE_FIELD_NUMBER: _ClassVar[int]
    object: _spatial_analyzer_values_pb2.CollectionObjectName
    remove_clipping_plane: bool
    def __init__(self, object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., remove_clipping_plane: bool = ...) -> None: ...

class SetViewClippingPlaneResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetWorkingColorRequest(_message.Message):
    __slots__ = ("new_working_color_name",)
    NEW_WORKING_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    new_working_color_name: _spatial_analyzer_values_pb2.Color
    def __init__(self, new_working_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ...) -> None: ...

class SetWorkingColorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetWorkingColorAutoIncrementRequest(_message.Message):
    __slots__ = ("auto_increment",)
    AUTO_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    auto_increment: bool
    def __init__(self, auto_increment: bool = ...) -> None: ...

class SetWorkingColorAutoIncrementResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideByObjectTypeRequest(_message.Message):
    __slots__ = ("all_collections", "specific_collection", "object_type_to_show_hide", "hide_show_false")
    ALL_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_TO_SHOW_HIDE_FIELD_NUMBER: _ClassVar[int]
    HIDE_SHOW_FALSE_FIELD_NUMBER: _ClassVar[int]
    all_collections: bool
    specific_collection: _spatial_analyzer_values_pb2.CollectionName
    object_type_to_show_hide: _spatial_analyzer_values_pb2.ObjectType
    hide_show_false: bool
    def __init__(self, all_collections: bool = ..., specific_collection: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., object_type_to_show_hide: _Optional[_Union[_spatial_analyzer_values_pb2.ObjectType, str]] = ..., hide_show_false: bool = ...) -> None: ...

class ShowHideByObjectTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideCalloutViewRequest(_message.Message):
    __slots__ = ("callout_view_to_show", "show_callout_view")
    CALLOUT_VIEW_TO_SHOW_FIELD_NUMBER: _ClassVar[int]
    SHOW_CALLOUT_VIEW_FIELD_NUMBER: _ClassVar[int]
    callout_view_to_show: _spatial_analyzer_values_pb2.CollectionItemName
    show_callout_view: bool
    def __init__(self, callout_view_to_show: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., show_callout_view: bool = ...) -> None: ...

class ShowHideCalloutViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideDimensionRequest(_message.Message):
    __slots__ = ("dimension_name", "show_dimension")
    DIMENSION_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_DIMENSION_FIELD_NUMBER: _ClassVar[int]
    dimension_name: _spatial_analyzer_values_pb2.CollectionItemName
    show_dimension: bool
    def __init__(self, dimension_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., show_dimension: bool = ...) -> None: ...

class ShowHideDimensionResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHidePointsRequest(_message.Message):
    __slots__ = ("point_names", "show_hide_false")
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    SHOW_HIDE_FALSE_FIELD_NUMBER: _ClassVar[int]
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    show_hide_false: bool
    def __init__(self, point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., show_hide_false: bool = ...) -> None: ...

class ShowHidePointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowByObjectTypeRequest(_message.Message):
    __slots__ = ("object_type_to_show", "all_collections")
    OBJECT_TYPE_TO_SHOW_FIELD_NUMBER: _ClassVar[int]
    ALL_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    object_type_to_show: _spatial_analyzer_values_pb2.CollectionObjectName
    all_collections: bool
    def __init__(self, object_type_to_show: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., all_collections: bool = ...) -> None: ...

class ShowByObjectTypeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowItemsInTreeRequest(_message.Message):
    __slots__ = ("collapse_all_other_items", "points", "objects", "instruments", "feature_checks", "datums", "collections")
    COLLAPSE_ALL_OTHER_ITEMS_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    DATUMS_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collapse_all_other_items: bool
    points: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    instruments: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    feature_checks: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    datums: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    collections: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collapse_all_other_items: bool = ..., points: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., instruments: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., feature_checks: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., datums: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., collections: _Optional[_Iterable[str]] = ...) -> None: ...

class ShowItemsInTreeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowLabelsRequest(_message.Message):
    __slots__ = ("point_labels_on", "objects_labels_on")
    POINT_LABELS_ON_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_LABELS_ON_FIELD_NUMBER: _ClassVar[int]
    point_labels_on: bool
    objects_labels_on: bool
    def __init__(self, point_labels_on: bool = ..., objects_labels_on: bool = ...) -> None: ...

class ShowLabelsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowObjectsRequest(_message.Message):
    __slots__ = ("objects_to_show",)
    OBJECTS_TO_SHOW_FIELD_NUMBER: _ClassVar[int]
    objects_to_show: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    def __init__(self, objects_to_show: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ...) -> None: ...

class ShowObjectsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideAnnotationsForDatumsRequest(_message.Message):
    __slots__ = ("datum_name_list", "show", "highlight", "set_inspection_view")
    DATUM_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_FIELD_NUMBER: _ClassVar[int]
    SET_INSPECTION_VIEW_FIELD_NUMBER: _ClassVar[int]
    datum_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    show: bool
    highlight: bool
    set_inspection_view: bool
    def __init__(self, datum_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., show: bool = ..., highlight: bool = ..., set_inspection_view: bool = ...) -> None: ...

class ShowHideAnnotationsForDatumsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideAnnotationsForFeatureChecksRequest(_message.Message):
    __slots__ = ("feature_check_name_list", "show", "highlight", "set_inspection_view")
    FEATURE_CHECK_NAME_LIST_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHT_FIELD_NUMBER: _ClassVar[int]
    SET_INSPECTION_VIEW_FIELD_NUMBER: _ClassVar[int]
    feature_check_name_list: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    show: bool
    highlight: bool
    set_inspection_view: bool
    def __init__(self, feature_check_name_list: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., show: bool = ..., highlight: bool = ..., set_inspection_view: bool = ...) -> None: ...

class ShowHideAnnotationsForFeatureChecksResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideInspectionBarRequest(_message.Message):
    __slots__ = ("show_inspection_bar",)
    SHOW_INSPECTION_BAR_FIELD_NUMBER: _ClassVar[int]
    show_inspection_bar: bool
    def __init__(self, show_inspection_bar: bool = ...) -> None: ...

class ShowHideInspectionBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideInstrumentInterfaceRequest(_message.Message):
    __slots__ = ("instrument_id", "minimize_interface", "hide_interface")
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    MINIMIZE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    HIDE_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    minimize_interface: bool
    hide_interface: bool
    def __init__(self, instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., minimize_interface: bool = ..., hide_interface: bool = ...) -> None: ...

class ShowHideInstrumentInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideInstrumentProbeTipRequest(_message.Message):
    __slots__ = ("show_instrument_probe_tip",)
    SHOW_INSTRUMENT_PROBE_TIP_FIELD_NUMBER: _ClassVar[int]
    show_instrument_probe_tip: bool
    def __init__(self, show_instrument_probe_tip: bool = ...) -> None: ...

class ShowHideInstrumentProbeTipResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideInstrumentsRequest(_message.Message):
    __slots__ = ("instrument_i_ds", "show_instruments")
    INSTRUMENT_I_DS_FIELD_NUMBER: _ClassVar[int]
    SHOW_INSTRUMENTS_FIELD_NUMBER: _ClassVar[int]
    instrument_i_ds: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionInstrumentId]
    show_instruments: bool
    def __init__(self, instrument_i_ds: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]]] = ..., show_instruments: bool = ...) -> None: ...

class ShowHideInstrumentsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideRelationshipReportRequest(_message.Message):
    __slots__ = ("collection_name", "show_relationship_report")
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_RELATIONSHIP_REPORT_FIELD_NUMBER: _ClassVar[int]
    collection_name: _spatial_analyzer_values_pb2.CollectionName
    show_relationship_report: bool
    def __init__(self, collection_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionName, _Mapping]] = ..., show_relationship_report: bool = ...) -> None: ...

class ShowHideRelationshipReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ShowHideRelationshipWatchRequest(_message.Message):
    __slots__ = ("relationship_name", "show_relationship_watch", "relationship_watch_window_properties", "window_top_left_x_position", "window_top_left_y_position", "window_width", "window_height")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_RELATIONSHIP_WATCH_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_WATCH_WINDOW_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_X_POSITION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_TOP_LEFT_Y_POSITION_FIELD_NUMBER: _ClassVar[int]
    WINDOW_WIDTH_FIELD_NUMBER: _ClassVar[int]
    WINDOW_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    show_relationship_watch: bool
    relationship_watch_window_properties: _spatial_analyzer_values_pb2.CollectionObjectName
    window_top_left_x_position: int
    window_top_left_y_position: int
    window_width: int
    window_height: int
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., show_relationship_watch: bool = ..., relationship_watch_window_properties: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., window_top_left_x_position: _Optional[int] = ..., window_top_left_y_position: _Optional[int] = ..., window_width: _Optional[int] = ..., window_height: _Optional[int] = ...) -> None: ...

class ShowHideRelationshipWatchResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
