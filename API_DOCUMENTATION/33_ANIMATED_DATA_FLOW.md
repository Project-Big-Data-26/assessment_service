# Animasi aliran data silver

[Buka animasi interaktif](33_ANIMATED_DATA_FLOW.html). Alur dimulai dari JSON ekstraksi, validasi blind AI N=3, qualification silver, snapshot, model, delivery siswa, scoring, CTT/IRT dan feedback otomatis.

Sistem memakai label silver AI tanpa persetujuan pelabel manusia. Operator mengelola data dan pekerjaan sistem; tidak menentukan label pedagogis. Hanya `silver_ready` masuk snapshot delivery. Soal dengan blocker ditahan untuk revisi dan revalidation AI.

Halaman terdiri dari 33 tahap beserta cerita, input/output, sumber kode dan rumus. Kalkulator softmax/confidence/entropy, Wilson CI, ordinal difficulty, probabilitas IRT, informasi tes dan EAP adalah contoh pembelajaran. Halaman tidak memanggil LLM atau memuat respons siswa nyata.

Buka HTML langsung atau jalankan:

```powershell
.\.venv\Scripts\python.exe -m http.server 8765 --bind 127.0.0.1
```

Lalu buka `http://127.0.0.1:8765/API_DOCUMENTATION/33_ANIMATED_DATA_FLOW.html`. Folder `interactive/` dan KaTeX lokal harus berdampingan dengan HTML. Tombol putar, jeda, langkah, penjelasan, salin JSON/rumus dan ringkasan PPT tersedia.

| Tahap | Arti |
|---|---|
| Validasi AI | N=3 dan adjudikasi menghasilkan label silver |
| Qualification | Kunci/solusi/visual, coverage dan hash tetap diperiksa |
| Snapshot | Versi immutable dengan provenance `ai_silver` |
| Delivery | Snapshot silver qualified, grade/track tepat, opsi opaque |
| CTT/IRT | Bukti empiris terpisah dari label awal |
| Feedback | Sistem mempertahankan, mengumpulkan data, atau menahan versi untuk AI review |
| Training berikutnya | Snapshot baru dan gate teknis; tidak auto-retrain |

`implemented` berarti fungsi kode tersedia, `conditional` memerlukan data/artifact/kredensial yang sesuai, dan `planned` belum menjadi fitur runtime. Scope IndoBERT tetap SD 1-6; delivery dan Gemini mendukung grade 1-12/TL. IRT menunggu data dan bukti asumsi, tanpa menganggap asumsi otomatis benar.

Lihat [34 ringkasan PPT](34_PPT_SUMMARY.md) dan [36 integrasi](36_SILVER_OPERATIONAL_INTEGRATION.md). Prompt/rubrik dan checkpoint lama tetap immutable sebagai bukti penilaian; policy operasional berada di luar teks prompt historis.
