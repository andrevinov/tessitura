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
        if not direction.strip():
            raise ValueError("Narrative intention direction cannot be blank")

        self._id = id
        self._direction = direction
        self.intensity = intensity
        self._pressure = pressure

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def direction(self) -> str:
        return self._direction

    @property
    def pressure(self) -> NarrativePressure:
        return self._pressure

    def increase_pressure(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Narrative pressure increase must be positive")

        self._pressure = NarrativePressure(self._pressure.value + amount)
