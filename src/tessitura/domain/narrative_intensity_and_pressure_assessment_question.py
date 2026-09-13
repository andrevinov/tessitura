from uuid import UUID

from .evaluation_trigger_kind import EvaluationTriggerKind
from .narrative_intensity_and_pressure_assessment_result import (
    NarrativeIntensityAndPressureAssessmentResult,
)


class NarrativeIntensityAndPressureAssessmentQuestion:
    def __init__(
        self,
        id: UUID,
        intention_id: UUID,
        trigger: EvaluationTriggerKind,
        prompt: str,
        initial_context: str,
    ) -> None:
        if not prompt.strip():
            raise ValueError("Narrative question prompt cannot be blank")

        self._id = id
        self._intention_id = intention_id
        self._trigger = trigger
        self._prompt = prompt
        self._initial_context = initial_context
        self._answer: NarrativeIntensityAndPressureAssessmentResult | None = None

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def intention_id(self) -> UUID:
        return self._intention_id

    @property
    def trigger(self) -> EvaluationTriggerKind:
        return self._trigger

    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def initial_context(self) -> str:
        return self._initial_context

    @property
    def answer(self) -> NarrativeIntensityAndPressureAssessmentResult | None:
        return self._answer

    def respond(
        self,
        answer: NarrativeIntensityAndPressureAssessmentResult,
    ) -> None:
        if self._answer is not None:
            raise ValueError("Narrative question has already been answered")

        self._answer = answer
