# Catatan ekstraksi pretest kelas2 (SD)

## Bab 8 - Berbagai Diagram (hal. 239-262, hal.263-272 = Daftar Pustaka/Profil
Penulis, BUKAN sampul bab 9 -- ini bab TERAKHIR buku, tidak ada bab 9)
- Guru bab8 file range 177-200 (judul cocok). Kunci: hal.182 (Ayo Berlatih subbab A
  #1 Kira mainan hal.246 + #2 Malosi sayur hal.247, DUA tabel tergabung baris-demi-
  baris dalam 1 blok OCR -- pisahkan per baris), hal.183 (Coba Pikirkan subbab A
  Tika bunga hal.248: Mawar=7,Lili=4,Tulip=5,Aster=4, TIDAK dipakai demi efisiensi),
  hal.185 (Ayo Berlatih subbab B #1 Kue Kesukaan hal.254 + #2 Upe permainan
  hal.255 + #3 Ibu buah parsel hal.256, tiga soal tergabung dalam 1 blok),
  hal.186 (Coba Pikirkan subbab B siswa berlari hal.257: >2 putaran=6, TIDAK
  dipakai), hal.187 (Evaluasi #1 turus buah hal.258: Apel=3,Jeruk=7,Semangka=1,
  Alpukat=3 + #2 pertanyaan a-g (duplikat pola, skip) + #3 Warna Kesukaan
  hal.259: Merah=7,Biru=5,Kuning=3,Hitam=2, f=merah paling disukai, TIDAK dipakai).
- Pola kunci penting: soal "Lengkapi diagram turus/gambar dengan mengisi kolom
  Banyak Anak/Banyaknya" (tabel kosong, sumber datanya cuma gambar ilustrasi
  siswa, mis. img-0246-03.png mainan, img-0247-01.png sayur, img-0258-04.png
  buah) -- ANGKA JAWABAN CUMA ADA DI KUNCI GURU (teks, bukan grafis/centang),
  turus di tabel siswa BISA MENYESATKAN karena simbol kelompok-5 (bundel 5
  garis) hilang saat OCR (mis. Kelereng tertulis turus "I" di teks siswa tapi
  kuncinya 6, Mainan balok tertulis "II" tapi kuncinya 7) -- JANGAN percaya
  jumlah goresan "I" di tabel siswa, selalu pakai angka dari kunci Guru.
  Verifikasi silang dengan menghitung manual objek pada gambar siswa (PNG)
  untuk item yang turusnya <5 (mis. Boneka IIII=4, Brokoli/Jagung dst.) cocok;
  untuk item besar (>=5) percayakan ke kunci Guru saja.
- Pola bagus (tanpa gambar sama sekali): soal "Buatlah diagram gambar
  berdasarkan data di atas" yang datanya SUDAH dinarasikan penuh sebagai
  kalimat ("Ada 4 anak yang suka bermain karet." dst, hal.255 Upe permainan
  tradisional) -- jangan buru-buru anggap ini soal gambar/proyek, baca dulu
  paragraf sebelumnya, kadang datanya full teks dan sangat mudah (tingkat 1).
- Pola bagus lain: sentence-completion eksplisit "a. Ada .... buah X." /
  "b. Jumlah ... dan ... adalah ...." (hal.256 Ibu buah parsel, hal.258-259
  Evaluasi #2/#3) sangat verbatim-friendly (kotak isian yang hilang cukup
  ditulis "...." tanpa pertanyaan_disesuaikan, sesuai pola bab4). TAPI kalau
  gambar sumber datanya cuma dekoratif/tidak presisi-terhitung (mis. img-0256-
  01/02.png keranjang buah Ibu untuk Bibi -- cuma ilustrasi pisang/mangga/apel
  menumpuk, TIDAK ada pictogram bintang/ikon per-kategori yang jelas jumlahnya),
  soal itu di-skip walau kuncinya (angka totalnya) sudah ketemu dari guru,
  karena stimulus tidak bisa dibuat self-contained tanpa gambar countable.
  Bandingkan dengan hal.254 Kue Kesukaan yang gambarnya BENAR-BENAR pictogram
  bintang per kategori (img-0254-04.png, jelas dihitung 6/5/3/7) -- ini DIPAKAI.
- Kunci Guru untuk onde-onde/lemper (hal.254 kue) di guru hal.185 SCRAMBLED
  parah (dua label "b."/"c." nempel duluan sebelum angkanya, angka 5 dan 3
  tertukar posisi) -- dikonfirmasi lewat hitung bintang langsung di PNG siswa
  (img-0254-04.png), pakai `dari_png:true` dengan kutipan cuma angkanya.
- Hasil: 19 soal (A:11, B:8), 22 dilewati, validate LOLOS 0 error 0 warning.
  status={'needs_review_soal': 15 (semua yang butuh_gambar:true), 'draft': 4
  (Upe permainan tradisional, sepenuhnya teks tanpa gambar)}.

## Bab 7 - Ayo Membilang sampai dengan 100 (hal. 205-236, sampul bab 8 mulai hal.237)
- Guru bab7 file range 161-176 (BEDA dengan siswa 205-238, seperti biasa penomoran
  guru terpisah). Kunci relevan: hal.166 (Ayo Berlatih subbab A #1 hal.215 dan #3
  hal.218 -- TEKS_DALAM_GAMBAR digabung dari 2 halaman berbeda dalam 1 blok OCR,
  scrambled; render PNG dipakai untuk konfirmasi), hal.167 (Ayo Berlatih subbab A #5
  hal.220, teks BERSIH tidak scrambled, aman langsung dipakai), hal.170 (Kunci
  Jawaban LENGKAP subbab B: Ayo Mencoba, Ayo Berlatih #1-5 hal.227-229, Coba
  Pikirkan -- teks bersih untuk #2/#3/#4/#5, tapi #1 lingkari & Coba Pikirkan
  jawabannya CUMA lingkaran di PNG -> dari_png:true), hal.172 (kunci Evaluasi #2b/c,
  #3 hubungkan lambang bilangan hal.233 (scrambled, render PNG), #4 tebak&hitung,
  #5 urutkan 5 bilangan hal.234 teks bersih).
- Pola kunci penting: soal "Hubungkan dengan bilangan yang tepat" (menjodohkan
  puluhan+satuan <-> bilangan, atau nama bilangan <-> lambang) TIDAK PERLU
  benar-benar melihat pasangan garis di PNG kalau himpunan pilihannya matematis
  UNIK (satu frasa cuma cocok dengan satu angka). Cukup hitung sendiri, lalu
  render PNG sekali untuk konfirmasi visual (garis panah), pakai dara_png:true
  dengan kutipan = angka jawaban saja (dara_png:true membuat validator SKIP
  pengecekan kutipan ke Markdown, jadi kutipan pendek seperti "92" tetap lolos).
  Dipakai di hal.166 (9 puluhan 2 satuan dst -> 92,100,73,66,87) dan hal.172
  (delapan puluh tiga dst -> 83,57,90,77,69).
- Banyak soal Eksplorasi/Contoh berjalan LINTAS BEBERAPA HALAMAN (hal.205-213 kue
  cubit menghitung 1-10 bungkus; hal.221-222 pohon bilangan kupu-kupu/capung;
  hal.223-226 bandingkan kelereng Halim/Malosi, 54 vs 58, urutan 76/83/57) -- semua
  jawabannya dijabarkan PENUH di teks Buku Siswa sendiri sehingga BUKAN latihan,
  di-skip semua (`dilewati`, alasan `lainnya`).
- Soal hitung benda dari gambar (Ayo Berlatih #1 hal.215 jeruk/pensil warna/
  kelereng, gambar gabungan 1 file img-0215-04.png) DIPAKAI (kunci sudah pasti
  dari guru hal.166, gambar jelas/raster). Tapi #2 hal.216-217 (tabel puluhan-
  satuan) dan Evaluasi #1/#2 hal.230-232 (pola sama) DI-SKIP demi efisiensi
  meski kuncinya sudah ketemu (53,84,78 dan 60,70,50,80,53,68,72) -- kalau mau
  ditambah lagi nanti, tinggal render img siswa terkait + pakai kunci di atas.
- "Tebak dan hitunglah banyak bendanya" (Ayo Berlatih #4 hal.219, Evaluasi #4
  hal.233-234) SELALU di-skip (alasan soal_terbuka): bagian "Tebakanku" bervariasi
  antarsiswa, walau "Hasil hitunganku" punya kunci pasti (76,98,59 dari guru
  hal.172) tidak pas dijadikan PG tunggal tanpa mengubah soal signifikan.
- Hasil: 26 soal (A:17, B:9), 13 dilewati, validate LOLOS 0 error 0 warning.

## Bab 6 - Pengukuran (hal. 169-202, sampul bab 7 mulai hal.203)
- Subbab A (Berat, hal.169-189): "Ayo Berlatih" hal.174-175 #1 (kupu-kupu/burung,
  kucing dewasa/tikus, kucing/kelinci -- isian kata lebih berat/lebih ringan/sama
  berat) dan hal.184-185 #1 (labu/apel, buku/bola tenis, gunting/kelereng,
  pisang/jeruk -- isian angka dari timbangan gambar) dipakai. hal.186-187 #2/#3
  (jeruk/mangga/rambutan; buku/tas/penggaris dengan 9 kelereng) POLANYA SAMA,
  di-skip demi waktu tapi kuncinya SUDAH ketemu lengkap di guru hal.151 (lihat
  di bawah) kalau mau ditambah nanti. Coba Pikirkan hal.178-179 (kol/wortel/labu;
  terong/tomat/jeruk/labu) TIDAK ada kunci di Buku Guru -- skip. Coba Pikirkan
  hal.188 (2 mangga=1 pepaya, 1 mangga=2 manggis, 1 pepaya=?manggis) PUNYA kunci
  eksplisit "Berat 1 pepaya adalah 4 manggis" di guru hal.151 -- soal reasoning
  bagus (tingkat 5), dipakai. Evaluasi hal.199-200 #1 (kucing/tikus/tupai/anjing),
  #2 (lingkari buah/benda paling berat/ringan -- kunci grafis semangka/bulu di
  guru hal.155, TAPI nama buah/benda cuma ada di gambar Siswa, bukan teks, jadi
  render PNG Siswa p199 dulu untuk tahu nama-namanya sebelum bisa dibuat PG),
  #3/#4 (pola perkalian jeruk-stroberi, rantai pisang-kelapa-apel) dipakai
  sebagian (item pertama tiap pola saja, sisanya duplikat pola di-skip). #5
  (kelompokkan waktu A/B/C) kunci cuma diagram tanpa teks -- skip.
- Subbab B (Waktu, hal.190-202): "Ayo Berlatih" hal.195 #1 item a = CONTOH
  terjawab ("Pukul 6 pagi"), item b-e = latihan sungguhan (kunci pukul 7 pagi/
  8 pagi/5 sore/8 malam di guru hal.154, TEKS eksplisit tidak scrambled).
  #2 (tarik garis kegiatan ke Pagi/Siang/Sore/Malam, diagram bercabang) di-skip
  (pasangan garis tidak presisi tanpa analisis piksel). #3 (centang kegiatan
  lebih lama, 4 pasang: menyisir/mandi, tidur malam/sikat gigi, belajar/sarapan,
  cuci tangan/main bola) kuncinya PAS di-render PNG guru hal.154 (centang jelas
  terlihat: Mandi, Tidur malam, Belajar di sekolah, Bermain bola). #4 (urutkan
  4 gambar A-D sesuai waktu) kunci TEKS eksplisit "bangun tidur, menyikat gigi,
  makan siang, bermain bola" di guru hal.154 (tidak scrambled, aman langsung
  dipakai tanpa dari_png). Ayo Berkarya hal.201 (proyek cerita+gambar jam) dan
  Catatanku hal.202 (checklist refleksi) di-skip.
- Kunci Jawaban Buku Guru bab 6 (halaman file p<PPPP>.md, bukan nomor cetak):
  hal.147 (kunci Ayo Berlatih subbab A #1-3 hal.174-177 -- SEMUA teks
  TEKS_DALAM_GAMBAR dua kolom yang TERGABUNG TIDAK BERURUTAN, mis. "lebih
  berat" milik kalimat kedua muncul SEBELUM subjek kalimat pertama selesai --
  pakai dari_png:true untuk kutipan yang urutan katanya berisiko terbalik,
  KECUALI kalau frasa lengkapnya kebetulan utuh berurutan seperti "Tikus lebih
  ringan dari kucing dewasa." yang aman tanpa dari_png), hal.150 (kunci
  pengukuran satuan tidak baku hal.184-185, teks BERSIH/tidak scrambled --
  dikonfirmasi lewat render PNG: a.labu=4 apel, b.buku=3 bola tenis, c.gunting=
  5 kelereng, d.2 pisang=4 jeruk), hal.151 (kunci hal.186-187 #2/#3 DAN Coba
  Pikirkan hal.188 pepaya=4 manggis -- perlu render PNG karena scrambled parah,
  angka a/b/c untuk #2 adalah jeruk=6, mangga=8, rambutan=3 balok mainan),
  hal.154 (kunci subbab B lengkap hal.195-198, jam & centang & urutan -- BUKA
  render PNG untuk baca centang #3 karena teks Markdown-nya cuma "..." tanpa
  centang), hal.155 (kunci Evaluasi hal.199-200 -- #1 kucing/tikus/tupai/anjing
  scrambled 3 kolom gabung karakter demi karakter dipakai dengan dari_png:true,
  #2 lingkari buah/benda cuma ada di PNG render sebagai coretan lingkaran tanpa
  teks OCR sama sekali, #3/#4 pola perkalian/rantai TEKS bersih tidak scrambled).
- Pola penting: `_approx_numeric_value` (dipakai validator utk cek opsi tidak
  boleh bernilai sama) HANYA mem-parse string yang SELURUHNYA berupa angka
  murni (boleh ada "Rp"/"%"), jadi teks campuran seperti "4 apel" vs "4 jeruk"
  atau "Pukul 7 pagi" vs "Pukul 7 sore" TIDAK dianggap bernilai sama meski
  angkanya sama -- aman dipakai sebagai distraktor tanpa perlu ganti angka.
- Pola penting utk `dilewati.alasan`: enum yang valid HANYA `soal_terbuka`,
  `pembuktian`, `menggambar_atau_mengukur`, `proyek_atau_aktivitas`,
  `isian_banyak`, `butuh_alat_peraga`, `duplikat`, `teks_tidak_terbaca`,
  `lainnya` (BUKAN bebas teks seperti "kunci_tidak_tersedia" atau
  "duplikat_pola" -- pakai `lainnya`/`duplikat` untuk kasus itu).
- Hasil: 24 soal (A:15, B:9), 15 dilewati, validate LOLOS 0 error 0 warning.

## Bab 5 - Pecahan (hal. 139-166, sampul bab 6 mulai hal.167)
- Subbab A (Setengah dari Benda Utuh, hal.139-146): pertanyaan "Gambar manakah yang
  menunjukkan setengah? A B" di hal.143 adalah CONTOH yang langsung dijawab di hal.144
  ("Gambar A menunjukkan setengah...") -- BUKAN latihan, di-skip. Latihan sungguhan:
  hal.145 Ayo Berlatih #3 (centang gambar kiri/kanan mana yang setengah, a=lingkaran,
  b=persegi panjang, c=hati -- kuncinya CUMA tanda centang di PNG Guru hal.124, tidak
  ada teks OCR, jawaban a=kanan, b=kanan, c=kiri) dan hal.146 #5 (klasifikasi 7 gambar
  A-G ke tabel Setengah/Bukan Setengah -- kunci Guru ADA sebagai teks eksplisit di
  hal.125: "Setengah A, C, F, G" / "Bukan Setengah B, D, E", TIDAK perlu render PNG).
  #1 (warna bebas) dan #2 (warna bebas) dan #4 (tarik garis+warna) di-skip (menggambar).
- Subbab B (Setengah dari Kumpulan Benda, hal.147-154): pertanyaan eksplorasi awal
  (Malosi/Upe, 4 kelereng) di hal.147 juga CONTOH terjawab di hal.148, di-skip.
  Ayo Berlatih hal.150-151 #1 (centang kelompok mana yang setengah, disajikan sebagai
  2 baris pembagian per bagian a/b, mis. "2+2" vs "1+3" -- pilih baris yang jumlahnya
  sama) kuncinya CUMA centang di PNG Guru hal.129 (tidak ada teks). #2 (lingkari
  kelompok a-d) di-skip: beberapa pasang kelompok berjumlah SAMA tapi hanya satu
  dilingkari di kunci tanpa kriteria tertulis (bukan soal jumlah/paritas yang jelas).
  #3 (warna kelompok a/b/c, mis. 8/10/6 benda) diubah jadi soal hitung "berapa yang
  diwarnai supaya setengah" (jawaban N/2) -- hitung sendiri dari PNG Guru hal.129
  (tidak ada teks angka). #4 (lingkari, blob tidak presisi) dan #5 (menggambar) di-skip.
  Evaluasi hal.162-163 #1 (centang kelompok setengah a/b/c, pola sama seperti hal.150)
  dan #2 (lingkari setengah dari kumpulan benda, diubah jadi hitung N/2) kuncinya di
  PNG Guru hal.135. #3/#4/#5 (mewarnai/tarik garis bebas) di-skip.
- Subbab C (Seperempat dari Benda Utuh, hal.154-161): intro cerita Kira/martabak tanpa
  soal tertutup, di-skip. Ayo Mencoba (lipat kertas) di-skip. Ayo Berlatih hal.159 #1
  (warna bebas) di-skip. #2 (4 gambar dengan bagian diwarnai ungu, pilih mana yang
  BENAR seperempat) kuncinya X/centang/X/X di PNG Guru hal.134 -- HATI-HATI, gambar ke-4
  (kotak grid 2x2 yang TERLIHAT sama besar) sebenarnya BUKAN seperempat (diukur presisi
  dengan piksel: kolom kiri lebih lebar & baris atas lebih pendek daripada kolom/baris
  lain) -- trik visual, JANGAN percaya grid yang terlihat rapi tanpa cross-check kunci.
  Hal.160 #3 (klasifikasi 8 gambar A-H ke Seperempat/Bukan Seperempat) kunci Guru ADA
  sebagai teks eksplisit di hal.134: "Seperempat B, D, G, H" / "Bukan Seperempat A, C,
  E, F", tidak perlu render PNG. #4 (tarik garis+warna) di-skip. Coba Pikirkan (diagram
  isian pendapat) di-skip.
- Kunci Jawaban Buku Guru bab 5 (halaman file p<PPPP>.md, bukan nomor cetak): hal.124
  (Ayo Berlatih subbab A hal.144-145, kunci #3 CUMA di PNG), hal.125 (lanjutan kunci
  subbab A #4/#5 hal.146 DAN teks eksplisit "Setengah A,C,F,G / Bukan B,D,E" +
  Eksplorasi Awal subbab B), hal.129 (kunci lengkap Ayo Berlatih subbab B #1-4
  hal.150-153, SEMUA dari PNG karena cuma tanda centang/lingkaran, tidak ada angka
  tertulis), hal.134 (kunci Ayo Berlatih subbab C hal.159-160, #2 dari PNG + #3 teks
  eksplisit "Seperempat B,D,G,H / Bukan A,C,E,F" + Coba Pikirkan), hal.135 (kunci
  Evaluasi hal.162-164 #1/#2 dari PNG, angka dihitung langsung dari gambar).
- Pola berguna: ketika kunci Guru CUMA berupa tanda centang/lingkaran di PNG (tanpa
  teks jawaban di Markdown), render p124/p129/p134/p135 SEKALIGUS (satu file PDF berisi
  beberapa spread kunci Buku Siswa sebagai gambar kecil per section) lalu crop per
  kuadran dengan PIL untuk baca presisi -- lebih hemat daripada render per-hal siswa.
- Pola penting untuk validator: `stimulus` HARUS >=90% verbatim (tidak ada keringanan
  untuk pertanyaan_disesuaikan, beda dengan `pertanyaan` yang keringanannya 50%).
  Untuk soal gambar-tanpa-teks (centang/lingkari kelompok mana yang benar), JANGAN
  tulis deskripsi gambar buatan sendiri di `stimulus` (pasti gagal verbatim) --
  taruh `stimulus` = instruksi asli TANPA modifikasi (persis dari buku, akan otomatis
  100% verbatim), lalu tambahkan "(bagian a)" dsb HANYA di `pertanyaan` (yang punya
  keringanan 50%). Deskripsi detail gambar (bentuk, warna, proporsi) ditaruh di
  `catatan` (field ini TIDAK diverifikasi validator) atau di dalam teks opsi
  jawaban/distraktor (juga tidak diverifikasi). Jangan sertakan angka hasil hitung dari
  gambar (mis. "8 bintang") di `pertanyaan`/`stimulus` kalau angka itu tidak tertulis
  di halaman Buku Siswa -- taruh angkanya hanya di `jawaban_benar`/`distraktor`.
- Hasil: 19 soal (A:5, B:11, C:3), 20 dilewati, validate LOLOS 0 error 0 warning.
  per-subbab siap pakai (tidak termasuk needs_image)={'A': 5, 'B': 2, 'C': 3}.

## Bab 4 - Posisi Benda dan Pola di Sekitar Kita (hal. 115-136, sampul bab 5 mulai hal.137)
- Subbab A (Posisi Benda, hal.116-125): latihan utama di "Ayo Berlatih" hal.119 (kucing
  vs meja/sepeda, 4 sub-gambar a-d, isian kata posisi) dan hal.120-122 (kandang, kamar,
  taman/rumah, masing-masing 6 kalimat isian kata posisi a-f). "Coba Pikirkan" hal.125
  (tebak benda dari 3 petunjuk arah + gambar kamar) hanya butir a yang jelas jawabannya
  (pot bunga); b dan c ambigu (beberapa benda cocok sebagian petunjuk) dan TIDAK ada
  kunci di Buku Guru -> di-skip.
- Subbab B (Pola, hal.126-136): "Ayo Berlatih" hal.130 #1 (pilih barisan gambar yang
  berpola, hanya baris a yang benar dari 4 baris) dan hal.131 #2 (lanjutkan pola bentuk,
  4 baris) + #3 (lanjutkan pola warna, 3 baris, gambar SEMUA baris #2 dan #3 gabung jadi
  1 file img-0131-01.png). Evaluasi hal.133 #3 (lanjutkan pola bentuk tabel kotak) dan #5
  (isi kotak pola) TIDAK punya file gambar sama sekali (tabel digambar vektor oleh PDF,
  bukan raster) -> image_refs kosong, status otomatis needs_image meski kuncinya sudah
  pasti dari PNG Guru. Evaluasi #4 (rumah Ani, cari pot kunci "paling kanan") punya
  gambar bersih (img-0133-07.png), kuncinya pot tanaman daun hijau di ujung kanan (bukan
  pot bunga).
- Kunci Jawaban Buku Guru bab 4 (angka halaman = nama file p<PPPP>.md, BUKAN nomor cetak):
  - hal.108 (cetak 107-110): kunci lengkap Ayo Berlatih subbab A #1-4 (kucing hal.119,
    kandang hal.120, kamar hal.121, taman/rumah hal.122). #1 (kucing) jawabannya CUMA
    lingkaran di PNG (kata "atas/bawah/dst" tidak tercetak sbg teks OCR) -> wajib
    dari_png:true. #2/#3/#4 jawabannya sudah berupa teks lengkap tertulis di Markdown
    Guru (mis. "a. Bola ada di bawah kandang."), tidak perlu render PNG.
  - hal.109: catatan pembelajaran umum untuk Ayo Bermain & Coba Pikirkan, TIDAK ada
    kunci literal untuk tebakan Coba Pikirkan.
  - hal.113 (cetak 118-119): kunci Ayo Berlatih subbab B #1 (centang gambar a saja),
    #2 (lingkaran pada gambar berikutnya: a=heksagon, b=kelinci, c=awan, d=daun), #3
    (warna lanjutan: a=hijau, b=merah muda lalu biru, c=oranye) -- SEMUA jawaban CUMA
    ada di PNG (centang/lingkaran/warna), tidak ada teks OCR sama sekali -> wajib
    dari_png:true untuk semua butir subbab B.
  - hal.114 (cetak 120-121): kunci Evaluasi #1 (posisi bola vs boneka/meja, 6 jawaban
    tapi gambarnya 3 pasang tergabung dalam 2 file kompleks -> di-skip), #3 (lanjutkan
    pola tabel: a=segilima oranye, b=lingkaran hijau, keduanya kotak ke-5), #4 (rumah
    Ani: pot paling kanan dilingkarin merah muda di PNG), #5 (isi kotak pola: kotak
    ke-4 = hati). Render PNG dipakai untuk hal.108, 113, 114 (crop per-baris dengan
    PIL untuk baca lingkaran/centang/warna presisi).
- Pola umum: kalimat isian kata posisi ("Bola ada di __ kandang.") ditulis dengan blank
  "...." di pertanyaan, TIDAK perlu pertanyaan_disesuaikan (masih dianggap verbatim
  karena token "...." bukan alfanumerik, diabaikan validator). pertanyaan_disesuaikan
  HANYA dipakai untuk soal pola bergambar (lingkari/warnai) yang diubah jadi pilih-nama,
  dengan tambahan minimal "(baris a)" dsb -- jangan tambah kalimat pertanyaan baru yang
  panjang, karena coverage measurement (SequenceMatcher berurutan) bisa jatuh di bawah
  50% kalau kata barunya banyak dan tidak berurutan dengan teks asli.
- Hasil: 35 soal (A:24 siap pakai, B:8 siap pakai; 3 soal B berstatus needs_image karena
  tabel pola vektor tanpa file gambar), 14 dilewati, validate LOLOS 0 error 0 warning.

## Bab 1 - Ayo Membilang sampai dengan 50 (hal. 8-50)
- Hal. 8-11 (dan sisipan p9,10 yang ditandai "latihan" di INDEX) adalah
  "Panduan Penggunaan Buku" (cover depan) yang menampilkan CUPLIKAN acak dari
  berbagai halaman asli sebagai contoh tampilan rubrik (Ayo Mencoba, Ayo
  Berlatih, Evaluasi, dll). BUKAN soal sungguhan -- selalu dilewati (lihat
  `dilewati` di bab01.json), soal aslinya ada di halaman lain (mis. hal. 23-24, 43).
- Bab 1 di Buku Siswa sungguhan dimulai hal. 13 (Sampul Bab), bukan hal. 8.
  Penomoran halaman cetak buku (pojok) = halaman PDF - 12 (mis. hal.24 PDF =
  "hal. 12" cetak).
- Kunci Jawaban Bab 1 di Buku Guru:
  - hal. 46: kunci Ayo Berlatih subbab A (hal. siswa 24-27): hitung benda
    gambar (24,34,45,36 / 25,32,34,42), lambang bilangan (43,35), baca
    bilangan (26,48,37 dibaca...), urutan bilangan.
  - hal. 51: kunci Ayo Berlatih subbab B (hal. siswa 33-34): nilai tempat
    (24=2p4s, dst), Tika lambang bilangan (35,43), Lili nilai tempat 46
    (kunci: "A dan B" sama-sama benar -> tidak bisa dibuat PG tunggal, di-skip).
  - hal. 54: kunci Ayo Berlatih subbab C (hal. siswa 38-41): tebak+hitung
    benda (22,35,28,30), lingkari lebih besar/kecil (JAWABAN GRAFIS -- hanya
    berupa lingkaran di PNG, teks Markdown-nya sama untuk kedua pilihan,
    HARUS render PNG guru & set `dari_png:true`), urutkan 4 bilangan.
  - hal. 55: kunci Coba Pikirkan subbab C (kartu bilangan Malosi/Kira/Lili):
    "Lili 32, Kira 34, Malosi 35" -- teks jawaban ADA di Markdown meski
    scrambled (TEKS_DALAM_GAMBAR), tidak perlu render PNG.
  - hal. 56: kunci Evaluasi (hal. siswa 43-46), semua 7 nomor lengkap dengan
    jawaban tertulis di Markdown (kecuali nomor gambar/hitung benda: 1,4,6).
- Render PNG dipakai untuk: siswa p0024 (verifikasi hitung benda, tidak jadi
  dipakai), guru p0046, p0054 (cek lingkaran jawaban lebih besar/kecil).
- Pola umum "TEKS_DALAM_GAMBAR" scrambled tapi kalau berisi ANGKA/teks
  jawaban tertulis lengkap, masih valid dipakai sebagai kutipan tanpa render
  (hanya urutan antar-baris yang kacau, isi teksnya utuh).
- Hasil: 21 soal (A:5, B:5, C:11), 17 dilewati, validate LOLOS 0 error 0 warning.

## Bab 2 - Penjumlahan dan Pengurangan (hal. 51-78)
- Bab sungguhan mulai hal. 51 (Eksplorasi Awal "Panen Jambu Air"), berakhir
  hal. 76 (Catatanku/refleksi); hal. 77-78 sudah Bab 3.
- Setiap Ayo Berlatih (subbab A hal.57-59, subbab B hal.64-65) berisi 4 nomor
  dengan METODE berbeda: 1=menghitung maju/mundur, 2=cara bersusun,
  3=pasangan bilangan, 4=bebas. **Nomor 2 (bersusun) JANGAN dipakai**:
  bilangan dua digit di Markdown tercetak per-digit terpisah (place value
  table), mis. "14" muncul sebagai token "1" lalu "4" terpisah, bukan "14"
  utuh -- verbatim/angka-hilang validator akan gagal. Nomor 1/3/4 aman
  (bilangan dua digit utuh di teks).
- Kunci Jawaban Buku Guru:
  - hal. 66: kunci lengkap Ayo Berlatih subbab A (1-4, semua nomor termasuk
    yang bersusun) tertulis scrambled tapi utuh di TEKS_DALAM_GAMBAR.
  - hal. 71: kunci lengkap Ayo Berlatih subbab B (1-4) sama pola dengan hal.66.
  - hal. 73: kunci Ayo Berlatih subbab C nomor 1-5 (soal cerita, semua sub a/b/c).
  - hal. 74: kunci Evaluasi nomor 1-9 (nomor 8 & 9 kuncinya CUMA lingkaran di
    PNG, tidak ada teks jawaban di Markdown -> `dari_png:true`). Nomor 10-11
    tidak dipakai (lihat di bawah).
  - Render PNG dipakai untuk: guru p0074 (cek lingkaran opsi benar nomor 8
    dan 9), siswa p0074 img -07/-08 (hitung kuntum bunga pot A-D: 2,4,5,6),
    siswa p0075 (base-10 block nomor 10: A=13,B=32,C=23,D=32 -- B dan D
    bernilai SAMA di buku aslinya, jadi nomor 10 tidak bisa dijadikan PG 4
    opsi berbeda, di-skip).
  - Evaluasi nomor 10 & 11 (hal.75) opsinya berupa gambar abacus/kombinasi
    bentuk yang di Markdown tersimpan sebagai banyak file PNG primitif per
    cincin/bentuk (bukan satu file utuh per opsi) -> tidak ada image_refs
    bersih, di-skip (lihat `dilewati`).
- Evaluasi bernomor lanjut 1-11 tapi menyebar di beberapa halaman siswa:
  1-2 di hal.71, 3-4 di hal.72, 5-6 di hal.73, 7-9 di hal.74, 10-11 di hal.75.
- Hasil: 24 soal (A:5, B:4, C:15), 11 dilewati, validate LOLOS 0 error 0 warning.

## Bab 3 - Bentuk di Sekitar Kita (hal. 79-112, sampul bab 4 mulai hal.113)
- Subbab A (Bangun Datar, hal.80-92): latihan utama ada di "Ayo Berlatih" hal.89
  (nama bangun dari gambar, 5 item: segitiga/segiempat/segilima/segienam/lingkaran)
  dan hal.90 (menjodohkan bangun<->ciri jumlah sisi, 5 item). Banyak halaman lain
  (82-88, 91-92) berisi Ayo Mencoba eksplorasi kelompok/tabel isian banyak/mewarnai
  -- semua di-skip (lihat `dilewati`).
- Subbab B (Mengurai & Menyusun, hal.93-101): SEMUA latihan berbentuk menjodohkan
  gambar (bukan teks), yaitu Ayo Berlatih hal.97 (#2 susun 4 pasang) dan hal.98
  (#3 urai 4 pasang). Pasangan garis TIDAK bisa ditebak dari Markdown (teks
  TEKS_DALAM_GAMBAR di kunci Guru hanya memuat instruksi, bukan pasangannya) --
  WAJIB render PNG kunci Guru hal.91 (dpi tinggi, mis. `--dpi 400`) lalu deteksi
  garis penghubung secara presisi (dot purple + garis hitam). Trik yang berhasil:
  crop region jawaban, tempel grid piksel, lalu hitung fraksi piksel gelap di
  sepanjang tiap kemungkinan pasangan (i,j) dengan numpy -- pasangan dengan
  fraksi >0.7 itulah yang benar. Hasil hal.97: L1(persegipanjang+segitiga)->anak
  panah kiri, L2(persegipanjang+persegi)->tangga, L3(persegipanjang+2segitiga)
  ->panah 2 arah, L4(4 persegi kecil)->persegi besar. Hasil hal.98 (urai, warna
  bentuk = petunjuk tambahan yang match dengan hasil): merah->2persegi,
  biru(zigzag)->2segitiga+1persegipanjang, hijau(persegi)->2segitiga,
  oranye(huruf T)->2persegipanjang beda ukuran. Ayo Berlatih #1 hal.97 (lingkari
  bagian lingkaran yang hilang) di-skip karena cuma 2 opsi asli di buku.
  Evaluasi #3/#4/#5 (hal.108-109) adalah pola menjodohkan SAMA PERSIS (skip,
  alasan duplikat) -- tidak perlu diulang render/trace lagi.
  Untuk pertanyaan_disesuaikan pada menjodohkan gambar, kalimat "Jika X disusun/
  diurai menjadi..., bentuk apa hasilnya?" sering GAGAL verbatim (cuma ~49%
  token cocok, minimum 50%); pakai kalimat yang lebih dekat ke instruksi asli,
  mis. "Susun bangun datar berikut menjadi satu bentuk. Bentuk apa hasil
  susunannya?" (cek dengan `coverage()` di validate.py sebelum commit).
- Subbab C (Bangun Ruang, hal.102-112): nama bangun ruang dari gambar ada 2 kali
  (Ayo Berlatih hal.105 #2 dan Evaluasi hal.110 #6, masing-masing 5 bentuk:
  kubus/balok/tabung/kerucut/bola) -- kunci Guru hal.96 & hal.97. Evaluasi #7
  (hal.110, hitung balok satuan pada susunan 3D, sudah PG A-D di buku) kuncinya
  cuma lingkaran di PNG Guru hal.97 (dari_png:true), jawaban B.8.
- Kunci Jawaban Buku Guru bab 3: hal.86 (Ayo Berlatih subbab A hal.89-90, TEKS_
  DALAM_GAMBAR scrambled tapi tokennya utuh: "kubu s"/"balo k"/"k eruc ut" pecah
  jadi token terpisah -- validator tetap lolos lewat fallback level-karakter),
  hal.87 (Coba Pikirkan subbab B, dilewati), hal.91 (kunci menjodohkan susun+urai
  subbab B, WAJIB render PNG, lihat catatan di atas), hal.96-97 (kunci Ayo
  Berlatih subbab C hal.105 + Evaluasi lengkap hal.107-110).
- Hasil: 29 soal (A:10, B:8, C:11), 32 dilewati, validate LOLOS 0 error 0 warning.
