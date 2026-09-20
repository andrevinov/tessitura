from tessitura.application.narrative_assessment_execution_record import (
    NarrativeAssessmentExecutionRecord,
)
from tessitura.application.narrative_assessment_narrator import (
    NarrativeAssessmentNarrator,
)
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention


def answer_narrative_assessment_question_with_narrator(
    intention: NarrativeIntention,
    question: NarrativeIntensityAndPressureAssessmentQuestion,
    narrator: NarrativeAssessmentNarrator,
) -> NarrativeAssessmentExecutionRecord:
    if question.intention_id != intention.id:
        raise ValueError(
            "Narrative question belongs to a different narrative intention"
        )

    execution_record = narrator.assess(question, intention)
    question.respond(execution_record.resulting_assessment)
    return execution_record
