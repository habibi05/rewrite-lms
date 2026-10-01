# LMS Documentation

This directory contains the structured documentation produced during the analysis, specification, review, decision, and handoff phases of the LMS rewrite.

The documentation system is governed by:

* `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md`
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

### `source/`

Contains source material and raw evidence used by the documentation process.

Examples:

* legacy source code references
* existing documentation
* screenshots
* database/schema references
* API definitions
* configuration references
* external/reference materials

Source material should remain distinguishable from AI-generated interpretation.

---

### `analysis/`

Contains analytical artifacts derived from source evidence.

Subdirectories:

* `reverse-engineering/` — system and legacy behavior analysis
* `domain/` — domain concepts and relationships
* `architecture/` — architectural analysis
* `data/` — data model and persistence analysis
* `workflow/` — process and workflow analysis
* `open-questions/` — unresolved questions requiring clarification or decision

Analysis must preserve traceability to its supporting evidence.

---

### `prd/`

Contains product requirements and specification artifacts that have progressed beyond raw analysis.

Subdirectories:

* `requirements/` — functional and non-functional requirements
* `user-flows/` — user and system flows
* `business-rules/` — documented business rules
* `acceptance-criteria/` — testable acceptance criteria

Analysis findings must not automatically become requirements without the appropriate review or decision process.

---

### `review/`

Contains review-related artifacts.

Subdirectories:

* `ai-review/` — AI-generated review findings
* `human-review/` — human review records
* `conflicts/` — conflicting evidence or interpretations
* `unresolved/` — issues that remain unresolved

Review artifacts should preserve the distinction between findings, questions, and decisions.

---

### `decisions/`

Contains explicit decisions that affect the documentation or rewrite direction.

Subdirectories:

* `ADR/` — Architecture Decision Records and significant technical decisions
* `decision-log/` — other documented decisions

A decision should identify its context, supporting evidence, decision owner, status, and affected artifacts where applicable.

AI analysis must not be presented as a human decision.

---

### `handoff/`

Contains curated outputs intended for downstream roles.

Subdirectories:

* `engineering/` — engineering-facing context
* `qa/` — QA and verification context
* `implementation/` — implementation-ready context

Handoff artifacts should reference their source analysis, decisions, requirements, and other relevant artifacts rather than silently reproducing unsupported conclusions.

---

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
