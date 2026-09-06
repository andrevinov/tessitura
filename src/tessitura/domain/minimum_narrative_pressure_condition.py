from dataclasses import dataclass

from .narrative_pressure import NarrativePressure


@dataclass(frozen=True)
class MinimumNarrativePressureCondition:
    # NarrativePressure is immutable, so sharing this default is safe.
    minimum: NarrativePressure = NarrativePressure(50)  # noqa: RUF009

    def is_satisfied_by(self, pressure: NarrativePressure) -> bool:
        return pressure.value >= self.minimum.value
