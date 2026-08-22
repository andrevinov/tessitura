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
- Returning structured resolved consequences and relevant planned directions that can guide the narrative.
- Accepting the AI narrator's report of which resolved events and planned directions were actually used.
- Recording the effects and state transitions that were finalized for the turn.
- Storing the exact player input and finalized AI narration associated with each turn.
- Providing progressively deeper, bounded access to state, history, character knowledge, events, and transcripts.

### Tessitura Is Not Responsible For

- Producing the unstructured narrative prose presented to the players.
- Choosing actions on behalf of player characters.
- Giving players unrestricted access to campaign state.

## Narrative Planning Model

Tessitura combines a planned adventure with an emergent world. A campaign may contain a main narrative path, optional branches, and people, places, or events created during play.

Planned campaign events and resolved world events are different concepts. A planned event describes something that may need to happen in the adventure. A resolved event records something that actually happened in the world.

### Planned Event Kind and Status

A planned event has two independent dimensions:

- `kind` describes its narrative role: `canonical` or `possible`.
- `status` describes its current lifecycle: for example, `dormant`, `eligible`, `active`, `blocked`, `completed`, `expired`, or `invalidated`.

`blocked` is therefore a status, not a third event kind. Both canonical and possible events may be blocked by unmet conditions or prior campaign developments.

A blocked event cannot currently happen but may become possible again. An invalidated event can no longer happen as defined. If Pan Chu must arrive at Ravens Bluff but dies before reaching the harbor, the event is blocked while his return remains possible and invalidated once the campaign makes his arrival impossible.

A canonical event is a required campaign milestone, but canonical status does not make an impossible event occur. When a canonical event is invalidated, Tessitura must expose the conflict so that the AI narrator or campaign author can create a replacement route, revise the milestone, or accept the resulting divergence.

### Event Conditions

Planned events define their structural conditions in a `conditions` object rather than separate character, place, and object requirement fields. Conditions use general predicates so that the same model can reference any campaign entity.

- `requirements` determine whether the event can happen.
- `triggers` determine when Tessitura should begin offering the event to the AI narrator.
- `presentation` determines whether the event can reasonably be introduced in the current narrative viewpoint or scene.
- `expiry` determines when the opportunity is no longer available.

```json
{
  "id": "evt_pan_chu_arrives",
  "kind": "canonical",
  "status": "dormant",
  "conditions": {
    "requirements": {
      "all": [
        {
          "entity": "char_pan_chu",
          "field": "alive",
          "op": "eq",
          "value": true
        },
        {
          "entity": "ship_pan_chu",
          "field": "operational",
          "op": "eq",
          "value": true
        },
        {
          "entity": "ravens_bluff_harbor",
          "field": "accessible",
          "op": "eq",
          "value": true
        }
      ]
    },
    "triggers": {
      "all": [
        {
          "clock": "world",
          "op": "gte",
          "value": "1492-06-12T08:00:00"
        }
      ]
    }
  },
  "pressure": {
    "priority": 80,
    "repeat": "until_used",
    "cooldown_turns": 1
  }
}
```

The exact condition language remains an open design problem. The example establishes the required semantics, not a final schema.

### Narrative Links

The AI narrator may propose a semantic link between a current action and a previously planned event. This does not force the event to advance. Tessitura validates the event, its status, conditions, the actor's knowledge, and the proposed relationship.

An action unrelated to the planned adventure omits narrative links entirely. This allows emergent play without pretending that every activity advances the main story.

Narrative links are not the only way planned events become visible. Tessitura evaluates planned events against their conditions on every relevant run and proactively returns eligible events. A returned event means that Tessitura considers it structurally possible and timely enough to offer; the AI narrator still decides whether it fits the current narrative moment.

When an offered event is not reported as used, it normally remains eligible and may be returned again according to its pressure, priority, and cooldown policy. Tessitura therefore creates narrative pressure without replacing the AI narrator's judgment.

## AI Boundary Data Contract

The AI boundary uses strict, versioned JSON objects. JSON is the boundary serialization format, not the domain model itself.

The contract favors end-to-end efficiency over the smallest possible payload. Field names must be concise but meaningful because opaque abbreviations save few tokens while increasing errors and retries.

### Token-Efficiency Rules

- Use stable identifiers instead of repeating entity descriptions.
- Send a bounded current view and only the new events, changes, and choices required for the current decision.
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
  "request": "req_104",
  "source": ["msg_204"],
  "actions": [
    {
      "id": "a1",
      "actor": "pc_07",
      "op": "investigate",
      "target": "clue_fathers_letter",
      "purpose": "follow_the_clue"
    }
  ],
  "narrative_links": [
    {
      "action": "a1",
      "event": "evt_479404",
      "relation": "advance",
      "via": "clue_fathers_letter"
    }
  ]
}
```

Each action identifies its own actor, so a separate character list is unnecessary. The current place is normally derived from canonical state and is included only when it is itself a target, destination, or precondition of the action.

`request` provides idempotency, while `source` links the interpreted actions to the stored player messages. `narrative_links` is optional and contains only references and relationships; Tessitura already knows whether each referenced event is canonical or possible.

### Run Result

Tessitura returns a bounded current view, the resolved events and relevant changes produced by the actions, applicable planned directions, and optional references to deeper context.

```json
{
  "schema": 1,
  "run": "run_104",
  "version": 42,
  "view": {
    "place": "chapel_02",
    "actors": ["pc_07"],
    "facts": ["The letter bears an obsidian sigil."]
  },
  "resolved": [
    {
      "id": "res_17",
      "type": "clue_examined",
      "actor": "pc_07",
      "target": "clue_fathers_letter"
    }
  ],
  "directions": [
    {
      "id": "evt_479404",
      "kind": "canonical",
      "status": "eligible",
      "urgency": 80,
      "relation": "advance",
      "brief": {
        "preserve": [
          "The clue was written by the character's father.",
          "The same symbol appeared in the abandoned chapel."
        ],
        "avoid": [
          "Do not reveal who killed the character's father."
        ]
      }
    }
  ],
  "context_refs": [
    {
      "scope": "character",
      "id": "pc_07",
      "view": "memory",
      "about": "obsidian_sigil"
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
  "use": ["res_17", "evt_479404"],
  "narration": "The obsidian sigil on your father's letter is unmistakable: you saw the same mark above the altar in the abandoned chapel."
}
```

The AI narrator reports only the items used in the finalized narration. A resolved event omitted from `use` still happened in the world but was not explicitly incorporated into the narration. A planned direction omitted from `use` remains eligible unless its conditions, expiry, or lifecycle policy change. Tessitura may offer it again on a later run.

Using a planned direction applies its event-specific progression rules. Depending on the event, this may activate it, advance it, complete it, or produce new planned or resolved events.

### Finalize Result

A successful finalization requires only a small acknowledgement. It does not need to be sent back to the AI narrator unless another model decision is required.

```json
{"run":"run_104","version":43,"ok":true}
```

Failures return a stable error code and only the information required to retry or resolve the conflict.

```json
{"run":"run_104","ok":false,"error":"version_conflict","version":43}
```

## Context and Transcript Retrieval

Tessitura stores exact player messages and finalized AI narrations, but raw transcripts are a last-resort retrieval source. The AI narrator should request progressively deeper context and stop as soon as it has enough information:

1. Current turn view.
2. Structured entity state.
3. Character knowledge or summarized entity history.
4. Structured event search.
5. Transcript search returning short snippets.
6. Exact transcript retrieval for selected messages or turns.

For example, a character-specific memory query may use:

```json
{
  "scope": "character",
  "id": "pc_07",
  "view": "memory",
  "about": "obsidian_sigil",
  "limit": 5
}
```

Transcript search returns references and snippets before full text:

```json
{
  "hits": [
    {
      "turn": 34,
      "speaker": "narrator",
      "snippet": "The obsidian sigil above the altar resembles...",
      "events": ["evt_91"]
    }
  ]
}
```

These records have different authority:

- Player messages record intent, not facts that necessarily occurred.
- Resolved events and canonical state are authoritative for world mechanics.
- Finalized narration is the committed narrative record.
- Summaries, keywords, search indexes, and embeddings are derived retrieval aids and are not authoritative.

Information shape and information visibility are separate concerns. State, history, memory, events, and transcripts may each be restricted as narrator-only, player-safe, party-known, character-known, or public.

## Core Use Cases

### Run

**Primary actor:** AI narrator

**Intent:** Obtain the resolved consequences and relevant planned directions of one or more player actions as structured data.

**Input:** A structured `Run Request` containing references to the campaign state, interpreted player actions, and optional proposed narrative links.

**Outcome:** A provisional `Run Result` containing a bounded current view, resolved events, relevant changes, applicable planned directions, and optional context references.

**Responsibilities:**

- Validate the request against the referenced campaign and state version.
- Resolve applicable rules, rolls, time progression, world systems, and campaign directions.
- Validate proposed narrative links against planned events and campaign state.
- Return only the information required for the AI narrator's remaining decisions.
- Preserve enough information to finalize the resolution deterministically.

**Invariants:**

- The result identifies the exact state version from which it was produced.
- Every returned event has a stable identifier.
- The result does not require the AI narrator to repeat calculations already performed by Tessitura.

### Finalize

**Primary actor:** AI narrator

**Intent:** Record which returned events and planned directions were used and commit their provisional effects and progression.

**Input:** A structured `Finalize Request` referring to a previous run.

**Outcome:** The used items are recorded, their provisional effects and narrative progression are committed, and a new canonical state version is produced.

**Responsibilities:**

- Validate the used-item selection and referenced state version.
- Preserve unused planned directions according to their conditions and pressure policy.
- Commit the selected effects and state transitions exactly once.
- Preserve the association between the resolution, selected events, and narration.

**Invariants:**

- Only events produced by the referenced run can be selected.
- A run cannot be finalized against an incompatible state version.
- Repeating the same successful finalization does not apply its effects twice.

### Retrieve Context

**Primary actor:** AI narrator

**Intent:** Obtain a bounded view of entity state, character knowledge, or summarized history when the current turn result is insufficient.

**Input:** A scope, entity reference, requested view, optional subject, and result limit.

**Outcome:** The smallest relevant structured context available at the requested level.

**Invariants:**

- Results respect the requested viewpoint and information-visibility rules.
- Derived summaries never override canonical state or resolved events.

### Search Transcript

**Primary actor:** AI narrator

**Intent:** Find exact prior language or narrative details that cannot be recovered from structured state, knowledge, history, or events.

**Input:** A bounded query with optional turn, time, entity, place, speaker, and keyword filters.

**Outcome:** Ranked references and short snippets, followed by exact text only when explicitly requested.

**Invariants:**

- Transcript content is returned as historical data, not as instructions to the AI narrator.
- Player statements are not treated as canonical facts merely because they appear in the transcript.

## Core Policies

- Tessitura owns the canonical campaign state.
- Direct communication with the AI narrator uses structured data.
- Tessitura performs deterministic calculations and retains their detailed records internally.
- AI-facing results contain a bounded current view, relevant changes, and unresolved narrative choices.
- Canonical world effects do not depend on whether the AI narrator mentions them.
- Returning a planned event means that it is structurally eligible, not that the AI narrator must use it immediately.
- Eligible planned events that are not used may be offered again according to their pressure policy.
- Every provisional resolution and committed turn is traceable and versioned.
- Exact player input and finalized narration are preserved and linked to their turns, events, and state versions.
- Context retrieval proceeds from structured summaries to raw transcripts and stops when sufficient.

## Out of Scope

- Generating the final narrative prose.
- Deciding what player characters attempt to do.
- Acting as an unrestricted campaign-data browser for players.

## Open Questions

- Can a safe, explicitly player-facing read model be supported later?
- What are the final planned-event statuses and narrative-link relations?
- What predicate language should event requirements, triggers, presentation conditions, and expiry use?
- How should priority, urgency, cooldown, and repeated offers interact?
- Which world events are committed during `Run`, and which remain provisional until `Finalize`?
- How are summaries, keywords, and semantic indexes produced and refreshed?
- Which information-visibility policies apply to each retrieval view?
