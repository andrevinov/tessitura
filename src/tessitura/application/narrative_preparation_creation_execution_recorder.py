from typing import Protocol

from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)


class NarrativePreparationCreationExecutionRecorder(Protocol):
    def record(
        self,
        execution: NarrativePreparationCreationExecutionRecord,
    ) -> None: ...
