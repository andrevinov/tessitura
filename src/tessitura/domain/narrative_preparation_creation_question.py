from uuid import UUID

from .narrator_justification import NarratorJustification


class NarrativePreparationCreationQuestion:
    def __init__(
        self,
        id: UUID,
        intention_id: UUID,
        prompt: str,
        initial_context: str,
    ) -> None:
        if not prompt.strip():
            raise ValueError("Narrative question prompt cannot be blank")

        self._id = id
        self._intention_id = intention_id
        self._prompt = prompt
        self._initial_context = initial_context
        self._answer: str | None = None
        self._justification: NarratorJustification | None = None

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def intention_id(self) -> UUID:
        return self._intention_id

    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def initial_context(self) -> str:
        return self._initial_context

    @property
    def answer(self) -> str | None:
        return self._answer

    @property
    def justification(self) -> NarratorJustification | None:
        return self._justification

    def respond(
        self,
        answer: str,
        justification: NarratorJustification,
    ) -> None:
        if self._answer is not None:
            raise ValueError("Narrative question has already been answered")

        self._answer = answer
        self._justification = justification
