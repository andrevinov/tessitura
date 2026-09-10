from uuid import UUID

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
