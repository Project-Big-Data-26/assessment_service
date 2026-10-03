# Melanjutkan validasi AI yang tertunda

Status terbaru dan daftar ID soal ada di [PENDING_AI_VALIDATION.json](PENDING_AI_VALIDATION.json). Kelas 8–10 selesai dinilai AI. Kelas 11 tertahan pada run ketiga soal ke-21, dan kelas 12 belum dinilai. Kelas 1–5 memakai checkpoint baru karena 102 soal/gambar berubah setelah penilaian lama; run yang masih cocok telah dipertahankan.

Gunakan model yang tercatat di checkpoint (`gemini-3.1-flash-lite`), rubrik yang sama, N=3, satu worker, dan output maksimal 4096 token. Kuota harian provider terakhir dilaporkan sebesar 500 request per project per model. Setelah kuota tersedia, perintah berikut melanjutkan checkpoint kerja, melewati batch lengkap, dan berhenti jika provider kembali memblokir. Jalankan dari root proyek.

```powershell
$env:GEMINI_MAX_OUTPUT_TOKENS = '4096'
$aiBacklog = Get-Content -LiteralPath 'output/pretest/PENDING_AI_VALIDATION.json' -Raw -Encoding UTF8 | ConvertFrom-Json
foreach ($aiBatch in $aiBacklog.grades) {
    if ($aiBatch.pendingAIQuestionCount -eq 0) { continue }
    $aiCheckpoint = Get-Content -LiteralPath $aiBatch.checkpoint -Raw -Encoding UTF8 | ConvertFrom-Json
    if (($aiCheckpoint.summary.successfulRuns -eq $aiBatch.targetRuns) -and
        ($aiCheckpoint.summary.failedRuns -eq 0) -and
        ($aiCheckpoint.summary.pendingAdjudication -eq 0)) { continue }
    $aiSource = "output/pretest/kelas$($aiBatch.grade)/soal_pretest_db.json"
    .\.venv\Scripts\python.exe scripts/generate_silver_labels_kelas1.py `
        --source $aiSource --grade $aiBatch.grade --output $aiBatch.checkpoint `
        --runs 3 --workers 1 --pause 3 --attempts 3 --execute
    if ($LASTEXITCODE -ne 0) { break }
}
```

Jangan resume checkpoint lama kelas 1–5 di `hasil_validasi/bukti_validasi/`: bukti itu terikat sumber sebelum koreksi. Jangan mengubah rubrik/sumber/model saat batch sedang berjalan atau resume snapshot di folder `seed_snapshot_20261003_v1`, `resume_20261003_v1`, dan `partial-v1`. File rubrik SD harus mempertahankan byte LF yang sesuai hash checkpoint; checkout Windows dengan CRLF dapat menyebabkan penolakan hash walaupun teks sama.

Setelah penilaian selesai, salin checkpoint kerja ke snapshot versi baru, lalu jalankan `scripts/audit_grade_aware_pilot.py` dan `scripts/build_blind_validation_bundle.py` terhadap snapshot tersebut. Audit exit code 2 berarti gate penelitian belum lolos; tetap boleh membangun laporan konten/label, tetapi tidak menyetujui training. Arsipkan laporan aktif sebelum menggantinya, lalu verifikasi seluruh hash manifest, sumber, opsi, kunci, aset, dan ekspor ID soal. Jangan menimpa snapshot atau audit lama.

Kelengkapan AI berbeda dari kelayakan konten. Soal yang selesai dinilai dapat tetap berstatus `revision_required` atau `pending_expert_review`; gold ahli tidak diisi otomatis. Model IndoBERT tetap diagnostik dan tidak menggantikan keputusan Gemini.
