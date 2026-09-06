from dataclasses import FrozenInstanceError

import pytest

from tessitura.domain.narrative_intensity import NarrativeIntensity


def test_narrative_intensity_has_value_equality() -> None:
    assert NarrativeIntensity(1) == NarrativeIntensity(1)


def test_narrative_intensity_is_immutable() -> None:
    intensity = NarrativeIntensity(1)

    with pytest.raises(FrozenInstanceError):
        intensity.value = 2  # pyright: ignore[reportAttributeAccessIssue]


@pytest.mark.parametrize("value", [1, 100])
def test_narrative_intensity_accepts_range_boundaries(value: int) -> None:
    assert NarrativeIntensity(value).value == value


@pytest.mark.parametrize("value", [-1, 0, 101])
def test_narrative_intensity_rejects_out_of_range_value(value: int) -> None:
    with pytest.raises(ValueError, match="must be between 1 and 100"):
        NarrativeIntensity(value)
