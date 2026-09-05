from uuid import UUID

import pytest

from tessitura.domain.narrative_intensity import NarrativeIntensity
from tessitura.domain.narrative_intention import NarrativeIntention
from tessitura.domain.narrative_preparation import NarrativePreparation
from tessitura.domain.narrative_pressure import NarrativePressure
from tessitura.domain.narrator_justification import NarratorJustification


def test_narrative_preparation_cannot_change_its_intention() -> None:
    original_intention = NarrativeIntention(
        id=UUID(int=1),
        direction="Borg seeks revenge",
        intensity=NarrativeIntensity(3),
        pressure=NarrativePressure(2),
    )
    preparation = NarrativePreparation(
        id=UUID(int=2),
        intention=original_intention,
        description="Borg hires mercenaries",
        justification=NarratorJustification(
            "This form preserves Borg as the causal origin."
        ),
    )
    another_intention = NarrativeIntention(
        id=UUID(int=3),
        direction="Reveal the corruption beneath the city",
        intensity=NarrativeIntensity(2),
        pressure=NarrativePressure(1),
    )

    with pytest.raises(AttributeError):
        preparation.intention = another_intention  # pyright: ignore[reportAttributeAccessIssue]

    assert preparation.intention.id == original_intention.id
