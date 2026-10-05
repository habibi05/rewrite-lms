---
document: PROMPT
artifact_id: PROMPT-REV-ART-001
version: 1.0
status: DRAFT
owner: PROJECT_OWNER
prompt_type: TARGETED_ARTIFACT_REVISION
target_artifact: ART-001
target_version: 1.0
target_output_version: 1.1
review_artifact: ART-002
---

# Revision Prompt Contract — ART-001 v1.0 → v1.1

## 1. Purpose

Prompt ini digunakan khusus untuk merevisi **Existing System Analysis artifact ART-001 v1.0** berdasarkan findings pada **Review Artifact ART-002 v1.0**.

Tujuan revisi adalah memperbaiki ketepatan evidence, evidence classification, traceability, reachability, flow reconstruction, dan wording pada ART-001 tanpa mengubahnya menjadi requirement, desain future-state, atau keputusan bisnis baru.

Prompt ini **bukan** prompt reverse engineering baru dan **bukan** prompt untuk melakukan approval.

---

## 2. Immutable Target

Target input wajib:

- Artifact ID: `ART-001`
- Version: `1.0`
- Document: `ANALYSIS`
- Path: `analysis/existing-system.md`
- Review Artifact: `ART-002`
- Review Version: `1.0`
- Findings yang wajib ditangani: `REV-001` sampai `REV-012`

Target output:

- Artifact ID: `ART-001`
- Version: `1.1`
- Path: `analysis/existing-system.md`
- Status: `DRAFT`

**Jangan membuat ART-002 baru. Jangan membuat artifact Existing System baru. Jangan mengganti ART-001 menjadi ART-003.**

---

## 3. Governance Preconditions

Sebelum melakukan revisi, baca dan pahami minimal:

1. `ARTIFACT-METADATA-CONVENTION-v1.md`
2. `REVIEW-ARTIFACT-CONVENTION-v1.md`
3. `ROLE-SPECIFIC-CONTRACT-REVERSE-ENGINEERING-RESEARCHER.md`
4. `reviews/REVIEW-ART-001-existing-system.md`
5. `analysis/existing-system.md`

Jika salah satu governance artifact wajib atau Review Artifact ART-002 tidak tersedia, **BLOCK** dan jangan melakukan revisi substantif.

---

## 4. Revision Authority

Satu-satunya sumber perubahan yang diwajibkan oleh prompt ini adalah:

- findings `REV-001` sampai `REV-012` pada ART-002;
- evidence legacy yang dapat diverifikasi;
- governance conventions yang berlaku.

Reviewer findings adalah instruksi perbaikan kualitas dokumentasi, **bukan requirement baru**.

Jika sebuah finding tidak dapat diselesaikan karena evidence tidak tersedia atau tidak cukup, jangan mengarang evidence. Gunakan `UNKNOWN`, `CONFLICT`, atau batasan evidence yang sesuai.

---

## 5. Core Principles

Selama revisi, wajib mempertahankan prinsip berikut:

1. **No evidence → no fact.**
2. **Existence ≠ active behavior.**
3. **Existence ≠ reachability.**
4. **Code/package/schema presence ≠ actual runtime usage.**
5. **Inference must be explicitly classified as DERIVED.**
6. **Insufficient evidence must remain UNKNOWN.**
7. **Contradictory evidence must remain CONFLICT until resolved by evidence.**
8. Legacy behavior is documented as evidence of the existing system; it is not automatically a requirement for the rewrite.
9. Jangan membuat future-state requirement, architecture, database design, API contract, UI design, atau implementation decision.
10. Jangan mengubah business decision yang belum diputuskan manusia.

---

## 6. Required Revision Handling

### REV-001 — Unsupported feature claims / evidence classification

Review dan revisi seluruh feature/module claims yang terlalu luas.

Pisahkan secara eksplisit:

- structural existence;
- behavioral evidence;
- reachability/activity;
- derived interpretation;
- unknown;
- conflict.

Contoh prinsip:

> “Course Management exists” tidak cukup jika evidence hanya menunjukkan folder/controller/model.

Gunakan wording yang sesuai evidence, misalnya:

- `FACT`: komponen/controller/model/schema tertentu ditemukan.
- `DERIVED`: perilaku disimpulkan dari beberapa evidence yang saling mendukung.
- `UNKNOWN`: perilaku aktif atau end-to-end flow belum dapat dibuktikan.

Jangan menaikkan classification menjadi FACT hanya karena artifact sebelumnya sudah menuliskannya sebagai FACT.

### REV-002 — Traceability

Perkuat traceability untuk seluruh substantive claims.

Claim material harus dapat ditelusuri ke evidence yang cukup granular, seperti:

- file/path;
- class;
- method/function;
- route;
- controller;
- model;
- migration/schema/table;
- config/env;
- job/event/listener;
- test;
- manifest/module registry;
- atau evidence lain yang benar-benar diperiksa.

Hindari referensi generik seperti “models, controllers, and schema” jika claim membutuhkan source yang lebih spesifik.

Jangan membuat nomor baris atau reference yang tidak benar-benar diketahui.

### REV-003 — Overbroad FACT claims

Cari dan revisi semua FACT yang menyatakan lebih dari yang dibuktikan evidence.

Pisahkan minimal:

1. evidence bahwa sesuatu **ada**;
2. evidence bahwa sesuatu **dipanggil/digunakan**;
3. evidence bahwa sesuatu **reachable**;
4. evidence bahwa sesuatu **aktif pada runtime**.

Untuk package/provider/integration/config reference, jangan menyimpulkan actual runtime usage tanpa evidence.

Contoh:
- package payment gateway ditemukan → FACT tentang package/reference existence;
- payment gateway benar-benar digunakan → hanya FACT/DERIVED jika ada execution/reference evidence;
- payment gateway aktif di production → UNKNOWN jika tidak ada runtime evidence.

### REV-004 — Existence vs active behavior / reachability

Revisi klaim yang menyamakan keberadaan komponen dengan perilaku aktif.

Khusus untuk `modules_statuses.json`, jika evidence menunjukkan 19 module entries enabled, tulis secara evidence-safe:

> “19 module entries are marked enabled in `modules_statuses.json).”

Jangan otomatis menulis:

> “19 modules are active.”

Jika loadability/reachability/runtime activity tidak dapat dibuktikan, tandai sebagai `UNKNOWN`.

### REV-005 — “All verified” overclaim

Hapus atau revisi wording absolut seperti:

- “all verified”;
- “fully verified”;
- “complete”;

jika artifact masih memiliki UNKNOWN, incomplete flows, missing runtime evidence, atau unresolved conflicts.

Gunakan wording yang menggambarkan batas evidence yang benar-benar tersedia.

### REV-006 — Flow reconstruction

Perdalam flow reconstruction untuk core flows yang memang memiliki evidence.

Jika evidence tersedia, flow minimal harus mencoba menjelaskan:

1. trigger;
2. entry point;
3. route/caller;
4. middleware/auth boundary;
5. controller/service/component;
6. validation;
7. decision/branch;
8. data read/write;
9. dependencies;
10. side effects;
11. success/stop condition;
12. error/failure branch jika dapat dibuktikan.

Prioritaskan flow penting seperti authentication, enrollment, order/payment, course access, progress, quiz/assessment, dan certificate **hanya jika evidence memang tersedia**.

Jangan mengisi langkah yang tidak terbukti hanya agar flow terlihat lengkap.

### REV-007 — Architecture precision

Revisi architecture conclusions yang terlalu absolut.

Contoh:

Jangan menyatakan:

> “No service layer exists.”

Jika `app/Services/` atau service classes ditemukan.

Gunakan bentuk evidence-safe seperti:

> “A Services directory exists, but the inspected application logic is predominantly implemented directly in controllers rather than consistently mediated through a service layer.”

Sesuaikan wording dengan evidence aktual.

Prinsip yang sama berlaku untuk repository pattern, domain layer, event-driven architecture, modularity, dan architectural boundaries lain.

### REV-008 — Runtime / operational claims

Pisahkan:

- code behavior;
- inferred runtime implication;
- observed runtime result.

Contoh queue job yang memanggil `Auth::user()`:

- FACT: job code calls `Auth::user()`;
- DERIVED: this creates a dependency on authenticated context;
- UNKNOWN: whether the job actually fails in the deployed runtime, jika tidak ada runtime evidence.

Jangan menyebut sesuatu “broken”, “fails”, atau “unusable” tanpa evidence runtime yang membuktikannya.

### REV-009 — Conflict classification

Periksa ulang seluruh conflict/issue classification.

Bedakan:

- contradictory evidence → `CONFLICT`;
- inconsistent data representation → inconsistency/data concern;
- runtime risk inferred from code → `DERIVED` risk;
- missing evidence → `UNKNOWN`;
- confirmed dead/orphan code → hanya jika control-flow/reachability evidence mendukung.

Jangan menyebut sesuatu sebagai contradiction hanya karena secara desain terlihat kurang ideal.

### REV-010 — Reachability

Perkuat reachability analysis dengan status yang evidence-based, bila dapat dibuktikan:

- `REACHABLE`
- `CONFIG-DEPENDENT`
- `REFERENCE-ONLY`
- `DEAD/ORPHAN`
- `UNKNOWN`

Jangan mengisi status hanya berdasarkan keberadaan file/module.

Jika reachability tidak dapat dipastikan, gunakan `UNKNOWN`.

### REV-011 — Evidence granularity

Perkuat evidence references pada feature/module areas yang sebelumnya hanya memiliki claim umum.

Feature areas yang perlu diperiksa kembali antara lain:

- Forum;
- Homework;
- Chatboard;
- Resume/Job Portal;
- Attendance;
- Wallet;
- Affiliate;
- dan feature/module lain yang evidence-nya sebelumnya terlalu generik.

Gunakan evidence yang benar-benar ditemukan. Jangan membuat evidence reference sintetis.

### REV-012 — Completion/readiness wording

Jangan menyatakan artifact “approved”, “gate-ready”, atau equivalent.

Setelah revisi selesai, artifact tetap:

`status: DRAFT`

Wording readiness harus membedakan:

- revisi telah selesai;
- artifact siap untuk independent review;
- artifact telah lulus review;
- artifact telah disetujui human.

Prompt ini hanya mengizinkan status pertama dan/atau readiness untuk review.

---

## 7. Evidence Re-check Rule

Untuk setiap substantive revision:

1. Mulai dari claim ART-001 v1.0.
2. Cocokkan claim dengan REV yang relevan.
3. Periksa evidence legacy yang tersedia.
4. Jika evidence cukup, revisi classification/wording.
5. Jika evidence tidak cukup, downgrade ke `UNKNOWN` atau batas evidence yang tepat.
6. Jika evidence saling bertentangan, gunakan `CONFLICT`.
7. Jika inference diperlukan, label `DERIVED` dan jelaskan basis reasoning.
8. Tambahkan/granulkan traceability.
9. Pastikan revisi tidak menciptakan requirement atau future-state decision.

**Jangan melakukan broad rewrite hanya demi gaya bahasa.** Revisi harus traceable terhadap findings dan evidence.

---

## 8. Artifact Preservation Rules

Pertahankan:

- `artifact_id: ART-001`;
- artifact type `ANALYSIS`;
- target path `analysis/existing-system.md`;
- struktur yang masih valid;
- evidence yang tetap valid;
- boundary WHAT EXISTS vs WHAT SHOULD EXIST.

Ubah:

- version → `1.1`;
- substantive claims yang terdampak findings;
- evidence classification;
- traceability;
- flow detail;
- reachability;
- wording readiness/completion jika diperlukan.

Jangan:

- menghapus findings dari ART-002;
- mengubah ART-002;
- menulis resolution status ke ART-002;
- membuat approval;
- mengubah human decision;
- memasukkan future-state design.

---

## 9. Metadata Output Contract

ART-001 v1.1 wajib menggunakan metadata artifact yang konsisten:

```yaml
---
document: ANALYSIS
artifact_id: ART-001
version: 1.1
status: DRAFT
owner: RE-RESEARCHER
prompt_id: <revision-prompt-id>
---
```

Jika repository convention mewajibkan field tambahan, pertahankan/tambahkan sesuai convention.

Jangan mengubah owner menjadi reviewer atau PROJECT_OWNER hanya karena proses review.

---

## 10. Required Revision Traceability

Di dalam ART-001 v1.1, jika convention memungkinkan dan tidak mengganggu struktur artifact, dokumentasikan hubungan revisi secara jelas:

- source artifact: `ART-001 v1.0`;
- review basis: `ART-002 v1.0`;
- findings addressed: `REV-001` … `REV-012`.

Traceability tidak berarti menyalin seluruh review findings ke dalam Existing System artifact.

---

## 11. Output Contract

Output utama hanya:

**`analysis/existing-system.md` — ART-001 v1.1**

Output wajib:

- valid terhadap Artifact & Metadata Convention;
- status tetap `DRAFT`;
- seluruh REV-001 sampai REV-012 telah ditangani atau secara eksplisit dinyatakan unresolved karena evidence limitation;
- tidak ada unsupported fact baru;
- traceability lebih granular;
- evidence classification lebih ketat;
- flow reconstruction lebih substansial pada area yang memiliki evidence;
- reachability tidak disamakan dengan existence;
- unknown/conflict dipertahankan bila diperlukan;
- WHAT EXISTS vs WHAT SHOULD EXIST tetap tegas.

---

## 12. Mandatory Final Self-Check

Sebelum menyelesaikan revisi, lakukan self-check berikut:

### Identity
- [ ] Target input benar: ART-001 v1.0.
- [ ] Review basis benar: ART-002 v1.0.
- [ ] Output benar: ART-001 v1.1.
- [ ] Artifact ID tetap ART-001.
- [ ] Status tetap DRAFT.

### Findings
- [ ] REV-001 ditangani.
- [ ] REV-002 ditangani.
- [ ] REV-003 ditangani.
- [ ] REV-004 ditangani.
- [ ] REV-005 ditangani.
- [ ] REV-006 ditangani.
- [ ] REV-007 ditangani.
- [ ] REV-008 ditangani.
- [ ] REV-009 ditangani.
- [ ] REV-010 ditangani.
- [ ] REV-011 ditangani.
- [ ] REV-012 ditangani.

### Evidence discipline
- [ ] Tidak ada claim FACT tanpa evidence yang memadai.
- [ ] Existence tidak dianggap active behavior.
- [ ] Existence tidak dianggap reachable.
- [ ] Runtime behavior tidak diklaim tanpa runtime evidence.
- [ ] DERIVED digunakan untuk inference.
- [ ] UNKNOWN digunakan saat evidence tidak cukup.
- [ ] CONFLICT digunakan hanya untuk genuinely contradictory evidence.
- [ ] Tidak ada evidence reference yang diada-adakan.

### Boundary
- [ ] Tidak ada requirement baru.
- [ ] Tidak ada future-state architecture.
- [ ] Tidak ada future-state database design.
- [ ] Tidak ada API/UI design.
- [ ] Tidak ada implementation plan.
- [ ] Tidak ada business decision baru.
- [ ] Legacy behavior tetap diposisikan sebagai evidence, bukan automatically as requirement.

### Review boundary
- [ ] ART-002 tidak diubah.
- [ ] Tidak ada finding yang dihapus.
- [ ] Tidak ada finding yang diberi status RESOLVED/ACCEPTED/REJECTED oleh AI.
- [ ] Tidak ada approval.
- [ ] Artifact siap diserahkan untuk independent re-review.

---

## 13. Completion Statement

Setelah file berhasil direvisi, laporkan secara ringkas:

1. output artifact: `ART-001 v1.1`;
2. findings `REV-001` sampai `REV-012`: addressed / partially addressed / blocked by evidence;
3. evidence limitations yang masih tersisa;
4. bahwa artifact tetap `DRAFT`;
5. bahwa independent re-review diperlukan.

**Jangan menyatakan ART-001 v1.1 approved atau gate-passed.**
