# Hasil validasi kelas 1-6

Gunakan **`kelasN/hasil_validasi/`** sebagai hasil final untuk setiap kelas. Label masih silver/advisory dan membutuhkan pemeriksaan ahli.

| Kelas | Soal | Easy | Medium | Hard | Belum diputuskan | Laporan |
|---|---:|---:|---:|---:|---:|---|
| [1](kelas1/hasil_validasi/README.md) | 50 | 48 | 2 | 0 | 0 | [Laporan](kelas1/hasil_validasi/LAPORAN_VALIDASI.md) |
| [2](kelas2/hasil_validasi/README.md) | 44 | 37 | 6 | 0 | 1 | [Laporan](kelas2/hasil_validasi/LAPORAN_VALIDASI.md) |
| [3](kelas3/hasil_validasi/README.md) | 42 | 33 | 9 | 0 | 0 | [Laporan](kelas3/hasil_validasi/LAPORAN_VALIDASI.md) |
| [4](kelas4/hasil_validasi/README.md) | 18 | 14 | 4 | 0 | 0 | [Laporan](kelas4/hasil_validasi/LAPORAN_VALIDASI.md) |
| [5](kelas5/hasil_validasi/README.md) | 72 | 47 | 23 | 2 | 0 | [Laporan](kelas5/hasil_validasi/LAPORAN_VALIDASI.md) |
| [6](kelas6/hasil_validasi/README.md) | 25 | 16 | 9 | 0 | 0 | [Laporan](kelas6/hasil_validasi/LAPORAN_VALIDASI.md) |

```text
kelas1/ ... kelas6/
  hasil_validasi/
    LAPORAN_VALIDASI.md
    validation_results.json
    questions.json
    indobert_predictions.json
    difficulty_groups.json
    difficulty/
    bukti_validasi/
    manifest.json
    README.md
  images/
  bab*.json
  soal_pretest_db.json
  sesi_pretest.json
  CATATAN.md
  _status.json
```

`images`, `bab*.json`, `soal_pretest_db.json`, dan `sesi_pretest.json` adalah sumber ekstraksi, bukan hasil validasi lama. Checkpoint dan audit final ada di `hasil_validasi/bukti_validasi/`. Arsip, hasil penilaian lama, checkpoint sementara, dan bundle duplikat telah dihapus. Snapshot training model aktif ada di `models/indobert-3x4x3-v1/training_provenance/`.
