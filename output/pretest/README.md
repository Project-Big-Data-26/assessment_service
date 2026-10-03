# Validasi AI silver semua kelas

Laporan aktif mencakup **580 soal** reguler kelas 1-12 dan TL kelas 11-12: **1,740/1,740 run awal sukses**, **0 adjudikasi tertunda**. Label operasional memakai `ai_silver` tanpa persetujuan pelabel manusia.

**571 soal silver_ready**, **9 soal revision_required**, **0 soal needs_ai_review**. Soal yang memerlukan revisi atau penilaian ulang ditahan dari snapshot delivery.

Label kesulitan seluruh soal: **414 Easy, 161 Medium, 5 Hard, 0 undecided**.

| Kelas | Soal | Run sukses | Easy | Medium | Hard | Silver siap | Revisi | AI review |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [kelas1](kelas1/hasil_validasi/README.md) | 50 | 150 | 48 | 2 | 0 | 50 | 0 | 0 |
| [kelas2](kelas2/hasil_validasi/README.md) | 44 | 132 | 38 | 6 | 0 | 43 | 1 | 0 |
| [kelas3](kelas3/hasil_validasi/README.md) | 42 | 126 | 33 | 9 | 0 | 41 | 1 | 0 |
| [kelas4](kelas4/hasil_validasi/README.md) | 18 | 54 | 14 | 4 | 0 | 18 | 0 | 0 |
| [kelas5](kelas5/hasil_validasi/README.md) | 72 | 216 | 48 | 22 | 2 | 70 | 2 | 0 |
| [kelas6](kelas6/hasil_validasi/README.md) | 25 | 75 | 16 | 9 | 0 | 25 | 0 | 0 |
| [kelas7](kelas7/hasil_validasi/README.md) | 49 | 147 | 28 | 20 | 1 | 49 | 0 | 0 |
| [kelas8](kelas8/hasil_validasi/README.md) | 42 | 126 | 24 | 17 | 1 | 42 | 0 | 0 |
| [kelas9](kelas9/hasil_validasi/README.md) | 42 | 126 | 28 | 14 | 0 | 41 | 1 | 0 |
| [kelas10](kelas10/hasil_validasi/README.md) | 46 | 138 | 29 | 17 | 0 | 46 | 0 | 0 |
| [kelas11](kelas11/hasil_validasi/README.md) | 22 | 66 | 15 | 6 | 1 | 21 | 1 | 0 |
| [kelas11_tl](kelas11_tl/hasil_validasi/README.md) | 55 | 165 | 44 | 11 | 0 | 54 | 1 | 0 |
| [kelas12](kelas12/hasil_validasi/README.md) | 32 | 96 | 19 | 13 | 0 | 31 | 1 | 0 |
| [kelas12_tl](kelas12_tl/hasil_validasi/README.md) | 41 | 123 | 30 | 11 | 0 | 40 | 1 | 0 |

[Snapshot silver](silver_operational/dataset_snapshot_v2.json) `operational-silver-20261003-v2` memuat **571 versi qualified**. Jika laporan berubah, bangun dan daftarkan snapshot baru melalui `scripts/build_operational_silver.py`; snapshot yang sudah terdaftar tetap immutable. Gate training/test dan dukungan tiap label tetap berlaku.

[Bukti migrasi](silver_operational_migration.json), [bukti verifikasi integritas](silver_operational/verification.json), dan [panduan integrasi](../../API_DOCUMENTATION/36_SILVER_OPERATIONAL_INTEGRATION.md).

Checkpoint dan laporan historis tetap immutable. Arsip lokal pra-migrasi berada di `archive/pre_silver_operational_v1`. Buku Guru tetap sumber bukti kunci. IRT memakai respons siswa nyata dan menyimpan difficulty empiris terpisah dari `intendedDifficulty`.

Laporan aktif `hasil_validasi/validation_results.json` memakai format soal ringkas: `items[].cognitive_level` dan delapan field `items[].ai_metadata`. Bukti lengkap tersimpan di `hasil_validasi/bukti_validasi/decision_audit.json`. Filter delivery memakai `ai_metadata.validation_status = silver_ready`. [Verifikasi format ringkas](silver_operational/compact_format_verification.json) mencatat preservasi sumber, audit dan identitas snapshot.
