# Briosa Python client

`briosa-client` is the thin asynchronous Python client for the open-source [Briosa](https://github.com/spatialanalyzer/briosa) gRPC bridge.

The package does not contain SpatialAnalyzer, the SpatialAnalyzer SDK, Briosa Server, or a license. Useful operation calls require a separately installed compatible Briosa server and a separately installed, running, licensed SpatialAnalyzer instance.

## Current compatibility

| Coordinate | Pinned value |
| --- | --- |
| SpatialAnalyzer | `2026.1.0529.7` exactly |
| Core protocol | `briosa.core.v1alpha1` |
| Target protocol | `briosa.sa.v2026_1_0529_7.v1alpha1` |
| Catalog | `briosa.sa.2026.1.0529.7`, revision `5` |
| Python | 3.10 or later |

The complete generation identity is committed in [`protocol.lock.json`](protocol.lock.json). Client package versions, Briosa server versions, protocol packages, catalog revisions, and SpatialAnalyzer releases are independent coordinates. Compatibility with any other SpatialAnalyzer release is not inferred.

Until Briosa publishes its first v0.2 release asset, the lock uses the reversible `source_commit_bootstrap` channel. CI rebuilds `0.2.0-dev.2` from immutable Briosa merge commit `1a0714345981592b37e26a90ffc4db0de32fe388` and verifies ZIP SHA-256 `4ce33ac6ecc9db382e870aa2c005f90a25128ad863fcf007c855d00470ea3e39`.

## Public API contract

The approved v1 design is defined in the [Briosa Python public API contract](docs/public-api-contract.md). It records the Python-specific decisions reviewed in [Discussion #6](https://github.com/orgs/spatialanalyzer/discussions/6#discussioncomment-17926452) and inherits cross-language guarantees from the authoritative [first-party client behavioral contract](https://github.com/spatialanalyzer/briosa/blob/main/docs/architecture/client-library-behavioral-contract.md).

The current code is an early bootstrap implementation and does not yet satisfy every contract rule. The example below documents the behavior in this checkout rather than the final v1 surface.

## Install and use the current bootstrap

Install the package into your application environment:

```console
python -m pip install briosa-client
```

The API is asynchronous and applies a deadline to every RPC:

```python
from briosa import BriosaClient


async def read_working_directory() -> str | None:
    async with BriosaClient(
        "http://127.0.0.1:50051", default_timeout=30.0
    ) as client:
        snapshot = await client.get_server_snapshot()
        if not snapshot.ready_for_mp:
            return None

        result = await client.get_working_directory()
        return result.directory if result.HasField("directory") else None
```

`get_server_snapshot()` validates the pinned protocol, catalog, exact SA target, and initial single-tenant isolation mode before returning discovery data. `snapshot.supports(...)` exposes capability discovery. Generated protobuf messages and gRPC stubs are currently importable under `briosa.core` and `briosa.sa`, but those imports and generated-message return values are bootstrap behavior rather than a supported part of the v1 idiomatic API. Raw gRPC consumers should generate bindings from the exact locked protocol artifact.

Protobuf presence is intentional: `result.HasField("directory")` distinguishes an absent output from a successfully retrieved empty string. Do not replace presence checks with truthiness checks.

Failed RPCs raise `BriosaCallError`. Its canonical `status_code` is independent from its optional typed `operation_error`; binary metadata is decoded from `briosa-operation-error-bin`, and status text is never parsed. `completion_unknown` and `reconciliation_required` remain distinct from worker recovery. The client performs no automatic operation replay.

Override a single deadline with `timeout=`. Cancel an in-flight RPC idiomatically by cancelling the containing `asyncio.Task`; cancellation does not imply the SpatialAnalyzer command was stopped or is safe to replay.

## Development

```powershell
python -m venv .venv
./.venv/Scripts/python -m pip install -e ".[dev]"
./.venv/Scripts/python -m ruff format --check .
./.venv/Scripts/python -m ruff check .
./.venv/Scripts/python -m mypy
./.venv/Scripts/python -m pytest
./.venv/Scripts/python -m build
```

Ordinary installation, builds, and unit tests require neither SpatialAnalyzer nor Briosa Server.

## Protocol regeneration and conformance

Regenerate only from an exact Briosa protocol ZIP with its adjacent `.zip.sha256` file:

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py C:\path\to\briosa-protocol-....zip --update
./.venv/Scripts/python eng/import_protocol_artifact.py C:\path\to\briosa-protocol-....zip
```

`--update` is an intentional dependency update. Verification regenerates into a temporary directory and fails on artifact, manifest, coordinate, generator, generated-file, or file-list drift. Never edit `src/briosa/core`, `src/briosa/sa`, `src/briosa/protocol_identity.py`, or `protocol.lock.json` by hand.

`eng/Test-Conformance.ps1` builds the pinned packaged Briosa server, substitutes its fake worker, and runs every shared live and typed-error fixture. It requires 64-bit Windows and the .NET SDK but not SpatialAnalyzer or a license. See [`eng/README.md`](eng/README.md) for exact commands.
