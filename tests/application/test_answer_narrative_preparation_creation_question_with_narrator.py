from datetime import UTC, datetime
from uuid import UUID

from tessitura.application.answer_narrative_preparation_creation_question_with_narrator import (
    answer_narrative_preparation_creation_question_with_narrator,
)
from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)
from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
from tessitura.domain.narrative_archetype import NarrativeArchetype
from tessitura.domain.narrative_eligibility_configuration import (
    NarrativeEligibilityConfiguration,
)
from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


class StubNarrativePreparationCreationNarrator:
    def __init__(
        self,
        execution_record: NarrativePreparationCreationExecutionRecord,
    ) -> None:
        self._execution_record = execution_record
        self.received_question: NarrativePreparationCreationQuestion | None = None
        self.received_intention: NarrativeIntention | None = None

    def propose(
        self,
        question: NarrativePreparationCreationQuestion,
        intention: NarrativeIntention,
    ) -> NarrativePreparationCreationExecutionRecord:
        self.received_question = question
        self.received_intention = intention
        return self._execution_record


def test_narrator_proposal_answers_preparation_creation_question() -> None:
    assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg wants severe retaliation and has reason to act soon."
        ),
    )
    archetype = NarrativeArchetype(
        name="The Tower",
        description="A presumed safety collapses abruptly.",
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        archetype=archetype,
        current_assessment=assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    question = NarrativePreparationCreationQuestion(
        id=UUID(int=2),
        intention_id=intention.id,
        initial_context="Borg has enough urgency to prepare a retaliation.",
    )
    justification = NarratorJustification(
        "An indirect retaliation realizes The Tower at the intended intensity."
    )
    expected_record = NarrativePreparationCreationExecutionRecord(
        execution_id=UUID(int=3),
        narrative_engine_version="0.1.0",
        completed_at=datetime(2026, 9, 29, 12, tzinfo=UTC),
        duration_milliseconds=750,
        provider="openai",
        model="gpt-5.6-luna",
        instructions="Propose a preparation for the supplied Narrative Intention.",
        question_id=question.id,
        intention_id=intention.id,
        initial_context=question.initial_context,
        intention_archetype=archetype,
        current_assessment=assessment,
        provider_response_id="response-1",
        raw_response=(
            '{"description":"Borg hires mercenaries",'
            '"justification":"An indirect retaliation realizes The Tower at '
            'the intended intensity."}'
        ),
        proposed_description="Borg hires mercenaries",
        justification=justification,
        input_tokens=240,
        output_tokens=35,
    )
    narrator = StubNarrativePreparationCreationNarrator(expected_record)

    execution_record = answer_narrative_preparation_creation_question_with_narrator(
        intention=intention,
        question=question,
        narrator=narrator,
    )

    assert narrator.received_question is question
    assert narrator.received_intention is intention
    assert execution_record is expected_record
    assert question.answer == expected_record.proposed_description
    assert question.justification is expected_record.justification
    assert intention.current_assessment is assessment
