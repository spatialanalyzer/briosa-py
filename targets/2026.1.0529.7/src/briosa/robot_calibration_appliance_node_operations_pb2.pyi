from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddCalibrationApplianceNodeRequest(_message.Message):
    __slots__ = ("calibration_appliance_node_to_add",)
    CALIBRATION_APPLIANCE_NODE_TO_ADD_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node_to_add: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node_to_add: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class AddCalibrationApplianceNodeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ClearCalibrationApplianceNodeTrapManagerRequestsRequest(_message.Message):
    __slots__ = ("calibration_appliance_node",)
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ClearCalibrationApplianceNodeTrapManagerRequestsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ConnectDisconnectCalibrationApplianceNodeRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "connect")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    CONNECT_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    connect: bool
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., connect: bool = ...) -> None: ...

class ConnectDisconnectCalibrationApplianceNodeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteCalibrationApplianceNodeRequest(_message.Message):
    __slots__ = ("calibration_appliance_node_to_delete",)
    CALIBRATION_APPLIANCE_NODE_TO_DELETE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node_to_delete: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node_to_delete: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class DeleteCalibrationApplianceNodeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableCalibrationApplianceNodeInstrumentAutoPointRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "enable_instrument_auto_point")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_INSTRUMENT_AUTO_POINT_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    enable_instrument_auto_point: bool
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., enable_instrument_auto_point: bool = ...) -> None: ...

class EnableDisableCalibrationApplianceNodeInstrumentAutoPointResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class EnableDisableCalibrationApplianceNodeTrapManagerRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "enable")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    enable: bool
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., enable: bool = ...) -> None: ...

class EnableDisableCalibrationApplianceNodeTrapManagerResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceNodeDataRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "real_value_count")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    REAL_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    real_value_count: int
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., real_value_count: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceNodeDataResult(_message.Message):
    __slots__ = ("real_values", "execution")
    REAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    real_values: _containers.RepeatedScalarFieldContainer[float]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, real_values: _Optional[_Iterable[float]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceNodeIntegerValueRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "index_offset")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    index_offset: int
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., index_offset: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceNodeIntegerValueResult(_message.Message):
    __slots__ = ("integer_value", "execution")
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    integer_value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, integer_value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceNodeRealValueRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "index_offset")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    index_offset: int
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., index_offset: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceNodeRealValueResult(_message.Message):
    __slots__ = ("real_value", "execution")
    REAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    real_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, real_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceNodeStatusRequest(_message.Message):
    __slots__ = ("calibration_appliance_node",)
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceNodeStatusResult(_message.Message):
    __slots__ = ("instrument_connected", "calibration_appliance_connected", "execution")
    INSTRUMENT_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_APPLIANCE_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    instrument_connected: bool
    calibration_appliance_connected: bool
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, instrument_connected: bool = ..., calibration_appliance_connected: bool = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeCalibrationApplianceIpAddressRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "calibration_appliance_ip_address")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_APPLIANCE_IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    calibration_appliance_ip_address: str
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., calibration_appliance_ip_address: _Optional[str] = ...) -> None: ...

class SetCalibrationApplianceNodeCalibrationApplianceIpAddressResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeDataRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "real_values")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    REAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    real_values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., real_values: _Optional[_Iterable[float]] = ...) -> None: ...

class SetCalibrationApplianceNodeDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeDisplayRobotRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "machine_id")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeDisplayRobotResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeInstrumentDwellTimeRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "measurement_dwell_time")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_DWELL_TIME_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_dwell_time: float
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_dwell_time: _Optional[float] = ...) -> None: ...

class SetCalibrationApplianceNodeInstrumentDwellTimeResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeInstrumentRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "instrument")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    instrument: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., instrument: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeInstrumentResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeIntegerValueRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "index_offset", "integer_value")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    index_offset: int
    integer_value: int
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., index_offset: _Optional[int] = ..., integer_value: _Optional[int] = ...) -> None: ...

class SetCalibrationApplianceNodeIntegerValueResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementFrameRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "measurement_reference_frame")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementOffsetTransformRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "measurement_offset_transform")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_OFFSET_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_offset_transform: _spatial_analyzer_values_pb2.Transform
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_offset_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementOffsetTransformResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementPointGroupRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "point_group_name")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    POINT_GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    point_group_name: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., point_group_name: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementPointGroupResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementProfileRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "measurement_profile")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_profile: str
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_profile: _Optional[str] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementProfileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementTargetRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "measurement_target")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_TARGET_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    measurement_target: str
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., measurement_target: _Optional[str] = ...) -> None: ...

class SetCalibrationApplianceNodeMeasurementTargetResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeRealValueRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "index_offset", "real_value")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    REAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    index_offset: int
    real_value: float
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., index_offset: _Optional[int] = ..., real_value: _Optional[float] = ...) -> None: ...

class SetCalibrationApplianceNodeRealValueResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceNodeTrappingNodeIdRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "trapping_node_id")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    TRAPPING_NODE_ID_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    trapping_node_id: int
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., trapping_node_id: _Optional[int] = ...) -> None: ...

class SetCalibrationApplianceNodeTrappingNodeIdResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SkipCalibrationApplianceNodeMeasurementRequest(_message.Message):
    __slots__ = ("calibration_appliance_node",)
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class SkipCalibrationApplianceNodeMeasurementResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class UpdateCalibrationApplianceNodeDisplayRobotJointsRequest(_message.Message):
    __slots__ = ("calibration_appliance_node", "enable_display_robot_joint_updates")
    CALIBRATION_APPLIANCE_NODE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DISPLAY_ROBOT_JOINT_UPDATES_FIELD_NUMBER: _ClassVar[int]
    calibration_appliance_node: _spatial_analyzer_values_pb2.CollectionObjectName
    enable_display_robot_joint_updates: bool
    def __init__(self, calibration_appliance_node: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., enable_display_robot_joint_updates: bool = ...) -> None: ...

class UpdateCalibrationApplianceNodeDisplayRobotJointsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
