from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeIntensity:
    value: int
