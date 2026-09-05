from dataclasses import dataclass


@dataclass(frozen=True)
class NarratorJustification:
    text: str

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Narrator justification cannot be empty")
