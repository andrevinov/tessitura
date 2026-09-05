from dataclasses import FrozenInstanceError
from datetime import UTC, datetime
from uuid import UUID

import pytest

from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intensity_and_pressure_assessment_record import (
    NarrativeIntensityAndPressureAssessmentRecord,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_assessment_record_preserves_occurrence_data_and_result() -> None:
    record_id = UUID(int=1)
    intention_id = UUID(int=2)
    evaluated_at = datetime(2026, 9, 5, 12, tzinfo=UTC)
    assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "A serious retaliation is warranted, but Borg needs time to prepare."
        ),
    )

    record = NarrativeIntensityAndPressureAssessmentRecord(
        id=record_id,
        intention_id=intention_id,
        evaluated_at=evaluated_at,
        trigger=EvaluationTriggerKind.TIME_THRESHOLD_REACHED,
        assessment=assessment,
    )

    assert record.id == record_id
    assert record.intention_id == intention_id
    assert record.evaluated_at == evaluated_at
    assert record.trigger is EvaluationTriggerKind.TIME_THRESHOLD_REACHED
    assert record.assessment is assessment


@pytest.mark.parametrize(
    ("field_name", "alternative_value"),
    [
        ("id", UUID(int=3)),
        ("intention_id", UUID(int=4)),
        ("evaluated_at", datetime(2026, 9, 6, 12, tzinfo=UTC)),
        ("trigger", EvaluationTriggerKind.TIME_THRESHOLD_REACHED),
        (
            "assessment",
            NarrativeIntensityAndPressureAssessment(
                intensity=NarrativeIntensity(8),
                pressure=NarrativePressure(1),
                justification=NarratorJustification(
                    "Borg chooses a more devastating but patient revenge."
                ),
            ),
        ),
    ],
)
def test_assessment_record_cannot_reassign_its_fields(
    field_name: str,
    alternative_value: UUID
    | datetime
    | EvaluationTriggerKind
    | NarrativeIntensityAndPressureAssessment,
) -> None:
    record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        evaluated_at=datetime(2026, 9, 5, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )
    original_value = getattr(record, field_name)
    assert alternative_value != original_value

    with pytest.raises(FrozenInstanceError):
        setattr(record, field_name, alternative_value)

    assert getattr(record, field_name) is original_value


def test_equal_assessments_can_belong_to_distinct_occurrences() -> None:
    first_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "A serious retaliation is warranted, but Borg needs time to prepare."
        ),
    )
    second_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "A serious retaliation is warranted, but Borg needs time to prepare."
        ),
    )
    first_record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=1),
        intention_id=UUID(int=3),
        evaluated_at=datetime(2026, 9, 5, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.INITIAL_EVALUATION,
        assessment=first_assessment,
    )
    second_record = NarrativeIntensityAndPressureAssessmentRecord(
        id=UUID(int=2),
        intention_id=UUID(int=3),
        evaluated_at=datetime(2026, 9, 6, 12, tzinfo=UTC),
        trigger=EvaluationTriggerKind.LEVEL_THRESHOLD_REACHED,
        assessment=second_assessment,
    )

    assert first_record.assessment == second_record.assessment
    assert first_record.intention_id == second_record.intention_id
    assert first_record.id != second_record.id
    assert first_record != second_record


def test_assessment_record_rejects_datetime_without_timezone() -> None:
    with pytest.raises(ValueError, match="must be timezone-aware"):
        NarrativeIntensityAndPressureAssessmentRecord(
            id=UUID(int=1),
            intention_id=UUID(int=2),
            evaluated_at=datetime(2026, 9, 5, 12),  # noqa: DTZ001 — invalid on purpose
            trigger=EvaluationTriggerKind.KNOWLEDGE_CHANGED,
            assessment=NarrativeIntensityAndPressureAssessment(
                intensity=NarrativeIntensity(2),
                pressure=NarrativePressure(3),
                justification=NarratorJustification(
                    "A serious retaliation is warranted, but Borg needs time to prepare."
                ),
            ),
        )
