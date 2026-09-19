from uuid import UUID

import pytest

from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)
from tessitura.domain.narrator_justification import NarratorJustification


def test_narrative_preparation_creation_question_preserves_its_response() -> None:
    question = NarrativePreparationCreationQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        initial_context="Borg has enough urgency to prepare a retaliation.",
    )
    justification = NarratorJustification(
        "An indirect retaliation matches Borg's resources and intended intensity."
    )

    question.respond(
        answer="Borg hires mercenaries",
        justification=justification,
    )

    assert question.answer == "Borg hires mercenaries"
    assert question.justification is justification


def test_narrative_preparation_creation_question_rejects_second_response() -> None:
    question = NarrativePreparationCreationQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        initial_context="Borg has enough urgency to prepare a retaliation.",
    )
    original_justification = NarratorJustification(
        "An indirect retaliation matches Borg's resources and intended intensity."
    )
    question.respond(
        answer="Borg hires mercenaries",
        justification=original_justification,
    )

    with pytest.raises(ValueError, match="has already been answered"):
        question.respond(
            answer="Borg attacks the player personally",
            justification=NarratorJustification(
                "A direct attack would express Borg's anger more forcefully."
            ),
        )

    assert question.answer == "Borg hires mercenaries"
    assert question.justification is original_justification
