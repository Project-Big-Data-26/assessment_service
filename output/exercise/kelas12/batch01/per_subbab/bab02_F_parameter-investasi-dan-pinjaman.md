# Lembar koreksi — kelas12 SMA12U-B2 subbab F: Parameter Investasi dan Pinjaman

57 soal | easy 20, medium 20, hard 17 | variasi 20, orisinal 37
> **Kapasitas kurang (hard): 17 dari kuota 20** — Subbab F hanya memuat dua parameter (suku bunga dan periode pembayaran) dengan rumus nilai akhir bunga majemuk; acuan pretest dan Buku Siswa sudah habis pada easy dan medium. Penalaran hard (evaluasi klaim, temukan kesalahan, syarat ganda, perancangan parameter, perbandingan skema) hanya layak sampai 17 soal tanpa kembar atau materi di luar subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b02-f-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: nilai akhir pinjaman online (bulan ke tahun)*

Sebuah aplikasi pinjaman online memberikan pinjaman sebesar Rp5.000.000,00 dengan suku bunga majemuk 10% per tahun. Periode pinjaman selama 36 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?

- A. Rp6.050.000,00  
  <sub>Salah: keliru memakai n = 2 tahun</sub>
- **B. Rp6.655.000,00** ✅  
  <sub>Benar: 36 bulan = 3 tahun; $5.000.000 \times (1,1)^3 = 6.655.000$</sub>
- C. Rp5.500.000,00  
  <sub>Salah: hanya menghitung bunga satu tahun (n = 1)</sub>
- D. Rp6.500.000,00  
  <sub>Salah: memakai bunga tunggal (bunga 10% x 3 tahun), bukan bunga majemuk</sub>

**Pembahasan:** 36 bulan = 3 tahun. Nilai akhir = $5.000.000 \times (1,1)^3 = 6.655.000$.
**Acuan:** pretest — kelas12-b02-p0092-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b02-f-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: pengembalian pinjaman koperasi digital*

Toko Makmur meminjam modal dari sebuah koperasi digital sebesar Rp30.000.000,00. Bunga majemuk yang dikenakan adalah 20% per tahun dan pinjaman dikembalikan sekaligus setelah 24 bulan. Jumlah yang harus dikembalikan adalah ....

- A. Rp36.000.000,00  
  <sub>Salah: hanya menghitung bunga satu tahun</sub>
- B. Rp51.840.000,00  
  <sub>Salah: keliru memakai n = 3 tahun</sub>
- C. Rp42.000.000,00  
  <sub>Salah: memakai bunga tunggal (20% x 2 tahun)</sub>
- **D. Rp43.200.000,00** ✅  
  <sub>Benar: 24 bulan = 2 tahun; $30.000.000 \times (1,2)^2 = 43.200.000$</sub>

**Pembahasan:** 24 bulan = 2 tahun. $30.000.000 \times (1,2)^2 = 43.200.000$.
**Acuan:** pretest — kelas12-b02-p0092-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b02-f-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: membandingkan dua koperasi*

Dua koperasi memberikan pinjaman masing-masing Rp10.000.000,00. Koperasi A memberikan suku bunga sebesar 10% per tahun selama 3 tahun, sedangkan Koperasi B memberikan suku bunga sebesar 20% per tahun selama 2 tahun.

Koperasi manakah yang nilai akhir pengembaliannya lebih besar, dan berapakah nilai akhir itu?

- A. Koperasi A dengan nilai akhir Rp13.000.000,00  
  <sub>Salah: memakai bunga tunggal untuk Koperasi A dan salah memilih koperasi</sub>
- **B. Koperasi B dengan nilai akhir Rp14.400.000,00** ✅  
  <sub>Benar: A: $10.000.000 \times (1,1)^3 = 13.310.000$; B: $10.000.000 \times (1,2)^2 = 14.400.000$; B lebih besar</sub>
- C. Koperasi A dengan nilai akhir Rp13.310.000,00  
  <sub>Salah: tertukar arah perbandingan, padahal nilai akhir B lebih besar</sub>
- D. Koperasi B dengan nilai akhir Rp14.000.000,00  
  <sub>Salah: memakai bunga tunggal untuk Koperasi B</sub>

**Pembahasan:** A: 13.310.000. B: 14.400.000. Nilai akhir terbesar ada pada Koperasi B.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b02-f-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: nilai akhir terbesar dua bank*

Bank Pelita dan Bank Sentosa sama-sama memberi pinjaman usaha sebesar Rp20.000.000,00. Bank Pelita menetapkan bunga majemuk 15% per tahun selama 2 tahun, sedangkan Bank Sentosa menetapkan bunga majemuk 8% per tahun selama 3 tahun. Nilai akhir pengembalian yang lebih besar di antara keduanya adalah ....

- A. Rp25.194.240,00  
  <sub>Salah: memilih nilai akhir yang lebih kecil (Bank Sentosa)</sub>
- **B. Rp26.450.000,00** ✅  
  <sub>Benar: Pelita: $20.000.000 \times (1,15)^2 = 26.450.000$; Sentosa: $20.000.000 \times (1,08)^3 = 25.194.240$</sub>
- C. Rp24.800.000,00  
  <sub>Salah: memakai bunga tunggal untuk Bank Sentosa</sub>
- D. Rp26.000.000,00  
  <sub>Salah: memakai bunga tunggal untuk Bank Pelita</sub>

**Pembahasan:** Pelita 26.450.000 > Sentosa 25.194.240, sehingga yang lebih besar adalah 26.450.000.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b02-f-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: nilai akhir modal di tempat kedua*

Rani memberikan modal di dua tempat, masing-masing Rp30.000.000,00. Modal pada tempat pertama memiliki suku bunga 6% per tahun dengan periode 2 tahun. Modal pada tempat kedua memiliki suku bunga 4% per tahun dengan periode 3 tahun. Berapakah nilai akhir modal pada tempat kedua?

- **A. Rp33.745.920,00** ✅  
  <sub>Benar: $30.000.000 \times (1,04)^3 = 33.745.920$</sub>
- B. Rp33.600.000,00  
  <sub>Salah: memakai bunga tunggal (4% x 3 tahun)</sub>
- C. Rp32.448.000,00  
  <sub>Salah: memakai n = 2 (periode tempat pertama)</sub>
- D. Rp33.708.000,00  
  <sub>Salah: menghitung nilai akhir tempat pertama, bukan kedua</sub>

**Pembahasan:** $30.000.000 \times (1,04)^3 = 33.745.920$.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b02-f-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: memilih pernyataan nilai akhir yang benar*

Ibu ingin memberikan modal investasi untuk anaknya sebesar Rp20.000.000,00.

Pernyataan manakah yang benar mengenai nilai akhir modal investasi tersebut? (bunga majemuk per tahun)

- A. Nilai akhir yang didapat sebesar Rp24.000.000,00 jika suku bunga 10% per tahun dengan periode selama 2 tahun.  
  <sub>Salah: memakai bunga tunggal, bukan majemuk</sub>
- **B. Nilai akhir yang didapat sebesar Rp24.200.000,00 jika suku bunga 10% per tahun dengan periode selama 2 tahun.** ✅  
  <sub>Benar: $20.000.000 \times (1,1)^2 = 24.200.000$</sub>
- C. Nilai akhir yang didapat lebih besar jika suku bunga 5% selama 3 tahun dibanding suku bunga 10% selama 2 tahun.  
  <sub>Salah: perbandingan terbalik: Rp23.152.500,00 lebih kecil dari Rp24.200.000,00</sub>
- D. Nilai akhir yang didapat sebesar Rp23.000.000,00 jika suku bunga 5% per tahun dengan periode selama 3 tahun.  
  <sub>Salah: memakai bunga tunggal; nilai majemuk sebenarnya Rp23.152.500,00</sub>

**Pembahasan:** 10% 2 tahun: 24.200.000. 5% 3 tahun: 23.152.500. Hanya pernyataan pertama yang benar.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b02-f-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: membandingkan dua skema deposito*

Pak Rudi ingin menyimpan modal sebesar Rp5.000.000,00 di sebuah deposito yang berbunga majemuk per tahun.

Pernyataan manakah yang benar mengenai nilai akhir simpanan Pak Rudi?

- A. Nilai akhir yang didapat lebih besar jika suku bunga 20% selama 2 tahun dibanding suku bunga 10% selama 4 tahun.  
  <sub>Salah: perbandingan terbalik: 7.200.000 lebih kecil dari 7.320.500</sub>
- B. Nilai akhir yang didapat sebesar Rp7.000.000,00 jika suku bunga 10% per tahun dengan periode selama 4 tahun.  
  <sub>Salah: memakai bunga tunggal; nilai majemuk sebenarnya Rp7.320.500,00</sub>
- C. Nilai akhir yang didapat sebesar Rp6.000.000,00 jika suku bunga 20% per tahun dengan periode selama 2 tahun.  
  <sub>Salah: hanya menghitung bunga satu tahun</sub>
- **D. Nilai akhir yang didapat lebih besar jika suku bunga 10% selama 4 tahun dibanding suku bunga 20% selama 2 tahun.** ✅  
  <sub>Benar: 20% 2 tahun: 5.000.000 x 1,44 = 7.200.000; 10% 4 tahun: 5.000.000 x 1,4641 = 7.320.500</sub>

**Pembahasan:** 20% 2 tahun: 7.200.000. 10% 4 tahun: 7.320.500. Maka 10% selama 4 tahun lebih besar.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b02-f-easy-bt01-008
*variasi (angka) | C2 | 1 langkah | jenis: nilai akhir dana investasi (pengaruh suku bunga)*

Sebuah yayasan mengelola dana investasi sebesar Rp50.000.000,00 yang dibungakan secara majemuk per tahun.

Jika yayasan menginvestasikan dananya pada kurun waktu 3 tahun, berapa nilai akhir yang didapat dari dana investasi tersebut ketika suku bunga berada pada angka 6%?

- A. Rp56.180.000,00  
  <sub>Salah: keliru memakai n = 2 tahun</sub>
- B. Rp59.000.000,00  
  <sub>Salah: memakai bunga tunggal (6% x 3 tahun)</sub>
- **C. Rp59.550.800,00** ✅  
  <sub>Benar: $50.000.000 \times (1,06)^3 = 59.550.800$</sub>
- D. Rp9.550.800,00  
  <sub>Salah: hanya menjawab total bunga, bukan nilai akhir</sub>

**Pembahasan:** $50.000.000 \times (1,06)^3 = 59.550.800$.
**Acuan:** siswa — siswa hal.90 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b02-f-easy-bt01-009
*variasi (angka) | C2 | 1 langkah | jenis: nilai akhir dana investasi (pengaruh periode)*

Koperasi Sejahtera memiliki dana investasi sebesar Rp25.000.000,00 yang dibungakan majemuk per tahun.

Jika koperasi menginvestasikan dananya pada kurun waktu 4 tahun, berapa nilai akhir yang didapat dari dana investasi tersebut ketika suku bunga berada pada angka 8%?

- A. Rp9.012.224,00  
  <sub>Salah: hanya menjawab total bunga, bukan nilai akhir</sub>
- **B. Rp34.012.224,00** ✅  
  <sub>Benar: $25.000.000 \times (1,08)^4 = 34.012.224$</sub>
- C. Rp31.492.800,00  
  <sub>Salah: keliru memakai n = 3 tahun</sub>
- D. Rp33.000.000,00  
  <sub>Salah: memakai bunga tunggal (8% x 4 tahun)</sub>

**Pembahasan:** $25.000.000 \times (1,08)^4 = 34.012.224$.
**Acuan:** siswa — siswa hal.91 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b02-f-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: nilai akhir dana kas klub*

Klub olahraga SMA Nusa menyimpan dana kas sebesar Rp40.000.000,00 di sebuah deposito berbunga majemuk 12% per tahun. Berapa nilai akhir dana kas tersebut setelah disimpan selama 2 tahun?

- **A. Rp50.176.000,00** ✅  
  <sub>Benar: $40.000.000 \times (1,12)^2 = 50.176.000$</sub>
- B. Rp49.600.000,00  
  <sub>Salah: memakai bunga tunggal (12% x 2 tahun)</sub>
- C. Rp44.800.000,00  
  <sub>Salah: hanya menghitung satu tahun</sub>
- D. Rp56.197.120,00  
  <sub>Salah: keliru memakai n = 3 tahun</sub>

**Pembahasan:** $40.000.000 \times (1,12)^2 = 50.176.000$.
**Acuan:** siswa — siswa hal.90 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b02-f-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: pengaruh suku bunga terhadap nilai akhir*

Dua investasi memiliki modal awal dan periode yang sama. Semakin besar suku bunga majemuk per tahun, nilai akhir investasi tersebut akan ....

- A. semakin kecil  
  <sub>Salah: mengira bunga besar mengurangi nilai akhir</sub>
- B. tetap sama karena modal awal tidak berubah  
  <sub>Salah: mengabaikan pengaruh suku bunga</sub>
- **C. semakin besar** ✅  
  <sub>Benar: bunga tiap periode makin besar sehingga nilai akhir ikut naik</sub>
- D. berkurang sebanding dengan kenaikan suku bunga  
  <sub>Salah: membalik arah hubungan</sub>

**Pembahasan:** Dengan modal dan periode sama, $(1+p)^n$ makin besar saat $p$ makin besar, sehingga nilai akhir makin besar.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b02-f-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: pengaruh periode terhadap pengembalian pinjaman*

Seorang peminjam menerima pinjaman dengan suku bunga majemuk tetap per tahun. Jika lama pinjaman diperpanjang dari 2 tahun menjadi 4 tahun, jumlah pengembalian pinjaman tersebut akan ....

- A. lebih kecil  
  <sub>Salah: mengira periode lebih lama menurunkan nilai akhir</sub>
- B. menjadi tepat dua kali lipat  
  <sub>Salah: mengira pengaruh periode linear, padahal berpangkat</sub>
- **C. lebih besar** ✅  
  <sub>Benar: periode makin lama menambah jumlah periode bunga sehingga pengembalian naik</sub>
- D. sama besar  
  <sub>Salah: mengira periode tidak memengaruhi hasil</sub>

**Pembahasan:** Makin lama periode, makin banyak bunga yang diperhitungkan, sehingga pengembalian makin besar (tidak persis dua kali lipat).
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b02-f-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: mengenal parameter investasi*

Dua parameter yang dipelajari memengaruhi nilai akhir investasi dan pinjaman adalah ....

- A. jumlah nasabah dan jenis kartu  
  <sub>Salah: hal yang tidak ada dalam rumus nilai akhir</sub>
- B. nama bank dan lokasi kantor  
  <sub>Salah: parameter nonmatematis yang tidak masuk rumus</sub>
- C. usia dan pekerjaan nasabah  
  <sub>Salah: data pribadi yang tidak memengaruhi hitungan</sub>
- **D. suku bunga dan periode pembayaran** ✅  
  <sub>Benar: buku membahas parameter suku bunga dan periode pembayaran</sub>

**Pembahasan:** Parameter yang dibahas adalah suku bunga dan periode pembayaran.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b02-f-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: nilai akhir pinjaman pada akhir tahun tertentu*

Bank XYZ memberikan pinjaman sebesar Rp40.000.000,00 dengan suku bunga majemuk 3% per tahun. Nilai akhir pinjaman tersebut pada akhir tahun kedua adalah ....

- **A. Rp42.436.000,00** ✅  
  <sub>Benar: $40.000.000 \times (1,03)^2 = 42.436.000$</sub>
- B. Rp41.200.000,00  
  <sub>Salah: memakai nilai akhir tahun pertama</sub>
- C. Rp42.400.000,00  
  <sub>Salah: memakai bunga tunggal</sub>
- D. Rp43.709.080,00  
  <sub>Salah: memakai nilai akhir tahun ketiga</sub>

**Pembahasan:** $40.000.000 \times (1,03)^2 = 42.436.000$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b02-f-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: selisih nilai akhir dua suku bunga*

Modal Rp10.000.000,00 diinvestasikan selama 2 tahun dengan bunga majemuk per tahun. Selisih nilai akhir jika suku bunganya 10% dan jika suku bunganya 5% adalah ....

- A. Rp500.000,00  
  <sub>Salah: selisih bunga tahun pertama saja</sub>
- B. Rp1.000.000,00  
  <sub>Salah: membandingkan hasil bunga tunggal</sub>
- **C. Rp1.075.000,00** ✅  
  <sub>Benar: 10%: 12.100.000; 5%: 11.025.000; selisih 1.075.000</sub>
- D. Rp2.100.000,00  
  <sub>Salah: menjawab total bunga pada suku bunga 10%</sub>

**Pembahasan:** 12.100.000 - 11.025.000 = 1.075.000.
**Acuan:** siswa — siswa hal.90

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b02-f-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: selisih nilai akhir dua periode*

Modal Rp30.000.000,00 dibungakan majemuk 10% per tahun. Selisih nilai akhir jika disimpan 3 tahun dan jika disimpan 2 tahun adalah ....

- A. Rp3.300.000,00  
  <sub>Salah: menghitung bunga tahun kedua, bukan tahun ketiga</sub>
- B. Rp9.930.000,00  
  <sub>Salah: menjawab total bunga 3 tahun</sub>
- C. Rp3.000.000,00  
  <sub>Salah: memakai bunga tunggal (satu tahun tambahan)</sub>
- **D. Rp3.630.000,00** ✅  
  <sub>Benar: 3 tahun: 39.930.000; 2 tahun: 36.300.000; selisih 3.630.000</sub>

**Pembahasan:** 39.930.000 - 36.300.000 = 3.630.000.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b02-f-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: memilih nilai akhir terbesar dari beberapa suku bunga*

Dana Rp10.000.000,00 akan diinvestasikan selama 2 tahun dengan bunga majemuk per tahun. Pilihan suku bunga yang tersedia adalah 3%, 5%, dan 7%. Nilai akhir terbesar yang dapat diperoleh adalah ....

- A. Rp10.609.000,00  
  <sub>Salah: nilai akhir untuk suku bunga 3%, yang terkecil</sub>
- B. Rp11.400.000,00  
  <sub>Salah: memakai bunga tunggal untuk 7%</sub>
- **C. Rp11.449.000,00** ✅  
  <sub>Benar: pada 7%: $10.000.000 \times (1,07)^2 = 11.449.000$; suku bunga terbesar memberi nilai akhir terbesar</sub>
- D. Rp11.025.000,00  
  <sub>Salah: nilai akhir untuk suku bunga 5%, bukan yang terbesar</sub>

**Pembahasan:** Suku bunga terbesar (7%) memberi nilai akhir terbesar: 11.449.000.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b02-f-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: membaca kenaikan nilai akhir dari tabel*

Nilai akhir dana Rp10.000.000,00 dengan bunga majemuk 3% per tahun:

| Periode (tahun) | Nilai akhir |
|---|---|
| 1 | Rp10.300.000,00 |
| 2 | Rp10.609.000,00 |
| 3 | Rp10.927.700,00 |

Kenaikan nilai akhir dari akhir tahun ke-2 ke akhir tahun ke-3 adalah ....

- A. Rp927.700,00  
  <sub>Salah: memakai total bunga tiga tahun</sub>
- B. Rp309.000,00  
  <sub>Salah: mengurangkan tahun ke-1 dari tahun ke-2</sub>
- C. Rp300.000,00  
  <sub>Salah: memakai bunga tahun pertama saja</sub>
- **D. Rp318.700,00** ✅  
  <sub>Benar: 10.927.700 - 10.609.000 = 318.700</sub>

**Pembahasan:** 10.927.700 - 10.609.000 = 318.700.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b02-f-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: penalaran dua parameter sekaligus*

Empat skema investasi berikut memakai modal awal yang sama dan bunga majemuk per tahun. Skema yang menghasilkan nilai akhir terbesar adalah ....

- **A. suku bunga 5% per tahun selama 4 tahun** ✅  
  <sub>Benar: suku bunga dan periode sama-sama paling besar sehingga nilai akhir terbesar</sub>
- B. suku bunga 5% per tahun selama 2 tahun  
  <sub>Salah: periode lebih pendek dari 4 tahun dengan suku bunga sama</sub>
- C. suku bunga 3% per tahun selama 2 tahun  
  <sub>Salah: suku bunga dan periode sama-sama paling kecil</sub>
- D. suku bunga 3% per tahun selama 4 tahun  
  <sub>Salah: suku bunga lebih kecil dari 5% dengan periode sama</sub>

**Pembahasan:** Makin besar suku bunga dan makin lama periode, makin besar nilai akhir. Skema 5% selama 4 tahun memenuhi keduanya.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b02-f-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: menyusun bentuk perhitungan nilai akhir*

Sebuah aplikasi pinjaman online memberikan pinjaman Rp12.000.000,00 dengan suku bunga majemuk 8% per tahun. Periode pinjaman selama 48 bulan. Bentuk perhitungan nilai akhir yang benar adalah ....

- **A. $12.000.000 \times (1,08)^4$** ✅  
  <sub>Benar: 48 bulan = 4 tahun; faktor $1 + 0,08 = 1,08$</sub>
- B. $12.000.000 \times (1,8)^4$  
  <sub>Salah: salah mengubah 8% menjadi 0,8</sub>
- C. $12.000.000 \times (1 + 0,08 \times 4)$  
  <sub>Salah: memakai rumus bunga tunggal</sub>
- D. $12.000.000 \times (1,08)^{48}$  
  <sub>Salah: memakai 48 bulan sebagai pangkat tahunan</sub>

**Pembahasan:** n = 48 : 12 = 4 tahun; nilai akhir = $12.000.000 \times (1,08)^4$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b02-f-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: selisih nilai akhir dua suku bunga (4 tahun)*

Sebuah perusahaan mengelola dana investasi sebesar Rp20.000.000,00 yang dibungakan secara majemuk per tahun.

Dengan investasi dalam kurun waktu yang sama, yaitu 4 tahun, berapa selisih nilai akhir yang didapat dari dana investasi tersebut ketika suku bunga berada pada nilai maksimal (10%) dibandingkan dengan suku bunga 5%?

- A. Rp4.000.000,00  
  <sub>Salah: memakai bunga tunggal: 20.000.000 x 5% x 4</sub>
- **B. Rp4.971.875,00** ✅  
  <sub>Benar: 10%: 20.000.000 x (1,1)^4 = Rp29.282.000,00; 5%: 20.000.000 x (1,05)^4 = Rp24.310.125,00; selisih Rp4.971.875,00</sub>
- C. Rp3.467.500,00  
  <sub>Salah: keliru memakai n = 3 tahun</sub>
- D. Rp29.282.000,00  
  <sub>Salah: hanya menjawab nilai akhir pada suku bunga 10%, tidak dikurangi</sub>

**Pembahasan:** Nilai akhir 10%: Rp29.282.000,00. Nilai akhir 5%: Rp24.310.125,00. Selisih = Rp4.971.875,00.
**Acuan:** siswa — siswa hal.90 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b02-f-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: selisih nilai akhir dua suku bunga (3 tahun)*

Koperasi pegawai menyimpan dana sebesar Rp50.000.000,00 pada deposito berbunga majemuk per tahun selama 3 tahun. Berapa lebih besar nilai akhir dana itu saat suku bunga tertinggi 8% dibanding saat suku bunga terendah 4%?

- A. Rp62.985.600,00  
  <sub>Salah: hanya menjawab nilai akhir pada suku bunga 8%</sub>
- **B. Rp6.742.400,00** ✅  
  <sub>Benar: 8%: Rp62.985.600,00; 4%: Rp56.243.200,00; selisih Rp6.742.400,00</sub>
- C. Rp6.000.000,00  
  <sub>Salah: memakai bunga tunggal: 50.000.000 x 4% x 3</sub>
- D. Rp4.240.000,00  
  <sub>Salah: keliru memakai n = 2 tahun</sub>

**Pembahasan:** 8%: 50.000.000 x (1,08)^3 = Rp62.985.600,00. 4%: 50.000.000 x (1,04)^3 = Rp56.243.200,00. Selisih = Rp6.742.400,00.
**Acuan:** siswa — siswa hal.90 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b02-f-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: tambahan nilai akhir karena periode lebih lama*

Sebuah dana investasi sebesar Rp10.000.000,00 dibungakan secara majemuk per tahun.

Anggap suku bunga yang terjadi adalah 10%. Berapa tambahan nilai akhir yang didapat dari dana investasi tersebut, jika periode waktunya dibuat lebih lama, yaitu 6 tahun dibanding 5 tahun?

- A. Rp1.000.000,00  
  <sub>Salah: memakai bunga tunggal: tambahan satu tahun = 10% x modal awal</sub>
- B. Rp17.715.610,00  
  <sub>Salah: menjawab nilai akhir 6 tahun, bukan tambahannya</sub>
- **C. Rp1.610.510,00** ✅  
  <sub>Benar: 5 tahun: Rp16.105.100,00; 6 tahun: Rp17.715.610,00; tambahan Rp1.610.510,00</sub>
- D. Rp1.464.100,00  
  <sub>Salah: menghitung bunga tahun ke-5, bukan tahun ke-6</sub>

**Pembahasan:** 10.000.000 x (1,1)^5 = Rp16.105.100,00; x (1,1)^6 = Rp17.715.610,00. Tambahan = Rp1.610.510,00.
**Acuan:** siswa — siswa hal.91 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b02-f-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: selisih tabungan 4 tahun dan 2 tahun*

Bu Sari menabung Rp25.000.000,00 pada deposito berbunga majemuk 6% per tahun. Berapa tambahan nilai akhir tabungannya bila ia menyimpannya selama 4 tahun dibanding hanya 2 tahun?

- **A. Rp3.471.924,00** ✅  
  <sub>Benar: 2 tahun: Rp28.090.000,00; 4 tahun: Rp31.561.924,00; tambahan Rp3.471.924,00</sub>
- B. Rp1.685.400,00  
  <sub>Salah: membandingkan 3 tahun dengan 2 tahun</sub>
- C. Rp31.561.924,00  
  <sub>Salah: menjawab nilai akhir 4 tahun, bukan tambahannya</sub>
- D. Rp3.000.000,00  
  <sub>Salah: memakai bunga tunggal untuk dua tahun tambahan</sub>

**Pembahasan:** 25.000.000 x (1,06)^2 = Rp28.090.000,00; x (1,06)^4 = Rp31.561.924,00. Tambahan = Rp3.471.924,00.
**Acuan:** siswa — siswa hal.91 Ayo, Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b02-f-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: membandingkan modal di dua tempat*

Dina memberikan modal di dua tempat, masing-masing sebesar Rp80.000.000,00. Modal pada tempat pertama memiliki suku bunga 8% per tahun dengan periode 2 tahun. Modal pada tempat kedua memiliki suku bunga 6% per tahun dengan periode 3 tahun. Gunakan bunga majemuk per tahun.

Hitunglah nilai akhir modal pada kedua tempat tersebut! Manakah yang lebih menguntungkan?

- A. Tempat pertama Rp93.312.000,00 dan tempat kedua Rp95.281.280,00; tempat pertama lebih menguntungkan  
  <sub>Salah: nilai akhir benar tetapi kesimpulan tertukar</sub>
- B. Tempat pertama Rp100.776.960,00 dan tempat kedua Rp89.888.000,00; tempat pertama lebih menguntungkan  
  <sub>Salah: periode kedua tempat tertukar</sub>
- **C. Tempat pertama Rp93.312.000,00 dan tempat kedua Rp95.281.280,00; tempat kedua lebih menguntungkan** ✅  
  <sub>Benar: 8%, 2 tahun: Rp93.312.000,00; 6%, 3 tahun: Rp95.281.280,00; kedua lebih besar</sub>
- D. Tempat pertama Rp92.800.000,00 dan tempat kedua Rp94.400.000,00; tempat kedua lebih menguntungkan  
  <sub>Salah: memakai bunga tunggal pada kedua tempat</sub>

**Pembahasan:** Tempat pertama: 80.000.000 x (1,08)^2 = Rp93.312.000,00. Tempat kedua: 80.000.000 x (1,06)^3 = Rp95.281.280,00. Tempat kedua lebih menguntungkan.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b02-f-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: membandingkan dua koperasi (selisih)*

Untuk menggalakkan program koperasi berdaya guna, beberapa koperasi akan memberikan pinjaman masing-masing sebesar Rp10.000.000,00 kepada pengurus desa untuk modal pembangunan. Koperasi A memberikan suku bunga majemuk sebesar 10% per tahun selama 5 tahun, sedangkan Koperasi B memberikan suku bunga majemuk sebesar 20% per tahun selama 3 tahun.

Bandingkan nilai akhir pengembalian pinjaman pada masing-masing koperasi. Koperasi manakah yang nilai akhirnya lebih besar, dan berapa selisihnya?

- **A. Koperasi B, lebih besar Rp1.174.900,00** ✅  
  <sub>Benar: A: Rp16.105.100,00; B: Rp17.280.000,00; B lebih besar Rp1.174.900,00</sub>
- B. Koperasi A, lebih besar Rp1.174.900,00  
  <sub>Salah: arah perbandingan tertukar</sub>
- C. Koperasi B, lebih besar Rp2.639.000,00  
  <sub>Salah: Koperasi A dihitung dengan n = 4</sub>
- D. Koperasi B, lebih besar Rp1.000.000,00  
  <sub>Salah: memakai bunga tunggal (A 50%, B 60%)</sub>

**Pembahasan:** A: 10.000.000 x (1,1)^5 = Rp16.105.100,00. B: 10.000.000 x (1,2)^3 = Rp17.280.000,00. Selisih Rp1.174.900,00.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b02-f-medium-bt01-007
*variasi (konteks) | C4 | 3 langkah | jenis: menganalisis dua bank (jebakan tunggal)*

Dua bank memberi pinjaman usaha masing-masing Rp20.000.000,00. Bank Mawar menetapkan bunga majemuk 9% per tahun selama 2 tahun, sedangkan Bank Melati menetapkan bunga majemuk 6% per tahun selama 3 tahun.

Bank manakah yang nilai akhir pengembaliannya lebih besar, dan berapa selisihnya?

- A. Bank Mawar, lebih besar Rp58.320,00  
  <sub>Salah: arah perbandingan tertukar</sub>
- B. Bank Melati, lebih besar Rp583.200,00  
  <sub>Salah: salah geser angka pada selisih</sub>
- C. Kedua bank sama besar  
  <sub>Salah: memakai bunga tunggal: 9% x 2 = 6% x 3 = 18%</sub>
- **D. Bank Melati, lebih besar Rp58.320,00** ✅  
  <sub>Benar: Mawar: Rp23.762.000,00; Melati: Rp23.820.320,00; Melati lebih besar Rp58.320,00</sub>

**Pembahasan:** Mawar: 20.000.000 x (1,09)^2 = Rp23.762.000,00. Melati: 20.000.000 x (1,06)^3 = Rp23.820.320,00. Selisih Rp58.320,00.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b02-f-medium-bt01-008
*variasi (angka) | C4 | 3 langkah | jenis: memilih pernyataan nilai akhir yang benar*

Pak Hadi ingin memberikan modal investasi untuk anaknya sebesar Rp50.000.000,00.

Pernyataan manakah yang benar mengenai nilai akhir modal investasi tersebut? (bunga majemuk per tahun)

- A. Nilai akhir yang didapat sebesar Rp58.320.000,00 jika suku bunga 8% per tahun dengan periode selama 3 tahun.  
  <sub>Salah: memakai n = 2; nilai sebenarnya Rp62.985.600,00</sub>
- B. Nilai akhir yang didapat sebesar Rp62.000.000,00 jika suku bunga 12% per tahun dengan periode selama 2 tahun.  
  <sub>Salah: memakai bunga tunggal; nilai majemuk sebenarnya Rp62.720.000,00</sub>
- C. Nilai akhir yang didapat sebesar Rp53.000.000,00 jika suku bunga 6% per tahun dengan periode selama 4 tahun.  
  <sub>Salah: hanya menghitung satu tahun; nilai sebenarnya Rp63.123.848,00</sub>
- **D. Nilai akhir yang didapat lebih besar jika suku bunga 6% selama 4 tahun dibanding suku bunga 12% selama 2 tahun.** ✅  
  <sub>Benar: 12%, 2 tahun: Rp62.720.000,00; 6%, 4 tahun: Rp63.123.848,00; 6% selama 4 tahun lebih besar</sub>

**Pembahasan:** 12% 2 tahun: Rp62.720.000,00; 6% 4 tahun: Rp63.123.848,00. Hanya pernyataan pertama yang benar.
**Acuan:** pretest — kelas12-b02-p0093-latihan-2-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b02-f-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: nilai akhir pinjaman online (60 bulan)*

Sebuah aplikasi pinjaman online memberikan pinjaman sebesar Rp25.000.000,00 dengan suku bunga majemuk 10% per tahun. Periode pinjaman selama 60 bulan. Berapakah nilai akhir pengembalian pinjaman tersebut?

- **A. Rp40.262.750,00** ✅  
  <sub>Benar: 60 bulan = 5 tahun; 25.000.000 x (1,1)^5 = Rp40.262.750,00</sub>
- B. Rp36.602.500,00  
  <sub>Salah: keliru memakai n = 4 tahun</sub>
- C. Rp37.500.000,00  
  <sub>Salah: memakai bunga tunggal (10% x 5 tahun)</sub>
- D. Rp15.262.750,00  
  <sub>Salah: hanya menjawab total bunga, bukan nilai akhir</sub>

**Pembahasan:** 60 bulan = 5 tahun. 25.000.000 x (1,1)^5 = Rp40.262.750,00.
**Acuan:** pretest — kelas12-b02-p0092-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b02-f-medium-bt01-010
*variasi (konteks) | C3 | 2 langkah | jenis: pengembalian kredit modal koperasi (36 bulan)*

Pak Hadi mengambil kredit modal Rp15.000.000,00 dari sebuah koperasi dengan bunga majemuk 20% per tahun. Kredit itu dilunasi sekaligus setelah 36 bulan. Jumlah yang harus dibayar Pak Hadi adalah ....

- **A. Rp25.920.000,00** ✅  
  <sub>Benar: 36 bulan = 3 tahun; 15.000.000 x (1,2)^3 = Rp25.920.000,00</sub>
- B. Rp21.600.000,00  
  <sub>Salah: keliru memakai n = 2 tahun</sub>
- C. Rp10.920.000,00  
  <sub>Salah: hanya menjawab total bunga</sub>
- D. Rp24.000.000,00  
  <sub>Salah: memakai bunga tunggal (20% x 3 tahun)</sub>

**Pembahasan:** 36 bulan = 3 tahun. 15.000.000 x (1,2)^3 = Rp25.920.000,00.
**Acuan:** pretest — kelas12-b02-p0092-latihan-2-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b02-f-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: dana investasi dari persentase omset*

Sebuah perusahaan menyisihkan dana investasi sebesar 10% dari omset minimum bulanannya, yaitu Rp300.000.000,00. Dana itu dibungakan majemuk 5% per tahun selama 3 tahun. Nilai akhir dana investasi tersebut adalah ....

- A. Rp347.287.500,00  
  <sub>Salah: lupa mengambil 10% dari omset, memakai seluruh omset</sub>
- B. Rp34.500.000,00  
  <sub>Salah: memakai bunga tunggal (5% x 3 tahun)</sub>
- C. Rp4.728.750,00  
  <sub>Salah: hanya menjawab total bunga</sub>
- **D. Rp34.728.750,00** ✅  
  <sub>Benar: dana = 10% x 300.000.000 = 30.000.000; 30.000.000 x (1,05)^3 = Rp34.728.750,00</sub>

**Pembahasan:** Dana = 30.000.000. Nilai akhir = 30.000.000 x (1,05)^3 = Rp34.728.750,00.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b02-f-medium-bt01-012
*orisinal | C4 | 2 langkah | jenis: menentukan suku bunga dari tabel nilai akhir*

Modal Rp10.000.000,00 dibungakan majemuk per tahun. Nilai akhirnya tercatat sebagai berikut.

| Akhir tahun ke- | Nilai akhir |
|---|---|
| 2 | Rp11.236.000,00 |
| 3 | Rp11.910.160,00 |

Suku bunga majemuk per tahun pada investasi tersebut adalah ....

- A. 12,4%  
  <sub>Salah: mengira nilai akhir tahun ke-2 adalah bunga dua tahun (12,36%) lalu membulatkan</sub>
- B. 6,7%  
  <sub>Salah: membagi selisih Rp674.160,00 dengan modal awal</sub>
- C. 19,1%  
  <sub>Salah: memakai total bunga tiga tahun terhadap modal awal</sub>
- **D. 6%** ✅  
  <sub>Benar: Rp11.910.160,00 : Rp11.236.000,00 = 1,06, sehingga p = 6%</sub>

**Pembahasan:** Nilai akhir tahun ke-3 dibagi tahun ke-2 sama dengan $1+p$: 11.910.160 : 11.236.000 = 1,06. Jadi $p = 6\%$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b02-f-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: menentukan periode dari nilai akhir*

Dana Rp20.000.000,00 dibungakan majemuk 10% per tahun sehingga nilai akhirnya menjadi Rp29.282.000,00. Lama dana tersebut dibungakan adalah ....

- A. 5 tahun  
  <sub>Salah: memakai bunga tunggal: 9.282.000 : 2.000.000 = 4,64 lalu dibulatkan</sub>
- **B. 4 tahun** ✅  
  <sub>Benar: 29.282.000 : 20.000.000 = 1,4641 = (1,1)^4</sub>
- C. 6 tahun  
  <sub>Salah: (1,1)^6 menghasilkan Rp35.431.220,00, terlalu besar</sub>
- D. 3 tahun  
  <sub>Salah: (1,1)^3 hanya menghasilkan Rp26.620.000,00</sub>

**Pembahasan:** Faktor pertumbuhan = 29.282.000 : 20.000.000 = 1,4641. Karena $(1,1)^4 = 1,4641$, n = 4 tahun.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b02-f-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: bunga pada tahun tertentu*

Modal Rp20.000.000,00 dibungakan majemuk 10% per tahun. Besar bunga yang diperoleh pada tahun ketiga saja adalah ....

- A. Rp6.620.000,00  
  <sub>Salah: menjawab total bunga tiga tahun</sub>
- B. Rp2.200.000,00  
  <sub>Salah: menghitung bunga tahun kedua</sub>
- **C. Rp2.420.000,00** ✅  
  <sub>Benar: nilai akhir tahun ke-2 = Rp24.200.000,00; bunga tahun ke-3 = 10% x itu = Rp2.420.000,00</sub>
- D. Rp2.000.000,00  
  <sub>Salah: memakai bunga tahun pertama (modal awal x 10%)</sub>

**Pembahasan:** Nilai akhir 2 tahun Rp24.200.000,00; bunga tahun ketiga = 10% x Rp24.200.000,00 = Rp2.420.000,00.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b02-f-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: menganalisis hubungan suku bunga dan bunga (tidak linear)*

Modal Rp10.000.000,00 dibungakan majemuk per tahun selama 2 tahun. Suku bunga A adalah 5% dan suku bunga B adalah 10%.

Pernyataan yang benar mengenai total bunga pada B dibanding A adalah ....

- A. Nilai akhir B tepat dua kali nilai akhir A.  
  <sub>Salah: mencampur nilai akhir dengan bunga; nilai akhir B hanya 1,098 kali nilai akhir A</sub>
- **B. Total bunga B lebih dari dua kali total bunga A.** ✅  
  <sub>Benar: bunga A = Rp1.025.000,00; bunga B = Rp2.100.000,00; 2 x bunga A = Rp2.050.000,00 < bunga B</sub>
- C. Total bunga B tepat dua kali total bunga A.  
  <sub>Salah: mengira suku bunga dua kali lipat berarti bunga dua kali lipat (pola bunga tunggal)</sub>
- D. Total bunga B kurang dari dua kali total bunga A.  
  <sub>Salah: arah perbandingan terbalik</sub>

**Pembahasan:** Bunga A = Rp1.025.000,00, bunga B = Rp2.100.000,00; Rp2.100.000,00 > 2 x Rp1.025.000,00 = Rp2.050.000,00.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b02-f-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: membandingkan dua tawaran pinjaman*

Sebuah usaha membutuhkan pinjaman Rp80.000.000,00. Pinjaman X berbunga majemuk 10% per tahun selama 2 tahun, sedangkan pinjaman Y berbunga majemuk 5% per tahun selama 4 tahun.

Pinjaman yang nilai akhir pengembaliannya lebih kecil dan selisihnya adalah ....

- **A. Pinjaman X, lebih kecil Rp440.500,00** ✅  
  <sub>Benar: X: Rp96.800.000,00; Y: Rp97.240.500,00; X lebih kecil Rp440.500,00</sub>
- B. Kedua pinjaman sama besar  
  <sub>Salah: memakai bunga tunggal: 10% x 2 = 5% x 4 = 20%</sub>
- C. Pinjaman Y, lebih kecil Rp440.500,00  
  <sub>Salah: arah perbandingan tertukar</sub>
- D. Pinjaman X, lebih kecil Rp4.405.000,00  
  <sub>Salah: salah geser angka pada selisih</sub>

**Pembahasan:** X: 80.000.000 x (1,1)^2 = Rp96.800.000,00. Y: 80.000.000 x (1,05)^4 = Rp97.240.500,00. Selisih Rp440.500,00.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b02-f-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: kenaikan nilai akhir akibat periode lebih panjang*

Pinjaman Rp10.000.000,00 berbunga majemuk 10% per tahun. Kenaikan jumlah pengembalian jika lama pinjaman diperpanjang dari 2 tahun menjadi 4 tahun adalah ....

- A. Rp2.000.000,00  
  <sub>Salah: memakai bunga tunggal untuk dua tahun tambahan</sub>
- B. Rp2.100.000,00  
  <sub>Salah: menjawab total bunga 2 tahun</sub>
- **C. Rp2.541.000,00** ✅  
  <sub>Benar: 2 tahun: Rp12.100.000,00; 4 tahun: Rp14.641.000,00; kenaikan Rp2.541.000,00</sub>
- D. Rp4.641.000,00  
  <sub>Salah: menjawab total bunga 4 tahun</sub>

**Pembahasan:** Rp14.641.000,00 - Rp12.100.000,00 = Rp2.541.000,00.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b02-f-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: total bunga pinjaman (bulan ke tahun)*

Seseorang meminjam Rp25.000.000,00 dengan bunga majemuk 10% per tahun dan melunasinya sekaligus setelah 48 bulan. Total bunga yang dibayarkan adalah ....

- A. Rp10.000.000,00  
  <sub>Salah: memakai bunga tunggal (10% x 4 tahun)</sub>
- B. Rp36.602.500,00  
  <sub>Salah: menjawab nilai akhir, bukan total bunga</sub>
- C. Rp8.275.000,00  
  <sub>Salah: keliru memakai n = 3 tahun</sub>
- **D. Rp11.602.500,00** ✅  
  <sub>Benar: 4 tahun: 25.000.000 x 1,4641 = Rp36.602.500,00; bunga = Rp11.602.500,00</sub>

**Pembahasan:** Total bunga = Rp36.602.500,00 - 25.000.000 = Rp11.602.500,00.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b02-f-medium-bt01-019
*orisinal | C3 | 2 langkah | jenis: menentukan modal awal dari nilai akhir*

Sebuah dana dibungakan majemuk 5% per tahun selama 3 tahun dan nilai akhirnya menjadi Rp46.305.000,00. Modal awal dana tersebut adalah ....

- A. Rp42.000.000,00  
  <sub>Salah: memakai pangkat 2, bukan 3</sub>
- **B. Rp40.000.000,00** ✅  
  <sub>Benar: Rp46.305.000,00 : (1,05)^3 = Rp40.000.000,00</sub>
- C. Rp39.359.250,00  
  <sub>Salah: mengurangi 15% dari nilai akhir</sub>
- D. Rp44.100.000,00  
  <sub>Salah: hanya membagi dengan 1,05 satu kali</sub>

**Pembahasan:** Modal = Rp46.305.000,00 : 1,157625 = Rp40.000.000,00.
**Acuan:** siswa — siswa hal.90

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b02-f-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: membandingkan perubahan suku bunga dan periode*

Dana Rp20.000.000,00 dibungakan majemuk per tahun. Kondisi awal: suku bunga 5% selama 3 tahun. Ada dua usulan perubahan: (1) menaikkan suku bunga menjadi 6% dengan periode tetap 3 tahun, atau (2) mempertahankan suku bunga 5% tetapi memperpanjang periode menjadi 4 tahun.

Usulan yang menghasilkan nilai akhir lebih besar dan selisih kedua usulan tersebut adalah ....

- A. Usulan (1), lebih besar Rp667.820,00  
  <sub>Salah: membandingkan usulan (1) dengan kondisi awal, bukan dengan usulan (2)</sub>
- B. Usulan (2), lebih besar Rp400.000,00  
  <sub>Salah: memakai bunga tunggal pada kedua usulan</sub>
- **C. Usulan (2), lebih besar Rp489.805,00** ✅  
  <sub>Benar: (1): Rp23.820.320,00; (2): Rp24.310.125,00; (2) lebih besar Rp489.805,00</sub>
- D. Usulan (1), lebih besar Rp489.805,00  
  <sub>Salah: arah perbandingan tertukar</sub>

**Pembahasan:** (1) 20.000.000 x (1,06)^3 = Rp23.820.320,00. (2) 20.000.000 x (1,05)^4 = Rp24.310.125,00. Selisih Rp489.805,00.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b02-f-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim periode dan total bunga*

Dina menyatakan: "Jika periode bunga majemuk digandakan dari 2 tahun menjadi 4 tahun, total bunga yang diperoleh juga tepat dua kali lipat." Modal Rp10.000.000,00 dibungakan majemuk 10% per tahun.

Pernyataan yang benar mengenai klaim Dina adalah ....

- A. Klaim salah: total bunga 4 tahun Rp4.641.000,00 kurang dari dua kali total bunga 2 tahun Rp2.100.000,00.  
  <sub>Salah: arah perbandingan terbalik, padahal 4.641.000 melebihi 4.200.000</sub>
- B. Klaim benar: total bunga 4 tahun Rp4.200.000,00, tepat dua kali total bunga 2 tahun Rp2.100.000,00.  
  <sub>Salah: memakai pola bunga tunggal yang linear terhadap periode</sub>
- C. Klaim salah: total bunga 4 tahun hanya Rp2.541.000,00, yaitu selisih nilai akhir 4 tahun dan 2 tahun.  
  <sub>Salah: mengambil kenaikan nilai akhir sebagai total bunga 4 tahun</sub>
- **D. Klaim salah: total bunga 4 tahun Rp4.641.000,00 lebih dari dua kali total bunga 2 tahun Rp2.100.000,00.** ✅  
  <sub>Benar: bunga 2 tahun Rp2.100.000,00; bunga 4 tahun Rp4.641.000,00 > 2 x 2.100.000 = 4.200.000</sub>

**Pembahasan:** Nilai akhir 2 tahun Rp12.100.000,00 (bunga Rp2.100.000,00); 4 tahun Rp14.641.000,00 (bunga Rp4.641.000,00). Karena 4.641.000 > 4.200.000, total bunga lebih dari dua kali lipat, klaim salah.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b02-f-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: merancang periode agar target tercapai*

Dana Rp40.000.000,00 dibungakan majemuk 10% per tahun. Paling sedikit berapa tahun (bilangan bulat) agar nilai akhir dana itu minimal dua kali modal awal?

- **A. 8 tahun** ✅  
  <sub>Benar: $(1,1)^7 = 1,9487 < 2$ sedangkan $(1,1)^8 = 2,1436 \geq 2$</sub>
- B. 7 tahun  
  <sub>Salah: pembulatan ke bawah: $(1,1)^7 = 1,9487$ masih kurang dari 2</sub>
- C. 10 tahun  
  <sub>Salah: memakai bunga tunggal: 100% : 10% = 10 tahun</sub>
- D. 9 tahun  
  <sub>Salah: memilih satu tahun lebih lama dari yang diperlukan</sub>

**Pembahasan:** Uji pangkat: $(1,1)^7 = 1,9487$ belum cukup, $(1,1)^8 = 2,1436$ sudah melebihi 2. Jadi paling sedikit 8 tahun.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b02-f-hard-bt01-003
*orisinal | C6 | 4 langkah | jenis: merancang suku bunga minimal*

Dana Rp40.000.000,00 diinvestasikan 3 tahun dengan bunga majemuk per tahun. Agar nilai akhirnya minimal Rp50.000.000,00, suku bunga bulat per tahun paling kecil yang dapat dipilih adalah ....

- **A. 8%** ✅  
  <sub>Benar: 8%: Rp50.388.480,00 (cukup); 7%: Rp49.001.720,00 (kurang dari 50.000.000)</sub>
- B. 9%  
  <sub>Salah: memakai bunga tunggal: 25% : 3 = 8,33% lalu dibulatkan ke atas</sub>
- C. 7%  
  <sub>Salah: nilai akhir hanya Rp49.001.720,00, belum mencapai target</sub>
- D. 13%  
  <sub>Salah: memakai n = 2 (25% : 2 = 12,5%) lalu dibulatkan ke atas</sub>

**Pembahasan:** Uji: $40.000.000 \times (1,07)^3 = Rp49.001.720,00$ (kurang), $40.000.000 \times (1,08)^3 = Rp50.388.480,00$ (cukup). Jadi 8%.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b02-f-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: syarat ganda skema investasi*

Dana Rp50.000.000,00 akan diinvestasikan dengan bunga majemuk per tahun. Syarat: (i) nilai akhir minimal Rp60.000.000,00, (ii) suku bunga tidak lebih dari 8% per tahun, (iii) periode tidak lebih dari 3 tahun. Skema yang memenuhi ketiga syarat adalah ....

- A. suku bunga 10% per tahun selama 2 tahun  
  <sub>Salah: nilai akhir Rp60.500.000,00 cukup, tetapi suku bunga 10% melebihi 8%</sub>
- **B. suku bunga 8% per tahun selama 3 tahun** ✅  
  <sub>Benar: nilai akhir Rp62.985.600,00 >= 60.000.000; 8% <= 8%; 3 tahun <= 3 tahun</sub>
- C. suku bunga 6% per tahun selama 3 tahun  
  <sub>Salah: suku bunga dan periode memenuhi, tetapi nilai akhir Rp59.550.800,00 kurang dari 60.000.000</sub>
- D. suku bunga 5% per tahun selama 4 tahun  
  <sub>Salah: nilai akhir Rp60.775.312,50 cukup, tetapi periode 4 tahun melebihi 3 tahun</sub>

**Pembahasan:** Skema 8%/3 tahun: 62.985.600 memenuhi semua. 5%/4 tahun melanggar periode, 10%/2 tahun melanggar suku bunga, 6%/3 tahun melanggar nilai akhir.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b02-f-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: perbandingan investasi dan pinjaman*

Pak Anton meminjam Rp100.000.000,00 dengan bunga majemuk 6% per tahun dan menaruh seluruh uangnya pada deposito berbunga majemuk 8% per tahun. Setelah 3 tahun, deposito dicairkan dan pinjaman dilunasi sekaligus. Keuntungan bersih Pak Anton adalah ....

- A. Rp4.280.000,00  
  <sub>Salah: memakai n = 2 tahun pada kedua perhitungan</sub>
- B. Rp125.971.200,00  
  <sub>Salah: hanya menjawab nilai akhir deposito, belum dikurangi pelunasan</sub>
- C. Rp6.000.000,00  
  <sub>Salah: memakai bunga tunggal: selisih 2% x 3 tahun x 100.000.000</sub>
- **D. Rp6.869.600,00** ✅  
  <sub>Benar: deposito Rp125.971.200,00; pelunasan Rp119.101.600,00; selisih Rp6.869.600,00</sub>

**Pembahasan:** Deposito: $100.000.000 \times (1,08)^3 = 125.971.200$. Pelunasan: $100.000.000 \times (1,06)^3 = 119.101.600$. Untung bersih 6.869.600.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b02-f-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan langkah perhitungan*

Dina menghitung nilai akhir modal Rp20.000.000,00 dengan bunga majemuk 10% per tahun selama 3 tahun:

| Tahun | Perhitungan Dina | Hasil |
|---|---|---|
| 1 | 20.000.000 + 10% x 20.000.000 | 22.000.000 |
| 2 | 22.000.000 + 10% x 20.000.000 | 24.000.000 |
| 3 | 24.000.000 + 10% x 20.000.000 | 26.000.000 |

Pernyataan yang benar mengenai pekerjaan Dina adalah ....

- A. Kesalahan hanya pada tahun ke-3: bunga tahun ke-3 seharusnya 10% x 26.000.000; nilai akhir yang benar Rp28.600.000,00.  
  <sub>Salah: mengira kesalahan baru muncul di tahun ke-3 dan memakai hasil Dina sebagai dasar</sub>
- B. Kesalahan mulai pada tahun ke-2: bunga dihitung dari modal awal; nilai akhir yang benar Rp26.000.000,00.  
  <sub>Salah: menyebut nilai akhir hasil perhitungan Dina sebagai nilai yang benar</sub>
- **C. Kesalahan mulai pada tahun ke-2: bunga dihitung dari modal awal, bukan dari nilai akhir tahun ke-1; nilai akhir yang benar Rp26.620.000,00.** ✅  
  <sub>Benar: tahun 2: 10% x 22.000.000 = 2.200.000 sehingga 24.200.000; tahun 3: 10% x 24.200.000 = 2.420.000 sehingga 26.620.000</sub>
- D. Kesalahan mulai pada tahun ke-1: bunga seharusnya dihitung dari 10% x 22.000.000; nilai akhir yang benar Rp26.620.000,00.  
  <sub>Salah: menunjuk langkah yang salah; tahun ke-1 sudah benar</sub>

**Pembahasan:** Nilai akhir yang benar: $20.000.000 \times (1,1)^3 = 26.620.000$. Dina memakai bunga tetap 2.000.000 (pola bunga tunggal) sejak tahun ke-2.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b02-f-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan satuan periode*

Rani meminjam Rp12.000.000,00 dengan bunga majemuk 6% per tahun untuk periode 36 bulan. Ia menulis jumlah pengembalian $12.000.000 \times (1,06)^{36}$. Pernyataan yang benar mengenai pekerjaan Rani adalah ....

- **A. Salah: periode harus dinyatakan dalam tahun, yaitu $n = 3$, sehingga jumlah pengembalian Rp14.292.192,00.** ✅  
  <sub>Benar: 36 bulan = 3 tahun; 12.000.000 x (1,06)^3 = 14.292.192</sub>
- B. Salah: periode $n = 3$, tetapi memakai bunga tunggal sehingga jumlah pengembalian Rp14.160.000,00.  
  <sub>Salah: mengubah ke bunga tunggal: 12.000.000 x (1 + 0,06 x 3)</sub>
- C. Salah: periode $n = 3$, tetapi faktor seharusnya $1,6$ sehingga jumlah pengembalian Rp49.152.000,00.  
  <sub>Salah: salah mengubah 6% menjadi 0,6</sub>
- D. Benar: bunga per tahun dipangkatkan dengan banyaknya bulan pinjaman.  
  <sub>Salah: tidak menyadari satuan periode harus sama dengan satuan suku bunga (tahun)</sub>

**Pembahasan:** Suku bunga per tahun sehingga $n$ dalam tahun: 36 : 12 = 3. Jumlah pengembalian $12.000.000 \times (1,06)^3 = 14.292.192$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b02-f-hard-bt01-008
*orisinal | C6 | 4 langkah | jenis: merancang batas suku bunga pinjaman*

Seorang peminjam menerima pinjaman Rp50.000.000,00 dengan bunga majemuk per tahun dan melunasinya sekaligus setelah 3 tahun. Ia hanya sanggup mengembalikan paling banyak Rp66.000.000,00. Suku bunga bulat per tahun terbesar yang masih dapat ia terima adalah ....

- A. 8%  
  <sub>Salah: memenuhi batas (Rp62.985.600,00) tetapi bukan yang terbesar</sub>
- B. 10%  
  <sub>Salah: pembulatan ke atas; pengembalian Rp66.550.000,00 melebihi batas</sub>
- C. 11%  
  <sub>Salah: memakai bunga tunggal: 32% : 3 = 10,67% lalu dibulatkan ke atas</sub>
- **D. 9%** ✅  
  <sub>Benar: 9%: Rp64.751.450,00 <= 66.000.000; 10%: Rp66.550.000,00 > 66.000.000</sub>

**Pembahasan:** Uji: 9% memberi 64.751.450 (memenuhi), 10% memberi 66.550.000 (melebihi 66.000.000). Maka maksimum 9%.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b02-f-hard-bt01-009
*orisinal | C6 | 4 langkah | jenis: merancang lama pinjaman maksimal (bulan)*

Pinjaman Rp30.000.000,00 berbunga majemuk 20% per tahun. Agar jumlah pengembalian tidak melebihi Rp45.000.000,00, lama pinjaman (dalam kelipatan tahun penuh) paling lama adalah ....

- A. 30 bulan  
  <sub>Salah: memakai bunga tunggal: 50% : 20% = 2,5 tahun, bukan kelipatan tahun penuh</sub>
- **B. 24 bulan** ✅  
  <sub>Benar: 2 tahun: Rp43.200.000,00 <= 45.000.000; 3 tahun: Rp51.840.000,00 > 45.000.000</sub>
- C. 12 bulan  
  <sub>Salah: memenuhi batas tetapi bukan yang paling lama</sub>
- D. 36 bulan  
  <sub>Salah: pengembalian Rp51.840.000,00 melebihi batas</sub>

**Pembahasan:** $30.000.000 \times (1,2)^2 = 43.200.000$ (memenuhi), $30.000.000 \times (1,2)^3 = 51.840.000$ (melebihi). Jadi 2 tahun = 24 bulan.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b02-f-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: rentang nilai akhir dari batas parameter*

Dana Rp100.000.000,00 akan diinvestasikan oleh konsultan dengan bunga majemuk per tahun. Suku bunga yang mungkin terjadi 3%-7% per tahun dan periode yang mungkin 2-4 tahun. Selisih antara nilai akhir terbesar dan nilai akhir terkecil yang mungkin adalah ....

- A. Rp22.000.000,00  
  <sub>Salah: memakai bunga tunggal: 28% - 6% dari modal</sub>
- B. Rp1.939.119,00  
  <sub>Salah: memasangkan suku bunga terbesar dengan periode terpendek dan sebaliknya</sub>
- **C. Rp24.989.601,00** ✅  
  <sub>Benar: terbesar (7%, 4 tahun) Rp131.079.601,00; terkecil (3%, 2 tahun) Rp106.090.000,00</sub>
- D. Rp18.528.720,00  
  <sub>Salah: periode dibuat sama (4 tahun), padahal terkecil memakai periode 2 tahun</sub>

**Pembahasan:** Nilai akhir naik bila suku bunga dan periode naik. Terbesar: 100.000.000 x (1,07)^4 = 131.079.601. Terkecil: 100.000.000 x (1,03)^2 = 106.090.000. Selisih 24.989.601.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b02-f-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: menyusun parameter dari data lalu memprediksi*

Nilai akhir sebuah investasi berbunga majemuk per tahun:

| Akhir tahun ke- | Nilai akhir |
|---|---|
| 2 | Rp14.520.000,00 |
| 3 | Rp15.972.000,00 |

Dengan suku bunga yang sama, nilai akhir investasi tersebut pada akhir tahun ke-5 adalah ....

- A. Rp18.876.000,00  
  <sub>Salah: memperpanjang pola linear: menambah bunga tahun ke-3 (1.452.000) dua kali</sub>
- B. Rp21.258.732,00  
  <sub>Salah: memakai n = 6 karena salah menghitung modal awal dan periode</sub>
- **C. Rp19.326.120,00** ✅  
  <sub>Benar: 15.972.000 : 14.520.000 = 1,1 sehingga $p = 10\%$; nilai akhir tahun ke-5 = 15.972.000 x (1,1)^2 = 19.326.120</sub>
- D. Rp17.569.200,00  
  <sub>Salah: menjawab nilai akhir tahun ke-4, bukan tahun ke-5</sub>

**Pembahasan:** Rasio 15.972.000 : 14.520.000 = 1,1 sehingga $p = 10\%$. Nilai akhir tahun ke-5 = $15.972.000 \times (1,1)^2 = 19.326.120$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b02-f-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: evaluasi beberapa pernyataan*

Modal Rp10.000.000,00 dibungakan majemuk 10% per tahun. Perhatikan pernyataan berikut.

(1) Nilai akhir setelah 3 tahun, Rp13.310.000,00, lebih besar dari nilai akhir bunga tunggal 3 tahun, Rp13.000.000,00.
(2) Besar bunga pada tahun ke-3 sama dengan besar bunga pada tahun ke-2.
(3) Jika suku bunga dinaikkan menjadi 20% untuk periode 2 tahun, total bunga menjadi tepat dua kali total bunga pada 10% untuk periode 2 tahun.
(4) Memperpanjang periode dari 2 tahun menjadi 3 tahun menambah nilai akhir sebesar Rp1.210.000,00.

Pernyataan yang benar adalah ....

- A. (1), (3), dan (4)  
  <sub>Salah: menganggap (3) benar karena suku bunga dua kali lipat</sub>
- B. (2) dan (4) saja  
  <sub>Salah: mengira bunga tiap tahun sama besar padahal bunga tahun ke-3 lebih besar</sub>
- C. (1) dan (3) saja  
  <sub>Salah: mengira bunga dua kali lipat saat suku bunga dua kali lipat (pola bunga tunggal)</sub>
- **D. (1) dan (4) saja** ✅  
  <sub>Benar: (1) benar (13.310.000 > 13.000.000); (2) salah (1.100.000 dan 1.210.000); (3) salah (4.400.000 vs 2.100.000, bukan dua kali); (4) benar (13.310.000 - 12.100.000)</sub>

**Pembahasan:** Bunga tahun ke-2 = 1.100.000, tahun ke-3 = 1.210.000, sehingga (2) salah. Total bunga 20% selama 2 tahun = 4.400.000 > 2 x 2.100.000, sehingga (3) salah. (1) dan (4) benar.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b02-f-hard-bt01-013
*orisinal | C6 | 5 langkah | jenis: membandingkan dua pinjaman dengan periode berbeda*

Pinjaman P berbunga majemuk 10% per tahun selama 3 tahun. Pinjaman Q dengan pokok yang sama berbunga majemuk 6% per tahun. Lama pinjaman Q (dalam tahun penuh) paling lama agar jumlah pengembalian Q tidak melebihi jumlah pengembalian P adalah ....

- A. 6 tahun  
  <sub>Salah: mengambil periode pertama yang melebihi batas lalu menambah 1</sub>
- **B. 4 tahun** ✅  
  <sub>Benar: $(1,1)^3 = 1,331$; $(1,06)^4 = 1,2625 \leq 1,331$; $(1,06)^5 = 1,3382 > 1,331$</sub>
- C. 3 tahun  
  <sub>Salah: menyamakan periode kedua pinjaman, padahal Q masih lebih murah</sub>
- D. 5 tahun  
  <sub>Salah: memakai bunga tunggal: 30% : 6% = 5 tahun; pada majemuk 1,3382 sudah melebihi 1,331</sub>

**Pembahasan:** Faktor P = 1,331. Q: 4 tahun 1,2625 (boleh), 5 tahun 1,3382 (melebihi). Jadi paling lama 4 tahun.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b02-f-hard-bt01-014
*orisinal | C6 | 6 langkah | jenis: titik silang dua skema investasi*

Skema A: modal Rp100.000.000,00 berbunga majemuk 10% per tahun. Skema B: modal Rp110.000.000,00 berbunga majemuk 8% per tahun. Paling sedikit berapa tahun (bilangan bulat) agar nilai akhir Skema A lebih besar dari nilai akhir Skema B?

- **A. 6 tahun** ✅  
  <sub>Benar: tahun ke-5: A Rp161.051.000,00 < B sekitar Rp161.626.088; tahun ke-6: A Rp177.156.100,00 > B sekitar Rp174.556.175</sub>
- B. 5 tahun  
  <sub>Salah: A baru Rp161.051.000,00, masih lebih kecil dari B (sekitar Rp161.626.088)</sub>
- C. 9 tahun  
  <sub>Salah: memakai bunga tunggal: 100 + 10n > 110 + 8,8n sehingga n > 8,33</sub>
- D. 7 tahun  
  <sub>Salah: memilih satu tahun setelah urutan berbalik</sub>

**Pembahasan:** Tahun ke-5: A 161.051.000 < B sekitar 161.626.088. Tahun ke-6: A 177.156.100 > B sekitar 174.556.175 Maka paling sedikit 6 tahun.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b02-f-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: syarat ganda anggaran dan nilai terbesar*

Sebuah usaha meminjam Rp50.000.000,00 dengan bunga majemuk per tahun dan sanggup mengembalikan paling banyak Rp65.000.000,00. Di antara pilihan berikut yang memenuhi batas itu, skema dengan jumlah pengembalian paling besar (paling menguntungkan bagi pemberi pinjaman) adalah ....

- A. suku bunga 8% per tahun selama 3 tahun  
  <sub>Salah: memenuhi batas (Rp62.985.600,00) tetapi bukan yang terbesar</sub>
- **B. suku bunga 9% per tahun selama 3 tahun** ✅  
  <sub>Benar: pengembalian Rp64.751.450,00 <= 65.000.000 dan lebih besar dari 8%/3 tahun (Rp62.985.600,00)</sub>
- C. suku bunga 10% per tahun selama 3 tahun  
  <sub>Salah: pengembalian Rp66.550.000,00 melebihi batas</sub>
- D. suku bunga 7% per tahun selama 4 tahun  
  <sub>Salah: pengembalian Rp65.539.800,50 melebihi batas</sub>

**Pembahasan:** Skema 9%/3 tahun 64.751.450 memenuhi dan lebih besar dari 8%/3 tahun 62.985.600. Skema 10%/3 tahun dan 7%/4 tahun melebihi 65.000.000.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b02-f-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim periode vs suku bunga*

Seorang konsultan menyatakan: "Memperpanjang periode 1 tahun selalu lebih menguntungkan daripada menaikkan suku bunga 2 poin persen." Sebagai contoh, dana Rp100.000.000,00 berbunga majemuk 3% per tahun selama 3 tahun.

Pernyataan yang benar mengenai klaim konsultan pada contoh tersebut adalah ....

- **A. Klaim salah: menaikkan suku bunga menjadi 5% memberi Rp115.762.500,00, lebih besar dari periode 4 tahun yang memberi Rp112.550.881,00.** ✅  
  <sub>Benar: periode 4 tahun pada 3%: 112.550.881; suku bunga 5% selama 3 tahun: 115.762.500</sub>
- B. Klaim salah: menaikkan suku bunga menjadi 5% memberi Rp115.000.000,00, lebih besar dari periode 4 tahun yang memberi Rp112.000.000,00.  
  <sub>Salah: memakai bunga tunggal pada kedua nilai</sub>
- C. Klaim benar: periode 4 tahun memberi Rp112.550.881,00, sedangkan suku bunga 5% hanya memberi Rp105.000.000,00.  
  <sub>Salah: hanya menghitung bunga satu tahun untuk suku bunga 5%</sub>
- D. Klaim salah: periode 4 tahun memberi Rp112.550.881,00 dan suku bunga 5% memberi Rp115.762.500,00, sehingga keduanya sama menguntungkan.  
  <sub>Salah: kesimpulan tidak sesuai nilai: kedua nilai berbeda</sub>

**Pembahasan:** Periode 4 tahun: $100.000.000 \times (1,03)^4 = 112.550.881$. Suku bunga 5%: $100.000.000 \times (1,05)^3 = 115.762.500$. Contoh penyangkal menunjukkan klaim salah.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b02-f-hard-bt01-017
*orisinal | C6 | 4 langkah | jenis: merancang modal awal minimal*

Seorang ayah ingin dana pendidikan anaknya mencapai minimal Rp100.000.000,00 setelah 4 tahun pada deposito berbunga majemuk 5% per tahun. Modal awal (dalam kelipatan jutaan rupiah) paling kecil yang harus disetor adalah ....

- A. Rp80.000.000,00  
  <sub>Salah: memakai bunga tunggal: dikurangi 4 x 5% = 20% dari target</sub>
- B. Rp95.000.000,00  
  <sub>Salah: hanya mengurangi 5% sekali dari target</sub>
- **C. Rp83.000.000,00** ✅  
  <sub>Benar: 83 juta: Rp100.887.018,75 >= 100.000.000; 82 juta: Rp99.671.512,50 < 100.000.000</sub>
- D. Rp82.000.000,00  
  <sub>Salah: pembulatan ke bawah: nilai akhir hanya Rp99.671.512,50</sub>

**Pembahasan:** $100.000.000 : (1,05)^4 = 82.270.247$ (kira-kira). Dalam kelipatan jutaan, paling kecil 83 juta.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
