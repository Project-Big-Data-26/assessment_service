# Alur terhubung silver -> siswa -> IRT

1. Ekstraksi menyimpan konten dan lineage JSON.
2. Gemini blind N=3 memeriksa soal, gambar, kunci dan tiga label; konflik menggunakan adjudikasi AI.
3. Qualification memisahkan `silver_ready`, `revision_required` dan `needs_ai_review`.
4. Builder membekukan snapshot silver serta memeriksa checksum dan provenance.
5. Registrasi snapshot dan blueprint menghubungkan dataset ke delivery siswa.
6. Server menilai respons dan menyimpan event sesuai versi soal.
7. Screen menghitung CTT dan IRT bila data/bukti asumsi cukup, lalu menyimpan feedback otomatis.
8. Masalah kualitas ditahan untuk revisi dan penilaian ulang AI. Versi baru dapat masuk freeze berikutnya.

Label awal tetap silver AI. Difficulty empiris dapat berbeda sesuai data populasi dan window; sistem menyimpan keduanya. Feedback tidak menimpa label awal atau melatih model aktif secara diam-diam.

Delivery silver dan feedback otomatis sudah diimplementasikan. Tidak ada tugas pelabelan guru, assignment ahli atau gate gold. Operator tetap mengelola integrasi, data dan proses komputasi. Gambar Buku Guru masih menjadi bukti sumber bila tersedia.

Personalization penuh belum tersedia: CAT, mastery per topik, release calibration, equating dan online model updates masih rancangan. IRT tidak otomatis dipanggil setiap respons; integrasi menjalankan pekerjaan screen sesuai jadwal atau jumlah data.

Rujukan: [08 delivery](08_ASSESSMENT_DELIVERY_API.md), [27 IRT](27_PSYCHOMETRICS_IMPLEMENTATION_RUNBOOK.md), [36 migrasi](36_SILVER_OPERATIONAL_INTEGRATION.md). Diagram gambar menggunakan alur yang sama dan membedakan fitur bersyarat dari rancangan.
