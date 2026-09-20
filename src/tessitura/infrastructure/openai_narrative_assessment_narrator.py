import json
from typing import cast

from openai import OpenAI

from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


class OpenAINarrativeAssessmentNarrator:
    def __init__(self, client: OpenAI, model: str = "gpt-5.6-luna") -> None:
        self._client = client
        self._model = model

    def assess(
        self,
        question: NarrativeIntensityAndPressureAssessmentQuestion,
        intention: NarrativeIntention,
    ) -> NarrativeIntensityAndPressureAssessment:
        response = self._client.responses.create(
            model=self._model,
            reasoning={"effort": "low"},
            max_output_tokens=500,
            instructions=(
                "You are Tessitura's narrative assessment component. "
                "Evaluate the supplied narrative intention using only the supplied "
                "structured data. Narrative intensity is the desired strength of "
                "the intention's eventual realization, from 1 to 100. Narrative "
                "pressure is its current urgency to find a realization, from 0 to "
                "100. Return final values rather than deltas. Justify the decision "
                "in one or two concise sentences."
            ),
            input=json.dumps(
                {
                    "question": {
                        "id": str(question.id),
                        "intention_id": str(question.intention_id),
                        "trigger": question.trigger.value,
                        "initial_context": question.initial_context,
                    },
                    "intention": {
                        "id": str(intention.id),
                        "direction": intention.direction,
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
                    "name": "narrative_assessment",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "properties": {
                            "intensity": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "pressure": {
                                "type": "integer",
                                "minimum": 0,
                                "maximum": 100,
                            },
                            "justification": {
                                "type": "string",
                                "minLength": 1,
                            },
                        },
                        "required": ["intensity", "pressure", "justification"],
                        "additionalProperties": False,
                    },
                }
            },
        )
        try:
            raw_response: object = json.loads(response.output_text)
        except json.JSONDecodeError as error:
            raise ValueError(
                "OpenAI returned no structured narrative assessment"
            ) from error

        if not isinstance(raw_response, dict):
            raise TypeError("OpenAI returned an invalid narrative assessment")

        parsed_response = cast(dict[str, object], raw_response)
        intensity = parsed_response.get("intensity")
        pressure = parsed_response.get("pressure")
        justification = parsed_response.get("justification")
        if (
            not isinstance(intensity, int)
            or isinstance(intensity, bool)
            or not isinstance(pressure, int)
            or isinstance(pressure, bool)
            or not isinstance(justification, str)
        ):
            raise TypeError("OpenAI returned an invalid narrative assessment")

        return NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(intensity),
            pressure=NarrativePressure(pressure),
            justification=NarratorJustification(justification),
        )
