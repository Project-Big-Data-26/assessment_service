# Import dan audit relasi soal

`scripts/auto_inserter.py` dan entry point lama `app/seed/seed_pretest.py`
menggunakan pemetaan berdasarkan **kelas, nomor bab, dan nama subbab**.
Nama subbab saja tidak cukup. Nama ganda dalam lokasi yang sama memblokir import.
ID soal sumber dipertahankan.

Mode bawaan adalah **dry-run satu kali**. Perilaku lama yang langsung menulis
database dan memaksa seluruh status menjadi `active` sudah dihapus.
Watcher lama yang masih berjalan perlu dijalankan ulang untuk memuat kode baru.

## Audit lokal, tanpa database

```powershell
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py --local --report runs/question_sync/local_inventory.json
```

Menghasilkan JSON dan Markdown lengkap per subbab. Katalog dibaca dari
`API_DOCUMENTATION/Pesan_eror.md`; dokumen hanya digunakan untuk daftar lokasi,
bukan sumber ID MongoDB. `--curriculum-report` menerima laporan lain berformat
sama. Inventaris tidak memperhitungkan riwayat siswa dan bukan audit production.

Batas dihitung **per level dalam setiap subbab**: SD 10, SMP 15, SMA 20.
Surplus easy tidak menutup kekurangan medium/hard, dan surplus subbab lain tidak
menutup kekurangan subbab ini. Bab cukup hanya jika semua subbab dan levelnya
memenuhi batas. JSON memuat `level_shortfalls`, ringkasan per bab, jumlah
kombinasi subbab-level kurang, dan total kekurangan soal pada level tersebut.

## Audit database tanpa menulis

Isi `MONGODB_URI` dan `MONGODB_DATABASE` melalui environment/`.env` untuk tujuan
yang benar. Tidak ada URI atau nama database production yang disisipkan di kode.
Alamat contoh ditolak sebelum koneksi.

```powershell
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py
```

Skema katalog yang didukung:

- `kelas`: `_id`, `nomor_kelas`, `name` (kelas 11/12 menyebut Umum/Lanjut).
- `bab`: `_id`, `kelas_id`, `nomor_bab`.
- `subbab`: `_id`, `bab_id`, `name`.
- `soal`: `_id` dan field relasi/validasi yang diaudit.

Untuk nomor bab berfield lain, gunakan `--chapter-number-field NAMA_FIELD`.
Skema yang tidak dikenali memblokir proses; tidak ada fallback ke nama global.
Alternatifnya, `--catalog catalog.json` menerima daftar pemetaan eksplisit:

```json
[
  {
    "class_key": "kelas10",
    "chapter_no": 2,
    "name": "Barisan",
    "kelas_id": "111111111111111111111111",
    "subbab_id": "222222222222222222222222"
  }
]
```

Ganti ID contoh dengan ID sebenarnya yang diekspor/diperiksa dari database.

## Audit snapshot offline

Snapshot JSON memuat array `kelas`, `bab`, `subbab`, `soal`, atau `catalog` dan
`soal`. ObjectId boleh berupa string atau Mongo Extended JSON `{"$oid":"..."}`.

```powershell
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py --snapshot snapshot.json
```

Laporan memuat jumlah insert/update, kesalahan pemetaan, ID database tanpa sumber
dalam cakupan, serta nilai sebelum dan sesudah untuk setiap perubahan. Exit code
`2` berarti input/koneksi bermasalah atau ada pemetaan yang diblokir.
ID yang tidak dikenal tidak dicocokkan berdasarkan kemiripan teks dan tidak dihapus.

## Penerapan dan watcher

Setelah rencana diperiksa terhadap database tujuan, `--execute` menerapkan
perubahan. Flag ini tidak bisa dipakai dengan `--snapshot` atau `--local`.

```powershell
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py --execute --once
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py --watch
.\.venv\Scripts\python.exe -B scripts/auto_inserter.py --watch --execute
```

`--watch-only` melewati sinkronisasi awal; tetap membutuhkan `--execute` untuk
menulis. `--file output/.../hasil_validasi/validation_results.json` membatasi ke
satu ekspor resmi. Watcher memuat ulang katalog saat sumber/metadata berubah.
Kegagalan menghentikan proses agar bisa diperiksa.

Sebelum penulisan, rencana disimpan dalam berkas bertimestamp di
`runs/question_sync/`, termasuk nilai lama field yang diubah. Ini cadangan field
terdampak, bukan backup penuh database. Watcher mempertahankan tiap laporan.
Penerapan bukan transaksi seluruh database; kegagalan bulk write dapat menyisakan
sebagian operasi selesai. Jalankan audit ulang sebelum melanjutkan.

- Soal baru memakai `_id` sumber dan `$setOnInsert`, bukan ID acak.
- Soal lama diperbarui pada relasi, field validasi, dan `source_kind` saja.
  Konten/kunci dan ID tidak diganti; riwayat jawaban tidak dihapus.
- Update memakai nilai lama sebagai syarat untuk mendeteksi perubahan bersamaan.
- Status mengikuti validasi; `inactive` tetap `inactive`. Tanpa label yang valid,
  soal tidak diterbitkan sebagai `active`.
- `source_kind` adalah `exercise` atau `pretest`, untuk filter backend web.
- Soal prasyarat tetap milik kelas asal menurut metadata sesi. Salinan di kelas
  lain tidak menimpa label/status sumber utama.
- Hanya ekspor resmi `output/exercise/kelas*/batch*/hasil_validasi` dan
  `output/pretest/kelas*/hasil_validasi` dibaca; paket LaTeX dan hasil intermediate
  tidak diimpor ulang.

Lihat [panduan perbaikan relasi](API_DOCUMENTATION/45_QUESTION_RELATION_REPAIR.md).
