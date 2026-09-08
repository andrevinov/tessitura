from uuid import UUID

import pytest

from tessitura.domain.binary_narrative_question import BinaryNarrativeQuestion
from tessitura.domain.narrator_justification import NarratorJustification


@pytest.mark.parametrize(
    ("answer", "justification_text"),
    [
        (True, "The ritual's consequences still constrain Borg's revenge."),
        (False, "The prevented ritual no longer supports this condition."),
    ],
)
def test_binary_question_keeps_answer_and_justification(
    answer: bool, justification_text: str
) -> None:
    question_id = UUID(int=1)
    intention_id = UUID(int=2)
    prompt = "Is the condition tied to Borg's ritual still relevant?"
    initial_context = "The player prevented Borg's ritual."
    question = BinaryNarrativeQuestion(
        id=question_id,
        intention_id=intention_id,
        prompt=prompt,
        initial_context=initial_context,
    )
    justification = NarratorJustification(justification_text)

    assert question.answer is None
    assert question.justification is None

    question.respond(answer, justification)

    assert question.answer is answer
    assert question.justification is justification
    assert question.id == question_id
    assert question.intention_id == intention_id
    assert question.prompt == prompt
    assert question.initial_context == initial_context


@pytest.mark.parametrize(
    ("original_answer", "original_justification_text"),
    [
        (True, "The ritual's consequences still constrain Borg's revenge."),
        (False, "The prevented ritual no longer supports this condition."),
    ],
)
def test_binary_question_rejects_second_answer_and_preserves_first(
    original_answer: bool, original_justification_text: str
) -> None:
    question = BinaryNarrativeQuestion(
        id=UUID(int=1),
        intention_id=UUID(int=2),
        prompt="Is the condition tied to Borg's ritual still relevant?",
        initial_context="The player prevented Borg's ritual.",
    )
    original_justification = NarratorJustification(original_justification_text)
    question.respond(original_answer, original_justification)
    alternative_justification = NarratorJustification(
        "A new interpretation leads to a different decision."
    )

    with pytest.raises(ValueError, match="has already been answered"):
        question.respond(not original_answer, alternative_justification)

    assert question.answer is original_answer
    assert question.justification is original_justification
