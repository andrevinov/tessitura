from collections.abc import Sequence


def evaluate_narrative_eligibility(
    mandatory_conditions: Sequence[bool],
    weighted_conditions: Sequence[tuple[bool, int]],
    minimum_score: int,
) -> bool:
    if minimum_score < 0:
        raise ValueError("Minimum eligibility score cannot be negative")
    if not mandatory_conditions and not weighted_conditions:
        raise ValueError("Narrative eligibility requires at least one condition")

    score = 0
    for is_satisfied, weight in weighted_conditions:
        if weight < 0:
            raise ValueError("Eligibility condition weight cannot be negative")
        if is_satisfied:
            score += weight

    return all(mandatory_conditions) and score >= minimum_score
