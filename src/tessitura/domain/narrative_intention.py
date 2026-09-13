from uuid import UUID

from .narrative_eligibility_configuration import NarrativeEligibilityConfiguration
from .narrative_intensity import NarrativeIntensity
from .narrative_intensity_and_pressure_assessment_result import (
    NarrativeIntensityAndPressureAssessmentResult,
)
from .narrative_pressure import NarrativePressure


class NarrativeIntention:
    def __init__(
        self,
        id: UUID,
        direction: str,
        current_assessment: NarrativeIntensityAndPressureAssessmentResult,
        eligibility_configuration: NarrativeEligibilityConfiguration,
    ) -> None:
        if not direction.strip():
            raise ValueError("Narrative intention direction cannot be blank")

        self._id = id
        self._direction = direction
        self._current_assessment = current_assessment
        self._eligibility_configuration = eligibility_configuration

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def eligibility_configuration(self) -> NarrativeEligibilityConfiguration:
        return self._eligibility_configuration

    @property
    def current_assessment(self) -> NarrativeIntensityAndPressureAssessmentResult:
        return self._current_assessment

    @property
    def intensity(self) -> NarrativeIntensity:
        return self._current_assessment.intensity

    @property
    def pressure(self) -> NarrativePressure:
        return self._current_assessment.pressure

    def apply_assessment(
        self, assessment: NarrativeIntensityAndPressureAssessmentResult
    ) -> None:
        self._current_assessment = assessment

    def revise_eligibility_configuration(
        self, configuration: NarrativeEligibilityConfiguration
    ) -> None:
        self._eligibility_configuration = configuration
