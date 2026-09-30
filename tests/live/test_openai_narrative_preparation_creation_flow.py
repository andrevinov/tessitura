import json
import os
from pathlib import Path
from uuid import UUID

import pytest
from openai import OpenAI

from tessitura.application.answer_narrative_preparation_creation_question_with_narrator import (
    answer_narrative_preparation_creation_question_with_narrator,
)
from tessitura.application.create_narrative_preparation_from_answered_question import (
    create_narrative_preparation_from_answered_question,
)
from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.application.narrative_preparation_creation_execution_recorder import (
    NarrativePreparationCreationExecutionRecorder,
)
from tessitura.application.narrative_preparation_creation_narrator import (
    NarrativePreparationCreationNarrator,
)
from tessitura.application.request_narrative_preparation_creation import (
    request_narrative_preparation_creation,
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
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification
from tessitura.infrastructure.json_lines_narrative_preparation_creation_execution_recorder import (
    JsonLinesNarrativePreparationCreationExecutionRecorder,
)
from tessitura.infrastructure.openai_narrative_preparation_creation_narrator import (
    OpenAINarrativePreparationCreationNarrator,
)

LIVE_OPENAI_ENABLED = (
    os.getenv("RUN_OPENAI_LIVE_TESTS") == "1"
    and "OPENAI_API_KEY" in os.environ
    and "TESSITURA_NARRATIVE_PREPARATION_CREATION_LOG_PATH" in os.environ
)

pytestmark = pytest.mark.skipif(
    not LIVE_OPENAI_ENABLED,
    reason=(
        "Set OPENAI_API_KEY, RUN_OPENAI_LIVE_TESTS=1, and "
        "TESSITURA_NARRATIVE_PREPARATION_CREATION_LOG_PATH to run the OpenAI "
        "narrative preparation creation live test"
    ),
)


def test_openai_narrator_creates_preparation_for_eligible_intention() -> None:
    current_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg wants severe retaliation and has reason to act soon."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        archetype=NarrativeArchetype(
            name="The Tower",
            description="A presumed safety collapses abruptly.",
        ),
        current_assessment=current_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )

    assert evaluate_narrative_intention_eligibility(intention) is True

    question = request_narrative_preparation_creation(
        question_id=UUID(int=2),
        intention=intention,
        initial_context=(
            "Borg is a proud orc war chief who considers humans inferior. The "
            "player character destroyed one of Borg's eyes and escaped. Borg "
            "has learned that the player character must travel through a road "
            "controlled by his scouts, but no retaliation has happened yet."
        ),
    )

    assert question.answer is None
    assert question.justification is None

    narrator: NarrativePreparationCreationNarrator = (
        OpenAINarrativePreparationCreationNarrator(
            client=OpenAI(),
            narrative_engine_version="0.1.0",
        )
    )
    execution_record = answer_narrative_preparation_creation_question_with_narrator(
        intention=intention,
        question=question,
        narrator=narrator,
    )

    assert execution_record.narrative_engine_version == "0.1.0"
    assert execution_record.provider == "openai"
    assert execution_record.model
    assert execution_record.instructions
    assert execution_record.question_id == question.id
    assert execution_record.intention_id == intention.id
    assert execution_record.initial_context == question.initial_context
    assert execution_record.intention_archetype is intention.archetype
    assert execution_record.current_assessment is current_assessment
    assert execution_record.provider_response_id
    assert execution_record.raw_response
    assert execution_record.proposed_description.strip()
    assert execution_record.justification.text.strip()
    assert execution_record.input_tokens >= 0
    assert execution_record.output_tokens >= 0
    assert execution_record.duration_milliseconds >= 0
    assert question.answer == execution_record.proposed_description
    assert question.justification is execution_record.justification

    log_path = Path(os.environ["TESSITURA_NARRATIVE_PREPARATION_CREATION_LOG_PATH"])
    recorder: NarrativePreparationCreationExecutionRecorder = (
        JsonLinesNarrativePreparationCreationExecutionRecorder(log_path)
    )
    recorder.record(execution_record)
    persisted_execution = json.loads(
        log_path.read_text(encoding="utf-8").splitlines()[-1]
    )

    assert persisted_execution["record_schema_version"] == 1
    assert persisted_execution["execution_id"] == str(execution_record.execution_id)
    assert persisted_execution["narrative_engine_version"] == "0.1.0"
    assert persisted_execution["provider_response_id"] == (
        execution_record.provider_response_id
    )
    assert persisted_execution["intention_archetype"] == {
        "name": intention.archetype.name,
        "description": intention.archetype.description,
    }
    assert persisted_execution["proposed_description"] == (
        execution_record.proposed_description
    )
    assert persisted_execution["justification"] == (execution_record.justification.text)

    preparation = create_narrative_preparation_from_answered_question(
        preparation_id=UUID(int=3),
        intention=intention,
        question=question,
    )

    assert preparation.id == UUID(int=3)
    assert preparation.intention is intention
    assert preparation.description == execution_record.proposed_description
    assert preparation.justification is execution_record.justification

    print(
        json.dumps(
            {
                "narrative_preparation_creation": {
                    "execution_id": str(execution_record.execution_id),
                    "preparation_id": str(preparation.id),
                    "description": preparation.description,
                    "justification": preparation.justification.text,
                }
            },
            ensure_ascii=False,
        )
    )
