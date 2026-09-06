from datetime import UTC, datetime
from uuid import UUID

import pytest

from tessitura.application.apply_recorded_narrative_assessment import (
    apply_recorded_narrative_assessment,
)
from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intensity_and_pressure_assessment_record import (
    NarrativeIntensityAndPressureAssessmentRecord,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_applies_assessment_from_record_for_matching_intention() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(3),
            pressure=NarrativePressure(7),
            justification=NarratorJustification(
                "Borg seeks a swift retaliation for his injury."
            ),
        ),
    )
    record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=2),
        intention_id=UUID(int=1),
        evaluated_at=datetime(2026, 9, 5, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(8),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "Borg chooses a more devastating but patient revenge."
            ),
        ),
    )

    apply_recorded_narrative_assessment(intention, record)

    assert intention.current_assessment is record.assessment


def test_rejects_record_for_another_intention_without_replacing_assessment() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(7),
        justification=NarratorJustification(
            "Borg seeks a swift retaliation for his injury."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
    )
    record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=2),
        intention_id=UUID(int=3),
        evaluated_at=datetime(2026, 9, 5, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.KNOWLEDGE_CHANGED,
        assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(8),
            pressure=NarrativePressure(2),
            justification=NarratorJustification(
                "The city's corruption warrants a serious but gradual revelation."
            ),
        ),
    )

    with pytest.raises(ValueError, match="belongs to a different narrative intention"):
        apply_recorded_narrative_assessment(intention, record)

    assert intention.current_assessment is original_assessment


def test_successive_applications_preserve_previous_record_result() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )
    first_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(7),
        justification=NarratorJustification(
            "Borg seeks a swift retaliation for his injury."
        ),
    )
    first_record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=2),
        intention_id=UUID(int=1),
        evaluated_at=datetime(2026, 9, 5, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.TIME_THRESHOLD_REACHED,
        assessment=first_assessment,
    )
    second_record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=3),
        intention_id=UUID(int=1),
        evaluated_at=datetime(2026, 9, 6, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(8),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "Borg chooses a more devastating but patient revenge."
            ),
        ),
    )

    apply_recorded_narrative_assessment(intention, first_record)
    assert intention.current_assessment is first_record.assessment

    apply_recorded_narrative_assessment(intention, second_record)

    assert intention.current_assessment is second_record.assessment
    assert first_record.assessment is first_assessment
    assert first_record.assessment.intensity == NarrativeIntensity(3)
    assert first_record.assessment.pressure == NarrativePressure(7)
    assert first_record.assessment.justification == NarratorJustification(
        "Borg seeks a swift retaliation for his injury."
    )
