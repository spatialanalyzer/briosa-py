"""Install the built wheel in isolation and verify the short public import."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    wheels = list((root / "dist").glob("*.whl"))
    if len(wheels) != 1:
        raise RuntimeError("Build exactly one wheel before the consumer check.")
    lock = json.loads((root / "protocol.lock.json").read_text())
    target = str(lock["target"]["spatial_analyzer"])
    distribution = "briosa-" + target.replace(".", "-")
    with tempfile.TemporaryDirectory(prefix="briosa-py-consumer-") as directory:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--no-deps",
                "--no-index",
                "--target",
                directory,
                str(wheels[0]),
            ],
            check=True,
        )
        program = """
import asyncio
import sys
from pathlib import Path
from importlib.metadata import version
sys.path.insert(0, sys.argv[1])
import briosa
from briosa.protocol_identity import SPATIAL_ANALYZER_TARGET
assert Path(briosa.__file__).is_relative_to(Path(sys.argv[1]))
assert SPATIAL_ANALYZER_TARGET == sys.argv[2]
assert version(sys.argv[3]) == sys.argv[4]
asyncio.run(briosa.BriosaClient().aclose())
print('Verified import briosa from ' + sys.argv[3])
"""
        subprocess.run(
            [
                sys.executable,
                "-I",
                "-c",
                program,
                directory,
                target,
                distribution,
                wheels[0].name.split("-")[1],
            ],
            check=True,
            cwd=directory,
        )


if __name__ == "__main__":
    main()
