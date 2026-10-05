# Serah-terima batch 01 — kelas10

Total **1037 soal**, pipeline `exercise-2026-10-01`, skill: v1 (935), pra-v1 (102)

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
- `kapasitas_kurang` (16 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMA10-B1 subbab B hard: 19/20 — Subbab B (Sifat-Sifat Eksponen, p23-p26) hanya memuat 7 sifat dan acuan siswa sudah habis; hard dibatasi pada penalaran (klaim, contoh penyangkal, ekspresi bersyarat, parameter, perancangan). Sisa soal akan nyaris kembar dengan easy/medium, sehingga hanya 19 soal yang layak ditulis.
  - SMA10-B1 subbab C hard: 16/20 — Bahan acuan siswa subbab C habis di easy/medium (13 jenis medium sudah memakai hampir semua konsep: fungsi dari data, persentase, waktu target, parameter, tafsir). Hard hanya mencakup penalaran evaluasi klaim, penyangkal, parameter ganda, perbandingan model, dan perancangan; sisanya akan nyaris kembar dengan medium atau di luar materi (transformasi grafik, grafik).
  - SMA10-B1 subbab D hard: 7/20 — Subbab D hanya p37-p39 dan easy+medium sudah memakai 32 soal dengan semua acuan siswa/pretest habis; akar bersarang, pangkat nol, dan notasi ilmiah di luar subbab D. Hard hanya memuat soal penalaran orisinal (evaluasi klaim, kesalahan rasionalisasi, perbandingan, parameter, perancangan) yang tidak kembar dengan easy/medium; sisanya akan menjadi nyaris kembar.
  - SMA10-B1 subbab D medium: 16/20 — Subbab D hanya p37-p39; acuan siswa/pretest sudah dipakai easy (pretest 24-1b, 24-2b, Contoh 6, Latihan 2.4 no.2a dan 2c). Acuan yang tersisa: Latihan 2.4 no.1a/1c (2 variasi masing-masing), pretest 2b dan Latihan 2.4 no.2a (variasi tingkat medium, 2 masing-masing), ditambah soal orisinal; materi di luar subbab (akar bersarang, pangkat nol, notasi ilmiah) dan kembar easy dihindari sehingga hanya 16 soal layak.
  - SMA10-B2 subbab A hard: 17/20 — Acuan siswa subbab A (p53-p66) nyaris habis di easy/medium dan materi hanya barisan aritmetika dan geometri (rumus Un, beda, rasio); 17 soal hard orisinal yang berbeda penalaran (klaim, penyangkal, syarat jumlah/hasil kali, rancang, banding) sudah layak; tambahan akan nyaris kembar dengan medium.
  - SMA10-B2 subbab B hard: 15/20 — Acuan siswa bersih di p66-p80 sudah dipakai easy/medium (sisanya dibuang karena ambigu atau rusak); materi hanya deret aritmetika, geometri, dan tak hingga tanpa sigma. Hard bermakna hanya lewat penalaran (klaim, penyangkal, parameter, perbandingan, perancangan), hanya sekitar 15 soal yang tidak nyaris kembar dengan easy/medium; tidak dipaksa sampai 20.
  - SMA10-B2 subbab C easy: 15/20 — Subbab C (Bunga) hanya p80-p83 (4 halaman): 2 definisi, 2 eksplorasi tabel, Latihan 2.6. Soal yang layak dan tidak nyaris kembar tinggal 15; Latihan 2.6 no.3-4 (cicilan) bernilai 3+ langkah (medium).
  - SMA10-B2 subbab C hard: 7/20 — Subbab C (Bunga) hanya p80-p83 dan hanya berisi bunga tunggal/majemuk dasar serta cicilan Latihan 2.6. Hard bermakna hanya lewat penalaran (klaim tunggal vs majemuk, titik impas, suku bunga dari dua kondisi, perancangan pokok); kombinasi lain akan nyaris kembar dengan easy/medium atau di luar materi (tabungan berkala, anuitas, tabel Eksplorasi 2.8 salah cetak). Hanya 7 soal layak, setara medium atas.
  - SMA10-B2 subbab C medium: 19/20 — Subbab C (Bunga) hanya p80-p83 (4 halaman: 2 definisi, 2 eksplorasi, Latihan 2.6). Acuan siswa/pretest tersisa setelah easy hanya Latihan 2.6 no.2b/2d/3/4 dan kalimat Angga; tabel Eksplorasi 2.8 salah cetak (50%) tidak dipakai; rumus nilai majemuk tidak ada di buku. Soal lain akan nyaris kembar dengan easy atau di luar materi (tabungan berkala/anuitas), sehingga hanya 19 soal yang layak.
  - SMA10-B4 subbab A hard: 12/20 — Kapasitas aktual sekitar 12-14 soal; sisanya hampir pasti kembar medium (hitung SPLTV, tafsir banyak solusi) atau di luar materi subbab A.
  - SMA10-B4 subbab B hard: 10/20 — Materi subbab B hanya menguji titik, tanda/nilai batas, pemodelan dan irisan daerah; soal hard tanpa grafik selain 10 ini nyaris kembar medium atau bergantung program linear di luar subbab.
  - SMA10-B6 subbab A easy: 15/20 — Subbab A (p197-p208) tipis dan hampir semua soal bukunya berupa grafik atau tabel gambar; acuan siswa/pretest bertekstual dengan jawaban pasti hanya beberapa. Soal tambahan akan nyaris kembar atau bergantung gambar.
  - SMA10-B6 subbab A hard: 11/20 — Subbab A (p197-p208) tipis dan hampir semua soal bukunya bergambar; acuan siswa tekstual sudah habis di easy/medium, sehingga hard hanya orisinal. Hanya 11 soal evaluatif tanpa gambar yang layak dan tidak kembar dengan easy/medium; sisa kuota akan berupa soal hitung atau nyaris kembar.
  - SMA10-B6 subbab A medium: 14/20 — Subbab A (p197-p208) tipis: hampir semua soal bukunya berupa grafik gambar, acuan siswa tekstual sudah terpakai di easy, dan tanpa gambar tidak ada pretest layak. Soal medium tambahan akan nyaris kembar dengan easy atau memerlukan gambar.
  - SMA10-B6 subbab C hard: 10/20 — Acuan teks subbab C habis dan jenis penalaran hard yang layak (evaluasi klaim korelasi, pencilan, kuartil, rancang data, temukan kesalahan) terbatas; soal hitung biasa dibuang dan soal kembar tidak dibuat demi kuota.
  - SMA10-B6 subbab C medium: 14/20 — Acuan siswa teks di subbab C (box plot dan diagram pencar) sudah dipakai di easy dan sebagian besar soal Latihan 6.4/6.5 bergambar atau jawabannya subjektif; soal medium yang tidak kembar dengan easy (data mentah, pencilan, perbandingan kelompok, tafsir diagram pencar) hanya cukup sekitar 14, sisanya hanya akan berupa soal nyaris kembar sehingga tidak dipaksa.

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA10-B1 | A. Definisi Eksponen | 20 | 20 | 20 |
| SMA10-B1 | B. Sifat-Sifat Eksponen | 20 | 20 | 19 |
| SMA10-B1 | C. Fungsi Eksponensial | 20 | 20 | 16 |
| SMA10-B1 | D. Bentuk Akar | 20 | 16 | 7 |
| SMA10-B2 | A. Barisan | 20 | 20 | 17 |
| SMA10-B2 | B. Deret | 20 | 20 | 15 |
| SMA10-B2 | C. Bunga | 15 | 19 | 7 |
| SMA10-B3 | A. Perbandingan Trigonometri | 20 | 20 | 20 |
| SMA10-B3 | B. Pemanfaatan Perbandingan Trigonometri | 20 | 20 | 20 |
| SMA10-B4 | A. Sistem Persamaan Linear | 20 | 20 | 12 |
| SMA10-B4 | B. Sistem Pertidaksamaan Linear | 20 | 20 | 10 |
| SMA10-B5 | A. Persamaan Kuadrat | 20 | 20 | 20 |
| SMA10-B5 | B. Fungsi Kuadrat | 20 | 20 | 20 |
| SMA10-B6 | A. Representasi Data | 15 | 14 | 11 |
| SMA10-B6 | B. Statistik Deskriptif | 20 | 20 | 20 |
| SMA10-B6 | C. Representasi Data Lanjutan | 20 | 14 | 10 |
| SMA10-B7 | A. Distribusi Peluang | 20 | 20 | 20 |
| SMA10-B7 | B. Aturan Penjumlahan | 20 | 20 | 20 |
| SMA10-B7 | C. Aturan Perkalian | 20 | 20 | 20 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
