import pytest

from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_pressure import NarrativePressure


def test_pressure_condition_preserves_default_and_custom_minimum() -> None:
    default_condition = MinimumNarrativePressureCondition()
    custom_minimum = NarrativePressure(70)
    custom_condition = MinimumNarrativePressureCondition(minimum=custom_minimum)

    assert default_condition.minimum == NarrativePressure(50)
    assert custom_condition.minimum is custom_minimum


@pytest.mark.parametrize(
    ("minimum", "pressure", "expected"),
    [
        (50, 49, False),
        (50, 50, True),
        (50, 51, True),
        (70, 69, False),
        (70, 70, True),
        (70, 71, True),
    ],
)
def test_pressure_condition_uses_inclusive_configured_minimum(
    minimum: int, pressure: int, expected: bool
) -> None:
    condition = MinimumNarrativePressureCondition(minimum=NarrativePressure(minimum))

    result = condition.is_satisfied_by(NarrativePressure(pressure))

    assert result is expected
