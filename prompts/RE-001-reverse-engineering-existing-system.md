# RE-001 — Reverse Engineering Existing System

## Prompt Metadata

| Field | Value |
|---|---|
| **PROMPT-ID** | `RE-001` |
| **TOPIK** | Reverse Engineering — Existing System |
| **MODEL** | Claude Opus 4.6 Thinking |
| **INPUT / FILE YANG DIBACA** | Project Governance & Documentation Foundation + Reverse Engineering Role Contract + Legacy LMS Repository |
| **OUTPUT / FILE YANG DIHASILKAN** | `analysis/existing-system.md` |
| **TUJUAN** | Merekonstruksi dan mendokumentasikan bagaimana legacy LMS benar-benar bekerja berdasarkan evidence yang dapat diverifikasi |
| **OUTPUT FORMAT** | Markdown sesuai Artifact & Metadata Convention |

---

## Objective

Lakukan **Reverse Engineering menyeluruh terhadap legacy LMS** untuk menghasilkan dokumentasi tentang **existing system yang benar-benar ada dan bagaimana sistem tersebut benar-benar bekerja**.

Output utama task ini adalah:

`analysis/existing-system.md`

Artifact tersebut akan menjadi baseline evidence untuk aktivitas analysis berikutnya.

**Jangan menentukan bagaimana sistem baru seharusnya dibangun.**

---

## Execution Instructions

### Phase 1 — Read Project Governance First

Sebelum membaca atau menganalisis source code legacy, baca terlebih dahulu dokumen governance berikut:

1. `AI-DOCUMENTATION-PROMPT-CONTRACT-v1.md`
2. `ROLE-SPECIFIC-CONTRACT-REVERSE-ENGINEERING-RESEARCHER.md`
3. `ARTIFACT-METADATA-CONVENTION-v1.md`
4. `LMS-REWRITE-DOCUMENTATION-WORKFLOW.md`
5. `OPEN-QUESTION-CONFLICT-CONVENTION-v1.md`
6. template/struktur existing-system yang tersedia di repository
7. `analysis/legacy-schema-snapshot.md` sebagai supporting evidence

Jika salah satu governance document yang diwajibkan tidak tersedia atau tidak dapat dibaca:

**BLOCK TASK.**

Jangan membuat aturan pengganti berdasarkan asumsi.

### Phase 2 — Inspect Legacy Repository

Setelah governance dipahami, lakukan reconnaissance terhadap legacy LMS repository.

Identifikasi sekurang-kurangnya:

- repository structure;
- application entry points;
- framework/runtime;
- module/component structure;
- routing;
- controllers/services/use cases;
- models/entities;
- database access;
- authentication;
- authorization;
- configuration;
- external integrations;
- background jobs;
- scheduled tasks;
- event/listener mechanisms;
- file/storage handling;
- notification mechanisms;
- API endpoints;
- UI/application flows;
- tests;
- deployment/runtime-related configuration jika tersedia.

Jangan berhenti pada directory listing.

Tujuan reconnaissance adalah memahami **hubungan antar bagian sistem**, bukan sekadar mencatat nama file.

### Phase 3 — Reconstruct System Behavior

Untuk setiap area yang relevan, telusuri execution path sejauh evidence memungkinkan.

Contoh:

`Entry Point → Route → Controller → Service/Use Case → Model → Database`

atau:

`User Action → Request → Validation → Business Logic → Persistence → Response`

atau:

`Scheduled Trigger → Job → Service → Database/External Integration`

Identifikasi:

- siapa/apa yang memicu flow;
- entry point;
- komponen yang dipanggil;
- decision point;
- data yang digunakan;
- data yang berubah;
- external dependency;
- output/side effect;
- kondisi yang menyebabkan flow berhenti atau bercabang.

Jika sebuah flow tidak dapat direkonstruksi secara reliable, jangan melengkapinya dengan asumsi.

Tandai sebagai `UNKNOWN` atau `CONFLICT` sesuai evidence.

### Phase 4 — Identify Observable Business Behavior

Dokumentasikan behavior bisnis yang **dapat diamati dari implementation legacy**.

Contoh area:

- user/account behavior;
- authentication;
- authorization;
- enrollment;
- course/module behavior;
- assessment;
- grading;
- submission;
- attendance;
- notification;
- reporting;
- administration;
- content management;
- payment/integration;
- data lifecycle.

Untuk setiap behavior:

- jelaskan behavior yang ditemukan;
- tunjukkan evidence;
- bedakan direct behavior dengan derived conclusion;
- jangan menyebut behavior sebagai requirement sistem baru.

Gunakan istilah **legacy behavior**, **existing behavior**, atau istilah setara jika diperlukan untuk menjaga boundary.

### Phase 5 — Analyze Data Flow

Gunakan source code dan `analysis/legacy-schema-snapshot.md` sebagai evidence pendukung.

Petakan:

- entity/model;
- table;
- relationship;
- foreign key/reference;
- read/write operation;
- ownership;
- lifecycle;
- data transformation;
- dependency antar data.

Jangan membuat schema baru.

Jika terdapat perbedaan antara source code dan schema snapshot:

**jangan memilih salah satunya secara diam-diam.**

Catat sebagai `CONFLICT` dan sertakan evidence dari kedua sisi.

### Phase 6 — Analyze Architecture and Dependencies

Rekonstruksi architecture legacy berdasarkan apa yang benar-benar ditemukan.

Identifikasi:

- architectural layers;
- module boundaries;
- dependency direction;
- shared components;
- tightly coupled components;
- external systems;
- infrastructure dependencies;
- configuration dependencies;
- runtime assumptions.

Jangan mengubah hasil observasi menjadi rekomendasi architecture baru.

### Phase 7 — Reachability and Activity Awareness

Jangan menganggap semua code yang ada sebagai active behavior.

Untuk setiap komponen penting, jika memungkinkan tentukan:

- apakah memiliki reference;
- apakah reachable dari entry point;
- apakah digunakan oleh flow yang teridentifikasi;
- apakah hanya dead/orphan code;
- apakah activation bergantung pada configuration;
- apakah activation bergantung pada environment;
- apakah statusnya tidak dapat dipastikan.

Jika tidak dapat memastikan:

`UNKNOWN`

**Code existence ≠ active behavior.**

### Phase 8 — Evidence Classification

Setiap substantive conclusion harus diklasifikasikan:

- `FACT`
- `DERIVED`
- `UNKNOWN`
- `CONFLICT`

Gunakan:

**FACT** — behavior dapat dibuktikan langsung dari legacy evidence.

**DERIVED** — conclusion berasal dari beberapa evidence yang saling mendukung dan reasoning dapat dijelaskan.

**UNKNOWN** — evidence belum cukup.

**CONFLICT** — terdapat evidence yang saling bertentangan.

Confidence (`HIGH`, `MEDIUM`, `LOW`) dapat digunakan sebagai atribut tambahan, tetapi tidak menggantikan evidence classification.

### Evidence Priority

Gunakan prioritas:

1. **Direct legacy evidence**
2. **Corroborated legacy evidence**
3. **Derived analysis**
4. **Model inference**

Model inference **tidak boleh dipromosikan menjadi FACT** hanya karena terlihat masuk akal.

Jika harus menggunakan inference:

- tandai `DERIVED` bila reasoning benar-benar dapat ditelusuri;
- jika tidak cukup evidence, gunakan `UNKNOWN`.

---

## Critical Boundary

Sepanjang task ini, selalu pisahkan:

### WHAT EXISTS

Apa yang benar-benar ditemukan pada legacy system.

dari:

### WHAT SHOULD EXIST

Apa yang mungkin dibutuhkan, diinginkan, atau dianggap lebih baik pada sistem baru.

**RE-001 hanya mendokumentasikan WHAT EXISTS.**

Jangan memasukkan:

- requirement baru;
- redesign;
- improvement;
- best practice recommendation;
- replacement proposal;
- feature retention decision;
- feature removal decision;
- target architecture;
- target database;
- target API;
- target UI.

Jika ide tersebut muncul selama investigation, jangan memasukkannya sebagai existing-system fact.

Jika relevan, catat hanya sebagai open question atau boundary note tanpa menjadikannya requirement.

---

## Unknown & Conflict Handling

Jika menemukan ambiguity:

`UNKNOWN`

Jika menemukan evidence yang bertentangan:

`CONFLICT`

Jangan menyelesaikan ambiguity dengan asumsi, convention framework, common practice, atau tebakan model.

Jika conflict/unknown berdampak signifikan terhadap downstream analysis, buat follow-up question/finding sesuai convention project.

---

## Output Requirements

Buat atau update:

`analysis/existing-system.md`

Artifact harus memberikan gambaran terstruktur mengenai, sesuai relevansi dan evidence:

1. metadata artifact;
2. scope investigation;
3. repository/system overview;
4. technology/runtime;
5. architecture;
6. application structure;
7. major modules/features;
8. execution flows;
9. observable business behavior;
10. authentication & authorization;
11. data architecture/data flow;
12. integrations;
13. background/scheduled processing;
14. configuration/environment dependencies;
15. tests/evidence;
16. reachability/activity observations;
17. constraints;
18. unknowns;
19. conflicts;
20. evidence/traceability;
21. boundary antara existing behavior dan non-existing/new-system concerns.

Sesuaikan struktur dengan template/convention yang ditemukan dalam governance repository.

**Jangan mengarang section hanya untuk mengisi template.**

Jika sebuah area tidak ditemukan evidence-nya, gunakan `UNKNOWN` atau jelaskan bahwa area tersebut belum dapat diverifikasi.

---

## Traceability Requirements

Setiap klaim penting harus memiliki traceability ke evidence.

Gunakan reference yang memungkinkan reviewer menemukan kembali:

- file;
- path;
- module;
- function/class;
- schema/table;
- configuration;
- test;
- atau evidence relevan lainnya.

Traceability harus cukup untuk memungkinkan reviewer melakukan verification.

---

## Review Preparation

Sebelum menyatakan task selesai, lakukan self-check:

### Evidence

- Apakah setiap FACT memiliki evidence?
- Apakah DERIVED conclusion memiliki reasoning?
- Apakah UNKNOWN benar-benar tidak dipaksakan menjadi conclusion?
- Apakah CONFLICT dicatat ketika evidence bertentangan?

### Boundary

- Apakah ada requirement baru yang terselip?
- Apakah ada recommendation untuk sistem baru?
- Apakah legacy behavior secara tidak sengaja diperlakukan sebagai target behavior?

### Completeness

- Apakah major application flow sudah ditelusuri?
- Apakah major modules sudah dipetakan?
- Apakah data flow utama sudah ditelusuri?
- Apakah dependency penting sudah diidentifikasi?
- Apakah configuration/reachability issue sudah diperhatikan?

### Traceability

- Apakah reviewer dapat menemukan evidence dari setiap klaim penting?
- Apakah source code dan schema snapshot yang bertentangan sudah ditandai?

### Governance

- Apakah metadata mengikuti convention?
- Apakah artifact mengikuti workflow stage?
- Apakah role boundary tetap dipatuhi?

---

## Blocking Conditions

**BLOCK dan laporkan secara eksplisit** jika:

- governance document wajib tidak tersedia;
- legacy repository tidak dapat diakses;
- evidence minimum tidak tersedia;
- output tidak dapat memenuhi metadata/traceability requirement;
- terdapat critical ambiguity yang membutuhkan human decision;
- executor diminta menentukan requirement/design baru.

Jangan menghasilkan artifact seolah-olah valid jika prerequisite task tidak terpenuhi.

---

## Final Output

Setelah investigation selesai:

1. Simpan hasil utama ke:
   `analysis/existing-system.md`
2. Pastikan metadata lengkap.
3. Pastikan evidence classification dan traceability konsisten.
4. Pastikan `WHAT EXISTS` tidak tercampur dengan `WHAT SHOULD EXIST`.
5. Pastikan unknown/conflict tidak disembunyikan.
6. Laporkan secara ringkas:
   - artifact yang dihasilkan;
   - area yang berhasil direkonstruksi;
   - major unknowns;
   - major conflicts;
   - blocking issues jika ada;
   - readiness untuk independent review.

**Jangan menganggap artifact sebagai APPROVED.**

Approval tetap berada pada governance/review process dan human decision maker.
