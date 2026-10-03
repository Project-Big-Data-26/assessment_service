# Integrasi ekstraksi agentic dengan silver

`babNN.json` mempertahankan buku/bab/halaman, konten, kunci sumber, gambar, opsi/distraktor, solusi agen dan catatan ekstraksi. Data ini staging; angka difficulty agen 1-5 dan confidence exporter bukan label model terkalibrasi.

`app/ingestion/pretest_import.py` membentuk identity, hash, content version dan provenance. Buku Guru tetap sumber bukti kunci; guru tidak menentukan label pedagogis sistem. Sumber diubah melalui versi baru, bukan menimpa bukti penilaian yang terkunci.

Gemini blind N=3 menerima konten, opsi, grade, rubrik dan gambar. Prediksi IndoBERT dan vote awal lain tidak masuk prompt. AI memeriksa key/solution/visual serta tiga label. Ketidakpastian memakai abstain/adjudikasi AI dan tidak membuat label default.

`hasil_validasi/validation_results.json` memuat label silver serta routing. `scripts/build_operational_silver.py` menggabungkan bundle qualified ke snapshot dengan pemetaan opsi kunci, verified solution, namespace kelas/track, checkpoint hashes dan split yang aman. Hanya silver_ready masuk delivery; blocker tetap ditahan.

Snapshot didaftarkan melalui `/api/v1/internal/silver/snapshots`, lalu blueprint dan participant menghubungkan ke siswa. Server memetakan pilihan opaque, memberi skor dan menyimpan event sesuai versi. CTT/IRT menggunakan session selesai dan feedback sistem otomatis.

CLI import Atlas opsional, runtime auth operator di app/staff, dan SQLite assessment tidak bergantung pada akun pelabel. Endpoint annotation dan keputusan label manual telah dihapus. [36 integrasi](36_SILVER_OPERATIONAL_INTEGRATION.md) adalah acuan migration dan kontrak aktif.
