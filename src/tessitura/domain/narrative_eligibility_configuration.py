from dataclasses import dataclass

from .minimum_narrative_pressure_condition import MinimumNarrativePressureCondition


@dataclass(frozen=True)
class NarrativeEligibilityConfiguration:
    mandatory_conditions: tuple[MinimumNarrativePressureCondition, ...]
    weighted_conditions: tuple[tuple[MinimumNarrativePressureCondition, int], ...]
    minimum_score: int

    def __post_init__(self) -> None:
        if self.minimum_score < 0:
            raise ValueError("Minimum eligibility score cannot be negative")
        if not self.mandatory_conditions and not self.weighted_conditions:
            raise ValueError("Narrative eligibility requires at least one condition")
        for _, weight in self.weighted_conditions:
            if weight < 0:
                raise ValueError("Eligibility condition weight cannot be negative")
