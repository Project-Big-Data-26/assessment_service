# Batch validasi blind SMP kelas 8 — 2 Oktober 2026

**Batch belum selesai karena kuota harian provider.** Target 42 soal × 3 run = 126 run awal. Tersimpan 8 run sukses: dua soal lengkap, satu soal baru dua run, dan 39 soal belum dinilai. Run 3 soal ke-3 gagal dengan `ClientError:429`; provider melaporkan kuota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`. Tidak ada adjudikasi sukses. Checkpoint kerja berstatus `blocked_provider_daily_quota`.

Model penilai `gemini-3.1-flash-lite`, prompt v6 SMP8, rubrik `math-rubric-3x4x3-v4-smp8-grade-aware`. Pengaturan proses: temperature 0.2, max output tokens 4096, satu worker, pause 3 detik. `.env`, sumber soal/gambar, prompt dan hash rubrik kelas 1-7 tidak diubah.

| Difficulty sementara | Jumlah |
|---|---:|
| Easy | 1 |
| Medium | 1 |
| Hard | 0 |
| Undecided | 40 |

Angka ini bukan distribusi akhir kelas 8. [Laporan sementara aktif](../hasil_validasi/LAPORAN_VALIDASI.md) dan [kelompok difficulty](../hasil_validasi/difficulty_groups.json) mencakup seluruh 42 soal. Dua soal `pending_expert_review`; 40 belum memiliki keputusan dan dirutekan `llm_retry_or_manual_review`. Semua gold ahli null. Seluruh diagnostik IndoBERT `out_of_scope`, semua head abstain dengan label/confidence/entropy null serta probabilitas kosong.

## Checkpoint kerja dan bukti terkunci

- [silver_labels.json](silver_labels.json): checkpoint kerja yang dapat dilanjutkan.
- [partial-v1/silver_labels.json](partial-v1/silver_labels.json): snapshot parsial yang dikunci sebelum pemeriksaan scope model.
- [Audit JSON](partial-v1/audit-v1/pilot_audit.json) dan [Markdown](partial-v1/audit-v1/PILOT_AUDIT.md): input/rubrik/blind cocok; batch belum lengkap, `readyForExpansion=false`.
- [Bundle versi parsial](partial-v1/bundle/README.md) dan [manifest aktif](../hasil_validasi/manifest.json): keluaran offline dari snapshot terkunci.
- [execution_verification.json](partial-v1/execution_verification.json): verifikasi offline kelengkapan ekspor, status parsial, hash, scope, dan gambar.

SHA-256 sumber: `a0e4625d81e79745117847233166fb745925d664ff5969f7fb5e47d6f3bc90a8`.
SHA-256 snapshot parsial: `e8f315b35fcff6fb0807e87df6fb37f0125837b89fd3e6385723d1902d575a72`.
SHA-256 rubrik kelas 8: `c32c97b5617645fa299e0b746313d96576f83bfaab5c33ef063ad17e6a2846d4`.

Token sukses tercatat 18.381; provider dapat mencatat usage tambahan dari percobaan gagal. Packaging tidak membuat API call. Tidak ada training, publikasi soal, respons siswa, CTT, atau IRT.

## Melanjutkan saat kuota tersedia

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas8/soal_pretest_db.json --grade 8 `
  --output output/pretest/kelas8/revalidasi_blind_20261002_v1/silver_labels.json `
  --runs 3 --workers 1 --pause 3 --attempts 3 --execute
```

Generator mempertahankan run sukses dan mengulang hanya run yang gagal atau belum ada. Jangan resume snapshot di `partial-v1`, mengubah rubrik/sumber di tengah batch, atau menimpa audit/bundle parsial. Setelah run lengkap, buat audit/bundle versi baru. Arsipkan laporan aktif sementara sebelum menggantinya dengan hasil lengkap.

Aturan dan perintah lengkap tersedia di [runbook kelas 8](../../../../API_DOCUMENTATION/30_KELAS8_BLIND_VALIDATION.md).
