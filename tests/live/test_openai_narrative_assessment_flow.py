import os
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
from tessitura.infrastructure.openai_narrative_assessment_narrator import (
    OpenAINarrativeAssessmentNarrator,
)

LIVE_OPENAI_ENABLED = (
    os.getenv("RUN_OPENAI_LIVE_TESTS") == "1" and "OPENAI_API_KEY" in os.environ
)

pytestmark = pytest.mark.skipif(
    not LIVE_OPENAI_ENABLED,
    reason=(
        "Set OPENAI_API_KEY and RUN_OPENAI_LIVE_TESTS=1 to run the OpenAI live test"
    ),
)


def test_openai_reassesses_an_intention_after_world_time_reaches_threshold() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge against the player character",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(30),
            pressure=NarrativePressure(20),
            justification=NarratorJustification(
                "Borg wants revenge but has not committed resources yet."
            ),
        ),
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

    narrator = OpenAINarrativeAssessmentNarrator(client=OpenAI())
    answer_narrative_assessment_question_with_narrator(
        intention=intention,
        question=question,
        narrator=narrator,
    )

    assessment = question.answer
    assert assessment is not None
    assert 1 <= assessment.intensity.value <= 100
    assert 0 <= assessment.pressure.value <= 100
    assert assessment.justification.text.strip()

    apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is assessment
    assert evaluate_narrative_intention_eligibility(intention) is (
        assessment.pressure.value >= 50
    )
