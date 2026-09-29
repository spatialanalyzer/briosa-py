from briosa._installation_policy import LEGACY_REVISION, LEGACY_VERSION, compatible


def test_contract_major_two_is_required_for_runtime_selection() -> None:
    assert not compatible(1, 0, "0.8.0", "source")
    assert compatible(2, 0, "0.9.0", "source")
    assert not compatible(3, 0, "1.0.0", "source")
    assert not compatible(0, 0, LEGACY_VERSION, LEGACY_REVISION)
