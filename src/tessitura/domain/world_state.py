from .world_time_advance import WorldTimeAdvance


class WorldState:
    def __init__(self, elapsed_minutes: int = 0) -> None:
        if elapsed_minutes < 0:
            raise ValueError("World elapsed minutes cannot be negative")

        self._elapsed_minutes = elapsed_minutes
        self._revision = 0

    @property
    def elapsed_minutes(self) -> int:
        return self._elapsed_minutes

    @property
    def revision(self) -> int:
        return self._revision

    def advance_time(self, minutes: int) -> WorldTimeAdvance:
        if minutes <= 0:
            raise ValueError("World time advance must be positive")

        previous_elapsed_minutes = self._elapsed_minutes
        self._elapsed_minutes += minutes
        self._revision += 1

        return WorldTimeAdvance(
            previous_elapsed_minutes=previous_elapsed_minutes,
            current_elapsed_minutes=self._elapsed_minutes,
            world_revision=self._revision,
        )
