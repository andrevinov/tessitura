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
        intention.pressure = (  # pyright: ignore[reportAttributeAccessIssue]
            NarrativePressure(-1)
        )

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


def test_narrative_intention_rejects_blank_direction() -> None:
    with pytest.raises(ValueError, match="direction cannot be blank"):
        NarrativeIntention(
            id=UUID(int=1),
            direction="   ",
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(3),
        )


def test_narrative_intention_cannot_change_its_direction_directly() -> None:
    original_direction = "Borg seeks revenge"
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction=original_direction,
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
    )

    with pytest.raises(AttributeError):
        intention.direction = (  # pyright: ignore[reportAttributeAccessIssue]
            "Reveal the corruption beneath the city"
        )

    assert intention.direction == original_direction


def test_narrative_intention_cannot_replace_its_pressure_directly() -> None:
    original_pressure = NarrativePressure(3)
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(2),
        pressure=original_pressure,
    )

    with pytest.raises(AttributeError):
        intention.pressure = (  # pyright: ignore[reportAttributeAccessIssue]
            NarrativePressure(4)
        )

    assert intention.pressure is original_pressure


def test_narrative_intention_increases_pressure_with_a_new_value() -> None:
    original_pressure = NarrativePressure(3)
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(2),
        pressure=original_pressure,
    )

    intention.increase_pressure(2)

    assert intention.pressure == NarrativePressure(5)
    assert intention.pressure is not original_pressure
    assert original_pressure == NarrativePressure(3)


@pytest.mark.parametrize("amount", [0, -1])
def test_narrative_intention_rejects_non_positive_pressure_increase(
    amount: int,
) -> None:
    original_pressure = NarrativePressure(3)
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(2),
        pressure=original_pressure,
    )

    with pytest.raises(ValueError, match="increase must be positive"):
        intention.increase_pressure(amount)

    assert intention.pressure is original_pressure
