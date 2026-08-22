# Domain Model

> Status: Draft

## Entities

### Campaign

- id: CampaignId
- name: str

### Character

- id: CharacterId
- campaign_id: CampaignId
- name: str
- kind: CharacterKind
- description: str
- sheet: CharacterSheet
- place_id: PlaceId

### Place

- id: PlaceId
- campaign_id: CampaignId
- name: str
- description: str

### Planned Event

- id: PlannedEventId
- campaign_id: CampaignId
- summary: str
- kind: PlannedEventKind
- status: PlannedEventStatus
- conditions: EventConditions
- pressure: EventPressure

### Resolved Event

- id: ResolvedEventId
- campaign_id: CampaignId
- kind: str
- occurred_at: datetime

### Turn

- id: TurnId
- campaign_id: CampaignId
- sequence: int
- player_inputs: list[str]
- narration: str | None

## Value Objects

### CharacterKind

- value: Enum[player_character, npc]

### AbilityScore

- score: int
- modifier: int (derived from score)

### CharacterSheet

- strength: AbilityScore
- dexterity: AbilityScore
- constitution: AbilityScore
- intelligence: AbilityScore
- wisdom: AbilityScore
- charisma: AbilityScore

### PlannedEventKind

- value: Enum[canonical, possible]

### PlannedEventStatus

- value: Enum[dormant, eligible, active, blocked, completed, expired, invalidated]

### EventConditions

- requirements: conditions
- triggers: conditions
- presentation: conditions
- expiry: conditions

### EventPressure

- priority: int
- repeat: str
- cooldown_turns: int

### Typed Identifiers

- CampaignId
- CharacterId
- PlaceId
- PlannedEventId
- ResolvedEventId
- TurnId

Each identifier contains a string value and identifies its corresponding entity.

## Boundary Objects

These objects belong to the versioned JSON contract with the AI narrator, not to the domain model itself.

### NarrativeResponse

- schema: SchemaVersion
- created_at: datetime

### SchemaVersion

- value: int
