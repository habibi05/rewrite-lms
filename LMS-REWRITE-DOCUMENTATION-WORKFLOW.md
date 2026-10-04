# LMS Rewrite — Documentation Workflow

## 1. Tujuan

Workflow ini digunakan untuk melakukan **rewrite project LMS lama dengan bantuan AI**, tetapi seluruh proses **dokumentasi dan requirement harus selesai serta direview terlebih dahulu sebelum masuk ke tahap coding**.

AI digunakan sebagai:

* Reverse engineer
* Business analyst
* Document architect
* Reviewer
* Second opinion

AI **tidak mengambil keputusan bisnis secara mandiri**.

Keputusan final mengenai scope, behavior, business rules, dan requirement tetap berada pada project owner.

---

# 2. Prinsip Utama

### 2.1 Legacy code bukan blueprint

Source code lama digunakan sebagai **referensi untuk memahami sistem yang sudah berjalan**, bukan sebagai blueprint untuk sistem baru.

Tujuannya adalah:

> Mengambil business knowledge yang masih dibutuhkan dan membuang kompleksitas, fitur, serta implementasi lama yang tidak diperlukan.

---

### 2.2 Separate "Existing" dan "Desired"

Sistem lama dan sistem baru harus dipisahkan secara eksplisit.

```text
OLD SYSTEM
"What does the existing application actually do?"
        ↓
existing-system.md
        ↓
NEW SYSTEM
"What do we actually want?"
        ↓
scope.md
        ↓
PRD
```

Dengan demikian AI tidak menganggap semua behavior pada sistem lama sebagai requirement sistem baru.

---

### 2.3 AI tidak boleh mengubah ambiguity menjadi asumsi

Jika AI menemukan:

* `UNKNOWN`
* `AMBIGUOUS`
* `CONFLICT`

AI harus menandainya dan meminta keputusan dari project owner.

AI boleh memberikan rekomendasi, tetapi keputusan final tetap dilakukan oleh project owner.

---

### 2.4 Dokumentasi harus menjadi source of truth

Setelah disetujui, dokumen requirement menjadi referensi utama untuk tahap berikutnya.

Source code lama tidak lagi menjadi sumber requirement utama.

---

### 2.5 Review Finding dan Gate Enforcement

Setiap official review menggunakan Review Artifact yang mengikuti `REVIEW-ARTIFACT-CONVENTION-v1.md` dan memiliki stable artifact identity `ART-xxx`. Review findings di dalamnya menggunakan stable finding ID:

```text
REV-xxx
```

Reviewer tidak memperbaiki document secara langsung.

Flow review:

```text
Document
   ↓
Reviewer
   ↓
REV-xxx Findings
   ↓
Human Decision
   ↓
Document Revision
   ↓
Re-review
   ↓
Gate
```

Sebuah stage tidak dapat melewati gate apabila masih terdapat unresolved blocking findings.

Blocking findings adalah:

```text
CRITICAL
HIGH
```

MEDIUM dan LOW harus memiliki explicit human resolution sebelum gate ditutup.

Jika document berubah setelah review, finding yang terdampak harus diverifikasi kembali.

Approval tidak menghapus atau mengabaikan review findings.

---

# 3. Documentation Workflow

```text
                    LEGACY LMS
                        │
                        ▼
             ┌─────────────────────┐
             │ 1. REVERSE          │
             │    ENGINEERING      │
             └──────────┬──────────┘
                        ▼
               existing-system.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 2. FEATURE          │
             │    MAPPING          │
             └──────────┬──────────┘
                        ▼
                 feature-map.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 3. DEFINE SCOPE     │
             └──────────┬──────────┘
                        ▼
                    scope.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 4. BUSINESS RULES   │
             └──────────┬──────────┘
                        ▼
              business-rules.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 5. PRD PER FEATURE  │
             └──────────┬──────────┘
                        ▼
                    prd/*.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 6. CROSS-FEATURE    │
             │    REVIEW           │
             └──────────┬──────────┘
                        ▼
                  REVIEW / FIX
                        │
                        ▼
             ┌─────────────────────┐
             │ 7. DATABASE DESIGN  │
             └──────────┬──────────┘
                        ▼
                  database.md
                        │
                        ▼
             ┌─────────────────────┐
             │ 8. FINAL            │
             │    CONSISTENCY      │
             │    REVIEW           │
             └──────────┬──────────┘
                        ▼
              DOCUMENTATION APPROVED
```

---

# 4. Stage 1 — Reverse Engineering

## Objective

Menjawab:

> "Project LMS lama ini sebenarnya melakukan apa?"

AI menganalisis source code lama untuk menemukan behavior yang benar-benar terjadi.

## Output

```text
analysis/
└── existing-system.md
```

## Isi

Dokumen harus menjelaskan:

* Existing features
* Existing user roles
* Existing workflows
* Existing business behavior
* Existing data relationships
* Existing validation
* Existing authorization
* Existing integrations
* Existing edge cases yang ditemukan

Setiap informasi penting harus menggunakan **Evidence Classification** yang sama dengan AI Documentation Prompt Contract.

Allowed classifications:

```text
FACT
DERIVED
REQUIREMENT
DECISION
UNKNOWN
CONFLICT
```

Untuk hasil analysis, `Confidence` dapat digunakan sebagai metadata tambahan dengan nilai:

```text
HIGH
MEDIUM
LOW
```

`Confidence` tidak menggantikan `Classification` dan tidak menjadi bukti.

AI tidak boleh mengubah `DERIVED` menjadi `FACT`, atau `UNKNOWN`/`CONFLICT` menjadi classification lain, tanpa evidence atau human decision yang sesuai.

## Gate

Project owner melakukan review:

> "Apakah dokumentasi ini benar-benar menggambarkan sistem lama?"

Jika tidak, kembali ke reverse engineering.

---

# 5. Stage 2 — Feature Mapping

## Objective

Menentukan fitur legacy mana yang akan dibawa ke sistem baru.

## Output

```text
feature-map.md
```

## Feature Mapping Entry

Setiap feature mapping entry wajib memiliki stable ID:

```text
FM-xxx
```

`FM-xxx` merepresentasikan satu Feature Mapping entry.

`feature-map.md` menjadi master reference untuk seluruh Feature Mapping dan hubungan feature dengan PRD.

Setiap Feature Mapping entry menggunakan struktur:

```text
ID
Legacy Feature
Status
New Feature
Notes
Feature PRD
```

## Status Feature

Setiap feature dapat memiliki status:

```text
KEEP
MODIFY
REPLACE
REMOVE
NEW
```

## Feature PRD

Feature yang tidak berstatus `REMOVE` harus memiliki `Feature PRD`.

`Feature PRD` berisi nama/path PRD dan harus unique.

Untuk feature dengan status:

```text
REMOVE
```

`Feature PRD` menggunakan:

```text
-
```

dan feature tersebut tidak menghasilkan PRD.

Contoh:

| ID     | Legacy Feature  | Status | New Feature     | Notes           | Feature PRD     |
| ------ | --------------- | ------ | --------------- | --------------- | --------------- |
| FM-001 | Course Progress | KEEP   | Course Progress | Core feature    | course-progress |
| FM-002 | Chapter         | KEEP   | Chapter         | Core feature    | chapter         |
| FM-003 | Payment         | REMOVE | —               | External system | —               |
| FM-004 | Certificate     | MODIFY | Certificate     | Simplified      | certificate     |
| FM-005 | New Reporting   | NEW    | Reporting       | New requirement | reporting       |


## Gate

Project owner menentukan:

> "Fitur apa saja yang benar-benar masuk ke sistem baru?"

---

# 6. Stage 3 — Define Scope

## Objective

Menentukan batas sistem baru.

## Output

```text
scope.md
```

## Isi

### Goal

Tujuan utama aplikasi.

### In Scope

Fitur yang memang harus tersedia.

### Out of Scope

Fitur yang secara eksplisit tidak akan dibuat.

### Actors

Role/user yang berinteraksi dengan sistem.

### High-Level Capabilities

Kemampuan utama sistem tanpa detail implementasi.

Contoh:

```text
Authentication
Course Management
Learning
Enrollment
Progress Tracking
Attendance
Certificate
```

## Gate

Project owner melakukan approval:

> "Apakah ini benar-benar aplikasi yang ingin dibangun?"

---

# 7. Stage 4 — Business Rules

## Objective

Mendefinisikan aturan bisnis yang berlaku pada sistem baru.

## Output

```text
business-rules.md
```

Setiap business rule memiliki ID.

Contoh:

```text
BR-001
Student must be enrolled before accessing a course.

BR-002
A locked class cannot be accessed.

BR-003
A completed class remains accessible.

BR-004
Completing the final required class completes the course.
```

Business rules dapat berasal dari:

* Existing system
* Requirement baru
* Keputusan project owner
* Perubahan behavior dari legacy system

Business rule baru tidak boleh dianggap berasal dari legacy hanya karena AI menganggapnya masuk akal.

## Gate

Project owner melakukan review terhadap seluruh business rules.

---

# 8. Stage 5 — PRD per Feature

## Objective

Mendokumentasikan requirement setiap feature secara terpisah.

## Output

```text
prd/
├── authentication.md
├── course.md
├── chapter.md
├── class.md
├── enrollment.md
├── course-progress.md
└── ...
```

## Struktur PRD

Setiap PRD minimal memiliki:

1. Feature
2. Purpose
3. Actors
4. Description
5. User Flow
6. Business Rules
7. Edge Cases
8. Acceptance Criteria

Setiap PRD harus merepresentasikan feature yang memiliki `Feature PRD` pada `feature-map.md`.

Nilai metadata `feature:` pada PRD harus sama dengan nilai `Feature PRD` pada Feature Mapping entry terkait.

Contoh:
```text
feature-map.md

FM-001 | Course Progress | KEEP | Course Progress | Core feature | course-progress
```

maka PRD:
```text
prd/course-progress.md
```

dengan metadata:
```yaml
---
document: prd
feature: course-progress
version: 1.0
status: DRAFT
---
```

`feature-map.md` menjadi master reference untuk menentukan feature dan PRD yang terkait.

Feature dengan status `REMOVE` tidak menghasilkan PRD.

PRD harus mereferensikan business rules yang relevan.

Contoh:

```text
Business Rules:
- BR-001
- BR-002
- BR-003
```

Acceptance criteria juga dapat diberi ID:

```text
AC-001
AC-002
AC-003
```

## Prinsip

PRD menjelaskan:

> **Apa yang sistem harus lakukan.**

PRD tidak menjelaskan implementasi teknis secara detail.

Contoh yang tidak perlu berada di PRD:

```text
Laravel Model
Repository
Service
Controller
Redis
JSON column
Specific migration implementation
```

## PRD Review

Setiap PRD wajib menjalani review sesuai **PRD Review Contract** pada AI Documentation Prompt Contract.

Review minimum mencakup:

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

Reviewer tidak boleh rewrite PRD secara langsung. Review menghasilkan REV-xxx findings dan mengikuti Review Finding Lifecycle serta Universal Review Gate Rule dari Contract.

Jika terdapat perubahan pada PRD setelah review, finding yang terdampak wajib diverifikasi melalui re-review sebelum gate dapat ditutup.

## Gate

Gate PRD mengikuti status gate universal:

```text
BLOCKED
READY_FOR_APPROVAL
APPROVED
```

Gate hanya dapat menjadi READY_FOR_APPROVAL jika required PRD review selesai, findings tercatat, human resolution telah diberikan untuk findings yang membutuhkan keputusan, tidak ada unresolved CRITICAL/HIGH, dan required revisions telah di-re-review.

APPROVED hanya diberikan setelah project owner memberikan human approval.

---

# 9. Stage 6 — Cross-Feature Review

## Objective

Memastikan seluruh PRD konsisten satu sama lain.

## Input

```text
scope.md
business-rules.md
prd/*.md
```

## Reviewer mencari

```text
CONTRADICTION
MISSING REQUIREMENT
AMBIGUITY
DUPLICATION
UNDEFINED BEHAVIOR
EDGE CASE
```

## Output

```text
reviews/
└── cross-feature-review.md
```

Contoh Review Finding:

```text
REV-001

Severity: HIGH

Category: CONTRADICTION

Affected ID:
- PRD-Course
- PRD-Course-Progress

Claim:
Course can be deleted.

Evidence:
...

Problem:
Course deletion behavior is not defined for course progress records.

Required Resolution:
Project owner must define the expected lifecycle behavior.

Status:
OPEN
```

Reviewer tidak boleh menyelesaikan ambiguity secara diam-diam.

## Gate

Project owner menentukan resolution setiap REV-xxx.

Stage tidak boleh dianggap selesai selama masih terdapat:

- unresolved CRITICAL finding
- unresolved HIGH finding

Untuk MEDIUM dan LOW, finding harus memiliki explicit human resolution.

Jika resolution menghasilkan perubahan pada document, document wajib kembali melalui review yang relevan sebelum gate dapat ditutup.

## Gate

Project owner menentukan resolution setiap issue.

---

# 10. Stage 7 — Database Design

## Objective

Mendesain struktur database berdasarkan requirement yang sudah stabil.

## Input

```text
scope.md
business-rules.md
prd/*.md
```

## Output

```text
database.md
```

## Isi

* Entities
* Columns
* Data types/concepts
* Relationships
* Constraints
* Uniqueness
* Nullable behavior
* Data lifecycle
* Referential relationships
* Important indexes where applicable

Database design belum berupa Laravel migration.

Belum ada:

```php
Schema::create(...)
```

Database design harus menjawab:

> "Data apa yang dibutuhkan untuk mendukung requirement dan business rules?"

## Database Review

Database design wajib menjalani review sesuai **Database Review Contract** pada AI Documentation Prompt Contract.

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

Reviewer tidak boleh mengubah database design secara langsung. Review menghasilkan REV-xxx findings dan mengikuti Review Finding Lifecycle.

Jika database design berubah setelah review, finding yang terdampak wajib diverifikasi melalui re-review.

## Gate

Database gate mengikuti Universal Review Gate Rule:

```text
BLOCKED
READY_FOR_APPROVAL
APPROVED
```

Gate hanya dapat menjadi READY_FOR_APPROVAL jika required database review selesai, findings tercatat, human resolution telah diberikan untuk findings yang membutuhkan keputusan, tidak ada unresolved CRITICAL/HIGH, dan required revisions telah di-re-review.

APPROVED hanya diberikan setelah project owner memberikan human approval.

---

# 11. Stage 8 — Final Consistency Review

## Objective

Memastikan seluruh documentation package konsisten sebelum dianggap final.

## Input

```text
scope.md
feature-map.md
business-rules.md
prd/*.md
database.md
```

## Review Matrix

### Scope ↔ PRD

Apakah seluruh scope memiliki requirement yang sesuai?

### Business Rules ↔ PRD

Apakah seluruh business rule direpresentasikan oleh PRD?

### PRD ↔ PRD

Apakah ada konflik antar feature?

### PRD ↔ Database

Apakah seluruh data yang dibutuhkan dapat direpresentasikan?

### Database ↔ Business Rules

Apakah database mendukung aturan bisnis dan data lifecycle?

## Output

```text
reviews/
└── final-review.md
```

## Final Documentation Audit

Stage 8 wajib menjalankan **Final Documentation Audit Contract** pada AI Documentation Prompt Contract.

Final audit minimum mencakup:

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

Final audit menghasilkan status audit:

```text
APPROVED
CHANGES_REQUIRED
```

Reviewer tidak boleh memperbaiki document secara langsung. Setiap issue harus dicatat sebagai `REV-xxx` dan mengikuti Review Finding Lifecycle pada Contract.

Jika terdapat perubahan pada document setelah final audit, finding yang terdampak wajib diverifikasi melalui re-review sebelum gate dapat ditutup.

### Final Audit Gate

Final audit menggunakan Universal Review Gate Rule pada Contract dengan status:

```text
BLOCKED
READY_FOR_APPROVAL
APPROVED
```

Jika final audit menghasilkan `CHANGES_REQUIRED`, atau masih terdapat unresolved CRITICAL/HIGH findings, gate berstatus `BLOCKED` dan documentation package tidak boleh dinyatakan approved.

Gate dapat menjadi `READY_FOR_APPROVAL` hanya jika:

- final audit selesai;
- seluruh findings tercatat menggunakan `REV-xxx`;
- human resolution telah diberikan untuk findings yang membutuhkan keputusan;
- tidak ada unresolved CRITICAL/HIGH findings;
- required revisions telah di-re-review.

`APPROVED` hanya diberikan setelah project owner memberikan human approval. Status `APPROVED` pada final audit tidak menggantikan human approval.

---

# 12. Final Documentation Structure

Setelah seluruh tahap selesai, struktur canonical repository adalah relative terhadap repository root (./).

> Catatan: repository `rewrite-lms` ditempatkan di dalam folder `docs/` milik legacy project. Karena itu, `docs/` adalah konteks filesystem legacy, bukan subdirectory di dalam repository ini.

```text
./
│
├── analysis/
│   └── existing-system.md
│
├── scope.md
├── feature-map.md
├── business-rules.md
├── database.md
│
├── prd/
│   ├── authentication.md
│   ├── course.md
│   ├── chapter.md
│   ├── class.md
│   ├── enrollment.md
│   ├── course-progress.md
│   └── ...
│
└── reviews/
    ├── cross-feature-review.md
    └── final-review.md
```

---

# 13. Approval Model

AI tidak menjadi decision maker.

Workflow menggunakan konsep:

```text
AI
 ↓
Analyze
 ↓
Propose
 ↓
Review
 ↓
Project Owner
 ↓
Approve / Reject / Modify
```

Project owner adalah pihak yang menentukan:

* Scope
* Feature selection
* Business behavior
* Business rules
* Ambiguous requirements
* Conflict resolution
* Final database requirements

---

# 14. Documentation Loop

Workflow tidak harus selalu linear.

Jika sebuah tahap menemukan masalah pada tahap sebelumnya, proses boleh kembali.

Contoh:

```text
Database Design
      ↓
Requirement ambiguity discovered
      ↓
PRD revision
      ↓
Business Rule revision
      ↓
Database revision
```

Prinsipnya:

> Jangan memperbaiki ambiguity dengan asumsi.

Jika requirement belum jelas, kembali ke sumber requirement dan selesaikan secara eksplisit.

---

# 15. Definition of Done

Fase dokumentasi dianggap selesai apabila:

* [ ] Existing system sudah terdokumentasi
* [ ] Legacy feature sudah dipetakan
* [ ] Scope sudah ditentukan
* [ ] Out-of-scope sudah jelas
* [ ] Business rules sudah didefinisikan
* [ ] Setiap feature yang dipilih memiliki PRD
* [ ] PRD sudah memiliki acceptance criteria
* [ ] Cross-feature review sudah selesai
* [ ] Seluruh ambiguity sudah diselesaikan
* [ ] Database design sudah dibuat
* [ ] Database sudah direview terhadap PRD
* [ ] Final consistency review sudah selesai
* [ ] Seluruh dokumen sudah disetujui project owner

---

# 16. Boundary Fase Dokumentasi

Fase ini **tidak melakukan coding**.

Tidak ada:

```text
Laravel implementation
Migration
Controller
Model
Service
Repository
API implementation
Frontend implementation
Unit test implementation
Deployment
```

Semua hal tersebut baru dibahas **setelah documentation package dinyatakan approved**.

---



## Human Decision Storage

Seluruh Human Decision yang menjadi keputusan authoritative WAJIB direkam sebagai Decision Artifact sesuai HUMAN-DECISION-CONVENTION-v1.md.

Decision artifact menggunakan ART-xxx dan disimpan pada decisions/. Tidak ada HD-xxx sebagai identity canonical.

Flow:

    REV-xxx / OQ-xxx / CON-xxx
                ↓
        Human Decision ART-xxx
                ↓
        Document Revision
                ↓
          Re-review / Gate

Human Decision tidak sama dengan approval. Approval tetap mengikuti gate dan authority yang berlaku.

# 17. Core Principle

> **Understand → Decide → Specify → Review → Approve → Only Then Build**

Legacy code memberi kita pengetahuan tentang sistem lama.

PRD dan business rules mendefinisikan sistem baru.

Database design menerjemahkan requirement menjadi struktur data.

Project owner menjadi final decision maker.

AI berfungsi sebagai partner analisis, dokumentasi, dan review — bukan sebagai pengambil keputusan bisnis.