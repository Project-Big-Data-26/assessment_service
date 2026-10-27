# Auto-Inserter — Dokumentasi

Skrip pemantau otomatis yang berjalan di latar belakang secara kontinu (*continuous file watcher*).
Setiap kali file `validation_results.json` dibuat atau diperbarui di dalam direktori `output/`, skrip akan mem-parse, memetakan data, dan meng-insert soal baru ke MongoDB — **tanpa duplikasi dan tanpa jeda lambat**.

---

## Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Cara Menjalankan](#cara-menjalankan)
- [Cara Menghentikan](#cara-menghentikan)
- [Alur Kerja Sistem](#alur-kerja-sistem)
- [Logika Lookup Kelas (In-Memory)](#logika-lookup-kelas-in-memory)
- [Logika Lookup Subbab](#logika-lookup-subbab)
- [Pencegahan Duplikasi Super Cepat](#pencegahan-duplikasi-super-cepat)
- [Indikator Heartbeat (Anti-Stuck)](#indikator-heartbeat-anti-stuck)
- [Konfigurasi](#konfigurasi)

---

## Fitur Utama

1. **Sinkronisasi Awal Otomatis (*Initial Sync*)**:
   Saat pertama kali dijalankan, skrip langsung memindai seluruh file `validation_results.json` yang sudah ada di folder `output/` dan meng-insert soal-soal yang belum masuk ke database.
2. **Pencegahan Duplikasi Kilat (< 0.05 detik)**:
   Menggunakan batch query `$in` ke MongoDB Atlas untuk ribuan ID sekaligus. Tidak ada serial `find_one` berulang (N+1 query) yang membuat terminal macet berjam-jam.
3. **Lookup Kelas In-Memory**:
   Memuat seluruh pemetaan kelas (14 jenjang) ke RAM saat startup. Pencocokan nama folder kelas ke ObjectId berjalan instan (0 ms).
4. **Indikator Detak (*Heartbeat*)**:
   Setiap 30 detik saat standby, terminal menampilkan status bahwa pemantau tetap aktif berjalan, sehingga Anda tidak perlu khawatir apakah skrip membeku atau macet.

---

## Cara Menjalankan

Dari **root proyek** (`assessment_service/`):

### Mode Standar (Rekomendasi)
Memeriksa file yang sudah ada terlebih dahulu (mengimpor soal yang belum tersimpan), lalu lanjut memantau file baru secara real-time:
```bash
python scripts/auto_inserter.py
```

### Mode Watch-Only
Lewati sinkronisasi berkas lama, hanya menunggu dan memproses berkas baru yang dibuat/diperbarui setelah skrip berjalan:
```bash
python scripts/auto_inserter.py --watch-only
```

---

## Cara Menghentikan

Tekan **Ctrl+C** di terminal kapan saja. Skrip akan berhenti dengan aman (*graceful shutdown*).

---

## Alur Kerja Sistem

```
┌────────────────────────────────────────────────────────┐
│                        Startup                         │
│  1. Sambungkan ke MongoDB Atlas                        │
│  2. Muat pemetaan Kelas & Subbab ke RAM (In-Memory)   │
│  3. Pindai seluruh file validation_results.json        │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│          Tahap 1: Sinkronisasi Awal (Auto)             │
│  - Periksa seluruh file existing                       │
│  - Ambil semua _id dan cek $in ke DB (0.05 detik/file) │
│  - Insert batch soal-soal yang belum ada di DB         │
│  - Cetak progres persentase ke terminal                │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│          Tahap 2: Real-time Continuous Watcher         │
│  - Polling folder output/ setiap 5 detik               │
│  - Jika ada file baru/diperbarui -> Auto-Import        │
│  - Jika standby -> Cetak Heartbeat tiap 30 detik       │
└────────────────────────────────────────────────────────┘
```

---

## Logika Lookup Kelas (In-Memory)

Kelas ditentukan secara **dinamis** dari nama folder dalam path file:

| Folder Path                 | Nomor Kelas | Kriteria di DB MongoDB          | Target Kelas                    |
|:----------------------------|:-----------:|:--------------------------------|:--------------------------------|
| `kelas1` s.d `kelas9`       | 1 s.d 9     | `nomor_kelas == X`              | Contoh: "Kelas 5 SD"            |
| `kelas10`                   | 10          | `nomor_kelas == 10`             | "Kelas 10 SMA"                  |
| `kelas11` atau `kelas12`    | 11 / 12     | `nomor_kelas == X` & `Umum`     | Contoh: "Kelas 11 SMA (Umum)"   |
| `kelas11_tl` / `kelas12_tl` | 11 / 12     | `nomor_kelas == X` & `Lanjut`   | Contoh: "Kelas 11 SMA (Lanjut)" |

*Catatan: Seluruh 14 dokumen kelas dimuat langsung saat inisialisasi, sehingga resolusi kelas berlangsung di memori tanpa membebani kuota jaringan database.*

---

## Logika Lookup Subbab

Field `subbab_id` pada JSON berisi nama subbab (string). Skrip mencocokkan nama tersebut dengan peta subbab di memori dan menggantinya dengan `ObjectId` resmi dari MongoDB.

---

## Pencegahan Duplikasi Super Cepat

- Duplikasi dicegah berdasarkan ID unik soal (`_id`).
- Menggunakan query massal: `Pertanyaan.find({"_id": {"$in": valid_oids}})` per berkas.
- Soal yang sudah ada di database akan dilewati secara otomatis (`skipped`).
- Hanya soal yang benar-benar baru yang dimasukkan via `Pertanyaan.insert_many()`.
- **Status Soal**: Seluruh soal yang di-insert secara otomatis dan mutlak berstatus **`active`**.

---

## Indikator Heartbeat (Anti-Stuck)

Jika belum ada berkas baru yang digenerate oleh LLM, terminal akan menampilkan sinyal detak aktif setiap 30 detik:
```text
20:25:00 | INFO    | 💓 [Standby] Pemantau aktif, menunggu berkas baru / pembaruan di output/ ...
```
Ini memastikan bahwa proses tidak macet / freeze, melainkan sedang dalam status siaga mendengarkan event berkas baru.

---

## Konfigurasi

Variabel konfigurasi di bagian atas [`scripts/auto_inserter.py`](file:///d:/Wildan%20A/BIG%20DATA/assessment_service/scripts/auto_inserter.py):

| Variabel                 | Nilai Default       | Deskripsi                                    |
|:-------------------------|:--------------------|:---------------------------------------------|
| `DB_NAME`                | `math_learning_db`  | Nama database MongoDB                        |
| `WATCH_DIR`              | `output/`           | Direktori yang dipantau                      |
| `TARGET_FILENAME`        | `validation_results.json` | Nama file target yang dicari           |
| `POLL_INTERVAL_SEC`      | `5`                 | Frekuensi pengecekan berkas (detik)          |
| `HEARTBEAT_INTERVAL_SEC` | `30`                | Frekuensi log status aktif saat siaga (detik)|
