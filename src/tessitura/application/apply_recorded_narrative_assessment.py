from tessitura.domain.narrative_intensity_and_pressure_assessment_record import (
    NarrativeIntensityAndPressureAssessmentRecord,
)
from tessitura.domain.narrative_intention import NarrativeIntention


def apply_recorded_narrative_assessment(
    intention: NarrativeIntention,
    record: NarrativeIntensityAndPressureAssessmentRecord,
) -> None:
    if record.intention_id != intention.id:
        raise ValueError("Assessment record belongs to a different narrative intention")

    intention.apply_assessment(record.assessment)
