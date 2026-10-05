# Serah-terima batch 01 — kelas5

Total **916 soal**, pipeline `exercise-2026-10-01`, skill: v1 (827), pra-v1 (89)

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
- `kapasitas_kurang` (37 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SD5-B4 subbab A easy: 9/10 — Subbab A hanya memuat satu konsep (keliling = jumlah panjang sisi). Soal pretest dan latihan Buku Siswa subbab A hampir semuanya bergambar (hanya p0129 1b-1 yang teksnya layak jadi acuan), dan rumus keliling segitiga/segi empat/segi banyak ada di subbab B-E. Soal ke-10 hanya akan nyaris kembar atau di luar materi.
  - SD5-B4 subbab A hard: 6/10 — Subbab A hanya memuat satu konsep (keliling = jumlah panjang sisi); rumus persegi/persegi panjang ada di subbab C dan keliling segitiga/segi banyak di B-E. Acuan pretest A (p0129) sudah habis dipakai di easy dan medium, dan soal Siswa p127-p130 hampir semua bergambar, sehingga hard bernalar yang layak hanya 6 tanpa nyaris kembar atau di luar materi.
  - SD5-B4 subbab A medium: 9/10 — Subbab A hanya memuat satu konsep (keliling = jumlah panjang sisi); rumus persegi/persegi panjang ada di subbab C dan keliling segitiga/segi banyak di B-E. Acuan pretest A hanya satu soal teks (p0129), sudah dipakai 2 variasi di easy, dan soal Siswa p123-p130 hampir semuanya bergambar, sehingga soal ke-10 hanya akan nyaris kembar atau di luar materi.
  - SD5-B4 subbab B easy: 9/10 — Subbab B (Siswa p131-p133) sangat tipis: hanya konsep keliling segitiga (jumlah tiga sisi, 3 x sisi untuk sama sisi). Soal Siswa dan pretest B (Ayo Berlatih 1-2, Uji Kompetensi 1) bergantung gambar sehingga tidak layak jadi acuan variasi; 9 soal orisinal tanpa soal nyaris kembar.
  - SD5-B4 subbab B hard: 7/10 — Subbab B (Siswa p131-p133) hanya memuat konsep keliling segitiga (jumlah tiga sisi, 3 x sisi untuk sama sisi). Easy dan medium sudah memakai sisi hilang, cerita, putaran, dan sisa kawat; 7 soal hard orisinal (evaluasi klaim, temukan kesalahan, keputusan, perancangan) tanpa nyaris kembar dan tanpa materi di luar subbab. Soal Siswa dan pretest bergantung gambar sehingga tidak ada acuan variasi layak.
  - SD5-B4 subbab B medium: 8/10 — Subbab B (Siswa p131-p133) hanya memuat konsep keliling segitiga (jumlah tiga sisi, 3 x sisi untuk sama sisi). Soal Siswa dan pretest B bergantung gambar sehingga tidak ada acuan variasi layak; 8 soal orisinal medium (sisi hilang, cerita, perbandingan, sisa kawat) tanpa soal nyaris kembar dan tanpa materi di luar subbab.
  - SD5-B4 subbab C easy: 9/10 — Subbab C (Siswa p134-p137) hanya memuat rumus persegi panjang, persegi, dan trapesium/segi empat sembarang, hampir semua bergambar; acuan pretest C (ayo-berlatih a/b, p0136-2, uji-kompetensi-2) bergantung gambar sehingga tidak layak jadi acuan variasi. 9 soal orisinal berbeda sudut; soal ke-10 hanya akan menjadi kembar.
  - SD5-B4 subbab C hard: 8/10 — Subbab C (Siswa p134-p137) hanya memuat rumus keliling persegi panjang, persegi, dan trapesium/segi empat sembarang, hampir semua bergambar; acuan pretest C bergantung gambar. Easy dan medium sudah memakai 9 soal orisinal tiap level; untuk hard hanya ada 8 sudut penalaran berbeda (evaluasi klaim, kesalahan, banyak kemungkinan, tembok, gabungan, perubahan ukuran, biaya dengan pintu); soal ke-9 dan 10 akan menjadi kembar atau memakai materi luas yang di luar subbab.
  - SD5-B4 subbab C medium: 9/10 — Subbab C (Siswa p134-p137) hanya memuat rumus keliling persegi panjang, persegi, dan trapesium/segi empat sembarang, hampir semua bergambar; acuan pretest C bergantung gambar sehingga tidak layak jadi acuan variasi. Level easy sudah memakai 9 soal orisinal; 9 soal medium orisinal berbeda sudut (pemodelan, bahan, banyak putaran, selisih), soal ke-10 hanya akan menjadi kembar.
  - SD5-B4 subbab D easy: 9/10 — Subbab D (Siswa p138-p140) tipis dan bergambar; satu-satunya soal pretest D (uji-kompetensi-3) bergantung gambar sehingga tidak ada acuan variasi layak. Semua soal orisinal; 10 soal akan menuntut variasi atau nyaris kembar.
  - SD5-B4 subbab D hard: 7/10 — Subbab D (Siswa p138-p140) sangat tipis dan bergambar: hanya keliling segi lima/enam/delapan beraturan dan penjumlahan sisi tak sama. Easy dan medium sudah memakai pola dasar. Hard tanpa acuan pretest yang layak; semua orisinal. Soal ke-8 sampai 10 akan nyaris kembar atau memerlukan materi di luar subbab (luas, bangun datar lain).
  - SD5-B4 subbab D medium: 9/10 — Subbab D (Siswa p138-p140) tipis dan bergambar: hanya keliling segi banyak beraturan (segi lima/enam/delapan) dan sisi tak sama = jumlah semua sisi. Pretest D bergantung gambar sehingga tidak ada acuan variasi layak; semua soal orisinal. Soal ke-10 akan nyaris kembar atau di luar materi.
  - SD5-B4 subbab E easy: 9/10 — Subbab E (Siswa p141-p145) hanya satu konsep (keliling bangun gabungan = jumlah sisi terluar) dan seluruh contoh/latihan serta soal pretest E bergantung gambar denah; tanpa gambar hanya 9 soal orisinal yang layak tanpa nyaris kembar, tidak ada acuan variasi.
  - SD5-B4 subbab E hard: 7/10 — Subbab E (Siswa p141-p145) hanya satu konsep (keliling bangun gabungan = jumlah sisi terluar) dan semua contoh, latihan, serta soal pretest E bergantung gambar denah; tanpa gambar hanya sekitar 7 soal hard berbasis penalaran yang layak tanpa nyaris kembar dengan easy/medium, tidak ada acuan variasi.
  - SD5-B4 subbab E medium: 9/10 — Subbab E (Siswa p141-p145) hanya satu konsep (keliling bangun gabungan = jumlah sisi terluar) dan semua contoh/latihan serta soal pretest E bergantung gambar denah; tanpa gambar hanya 9 soal medium orisinal yang layak tanpa nyaris kembar dengan easy, tidak ada acuan variasi.
  - SD5-B5 subbab B easy: 9/10 — Tidak ada acuan variasi yang layak: soal Buku Siswa dan pretest subbab B (tabel/kotak satuan, kertas berpetak, gambar bangun) semuanya bergantung gambar, dan pretest 5-4 milik subbab D. Maka 9 soal orisinal berdasarkan rumus subbab (persegi panjang, persegi, segitiga, jajar genjang, trapesium, belah ketupat, layang-layang, soal cerita, ukuran hilang); soal ke-10 akan nyaris kembar.
  - SD5-B5 subbab B medium: 9/10 — Tidak ada acuan variasi yang layak: soal Buku Siswa dan pretest subbab B (kertas berpetak, kotak satuan, gambar bangun gabungan) bergantung gambar atau sudah dipakai di easy, dan pretest 5-4 milik subbab D. Maka 9 soal orisinal berbasis rumus subbab; soal ke-10 akan nyaris kembar dengan easy atau di luar materi.
  - SD5-B5 subbab C easy: 9/10 — Subbab C tidak punya soal teks yang layak jadi acuan variasi: semua soal pretest C (Uji Kompetensi 3 dan 4, dan 1-2 di subbab lain) dan Uji Kompetensi Siswa p178 bergambar tanpa ukuran terbaca di teks, Eksplorasi 5.3 berisi isian gambar. Maka 9 soal semuanya orisinal (porsi variasi 0), bukan dilabeli variasi demi porsi; soal ke-10 akan nyaris kembar (pola bagian + bagian).
  - SD5-B5 subbab C medium: 9/10 — Tidak ada acuan variasi yang layak di subbab C (soal pretest dan Uji Kompetensi p178 bergambar tanpa ukuran di teks), jadi 9 soal semuanya orisinal; soal ke-10 akan nyaris kembar pola easy/medium; porsi variasi 0 dinyatakan, tidak dilabeli demi porsi.
  - SD5-B5 subbab D easy: 9/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) dengan 2 soal pretest; acuan variasi teks hanya 2 sehingga maks 4 variasi, materi tidak cukup untuk 10 soal tanpa nyaris kembar.
  - SD5-B5 subbab D hard: 7/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) tentang keliling dan luas persegi panjang/persegi; acuan variasi sudah habis di easy dan medium. Hanya 7 soal penalaran yang layak tanpa nyaris kembar dengan easy/medium atau keluar materi.
  - SD5-B5 subbab D medium: 9/10 — Subbab D hanya 1 eksplorasi (Siswa p175-p176) dengan 2 soal pretest; acuan variasi teks hanya 2 dan sudah dipakai easy. Materi (keliling dan luas persegi panjang/persegi) tidak cukup untuk 10 soal medium tanpa nyaris kembar dengan easy.
  - SD5-B6 subbab A easy: 8/10 — Subbab A (p182-185) hampir seluruhnya berbasis gambar/praktik (lipat kertas, mengenali sudut pada bangun bergambar); soal pretest dan Ayo Berlatih bergantung gambar sehingga tidak ada acuan variasi layak, dan konsep teks hanya: penggaris siku-siku, lipatan kertas, pojok bangun persegi panjang/segitiga siku-siku. Lebih dari ini akan kembar atau masuk subbab B (lancip/tumpul).
  - SD5-B6 subbab A hard: 5/10 — Subbab A (p182-185) hampir seluruhnya berbasis gambar/praktik dengan konsep teks sangat sedikit (penggaris siku-siku, lipatan kertas, sudut siku-siku pada persegi panjang/segitiga siku-siku). Setelah easy (8) dan medium (7), hanya 5 soal penalaran hard yang layak dan tidak kembar; lainnya akan kembar atau masuk subbab B (lancip/tumpul).
  - SD5-B6 subbab A medium: 7/10 — Subbab A (p182-185) hampir seluruhnya berbasis gambar/praktik; konsep teks hanya penggaris siku-siku, lipatan kertas, pencatatan detektif sudut, dan sudut siku-siku pada persegi panjang/segitiga siku-siku. Soal medium C3-C4 yang layak dan tidak kembar dengan easy hanya 7; lebih dari itu akan kembar atau masuk subbab B (lancip/tumpul).
  - SD5-B6 subbab B easy: 9/10 — Subbab B (Siswa p186-190) singkat dan visual: definisi sudut/titik sudut/kaki sudut, lancip-siku-siku-tumpul, dan Ayo Berlatih jam serta benda bergambar. Pretest B hanya soal bergambar (jam, benda, peta persimpangan), sehingga acuan variasi terbatas pada jam, tangga, gunting, jendela. Soal lain akan kembar atau masuk subbab C (mengukur sudut dengan busur).
  - SD5-B6 subbab B hard: 8/10 — Subbab B (Siswa p186-190) hanya memuat definisi sudut/titik sudut/kaki sudut, tiga jenis sudut, dan jam; pengukuran busur milik subbab C. Acuan variasi pretest sudah habis di easy/medium. Setelah 8 soal penalaran (klaim, kesalahan, pasti-tidak pasti, simetri jam, perancangan pasangan pukul), soal ke-9 dan ke-10 akan kembar dengan easy/medium (jenis sudut benda/jam).
  - SD5-B6 subbab B medium: 7/10 — Subbab B (Siswa p186-190) singkat dan visual: definisi sudut/titik/kaki sudut, lancip-siku-siku-tumpul, dan jam. Acuan variasi pretest B (jam, tangga, gunting, jendela) sudah dipakai di easy dan butuh gambar; pengukuran busur milik subbab C. Hanya 7 soal orisinal medium yang layak tanpa kembar dengan easy.
  - SD5-B6 subbab C hard: 8/10 — Materi subbab C tinggal mengukur dengan busur (bergambar, dilewati), membandingkan lebar kipas, jenis sudut, sudut releks, dan jam; easy dan medium sudah memakai pola jam, releks, kipas, sudut luar, sehingga hard bernalar yang tidak kembar hanya cukup 8.
  - SD5-B6 subbab D easy: 9/10 — Subbab D (Siswa p199-p201) hanya memuat lima langkah melukis sudut dengan busur derajat; Ayo Berlatih berupa tugas menggambar dan pretest D (keramik) bergantung gambar, sehingga tidak ada acuan variasi teks. Setelah 9 soal tentang langkah, posisi busur, skala, dan pemeriksaan, soal ke-10 akan kembar.
  - SD5-B6 subbab D hard: 5/10 — Subbab D (Siswa p199-p200) hanya memuat lima langkah melukis sudut dengan busur derajat; easy dan medium sudah memakai 9 soal masing-masing dari seluruh pola (skala dua deret, garis lurus, urutan, salah baca, banding, berdampingan, klasifikasi, pembagian, kelipatan). Hard hanya layak 5 soal penalaran (evaluasi pernyataan, perancangan titik tanda, kesalahan skala, garis berimpit, hitung titik); soal ke-6 dst. akan kembar atau keluar materi.
  - SD5-B6 subbab D medium: 9/10 — Subbab D (Siswa p199-p201) hanya memuat lima langkah melukis sudut dengan busur derajat; Ayo Berlatih berupa tugas menggambar dan pretest D bergantung gambar, sehingga tidak ada acuan variasi. Medium dibatasi pada penerapan skala, sudut berdampingan, analisis kesalahan, dan perbandingan hasil; soal ke-10 akan kembar atau keluar materi.
  - SD5-B7 subbab A hard: 7/10 — Subbab hanya memuat ciri dan syarat segitiga; pola sedotan, sama kaki, dan sudut ketiga sudah dipakai easy/medium. Hanya 7 soal penalaran hard yang tidak kembar dengan level lain; sisanya akan menjadi variasi medium.
  - SD5-B7 subbab B hard: 7/10 — Teks subbab B hanya berisi penggolongan dan ciri (sisi, sudut berhadapan, diagonal, sumbu simetri); acuan pretest habis di easy/medium dan soal gambar dilewati. Hanya 7 soal penalaran yang tidak kembar dengan easy/medium; setara medium atas.
  - SD5-B8 subbab B hard: 7/10 — Subbab Piktogram hanya memuat konsep dasar (pengertian, membaca nilai simbol, setengah simbol). Hard tanpa gambar hanya tersisa 7 soal penalaran (evaluasi klaim, temukan kesalahan, nilai simbol, perancangan) yang tidak kembar dengan easy dan medium; sisanya akan menjadi variasi pola yang sama.
  - SD5-B8 subbab C hard: 6/10 — Subbab Diagram Batang (teks saja, tanpa gambar) hanya memberi 6 pola penalaran hard yang layak dan tidak kembar dengan easy/medium: sumbu terpotong, salah baca skala, pemilihan skala, data hilang dari total, menilai dua pernyataan, menilai kesimpulan. Pola lain (baca tabel lalu bandingkan, selisih, total, urutan) sudah dipakai di easy/medium.
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
| SD5-B4 | A. Apakah Keliling Bangun Datar Itu? | 9 | 9 | 6 |
| SD5-B4 | B. Keliling Segitiga | 9 | 8 | 7 |
| SD5-B4 | C. Keliling Segi Empat | 9 | 9 | 8 |
| SD5-B4 | D. Keliling Segi Banyak | 9 | 9 | 7 |
| SD5-B4 | E. Keliling Bangun Gabungan | 9 | 9 | 7 |
| SD5-B5 | A. Konsep Luas Daerah Bangun Datar | 10 | 10 | 10 |
| SD5-B5 | B. Luas Daerah Bangun Datar | 9 | 9 | 10 |
| SD5-B5 | C. Luas Daerah Bangun Gabungan | 9 | 9 | 10 |
| SD5-B5 | D. Hubungan Keliling dan Luas Daerah Bangun Datar | 9 | 9 | 7 |
| SD5-B6 | A. Sudut Siku-Siku | 8 | 7 | 5 |
| SD5-B6 | B. Pengertian Sudut | 9 | 7 | 8 |
| SD5-B6 | C. Mengukur dan Membandingkan Sudut | 10 | 10 | 8 |
| SD5-B6 | D. Melukis Sudut | 9 | 9 | 5 |
| SD5-B7 | A. Membandingkan Ciri-Ciri Segitiga | 10 | 10 | 7 |
| SD5-B7 | B. Membandingkan Ciri-Ciri Segi Empat | 10 | 10 | 7 |
| SD5-B8 | A. Mengumpulkan Data | 10 | 10 | 10 |
| SD5-B8 | B. Piktogram | 10 | 10 | 7 |
| SD5-B8 | C. Diagram Batang | 10 | 10 | 6 |
| SD5-B9 | A. Membaca dan Menulis Bilangan Cacah Sampai 1.000.000 dan Menentukan Nilai Tempatnya | 10 | 10 | 10 |
| SD5-B9 | B. Mengurutkan dan Membandingkan Bilangan Sampai 1.000.000 | 10 | 10 | 9 |
| SD5-B9 | C. Komposisi dan Dekomposisi Bilangan Sampai 1.000.000 | 10 | 10 | 10 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
