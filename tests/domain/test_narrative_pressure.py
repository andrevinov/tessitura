from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.narrative_pressure import NarrativePressure


def test_narrative_pressure_has_value_equality() -> None:
    assert NarrativePressure(1) == NarrativePressure(1)


def test_narrative_pressure_is_immutable() -> None:
    pressure = NarrativePressure(1)

    with pytest.raises(FrozenInstanceError):
        pressure.value = 2  # pyright: ignore[reportAttributeAccessIssue]
