import json
from pathlib import Path

from tessitura.application.narrative_assessment_execution_record import (
    NarrativeAssessmentExecutionRecord,
)


class JsonLinesNarrativeAssessmentExecutionRecorder:
    def __init__(self, path: Path) -> None:
        self._path = path

    def record(self, execution: NarrativeAssessmentExecutionRecord) -> None:
        serialized_execution = {
            "record_schema_version": 1,
            "execution_id": str(execution.execution_id),
            "narrative_engine_version": execution.narrative_engine_version,
            "completed_at": execution.completed_at.isoformat(),
            "duration_milliseconds": execution.duration_milliseconds,
            "provider": execution.provider,
            "model": execution.model,
            "instructions": execution.instructions,
            "question_id": str(execution.question_id),
            "intention_id": str(execution.intention_id),
            "trigger": execution.trigger.value,
            "initial_context": execution.initial_context,
            "intention_direction": execution.intention_direction,
            "previous_assessment": {
                "intensity": execution.previous_assessment.intensity.value,
                "pressure": execution.previous_assessment.pressure.value,
                "justification": execution.previous_assessment.justification.text,
            },
            "provider_response_id": execution.provider_response_id,
            "raw_response": execution.raw_response,
            "resulting_assessment": {
                "intensity": execution.resulting_assessment.intensity.value,
                "pressure": execution.resulting_assessment.pressure.value,
                "justification": execution.resulting_assessment.justification.text,
            },
            "input_tokens": execution.input_tokens,
            "output_tokens": execution.output_tokens,
        }

        with self._path.open("a", encoding="utf-8") as output_file:
            output_file.write(
                json.dumps(serialized_execution, ensure_ascii=False) + "\n"
            )
