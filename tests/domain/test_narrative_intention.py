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


@pytest.mark.parametrize(
    ("intensity_value", "pressure_value", "justification_text", "error_message"),
    [
        (
            -1,
            4,
            "Borg is postponing his retaliation.",
            "intensity must be between 1 and 100",
        ),
        (
            4,
            -1,
            "Borg is postponing his retaliation.",
            "pressure must be between 0 and 100",
        ),
        (4, 5, "", "justification cannot be empty"),
        (4, 5, "   ", "justification cannot be empty"),
    ],
)
def test_invalid_reassessment_preserves_entire_current_assessment(
    intensity_value: int,
    pressure_value: int,
    justification_text: str,
    error_message: str,
) -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "A serious retaliation is warranted, but Borg needs time to prepare."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=0),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
    )

    with pytest.raises(ValueError, match=error_message):
        intention.apply_assessment(
            NarrativeIntensityAndPressureAssessment(
                intensity=NarrativeIntensity(intensity_value),
                pressure=NarrativePressure(pressure_value),
                justification=NarratorJustification(justification_text),
            )
        )

    assert intention.current_assessment is original_assessment
    assert intention.intensity == NarrativeIntensity(2)
    assert intention.pressure == NarrativePressure(3)
    assert intention.current_assessment.justification == NarratorJustification(
        "A serious retaliation is warranted, but Borg needs time to prepare."
    )


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


def test_narrative_intention_cannot_replace_its_current_assessment_directly() -> None:
    original_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(7),
        justification=NarratorJustification(
            "Borg seeks a swift retaliation for his injury."
        ),
    )
    intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        current_assessment=original_assessment,
    )
    alternative_assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(8),
        pressure=NarrativePressure(3),
        justification=NarratorJustification(
            "Borg chooses a more devastating but patient revenge."
        ),
    )

    with pytest.raises(AttributeError):
        intention.current_assessment = (  # pyright: ignore[reportAttributeAccessIssue]
            alternative_assessment
        )

    assert intention.current_assessment is original_assessment


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
