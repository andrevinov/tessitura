import json
from datetime import UTC, datetime
from time import perf_counter
from typing import cast
from uuid import uuid4

from openai import OpenAI

from tessitura.application.narrative_preparation_creation_execution_record import (
    NarrativePreparationCreationExecutionRecord,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation_creation_question import (
    NarrativePreparationCreationQuestion,
)
from tessitura.domain.narrator_justification import NarratorJustification


class OpenAINarrativePreparationCreationNarrator:
    def __init__(
        self,
        client: OpenAI,
        narrative_engine_version: str,
        model: str = "gpt-5.6-luna",
    ) -> None:
        self._client = client
        self._narrative_engine_version = narrative_engine_version
        self._model = model

    def propose(
        self,
        question: NarrativePreparationCreationQuestion,
        intention: NarrativeIntention,
    ) -> NarrativePreparationCreationExecutionRecord:
        instructions = (
            "You are Tessitura's narrative preparation creation component. "
            "Propose one Narrative Preparation for the supplied eligible "
            "Narrative Intention. A Narrative Preparation is a concrete "
            "possible future development, not a canonical fact and not a "
            "completed event. Concretize the intention's narrative archetype "
            "at its intended intensity using only the supplied context. Do not "
            "claim that the proposed events have already happened. Provide a "
            "concise description and justify in one or two sentences how the "
            "proposal realizes the archetype, fits the context, and matches "
            "the intended intensity."
        )
        started_at = perf_counter()
        response = self._client.responses.create(
            model=self._model,
            reasoning={"effort": "low"},
            max_output_tokens=500,
            instructions=instructions,
            input=json.dumps(
                {
                    "question": {
                        "id": str(question.id),
                        "intention_id": str(question.intention_id),
                        "initial_context": question.initial_context,
                    },
                    "intention": {
                        "id": str(intention.id),
                        "archetype": {
                            "name": intention.archetype.name,
                            "description": intention.archetype.description,
                        },
                        "current_assessment": {
                            "intensity": intention.intensity.value,
                            "pressure": intention.pressure.value,
                            "justification": (
                                intention.current_assessment.justification.text
                            ),
                        },
                    },
                },
                ensure_ascii=False,
            ),
            text={
                "format": {
                    "type": "json_schema",
                    "name": "narrative_preparation_creation",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "description": {
                                "type": "string",
                                "minLength": 1,
                            },
                            "justification": {
                                "type": "string",
                                "minLength": 1,
                            },
                        },
                        "required": ["description", "justification"],
                        "additionalProperties": False,
                    },
                }
            },
        )
        response_text = response.output_text
        try:
            raw_response: object = json.loads(response_text)
        except json.JSONDecodeError as error:
            raise ValueError(
                "OpenAI returned no structured narrative preparation proposal"
            ) from error

        if not isinstance(raw_response, dict):
            raise TypeError("OpenAI returned an invalid narrative preparation proposal")

        parsed_response = cast(dict[str, object], raw_response)
        description = parsed_response.get("description")
        justification_text = parsed_response.get("justification")
        if not isinstance(description, str) or not isinstance(justification_text, str):
            raise TypeError("OpenAI returned an invalid narrative preparation proposal")

        justification = NarratorJustification(justification_text)
        usage = response.usage
        if usage is None:
            raise ValueError("OpenAI returned no token usage information")

        return NarrativePreparationCreationExecutionRecord(
            execution_id=uuid4(),
            narrative_engine_version=self._narrative_engine_version,
            completed_at=datetime.now(UTC),
            duration_milliseconds=round((perf_counter() - started_at) * 1000),
            provider="openai",
            model=response.model,
            instructions=instructions,
            question_id=question.id,
            intention_id=intention.id,
            initial_context=question.initial_context,
            intention_archetype=intention.archetype,
            current_assessment=intention.current_assessment,
            provider_response_id=response.id,
            raw_response=response_text,
            proposed_description=description,
            justification=justification,
            input_tokens=usage.input_tokens,
            output_tokens=usage.output_tokens,
        )
