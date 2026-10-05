# Lembar koreksi — kelas12 SMA12U-B2 subbab B: Investasi Bunga Majemuk

55 soal | easy 20, medium 20, hard 15 | variasi 20, orisinal 35
> **Kapasitas kurang (hard): 15 dari kuota 20** — Materi subbab B (bunga majemuk) sempit: hanya rumus M(1+p)^n, p per periode, dan tabel pangkat. Setelah easy dan medium memakai semua acuan variasi dan sudut hitung dasar, hard yang layak (evaluasi klaim, temukan kesalahan, penyangkal, perbandingan skema, rancang) hanya cukup 15 soal tanpa nyaris kembar atau di luar materi.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b02-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: modal akhir bunga majemuk (tahun)*

Modal sebesar Rp2.000.000,00 dibungakan dengan bunga majemuk 20% per tahun. Tentukan modal akhir setelah 3 tahun.

- A. Rp2.880.000,00  
  <sub>Salah: pangkat n dikurangi satu (n-1)</sub>
- **B. Rp3.456.000,00** ✅  
  <sub>Benar: $2.000.000 \times (1,2)^3 = 3.456.000$</sub>
- C. Rp3.200.000,00  
  <sub>Salah: memakai bunga tunggal (20% x 3 tahun) bukan majemuk</sub>
- D. Rp1.456.000,00  
  <sub>Salah: yang dihitung hanya bunganya, bukan modal akhir</sub>

**Pembahasan:** $M_n = M(1+p)^n = 2.000.000(1,2)^3 = 3.456.000$. Modal akhir Rp3.456.000,00.
**Acuan:** siswa — siswa hal.62 Contoh 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b02-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: bunga yang diperoleh*

Modal sebesar Rp8.000.000,00 dibungakan dengan bunga majemuk 5% per tahun. Tentukan bunga yang diperoleh setelah 2 tahun.

- A. Rp400.000,00  
  <sub>Salah: hanya menghitung bunga tahun pertama</sub>
- B. Rp800.000,00  
  <sub>Salah: memakai bunga tunggal 8.000.000 x 5% x 2</sub>
- C. Rp8.820.000,00  
  <sub>Salah: menjawab modal akhir, bukan bunganya</sub>
- **D. Rp820.000,00** ✅  
  <sub>Benar: modal akhir 8.820.000 dikurangi modal awal 8.000.000</sub>

**Pembahasan:** $M_2 = 8.000.000(1,05)^2 = 8.820.000$. Bunga = 8.820.000 - 8.000.000 = 820.000.
**Acuan:** siswa — siswa hal.62 Contoh 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b02-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: modal awal dari saldo akhir*

Dina menabung uang di bank dengan bunga majemuk sebesar 10% per 6 bulan. Setelah 12 bulan menabung, saldo tabungan menjadi sebesar Rp3.630.000,00. Berapakah jumlah uang yang ditabung Dina semula?

- **A. Rp3.000.000,00** ✅  
  <sub>Benar: n = 2 periode, $3.630.000 : (1,1)^2 = 3.000.000$</sub>
- B. Rp3.300.000,00  
  <sub>Salah: memakai n = 1 padahal ada 2 periode</sub>
- C. Rp3.025.000,00  
  <sub>Salah: menganggap bunga 10% x 2 = 20% (bunga tunggal) lalu membagi 1,2</sub>
- D. Rp2.904.000,00  
  <sub>Salah: mengurangi 20% dari saldo, bukan membagi faktor bunga</sub>

**Pembahasan:** 12 bulan = 2 periode 6 bulan. $M(1,1)^2 = 3.630.000$ sehingga $M = 3.630.000 : 1,21 = 3.000.000$.
**Acuan:** siswa — siswa hal.63 Contoh 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b02-b-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: modal awal dari saldo akhir (koperasi)*

Pak Dodi menyimpan uang di koperasi yang memberi bunga majemuk 4% per 2 bulan. Simpanan Pak Dodi menjadi Rp5.408.000,00 setelah 4 bulan. Berapa besar simpanan awal Pak Dodi?

- **A. Rp5.000.000,00** ✅  
  <sub>Benar: n = 2 periode, $5.408.000 : (1,04)^2 = 5.000.000$</sub>
- B. Rp4.975.360,00  
  <sub>Salah: mengurangi 8% dari saldo, bukan membagi faktor bunga</sub>
- C. Rp408.000,00  
  <sub>Salah: menjawab bunga, bukan simpanan awal</sub>
- D. Rp5.200.000,00  
  <sub>Salah: memakai n = 1 padahal ada 2 periode</sub>

**Pembahasan:** 4 bulan = 2 periode. $M = 5.408.000 : 1,0816 = 5.000.000$.
**Acuan:** siswa — siswa hal.63 Contoh 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b02-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: nilai akhir investasi (saham)*

Seseorang berinvestasi emas di suatu aplikasi online. Modal yang diberikan sebesar Rp4.000.000,00. Keuntungan yang didapat menggunakan suku bunga majemuk 10% per tahun. Hitunglah nilai akhir modal tersebut setelah 4 tahun.

- A. Rp1.856.400,00  
  <sub>Salah: menjawab bunga saja, bukan nilai akhir</sub>
- B. Rp5.600.000,00  
  <sub>Salah: memakai bunga tunggal (10% x 4)</sub>
- **C. Rp5.856.400,00** ✅  
  <sub>Benar: $4.000.000 \times (1,1)^4 = 5.856.400$</sub>
- D. Rp5.324.000,00  
  <sub>Salah: pangkat n dikurangi satu</sub>

**Pembahasan:** $M_4 = 4.000.000(1,1)^4 = 4.000.000 \times 1,4641 = 5.856.400$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b02-b-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: nilai akhir investasi (reksa dana)*

Bu Sari menanamkan modal Rp12.000.000,00 pada reksa dana yang memberi imbal hasil majemuk 5% per tahun. Berapa nilai akhir investasinya setelah 2 tahun?

- A. Rp1.230.000,00  
  <sub>Salah: menjawab bunga, bukan nilai akhir</sub>
- **B. Rp13.230.000,00** ✅  
  <sub>Benar: $12.000.000 \times (1,05)^2 = 13.230.000$</sub>
- C. Rp12.600.000,00  
  <sub>Salah: hanya menghitung satu tahun</sub>
- D. Rp13.200.000,00  
  <sub>Salah: memakai bunga tunggal (5% x 2)</sub>

**Pembahasan:** $M_2 = 12.000.000 \times 1,1025 = 13.230.000$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b02-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: bunga tahunan dibayar bulanan*

Budi menyimpan uang sejumlah Rp10.000.000,00 di bank yang menawarkan bunga majemuk sebesar 12% setiap tahun dengan pembayaran setiap bulan. Setelah 3 bulan, Budi mencairkan seluruh uangnya. Total nilai uang Budi sebesar ....

- A. Rp14.049.280,00  
  <sub>Salah: memakai 12% sebagai bunga per bulan</sub>
- **B. Rp10.303.010,00** ✅  
  <sub>Benar: bunga 1% per bulan, $10.000.000(1,01)^3 = 10.303.010$</sub>
- C. Rp10.300.000,00  
  <sub>Salah: bunga 1% per bulan dihitung tunggal (3 x 100.000)</sub>
- D. Rp10.927.270,00  
  <sub>Salah: membagi 12% dengan 4 (bukan 12) lalu dipangkatkan 3</sub>

**Pembahasan:** 12% per tahun dengan pembayaran bulanan = 1% per bulan. $M_3 = 10.000.000(1,01)^3 = 10.303.010$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b02-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: modal akhir deposito (tahun)*

Bu Wati menabung uang di bank sebesar Rp30.000.000,00 dengan bunga majemuk 2% per tahun selama 2 tahun. Modal akhir Bu Wati adalah ....

- A. Rp1.212.000,00  
  <sub>Salah: menjawab bunga saja</sub>
- B. Rp31.200.000,00  
  <sub>Salah: bunga tunggal 2% x 2 tahun</sub>
- **C. Rp31.212.000,00** ✅  
  <sub>Benar: $30.000.000(1,02)^2 = 31.212.000$</sub>
- D. Rp30.600.000,00  
  <sub>Salah: hanya satu tahun</sub>

**Pembahasan:** $M_2 = 30.000.000 \times 1,0404 = 31.212.000$.
**Acuan:** siswa — siswa hal.59 Ayo, Berkolaborasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b02-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: simpanan awal dari tabel pangkat*

Koperasi Harapan memiliki program simpanan berjangka dengan suku bunga majemuk 4% per semester selama 18 bulan. Simpanan Bu Lastri saat ini mencapai Rp56.243.200,00. Diketahui $(1,04)^3 = 1,124864$. Simpanan awal Bu Lastri adalah ....

- A. Rp54.080.000,00  
  <sub>Salah: memakai n = 1 (dibagi 1,04)</sub>
- B. Rp6.243.200,00  
  <sub>Salah: menjawab bunga, bukan simpanan awal</sub>
- **C. Rp50.000.000,00** ✅  
  <sub>Benar: 18 bulan = 3 semester, $56.243.200 : 1,124864 = 50.000.000$</sub>
- D. Rp52.000.000,00  
  <sub>Salah: memakai n = 2 (dibagi 1,0816)</sub>

**Pembahasan:** 18 bulan = 3 semester. $M = 56.243.200 : 1,124864 = 50.000.000$.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b02-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: persentase bunga total*

Suatu tabungan berbunga majemuk 10% per tahun selama 3 tahun. Diketahui $(1,1)^3 = 1,331$. Total bunga yang diterima adalah ... dari tabungan awal.

- A. 3,31%  
  <sub>Salah: salah menaruh koma desimal</sub>
- B. 133,1%  
  <sub>Salah: menyebut persentase modal akhir, bukan bunga</sub>
- C. 30%  
  <sub>Salah: memakai bunga tunggal 10% x 3</sub>
- **D. 33,1%** ✅  
  <sub>Benar: faktor 1,331 berarti bertambah 0,331 atau 33,1%</sub>

**Pembahasan:** Modal akhir = 1,331 M, bunga = 0,331 M = 33,1% dari tabungan awal.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b02-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: bunga tahunan dibayar bulanan*

Dewi menyimpan uang sejumlah Rp2.000.000,00 di bank yang menawarkan bunga majemuk sebesar 24% setiap tahun dengan pembayaran setiap bulan. Setelah 2 bulan, seluruh uang dicairkan. Total nilai uang Dewi sebesar ....

- A. Rp3.075.200,00  
  <sub>Salah: memakai 24% sebagai bunga per bulan</sub>
- B. Rp2.080.000,00  
  <sub>Salah: bunga 2% per bulan dihitung tunggal</sub>
- C. Rp2.508.800,00  
  <sub>Salah: membagi 24% dengan 2 (bukan 12)</sub>
- **D. Rp2.080.800,00** ✅  
  <sub>Benar: bunga 2% per bulan, $2.000.000(1,02)^2 = 2.080.800$</sub>

**Pembahasan:** 24% per tahun dengan pembayaran bulanan = 2% per bulan. $M_2 = 2.000.000 \times 1,0404 = 2.080.800$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b02-b-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: bunga pada tahun tertentu*

Modal Rp20.000.000,00 dibungakan dengan bunga majemuk 5% per tahun. Besar bunga yang diterima pada tahun ketiga adalah ....

- A. Rp1.050.000,00  
  <sub>Salah: memakai bunga tahun kedua</sub>
- B. Rp1.000.000,00  
  <sub>Salah: memakai modal awal (bunga tunggal) untuk tahun ketiga</sub>
- **C. Rp1.102.500,00** ✅  
  <sub>Benar: modal awal tahun ketiga 22.050.000, bunga 5% darinya</sub>
- D. Rp23.152.500,00  
  <sub>Salah: menjawab modal akhir tahun ketiga, bukan bunganya</sub>

**Pembahasan:** Tahun 1: 21.000.000; tahun 2: 22.050.000. Bunga tahun ke-3 = 5% x 22.050.000 = 1.102.500.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b02-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: konsep bunga majemuk*

Pernyataan yang benar tentang bunga majemuk adalah ....

- A. Bunga hanya dihitung satu kali di akhir seluruh periode dari modal awal  
  <sub>Salah: salah paham bahwa bunga tidak dihitung tiap periode</sub>
- B. Bunga tiap periode selalu sama besar karena dihitung dari modal awal  
  <sub>Salah: mencampur dengan sifat bunga tunggal</sub>
- C. Bunga tiap periode dihitung hanya dari bunga periode sebelumnya tanpa modal  
  <sub>Salah: menganggap dasar bunga hanya bunga lama</sub>
- **D. Bunga tiap periode dihitung dari modal pada periode berjalan sehingga besarnya berubah dari periode ke periode** ✅  
  <sub>Benar: sesuai definisi di buku</sub>

**Pembahasan:** Bunga majemuk dihitung dari modal pada periode berjalan (modal + bunga sebelumnya), sehingga bunga periode pertama, kedua, dan seterusnya berbeda.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b02-b-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: banyak periode bunga*

Sebuah bank memberi bunga majemuk 2% per triwulan. Sebuah tabungan disimpan selama 2 tahun. Banyak periode bunga (n) yang digunakan dalam rumus adalah ....

- A. 6  
  <sub>Salah: menganggap satu periode 4 bulan (24 : 4)</sub>
- B. 2  
  <sub>Salah: memakai lama dalam tahun sebagai n</sub>
- **C. 8** ✅  
  <sub>Benar: 2 tahun = 24 bulan; 1 triwulan = 3 bulan; 24 : 3 = 8</sub>
- D. 24  
  <sub>Salah: memakai lama dalam bulan sebagai n</sub>

**Pembahasan:** Triwulan = 3 bulan. 2 tahun = 24 bulan sehingga n = 24 : 3 = 8.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b02-b-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: faktor (1+p)*

Suatu modal dibungakan dengan bunga majemuk 7,5% per tahun. Pada rumus $M_n = M(1+p)^n$, nilai $(1+p)$ adalah ....

- A. 0,075  
  <sub>Salah: lupa menambah 1</sub>
- **B. 1,075** ✅  
  <sub>Benar: p = 7,5% = 0,075 sehingga 1 + p = 1,075</sub>
- C. 7,5  
  <sub>Salah: tidak mengubah persen ke desimal</sub>
- D. 1,75  
  <sub>Salah: salah nilai desimal 7,5% (0,75)</sub>

**Pembahasan:** $p = 7,5\% = 0,075$ sehingga $1+p = 1,075$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b02-b-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: bunga tunggal vs majemuk*

Anto dan Beni masing-masing menabung Rp10.000.000,00 selama 2 tahun dengan bunga 10% per tahun. Anto memakai bunga tunggal, Beni memakai bunga majemuk. Selisih saldo akhir Beni dan Anto adalah ....

- A. Rp2.100.000,00  
  <sub>Salah: menjawab bunga majemuk, bukan selisih</sub>
- B. Rp12.100.000,00  
  <sub>Salah: menjawab saldo akhir Beni</sub>
- C. Rp1.000.000,00  
  <sub>Salah: menjawab bunga satu tahun</sub>
- **D. Rp100.000,00** ✅  
  <sub>Benar: tunggal 12.000.000; majemuk 12.100.000</sub>

**Pembahasan:** Anto: 10.000.000 + 2 x 1.000.000 = 12.000.000. Beni: $10.000.000(1,1)^2 = 12.100.000$. Selisih = 100.000.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b02-b-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: membaca tabel bunga majemuk*

| Tahun ke | Bunga (Rp) | Modal akhir (Rp) |
|---|---|---|
| 0 | 0 | 10.000.000,00 |
| 1 | 1.000.000,00 | 11.000.000,00 |
| 2 | 1.100.000,00 | 12.100.000,00 |
| 3 | 1.210.000,00 | 13.310.000,00 |

Sebuah tabungan berbunga majemuk 10% per tahun, dengan perhitungan tahun ke-0 sampai ke-3 seperti pada data stimulus. Besar bunga pada tahun ke-4 adalah ....

- A. Rp1.000.000,00  
  <sub>Salah: menghitung dari modal awal 10.000.000</sub>
- **B. Rp1.331.000,00** ✅  
  <sub>Benar: 10% x 13.310.000 = 1.331.000</sub>
- C. Rp1.464.100,00  
  <sub>Salah: bunga tahun ke-5, salah satu periode</sub>
- D. Rp1.210.000,00  
  <sub>Salah: memakai bunga tahun ke-3 dari tabel</sub>

**Pembahasan:** Bunga tahun ke-4 = 10% x modal akhir tahun ke-3 = 10% x 13.310.000 = 1.331.000.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b02-b-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: memilih rumus bunga majemuk*

Modal $M$ dibungakan dengan bunga majemuk $p$ per tahun ($p$ dalam bentuk desimal). Modal akhir setelah $n$ tahun dinyatakan oleh ....

- **A. $M(1+p)^n$** ✅  
  <sub>Benar: pola $M(1+p)$, $M(1+p)^2$, $M(1+p)^3$, dan seterusnya</sub>
- B. $M(1+p) \times n$  
  <sub>Salah: mengalikan faktor satu tahun dengan n</sub>
- C. $M(1+np)$  
  <sub>Salah: rumus bunga tunggal</sub>
- D. $M \times p^n$  
  <sub>Salah: lupa menambah 1 pada p</sub>

**Pembahasan:** Tiap tahun modal dikalikan $(1+p)$, sehingga setelah $n$ tahun menjadi $M(1+p)^n$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b02-b-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: bunga total dua periode semester*

Modal Rp5.000.000,00 dibungakan dengan bunga majemuk 4% per semester. Total bunga yang diperoleh setelah 1 tahun adalah ....

- **A. Rp408.000,00** ✅  
  <sub>Benar: 1 tahun = 2 semester; $5.000.000(1,04)^2 - 5.000.000 = 408.000$</sub>
- B. Rp5.408.000,00  
  <sub>Salah: menjawab modal akhir</sub>
- C. Rp400.000,00  
  <sub>Salah: bunga tunggal 4% x 2 semester</sub>
- D. Rp200.000,00  
  <sub>Salah: hanya bunga satu semester</sub>

**Pembahasan:** $M_2 = 5.000.000 \times 1,0816 = 5.408.000$. Bunga = 408.000.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b02-b-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: dasar perhitungan bunga tahun kedua*

Modal Rp40.000.000,00 dibungakan dengan bunga majemuk 2% per tahun. Bunga pada tahun kedua dihitung dari modal sebesar ....

- **A. Rp40.800.000,00** ✅  
  <sub>Benar: modal akhir tahun pertama = 40.000.000 + 800.000</sub>
- B. Rp41.616.000,00  
  <sub>Salah: memakai modal akhir tahun kedua</sub>
- C. Rp40.000.000,00  
  <sub>Salah: memakai modal awal (cara bunga tunggal)</sub>
- D. Rp800.000,00  
  <sub>Salah: memakai bunga tahun pertama</sub>

**Pembahasan:** Setelah tahun pertama modal menjadi 40.000.000 + 2% x 40.000.000 = 40.800.000; inilah dasar bunga tahun kedua.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b02-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: bunga tahunan dibayar bulanan (3 bulan)*

Citra menyimpan uang sejumlah Rp8.000.000,00 di bank yang menawarkan bunga majemuk sebesar 36% setiap tahun dengan pembayaran setiap bulan. Setelah 3 bulan, Citra mencairkan seluruh uangnya. Total nilai uang Citra sebesar ....

- A. Rp8.720.000,00  
  <sub>Salah: bunga 3% per bulan dihitung tunggal (3 x 3%)</sub>
- B. Rp8.487.200,00  
  <sub>Salah: memakai n = 2 padahal 3 bulan</sub>
- C. Rp10.360.232,00  
  <sub>Salah: membagi 36% dengan 4 (bukan 12) lalu dipangkatkan 3</sub>
- **D. Rp8.741.816,00** ✅  
  <sub>Benar: bunga 3% per bulan, $8.000.000(1,03)^3 = 8.741.816$</sub>

**Pembahasan:** 36% per tahun dengan pembayaran bulanan = 3% per bulan. $M_3 = 8.000.000 \times 1,092727 = 8.741.816$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b02-b-medium-bt01-002
*variasi (konteks) | C3 | 4 langkah | jenis: bunga yang diperoleh dari saldo akhir*

Koperasi Mekar memberi bunga majemuk 5% per 3 bulan. Setelah menyimpan uang selama 1 tahun, saldo simpanan Bu Sinta menjadi Rp24.310.125,00. Besar bunga yang diperoleh Bu Sinta selama 1 tahun adalah ....

- A. Rp24.310.125,00  
  <sub>Salah: menjawab saldo akhir, bukan bunga</sub>
- B. Rp2.260.125,00  
  <sub>Salah: memakai n = 2 periode padahal 4 periode</sub>
- **C. Rp4.310.125,00** ✅  
  <sub>Benar: n = 4; simpanan awal $24.310.125 : 1,21550625 = 20.000.000$; bunga = 24.310.125 - 20.000.000</sub>
- D. Rp3.310.125,00  
  <sub>Salah: memakai n = 3 periode padahal 4 periode</sub>

**Pembahasan:** 1 tahun = 4 periode 3 bulan. $M = 24.310.125 : (1,05)^4 = 20.000.000$. Bunga = 24.310.125 - 20.000.000 = 4.310.125.
**Acuan:** siswa — siswa hal.63 Contoh 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b02-b-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: mencari lama waktu dari tabel pangkat*

| n | $(1,1)^n$ |
|---|---|
| 2 | 1,21 |
| 3 | 1,331 |
| 4 | 1,4641 |
| 5 | 1,61051 |
| 6 | 1,771561 |

Modal Rp3.000.000,00 dibungakan dengan bunga majemuk 10% per tahun hingga menjadi Rp4.831.530,00. Dengan memakai tabel, lama modal tersebut dibungakan adalah ... tahun.

- A. 6  
  <sub>Salah: memakai bunga tunggal: bunga 61,051% dibagi 10% sekitar 6</sub>
- **B. 5** ✅  
  <sub>Benar: $4.831.530 : 3.000.000 = 1,61051 = (1,1)^5$</sub>
- C. 3  
  <sub>Salah: salah memilih baris tabel (1,331)</sub>
- D. 4  
  <sub>Salah: salah memilih baris tabel (1,4641)</sub>

**Pembahasan:** Faktor pertumbuhan = 4.831.530 : 3.000.000 = 1,61051. Pada tabel $(1,1)^5 = 1,61051$, sehingga n = 5 tahun.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b02-b-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: bunga tahunan dibayar triwulan*

Bu Ratna menabung Rp15.000.000,00 pada sebuah koperasi yang memberi bunga majemuk 8% per tahun dengan perhitungan setiap triwulan. Setelah 9 bulan, saldo tabungan Bu Ratna sebesar ....

- A. Rp18.895.680,00  
  <sub>Salah: memakai 8% sebagai bunga tiap triwulan</sub>
- **B. Rp15.918.120,00** ✅  
  <sub>Benar: 2% per triwulan, 9 bulan = 3 triwulan, $15.000.000(1,02)^3 = 15.918.120$</sub>
- C. Rp15.606.000,00  
  <sub>Salah: memakai n = 2 periode padahal 3 triwulan</sub>
- D. Rp15.900.000,00  
  <sub>Salah: bunga 2% per triwulan dihitung tunggal (3 x 2%)</sub>

**Pembahasan:** Triwulan = 3 bulan, sehingga 9 bulan = 3 periode dengan $p = 8\% : 4 = 2\%$. $M_3 = 15.000.000 \times 1,061208 = 15.918.120$.
**Acuan:** pretest — kelas12-b02-p0072-latihan-2-1-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b02-b-medium-bt01-005
*orisinal | C4 | 4 langkah | jenis: membandingkan dua skema periode bunga*

Pak Hadi memiliki uang Rp20.000.000,00. Bank A memberi bunga majemuk 10% per tahun, sedangkan Bank B memberi bunga majemuk 5% per semester. Jika uang itu disimpan selama 2 tahun, selisih saldo akhir di Bank B dan Bank A adalah ....

- A. Rp24.310.125,00  
  <sub>Salah: menjawab saldo akhir Bank B saja</sub>
- B. Rp2.150.000,00  
  <sub>Salah: memakai n = 2 semester untuk Bank B (hanya 1 tahun)</sub>
- C. Rp200.000,00  
  <sub>Salah: Bank B dihitung bunga tunggal $5\% \times 4$, lalu selisih dengan saldo Bank A</sub>
- **D. Rp110.125,00** ✅  
  <sub>Benar: Bank A: $20.000.000(1,1)^2 = 24.200.000$; Bank B: $20.000.000(1,05)^4 = 24.310.125$</sub>

**Pembahasan:** Bank A: $n = 2$, saldo 24.200.000. Bank B: 2 tahun = 4 semester, saldo 24.310.125. Selisih = 110.125.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b02-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: persentase bunga total terhadap modal awal*

Suatu tabungan berbunga majemuk 20% per semester selama 2 tahun. Diketahui $(1,2)^4 = 2,0736$. Total bunga yang diterima adalah ... dari tabungan awal.

- A. 207,36%  
  <sub>Salah: menyebut persentase modal akhir, bukan bunga</sub>
- B. 72,8%  
  <sub>Salah: memakai n = 3 semester ($1,2^3 = 1,728$)</sub>
- **C. 107,36%** ✅  
  <sub>Benar: 2 tahun = 4 semester; faktor 2,0736 berarti bertambah 1,0736 atau 107,36%</sub>
- D. 80%  
  <sub>Salah: memakai bunga tunggal 20% x 4 semester</sub>

**Pembahasan:** 2 tahun = 4 semester. Modal akhir = 2,0736 M sehingga bunga = 1,0736 M = 107,36% dari tabungan awal.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b02-b-medium-bt01-007
*orisinal | C3 | 4 langkah | jenis: total dua simpanan dengan periode bunga berbeda*

Bu Dewi menyimpan Rp10.000.000,00 di Bank X dengan bunga majemuk 8% per tahun dan Rp15.000.000,00 di Bank Y dengan bunga majemuk 4% per semester. Setelah 1 tahun, total saldo kedua simpanan adalah ....

- **A. Rp27.024.000,00** ✅  
  <sub>Benar: Bank X: 10.800.000; Bank Y: $15.000.000(1,04)^2 = 16.224.000$</sub>
- B. Rp27.000.000,00  
  <sub>Salah: Bank Y dihitung 8% per tahun (tunggal 4% x 2)</sub>
- C. Rp26.400.000,00  
  <sub>Salah: Bank Y dihitung hanya satu semester</sub>
- D. Rp16.224.000,00  
  <sub>Salah: menjawab saldo Bank Y saja</sub>

**Pembahasan:** Bank X: $10.000.000 \times 1,08 = 10.800.000$. Bank Y: 1 tahun = 2 semester, $15.000.000 \times 1,0816 = 16.224.000$. Total = 27.024.000.
**Acuan:** siswa — siswa hal.59

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b02-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: simpanan awal dari tabel faktor*

Koperasi Tani Makmur memiliki program simpanan berjangka dengan suku bunga majemuk 5% per 4 bulan. Bu Wulan menyimpan uang selama 20 bulan dan saldonya sekarang Rp102.102.525,00.

| N | $(1+i)^N$ dengan $i = 5\%$ |
|---|---|
| 3 | 1,157625 |
| 4 | 1,21550625 |
| 5 | 1,2762815625 |
| 6 | 1,340095640625 |

Berdasarkan tabel tersebut, simpanan awal Bu Wulan sebesar ....

- A. Rp22.102.525,00  
  <sub>Salah: menjawab bunga yang diterima, bukan simpanan awal</sub>
- **B. Rp80.000.000,00** ✅  
  <sub>Benar: 20 bulan = 5 periode; $102.102.525 : 1,2762815625 = 80.000.000$</sub>
- C. Rp84.000.000,00  
  <sub>Salah: memakai faktor N = 4 (1,21550625)</sub>
- D. Rp88.200.000,00  
  <sub>Salah: memakai faktor N = 3 (1,157625)</sub>

**Pembahasan:** 20 bulan : 4 bulan = 5 periode. $M = 102.102.525 : 1,2762815625 = 80.000.000$.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b02-b-medium-bt01-009
*orisinal | C3 | 4 langkah | jenis: penambahan setoran di tengah masa bunga*

Pak Dedi menabung Rp10.000.000,00 dengan bunga majemuk 10% per tahun. Setelah 2 tahun, ia menambah tabungannya Rp5.000.000,00. Saldo tabungan Pak Dedi 2 tahun setelah penambahan adalah ....

- A. Rp20.520.000,00  
  <sub>Salah: tahun berikutnya dihitung bunga tunggal 10% x 2</sub>
- B. Rp19.641.000,00  
  <sub>Salah: setoran 5.000.000 tidak ikut berbunga</sub>
- **C. Rp20.691.000,00** ✅  
  <sub>Benar: saldo setelah 2 tahun 12.100.000 ditambah 5.000.000 = 17.100.000; lalu $17.100.000(1,1)^2 = 20.691.000$</sub>
- D. Rp14.641.000,00  
  <sub>Salah: lupa memasukkan tambahan Rp5.000.000,00</sub>

**Pembahasan:** $M_2 = 10.000.000(1,1)^2 = 12.100.000$. Setelah ditambah menjadi 17.100.000. Dua tahun lagi: $17.100.000 \times 1,21 = 20.691.000$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b02-b-medium-bt01-010
*variasi (konteks) | C4 | 3 langkah | jenis: cara tidak tepat memakai tabel (faktor dijumlahkan)*

Koperasi Rukun Sentosa memberi bunga majemuk 4% per semester. Bu Ani menyimpan uang selama 30 bulan.

| N | $(1+i)^N$ dengan $i = 4\%$ |
|---|---|
| 2 | 1,0816 |
| 3 | 1,124864 |

Misalkan simpanan awal Bu Ani adalah $M$. Dengan menggunakan tabel tersebut, cara yang tidak tepat untuk menghitung simpanan Bu Ani setelah 30 bulan adalah ....

- **A. $(1,124864 + 1,0816) \times M$** ✅  
  <sub>Benar: 30 bulan = 5 semester sehingga seharusnya $(1,04)^5 M$; faktor harus dikalikan (N = 3 dan N = 2), bukan dijumlahkan</sub>
- B. $(1,04)^5 \times M$  
  <sub>Salah: cara ini benar: rumus langsung dengan n = 5</sub>
- C. $(1,124864) \times (1,0816) \times M$  
  <sub>Salah: cara ini benar: $(1,04)^3 (1,04)^2 = (1,04)^5$</sub>
- D. $(1,0816)^2 \times (1,04) \times M$  
  <sub>Salah: cara ini benar: $(1,04)^4 (1,04) = (1,04)^5$</sub>

**Pembahasan:** 30 bulan : 6 bulan = 5 periode, nilai simpanan $M(1,04)^5$. Menjumlahkan faktor (1,124864 + 1,0816 = 2,206464) tidak sama dengan $(1,04)^5 = 1,2166529024$.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b02-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: waktu minimal modal melebihi dua kali lipat*

Modal dibungakan dengan bunga majemuk 30% per tahun. Paling sedikit berapa tahun agar modal akhir lebih dari dua kali modal awal?

- **A. 3 tahun** ✅  
  <sub>Benar: $(1,3)^2 = 1,69 < 2$ dan $(1,3)^3 = 2,197 > 2$</sub>
- B. 7 tahun  
  <sub>Salah: membagi 200% dengan 30% lalu membulatkan ke atas</sub>
- C. 4 tahun  
  <sub>Salah: memakai bunga tunggal: 30% x 4 tahun melebihi 100%</sub>
- D. 2 tahun  
  <sub>Salah: membulatkan faktor 1,69 menjadi 2</sub>

**Pembahasan:** Faktor akhir tahun ke-2 adalah 1,69 (belum lebih dari 2), tahun ke-3 adalah 2,197 (lebih dari 2). Jadi 3 tahun.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b02-b-medium-bt01-012
*variasi (konteks) | C3 | 3 langkah | jenis: simpanan akhir dari tabel faktor*

Pak Hendra menyimpan Rp60.000.000,00 pada program simpanan berjangka sebuah bank dengan bunga majemuk 5% per 4 bulan. Uang itu disimpan selama 12 bulan.

| N | $(1+i)^N$ dengan $i = 5\%$ |
|---|---|
| 3 | 1,157625 |
| 4 | 1,21550625 |
| 5 | 1,2762815625 |
| 6 | 1,340095640625 |

Berdasarkan tabel tersebut, simpanan Pak Hendra setelah 12 bulan sebesar ....

- A. Rp69.000.000,00  
  <sub>Salah: memakai bunga tunggal (3 x 5%)</sub>
- **B. Rp69.457.500,00** ✅  
  <sub>Benar: 12 bulan = 3 periode; $60.000.000 \times 1,157625 = 69.457.500$</sub>
- C. Rp72.930.375,00  
  <sub>Salah: memakai faktor N = 4 (1,21550625)</sub>
- D. Rp66.150.000,00  
  <sub>Salah: memakai n = 2 periode</sub>

**Pembahasan:** 12 bulan : 4 bulan = 3 periode. $M_3 = 60.000.000 \times 1,157625 = 69.457.500$.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b02-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: bunga untuk lama menabung 1,5 tahun*

Rina menabung Rp7.000.000,00 dengan bunga majemuk 10% per semester. Besar bunga yang diperoleh setelah 1,5 tahun adalah ....

- **A. Rp2.317.000,00** ✅  
  <sub>Benar: 1,5 tahun = 3 semester; $7.000.000(1,1)^3 = 9.317.000$; bunga = 2.317.000</sub>
- B. Rp2.100.000,00  
  <sub>Salah: bunga tunggal 10% x 3 semester</sub>
- C. Rp1.470.000,00  
  <sub>Salah: memakai n = 2 semester</sub>
- D. Rp9.317.000,00  
  <sub>Salah: menjawab modal akhir, bukan bunga</sub>

**Pembahasan:** 1,5 tahun = 3 semester. $M_3 = 7.000.000 \times 1,331 = 9.317.000$. Bunga = 9.317.000 - 7.000.000 = 2.317.000.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b02-b-medium-bt01-014
*variasi (konteks) | C4 | 3 langkah | jenis: cara tidak tepat memakai tabel (bunga tunggal)*

Sebuah bank memberi bunga majemuk 3% per semester. Pak Joko menabung selama 3 tahun.

| N | $(1+i)^N$ dengan $i = 3\%$ |
|---|---|
| 2 | 1,0609 |
| 3 | 1,092727 |

Misalkan tabungan awal Pak Joko adalah $M$. Dengan menggunakan tabel tersebut, cara yang tidak tepat untuk menghitung tabungan Pak Joko setelah 3 tahun adalah ....

- A. $(1,092727)^2 \times M$  
  <sub>Salah: cara ini benar: $((1,03)^3)^2 = (1,03)^6$</sub>
- B. $(1,03)^6 \times M$  
  <sub>Salah: cara ini benar: rumus langsung dengan n = 6</sub>
- **C. $(1 + 6 \times 0,03) \times M$** ✅  
  <sub>Benar: 3 tahun = 6 semester; rumus ini bunga tunggal, bukan pemangkatan $(1,03)^6$</sub>
- D. $(1,0609)^3 \times M$  
  <sub>Salah: cara ini benar: $((1,03)^2)^3 = (1,03)^6$</sub>

**Pembahasan:** 3 tahun = 6 semester. Bunga majemuk memberi $M(1,03)^6 = M(1,0609)^3 = M(1,092727)^2$. Bentuk $(1 + 6 \times 0,03)M$ adalah bunga tunggal.
**Acuan:** pretest — kelas12-b02-p0095-uji-kompetensi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b02-b-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: modal awal dari total bunga*

Modal $M$ dibungakan dengan bunga majemuk 10% per tahun. Setelah 3 tahun, bunga yang diperoleh sebesar Rp1.986.000,00. Besar modal $M$ adalah ....

- A. Rp19.860.000,00  
  <sub>Salah: menganggap 1.986.000 adalah bunga satu tahun (10% dari M)</sub>
- B. Rp7.986.000,00  
  <sub>Salah: menjawab modal akhir, bukan modal awal</sub>
- C. Rp6.620.000,00  
  <sub>Salah: memakai bunga tunggal: bunga = 30% dari M</sub>
- **D. Rp6.000.000,00** ✅  
  <sub>Benar: bunga $= M[(1,1)^3 - 1] = 0,331M = 1.986.000$ sehingga $M = 6.000.000$</sub>

**Pembahasan:** Bunga = modal akhir - modal awal = $M(1,331) - M = 0,331M$. Jadi $M = 1.986.000 : 0,331 = 6.000.000$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b02-b-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: modal awal dari saldo akhir (3 periode)*

Lia menabung uang di bank dengan bunga majemuk sebesar 2,5% per 3 bulan. Setelah 9 bulan menabung, saldo tabungan menjadi sebesar Rp8.615.125,00. Berapakah jumlah uang yang ditabung Lia semula?

- A. Rp615.125,00  
  <sub>Salah: menjawab bunga, bukan tabungan semula</sub>
- **B. Rp8.000.000,00** ✅  
  <sub>Benar: n = 3 periode, $8.615.125 : (1,025)^3 = 8.615.125 : 1,076890625 = 8.000.000$</sub>
- C. Rp8.014.070,00  
  <sub>Salah: menganggap bunga tunggal 3 x 2,5% = 7,5% lalu membagi 1,075</sub>
- D. Rp8.200.000,00  
  <sub>Salah: memakai n = 2 periode padahal 3 periode</sub>

**Pembahasan:** 9 bulan : 3 bulan = 3 periode. $M \times (1,025)^3 = 8.615.125$ sehingga $M = 8.615.125 : 1,076890625 = 8.000.000$.
**Acuan:** siswa — siswa hal.63 Contoh 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b02-b-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: melanjutkan pola tabel bunga majemuk*

| Tahun ke | Bunga (Rp) | Modal akhir (Rp) |
|---|---|---|
| 0 | 0 | 5.000.000,00 |
| 1 | 1.000.000,00 | 6.000.000,00 |
| 2 | 1.200.000,00 | 7.200.000,00 |
| 3 | 1.440.000,00 | 8.640.000,00 |

Tabel di atas menunjukkan perhitungan bunga majemuk suatu tabungan dengan bunga $p$ per tahun tetap. Modal akhir pada tahun ke-5 adalah ....

- A. Rp10.368.000,00  
  <sub>Salah: berhenti di tahun ke-4</sub>
- B. Rp14.929.920,00  
  <sub>Salah: salah menghitung hingga tahun ke-6</sub>
- C. Rp11.520.000,00  
  <sub>Salah: bunga tahun ke-3 dianggap tetap (bunga tunggal) untuk 2 tahun berikutnya</sub>
- **D. Rp12.441.600,00** ✅  
  <sub>Benar: $p = 1.000.000 : 5.000.000 = 20\%$; $M_5 = 8.640.000 \times (1,2)^2 = 12.441.600$</sub>

**Pembahasan:** Bunga tahun pertama 1.000.000 dari modal 5.000.000 sehingga $p = 20\%$. $M_4 = 10.368.000$, $M_5 = 12.441.600$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b02-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: selisih bunga dua tahun berurutan*

Modal Rp20.000.000,00 dibungakan dengan bunga majemuk 10% per tahun. Selisih bunga yang diterima pada tahun kelima dan tahun keempat adalah ....

- A. Rp2.662.000,00  
  <sub>Salah: menjawab bunga tahun keempat saja</sub>
- B. Rp242.000,00  
  <sub>Salah: selisih bunga tahun keempat dan ketiga (salah tahun)</sub>
- **C. Rp266.200,00** ✅  
  <sub>Benar: bunga tahun ke-4 = 2.662.000 (10% x 26.620.000), tahun ke-5 = 2.928.200; selisih 266.200</sub>
- D. Rp2.928.200,00  
  <sub>Salah: menjawab bunga tahun kelima saja</sub>

**Pembahasan:** $M_3 = 26.620.000$, bunga tahun ke-4 = 2.662.000, $M_4 = 29.282.000$, bunga tahun ke-5 = 2.928.200. Selisih = 266.200.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b02-b-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: membandingkan bunga tunggal dan majemuk berbeda p*

Dua tabungan masing-masing Rp10.000.000,00 disimpan selama 5 tahun. Tabungan pertama berbunga tunggal 12% per tahun, tabungan kedua berbunga majemuk 10% per tahun. Selisih saldo akhir tabungan kedua dikurangi tabungan pertama adalah ....

- A. Rp1.359.000,00  
  <sub>Salah: tabungan majemuk dihitung hanya 4 tahun</sub>
- B. Rp6.000.000,00  
  <sub>Salah: menjawab bunga tunggal, bukan selisih saldo</sub>
- C. Rp6.105.100,00  
  <sub>Salah: menjawab bunga majemuk, bukan selisih saldo</sub>
- **D. Rp105.100,00** ✅  
  <sub>Benar: tunggal: $10.000.000(1 + 5 \times 0,12) = 16.000.000$; majemuk: $10.000.000(1,1)^5 = 16.105.100$</sub>

**Pembahasan:** Saldo tunggal = 16.000.000. Saldo majemuk = $10.000.000 \times 1,61051 = 16.105.100$. Selisih = 105.100.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b02-b-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: mencari suku bunga dari modal awal dan akhir*

Tabungan Rp10.000.000,00 menjadi Rp12.544.000,00 setelah 2 tahun dengan bunga majemuk $p$ per tahun. Nilai $p$ adalah ....

- **A. 12%** ✅  
  <sub>Benar: $(1+p)^2 = 1,2544$ sehingga $1+p = 1,12$ dan $p = 12\%$</sub>
- B. 12,72%  
  <sub>Salah: memakai bunga tunggal: 25,44% dibagi 2 tahun</sub>
- C. 25,44%  
  <sub>Salah: menjawab bunga total dua tahun, bukan per tahun</sub>
- D. 6,36%  
  <sub>Salah: membagi 12,72% sekali lagi dengan 2</sub>

**Pembahasan:** $12.544.000 : 10.000.000 = 1,2544 = (1,12)^2$, sehingga $p = 0,12 = 12\%$ per tahun.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b02-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan p per periode*

Rudi menabung Rp5.000.000,00 dengan bunga majemuk 24% per tahun yang dibayarkan setiap bulan. Untuk saldo setelah 6 bulan, Rudi menulis $5.000.000 \times (1,24)^6$. Pernyataan yang benar tentang pekerjaan Rudi adalah ....

- **A. Salah, bunga per bulan seharusnya 2% sehingga yang benar $5.000.000 \times (1,02)^6$** ✅  
  <sub>Benar: 24% per tahun dibayar bulanan berarti 2% per bulan, dan 6 bulan = 6 periode</sub>
- B. Benar, karena 24% adalah bunga untuk setiap periode perhitungan sehingga $(1,24)^6$ tepat  
  <sub>Salah: tidak mengubah 24% per tahun menjadi per bulan</sub>
- C. Salah, bunga per bulan seharusnya 4% sehingga yang benar $5.000.000 \times (1,04)^6$  
  <sub>Salah: 24% dibagi 6 (banyak bulan), bukan dibagi 12</sub>
- D. Salah, bunga per bulan seharusnya 2% sehingga yang benar $5.000.000 \times (1,02)^{12}$  
  <sub>Salah: n dianggap 12 padahal hanya 6 bulan</sub>

**Pembahasan:** 24% per tahun dengan pembayaran bulanan = 24% : 12 = 2% per bulan. 6 bulan = 6 periode, jadi $M_6 = 5.000.000 (1,02)^6$.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b02-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim total bunga*

Bu Mira menabung dengan bunga majemuk 10% per tahun selama 3 tahun. Pernyataan yang benar tentang total bunga yang diterimanya adalah ....

- **A. Total bunga 33,1% dari modal awal, lebih besar daripada bunga tunggal 30%** ✅  
  <sub>Benar: $(1,1)^3 = 1,331$ sehingga bunga total 33,1% dari modal, lebih dari 3 x 10% = 30%</sub>
- B. Total bunga 33,1% dari modal awal, lebih kecil daripada bunga tunggal 30%  
  <sub>Salah: angka benar tetapi perbandingan dengan 30% terbalik</sub>
- C. Total bunga 30% dari modal awal, sama dengan bunga tunggal  
  <sub>Salah: mengira majemuk sama dengan tunggal (3 x 10%)</sub>
- D. Total bunga 21% dari modal awal karena hanya dua tahun pertama yang berbunga majemuk  
  <sub>Salah: hanya memangkatkan 2, tahun ketiga terlewat</sub>

**Pembahasan:** $M_3 = M(1,1)^3 = 1,331M$, bunga 0,331M = 33,1% dari M. Bunga tunggal 3 tahun hanya 30%.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b02-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim majemuk lebih besar*

Klaim: "Dengan suku bunga p per tahun yang sama, saldo akhir bunga majemuk selalu lebih besar daripada saldo akhir bunga tunggal untuk setiap lama menabung bilangan asli n tahun." Lama menabung yang menjadi contoh penyangkal klaim tersebut adalah ....

- A. 10 tahun  
  <sub>Salah: pada n = 10, majemuk jauh lebih besar, klaim berlaku</sub>
- B. 2 tahun  
  <sub>Salah: pada n = 2, majemuk lebih besar (selisih $p^2$ per modal), klaim berlaku</sub>
- **C. 1 tahun** ✅  
  <sub>Benar: untuk n = 1, $(1+p)^1 = 1 + p$ sehingga kedua saldo sama dan tidak ada yang lebih besar</sub>
- D. 3 tahun  
  <sub>Salah: pada n = 3, majemuk lebih besar, klaim berlaku</sub>

**Pembahasan:** Saldo tunggal $M(1+np)$, majemuk $M(1+p)^n$. Untuk n = 1 keduanya $M(1+p)$ (sama), sedangkan untuk n >= 2 majemuk lebih besar. Jadi n = 1 menyangkal klaim.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b02-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: membandingkan empat periode bunga setara 12% per tahun*

| Bank | Bunga majemuk |
|---|---|
| P | 12% per tahun |
| Q | 6% per semester |
| R | 3% per triwulan |
| S | 1% per bulan |

Empat bank menawarkan bunga majemuk dengan periode berbeda. Dengan uang awal yang sama dan disimpan tepat 1 tahun, bank yang memberi saldo akhir paling besar adalah ....

- A. Bank R: 3% per triwulan  
  <sub>Salah: faktor sekitar 1,1255 masih lebih kecil dari S</sub>
- **B. Bank S: 1% per bulan** ✅  
  <sub>Benar: faktor 1 tahun: P 1,12; Q $(1,06)^2 = 1,1236$; R $(1,03)^4 \approx 1,1255$; S $(1,01)^{12} \approx 1,1268$ sehingga S terbesar</sub>
- C. Bank Q: 6% per semester  
  <sub>Salah: faktor 1,1236 masih lebih kecil dari S</sub>
- D. Bank P: 12% per tahun  
  <sub>Salah: faktor 1,12 adalah yang terkecil, hanya satu kali berbunga</sub>

**Pembahasan:** Makin sering bunga ditambahkan ke modal, makin besar saldo 1 tahun: 1,12 < 1,1236 < 1,1255 < 1,1268. Bank S terbesar.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b02-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: parameter p dari selisih bunga dua tahun*

Modal Rp3.000.000,00 dibungakan dengan bunga majemuk $p$ per tahun ($p$ positif). Bunga yang diterima pada tahun kedua Rp120.000,00 lebih besar daripada bunga tahun pertama. Nilai $p$ adalah ....

- A. 2%  
  <sub>Salah: membagi 4% sekali lagi dengan 2</sub>
- B. 40%  
  <sub>Salah: mengalikan p dengan 2 setelah akar (salah mengurai selisih menjadi $2Mp^2$)</sub>
- C. 4%  
  <sub>Salah: menganggap $p^2 = 0,04$ sebagai p (lupa akar)</sub>
- **D. 20%** ✅  
  <sub>Benar: bunga tahun 1 = $Mp$, tahun 2 = $M(1+p)p$, selisih = $Mp^2 = 120.000$ sehingga $p^2 = 0,04$ dan $p = 0,2$</sub>

**Pembahasan:** Bunga tahun ke-1 = $3.000.000p$; bunga tahun ke-2 = $3.000.000(1+p)p$. Selisih = $3.000.000p^2 = 120.000$, jadi $p^2 = 0,04$ dan $p = 20\%$. Cek: 600.000 dan 720.000.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b02-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: bunga ditarik vs dibiarkan berbunga*

Pak Anto menyimpan Rp10.000.000,00 selama 3 tahun dengan suku bunga 12% per tahun. Pada Rencana I bunga diambil setiap akhir tahun (modal tetap Rp10.000.000,00). Pada Rencana II bunga dibiarkan dan ikut berbunga (bunga majemuk). Selisih total kekayaan Pak Anto pada akhir tahun ketiga (modal ditambah bunga) antara Rencana II dan Rencana I adalah ....

- A. Rp14.049.280,00  
  <sub>Salah: menjawab total kekayaan Rencana II, bukan selisih</sub>
- B. Rp1.200.000,00  
  <sub>Salah: menjawab bunga satu tahun</sub>
- C. Rp4.049.280,00  
  <sub>Salah: menjawab bunga Rencana II, bukan selisih</sub>
- **D. Rp449.280,00** ✅  
  <sub>Benar: I: 10.000.000 + 3 x 1.200.000 = 13.600.000; II: $10.000.000(1,12)^3 = 14.049.280$</sub>

**Pembahasan:** Rencana I: modal 10.000.000 + bunga 3 x 1.200.000 = 13.600.000. Rencana II: $10.000.000 \times 1,404928 = 14.049.280$. Selisih = 449.280.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b02-b-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: memperluas pola majemuk (2 kali dalam 5 tahun)*

Suatu modal menjadi tepat 2 kali lipat setelah 5 tahun dengan bunga majemuk p per tahun yang tetap. Setelah 15 tahun, modal tersebut menjadi ... kali modal awal.

- **A. 8** ✅  
  <sub>Benar: $(1+p)^5 = 2$ sehingga $(1+p)^{15} = ((1+p)^5)^3 = 2^3 = 8$</sub>
- B. 4  
  <sub>Salah: memakai pola bunga tunggal: bunga 100% tiap 5 tahun sehingga 1 + 3 = 4</sub>
- C. 6  
  <sub>Salah: mengalikan 2 dengan 3 (pola linear)</sub>
- D. 16  
  <sub>Salah: memangkatkan 2 dengan 4 (mengira 15 tahun = 4 kelompok 5 tahun)</sub>

**Pembahasan:** Faktor 5 tahun = 2. Lima belas tahun = 3 kelompok 5 tahun, faktor $2 \times 2 \times 2 = 8$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b02-b-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan dasar bunga tahun ketiga*

Rani menabung Rp5.000.000,00 dengan bunga majemuk 10% per tahun. Ia menghitung bunga tahun ketiga sebesar $10\% \times 5.000.000 = 500.000$. Bunga yang benar pada tahun ketiga adalah ....

- A. Rp665.500,00  
  <sub>Salah: bunga tahun keempat (dasar saldo tahun ketiga)</sub>
- B. Rp550.000,00  
  <sub>Salah: bunga tahun kedua (dasar saldo tahun pertama)</sub>
- **C. Rp605.000,00** ✅  
  <sub>Benar: bunga tahun ke-3 dihitung dari saldo akhir tahun ke-2: $5.000.000 \times 1,21 = 6.050.000$, lalu x 10% = 605.000</sub>
- D. Rp500.000,00  
  <sub>Salah: kesalahan Rani sendiri: memakai modal awal sebagai dasar</sub>

**Pembahasan:** Saldo akhir tahun ke-2 = 6.050.000. Bunga tahun ke-3 = 10% x 6.050.000 = 605.000.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b02-b-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: suku bunga tunggal ekuivalen dengan majemuk*

Tabungan A berbunga majemuk 10% per tahun. Tabungan B berbunga tunggal q% per tahun. Dengan modal awal sama, agar saldo keduanya sama setelah tepat 2 tahun, nilai q adalah ....

- A. 5,25%  
  <sub>Salah: membagi 10,5% sekali lagi dengan 2</sub>
- **B. 10,5%** ✅  
  <sub>Benar: $1 + 2q = (1,1)^2 = 1,21$ sehingga $q = 0,105$</sub>
- C. 10%  
  <sub>Salah: mengira p yang sama membuat saldo sama</sub>
- D. 21%  
  <sub>Salah: menganggap total bunga 2 tahun sebagai bunga per tahun</sub>

**Pembahasan:** Majemuk: $M(1,1)^2 = 1,21M$. Tunggal: $M(1 + 2q)$. Samakan: $2q = 0,21$, jadi $q = 10,5\%$.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b02-b-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: membandingkan rencana pindah bank*

Bu Sari mempunyai Rp10.000.000,00 untuk 2 tahun. Rencana I: tahun pertama di Bank A (bunga majemuk 10% per tahun), lalu seluruh saldo dipindah ke Bank B untuk tahun kedua. Rencana II: seluruh uang disimpan 2 tahun di Bank B. Bank B memberi bunga majemuk 5% per semester. Selisih saldo akhir Rencana II dikurangi Rencana I adalah ....

- A. Rp2.155.062,50  
  <sub>Salah: menjawab bunga Rencana II, bukan selisih</sub>
- **B. Rp27.562,50** ✅  
  <sub>Benar: I: $10.000.000 \times 1,1 \times (1,05)^2 = 12.127.500$; II: $10.000.000(1,05)^4 = 12.155.062,50$</sub>
- C. Rp12.127.500,00  
  <sub>Salah: menjawab saldo akhir Rencana I</sub>
- D. Rp12.155.062,50  
  <sub>Salah: menjawab saldo akhir Rencana II</sub>

**Pembahasan:** Rencana I: 10.000.000 x 1,1 = 11.000.000, lalu x 1,1025 = 12.127.500. Rencana II: 10.000.000 x 1,21550625 = 12.155.062,50. Selisih = 27.562,50.
**Acuan:** siswa — siswa hal.59

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b02-b-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: tahun pertama bunga tahunan melampaui batas*

| n | $(1,1)^n$ |
|---|---|
| 6 | 1,771561 |
| 7 | 1,9487171 |
| 8 | 2,14358881 |
| 9 | 2,357947691 |

Modal Rp5.000.000,00 dibungakan dengan bunga majemuk 10% per tahun. Bunga yang diterima pada tahun ke-$k$ dihitung dari saldo akhir tahun ke-$(k-1)$. Bunga yang diterima dalam satu tahun pertama kali lebih dari Rp1.000.000,00 pada tahun ke-....

- **A. 9** ✅  
  <sub>Benar: bunga tahun ke-$k$ = $500.000 \times (1,1)^{k-1} > 1.000.000$ berarti $(1,1)^{k-1} > 2$; menurut tabel $(1,1)^8 = 2,14358881 > 2$ sehingga $k - 1 = 8$ dan $k = 9$</sub>
- B. 10  
  <sub>Salah: bunga tahun ke-10 memang lebih dari 1.000.000, tetapi bukan yang pertama kali</sub>
- C. 8  
  <sub>Salah: memakai pangkat k = 8 (bukan k - 1), padahal bunga tahun ke-8 hanya 974.358</sub>
- D. 7  
  <sub>Salah: membulatkan $(1,1)^7 = 1,9487$ menjadi 2</sub>

**Pembahasan:** Bunga tahun ke-k = 10% x $5.000.000(1,1)^{k-1}$ = $500.000(1,1)^{k-1}$. Syarat > 1.000.000 berarti $(1,1)^{k-1} > 2$. Dari tabel, pangkat 7 = 1,9487 (belum) dan pangkat 8 = 2,1436 (sudah), sehingga k - 1 = 8, k = 9.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b02-b-hard-bt01-012
*orisinal | C5 | 3 langkah | jenis: mengenali pola saldo bunga majemuk*

Saldo akhir tahun ke-0 sampai tahun ke-3 (dalam rupiah) dari empat tabungan dengan modal awal Rp5.000.000,00 dicatat sebagai berikut. Catatan yang menunjukkan bunga majemuk dengan $p$ tetap per tahun adalah ....

- A. 5.000.000; 5.500.000; 6.050.000; 6.600.000  
  <sub>Salah: bunga tahun ketiga hanya 550.000, tidak berbunga atas bunga sebelumnya</sub>
- B. 5.000.000; 5.500.000; 6.000.000; 6.500.000  
  <sub>Salah: selisih tetap 500.000 (bunga tunggal 10%), bukan majemuk</sub>
- C. 5.000.000; 5.500.000; 6.100.000; 6.700.000  
  <sub>Salah: rasio tidak tetap (1,1; 1,109; 1,098), sehingga p berubah-ubah</sub>
- **D. 5.000.000; 5.500.000; 6.050.000; 6.655.000** ✅  
  <sub>Benar: rasio saldo berurutan sama: 5.500.000 : 5.000.000 = 6.050.000 : 5.500.000 = 6.655.000 : 6.050.000 = 1,1</sub>

**Pembahasan:** Pada bunga majemuk, saldo tiap tahun = saldo sebelumnya x $(1+p)$, jadi rasio berurutan tetap. Hanya 5.000.000; 5.500.000; 6.050.000; 6.655.000 yang rasionya selalu 1,1.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b02-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: modal awal dari dua saldo pada waktu berbeda*

Tabungan berbunga majemuk $p$ per tahun ($p$ positif) bernilai Rp14.520.000,00 setelah 2 tahun dan Rp17.569.200,00 setelah 4 tahun. Modal awal tabungan tersebut adalah ....

- A. Rp13.200.000,00  
  <sub>Salah: membagi 14.520.000 dengan 1,1 (hanya 1 tahun)</sub>
- B. Rp3.049.200,00  
  <sub>Salah: menjawab selisih kedua saldo, bukan modal awal</sub>
- **C. Rp12.000.000,00** ✅  
  <sub>Benar: $(1+p)^2 = 17.569.200 : 14.520.000 = 1,21$ sehingga $p = 10\%$; $M = 14.520.000 : 1,21 = 12.000.000$</sub>
- D. Rp12.100.000,00  
  <sub>Salah: membagi 14.520.000 dengan 1,2 (bunga tunggal 10% x 2)</sub>

**Pembahasan:** Selang 2 tahun saldo naik dengan faktor $(1+p)^2 = 1,21$, jadi $p = 10\%$. Modal awal: $14.520.000 : (1,1)^2 = 12.000.000$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b02-b-hard-bt01-014
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim dua modal berbeda*

Tabungan A berisi Rp5.000.000,00 dan tabungan B berisi Rp20.000.000,00. Keduanya berbunga majemuk 8% per tahun dan disimpan 3 tahun. Pernyataan yang benar adalah ....

- A. Tabungan B mencapai dua kali modalnya lebih cepat daripada A  
  <sub>Salah: waktu menggandakan hanya bergantung pada p, bukan modal</sub>
- B. Persentase kenaikan saldo A lebih besar daripada B karena modal A lebih kecil  
  <sub>Salah: persentase kenaikan tidak bergantung modal</sub>
- **C. Bunga B tepat 4 kali bunga A, sedangkan persentase kenaikan saldo keduanya sama** ✅  
  <sub>Benar: saldo $= M(1,08)^3$ sebanding dengan M, sehingga bunga B = 4 x bunga A dan faktor kenaikan keduanya sama</sub>
- D. Persentase kenaikan saldo B 4 kali persentase kenaikan saldo A  
  <sub>Salah: mencampur bunga rupiah dengan persentase kenaikan</sub>

**Pembahasan:** Saldo akhir $M(1,08)^3$ berbanding lurus dengan M. Bunga B = 4 x bunga A (modal 4 kali), tetapi faktor kenaikan $(1,08)^3 - 1$ sama untuk keduanya.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b02-b-hard-bt01-015
*orisinal | C6 | 4 langkah | jenis: merancang skema bunga untuk target saldo*

Bu Tika ingin uang Rp10.000.000,00 menjadi paling sedikit Rp13.000.000,00 setelah tepat 2 tahun. Skema bunga majemuk yang memenuhi keinginannya adalah ....

- A. 13% per tahun  
  <sub>Salah: $10.000.000 (1,13)^2 = 12.769.000 < 13.000.000$</sub>
- **B. 7% per semester** ✅  
  <sub>Benar: $10.000.000 (1,07)^4 = 13.107.960 \ge 13.000.000$</sub>
- C. 6% per semester  
  <sub>Salah: $10.000.000 (1,06)^4 \approx 12.624.770 < 13.000.000$</sub>
- D. 3% per triwulan  
  <sub>Salah: $10.000.000 (1,03)^8 \approx 12.667.700 < 13.000.000$</sub>

**Pembahasan:** 2 tahun = 2 periode tahunan, 4 semester, atau 8 triwulan. Saldo: 13% tahunan 12.769.000; 6% semesteran sekitar 12.624.770; 3% triwulanan sekitar 12.667.700; 7% semesteran sekitar 13.107.960. Hanya 7% per semester mencapai 13.000.000.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
