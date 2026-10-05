# Lembar koreksi — kelas12 SMA12U-B2 subbab E: Pinjaman dengan Anuitas

60 soal | easy 20, medium 20, hard 20 | variasi 21, orisinal 39

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b02-e-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: angsuran pokok bulan ke-n*

Bu Sari meminjam uang di bank sebesar Rp30.000.000,00 dengan bunga 24% per tahun (2% per bulan). Ia membayar pinjaman tersebut dengan anuitas sebesar Rp1.200.000,00 per bulan. Anuitas dibayar pada akhir tiap bulan dan bunga dihitung dari sisa pinjaman. Berapakah besar angsuran pinjaman pokok yang dibayarkan Bu Sari pada anuitas bulan ke-3?

- A. Rp636.725,00  
  <sub>Salah: memakai pangkat n = 3, bukan n - 1 = 2</sub>
- B. Rp1.248.480,00  
  <sub>Salah: lupa mengurangkan bunga Mi: memakai A x (1+i)^(n-1)</sub>
- C. Rp600.000,00  
  <sub>Salah: hanya menghitung angsuran pokok bulan pertama (A - Mi), lupa faktor (1+i)^(n-1)</sub>
- **D. Rp624.240,00** ✅  
  <sub>Benar: a_3 = (1.200.000 - 0,02 x 30.000.000) x (1,02)^2 = 600.000 x 1,0404 = 624.240</sub>

**Pembahasan:** Bunga 2% per bulan. a_3 = (A - Mi)(1+i)^(n-1) = (1.200.000 - 600.000) x 1,02^2 = 624.240.
**Acuan:** siswa — siswa hal.83 Contoh 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b02-e-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: angsuran pokok bulan ke-n*

Pak Dedi mengambil kredit renovasi rumah sebesar Rp40.000.000,00 dengan bunga 12% per tahun (1% per bulan). Kredit itu dilunasi dengan anuitas tetap Rp1.800.000,00 setiap bulan. Anuitas dibayar pada akhir tiap bulan dan bunga dihitung dari sisa pinjaman. Berapakah bagian angsuran pokok yang termuat dalam pembayaran anuitas bulan kedua?

- A. Rp1.386.000,00  
  <sub>Salah: mengalikan dengan (1 - i), bukan (1 + i)</sub>
- **B. Rp1.414.000,00** ✅  
  <sub>Benar: a_2 = (1.800.000 - 400.000) x 1,01 = 1.414.000</sub>
- C. Rp1.428.140,00  
  <sub>Salah: memakai pangkat n = 2 (1,01^2), bukan n - 1 = 1</sub>
- D. Rp1.400.000,00  
  <sub>Salah: angsuran pokok bulan pertama, lupa dikalikan (1+i)</sub>

**Pembahasan:** a_1 = 1.800.000 - 0,01 x 40.000.000 = 1.400.000. Angsuran pokok naik dengan faktor 1,01: a_2 = 1.414.000.
**Acuan:** siswa — siswa hal.83 Contoh 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b02-e-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: sisa pinjaman setelah anuitas ke-n*

Bu Tini meminjam uang di bank sebesar Rp20.000.000,00 dengan bunga 12% per tahun. Ia membayar pinjaman tersebut dengan anuitas sebesar Rp1.000.000,00 per bulan. Anuitas dibayar pada akhir tiap bulan dan bunga dihitung dari sisa pinjaman. Berapakah sisa pinjaman Bu Tini setelah anuitas bulan ke-3 dibayarkan?

- **A. Rp17.575.920,00** ✅  
  <sub>Benar: S_3 = 800.000 x (1,01^3 - 1)/0,01 = 2.424.080; sisa = 20.000.000 - 2.424.080 = 17.575.920</sub>
- B. Rp17.600.000,00  
  <sub>Salah: menganggap angsuran pokok tiga bulan sama dengan bulan pertama (3 x 800.000)</sub>
- C. Rp17.000.000,00  
  <sub>Salah: mengurangkan seluruh anuitas (3 x 1.000.000) dari pinjaman, padahal sebagian anuitas adalah bunga</sub>
- D. Rp2.424.080,00  
  <sub>Salah: hanya memberi jumlah angsuran pokok S_3, lupa mengurangkan dari pinjaman</sub>

**Pembahasan:** a_1 = 1.000.000 - 200.000 = 800.000, r = 1,01. S_3 = 800.000 x (1,01^3 - 1)/0,01 = 2.424.080. Sisa = 17.575.920.
**Acuan:** siswa — siswa hal.84 Contoh 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b02-e-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: jumlah angsuran pokok hingga bulan ke-n*

Rina memperoleh pinjaman usaha sebesar Rp60.000.000,00 dengan bunga 24% per tahun (2% per bulan). Pinjaman dicicil dengan anuitas tetap Rp2.500.000,00 per bulan. Anuitas dibayar pada akhir tiap bulan dan bunga dihitung dari sisa pinjaman. Berapakah jumlah angsuran pokok yang telah terbayar hingga anuitas bulan ke-2?

- A. Rp1.300.000,00  
  <sub>Salah: hanya menghitung angsuran pokok bulan pertama</sub>
- **B. Rp2.626.000,00** ✅  
  <sub>Benar: a_1 = 1.300.000, a_2 = 1.326.000, jumlah = 2.626.000</sub>
- C. Rp2.600.000,00  
  <sub>Salah: menganggap angsuran pokok bulan kedua sama dengan bulan pertama (2 x 1.300.000)</sub>
- D. Rp2.652.000,00  
  <sub>Salah: mengalikan 2 x a_1 x (1+i), bukan menjumlahkan a_1 dan a_2</sub>

**Pembahasan:** a_1 = 2.500.000 - 0,02 x 60.000.000 = 1.300.000; a_2 = 1.300.000 x 1,02 = 1.326.000; jumlah 2.626.000.
**Acuan:** siswa — siswa hal.84 Contoh 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b02-e-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: pinjaman awal dari anuitas*

Seseorang meminjam uang di bank dengan bunga 2% per bulan dan melunasinya dengan sistem anuitas. Jika ia harus membayar Rp1.040.400,00 pada akhir setiap bulan selama 2 bulan, maka jumlah pinjaman awal yang diberikan oleh bank adalah ....

- A. Rp1.020.000,00  
  <sub>Salah: hanya memakai nilai sekarang anuitas pertama</sub>
- **B. Rp2.020.000,00** ✅  
  <sub>Benar: M = 1.040.400 x (1 - 1,02^-2)/0,02 = 1.020.000 + 1.000.000 = 2.020.000</sub>
- C. Rp2.080.800,00  
  <sub>Salah: menjumlahkan dua anuitas tanpa mendiskontokan bunga</sub>
- D. Rp2.040.000,00  
  <sub>Salah: mendiskontokan jumlah dua anuitas hanya satu periode</sub>

**Pembahasan:** M = A[1 - (1+i)^-n]/i = 1.040.400 x (1 - 1,02^-2)/0,02 = 2.020.000.
**Acuan:** siswa — siswa hal.85 Contoh 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b02-e-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: pinjaman awal dari anuitas*

Koperasi tani memberi pinjaman kepada Bu Ratna dengan bunga 10% per tahun. Bu Ratna melunasinya dengan sistem anuitas sebesar Rp1.210.000,00 pada akhir setiap tahun selama 2 tahun. Besar pinjaman yang diterima Bu Ratna adalah ....

- A. Rp1.100.000,00  
  <sub>Salah: hanya memakai nilai sekarang anuitas tahun pertama</sub>
- **B. Rp2.100.000,00** ✅  
  <sub>Benar: M = 1.210.000/1,1 + 1.210.000/1,21 = 1.100.000 + 1.000.000 = 2.100.000</sub>
- C. Rp2.420.000,00  
  <sub>Salah: menjumlahkan dua anuitas tanpa diskonto bunga</sub>
- D. Rp2.200.000,00  
  <sub>Salah: mendiskontokan total dua anuitas hanya satu periode</sub>

**Pembahasan:** M = A[1 - (1+i)^-n]/i = 1.210.000 x (1 - 1,1^-2)/0,1 = 2.100.000.
**Acuan:** siswa — siswa hal.85 Contoh 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b02-e-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: besar anuitas (periode semesteran)*

Pak Hari membeli sebuah mesin jahit seharga Rp4.120.000,00 secara kredit dengan sistem anuitas dan suku bunga 12% per tahun. Ia berencana melunasinya dengan 2 kali anuitas yang dibayarkan pada akhir setiap enam bulan (bunga 6% per semester). Besar anuitas yang harus dibayarkan Pak Hari adalah ....

- **A. Rp2.247.200,00** ✅  
  <sub>Benar: A = 4.120.000 x 0,06/(1 - 1,06^-2) = 2.247.200</sub>
- B. Rp2.183.600,00  
  <sub>Salah: menambahkan bunga satu periode lalu membagi dua (M(1+i)/2)</sub>
- C. Rp2.060.000,00  
  <sub>Salah: membagi pinjaman 2 sama rata tanpa bunga</sub>
- D. Rp2.437.796,00  
  <sub>Salah: memakai 12% per semester (tidak mengonversi bunga tahunan ke semester)</sub>

**Pembahasan:** i = 6% per semester, n = 2. A = M i /(1 - (1+i)^-n) = 4.120.000 x 0,06/(1 - 1,06^-2) = 2.247.200.
**Acuan:** siswa — siswa hal.85 Contoh 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b02-e-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: besar anuitas (periode bulanan)*

Sebuah toko menjual kulkas seharga Rp4.030.000,00 dengan kredit sistem anuitas berbunga 18% per tahun (1,5% per bulan). Pembeli melunasinya dengan 2 kali anuitas yang dibayarkan pada akhir tiap bulan. Besar anuitas per bulan adalah ....

- A. Rp2.574.024,00  
  <sub>Salah: memakai 18% per bulan (bunga tahunan tidak dikonversi ke bulan)</sub>
- B. Rp2.045.225,00  
  <sub>Salah: menambah bunga satu bulan lalu membagi dua (M(1+i)/2)</sub>
- **C. Rp2.060.450,00** ✅  
  <sub>Benar: A = 4.030.000 x 0,015/(1 - 1,015^-2) = 2.060.450</sub>
- D. Rp2.015.000,00  
  <sub>Salah: membagi harga 2 sama rata, tanpa bunga</sub>

**Pembahasan:** i = 1,5% per bulan, n = 2. A = M i/(1 - (1+i)^-n) = 2.060.450.
**Acuan:** siswa — siswa hal.85 Contoh 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b02-e-easy-bt01-009
*variasi (angka) | C2 | 1 langkah | jenis: anuitas dari tabel rencana angsuran*

Seseorang meminjam uang sebesar Rp12.000.000,00 dengan bunga 3% per bulan dan melunasinya dengan anuitas tetap setiap bulan. Berikut tabel rencana angsuran untuk 3 bulan pertama.

| Bulan | Pinjaman Awal Bulan (Rp) | Bunga (Rp) | Angsuran (Rp) | Pinjaman Akhir Bulan (Rp) |
|---|---|---|---|---|
| 1 | 12.000.000 | 360.000 | 1.640.000 | 10.360.000 |
| 2 | 10.360.000 | 310.800 | 1.689.200 | 8.670.800 |
| 3 | 8.670.800 | 260.124 | 1.739.876 | 6.930.924 |

Besar anuitas pada sistem angsuran tersebut adalah ....

- A. Rp1.640.000,00  
  <sub>Salah: hanya mengambil angsuran bulan pertama tanpa bunga</sub>
- B. Rp2.049.200,00  
  <sub>Salah: menjumlahkan bunga bulan 1 dengan angsuran bulan 2 (baris tertukar)</sub>
- C. Rp1.950.800,00  
  <sub>Salah: menjumlahkan bunga bulan 2 dengan angsuran bulan 1 (baris tertukar)</sub>
- **D. Rp2.000.000,00** ✅  
  <sub>Benar: anuitas = bunga + angsuran dalam satu bulan = 360.000 + 1.640.000 = 2.000.000</sub>

**Pembahasan:** A = a + b. Bulan 1: 360.000 + 1.640.000 = 2.000.000 (sama tiap bulan).
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b02-e-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: anuitas dari tabel rencana angsuran*

Bu Wulan mengambil kredit modal warung sebesar Rp8.000.000,00 dengan bunga 2% per bulan. Setiap bulan ia membayar anuitas yang jumlahnya sama. Rencana pelunasan untuk dua bulan pertama sebagai berikut.

| Bulan | Sisa Utang Awal (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Sisa Utang Akhir (Rp) |
|---|---|---|---|---|
| 1 | 8.000.000 | 160.000 | 1.940.000 | 6.060.000 |
| 2 | 6.060.000 | 121.200 | 1.978.800 | 4.081.200 |

Pembayaran tetap (anuitas) yang harus dibayar Bu Wulan tiap bulan adalah ....

- A. Rp2.061.200,00  
  <sub>Salah: menjumlahkan bunga bulan 2 dengan angsuran pokok bulan 1 (baris tertukar)</sub>
- B. Rp2.138.800,00  
  <sub>Salah: menjumlahkan bunga bulan 1 dengan angsuran pokok bulan 2 (baris tertukar)</sub>
- C. Rp1.940.000,00  
  <sub>Salah: hanya mengambil angsuran pokok tanpa bunga</sub>
- **D. Rp2.100.000,00** ✅  
  <sub>Benar: anuitas = bunga + angsuran pokok = 160.000 + 1.940.000 = 2.100.000</sub>

**Pembahasan:** A = angsuran pokok + bunga = 1.940.000 + 160.000 = 2.100.000.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b02-e-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: pinjaman awal dari anuitas*

Dewi meminjam uang di bank yang menawarkan bunga 3% per bulan. Pinjaman itu dibayar dengan sistem anuitas sebesar Rp1.092.727,00 pada akhir setiap bulan selama 3 bulan. Besar uang yang dipinjam Dewi adalah ....

- A. Rp3.182.700,00  
  <sub>Salah: mendiskontokan total tiga anuitas hanya satu periode</sub>
- B. Rp2.090.900,00  
  <sub>Salah: memakai n = 2, bukan n = 3</sub>
- **C. Rp3.090.900,00** ✅  
  <sub>Benar: M = 1.092.727 x (1 - 1,03^-3)/0,03 = 3.090.900</sub>
- D. Rp3.278.181,00  
  <sub>Salah: menjumlahkan tiga anuitas tanpa diskonto bunga</sub>

**Pembahasan:** M = A[1 - (1+i)^-n]/i dengan i = 0,03 dan n = 3 menghasilkan 3.090.900.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b02-e-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: hubungan anuitas, angsuran, bunga*

Pak Eko melunasi pinjaman dengan anuitas sebesar Rp1.500.000,00 per bulan. Pada pembayaran bulan tertentu, bagian bunganya Rp275.000,00. Besar angsuran pinjaman pokok pada bulan tersebut adalah ....

- A. Rp1.775.000,00  
  <sub>Salah: menjumlahkan anuitas dan bunga</sub>
- B. Rp1.500.000,00  
  <sub>Salah: mengira seluruh anuitas adalah angsuran pokok</sub>
- **C. Rp1.225.000,00** ✅  
  <sub>Benar: a = A - b = 1.500.000 - 275.000 = 1.225.000</sub>
- D. Rp275.000,00  
  <sub>Salah: mengambil bunga saja sebagai angsuran pokok</sub>

**Pembahasan:** A = a + b sehingga a = 1.500.000 - 275.000 = 1.225.000.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b02-e-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: sisa utang setelah angsuran pertama*

Rudi meminjam uang Rp8.000.000,00 dengan bunga 24% per tahun (2% per bulan) dan membayarnya dengan anuitas Rp2.000.000,00 per bulan. Anuitas dibayar pada akhir tiap bulan dan bunga dihitung dari sisa pinjaman. Sisa utang Rudi setelah angsuran pertama dibayarkan adalah ....

- A. Rp5.840.000,00  
  <sub>Salah: mengurangkan anuitas dan bunga sekaligus (bunga dikurangkan dua kali)</sub>
- B. Rp6.000.000,00  
  <sub>Salah: mengurangkan seluruh anuitas dari pinjaman, tidak memisahkan bunga</sub>
- **C. Rp6.160.000,00** ✅  
  <sub>Benar: B_1 = 160.000; a_1 = 2.000.000 - 160.000 = 1.840.000; sisa = 8.000.000 - 1.840.000 = 6.160.000</sub>
- D. Rp7.840.000,00  
  <sub>Salah: mengurangkan hanya bunga dari pinjaman</sub>

**Pembahasan:** Bunga = 2% x 8.000.000 = 160.000. Angsuran pokok = 2.000.000 - 160.000 = 1.840.000. Sisa = 6.160.000.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b02-e-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: pola bunga dan angsuran tiap bulan*

Sebuah pinjaman dilunasi dengan sistem anuitas (pembayaran tiap bulan selalu sama besar). Dari bulan ke bulan, perubahan bunga dan angsuran pokok pada pembayaran tersebut adalah ....

- A. bunga dan angsuran pokok keduanya tetap  
  <sub>Salah: mengira yang tetap adalah tiap komponen, bukan jumlahnya</sub>
- B. bunga semakin kecil dan angsuran pokok tetap  
  <sub>Salah: tertukar dengan sistem angsuran pokok tetap</sub>
- C. bunga semakin besar dan angsuran pokok semakin kecil  
  <sub>Salah: pola terbalik</sub>
- **D. bunga semakin kecil dan angsuran pokok semakin besar** ✅  
  <sub>Benar: sisa pinjaman berkurang sehingga bunga mengecil; karena anuitas tetap, bagian angsuran pokok membesar</sub>

**Pembahasan:** Bunga = i x sisa pinjaman, makin kecil. Anuitas tetap sehingga angsuran pokok = A - bunga makin besar.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b02-e-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: rasio barisan angsuran pokok*

Pada pinjaman dengan sistem anuitas berbunga 2,5% per bulan, angsuran pokok dari bulan ke bulan membentuk barisan geometri. Rasio barisan tersebut adalah ....

- **A. 1,025** ✅  
  <sub>Benar: r = 1 + i = 1 + 0,025 = 1,025</sub>
- B. 0,975  
  <sub>Salah: memakai 1 - i</sub>
- C. 2,5  
  <sub>Salah: memakai persen tanpa dikonversi dan tanpa tambah 1</sub>
- D. 0,025  
  <sub>Salah: memakai i saja sebagai rasio</sub>

**Pembahasan:** Angsuran pokok membentuk barisan geometri dengan rasio r = 1 + i = 1,025.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b02-e-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: anuitas terakhir*

Pak Agus melunasi pinjaman dengan anuitas Rp1.000.000,00 per bulan berbunga 2% per bulan. Pada awal bulan pembayaran terakhir, sisa pinjamannya Rp500.000,00 dan seluruhnya lunas pada pembayaran itu. Besar anuitas terakhir yang dibayarkan adalah ....

- **A. Rp510.000,00** ✅  
  <sub>Benar: anuitas terakhir = sisa pinjaman + bunga = 500.000 + 0,02 x 500.000 = 510.000</sub>
- B. Rp1.000.000,00  
  <sub>Salah: mengira anuitas terakhir selalu sama dengan anuitas sebelumnya</sub>
- C. Rp490.000,00  
  <sub>Salah: mengurangkan bunga dari sisa pinjaman, bukan menambahkan</sub>
- D. Rp500.000,00  
  <sub>Salah: hanya membayar sisa pinjaman, lupa bunga</sub>

**Pembahasan:** Pembayaran terakhir = 500.000 + 2% x 500.000 = 510.000.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b02-e-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: sisa pinjaman dari jumlah angsuran pokok*

Bu Lina meminjam Rp25.000.000,00 dan melunasinya dengan anuitas Rp1.200.000,00 per bulan. Jumlah angsuran pokok yang telah dibayarkan hingga anuitas bulan ke-6 adalah Rp5.800.000,00. Sisa pinjaman Bu Lina setelah anuitas bulan ke-6 adalah ....

- **A. Rp19.200.000,00** ✅  
  <sub>Benar: sisa = M - S_6 = 25.000.000 - 5.800.000 = 19.200.000</sub>
- B. Rp17.800.000,00  
  <sub>Salah: mengurangkan 6 x anuitas (termasuk bunga) dari pinjaman</sub>
- C. Rp30.800.000,00  
  <sub>Salah: menjumlahkan pinjaman dan angsuran pokok</sub>
- D. Rp5.800.000,00  
  <sub>Salah: menjawab jumlah angsuran pokok, bukan sisa pinjaman</sub>

**Pembahasan:** Sisa pinjaman = M - S_n = 25.000.000 - 5.800.000 = 19.200.000. Bunga tidak mengurangi pokok.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b02-e-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: konsep pinjaman awal sebagai nilai sekarang*

Menghitung besar pinjaman awal pada pinjaman dengan anuitas memakai prosedur yang sama dengan menghitung ....

- A. jumlah tak hingga deret geometri  
  <sub>Salah: mengacaukan dengan deret geometri tak hingga</sub>
- **B. nilai sekarang (present value) anuitas** ✅  
  <sub>Benar: pinjaman awal adalah nilai sekarang dari seluruh anuitas yang akan dibayar</sub>
- C. bunga tunggal dari pinjaman  
  <sub>Salah: mengira pinjaman memakai bunga tunggal</sub>
- D. nilai masa depan (future value) anuitas  
  <sub>Salah: tertukar PV dengan FV</sub>

**Pembahasan:** Besar pinjaman awal M = A[1 - (1+i)^-n]/i adalah rumus nilai sekarang anuitas.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b02-e-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: melanjutkan tabel rencana pelunasan*

Pinjaman Rp6.000.000,00 berbunga 2% per bulan dilunasi dengan anuitas tetap Rp1.500.000,00 per bulan (dibayar akhir bulan). Rencana pelunasan dua bulan pertama:

| Bulan | Pinjaman Awal Bulan (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Pinjaman Akhir Bulan (Rp) |
|---|---|---|---|---|
| 1 | 6.000.000 | 120.000 | 1.380.000 | 4.620.000 |
| 2 | 4.620.000 | 92.400 | 1.407.600 | 3.212.400 |

Besar bunga yang termuat dalam anuitas bulan ketiga adalah ....

- A. Rp92.400,00  
  <sub>Salah: mengulang bunga bulan kedua</sub>
- B. Rp120.000,00  
  <sub>Salah: menghitung bunga dari pinjaman awal 6.000.000</sub>
- **C. Rp64.248,00** ✅  
  <sub>Benar: bunga bulan ke-3 = 2% x sisa akhir bulan ke-2 = 0,02 x 3.212.400 = 64.248</sub>
- D. Rp1.435.752,00  
  <sub>Salah: menjawab angsuran pokok bulan ketiga (1.500.000 - 64.248), bukan bunga</sub>

**Pembahasan:** Bunga bulan ke-3 dihitung dari sisa pinjaman 3.212.400: 0,02 x 3.212.400 = 64.248.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b02-e-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: membandingkan tenor pinjaman*

Sebuah bank menawarkan pinjaman Rp20.000.000,00 dengan bunga 1% per bulan. Tenor 12 bulan menghasilkan anuitas Rp1.776.976,00 per bulan, sedangkan tenor 24 bulan menghasilkan anuitas Rp941.469,00 per bulan. Pernyataan yang benar adalah ....

- A. tenor 24 bulan memberi anuitas lebih besar dan total pembayaran lebih besar  
  <sub>Salah: mengira tenor lebih panjang menaikkan anuitas</sub>
- B. tenor 24 bulan memberi anuitas lebih kecil dan total pembayaran lebih kecil  
  <sub>Salah: mengira anuitas kecil berarti total lebih hemat</sub>
- C. total pembayaran kedua tenor sama karena pinjaman pokoknya sama  
  <sub>Salah: mengabaikan bunga yang bertambah seiring tenor</sub>
- **D. tenor 24 bulan memberi anuitas lebih kecil, tetapi total pembayaran lebih besar** ✅  
  <sub>Benar: 12 x 1776976 = 21323712 sedangkan 24 x 941469 = 22595256; anuitas 24 bulan lebih kecil tetapi totalnya lebih besar</sub>

**Pembahasan:** Total tenor 12 bulan = 21323712; total tenor 24 bulan = 22595256. Anuitas turun, total bayar naik.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b02-e-medium-bt01-001
*variasi (angka) | C4 | 4 langkah | jenis: bunga bulan ke-n dari tabel (pola geometri)*

Seorang pedagang meminjam uang sebesar Rp5.000.000,00 dengan suku bunga 10% per bulan dan melunasinya dengan anuitas tetap setiap bulan (dibayar akhir bulan, bunga dari sisa pinjaman). Berikut tabel rencana angsuran hingga anuitas ke-3.

| Bulan | Pinjaman Awal Bulan (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Pinjaman Akhir Bulan (Rp) |
|---|---|---|---|---|
| 1 | 5.000.000 | 500.000 | 700.000 | 4.300.000 |
| 2 | 4.300.000 | 430.000 | 770.000 | 3.530.000 |
| 3 | 3.530.000 | 353.000 | 847.000 | 2.683.000 |

Besar bunga yang termuat dalam anuitas ke-5 adalah ....

- A. Rp72.643,00  
  <sub>Salah: memakai angsuran pokok bulan ke-6 (pangkat 5)</sub>
- **B. Rp175.130,00** ✅  
  <sub>Benar: A = 500.000 + 700.000 = 1.200.000; a_5 = 700.000 x 1,1^4 = 1.024.870; bunga = 1.200.000 - 1.024.870 = 175.130</sub>
- C. Rp1.024.870,00  
  <sub>Salah: menjawab angsuran pokok bulan ke-5, bukan bunganya</sub>
- D. Rp268.300,00  
  <sub>Salah: memakai angsuran pokok bulan ke-4 (pangkat 3), bukan bulan ke-5</sub>

**Pembahasan:** Anuitas A = bunga + angsuran pokok = 500.000 + 700.000 = 1.200.000. Angsuran pokok membentuk barisan geometri rasio 1,1 (770.000/700.000), a_5 = 700.000 x 1,1^4 = 1.024.870. Bunga = A - a_5 = 175.130.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b02-e-medium-bt01-002
*variasi (konteks) | C4 | 4 langkah | jenis: bunga bulan ke-n dari tabel (pola geometri)*

Bu Mira mengambil kredit usaha Rp4.000.000,00 dengan bunga 5% per bulan. Kredit itu dilunasi dengan anuitas yang jumlahnya sama setiap akhir bulan. Rencana pelunasan tiga bulan pertama:

| Bulan | Sisa Utang Awal (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Sisa Utang Akhir (Rp) |
|---|---|---|---|---|
| 1 | 4.000.000 | 200.000 | 400.000 | 3.600.000 |
| 2 | 3.600.000 | 180.000 | 420.000 | 3.180.000 |
| 3 | 3.180.000 | 159.000 | 441.000 | 2.739.000 |

Bagian bunga dalam pembayaran bulan ke-5 adalah ....

- **A. Rp113.797,50** ✅  
  <sub>Benar: A = 200.000 + 400.000 = 600.000; a_5 = 400.000 x 1,05^4 = 486.202,50; bunga = 600.000 - 486.202,50 = 113.797,50</sub>
- B. Rp136.950,00  
  <sub>Salah: memakai bunga bulan ke-4 (pangkat 3)</sub>
- C. Rp200.000,00  
  <sub>Salah: menjawab bunga bulan pertama</sub>
- D. Rp486.202,50  
  <sub>Salah: menjawab angsuran pokok bulan ke-5, bukan bunganya</sub>

**Pembahasan:** A = 600.000. Rasio angsuran pokok 1,05 (420.000/400.000). a_5 = 400.000 x 1,05^4 = 486.202,50. Bunga bulan ke-5 = 600.000 - 486.202,50 = 113.797,50.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b02-e-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: omzet minimal setelah pinjaman*

Bu Rani memiliki toko bangunan dengan omzet rata-rata Rp110.000.000,00 per bulan. Ia memiliki 6 karyawan dengan gaji Rp5.000.000,00 per orang, serta pengeluaran rutin lain Rp30.000.000,00 per bulan. Pendapatan bersih per bulan adalah omzet dikurangi semua pengeluaran.

Bu Rani mengambil pinjaman Rp60.000.000,00 dengan tenor 12 bulan dan angsuran Rp5.247.089,00 per bulan, lalu membuka cabang baru dengan 4 karyawan tambahan bergaji Rp5.000.000,00 per orang. Berapa omzet minimal cabang baru per bulan agar pendapatan bersih total menjadi 1,5 kali pendapatan bersih sebelumnya (angsuran ikut menjadi pengeluaran)?

- A. Rp100.247.089,00  
  <sub>Salah: memakai target total 75 juta tanpa mengurangi pendapatan bersih lama</sub>
- B. Rp45.000.000,00  
  <sub>Salah: lupa memasukkan angsuran pinjaman</sub>
- C. Rp25.000.000,00  
  <sub>Salah: hanya memakai tambahan pendapatan bersih, tanpa gaji dan angsuran</sub>
- **D. Rp50.247.089,00** ✅  
  <sub>Benar: bersih lama 50 juta; target 75 juta; tambahan 25 juta; omzet baru = 25.000.000 + 20.000.000 + 5.247.089 = 50.247.089</sub>

**Pembahasan:** Bersih lama = 110 - (30 + 30) = 50 juta. Target 1,5 kali = 75 juta, jadi tambahan bersih 25 juta. Beban baru = gaji 4 x 5 juta = 20 juta ditambah angsuran 5.247.089. Omzet minimal = 25.000.000 + 20.000.000 + 5.247.089 = 50.247.089.
**Acuan:** pretest — kelas12-b02-p0098-uji-kompetensi-10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b02-e-medium-bt01-004
*variasi (konteks) | C4 | 4 langkah | jenis: omzet minimal setelah pinjaman*

Pak Bima mengelola bengkel motor yang beromzet Rp90.000.000,00 per bulan. Bengkel itu mempekerjakan 6 mekanik yang masing-masing digaji Rp3.500.000,00 per bulan, dan biaya operasional lainnya Rp19.000.000,00 per bulan. Pendapatan bersih per bulan adalah omzet dikurangi semua pengeluaran.

Untuk membuka bengkel kedua, Pak Bima meminjam Rp40.000.000,00 dengan tenor 24 bulan dan angsuran Rp1.827.390,00 per bulan, serta menambah 3 mekanik dengan gaji yang sama. Berapa omzet minimal bengkel kedua per bulan agar pendapatan bersih total Pak Bima menjadi dua kali lipat dari sebelumnya (angsuran ikut menjadi pengeluaran)?

- A. Rp50.000.000,00  
  <sub>Salah: hanya memakai tambahan pendapatan bersih</sub>
- B. Rp60.500.000,00  
  <sub>Salah: lupa memasukkan angsuran pinjaman</sub>
- C. Rp112.327.390,00  
  <sub>Salah: memakai target total 100 juta tanpa mengurangi pendapatan bersih lama</sub>
- **D. Rp62.327.390,00** ✅  
  <sub>Benar: bersih lama 50 juta; target 100 juta; tambahan 50 juta; omzet = 50.000.000 + 10.500.000 + 1.827.390 = 62.327.390</sub>

**Pembahasan:** Bersih lama = 90 - (21 + 19) = 50 juta. Target 2 kali = 100 juta sehingga tambahan 50 juta. Beban baru = 3 x 3,5 juta = 10,5 juta ditambah angsuran 1.827.390. Omzet minimal = 62.327.390.
**Acuan:** pretest — kelas12-b02-p0098-uji-kompetensi-10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b02-e-medium-bt01-005
*variasi (konteks) | C4 | 4 langkah | jenis: kemampuan angsuran terhadap pendapatan bersih*

Pak Hendra memiliki toko dengan omzet Rp70.000.000,00 per bulan, 5 karyawan bergaji Rp3.000.000,00 per orang, dan pengeluaran rutin lain Rp15.000.000,00 per bulan. Ia ingin mengajukan kredit ke bank dan membatasi angsuran per bulan: tidak lebih dari 20% pendapatan bersih bila tenor 12 bulan, dan tidak lebih dari 10% pendapatan bersih bila tenor lebih dari 12 bulan. Cuplikan brosur bank (angsuran per bulan):

| Pinjaman | 12 bulan | 24 bulan |
|---|---|---|
| Rp80.000.000,00 | Rp6.996.118,00 | Rp3.654.780,00 |
| Rp100.000.000,00 | Rp8.745.148,00 | Rp4.568.474,00 |
| Rp130.000.000,00 | Rp11.368.693,00 | Rp5.939.017,00 |

Pernyataan yang BENAR mengenai kemampuan angsuran Pak Hendra adalah ....

- A. Pinjaman Rp130.000.000,00 dengan tenor 24 bulan memenuhi batas.  
  <sub>Salah: 5.939.017 melebihi batas 10% (4.000.000)</sub>
- B. Pinjaman Rp100.000.000,00 dengan tenor 24 bulan memenuhi batas.  
  <sub>Salah: 4.568.474 melebihi batas 10% (4.000.000); salah memakai batas 20%</sub>
- **C. Pinjaman Rp80.000.000,00 dengan tenor 12 bulan memenuhi batas.** ✅  
  <sub>Benar: bersih 40 juta; batas 12 bulan 8 juta; 6.996.118 <= 8.000.000 sehingga memenuhi</sub>
- D. Pinjaman Rp100.000.000,00 dengan tenor 12 bulan memenuhi batas.  
  <sub>Salah: 8.745.148 melebihi batas 20% (8.000.000)</sub>

**Pembahasan:** Pendapatan bersih = 70 - (15 + 15) = 40 juta. Batas tenor 12 bulan = 8 juta, tenor lebih dari 12 bulan = 4 juta. Hanya Rp80 juta/12 bulan (6.996.118) yang tidak melebihi batas.
**Acuan:** pretest — kelas12-b02-p0098-uji-kompetensi-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b02-e-medium-bt01-006
*variasi (konteks) | C4 | 4 langkah | jenis: kemampuan angsuran terhadap pendapatan bersih*

Bu Sinta menjalankan usaha katering dengan omzet Rp110.000.000,00 per bulan, 12 pegawai yang masing-masing digaji Rp3.500.000,00, dan biaya bahan serta operasional lain Rp16.000.000,00 per bulan. Bank mensyaratkan angsuran tidak lebih dari 20% pendapatan bersih bulanan untuk tenor 12 bulan, dan tidak lebih dari 10% pendapatan bersih bulanan untuk tenor lebih dari 12 bulan. Simulasi angsuran bank per bulan:

| Pinjaman | 12 bulan | 24 bulan | 36 bulan |
|---|---|---|---|
| Rp130.000.000,00 | Rp11.368.693,00 | Rp5.939.017,00 | Rp4.133.965,00 |
| Rp150.000.000,00 | Rp13.117.722,00 | Rp6.852.711,00 | Rp4.769.959,00 |

Pernyataan manakah yang BENAR mengenai kemampuan angsuran Bu Sinta?

- A. Pinjaman Rp150.000.000,00 dengan tenor 12 bulan.  
  <sub>Salah: 13.117.722 melebihi batas 20% (10.400.000)</sub>
- B. Pinjaman Rp150.000.000,00 dengan tenor 24 bulan.  
  <sub>Salah: 6.852.711 melebihi batas 10% (5.200.000)</sub>
- **C. Pinjaman Rp130.000.000,00 dengan tenor 36 bulan.** ✅  
  <sub>Benar: bersih 52 juta; batas >12 bulan 5,2 juta; 4.133.965 <= 5.200.000 sehingga memenuhi</sub>
- D. Pinjaman Rp130.000.000,00 dengan tenor 24 bulan.  
  <sub>Salah: 5.939.017 melebihi batas 10% (5.200.000)</sub>

**Pembahasan:** Pendapatan bersih = 110 - (42 + 16) = 52 juta. Batas 12 bulan = 10,4 juta; lebih dari 12 bulan = 5,2 juta. Hanya Rp130 juta/36 bulan (4.133.965) yang memenuhi.
**Acuan:** pretest — kelas12-b02-p0098-uji-kompetensi-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b02-e-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: besar anuitas dari harga kredit*

Pak Teguh membeli sebuah mesin cuci dengan sistem anuitas pada pembayaran kreditnya. Harga mesin cuci tersebut adalah Rp4.641.000,00 dengan tingkat suku bunga 20% per tahun. Pak Teguh melunasi kreditnya dengan 4 kali anuitas yang dibayarkan pada akhir setiap enam bulan. Berapakah besar anuitas yang harus dibayarkan Pak Teguh?

- **A. Rp1.464.100,00** ✅  
  <sub>Benar: i = 10% per semester, n = 4; A = 4.641.000 x 0,1/(1 - 1,1^-4) = 1.464.100</sub>
- B. Rp1.792.767,81  
  <sub>Salah: memakai 20% per semester (bunga tahunan tidak dikonversi)</sub>
- C. Rp1.160.250,00  
  <sub>Salah: membagi harga 4 sama rata tanpa bunga</sub>
- D. Rp1.276.275,00  
  <sub>Salah: menambah bunga satu semester lalu membagi 4</sub>

**Pembahasan:** i = 20%/2 = 10% per semester dan n = 4. A = M i /(1 - (1+i)^-n) = 4.641.000 x 0,1/(1 - 1,1^-4) = 1.464.100.
**Acuan:** siswa — siswa hal.85 Contoh 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b02-e-medium-bt01-008
*variasi (angka) | C3 | 4 langkah | jenis: sisa pinjaman setelah anuitas ke-n*

Bu Nia meminjam uang di bank sebesar Rp15.000.000,00 dengan bunga 24% per tahun. Ia membayar pinjaman tersebut dengan anuitas sebesar Rp550.000,00 per bulan (dibayar akhir bulan, bunga dihitung dari sisa pinjaman). Berapakah sisa pinjaman yang masih perlu dibayar setelah pembayaran anuitas bulan ke-4?

- A. Rp12.800.000,00  
  <sub>Salah: mengurangkan 4 x anuitas (termasuk bunga) dari pinjaman</sub>
- **B. Rp13.969.598,00** ✅  
  <sub>Benar: i = 2% per bulan; a_1 = 550.000 - 300.000 = 250.000; S_4 = 250.000 x (1,02^4 - 1)/0,02 = 1.030.402; sisa = 13.969.598</sub>
- C. Rp1.030.402,00  
  <sub>Salah: menjawab jumlah angsuran pokok S_4, bukan sisa pinjaman</sub>
- D. Rp14.000.000,00  
  <sub>Salah: menganggap angsuran pokok empat bulan sama dengan bulan pertama</sub>

**Pembahasan:** Bunga per bulan 24%/12 = 2%. a_1 = 550.000 - 2% x 15.000.000 = 250.000, rasio 1,02. S_4 = 250.000 x (1,02^4 - 1)/0,02 = 1.030.402. Sisa = 15.000.000 - 1.030.402 = 13.969.598.
**Acuan:** siswa — siswa hal.84 Contoh 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b02-e-medium-bt01-009
*variasi (konteks) | C3 | 3 langkah | jenis: besar anuitas dari harga kredit*

Sebuah toko elektronik menjual lemari es seharga Rp1.820.000,00 secara kredit dengan sistem anuitas berbunga 20% per tahun. Pembeli melunasinya dengan 3 kali anuitas yang dibayarkan pada akhir setiap tahun. Besar anuitas per tahun adalah ....

- A. Rp1.048.320,00  
  <sub>Salah: menumbuhkan harga dengan bunga majemuk 3 tahun lalu membagi 3</sub>
- B. Rp364.000,00  
  <sub>Salah: hanya menghitung bunga tahun pertama</sub>
- C. Rp728.000,00  
  <sub>Salah: menambah bunga satu tahun lalu membagi 3</sub>
- **D. Rp864.000,00** ✅  
  <sub>Benar: A = 1.820.000 x 0,2/(1 - 1,2^-3) = 864.000</sub>

**Pembahasan:** i = 20% per tahun, n = 3. A = M i /(1 - (1+i)^-n) = 1.820.000 x 0,2/(1 - 1,2^-3) = 864.000.
**Acuan:** siswa — siswa hal.85 Contoh 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b02-e-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: pinjaman awal dari anuitas*

Seseorang meminjam uang di bank dengan bunga 20% per tahun dan melunasinya dengan sistem anuitas. Jika ia harus membayar kepada pihak bank sebesar Rp1.944.810,00 pada akhir setiap triwulan selama satu tahun, maka berapa jumlah pinjaman awal yang diberikan oleh bank?

- A. Rp1.852.200,00  
  <sub>Salah: hanya memakai nilai sekarang anuitas pertama</sub>
- B. Rp7.408.800,00  
  <sub>Salah: mendiskontokan total empat anuitas hanya satu periode</sub>
- **C. Rp6.896.200,00** ✅  
  <sub>Benar: i = 5% per triwulan, n = 4; M = 1.944.810 x (1 - 1,05^-4)/0,05 = 6.896.200</sub>
- D. Rp7.779.240,00  
  <sub>Salah: menjumlahkan empat anuitas tanpa diskonto bunga</sub>

**Pembahasan:** Bunga per triwulan = 20%/4 = 5%, n = 4. M = A[1 - (1+i)^-n]/i = 1.944.810 x (1 - 1,05^-4)/0,05 = 6.896.200.
**Acuan:** siswa — siswa hal.85 Contoh 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b02-e-medium-bt01-011
*orisinal | C3 | 2 langkah | jenis: total bunga seluruh masa pinjaman*

Pak Joko meminjam Rp3.060.400,00 dengan bunga 2% per bulan. Pinjaman itu lunas tepat dalam 3 kali anuitas sebesar Rp1.061.208,00 yang dibayar pada akhir tiap bulan. Total bunga yang dibayarkan Pak Joko selama 3 bulan adalah ....

- A. Rp183.624,00  
  <sub>Salah: memakai bunga tunggal 3 x 2% dari pinjaman awal</sub>
- B. Rp3.183.624,00  
  <sub>Salah: menjawab total pembayaran, belum dikurangi pinjaman pokok</sub>
- C. Rp61.208,00  
  <sub>Salah: hanya menghitung bunga bulan pertama</sub>
- **D. Rp123.224,00** ✅  
  <sub>Benar: total bayar = 3 x 1.061.208 = 3.183.624; bunga = 3.183.624 - 3.060.400 = 123.224</sub>

**Pembahasan:** Setiap anuitas terdiri atas angsuran pokok dan bunga, sehingga seluruh anuitas dikurangi pinjaman pokok adalah total bunga: 3 x 1.061.208 - 3.060.400 = 123.224.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b02-e-medium-bt01-012
*orisinal | C3 | 4 langkah | jenis: bunga bulan ke-n dari anuitas*

Bu Lastri meminjam Rp25.000.000,00 dengan bunga 24% per tahun dan membayarnya dengan anuitas Rp1.000.000,00 per bulan (dibayar akhir bulan, bunga dihitung dari sisa pinjaman). Bagian bunga yang termuat dalam anuitas bulan ke-4 adalah ....

- **A. Rp469.396,00** ✅  
  <sub>Benar: a_1 = 1.000.000 - 500.000 = 500.000; a_4 = 500.000 x 1,02^3 = 530.604; bunga = 469.396</sub>
- B. Rp500.000,00  
  <sub>Salah: menjawab bunga bulan pertama</sub>
- C. Rp530.604,00  
  <sub>Salah: menjawab angsuran pokok bulan ke-4, bukan bunganya</sub>
- D. Rp458.783,92  
  <sub>Salah: memakai pangkat n = 4 untuk angsuran pokok, bukan n - 1</sub>

**Pembahasan:** Bunga per bulan 2%. a_1 = 500.000, rasio 1,02, a_4 = 500.000 x 1,02^3 = 530.604. Bunga = A - a_4 = 469.396.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b02-e-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: pinjaman awal dari angsuran pokok pertama*

Anuitas suatu pinjaman adalah Rp1.350.000,00 per bulan dengan bunga 1,5% per bulan. Pada pembayaran pertama, angsuran pinjaman pokoknya Rp900.000,00. Besar pinjaman awal adalah ....

- A. Rp60.000.000,00  
  <sub>Salah: membagi angsuran pokok dengan i, bukan bunganya</sub>
- **B. Rp30.000.000,00** ✅  
  <sub>Benar: bunga bulan 1 = 1.350.000 - 900.000 = 450.000 = 1,5% x M sehingga M = 30.000.000</sub>
- C. Rp90.000.000,00  
  <sub>Salah: membagi seluruh anuitas dengan i</sub>
- D. Rp450.000,00  
  <sub>Salah: menjawab bunga bulan pertama sebagai pinjaman awal, lupa membaginya dengan suku bunga</sub>

**Pembahasan:** b_1 = A - a_1 = 450.000. Karena b_1 = i x M, M = 450.000 / 0,015 = 30.000.000.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b02-e-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: melanjutkan tabel rencana pelunasan*

Pinjaman Rp12.000.000,00 berbunga 1% per bulan dilunasi dengan anuitas tetap Rp2.000.000,00 per bulan (dibayar akhir bulan). Rencana pelunasan dua bulan pertama:

| Bulan | Sisa Utang Awal (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Sisa Utang Akhir (Rp) |
|---|---|---|---|---|
| 1 | 12.000.000 | 120.000 | 1.880.000 | 10.120.000 |
| 2 | 10.120.000 | 101.200 | 1.898.800 | 8.221.200 |

Sisa utang pada akhir bulan ke-3 adalah ....

- A. Rp8.138.988,00  
  <sub>Salah: hanya mengurangkan bunga dari sisa utang</sub>
- B. Rp6.221.200,00  
  <sub>Salah: mengurangkan seluruh anuitas dari sisa utang tanpa memisahkan bunga</sub>
- **C. Rp6.303.412,00** ✅  
  <sub>Benar: bunga bulan 3 = 1% x 8.221.200 = 82.212; angsuran pokok = 2.000.000 - 82.212 = 1.917.788; sisa = 8.221.200 - 1.917.788 = 6.303.412</sub>
- D. Rp6.322.400,00  
  <sub>Salah: memakai bunga bulan ke-2 (101.200) untuk bulan ke-3</sub>

**Pembahasan:** Sisa awal bulan 3 = 8.221.200. Bunga = 1% x 8.221.200 = 82.212. Angsuran pokok = 2.000.000 - 82.212 = 1.917.788. Sisa akhir = 8.221.200 - 1.917.788 = 6.303.412.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b02-e-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: tahun pertama angsuran pokok melampaui batas*

Sebuah pinjaman berbunga 10% per tahun dilunasi dengan anuitas yang dibayar pada akhir tiap tahun. Angsuran pokok tahun pertama Rp1.000.000,00 dan angsuran pokok tahun-tahun berikutnya membentuk barisan geometri. Pada tahun ke berapa angsuran pokok untuk pertama kalinya lebih dari Rp1.400.000,00?

- A. 14  
  <sub>Salah: membagi 1.400.000 dengan kenaikan 100.000</sub>
- B. 4  
  <sub>Salah: memakai 1,1^n (bukan n - 1): 1,1^4 sudah melebihi 1,4</sub>
- **C. 5** ✅  
  <sub>Benar: r = 1,1: a_4 = 1.331.000 (belum), a_5 = 1.464.100 (> 1.400.000) sehingga tahun ke-5</sub>
- D. 6  
  <sub>Salah: mengira angsuran bertambah tetap 100.000 per tahun (aritmetika) sehingga baru melebihi di tahun ke-6</sub>

**Pembahasan:** a_n = 1.000.000 x 1,1^(n-1). a_4 = 1.331.000 belum melebihi 1.400.000, a_5 = 1.464.100 sudah. Jadi tahun ke-5.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b02-e-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: selisih total pembayaran dua tenor*

Sebuah bank menawarkan pinjaman Rp100.000.000,00 dengan dua pilihan: tenor 12 bulan dengan anuitas Rp8.745.148,00 per bulan, atau tenor 24 bulan dengan anuitas Rp4.568.474,00 per bulan. Selisih total pembayaran antara kedua pilihan tersebut adalah ....

- **A. Rp4.701.600,00** ✅  
  <sub>Benar: total 12 bulan = 104.941.776; total 24 bulan = 109.643.376; selisih = 4.701.600</sub>
- B. Rp109.643.376,00  
  <sub>Salah: menjawab total pembayaran tenor 24 bulan</sub>
- C. Rp4.176.674,00  
  <sub>Salah: selisih anuitas per bulan, bukan selisih total pembayaran</sub>
- D. Rp104.941.776,00  
  <sub>Salah: menjawab total pembayaran tenor 12 bulan</sub>

**Pembahasan:** Total tenor 12 bulan = 12 x 8.745.148 = 104.941.776. Total tenor 24 bulan = 24 x 4.568.474 = 109.643.376. Selisih = 4.701.600.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b02-e-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: sisa pinjaman sebagai nilai sekarang sisa anuitas*

Suatu pinjaman dengan bunga 10% per tahun dilunasi dengan 4 kali anuitas tahunan sebesar Rp1.464.100,00 yang dibayar pada akhir tiap tahun. Sesaat setelah anuitas ke-2 dibayarkan, sisa pinjaman sama dengan nilai sekarang dari dua anuitas yang belum dibayar, yaitu sebesar ....

- A. Rp2.928.200,00  
  <sub>Salah: menjumlahkan dua anuitas tanpa diskonto bunga</sub>
- B. Rp1.331.000,00  
  <sub>Salah: hanya mendiskontokan satu anuitas yang tersisa</sub>
- C. Rp2.662.000,00  
  <sub>Salah: mendiskontokan total dua anuitas hanya satu periode</sub>
- **D. Rp2.541.000,00** ✅  
  <sub>Benar: 1.464.100/1,1 + 1.464.100/1,21 = 1.331.000 + 1.210.000 = 2.541.000</sub>

**Pembahasan:** Sisa pinjaman = nilai sekarang dua anuitas yang tersisa: 1.464.100/1,1 + 1.464.100/1,1^2 = 2.541.000. (Cek: pinjaman 4.641.000, sisa tahun ke-1 = 3.641.000, sisa tahun ke-2 = 2.541.000.)
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b02-e-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: temukan kesalahan perhitungan angsuran*

Pinjaman Rp10.000.000,00 berbunga 3% per bulan dilunasi dengan anuitas Rp1.500.000,00 per bulan. Dina menghitung angsuran pokok bulan ke-3 sebagai berikut: a_1 = 1.500.000 - 3% x 10.000.000 = 1.200.000, lalu a_3 = 1.200.000 x 1,03^3 = Rp1.311.272,40. Kesalahan Dina adalah ....

- A. faktor pertumbuhan seharusnya 1 - i = 0,97, lalu dipangkatkan 2  
  <sub>Salah: angsuran pokok membesar dengan rasio 1 + i, bukan 1 - i</sub>
- **B. pangkatnya seharusnya n - 1 = 2, sehingga a_3 = Rp1.273.080,00** ✅  
  <sub>Benar: a_3 = a_1 x r^(n-1) = 1.200.000 x 1,03^2 = 1.273.080, bukan memakai pangkat 3</sub>
- C. hasilnya seharusnya dikalikan 3 karena yang dicari bulan ke-3  
  <sub>Salah: a_3 hanya angsuran bulan itu, tidak dikalikan banyak bulan</sub>
- D. a_1 seharusnya A + Mi, yaitu Rp1.800.000,00, lalu dikali 1,03^2  
  <sub>Salah: tertukar rumus a_1: yang benar A - Mi, dan nilai 1.200.000 milik Dina sudah benar</sub>

**Pembahasan:** a_1 = 1.500.000 - 300.000 = 1.200.000 sudah benar dan rasio 1,03 benar. Namun suku ke-3 barisan geometri memakai pangkat n - 1 = 2: a_3 = 1.200.000 x 1,0609 = 1.273.080.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b02-e-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: memilih tenor sesuai batas cicilan*

Penghasilan bersih Pak Arman Rp30.000.000,00 per bulan dan ia membatasi cicilan tidak lebih dari 15% penghasilan. Ia meminjam Rp100.000.000,00 dengan anuitas per bulan: tenor 12 bulan Rp8.745.148,00; tenor 24 bulan Rp4.568.474,00; tenor 36 bulan Rp3.179.973,00; tenor 48 bulan Rp2.488.504,00. Tenor paling singkat yang memenuhi batas tersebut adalah ....

- A. 24 bulan  
  <sub>Salah: membulatkan 4.568.474 menjadi 4,5 juta sehingga dianggap memenuhi</sub>
- **B. 36 bulan** ✅  
  <sub>Benar: batas = 15% x 30.000.000 = 4.500.000; 12 dan 24 bulan melebihi; 36 bulan 3.179.973 memenuhi</sub>
- C. 48 bulan  
  <sub>Salah: memilih tenor terpanjang padahal ada tenor lebih singkat yang memenuhi</sub>
- D. 12 bulan  
  <sub>Salah: memilih tenor terpendek tanpa memeriksa batas cicilan</sub>

**Pembahasan:** Batas cicilan = 4.500.000. Tenor 12 (8.745.148) dan 24 bulan (4.568.474) melebihi batas, tenor 36 bulan (3.179.973) memenuhi dan paling singkat.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b02-e-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: pinjaman awal dari rasio angsuran pokok*

Suatu pinjaman dilunasi dengan anuitas Rp1.950.000,00 per bulan. Angsuran pokok bulan pertama Rp1.200.000,00 dan bulan kedua Rp1.236.000,00. Besar pinjaman awal adalah ....

- **A. Rp25.000.000,00** ✅  
  <sub>Benar: r = 1.236.000/1.200.000 = 1,03 sehingga i = 3%; bunga bulan 1 = 750.000; M = 750.000/0,03 = 25.000.000</sub>
- B. Rp25.750.000,00  
  <sub>Salah: menghitung i dengan membagi selisih angsuran dengan a_2, bukan a_1</sub>
- C. Rp40.000.000,00  
  <sub>Salah: memakai angsuran pokok sebagai bunga bulan pertama</sub>
- D. Rp65.000.000,00  
  <sub>Salah: memakai seluruh anuitas sebagai bunga bulan pertama</sub>

**Pembahasan:** Karena angsuran pokok membentuk barisan geometri dengan rasio 1 + i, 1 + i = 1.236.000/1.200.000 = 1,03 jadi i = 3%. Bunga bulan 1 = 1.950.000 - 1.200.000 = 750.000 = 3% x M, sehingga M = 25.000.000.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b02-e-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim*

Pak Wahyu meminjam Rp50.000.000,00 dengan bunga 1% per bulan dan membayarnya dengan anuitas Rp2.000.000,00 per bulan (dibayar akhir bulan, bunga dihitung dari sisa pinjaman). Tiga pernyataan tentang pinjaman itu: (I) angsuran pokok bulan ke-2 adalah Rp1.515.000,00; (II) bagian bunga dalam anuitas bulan ke-2 adalah Rp485.000,00; (III) sisa pinjaman setelah anuitas bulan ke-2 adalah Rp47.000.000,00. Pernyataan yang benar adalah ....

- **A. I dan II saja** ✅  
  <sub>Benar: a_1 = 2.000.000 - 500.000 = 1.500.000; a_2 = 1.500.000 x 1,01 = 1.515.000; bunga bulan 2 = 2.000.000 - 1.515.000 = 485.000; sisa = 50.000.000 - 1.500.000 - 1.515.000 = 46.985.000 (bukan 47.000.000)</sub>
- B. II dan III saja  
  <sub>Salah: mengira angsuran pokok bulan ke-2 sama dengan bulan ke-1 (Rp1.500.000,00) sehingga I salah dan III benar</sub>
- C. I saja  
  <sub>Salah: menganggap bunga tiap bulan tetap Rp500.000,00 sehingga II dinilai salah</sub>
- D. I, II, dan III  
  <sub>Salah: menganggap sisa pinjaman Rp47.000.000,00 benar (mengurangkan 2 x Rp1.500.000,00, lupa angsuran naik)</sub>

**Pembahasan:** Bunga bulan 1 = 500.000, a_1 = 1.500.000, rasio 1,01 sehingga a_2 = 1.515.000 (I benar). Bunga bulan 2 = 2.000.000 - 1.515.000 = 485.000 (II benar). Sisa = 50.000.000 - (1.500.000 + 1.515.000) = 46.985.000, bukan 47.000.000 (III salah).
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b02-e-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim*

Pak Rudi meminjam Rp2.040.000,00 dengan bunga 4% per tahun dan melunasinya dengan 2 kali anuitas tahunan sebesar Rp1.081.600,00 (dibayar akhir tahun, bunga dihitung dari sisa pinjaman). Rani menyatakan, "Sisa pinjaman setelah anuitas pertama adalah pinjaman dikurangi anuitas, yaitu Rp958.400,00." Penilaian yang tepat terhadap pernyataan Rani adalah ....

- A. Pernyataan salah; sisa yang benar Rp1.081.600,00 karena sisa sama dengan anuitas kedua  
  <sub>Salah: menyamakan sisa dengan anuitas tanpa mendiskontokan bunga</sub>
- **B. Pernyataan salah; sisa yang benar Rp1.040.000,00 karena sebagian anuitas adalah bunga** ✅  
  <sub>Benar: bunga tahun 1 = 81.600; angsuran pokok = 1.000.000; sisa = 2.040.000 - 1.000.000 = 1.040.000</sub>
- C. Pernyataan salah; sisa yang benar Rp1.000.000,00 karena sisa sama dengan angsuran pokok pertama  
  <sub>Salah: tertukar antara angsuran pokok dan sisa pinjaman</sub>
- D. Pernyataan benar; sisa Rp958.400,00 karena sisa adalah selisih pinjaman dan anuitas  
  <sub>Salah: mengurangkan seluruh anuitas termasuk bunga dari pinjaman</sub>

**Pembahasan:** Bunga tahun 1 = 4% x 2.040.000 = 81.600. Angsuran pokok = 1.081.600 - 81.600 = 1.000.000. Sisa = 2.040.000 - 1.000.000 = 1.040.000. (Cek: nilai sekarang anuitas kedua = 1.081.600/1,04 = 1.040.000.)
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b02-e-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim*

Pada pinjaman dengan anuitas tetap, angsuran pokok bulan ke-1, ke-2, dan ke-3 berturut-turut adalah Rp1.200.000,00, Rp1.236.000,00, dan Rp1.273.080,00. Kesimpulan yang benar tentang pola angsuran pokok dan nilai $a_4$ adalah ....

- A. barisan aritmetika dengan beda Rp37.080,00, sehingga $a_4$ = Rp1.310.160,00  
  <sub>Salah: hanya memakai selisih suku kedua dan ketiga; selisihnya tidak tetap</sub>
- **B. barisan geometri dengan rasio 1,03, sehingga $a_4$ = Rp1.311.272,40** ✅  
  <sub>Benar: selisih 36.000 dan 37.080 tidak sama (bukan aritmetika), rasio 1.236.000/1.200.000 = 1.273.080/1.236.000 = 1,03; a_4 = 1.273.080 x 1,03 = 1.311.272,40</sub>
- C. barisan aritmetika dengan beda Rp36.000,00, sehingga $a_4$ = Rp1.309.080,00  
  <sub>Salah: hanya memakai selisih suku pertama dan kedua tanpa memeriksa suku ketiga</sub>
- D. barisan geometri dengan rasio 1,03, sehingga $a_4$ = Rp1.309.080,00  
  <sub>Salah: rasio benar tetapi suku berikutnya dicari dengan menambah selisih, bukan mengalikan rasio</sub>

**Pembahasan:** Selisih 36.000 dan 37.080 berbeda, jadi bukan aritmetika. Rasio kedua pasangan suku sama, 1,03, jadi geometri. a_4 = 1.273.080 x 1,03 = 1.311.272,40.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b02-e-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim*

Bu Citra meminjam Rp20.000.000,00 dengan bunga 2% per bulan dan berencana membayar anuitas Rp300.000,00 pada akhir tiap bulan (bunga dihitung dari sisa pinjaman). Pernyataan yang benar tentang rencana tersebut adalah ....

- A. sisa pinjaman tetap Rp20.000.000,00 setiap bulan, karena anuitas hanya membayar bunga  
  <sub>Salah: mengira anuitas tepat menutup bunga; bunga Rp400.000,00 lebih besar dari anuitas</sub>
- B. pinjaman lunas dalam sekitar 67 bulan, karena 20.000.000 : 300.000 mendekati 67  
  <sub>Salah: mengabaikan bunga dan membagi pinjaman dengan anuitas</sub>
- C. pinjaman lunas setelah lebih dari 67 bulan, karena bunga memperpanjang masa pelunasan  
  <sub>Salah: mengira bunga hanya memperlama pelunasan, padahal anuitas tidak menutup bunga</sub>
- **D. pinjaman tidak akan pernah lunas, karena bunga bulan pertama Rp400.000,00 lebih besar dari anuitas sehingga sisa pinjaman bertambah** ✅  
  <sub>Benar: bunga bulan 1 = 0,02 x 20.000.000 = 400.000 > 300.000; sisa setelah bulan 1 = 20.100.000 > 20.000.000, dan keadaan ini berlanjut</sub>

**Pembahasan:** Angsuran pokok bulan 1 = 300.000 - 400.000 = -100.000 (negatif), jadi sisa pinjaman naik menjadi 20.100.000 dan bunga bulan berikutnya makin besar. Pinjaman tidak pernah lunas.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b02-e-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan*

Pinjaman Rp24.000.000,00 berbunga 12% per tahun dilunasi dengan anuitas Rp2.400.000,00 per bulan. Bayu menghitung bunga bulan pertama = 12% x 24.000.000 = Rp2.880.000,00, lalu menyimpulkan angsuran pokok bulan pertama bernilai negatif sehingga pinjaman tidak dapat dilunasi. Kesalahan Bayu dan perhitungan yang benar adalah ....

- A. bunga 12% adalah per tahun, sehingga bunga bulan pertama seharusnya 12% x 24.000.000 : 4 = Rp720.000,00 dan angsuran pokok bulan pertama Rp1.680.000,00  
  <sub>Salah: membagi bunga tahunan dengan 4 (bukan 12) saat mengonversi ke bulan</sub>
- B. perhitungan bunga sudah benar, tetapi angsuran pokok seharusnya anuitas ditambah bunga, yaitu Rp5.280.000,00  
  <sub>Salah: mengira angsuran pokok = anuitas + bunga, padahal anuitas = angsuran pokok + bunga</sub>
- C. bunga dihitung dari anuitas, sehingga bunga bulan pertama seharusnya 12% x 2.400.000 = Rp288.000,00 dan angsuran pokok bulan pertama Rp2.112.000,00  
  <sub>Salah: mengira bunga dihitung dari anuitas, padahal dari sisa pinjaman</sub>
- **D. bunga 12% adalah per tahun, sehingga bunga bulan pertama seharusnya 1% x 24.000.000 = Rp240.000,00 dan angsuran pokok bulan pertama Rp2.160.000,00** ✅  
  <sub>Benar: bunga per bulan = 12%/12 = 1%; b_1 = 240.000; a_1 = 2.400.000 - 240.000 = 2.160.000</sub>

**Pembahasan:** Bunga 12% per tahun setara 1% per bulan, jadi b_1 = 0,01 x 24.000.000 = 240.000 dan a_1 = 2.400.000 - 240.000 = 2.160.000 (positif).
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b02-e-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan*

Pinjaman dengan bunga 10% per tahun dilunasi dengan 3 kali anuitas sebesar Rp1.331.000,00 pada akhir tiap tahun. Nanda menghitung sisa pinjaman sesaat setelah anuitas pertama dibayar dengan rumus nilai sekarang anuitas, memakai n = 3, dan memperoleh Rp3.310.000,00. Kesalahan Nanda dan sisa pinjaman yang benar adalah ....

- A. faktor diskonto seharusnya (1,1)^n tanpa tanda negatif, sehingga sisa = 1.331.000 x (1,1 + 1,21) = Rp3.074.610,00  
  <sub>Salah: mengalikan anuitas dengan faktor bunga, bukan mendiskontokan</sub>
- B. sisa pinjaman seharusnya pinjaman dikurangi anuitas, yaitu 3.310.000 - 1.331.000 = Rp1.979.000,00  
  <sub>Salah: mengurangkan seluruh anuitas dari pinjaman tanpa memperhitungkan bunga</sub>
- **C. setelah anuitas pertama tinggal 2 anuitas, sehingga sisa = 1.331.000/1,1 + 1.331.000/1,21 = Rp2.310.000,00** ✅  
  <sub>Benar: sisa pinjaman = nilai sekarang anuitas yang belum dibayar: n = 2, bukan 3; 1.210.000 + 1.100.000 = 2.310.000</sub>
- D. setelah anuitas pertama tinggal 1 anuitas, sehingga sisa = 1.331.000/1,1 = Rp1.210.000,00  
  <sub>Salah: menghitung hanya satu anuitas yang belum dibayar</sub>

**Pembahasan:** Pinjaman Rp3.310.000,00 adalah nilai sekarang 3 anuitas. Setelah anuitas pertama dibayar, yang tersisa 2 anuitas: sisa = 1.331.000/1,1 + 1.331.000/1,1^2 = 1.210.000 + 1.100.000 = 2.310.000. (Cek: 3.310.000 x 1,1 - 1.331.000 = 2.310.000.)
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b02-e-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan*

Pinjaman Rp10.000.000,00 berbunga 3% per bulan dilunasi dengan anuitas tetap Rp1.500.000,00 per bulan (dibayar akhir bulan). Rencana pelunasan yang disusun seorang petugas:

| Bulan | Pinjaman Awal Bulan (Rp) | Bunga (Rp) | Angsuran Pokok (Rp) | Pinjaman Akhir Bulan (Rp) |
|---|---|---|---|---|
| 1 | 10.000.000 | 300.000 | 1.200.000 | 8.800.000 |
| 2 | 8.800.000 | 300.000 | 1.200.000 | 7.600.000 |

Kesalahan pertama pada tabel rencana pelunasan tersebut adalah ....

- A. pinjaman awal bulan ke-2 seharusnya Rp10.000.000,00 karena pinjaman tidak berkurang oleh angsuran  
  <sub>Salah: mengira angsuran tidak mengurangi pinjaman pokok</sub>
- B. angsuran pokok bulan ke-1 seharusnya Rp1.500.000,00 karena seluruh anuitas adalah angsuran pokok  
  <sub>Salah: mengabaikan bagian bunga dalam anuitas</sub>
- **C. bunga bulan ke-2 dihitung dari pinjaman awal bulan ke-1, seharusnya 3% x 8.800.000 = Rp264.000,00** ✅  
  <sub>Benar: bunga tiap bulan dihitung dari pinjaman awal bulan itu; bulan 2: 0,03 x 8.800.000 = 264.000 (bukan 300.000), sehingga angsuran pokok 1.236.000 dan sisa 7.564.000</sub>
- D. anuitas bulan ke-2 seharusnya Rp1.464.000,00 karena ikut turun mengikuti bunga  
  <sub>Salah: mengira anuitas berubah-ubah, padahal anuitas tetap</sub>

**Pembahasan:** Baris 1 benar: bunga 300.000, angsuran 1.200.000, sisa 8.800.000. Pada baris 2 bunga harus 3% x 8.800.000 = 264.000, bukan 300.000. Akibatnya angsuran pokok 1.236.000 dan sisa 7.564.000.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b02-e-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan*

Sebuah pinjaman Rp2.060.000,00 berbunga 12% per tahun dilunasi dengan 2 kali anuitas sebesar Rp1.123.600,00 yang dibayar pada akhir tiap semester (bunga dihitung dari sisa pinjaman). Dani menghitung sisa pinjaman setelah anuitas pertama = 2.060.000 x 1,12 - 1.123.600 = Rp1.183.600,00. Kesalahan Dani dan sisa pinjaman yang benar adalah ....

- **A. bunga per semester seharusnya 12% : 2 = 6%, sehingga sisa = 2.060.000 x 1,06 - 1.123.600 = Rp1.060.000,00** ✅  
  <sub>Benar: bunga 12% per tahun = 6% per semester; 2.060.000 x 1,06 = 2.183.600; dikurangi 1.123.600 = 1.060.000</sub>
- B. bunga tidak perlu dihitung, sehingga sisa = 2.060.000 - 1.123.600 = Rp936.400,00  
  <sub>Salah: mengurangkan seluruh anuitas dari pinjaman tanpa memperhitungkan bunga</sub>
- C. bunga per semester seharusnya 12% x 2 = 24%, sehingga sisa = 2.060.000 x 1,24 - 1.123.600 = Rp1.430.800,00  
  <sub>Salah: mengalikan bukan membagi saat mengonversi bunga tahunan ke semester</sub>
- D. bunga per semester seharusnya 12% : 4 = 3%, sehingga sisa = 2.060.000 x 1,03 - 1.123.600 = Rp998.200,00  
  <sub>Salah: membagi bunga tahunan dengan 4 padahal satu tahun berisi 2 semester</sub>

**Pembahasan:** Satu semester = setengah tahun, sehingga bunga 12% per tahun menjadi 6% per semester. Sisa = 2.060.000 x 1,06 - 1.123.600 = 2.183.600 - 1.123.600 = 1.060.000.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b02-e-hard-bt01-009
*orisinal | C6 | 3 langkah | jenis: perancangan anuitas atau pinjaman*

Bu Ayu meminjam Rp10.000.000,00 dengan bunga 2% per bulan dan ingin pinjamannya lunas dalam 12 bulan dengan anuitas tetap akhir bulan. Bank hanya menerima anuitas berupa kelipatan Rp1.000,00. Anuitas terkecil yang dapat dipilih Bu Ayu agar pinjaman lunas paling lambat dalam 12 bulan adalah ....

- A. Rp834.000,00  
  <sub>Salah: membagi pinjaman dengan 12 tanpa bunga (dibulatkan ke atas)</sub>
- B. Rp1.034.000,00  
  <sub>Salah: menghitung bunga tunggal 12 bulan lalu membagi 12 (bukan anuitas terkecil)</sub>
- C. Rp945.000,00  
  <sub>Salah: membulatkan ke bawah, padahal anuitas kurang dari 945.595,97 tidak cukup melunasi dalam 12 bulan</sub>
- **D. Rp946.000,00** ✅  
  <sub>Benar: anuitas tepat = 10.000.000 x 0,02/(1 - 1,02^-12) = 945.595,97; kelipatan 1.000 terkecil yang tidak kurang dari itu adalah 946.000</sub>

**Pembahasan:** A = M i/(1 - (1+i)^-n) = 10.000.000 x 0,02/(1 - 1,02^-12) = 945.595,97. Anuitas harus tidak kurang dari nilai itu; kelipatan 1.000 terkecil adalah 946.000 (945.000 masih kurang).
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b02-e-hard-bt01-010
*orisinal | C6 | 4 langkah | jenis: perancangan anuitas atau pinjaman*

Pinjaman Rp40.000.000,00 berbunga 2% per bulan akan dilunasi dengan anuitas tetap akhir bulan. Angsuran pokok bulan ke-3 harus sedikitnya Rp1.200.000,00. Anuitas terkecil (kelipatan Rp10.000,00) yang memenuhi syarat itu adalah ....

- A. Rp1.950.000,00  
  <sub>Salah: membulatkan ke bawah: a_3 = 1.150.000 x 1,0404 = 1.196.460 masih kurang dari 1.200.000</sub>
- B. Rp1.160.000,00  
  <sub>Salah: lupa menambahkan bunga bulan pertama Rp800.000,00 (a_1 dianggap sama dengan anuitas)</sub>
- **C. Rp1.960.000,00** ✅  
  <sub>Benar: a_3 = (A - 800.000) x 1,02^2 >= 1.200.000 sehingga A >= 800.000 + 1.153.402,5 = 1.953.402,5; kelipatan 10.000 terkecil adalah 1.960.000</sub>
- D. Rp2.000.000,00  
  <sub>Salah: menetapkan a_1 = 1.200.000 tanpa memakai rasio 1,02 sehingga anuitas terlalu besar (bukan yang terkecil)</sub>

**Pembahasan:** Bunga bulan 1 = 800.000, a_1 = A - 800.000, a_3 = a_1 x 1,02^2 = a_1 x 1,0404. Syarat a_3 >= 1.200.000 memberi a_1 >= 1.153.402,5 dan A >= 1.953.402,5. Kelipatan 10.000 terkecil: 1.960.000 (cek a_3 = 1.160.000 x 1,0404 = 1.206.864; untuk 1.950.000 hanya 1.196.460).
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b02-e-hard-bt01-011
*orisinal | C6 | 3 langkah | jenis: perancangan anuitas atau pinjaman*

Penghasilan bersih Pak Anto Rp13.310.000,00 per tahun dan ia membatasi anuitas tidak lebih dari 20% penghasilan bersih. Bank menawarkan bunga 10% per tahun dengan 3 kali anuitas yang dibayar pada akhir tiap tahun. Pinjaman terbesar yang dapat diambil Pak Anto tanpa melanggar batas tersebut adalah ....

- A. Rp7.986.000,00  
  <sub>Salah: menjumlahkan tiga anuitas tanpa mendiskontokan bunga</sub>
- B. Rp26.620.000,00  
  <sub>Salah: membagi anuitas dengan bunga (nilai sekarang anuitas tak terhingga), bukan 3 anuitas</sub>
- C. Rp7.260.000,00  
  <sub>Salah: mendiskontokan jumlah tiga anuitas hanya satu periode</sub>
- **D. Rp6.620.000,00** ✅  
  <sub>Benar: anuitas maksimum = 0,2 x 13.310.000 = 2.662.000; M = 2.662.000 x (1 - 1,1^-3)/0,1 = 6.620.000</sub>

**Pembahasan:** Batas anuitas = 20% x 13.310.000 = 2.662.000. Pinjaman maksimum = nilai sekarang 3 anuitas: 2.662.000/1,1 + 2.662.000/1,21 + 2.662.000/1,331 = 2.420.000 + 2.200.000 + 2.000.000 = 6.620.000.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b02-e-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: analisis waktu pelunasan*

Pinjaman Rp50.000.000,00 berbunga 10% per tahun dilunasi dengan anuitas Rp7.000.000,00 pada akhir tiap tahun. Setelah pembayaran anuitas tahun ke berapa untuk pertama kalinya sisa pinjaman kurang dari setengah pinjaman awal (kurang dari Rp25.000.000,00)?

- A. tahun ke-10  
  <sub>Salah: bukan yang pertama kali: syarat sudah terpenuhi pada tahun sebelumnya</sub>
- **B. tahun ke-9** ✅  
  <sub>Benar: a_1 = 2.000.000, S_n = 20.000.000 x (1,1^n - 1); S_8 = Rp22.871.776,20 (sisa Rp27.128.223,80), S_9 = Rp27.158.953,82 (sisa Rp22.841.046,18)</sub>
- C. tahun ke-8  
  <sub>Salah: sisa setelah tahun ke-8 masih Rp27.128.223,80, belum kurang dari Rp25.000.000,00</sub>
- D. tahun ke-13  
  <sub>Salah: memakai perkiraan masa pelunasan penuh, bukan saat sisa pertama kali di bawah setengah</sub>

**Pembahasan:** Sisa = M - S_n dengan S_n = 2.000.000 x (1,1^n - 1)/0,1. Sisa < 25.000.000 berarti S_n > 25.000.000, yaitu 1,1^n > 2,25. 1,1^8 = 2,1436 (belum), 1,1^9 = 2,3579 (sudah). Jadi tahun ke-9.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b02-e-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: perbandingan skema*

Sebuah bank memberi pinjaman Rp100.000.000,00 dengan bunga 1% per bulan. Anuitas tenor 12 bulan adalah Rp8.884.879,00 per bulan dan anuitas tenor 24 bulan adalah Rp4.707.347,00 per bulan. Pernyataan yang benar tentang kedua tenor tersebut adalah ....

- A. anuitas tenor 24 bulan kurang dari separuh anuitas tenor 12 bulan, dan total pembayarannya lebih besar Rp6.357.780,00  
  <sub>Salah: salah membandingkan anuitas dengan separuhnya</sub>
- B. anuitas tenor 24 bulan lebih dari separuh anuitas tenor 12 bulan, dan total pembayarannya lebih kecil Rp6.357.780,00  
  <sub>Salah: arah selisih total terbalik: tenor lebih panjang membayar bunga lebih banyak</sub>
- C. anuitas tenor 24 bulan tepat separuh anuitas tenor 12 bulan, sehingga total pembayaran kedua tenor sama  
  <sub>Salah: mengira tenor dua kali lipat membuat anuitas tepat separuh (mengabaikan bunga yang berjalan)</sub>
- **D. anuitas tenor 24 bulan lebih dari separuh anuitas tenor 12 bulan, dan total pembayarannya lebih besar Rp6.357.780,00** ✅  
  <sub>Benar: separuh anuitas 12 bulan = Rp4.442.439,50 < Rp4.707.347,00; total 12 bulan = Rp106.618.548,00, total 24 bulan = Rp112.976.328,00, selisih Rp6.357.780,00</sub>

**Pembahasan:** Separuh anuitas 12 bulan = Rp4.442.439,50, lebih kecil dari Rp4.707.347,00. Total 12 bulan = 12 x 8.884.879 = 106.618.548; total 24 bulan = 24 x 4.707.347 = 112.976.328; selisih 6.357.780.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b02-e-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: perbandingan skema*

Pinjaman X dan pinjaman Y masing-masing Rp20.000.000,00 dengan anuitas yang sama, Rp1.000.000,00 per bulan, dibayar akhir bulan dan bunga dihitung dari sisa pinjaman. Bunga pinjaman X adalah 2% per bulan, sedangkan pinjaman Y 1% per bulan. Setelah anuitas bulan ke-2 dibayarkan, pernyataan yang benar tentang sisa pinjaman kedua pinjaman adalah ....

- **A. sisa pinjaman Y lebih kecil Rp396.000,00 daripada sisa pinjaman X** ✅  
  <sub>Benar: sisa X = 18.788.000, sisa Y = 18.392.000; selisih 396.000</sub>
- B. sisa pinjaman Y lebih kecil Rp400.000,00 daripada sisa pinjaman X  
  <sub>Salah: mengalikan selisih bunga bulan pertama dengan 2, mengabaikan bunga atas selisih sisa</sub>
- C. sisa pinjaman X lebih kecil Rp396.000,00 daripada sisa pinjaman Y  
  <sub>Salah: arah perbandingan terbalik: bunga lebih besar membuat sisa lebih besar</sub>
- D. sisa kedua pinjaman sama, yaitu Rp18.000.000,00, karena anuitasnya sama  
  <sub>Salah: mengabaikan bunga dan mengira anuitas sama berarti sisa sama</sub>

**Pembahasan:** Pinjaman X: sisa 1 = 20.000.000 x 1,02 - 1.000.000 = 19.400.000; sisa 2 = 19.400.000 x 1,02 - 1.000.000 = 18.788.000. Pinjaman Y: sisa 1 = 19.200.000; sisa 2 = 19.200.000 x 1,01 - 1.000.000 = 18.392.000. Selisih 396.000.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b02-e-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: syarat ganda*

Bank menawarkan pinjaman Rp60.000.000,00 dengan bunga 1% per bulan. Anuitas per bulan untuk tiap tenor:

| Tenor | Anuitas per bulan |
|---|---|
| 12 bulan | Rp5.330.927,00 |
| 24 bulan | Rp2.824.408,00 |
| 36 bulan | Rp1.992.859,00 |
| 48 bulan | Rp1.580.030,00 |

Penghasilan bersih Bu Gina Rp14.000.000,00 per bulan. Ia mensyaratkan anuitas tidak lebih dari 25% penghasilan bersih dan total seluruh pembayaran tidak lebih dari Rp70.000.000,00. Tenor yang memenuhi kedua syarat tersebut adalah ....

- **A. 24 bulan** ✅  
  <sub>Benar: batas anuitas 3.500.000; 12 bulan 5.330.927 melanggar; 24 bulan total 67.785.792 memenuhi; 36 bulan total 71.742.924 dan 48 bulan total 75.841.440 melebihi 70.000.000</sub>
- B. 36 bulan  
  <sub>Salah: anuitas memenuhi batas tetapi total pembayaran 71.742.924 melebihi 70.000.000</sub>
- C. 48 bulan  
  <sub>Salah: anuitas memenuhi batas tetapi total pembayaran 75.841.440 melebihi 70.000.000</sub>
- D. 12 bulan  
  <sub>Salah: anuitas 5.330.927 melebihi batas 3.500.000</sub>

**Pembahasan:** Batas anuitas = 25% x 14.000.000 = 3.500.000. Tenor 12 bulan gagal pada anuitas. Tenor 36 dan 48 bulan gagal pada total pembayaran (n x anuitas > 70.000.000). Hanya tenor 24 bulan memenuhi keduanya.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b02-e-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: syarat ganda*

Pinjaman Rp40.000.000,00 berbunga 2% per bulan dilunasi dengan anuitas tetap akhir bulan. Anuitas yang dipilih harus memenuhi dua syarat: angsuran pokok bulan ke-2 sedikitnya Rp1.000.000,00 dan anuitas tidak lebih dari Rp1.900.000,00. Anuitas yang memenuhi kedua syarat adalah ....

- A. Rp1.600.000,00  
  <sub>Salah: anuitas memenuhi batas tetapi a_2 = 816.000 kurang dari 1.000.000</sub>
- B. Rp2.000.000,00  
  <sub>Salah: a_2 memenuhi tetapi anuitas melebihi batas 1.900.000</sub>
- **C. Rp1.800.000,00** ✅  
  <sub>Benar: a_2 = (A - 800.000) x 1,02: untuk 1.800.000 a_2 = 1.020.000 (>= 1.000.000) dan 1.800.000 <= 1.900.000</sub>
- D. Rp2.200.000,00  
  <sub>Salah: a_2 memenuhi tetapi anuitas melebihi batas 1.900.000</sub>

**Pembahasan:** Bunga bulan 1 = 800.000, a_1 = A - 800.000, a_2 = 1,02 a_1. Syarat a_2 >= 1.000.000 memberi A >= 1.780.392. Digabung A <= 1.900.000, hanya 1.800.000 yang memenuhi.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b02-e-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: parameter dari data tidak langsung*

Suatu pinjaman dilunasi dengan anuitas Rp2.000.000,00 per bulan (dibayar akhir bulan, bunga dihitung dari sisa pinjaman). Bagian bunga dalam anuitas bulan ke-1 adalah Rp800.000,00 dan dalam anuitas bulan ke-2 adalah Rp776.000,00. Besar pinjaman awal adalah ....

- A. Rp26.666.667,00  
  <sub>Salah: memakai (b_1 - b_2)/b_1 sebagai suku bunga (3%)</sub>
- **B. Rp40.000.000,00** ✅  
  <sub>Benar: a_1 = 1.200.000; bunga turun 24.000 karena a_1 dibayar: i x a_1 = 24.000 sehingga i = 2%; M = 800.000/0,02 = 40.000.000</sub>
- C. Rp38.800.000,00  
  <sub>Salah: memakai bunga bulan ke-2 sebagai bunga atas pinjaman awal</sub>
- D. Rp66.666.667,00  
  <sub>Salah: memakai (b_1 - b_2)/anuitas sebagai suku bunga (1,2%)</sub>

**Pembahasan:** Sisa pinjaman turun sebesar a_1 = 2.000.000 - 800.000 = 1.200.000, sehingga bunga turun i x 1.200.000 = 800.000 - 776.000 = 24.000, jadi i = 2%. Pinjaman awal = 800.000/0,02 = 40.000.000.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b02-e-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: parameter dari data tidak langsung*

Pinjaman Rp2.320.500,00 berbunga 10% per tahun dilunasi tepat dengan anuitas tetap Rp732.050,00 pada akhir tiap tahun. Banyak anuitas yang dibayarkan sampai pinjaman lunas adalah ....

- A. 6  
  <sub>Salah: nilai sekarang 6 anuitas Rp3.188.269,00, melebihi pinjaman</sub>
- B. 5  
  <sub>Salah: nilai sekarang 5 anuitas Rp2.775.045,00, melebihi pinjaman</sub>
- **C. 4** ✅  
  <sub>Benar: nilai sekarang 4 anuitas = 732.050 x (1 - 1,1^-4)/0,1 = 2.320.500; n = 3 dan n = 5 menghasilkan nilai yang berbeda dari pinjaman</sub>
- D. 3  
  <sub>Salah: nilai sekarang 3 anuitas hanya Rp1.820.500,00, kurang dari pinjaman</sub>

**Pembahasan:** Pinjaman = nilai sekarang semua anuitas. Untuk n = 4: 732.050/1,1 + 732.050/1,21 + 732.050/1,331 + 732.050/1,4641 = 665.500 + 605.000 + 550.000 + 500.000 = 2.320.500. Jadi 4 kali anuitas.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b02-e-hard-bt01-019
*orisinal | C6 | 4 langkah | jenis: restrukturisasi sisa pinjaman*

Pinjaman Rp3.152.500,00 berbunga 5% per tahun dilunasi dengan 3 kali anuitas tahunan sebesar Rp1.157.625,00. Setelah anuitas pertama dibayar, bank menaikkan bunga menjadi 10% per tahun untuk sisa pinjaman, dan sisanya harus lunas dalam 2 kali anuitas tahunan baru yang sama besar. Besar anuitas baru tersebut adalah ....

- **A. Rp1.240.250,00** ✅  
  <sub>Benar: sisa = 3.152.500 x 1,05 - 1.157.625 = 2.152.500; A' = 2.152.500 x 0,1/(1 - 1,1^-2) = 1.240.250</sub>
- B. Rp1.183.875,00  
  <sub>Salah: menambah bunga satu periode lalu membagi dua (bukan anuitas)</sub>
- C. Rp1.076.250,00  
  <sub>Salah: membagi sisa pinjaman dua tanpa bunga</sub>
- D. Rp1.157.625,00  
  <sub>Salah: tetap memakai anuitas lama, mengabaikan kenaikan bunga</sub>

**Pembahasan:** Sisa pinjaman setelah anuitas pertama = 3.152.500 x 1,05 - 1.157.625 = 2.152.500. Anuitas baru: A' = M i /(1 - (1+i)^-n) dengan M = 2.152.500, i = 10%, n = 2: A' = 2.152.500 x 0,1/(1 - 1,1^-2) = 1.240.250.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b02-e-hard-bt01-020
*orisinal | C5 | 6 langkah | jenis: anuitas terakhir dan total bunga*

Pinjaman Rp10.000.000,00 berbunga 10% per tahun dilunasi dengan anuitas Rp3.800.000,00 pada akhir tiap tahun. Pembayaran terakhir menyesuaikan sisa pinjaman beserta bunganya sehingga pinjaman lunas tepat pada pembayaran itu. Total bunga yang dibayarkan selama masa pinjaman adalah ....

- A. Rp5.200.000,00  
  <sub>Salah: menganggap pembayaran terakhir juga Rp3.800.000,00</sub>
- **B. Rp2.205.200,00** ✅  
  <sub>Benar: sisa setelah tahun 1: 7.200.000; tahun 2: 4.120.000; tahun 3: 732.000; pembayaran ke-4 = 732.000 x 1,1 = 805.200; total = 11.400.000 + 805.200 = 12.205.200; bunga = 2.205.200</sub>
- C. Rp1.400.000,00  
  <sub>Salah: hanya menghitung tiga pembayaran penuh dan melupakan pembayaran terakhir</sub>
- D. Rp12.205.200,00  
  <sub>Salah: menjawab total seluruh pembayaran, belum dikurangi pinjaman pokok</sub>

**Pembahasan:** Sisa akhir tahun: 10.000.000 x 1,1 - 3.800.000 = 7.200.000; 7.200.000 x 1,1 - 3.800.000 = 4.120.000; 4.120.000 x 1,1 - 3.800.000 = 732.000. Pembayaran ke-4 = 732.000 x 1,1 = 805.200. Total bayar = 3 x 3.800.000 + 805.200 = 12.205.200. Total bunga = 12.205.200 - 10.000.000 = 2.205.200.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
