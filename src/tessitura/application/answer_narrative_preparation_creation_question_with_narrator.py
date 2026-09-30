from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)
from tessitura.application.narrative_preparation_creation_narrator import (
    NarrativePreparationCreationNarrator,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)


def answer_narrative_preparation_creation_question_with_narrator(
    intention: NarrativeIntention,
    question: NarrativePreparationCreationQuestion,
    narrator: NarrativePreparationCreationNarrator,
) -> NarrativePreparationCreationExecutionRecord:
    if question.intention_id != intention.id:
        raise ValueError(
            "Narrative question belongs to a different narrative intention"
        )

    execution_record = narrator.propose(question, intention)
    question.respond(
        answer=execution_record.proposed_description,
        justification=execution_record.justification,
    )
    return execution_record
