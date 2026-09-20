from uuid import UUID

from tessitura.application.evaluate_narrative_intention_eligibility import (
    evaluate_narrative_intention_eligibility,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)


def request_narrative_preparation_creation(
    question_id: UUID,
    intention: NarrativeIntention,
    initial_context: str,
) -> NarrativePreparationCreationQuestion:
    if not evaluate_narrative_intention_eligibility(intention):
        raise ValueError(
            "Narrative intention is not eligible to request preparation creation"
        )

    return NarrativePreparationCreationQuestion(
        id=question_id,
        intention_id=intention.id,
        initial_context=initial_context,
    )
