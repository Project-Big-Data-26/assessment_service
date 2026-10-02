# Dokumentasi API Nalar

Dokumentasi ini mengikuti backend **API 2.1.0**: ekstraksi → qualification/penilaian manusia blind → gold snapshot → IndoBERT grade-aware ordinal, serta gold → pilot server-scored → CTT/IRT → review empiris manusia. Gemini blind N=3 tersedia untuk silver penelitian; Claude API tetap target.

## Mulai menggunakan sistem

- [27 runbook CTT/IRT dan pilot](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md): demo Rasch/2PL/3PL langsung, matriks nyata, API, gold-only delivery dan empirical review.
- [12 endpoint aktual](12_ENDPOINT_MASTER_REFERENCE.md): dihasilkan dari kode FastAPI, bukan daftar target.
- [09 kontrak/schema](09_JSON_SCHEMA_REFERENCE.md): OpenAPI dan JSON Schema aktual.
- [25 pipeline ordinal](25_GRADE_AWARE_ORDINAL_PIPELINE.md): training, blind silver, audit, calibration dan promotion.
- [Indeks hasil validasi kelas 1–6](../output/pretest/README.md): bundle advisory; bukan gold manusia atau data respons siswa.

## Keputusan domain dan proses

Head 1 knowing/applying/reasoning; Head 2 factual/conceptual/procedural/metacognitive; Head 3 Easy/Medium/Hard sebagai intended difficulty relatif grade. C1–C6 hanya legacy /v1. KKO petunjuk eksperimen, bukan label.

Default training grade-aware-ordinal-v2: IndoBERT/LoRA shared, dua multiclass heads dan ordinal difficulty + grade embedding. Parallel/conditioned tetap ablation. Artifact silver/research-only, unapproved atau gagal promotion tidak servable.

Tiga run LLM blind/adjudikasi menghasilkan silver advisory sebelum comparison model. Tiga ahli manusia membentuk gold dari penilaian awal blind yang dikunci, consensus/discussion dan senior adjudication bila diperlukan. Agreement AI bukan calibrated confidence/gold.

Pilot memakai human-gold checksum/version/key/solution. Identity dan correctness server; opsi publik opaque; skip/missing null. CTT/IRT mengukur populasi/family/grade/form/time window tertentu. Empirical result tidak mengubah domain/knowledge/intended difficulty otomatis. Ahli retain/revise/quarantine; held version dikecualikan dari delivery dan freeze berikutnya.

## Peta dokumen

| Dokumen | Fokus |
|---|---|
| [01](01_API_ARCHITECTURE.md) | Boundary FastAPI, auth, storage dan target lanjutan |
| [02](02_QUESTION_API.md) | Authoring target dan immutable version |
| [03](03_EXTRACTION_API.md) | Ekstraksi/staging/import |
| [04](04_CLASSIFICATION_API.md) | Classifier ordinal dan blind LLM |
| [05](05_AI_DECISION_ARBITRATION_API.md) | Blind manusia, consensus/discussion/adjudication |
| [06](06_STUDENT_RESPONSE_API.md) | Single-choice server-scored dan NA |
| [07](07_PSYCHOMETRICS_API.md) | CTT, gate, estimator/diagnostics IRT |
| [08](08_ASSESSMENT_DELIVERY_API.md) | Gold blueprint, peserta/session/delivery |
| [09](09_JSON_SCHEMA_REFERENCE.md) | Kontrak implementasi vs gateway target |
| [10](10_SWAGGER_POSTMAN_GUIDE.md) | Smoke API dan contract checks |
| [11](11_FRONTEND_INTEGRATION_ADAPTER.md) | Port siswa/operator/ahli |
| [12](12_ENDPOINT_MASTER_REFERENCE.md) | Inventaris endpoint aktual otomatis |
| [13](13_SYSTEM_ASPECTS_EXPLANATION.md) | Aspek sistem dan batas kesiapan |
| [14](14_TAXONOMY_6X4X3_MAP.md) | Rubrik 3×4×3; nama legacy tetap |
| [15](15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md) | Feedback learning terkontrol |
| [16](16_CONTROLLED_QUESTION_VARIATION_GENERATION.md) | Generator varian target |
| [17](17_MONGODB_DATA_MODEL_ERD.md) | MongoDB gold/auth + SQLite pilot, ERD target |
| [18](18_CLAUDE_PROVIDER_SETUP.md) | Claude target dan pemisahan provider aktif |
| [19](19_GEMINI_SMOKE_EVALUATION.md) | Smoke legacy, berbeda dari Gemini blind aktif |
| [21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md) | Pipeline agentic dan adapter impor |
| [22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md) | Operasi anotasi/gold/model |
| [23](23_EMPIRICAL_VALIDATION_FEEDBACK_FLOW.md) | Diagram aktual delivery → CTT/IRT → ahli |
| [24](24_INDOBERT_FINETUNING_LLM_REASONING_DETAIL.md) | Diagram 4K ordinal training dan blind LLM |
| [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md) | Gate/audit/training ordinal |
| [26](26_KELAS2_BLIND_VALIDATION.md) | Status batch advisory kelas 2 |
| [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md) | Eksekusi CTT/IRT dan pilot |

Diagram end-to-end lama bernomor 20 telah dihapus pada worktree; tautan aktif memakai 23/24. `schemas/nalar-api.schema.json` tetap desain gateway luas. Kontrak implementasi ada pada `schemas/openapi.json` dan `schemas/implemented-api.schema.json`.

## Kesiapan

Implemented berarti kode/tes tersedia, bukan bahwa cloud, ahli, gold/model final atau respons siswa telah tersedia. SQLite pilot lokal dapat berjalan tanpa MongoDB untuk CLI assessment dari gold JSON; analisis matriks/demo tidak memerlukan database/provider. Anotasi dan keputusan ahli API membutuhkan provisioning MongoDB/auth. Hasil simulasi diberi origin synthetic.

UI siswa, generation/variants, public authoring, CAT, DIF/equating/linking, model polytomous, Redis jobs dan multihost deployment tetap target. Tidak ada publish/retrain otomatis. Secret dibaca dari environment atau .env privat sesuai [template](../.env.example); jangan commit credentials atau event/estimasi individual.

Jumlah soal hasil ekstraksi dan jumlah run LLM bukan ukuran sampel siswa. Snapshot staging historis berisi 1.254 soal/46 file bab; status draft bukan expert-validated.
