from typing import Protocol

from tessitura.application.narrative_assessment_execution_record import (
    NarrativeAssessmentExecutionRecord,
)


class NarrativeAssessmentExecutionRecorder(Protocol):
    def record(self, execution: NarrativeAssessmentExecutionRecord) -> None: ...
