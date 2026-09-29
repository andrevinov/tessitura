from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeArchetype:
    name: str
    description: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Narrative archetype name cannot be blank")

        if not self.description.strip():
            raise ValueError("Narrative archetype description cannot be blank")
