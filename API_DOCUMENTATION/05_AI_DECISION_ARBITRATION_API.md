# Keputusan AI dan qualification silver

Gemini menilai setiap soal tiga kali secara blind. Prompt awal tidak memuat prediksi IndoBERT, estimasi difficulty agen, suara run lain atau kuota distribusi label. Ketiga suara sepakat dapat diterima; perbedaan, abstain dan masalah konten menggunakan adjudikasi AI terpisah.

Tiga run berasal dari model yang sama. Vote agreement adalah kestabilan keputusan AI dan tidak disamakan dengan probabilitas confidence yang terkalibrasi.

| Status | Arti | Tindakan |
|---|---|---|
| `silver_ready` | Label, konten dan bukti cukup untuk qualification | Bekukan ke snapshot silver |
| `revision_required` | Struktur, konten atau kunci bermasalah | Tahan dan perbaiki konten; validasi ulang AI |
| `needs_ai_review` | Label atau pemetaan kunci belum tuntas | Retry/adjudikasi AI; tahan dari delivery |

Label tersimpan pada `items[].llmAdvisory.advisoryLabels`. `labelProvenance=ai_silver` dan `reviewMode=automated_ai`. Persetujuan pelabel manusia tidak diperlukan. Riwayat run gagal tidak dihitung sebagai suara; run sukses yang sudah terkunci tidak ditimpa.

Qualification operasional ditetapkan di `app/silver/policy.py`; `scripts/build_operational_silver.py` memeriksa ID, hash sumber, prompt/response, kunci, solusi dan byte gambar. Kunci jawaban AI berupa nilai dapat dipetakan ke opsi secara deterministik bila unambiguous; hasil yang tidak cocok tetap ditahan.

Inference IndoBERT hanya diagnostik pada bundle blind dan tidak menimpa label terkunci. Prediksi classifier tunggal belum cukup untuk membuat item `silver_ready` tanpa bukti validasi AI dan qualification konten.
