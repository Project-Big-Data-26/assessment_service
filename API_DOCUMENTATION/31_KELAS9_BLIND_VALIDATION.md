# Validasi blind kelas 9 SMP

Korpus kelas 9 berisi 42 soal dari `output/pretest/kelas9/soal_pretest_db.json` dengan 3 referensi gambar. Mekanisme tetap blind N=3, verifikasi kunci/solusi/visual, dan adjudikasi AI terpisah bila diperlukan. Label tetap silver/advisory; gold manusia null. Sumber ekstraksi tidak diubah.

## Rubrik dan cakupan

- Prompt: `gemini-silver-math-3x4x3-v7-blind-smp9-key-verified`.
- Adjudikasi: `gemini-silver-math-3x4x3-v7-adjudication-smp9`.
- Rubrik: `math-rubric-3x4x3-v5-smp9-grade-aware` di `configs/rubric_math_3x4x3_v5_smp9.yaml`.

Konteks mengikuti materi korpus: PLDV/SPLDV, pemodelan, kapasitas angkut, kemiringan, jaring-jaring dan bangun ruang, lingkaran, luas/volume/satuan, keliling dan luas, lokasi serta transformasi, kongruensi/kesebangunan, peluang empiris/teoretis, frekuensi harapan, pemilihan sampel, dan kuartil. Rubrik penelitian ini perlu review ahli; jangan menganggap semua siswa menguasai semua materi. Penilaian mengikuti solusi minimum yang diperlukan, bukan panjang teks, angka besar, atau kata kerja saja.

Periksa skala luas k² dan volume k³, diameter/jari-jari/garis pelukis, permukaan yang ditutup, liter/satuan kubik, pusat/arah rotasi dan korespondensi titik, ruang sampel dan asumsi peluang, bias sampel, serta data/konvensi kuartil. Ambiguitas, data yang hilang, konflik kunci, dan gambar kurang adalah persoalan konten. Solusi maksimal 700 karakter sesuai schema; validator tidak dilonggarkan. Distribusi Easy/Medium/Hard tidak dipaksakan seimbang atau lengkap.

Generator dan audit kemudian mendukung grade 1-12; SMA 10-12 memakai rubrik tersendiri pada [runbook 32](32_KELAS10_11_12_BLIND_VALIDATION.md). Prompt/hash rubrik kelas 1-8 dan checkpoint kelas 7-8 dipertahankan. Resume menolak perubahan sumber, grade, model, versi prompt, atau hash rubrik.

IndoBERT lama hanya mendukung SD kelas 1-6. Kelas 9 mengembalikan `out_of_scope` dan seluruh head `abstain`, dengan label/confidence/entropy null serta probabilitas kosong. Encoder tidak dijalankan; input terserialisasi hanya dicatat untuk audit. Tidak ada agreement dengan Gemini yang dapat diukur dari abstention. Batch ini tidak memperluas cakupan model, melatih ulang, memublikasikan soal, atau menghitung CTT/IRT.

## Menjalankan dan melanjutkan batch

Run awal menerima soal, opsi, kunci sumber, gambar, dan rubrik kelas 9. Prediksi IndoBERT, vote run lain, estimasi agen, konsensus, dan distribusi target tidak diberikan. Kesepakatan 3-0 dapat diterima sebagai silver; ketidaksepakatan, abstain, atau masalah konten/kunci masuk adjudikasi dari Gemini yang sama, bukan ahli manusia.

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas9/soal_pretest_db.json --grade 9 `
  --output output/pretest/kelas9/revalidasi_blind_20261002_v1/silver_labels.json `
  --runs 3 --workers 1 --pause 3 --attempts 3 --execute
```

Target 126 run awal. Perintah yang sama me-resume checkpoint kerja dan mempertahankan run sukses. `.env` tidak perlu diubah untuk batas token proses. Daily quota menghentikan batch langsung; jangan mengulang panggilan selama kondisi kuota belum berubah.

Setelah semua run dan adjudikasi lengkap, buat audit final dan bundle dalam direktori versi baru:

```powershell
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py `
  --source output/pretest/kelas9/soal_pretest_db.json --grade 9 `
  --checkpoint output/pretest/kelas9/revalidasi_blind_20261002_v1/silver_labels.json `
  --output-dir output/pretest/kelas9/revalidasi_blind_20261002_v1/audit-final-v1

.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py `
  --source output/pretest/kelas9/soal_pretest_db.json `
  --checkpoint output/pretest/kelas9/revalidasi_blind_20261002_v1/silver_labels.json `
  --audit output/pretest/kelas9/revalidasi_blind_20261002_v1/audit-final-v1/pilot_audit.json `
  --artifact models/indobert-3x4x3-v1 `
  --output-dir output/pretest/kelas9/revalidasi_blind_20261002_v1/bundle-final-v1
```

Audit mengunci checkpoint sebelum pemeriksaan scope model. Packaging offline tidak memanggil LLM. Setelah audit final, jangan resume atau mengubah checkpoint tersebut. Kegagalan gate boleh dilaporkan tetapi tidak menyetujui ekspansi/training. Direktori bundle berisi tidak boleh ditimpa; laporan aktif sementara diarsipkan sebelum pembaruan final.

## Status eksekusi 2 Oktober 2026

Panggilan pertama berhenti dengan `ClientError:429`, quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Status `blocked_provider_daily_quota`; **0/126 run sukses, 0 adjudikasi sukses, 42 soal belum dinilai AI**. Tidak ada distribusi difficulty yang dapat disimpulkan: Easy/Medium/Hard masing-masing 0, undecided 42. Angka nol tidak berarti tidak ada soal Medium atau Hard.

Checkpoint kerja tetap resumable di direktori batch. Salinannya dikunci di `partial-v1/silver_labels.json` untuk audit dan laporan status. `readyForExpansion=false` karena batch belum dinilai. Audit hanya membuktikan sumber/input, blind prompt, dan identitas rubrik cocok; bukan kelulusan validasi soal.

[Laporan status aktif](../output/pretest/kelas9/hasil_validasi/LAPORAN_VALIDASI.md) mengekspor seluruh 42 soal, semuanya `llm_retry_or_manual_review`, tanpa label advisory atau gold. Tiga gambar tetap ditautkan. Seluruh keluaran IndoBERT `out_of_scope`/`abstain`. Bukti dan perintah resume tersedia di [README batch](../output/pretest/kelas9/revalidasi_blind_20261002_v1/README.md) dan [audit terkunci](../output/pretest/kelas9/revalidasi_blind_20261002_v1/partial-v1/audit-v1/pilot_audit.json).
