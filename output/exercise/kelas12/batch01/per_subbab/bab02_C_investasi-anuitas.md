# Lembar koreksi — kelas12 SMA12U-B2 subbab C: Investasi Anuitas

56 soal | easy 20, medium 19, hard 17 | variasi 10, orisinal 46
> **Kapasitas kurang (medium): 19 dari kuota 20** — Acuan variasi layak subbab C (Contoh 2.3, 2.4, pretest Aliyya, UK-6, UK-7) sudah terpakai maksimum 2 variasi masing-masing di easy, sehingga medium seluruhnya orisinal. Materi subbab hanya FV/PV anuitas biasa, konversi periode, dan hubungan FV-PV; soal orisinal ke-20 akan nyaris kembar dengan soal lain atau memakai anuitas terutang yang rumusnya tidak diberikan buku.
> **Kapasitas kurang (hard): 17 dari kuota 20** — Subbab C hanya memuat anuitas biasa (FV, PV, konversi periode, hubungan FV-PV). Setelah easy dan medium, seluruh acuan variasi sudah terpakai maksimum dan sudut hard (evaluasi klaim, temukan kesalahan, syarat ganda, perancangan, perbandingan skema, dua fase) habis pada 17 soal; soal tambahan akan nyaris kembar atau memerlukan anuitas terutang yang rumusnya tidak diberikan buku.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b02-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: FV anuitas tahunan*

Dewi selalu menyisihkan uangnya sebesar Rp4.000.000,00 per tahun pada akhir tahun dan memasukkannya ke dalam rekening deposito dengan bunga majemuk 5% per tahun. Berapa nilai masa depan tabungan Dewi dalam 3 tahun?

- **A. Rp12.610.000,00** ✅  
  <sub>Benar: FV = A x ((1+i)^n - 1)/i = 4.000.000 x (1,05^3 - 1)/0,05 = 4.000.000 x 3,1525</sub>
- B. Rp4.630.500,00  
  <sub>Salah: memakai rumus bunga majemuk untuk setoran tunggal, bukan anuitas</sub>
- C. Rp8.200.000,00  
  <sub>Salah: memakai n-1 = 2 periode sehingga satu setoran terlewat</sub>
- D. Rp12.000.000,00  
  <sub>Salah: hanya menjumlahkan setoran, bunga diabaikan</sub>

**Pembahasan:** Setoran akhir tahun: $FV = A \times \frac{(1+i)^n - 1}{i} = 4.000.000 \times \frac{1,05^3 - 1}{0,05} = 4.000.000 \times 3,1525 = 12.610.000$.
**Acuan:** siswa — siswa hal.67 Contoh 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b02-c-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: FV anuitas bulanan*

Pak Rudi rutin menabung Rp1.000.000,00 pada akhir setiap bulan di sebuah bank yang memberikan bunga majemuk 2% per bulan. Tentukan nilai masa depan seluruh tabungan Pak Rudi setelah 4 bulan.

- A. Rp1.082.432,00  
  <sub>Salah: memakai rumus setoran tunggal, hanya satu setoran yang dibungakan</sub>
- **B. Rp4.121.608,00** ✅  
  <sub>Benar: FV = 1.000.000 x (1,02^4 - 1)/0,02 = 1.000.000 x 4,121608</sub>
- C. Rp4.000.000,00  
  <sub>Salah: bunga diabaikan, hanya total setoran</sub>
- D. Rp3.060.400,00  
  <sub>Salah: memakai n-1 = 3 periode</sub>

**Pembahasan:** $FV = 1.000.000 \times \frac{1,02^4 - 1}{0,02} = 1.000.000 \times 4,121608 = 4.121.608$.
**Acuan:** siswa — siswa hal.67 Contoh 2.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b02-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: PV penarikan tahunan*

Seorang pengusaha menabung sejumlah uang di bank dan mendapat bunga majemuk 10% per tahun. Pada akhir setiap tahun selama 3 tahun, ia mengambil Rp2.662.000,00 dari tabungan itu sehingga tabungannya habis tepat setelah pengambilan ketiga. Berapakah uang yang harus ia tabung di awal?

- **A. Rp6.620.000,00** ✅  
  <sub>Benar: PV = 2.662.000 x (1 - 1,1^-3)/0,1 = 2.662.000 x 2,48685 = 6.620.000</sub>
- B. Rp7.986.000,00  
  <sub>Salah: menjumlahkan semua pengambilan tanpa memperhitungkan bunga</sub>
- C. Rp8.811.220,00  
  <sub>Salah: tertukar memakai rumus nilai masa depan anuitas</sub>
- D. Rp2.000.000,00  
  <sub>Salah: hanya menghitung nilai sekarang pengambilan terakhir</sub>

**Pembahasan:** $PV = A \times \frac{1-(1+i)^{-n}}{i} = 2.662.000 \times \frac{1-1,1^{-3}}{0,1} = 6.620.000$.
**Acuan:** siswa — siswa hal.69 Contoh 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b02-c-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: PV beasiswa*

Sebuah yayasan ingin memberi beasiswa sebesar Rp2.205.000,00 pada akhir setiap tahun kepada seorang siswa selama 2 tahun. Dana beasiswa disimpan di bank berbunga majemuk 5% per tahun dan habis tepat setelah pemberian kedua. Dana yang harus disimpan yayasan di awal adalah ....

- **A. Rp4.100.000,00** ✅  
  <sub>Benar: PV = 2.205.000/1,05 + 2.205.000/1,05^2 = 2.100.000 + 2.000.000</sub>
- B. Rp4.410.000,00  
  <sub>Salah: menjumlahkan pemberian tanpa memperhitungkan bunga</sub>
- C. Rp4.520.250,00  
  <sub>Salah: memakai rumus nilai masa depan anuitas</sub>
- D. Rp2.100.000,00  
  <sub>Salah: hanya menghitung nilai sekarang pemberian pertama</sub>

**Pembahasan:** $PV = \frac{2.205.000}{1,05} + \frac{2.205.000}{1,05^2} = 2.100.000 + 2.000.000 = 4.100.000$.
**Acuan:** siswa — siswa hal.69 Contoh 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b02-c-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: PV pensiun bulanan*

Pak Doni ingin menerima penghasilan Rp3.000.000,00 pada akhir setiap bulan selama 2 bulan setelah pensiun dari tabungannya. Bank memberi bunga majemuk 24% per tahun yang dihitung tiap bulan (2% per bulan). Besar uang tabungan yang harus ia siapkan adalah ....

- A. Rp4.370.447,00  
  <sub>Salah: memakai bunga 24% per bulan tanpa dibagi 12</sub>
- B. Rp6.060.000,00  
  <sub>Salah: memakai rumus nilai masa depan anuitas, bukan nilai sekarang</sub>
- **C. Rp5.824.683,00** ✅  
  <sub>Benar: PV = 3.000.000 x (1 - 1,02^-2)/0,02 = 3.000.000 x 1,941561</sub>
- D. Rp6.000.000,00  
  <sub>Salah: menjumlahkan penghasilan tanpa memperhitungkan bunga</sub>

**Pembahasan:** $i = 24\% : 12 = 2\%$ per bulan. $PV = 3.000.000 \times \frac{1-1,02^{-2}}{0,02} \approx 3.000.000 \times 1,941561$.
**Acuan:** pretest — kelas12-b02-p0068-ayo-berpikir-kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b02-c-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: PV pensiun semesteran*

Bu Mirna ingin menerima Rp3.630.000,00 pada akhir setiap semester selama 1 tahun dari tabungannya. Bank memberi bunga majemuk 20% per tahun yang dihitung tiap semester. Tabungan awal yang harus ia siapkan adalah ....

- A. Rp5.545.833,00  
  <sub>Salah: memakai bunga 20% per semester tanpa dibagi 2</sub>
- B. Rp7.260.000,00  
  <sub>Salah: tanpa memperhitungkan bunga</sub>
- C. Rp7.623.000,00  
  <sub>Salah: memakai rumus nilai masa depan anuitas</sub>
- **D. Rp6.300.000,00** ✅  
  <sub>Benar: i = 20%/2 = 10% per semester, n = 2; PV = 3.630.000/1,1 + 3.630.000/1,21 = 3.300.000 + 3.000.000</sub>

**Pembahasan:** $i = 20\% : 2 = 10\%$ per semester, $n = 2$. $PV = \frac{3.630.000}{1,1} + \frac{3.630.000}{1,1^2} = 3.300.000 + 3.000.000 = 6.300.000$.
**Acuan:** pretest — kelas12-b02-p0068-ayo-berpikir-kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b02-c-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: FV tabungan bulanan*

Rina menabung Rp1.000.000,00 pada akhir setiap bulan ke rekening deposito yang memberikan bunga majemuk 12% per tahun, dihitung tiap bulan. Nilai masa depan tabungannya setelah 3 bulan adalah ....

- A. Rp3.000.000,00  
  <sub>Salah: bunga diabaikan</sub>
- B. Rp1.030.301,00  
  <sub>Salah: memakai rumus setoran tunggal</sub>
- **C. Rp3.030.100,00** ✅  
  <sub>Benar: i = 12%/12 = 1% per bulan; FV = 1.000.000 x (1,01^3 - 1)/0,01 = 1.000.000 x 3,0301</sub>
- D. Rp3.374.400,00  
  <sub>Salah: memakai 12% per bulan tanpa dibagi 12</sub>

**Pembahasan:** $i = 12\% : 12 = 1\%$ per bulan. $FV = 1.000.000 \times \frac{1,01^3-1}{0,01} = 1.000.000 \times 3,0301 = 3.030.100$.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b02-c-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: FV tabungan semesteran*

Tia menabung Rp5.000.000,00 pada akhir setiap semester di sebuah bank dengan bunga majemuk 6% per tahun, dihitung tiap semester. Nilai masa depan tabungannya setelah satu setengah tahun adalah ....

- A. Rp15.918.000,00  
  <sub>Salah: memakai 6% per semester tanpa dibagi 2</sub>
- B. Rp15.000.000,00  
  <sub>Salah: bunga diabaikan</sub>
- C. Rp10.150.000,00  
  <sub>Salah: mengira satu setengah tahun hanya 2 semester</sub>
- **D. Rp15.454.500,00** ✅  
  <sub>Benar: i = 6%/2 = 3% per semester, n = 1,5 x 2 = 3; FV = 5.000.000 x (1,03^3 - 1)/0,03</sub>

**Pembahasan:** $i = 6\% : 2 = 3\%$ per semester, $n = 3$. $FV = 5.000.000 \times \frac{1,03^3-1}{0,03} = 15.454.500$.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b02-c-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: mencari lama menabung*

Eko menabung Rp2.000.000,00 pada akhir setiap tahun di bank dengan bunga majemuk 10% per tahun. Agar nilai masa depan tabungannya mencapai Rp6.620.000,00, Eko harus menabung selama .... tahun.

- **A. 3** ✅  
  <sub>Benar: FV tiga setoran = 2.000.000 x (1,1^3 - 1)/0,1 = 2.000.000 x 3,31 = 6.620.000</sub>
- B. 4  
  <sub>Salah: empat setoran menghasilkan 9.282.000, melebihi target</sub>
- C. 2  
  <sub>Salah: dua setoran hanya menghasilkan 4.200.000</sub>
- D. 5  
  <sub>Salah: lima setoran menghasilkan 12.210.200, melebihi target</sub>

**Pembahasan:** Uji n: n = 2 memberi $2.000.000 \times 2,1 = 4.200.000$; n = 3 memberi $2.000.000 \times 3,31 = 6.620.000$. Jadi n = 3.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b02-c-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: mencari periode menabung*

Sari menabung Rp5.000.000,00 pada akhir setiap triwulan di bank dengan bunga majemuk 4% per triwulan. Agar nilai masa depan tabungannya mencapai Rp10.200.000,00, Sari harus menabung selama .... triwulan.

- A. 3  
  <sub>Salah: tiga setoran menghasilkan 15.608.000, melebihi target</sub>
- **B. 2** ✅  
  <sub>Benar: FV dua setoran = 5.000.000 x (1,04^2 - 1)/0,04 = 5.000.000 x 2,04 = 10.200.000</sub>
- C. 1  
  <sub>Salah: satu setoran hanya bernilai 5.000.000</sub>
- D. 4  
  <sub>Salah: empat setoran menghasilkan 21.232.320, melebihi target</sub>

**Pembahasan:** $n=1$: 5.000.000. $n=2$: $5.000.000 \times 2,04 = 10.200.000$. Jadi $n = 2$ triwulan.
**Acuan:** pretest — kelas12-b02-p0096-uji-kompetensi-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b02-c-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: definisi anuitas*

Dalam investasi, anuitas adalah ....

- A. bunga yang baru dibayarkan sekali pada akhir seluruh masa investasi  
  <sub>Salah: mengira anuitas adalah jadwal pembayaran bunga</sub>
- B. pembayaran pada periode teratur dengan jumlah yang berbeda-beda tiap periode  
  <sub>Salah: salah: jumlah anuitas harus sama</sub>
- **C. sistem pembayaran atau penerimaan pada periode waktu yang teratur dengan jumlah yang sama** ✅  
  <sub>Benar: sesuai definisi anuitas di buku</sub>
- D. setoran satu kali di awal yang kemudian hanya dibungakan sampai akhir masa  
  <sub>Salah: tertukar dengan setoran tunggal bunga majemuk</sub>

**Pembahasan:** Anuitas adalah sistem pembayaran atau penerimaan pada periode teratur dalam jumlah yang sama.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b02-c-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: klasifikasi skenario anuitas*

Pak Anto menyetor Rp1.000.000,00 ke tabungan berjangka pada tanggal 1 setiap bulan, yaitu di awal tiap bulan, dengan jumlah yang selalu sama. Jenis anuitas pada penyetoran Pak Anto adalah ....

- A. anuitas biasa  
  <sub>Salah: tertukar dengan anuitas biasa yang dibayar di akhir periode</sub>
- **B. anuitas terutang** ✅  
  <sub>Benar: pembayaran di awal setiap periode disebut anuitas terutang</sub>
- C. tabungan sekali setor  
  <sub>Salah: setoran dilakukan berulang, bukan sekali</sub>
- D. bunga tunggal  
  <sub>Salah: bunga tunggal bukan jenis anuitas</sub>

**Pembahasan:** Setoran di awal setiap periode adalah anuitas terutang; di akhir periode adalah anuitas biasa.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b02-c-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: rasio deret anuitas*

Nilai akhir tiap setoran pada anuitas beserta bunganya membentuk deret geometri dengan rasio $(1+i)$. Jika bunga majemuk 8% per tahun, rasio deret tersebut adalah ....

- A. 8  
  <sub>Salah: memakai persen tanpa mengubah ke desimal</sub>
- B. 0,92  
  <sub>Salah: mengurangkan bunga dari 1, bukan menambahkan</sub>
- **C. 1,08** ✅  
  <sub>Benar: 1 + 0,08 = 1,08</sub>
- D. 0,08  
  <sub>Salah: mengira rasio sama dengan suku bunga saja</sub>

**Pembahasan:** $r = 1 + i = 1 + 0,08 = 1,08$.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b02-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: istilah PV dan FV*

Pada konsep bunga majemuk, nilai sekarang ($PV$) menyatakan ....

- A. jumlah seluruh bunga yang diterima  
  <sub>Salah: PV bukan jumlah bunga</sub>
- B. besarnya tabungan akhir setelah dikenai bunga  
  <sub>Salah: tertukar dengan nilai masa depan ($FV$)</sub>
- **C. besarnya tabungan awal** ✅  
  <sub>Benar: PV adalah tabungan awal atau modal awal</sub>
- D. besarnya setoran rutin tiap periode  
  <sub>Salah: tertukar dengan anuitas $A$</sub>

**Pembahasan:** Nilai sekarang adalah tabungan awal; nilai masa depan adalah tabungan akhir.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b02-c-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: FV dari PV*

Hubungan nilai sekarang dan nilai masa depan adalah $FV = PV \times (1+i)^n$. Jika $PV$ = Rp2.500.000,00, bunga majemuk 4% per tahun, dan $n$ = 2 tahun, maka $FV$ adalah ....

- A. Rp2.700.000,00  
  <sub>Salah: memakai bunga tunggal 1 + 2 x 4%</sub>
- **B. Rp2.704.000,00** ✅  
  <sub>Benar: 2.500.000 x 1,04^2 = 2.500.000 x 1,0816</sub>
- C. Rp2.600.000,00  
  <sub>Salah: hanya satu periode, lupa pangkat 2</sub>
- D. Rp2.812.160,00  
  <sub>Salah: memakai pangkat 3 (n + 1)</sub>

**Pembahasan:** $FV = 2.500.000 \times 1,04^2 = 2.500.000 \times 1,0816 = 2.704.000$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b02-c-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: konversi bunga per periode*

Bank memberi bunga majemuk 9% per tahun, dan Hana menyetor tabungan tiap triwulan (3 bulan). Suku bunga per triwulan ($i$) yang dipakai adalah ....

- **A. 2,25%** ✅  
  <sub>Benar: satu tahun = 4 triwulan, sehingga i = 9%/4 = 2,25%</sub>
- B. 3%  
  <sub>Salah: membagi 9% dengan 3 (banyak bulan per triwulan)</sub>
- C. 0,75%  
  <sub>Salah: membagi dengan 12 (bunga per bulan)</sub>
- D. 9%  
  <sub>Salah: tidak mengubah bunga tahunan ke bunga per triwulan</sub>

**Pembahasan:** Satu tahun ada 4 triwulan, sehingga $i = 9\% : 4 = 2,25\%$.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b02-c-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: banyak periode setoran*

Dika menyetor tabungan anuitas setiap semester selama 4 tahun. Banyak periode setoran ($n$) adalah ....

- A. 12  
  <sub>Salah: mengalikan 4 dengan 3 (keliru banyak semester per tahun)</sub>
- B. 4  
  <sub>Salah: memakai lama dalam tahun, bukan semester</sub>
- C. 48  
  <sub>Salah: memakai banyak bulan, bukan semester</sub>
- **D. 8** ✅  
  <sub>Benar: 1 tahun = 2 semester, 4 tahun = 8 semester</sub>

**Pembahasan:** $n = 4 \times 2 = 8$ semester.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b02-c-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: memilih rumus FV*

Seseorang menabung sebesar $A$ pada akhir setiap periode dengan suku bunga majemuk $i$ per periode selama $n$ periode. Rumus nilai masa depan ($FV$) tabungannya adalah ....

- A. $FV = A \times \frac{(1+i)^n - 1}{n}$  
  <sub>Salah: membagi dengan $n$, bukan dengan $i$</sub>
- B. $FV = A \times \frac{1-(1+i)^{-n}}{i}$  
  <sub>Salah: tertukar dengan rumus nilai sekarang ($PV$) anuitas</sub>
- C. $FV = A \times (1+i)^n$  
  <sub>Salah: rumus setoran tunggal, bukan anuitas</sub>
- **D. $FV = A \times \frac{(1+i)^n - 1}{i}$** ✅  
  <sub>Benar: rumus FV anuitas biasa</sub>

**Pembahasan:** Nilai masa depan anuitas biasa: $FV = A \times \frac{(1+i)^n - 1}{i}$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b02-c-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: memilih rumus PV*

Seseorang ingin mengambil uang sebesar $A$ pada akhir setiap periode selama $n$ periode dari tabungan yang berbunga majemuk $i$ per periode. Rumus tabungan awal yang diperlukan ($PV$) adalah ....

- A. $PV = A \times \frac{1-(1+i)^{-n}}{n}$  
  <sub>Salah: membagi dengan $n$, bukan dengan $i$</sub>
- B. $PV = A \times \frac{(1+i)^n - 1}{i}$  
  <sub>Salah: tertukar dengan rumus nilai masa depan ($FV$) anuitas</sub>
- C. $PV = A \times \frac{1-(1+i)^{n}}{i}$  
  <sub>Salah: lupa tanda negatif pada pangkat $n$</sub>
- **D. $PV = A \times \frac{1-(1+i)^{-n}}{i}$** ✅  
  <sub>Benar: rumus PV anuitas biasa</sub>

**Pembahasan:** Nilai sekarang anuitas biasa: $PV = A \times \frac{1-(1+i)^{-n}}{i}$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b02-c-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: jumlah dua setoran*

Lani menyetor Rp1.500.000,00 pada akhir tahun pertama dan Rp1.500.000,00 pada akhir tahun kedua ke bank dengan bunga majemuk 8% per tahun. Nilai tabungan Lani tepat setelah setoran kedua adalah ....

- A. Rp3.000.000,00  
  <sub>Salah: bunga diabaikan</sub>
- **B. Rp3.120.000,00** ✅  
  <sub>Benar: setoran pertama berbunga 1 tahun: 1.500.000 x 1,08 = 1.620.000; ditambah setoran kedua 1.500.000</sub>
- C. Rp3.369.600,00  
  <sub>Salah: menganggap setoran di awal tahun (anuitas terutang)</sub>
- D. Rp3.240.000,00  
  <sub>Salah: kedua setoran dikalikan 1,08 padahal setoran kedua belum berbunga</sub>

**Pembahasan:** $1.500.000 \times 1,08 + 1.500.000 = 1.620.000 + 1.500.000 = 3.120.000$.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b02-c-medium-bt01-001
*orisinal | C3 | 3 langkah | jenis: FV anuitas triwulan*

Bu Ratna menabung Rp2.000.000,00 pada akhir setiap triwulan selama 1 tahun di bank yang memberi bunga majemuk 20% per tahun, dihitung setiap triwulan. Nilai masa depan seluruh tabungan Bu Ratna setelah 1 tahun adalah ....

- A. Rp10.736.000,00  
  <sub>Salah: memakai 20% per triwulan tanpa dibagi 4</sub>
- B. Rp6.305.000,00  
  <sub>Salah: memakai n = 3 sehingga satu setoran terlewat</sub>
- **C. Rp8.620.250,00** ✅  
  <sub>Benar: i = 20%/4 = 5% per triwulan, n = 4; FV = 2.000.000 x (1,05^4 - 1)/0,05 = 2.000.000 x 4,310125</sub>
- D. Rp8.000.000,00  
  <sub>Salah: bunga diabaikan, hanya total setoran</sub>

**Pembahasan:** $i = 20\% : 4 = 5\%$ per triwulan, $n = 1 \times 4 = 4$. $FV = 2.000.000 \times \frac{1,05^4-1}{0,05} = 2.000.000 \times 4,310125 = 8.620.250$.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b02-c-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: mencari besar setoran*

Dedi ingin memiliki tabungan Rp13.923.000,00 tepat setelah 4 tahun. Ia menyetor sejumlah uang yang sama pada akhir setiap tahun ke bank yang memberi bunga majemuk 10% per tahun. Besar setoran tiap tahun yang harus ia lakukan adalah ....

- A. Rp1.392.300,00  
  <sub>Salah: mengalikan target dengan suku bunga 10%</sub>
- B. Rp9.945.000,00  
  <sub>Salah: membagi dengan $1 + n \times i$ = 1,4 (memakai bunga tunggal)</sub>
- C. Rp3.480.750,00  
  <sub>Salah: membagi target dengan 4 tanpa memperhitungkan bunga</sub>
- **D. Rp3.000.000,00** ✅  
  <sub>Benar: faktor = (1,1^4 - 1)/0,1 = 4,641; A = 13.923.000 : 4,641 = 3.000.000</sub>

**Pembahasan:** $FV = A \times \frac{(1+i)^n - 1}{i}$ sehingga $13.923.000 = A \times 4,641$ dan $A = 3.000.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b02-c-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: total bunga anuitas*

Ali menyetor Rp1.500.000,00 pada akhir setiap tahun selama 3 tahun ke bank dengan bunga majemuk 8% per tahun. Total bunga yang diperoleh Ali selama 3 tahun adalah ....

- A. Rp360.000,00  
  <sub>Salah: memakai bunga tunggal 8% dari total setoran</sub>
- B. Rp4.869.600,00  
  <sub>Salah: menjawab nilai masa depan, bukan bunganya</sub>
- **C. Rp369.600,00** ✅  
  <sub>Benar: FV = 1.500.000 x 3,2464 = 4.869.600; total setoran 4.500.000; bunga = 369.600</sub>
- D. Rp3.369.600,00  
  <sub>Salah: mengurangi dengan satu setoran saja, bukan seluruh setoran</sub>

**Pembahasan:** $FV = 1.500.000 \times \frac{1,08^3-1}{0,08} = 4.869.600$. Bunga = $4.869.600 - 3 \times 1.500.000 = 369.600$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b02-c-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: FV anuitas lalu dibiarkan berbunga*

Wati menyetor Rp1.000.000,00 pada akhir setiap tahun selama 3 tahun (tiga kali setoran) ke bank dengan bunga majemuk 10% per tahun. Setelah setoran ketiga ia tidak menyetor lagi dan membiarkan tabungannya berbunga 1 tahun lagi. Saldo tabungan Wati pada akhir tahun ke-4 adalah ....

- **A. Rp3.641.000,00** ✅  
  <sub>Benar: FV setelah setoran ketiga = 3.310.000; setahun kemudian 3.310.000 x 1,1 = 3.641.000</sub>
- B. Rp4.641.000,00  
  <sub>Salah: menganggap ada empat kali setoran</sub>
- C. Rp4.310.000,00  
  <sub>Salah: menambah setoran keempat padahal tidak ada setoran lagi</sub>
- D. Rp3.310.000,00  
  <sub>Salah: lupa menambahkan bunga tahun ke-4</sub>

**Pembahasan:** $FV_3 = 1.000.000 \times \frac{1,1^3-1}{0,1} = 3.310.000$. Lalu $FV = 3.310.000 \times 1,1 = 3.641.000$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b02-c-medium-bt01-005
*orisinal | C4 | 4 langkah | jenis: saldo setelah penarikan*

Pak Hasan menabung sejumlah uang di bank dengan bunga majemuk 10% per tahun. Pada akhir setiap tahun selama 3 tahun ia menarik Rp2.662.000,00 sehingga tabungannya habis tepat setelah penarikan ketiga. Saldo tabungan Pak Hasan tepat setelah penarikan pertama adalah ....

- A. Rp3.958.000,00  
  <sub>Salah: mengurangi tabungan awal dengan penarikan tanpa memperhitungkan bunga</sub>
- **B. Rp4.620.000,00** ✅  
  <sub>Benar: saldo setelah penarikan pertama = nilai sekarang dua penarikan tersisa = 2.662.000/1,1 + 2.662.000/1,21 = 2.420.000 + 2.200.000</sub>
- C. Rp6.620.000,00  
  <sub>Salah: menjawab tabungan awal, bukan saldo setelah penarikan</sub>
- D. Rp5.324.000,00  
  <sub>Salah: menjumlahkan dua penarikan tersisa tanpa bunga</sub>

**Pembahasan:** Tabungan awal $= 6.620.000$. Setelah satu tahun: $6.620.000 \times 1,1 - 2.662.000 = 4.620.000$. Cek: $\frac{2.662.000}{1,1} + \frac{2.662.000}{1,1^2} = 2.420.000 + 2.200.000 = 4.620.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b02-c-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: PV penarikan semesteran*

Bu Sinta ingin menarik Rp1.331.000,00 pada akhir setiap semester selama satu setengah tahun dari tabungannya. Bank memberi bunga majemuk 20% per tahun yang dihitung tiap semester, dan tabungan habis tepat setelah penarikan terakhir. Tabungan awal yang harus disiapkan adalah ....

- A. Rp2.310.000,00  
  <sub>Salah: memakai n = 2 (mengira satu setengah tahun hanya 2 semester)</sub>
- **B. Rp3.310.000,00** ✅  
  <sub>Benar: i = 10% per semester, n = 3; PV = 1.331.000 x (1 - 1,1^-3)/0,1 = 1.331.000 x 2,486852 ... = 1.210.000 + 1.100.000 + 1.000.000</sub>
- C. Rp3.993.000,00  
  <sub>Salah: menjumlahkan penarikan tanpa memperhitungkan bunga</sub>
- D. Rp4.405.610,00  
  <sub>Salah: memakai rumus nilai masa depan anuitas</sub>

**Pembahasan:** $i = 20\% : 2 = 10\%$, $n = 1,5 \times 2 = 3$. $PV = \frac{1.331.000}{1,1} + \frac{1.331.000}{1,1^2} + \frac{1.331.000}{1,1^3} = 1.210.000 + 1.100.000 + 1.000.000 = 3.310.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b02-c-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: mencari suku bunga*

Rani menyetor Rp3.000.000,00 pada akhir tahun pertama dan Rp3.000.000,00 pada akhir tahun kedua ke sebuah bank. Tepat setelah setoran kedua, saldo tabungannya Rp6.450.000,00. Suku bunga majemuk bank tersebut per tahun adalah ....

- A. 30%  
  <sub>Salah: membagi bunga 450.000 dengan 1.500.000</sub>
- B. 7,5%  
  <sub>Salah: membagi hasil 15% dengan 2 karena ada dua setoran</sub>
- **C. 15%** ✅  
  <sub>Benar: A + A(1+i) = 6.450.000 sehingga 1 + i = 1,15, i = 15%</sub>
- D. 115%  
  <sub>Salah: menganggap faktor 1,15 sebagai suku bunga</sub>

**Pembahasan:** Setoran pertama berbunga satu tahun: $3.000.000(1+i) + 3.000.000 = 6.450.000$, sehingga $1+i = 1,15$ dan $i = 15\%$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b02-c-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: deret geometri anuitas*

Rudi menyetor Rp2.000.000,00 pada akhir setiap tahun selama 3 tahun ke bank dengan bunga majemuk 5% per tahun. Nilai akhir tiap setoran beserta bunganya (dihitung sampai akhir tahun ketiga) adalah Rp2.000.000,00; Rp2.100.000,00; dan Rp2.205.000,00, yang membentuk deret geometri. Rasio deret dan nilai masa depan seluruh tabungan Rudi berturut-turut adalah ....

- **A. 1,05 dan Rp6.305.000,00** ✅  
  <sub>Benar: rasio = 2.100.000 : 2.000.000 = 1,05; jumlah = 2.000.000 + 2.100.000 + 2.205.000</sub>
- B. 0,05 dan Rp6.305.000,00  
  <sub>Salah: mengira rasio sama dengan suku bunga saja</sub>
- C. 1,05 dan Rp4.305.000,00  
  <sub>Salah: tidak menyertakan suku pertama dalam penjumlahan</sub>
- D. 1,05 dan Rp6.000.000,00  
  <sub>Salah: menjumlahkan setoran tanpa bunga</sub>

**Pembahasan:** Rasio $= 1 + 0,05 = 1,05$. Jumlah $= 2.000.000 + 2.100.000 + 2.205.000 = 6.305.000$.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b02-c-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: mencari lama penarikan*

Tabungan awal Rp3.640.000,00 disimpan di bank dengan bunga majemuk 20% per tahun. Pada akhir setiap tahun diambil Rp1.728.000,00 sehingga tabungan habis tepat setelah pengambilan terakhir. Pengambilan dapat dilakukan selama .... tahun.

- A. 2  
  <sub>Salah: dua pengambilan hanya membutuhkan tabungan awal 2.640.000</sub>
- **B. 3** ✅  
  <sub>Benar: n = 3 memberi PV = 1.440.000 + 1.200.000 + 1.000.000 = 3.640.000</sub>
- C. 4  
  <sub>Salah: empat pengambilan membutuhkan sekitar 4.473.333, melebihi tabungan awal</sub>
- D. 5  
  <sub>Salah: lima pengambilan membutuhkan jauh lebih dari 3.640.000</sub>

**Pembahasan:** Uji $n$: $n=2$ memberi $1.440.000+1.200.000 = 2.640.000$; $n=3$ memberi $2.640.000 + 1.000.000 = 3.640.000$. Jadi 3 tahun.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b02-c-medium-bt01-010
*orisinal | C4 | 4 langkah | jenis: membandingkan dua bank*

Dua orang masing-masing menyetor Rp1.000.000,00 pada akhir setiap tahun selama 3 tahun. Orang pertama menabung di Bank X dengan bunga majemuk 8% per tahun, orang kedua di Bank Y dengan bunga majemuk 10% per tahun. Selisih nilai masa depan tabungan keduanya adalah ....

- A. Rp3.246.400,00  
  <sub>Salah: menjawab nilai masa depan Bank X, bukan selisih</sub>
- **B. Rp63.600,00** ✅  
  <sub>Benar: FV X = 3.246.400; FV Y = 3.310.000; selisih = 63.600</sub>
- C. Rp60.000,00  
  <sub>Salah: memakai bunga tunggal: 2% x 3.000.000</sub>
- D. Rp20.000,00  
  <sub>Salah: memakai n = 2 bukan 3</sub>

**Pembahasan:** $FV_X = 1.000.000 \times 3,2464 = 3.246.400$, $FV_Y = 1.000.000 \times 3,31 = 3.310.000$. Selisih $= 63.600$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b02-c-medium-bt01-011
*orisinal | C3 | 2 langkah | jenis: memilih model FV bulanan*

Rina menabung Rp750.000,00 pada akhir setiap bulan selama 2 tahun di bank dengan bunga majemuk 12% per tahun yang dihitung tiap bulan. Ekspresi yang benar untuk nilai masa depan tabungan Rina adalah ....

- A. $750.000 \times \frac{(1,01)^{2} - 1}{0,01}$  
  <sub>Salah: memakai n = 2 (tahun) padahal periode bulanan</sub>
- B. $750.000 \times \frac{(1,12)^{24} - 1}{0,12}$  
  <sub>Salah: memakai bunga tahunan 12% untuk periode bulanan</sub>
- **C. $750.000 \times \frac{(1,01)^{24} - 1}{0,01}$** ✅  
  <sub>Benar: i = 12%/12 = 1% = 0,01 per bulan dan n = 2 x 12 = 24</sub>
- D. $750.000 \times \frac{(1,01)^{24} - 1}{24}$  
  <sub>Salah: membagi dengan $n$, bukan dengan $i$</sub>

**Pembahasan:** $i = 12\% : 12 = 1\% = 0,01$, $n = 2 \times 12 = 24$. $FV = 750.000 \times \frac{(1,01)^{24}-1}{0,01}$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b02-c-medium-bt01-012
*orisinal | C3 | 4 langkah | jenis: FV deposit awal ditambah anuitas*

Pak Toni mendepositokan Rp2.000.000,00 hari ini, lalu menyetor Rp1.000.000,00 pada akhir setiap tahun selama 3 tahun ke bank yang sama dengan bunga majemuk 10% per tahun. Saldo tabungan Pak Toni tepat setelah setoran ketiga adalah ....

- A. Rp5.000.000,00  
  <sub>Salah: menjumlahkan semua uang tanpa bunga</sub>
- B. Rp5.310.000,00  
  <sub>Salah: deposit awal tidak dibungakan</sub>
- C. Rp3.310.000,00  
  <sub>Salah: lupa menyertakan deposit awal</sub>
- **D. Rp5.972.000,00** ✅  
  <sub>Benar: deposit awal: 2.000.000 x 1,1^3 = 2.662.000; setoran rutin: 1.000.000 x 3,31 = 3.310.000; jumlah 5.972.000</sub>

**Pembahasan:** $2.000.000 \times 1,1^3 + 1.000.000 \times \frac{1,1^3-1}{0,1} = 2.662.000 + 3.310.000 = 5.972.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b02-c-medium-bt01-013
*orisinal | C4 | 4 langkah | jenis: kekurangan dana*

Bu Dewi ingin menarik Rp1.157.625,00 pada akhir setiap tahun selama 3 tahun dari tabungan yang berbunga majemuk 5% per tahun, sehingga tabungan habis tepat setelah penarikan ketiga. Saat ini ia hanya memiliki Rp3.000.000,00. Kekurangan dana yang harus ia tambahkan adalah ....

- A. Rp3.152.500,00  
  <sub>Salah: menjawab kebutuhan dana, bukan kekurangannya</sub>
- B. Rp472.875,00  
  <sub>Salah: memakai total penarikan tanpa bunga</sub>
- **C. Rp152.500,00** ✅  
  <sub>Benar: kebutuhan = PV = 1.102.500 + 1.050.000 + 1.000.000 = 3.152.500; kekurangan = 152.500</sub>
- D. Rp847.500,00  
  <sub>Salah: memakai dua penarikan saja lalu membalik selisihnya</sub>

**Pembahasan:** $PV = \frac{1.157.625}{1,05} + \frac{1.157.625}{1,05^2} + \frac{1.157.625}{1,05^3} = 1.102.500 + 1.050.000 + 1.000.000 = 3.152.500$. Kekurangan $= 3.152.500 - 3.000.000 = 152.500$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b02-c-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: PV penarikan 4 tahun*

Yayasan Bina Cerdas menyiapkan dana beasiswa yang diambil Rp1.464.100,00 pada akhir setiap tahun selama 4 tahun. Dana disimpan di bank dengan bunga majemuk 10% per tahun dan habis tepat setelah pengambilan keempat. Dana yang harus disimpan di awal adalah ....

- A. Rp5.856.400,00  
  <sub>Salah: menjumlahkan pengambilan tanpa memperhitungkan bunga</sub>
- B. Rp14.641.000,00  
  <sub>Salah: membagi dengan $i$ saja tanpa faktor $1-(1+i)^{-n}$</sub>
- C. Rp3.641.000,00  
  <sub>Salah: memakai n = 3 sehingga satu pengambilan terlewat</sub>
- **D. Rp4.641.000,00** ✅  
  <sub>Benar: PV = 1.331.000 + 1.210.000 + 1.100.000 + 1.000.000 = 4.641.000</sub>

**Pembahasan:** $PV = A \times \frac{1-(1+i)^{-4}}{i} = \frac{1.464.100}{1,1} + \frac{1.464.100}{1,1^2} + \frac{1.464.100}{1,1^3} + \frac{1.464.100}{1,1^4} = 4.641.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b02-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: FV anuitas bulanan desimal*

Nina menabung Rp1.000.000,00 pada akhir setiap bulan selama 3 bulan di bank yang memberi bunga majemuk 18% per tahun, dihitung tiap bulan. Nilai masa depan tabungan Nina setelah 3 bulan adalah ....

- **A. Rp3.045.225,00** ✅  
  <sub>Benar: i = 18%/12 = 1,5% per bulan; FV = 1.000.000 x (1 + 1,015 + 1,030225)</sub>
- B. Rp3.572.400,00  
  <sub>Salah: memakai 18% per bulan tanpa dibagi 12</sub>
- C. Rp3.000.000,00  
  <sub>Salah: bunga diabaikan</sub>
- D. Rp2.015.000,00  
  <sub>Salah: memakai n = 2</sub>

**Pembahasan:** $i = 18\% : 12 = 1,5\%$. $FV = 1.000.000 \times \frac{1,015^3-1}{0,015} = 1.000.000 \times 3,045225 = 3.045.225$.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b02-c-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: PV penarikan triwulan*

Pak Joko akan menarik Rp1.102.500,00 pada akhir setiap triwulan selama 6 bulan dari tabungannya. Bank memberi bunga majemuk 20% per tahun yang dihitung tiap triwulan, dan tabungan habis tepat setelah penarikan terakhir. Tabungan awal yang harus disiapkan adalah ....

- A. Rp2.260.125,00  
  <sub>Salah: memakai rumus nilai masa depan anuitas</sub>
- B. Rp1.684.375,00  
  <sub>Salah: memakai 20% per triwulan tanpa dibagi 4</sub>
- C. Rp2.205.000,00  
  <sub>Salah: menjumlahkan penarikan tanpa bunga</sub>
- **D. Rp2.050.000,00** ✅  
  <sub>Benar: i = 20%/4 = 5% per triwulan, n = 2; PV = 1.102.500/1,05 + 1.102.500/1,05^2 = 1.050.000 + 1.000.000</sub>

**Pembahasan:** $i = 5\%$, $n = 6 : 3 = 2$. $PV = \frac{1.102.500}{1,05} + \frac{1.102.500}{1,05^2} = 1.050.000 + 1.000.000 = 2.050.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b02-c-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: total bunga penarikan*

Pak Budi menabung sejumlah uang di bank berbunga majemuk 10% per tahun. Pada akhir tahun pertama dan kedua ia menarik Rp2.420.000,00 sehingga tabungannya habis tepat setelah penarikan kedua. Total bunga yang diterima Pak Budi selama 2 tahun adalah ....

- A. Rp484.000,00  
  <sub>Salah: mengambil 10% dari total penarikan</sub>
- B. Rp4.200.000,00  
  <sub>Salah: menjawab tabungan awal, bukan bunga</sub>
- C. Rp4.840.000,00  
  <sub>Salah: menjawab total penarikan, bukan bunga</sub>
- **D. Rp640.000,00** ✅  
  <sub>Benar: tabungan awal 1 : 2.200.000 + 2.000.000 = 4.200.000; total penarikan 4.840.000; bunga = 640.000</sub>

**Pembahasan:** $PV = \frac{2.420.000}{1,1} + \frac{2.420.000}{1,1^2} = 2.200.000 + 2.000.000 = 4.200.000$. Bunga $= 4.840.000 - 4.200.000 = 640.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b02-c-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: setoran tunggal setara FV anuitas*

Seseorang menyetor Rp1.210.000,00 pada akhir setiap tahun selama 2 tahun ke bank dengan bunga majemuk 10% per tahun. Jika ia hanya menyetor satu kali di awal (tahun ke-0) agar saldo setelah 2 tahun sama besar dengan nilai masa depan tabungan tadi, setoran tunggal itu adalah ....

- A. Rp2.420.000,00  
  <sub>Salah: menjumlahkan dua setoran tanpa bunga</sub>
- **B. Rp2.100.000,00** ✅  
  <sub>Benar: FV anuitas = 1.210.000 x 2,1 = 2.541.000; PV = 2.541.000 : 1,1^2 = 2.100.000</sub>
- C. Rp3.074.610,00  
  <sub>Salah: mengalikan, bukan membagi, dengan $(1+i)^n$</sub>
- D. Rp2.310.000,00  
  <sub>Salah: membagi dengan 1,1 sekali, bukan 1,1 pangkat 2</sub>

**Pembahasan:** $FV = 1.210.000 \times 2,1 = 2.541.000$. Dari $FV = PV (1+i)^n$: $PV = \frac{2.541.000}{1,1^2} = 2.100.000$.
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b02-c-medium-bt01-019
*orisinal | C3 | 2 langkah | jenis: saldo setelah setoran berikutnya*

Tepat setelah setoran keempat, saldo tabungan Sari Rp4.641.000,00. Sari menyetor Rp1.000.000,00 pada akhir setiap tahun ke bank dengan bunga majemuk 10% per tahun. Saldo tabungan Sari tepat setelah setoran kelima adalah ....

- **A. Rp6.105.100,00** ✅  
  <sub>Benar: saldo berbunga setahun: 4.641.000 x 1,1 = 5.105.100; ditambah setoran kelima 1.000.000</sub>
- B. Rp5.641.000,00  
  <sub>Salah: menambah setoran tanpa memperhitungkan bunga setahun</sub>
- C. Rp6.000.000,00  
  <sub>Salah: menjumlahkan lima setoran tanpa bunga</sub>
- D. Rp5.105.100,00  
  <sub>Salah: lupa menambahkan setoran kelima</sub>

**Pembahasan:** $4.641.000 \times 1,1 + 1.000.000 = 5.105.100 + 1.000.000 = 6.105.100$.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas12-b02-c-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan pembilang FV*

Dina menghitung nilai masa depan setoran Rp2.000.000,00 pada akhir setiap tahun selama 4 tahun dengan bunga majemuk 10% per tahun. Ia menulis $FV = 2.000.000 \times \frac{(1,1)^4}{0,1} = 29.282.000$. Pernyataan yang benar tentang pekerjaan Dina adalah ....

- A. Benar: nilai masa depan Rp29.282.000,00 karena bunga ikut dihitung penuh  
  <sub>Salah: menganggap rumus Dina benar padahal pembilang tidak dikurangi 1</sub>
- B. Salah: tidak ada bunga pada anuitas, sehingga nilai masa depan yang benar Rp8.000.000,00  
  <sub>Salah: mengabaikan bunga majemuk</sub>
- **C. Salah: pembilang seharusnya $(1,1)^4 - 1$, sehingga nilai masa depan yang benar Rp9.282.000,00** ✅  
  <sub>Benar: rumus FV anuitas adalah A x ((1+i)^n - 1)/i; Dina lupa mengurangi 1, hasil benar 2.000.000 x 4,641</sub>
- D. Salah: suku bunga seharusnya $10\% : 4$, sehingga nilai masa depan yang benar Rp9.282.000,00  
  <sub>Salah: alasan pembetulan keliru: bunga sudah per tahun, tidak perlu dibagi 4</sub>

**Pembahasan:** Rumus yang benar: $FV = A \times \frac{(1+i)^n - 1}{i} = 2.000.000 \times \frac{1,4641 - 1}{0,1} = 2.000.000 \times 4,641 = 9.282.000$. Dina memakai $(1,1)^4/0,1 = 14,641$ sehingga hasilnya terlalu besar.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b02-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim suku bunga dua kali*

Dua orang masing-masing menyetor Rp1.000.000,00 pada akhir setiap tahun selama 3 tahun. Orang pertama mendapat bunga majemuk 10% per tahun dan orang kedua 20% per tahun. Pernyataan yang benar adalah ....

- **A. Total bunga orang kedua (Rp640.000,00) lebih dari dua kali total bunga orang pertama (Rp310.000,00)** ✅  
  <sub>Benar: FV 10% = 3.310.000 sehingga bunga 310.000; FV 20% = 3.640.000 sehingga bunga 640.000 > 2 x 310.000 = 620.000</sub>
- B. Total bunga orang kedua kurang dari dua kali total bunga orang pertama  
  <sub>Salah: membalik arah perbandingan; 640.000 > 620.000</sub>
- C. Nilai masa depan tabungan orang kedua tepat dua kali nilai masa depan tabungan orang pertama  
  <sub>Salah: mengira suku bunga dua kali membuat FV dua kali; FV 3.640.000 vs 3.310.000</sub>
- D. Total bunga orang kedua tepat dua kali total bunga orang pertama  
  <sub>Salah: mengira bunga sebanding dengan suku bunga seperti bunga tunggal; 640.000 bukan 620.000</sub>

**Pembahasan:** $FV_{10\%} = 1.000.000 \times 3,31 = 3.310.000$ (bunga 310.000); $FV_{20\%} = 1.000.000 \times 3,64 = 3.640.000$ (bunga 640.000). Karena bunga majemuk berbunga lagi, $640.000 > 2 \times 310.000 = 620.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b02-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: membandingkan dua skema periode setoran*

Dua skema menabung selama 2 tahun dengan bunga majemuk 20% per tahun. Skema 1: menyetor Rp1.000.000,00 pada akhir setiap semester dengan bunga dihitung tiap semester. Skema 2: menyetor Rp2.000.000,00 pada akhir setiap tahun dengan bunga dihitung tiap tahun. Kesimpulan yang benar adalah ....

- A. Skema 1 lebih besar, selisih nilai masa depan Rp641.000,00  
  <sub>Salah: mengambil bunga skema 1 (641.000) sebagai selisih</sub>
- **B. Skema 1 lebih besar, selisih nilai masa depan Rp241.000,00** ✅  
  <sub>Benar: Skema 1: i = 10%, n = 4, FV = 4.641.000. Skema 2: i = 20%, n = 2, FV = 4.400.000. Selisih 241.000</sub>
- C. Kedua skema sama besar karena total setoran sama, yaitu Rp4.000.000,00  
  <sub>Salah: mengabaikan bunga dan perbedaan frekuensi</sub>
- D. Skema 2 lebih besar, selisih nilai masa depan Rp241.000,00  
  <sub>Salah: membalik arah perbandingan</sub>

**Pembahasan:** Skema 1: $i = 20\% : 2 = 10\%$, $n = 4$, $FV = 1.000.000 \times 4,641 = 4.641.000$. Skema 2: $FV = 2.000.000 \times 2,2 = 4.400.000$. Selisih $= 241.000$.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b02-c-hard-bt01-004
*orisinal | C6 | 3 langkah | jenis: setoran minimum kelipatan*

Rendi ingin tabungannya paling sedikit Rp10.000.000,00 tepat setelah setoran ke-4. Ia menyetor sejumlah yang sama pada akhir setiap tahun selama 4 tahun ke bank berbunga majemuk 10% per tahun, dan besar setoran harus kelipatan Rp100.000,00. Setoran tahunan terkecil yang memenuhi adalah ....

- A. Rp2.100.000,00  
  <sub>Salah: pembulatan ke bawah: FV = 9.746.100 masih kurang dari 10.000.000</sub>
- B. Rp2.500.000,00  
  <sub>Salah: membagi target dengan 4 tanpa bunga; memenuhi tetapi bukan yang terkecil</sub>
- **C. Rp2.200.000,00** ✅  
  <sub>Benar: A >= 10.000.000 : 4,641 = 2.154.6xx; kelipatan 100.000 terkecil adalah 2.200.000 (FV 10.210.200)</sub>
- D. Rp2.000.000,00  
  <sub>Salah: FV = 9.282.000 kurang dari target</sub>

**Pembahasan:** $A \geq 10.000.000 : 4,641 \approx 2.154.665$. Kelipatan 100.000 terkecil: $2.200.000$ (FV $= 10.210.200$). Untuk $2.100.000$ FV $= 9.746.100 < 10.000.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b02-c-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: banyak setoran minimum*

Fira menyetor Rp2.000.000,00 pada akhir setiap tahun ke bank berbunga majemuk 10% per tahun. Ia ingin nilai masa depan tabungannya lebih dari Rp15.000.000,00 tepat setelah setoran terakhir. Banyak setoran paling sedikit yang diperlukan adalah ....

- A. 4  
  <sub>Salah: FV n = 4 hanya 9.282.000</sub>
- B. 5  
  <sub>Salah: FV n = 5 hanya 12.210.200, belum melampaui 15.000.000</sub>
- **C. 6** ✅  
  <sub>Benar: n = 5 memberi 12.210.200 (kurang); n = 6 memberi 15.431.220 (lebih dari 15.000.000)</sub>
- D. 8  
  <sub>Salah: membagi 15.000.000 dengan 2.000.000 tanpa bunga lalu membulatkan ke atas</sub>

**Pembahasan:** $FV_5 = 2.000.000 \times 6,1051 = 12.210.200$ dan $FV_6 = 2.000.000 \times 7,7156 = 15.431.220$. Jadi $n$ minimal 6.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b02-c-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan rumus FV dipakai untuk PV*

Gita ingin menarik Rp1.210.000,00 pada akhir setiap tahun selama 2 tahun dari tabungan berbunga majemuk 10% per tahun, hingga tabungan habis. Untuk mencari tabungan awal ia menghitung $1.210.000 \times \frac{(1,1)^2 - 1}{0,1} = 2.541.000$. Pernyataan yang benar adalah ....

- A. Gita keliru memakai bunga; tabungan awal yang benar Rp2.420.000,00  
  <sub>Salah: menjumlahkan penarikan tanpa bunga</sub>
- B. Gita keliru karena hanya perlu satu penarikan; tabungan awal yang benar Rp1.100.000,00  
  <sub>Salah: hanya menghitung penarikan pertama</sub>
- C. Gita sudah benar karena tabungan awal harus mencakup bunga sehingga Rp2.541.000,00  
  <sub>Salah: tabungan awal justru lebih kecil dari total penarikan karena bunga membantu</sub>
- **D. Gita keliru memakai rumus nilai masa depan; tabungan awal yang benar Rp2.100.000,00** ✅  
  <sub>Benar: tabungan awal adalah nilai sekarang: 1.210.000/1,1 + 1.210.000/1,21 = 1.100.000 + 1.000.000</sub>

**Pembahasan:** Nilai sekarang: $PV = 1.210.000 \times \frac{1-(1,1)^{-2}}{0,1} = 1.100.000 + 1.000.000 = 2.100.000$. Rumus Gita adalah rumus nilai masa depan.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b02-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: banyak penarikan penuh maksimum*

Bu Lia menyimpan Rp3.200.000,00 di bank berbunga majemuk 10% per tahun. Pada akhir setiap tahun, mulai akhir tahun pertama, ia menarik Rp1.000.000,00. Banyak penarikan penuh Rp1.000.000,00 yang dapat ia lakukan paling banyak adalah ....

- **A. 4** ✅  
  <sub>Benar: PV 4 penarikan = 3.169.865 <= 3.200.000, PV 5 penarikan = 3.790.787 > 3.200.000; saldo setelah penarikan ke-4 = 44.120</sub>
- B. 3  
  <sub>Salah: membagi 3.200.000 dengan 1.000.000 tanpa memperhitungkan bunga</sub>
- C. 5  
  <sub>Salah: PV 5 penarikan 3.790.787 melebihi tabungan</sub>
- D. 2  
  <sub>Salah: menghitung terlalu banyak diskonto atau berhenti terlalu cepat</sub>

**Pembahasan:** $PV_4 = 1.000.000 \times 3,169865 = 3.169.865 \leq 3.200.000$, sedangkan $PV_5 = 3.790.787 > 3.200.000$. Simulasi: saldo akhir tahun ke-4 setelah penarikan Rp44.120, tidak cukup untuk penarikan ke-5.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b02-c-hard-bt01-008
*orisinal | C6 | 3 langkah | jenis: setoran ekuivalen dua lama menabung*

Rama menyetor Rp1.000.000,00 pada akhir setiap tahun selama 4 tahun ke bank berbunga majemuk 10% per tahun. Sari ingin nilai masa depan tabungannya sama dengan Rama tepat saat setoran terakhir, tetapi hanya menyetor selama 2 tahun di bank yang sama. Setoran tahunan Sari yang harus ia lakukan adalah ....

- A. Rp2.100.000,00  
  <sub>Salah: mengambil faktor anuitas 2 tahun (2,1) sebagai besar setoran</sub>
- B. Rp2.320.500,00  
  <sub>Salah: membagi FV dengan 2 (banyak setoran), bukan dengan faktor anuitas</sub>
- **C. Rp2.210.000,00** ✅  
  <sub>Benar: FV Rama = 4.641.000; faktor 2 tahun = 2,1 sehingga A = 4.641.000 : 2,1 = 2.210.000</sub>
- D. Rp2.000.000,00  
  <sub>Salah: membagi 4 tahun dengan 2 tahun tanpa memperhitungkan bunga</sub>

**Pembahasan:** $FV_{Rama} = 1.000.000 \times 4,641 = 4.641.000$. Untuk Sari: $A \times 2,1 = 4.641.000$ sehingga $A = 2.210.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b02-c-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan eksponen setoran*

Hana menyetor Rp500.000,00 pada akhir setiap tahun selama 4 tahun ke bank berbunga majemuk 20% per tahun. Ia menghitung nilai masa depan sebagai $500.000 \times (1,2^4 + 1,2^3 + 1,2^2 + 1,2) = 3.220.800$. Pernyataan yang benar adalah ....

- **A. Hana keliru karena setoran terakhir tidak berbunga; nilai masa depan yang benar Rp2.684.000,00** ✅  
  <sub>Benar: suku yang benar 1 + 1,2 + 1,2^2 + 1,2^3 = 5,368 sehingga FV = 500.000 x 5,368</sub>
- B. Hana benar karena setiap setoran berbunga sejak disetor  
  <sub>Salah: menganggap setoran akhir tahun berbunga satu tahun penuh</sub>
- C. Hana keliru karena bunga harus tunggal; nilai yang benar Rp2.500.000,00  
  <sub>Salah: mengabaikan bunga majemuk</sub>
- D. Hana keliru karena setoran pertama tidak berbunga; nilai masa depan yang benar Rp2.684.000,00  
  <sub>Salah: setoran pertama justru berbunga paling lama (3 tahun)</sub>

**Pembahasan:** Setoran akhir tahun ke-4 belum sempat berbunga. $FV = 500.000 \times (1 + 1,2 + 1,44 + 1,728) = 500.000 \times 5,368 = 2.684.000$. Hana memberi tiap setoran bunga satu tahun lebih lama.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b02-c-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: mencari penarikan dari saldo tengah*

Seseorang menarik jumlah yang sama pada akhir setiap tahun selama 3 tahun dari tabungan berbunga majemuk 10% per tahun, hingga tabungan habis tepat setelah penarikan ketiga. Tepat setelah penarikan pertama, saldo tabungan Rp2.310.000,00. Besar penarikan tiap tahun adalah ....

- A. Rp770.000,00  
  <sub>Salah: membagi saldo dengan 3 padahal tersisa dua penarikan</sub>
- B. Rp2.541.000,00  
  <sub>Salah: menganggap hanya satu penarikan tersisa sehingga saldo = A/1,1</sub>
- C. Rp1.155.000,00  
  <sub>Salah: membagi saldo dengan 2 tanpa bunga</sub>
- **D. Rp1.331.000,00** ✅  
  <sub>Benar: saldo = A/1,1 + A/1,21 = A x 1,735537 = 2.310.000 sehingga A = 1.331.000</sub>

**Pembahasan:** Saldo setelah penarikan pertama sama dengan nilai sekarang dua penarikan tersisa: $\frac{A}{1,1} + \frac{A}{1,1^2} = 2.310.000$, sehingga $A \times \frac{2,1}{1,21} = 2.310.000$ dan $A = 1.331.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b02-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: syarat ganda banyak setoran*

Dani menyetor Rp1.000.000,00 pada akhir setiap tahun ke bank berbunga majemuk 10% per tahun, sebanyak $n$ kali. Ia ingin nilai masa depan tabungan tepat setelah setoran terakhir paling sedikit Rp6.000.000,00, sedangkan total uang yang ia setor tidak lebih dari Rp8.000.000,00. Banyak nilai $n$ bulat positif yang memenuhi kedua syarat adalah ....

- **A. 4** ✅  
  <sub>Benar: FV n=5 = 6.105.100 >= 6.000.000 (n=4: 4.641.000 kurang); total setoran <= 8.000.000 berarti n <= 8; n = 5, 6, 7, 8</sub>
- B. 5  
  <sub>Salah: memasukkan n = 4 padahal FV hanya 4.641.000</sub>
- C. 8  
  <sub>Salah: hanya memakai syarat total setoran, tanpa syarat nilai masa depan</sub>
- D. 3  
  <sub>Salah: memakai syarat total setoran kurang dari 8.000.000 sehingga n = 8 tidak dihitung dan n = 5, 6, 7 saja</sub>

**Pembahasan:** $FV_4 = 4.641.000 < 6.000.000$ dan $FV_5 = 6.105.100 \geq 6.000.000$, jadi $n \geq 5$. Total setoran $n \times 1.000.000 \leq 8.000.000$ memberi $n \leq 8$. Nilai $n$: 5, 6, 7, 8 (4 nilai).
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b02-c-hard-bt01-012
*orisinal | C6 | 4 langkah | jenis: dua fase menabung lalu menarik*

Wulan menyetor Rp1.000.000,00 pada akhir tahun pertama dan akhir tahun kedua ke bank berbunga majemuk 10% per tahun. Setelah itu ia tidak menyetor lagi, melainkan menarik jumlah yang sama pada akhir tahun ketiga dan akhir tahun keempat sehingga tabungan habis tepat setelah penarikan keempat. Besar penarikan tiap tahun adalah ....

- A. Rp2.541.000,00  
  <sub>Salah: mengalikan saldo dengan 1,21 menjadi satu nilai, bukan dibagi dua penarikan</sub>
- **B. Rp1.210.000,00** ✅  
  <sub>Benar: saldo akhir tahun ke-2 = 2.100.000 = PV dua penarikan = A x (1/1,1 + 1/1,21) = A x 1,735537 sehingga A = 1.210.000</sub>
- C. Rp1.050.000,00  
  <sub>Salah: membagi saldo 2.100.000 dengan 2 tanpa bunga</sub>
- D. Rp1.155.000,00  
  <sub>Salah: membagi saldo yang sudah berbunga satu tahun (2.310.000) dengan 2</sub>

**Pembahasan:** Setelah dua setoran: $FV = 1.000.000 \times 2,1 = 2.100.000$. Nilai ini sama dengan nilai sekarang dua penarikan: $A \left(\frac{1}{1,1} + \frac{1}{1,1^2}\right) = 2.100.000$, sehingga $A = 1.210.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b02-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: tunai vs cicilan nilai sekarang*

Seorang penjual menawarkan dua pilihan pembayaran: menerima Rp3.300.000,00 tunai sekarang, atau menerima Rp1.331.000,00 pada akhir setiap tahun selama 3 tahun. Suku bunga majemuk yang berlaku 10% per tahun. Kesimpulan yang benar adalah ....

- A. Pilihan tunai lebih menguntungkan karena nilai sekarang penerimaan berkala Rp10.000,00 lebih kecil  
  <sub>Salah: membalik arah perbandingan</sub>
- B. Kedua pilihan sama menguntungkan karena nilai sekarangnya sama  
  <sub>Salah: salah hitung nilai sekarang penerimaan berkala</sub>
- C. Pilihan 3 kali penerimaan lebih menguntungkan karena selisihnya Rp693.000,00  
  <sub>Salah: membandingkan total tanpa bunga (3.993.000 - 3.300.000)</sub>
- **D. Pilihan 3 kali penerimaan lebih menguntungkan karena nilai sekarangnya Rp10.000,00 lebih besar daripada tunai** ✅  
  <sub>Benar: PV penerimaan = 1.210.000 + 1.100.000 + 1.000.000 = 3.310.000 > 3.300.000</sub>

**Pembahasan:** $PV = \frac{1.331.000}{1,1} + \frac{1.331.000}{1,1^2} + \frac{1.331.000}{1,1^3} = 1.210.000 + 1.100.000 + 1.000.000 = 3.310.000$. Lebih besar Rp10.000 dari tunai Rp3.300.000.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b02-c-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: bunga yang dihasilkan tiap setoran*

Gilang menyetor Rp1.000.000,00 pada akhir setiap tahun selama 4 tahun ke bank berbunga majemuk 10% per tahun. Pernyataan yang benar tentang bunga yang dihasilkan masing-masing setoran sampai akhir tahun ke-4 adalah ....

- A. Setoran pertama menghasilkan bunga Rp300.000,00 dan setoran kedua Rp200.000,00  
  <sub>Salah: memakai bunga tunggal 10% per tahun</sub>
- **B. Setoran pertama menghasilkan bunga Rp331.000,00, setoran kedua Rp210.000,00, dan setoran keempat tidak menghasilkan bunga** ✅  
  <sub>Benar: setoran pertama berbunga 3 tahun: 1.331.000 - 1.000.000; kedua 2 tahun: 1.210.000 - 1.000.000; keempat tidak berbunga</sub>
- C. Setoran pertama menghasilkan bunga Rp400.000,00 dan setoran keempat Rp100.000,00  
  <sub>Salah: memakai bunga tunggal dan mengira setoran terakhir berbunga satu tahun</sub>
- D. Setiap setoran menghasilkan bunga yang sama, yaitu Rp160.250,00  
  <sub>Salah: membagi total bunga 641.000 rata ke empat setoran</sub>

**Pembahasan:** Setoran ke-$k$ berbunga $(4-k)$ tahun: $1.000.000 \times (1,1^{4-k} - 1)$ = 331.000; 210.000; 100.000; 0. Jumlahnya 641.000 = 4.641.000 - 4.000.000.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b02-c-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: pola bunga saat penarikan*

Seseorang menyimpan Rp3.310.000,00 di bank berbunga majemuk 10% per tahun, lalu menarik Rp1.331.000,00 pada akhir setiap tahun selama 3 tahun hingga tabungan habis. Bunga yang diterima pada tahun pertama lebih besar daripada bunga yang diterima pada tahun ketiga sebesar ....

- A. Rp331.000,00  
  <sub>Salah: menjawab bunga tahun pertama saja</sub>
- B. Rp110.000,00  
  <sub>Salah: mengurangkan bunga tahun kedua dengan bunga tahun ketiga</sub>
- C. Rp683.000,00  
  <sub>Salah: menjawab total bunga tiga tahun</sub>
- **D. Rp210.000,00** ✅  
  <sub>Benar: bunga tahun 1 = 331.000; saldo awal tahun 3 = 1.210.000 sehingga bunga tahun 3 = 121.000; selisih 210.000</sub>

**Pembahasan:** Tahun 1: $3.310.000 \times 10\% = 331.000$, saldo akhir $2.310.000$. Tahun 2: bunga $231.000$, saldo akhir $1.210.000$. Tahun 3: bunga $121.000$. Selisih $331.000 - 121.000 = 210.000$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b02-c-hard-bt01-016
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim lama menabung dua kali*

Bayu berkata, "Jika lama menabung dilipatduakan, nilai masa depan tabunganku juga menjadi dua kali." Bayu menyetor sejumlah yang sama pada akhir setiap tahun dengan bunga majemuk 20% per tahun. Perbandingan nilai masa depan tabungan setelah 4 tahun terhadap setelah 2 tahun adalah ...., sehingga klaim Bayu keliru.

- A. 5,368  
  <sub>Salah: mengambil faktor anuitas 4 tahun saja</sub>
- B. 2  
  <sub>Salah: mengikuti klaim Bayu seolah FV sebanding dengan lama menabung</sub>
- **C. 2,44** ✅  
  <sub>Benar: faktor 4 tahun = 5,368; faktor 2 tahun = 2,2; 5,368 : 2,2 = 2,44</sub>
- D. 2,2  
  <sub>Salah: mengambil faktor anuitas 2 tahun sebagai perbandingan</sub>

**Pembahasan:** $\frac{FV_4}{FV_2} = \frac{(1,2^4 - 1)/0,2}{(1,2^2 - 1)/0,2} = \frac{5,368}{2,2} = 2,44$. Karena 2,44 > 2, klaim Bayu keliru.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b02-c-hard-bt01-017
*orisinal | C6 | 4 langkah | jenis: rancang setoran dengan deposit awal*

Eko mendepositokan Rp1.000.000,00 hari ini, lalu menyetor sejumlah yang sama pada akhir setiap tahun selama 3 tahun ke bank yang sama berbunga majemuk 10% per tahun. Ia menginginkan saldo tepat setelah setoran ketiga sebesar Rp6.296.000,00. Besar setoran tahunan yang harus dilakukan adalah ....

- A. Rp1.600.000,00  
  <sub>Salah: deposit awal tidak dibungakan: (6.296.000 - 1.000.000) : 3,31</sub>
- **B. Rp1.500.000,00** ✅  
  <sub>Benar: deposit awal menjadi 1.000.000 x 1,331 = 1.331.000; sisa 4.965.000 : 3,31 = 1.500.000</sub>
- C. Rp1.655.000,00  
  <sub>Salah: setoran tidak dibungakan: (6.296.000 - 1.331.000) : 3</sub>
- D. Rp1.902.115,00  
  <sub>Salah: lupa memperhitungkan deposit awal: 6.296.000 : 3,31</sub>

**Pembahasan:** $1.000.000 \times 1,1^3 + A \times 3,31 = 6.296.000$, sehingga $1.331.000 + 3,31A = 6.296.000$ dan $A = 4.965.000 : 3,31 = 1.500.000$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
