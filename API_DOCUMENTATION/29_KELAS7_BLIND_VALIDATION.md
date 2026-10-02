# Validasi blind kelas 7 SMP

Batch kelas 7 memakai 49 soal di `output/pretest/kelas7/soal_pretest_db.json` dengan konteks SMP, blind N=3, verifikasi kunci/solusi/gambar, dan adjudikasi AI bila diperlukan. Sumber tetap utuh. Seluruh label adalah silver/advisory; gold manusia tetap null.

## Rubrik dan cakupan

Kelas 1–6 tetap memakai prompt v4 dan rubrik `math-rubric-3x4x3-v2-grade-aware` dengan hash file SD yang sama. Kelas 7 memakai:

- Prompt `gemini-silver-math-3x4x3-v5-blind-smp7-key-verified`.
- Adjudikasi `gemini-silver-math-3x4x3-v5-adjudication-smp7`.
- Rubrik `math-rubric-3x4x3-v3-smp7-grade-aware` di `configs/rubric_math_3x4x3_v3_smp7.yaml`.

Konteks prasyarat mengikuti subtopik korpus kelas 7: bilangan bulat/rasional, rasio/skala, aljabar, hubungan sudut/kesebangunan, dan data/diagram. Konteks ini adalah rubrik penelitian yang perlu diperiksa ahli; bukan klaim bahwa seluruh siswa telah menguasai semua topik. Penilaian mempertimbangkan tuntutan solusi minimum. Notasi variabel, pecahan, tanda negatif, dan angka besar tidak otomatis membuat soal Hard.

Generator dan audit memilih versi/hash rubrik berdasarkan grade. Resume menolak perubahan grade, model, sumber, versi prompt, atau hash rubrik. Dukungan kelas 8–12 kemudian ditambahkan melalui [runbook 30](30_KELAS8_BLIND_VALIDATION.md), [31](31_KELAS9_BLIND_VALIDATION.md), dan [32](32_KELAS10_11_12_BLIND_VALIDATION.md) dengan versi tersendiri. Perluasan ini tidak mengubah kelas yang didukung model IndoBERT, konfigurasi training SD, atau gate publikasi.

## Mekanisme penilaian

Tiga run awal menerima soal, opsi, kunci sumber, gambar, dan rubrik kelas 7. Prediksi IndoBERT, estimasi agen, vote run lain, konsensus, dan distribusi target tidak masuk prompt. Kesepakatan 3–0 dapat diterima sebagai silver. Ketidaksepakatan, abstain, konflik kunci, dan masalah konten masuk adjudikasi AI terpisah.

Audit mengunci checkpoint melalui SHA-256 sebelum pemeriksaan scope model. Semua kategori difficulty tetap diekspor, termasuk kategori kosong. Distribusi tidak dipaksakan seimbang. Masalah konten atau kunci membuat `revision_required` atau `llm_retry_or_manual_review`, meskipun terdapat label usulan.

Model IndoBERT lama hanya menerima kelas 1–6. Untuk kelas 7, runtime mengembalikan `out_of_scope` dan seluruh head `abstain`: label, confidence, dan entropy null; probabilitas kosong. Encoder tidak dijalankan. Jangan mengubah scope model agar memperoleh angka prediksi SMP dari artifact SD. Pembandingan dengan label blind tidak menghasilkan agreement/disagreement yang bermakna bila model abstain. Model untuk SMP membutuhkan pekerjaan training/evaluasi tersendiri.

## Perintah batch

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas7/soal_pretest_db.json --grade 7 `
  --output output/pretest/kelas7/revalidasi_blind_20261002_v1/silver_labels.json `
  --runs 3 --workers 1 --pause 3 --attempts 3 --execute
```

Run sukses disimpan dan tidak dipanggil ulang saat resume. Nama generator masih historis; argumen source/grade mengatur kelas sebenarnya. `.env` tidak perlu diubah untuk menetapkan batas output token pada proses ini.

Setelah semua run dan adjudikasi selesai:

```powershell
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py `
  --source output/pretest/kelas7/soal_pretest_db.json --grade 7 `
  --checkpoint output/pretest/kelas7/revalidasi_blind_20261002_v1/silver_labels.json `
  --output-dir output/pretest/kelas7/revalidasi_blind_20261002_v1/audit-v1

.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py `
  --source output/pretest/kelas7/soal_pretest_db.json `
  --checkpoint output/pretest/kelas7/revalidasi_blind_20261002_v1/silver_labels.json `
  --audit output/pretest/kelas7/revalidasi_blind_20261002_v1/audit-v1/pilot_audit.json `
  --artifact models/indobert-3x4x3-v1 `
  --output-dir output/pretest/kelas7/revalidasi_blind_20261002_v1/bundle
```

Audit yang belum lolos gate tetap dapat dipakai untuk laporan, tetapi tidak menyetujui ekspansi/training. Jangan mengubah atau me-resume checkpoint setelah audit final. Audit dan bundle memakai direktori versi baru dan menolak overwrite. Jika provider berhenti karena kuota, checkpoint kerja dapat dilanjutkan sebelum audit final; salinan audit/bundle sementara harus tetap utuh.

## Keluaran

Bundle menggunakan `ai-decision-bundle-v2-blind` untuk keputusan, `question-validation-input-v2-blind` untuk soal, dan `blind-difficulty-groups-v1` untuk pengelompokan. Konsumen membaca label dari `items[].llmAdvisory.advisoryLabels` bersama `finalRouting` dan `humanValidation`.

`difficulty/Easy.json`, `difficulty/Medium.json`, `difficulty/Hard.json`, dan `difficulty/undecided.json` memuat subset advisory. `contentQualified` hanya menandai soal tanpa blocker konten AI; pemeriksaan ahli tetap wajib. Topik diekspor sebagai `Matematika SMP Kelas 7`. `indobert_predictions.json` merekam abstention di luar cakupan, bukan prediksi terkalibrasi kelas 7.

Laporan aktif berada di `output/pretest/kelas7/hasil_validasi`. Salinan versi berada di direktori batch. Hasil lama, jika ada, diarsipkan sebelum laporan aktif diperbarui. Batch ini tidak melatih ulang model atau menghitung CTT/IRT dari respons siswa.

## Hasil eksekusi 2 Oktober 2026

Seluruh 49 soal selesai dengan 147 run awal sukses dan 16 adjudikasi AI. Distribusi advisory: Easy 28, Medium 20, Hard 1, undecided 0. Satu soal Hard adalah nomor 33, ID `78652b4108bd747c96b2f4a8`, tentang hubungan panjang pada segitiga dengan garis sejajar dan garis bagi sudut. Semua soal tetap `pending_expert_review`; gold manusia null.

Audit mengunci checkpoint dan mengonfirmasi cakupan 49/49, sumber/input cocok, tidak ada kebocoran prediksi ke prompt blind, serta versi/hash rubrik cocok. `requiredEvidenceComplete` masih FAIL karena run 3 soal 37 (`544a2e4954b07fcf67f1ed3c`) menandai `answerKeyStatus=conflict`. Adjudikasi kemudian menerima kunci C tetapi mempertahankan catatan penghitungan huruf nama. Riwayat konflik tidak dihapus; `readyForExpansion=false`.

Run 1 soal 18 sempat gagal karena `verifiedMinimalSolution` melampaui batas 700 karakter. Resume mempertahankan semua run sukses. Retry terakhir memakai temperature 0.7 pada proses untuk run tersebut, dengan prompt/rubrik/schema yang sama; run awal lain memakai temperature 0.2 dan adjudikasi tetap 0.0. Respons diterima setelah lolos schema, tanpa pemotongan solusi atau pelonggaran validator. `.env` tidak diubah. Token sukses yang tercatat berjumlah 386.009; percobaan gagal dapat menambah penggunaan provider yang tidak tercatat pada checkpoint.

Lihat [laporan aktif](../output/pretest/kelas7/hasil_validasi/LAPORAN_VALIDASI.md), [kelompok difficulty](../output/pretest/kelas7/hasil_validasi/difficulty_groups.json), dan [audit terkunci](../output/pretest/kelas7/revalidasi_blind_20261002_v1/audit-v1/pilot_audit.json). Seluruh 49 diagnostik IndoBERT abstain di luar cakupan SMP; nol disagreement tidak berarti model setuju dengan Gemini.
