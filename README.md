# LMS Documentation

This directory contains the structured documentation produced during the analysis, specification, review, decision, and handoff phases of the LMS rewrite.

The documentation system is governed by:

* `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md`
* `ARTIFACT-METADATA-CONVENTION-v1.md`
* `HANDOFF-MANIFEST-CONVENTION-v1.md`
* `REVIEW-ARTIFACT-CONVENTION-v1.md`
* `HUMAN-DECISION-CONVENTION-v1.md`
* `LMS-REWRITE-DOCUMENTATION-WORKFLOW.md`

Those documents define the authoritative rules for evidence handling, classification, stable identifiers, document status, review, decisions, traceability, and artifact handoff.

This README provides the orientation and directory map only. It does not replace or duplicate those contracts.

---

## Documentation Flow

Documentation follows this general flow:

```text
source
   ↓
analysis
   ↓
review / decisions
   ↓
prd
   ↓
handoff
```

The flow is intentionally separated so that observed evidence, analytical findings, human decisions, product requirements, and implementation handoff are not conflated.

---

## Directory Structure

The GitHub repository root (`./`) is the canonical root for all Rewrite LMS documentation artifacts.

> **Legacy project context:** this repository is intentionally located inside the legacy project's `docs/` directory. Therefore, `docs/` is a filesystem location in the legacy project, not a directory that should be recreated inside this repository.

```text
./
├── AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md
├── ARTIFACT-METADATA-CONVENTION-v1.md
├── LMS-REWRITE-DOCUMENTATION-WORKFLOW.md
├── DOCUMENTATION-INDEX.md
├── ROLE-SPECIFIC-CONTRACT-TEMPLATE.md
├── ROLE-SPECIFIC-CONTRACT-*.md
│
├── analysis/
│   ├── existing-system.md
│   └── legacy-schema-snapshot.md
│
├── scope.md
├── feature-map.md
├── business-rules.md
├── database.md
│
├── prd/
│   └── <feature>.md
│
├── decisions/
│   └── <decision-name>.md
│
├── reviews/
│   ├── cross-feature-review.md
│   └── final-review.md
│
└── tools/
    └── generate-legacy-schema.py
```

### Canonical Artifact Paths

All workflow and role-specific contracts use paths relative to this repository root:

* `analysis/existing-system.md`
* `analysis/legacy-schema-snapshot.md`
* `scope.md`
* `feature-map.md`
* `business-rules.md`
* `prd/*.md`
* `database.md`
* `reviews/*.md`
* `decisions/*.md`

Do not prepend `docs/` to these paths inside this repository.
## Artifact Traceability

Documentation artifacts should be traceable across the documentation lifecycle.

A typical chain may look like:

```text
Source Evidence
      ↓
Analysis Finding
      ↓
Review / Conflict
      ↓
Decision
      ↓
Requirement
      ↓
Acceptance Criteria
      ↓
Handoff
```

Not every artifact requires every stage.

The applicable chain depends on the nature and maturity of the information.

---

## Documentation Index

`DOCUMENTATION-INDEX.md` provides the catalog of documentation artifacts currently present in this directory.

It should be updated when significant artifacts are created, changed, deprecated, or superseded.

The index is a navigation and registry mechanism. It is not a replacement for the artifacts themselves or for the master documentation contract.

---

## Source of Truth

When information appears to conflict, use the source-of-truth hierarchy and conflict-handling rules defined by the master documentation contract.

Do not resolve conflicts silently.

When a conflict cannot be resolved from available evidence, preserve it as an explicit conflict or open question and route it through the appropriate review or decision process.

---

## Status

This documentation structure is the initial baseline for the LMS rewrite documentation system.

The structure may evolve as the project introduces additional artifact types or workflow requirements. Structural changes should remain consistent with the master documentation contract and documentation workflow.
