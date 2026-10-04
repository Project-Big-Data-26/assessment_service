# Serah-terima batch 01 — kelas5

Total **578 soal**, pipeline `exercise-2026-10-01`, skill: v1 (489), pra-v1 (89)

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

  - SD5-B4 subbab A easy: 9/10 — Subbab A hanya memuat satu konsep (keliling = jumlah panjang sisi). Soal pretest dan latihan Buku Siswa subbab A hampir semuanya bergambar (hanya p0129 1b-1 yang teksnya layak jadi acuan), dan rumus keliling segitiga/segi empat/segi banyak ada di subbab B-E. Soal ke-10 hanya akan nyaris kembar atau di luar materi.
  - SD5-B4 subbab B easy: 9/10 — Subbab B (Siswa p131-p133) sangat tipis: hanya konsep keliling segitiga (jumlah tiga sisi, 3 x sisi untuk sama sisi). Soal Siswa dan pretest B (Ayo Berlatih 1-2, Uji Kompetensi 1) bergantung gambar sehingga tidak layak jadi acuan variasi; 9 soal orisinal tanpa soal nyaris kembar.
  - SD5-B5 subbab B easy: 9/10 — Tidak ada acuan variasi yang layak: soal Buku Siswa dan pretest subbab B (tabel/kotak satuan, kertas berpetak, gambar bangun) semuanya bergantung gambar, dan pretest 5-4 milik subbab D. Maka 9 soal orisinal berdasarkan rumus subbab (persegi panjang, persegi, segitiga, jajar genjang, trapesium, belah ketupat, layang-layang, soal cerita, ukuran hilang); soal ke-10 akan nyaris kembar.
  - SD5-B5 subbab B medium: 9/10 — Tidak ada acuan variasi yang layak: soal Buku Siswa dan pretest subbab B (kertas berpetak, kotak satuan, gambar bangun gabungan) bergantung gambar atau sudah dipakai di easy, dan pretest 5-4 milik subbab D. Maka 9 soal orisinal berbasis rumus subbab; soal ke-10 akan nyaris kembar dengan easy atau di luar materi.
  - SD5-B5 subbab C easy: 9/10 — Subbab C tidak punya soal teks yang layak jadi acuan variasi: semua soal pretest C (Uji Kompetensi 3 dan 4, dan 1-2 di subbab lain) dan Uji Kompetensi Siswa p178 bergambar tanpa ukuran terbaca di teks, Eksplorasi 5.3 berisi isian gambar. Maka 9 soal semuanya orisinal (porsi variasi 0), bukan dilabeli variasi demi porsi; soal ke-10 akan nyaris kembar (pola bagian + bagian).
  - SD5-B5 subbab C medium: 9/10 — Tidak ada acuan variasi yang layak di subbab C (soal pretest dan Uji Kompetensi p178 bergambar tanpa ukuran di teks), jadi 9 soal semuanya orisinal; soal ke-10 akan nyaris kembar pola easy/medium; porsi variasi 0 dinyatakan, tidak dilabeli demi porsi.
  - SD5-B5 subbab D easy: 9/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) dengan 2 soal pretest; acuan variasi teks hanya 2 sehingga maks 4 variasi, materi tidak cukup untuk 10 soal tanpa nyaris kembar.
  - SD5-B5 subbab D hard: 7/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) tentang keliling dan luas persegi panjang/persegi; acuan variasi sudah habis di easy dan medium. Hanya 7 soal penalaran yang layak tanpa nyaris kembar dengan easy/medium atau keluar materi.
  - SD5-B5 subbab D medium: 9/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) dengan 2 soal pretest; acuan variasi teks hanya 2 dan sudah dipakai easy. Materi (keliling dan luas persegi panjang/persegi) tidak cukup untuk 10 soal medium tanpa nyaris kembar dengan easy.
  - SD5-B9 subbab B hard: 9/10 — Acuan pretest subbab B habis di easy/medium; soal ke-10 hanya akan nyaris kembar dengan easy/medium atau keluar materi (pembulatan, kelipatan).

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SD5-B1 | A. Membaca dan Menulis Bilangan Cacah Sampai 100.000 dan Menentukan Nilai Tempatnya | 10 | 10 | 10 |
| SD5-B1 | B. Membandingkan dan Mengurutkan Bilangan Cacah Sampai 100.000 | 10 | 10 | 10 |
| SD5-B1 | C. Komposisi dan Dekomposisi Bilangan Sampai 100.000 | 10 | 10 | 10 |
| SD5-B1 | D. Operasi Hitung pada Bilangan Cacah Sampai 100.000 | 10 | 10 | 10 |
| SD5-B2 | A. Kelipatan | 10 | 10 | 10 |
| SD5-B2 | B. Kelipatan Persekutuan | 10 | 10 | 10 |
| SD5-B2 | C. Faktor | 10 | 10 | 10 |
| SD5-B2 | D. Faktor Persekutuan | 10 | 10 | 10 |
| SD5-B2 | E. Menentukan KPK dan FPB dengan Menggunakan Faktor Prima | 10 | 10 | 10 |
| SD5-B3 | A. Membandingkan dan Mengurutkan Pecahan | 10 | 10 | 10 |
| SD5-B3 | B. Penjumlahan Bilangan Pecahan | 10 | 10 | 10 |
| SD5-B3 | C. Pengurangan Bilangan Pecahan | 10 | 10 | 10 |
| SD5-B4 | A. Apakah Keliling Bangun Datar Itu? | 9 | 0 | 0 |
| SD5-B4 | B. Keliling Segitiga | 9 | 0 | 0 |
| SD5-B5 | A. Konsep Luas Daerah Bangun Datar | 10 | 10 | 10 |
| SD5-B5 | B. Luas Daerah Bangun Datar | 9 | 9 | 10 |
| SD5-B5 | C. Luas Daerah Bangun Gabungan | 9 | 9 | 10 |
| SD5-B5 | D. Hubungan Keliling dan Luas Daerah Bangun Datar | 9 | 9 | 7 |
| SD5-B9 | A. Membaca dan Menulis Bilangan Cacah Sampai 1.000.000 dan Menentukan Nilai Tempatnya | 10 | 10 | 10 |
| SD5-B9 | B. Mengurutkan dan Membandingkan Bilangan Sampai 1.000.000 | 10 | 10 | 9 |
| SD5-B9 | C. Komposisi dan Dekomposisi Bilangan Sampai 1.000.000 | 10 | 10 | 10 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
