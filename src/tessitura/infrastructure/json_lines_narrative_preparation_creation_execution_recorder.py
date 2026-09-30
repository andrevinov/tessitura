import json
from pathlib import Path

from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)


class JsonLinesNarrativePreparationCreationExecutionRecorder:
    def __init__(self, path: Path) -> None:
        self._path = path

    def record(
        self,
        execution: NarrativePreparationCreationExecutionRecord,
    ) -> None:
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
            "initial_context": execution.initial_context,
            "intention_archetype": {
                "name": execution.intention_archetype.name,
                "description": execution.intention_archetype.description,
            },
            "current_assessment": {
                "intensity": execution.current_assessment.intensity.value,
                "pressure": execution.current_assessment.pressure.value,
                "justification": execution.current_assessment.justification.text,
            },
            "provider_response_id": execution.provider_response_id,
            "raw_response": execution.raw_response,
            "proposed_description": execution.proposed_description,
            "justification": execution.justification.text,
            "input_tokens": execution.input_tokens,
            "output_tokens": execution.output_tokens,
        }

        with self._path.open("a", encoding="utf-8") as output_file:
            output_file.write(
                json.dumps(serialized_execution, ensure_ascii=False) + "\n"
            )
