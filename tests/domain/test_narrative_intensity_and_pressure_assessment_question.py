from uuid import UUID

import pytest

from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_assessment_question_keeps_answer_and_justification() -> None:
    question_id = UUID(int=1)
    intention_id = UUID(int=2)
    prompt = "How intense and urgent should Borg's revenge be?"
    initial_context = "The player injured Borg and escaped."
    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=question_id,
        intention_id=intention_id,
        trigger=EvaluationTriggerKind.INITIAL_EVALUATION,
        prompt=prompt,
        initial_context=initial_context,
    )
    intensity = NarrativeIntensity(80)
    pressure = NarrativePressure(60)
    justification = NarratorJustification(
        "Borg wants severe retaliation and has reason to act soon."
    )

    assert question.intensity is None
    assert question.pressure is None
    assert question.justification is None

    question.respond(intensity, pressure, justification)

    assert question.intensity is intensity
    assert question.pressure is pressure
    assert question.justification is justification
    assert question.id == question_id
    assert question.intention_id == intention_id
    assert question.prompt == prompt
    assert question.initial_context == initial_context


def test_assessment_question_rejects_second_answer_and_preserves_first() -> None:
    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        prompt="How intense and urgent should Borg's revenge be?",
        initial_context="The player injured Borg and escaped.",
    )
    original_intensity = NarrativeIntensity(80)
    original_pressure = NarrativePressure(60)
    original_justification = NarratorJustification(
        "Borg wants severe retaliation and has reason to act soon."
    )
    question.respond(
        original_intensity,
        original_pressure,
        original_justification,
    )

    with pytest.raises(ValueError, match="has already been answered"):
        question.respond(
            NarrativeIntensity(30),
            NarrativePressure(20),
            NarratorJustification(
                "Borg has reconsidered both the severity and urgency of his revenge."
            ),
        )

    assert question.intensity is original_intensity
    assert question.pressure is original_pressure
    assert question.justification is original_justification


def test_assessment_question_preserves_its_trigger() -> None:
    trigger = EvaluationTriggerKind.TIME_THRESHOLD_REACHED

    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        trigger=trigger,
        prompt="How should Borg's revenge be reassessed?",
        initial_context="The time threshold for reassessment was reached.",
    )

    assert question.trigger is trigger
