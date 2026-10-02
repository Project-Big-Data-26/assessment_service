# Runbook Implementasi IndoBERT v2 3×4×3

## Status nyata

Kode vertical slice tersedia; keberadaan kode bukan bukti gold/model final atau deployment. Provisioning Atlas/PaaS/S3, akun/anotasi ahli dan gold harus diverifikasi operator. `/v2/classify` tetap 503 bila artefak research-only, unapproved, atau gagal data/anti-collapse/promotion/integrity gate. Pipeline terbaru mengikuti [25](25_GRADE_AWARE_ORDINAL_PIPELINE.md).

`/v1/classify` tetap legacy C1–C6. Gemini blind silver runtime tersedia; Claude API tetap target. Delivery single-choice, scoring server, CTT batch dan IRT Rasch/2PL/3PL kini tersedia pada [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md). Analisis empiris tetap research/advisory, tidak mempromosikan classifier.

## Komponen kode

| Komponen | Lokasi | Status |
|---|---|---|
| Kontrak 3×4×3 dan serializer | `app/classification/v2` | implemented |
| Import immutable `babNN.json` | `app/ingestion/pretest_import.py` | implemented |
| Auth, UI blind, CSRF, IDOR guard | `app/annotation` | implemented, belum diprovision |
| Atlas collections/index/transaction | `app/annotation/repository.py` | implemented, belum diprovision |
| Consensus dan agreement | `app/annotation/consensus.py` | implemented |
| Snapshot dan group split | `app/training/v2/dataset.py` | implemented |
| Baseline dan LoRA CPU | `app/training/v2` | implemented; default grade-aware ordinal, parallel/conditioned tetap ablation legacy |
| Kalibrasi, confidence+entropy routing dan artefak checksum | `app/classification/v2` | implemented |
| API advisory | `/v2/*` | implemented, 503 tanpa artefak |
| Pilot dan response event | `app/assessment` | implemented_local; gold-only, server-scored, SQLite |
| CTT, Rasch/2PL/3PL dan empirical review | `app/psychometrics`, `scripts/psychometrics.py` | implemented; data/asumsi gate dan human feedback |

## 1. Verifikasi candidate lokal

```powershell
.\.venv\Scripts\python.exe scripts\import_candidates_v2.py `
  --source output\pretest `
  --output data\processed\question_versions_v2.jsonl
```

Pada snapshot kerja saat implementasi, 1.254 record terbaca: 749 `pending_qualification`, 283 `revision_required`, dan 222 `out_of_scope` untuk model SD. Angka itu adalah routing awal, bukan hasil penilaian ahli.

## 2. Provision dan muat Atlas

Isi secret store berdasarkan `.env.example`; jangan commit nilai aktual. Kemudian:

```powershell
.\.venv\Scripts\python.exe scripts\bootstrap_annotation_admin.py --username admin-riset
.\.venv\Scripts\python.exe scripts\load_candidates_to_atlas.py --source output\pretest
```

Buat tiga profil `primary_annotator` dan satu `senior_adjudicator`, lengkap dengan bukti keahlian, deklarasi konflik kepentingan, dan consent. Setelah itu buat assignment:

```powershell
.\.venv\Scripts\python.exe scripts\provision_expert_account.py --help
.\.venv\Scripts\python.exe scripts\create_annotation_assignments.py `
  --expert-id EXPERT-01 --expert-id EXPERT-02 --expert-id EXPERT-03
```

Reviewer masuk melalui `/internal/v2/ui/login`. Prediksi AI, suara ahli lain, consensus, jawaban agen, dan tingkat kesulitan agen tidak dikirim ke reviewer. Submission terkunci dalam transaction; koreksi harus berupa compensating event, bukan edit.

## 3. Consensus, agreement, dan adjudikasi

```powershell
.\.venv\Scripts\python.exe scripts\agreement_report_v2.py --output reports\agreement-v1.json
.\.venv\Scripts\python.exe scripts\materialize_consensus.py
```

Pola 3–0 menjadi unanimous dan 2–1 majority dengan dissent tersimpan. Pola 1–1–1, abstain, konflik konten/kunci, atau bukti kurang masuk `discussion_required`. Tiga ahli membahasnya secara terstruktur; hanya konflik yang masih unresolved menjadi `pending_adjudication` untuk ahli senior keempat. Agreement tetap dihitung dari suara awal sebelum diskusi: pairwise percent agreement, Fleiss’ kappa, Krippendorff’s alpha nominal, distribusi pola, dan bootstrap 95% CI.

## 4. Freeze dataset

```powershell
.\.venv\Scripts\python.exe scripts\freeze_dataset_v2.py `
  --snapshot-id sd-math-gold-v1 `
  --output data\processed\sd-math-gold-v1.snapshot.json
```

Snapshot memisahkan SD 1–6 dari expansion SMP/SMA. Test tetap `locked` jika validation atau test memiliki kurang dari 15 item untuk salah satu kelas label. Source exercise, stimulus bersama, dan duplicate family di-union sebelum split 70/15/15.

## 5. Baseline, search, tiga seed, dan packaging

```powershell
.\.venv\Scripts\python.exe scripts\evaluate_baselines_v2.py `
  --snapshot data\processed\sd-math-gold-v1.snapshot.json `
  --output reports\baseline-validation-v1.json

.\.venv\Scripts\python.exe -m app.training.v2.train_lora `
  --snapshot data\processed\sd-math-gold-v1.snapshot.json `
  --architecture conditioned-difficulty-v1 `
  --resume
```

Trainer menjalankan grid `rank {8,16} × LR {1e-4,2e-4}` dengan seed 42, lalu konfigurasi terbaik pada seed 13, 42, dan 73. Artefak utama memakai seed 42 dan mencatat stabilitas tiga seed. Pada `conditioned-difficulty-v1`, input Head 3 adalah `[CLS] 768 + P(Head 1) 3 + P(Head 2) 4 = 775`; probabilitas conditioning di-`detach`. Temperature serta pasangan confidence-floor/entropy-ceiling hanya di-fit pada validation.

Jalankan baseline arsitektur pada snapshot dan seed yang sama:

```powershell
.\.venv\Scripts\python.exe -m app.training.v2.train_lora `
  --snapshot data\processed\sd-math-gold-v1.snapshot.json `
  --architecture parallel-v1 `
  --output-dir models\indobert-3x4x3-parallel-v1 `
  --work-dir runs\indobert-3x4x3-parallel-v1
```

Promosi conditioned model memerlukan peningkatan Head 3 yang konsisten tanpa regresi Head 1/2, kalibrasi, coverage, atau stabilitas antar-seed. Artefak lama tanpa field arsitektur/routing dibaca sebagai `parallel-v1` + `confidence-only-v1` agar tetap kompatibel; ia tidak diam-diam dianggap conditioned.

### Hasil smoke ablation silver kelas 1

Satu challenger `conditioned-difficulty-v1` sudah dilatih secara lokal pada snapshot silver 50 item (`36/7/7`), representasi `metadata`, rank 8, LR LoRA `1e-4`, dan seed 42. Hasil validation berikut hanya pemeriksaan teknis, bukan bukti penelitian:

| Arsitektur | Macro-F1 kognitif | Macro-F1 pengetahuan | Macro-F1 difficulty | Rata-rata tiga head |
|---|---:|---:|---:|---:|
| `parallel-v1` lama | 0,667 | 0,354 | 0,308 | 0,443 |
| `conditioned-difficulty-v1` challenger | 0,667 | 0,267 | 0,308 | 0,414 |

Conditioning **belum meningkatkan Head 3** dan Head 2 turun pada sampel kecil tersebut. Karena itu challenger tidak dipromosikan, `approvedForProvisional` tetap `false`, dan artefak aktif tetap legacy parallel. CLI mewajibkan `--architecture` secara eksplisit agar conditioned model tidak mengganti baseline diam-diam. Keputusan final menunggu gold label, class coverage memadai, ablation pada split yang sama, dan tiga seed.

Default trainer adalah representasi `solution` tanpa KKO eksplisit. Jalankan eksperimen terpisah dengan `--representation stem_options`, `metadata`, `solution`, dan `kko`. `kko` hanya boleh dipilih bila validation macro-F1 meningkat tanpa merusak challenge set berisi KKO sama tetapi tuntutan proses berbeda.

## 6. Frozen test

Test baru dibuka setelah rubric, split hash, dan promotion gate disetujui dosen:

```powershell
.\.venv\Scripts\python.exe scripts\evaluate_frozen_test_v2.py `
  --snapshot data\processed\sd-math-gold-v1.snapshot.json `
  --artifact models\indobert-3x4x3-v1 `
  --output reports\frozen-test-v1.json `
  --unlock-frozen-test
```

Perintah membuat marker `FROZEN_TEST_OPENED.json` dan menolak pembukaan kedua. Laporan tidak otomatis mengubah `approvedForProvisional`; persetujuan akademik tetap tindakan terpisah.

## 7. Hasil validasi per kelas SD

Hasil final kelas 1-6 tersedia di [indeks hasil validasi](../output/pretest/README.md). Lokasi yang berlaku adalah `output/pretest/kelasN/hasil_validasi/` untuk setiap kelas. Folder ini memuat laporan, `questions.json`, `indobert_predictions.json`, `validation_results.json`, kelompok `difficulty/`, dan `manifest.json`. Subfolder `bukti_validasi/` memuat checkpoint Gemini serta audit final yang dikunci. Arsip, salinan bundle, hasil anchored review lama, dan checkpoint sementara telah dihapus setelah berkas final diverifikasi.

Konsumen membaca `items[].llmAdvisory.advisoryLabels` dan `items[].finalRouting`. Gold ahli tetap null dan `pending_expert_review` membutuhkan ahli. Metode yang berlaku adalah blind N=3, verifikasi kunci/solusi, adjudikasi AI untuk ketidaksepakatan atau masalah konten, penguncian SHA-256, lalu diagnostik IndoBERT. Label difficulty dinilai relatif terhadap kelas sasaran dan tidak dipaksakan mengisi Hard. Gate `readyForExpansion` mengikuti audit; batch selesai tidak otomatis berarti gate lolos.

Checkpoint dan audit final mempertahankan byte serta hash asli. Path yang tertulis di dalam audit adalah lokasi historis pada saat penilaian; `manifest.json` menunjuk lokasi sumber yang berlaku setelah perapihan. Snapshot yang masih menjadi sumber model aktif berada di `models/indobert-3x4x3-v1/training_provenance/dataset_snapshot_silver.json`, terpisah dari hasil validasi final. Snapshot itu mempertahankan hash dataset dan split yang dicatat pada manifest model.

Untuk batch baru, gunakan workspace sementara terpisah. Contoh berikut menggunakan kelas 3 dan tidak menimpa hasil aktif:

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py --source output/pretest/kelas3/soal_pretest_db.json --grade 3 --output output/validation_work/kelas3/silver_labels.json --runs 3 --workers 1 --pause 3 --execute
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py --source output/pretest/kelas3/soal_pretest_db.json --grade 3 --checkpoint output/validation_work/kelas3/silver_labels.json --output-dir output/validation_work/kelas3/audit
.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py --source output/pretest/kelas3/soal_pretest_db.json --checkpoint output/validation_work/kelas3/silver_labels.json --audit output/validation_work/kelas3/audit/pilot_audit.json --artifact models/indobert-3x4x3-v1 --output-dir output/validation_work/kelas3/bundle
```

Nama generator historis; `--grade` dan `--source` menentukan kelas sebenarnya. `--execute` mengaktifkan live pada proses CLI dan tidak mengubah `.env`. Resume hanya dilakukan sebelum audit final dan mempertahankan run sukses. Setelah audit final, checkpoint terkunci; perubahan konfigurasi memerlukan batch baru. Ekspor bundle tidak otomatis menulis ke MongoDB, melatih ulang, atau mengirim soal ke siswa. `newLlmCalls=0` pada manifest hanya merujuk tahap packaging offline.

## Intervensi yang masih wajib

- URI/nama database Atlas dengan least privilege dan IP allowlist;
- service PaaS, stable egress bila ada, TLS, host/origin production;
- bucket S3-compatible private;
- identitas, bukti keahlian, COI dan consent tiga ahli + satu senior;
- source PDF/Excel/checksum yang tidak ada di Git;
- persetujuan dosen atas rubric, split hash, dan promotion gate;
- waktu CPU panjang serta unduhan awal base model.
