# Review Artifact Convention

## 1. Purpose

Dokumen ini adalah governing convention untuk struktur, identity, metadata, scope, findings, lifecycle, evidence boundary, re-review, dan gate-readiness pada setiap Review Artifact dalam Rewrite LMS.

Convention ini mendefinisikan struktur dan aturan Review Artifact. Convention ini tidak memberikan business authority, approval authority, atau hak kepada reviewer untuk mengubah target artifact secara diam-diam.

## 2. Authority

Urutan authority: Master Documentation Contract → Artifact & Metadata Convention → Review Artifact Convention → Documentation Workflow → Role-Specific Contract → Individual Review Artifact.

Artifact dengan authority lebih rendah tidak boleh mengubah aturan level lebih tinggi secara diam-diam.

## 3. Identity

Setiap official Review Artifact WAJIB mengikuti Artifact & Metadata Convention, memiliki ART-xxx sebagai artifact identity, memiliki target review yang dapat diidentifikasi secara stabil, dan menyimpan findings menggunakan REV-xxx.

Review Artifact != Review Finding. ART-xxx mengidentifikasi Review Artifact; REV-xxx mengidentifikasi finding di dalamnya.

## 4. Required Metadata

Minimum metadata:

```yaml
---
document: REVIEW
artifact_id: ART-xxx
version: 1.0
status: DRAFT
owner: <review-owner>
---
```

Target review WAJIB mengidentifikasi exact artifact version:

```yaml
target:
  artifact_id: ART-014
  version: 1.2
```

Review terhadap ART-014 v1.1 tidak otomatis berlaku untuk v1.2.

## 5. Review Identity

Review dapat mencatat type dan reviewer role. Baseline types: ARTIFACT_REVIEW, PRD_REVIEW, DATABASE_REVIEW, CROSS_FEATURE_REVIEW, FINAL_CONSISTENCY_REVIEW, METADATA_REVIEW, TRACEABILITY_REVIEW.

Review type tidak memberikan approval authority.

## 6. Scope dan Evidence Boundary

Review Artifact WAJIB mendefinisikan scope secara eksplisit bila memiliki batas material dan menjaga evidence boundary. Reviewer hanya boleh membuat finding berdasarkan evidence yang dapat ditelusuri. Model inference dan inferred business decisions bukan evidence.

## 7. Finding Registry

Review Artifact WAJIB memiliki registry findings ketika findings dihasilkan:

```yaml
findings:
  - REV-041
  - REV-042
```

Jika tidak ada issue, gunakan `findings: []`.

## 8. Standard Review Finding

Setiap REV-xxx menggunakan minimum:

```markdown
### REV-041

**Severity:** HIGH

**Category:** CONTRADICTION

**Affected ID:** ART-014

**Claim**
...

**Evidence**
...

**Problem**
...

**Required Resolution**
...

**Status**
OPEN
```

Severity baseline: CRITICAL, HIGH, MEDIUM, LOW. Reviewer tidak boleh memaksakan business decision.

## 9. Finding Lifecycle

REV-xxx mengikuti lifecycle authoritative dari Master Documentation Contract: OPEN, IN_PROGRESS, RESOLVED, ACCEPTED, REJECTED, SUPERSEDED.

Reviewer tidak boleh mengubah finding menjadi RESOLVED, ACCEPTED, atau REJECTED tanpa decision/verification yang sesuai. Finding tidak boleh dihapus dari historical review record.

## 10. Re-review

Re-review adalah Review Artifact baru terhadap target version baru dan harus mempertahankan historical linkage. Contoh:

```yaml
review:
  type: PRD_REVIEW
  supersedes_review:
    artifact_id: ART-030
target:
  artifact_id: ART-014
  version: 1.2
```

`suppersedes_review` menunjuk ke Review Artifact sebelumnya, bukan target artifact.

## 11. Review Result

Review result tidak sama dengan approval. Baseline results: NO_FINDINGS, FINDINGS_RECORDED, CHANGES_REQUIRED, READY_FOR_REVIEW_GATE. `APPROVED` bukan review result.

Approval tetap mengikuti Artifact & Metadata Convention dan human approval gate.

## 12. Gate Readiness

Review Artifact dapat mencatat gate readiness bila applicable. `READY_FOR_APPROVAL` berarti review obligations terpenuhi, bukan human approval. Unresolved CRITICAL/HIGH memblokir gate; MEDIUM/LOW mengikuti explicit human resolution rules pada Master Contract dan applicable gate.

## 13. Review Artifact Structure

Baseline location:

```text
reviews/
└── <review-name>.md
```

Recommended order: review identity, target artifact + version, scope, evidence policy, review method/checks, finding registry, findings, review result, gate readiness, re-review linkage, traceability.

Filename adalah navigational information. ART-xxx tetap menjadi identity authority.

## 14. Reviewer Non-Rewrite Rule

Reviewer membuat Review Artifact, mencatat REV-xxx, menyediakan evidence, memberikan analysis/recommendation, dan memverifikasi resolution pada re-review.

Reviewer TIDAK BOLEH silently rewrite target artifact, mengubah business decision, memberikan human approval, atau menghapus unresolved findings untuk menutup gate.

## 15. Traceability

Minimum relationship:

```text
Target Artifact (ART-xxx @ version)
        ↓
Review Artifact (ART-xxx)
        ↓
REV-xxx Findings
        ↓
Human Decision / Revision
        ↓
Re-review Artifact
```

Review Artifact harus dapat ditelusuri ke target artifact/version, evidence, findings, affected IDs, resolution/decision bila applicable, dan prior review bila re-review.

## 16. Non-Boundaries

Convention ini tidak mendefinisikan business authority, approval authority, role workflow detail, requirement content, business decision, substantive resolution, atau implementation behavior. Hal tersebut tetap berada pada higher contract, workflow, role contract, human decision rules, atau target artifact rules yang applicable.

## 17. Validation Checklist

- [ ] `document: REVIEW` tersedia
- [ ] `artifact_id: ART-xxx` tersedia
- [ ] required metadata lengkap
- [ ] target ART-xxx dan exact version tersedia
- [ ] scope dan evidence boundary jelas bila applicable
- [ ] finding registry tersedia
- [ ] setiap finding menggunakan REV-xxx
- [ ] finding lifecycle mengikuti Master Contract
- [ ] review result tidak menggunakan APPROVED
- [ ] gate readiness tidak disamakan dengan approval
- [ ] re-review mempertahankan target version dan historical linkage
- [ ] reviewer tidak silently rewrite target
- [ ] traceability tersedia
- [ ] tidak ada conflict dengan higher-authority contract

## 18. Definition of Done

Review Artifact selesai apabila identity dan target version jelas, scope/evidence cukup, findings stable dan traceable, result dicatat, gate readiness dicatat bila applicable, re-review linkage tersedia bila applicable, tidak ada silent rewrite, tidak ada convention conflict, dan human decision boundary tetap terjaga.

## 19. Change Control

Perubahan convention WAJIB mengidentifikasi rule yang berubah, Master Contract sections yang terdampak, workflow/role/template yang terdampak, downstream impact, human approval, versioning, dan historical traceability.

## 20. Governing Principles

> A Review Artifact is the review record; a REV-xxx is a finding within that record.

> Every review is bound to an exact target artifact version.

> Review result and gate readiness never equal human approval.

> Reviewers record findings; authorized roles revise artifacts; human authority resolves decisions.

## 21. Convention Status

```yaml
convention: REVIEW-ARTIFACT-CONVENTION
version: 1.0
status: APPROVED
owner: PROJECT_OWNER
```
