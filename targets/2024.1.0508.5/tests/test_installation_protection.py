from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

import briosa


@pytest.mark.skipif(sys.platform != "win32", reason="Windows ACL semantics")
@pytest.mark.parametrize(
    ("sddl", "include_write", "expected"),
    [
        ("O:SYG:SY", True, False),
        ("O:SYG:SYD:(A;;FA;;;SY)(A;;FA;;;BA)", True, True),
        ("O:SYG:SYD:(A;;FA;;;SY)(A;;FW;;;BU)", False, True),
        ("O:SYG:SYD:(A;;FA;;;SY)(A;;FW;;;BU)", True, False),
        ("O:SYG:SYD:(A;;FA;;;SY)(A;;0x40;;;BU)", False, False),
        ("O:SYG:SYD:(A;;GA;;;BU)", False, False),
        ("O:SYG:SYD:(A;CIIO;GA;;;BU)", True, True),
        (
            "O:S-1-5-80-956008885-3418522649-1831038044-1853292631-2271478464G:SYD:(A;;FA;;;SY)",
            True,
            True,
        ),
        ("O:BUG:SYD:(A;;FA;;;SY)", True, False),
    ],
)
def test_native_acl_policy(sddl: str, include_write: bool, expected: bool) -> None:
    resource = Path(briosa.__file__).parent / "_protected_installation.ps1"
    executable = (
        Path(os.environ["SYSTEMROOT"])
        / "System32/WindowsPowerShell/v1.0/powershell.exe"
    )
    result = subprocess.run(
        [
            str(executable),
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(resource),
            "-CheckAcl",
        ],
        input=json.dumps({"sddl": sddl, "includeWrite": include_write}),
        text=True,
        capture_output=True,
        check=True,
        timeout=30,
    )
    assert result.stdout.strip() == str(expected).lower()
