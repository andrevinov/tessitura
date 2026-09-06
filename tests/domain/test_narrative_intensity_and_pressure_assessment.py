from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intensity_and_pressure_assessment import (
    NarrativeIntensityAndPressureAssessment,
)
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


@pytest.mark.parametrize(
    ("field_name", "alternative_value"),
    [
        ("intensity", NarrativeIntensity(8)),
        ("pressure", NarrativePressure(1)),
        (
            "justification",
            NarratorJustification(
                "Borg chooses a more devastating but patient revenge."
            ),
        ),
    ],
)
def test_assessment_cannot_reassign_its_fields(
    field_name: str,
    alternative_value: NarrativeIntensity | NarrativePressure | NarratorJustification,
) -> None:
    assessment = NarrativeIntensityAndPressureAssessment(
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(7),
        justification=NarratorJustification(
            "Borg seeks a swift retaliation for his injury."
        ),
    )
    original_value = getattr(assessment, field_name)
    assert alternative_value != original_value

    with pytest.raises(FrozenInstanceError):
        setattr(assessment, field_name, alternative_value)

    assert getattr(assessment, field_name) is original_value
