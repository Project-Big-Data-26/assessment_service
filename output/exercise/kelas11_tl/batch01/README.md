# Serah-terima batch 01 — kelas11_tl

Total **1191 soal**, pipeline `exercise-2026-10-01`, skill: v1 (1191)

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
- `kapasitas_kurang` (25 subbab-level): jumlah soal di bawah kuota karena bahan subbab habis (alasan di meta dan lembar koreksi):

  - SMA11L-B1 subbab A hard: 10/20 — Subbab A (Jenis-Jenis Matriks, sekitar 8 halaman) hanya memuat definisi jenis matriks, transpos, dan kesamaan; easy+medium sudah memakai 40 soal dan 8 jenis. Penalaran sifat yang tersisa (klaim, penyangkal, parameter dua jenis, pencacahan matriks) hanya cukup untuk sekitar 10 soal hard tanpa kembar; sisanya akan menjadi soal hitung atau di luar materi subbab.
  - SMA11L-B1 subbab B hard: 10/20 — Subbab B hanya ~2 halaman (Definisi 1.1: ordo sama dan elemen seletak sama). Easy dan medium sudah memakai 40 soal; hard yang bermakna hanya penalaran sifat kesamaan (evaluasi klaim, contoh penyangkal, kesalahan ordo, parameter, pencacahan, rantai). Menambah ke 20 akan memunculkan soal nyaris kembar atau materi di luar subbab.
  - SMA11L-B1 subbab C hard: 12/20 — Materi C (penjumlahan/pengurangan matriks, lawan, sifat 1.1) sempit dan 40 soal easy+medium sudah menghabiskan hitungan dan persamaan matriks; hard bermakna hanya lewat penalaran (evaluasi klaim, penyangkal, parameter, temukan kesalahan) yang layak 12 soal tanpa nyaris kembar. Acuan siswa terbaca habis sehingga semua soal orisinal (hard tanpa batas bawah variasi).
  - SMA11L-B1 subbab D hard: 18/20 — Hard subbab D bermakna hanya lewat penalaran sifat perkalian matriks (klaim, penyangkal, parameter, pangkat, perancangan, pengelompokan). Setelah easy dan medium memakai 40 soal dan acuan siswa/pretest habis, bahan penalaran orisinal yang tidak nyaris kembar hanya cukup untuk sekitar belasan soal, bukan 20.
  - SMA11L-B1 subbab E hard: 14/20 — Hard bermakna hanya lewat penalaran sifat |AB|=|A||B|, |kA|, invers, adjoin, syarat Cramer, parameter dua syarat, dan contoh penyangkal; materi inti (hitung determinan/invers/SPL) sudah habis terpakai di easy dan medium (40 soal) dan bentuk lain akan nyaris kembar atau di luar subbab.
  - SMA11L-B2 subbab A hard: 9/20 — Materi subbab A tipis (definisi, derajat, koefisien utama, nilai fungsi, perilaku ujung, pemodelan). Hanya 9 soal hard yang benar-benar bernalar (evaluasi klaim, temukan kesalahan, penyangkal, rancang); sisanya hanya hitung langsung atau mengulang pola easy/medium sehingga tidak dipaksa.
  - SMA11L-B2 subbab B hard: 16/20 — Hard subbab B (penjumlahan, pengurangan, perkalian polinomial) hanya menyediakan penalaran C5-C6 pada evaluasi klaim derajat, temuan kesalahan langkah, contoh penyangkal, dan perancangan polinomial; soal hitung langsung, parameter, atau soal sistem polinomial bersifat C3-C4 sehingga tidak dilabeli hard. Sisanya akan menjadi soal nyaris kembar.
  - SMA11L-B2 subbab C hard: 17/20 — Subbab C (pembagian polinomial, p84-p95) sempit: penalaran hard hanya berkisar pada Teorema Sisa, Horner, dan sisa pembagi kuadrat; sudah dipakai easy dan medium. Soal hard tambahan akan berupa kembaran berangka berbeda atau materi faktor (subbab D), sehingga tidak dipaksakan.
  - SMA11L-B2 subbab D hard: 11/20 — Subbab D (p96-p100) tipis. Hanya sebelas soal yang benar-benar menuntut penalaran C5-C6 (evaluasi klaim, contoh penyangkal, temukan kesalahan, rancang, bandingkan). Soal parameter dan hitung langsung murni C3-C4 dan sudah dipakai di medium; membuat soal kembar berangka beda hanya demi kuota ditolak.
  - SMA11L-B2 subbab E hard: 7/20 — Subbab E (Identitas Polinomial) hanya 5 halaman dengan satu sifat (7 identitas) dan dua contoh; setelah easy (20) dan medium (16), bahan hard yang bernalar sungguhan hanya Latihan E no.7 (tripel Pythagoras), evaluasi klaim/contoh penyangkal, penyamaan koefisien, dan faktorisasi non-standar. Soal tambahan akan menjadi kembar berangka beda atau hanya hitung langsung.
  - SMA11L-B2 subbab E medium: 16/20 — Subbab E (Identitas Polinomial) hanya 5 halaman dengan satu sifat (7 identitas) dan dua contoh; soal medium yang layak hanya lewat faktorisasi bentuk tersusun, parameter koefisien, nilai numerik dengan identitas, dan evaluasi klaim. Soal tambahan akan menjadi kembar berangka beda atau berpindah ke hard.
  - SMA11L-B3 subbab A hard: 13/20 — Subbab A (konversi radian-derajat, lingkaran satuan, tanda fungsi, genap-ganjil) sempit; soal hard yang benar-benar bernalar (evaluasi klaim, contoh penyangkal, temukan kesalahan, parameter) hanya cukup 13 tanpa jatuh menjadi hitung langsung atau kembar dengan easy/medium. Kuota 20 tidak dipaksa.
  - SMA11L-B3 subbab B hard: 10/20 — Subbab B (Grafik Fungsi Trigonometri) hampir seluruh soalnya berbasis gambar grafik (Latihan B, Mari Berpikir Kreatif, Contoh sketsa) dan acuan teks sudah habis di easy/medium; hard hanya bisa berupa evaluasi klaim, contoh penyangkal, kesalahan penyusunan model, dan syarat parameter tanpa membuat soal kembar atau memakai materi di luar subbab.
  - SMA11L-B3 subbab B medium: 14/20 — Subbab B (Grafik Fungsi Trigonometri) teks-saja: acuan variasi siswa yang terbaca sudah dipakai easy (Contoh 3.12 no.1, MM3.12 no.1, Latihan B no.6a, 8a, 9a, 9c, pretest) dan sisa Latihan B/Contoh/MBK butuh grafik; sisa acuan hanya Contoh 3.12 no.2, MM3.12 no.2, Latihan B 8a/8c/9b. Soal orisinal medium (transformasi, model gelombang dua langkah+) lebih banyak akan nyaris kembar satu sama lain.
  - SMA11L-B3 subbab C hard: 6/20 — Subbab C hanya p150-p155 (identitas dasar, penjumlahan/pengurangan sudut, Latihan C). Bukti identitas bergambar tidak dapat dipakai, dan acuan teks habis di easy dan medium. Soal hard yang layak (evaluasi klaim, syarat domain, temukan kesalahan, rancang identitas) hanya cukup sekitar 6; sisanya menjadi soal kembar atau di luar subbab.
  - SMA11L-B3 subbab C medium: 15/20 — Subbab C hanya p150-p155: identitas dasar, penjumlahan/pengurangan sudut, dan Latihan C 6 soal. Bukti identitas (Latihan 4b, Contoh 3.13/3.14, Mari Mencoba) berupa gambar sehingga tidak dapat dipakai; acuan siswa/pretest teks sudah banyak terpakai di easy. Soal medium lain akan nyaris kembar atau di luar materi.
  - SMA11L-B3 subbab D hard: 10/20 — Subbab D (Aturan Sinus) tipis dan tanpa soal bergambar: acuan variasi sudah habis di easy/medium, sedangkan penalaran hard yang tidak kembar hanya mencakup kasus ambigu SSA (jumlah segitiga), klaim sinus-sisi, dan batas sinus lewat jari-jari lingkaran luar. Soal layak yang tidak kembar hanya 10.
  - SMA11L-B3 subbab D medium: 11/20 — Subbab D (Aturan Sinus) tipis: Rumus Sifat 3.5 hanya gambar, Contoh 3.16 dan Latihan D no.1-2, 6-8 berupa gambar atau teks pecahan rusak, dan acuan variasi pretest/Buku Siswa sudah dipakai di easy. Soal medium layak yang tidak kembar dengan easy hanya tersedia sekitar 11.
  - SMA11L-B3 subbab E hard: 11/20 — Aturan Kosinus hanya satu subbab tipis; setelah soal hitung langsung dan variasi acuan habis (Latihan E no.7 ambigu), hanya 11 soal penalaran (C5) yang layak tanpa soal kembar berangka beda.
  - SMA11L-B4 subbab A hard: 12/20 — Acuan variasi habis di easy+medium dan materi subbab hanya menopang soal hard berupa evaluasi klaim, temukan kesalahan, dan rancangan sederhana; soal hitung langsung dibuang agar tidak setara medium.
  - SMA11L-B4 subbab B hard: 15/20 — Hard subbab Hasil Kali Titik hanya memuat satu rumus inti (u.v = |u||v|cos theta, tanda sudut, ortogonal, proyeksi). Soal hard sungguhan (evaluasi klaim, contoh penyangkal, kesalahan langkah, syarat parameter, perancangan) habis di sekitar 15; sisanya hanya hitung langsung atau soal kembar berangka beda yang tidak dipaksa.
  - SMA11L-B4 subbab C hard: 11/20 — Hard Pembuktian Geometris sangat tipis: acuan teks terbaca habis di easy/medium dan soal pembuktian terbuka tidak bisa jadi pilihan ganda. 11 soal evaluasi klaim/penyangkal/temuan kesalahan/syarat parameter yang layak tanpa kembar; sisanya hanya hitung langsung sehingga dibuang.
  - SMA11L-B4 subbab C medium: 17/20 — Medium Pembuktian Geometris tipis: acuan teks terbaca habis di easy (Latihan C no.1,2,4, Contoh/MM 4.17 sudah dipakai 2x); Latihan C no.3,5,6 dan Contoh/MM 4.16 bergantung gambar; soal pembuktian panjang tidak bisa jadi pilihan ganda. 17 soal layak tanpa kembar dengan easy.
  - SMA11L-B5 subbab A hard: 12/20 — Materi subbab A (translasi, refleksi, rotasi, dilatasi) hanya menopang sekitar 12 soal hard yang benar-benar C5 tanpa menjadi soal hitung langsung atau kembar berangka beda; soal parameter dan hitung murni sudah dipakai di medium.
  - SMA11L-B5 subbab B hard: 14/20 — Subbab B hanya memuat matriks transformasi tunggal (pencerminan, translasi, rotasi, dilatasi); komposisi transformasi ada di subbab C. Penalaran tingkat hard yang layak tanpa soal kembar hanya cukup untuk 14 soal.

## Ringkasan per subbab

| Bab | Subbab | easy | medium | hard |
|---|---|---|---|---|
| SMA11L-B1 | A. Jenis-Jenis Matriks | 20 | 20 | 10 |
| SMA11L-B1 | B. Kesamaan Dua Matriks | 20 | 20 | 10 |
| SMA11L-B1 | C. Penjumlahan dan Pengurangan Antarmatriks | 20 | 20 | 12 |
| SMA11L-B1 | D. Perkalian Matriks | 20 | 20 | 18 |
| SMA11L-B1 | E. Determinan Matriks dan Invers Matriks | 20 | 20 | 14 |
| SMA11L-B2 | A. Polinomial dan Fungsi Polinomial | 20 | 20 | 9 |
| SMA11L-B2 | B. Penjumlahan, Pengurangan, dan Perkalian Polinomial | 20 | 20 | 16 |
| SMA11L-B2 | C. Pembagian Polinomial | 20 | 20 | 17 |
| SMA11L-B2 | D. Faktor dan Pembuat Nol Polinomial | 20 | 20 | 11 |
| SMA11L-B2 | E. Identitas Polinomial | 20 | 16 | 7 |
| SMA11L-B3 | A. Fungsi Trigonometri dan Lingkaran Satuan | 20 | 20 | 13 |
| SMA11L-B3 | B. Grafik Fungsi Trigonometri | 20 | 14 | 10 |
| SMA11L-B3 | C. Identitas Trigonometri | 20 | 15 | 6 |
| SMA11L-B3 | D. Aturan Sinus | 20 | 11 | 10 |
| SMA11L-B3 | E. Aturan Kosinus | 20 | 20 | 11 |
| SMA11L-B4 | A. Vektor pada Bidang | 20 | 20 | 12 |
| SMA11L-B4 | B. Hasil Kali Titik | 20 | 20 | 15 |
| SMA11L-B4 | C. Pembuktian Geometris | 20 | 17 | 11 |
| SMA11L-B5 | A. Transformasi pada Bidang Kartesius | 20 | 20 | 12 |
| SMA11L-B5 | B. Kaitan Matriks dengan Transformasi | 20 | 20 | 14 |
| SMA11L-B5 | C. Komposisi Transformasi dengan Matriks | 20 | 20 | 20 |
| SMA11L-B6 | A. Fungsi Logaritma | 20 | 20 | 20 |
| SMA11L-B6 | B. Fungsi Aljabar | 20 | 20 | 20 |

## Aturan pemakaian

- Master tidak diubah setelah diserahkan. Perbaikan/tambahan soal lewat batch baru agar hasil validasi tetap cocok dengan isi file.
- Koreksi isi soal dilakukan di file kerja `bab<NN>/<K>_<level>.json`, lalu export dijalankan ulang (hasil export deterministik).
