# Lembar koreksi — kelas10 SMA10-B6 subbab C: Representasi Data Lanjutan

44 soal | easy 20, medium 14, hard 10 | variasi 18, orisinal 26
> **Kapasitas kurang (medium): 14 dari kuota 20** — Acuan siswa teks di subbab C (box plot dan diagram pencar) sudah dipakai di easy dan sebagian besar soal Latihan 6.4/6.5 bergambar atau jawabannya subjektif; soal medium yang tidak kembar dengan easy (data mentah, pencilan, perbandingan kelompok, tafsir diagram pencar) hanya cukup sekitar 14, sisanya hanya akan berupa soal nyaris kembar sehingga tidak dipaksa.
> **Kapasitas kurang (hard): 10 dari kuota 20** — Acuan teks subbab C habis dan jenis penalaran hard yang layak (evaluasi klaim korelasi, pencilan, kuartil, rancang data, temukan kesalahan) terbatas; soal hitung biasa dibuang dan soal kembar tidak dibuat demi kuota.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b06-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: batas pencilan dari Q1 dan Q3*

Sebuah kecamatan mencatat banyak sampah mingguan (dalam kg) dari 10 RT. Dari data terurut diperoleh Q1 = 44 kg dan Q3 = 47 kg, sedangkan satu RT mencatat 95 kg. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Batas atas yang dipakai untuk menentukan pencilan pada data sampah itu adalah ....

- A. 48,5 kg  
  <sub>Salah: menambahkan 1,5 ke Q3 tanpa dikalikan IQR</sub>
- **B. 51,5 kg** ✅  
  <sub>Benar: IQR = 47 - 44 = 3; batas atas = 47 + 1,5 x 3 = 51,5 kg, sehingga 95 kg di atas batas itu.</sub>
- C. 50 kg  
  <sub>Salah: memakai Q3 + IQR tanpa faktor 1,5</sub>
- D. 39,5 kg  
  <sub>Salah: menghitung batas bawah (Q1 - 1,5 x IQR), bukan batas atas</sub>

**Pembahasan:** IQR = Q3 - Q1 = 3. Batas atas = Q3 + 1,5 x IQR = 47 + 4,5 = 51,5 kg.
**Acuan:** pretest — kelas10-b06-p0228-latihan-6-4-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b06-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: identifikasi data pencilan*

Waktu tunggu (dalam menit) delapan pelanggan di sebuah loket: 14, 12, 15, 13, 16, 14, 2, 15. Dari data ini diperoleh Q1 = 12,5 dan Q3 = 15. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Data yang tergolong pencilan adalah ....

- **A. 2 menit** ✅  
  <sub>Benar: IQR = 2,5; batas bawah = 12,5 - 3,75 = 8,75 dan batas atas = 15 + 3,75 = 18,75; hanya 2 yang di luar batas.</sub>
- B. 12 menit  
  <sub>Salah: membandingkan dengan Q1 tanpa memakai batas bawah 8,75</sub>
- C. 15 menit  
  <sub>Salah: menganggap Q3 sendiri sebagai pencilan</sub>
- D. 16 menit  
  <sub>Salah: mengira nilai terbesar pasti pencilan, padahal 16 < 18,75</sub>

**Pembahasan:** IQR = 15 - 12,5 = 2,5; 1,5 x IQR = 3,75. Batas: 8,75 sampai 18,75. Hanya 2 di luar batas.
**Acuan:** siswa — siswa hal.224 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b06-c-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: tafsir persentase data pada diagram kotak garis*

Banyak pengunjung harian sebuah perpustakaan selama 40 hari diringkas sebagai berikut: nilai minimum 12, Q1 = 20, Q2 = 26, Q3 = 33, dan nilai maksimum 41.

Persentase hari yang banyak pengunjungnya terletak antara 20 dan 41 adalah ....

- **A. 75%** ✅  
  <sub>Benar: Antara Q1 dan Q2, Q2 dan Q3, serta Q3 dan maksimum masing-masing ada 25% data, jadi 75%.</sub>
- B. 25%  
  <sub>Salah: hanya menghitung satu bagian 25% (Q3 sampai maksimum)</sub>
- C. 50%  
  <sub>Salah: hanya menghitung data antara Q1 dan Q3</sub>
- D. 100%  
  <sub>Salah: mengira semua data berada di antara nilai terkecil dan terbesar, padahal batas bawahnya Q1</sub>

**Pembahasan:** Q1 sampai Q2 = 25%, Q2 sampai Q3 = 25%, Q3 sampai maksimum = 25%, total 75%.
**Acuan:** siswa — siswa hal.223 Ayo, Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b06-c-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: bandingkan median dua kelompok*

Dua warung, X dan Y, mencatat penjualan harian (dalam bungkus) selama 10 hari. Data sudah terurut.

- Warung X: 39, 40, 41, 42, 43, 44, 45, 46, 47, 48
- Warung Y: 33, 35, 36, 37, 38, 39, 41, 44, 50, 52

Warung yang penjualan mediannya lebih tinggi, beserta nilai mediannya, adalah ....

- A. Warung Y, median 38,5  
  <sub>Salah: menghitung median Y dengan benar tetapi menyimpulkan Y yang lebih tinggi</sub>
- **B. Warung X, median 43,5** ✅  
  <sub>Benar: Median X = (43 + 44)/2 = 43,5 dan median Y = (38 + 39)/2 = 38,5, sehingga X lebih tinggi.</sub>
- C. Warung X, median 44  
  <sub>Salah: hanya mengambil data ke-6 tanpa merata-ratakan dengan data ke-5</sub>
- D. Warung Y, median 52  
  <sub>Salah: memakai nilai maksimum sebagai median dan membandingkan puncak data</sub>

**Pembahasan:** n = 10 sehingga median = rata-rata data ke-5 dan ke-6. X: (43+44)/2 = 43,5; Y: (38+39)/2 = 38,5.
**Acuan:** siswa — siswa hal.227 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b06-c-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: bandingkan sebaran dua kelompok*

Waktu tempuh (dalam menit) dua rute bus, P dan Q, selama 8 hari. Data sudah terurut.

- Rute P: 24, 25, 26, 27, 28, 29, 30, 31
- Rute Q: 21, 22, 24, 27, 28, 30, 33, 35

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Rute yang waktu tempuhnya lebih konsisten menurut IQR, beserta IQR-nya, adalah ....

- **A. Rute P, IQR = 4 menit** ✅  
  <sub>Benar: P: Q1 = 25,5 dan Q3 = 29,5 sehingga IQR = 4; Q: Q1 = 23 dan Q3 = 31,5 sehingga IQR = 8,5. IQR P lebih kecil.</sub>
- B. Rute Q, IQR = 8,5 menit  
  <sub>Salah: menganggap IQR lebih besar berarti lebih konsisten</sub>
- C. Rute P, IQR = 7 menit  
  <sub>Salah: memakai jangkauan (31 - 24) sebagai IQR</sub>
- D. Rute Q, IQR = 14 menit  
  <sub>Salah: memakai jangkauan (35 - 21) sebagai IQR dan memilih yang lebih besar</sub>

**Pembahasan:** n = 8: Q1 = rata-rata data ke-2 dan ke-3, Q3 = rata-rata data ke-6 dan ke-7. IQR P = 4, IQR Q = 8,5.
**Acuan:** siswa — siswa hal.227 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b06-c-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: bandingkan sebaran dua kelompok*

Banyak roti (dalam ratusan buah) yang dihasilkan dua pabrik selama sebulan diringkas sebagai berikut.

| Ukuran | Pabrik A | Pabrik B |
|---|---|---|
| Minimum | 40 | 48 |
| Q1 | 52 | 56 |
| Median (Q2) | 60 | 62 |
| Q3 | 72 | 68 |
| Maksimum | 85 | 76 |

Kesimpulan yang benar tentang kedua pabrik adalah ....

- A. Pabrik A memiliki median lebih tinggi dan rentang lebih lebar sehingga lebih konsisten  
  <sub>Salah: menganggap rentang lebih lebar berarti lebih konsisten, dan salah membaca median</sub>
- B. Pabrik A memiliki median lebih tinggi dan IQR lebih kecil sehingga lebih konsisten  
  <sub>Salah: terbalik membaca median dan IQR kedua pabrik</sub>
- **C. Pabrik B memiliki median lebih tinggi dan IQR lebih kecil sehingga lebih konsisten** ✅  
  <sub>Benar: Median B 62 > 60; IQR B = 68 - 56 = 12 < IQR A = 72 - 52 = 20.</sub>
- D. Pabrik B memiliki median lebih rendah tetapi IQR lebih kecil sehingga lebih konsisten  
  <sub>Salah: salah membandingkan median (62 lebih besar dari 60)</sub>

**Pembahasan:** Median B = 62 lebih besar dari A = 60. IQR A = 20 dan IQR B = 12; IQR kecil berarti data lebih konsisten.
**Acuan:** siswa — siswa hal.225 Contoh

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b06-c-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: bandingkan median dua kelompok*

Waktu muat halaman (dalam detik) dua aplikasi, X dan Y, dari 7 percobaan (belum terurut).

- Aplikasi X: 2,4; 2,1; 2,6; 2,2; 2,5; 2,3; 2,0
- Aplikasi Y: 2,8; 1,9; 2,0; 1,7; 3,0; 1,8; 2,2

Aplikasi yang umumnya memuat halaman lebih cepat berdasarkan mediannya, beserta mediannya, adalah ....

- A. Aplikasi X, median 2,2 detik  
  <sub>Salah: mengambil data ke-4 dari urutan asli X tanpa mengurutkan</sub>
- B. Aplikasi X, median 2,3 detik  
  <sub>Salah: menghitung median benar tetapi menyimpulkan X lebih cepat karena melihat nilai Y yang besar (3,0)</sub>
- **C. Aplikasi Y, median 2,0 detik** ✅  
  <sub>Benar: Setelah diurutkan, data ke-4 X = 2,3 dan data ke-4 Y = 2,0; median Y lebih kecil sehingga lebih cepat.</sub>
- D. Aplikasi Y, median 1,7 detik  
  <sub>Salah: mengambil data ke-4 dari urutan asli tanpa mengurutkan</sub>

**Pembahasan:** n = 7 sehingga median = data ke-4 setelah diurutkan. X: 2,0; 2,1; 2,2; 2,3; ... median 2,3. Y: 1,7; 1,8; 1,9; 2,0; ... median 2,0.
**Acuan:** siswa — siswa hal.228 Latihan 6.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b06-c-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: bandingkan sebaran dua kelompok*

Volume isi botol (dalam mL) yang dihasilkan dua mesin pengisi, A dan B, dari 6 botol masing-masing. Data sudah terurut.

- Mesin A: 498, 499, 500, 500, 501, 502
- Mesin B: 495, 497, 500, 501, 503, 506

Mesin yang isinya lebih seragam berdasarkan jangkauan (maksimum - minimum), beserta jangkauannya, adalah ....

- A. Mesin B, jangkauan 11 mL  
  <sub>Salah: menganggap jangkauan lebih besar berarti lebih seragam</sub>
- **B. Mesin A, jangkauan 4 mL** ✅  
  <sub>Benar: Jangkauan A = 502 - 498 = 4 dan jangkauan B = 506 - 495 = 11; jangkauan lebih kecil berarti lebih seragam.</sub>
- C. Mesin A, jangkauan 502 mL  
  <sub>Salah: memakai nilai maksimum sebagai jangkauan</sub>
- D. Mesin A, jangkauan 1 mL  
  <sub>Salah: mengurangkan dua data terakhir (502 - 501), bukan maksimum dengan minimum</sub>

**Pembahasan:** Jangkauan = maksimum - minimum. Mesin A: 502 - 498 = 4 mL; Mesin B: 506 - 495 = 11 mL.
**Acuan:** siswa — siswa hal.228 Latihan 6.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b06-c-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: jenis korelasi dari pasangan data*

Delapan siswa dicatat lama bermain gim per hari (sumbu x) dan nilai ulangan matematika (sumbu y).

| Jam bermain gim per hari | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Nilai ulangan | 92 | 88 | 85 | 79 | 74 | 71 | 65 | 60 |

Jika pasangan data itu digambar sebagai diagram pencar, jenis korelasinya adalah ....

- A. Korelasi positif sedang  
  <sub>Salah: salah arah dan salah menilai kekuatan hubungan</sub>
- B. Korelasi positif kuat  
  <sub>Salah: membalik arah: mengira y ikut naik saat x naik</sub>
- C. Tidak ada korelasi  
  <sub>Salah: mengira titik tersebar acak padahal polanya jelas menurun</sub>
- **D. Korelasi negatif kuat** ✅  
  <sub>Benar: Nilai y turun hampir lurus ketika x naik dari 1 sampai 8, sehingga korelasi negatif dan titik-titik hampir segaris.</sub>

**Pembahasan:** Setiap kenaikan x diikuti penurunan y secara hampir lurus: korelasi negatif kuat.
**Acuan:** siswa — siswa hal.236 Latihan 6.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b06-c-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: jenis korelasi dari pasangan data*

Seorang pedagang mencatat suhu udara (sumbu x) dan banyak es teh terjual (sumbu y) selama 8 hari.

| Suhu udara (derajat Celsius) | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
|---|---|---|---|---|---|---|---|---|
| Es teh terjual (gelas) | 40 | 46 | 50 | 58 | 63 | 69 | 75 | 80 |

Jenis korelasi antara suhu udara dan penjualan es teh adalah ....

- A. Korelasi negatif sedang  
  <sub>Salah: salah arah dan menganggap titik terlalu menyebar</sub>
- B. Tidak ada korelasi  
  <sub>Salah: mengira data tidak punya pola padahal selalu naik</sub>
- **C. Korelasi positif kuat** ✅  
  <sub>Benar: Penjualan naik hampir lurus ketika suhu naik, sehingga positif dan titik-titik mendekati garis lurus.</sub>
- D. Korelasi negatif kuat  
  <sub>Salah: membalik arah hubungan</sub>

**Pembahasan:** Suhu naik diikuti penjualan naik secara hampir linear: korelasi positif kuat.
**Acuan:** siswa — siswa hal.234 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b06-c-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: jenis korelasi dari pasangan data*

Delapan siswa dicatat nomor sepatu (sumbu x) dan nilai ulangan matematika (sumbu y).

| Nomor sepatu | 38 | 40 | 39 | 41 | 37 | 42 | 40 | 39 |
|---|---|---|---|---|---|---|---|---|
| Nilai matematika | 78 | 65 | 90 | 85 | 72 | 70 | 88 | 68 |

Pernyataan yang paling sesuai dengan diagram pencar dari data itu adalah ....

- **A. Tidak ada korelasi antara nomor sepatu dan nilai matematika** ✅  
  <sub>Benar: Nilai y naik turun tidak beraturan ketika x bertambah, tanpa kecenderungan naik atau turun.</sub>
- B. Korelasi positif kuat: makin besar nomor sepatu, makin tinggi nilai  
  <sub>Salah: mengira ada hubungan padahal tidak ada pola naik</sub>
- C. Korelasi positif sedang: nilai cenderung naik bersama nomor sepatu  
  <sub>Salah: menganggap sedikit kenaikan acak sebagai korelasi positif</sub>
- D. Korelasi negatif kuat: makin besar nomor sepatu, makin rendah nilai  
  <sub>Salah: mengira ada pola menurun padahal acak</sub>

**Pembahasan:** Pada nomor sepatu yang sama (mis. 40) nilainya 65 dan 88; titik menyebar tanpa arah. Tidak ada korelasi.
**Acuan:** siswa — siswa hal.237 Latihan 6.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b06-c-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: banyak data pencilan*

Waktu pengerjaan (dalam menit) 12 peserta lomba yang diurutkan: 3, 40, 41, 42, 43, 44, 44, 45, 46, 47, 48, 95. Dari data ini diperoleh Q1 = 41,5 dan Q3 = 46,5. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Banyak peserta yang waktu pengerjaannya tergolong pencilan adalah ....

- A. 1 peserta  
  <sub>Salah: hanya memeriksa data terbesar dan lupa batas bawah</sub>
- B. 0 peserta  
  <sub>Salah: mengira tidak ada data yang melewati batas</sub>
- C. 3 peserta  
  <sub>Salah: ikut menghitung 40 yang berada tepat di dalam batas bawah 34</sub>
- **D. 2 peserta** ✅  
  <sub>Benar: IQR = 5; batas bawah = 41,5 - 7,5 = 34 dan batas atas = 46,5 + 7,5 = 54; data 3 dan 95 di luar batas.</sub>

**Pembahasan:** Batas wajar 34 sampai 54. Data di luarnya: 3 dan 95, jadi 2 pencilan.
**Acuan:** siswa — siswa hal.223 Ayo, Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b06-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: konsep lima ukuran diagram kotak garis*

Ukuran berikut yang BUKAN salah satu dari lima ukuran data yang dipakai untuk menggambar diagram kotak garis (box plot) adalah ....

- **A. Modus** ✅  
  <sub>Benar: Lima ukuran: minimum, Q1, median, Q3, maksimum; modus tidak termasuk.</sub>
- B. Nilai minimum  
  <sub>Salah: minimum termasuk lima ukuran (ujung kumis kiri)</sub>
- C. Median  
  <sub>Salah: median termasuk lima ukuran (Q2)</sub>
- D. Kuartil ketiga (Q3)  
  <sub>Salah: Q3 termasuk lima ukuran</sub>

**Pembahasan:** Diagram kotak garis memakai minimum, Q1, median, Q3, dan maksimum. Modus tidak dipakai.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b06-c-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: menghitung IQR dari lima ukuran*

Ringkasan lima ukuran data nilai ujian: minimum 15, Q1 = 28, Q2 = 35, Q3 = 47, maksimum 60.

Jangkauan interkuartil (IQR) data nilai itu adalah ....

- A. 32  
  <sub>Salah: menghitung Q3 - minimum</sub>
- B. 45  
  <sub>Salah: menghitung jangkauan (maksimum - minimum)</sub>
- C. 12  
  <sub>Salah: menghitung Q3 - Q2</sub>
- **D. 19** ✅  
  <sub>Benar: IQR = Q3 - Q1 = 47 - 28 = 19.</sub>

**Pembahasan:** IQR = Q3 - Q1 = 47 - 28 = 19.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b06-c-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: menentukan Q1 dan Q3 data tunggal*

Data terurut (n = 12): 12, 15, 17, 18, 21, 23, 24, 27, 29, 30, 34, 38.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Nilai Q1 dan Q3 data tersebut berturut-turut adalah ....

- A. Q1 = 17,5 dan Q3 = 27  
  <sub>Salah: Q1 benar, tetapi Q3 diambil dari data ke-8</sub>
- **B. Q1 = 17,5 dan Q3 = 29,5** ✅  
  <sub>Benar: n/4 = 3 sehingga Q1 = (17 + 18)/2 = 17,5; 3n/4 = 9 sehingga Q3 = (29 + 30)/2 = 29,5.</sub>
- C. Q1 = 18 dan Q3 = 30  
  <sub>Salah: mengambil data ke-4 dan ke-10 (data setelahnya) saja</sub>
- D. Q1 = 17 dan Q3 = 29  
  <sub>Salah: hanya mengambil data ke-3 dan ke-9 tanpa merata-ratakan dengan data berikutnya</sub>

**Pembahasan:** n/4 = 3 (bulat): rata-rata data ke-3 dan ke-4. 3n/4 = 9 (bulat): rata-rata data ke-9 dan ke-10.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b06-c-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: tafsir persentase data pada diagram kotak garis*

Dari 48 nilai terurut diperoleh Q1 = 15, Q2 = 22, dan Q3 = 31.

Banyak nilai yang terletak di antara Q1 dan Q3 adalah ....

- A. 48 nilai  
  <sub>Salah: mengira semua data berada di antara Q1 dan Q3</sub>
- **B. 24 nilai** ✅  
  <sub>Benar: Antara Q1 dan Q3 ada 50% data, yaitu 50% x 48 = 24.</sub>
- C. 36 nilai  
  <sub>Salah: menghitung 75% data (dari minimum sampai Q3)</sub>
- D. 12 nilai  
  <sub>Salah: hanya menghitung 25% data (satu bagian)</sub>

**Pembahasan:** Q1 ke Q2 = 25% dan Q2 ke Q3 = 25%, jadi 50% x 48 = 24.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b06-c-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: konsep pencilan*

Menurut aturan pada diagram kotak garis, sebuah data disebut pencilan jika ....

- A. berbeda lebih dari 1,5 dari modus  
  <sub>Salah: mengaitkan pencilan dengan modus</sub>
- B. terletak di antara Q1 dan Q3  
  <sub>Salah: menyebut data di dalam kotak, yang justru data wajar</sub>
- **C. kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR** ✅  
  <sub>Benar: Batas pencilan berjarak 1,5 kali IQR di bawah Q1 dan di atas Q3.</sub>
- D. lebih besar dari 1,5 kali nilai median  
  <sub>Salah: mengganti IQR dengan median</sub>

**Pembahasan:** Pencilan: < Q1 - 1,5 x IQR atau > Q3 + 1,5 x IQR.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b06-c-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: konsep jenis korelasi*

Situasi berikut yang menunjukkan korelasi negatif adalah ....

- A. makin tinggi badan seseorang, makin besar ukuran sepatunya  
  <sub>Salah: kedua variabel naik bersama (korelasi positif)</sub>
- B. makin tinggi suhu ruangan, makin banyak es krim yang terjual  
  <sub>Salah: kedua variabel naik bersama (korelasi positif)</sub>
- C. nomor urut absen siswa dan tinggi badannya  
  <sub>Salah: tidak ada hubungan arah yang jelas (tidak ada korelasi)</sub>
- **D. makin lama sebuah motor dipakai berkeliling, makin sedikit bensin yang tersisa** ✅  
  <sub>Benar: lama pemakaian naik, sisa bensin turun: berlawanan arah.</sub>

**Pembahasan:** Korelasi negatif: satu variabel naik, variabel lain turun. Hanya bensin yang memenuhi.
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b06-c-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: korelasi dan sebab-akibat*

Di sebuah kota, data bulanan menunjukkan korelasi positif yang kuat antara banyak es krim yang terjual dan banyak kunjungan ke kolam renang.

Kesimpulan yang paling tepat dari data itu adalah ....

- A. kunjungan ke kolam renang menyebabkan penjualan es krim bertambah  
  <sub>Salah: menyimpulkan sebab-akibat arah sebaliknya</sub>
- B. penjualan es krim harus dilarang agar kunjungan ke kolam renang turun  
  <sub>Salah: mengambil tindakan atas anggapan sebab-akibat yang salah</sub>
- C. penjualan es krim menyebabkan kunjungan ke kolam renang bertambah  
  <sub>Salah: menyimpulkan sebab-akibat dari korelasi</sub>
- **D. kedua hal cenderung naik bersama, tetapi korelasi saja tidak membuktikan satu menyebabkan yang lain** ✅  
  <sub>Benar: Korelasi hanya menunjukkan hubungan arah; sebab-akibat memerlukan bukti lain (misalnya cuaca panas memengaruhi keduanya).</sub>

**Pembahasan:** Korelasi positif kuat tidak sama dengan sebab-akibat; keduanya bisa dipengaruhi faktor lain.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b06-c-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: koordinat titik pada diagram pencar*

| Siswa | Jam belajar | Nilai |
|---|---|---|
| Andi | 2 | 60 |
| Budi | 5 | 78 |
| Dina | 3 | 72 |
| Eka | 6 | 85 |

Pada diagram pencar, sumbu x menunjukkan jam belajar dan sumbu y menunjukkan nilai.

Koordinat titik yang mewakili Dina adalah ....

- A. (72, 3)  
  <sub>Salah: menukar sumbu x dan y</sub>
- B. (5, 72)  
  <sub>Salah: memakai jam belajar milik Budi untuk sumbu x</sub>
- **C. (3, 72)** ✅  
  <sub>Benar: Dina belajar 3 jam (x) dan bernilai 72 (y), sehingga titiknya (3, 72).</sub>
- D. (3, 78)  
  <sub>Salah: memakai nilai milik Budi untuk sumbu y</sub>

**Pembahasan:** Titik = (jam belajar, nilai) = (3, 72).
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b06-c-medium-bt01-001
*variasi (angka) | C3 | 4 langkah | jenis: pencilan dari data mentah*

Tagihan air bulanan (dalam ribu rupiah) dari 10 rumah di sebuah gang, belum terurut: 85, 92, 88, 90, 95, 89, 310, 91, 87, 94.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Data yang tergolong pencilan beserta batas atas pencilannya adalah ....

- **A. 310 ribu rupiah, batas atas 103** ✅  
  <sub>Benar: Terurut: 85, 87, 88, 89, 90, 91, 92, 94, 95, 310. n/4 = 2,5 sehingga Q1 = data ke-3 = 88; 3n/4 = 7,5 sehingga Q3 = data ke-8 = 94. IQR = 6, batas atas = 94 + 9 = 103, batas bawah = 79. Hanya 310 di luar batas.</sub>
- B. 310 ribu rupiah, batas atas 100  
  <sub>Salah: memakai Q3 + IQR tanpa faktor 1,5</sub>
- C. 95 ribu rupiah, batas atas 94  
  <sub>Salah: menganggap data di atas Q3 sebagai pencilan tanpa faktor 1,5 x IQR</sub>
- D. Tidak ada pencilan, batas atas 431,5  
  <sub>Salah: memakai jangkauan (310 - 85) sebagai IQR</sub>

**Pembahasan:** Urutkan data, Q1 = 88, Q3 = 94, IQR = 6, batas atas = 94 + 1,5 x 6 = 103 dan batas bawah = 79. Hanya 310 yang melebihi 103.
**Acuan:** siswa — siswa hal.224 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b06-c-medium-bt01-002
*variasi (konteks) | C4 | 4 langkah | jenis: bandingkan konsistensi dari data mentah (IQR vs jangkauan)*

Daya tahan baterai (dalam jam) dua merek, X dan Y, diuji pada 10 baterai masing-masing (belum terurut).

- Merek X: 14, 12, 13, 15, 13, 12, 14, 13, 28, 14
- Merek Y: 9, 16, 11, 18, 13, 10, 17, 12, 15, 14

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Merek yang daya tahannya lebih konsisten menurut IQR, beserta IQR-nya, adalah ....

- A. Merek Y, IQR = 5 jam  
  <sub>Salah: memilih berdasarkan jangkauan (X: 16, Y: 9) dan menganggap IQR kecil berarti kurang konsisten</sub>
- B. Merek X, IQR = 2 jam  
  <sub>Salah: mengambil Q1 dari data ke-2 (12) bukan data ke-3</sub>
- C. Merek Y, IQR = 9 jam  
  <sub>Salah: memakai jangkauan Y sebagai IQR</sub>
- **D. Merek X, IQR = 1 jam** ✅  
  <sub>Benar: Merek X terurut: 12, 12, 13, 13, 13, 14, 14, 14, 15, 28 sehingga Q1 = 13 dan Q3 = 14 (IQR 1). Merek Y terurut: 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 sehingga Q1 = 11 dan Q3 = 16 (IQR 5). IQR X lebih kecil.</sub>

**Pembahasan:** n = 10: Q1 = data ke-3, Q3 = data ke-8. IQR X = 14 - 13 = 1, IQR Y = 16 - 11 = 5. IQR tidak terpengaruh nilai 28, jadi X lebih konsisten.
**Acuan:** siswa — siswa hal.225 Contoh

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b06-c-medium-bt01-003
*variasi (konteks) | C4 | 3 langkah | jenis: titik menyimpang pada diagram pencar*

Seorang petani mencatat banyak pupuk (kg, sumbu x) dan hasil panen (kuintal, sumbu y) pada 10 petak, belum terurut menurut x.

| Pupuk (kg) | 2 | 5 | 3 | 8 | 1 | 6 | 4 | 9 | 7 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Hasil panen (kuintal) | 26 | 35 | 29 | 28 | 23 | 38 | 32 | 47 | 41 | 50 |

Jika pasangan data itu digambar sebagai diagram pencar, pernyataan yang benar adalah ....

- A. Korelasi negatif, dan petak dengan pupuk 8 kg dan hasil 28 kuintal menyimpang dari pola  
  <sub>Salah: salah arah: satu titik rendah dianggap mewakili tren menurun</sub>
- **B. Korelasi positif, dan petak dengan pupuk 8 kg dan hasil 28 kuintal menyimpang dari pola** ✅  
  <sub>Benar: Setelah diurutkan menurut x, y naik 3 kuintal setiap tambahan 1 kg pupuk (23, 26, 29, 32, 35, 38, 41, 47, 50) kecuali pada x = 8 yang hasilnya 28 (seharusnya sekitar 44).</sub>
- C. Korelasi positif, dan petak dengan pupuk 10 kg dan hasil 50 kuintal menyimpang dari pola  
  <sub>Salah: menandai titik terbesar sebagai menyimpang padahal masih tepat pada pola</sub>
- D. Tidak ada korelasi, dan petak dengan pupuk 8 kg dan hasil 28 kuintal menyimpang dari pola  
  <sub>Salah: satu titik menyimpang dianggap membuat seluruh titik acak</sub>

**Pembahasan:** Urutkan menurut x: hasil panen naik tetap 3 kuintal per kg pupuk, kecuali x = 8 (28 kuintal, jauh di bawah 44). Arah naik berarti korelasi positif.
**Acuan:** siswa — siswa hal.236 Latihan 6.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b06-c-medium-bt01-004
*variasi (konteks) | C3 | 4 langkah | jenis: selisih IQR dua kelompok*

Waktu pengantaran (dalam menit) pesanan oleh dua kurir, A dan B, pada 12 pengantaran masing-masing (belum terurut).

- Kurir A: 32, 45, 38, 41, 36, 50, 44, 39, 47, 42, 35, 40
- Kurir B: 30, 52, 38, 44, 58, 35, 48, 41, 55, 33, 46, 50

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Selisih IQR kedua kurir (IQR yang lebih besar dikurangi IQR yang lebih kecil) adalah ....

- A. 10 menit  
  <sub>Salah: mengurangkan jangkauan kedua kurir (28 - 18), bukan IQR</sub>
- B. 14,5 menit  
  <sub>Salah: hanya menyebut IQR kurir B tanpa dikurangi IQR kurir A</sub>
- C. 6,5 menit  
  <sub>Salah: mengurangkan Q3 kedua kurir (51 - 44,5), bukan IQR</sub>
- **D. 7 menit** ✅  
  <sub>Benar: A terurut: 32, 35, 36, 38, 39, 40, 41, 42, 44, 45, 47, 50 sehingga Q1 = (36 + 38)/2 = 37, Q3 = (44 + 45)/2 = 44,5, IQR 7,5. B terurut: 30, 33, 35, 38, 41, 44, 46, 48, 50, 52, 55, 58 sehingga Q1 = (35 + 38)/2 = 36,5, Q3 = (50 + 52)/2 = 51, IQR 14,5. Selisih 7.</sub>

**Pembahasan:** n = 12: n/4 = 3 dan 3n/4 = 9 (bulat). IQR A = 44,5 - 37 = 7,5; IQR B = 51 - 36,5 = 14,5; selisih = 7.
**Acuan:** siswa — siswa hal.227 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b06-c-medium-bt01-005
*variasi (konteks) | C4 | 4 langkah | jenis: tafsir korelasi dari rata-rata dua kelompok*

Sebuah toko mencatat banyak iklan yang dipasang per minggu (sumbu x) dan banyak pengunjung baru per minggu (sumbu y) selama 10 minggu.

| Iklan per minggu | 3 | 6 | 1 | 8 | 4 | 2 | 7 | 3 | 9 | 5 |
|---|---|---|---|---|---|---|---|---|---|---|
| Pengunjung baru | 210 | 330 | 150 | 410 | 250 | 190 | 380 | 230 | 460 | 300 |

Pasangan data dengan 3 iklan atau kurang dibandingkan dengan pasangan data dengan 6 iklan atau lebih. Pernyataan yang benar adalah ....

- A. korelasi positif; rata-rata pengunjung baru: 780 untuk 3 iklan atau kurang dan 1.580 untuk 6 iklan atau lebih  
  <sub>Salah: memakai jumlah, bukan rata-rata</sub>
- **B. korelasi positif; rata-rata pengunjung baru: 195 untuk 3 iklan atau kurang dan 395 untuk 6 iklan atau lebih** ✅  
  <sub>Benar: Iklan 3 atau kurang: 210, 150, 190, 230 dengan rata-rata 780/4 = 195. Iklan 6 atau lebih: 330, 410, 380, 460 dengan rata-rata 1.580/4 = 395. Rata-rata naik saat iklan bertambah.</sub>
- C. korelasi negatif; rata-rata pengunjung baru: 395 untuk 3 iklan atau kurang dan 195 untuk 6 iklan atau lebih  
  <sub>Salah: menukar dua kelompok sehingga arah korelasi terbalik</sub>
- D. tidak ada korelasi; rata-rata pengunjung baru: 195 untuk 3 iklan atau kurang dan 395 untuk 6 iklan atau lebih  
  <sub>Salah: menghitung rata-rata benar tetapi mengabaikan kenaikan yang konsisten</sub>

**Pembahasan:** Rata-rata 4 pasangan dengan x <= 3 adalah 195 dan dengan x >= 6 adalah 395; makin banyak iklan, makin banyak pengunjung: korelasi positif.
**Acuan:** siswa — siswa hal.237 Latihan 6.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b06-c-medium-bt01-006
*variasi (konteks) | C4 | 4 langkah | jenis: median dan IQR dua kelompok bersamaan*

Waktu respons (dalam milidetik) dua server, P dan Q, pada 10 permintaan masing-masing (belum terurut).

- Server P: 30, 55, 36, 33, 48, 35, 45, 52, 37, 38
- Server Q: 41, 46, 36, 44, 39, 42, 38, 45, 43, 40

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Pernyataan yang benar tentang kedua server adalah ....

- A. median P (37) lebih rendah daripada median Q (41), tetapi IQR P (13) lebih besar daripada IQR Q (5); P umumnya lebih cepat namun kurang konsisten  
  <sub>Salah: mengambil data ke-5 saja sebagai median tanpa merata-ratakan dengan data ke-6</sub>
- **B. median P (37,5) lebih rendah daripada median Q (41,5), tetapi IQR P (13) lebih besar daripada IQR Q (5); P umumnya lebih cepat namun kurang konsisten** ✅  
  <sub>Benar: P terurut: 30, 33, 35, 36, 37, 38, 45, 48, 52, 55: median = (37 + 38)/2 = 37,5; Q1 = 35, Q3 = 48, IQR = 13. Q terurut: 36, 38, 39, 40, 41, 42, 43, 44, 45, 46: median = (41 + 42)/2 = 41,5; Q1 = 39, Q3 = 44, IQR = 5.</sub>
- C. median P (37,5) lebih rendah daripada median Q (41,5) dan IQR P (5) lebih kecil daripada IQR Q (13); P umumnya lebih cepat dan lebih konsisten  
  <sub>Salah: menukar nilai IQR kedua server</sub>
- D. median Q (37,5) lebih rendah daripada median P (41,5), tetapi IQR Q (13) lebih besar daripada IQR P (5); Q umumnya lebih cepat namun kurang konsisten  
  <sub>Salah: menukar nama server pada seluruh hasil hitungan</sub>

**Pembahasan:** n = 10: median = rata-rata data ke-5 dan ke-6; Q1 = data ke-3; Q3 = data ke-8. P: median 37,5, IQR 48 - 35 = 13. Q: median 41,5, IQR 44 - 39 = 5.
**Acuan:** siswa — siswa hal.228 Latihan 6.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b06-c-medium-bt01-007
*orisinal | C3 | 4 langkah | jenis: mencocokkan data dengan lima ukuran*

Diagram kotak garis suatu kumpulan 10 data memiliki nilai minimum 12, Q1 = 18, median (Q2) = 25, Q3 = 31, dan nilai maksimum 44.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu.

Kumpulan 10 data terurut yang sesuai dengan diagram kotak garis itu adalah ....

- A. 12, 15, 18, 22, 24, 26, 29, 34, 38, 44  
  <sub>Salah: Q3 = data ke-8 = 34, bukan 31</sub>
- B. 12, 15, 18, 22, 24, 26, 29, 31, 38, 40  
  <sub>Salah: nilai maksimum 40, bukan 44</sub>
- **C. 12, 15, 18, 22, 24, 26, 29, 31, 38, 44** ✅  
  <sub>Benar: n = 10: Q1 = data ke-3 = 18, median = (24 + 26)/2 = 25, Q3 = data ke-8 = 31, minimum 12, maksimum 44.</sub>
- D. 12, 15, 18, 22, 26, 28, 29, 31, 38, 44  
  <sub>Salah: median = (26 + 28)/2 = 27, bukan 25</sub>

**Pembahasan:** Periksa kelima ukuran tiap pilihan. Hanya pilihan benar yang memberi 12, 18, 25, 31, 44.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b06-c-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: bagian 25% data paling rapat*

Nilai 80 siswa diringkas: minimum 20, Q1 = 45, Q2 = 50, Q3 = 68, dan maksimum 78.

Bagian nilai yang memuat 25% data dengan sebaran paling sempit (paling rapat) beserta banyak siswa di bagian itu adalah ....

- A. antara 20 dan 45, yaitu 20 siswa  
  <sub>Salah: memilih bagian terlebar (25) sebagai yang paling rapat</sub>
- B. antara 68 dan 78, yaitu 20 siswa  
  <sub>Salah: menganggap kumis atas (lebar 10) paling sempit padahal lebar 5 lebih kecil</sub>
- **C. antara 45 dan 50, yaitu 20 siswa** ✅  
  <sub>Benar: Lebar keempat bagian: 20 ke 45 = 25, 45 ke 50 = 5, 50 ke 68 = 18, 68 ke 78 = 10. Terkecil 5 (antara Q1 dan Q2), memuat 25% x 80 = 20 siswa.</sub>
- D. antara 45 dan 50, yaitu 40 siswa  
  <sub>Salah: mengira bagian itu memuat 50% data</sub>

**Pembahasan:** Tiap bagian antar-ukuran memuat 25% data (20 siswa). Bagian dengan selisih terkecil (5) paling rapat: antara Q1 dan Q2.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b06-c-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: pencilan dengan nilai di batas*

Dari data nilai sebuah tes diperoleh Q1 = 40 dan Q3 = 52. Tiga nilai terendah adalah 15, 22, 30 dan tiga nilai tertinggi adalah 66, 70, 74.

Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Nilai yang tergolong pencilan adalah ....

- **A. 15 dan 74** ✅  
  <sub>Benar: IQR = 12; batas bawah = 40 - 18 = 22 dan batas atas = 52 + 18 = 70. Pencilan harus kurang dari 22 atau lebih dari 70: hanya 15 dan 74 (22 dan 70 tepat di batas, bukan pencilan).</sub>
- B. 15, 22, 70, dan 74  
  <sub>Salah: menganggap nilai tepat di batas (22 dan 70) sebagai pencilan padahal harus kurang atau lebih dari batas</sub>
- C. 74 saja  
  <sub>Salah: hanya memeriksa batas atas dan lupa batas bawah</sub>
- D. 15, 22, 66, 70, dan 74  
  <sub>Salah: memakai Q1 - IQR dan Q3 + IQR (batas 28 dan 64) tanpa faktor 1,5</sub>

**Pembahasan:** Batas wajar 22 sampai 70. Nilai 22 dan 70 masih di dalam batas, sehingga pencilan hanya 15 dan 74.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b06-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: nilai terbesar yang bukan pencilan*

Pada data waktu tempuh (menit) diperoleh Q1 = 49, median = 55, dan Q3 = 62. Seorang peserta baru akan menambahkan satu data bilangan bulat dan nilai Q1 dan Q3 dianggap tidak berubah.

Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Bilangan bulat terbesar yang masih bukan pencilan adalah ....

- **A. 81** ✅  
  <sub>Benar: IQR = 62 - 49 = 13; batas atas = 62 + 1,5 x 13 = 81,5. Bilangan bulat terbesar yang tidak lebih dari 81,5 adalah 81.</sub>
- B. 75  
  <sub>Salah: memakai Q3 + IQR tanpa faktor 1,5</sub>
- C. 72  
  <sub>Salah: memakai IQR = Q3 - median = 7 sehingga batas atas 72,5</sub>
- D. 82  
  <sub>Salah: membulatkan batas atas 81,5 ke atas, padahal 82 > 81,5 sudah pencilan</sub>

**Pembahasan:** Batas atas = 81,5. Data bulat yang lebih dari 81,5 adalah pencilan, jadi 81 adalah yang terbesar yang bukan pencilan.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b06-c-medium-bt01-011
*orisinal | C4 | 4 langkah | jenis: dampak membuang pencilan*

Waktu pengerjaan (menit) 11 peserta, sudah terurut: 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 95. Data 95 adalah pencilan dan dibuang dari kumpulan data.

Setelah data 95 dibuang, jangkauan (maksimum - minimum) berkurang sebesar .... dan median yang baru adalah ....

- A. 57 dan 43,5  
  <sub>Salah: menyebut jangkauan lama sebagai besar pengurangan</sub>
- B. 10 dan 43,5  
  <sub>Salah: menyebut jangkauan baru sebagai besar pengurangan</sub>
- C. 47 dan 44  
  <sub>Salah: tidak menghitung ulang median; memakai median 11 data</sub>
- **D. 47 dan 43,5** ✅  
  <sub>Benar: Jangkauan semula 95 - 38 = 57, sekarang 48 - 38 = 10, berkurang 47. Sekarang ada 10 data sehingga median = (43 + 44)/2 = 43,5.</sub>

**Pembahasan:** Jangkauan turun dari 57 menjadi 10 (berkurang 47). Dengan 10 data, median = rata-rata data ke-5 dan ke-6 = 43,5.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b06-c-medium-bt01-012
*orisinal | C3 | 4 langkah | jenis: menghitung banyak data dari persentase kuartil*

Nilai ulangan dua kelas diringkas dengan diagram kotak garis.

- Kelas A (32 siswa): minimum 45, Q1 = 70, Q2 = 78, Q3 = 85, maksimum 98.
- Kelas B (40 siswa): minimum 30, Q1 = 48, Q2 = 58, Q3 = 70, maksimum 92.

Banyak siswa kelas A yang nilainya antara 70 dan nilai maksimum, ditambah banyak siswa kelas B yang nilainya antara 70 dan nilai maksimum, adalah ....

- A. 18 siswa  
  <sub>Salah: mengira kelas A hanya 25% data di atas 70 (menganggap 70 sebagai Q3)</sub>
- B. 26 siswa  
  <sub>Salah: mengira kelas A hanya 50% data di atas 70 (menganggap 70 sebagai Q2)</sub>
- **C. 34 siswa** ✅  
  <sub>Benar: Kelas A: 70 adalah Q1, dari Q1 sampai maksimum ada 75% x 32 = 24 siswa. Kelas B: 70 adalah Q3, dari Q3 sampai maksimum ada 25% x 40 = 10 siswa. Jumlah 34.</sub>
- D. 54 siswa  
  <sub>Salah: mengira 70 adalah Q1 pada kedua kelas (75% dari tiap kelas)</sub>

**Pembahasan:** Kelas A: 75% x 32 = 24. Kelas B: 25% x 40 = 10. Total 34.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b06-c-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: membandingkan kekuatan korelasi*

Dua kelompok pasangan data (x, y) memiliki nilai x yang sama.

| x | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| y kelompok P | 5 | 7 | 9 | 11 | 13 | 15 |
| y kelompok Q | 8 | 6 | 14 | 9 | 15 | 12 |

Jika kedua kelompok digambar sebagai diagram pencar, pernyataan yang benar adalah ....

- A. P berkorelasi positif sedangkan Q berkorelasi negatif karena y Q beberapa kali turun  
  <sub>Salah: menganggap penurunan sesekali sebagai arah korelasi negatif padahal kecenderungan keseluruhan naik</sub>
- B. korelasi Q lebih kuat daripada P karena nilai y Q lebih bervariasi  
  <sub>Salah: mengira variasi nilai y yang besar berarti korelasi kuat</sub>
- C. keduanya berkorelasi positif dan sama kuat karena nilai x-nya sama  
  <sub>Salah: mengira kekuatan korelasi hanya ditentukan nilai x</sub>
- **D. keduanya berkorelasi positif, tetapi korelasi P lebih kuat karena titik-titiknya tepat pada satu garis lurus** ✅  
  <sub>Benar: Pada P, y selalu naik 2 setiap x naik 1 (y = 2x + 3), sehingga semua titik segaris. Pada Q, y cenderung naik tetapi titik-titiknya menyebar (misalnya turun dari 8 ke 6 dan dari 14 ke 9).</sub>

**Pembahasan:** Korelasi kuat berarti titik sangat dekat pada garis lurus. P tepat pada garis y = 2x + 3 (kuat), Q naik secara kasar dengan sebaran besar (positif, tetapi lebih lemah).
**Acuan:** siswa — siswa hal.232

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b06-c-medium-bt01-014
*orisinal | C3 | 4 langkah | jenis: IQR dan banyak pencilan data mentah ganjil*

Lama latihan (dalam menit) 15 atlet, belum terurut: 52, 48, 55, 50, 49, 30, 53, 51, 50, 46, 54, 49, 88, 47, 52.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

IQR data tersebut dan banyak pencilannya berturut-turut adalah ....

- A. IQR = 5 dan 1 pencilan  
  <sub>Salah: hanya memeriksa batas atas (88) dan lupa data 30 di bawah batas bawah</sub>
- B. IQR = 58 dan 0 pencilan  
  <sub>Salah: memakai jangkauan (88 - 30) sebagai IQR sehingga batas pencilan menjadi sangat lebar</sub>
- **C. IQR = 5 dan 2 pencilan** ✅  
  <sub>Benar: Terurut: 30, 46, 47, 48, 49, 49, 50, 50, 51, 52, 52, 53, 54, 55, 88. n/4 = 3,75 sehingga Q1 = data ke-4 = 48; 3n/4 = 11,25 sehingga Q3 = data ke-12 = 53. IQR = 5; batas = 40,5 dan 60,5. Data di luar batas: 30 dan 88.</sub>
- D. IQR = 4 dan 2 pencilan  
  <sub>Salah: membulatkan Q3 ke bawah sehingga memakai data ke-11 (52) dan Q1 data ke-4</sub>

**Pembahasan:** Q1 = 48, Q3 = 53, IQR = 5. Batas wajar 40,5 sampai 60,5. Data 30 dan 88 berada di luar batas: 2 pencilan.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas10-b06-c-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim korelasi vs sebab-akibat*

Dinas pemadam kebakaran mencatat 8 kebakaran gedung. Tabel berikut memuat banyak unit mobil pemadam yang dikirim dan kerugian (dalam juta rupiah). Titik-titik pada diagram pencar data ini hampir membentuk garis lurus naik.

|Unit dikirim|Kerugian (juta rupiah)|
|---|---|
|2|40|
|3|55|
|4|90|
|6|120|
|7|150|
|9|210|
|10|230|
|12|300|

Seorang pejabat menyimpulkan: "Makin banyak unit dikirim, makin besar kerugian. Jadi mengurangi jumlah unit yang dikirim akan menurunkan kerugian." Penilaian yang paling tepat terhadap kesimpulan itu adalah ....

- A. Sah, karena korelasi positif yang kuat membuktikan bahwa banyak unit yang menyebabkan kerugian  
  <sub>Salah: menyamakan korelasi kuat dengan sebab-akibat</sub>
- B. Tidak sah, karena korelasi hanya boleh ditafsirkan bila semua titik tepat berada pada satu garis lurus  
  <sub>Salah: menganggap korelasi hanya bermakna bila sempurna</sub>
- **C. Tidak sah, karena data hanya menunjukkan korelasi positif; kebakaran yang lebih besar mungkin memerlukan lebih banyak unit sekaligus merugikan lebih banyak** ✅  
  <sub>Benar: Korelasi positif hanya berarti keduanya cenderung naik bersama. Ukuran kebakaran dapat menjadi faktor lain yang memengaruhi keduanya, sehingga sebab-akibat dari unit ke kerugian tidak terbukti.</sub>
- D. Tidak sah, karena data itu menunjukkan korelasi negatif antara unit dan kerugian  
  <sub>Salah: salah membaca arah korelasi</sub>

**Pembahasan:** Unit dan kerugian berkorelasi positif kuat, tetapi korelasi tidak membuktikan sebab-akibat; faktor ukuran kebakaran bisa menjelaskan keduanya.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas10-b06-c-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: evaluasi dampak membuang pencilan*

Gaji bulanan (juta rupiah) 11 karyawan sebuah kantor kecil: 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 40.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Data 40 tergolong pencilan dan dibuang, sehingga tersisa 10 data. Pernyataan yang benar tentang perubahan ukuran data setelah pembuangan adalah ....

- **A. Rata-rata turun lebih dari 3 juta, median turun 0,5 juta, dan IQR tidak berubah** ✅  
  <sub>Benar: Mean 105/11 = 9,55 menjadi 6,5 (turun 3,05). Median 7 menjadi 6,5. Q1 = 5 dan Q3 = 8 sebelum dan sesudah sehingga IQR tetap 3.</sub>
- B. Rata-rata turun lebih dari 3 juta, median tetap 7 juta, dan IQR tidak berubah  
  <sub>Salah: mengira median sama sekali tidak terpengaruh pembuangan data</sub>
- C. Rata-rata turun lebih dari 3 juta, median turun 0,5 juta, dan IQR berubah dari 3 menjadi 2  
  <sub>Salah: mengira IQR ikut menyusut karena pencilan dibuang</sub>
- D. Rata-rata turun kurang dari 1 juta, median turun 0,5 juta, dan IQR tidak berubah  
  <sub>Salah: meremehkan pengaruh pencilan terhadap rata-rata</sub>

**Pembahasan:** Pencilan paling memengaruhi rata-rata; median bergeser sedikit; kuartil tetap sehingga IQR 3 tidak berubah.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas10-b06-c-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: temukan kesalahan menentukan Q3*

Seorang siswa mengerjakan data 12 nilai berikut: 12, 15, 15, 18, 20, 22, 25, 27, 30, 31, 35, 60.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Langkah 1: data sudah terurut dan n = 12.
Langkah 2: n/4 = 3 (bulat), sehingga Q1 = rata-rata data ke-3 dan ke-4 = 16,5.
Langkah 3: 3n/4 = 9, sehingga Q3 = data ke-9 = 30.
Langkah 4: IQR = 30 - 16,5 = 13,5; batas atas = 30 + 1,5 x 13,5 = 50,25; jadi 60 adalah pencilan.

Langkah pertama yang mengandung kesalahan dan batas atas pencilan yang benar adalah ....

- A. Langkah 2; Q1 seharusnya 15 sehingga batas atas yang benar 53,75  
  <sub>Salah: mengira Q1 cukup data ke-3 padahal n/4 bulat berarti dirata-rata</sub>
- B. Langkah 3; Q3 seharusnya 31 sehingga batas atas yang benar 52,75  
  <sub>Salah: mengambil data ke-(m + 1) saja, bukan rata-rata dua data</sub>
- **C. Langkah 3; Q3 seharusnya 30,5 sehingga batas atas yang benar 51,5** ✅  
  <sub>Benar: Karena 3n/4 = 9 bulat, Q3 = (data ke-9 + data ke-10)/2 = (30 + 31)/2 = 30,5. IQR = 14, batas atas = 30,5 + 21 = 51,5.</sub>
- D. Langkah 4; batas atas seharusnya Q3 + IQR = 43,5  
  <sub>Salah: mengira faktor 1,5 tidak dipakai, padahal langkah 3 yang keliru</sub>

**Pembahasan:** Kesalahan pertama pada langkah 3 (Q3 tidak dirata-rata). Q3 = 30,5, IQR = 14, batas atas = 51,5; 60 tetap pencilan.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas10-b06-c-hard-bt01-004
*orisinal | C6 | 6 langkah | jenis: rancang data memenuhi lima ukuran dan satu pencilan*

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Sebuah kumpulan 9 bilangan bulat terurut harus memenuhi: minimum 10, Q1 = 14, median = 20, Q3 = 26, maksimum 60, dan tepat satu data yang tergolong pencilan.

Kumpulan data yang memenuhi semua syarat itu adalah ....

- **A. 10, 12, 14, 17, 20, 23, 26, 31, 60** ✅  
  <sub>Benar: Q1 = data ke-3 = 14, median = data ke-5 = 20, Q3 = data ke-7 = 26; IQR = 12, batas atas = 44 sehingga hanya 60 yang pencilan (31 < 44).</sub>
- B. 10, 12, 14, 17, 20, 23, 26, 48, 60  
  <sub>Salah: data 48 dan 60 sama-sama melebihi batas atas 44 sehingga ada dua pencilan</sub>
- C. 10, 12, 14, 17, 20, 23, 28, 31, 60  
  <sub>Salah: Q3 (data ke-7) bernilai 28, bukan 26</sub>
- D. 10, 12, 14, 17, 21, 23, 26, 31, 60  
  <sub>Salah: median (data ke-5) bernilai 21, bukan 20</sub>

**Pembahasan:** Periksa tiap syarat dengan aturan letak kuartil untuk n = 9: Q1 = data ke-3, median data ke-5, Q3 data ke-7.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas10-b06-c-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: bandingkan dua sebaran lewat lima ukuran*

Nilai ulangan dua kelas yang masing-masing terdiri dari 40 siswa diringkas sebagai berikut.

|Ukuran|Kelas A|Kelas B|
|---|---|---|
|Minimum|40|45|
|Q1|55|65|
|Median|62|72|
|Q3|70|85|
|Maksimum|95|90|

Pada tiap kelas, 25% data terletak di bawah Q1, 25% di antara Q1 dan median, 25% di antara median dan Q3, dan 25% di atas Q3.

Pernyataan yang benar berdasarkan ringkasan itu adalah ....

- A. Lebih dari 25% siswa kelas A mendapat nilai di atas 90 (nilai tertinggi kelas B)  
  <sub>Salah: mengira nilai tertinggi A yang besar berarti banyak siswa A di atas 90; padahal paling banyak 25% data A di atas Q3 = 70</sub>
- **B. Paling sedikit 75% siswa kelas B mendapat nilai di atas median kelas A** ✅  
  <sub>Benar: Q1 kelas B = 65 > median kelas A = 62; paling sedikit 75% siswa B bernilai minimal Q1 B sehingga di atas 62.</sub>
- C. Median kelas B lebih rendah daripada Q3 kelas A  
  <sub>Salah: membandingkan 72 dengan 70 secara terbalik; 72 > 70</sub>
- D. Sebaran 50% nilai tengah kelas B lebih sempit daripada kelas A  
  <sub>Salah: IQR B = 20 lebih besar dari IQR A = 15; membalik arah perbandingan</sub>

**Pembahasan:** IQR A = 15, IQR B = 20; median B 72 > Q3 A 70; paling banyak 25% data A di atas 70 sehingga tidak mungkin lebih dari 25% di atas 90; Q1 B = 65 > median A = 62 sehingga klaim pertama benar.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas10-b06-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi pemilihan representasi*

Sebuah tim peneliti sekolah memilih diagram untuk empat tujuan. Pilihan dibatasi pada diagram pencar (untuk pasangan dua variabel) dan diagram kotak garis (untuk sebaran satu variabel):

(a) Melihat apakah makin lama jam belajar siswa makin tinggi nilainya, dengan tiap siswa dicatat jam belajar dan nilainya: diagram pencar.
(b) Membandingkan sebaran uang saku siswa kelas X dan kelas XI (satu variabel, dua kelompok): diagram pencar.
(c) Memeriksa apakah ada tagihan listrik yang tergolong pencilan pada satu kumpulan data tagihan: diagram kotak garis.
(d) Mencari satu pasangan data (tinggi, berat) yang menyimpang dari pola hubungan seluruh pasangan lain: diagram kotak garis.

Penilaian yang tepat terhadap keempat pilihan itu adalah ....

- A. Pilihan (a) dan (c) keliru, sedangkan (b) dan (d) sudah tepat  
  <sub>Salah: membalik semua penilaian</sub>
- B. Hanya pilihan (d) yang keliru  
  <sub>Salah: tidak memeriksa (b): sebaran satu variabel dua kelompok cocok dengan diagram kotak garis</sub>
- C. Hanya pilihan (b) yang keliru  
  <sub>Salah: tidak memeriksa (d): titik menyimpang dari pola hubungan terlihat di diagram pencar</sub>
- **D. Pilihan (b) dan (d) keliru, sedangkan (a) dan (c) sudah tepat** ✅  
  <sub>Benar: Pasangan dua variabel dan titik yang menyimpang dari pola hubungan membutuhkan diagram pencar; sebaran satu variabel, perbandingan kelompok, dan pencilan memakai diagram kotak garis. Maka (b) dan (d) tertukar.</sub>

**Pembahasan:** (a) pencar tepat, (b) seharusnya kotak garis, (c) kotak garis tepat, (d) seharusnya pencar.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b06-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: evaluasi dampak titik menyimpang pada korelasi*

Sepuluh pasangan data (x, y) dicatat sebagai berikut.

|x|y|
|---|---|
|1|3|
|2|5|
|3|7|
|4|9|
|5|11|
|6|13|
|7|15|
|8|17|
|9|19|
|10|3|

Pernyataan yang paling tepat tentang diagram pencar data itu adalah ....

- A. Sembilan titik pertama segaris naik; titik (10, 3) pasti salah catat sehingga harus dibuang  
  <sub>Salah: menganggap titik menyimpang otomatis salah catat tanpa dasar</sub>
- B. Sembilan titik pertama segaris naik; titik (10, 3) membalik arah korelasi menjadi negatif  
  <sub>Salah: mengira satu titik di bawah garis membalik arah korelasi</sub>
- C. Sembilan titik pertama segaris naik; titik (10, 3) menghapus korelasi sehingga x dan y tidak berkorelasi  
  <sub>Salah: mengira satu titik menyimpang menghapus seluruh pola naik</sub>
- **D. Sembilan titik pertama segaris naik; titik (10, 3) melemahkan korelasi tetapi arahnya tetap positif** ✅  
  <sub>Benar: Untuk x = 1 sampai 9, y = 2x + 1 (garis naik sempurna). Titik (10, 3) jauh di bawah pola itu sehingga memperlemah pola, namun kecenderungan keseluruhan masih naik (r positif).</sub>

**Pembahasan:** Sembilan titik naik, satu titik menyimpang melemahkan tetapi tidak membalik arah.
**Acuan:** siswa — siswa hal.233

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b06-c-hard-bt01-008
*orisinal | C5 | 6 langkah | jenis: rancang data tambahan agar muncul pencilan*

Data waktu tunggu (menit) 10 pelanggan: 21, 22, 24, 25, 27, 28, 30, 31, 33, 35.

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Dua pelanggan baru ditambahkan, keduanya dengan waktu tunggu v menit (v bilangan bulat, lebih besar dari 35). Nilai v terkecil sehingga data v tergolong pencilan pada kumpulan 12 data yang baru adalah ....

- A. 46  
  <sub>Salah: memakai Q3 = data ke-9 = 33 saja (tanpa rata-rata dengan data ke-10) sehingga batas 45,75</sub>
- **B. 49** ✅  
  <sub>Benar: Dengan 12 data: Q1 = (24 + 25)/2 = 24,5; Q3 = (33 + 35)/2 = 34; IQR = 9,5; batas atas = 34 + 14,25 = 48,25 sehingga v terkecil = 49.</sub>
- C. 42  
  <sub>Salah: memakai batas atas dari 10 data semula (Q3 = 31, IQR = 7, batas 41,5) padahal n berubah</sub>
- D. 48  
  <sub>Salah: membulatkan batas atas 48,25 ke bawah padahal data harus lebih dari 48,25</sub>

**Pembahasan:** Setelah penambahan n = 12, kuartil dihitung ulang. Batas atas 48,25, jadi v = 49 adalah bilangan bulat terkecil yang melebihi batas.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b06-c-hard-bt01-009
*orisinal | C5 | 6 langkah | jenis: pencilan relatif terhadap sebaran kelompok*

Nilai ujian 12 siswa kelas A dan 12 siswa kelas B (terurut).
Kelas A: 52, 70, 72, 73, 74, 75, 76, 77, 78, 80, 81, 83
Kelas B: 52, 60, 66, 72, 75, 79, 82, 85, 88, 91, 94, 97

Aturan letak kuartil: dengan n data terurut, hitung n/4 untuk Q1, n/2 untuk Q2, dan 3n/4 untuk Q3. Jika hasilnya bilangan bulat m, kuartil = rata-rata data ke-m dan ke-(m + 1); jika tidak bulat, bulatkan ke atas lalu ambil data pada urutan itu. Pencilan: data kurang dari Q1 - 1,5 x IQR atau lebih dari Q3 + 1,5 x IQR.

Seorang siswa di tiap kelas memperoleh nilai 52. Pernyataan yang benar mengenai nilai 52 itu, beserta batas bawah pencilan tiap kelas, adalah ....

- **A. Pencilan di kelas A (batas bawah 62,75), bukan pencilan di kelas B (batas bawah 38,25)** ✅  
  <sub>Benar: A: Q1 = 72,5, Q3 = 79, IQR = 6,5, batas bawah = 62,75 > 52. B: Q1 = 69, Q3 = 89,5, IQR = 20,5, batas bawah = 38,25 < 52.</sub>
- B. Pencilan di kedua kelas, karena 52 lebih kecil dari Q1 kedua kelas (72,5 dan 69)  
  <sub>Salah: membandingkan dengan Q1, bukan dengan Q1 - 1,5 x IQR</sub>
- C. Pencilan di kelas B (batas bawah 62,75), bukan pencilan di kelas A (batas bawah 38,25)  
  <sub>Salah: menukar batas bawah kedua kelas</sub>
- D. Bukan pencilan di kedua kelas (batas bawah 26 dan 1,5)  
  <sub>Salah: memakai jangkauan sebagai pengganti IQR dalam batas pencilan</sub>

**Pembahasan:** Batas bawah bergantung pada IQR tiap kelas: kelas A rapat sehingga 52 pencilan; kelas B menyebar lebar sehingga 52 wajar.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b06-c-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: evaluasi kesimpulan korelasi gabungan dua kelompok*

Tabel berikut memuat lama belajar per pekan (jam) dan nilai ujian 8 siswa dari dua kelompok kemampuan yang berbeda.

|Jam belajar|Nilai|Kelompok|
|---|---|---|
|1|80|Kelompok I|
|2|82|Kelompok I|
|3|84|Kelompok I|
|4|86|Kelompok I|
|6|40|Kelompok II|
|7|42|Kelompok II|
|8|44|Kelompok II|
|9|46|Kelompok II|

Pernyataan yang paling tepat tentang korelasi pada data itu adalah ....

- A. Korelasi seluruh data negatif, sehingga terbukti belajar lebih lama menurunkan nilai  
  <sub>Salah: menyimpulkan sebab-akibat dari korelasi gabungan</sub>
- **B. Korelasi seluruh data negatif, tetapi di dalam tiap kelompok positif; kesimpulan "belajar lebih lama menurunkan nilai" tidak dibenarkan** ✅  
  <sub>Benar: Kelompok I: naik 2 nilai tiap jam, positif. Kelompok II: sama, positif. Gabungan: jam belajar lebih besar berada di kelompok bernilai lebih rendah, sehingga keseluruhan menurun (negatif). Perbedaan kelompok, bukan lama belajar, yang menjelaskan nilai.</sub>
- C. Korelasi seluruh data positif karena di dalam tiap kelompok positif  
  <sub>Salah: mengira korelasi gabungan pasti mengikuti korelasi tiap kelompok</sub>
- D. Di dalam tiap kelompok korelasinya negatif, sama seperti seluruh data  
  <sub>Salah: salah membaca pola per kelompok</sub>

**Pembahasan:** Dua kelompok punya pola naik sendiri-sendiri, tetapi menggabungkannya membalik arah korelasi.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
