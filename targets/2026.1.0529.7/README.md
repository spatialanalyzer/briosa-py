# Briosa Python client

`briosa-2026-1-0529-7` is the asynchronous Python client for the open-source
[Briosa](https://github.com/spatialanalyzer/briosa) SpatialAnalyzer bridge. It
provides idiomatic lifecycle and MP APIs while keeping generated protobuf and
gRPC types private.

The package does not include SpatialAnalyzer, the SA SDK, or a license. It
targets SpatialAnalyzer `2026.1.0529.7` exactly and Python 3.10 or later. The
complete protocol identity is pinned in [`protocol.lock.json`](protocol.lock.json).

## Package Identity

The next version is not published yet. Build the candidate locally and use its
package path or feed in the installation command below.

The distribution is named `briosa-2026-1-0529-7`, while application code keeps
the stable `briosa` import package. Install the distribution with:

```powershell
python -m pip install C:\path\to\dist\briosa_2026_1_0529_7-0.5.0-py3-none-any.whl
```

Each exact SpatialAnalyzer target will have a separate distribution name. Two
target distributions intentionally provide the same `briosa` import package,
so applications targeting different SA releases should use separate virtual
environments or processes. There is no universal runtime target selector. Both
reviewed SA targets are maintained independently in this repository.

## Usage

```python
from briosa import BriosaClient


async with BriosaClient() as briosa:
    working_directory = await briosa.get_working_directory()
```

Construction is dormant. Entering the async context, or calling `start()`,
locates and launches the matching local Briosa server, starts a disconnected SA
SDK generation, launches SpatialAnalyzer, connects the SDK, and verifies MP
readiness. `BriosaStartOptions` can select a control-plane-only startup or
connect to an eligible application that is already running.

Application and SDK state, launch, connect, stop, and recovery methods remain
available for diagnosis and explicit control. `stop()`, `aclose()`, and async
context exit stop the owned server and SDK but never close SpatialAnalyzer.

`BriosaStartOptions.startup_timeout` bounds the whole `start()` and defaults to
`120.0` seconds. That covers the server's default worst case of about 100 seconds
for a start that launches SpatialAnalyzer, with a 20-second margin. If you raise
the server's `Briosa:Worker:StartupTimeout`, `Briosa:Worker:ReadinessProbeTimeout`,
or `Briosa:SpatialAnalyzer:ApplicationStartupTimeout`, raise the client budget
too; the [public API contract](docs/public-api-contract.md#startup-and-lifecycle-time-budgets)
shows how to size it. Lifecycle methods send no deadline unless you pass
`timeout`. If the budget expires while the server is starting or connecting the
SDK, read the SDK state before retrying: the server finishes a step it has
accepted, so the abandoned start may still produce a ready generation.

The client retains lifecycle generations and supplies guards automatically.
Typed lifecycle failures, compatibility failures, task cancellation, ambiguous
MP completion, and replay guidance remain distinct. MP operations are never
automatically replayed.

See the [Briosa documentation](https://spatialanalyzer.github.io/briosa-docs/api/python/)
for the client API overview. The target-specific source and locked protocol define
this package's exact API.

## Contract major 3 (0.5.0)

0.5.0 is a breaking release. It selects only servers that declare behavioral
contract major 3 (Server 0.10.0, built here against the frozen checkpoint
`0.10.0-dev.1`). The
[contract major 3 record](https://github.com/spatialanalyzer/briosa/blob/main/docs/development/contract-major-3.md)
and the
[client behavioral contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/client-library-behavioral-contract.md)
are authoritative; this section lists what changes for Python callers.

### Results and typed failures

- **Partial success.** An MP that returns code 4 (PARTIAL SUCCESS) did its
  work, but not all of its intended effect. The method returns its outputs as
  usual and never raises or retries. To see how a call completed, pass the
  keyword-only `on_mp_completion` that every MP method takes. It receives one
  `MpCompletion` with `state` (`MpExecutionState.SUCCEEDED` or
  `PARTIAL_SUCCESS`) and its `mp_result_code` (2 or 4), before the method
  returns:

  ```python
  completions: list[MpCompletion] = []
  directory = await briosa.get_working_directory(on_mp_completion=completions.append)
  if completions[0].state is MpExecutionState.PARTIAL_SUCCESS:
      ...
  ```

  The client checks every MP success, whether or not you pass an observer:
  the execution details must pair `SUCCEEDED` with MP code 2 or
  `PARTIAL_SUCCESS` with code 4. Anything else, including a missing code, is
  `BriosaProtocolError` (`mp-completion-invalid`). The observer runs before the
  outputs are mapped, so it hears of a success even when the outputs then fail
  to map.

  A failed call reports no completion. Its `BriosaOperationError.failure`
  carries `mp_execution` (an `MpExecutionDetails`), which keeps
  `PARTIAL_SUCCESS` distinct, for example when code 4 came without an output.
  Four operations document code 4 as leaving the work undone, and report it as
  an ordinary `MP_FAILURE` with code 4: `construct_point_from_survey_target_center`,
  `open_sa_file`, `open_template_file` and `set_report_options_for_object`.
- **SDK call faults.** `OperationFailureKind.SDK_CALL_FAULTED` reports that an
  SDK call threw during the MP sequence. The execution disposition gives the
  phase: `NOT_STARTED` (nothing ran), `STARTED_OUTCOME_UNKNOWN` (reconcile
  before any replay) or `COMPLETED` (an output getter failed after MP success).
  It is never folded into `INTERNAL` or a retrieval failure.
- **Modal dialogs.** A watchdog timeout or readiness failure caused by an open
  SpatialAnalyzer dialog reports diagnostic `sa-modal-dialog-open`, with
  recovery guidance `OPERATOR_INTERVENTION_REQUIRED` for operations. Replacing
  the worker doesn't clear the dialog: an operator must close it. The client
  never retries. Unattended stations can set the server option
  `Briosa:SpatialAnalyzer:InteractionMode` to `Silent` (the default is
  `Unchanged`). SpatialAnalyzer keeps the mode across restarts and has no getter
  for it, and the client never sets it.
- **Lifecycle caller kinds.** `SpatialAnalyzerSdkLifecycleFailureKind` and
  `SpatialAnalyzerLifecycleFailureKind` gain `CALLER_CANCELLED` and
  `CALLER_DEADLINE_EXCEEDED`. They describe the caller's own interruption,
  never a state conflict. gRPC rarely delivers them: cancelling a call raises
  `asyncio.CancelledError`, and a `timeout` raises `BriosaTransportError` with
  `transport-deadline-exceeded`.
- **Wire-order enums.** Every enum value is appended in wire order. An unknown
  value is still a protocol error, except in discovery (below).

### Discovery and admission

- `BriosaServerSnapshot` reports the server's `admission_profile` and an opaque
  `policy_fingerprint`; compare the fingerprint only for equality.
- Each `BriosaOperationCapability` carries `risk_flags` (an ordered set; empty
  means no reviewed risk), `duration_class`, `validation_status` and
  `admission`. A value that a later 3.x revision adds maps to `UNKNOWN`.
- The snapshot's operations are the admitted ones only. The client takes
  admission from the server and never pre-validates a call or its options; the
  server decides. Validation status is informational.
- `await briosa.list_capabilities(include_denied=True)` is a diagnostic listing
  that also returns each denied operation with its denial reason in
  `admission`. It never makes an operation callable.
- The packaged `standard` profile no longer admits device sessions, device
  configuration, motion, code execution, external IO, file deletion or
  operator UI. The seven `device_config` operations need `Profile=device`,
  `full`, or an override; interactive operations need the explicit opt-in
  `Flags:interactive_ui=allow`. Facades for denied and exclusive operations
  remain, and a denied call fails with `POLICY_DENIED` and `NOT_STARTED`. See the
  [admission profile migration](https://github.com/spatialanalyzer/briosa/blob/main/docs/development/admission-profile-migration.md).

### Request defaults and arguments

- **Ten defaults flip**, because the server now denies the old values:
  `measure_immediately=True` on `measure_single_point_here`,
  `configure_and_measure`, `measure_existing_single_point`,
  `measure_existing_single_point_and_compare` and
  `measure_existing_single_point_manual_guide`; `auto_start=True` on
  `auto_measure_points`; `wait_for_complete=True` on
  `auto_measure_specified_geometry`; `acknowledge_arrival=True` on both robot
  moves; and `prompt_on_missing_components=False` on `direct_cad_access`.
- **Now optional, left unset when omitted:** the `template_chart_name` of
  `create_chart_from_vector_group` (now keyword-only), the `profile_file_name`
  of `set_user_interface_profile`, and the `starting_condition_geometry` of the
  three fit operations.
- **Now required, with no default:** the relationship `tolerance` and
  `constraint` of the four `make_*_relationship` operations (pass
  `ToleranceVectorOptions.NO_LIMITS` for none); the six joints of
  `move_robot_machine_to_joint_pose_six_dof`; `set_automatically` of
  `set_instrument_weather_setting`; the `scale_factor` of `scale_objects` and of
  both instrument scale-factor setters; the model-link `configuration` (whose
  members lose their defaults); the robot `parameter_name` and
  `parameter_value` of `set_robot_machine_parameter`; the
  `observation_index` and `vector_index` of the three destructive index
  operations; and the names and patterns of `delete_folder`, `delete_variable`,
  `delete_variables_wildcard_match`, `delete_vector_by_name` and
  `delete_robot_calibration`, and the `tag_name` of `remove_report_tag`.
- **Weather values:** `temperature`, `pressure` and `relative_humidity` lose
  their 0 default. Omitted, they stay unset; the server rejects that when
  `set_automatically` is false.
- **Lists:** the callout notes and both `quick_align` lists stay optional and
  are sent empty when omitted or `None` (briosa-py#44). The four
  `feature_inspection_auto_filter` lists and the quick fit's
  `other_objects_to_transform` are required, because the server rejects them
  empty. USMN `excluded_groups` stays optional; the server skips its setter for
  an empty list.
- **Inputs the server requires are required**, with no fill-in: no identity
  transform, default settings value, empty list or default choice. Omitting one
  fails with `TypeError` before any call. These lose their default or `None`:
  - **Transforms:** `calculate_tcp_fixture_uncertainties` (`tcp_in_working`);
    `construct_ellipsoid` (`transform_in_working_coordinates`);
    `construct_frame` (`transform_in_working_coordinates`);
    `construct_frame_from_transform_in_world`
    (`transform_in_world_coordinates`);
    `set_calibration_appliance_node_measurement_offset_transform`
    (`measurement_offset_transform`);
    `set_robot_calibration_measurement_offset_in_tool_frame`
    (`measurement_frame`); `set_robot_calibration_tool_frame` (`tool_frame`);
    `set_robot_machine_base_transform` (`destination_transform`).
  - **Settings:** `auto_filter_clouds_to_nominal_geometry_2d`
    (`filter_proximity_settings_2d`);
    `auto_filter_clouds_to_nominal_geometry_3d`
    (`filter_proximity_settings_3d`);
    `auto_filter_points_to_nominal_geometry_3d`
    (`filter_proximity_settings_3d`); `do_relationship_fit` (`motion_to_allow`);
    `make_groups_to_objects_relationship` (`projection_options`);
    `make_point_clouds_to_objects_relationship` (`projection_options`);
    `make_points_to_objects_relationship` (`projection_options`);
    `move_collections_by_minimizing_relationships` (`motion_to_allow`);
    `relationship_watch_window_template` (`options`).
  - **Tolerances:** `build_target` (`tolerance`);
    `make_frame_to_frame_relationship` (`orientation_tolerance`,
    `position_tolerance`);
    `set_object_to_object_direction_relationship_tolerances`
    (`angle_between_vectors_tolerances`,
    `mutual_perpendicular_length_tolerances`).
  - **Lists:** `auto_filter_points_groups_clouds_to_surface_faces` (`points`,
    `groups`, `clouds`); `create_points_to_objects_map` (`points`, `groups`);
    `extract_geometry_from_point_clouds` (`bounding_points`);
    `set_points_to_points_relationship_associated_data` (`nominal_points`,
    `actual_points`); `set_relationship_associated_data` (`individual_points`,
    `point_groups`, `point_clouds`, `objects`).
  - **Choices:** `auto_filter_points_groups_clouds_to_surface_faces`
    (`offset_direction`); `collimation` (`tilt_mode`, `baseline_method`);
    `construct_points_from_surfaces_on_uv_grid` (`edge_point_mode`);
    `create_point_callout` (`desired_coordinate_system`);
    `extract_geometry_from_point_clouds` (`geometry_type`);
    `feature_inspection_auto_filter` (`offset_direction`);
    `locate_instruments_usmn` (`show_usmn_dialog`);
    `make_collection_item_name_ref_list_wildcard_selection` (`item_type`);
    `make_collection_object_name_ref_list_by_type` (`object_type`);
    `make_collection_object_name_ref_list_by_type_and_color` (`object_type`);
    `make_collection_object_name_ref_list_runtime_select` (`object_type`);
    `make_collection_object_name_ref_list_wildcard_selection` (`object_type`);
    `make_collection_object_name_runtime_select` (`object_type`);
    `make_dynamic_circle_relationship` (`construction_mode`);
    `make_dynamic_ellipse_relationship` (`construction_mode`);
    `make_dynamic_line_relationship` (`construction_mode`);
    `make_dynamic_plane_relationship` (`construction_mode`);
    `make_dynamic_point_relationship` (`construction_mode`); `set_gdt_options`
    (`distance_between_mode`, `evaluation_method`);
    `set_target_computation_options` (`computation_method`).
  - **Names, points and vectors:** `auto_correspond_with_proximity_trigger`
    (`deviation_vector_group_name`); `collimation` (`scale_point_1`,
    `scale_point_2`, `not_measured_by_moving_instrument`,
    `as_measured_by_moving_instrument`); `construct_cross_section_cloud`
    (`reference_object`); `construct_point_from_cloud_point_runtime_select`
    (`constructed_point_name`); `construct_points_shifted_in_working_frame`
    (`shift_vector`); `construct_points_subset_with_greatest_spacing`
    (`group_for_subset`); `enable_disable_datum_alignment_for_feature_check`
    (`alignment`); `get_gradient_at_projected_point_on_surface_edge`
    (`edge_offset_direction`); `make_dynamic_point_relationship`
    (`third_reference_geometry`); `relationship_watch_window_template`
    (`watch_window_template_name`); `set_observation_collimation_shot_options`
    (`targeted_instrument`).
  - **Q-DAS:** `export_qdas_characteristics` and `prepare_qdas_data_list`
    (`k0004_date_time_stamp`), which defaulted to a captured timestamp. The SA
    2024 package already required it.
  - **Option members:** every member of `FilterProximitySettings` (below);
    the `udp_network_transmit_settings` of
    `RelationshipWatchWindowTemplateOptions` (pass
    `RelationshipWatchWindowUdpSettings()` to leave UDP off); and the `objects`,
    `geometry_relationships`, `auxiliary_object` and
    `auxiliary_geometry_relationship` of both GD&T annotation options, which are
    now keyword-only. `ReportOutputOptions` needs exactly one destination.
  Pass `ProjectionOptions.DEFAULT` to keep the reviewed projection defaults. A
  newly required input that follows every positional parameter and precedes
  every optional input in MP order is positional; the others are required
  keywords, so no existing positional parameter moves.
- **Proximity settings.** All eleven `FilterProximitySettings` members are
  required, with no default: the six distances (`surface_inclusion_proximity`,
  `edge_exclusion_proximity`, `planar_inclusion_proximity`,
  `planar_exclusion_proximity`, `radial_inclusion_proximity`,
  `geometry_extraction_tolerance`), the two Booleans (`project_to_plane`,
  `assert_plane_boundaries`) and the three proximity modes. The server reads the
  distances and Booleans without checking presence, so an absent one would
  reach SA as 0 or false, and a distance is a length in the SA job's units.
  Client 0.4 filled in 0.1, 0.1, 0.5, 0.1, 0.1 and 0.01, `True` and `False`, and
  `BOTH` for each mode. Pass the values your job needs instead.
- An argument you leave unset is never sent as an empty value, 0 or false, and
  the client doesn't pre-validate empty values. The server rejects them before
  dispatch with `VALIDATION` and `NOT_STARTED`. See the
  [argument defaults migration](https://github.com/spatialanalyzer/briosa/blob/main/docs/development/argument-defaults-migration.md).

### Removed operations

SpatialAnalyzer rejects the first eight on both exact targets, so they are gone
with their value types:

- `mirror_objects` (with `MirrorFramePlane`) and
  `delete_cloud_points_by_x_y_z_range`. There is no X Y Z box delete; the radial
  delete has different semantics and isn't licensed-validated yet.
- `construct_circles_lines_from_surfaces` (with `CircleLineMode`),
  `add_collection_instruments_to_ref_list_wildcard_selection`,
  `make_callout_view_ref_list_wildcard_selection` and
  `set_callout_view_properties`. Callout-view selection moves to the
  collection-item wildcard selection.
- `construct_polygonized_surface_from_point_clouds` (with
  `MeshOrientationType`) and
  `make_collection_vector_group_name_ref_list_runtime_select`. Nothing replaces
  them.
- `make_vector_name_ref_list_runtime_select` is the exception: SA never
  rejected it, but no operator could complete the selection on either target in
  licensed probe session 3. It can return in a 3.x revision once a licensed
  session verifies it.

### Lifecycle

- A server accepts a Start, Connect, Reconnect or Recover and then finishes it
  under its own bounds, even after the caller stops waiting. After a cancelled
  or timed-out lifecycle call, refresh state with
  `get_spatial_analyzer_sdk_state()` before deciding what to do: the startup you
  abandoned may still produce a ready generation. Call `get_server_snapshot()`
  to reopen MP calls on it.
- Treat `sdk-lifecycle-transition-in-progress` (`STATE_CONFLICT`,
  `REFRESH_STATE`) as "refresh and retry later". Stop a generation you own
  only after the accepted transition has ended.
- After a launch timeout, the server may still bring SpatialAnalyzer to
  `RUNNING`. Refresh application state before launching again, and treat
  `application-lifecycle-transition-in-progress` the same way.

### Fixed

- `locate_instrument_group_to_surface_quick_fit` returned a bare `TypeError`
  after every successful fit. It now maps `maximum_absolute_error` to
  `FitErrorResult.maximum_error` (briosa-py#45).
- `get_robot_machine_model_link_parameters` raised `TypeError` after every
  successful call; it now returns its nested result.
- Eight facades sent one argument twice and never sent another.
  `set_vector_group_to_vector_group_fit_weights` sent each gap as its fit
  weight, and `construct_point_group_from_point_cloud` sent the `sub_sampling`
  flag as `sub_sampling_distance`. The other six failed every call before
  dispatch: `construct_frame_known_origin_object_direction_object_direction`,
  the three `construct_points_at_projection_on_surfaces_*` operations, and
  `get_ith_callout_position_in_callout_view` and
  `set_ith_callout_position_in_callout_view`.
- A result that doesn't match its result type now fails as
  `BriosaProtocolError` (`operation-result-field-drift` or
  `operation-result-invalid`), never as a bare `TypeError`.
- `get_working_directory` is an ordinary MP operation now. A missing directory
  is `required-output-missing:directory`, like any other missing output.
- `get_relationship_ref_list_variable` and
  `get_report_items_reference_list_variable` are annotated
  `list[CollectionItemName]`, the type they return; they said
  `list[CollectionObjectName]`.
- A negative enum number now fails like any other unknown value. Client 0.4
  counted it from the end of the member list, so a lifecycle state or typed
  failure could report a member the server never sent. An operation error
  that carries one, including in its MP execution details, fails as
  `typed-error-malformed`; a lifecycle state or lifecycle error raises
  `BriosaProtocolError` (`unknown-enum-value`).

## Server selection

Applications select a server independently of their protocol generation pin.
On Windows x64, discovery reads Registry64 installation hints, committed
canonical stores, explicit search roots, and supported local layouts. It validates
receipts and manifests, filters the exact SA target and compatibility contract,
and selects the highest compatible stable release. No internet access is needed.

This development checkout prepares client 0.5.0 for behavioral contract **3.0**
(major 3, revision at least 0), built against the frozen protocol checkpoint
`0.10.0-dev.1` (spatialanalyzer/briosa `2960705e`). It is not a published
compatibility claim. The planned server release is 0.10.0. Major-2 servers,
including every released 0.9 server, major-1 servers, and servers without
contract metadata, including Server 0.6.1, are rejected before launch. Protocol
and source pins remain exact build inputs; startup verifies the running server
against its selected installation.

The three robot methods Get Robot Machine Parameter, Start Robot Machine
Interface, and Stop Robot Machine Interface now take a collection/instrument
identity for the MP argument named Machine ID. Supply an instrument ID rather
than a machine ID; other robot methods retain their existing types.

A full server queue returns an overload error with NotStarted, no recovery
action, and MayReplay guidance. The client preserves these separate facts and
never retries automatically. The 64 KiB inbound limit may also produce a
transport size error without typed detail. See the
[authoritative migration guide](https://github.com/spatialanalyzer/briosa/blob/main/docs/development/runtime-redesign-migration.md).

A missing or incompatible explicit choice fails without selecting another
installation. The choice is fixed for the session, including worker recovery.
Prereleases require explicit opt-in. Conflicting manifests for the same release
precedence produce an ambiguity error; identical copies prefer machine, user,
then portable scope and a stable path order. Elevated automatic discovery admits
only protected machine installations.

The optional selection settings include an executable path or installation ID,
an exact version, minimum version (inclusive), maximum version (exclusive),
excluded versions, search roots, allowed scopes, and an SA executable path.
Search roots name package stores with a committed `products` directory.
Read-only discovery returns candidates, the selected identity, and rejection codes
without starting Briosa, the SDK, or SA. Detailed paths belong to explicitly
requested diagnostics; installer **Verify/Repair** provides full payload checks.

`BRIOSA_SERVER_PATH` is ignored by default in client 0.2. Use a direct selection
option in new applications. Existing scripts can opt in to the legacy environment
override; an invalid override fails without fallback. Direct selectors take
precedence. Published 0.1.0/0.1.1 packages retain their original behavior.

Custom stores can be registered through the Installer's **Register existing
installations** action or `packages register` command. Alternatively provide a
search root or executable path per application. No machine-wide active server is
selected. Installing several SA releases does not establish concurrent execution:
the server still verifies the activated SDK and connected SA independently.

The [shared selection contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/installation-selection-and-compatibility.md)
owns these rules and the [compatibility matrix](https://github.com/spatialanalyzer/briosa/blob/main/compatibility/matrix.json)
distinguishes tested pairs from declared forward compatibility.

```python
from briosa import BriosaServerSelection, BriosaStartOptions, discover_installations

selection = BriosaServerSelection(version="0.10.0")
report = discover_installations(selection)  # no process launch
await briosa.start(BriosaStartOptions(server_selection=selection))

```

Use `executable_path`, `installation_id`, `minimum_version`, `maximum_version_exclusive`,
`excluded_versions`, `search_roots`, `allowed_scopes`, `allow_prerelease`,
`spatial_analyzer_executable_path`, and `use_legacy_environment_override` as needed.
Pass paths as `pathlib.Path` values. Use a separate environment for each exact-target package.

## Development

Run these commands from `targets/2026.1.0529.7/`. Each target builds and
packages independently. Use a separate Python environment for each target.

```powershell
python -m venv .venv
./.venv/Scripts/python -m pip install -e ".[dev]"
./.venv/Scripts/python -m ruff format --check .
./.venv/Scripts/python -m ruff check .
./.venv/Scripts/python -m mypy
./.venv/Scripts/python -m pytest
./eng/Test-Conformance.ps1 `
  -ArtifactPath C:\path\to\briosa-client-conformance-0.9.2-sa-2026.1.0529.7-win-x64.zip `
  -ExpectIncompatible `
  -PythonExecutable ./.venv/Scripts/python.exe
./.venv/Scripts/python -m build
./.venv/Scripts/python eng/test_package_identity.py
./.venv/Scripts/python eng/test_package_consumer.py
```

Unit tests use fake server/transport boundaries. The shared conformance suite
runs the real client and server against a portable fake SDK/application host.
Neither path requires SpatialAnalyzer nor a license.

## Protocol regeneration

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.10.0-dev.1-sa-2026.1.0529.7.zip `
  --update --source-channel source_commit_bootstrap

./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.10.0-dev.1-sa-2026.1.0529.7.zip
```

Never edit generated `*_pb2.py`, `*_pb2.pyi`, `*_pb2_grpc.py`,
`protocol_identity.py`, or `protocol.lock.json` files by hand.
## Server Logging

Pass optional typed `logging` settings through `BriosaStartOptions`:

```python
from briosa import BriosaLoggingOptions, BriosaLogLevel, BriosaStartOptions

await briosa.start(BriosaStartOptions(
    logging=BriosaLoggingOptions(
        minimum_level=BriosaLogLevel.DEBUG,
        console_enabled=False,
        max_file_size_mib=20,
        retained_file_count=10,
    ),
))
```

The remaining controls are `category_levels`, `file_enabled`, `file_directory`,
`max_age_days`, and `max_total_size_mib`. Omitted settings preserve server
configuration. Options validate at construction; custom directories must be
absolute Windows paths. See the [shared startup contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/client-library-behavioral-contract.md#server-logging-startup-controls)
and [server observability guide](https://github.com/spatialanalyzer/briosa/blob/main/targets/2026.1.0529.7/docs/operations/server-observability.md).

## Compatibility and validation

This package pins its generation artifact and tests the declared compatibility
contract against packaged servers. The retained Server 0.9.2 baseline, the
newest major-2 server, must be rejected. Exact SA target, runtime identity,
capabilities, and readiness still gate MP calls.

Portable conformance covers lifecycle, identity mismatch, denied capabilities
with the admission profile and denial reasons, typed MP and output failure, SDK
call faults, partial success, deadlines, cancellation, an abandoned lifecycle
Connect, watchdog recovery, SDK loss, and owned-process cleanup. Unit tests also
check every changed default, omission and requiredness rule on the built
request, and map a fully populated response for every operation. Its harness disables Control Center auto-launch and
restores the prior setting afterward. These checks use a fake SDK, without a
SpatialAnalyzer installation or license.

The public relationship-reference inputs use `CollectionItemName`, including
the item name and optional item type; they are not geometric object references.
This corrects earlier pre-publication facade annotations that disagreed with the
protocol. Existing callers of those methods must pass the item-name value.

Broader licensed runtime coverage and protected runtime CI remain outstanding.
Enterprise Artifactory integration is also unverified. This package remains v0.x;
portable results do not imply v1.0 readiness or validation on physical instruments.
