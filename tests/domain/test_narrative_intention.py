from uuid import UUID

import pytest

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


def test_invalid_pressure_does_not_replace_current_intention_pressure() -> None:
    original_pressure = NarrativePressure(3)
    intention = NarrativeIntention(
        id=UUID(int=0),
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(2),
        pressure=original_pressure,
    )

    with pytest.raises(ValueError, match="cannot be negative"):
        intention.pressure = NarrativePressure(-1)

    assert intention.pressure is original_pressure


def test_narrative_intention_cannot_change_its_id() -> None:
    original_id = UUID(int=1)
    intention = NarrativeIntention(
        id=original_id,
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
    )

    with pytest.raises(AttributeError):
        intention.id = UUID(int=2)  # pyright: ignore[reportAttributeAccessIssue]

    assert intention.id == original_id
