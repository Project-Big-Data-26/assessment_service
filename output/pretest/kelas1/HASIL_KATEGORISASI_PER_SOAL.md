# Hasil kategorisasi dan validasi per soal — pretest kelas 1

Dibuat: **2026-09-29 01:57 WIB**. Sumber: [`soal_pretest_db.json`](soal_pretest_db.json) (SHA-256 `18d73d90793fe4c81276de01e360067e6cf5e938ee93f2d61f7151e5b49f88ce`). Jumlah: **50 soal**.

## Status hasil saat laporan dibuat

| Tahap | Hasil yang tersedia | Keterangan |
|---|---|---|
| Pemeriksaan struktur JSON | **50/50 lulus** | Stem, 4 opsi, keunikan opsi, kunci, konsistensi alasan dan keberadaan aset |
| Aset visual | **19 soal** memuat 62 referensi; **62/62 file ditemukan** | Keberadaan file belum membuktikan isi gambar atau kecocokannya |
| Provenance `babNN.json` | **49/50 cocok tunggal** | Match berdasarkan stem, teks jawaban, dan referensi gambar; sisanya ambigu |
| Status ekstraksi sumber | `draft`: 41, `needs_review_soal`: 8 | Status pipeline ekstraksi; belum keputusan ahli |
| Validasi konten/kunci/solusi oleh ahli | **Belum** | Kunci yang menunjuk opsi belum membuktikan opsi itu benar secara matematika |
| Klasifikasi IndoBERT 3×4×3 | **Belum** | Artefak model terlatih tidak tersedia; `/v2/classify` belum menghasilkan prediksi |
| Confidence IndoBERT | **Belum** | Memerlukan logits model serta suhu kalibrasi yang ditetapkan dari validation gold |
| Gemini silver label / review | **Belum** | Belum ada hasil generasi per soal pada laporan ini |
| CTT / IRT | **Tidak diterapkan** | Belum ada jawaban siswa |

Tanda **—** pada tabel di bawah berarti hasil belum dihasilkan; itu bukan skor nol atau prediksi `knowing`. Pemeriksaan struktur tidak memberi gold label. `cognitive_level`, `cognitive_score`, dan `confidence_score` pada sumber saat ini kosong.

## Ringkasan masalah format

Tidak ditemukan masalah format oleh pemeriksaan otomatis. Isi matematika tetap harus direview.

## Ringkasan 50 soal

| No. | ID sumber | Subtopik | Stem singkat | KKO terdeteksi | Kesulitan agen 1–5 | Bukti buku guru | Validasi format | IndoBERT 3×4×3 | Confidence | Gemini |
|---:|---|---|---|---|---:|---|---|---|---|---|
| 1 | `1f52d8dff6bbb1b9be6a4516` | Menghitung, Membaca, dan Menulis Bilangan | Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. We… | menghitung | 2 | cocok, guru hlm. 38 | Lulus struktur | — | — | — |
| 2 | `e91b53ee437d36556aa832b8` | Menghitung, Membaca, dan Menulis Bilangan | Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca .... | — | 1 | cocok, guru hlm. 38 | Lulus struktur | — | — | — |
| 3 | `aded1ab9ecb9a5ad0e341f2a` | Membandingkan Banyak Benda | Buah mana yang jumlahnya lebih banyak? | membandingkan | 3 | cocok, guru hlm. 51 | Lulus struktur | — | — | — |
| 4 | `71dcf3a05499a6d3e660d279` | Membandingkan Banyak Benda | Buah mana yang jumlahnya lebih sedikit? | membandingkan | 3 | cocok, guru hlm. 51 | Lulus struktur | — | — | — |
| 5 | `a035dee2caefafa52096496e` | Menghitung Maju dan Mundur | Lengkapi urutan bilangan berikut. Lengkapi urutan bilangan berikut: 1, 2, .... | — | 2 | cocok, guru hlm. 46 | Lulus struktur | — | — | — |
| 6 | `593cbed3be61dd6c967e770c` | Menghitung Maju dan Mundur | Lengkapi urutan bilangan berikut. Lengkapi urutan bilangan berikut: 4, 5, .... | — | — | match sumber ambigu | Lulus struktur | — | — | — |
| 7 | `82267daa87c52ac8b3876098` | Pasangan Bilangan | Temukan pasangan bilangan berikut. Temukan pasangan bilangan berikut. Bilangan 9 dipa… | menghitung | 3 | cocok, guru hlm. 50 | Lulus struktur | — | — | — |
| 8 | `ddae4518c6926e380356e576` | Pasangan Bilangan | Pasangkan dua bilangan yang jumlahnya 6. Pasangkan dua bilangan yang jumlahnya 6. Bil… | menghitung | 2 | cocok, guru hlm. 50 | Lulus struktur | — | — | — |
| 9 | `ef1c6489a0d0caf13ccb067e` | Cerita Penjumlahan | Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil. | — | 3 | cocok, guru hlm. 66 | Lulus struktur | — | — | — |
| 10 | `f00f8cf40ab22284c6d216e4` | Cerita Penjumlahan | Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Sekarang ada 6… | menghitung | 1 | cocok, guru hlm. 64 | Lulus struktur | — | — | — |
| 11 | `bfe710d81f98780c622d6066` | Berbagai Cara Melakukan Penjumlahan | 2 + 4 = .... | — | 2 | cocok, guru hlm. 71 | Lulus struktur | — | — | — |
| 12 | `f9582859a11afb87b07d7da8` | Berbagai Cara Melakukan Penjumlahan | 1 + 1 = .... | — | 1 | cocok, guru hlm. 75 | Lulus struktur | — | — | — |
| 13 | `018e7b45e13d10afc8e87d48` | Soal Cerita Penjumlahan | Ada 3 sepeda Ada 1 becak. Berapa jumlah semua rodanya? | menghitung | 4 | cocok, guru hlm. 81 | Lulus struktur | — | — | — |
| 14 | `ef576d96de5e9070503cfdbb` | Soal Cerita Penjumlahan | Ada 3 motor. Ada 2 mobil. Berapa jumlah semua kendaraan? | menghitung | 3 | cocok, guru hlm. 82 | Lulus struktur | — | — | — |
| 15 | `adaec31c66c75d9c825ad888` | Cerita Pengurangan | 9 ... 7 Amati gambar. Lengkapi operasi pengurangannya. | — | 3 | cocok, guru hlm. 99 | Lulus struktur | — | — | — |
| 16 | `91118c063eea5c139d44fcfe` | Cerita Pengurangan | 7 – 2 = .... Isilah dengan bilangan yang tepat. | — | 2 | cocok, guru hlm. 113 | Lulus struktur | — | — | — |
| 17 | `7aa38a3601f61c91adbf30d4` | Berbagai Cara Melakukan Pengurangan | 6 – 4 = .... Isilah titik-titik di bawah ini. Tulis hasil pengurangannya. | — | 3 | cocok, guru hlm. 102 | Lulus struktur | — | — | — |
| 18 | `dde0b5654f117861d23c7988` | Berbagai Cara Melakukan Pengurangan | 0 1 2 3 4 5 6 7 8 9 10 Hitunglah. c. 9 – 3 = | menghitung | 1 | cocok, guru hlm. 113 | Lulus struktur | — | — | — |
| 19 | `b32a5eeea2898efe65526fe5` | Hubungan Penjumlahan dan Pengurangan | 9 - ... = 7 Isilah titik-titik di bawah ini. | — | 3 | cocok, guru hlm. 111 | Lulus struktur | — | — | — |
| 20 | `f6fcf5836947ff740007f70e` | Hubungan Penjumlahan dan Pengurangan | 2 + 6 = .... Isilah titik-titik di bawah ini. | — | 1 | cocok, guru hlm. 111 | Lulus struktur | — | — | — |
| 21 | `63d056eda46964278255c543` | Soal Cerita Pengurangan | Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe … | — | 4 | cocok, guru hlm. 113 | Lulus struktur | — | — | — |
| 22 | `9948cc37d48fcfe7ef094209` | Soal Cerita Pengurangan | Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah. Berapakah sisa telur Ibu sek… | — | 3 | cocok, guru hlm. 114 | Lulus struktur | — | — | — |
| 23 | `355049fbd1c523a25cd2de3d` | Mendeskripsikan Benda Berdasarkan Bentuk | Pasangkan yang bentuknya sama dengan gambar berikut. | — | 2 | cocok, guru hlm. 123 | Lulus struktur | — | — | — |
| 24 | `83dd4d12892fc170e56f4e1b` | Mendeskripsikan Benda Berdasarkan Bentuk | Pasangkan bentuk dengan namanya. Bangun keempat dari atas. | — | 1 | cocok, guru hlm. 131 | Lulus struktur | — | — | — |
| 25 | `98891851d1e28d6d8482ab94` | Mengelompokkan Benda | Lingkari jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas. | — | 3 | cocok, guru hlm. 127 | Lulus struktur | — | — | — |
| 26 | `7bde28fb9ff374327ad9c3ae` | Mengelompokkan Benda | Bangun yang satu warna dengan gambar di atas. | — | 2 | cocok, guru hlm. 127 | Lulus struktur | — | — | — |
| 27 | `aaf396a280df35704272b0d3` | Menyusun dan Mengurai Bentuk Bangun | Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa? | menghitung | 3 | cocok, guru hlm. 130 | Lulus struktur | — | — | — |
| 28 | `595d20d8c4a6f9418dc496b0` | Menyusun dan Mengurai Bentuk Bangun | Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa? | menghitung | 3 | cocok, guru hlm. 130 | Lulus struktur | — | — | — |
| 29 | `4d125a6ed9a2701db41cdcd1` | Menghitung, Membaca, dan Menulis Bilangan | Isilah dengan bilangan yang benar. 10 ditambah 3 menjadi .... | — | 2 | cocok, guru hlm. 141 | Lulus struktur | — | — | — |
| 30 | `fbc23bca48392d3c678c3beb` | Menghitung, Membaca, dan Menulis Bilangan | Isilah titik-titik berikut. 8 ditambah 10 menjadi .... | — | 2 | cocok, guru hlm. 150 | Lulus struktur | — | — | — |
| 31 | `4953bd9e508059b6896af5e5` | Menghitung Maju dan Mundur | Isilah titik-titik berikut. 15, 14, ...., .... | — | 3 | cocok, guru hlm. 144 | Lulus struktur | — | — | — |
| 32 | `02bd8bfdfd682bd80aa5f426` | Menghitung Maju dan Mundur | Lengkapi urutan bilangan berikut dan warnailah. 20, ...., 18 | — | 2 | cocok, guru hlm. 144 | Lulus struktur | — | — | — |
| 33 | `fb13c7e49793c36315b9e324` | Nilai Tempat | Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya. .... puluhan dan .... … | — | 3 | cocok, guru hlm. 147 | Lulus struktur | — | — | — |
| 34 | `daa41e2808537d493a6c0994` | Nilai Tempat | Hitunglah dan isi tabelnya. Nilai tempat 14 = .... puluhan dan .... satuan | menghitung | 2 | cocok, guru hlm. 151 | Lulus struktur | — | — | — |
| 35 | `76bd2315ce21573dfa2ea8d7` | Membandingkan Bilangan | Perhatikan bilangan berikut. 13 11 18 Urutan mulai dari bilangan terkecil: .... , ...… | — | 3 | cocok, guru hlm. 149 | Lulus struktur | — | — | — |
| 36 | `84e373946789a200e6b5203a` | Membandingkan Bilangan | Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola. Urutan banya… | — | 3 | cocok, guru hlm. 151 | Lulus struktur | — | — | — |
| 37 | `31e0c54a133ed9b166d1ed06` | Mengenal Konsep Lebih dari, Kurang dari, dan Selisih | Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi. Berapak… | — | 3 | cocok, guru hlm. 160 | Lulus struktur | — | — | — |
| 38 | `fafff0345aa730c0722fc259` | Mengenal Konsep Lebih dari, Kurang dari, dan Selisih | Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tik… | membandingkan | 1 | cocok, guru hlm. 157 | Lulus struktur | — | — | — |
| 39 | `4a1c88e1d656ed6e318fbc08` | Penjumlahan yang Hasilnya kurang dari 20 | Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng. Berapa jumlah kelereng mereka? | menghitung | 3 | cocok, guru hlm. 164 | Lulus struktur | — | — | — |
| 40 | `c5a941d72ce972bb9d49a4cc` | Penjumlahan yang Hasilnya kurang dari 20 | Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah. 14 + 5 = .... | menghitung, menerapkan | 2 | cocok, guru hlm. 168 | Lulus struktur | — | — | — |
| 41 | `54e65cf97cc65f3ef126daef` | Pengurangan yang Hasilnya Kurang dari 20 | Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus. Berapakah sisa bolu kukus Ibu… | — | 3 | cocok, guru hlm. 167 | Lulus struktur | — | — | — |
| 42 | `3dbc40f08ab7c63a376fc3e5` | Pengurangan yang Hasilnya Kurang dari 20 | Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah. 15 – 4 = .... | menghitung, menerapkan | 2 | cocok, guru hlm. 168 | Lulus struktur | — | — | — |
| 43 | `ff83d65211d6e4aa98e13b06` | Membandingkan dan Mengurutkan Panjang Benda | 4. Perhatikan gambar berikut. A B C Urutan bunga dari paling pendek: ...., ...., .... | — | 4 | cocok, guru hlm. 177 | Lulus struktur | — | — | — |
| 44 | `dc65bbd6611c904972206f6c` | Membandingkan dan Mengurutkan Panjang Benda | 7. C A B Burung yang terbang paling tinggi adalah .... | — | 2 | cocok, guru hlm. 177 | Lulus struktur | — | — | — |
| 45 | `75434d44f2b377da3027e153` | Mengukur Panjang Benda | 4. Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil … | — | 4 | cocok, guru hlm. 180 | Lulus struktur | — | — | — |
| 46 | `62785ac6ff0622ab70a94b13` | Mengukur Panjang Benda | 6. Temukan panjang pita berikut. A B C. Panjang pita B = 5 kotak. Panjang pita C = 4 … | — | 2 | cocok, guru hlm. 181 | Lulus struktur | — | — | — |
| 47 | `5e007b54e25f6f72efa82174` | Mengelompokkan Data | Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk.… | — | 3 | cocok, guru hlm. 190 | Lulus struktur | — | — | — |
| 48 | `17ba235cdc9fddc600303514` | Mengelompokkan Data | Perhatikan tabel dan jawablah pertanyaannya. Tabel Kue Kesukaan: Nama Kue Kue Talam K… | — | 2 | cocok, guru hlm. 196 | Lulus struktur | — | — | — |
| 49 | `e7d8a29f2e3a28f99529dfc8` | Diagram Gambar | Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Diagram Buah Kesukaan. Gam… | membandingkan | 4 | cocok, guru hlm. 195 | Lulus struktur | — | — | — |
| 50 | `8812007076d1edea9f050f6f` | Diagram Gambar | Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing. Wa… | — | 2 | cocok, guru hlm. 196 | Lulus struktur | — | — | — |

## Detail tiap soal

Pada setiap kartu, status `perlu review isi` berarti seseorang masih harus memeriksa ketepatan kunci, kecukupan stimulus, makna gambar, dan solusi minimum. Semua model tetap berstatus advisory sampai ada anotasi manusia.

### 01. `1f52d8dff6bbb1b9be6a4516`

Subtopik: Menghitung, Membaca, dan Menulis Bilangan · tipe: pilihan ganda · kelas: 1.

> Ayo menghitung banyak mainan. Wei pergi ke toko mainan. Wei melihat banyak mainan. Wei kesulitan menghitungnya. Ayo bantu Wei.
>
> Ayo bantu Wei. Ada .... (boneka kelinci). Berapa banyaknya?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 5 | Salah: tertukar dengan jumlah bola |
| B | 7 | Salah: salah hitung, kelebihan satu |
| C | 9 | Salah: tertukar dengan jumlah mobil-mobilan |
| D | 6 | Benar: ada 6 boneka kelinci pada rak paling atas |

- Kunci pada file: **D — 6**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0027-ayo-menghitung-mainan-4a`; siswa hlm. 27, guru hlm. 38; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: menghitung banyak benda pada gambar dalam satu kelompok. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0027-06.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 02. `e91b53ee437d36556aa832b8`

Subtopik: Menghitung, Membaca, dan Menulis Bilangan · tipe: pilihan ganda · kelas: 1.

> Pasangkan lambang bilangan dengan namanya. Bilangan 7 dibaca ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Tujuh | Benar: lambang 7 dibaca 'tujuh' |
| B | Delapan | Salah: tertukar dengan bilangan 8 |
| C | Enam | Salah: tertukar dengan bilangan 6 |
| D | Sembilan | Salah: tertukar dengan bilangan 9 |

- Kunci pada file: **A — Tujuh**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0026-pasangkan-lambang-bilangan-7`; siswa hlm. 26, guru hlm. 38; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: hanya membaca/mengingat nama bilangan yang sudah dikenalkan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `pertanyaan_disesuaikan_untuk_pg`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 03. `aded1ab9ecb9a5ad0e341f2a`

Subtopik: Membandingkan Banyak Benda · tipe: pilihan ganda · kelas: 1.

> Buah mana yang jumlahnya lebih banyak?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Tidak dapat ditentukan | Salah: tidak mau menghitung gambar pada kotak |
| B | B (jeruk) | Benar: jeruk pada kotak B berjumlah 6, lebih banyak daripada mangga pada kotak A yang berjumlah 4 |
| C | Sama banyak | Salah: tidak menghitung ulang jumlah pada tiap kotak |
| D | A (mangga) | Salah: tertukar, padahal jumlah mangga lebih sedikit |

- Kunci pada file: **B — B (jeruk)**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0048-evaluasi-2a`; siswa hlm. 48, guru hlm. 51; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus menghitung jumlah buah pada tiap kotak gambar sebelum membandingkan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **membandingkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 04. `71dcf3a05499a6d3e660d279`

Subtopik: Membandingkan Banyak Benda · tipe: pilihan ganda · kelas: 1.

> Buah mana yang jumlahnya lebih sedikit?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Tidak dapat ditentukan | Salah: tidak mau menghitung gambar pada kotak |
| B | A (mangga) | Benar: mangga pada kotak A berjumlah 4, lebih sedikit daripada jeruk pada kotak B yang berjumlah 6 |
| C | Sama banyak | Salah: tidak menghitung ulang jumlah pada tiap kotak |
| D | B (jeruk) | Salah: tertukar, padahal jumlah jeruk lebih banyak |

- Kunci pada file: **B — A (mangga)**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0048-evaluasi-2b`; siswa hlm. 48, guru hlm. 51; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus menghitung jumlah buah pada tiap kotak gambar sebelum membandingkan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0048-05.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **membandingkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 05. `a035dee2caefafa52096496e`

Subtopik: Menghitung Maju dan Mundur · tipe: pilihan ganda · kelas: 1.

> Lengkapi urutan bilangan berikut.
>
> Lengkapi urutan bilangan berikut: 1, 2, ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 | Benar: urutan naik satu-satu: 1, 2, 3 |
| B | 1 | Salah: mengulang bilangan pertama |
| C | 0 | Salah: menghitung mundur, bukan maju |
| D | 4 | Salah: meloncat satu angka |

- Kunci pada file: **A — 3**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0039-ayo-berlatih-1a`; siswa hlm. 39, guru hlm. 46; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: melanjutkan urutan bilangan naik dengan langkah satu-satu. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 06. `593cbed3be61dd6c967e770c`

Subtopik: Menghitung Maju dan Mundur · tipe: pilihan ganda · kelas: 1.

> Lengkapi urutan bilangan berikut.
>
> Lengkapi urutan bilangan berikut: 4, 5, ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 | Salah: menghitung mundur, bukan maju |
| B | 4 | Salah: mengulang bilangan pertama |
| C | 6 | Benar: urutan naik satu-satu: 4, 5, 6 |
| D | 7 | Salah: meloncat satu angka |

- Kunci pada file: **C — 6**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: 2 kandidat dari `babNN.json`; asal tunggal belum dapat dipastikan dari file ringkasan ini.
- Perkiraan kesulitan agen ekstraksi: — (provenance ambigu).
- Flag ekstraksi: — (provenance ambigu).
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 07. `82267daa87c52ac8b3876098`

Subtopik: Pasangan Bilangan · tipe: pilihan ganda · kelas: 1.

> Temukan pasangan bilangan berikut.
>
> Temukan pasangan bilangan berikut. Bilangan 9 dipasangkan menjadi dua bilangan berapa dan berapa?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 5 dan 3 | Salah: jumlahnya 8, bukan 9 |
| B | 4 dan 4 | Salah: jumlahnya 8, bukan 9 |
| C | 3 dan 6 | Salah: salah menghitung salah satu kelompok gambar |
| D | 4 dan 5 | Benar: 9 = 4 + 5, sesuai gambar 4 jeruk dan 5 buah lainnya |

- Kunci pada file: **D — 4 dan 5**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0043-ayo-berlatih-1b`; siswa hlm. 43, guru hlm. 50; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: melengkapi dua bagian sekaligus dari pasangan bilangan berdasarkan gambar. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0043-04.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 08. `ddae4518c6926e380356e576`

Subtopik: Pasangan Bilangan · tipe: pilihan ganda · kelas: 1.

> Pasangkan dua bilangan yang jumlahnya 6.
>
> Pasangkan dua bilangan yang jumlahnya 6. Bilangan berapa yang berpasangan dengan 4?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 | Salah: 4 + 3 = 7, bukan 6 |
| B | 2 | Benar: 4 + 2 = 6 |
| C | 4 | Salah: memasangkan bilangan dengan dirinya sendiri |
| D | 1 | Salah: 4 + 1 = 5, bukan 6 |

- Kunci pada file: **B — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab01.json` / `kelas1-b01-p0046-ayo-berlatih-4`; siswa hlm. 46, guru hlm. 50; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: mencari bilangan pelengkap agar jumlah dua bilangan sama dengan 6. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `pertanyaan_disesuaikan_untuk_pg`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 09. `ef1c6489a0d0caf13ccb067e`

Subtopik: Cerita Penjumlahan · tipe: pilihan ganda · kelas: 1.

> Ada .... mobil berwarna kuning. Ada .... mobil berwarna merah. Semuanya ada .... mobil.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 4 mobil kuning, 5 mobil merah, semuanya 9 mobil | Salah: salah menghitung mobil merah, kelebihan satu |
| B | 4 mobil kuning, 4 mobil merah, semuanya 9 mobil | Salah: salah menjumlahkan 4 + 4 |
| C | 4 mobil kuning, 4 mobil merah, semuanya 8 mobil | Benar: gambar menunjukkan 4 mobil kuning dan 4 mobil merah, 4 + 4 = 8 |
| D | 5 mobil kuning, 4 mobil merah, semuanya 9 mobil | Salah: salah menghitung mobil kuning, kelebihan satu |

- Kunci pada file: **C — 4 mobil kuning, 4 mobil merah, semuanya 8 mobil**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0058-ayo-berlatih-1a`; siswa hlm. 58, guru hlm. 66; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus menghitung dua kelompok mobil dari gambar lalu menjumlahkannya. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0058-03.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 10. `f00f8cf40ab22284c6d216e4`

Subtopik: Cerita Penjumlahan · tipe: pilihan ganda · kelas: 1.

> Ada 4 anak bermain lompat tali. Datang lagi 2 anak untuk ikut bermain. Sekarang ada 6 anak yang bermain. Mereka bermain bergantian.
>
> Berapa jumlah anak sekarang?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 2 | Salah: hanya jumlah anak yang datang, lupa anak yang sudah bermain sebelumnya |
| B | 6 | Benar: 4 anak awal ditambah 2 anak yang datang sama dengan 6 anak |
| C | 8 | Salah: salah menjumlahkan 4 dan 2 |
| D | 4 | Salah: hanya jumlah anak semula, lupa menambahkan anak yang datang |

- Kunci pada file: **B — 6**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0055-bermain-lompat-tali-2`; siswa hlm. 55, guru hlm. 64; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: tinggal membaca hasil penjumlahan yang sudah disebutkan dalam cerita ('Sekarang ada 6 anak'). Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 11. `bfe710d81f98780c622d6066`

Subtopik: Berbagai Cara Melakukan Penjumlahan · tipe: pilihan ganda · kelas: 1.

> 2 + 4 = ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 4 | Salah: hanya menuliskan salah satu bagian pasangan bilangan, lupa menjumlahkan dengan 2 |
| B | 5 | Salah: kurang menghitung satu |
| C | 6 | Benar: 2 + 4 = 6 |
| D | 7 | Salah: kelebihan menghitung satu |

- Kunci pada file: **C — 6**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0065-ayo-berlatih-1a`; siswa hlm. 65, guru hlm. 71; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: penjumlahan satu langkah, kedua bagian sudah diketahui dari pasangan bilangan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 12. `f9582859a11afb87b07d7da8`

Subtopik: Berbagai Cara Melakukan Penjumlahan · tipe: pilihan ganda · kelas: 1.

> 1 + 1 = ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 | Salah: kelebihan menghitung satu |
| B | 1 | Salah: hanya menghitung jari satu tangan, lupa tangan yang lain |
| C | 11 | Salah: menuliskan kedua angka berdampingan sebagai bilangan dua digit, bukan menjumlahkannya |
| D | 2 | Benar: 1 + 1 = 2 |

- Kunci pada file: **D — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0071-ayo-berlatih-1a`; siswa hlm. 71, guru hlm. 75; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: penjumlahan dasar 1 + 1 yang bisa dihitung langsung dari jari pada gambar. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 13. `018e7b45e13d10afc8e87d48`

Subtopik: Soal Cerita Penjumlahan · tipe: pilihan ganda · kelas: 1.

> Ada 3 sepeda Ada 1 becak.
>
> Berapa jumlah semua rodanya?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 9 roda | Benar: 3 sepeda x 2 roda = 6, 1 becak x 3 roda = 3, semuanya 6 + 3 = 9 roda |
| B | 10 roda | Salah: mengira salah satu sepeda beroda 4 seperti mobil |
| C | 6 roda | Salah: hanya menjumlahkan roda sepeda saja, lupa menambahkan roda becak |
| D | 8 roda | Salah: mengira becak beroda 2 seperti sepeda: 3x2 + 1x2 = 8 |

- Kunci pada file: **A — 9 roda**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0081-ayo-berlatih-3b`; siswa hlm. 81, guru hlm. 81; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **4/5**; alasan sumber: harus mengetahui jumlah roda tiap jenis kendaraan dari gambar sebelum menjumlahkan semuanya. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0081-01.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 14. `ef576d96de5e9070503cfdbb`

Subtopik: Soal Cerita Penjumlahan · tipe: pilihan ganda · kelas: 1.

> Ada 3 motor. Ada 2 mobil.
>
> Berapa jumlah semua kendaraan?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 6 | Salah: salah menjumlahkan, kelebihan satu |
| B | 3 | Salah: hanya menghitung motor, lupa mobil |
| C | 5 | Benar: 3 motor + 2 mobil = 5 kendaraan |
| D | 4 | Salah: salah menjumlahkan, kurang satu |

- Kunci pada file: **C — 5**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab02.json` / `kelas1-b02-p0084-evaluasi-6a`; siswa hlm. 84, guru hlm. 82; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: soal cerita yang memerlukan satu langkah penjumlahan jumlah kendaraan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 15. `adaec31c66c75d9c825ad888`

Subtopik: Cerita Pengurangan · tipe: pilihan ganda · kelas: 1.

> 9 ... 7
>
> Amati gambar. Lengkapi operasi pengurangannya.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 | Salah: salah menghitung, kurang tepat satu langkah |
| B | 16 | Salah: menjumlahkan 9 dan 7, bukan mencari selisihnya |
| C | 2 | Benar: 9 dikurangi 2 sama dengan 7 |
| D | 7 | Salah: menyalin hasil yang sudah tertulis, bukan mencari bilangan pengurang |

- Kunci pada file: **C — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0095-ayo-berlatih-2c`; siswa hlm. 95, guru hlm. 99; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus mencari bilangan pengurang, bukan langsung hasil pengurangan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 16. `91118c063eea5c139d44fcfe`

Subtopik: Cerita Pengurangan · tipe: pilihan ganda · kelas: 1.

> 7 – 2 = ....
>
> Isilah dengan bilangan yang tepat.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 5 | Benar: 7 dikurangi 2 sama dengan 5 |
| B | 2 | Salah: menjawab bilangan pengurang, bukan hasilnya |
| C | 7 | Salah: lupa mengurangkan, mengulang bilangan mula-mula |
| D | 9 | Salah: menjumlahkan 7 dan 2, bukan mengurangkan |

- Kunci pada file: **A — 5**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0121-evaluasi-1b`; siswa hlm. 121, guru hlm. 113; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: melengkapi hasil pengurangan dari bilangan yang sudah diketahui. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 17. `7aa38a3601f61c91adbf30d4`

Subtopik: Berbagai Cara Melakukan Pengurangan · tipe: pilihan ganda · kelas: 1.

> 6 – 4 = ....
>
> Isilah titik-titik di bawah ini. Tulis hasil pengurangannya.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 10 | Salah: menjumlahkan 6 dan 4, bukan mengurangkan |
| B | 2 | Benar: 6 dikurangi 4 sama dengan 2 |
| C | 6 | Salah: mengulang bilangan gabungan, lupa mengurangkan |
| D | 3 | Salah: salah menghitung, kurang satu langkah |

- Kunci pada file: **B — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0103-ayo-berlatih-1a`; siswa hlm. 103, guru hlm. 102; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus memahami pasangan bilangan (gabungan-bagian) sebelum mengurangkan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 18. `dde0b5654f117861d23c7988`

Subtopik: Berbagai Cara Melakukan Pengurangan · tipe: pilihan ganda · kelas: 1.

> 0 1 2 3 4 5 6 7 8 9 10
>
> Hitunglah. c. 9 – 3 =

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 12 | Salah: menjumlahkan 9 dan 3, bukan mengurangkan |
| B | 3 | Salah: menjawab bilangan pengurang, bukan hasilnya |
| C | 6 | Benar: 9 dikurangi 3 sama dengan 6 |
| D | 5 | Salah: salah menghitung, kurang satu langkah |

- Kunci pada file: **C — 6**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0122-evaluasi-4c`; siswa hlm. 122, guru hlm. 113; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: fakta pengurangan dasar dengan bantuan garis bilangan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 19. `b32a5eeea2898efe65526fe5`

Subtopik: Hubungan Penjumlahan dan Pengurangan · tipe: pilihan ganda · kelas: 1.

> 9 - ... = 7
>
> Isilah titik-titik di bawah ini.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 2 | Benar: 9 dikurangi 2 sama dengan 7 |
| B | 3 | Salah: salah menghitung, kurang tepat satu langkah |
| C | 7 | Salah: menyalin hasil yang sudah tertulis, bukan mencari bilangan pengurang |
| D | 16 | Salah: menjumlahkan 9 dan 7, bukan mencari selisihnya |

- Kunci pada file: **A — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0117-ayo-berlatih-5a`; siswa hlm. 117, guru hlm. 111; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus mencari bilangan pengurang, bukan langsung hasil pengurangan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 20. `f6fcf5836947ff740007f70e`

Subtopik: Hubungan Penjumlahan dan Pengurangan · tipe: pilihan ganda · kelas: 1.

> 2 + 6 = ....
>
> Isilah titik-titik di bawah ini.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 4 | Salah: mengurangkan 6-2, tertukar dengan operasi pengurangan |
| B | 26 | Salah: menggabungkan angka 2 dan 6, bukan menjumlahkan |
| C | 9 | Salah: salah menghitung, kelebihan satu |
| D | 8 | Benar: 2 ditambah 6 sama dengan 8 |

- Kunci pada file: **D — 8**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0117-ayo-berlatih-5b`; siswa hlm. 117, guru hlm. 111; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: fakta penjumlahan dasar tanpa cerita. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 21. `63d056eda46964278255c543`

Subtopik: Soal Cerita Pengurangan · tipe: pilihan ganda · kelas: 1.

> Malosi mempunyai 9 kelereng. Malosi memberi Kira 2 kelereng. Malosi juga memberi Upe 4 kelereng.
>
> Berapakah sisa kelereng Malosi?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 kelereng | Benar: 9 kelereng dikurangi 2 (untuk Kira) dikurangi 4 (untuk Upe) = 3 kelereng |
| B | 7 kelereng | Salah: hanya mengurangkan pemberian untuk Kira, lupa pemberian untuk Upe |
| C | 5 kelereng | Salah: hanya mengurangkan pemberian untuk Upe, lupa pemberian untuk Kira |
| D | 15 kelereng | Salah: menjumlahkan semua bilangan, bukan mengurangkan |

- Kunci pada file: **A — 3 kelereng**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0120-ayo-berlatih-5`; siswa hlm. 120, guru hlm. 113; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **4/5**; alasan sumber: soal cerita dua langkah, mengurangkan dua kali secara berurutan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 22. `9948cc37d48fcfe7ef094209`

Subtopik: Soal Cerita Pengurangan · tipe: pilihan ganda · kelas: 1.

> Ibu mempunyai 6 telur. Sebanyak 2 telur milik Ibu pecah.
>
> Berapakah sisa telur Ibu sekarang?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 3 telur | Salah: salah menghitung, kurang satu langkah |
| B | 8 telur | Salah: menjumlahkan 6 dan 2, bukan mengurangkan |
| C | 4 telur | Benar: 6 telur dikurangi 2 yang pecah = 4 telur |
| D | 6 telur | Salah: lupa mengurangkan, memakai bilangan mula-mula |

- Kunci pada file: **C — 4 telur**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab03.json` / `kelas1-b03-p0123-evaluasi-7`; siswa hlm. 123, guru hlm. 114; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: soal cerita, perlu menerjemahkan kalimat menjadi operasi pengurangan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 23. `355049fbd1c523a25cd2de3d`

Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk · tipe: pilihan ganda · kelas: 1.

> Pasangkan yang bentuknya sama dengan gambar berikut.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Bentuk bintang | Salah: bentuk pengecoh yang tidak ada pada gambar manapun di soal ini |
| B | Segi empat | Salah: mengira potongan buah yang dipotong lurus selalu berbentuk segi empat |
| C | Segitiga | Benar: Potongan semangka berbentuk irisan baji (wedge) yang menyerupai segitiga. |
| D | Bentuk lengkung | Salah: terpengaruh sisi kulit semangka yang melengkung, bukan bentuk irisan keseluruhan |

- Kunci pada file: **C — Segitiga**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0134-ayo-berlatih-1a`; siswa hlm. 134, guru hlm. 123; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: mengenali satu bentuk dasar pada gambar benda sehari-hari (satu langkah identifikasi). Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0134-03.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 24. `83dd4d12892fc170e56f4e1b`

Subtopik: Mendeskripsikan Benda Berdasarkan Bentuk · tipe: pilihan ganda · kelas: 1.

> Pasangkan bentuk dengan namanya. Bangun keempat dari atas.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Bentuk lengkung | Benar: Bangun keempat (dari atas) adalah lingkaran merah, tidak bersudut dan sisinya melengkung. |
| B | Bentuk bintang | Salah: bentuk pengecoh yang tidak dipelajari di bab ini |
| C | Segi empat | Salah: keliru menghitung sisi bangun bulat sebagai empat sisi lurus |
| D | Segitiga | Salah: keliru mengira bangun tanpa sudut ini punya sudut runcing |

- Kunci pada file: **A — Bentuk lengkung**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0153-evaluasi-2d`; siswa hlm. 153, guru hlm. 131; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: mengingat langsung nama bentuk bangun datar standar. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 4/4 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0153-01.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0153-02.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0153-03.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0153-04.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 25. `98891851d1e28d6d8482ab94`

Subtopik: Mengelompokkan Benda · tipe: pilihan ganda · kelas: 1.

> Lingkari jawaban yang benar. Bangun yang satu kelompok dengan gambar di atas.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Persegi panjang berwarna ungu | Salah: mengira bentuk segi empat termasuk satu kelompok karena warnanya sama dengan gambar acuan |
| B | Segitiga terbalik berwarna ungu | Benar: Ketiga bangun acuan (ungu, oranye, merah muda) sama-sama berbentuk segitiga meski warna dan ukurannya berbeda, jadi bangun yang satu kelompok (sebentuk) adalah segitiga. |
| C | Persegi berwarna ungu | Salah: memilih berdasarkan warna yang sama dengan salah satu opsi, bukan berdasarkan bentuk |
| D | Oval berwarna ungu | Salah: memilih berdasarkan warna, bukan bentuk segitiga pada ketiga gambar acuan |

- Kunci pada file: **B — Segitiga terbalik berwarna ungu**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0143-ayo-berlatih-1a`; siswa hlm. 143, guru hlm. 127; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus mengabaikan variasi warna dan ukuran tiga segitiga acuan, lalu memilih opsi yang sebentuk (dua langkah: kenali pola lalu cocokkan). Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `butuh_gambar`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 4/4 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0143-05.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0143-07.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0143-08.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0143-09.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 26. `7bde28fb9ff374327ad9c3ae`

Subtopik: Mengelompokkan Benda · tipe: pilihan ganda · kelas: 1.

> Bangun yang satu warna dengan gambar di atas.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Persegi berwarna ungu | Salah: memilih berdasarkan kemiripan tidak relevan, warnanya tidak sama (ungu, bukan merah muda) |
| B | Oval berwarna hijau | Salah: warnanya tidak sama dengan gambar acuan yang merah muda |
| C | Persegi panjang berwarna biru | Salah: warnanya berbeda dari gambar acuan meski pernah muncul sebagai bentuk segi empat sebelumnya |
| D | Segitiga terbalik berwarna merah muda | Benar: Ketiga bangun acuan (persegi panjang, segitiga, persegi panjang) sama-sama berwarna merah muda, jadi bangun yang satu warna adalah segitiga merah muda. |

- Kunci pada file: **D — Segitiga terbalik berwarna merah muda**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0144-ayo-berlatih-1b`; siswa hlm. 144, guru hlm. 127; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: satu langkah: mencocokkan warna gambar acuan dengan opsi. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `butuh_gambar`, `kunci_guru_dari_png`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0144-00.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 27. `aaf396a280df35704272b0d3`

Subtopik: Menyusun dan Mengurai Bentuk Bangun · tipe: pilihan ganda · kelas: 1.

> Hitunglah banyaknya bentuk bangun pada gambar berikut. Bentuk lengkung ada berapa?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 6 | Salah: menghitung dua kali salah satu bentuk bulat pada tubuh |
| B | 8 | Salah: tertukar dengan jumlah bentuk segi empat pada gambar yang sama |
| C | 4 | Salah: kurang menghitung satu bagian, misalnya salah satu bercak bulat pada badan |
| D | 5 | Benar: Bentuk lengkung pada gambar anjing: 2 mata (titik), 1 telinga kanan (oval), dan 2 bercak bulat di badan = 5. |

- Kunci pada file: **D — 5**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0150-ayo-berlatih-2a`; siswa hlm. 150, guru hlm. 130; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: menghitung tiap bagian pada gambar gabungan (anjing) memerlukan ketelitian mengenali semua bentuk lengkung yang tersembunyi. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 9/9 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-04.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-05.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-06.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-07.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-08.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-09.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-10.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-11.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 28. `595d20d8c4a6f9418dc496b0`

Subtopik: Menyusun dan Mengurai Bentuk Bangun · tipe: pilihan ganda · kelas: 1.

> Hitunglah banyaknya bentuk bangun pada gambar berikut. Segitiga ada berapa?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 8 | Salah: tertukar dengan jumlah bentuk segi empat pada gambar yang sama |
| B | 0 | Salah: tidak menyadari bahwa ekor anjing berbentuk segitiga |
| C | 1 | Benar: Hanya ekor anjing yang berbentuk segitiga = 1. |
| D | 2 | Salah: menghitung ujung telinga kiri yang meruncing sebagai segitiga tambahan |

- Kunci pada file: **C — 1**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab04.json` / `kelas1-b04-p0150-ayo-berlatih-2c`; siswa hlm. 150, guru hlm. 130; status kunci sumber `cocok`, status ekstraksi `needs_review_soal`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: menghitung tiap bagian pada gambar gabungan (anjing) memerlukan ketelitian mengenali bentuk segitiga yang jumlahnya sedikit. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `pertanyaan_disesuaikan_untuk_pg`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 9/9 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0150-03.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-04.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-05.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-06.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-07.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-08.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-09.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-10.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0150-11.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 29. `4d125a6ed9a2701db41cdcd1`

Subtopik: Menghitung, Membaca, dan Menulis Bilangan · tipe: pilihan ganda · kelas: 1.

> Isilah dengan bilangan yang benar.
>
> 10 ditambah 3 menjadi ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 14 | Salah: keliru satu angka lebih besar saat menghitung maju dari 10 |
| B | 12 | Salah: keliru satu angka lebih kecil saat menghitung maju dari 10 |
| C | 31 | Salah: tertukar posisi angka puluhan dan satuan (13 dibalik jadi 31) |
| D | 13 | Benar: 10 ditambah 3 sama dengan 13 (10+3=13) |

- Kunci pada file: **D — 13**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0167-ayo-berlatih-5a`; siswa hlm. 167, guru hlm. 141; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: satu operasi penjumlahan langsung dengan 10 sebagai salah satu suku. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 30. `fbc23bca48392d3c678c3beb`

Subtopik: Menghitung, Membaca, dan Menulis Bilangan · tipe: pilihan ganda · kelas: 1.

> Isilah titik-titik berikut.
>
> 8 ditambah 10 menjadi ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 18 | Benar: 8 ditambah 10 sama dengan 18 (8+10=18) |
| B | 810 | Salah: menuliskan gabungan angka 8 dan 10, bukan menjumlahkannya |
| C | 19 | Salah: keliru satu angka lebih besar saat menghitung maju dari 8 |
| D | 17 | Salah: keliru satu angka lebih kecil saat menghitung maju dari 8 |

- Kunci pada file: **A — 18**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0182-evaluasi-2b`; siswa hlm. 182, guru hlm. 150; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: satu operasi penjumlahan langsung dengan 10 sebagai salah satu suku. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 31. `4953bd9e508059b6896af5e5`

Subtopik: Menghitung Maju dan Mundur · tipe: pilihan ganda · kelas: 1.

> Isilah titik-titik berikut.
>
> 15, 14, ...., ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 14, 13 | Salah: mengulang angka 14 alih-alih melanjutkan turun ke 13 dan 12 |
| B | 16, 17 | Salah: menghitung maju, bukan mundur, dari 15 |
| C | 12, 13 | Salah: urutan dua angka terakhir tertukar (seharusnya turun, bukan naik) |
| D | 13, 12 | Benar: urutan menghitung mundur dari 15 adalah 15, 14, 13, 12 |

- Kunci pada file: **D — 13, 12**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0171-ayo-berlatih-1b`; siswa hlm. 171, guru hlm. 144; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: melengkapi dua bilangan berurutan pada barisan hitung mundur. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 32. `02bd8bfdfd682bd80aa5f426`

Subtopik: Menghitung Maju dan Mundur · tipe: pilihan ganda · kelas: 1.

> Lengkapi urutan bilangan berikut dan warnailah.
>
> 20, ...., 18

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 18 | Salah: mengulang angka terakhir, bukan bilangan di antaranya |
| B | 19 | Benar: urutan bilangan mundur 20, 19, 18 turun satu-satu |
| C | 21 | Salah: naik, bukan turun, dari 20 |
| D | 17 | Salah: terlalu jauh turun, melewati 18 |

- Kunci pada file: **B — 19**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0172-ayo-berlatih-2b`; siswa hlm. 172, guru hlm. 144; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: melengkapi satu bilangan yang hilang di tengah barisan hitung mundur sederhana. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 33. `fb13c7e49793c36315b9e324`

Subtopik: Nilai Tempat · tipe: pilihan ganda · kelas: 1.

> Isilah titik-titik dalam tabel. Lengkapi juga nilai tempatnya.
>
> .... puluhan dan .... satuan = ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 1 puluhan dan 5 satuan = 15 | Benar: gambar c menunjukkan 1 rak berisi 10 telur dan 5 telur lepas, jadi 1 puluhan dan 5 satuan = 15 |
| B | 0 puluhan dan 15 satuan = 15 | Salah: tidak mengelompokkan 10 telur dalam rak sebagai 1 puluhan |
| C | 1 puluhan dan 6 satuan = 16 | Salah: salah hitung telur lepas, kelebihan satu |
| D | 1 puluhan dan 4 satuan = 14 | Salah: salah hitung telur lepas, kurang satu |

- Kunci pada file: **A — 1 puluhan dan 5 satuan = 15**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0175-ayo-berlatih-1c`; siswa hlm. 175, guru hlm. 147; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: menghitung banyak benda pada gambar terlebih dahulu baru menentukan puluhan dan satuannya. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0175-03.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 34. `daa41e2808537d493a6c0994`

Subtopik: Nilai Tempat · tipe: pilihan ganda · kelas: 1.

> Hitunglah dan isi tabelnya.
>
> Nilai tempat 14 = .... puluhan dan .... satuan

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 1 puluhan dan 4 satuan | Benar: 14 terdiri atas 1 puluhan (10) dan 4 satuan, karena 10+4=14 |
| B | 1 puluhan dan 3 satuan | Salah: salah hitung satuan, seharusnya 4 bukan 3 |
| C | 4 puluhan dan 1 satuan | Salah: tertukar posisi angka puluhan dan satuan |
| D | 0 puluhan dan 14 satuan | Salah: tidak mengelompokkan 10 sebagai 1 puluhan |

- Kunci pada file: **A — 1 puluhan dan 4 satuan**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0183-evaluasi-5a`; siswa hlm. 183, guru hlm. 151; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: mengurai satu bilangan dua angka menjadi puluhan dan satuan secara langsung. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 35. `76bd2315ce21573dfa2ea8d7`

Subtopik: Membandingkan Bilangan · tipe: pilihan ganda · kelas: 1.

> Perhatikan bilangan berikut. 13 11 18
>
> Urutan mulai dari bilangan terkecil: .... , .... , ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 13, 11, 18 | Salah: tidak diurutkan, hanya menyalin urutan asal penyebutan |
| B | 11, 13, 18 | Benar: bilangan 13, 11, 18 diurutkan naik: 11 < 13 < 18 |
| C | 11, 18, 13 | Salah: urutan benar di awal tapi dua bilangan terakhir tertukar |
| D | 18, 13, 11 | Salah: menuliskan urutan dari terbesar, bukan dari terkecil |

- Kunci pada file: **B — 11, 13, 18**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0180-ayo-berlatih-4a`; siswa hlm. 180, guru hlm. 149; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: membandingkan dan mengurutkan tiga bilangan dua angka sekaligus. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 36. `84e373946789a200e6b5203a`

Subtopik: Membandingkan Bilangan · tipe: pilihan ganda · kelas: 1.

> Malosi mempunyai 13 bola. Wei mempunyai 11 bola. Kira mempunyai 10 bola.
>
> Urutan banyak bola dari yang terkecil: .... , .... , ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 13, 11, 10 | Salah: urutan dari terbesar, bukan dari terkecil |
| B | 10, 13, 11 | Salah: urutan benar di awal tapi dua bilangan terakhir tertukar |
| C | 11, 10, 13 | Salah: dua bilangan pertama tertukar urutannya |
| D | 10, 11, 13 | Benar: urutan banyak bola dari yang paling sedikit: Kira (10), Wei (11), Malosi (13) |

- Kunci pada file: **D — 10, 11, 13**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab05.json` / `kelas1-b05-p0184-evaluasi-8c`; siswa hlm. 184, guru hlm. 151; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen cocok. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: membandingkan dan mengurutkan tiga jumlah dari cerita singkat. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 37. `31e0c54a133ed9b166d1ed06`

Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih · tipe: pilihan ganda · kelas: 1.

> Malosi mempunyai 5 kelereng. Halim mempunyai 2 kelereng lebihnya dari Malosi.
>
> Berapakah selisih banyak kelereng Halim dan Malosi?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 7 | Salah: menjawab banyak kelereng Halim, bukan selisihnya |
| B | 9 | Salah: menjumlahkan 7 dan 2, bukan mencari selisih |
| C | 5 | Salah: menjawab banyak kelereng Malosi, bukan selisihnya |
| D | 2 | Benar: banyak kelereng Halim = 5 + 2 = 7, selisih Halim dan Malosi = 7 - 5 = 2 |

- Kunci pada file: **D — 2**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0194-ayo-berlatih-7b`; siswa hlm. 194, guru hlm. 160; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: dua langkah: menghitung banyak kelereng Halim dulu, baru mencari selisihnya dengan Malosi. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 38. `fafff0345aa730c0722fc259`

Subtopik: Mengenal Konsep Lebih dari, Kurang dari, dan Selisih · tipe: pilihan ganda · kelas: 1.

> Hari Minggu telah tiba. Tika membantu Ibu memasak di dapur. Mereka membuat donat. Tika membantu Ibu menghias donat. Ibu menghias 7 kue donat. Tika menghias 6 donat. Tika sangat senang.
>
> Siapa yang memiliki donat lebih banyak?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Tidak bisa ditentukan | Salah: tidak membandingkan angka yang sudah diberikan di cerita |
| B | Sama banyak | Salah: mengira 7 dan 6 sama banyak |
| C | Ibu | Benar: Ibu menghias 7 donat, lebih banyak dari 6 donat Tika |
| D | Tika | Salah: tertukar, memilih pihak yang donatnya lebih sedikit |

- Kunci pada file: **C — Ibu**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0189-membantu-ibu-1`; siswa hlm. 189, guru hlm. 157; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **1/5**; alasan sumber: membandingkan dua bilangan yang sudah diberikan langsung (7 dan 6). Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **membandingkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 39. `4a1c88e1d656ed6e318fbc08`

Subtopik: Penjumlahan yang Hasilnya kurang dari 20 · tipe: pilihan ganda · kelas: 1.

> Halim mempunyai 11 kelereng. Malosi mempunyai 6 kelereng.
>
> Berapa jumlah kelereng mereka?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 18 | Salah: kelebihan satu saat menghitung |
| B | 16 | Salah: kekurangan satu saat menghitung |
| C | 5 | Salah: mengurangkan 11 - 6 alih-alih menjumlahkan |
| D | 17 | Benar: 11 + 6 = 17 |

- Kunci pada file: **D — 17**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0200-ayo-berlatih-4`; siswa hlm. 200, guru hlm. 164; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: soal cerita, perlu menerjemahkan konteks menjadi operasi penjumlahan dulu. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 40. `c5a941d72ce972bb9d49a4cc`

Subtopik: Penjumlahan yang Hasilnya kurang dari 20 · tipe: pilihan ganda · kelas: 1.

> Hitunglah operasi penjumlahan berikut. Gunakan cara yang paling mudah.
>
> 14 + 5 = ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 19 | Benar: 14 + 5 = 19 |
| B | 9 | Salah: hanya menjumlahkan satuannya (4+5), lupa nilai puluhan |
| C | 20 | Salah: kelebihan satu saat menghitung |
| D | 14 | Salah: lupa menjumlahkan, hanya mengulang bilangan pertama |

- Kunci pada file: **A — 19**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0206-evaluasi-4d`; siswa hlm. 206, guru hlm. 168; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: satu operasi penjumlahan langsung dari bilangan yang diberikan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung, menerapkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 41. `54e65cf97cc65f3ef126daef`

Subtopik: Pengurangan yang Hasilnya Kurang dari 20 · tipe: pilihan ganda · kelas: 1.

> Ibu membeli 13 bolu kukus. Malosi memakan 2 bolu kukus.
>
> Berapakah sisa bolu kukus Ibu sekarang?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 10 | Salah: kekurangan satu saat menghitung |
| B | 11 | Benar: 13 - 2 = 11 |
| C | 15 | Salah: menjumlahkan 13+2 alih-alih mengurangkan |
| D | 12 | Salah: kelebihan satu saat menghitung |

- Kunci pada file: **B — 11**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0204-ayo-berlatih-4`; siswa hlm. 204, guru hlm. 167; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: soal cerita, perlu menerjemahkan konteks menjadi operasi pengurangan dulu. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 42. `3dbc40f08ab7c63a376fc3e5`

Subtopik: Pengurangan yang Hasilnya Kurang dari 20 · tipe: pilihan ganda · kelas: 1.

> Hitunglah operasi pengurangan berikut. Gunakan cara yang paling mudah.
>
> 15 – 4 = ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 12 | Salah: kekurangan satu langkah saat menghitung mundur |
| B | 11 | Benar: 15 - 4 = 11 |
| C | 19 | Salah: menjumlahkan 15+4 alih-alih mengurangkan |
| D | 10 | Salah: kelebihan satu langkah saat menghitung mundur |

- Kunci pada file: **B — 11**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab06.json` / `kelas1-b06-p0206-evaluasi-5d`; siswa hlm. 206, guru hlm. 168; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: satu operasi pengurangan langsung dari bilangan yang diberikan. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **menghitung, menerapkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 43. `ff83d65211d6e4aa98e13b06`

Subtopik: Membandingkan dan Mengurutkan Panjang Benda · tipe: pilihan ganda · kelas: 1.

> 4. Perhatikan gambar berikut. A B C
>
> Urutan bunga dari paling pendek: ...., ...., ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | B, C, A | Salah: urutan terbalik, dimulai dari yang paling tinggi |
| B | C, A, B | Salah: tertukar posisi bunga A dan C |
| C | A, C, B | Benar: Urutan tinggi bunga dari yang terpendek adalah A, lalu C, lalu B (paling tinggi). |
| D | A, B, C | Salah: urutan tidak sesuai, menaruh B (paling tinggi) di posisi tengah |

- Kunci pada file: **C — A, C, B**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab07.json` / `kelas1-b07-p0218-ayo-berlatih-4c`; siswa hlm. 218, guru hlm. 177; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **4/5**; alasan sumber: menyusun urutan tiga benda sekaligus berdasarkan tinggi. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 5/5 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0218-01.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0218-02.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0218-03.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0218-04.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0218-05.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 44. `dc65bbd6611c904972206f6c`

Subtopik: Membandingkan dan Mengurutkan Panjang Benda · tipe: pilihan ganda · kelas: 1.

> 7. C A B
>
> Burung yang terbang paling tinggi adalah ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Ketiga burung terbang sama tinggi | Salah: tidak memperhatikan perbedaan posisi yang jelas pada gambar |
| B | C | Benar: Burung C terbang di posisi paling tinggi di antara ketiga burung pada gambar. |
| C | B | Salah: burung ini justru terbang paling rendah |
| D | A | Salah: burung ini berada di posisi tengah, bukan yang paling tinggi |

- Kunci pada file: **B — C**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab07.json` / `kelas1-b07-p0219-ayo-berlatih-7b`; siswa hlm. 219, guru hlm. 177; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: membandingkan posisi tiga benda untuk menentukan yang paling tinggi. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0219-07.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 45. `75434d44f2b377da3027e153`

Subtopik: Mengukur Panjang Benda · tipe: pilihan ganda · kelas: 1.

> 4. Temukan panjang pensil berikut. A B C. Panjang pensil A = 4 kotak. Panjang pensil B = 8 kotak. Panjang pensil C = 5 kotak.
>
> Urutan pensil dari paling pendek: ...., ...., ....

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | A, C, B | Benar: Urutan panjang pensil dari yang terpendek adalah A (4 kotak), C (5 kotak), lalu B (8 kotak). |
| B | A, B, C | Salah: urutan tidak sesuai, menaruh B (paling panjang) di posisi tengah |
| C | B, C, A | Salah: urutan terbalik, dimulai dari yang paling panjang |
| D | C, A, B | Salah: tertukar posisi pensil A dan C |

- Kunci pada file: **A — A, C, B**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab07.json` / `kelas1-b07-p0225-ayo-berlatih-4h`; siswa hlm. 225, guru hlm. 180; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **4/5**; alasan sumber: menyusun urutan tiga hasil hitung sekaligus. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0225-04.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 46. `62785ac6ff0622ab70a94b13`

Subtopik: Mengukur Panjang Benda · tipe: pilihan ganda · kelas: 1.

> 6. Temukan panjang pita berikut. A B C. Panjang pita B = 5 kotak. Panjang pita C = 4 kotak.
>
> Pita B lebih .... dari pita C.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | panjang | Benar: Pita B adalah 5 kotak, lebih besar dari pita C yang 4 kotak, sehingga pita B lebih panjang. |
| B | pendek | Salah: tertukar arah perbandingan, padahal B lebih besar dari C |
| C | tinggi | Salah: memakai kata pembanding dimensi yang salah untuk benda mendatar |
| D | besar | Salah: memakai kata pembanding ukuran yang tidak sesuai konteks panjang |

- Kunci pada file: **A — panjang**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab07.json` / `kelas1-b07-p0228-evaluasi-6e`; siswa hlm. 228, guru hlm. 181; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: membandingkan dua hasil hitung untuk menentukan kata pembanding yang tepat. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `notasi_dari_png`, `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 1/1 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0228-03.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 47. `5e007b54e25f6f72efa82174`

Subtopik: Mengelompokkan Data · tipe: pilihan ganda · kelas: 1.

> Amati gambar buah-buahan. Lengkapi daftarnya. Daftar Buah-buahan: Ada ... buah jeruk. Ada ... buah apel. Ada ... buah mangga.
>
> Buah yang paling banyak adalah ...

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Apel | Salah: apel berjumlah 4, jumlah paling sedikit, bukan terbanyak |
| B | Mangga | Benar: hasil hitung gambar: jeruk 5, apel 4, mangga 6, sehingga mangga paling banyak |
| C | Jambu | Salah: jambu tidak ada dalam daftar buah pada gambar |
| D | Jeruk | Salah: jeruk berjumlah 5, bukan yang terbanyak |

- Kunci pada file: **B — Mangga**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab08.json` / `kelas1-b08-p0238-ayo-berlatih-1a`; siswa hlm. 238, guru hlm. 190; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **3/5**; alasan sumber: harus menghitung gambar buah tiga jenis dari ilustrasi lalu menentukan yang terbanyak. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 15/15 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0238-11.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-12.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-13.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-14.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-15.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-16.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-17.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-18.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-19.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-20.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-21.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-22.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-23.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-24.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0238-25.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 48. `17ba235cdc9fddc600303514`

Subtopik: Mengelompokkan Data · tipe: pilihan ganda · kelas: 1.

> Perhatikan tabel dan jawablah pertanyaannya. Tabel Kue Kesukaan: Nama Kue Kue Talam Kue Cucur Kue Lapis Kue Bugis, Banyak anak 5 3 5 6.
>
> Apa nama kue yang paling disukai?

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Kue Cucur | Salah: kue cucur hanya disukai 3 anak, jumlah paling sedikit |
| B | Kue Lapis | Salah: kue lapis hanya disukai 5 anak, bukan yang terbanyak |
| C | Kue Talam | Salah: kue talam hanya disukai 5 anak, bukan yang terbanyak |
| D | Kue Bugis | Benar: kue bugis disukai 6 anak, angka terbesar di tabel |

- Kunci pada file: **D — Kue Bugis**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab08.json` / `kelas1-b08-p0249-evaluasi-2c`; siswa hlm. 249, guru hlm. 196; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: membandingkan empat nilai pada tabel untuk menentukan yang terbesar. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 49. `e7d8a29f2e3a28f99529dfc8`

Subtopik: Diagram Gambar · tipe: pilihan ganda · kelas: 1.

> Diagram berikut menunjukkan jenis buah kesukaan anak-anak. Diagram Buah Kesukaan. Gambar mewakili 1 anak. Lengkapi setiap kalimat berikut.
>
> Anak yang suka belimbing ... lebih banyak dari anak yang suka apel.

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | 2 | Salah: salah menghitung selisih, kurang satu dari hasil sebenarnya |
| B | 3 | Benar: belimbing 7 dikurangi apel 4 sama dengan 3 |
| C | 4 | Salah: tertukar dengan jumlah anak suka apel, bukan selisihnya |
| D | 1 | Salah: salah menghitung selisih, jauh lebih kecil dari hasil sebenarnya |

- Kunci pada file: **B — 3**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab08.json` / `kelas1-b08-p0246-ayo-berlatih-1f`; siswa hlm. 246, guru hlm. 195; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **4/5**; alasan sumber: membaca dua kolom diagram lalu menghitung selisihnya. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`, `butuh_gambar`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 4/4 file tersedia; `images/kelas1_panduan_siswa_kelas1.pdf-0246-04.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0246-05.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0246-06.png`, `images/kelas1_panduan_siswa_kelas1.pdf-0246-07.png`. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **membandingkan**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

### 50. `8812007076d1edea9f050f6f`

Subtopik: Diagram Gambar · tipe: pilihan ganda · kelas: 1.

> Ibu membeli buah di pasar. Ibu membeli 6 jeruk, 3 apel, 4 mangga, dan 5 belimbing. Warnailah sesuai dengan banyak buah. Lengkapi dengan jawaban yang benar.
>
> Buah yang paling sedikit adalah ...

| Opsi | Isi | Catatan sumber |
|---|---|---|
| A | Belimbing | Salah: belimbing berjumlah 5, bukan yang paling sedikit |
| B | Jeruk | Salah: jeruk berjumlah 6, jumlah paling banyak |
| C | Apel | Benar: apel berjumlah 3, paling sedikit dibanding jeruk 6, mangga 4, belimbing 5 |
| D | Mangga | Salah: mangga berjumlah 4, bukan yang paling sedikit |

- Kunci pada file: **C — Apel**. Pemeriksaan otomatis: menunjuk satu opsi; kebenaran matematis belum diverifikasi independen.
- Provenance: `bab08.json` / `kelas1-b08-p0251-evaluasi-4e`; siswa hlm. 251, guru hlm. 196; status kunci sumber `cocok`, status ekstraksi `draft`, jawaban agen berbeda. Ini bukti ekstraksi, belum verifikasi ahli.
- Perkiraan kesulitan agen ekstraksi: **2/5**; alasan sumber: membandingkan empat angka buah untuk menentukan yang paling sedikit. Skor ini berbeda dari head `intendedDifficulty` IndoBERT.
- Flag ekstraksi: `ada_stimulus`.
- Validasi struktur: **lulus**; flag: tidak ada.
- Gambar: 0/0 file tersedia; tidak ada referensi. Keberadaan dan kebutuhan semantik gambar perlu diperiksa pada review isi.
- KKO terdeteksi: **tidak terdeteksi**. KKO hanya fitur teks; tidak menentukan head kognitif.
- Kualifikasi konten: **perlu review isi/kunci/solusi oleh manusia**.
- IndoBERT: `mathCognitiveDomain=—`, `knowledgeDimension=—`, `intendedDifficulty=—`; confidence dan probabilitas ketiga head `—` (artefak terlatih belum ada).
- Gemini: `silverLabel=—`, `review=—`, `N-run=—`, penggunaan token `0` untuk laporan ini (belum dipanggil).

## Cara IndoBERT akan bekerja setelah artefak tersedia

1. Import sumber sebagai versi konten tetap. `kelas_id` yang kosong diisi sebagai kelas 1 berdasarkan lokasi dataset, dengan provenance inferensi tersebut. Stem, opsi, kunci, dan gambar diberi `contentHash`. Revisi soal membuat versi baru.
2. Periksa format, isi, kunci, dan gambar. `jawaban` hanyalah kunci opsi, bukan `verifiedMinimalSolution`. Banyak soal visual tidak dapat dinilai aman dari teks saja.
3. Serialisasi input menjadi `Kelas`, `Topik/Subtopik`, `Tipe`, `Stimulus`, `Soal`, `Pilihan`, `Solusi minimum terverifikasi` jika tersedia, `KKO`, dan transkripsi visual terverifikasi. Jangan mengarang field yang belum ada.
4. Tokenizer IndoBERT memecah teks ke token, memakai truncation maksimum yang tercatat pada manifest, lalu shared encoder menghasilkan representasi. Tiga head menghasilkan masing-masing 3, 4, dan 3 logits.
5. Probabilitas per head dihitung `softmax(logits / temperature_head)`. Label tertinggi dan probabilitasnya menjadi `calibratedConfidence`. Normalized entropy, truncation, scope, dan provenance menentukan `predict`, `review`, atau `abstain`.
6. Temperature dan threshold harus dipilih pada validation set gold manusia. Tanpa gold, angka probabilitas model bootstrap tidak boleh disebut terkalibrasi atau akurasi ilmiah.

Parameter yang dipakai model: tugas matematika yang benar-benar diminta, struktur operasi, konsep, langkah solusi, hubungan representasi, kelas dan subtopik, opsi, beban visual, serta KKO sebagai sinyal lemah. Label head 1: `knowing/applying/reasoning`; head 2: `factual/conceptual/procedural/metacognitive`; head 3: `Easy/Medium/Hard` sebagai kesulitan yang dimaksud oleh isi soal.

## Cara Gemini akan bekerja

1. Untuk bootstrap tanpa gold, Gemini dapat mengusulkan tiga label sebagai **silver** melalui prompt dan structured JSON. Output menyertakan bukti singkat, alasan dan `abstain` bila soal tidak cukup jelas.
2. Jika N=3 diaktifkan, tiga run model dan konfigurasi yang sama dikumpulkan. 3 sama → konsisten; 2 sama → mayoritas dengan dissent; 1–1–1 atau abstain tanpa mayoritas → antrean review. N=3 mengukur kestabilan Gemini, bukan voting ahli.
3. Setelah IndoBERT benar-benar ada, reviewer Gemini dapat melihat item, prediksi, probabilitas per head dan rubrik; keluarannya `confirm/revise/abstain` per head. Runtime reviewer yang ada tidak dapat menghasilkan hasil ini ketika prediksi IndoBERT belum tersedia.
4. Simpan ID model, versi prompt/rubrik, hash input, response ID, latency, token usage, tiga hasil mentah yang sudah divalidasi, dan keputusan agregat. Jangan menyimpan atau menampilkan API key maupun chain-of-thought.

Gemini yang membentuk silver dan kemudian mereview IndoBERT memberi dua hasil yang tidak independen. Agreement keduanya dapat dipakai untuk diagnosis pipeline, bukan sebagai bukti gold atau kualitas model.

## Batas dan langkah berikutnya

- Semua 50 item memerlukan verifikasi konten dan kunci. Prioritaskan item visual serta stem yang masih merujuk gambar. File gambar tersedia, tetapi isi gambarnya belum diperiksa dalam audit ini.
- Untuk menjalankan klasifikasi IndoBERT, perlu gold/silver dataset yang diberi provenance jelas, training, kalibrasi yang layak, dan artefak manifest terverifikasi. Laporan ini belum memuat angka model karena artefak tidak tersedia.
- Panggilan Gemini memerlukan konfigurasi live dan akan memakai kuota. Laporan ini dihasilkan offline dan tidak mengirim soal atau key ke penyedia.
- Proses berhenti pada paket review manusia. CTT, discrimination index, dan IRT tidak dapat dihitung tanpa data jawaban siswa dan tidak dikerjakan di sini.
