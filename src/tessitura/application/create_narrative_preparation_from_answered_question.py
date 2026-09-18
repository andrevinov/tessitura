from uuid import UUID

from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation import NarrativePreparation
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)


def create_narrative_preparation_from_answered_question(
    preparation_id: UUID,
    intention: NarrativeIntention,
    question: NarrativePreparationCreationQuestion,
) -> NarrativePreparation:
    if question.intention_id != intention.id:
        raise ValueError(
            "Narrative question belongs to a different narrative intention"
        )

    answer = question.answer
    justification = question.justification
    if answer is None or justification is None:
        raise ValueError(
            "Narrative preparation creation question has not been answered"
        )

    if not evaluate_narrative_intention_eligibility(intention):
        raise ValueError("Narrative intention is not eligible to produce a preparation")

    return NarrativePreparation(
        id=preparation_id,
        intention=intention,
        description=answer,
        justification=justification,
    )
