from uuid import UUID

from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.world_time_advance import WorldTimeAdvance


def request_narrative_assessment_for_time_threshold(
    question_id: UUID,
    intention: NarrativeIntention,
    time_advance: WorldTimeAdvance,
    reassessment_at_elapsed_minute: int,
) -> NarrativeIntensityAndPressureAssessmentQuestion | None:
    if not time_advance.reaches(reassessment_at_elapsed_minute):
        return None

    initial_context = (
        "World time advanced from fictional minute "
        f"{time_advance.previous_elapsed_minutes} to fictional minute "
        f"{time_advance.current_elapsed_minutes}, reaching the reassessment "
        f"threshold at fictional minute {reassessment_at_elapsed_minute} in "
        f"world revision {time_advance.world_revision}."
    )

    return NarrativeIntensityAndPressureAssessmentQuestion(
        id=question_id,
        intention_id=intention.id,
        trigger=EvaluationTriggerKind.TIME_THRESHOLD_REACHED,
        initial_context=initial_context,
    )
