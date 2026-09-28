# Runbook Implementasi IndoBERT v2 3×4×3

## Status nyata

Kode vertical slice telah tersedia, tetapi hasil riset belum boleh diklaim. Atlas/PaaS/S3 belum diprovision, empat ahli belum dibuat, qualification dan anotasi belum berlangsung, snapshot gold belum ada, dan model final belum dilatih. Karena itu `/v2/classify` menjawab 503 sampai artefak lengkap dan checksum-valid tersedia.

`/v1/classify` tetap legacy C1–C6. Tidak ada Claude runtime, delivery siswa, CTT, atau IRT dalam fase ini.

## Komponen kode

| Komponen | Lokasi | Status |
|---|---|---|
| Kontrak 3×4×3 dan serializer | `app/classification/v2` | implemented |
| Import immutable `babNN.json` | `app/ingestion/pretest_import.py` | implemented |
| Auth, UI blind, CSRF, IDOR guard | `app/annotation` | implemented, belum diprovision |
| Atlas collections/index/transaction | `app/annotation/repository.py` | implemented, belum diprovision |
| Consensus dan agreement | `app/annotation/consensus.py` | implemented |
| Snapshot dan group split | `app/training/v2/dataset.py` | implemented |
| Baseline dan LoRA CPU | `app/training/v2` | implemented, belum dijalankan pada gold |
| Kalibrasi dan artefak checksum | `app/classification/v2` | implemented |
| API advisory | `/v2/*` | implemented, 503 tanpa artefak |

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
  --resume
```

Trainer menjalankan grid `rank {8,16} × LR {1e-4,2e-4}` dengan seed 42, lalu konfigurasi terbaik pada seed 13, 42, dan 73. Artefak utama memakai seed 42 dan mencatat stabilitas tiga seed. Calibration dan routing threshold hanya memakai validation.

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

## Intervensi yang masih wajib

- URI/nama database Atlas dengan least privilege dan IP allowlist;
- service PaaS, stable egress bila ada, TLS, host/origin production;
- bucket S3-compatible private;
- identitas, bukti keahlian, COI dan consent tiga ahli + satu senior;
- source PDF/Excel/checksum yang tidak ada di Git;
- persetujuan dosen atas rubric, split hash, dan promotion gate;
- waktu CPU panjang serta unduhan awal base model.
