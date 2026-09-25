from briosa import operation_outcomes_pb2 as _operation_outcomes_pb2
from briosa import spatial_analyzer_values_pb2 as _spatial_analyzer_values_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RobotActiveJointComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_ACTIVE_JOINT_COMPONENT_UNSPECIFIED: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_NONE: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_X: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_Y: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_Z: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_RX: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_RY: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_RZ: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_ALPHA: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_A: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_D: _ClassVar[RobotActiveJointComponent]
    ROBOT_ACTIVE_JOINT_COMPONENT_THETA: _ClassVar[RobotActiveJointComponent]

class RobotModelLinkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ROBOT_MODEL_LINK_TYPE_UNSPECIFIED: _ClassVar[RobotModelLinkType]
    ROBOT_MODEL_LINK_TYPE_DH: _ClassVar[RobotModelLinkType]
    ROBOT_MODEL_LINK_TYPE_SIX_DOF: _ClassVar[RobotModelLinkType]
ROBOT_ACTIVE_JOINT_COMPONENT_UNSPECIFIED: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_NONE: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_X: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_Y: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_Z: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_RX: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_RY: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_RZ: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_ALPHA: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_A: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_D: RobotActiveJointComponent
ROBOT_ACTIVE_JOINT_COMPONENT_THETA: RobotActiveJointComponent
ROBOT_MODEL_LINK_TYPE_UNSPECIFIED: RobotModelLinkType
ROBOT_MODEL_LINK_TYPE_DH: RobotModelLinkType
ROBOT_MODEL_LINK_TYPE_SIX_DOF: RobotModelLinkType

class AddRobotMachineManipKinRequest(_message.Message):
    __slots__ = ("manip_kin_file",)
    MANIP_KIN_FILE_FIELD_NUMBER: _ClassVar[int]
    manip_kin_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, manip_kin_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class AddRobotMachineManipKinResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class AddRobotMachineSaMachineRequest(_message.Message):
    __slots__ = ("sa_machine_file",)
    SA_MACHINE_FILE_FIELD_NUMBER: _ClassVar[int]
    sa_machine_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, sa_machine_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class AddRobotMachineSaMachineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ComputeRobotMachineAdjustedGoalFrameRequest(_message.Message):
    __slots__ = ("original_goal_frame", "last_adjusted_goal_frame", "actual_measured_frame", "modified_goal_frame")
    ORIGINAL_GOAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    LAST_ADJUSTED_GOAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    ACTUAL_MEASURED_FRAME_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_GOAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    original_goal_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    last_adjusted_goal_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    actual_measured_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    modified_goal_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    def __init__(self, original_goal_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., last_adjusted_goal_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., actual_measured_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., modified_goal_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ...) -> None: ...

class ComputeRobotMachineAdjustedGoalFrameResult(_message.Message):
    __slots__ = ("transform_value", "execution")
    TRANSFORM_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    transform_value: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, transform_value: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class CreateRobotCalibrationRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ...) -> None: ...

class CreateRobotCalibrationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteRobotCalibrationRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ...) -> None: ...

class DeleteRobotCalibrationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class DeleteRobotMachineRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ...) -> None: ...

class DeleteRobotMachineResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceDataRequest(_message.Message):
    __slots__ = ("real_value_count",)
    REAL_VALUE_COUNT_FIELD_NUMBER: _ClassVar[int]
    real_value_count: int
    def __init__(self, real_value_count: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceDataResult(_message.Message):
    __slots__ = ("real_values", "execution")
    REAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    real_values: _containers.RepeatedScalarFieldContainer[float]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, real_values: _Optional[_Iterable[float]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceIntegerValueRequest(_message.Message):
    __slots__ = ("index_offset",)
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    index_offset: int
    def __init__(self, index_offset: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceIntegerValueResult(_message.Message):
    __slots__ = ("integer_value", "execution")
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    integer_value: int
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, integer_value: _Optional[int] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetCalibrationApplianceRealValueRequest(_message.Message):
    __slots__ = ("index_offset",)
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    index_offset: int
    def __init__(self, index_offset: _Optional[int] = ...) -> None: ...

class GetCalibrationApplianceRealValueResult(_message.Message):
    __slots__ = ("real_value", "execution")
    REAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    real_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, real_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRobotMachineModelLinkParametersRequest(_message.Message):
    __slots__ = ("machine_id", "link_name")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    link_name: str
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., link_name: _Optional[str] = ...) -> None: ...

class GetRobotMachineModelLinkParametersResult(_message.Message):
    __slots__ = ("link_type", "dh_alpha_component", "dh_a_component", "dh_d_component", "dh_theta_component", "dh_x_axis_deflection_factor", "dh_y_axis_deflection_factor", "dh_z_axis_deflection_factor", "six_dof_x_component", "six_dof_y_component", "six_dof_z_component", "six_dof_rx_component", "six_dof_ry_component", "six_dof_rz_component", "active_joint_component", "encoder_value", "encoder_offset_value", "minimum_encoder_limit", "maximum_encoder_limit", "encoder_sense_negative", "include_additional_encoder", "additional_encoder_index_offset", "additional_encoder_sense_negative", "segment_origin_mass_kg", "segment_cg_mass_kg", "segment_cg_in_segment", "execution")
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DH_ALPHA_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_A_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_D_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_THETA_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_X_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DH_Y_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DH_Z_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_X_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_Y_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_Z_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RX_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RY_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RZ_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_JOINT_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ENCODER_VALUE_FIELD_NUMBER: _ClassVar[int]
    ENCODER_OFFSET_VALUE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ENCODER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ENCODER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENCODER_SENSE_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ADDITIONAL_ENCODER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENCODER_INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENCODER_SENSE_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ORIGIN_MASS_KG_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_CG_MASS_KG_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_CG_IN_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    link_type: RobotModelLinkType
    dh_alpha_component: float
    dh_a_component: float
    dh_d_component: float
    dh_theta_component: float
    dh_x_axis_deflection_factor: float
    dh_y_axis_deflection_factor: float
    dh_z_axis_deflection_factor: float
    six_dof_x_component: float
    six_dof_y_component: float
    six_dof_z_component: float
    six_dof_rx_component: float
    six_dof_ry_component: float
    six_dof_rz_component: float
    active_joint_component: RobotActiveJointComponent
    encoder_value: float
    encoder_offset_value: float
    minimum_encoder_limit: float
    maximum_encoder_limit: float
    encoder_sense_negative: bool
    include_additional_encoder: bool
    additional_encoder_index_offset: int
    additional_encoder_sense_negative: bool
    segment_origin_mass_kg: float
    segment_cg_mass_kg: float
    segment_cg_in_segment: _spatial_analyzer_values_pb2.Vector
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, link_type: _Optional[_Union[RobotModelLinkType, str]] = ..., dh_alpha_component: _Optional[float] = ..., dh_a_component: _Optional[float] = ..., dh_d_component: _Optional[float] = ..., dh_theta_component: _Optional[float] = ..., dh_x_axis_deflection_factor: _Optional[float] = ..., dh_y_axis_deflection_factor: _Optional[float] = ..., dh_z_axis_deflection_factor: _Optional[float] = ..., six_dof_x_component: _Optional[float] = ..., six_dof_y_component: _Optional[float] = ..., six_dof_z_component: _Optional[float] = ..., six_dof_rx_component: _Optional[float] = ..., six_dof_ry_component: _Optional[float] = ..., six_dof_rz_component: _Optional[float] = ..., active_joint_component: _Optional[_Union[RobotActiveJointComponent, str]] = ..., encoder_value: _Optional[float] = ..., encoder_offset_value: _Optional[float] = ..., minimum_encoder_limit: _Optional[float] = ..., maximum_encoder_limit: _Optional[float] = ..., encoder_sense_negative: bool = ..., include_additional_encoder: bool = ..., additional_encoder_index_offset: _Optional[int] = ..., additional_encoder_sense_negative: bool = ..., segment_origin_mass_kg: _Optional[float] = ..., segment_cg_mass_kg: _Optional[float] = ..., segment_cg_in_segment: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRobotMachineParameterRequest(_message.Message):
    __slots__ = ("machine_id", "parameter_name")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    parameter_name: str
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., parameter_name: _Optional[str] = ...) -> None: ...

class GetRobotMachineParameterResult(_message.Message):
    __slots__ = ("parameter_value", "execution")
    PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    parameter_value: float
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, parameter_value: _Optional[float] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class GetRobotPoseForAFrameRequest(_message.Message):
    __slots__ = ("machine_id", "goal_frame", "reference_pose", "goal_pose_count")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_FRAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_POSE_FIELD_NUMBER: _ClassVar[int]
    GOAL_POSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    goal_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    reference_pose: _containers.RepeatedScalarFieldContainer[float]
    goal_pose_count: int
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., goal_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., reference_pose: _Optional[_Iterable[float]] = ..., goal_pose_count: _Optional[int] = ...) -> None: ...

class GetRobotPoseForAFrameResult(_message.Message):
    __slots__ = ("goal_pose", "execution")
    GOAL_POSE_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    goal_pose: _containers.RepeatedScalarFieldContainer[float]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, goal_pose: _Optional[_Iterable[float]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportPosesMatchToFramesRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "frame_names", "csv_joint_set_file")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    FRAME_NAMES_FIELD_NUMBER: _ClassVar[int]
    CSV_JOINT_SET_FILE_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    frame_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    csv_joint_set_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., frame_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., csv_joint_set_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportPosesMatchToFramesResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class ImportPosesMatchToMeasurementsRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "point_names", "csv_joint_set_file")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    POINT_NAMES_FIELD_NUMBER: _ClassVar[int]
    CSV_JOINT_SET_FILE_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    point_names: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.PointName]
    csv_joint_set_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., point_names: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.PointName, _Mapping]]] = ..., csv_joint_set_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class ImportPosesMatchToMeasurementsResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveRobotMachineThroughPathRequest(_message.Message):
    __slots__ = ("machine_id", "path_frames", "use_sa_kinematics", "linear_segments", "acknowledge_arrival")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FRAMES_FIELD_NUMBER: _ClassVar[int]
    USE_SA_KINEMATICS_FIELD_NUMBER: _ClassVar[int]
    LINEAR_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGE_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    path_frames: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    use_sa_kinematics: bool
    linear_segments: bool
    acknowledge_arrival: bool
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., path_frames: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., use_sa_kinematics: bool = ..., linear_segments: bool = ..., acknowledge_arrival: bool = ...) -> None: ...

class MoveRobotMachineThroughPathResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveRobotMachineToFrameRequest(_message.Message):
    __slots__ = ("machine_id", "destination_frame", "use_sa_kinematics", "acknowledge_arrival")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FRAME_FIELD_NUMBER: _ClassVar[int]
    USE_SA_KINEMATICS_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGE_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    destination_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    use_sa_kinematics: bool
    acknowledge_arrival: bool
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., destination_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., use_sa_kinematics: bool = ..., acknowledge_arrival: bool = ...) -> None: ...

class MoveRobotMachineToFrameResult(_message.Message):
    __slots__ = ("actual_transform_in_working", "execution")
    ACTUAL_TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    actual_transform_in_working: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, actual_transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveRobotMachineToJointPoseSixDofRequest(_message.Message):
    __slots__ = ("machine_id", "joint_1", "joint_2", "joint_3", "joint_4", "joint_5", "joint_6")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    JOINT_1_FIELD_NUMBER: _ClassVar[int]
    JOINT_2_FIELD_NUMBER: _ClassVar[int]
    JOINT_3_FIELD_NUMBER: _ClassVar[int]
    JOINT_4_FIELD_NUMBER: _ClassVar[int]
    JOINT_5_FIELD_NUMBER: _ClassVar[int]
    JOINT_6_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    joint_1: float
    joint_2: float
    joint_3: float
    joint_4: float
    joint_5: float
    joint_6: float
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., joint_1: _Optional[float] = ..., joint_2: _Optional[float] = ..., joint_3: _Optional[float] = ..., joint_4: _Optional[float] = ..., joint_5: _Optional[float] = ..., joint_6: _Optional[float] = ...) -> None: ...

class MoveRobotMachineToJointPoseSixDofResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class MoveRobotMachineToNamedDestinationRequest(_message.Message):
    __slots__ = ("machine_id", "destination_name", "acknowledge_arrival")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_NAME_FIELD_NUMBER: _ClassVar[int]
    ACKNOWLEDGE_ARRIVAL_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    destination_name: str
    acknowledge_arrival: bool
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., destination_name: _Optional[str] = ..., acknowledge_arrival: bool = ...) -> None: ...

class MoveRobotMachineToNamedDestinationResult(_message.Message):
    __slots__ = ("actual_transform_in_working", "execution")
    ACTUAL_TRANSFORM_IN_WORKING_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    actual_transform_in_working: _spatial_analyzer_values_pb2.Transform
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, actual_transform_in_working: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PerformRobotCalibrationAlternateRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "set_current_base_as_nominal", "base_degrees_of_freedom", "robot_degrees_of_freedom", "tool_degrees_of_freedom", "show_interface", "allowed_outlier_rejection_count", "allowable_maximum_error", "allowable_average_error")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SET_CURRENT_BASE_AS_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    BASE_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    ROBOT_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    TOOL_DEGREES_OF_FREEDOM_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OUTLIER_REJECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOWABLE_MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    ALLOWABLE_AVERAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    set_current_base_as_nominal: bool
    base_degrees_of_freedom: str
    robot_degrees_of_freedom: str
    tool_degrees_of_freedom: str
    show_interface: bool
    allowed_outlier_rejection_count: int
    allowable_maximum_error: float
    allowable_average_error: float
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., set_current_base_as_nominal: bool = ..., base_degrees_of_freedom: _Optional[str] = ..., robot_degrees_of_freedom: _Optional[str] = ..., tool_degrees_of_freedom: _Optional[str] = ..., show_interface: bool = ..., allowed_outlier_rejection_count: _Optional[int] = ..., allowable_maximum_error: _Optional[float] = ..., allowable_average_error: _Optional[float] = ...) -> None: ...

class PerformRobotCalibrationAlternateResult(_message.Message):
    __slots__ = ("metrics", "execution")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    metrics: RobotCalibrationMetrics
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, metrics: _Optional[_Union[RobotCalibrationMetrics, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class PerformRobotCalibrationRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "set_current_base_as_nominal", "show_interface", "allowed_outlier_rejection_count", "allowable_maximum_error", "allowable_average_error")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    SET_CURRENT_BASE_AS_NOMINAL_FIELD_NUMBER: _ClassVar[int]
    SHOW_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_OUTLIER_REJECTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    ALLOWABLE_MAXIMUM_ERROR_FIELD_NUMBER: _ClassVar[int]
    ALLOWABLE_AVERAGE_ERROR_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    set_current_base_as_nominal: bool
    show_interface: bool
    allowed_outlier_rejection_count: int
    allowable_maximum_error: float
    allowable_average_error: float
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., set_current_base_as_nominal: bool = ..., show_interface: bool = ..., allowed_outlier_rejection_count: _Optional[int] = ..., allowable_maximum_error: _Optional[float] = ..., allowable_average_error: _Optional[float] = ...) -> None: ...

class PerformRobotCalibrationResult(_message.Message):
    __slots__ = ("metrics", "execution")
    METRICS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    metrics: RobotCalibrationMetrics
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, metrics: _Optional[_Union[RobotCalibrationMetrics, _Mapping]] = ..., execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class RobotCalibrationMetrics(_message.Message):
    __slots__ = ("xyz_max", "xyz_average", "xyz_rms", "orient_max", "orient_average", "orient_rms", "robustness")
    XYZ_MAX_FIELD_NUMBER: _ClassVar[int]
    XYZ_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    XYZ_RMS_FIELD_NUMBER: _ClassVar[int]
    ORIENT_MAX_FIELD_NUMBER: _ClassVar[int]
    ORIENT_AVERAGE_FIELD_NUMBER: _ClassVar[int]
    ORIENT_RMS_FIELD_NUMBER: _ClassVar[int]
    ROBUSTNESS_FIELD_NUMBER: _ClassVar[int]
    xyz_max: float
    xyz_average: float
    xyz_rms: float
    orient_max: float
    orient_average: float
    orient_rms: float
    robustness: float
    def __init__(self, xyz_max: _Optional[float] = ..., xyz_average: _Optional[float] = ..., xyz_rms: _Optional[float] = ..., orient_max: _Optional[float] = ..., orient_average: _Optional[float] = ..., orient_rms: _Optional[float] = ..., robustness: _Optional[float] = ...) -> None: ...

class SetActiveRobotCalibrationRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ...) -> None: ...

class SetActiveRobotCalibrationResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceDataRequest(_message.Message):
    __slots__ = ("real_values",)
    REAL_VALUES_FIELD_NUMBER: _ClassVar[int]
    real_values: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, real_values: _Optional[_Iterable[float]] = ...) -> None: ...

class SetCalibrationApplianceDataResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceIntegerValueRequest(_message.Message):
    __slots__ = ("index_offset", "integer_value")
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    INTEGER_VALUE_FIELD_NUMBER: _ClassVar[int]
    index_offset: int
    integer_value: int
    def __init__(self, index_offset: _Optional[int] = ..., integer_value: _Optional[int] = ...) -> None: ...

class SetCalibrationApplianceIntegerValueResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetCalibrationApplianceRealValueRequest(_message.Message):
    __slots__ = ("index_offset", "real_value")
    INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    REAL_VALUE_FIELD_NUMBER: _ClassVar[int]
    index_offset: int
    real_value: float
    def __init__(self, index_offset: _Optional[int] = ..., real_value: _Optional[float] = ...) -> None: ...

class SetCalibrationApplianceRealValueResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRobotCalibrationMeasurementOffsetInToolFrameRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "measurement_frame")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    MEASUREMENT_FRAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    measurement_frame: _spatial_analyzer_values_pb2.Transform
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., measurement_frame: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetRobotCalibrationMeasurementOffsetInToolFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRobotCalibrationToolFrameRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "tool_frame")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_FRAME_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    tool_frame: _spatial_analyzer_values_pb2.Transform
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., tool_frame: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ...) -> None: ...

class SetRobotCalibrationToolFrameResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRobotMachineBaseTransformRequest(_message.Message):
    __slots__ = ("machine_id", "destination_transform", "reference_frame", "number_of_steps")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FRAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_STEPS_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    destination_transform: _spatial_analyzer_values_pb2.Transform
    reference_frame: _spatial_analyzer_values_pb2.CollectionObjectName
    number_of_steps: int
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., destination_transform: _Optional[_Union[_spatial_analyzer_values_pb2.Transform, _Mapping]] = ..., reference_frame: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]] = ..., number_of_steps: _Optional[int] = ...) -> None: ...

class SetRobotMachineBaseTransformResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRobotMachineModelLinkParametersRequest(_message.Message):
    __slots__ = ("machine_id", "link_name", "link_type", "dh_alpha_component", "dh_a_component", "dh_d_component", "dh_theta_component", "dh_x_axis_deflection_factor", "dh_y_axis_deflection_factor", "dh_z_axis_deflection_factor", "six_dof_x_component", "six_dof_y_component", "six_dof_z_component", "six_dof_rx_component", "six_dof_ry_component", "six_dof_rz_component", "active_joint_component", "encoder_offset_value", "minimum_encoder_limit", "maximum_encoder_limit", "encoder_sense_negative", "include_additional_encoder", "additional_encoder_index_offset", "additional_encoder_sense_negative", "segment_origin_mass_kg", "segment_cg_mass_kg", "segment_cg_in_segment")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    LINK_NAME_FIELD_NUMBER: _ClassVar[int]
    LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
    DH_ALPHA_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_A_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_D_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_THETA_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    DH_X_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DH_Y_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    DH_Z_AXIS_DEFLECTION_FACTOR_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_X_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_Y_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_Z_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RX_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RY_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    SIX_DOF_RZ_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_JOINT_COMPONENT_FIELD_NUMBER: _ClassVar[int]
    ENCODER_OFFSET_VALUE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_ENCODER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ENCODER_LIMIT_FIELD_NUMBER: _ClassVar[int]
    ENCODER_SENSE_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ADDITIONAL_ENCODER_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENCODER_INDEX_OFFSET_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_ENCODER_SENSE_NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_ORIGIN_MASS_KG_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_CG_MASS_KG_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_CG_IN_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    link_name: str
    link_type: RobotModelLinkType
    dh_alpha_component: float
    dh_a_component: float
    dh_d_component: float
    dh_theta_component: float
    dh_x_axis_deflection_factor: float
    dh_y_axis_deflection_factor: float
    dh_z_axis_deflection_factor: float
    six_dof_x_component: float
    six_dof_y_component: float
    six_dof_z_component: float
    six_dof_rx_component: float
    six_dof_ry_component: float
    six_dof_rz_component: float
    active_joint_component: RobotActiveJointComponent
    encoder_offset_value: float
    minimum_encoder_limit: float
    maximum_encoder_limit: float
    encoder_sense_negative: bool
    include_additional_encoder: bool
    additional_encoder_index_offset: int
    additional_encoder_sense_negative: bool
    segment_origin_mass_kg: float
    segment_cg_mass_kg: float
    segment_cg_in_segment: _spatial_analyzer_values_pb2.Vector
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., link_name: _Optional[str] = ..., link_type: _Optional[_Union[RobotModelLinkType, str]] = ..., dh_alpha_component: _Optional[float] = ..., dh_a_component: _Optional[float] = ..., dh_d_component: _Optional[float] = ..., dh_theta_component: _Optional[float] = ..., dh_x_axis_deflection_factor: _Optional[float] = ..., dh_y_axis_deflection_factor: _Optional[float] = ..., dh_z_axis_deflection_factor: _Optional[float] = ..., six_dof_x_component: _Optional[float] = ..., six_dof_y_component: _Optional[float] = ..., six_dof_z_component: _Optional[float] = ..., six_dof_rx_component: _Optional[float] = ..., six_dof_ry_component: _Optional[float] = ..., six_dof_rz_component: _Optional[float] = ..., active_joint_component: _Optional[_Union[RobotActiveJointComponent, str]] = ..., encoder_offset_value: _Optional[float] = ..., minimum_encoder_limit: _Optional[float] = ..., maximum_encoder_limit: _Optional[float] = ..., encoder_sense_negative: bool = ..., include_additional_encoder: bool = ..., additional_encoder_index_offset: _Optional[int] = ..., additional_encoder_sense_negative: bool = ..., segment_origin_mass_kg: _Optional[float] = ..., segment_cg_mass_kg: _Optional[float] = ..., segment_cg_in_segment: _Optional[_Union[_spatial_analyzer_values_pb2.Vector, _Mapping]] = ...) -> None: ...

class SetRobotMachineModelLinkParametersResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SetRobotMachineParameterRequest(_message.Message):
    __slots__ = ("machine_id", "parameter_name", "parameter_value")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    parameter_name: str
    parameter_value: float
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., parameter_name: _Optional[str] = ..., parameter_value: _Optional[float] = ...) -> None: ...

class SetRobotMachineParameterResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class SimulateRobotMachinePathOutputCsvFileRequest(_message.Message):
    __slots__ = ("machine_id", "path_frames", "output_csv_file")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FRAMES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CSV_FILE_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    path_frames: _containers.RepeatedCompositeFieldContainer[_spatial_analyzer_values_pb2.CollectionObjectName]
    output_csv_file: _spatial_analyzer_values_pb2.FileReference
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., path_frames: _Optional[_Iterable[_Union[_spatial_analyzer_values_pb2.CollectionObjectName, _Mapping]]] = ..., output_csv_file: _Optional[_Union[_spatial_analyzer_values_pb2.FileReference, _Mapping]] = ...) -> None: ...

class SimulateRobotMachinePathOutputCsvFileResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartRobotMachineInterfaceRequest(_message.Message):
    __slots__ = ("machine_id", "interface_type", "run_in_simulation")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RUN_IN_SIMULATION_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    interface_type: int
    run_in_simulation: bool
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., interface_type: _Optional[int] = ..., run_in_simulation: bool = ...) -> None: ...

class StartRobotMachineInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StartStopRobotCalibrationTrappingRequest(_message.Message):
    __slots__ = ("machine_id", "calibration_name", "instrument_id", "start_trapping")
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    CALIBRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    START_TRAPPING_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionMachineId
    calibration_name: str
    instrument_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    start_trapping: bool
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionMachineId, _Mapping]] = ..., calibration_name: _Optional[str] = ..., instrument_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ..., start_trapping: bool = ...) -> None: ...

class StartStopRobotCalibrationTrappingResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...

class StopRobotMachineInterfaceRequest(_message.Message):
    __slots__ = ("machine_id",)
    MACHINE_ID_FIELD_NUMBER: _ClassVar[int]
    machine_id: _spatial_analyzer_values_pb2.CollectionInstrumentId
    def __init__(self, machine_id: _Optional[_Union[_spatial_analyzer_values_pb2.CollectionInstrumentId, _Mapping]] = ...) -> None: ...

class StopRobotMachineInterfaceResult(_message.Message):
    __slots__ = ("execution",)
    EXECUTION_FIELD_NUMBER: _ClassVar[int]
    execution: _operation_outcomes_pb2.MpExecutionDetails
    def __init__(self, execution: _Optional[_Union[_operation_outcomes_pb2.MpExecutionDetails, _Mapping]] = ...) -> None: ...
