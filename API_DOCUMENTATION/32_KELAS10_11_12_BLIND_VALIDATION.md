# Validasi blind kelas 10, 11, dan 12 SMA

Ketiga kelas memakai blind N=3, verifikasi kunci/solusi/visual, dan adjudikasi AI terpisah bila diperlukan. Sumber soal dan gambar tetap utuh. Label tetap silver/advisory; gold ahli null. Rubrik penelitian berdasarkan materi korpus memerlukan pemeriksaan ahli.

| Kelas | Soal | Referensi gambar | Target run awal | Materi korpus |
|---|---:|---:|---:|---|
| 10 | 46 | 10 | 138 | Eksponen/akar, barisan/deret/bunga, trigonometri, SPLTV/pertidaksamaan/kuadrat, statistik dan peluang |
| 11 | 22 | 5 | 66 | Fungsi/komposisi/invers, lingkaran, diagram pencar, regresi/korelasi dan pencilan |
| 12 | 32 | 1 | 96 | Barisan/deret, bunga/investasi/pinjaman/anuitas, pencacahan dan peluang majemuk |
| Total | 100 | 16 | 300 | |

## Versi dan cakupan

Tiap kelas memiliki prompt `gemini-silver-math-3x4x3-v8-blind-smaN-key-verified`, adjudikasi `gemini-silver-math-3x4x3-v8-adjudication-smaN`, serta rubrik `math-rubric-3x4x3-v6-smaN-grade-aware`, dengan N = 10, 11, atau 12. File rubrik masing-masing berada di `configs/rubric_math_3x4x3_v6_smaN.yaml`. Hash dan konteks berbeda per kelas; resume menolak pertukaran grade/rubrik/model/sumber.

Konteks menilai tuntutan solusi minimum relatif kelas sasaran, tanpa menganggap semua siswa menguasai materi lanjutan. SMA, angka besar, notasi rumus, faktorial, atau anuitas tidak otomatis Hard. Kategori difficulty tidak dipaksakan lengkap/seimbang. Periksa domain, urutan komposisi, orientasi gambar, satuan, konvensi statistik, independensi/irisan peluang, periode bunga, model angsuran, dan waktu setoran. Ambiguitas/konflik kunci adalah masalah konten, bukan alasan menaikkan difficulty.

Prompt/hash rubrik kelas 1-9 serta checkpoint kelas 7-9 dipertahankan. Penilaian silver kini mendukung kelas 1-12: SD 1-6, SMP 7-9, SMA 10-12. Model IndoBERT lama tetap hanya mendukung SD 1-6. Untuk SMA, seluruh head `abstain` dengan scope `out_of_scope`; label/confidence/entropy null, probabilitas kosong, encoder tidak dijalankan. Input terserialisasi dicatat untuk audit, bukan prediksi SMA. Tidak ada agreement yang dapat diukur dengan Gemini ketika model abstain.

## Pelaksana batch bersama dan resume

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_sma.py `
  --grades 10 11 12 --batch-name revalidasi_blind_20261002_v1 --execute
```

Pelaksana menyiapkan checkpoint tiap kelas dan menjalankan generator serial. Jika suatu kelas terkena blok kuota/config provider, kelas berikutnya ditandai menunggu dengan `blockedByGrade`; tidak ada panggilan API berulang ke kelas berikutnya selama blok tersebut. Kelas yang sudah lengkap dilewati tanpa mengubah checkpoint yang selesai. Run sukses dipertahankan oleh generator saat resume. Ringkasan bersama berada di `output/pretest/revalidasi_blind_20261002_v1_sma_execution.json`.

Tiga run awal tidak menerima prediksi IndoBERT, vote run lain, estimasi agen, konsensus, atau distribusi target. Kesepakatan 3-0 dapat diterima sebagai silver; perbedaan/abstain/masalah konten masuk adjudikasi Gemini yang sama, bukan ahli manusia. Schema dan batas solusi 700 karakter tidak dilonggarkan. `.env` tidak diubah; batas token berlaku pada proses.

Setelah kuota tersedia, jalankan perintah bersama tersebut untuk melanjutkan checkpoint kerja. Jangan menjalankan ulang selama kondisi provider belum berubah. Untuk kelas tertentu, generator historis juga dapat dipakai dengan `--source output/pretest/kelasN/soal_pretest_db.json --grade N --output output/pretest/kelasN/revalidasi_blind_20261002_v1/silver_labels.json --runs 3 --workers 1 --pause 3 --attempts 3 --execute`.

## Audit dan packaging

Setelah semua run/adjudikasi selesai, audit mengunci checkpoint sebelum pemeriksaan scope IndoBERT. Contoh untuk kelas 10; ganti kelas untuk 11/12:

```powershell
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py `
  --source output/pretest/kelas10/soal_pretest_db.json --grade 10 `
  --checkpoint output/pretest/kelas10/revalidasi_blind_20261002_v1/silver_labels.json `
  --output-dir output/pretest/kelas10/revalidasi_blind_20261002_v1/audit-final-v1

.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py `
  --source output/pretest/kelas10/soal_pretest_db.json `
  --checkpoint output/pretest/kelas10/revalidasi_blind_20261002_v1/silver_labels.json `
  --audit output/pretest/kelas10/revalidasi_blind_20261002_v1/audit-final-v1/pilot_audit.json `
  --artifact models/indobert-3x4x3-v1 `
  --output-dir output/pretest/kelas10/revalidasi_blind_20261002_v1/bundle-final-v1
```

Audit/bundle memakai direktori versi baru; tidak menimpa snapshot parsial. Setelah audit final, jangan resume/mengubah checkpoint terkunci. Laporan aktif sementara diarsipkan sebelum pembaruan. Audit gagal gate boleh dilaporkan tetapi tidak menyetujui ekspansi/training. Packaging tidak memanggil LLM.

## Status eksekusi 2 Oktober 2026

Panggilan pertama kelas 10 mengembalikan `ClientError:429`, quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Kelas 10 berstatus `blocked_provider_daily_quota`. Kelas 11 dan 12 berstatus `waiting_provider_daily_quota`, `blockedByGrade=10`, tanpa panggilan API untuk kedua kelas tersebut.

Seluruh kelas memiliki **0 run dan 0 adjudikasi sukses**. Semua 100 soal belum dinilai; tidak ada distribusi Easy/Medium/Hard yang dapat disimpulkan. Angka nol pada berkas kategori berarti belum dinilai, bukan tidak ada soal dalam kategori tersebut. Semua item `undecided`/`llm_retry_or_manual_review`, label advisory/gold null. Audit `readyForExpansion=false` karena batch belum lengkap.

Checkpoint kerja dapat di-resume. Snapshot terpisah di `kelasN/revalidasi_blind_20261002_v1/partial-v1/silver_labels.json` dikunci untuk audit dan laporan status; snapshot ini tidak boleh di-resume. Hasil offline tetap mengekspor semua soal dan menautkan 16 referensi gambar. Tidak ada training, perluasan scope IndoBERT, publikasi soal, respons siswa, CTT, atau IRT.

| Kelas | Laporan status | Checkpoint dan bukti |
|---|---|---|
| 10 | [Laporan](../output/pretest/kelas10/hasil_validasi/LAPORAN_VALIDASI.md) | [README batch](../output/pretest/kelas10/revalidasi_blind_20261002_v1/README.md) |
| 11 | [Laporan](../output/pretest/kelas11/hasil_validasi/LAPORAN_VALIDASI.md) | [README batch](../output/pretest/kelas11/revalidasi_blind_20261002_v1/README.md) |
| 12 | [Laporan](../output/pretest/kelas12/hasil_validasi/LAPORAN_VALIDASI.md) | [README batch](../output/pretest/kelas12/revalidasi_blind_20261002_v1/README.md) |
