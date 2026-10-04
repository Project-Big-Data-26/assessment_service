# Serah-terima batch 01 — kelas7

Total **617 soal**, pipeline `exercise-2026-10-01`, skill: v1 (617)

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
- `kapasitas_kurang` (12 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMP7-B1 subbab A hard: 10/15 — Materi A tipis (p27-34: garis bilangan, bilangan cacah/asli/bulat, tanda positif-negatif, perbandingan dan urutan). Soal penalaran C5-C6 yang sah tanpa operasi hitung (subbab B) hanya cukup untuk 10 soal; sisanya akan nyaris kembar dengan easy/medium atau keluar dari materi subbab.
  - SMP7-B2 subbab A hard: 11/15 — Materi subbab A tipis (definisi a/b, desimal terbatas/berulang, irasional, real). Acuan pretest A sudah habis dan Tabel 2.4 sudah dipakai di easy/medium; hanya 11 soal penalaran (contoh penyangkal, temukan kesalahan, evaluasi klaim, syarat ganda, perancangan) yang layak tanpa nyaris kembar dan tanpa materi di luar subbab.
  - SMP7-B2 subbab B hard: 11/15 — Materi subbab B sempit (perbandingan pecahan/desimal, urutan, estimasi, penyamaan penyebut) dan sudah dipakai easy/medium; soal hard berbasis penalaran yang layak dan tidak nyaris kembar hanya 11.
  - SMP7-B4 subbab A hard: 12/15 — Materi subbab A tipis (istilah variabel, suku, koefisien, konstanta, substitusi). Acuan pretest habis di easy/medium, sisa acuan siswa hanya 3b (terlalu mudah) dan Ayo Berpikir Kritis 1a/2a (2a ambigu); soal bergambar tidak dapat dipakai. Penalaran hard di luar 12 soal ini akan menjadi nyaris kembar atau di luar materi.
  - SMP7-B5 subbab A easy: 12/15 — Subbab A tipis dan hampir seluruh soal pretest/Buku Siswa-nya bergantung gambar (jajargenjang, persimpangan jalan, Tabel 5.2/5.3 bergambar); acuan variasi yang layak dan bisa ditulis penuh sebagai teks hanya sedikit (5-1-2, Ayo Berpikir Kritis, 5-1-3a), sehingga porsi variasi 60% hanya tercapai pada 12 soal; tambahan soal orisinal akan nyaris kembar atau membuat porsi variasi tidak terpenuhi.
  - SMP7-B5 subbab A hard: 6/15 — Subbab A tipis dan sebagian besar bahan bergantung gambar. Setelah easy (12) dan medium (10) memakai hampir semua pola hubungan sudut yang konfigurasinya dapat ditulis teks, hanya 6 soal hard yang benar-benar bernalar (evaluasi klaim, temukan kesalahan, sistem dua persamaan, banyak nilai x, contoh penyangkal, gabungan segitiga dengan garis sejajar) tanpa nyaris kembar; soal tambahan hanya mengulang pola atau berupa medium dengan angka lain.
  - SMP7-B5 subbab A medium: 10/15 — Subbab A tipis: hampir semua soal pretest/Buku Siswa bergantung gambar (Tabel 5.2/5.3, Eksplorasi lidi/jalan, Latihan 5.1 no.1 dan 3b) dan acuan teks (5-1-2, Ayo Berpikir Kritis, 5-1-3a) sudah dipakai di easy. Soal medium dibatasi pada hubungan sudut yang konfigurasinya dapat ditulis penuh sebagai teks; 10 soal tanpa nyaris kembar dengan easy, soal tambahan akan mengulang pola.
  - SMP7-B5 subbab B easy: 10/15 — Subbab B (Arti Kesebangunan, p0192-p0197) tipis: hanya definisi sebangun, pas foto dan perbandingan sama/beda. Semua soal Latihan 5.2 dan pretest B (selain Eksplorasi 5.2 no.2 sama/beda) bergantung gambar sehingga tidak dapat jadi acuan variasi; acuan variasi hanya 2 (maks 4 variasi), sisanya orisinal dari materi tipis tanpa soal nyaris kembar.
  - SMP7-B5 subbab B hard: 8/15 — Subbab B (Arti Kesebangunan) hanya memuat definisi sebangun (sudut bersesuaian sama besar dan sisi sebanding), pas foto, serta perbandingan keliling/luas pada pembesaran-pengecilan. Semua soal Latihan 5.2 dan pretest B bergantung gambar atau sudah dipakai easy/medium, sehingga hard hanya berisi 8 soal orisinal berbasis penalaran (contoh penyangkal, syarat dengan ekspresi aljabar, faktor gabungan, perancangan ukuran). Soal tambahan akan menjadi kembar dengan easy/medium atau keluar dari materi subbab (kesebangunan segitiga ada di subbab C).
  - SMP7-B5 subbab B medium: 12/15 — Subbab B (Arti Kesebangunan, p0192-p0197) tipis: hanya definisi sebangun, pas foto, dan perbandingan sama/beda saat diperbesar. Soal Latihan 5.2 dan pretest B (kecuali Eksplorasi 5.2 no.2 yang sudah dipakai easy dan tanpa angka) bergantung gambar sehingga tidak dapat jadi acuan variasi; medium dibuat 8 soal orisinal (syarat sebangun, sisi/sudut tak diketahui, skala model, klaim persegi/persegi panjang) tanpa soal nyaris kembar.
  - SMP7-B5 subbab C hard: 7/15 — Hampir semua soal buku dan pretest subbab C bergantung gambar dan acuan variasi sudah habis di easy dan medium; hard orisinal hanya layak untuk soal penalaran (evaluasi klaim, penyangkal, kesalahan pasangan sisi, dua bayangan, rancangan ukuran) yang bisa dinyatakan penuh sebagai teks. Soal tambahan akan nyaris kembar dengan easy/medium (x aljabar pada sisi atau sudut, luas dan keliling) atau memerlukan syarat sisi-sudut-sisi yang tidak ada di buku.
  - SMP7-B5 subbab C medium: 13/15 — Hampir semua soal buku dan pretest subbab C bergantung gambar (Latihan 5.3 no.1, 3a-b, UK 1/2/4 dan lainnya) sehingga tidak bisa ditulis penuh sebagai teks; acuan variasi yang layak tinggal pretest 4b, 4d, 4e, 3d dan UK-3, sedangkan 2b, 4a, 4c sudah dipakai easy. Soal orisinal tambahan akan nyaris kembar dengan soal lain atau di luar materi (luas dua segitiga sebangun, SsdS).

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMP7-B1 | A. Memahami Bilangan Bulat | 15 | 15 | 10 |
| SMP7-B1 | B. Operasi Hitung Bilangan Bulat | 15 | 15 | 15 |
| SMP7-B1 | C. Faktor Bilangan Bulat | 15 | 15 | 15 |
| SMP7-B2 | A. Di Antara Dua Bilangan Bulat | 15 | 15 | 11 |
| SMP7-B2 | B. Membandingkan Bilangan Rasional | 15 | 15 | 11 |
| SMP7-B2 | C. Operasi Hitung Bilangan Rasional | 15 | 15 | 15 |
| SMP7-B3 | A. Konsep Rasio | 15 | 15 | 15 |
| SMP7-B3 | B. Skala | 15 | 15 | 15 |
| SMP7-B3 | C. Laju Perubahan Satuan | 15 | 15 | 15 |
| SMP7-B4 | A. Unsur-Unsur Bentuk Aljabar | 15 | 15 | 12 |
| SMP7-B4 | B. Sifat-Sifat dan Operasi Aljabar | 15 | 15 | 15 |
| SMP7-B4 | C. Pemodelan dengan Bentuk Aljabar | 15 | 15 | 15 |
| SMP7-B5 | A. Hubungan Antar Sudut | 12 | 10 | 6 |
| SMP7-B5 | B. Arti Kesebangunan | 10 | 12 | 8 |
| SMP7-B5 | C. Kesebangunan pada Segitiga | 15 | 13 | 7 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
