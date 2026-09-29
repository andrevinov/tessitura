from uuid import UUID

from .narrative_archetype import NarrativeArchetype
from .narrative_eligibility_configuration import NarrativeEligibilityConfiguration
from .narrative_intensity import NarrativeIntensity
from .narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from .narrative_pressure import NarrativePressure


class NarrativeIntention:
    def __init__(
        self,
        id: UUID,
        archetype: NarrativeArchetype,
        current_assessment: NarrativeIntensityAndPressureAssessment,
        eligibility_configuration: NarrativeEligibilityConfiguration,
    ) -> None:
        self._id = id
        self._archetype = archetype
        self._current_assessment = current_assessment
        self._eligibility_configuration = eligibility_configuration

    def __repr__(self) -> str:
        return (
            "NarrativeIntention("
            f"id={self._id!r}, "
            f"archetype_name={self._archetype.name!r}, "
            f"intensity={self.intensity.value}, "
            f"pressure={self.pressure.value}"
            ")"
        )

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def archetype(self) -> NarrativeArchetype:
        return self._archetype

    @property
    def eligibility_configuration(self) -> NarrativeEligibilityConfiguration:
        return self._eligibility_configuration

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

    def revise_eligibility_configuration(
        self, configuration: NarrativeEligibilityConfiguration
    ) -> None:
        self._eligibility_configuration = configuration
