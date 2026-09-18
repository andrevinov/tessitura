from uuid import UUID

from tessitura.application.apply_answered_narrative_assessment_question import (
    apply_answered_narrative_assessment_question,
)
from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind
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
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_reassessment_can_make_narrative_intention_eligible() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(30),
        pressure=NarrativePressure(20),
        justification=NarratorJustification(
            "Borg wants revenge but has not committed resources yet."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(MinimumNarrativePressureCondition(),),
            weighted_conditions=(),
            minimum_score=0,
        ),
    )

    assert evaluate_narrative_intention_eligibility(intention) is False

    question = NarrativeIntensityAndPressureAssessmentQuestion(
        id=UUID(int=2),
        intention_id=intention.id,
        trigger=EvaluationTriggerKind.ANCHOR_STATE_CHANGED,
        prompt="How intense and urgent should Borg's revenge now be?",
        initial_context="The player injured Borg and escaped.",
    )
    reassessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg wants severe retaliation and has reason to act soon."
        ),
    )
    question.respond(reassessment)

    apply_answered_narrative_assessment_question(intention, question)

    assert intention.current_assessment is reassessment
    assert evaluate_narrative_intention_eligibility(intention) is True


def test_unsatisfied_mandatory_condition_blocks_narrative_intention() -> None:
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(80),
            pressure=NarrativePressure(60),
            justification=NarratorJustification(
                "Borg is ready to retaliate, but one required threshold is still unmet."
            ),
        ),
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(
                MinimumNarrativePressureCondition(NarrativePressure(70)),
            ),
            weighted_conditions=(
                (MinimumNarrativePressureCondition(NarrativePressure(50)), 10),
            ),
            minimum_score=10,
        ),
    )

    assert evaluate_narrative_intention_eligibility(intention) is False


def test_only_satisfied_weighted_conditions_contribute_to_eligibility() -> None:
    satisfied_condition = MinimumNarrativePressureCondition(NarrativePressure(50))
    unsatisfied_condition = MinimumNarrativePressureCondition(NarrativePressure(70))
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(80),
            pressure=NarrativePressure(60),
            justification=NarratorJustification(
                "Borg is under pressure, but the strongest eligibility signal is absent."
            ),
        ),
        eligibility_configuration=NarrativeEligibilityConfiguration(
            mandatory_conditions=(),
            weighted_conditions=(
                (satisfied_condition, 3),
                (unsatisfied_condition, 100),
            ),
            minimum_score=4,
        ),
    )

    assert satisfied_condition.is_satisfied_by(intention.pressure) is True
    assert unsatisfied_condition.is_satisfied_by(intention.pressure) is False
    assert evaluate_narrative_intention_eligibility(intention) is False


def test_repeated_eligibility_evaluation_is_deterministic_and_non_mutating() -> None:
    assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(80),
        pressure=NarrativePressure(60),
        justification=NarratorJustification(
            "Borg's current urgency is established for this evaluation."
        ),
    )
    configuration = NarrativeEligibilityConfiguration(
        mandatory_conditions=(MinimumNarrativePressureCondition(),),
        weighted_conditions=(),
        minimum_score=0,
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=assessment,
        eligibility_configuration=configuration,
    )

    first_result = evaluate_narrative_intention_eligibility(intention)
    second_result = evaluate_narrative_intention_eligibility(intention)

    assert first_result is True
    assert second_result == first_result
    assert intention.current_assessment is assessment
    assert intention.eligibility_configuration is configuration
