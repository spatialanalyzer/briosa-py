# Briosa Python client

`briosa-client` is the asynchronous Python client for the open-source
[Briosa](https://github.com/spatialanalyzer/briosa) SpatialAnalyzer bridge. It
provides idiomatic lifecycle and MP APIs while keeping generated protobuf and
gRPC types private.

The package does not include SpatialAnalyzer, the SA SDK, or a license. It
targets SpatialAnalyzer `2026.1.0529.7` exactly and Python 3.10 or later. The
complete protocol identity is pinned in [`protocol.lock.json`](protocol.lock.json).

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
for the complete Next API contract.

## Server distribution lookup

The client resolves the matching server distribution in this order:

1. `BRIOSA_SERVER_PATH`
2. A package-local `briosa-server/Briosa.Server.exe`
3. `%LOCALAPPDATA%/Briosa/servers/<briosa-version>/sa-<sa-target>/Briosa.Server.exe`

The locator is private so the installer/package layout can evolve without
adding executable paths to the public startup options.

## Development

```powershell
python -m venv .venv
./.venv/Scripts/python -m pip install -e ".[dev]"
./.venv/Scripts/python -m ruff format --check .
./.venv/Scripts/python -m ruff check .
./.venv/Scripts/python -m mypy
./.venv/Scripts/python -m pytest
./eng/Test-Conformance.ps1 `
  -ArtifactPath C:\path\to\briosa-client-conformance-0.2.0-lifecycle-sa-2026.1.0529.7-win-x64.zip `
  -PythonExecutable ./.venv/Scripts/python.exe
./.venv/Scripts/python -m build
```

Unit tests use fake server/transport boundaries. The shared conformance suite
runs the real client and server against a portable fake SDK/application host.
Neither path requires SpatialAnalyzer nor a license.

## Protocol regeneration

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.2.0-lifecycle-sa-2026.1.0529.7.zip `
  --update --source-channel source_commit_bootstrap

./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.2.0-lifecycle-sa-2026.1.0529.7.zip
```

Never edit generated `*_pb2.py`, `*_pb2.pyi`, `*_pb2_grpc.py`,
`protocol_identity.py`, or `protocol.lock.json` files by hand.
