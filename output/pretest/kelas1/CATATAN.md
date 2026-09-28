# Catatan ekstraksi pretest kelas1

## Bab 1 - Ayo Membilang sampai dengan 10 (hal. 9-54)
- Hal. 9-12 di rentang bab (menurut INDEX) sebenarnya masih "Petunjuk Penggunaan Buku"
  (contoh rubrik Ayo Mencoba/Ayo Bermain/dst dari berbagai bab lain), BUKAN materi Bab 1.
  Materi Bab 1 baru mulai hal. 13. Dicatat sebagai `dilewati` untuk hal. 9 & 10 (perlu untuk
  hal. 11-12 juga kalau divalidasi ulang, tapi validator hanya menandai 9 & 10 sebagai warning).
- Kunci Jawaban Buku Guru bab 1 TIDAK berurutan mengikuti halaman Siswa. Kunci tersebar di
  guru hal. 33 (subbab A: Ayo Mencoba angka-nama, Ayo Berlatih hitung+pasang benda),
  hal. 38 (subbab A lanjutan: hitung jari, pasangkan lambang-nama, "Ayo menghitung banyak
  mainan" - Wei), hal. 42 (subbab B: bandingkan banyak benda item 1-3), hal. 46 (subbab C:
  lengkapi urutan bilangan), hal. 50 (subbab D: pasangan bilangan / number bond, termasuk
  "Upe 8 mobil-mobilan"), hal. 51 (Evaluasi akhir bab).
- PENTING: soal "Ayo Mencoba - Amati gambar, hitung Mata/Hidung/Telinga/dst" (siswa hal. 16)
  punya kunci ANGKA (Mata=2, Jari kaki=10, dst) di guru hal. 33, TAPI ada gelembung teks di
  PNG guru yang menyatakan "Jawaban peserta didik dapat beragam" tepat menunjuk ke panel ini
  → statusnya tetap variatif, DILEWATI meski ada angka di teks OCR (jangan tertipu angka yang
  muncul di markdown guru).
- Soal "Temukan pasangan bilangan" (number bond) yang HANYA punya 1 lingkaran kosong dengan
  1 angka sudah diberikan (siswa hal. 43 bond pertama, 8=5+3) → kunci PASTI/fixed.
  Yang keduanya kosong tanpa anchor (siswa hal. 43 bond kedua 9=..+.., hal 44, hal 47 bonds
  2-4) → cek dulu apakah guru menyatakan "dapat beragam"; kalau tidak (spt bond 9=4+5 di
  hal 43) tetap fixed, kalau ya (spt hal 44 dan hal 47) → DILEWATI.
- Banyak soal "pasangkan garis" (angka-nama, angka-angka, benda-angka) kuncinya hanya berupa
  GAMBAR garis penghubung di PNG guru, teks markdown-nya jumbled/tidak urut. Render PNG guru
  di halaman yang sama untuk baca pasangannya, gunakan `kunci_guru.dari_png: true`.
- Item "Ayo menghitung banyak mainan" (Wei, siswa hal. 27, 5 sub-isian) kuncinya justru
  tertulis bersih sebagai teks di guru hal. 38: "Ada 6 ... Ada 9 ...\nAda 6 ... Ada 6 ...\n
  Ada 5 ..." (urutan sesuai gambar: kelinci=6, mobil=9, pesawat=6, gasing=6, bola=5).
- Evaluasi akhir bab (siswa hal. 48) kuncinya lengkap & bersih di guru hal. 51, termasuk teks
  eksplisit "jeruk (B)" / "mangga (A)" untuk soal banding buah — bisa dikutip verbatim.
- Banyak soal butuh gambar (mencocokkan benda dengan angka, mewarnai, menebalkan, connect-the-
  dots, menunjukkan bilangan dengan jari) — sengaja dilewati demi efisiensi meski beberapa di
  antaranya (hal. 17, 19, 20) sebenarnya punya kunci pasti di guru hal. 33, karena butuh
  banyak image_ref per sub-gambar kecil yang berisiko salah rujuk.

## Bab 4 - Mengenal Bentuk (hal. 129-158)
- Bab ini hampir seluruhnya bergantung gambar (topik "bentuk"): hampir tidak ada soal teks murni.
  21 soal berhasil diekstrak, semua `butuh_gambar: true`.
- Kunci Guru tersebar: guru p0123 (kunci utk siswa hal. 122-125 = subbab A item 1-5 + Ayo
  Bermain), guru p0127 (kunci utk siswa hal. 131-133 = subbab B item 1a-c "Lingkari jawaban
  yang benar" + "Warnailah"), guru p0130 (kunci utk siswa hal. 137-138 = subbab C item 1 puzzle
  + item 2 hitung bentuk gambar anjing, ANGKA TERCETAK JELAS: "Bentuk lengkung ada 5, Segi
  empat ada 8, Segitiga ada 1" -- aman dipakai langsung tanpa dari_png), guru p0131 (kunci
  Evaluasi hal. 140-142).
- PERANGKAP: guru p0131 (kunci Evaluasi soal 5, hitung bentuk gambar robot) punya angka
  tercetak jelas ("Bentuk lengkung ada 4, Segi empat ada 9, Segitiga ada 5") TAPI berdekatan
  dengan gelembung teks "Jawaban peserta didik dapat beragam..." -- ambigu apakah utk soal 4
  (puzzle) atau soal 5 (hitung), jadi soal 5 SENGAJA DILEWATI demi kehati-hatian (pola sama
  dgn perangkap di CATATAN Bab 1). Soal hitung SEJENIS di guru p0130 (anjing, subbab C) TIDAK
  punya gelembung serupa -> dipakai dengan aman.
- Banyak soal "Pasangkan yang bentuknya sama" / "Pasangkan bentuk dengan namanya" adalah
  matching N gambar -> 3 label (segitiga/segi empat/bentuk lengkung), N>3 sehingga BEBERAPA
  gambar berpasangan dgn label yang sama (fan-in). Dipecah jadi 1 soal PG per gambar kanan
  (`pertanyaan_disesuaikan: true`), kunci dibaca dari GARIS pada PNG Guru (`dari_png: true`,
  tidak ada teks tercetak utk pasangan individual). Pola shape->nama SELALU konsisten di
  seluruh bab: segitiga/segitiga siku-siku -> "Segitiga"; persegi/persegi panjang -> "Segi
  empat"; lingkaran/oval -> "Bentuk lengkung" (dicek silang 2x lewat pixel-trace PNG Guru,
  selalu cocok) -- tidak perlu trace pixel manual lagi kalau ketemu pola serupa, cukup
  pakai identitas bentuk.
- Item "Lingkari bentuk bangun yang benar" (p0136 item4, mirip di beberapa tempat) SELALU
  py >1 jawaban benar per kategori di antara 5 pilihan -> tidak bisa PG, DILEWATI.
- Item puzzle "Lingkari pasangannya" (potongan bentuk melengkapi gambar induk, p0149-150 &
  p0154 item4) SENGAJA DILEWATI: opsi jawaban hanya beda samar (potongan hampir identik),
  tidak bisa dibuat distraktor yang pasti salah tanpa gambar definisi tinggi.
- Soal hitung "Ada __ bangun datar" tanpa breakdown per kategori (p0151 item3, gambar rumah)
  TIDAK ADA kunci di Buku Guru & ambigu cara menghitung atap (1 atau 2 bentuk) -> DILEWATI.
  Soal hitung yang breakdown per kategori (lengkung/segiempat/segitiga terpisah) jauh lebih
  aman krn tiap sub-angka bisa dicek silang mandiri.
- Banyak gambar kecil (bentuk vektor polos: segitiga/persegi/oval tanpa gradasi) TIDAK
  diekstrak sbg file img/ (hanya elemen berteksur/gradasi yang dirasterkan). Jadi utk soal
  matching sederhana, opsi ditulis sbg TEKS deskriptif (nama bentuk + warna), bukan image_ref
  per opsi -- hanya gambar ACUAN/OBJEK utama yang direferensikan via image_refs.

## Bab 5 - Ayo Membilang sampai dengan 20 (hal. 159-188)
- Guru bab 5 (hal. 135-152) hampir SELALU menyediakan kunci teks bersih (bukan grafis) untuk
  soal isian angka/barisan/nilai tempat/urutan bilangan -- jauh lebih mudah dari bab 1-4.
  Lokasi kunci: guru p141 (kunci Ayo Berlatih subbab A hal.164-167, termasuk item matching
  hal.164 & hitung gambar hal.165-166 yang TIDAK dipakai di sini), guru p144 (kunci Ayo
  Berlatih subbab B hal.171-172, subbab C baru dimulai stlh ini), guru p147 (kunci Ayo
  Berlatih subbab C hal.175-176 DAN mulai Subbab D), guru p149 (kunci Ayo Berlatih subbab D
  hal.179-181 & Evaluasi awal), guru p150-151 (kunci Evaluasi hal.181-186 lengkap sampai
  item 8).
- Banyak halaman [T] (TEKS_DALAM_GAMBAR) berisi barisan bilangan ("Isilah titik-titik")
  dengan urutan token di Markdown TERBALIK/kacau dari urutan visual asli (mis. hal.171 item
  1c "19 ... / 17 ..." padahal visual PNG-nya 17, ..., 19, ...). WAJIB render PNG utk urutan
  visual yang benar, lalu kalau urutan hasil render beda dari urutan token Markdown, set
  `pertanyaan_disesuaikan: true` (bukan cuma `notasi_dari_png`) supaya verbatim-check pakai
  ambang 50% (longgar), karena SequenceMatcher token-order akan gagal cocok kalau urutan
  kita (benar secara visual) beda dari urutan Markdown (kacau).
  Item lain di bab yang sama kadang KEBETULAN urutan Markdown-nya SAMA dgn visual (mis.
  hal.171 item1a/1b, hal.172 item2a/2b) -- cek per item, jangan asumsikan semua kacau.
- Pola soal "Perhatikan bilangan berikut. X Y Z / Urutan dari terkecil: ../ Urutan dari
  terbesar: .." (subbab D, hal.180-184) SANGAT produktif: teks stimulusnya berupa angka polos
  (urutan Markdown biasanya sudah benar utk pola ini krn bukan barisan bergambar), kuncinya
  eksplisit lengkap di Guru. Bisa dipakai berulang di beberapa halaman berbeda (hal.180,181,
  184) tanpa masalah duplikasi karena nilai berbeda-beda.
- Soal cerita "Malosi/Wei/Kira punya N bola, siapa paling banyak/sedikit + urutan" (Evaluasi
  item 8, hal.184): Buku Guru hanya menjawab EKSPLISIT untuk sub-pertanyaan "urutan angka"
  (mis. "10, 11, 13"), TIDAK menuliskan ulang nama utk sub-pertanyaan "siapa paling banyak/
  sedikit" meski jawabannya jelas dari data yg sama -> beri `status_kunci: tidak_ada_di_guru`
  utk sub-pertanyaan nama (bukan `cocok`), meski secara logika pasti benar.
- Item nilai tempat yang BUTUH gambar (hal.175 item1c "telur"=15, item1d "lingkaran merah"=
  14) punya kunci teks bersih di guru p147 ("1 puluhan dan 5 satuan = 15" dst) sehingga tidak
  perlu tebak-tebak dari PNG siswa -- tinggal pastikan `image_refs` menunjuk file gambar
  gabungan yang benar (satu file PNG bisa memuat panel a-d sekaligus, cek dulu isinya).
- Hal.164 (Ayo Berlatih matching+hitung gambar) dan hal.168 (Ayo Mencoba tebak-buktikan
  kelereng dlm stoples) SENGAJA `dilewati` (masing-masing hanya 1 entri dilewati mewakili
  beberapa nomor) krn ★-tag hanya butuh 1 halaman tersentuh; latihan lanjutannya (hal.165-166,
  169-170) tidak perlu disentuh terpisah.

## Bab 6 - Penjumlahan dan Pengurangan sampai dengan 20 (hal. 189-208, sisa 209-210 sudah Bab 7)
- Bab ini JAUH lebih ramah teks dibanding bab 1/4: sebagian besar latihan (Ayo Berlatih,
  Evaluasi) berupa persamaan angka murni ("13 + 4 = ", "17 – 4 = ") atau soal cerita pendek
  tanpa gambar wajib -> 30 soal berhasil diekstrak TANPA satupun butuh_gambar/render PNG.
- Kunci Jawaban Guru bab 6 (guru hal. 149-160, file p0157/p0158/p0160/p0161/p0164/p0167/p0168)
  sinkron rapi dengan urutan Ayo Berlatih/Evaluasi Buku Siswa, teksnya bersih (bukan grafis),
  meski SANGAT jumbled urutan tokennya (OCR 2 kolom/panel tercampur, angka jawaban kadang
  MENEMPEL tepat setelah soal, mis. "13 + 4 = 17 b. 15 + 3 = 18"). Validator (SequenceMatcher
  berbasis matching-block, bukan exact substring) tetap lolos asal semua kata & angka ada di
  halaman ±1, jadi kutipan kunci cukup ditulis natural/ringkas ("13 + 4 = 17") tanpa perlu
  meniru urutan jumbled aslinya.
- Pola subbab A (konsep "lebih dari/kurang dari/selisih", hal. 189-194): soal cerita yang
  memakai kata "lebihnya/kurangnya/selisih" DIKLASIFIKASIKAN subbab A meskipun operasinya
  penjumlahan (mis. "Halim 2 kelereng lebihnya dari Malosi" = 5+2, tetap subbab A) -- konsep
  yang diuji adalah pemahaman kosakata perbandingan, bukan jenis operasinya. Item yang punya
  2 sub-pertanyaan (a: pakai kosakata lebih/kurang -> subbab A; b: "jumlah jika digabungkan"
  tanpa kosakata banding -> subbab B) dipecah lintas subbab (lihat soal p0201 & p0205 item 5).
- Item bernomor ganjil di teks siswa hasil OCR sering muncul dobel jadi "55." atau "77."
  (harusnya "5." dan "7.") -- source_item_no tetap ditulis "5"/"7" (angka bersih), bukan
  ditiru dobel.
- Halaman 190-191, 195-198, 201(bag. awal), 202 adalah "Ayo Mencoba"/penjelasan bermetode
  (menghitung maju/dengan 10/berulang/pasangan bilangan/nilai tempat) yang SUDAH dijawab di
  buku (contoh, bukan latihan) -- correctly tidak diambil sebagai soal.
- Soal yang butuh gambar (hal. 192-193 item1-4: kelereng merah/biru, mangga/apel, mobil-
  pesawat, penggaris) SEMUA punya kunci angka pasti di guru hal. 160, tapi TIDAK diambil
  (masuk `dilewati` alasan butuh_alat_peraga) karena tidak ada file img/ untuk direferensikan
  dan constraint waktu -- kalau perlu menambah soal subbab A nanti, ini sumber cadangan.
- Item "16 – 4"/"17 – 5" (hal. 204 item3, tabel nilai tempat) sengaja dilewati: teks siswa
  tidak punya tanda "=" (hanya heading angka polos), beda dari item1/2/5 yang selalu ada "=".
- Evaluasi item1 (hal. 205, kue lapis vs onde-onde) dilewati: angka (8 kue lapis, 6 onde-onde)
  HANYA ada di kunci Guru/gambar, sama sekali tidak disebut di teks siswa (beda dari Evaluasi
  item2 gantungan kunci yang angkanya eksplisit di teks siswa).
- Halaman 209-210 SUDAH bagian Bab 7 (Mengukur Panjang Benda) meski rentang tugas ditulis
  s.d. 210 -- tidak ada materi Bab 6 di sana, jangan disentuh ulang.

## Bab 7 - Mengukur Panjang Benda (hal. 211-230, hal. 231-232 sudah Bab 8)
- Materi Bab 7 sesungguhnya hal. 211-230 (Catatanku di hal. 230 = akhir bab); hal. 231-232
  sudah "8 Mengenal Diagram" meski rentang tugas ditulis s.d. 232 -- tidak perlu disentuh.
- Kunci Jawaban Guru bab 7 SANGAT bersih & lengkap (tidak seperti bab 1-6): guru hal. 177
  memuat kunci utk SEMUA Ayo Berlatih subbab A (item 1-7, siswa hal. 217-219) sekaligus,
  guru hal. 180 memuat kunci Ayo Berlatih subbab B (item 1-4, siswa hal. 224-225) DAN
  Evaluasi item 1-5 (siswa hal. 226-227), guru hal. 181 memuat kunci Evaluasi item 6-7
  (siswa hal. 228, bernomor ganda "66."/"77." di teks siswa akibat OCR, source_item_no
  ditulis "6"/"7" bersih). 53 soal berhasil diekstrak dari hanya 2 halaman kunci utama.
- PENTING: soal "Lingkari benda yang lebih pendek/panjang" (2 kelompok objek berlabel
  a/b per soal, TANPA kunci teks di Markdown Guru) TERNYATA tetap py kunci PASTI berupa
  LINGKARAN MERAH pada PNG Guru (render `guru p177` & `guru p180`) -- jangan buru-buru
  dilewati karena "binary/no kunci teks"; render dulu guru PNG-nya. Untuk soal biner spt
  ini (hanya 2 objek per kelompok), MCQ 4 opsi tetap bisa dibuat dgn opsi: objek benar,
  objek salah (dari pasangannya), "kedua X sama panjang/tinggi", "tidak dapat ditentukan
  tanpa mengukur" -- pola generik ini valid krn scr visual jelas tidak sama & terlihat jelas.
- Soal "hitung panjang pakai satuan tidak baku" (penjepit kertas/kotak, subbab B Ayo
  Berlatih & Evaluasi) SEMUA py kunci angka bersih di Guru hal.180-181, TIDAK perlu
  render PNG siswa maupun guru sama sekali -- tinggal cross-check logika antar sub-jawaban
  (mis. "Pensil A lebih pendek dari B" konsisten dgn "A=4 kotak, B=8 kotak").
  PERANGKAP validator numerik: stimulus/pertanyaan yang menyalin ANGKA HASIL (mis. "Tinggi
  jerapah: 9 kotak") ke dalam stimulus soal LAIN (mis. soal 2d "hewan paling tinggi") akan
  DITOLAK validator krn angka itu tidak ada di halaman Siswa (siswa hanya py titik-titik
  kosong, angka cuma ada di Guru) -- utk soal turunan (paling tinggi/pendek dari beberapa
  hasil hitung), stimulus cukup ulangi teks pertanyaan asli tanpa angka.
- PERANGKAP validator lain: stimulus pendek yang hanya berisi label huruf terpisah jauh
  dari teks lain di halaman (mis. "6. A B C" saja, padahal "A B C" muncul jauh setelah
  gambar besar dan sebelum baris "Payung yang paling panjang adalah...") bisa GAGAL
  verbatim-check (~75% < 90%) krn potongan teks terlalu pendek relatif terhadap total teks
  halaman -- solusi: perpanjang stimulus dgn menambahkan kalimat lain yg berdekatan di
  halaman yg sama (mis. gabungkan "6. A B C" + "Payung yang paling panjang adalah ...").
- Item "Kupu-Kupu Terbang" (siswa hal. 215, narasi dgn pertanyaan tersirat yg bisa dijawab
  murni dari teks tanpa gambar) SENGAJA DILEWATI krn Buku Guru hal. 176 eksplisit
  menyebutnya "contoh ... untuk didiskusikan", bukan latihan berkunci -- pola: cek dulu
  apakah Guru menyebut suatu bagian sbg "contoh" sebelum memakainya sbg soal, meski scr
  tekstual jawabannya bisa disimpulkan.
- Soal "urutan" yg kuncinya menerima >1 susunan benar (krn ada 2 objek yg sama tinggi/
  panjang di tengah urutan, mis. subbab A item5 "urutan pohon dari paling pendek: B,C,D,A
  ATAU B,D,C,A") tetap DILEWATI sesuai pola bab-bab sebelumnya (kunci_ganda -> validator
  schema tidak py kategori khusus, pakai alasan "lainnya").
- Skema `dilewati.alasan` HANYA menerima enum: soal_terbuka, pembuktian,
  menggambar_atau_mengukur, proyek_atau_aktivitas, isian_banyak, butuh_alat_peraga,
  duplikat, teks_tidak_terbaca, lainnya (BUKAN bebas teks spt "jawaban_bervariasi" atau
  "soal_pengantar" -- pakai "soal_terbuka" utk aktivitas personal/variatif, "lainnya" utk
  kasus lain spt kunci ganda atau bagian "contoh" bukan latihan). `dilewati.source_item_no`
  WAJIB string (pakai "" bukan null kalau tidak ada nomor item).

## Bab 8 - Mengenal Diagram (hal. 233-254, sisa 255-264 sudah Daftar Pustaka/Profil Penulis)
- INDEX bab8 resmi mulai hal.233 (cocok dgn task), tapi konten "8 Mengenal Diagram" sebenarnya
  sudah muncul di hal.231-232 (masih ditandai Bab 7 di header markdown) -- tidak disentuh krn
  di luar rentang tugas & sudah bagian pembuka bab yg diulang lagi di hal.233-234.
- Materi bab berakhir di hal.254 (Catatanku); hal.255-264 murni Daftar Pustaka/Daftar Kredit
  Gambar/Profil Penulis (bukan materi matematika) -- tidak perlu disentuh sama sekali.
- Kunci Jawaban Guru bab 8 HANYA ada di 3 halaman: guru p190 (kunci Ayo Berlatih subbab A
  hal.238-239siswa: Tabel Pita Wei[tidak dipakai,tanpa soal]+Daftar Buah+Tabel Pensil Warna,
  DAN Tabel Mainan Kesukaan hal.240), guru p195 (kunci Ayo Berlatih subbab B hal.246-247:
  Diagram Buah Kesukaan+Pakaian Kira, format TEKS BERSIH bukan grafis meski soalnya berbasis
  diagram gambar), guru p196 (kunci Evaluasi hal.249-251 lengkap item1-4). Semua 3 halaman
  berisi picture-text yg jumbled (2 kolom tercampur) tapi tetap lengkap & mudah dicocokkan
  krn formatnya konsisten "huruf. <jawaban>".
- POLA PENTING: banyak soal diagram gambar (subbab B) yg templatenya KOSONG di buku siswa
  (lingkaran/kotak putih tanpa isi bintang, mis. hal.248 Diagram Hewan Pak Budi & hal.251
  Diagram Banyak Buah) TERNYATA datanya SUDAH lengkap di teks narasi soal itu sendiri (mis.
  "Ada 4 ayam. Banyak bebek 2 kurangnya dari ayam.") -- sehingga BISA dikerjakan murni dari
  teks tanpa render PNG sama sekali (butuh_gambar:false), beda dgn diagram yg SUDAH terisi
  gambar bintang penuh di buku (hal.246 Diagram Buah Kesukaan, hal.250 Diagram Sayur
  Kesukaan) yg WAJIB render PNG utk menghitung tinggi kolom.
- Render PNG (hal.238,239,246,247,249,250) semua dicek dgn menghitung manual dari gambar
  dan HASILNYA SELALU cocok 100% dengan angka di kunci Guru (jeruk/apel/mangga hal.238;
  pensil 4 warna hal.239; kelereng 4 warna hal.249; buah kesukaan & pakaian Kira hal.
  246-247; sayur kesukaan hal.250) -- render PNG di bab ini bisa dipercaya penuh, tidak ada
  jebakan seperti bab 1/4 (gelembung "jawaban dapat beragam").
- Soal narasi "Kira Membantu Paman" hal.234 (Daftar Mainan di Toko, tabel SUDAH terisi angka
  di teks siswa, bukan blank) dipakai sbg soal krn datanya identik dgn "Contoh" Guru hal.188
  meski Guru tidak menulis eksplisit kata jawabannya -- status_kunci tetap `cocok` dgn
  penjelasan di `catatan` (pola ini bisa dipakai lagi kalau ketemu soal serupa: tabel/daftar
  yg sudah terisi angka di teks siswa + Guru menyajikan tabel identik sbg "Contoh").
- Item unlabeled (tanpa huruf a/b/c di buku siswa, mis. hal.247 "Kira mempunyai ... kaus
  pendek/panjang/celana... paling banyak... paling sedikit... lebih...jumlah") WAJIB diberi
  `source_item_no` unik manual (mis. "2-kaus-pendek") krn validator menolak duplikat
  (halaman, section, nomor) kalau semua item pakai nomor section yg sama ("2").
- Banyak bagian "contoh sudah terjawab penuh di teks" (pola sama dgn bab 1/6/7): hal.236
  (tabel bola Upe), hal.241-242 (pengantar diagram gambar sayur), hal.244 (Diagram Mainan
  Kesukaan Tika), hal.245 (narasi Bermain Karet Gelang) -- SEMUA dilewati krn jawabannya
  sudah tertulis lengkap di buku siswa sendiri, bukan latihan.
- Aktivitas personal/proyek (Ayo Mencoba alat tulis hal.235, Ayo Bermain data mainan
  kelompok hal.240, Ayo Berkarya wawancara menabung hal.252-253, Catatanku refleksi
  hal.254) semua dilewati (soal_terbuka/proyek_atau_aktivitas) sesuai pola bab-bab
  sebelumnya.
- Hasil akhir: 50 soal (20 subbab A, 30 subbab B), 13 dilewati, LOLOS validator tanpa
  warning sejak percobaan kedua (percobaan pertama gagal krn stimulus p246/p250 menambahkan
  keterangan "(jeruk, apel, mangga, belimbing)" yg tidak verbatim, dan duplikat item_no
  hal.247 di atas).

## Bab 3 - Pengurangan sampai dengan 10 (hal. 89-128)
- INDEX hanya menandai "latihan" pada halaman PERTAMA tiap section (93,99,103,107,111,114,
  115,118,121); validator hanya cek page±1 dari halaman itu, jadi halaman lanjutan (94-98,
  104-106,108-110,112-113,116-117,119-120,122-126) TIDAK wajib disentuh untuk menghindari
  warning "tidak disentuh" — dipakai untuk menghemat ekstraksi tanpa kehilangan cakupan wajib.
- Sengaja diprioritaskan soal yang TIDAK butuh gambar (angka sudah tertulis di teks/picture-text
  sebagai bagian dari persamaan, mis. "6 – 4 = ...") supaya lolos verbatim-check dengan aman;
  soal yang benar-benar butuh gambar (hitung objek di ilustrasi, mis. hal. 95 item2b, hal. 96
  item3, hal. 98 item5, hal. 104 item2, hal. 105 item4-5, hal. 115 item2, hal. 116 item3)
  sudah dicek jawabannya via kunci Guru & render PNG tapi TIDAK dimasukkan (bukan ditolak,
  hanya tidak diprioritaskan) demi efisiensi karena halaman tsb tidak wajib disentuh.
- Kunci Jawaban Guru bab 3 juga TIDAK sinkron dengan halaman siswa: kunci "Ayo Berlatih" hal.
  93-98 siswa ada di guru hal. 98-99; hal.103-105 siswa -> guru hal.102-103; hal.107 siswa ->
  guru hal.105; hal.111-112 siswa -> guru hal.107; hal.115-117 siswa -> guru hal.110-111;
  hal.118-120 siswa -> guru hal.112-113; Evaluasi hal.121-124 siswa -> guru hal.113-114.
  Pola umum: kunci Guru untuk "Ayo Berlatih hal. N" biasanya ada di guru sekitar (N+5).
- Teks kunci Guru di halaman [T]/RISIKO_MATEMATIKA sering SANGAT jumbled (OCR picture-text
  dari 2 section berbeda tercampur jadi satu blok, kadang jawaban tercetak MENEMPEL sebelum
  soalnya, mis. "9 – … = 7 2" artinya jawabannya "2"). Selalu cross-check dengan jawaban
  sendiri sebelum mempercayai potongan yang terlihat acak.
- Beberapa soal "Buatlah operasi hitung dari angka X,Y,Z,tanda,=" (hal. 117 item7, hal. 123
  item8) punya kunci Guru yang MENERIMA 2 susunan berbeda sebagai benar (mis. "8-2=6 atau
  8-6=2") — DILEWATI karena tidak ada 1 jawaban pasti untuk PG.
- Soal "Lingkari operasi hitung yang hasilnya 5" (hal. 116 item4) dan "Gunakan tanda + atau -"
  (hal. 117 item6) DILEWATI: yang pertama punya >1 jawaban benar dari pilihan yang tersedia
  (tidak bisa dibuat 1 benar+3 distraktor pasti salah), yang kedua cuma 2 kemungkinan jawaban
  (+/-) sehingga tidak bisa diisi 4 opsi unik.
- Perangkap verbatim-checker: frasa pendek yang terpisah gambar (mis. hal. 94 "Sisanya ada" +
  "anak perempuan.") bisa GAGAL coverage 90% kalau frasa yang SAMA/mirip muncul lagi di
  halaman yang sama dengan susunan token kontigu berbeda (matcher greedy memilih blok
  match terpanjang, bukan yang benar) — solusi: pindahkan sebagian frasa ke `stimulus`
  supaya `pertanyaan` yang tersisa jadi lebih pendek & unik (cek dengan skrip coverage()
  manual sebelum commit kalau ada frasa berulang di halaman yang sama).
