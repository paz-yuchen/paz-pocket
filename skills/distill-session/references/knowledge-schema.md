# Knowledge Schema and Lifecycle

Use this schema for knowledge notes created or managed by the skill. Preserve additional properties already used by the vault.

## Frontmatter

Use lowercase enum values and ISO dates. Quote wikilinks stored as YAML values.

```yaml
---
type: knowledge
title: Kafka Consumer Idempotency
category: middleware
scope: multi-project
status: active
evidence: confirmed
volatility: version-bound
verified: 2026-09-16
projects:
  - "[[Project Alpha]]"
  - "[[Project Beta]]"
components:
  - "[[Kafka]]"
sources:
  - repo-alpha/path/to/config.yml@commit
aliases: []
tags:
  - knowledge
---
```

Required properties:

- `type`: always `knowledge`.
- `title`: canonical human-readable note title.
- `category`: `code-convention`, `domain-model`, `data-analysis`, `middleware`, `dependency`, `debugging`, or `architecture`.
- `scope`: `project`, `multi-project`, or `cross-project`.
- `status`: `active`, `needs-review`, `superseded`, or `deprecated`.
- `evidence`: `confirmed`, `decided`, `observed`, or `hypothesis`.
- `volatility`: `stable`, `version-bound`, or `volatile`.
- `verified`: date the claim was last actually checked against its evidence. Do not advance it for an editorial-only change.
- `projects`: wikilinks to affected project notes; use an empty list only for genuinely project-independent knowledge.
- `components`: wikilinks to relevant services, libraries, middleware, datasets, or domain components.
- `sources`: repository paths with revisions, documentation URLs, ADRs, tests, queries, or other evidence locators.

Conditional properties:

- `review_after`: required for `volatile`; optional for `version-bound`; omit for `stable` unless a real review date is known.
- `supersedes`: wikilink to the older canonical note when this note replaces one.
- `superseded_by`: wikilink to the replacement when `status` is `superseded`.
- `aliases` and `tags`: preserve and extend according to vault conventions.

## Body

Use only the sections needed by the knowledge, while keeping the claim and its limits explicit:

```markdown
# Title

## Knowledge

Direct statement of the reusable knowledge.

## Applies when

Scope, versions, assumptions, and boundaries.

## Rationale and evidence

Why it is believed and why it matters.

## Relationships

- Applies to [[Project Alpha]].
- Depends on [[Kafka]].
- Produces data consumed by [[Project Beta]].

## Exceptions and failure modes

Conditions under which the knowledge is unsafe or false.
```

Properties support filtering; body links express typed meaning. Avoid repeating the same prose in both.

## Touch maintenance

Whenever an approved create or update touches a note:

1. Re-check the source and evidence used by the changed claim. Update `verified` only when this check occurred.
2. Reconcile `scope`, `projects`, `components`, and body relationships with the approved knowledge.
3. Set `status: needs-review` when evidence conflicts, a required source is unavailable, or a volatile claim has exceeded `review_after`. Return the conflict for user review rather than choosing a side silently.
4. Preserve historical notes. When one concept replaces another, set reciprocal `supersedes` and `superseded_by` links and mark the older note `superseded`.
5. For duplicates, merge unique knowledge into the canonical note, preserve useful aliases, update directly affected links, and supersede the duplicate. Deletion requires separate user authorization.
6. Keep `active` for currently applicable confirmed or decided knowledge. Use `deprecated` when the knowledge remains historically relevant but should no longer guide new work.

## Vault-wide maintenance boundary

Session distillation maintains only notes and relationships directly involved in approved changes. A separate vault-maintenance workflow should periodically review:

- `needs-review` notes and overdue `review_after` dates.
- Version-bound notes after dependency or platform upgrades.
- Duplicate concepts and aliases.
- Broken, ambiguous, or one-way relationships.
- Orphan knowledge notes with no project, component, or concept connections.
- `superseded` and `deprecated` notes whose backlinks still treat them as active guidance.

That workflow must produce a review manifest before changing notes and must not delete notes without explicit approval.
