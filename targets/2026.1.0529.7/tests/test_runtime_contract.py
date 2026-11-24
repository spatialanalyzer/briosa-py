from briosa._installation_policy import (
    LEGACY_REVISION,
    LEGACY_VERSION,
    MINIMUM_COMPATIBILITY_REVISION,
    compatible,
)
from briosa.protocol_identity import COMPATIBILITY_MAJOR, COMPATIBILITY_REVISION


def test_contract_major_three_is_required_for_runtime_selection() -> None:
    assert COMPATIBILITY_MAJOR == 3
    assert not compatible(1, 0, "0.8.0", "source")
    assert not compatible(2, 0, "0.9.2", "source")
    assert compatible(3, 0, "0.10.0", "source")
    assert compatible(3, 1, "0.10.1", "source")
    assert compatible(3, 7, "0.10.9", "source")
    assert not compatible(4, 0, "1.0.0", "source")
    assert not compatible(0, 0, LEGACY_VERSION, LEGACY_REVISION)


def test_the_pinned_protocol_is_revision_one_but_revision_zero_stays_accepted() -> None:
    # The importer records the pinned protocol's own revision (Server 0.10.1).
    # The client's minimum stays 0 so that it keeps working with Server 0.10.0.
    assert COMPATIBILITY_REVISION == 1
    assert MINIMUM_COMPATIBILITY_REVISION == 0
    assert compatible(3, 0, "0.10.0", "source")
