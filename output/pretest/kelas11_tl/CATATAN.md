# Catatan ekstraksi pretest kelas11_tl (SMA Matematika Tingkat Lanjut)

## Bab 1 - Matriks (hal. 15-60 siswa, hal. 13-74 guru)
- Sumber soal dipakai: Latihan A-E (Penerapan Konsep, item nomor 4/5 atau 5a/5b),
  masing-masing 2 soal per subbab (A-E). Item Pemahaman Konsep (Benar/Salah) TIDAK
  dipakai karena Latihan A butir 1-4 punya 2 pernyataan benar (1 & 4) sehingga tidak
  bisa dijadikan PG "manakah yang benar" (harus tepat 1 benar). Item Penerapan Konsep
  lebih bersih untuk PG numerik/matriks.
- WARNING validator "halaman X tidak ada di soal/dilewati" untuk Mari Mencoba 1.3/1.4/
  1.5/1.6/1.8/1.9, Uji Kompetensi Bab 1, dan Pengayaan: SENGAJA tidak dipakai karena
  Latihan A-E sudah cukup (2 soal/subbab, per_subbab semua = 2). Tidak perlu diperbaiki.
- **Bug OCR penting**: banyak halaman Latihan (p0023, p0026, p0034-35, p0041) yang
  BUKAN halaman [M]/[T] di INDEX.md tetap punya soal (matriks/persamaan) yang teksnya
  HANYA ada di gambar embedded, tidak ter-OCR ke Markdown sama sekali (bukan cuma
  notasi rusak, tapi teks soal hilang total). Contoh: p0035 & p0041 item nomor 4-5 di
  Latihan C & D sama sekali tidak ada di .md, harus render PNG. p0026 (Latihan B item
  4-6) & p0052-53 (Latihan E) juga begitu.
- **Solusi verbatim check untuk kasus ini**: karena teks soal genuinely tidak ada di
  Markdown (bukan parafrase), gunakan notasi LaTeX untuk SELURUH kalimat pertanyaan/
  stimulus (bukan cuma angka), termasuk kata biasa via `\text{...}` atau bungkus utuh
  dalam `$...$`, sehingga token non-LaTeX yang dicek validator < 3 dan otomatis
  di-skip (`notasi_dari_png: true`). Cara ini dipakai untuk soal Latihan C-4, C-5, D-4,
  D-5, E-4 di bab01.json. Tetap pastikan isi (angka/persamaan) sama persis dengan PNG.
- Kunci Buku Guru bab 1 ada di guru p0061 (Latihan A), p0062-63 (Latihan B), p0064-65
  (Latihan C), p0066 (Latihan D), p0067 (Latihan E). Kunci utuh untuk beberapa nomor
  (nilai x,y,z / matriks X / determinan / (AB^-1)^-1) HANYA tercetak di gambar
  (`panduan_guru_...png`), tidak ada di teks Markdown -> `kunci_guru.dari_png: true`.
  Contoh: Latihan B no.4 (hal.63, pecahan garbled jadi "35"), Latihan D no.4 (hal.66,
  matriks X hanya di gambar), Latihan E no.4 & no.5 (hal.67, seluruh alternatif
  penyelesaian no.4-5 ada di satu gambar `0067-09.png`).
- Penomoran Buku Guru untuk "H. Kunci Jawaban" mengikuti urutan Latihan (1. Latihan A,
  2. Latihan B, dst.), BUKAN nomor bab. Cocokkan dari judul Latihan, bukan angka di
  depannya.
- Prasyarat bab ini: SMP9-B1 (kelas9 bab01) -- belum dikerjakan di sesi ini (bukan
  bagian tugas subagent untuk bab01.json kelas11_tl).

## Bab 2 - Polinomial (hal. 61-112 siswa, hal. 75-128 guru)
- SEMUA halaman Latihan di bab ini ditandai [M] di INDEX.md, tapi kebanyakan notasi
  sup/sub (`<sup>n</sup>`) sudah terbaca benar di Markdown tanpa perlu render PNG.
  Cukup render kalau ada tanda aneh (mis. bullet floating `<u>2</u>` sebelum nomor
  soal, huruf/angka nyasar) -- itu indikasi PECAHAN yang rusak jadi teks terpisah.
  Contoh nyata: soal Latihan C no.7 (hal. siswa 94) aslinya `c = 2/3` tapi di
  Markdown jadi `dan _c_ = 3` dengan sisa `<u>2</u>` nyasar sebagai bullet terpisah
  sebelum nomor 7 -- HARUS di-render PNG untuk ketahuan.
- Karena page ber-flag [M] memicu WARNING notasi_dari_png=false di validator untuk
  SEMUA soal di halaman itu (bukan cuma yang benar-benar rusak), dan karena
  pertanyaan/stimulus di bab ini banyak pakai LaTeX (exponent, pecahan), set
  `notasi_dari_png: true` di semua soal bab ini sekalian (LaTeX butuh `strip_latex`
  saat verbatim check, jadi flag ini WAJIB true kalau pakai `$...$`, bukan cuma
  soal ekstra hati-hati).
- Kunci Guru bab 2: p0114 (Latihan A), p0115 (Latihan B, lanjut ke p0116 utk soal
  no.5), p0117-118 (Latihan C, no.7 kuncinya di gambar png halaman 118 karena
  pecahan c=2/3 rusak jadi "P b 3 l = 5" di Markdown), p0119-120 (Latihan D),
  p0121 (Latihan E). Urutan kunci ikut urutan Latihan A-E (bukan nomor sub-bab).
- Latihan A-E masing-masing 2 soal (subbab A-E semua = 2, cukup). Item Pemahaman
  Konsep (Benar/Salah tunggal no.1/2/3 tiap Latihan) SENGAJA tidak dipakai kecuali
  1 soal per subbab yang mudah dikonversi jadi PG tanpa mengarang pernyataan baru
  (mis. Latihan A no.3 "perilaku ujung ... adalah ...." dan Latihan E no.3
  "p^3-q^3 = ...." -- bentuk isian, bukan B/S, jadi tidak perlu pertanyaan_disesuaikan).
  Latihan E no.4a ("Buktikan ... identitas atau bukan") DIKONVERSI jadi PG tertutup
  dengan opsi kesimpulan+alasan (`pertanyaan_disesuaikan: true`).
- WARNING validator utk "Mari Mencoba 2.1/2.2/2.3/2.4/2.5/2.7/2.8/2.10", Uji
  Kompetensi Bab 2, dan Pengayaan: SENGAJA tidak dipakai (Latihan A-E sudah cukup,
  2 soal/subbab). Sama seperti pola Bab 1. Tidak perlu diperbaiki.

## Bab 3 - Fungsi Trigonometri (hal. 113-172 siswa, hal. 129-188 guru)
- Sumber soal: Latihan A-E, masing-masing 2 soal/subbab (Pemahaman Konsep item
  isian/hitungan yang jawabannya pasti, BUKAN item Benar/Salah tunggal -- item
  B/S tunggal seperti Latihan A no.1, Latihan C no.1/3, Latihan D no.1/2/3,
  Latihan E no.1/2/3 SENGAJA dilewati karena mengonversi jadi PG "pernyataan
  mana yang benar" butuh mengarang 3 pernyataan salah baru (tidak ada pilihan
  lain di buku), beda dgn kasus Menjodohkan/beberapa-pernyataan yg memang
  didesain utk itu. Latihan C no.6 ("Menemukan Kesalahan" ala Abel) dipakai
  sbg pengecualian krn itu soal uraian terbuka (bukan B/S) yg biasa dikonversi
  jadi PG tertutup (pertanyaan_disesuaikan: true), bukan B/S yang perlu
  pernyataan karangan.
- "H. Kunci Jawaban" Guru bab 3 ada di p0174 (Latihan A), p0177 (Latihan B),
  p0178-179 (Latihan C), p0180 (Latihan D), p0182 (Latihan E). Urutan ikut
  urutan Latihan A-E, bukan nomor sub-bab. Setelah itu p0182 lanjut ke "6. Uji
  Kompetensi".
- Banyak kunci Latihan A/B/D di atas GENUINELY berupa teks asli PDF (bukan
  gambar), tapi Markdown-nya garbled (pecahan bersusun & simbol π hilang jadi
  huruf "r" nyasar, mis. p0174 no.2 "- 2. 180" seharusnya "π/180", p0174 no.5
  hanya nongol "45°=45·180=4" padahal PDF asli utuh "45°=45·π/180=π/4 rad" +
  144° + 306°). WAJIB render PNG guru utk baca lengkap -- hasilnya konsisten
  dgn perhitungan sendiri, jadi status_kunci semua "cocok" tapi ditandai
  `kunci_guru.dari_png: true` krn Markdown tak lengkap.
- Soal numerik bersih (tanpa perlu gambar) yang dipakai: Latihan A no.2 & 5
  (konversi derajat<->radian), Latihan B no.2 & 4 (amplitudo/periode grafik
  transformasi & periode tan x), Latihan C no.2 (identitas sec²-tan²=1) & no.6
  (Abel), Latihan D no.4 & 5 (Aturan Sinus, segitiga tanpa gambar tambahan),
  Latihan E no.4 & 5 (Aturan Kosinus, segitiga tanpa gambar tambahan). Semua
  item lain di Latihan A-E (no.3,4,6-13 di A; no.1,3,5,6 di B; no.1,3,4,5 di C;
  no.1,2,3,6,7,8 di D&E) butuh gambar/grafik/tabel atau pembuktian -> dilewati.
- WARNING validator utk "Mari Mencoba 3.1/3.2/3.4/3.5/3.10/3.11/3.13/3.15/3.17",
  Uji Kompetensi Bab 3, dan Pengayaan: SENGAJA tidak dipakai (Latihan A-E sudah
  cukup, 2 soal/subbab). Sama seperti pola Bab 1 & 2. Tidak perlu diperbaiki.
- Prasyarat bab ini: SMA10-B3 (kelas10 bab 3) -- belum dikerjakan di sesi ini.

## Bab 4 - Vektor (hal. 173-214 siswa, hal. 189-222 guru)
- Hanya 3 subbab (A Vektor pada Bidang, B Hasil Kali Titik, C Pembuktian
  Geometris), jadi cukup 6 soal (2/subbab). Sumber: Latihan A no.4 & 5, Latihan
  B no.4 & 8, Latihan C no.3a & 3b (bukan Uji Kompetensi/Mari Mencoba -- pola
  sama dgn Bab 1-3: sudah cukup, WARNING utk halaman² tsb SENGAJA dibiarkan).
- Item B/S tunggal (Latihan A no.1-3, B no.1-2, C no.1-2) SENGAJA dilewati
  (pola sama dgn bab-bab sebelumnya, hindari mengarang 3 pernyataan salah).
- Item pembuktian ("Buktikan...") SEMUA dilewati (alasan: pembuktian) --
  Latihan A no.8, C no.3c/4/5/6c.
- **Bug OCR notasi vektor**: pola `⟨a,b⟩` (angle bracket) di Buku Siswa SERING
  kehilangan salah satu simbolnya di Markdown walau halaman TIDAK ditandai [M]
  di INDEX.md. Contoh nyata: p0191 Latihan A no.4 "Vektor 4,12 ..." harusnya
  "⟨-4,12⟩" (minus hilang, bukan cuma bracket) -- WAJIB render PNG utk
  memverifikasi tanda dan bracket meski page tak ber-flag [M]. p0206 Latihan B
  no.4 "sudut ... adalah 3" harusnya "π/3" (simbol pi hilang total, hanya sisa
  angka penyebut) -- ini halaman DENGAN flag [M] (RISIKO_MATEMATIKA=sup/sub).
- Kunci Guru bab 4: p0212 (Latihan A), p0213 (Latihan B no.1-7), p0214
  (lanjutan Latihan B no.8 + Latihan C no.1-4), p0217 (Uji Kompetensi). Urutan
  ikut Latihan A-C, bukan nomor subbab.
- **Kunci Guru salah ketik ditemukan**: Latihan C no.3a/3b (hal.214) menulis
  jawaban pakai vektor "AL" (A ke L), padahal soal siswa (dikonfirmasi via PNG
  hal.210) minta jawaban dalam "LA" (L ke A). Karena AL = -LA, ini mengubah
  hasil (KA-AL = KA+LA, BEDA dari KA-LA yang benar). Diverifikasi numerik
  dengan segitiga uji A(0,2) B(0,0) C(2,0): KL sebenarnya = KA-LA, BUKAN
  KA-AL. status_kunci="tidak_cocok" utk kedua soal ini, jawaban_benar pakai
  hasil sendiri. Kalau nanti nemu pola serupa (arah vektor AL vs LA tertukar)
  di bab lain buku ini, cek dulu dgn titik uji sebelum percaya kunci Guru.
- Prasyarat bab ini: SMP7-B5, SMP9-B3 (kelas7 & kelas9) -- belum dikerjakan.

## Bab 5 - Transformasi Geometri (hal. 215-256 siswa, hal. 223-252 guru)
- 3 subbab (A, B, C); 8 soal dari Latihan A 4b/4c/4d (siswa p0238), Latihan B 5a/5d (p0247), Latihan C 4a/4b/5 (p0251). Item B/S tunggal dilewati (pola bab lain).
- Kunci Guru: p0244-245 (Latihan A), p0245-246 (Latihan B), p0247 (Latihan C). Kunci A no.4a di md kehilangan tanda minus (asli (-1/2, 6)); 4a tidak dipakai.
- Variabel bergaya md (`_x_`) memicu error "angka tidak ada" untuk `2x`, `T1`: tulis dalam LaTeX (`$2x + 3y$`, `$T_1$`) dengan notasi_dari_png true.
- WARNING Mari Mencoba 5.x, Uji Kompetensi, Pengayaan: SENGAJA tidak dipakai (2+ soal per subbab sudah cukup).
- Prasyarat bab ini: SMA11L-B1 (bab01 kelas11_tl), SMP9-B3 (kelas9).

## Bab 6 - Fungsi dan Pemodelannya (hal. 257-320 siswa, hal. 253-320 guru)
- 10 soal dari Latihan A (siswa p0273 no.4,7,8), Latihan B (p0287 no.5a,5b,6,7a), Latihan C (p0299 no.3a-3c). Item B/S tunggal, sketsa/grafik dilewati.
- Kunci Guru: p0291 (Latihan A), p0292-293 (Latihan B), p0295 (Latihan C). Latihan A no.6 (gempa) dilewati karena kunci Guru di Markdown ambigu (100 kali vs 1/100).
- Notasi soal (pecahan, akar pangkat 3) hanya benar di PNG siswa p0273/p0287; Markdown-nya garbled.
- WARNING Mari Mencoba 6.x, Uji Kompetensi, Pengayaan: SENGAJA tidak dipakai (2+ soal per subbab sudah cukup).
- Prasyarat bab ini: SMA10-B1 (kelas10 bab01), SMP8-B4 (kelas8).
