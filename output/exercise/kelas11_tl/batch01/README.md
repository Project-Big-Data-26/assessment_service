# Serah-terima batch 01 — kelas11_tl

Total **264 soal**, pipeline `exercise-2026-10-01`, skill: v1 (264)

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

  - SMA11L-B1 subbab A hard: 10/20 — Subbab A (Jenis-Jenis Matriks, sekitar 8 halaman) hanya memuat definisi jenis matriks, transpos, dan kesamaan; easy+medium sudah memakai 40 soal dan 8 jenis. Penalaran sifat yang tersisa (klaim, penyangkal, parameter dua jenis, pencacahan matriks) hanya cukup untuk sekitar 10 soal hard tanpa kembar; sisanya akan menjadi soal hitung atau di luar materi subbab.
  - SMA11L-B1 subbab B hard: 10/20 — Subbab B hanya ~2 halaman (Definisi 1.1: ordo sama dan elemen seletak sama). Easy dan medium sudah memakai 40 soal; hard yang bermakna hanya penalaran sifat kesamaan (evaluasi klaim, contoh penyangkal, kesalahan ordo, parameter, pencacahan, rantai). Menambah ke 20 akan memunculkan soal nyaris kembar atau materi di luar subbab.
  - SMA11L-B1 subbab C hard: 12/20 — Materi C (penjumlahan/pengurangan matriks, lawan, sifat 1.1) sempit dan 40 soal easy+medium sudah menghabiskan hitungan dan persamaan matriks; hard bermakna hanya lewat penalaran (evaluasi klaim, penyangkal, parameter, temukan kesalahan) yang layak 12 soal tanpa nyaris kembar. Acuan siswa terbaca habis sehingga semua soal orisinal (hard tanpa batas bawah variasi).
  - SMA11L-B1 subbab D hard: 18/20 — Hard subbab D bermakna hanya lewat penalaran sifat perkalian matriks (klaim, penyangkal, parameter, pangkat, perancangan, pengelompokan). Setelah easy dan medium memakai 40 soal dan acuan siswa/pretest habis, bahan penalaran orisinal yang tidak nyaris kembar hanya cukup untuk sekitar belasan soal, bukan 20.
  - SMA11L-B1 subbab E hard: 14/20 — Hard bermakna hanya lewat penalaran sifat |AB|=|A||B|, |kA|, invers, adjoin, syarat Cramer, parameter dua syarat, dan contoh penyangkal; materi inti (hitung determinan/invers/SPL) sudah habis terpakai di easy dan medium (40 soal) dan bentuk lain akan nyaris kembar atau di luar subbab.

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA11L-B1 | A. Jenis-Jenis Matriks | 20 | 20 | 10 |
| SMA11L-B1 | B. Kesamaan Dua Matriks | 20 | 20 | 10 |
| SMA11L-B1 | C. Penjumlahan dan Pengurangan Antarmatriks | 20 | 20 | 12 |
| SMA11L-B1 | D. Perkalian Matriks | 20 | 20 | 18 |
| SMA11L-B1 | E. Determinan Matriks dan Invers Matriks | 20 | 20 | 14 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
