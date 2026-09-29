from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import pytest

from briosa import (
    BriosaCompatibilityError,
    BriosaInstallation,
    BriosaServerSelection,
    discover_installations,
    discovery_pb2,
    version_coordinates_pb2,
)
from briosa._installation_policy import (
    LEGACY_REVISION,
    LEGACY_VERSION,
    select_installation,
)
from briosa.installation_discovery import read_installation
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET
from briosa.transport import _validate_compatibility, validate_installation


def test_shared_selection_vectors() -> None:
    data = json.loads(
        (Path(__file__).parent / "fixtures/selection-cases.json").read_text()
    )
    names = {
        "executablePath": "executable_path",
        "allowPrerelease": "allow_prerelease",
        "version": "version",
        "installationId": "installation_id",
        "minimumVersion": "minimum_version",
        "maximumVersionExclusive": "maximum_version_exclusive",
        "excludedVersions": "excluded_versions",
        "allowedScopes": "allowed_scopes",
    }
    for case in data["cases"]:
        options = BriosaServerSelection(
            **{names[k]: v for k, v in case["options"].items()}
        )
        candidates = tuple(
            BriosaInstallation(
                c["id"],
                Path(c["path"]),
                c["version"],
                c["sourceRevision"],
                c["target"],
                c["rid"],
                c["major"],
                c["revision"],
                c["manifestSha256"],
                c["scope"],
            )
            for c in case["candidates"]
        )
        selected, code = select_installation(
            candidates,
            options,
            case["target"],
            case["requiredMajor"],
            case["minimumRevision"],
        )
        assert (selected.installation_id if selected else None) == case["selectedId"], (
            case["name"]
        )
        assert code == case.get("error"), case["name"]


def install(root: Path) -> Path:
    identity = f"briosa-0.7.0-sa-{SPATIAL_ANALYZER_TARGET}-win-x64"
    product = root / "products" / identity
    payload = product / "payload"
    payload.mkdir(parents=True)
    manifest = json.dumps(
        {
            "schemaVersion": 3,
            "artifactName": identity,
            "briosaVersion": "0.7.0",
            "sourceRevision": "a" * 40,
            "spatialAnalyzerTarget": SPATIAL_ANALYZER_TARGET,
            "runtimeIdentifier": "win-x64",
            "protocolPackage": "briosa",
            "spatialAnalyzerBundled": False,
            "compatibility": {"major": 1, "revision": 0},
        }
    ).encode()
    (payload / "manifest.json").write_bytes(manifest)
    for name in ("Briosa.Server.exe", "Briosa.Worker.exe"):
        (payload / name).write_text("inert")
    (product / "receipt.json").write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "package": {
                    "id": identity,
                    "component": "server",
                    "version": "0.7.0",
                    "spatialAnalyzerTarget": SPATIAL_ANALYZER_TARGET,
                    "runtimeIdentifier": "win-x64",
                },
                "files": {
                    "manifest.json": hashlib.sha256(manifest).hexdigest(),
                    "Briosa.Server.exe": "a" * 64,
                    "Briosa.Worker.exe": "a" * 64,
                },
            }
        )
    )
    return payload / "Briosa.Server.exe"


def test_receipt_manifest_identity_is_verified(tmp_path: Path) -> None:
    path = install(tmp_path)
    assert read_installation(path, "user").version == "0.7.0"
    manifest = path.parent / "manifest.json"
    value = json.loads(manifest.read_text())
    value["sourceRevision"] = "b" * 40
    manifest.write_text(json.dumps(value))
    with pytest.raises(ValueError, match="file evidence"):
        read_installation(path, "user")


def test_missing_worker_is_not_a_distribution(tmp_path: Path) -> None:
    path = install(tmp_path)
    (path.parent / "Briosa.Worker.exe").unlink()
    with pytest.raises(FileNotFoundError):
        read_installation(path, "user")


def test_invalid_explicit_selection_never_falls_back(tmp_path: Path) -> None:
    report = discover_installations(
        BriosaServerSelection(executable_path=tmp_path / "missing/Briosa.Server.exe")
    )
    assert report.selected is None
    assert report.diagnostic_code in (
        "server-installation-invalid",
        "server-platform-unsupported",
    )


def snapshot() -> tuple[Any, Any]:
    return (
        discovery_pb2.GetServerInfoResponse(
            version=version_coordinates_pb2.VersionCoordinates(
                briosa_version="0.9.0",
                source_revision="a" * 40,
                protocol_package="briosa",
                spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
            ),
            compatibility=discovery_pb2.CompatibilityContract(major=2),
            target_isolation_mode=discovery_pb2.TARGET_ISOLATION_MODE_SINGLE_TENANT,
        ),
        discovery_pb2.ListCapabilitiesResponse(
            protocol_package="briosa",
            spatial_analyzer_target=SPATIAL_ANALYZER_TARGET,
        ),
    )


def test_contract_compatibility_and_selected_identity_are_separate() -> None:
    server, capabilities = snapshot()
    _validate_compatibility(server, capabilities)
    installation = BriosaInstallation(
        "id",
        Path("path"),
        "0.9.0",
        "a" * 40,
        SPATIAL_ANALYZER_TARGET,
        "win-x64",
        2,
        0,
        "hash",
        "user",
    )
    validate_installation(server, installation)
    server.version.source_revision = "b" * 40
    _validate_compatibility(server, capabilities)
    with pytest.raises(BriosaCompatibilityError):
        validate_installation(server, installation)
    server.compatibility.major = 1
    with pytest.raises(BriosaCompatibilityError):
        _validate_compatibility(server, capabilities)


def test_missing_contract_is_rejected_including_legacy_build() -> None:
    server, capabilities = snapshot()
    server.ClearField("compatibility")
    with pytest.raises(BriosaCompatibilityError):
        _validate_compatibility(server, capabilities)
    server.version.briosa_version = LEGACY_VERSION
    server.version.source_revision = LEGACY_REVISION
    with pytest.raises(BriosaCompatibilityError, match="server-contract-incompatible"):
        _validate_compatibility(server, capabilities)
    server.version.source_revision = "a" * 40
    with pytest.raises(BriosaCompatibilityError):
        _validate_compatibility(server, capabilities)
