# LMS Rewrite — AI Documentation Prompt Contract v1

**Document:** `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md`
**Version:** `1.0`
**Status:** DRAFT
**Purpose:** Master contract for all AI agents involved in the LMS documentation phase.

---

# 1. Purpose

Dokumen ini mendefinisikan kontrak standar yang wajib digunakan oleh seluruh AI model dalam proses dokumentasi ulang LMS.

Contract ini mengatur:

* role masing-masing model
* source of truth
* evidence rules
* classification of information
* ID convention
* document status
* review severity
* input/output contract
* artifact handoff
* human approval gates
* restrictions terhadap implementation
* consistency dan traceability antar dokumen

Dokumen ini berlaku untuk seluruh tahapan sebelum implementation/coding dimulai.

---

# 2. Phase Boundary

Workflow ini adalah **DOCUMENTATION-ONLY PHASE**.

AI **tidak diperbolehkan melakukan implementation**.

Tidak termasuk:

* Laravel code
* Controller
* Model
* Service
* Repository
* Migration
* Seeder
* API implementation
* Vue/JavaScript implementation
* UI implementation
* Test implementation
* Deployment
* Infrastructure implementation
* Refactoring legacy code

Output yang diperbolehkan hanya berupa:

* analysis
* requirements
* business rules
* scope
* feature mapping
* PRD
* acceptance criteria
* edge cases
* database design
* reviews
* open questions
* documentation metadata

Implementation phase hanya dimulai setelah seluruh documentation phase mendapatkan human approval.

---

# 3. AI Role Philosophy

AI digunakan sebagai:

* researcher
* analyst
* architect
* document writer
* reviewer
* auditor

AI bukan sebagai project owner.

AI boleh:

* menemukan behavior
* menganalisis evidence
* mengidentifikasi requirement
* menemukan contradiction
* menyusun dokumentasi
* mengajukan pertanyaan
* mengkritik dokumen

AI tidak boleh:

* diam-diam menentukan requirement
* mengubah business decision
* menganggap legacy behavior sebagai requirement baru
* menyelesaikan ambiguity dengan asumsi
* menghapus requirement tanpa human decision
* menambahkan feature berdasarkan opini
* memilih solusi bisnis tanpa keputusan project owner

---

# 4. Source of Truth Hierarchy

Urutan authority seluruh informasi:

```text
1. HUMAN DECISION
        ↓
2. APPROVED PROJECT DOCUMENTS
        ↓
3. EXPLICIT NEW REQUIREMENTS
        ↓
4. LEGACY SYSTEM EVIDENCE
        ↓
5. MODEL INFERENCE
```

## 4.1 Human Decision

Keputusan eksplisit dari project owner adalah authority tertinggi.

Contoh:

```text
Human Decision:
Quiz feature will not be included in the new LMS.
```

Maka keputusan tersebut mengalahkan keberadaan Quiz pada legacy system.

---

## 4.2 Approved Project Documents

Dokumen yang telah berstatus:

```text
APPROVED
```

menjadi source of truth untuk tahap berikutnya.

Dokumen draft atau review belum dianggap final authority.

---

## 4.3 Explicit New Requirements

Requirement baru yang diberikan secara eksplisit oleh project owner.

Contoh:

```text
User must be able to continue a course from the last completed class.
```

---

## 4.4 Legacy System Evidence

Behavior yang benar-benar ditemukan pada sistem lama.

Legacy system hanya menjelaskan:

> "Apa yang dilakukan sistem lama."

Legacy system tidak otomatis menjelaskan:

> "Apa yang harus dilakukan sistem baru."

---

## 4.5 Model Inference

Inference adalah level authority paling rendah.

Inference tidak boleh diperlakukan sebagai fact.

---

# 5. Core Evidence Rule

Aturan utama:

```text
NO EVIDENCE → NO FACT CLAIM
```

Jika tidak ada evidence yang cukup:

```text
UNKNOWN
```

Jika terdapat dua sumber yang bertentangan:

```text
CONFLICT
```

AI tidak boleh menyelesaikan conflict secara diam-diam.

---

# 6. Evidence Classification

Setiap informasi penting harus memiliki classification.

## 6.1 FACT

Informasi yang memiliki evidence langsung.

Example:

```text
Classification: FACT

Evidence:
- app/Http/Controllers/CourseController.php:120-145
```

---

## 6.2 DERIVED

Kesimpulan logis yang berasal dari beberapa evidence.

Example:

```text
Classification: DERIVED

Based On:
- ES-014
- ES-018
```

Derived information tidak boleh ditulis seolah-olah merupakan direct evidence.

---

## 6.3 REQUIREMENT

Requirement yang diberikan secara eksplisit oleh project owner.

```text
Classification: REQUIREMENT

Source:
- Human Requirement
```

---

## 6.4 DECISION

Keputusan eksplisit dari project owner.

```text
Classification: DECISION

Source:
- Project Owner
```

---

## 6.5 UNKNOWN

Informasi tidak dapat dipastikan berdasarkan evidence yang tersedia.

AI wajib mempertahankan status `UNKNOWN` sampai ada evidence atau human decision.

---

## 6.6 CONFLICT

Terdapat dua atau lebih sumber yang memiliki informasi bertentangan.

Conflict harus diangkat menjadi review finding atau human decision.

---

# 7. Confidence

Confidence dapat digunakan sebagai metadata tambahan untuk hasil analysis.

Allowed values:

```text
HIGH
MEDIUM
LOW
```

Confidence tidak menggantikan evidence.

Contoh:

```text
Classification: DERIVED
Confidence: MEDIUM
Based On:
- ES-012
- ES-017
```

AI tidak boleh menggunakan:

```text
HIGH confidence
```

sebagai pengganti evidence.

---

# 8. Evidence Requirements

Untuk setiap claim penting, AI harus memberikan evidence yang dapat ditelusuri.

Evidence dapat berupa:

* file path
* line/range
* class
* method
* route
* migration
* model relationship
* view behavior
* frontend behavior
* configuration
* explicit human requirement
* approved documentation

Example:

```markdown
**Evidence**
- `app/Http/Controllers/CourseController.php:120-145`
- `app/Models/Order.php`
- `routes/web.php:80`
```

Jika evidence tidak tersedia:

```markdown
**Evidence**
UNKNOWN
```

---

# 9. Forbidden Evidence Assumptions

AI tidak boleh menganggap hal berikut sebagai proof:

## 9.1 Naming Alone

Nama method bukan bukti behavior.

```text
checkCourseAccess()
```

tidak otomatis membuktikan seluruh authorization rule.

---

## 9.2 Database Field Alone

Adanya field:

```text
is_active
```

tidak otomatis berarti terdapat business rule:

```text
User can only access active records.
```

Behavior harus ditemukan dari evidence lain.

---

## 9.3 UI Alone

UI tidak otomatis menjadi source of truth terhadap backend behavior.

---

## 9.4 Legacy Behavior Alone

Behavior legacy tidak otomatis menjadi requirement sistem baru.

---

# 10. ID Convention

Stable artifact identity, domain-specific IDs, and their governing rules are defined by:

**Artifact & Metadata Convention**

See:

`ARTIFACT-METADATA-CONVENTION-v1.md`

The Master Contract remains authoritative for documentation governance; the convention provides the canonical artifact identity and metadata model.
---

# 11. ID Stability

ID bersifat immutable.

Jika:

```text
BR-014
```

sudah dibuat, ID tersebut tidak boleh berubah hanya karena document version berubah.

Example:

```text
v1.0 → BR-014
v1.1 → BR-014
v2.0 → BR-014
```

Jika rule sudah tidak berlaku, gunakan status:

```text
SUPERSEDED
```

Jangan recycle ID.

---

# 12. Document Status

Document lifecycle status, semantics, allowed values, transitions, ownership, and approval boundaries are governed by:

**Artifact & Metadata Convention**

See:

`ARTIFACT-METADATA-CONVENTION-v1.md`

The Master Contract does not maintain a second lifecycle vocabulary.

---

# 13. Document Metadata

Metadata structure, required fields, artifact identity, lifecycle status, ownership, versioning, and supersession rules are governed by:

**Artifact & Metadata Convention**

See:

`ARTIFACT-METADATA-CONVENTION-v1.md`

Every official document MUST comply with that convention.

# 14. Review Severity and Review Artifact

Review severity and finding semantics remain governed by this Master Contract. The structure, identity, target-version binding, finding registry, review result, gate-readiness record, and re-review structure of a Review Artifact are governed by:

**Review Artifact Convention**

See:

`REVIEW-ARTIFACT-CONVENTION-v1.md`

Baseline severity:

```text
CRITICAL
HIGH
MEDIUM
LOW
```

CRITICAL/HIGH findings block applicable review gates until resolved or otherwise explicitly handled under the human decision rules. MEDIUM/LOW follow the applicable gate rules.

---

# 15. Review Categories

Reviewer may use the established review categories, including:

```text
UNSUPPORTED_CLAIM
MISSING_EVIDENCE
WRONG_INTERPRETATION
MISSED_BEHAVIOR
CONTRADICTION
SCOPE_CONTRADICTION
BUSINESS_RULE_CONTRADICTION
MISSING_REQUIREMENT
AMBIGUOUS_REQUIREMENT
MISSING_EDGE_CASE
ACCEPTANCE_CRITERIA_GAP
DEPENDENCY_GAP
TRACEABILITY_GAP
DATA_MODEL_GAP
TERMINOLOGY_INCONSISTENCY
LEGACY_ASSUMPTION
IMPLEMENTATION_LEAK
OTHER
```

---

# 16. Reviewer Non-Rewrite Rule

Reviewer tidak boleh diam-diam memperbaiki document yang direview. Reviewer menghasilkan findings; target artifact direvisi oleh role/authority yang berwenang.

---

# 17. Review Finding Format and Lifecycle

Standard finding structure, Review Artifact structure, target version binding, finding registry, re-review linkage, review result, dan gate-readiness record are governed by `REVIEW-ARTIFACT-CONVENTION-v1.md`.

Every finding uses `REV-xxx` and the lifecycle:

```text
OPEN
IN_PROGRESS
RESOLVED
ACCEPTED
REJECTED
SUPERSEDED
```

Reviewer tidak boleh mengubah finding menjadi RESOLVED, ACCEPTED, atau REJECTED tanpa human decision atau verification yang sesuai. Findings tidak boleh dihapus dari historical review record.

---

# 18. Human Decision Convention

Human Decision artifact structure, identity, storage, authority boundary, lifecycle, supersession, and traceability are governed by:

**Human Decision Convention**

See:

HUMAN-DECISION-CONVENTION-v1.md

Official Human Decision menggunakan canonical artifact identity:

ART-xxx

Tidak ada HD-xxx sebagai identity canonical.

Human Decision harus dibedakan dari recommendation, review finding (REV-xxx), open question (OQ-xxx), conflict (CON-xxx), requirement, dan approval.

AI boleh menganalisis, menyajikan evidence, opsi, recommendation, dan draft decision artifact. AI tidak boleh menetapkan authoritative decision tanpa explicit human authority.

Human Decision menjadi authority tertinggi setelah decision ditetapkan oleh human authority yang berwenang sesuai workflow.

Decision artifact tidak otomatis mengubah downstream artifact; artifact terdampak harus direvisi dan direview melalui workflow yang berlaku.

---

# 19. Open Question & Conflict Convention

Open Question and Conflict artifact structure, storage, lifecycle, escalation, resolution authority, historical preservation, blocking behavior, and traceability are governed by:

**Open Question & Conflict Convention**

See:

`OPEN-QUESTION-CONFLICT-CONVENTION-v1.md`

The convention defines `ART-xxx` artifact identity with `OQ-xxx` / `CON-xxx` domain records. AI may identify and document unresolved matters, but may not silently resolve them.

---

# 20. Requirement Baseline Convention

Requirement candidate, baseline entry criteria, resolution flow, change control, blocking behavior, and the boundary between requirement authority and workflow resolution are governed by:

**Requirement Baseline Convention**

See:

`REQUIREMENT-BASELINE-CONVENTION-v1.md`

Core rule:

> Workflow boleh menemukan, mengklarifikasi, menguji, dan mengusulkan perubahan requirement. Workflow tidak boleh diam-diam mengubah requirement baseline.

Legacy behavior is evidence about the old system, not an automatic requirement for the new system. Model inference is not an authoritative requirement source.

A requirement may be treated as baseline only after the convention's source, traceability, review, ambiguity/conflict, human decision, and lifecycle criteria are satisfied.

Requirement IDs remain governed by the Artifact & Metadata Convention. Baseline requirements may use FR-xxx, NFR-xxx, or another applicable requirement domain ID.

Unresolved material OQ-xxx, CON-xxx, required human decisions, or required reviews block downstream use of the affected requirement. Review completion does not itself equal human approval.

Changes to a requirement baseline must use controlled revision and preserve stable identity/history according to the applicable conventions.

---

# 21. Universal Output Rules

Semua AI output harus:

1. menggunakan Markdown
2. menggunakan stable IDs
3. menyebutkan source/evidence
4. membedakan fact dan inference
5. mempertahankan UNKNOWN
6. mempertahankan CONFLICT
7. tidak mengarang requirement
8. tidak memasukkan implementation detail kecuali document memang secara eksplisit membutuhkannya
9. menjaga terminology tetap konsisten
10. menjaga traceability antar document

---

# 22. Requirement vs Implementation Boundary

Documentation phase mendefinisikan:

```text
WHAT
WHY
WHEN
WHO
RULES
EXPECTED BEHAVIOR
```

Documentation phase tidak mendefinisikan:

```text
HOW TO CODE IT
```

Contoh valid:

```text
User must complete the previous class before accessing the next class.
```

Contoh implementation leak:

```text
Create CourseProgressService::unlockNextClass().
```

---

# 23. Traceability

Requirement dan feature harus dapat ditelusuri dari source sampai data requirement.
Feature Mapping menjadi referensi utama untuk hubungan antara feature mapping entry dan PRD.
Setiap Feature Mapping entry menggunakan stable ID:

```text
FM-xxx
```

Untuk feature yang tidak berstatus REMOVE, Feature Mapping harus memiliki `Feature PRD` yang unique dan menunjuk ke PRD feature tersebut.

Contoh:

```text
FM-001
    ↓
Feature PRD: course-progress
    ↓
prd/course-progress.md
```

Contoh traceability requirement:

```text
Human Decision
    ↓
FM-001
    ↓
PRD
    ↓
BR-014
    ↓
FR-021
    ↓
AC-034
    ↓
DB-007
```

Traceability minimum:

```text
Business Rule
    ↓
PRD
    ↓
Functional Requirement
    ↓
Acceptance Criteria
    ↓
Database Requirement
```

Tidak semua requirement harus memiliki database entity.

---

# 24. Artifact-Based Handoff

Model tidak meneruskan conversation history sebagai primary context.

Handoff dilakukan melalui artifact dan context package yang didefinisikan oleh:

**Handoff Manifest Convention**

See:

`HANDOFF-MANIFEST-CONVENTION-v1.md`

Handoff identity menggunakan:

- `ART-xxx` untuk manifest artifact identity.
- `HOF-xxx` untuk handoff instance identity.

Role Contract tetap menentukan apa yang dilakukan receiver. Handoff Convention menentukan bounded context yang diteruskan.

---

# 25. Context Package

Untuk handoff antar model, gunakan context package sesuai Handoff Manifest Convention.

Baseline structure:

```text
handoff/
├── manifest.md
├── source/
├── target/
└── instructions.md
```

`manifest.md` adalah authoritative definition of the handoff package.

`instructions.md` tidak boleh override manifest atau governing contracts.

Copied files di dalam package adalah context snapshots, bukan source-of-truth artifacts baru, kecuali secara eksplisit diregistrasikan sebagai artifact.

---

# 26. Handoff Manifest

Setiap handoff WAJIB menggunakan manifest yang comply dengan:

`HANDOFF-MANIFEST-CONVENTION-v1.md`

Minimum manifest metadata:

```yaml
---
document: HANDOFF
artifact_id: ART-xxx
handoff_id: HOF-xxx
version: 1.0
status: DRAFT
owner: <role-or-authority>
from_role: <sender-role>
to_role: <receiver-role>
purpose: <handoff-purpose>
---
```

Manifest WAJIB mendefinisikan, sesuai applicability:

- source artifact registry
- target definition
- handoff purpose
- expected output
- in-scope / out-of-scope
- restrictions
- known open questions
- known conflicts
- review scope
- evidence boundary
- completion criteria
- context package structure

Manifest tidak memberikan approval authority.

`completion` tidak sama dengan approval.

---

# 27. Handoff Rules

Sender WAJIB:

* memberikan manifest dengan identity dan metadata yang valid
* meregistrasikan source menggunakan stable artifact IDs
* mendefinisikan target, purpose, expected output, dan applicable constraints
* mempertahankan known open questions dan conflicts
* menjaga evidence boundary dan completion criteria

Receiver WAJIB:

* membaca manifest sebelum memproses handoff
* membaca source artifacts yang diwajibkan
* membaca target artifact bila ada
* mengikuti Master Contract, Artifact & Metadata Convention, Handoff Manifest Convention, dan Role-Specific Contract yang applicable
* mematuhi scope dan restrictions
* mempertahankan unresolved questions dan conflicts
* menggunakan evidence sesuai evidence boundary
* tidak mengambil business decision atau approval authority yang tidak diberikan

Receiver tidak boleh menganggap source artifact selalu sempurna dan tidak boleh menyelesaikan conflicts secara diam-diam.

Handoff tidak boleh digunakan untuk mengubah role responsibility, business decision, approval authority, atau higher-authority contract.

---

# 28. Independent Review Rule

Jika menggunakan second-opinion model:

```text
Primary Review
```

dan:

```text
Independent Review
```

harus dilakukan secara independen.

Contoh:

```text
PRD
 ├────────→ Terra Review
 │
 └────────→ Gemini Review
```

Gemini tidak boleh diberikan hasil Terra terlebih dahulu.

Tujuannya untuk menghindari reviewer kedua hanya mengikuti reviewer pertama.

---

# 29. AI Model Role Matrix

| Role                   | Model                    | Primary Responsibility                  |
| ---------------------- | ------------------------ | --------------------------------------- |
| Researcher             | Claude Opus 4.6 Thinking | Reverse engineering                     |
| Document Architect     | GPT-5.6-terra            | Requirements/document construction      |
| Primary Critic         | GPT-5.6-terra-review     | Critical review                         |
| Second Opinion         | Gemini 3.1 Pro High      | Independent review                      |
| Document Worker        | Gemini 3.6 Flash Medium  | Formatting/normalization                |
| Coding-oriented models | Kiro models              | Reserved for later implementation phase |

---

# 30. Researcher Contract

**Prompt Title:**

```text
LMS Documentation — Legacy System Reverse Engineering Researcher
```

**Model:**

```text
Claude Opus 4.6 Thinking
```

Responsibilities:

* understand legacy behavior
* identify actors
* identify features
* identify flows
* identify authorization
* identify validation
* identify state transitions
* identify dependencies
* identify edge cases
* identify unknown behavior

Forbidden:

* PRD creation
* new architecture
* refactoring proposal
* implementation
* migration design

Primary output:

```text
analysis/existing-system.md
```

---

# 31. Existing System Reviewer Contract

**Prompt Title:**

```text
LMS Documentation — Existing System Evidence Reviewer
```

**Model:**

```text
GPT-5.6-terra-review
```

Responsibilities:

* verify evidence
* find unsupported claims
* find missed behavior
* find wrong interpretations
* identify contradictions
* identify false certainty

Output:

```text
review findings
```

Reviewer does not rewrite the analysis.

---

# 32. Feature Mapping Contract

**Prompt Title:**

```text
LMS Documentation — Legacy Feature Mapping Architect
```

**Model:**

```text
GPT-5.6-terra
```

Output:

```text
feature-map.md
```

**feature-map.md** adalah master reference untuk Feature Mapping dan hubungan feature dengan PRD.

Setiap Feature Mapping entry wajib memiliki stable ID:
```text
FM-xxx
```

Setiap FM-xxx merepresentasikan satu Feature Mapping entry.

Feature Mapping minimal menggunakan struktur:

```text
ID
Legacy Feature
Status
New Feature
Notes
Feature PRD
```

Contoh:
| ID     | Legacy Feature  | Status | New Feature     | Notes        | Feature PRD     |
| ------ | --------------- | ------ | --------------- | ------------ | --------------- |
| FM-001 | Course Progress | KEEP   | Course Progress | Core feature | course-progress |
| FM-002 | Payment         | REMOVE | —               | External     | —               |

`Feature PRD`

`Feature PRD` adalah nama/path PRD yang merepresentasikan feature tersebut.

`Feature PRD` harus unique.

Untuk feature yang tidak berstatus REMOVE, `Feature PRD` wajib menunjuk ke PRD yang sesuai.

Untuk feature dengan status:
```text
REMOVE
```

`Feature PRD` harus menggunakan:
```text
-
```

dan feature tersebut tidak menghasilkan PRD.

Nilai `Feature PRD` harus sesuai dengan nilai feature: pada metadata PRD terkait.

Contoh:

```text
---
document: prd
feature: course-progress
version: 1.0
status: DRAFT
---
```

direferensikan oleh:
```text
FM-001 → Feature PRD: course-progress
```
**feature-map.md** menjadi master reference untuk menentukan mapping feature dan PRD yang terkait.

Allowed decisions:

```text
KEEP
MODIFY
REPLACE
REMOVE
NEW
UNKNOWN
```

AI must not determine business priority without human input.

AI must not create a new feature based on opinion.

A **NEW** feature must originate from an explicit new requirement or human/project owner decision.

A feature mapping entry with status REMOVE must not generate a PRD.

---

# 33. Scope Contract

**Prompt Title:**

```text
LMS Documentation — Product Scope & Boundary Architect
```

**Model:**

```text
GPT-5.6-terra
```

Reviewer:

```text
Gemini 3.1 Pro High
```

Output:

```text
scope.md
```

Required sections:

```text
Purpose
Goals
Actors
In Scope
Out of Scope
High-Level Capabilities
Constraints
Assumptions
Open Questions
```

---

# 34. Business Rules Contract

**Prompt Title:**

```text
LMS Documentation — Business Rules Extraction & Definition
```

**Model:**

```text
Claude Opus 4.6 Thinking
```

Reviewer:

```text
GPT-5.6-terra-review
```

Output:

```text
business-rules.md
```

Each rule requires:

```text
BR-ID
Status
Source
Classification
Rule
Evidence
Affected Domains
Exceptions
Open Questions
```

---

# 35. PRD Contract

**Prompt Title:**

```text
LMS Documentation — Feature PRD Architect
```

**Primary Model:**

```text
GPT-5.6-terra
```

Escalation:

```text
Claude Opus 4.6 Thinking
```

Reviewer:

```text
GPT-5.6-terra-review
```

Required PRD sections:

```text
Feature
Purpose
Actors
Scope
Functional Requirements
User Flow
Business Rules
Edge Cases
Acceptance Criteria
Dependencies
Open Questions
Traceability
```

PRD harus merepresentasikan feature yang memiliki `Feature PRD` pada `feature-map.md`.

Nilai metadata:

```yaml
feature: <feature-prd>
```

harus sama dengan nilai `Feature PRD` pada Feature Mapping entry terkait.

Contoh:

```text
feature-map.md
FM-001 → Course Progress → course-progress
```

PRD:

```yaml
---
document: prd
feature: course-progress
version: 1.0
status: DRAFT
---
```

PRD tidak perlu menyimpan `FM-xxx` sebagai metadata tambahan.

Feature dengan status `REMOVE` tidak menghasilkan PRD.

---

# 36. Acceptance Criteria Contract

Acceptance criteria must be behaviorally testable.

Preferred format:

```markdown
### AC-001

**Given**
...

**When**
...

**Then**
...
```

Avoid:

```text
System works correctly.
```

Prefer:

```text
Given the user has completed Class 1
When the user opens Class 2
Then Class 2 becomes available for playback.
```

---

# 37. Edge Case Contract

Each significant feature must consider:

```text
normal flow
failure flow
boundary condition
unauthorized condition
invalid state
empty state
duplicate action
repeated action
```

AI should document edge cases only when supported by requirements, evidence, or reasonable explicit analysis.

Unknown behavior must remain `UNKNOWN`.

---

# 38. PRD Review Contract

**Prompt Title:**

```text
LMS Documentation — PRD Critical Reviewer
```

**Model:**

```text
GPT-5.6-terra-review
```

Review:

```text
PRD ↔ Scope
PRD ↔ Business Rules
PRD ↔ Existing System
PRD ↔ Other PRDs
FR ↔ AC
Edge Cases
Dependencies
Unknowns
```

Reviewer must not rewrite PRD.

---

# 39. Independent Requirements Auditor Contract

**Prompt Title:**

```text
LMS Documentation — Independent Requirements Auditor
```

**Model:**

```text
Gemini 3.1 Pro High
```

Purpose:

Identify blind spots independently from the primary reviewer.

Input:

```text
PRD
Scope
Business Rules
Related PRDs
```

The reviewer should not receive the primary review before completing its own analysis.

---

# 40. Cross-Feature Review Contract

**Prompt Title:**

```text
LMS Documentation — Cross-Feature Consistency Auditor
```

**Model:**

```text
GPT-5.6-terra-review
```

Review:

```text
PRD ↔ PRD
PRD ↔ Business Rules
PRD ↔ Scope
Feature lifecycle
Authorization
State transitions
Terminology
Dependencies
Data ownership
```

Output:

```text
cross-feature-review.md
```

Conflicts use:

```text
CON-xxx
```

---

# 41. Database Design Contract

**Prompt Title:**

```text
LMS Documentation — Requirements-Driven Database Architect
```

**Primary Model:**

```text
GPT-5.6-terra
```

Complex domain escalation:

```text
Claude Opus 4.6 Thinking
```

Reviewer:

```text
GPT-5.6-terra-review
```

Database design must originate from:

```text
Requirements
      ↓
Business Rules
      ↓
Data Requirements
      ↓
Entities
      ↓
Relationships
      ↓
Constraints
```

Not:

```text
Legacy Database
      ↓
Copy
      ↓
Rename
```

No migration or implementation is produced during this phase.

## 41.1 Database Review Contract

Database design wajib direview terhadap sumber requirement yang menjadi inputnya.

Review minimum mencakup:

```text
Database ↔ Requirements
Database ↔ Business Rules
Database ↔ PRD
Entities ↔ Relationships
Relationships ↔ Constraints
Data lifecycle
Nullable behavior
Uniqueness / integrity constraints
Traceability
Unsupported assumptions
Implementation leakage
```

Reviewer tidak boleh diam-diam mengubah database design. Review menghasilkan REV-xxx findings dan mengikuti Review Finding Lifecycle serta Universal Review Gate Rule.

Jika database design berubah setelah review, finding yang terdampak wajib diverifikasi melalui re-review sebelum gate dapat ditutup.

---

# 42. Final Documentation Audit Contract

**Prompt Title:**

```text
LMS Documentation — Final Requirements Consistency Auditor
```

Primary:

```text
GPT-5.6-terra-review
```

Deep audit:

```text
Claude Opus 4.6 Thinking
```

Optional independent audit:

```text
Gemini 3.1 Pro High
```

Final audit checks:

```text
Scope completeness
Feature completeness
Business rule coverage
PRD consistency
Cross-feature consistency
Acceptance criteria coverage
Edge case coverage
Database coverage
Traceability
Open questions
Unresolved conflicts
Implementation leakage
Unsupported assumptions
```

Final status:

```text
APPROVED
```

or:

```text
CHANGES_REQUIRED
```

---

# 43. Human Approval Gates

AI workflow memiliki mandatory human gates.

## Gate 1 — Existing System

```text
Legacy Analysis
      ↓
Review
      ↓
HUMAN APPROVAL
```

---

## Gate 2 — Scope

```text
Feature Map
      ↓
Scope
      ↓
HUMAN APPROVAL
```

---

## Gate 3 — Business Rules

```text
Business Rules
      ↓
Review
      ↓
HUMAN APPROVAL
```

---

## Gate 4 — PRDs

```text
PRDs
 ↓
Reviews
 ↓
HUMAN APPROVAL
```

---

## Gate 5 — Cross Feature

```text
Cross Feature Review
        ↓
HUMAN APPROVAL
```

---

## Gate 6 — Database

```text
Database Design
       ↓
Review
       ↓
HUMAN APPROVAL
```

---

## Gate 7 — Final Documentation

```text
Final Audit
     ↓
HUMAN APPROVAL
     ↓
DOCUMENTATION APPROVED
```

---

## 43.0 Universal Review Gate Rule

Setiap mandatory review gate harus memenuhi seluruh kondisi berikut:

```text
1. Required review completed
2. All review findings recorded using REV-xxx
3. Human resolution recorded for findings requiring decision
4. No unresolved CRITICAL findings
5. No unresolved HIGH findings
6. Required revisions have been re-reviewed
7. Document status is APPROVED
```

Jika salah satu kondisi tersebut belum terpenuhi:

```text
GATE = BLOCKED
```

Workflow tidak boleh melanjutkan ke stage berikutnya.

Human/project owner tetap memiliki authority untuk menentukan resolution, tetapi approval tidak boleh mengabaikan mandatory contract requirements.

### Gate Status

Setiap gate secara konseptual memiliki status:

```text
BLOCKED
READY_FOR_APPROVAL
APPROVED
```

READY_FOR_APPROVAL berarti seluruh review obligations telah terpenuhi dan document siap menunggu keputusan human.

APPROVED hanya dapat diberikan setelah human/project owner memberikan approval.

---
# 44. Escalation Rules

Complexity determines model escalation.

```text
LOW
↓
Gemini 3.6 Flash Medium

MEDIUM
↓
GPT-5.6-terra

HIGH
↓
Claude Opus 4.6 Thinking

CRITICAL / CONFLICT
↓
Multiple independent models
+
Human decision
```

Model escalation does not grant the model authority to make business decisions.

---

# 45. No Silent Assumption Rule

Jika model membutuhkan assumption untuk melanjutkan, model harus menandainya.

Allowed:

```markdown
**Assumption**
The existing system appears to treat X as Y.

**Confidence**
LOW

**Evidence**
...

**Status**
REQUIRES_VALIDATION
```

Not allowed:

```markdown
The system treats X as Y.
```

jika evidence tidak cukup.

---

# 46. Legacy vs New System Rule

Legacy system documentation harus menjawab:

```text
WHAT EXISTS
```

Product requirements harus menjawab:

```text
WHAT SHOULD EXIST
```

Keduanya tidak boleh dicampur.

Relationship:

```text
Legacy Analysis
       ↓
Feature Mapping
       ↓
Human Decision
       ↓
New Scope
       ↓
New Requirements
```

---

# 47. Terminology Rule

Terminology harus konsisten.

Jika project menetapkan:

```text
Course
Chapter
Class
```

AI tidak boleh berganti-ganti menjadi:

```text
Course
Module
Lesson
Session
```

tanpa explicit definition.

Jika terdapat legacy terminology berbeda, document harus menjelaskan mapping-nya.

Example:

```markdown
**Legacy Term:** Lesson

**New Project Term:** Class

**Mapping:** Lesson → Class

**Source:** HD-004
```

---

# 48. Versioning Rule

Document version mengikuti perubahan material.

Example:

```text
1.0
1.1
1.2
2.0
```

Minor revision:

* wording
* clarification
* documentation improvement

Major revision:

* business rule changes
* scope changes
* feature behavior changes
* data model changes

---

# 49. Supersession Rule

Jika document digantikan:

```yaml
---
status: SUPERSEDED
superseded_by: v2.0
---
```

Jangan menghapus historical documentation tanpa alasan.

Historical documents berguna untuk traceability.

---

# 50. Documentation Definition of Done

Documentation phase hanya dianggap selesai apabila:

```text
[ ] Legacy system behavior documented
[ ] Existing system reviewed
[ ] Feature map approved
[ ] Scope approved
[ ] Business rules approved
[ ] PRDs created
[ ] PRDs reviewed
[ ] Acceptance criteria complete
[ ] Edge cases documented
[ ] Cross-feature review complete
[ ] Conflicts resolved
[ ] Open questions resolved or explicitly accepted
[ ] Database design complete
[ ] Database design reviewed
[ ] Traceability verified
[ ] Final audit complete
[ ] No unresolved CRITICAL findings
[ ] No unresolved HIGH findings
[ ] Human/project owner approval obtained
```

---

# 51. Final Documentation Pipeline

```text
┌───────────────────────┐
│   LEGACY REPOSITORY   │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ OPUS RESEARCHER       │
│ Reverse Engineering   │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ existing-system.md    │
└───────────┬───────────┘
            ↓
┌───────────────────────┐
│ TERRA REVIEW          │
└───────────┬───────────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ TERRA ARCHITECT       │
│ Feature Mapping       │
└───────────┬───────────┘
            ↓
│ feature-map.md        │
│ scope.md              │
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ OPUS                   │
│ Business Rules        │
└───────────┬───────────┘
            ↓
│ business-rules.md     │
            ↓
┌───────────────────────┐
│ TERRA REVIEW          │
└───────────┬───────────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ TERRA                  │
│ PRD Architect         │
└───────────┬───────────┘
            ↓
│ prd/*.md              │
            ↓
      ┌─────┴─────┐
      ↓           ↓
TERRA REVIEW   GEMINI REVIEW
      └─────┬─────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ CROSS-FEATURE REVIEW  │
└───────────┬───────────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ DATABASE ARCHITECT    │
│ TERRA / OPUS          │
└───────────┬───────────┘
            ↓
│ database.md           │
            ↓
┌───────────────────────┐
│ DATABASE REVIEW       │
└───────────┬───────────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ FINAL AUDIT           │
│ TERRA + OPUS + GEMINI │
└───────────┬───────────┘
            ↓
       HUMAN GATE
            ↓
┌───────────────────────┐
│ DOCUMENTATION         │
│ APPROVED              │
└───────────────────────┘
```

---

# 52. Final Principle

Seluruh documentation workflow mengikuti prinsip:

> **AI discovers. AI analyzes. AI documents. AI reviews. Human decides.**

Dan:

> **No evidence → no fact.**

> **No human decision → no invented requirement.**

> **No approval → no source-of-truth status.**

> **No approved documentation → no implementation.**

---

# 53. Contract Status

```yaml
contract: AI-DOCUMENTATION-PROMPT-CONTRACT
version: 1.0
phase: DOCUMENTATION_ONLY
implementation_allowed: false
status: DRAFT
owner: PROJECT_OWNER
```
