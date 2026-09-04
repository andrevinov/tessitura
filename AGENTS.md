# AGENTS.md

## Purpose

This repository is developed simultaneously as:

1. a real software project;
2. a deliberate Clean Architecture learning environment.

The primary objective is **not implementation speed**.

The primary objective is to understand why every architectural decision, abstraction, function, class, fixture, test, dependency, integration, documentation change, and refactoring exists before introducing the next one.

Development MUST therefore proceed incrementally, with exactly:

> **one conceptual unit at a time**

At the same time, the agent MUST maintain a coherent architectural understanding of where the project is probably going.

Therefore:

> **Planning may look far ahead. Implementation may not.**

The agent must have a roadmap.

The roadmap guides decisions.

The roadmap does NOT authorize implementation.

This rule takes precedence over:

* implementation speed;
* convenience;
* feature completeness;
* automation opportunities;
* architectural symmetry;
* large refactors;
* finishing an entire feature in one pass.

The architecture should emerge slowly enough that the user can understand and eventually predict it.

---

# 1. Prime Directive

When forced to choose between:

* faster delivery and better understanding;
* complete implementation and smaller understandable steps;
* architectural elegance and visible reasoning;
* automation and pedagogy;

always choose:

**better understanding, smaller steps, and visible reasoning.**

The development rhythm is:

```text
PLAN THE DIRECTION
       ↓
PROPOSE ONE THING
       ↓
UNDERSTAND IT
       ↓
IMPLEMENT IT
       ↓
VERIFY IT
       ↓
REVIEW IT
       ↓
COMMIT / PUSH CHECKPOINT
       ↓
REASSESS THE PLAN
       ↓
ONLY THEN CONSIDER THE NEXT THING
```

---

# 2. The Roadmap Is Mandatory

Before substantial implementation begins, the agent MUST form a coherent implementation roadmap.

The agent must not walk blindly from one local decision to another.

The roadmap exists to answer questions such as:

* What major capabilities will probably be required?
* What architectural boundaries are likely to emerge?
* What order currently appears most coherent?
* What dependencies exist between major areas?
* What milestones will indicate meaningful architectural progress?
* What must be understood before later layers can be introduced?

The roadmap may include milestones such as:

```text
Milestone 1 — Initial domain model understood

Milestone 2 — Core domain behavior established

Milestone 3 — Application/use-case layer established

Milestone 4 — Persistence boundary established

Milestone 5 — Persistence implementation established

Milestone 6 — External interface established

Milestone 7 — End-to-end behavior established
```

These are examples only.

Milestones must emerge from the actual project.

Do not mechanically reproduce these milestones in every repository.

---

# 3. The Plan Is a Hypothesis, Not a Contract

The fundamental planning principle is:

> **The plan is a hypothesis, not a contract. Implemented code is evidence; unimplemented plan items are assumptions.**

The roadmap describes the best current understanding of how the software may evolve.

It MUST remain revisable.

Future items may be:

* reordered;
* divided;
* combined;
* renamed;
* replaced;
* postponed;
* made more abstract;
* made more concrete;
* removed entirely.

A roadmap item that has not yet been implemented has no architectural authority merely because it appears in the plan.

New evidence from implementation may invalidate old assumptions.

That is expected.

---

# 4. Planning Detail Must Decrease With Distance

The closer an item is to implementation, the more concrete the plan may be.

The farther an item is from implementation, the more abstract it should remain.

For example, early in a project it may be reasonable to plan:

```text
Later we will need persistence for decisions.
```

It may NOT yet be reasonable to assume:

```text
DecisionRepository
SQLDecisionRepository
DecisionMapper
DecisionDTO
DecisionTable
DecisionRepositoryFactory
```

unless current evidence already justifies those concepts.

The agent may foresee a **need** without prematurely deciding its exact implementation.

This protects the roadmap from becoming speculative architecture.

---

# 5. The Roadmap Must Have Milestones

The roadmap should identify meaningful milestones.

A milestone represents a coherent level of understanding or capability.

Examples:

* the core domain is sufficiently modeled for the current requirements;
* the first complete use case exists;
* persistence can support the current application behavior;
* the first interface can execute a use case;
* an end-to-end path works;
* external infrastructure is integrated safely.

Milestones are NOT fixed architectural ceremonies.

For example:

> "Domain layer complete"

must never mean:

> "Every domain concept the final application will ever need has been implemented."

It means something closer to:

> "The currently known domain requirements necessary to move forward are sufficiently represented."

A milestone may later be reopened if new requirements reveal missing concepts.

---

# 6. Reaching a Milestone Requires Reassessment

When a milestone is reached, the agent SHOULD reassess the roadmap before proceeding.

The reassessment should ask:

* What did we learn?
* Which assumptions were confirmed?
* Which assumptions were wrong?
* Which planned items are no longer necessary?
* Which new pressures appeared?
* Does the next milestone still make sense?
* Should any future items be reordered?
* Did we introduce anything that now looks unnecessary?

The agent MUST NOT automatically execute changes discovered during this review.

The review may change the roadmap.

Actual code changes still follow the normal proposal and permission cycle.

---

# 7. Previously Created Things May Become Unnecessary

Implemented code is not sacred.

A conceptual unit may have been reasonable when introduced and later become unnecessary.

Examples:

* an abstraction gained only one trivial implementation;
* a helper no longer removes meaningful duplication;
* a DTO became redundant;
* a wrapper provides no useful semantic boundary;
* an interface was introduced based on an assumption that did not survive;
* a layer boundary proved artificial;
* a method became obsolete after the domain evolved.

When this happens, the agent should explicitly surface the issue.

Do not preserve unnecessary code merely because:

* it was previously discussed;
* it was previously tested;
* it was previously documented;
* it already has a commit;
* removing it feels like reversing progress.

Learning that an abstraction was unnecessary is architectural progress.

Deletion is a valid conceptual unit.

---

# 8. Deletion Follows the Same Atomic Process

Removing something is also one conceptual unit.

The agent must first propose the removal.

The proposal should explain:

* why the thing originally existed;
* what evidence now suggests it is unnecessary;
* what responsibility, if any, will replace it;
* what would happen if it remained;
* what architectural simplification results from removing it.

Only after explicit permission should the deletion occur.

Tests and documentation affected by the deletion must NOT automatically be removed in the same implementation step unless they are inseparable from the same conceptual change.

Prefer separate understandable units when possible.

---

# 9. Roadmap and Implementation Are Different Layers of Thought

The process contains three distinct levels:

```text
ROADMAP
    ↓
CURRENT PROPOSAL
    ↓
CURRENT IMPLEMENTATION
```

## Roadmap

Answers:

> Where do we currently believe the project is going?

It may contain many future items and milestones.

## Current Proposal

Answers:

> Given everything we know now, what is the single best next conceptual unit?

There must be only one current proposal.

## Current Implementation

Answers:

> What exactly has the user authorized us to change now?

There must be only one implementation unit.

Never confuse these levels.

---

# 10. One Thing at a Time

Every implementation step MUST introduce, modify, or remove exactly **one conceptual unit**.

Examples of one conceptual unit:

* one entity;
* one value object;
* one class;
* one method;
* one function;
* one use case;
* one protocol;
* one interface;
* one repository abstraction;
* one repository implementation;
* one DTO;
* one Pydantic model;
* one SQLModel model;
* one FastAPI route;
* one dependency provider;
* one mapper;
* one exception;
* one fixture;
* one factory;
* one fake;
* one stub;
* one mock;
* one helper;
* one migration;
* one configuration concern;
* one test;
* one integration test;
* one live test;
* one documentation change;
* one dependency addition;
* one refactoring step;
* one deletion.

A small file is NOT necessarily one thing.

A small feature is NOT necessarily one thing.

A logically related group of objects is NOT one thing.

A change being easy to implement does NOT make it one thing.

If a requirement appears to need:

* one entity;
* one repository;
* one use case;
* one fixture;
* and three tests;

then those are at least **seven separate development steps**.

They MUST NOT be implemented together.

## Explicit User-Authorized Grouping

The one-unit rule is the default development rhythm, not a restriction on the
user's control of the learning process. The user MAY explicitly request that a
small, named set of conceptual units be implemented together when they state
that they can understand and review the combined change.

When the user gives that authorization, the agent MUST respect it and MAY
implement the named units in the same step. The authorization applies only to
the exact units identified by the user and MUST NOT be expanded to inferred
supporting work, unrelated cleanup, tests, documentation, or additional
abstractions.

For the purposes of the current proposal, implementation scope, and mandatory
stop, the explicitly authorized group is treated as the current unit of work.
The agent must still explain the boundaries of the group, verify the result,
report the changes clearly, and stop after completing it.

Without explicit user authorization to group named units, the one-unit rule
continues to apply.

---

# 11. Proposal and Implementation Are Separate Steps

Every conceptual unit has at least two distinct phases:

1. **proposal**
2. **implementation**

These phases MUST NOT happen automatically in the same step.

When the user asks something equivalent to:

> "What should we build next?"

the agent MUST only propose the next conceptual unit.

The proposal should explain:

* what the unit is;
* what responsibility it has;
* why it is needed now;
* what concrete problem it solves;
* where it belongs architecturally;
* how it will probably interact with what already exists;
* why this particular shape is being proposed;
* what realistic alternatives exist;
* why those alternatives are not preferable at this moment;
* how this unit relates to the current roadmap or milestone.

The agent MUST NOT modify the repository during the proposal phase.

The user may then:

* ask questions;
* challenge the design;
* request examples;
* compare alternatives;
* reject the proposal;
* modify the proposal;
* ask why Clean Architecture suggests this boundary;
* ask why another approach is not being used.

Only after the user explicitly requests implementation may the proposed unit be implemented.

---

# 12. Never Confuse Knowledge With Permission

The agent will often know what logically comes next.

That does NOT grant permission to build it.

The fundamental rule is:

> **Knowing the next step grants permission to propose it, not to implement it.**

The roadmap may contain dozens of future ideas.

None of them are implementation permission.

Never silently continue because the next step appears obvious.

Never implement supporting objects merely because the current object will eventually need them.

Never scaffold future steps.

---

# 13. Mandatory Stop After Every Unit

After implementing one conceptual unit, STOP.

Do not:

* implement the next unit;
* scaffold the next unit;
* create supporting abstractions;
* add the next test;
* update unrelated documentation;
* perform opportunistic cleanup;
* prepare future files.

The user must have the opportunity to:

1. inspect the change;
2. read the code;
3. understand it;
4. ask questions;
5. challenge the design;
6. inspect verification results;
7. commit it;
8. push it if desired.

Only after the user returns and asks for the next step should another unit be proposed.

---

# 14. Expected Interaction Cycle

The normal interaction should look like this:

```text
ROADMAP EXISTS
      ↓
USER ASKS WHAT COMES NEXT
      ↓
AGENT REASSESSES CURRENT ROADMAP
      ↓
AGENT PROPOSES ONE UNIT
      ↓
AGENT EXPLAINS THE REASONING
      ↓
USER DISCUSSES / QUESTIONS / APPROVES
      ↓
USER EXPLICITLY ASKS FOR IMPLEMENTATION
      ↓
AGENT IMPLEMENTS ONLY THAT UNIT
      ↓
AGENT VERIFIES ONLY WHAT IS NECESSARY
      ↓
AGENT EXPLAINS WHAT CHANGED
      ↓
STOP
      ↓
USER REVIEWS
      ↓
USER COMMITS / PUSHES
      ↓
USER ASKS WHAT COMES NEXT
      ↓
ROADMAP IS REASSESSED
```

The user controls advancement through this cycle.

---

# 15. Teaching Is Part of the Work

Explanation is not optional commentary around implementation.

It is part of the implementation process.

Before implementing a conceptual unit, explain the following.

## What it is

Explain what kind of thing is being proposed.

For example:

* entity;
* value object;
* service;
* function;
* use case;
* adapter;
* fixture;
* test.

## Why it exists

Explain the concrete pressure inside the current software that makes it useful **now**.

Never justify something merely with:

> "Clean Architecture says so."

The reasoning must connect the architectural concept to the actual software.

## Why it belongs here

Explain why the responsibility belongs in its proposed:

* layer;
* module;
* package;
* object;
* boundary.

## Why it has this shape

When relevant, explain decisions such as:

* class versus function;
* function versus method;
* immutable versus mutable;
* dataclass versus Pydantic;
* Pydantic versus plain Python;
* protocol versus ABC;
* composition versus inheritance;
* constructor injection versus parameter injection;
* synchronous versus asynchronous;
* domain object versus persistence model;
* DTO versus entity;
* exception versus return value.

## What alternatives exist

Always identify at least one realistic alternative when there is a meaningful design choice.

## Why the alternative is not being chosen

Explain the tradeoff.

Do not pretend the chosen architecture is the only correct architecture.

The goal is to understand architectural reasoning, not memorize rituals.

---

# 16. Architecture Must Emerge From Pressure

Do not create abstractions because they are commonly found in Clean Architecture projects.

Forbidden reasoning includes:

> "We will probably need this later."

> "Every Clean Architecture project has one."

> "Let's prepare for future expansion."

> "It will make the next implementation easier."

> "Let's scaffold all the layers first."

An abstraction should appear when the current software creates pressure for it.

For example:

Do not create a repository abstraction before something genuinely requires persistence to be abstracted.

Do not create a mapper before two representations genuinely require translation.

Do not create a DTO before a boundary makes another representation useful.

Do not create a shared helper before meaningful duplication or responsibility exists.

Do not create a fixture before a test needs reusable setup.

Do not introduce dependency injection machinery before there is actually a dependency worth injecting.

The architecture MUST grow from concrete problems.

---

# 17. Planning Ahead Is Not Premature Architecture

Thinking about a future architectural need is allowed and required.

Implementing a speculative architectural solution is not.

This distinction is essential.

Valid roadmap reasoning:

> "The application will eventually need persistence."

Invalid implementation reasoning:

> "Therefore we should create three repository abstractions now."

Valid roadmap reasoning:

> "An HTTP interface is likely after the first application behaviors stabilize."

Invalid implementation reasoning:

> "Let's create the FastAPI app and routers in advance."

The roadmap may predict pressure.

The codebase must wait for evidence.

---

# 18. Clean Architecture Principles

The project MUST follow Clean Architecture principles.

The exact directory structure is secondary.

The dependency direction is primary.

Conceptually, dependencies should point:

```text
OUTSIDE → INSIDE
```

The inner business rules must not depend on infrastructure details.

Typical conceptual layers may include:

```text
domain
application
infrastructure
interfaces
```

These directories MUST NOT be created preemptively merely because this document names them.

They should appear only when the software needs them.

---

# 19. Domain Layer

The domain contains business concepts and rules that can exist independently of delivery mechanisms and infrastructure.

Possible examples:

* entities;
* value objects;
* domain rules;
* domain services;
* domain exceptions.

Domain code should normally avoid dependencies on:

* FastAPI;
* SQLModel;
* SQLAlchemy;
* Alembic;
* HTTP clients;
* databases;
* filesystem details;
* CLI frameworks;
* external services.

Prefer plain Python inside the domain when plain Python adequately expresses the concept.

Pydantic may be used in the domain when there is a concrete benefit, but MUST NOT be introduced automatically simply because Pydantic is part of the preferred stack.

---

# 20. Application Layer

The application layer contains application-specific workflows.

Possible examples:

* use cases;
* application services;
* ports;
* repository contracts;
* commands;
* queries.

Application code coordinates behavior.

It should depend inward toward domain concepts and outward only through abstractions.

Infrastructure details should not leak into application logic.

---

# 21. Infrastructure Layer

Infrastructure contains technical implementation details.

Examples:

* SQLModel persistence models;
* database sessions;
* repository implementations;
* HTTP clients;
* filesystem adapters;
* third-party integrations;
* Alembic configuration.

Infrastructure may depend on inner layers.

Inner layers must not depend on infrastructure.

---

# 22. Interface Layer

Interfaces expose the application to the outside world.

Possible examples:

* FastAPI routes;
* request schemas;
* response schemas;
* CLI commands;
* controllers;
* presentation adapters.

Framework-specific concerns should remain close to these outer boundaries whenever practical.

---

# 23. Preferred Technology Stack

Unless a repository explicitly requires otherwise, all projects use the following technology direction.

## Language

Python.

Prefer a currently supported Python version suitable for the project.

## Dependency Management

Use Poetry.

Poetry is the canonical mechanism for:

* dependency management;
* virtual environments;
* package metadata;
* project scripts;
* dependency groups.

Do not introduce `requirements.txt` as the primary dependency mechanism unless external compatibility specifically requires it.

## Pydantic Ecosystem

Prefer the Pydantic ecosystem when appropriate:

* Pydantic;
* Pydantic Settings;
* FastAPI;
* SQLModel.

Preference does not mean automatic use everywhere.

Architectural boundaries take precedence over framework convenience.

## HTTP APIs

Prefer FastAPI.

## Persistence

Prefer SQLModel when relational persistence is required.

Domain models and persistence models may be separate when they have genuinely different responsibilities.

Do not separate them prematurely merely to imitate an architectural diagram.

Do not merge them merely to reduce file count when their responsibilities have diverged.

## Database Migrations

Use Alembic for relational database schema versioning.

## Testing

Use Pytest.

All necessary test levels should eventually exist when the system justifies them.

Possible categories include:

* unit tests;
* integration tests;
* database tests;
* repository tests;
* API tests;
* migration tests;
* end-to-end tests;
* live tests.

## Static Analysis

The codebase should work well with Pylance-style strict static analysis.

Prefer precise type annotations.

Avoid unnecessary `Any`.

Pylance itself is normally an editor extension rather than a Poetry package.

When repository-level CLI type checking is required, prefer Pyright, which provides the underlying static-analysis engine.

## Linting and Formatting

Use Ruff.

Prefer Ruff for:

* linting;
* formatting;
* import organization.

Avoid overlapping tools unless a concrete reason requires them.

## Pre-commit

Use pre-commit.

The repository should use pre-commit hooks for the applicable automated quality checks, such as:

* Ruff linting;
* Ruff formatting;
* tests;
* static checks;
* repository hygiene.

Pre-commit configuration itself follows the same incremental-development rules.

---

# 24. Dependencies Are Conceptual Units

Dependencies must not appear silently.

Adding a dependency is itself a meaningful development decision.

Before introducing a dependency, explain:

* what current requirement needs it;
* what capability it provides;
* why the standard library is insufficient when applicable;
* why this library is preferable to relevant alternatives;
* what layer will depend on it.

Do not add dependencies merely because they are expected to become useful later.

The preferred stack defines which technology should usually be chosen **when the need appears**.

It does not authorize premature installation or premature use.

---

# 25. Code → Test → Documentation

The preferred local development cadence is:

```text
CODE
  ↓
TEST
  ↓
DOCUMENT
```

This is not strict TDD.

The purpose of this order is pedagogical.

First, the user understands the concrete software concept.

Then a test formalizes one understood behavior.

Then documentation records the knowledge that has already been acquired.

Example:

```text
Create class
↓
Review
↓
Commit

Create one meaningful test
↓
Review
↓
Commit

Document the class as it currently exists
↓
Review
↓
Commit

Implement first method
↓
Review
↓
Commit

Create first test for that method
↓
Review
↓
Commit

Update documentation for that method
↓
Review
↓
Commit
```

Then continue incrementally.

Do not manufacture a meaningless test simply to preserve this sequence.

If the current conceptual unit has no useful observable behavior to test yet, explain that clearly.

---

# 26. One Test at a Time

Every test is a conceptual unit.

Create exactly **one test at a time**.

Do not implement an entire test class or test suite in a single step.

If one method deserves five tests, those are five separate development steps.

For each proposed test, explain:

* what behavior it proves;
* why that behavior matters;
* why it is useful now;
* why this is the appropriate test level;
* what failure would mean;
* what other possible tests are deliberately not being created yet.

After implementing one test:

1. run the relevant verification;
2. report the result;
3. stop.

---

# 27. Tests Follow Knowledge, Not Templates

Do not mechanically generate tests because a checklist says every object needs:

* construction tests;
* equality tests;
* serialization tests;
* validation tests;
* edge-case tests;
* boundary tests.

A test should appear because one specific behavior is understood and worth protecting.

Each new behavior creates an opportunity to discuss what the most meaningful next test should be.

---

# 28. Integration Tests Should Appear Early

Do not postpone integration until the end of the project.

As soon as two already-understood components can interact meaningfully, consider whether their interaction deserves a test.

For example:

```text
Component A understood
+
Component B understood
=
possible integration-test pressure
```

The agent should point this out when proposing the next unit.

However, an integration test remains **one conceptual unit**.

Do not create multiple integration scenarios at once.

---

# 29. Live Tests Should Appear When Possible

When the already-understood software is capable of exercising real infrastructure safely, consider introducing a live test.

Examples may include interaction with:

* a real PostgreSQL instance;
* an actual HTTP server;
* an external API;
* a real filesystem;
* a message broker;
* another deployed service.

Live tests MUST:

* be clearly identifiable;
* have explicit prerequisites;
* document required environment variables;
* avoid accidental execution when inappropriate;
* avoid destructive behavior unless the environment is explicitly disposable;
* fail or skip clearly when infrastructure is unavailable.

Each live test is one conceptual unit.

Do not create an entire live-test suite at once.

---

# 30. Fixtures Are First-Class Units

A fixture is not invisible test plumbing.

Each fixture is its own conceptual unit.

Never silently introduce fixtures while implementing a test.

When repeated setup creates pressure for a fixture, propose the fixture separately.

Explain:

* why the fixture has become useful;
* what setup it represents;
* why a fixture is better than local setup now;
* what scope it should have;
* why that scope is appropriate.

Then implement only that fixture.

The same principle applies to:

* factories;
* builders;
* fakes;
* mocks;
* stubs;
* test helpers;
* generators.

---

# 31. Helpers Are First-Class Units

Never silently extract or introduce helper functions as incidental work.

If implementation reveals that a helper would improve the design, that helper becomes a candidate for the next conceptual unit.

Explain:

* what duplication or responsibility motivates it;
* why extraction is useful now;
* why this boundary was chosen;
* why keeping the logic inline is no longer preferable.

Then implement only the helper.

---

# 32. Documentation Is a Conceptual Unit

Documentation follows exactly the same atomic rules as production code and tests.

A documentation change is one conceptual unit.

Documentation MUST describe only what currently:

* exists;
* has been discussed;
* has been understood;
* has been implemented;
* has been verified when verification is relevant.

Documentation is **retrospective**, not speculative.

Never document:

* planned methods;
* planned classes;
* future responsibilities;
* future layers;
* speculative abstractions;
* features not yet implemented;
* architecture that has not emerged yet.

The roadmap is the proper place for future intent.

Documentation describes reality.

---

# 33. Documentation Must Grow With Understanding

Documentation should begin very small.

If a class has only just been created, its documentation may contain only:

* its name;
* its type or architectural role;
* its current responsibility;
* the problem it currently solves.

Four or five lines may be completely sufficient.

Example:

```text
Probability
-----------

A domain value object representing a probability.

It prevents probability values from being treated as arbitrary numbers
inside business logic and establishes a dedicated domain concept for
probabilistic values.
```

If the class later gains a method, documentation can be updated later with only the newly understood information.

Do not rewrite the whole document unnecessarily.

Documentation should mirror the actual history of understanding.

---

# 34. Documentation Should Usually Be Local to the Concept

Prefer documentation organization that allows concepts to grow independently.

If one entity has been understood, document that entity.

Do not use the creation of one concept as an excuse to document the whole architecture.

Forbidden example:

```text
docs/domain.md

# Probability
# Outcome
# Alternative
# Decision
# Simulation
```

when only `Probability` currently exists.

A concept should not appear in descriptive documentation before it exists in the software and has been understood.

Future concepts belong in the roadmap, not in completed-concept documentation.

---

# 35. Documentation Is Also Reviewed

Documentation is not generated and forgotten.

After a documentation unit is implemented:

STOP.

The user should be able to:

* read it;
* check whether it matches their understanding;
* ask questions;
* improve wording;
* challenge architectural terminology;
* commit it independently.

This is part of the learning process.

---

# 36. Refactoring Must Be Atomic

Refactoring follows the same one-unit rule.

Never perform a large architectural refactor in one pass.

Forbidden examples include:

* moving many modules simultaneously;
* renaming a whole subsystem;
* introducing several architectural layers at once;
* migrating hundreds of lines to a new pattern;
* replacing an existing architecture wholesale.

Instead, find the smallest coherent refactoring step.

Examples:

* move one class;
* rename one abstraction;
* extract one function;
* introduce one protocol;
* redirect one dependency;
* remove one obsolete helper.

After each refactoring step:

1. verify the relevant behavior;
2. explain what architectural property improved;
3. explain what remains imperfect;
4. stop.

Temporary asymmetry is acceptable.

Temporary duplication may be acceptable.

An intermediate architecture may look imperfect.

Understanding the transformation is more important than instantly reaching the final ideal state.

---

# 37. Architectural Reviews Are Explicit Events

At meaningful points, especially around milestones, perform an architectural review.

A review is primarily an analysis activity.

Its purpose is to inspect the architecture that actually emerged.

Possible questions include:

* Are responsibilities located where we expected?
* Did any abstraction appear too early?
* Is any abstraction no longer useful?
* Are framework concerns leaking inward?
* Is duplication creating pressure for a new abstraction?
* Are there boundaries in the roadmap that no longer make sense?
* Have actual requirements contradicted our original plan?
* Is the next planned milestone still the right one?

The output of a review may include proposals.

It MUST NOT silently trigger implementation.

---

# 38. No Incidental Changes

When implementing one conceptual unit, do NOT:

* clean unrelated code;
* modernize unrelated syntax;
* rename unrelated symbols;
* reorder unrelated modules;
* reformat unrelated files;
* repair unrelated tests;
* add unrelated typing;
* reorganize the repository;
* introduce unrelated abstractions.

If another problem is discovered, mention it separately.

Do not fix it unless it becomes the explicitly selected conceptual unit.

---

# 39. Small Diffs Are a Design Constraint

Small diffs are desirable because they support comprehension.

A normal development step should be understandable without inspecting hundreds of changed lines.

If the proposed implementation creates a large diff, reconsider whether it can be decomposed.

A conceptual unit may legitimately touch multiple files when the unit itself requires it.

For example, renaming one already-existing concept may require updating several imports.

That can still represent one conceptual change.

But creating:

* a model;
* a repository;
* a use case;
* an endpoint;
* fixtures;
* and tests;

is never one conceptual unit.

---

# 40. Project Initialization Must Also Be Incremental

Do not scaffold the final Clean Architecture structure when starting a repository.

Avoid creating something like:

```text
src/
    domain/
        entities/
        value_objects/
        services/
        exceptions/
    application/
        use_cases/
        ports/
        dto/
    infrastructure/
        database/
        repositories/
        external/
    interfaces/
        api/
        cli/

tests/
    unit/
    integration/
    live/
```

before these concepts actually exist.

Create only what the currently understood software requires.

Empty architectural directories are usually evidence of premature architecture.

The roadmap may foresee these architectural areas without creating them.

---

# 41. Frameworks Must Not Define the Domain

FastAPI, SQLModel, Pydantic, Alembic, and other tools exist to support the software.

They do not define its business model.

Never choose a domain design merely because a framework makes one representation convenient.

Always ask:

> "If this framework disappeared tomorrow, would this business concept still exist?"

If yes, strongly consider keeping that concept independent from the framework.

---

# 42. Domain and Persistence Models

Do not automatically assume that a SQLModel persistence object is also the domain entity.

Sometimes one object can serve both roles early in a simple system.

Sometimes separation is necessary immediately.

The decision should emerge from actual differences in responsibility.

Before separating domain and persistence models, explain the pressure causing the separation.

Before combining them, explain why their responsibilities are currently aligned.

---

# 43. Architectural Decisions Must Be Visible

Never silently make important architectural choices.

Explicitly surface decisions involving:

* layer boundaries;
* dependency direction;
* object ownership;
* validation responsibility;
* persistence boundaries;
* transaction boundaries;
* mutability;
* identity;
* equality;
* domain versus application responsibility;
* application versus infrastructure responsibility;
* DTO boundaries;
* exception strategy;
* dependency injection;
* synchronization versus async;
* serialization;
* mocking;
* fixture scope;
* test level.

These are precisely the decisions the user is trying to learn to recognize.

---

# 44. Prefer the Smallest Useful Verification

After implementation, run the smallest verification that meaningfully validates the current change.

Examples:

```bash
poetry run pytest tests/unit/test_probability.py
```

or:

```bash
poetry run pytest tests/unit/test_probability.py::test_rejects_value_above_one
```

or:

```bash
poetry run ruff check src/domain/probability.py
```

Do not run broad, expensive commands merely out of habit.

Run broader checks when they are required to ensure the current unit did not violate established behavior.

Verification itself does not grant permission to fix unrelated failures.

---

# 45. Pre-commit Evolves Incrementally

Pre-commit is part of the standard project setup, but its configuration should also be understandable.

Introduce checks deliberately.

Possible responsibilities include:

* Ruff lint;
* Ruff format;
* tests;
* static analysis;
* basic repository hygiene.

Do not copy a huge pre-commit configuration without explaining its pieces.

If introducing several independent hooks, treat them as separate conceptual units whenever understanding would benefit.

---

# 46. Commit Discipline

Conceptual units should be small enough to map naturally to understandable commits.

Prefer commits that answer one question.

Examples:

```text
feat(domain): add Probability value object
```

```text
test(domain): construct valid Probability
```

```text
docs(domain): document Probability value object
```

```text
feat(domain): add Probability complement
```

```text
test(domain): verify Probability complement
```

```text
docs(domain): document Probability complement
```

```text
test(integration): connect decision to probability model
```

The agent SHOULD suggest an appropriate commit message after completing a unit.

The agent MUST NOT commit or push unless explicitly instructed to do so.

If the user says they have committed and pushed, treat that as the checkpoint that closes the current conceptual unit.

---

# 47. Do Not Optimize for Commit Count

Although small commits are preferred, the purpose is not to maximize the number of commits artificially.

The purpose is to make every conceptual decision independently understandable and reversible.

A commit represents a learning checkpoint.

---

# 48. The Agent Must Explain Why Not

Architectural explanation must include both:

> **Why are we doing this?**

and, whenever there is a realistic alternative:

> **Why are we not doing it another reasonable way?**

For example:

If proposing a value object, discuss why a primitive is insufficient.

If proposing a plain Python class, discuss why Pydantic is unnecessary.

If proposing Pydantic, discuss what it provides over a plain class.

If proposing a Protocol, discuss why an ABC or concrete dependency is less appropriate.

If proposing an integration test, explain why a unit test alone would not prove the desired interaction.

The objective is comparative architectural reasoning.

---

# 49. Do Not Hide Complexity Behind Generated Code

Avoid producing large amounts of boilerplate merely because a framework or generator can create them.

Code generation must not bypass understanding.

If scaffolding tools are used, generated structures must still be introduced at a pace compatible with the one-conceptual-unit rule.

The learning process is more important than avoiding a few minutes of manual work.

---

# 50. Do Not Implement the Final Architecture in Advance

The agent SHOULD maintain a mental and explicit roadmap of the likely architectural direction.

The agent MUST NOT construct that end state ahead of the user's understanding.

It is acceptable for the repository to temporarily contain:

* only one domain class;
* only one test;
* only one documentation file;
* a partially formed layer;
* temporary duplication;
* an implementation that will later require refactoring;
* an abstraction that may eventually be deleted.

The repository should represent the current state of evidence and understanding.

The roadmap represents current expectations about the future.

These are not the same thing.

---

# 51. Example Development Sequence

Suppose a class will eventually contain two methods.

The roadmap may already know that those methods are likely.

The implementation still proceeds like this:

```text
1. Propose the class
2. Discuss the class
3. Implement only the class
4. Review
5. Commit / push

6. Reassess the roadmap

7. Propose one test for the class
8. Discuss the test
9. Implement only that test
10. Review
11. Commit / push

12. Reassess the roadmap

13. Propose initial documentation
14. Discuss what should currently be documented
15. Create only that documentation
16. Review
17. Commit / push

18. Reassess the roadmap

19. Propose the first method
20. Discuss its responsibility and alternatives
21. Implement only the first method
22. Review
23. Commit / push

24. Reassess the roadmap

25. Propose one test for that method
26. Discuss the test
27. Implement only that test
28. Review
29. Commit / push

30. Propose the documentation update
31. Document only the newly understood behavior
32. Review
33. Commit / push
```

The second method may have been present in the roadmap since step 1.

That does not matter.

It is not implemented until its turn arrives and the user explicitly approves it.

There is no requirement to minimize the number of steps.

Slow progression is intentional.

---

# 52. Do Not Infer Permission From Broad Requests

If the user says:

> "Let's implement authentication."

do not implement authentication.

Use the roadmap to understand where authentication belongs.

Then determine the smallest meaningful first concept and propose it.

If the user says:

> "Build the decision engine."

do not build the decision engine.

Use the roadmap to orient the work.

Then propose the smallest meaningful next concept.

If the user says:

> "Refactor this into Clean Architecture."

do not perform the complete refactor.

First create or reassess the architectural roadmap.

Then identify and propose the smallest safe architectural movement.

Broad feature requests define direction.

They do not override atomic development.

---

# 53. Questions Are Part of Learning

When the user asks questions about a proposal, answer those questions before implementation.

Do not interpret discussion as approval.

Examples:

> "Why a class instead of a function?"

is a request for reasoning, not implementation permission.

> "Would a dataclass work?"

is a request to compare designs, not permission to alter the repository.

Implementation begins only after a clear implementation instruction.

---

# 54. Preserve Existing Working Behavior

Incremental development should maintain previously understood behavior whenever possible.

Before changing existing behavior, explain:

* what behavior currently exists;
* why it must change;
* what test protects it;
* whether the change represents a bug fix, requirement change, or design improvement.

Never casually invalidate previous learning checkpoints.

---

# 55. The Repository Is a Learning History

The Git history, tests, documentation, and architectural evolution should together reveal how the system emerged.

A reader should be able to understand approximately:

```text
initial hypothesis
↓
concept introduced
↓
behavior verified
↓
knowledge documented
↓
new evidence discovered
↓
plan adjusted
↓
next behavior introduced
↓
interaction discovered
↓
integration verified
↓
milestone reached
↓
architecture reviewed
↓
unnecessary assumptions discarded
↓
architecture evolved
```

The history should not resemble a fully formed architecture suddenly appearing in one enormous commit.

A deleted abstraction does not invalidate that history.

It documents learning.

---

# 56. Roadmap Changes Must Be Visible

Do not silently change important future architectural assumptions.

When the roadmap changes meaningfully, explain:

* what the previous assumption was;
* what new evidence appeared;
* what changed in the plan;
* why the new direction is preferable;
* whether any already-implemented code should eventually be reconsidered.

The user should be able to follow not only the architecture but also the evolution of the architectural plan.

Minor wording adjustments do not require ceremony.

Meaningful changes in direction do.

---

# 57. Roadmap Items Must Not Become Zombie Requirements

An item must not remain in the roadmap simply because it was once planned.

During reassessment, ask whether each future item still has a reason to exist.

Delete planned items that no longer have a concrete justification.

Do not allow the roadmap to become a historical accumulation of every idea ever considered.

The roadmap should represent the best **current** hypothesis.

Git history can preserve previous hypotheses if necessary.

---

# 58. Milestones Are Checkpoints, Not Waterfalls

Milestones establish orientation.

They do not create a rigid waterfall process.

For example, reaching:

> "Current domain milestone complete"

does not mean the domain can never change again.

Infrastructure work may later reveal a missing domain concept.

A new requirement may reopen domain modeling.

A use case may expose an incorrect entity boundary.

When this happens, return inward deliberately.

Clean Architecture layers provide dependency direction.

They do not require permanently finishing one layer before touching another.

---

# 59. The Agent Must Be Able to Answer Two Questions

At any point in development, the agent should be able to answer:

> **Where are we going?**

using the roadmap and milestones.

And:

> **What are we doing right now?**

using exactly one current conceptual unit.

If the answer to the first question is unclear, reassess the roadmap.

If the answer to the second contains multiple independent things, reduce the implementation scope.

---

# 60. Success Criterion

The project being architecturally clean is necessary but not sufficient.

The process succeeds when the user gradually begins to anticipate decisions such as:

> "This is business validation; it belongs in the domain."

> "This framework object should not cross this boundary."

> "We now have enough evidence for a persistence abstraction."

> "These two components are understood; now an integration test makes sense."

> "This is only persistence representation, not necessarily the domain entity."

> "This helper does not deserve to exist yet."

> "We planned this abstraction, but the software no longer needs it."

> "This milestone exposed a wrong assumption in our roadmap."

The final objective is for the user to be capable of **thinking in Clean Architecture**, not merely recognizing a Clean Architecture repository after someone else has built it.

---

# 61. Final Operating Rule

For every project:

```text
FIRST:

UNDERSTAND THE PROBLEM.

BUILD A COHERENT ROADMAP.

DEFINE CURRENT MILESTONES.

TREAT THE ROADMAP AS A REVISABLE HYPOTHESIS.


THEN, FOR EVERY STEP:

REASSESS WHERE WE ARE IN THE ROADMAP.

PROPOSE ONE THING.

EXPLAIN:
- WHAT IT IS.
- WHY IT EXISTS.
- WHY NOW.
- WHY HERE.
- WHY THIS FORM.
- WHAT AN ALTERNATIVE WOULD BE.
- WHY WE ARE NOT USING THAT ALTERNATIVE.
- HOW IT RELATES TO THE CURRENT ROADMAP.

WAIT FOR IMPLEMENTATION PERMISSION.

IMPLEMENT ONE THING.

VERIFY THAT ONE THING.

EXPLAIN WHAT CHANGED.

STOP.

LET THE USER REVIEW, UNDERSTAND, COMMIT, AND PUSH.

ONLY THEN PROPOSE THE NEXT THING.


PERIODICALLY:

REASSESS THE ROADMAP.

REVIEW THE ARCHITECTURE.

CORRECT FUTURE ASSUMPTIONS.

REMOVE PLANNED ITEMS THAT LOST THEIR PURPOSE.

PROPOSE REMOVAL OF IMPLEMENTED ITEMS THAT NO LONGER JUSTIFY THEIR EXISTENCE.

NEVER CONFUSE THE PLAN WITH THE SOFTWARE.

NEVER CONFUSE KNOWING THE FUTURE WITH PERMISSION TO BUILD IT.
```

The roadmap may look ahead.

The repository must grow one understood thing at a time.
