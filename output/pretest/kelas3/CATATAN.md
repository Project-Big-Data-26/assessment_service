# Catatan ekstraksi kelas3

## Bab 2
- Soal latihan berupa kalimat Matematika isian ("7 + … = 15") ada di dalam gambar [T]
  tapi teks di Markdown sudah lengkap dan berurutan, tidak perlu render PNG.
- Kunci Latihan 1 & 2: Guru p0116-p0118. Kunci ASESMEN: Guru p0119-p0121 (semua "cocok").
- Banyak item "buatlah lima kemungkinan..." (jawaban bervariasi) di Latihan 1 no.5,
  Latihan 2 no.6, ASESMEN no.9-10, dan dua "Ayo Berpikir" (p0094, p0106) -> semua dilewati.
- Aktivitas 1 (p0089-90, kelereng) dan Aktivitas 2 (p0098-99, permen) adalah kegiatan
  kelompok isi tabel manual, bukan soal jawaban tunggal -> dilewati (butuh_alat_peraga).
- Klasifikasi subbab ASESMEN dari BENTUK kalimat matematika (persamaan "+" = subbab A,
  "-" = subbab B), bukan dari letak halaman, karena metode "mengisi nilai belum diketahui
  pada penjumlahan via pengurangan" adalah inti subbab A.

## Bab 3
- Buku Guru bab ini TIDAK punya kunci jawaban untuk Ayo Berlatih biasa (hanya panduan
  mengajar tanpa angka) -- semua Ayo Berlatih diberi status_kunci "tidak_ada_di_guru".
  Satu-satunya kunci eksplisit ada di Guru p0146 "ASESMEN (KUNCI JAWABAN)", teks biasa
  (bukan gambar), memuat kunci untuk SEMUA 5 nomor ASESMEN Siswa p0151-152 (status "cocok"
  semua) -- sumber soal paling efisien di bab ini.
- Banyak "Ayo Berlatih" berupa tabel isian/centang/menghubungkan garis dengan banyak
  pasangan yang hanya terlihat di gambar (p0121, 127, 136-138, 140-142, 150 no.4) ->
  dilewati (isian_banyak). Dua "Aktivitas" kelompok (p0117, p0134, p0148) dan satu
  Aktivitas menimbang di rumah (p0144) -> dilewati (butuh_alat_peraga/proyek).
- Soal berbasis gambar yang BISA diekstrak: p0128 no.3 (tinggi tanaman pot 1/2/3 = 20/15/35
  cm, dari label di gambar) dan no.4 (tiga pensil, semua panjangnya 11 cm meski beda
  posisi/warna -- p0128 gambar 07, p0129 gambar 00 & 02); p0139 no.2 (B-S timbangan
  buah, 100 gram vs 500 gram -> tambahan sebenarnya 400 gram); p0143 no.1 (3 timbangan
  digital: gula 1000 g, tepung 1250 g, telur 250 g). Nomor-nomor ini TIDAK ada kuncinya
  di Guru (angka hanya ada di gambar Siswa), jadi kunci dihitung sendiri.
- Pengamatan 1 (p0145-146, telur di 2 timbangan) dan p0150 no.3 (buah + 2 anak timbangan
  500 gram) sengaja TIDAK diambil: pola "Ayo Mengamati" ini jawabannya langsung dibuka di
  bawahnya (mis. p0146 langsung menulis "1 kilogram = 1.000 gram" setelah pertanyaan
  panduan) sehingga lebih ke penjelasan konsep daripada soal latihan mandiri.
- Item konversi satuan (cm<->m, gram<->kg) di p0131-133 dan p0149 SEMUANYA bisa dikerjakan
  langsung dari teks Markdown (angka sudah tercetak, bukan di gambar) -- sumber murah untuk
  subbab B & D, tidak perlu render PNG sama sekali.

## Bab 4
- Mode prasyarat (subbab C, garis tegak lurus & sejajar) untuk SD5-B6. Latihan subbab C: Siswa p0196-0198 (Ayo Berlatih no. 1-3); kunci di Guru p0191 (no. 1-2) dan p0192 (no. 3, "Jawab: ...").
- Semua soal subbab C bergambar (kertas berpetak / huruf MATEMATIKA). Gambar Siswa p0197: file 0197-01 = gambar a+c, 0197-02 = b, 0197-03 = d.
- Siswa p0199-0202 ("3. Bangun Datar Sederhana") secara buku ada di bawah C, tetapi isinya sisi/sudut bangun datar (konsep A/B).
- Ayo Mengamati p0190-0191 (tegak lurus, kertas lipat) tidak punya kunci di Guru. ASESMEN p0203-0204 semuanya menggambar/aktivitas.
- Soal tersulit: p0198 no. 3c (kunci Guru "tidak ada").
- Bab dilengkapi jadi mode "lengkap" (dipakai juga sebagai bab reguler kelas3, bukan cuma
  prasyarat SD5-B6). Subbab A (Sisi Pada Bangun Datar, p0156-163) dan B (Sudut Pada Bidang
  Datar, p0164-186) ditambahkan setelahnya:
  - Subbab A: p0162 "Ayo Berlatih A" (PG garis/ruas garis/sinar garis/kurva, item 1-4).
    Kunci Guru p0159-160 TIDAK punya penanda teks untuk opsi benar -- jawaban hanya
    dibedakan warna BIRU di PDF (harus lihat PNG Guru), jadi semua item pakai
    `kunci_guru.dari_png: true`. Item 3 (MN=garis) dan 4 (RS=kurva) belum dipakai, bisa
    jadi cadangan.
  - Subbab B: p0182 "Ayo Berlatih" no. 3a-3f (sebutkan nama+ukuran+jenis sudut). Kunci
    LENGKAP (teks biasa, bukan warna) di Guru p0176. Item 3a, 3d, 3e, 3f belum dipakai,
    bisa jadi cadangan (nilainya: a=∠PQR 30° lancip, d=∠BOA 180° lurus, e=∠KLM 260°
    refleks, f=∠EFG 140° tumpul).
  - p0166, p0168, p0180 latihan bab ini semuanya `dilewati` (butuh_alat_peraga/
    soal_terbuka/menggambar_atau_mengukur busur derajat) -- lihat detail alasan di
    bab04.json.

## Bab 5
- ASESMEN (Siswa p0218-221, soal 1-6) kuncinya lengkap di Guru p0212-215 sebagai teks biasa
  (bukan gambar) -- sumber soal paling efisien di bab ini (semua status "cocok").
  "Ayo Berpikir"/"Ayo Berlatih" (Siswa p0216-217, tabel huruf SEKOLAH/STATISTIKA) kuncinya di
  Guru p0210-212 (bukan di halaman rubrik penskoran p0216-222 yang hanya berisi bobot skor
  tanpa nilai). Item 5 & 6 ASESMEN (benda dlm gambar & huruf a/b/c/x/y/z, Siswa p0220-221)
  kuncinya lengkap dengan angka di Guru p0215 -- hitungan manual saya (bola=3, pensil=3,
  a=4, b=9, c=11) persis cocok dengan kunci ini, termasuk konfirmasi kategori benda
  (buku, bolpoin, pensil, rautan pensil, penghapus, bola).
- Tabel turus (huruf SEKOLAH/STATISTIKA/MATEMATIKA) di Markdown Siswa RUSAK: karakter "|"
  turus tabrakan dengan pemisah kolom tabel sehingga baris tabel pecah acak -- WAJIB render
  PNG (p0216 dst) untuk mengetahui sel mana yang sudah terisi vs kosong ("….." = 1 ellipsis
  + 2 titik, bukan 5 titik ASCII). Untuk stimulus tabel semacam ini, JANGAN tulis turus
  sebagai huruf "I"/"II" (huruf I ikut dihitung token oleh validator dan menurunkan skor
  verbatim ~85%<90%) -- pakai karakter pipa "|"/"||" murni (bukan alfanumerik) supaya lolos
  cek verbatim, dan jangan tambah kata pembantu seperti "(dua garis turus)".
- Banyak sub-soal "urutkan ..." dan "huruf/benda apa yang sama banyak" di bab ini
  PUNYA HASIL SERI (>=2 nilai dengan frekuensi sama), jadi tidak adil dijadikan PG dengan
  1 jawaban pasti -> dilewati alasan "lainnya" (jawaban_seri). Cek dulu apakah ada seri
  sebelum membuat opsi PG dari soal "urutkan" atau "sama banyak" di bab statistika SD.
  Satu kunci Guru (ASESMEN 2b, huruf MATEMATIKA) tampak salah/tidak konsisten dengan
  tabelnya sendiri (menyebut "E, I, K, M, dan A" padahal A unik=3) -> dilewati juga.
- Aktivitas 1/2/3 (Siswa p0208-215, kerja kelompok isi data sendiri/lidi/manik-manik) dan
  Tugas Proyek (p0221) semuanya dilewati (butuh_alat_peraga/proyek, data bervariasi).
