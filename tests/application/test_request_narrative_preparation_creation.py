from uuid import UUID

import pytest

from tessitura.application.request_narrative_preparation_creation import (
    request_narrative_preparation_creation,
)
from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_eligibility_configuration import (
    NarrativeEligibilityConfiguration,
)
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_ineligible_intention_cannot_request_narrative_preparation_creation() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(30),
            pressure=NarrativePressure(20),
            justification=NarratorJustification(
                "Borg wants revenge but has not committed resources yet."
            ),
        ),
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(
                MinimumNarrativePressureCondition(minimum=NarrativePressure(50)),
            ),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )

    with pytest.raises(ValueError, match="not eligible"):
        request_narrative_preparation_creation(
            question_id=UUID(int=2),
            intention=intention,
            initial_context="Borg has not reached the required narrative pressure.",
        )


def test_eligible_intention_can_request_narrative_preparation_creation() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(80),
            pressure=NarrativePressure(60),
            justification=NarratorJustification(
                "Borg wants severe retaliation and has reason to act soon."
            ),
        ),
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(
                MinimumNarrativePressureCondition(minimum=NarrativePressure(50)),
            ),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question_id = UUID(int=2)
    initial_context = "Borg has enough urgency to prepare a retaliation."

    question = request_narrative_preparation_creation(
        question_id=question_id,
        intention=intention,
        initial_context=initial_context,
    )

    assert question.id == question_id
    assert question.intention_id == intention.id
    assert question.initial_context == initial_context
    assert question.answer is None
    assert question.justification is None
