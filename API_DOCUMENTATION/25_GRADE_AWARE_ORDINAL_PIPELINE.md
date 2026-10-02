# Pipeline Klasifikasi 3-Head Grade-Aware v2

Dokumen ini adalah runbook untuk pipeline baru. Artifact, snapshot, checkpoint, audit, dan batch lama tetap dipertahankan. Setiap keluaran final menolak overwrite; checkpoint LLM hanya boleh berubah selama proses resume dan kemudian dikunci oleh hash audit.

## Alur yang berlaku

1. Pilih pilot 60 soal secara deterministik dari korpus kelas sasaran. Stratifikasi memakai bab, visual, jenis sumber, dan band estimasi agen hanya untuk sampling.
2. Jalankan tiga review LLM yang blind. Prompt tidak memuat prediksi IndoBERT, nilai estimasi agen, vote lain, atau distribusi target.
3. Terima langsung hanya keputusan 3-0. Kasus 2-1, abstain, content concern, konflik kunci, atau output provider yang tidak lengkap masuk satu adjudikasi terpisah.
4. Audit pilot dan kunci checkpoint melalui SHA-256. Jika `Medium`/`Hard` tidak muncul atau satu label melebihi 90%, ekspansi berhenti sampai boundary analysis tertulis disetujui. Boundary analysis tidak boleh mengubah label.
5. Setelah pilot lolos, bangun snapshot kelas 1-6 dengan split group-aware 70/15/15. Source family, stimulus yang sama, exact duplicate, dan near duplicate tidak boleh melintasi split.
6. Train shared IndoBERT + LoRA dengan Head 1/2 multiclass dan Head 3 cumulative ordinal yang menerima grade embedding.
7. Kalibrasi global pada validation. Kalibrasi per-grade hanya aktif bila setiap kelas pada grade tersebut memiliki minimal 10 sampel validation dan menghasilkan threshold nontrivial.
8. Jalankan prediksi research, lalu bandingkan dengan silver yang sudah dikunci. Tidak ada reviewer LLM pascaprediksi pada pipeline baru.
9. Artifact silver selalu `researchOnly=true`. API publik tetap 503 sampai tersedia gold manusia, semua gate teknis lolos, dan artifact mendapat approval eksplisit.

## Perintah pilot kelas 1

```powershell
.\.venv\Scripts\python.exe scripts\prepare_grade_aware_pilot.py `
  --grade 1 --limit 60 --seed 42 `
  --output-dir output\pilots\kelas1-grade-aware-v2.2

.\.venv\Scripts\python.exe scripts\generate_silver_labels_kelas1.py `
  --source output\pilots\kelas1-grade-aware-v2.2\questions.json `
  --grade 1 `
  --output output\pilots\kelas1-grade-aware-v2.2\silver_labels_gemini_3_8_flash_v4.json `
  --runs 3 --workers 1 --pause 2 --attempts 5 --execute
```

Perintah kedua resumable. Run sukses tidak dipanggil ulang; run `429`, `503`, invalid schema, atau kegagalan lain tetap dianggap gagal dan dicoba lagi pada invocation berikutnya.

Setelah semua item selesai:

```powershell
.\.venv\Scripts\python.exe scripts\audit_grade_aware_pilot.py `
  --source output\pilots\kelas1-grade-aware-v2.2\questions.json `
  --checkpoint output\pilots\kelas1-grade-aware-v2.2\silver_labels_gemini_3_8_flash_v4.json `
  --grade 1 `
  --output-dir output\pilots\kelas1-grade-aware-v2.2\audit-v1
```

Exit code nonzero berarti ekspansi harus berhenti. Jika satu-satunya kegagalan adalah boundary alami, buat JSON baru yang berisi `accepted=true`, `checkpointSha256` dari audit, `rationale`, `reviewedBy`, dan `createdAt`, lalu buat audit versi baru dengan `--boundary-analysis`. Jangan mengedit audit atau checkpoint lama.

## Snapshot dan training

Snapshot per grade dibuat dari checkpoint v4 yang kunci dan solusi minimumnya terverifikasi:

```powershell
.\.venv\Scripts\python.exe scripts\build_silver_snapshot_kelas1.py `
  --source <questions-grade-N.json> `
  --silver <silver-v4-grade-N.json> `
  --audit <audit-grade-N\pilot_audit.json> `
  --grade <N> --id-namespace kelas<N> `
  --snapshot-id <snapshot-version-baru> `
  --output <snapshot-version-baru.json>
```

Gabungkan snapshot kelas 1-6:

```powershell
.\.venv\Scripts\python.exe scripts\build_multigrade_snapshot_v2.py `
  --snapshot <kelas1.json> --snapshot <kelas2.json> --snapshot <kelas3.json> `
  --snapshot <kelas4.json> --snapshot <kelas5.json> --snapshot <kelas6.json> `
  --snapshot-id <combined-version-baru> `
  --output <combined-version-baru.json>
```

Training normal menolak missing class dan snapshot yang gagal gate:

```powershell
.\.venv\Scripts\python.exe -m app.training.v2.train_lora `
  --snapshot <combined-version-baru.json> `
  --output-dir models\indobert-3x4x3-grade-aware-v2-<version> `
  --work-dir runs\indobert-3x4x3-grade-aware-v2-<version> `
  --model-version indobert-3x4x3-grade-aware-v2-<version>
```

Search memakai rank `{8,16}`, learning rate `{1e-4,2e-4}`, dan final seed `{13,42,73}`. Checkpoint dipilih berdasarkan lolos anti-collapse, macro-F1 head terendah, lalu rata-rata macro-F1.

## Research inference dan disagreement

Artifact yang tidak servable hanya dapat digunakan dengan flag eksplisit:

```powershell
.\.venv\Scripts\python.exe scripts\run_indobert_silver_kelas1.py `
  --snapshot <snapshot.json> --artifact <artifact-dir> `
  --output <predictions-version-baru.json> `
  --allow-research-artifact
```

Prediksi harus dibuat setelah audit mengunci blind labels. Perbandingan berikut hanya melakukan join offline dan tidak mengirim prediksi ke LLM:

```powershell
.\.venv\Scripts\python.exe scripts\compare_blind_labels_to_predictions.py `
  --silver <silver-v4.json> `
  --audit <audit-v1\pilot_audit.json> `
  --predictions <predictions-version-baru.json> `
  --output <disagreement-version-baru.json>
```

`review_indobert_gemini_kelas1.py` adalah jalur legacy anchored. Script tersebut kini berhenti secara default dan hanya tersedia dengan opt-in eksplisit untuk reproduksi historis.

## Gate model dan API

Artifact tidak servable bila salah satu kondisi berikut benar:

- `researchOnly=true`;
- `approvedForProvisional=false`;
- `dataGatesPassed=false`;
- `antiCollapsePassed=false`;
- `promotionGates.passed` bukan `true`.

Promotion teknis mensyaratkan Head 3 macro-F1 minimal 0,65, setiap class F1 minimal 0,50, ECE tiap head maksimal 0,10, selective accuracy minimal 0,80 pada coverage minimal 0,70, unggul dari majority baseline, tidak ada supported class dengan recall nol, dan stabil pada tiga seed. Artifact berbasis silver tetap research-only meskipun semua metrik teknis terpenuhi.

## Status historis pilot awal saat implementasi

- Pilot final v2.2 berhasil disiapkan: 266 soal kelas 1 ditemukan, 173 lolos qualification awal, 60 dipilih, dan 43 source family dipertahankan untuk mencegah leakage.
- Smoke v4 pada snapshot pendahulu v2.1 belum memperoleh run valid karena provider mengembalikan `429`, `503`, lalu `429`. Checkpoint gagal itu tetap disimpan sebagai histori.
- Pipeline berhenti sebelum snapshot, training, atau promotion; tidak ada data gagal yang diperlakukan sebagai label.
- Checkpoint dapat dilanjutkan dengan perintah yang sama setelah quota/provider pulih.

Status di atas adalah histori pilot awal, bukan status seluruh batch terkini. Laporan aktif kelas 1–6 ada pada [indeks validasi](../output/pretest/README.md) dan [26](26_KELAS2_BLIND_VALIDATION.md); audit hash tetap menentukan apakah checkpoint boleh dilanjutkan. Pembaruan sistem berikutnya menambahkan CTT/IRT, pilot server-scored dan empirical expert hold pada [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md). Hasil AI di folder validasi tetap bukan respons siswa/gold; tidak otomatis menjadi data kalibrasi atau delivery.
