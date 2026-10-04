# Open Question & Conflict Convention v1

## 1. Purpose

This convention governs the canonical storage, structure, lifecycle, escalation, resolution, traceability, and historical preservation of unresolved Open Questions and Conflicts in the Rewrite LMS documentation system.

It complements the Artifact & Metadata Convention, Human Decision Convention, Review Artifact Convention, and Documentation Workflow.

This convention does not grant AI authority to resolve business ambiguity or conflict.

---

## 2. Governing Authority

The authority hierarchy is:

1. AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md
2. ARTIFACT-METADATA-CONVENTION-v1.md
3. HUMAN-DECISION-CONVENTION-v1.md
4. REVIEW-ARTIFACT-CONVENTION-v1.md
5. OPEN-QUESTION-CONFLICT-CONVENTION-v1.md
6. LMS-REWRITE-DOCUMENTATION-WORKFLOW.md
7. Role-Specific Contracts
8. Individual artifacts and instructions

If a lower-level document conflicts with a higher-level contract, the higher-level contract prevails.

---

## 3. Core Distinction

An Open Question records unresolved uncertainty that requires clarification, evidence, or human decision.

A Conflict records incompatible claims, rules, interpretations, requirements, or evidence that cannot be safely treated as simultaneously authoritative.

Neither is a decision.

Neither may be silently converted into a resolved state by AI.

The boundary is:

```text
Open Question / Conflict
        ↓
Unresolved State
        ↓
Escalation / Evidence
        ↓
Human Decision when authority is required
        ↓
Affected Artifact Revision
        ↓
Re-review when applicable
```

---

## 4. Identity Model

The canonical artifact identity remains `ART-xxx`.

Domain record identities are:

- `OQ-xxx` = Open Question record
- `CON-xxx` = Conflict record

`OQ-xxx` and `CON-xxx` are not artifact identities.

An artifact may therefore contain one or more records:

```text
ART-xxx
document: OPEN-QUESTION

    contains

OQ-xxx
```

or:

```text
ART-xxx
document: CONFLICT

    contains

CON-xxx
```

---

## 5. Canonical Storage

Open Question artifacts are stored under:

```text
open-questions/<name>.md
```

Conflict artifacts are stored under:

```text
conflicts/<name>.md
```

These paths are repository-relative.

The artifact filename is descriptive. The stable identity is the `ART-xxx` metadata field.

---

## 6. Required Metadata

Each Open Question artifact must contain:

```yaml
---
document: OPEN-QUESTION
artifact_id: ART-xxx
version: 1.0
status: DRAFT
owner: <role-or-authority>
---
```

Each Conflict artifact must contain:

```yaml
---
document: CONFLICT
artifact_id: ART-xxx
version: 1.0
status: DRAFT
owner: <role-or-authority>
---
```

Additional metadata may be required by the Artifact & Metadata Convention or by the applicable workflow.

---

## 7. Open Question Record

Each `OQ-xxx` should capture at minimum:

- Question
- Context
- Why the answer is currently unknown
- Evidence reviewed
- Affected artifacts or records
- Required authority or stakeholder
- Current impact
- Proposed next action
- Related decisions, reviews, conflicts, or requirements

An Open Question must remain explicit when available evidence is insufficient.

### Open Question States

The baseline domain states are:

- `OPEN`
- `IN_PROGRESS`
- `ANSWERED`
- `CANCELLED`
- `SUPERSEDED`

`ANSWERED` means the question has received an authoritative answer or decision; it does not itself constitute the decision artifact.

Where a Human Decision is required, the Open Question must link to the resulting `ART-xxx` decision artifact.

---

## 8. Conflict Record

Each `CON-xxx` should capture at minimum:

- Conflict statement
- Conflicting claims or sources
- Evidence for each side
- Why the claims cannot currently coexist
- Affected artifacts or records
- Impact
- Required authority or stakeholder
- Proposed resolution path
- Related decisions, reviews, open questions, or requirements

A conflict must not be hidden by selecting one side without recording the conflict and its resolution basis.

### Conflict States

The baseline domain states are:

- `OPEN`
- `IN_PROGRESS`
- `RESOLVED`
- `REJECTED`
- `SUPERSEDED`

`RESOLVED` means an authoritative resolution has been established and linked to the affected downstream artifacts.

Where human authority is required, the Conflict must link to the resulting `ART-xxx` Human Decision artifact.

---

## 9. Resolution Authority

AI may:

- identify an Open Question or Conflict;
- collect and organize evidence;
- distinguish known facts from assumptions;
- identify affected artifacts;
- propose options;
- recommend escalation;
- draft an Open Question or Conflict artifact.

AI may not:

- silently answer an unresolved business question;
- silently choose between conflicting authoritative sources;
- represent a recommendation as a human decision;
- mark a matter resolved solely because the model inferred a plausible answer.

Resolution authority belongs to the appropriate human authority defined by the project and applicable role contracts.

---

## 10. Human Decision Relationship

Open Questions and Conflicts are inputs to decision-making, not substitutes for it.

When a matter requires human authority:

```text
OQ-xxx / CON-xxx
       ↓
Human Decision
       ↓
ART-xxx (DECISION)
       ↓
Affected Artifact Revision
```

The Human Decision Convention governs the decision artifact.

This convention governs the unresolved item and its linkage to the decision.

---

## 11. Review Relationship

Reviews may discover or reference Open Questions and Conflicts.

Review findings use `REV-xxx` and remain governed by the Review Artifact Convention.

A reviewer must not silently resolve an Open Question or Conflict merely by editing the target artifact.

When a review finding exposes unresolved ambiguity or incompatibility, the appropriate `OQ-xxx` or `CON-xxx` record should be created or linked.

---

## 12. Blocking and Gate Behavior

Unresolved Open Questions and Conflicts may block downstream completion when they affect correctness, scope, business behavior, data requirements, acceptance criteria, or another material contract.

Blocking status must be explicit in the relevant artifact, review, or workflow context.

An item is not considered resolved merely because work continues around it.

Before an approval or acceptance gate, all material unresolved items must either:

1. be resolved and reflected in affected artifacts; or
2. have an explicit human decision accepting the remaining uncertainty/risk where the governing workflow permits it.

Approval does not erase the historical Open Question or Conflict.

---

## 13. Historical Preservation

Open Question and Conflict records are historical records.

Do not delete a record merely because it was answered, resolved, rejected, cancelled, or superseded.

When a new state or artifact supersedes an earlier record, preserve the original record and establish an explicit relationship.

The Artifact & Metadata Convention governs artifact-level supersession.

---

## 14. Traceability

Where applicable, trace:

```text
Source Evidence
      ↓
OQ-xxx / CON-xxx
      ↓
REV-xxx
      ↓
ART-xxx Human Decision
      ↓
Affected Artifact Revision
      ↓
Re-review
```

Not every item requires every relationship.

Traceability must be sufficient to explain:

- why the item existed;
- what evidence produced it;
- who or what resolved it;
- which artifacts changed as a result;
- whether re-review was required.

---

## 15. Documentation Index

The Documentation Index should register Open Question and Conflict artifacts using the canonical artifact identity.

At minimum, registry entries should expose:

- Artifact ID
- Artifact Type
- Status
- Location
- Owner
- Related decisions
- Relevant dependencies or affected artifacts

The Index is a navigation and registry mechanism. It is not the source of truth for the unresolved item.

---

## 16. Non-Boundaries

This convention does not define:

- human decision authority itself;
- approval authority;
- review finding lifecycle;
- requirement lifecycle;
- handoff manifest structure;
- implementation behavior.

Those remain governed by their respective contracts and conventions.

---

## 17. Validation Checklist

Before an Open Question or Conflict artifact is considered structurally valid:

- [ ] Artifact uses `ART-xxx`
- [ ] Domain records use `OQ-xxx` or `CON-xxx`
- [ ] Required metadata is present
- [ ] Canonical repository path is used
- [ ] Uncertainty or incompatibility is explicitly stated
- [ ] Evidence is recorded
- [ ] Affected artifacts are identified where known
- [ ] Required authority is identified
- [ ] Related decisions/reviews are linked where applicable
- [ ] Resolution is not attributed to AI without authority
- [ ] Historical state is preserved

---

## 18. Definition of Done

The convention is operational when:

1. Open Question and Conflict artifacts have canonical locations.
2. Their metadata and identity model are defined.
3. `OQ-xxx` and `CON-xxx` records are distinct from `ART-xxx`.
4. Resolution authority is explicit.
5. Human Decision linkage is defined.
6. Review linkage is defined.
7. Blocking behavior is explicit.
8. Historical preservation is explicit.
9. Documentation Index representation is defined.
10. Master Contract, Workflow, Role-Specific Contract Template, and README reference this convention consistently.

---

## 19. Change Control

Changes to this convention must preserve compatibility with the Master Contract and Artifact & Metadata Convention.

Material changes require appropriate review and human approval under the project documentation workflow.

---

## 20. Governing Principle

> Open Questions preserve uncertainty. Conflicts preserve incompatibility. Humans resolve matters requiring authority. Downstream artifacts express the resulting decision through the documentation workflow.

---

## Convention Status

```yaml
convention: OPEN-QUESTION-CONFLICT-CONVENTION
version: 1.0
status: APPROVED
owner: PROJECT_OWNER
```
