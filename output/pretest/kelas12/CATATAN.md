# Catatan ekstraksi pretest kelas12 (SMA)

## Kunci Buku Guru kelas12 Bab 3 (Kaidah Pencacahan)
- Kunci Latihan 3.1-3.4 & Uji Kompetensi Bab 3 ada di guru hal. 214-229 (dicocokkan dari
  judul "H. KUNCI JAWABAN" / "Kunci Jawaban Uji Kompetensi Bab 3"), bukan sesuai nomor
  halaman siswa (99-140).
- Latihan 3.2 no.6 (susunan huruf "LABUAN BAJO") -- kunci Guru (hal.222) SALAH menghitung
  jumlah huruf sebagai 11 (harusnya 10, kata tanpa spasi = L,A,B,U,A,N,B,A,J,O), sehingga
  hasilnya 3.326.400 padahal yang benar 10!/(3!2!)=302.400. Jangan dipakai sebagai kunci;
  pakai hasil hitung mandiri (`status_kunci: tidak_cocok`).
- Latihan 3.4 no.2 (peluang tepat 8 dari 12 siswa evakuasi benar, p=0,7) -- kunci Guru
  (hal.225) tercetak SALAH, mengulang jawaban soal no.1 (0,432 untuk kasus n=3,p=0,6) alih-alih
  menghitung ulang untuk n=12,r=8,p=0,7. Jawaban benar hasil hitung mandiri: C(12,8) x
  0,7^8 x 0,3^4 = 0,2311.
- Beberapa tabel Benar/Salah di Latihan 3.2 no.3 (novel) dan Latihan 3.3 no.1 & no.3 hasilnya
  2 benar+2 salah (atau 2 benar+1 salah), TIDAK bisa dikonversi jadi PG 1-jawaban-benar+3-
  distraktor tanpa mengarang pernyataan baru -- dilewati. Yang BISA dikonversi hanya tabel
  Latihan 3.1 no.2 (4 benar + 1 salah, kunci lengkap di guru hal.216).
- Uji Kompetensi Bab 3 no.1-6 sudah berupa PG A-E asli buku (opsi di siswa hal.137-138,
  kunci huruf di guru hal.226-228); no.7-9 esai tanpa opsi (kunci di guru hal.228-229,
  no.7 kuncinya tidak konsisten sebut jumlah orang, dilewati); no.10 menjodohkan dengan
  teks gambar rusak urutannya (guru hal.229 hanya beri kunci pasangan huruf, dilewati).
- Distraktor TIDAK divalidasi verbatim terhadap halaman manapun oleh validate.py (hanya
  pertanyaan/stimulus/kunci_guru.kutipan yang dicek) -- aman mengarang distraktor untuk
  soal esai Uji Kompetensi (no.8,9) yang tidak punya opsi tercetak di buku.

## Buku Siswa: halaman depan (roman) menduplikasi konten bab
- PDF hal. 11-18 (footer "xi".."xviii") adalah "Petunjuk Penggunaan Buku" (front matter),
  BUKAN latihan sungguhan meski INDEX.md/index.json menandainya `latihan` (mis. "16. Latihan",
  "18. Uji Kompetensi"). Isinya cuplikan/contoh dari bab yang sama (kadang dari bab lain,
  mis. hal.14 mengutip Bab 2 hal.56) untuk menjelaskan fitur buku (Ayo Mencoba, Latihan, Uji
  Kompetensi, dst). Jangan diambil sebagai soal baru -- cek dulu apakah kontennya sudah ada
  di halaman "asli"-nya (biasanya nomor halaman lebih besar, di badan bab). Selalu tambahkan
  `dilewati` (alasan `duplikat`) untuk tiap halaman xi-xvii yang bertanda `latihan` di index,
  supaya WARNING cakupan halaman tidak muncul.
- Bab 1 (Barisan dan Deret) baru benar-benar mulai di PDF hal. 19 (bukan hal.11 walau
  INDEX.md bilang "hal. 11-52"); hal.11-18 adalah front matter di atas.

## Kunci Buku Guru kelas12 Bab 1
- Kunci Latihan 1.1-1.4 & Uji Kompetensi Bab 1 ada di guru hal. 99-115 (bukan sesuai nomor
  halaman siswa; cocokkan dari judul "H. Kunci Jawaban" / "Kunci Jawaban Uji Kompetensi").
- Banyak kesimpulan akhir (angka final) HANYA tercetak sebagai gambar rumus (bukan teks
  Markdown), walau halaman guru tidak selalu ditandai [M]. Kalau teks markdown terhenti
  tepat sebelum "Jadi, ..." dan lanjut ke gambar/heading berikutnya, WAJIB render PNG guru
  untuk memastikan angka akhir (contoh: hal.100 soal 3 barisan aritmetika a/b/Un, hal.103
  soal 3 barisan geometri, hal.108 soal 1 Latihan 1.4, hal.110 soal 5 deret A vs B).
- Soal Uji Kompetensi Bab 1 nomor 9 (inflasi emas) memakai rumus PERTUMBUHAN BERGANDA
  (compound, Ht = P(1+r)^t = 2.000.000(1.08)^4 = 2.720.980), BUKAN bunga tunggal aditif
  (yang akan memberi 2.640.000). Meski letaknya dekat materi bunga tunggal, konsepnya
  barisan/deret geometri -- jangan tertukar.

## Verbatim/token: notasi _X_ N (mis. `_U_ 100`, `_S_ 10`) tokenisasi terpisah
- Markdown menulis subskrip sebagai italic+spasi, mis. `_U_ 100` -> token terpisah "u" dan
  "100" (BUKAN "u100"). Kalau menulis ulang di `pertanyaan`/kutipan tanpa spasi (mis. "U100",
  "S10", "3n"), validator akan menandai ERROR "angka ... tidak ada di halaman" walau
  angkanya benar -- gunakan spasi seperti sumber asli ("U 100", "S 10", "3 n").

## Subbab Bab 1 (dari Prasyarat_Math.xlsx)
A = Barisan (aritmetika & geometri, termasuk Latihan 1.1 & 1.2), B = Deret (aritmetika,
geometri, geometri tak hingga, termasuk Latihan 1.3 & 1.4), C = Bunga Tunggal (tidak ada
Latihan bernomor di Buku Siswa untuk C; sumber soal dipakai dari Uji Kompetensi Bab 1
no.6 & no.9, ditambah 2 soal dari tabel isian "Ayo, Bereksplorasi" hal.49 (Tabel 1.5,
tokoh Angga) -- tidak ada kunci numerik di Buku Guru untuk tabel ini (guru hal.94 hanya
panduan mengajar), jadi `status_kunci: tidak_ada_di_guru` dengan jawaban dihitung sendiri
memakai rumus B=M×p%×n yang sama seperti baris tahun pertama tabel.

## Kunci Buku Guru kelas12 Bab 2 (Investasi dan Pinjaman)
- Kunci Latihan 2.1/2.2/2.3 & Uji Kompetensi Bab 2 ada di guru hal. 158-176 (dicocokkan
  dari judul "H. Kunci Jawaban" / "Kunci Jawaban Uji Kompetensi Bab 2", bukan sesuai nomor
  halaman siswa).
- Latihan 2.1 no.4 (Maya menyetor rutin tiap tahun ke deposito) -- soal jelas berkonsep
  ANUITAS (setoran rutin), tapi kunci Guru (hal.160-161) menghitungnya sebagai bunga
  majemuk lump-sum tunggal PV x (1+i)^n, TIDAK sesuai konsep soal. Jangan dipakai.
- Latihan 2.2 no.5 (selisih total KPR promo X tenor 12 vs 15 tahun) -- hasil hitung mandiri
  dengan rumus anuitas standar berbeda cukup jauh dari kunci Guru (hal.165-167:
  Rp174.580,00); kemungkinan kunci Guru memakai pembulatan bertingkat. Jangan dipakai
  tanpa verifikasi tambahan.
- Latihan 2.2 no.2 (menjodohkan % tahunan ke % per bulan/semester/triwulan) -- tabel
  pasangan rusak total saat ekstraksi Markdown (kolom B tidak sejajar kolom A), kunci Guru
  (hal.163) juga tidak jelas pasangannya tanpa PNG asli. Skip.
- Uji Kompetensi Bab 2 no.3 (opsi metode "(1,0612) x M") -- di PNG Buku Siswa hal.95, opsi
  ini TIDAK punya pangkat yang jelas tercetak (beda dgn opsi d "(1,0404) 3x M" dan e
  "(1,02) 6x M" yang pangkatnya kelihatan sbg superscript kecil), kemungkinan salah cetak
  asli buku. Jangan dipakai sbg distraktor kalau butuh opsi ini.
- Banyak kunci Uji Kompetensi memakai frasa "Jadi, jawabannya adalah (X) ..."; huruf opsi
  di teks kunci Guru kadang meleset (OCR), tapi NILAINYA selalu cocok salah satu opsi
  Siswa -- cocokkan by value, bukan by huruf.
- Subbab Bab 2: A=Suku Bunga Tunggal (hal.55-57, tanpa Latihan bernomor -- pakai Masalah
  A/B di "Ayo Bereksplorasi"), B=Investasi Bunga Majemuk (hal.58-63, Latihan 2.1
  no.1,2,3,5,6 & Uji Komp no.1-3), C=Investasi Anuitas (hal.63-72, minim soal bernomor --
  pakai "Ayo Berpikir Kreatif" hal.68 (Aliyya, PV anuitas) + Uji Komp no.6-7 Dani),
  D=Pinjaman Bunga Majemuk (hal.73-76, Latihan 2.2 no.1a/b/c pokok tetap),
  E=Pinjaman dengan Anuitas (hal.77-89, Latihan 2.2 no.3 & Uji Komp no.4,5,8,9,10),
  F=Parameter Investasi dan Pinjaman (hal.89-93, tapi soal numerik utamanya justru di
  Latihan 2.3 no.1,3,4,5 -- "Ayo Berpikir Kritis Parameter..." hal.90-92 isinya
  opini/kesimpulan dan grafik teks rusak, tidak dipakai).

## Kunci Buku Guru kelas12 Bab 4 (Peluang)
- Kunci Latihan 4.1-4.3 & Uji Kompetensi Bab 4 ada di guru hal. 269-285 (judul "H. Kunci Jawaban").
  Banyak jawaban akhir (pecahan) hanya berupa gambar (guru hal. 275-279, 281): render PNG guru.
- Subbab Bab 4: A = Peluang Suatu Kejadian (hanya Latihan 4.1 no.1,2,3 yang layak; no.5,6,7 dilewati
  karena kunci Guru tidak sesuai/ambigu), B = Peluang Kejadian Majemuk (Latihan 4.2, 4.3, Uji Kompetensi).
- Uji Kompetensi no.3 (tidak pernah dadu): kunci Guru 1/64 SALAH, benar 1/8 (GGG). status tidak_cocok.
- Latihan 4.1 no.5: kunci Guru memakai dadu 2,2,3,4,5,7 (bukan 1,2,4,5,6,7 seperti soal) -> dilewati.
- Latihan 4.1 no.2: nilai '50%' pada stimulus rusak di Markdown ('���'); ditulis 0,5 agar lolos validator.
- Halaman 165-189 banyak kunci dengan '�' pada Markdown; kutipan boleh menyalin karakter � apa adanya.
- Saat menyunting JSON via Python: jangan menulis "\frac" tanpa escape ganda (menjadi form-feed).
