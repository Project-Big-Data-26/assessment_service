# Serah-terima batch 01 — kelas12

Total **234 soal**, pipeline `exercise-2026-10-01`, skill: v1 (234)

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
- `kapasitas_kurang` (1 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMA12U-B3 subbab A hard: 14/20 — Subbab A (Aturan Pengisian Tempat) hanya memuat aturan penjumlahan, perkalian, dan faktorial; easy dan medium sudah memakai 40 soal dan menghabiskan sudut bilangan bersyarat, komplemen, data lintas kelompok, dan faktorial. Soal hard yang layak berupa evaluasi penyelesaian, contoh penyangkal, urutan pengisian, perbandingan perubahan, perancangan parameter, dan kasus bersyarat berjenjang: sekitar 14 soal tanpa kembar atau materi di luar subbab (permutasi/kombinasi ada di subbab B dan C).

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA12U-B3 | A. Aturan Pengisian Tempat | 20 | 20 | 14 |
| SMA12U-B3 | B. Permutasi | 20 | 20 | 20 |
| SMA12U-B3 | C. Kombinasi | 20 | 20 | 20 |
| SMA12U-B3 | D. Penerapan Permutasi dan Kombinasi | 20 | 20 | 20 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
