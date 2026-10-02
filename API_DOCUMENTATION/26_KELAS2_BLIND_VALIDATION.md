# Validasi kelas 2 dengan rubrik grade-aware

Korpus pretest kelas 2 berisi 44 soal di `output/pretest/kelas2/soal_pretest_db.json`. Kelas sasaran diberikan melalui `--grade 2` karena `kelas_id` pada sumber lama dapat bernilai null. Sumber dan kunci ekstraksi dipertahankan; penilaian AI tidak mengubahnya menjadi gold ahli.

## Penilaian dan skema hasil

Tiga run Gemini menilai soal, gambar, kunci sumber, dan solusi minimum secara blind. Prediksi IndoBERT, estimasi agen, dan distribusi target tidak masuk prompt. Rubrik `math-rubric-3x4x3-v2-grade-aware` menilai difficulty relatif terhadap siswa kelas 2:

- `Easy`: tugas familiar dan langsung dengan beban rendah.
- `Medium`: beberapa langkah rutin yang terkait, pemilihan prosedur, atau perpindahan representasi.
- `Hard`: strategi nonrutin, constraint saling terkait, justifikasi, atau integrasi representasi kompleks.

Kesepakatan 3–0 diterima sebagai silver. Ketidaksepakatan, abstain, atau masalah konten/kunci memerlukan adjudikasi AI terpisah. Label akhir mengikuti checkpoint blind yang dikunci dengan audit SHA-256. IndoBERT lama hanya menghasilkan diagnostik setelah audit; tidak menentukan label akhir dan tidak dilatih ulang oleh proses ini.

Bundle menggunakan `ai-decision-bundle-v2-blind`. Konsumen membaca `items[].llmAdvisory.advisoryLabels`, `items[].finalRouting`, dan `items[].humanValidation`. Gold ahli tetap null. Routing `revision_required` dan `llm_retry_or_manual_review` harus tetap dibaca meskipun item memiliki label usulan.

Pengelompokan difficulty tersedia dalam `difficulty_groups.json` serta `difficulty/Easy.json`, `difficulty/Medium.json`, `difficulty/Hard.json`, dan `difficulty/undecided.json`. Setiap subset memuat kelas sasaran, jumlah usulan, jumlah soal tanpa blocker konten, serta item dengan soal, label advisory, routing, `contentQualified`, dan kewajiban review ahli. Kategori kosong tetap diekspor. `contentQualified=true` berarti tanpa blocker konten pada batch AI, bukan izin publikasi atau gold ahli.

Distribusi tidak dipaksakan seimbang. Bila Medium atau Hard kosong, audit meminta boundary analysis; tidak membuat label buatan atau mengubah label yang terkunci. Soal tambahan atau varian membutuhkan tahap terpisah dan validasi baru.

## Eksekusi dan resume

Hasil aktif kelas 2 hanya berada di `output/pretest/kelas2/hasil_validasi/`. Checkpoint dan audit final berada di subfolder `bukti_validasi/`; arsip, checkpoint sementara, dan salinan bundle lama telah dihapus setelah verifikasi hash. Untuk batch baru, gunakan lokasi sementara yang berbeda dan jangan me-resume checkpoint final yang sudah dikunci.

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas2/soal_pretest_db.json --grade 2 `
  --output output/validation_work/kelas2/silver_labels.json `
  --runs 3 --workers 3 --pause 1 --attempts 3 --execute
```

Nama script generator masih historis; `--grade` dan `--source` mengatur kelas sebenarnya. Perintah dapat diulang sebelum audit final: run sukses tidak dipanggil ulang, kegagalan lama disimpan dalam `retryHistory`, dan run gagal dapat dicoba kembali. Konfigurasi provider dibaca dari environment proyek; tidak perlu mengubah `.env` untuk packaging lokal. Setelah audit final, jangan melanjutkan atau mengubah checkpoint yang telah dikunci.

```powershell
.\.venv\Scripts\python.exe scripts/audit_grade_aware_pilot.py `
  --source output/pretest/kelas2/soal_pretest_db.json --grade 2 `
  --checkpoint output/validation_work/kelas2/silver_labels.json `
  --output-dir output/validation_work/kelas2/audit

.\.venv\Scripts\python.exe scripts/build_blind_validation_bundle.py `
  --source output/pretest/kelas2/soal_pretest_db.json `
  --checkpoint output/validation_work/kelas2/silver_labels.json `
  --audit output/validation_work/kelas2/audit/pilot_audit.json `
  --artifact models/indobert-3x4x3-v1 `
  --output-dir output/validation_work/kelas2/bundle
```

Audit exit code 2 berarti gate ekspansi/training belum lolos. Laporan tetap dapat dibuat untuk memperlihatkan distribusi dan blocker; packaging tidak menyetujui ekspansi. Bundle menolak menimpa direktori hasil yang sudah berisi file. Semua keluaran, termasuk subset difficulty, dicatat hash-nya dalam manifest. Tautan gambar dihitung dari lokasi bundle agar laporan dapat ditempatkan di direktori versi maupun `hasil_validasi`.

Tidak ada training ulang, pengiriman ke siswa, CTT, atau IRT pada **batch validasi AI ini**. Backend kini menyediakan pilot dan analisis empiris [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md), tetapi label bundle ini tetap advisory, bukan human gold atau respons siswa.

## Hasil batch 2 Oktober 2026

Seluruh 44 soal selesai dengan 132/132 run awal sukses dan 24 adjudikasi AI. Distribusi semua usulan: Easy 37, Medium 6, Hard 0, dan belum diputuskan 1. Setelah mengecualikan 3 soal `revision_required`, tersisa 35 Easy dan 6 Medium pada 41 soal `pending_expert_review`. Gold ahli tetap null.

Checkpoint dan audit terkunci tersedia di `output/pretest/kelas2/hasil_validasi/bukti_validasi/`. Gate hash, kelengkapan item, tiga run, dan blind prompt lolos. Gate kelengkapan evidence dan boundary analysis belum lolos; `readyForExpansion=false`. Hard kosong dan beberapa pemeriksaan kunci/visual belum lengkap. Laporan aktif ada di `output/pretest/kelas2/hasil_validasi/`; tidak ada salinan bundle atau arsip hasil lama. Lokasi di dalam audit tetap merupakan catatan historis, sedangkan manifest menunjuk lokasi berkas saat ini. Indeks seluruh kelas tersedia di [output/pretest/README.md](../output/pretest/README.md).
