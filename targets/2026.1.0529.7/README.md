# Briosa Python client

`briosa-2026-1-0529-7` is the asynchronous Python client for the open-source
[Briosa](https://github.com/spatialanalyzer/briosa) SpatialAnalyzer bridge. It
provides idiomatic lifecycle and MP APIs while keeping generated protobuf and
gRPC types private.

The package does not include SpatialAnalyzer, the SA SDK, or a license. It
targets SpatialAnalyzer `2026.1.0529.7` exactly and Python 3.10 or later. The
complete protocol identity is pinned in [`protocol.lock.json`](protocol.lock.json).

## Package Identity

The distribution is named `briosa-2026-1-0529-7`, while application code keeps
the stable `briosa` import package. Install the distribution with:

```powershell
python -m pip install briosa-2026-1-0529-7==0.3.0
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

The client retains lifecycle generations and supplies guards automatically.
Typed lifecycle failures, compatibility failures, task cancellation, ambiguous
MP completion, and replay guidance remain distinct. MP operations are never
automatically replayed.

See the [Briosa documentation](https://spatialanalyzer.github.io/briosa-docs/api/python/)
for the client API overview. The target-specific source and locked protocol define
this package's exact API.

## Server selection

Applications select a server independently of their protocol generation pin.
On Windows x64, discovery reads Registry64 installation hints, committed
canonical stores, explicit search roots, and supported local layouts. It validates
receipts and manifests, filters the exact SA target and compatibility contract,
and selects the highest compatible stable release. No internet access is needed.

This client requires behavioral contract **1.0** (major 1, revision at least 0).
The exact published Server 0.6.1 identity is also supported through a tested
legacy exception. Other servers without contract metadata are rejected. Protocol
and source pins remain exact build inputs; startup verifies the running server
against its selected installation instead of requiring the generation build.

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

selection = BriosaServerSelection(version="0.6.1")
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
  -ArtifactPath C:\path\to\briosa-client-conformance-0.6.1-sa-2026.1.0529.7-win-x64.zip `
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
  C:\path\to\briosa-protocol-0.7.0-sa-2026.1.0529.7.zip `
  --update --source-channel github_release

./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.7.0-sa-2026.1.0529.7.zip
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
contract against packaged servers, including the retained 0.6.1 baseline.
Exact SA target, runtime identity, capabilities, and readiness still gate MP calls.

Portable conformance covers lifecycle, identity mismatch, denied capabilities,
typed MP and output failure, deadlines, cancellation, watchdog recovery, SDK loss,
and owned-process cleanup. Its harness disables Control Center auto-launch and
restores the prior setting afterward. These checks use a fake SDK, without a
SpatialAnalyzer installation or license.

The public relationship-reference inputs use `CollectionItemName`, including
the item name and optional item type; they are not geometric object references.
This corrects earlier pre-publication facade annotations that disagreed with the
protocol. Existing callers of those methods must pass the item-name value.

Broader licensed runtime coverage and protected runtime CI remain outstanding.
Enterprise Artifactory integration is also unverified. This package remains v0.x;
portable results do not imply v1.0 readiness or validation on physical instruments.
