# Human Decision Convention v1

**Status:** APPROVED  
**Owner:** PROJECT_OWNER

## 1. Purpose

Convention ini mendefinisikan struktur, identitas, authority, penyimpanan, lifecycle, dan traceability untuk keputusan manusia yang menjadi sumber kebenaran normatif.

## 2. Authority

Urutan authority:
1. Master Documentation Contract
2. Artifact & Metadata Convention
3. Human Decision Convention
4. Documentation Workflow
5. Role-Specific Contract
6. Individual Decision Artifact

Convention ini mengatur bentuk dan pengelolaan decision artifact. Authority substantif tetap berasal dari manusia yang berwenang.

## 3. Core Boundary

Human Decision berbeda dari:
- Recommendation — usulan AI/reviewer yang belum menjadi keputusan.
- Review Finding (REV-xxx) — temuan review.
- Open Question (OQ-xxx) — pertanyaan yang belum diputuskan.
- Conflict (CON-xxx) — pertentangan yang membutuhkan resolusi.
- Requirement — hasil dokumentasi normatif downstream.
- Approval — otorisasi terhadap artifact, perubahan, atau gate.

AI tidak boleh mengubah recommendation, finding, evidence, atau inference menjadi authoritative decision.

## 4. Identity

Official Human Decision menggunakan canonical artifact identity ART-xxx dari Artifact & Metadata Convention.

Metadata minimum:

    ---
    document: DECISION
    artifact_id: ART-xxx
    version: 1.0
    status: DRAFT
    owner: PROJECT_OWNER
    ---

Tidak ada identity HD-xxx sebagai identity canonical. Domain IDs tetap menggunakan convention masing-masing.

## 5. Human Authority

Decision artifact MUST mengidentifikasi decision maker/authority.

AI boleh mengidentifikasi kebutuhan keputusan, menyajikan evidence, opsi, recommendation, dan draft artifact. AI tidak boleh menetapkan business decision, mengklaim keputusan telah dibuat, atau mengubah recommendation menjadi authoritative decision tanpa explicit human action.

## 6. Decision Statement

Minimum content:
- Decision Type
- Decision
- Decision Maker
- Context
- Rationale

Decision statement MUST eksplisit dan tidak ambigu.

## 7. Decision Types

Baseline:

    SCOPE
    FEATURE
    BUSINESS_BEHAVIOR
    BUSINESS_RULE
    CONFLICT_RESOLUTION
    ASSUMPTION_ACCEPTANCE
    DATA_REQUIREMENT
    TERMINOLOGY
    PROCESS
    OTHER

Decision type bukan lifecycle status.

## 8. Options and Evidence

Jika alternatif material dipertimbangkan, artifact SHOULD mencatat options considered dan selected outcome.

Evidence/context SHOULD dicatat jika tersedia. Evidence tidak otomatis menjadi decision; authority tetap berasal dari manusia.

## 9. Affected Artifacts

Decision MUST mencatat affected artifacts/domain records yang diketahui terdampak bila ada downstream impact.

Affected artifacts bukan pengganti revisi artifact tersebut.

## 10. Relationship to REV/OQ/CON

Decision dapat:
- mengarahkan penanganan REV-xxx
- menjawab OQ-xxx
- menjadi resolusi authoritative terhadap CON-xxx

Historical findings/questions/conflicts tetap dipertahankan dan ditautkan.

    REV-xxx / OQ-xxx / CON-xxx
                ↓
        Human Decision ART-xxx
                ↓
        Downstream Revision
                ↓
          Review / Approval

## 11. Decision vs Approval

Decision menjawab apa yang diputuskan manusia.

Approval mengotorisasi artifact, perubahan, atau gate.

Contoh:
- Decision: Quiz tidak masuk LMS baru.
- Approval: Project Owner menyetujui PRD versi 2.0.

Keduanya tidak boleh dianggap sinonim.

## 12. Lifecycle

Decision artifact menggunakan lifecycle canonical Artifact & Metadata Convention:

    DRAFT
    IN_REVIEW
    REVIEWED
    READY_FOR_APPROVAL
    APPROVED
    ACCEPTED
    SUPERSEDED
    DEPRECATED

Decision hanya authoritative ketika human authority dan workflow requirements telah terpenuhi. APPROVED tidak boleh dipakai untuk menyamarkan keputusan yang belum dibuat manusia.

## 13. Supersession and History

Decision lama tidak dihapus atau ID-nya didaur ulang. Decision baru yang menggantikannya harus menggunakan versioning/supersession canonical.

Historical rationale, authority, dan relationship harus tetap dapat diaudit.

## 14. Storage

Official decision artifacts disimpan pada:

    decisions/
    └── <decision-name>.md

Decision tidak boleh hanya hidup sebagai chat instruction, temporary note, atau implicit context.

## 15. Baseline Record

    ---
    document: DECISION
    artifact_id: ART-xxx
    version: 1.0
    status: DRAFT
    owner: PROJECT_OWNER
    ---

    # <Decision Title>

    ## Decision Type
    <type>

    ## Decision
    <explicit decision>

    ## Decision Maker
    <authorized human authority>

    ## Context
    <question / issue>

    ## Options Considered
    <if applicable>

    ## Selected Outcome
    <selected outcome>

    ## Rationale
    <reasoning>

    ## Evidence
    - <artifact / record / source>

    ## Affected Artifacts
    - <artifact / record>

    ## Related Records
    - OQ-xxx
    - CON-xxx
    - REV-xxx

    ## Downstream Impact
    <known impact>

## 16. Source of Truth

Authoritative human decision memiliki priority tertinggi terhadap conflicting lower-authority documentation.

Decision artifact tidak otomatis mengubah downstream documentation. Artifact terdampak harus direvisi melalui workflow yang berlaku.

## 17. Traceability

Minimum:

    Evidence / Question / Conflict / Finding
                  ↓
           Human Decision
              ART-xxx
                  ↓
         Affected Artifact
                  ↓
           Requirement / Rule
                  ↓
          Review / Approval

## 18. Non-Boundaries

Convention ini tidak menentukan siapa pemilik business authority secara universal, isi keputusan tertentu, requirement content, review finding semantics, approval workflow detail, atau implementation detail.

## 19. Validation Checklist

- [ ] menggunakan ART-xxx
- [ ] document: DECISION
- [ ] decision maker teridentifikasi
- [ ] decision statement eksplisit
- [ ] context tersedia
- [ ] rationale tersedia jika relevan
- [ ] evidence dicatat jika tersedia
- [ ] affected artifacts dicatat jika ada
- [ ] related OQ/CON/REV dicatat jika relevan
- [ ] lifecycle mengikuti Artifact & Metadata Convention
- [ ] historical decision tidak dihapus
- [ ] AI tidak diposisikan sebagai decision authority
- [ ] downstream impact dapat ditelusuri

## 20. Definition of Done

Convention dianggap diterapkan ketika:
1. decision artifact memiliki canonical ART-xxx
2. storage location decisions/ tersedia
3. human authority boundary jelas
4. traceability input/downstream terdefinisi
5. relationship ke OQ-xxx, CON-xxx, REV-xxx terdefinisi
6. decision dan approval tidak tercampur
7. historical preservation terdefinisi
8. tidak ada competing HD-xxx identity convention

## 21. Change Control

Perubahan terhadap convention ini mengikuti Artifact & Metadata Convention dan memerlukan human authority yang sesuai.

## 22. Governing Principle

> AI may analyze and recommend. Humans decide. Decision artifacts preserve what humans decided. Downstream artifacts express that decision through the documentation workflow.
