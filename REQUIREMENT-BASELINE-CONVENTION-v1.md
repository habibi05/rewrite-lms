# REQUIREMENT BASELINE CONVENTION v1

**Document:** `REQUIREMENT-BASELINE-CONVENTION-v1.md`  
**Version:** `1.0`  
**Status:** `APPROVED`  
**Owner:** `PROJECT_OWNER`

---

## 1. Purpose

Convention ini mengunci batas antara **requirement candidate**, proses analisis/resolusi workflow, dan **requirement baseline**.

Tujuan utamanya adalah mencegah AI mengubah observasi legacy, inference, interpretasi, atau hasil workflow menjadi requirement authoritative tanpa source dan authority yang sah.

> **Workflow boleh menemukan, mengklarifikasi, menguji, dan mengusulkan perubahan requirement. Workflow tidak boleh diam-diam mengubah requirement baseline.**

---

## 2. Authority Boundary

Requirement authority mengikuti hierarchy pada Master Contract:

1. HUMAN DECISION
2. APPROVED PROJECT DOCUMENTS
3. EXPLICIT NEW REQUIREMENTS
4. LEGACY SYSTEM EVIDENCE
5. MODEL INFERENCE

Legacy evidence dan model inference **tidak otomatis menjadi requirement**.

Requirement hanya dapat menjadi baseline apabila source, authority, status, traceability, dan review yang diwajibkan telah terpenuhi.

---

## 3. Requirement States

Requirement dibedakan menjadi tiga kondisi konseptual:

### 3.1 Candidate

Requirement candidate adalah kandidat requirement yang ditemukan dari:

- explicit new requirement;
- human decision;
- approved project documentation;
- hasil analisis evidence;
- hasil review;
- resolusi OQ/CON.

Candidate belum authoritative dan tidak boleh diperlakukan downstream sebagai baseline.

### 3.2 Baseline

Requirement baseline adalah requirement yang telah memenuhi seluruh entry criteria dan boleh menjadi authoritative input bagi downstream specification.

Baseline harus memiliki stable domain ID sesuai Artifact & Metadata Convention, misalnya:

- `FR-xxx`
- `NFR-xxx`
- atau requirement domain ID lain yang berlaku.

### 3.3 Superseded / Deprecated

Requirement baseline yang tidak lagi berlaku tidak boleh dihapus atau ID-nya digunakan ulang.

Gunakan lifecycle/status yang berlaku pada Artifact & Metadata Convention, termasuk `SUPERSEDED` atau `DEPRECATED` sesuai konteks.

---

## 4. Source Rules

Setiap candidate WAJIB memiliki source classification.

### 4.1 Human Decision

Human Decision adalah authority untuk keputusan bisnis, scope, behavior, conflict resolution, dan ambiguity yang membutuhkan keputusan manusia.

Decision artifact menggunakan canonical `ART-xxx`.

### 4.2 Explicit New Requirement

Requirement yang diberikan secara eksplisit oleh project owner dapat menjadi candidate dengan classification `REQUIREMENT`.

Jika wording atau intent masih ambigu, candidate tidak boleh dipaksa menjadi baseline; buat atau tautkan `OQ-xxx` sesuai convention.

### 4.3 Approved Documentation

Approved project artifacts dapat menjadi source requirement apabila artifact tersebut memang authoritative untuk requirement terkait.

Draft/review artifact tidak boleh diperlakukan sebagai final requirement authority hanya karena isinya terlihat meyakinkan.

### 4.4 Legacy Evidence

Legacy behavior menjawab:

> Apa yang dilakukan sistem lama?

Legacy behavior tidak otomatis menjawab:

> Apa yang harus dilakukan sistem baru?

Legacy evidence boleh menjadi evidence pendukung candidate, tetapi **tidak boleh sendirian mengangkat requirement baru menjadi baseline**.

### 4.5 Model Inference

Model inference boleh membantu menemukan candidate, gap, atau rekomendasi.

Inference tidak boleh menjadi authoritative requirement source.

---

## 5. Candidate Registration

Setiap material candidate harus dapat ditelusuri ke:

- source;
- evidence atau decision;
- classification;
- affected scope/feature;
- related OQ/CON/REV bila ada.

Candidate yang belum cukup jelas harus tetap ditandai sebagai candidate/UNKNOWN dan tidak dipromosikan ke baseline.

---

## 6. Baseline Entry Criteria

Requirement hanya boleh masuk baseline apabila:

- source authority dapat diidentifikasi;
- requirement statement cukup jelas untuk downstream use;
- tidak terdapat unresolved ambiguity yang material;
- tidak terdapat unresolved conflict yang memengaruhi requirement;
- required human decision sudah dicatat bila diperlukan;
- traceability ke source tersedia;
- applicable review telah selesai;
- required findings telah ditangani sesuai Review Artifact Convention;
- scope dan terminology konsisten dengan approved artifacts;
- requirement tidak merupakan implementation detail yang melanggar documentation boundary.

Jika salah satu kondisi material belum terpenuhi, requirement tetap candidate atau BLOCKED.

---

## 7. Resolution Workflow

Baseline flow:

`text
Requirement Candidate
        ↓
Evidence / Source Analysis
        ↓
Ambiguity or Conflict?
   ┌────┴────┐
  YES       NO
   ↓         ↓
OQ / CON   Review
   ↓         ↓
Human      Candidate
Decision    Validation
   ↓         ↓
Revision / Resolution
        ↓
Requirement Baseline
        ↓
PRD / BR / AC / DB
`

Workflow tidak boleh melewati OQ/CON atau human decision yang diwajibkan hanya untuk membuat downstream document terlihat complete.

---

## 8. Open Questions

Jika requirement intent belum dapat dipastikan, gunakan `OQ-xxx`.

AI boleh:

- mengidentifikasi ambiguity;
- menyusun pertanyaan;
- mengumpulkan evidence;
- menyajikan opsi;
- membuat recommendation.

AI tidak boleh mengubah recommendation menjadi requirement baseline tanpa authority yang diperlukan.

Resolusi harus ditautkan ke decision artifact atau source authoritative yang sesuai.

---

## 9. Conflicts

Jika sumber requirement atau evidence bertentangan, gunakan `CON-xxx`.

AI tidak boleh memilih salah satu sisi secara diam-diam.

Conflict yang material harus memiliki resolution authority yang sah sebelum requirement yang terdampak dapat masuk baseline.

Jika resolution menghasilkan requirement baru atau perubahan requirement, affected requirement harus direvisi dan direview kembali sesuai workflow.

---

## 10. Review Relationship

Review finding menggunakan `REV-xxx`.

Review dapat menyatakan requirement:

- unsupported;
- ambiguous;
- contradictory;
- incomplete;
- inconsistent;
- implementation-leaking.

Reviewer menghasilkan finding dan tidak mengambil alih authority project owner.

Resolution finding tidak otomatis berarti requirement telah approved sebagai baseline. Baseline tetap membutuhkan entry criteria convention ini.

---

## 11. Requirement Changes After Baseline

Requirement baseline dapat berubah hanya melalui controlled revision.

Perubahan harus:

1. mempertahankan stable requirement ID bila identity requirement tetap sama;
2. mencatat perubahan versi artifact yang relevan;
3. menjaga traceability ke source/decision;
4. mengevaluasi downstream impact;
5. menjalani review yang diwajibkan;
6. menggunakan `SUPERSEDED` bila requirement lama digantikan oleh requirement baru yang secara substantif berbeda.

AI tidak boleh menghapus, mengganti, atau melemahkan baseline secara diam-diam.

---

## 12. Downstream Traceability

Baseline requirement menjadi input untuk specification berikutnya.

Minimum conceptual chain:

`text
Source / Human Decision
        ↓
Requirement Baseline
        ↓
PRD
        ↓
Business Rule
        ↓
Acceptance Criteria
        ↓
Database Requirement
`

Tidak semua requirement harus berujung pada database entity.

Setiap downstream artifact harus dapat menunjukkan requirement source yang mendasarinya apabila applicable.

---

## 13. Blocking Rules

Downstream work harus berstatus `BLOCKED` apabila membutuhkan requirement yang:

- masih candidate dan belum eligible sebagai baseline;
- memiliki unresolved material OQ;
- memiliki unresolved material CON;
- membutuhkan human decision yang belum tersedia;
- gagal required review;
- tidak memiliki traceability yang diwajibkan.

AI tidak boleh mengubah `BLOCKED` menjadi `READY` atau `APPROVED` melalui assumption.

---

## 14. AI Prohibition

AI DILARANG:

- menciptakan requirement baru hanya karena legacy behavior ada;
- mengubah inference menjadi requirement tanpa source authority;
- mengisi requirement ambiguity dengan preferensi model;
- memilih conflict resolution secara autonomous;
- menghapus requirement baseline tanpa controlled change;
- menyatakan requirement baseline hanya karena PRD sudah ditulis;
- menganggap review pass sebagai human approval;
- menganggap completion workflow sebagai approval.

AI BOLEH menganalisis dan merekomendasikan, tetapi authority tetap berada pada source dan human governance yang berlaku.

---

## 15. Relationship to Other Conventions

Convention ini bekerja bersama:

- `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md` — governance dan authority;
- `ARTIFACT-METADATA-CONVENTION-v1.md` — identity, metadata, lifecycle;
- `OPEN-QUESTION-CONFLICT-CONVENTION-v1.md` — unresolved uncertainty/conflict;
- `HUMAN-DECISION-CONVENTION-v1.md` — authoritative human decisions;
- `REVIEW-ARTIFACT-CONVENTION-v1.md` — review structure dan findings;
- `LMS-REWRITE-DOCUMENTATION-WORKFLOW.md` — process dan sequencing.

Jika terdapat conflict, higher-authority contract tetap berlaku.

---

## 16. Definition of Done

Requirement dapat dianggap baseline-ready hanya apabila:

- [ ] source authority teridentifikasi;
- [ ] stable requirement ID valid;
- [ ] requirement statement jelas;
- [ ] evidence/decision traceability tersedia;
- [ ] material OQ/CON telah resolved atau explicitly handled;
- [ ] required human decision tersedia;
- [ ] required review selesai;
- [ ] downstream impact diketahui;
- [ ] tidak ada unsupported assumption yang diperlakukan sebagai requirement;
- [ ] status artifact sesuai lifecycle convention.

---

## 17. Governing Principle

> **Observe → Classify → Clarify → Decide when required → Review → Baseline → Specify.**

Requirement baseline adalah hasil governance yang dapat ditelusuri, bukan hasil improvisasi AI.
