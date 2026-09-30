# Catatan ekstraksi pretest kelas8

## Umum / pola buku
- Flag header `GRAFIK_KOMPLEKS=<angka> (teks polos, WAJIB lihat PNG)` di halaman pembuka
  bab (mis. hal.21, hal.22 Bab 1) = dekorasi vektor berat, konversi PNG dilewati otomatis.
  Isinya biasanya cover/judul bab saja (nama penulis, ISBN, judul, gambar dekorasi) --
  TIDAK ada soal. Cukup baca teks polosnya, tidak perlu render PNG untuk halaman ini.
- Heading subbab di Buku Siswa memakai format `# **A. <Judul>**`, `# **B. ...**`, dst
  (grep `^# \*\*[A-Z]\.` untuk menemukan batas subbab dengan cepat per buku).
- Banyak halaman [M] (RISIKO_MATEMATIKA) untuk notasi akar/pangkat ternyata tetap
  terbaca bersih di Markdown kalau notasinya HTML `<sup>`/`<sub>` biasa (tidak perlu PNG).
  PNG baru wajib untuk pola "pecahan_bersusun" (akar/pecahan bertumpuk, banyak simbol
  `#`, `<u>` yang kacau).
- Bagian "Ayo Berpikir Kritis/Kreatif/Berkomunikasi" di Buku Siswa SEBAGIAN memuat soal
  dengan jawaban pasti dan kuncinya ADA di Buku Guru (bukan cuma metodologi generik) --
  contoh: kartu angka Bab 1 hal.29 "Ayo Berpikir Kreatif" kuncinya ada verbatim di Guru
  hal.52 ("...? Bathari", "...? Dwi"). Jangan langsung anggap soal_terbuka tanpa
  mengecek Buku Guru dulu.
- Bagian "Ayo Berlatih" (bukan "Soal Laihan X.Y") biasanya TIDAK punya kunci di Buku
  Guru -- Guru hanya menjelaskan metodologi kegiatan secara umum per jenis aktivitas
  (definisi "Ayo Berpikir Kritis", dst, bukan kunci per soal). Kunci resmi per subbab
  ada di "Jawaban Soal Laihan 1.1/1.2/1.3" dst.
- Soal "Soal Laihan" di Buku Siswa yang bergambar (pecahan/akar bersusun) WAJIB
  di-render PNG (`convert.py render <buku> siswa <hal>`) karena Markdown-nya kacau total
  (simbol `#`, `<u>`); setelah dirender, teksnya jelas dan bersih.
- Kunci di Buku Guru untuk "Jawaban Soal Laihan X.Y" SERING juga garbled di Markdown
  (format sama seperti soal: "3 2 + 5 2 = 8 2" untuk "3√2+5√2=8√2") padahal PNG-nya
  belum tentu perlu dirender kalau pola kesalahan konversinya konsisten dan bisa
  dicocokkan lewat pola item lain di halaman yang sama.

## Bab 1 - Bilangan Berpangkat (hal. 21-64)
- Subbab: A=hal.25-45 (Bilangan Berpangkat Bulat), B=hal.46-56 (Bilangan Bentuk Akar),
  C=hal.57-64 (Penulisan Bentuk Baku).
- Kunci Guru Bab 1: p0052 (Ayo Berpikir Kreatif kartu angka), p0083 (Jawaban Soal
  Laihan 1.2, garbled tapi terbaca via pola), p0089-p0090 (Jawaban Soal Laihan 1.3,
  bersih/tidak garbled).
- Soal Laihan 1.1 (hal.44-45) SELURUH butirnya tercetak sebagai gambar pecahan
  berpangkat bersusun -- dilewati, subbab A diwakili oleh "Ayo Berpikir Kreatif" hal.29.
- "Ayo Mencoba" hal.57 (rasionalisasi bentuk akar, 20 butir) seluruhnya
  TEKS_DALAM_GAMBAR yang urutan/pasangannya kacau -- dilewati.
- File `bab01.json`: 6 soal (2/subbab), status_kunci semua "cocok", LOLOS validate
  (0 error, 4 warning -- semua warning [M] false-positive sudah dijelaskan di `catatan`
  tiap soal karena notasinya bersih/tidak perlu PNG).

## Bab 2 - Teorema Pythagoras (hal. 65-116)
- Subbab: A=hal.65-83 (Menemukan Konsep Pythagoras), B=hal.84-96 (Tripel Pythagoras),
  C=hal.96-103 (Segitiga Istimewa), D=hal.104-109 (Penerapan Teorema Pythagoras),
  E=hal.110-116 (Rumus Jarak, Pengayaan). "Soal Laihan 2.1" (p.80-83), "2.2" (p.94-96),
  "2.3" (p.101-103), "2.4" (p.111-112) masing-masing bernomor 1-4/5 KONTINU walau heading
  "Ayo Berpikir Kritis/Kreatif" muncul lagi di tengah nomor (artefak layout, bukan section
  baru) -- treat sebagai satu rangkaian nomor per "Soal Laihan X.Y".
- Kunci Guru Bab 2: p0111-p0113 (Jawaban Soal Laihan 2.1), p0123-p0124 (2.2), p0130-p0132
  (2.3), p0136-p0138 (2.4 + kunci Rumus Jarak intro tidak lengkap), p0138 (Uji Kompetensi
  Bab 2 kunci PG A-D).
- **PENTING: koordinat bertanda negatif SERING hilang saat konversi Markdown Siswa**
  (mis. hal.110 "A(-2,-1)" tercetak jadi "A(2,1)" di .md, tanda minus lenyap). SELALU
  render PNG untuk soal koordinat kartesius sebelum memakai angkanya.
- Ditemukan 2 kasus kunci Buku Guru bab ini SALAH (bukan salah ketik minor, tapi salah
  konsep/tertukar), diverifikasi ulang dengan hitungan manual teliti sebelum menandai
  `tidak_cocok`:
  1. p0095 Soal Laihan 2.2 no.2 (identifikasi tripel Pythagoras a/b/c): kunci Guru hal.124
     bilang a="Tripel", c="Bukan Tripel" -- padahal hasil hitung c²=a²+b² membuktikan
     justru c (6, 2½, 6½) yang tripel (42,25=42,25 persis), sedangkan a (17,24,25) dan
     b (7,11,13) tidak (865≠625 dan 170≠169). Sepertinya tertukar/typo di Buku Guru.
  2. p0111 Soal Laihan 2.4 no.1 (segitiga ABC dari titik A(-1,3),B(4,-2),C(1,-5) siku-siku
     atau bukan?): kunci Guru hal.136 bilang BUKAN siku-siku dengan alasan sisi-sisinya
     "tidak membentuk Tripel Pythagoras" (mensyaratkan bilangan bulat) -- padahal Teorema
     Pythagoras tidak perlu sisi integer. Hitung ulang: AB²=50, BC²=18, CA²=68, dan
     50+18=68 (persis sama) sehingga segitiga itu sebenarnya SIKU-SIKU di B.
  - Pola ini berguna untuk bab lain: kalau soal melibatkan pengecekan "tripel Pythagoras"
    atau "siku-siku atau bukan", JANGAN percaya begitu saja kesimpulan kualitatif Guru --
    hitung ulang c² vs a²+b² dengan teliti karena Buku Guru bab ini beberapa kali keliru
    di soal analitik semacam ini.
- Kunci untuk item yang hanya berupa rumus/angka akhir di dalam GAMBAR PNG Guru (bukan di
  teks Markdown): Soal Laihan 2.4 no.3b (Aldo-Arjuna, jarak 45 langkah) -- markdown guru
  cuma bilang "gunakan Teorema Pythagoras", angka finalnya (36,27,2025,45) hanya ada di
  gambar rumus PNG hal.137. Tandai `kunci_guru.dari_png: true`.
- Bagian intro "E. Rumus Jarak" (p.110, sebelum "Soal Laihan 2.4") berisi 3 sub-pertanyaan
  a/b/c tapi Buku Guru (p.136) TIDAK memberi jawaban tuntas untuk poin b (angka) --
  langsung lompat ke "Jawaban Soal Laihan 2.4". status_kunci "tidak_ada_di_guru" untuk
  kasus begini.
- Banyak "Ayo Mencoba"/"Ayo Bekerja Sama" bab ini betul-betul butuh alat peraga fisik
  (gunting kertas, benang, kertas berpetak) -- p.73-74, p.87-88 -- dilewati semua.
- "Ayo Bereksplorasi" pembuka subbab D (p.104, permainan bentengan) TIDAK PERNAH dijawab
  tuntas secara numerik baik di Siswa maupun Guru (hanya ilustrasi pengantar rumus) --
  dilewati.
- File `bab02.json`: 10 soal (2/subbab A-E), status_kunci: 8 "cocok", 1 "tidak_ada_di_guru",
  1 "tidak_cocok" (sudah diverifikasi lewat hitungan manual, lihat poin kunci salah di
  atas). LOLOS validate (0 error, 0 warning).

## Bab 3 - Persamaan Linier dan Pertidaksamaan Linier Satu Variabel (hal. 117-156)
- Subbab: A=hal.117-132 (Memahami Konsep PLSV, s.d. Soal Laihan 3.1), B=hal.133-140
  (Menyelesaikan PLSV, s.d. Soal Laihan 3.2), C=hal.140-146 (Menemukan Konsep PtLSV,
  s.d. Soal Laihan 3.3), D=hal.146-156 (Menyelesaikan Masalah PtLSV, Soal Laihan 3.4 +
  Uji Kompetensi Bab 3). Subbab D = prasyarat SMP9-B1, diberi 4 soal (bukan 2) termasuk
  1 soal tingkat 5 (Soal Laihan 3.4 no.4b, pembulatan ke atas banyak pengangkutan).
- Kunci Guru Bab 3: p0148 (Ayo Berpikir Kritis kalimat benar/salah), p0154 (Jawaban Soal
  Laihan 3.1), p0161 (3.2), p0165 (3.3), p0170-p0172 (3.4), p0173 (Uji Kompetensi Bab 3
  PG A + esai B).
- **Angka/simbol TERSEMBUNYI walau halaman TIDAK berlabel [M]**: hal.132 Soal Laihan 3.1
  no.1c tercetak di Markdown sebagai "Terdapat 1800 detik dalam 2 jam" (hilang pecahan
  1/2) -- PNG membuktikan aslinya "1800 detik dalam **1/2** jam". Kalau ada pecahan kecil
  menempel di angka lain dan pernyataannya terasa tidak masuk akal secara matematis
  (1800 detik ≠ 2 jam), WAJIB curiga dan render PNG meski halaman tidak berlabel [M]/[T].
- **Pola substitusi simbol pertidaksamaan di seluruh bab (dan mungkin bab lain)**: OCR
  Markdown mengganti `<` -> `1`, `>` -> `2`, `≤` -> `#`, `≥` -> `$` secara KONSISTEN.
  Contoh: "t 1 44" = "t < 44", "a 2 b" = "a > b", "x #-3" = "x ≤ -3", "5 $ ..." = "≥".
  Berguna untuk membaca kunci Guru yang juga garbled dengan pola sama tanpa perlu PNG.
- Statement "Pegunungan Lantimojong terletak di Sulawesi Utara" (hal.123, Ayo Berpikir
  Kritis) ditandai Guru (hal.148) sebagai **bernilai benar** -- padahal secara geografi
  nyata Latimojong berada di Sulawesi Selatan (Enrekang). Karena ini bukan fakta yang
  bisa dihitung ulang (bukan Pythagoras dkk), kunci Guru dipakai apa adanya tanpa
  ditandai `tidak_cocok`; statement ini disingkirkan dari opsi PG (dipakai kalimat 1-4
  saja, hanya kalimat 4 yang benar) supaya tidak ada ambiguitas jawaban.
  - Item angka/variabel yang digabung tanpa spasi (mis. "3x") kadang bikin
  `missing_numbers` validator gagal karena di Markdown sumber tokennya terpisah
  ("3 _x_" -> token "3" dan "x" beda). Kalau stimulus/pertanyaan berisi ekspresi
  seperti ini, tulis dengan spasi ("3 x + 5 = -10") supaya tokenisasi cocok, atau
  gunakan LaTeX `$...$` + `notasi_dari_png` kalau memang berasal dari PNG.
- "Ayo Bereksplorasi" hal.129 (menjodohkan kalimat aljabar ke kategori persamaan/
  pertidaksamaan) dan "Ayo Mencoba" hal.131 (tabel lanjutannya) -- TEKS_DALAM_GAMBAR
  kacau, dilewati. "Ayo Mencoba" hal.133-135 (kelereng+balok di timbangan, tabel 6
  baris) butuh alat peraga fisik, dilewati.
- File `bab03.json`: 10 soal (2/subbab A-C, 4/subbab D), status_kunci semua "cocok".
  LOLOS validate (0 error, 2 warning -- keduanya soal di hal.145 [M] sup/sub palsu-positif,
  flag itu untuk item lain di halaman yang sama (m² pada soal volume kolam), sudah
  dijelaskan di `catatan` masing-masing soal).

## Bab 4 - Relasi dan Fungsi (hal. 157-226)
- Subbab: A=hal.161-181 (Memahami Relasi, s.d. Soal Laihan 4.1), B=hal.182-209
  (Memahami Fungsi, s.d. Soal Laihan 4.2 & 4.3), C=hal.210-226 (Korespondensi
  Satu-satu (Pengayaan), Soal Laihan 4.4 + Uji Kompetensi Bab 4). Heading "C." di
  Markdown Siswa TIDAK memakai format bold biasa (`# **C. ...**`) seperti bab lain,
  tapi teks polos "C. Korespondensi Satu-satu (Pengayaan)" di tengah paragraf
  (hal.210, halaman ini juga GRAFIK_KOMPLEKS+RISIKO_MATEMATIKA tapi ternyata tanpa
  soal) -- grep `^# \*\*[A-Z]\.` TIDAK menemukan batas subbab C, harus dicari manual
  via kata "Korespondensi Satu-satu (Pengayaan)".
- **Tanda kurung kurawal himpunan `{ }` sering tercetak sebagai tanda kutip `"..."`
  di Markdown Siswa bab ini** (bukan pola pertidaksamaan seperti Bab 3), misal
  `_A_ = "2, 3, 4, 6, 8, 10,` untuk `A = {2, 3, 4, 6, 8, 10}`. Aman ditulis ulang
  dengan notasi himpunan standar (dianggap perbaikan notasi matematika, bukan
  parafrase), asal angka/isinya tidak diubah.
- Kunci Guru Bab 4: p0198 (Soal Laihan 4.1, hanya no.1-2 lengkap, no.3-10
  di p0199), p0206-207 (Soal Laihan 4.2 no.1-8, banyak item "diserahkan kepada
  teman Guru"), p0220-221 (Ayo Berkomunikasi banyak fungsi contoh 4!=24 + Soal
  Laihan 4.4 no.1,3,5 dengan kunci pasti; no.2,4,6-10 "diserahkan kepada teman
  Guru"), p0223 (Uji Kompetensi Bab 4 A+B, belum dipakai).
- Banyak sekali item "Ayo Berpikir Kritis/Kreatif" berbentuk debat dua tokoh
  fiksi (mis. Durahman vs Bahrudin, Tasya vs Rosi, Halim vs Mawardi) yang formatnya
  opini/penalaran terbuka -- SEBAGIAN punya jawaban pasti di Buku Guru (mis. hal.177
  kuncinya di guru hal.198, hal.216 kuncinya di guru hal.220-221) tapi tetap
  dilewati karena kuota 2 soal/subbab sudah tercukupi dari Soal Laihan yang lebih
  langsung diverifikasi. Kalau butuh soal tambahan/prasyarat dari bab ini nanti,
  cek dulu daftar `dilewati` di `bab04.json` sebelum membaca ulang halaman siswa.
- Soal-soal dengan jawaban "tentukan nilai fungsi f(x)=..." (nilai fungsi, hal.200-209)
  BANYAK berisi notasi pecahan/pangkat bersusun kacau di Markdown meski halaman tidak
  selalu berlabel [M] tegas (kadang cuma RISIKO_MATEMATIKA ringan) -- kalau perlu
  soal dari area ini nanti, WAJIB render PNG dulu.
- Formula kunci bab ini yang berguna untuk verifikasi mandiri (tanpa perlu PNG):
  banyak fungsi dari A ke B = n(B)^n(A) (dikonfirmasi Guru hal.207 no.8b: 3²=9);
  banyak korespondensi satu-satu A ke B (n(A)=n(B)=n) = n! (dikonfirmasi Guru
  hal.220: 4!=24, dan hal.221: 12!, 9!).
- File `bab04.json`: 6 soal (2/subbab A-C), status_kunci semua "cocok". LOLOS
  validate (0 error, 0 warning) setelah melengkapi seluruh halaman latihan
  tersentuh (soal atau dilewati) -- 22 entri `dilewati` dicatat untuk semua
  "Ayo Berpikir Kritis/Kreatif" opini dan soal terbuka yang tidak dipakai.

## Bab 5 - Persamaan Garis Lurus (hal. 227-274)
- Subbab: A=hal.227-242 (Grafik Persamaan Garis Lurus, s.d. Soal Laihan 5.1),
  B=hal.243-274 (Pengertian Kemiringan, s.d. Soal Laihan 5.2/5.3 + Uji
  Kompetensi Bab 5). Kurikulum (`kurikulum.get('kelas8',5)`) hanya
  mendaftar 2 subbab (A, B) -- B = "Pengertian Kemiringan" memang subbab
  TERAKHIR, jadi valid dipakai sebagai sumber prasyarat SMP9-B1/SMP9-B3;
  diberi 4 soal (bukan 2) termasuk 1 soal tingkat 5 (UK Bab 5 no.5, titik
  sudut persegi panjang PQRS).
- **Uji Kompetensi Bab 5 bagian A (hal.271-273, no.1-5) adalah sumber PALING
  BERKUALITAS untuk subbab B**: sudah berbentuk PG dengan 4 opsi asli buku,
  kuncinya di Guru hal.257 ringkas per huruf ("1. c", "2. a", dst, no.4 disertai
  Alternatif Pembahasan lengkap). No.1 dan no.6-10 tetap harus dilewati karena
  opsi/soalnya berupa grafik (butuh_gambar). Kunci Guru untuk PG di Uji
  Kompetensi HANYA berupa huruf opsi (tidak mengulang angka jawaban) --
  ini akan SELALU memicu WARNING validator "kutipan tidak memuat angka
  jawaban" walau status_kunci sudah benar "cocok"; cukup jelaskan di
  `catatan` per soal (lihat contoh di `bab05.json` no.3 dan no.5), tidak
  perlu diperbaiki.
- Tabel-tabel kemiringan/gradien (Soal Laihan 5.2 no.3, UK Bab 5 no.2, dst)
  di Markdown Siswa SANGAT kacau urutannya (baris/kolom tercampur, angka
  dan huruf bertukar posisi) walau halamannya TIDAK selalu berlabel [M] --
  WAJIB render PNG untuk memastikan pasangan (titik, kemiringan, persamaan)
  per baris sebelum menghitung jawaban sendiri.
- **Koordinat negatif hilang lagi di Markdown Siswa** (pola sama seperti Bab 2):
  hal.252 Soal Laihan 5.2 no.6 "titik (5, 2p) dan (1, p)" di Markdown
  aslinya adalah "(-5, 2p) dan (-1, p)" (terbukti lewat PNG); begitu juga
  no.7a titik "A(2,3)" aslinya "A(-2,3)". SELALU render PNG untuk soal
  koordinat di bab ini juga.
- Untuk menuliskan pertanyaan/stimulus verbatim yang memuat ekspresi
  aljabar TANPA spasi (mis. sumber "_y_ = 2 _x_ - 3" jangan ditulis ulang
  jadi "y = 2x - 3"): validator men-tokenize "2x" jadi SATU token beda dari
  token "2" + "x" di halaman sumber (yang punya spasi) sehingga gagal
  `missing_numbers`. Tulis dengan spasi ("y = 2 x - 3") -- ini menegaskan
  ulang temuan Bab 3, ternyata juga muncul di bab ini pada teks BIASA
  (bukan pertidaksamaan).
- Trik verbatim untuk stimulus tabel yang genuinely kacau di Markdown: taruh
  seluruh isi tabel (angka/persamaan) di dalam blok `$$...$$` (LaTeX), sisakan
  hanya kalimat pengantar asli buku sebagai teks polos. `_LATEX_RE` di
  validator men-strip seluruh isi `$$...$$` sebelum menghitung coverage,
  jadi tabel yang kacau tidak perlu cocok persis, sementara kalimat
  pengantar (yang biasanya bersih di Markdown) tetap dicek verbatim dan
  lolos dengan mudah. Set `notasi_dari_png: true`.
- Banyak "Ayo Bereksplorasi/Berkomunikasi/Berpikir Kritis/Kreatif" di bab ini
  murni analisis kualitatif (menjelaskan makna kemiringan, membandingkan
  grafik, pendapat) tanpa jawaban tunggal -- dilewati semua (lihat
  `dilewati` di `bab05.json`, >25 entri, kebanyakan kategori `soal_terbuka`
  dan `lainnya` untuk yang butuh gambar vektor tanpa file img).
- File `bab05.json`: 6 soal (2 subbab A dari Soal Laihan 5.1, 4 subbab B dari
  Uji Kompetensi Bab 5 no.2-5), status_kunci: 5 "cocok", 1 "tidak_ada_di_guru"
  (Soal Laihan 5.1 no.2, Guru menjawab "diserahkan kepada teman Guru").
  LOLOS validate (0 error, 2 warning -- keduanya kasus kunci UK huruf-saja
  di atas, sudah dijelaskan di `catatan` masing-masing soal).

## Bab 6 - Statistika (hal. 275-344, BAB TERAKHIR kelas8)
- Materi (dan soal latihan) berhenti di hal.308 (Pengayaan no.4); hal.309-344
  hanyalah Index/Daftar Pustaka/Biodata Penulis -- tidak ada soal, aman
  dipakai `halaman_siswa: [275, 308]` meski rentang resmi bab 275-344.
- Subbab: A=hal.279-298 (Pemusatan Data: Modus/Median/Rata-rata, s.d. Soal
  Laihan 6.1), B=hal.298-308 (Penyebaran Data: Jangkauan/Kuartil/Jangkauan
  Kuartil/Simpangan Kuartil, Soal Laihan 6.2 + Uji Kompetensi + Pengayaan).
  B = subbab TERAKHIR -> dipakai sebagai prasyarat SMP9-B4, diberi 4 soal
  (bukan 2), termasuk 1 soal tingkat 5 (Soal Laihan 6.2 no.3, tekanan darah).
- Cek `data/processed/pretest_md/kelas8/siswa/index.json` field
  `pages[<no>].latihan` untuk tahu PERSIS halaman mana yang wajib
  disentuh (soal/dilewati) supaya validator tidak warning -- jauh lebih
  murah daripada menyisir INDEX.md manual. Bab ini hanya 7 halaman
  ber-flag: 283, 292, 294, 295, 299, 301, 303 (Uji Kompetensi & Pengayaan
  di hal.304-308 TIDAK diberi flag `latihan` sama sekali walau berisi soal
  bernomor -- validator tidak akan warning meski tidak disentuh, tapi tetap
  baik didokumentasikan di `dilewati` untuk sesi berikutnya).
- **Metode kuartil buku ini = "belah dua" (exclusive median-of-halves):**
  urutkan data, cari median (Q2) dari SELURUH data, lalu Q1 = median
  separuh bawah dan Q3 = median separuh atas (kalau n genap, separuh
  bawah/atas TIDAK mengikutsertakan Q2 sama sekali, langsung dibagi rata
  n/2 & n/2). BUKAN interpolasi (n+1)/4. Diverifikasi cocok persis dengan
  kunci Guru di 3 soal berbeda (Soal Laihan 6.2 no.1a, 1b, no.2 data
  berkelompok) sebelum dipakai untuk memeriksa kunci Guru yang ternyata
  salah (lihat poin berikut). Berguna kalau bab statistika kelas lain
  (kelas7/kelas9) memakai metode kuartil yang sama.
- **Kunci Guru Bab 6 no.3 (Soal Laihan 6.2, tekanan darah 16 data) SALAH
  HITUNG**: Guru hal.288 bilang Q3=174,5 (jangkauan=44, simpangan=22).
  Data terurut: 120,124,124,126,135,150,165,165,165,170,174,175,176,180,
  182,185. Separuh atas (8 data terakhir) = 165,170,174,175,176,180,182,185
  -> median = (175+176)/2 = **175,5**, bukan 174,5. Q1 dan Q2 pada soal yang
  sama SUDAH cocok persis dengan Guru (130,5 dan 165) memakai metode yang
  sama, jadi errornya murni di Q3 (Guru kemungkinan salah membaca pasangan
  tengah). Ditandai `tidak_cocok`, kunci Guru yang salah dipakai sebagai
  salah satu distraktor (`alasan`: "kesalahan yang persis sama dengan Buku
  Guru") -- pola ini efektif untuk distraktor yang benar-benar meniru
  miskonsepsi nyata (di sini miskonsepsi si penulis kunci sendiri).
- Data mentah di Markdown Siswa kadang kehilangan TANDA KOMA antar-angka
  (bukan hilang angkanya): Soal Laihan 6.2 no.1b tercetak "...75, 80 65"
  (harusnya "...75, 80, 65", 14 data). Dipastikan aman (bukan salah baca)
  karena hasil hitung kuartil dengan 14 data itu PERSIS cocok dengan kunci
  Guru (Q1=65, Q2=67,5, Q3=80). Kalau ragu apakah dua angka berdempetan
  tanpa koma itu satu atau dua data, coba hitung dengan asumsi "dua data"
  dan cocokkan ke kunci Guru dulu sebelum render PNG (lebih murah).
- Kunci Guru Bab 6 hanya sampai hal.291 (Uji Kompetensi Bab 6 no.5b) --
  Pengayaan (Soal Siswa hal.307-308) TIDAK ADA kuncinya sama sekali di
  Buku Guru manapun yang ter-convert untuk kelas8 (guru/index.json
  berhenti di p0299, tidak ada bagian "Pengayaan" ditemukan lewat grep).
  Kalau butuh soal tambahan dari Pengayaan nanti, catat `tidak_ada_di_guru`.
- Banyak "Ayo Bereksplorasi/Berkomunikasi/Mencoba" bab ini adalah tabel
  isian titik-titik BERPEMANDU (jawabannya dituntun langkah demi langkah,
  sering dilanjutkan ke halaman berikutnya dengan "Alternatif Jawaban" versi
  Siswa sendiri) -- ini BUKAN latihan mandiri walau bukan Contoh formal,
  dikategorikan `isian_banyak`, bukan `soal_terbuka`.
- File `bab06.json`: 6 soal (2 subbab A, 4 subbab B), status_kunci: 5
  "cocok", 1 "tidak_cocok" (Soal Laihan 6.2 no.3, lihat poin kunci salah di
  atas). LOLOS validate (0 error, 0 warning) langsung tanpa perlu render
  PNG sama sekali (semua soal yang dipakai ada di halaman tanpa flag [M]).
