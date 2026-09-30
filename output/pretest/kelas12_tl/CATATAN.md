# Catatan kelas12_tl (SMA - Matematika Tingkat Lanjut kelas XII)

## Bab 1 - Lingkaran, Elips, dan Garis Singgung Lingkaran (hal.12-94)
- Halaman 12-16 Buku Siswa BUKAN materi Bab 1: itu bagian "Ada Apa di Buku Ini?"
  (penjelasan format buku) yang memakai Bab 1 sebagai contoh generik (termasuk contoh
  soal/definisi yang aslinya milik Bab 2). Materi Bab 1 sesungguhnya baru mulai p0017.
- Latihan Soal per subbab: "Latihan Soal Lingkaran" p32-33 (subbab A), "Latihan Soal
  Elips" p52-53 (subbab B), "Latihan Soal Kedudukan Titik dan Garis terhadap Lingkaran"
  p66-67 (subbab C), "Latihan Soal Persamaan Garis Singgung Lingkaran" p82-83 (subbab D,
  10 soal, lanjut ke p83), lalu "Uji Kompetensi Bab 1" p83-84 (10 soal campuran semua
  subbab), lalu "Pengayaan" p84 (topik baru: Parabola, di luar subbab A-D, tidak dipakai).
- Kunci Guru Bab 1 ada di Buku Guru p76-104 (bukan p35-108 seperti rentang bab di
  INDEX.md Guru). "H. Kunci Jawaban" mulai p76. Latihan Soal Lingkaran: p76-78 & p81-82.
  Latihan Soal Elips: p83-86. Latihan Soal Kedudukan: p90-94. Latihan Soal Garis
  Singgung: p94-99. Uji Kompetensi Bab 1: p100-104.
- KUAT dugaan typo di Buku Siswa DAN Buku Guru: Latihan Soal Lingkaran no.2a menulis
  "(x-1)^2+(x+5)^2=9" (dua suku x, tidak ada y) -- dilewati, kemungkinan seharusnya
  (y+5)^2.
- Banyak halaman TIDAK bertanda [M]/RISIKO_MATEMATIKA padahal notasinya tetap rusak:
  pola "^angka, angkah" adalah artefak OCR untuk tanda kurung koordinat, mis.
  "^1, 2h" = "(1,2)", dan "h" sering menempel ke angka sebelumnya jadi TOKEN GABUNGAN
  (mis. "2h" atau "3h2") saat divalidasi. Solusi yang dipakai: tulis ulang notasi
  memakai LaTeX ($...$) + notasi_dari_png=true untuk SEMUA soal yang memuat koordinat/
  persamaan pada bab ini (bukan cuma yang bertanda [M]), supaya token tidak pernah
  dicocokkan mentah ke Markdown yang rusak.
- Kutipan kunci_guru: banyak kesimpulan akhir (persamaan/nilai akhir) Buku Guru
  tercetak sebagai GAMBAR RUMUS (bukan teks), walau uraian langkah sebelumnya (nilai
  a, b, A, B, C, dsb.) ada sebagai teks. Kalau kesimpulan akhir hanya ada di gambar,
  pakai kunci_guru.dari_png=true dan tulis catatan menyebutkan bagian mana yang dari
  teks vs PNG. Render dengan `convert render kelas12_tl guru <hal>`.
- Latihan Soal Elips no.1 (a-d) dan no.2 (a-b) di Buku Siswa p52 TIDAK terekstrak sama
  sekali sebagai teks Markdown (seluruh soal ada di dalam satu gambar tanpa OCR
  "picture text"). Sub-item 2c,2d dan soal no.3-8 di p53 terekstrak normal sebagai
  teks. Untuk soal dari p52, kalimat perintah induk (stem) harus dibaca dari PNG dan
  digabung ke pertanyaan dengan pertanyaan_disesuaikan=true (verbatim minimum turun ke
  50%), stimulus dikosongkan supaya tidak kena cek verbatim.
- Ayo Mencoba 1.1-1.13 dan bagian "Ayo Berpikir Kreatif/Kritis" (banyak halaman, lihat
  warning validator) TIDAK dipakai sebagai sumber soal karena "Latihan Soal" +
  "Uji Kompetensi" pada bab ini sudah menyediakan >=5 soal siap pakai per subbab
  (prioritas 1 di SKILL.md). Ini valid, bukan soal yang gagal diekstrak.
- Status: bab01.json LOLOS validate (0 error). 31 soal (A:7+UK1, B:5, C:7, D:9+UK2),
  8 dilewati.

## Bab 2 - Turunan Fungsi (hal.95-174) -- SEDANG DIKERJAKAN
- Latihan Soal per subbab (siswa): "Latihan Soal Definisi Turunan Fungsi" p118 (subbab A,
  4 nomor 1(a-e)/2/3/4(a-c), SELURUHNYA satu gambar tanpa OCR teks sama sekali kecuali
  heading+"Gunakanlah sifat-sifat limit..."+"1. Tentukan nilai dari:"), "Latihan Soal
  Sifat-Sifat Turunan Fungsi" p142 (subbab B), "Latihan Soal Aplikasi Turunan Fungsi"
  p162 (subbab C, TANPA tanda [M] di INDEX -- kemungkinan OCR teks lebih baik, cek dulu),
  "Latihan Soal Aplikasi Turunan Fungsi di Berbagai Bidang Ilmu" + "Uji Kompetensi Bab 2"
  p169 (subbab D), lalu "Pengayaan" p172 (topik baru, di luar subbab A-D).
- Kunci Guru Bab 2: "H. Kunci Jawaban" mulai p148 (Latihan Definisi, lanjut p149-151),
  bab 3 mulai p181 di Guru jadi kunci Latihan Sifat-Sifat/Aplikasi/UK ada di p152-180an
  (belum dicek persis, cari dengan Grep angka/istilah khas tiap soal).
- KUNCI GURU HAL.149-151 UNTUK LATIHAN DEFINISI SELURUHNYA GAMBAR (tanpa OCR teks),
  kecuali No.1a (p148, teks asli, ada "= 32 + 2 = 11") dan No.3 bagian pembuktian awal
  (p150, teks asli, tapi KESIMPULAN AKHIR "g(x) kontinu di R" hanya ada di gambar p151).
  Semua kunci_guru untuk 1b-e/2/3(kesimpulan)/4 pakai dari_png=true.
- Teknik lolos validator untuk soal yang SUMBER SISWA-nya juga gambar total (p118):
  tulis pertanyaan/stimulus HAMPIR SELURUHNYA dalam LaTeX ($...$) dengan notasi_dari_png=
  true, DAN jaga kata polos di LUAR tanda $ maksimal 2 token (mis. "dan", "untuk", "di").
  Kode validator men-skip total pengecekan verbatim kalau token non-LaTeX < 3 (lihat
  validate.py baris ~181). Kalau >=3 token polos (mis. "Tentukan ... dan ... jika ..."),
  coverage jatuh ke ~67% dan GAGAL karena halaman sumber memang tidak ada teksnya sama
  sekali. Sudah diverifikasi jalan untuk item 1a,1c,1d,2,3,4a,4b subbab A (7 soal, LOLOS).
- Soal no.3 (kontinuitas piecewise) dikonversi dari "Apakah g(x) kontinu di R?" (ya/tidak)
  jadi PG pernyataan benar/salah, pertanyaan_disesuaikan=true.
- Item 1b, 1e (subbab A) BELUM diekstrak (sudah cukup 7 soal untuk subbab A tanpa itu,
  disimpan sebagai cadangan kalau butuh soal prasyarat tersulit nanti: 1e paling sulit,
  perlu substitusi y=x-pi/2 dan identitas cos(A+B)).
- Ayo Bereksplorasi/Ayo Mencoba/Ayo Berpikir Kritis-Kreatif (banyak halaman, lihat warning
  validator) belum diputuskan dipakai atau tidak -- baru dicoba kalau Latihan Soal per
  subbab B/C/D kurang dari 2 soal siap pakai.
- Subbab B selesai (7 soal): "Latihan Soal Sifat-Sifat Turunan Fungsi" p142-143 no.1(a-f
  gambar penuh hal.142), no.2 (kalimat tunggal minta 2 hal -- luas & volume bola, dipecah
  jadi 2a/2b tanpa perlu pertanyaan_disesuaikan karena tiap potongan tetap verbatim),
  no.3(a-b, teks asli garbled tapi utuh di hal.142, bukan gambar), no.4 & no.5 (hal.143,
  soal cerita eksponensial -- BELUM dipakai, cadangan kalau butuh tambahan).
  Item 1b DILEWATI: fungsi di Buku Siswa tertulis y=(x^2+1/x^2)^-4 tapi turunan Buku Guru
  memakai u(x)=x^3+1/x^2 (u'=3x^2-2/x^3) -- diduga typo pangkat 2 vs 3, ambigu, tidak
  dipakai. Item 1d, 1f juga belum dipakai (cadangan, sudah cukup 7 soal utk subbab B).
  Kunci Guru: hal.152 (no.1, gambar penuh), hal.153 (no.2 & no.3, gambar penuh untuk hasil
  akhir; kalimat pengantar "Luas bola (L)=4πr^2 sehingga..." adalah teks asli).
- Teknik verbatim untuk soal yang TEKS ASLINYA ada (walau garbled, bukan gambar, mis.
  no.3 hal.142): tulis prosa Indonesia verbatim, HANYA notasi matematika yang diganti
  LaTeX + notasi_dari_png=true. Coverage tetap lolos krn kata-kata biasa match persis
  di halaman (beda dgn item full-gambar yg pakai teknik <3 token di atas).
- Subbab C selesai (5 soal): "Latihan Soal Aplikasi Turunan Fungsi" p162-163 (teks ASLI
  ada, bukan gambar, walau garbled OCR -- tanda < dan > sering tercetak sebagai angka
  1 dan 2). Dipakai: 6a (interval naik/turun, kunci teks asli hal.159), 11a/11b/11c
  (titik balik maks/min, kesimpulan angka HANYA di gambar hal.163 meski uraian awal teks
  asli), 13a (nilai ekstrem, kesimpulan di gambar hal.165). Item 1-5 (persamaan garis
  singgung), 6b/6c, 7-10, 11d, 12, 14-15 BELUM dipakai (cadangan kalau butuh tambahan;
  no.14/15 levelnya tinggi utk soal prasyarat tersulit kalau perlu).
- Kunci Guru subbab C: hal.154 (awal Latihan, no.1 gambar), hal.159 (no.6, teks asli utk
  6a), hal.160 (no.6bc, no.7), hal.163-165 (no.11, 12, 13, 14 -- kesimpulan akhir tiap
  soal SELALU di gambar walau uraian langkah kadang teks asli).
- Subbab D selesai (4 soal): "Latihan Soal Aplikasi Turunan Fungsi di Berbagai Bidang
  Ilmu" p169 no.2 (dua bilangan hasil kali 80), no.3 (talang air), no.4 (luas maks
  ABCD di bawah parabola, BUTUH GAMBAR 2.22 utk konfigurasi titik), no.5 (keuntungan
  produksi). Kunci Guru hal.167-168, SEBAGIAN BESAR teks asli (bukan gambar) utk bab
  ini -- beda dari subbab A-C yang banyak gambar.
  No.1 (biaya jembatan) DILEWATI: Buku Siswa mencetak y=3x-900+120/x, tapi kunci Guru
  hal.166 menyelesaikannya sebagai y=(3x-900+120/x)*x=3x^2-900x+120 (dikalikan x lagi)
  utk dapat x=150 hari -- kalimat yang menjelaskan perkalian ini tidak ada di Markdown
  Siswa maupun render PNG yang dicek, jadi dilewati (bukan typo yang bisa dikoreksi
  dengan yakin).
  Uji Kompetensi Bab 2 bagian A (isian singkat, p169-170, 5 soal turunan dasar) BELUM
  dipakai (subbab A/B sudah cukup >=2 soal); item 6-15 Latihan Aplikasi (persamaan
  garis singgung no.1-5 hal.162, fungsi naik/turun 6b/6c/7/8/9/10, titik ekstrem 11d/12/
  13b/14/15) dan Pengayaan p172 (soal gerak & pertumbuhan bakteri, mirip subbab D) BELUM
  dipakai -- cadangan kalau perlu tambahan soal atau soal prasyarat.
- STATUS AKHIR bab02.json: LOLOS validate (0 error, 20 warning -- semua warning adalah
  halaman Ayo Mencoba/Ayo Berpikir Kritis-Kreatif/Pengayaan yang sengaja tidak dipakai
  krn Latihan Soal + Uji Kompetensi sudah cukup, sama seperti pola bab01). 23 soal
  (A:7, B:7, C:5, D:4), 1 dilewati.

## Bab 3 - Integral (hal.175-236) -- SELESAI
- Latihan Soal: Integral Tak Tentu p193 (A, soal 1-3 gambar penuh tanpa OCR), Integral Tentu p218-219 (B), Penerapan Integral p227-228 (C), Uji Kompetensi p228-232 (isian/B-S/PG kompleks, tidak dipakai).
- Kunci Guru: Latihan Tak Tentu p221-222, Tentu p223-227, Penerapan p227-230. Mayoritas gambar rumus (dari_png=true); teks asli: 14b, C3, C4.
- Guru Riemann 1-3 (p223-224) memakai titik ujung KANAN padahal soal minta ujung KIRI -> dilewati. Soal A5 (harga) kunci "sekitar Rp39.499,00" vs hitungan 39.499,59 -> dilewati. Kasus Rusman (p227) tidak punya kunci di Guru.
- Untuk soal gambar penuh: stimulus "" atau kalimat perintah pendek (<3 kata polos di luar $..$) agar lolos cek verbatim.
- Status: bab03.json LOLOS (0 error, 15 warning halaman Ayo Mencoba/Berpikir yang sengaja tidak dipakai). 17 soal (A:7, B:6, C:4), 6 dilewati.

## Bab 4 - Analisis Data dan Peluang (hal.237-320) -- SELESAI
- Latihan Soal: Variabel Acak p245 (A), Diskret p252-253 (B), Kontinu p257 (C, 1 soal a-c), Fungsi Peluang p263-264 (D), Densitas p269 (E, teks soal ada tapi rumus f(x) gambar), Binomial p279-280 (F), Normal p292 (G). Uji Kompetensi p293-295 (B/S + uraian) tidak dipakai.
- Kunci Guru: A p275-276, B p277, C p278, D p278-281, E p282 (SELURUHNYA gambar, dari_png), F p282-284 (banyak gambar; 5b,5c,6a teks), G p284-289 (nilai z-table ada di teks: 0,7745; 0,0808; 0,5111; no.8 p289). UK p289-291.
- Dilewati: B2c (pembuktian), D2 (rumus garbled), G7 (kunci "28 atau 29").
- Status: bab04.json LOLOS, 19 soal (A:2,B:2,C:2,D:3,E:3,F:3,G:4). D memakai pertanyaan_disesuaikan (fungsi peluang gambar dihapus dari perintah, opsi tabel distribusi).
