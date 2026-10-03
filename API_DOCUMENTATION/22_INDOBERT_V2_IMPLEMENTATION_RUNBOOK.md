# Runbook silver dan IndoBERT v2

Snapshot training dan delivery berasal dari label silver yang telah lolos qualification AI. Tidak ada tahap assignment, diskusi pelabel atau freeze gold.

```powershell
.\.venv\Scripts\python.exe scripts/build_operational_silver.py --snapshot-id silver-batch-v3 --output output/pretest/silver_operational/dataset_snapshot_v3.json
```

Gunakan output baru pada setiap freeze. `scripts/freeze_dataset_v2.py` meneruskan ke builder yang sama. Tambahkan `--class-name kelas11_tl` untuk memilih sumber atau `--assessment-db data/local/assessments.sqlite3` untuk mengecualikan versi yang held dan mendaftarkan snapshot ke API.

Builder memeriksa sumber, aset, coverage ID, checkpoint, prompt/response hashes, tiga run sukses, adjudikasi, label, kunci dan solusi. Versi operasional memakai namespace kelas/track dan digest konten. Snapshot memakai `TrainingRow`, provenance `ai_silver`, split group-aware 70/15/15 dan expansion hash.

Training model saat ini menggunakan `rows` SD 1-6. Kelas 7-12/TL berada di `expansionRows`, dapat dipakai delivery pada grade/track yang sesuai tetapi tidak memperluas scope IndoBERT lama. Label evaluasi model tetap silver dan harus disebut demikian pada metrik.

Minimum dukungan kelas label, kebocoran kelompok, anti-collapse, macro-F1, kalibrasi confidence/entropy dan gate frozen-test tetap berlaku. Distribusi Hard yang sangat kecil dapat mengunci evaluasi; penghapusan pelabel manusia tidak menghapus gate teknis ini. Tidak ada training ulang atau promosi model otomatis dalam migrasi.
