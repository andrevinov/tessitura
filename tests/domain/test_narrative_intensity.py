from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.narrative_intensity import NarrativeIntensity


def test_narrative_intensity_has_value_equality() -> None:
    assert NarrativeIntensity(1) == NarrativeIntensity(1)


def test_narrative_intensity_is_immutable() -> None:
    intensity = NarrativeIntensity(1)

    with pytest.raises(FrozenInstanceError):
        intensity.value = 2  # pyright: ignore[reportAttributeAccessIssue]


def test_narrative_intensity_rejects_negative_value() -> None:
    with pytest.raises(ValueError, match="cannot be negative"):
        NarrativeIntensity(-1)
