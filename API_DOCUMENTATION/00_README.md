# Dokumentasi API Nalar

Folder ini adalah kontrak bersama antara frontend, API gateway, layanan AI, worker generation, worker psikometrik, database, dan QA. Kontrak sengaja tidak bergantung pada satu implementasi frontend sehingga UI prototype dapat dilepas dan diganti tanpa mengubah domain backend.

## Sumber kebenaran arsitektur

- [`15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md`](15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md) adalah arsitektur target sistem utama.
- [`16_CONTROLLED_QUESTION_VARIATION_GENERATION.md`](16_CONTROLLED_QUESTION_VARIATION_GENERATION.md) adalah arsitektur target subsistem generasi variasi soal.
- Dokumen 01-14 menerjemahkan kedua arsitektur tersebut menjadi kontrak API, schema, UI adapter, dan aturan domain.
- [`17_MONGODB_DATA_MODEL_ERD.md`](17_MONGODB_DATA_MODEL_ERD.md) mendefinisikan model data MongoDB dan relasi logisnya.
- [`schemas/nalar-api.schema.json`](schemas/nalar-api.schema.json) adalah bundle JSON Schema machine-readable untuk DTO publik utama.

## Peran teacher

Teacher adalah **author**, bukan reviewer atau annotator. Teacher dapat:

- membuat soal secara manual atau mengimpor sumber;
- memperbaiki draft hasil ekstraksi;
- mengubah authoring content miliknya;
- mengirim versi soal ke workflow otomatis;
- melihat status, warning, dan hasil screening yang aman ditampilkan.

Teacher tidak menetapkan label final, tidak menjadi adjudikator, tidak melakukan approval publikasi, dan tidak dapat melewati quality gate. Konflik IndoBERT-LLM ditangani automated LLM adjudication; konflik yang tidak selesai masuk quarantine.

## Daftar dokumen

| File | Isi |
|---|---|
| [`01_API_ARCHITECTURE.md`](01_API_ARCHITECTURE.md) | Topologi, role, boundary frontend, versioning, job, error, dan security. |
| [`02_QUESTION_API.md`](02_QUESTION_API.md) | Teacher authoring, revision, submit, versioning, dan status soal. |
| [`03_EXTRACTION_API.md`](03_EXTRACTION_API.md) | Ekstraksi sumber menjadi authoring candidate, bukan validasi final. |
| [`04_CLASSIFICATION_API.md`](04_CLASSIFICATION_API.md) | IndoBERT-LLM screening dan klasifikasi taksonomi. |
| [`05_AI_DECISION_ARBITRATION_API.md`](05_AI_DECISION_ARBITRATION_API.md) | AI agreement, risk routing, dan LLM adjudication otomatis. |
| [`06_STUDENT_RESPONSE_API.md`](06_STUDENT_RESPONSE_API.md) | Delivery-bound response event dan server-side scoring. |
| [`07_PSYCHOMETRICS_API.md`](07_PSYCHOMETRICS_API.md) | Analisis varian/family, CTT, dan automated item routing. |
| [`08_ASSESSMENT_DELIVERY_API.md`](08_ASSESSMENT_DELIVERY_API.md) | Session, delivery instance, public item DTO, dan penyembunyian kunci. |
| [`09_JSON_SCHEMA_REFERENCE.md`](09_JSON_SCHEMA_REFERENCE.md) | Aturan dan daftar JSON Schema publik. |
| [`10_SWAGGER_POSTMAN_GUIDE.md`](10_SWAGGER_POSTMAN_GUIDE.md) | OpenAPI, Postman, mock, dan contract testing. |
| [`11_FRONTEND_INTEGRATION_ADAPTER.md`](11_FRONTEND_INTEGRATION_ADAPTER.md) | Port/adapter frontend yang dapat dicopot-pasang. |
| [`12_ENDPOINT_MASTER_REFERENCE.md`](12_ENDPOINT_MASTER_REFERENCE.md) | Master endpoint target, caller, side effect, dan idempotency. |
| [`13_SYSTEM_ASPECTS_EXPLANATION.md`](13_SYSTEM_ASPECTS_EXPLANATION.md) | Rasional sistem, batas klaim, status implementasi, dan prioritas. |
| [`14_TAXONOMY_6X4X3_MAP.md`](14_TAXONOMY_6X4X3_MAP.md) | Ruang 72 kombinasi dan penggunaannya sebagai target/screening. |
| [`15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md`](15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md) | Arsitektur autonomous hybrid AI end-to-end. |
| [`16_CONTROLLED_QUESTION_VARIATION_GENERATION.md`](16_CONTROLLED_QUESTION_VARIATION_GENERATION.md) | Controlled question variation generation. |
| [`17_MONGODB_DATA_MODEL_ERD.md`](17_MONGODB_DATA_MODEL_ERD.md) | Koleksi, atribut, index, embedding/reference, dan ERD MongoDB. |
| [`19_GEMINI_SMOKE_EVALUATION.md`](19_GEMINI_SMOKE_EVALUATION.md) | Prosedur, hasil, latency, konsistensi, dan keputusan smoke evaluation Gemini. |

## Status kontrak

Dokumentasi membedakan:

- `implemented`: tersedia pada repository dan dapat diuji;
- `prototype`: tersedia, tetapi kontrak atau kontrol produksinya belum lengkap;
- `target`: desain yang harus dikembangkan;
- `future`: tidak termasuk MVP.

Versi API target tetap `/api/v1`. Breaking change memakai `/api/v2`. Dokumentasi target tidak boleh dianggap sebagai bukti bahwa endpoint sudah aktif.

Kondisi implementasi tahap pertama:

- UI teacher dapat membuat, merevisi, membaca, dan submit draft; data tersimpan sebagai file di `data/local/`, tanpa MongoDB.
- Worker lokal memiliki validasi schema/relasi, verifikasi aritmetika terbatas, adapter IndoBERT dan LLM, agreement/adjudication, risk gate, dan recovery run setelah restart.
- Adapter AI hanya menghasilkan `provisional` jika artefak IndoBERT sungguhan telah dinyatakan layak, LLM sungguhan tersedia, dan risk policy per-head sudah dikalibrasi/disetujui. Tanpanya workflow `failed` dan draft tidak hilang. Simulasi hanya ada dalam tes.
- PDF analyzer tetap prototype ekstraksi. MongoDB, generation service, secure student delivery, feedback psikometrik, dan model registry masih target.
- Workflow dua reviewer manusia dan educator verification adalah desain lama dan tidak lagi menjadi target arsitektur.

## Urutan baca

- Frontend: 01, 02, 03, 08, 09, 11, dan 12.
- Backend/gateway: 01-12 dan 17.
- AI/generation: 04, 05, 09, 14, 15, dan 16.
- Data/psychometrics: 06, 07, 13, 15, 16, dan 17.
- QA: 09, 10, 12, serta acceptance gate pada 15-16.
