# Engineering workflows

`import_protocol_artifact.py` verifies one schema-2 Briosa protocol ZIP and its
adjacent checksum. `--update` regenerates the direct `src/briosa/*_pb2.py`,
`.pyi`, and `*_pb2_grpc.py` transport files plus the exact identity and lock.
Verification mode regenerates in a temporary directory and fails on identity,
toolchain, file-list, or generated-byte drift.

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.6.0-sa-2026.1.0529.7.zip `
  --update --source-channel github_release
```

Generated transport modules are private implementation details. Handwritten
public dataclasses, enums, lifecycle orchestration, and exceptions live beside
them but never expose a generated value.

`Test-Conformance.ps1` verifies the immutable package named by
`conformance.lock.json`, then runs the shared Briosa scenario runner against the
public-API-only `tools/client_conformance.py` fixture. The package supplies the
real Briosa server plus a portable fake SDK/application host, so lifecycle,
compatibility, capability, failure, interruption, worker-loss, recovery, and
cleanup behavior can run in ordinary Windows CI without SpatialAnalyzer or a
license.


Run all commands from this exact-target directory. `Test-Conformance.ps1` runs
headlessly with `Briosa__Desktop__Mode=Disabled` for its child processes and restores
the caller's prior value. The package consumer check installs the actual local
package and validates the stable public namespace/import without launching SA.

`tests/test_server_discovery.py` covers the shared Installer discovery contract
using isolated user and machine stores. These portable tests do not launch SA.
