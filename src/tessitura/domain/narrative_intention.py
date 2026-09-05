from uuid import UUID

from .narrative_intensity import NarrativeIntensity
from .narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from .narrative_pressure import NarrativePressure


class NarrativeIntention:
    def __init__(
        self,
        id: UUID,
        direction: str,
        current_assessment: NarrativeIntensityAndPressureAssessment,
    ) -> None:
        if not direction.strip():
            raise ValueError("Narrative intention direction cannot be blank")

        self._id = id
        self._direction = direction
        self._current_assessment = current_assessment

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def current_assessment(self) -> NarrativeIntensityAndPressureAssessment:
        return self._current_assessment

    @property
    def intensity(self) -> NarrativeIntensity:
        return self._current_assessment.intensity

    @property
    def pressure(self) -> NarrativePressure:
        return self._current_assessment.pressure

    def apply_assessment(
        self, assessment: NarrativeIntensityAndPressureAssessment
    ) -> None:
        self._current_assessment = assessment
