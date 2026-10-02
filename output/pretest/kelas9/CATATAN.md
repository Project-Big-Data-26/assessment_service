# Catatan ekstraksi pretest kelas9

## Struktur umum buku kelas9 (SMP)
- Siswa PDF 320 hal., Guru PDF 288 hal. Guru punya penomoran halaman SENDIRI di
  footer (mis. Guru p0048 footer "36", p0072 footer "60") -- selalu pakai nomor
  file `p<PPPP>.md`, bukan angka footer, saat menulis `kunci_guru.halaman`.
- Bab 1 Siswa hal. 17-60 SECARA FISIK, tapi hal. 17-21 adalah bagian
  "Petunjuk Penggunaan Buku" / "Pemetaan Pikiran" (front matter) yang cuma
  KEBETULAN diberi tag "Bab 1" oleh converter karena posisinya. Isi bab yang
  sebenarnya (Tujuan Pembelajaran, dst.) baru mulai p0021. Front matter berisi
  cuplikan acak dari semua bab (termasuk contoh dari Bab 4) sebagai ilustrasi
  fitur buku -- JANGAN dipakai sebagai soal walau teksnya mirip soal asli.
- Bab 1 Guru hal. 39-92 (file), berisi "Kunci Jawaban Latihan A" di p0050 dan
  "Kunci Jawaban Latihan B" di p0072. Item bernomor di Latihan A/B guru
  BERSAMBUNG lintas sub-heading (Pemahaman Konsep + Penerapan Konsep jadi 1
  nomor urut 1..12), sedangkan di Siswa markdown, nomor urut PDF (lingkaran
  bernomor ①②③) sering ter-render jadi huruf "B", "C", "D"... di Markdown
  biasa -- WAJIB render PNG untuk memastikan nomor asli soal (mis. p0031,
  p0032, p0051 semua begitu).

## Pola notasi rusak
- Superscript/subscript dan pecahan sering rontok di Markdown biasa untuk
  angka + variabel (mis. "2 _x+y=_ 48" untuk "2x + y = 48", atau
  "_y_ = 35 000. _x_" untuk "y = 35.000x"). Selalu render PNG untuk halaman
  [M] sebelum menyalin notasi ke `pertanyaan`/`jawaban_benar`, lalu tulis
  ulang dalam LaTeX inline dan set `notasi_dari_png: true` HANYA jika bagian
  soal yang dipakai memang mengandung notasi rusak tsb (kalau soal yang
  dipakai cuma teks biasa di halaman [M], boleh `notasi_dari_png: false`,
  jelaskan di `catatan`).

## Kunci di Buku Guru -- Bab 1
- Latihan A (Persamaan Linear Dua Variabel): kunci di Guru p0050 (soal 1-2)
  dan p0051-p0052 (soal 3-5). Ayo Mencoba 1.1 (segitiga sama kaki, Siswa
  p0025) kuncinya di Guru p0048 "Alternatif Penyelesaian Ayo Mencoba 1.1".
- Latihan B (Sistem Persamaan Linear Dua Variabel): kunci mulai Guru p0072.
  Soal nomor 9 (Wayan/kue basung-mendut) kuncinya di Guru p0078 (footer 66),
  nomor 10 (kuas lukis) di Guru p0079 (footer 67). Nomor-nomor besar (9-12)
  ada di halaman guru yang JAUH dari awal "Kunci Jawaban Latihan B" (p0072)
  -- kalau grep angka spesifik dari soal (mis. "13.500", "1.103.000") lebih
  cepat daripada scroll berurutan dari p0072.

## Subbab Bab 1 (dari kurikulum)
- A: Persamaan Linear Dua Variabel (Latihan A, Siswa p0031-0032)
- B: Sistem Persamaan Linear Dua Variabel (Latihan B, Siswa p0049-0052)
- Prasyarat bab ini: SMP8-B3, SMP8-B5 (dari buku kelas8, belum diekstrak).

## Soal yang belum dipakai di Bab 1 (bukan berarti tidak layak)
2 soal/subbab sudah terpenuhi dari sumber yang paling bersih (Ayo Mencoba +
Latihan A/B nomor cerita). Latihan A/B masih punya banyak item lain (grafik,
metode eliminasi/substitusi/campuran, benar-salah, menjodohkan grafik) yang
belum diekstrak -- bisa dipakai kalau suatu saat perlu >2 soal/subbab atau
soal prasyarat untuk bab lain yang mensyaratkan Bab 1 ini.

## Bab 2 - Bangun Ruang (6 subbab A-F, halaman Siswa 61-154)
- Subbab Bab 2 PERSIS mengikuti nama "Latihan A" s.d. "Latihan F" di Siswa
  (A=Klasifikasi & Jaring-Jaring p0069, B=Luas Permukaan Sisi Datar p0079-80,
  C=Volume Sisi Datar p0098-99, D=Lingkaran p0115-16, E=Luas Permukaan Sisi
  Lengkung p0129-30, F=Volume Sisi Lengkung p0143-44) -- tidak perlu menebak
  subbab dari isi soal, tinggal cocokkan nama Latihan-nya.
- Penomoran soal di tiap Latihan TIDAK di-reset per Pemahaman/Penerapan
  Konsep: nomor lingkaran hitam (❶❷❸...) di PNG berjalan urut 1..n dari
  Pemahaman Konsep sampai Penerapan Konsep dalam satu Latihan, dan angka ini
  SAMA PERSIS dengan nomor di Kunci Jawaban Guru (mis. Latihan A: 1=Sebutkan
  jenis bangun ruang, 2=definisi jaring-jaring, 3=jaring-jaring bola,
  4=gambar bangun ruang, 5=gambar jaring-jaring). Di Markdown biasa nomor ini
  SERING berubah jadi huruf B, C, D... (bukan A -- itu sudah dipakai untuk
  heading). WAJIB render PNG sekali per Latihan untuk memastikan pemetaan
  huruf->angka, lalu pakai angka itu sebagai `source_item_no` dan untuk
  mencari padanan di Kunci Guru.
- Kunci Guru Bab 2: Latihan A -> Guru p0109; B -> p0118; C -> p0124-125;
  D -> p0137; E -> p0145-146; F -> p0153-154. Nomor soal Guru = nomor soal
  Siswa (lihat poin di atas), jadi tinggal cari nomor yang sama, tidak perlu
  grep angka spesifik untuk sebagian besar soal (grep tetap berguna untuk
  soal panjang/cerita, mis. "37.680", "6.720").
- **Kunci Guru SALAH di Latihan B nomor 6** (Guru p0118): soal minta LUAS
  PERMUKAAN kubus (rumus 6×s²) untuk 3 ukuran sisi berbeda, tapi kunci Guru
  menghitung VOLUME (s³) untuk ketiganya (mis. sisi 0,23 m -> Guru jawab
  0,012167 m² yang sebenarnya 0,23³, padahal jawaban benar 6×0,23²=0,3174
  m²). Konsisten salah di 6a/6b/6c. status_kunci dibuat `tidak_cocok` untuk
  6a di bab02.json.
- Unit pangkat (cm², m², dm³, dll.) di kutipan `kunci_guru`: JANGAN tulis
  sebagai "cm2" (huruf+angka nempel) karena validator men-tokenize itu jadi
  SATU token "cm2" yang tidak akan pernah cocok dengan sumber (yang setelah
  tag `<sup>2</sup>` dihapus menjadi token terpisah "cm" dan "2"). Solusinya:
  tulis pakai simbol unicode super/subscript asli ("cm²", "m³") supaya
  karakter pangkatnya didrop tokenizer dan tinggal token "cm"/"m" yang
  dicocokkan (angka lain di kutipan tetap harus persis).
- Banyak halaman "Ayo Mencoba"/"Ayo Berpikir Kritis/Kreatif"/"Eksplorasi" di
  antara tiap Latihan berisi soal cerita yang BAGUS (mis. p0073, p0095
  piramida Khafre, p0104, p0120, p0123, p0127, p0133, p0136 truk/bis
  beton/pipa) tapi sengaja tidak dipakai karena tiap subbab sudah cukup 2
  soal dari Latihan itu sendiri -- semuanya dicatat di `dilewati` dengan
  alasan "duplikat" supaya tidak memicu WARNING cakupan halaman. Kalau perlu
  >2 soal/subbab (mis. untuk soal prasyarat bab lain), halaman-halaman ini
  sumber yang bagus.
- Uji Pemahaman di akhir bab (p0146) isinya rekap definisi/rumus (isian
  titik-titik F-U) dan Benar/Salah (B-D) merangkum semua subbab -- tidak
  dipakai (alasan `isian_banyak`) karena tiap subbab sudah punya soal dari
  Latihan A-F masing-masing.

## Bab 3 - Transformasi Geometri (5 subbab A-E, halaman Siswa 157-234)
- Subbab: A=Translasi (Latihan A p0163-165), B=Refleksi (Latihan B p0184-185),
  C=Rotasi (Latihan C p0190-191), D=Kekongruenan (Latihan D p0210-211),
  E=Dilatasi (Latihan E p0219-221). Latihan tiap subbab jauh lebih pendek
  dari Bab 2 (cuma 1 halaman Pemahaman + 1 halaman Penerapan), jadi 2 soal
  langsung diambil dari situ, TIDAK perlu banyak "Ayo Mencoba" tambahan.
- Pola nomor lingkaran hitam ❶❷❸ -> huruf B,C,D... sama seperti Bab 2 (huruf
  A dipakai heading, jadi nomor mulai dari B=1). WAJIB render PNG sekali per
  Latihan untuk memetakan huruf ke angka asli (dipakai sebagai
  `source_item_no`, dan untuk mencari nomor yang sama di Kunci Guru).
- **AWAS: satu item bisa HILANG TOTAL dari Markdown meski terlihat jelas di
  PNG.** Latihan A item ❻ (p0165, "Diketahui titik A(3,-2) dan B(9,11)...")
  sama sekali tidak ada teksnya di p0164.md maupun p0165.md (tidak ada di
  mana pun, sudah di-grep) -- kemungkinan seluruh blok soal+opsi (yang
  memakai notasi vektor pecahan) ter-OCR sebagai satu gambar utuh. Soal ini
  TIDAK BISA dipakai (`teks_tidak_terbaca`) walau jawabannya kelihatan jelas
  di PNG dan di Kunci Guru, karena validator mensyaratkan pertanyaan
  verbatim ada di Markdown. Selalu grep potongan soal yang dicurigai hilang
  sebelum menuliskannya ke JSON.
- Notasi pecahan/vektor rontok dengan pola baru di bab ini: faktor skala
  dilatasi "1/2" di Latihan E Ayo Mencoba 3.14 (Siswa p0217) muncul di
  Markdown sebagai "[O, 2]" (angka "1" pembilang hilang total, bukan cuma
  format rusak) -- kalau tidak render PNG, akan salah kira faktor skala = 2.
  Selalu render PNG untuk setiap soal dilatasi/translasi dengan notasi
  pecahan/vektor sebelum menghitung jawaban.
- Soal menjodohkan dengan garis penghubung (Latihan B Refleksi item ❷,
  p0184: 7 jenis refleksi vs 7 hasil refleksi titik (2,-3)) -- daftar di
  Markdown Siswa DAN Guru sama-sama tidak menunjukkan pasangan yang benar
  (cuma daftar kiri lalu daftar kanan berurutan, garis panah hanya di
  gambar). Cara memastikan pasangan: hitung sendiri dengan rumus refleksi
  baku (semua 7 hasil di rumus PERSIS sama dengan 7 nilai yang tercetak,
  tidak ada sisa/kurang -- tanda kuat perhitungan benar), lalu render PNG
  Guru untuk verifikasi pola garis silang.
- **Kunci Guru salah ketik di Latihan C Rotasi nomor 3** (Guru p0192): hasil
  rotasi 90° CCW dari C(2,1) seharusnya C'(-1,2) (konsisten dengan rumus
  yang dipakai untuk A' dan B' di soal yang sama), tapi Guru menulis
  "C(1,-2)" yang adalah hasil rotasi 90° CW (arah terbalik). Dikonfirmasi
  lewat grafik Gambar 3.25 di halaman yang sama (C' tergambar dekat
  (-1,2)). status_kunci dibuat `tidak_cocok` untuk item ini di bab03.json.
- Kunci Guru Bab 3: Latihan A -> Guru p0170-171; B -> p0185; C -> p0192-193;
  D -> p0203-204; E -> p0210-211. Nomor soal Guru = nomor soal Siswa (sama
  seperti Bab 2). Ayo Mencoba tanpa nomor circle biasanya punya kunci di
  Guru berjudul "Alternatif Penyelesaian Ayo Mencoba <n.n>" tak jauh dari
  soalnya (mis. Ayo Mencoba 3.14 di Siswa p0217 -> Guru p0209).
- Unit luas (cm²) di kutipan `kunci_guru`: selain pakai simbol unicode
  superscript (bukan "cm2"), pastikan juga TIDAK menempelkan angka dengan
  huruf sebelumnya tanpa spasi (mis. "45cm" gagal tokenisasi jadi satu
  token "45cm" yang tidak pernah cocok dengan "45" + "cm" terpisah di
  sumber -- selalu tulis "45 cm" dengan spasi).
- Banyak halaman "Ayo Mencoba"/"Ayo Berpikir Kreatif/Kritis" di antara tiap
  Latihan (p0162, 174-176, 179, 181-183, 189, 197, 200, 205, 208, 218, 219)
  berisi soal translasi/refleksi/rotasi/dilatasi/kekongruenan yang bagus
  tapi sengaja tidak dipakai karena tiap subbab sudah cukup 2 soal dari
  Latihan itu sendiri -- dicatat di `dilewati` alasan `duplikat` (kecuali
  p0181 & p0200 yang memang `soal_terbuka`, p0197 `butuh_alat_peraga`,
  p0208 `pembuktian`). Kalau perlu >2 soal/subbab, halaman-halaman ini
  sumber yang bagus (tinggal render PNG untuk cek notasi pecahan/vektor).
- Uji Pemahaman akhir bab (p0224) isinya Benar/Salah rekap semua subbab
  (huruf B-I saja yang punya teks utuh di Markdown; sebagian nomor 1-10
  yang disebut intro tidak semuanya ter-OCR) -- tidak dipakai (`duplikat`)
  karena tiap subbab sudah punya 2 soal. Halaman p0225-234 (Uji Kompetensi
  nomor 11-13 menggambar, proyek desain batik GeoGebra, refleksi diri) juga
  tidak dipakai, tidak perlu di-dilewati satu-satu karena tidak bertanda
  `latihan` di index.json (tidak memicu WARNING cakupan halaman).

## Bab 4 - Peluang dan Pemilihan Sampel (4 subbab A-D, halaman Siswa 235-320) -- BAB TERAKHIR kelas9
- Subbab PERSIS mengikuti nama "Latihan A" s.d. "Latihan D" di Siswa (A=Peluang
  p0251-252, B=Peluang Empiris p0264-266, C=Frekuensi Harapan p0272-273,
  D=Pemilihan Sampel p0285-287) -- sama seperti pola Bab 2/3, tinggal cocokkan
  nama Latihan-nya, tidak perlu menebak dari isi.
- Pola huruf->angka SAMA seperti Bab 2/3 (huruf "A" terpakai untuk badge
  "Latihan A", jadi item pertama circled-1 muncul sebagai huruf "B" di
  Markdown, circled-2 sebagai "C", dst) DAN INI KONSISTEN DI SELURUH BAB,
  bahkan di halaman non-Latihan (mis. Tabel 4.7 di p0272 yang merupakan
  aktivitas TERPISAH sebelum "Latihan C" ternyata circled-numbernya memang
  numerik asli 1-5, bukan huruf, karena PNG-nya menampilkan digit sungguhan
  di badge itu -- jadi tetap WAJIB render PNG per Latihan untuk pastikan,
  jangan asumsikan semua circled shape di bab ini pasti huruf).
- Kunci Guru Bab 4: Latihan A -> Guru p0243-244; B -> p0253; C -> p0261;
  D -> p0269. Nomor soal Guru = nomor soal Siswa (huruf B,C,D...->1,2,3...
  seperti di atas), grep angka spesifik tetap berguna untuk soal cerita
  panjang (mis. "407", "93", "10/125").
- **Kunci Guru SALAH LABEL di Ayo Mencoba 4.6** (Siswa p0263, Guru p0253):
  soal minta banyak kartu lingkaran & bintang dari data (Lingkaran muncul
  407/500, Bintang 93/500, total 5 kartu). Guru menghitung 93/500x5=0,93≈1
  lalu MENYEBUTNYA "kartu bergambar lingkaran" dan sisanya (4) "bergambar
  bintang" -- terbalik, karena 93 itu data BINTANG bukan lingkaran. Angka
  hitungannya benar, cuma labelnya tertukar. status_kunci `tidak_cocok`
  untuk soal ini di bab04.json.
- Fraksi/pecahan yang dipisah tanda "/" kadang RONTOK di Markdown biasa
  walau halamannya TIDAK ditandai [M] (mis. Guru p0253 kunci Latihan B
  nomor 4 "2/12 = 1/6" tercetak sebagai baris terpisah "2 1" dan "12 6"
  tanpa tanda "/" sama sekali) -- selalu render PNG Guru untuk memverifikasi
  kutipan kunci pecahan meskipun halamannya tidak bertanda [M], dan pakai
  `dari_png: true` kalau susunannya kacau di Markdown.
- Simbol pecahan unicode "½" (bukan teks "1/2") di kutipan kunci Guru
  (mis. p0244 "P(A) = ½.") membuat validator tidak mendeteksi digit apa pun
  di kutipan (regex `\d+` tidak menangkap "½"), sehingga memicu WARNING
  "kutipan tidak memuat angka jawaban" walau kutipannya sudah benar --
  WARNING ini aman diabaikan (dijelaskan di `catatan`), JANGAN mengubah
  kutipan jadi "1/2" karena itu bukan teks yang benar-benar tercetak di
  halaman (angka "1"/"2" ASCII tidak akan ditemukan di sana, malah memicu
  ERROR "angka tidak ada di halaman").
- Item soal "sudah 3-opsi" di buku (mis. Latihan D nomor 6, Dhien memilih
  cara sampling OSIS dari opsi ⓐⓑⓒ) bisa langsung dipakai sebagai PG:
  2 opsi salah dari buku dipakai sebagai distraktor, tambah 1 distraktor
  buatan (miskonsepsi baru, mis. convenience sampling) supaya genap 4 opsi.
- Bab ini TIDAK kena masalah front matter Bab 1 (halaman 235 awal bab
  langsung "Tujuan Pembelajaran", tidak ada cuplikan acak bab lain) dan
  tidak ditemukan pola "soal hilang total dari Markdown" seperti Bab 3.
- Latihan A-D semuanya cukup 2 soal/subbab dari item Penerapan Konsep-nya
  sendiri; banyak halaman "Ayo Mencoba"/"Ayo Berpikir Kreatif/Kritis" di
  antaranya (p0243, 246, 249, 255, 260, 270, 276, 284) dan "Uji Pemahaman"
  rekap di akhir (p0289) dicatat `dilewati` alasan `duplikat` -- bisa
  dipakai kalau perlu >2 soal/subbab atau soal prasyarat bab lain yang
  mensyaratkan Bab 4 ini.
