import pytest

from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_eligibility_configuration import (
    NarrativeEligibilityConfiguration,
)


@pytest.mark.parametrize(
    ("mandatory_conditions", "weighted_conditions", "minimum_score", "error_message"),
    [
        ((), (), 0, "requires at least one condition"),
        ((), (), 1, "requires at least one condition"),
        (
            (MinimumNarrativePressureCondition(),),
            (),
            -1,
            "Minimum eligibility score cannot be negative",
        ),
        (
            (),
            ((MinimumNarrativePressureCondition(), -1),),
            0,
            "condition weight cannot be negative",
        ),
        (
            (MinimumNarrativePressureCondition(),),
            ((MinimumNarrativePressureCondition(), -1),),
            0,
            "condition weight cannot be negative",
        ),
    ],
)
def test_eligibility_configuration_rejects_invalid_configuration(
    mandatory_conditions: tuple[MinimumNarrativePressureCondition, ...],
    weighted_conditions: tuple[tuple[MinimumNarrativePressureCondition, int], ...],
    minimum_score: int,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        NarrativeEligibilityConfiguration(
            mandatory_conditions=mandatory_conditions,
            weighted_conditions=weighted_conditions,
            minimum_score=minimum_score,
        )
