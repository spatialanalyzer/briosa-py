from briosa._installation_policy import LEGACY_REVISION, LEGACY_VERSION, compatible
from briosa.protocol_identity import COMPATIBILITY_MAJOR, COMPATIBILITY_REVISION


def test_contract_major_three_is_required_for_runtime_selection() -> None:
    assert (COMPATIBILITY_MAJOR, COMPATIBILITY_REVISION) == (3, 0)
    assert not compatible(1, 0, "0.8.0", "source")
    assert not compatible(2, 0, "0.9.2", "source")
    assert compatible(3, 0, "0.10.0", "source")
    assert compatible(3, 1, "0.10.1", "source")
    assert not compatible(4, 0, "1.0.0", "source")
    assert not compatible(0, 0, LEGACY_VERSION, LEGACY_REVISION)
