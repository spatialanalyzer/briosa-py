# MP Argument Name Migration

The next server and client releases remove parenthetical MP-label qualifiers from public argument and result names. For example, `angle_tolerance_0_0_for_none` becomes `angle_tolerance` (`angleTolerance` in .NET and JavaScript). **0.0 still disables angle tolerance.** Units, defaults, presence, omission behavior, and SDK bindings do not change.

This is a source and JSON naming change. Update named arguments, result properties, object keys, keyword arguments, JSON/TextFormat payloads, and reflection-based lookups when adopting the new packages. Regenerate custom transport clients from the matching new protocol artifact. Binary protobuf field numbers, types, and presence remain unchanged. Runtime admission continues to use the existing exact-SA-target and behavioral compatibility rules independently of package versions.

Keep all existing names for **Evaluate Feature Check**, **Reset Cloud Bounding Box**, **Define point of view**, and **Get point of view parameters** because removing qualifiers causes collisions. Their entire signatures remain unchanged. The same method-level rule applies to future collisions.

Applications keep control of their package dependencies and server selection. Existing released packages and documentation snapshots retain their original names. Upgrade a consuming application by updating its client package for the same exact SA target, applying the table below, and running its tests. A new installer/server installation does not upgrade the application's client dependency. Previous immutable packages remain available for rollback.

The 2024 product has 168 renamed members in 83 commands. The 2026 product has 172 in 86 commands; its additions are Set Cone Properties, Set Line Properties, and Set Geom Relationship Auto Measure Nominal Feature. Shared result values follow their declaring type. The table lists every occurrence in the 2026 product; entries marked 2026 only are absent from 2024.

Names preserve established abbreviations and identifier conventions unrelated to parentheses. For example, `value_0_360` retains its necessary identifier prefix, and percent outside parentheses remains part of `per_unit_length_step_over_percent`.

## Rename Table

The authoritative naming rule and wire contracts belong to [Briosa](https://github.com/spatialanalyzer/briosa/blob/main/docs/development/mp-argument-name-migration.md).

| Command | Direction | Previous Member | New Member | Meaning |
| --- | --- | --- | --- | --- |
| Angle Between Line and Plane | input | `angle_tolerance_0_0_for_none` | `angle_tolerance` | 0.0 disables this tolerance. |
| Angle Between Two Lines | input | `angle_tolerance_0_0_for_none` | `angle_tolerance` | 0.0 disables this tolerance. |
| Angle Between Two Planes' normals | input | `angle_tolerance_0_0_for_none` | `angle_tolerance` | 0.0 disables this tolerance. |
| Best Fit Transformation - Group to Group | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Best Fit Transformation - Group to Group | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Best Fit Transformation - Group to Group | input | `file_path_for_csv_text_report_requires_show_interface_true` | `file_path_for_csv_text_report` | Requires Show Interface to be true. |
| Fit Geometry to Point Group | input | `fit_interface_tolerance_1_0_use_profile` | `fit_interface_tolerance` | -1.0 uses the profile tolerance. |
| Fit Geometry to Point Group | input | `starting_condition_geometry_optional` | `starting_condition_geometry` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Fit Geometry to Point Group Projected to Plane | input | `fit_interface_tolerance_1_0_use_profile` | `fit_interface_tolerance` | -1.0 uses the profile tolerance. |
| Fit Geometry to Point Group Projected to Plane | input | `starting_condition_geometry_optional` | `starting_condition_geometry` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Fit Geometry to Points | input | `fit_interface_tolerance_1_0_use_profile` | `fit_interface_tolerance` | -1.0 uses the profile tolerance. |
| Fit Geometry to Points | input | `starting_condition_geometry_optional` | `starting_condition_geometry` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Get Cone Properties | output | `cone_end_point_in_working_coordinates` | `cone_end_point` | Expressed in working coordinates. |
| Get Cone Properties | output | `cone_axis_in_working_coordinates` | `cone_axis` | Expressed in working coordinates. |
| Get Measurement Weather Data | output | `temperature_deg_f` | `temperature` | Temperature in degrees Fahrenheit. |
| Get Measurement Weather Data | output | `pressure_in_hg` | `pressure` | Pressure in inches of mercury. |
| Get Measurement Weather Data | output | `humidity_rh` | `humidity` | Relative humidity in percent. |
| Get Slot Properties | output | `slot_transform_in_working_coordinates` | `slot_transform` | Expressed in working coordinates. |
| Get Slot Properties | output | `center_in_working_coordinates` | `center` | Expressed in working coordinates. |
| Get Slot Properties | output | `normal_direction_in_working_coordinates` | `normal_direction` | Expressed in working coordinates. |
| Get Slot Properties | output | `centerline_pt_1_in_working_coordinates` | `centerline_pt_1` | Expressed in working coordinates. |
| Get Slot Properties | output | `centerline_pt_2_in_working_coordinates` | `centerline_pt_2` | Expressed in working coordinates. |
| Group To Surface Fit | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Group To Surface Fit | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Make Circle Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Circle Fit Profile | input | `override_planar_offset_1_0_use_current` | `override_planar_offset` | -1.0 uses the current offset. |
| Make Circle Fit Profile | input | `lock_radius_1_0_do_not_lock` | `lock_radius` | -1.0 leaves this dimension unlocked. |
| Make Cone Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Cone Fit Profile | input | `lock_angle_in_degrees_1_0_do_not_lock` | `lock_angle_in_degrees` | -1.0 leaves this dimension unlocked. |
| Make Cylinder Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Cylinder Fit Profile | input | `lock_radius_1_0_do_not_lock` | `lock_radius` | -1.0 leaves this dimension unlocked. |
| Make Ellipse Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Ellipse Fit Profile | input | `override_planar_offset_1_0_use_current` | `override_planar_offset` | -1.0 uses the current offset. |
| Make Paraboloid Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Paraboloid Fit Profile | input | `lock_focal_length_1_0_do_not_lock` | `lock_focal_length` | -1.0 leaves this dimension unlocked. |
| Make Plane Fit Profile | input | `override_planar_offset_1_0_use_current` | `override_planar_offset` | -1.0 uses the current offset. |
| Make Slot Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Slot Fit Profile | input | `override_planar_offset_1_0_use_current` | `override_planar_offset` | -1.0 uses the current offset. |
| Make Sphere Fit Profile | input | `override_radial_offset_1_0_use_current` | `override_radial_offset` | -1.0 uses the current offset. |
| Make Sphere Fit Profile | input | `lock_radius_1_0_do_not_lock` | `lock_radius` | -1.0 leaves this dimension unlocked. |
| Query Clouds to Objects | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Query Clouds to Objects | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Query Clouds to Surface | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Query Clouds to Surface | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Query Frame to Frame | output | `rx_roll` | `rx` | MP qualifier: Roll. |
| Query Frame to Frame | output | `ry_pitch` | `ry` | MP qualifier: Pitch. |
| Query Frame to Frame | output | `rz_yaw` | `rz` | MP qualifier: Yaw. |
| Query Groups to Objects | input | `group_name_list_groups_to_project` | `group_name_list` | MP qualifier: Groups to Project. |
| Query Groups to Objects | input | `object_name_list_objects_to_project_to` | `object_name_list` | MP qualifier: Objects to Project to. |
| Query Groups to Objects | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Query Groups to Objects | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Query Points to Objects | input | `object_name_list_objects_to_project_to` | `object_name_list` | MP qualifier: Objects to Project to. |
| Query Points to Objects | input | `rms_tolerance_0_0_for_none` | `rms_tolerance` | 0.0 disables this tolerance. |
| Query Points to Objects | input | `maximum_absolute_tolerance_0_0_for_none` | `maximum_absolute_tolerance` | 0.0 disables this tolerance. |
| Set Cone Properties | input | `cone_end_point_in_working_coordinates` | `cone_end_point` | Expressed in working coordinates. |
| Set Cone Properties | input | `cone_axis_in_working_coordinates` | `cone_axis` | Expressed in working coordinates. |
| Set Line Properties | input | `length_optional` | `length` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Temperature Compensate a group | input | `scaling_origin_coordinate_frame` | `scaling_origin` | MP qualifier: coordinate frame. |
| Temperature Compensate a group | input | `material_cte_1_deg_f` | `material_cte` | Coefficient per degree Fahrenheit. |
| Temperature Compensate a group | input | `initial_temperature_f` | `initial_temperature` | Temperature in degrees Fahrenheit. |
| Temperature Compensate a group | input | `final_temperature_f` | `final_temperature` | Temperature in degrees Fahrenheit. |
| Cloud Display Control | input | `thin_draw_increment` | `thin` | MP qualifier: Draw Increment. |
| Create Point Callout | input | `show_x_r` | `show_x` | MP qualifier: R. |
| Create Point Callout | input | `show_y_theta` | `show_y` | MP qualifier: Theta. |
| Create Point Callout | input | `show_z_phi` | `show_z` | MP qualifier: Phi. |
| Create Point Callout | input | `show_ux_ur` | `show_ux` | MP qualifier: Ur. |
| Create Point Callout | input | `show_uy_utheta` | `show_uy` | MP qualifier: Utheta. |
| Create Point Callout | input | `show_uz_uphi` | `show_uz` | MP qualifier: Uphi. |
| Get Gradient At Projected Point On Surface Edge | input | `surface_edge_b_spline` | `surface_edge` | MP qualifier: B-Spline. |
| Construct Points Cylindrically Shifted | input | `theta_shift_degrees` | `theta_shift` | Angle in degrees. |
| Create Hidden Point Rod | input | `target_to_target_distance` | `a_to_b_distance` | MP qualifier: Target to Target. |
| Create Hidden Point Rod | input | `target_to_tip_distance` | `a_to_c_distance` | MP qualifier: Target to Tip. |
| Construct Sphere | input | `sphere_center_in_working_coordinates` | `sphere_center` | Expressed in working coordinates. |
| Direct CAD Access | input | `surface_normals_mode_1_or_2` | `surface_normals_mode` | MP qualifier: 1 or 2. |
| Direct CAD Access | input | `cad_file_units_leave_blank_to_use_the_units_specified_in_the_file` | `cad_file_units` | An empty value uses the units specified in the file. |
| Export ASCII Point Set | input | `maximum_precision_scientific_notation` | `maximum_precision` | MP qualifier: Scientific Notation. |
| Export ASCII Points | input | `maximum_precision_scientific_notation` | `maximum_precision` | MP qualifier: Scientific Notation. |
| Export Vector Container to ASCII File | input | `overwrite_existing_file_false_append` | `overwrite_existing_file` | False appends to the existing file. |
| Export Vector Container to ASCII File | input | `use_full_precision_scientific_notation` | `use_full_precision` | MP qualifier: Scientific Notation. |
| Import SA File | input | `selected_collections_optional` | `selected_collections` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Make GD&T Feature Check Annotation | input | `per_unit_area_length_distance` | `per_unit_length_distance` | MP qualifier: area. |
| Make GD&T Feature Check Annotation | input | `per_unit_area_length_step_over_percent` | `per_unit_length_step_over_percent` | MP qualifier: area. |
| LR Self Test | output | `reference_arm_length_inches` | `reference_arm_length` | Length in inches. |
| LR Self Test | output | `mirror_measurement_range_mean_inches` | `mirror_measurement_range_mean` | Length in inches. |
| LR Self Test | output | `mirror_measurement_range_standard_deviation_inches` | `mirror_measurement_range_standard_deviation` | Length in inches. |
| Get Current Instrument Position Update | output | `y_or_theta_degrees` | `y_or_theta` | Angle in degrees. |
| Get Current Instrument Position Update | output | `z_or_phi_degrees` | `z_or_phi` | Angle in degrees. |
| Get Current Instrument Position Update | output | `time_since_update_seconds` | `time_since_update` | Time in seconds. |
| Get Current Instrument Position Update | output | `timestamp_approximate` | `timestamp` | MP qualifier: Approximate. |
| Locate Instruments (USMN) | input | `analysis_time_limit_minutes` | `analysis_time_limit` | Time in minutes; 0 disables the time limit. |
| Create Templated Instrument (USMN) | input | `azimuth_weight` | `component_1_weight` | MP qualifier: Azimuth. |
| Create Templated Instrument (USMN) | input | `elevation_weight` | `component_2_weight` | MP qualifier: Elevation. |
| Create Templated Instrument (USMN) | input | `distance_weight` | `component_3_weight` | MP qualifier: Distance. |
| Get Tracker/EDM Theodolite Uncertainties | output | `theta_dispersion_arcseconds` | `theta_dispersion` | Angle in arcseconds. |
| Get Tracker/EDM Theodolite Uncertainties | output | `phi_dispersion_arcseconds` | `phi_dispersion` | Angle in arcseconds. |
| Get Tracker/EDM Theodolite Uncertainties | output | `distance_ppm` | `distance` | Value in parts per million. |
| Set Tracker/EDM Theodolite Uncertainties | input | `theta_dispersion_arcseconds` | `theta_dispersion` | Angle in arcseconds. |
| Set Tracker/EDM Theodolite Uncertainties | input | `phi_dispersion_arcseconds` | `phi_dispersion` | Angle in arcseconds. |
| Set Tracker/EDM Theodolite Uncertainties | input | `distance_ppm` | `distance` | Value in parts per million. |
| Get Instrument Weather Setting | output | `temperature_fahrenheit` | `temperature` | Temperature in degrees Fahrenheit. |
| Get Instrument Weather Setting | output | `pressure_mmhg` | `pressure` | Pressure in millimeters of mercury. |
| Get Instrument Weather Setting | output | `relative_humidity_percent` | `relative_humidity` | Relative humidity in percent. |
| Set Instrument Weather Setting | input | `temperature_fahrenheit` | `temperature` | Temperature in degrees Fahrenheit. |
| Set Instrument Weather Setting | input | `pressure_mmhg` | `pressure` | Pressure in millimeters of mercury. |
| Set Instrument Weather Setting | input | `relative_humidity_percent` | `relative_humidity` | Relative humidity in percent. |
| Compute CTE Scale Factor | input | `material_cte_per_degree_fahrenheit` | `material_cte` | Coefficient per degree Fahrenheit. |
| Compute CTE Scale Factor | input | `initial_temperature_fahrenheit` | `initial_temperature` | Temperature in degrees Fahrenheit. |
| Compute CTE Scale Factor | input | `final_temperature_fahrenheit` | `final_temperature` | Temperature in degrees Fahrenheit. |
| Get Instrument Interface Response Timeout | output | `timeout_seconds` | `timeout` | Time in seconds. |
| Set Instrument Interface Response Timeout | input | `timeout_seconds` | `timeout` | Time in seconds. |
| Ask for User Decision from Image | input | `window_width_0_default` | `window_width` | 0 uses the default window dimension. |
| Ask for User Decision from Image | input | `window_height_0_default` | `window_height` | 0 uses the default window dimension. |
| Ask for User Decision from Strings | input | `button1_text_empty_to_hide_button` | `button1_text` | An empty string hides the button. |
| Ask for User Decision from Strings | input | `button2_text_empty_to_hide_button` | `button2_text` | An empty string hides the button. |
| Ask for User Decision from Strings | input | `button3_text_empty_to_hide_button` | `button3_text` | An empty string hides the button. |
| Get Geom Relationship Auto Vectors | output | `auto_vectors_nominal_avn_enabled` | `auto_vectors_nominal_enabled` | MP qualifier: AVN. |
| Get Geom Relationship Auto Vectors | output | `auto_vectors_nominal_avn_name` | `auto_vectors_nominal_name` | MP qualifier: AVN. |
| Get Geom Relationship Auto Vectors | output | `auto_vectors_fit_avf_enabled` | `auto_vectors_fit_enabled` | MP qualifier: AVF. |
| Get Geom Relationship Auto Vectors | output | `auto_vectors_fit_avf_name` | `auto_vectors_fit_name` | MP qualifier: AVF. |
| Set Geom Relationship Auto Measure Nominal Feature | input | `trap_clouds_false_geometry` | `trap_clouds` | False selects geometry. |
| Set Relationship Voxel Cloud Display | input | `voxel_size_1_0_autodetect` | `voxel_size` | -1.0 selects automatic detection. |
| Set Relationship Voxel Cloud Display | input | `voxel_rendering_diameter_1_0_fast` | `voxel_rendering_diameter` | -1.0 selects fast rendering. |
| Relationship Watch Window Template | input | `show_deviation_x_rx` | `show_deviation_x` | MP qualifier: Rx. |
| Relationship Watch Window Template | input | `show_deviation_y_ry` | `show_deviation_y` | MP qualifier: Ry. |
| Relationship Watch Window Template | input | `show_deviation_z_rz` | `show_deviation_z` | MP qualifier: Rz. |
| Create Chart from Vector Group | input | `template_chart_name_optional` | `template_chart_name` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Define Report Template | input | `report_page_settings_sa_report_only` | `report_page_settings` | MP qualifier: SA Report only. |
| Make New SA Report | input | `sa_report_template_optional` | `sa_report_template` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Quick Report | input | `report_name_optional` | `report_name` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Save Current View (BMP/JPG/PNG/GIF/TIFF) | input | `render_scale_factor_1_0_uses_window_size` | `render_scale_factor` | 1.0 uses the window size. |
| Set Calibration Appliance Node Instrument Dwell Time | input | `measurement_dwell_time_seconds` | `measurement_dwell_time` | Time in seconds. |
| Set Robot Calibration Tool Frame | input | `tool_frame_relative_to_flange` | `tool_frame` | MP qualifier: relative to flange. |
| Set Robot Calibration Measurement Offset In Tool Frame | input | `measurement_frame_relative_to_tool` | `measurement_frame` | MP qualifier: relative to tool. |
| Scale Bar Check | input | `current_temperature_f` | `current_temperature` | Temperature in degrees Fahrenheit. |
| Scale Bar Check | input | `material_cte_ppm_f` | `material_cte` | Coefficient in parts per million per degree Fahrenheit. |
| Get Angular Representation | output | `value_0_360_false_180` | `value_0_360` | False selects the +/-180 angular representation. |
| Get Screen Resolution | input | `display_1_primary` | `display` | -1 selects the primary display. |
| Set Angular Representation | input | `value_0_360_false_180` | `value_0_360` | False selects the +/-180 angular representation. |
| Set Collection Notes | input | `append_false_overwrite` | `append` | False overwrites existing notes. |
| Set Folder Notes | input | `append_false_overwrite` | `append` | False overwrites existing notes. |
| Set Object Notes | input | `append_false_overwrite` | `append` | False overwrites existing notes. |
| Set Point Notes | input | `append_false_overwrite` | `append` | False overwrites existing notes. |
| Set User Interface Profile | input | `profile_file_name_optional` | `profile_file_name` | Optional in the MP editor; the existing API presence and omission behavior is unchanged. |
| Auto-Range and Set Vector Group Colorization (All) | input | `colorization_options_uses_mode_only` | `colorization_options` | MP qualifier: Uses Mode Only. |
| Auto-Range and Set Vector Group Colorization (Selected) | input | `colorization_options_uses_mode_only` | `colorization_options` | MP qualifier: Uses Mode Only. |
| Highlight Objects | input | `object_names_empty_to_clear_all` | `object_names` | An empty selection clears all highlights. |
| Highlight Point | input | `point_name_empty_to_clear_all` | `point_name` | An empty selection clears all highlights. |
| Highlight Relationships | input | `relationships_empty_to_clear_all` | `relationships` | An empty selection clears all highlights. |
| Show / Hide by Object Type | input | `hide_show_false` | `hide` | False shows the objects. |
| Show / Hide Points | input | `show_hide_false` | `show` | False hides the points. |
| Get Observation Info | output | `temperature_fahrenheit` | `temperature` | Temperature in degrees Fahrenheit. |
| Get Observation Info | output | `pressure_in_hg` | `pressure` | Pressure in inches of mercury. |
| Get Observation Info | output | `relative_humidity_percent` | `relative_humidity` | Relative humidity in percent. |
| LR Get Most Recent SNR Info | output | `peak_value_db` | `peak_value` | Value in decibels. |
| LR Get Most Recent SNR Info | output | `measured_range_meters` | `measured_range` | Range in meters. |
| LR Self Test - Flip Test | output | `front_range_inches` | `front_range` | Length in inches. |
| LR Self Test - Flip Test | output | `front_azimuth_degrees` | `front_azimuth` | Angle in degrees. |
| LR Self Test - Flip Test | output | `front_elevation_degrees` | `front_elevation` | Angle in degrees. |
| LR Self Test - Flip Test | output | `back_range_inches` | `back_range` | Length in inches. |
| LR Self Test - Flip Test | output | `back_azimuth_degrees` | `back_azimuth` | Angle in degrees. |
| LR Self Test - Flip Test | output | `back_elevation_degrees` | `back_elevation` | Angle in degrees. |
| LR Self Test - Flip Test | output | `front_back_difference_range_inches` | `front_back_difference_range` | Length in inches. |
| LR Self Test - Flip Test | output | `front_back_difference_azimuth_degrees` | `front_back_difference_azimuth` | Angle in degrees. |
| LR Self Test - Flip Test | output | `front_back_difference_elevation_degrees` | `front_back_difference_elevation` | Angle in degrees. |
| LR Self Test - LO Sep | output | `primary_lo_index` | `primary_lo` | Indexing starts at 1. |
| LR Self Test - LO Sep | output | `secondary_lo_index` | `secondary_lo` | Indexing starts at 1. |
| LR Self Test - LO Sep | output | `primary_lo_range_mean_inches` | `primary_lo_range_mean` | Length in inches. |
| LR Self Test - LO Sep | output | `primary_lo_range_standard_deviation_inches` | `primary_lo_range_standard_deviation` | Length in inches. |
| LR Self Test - LO Sep | output | `secondary_lo_range_mean_inches` | `secondary_lo_range_mean` | Length in inches. |
| LR Self Test - LO Sep | output | `secondary_lo_range_standard_deviation_inches` | `secondary_lo_range_standard_deviation` | Length in inches. |
