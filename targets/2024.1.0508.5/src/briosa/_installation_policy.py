"""Shared-contract selection rules with no process, Registry, or filesystem access."""

from __future__ import annotations

from briosa.installation_models import (
    BriosaInstallation,
    BriosaServerSelection,
    path_key,
    version_key,
)
from briosa.protocol_identity import (
    COMPATIBILITY_MAJOR,
    SPATIAL_ANALYZER_TARGET,
)

LEGACY_VERSION = "0.6.1"
LEGACY_REVISION = "32a3b56ba4ae31ea5ec6ec3b2aa051eb61c866aa"

# The lowest server revision this client accepts, in installation selection and
# in live discovery alike. It is deliberately not the generated
# COMPATIBILITY_REVISION of the pinned protocol (1, Server 0.10.1): every feature
# this client uses from revision 1 is optional, so it keeps working with Server
# 0.10.0, which declares revision 0.
MINIMUM_COMPATIBILITY_REVISION = 0


def compatible(
    major: int,
    revision: int,
    version: str,
    source: str,
    required_major: int = COMPATIBILITY_MAJOR,
    minimum_revision: int = MINIMUM_COMPATIBILITY_REVISION,
) -> bool:
    return (major == required_major and major > 0 and revision >= minimum_revision) or (
        major == 0
        and revision == 0
        and required_major == 1
        and minimum_revision == 0
        and version == LEGACY_VERSION
        and source == LEGACY_REVISION
    )


def select_installation(
    candidates: tuple[BriosaInstallation, ...],
    options: BriosaServerSelection,
    target: str = SPATIAL_ANALYZER_TARGET,
    required_major: int = COMPATIBILITY_MAJOR,
    minimum_revision: int = MINIMUM_COMPATIBILITY_REVISION,
) -> tuple[BriosaInstallation | None, str | None]:
    eligible = [
        c
        for c in candidates
        if c.spatial_analyzer_target == target
        and c.runtime_identifier == "win-x64"
        and compatible(
            c.contract_major,
            c.contract_revision,
            c.version,
            c.source_revision,
            required_major,
            minimum_revision,
        )
        and (options.version is None or c.version == options.version)
        and (
            options.installation_id is None
            or c.installation_id == options.installation_id
        )
        and (
            options.executable_path is None
            or path_key(c.executable_path) == path_key(options.executable_path)
        )
        and c.scope in options.allowed_scopes
        and (options.allow_prerelease or "-" not in c.version.split("+", 1)[0])
        and c.version not in options.excluded_versions
        and (
            options.minimum_version is None
            or version_key(c.version) >= version_key(options.minimum_version)
        )
        and (
            options.maximum_version_exclusive is None
            or version_key(c.version) < version_key(options.maximum_version_exclusive)
        )
    ]
    if not eligible:
        return (
            None,
            "server-installation-incompatible"
            if candidates
            else "server-distribution-not-found",
        )
    eligible.sort(
        key=lambda c: (
            ("machine", "user", "portable").index(c.scope),
            path_key(c.executable_path).encode("utf-8"),
        )
    )
    eligible.sort(key=lambda c: version_key(c.version), reverse=True)
    selected = eligible[0]
    if any(
        version_key(c.version) == version_key(selected.version)
        and (
            c.manifest_sha256 != selected.manifest_sha256
            or c.source_revision != selected.source_revision
        )
        for c in eligible
    ):
        return None, "server-installation-ambiguous"
    return selected, None
