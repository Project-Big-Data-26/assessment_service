# Serah-terima batch 01 — kelas7

Total **389 soal**, pipeline `exercise-2026-10-01`, skill: v1 (389)

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
- `kapasitas_kurang` (4 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMP7-B1 subbab A hard: 10/15 — Materi A tipis (p27-34: garis bilangan, bilangan cacah/asli/bulat, tanda positif-negatif, perbandingan dan urutan). Soal penalaran C5-C6 yang sah tanpa operasi hitung (subbab B) hanya cukup untuk 10 soal; sisanya akan nyaris kembar dengan easy/medium atau keluar dari materi subbab.
  - SMP7-B2 subbab A hard: 11/15 — Materi subbab A tipis (definisi a/b, desimal terbatas/berulang, irasional, real). Acuan pretest A sudah habis dan Tabel 2.4 sudah dipakai di easy/medium; hanya 11 soal penalaran (contoh penyangkal, temukan kesalahan, evaluasi klaim, syarat ganda, perancangan) yang layak tanpa nyaris kembar dan tanpa materi di luar subbab.
  - SMP7-B2 subbab B hard: 11/15 — Materi subbab B sempit (perbandingan pecahan/desimal, urutan, estimasi, penyamaan penyebut) dan sudah dipakai easy/medium; soal hard berbasis penalaran yang layak dan tidak nyaris kembar hanya 11.
  - SMP7-B4 subbab A hard: 12/15 — Materi subbab A tipis (istilah variabel, suku, koefisien, konstanta, substitusi). Acuan pretest habis di easy/medium, sisa acuan siswa hanya 3b (terlalu mudah) dan Ayo Berpikir Kritis 1a/2a (2a ambigu); soal bergambar tidak dapat dipakai. Penalaran hard di luar 12 soal ini akan menjadi nyaris kembar atau di luar materi.

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMP7-B1 | A. Memahami Bilangan Bulat | 15 | 15 | 10 |
| SMP7-B1 | B. Operasi Hitung Bilangan Bulat | 15 | 15 | 15 |
| SMP7-B1 | C. Faktor Bilangan Bulat | 15 | 15 | 15 |
| SMP7-B2 | A. Di Antara Dua Bilangan Bulat | 15 | 15 | 11 |
| SMP7-B2 | B. Membandingkan Bilangan Rasional | 15 | 15 | 11 |
| SMP7-B2 | C. Operasi Hitung Bilangan Rasional | 15 | 15 | 15 |
| SMP7-B4 | A. Unsur-Unsur Bentuk Aljabar | 15 | 15 | 12 |
| SMP7-B4 | B. Sifat-Sifat dan Operasi Aljabar | 15 | 15 | 15 |
| SMP7-B4 | C. Pemodelan dengan Bentuk Aljabar | 15 | 15 | 15 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
