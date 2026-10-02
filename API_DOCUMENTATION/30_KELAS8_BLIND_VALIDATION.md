# Validasi blind kelas 8 SMP

Batch kelas 8 menggunakan 42 soal dari `output/pretest/kelas8/soal_pretest_db.json`, 8 referensi gambar, blind N=3, verifikasi kunci/solusi/visual, dan adjudikasi AI bila diperlukan. Sumber ekstraksi tetap utuh. Label masih silver/advisory; gold manusia tetap null.

## Rubrik dan cakupan

- Prompt: `gemini-silver-math-3x4x3-v6-blind-smp8-key-verified`.
- Adjudikasi: `gemini-silver-math-3x4x3-v6-adjudication-smp8`.
- Rubrik: `math-rubric-3x4x3-v4-smp8-grade-aware` di `configs/rubric_math_3x4x3_v4_smp8.yaml`.

Konteks kesempatan belajar mengikuti subtopik korpus: pangkat/akar/bentuk baku, operasi rasional, Pythagoras/tripel/segitiga istimewa/penerapan/jarak, kesebangunan, persamaan dan pertidaksamaan linier satu variabel, pemodelan aljabar, relasi/fungsi/korespondensi, persamaan garis/kemiringan, serta pemusatan dan penyebaran data. Ini rubrik penelitian untuk review ahli, bukan klaim penguasaan semua siswa. Materi pengayaan, bilangan besar, atau faktorial tidak otomatis Hard; nilai solusi minimum yang benar-benar diperlukan.

Periksa orientasi visual, satuan, hipotenusa, pembulatan jumlah pengangkutan, domain/kodomain, dan konvensi kuartil. Karakter ekstraksi yang rusak, konflik kunci, atau ambigu adalah masalah konten. Prompt meminta solusi maksimal 700 karakter sesuai schema; batas validator tidak dilonggarkan. Penilaian tidak dipaksa mengisi atau menyeimbangkan setiap kategori difficulty.

Prompt/hash rubrik kelas 1-7 tetap sama. Generator dan audit kemudian mendukung grade 1-12; kelas 9 memakai versi tersendiri pada [runbook 31](31_KELAS9_BLIND_VALIDATION.md), sedangkan SMA 10-12 pada [32](32_KELAS10_11_12_BLIND_VALIDATION.md). Resume menolak perubahan grade, sumber, model, versi prompt, atau hash rubrik.

Model IndoBERT lama hanya mendukung SD kelas 1-6. Untuk kelas 8, runtime mengembalikan `out_of_scope` dan tiga head `abstain`; label/confidence/entropy null, probabilitas kosong. Encoder tidak dijalankan untuk kelas di luar cakupan. Input terserialisasi hanya dicatat untuk audit. Agreement dengan Gemini tidak tersedia; nol disagreement tidak menyatakan model setuju. Batch tidak memperluas cakupan model atau melakukan training ulang.

## Prosedur

Ketiga run awal menerima soal, opsi, kunci sumber, gambar, dan rubrik kelas 8. Tidak ada prediksi IndoBERT, vote run lain, estimasi agen, konsensus, atau distribusi target dalam prompt blind. Run 3-0 dapat diterima sebagai silver; ketidaksepakatan, abstain, atau masalah konten/kunci masuk adjudikasi AI terpisah. Adjudikasi tetap berasal dari Gemini yang sama, bukan ahli manusia.

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas8/soal_pretest_db.json --grade 8 `
  --output output/pretest/kelas8/revalidasi_blind_20261002_v1/silver_labels.json `
  --runs 3 --workers 1 --pause 3 --attempts 3 --execute
```

Run sukses tersimpan dan tidak dipanggil ulang saat resume. Nama generator historis; source/grade menetapkan kelas aktual. `.env` tidak perlu diubah.

Setelah run dan adjudikasi selesai, audit mengunci checkpoint sebelum pemeriksaan scope IndoBERT:

```powershell
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py `
  --source output/pretest/kelas8/soal_pretest_db.json --grade 8 `
  --checkpoint output/pretest/kelas8/revalidasi_blind_20261002_v1/silver_labels.json `
  --output-dir output/pretest/kelas8/revalidasi_blind_20261002_v1/audit-v1

.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py `
  --source output/pretest/kelas8/soal_pretest_db.json `
  --checkpoint output/pretest/kelas8/revalidasi_blind_20261002_v1/silver_labels.json `
  --audit output/pretest/kelas8/revalidasi_blind_20261002_v1/audit-v1/pilot_audit.json `
  --artifact models/indobert-3x4x3-v1 `
  --output-dir output/pretest/kelas8/revalidasi_blind_20261002_v1/bundle
```

Laporan aktif dibuat melalui perintah packaging yang sama dengan `--output-dir output/pretest/kelas8/hasil_validasi`. Packaging offline tidak memanggil LLM. Audit yang gagal gate tetap boleh dilaporkan, tetapi tidak menyetujui ekspansi/training. Konflik pada run awal tidak dihapus walaupun adjudikasi menerima kunci. Jangan resume/mengubah checkpoint setelah audit final; gunakan direktori versi baru untuk pekerjaan berikutnya. Output menolak overwrite direktori bundle berisi.

## Keluaran

Data keputusan memakai `ai-decision-bundle-v2-blind`; soal memakai `question-validation-input-v2-blind` dan topik `Matematika SMP Kelas 8`. Konsumen membaca `items[].llmAdvisory.advisoryLabels` bersama `finalRouting` dan `humanValidation`.

`difficulty_groups.json` dan subset `difficulty/Easy.json`, `Medium.json`, `Hard.json`, serta `undecided.json` memuat semua kategori, termasuk kategori kosong. `contentQualified` hanya menandai soal tanpa blocker konten AI; ahli tetap harus memeriksa. Soal bermasalah tetap diekspor dengan routing revisi/review yang sesuai.

`LAPORAN_VALIDASI.md` menyajikan soal, kunci, solusi minimum, bukti label, profil difficulty, tiga run, adjudikasi, dan abstention IndoBERT. `manifest.json` mengikat hash sumber, checkpoint, audit, serta keluaran. Semua label tetap advisory. Tidak ada gold ahli, publikasi soal, respons siswa, perhitungan CTT/IRT, atau training dalam batch ini.

## Status eksekusi 2 Oktober 2026

Provider menghentikan batch pada run 3 soal ke-3 dengan `ClientError:429`, quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Status checkpoint kerja `blocked_provider_daily_quota`. Terdapat 8 run sukses dari target 126; dua soal lengkap, satu soal baru dua run, dan 39 soal belum dinilai. Belum ada adjudikasi sukses. Token sukses tercatat 18.381.

Distribusi sementara: Easy 1, Medium 1, Hard 0, undecided 40. Ini bukan distribusi final kelas 8. Seluruh 42 soal tetap diekspor; dua item `pending_expert_review`, 40 `llm_retry_or_manual_review`; gold null. Audit tidak menyetujui ekspansi/training karena batch belum lengkap dan kategori Hard belum terisi pada sampel sementara.

Snapshot checkpoint disalin ke `revalidasi_blind_20261002_v1/partial-v1/silver_labels.json` sebelum audit. Audit dan bundle sementara memakai salinan terkunci tersebut; checkpoint kerja di direktori batch tetap dapat di-resume saat kuota tersedia. Resume memakai perintah generator di atas dan mempertahankan delapan run sukses. Setelah batch lengkap, buat audit/bundle versi baru tanpa menimpa snapshot parsial; laporan aktif sementara diarsipkan sebelum pembaruan.

Lihat [laporan sementara](../output/pretest/kelas8/hasil_validasi/LAPORAN_VALIDASI.md), [checkpoint dan petunjuk resume](../output/pretest/kelas8/revalidasi_blind_20261002_v1/README.md), dan [audit parsial terkunci](../output/pretest/kelas8/revalidasi_blind_20261002_v1/partial-v1/audit-v1/pilot_audit.json). Seluruh 42 diagnostik IndoBERT `out_of_scope`/`abstain`; tidak ada probabilitas kelas 8 yang dibuat.
