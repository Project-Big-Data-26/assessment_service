# Serah-terima batch 01 — kelas12

Total **836 soal**, pipeline `exercise-2026-10-01`, skill: v1 (836)

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

  - SMA12U-B1 subbab C easy: 13/20 — Subbab C (Bunga Tunggal) hanya selebar p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5 Angga), rumus B = M x p% x n, dan Contoh 1.9 (Zaka), tanpa Latihan bernomor. Acuan pretest hanya 2 soal (4 variasi) ditambah Contoh 1.9 (2 variasi); UK 6 (cicilan) 3 langkah sehingga melebihi easy. Lebih dari 13 soal easy akan nyaris kembar.
  - SMA12U-B1 subbab C hard: 13/20 — Subbab C (Bunga Tunggal) hanya p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5), rumus B = M x p% x n, dan Contoh 1.9, tanpa Latihan bernomor. Penalaran hard yang layak (evaluasi klaim, temukan kesalahan, contoh penyangkal, rancang modal/lama, perbandingan skema bunga dan cicilan, parameter dua simpanan) sudah terpakai dalam 13 soal; semua acuan variasi sudah habis di easy/medium sehingga seluruh soal orisinal. Tambahan akan nyaris kembar atau keluar materi (bunga majemuk, bukan bagian subbab).
  - SMA12U-B1 subbab C medium: 15/20 — Subbab C (Bunga Tunggal) hanya p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5), rumus B = M x p% x n, dan Contoh 1.9, tanpa Latihan bernomor. Acuan variasi layak untuk medium hanya UK 6 (cicilan Raka) dan Contoh 1.9 (masing-masing maks 2); acuan pretest lain bertaraf easy dan sudah dipakai di easy. Sudut medium orisinal (cari n/p/M dari saldo, bandingkan simpanan, barisan dan deret nilai uang, satuan bulan, angsuran) sudah terpakai; tambahan akan nyaris kembar.
  - SMA12U-B2 subbab A easy: 14/20 — Subbab A Bab 2 (Suku Bunga Tunggal) hanya 3 halaman (p55-p57): dua pengertian, rumus B = M x p% x n, Masalah A dan Masalah B, tanpa Latihan bernomor. Acuan hanya 2 soal (pretest Masalah A/B, maks 4 variasi), sehingga porsi variasi easy 60% tidak tercapai; konsep sama dengan Bab 1 subbab C, jadi lebih dari 14 soal akan nyaris kembar dengan soal-soal Bab 1 C atau sesamanya.
  - SMA12U-B2 subbab A hard: 11/20 — Subbab A Bab 2 (Suku Bunga Tunggal) hanya p55-p57 tanpa Latihan bernomor; konsepnya cuma B = M x p% x n, konversi persen tahunan ke bulanan, modal akhir, dan sifat linear. Acuan variasi pretest sudah habis di easy dan medium, sehingga hard 0 variasi. Sudut penalaran yang layak (evaluasi klaim, temukan kesalahan, contoh penyangkal, perancangan, perbandingan skema) habis sekitar 11 soal; lebih dari itu nyaris kembar satu sama lain atau dengan Bab 1 subbab C (bunga tunggal tahunan, cicilan, dua bank).
  - SMA12U-B2 subbab A medium: 14/20 — Subbab A Bab 2 (Suku Bunga Tunggal) hanya p55-p57 tanpa Latihan bernomor; konsepnya cuma rumus B = M x p% x n, konversi persen tahunan ke bulanan, modal akhir, dan sifat linear. Kedua acuan pretest (Masalah A/B) sudah habis dipakai (maks 2 variasi per level) di easy dan tidak ada soal asli lain di buku, sehingga medium 0 variasi (di bawah porsi 50%). Lebih dari 14 soal medium akan nyaris kembar satu sama lain atau dengan Bab 1 C (bunga tunggal tahunan, cicilan, dua bank).
  - SMA12U-B2 subbab B hard: 15/20 — Materi subbab B (bunga majemuk) sempit: hanya rumus M(1+p)^n, p per periode, dan tabel pangkat. Setelah easy dan medium memakai semua acuan variasi dan sudut hitung dasar, hard yang layak (evaluasi klaim, temukan kesalahan, penyangkal, perbandingan skema, rancang) hanya cukup 15 soal tanpa nyaris kembar atau di luar materi.
  - SMA12U-B2 subbab C hard: 17/20 — Subbab C hanya memuat anuitas biasa (FV, PV, konversi periode, hubungan FV-PV). Setelah easy dan medium, seluruh acuan variasi sudah terpakai maksimum dan sudut hard (evaluasi klaim, temukan kesalahan, syarat ganda, perancangan, perbandingan skema, dua fase) habis pada 17 soal; soal tambahan akan nyaris kembar atau memerlukan anuitas terutang yang rumusnya tidak diberikan buku.
  - SMA12U-B2 subbab C medium: 19/20 — Acuan variasi layak subbab C (Contoh 2.3, 2.4, pretest Aliyya, UK-6, UK-7) sudah terpakai maksimum 2 variasi masing-masing di easy, sehingga medium seluruhnya orisinal. Materi subbab hanya FV/PV anuitas biasa, konversi periode, dan hubungan FV-PV; soal orisinal ke-20 akan nyaris kembar dengan soal lain atau memakai anuitas terutang yang rumusnya tidak diberikan buku.
  - SMA12U-B2 subbab D hard: 14/20 — Materi subbab D hanya p73-p76 (satu skema pinjaman pokok tetap dengan rumus bunga bulan ke-k; anuitas milik subbab E). Setelah 14 soal hard orisinal (evaluasi klaim, temukan kesalahan, contoh penyangkal, perancangan, perbandingan skema), sudut penalaran yang tersisa nyaris kembar dengan easy/medium atau di luar materi, jadi tidak dipaksa ke 20.
  - SMA12U-B2 subbab F hard: 17/20 — Subbab F hanya memuat dua parameter (suku bunga dan periode pembayaran) dengan rumus nilai akhir bunga majemuk; acuan pretest dan Buku Siswa sudah habis pada easy dan medium. Penalaran hard (evaluasi klaim, temukan kesalahan, syarat ganda, perancangan parameter, perbandingan skema) hanya layak sampai 17 soal tanpa kembar atau materi di luar subbab.
  - SMA12U-B3 subbab A hard: 14/20 — Subbab A (Aturan Pengisian Tempat) hanya memuat aturan penjumlahan, perkalian, dan faktorial; easy dan medium sudah memakai 40 soal dan menghabiskan sudut bilangan bersyarat, komplemen, data lintas kelompok, dan faktorial. Soal hard yang layak berupa evaluasi penyelesaian, contoh penyangkal, urutan pengisian, perbandingan perubahan, perancangan parameter, dan kasus bersyarat berjenjang: sekitar 14 soal tanpa kembar atau materi di luar subbab (permutasi/kombinasi ada di subbab B dan C).

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA12U-B1 | A. Barisan | 20 | 20 | 20 |
| SMA12U-B1 | B. Deret | 20 | 20 | 20 |
| SMA12U-B1 | C. Bunga Tunggal | 13 | 15 | 13 |
| SMA12U-B2 | A. Suku Bunga Tunggal | 14 | 14 | 11 |
| SMA12U-B2 | B. Investasi Bunga Majemuk | 20 | 20 | 15 |
| SMA12U-B2 | C. Investasi Anuitas | 20 | 19 | 17 |
| SMA12U-B2 | D. Pinjaman Bunga Majemuk | 20 | 20 | 14 |
| SMA12U-B2 | E. Pinjaman dengan Anuitas | 20 | 20 | 20 |
| SMA12U-B2 | F. Parameter Investasi dan Pinjaman | 20 | 20 | 17 |
| SMA12U-B3 | A. Aturan Pengisian Tempat | 20 | 20 | 14 |
| SMA12U-B3 | B. Permutasi | 20 | 20 | 20 |
| SMA12U-B3 | C. Kombinasi | 20 | 20 | 20 |
| SMA12U-B3 | D. Penerapan Permutasi dan Kombinasi | 20 | 20 | 20 |
| SMA12U-B4 | A. Peluang Suatu Kejadian | 20 | 20 | 20 |
| SMA12U-B4 | B. Peluang Kejadian Majemuk | 20 | 20 | 20 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
