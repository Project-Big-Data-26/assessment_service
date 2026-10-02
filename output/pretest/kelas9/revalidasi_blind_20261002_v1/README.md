# Batch validasi blind SMP kelas 9 — 2 Oktober 2026

**Batch tertahan kuota sebelum penilaian pertama berhasil.** Target 42 soal × 3 run = 126 run awal. Tercatat 0 run sukses, 1 panggilan gagal, dan 0 adjudikasi. Seluruh 42 soal belum dinilai AI. Provider mengembalikan `ClientError:429` dan quota `GenerateRequestsPerDayPerProjectPerModel-FreeTier=500`; checkpoint berstatus `blocked_provider_daily_quota`. Tidak ada retry API setelah penghentian kuota.

Model penilai `gemini-3.1-flash-lite`, prompt v7 SMP9, rubrik `math-rubric-3x4x3-v5-smp9-grade-aware`. Pengaturan proses: temperature 0.2, max output tokens 4096, satu worker, pause 3 detik. Sumber soal/gambar, `.env`, prompt/hash rubrik kelas 1-8, dan checkpoint kelas 7-8 tidak diubah.

Tidak ada label difficulty yang dapat disimpulkan: seluruh 42 item `undecided`. Berkas Easy/Medium/Hard kosong karena penilaian belum dilakukan, bukan karena kategori tersebut tidak ada pada korpus.

[Laporan status aktif](../hasil_validasi/LAPORAN_VALIDASI.md) dan [kelompok difficulty](../hasil_validasi/difficulty_groups.json) tetap mengekspor semua soal. Seluruh item `llm_retry_or_manual_review`, label advisory/gold null, dan human review wajib. Ketiga head IndoBERT `out_of_scope`/`abstain`, dengan label/confidence/entropy null dan probabilitas kosong; encoder tidak dijalankan untuk grade 9.

## Checkpoint kerja dan bukti terkunci

- [silver_labels.json](silver_labels.json): checkpoint kerja yang dapat di-resume ketika kuota tersedia.
- [Snapshot parsial](partial-v1/silver_labels.json): salinan yang dikunci sebelum pemeriksaan scope model.
- [Audit JSON](partial-v1/audit-v1/pilot_audit.json) dan [Markdown](partial-v1/audit-v1/PILOT_AUDIT.md): source/input/blind/rubrik cocok; batch belum dinilai, `readyForExpansion=false`.
- [Bundle versi status](partial-v1/bundle/README.md) dan [manifest aktif](../hasil_validasi/manifest.json): keluaran offline dari snapshot terkunci.
- [execution_verification.json](partial-v1/execution_verification.json): verifikasi hash, ekspor, gambar, status tanpa label, dan scope.

SHA-256 sumber: `b138ff3b11bce2373c9a83f70cb0d247d99dad97fb927153de82c497c85fd97f`.
SHA-256 snapshot: `d655eb35f5106977e4ce63a46f5ad47f53122252f9880085ce87c257a30e50d2`.
SHA-256 rubrik: `acd9be38d23c5cf0809ba56799cd177502b754cfbb7a2e55f4c9be07bed2cc1d`.

Token sukses tercatat 0; panggilan gagal tidak menghasilkan label. Packaging tidak memanggil LLM. Tidak ada training, publikasi soal, respons siswa, CTT, atau IRT.

## Melanjutkan ketika kuota tersedia

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS='4096'
.\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
  --source output/pretest/kelas9/soal_pretest_db.json --grade 9 `
  --output output/pretest/kelas9/revalidasi_blind_20261002_v1/silver_labels.json `
  --runs 3 --workers 1 --pause 3 --attempts 3 --execute
```

Resume memakai checkpoint kerja, bukan snapshot `partial-v1`. Generator mempertahankan run sukses dan riwayat retry. Jangan mengubah sumber/rubrik atau menimpa snapshot/audit/bundle status. Setelah batch lengkap, buat audit dan bundle final dalam direktori baru, lalu arsipkan laporan aktif sementara sebelum menggantinya.

Aturan dan perintah audit/packaging final tersedia di [runbook kelas 9](../../../../API_DOCUMENTATION/31_KELAS9_BLIND_VALIDATION.md).
