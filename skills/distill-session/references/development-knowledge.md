# Development Knowledge Criteria

Apply every section when classifying knowledge from a software-development session.

## Scope is not value

Assign one scope:

- `PROJECT`: applies to one project or repository.
- `MULTI_PROJECT`: describes a shared domain, contract, component, or dependency across named projects.
- `CROSS_PROJECT`: a generally reusable engineering technique, model, or lesson.

All three scopes are eligible for Obsidian. A project-only fact passes when it will answer a future question or prevent costly rediscovery. A relationship spanning repositories is itself a meaningful delta even when each endpoint is already documented locally.

## Candidate categories

- `CODE_CONVENTION`: a coding, testing, error-handling, naming, or module-boundary rule. Capture its rationale, applicability, and a useful example or counterexample. A formatter or linter setting without additional meaning is a source restatement.
- `DOMAIN_MODEL`: terminology, entities, invariants, state transitions, calculation definitions, exceptions, and downstream consequences.
- `DATA_ANALYSIS`: reusable query or analysis patterns, metric semantics, assumptions, validation methods, data-quality traps, and failure conditions. A one-off result is session output rather than knowledge.
- `MIDDLEWARE`: configuration semantics, version constraints, lifecycle behavior, ordering, retries, idempotency, timeouts, observability, and failure modes.
- `DEPENDENCY`: producer-consumer relationships, ownership, contracts, data flow, compatibility constraints, failure propagation, and operational boundaries between systems.
- `DEBUGGING`: repeatable symptoms, root causes, diagnostic signals, minimal reproductions, and durable fixes or prevention. Preserve the lesson rather than raw logs.
- `ARCHITECTURE`: module responsibilities, architectural decisions and trade-offs, security boundaries, deployment topology, and operational constraints.

## Persistence gates

A candidate must pass every gate:

1. **Retrieval value**: name a credible future development question the note will answer or a rediscovery cost it will avoid.
2. **Standalone meaning**: state one coherent concept that remains understandable outside the session.
3. **Evidence**: identify why it is believed and assign an evidence status from the section below.
4. **Scope**: identify affected projects, components, versions, environments, or business contexts closely enough to prevent unsafe generalization.
5. **Meaningful delta**: add a new concept, relationship, rationale, exception, example, failure mode, or stronger evidence beyond what the vault already contains.
6. **Graph value**: link the knowledge to the relevant concepts and project entities. Create or update a relationship when the relationship is the reusable knowledge.
7. **Safe content**: exclude credentials, secrets, unnecessary production data, and sensitive material outside the user's requested scope.

Mutable knowledge can pass when it is costly to rediscover and records its applicability, source, and verification date. Prefer `SKIP` when a candidate cannot pass a gate without speculation.

## Evidence status

- `CONFIRMED`: supported by tests, inspected code or configuration, authoritative documentation, or a reproducible runtime result.
- `DECIDED`: an explicit user or team decision; record the rationale and decision scope rather than presenting it as a universal fact.
- `OBSERVED`: supported by a bounded observation that is useful but not fully established; record the environment and limitation.
- `HYPOTHESIS`: not yet established. Use `SKIP` with `UNVERIFIED` unless the user explicitly asks to maintain hypothesis notes.

## Source of truth

Code, configuration, schemas, and repository documentation remain authoritative for exact implementation state. Obsidian should capture interpretation and retrieval value: why a rule exists, how a contract behaves, what crosses repository boundaries, which failure mode matters, and where the authoritative evidence lives.

The existence of a repository source does not force a skip. Choose `SKIP` only when the candidate merely repeats that source without adding meaning or graph relationships.

## Actions and reason codes

- `CREATE`: no canonical note represents the knowledge. Use `NEW_CONCEPT`, `NEW_RELATION`, or `NEW_PROJECT_APPLICATION`.
- `UPDATE`: a canonical note exists and the candidate adds value. Use `MEANINGFUL_DELTA`, `SCOPE_EXPANSION`, `EVIDENCE_UPGRADE`, or `RELATION_CHANGE`.
- `SKIP`: no write is justified. Use `DUPLICATE`, `EPHEMERAL`, `UNVERIFIED`, `SOURCE_RESTATEMENT`, `LOW_RETRIEVAL_VALUE`, `MISSING_SCOPE`, `TOO_BROAD`, or `SENSITIVE`.

## Canonical notes

Use the shared knowledge schema. Prefer one canonical concept note linked to several projects over duplicated per-project explanations. Keep a project-specific note when the project itself is the subject, and link it back to the general concept.
