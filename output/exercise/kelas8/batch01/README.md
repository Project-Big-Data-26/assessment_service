# Serah-terima batch 01 — kelas8

Total **538 soal**, pipeline `exercise-2026-10-01`, skill: v1 (538)

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
- `kapasitas_kurang` (2 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMP8-B1 subbab C hard: 14/15 — Materi subbab C sempit (syarat bentuk baku, konversi baku-biasa, operasi baku); setelah soal easy dan medium memakai semua acuan siswa/pretest yang layak, hanya sekitar 14 soal penalaran yang tidak nyaris kembar. Soal berat Bumi (salah cetak) dan flashdisk 2^10 B (konsep keliru) sengaja tidak dipakai.
  - SMP8-B4 subbab C hard: 14/15 — Materi subbab C pengayaan dan sempit (definisi, n!, fungsi sebagai korespondensi); bahan acuan dan pola penalaran habis di easy-medium, sehingga hanya soal penalaran yang layak yang ditulis tanpa soal nyaris kembar.

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMP8-B1 | A. Bilangan Berpangkat Bulat | 15 | 15 | 15 |
| SMP8-B1 | B. Bilangan Bentuk Akar | 15 | 15 | 15 |
| SMP8-B1 | C. Penulisan Bentuk Baku | 15 | 15 | 14 |
| SMP8-B3 | A. Memahami Konsep Persamaan Linier Satu Variabel | 15 | 15 | 15 |
| SMP8-B3 | B. Menyelesaikan Persamaan Linier Satu Variabel | 15 | 15 | 15 |
| SMP8-B3 | C. Menemukan Konsep Pertidaksamaan Linier Satu Variabel | 15 | 15 | 15 |
| SMP8-B3 | D. Menyelesaikan Masalah terkait Pertidaksamaan Linier Satu Variabel | 15 | 15 | 15 |
| SMP8-B4 | A. Memahami Relasi | 15 | 15 | 15 |
| SMP8-B4 | B. Memahami Fungsi | 15 | 15 | 15 |
| SMP8-B4 | C. Korespondensi Satu-satu (Pengayaan) | 15 | 15 | 14 |
| SMP8-B6 | A. Pemusatan Data | 15 | 15 | 15 |
| SMP8-B6 | B. Penyebaran Data | 15 | 15 | 15 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
