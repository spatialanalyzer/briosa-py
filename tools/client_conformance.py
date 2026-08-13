"""Emit the normalized public lifecycle contract implemented by this package."""

from __future__ import annotations

import json

from briosa.protocol_identity import (
    ARTIFACT_NAME,
    PROTOCOL_PACKAGE,
    SOURCE_REVISION,
    SPATIAL_ANALYZER_TARGET,
)


def main() -> int:
    report = {
        "schema_version": 2,
        "implementation": "python",
        "protocol": {
            "artifact": ARTIFACT_NAME,
            "source_revision": SOURCE_REVISION,
            "package": PROTOCOL_PACKAGE,
            "spatial_analyzer_target": SPATIAL_ANALYZER_TARGET,
        },
        "construction_is_dormant": True,
        "owns_local_server": True,
        "default_start": [
            "start_server",
            "start_spatial_analyzer_sdk",
            "launch_spatial_analyzer",
            "connect_to_spatial_analyzer",
            "verify_mp_readiness",
        ],
        "lifecycle_methods": [
            "get_spatial_analyzer_state",
            "launch_spatial_analyzer",
            "close_owned_spatial_analyzer",
            "get_spatial_analyzer_sdk_state",
            "start_spatial_analyzer_sdk",
            "connect_to_spatial_analyzer",
            "reconnect_to_spatial_analyzer",
            "stop_spatial_analyzer_sdk",
            "recover_spatial_analyzer_sdk",
        ],
        "stop_closes_spatial_analyzer": False,
        "automatic_mp_replay": False,
    }
    print(json.dumps(report, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
