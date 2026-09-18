"""Internal executable lookup; shared policy lives in the Briosa store contract."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import cast

from briosa.errors import BriosaStartupError
from briosa.protocol_identity import (
    BRIOSA_VERSION,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)


def resolve_server_executable() -> Path:
    return _resolve(
        os.environ.get("BRIOSA_SERVER_PATH"),
        Path(__file__).resolve().parent,
        os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local"),
        os.environ.get("PROGRAMDATA", ""),
    )


def _resolve(
    configured: str | None,
    module_directory: Path,
    local_app_data: str,
    common_app_data: str,
) -> Path:
    for candidate in (
        Path(configured) if configured else None,
        module_directory / "briosa-server" / "Briosa.Server.exe",
    ):
        if (
            candidate
            and candidate.name.lower() == "briosa.server.exe"
            and _is_file(candidate)
        ):
            return candidate.resolve()
    for root in (local_app_data, common_app_data):
        if not root or not Path(root).is_absolute():
            continue
        managed = _managed_executable(Path(root) / "Briosa" / "Packages")
        if managed is not None:
            return managed
    if local_app_data and Path(local_app_data).is_absolute():
        legacy = (
            Path(local_app_data)
            / "Briosa"
            / "servers"
            / BRIOSA_VERSION
            / f"sa-{SPATIAL_ANALYZER_TARGET}"
            / "Briosa.Server.exe"
        )
        if _is_file(legacy):
            return legacy.resolve()
    raise BriosaStartupError("server-distribution-not-found")


def _is_file(path: Path) -> bool:
    try:
        return path.is_file()
    except (OSError, ValueError):
        return False


def _object(value: object) -> dict[str, object]:
    return cast(dict[str, object], value) if isinstance(value, dict) else {}


def _managed_executable(store: Path) -> Path | None:
    product_id = f"briosa-{BRIOSA_VERSION}-sa-{SPATIAL_ANALYZER_TARGET}-win-x64"
    product = store / "products" / product_id
    payload = product / "payload"
    try:
        receipt = _object(
            json.loads((product / "receipt.json").read_text(encoding="utf-8"))
        )
        manifest = _object(
            json.loads((payload / "manifest.json").read_text(encoding="utf-8"))
        )
        package = _object(receipt.get("package"))
        if (
            type(receipt.get("schemaVersion")) is not int
            or receipt.get("schemaVersion") != 1
            or type(manifest.get("schemaVersion")) is not int
            or manifest.get("schemaVersion") != 2
            or package.get("id") != product_id
            or package.get("component") != "server"
            or package.get("version") != BRIOSA_VERSION
            or package.get("runtimeIdentifier") != "win-x64"
            or package.get("spatialAnalyzerTarget") != SPATIAL_ANALYZER_TARGET
            or manifest.get("artifactName") != product_id
            or manifest.get("briosaVersion") != BRIOSA_VERSION
            or manifest.get("spatialAnalyzerTarget") != SPATIAL_ANALYZER_TARGET
            or manifest.get("runtimeIdentifier") != "win-x64"
            or manifest.get("sourceRevision") != SOURCE_REVISION
            or manifest.get("protocolPackage") != "briosa"
            or manifest.get("spatialAnalyzerBundled") is not False
        ):
            return None
        files = _object(receipt.get("files"))
        for name in ("manifest.json", "Briosa.Server.exe", "Briosa.Worker.exe"):
            digest = files.get(name)
            if (
                not isinstance(digest, str)
                or re.fullmatch(r"[0-9a-f]{64}", digest) is None
                or not _is_file(payload / name)
            ):
                return None
        return (payload / "Briosa.Server.exe").resolve()
    except (OSError, ValueError):
        return None
