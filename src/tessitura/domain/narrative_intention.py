from uuid import UUID

from .narrative_intensity import NarrativeIntensity
from .narrative_pressure import NarrativePressure


class NarrativeIntention:
    def __init__(
        self,
        id: UUID,
        direction: str,
        intensity: NarrativeIntensity,
        pressure: NarrativePressure,
    ) -> None:
        self._id = id
        self.direction = direction
        self.intensity = intensity
        self.pressure = pressure

    @property
    def id(self) -> UUID:
        return self._id
