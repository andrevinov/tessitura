from uuid import UUID

from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)
from tessitura.domain.narrator_justification import NarratorJustification


def test_narrative_preparation_creation_question_preserves_its_response() -> None:
    question = NarrativePreparationCreationQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        prompt="How should Borg's revenge take concrete form?",
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
