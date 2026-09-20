from typing import Protocol

from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intensity_and_pressure_assessment_question import (
    NarrativeIntensityAndPressureAssessmentQuestion,
)
from tessitura.domain.narrative_intention import NarrativeIntention


class NarrativeAssessmentNarrator(Protocol):
    def assess(
        self,
        question: NarrativeIntensityAndPressureAssessmentQuestion,
        intention: NarrativeIntention,
    ) -> NarrativeIntensityAndPressureAssessment: ...
