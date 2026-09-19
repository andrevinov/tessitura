from uuid import UUID

import pytest

from tessitura.application.apply_answered_narrative_assessment_question import (
    apply_answered_narrative_assessment_question,
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
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_applies_answered_assessment_question_to_matching_intention() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(30),
        pressure=NarrativePressure(20),
        justification=NarratorJustification(
            "Borg wants revenge but has not committed resources yet."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=2),
        intention_id=UUID(int=1),
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        initial_context="The player injured Borg and escaped.",
    )
    assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg wants severe retaliation and has reason to act soon."
        ),
    )
    question.respond(assessment)

    apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is assessment


def test_rejects_unanswered_assessment_question_without_changing_intention() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(30),
        pressure=NarrativePressure(20),
        justification=NarratorJustification(
            "Borg wants revenge but has not committed resources yet."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=2),
        intention_id=UUID(int=1),
        trigger=EvaluationTriggerKind.TIME_THRESHOLD_REACHED,
        initial_context="The configured time threshold was reached.",
    )

    with pytest.raises(ValueError, match="has not been answered"):
        apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is original_assessment


def test_rejects_assessment_question_for_another_intention() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(30),
        pressure=NarrativePressure(20),
        justification=NarratorJustification(
            "Borg wants revenge but has not committed resources yet."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=2),
        intention_id=UUID(int=3),
        trigger=EvaluationTriggerKind.KNOWLEDGE_CHANGED,
        initial_context="Relevant knowledge changed.",
    )
    question.respond(
        NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(80),
            pressure=NarrativePressure(60),
            justification=NarratorJustification(
                "The new information makes this intention more intense and urgent."
            ),
        ),
    )

    with pytest.raises(ValueError, match="belongs to a different narrative intention"):
        apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is original_assessment
