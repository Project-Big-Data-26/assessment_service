# Catatan Smoke Gemini Historis dan Runtime Aktif

Smoke backend lama untuk solver/Bloom C1–C6/adjudikator AI adalah **histori**: dua dari enam kasus selesai, empat tidak terukur karena 429/provider failure. Rasio 2/6 bukan akurasi. Runner/fixture Express lama sudah dihapus; hasil tersebut tidak menjadi gold atau bukti validitas pipeline ordinal.

Runtime saat ini memakai **Gemini adapter** pada app/llm untuk blind silver N=3/adjudikasi sebelum comparison IndoBERT. GET /v2/llm-info memberi konfigurasi lokal tanpa network check. Model ID/settings berasal dari environment; configured tidak berarti quota/availability provider sudah diverifikasi. Live generation tetap opt-in.

Pipeline agentic Claude Code untuk ekstraksi, Ollama legacy, Gemini blind labeling, dan Claude Messages API target adalah penggunaan berbeda. Koneksi atau keberhasilan salah satunya tidak membuktikan yang lain.

Batch advisory terkini tersedia pada [indeks validasi](../output/pretest/README.md) dan [26](26_KELAS2_BLIND_VALIDATION.md). Gold manusia, review blind, frozen test dan promotion tetap diperlukan. IRT/CTT berjalan pada respons siswa yang sah, bukan jumlah run LLM; [27](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md).
