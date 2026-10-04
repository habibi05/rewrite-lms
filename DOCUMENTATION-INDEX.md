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
| — | AI-DOCUMENTATION-PROMPT-CONTRACT-v1 | MASTER-CONTRACT | DRAFT | AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md | — |
| — | ARTIFACT-METADATA-CONVENTION-v1 | CONVENTION | APPROVED | ARTIFACT-METADATA-CONVENTION-v1.md | MASTER-CONTRACT |
| — | HANDOFF-MANIFEST-CONVENTION-v1 | CONVENTION | APPROVED | HANDOFF-MANIFEST-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION |
| — | REVIEW-ARTIFACT-CONVENTION-v1 | CONVENTION | APPROVED | REVIEW-ARTIFACT-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION |
| — | HUMAN-DECISION-CONVENTION-v1 | CONVENTION | APPROVED | HUMAN-DECISION-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION |
| — | OPEN-QUESTION-CONFLICT-CONVENTION-v1 | CONVENTION | APPROVED | OPEN-QUESTION-CONFLICT-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION, HUMAN-DECISION-CONVENTION |
| — | REQUIREMENT-BASELINE-CONVENTION-v1 | CONVENTION | APPROVED | REQUIREMENT-BASELINE-CONVENTION-v1.md | ARTIFACT-METADATA-CONVENTION, HUMAN-DECISION-CONVENTION, REVIEW-ARTIFACT-CONVENTION, OPEN-QUESTION-CONFLICT-CONVENTION |

### Workflow & Templates

| Artifact ID | Title | Type | Status | Location | Related / Depends On |
| ----------- | ----- | ---- | ------ | -------- | -------------------- |
| — | LMS-REWRITE-DOCUMENTATION-WORKFLOW | WORKFLOW | DRAFT | LMS-REWRITE-DOCUMENTATION-WORKFLOW.md | MASTER-CONTRACT, applicable conventions |
| — | ROLE-SPECIFIC-CONTRACT-TEMPLATE | TEMPLATE | DRAFT | ROLE-SPECIFIC-CONTRACT-TEMPLATE.md | MASTER-CONTRACT, WORKFLOW, applicable conventions |

### Active Operational Artifacts

No operational artifacts have been created yet.

This section will be populated as reverse engineering and downstream documentation begin.

Do not pre-register planned artifacts as existing artifacts.

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
| `HANDOFF`             | Curated downstream handoff artifact                        |
| `MASTER-CONTRACT`     | Highest-level documentation governance contract          |
| `CONVENTION`          | Governing structural or semantic convention              |
| `WORKFLOW`            | Documentation process and sequencing rules               |
| `ROLE-CONTRACT`       | Role-specific operating contract                         |
| `TEMPLATE`            | Reusable artifact/document template                      |
| `INDEX`               | Documentation catalog and navigation index               |                          |

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

### Governance
Registered above under **Governance Artifacts**.

### Workflow & Templates
Registered above under **Workflow & Templates**.

### Source
No operational source artifacts have been created yet.

### Analysis
No operational analysis artifacts have been created yet.

### Review
No operational review artifacts have been created yet.

### Decisions
No project decision artifacts have been created yet.

### Open Questions
No Open Question artifacts have been created yet.

### Conflicts
No Conflict artifacts have been created yet.

### Requirements
No requirement baseline artifacts have been created yet.

### PRD
No PRD artifacts have been created yet.

### Handoff
No handoff manifests have been created yet.

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
