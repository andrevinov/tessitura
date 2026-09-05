from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeIntensity:
    value: int

    def __post_init__(self) -> None:
        if self.value < 0:
            raise ValueError("Narrative intensity cannot be negative")
