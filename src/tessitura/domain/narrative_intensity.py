from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeIntensity:
    value: int

    def __post_init__(self) -> None:
        if not 1 <= self.value <= 100:
            raise ValueError("Narrative intensity must be between 1 and 100")
