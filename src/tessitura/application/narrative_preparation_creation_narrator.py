from typing import Protocol

from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)


class NarrativePreparationCreationNarrator(Protocol):
    def propose(
        self,
        question: NarrativePreparationCreationQuestion,
        intention: NarrativeIntention,
    ) -> NarrativePreparationCreationExecutionRecord: ...
