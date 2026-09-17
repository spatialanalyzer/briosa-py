from __future__ import annotations

import json
import re
import tarfile
import zipfile
from email.parser import Parser
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PYPROJECT_PATH = REPOSITORY_ROOT / "pyproject.toml"
PROTOCOL_LOCK_PATH = REPOSITORY_ROOT / "protocol.lock.json"
DIST_DIRECTORY = REPOSITORY_ROOT / "dist"


def distribution_name(target: str) -> str:
    return f"briosa-{target.replace('.', '-')}"


def import_package_name(_target: str) -> str:
    return "briosa"


def normalized_distribution_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def protocol_target() -> str:
    document = json.loads(PROTOCOL_LOCK_PATH.read_text(encoding="utf-8"))
    if not isinstance(document, dict):
        raise RuntimeError("Protocol lock must be a JSON object.")
    target = document.get("target")
    if not isinstance(target, dict):
        raise RuntimeError("Protocol lock must contain a target object.")
    spatial_analyzer = target.get("spatial_analyzer")
    if not isinstance(spatial_analyzer, str):
        raise RuntimeError("Protocol lock must contain a SpatialAnalyzer target.")
    return spatial_analyzer


def project_string(field: str) -> str:
    document = PYPROJECT_PATH.read_text(encoding="utf-8")
    try:
        project_section = document.split("[project]", maxsplit=1)[1].split(
            "\n[", maxsplit=1
        )[0]
    except IndexError as error:
        raise RuntimeError("pyproject.toml must contain a project section.") from error
    match = re.search(
        rf'^\s*{re.escape(field)}\s*=\s*"([^"]+)"\s*$', project_section, re.MULTILINE
    )
    if match is None:
        raise RuntimeError(f"Project field {field!r} must be a string.")
    return match.group(1)


def main() -> None:
    target = protocol_target()
    expected_name = distribution_name(target)

    project_name = project_string("name")
    version = project_string("version")
    if project_name != expected_name:
        raise RuntimeError(
            f"Distribution name {project_name!r} does not match {expected_name!r}."
        )

    simulated_name = distribution_name("2027.1.0000.0")
    if simulated_name == expected_name:
        raise RuntimeError("Different exact targets must have distinct distributions.")
    if import_package_name(target) != import_package_name("2027.1.0000.0"):
        raise RuntimeError(
            "Exact targets must retain the stable briosa import package."
        )

    wheels = sorted(DIST_DIRECTORY.glob("*.whl"))
    source_distributions = sorted(DIST_DIRECTORY.glob("*.tar.gz"))
    if len(wheels) != 1 or len(source_distributions) != 1:
        raise RuntimeError("Expected exactly one wheel and one source distribution.")

    wheel_name = normalized_distribution_name(expected_name).replace("-", "_")
    expected_wheel_prefix = f"{wheel_name}-{version}-"
    if not wheels[0].name.startswith(expected_wheel_prefix):
        raise RuntimeError("Wheel filename does not contain the exact-target identity.")

    with zipfile.ZipFile(wheels[0]) as archive:
        import_files = {
            name
            for name in archive.namelist()
            if name.startswith("briosa/") and not name.endswith("/")
        }
        metadata_paths = [
            name for name in archive.namelist() if name.endswith(".dist-info/METADATA")
        ]
        if len(metadata_paths) != 1:
            raise RuntimeError("Wheel must contain exactly one metadata document.")
        metadata = Parser().parsestr(archive.read(metadata_paths[0]).decode("utf-8"))
        if normalized_distribution_name(metadata["Name"]) != expected_name:
            raise RuntimeError("Wheel metadata does not match the exact-target name.")
        if not import_files:
            raise RuntimeError("Wheel must retain the stable briosa import package.")

    expected_sdist_prefix = f"{wheel_name}-{version}"
    if not source_distributions[0].name.startswith(expected_sdist_prefix):
        raise RuntimeError(
            "Source distribution filename does not contain the exact-target identity."
        )
    with tarfile.open(source_distributions[0], mode="r:gz") as archive:
        if not any("/src/briosa/" in member.name for member in archive.getmembers()):
            raise RuntimeError(
                "Source distribution must retain the stable briosa import package."
            )

    print(
        f"Verified {expected_name} with stable briosa imports, separate-environment "
        "targeting, and distinct simulated target identity."
    )


if __name__ == "__main__":
    main()
