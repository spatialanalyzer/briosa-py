from __future__ import annotations

import json
from pathlib import Path
from typing import cast

import pytest

from briosa._server_discovery import _resolve
from briosa.errors import BriosaStartupError
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)

PRODUCT_ID = f"briosa-{BRIOSA_VERSION}-sa-{SPATIAL_ANALYZER_TARGET}-win-x64"


def touch(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("fixture")
    return path


def install(root: Path) -> Path:
    product = root / "Briosa" / "Packages" / "products" / PRODUCT_ID
    payload = product / "payload"
    server = touch(payload / "Briosa.Server.exe")
    touch(payload / "Briosa.Worker.exe")
    (payload / "manifest.json").write_text(
        json.dumps(
            {
                "schemaVersion": 2,
                "artifactName": PRODUCT_ID,
                "briosaVersion": BRIOSA_VERSION,
                "spatialAnalyzerTarget": SPATIAL_ANALYZER_TARGET,
                "runtimeIdentifier": "win-x64",
                "sourceRevision": SOURCE_REVISION,
                "protocolPackage": "briosa",
                "spatialAnalyzerBundled": False,
            }
        )
    )
    (product / "receipt.json").write_text(
        json.dumps(
            {
                "schemaVersion": 1,
                "package": {
                    "id": PRODUCT_ID,
                    "component": "server",
                    "version": BRIOSA_VERSION,
                    "spatialAnalyzerTarget": SPATIAL_ANALYZER_TARGET,
                    "runtimeIdentifier": "win-x64",
                },
                "files": {
                    name: "a" * 64
                    for name in (
                        "manifest.json",
                        "Briosa.Server.exe",
                        "Briosa.Worker.exe",
                    )
                },
            }
        )
    )
    return server


def resolve(root: Path, configured: Path | None = None) -> Path:
    return _resolve(
        str(configured) if configured else None,
        root / "client",
        str(root / "user"),
        str(root / "machine"),
    )


def test_explicit_local_user_machine_legacy_precedence(tmp_path: Path) -> None:
    legacy = touch(
        tmp_path
        / "user"
        / "Briosa"
        / "servers"
        / BRIOSA_VERSION
        / f"sa-{SPATIAL_ANALYZER_TARGET}"
        / "Briosa.Server.exe"
    )
    assert resolve(tmp_path) == legacy
    machine = install(tmp_path / "machine")
    assert resolve(tmp_path) == machine
    user = install(tmp_path / "user")
    assert resolve(tmp_path) == user
    local = touch(tmp_path / "client" / "briosa-server" / "Briosa.Server.exe")
    assert resolve(tmp_path) == local
    custom = touch(tmp_path / "custom" / "Briosa.Server.exe")
    assert resolve(tmp_path, custom) == custom
    assert resolve(tmp_path, tmp_path / "absent" / "Briosa.Server.exe") == local
    assert resolve(tmp_path, touch(tmp_path / "not-Briosa.Server.exe")) == local


@pytest.mark.parametrize(
    ("name", "keys", "value"),
    [
        ("receipt.json", ("schemaVersion",), True),
        ("receipt.json", ("package",), None),
        ("receipt.json", ("package", "id"), "wrong"),
        ("receipt.json", ("package", "component"), "installer"),
        ("receipt.json", ("package", "version"), "99.0.0"),
        ("receipt.json", ("package", "spatialAnalyzerTarget"), "other"),
        ("receipt.json", ("package", "runtimeIdentifier"), "win-arm64"),
        ("receipt.json", ("files",), {}),
        ("receipt.json", ("files", "Briosa.Worker.exe"), "invalid"),
        ("manifest.json", ("schemaVersion",), 99),
        ("manifest.json", ("artifactName",), "wrong"),
        ("manifest.json", ("briosaVersion",), "99.0.0"),
        ("manifest.json", ("spatialAnalyzerTarget",), "other"),
        ("manifest.json", ("runtimeIdentifier",), "win-arm64"),
        ("manifest.json", ("sourceRevision",), "wrong"),
        ("manifest.json", ("protocolPackage",), "wrong"),
        ("manifest.json", ("spatialAnalyzerBundled",), True),
    ],
)
def test_invalid_metadata_is_skipped(
    tmp_path: Path, name: str, keys: tuple[str, ...], value: object
) -> None:
    payload = install(tmp_path / "user").parent
    path = (payload.parent if name == "receipt.json" else payload) / name
    document = json.loads(path.read_text())
    parent = cast(dict[str, object], document)
    for key in keys[:-1]:
        parent = cast(dict[str, object], parent[key])
    parent[keys[-1]] = value
    path.write_text(json.dumps(document))
    with pytest.raises(BriosaStartupError, match="server-distribution-not-found"):
        resolve(tmp_path)
    machine = install(tmp_path / "machine")
    assert resolve(tmp_path) == machine


@pytest.mark.parametrize(
    "name", ["receipt.json", "manifest.json", "Briosa.Server.exe", "Briosa.Worker.exe"]
)
@pytest.mark.parametrize("damage", ["missing", "directory"])
def test_missing_or_directory_file_is_skipped(
    tmp_path: Path, name: str, damage: str
) -> None:
    payload = install(tmp_path / "user").parent
    path = (payload.parent if name == "receipt.json" else payload) / name
    path.unlink()
    if damage == "directory":
        path.mkdir()
    with pytest.raises(BriosaStartupError):
        resolve(tmp_path)
    machine = install(tmp_path / "machine")
    assert resolve(tmp_path) == machine


@pytest.mark.parametrize("name", ["receipt.json", "manifest.json"])
@pytest.mark.parametrize("content", ["{", "[]", "null"])
def test_malformed_document_is_skipped(tmp_path: Path, name: str, content: str) -> None:
    payload = install(tmp_path / "user").parent
    path = (payload.parent if name == "receipt.json" else payload) / name
    path.write_text(content)
    with pytest.raises(BriosaStartupError):
        resolve(tmp_path)
    machine = install(tmp_path / "machine")
    assert resolve(tmp_path) == machine


def test_other_product_directories_transactions_and_unavailable_roots(
    tmp_path: Path,
) -> None:
    product = install(tmp_path / "user").parent.parent
    other = product.with_name(product.name + "-other")
    product.rename(other)
    with pytest.raises(BriosaStartupError):
        resolve(tmp_path)
    staging = (
        tmp_path
        / "user"
        / "Briosa"
        / "Packages"
        / "transactions"
        / "pending"
        / PRODUCT_ID
    )
    staging.parent.mkdir(parents=True)
    other.rename(staging)
    with pytest.raises(BriosaStartupError):
        resolve(tmp_path)
    for missing_root in ("", "relative"):
        with pytest.raises(BriosaStartupError):
            _resolve(None, tmp_path / "client", missing_root, missing_root)
