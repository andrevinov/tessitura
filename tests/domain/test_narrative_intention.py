from uuid import UUID

import pytest

from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_narrative_intention_keeps_intensity_and_pressure_distinct() -> None:
    intensity = NarrativeIntensity(2)
    pressure = NarrativePressure(3)

    intention = NarrativeIntention(
        id=UUID(int=0),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=intensity,
            pressure=pressure,
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    assert intention.intensity is intensity
    assert intention.pressure is pressure


def test_invalid_pressure_does_not_replace_current_intention_pressure() -> None:
    original_pressure = NarrativePressure(3)
    intention = NarrativeIntention(
        id=UUID(int=0),
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=original_pressure,
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    with pytest.raises(ValueError, match="cannot be negative"):
        intention.apply_assessment(
            NarrativeIntensityAndPressureAssessment(
                intensity=NarrativeIntensity(4),
                pressure=NarrativePressure(-1),
                justification=NarratorJustification(
                    "Borg is postponing his retaliation."
                ),
            )
        )

    assert intention.pressure is original_pressure


def test_narrative_intention_cannot_change_its_id() -> None:
    original_id = UUID(int=1)
    intention = NarrativeIntention(
        id=original_id,
        direction="Borg seeks revenge",
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    with pytest.raises(AttributeError):
        intention.id = UUID(int=2)  # pyright: ignore[reportAttributeAccessIssue]

    assert intention.id == original_id


def test_narrative_intention_rejects_blank_direction() -> None:
    with pytest.raises(ValueError, match="direction cannot be blank"):
        NarrativeIntention(
            id=UUID(int=1),
            direction="   ",
            current_assessment=NarrativeIntensityAndPressureAssessment(
                intensity=NarrativeIntensity(2),
                pressure=NarrativePressure(3),
                justification=NarratorJustification(
                    "A serious retaliation is warranted, but Borg needs time to prepare."
                ),
            ),
        )


def test_narrative_intention_cannot_change_its_direction_directly() -> None:
    original_direction = "Borg seeks revenge"
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction=original_direction,
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=NarrativePressure(3),
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
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
        current_assessment=NarrativeIntensityAndPressureAssessment(
            intensity=NarrativeIntensity(2),
            pressure=original_pressure,
            justification=NarratorJustification(
                "A serious retaliation is warranted, but Borg needs time to prepare."
            ),
        ),
    )

    with pytest.raises(AttributeError):
        intention.pressure = (  # pyright: ignore[reportAttributeAccessIssue]
            NarrativePressure(4)
        )

    assert intention.pressure is original_pressure


def test_narrative_intention_applies_reassessment() -> None:
    original_id = UUID(int=1)
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(7),
        justification=NarratorJustification(
            "Borg seeks a swift retaliation for his injury."
        ),
    )
    intention = NarrativeIntention(
        id=original_id,
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
    )
    new_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(8),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "After losing his army, Borg chooses a more devastating but patient revenge."
        ),
    )

    intention.apply_assessment(new_assessment)

    assert intention.intensity == NarrativeIntensity(8)
    assert intention.pressure == NarrativePressure(3)
    assert intention.current_assessment.justification == new_assessment.justification
    assert intention.id == original_id
    assert original_assessment.intensity == NarrativeIntensity(3)
    assert original_assessment.pressure == NarrativePressure(7)
    assert original_assessment.justification == NarratorJustification(
        "Borg seeks a swift retaliation for his injury."
    )
