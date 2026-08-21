# Tessitura Use Cases

> Status: Draft

This document defines what Tessitura does independently of any user interface, framework, storage mechanism, or external integration.

## Purpose

Tessitura exists to maintain and resolve the canonical state of an AI-narrated tabletop role-playing campaign. It performs the mechanical, temporal, and state-management work required by a turn so that the AI narrator does not need to keep the campaign rules, calculations, and complete history in its context.

## Actors

### AI Narrator

The AI narrator is ideally the only actor that interacts directly with Tessitura. Players communicate their actions to the AI narrator, which translates those actions into structured Tessitura requests and uses Tessitura's results to guide the campaign narrative.

Tessitura is designed primarily for AI consumption. A player-facing interface could expose limited character information, but direct access is discouraged because unrestricted queries could reveal campaign secrets, future events, and other information that the player should not know.

## System Boundary

### Tessitura Is Responsible For

- Accepting structured requests produced by an AI narrator from a player's natural-language action.
- Resolving those requests against the rules and the current canonical application state.
- Returning structured canonical and possible consequences that can guide the narrative.
- Accepting the AI narrator's decision about which possible consequences were used, deferred, or omitted.
- Recording the effects and state transitions that were finalized for the turn.

### Tessitura Is Not Responsible For

- Producing the unstructured narrative prose presented to the players.
- Choosing actions on behalf of player characters.
- Giving players unrestricted access to campaign state.

## AI Boundary Data Contract

The AI boundary uses strict, versioned JSON objects. JSON is the boundary serialization format, not the domain model itself.

The contract favors end-to-end efficiency over the smallest possible payload. Field names must be concise but meaningful because opaque abbreviations save few tokens while increasing errors and retries.

### Token-Efficiency Rules

- Use stable identifiers instead of repeating entity descriptions.
- Send only the state delta and facts required for the current decision.
- Omit null, empty, default, and derivable fields.
- Use short, stable enums for operations, event types, and dispositions.
- Keep operation objects flat when doing so remains unambiguous.
- Do not return calculations already completed by Tessitura unless they are narratively relevant or explicitly requested for diagnostics.
- Use concise natural-language facts when they are smaller and clearer than deeply nested structured data.
- Pretty-print examples in documentation, but serialize production payloads without insignificant whitespace.

### Run Request

The AI narrator sends interpreted actions, not the original player prose or character-sheet data already owned by Tessitura.

```json
{
  "schema": 1,
  "campaign": "cmp_01",
  "version": 42,
  "actions": [
    {
      "actor": "pc_07",
      "op": "ability_check",
      "ability": "dexterity",
      "bonus": 2
    }
  ]
}
```

### Run Result

Tessitura returns a provisional resolution. Canonical events describe facts or effects established by Tessitura. Possible events may be used, deferred, or omitted by the AI narrator.

```json
{
  "schema": 1,
  "run": "run_104",
  "version": 42,
  "canonical": [
    {
      "id": "evt_17",
      "type": "discovery",
      "actor": "pc_07",
      "fact": "A concealed passage is behind the west wall."
    }
  ],
  "possible": [
    {
      "id": "evt_21",
      "type": "foreshadowing",
      "fact": "A rhythmic vibration comes from beyond the passage."
    }
  ]
}
```

### Finalize Request

The AI narrator sends its event selection and the resulting narration together. This allows Tessitura to validate and commit the turn without requiring another model generation on the successful path.

```json
{
  "schema": 1,
  "run": "run_104",
  "decisions": {
    "evt_17": "use",
    "evt_21": "use"
  },
  "narration": "You press your hand against the west wall and notice a rhythmic vibration beyond a concealed passage."
}
```

Every returned event receives a disposition. For a canonical event, `omit` means that it was not used in the narration; it does not undo the canonical fact. For a possible event, `use`, `defer`, and `omit` control the lifecycle defined by that event type.

### Finalize Result

A successful finalization requires only a small acknowledgement. It does not need to be sent back to the AI narrator unless another model decision is required.

```json
{"run":"run_104","version":43,"ok":true}
```

Failures return a stable error code and only the information required to retry or resolve the conflict.

```json
{"run":"run_104","ok":false,"error":"version_conflict","version":43}
```

## Core Use Cases

### Run

**Primary actor:** AI narrator

**Intent:** Obtain the canonical and possible consequences of one or more player actions as structured data.

**Input:** A structured `Run Request` containing references to the campaign state and the interpreted player actions.

**Outcome:** A provisional `Run Result` containing the canonical and possible events applicable to the turn.

**Responsibilities:**

- Validate the request against the referenced campaign and state version.
- Resolve applicable rules, rolls, time progression, world systems, and campaign directions.
- Return only the information required for the AI narrator's remaining decisions.
- Preserve enough information to finalize the resolution deterministically.

**Invariants:**

- The result identifies the exact state version from which it was produced.
- Every returned event has a stable identifier.
- The result does not require the AI narrator to repeat calculations already performed by Tessitura.

### Finalize

**Primary actor:** AI narrator

**Intent:** Record how the returned events were handled and commit the selected possible effects to the canonical state.

**Input:** A structured `Finalize Request` referring to a previous run.

**Outcome:** The event dispositions are recorded, selected possible effects are committed, and a new canonical state version is produced.

**Responsibilities:**

- Validate the event selection and referenced state version.
- Enforce event-disposition rules.
- Commit the selected effects and state transitions exactly once.
- Preserve the association between the resolution, selected events, and narration.

**Invariants:**

- Only events produced by the referenced run can be selected.
- A run cannot be finalized against an incompatible state version.
- Repeating the same successful finalization does not apply its effects twice.

## Core Policies

- Tessitura owns the canonical campaign state.
- Direct communication with the AI narrator uses structured data.
- Tessitura performs deterministic calculations and retains their detailed records internally.
- AI-facing results contain only the relevant delta and unresolved narrative choices.
- Canonical world effects do not depend on whether the AI narrator mentions them.
- Every provisional resolution and committed turn is traceable and versioned.

## Out of Scope

- Generating the final narrative prose.
- Deciding what player characters attempt to do.
- Acting as an unrestricted campaign-data browser for players.

## Open Questions

- Can a safe, explicitly player-facing read model be supported later?
- Which world events are committed during `Run`, and which remain provisional until `Finalize`?
- Should narration be stored by Tessitura or only associated with the finalized turn by an external adapter?
