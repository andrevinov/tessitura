import pytest

from tessitura.domain.evaluate_narrative_eligibility import (
    evaluate_narrative_eligibility,
)


@pytest.mark.parametrize("minimum_score", [0, 1])
def test_eligibility_rejects_absence_of_conditions(minimum_score: int) -> None:
    with pytest.raises(ValueError, match="requires at least one condition"):
        evaluate_narrative_eligibility(
            mandatory_conditions=(),
            weighted_conditions=(),
            minimum_score=minimum_score,
        )


@pytest.mark.parametrize(
    ("mandatory_conditions", "weighted_conditions", "minimum_score", "expected"),
    [
        ((True,), (), 0, True),
        ((False,), (), 0, False),
        ((), ((True, 5),), 5, True),
        ((), ((False, 5),), 5, False),
    ],
)
def test_eligibility_can_evaluate_a_single_category_of_conditions(
    mandatory_conditions: tuple[bool, ...],
    weighted_conditions: tuple[tuple[bool, int], ...],
    minimum_score: int,
    expected: bool,
) -> None:
    result = evaluate_narrative_eligibility(
        mandatory_conditions=mandatory_conditions,
        weighted_conditions=weighted_conditions,
        minimum_score=minimum_score,
    )

    assert result is expected


def test_unsatisfied_mandatory_condition_blocks_eligibility_despite_score() -> None:
    result = evaluate_narrative_eligibility(
        mandatory_conditions=(True, False),
        weighted_conditions=((True, 100),),
        minimum_score=5,
    )

    assert result is False


@pytest.mark.parametrize(
    ("minimum_score", "expected"),
    [(6, False), (5, True), (4, True)],
    ids=["below_threshold", "at_threshold", "above_threshold"],
)
def test_eligibility_counts_only_satisfied_weighted_conditions(
    minimum_score: int, expected: bool
) -> None:
    result = evaluate_narrative_eligibility(
        mandatory_conditions=(True, True),
        weighted_conditions=((True, 2), (False, 100), (True, 3)),
        minimum_score=minimum_score,
    )

    assert result is expected


@pytest.mark.parametrize("mandatory_satisfied", [True, False])
@pytest.mark.parametrize(
    ("weighted_conditions", "minimum_score", "error_message"),
    [
        (((True, -1),), 0, "condition weight cannot be negative"),
        (((False, -1),), 0, "condition weight cannot be negative"),
        (((True, 1),), -1, "Minimum eligibility score cannot be negative"),
    ],
    ids=[
        "negative_satisfied_weight",
        "negative_unsatisfied_weight",
        "negative_minimum",
    ],
)
def test_eligibility_rejects_negative_configuration_before_deciding(
    mandatory_satisfied: bool,
    weighted_conditions: tuple[tuple[bool, int], ...],
    minimum_score: int,
    error_message: str,
) -> None:
    with pytest.raises(ValueError, match=error_message):
        evaluate_narrative_eligibility(
            mandatory_conditions=(mandatory_satisfied,),
            weighted_conditions=weighted_conditions,
            minimum_score=minimum_score,
        )
