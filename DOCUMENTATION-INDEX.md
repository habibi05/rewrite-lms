# Documentation Index

This file is the catalog and navigation index for documentation artifacts within the LMS rewrite documentation system.

It provides a structured overview of available artifacts, their current status, relationships, and locations.

This index is not a replacement for the artifacts themselves and does not override the master documentation contract.

---

## Index Rules

Each significant documentation artifact should be registered here when it becomes part of the active documentation set.

The index should help answer:

* What documentation exists?
* Where is it located?
* What type of artifact is it?
* What is its current status?
* What artifacts or evidence does it depend on?
* What decisions or downstream artifacts are related to it?

The index should not contain detailed findings or duplicate artifact content.

---

## Artifact Registry

### Governance Artifacts

| Artifact ID | Title | Type | Status | Location | Related / Depends On |
| ----------- | ----- | ---- | ------ | -------- | -------------------- |
| — | HUMAN-DECISION-CONVENTION-v1 | CONVENTION | APPROVED | HUMAN-DECISION-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION |


| Artifact ID | Title | Type | Status | Location | Related / Depends On |
| ----------- | ----- | ---- | ------ | -------- | -------------------- |
| —           | —     | —    | —      | —        | —                    |

---

## Artifact Types

The following artifact categories are used by this documentation structure.

| Type                  | Purpose                                                      |
| --------------------- | ------------------------------------------------------------ |
| `SOURCE`              | Source material or evidence reference                        |
| `ANALYSIS`            | Analytical finding derived from evidence                     |
| `REVIEW`              | Review activity or review finding                            |
| `CONFLICT`            | Explicitly documented conflicting evidence or interpretation |
| `OPEN-QUESTION`       | Unresolved question requiring clarification or decision      |
| `DECISION`            | Explicit project or product decision                         |
| `ADR`                 | Architecture Decision Record                                 |
| `REQUIREMENT`         | Product or system requirement                                |
| `USER-FLOW`           | Documented user/system flow                                  |
| `BUSINESS-RULE`       | Documented business rule                                     |
| `ACCEPTANCE-CRITERIA` | Testable acceptance criteria                                 |
| `HANDOFF`             | Curated downstream handoff artifact                          |

Additional artifact types may be introduced when required by the workflow.

---

## Status Values

Artifact status must follow the status definitions established by the master documentation contract.

Common lifecycle states may include:

* `DRAFT`
* `IN_REVIEW`
* `REVIEWED`
* `APPROVED`
* `ACCEPTED`
* `SUPERSEDED`
* `DEPRECATED`

Only statuses defined or permitted by the governing contract should be used for project artifacts.

---

## Relationship Conventions

The `Related / Depends On` column should reference stable artifact IDs rather than relying only on filenames.

Typical relationships include:

```text
SOURCE
  ↓
ANALYSIS
  ↓
REVIEW / CONFLICT
  ↓
DECISION
  ↓
REQUIREMENT
  ↓
ACCEPTANCE CRITERIA
  ↓
HANDOFF
```

An artifact may have multiple upstream or downstream relationships.

---

## Current Documentation Map

### Source

No registered artifacts yet.

### Analysis

No registered artifacts yet.

### Review

No registered artifacts yet.

### Decisions

No registered artifacts yet.

### PRD

No registered artifacts yet.

### Handoff

No registered artifacts yet.

---

## Maintenance

Update this index when:

1. A new significant artifact is created.
2. An artifact changes lifecycle status.
3. An artifact is superseded or deprecated.
4. A significant relationship between artifacts changes.
5. A decision materially changes the documentation structure or downstream artifacts.

Do not use this index to hide unresolved conflicts or replace missing evidence.

If an artifact cannot currently be classified or linked confidently, preserve the uncertainty rather than inventing metadata.

---

## Source of Truth

The artifact itself remains the source of truth for its detailed content.

The master documentation contract remains authoritative for documentation rules.

The documentation workflow remains authoritative for process and sequencing.

This index exists to make the documentation system discoverable and navigable.
