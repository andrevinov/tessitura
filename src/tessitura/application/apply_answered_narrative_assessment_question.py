from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention


def apply_answered_narrative_assessment_question(
    intention: NarrativeIntention,
    question: NarrativeIntensityAndPressureAssessmentQuestion,
) -> None:
    if question.intention_id != intention.id:
        raise ValueError(
            "Narrative question belongs to a different narrative intention"
        )

    assessment = question.answer
    if assessment is None:
        raise ValueError("Narrative assessment question has not been answered")

    intention.apply_assessment(assessment)
