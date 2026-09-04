from uuid import UUID

from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure


def test_narrative_intention_keeps_intensity_and_pressure_distinct() -> None:
    intensity = NarrativeIntensity(2)
    pressure = NarrativePressure(3)

    intention = NarrativeIntention(
        id=UUID(int=0),
        direction="Borg seeks revenge",
        intensity=intensity,
        pressure=pressure,
    )

    assert intention.intensity is intensity
    assert intention.pressure is pressure
