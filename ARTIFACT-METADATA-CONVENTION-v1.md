# Artifact & Metadata Convention

## 1. Purpose

Dokumen ini adalah **governing convention** untuk identitas, metadata, lifecycle, ownership, versioning, traceability, source of truth, dan repository placement seluruh documentation artifact pada Rewrite LMS.

Convention ini digunakan oleh Master Documentation Contract, Documentation Workflow, Role-Specific Contracts, artifact templates, review artifacts, decision artifacts, handoff artifacts, dan Documentation Index.

Convention ini mendefinisikan **struktur dan aturan artifact**. Convention ini **tidak mendefinisikan workflow role**, business decision, atau urutan pekerjaan antar-role.

---

## 2. Authority

Urutan authority documentation system adalah:

1. Master Documentation Contract
2. Artifact & Metadata Convention
3. Documentation Workflow
4. Role-Specific Contract
5. Individual Artifact

Jika terjadi conflict, artifact dengan authority lebih rendah tidak boleh diam-diam mengubah aturan pada level yang lebih tinggi.

---

## 3. Artifact Identity

Setiap official artifact WAJIB memiliki stable identity.

Untuk document-level artifact:

`ART-xxx`

Contoh:

`ART-001`, `ART-002`, `ART-003`

`ART-xxx` mengidentifikasi artifact/document, bukan claim atau finding di dalam artifact.

Stable IDs untuk domain-specific records tetap dipertahankan:

| Prefix | Meaning |
| --- | --- |
| `ES-xxx` | Existing System Finding |
| `FM-xxx` | Feature Mapping Entry |
| `BR-xxx` | Business Rule |
| `FR-xxx` | Functional Requirement |
| `NFR-xxx` | Non-Functional Requirement |
| `UC-xxx` | Use Case / User Flow |
| `AC-xxx` | Acceptance Criteria |
| `EC-xxx` | Edge Case |
| `DEP-xxx` | Dependency |
| `OQ-xxx` | Open Question |
| `CON-xxx` | Conflict |
| `REV-xxx` | Review Finding |

Domain-specific IDs identify records inside or across artifacts. `ART-xxx` identifies the artifact that contains or governs those records.

### Identity Rules

1. ID harus unique dalam documentation system.
2. ID tidak boleh berubah hanya karena filename berubah.
3. ID tidak boleh digunakan ulang untuk artifact berbeda.
4. Artifact yang disupersede mempertahankan identity historisnya.
5. Revision material dari artifact yang sama mempertahankan `ART-xxx` dan menaikkan `version`.
6. Artifact baru yang menggantikan artifact lama mendapatkan `ART-xxx` baru dan mereferensikan `supersedes` / `superseded_by`.
7. Domain record ID tidak boleh dipakai sebagai pengganti artifact identity.

---

## 4. Artifact Type

`document` adalah metadata key canonical untuk artifact type.

Allowed baseline types:

`MASTER-CONTRACT`, `CONVENTION`, `WORKFLOW`, `ROLE-CONTRACT`, `SOURCE`, `ANALYSIS`, `REVIEW`, `CONFLICT`, `OPEN-QUESTION`, `DECISION`, `ADR`, `REQUIREMENT`, `USER-FLOW`, `BUSINESS-RULE`, `ACCEPTANCE-CRITERIA`, `HANDOFF`, `INDEX`

Feature-specific artifacts menggunakan type sesuai purpose-nya dan dapat memiliki `feature`.

Artifact type baru hanya boleh diperkenalkan apabila diperlukan oleh workflow dan tidak bertentangan dengan Master Contract.

---

## 5. Required Metadata

Setiap official artifact WAJIB memiliki YAML front matter.

Minimum:

```yaml
---
document: <artifact-type>
artifact_id: ART-xxx
version: 1.0
status: DRAFT
owner: <role-or-authority>
---
```

### Feature-Specific Artifact

Artifact yang secara khusus mewakili satu feature WAJIB menambahkan:

`feature: <feature-id>`

Contoh:

```yaml
---
document: REQUIREMENT
artifact_id: ART-014
feature: course-progress
version: 1.0
status: DRAFT
owner: PRD-ANALYST
---
```

### Optional Metadata

Metadata berikut dapat digunakan bila relevan:

`created_from:`, `depends_on:`, `supersedes:`, `superseded_by:`, `reviewed_by:`, `approved_by:`

Optional metadata tidak boleh menjadi substitute untuk required traceability.

---

## 6. Metadata Semantics

- `document`: artifact type; bukan title atau filename.
- `artifact_id`: stable identity; tidak berubah pada revision artifact yang sama.
- `version`: version dengan format `MAJOR.MINOR`.
- `status`: lifecycle status artifact.
- `owner`: authority atau role yang bertanggung jawab; tidak otomatis berarti approval authority.
- `feature`: feature identifier untuk feature-specific artifact dan harus konsisten dengan Feature Mapping bila applicable.

---

## 7. Lifecycle Status

Baseline lifecycle states:

`DRAFT`, `IN_REVIEW`, `REVIEWED`, `READY_FOR_APPROVAL`, `APPROVED`, `ACCEPTED`, `SUPERSEDED`, `DEPRECATED`

Meaning:

- `DRAFT`: masih disusun dan belum menjadi source of truth.
- `IN_REVIEW`: sedang menjalani review yang diwajibkan.
- `REVIEWED`: review selesai, approval belum diberikan.
- `READY_FOR_APPROVAL`: review obligations terpenuhi dan siap menunggu human approval.
- `APPROVED`: approval yang diwajibkan telah diberikan dan artifact dapat menjadi source of truth sesuai authority.
- `ACCEPTED`: diterima sebagai keputusan/hasil ketika workflow menggunakan status ini secara eksplisit.
- `SUPERSEDED`: digantikan artifact atau revision yang lebih baru.
- `DEPRECATED`: tidak lagi direkomendasikan untuk penggunaan aktif tetapi dipertahankan untuk historical traceability.

Rules:

1. Non-`APPROVED` status tidak boleh diperlakukan equivalent terhadap `APPROVED`.
2. Artifact `APPROVED` tidak boleh berubah secara material tanpa revision dan applicable review.
3. `SUPERSEDED` dan `DEPRECATED` tetap dipertahankan kecuali ada aturan retention yang lebih tinggi.
4. Status tidak boleh dinaikkan untuk melewati required review atau human approval.

---

## 8. Ownership

Setiap official artifact WAJIB memiliki satu `owner`.

Owner bertanggung jawab menjaga compliance, review obligations, traceability, dan accuracy status.

Ownership bukan berarti owner bebas mengubah business decision atau higher-authority contract.

Jika ownership berpindah, artifact identity tetap sama dan perubahan ownership harus tercermin pada metadata revision berikutnya.

---

## 9. Versioning

Minor revision:

`1.0 → 1.1`

Untuk wording clarification, editorial correction, documentation improvement, atau non-material clarification.

Major revision:

`1.x → 2.0`

Untuk business rule change, scope change, feature behavior change, material data-model change, atau material authority/decision change.

Perubahan material WAJIB melalui applicable review/re-approval process.

---

## 10. Supersession

Jika artifact digantikan:

```yaml
status: SUPERSEDED
superseded_by: ART-xxx
```

Artifact pengganti dapat menggunakan:

`supersedes: ART-xxx`

Historical artifact tidak dihapus hanya untuk membersihkan repository.

---

## 11. Traceability

Artifact harus menggunakan stable IDs ketika merujuk artifact lain.

Preferred reference:

`ART-014`

Bukan hanya:

`prd/course-progress.md`

Path tetap boleh dicantumkan sebagai navigational information.

Jika applicable:

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

Tidak semua artifact harus memiliki seluruh chain. AI tidak boleh menciptakan relationship hanya untuk membuat chain terlihat lengkap.

---

## 12. Source of Truth

Source of truth ditentukan oleh **authority + status + workflow context**.

General rule:

```text
APPROVED authoritative artifact
        >
non-approved artifact
```

Namun `APPROVED` tidak otomatis mengalahkan artifact dengan authority yang lebih tinggi.

Contoh:

```text
Master Contract
    >
Artifact & Metadata Convention
    >
Workflow
    >
Role Contract
    >
Individual Artifact
```

Jika dua artifact pada level yang setara bertentangan:

1. Jangan resolve secara diam-diam.
2. Record `CON-xxx`.
3. Escalate sesuai workflow.
4. Gunakan human decision bila diperlukan.
5. Update affected artifact setelah resolution.

---

## 13. Repository Placement

Repository root adalah canonical documentation root.

Global governance artifacts berada di root:

- `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md`
- `ARTIFACT-METADATA-CONVENTION-v1.md`
- `LMS-REWRITE-DOCUMENTATION-WORKFLOW.md`
- `DOCUMENTATION-INDEX.md`
- `ROLE-SPECIFIC-CONTRACT-*.md`

Domain artifacts berada pada directory yang sesuai:

- `analysis/`
- `prd/`
- `reviews/`

Artifact baru tidak boleh membuat duplicate governance file di subdirectory tanpa explicit architectural reason.

`docs/` tidak boleh ditambahkan di depan path karena repository ini sendiri berada di legacy project's `docs/` directory.

---

## 14. Template Compliance

Template WAJIB mengikuti convention ini.

Template tidak boleh mendefinisikan metadata schema alternatif, membuat stable ID system sendiri, mengganti lifecycle status, mengganti source-of-truth rules, atau menghilangkan required metadata.

Field tambahan boleh digunakan bila additive dan tidak conflict dengan global convention.

---

## 15. Role Contract Compliance

Setiap Role-Specific Contract WAJIB merujuk convention ini sebagai governing artifact.

Role WAJIB menghasilkan artifact dengan required metadata, mempertahankan stable identity, dan menjaga traceability.

Role TIDAK BOLEH mengubah global artifact rules atau menaikkan status artifact tanpa memenuhi gate.

Workflow behavior tetap berada di Role-Specific Contract dan Documentation Workflow.

---

## 16. Review Artifact Rules

Review findings menggunakan `REV-xxx`.

Review artifact harus dapat ditelusuri ke artifact yang direview.

Minimum relationship:

```text
Review Artifact
    ↓
Target Artifact (ART-xxx)
    ↓
REV-xxx Findings
```

Review finding tidak boleh mengubah target artifact secara diam-diam.

---

## 17. Human Decision Boundary

Artifact convention tidak memberikan authority kepada AI untuk mengambil business decision.

Jika artifact membutuhkan scope decision, business behavior decision, conflict resolution, acceptance of material assumption, atau final approval, decision harus dicatat menggunakan artifact/record yang sesuai dan mengikuti human approval requirements.

AI boleh memberikan recommendation.

AI tidak boleh mengubah recommendation menjadi authoritative `DECISION` tanpa authority yang diwajibkan.

---

## 18. Migration / Legacy Artifact Rule

Existing artifacts yang dibuat sebelum convention ini dikunci **tidak wajib langsung dimigrasikan seluruhnya**.

Migration dilakukan ketika:

1. artifact mengalami material revision,
2. artifact menjadi dependency untuk downstream stage,
3. artifact masuk review/approval baru,
4. artifact secara eksplisit dipilih untuk migration.

Saat migration dilakukan, artifact harus di-align dengan convention tanpa mengubah historical meaning secara diam-diam.

Tujuannya mencegah bulk rewrite yang tidak diperlukan sekaligus memastikan artifact aktif bergerak menuju satu convention.

---

## 19. Validation Checklist

Official artifact dianggap metadata-compliant apabila:

- [ ] `document` tersedia
- [ ] `artifact_id` tersedia dan unique
- [ ] `version` tersedia
- [ ] `status` valid
- [ ] `owner` tersedia
- [ ] `feature` tersedia bila feature-specific
- [ ] Artifact type sesuai purpose
- [ ] Stable IDs di dalam artifact mengikuti applicable prefix
- [ ] References menggunakan stable artifact IDs bila cross-artifact
- [ ] Supersession metadata lengkap bila applicable
- [ ] Source-of-truth claim sesuai authority dan status
- [ ] Repository placement sesuai convention

Metadata compliance **tidak sama dengan review approval**.

---

## 20. Definition of Done

Artifact creation selesai hanya apabila:

1. Artifact type ditentukan.
2. Stable artifact identity diberikan.
3. Required metadata lengkap.
4. Repository location sesuai.
5. Required internal IDs diberikan.
6. Applicable traceability tersedia.
7. Lifecycle status benar.
8. Ownership jelas.
9. Required review/approval obligations diketahui.
10. Tidak ada metadata convention yang dilanggar.

---

## 21. Change Control

Perubahan terhadap convention ini adalah perubahan terhadap global documentation infrastructure.

Perubahan WAJIB mengidentifikasi rule yang berubah, artifact/template/role contract yang terdampak, downstream impact, review terhadap Master Contract, human approval yang diwajibkan, versioning yang sesuai, dan historical traceability.

Tidak ada Role-Specific Contract atau individual artifact yang boleh mengubah convention ini secara diam-diam.

---

## 22. Governing Principle

> **One documentation system, one artifact identity model, one metadata convention.**

> **Artifact identity identifies the artifact. Domain IDs identify the records inside the artifact.**

> **Metadata governs structure; workflow governs process; human authority governs decisions.**

---

## 23. Convention Status

```yaml
convention: ARTIFACT-METADATA-CONVENTION
version: 1.0
status: APPROVED
owner: PROJECT_OWNER
```
