from uuid import UUID

from .narrative_intention import NarrativeIntention
from .narrator_justification import NarratorJustification


class NarrativePreparation:
    def __init__(
        self,
        id: UUID,
        intention: NarrativeIntention,
        description: str,
        justification: NarratorJustification,
    ) -> None:
        self.id = id
        self._intention = intention
        self.description = description
        self.justification = justification

    @property
    def intention(self) -> NarrativeIntention:
        return self._intention
