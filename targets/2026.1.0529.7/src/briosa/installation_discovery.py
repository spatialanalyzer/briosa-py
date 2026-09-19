"""Registry and committed-store discovery. Never starts a server or activates COM."""

from __future__ import annotations

import base64
import ctypes
import hashlib
import json
import os
import stat
import subprocess
from dataclasses import replace
from pathlib import Path
from typing import Any, cast

from briosa._installation_policy import LEGACY_VERSION, select_installation
from briosa.errors import BriosaStartupError
from briosa.installation_models import (
    BriosaDiscoveryDiagnostic,
    BriosaDiscoveryReport,
    BriosaInstallation,
    BriosaServerSelection,
    Scope,
    path_key,
    valid_version,
)
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET

_REQUIRED = ("manifest.json", "Briosa.Server.exe", "Briosa.Worker.exe")
_REGISTRY = r"Software\Briosa\Installations"


def installation_id(directory: Path) -> str:
    return hashlib.sha256(path_key(directory).encode("utf-8")).hexdigest()


def _local(path: Path) -> bool:
    return path.is_absolute() and not str(path).startswith("\\\\")


def _no_links(path: Path) -> None:
    for item in (path, *path.parents):
        if item.exists() and (
            item.is_symlink()
            or getattr(item.stat(follow_symlinks=False), "st_file_attributes", 0)
            & stat.FILE_ATTRIBUTE_REPARSE_POINT
        ):
            raise ValueError("Linked installations are not eligible")


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate metadata property")
        result[key] = value
    return result


def _json(data: bytes | str) -> dict[str, Any]:
    try:
        value: Any = json.loads(data, object_pairs_hook=_unique)
    except RecursionError as error:
        raise ValueError("Metadata nesting limit exceeded") from error
    if not isinstance(value, dict):
        raise ValueError("Metadata must be an object")
    return value


def _read(path: Path, limit: int) -> bytes:
    _no_links(path)
    with path.open("rb") as stream:
        data = stream.read(limit + 1)
    if len(data) > limit:
        raise ValueError("Metadata size limit exceeded")
    return data


def _text(value: dict[str, Any], key: str) -> str:
    item = value.get(key)
    if not isinstance(item, str):
        raise ValueError("Invalid string metadata")
    return item


def _uint(value: dict[str, Any], key: str) -> int:
    item = value.get(key)
    if type(item) is not int or not 0 <= item <= 4294967295:
        raise ValueError("Invalid numeric metadata")
    return item


def _hex(value: str, length: int) -> bool:
    return len(value) == length and all(c in "0123456789abcdef" for c in value)


def read_installation(path: Path, scope: Scope) -> BriosaInstallation:
    path = Path(path)
    if not _local(path) or path.name.lower() != "briosa.server.exe":
        raise ValueError("Invalid server path")
    path = Path(os.path.abspath(path))
    _no_links(path)
    if not path.is_file():
        raise FileNotFoundError(path)
    payload, product = path.parent, path.parent.parent
    managed = payload.name.lower() == "payload"
    data = _read(payload / "manifest.json", 1024 * 1024)
    manifest = _json(data)
    schema = _uint(manifest, "schemaVersion")
    version, target, rid, source = (
        _text(manifest, key)
        for key in (
            "briosaVersion",
            "spatialAnalyzerTarget",
            "runtimeIdentifier",
            "sourceRevision",
        )
    )
    artifact = f"briosa-{version}-sa-{target}-{rid}"
    if (
        schema not in (2, 3)
        or not valid_version(version)
        or not _hex(source, 40)
        or not 1 <= len(target) <= 64
        or not 1 <= len(rid) <= 64
        or manifest.get("artifactName") != artifact
        or manifest.get("protocolPackage") != "briosa"
        or manifest.get("spatialAnalyzerBundled") is not False
    ):
        raise ValueError("Invalid server manifest")
    major = revision = 0
    if schema == 3:
        contract = manifest.get("compatibility")
        if not isinstance(contract, dict):
            raise ValueError("Missing compatibility")
        major, revision = _uint(contract, "major"), _uint(contract, "revision")
        if major == 0:
            raise ValueError("Invalid compatibility major")
    digest = hashlib.sha256(data).hexdigest()
    for name in _REQUIRED:
        _no_links(payload / name)
        if not (payload / name).is_file():
            raise FileNotFoundError(payload / name)
    if managed:
        if product.name != artifact or product.parent.name.lower() != "products":
            raise ValueError("Not a committed product location")
        receipt = _json(_read(product / "receipt.json", 8 * 1024 * 1024))
        package, files = receipt.get("package"), receipt.get("files")
        if (
            _uint(receipt, "schemaVersion") != 1
            or not isinstance(package, dict)
            or package.get("id") != artifact
            or package.get("component") != "server"
            or package.get("version") != version
            or package.get("spatialAnalyzerTarget") != target
            or package.get("runtimeIdentifier") != rid
            or not isinstance(files, dict)
        ):
            raise ValueError("Receipt mismatch")
        if (
            any(not _hex(_text(files, name), 64) for name in _REQUIRED)
            or files["manifest.json"] != digest
        ):
            raise ValueError("Missing or mismatched file evidence")
    return BriosaInstallation(
        installation_id(product if managed else payload),
        path.absolute(),
        version,
        source,
        target,
        rid,
        major,
        revision,
        digest,
        scope,
    )


def _registrations(
    elevated: bool, diagnostics: list[BriosaDiscoveryDiagnostic]
) -> list[tuple[Path, Scope, dict[str, Any]]]:
    if os.name != "nt":
        return []
    import winreg

    result: list[tuple[Path, Scope, dict[str, Any]]] = []
    for hive, scope in (
        (winreg.HKEY_LOCAL_MACHINE, "machine"),
        (winreg.HKEY_CURRENT_USER, "user"),
    ):
        if elevated and scope == "user":
            continue
        try:
            with winreg.OpenKey(
                hive, _REGISTRY, 0, winreg.KEY_READ | winreg.KEY_WOW64_64KEY
            ) as root:
                for index in range(min(winreg.QueryInfoKey(root)[0], 1000)):
                    identity = winreg.EnumKey(root, index)
                    try:
                        with winreg.OpenKey(root, identity) as key:
                            raw, kind = winreg.QueryValueEx(key, "Registration")
                        if (
                            kind != winreg.REG_SZ
                            or not isinstance(raw, str)
                            or len(raw) > 32768
                        ):
                            continue
                        hint = _json(raw)
                        directory = Path(_text(hint, "productDirectory"))
                        if (
                            _uint(hint, "schemaVersion") == 1
                            and _local(directory)
                            and identity
                            == hint.get("installationId")
                            == installation_id(directory)
                        ):
                            result.append((directory, cast(Scope, scope), hint))
                    except (OSError, ValueError):
                        diagnostics.append(
                            BriosaDiscoveryDiagnostic(
                                f"{scope}:{identity}", "server-registration-invalid"
                            )
                        )
        except FileNotFoundError:
            pass
        except OSError:
            diagnostics.append(
                BriosaDiscoveryDiagnostic(scope, "server-registration-unavailable")
            )
    return result


def _elevated() -> bool:
    return os.name == "nt" and bool(ctypes.windll.shell32.IsUserAnAdmin())


def _protected(path: Path) -> bool:
    # A constant program receives paths as JSON data, never interpolated shell text.
    script = (
        Path(__file__)
        .with_name("_protected_installation.ps1")
        .read_text(encoding="utf-8")
    )
    try:
        executable = (
            Path(os.environ.get("SYSTEMROOT", r"C:\Windows"))
            / "System32/WindowsPowerShell/v1.0/powershell.exe"
        )
        result = subprocess.run(
            [
                str(executable),
                "-NoProfile",
                "-NonInteractive",
                "-EncodedCommand",
                base64.b64encode(script.encode("utf-16le")).decode("ascii"),
            ],
            input=json.dumps(str(path)),
            encoding="utf-8",
            capture_output=True,
            timeout=10,
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )
        return result.returncode == 0 and result.stdout.strip() == "true"
    except (OSError, subprocess.TimeoutExpired):
        return False


def discover_installations(
    selection: BriosaServerSelection | None = None,
) -> BriosaDiscoveryReport:
    options = selection or BriosaServerSelection()
    if os.name != "nt":
        return BriosaDiscoveryReport((), (), None, "server-platform-unsupported")
    candidates: list[BriosaInstallation] = []
    diagnostics: list[BriosaDiscoveryDiagnostic] = []
    explicit = options.executable_path
    if (
        explicit is None
        and options.installation_id is None
        and options.use_legacy_environment_override
    ):
        raw = os.environ.get("BRIOSA_SERVER_PATH")
        explicit = Path(raw) if raw is not None else None
    if explicit is not None:
        try:
            candidate = read_installation(explicit, "portable")
            selected, code = select_installation(
                (candidate,), replace(options, executable_path=explicit)
            )
            return BriosaDiscoveryReport((candidate,), (), selected, code)
        except (OSError, ValueError):
            return BriosaDiscoveryReport(
                (),
                (
                    BriosaDiscoveryDiagnostic(
                        str(explicit), "server-installation-invalid"
                    ),
                ),
                None,
                "server-installation-invalid",
            )
    elevated = _elevated()

    def add(path: Path, scope: Scope, hint: dict[str, Any] | None = None) -> None:
        if scope not in options.allowed_scopes or (elevated and scope != "machine"):
            return
        try:
            candidate = read_installation(path, scope)
            if hint is not None and any(
                hint.get(key) != value
                for key, value in {
                    "installationId": candidate.installation_id,
                    "serverVersion": candidate.version,
                    "spatialAnalyzerTarget": candidate.spatial_analyzer_target,
                    "runtimeIdentifier": candidate.runtime_identifier,
                    "packageId": (
                        f"briosa-{candidate.version}-sa-"
                        f"{candidate.spatial_analyzer_target}-{candidate.runtime_identifier}"
                    ),
                }.items()
            ):
                raise ValueError("Registration mismatch")
            if elevated and not _protected(path):
                return
            if not any(
                path_key(c.executable_path) == path_key(candidate.executable_path)
                for c in candidates
            ):
                candidates.append(candidate)
        except (OSError, ValueError):
            diagnostics.append(
                BriosaDiscoveryDiagnostic(str(path), "server-installation-invalid")
            )

    for directory, scope, hint in _registrations(elevated, diagnostics):
        add(directory / "payload/Briosa.Server.exe", scope, hint)
    user = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData/Local")
    roots: list[tuple[Path, Scope]] = [(user / "Briosa/Packages", "user")]
    machine = os.environ.get("PROGRAMDATA")
    if machine:
        roots.append((Path(machine) / "Briosa/Packages", "machine"))
    roots.extend((Path(path), "portable") for path in options.search_roots)
    for store, scope in roots:
        if (
            not _local(store)
            or scope not in options.allowed_scopes
            or (elevated and scope != "machine")
        ):
            continue
        try:
            _no_links(store)
            products = store / "products"
            if products.is_dir():
                _no_links(products)
                for index, product in enumerate(products.iterdir()):
                    if index >= 1000:
                        break
                    if product.is_dir():
                        add(product / "payload/Briosa.Server.exe", scope)
        except (OSError, ValueError):
            diagnostics.append(
                BriosaDiscoveryDiagnostic(str(store), "server-store-unavailable")
            )
    if not elevated and "portable" in options.allowed_scopes:
        for path in (
            Path(__file__).parent / "briosa-server/Briosa.Server.exe",
            user
            / "Briosa/servers"
            / LEGACY_VERSION
            / f"sa-{SPATIAL_ANALYZER_TARGET}/Briosa.Server.exe",
        ):
            if path.is_file():
                add(path, "portable")
    selected, code = select_installation(tuple(candidates), options)
    for candidate in candidates:
        _, rejected = select_installation((candidate,), options)
        if rejected:
            diagnostics.append(
                BriosaDiscoveryDiagnostic(str(candidate.executable_path), rejected)
            )
    if selected is None and not candidates and diagnostics:
        code = "server-installation-invalid"
    return BriosaDiscoveryReport(tuple(candidates), tuple(diagnostics), selected, code)


def resolve_installation(
    selection: BriosaServerSelection | None = None,
) -> BriosaInstallation:
    report = discover_installations(selection)
    if report.selected is None:
        raise BriosaStartupError(
            report.diagnostic_code or "server-distribution-not-found"
        )
    return report.selected
