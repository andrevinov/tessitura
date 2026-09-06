from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativePressure:
    value: int

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 100:
            raise ValueError("Narrative pressure must be between 0 and 100")
