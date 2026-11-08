# Serah-terima batch 01 — kelas11

Total **504 soal**, pipeline `exercise-2026-10-01`, skill: v1 (504)

## File

| File | Isi |
|---|---|
| `soal_exercise_db.json` | **Master.** Baris tabel `soal`; input validasi dan insert. `cognitive_level`, `cognitive_score`, `confidence_score`, `status` sengaja `null`. |
| `soal_exercise_meta.json` | Info pendamping per `_id` (level target, tipe, acuan, pembahasan, penanda). Bawa bersama master. |
| `per_subbab/*.md`, `*.json` | Turunan untuk koreksi manusia, satu subbab per file (3 level × kuota). Jangan disunting. |

## Prior kesulitan (untuk kalibrasi IRT)

Level easy/medium/hard hanya **perkiraan awal**. Field di meta yang bisa dipakai sebagai prior yang lebih halus:
`level_target`, `cognitive_c` (C1–C6), `jumlah_langkah`, `cognitive_score_target` (600/1000/1400).

Catatan untuk kalibrasi:
- Kunci jawaban **belum diverifikasi pihak independen** (dikerjakan dua kali oleh generator sendiri). Soal berkunci salah/ambigu akan terlihat
  sulit karena banyak dijawab salah: gunakan **daya beda** (point-biserial / parameter *a*) agar soal berdaya beda rendah/negatif masuk
  antrean tinjau manusia, bukan otomatis dijadikan hard.
- Pindahkan level hanya setelah jumlah jawaban per soal cukup, dan beri jeda agar label tidak bolak-balik.
- Hard di sini sering setara medium atas (kesulitan dari penalaran, bukan konsep baru), terutama SD dan SMA.

## Penanda khusus

- `dipaksa_kuota` (0 soal): soal tambahan agar kuota penuh saat bahan tipis; rentan nyaris kembar. Perlu perhatian ekstra.
- `kapasitas_kurang` (5 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMA11U-B1 subbab A hard: 16/20 — 10 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA11U-B2 subbab B hard: 19/20 — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA11U-B2 subbab C hard: 12/20 — 22 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA11U-B2 subbab C medium: 19/20 — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA11U-B3 subbab B hard: 18/20 — 11 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA11U-B1 | A. Fungsi | 20 | 20 | 16 |
| SMA11U-B1 | B. Komposisi Fungsi | 20 | 20 | 20 |
| SMA11U-B1 | C. Fungsi Invers | 20 | 20 | 20 |
| SMA11U-B2 | A. Lingkaran dan Busur Lingkaran | 20 | 20 | 20 |
| SMA11U-B2 | B. Lingkaran dan Garis Singgung | 20 | 20 | 19 |
| SMA11U-B2 | C. Lingkaran dan Tali Busur | 20 | 19 | 12 |
| SMA11U-B3 | A. Diagram Pencar atau Diagram Scatter | 20 | 20 | 20 |
| SMA11U-B3 | B. Regresi Linear | 20 | 20 | 18 |
| SMA11U-B3 | C. Analisis Korelasi | 20 | 20 | 0 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
