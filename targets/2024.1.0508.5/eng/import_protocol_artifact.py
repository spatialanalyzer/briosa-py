"""Verify one Briosa protocol artifact and deterministically generate Python stubs."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
LOCK_PATH = REPOSITORY_ROOT / "protocol.lock.json"
SOURCE_ROOT = REPOSITORY_ROOT / "src"
BRIOSA_ROOT = SOURCE_ROOT / "briosa"
GENERATED_TREES = (BRIOSA_ROOT / "core", BRIOSA_ROOT / "sa")
IDENTITY_PATH = BRIOSA_ROOT / "protocol_identity.py"
GENERATED_PATTERNS = ("*_pb2.py", "*_pb2.pyi", "*_pb2_grpc.py")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path.name} must contain a JSON object")
    return value


def _require(actual: object, expected: object, message: str) -> None:
    if actual != expected:
        raise ValueError(message)


def _extract_verified(artifact: Path, destination: Path) -> tuple[Path, dict[str, Any]]:
    artifact_hash = _sha256(artifact)
    checksum_path = Path(f"{artifact}.sha256")
    if not checksum_path.is_file():
        raise ValueError("The adjacent protocol ZIP checksum does not exist")
    _require(
        checksum_path.read_text(encoding="utf-8").strip(),
        f"{artifact_hash}  {artifact.name}",
        "The external protocol ZIP checksum does not match",
    )

    with zipfile.ZipFile(artifact) as archive:
        names = [item.filename for item in archive.infolist() if not item.is_dir()]
        if not names:
            raise ValueError("The protocol artifact is empty")
        paths = [PurePosixPath(name) for name in names]
        if any(path.is_absolute() or ".." in path.parts for path in paths):
            raise ValueError("The protocol artifact contains an unsafe path")
        roots = {path.parts[0] for path in paths}
        if len(roots) != 1:
            raise ValueError(
                "The protocol artifact must contain one top-level directory"
            )
        archive.extractall(destination)

    bundle_root = destination / roots.pop()
    manifest = _load_json(bundle_root / "manifest.json")
    _require(manifest.get("schema_version"), 2, "Unsupported protocol manifest schema")
    _require(
        manifest.get("artifact_kind"), "briosa_protocol", "Unexpected artifact kind"
    )
    _require(
        manifest.get("client_generation_contract"),
        "standard-protobuf-grpc",
        "Unsupported client generation contract",
    )
    _require(manifest.get("artifact_name"), artifact.stem, "Artifact name drift")

    checksums: dict[str, str] = {}
    for line in (bundle_root / "files.sha256").read_text(encoding="utf-8").splitlines():
        fields = line.split("  ", 1)
        if len(fields) != 2 or len(fields[0]) != 64:
            raise ValueError("Malformed files.sha256 entry")
        checksums[fields[1]] = fields[0]
    actual_paths = sorted(
        path.relative_to(bundle_root).as_posix()
        for path in bundle_root.rglob("*")
        if path.is_file() and path.name != "files.sha256"
    )
    _require(sorted(checksums), actual_paths, "Unchecked or missing protocol content")
    for relative_path, expected_hash in checksums.items():
        _require(
            _sha256(bundle_root / relative_path),
            expected_hash,
            f"Protocol checksum mismatch: {relative_path}",
        )

    manifest_files = manifest.get("files")
    if not isinstance(manifest_files, list):
        raise ValueError("The protocol manifest file list is missing")
    recorded = {
        str(item["path"]): str(item["sha256"])
        for item in manifest_files
        if isinstance(item, dict) and "path" in item and "sha256" in item
    }
    _require(
        sorted(recorded),
        sorted(path for path in actual_paths if path != "manifest.json"),
        "The protocol manifest file list is incomplete",
    )
    for relative_path, expected_hash in recorded.items():
        _require(expected_hash, checksums[relative_path], "Manifest checksum drift")
    return bundle_root, manifest


def _generate(
    bundle_root: Path,
    output_root: Path,
    manifest: dict[str, Any],
    artifact_hash: str,
) -> None:
    proto_root = bundle_root / "proto"
    proto_files = sorted(
        path.relative_to(proto_root).as_posix() for path in proto_root.rglob("*.proto")
    )
    if not proto_files:
        raise ValueError("The protocol artifact contains no protobuf sources")
    command = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        f"--proto_path={proto_root}",
        f"--python_out={output_root}",
        f"--pyi_out={output_root}",
        f"--grpc_python_out={output_root}",
        *proto_files,
    ]
    subprocess.run(command, cwd=proto_root, check=True)

    generated_package = output_root / "briosa"

    identity_values = {
        "ARTIFACT_NAME": manifest["artifact_name"],
        "ARTIFACT_SHA256": artifact_hash,
        "BRIOSA_VERSION": manifest["briosa_version"],
        "SOURCE_REVISION": manifest["source_revision"],
        "PROTOCOL_SCHEMA_SHA256": manifest["protocol_schema_sha256"],
        "DESCRIPTOR_SET_SHA256": manifest["descriptor_set_sha256"],
        "PROTOCOL_PACKAGE": manifest["protocol_package"],
        "CLIENT_GENERATION_CONTRACT": manifest["client_generation_contract"],
        "SPATIAL_ANALYZER_TARGET": manifest["spatial_analyzer_target"],
    }
    identity_lines = [
        '"""Generated exact Briosa protocol identity. Do not edit."""',
        "",
        *(f"{key} = {value!r}" for key, value in identity_values.items()),
        "",
    ]
    (generated_package / "protocol_identity.py").write_text(
        "\n".join(identity_lines), encoding="utf-8", newline="\n"
    )


def _generated_files(root: Path) -> list[dict[str, str]]:
    return [
        {"path": path.relative_to(root).as_posix(), "sha256": _sha256(path)}
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]


def _make_lock(
    artifact: Path,
    artifact_hash: str,
    manifest: dict[str, Any],
    source_channel: str,
    generated_files: list[dict[str, str]],
) -> dict[str, Any]:
    return {
        "schema_version": 2,
        "artifact": {
            "name": manifest["artifact_name"],
            "file_name": artifact.name,
            "sha256": artifact_hash,
            "briosa_version": manifest["briosa_version"],
            "source_revision": manifest["source_revision"],
            "source_repository": "https://github.com/spatialanalyzer/briosa",
            "source_channel": source_channel,
        },
        "protocol": {
            "generation_contract": manifest["client_generation_contract"],
            "schema_sha256": manifest["protocol_schema_sha256"],
            "descriptor_sha256": manifest["descriptor_set_sha256"],
            "package": manifest["protocol_package"],
        },
        "target": {
            "spatial_analyzer": manifest["spatial_analyzer_target"],
        },
        "generation": {
            "grpcio_tools_version": importlib.metadata.version("grpcio-tools"),
            "protoc_version": subprocess.check_output(
                [sys.executable, "-m", "grpc_tools.protoc", "--version"],
                text=True,
            ).strip(),
            "files": generated_files,
        },
    }


def _apply_generated(generated_root: Path) -> None:
    for tree in GENERATED_TREES:
        if tree.exists():
            shutil.rmtree(tree)
    for pattern in GENERATED_PATTERNS:
        for path in BRIOSA_ROOT.glob(pattern):
            path.unlink()
    IDENTITY_PATH.unlink(missing_ok=True)
    for source in sorted((generated_root / "briosa").rglob("*")):
        if not source.is_file():
            continue
        destination = BRIOSA_ROOT / source.relative_to(generated_root / "briosa")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)


def _verify_generated(
    generated_root: Path, expected_files: list[dict[str, str]]
) -> None:
    generated_package = generated_root / "briosa"
    actual_files = []
    for relative in [str(item["path"]) for item in expected_files]:
        path = BRIOSA_ROOT / PurePosixPath(relative)
        if path.is_file():
            actual_files.append({"path": relative, "sha256": _sha256(path)})
    _require(actual_files, expected_files, "Generated protocol files have drifted")
    _require(
        _generated_files(generated_package),
        expected_files,
        "Generated protocol output is not deterministic",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--update", action="store_true")
    parser.add_argument(
        "--source-channel",
        choices=(
            "github_release",
            "github_actions_artifact",
            "source_commit_bootstrap",
        ),
    )
    args = parser.parse_args()
    artifact = args.artifact.resolve()
    if not artifact.is_file():
        raise ValueError("The protocol artifact does not exist")
    if not args.update and not LOCK_PATH.is_file():
        raise ValueError("protocol.lock.json is missing; use --update")

    existing_lock = _load_json(LOCK_PATH) if LOCK_PATH.is_file() else None
    source_channel = args.source_channel
    if source_channel is None:
        source_channel = (
            str(existing_lock["artifact"]["source_channel"])
            if existing_lock is not None and not args.update
            else "github_release"
        )

    with tempfile.TemporaryDirectory(prefix="briosa-py-protocol-") as temporary:
        temporary_root = Path(temporary)
        bundle_root, manifest = _extract_verified(artifact, temporary_root / "artifact")
        generated_root = temporary_root / "generated"
        generated_root.mkdir()
        artifact_hash = _sha256(artifact)
        _generate(bundle_root, generated_root, manifest, artifact_hash)
        generated_files = _generated_files(generated_root / "briosa")
        lock = _make_lock(
            artifact,
            artifact_hash,
            manifest,
            source_channel,
            generated_files,
        )
        if args.update:
            _apply_generated(generated_root)
            LOCK_PATH.write_text(
                json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n"
            )
            print("Updated generated Python protocol code and protocol.lock.json.")
        else:
            _require(
                existing_lock, lock, "Protocol artifact identity or toolchain drifted"
            )
            _verify_generated(generated_root, generated_files)
            print("Verified protocol identity and generated-code drift.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
