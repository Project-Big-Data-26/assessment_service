# Perbaikan relasi soal dan audit ketersediaan

Implementasi lokal memperbaiki watcher `scripts/auto_inserter.py` dan seeder
manual `app/seed/seed_pretest.py`. Tidak ada perubahan database yang dilakukan
saat implementasi. Rencana production memerlukan katalog ID database tujuan.
Konfigurasi `.env` saat pemeriksaan masih menunjuk URI contoh.

## Bukti masalah

Laporan `Pesan_eror.md` mencantumkan 8.841 soal di 271 subbab. Pemetaan global
nama subbab ke entri terakhir mereproduksi seluruh 271 total subbab tersebut.
Ada 13 nama berulang pada 27 subbab. Ini indikasi kuat benturan pemetaan,
bukan alasan langsung menambah generate pada subbab yang tercatat kosong.

Kode lama juga memaksa semua status menjadi `active`. Sumber validasi sebenarnya
mengandung soal inactive dan draft tanpa label. Status harus dipertahankan saat
import maupun update, bukan diaktifkan hanya karena sudah memiliki label.

## Alur koreksi

1. Cocokkan database tujuan dengan deployment web. Dokumen menyebut
   `db_nolla_staging`; pastikan itu database deployment yang dimaksud.
2. Jalankan audit read-only pada database sebenarnya atau snapshot hasil ekspor.
   Periksa `soal.kelas_id`, `soal.subbab_id`, `subbab.bab_id`, dan `bab.kelas_id`.
3. Jika relasi benar, koreksi query laporan. Jika salah, tinjau rencana koreksi
   berdasarkan ID soal sumber yang tetap.
4. Terapkan rencana tanpa kesalahan pemetaan, dengan cadangan database dan
   menghentikan importer versi lama terlebih dahulu.
5. Audit ulang dan uji kelas/subbab terdampak melalui web, lalu gunakan watcher
   versi baru jika diperlukan.

Laporan menyimpan nilai field sebelum perubahan. Penerapan tidak mengganti ID
atau menghapus soal. ID database tanpa pasangan sumber dilaporkan untuk diperiksa,
bukan diperbaiki dengan tebakan atau dihapus.

## Kontrak latihan untuk backend utama

Route `app/api/routes/exercise.py` dan `pretest.py` di repo ini kosong. Layanan
assessment lokal yang berbeda memakai blueprint/snapshot riset. Aturan latihan
web utama tidak diubah pada layanan riset tersebut.

Backend utama perlu memakai filter yang sama untuk menghitung dan memilih soal:

```text
kelas_id = kelas sesi
subbab_id = subbab sesi (harus berada di bab dan kelas tersebut)
source_kind = exercise
status = active
cognitive_level = level yang dipilih sesi (easy, medium, atau hard)
_id belum digunakan, bila kebijakan sesi melarang pengulangan
```

Batas berlaku **PER LEVEL pada SETIAP SUBBAB**: SD 10, SMP 15, SMA 20.
Setiap subbab SD membutuhkan minimal 10 easy, 10 medium, dan 10 hard;
SMP masing-masing 15; SMA masing-masing 20. Bab dinyatakan cukup hanya jika
seluruh level pada seluruh subbab memenuhi batas.

Contoh SMA: easy 25, medium 19, hard 25 masih kurang 1 medium walaupun totalnya
69. Surplus level lain atau subbab lain tidak menutup kekurangan tersebut.
Pemilihan soal harus mempertahankan filter level sesi. Jangan mengubah label
asli, mengambil level lain, atau diam-diam mengulang soal hanya untuk mengisi kuota.

Ketersediaan setelah pengecualian soal yang pernah dipakai bersifat per siswa.
Inventaris global yang cukup tidak menjamin setiap siswa selalu memiliki soal
baru sebanyak kuota. Notifikasi perlu membedakan kekurangan bank dan habisnya
soal baru untuk siswa tersebut.

Pretest diaudit terpisah. Generator lokal memakai 2 soal per subbab ditambah
prasyarat. Aturan laporan yang mewajibkan ketiga level perlu dicocokkan dengan
algoritme pretest backend utama.

## Inventaris lokal 2026-11-03

Perhitungan menggunakan katalog 271 subbab dari laporan, sumber utama per ID,
dan hanya latihan active berlabel. Tidak menggunakan database production atau
riwayat siswa. Ada 8.332 soal latihan dan 509 soal pretest unik. Latihan active
tersedia 8.095.

Ada **567 dari 813 kombinasi subbab-level** yang belum memenuhi batas.
Seluruh 271 subbab dalam katalog memiliki setidaknya satu level kurang;
seluruh 80 bab karenanya belum memenuhi seluruh persyaratan. Ini tidak berarti
semua level atau soal pada bab tersebut bermasalah.

| Kelompok | Subbab dengan level kurang | Kombinasi level kurang | Kekurangan kuota soal aktif |
|---|---:|---:|---:|
| Kelas 1-4 | 85 | 255 | 2.550 |
| Kelas 5-12, termasuk TL | 186 | 312 | 2.028 |
| Total | 271 | 567 | 4.578 |

Angka kekurangan adalah jumlah tambahan latihan aktif yang dibutuhkan pada
masing-masing level, bukan otomatis jumlah soal yang harus digenerate baru.
Hasil generate yang belum tervalidasi perlu diperiksa terlebih dahulu.
Label validasi tidak boleh diganti hanya untuk mengejar kuota.

Contoh kelas 11 Umum Bab 2, minimum 20 pada setiap level:

| Subbab | Easy | Medium | Hard | Kurang E/M/H |
|---|---:|---:|---:|---|
| Lingkaran dan Busur Lingkaran | 17 | 15 | 12 | 3 / 5 / 8 |
| Lingkaran dan Garis Singgung | 14 | 21 | 22 | 6 / 0 / 0 |
| Lingkaran dan Tali Busur | 12 | 21 | 8 | 8 / 0 / 12 |

Angka 541 pada laporan database memakai aturan per level yang sesuai dengan
klarifikasi pengguna. Angka itu belum sama dengan audit lokal 567 karena
pemetaan kelas/bab, status active, dan pemisahan latihan dari pretest harus
dicocokkan juga. Kedua angka tidak boleh dianggap sebagai hasil query identik.

Laporan lengkap: `runs/question_sync/local_inventory.json` dan
`runs/question_sync/local_inventory.md`. Angka perlu dicek ulang setelah relasi
dan status database diperbaiki; ini tidak menggantikan pemeriksaan deployment.

Lihat [cara menjalankan importer](../AUTO_INSERTER.md).
