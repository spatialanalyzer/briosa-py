"""Per-application installation selection values; construction performs no I/O."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

Scope = Literal["machine", "user", "portable"]
_ASCII_LOWER = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")


def path_key(value: Path) -> str:
    return os.path.abspath(value).replace("\\", "/").rstrip("/").translate(_ASCII_LOWER)


_VERSION = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*))?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)


def valid_version(value: str) -> bool:
    return len(value) <= 128 and _VERSION.fullmatch(value) is not None


def version_key(
    value: str,
) -> tuple[tuple[int, ...], int, tuple[tuple[int, int | str], ...]]:
    core, _, preview = value.split("+", 1)[0].partition("-")
    return (
        tuple(int(part) for part in core.split(".")),
        0 if preview else 1,
        tuple(
            (0, int(part)) if part.isascii() and part.isdigit() else (1, part)
            for part in preview.split(".")
        )
        if preview
        else (),
    )


@dataclass(frozen=True, slots=True)
class BriosaServerSelection:
    """Constrains one startup; explicit choices never silently fall back."""

    executable_path: Path | None = None
    installation_id: str | None = None
    version: str | None = None
    minimum_version: str | None = None
    maximum_version_exclusive: str | None = None
    excluded_versions: tuple[str, ...] = ()
    search_roots: tuple[Path, ...] = ()
    allowed_scopes: tuple[Scope, ...] = ("machine", "user", "portable")
    allow_prerelease: bool = False
    use_legacy_environment_override: bool = False
    spatial_analyzer_executable_path: Path | None = None

    def __post_init__(self) -> None:
        if self.executable_path is not None and self.installation_id is not None:
            raise ValueError(
                "executable_path and installation_id are mutually exclusive"
            )
        for path in (
            self.executable_path,
            self.spatial_analyzer_executable_path,
            *self.search_roots,
        ):
            if path is not None and (
                not Path(path).is_absolute() or str(path).startswith("\\\\")
            ):
                raise ValueError("Selection paths must be absolute local paths")
        for value in (
            self.version,
            self.minimum_version,
            self.maximum_version_exclusive,
            *self.excluded_versions,
        ):
            if value is not None and not valid_version(value):
                raise ValueError("Invalid server version constraint")
        if self.installation_id is not None and not self.installation_id.strip():
            raise ValueError("installation_id must not be empty")
        if not self.allowed_scopes or any(
            scope not in ("machine", "user", "portable")
            for scope in self.allowed_scopes
        ):
            raise ValueError("Invalid installation scope")


@dataclass(frozen=True, slots=True)
class BriosaInstallation:
    """Local installation evidence, independently checked against runtime identity."""

    installation_id: str
    executable_path: Path
    version: str
    source_revision: str
    spatial_analyzer_target: str
    runtime_identifier: str
    contract_major: int
    contract_revision: int
    manifest_sha256: str
    scope: Scope


@dataclass(frozen=True, slots=True)
class BriosaDiscoveryDiagnostic:
    path: str
    code: str


@dataclass(frozen=True, slots=True)
class BriosaDiscoveryReport:
    installations: tuple[BriosaInstallation, ...]
    diagnostics: tuple[BriosaDiscoveryDiagnostic, ...]
    selected: BriosaInstallation | None
    diagnostic_code: str | None
