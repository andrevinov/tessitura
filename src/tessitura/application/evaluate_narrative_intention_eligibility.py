from tessitura.domain.evaluate_narrative_eligibility import (
    evaluate_narrative_eligibility,
)
from tessitura.domain.narrative_intention import NarrativeIntention


def evaluate_narrative_intention_eligibility(
    intention: NarrativeIntention,
) -> bool:
    configuration = intention.eligibility_configuration
    pressure = intention.pressure

    mandatory_results = tuple(
        condition.is_satisfied_by(pressure)
        for condition in configuration.mandatory_conditions
    )
    weighted_results = tuple(
        (condition.is_satisfied_by(pressure), weight)
        for condition, weight in configuration.weighted_conditions
    )

    return evaluate_narrative_eligibility(
        mandatory_conditions=mandatory_results,
        weighted_conditions=weighted_results,
        minimum_score=configuration.minimum_score,
    )
