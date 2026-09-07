from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_eligibility_configuration import (
    NarrativeEligibilityConfiguration,
)
from tessitura.domain.narrative_pressure import NarrativePressure


@pytest.mark.parametrize(
    ("field_name", "alternative_value"),
    [
        (
            "mandatory_conditions",
            (MinimumNarrativePressureCondition(minimum=NarrativePressure(80)),),
        ),
        (
            "weighted_conditions",
            ((MinimumNarrativePressureCondition(minimum=NarrativePressure(30)), 2),),
        ),
        ("minimum_score", 2),
    ],
)
def test_eligibility_configuration_cannot_reassign_its_fields(
    field_name: str,
    alternative_value: tuple[MinimumNarrativePressureCondition, ...]
    | tuple[tuple[MinimumNarrativePressureCondition, int], ...]
    | int,
) -> None:
    configuration = NarrativeEligibilityConfiguration(
        mandatory_conditions=(MinimumNarrativePressureCondition(),),
        weighted_conditions=(
            (MinimumNarrativePressureCondition(minimum=NarrativePressure(70)), 5),
        ),
        minimum_score=5,
    )
    original_value = getattr(configuration, field_name)
    assert alternative_value != original_value

    with pytest.raises(FrozenInstanceError):
        setattr(configuration, field_name, alternative_value)

    assert getattr(configuration, field_name) is original_value


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
