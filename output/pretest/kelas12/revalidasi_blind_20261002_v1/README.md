# Batch validasi blind SMA kelas 12 — 2 Oktober 2026

**Batch belum dinilai karena kuota provider.** Target 32 soal × 3 run = 96 run awal. Tercatat 0 run dan 0 adjudikasi sukses; seluruh 32 soal belum dinilai AI. Belum ada panggilan API untuk kelas ini. Pelaksana batch bersama menundanya setelah kelas 10 melaporkan kuota harian `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Status checkpoint `waiting_provider_daily_quota`, dengan `blockedByGrade=10`.

Model penilai `gemini-3.1-flash-lite`, prompt `gemini-silver-math-3x4x3-v8-blind-sma12-key-verified`, rubrik `math-rubric-3x4x3-v6-sma12-grade-aware`. Konteks SMA relatif kelas 12; materi dan tuntutan solusi minimum menentukan label. Semua 1 referensi gambar tersedia. Sumber soal/gambar, `.env`, dan prompt/hash rubrik kelas 1-9 tetap utuh.

[Laporan status aktif](../hasil_validasi/LAPORAN_VALIDASI.md) dan [kelompok difficulty](../hasil_validasi/difficulty_groups.json) mengekspor seluruh 32 soal. Semua item `undecided`/`llm_retry_or_manual_review`, label advisory/gold null. Berkas Easy/Medium/Hard kosong karena belum ada penilaian, bukan bukti bahwa kategori tersebut tidak ada.

IndoBERT lama hanya mendukung SD 1-6. Seluruh keluaran SMA kelas 12 `out_of_scope`; tiga head abstain dengan label/confidence/entropy null serta probabilitas kosong. Encoder tidak dijalankan; input terserialisasi hanya untuk audit. Tidak ada agreement dengan Gemini yang tersedia.

## Checkpoint dan bukti

- [silver_labels.json](silver_labels.json): checkpoint kerja untuk resume.
- [Snapshot parsial](partial-v1/silver_labels.json): salinan yang dikunci untuk laporan status.
- [Audit JSON](partial-v1/audit-v1/pilot_audit.json) dan [Markdown](partial-v1/audit-v1/PILOT_AUDIT.md): sumber/input/blind/rubrik cocok, tetapi batch belum dinilai; `readyForExpansion=false`.
- [Bundle versi status](partial-v1/bundle/README.md) dan [manifest aktif](../hasil_validasi/manifest.json): keluaran offline.
- [execution_verification.json](partial-v1/execution_verification.json): verifikasi ekspor, hash, gambar, status tanpa label, dan scope.
- [Status batch bersama](../../revalidasi_blind_20261002_v1_sma_execution.json): status ketiga kelas dan asal blok provider.

SHA-256 sumber: `086fe5310aab2fafc691ede89aef2851bdf28a2929aa5deb6cd7b808f19863a7`.
SHA-256 snapshot: `0900ae4f0bf26031c99fd7233d858645fdd6a5304cba4b7f7ea3c16cf0b08257`.
SHA-256 rubrik: `677d45abd86a27baa6fe1a891a5775c1a42216e831991928c35351a9b80bdd7d`.

Token sukses tercatat 0. Packaging tidak memanggil LLM. Tidak ada training, publishing, respons siswa, CTT, atau IRT.

## Resume ketika kuota tersedia

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_sma.py `
  --grades 10 11 12 --batch-name revalidasi_blind_20261002_v1 --execute
```

Pelaksana menyiapkan/melanjutkan checkpoint kerja, mempertahankan run sukses, dan menghentikan kelas berikutnya bila provider memblokir kelas sebelumnya. Jangan menjalankan ulang selama kuota belum tersedia, me-resume snapshot `partial-v1`, mengubah sumber/rubrik di tengah batch, atau menimpa audit/bundle status.

Setelah batch lengkap, buat audit/bundle final dalam direktori baru dan arsipkan laporan aktif sementara sebelum menggantinya. Aturan dan perintah ada di [runbook SMA](../../../../API_DOCUMENTATION/32_KELAS10_11_12_BLIND_VALIDATION.md).
