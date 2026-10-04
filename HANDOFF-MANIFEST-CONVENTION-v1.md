# Handoff Manifest Convention

## 1. Purpose

Dokumen ini adalah **governing convention** untuk identitas, metadata, source registry, target, scope, constraints, evidence boundary, review scope, dan completion criteria pada setiap artifact-based handoff dalam Rewrite LMS.

Convention ini digunakan oleh Master Documentation Contract, Documentation Workflow, Role-Specific Contracts, dan individual handoff manifests.

Convention ini mendefinisikan **struktur dan aturan handoff package**. Convention ini **tidak mendefinisikan workflow role**, business decision, approval authority, atau isi artifact yang dihasilkan.

---

## 2. Authority

Urutan authority untuk handoff adalah:

1. Master Documentation Contract
2. Artifact & Metadata Convention
3. Handoff Manifest Convention
4. Documentation Workflow
5. Role-Specific Contract
6. Individual Handoff Manifest
7. `instructions.md`

Jika terjadi conflict, artifact dengan authority lebih rendah tidak boleh diam-diam mengubah aturan pada level yang lebih tinggi.

Manifest mendefinisikan handoff package. `instructions.md` hanya memberikan operational context dan tidak boleh override manifest atau governing contracts.

---

## 3. Handoff Identity

Setiap official handoff manifest adalah artifact dan WAJIB memiliki:

- `ART-xxx` sebagai artifact identity
- `HOF-xxx` sebagai handoff identity

`ART-xxx` mengidentifikasi manifest sebagai artifact.

`HOF-xxx` mengidentifikasi satu instance handoff/package.

Satu artifact dapat terlibat dalam beberapa handoff berbeda dan setiap handoff tetap memiliki `HOF-xxx` sendiri.

Identity rules:

1. `ART-xxx` dan `HOF-xxx` harus unique.
2. Identity tidak boleh berubah hanya karena package directory atau filename berubah.
3. Handoff identity tidak boleh digunakan sebagai pengganti artifact identity.
4. Snapshot/copy file di dalam package tidak otomatis menjadi artifact baru.
5. Historical handoff identity dipertahankan untuk traceability.

---

## 4. Required Manifest Metadata

Manifest WAJIB menggunakan YAML front matter yang mengikuti Artifact & Metadata Convention.

Minimum:

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

`document: HANDOFF` menggunakan artifact type yang didefinisikan oleh Artifact & Metadata Convention.

`from_role` dan `to_role` menjelaskan konteks handoff; keduanya tidak memberikan authority di luar Role-Specific Contract dan Master Contract.

---

## 5. Handoff Purpose

Purpose menjelaskan tujuan handoff, bukan nama role atau business decision.

Baseline values:

```text
RESEARCH
ANALYSIS
CREATE
REVIEW
REVISE
DECISION_SUPPORT
VALIDATION
FINALIZATION
```

Purpose baru boleh ditambahkan jika diperlukan dan tidak conflict dengan governing contracts.

Purpose tidak boleh menyiratkan approval yang belum diberikan.

Contoh valid:

```text
REVIEW
```

Bukan:

```text
APPROVE_PRD
```

---

## 6. Source Artifact Registry

Setiap source input yang menjadi authoritative context untuk handoff WAJIB diregistrasikan menggunakan stable artifact identity.

Example:

```yaml
source_artifacts:
  - artifact_id: ART-003
    role: PRIMARY_INPUT
  - artifact_id: ART-005
    role: SUPPORTING_INPUT
  - artifact_id: ART-007
    role: REVIEW_CONTEXT
```

Baseline source roles:

```text
PRIMARY_INPUT
SUPPORTING_INPUT
REVIEW_CONTEXT
REFERENCE
```

Path boleh dicantumkan untuk navigasi, tetapi stable artifact ID tetap authoritative.

File yang hanya merupakan copied snapshot di `handoff/source/` tidak menjadi source of truth baru kecuali secara eksplisit diregistrasikan sebagai artifact.

---

## 7. Target Definition

Target handoff dapat berupa artifact existing atau artifact baru.

Existing artifact:

```yaml
target:
  artifact_id: ART-014
  action: REVIEW
```

New artifact:

```yaml
target:
  artifact_id: NEW
  artifact_type: REQUIREMENT
  action: CREATE
```

Baseline target actions:

```text
CREATE
REVIEW
REVISE
VALIDATE
FINALIZE
```

Target definition tidak memberikan approval authority.

Jika target merupakan existing artifact, manifest harus mempertahankan identity artifact tersebut.

---

## 8. Expected Output

Manifest WAJIB menjelaskan output yang diharapkan.

Expected output harus mendeskripsikan artifact/result yang harus dihasilkan, bukan status approval yang belum diberikan.

Contoh:

```text
PRD revision ready for human review
```

Bukan:

```text
APPROVED PRD
```

Completion of a handoff never equals human approval unless approval is explicitly performed by the authorized human gate.

---

## 9. Scope

Manifest WAJIB mendefinisikan batas pekerjaan bila handoff memiliki scope yang material.

Example:

```yaml
in_scope:
  - course enrollment behavior
  - enrollment validation
  - enrollment edge cases

out_of_scope:
  - database schema
  - UI design
  - payment behavior
```

Scope pada manifest tidak boleh contradict higher-authority scope atau explicit human decision.

Jika terdapat scope contradiction, record conflict dan jangan resolve secara diam-diam.

---

## 10. Restrictions

Restrictions harus mempertahankan mandatory governance rules dan dapat menambahkan constraints yang spesifik terhadap handoff.

Example:

```yaml
restrictions:
  - do_not_invent_business_rules
  - do_not_resolve_conflicts
  - do_not_modify_human_decisions
  - do_not_use_legacy_behavior_as_requirement_without_classification
```

Restrictions tidak boleh digunakan untuk menonaktifkan higher-authority contract.

---

## 11. Open Questions and Conflicts

Known unresolved records WAJIB dipertahankan ketika relevan.

Example:

```yaml
known_open_questions:
  - OQ-003

known_conflicts:
  - CON-002
```

Manifest hanya meregistrasikan unresolved state yang diketahui. Manifest tidak memberikan authority untuk menjawab, menutup, atau mengubah `OQ-xxx` atau `CON-xxx`.

Receiver tidak boleh menghilangkan unresolved question atau conflict hanya karena tidak nyaman untuk downstream work.

---

## 12. Review Scope

Jika handoff meminta review atau validation, manifest harus mendefinisikan review scope secukupnya.

Example:

```yaml
review_scope:
  consistency:
    - scope
    - business_rules
  check_for:
    - contradiction
    - unsupported_assumption
    - missing_requirement
    - ambiguity
```

Review scope tidak mengubah Review Contract atau memberikan authority kepada reviewer untuk rewrite target artifact secara diam-diam.

---

## 13. Evidence Boundary

Manifest WAJIB menjaga evidence boundary.

Example:

```yaml
evidence_policy:
  allowed:
    - source_artifacts
    - repository_source
    - referenced_evidence
  prohibited:
    - unsupported_assumptions
    - inferred_business_decisions
```

Evidence rules pada Master Contract tetap berlaku.

Manifest tidak boleh memperlakukan model inference sebagai evidence.

---

## 14. Completion Criteria

Manifest harus mendefinisikan completion criteria yang relevan.

Example:

```yaml
completion:
  required:
    - all_source_artifacts_read
    - target_artifact_read
    - restrictions_checked
    - open_questions_preserved
    - conflicts_preserved
    - output_artifact_created
```

Completion berarti kewajiban handoff telah dipenuhi.

``completion` != `approval``.

Approval tetap mengikuti human approval gate dan Artifact & Metadata Convention.

---

## 15. Context Package Structure

Baseline context package:

```text
handoff/
├── manifest.md
├── source/
├── target/
└── instructions.md
```

Rules:

1. `manifest.md` adalah authoritative definition of the package.
2. `source/` berisi input context yang diregistrasikan dalam manifest.
3. `target/` berisi target artifact/context yang diregistrasikan.
4. `instructions.md` berisi operational instructions dan tidak boleh override manifest.
5. Package tidak boleh menduplikasi governance artifacts tanpa alasan architectural yang eksplisit.
6. Copied files tetap merupakan snapshot/context kecuali secara eksplisit diregistrasikan sebagai artifact.
7. Stable artifact IDs tetap menjadi identity authority meskipun package menggunakan file copies.

---

## 16. Receiver Obligations

Receiver WAJIB:

1. membaca manifest sebelum memproses handoff;
2. membaca source artifacts yang diwajibkan;
3. membaca target artifact bila ada;
4. mengikuti Master Contract, Artifact & Metadata Convention, dan Role-Specific Contract yang applicable;
5. mematuhi scope dan restrictions;
6. mempertahankan known open questions dan conflicts;
7. menggunakan evidence sesuai evidence boundary;
8. menghasilkan output sesuai expected output dan completion criteria;
9. tidak mengambil business decision atau approval authority yang tidak diberikan.

Receiver tidak boleh menganggap source artifact selalu sempurna. Source tetap harus dianalisis sesuai evidence dan review rules.

---

## 17. Sender Obligations

Sender WAJIB memastikan sebelum handoff:

1. manifest memiliki identity dan metadata yang valid;
2. source artifacts diregistrasikan menggunakan stable artifact IDs;
3. target definition jelas;
4. purpose dan expected output jelas;
5. scope dan restrictions tidak ambigu;
6. known open questions dan conflicts dipertahankan;
7. evidence boundary cukup untuk pekerjaan receiver;
8. completion criteria dapat diverifikasi.

Sender tidak boleh menggunakan handoff untuk menyelundupkan business decision atau approval yang belum sah.

---

## 18. Traceability

Minimum handoff traceability:

```text
Source Artifact(s)
      ↓
HOF-xxx
      ↓
Target Artifact
      ↓
Output / Review
```

Handoff harus dapat ditelusuri kembali ke artifact source dan target.

Manifest dapat mencantumkan domain IDs seperti `OQ-xxx`, `CON-xxx`, atau `REV-xxx` bila relevan.

---

## 19. Non-Boundaries

Convention ini TIDAK mendefinisikan:

- role responsibility;
- business decision;
- approval authority;
- workflow sequencing;
- artifact content rules;
- implementation details.

Hal tersebut tetap berada pada governing contract, workflow, role contract, atau artifact-specific rules yang applicable.

---

## 20. Validation Checklist

Handoff manifest compliant apabila:

- [ ] `document: HANDOFF` tersedia
- [ ] `artifact_id: ART-xxx` tersedia
- [ ] `handoff_id: HOF-xxx` tersedia
- [ ] version tersedia
- [ ] status valid
- [ ] owner tersedia
- [ ] from_role dan to_role tersedia
- [ ] purpose tersedia
- [ ] source artifacts menggunakan stable IDs
- [ ] target definition tersedia
- [ ] expected output tersedia
- [ ] scope tersedia bila applicable
- [ ] restrictions tersedia bila applicable
- [ ] known OQ/CON dipertahankan bila applicable
- [ ] evidence boundary tersedia bila applicable
- [ ] completion criteria tersedia
- [ ] package structure sesuai convention
- [ ] tidak ada rule yang conflict dengan higher-authority contracts

Manifest compliance tidak sama dengan review atau approval.

---

## 21. Definition of Done

Handoff setup selesai hanya apabila:

1. `HOF-xxx` dan `ART-xxx` diberikan.
2. Required metadata lengkap.
3. Source registry jelas.
4. Target jelas.
5. Purpose dan expected output jelas.
6. Scope/restrictions diketahui.
7. Known unresolved records dipertahankan.
8. Evidence boundary diketahui.
9. Completion criteria dapat diverifikasi.
10. Context package mengikuti baseline structure.
11. Tidak ada convention conflict.

---

## 22. Change Control

Perubahan terhadap convention ini adalah perubahan terhadap global handoff infrastructure.

Perubahan WAJIB mengidentifikasi:

- rule yang berubah;
- manifest/template/role contract yang terdampak;
- downstream impact;
- review terhadap Master Contract;
- human approval yang diwajibkan;
- versioning yang sesuai;
- historical traceability.

Tidak ada Role-Specific Contract atau individual manifest yang boleh mengubah convention ini secara diam-diam.

---

## 23. Governing Principle

> **A handoff is an explicit transfer of bounded context, not a transfer of conversation history.**

> **The manifest defines what is handed off; the role contract defines what the receiver does.**

> **Stable artifact IDs define identity; HOF-xxx defines the handoff instance.**

> **Completion is not approval. Human authority remains outside the handoff mechanism.**

---

## 24. Convention Status

```yaml
convention: HANDOFF-MANIFEST-CONVENTION
version: 1.0
status: APPROVED
owner: PROJECT_OWNER
```
