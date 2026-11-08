# Serah-terima batch 01 — kelas12_tl

Total **1060 soal**, pipeline `exercise-2026-10-01`, skill: v1 (1060)

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
- `kapasitas_kurang` (10 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMA12L-B1 subbab C hard: 19/20 — 7 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B1 subbab D hard: 19/20 — 5 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B3 subbab A hard: 18/20 — 11 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B3 subbab B medium: 19/20 — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B3 subbab C hard: 17/20 — 5 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B3 subbab C medium: 16/20 — 6 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B4 subbab A hard: 17/20 — 9 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B4 subbab B hard: 18/20 — 12 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B4 subbab D hard: 19/20 — 9 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
  - SMA12L-B4 subbab F hard: 18/20 — 10 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA12L-B1 | A. Lingkaran | 20 | 20 | 20 |
| SMA12L-B1 | B. Elips | 20 | 20 | 20 |
| SMA12L-B1 | C. Kedudukan Titik dan Garis terhadap Lingkaran | 20 | 20 | 19 |
| SMA12L-B1 | D. Persamaan Garis Singgung Lingkaran | 20 | 20 | 19 |
| SMA12L-B2 | A. Definisi Turunan Fungsi | 20 | 20 | 20 |
| SMA12L-B2 | B. Sifat-Sifat Turunan Fungsi | 20 | 20 | 20 |
| SMA12L-B2 | C. Aplikasi Turunan Fungsi | 20 | 20 | 20 |
| SMA12L-B2 | D. Aplikasi Turunan Fungsi di Berbagai Bidang Ilmu | 20 | 20 | 20 |
| SMA12L-B3 | A. Integral Tak Tentu | 20 | 20 | 18 |
| SMA12L-B3 | B. Integral Tentu | 20 | 19 | 20 |
| SMA12L-B3 | C. Penerapan Integral | 20 | 16 | 17 |
| SMA12L-B4 | A. Variabel Acak | 20 | 20 | 17 |
| SMA12L-B4 | B. Variabel Acak Diskret | 20 | 20 | 18 |
| SMA12L-B4 | C. Variabel Acak Kontinu | 20 | 20 | 20 |
| SMA12L-B4 | D. Fungsi Peluang | 20 | 20 | 19 |
| SMA12L-B4 | E. Fungsi Densitas Peluang | 20 | 20 | 20 |
| SMA12L-B4 | F. Distribusi Binomial | 20 | 20 | 18 |
| SMA12L-B4 | G. Distribusi Normal | 20 | 20 | 20 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
