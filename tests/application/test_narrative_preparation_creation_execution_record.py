from dataclasses import FrozenInstanceError
from datetime import UTC, datetime
from uuid import UUID

import pytest

from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)
from tessitura.domain.narrative_archetype import NarrativeArchetype
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_preparation_creation_execution_record_cannot_be_changed_after_creation() -> (
    None
):
    record = NarrativePreparationCreationExecutionRecord(
        execution_id=UUID(int=1),
        narrative_engine_version="0.1.0",
        completed_at=datetime(2026, 9, 29, 12, tzinfo=UTC),
        duration_milliseconds=750,
        provider="openai",
        model="gpt-5.6-luna",
        instructions="Propose a preparation for the supplied Narrative Intention.",
        question_id=UUID(int=2),
        intention_id=UUID(int=3),
        initial_context="Borg has enough urgency to prepare a retaliation.",
        intention_archetype=NarrativeArchetype(
            name="The Tower",
            description="A presumed safety collapses abruptly.",
        ),
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(80),
            pressure=NarrativePressure(60),
            justification=NarratorJustification(
                "Borg wants severe retaliation and has reason to act soon."
            ),
        ),
        provider_response_id="response-1",
        raw_response=(
            '{"description":"Borg hires mercenaries",'
            '"justification":"An indirect retaliation realizes The Tower."}'
        ),
        proposed_description="Borg hires mercenaries",
        justification=NarratorJustification(
            "An indirect retaliation realizes The Tower."
        ),
        input_tokens=240,
        output_tokens=35,
    )

    field_name = "model"
    with pytest.raises(FrozenInstanceError):
        setattr(record, field_name, "gpt-5.6-terra")

    assert record.model == "gpt-5.6-luna"
