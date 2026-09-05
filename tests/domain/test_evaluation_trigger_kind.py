import pytest

from tessitura.domain.evaluation_trigger_kind import EvaluationTriggerKind


def test_evaluation_trigger_kind_rejects_unknown_category() -> None:
    with pytest.raises(ValueError):
        EvaluationTriggerKind("unknown_trigger")
