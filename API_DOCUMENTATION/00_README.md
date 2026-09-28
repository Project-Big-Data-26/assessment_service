# Dokumentasi API Nalar

Dokumen ini mendeskripsikan arsitektur bertahap: ekstraksi → qualification dan gold blind → IndoBERT → fase Claude berikutnya → pilot → psikometrik. Repo Python mempertahankan `/v1` Bloom C1–C6 sebagai legacy, sedangkan fondasi `/v2` 3×4×3 sudah diimplementasikan tetapi belum diprovision dan belum memiliki gold/model final. Istilah `target` tidak berarti fitur sudah aktif; lihat status nyata pada [dokumen 22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md).

## Keputusan domain yang berlaku

- Head 1: `knowing/applying/reasoning` menurut domain kognitif matematika TIMSS dan AKM.
- Head 2: `factual/conceptual/procedural/metacognitive` dari dimensi pengetahuan Revised Bloom.
- Head 3: `Easy/Medium/Hard` sebagai *intended difficulty* yang dinilai sebelum pilot; difficulty empiris terpisah.
- C1–C6 tidak menjadi target model. KKO adalah `features.lexical.detectedKKO` dan hanya petunjuk; label pakar mengikuti bukti penyelesaian.
- IndoBERT memberi prediksi dan ketidakpastian. Claude mengaudit usulan IndoBERT. Keduanya merupakan satu pipeline berurutan.
- Tiga pakar matematika membuat penilaian blind yang dikunci, lalu mereview proposal AI. Keputusan 3–0/2–1 dicatat per head; 1–1–1 atau bukti kurang melalui adjudikasi manusia.
- Seed dataset untuk fine-tuning IndoBERT harus dibentuk dari penilaian blind manusia **sebelum** ada model produksi.
- Pilot hanya untuk item expert-validated. Psikometrik mengukur perilaku item pada populasi tertentu dan tidak otomatis mengubah domain atau dimensi pengetahuan.

## Peta dokumen

| Nomor | Fokus |
|---|---|
| [01](01_API_ARCHITECTURE.md) | Boundary, aktor, keamanan, status target |
| [02](02_QUESTION_API.md) | Authoring, versi, lifecycle |
| [03](03_EXTRACTION_API.md) | Ekstraksi dan authoring candidate |
| [04](04_CLASSIFICATION_API.md) | Input, fitur KKO, IndoBERT, Claude |
| [05](05_AI_DECISION_ARBITRATION_API.md) | Tiga annotator, konsensus dan adjudikasi |
| [06](06_STUDENT_RESPONSE_API.md) | Event jawaban terikat delivery |
| [07](07_PSYCHOMETRICS_API.md) | CTT, populasi, keputusan sesudah pilot |
| [08](08_ASSESSMENT_DELIVERY_API.md) | Session dan item publik |
| [09](09_JSON_SCHEMA_REFERENCE.md) | DTO dan versi schema |
| [10](10_SWAGGER_POSTMAN_GUIDE.md) | OpenAPI, Postman, contract test |
| [11](11_FRONTEND_INTEGRATION_ADAPTER.md) | Port frontend dan review UI |
| [12](12_ENDPOINT_MASTER_REFERENCE.md) | Inventaris endpoint target |
| [13](13_SYSTEM_ASPECTS_EXPLANATION.md) | Rasional dan kesiapan sistem |
| [14](14_TAXONOMY_6X4X3_MAP.md) | Rubrik label 3 × 4 × 3; nama file lama dipertahankan |
| [15](15_AUTONOMOUS_AI_PSYCHOMETRIC_LEARNING_ARCHITECTURE.md) | Arsitektur end to end dan model learning |
| [16](16_CONTROLLED_QUESTION_VARIATION_GENERATION.md) | Generasi varian terkontrol, tahap lanjutan |
| [17](17_MONGODB_DATA_MODEL_ERD.md) | Data model MongoDB dan ERD |
| [18](18_CLAUDE_PROVIDER_SETUP.md) | Konfigurasi Claude dan migrasi environment |
| [19](19_GEMINI_SMOKE_EVALUATION.md) | Catatan historis Gemini; bukan provider aktif |
| [20](20_END_TO_END_VALIDATION_FLOW.md) | Diagram lengkap dari bootstrap model sampai psikometrik, dengan tech stack dan cabang error |
| [21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md) | Pipeline agentic pretest hasil merge, kontrak staging, progres dan adapter ke API target |
| [22](22_INDOBERT_V2_IMPLEMENTATION_RUNBOOK.md) | Implementasi aktual 3×4×3, keamanan anotasi, perintah operasional dan gate eksternal |

Schema target ada pada [bundle JSON](schemas/nalar-api.schema.json). Bila kode/schema lama belum bermigrasi, dokumen menyebutnya secara eksplisit. Setiap breaking semantic change membutuhkan versi rubric, dataset, model, API/schema, dan migration plan.

## Peran dan status

Teacher menulis dan memperbaiki konten lalu submit. Teacher tidak memutuskan label final pada item sendiri. Tiga ahli matematika melakukan review dengan identitas, keahlian, konflik kepentingan dan alasan keputusan yang dapat diaudit. System admin mengelola operasi, bukan sumber gold pedagogis.

Status: `implemented` = ada dan diuji dalam repo; `implemented_unprovisioned` = kodenya ada tetapi membutuhkan cloud/akun/data manusia; `implemented_local` = batch/CLI lokal; `prototype` = terbatas; `target` = belum selesai; `future` = di luar fase. Importer 1.254 candidate, kontrak 3×4×3, Atlas repository, UI blind, consensus/adjudication, snapshot/split, baseline, LoRA trainer, kalibrasi, packaging, dan route `/v2` kini tersedia. Gold label, training final, deployment PaaS, dan pembukaan frozen test belum dapat dilakukan tanpa ahli, secrets, aset privat, dan persetujuan dosen.

Snapshot artefak hasil merge memuat 1.254 soal pada 46 file bab: 45 bab valid menurut status tersimpan, satu gagal, dan 951 item berstatus staging `draft`. Status tersebut berarti candidate ekstraksi siap menuju gate berikutnya, bukan `expert_validated`. Detail dan batas reproduksibilitas ada pada [dokumen 21](21_PRETEST_AGENTIC_PIPELINE_INTEGRATION.md).

## Lingkungan dan folder lama

`project_assessment` sudah kosong; file tracked-nya sudah berstatus deleted sebelum pembaruan ini. Tidak ada `.env` atau URI MongoDB nyata di folder tersebut untuk dipindah. [Template root](../.env.example) kini memuat nama variabel target `ANTHROPIC_API_KEY`, `CLAUDE_MODEL`, `MONGODB_URI`, dan `AI_SERVICE_URL`. Jangan commit `.env`, token, atau URI yang mengandung kredensial. Instalasi Claude CLI lokal tidak dengan sendirinya membuktikan koneksi API worker; lihat dokumen 18.

## Landasan inti

[TIMSS 2023 matematika](https://timssandpirls.bc.edu/timss2023/frameworks/pdf/T23_Frameworks_Ch1_Mathematics.pdf), [AKM numerasi Pusmendik](https://pusmendik.kemdikbud.go.id/an/Framework_AKM_31032022.pdf), [Revised Bloom (Krathwohl, 2002)](https://eric.ed.gov/?id=EJ667155), [IndoNLU/IndoBERT](https://aclanthology.org/2020.aacl-main.85/), dan [Claude Messages API](https://platform.claude.com/docs/en/api/messages/create).
