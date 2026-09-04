from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativePressure:
    value: int
