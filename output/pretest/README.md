# Hasil validasi kelas 1-12

Gunakan **`kelasN/hasil_validasi/`** sebagai laporan aktif untuk setiap kelas. Label masih silver/advisory dan membutuhkan pemeriksaan ahli. **Kelas 8–12 tertahan kuota harian Gemini: kelas 8 baru 8/126 run awal sukses, sedangkan kelas 9–12 belum memiliki penilaian AI berhasil.**

| Kelas | Soal | Easy | Medium | Hard | Belum diputuskan | Laporan |
|---|---:|---:|---:|---:|---:|---|
| [1](kelas1/hasil_validasi/README.md) | 50 | 48 | 2 | 0 | 0 | [Laporan](kelas1/hasil_validasi/LAPORAN_VALIDASI.md) |
| [2](kelas2/hasil_validasi/README.md) | 44 | 37 | 6 | 0 | 1 | [Laporan](kelas2/hasil_validasi/LAPORAN_VALIDASI.md) |
| [3](kelas3/hasil_validasi/README.md) | 42 | 33 | 9 | 0 | 0 | [Laporan](kelas3/hasil_validasi/LAPORAN_VALIDASI.md) |
| [4](kelas4/hasil_validasi/README.md) | 18 | 14 | 4 | 0 | 0 | [Laporan](kelas4/hasil_validasi/LAPORAN_VALIDASI.md) |
| [5](kelas5/hasil_validasi/README.md) | 72 | 47 | 23 | 2 | 0 | [Laporan](kelas5/hasil_validasi/LAPORAN_VALIDASI.md) |
| [6](kelas6/hasil_validasi/README.md) | 25 | 16 | 9 | 0 | 0 | [Laporan](kelas6/hasil_validasi/LAPORAN_VALIDASI.md) |
| [7](kelas7/hasil_validasi/README.md) | 49 | 28 | 20 | 1 | 0 | [Laporan](kelas7/hasil_validasi/LAPORAN_VALIDASI.md) |
| [8 (sementara)](kelas8/hasil_validasi/README.md) | 42 | 1 | 1 | 0 | 40 | [Laporan sementara](kelas8/hasil_validasi/LAPORAN_VALIDASI.md) |
| [9 (belum dinilai)](kelas9/hasil_validasi/README.md) | 42 | 0 | 0 | 0 | 42 | [Laporan status](kelas9/hasil_validasi/LAPORAN_VALIDASI.md) |
| [10 (belum dinilai)](kelas10/hasil_validasi/README.md) | 46 | 0 | 0 | 0 | 46 | [Laporan status](kelas10/hasil_validasi/LAPORAN_VALIDASI.md) |
| [11 (menunggu kuota)](kelas11/hasil_validasi/README.md) | 22 | 0 | 0 | 0 | 22 | [Laporan status](kelas11/hasil_validasi/LAPORAN_VALIDASI.md) |
| [12 (menunggu kuota)](kelas12/hasil_validasi/README.md) | 32 | 0 | 0 | 0 | 32 | [Laporan status](kelas12/hasil_validasi/LAPORAN_VALIDASI.md) |

```text
kelas1/ ... kelas12/
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

`images`, `bab*.json`, `soal_pretest_db.json`, dan `sesi_pretest.json` adalah sumber ekstraksi, bukan hasil validasi lama. Untuk kelas 1-6, checkpoint dan audit final ada di `hasil_validasi/bukti_validasi/`; arsip, hasil penilaian lama, checkpoint sementara, dan bundle duplikat telah dihapus. Snapshot training model aktif ada di `models/indobert-3x4x3-v1/training_provenance/`.

Kelas 7 memakai rubrik SMP dan blind N=3 dengan 147 run sukses serta 16 adjudikasi AI. Bukti batch dan audit terkunci disimpan di [revalidasi_blind_20261002_v1](kelas7/revalidasi_blind_20261002_v1/README.md). Semua soal masih `pending_expert_review`; gate ekspansi/training belum lolos karena satu run soal ke-37 menandai konflik kunci. IndoBERT lama hanya mendukung kelas 1-6, sehingga seluruh diagnostik kelas 7 `out_of_scope`/`abstain`. Label kelas 7 mengikuti Gemini blind, bukan prediksi IndoBERT.

Kelas 8 memakai rubrik SMP tersendiri. Dua soal memiliki tiga run lengkap; soal ketiga baru dua run sukses; 39 soal belum dinilai. Angka Easy/Medium/Hard di atas masih sementara dan tidak menggambarkan distribusi akhir kelas 8. Checkpoint kerja tetap resumable; snapshot bukti yang dikunci berada di [partial-v1](kelas8/revalidasi_blind_20261002_v1/README.md). Seluruh 42 soal diekspor; 40 yang belum memiliki keputusan tetap `undecided`/`llm_retry_or_manual_review`. IndoBERT juga abstain di luar cakupan kelas 8.

Kelas 9 telah disiapkan dengan rubrik SMP kelas 9. Panggilan AI pertama gagal karena kuota harian; seluruh 42 soal belum dinilai, sehingga nol Easy/Medium/Hard tidak menunjukkan distribusi difficulty. Checkpoint resume dan snapshot audit tersedia di [batch kelas 9](kelas9/revalidasi_blind_20261002_v1/README.md). Seluruh soal tetap `undecided`/`llm_retry_or_manual_review`; IndoBERT kelas 9 `out_of_scope`/`abstain`.

Kelas 10–12 memakai rubrik SMA per kelas dan [pelaksana batch serial](../../scripts/generate_silver_labels_sma.py). Panggilan pertama kelas 10 terkena kuota; kelas 11–12 ditandai menunggu blok yang sama tanpa panggilan API tambahan. Semua 100 soal belum dinilai dan tetap `undecided`, dengan target 300 run awal. Nol Easy/Medium/Hard bukan distribusi difficulty korpus. Lihat [status batch bersama](revalidasi_blind_20261002_v1_sma_execution.json) dan [runbook SMA](../../API_DOCUMENTATION/32_KELAS10_11_12_BLIND_VALIDATION.md) untuk resume. Semua diagnostik SMA `out_of_scope`/`abstain`; scope IndoBERT tetap SD 1–6.
