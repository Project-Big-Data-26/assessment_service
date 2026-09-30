# Catatan ekstraksi pretest kelas11

## Umum
- Halaman PDF siswa/guru offset dari halaman cetak buku. Bab 1 "hal. 5-62" (INDEX)
  sebenarnya berisi Daftar Isi/Petunjuk Penggunaan Buku (angka romawi) di PDF hal.5-16;
  isi Bab 1 yang sebenarnya baru mulai di PDF p0017 ("Bab 1" tercetak "1").
  Jangan kaget kalau WARNING validator menyebut hal.12/14/15 "terlewat" -- itu bagian
  Petunjuk Penggunaan Buku, bukan latihan sungguhan, boleh diabaikan.
- Buku Guru bab 1 ada di PDF hal.27-76 (judul Guru: "Bab 1 | Komposisi Fungsi dan Invers",
  sedikit beda dari judul Siswa "... dan Fungsi Invers" -- cocokkan dari isi, bukan judul persis).

## Kunci di Buku Guru bab 1 (kelas11)
- Kunci Jawaban Latihan 1.1 -> guru p0034.
- Kunci Jawaban Latihan 1.3 -> guru p0049 (item 1-2) lanjut p0050 (item 4-8).
- Jawaban Latihan 1.4 -> guru p0058 (item 2d-4) lanjut p0059 (item 5-9).
- Jawaban Latihan 1.5 -> guru p0069 (item 1a) lanjut p0070-73 (item 1b-5).
- Rumus pecahan/invers di Buku Guru sering rusak akibat ekstraksi PDF (contoh: "(x-2)/2"
  tercetak jadi "x 2 2" tanpa tanda kurang & garis bagi). Kalau nilai konstanta di sekitarnya
  (misal b=2) tetap terbaca jelas dan cocok dengan pengerjaan sendiri, tetap pakai status_kunci
  "cocok" dan jelaskan di catatan -- jangan otomatis dianggap "tidak_ada_di_guru".

## Soal yang TIDAK bisa dipakai (contoh nyata)
- Latihan 1.4 no.3 (p47 siswa): "tentukan a dan b sehingga (f∘g)(x)=(g∘f)(x)" -- kunci Guru
  (p58) bilang "Ada banyak kemungkinan nilai a dan b yang memenuhi, contoh a=-1, b=2" ->
  jawaban tidak tunggal, masuk dilewati (soal_terbuka). Kalau nanti mengerjakan bab lain
  dengan pola serupa (dua fungsi linear disamakan komposisinya tanpa syarat tambahan),
  cek dulu ke Guru sebelum jadi PG.

## Status bab01 (Bab 1 - Komposisi Fungsi dan Fungsi Invers)
- 6 soal siap pakai: subbab A=2, B=2, C=2. Validator LOLOS (0 error).
- WARNING tersisa: beberapa halaman latihan/eksplorasi lain di rentang bab (hal.12,14,15
  [Petunjuk Buku, bukan soal], 30, 37, 49, 62 [Ayo Berpikir Kritis/Mencoba]) belum disentuh
  karena tugas hanya minta 2 soal/subbab -- sengaja tidak ditambah lagi supaya tidak
  membengkak, aman diabaikan untuk sesi pretest.

## Kunci di Buku Guru bab 2 (kelas11 - Lingkaran)
- Judul Guru sama dengan Siswa: "Bab 2 | Lingkaran". Buku Guru bab 2 di PDF hal.77-136.
- Jawaban Latihan 2.1 -> guru p0096 (item 1) lanjut p0097 (item 2-3) lanjut p0098 (item 4-5).
  Item 4 (sudut ACB, panjang AB/BC) jawabannya HANYA tercetak di gambar/PNG guru p0098
  (rumus Pythagoras + hasil "BC = 15cm"), tidak ada di teks Markdown -> dari_png=true.
- Jawaban Latihan 2.2 -> guru p0107 (item 1, PB=24cm ada di teks biasa) lanjut p0108
  (item 2, ∠BDC=33° -- hasil akhir "= 33°" hanya di gambar/PNG -> dari_png=true).
- Jawaban Latihan 2.3 -> guru p0122 (item 1: diameter 10cm; item 2a-b: ∠BAE=60°, ∠BDE=30°,
  semua di teks Markdown biasa, tidak perlu PNG).
- Pola umum bab ini: nomor soal & jawabannya sering campur teks-Markdown dan gambar/PNG
  pada halaman Guru yang sama -- selalu cek gambar sebelum menyimpulkan "tidak_ada_di_guru".

## Soal yang TIDAK bisa dipakai (bab 2)
- Latihan 2.1 no.1 (p73) dan Latihan 2.3 "3. Apotema" (p89): soal pembuktian ("Buktikan
  bahwa ..."), tidak bisa dijadikan PG yang adil -> dilewati.
- Banyak soal bab ini (Latihan 2.1 no.2-6, Latihan 2.2 no.1-2, Latihan 2.3 no.2,4) butuh
  gambar lingkaran (butuh_gambar=true) untuk memastikan konfigurasi titik (pusat, jari-jari,
  garis singgung, dsb) -- WAJIB lihat PNG siswa sebelum menulis soal, teks saja sering
  ambigu (misal "∠BOC=90°, berapa ∠BEC?" perlu tahu E ada di busur besar dari gambar).

## Status bab02 (Bab 2 - Lingkaran)
- 6 soal siap pakai: subbab A=2 (sudut pusat & sudut keliling / Thales), B=2 (garis
  singgung), C=2 (tali busur). Validator LOLOS (0 error, 10 warning).
- WARNING tersisa: 4x "[M] tapi notasi_dari_png=false" untuk soal di hal.74 & 81 -- sudah
  dicek PNG, notasi angka (90°, 25cm, 7cm, 147°) tidak rusak di Markdown, aman diabaikan.
  Sisanya halaman latihan/eksplorasi lain (hal.63,75,84,91,92,94) belum disentuh karena
  tugas hanya minta 2 soal/subbab -- sengaja tidak ditambah, aman diabaikan.

## Kunci di Buku Guru bab 3 (kelas11 - Statistika)
- Judul Guru sama dengan Siswa: "Bab 3 | Statistika". Buku Guru bab 3 ada di PDF hal.137-200
  (INDEX Guru bilang "137-200" tapi konten sebenarnya berhenti sekitar hal.180-an).
- Subbab (dari kurikulum Excel): A = Diagram Pencar/Scatter (Siswa hal.97-107, "A. Diagram
  Pencar..." heading di p0100), B = Regresi Linear (heading "B. Regresi Linear" di p0111,
  berisi juga "2. Metode Kuadrat Terkecil" dan "3. Koefisien Determinasi" -- HATI-HATI:
  "Koefisien Determinasi" posisinya secara PAGE ada SEBELUM heading "C. Analisis Korelasi"
  muncul lagi di p0134 sebagai sub-bagian nomor urut lanjutan yang SEBENARNYA masuk C,
  karena "C. Analisis Korelasi" sendiri sudah dimulai duluan di p0125 (sebelum p0134);
  urutan definitif: A hal.97-110, B hal.111-124, C hal.125-146 (Latihan 3.5, 3.6, koefisien
  korelasi & determinasi semua masuk C).
- Kunci Jawaban Latihan 3.1 -> guru p0149 (item 1a-c korelasi kualitatif, tanpa hitungan).
- Kunci Jawaban Latihan 3.2 -> guru p0150 (butuh gambar, dilewati).
- Kunci Jawaban Latihan 3.3 -> guru p0161 (tabel residu kuadrat lengkap untuk 2 persamaan).
- Kunci Jawaban Latihan 3.4 -> guru p0163-0164 (item 1 a-f, item 2 a-g), semua tabel
  numerik ada di teks Markdown biasa (tidak perlu PNG untuk data numerik jarak reaksi/tinggi).
- Kunci Jawaban Eksplorasi 3.6 -> guru p0171 (item 1-6).
- Kunci Jawaban Latihan 3.6 -> guru p0175 (item 1-2).
- Pola bab ini: BANYAK soal latihan (3.2, 3.5, sebagian 3.3/3.4/3.6) wajib gambar diagram
  pencar/tabel yang HANYA ada sebagai gambar vektor (tidak ada representasi teks/tabel di
  Markdown) -- cek dulu apakah data tabelnya ada di teks sebelum memutuskan butuh_gambar.
  Latihan yang datanya berupa tabel teks (bisa dipakai tanpa gambar): Latihan 3.1 #1 (a,b,c
  kualitatif), Latihan 3.3 #1 (tabel pesawat), Latihan 3.4 #1 (tabel kecepatan/jarak reaksi),
  Eksplorasi 3.6 #2/#4/#5 (nilai r & persamaan garis sudah diberikan sebagai teks, tidak
  perlu diagram).
- BUG kunci Guru ditemukan: Eksplorasi 3.6 no.5 (p171) menulis "100% - 1,9% = 99,1%" --
  ini salah hitung (seharusnya 98,1%). Dipakai jawaban_benar=98,1% (status_kunci=tidak_cocok).
  Kalau nanti menemukan pola pengurangan "100% - r%" lain di bab ini, cek ulang sendiri,
  jangan percaya langsung ke Guru.
- Tabel di stimulus (mis. Latihan 3.3, tabel pesawat) harus disalin sebagai markdown table
  verbatim (`|kolom|...|`), BUKAN diparafrase ke kalimat prosa (mis. menambah "Rp" di
  depan angka yang di buku tidak ada) -- validator menolak angka yang tidak identik
  (contoh gagal: "Rp1.100.000,00" ditolak karena sumber cuma "1.100.000,00" tanpa "Rp").
- Untuk pertanyaan gabungan kalimat induk + item huruf (mis. Latihan 3.1 "Tentukan
  bagaimana hubungan mereka..." + "a. Banyak kendaraan bermotor...") yang diubah jadi
  satu kalimat tanya ("Bagaimana hubungan antara X dan Y?"), WAJIB set
  pertanyaan_disesuaikan=true karena kata tambahan "Bagaimana hubungan antara" menurunkan
  skor verbatim di bawah 90%; ambang untuk pertanyaan_disesuaikan cuma 50% jadi aman.

## Status bab03 (Bab 3 - Statistika)
- 6 soal siap pakai: subbab A=2 (Latihan 3.1 #1a/#1b, korelasi kualitatif), B=2 (Latihan
  3.3 #1 bandingkan 2 garis regresi via jumlah kuadrat residu; Latihan 3.4 #1e hitung
  regresi penuh lalu prediksi), C=2 (Eksplorasi 3.6 #4/#5 koefisien determinasi & sisanya).
  Validator LOLOS (0 error, 8 warning).
- status_kunci: 5 cocok, 1 tidak_cocok (Eksplorasi 3.6 #5, kunci Guru salah hitung
  100%-1,9%=99,1% seharusnya 98,1%).
- 7 kelompok soal masuk `dilewati` (mayoritas alasan="lainnya"/butuh_gambar: Latihan 3.1
  #2, Latihan 3.2 semua, Latihan 3.3 #2c-d, Latihan 3.5 semua, Latihan 3.6 #2; alasan
  soal_terbuka: Latihan 3.3 dan Eksplorasi 3.6 #1/#3 jawaban pendapat/deskriptif).
- WARNING tersisa: 1x "[M] tapi notasi_dari_png=false" di hal.117 (Latihan 3.3 ada di
  bagian atas halaman tanpa rumus; tanda [M] dipicu tabel lain di bawahnya yang memang
  ada notasi rusak -- aman diabaikan). Sisanya 6x "halaman X tidak ada di soal/dilewati"
  (hal.104,112,113,124,138 Ayo Berpikir Kritis/Kreatif, hal.141 Uji Kompetensi, hal.146
  Pengayaan) -- sengaja tidak disentuh karena tugas hanya minta 2 soal/subbab, aman
  diabaikan untuk sesi pretest.
