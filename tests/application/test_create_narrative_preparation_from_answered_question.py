from uuid import UUID

import pytest

from tessitura.application.apply_answered_narrative_assessment_question import (
    apply_answered_narrative_assessment_question,
)
from tessitura.application.create_narrative_preparation_from_answered_question import (
    create_narrative_preparation_from_answered_question,
)
from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
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
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_ineligible_intention_cannot_produce_narrative_preparation() -> None:
    minimum_pressure = MinimumNarrativePressureCondition(minimum=NarrativePressure(50))
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
            mandatory_conditions=(minimum_pressure,),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question = NarrativePreparationCreationQuestion(
        id=UUID(int=2),
        intention_id=intention.id,
        prompt="How should Borg's revenge take concrete form?",
        initial_context="Borg has not reached the required narrative pressure.",
    )
    question.respond(
        answer="Borg hires mercenaries",
        justification=NarratorJustification(
            "An indirect retaliation would suit Borg's current resources."
        ),
    )

    with pytest.raises(ValueError, match="not eligible"):
        create_narrative_preparation_from_answered_question(
            preparation_id=UUID(int=3),
            intention=intention,
            question=question,
        )


def test_reassessment_allows_narrative_preparation_creation() -> None:
    minimum_pressure = MinimumNarrativePressureCondition(minimum=NarrativePressure(50))
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
            mandatory_conditions=(minimum_pressure,),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )

    assert evaluate_narrative_intention_eligibility(intention) is False

    assessment_question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=2),
        intention_id=intention.id,
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        prompt="How intense and urgent should Borg's revenge now be?",
        initial_context="The player injured Borg and escaped.",
    )
    reassessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg wants severe retaliation and has reason to act soon."
        ),
    )
    assessment_question.respond(reassessment)
    apply_answered_narrative_assessment_question(intention, assessment_question)

    assert evaluate_narrative_intention_eligibility(intention) is True

    preparation_question = NarrativePreparationCreationQuestion(
        id=UUID(int=3),
        intention_id=intention.id,
        prompt="How should Borg's revenge take concrete form?",
        initial_context="Borg now has enough urgency to prepare a retaliation.",
    )
    preparation_justification = NarratorJustification(
        "An indirect retaliation matches Borg's resources and intended intensity."
    )
    preparation_question.respond(
        answer="Borg hires mercenaries",
        justification=preparation_justification,
    )

    preparation = create_narrative_preparation_from_answered_question(
        preparation_id=UUID(int=4),
        intention=intention,
        question=preparation_question,
    )

    assert preparation.id == UUID(int=4)
    assert preparation.intention is intention
    assert preparation.description == "Borg hires mercenaries"
    assert preparation.justification is preparation_justification
