# Validasi AI silver semua kelas

Laporan aktif mencakup **580 soal** reguler kelas 1-12 dan TL kelas 11-12: **1,740/1,740 run awal sukses**, **0 adjudikasi tertunda**. Label operasional memakai `ai_silver` tanpa persetujuan pelabel manusia.

**562 soal silver_ready**, **15 soal revision_required**, **3 soal needs_ai_review**. Soal yang memerlukan revisi atau penilaian ulang ditahan dari snapshot delivery.

Label kesulitan seluruh soal: **428 Easy, 142 Medium, 7 Hard, 3 undecided**.

| Kelas | Soal | Run sukses | Easy | Medium | Hard | Silver siap | Revisi | AI review |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [kelas1](kelas1/hasil_validasi/README.md) | 50 | 150 | 46 | 4 | 0 | 49 | 1 | 0 |
| [kelas2](kelas2/hasil_validasi/README.md) | 44 | 132 | 38 | 5 | 1 | 43 | 1 | 0 |
| [kelas3](kelas3/hasil_validasi/README.md) | 42 | 126 | 33 | 9 | 0 | 40 | 2 | 0 |
| [kelas4](kelas4/hasil_validasi/README.md) | 18 | 54 | 15 | 3 | 0 | 18 | 0 | 0 |
| [kelas5](kelas5/hasil_validasi/README.md) | 72 | 216 | 47 | 21 | 2 | 67 | 4 | 1 |
| [kelas6](kelas6/hasil_validasi/README.md) | 25 | 75 | 16 | 9 | 0 | 25 | 0 | 0 |
| [kelas7](kelas7/hasil_validasi/README.md) | 49 | 147 | 32 | 16 | 1 | 48 | 1 | 0 |
| [kelas8](kelas8/hasil_validasi/README.md) | 42 | 126 | 26 | 16 | 0 | 41 | 1 | 0 |
| [kelas9](kelas9/hasil_validasi/README.md) | 42 | 126 | 30 | 12 | 0 | 39 | 3 | 0 |
| [kelas10](kelas10/hasil_validasi/README.md) | 46 | 138 | 33 | 13 | 0 | 46 | 0 | 0 |
| [kelas11](kelas11/hasil_validasi/README.md) | 22 | 66 | 18 | 4 | 0 | 20 | 0 | 2 |
| [kelas11_tl](kelas11_tl/hasil_validasi/README.md) | 55 | 165 | 46 | 8 | 1 | 55 | 0 | 0 |
| [kelas12](kelas12/hasil_validasi/README.md) | 32 | 96 | 18 | 11 | 2 | 31 | 1 | 0 |
| [kelas12_tl](kelas12_tl/hasil_validasi/README.md) | 41 | 123 | 30 | 11 | 0 | 40 | 1 | 0 |

[Snapshot silver](silver_operational/dataset_snapshot_v2.json) `operational-silver-20261003-v2` memuat **571 versi qualified**. Jika laporan berubah, bangun dan daftarkan snapshot baru melalui `scripts/build_operational_silver.py`; snapshot yang sudah terdaftar tetap immutable. Gate training/test dan dukungan tiap label tetap berlaku.

[Bukti migrasi](silver_operational_migration.json), [bukti verifikasi integritas](silver_operational/verification.json), dan [panduan integrasi](../../API_DOCUMENTATION/36_SILVER_OPERATIONAL_INTEGRATION.md).

Checkpoint dan laporan historis tetap immutable. Arsip lokal pra-migrasi berada di `archive/pre_silver_operational_v1`. Buku Guru tetap sumber bukti kunci. IRT memakai respons siswa nyata dan menyimpan difficulty empiris terpisah dari `intendedDifficulty`.

Laporan aktif `hasil_validasi/validation_results.json` berupa array dokumen soal dengan field yang sama seperti `soal_pretest_db.json`. `cognitive_level` memakai difficulty final `easy`, `medium`, `hard`; domain knowing/applying/reasoning tetap di metadata audit. `cognitive_score` memakai Easy=600, Medium=1000, Hard=1400. `confidence_score` adalah persentase dukungan run awal terhadap label final terendah dari tiga head (0-100), bukan probabilitas akurasi. Status database hanya `active` atau `inactive`; filter delivery memakai `status = active`. Routing validasi asli tetap ada di metadata audit. Bukti lengkap tersimpan di `hasil_validasi/bukti_validasi/decision_audit.json`; profil tiga head, identitas snapshot dan rumus ekspor ada di `manifest.json.databaseExport`. [Verifikasi ekspor database](silver_operational/database_format_verification.json) mencatat preservasi sumber, audit dan identitas snapshot.
