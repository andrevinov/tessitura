from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from tessitura.domain.narrative_archetype import NarrativeArchetype
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrator_justification import NarratorJustification


@dataclass(frozen=True)
class NarrativePreparationCreationExecutionRecord:
    execution_id: UUID
    narrative_engine_version: str
    completed_at: datetime
    duration_milliseconds: int
    provider: str
    model: str
    instructions: str
    question_id: UUID
    intention_id: UUID
    initial_context: str
    intention_archetype: NarrativeArchetype
    current_assessment: NarrativeIntensityAndPressureAssessment
    provider_response_id: str
    raw_response: str
    proposed_description: str
    justification: NarratorJustification
    input_tokens: int
    output_tokens: int
