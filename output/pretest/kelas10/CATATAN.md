# CATATAN kelas10

## Bab 1
- Mode lengkap, 4 subbab (A Definisi Eksponen, B Sifat-Sifat Eksponen, C Fungsi Eksponensial,
  D Bentuk Akar) x 2 soal = 8 soal, semua status_kunci cocok kecuali 1 tidak_cocok.
- Kuirk pencetakan: SEMUA Eksplorasi/Latihan di Bab 1 Siswa berlabel "2.x" (bukan "1.x"),
  cth. "Eksplorasi 2.1", "Latihan 2.1" .. "2.6" -- dicek dari PNG, memang tercetak begitu (bukan
  typo OCR). Guru menyebutnya "Eksplorasi/Latihan 1.x" (mengikuti nomor bab yang benar).
  Kalau menemukan pola serupa di bab lain, cek PNG dulu sebelum menganggap typo.
- Guru Bab 1 Eksponen berada di halaman yang INDEX Guru label salah ("Bab 4 - Sistem
  Persamaan..." p27-p158), tapi footer halamannya sendiri konsisten "Bab 3 | Eksponen".
  Kunci Jawaban Latihan 1.1 (=Siswa Latihan 2.1) di p0045-0046, Latihan 1.2 (=Siswa 2.2,
  pertumbuhan) di p0051-0054, Latihan 1.3 (=Siswa 2.3, peluruhan) di p0055-0056, Latihan 1.4
  (=Siswa 2.4, bentuk akar) di p0061-0062, Latihan 1.5 di p0063, Uji Kompetensi di p0067.
- Latihan 2.1 no.2b (Siswa p25) tercetak "b^p . b^5 = 3^9" -- typo, RHS seharusnya "b^9"
  (dikonfirmasi dari Kunci Guru p46 yang langsung menulis "b^4.b^5=b^9", p=4). Soal
  dilewati karena sebagaimana tercetak tidak punya jawaban unik.
- Latihan 2.3 no.2 (Siswa p36, peluruhan zat radioaktif): Kunci Guru p55 menghitung
  f(8)=0,3x0,85^8=0,08172 kg dengan benar (fungsi f(x) didefinisikan sebagai massa yang
  TERSISA), tapi lalu keliru mengurangkan 300-81,72=218,28 gram sebagai "sisa" -- kontradiksi
  dengan definisi f(x) sendiri. status_kunci=tidak_cocok, jawaban_benar pakai f(8)=81,72 gram.
- Kunci Latihan 1.1 (p46) dan 1.4 (p61-p62) nilainya HANYA ada di gambar (raw markdown
  cuma berisi label "a. b. c." kosong) -- wajib render PNG Guru, dari_png=true.
- Halaman 43-49 (setelah D. Bentuk Akar) sudah masuk materi Logaritma (Eksplorasi Logaritma,
  Latihan 2.6, dst), TAPI Prasyarat_Math.xlsx Bab 1 hanya punya subbab A-D (tidak ada
  subbab Logaritma) -- semua soal Logaritma di halaman ini masuk dilewati (alasan lainnya).
- Beberapa soal cerita (HIV-AIDS, hoaks, dsb) di halaman ber-flag [M] tidak mengandung
  rumus sama sekali (notasi cuma ada di bagian lain halaman itu) -> notasi_dari_png=false
  wajar, validator tetap kasih WARNING "abaikan kalau soal ini tanpa rumus" (memang begitu).

## Bab 2
- UPDATE: mode diubah dari "prasyarat" ke "lengkap" karena bab ini juga butuh subbab A "Barisan"
  dan B "Deret" utk pretest bab itu sendiri (bukan cuma sumber prasyarat bab lain).
  Subbab A: Latihan 2.1 no.2 (suku ke-50, p59, kunci Guru p79) & no.5 (Ivan permen, suku
  ke-10, p60, kunci Guru p81). Subbab B: Latihan 2.3 no.1 (jumlah kelipatan 4, p74-75, kunci
  Guru p91) & no.4 (Vina permen, deret aritmetika, p75, kunci Guru p92). Semua status_kunci
  cocok. Guru Bab 2 di halaman yang INDEX Guru label salah ("Bab 4 - Sistem Persamaan...");
  footer halaman sendiri konsisten "Bab 2 | Barisan dan Deret" (p79, p81, p91, p92 dicek).
- Latihan 2.1 (Barisan Aritmetika, p59-60), 2.2 (Barisan Geometri, p65-66, "1a" notasi
  pecahan bertingkat rusak, RISIKO sup/sub) = subbab A. Latihan 2.3 (Deret Aritmetika,
  p74-75), 2.4 (Deret Geometri Tak Hingga, p77-78, no.1 & no.2 jawabannya RANGE nilai
  bukan tunggal krn r bebas -> soal_terbuka) = subbab B. Latihan 2.5 (p79, Uji halaman
  campuran barisan+deret) & Uji Kompetensi p84 tidak dipakai krn kuota A/B sudah terpenuhi,
  tapi keduanya kandidat cadangan bagus (banyak item bersih tanpa masalah notasi).
- Banyak Eksplorasi/Ayo Berpikir Kritis/Kreatif/Berefleksi subbab A & B adalah diskusi
  terbuka atau tabel checklist refleksi diri (bukan soal) -> semua dilewati (soal_terbuka
  atau "lainnya"), lihat `dilewati` di bab02.json utk daftar lengkap per halaman 61-78.
- Mode prasyarat (SEBELUM update di atas), subbab terakhir = C "Bunga" (Siswa hal. 80-83: Eksplorasi 2.8, 2.9, Latihan 2.6). Uji Kompetensi hal. 84 TIDAK memuat soal bunga.
- Kunci Latihan 2.6 + Eksplorasi 2.9 ada di Guru p0104-p0105 (INDEX Guru salah label bab "Bab 4"; footer "Bab 2 | Barisan dan Deret"). Kunci Uji Kompetensi Bab 2 di Guru p0106-p0108.
- Kesalahan Guru: no. 3 (Made) memakai bunga 8% padahal Siswa 4% (cicilan benar Rp112.500, bukan 120.833); no. 4 (Dina) memakai 7% padahal Siswa 3% (dicek dari PNG Siswa hal. 83).
- Kunci Eksplorasi 2.9 (Guru p0104) tidak konsisten: U1 = 1.000.000 dan Un = 1.000.000 x 1,05^n, padahal tabungan tahun ke-1 = 1.050.000.
- Kutipan Guru dengan angka format "10 _._ 300 _._ 000" lolos validator bila disalin persis.

## Bab 3
- Mode lengkap, 2 subbab (A Perbandingan Trigonometri p91-103, B Pemanfaatan Perbandingan
  Trigonometri p104-121) x 2 soal = 4 soal, semua status_kunci cocok. Header "B." ada di
  Siswa p104. Guru Bab 3 di halaman yang INDEX Guru label salah ("Bab 4 - Sistem Persamaan..."
  p117-p137), tapi footer halaman sendiri konsisten "Bab 3 | Perbandingan Trigonometri" (BEDA
  dengan Bab 1: di sini tidak ada kuirk penomoran Latihan, "Latihan 3.x" Siswa = "Latihan 3.x"
  Guru, sama persis).
- Kunci Latihan 3.1 p117, 3.2+3.3 p119, 3.4 p120, 3.5 p127, 3.6 p129, 3.7+Uji Kompetensi p131
  (index Guru); nilai Latihan 3.3 no.1 (a & b, tinggi orang dewasa via Gambar 3.15) HANYA ada
  di gambar Guru p120 (markdown mentah cuma "a. Menggunakan segitiga sebangun" kosong) --
  wajib render PNG, dari_png=true. Nilai y=173,85 cm benar & konsisten utk metode sebangun & trig.
  Latihan 3.7 no.1 (z=18,4, x=15,94) & Latihan 3.5 no.1 ada di teks biasa Guru (dari_png=false).
- Guru Latihan 3.5 no.1b salah ketik "cos 35,8°" (seharusnya 36,8° sesuai ∠Q pada soal Siswa
  & opsi Siswa sendiri "ii. Cos 36,8"); pilihan "ii" yang dimaksud tetap sama -> status_kunci
  cocok, jawaban_benar pakai angka Siswa yang benar (36,8°).
- Banyak soal Latihan (3.1 no.1, 3.2 no.1, Uji Kompetensi no.3) butuh render PNG utk memastikan
  posisi sudut siku-siku / sisi mana yang mana (TEKS_DALAM_GAMBAR sering scramble urutan
  angka vs label huruf) -- selalu render sebelum menyimpulkan geometrinya.
- Uji Kompetensi hal.119 no.1 ("Jika cos x = 20/29, cari sin x dan tan x") adalah soal bagus
  tanpa perlu gambar (segitiga Pythagoras 20-21-29) -- TIDAK dipakai di sini karena kuota
  sudah terpenuhi dari Latihan 3.3/3.5/3.7, tapi layak jadi calon utama kalau butuh soal
  tambahan/prasyarat dari Bab 3 di masa depan.
- Banyak halaman bab ini berisi proyek (klinometer p102-103), eksplorasi pengukuran mandiri
  (Ayo Mencoba p92, Latihan 3.2 no.2-5 p96), atau soal terbuka/pembuktian (Ayo Berpikir Kreatif/
  Kritis) -- lihat `dilewati` di bab03.json utk daftar lengkap alasannya.

## Bab 4
- Mode lengkap, 2 subbab (A Sistem Persamaan Linear p125-134, B Sistem Pertidaksamaan Linear
  p135-144) x 2 soal = 4 soal, semua status_kunci cocok. TIDAK ada halaman [M] di bab ini
  (siswa maupun guru) -- tidak perlu render PNG sama sekali.
- Guru Bab 4 di halaman yang INDEX Guru label salah ("Bab 4 - Sistem Persamaan..." p17-p158,
  gabungan Bab 1/2/3/4 asli), tapi footer halaman sendiri konsisten "Bab 4 | Sistem Persamaan
  dan Pertidaksamaan Linear". Kunci Latihan 4.1 di Guru p143-144, Ayo Berpikir Kritis (0,0)
  di p149 (dalam gambar "Masalah > Model Matematika > ... > Ayo, Berpikir Kritis a. Ya b.
  Tidak" tapi teksnya terbaca utuh di markdown, TIDAK perlu render), Kunci Latihan 4.2 di
  p149-152, Uji Kompetensi mulai p152.
- Kunci Guru utk "a. Ya b. Tidak" (p149) sangat singkat tanpa bukti angka -> validator warning
  "kutipan tidak memuat angka jawaban", wajar & sudah dijelaskan di catatan tiap soal (bukan
  bug); pembuktian substitusi (2(0)+5(0)=0<10, 6(0)+2(0)=0>10) dikerjakan mandiri, konsisten.
- Banyak Eksplorasi bab ini (4.1 Menimbang Bola p126-129, 4.2 Menimbang Buah p135,
  4.3 Perayaan Kemerdekaan p137-139) memakai strategi "coba dan perbaiki" / menimbang benda
  sungguhan -- Kunci Guru sendiri eksplisit menyatakan "ada lebih dari 1 (set) kemungkinan
  jawaban" atau memberi beberapa contoh berbeda, jadi SEMUA soal Eksplorasi bab ini dilewati
  (soal_terbuka/butuh_alat_peraga), bukan cuma sebagian.
- Banyak soal Latihan 4.1 no.4-5 (p134) dan Uji Kompetensi no.1 (p141) merujuk ke paket/rumus
  yang HANYA ada di gambar (markdown mentah kosong/kode huruf A-H) -- butuh render PNG kalau
  suatu saat dipakai. Uji Kompetensi no.3/4/6 (p142, SPL 3 variabel bersih, solusi tunggal)
  dan Latihan 4.2 no.3 (Bu Dini beli telur, p140, Ya/contoh 4kg+2kg di Guru p151-152) adalah
  kandidat cadangan bagus yang TIDAK terpakai karena kuota sudah terpenuhi dari soal lain.

## Bab 5
- Mode lengkap, 2 subbab (A Persamaan Kuadrat p148-164, B Fungsi Kuadrat p165-194) x 2 soal
  = 4 soal. Header "B. Fungsi Kuadrat" muncul DI TENGAH p0165 (sesudah Latihan 5.5), jadi
  Latihan 5.5 (diskriminan) masih subbab A, Latihan 5.6 dst subbab B.
  Guru Bab 5 di halaman yang INDEX Guru label benar ("Bab 5 - Persamaan dan Fungsi Kuadrat"
  p159-208, tanpa kuirk penomoran bab seperti Bab 1/3/4), Kunci Latihan 5.1 p165, 5.2
  p168-169, 5.3 p175, 5.4 p178, 5.5 p180, Eksplorasi 5.6 p183, 5.6 p189, 5.7 p190-191,
  5.8 p192, 5.9 p197-198, 5.10 p201.
- Token validator: variabel selalu ditulis `_x_` (underscore) di Markdown, sehingga
  underscore memisahkan angka dari huruf jadi token TERPISAH ("2", "x", "2" bukan "2x2").
  Kalau pertanyaan menulis "2x²" (digabung tanpa spasi/underscore) -> tokenizer gabung jadi
  1 token "2x" yang TIDAK ADA di halaman -> ERROR "angka tidak ada". Solusi: tulis
  pertanyaan/kutipan pakai LaTeX inline `$2x^2-8x+6=0$` + `notasi_dari_png:true` (LaTeX
  di-strip sebelum dicek), ATAU salin literal markdown mentah dg underscore+`<sup>` utk kutipan
  Guru (`_x_<sup>2</sup>`) supaya tokennya persis sama dengan halaman.
- Kunci Guru Latihan 5.2 no.5 (p0169, `2x²-18=0`) SALAH CETAK: sesudah benar menulis
  `(x+3)(x-3)=0`, baris berikutnya menuliskan KEDUA faktor sebagai `(x+3)=0` sehingga
  hasilnya `x=-3` dan `x=-3` (bukan x=3). Dikonfirmasi dari render PNG Guru p0169 (memang
  tercetak begitu, bukan OCR). status_kunci=tidak_cocok, jawaban_benar=x=3 atau x=-3.
- Kunci Latihan 5.9 no.2 (bola dilempar, p180) HANYA ada di gambar formula Guru p0198
  (markdown mentah kosong sesudah "maka Fungsinya atau") -- wajib render PNG, dari_png=true.
  Nilai a=-1, f(x)=-x²+4x+4 (dari titik puncak (2,8) & titik (0,4)), konsisten dgn hitungan
  mandiri.
- Banyak Latihan (5.1 p150, 5.3 p161, 5.4 p163, 5.5 p165, 5.8 p174) punya sub-soal dgn
  notasi pecahan/pangkat SANGAT rusak di Markdown (mis. "2<sup>x2+5</sup><sup>x+9=0</sup>"
  utk 2^(x²+5x+9)? atau pecahan koefisien) -- dilewati kalau kuota sudah terpenuhi dari
  sub-soal lain yang bersih (spt Latihan 5.2 no.4-5 yg sederhana `2x²-8x+6=0`, `2x²-18=0`).
- Latihan 5.6, 5.8 (arah bukaan/titik potong sumbu X dari beberapa fungsi a-h) & Eksplorasi
  5.7 (busur panah) SEPENUHNYA berbasis gambar vektor (grafik a-d/a-h), tidak ada file img
  -- semua dilewati (menggambar_atau_mengukur).
- Latihan 5.7 no.2/3 & "Ayo Berpikir Kritis" p172-176 (arah bukaan grafik dari tabel/skenario
  kualitatif) adalah soal PG bagus (2 pilihan atas/bawah + alasan) walau halaman ber-flag [M]
  -- notasi_dari_png=false wajar krn soal ini murni tabel angka, tanpa rumus/pangkat.

## Bab 7
- UPDATE: mode diubah dari "prasyarat" ke "lengkap" karena bab ini juga butuh subbab A "Distribusi
  Peluang" dan B "Aturan Penjumlahan" utk pretest bab itu sendiri. Subbab A: Latihan 7.1 no.1a & 1b
  (p0262, jumlah 2/dadu, kunci Guru p0259). Subbab B: Latihan 7.4 no.1 & no.2 (p0272, aturan
  penjumlahan saling lepas vs tidak saling lepas, kunci Guru p0276). Total 13 soal siap pakai
  (A:2, B:2, C:9), semua status_kunci cocok. Guru Bab 7 di INDEX Guru berlabel BENAR ("Bab 7 -
  Peluang" p253-320, tanpa kuirk penomoran seperti Bab 1/3/4).
- Header fisik: "A. Distribusi Peluang" p0258, "B. Aturan Penjumlahan" p0265, "C. Aturan Perkalian"
  p0273 (di TENGAH halaman, sesudah Latihan 7.4 no.3/4 & Ayo Berpikir Kreatif yang masih subbab B).
  Latihan 7.1 (p0262) & 7.2 (p0263) = subbab A; Latihan 7.3 (p0269, frekuensi relatif/harapan,
  topik agak lepas dari "aturan penjumlahan" tapi posisinya di antara header B jadi tetap
  dikategorikan B kalau dipakai) & 7.4 (p0272) = subbab B; Eksplorasi 7.3 & Latihan 7.5-7.6
  (p0273-0282) = subbab C.
- Kunci Latihan 7.1 (Guru p0259) & Latihan 7.4 (Guru p0276) nilainya HANYA terbaca jelas di PNG
  (markdown mentah gabung digit tanpa pemisah, mis. "3336 = ,0 917" utk 33/36, atau kosong/titik
  RISIKO_MATEMATIKA) -- wajib render PNG, dari_png=true. Nilai dikonfirmasi: Latihan 7.1 1a=3/36,
  1b=33/36; Latihan 7.4 no.1=10/36 (saling lepas, dobel selalu genap jadi tak mungkin =5),
  no.2=6/36 (TIDAK saling lepas, jumlah 2 hanya dari dobel (1,1) jadi P(A∩B)=1/36).
- Mode prasyarat (SEBELUM update di atas), subbab terakhir = C "Aturan Perkalian" (Siswa p0273-p0277: Eksplorasi 7.3, Latihan 7.5). Latihan 7.6 & Uji Kompetensi (p0282) campuran/aturan penjumlahan, bukan perkalian.
- Kunci Latihan 7.5 di Guru p0283-p0285 (Guru bab 7 = "Peluang", nomor bab sama). Pecahan kunci rusak di Markdown; baca PNG Guru p0283 (5/216) dan p0285 (4b: 35/144, 74/144, 95/144). Kunci Guru benar semua.
- Kunci Latihan 7.6 no. 7 (Guru p0288-p0289) hanya argumen kualitatif, tanpa nilai peluang.
- Banyak Eksplorasi/Ayo Mencoba/Berpikir Kritis/Berdiskusi di subbab A & B (p0259, p0263-0264,
  p0268-0269, p0273) berupa isian tabel gambar, contoh yang sudah dijawab di teks, atau diskusi
  opini -- semua dilewati (isian_banyak/soal_terbuka/lainnya). Asesmen Diri (p0281) = checklist
  refleksi, Pengayaan "Percobaan Jarum Buffon" (p0283) = proyek ICT spreadsheet (proyek_atau_aktivitas).

## Bab 6
- Mode lengkap, 3 subbab (A Representasi Data p196-208, B Statistik Deskriptif p209-220,
  C Representasi Data Lanjutan p221-256) x 2 soal = 6 soal, SEMUA status_kunci cocok.
  Header "B." muncul di Siswa p0209, "C." di p0221 (tengah halaman, sesudah materi kuartil
  data tunggal yang masih bagian B). Guru Bab 6 di INDEX Guru berlabel BENAR ("Bab 6 -
  Representasi dan Interpretasi Data" p209-252, tanpa kuirk penomoran seperti Bab 1/3/4).
- Kunci Latihan 6.1 di Guru p0215, 6.2 di p0217, 6.3 (d. Mean Data Kelompok) di p0227,
  6.4 di p0236+p0238-0239, Uji Kompetensi di p0245, Pengayaan Kuartil/Persentil Data
  Kelompok di p0246-0248, 6.5 di p0244, Ukuran Penyebaran (Jangkauan Interkuartil, Varian)
  di p0248-0250, 6.6 di p0247, 6.7 di p0250.
- Perhatian urutan fisik halaman TIDAK selalu sama dengan urutan subbab konsep: materi
  Kuartil/Persentil Data Kelompok & Ukuran Penyebaran (Varian, Simpangan Baku) letaknya di
  halaman 239-253 (setelah header "C." p221 & Uji Kompetensi p237, berlabel "Pengayaan"/
  Latihan 6.6-6.7), tapi ISINYA tetap konsep Statistik Deskriptif (subbab B, bukan C).
  Selalu cek ISI (bukan hanya posisi halaman/header terdekat) saat menentukan subbab.
- Banyak soal butuh baca diagram/box plot dari gambar (bar chart, box-and-whisker):
  gambar tertanam sebagai file PNG terpisah TAPI sering pecah jadi beberapa fragmen kecil
  (mis. p0228: kotak box-plot dan skala sumbu jadi 2 file PNG berbeda) -- WAJIB render
  halaman penuh dg `convert render kelas10 siswa <hal>` utk melihat gabungannya, jangan
  hanya baca 1 file img fragmen.
- Soal "Ayo Mencoba" di p0224 (mengapa 750 kWh pencilan) adalah DUPLIKAT persis dari
  Latihan 6.4 no.2b di p0228 (materi diulang sbg latihan mandiri sebelum versi Latihan
  resmi) -- kalau menemukan pola serupa (soal sama persis muncul dua kali di bab lain),
  cek dulu sebelum membuat 2 entri soal berbeda utk hal yg sama.
- Banyak Eksplorasi/Ayo Mencoba/Ayo Berpikir Kritis bab ini berupa DISKUSI kualitatif
  (korelasi diagram pencar, alasan pencilan, membandingkan grafik) -- Kunci Guru untuk
  ini eksplisit "jawaban bisa bervariasi" atau tidak memberi nilai pasti, jadi SEMUA
  dilewati (soal_terbuka), meski topiknya statistik.
- Skill note: field `dilewati[].alasan` HANYA menerima salah satu dari enum: soal_terbuka,
  pembuktian, menggambar_atau_mengukur, proyek_atau_aktivitas, isian_banyak,
  butuh_alat_peraga, duplikat, teks_tidak_terbaca, lainnya (bukan bebas teks apa saja).
  Kalau alasan sebenarnya "kuota subbab sudah terpenuhi" atau "belum diperiksa", tetap
  pakai `"lainnya"` lalu jelaskan alasan sebenarnya di `keterangan`.
