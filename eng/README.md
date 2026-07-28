# Engineering workflows

## Protocol artifact

`import_protocol_artifact.py` accepts one exact Briosa protocol ZIP and requires its adjacent `.zip.sha256` sidecar. With `--update`, it verifies the full archive, generates the Python protobuf messages, `.pyi` types, asynchronous-capable gRPC transport stubs, identity constants, and `protocol.lock.json`. Without `--update`, it regenerates in a temporary directory and fails on any ZIP, manifest, coordinate, toolchain, file-list, or generated-byte drift.

Generation is pinned to `grpcio-tools==1.74.0` (`libprotoc 31.1`). Generated namespaces are `src/briosa/core` and `src/briosa/sa`; `src/briosa/protocol_identity.py` is also generated. Change the protocol artifact or importer and regenerate—never edit those outputs or the lock by hand.

For the current bootstrap artifact:

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.2.0-dev.2-sa-2026.1.0529.7-catalog-5.zip `
  --update --source-channel source_commit_bootstrap

./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.2.0-dev.2-sa-2026.1.0529.7-catalog-5.zip
```

The bootstrap channel is temporary. A released Briosa asset should use the default `github_release` source channel.

## Shared conformance

`Test-Conformance.ps1` requires the pinned protocol ZIP and an exact Briosa source checkout:

```powershell
./eng/Test-Conformance.ps1 `
  -ProtocolArtifactPath C:\path\to\briosa-protocol-0.2.0-dev.2-sa-2026.1.0529.7-catalog-5.zip `
  -BriosaRepository C:\path\to\briosa `
  -PythonPath ./.venv/Scripts/python.exe
```

The script validates every language-neutral typed-error fixture, builds the smoke worker and deterministic Windows server package from the lock's source revision, and runs all nine live scenarios through the public Python client. The scenarios cover readiness, unavailable and policy-denied states, MP and output failure, deadline, cancellation, watchdog recovery, and an unsupported target package. The runner does not print the returned working-directory value.

This workflow requires 64-bit Windows, Python 3.10 or later, and the repository's .NET SDK. It does not install, launch, or connect to SpatialAnalyzer and requires neither an SA license nor proprietary SDK binaries.
