# Lembar koreksi — kelas12 SMA12U-B1 subbab C: Bunga Tunggal

41 soal | easy 13, medium 15, hard 13 | variasi 10, orisinal 31
> **Kapasitas kurang (easy): 13 dari kuota 20** — Subbab C (Bunga Tunggal) hanya selebar p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5 Angga), rumus B = M x p% x n, dan Contoh 1.9 (Zaka), tanpa Latihan bernomor. Acuan pretest hanya 2 soal (4 variasi) ditambah Contoh 1.9 (2 variasi); UK 6 (cicilan) 3 langkah sehingga melebihi easy. Lebih dari 13 soal easy akan nyaris kembar.
> **Kapasitas kurang (medium): 15 dari kuota 20** — Subbab C (Bunga Tunggal) hanya p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5), rumus B = M x p% x n, dan Contoh 1.9, tanpa Latihan bernomor. Acuan variasi layak untuk medium hanya UK 6 (cicilan Raka) dan Contoh 1.9 (masing-masing maks 2); acuan pretest lain bertaraf easy dan sudah dipakai di easy. Sudut medium orisinal (cari n/p/M dari saldo, bandingkan simpanan, barisan dan deret nilai uang, satuan bulan, angsuran) sudah terpakai; tambahan akan nyaris kembar.
> **Kapasitas kurang (hard): 13 dari kuota 20** — Subbab C (Bunga Tunggal) hanya p48-p50 Buku Siswa: satu eksplorasi (Tabel 1.5), rumus B = M x p% x n, dan Contoh 1.9, tanpa Latihan bernomor. Penalaran hard yang layak (evaluasi klaim, temukan kesalahan, contoh penyangkal, rancang modal/lama, perbandingan skema bunga dan cicilan, parameter dua simpanan) sudah terpakai dalam 13 soal; semua acuan variasi sudah habis di easy/medium sehingga seluruh soal orisinal. Tambahan akan nyaris kembar atau keluar materi (bunga majemuk, bukan bagian subbab).

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b01-c-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: bunga tunggal pada tahun tertentu*

Dina menabung uang sebesar Rp3.500.000,00 di sebuah bank. Bank memberikan bunga tunggal tetap sebesar 6% setiap tahun dari saldo awal. Besar bunga yang diterima Dina pada tahun ketiga adalah ....

- **A. Rp210.000,00** ✅  
  <sub>Benar: bunga tunggal selalu dihitung dari modal awal: 6% x Rp3.500.000,00 = Rp210.000,00 setiap tahun</sub>
- B. Rp21.000,00  
  <sub>Salah: salah menaruh koma desimal, memakai 0,6% bukan 6%</sub>
- C. Rp630.000,00  
  <sub>Salah: mengalikan bunga setahun dengan nomor tahun (3 x Rp210.000,00)</sub>
- D. Rp235.956,00  
  <sub>Salah: menghitung bunga dari saldo akhir tahun sebelumnya (bunga majemuk), padahal bunga tunggal dari modal awal</sub>

**Pembahasan:** Bunga tunggal tiap tahun sama: $B = M \times p\% = 3.500.000 \times 0,06 = 210.000$. Tahun ketiga tetap Rp210.000,00.
**Acuan:** pretest — kelas12-b01-p0049-ayo-bereksplorasi-bunga-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b01-c-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: bunga tunggal pada tahun tertentu*

Pak Hendra menyimpan Rp8.000.000,00 di koperasi pegawai. Koperasi itu menetapkan bunga tunggal 3% per tahun yang dihitung dari simpanan awal. Berapa rupiah bunga yang diterima Pak Hendra pada tahun kedua?

- A. Rp247.200,00  
  <sub>Salah: bunga tahun kedua dihitung dari saldo tahun pertama (bunga majemuk)</sub>
- B. Rp480.000,00  
  <sub>Salah: mengalikan bunga setahun dengan 2 karena tahun kedua</sub>
- C. Rp24.000,00  
  <sub>Salah: salah menaruh koma desimal, memakai 0,3% bukan 3%</sub>
- **D. Rp240.000,00** ✅  
  <sub>Benar: bunga tunggal dihitung dari simpanan awal: 3% x Rp8.000.000,00 = Rp240.000,00</sub>

**Pembahasan:** $B = M \times p\% = 8.000.000 \times 0,03 = 240.000$ untuk setiap tahun.
**Acuan:** pretest — kelas12-b01-p0049-ayo-bereksplorasi-bunga-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b01-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: nilai tabungan akhir tahun*

Rina menabung Rp4.000.000,00 di bank yang memberi bunga tunggal tetap 3% setiap tahun dari saldo awal. Bunga ditambahkan ke saldo setiap akhir tahun. Nilai total tabungan Rina pada akhir tahun ketiga adalah ....

- **A. Rp4.360.000,00** ✅  
  <sub>Benar: bunga tetap Rp120.000,00 per tahun, selama 3 tahun Rp360.000,00, sehingga total Rp4.360.000,00</sub>
- B. Rp4.120.000,00  
  <sub>Salah: hanya menambahkan bunga satu tahun</sub>
- C. Rp360.000,00  
  <sub>Salah: lupa menambahkan modal awal, hanya bunga tiga tahun</sub>
- D. Rp4.370.908,00  
  <sub>Salah: memakai bunga majemuk (bunga dihitung dari saldo tahun sebelumnya)</sub>

**Pembahasan:** Bunga per tahun: $4.000.000 \times 0,03 = 120.000$. Setelah 3 tahun: $4.000.000 + 3 \times 120.000 = 4.360.000$.
**Acuan:** pretest — kelas12-b01-p0049-ayo-bereksplorasi-bunga-2-nilai

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b01-c-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: nilai tabungan akhir tahun*

Bu Sari menyetor Rp4.500.000,00 pada tabungan koperasi sekolah dengan bunga tunggal 8% per tahun. Selama lima tahun ia tidak menarik uangnya. Berapa saldo Bu Sari setelah lima tahun?

- A. Rp1.800.000,00  
  <sub>Salah: lupa menambahkan modal awal, hanya bunga lima tahun</sub>
- B. Rp6.611.976,00  
  <sub>Salah: memakai bunga majemuk, bunga dihitung dari saldo yang terus bertambah</sub>
- **C. Rp6.300.000,00** ✅  
  <sub>Benar: bunga lima tahun 5 x Rp360.000,00 = Rp1.800.000,00, ditambah modal menjadi Rp6.300.000,00</sub>
- D. Rp4.860.000,00  
  <sub>Salah: hanya menambahkan bunga satu tahun</sub>

**Pembahasan:** $B = 4.500.000 \times 0,08 \times 5 = 1.800.000$; saldo $= 4.500.000 + 1.800.000 = 6.300.000$.
**Acuan:** pretest — kelas12-b01-p0049-ayo-bereksplorasi-bunga-2-nilai

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b01-c-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: total simpanan dengan rumus B = M x p% x n*

Salsa memulai usaha kecil-kecilan kue kering dan memperoleh keuntungan pertama sebesar Rp6.000.000,00. Uang tersebut ia simpan di koperasi desa yang memberikan bunga tunggal sebesar 4% per tahun. Bunga diberikan sekali setahun dan langsung ditambahkan ke total simpanan sebelumnya. Berapa total uang yang didapatkan Salsa selama 3 tahun?

- A. Rp720.000,00  
  <sub>Salah: hanya menjawab besar bunga, lupa menambahkan modal awal</sub>
- B. Rp6.240.000,00  
  <sub>Salah: hanya menambahkan bunga untuk satu tahun</sub>
- C. Rp6.749.184,00  
  <sub>Salah: memakai bunga majemuk (dipangkatkan) padahal bunga tunggal</sub>
- **D. Rp6.720.000,00** ✅  
  <sub>Benar: B = 6.000.000 x 0,04 x 3 = 720.000; total = 6.000.000 + 720.000 = 6.720.000</sub>

**Pembahasan:** $B = M \times p\% \times n = 6.000.000 \times 0,04 \times 3 = 720.000$. Total $= 6.000.000 + 720.000 = 6.720.000$.
**Acuan:** siswa — siswa hal.49 Contoh 1.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b01-c-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: total pinjaman dengan bunga tunggal*

Bu Tari meminjam Rp8.000.000,00 dari sebuah koperasi untuk menambah modal warungnya. Koperasi menetapkan bunga tunggal 3% per tahun dari pinjaman awal. Jika Bu Tari melunasi seluruh pinjaman beserta bunganya sekaligus setelah 2 tahun, berapa rupiah yang harus ia bayarkan?

- A. Rp8.240.000,00  
  <sub>Salah: hanya menghitung bunga untuk satu tahun</sub>
- **B. Rp8.480.000,00** ✅  
  <sub>Benar: bunga 2 tahun = Rp480.000,00, ditambah pokok pinjaman menjadi Rp8.480.000,00</sub>
- C. Rp8.487.200,00  
  <sub>Salah: memakai bunga majemuk (bunga berbunga) padahal bunga tunggal</sub>
- D. Rp480.000,00  
  <sub>Salah: hanya membayar bunga, lupa pokok pinjaman</sub>

**Pembahasan:** $B = 8.000.000 \times 0,03 \times 2 = 480.000$. Total bayar $= 8.000.000 + 480.000 = 8.480.000$.
**Acuan:** siswa — siswa hal.49 Contoh 1.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b01-c-easy-bt01-007
*orisinal | C2 | 2 langkah | jenis: jenis barisan nilai tabungan*

Sebuah tabungan Rp2.000.000,00 mendapat bunga tunggal 5% per tahun dari modal awal. Nilai uang pada akhir tahun pertama, kedua, ketiga, dan seterusnya membentuk barisan yang tepat dijelaskan sebagai ....

- **A. aritmetika dengan beda Rp100.000,00** ✅  
  <sub>Benar: bunga tiap tahun tetap Rp100.000,00 sehingga selisih nilai uang antartahun selalu sama</sub>
- B. geometri dengan rasio 0,05  
  <sub>Salah: menganggap rasio sama dengan persen bunga</sub>
- C. aritmetika dengan beda Rp2.000.000,00  
  <sub>Salah: mengira beda sama dengan modal awal</sub>
- D. geometri dengan rasio 1,05  
  <sub>Salah: mengira bunga berbunga (majemuk) sehingga nilai uang dikali 1,05 tiap tahun</sub>

**Pembahasan:** Bunga tiap tahun $2.000.000 \times 0,05 = 100.000$, tetap. Nilai uang: 2.100.000; 2.200.000; 2.300.000; ... adalah barisan aritmetika dengan beda 100.000.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b01-c-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: definisi bunga simpanan*

Menurut Otoritas Jasa Keuangan, bunga simpanan adalah ....

- A. biaya yang harus dibayar nasabah kepada bank untuk membuka rekening  
  <sub>Salah: mengira bunga sama dengan biaya administrasi</sub>
- **B. balas jasa dari bank kepada nasabah karena nasabah menyimpan uangnya di bank** ✅  
  <sub>Benar: definisi bunga simpanan pada buku: balas jasa bank kepada penyimpan dana</sub>
- C. balas jasa yang ditetapkan bank kepada peminjam atas pinjaman yang diperolehnya  
  <sub>Salah: tertukar dengan definisi bunga pinjaman</sub>
- D. pajak yang dipungut pemerintah dari uang yang disimpan nasabah di bank  
  <sub>Salah: mengira bunga sama dengan pajak simpanan</sub>

**Pembahasan:** Bunga simpanan adalah balas jasa dari bank kepada nasabah atas jasa nasabah menyimpan uangnya di bank. Balas jasa kepada peminjam disebut bunga pinjaman.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b01-c-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: menghitung besar bunga dengan rumus*

Pak Danu menyimpan Rp5.000.000,00 pada sebuah bank yang memberi bunga tunggal 6% per tahun. Besar bunga yang diperoleh Pak Danu selama 3 tahun adalah ....

- A. Rp955.080,00  
  <sub>Salah: memakai bunga majemuk</sub>
- B. Rp300.000,00  
  <sub>Salah: hanya menghitung bunga untuk satu tahun</sub>
- C. Rp90.000,00  
  <sub>Salah: salah menaruh koma desimal, memakai 0,6% bukan 6%</sub>
- **D. Rp900.000,00** ✅  
  <sub>Benar: B = M x p% x n = 5.000.000 x 0,06 x 3 = 900.000</sub>

**Pembahasan:** $B = M \times p\% \times n = 5.000.000 \times 0,06 \times 3 = 900.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b01-c-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: sifat bunga tunggal tetap tiap tahun*

Rafi menabung Rp2.000.000,00 dengan bunga tunggal 4% per tahun dari saldo awal. Besar bunga yang diterima Rafi pada tahun ke-4 adalah ....

- A. Rp8.000,00  
  <sub>Salah: salah menaruh koma desimal, memakai 0,4% bukan 4%</sub>
- B. Rp320.000,00  
  <sub>Salah: mengalikan bunga setahun dengan nomor tahun ke-4</sub>
- **C. Rp80.000,00** ✅  
  <sub>Benar: bunga tunggal tetap tiap tahun: 4% x 2.000.000 = 80.000</sub>
- D. Rp89.989,00  
  <sub>Salah: menghitung dari saldo tahun sebelumnya (bunga majemuk)</sub>

**Pembahasan:** Bunga tunggal selalu dari modal awal: $2.000.000 \times 0,04 = 80.000$, sama untuk tahun ke-1 sampai ke-4.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b01-c-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: nilai tabungan akhir tahun*

Kirana menabung Rp2.000.000,00 dengan bunga tunggal 3% per tahun. Bunga ditambahkan ke saldo setiap akhir tahun dan uang tidak pernah diambil. Saldo tabungan Kirana pada akhir tahun keenam adalah ....

- A. Rp2.300.000,00  
  <sub>Salah: salah menghitung lama menabung sebagai 5 tahun</sub>
- B. Rp2.388.105,00  
  <sub>Salah: memakai bunga majemuk</sub>
- **C. Rp2.360.000,00** ✅  
  <sub>Benar: bunga 6 tahun = 6 x 60.000 = 360.000; saldo = 2.000.000 + 360.000</sub>
- D. Rp2.060.000,00  
  <sub>Salah: hanya menambahkan bunga satu tahun</sub>

**Pembahasan:** Bunga tahunan $2.000.000 \times 0,03 = 60.000$. Saldo akhir tahun ke-6 $= 2.000.000 + 6 \times 60.000 = 2.360.000$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b01-c-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: mencari persentase bunga*

Seorang nasabah menyimpan Rp2.500.000,00 selama 3 tahun dan memperoleh total bunga tunggal Rp375.000,00. Persentase bunga tunggal per tahun yang diberikan bank adalah ....

- **A. 5%** ✅  
  <sub>Benar: p% = B : (M x n) = 375.000 : 7.500.000 = 0,05 = 5%</sub>
- B. 15%  
  <sub>Salah: lupa membagi dengan lama simpanan (3 tahun)</sub>
- C. 0,5%  
  <sub>Salah: salah menaruh koma desimal pada hasil 0,05</sub>
- D. 45%  
  <sub>Salah: mengalikan dengan 3 bukan membagi dengan 3</sub>

**Pembahasan:** $B = M \times p\% \times n \Rightarrow p\% = \frac{375.000}{2.500.000 \times 3} = 0,05 = 5\%$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b01-c-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: mencari modal awal*

Dengan bunga tunggal 6% per tahun, seorang nasabah memperoleh bunga Rp360.000,00 setelah menyimpan uang selama 2 tahun. Besar uang yang ia simpan di awal adalah ....

- A. Rp12.000.000,00  
  <sub>Salah: mengalikan dengan 2 alih-alih membagi</sub>
- **B. Rp3.000.000,00** ✅  
  <sub>Benar: M = B : (p% x n) = 360.000 : 0,12 = 3.000.000</sub>
- C. Rp43.200,00  
  <sub>Salah: mengalikan bunga dengan 12% bukan membaginya</sub>
- D. Rp6.000.000,00  
  <sub>Salah: lupa memperhitungkan lama simpanan 2 tahun (membagi 6% saja)</sub>

**Pembahasan:** $M = \frac{B}{p\% \times n} = \frac{360.000}{0,06 \times 2} = 3.000.000$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [medium] kelas12-b01-c-medium-bt01-001
*variasi (angka) | C3 | 4 langkah | jenis: cicilan bulanan pinjaman bunga tunggal*

Dimas mengikuti program Young Business Camp di sekolahnya. Untuk membeli peralatan produksi awal, ia memperoleh dana talangan usaha sebesar Rp3.600.000,00 dari koperasi pemuda. Koperasi tersebut menerapkan bunga sederhana sebesar 5% per tahun dan memberikan keringanan berupa angsuran bulanan tetap selama 3 tahun agar peserta tidak terbebani. Dimas perlu menghitung besar cicilan bulanan agar pinjaman lunas sesuai perjanjian. Berapakah cicilan yang harus dibayarkan Dimas setiap bulan?

- A. Rp345.000,00  
  <sub>Salah: membagi total dengan 12, lupa bahwa 3 tahun adalah 36 bulan</sub>
- B. Rp105.000,00  
  <sub>Salah: menghitung bunga hanya untuk 1 tahun lalu membagi 36 bulan</sub>
- **C. Rp115.000,00** ✅  
  <sub>Benar: B = 3.600.000 x 0,05 x 3 = 540.000; total 4.140.000; dibagi 36 bulan = 115.000</sub>
- D. Rp100.000,00  
  <sub>Salah: lupa menambahkan bunga, hanya membagi pokok dengan 36 bulan</sub>

**Pembahasan:** $B = 3.600.000 \times 0,05 \times 3 = 540.000$. Total $= 3.600.000 + 540.000 = 4.140.000$. Cicilan $= 4.140.000 : 36 = 115.000$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [medium] kelas12-b01-c-medium-bt01-002
*variasi (konteks) | C3 | 4 langkah | jenis: cicilan bulanan pinjaman bunga tunggal*

Bu Wulan membutuhkan modal untuk membeli mesin jahit sehingga ia meminjam uang Rp9.000.000,00 pada sebuah koperasi. Koperasi mengenakan bunga tunggal 6% per tahun. Pinjaman itu harus dilunasi dengan angsuran yang sama besar setiap bulan selama 18 bulan. Besar angsuran yang dibayar Bu Wulan tiap bulan adalah ....

- A. Rp500.000,00  
  <sub>Salah: lupa menambahkan bunga ke pokok pinjaman</sub>
- **B. Rp545.000,00** ✅  
  <sub>Benar: lama pinjaman 1,5 tahun: B = 9.000.000 x 0,06 x 1,5 = 810.000; total 9.810.000; dibagi 18 = 545.000</sub>
- C. Rp530.000,00  
  <sub>Salah: menghitung bunga hanya untuk 1 tahun, bukan 1,5 tahun</sub>
- D. Rp1.040.000,00  
  <sub>Salah: memperlakukan 18 bulan sebagai 18 tahun dalam rumus bunga</sub>

**Pembahasan:** $n = 18 : 12 = 1,5$ tahun. $B = 9.000.000 \times 0,06 \times 1,5 = 810.000$. Total $= 9.810.000$. Angsuran $= 9.810.000 : 18 = 545.000$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas12-b01-c-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: total simpanan dengan persentase desimal*

Dika memenangkan lomba desain poster dan memperoleh hadiah pertama sebesar Rp12.000.000,00. Uang tersebut ia simpan di koperasi sekolah yang memberikan bunga tunggal sebesar 7,5% per tahun. Bunga diberikan sekali setahun dan langsung ditambahkan ke total simpanan sebelumnya. Berapa total uang yang didapatkan Dika selama 6 tahun?

- **A. Rp17.400.000,00** ✅  
  <sub>Benar: B = 12.000.000 x 0,075 x 6 = 5.400.000; total = 12.000.000 + 5.400.000 = 17.400.000</sub>
- B. Rp12.900.000,00  
  <sub>Salah: hanya menambahkan bunga untuk satu tahun</sub>
- C. Rp18.519.618,00  
  <sub>Salah: memakai bunga majemuk (dipangkatkan) padahal bunga tunggal</sub>
- D. Rp5.400.000,00  
  <sub>Salah: hanya menjawab bunga, lupa menambah modal awal</sub>

**Pembahasan:** $B = 12.000.000 \times 0,075 \times 6 = 5.400.000$. Total $= 12.000.000 + 5.400.000 = 17.400.000$.
**Acuan:** siswa — siswa hal.49 Contoh 1.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas12-b01-c-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: total simpanan dengan lama dalam bulan*

Tamara menerima honor pertama dari menulis cerpen sebesar Rp8.000.000,00 lalu menabungkannya di sebuah bank. Bank itu membayar bunga tunggal 6% per tahun, dan bunganya digabung ke saldo tabungan. Jika Tamara tidak mengambil uangnya, saldo tabungan setelah 30 bulan adalah ....

- A. Rp1.200.000,00  
  <sub>Salah: hanya menghitung bunga, lupa menambah modal</sub>
- B. Rp9.440.000,00  
  <sub>Salah: membulatkan 2,5 tahun menjadi 3 tahun</sub>
- **C. Rp9.200.000,00** ✅  
  <sub>Benar: 30 bulan = 2,5 tahun; B = 8.000.000 x 0,06 x 2,5 = 1.200.000; saldo = 9.200.000</sub>
- D. Rp22.400.000,00  
  <sub>Salah: memakai 30 sebagai banyak tahun, bukan bulan</sub>

**Pembahasan:** $n = 30 : 12 = 2,5$ tahun. $B = 8.000.000 \times 0,06 \times 2,5 = 1.200.000$. Saldo $= 8.000.000 + 1.200.000 = 9.200.000$.
**Acuan:** siswa — siswa hal.49 Contoh 1.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas12-b01-c-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: mencari lama menabung*

Eko menabung Rp5.000.000,00 di bank dengan bunga tunggal 6% per tahun. Bunga ditambahkan ke saldo setiap akhir tahun dan uang tidak pernah diambil. Saldo tabungan Eko menjadi Rp6.200.000,00 setelah menabung selama ... tahun.

- A. 5  
  <sub>Salah: menambah 1 tahun karena mengira tahun pertama belum berbunga</sub>
- B. 2  
  <sub>Salah: memakai p = 12% sehingga bunga setahun 600.000</sub>
- C. 40  
  <sub>Salah: memakai p = 0,6% (salah menaruh koma) sehingga bunga setahun 30.000</sub>
- **D. 4** ✅  
  <sub>Benar: bunga total = 6.200.000 - 5.000.000 = 1.200.000; bunga setahun 300.000; n = 1.200.000 : 300.000 = 4</sub>

**Pembahasan:** $B = 6.200.000 - 5.000.000 = 1.200.000$. $B = M \times p\% \times n \Rightarrow n = \frac{1.200.000}{5.000.000 \times 0,06} = 4$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas12-b01-c-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: mencari persentase dari saldo akhir*

Sinta menabung Rp4.000.000,00 di sebuah bank. Bunga tunggal tetap ditambahkan ke saldo setiap akhir tahun. Pada akhir tahun kelima, saldo tabungan Sinta menjadi Rp5.000.000,00. Persentase bunga tunggal per tahun yang diberikan bank adalah ....

- A. 4%  
  <sub>Salah: membagi bunga dengan saldo akhir, bukan modal awal</sub>
- B. 20%  
  <sub>Salah: membagi bunga dengan saldo akhir tanpa memperhitungkan lama menabung</sub>
- **C. 5%** ✅  
  <sub>Benar: B = 5.000.000 - 4.000.000 = 1.000.000; p% = 1.000.000 : (4.000.000 x 5) = 0,05</sub>
- D. 25%  
  <sub>Salah: lupa membagi dengan lama menabung 5 tahun</sub>

**Pembahasan:** $B = 5.000.000 - 4.000.000 = 1.000.000$. $p\% = \frac{B}{M \times n} = \frac{1.000.000}{4.000.000 \times 5} = 0,05 = 5\%$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas12-b01-c-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: mencari modal dari saldo akhir*

Pak Rahmat menyimpan sejumlah uang di koperasi dengan bunga tunggal 8% per tahun. Bunga ditambahkan ke saldo setiap akhir tahun. Setelah 4 tahun, total uang Pak Rahmat menjadi Rp7.920.000,00. Besar uang yang ia simpan pada awal adalah ....

- A. Rp6.336.000,00  
  <sub>Salah: memakai 0,8 sebagai pengali (salah menaruh koma desimal)</sub>
- B. Rp5.385.600,00  
  <sub>Salah: menghitung 32% dari saldo akhir lalu mengurangkannya, padahal 32% adalah dari modal awal</sub>
- **C. Rp6.000.000,00** ✅  
  <sub>Benar: total = M + M x 0,08 x 4 = 1,32M = 7.920.000, sehingga M = 6.000.000</sub>
- D. Rp7.286.400,00  
  <sub>Salah: hanya mengurangkan bunga satu tahun (8%) dari saldo akhir</sub>

**Pembahasan:** Total $= M + M \times 0,08 \times 4 = 1,32M$. Jadi $M = \frac{7.920.000}{1,32} = 6.000.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b01-c-medium-bt01-008
*orisinal | C4 | 4 langkah | jenis: membandingkan dua simpanan*

Dewi menyimpan Rp10.000.000,00 selama 4 tahun dengan bunga tunggal 5% per tahun. Eka menyimpan Rp8.000.000,00 selama 5 tahun dengan bunga tunggal 6% per tahun. Selisih total bunga yang diterima Eka dan Dewi adalah ....

- **A. Rp400.000,00** ✅  
  <sub>Benar: bunga Dewi 2.000.000, bunga Eka 2.400.000, selisih 400.000</sub>
- B. Rp2.400.000,00  
  <sub>Salah: hanya menulis bunga Eka tanpa mengurangi bunga Dewi</sub>
- C. Rp4.400.000,00  
  <sub>Salah: menjumlahkan kedua bunga, bukan mencari selisih</sub>
- D. Rp20.000,00  
  <sub>Salah: membandingkan bunga satu tahun saja (480.000 dan 500.000)</sub>

**Pembahasan:** Dewi: $10.000.000 \times 0,05 \times 4 = 2.000.000$. Eka: $8.000.000 \times 0,06 \times 5 = 2.400.000$. Selisih $= 400.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b01-c-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: suku ke-n barisan nilai uang*

Dewa menabung Rp3.000.000,00 dengan bunga tunggal 4% per tahun dari modal awal. Nilai uang pada akhir tahun pertama, kedua, ketiga, dan seterusnya membentuk barisan aritmetika. Nilai uang Dewa pada akhir tahun ke-10 adalah ....

- A. Rp4.320.000,00  
  <sub>Salah: memakai U1 + 10b, padahal suku ke-10 adalah U1 + 9b</sub>
- B. Rp4.080.000,00  
  <sub>Salah: mengira suku pertama adalah modal awal sehingga U10 = modal + 9b</sub>
- C. Rp1.200.000,00  
  <sub>Salah: hanya menghitung total bunga 10 tahun, lupa modal awal</sub>
- **D. Rp4.200.000,00** ✅  
  <sub>Benar: U1 = 3.120.000, beda = 120.000, U10 = 3.120.000 + 9 x 120.000 = 4.200.000</sub>

**Pembahasan:** $U_1 = 3.000.000 + 120.000 = 3.120.000$ dan $b = 120.000$. $U_{10} = U_1 + 9b = 3.120.000 + 9 \times 120.000 = 4.200.000$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b01-c-medium-bt01-010
*orisinal | C4 | 4 langkah | jenis: deret nilai uang*

Nilai uang pada akhir setiap tahun dari tabungan Rp2.000.000,00 dengan bunga tunggal 5% per tahun membentuk barisan aritmetika. Jumlah kelima nilai uang itu, yaitu dari akhir tahun pertama sampai akhir tahun kelima, adalah ....

- A. Rp12.500.000,00  
  <sub>Salah: menganggap kelima nilai uang sama dengan U5 (5 x 2.500.000)</sub>
- **B. Rp11.500.000,00** ✅  
  <sub>Benar: U1 = 2.100.000, beda 100.000, U5 = 2.500.000; S5 = 5/2 x (2.100.000 + 2.500.000) = 11.500.000</sub>
- C. Rp10.500.000,00  
  <sub>Salah: menganggap kelima nilai uang sama dengan U1 (5 x 2.100.000)</sub>
- D. Rp11.000.000,00  
  <sub>Salah: memakai modal awal 2.000.000 sebagai suku pertama</sub>

**Pembahasan:** $U_1 = 2.100.000$, $b = 100.000$, $U_5 = 2.500.000$. $S_5 = \frac{5}{2}(2.100.000 + 2.500.000) = 11.500.000$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b01-c-medium-bt01-011
*orisinal | C3 | 2 langkah | jenis: bunga dengan lama dalam bulan*

Pak Hasan menabung Rp9.000.000,00 dengan bunga tunggal 6% per tahun. Besar bunga yang diperoleh Pak Hasan setelah 8 bulan adalah ....

- A. Rp4.320.000,00  
  <sub>Salah: memakai 8 sebagai banyak tahun</sub>
- B. Rp540.000,00  
  <sub>Salah: menghitung bunga satu tahun penuh</sub>
- C. Rp45.000,00  
  <sub>Salah: hanya menghitung bunga satu bulan</sub>
- **D. Rp360.000,00** ✅  
  <sub>Benar: n = 8/12 tahun; B = 9.000.000 x 0,06 x 8/12 = 360.000</sub>

**Pembahasan:** $n = \frac{8}{12}$ tahun. $B = 9.000.000 \times 0,06 \times \frac{8}{12} = 360.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b01-c-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: persentase bunga dari angsuran*

Rudi meminjam Rp5.000.000,00 dari koperasi dengan bunga tunggal. Ia melunasinya dengan angsuran tetap Rp275.000,00 setiap bulan selama 2 tahun. Persentase bunga tunggal per tahun yang dikenakan koperasi adalah ....

- A. 32%  
  <sub>Salah: lupa membagi dengan lama pinjaman 2 tahun</sub>
- **B. 16%** ✅  
  <sub>Benar: total bayar = 24 x 275.000 = 6.600.000; bunga = 1.600.000; p% = 1.600.000 : (5.000.000 x 2) = 16%</sub>
- C. 66%  
  <sub>Salah: memakai total pembayaran 6.600.000 sebagai bunga</sub>
- D. 132%  
  <sub>Salah: membagi total pembayaran dengan pokok, bukan bunga dengan pokok</sub>

**Pembahasan:** Total bayar $= 24 \times 275.000 = 6.600.000$. Bunga $= 6.600.000 - 5.000.000 = 1.600.000$. $p\% = \frac{1.600.000}{5.000.000 \times 2} = 16\%$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b01-c-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: modal dari dua data saldo*

Saldo sebuah tabungan dengan bunga tunggal adalah Rp5.600.000,00 pada akhir tahun kedua dan Rp6.500.000,00 pada akhir tahun kelima. Bunga ditambahkan ke saldo setiap akhir tahun. Besar uang yang disetorkan pada awal adalah ....

- **A. Rp5.000.000,00** ✅  
  <sub>Benar: selisih 3 tahun = 900.000, bunga setahun 300.000; modal = 5.600.000 - 2 x 300.000 = 5.000.000</sub>
- B. Rp5.900.000,00  
  <sub>Salah: menambah bunga satu tahun, bukan mengurangi</sub>
- C. Rp4.700.000,00  
  <sub>Salah: mengurangi bunga tiga tahun dari saldo tahun kedua</sub>
- D. Rp5.300.000,00  
  <sub>Salah: hanya mengurangi bunga satu tahun dari saldo tahun kedua</sub>

**Pembahasan:** Beda $= \frac{6.500.000 - 5.600.000}{3} = 300.000$ per tahun. Modal $= 5.600.000 - 2 \times 300.000 = 5.000.000$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b01-c-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: waktu saldo dua tabungan sama*

Ali menabung Rp8.000.000,00 dengan bunga tunggal 5% per tahun. Budi menabung Rp6.000.000,00 dengan bunga tunggal 10% per tahun. Keduanya tidak pernah menarik uang. Saldo tabungan keduanya akan sama besar setelah ... tahun.

- **A. 10** ✅  
  <sub>Benar: 8.000.000 + 400.000n = 6.000.000 + 600.000n, sehingga n = 10</sub>
- B. 20  
  <sub>Salah: membagi selisih modal dengan 100.000 (salah menghitung selisih bunga tahunan)</sub>
- C. 15  
  <sub>Salah: menjumlahkan persentase bunga 5 dan 10</sub>
- D. 5  
  <sub>Salah: membagi selisih modal 2.000.000 dengan bunga setahun Ali saja</sub>

**Pembahasan:** Bunga setahun Ali $= 400.000$, Budi $= 600.000$. $8.000.000 + 400.000n = 6.000.000 + 600.000n \Rightarrow 200.000n = 2.000.000 \Rightarrow n = 10$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b01-c-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: simpanan terpisah di dua bank*

Bu Lina membagi uangnya Rp12.000.000,00 menjadi dua simpanan. Rp7.000.000,00 disimpan di Bank A dengan bunga tunggal 4% per tahun, dan sisanya disimpan di Bank B dengan bunga tunggal 6% per tahun. Total bunga dari kedua bank setelah 3 tahun adalah ....

- A. Rp1.800.000,00  
  <sub>Salah: memakai persentase rata-rata 5% untuk seluruh uang</sub>
- B. Rp580.000,00  
  <sub>Salah: hanya menghitung bunga satu tahun</sub>
- C. Rp1.440.000,00  
  <sub>Salah: menganggap seluruh uang berbunga 4%</sub>
- **D. Rp1.740.000,00** ✅  
  <sub>Benar: Bank A: 7.000.000 x 0,04 x 3 = 840.000; Bank B: 5.000.000 x 0,06 x 3 = 900.000; total 1.740.000</sub>

**Pembahasan:** Bank A: $7.000.000 \times 0,04 \times 3 = 840.000$. Bank B: $5.000.000 \times 0,06 \times 3 = 900.000$. Total $= 1.740.000$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [hard] kelas12-b01-c-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan tentang tabungan*

Dewi menabung Rp4.000.000,00 dengan bunga tunggal 5% per tahun dari saldo awal. Bunga ditambahkan ke saldo setiap akhir tahun dan uang tidak pernah diambil. Pernyataan yang benar tentang tabungan Dewi adalah ....

- **A. Saldo menjadi tepat dua kali modal pada akhir tahun ke-20.** ✅  
  <sub>Benar: bunga tiap tahun tetap 200.000; saldo = 4.000.000 + 200.000n = 8.000.000 saat n = 20</sub>
- B. Saldo akhir tahun ke-10 adalah Rp8.000.000,00.  
  <sub>Salah: memakai 10% per tahun sehingga bunga 10 tahun dianggap 4.000.000</sub>
- C. Bunga yang diterima pada tahun ke-10 sepuluh kali bunga tahun pertama.  
  <sub>Salah: mengira bunga bertambah tiap tahun, padahal bunga tunggal tetap Rp200.000</sub>
- D. Saldo menjadi dua kali modal pada akhir tahun ke-10.  
  <sub>Salah: mengira 5% x 10 tahun sudah 100% dari modal</sub>

**Pembahasan:** Bunga per tahun $= 4.000.000 \times 0,05 = 200.000$ dan tetap. Saldo akhir tahun ke-$n$ $= 4.000.000 + 200.000n$. Tahun ke-10: 6.000.000 (bukan 8.000.000). Saldo 8.000.000 tercapai saat $n = 20$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [hard] kelas12-b01-c-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan satuan waktu*

Seorang siswa menghitung saldo tabungan Rp5.000.000,00 yang berbunga tunggal 6% per tahun setelah 9 bulan dengan cara berikut: $B = 5.000.000 \times 0,06 \times 9 = 2.700.000$, sehingga saldo akhir $= 5.000.000 + 2.700.000 = 7.700.000$. Kesalahan penyelesaian siswa tersebut adalah ....

- **A. Lama 9 bulan tidak diubah ke tahun; seharusnya $n = \frac{9}{12}$ sehingga bunganya Rp225.000,00.** ✅  
  <sub>Benar: persentase per tahun sehingga n harus dalam tahun: 9/12 = 0,75; B = 5.000.000 x 0,06 x 0,75 = 225.000</sub>
- B. Persentase 6% seharusnya ditulis 0,6 sehingga bunganya Rp27.000.000,00.  
  <sub>Salah: salah mengubah persen ke desimal</sub>
- C. Rumus yang benar adalah $B = M \times p\% : n$ sehingga bunganya Rp33.333,00.  
  <sub>Salah: mengubah rumus bunga tunggal menjadi pembagian</sub>
- D. Modal awal tidak boleh ditambahkan ke bunga sehingga saldo akhirnya Rp2.700.000,00.  
  <sub>Salah: mengira saldo hanya berisi bunga</sub>

**Pembahasan:** $p\%$ per tahun, sehingga $n$ harus dalam tahun: $n = \frac{9}{12} = 0,75$. $B = 5.000.000 \times 0,06 \times 0,75 = 225.000$ dan saldo $= 5.225.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas12-b01-c-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: evaluasi dua rumus suku ke-n*

Tabungan Rp5.000.000,00 berbunga tunggal 4% per tahun, dengan bunga ditambahkan ke saldo setiap akhir tahun. Nilai uang pada akhir tahun ke-$n$ dinyatakan Dani dengan $U_n = 5.200.000 + 200.000(n-1)$ dan dinyatakan Eka dengan $U_n = 5.000.000 + 200.000n$. Pernyataan yang benar tentang rumus Dani dan Eka adalah ....

- A. Keduanya salah karena nilai uang membentuk barisan geometri.  
  <sub>Salah: mengira nilai uang bunga tunggal berpola rasio tetap</sub>
- **B. Keduanya benar karena menghasilkan nilai yang sama untuk setiap $n$.** ✅  
  <sub>Benar: 5.200.000 + 200.000(n-1) = 5.000.000 + 200.000n; keduanya barisan aritmetika dengan U1 = 5.200.000 dan b = 200.000</sub>
- C. Hanya rumus Dani yang benar karena suku pertama barisan harus 5.200.000.  
  <sub>Salah: mengira rumus Eka menghasilkan suku pertama 5.000.000, padahal $U_1 = 5.200.000$</sub>
- D. Hanya rumus Eka yang benar karena memakai modal awal 5.000.000.  
  <sub>Salah: tidak melihat bahwa rumus Dani dapat disederhanakan menjadi rumus Eka</sub>

**Pembahasan:** $U_1 = 5.000.000 + 200.000 = 5.200.000$ dan $b = 200.000$. Rumus Dani: $5.200.000 + 200.000n - 200.000 = 5.000.000 + 200.000n$, sama dengan rumus Eka.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas12-b01-c-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: dampak perubahan parameter bunga*

Pada bunga tunggal, besar bunga $B = M \times p\% \times n$. Sebuah simpanan diubah: modal awal dijadikan 2 kali semula, persentase bunga per tahun dijadikan setengah dari semula, dan lama menyimpan dijadikan 3 kali semula. Bunga yang diperoleh menjadi ... bunga semula.

- **A. 3 kali** ✅  
  <sub>Benar: faktor perubahan 2 x 1/2 x 3 = 3</sub>
- B. 6 kali  
  <sub>Salah: lupa bahwa persentase dijadikan setengah (2 x 3)</sub>
- C. 1 kali  
  <sub>Salah: lupa memperhitungkan perubahan lama menyimpan (2 x 1/2)</sub>
- D. 5,5 kali  
  <sub>Salah: menjumlahkan faktor perubahan (2 + 0,5 + 3)</sub>

**Pembahasan:** Bunga baru $= (2M) \times \frac{p\%}{2} \times (3n) = 3 \times (M \times p\% \times n)$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas12-b01-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: modal minimal bersyarat kelipatan*

Bu Rina ingin memperoleh bunga tunggal paling sedikit Rp2.000.000,00 dari simpanan selama 3 tahun dengan bunga 6% per tahun. Modal yang disetor harus kelipatan Rp1.000.000,00. Modal terkecil yang memenuhi keinginan Bu Rina adalah ....

- A. Rp11.000.000,00  
  <sub>Salah: membulatkan ke bawah; bunganya hanya Rp1.980.000,00 sehingga kurang dari Rp2.000.000,00</sub>
- **B. Rp12.000.000,00** ✅  
  <sub>Benar: M x 0,06 x 3 >= 2.000.000 sehingga M >= 11.111.111,1; kelipatan terkecil 12.000.000 (bunga 2.160.000)</sub>
- C. Rp34.000.000,00  
  <sub>Salah: lupa mengalikan dengan lama 3 tahun: 2.000.000 : 0,06 = 33,3 juta</sub>
- D. Rp11.111.111,00  
  <sub>Salah: tidak memenuhi syarat kelipatan Rp1.000.000,00</sub>

**Pembahasan:** $M \times 0,06 \times 3 \geq 2.000.000 \Rightarrow M \geq 11.111.111,1$. Kelipatan Rp1.000.000 terkecil adalah 12.000.000. Cek: 11.000.000 memberi bunga 1.980.000 (kurang).
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas12-b01-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: lama minimal agar saldo dua kali modal*

Sebuah tabungan berbunga tunggal 8% per tahun dari modal awal. Bunga ditambahkan ke saldo hanya pada setiap akhir tahun, dan uang tidak pernah diambil. Banyak tahun paling sedikit agar saldo tabungan paling sedikit dua kali modal awal adalah ....

- **A. 13** ✅  
  <sub>Benar: saldo = M(1 + 0,08n) >= 2M sehingga n >= 12,5; karena bunga ditambahkan akhir tahun, n bulat terkecil 13</sub>
- B. 25  
  <sub>Salah: memakai bunga 4% per tahun (100 : 4)</sub>
- C. 12  
  <sub>Salah: membulatkan 12,5 ke bawah; saldonya baru 196% dari modal</sub>
- D. 14  
  <sub>Salah: menambah satu tahun karena mengira tahun pertama belum berbunga</sub>

**Pembahasan:** $M + M \times 0,08 \times n \geq 2M \Rightarrow n \geq 12,5$. Bunga ditambahkan akhir tahun sehingga $n = 13$. Cek: $n = 12$ memberi $1,96M$, $n = 13$ memberi $2,04M$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas12-b01-c-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: membandingkan dua skema periode bunga*

Modal Rp10.000.000,00 dapat disimpan selama 2,5 tahun di salah satu bank. Bank A memberi bunga tunggal 6% per tahun. Bank B memberi bunga tunggal 3,2% per semester dari modal awal. Pilihan yang paling tepat adalah ....

- A. Bank A lebih menguntungkan, selisih bunga Rp100.000,00.  
  <sub>Salah: membandingkan 6% dan 3,2% tanpa menyamakan periode (semester vs tahun)</sub>
- B. Bank B lebih menguntungkan, selisih bunga Rp1.600.000,00.  
  <sub>Salah: menyebut bunga Bank B sebagai selisih</sub>
- C. Bank B lebih menguntungkan, selisih bunga Rp40.000,00.  
  <sub>Salah: hanya menghitung selisih bunga untuk satu tahun, bukan 2,5 tahun</sub>
- **D. Bank B lebih menguntungkan, selisih bunga Rp100.000,00.** ✅  
  <sub>Benar: Bank A: 10.000.000 x 0,06 x 2,5 = 1.500.000; Bank B: 10.000.000 x 0,032 x 5 = 1.600.000; selisih 100.000</sub>

**Pembahasan:** 2,5 tahun = 5 semester. Bank A: $10.000.000 \times 0,06 \times 2,5 = 1.500.000$. Bank B: $10.000.000 \times 0,032 \times 5 = 1.600.000$. Bank B lebih besar Rp100.000.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas12-b01-c-hard-bt01-008
*orisinal | C5 | 6 langkah | jenis: membandingkan dua skema cicilan*

Pak Tono meminjam Rp9.000.000,00 dan harus melunasinya dengan angsuran bulanan sama besar. Skema X: bunga tunggal 10% per tahun selama 2 tahun. Skema Y: bunga tunggal 8% per tahun selama 3 tahun. Pernyataan yang benar tentang kedua skema adalah ....

- A. Total bayar Skema X lebih kecil Rp360.000,00 dan angsuran bulanannya juga lebih kecil Rp140.000,00 daripada Skema Y.  
  <sub>Salah: mengira total lebih kecil berarti angsuran lebih kecil, padahal angsuran dibagi 24 vs 36 bulan</sub>
- B. Total bayar Skema X lebih kecil Rp180.000,00 dan angsuran bulanannya lebih besar Rp140.000,00 daripada Skema Y.  
  <sub>Salah: membandingkan bunga satu tahun (900.000 dan 720.000), bukan seluruh masa pinjaman</sub>
- **C. Total bayar Skema X lebih kecil Rp360.000,00 dan angsuran bulanannya lebih besar Rp140.000,00 daripada Skema Y.** ✅  
  <sub>Benar: X: total 10.800.000, angsuran 450.000; Y: total 11.160.000, angsuran 310.000; selisih total 360.000, selisih angsuran 140.000</sub>
- D. Total bayar Skema Y lebih kecil Rp360.000,00 dan angsuran bulanannya lebih kecil Rp140.000,00 daripada Skema X.  
  <sub>Salah: menduga persentase lebih rendah pasti total lebih kecil, mengabaikan lama pinjaman</sub>

**Pembahasan:** X: $9.000.000 \times 0,10 \times 2 = 1.800.000$, total 10.800.000, angsuran $10.800.000 : 24 = 450.000$. Y: $9.000.000 \times 0,08 \times 3 = 2.160.000$, total 11.160.000, angsuran $11.160.000 : 36 = 310.000$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas12-b01-c-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: menentukan pembagian modal dua bank*

Pak Surya membagi uang Rp20.000.000,00 menjadi dua simpanan. Sebagian disimpan di Bank P dengan bunga tunggal 6% per tahun, dan sisanya di Bank Q dengan bunga tunggal 4% per tahun. Setelah 5 tahun, jumlah bunga kedua bank adalah Rp4.600.000,00. Uang yang disimpan di Bank P adalah ....

- A. Rp10.000.000,00  
  <sub>Salah: mengira uang dibagi sama besar</sub>
- B. Rp14.000.000,00  
  <sub>Salah: menukar bagian Bank P dengan bagian Bank Q</sub>
- C. Rp12.000.000,00  
  <sub>Salah: membagi kelebihan bunga 600.000 dengan 5%, lupa selisih persentase 2% x 5 tahun</sub>
- **D. Rp6.000.000,00** ✅  
  <sub>Benar: 0,3x + 0,2(20.000.000 - x) = 4.600.000 sehingga 0,1x = 600.000, x = 6.000.000</sub>

**Pembahasan:** Misalkan Bank P $= x$. $x \times 0,06 \times 5 + (20.000.000 - x) \times 0,04 \times 5 = 4.600.000 \Rightarrow 0,1x + 4.000.000 = 4.600.000 \Rightarrow x = 6.000.000$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas12-b01-c-hard-bt01-010
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan angsuran*

Pak Yusuf meminjam Rp7.200.000,00 dengan bunga tunggal 5% per tahun dan akan melunasinya dengan angsuran bulanan sama besar selama 3 tahun. Seorang siswa menghitung angsuran per bulan sebagai $\frac{7.200.000 \times 0,05 \times 3}{36} = 30.000$. Kesalahan siswa tersebut adalah ....

- A. Pembaginya seharusnya 3 karena lama pinjaman 3 tahun, sehingga angsurannya Rp360.000,00.  
  <sub>Salah: mengira angsuran bulanan dibagi lama dalam tahun</sub>
- **B. Siswa hanya membagi bunga dengan 36; seharusnya pokok ditambah bunga dibagi 36 sehingga angsuran Rp230.000,00.** ✅  
  <sub>Benar: total bayar = 7.200.000 + 1.080.000 = 8.280.000; angsuran = 8.280.000 : 36 = 230.000</sub>
- C. Persentase seharusnya 0,5 sehingga angsurannya Rp3.000,00.  
  <sub>Salah: salah mengubah 5% ke desimal</sub>
- D. Bunga seharusnya dikalikan 36 lagi sehingga angsurannya Rp1.080.000,00.  
  <sub>Salah: menggandakan lama pinjaman dalam bulan pada rumus bunga</sub>

**Pembahasan:** Bunga total $= 7.200.000 \times 0,05 \times 3 = 1.080.000$. Total bayar $= 8.280.000$. Angsuran $= 8.280.000 : 36 = 230.000$. Siswa lupa menyertakan pokok pinjaman.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas12-b01-c-hard-bt01-011
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim*

Klaim: "Jika dua simpanan berbunga tunggal disimpan selama waktu yang sama, simpanan dengan persentase bunga lebih besar selalu menghasilkan bunga lebih besar." Pasangan simpanan yang menjadi contoh penyangkal klaim tersebut adalah ....

- A. X: Rp4.000.000,00 dengan bunga 3%; Y: Rp7.000.000,00 dengan bunga 5%  
  <sub>Salah: Y unggul pada persentase dan modal sehingga mendukung klaim (120.000 < 350.000)</sub>
- B. X: Rp6.000.000,00 dengan bunga 4%; Y: Rp6.000.000,00 dengan bunga 5%  
  <sub>Salah: modal sama, jadi persentase lebih besar memang menghasilkan bunga lebih besar (240.000 < 300.000), bukan penyangkal</sub>
- **C. X: Rp8.000.000,00 dengan bunga 5%; Y: Rp5.000.000,00 dengan bunga 6%** ✅  
  <sub>Benar: persentase Y lebih besar tetapi bunga setahun Y = 300.000 lebih kecil dari X = 400.000</sub>
- D. X: Rp9.000.000,00 dengan bunga 2%; Y: Rp9.000.000,00 dengan bunga 8%  
  <sub>Salah: selisih persentase besar dengan modal sama mendukung klaim (180.000 < 720.000)</sub>

**Pembahasan:** Bunga per tahun $= M \times p\%$. Pasangan pertama: X $= 400.000$, Y $= 300.000$, padahal persentase Y lebih besar. Pasangan lain: bunga simpanan berpersentase lebih besar juga lebih besar.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas12-b01-c-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: mencari persentase dari syarat dua simpanan*

Tina menyimpan Rp6.000.000,00 dan Umi menyimpan Rp4.000.000,00, keduanya dengan bunga tunggal selama 5 tahun. Persentase bunga per tahun simpanan Umi 2 poin persentase lebih besar daripada simpanan Tina, dan bunga yang mereka terima selama 5 tahun sama besar. Persentase bunga per tahun simpanan Umi adalah ....

- A. 4%  
  <sub>Salah: menjawab persentase Tina, bukan persentase Umi</sub>
- B. 5%  
  <sub>Salah: mengambil rata-rata tanpa persamaan</sub>
- C. 8%  
  <sub>Salah: mengira persentase Umi dua kali persentase Tina</sub>
- **D. 6%** ✅  
  <sub>Benar: 6.000.000 x p x 5 = 4.000.000 x (p+2) x 5 sehingga 6p = 4p + 8, p = 4 (Tina), Umi 6%</sub>

**Pembahasan:** Misalkan Tina $p\%$ dan Umi $(p+2)\%$. $6.000.000 \times p\% \times 5 = 4.000.000 \times (p+2)\% \times 5 \Rightarrow 6p = 4p + 8 \Rightarrow p = 4$. Umi $= 6\%$. Cek: bunga masing-masing 1.200.000.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b01-c-hard-bt01-013
*orisinal | C6 | 3 langkah | jenis: merancang deposito bunga bulanan*

Pak Anto ingin mendapat bunga tunggal tepat Rp300.000,00 setiap bulan dari sebuah deposito. Pasangan modal dan persentase bunga per tahun yang memenuhi keinginan Pak Anto adalah ....

- A. Modal Rp5.000.000,00 dengan bunga 6% per tahun  
  <sub>Salah: bunga Rp300.000,00 adalah bunga setahun, bukan sebulan</sub>
- B. Modal Rp50.000.000,00 dengan bunga 6% per tahun  
  <sub>Salah: bunga per bulan hanya Rp250.000,00</sub>
- **C. Modal Rp60.000.000,00 dengan bunga 6% per tahun** ✅  
  <sub>Benar: bunga setahun = 60.000.000 x 0,06 = 3.600.000; per bulan = 3.600.000 : 12 = 300.000</sub>
- D. Modal Rp72.000.000,00 dengan bunga 6% per tahun  
  <sub>Salah: bunga per bulan Rp360.000,00, terlalu besar</sub>

**Pembahasan:** Bunga per bulan $= \frac{M \times p\%}{12}$. Untuk $M = 60.000.000$ dan $p = 6\%$: $\frac{3.600.000}{12} = 300.000$. Pilihan lain menghasilkan 250.000; 360.000; dan 25.000 per bulan.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
