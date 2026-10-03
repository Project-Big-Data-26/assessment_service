# Konten soal dan qualification silver

`babNN.json` dan `soal_pretest_db.json` menyimpan konten sumber. Hasil ekstraksi merupakan candidate dan tidak langsung menjadi soal delivery. Import lokal membentuk identity, versi, hash, opsi stabil dan provenance. Buku Guru tetap dapat dipakai sebagai sumber kunci; buku sumber tidak bertindak sebagai pelabel sistem.

```text
candidate -> blind_ai_validation -> AI adjudication bila diperlukan
          -> silver_ready -> frozen silver snapshot -> assessment
          -> revision_required / needs_ai_review -> revisi dan validasi ulang AI
```

AI menilai `mathCognitiveDomain`, `knowledgeDimension` dan `intendedDifficulty`. Kunci, solusi, gambar, tiga run sukses serta bukti checkpoint harus memenuhi qualification. Label tetap `ai_silver` pada setiap tahap.

Tidak ada API yang meminta guru menentukan label final. Operator boleh menyiapkan atau memperbaiki isi sumber. Sesudah isi berubah, hash input berubah dan penilaian lama tidak dapat dipakai sebagai bukti versi baru.

API authoring publik dan editor revisi otomatis masih rancangan. Integrasi operasional yang sudah tersedia menggunakan [registrasi snapshot silver](08_ASSESSMENT_DELIVERY_API.md), bukan endpoint authoring target. JSON sumber tidak dikirim langsung ke siswa.
