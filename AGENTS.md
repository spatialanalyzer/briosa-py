# Briosa Python client agent guide

This repository contains a thin, asynchronous Python client for Briosa. Shared protocol and operation semantics belong in `spatialanalyzer/briosa`, not here.

- Consume only a versioned Briosa protocol artifact and record its complete identity in `protocol.lock.json`.
- Never hand-edit `src/briosa/*_pb2.py`, `src/briosa/*_pb2.pyi`,
  `src/briosa/*_pb2_grpc.py`, or `src/briosa/protocol_identity.py`; regenerate
  them with `eng/import_protocol_artifact.py`.
- Keep hand-written code limited to idiomatic adapters, packaging, tests, and documentation.
- Preserve protobuf presence. An absent optional field is not equivalent to a present field containing a Python default-like value.
- Expose gRPC status separately from typed `OperationError` details. Never parse status text for policy.
- Never automatically replay an operation with ambiguous completion. Recovery and replay are independent decisions.
- Ordinary builds and tests must not require SpatialAnalyzer, an SA license, or proprietary SDK binaries.
- Keep public documentation and `eng/README.md` synchronized with behavior and tooling.

## Exact-target products

- Work in `targets/<exact-sa-release>/`; each product owns its source, locks, tests, tooling, and package metadata.
- Run build, regeneration, conformance, and packaging from that target directory.
- Do not reference another target's runtime source or generated transport.
- CI must cover both supported targets explicitly. Package versions are independent of server versions.
