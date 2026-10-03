# Delivery siswa dari snapshot silver

Delivery menerima snapshot `labelProvenance=ai_silver` yang sudah memenuhi qualification. Tidak ada gate persetujuan pelabel manusia. Flag `researchOnly` tidak menjadi larangan memakai silver untuk pilot; gate kualitas konten dan checksum tetap wajib.

## Urutan integrasi

1. Bekukan dataset memakai `scripts/build_operational_silver.py`.
2. Daftarkan JSON `DatasetSnapshot` melalui `POST /api/v1/internal/silver/snapshots`.
3. Buat form melalui `POST /api/v1/internal/assessments` dengan `snapshotId` dan daftar `questionVersionIds`.
4. Provision participant melalui `POST /api/v1/internal/assessments/{assessment_id}/participants`.
5. Siswa memulai session, mengambil item berikutnya, mengirim respons, lalu menyelesaikan session.

Registrasi dan pembuatan assessment dapat berjalan dengan service credential dan SQLite tanpa MongoDB. Operator cookie tetap alternatif ketika layanan akun dikonfigurasi.

```json
{
  "assessmentId": "pilot-kelas11-tl-v1",
  "snapshotId": "operational-silver-20261003-v2",
  "questionVersionIds": ["<versi yang tersedia dalam snapshot>"],
  "populationId": "kelas11-tl-sekolah-a",
  "assessmentFamily": "matematika-kelas11-tl",
  "grade": 11,
  "subjectTrack": "tl",
  "sessionTtlMinutes": 120
}
```

Grade delivery mendukung 1-12. Track `tl` hanya untuk kelas 11-12 dan tidak dicampur dengan reguler. Scope classifier IndoBERT saat ini tetap SD 1-6; dukungan delivery tidak memperluas scope model.

Snapshot memiliki checksum terpisah untuk `rows` dan `expansionRows`. Semua versi harus punya provenance keputusan AI, tiga run sukses, hash checkpoint/input/respons, key verified dan solusi. Gambar essential memerlukan transkripsi AI terverifikasi karena pilot aktif memakai delivery teks.

Pilihan ganda satu jawaban saja. Server membuat mapping opsi opaque dan menyimpan kunci privat. `skip` adalah missing/null. Versi yang ditahan feedback empiris ditolak pada create, next item dan respond. Rancangan media asli dan CAT belum diaktifkan.
