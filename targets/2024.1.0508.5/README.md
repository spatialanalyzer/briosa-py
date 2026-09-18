# Briosa Python client

`briosa-2024-1-0508-5` is the asynchronous Python client for the open-source
[Briosa](https://github.com/spatialanalyzer/briosa) SpatialAnalyzer bridge. It
provides idiomatic lifecycle and MP APIs while keeping generated protobuf and
gRPC types private.

The package does not include SpatialAnalyzer, the SA SDK, or a license. It
targets SpatialAnalyzer `2024.1.0508.5` exactly and Python 3.10 or later. The
complete protocol identity is pinned in [`protocol.lock.json`](protocol.lock.json).

## Package Identity

The distribution is named `briosa-2024-1-0508-5`, while application code keeps
the stable `briosa` import package. Install the distribution with:

```powershell
python -m pip install briosa-2024-1-0508-5==0.1.0
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

## Server distribution lookup

Install **Briosa Server 0.6.0 for SA 2024.1.0508.5** with the Briosa Installer.
Default startup searches these locations in order:

1. `BRIOSA_SERVER_PATH`, pointing to `Briosa.Server.exe`.
2. A client-local `briosa-server/Briosa.Server.exe`.
3. `%LOCALAPPDATA%/Briosa/Packages/products/<package-id>/payload/Briosa.Server.exe`.
4. `%PROGRAMDATA%/Briosa/Packages/products/<package-id>/payload/Briosa.Server.exe`.
5. The legacy `%LOCALAPPDATA%/Briosa/servers/<briosa-version>/sa-<sa-target>/Briosa.Server.exe`.

For this client, `<package-id>` is `briosa-0.6.0-sa-2024.1.0508.5-win-x64`.
Managed installations must have a matching committed receipt, manifest, and required
entry points. Missing or invalid candidates are skipped; discovery never selects a
different server version or SA target. Runtime compatibility checks still apply.
Installer verification/repair checks package integrity separately.

For a custom Installer store, set `BRIOSA_SERVER_PATH` to the desired product's
`payload/Briosa.Server.exe`. Custom stores are not searched automatically.
The [shared discovery contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/installed-package-store.md#client-server-discovery)
defines precedence, eligibility, root handling, and the installation/runtime boundary.

## Development

Run these commands from `targets/2024.1.0508.5/`. Each target builds and
packages independently. Use a separate Python environment for each target.

```powershell
python -m venv .venv
./.venv/Scripts/python -m pip install -e ".[dev]"
./.venv/Scripts/python -m ruff format --check .
./.venv/Scripts/python -m ruff check .
./.venv/Scripts/python -m mypy
./.venv/Scripts/python -m pytest
./eng/Test-Conformance.ps1 `
  -ArtifactPath C:\path\to\briosa-client-conformance-0.6.0-sa-2024.1.0508.5-win-x64.zip `
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
  C:\path\to\briosa-protocol-0.6.0-sa-2024.1.0508.5.zip `
  --update --source-channel github_release

./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.6.0-sa-2024.1.0508.5.zip
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
and [server observability guide](https://github.com/spatialanalyzer/briosa/blob/main/targets/2024.1.0508.5/docs/operations/server-observability.md).

## Compatibility and validation

This package pins the matching Briosa v0.6.0 protocol and conformance bundles.
Startup checks the server version, source revision, protocol package, and exact
SA target before admitting MP calls. The other SA target is not interchangeable.

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

### SA 2024 differences

The facade implements the reviewed 996-operation SA 2024 surface. It omits later
commands and the three scan operations whose SDK bindings are unavailable in
this release. See the authoritative [compatibility record](https://github.com/spatialanalyzer/briosa/blob/v0.6.0/targets/2024.1.0508.5/docs/development/sa2024-compatibility.md)
for the complete command and field differences.

- Run Crib Sheet, Project Objects, and Stop Projection are available. Their
  instrument-dependent runtime validation remains outstanding.
- Surface-face construction takes seven explicit Boolean selectors (planes,
  cylinders, spheres, cones, lines, points, circles).
- Direct CAD Access requires an explicit surface compatibility mode; both QDAS
  operations require the caller's date/time stamp.
- General relationship statistics return Max Deviation without an inferred
  absolute-value guarantee. Cone properties omit cut length; points-to-objects
  statistics omit average deviation; feature-check reporting omits the later
  failed-vectors-only option.
- Enhanced Cloud and the three later system-string choices are absent. Reserved
  wire values stay reserved; remaining choices retain their original numbers.
- Instrument names retain the exact value supplied by the caller. The server
  validates against the 185 reviewed 2024 literals, including `PMT Arm 4m 7 dof`.
