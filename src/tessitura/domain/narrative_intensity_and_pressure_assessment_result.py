from dataclasses import dataclass

from .narrative_intensity import NarrativeIntensity
from .narrative_pressure import NarrativePressure
from .narrator_justification import NarratorJustification


@dataclass(frozen=True)
class NarrativeIntensityAndPressureAssessmentResult:
    intensity: NarrativeIntensity
    pressure: NarrativePressure
    justification: NarratorJustification
