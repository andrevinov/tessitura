from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)


@dataclass(frozen=True)
class NarrativeAssessmentExecutionRecord:
    execution_id: UUID
    narrative_engine_version: str
    completed_at: datetime
    duration_milliseconds: int
    provider: str
    model: str
    instructions: str
    question_id: UUID
    intention_id: UUID
    trigger: EvaluationTriggerKind
    initial_context: str
    intention_direction: str
    previous_assessment: NarrativeIntensityAndPressureAssessment
    provider_response_id: str
    raw_response: str
    resulting_assessment: NarrativeIntensityAndPressureAssessment
    input_tokens: int
    output_tokens: int
