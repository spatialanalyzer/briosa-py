from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddChartsToReportBarRequest(_message.Message):
    __slots__ = ("charts", "clear_existing")
    CHARTS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    charts: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, charts: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddChartsToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddCustomTableToSaReportRequest(_message.Message):
    __slots__ = ("table_name", "report_name", "show_report")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_REPORT_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    show_report: bool
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., show_report: bool = ...) -> None: ...

class AddCustomTableToSaReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddCustomTablesToReportBarRequest(_message.Message):
    __slots__ = ("custom_tables_to_report", "clear_existing")
    CUSTOM_TABLES_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    custom_tables_to_report: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, custom_tables_to_report: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddCustomTablesToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddDatumsToReportBarRequest(_message.Message):
    __slots__ = ("datums", "clear_existing")
    DATUMS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    datums: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    clear_existing: bool
    def __init__(self, datums: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddDatumsToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddEventsToReportBarRequest(_message.Message):
    __slots__ = ("events", "clear_existing")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, events: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddEventsToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddFeatureChecksToReportBarRequest(_message.Message):
    __slots__ = ("feature_checks", "clear_existing")
    FEATURE_CHECKS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    feature_checks: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, feature_checks: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddFeatureChecksToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddItemToSaReportAtLocationRequest(_message.Message):
    __slots__ = ("report_name", "item_name", "page_number", "horizontal_location", "vertical_location", "show_report")
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    HORIZONTAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    VERTICAL_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SHOW_REPORT_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    item_name: _spatial_analyzer_values_pb2.CollectionObjectName
    page_number: int
    horizontal_location: float
    vertical_location: float
    show_report: bool
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., item_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., page_number: _Optional[int] = ..., horizontal_location: _Optional[float] = ..., vertical_location: _Optional[float] = ..., show_report: bool = ...) -> None: ...

class AddItemToSaReportAtLocationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddObjectsToReportBarRequest(_message.Message):
    __slots__ = ("objects", "clear_existing")
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    objects: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    clear_existing: bool
    def __init__(self, objects: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddObjectsToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddPicturesToReportBarRequest(_message.Message):
    __slots__ = ("pictures", "clear_existing")
    PICTURES_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    pictures: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, pictures: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddPicturesToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddRelationshipsToReportBarRequest(_message.Message):
    __slots__ = ("relationships", "clear_existing")
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    CLEAR_EXISTING_FIELD_NUMBER: _ClassVar[int]
    relationships: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    clear_existing: bool
    def __init__(self, relationships: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., clear_existing: bool = ...) -> None: ...

class AddRelationshipsToReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AppendItemsToSaReportRequest(_message.Message):
    __slots__ = ("report_name", "items_to_report", "show_report", "begin_on_new_page")
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEMS_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
    SHOW_REPORT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_ON_NEW_PAGE_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    items_to_report: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    show_report: bool
    begin_on_new_page: bool
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., items_to_report: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., show_report: bool = ..., begin_on_new_page: bool = ...) -> None: ...

class AppendItemsToSaReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CaptureCurrentViewRequest(_message.Message):
    __slots__ = ("picture_name",)
    PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class CaptureCurrentViewResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CaptureScreenToFileBmpJpgPngGifTiffRequest(_message.Message):
    __slots__ = ("file_to_save_to",)
    FILE_TO_SAVE_TO_FIELD_NUMBER: _ClassVar[int]
    file_to_save_to: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, file_to_save_to: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class CaptureScreenToFileBmpJpgPngGifTiffResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearCustomTableRequest(_message.Message):
    __slots__ = ("table_name",)
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ClearCustomTableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CloseAllReportsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseAllReportsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CloseHtmlDisplayBoardRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CloseHtmlDisplayBoardResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CombineSaReportsRequest(_message.Message):
    __slots__ = ("sa_reports_to_combine", "output_sa_report_name", "show_report")
    SA_REPORTS_TO_COMBINE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SA_REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_REPORT_FIELD_NUMBER: _ClassVar[int]
    sa_reports_to_combine: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    output_sa_report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    show_report: bool
    def __init__(self, sa_reports_to_combine: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., output_sa_report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., show_report: bool = ...) -> None: ...

class CombineSaReportsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateChartFromVectorGroupRequest(_message.Message):
    __slots__ = ("new_chart_name", "vector_group_name", "chart_type", "data_set_to_chart", "aux_data_set_to_chart", "template_chart_name_optional", "show_interface")
    NEW_CHART_NAME_FIELD_NUMBER: _ClassVar[int]
    VECTOR_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    CHART_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_SET_TO_CHART_FIELD_NUMBER: _ClassVar[int]
    AUX_DATA_SET_TO_CHART_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_CHART_NAME_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    new_chart_name: _spatial_analyzer_values_pb2.ChartName
    vector_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    chart_type: _spatial_analyzer_values_pb2.ChartType
    data_set_to_chart: _spatial_analyzer_values_pb2.DatasetType
    aux_data_set_to_chart: _spatial_analyzer_values_pb2.DatasetType
    template_chart_name_optional: _spatial_analyzer_values_pb2.ChartName
    show_interface: bool
    def __init__(self, new_chart_name: _Optional[_Union[_spatial_analyzer_values_pb2.ChartName, _Mapping]] = ..., vector_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., chart_type: _Optional[_Union[_spatial_analyzer_values_pb2.ChartType, str]] = ..., data_set_to_chart: _Optional[_Union[_spatial_analyzer_values_pb2.DatasetType, str]] = ..., aux_data_set_to_chart: _Optional[_Union[_spatial_analyzer_values_pb2.DatasetType, str]] = ..., template_chart_name_optional: _Optional[_Union[_spatial_analyzer_values_pb2.ChartName, _Mapping]] = ..., show_interface: bool = ...) -> None: ...

class CreateChartFromVectorGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DefineReportTemplateRequest(_message.Message):
    __slots__ = ("report_template_name", "title", "graphical_view_options", "items_to_report", "relationships_to_report", "events_to_report", "report_output_options", "report_page_settings_sa_report_only", "generate_now", "show_generated_report")
    REPORT_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    GRAPHICAL_VIEW_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
    EVENTS_TO_REPORT_FIELD_NUMBER: _ClassVar[int]
    REPORT_OUTPUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    REPORT_PAGE_SETTINGS_SA_REPORT_ONLY_FIELD_NUMBER: _ClassVar[int]
    GENERATE_NOW_FIELD_NUMBER: _ClassVar[int]
    SHOW_GENERATED_REPORT_FIELD_NUMBER: _ClassVar[int]
    report_template_name: _spatial_analyzer_values_pb2.CollectionObjectName
    title: _containers.RepeatedScalarFieldContainer[str]
    graphical_view_options: _spatial_analyzer_values_pb2.ReportViewOptions
    items_to_report: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    relationships_to_report: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    events_to_report: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionItemName]
    report_output_options: _spatial_analyzer_values_pb2.ReportOutputOptions
    report_page_settings_sa_report_only: _spatial_analyzer_values_pb2.ReportPageSettings
    generate_now: bool
    show_generated_report: bool
    def __init__(self, report_template_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., title: _Optional[_Iterable[str]] = ..., graphical_view_options: _Optional[_Union[_spatial_analyzer_values_pb2.ReportViewOptions, _Mapping]] = ..., items_to_report: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., relationships_to_report: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., events_to_report: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]]] = ..., report_output_options: _Optional[_Union[_spatial_analyzer_values_pb2.ReportOutputOptions, _Mapping]] = ..., report_page_settings_sa_report_only: _Optional[_Union[_spatial_analyzer_values_pb2.ReportPageSettings, str]] = ..., generate_now: bool = ..., show_generated_report: bool = ...) -> None: ...

class DefineReportTemplateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteChartRequest(_message.Message):
    __slots__ = ("chart_name",)
    CHART_NAME_FIELD_NUMBER: _ClassVar[int]
    chart_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, chart_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteChartResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCustomTableRequest(_message.Message):
    __slots__ = ("table_name",)
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteCustomTableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeletePictureRequest(_message.Message):
    __slots__ = ("picture_name",)
    PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class DeletePictureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteSaDocRequest(_message.Message):
    __slots__ = ("doc_name",)
    DOC_NAME_FIELD_NUMBER: _ClassVar[int]
    doc_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, doc_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteSaDocResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteSaReportRequest(_message.Message):
    __slots__ = ("report_name",)
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteSaReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteSaReportTemplateRequest(_message.Message):
    __slots__ = ("report_template_name",)
    REPORT_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    report_template_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, report_template_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteSaReportTemplateResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GenerateQuickReportFromTabOrderRequest(_message.Message):
    __slots__ = ("report_output_options", "open_report")
    REPORT_OUTPUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OPEN_REPORT_FIELD_NUMBER: _ClassVar[int]
    report_output_options: _spatial_analyzer_values_pb2.ReportOutputOptions
    open_report: bool
    def __init__(self, report_output_options: _Optional[_Union[_spatial_analyzer_values_pb2.ReportOutputOptions, _Mapping]] = ..., open_report: bool = ...) -> None: ...

class GenerateQuickReportFromTabOrderResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GenerateStandardHtmlReportRequest(_message.Message):
    __slots__ = ("html_output_file", "decimal_precision")
    HTML_OUTPUT_FILE_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    html_output_file: _spatial_analyzer_values_pb2.FileReference
    decimal_precision: int
    def __init__(self, html_output_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., decimal_precision: _Optional[int] = ...) -> None: ...

class GenerateStandardHtmlReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GenerateUpdateTemplatedReportRequest(_message.Message):
    __slots__ = ("report_template",)
    REPORT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    report_template: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, report_template: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GenerateUpdateTemplatedReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCustomTableCellDoubleRequest(_message.Message):
    __slots__ = ("table_name", "row", "column")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...

class GetCustomTableCellDoubleResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCustomTableCellStringRequest(_message.Message):
    __slots__ = ("table_name", "row", "column")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...

class GetCustomTableCellStringResult(_message.Message):
    __slots__ = ("value", "execution")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    value: str
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, value: _Optional[str] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetDefinedReportTagsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDefinedReportTagsResult(_message.Message):
    __slots__ = ("defined_tags", "execution")
    DEFINED_TAGS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    defined_tags: _containers.RepeatedScalarFieldContainer[str]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, defined_tags: _Optional[_Iterable[str]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetReportTagValueRequest(_message.Message):
    __slots__ = ("tag_name",)
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    def __init__(self, tag_name: _Optional[str] = ...) -> None: ...

class GetReportTagValueResult(_message.Message):
    __slots__ = ("tag_value_as_string", "tag_value_as_integer", "tag_value_as_double", "execution")
    TAG_VALUE_AS_STRING_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_AS_INTEGER_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_AS_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    tag_value_as_string: str
    tag_value_as_integer: int
    tag_value_as_double: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, tag_value_as_string: _Optional[str] = ..., tag_value_as_integer: _Optional[int] = ..., tag_value_as_double: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class HtmlDisplayBoardRequest(_message.Message):
    __slots__ = ("input_html_file", "show_board")
    INPUT_HTML_FILE_FIELD_NUMBER: _ClassVar[int]
    SHOW_BOARD_FIELD_NUMBER: _ClassVar[int]
    input_html_file: _spatial_analyzer_values_pb2.FileReference
    show_board: bool
    def __init__(self, input_html_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., show_board: bool = ...) -> None: ...

class HtmlDisplayBoardResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeCustomTableRequest(_message.Message):
    __slots__ = ("table_name", "decimal_precision")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    decimal_precision: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., decimal_precision: _Optional[int] = ...) -> None: ...

class MakeCustomTableResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeNewSaReportRequest(_message.Message):
    __slots__ = ("new_sa_report_name", "sa_report_template_optional")
    NEW_SA_REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    SA_REPORT_TEMPLATE_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    new_sa_report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    sa_report_template_optional: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, new_sa_report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., sa_report_template_optional: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class MakeNewSaReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MakeUtilityChartRequest(_message.Message):
    __slots__ = ("ascii_file_path", "chart_title_override", "output_picture_name", "show_chart_dialog", "plot_additional_xy_value", "x_value", "y_value")
    ASCII_FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CHART_TITLE_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_CHART_DIALOG_FIELD_NUMBER: _ClassVar[int]
    PLOT_ADDITIONAL_XY_VALUE_FIELD_NUMBER: _ClassVar[int]
    X_VALUE_FIELD_NUMBER: _ClassVar[int]
    Y_VALUE_FIELD_NUMBER: _ClassVar[int]
    ascii_file_path: _spatial_analyzer_values_pb2.FileReference
    chart_title_override: str
    output_picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    show_chart_dialog: bool
    plot_additional_xy_value: bool
    x_value: float
    y_value: float
    def __init__(self, ascii_file_path: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., chart_title_override: _Optional[str] = ..., output_picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., show_chart_dialog: bool = ..., plot_additional_xy_value: bool = ..., x_value: _Optional[float] = ..., y_value: _Optional[float] = ...) -> None: ...

class MakeUtilityChartResult(_message.Message):
    __slots__ = ("is_point_inside", "execution")
    IS_POINT_INSIDE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    is_point_inside: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, is_point_inside: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NotifyUserDoubleRequest(_message.Message):
    __slots__ = ("leading_text", "font", "reported_value", "decimal_precision", "display_timeout")
    LEADING_TEXT_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    REPORTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    leading_text: str
    font: _spatial_analyzer_values_pb2.Font
    reported_value: float
    decimal_precision: int
    display_timeout: int
    def __init__(self, leading_text: _Optional[str] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., reported_value: _Optional[float] = ..., decimal_precision: _Optional[int] = ..., display_timeout: _Optional[int] = ...) -> None: ...

class NotifyUserDoubleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NotifyUserHtmlRequest(_message.Message):
    __slots__ = ("html_file",)
    HTML_FILE_FIELD_NUMBER: _ClassVar[int]
    html_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, html_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class NotifyUserHtmlResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NotifyUserIntegerRequest(_message.Message):
    __slots__ = ("leading_text", "font", "reported_value", "display_timeout")
    LEADING_TEXT_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    REPORTED_VALUE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    leading_text: str
    font: _spatial_analyzer_values_pb2.Font
    reported_value: int
    display_timeout: int
    def __init__(self, leading_text: _Optional[str] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., reported_value: _Optional[int] = ..., display_timeout: _Optional[int] = ...) -> None: ...

class NotifyUserIntegerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class NotifyUserTextArrayRequest(_message.Message):
    __slots__ = ("notification_text", "font", "auto_expand_to_fit_text", "display_timeout")
    NOTIFICATION_TEXT_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    AUTO_EXPAND_TO_FIT_TEXT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    notification_text: _containers.RepeatedScalarFieldContainer[str]
    font: _spatial_analyzer_values_pb2.Font
    auto_expand_to_fit_text: bool
    display_timeout: int
    def __init__(self, notification_text: _Optional[_Iterable[str]] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ..., auto_expand_to_fit_text: bool = ..., display_timeout: _Optional[int] = ...) -> None: ...

class NotifyUserTextArrayResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class OutputSaReportToExcelRequest(_message.Message):
    __slots__ = ("report_name", "file_name", "show_file")
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_FILE_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    file_name: _spatial_analyzer_values_pb2.FileReference
    show_file: bool
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., show_file: bool = ...) -> None: ...

class OutputSaReportToExcelResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class OutputSaReportToPdfRequest(_message.Message):
    __slots__ = ("report_name", "file_name", "show_pdf")
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_PDF_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionObjectName
    file_name: _spatial_analyzer_values_pb2.FileReference
    show_pdf: bool
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., file_name: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., show_pdf: bool = ...) -> None: ...

class OutputSaReportToPdfResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class QuickReportRequest(_message.Message):
    __slots__ = ("item_name", "report_name_optional", "open_report")
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_NAME_OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    OPEN_REPORT_FIELD_NUMBER: _ClassVar[int]
    item_name: _spatial_analyzer_values_pb2.CollectionObjectName
    report_name_optional: str
    open_report: bool
    def __init__(self, item_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., report_name_optional: _Optional[str] = ..., open_report: bool = ...) -> None: ...

class QuickReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RefreshCalloutViewsInSaReportRequest(_message.Message):
    __slots__ = ("report_name",)
    REPORT_NAME_FIELD_NUMBER: _ClassVar[int]
    report_name: _spatial_analyzer_values_pb2.CollectionItemName
    def __init__(self, report_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ...) -> None: ...

class RefreshCalloutViewsInSaReportResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RefreshReportBarRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RefreshReportBarResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RemoveReportTagRequest(_message.Message):
    __slots__ = ("tag_name",)
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    def __init__(self, tag_name: _Optional[str] = ...) -> None: ...

class RemoveReportTagResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RenamePictureRequest(_message.Message):
    __slots__ = ("original_picture_name", "new_picture_name", "overwrite_if_exists")
    ORIGINAL_PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    original_picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    new_picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    overwrite_if_exists: bool
    def __init__(self, original_picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., new_picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., overwrite_if_exists: bool = ...) -> None: ...

class RenamePictureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveChartToJPegFileRequest(_message.Message):
    __slots__ = ("chart_to_save", "file_to_save_to")
    CHART_TO_SAVE_FIELD_NUMBER: _ClassVar[int]
    FILE_TO_SAVE_TO_FIELD_NUMBER: _ClassVar[int]
    chart_to_save: _spatial_analyzer_values_pb2.ChartName
    file_to_save_to: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, chart_to_save: _Optional[_Union[_spatial_analyzer_values_pb2.ChartName, _Mapping]] = ..., file_to_save_to: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SaveChartToJPegFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SaveCurrentViewBmpJpgPngGifTiffRequest(_message.Message):
    __slots__ = ("file_to_save_to", "render_scale_factor_1_0_uses_window_size")
    FILE_TO_SAVE_TO_FIELD_NUMBER: _ClassVar[int]
    RENDER_SCALE_FACTOR_1_0_USES_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_to_save_to: _spatial_analyzer_values_pb2.FileReference
    render_scale_factor_1_0_uses_window_size: float
    def __init__(self, file_to_save_to: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ..., render_scale_factor_1_0_uses_window_size: _Optional[float] = ...) -> None: ...

class SaveCurrentViewBmpJpgPngGifTiffResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableCellColorRequest(_message.Message):
    __slots__ = ("table_name", "row", "column", "foreground_color_name", "background_color_name")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    FOREGROUND_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_NAME_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    foreground_color_name: _spatial_analyzer_values_pb2.Color
    background_color_name: _spatial_analyzer_values_pb2.Color
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ..., foreground_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ..., background_color_name: _Optional[_Union[_spatial_analyzer_values_pb2.Color, _Mapping]] = ...) -> None: ...

class SetCustomTableCellColorResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableCellDoubleRequest(_message.Message):
    __slots__ = ("table_name", "row", "column", "value", "span", "decimal_precision")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    DECIMAL_PRECISION_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    value: float
    span: int
    decimal_precision: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ..., value: _Optional[float] = ..., span: _Optional[int] = ..., decimal_precision: _Optional[int] = ...) -> None: ...

class SetCustomTableCellDoubleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableCellFontRequest(_message.Message):
    __slots__ = ("table_name", "row", "column", "font")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    FONT_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    font: _spatial_analyzer_values_pb2.Font
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ..., font: _Optional[_Union[_spatial_analyzer_values_pb2.Font, _Mapping]] = ...) -> None: ...

class SetCustomTableCellFontResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableCellStringRequest(_message.Message):
    __slots__ = ("table_name", "row", "column", "value", "span")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    value: str
    span: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ..., value: _Optional[str] = ..., span: _Optional[int] = ...) -> None: ...

class SetCustomTableCellStringResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableHeaderCellRequest(_message.Message):
    __slots__ = ("table_name", "row", "column", "header_text", "span")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    HEADER_TEXT_FIELD_NUMBER: _ClassVar[int]
    SPAN_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    column: int
    header_text: str
    span: int
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., column: _Optional[int] = ..., header_text: _Optional[str] = ..., span: _Optional[int] = ...) -> None: ...

class SetCustomTableHeaderCellResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableHeaderRowRequest(_message.Message):
    __slots__ = ("table_name", "row", "value")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    ROW_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    row: int
    value: str
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., row: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class SetCustomTableHeaderRowResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCustomTableTitleRequest(_message.Message):
    __slots__ = ("table_name", "title_line_1", "title_line_2")
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_LINE_1_FIELD_NUMBER: _ClassVar[int]
    TITLE_LINE_2_FIELD_NUMBER: _ClassVar[int]
    table_name: _spatial_analyzer_values_pb2.CollectionObjectName
    title_line_1: str
    title_line_2: str
    def __init__(self, table_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., title_line_1: _Optional[str] = ..., title_line_2: _Optional[str] = ...) -> None: ...

class SetCustomTableTitleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetPointGroupReportOptionsRequest(_message.Message):
    __slots__ = ("point_group", "coordinate_system", "show_x_component", "show_y_component", "show_z_component", "show_offsets", "show_uncertainty", "show_notes", "show_measurements", "show_measurement_details", "show_pointing_error_worst_angle", "sort_by_point_names", "make_default", "apply_to_all")
    POINT_GROUP_FIELD_NUMBER: _ClassVar[int]
    COORDINATE_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    SHOW_X_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SHOW_Y_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SHOW_Z_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SHOW_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    SHOW_UNCERTAINTY_FIELD_NUMBER: _ClassVar[int]
    SHOW_NOTES_FIELD_NUMBER: _ClassVar[int]
    SHOW_MEASUREMENTS_FIELD_NUMBER: _ClassVar[int]
    SHOW_MEASUREMENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SHOW_POINTING_ERROR_WORST_ANGLE_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    MAKE_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    APPLY_TO_ALL_FIELD_NUMBER: _ClassVar[int]
    point_group: _spatial_analyzer_values_pb2.CollectionObjectName
    coordinate_system: _spatial_analyzer_values_pb2.CoordinateSystemType
    show_x_component: bool
    show_y_component: bool
    show_z_component: bool
    show_offsets: bool
    show_uncertainty: bool
    show_notes: bool
    show_measurements: bool
    show_measurement_details: bool
    show_pointing_error_worst_angle: bool
    sort_by_point_names: bool
    make_default: bool
    apply_to_all: bool
    def __init__(self, point_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., coordinate_system: _Optional[_Union[_spatial_analyzer_values_pb2.CoordinateSystemType, str]] = ..., show_x_component: bool = ..., show_y_component: bool = ..., show_z_component: bool = ..., show_offsets: bool = ..., show_uncertainty: bool = ..., show_notes: bool = ..., show_measurements: bool = ..., show_measurement_details: bool = ..., show_pointing_error_worst_angle: bool = ..., sort_by_point_names: bool = ..., make_default: bool = ..., apply_to_all: bool = ...) -> None: ...

class SetPointGroupReportOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRelationshipReportOptionsRequest(_message.Message):
    __slots__ = ("relationship_name", "report_options")
    RELATIONSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    REPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    relationship_name: _spatial_analyzer_values_pb2.CollectionObjectName
    report_options: _spatial_analyzer_values_pb2.PointDeltaReportOptions
    def __init__(self, relationship_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., report_options: _Optional[_Union[_spatial_analyzer_values_pb2.PointDeltaReportOptions, _Mapping]] = ...) -> None: ...

class SetRelationshipReportOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportBarVisibilityRequest(_message.Message):
    __slots__ = ("show_report_bar",)
    SHOW_REPORT_BAR_FIELD_NUMBER: _ClassVar[int]
    show_report_bar: bool
    def __init__(self, show_report_bar: bool = ...) -> None: ...

class SetReportBarVisibilityResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportOptionsForObjectRequest(_message.Message):
    __slots__ = ("object",)
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    object: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, object: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetReportOptionsForObjectResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportTagValueFromDoubleRequest(_message.Message):
    __slots__ = ("tag_name", "tag_value")
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    tag_value: float
    def __init__(self, tag_name: _Optional[str] = ..., tag_value: _Optional[float] = ...) -> None: ...

class SetReportTagValueFromDoubleResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportTagValueFromIntegerRequest(_message.Message):
    __slots__ = ("tag_name", "tag_value")
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    tag_value: int
    def __init__(self, tag_name: _Optional[str] = ..., tag_value: _Optional[int] = ...) -> None: ...

class SetReportTagValueFromIntegerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetReportTagValueFromStringRequest(_message.Message):
    __slots__ = ("tag_name", "tag_value")
    TAG_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_VALUE_FIELD_NUMBER: _ClassVar[int]
    tag_name: str
    tag_value: str
    def __init__(self, tag_name: _Optional[str] = ..., tag_value: _Optional[str] = ...) -> None: ...

class SetReportTagValueFromStringResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetScaleForPictureRequest(_message.Message):
    __slots__ = ("picture_name", "scale")
    PICTURE_NAME_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    picture_name: _spatial_analyzer_values_pb2.CollectionItemName
    scale: float
    def __init__(self, picture_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionItemName, _Mapping]] = ..., scale: _Optional[float] = ...) -> None: ...

class SetScaleForPictureResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetVectorGroupReportOptionsRequest(_message.Message):
    __slots__ = ("vector_group", "report_options")
    VECTOR_GROUP_FIELD_NUMBER: _ClassVar[int]
    REPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    vector_group: _spatial_analyzer_values_pb2.CollectionObjectName
    report_options: _spatial_analyzer_values_pb2.PointDeltaReportOptions
    def __init__(self, vector_group: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., report_options: _Optional[_Union[_spatial_analyzer_values_pb2.PointDeltaReportOptions, _Mapping]] = ...) -> None: ...

class SetVectorGroupReportOptionsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
