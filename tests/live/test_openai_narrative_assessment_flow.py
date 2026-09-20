import json
import os
from pathlib import Path
from uuid import UUID

import pytest
from openai import OpenAI

from tessitura.application.answer_narrative_assessment_question_with_narrator import (
    answer_narrative_assessment_question_with_narrator,
)
from tessitura.application.apply_answered_narrative_assessment_question import (
    apply_answered_narrative_assessment_question,
)
from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.application.narrative_assessment_execution_recorder import (
    NarrativeAssessmentExecutionRecorder,
)
from tessitura.application.request_narrative_assessment_for_time_threshold import (
    request_narrative_assessment_for_time_threshold,
)
from tessitura.domain.minimum_narrative_pressure_condition import (
    MinimumNarrativePressureCondition,
)
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
from tessitura.domain.world_state import WorldState
from tessitura.infrastructure.json_lines_narrative_assessment_execution_recorder import (
    JsonLinesNarrativeAssessmentExecutionRecorder,
)
from tessitura.infrastructure.openai_narrative_assessment_narrator import (
    OpenAINarrativeAssessmentNarrator,
)

LIVE_OPENAI_ENABLED = (
    os.getenv("RUN_OPENAI_LIVE_TESTS") == "1"
    and "OPENAI_API_KEY" in os.environ
    and "TESSITURA_NARRATIVE_ASSESSMENT_LOG_PATH" in os.environ
)

pytestmark = pytest.mark.skipif(
    not LIVE_OPENAI_ENABLED,
    reason=(
        "Set OPENAI_API_KEY, RUN_OPENAI_LIVE_TESTS=1, and "
        "TESSITURA_NARRATIVE_ASSESSMENT_LOG_PATH to run the OpenAI live test"
    ),
)


def test_openai_reassesses_an_intention_after_world_time_reaches_threshold() -> None:
    previous_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(30),
        pressure=NarrativePressure(20),
        justification=NarratorJustification(
            "Borg wants revenge but has not committed resources yet."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge against the player character",
        current_assessment=previous_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )
    world = WorldState()
    time_advance = world.advance_time(minutes=60)
    question = request_narrative_assessment_for_time_threshold(
        question_id=UUID(int=2),
        intention=intention,
        time_advance=time_advance,
        reassessment_at_elapsed_minute=60,
    )

    assert question is not None
    assert question.answer is None

    narrator = OpenAINarrativeAssessmentNarrator(
        client=OpenAI(),
        narrative_engine_version="0.1.0",
    )
    execution_record = answer_narrative_assessment_question_with_narrator(
        intention=intention,
        question=question,
        narrator=narrator,
    )

    assessment = question.answer
    assert assessment is not None
    assert execution_record.narrative_engine_version == "0.1.0"
    assert execution_record.provider == "openai"
    assert execution_record.model
    assert execution_record.instructions
    assert execution_record.question_id == question.id
    assert execution_record.intention_id == intention.id
    assert execution_record.trigger is question.trigger
    assert execution_record.initial_context == question.initial_context
    assert execution_record.intention_direction == intention.direction
    assert execution_record.previous_assessment is previous_assessment
    assert execution_record.provider_response_id
    assert execution_record.raw_response
    assert execution_record.resulting_assessment is assessment
    assert execution_record.input_tokens >= 0
    assert execution_record.output_tokens >= 0
    assert execution_record.duration_milliseconds >= 0
    assert 1 <= assessment.intensity.value <= 100
    assert 0 <= assessment.pressure.value <= 100
    assert assessment.justification.text.strip()

    log_path = Path(os.environ["TESSITURA_NARRATIVE_ASSESSMENT_LOG_PATH"])
    recorder: NarrativeAssessmentExecutionRecorder = (
        JsonLinesNarrativeAssessmentExecutionRecorder(log_path)
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

    apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is assessment
    assert evaluate_narrative_intention_eligibility(intention) is (
        assessment.pressure.value >= 50
    )
