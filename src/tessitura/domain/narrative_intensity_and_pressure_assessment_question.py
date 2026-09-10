from uuid import UUID

from .evaluation_trigger_kind import EvaluationTriggerKind
from .narrative_intensity import NarrativeIntensity
from .narrative_pressure import NarrativePressure
from .narrator_justification import NarratorJustification


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
        self._intensity: NarrativeIntensity | None = None
        self._pressure: NarrativePressure | None = None
        self._justification: NarratorJustification | None = None

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
    def intensity(self) -> NarrativeIntensity | None:
        return self._intensity

    @property
    def pressure(self) -> NarrativePressure | None:
        return self._pressure

    @property
    def justification(self) -> NarratorJustification | None:
        return self._justification

    def respond(
        self,
        intensity: NarrativeIntensity,
        pressure: NarrativePressure,
        justification: NarratorJustification,
    ) -> None:
        if self._intensity is not None:
            raise ValueError("Narrative question has already been answered")

        self._intensity = intensity
        self._pressure = pressure
        self._justification = justification
