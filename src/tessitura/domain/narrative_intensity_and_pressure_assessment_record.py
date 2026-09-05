from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from .evaluation_trigger_kind import EvaluationTriggerKind
from .narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)


@dataclass(frozen=True, eq=False)
class NarrativeIntensityAndPressureAssessmentRecord:
    id: UUID
    intention_id: UUID
    evaluated_at: datetime
    trigger: EvaluationTriggerKind
    assessment: NarrativeIntensityAndPressureAssessment

    def __post_init__(self) -> None:
        if self.evaluated_at.utcoffset() is None:
            raise ValueError("Assessment evaluation datetime must be timezone-aware")
