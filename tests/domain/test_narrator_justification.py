import pytest

from tessitura.domain.narrator_justification import NarratorJustification


def test_narrator_justification_has_value_equality() -> None:
    text = "Borg's retaliation preserves the intention's causal origin."

    assert NarratorJustification(text) == NarratorJustification(text)


def test_narrator_justification_rejects_empty_text() -> None:
    with pytest.raises(ValueError, match="cannot be empty"):
        NarratorJustification("")
