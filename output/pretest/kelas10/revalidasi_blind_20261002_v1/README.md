# Batch validasi blind SMA kelas 10 — 2 Oktober 2026

**Batch belum dinilai karena kuota provider.** Target 46 soal × 3 run = 138 run awal. Tercatat 0 run dan 0 adjudikasi sukses; seluruh 46 soal belum dinilai AI. Satu panggilan API pada run 1 soal pertama ditolak dengan `ClientError:429`, quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Status checkpoint `blocked_provider_daily_quota`.

Model penilai `gemini-3.1-flash-lite`, prompt `gemini-silver-math-3x4x3-v8-blind-sma10-key-verified`, rubrik `math-rubric-3x4x3-v6-sma10-grade-aware`. Konteks SMA relatif kelas 10; materi dan tuntutan solusi minimum menentukan label. Semua 10 referensi gambar tersedia. Sumber soal/gambar, `.env`, dan prompt/hash rubrik kelas 1-9 tetap utuh.

[Laporan status aktif](../hasil_validasi/LAPORAN_VALIDASI.md) dan [kelompok difficulty](../hasil_validasi/difficulty_groups.json) mengekspor seluruh 46 soal. Semua item `undecided`/`llm_retry_or_manual_review`, label advisory/gold null. Berkas Easy/Medium/Hard kosong karena belum ada penilaian, bukan bukti bahwa kategori tersebut tidak ada.

IndoBERT lama hanya mendukung SD 1-6. Seluruh keluaran SMA kelas 10 `out_of_scope`; tiga head abstain dengan label/confidence/entropy null serta probabilitas kosong. Encoder tidak dijalankan; input terserialisasi hanya untuk audit. Tidak ada agreement dengan Gemini yang tersedia.

## Checkpoint dan bukti

- [silver_labels.json](silver_labels.json): checkpoint kerja untuk resume.
- [Snapshot parsial](partial-v1/silver_labels.json): salinan yang dikunci untuk laporan status.
- [Audit JSON](partial-v1/audit-v1/pilot_audit.json) dan [Markdown](partial-v1/audit-v1/PILOT_AUDIT.md): sumber/input/blind/rubrik cocok, tetapi batch belum dinilai; `readyForExpansion=false`.
- [Bundle versi status](partial-v1/bundle/README.md) dan [manifest aktif](../hasil_validasi/manifest.json): keluaran offline.
- [execution_verification.json](partial-v1/execution_verification.json): verifikasi ekspor, hash, gambar, status tanpa label, dan scope.
- [Status batch bersama](../../revalidasi_blind_20261002_v1_sma_execution.json): status ketiga kelas dan asal blok provider.

SHA-256 sumber: `1eacd0f235f65e9ff52bdaaca8de72e6dca09502f00f27d54fd02addb2bcf3c1`.
SHA-256 snapshot: `665a92e86fefbc5ac5fc2ba3d9ac710eef50321d1a1fce104b746437ae150328`.
SHA-256 rubrik: `421d29e59807ca918a95f2f9d329d9fb53684d766f33b5ef675b01fe7213d6e8`.

Token sukses tercatat 0. Packaging tidak memanggil LLM. Tidak ada training, publishing, respons siswa, CTT, atau IRT.

## Resume ketika kuota tersedia

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_sma.py `
  --grades 10 11 12 --batch-name revalidasi_blind_20261002_v1 --execute
```

Pelaksana menyiapkan/melanjutkan checkpoint kerja, mempertahankan run sukses, dan menghentikan kelas berikutnya bila provider memblokir kelas sebelumnya. Jangan menjalankan ulang selama kuota belum tersedia, me-resume snapshot `partial-v1`, mengubah sumber/rubrik di tengah batch, atau menimpa audit/bundle status.

Setelah batch lengkap, buat audit/bundle final dalam direktori baru dan arsipkan laporan aktif sementara sebelum menggantinya. Aturan dan perintah ada di [runbook SMA](../../../../API_DOCUMENTATION/32_KELAS10_11_12_BLIND_VALIDATION.md).
