# Engineering workflows

`import_protocol_artifact.py` verifies one schema-2 Briosa protocol ZIP and its
adjacent checksum. `--update` regenerates the direct `src/briosa/*_pb2.py`,
`.pyi`, and `*_pb2_grpc.py` transport files plus the exact identity and lock.
Verification mode regenerates in a temporary directory and fails on identity,
toolchain, file-list, or generated-byte drift.

```powershell
./.venv/Scripts/python eng/import_protocol_artifact.py `
  C:\path\to\briosa-protocol-0.2.0-lifecycle-sa-2026.1.0529.7.zip `
  --update --source-channel source_commit_bootstrap
```

Generated transport modules are private implementation details. Handwritten
public dataclasses, enums, lifecycle orchestration, and exceptions live beside
them but never expose a generated value.

`tools/client_conformance.py` emits the normalized lifecycle contract
implemented by this package. Behavioral tests use fake server/transport
boundaries and require neither SpatialAnalyzer nor a license.
