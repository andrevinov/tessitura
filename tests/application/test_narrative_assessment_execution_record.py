from dataclasses import FrozenInstanceError
from datetime import UTC, datetime
from uuid import UUID

import pytest

from tessitura.application.narrative_assessment_execution_record import (
    NarrativeAssessmentExecutionRecord,
)
from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_execution_record_cannot_be_changed_after_creation() -> None:
    record = NarrativeAssessmentExecutionRecord(
        execution_id=UUID(int=1),
        completed_at=datetime(2026, 9, 20, 12, tzinfo=UTC),
        duration_milliseconds=750,
        provider="openai",
        model="gpt-5.6-luna",
        instructions="Reassess the supplied Narrative Intention.",
        question_id=UUID(int=2),
        intention_id=UUID(int=3),
        trigger=EvaluationTriggerKind.TIME_THRESHOLD_REACHED,
        initial_context="World time advanced from minute 0 to minute 60.",
        intention_direction="Borg seeks revenge against the player character",
        previous_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(30),
            pressure=NarrativePressure(20),
            justification=NarratorJustification(
                "Borg wants revenge but has not committed resources yet."
            ),
        ),
        provider_response_id="response-1",
        raw_response=(
            '{"intensity":30,"pressure":20,'
            '"justification":"No new developments support a change."}'
        ),
        resulting_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(30),
            pressure=NarrativePressure(20),
            justification=NarratorJustification(
                "No new developments support a change."
            ),
        ),
        input_tokens=240,
        output_tokens=35,
    )

    field_name = "model"
    with pytest.raises(FrozenInstanceError):
        setattr(record, field_name, "gpt-5.6-terra")

    assert record.model == "gpt-5.6-luna"
