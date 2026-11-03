# Auto-Inserter — Dokumentasi

Skrip pemantau otomatis yang berjalan di latar belakang secara kontinu (*continuous file watcher*).
Setiap kali file `validation_results.json` dibuat atau diperbarui di dalam direktori `output/`, skrip akan mem-parse, memetakan data, meng-insert soal baru, dan memperbarui skor kognitif ke MongoDB — **tanpa duplikasi dan tanpa jeda lambat**.

---

## Daftar Isi

- [Fitur Utama](#fitur-utama)
- [Filter Folder 'hasil_validasi'](#filter-folder-hasil_validasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Cara Menghentikan](#cara-menghentikan)
- [Alur Kerja Sistem](#alur-kerja-sistem)
- [Logika Lookup Kelas (In-Memory)](#logika-lookup-kelas-in-memory)
- [Logika Lookup Subbab](#logika-lookup-subbab)
- [Pencegahan Duplikasi & Auto-Update](#pencegahan-duplikasi--auto-update)
- [Indikator Heartbeat (Anti-Stuck)](#indikator-heartbeat-anti-stuck)
- [Konfigurasi](#konfigurasi)

---

## Fitur Utama

1. **Khusus Berkas Resmi (`hasil_validasi`)**:
   Hanya memantau dan memproses file `validation_results.json` yang berada persis di dalam folder `hasil_validasi/`. Seluruh file `validation_results.json` di luar folder tersebut (seperti di folder audit, bundle, operational_balance, backup) diabaikan secara otomatis.
2. **Sinkronisasi Awal Otomatis (*Initial Sync*)**:
   Saat pertama kali dijalankan, skrip langsung memindai 21 berkas resmi yang ada di `output/` dan meng-insert soal-soal yang belum masuk ke database.
3. **Pencegahan Duplikasi Kilat (< 0.05 detik) & Auto-Update**:
   Menggunakan batch query `$in` ke MongoDB Atlas untuk ribuan ID sekaligus. Jika berkas diperbarui oleh LLM dengan skor kognitif baru, skrip otomatis meng-update field tersebut di MongoDB tanpa menduplikasi data.
4. **Lookup Kelas In-Memory**:
   Memuat seluruh pemetaan kelas (14 jenjang) ke RAM saat startup. Pencocokan nama folder kelas ke ObjectId berjalan instan (0 ms).
5. **Indikator Detak (*Heartbeat*)**:
   Setiap 30 detik saat standby, terminal menampilkan status bahwa pemantau tetap aktif berjalan, sehingga Anda tidak perlu khawatir apakah skrip membeku atau macet.

---

## Filter Folder 'hasil_validasi'

Dalam direktori `output/`, terdapat banyak file `validation_results.json` yang dihasilkan dari berbagai proses (misal snapshot audit, operational balance, intermediate pilot bundle).

Skrip `auto_inserter.py` secara ketat memfilter hanya file yang path-nya berada langsung di dalam folder:
```
.../<batch atau jenjang>/hasil_validasi/validation_results.json
```

**Daftar Berkas yang Diproses (Total 21 Berkas):**
- Exercise (7 berkas):
  - `output/exercise/kelas5/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas6/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas7/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas8/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas9/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas10/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas11/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas11_tl/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas12/batch01/hasil_validasi/validation_results.json`
  - `output/exercise/kelas12_tl/batch01/hasil_validasi/validation_results.json`
- Pretest (14 berkas):
  - `output/pretest/kelas1` s.d `kelas12_tl` (`.../hasil_validasi/validation_results.json`)

**Berkas yang Diabaikan (122 Berkas):**
- Seluruh file di `output/pretest/*/operational_balance_v*/*`
- Seluruh file di `output/pretest/*/revalidasi_blind_*/*`
- Seluruh file di `output/pretest/*/rubric_v8_*/*`
- Seluruh file di `output/pretest/*/bundle/*`

---

## Cara Menjalankan

Dari **root proyek** (`assessment_service/`):

### Mode Standar (Rekomendasi)
Memeriksa 21 berkas resmi terlebih dahulu (mengimpor soal yang belum tersimpan / memperbarui skor), lalu lanjut memantau berkas baru secara real-time:
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
│  3. Pindai berkas: hasil_validasi/validation_results  │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│          Tahap 1: Sinkronisasi Awal (Auto)             │
│  - Periksa 21 berkas resmi                             │
│  - Cek $in ke DB (< 0.05 detik/file)                   │
│  - Insert batch soal-soal baru                         │
│  - Update massal skor kognitif jika ada nilai baru     │
│  - Cetak progres ke terminal                           │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│          Tahap 2: Real-time Continuous Watcher         │
│  - Polling folder output/ setiap 5 detik               │
│  - Jika berkas hasil_validasi berubah -> Auto-Sync     │
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

---

## Logika Lookup Subbab

Field `subbab_id` pada JSON berisi nama subbab (string). Skrip mencocokkan nama tersebut dengan peta subbab di memori dan menggantinya dengan `ObjectId` resmi dari MongoDB.

---

## Pencegahan Duplikasi & Auto-Update

- Duplikasi dicegah berdasarkan ID unik soal (`_id`).
- Menggunakan query massal: `Pertanyaan.find({"_id": {"$in": valid_oids}})` per berkas.
- Soal yang belum ada di database akan dimasukkan via `Pertanyaan.insert_many()`.
- **Auto-Update Skor Kognitif**: Jika sebuah soal sudah ada di DB tetapi di JSON baru terisi nilai `cognitive_level`, `cognitive_score`, dan `confidence_score`, skrip otomatis memperbarui field tersebut via bulk write `UpdateOne`.
- **Status Soal**: Seluruh soal yang di-insert secara otomatis dan mutlak berstatus **`active`**.

---

## Indikator Heartbeat (Anti-Stuck)

Jika belum ada berkas baru yang digenerate oleh LLM, terminal akan menampilkan sinyal detak aktif setiap 30 detik:
```text
20:25:00 | INFO | 💓 [Standby] Pemantau aktif, menunggu berkas baru di hasil_validasi/ ...
```

---

## Konfigurasi

Variabel konfigurasi di bagian atas [`scripts/auto_inserter.py`](file:///d:/Wildan%20A/BIG%20DATA/assessment_service/scripts/auto_inserter.py):

| Variabel                 | Nilai Default            | Deskripsi                                    |
|:-------------------------|:-------------------------|:---------------------------------------------|
| `DB_NAME`                | `nolla_experiment`       | Nama database MongoDB                        |
| `WATCH_DIR`              | `output/`                | Direktori yang dipantau                      |
| `TARGET_FILENAME`        | `validation_results.json`| Nama file target yang dicari                 |
| `TARGET_PARENT_DIR`      | `hasil_validasi`         | Hanya proses berkas jika di dalam folder ini |
| `POLL_INTERVAL_SEC`      | `5`                      | Frekuensi pengecekan berkas (detik)          |
| `HEARTBEAT_INTERVAL_SEC` | `30`                     | Frekuensi log status aktif saat siaga (detik)|
