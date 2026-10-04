# Serah-terima batch 01 — kelas5

Total **89 soal**, pipeline `exercise-2026-10-01`, skill: pra-v1 (89)

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

  - SD5-B9 subbab B hard: 9/10 — Acuan pretest subbab B habis di easy/medium; soal ke-10 hanya akan nyaris kembar dengan easy/medium atau keluar materi (pembulatan, kelipatan).

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SD5-B9 | A. Membaca dan Menulis Bilangan Cacah Sampai 1.000.000 dan Menentukan Nilai Tempatnya | 10 | 10 | 10 |
| SD5-B9 | B. Mengurutkan dan Membandingkan Bilangan Sampai 1.000.000 | 10 | 10 | 9 |
| SD5-B9 | C. Komposisi dan Dekomposisi Bilangan Sampai 1.000.000 | 10 | 10 | 10 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
