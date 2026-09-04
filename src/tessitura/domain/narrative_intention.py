from dataclasses import dataclass
from uuid import UUID

from .narrative_intensity import NarrativeIntensity
from .narrative_pressure import NarrativePressure


@dataclass(eq=False)
class NarrativeIntention:
    id: UUID
    direction: str
    intensity: NarrativeIntensity
    pressure: NarrativePressure
