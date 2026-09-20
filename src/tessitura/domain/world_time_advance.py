from dataclasses import dataclass


@dataclass(frozen=True)
class WorldTimeAdvance:
    previous_elapsed_minutes: int
    current_elapsed_minutes: int
    world_revision: int

    def reaches(self, elapsed_minute: int) -> bool:
        if elapsed_minute < 0:
            raise ValueError("Elapsed minute threshold cannot be negative")

        return (
            self.previous_elapsed_minutes
            < elapsed_minute
            <= self.current_elapsed_minutes
        )
