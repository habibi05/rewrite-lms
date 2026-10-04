# ROLE-SPECIFIC CONTRACT — MASTER TEMPLATE

## 1. Identitas Role

- **Nama Role:**
- **Role ID:**
- **Tanggung Jawab Utama:**
- **Tipe Role:**
- **Model Utama:**
- **Model Eskalasi:**
- **Reviewer:**

---

## 2. Misi

Definisikan tujuan utama dan fungsi spesifik role ini dalam sistem dokumentasi LMS.

Role ini WAJIB beroperasi dalam batasan yang ditetapkan oleh:

1. Master Contract v1
2. Documentation Workflow
3. Artifact & Metadata Convention
4. Human Decision Convention
5. Open Question & Conflict Convention
6. Folder Structure
7. Role-Specific Contract ini

Contract ini TIDAK BOLEH menggantikan, mengubah, atau mendefinisikan ulang contract pada tingkat yang lebih tinggi.

---

## 3. Scope

### 3.1 Dalam Scope

Definisikan secara eksplisit hal-hal yang menjadi tanggung jawab role ini.

### 3.2 Di Luar Scope

Definisikan secara eksplisit hal-hal yang TIDAK BOLEH dilakukan oleh role ini.

---

## 4. Inputs

Definisikan seluruh artifact, dokumen, metadata, evidence, dan output dari role sebelumnya yang boleh digunakan oleh role ini.

Untuk setiap input, tentukan:

- Artifact
- Source
- Required / Optional
- Expected status
- Dependency

---

## 5. Sources of Truth

Definisikan sumber yang WAJIB digunakan oleh role ini sebagai referensi authoritative.

Prioritas sumber WAJIB mengikuti hierarki yang telah ditetapkan oleh Master Contract v1.

Role TIDAK BOLEH secara diam-diam mengganti, menafsirkan ulang, atau menurunkan tingkat authority dari source of truth yang memiliki prioritas lebih tinggi.

---

## 6. Allowed Actions

Definisikan tindakan yang BOLEH dilakukan oleh role ini.

Contoh:

- Analyze
- Extract
- Classify
- Map
- Derive
- Document
- Identify conflicts
- Identify unknowns
- Produce findings
- Produce required artifacts

Seluruh tindakan WAJIB tetap berada dalam scope role yang telah ditentukan.

---

## 7. Forbidden Actions

Definisikan tindakan yang TIDAK BOLEH dilakukan oleh role ini.

Contoh:

- Mengarang fakta yang tidak didukung evidence
- Mengubah assumption menjadi FACT tanpa evidence
- Menyelesaikan conflict secara diam-diam
- Mengambil alih human decision
- Mengubah authoritative artifact milik role lain tanpa otorisasi
- Melewati review gate
- Melewati metadata requirements
- Memasukkan keputusan implementasi yang tidak terdokumentasi
- Mengubah atau mengesampingkan Master Contract v1

---

## 8. Evidence Handling

Role WAJIB mengikuti convention klasifikasi evidence dan confidence yang ditetapkan oleh:

**Artifact & Metadata Convention**

Classification yang digunakan:

- FACT
- DERIVED
- REQUIREMENT
- DECISION
- UNKNOWN
- CONFLICT

Confidence yang digunakan:

- HIGH
- MEDIUM
- LOW

Role WAJIB mempertahankan perbedaan antara:

**Evidence Classification ≠ Confidence**

Role TIDAK BOLEH meningkatkan evidence classification tanpa evidence pendukung yang memadai atau human decision yang diwajibkan.

---

## 9. Analysis Responsibilities

Definisikan tanggung jawab analisis spesifik dari role ini.

Role WAJIB membedakan secara eksplisit antara:

- Informasi yang diobservasi
- Informasi yang diturunkan
- Requirements
- Business decisions
- Unknowns
- Conflicts

Setiap inference WAJIB dapat ditelusuri kembali ke source-nya.

---

## 10. Artifact Responsibilities

Definisikan seluruh artifact yang menjadi tanggung jawab role ini untuk dibuat atau diperbarui.

Untuk setiap artifact tentukan:

| Artifact | Purpose | Required Metadata | Output Location | Status |
| -------- | ------- | ----------------- | --------------- | ------ |

Role WAJIB mengikuti Artifact & Metadata Convention.

---

## 11. Metadata Requirements

Setiap artifact yang dihasilkan oleh role ini WAJIB memenuhi Artifact & Metadata Convention yang telah dikunci.

Metadata WAJIB mencakup seluruh field yang diwajibkan oleh convention tersebut.

Role TIDAK BOLEH:

- Membuat struktur metadata alternatif
- Menghilangkan metadata yang diwajibkan
- Membuat sistem identity yang duplikat
- Mendefinisikan ulang stable ID rules

---

## 12. Traceability Requirements

Setiap claim, requirement, rule, decision, atau derived conclusion yang material WAJIB dapat ditelusuri kembali ke source-nya apabila diwajibkan oleh Master Contract.

Traceability WAJIB mempertahankan hubungan antara:

```text
Source
  ↓
Evidence
  ↓
Analysis
  ↓
Artifact
  ↓
Review
  ↓
Approval
```

Role TIDAK BOLEH menghasilkan authoritative claim yang tidak memiliki traceability.

---

## 13. Handoff Contract

Definisikan apa yang WAJIB disediakan oleh role ini kepada downstream role.

Untuk setiap handoff tentukan:

- Upstream artifact yang digunakan
- Output artifact yang dihasilkan
- Required metadata
- Required status
- Required traceability
- Conditions that block handoff

Downstream role TIDAK BOLEH dianggap ready apabila kondisi upstream yang bersifat mandatory masih unresolved.

---

## 14. Review Responsibilities

Definisikan apakah role ini:

- Menghasilkan artifact untuk direview
- Melakukan review
- Berpartisipasi dalam re-review
- Menyelesaikan findings
- Menyediakan evidence untuk resolution

Seluruh review findings WAJIB mengikuti Review Finding Lifecycle yang ditetapkan oleh Master Contract v1 dan struktur Review Artifact WAJIB mengikuti `REVIEW-ARTIFACT-CONVENTION-v1.md`.

Human Decision artifact WAJIB mengikuti `HUMAN-DECISION-CONVENTION-v1.md` dan menggunakan canonical ART-xxx. Role tidak boleh menggunakan HD-xxx sebagai identity canonical.

Open Question dan Conflict artifact WAJIB mengikuti `OPEN-QUESTION-CONFLICT-CONVENTION-v1.md`, termasuk canonical storage, `ART-xxx` artifact identity, `OQ-xxx` / `CON-xxx` records, escalation, resolution linkage, blocking behavior, dan historical preservation.

Review findings WAJIB menggunakan:

```text
REV-xxx
```

Role TIDAK BOLEH melewati:

- Human resolution requirements
- CRITICAL/HIGH blocking rules
- Re-review requirements
- Universal Review Gate Rule

---

## 15. Escalation Rules

Definisikan kondisi yang WAJIB dieskalasikan.

Contoh:

- Conflict antar-source
- Informasi kritis yang tidak tersedia
- Business intent yang ambigu
- Unsupported assumptions
- Scope ambiguity
- Ketidakkonsistenan antar-artifact
- Requirements yang membutuhkan human decision
- Decision yang berada di luar authority role

Eskalasi WAJIB mempertahankan uncertainty atau conflict yang asli.

Role TIDAK BOLEH menyelesaikan issue yang telah dieskalasikan secara diam-diam.

---

## 16. Human Decision Boundaries

Definisikan secara eksplisit decision yang TIDAK BOLEH dibuat secara autonomous oleh role ini.

Human approval WAJIB dilakukan pada kondisi yang ditentukan oleh Master Contract v1.

Contoh:

- Business decisions
- Scope decisions
- Conflict resolution
- Acceptance terhadap material assumptions
- Final approval
- Perubahan terhadap authoritative documentation

AI analysis BOLEH memberikan rekomendasi atau menampilkan opsi, tetapi TIDAK BOLEH mengubah rekomendasi menjadi authoritative decision tanpa human approval yang diwajibkan.

---

## 17. Output Contract

Definisikan output yang secara tepat diharapkan dari role ini.

Output WAJIB menentukan:

- Artifact name
- Artifact type
- Required sections
- Required metadata
- Required IDs
- Required traceability
- Required status
- Downstream consumer

Output TIDAK dianggap complete hanya karena content-nya sudah tersedia.

Output WAJIB memenuhi contract dan metadata requirements yang berlaku.

---

## 18. Definition of Done

Pekerjaan role dianggap selesai HANYA apabila:

- [ ] Seluruh scope requirements terpenuhi
- [ ] Seluruh input yang diwajibkan telah diproses
- [ ] Evidence classification valid
- [ ] Confidence dicatat apabila diwajibkan
- [ ] Stable IDs diberikan apabila diwajibkan
- [ ] Required metadata lengkap
- [ ] Traceability lengkap
- [ ] Required artifacts telah dibuat
- [ ] Required review telah selesai
- [ ] Required findings telah resolved atau secara eksplisit accepted
- [ ] Required re-review telah selesai
- [ ] Tidak ada unresolved CRITICAL/HIGH findings
- [ ] Required human decisions telah dicatat
- [ ] Applicable gate telah terpenuhi

---

## 19. Failure / Blocking Conditions

Role WAJIB melaporkan status sebagai `BLOCKED` apabila:

- Required source material tidak tersedia
- Required evidence tidak tersedia
- Critical conflicts masih unresolved
- Required human decisions masih pending
- Required metadata belum lengkap
- Required upstream artifacts belum ready
- Required review belum selesai
- CRITICAL/HIGH findings masih unresolved
- Required re-review belum dilakukan
- Pemenuhan role akan melanggar higher-level contract

Status `BLOCKED` TIDAK BOLEH secara diam-diam diubah menjadi `READY` atau `APPROVED`.

---

## 20. Contract Compliance

Role-Specific Contract ini berada di bawah:

1. Master Contract v1
2. Documentation Workflow
3. Artifact & Metadata Convention
4. Folder Structure

Apabila terjadi conflict, contract dengan tingkat authority yang lebih tinggi WAJIB diprioritaskan.

Role ini TIDAK BOLEH memperkenalkan aturan yang bertentangan dengan established source of truth.

---

## 21. Contract Change Control

Perubahan terhadap Role-Specific Contract ini WAJIB:

1. Didokumentasikan secara eksplisit
2. Menjelaskan behavior role yang terdampak
3. Mengidentifikasi artifact yang terdampak
4. Mengidentifikasi downstream dependencies yang terdampak
5. Direview terhadap Master Contract v1
6. Mendapatkan human approval yang diwajibkan
7. Diversikan sesuai documentation convention project

Tidak ada perubahan Role-Specific Contract yang boleh secara diam-diam mengubah global documentation system.
