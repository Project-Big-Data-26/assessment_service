# Arsip Smoke Evaluation Gemini

> Dokumen historis. Gemini tidak lagi menjadi provider LLM target; Claude dipilih untuk pipeline IndoBERT→LLM→tiga annotator. Evaluasi berikut tidak dapat digunakan untuk menyatakan Claude sudah terpasang, memiliki API key, atau memenuhi kualitas model.

## Hasil historis 27 September 2026

Prototype backend lama pernah menjalankan smoke test Gemini untuk solver, klasifikasi C1–C6 dan adjudikator AI. Dua dari enam kasus selesai dan lolos; empat kasus tidak terukur karena HTTP 429/gangguan provider. Rasio 2/6 bukan akurasi. Hasil ini hanya menunjukkan sebagian koneksi prototype pada konfigurasi lama. Folder `project_assessment` beserta runner/fixture lama sudah tidak ada di worktree, sehingga perintah lama tidak boleh dipakai.

| Kasus | Catatan |
|---|---|
| Fakta pi dan luas lingkaran | Solver lama menghasilkan jawaban yang diharapkan pada sampel selesai |
| Soal tidak lengkap, klasifikasi dan adjudikasi | Tidak terukur lengkap akibat gangguan akses |
| Kesiapan produksi | Tidak pernah dibuktikan oleh smoke test ini |

Output lama, jika masih ada pada lingkungan lain, hanya artefak historis dan tidak boleh dijadikan gold label. Catatan infrastruktur baru ada di [18_CLAUDE_PROVIDER_SETUP.md](18_CLAUDE_PROVIDER_SETUP.md). Evaluasi baru harus memakai rubrik 3 × 4 × 3 dan gold tiga pakar; jangan memindahkan verdict Gemini menjadi verdict Claude.

## Hubungan dengan merge terbaru

Pipeline pretest agentic yang baru tidak mengaktifkan kembali Gemini. Jalur barunya memakai Claude Code untuk ekstraksi lokal, sedangkan file `llm_backend.py` pada jalur legacy masih menunjuk Ollama `qwen3:4b`. Keduanya terpisah dari Claude Messages API target untuk audit hasil IndoBERT. Dengan demikian arsip smoke Gemini tetap historis dan tidak menjadi pembanding langsung bagi kualitas ekstraksi 1.254 soal yang baru.
