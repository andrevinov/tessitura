from uuid import UUID

import pytest

from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_eligibility_configuration import (
    NarrativeEligibilityConfiguration,
)
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment_result import (
    NarrativeIntensityAndPressureAssessmentResult,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation import NarrativePreparation
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_narrative_preparation_preserves_its_intention() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    preparation = NarrativePreparation(
        id=UUID(int=2),
        intention=intention,
        description="Borg hires mercenaries",
        justification=NarratorJustification(
            "This form preserves Borg as the causal origin."
        ),
    )

    assert preparation.intention is intention


def test_narrative_preparation_cannot_change_its_intention() -> None:
    original_intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )
    preparation = NarrativePreparation(
        id=UUID(int=2),
        intention=original_intention,
        description="Borg hires mercenaries",
        justification=NarratorJustification(
            "This form preserves Borg as the causal origin."
        ),
    )
    another_intention = NarrativeIntention(
        id=UUID(int=3),
        direction="Reveal the corruption beneath the city",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(1),
            justification=NarratorJustification(
                "The city's corruption warrants a serious but gradual revelation."
            ),
        ),
    )

    with pytest.raises(AttributeError):
        preparation.intention = another_intention  # pyright: ignore[reportAttributeAccessIssue]

    assert preparation.intention.id == original_intention.id


def test_narrative_preparation_rejects_blank_description() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    with pytest.raises(ValueError, match="description cannot be blank"):
        NarrativePreparation(
            id=UUID(int=2),
            intention=intention,
            description="   ",
            justification=NarratorJustification(
                "This form preserves Borg as the causal origin."
            ),
        )


def test_narrative_preparation_cannot_change_its_id() -> None:
    original_id = UUID(int=2)
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )
    preparation = NarrativePreparation(
        id=original_id,
        intention=intention,
        description="Borg hires mercenaries",
        justification=NarratorJustification(
            "This form preserves Borg as the causal origin."
        ),
    )

    with pytest.raises(AttributeError):
        preparation.id = UUID(int=3)  # pyright: ignore[reportAttributeAccessIssue]

    assert preparation.id == original_id


def test_narrative_preparation_cannot_change_its_description_directly() -> None:
    original_description = "Borg hires mercenaries"
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
        current_assessment=NarrativeIntensityAndPressureAssessmentResult(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )
    preparation = NarrativePreparation(
        id=UUID(int=2),
        intention=intention,
        description=original_description,
        justification=NarratorJustification(
            "This form preserves Borg as the causal origin."
        ),
    )

    with pytest.raises(AttributeError):
        preparation.description = (  # pyright: ignore[reportAttributeAccessIssue]
            "Borg confronts the group personally"
        )

    assert preparation.description == original_description
