from tessitura.domain.world_state import WorldState
from tessitura.domain.world_time_advance import WorldTimeAdvance


def test_advancing_world_time_records_the_transition() -> None:
    world = WorldState(elapsed_minutes=30)

    time_advance = world.advance_time(minutes=45)

    assert world.elapsed_minutes == 75
    assert world.revision == 1
    assert time_advance == WorldTimeAdvance(
        previous_elapsed_minutes=30,
        current_elapsed_minutes=75,
        world_revision=1,
    )
