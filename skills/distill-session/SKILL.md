---
name: distill-session
description: Distill durable software-development knowledge from the current session, preview create/update/skip decisions for review, and apply approved changes to Obsidian. Use when the user wants to retain project, multi-project, or cross-project learnings.
---

# Distill Session

Turn the current session into topic-based knowledge, not a transcript or a chronological session summary.

## Obsidian dependency

Load and follow the installed `obsidian-cli` skill for active-vault discovery, search, reads, and writes, and `obsidian-markdown` for note syntax and properties. When the personal `obsidian-vault` skill is available, also load it for naming, linking, and index conventions. Treat the active vault resolved by `obsidian-cli` as authoritative when paths conflict, and disclose the conflict in the review manifest. If the operational skill or a safe vault destination cannot be resolved, report the missing dependency and make no writes.

## Phase 1: Distill and propose

1. Read [references/development-knowledge.md](references/development-knowledge.md) and [references/knowledge-schema.md](references/knowledge-schema.md). Apply all classification, evidence, persistence, schema, graph, and lifecycle rules.
2. Treat the full available conversation and the artifacts it references as source material. Extract candidate development knowledge across every relevant category in the reference.
3. Rewrite each candidate as a standalone claim or model with explicit scope, evidence, applicability, provenance, and relationships.
4. Search the vault by title terms, synonyms, projects, components, and related concepts. Read plausible matches before deciding; filename matching alone is insufficient.
5. Produce a review manifest covering every material candidate. Assign stable IDs (`K1`, `K2`, ...) and include:
   - Every item: category, scope, evidence status, volatility, affected projects, relationships, action, and reason code.
   - `CREATE`: proposed title/path, related notes, and complete note body.
   - `UPDATE`: target path and a readable diff of the exact proposed edit.
   - `SKIP`: concise candidate description and a specific reason.
6. End after the manifest and ask the user to approve all, approve selected IDs, or request revisions. The initial invocation never authorizes vault writes.

## Phase 2: Apply approved changes

Proceed only after explicit approval. Apply only the approved `CREATE` and `UPDATE` IDs; `SKIP` decisions require no approval.

Immediately before each change, re-read the target or related notes and detect drift from the reviewed version. If drift changes the proposed edit, return that item for renewed review. Otherwise preserve the user's edits and make the smallest coherent change. Re-read each saved note to verify the result.

Perform touch maintenance only on approved target notes and their directly affected relationships, following the lifecycle rules in `knowledge-schema.md`. A session distillation does not authorize a vault-wide cleanup.

Return an execution ledger keyed by the manifest IDs with `CREATED`, `UPDATED`, `NOT APPROVED`, or `FAILED`, plus the final note path and any failure reason. The review manifest and execution ledger in the session are the audit record; create a separate audit note only when the user requests one.

## Note shape

- Organize by concept, not by session or date. Use the vault's established naming conventions.
- Keep one coherent subject per note unless the vault already has a broader canonical note for it.
- Treat Obsidian as one knowledge graph for project, multi-project, and cross-project knowledge. Use the shared frontmatter schema and connect concepts, projects, components, middleware, producers, and consumers with wikilinks.
- Keep code, configuration, and repository documentation authoritative for exact implementation details. Store the meaning, rationale, constraints, hard-won findings, and relationships that make those sources reusable and discoverable.
- Update the canonical concept note when one exists instead of creating a project-specific duplicate; express project-specific applications or exceptions in that note or through linked project notes.

## Completion

Phase 1 is complete only when every material candidate has a manifest decision and every proposed write is fully reviewable. Phase 2 is complete only when every approved ID has an execution result and every successful write has been verified. If nothing passes the gate, say so plainly and create nothing.
