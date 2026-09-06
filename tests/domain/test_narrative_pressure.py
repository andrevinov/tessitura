from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.narrative_pressure import NarrativePressure


def test_narrative_pressure_has_value_equality() -> None:
    assert NarrativePressure(1) == NarrativePressure(1)


def test_narrative_pressure_is_immutable() -> None:
    pressure = NarrativePressure(1)

    with pytest.raises(FrozenInstanceError):
        pressure.value = 2  # pyright: ignore[reportAttributeAccessIssue]


@pytest.mark.parametrize("value", [0, 100])
def test_narrative_pressure_accepts_range_boundaries(value: int) -> None:
    assert NarrativePressure(value).value == value


@pytest.mark.parametrize("value", [-1, 101])
def test_narrative_pressure_rejects_out_of_range_value(value: int) -> None:
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        NarrativePressure(value)
