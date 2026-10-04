# Lembar koreksi — kelas11_tl SMA11L-B1 subbab C: Penjumlahan dan Pengurangan Antarmatriks

52 soal | easy 20, medium 20, hard 12 | variasi 19, orisinal 33
> **Kapasitas kurang (hard): 12 dari kuota 20** — Materi C (penjumlahan/pengurangan matriks, lawan, sifat 1.1) sempit dan 40 soal easy+medium sudah menghabiskan hitungan dan persamaan matriks; hard bermakna hanya lewat penalaran (evaluasi klaim, penyangkal, parameter, temukan kesalahan) yang layak 12 soal tanpa nyaris kembar. Acuan siswa terbaca habis sehingga semua soal orisinal (hard tanpa batas bawah variasi).

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b01-c-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: konsep penjumlahan*

Matriks $A$ dan $B$ berordo sama. Pernyataan yang benar mengenai cara memperoleh matriks $A + B$ adalah ....

- A. Semua elemen $A$ dijumlahkan lebih dulu, kemudian ditambahkan dengan jumlah semua elemen $B$  
  <sub>Salah: mengira penjumlahan matriks menghasilkan satu bilangan</sub>
- **B. Elemen-elemen $A$ dan $B$ yang seletak dijumlahkan, dan hasilnya berordo sama dengan $A$ dan $B$** ✅  
  <sub>Benar: menurut definisi penjumlahan matriks, $c_{ij} = a_{ij} + b_{ij}$ sehingga ordo hasil sama</sub>
- C. Baris-baris $A$ dikalikan dengan kolom-kolom $B$, lalu hasilnya dijumlahkan  
  <sub>Salah: mencampur dengan prosedur perkalian matriks</sub>
- D. Ordo hasil adalah jumlah ordo $A$ dan ordo $B$ sehingga matriks hasil lebih besar  
  <sub>Salah: mengira ordo ikut dijumlahkan</sub>

**Pembahasan:** Jika $A$ dan $B$ berordo $m \times n$, maka $C = A + B$ berordo $m \times n$ dengan $c_{ij} = a_{ij} + b_{ij}$.
**Acuan:** siswa — siswa hal.34 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b01-c-easy-bt01-002
*variasi (konteks) | C1 | 1 langkah | jenis: konsep penjumlahan*

Pada penjumlahan dua matriks $A$ dan $B$ yang berordo sama, elemen baris ke-2 kolom ke-3 matriks $A + B$ diperoleh dengan cara ....

- A. menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-3 kolom ke-2 matriks $B$  
  <sub>Salah: baris dan kolom tertukar sehingga elemen tidak seletak</sub>
- B. mengalikan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen yang seletak pada matriks $B$  
  <sub>Salah: mengganti penjumlahan dengan perkalian</sub>
- C. menjumlahkan semua elemen baris ke-2 matriks $A$ dengan semua elemen baris ke-2 matriks $B$  
  <sub>Salah: menjumlahkan satu baris penuh, bukan satu elemen</sub>
- **D. menjumlahkan elemen baris ke-2 kolom ke-3 matriks $A$ dengan elemen baris ke-2 kolom ke-3 matriks $B$** ✅  
  <sub>Benar: penjumlahan dilakukan pada elemen yang seletak</sub>

**Pembahasan:** Elemen $c_{23} = a_{23} + b_{23}$, yaitu penjumlahan elemen yang seletak.
**Acuan:** siswa — siswa hal.34 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b01-c-easy-bt01-003
*variasi (konteks) | C1 | 1 langkah | jenis: syarat ordo operasi*

Matriks $M$ berordo $4 \times 3$. Matriks $N$ dapat dikurangkan dari $M$ (selisih $M - N$ terdefinisi) hanya jika $N$ berordo ....

- A. $3 \times 3$  
  <sub>Salah: hanya menyamakan banyak kolom</sub>
- B. $4 \times 4$  
  <sub>Salah: hanya menyamakan banyak baris</sub>
- C. $3 \times 4$  
  <sub>Salah: ordo dibalik (banyak baris dan kolom tertukar)</sub>
- **D. $4 \times 3$** ✅  
  <sub>Benar: pengurangan hanya terdefinisi untuk matriks berordo sama</sub>

**Pembahasan:** Dua matriks dapat dikurangkan apabila ordonya sama, jadi $N$ harus berordo $4 \times 3$.
**Acuan:** siswa — siswa hal.34 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b01-c-easy-bt01-004
*variasi (konteks) | C2 | 1 langkah | jenis: syarat ordo operasi*

Matriks $P$ dan $Q$ sama-sama berordo $3 \times 5$. Ordo matriks $P - Q$ adalah ....

- A. $6 \times 10$  
  <sub>Salah: ordo kedua matriks dijumlahkan</sub>
- B. $5 \times 3$  
  <sub>Salah: ordo dibalik</sub>
- C. $3 \times 3$  
  <sub>Salah: hanya mengingat banyak baris</sub>
- **D. $3 \times 5$** ✅  
  <sub>Benar: selisih dua matriks berordo $m \times n$ juga berordo $m \times n$</sub>

**Pembahasan:** Pengurangan dilakukan elemen demi elemen sehingga hasilnya tetap berordo $3 \times 5$.
**Acuan:** siswa — siswa hal.34 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b01-c-easy-bt01-005
*variasi (konteks) | C2 | 1 langkah | jenis: syarat ordo operasi*

Diketahui $A$ = $\begin{bmatrix} 8 & -4 \\ 7 & 5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 6 & 2 \\ -3 & 9 \\ 4 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A + B$ adalah ....

- A. $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \\ 4 & 1 \end{bmatrix}$ karena baris ketiga $B$ disalin  
  <sub>Salah: menyalin baris tanpa pasangan seolah dijumlah dengan nol</sub>
- **B. $A + B$ tidak terdefinisi karena ordo $A$ dan $B$ berbeda** ✅  
  <sub>Benar: $A$ berordo $2 \times 2$ sedangkan $B$ berordo $3 \times 2$</sub>
- C. $A + B$ = $\begin{bmatrix} 14 & -2 \\ 4 & 14 \end{bmatrix}$ karena baris ketiga $B$ diabaikan  
  <sub>Salah: mengabaikan baris yang tidak punya pasangan</sub>
- D. $A + B$ terdefinisi dan berordo $5 \times 2$  
  <sub>Salah: mengira ordo hasil adalah jumlah ordo</sub>

**Pembahasan:** Penjumlahan hanya terdefinisi bila ordo sama. Ordo $A$ adalah $2 \times 2$ dan ordo $B$ adalah $3 \times 2$, sehingga $A + B$ tidak terdefinisi.
**Acuan:** siswa — siswa hal.34 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b01-c-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: soal cerita operasi matriks*

Dua pabrik roti mencatat pengeluaran bulan ini (dalam juta rupiah) untuk tepung dan gula, dengan baris menyatakan Pabrik I dan Pabrik II serta kolom menyatakan roti tawar dan roti manis. Pengeluaran tepung $\begin{bmatrix} 14 & 22 \\ 9 & 17 \end{bmatrix}$ dan pengeluaran gula $\begin{bmatrix} 5 & 8 \\ 6 & 3 \end{bmatrix}$. Matriks total pengeluaran kedua bahan tersebut adalah ....

- **A. $\begin{bmatrix} 19 & 30 \\ 15 & 20 \end{bmatrix}$** ✅  
  <sub>Benar: total pengeluaran = jumlah elemen seletak: 14+5, 22+8, 9+6, 17+3</sub>
- B. $\begin{bmatrix} 9 & 14 \\ 3 & 14 \end{bmatrix}$  
  <sub>Salah: mengurangkan, bukan menjumlahkan</sub>
- C. $\begin{bmatrix} 19 & 15 \\ 30 & 20 \end{bmatrix}$  
  <sub>Salah: baris dan kolom hasil tertukar (transpos)</sub>
- D. $\begin{bmatrix} 19 & 30 \\ 15 & 23 \end{bmatrix}$  
  <sub>Salah: elemen terakhir dijumlahkan dengan elemen yang tidak seletak (17 + 6)</sub>

**Pembahasan:** Total = tepung + gula = $\begin{bmatrix} 19 & 30 \\ 15 & 20 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.28 Eksplorasi Penjumlahan Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b01-c-easy-bt01-007
*variasi (konteks) | C2 | 1 langkah | jenis: soal cerita operasi matriks*

Banyak pesanan (unit) yang diterima sebuah toko daring.

| Minggu I | Kaos | Topi |
|---|---|---|
| Cabang Timur | 12 | 7 |
| Cabang Barat | 9 | 15 |
| Cabang Utara | 4 | 10 |

| Minggu II | Kaos | Topi |
|---|---|---|
| Cabang Timur | 6 | 5 |
| Cabang Barat | 11 | 4 |
| Cabang Utara | 8 | 2 |

Matriks banyak pesanan selama dua minggu, dengan baris menyatakan cabang (Timur, Barat, Utara) dan kolom menyatakan barang (kaos, topi), adalah ....

- A. $\begin{bmatrix} 18 & 20 & 12 \\ 12 & 19 & 12 \end{bmatrix}$  
  <sub>Salah: matriks hasil ditulis dengan baris dan kolom tertukar</sub>
- B. $\begin{bmatrix} 6 & 2 \\ -2 & 11 \\ -4 & 8 \end{bmatrix}$  
  <sub>Salah: mengurangkan pesanan minggu I dengan minggu II</sub>
- **C. $\begin{bmatrix} 18 & 12 \\ 20 & 19 \\ 12 & 12 \end{bmatrix}$** ✅  
  <sub>Benar: jumlahkan elemen seletak kedua tabel</sub>
- D. $\begin{bmatrix} -6 & -2 \\ 2 & -11 \\ 4 & -8 \end{bmatrix}$  
  <sub>Salah: mengurangkan dengan urutan terbalik</sub>

**Pembahasan:** Hasil = $\begin{bmatrix} 18 & 12 \\ 20 & 19 \\ 12 & 12 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.28 Eksplorasi Penjumlahan Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b01-c-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: soal cerita operasi matriks*

Sebuah toko buku memiliki stok awal (eksemplar) pada cabang X dan cabang Y untuk novel, komik, dan kamus: $\begin{bmatrix} 40 & 25 \\ 30 & 18 \\ 22 & 35 \end{bmatrix}$, dengan kolom pertama cabang X dan kolom kedua cabang Y. Buku yang terjual dalam sebulan: $\begin{bmatrix} 12 & 9 \\ 10 & 17 \\ 5 & 14 \end{bmatrix}$. Matriks sisa stok setiap jenis buku di kedua cabang adalah ....

- A. $\begin{bmatrix} 28 & 20 & 17 \\ 16 & 1 & 21 \end{bmatrix}$  
  <sub>Salah: hasil benar tetapi baris dan kolom tertukar</sub>
- B. $\begin{bmatrix} 52 & 34 \\ 40 & 35 \\ 27 & 49 \end{bmatrix}$  
  <sub>Salah: menjumlahkan stok dengan yang terjual</sub>
- C. $\begin{bmatrix} -28 & -16 \\ -20 & -1 \\ -17 & -21 \end{bmatrix}$  
  <sub>Salah: urutan pengurangan terbalik sehingga semua elemen bernilai negatif</sub>
- **D. $\begin{bmatrix} 28 & 16 \\ 20 & 1 \\ 17 & 21 \end{bmatrix}$** ✅  
  <sub>Benar: sisa = stok awal dikurangi terjual, elemen seletak</sub>

**Pembahasan:** Sisa = $\begin{bmatrix} 28 & 16 \\ 20 & 1 \\ 17 & 21 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.35 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b01-c-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: soal cerita operasi matriks*

Kapasitas kursi dua studio bioskop pada sesi siang dan malam adalah $\begin{bmatrix} 80 & 60 \\ 120 & 90 \end{bmatrix}$ (baris: studio 1 dan 2; kolom: siang dan malam). Kursi yang terisi adalah $\begin{bmatrix} 57 & 41 \\ 85 & 63 \end{bmatrix}$. Matriks banyak kursi yang masih kosong adalah ....

- **A. $\begin{bmatrix} 23 & 19 \\ 35 & 27 \end{bmatrix}$** ✅  
  <sub>Benar: kursi kosong = kapasitas dikurangi terisi</sub>
- B. $\begin{bmatrix} 137 & 101 \\ 205 & 153 \end{bmatrix}$  
  <sub>Salah: menjumlahkan kapasitas dan kursi terisi</sub>
- C. $\begin{bmatrix} 23 & 19 \\ 120 & 90 \end{bmatrix}$  
  <sub>Salah: baris kedua belum dikurangkan (setengah langkah)</sub>
- D. $\begin{bmatrix} 23 & 35 \\ 19 & 27 \end{bmatrix}$  
  <sub>Salah: hasil benar tetapi ditulis transpos</sub>

**Pembahasan:** Kursi kosong = $\begin{bmatrix} 23 & 19 \\ 35 & 27 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.35 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b01-c-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: sifat operasi matriks*

Diketahui $A$ = $\begin{bmatrix} 5 & 2 \\ 1 & 4 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 3 & 6 \\ 0 & 1 \end{bmatrix}$. Pernyataan yang benar mengenai $A - B$ dan $B - A$ adalah ....

- A. $A - B$ dan $B - A$ berbeda ordo sehingga tidak dapat dibandingkan  
  <sub>Salah: mengira urutan pengurangan mengubah ordo hasil</sub>
- **B. $A - B$ dan $B - A$ saling berlawanan sehingga tidak sama; sifat komutatif tidak berlaku pada pengurangan** ✅  
  <sub>Benar: $A - B$ = $\begin{bmatrix} 2 & -4 \\ 1 & 3 \end{bmatrix}$ sedangkan $B - A$ = $\begin{bmatrix} -2 & 4 \\ -1 & -3 \end{bmatrix}$</sub>
- C. $A - B$ terdefinisi, tetapi $B - A$ tidak terdefinisi  
  <sub>Salah: mengira urutan pengurangan memengaruhi keterdefinisian</sub>
- D. $A - B$ dan $B - A$ sama karena kedua matriks berordo sama; sifat komutatif berlaku pada pengurangan  
  <sub>Salah: mengira pengurangan bersifat komutatif seperti penjumlahan</sub>

**Pembahasan:** $A - B$ = $\begin{bmatrix} 2 & -4 \\ 1 & 3 \end{bmatrix}$ dan $B - A$ = $\begin{bmatrix} -2 & 4 \\ -1 & -3 \end{bmatrix}$. Keduanya berlawanan, jadi $A - B \neq B - A$.
**Acuan:** siswa — siswa hal.32 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b01-c-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: hitung langsung penjumlahan/pengurangan*

Diketahui $A$ = $\begin{bmatrix} 5 & -2 \\ 8 & 6 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} -4 & 7 \\ 3 & -9 \end{bmatrix}$. Hasil $A + B$ adalah ....

- A. $\begin{bmatrix} 9 & -9 \\ 5 & 15 \end{bmatrix}$  
  <sub>Salah: mengurangkan, bukan menjumlahkan</sub>
- **B. $\begin{bmatrix} 1 & 5 \\ 11 & -3 \end{bmatrix}$** ✅  
  <sub>Benar: jumlahkan elemen seletak</sub>
- C. $\begin{bmatrix} 1 & 5 \\ 11 & 15 \end{bmatrix}$  
  <sub>Salah: salah tanda: 6 + (-9) dihitung 6 + 9</sub>
- D. $\begin{bmatrix} -20 & -14 \\ 24 & -54 \end{bmatrix}$  
  <sub>Salah: mengalikan elemen yang seletak</sub>

**Pembahasan:** $A + B$ = $\begin{bmatrix} 1 & 5 \\ 11 & -3 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b01-c-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: hitung langsung penjumlahan/pengurangan*

Diketahui $A$ = $\begin{bmatrix} 3 & -1 & 6 \\ 2 & 8 & -5 \end{bmatrix}$ dan $B$ = $\begin{bmatrix} 4 & 2 & -7 \\ -6 & 1 & 9 \end{bmatrix}$. Nilai elemen baris ke-2 kolom ke-3 dari $A + B$ adalah ....

- **A. $4$** ✅  
  <sub>Benar: $-5 + 9 = 4$</sub>
- B. $9$  
  <sub>Salah: mengambil elemen baris ke-2 kolom ke-2 ($8 + 1$)</sub>
- C. $-14$  
  <sub>Salah: mengurangkan: $-5 - 9$</sub>
- D. $14$  
  <sub>Salah: tanda negatif pada $-5$ diabaikan</sub>

**Pembahasan:** Elemen baris ke-2 kolom ke-3: $a_{23} + b_{23} = -5 + 9 = 4$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b01-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: hitung langsung penjumlahan/pengurangan*

Diketahui $P$ = $\begin{bmatrix} 6 & -3 \\ -2 & 5 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} -4 & 1 \\ 7 & -8 \end{bmatrix}$. Hasil $P - Q$ adalah ....

- A. $\begin{bmatrix} -10 & 4 \\ 9 & -13 \end{bmatrix}$  
  <sub>Salah: urutan pengurangan terbalik</sub>
- B. $\begin{bmatrix} 2 & -2 \\ 5 & -3 \end{bmatrix}$  
  <sub>Salah: menjumlahkan, bukan mengurangkan</sub>
- C. $\begin{bmatrix} 10 & -2 \\ 5 & 13 \end{bmatrix}$  
  <sub>Salah: salah tanda pada elemen yang melibatkan bilangan negatif ($-3-1$ dan $-2-7$)</sub>
- **D. $\begin{bmatrix} 10 & -4 \\ -9 & 13 \end{bmatrix}$** ✅  
  <sub>Benar: kurangkan elemen seletak: 6-(-4)=10, -3-1=-4, -2-7=-9, 5-(-8)=13</sub>

**Pembahasan:** $P - Q$ = $\begin{bmatrix} 10 & -4 \\ -9 & 13 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b01-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: hitung langsung penjumlahan/pengurangan*

Diketahui $M$ = $\begin{bmatrix} 8 & -1 & 5 \end{bmatrix}$ dan $N$ = $\begin{bmatrix} 3 & 6 & -4 \end{bmatrix}$. Hasil $M - N$ adalah ....

- A. $\begin{bmatrix} 11 & 5 & 1 \end{bmatrix}$  
  <sub>Salah: menjumlahkan, bukan mengurangkan</sub>
- B. $\begin{bmatrix} -5 & 7 & -9 \end{bmatrix}$  
  <sub>Salah: urutan pengurangan terbalik</sub>
- **C. $\begin{bmatrix} 5 & -7 & 9 \end{bmatrix}$** ✅  
  <sub>Benar: 8-3=5, -1-6=-7, 5-(-4)=9</sub>
- D. $\begin{bmatrix} 5 & -7 & 1 \end{bmatrix}$  
  <sub>Salah: tanda negatif pada $-4$ diabaikan ($5 - 4$)</sub>

**Pembahasan:** $M - N$ = $\begin{bmatrix} 5 & -7 & 9 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b01-c-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: sifat dan lawan matriks*

Lawan dari matriks $A$ = $\begin{bmatrix} 3 & -5 \\ -1 & 0 \\ 6 & 2 \end{bmatrix}$ adalah ....

- A. $\begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}$  
  <sub>Salah: mengira lawan matriks adalah matriks nol</sub>
- **B. $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$** ✅  
  <sub>Benar: lawan matriks $A$ adalah $-A$, semua elemennya dikalikan $-1$</sub>
- C. $\begin{bmatrix} -3 & -5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$  
  <sub>Salah: elemen negatif tidak diubah tandanya</sub>
- D. $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & 2 \end{bmatrix}$  
  <sub>Salah: elemen terakhir tidak diubah tandanya</sub>

**Pembahasan:** $-A$ = $\begin{bmatrix} -3 & 5 \\ 1 & 0 \\ -6 & -2 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b01-c-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: hitung langsung penjumlahan/pengurangan*

Diketahui $A$ = $\begin{bmatrix} 3 & -2 \\ 5 & 1 \end{bmatrix}$, $B$ = $\begin{bmatrix} 4 & 6 \\ -1 & 2 \end{bmatrix}$, dan $C$ = $\begin{bmatrix} 2 & -5 \\ 3 & 7 \end{bmatrix}$. Hasil $A + B - C$ adalah ....

- **A. $\begin{bmatrix} 5 & 9 \\ 1 & -4 \end{bmatrix}$** ✅  
  <sub>Benar: $A + B$ dahulu, lalu dikurangi $C$</sub>
- B. $\begin{bmatrix} -3 & -3 \\ 3 & -8 \end{bmatrix}$  
  <sub>Salah: $B$ ikut dikurangkan, bukan dijumlahkan</sub>
- C. $\begin{bmatrix} 5 & -1 \\ 1 & -4 \end{bmatrix}$  
  <sub>Salah: salah tanda pada $4 - (-5)$ (dihitung $4 - 5$)</sub>
- D. $\begin{bmatrix} 9 & -1 \\ 7 & 10 \end{bmatrix}$  
  <sub>Salah: $C$ ikut dijumlahkan, bukan dikurangkan</sub>

**Pembahasan:** $A + B$ = $\begin{bmatrix} 7 & 4 \\ 4 & 3 \end{bmatrix}$; dikurangi $C$ menjadi $\begin{bmatrix} 5 & 9 \\ 1 & -4 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b01-c-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: sifat dan lawan matriks*

Matriks $A$ dan $B$ berordo sama dengan $A + B$ = $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$. Hasil $B + A$ adalah ....

- A. $\begin{bmatrix} 3 & 8 \\ -1 & 2 \end{bmatrix}$  
  <sub>Salah: baris dan kolom ditukar saat membalik urutan</sub>
- B. $\begin{bmatrix} 2 & 8 \\ -1 & 3 \end{bmatrix}$  
  <sub>Salah: elemen disusun dari belakang</sub>
- **C. $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$** ✅  
  <sub>Benar: sifat komutatif: $A + B = B + A$</sub>
- D. $\begin{bmatrix} -3 & 1 \\ -8 & -2 \end{bmatrix}$  
  <sub>Salah: mengira urutan terbalik mengubah tanda</sub>

**Pembahasan:** Penjumlahan matriks bersifat komutatif, sehingga $B + A = A + B$ = $\begin{bmatrix} 3 & -1 \\ 8 & 2 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b01-c-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: sifat dan lawan matriks*

Untuk matriks $A$ dan $B$ yang berordo sama, pengurangan $A - B$ didefinisikan sebagai ....

- A. $-(A + B)$  
  <sub>Salah: mengira seluruh jumlah dibalik tandanya</sub>
- B. $(-A) + B$  
  <sub>Salah: lawan dikenakan pada matriks yang salah (hasilnya $B - A$)</sub>
- **C. $A + (-B)$** ✅  
  <sub>Benar: pengurangan = jumlah matriks pertama dengan lawan matriks kedua</sub>
- D. $A + B$  
  <sub>Salah: mengabaikan lawan matriks</sub>

**Pembahasan:** Definisi 1.3: $A - B = A + (-B)$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b01-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: persamaan matriks*

Diketahui $\begin{bmatrix} x & 3 \\ 2 & y \end{bmatrix}$ + $\begin{bmatrix} 4 & -1 \\ 5 & 6 \end{bmatrix}$ = $\begin{bmatrix} 9 & 2 \\ 7 & 10 \end{bmatrix}$. Nilai $x + y$ adalah ....

- **A. $9$** ✅  
  <sub>Benar: $x + 4 = 9$ sehingga $x = 5$; $y + 6 = 10$ sehingga $y = 4$; $x + y = 9$</sub>
- B. $1$  
  <sub>Salah: yang dihitung $x - y$, bukan $x + y$</sub>
- C. $20$  
  <sub>Salah: yang dihitung $x \cdot y$</sub>
- D. $29$  
  <sub>Salah: $x$ dan $y$ diperoleh dengan menjumlahkan, bukan mengurangkan ($9+4$ dan $10+6$)</sub>

**Pembahasan:** Elemen seletak: $x + 4 = 9$ dan $y + 6 = 10$, sehingga $x = 5$ dan $y = 4$, maka $x + y = 9$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b01-c-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: persamaan matriks*

Diketahui $P$ = $\begin{bmatrix} 2 & -5 \\ 6 & 1 \end{bmatrix}$ dan $Q$ = $\begin{bmatrix} 9 & -3 \\ -4 & 9 \end{bmatrix}$. Jika $X$ matriks berordo $2 \times 2$ dan $X + P = Q$, maka $X$ adalah ....

- A. $\begin{bmatrix} 7 & -8 \\ -10 & 8 \end{bmatrix}$  
  <sub>Salah: salah tanda pada $-3 - (-5)$ (dihitung $-3 - 5$)</sub>
- B. $\begin{bmatrix} 11 & -8 \\ 2 & 10 \end{bmatrix}$  
  <sub>Salah: $P$ dijumlahkan ke $Q$ bukan dipindahkan ruas</sub>
- **C. $\begin{bmatrix} 7 & 2 \\ -10 & 8 \end{bmatrix}$** ✅  
  <sub>Benar: $X = Q - P$</sub>
- D. $\begin{bmatrix} -7 & -2 \\ 10 & -8 \end{bmatrix}$  
  <sub>Salah: urutan pengurangan terbalik ($P - Q$)</sub>

**Pembahasan:** $X = Q - P$ = $\begin{bmatrix} 7 & 2 \\ -10 & 8 \end{bmatrix}$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b01-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} 3x & y \\ 5z & 7z \end{pmatrix}$ - $\begin{pmatrix} 19 & -x \\ -4y & 17 \end{pmatrix}$ + $\begin{pmatrix} 4 & -3 \\ -7 & -4 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ berturut-turut adalah ....

- A. $x = 5$, $y = -2$, $z = -3$  
  <sub>Salah: salah tanda saat menyelesaikan $5z + 4y - 7 = 0$ ($5z = -15$)</sub>
- **B. $x = 5$, $y = -2$, $z = 3$** ✅  
  <sub>Benar: elemen (1,1): $3x - 19 + 4 = 0$ sehingga $x = 5$; (1,2): $y + x - 3 = 0$ sehingga $y = -2$; (2,1): $5z + 4y - 7 = 0$ sehingga $z = 3$</sub>
- C. $x = 5$, $y = -8$, $z = 3$  
  <sub>Salah: salah tanda pada elemen (1,2): $y + x + 3 = 0$</sub>
- D. $x = -5$, $y = -2$, $z = 3$  
  <sub>Salah: salah tanda saat menyelesaikan $3x - 19 + 4 = 0$ ($3x = -15$)</sub>

**Pembahasan:** Elemen seletak: $3x - 19 + 4 = 0 \Rightarrow x = 5$; $y - (-x) + (-3) = 0 \Rightarrow y = -2$; $5z - (-4y) + (-7) = 0 \Rightarrow z = 3$; cek $7z - 17 - 4 = 0$.
**Acuan:** pretest — kelas11_tl-b01-p0035-latihan-c-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b01-c-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} 3x & 2y \\ z & 4z \end{pmatrix}$ - $\begin{pmatrix} 5 & -3x \\ 2y & -9 \end{pmatrix}$ + $\begin{pmatrix} 11 & -4 \\ 13 & 3 \end{pmatrix}$ = $\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$. Nilai $x$, $y$, dan $z$ yang memenuhi adalah ....

- A. $x = -2$, $y = 5$, $z = 3$  
  <sub>Salah: salah tanda saat menyelesaikan $4z + 9 + 3 = 0$ ($4z = 12$)</sub>
- **B. $x = -2$, $y = 5$, $z = -3$** ✅  
  <sub>Benar: $3x - 5 + 11 = 0$ sehingga $x = -2$; $2y + 3x - 4 = 0$ sehingga $y = 5$; $z - 2y + 13 = 0$ sehingga $z = -3$</sub>
- C. $x = -2$, $y = -1$, $z = -3$  
  <sub>Salah: salah tanda pada $-(-3x)$ sehingga $2y - 3x - 4 = 0$</sub>
- D. $x = 2$, $y = -1$, $z = -3$  
  <sub>Salah: salah tanda pada $3x + 6 = 0$ sehingga $x = 2$ dan $y$ ikut salah</sub>

**Pembahasan:** Elemen (1,1): $3x - 5 + 11 = 0$, $x = -2$. Elemen (1,2): $2y - (-3x) - 4 = 0$, $y = 5$. Elemen (2,1): $z - 2y + 13 = 0$, $z = -3$. Cek (2,2): $4z + 9 + 3 = 0$.
**Acuan:** pretest — kelas11_tl-b01-p0035-latihan-c-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b01-c-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} 7a \\ 7b \end{pmatrix}$ + $\begin{pmatrix} 3b \\ 3a \end{pmatrix}$ = $\begin{pmatrix} 5 \\ -15 \end{pmatrix}$. Nilai $a$ dan $b$ adalah ....

- **A. $a = 2$, $b = -3$** ✅  
  <sub>Benar: $7a + 3b = 5$ dan $3a + 7b = -15$; eliminasi memberi $a = 2$ dan $b = -3$</sub>
- B. $a = -2$, $b = 3$  
  <sub>Salah: kedua nilai salah tanda</sub>
- C. $a = 2$, $b = 3$  
  <sub>Salah: salah tanda pada nilai $b$</sub>
- D. $a = -3$, $b = 2$  
  <sub>Salah: nilai $a$ dan $b$ tertukar</sub>

**Pembahasan:** Elemen seletak: $7a + 3b = 5$ dan $3a + 7b = -15$. Dari eliminasi: $40b = -120$ sehingga $b = -3$ dan $a = 2$.
**Acuan:** pretest — kelas11_tl-b01-p0035-latihan-c-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b01-c-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} 9a \\ 2b \end{pmatrix}$ + $\begin{pmatrix} 5b \\ 6a \end{pmatrix}$ = $\begin{pmatrix} 11 \\ 14 \end{pmatrix}$. Nilai $a + b$ adalah ....

- A. $-20$  
  <sub>Salah: yang dihitung $a \cdot b$</sub>
- B. $9$  
  <sub>Salah: yang dihitung $a - b$, bukan $a + b$</sub>
- **C. $-1$** ✅  
  <sub>Benar: $9a + 5b = 11$ dan $6a + 2b = 14$ memberi $a = 4$, $b = -5$ sehingga $a + b = -1$</sub>
- D. $1$  
  <sub>Salah: salah tanda pada hasil akhir</sub>

**Pembahasan:** Dari $9a + 5b = 11$ dan $6a + 2b = 14$ diperoleh $a = 4$ dan $b = -5$, sehingga $a + b = -1$.
**Acuan:** pretest — kelas11_tl-b01-p0035-latihan-c-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b01-c-medium-bt01-005
*orisinal | C3 | 4 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} a+b & 2c \\ c-d & 3a \end{pmatrix}$ + $\begin{pmatrix} 2a & -c \\ 4 & -b \end{pmatrix}$ = $\begin{pmatrix} 11 & 4 \\ 9 & 7 \end{pmatrix}$. Nilai $a + b + c + d$ adalah ....

- A. $4$  
  <sub>Salah: salah tanda pada $b$ (dipakai $b = -2$)</sub>
- **B. $8$** ✅  
  <sub>Benar: $3a + b = 11$ dan $3a - b = 7$ memberi $a = 3$, $b = 2$; $c = 4$; $c - d + 4 = 9$ memberi $d = -1$; jumlah $= 8$</sub>
- C. $9$  
  <sub>Salah: nilai $d$ tidak ikut dijumlahkan</sub>
- D. $10$  
  <sub>Salah: salah tanda pada $d$ (dipakai $d = 1$)</sub>

**Pembahasan:** Elemen (1,1): $(a+b) + 2a = 11$; (2,2): $3a - b = 7$; sehingga $a = 3$, $b = 2$. Elemen (1,2): $2c - c = 4$, $c = 4$. Elemen (2,1): $c - d + 4 = 9$, $d = -1$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b01-c-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: mencari matriks X*

Diketahui $A$ = $\begin{pmatrix} 7 & -2 \\ 4 & 9 \\ -5 & 3 \end{pmatrix}$, $B$ = $\begin{pmatrix} 12 & 6 \\ -3 & 8 \\ 10 & -4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -9 \\ 2 & -6 \\ 8 & 1 \end{pmatrix}$. Jika $X$ matriks berordo $3 \times 2$ dan $X + A = B - C$, maka $X$ adalah ....

- A. $\begin{pmatrix} 14 & 13 \\ -1 & 23 \\ -3 & -2 \end{pmatrix}$  
  <sub>Salah: $A$ ditambahkan ke ruas kanan, bukan dipindahkan dengan tanda berlawanan</sub>
- B. $\begin{pmatrix} 0 & -17 \\ 9 & -5 \\ -7 & 8 \end{pmatrix}$  
  <sub>Salah: urutan pengurangan terbalik: dihitung $A - B + C$</sub>
- **C. $\begin{pmatrix} 0 & 17 \\ -9 & 5 \\ 7 & -8 \end{pmatrix}$** ✅  
  <sub>Benar: $X = B - C - A$, dihitung elemen demi elemen</sub>
- D. $\begin{pmatrix} 10 & -1 \\ -5 & -7 \\ 23 & -6 \end{pmatrix}$  
  <sub>Salah: tanda $C$ salah: dihitung $B + C - A$</sub>

**Pembahasan:** $X + A = B - C \Rightarrow X = B - C - A$. $B - C$ = $\begin{pmatrix} 7 & 15 \\ -5 & 14 \\ 2 & -5 \end{pmatrix}$, dikurangi $A$ menjadi $\begin{pmatrix} 0 & 17 \\ -9 & 5 \\ 7 & -8 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b01-c-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: mencari matriks X*

Diketahui $A$ = $\begin{pmatrix} 9 & -4 & 6 \\ 2 & 8 & -5 \end{pmatrix}$, $B$ = $\begin{pmatrix} 3 & 7 & -2 \\ -6 & 1 & 4 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -3 & 8 \\ 2 & 9 & -1 \end{pmatrix}$. Jika $A - X = B + C$, maka $X$ adalah ....

- **A. $\begin{pmatrix} 1 & -8 & 0 \\ 6 & -2 & -8 \end{pmatrix}$** ✅  
  <sub>Benar: $X = A - (B + C) = A - B - C$</sub>
- B. $\begin{pmatrix} -1 & 8 & 0 \\ -6 & 2 & 8 \end{pmatrix}$  
  <sub>Salah: urutan terbalik: dihitung $B + C - A$</sub>
- C. $\begin{pmatrix} 11 & -14 & 16 \\ 10 & 16 & -10 \end{pmatrix}$  
  <sub>Salah: tanda $C$ salah: dihitung $A - B + C$</sub>
- D. $\begin{pmatrix} 17 & 0 & 12 \\ -2 & 18 & -2 \end{pmatrix}$  
  <sub>Salah: semua matriks dijumlahkan</sub>

**Pembahasan:** $A - X = B + C \Rightarrow X = A - (B + C)$. $B + C$ = $\begin{pmatrix} 8 & 4 & 6 \\ -4 & 10 & 3 \end{pmatrix}$, sehingga $X$ = $\begin{pmatrix} 1 & -8 & 0 \\ 6 & -2 & -8 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b01-c-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: mencari matriks X*

Diketahui $P$ = $\begin{pmatrix} 6 & -3 \\ -8 & 5 \\ 2 & 9 \end{pmatrix}$, $Q$ = $\begin{pmatrix} 4 & 7 \\ -1 & -6 \\ 3 & 2 \end{pmatrix}$, dan $R$ = $\begin{pmatrix} -5 & 2 \\ 9 & 1 \\ -4 & 8 \end{pmatrix}$. Jika $X$ memenuhi $(X - P) + (Q - R) = O$ dengan $O$ matriks nol berordo $3 \times 2$, maka $X$ adalah ....

- A. $\begin{pmatrix} 15 & 2 \\ -18 & -2 \\ 9 & 3 \end{pmatrix}$  
  <sub>Salah: lawan $(Q - R)$ tidak dikerjakan: dihitung $P + Q - R$</sub>
- B. $\begin{pmatrix} 7 & -12 \\ -16 & 10 \\ 3 & -1 \end{pmatrix}$  
  <sub>Salah: tanda $R$ salah: dihitung $P - Q - R$</sub>
- C. $\begin{pmatrix} 3 & 8 \\ -2 & -12 \\ 5 & -15 \end{pmatrix}$  
  <sub>Salah: seluruh hasil terbalik tanda</sub>
- **D. $\begin{pmatrix} -3 & -8 \\ 2 & 12 \\ -5 & 15 \end{pmatrix}$** ✅  
  <sub>Benar: $X - P = -(Q - R) = R - Q$ sehingga $X = P - Q + R$</sub>

**Pembahasan:** $(X - P) + (Q - R) = O \Rightarrow X = P - (Q - R) = P - Q + R$ = $\begin{pmatrix} -3 & -8 \\ 2 & 12 \\ -5 & 15 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b01-c-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: syarat ordo operasi*

Matriks $A$ berordo $(2m - 1) \times (n + 2)$ dan matriks $B$ berordo $5 \times 6$. Jika $A - B$ terdefinisi dengan $m$ dan $n$ bilangan asli, nilai $m + n$ adalah ....

- A. $9$  
  <sub>Salah: $n$ dihitung $n = 6$ (konstanta $+2$ diabaikan)</sub>
- **B. $7$** ✅  
  <sub>Benar: ordo harus sama: $2m - 1 = 5$ sehingga $m = 3$ dan $n + 2 = 6$ sehingga $n = 4$</sub>
- C. $11$  
  <sub>Salah: yang dijumlahkan adalah banyak baris dan kolom $B$ ($5 + 6$)</sub>
- D. $6$  
  <sub>Salah: salah menyelesaikan $2m - 1 = 5$ menjadi $2m = 4$</sub>

**Pembahasan:** $A - B$ terdefinisi bila ordo sama: $2m - 1 = 5 \Rightarrow m = 3$ dan $n + 2 = 6 \Rightarrow n = 4$, sehingga $m + n = 7$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b01-c-medium-bt01-010
*variasi (konteks) | C4 | 3 langkah | jenis: syarat ordo operasi*

Biaya pembelian kain pada bulan Januari disusun dalam matriks $P$ berordo $3 \times 4$ (baris: jenis kain, kolom: pemasok ke-1 sampai ke-4). Pada bulan Februari pemasok ke-4 tidak dipakai lagi sehingga matriks $Q$ hanya berordo $3 \times 3$. Agar $P + Q$ dapat dihitung tanpa menambah data baru pada $Q$, pernyataan yang benar adalah ....

- **A. Kolom pemasok ke-4 pada $P$ dihapus sehingga $P$ berordo $3 \times 3$ dan $P + Q$ berordo $3 \times 3$** ✅  
  <sub>Benar: ordo harus sama, jadi $P$ harus dikurangi satu kolom sehingga menjadi $3 \times 3$</sub>
- B. Baris ketiga pada $P$ dihapus sehingga $P$ berordo $2 \times 4$ dan $P + Q$ berordo $2 \times 4$  
  <sub>Salah: baris yang dikurangi, padahal selisih ordo ada pada kolom</sub>
- C. Kolom pemasok ke-1 pada $Q$ digandakan sehingga $Q$ berordo $3 \times 4$ dan $P + Q$ berordo $3 \times 4$  
  <sub>Salah: menambah kolom dengan menyalin data sehingga data $Q$ berubah (melanggar syarat tanpa data baru)</sub>
- D. Kolom pemasok ke-4 pada $P$ dihapus sehingga $P + Q$ dapat dihitung dan berordo $3 \times 4$  
  <sub>Salah: ordo hasil penjumlahan dikira mengikuti ordo $P$ semula</sub>

**Pembahasan:** $P$ ($3 \times 4$) dan $Q$ ($3 \times 3$) berbeda ordo. Dengan menghapus kolom pemasok ke-4 pada $P$, kedua matriks berordo $3 \times 3$ dan jumlahnya berordo $3 \times 3$.
**Acuan:** siswa — siswa hal.28 Eksplorasi Penjumlahan Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b01-c-medium-bt01-011
*variasi (konteks) | C3 | 2 langkah | jenis: interpretasi elemen hasil operasi*

Penjualan roti (buah) sebuah toko pada pagi hari dicatat dalam matriks $M$ = $\begin{pmatrix} 38 & 52 & 23 \\ 45 & 17 & 60 \end{pmatrix}$ dan pada sore hari dalam matriks $N$ = $\begin{pmatrix} 27 & 33 & 14 \\ 19 & 41 & 25 \end{pmatrix}$, dengan baris menyatakan cabang (Utara, Selatan) dan kolom menyatakan jenis roti (tawar, manis, keju). Pernyataan yang benar mengenai elemen baris ke-2 kolom ke-3 matriks $M + N$ adalah ....

- A. total roti manis yang terjual di cabang Selatan sepanjang hari, yaitu 58 buah  
  <sub>Salah: kolom yang dibaca keliru (kolom 2 dikira keju)</sub>
- B. selisih penjualan roti keju pagi dan sore di cabang Selatan, yaitu 35 buah  
  <sub>Salah: mengurangkan, bukan menjumlahkan elemen seletak</sub>
- C. total roti keju yang terjual di cabang Utara sepanjang hari, yaitu 37 buah  
  <sub>Salah: baris yang dibaca keliru (baris 1 dikira cabang Selatan)</sub>
- **D. total roti keju yang terjual di cabang Selatan sepanjang hari, yaitu 85 buah** ✅  
  <sub>Benar: $m_{23} + n_{23} = 60 + 25 = 85$, baris 2 = Selatan dan kolom 3 = keju</sub>

**Pembahasan:** Elemen $(2,3)$ dari $M + N$ adalah $60 + 25 = 85$: roti keju di cabang Selatan, pagi ditambah sore.
**Acuan:** siswa — siswa hal.28 Eksplorasi Penjumlahan Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b01-c-medium-bt01-012
*variasi (konteks) | C4 | 4 langkah | jenis: sifat operasi matriks*

Diketahui $A$ = $\begin{pmatrix} 6 & -1 \\ 3 & 8 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 5 \\ -4 & 1 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 3 & -2 \\ 7 & 4 \end{pmatrix}$. Pernyataan yang benar tentang $(A - B) - C$ dan $A - (B - C)$ adalah ....

- A. kedua bentuk sama dengan $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan  
  <sub>Salah: mengira $A - (B - C) = A - B - C$ (tanda $C$ tidak berubah)</sub>
- B. $(A - B) - C$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan  
  <sub>Salah: hasil kedua bentuk tertukar</sub>
- **C. $(A - B) - C$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$ dan $A - (B - C)$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif tidak berlaku pada pengurangan** ✅  
  <sub>Benar: kedua bentuk dihitung terpisah dan hasilnya berbeda</sub>
- D. kedua bentuk sama dengan $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$ sehingga sifat asosiatif berlaku pada pengurangan  
  <sub>Salah: mengira $(A - B) - C = A - B + C$</sub>

**Pembahasan:** $A - B$ = $\begin{pmatrix} 4 & -6 \\ 7 & 7 \end{pmatrix}$, sehingga $(A - B) - C$ = $\begin{pmatrix} 1 & -4 \\ 0 & 3 \end{pmatrix}$. $B - C$ = $\begin{pmatrix} -1 & 7 \\ -11 & -3 \end{pmatrix}$, sehingga $A - (B - C)$ = $\begin{pmatrix} 7 & -8 \\ 14 & 11 \end{pmatrix}$. Hasil berbeda.
**Acuan:** siswa — siswa hal.32 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b01-c-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: sifat operasi matriks*

Matriks $A$, $B$, dan $C$ berordo sama. Bentuk paling sederhana dari $(A + B) - (B - C) - C$ adalah ....

- **A. $A$** ✅  
  <sub>Benar: $-(B - C) = -B + C$ sehingga $A + B - B + C - C = A$</sub>
- B. $A - 2C$  
  <sub>Salah: $-(B - C)$ ditulis $-B - C$</sub>
- C. $A + 2C$  
  <sub>Salah: $-C$ di akhir ditulis $+C$</sub>
- D. $O$ (matriks nol)  
  <sub>Salah: mengira semua suku saling meniadakan, termasuk $A$</sub>

**Pembahasan:** $(A + B) - (B - C) - C = A + B - B + C - C = A + (B + (-B)) + (C + (-C)) = A$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b01-c-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: sifat operasi matriks*

Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 8 & -3 \\ 5 & 11 \end{pmatrix}$ dan $B - C$ = $\begin{pmatrix} 2 & 6 \\ -4 & 3 \end{pmatrix}$. Hasil $A + C$ adalah ....

- A. $\begin{pmatrix} 10 & 3 \\ 1 & 14 \end{pmatrix}$  
  <sub>Salah: kedua persamaan dijumlahkan, bukan dikurangkan</sub>
- B. $\begin{pmatrix} -10 & -3 \\ -1 & -14 \end{pmatrix}$  
  <sub>Salah: jumlah kedua matriks dibalik tandanya</sub>
- C. $\begin{pmatrix} -6 & 9 \\ -9 & -8 \end{pmatrix}$  
  <sub>Salah: urutan pengurangan terbalik</sub>
- **D. $\begin{pmatrix} 6 & -9 \\ 9 & 8 \end{pmatrix}$** ✅  
  <sub>Benar: $A + C = (A + B) - (B - C)$</sub>

**Pembahasan:** $(A + B) - (B - C) = A + C$, sehingga $A + C$ = $\begin{pmatrix} 8 & -3 \\ 5 & 11 \end{pmatrix}$ - $\begin{pmatrix} 2 & 6 \\ -4 & 3 \end{pmatrix}$ = $\begin{pmatrix} 6 & -9 \\ 9 & 8 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b01-c-medium-bt01-015
*variasi (konteks) | C3 | 2 langkah | jenis: soal cerita operasi matriks*

Sebuah usaha konveksi mencatat biaya (dalam juta rupiah) di dua cabang untuk dua jenis pakaian (baris: cabang I dan II; kolom: kemeja dan jaket). Biaya kain adalah $\begin{pmatrix} 24 & 35 \\ 18 & 42 \end{pmatrix}$, biaya upah penjahit adalah $\begin{pmatrix} 9 & 12 \\ 7 & 15 \end{pmatrix}$, dan biaya pengiriman adalah $\begin{pmatrix} 4 & 6 \\ 3 & 5 \end{pmatrix}$. Matriks total biaya produksi ketiga komponen tersebut adalah ....

- **A. $\begin{pmatrix} 37 & 53 \\ 28 & 62 \end{pmatrix}$** ✅  
  <sub>Benar: total = kain + upah + pengiriman, dijumlahkan pada elemen seletak</sub>
- B. $\begin{pmatrix} 11 & 17 \\ 8 & 22 \end{pmatrix}$  
  <sub>Salah: biaya kain dikurangi upah dan pengiriman</sub>
- C. $\begin{pmatrix} 29 & 41 \\ 22 & 52 \end{pmatrix}$  
  <sub>Salah: biaya pengiriman dikurangkan, bukan dijumlahkan</sub>
- D. $\begin{pmatrix} 33 & 47 \\ 25 & 57 \end{pmatrix}$  
  <sub>Salah: biaya pengiriman belum ikut dijumlahkan (setengah langkah)</sub>

**Pembahasan:** Total = $\begin{pmatrix} 33 & 47 \\ 25 & 57 \end{pmatrix}$ ditambah $\begin{pmatrix} 4 & 6 \\ 3 & 5 \end{pmatrix}$ = $\begin{pmatrix} 37 & 53 \\ 28 & 62 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.28 Eksplorasi Penjumlahan Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b01-c-medium-bt01-016
*variasi (konteks) | C4 | 3 langkah | jenis: soal cerita operasi matriks*

Dua koperasi (A dan B) menerima kiriman tiga jenis beras (kg): $\begin{pmatrix} 58 & 41 \\ 36 & 75 \\ 64 & 29 \end{pmatrix}$, dengan baris menyatakan jenis beras dan kolom menyatakan koperasi (kolom pertama koperasi A, kolom kedua koperasi B). Setelah diperiksa, beras yang rusak dan tidak layak jual adalah $\begin{pmatrix} 7 & 3 \\ 0 & 9 \\ 5 & 2 \end{pmatrix}$. Total beras layak jual di koperasi B adalah .... kg.

- A. $159$  
  <sub>Salah: beras rusak dijumlahkan, bukan dikurangkan</sub>
- B. $146$  
  <sub>Salah: yang dijumlahkan kolom koperasi A, bukan B</sub>
- **C. $131$** ✅  
  <sub>Benar: matriks layak = kiriman $-$ rusak, lalu jumlahkan kolom koperasi B: $38 + 66 + 27$</sub>
- D. $145$  
  <sub>Salah: beras rusak belum dikurangkan</sub>

**Pembahasan:** Matriks layak jual = $\begin{pmatrix} 51 & 38 \\ 36 & 66 \\ 59 & 27 \end{pmatrix}$. Kolom kedua: $38 + 66 + 27 = 131$ kg.
**Acuan:** siswa — siswa hal.35 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b01-c-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: soal cerita operasi matriks*

Penjualan tiga jenis sepatu (pasang) di dua toko dicatat tiap bulan, dengan baris menyatakan toko dan kolom menyatakan jenis sepatu. Penjualan Januari adalah $\begin{pmatrix} 34 & 28 & 19 \\ 41 & 25 & 36 \end{pmatrix}$ dan Februari adalah $\begin{pmatrix} 29 & 31 & 22 \\ 38 & 27 & 40 \end{pmatrix}$. Total penjualan selama Januari-Maret adalah $\begin{pmatrix} 95 & 89 & 64 \\ 120 & 81 & 115 \end{pmatrix}$. Matriks penjualan bulan Maret adalah ....

- A. $\begin{pmatrix} 158 & 148 & 105 \\ 199 & 133 & 191 \end{pmatrix}$  
  <sub>Salah: total ditambah penjualan kedua bulan lainnya</sub>
- **B. $\begin{pmatrix} 32 & 30 & 23 \\ 41 & 29 & 39 \end{pmatrix}$** ✅  
  <sub>Benar: Maret = total $-$ Januari $-$ Februari</sub>
- C. $\begin{pmatrix} 61 & 61 & 45 \\ 79 & 56 & 79 \end{pmatrix}$  
  <sub>Salah: penjualan Februari belum dikurangkan (setengah langkah)</sub>
- D. $\begin{pmatrix} 90 & 92 & 67 \\ 117 & 83 & 119 \end{pmatrix}$  
  <sub>Salah: penjualan Februari dijumlahkan, bukan dikurangkan</sub>

**Pembahasan:** Maret = $\begin{pmatrix} 95 & 89 & 64 \\ 120 & 81 & 115 \end{pmatrix}$ - $\begin{pmatrix} 34 & 28 & 19 \\ 41 & 25 & 36 \end{pmatrix}$ - $\begin{pmatrix} 29 & 31 & 22 \\ 38 & 27 & 40 \end{pmatrix}$ = $\begin{pmatrix} 32 & 30 & 23 \\ 41 & 29 & 39 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b01-c-medium-bt01-018
*orisinal | C3 | 4 langkah | jenis: persamaan matriks variabel elemen*

Diketahui $\begin{pmatrix} 2a & 5 \\ b+1 & 4 \end{pmatrix}$ - $\begin{pmatrix} 3 & c \\ 2b & -1 \end{pmatrix}$ = $\begin{pmatrix} 9 & -2 \\ -3 & 5 \end{pmatrix}$. Nilai $a + b + c$ adalah ....

- A. $3$  
  <sub>Salah: salah tanda pada $c$ (dipakai $c = -7$)</sub>
- B. $14$  
  <sub>Salah: $2a = 6$ sehingga $a$ dihitung $3$ (lupa membagi balik)</sub>
- C. $15$  
  <sub>Salah: $b$ salah: $-b + 1 = -3$ ditulis $-b = -3 + 1$ sehingga $b = 2$</sub>
- **D. $17$** ✅  
  <sub>Benar: $2a - 3 = 9$ sehingga $a = 6$; $5 - c = -2$ sehingga $c = 7$; $(b + 1) - 2b = -3$ sehingga $b = 4$</sub>

**Pembahasan:** Elemen (1,1): $2a - 3 = 9$, $a = 6$. Elemen (1,2): $5 - c = -2$, $c = 7$. Elemen (2,1): $b + 1 - 2b = -3$, $b = 4$. Jumlah $= 17$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b01-c-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: sistem dua persamaan matriks*

Matriks $A$ dan $B$ berordo $2 \times 2$ dengan $A + B$ = $\begin{pmatrix} 7 & 3 \\ 10 & -2 \end{pmatrix}$ dan $A - B$ = $\begin{pmatrix} 1 & 9 \\ 4 & 6 \end{pmatrix}$. Matriks $B$ adalah ....

- A. $\begin{pmatrix} 4 & 6 \\ 7 & 2 \end{pmatrix}$  
  <sub>Salah: yang dihitung adalah matriks $A$, bukan $B$</sub>
- B. $\begin{pmatrix} -3 & 3 \\ -3 & 4 \end{pmatrix}$  
  <sub>Salah: urutan pengurangan terbalik sehingga $B$ bertanda berlawanan</sub>
- **C. $\begin{pmatrix} 3 & -3 \\ 3 & -4 \end{pmatrix}$** ✅  
  <sub>Benar: tiap elemen: $a + b = p$ dan $a - b = q$, sehingga $b = (p - q) / 2$</sub>
- D. $\begin{pmatrix} 6 & -6 \\ 6 & -8 \end{pmatrix}$  
  <sub>Salah: selisih jumlah dan selisih tidak dibagi 2</sub>

**Pembahasan:** Untuk tiap elemen, $2b = (a + b) - (a - b)$. Maka $B$ = $\begin{pmatrix} 3 & -3 \\ 3 & -4 \end{pmatrix}$ (cek: $A$ = $\begin{pmatrix} 4 & 6 \\ 7 & 2 \end{pmatrix}$).
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b01-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: mencari matriks X*

Diketahui $A$ = $\begin{pmatrix} 4 & -2 & 7 \\ 3 & 5 & -1 \\ 6 & 0 & 2 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 9 & 1 & -3 \\ -4 & 8 & 2 \\ 5 & -6 & 14 \end{pmatrix}$. Jika $X + A = B$, jumlah elemen pada diagonal utama matriks $X$ adalah ....

- A. $-8$  
  <sub>Salah: yang dijumlahkan diagonal samping ($x_{13} + x_{22} + x_{31}$)</sub>
- B. $42$  
  <sub>Salah: $X$ dihitung sebagai $A + B$</sub>
- C. $-20$  
  <sub>Salah: urutan terbalik: dihitung $A - B$</sub>
- **D. $20$** ✅  
  <sub>Benar: $X = B - A$ = $\begin{pmatrix} 5 & 3 & -10 \\ -7 & 3 & 3 \\ -1 & -6 & 12 \end{pmatrix}$, diagonal utama: $5 + 3 + 12$</sub>

**Pembahasan:** $X = B - A$ = $\begin{pmatrix} 5 & 3 & -10 \\ -7 & 3 & 3 \\ -1 & -6 & 12 \end{pmatrix}$. Diagonal utama: $5 + 3 + 12 = 20$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b01-c-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim sifat operasi*

Seorang siswa berpendapat bahwa $A - B = B - A$ untuk setiap dua matriks $A$ dan $B$ yang berordo sama, karena penjumlahan matriks bersifat komutatif. Penilaian yang tepat terhadap pendapat tersebut adalah ....

- A. Pendapat itu salah untuk semua pasangan $A$ dan $B$ tanpa kecuali  
  <sub>Salah: mengabaikan kasus $A = B$ yang memenuhi persamaan</sub>
- B. Pendapat itu benar bila $A$ dan $B$ sama-sama matriks persegi  
  <sub>Salah: mengira jenis matriks (persegi) menentukan sifat komutatif pada pengurangan</sub>
- **C. Pendapat itu salah secara umum; $A - B = B - A$ hanya terjadi bila $A = B$** ✅  
  <sub>Benar: $A - B = B - A$ berarti $A - B$ sama dengan lawannya sendiri, sehingga $A - B = O$ dan $A = B$</sub>
- D. Pendapat itu benar, sebab pengurangan didefinisikan sebagai penjumlahan dengan lawan matriks  
  <sub>Salah: sifat komutatif penjumlahan dikira otomatis berlaku pada pengurangan</sub>

**Pembahasan:** Dengan $A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ dan $B = O$, $A - B \neq B - A$. Secara umum, $A - B = B - A$ ekuivalen dengan $A - B = -(A - B)$, sehingga $A - B = O$ dan $A = B$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b01-c-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan penyelesaian*

Seorang siswa menulis $A - (B - C) = A - B - C$ untuk matriks-matriks $A$, $B$, dan $C$ yang berordo sama. Kesalahan siswa tersebut dan bentuk yang benar adalah ....

- **A. Lawan dari $(B - C)$ adalah $-B + C$, sehingga bentuk yang benar adalah $A - B + C$** ✅  
  <sub>Benar: $A - (B - C) = A + (-(B - C)) = A + (-B + C) = A - B + C$</sub>
- B. Tanda $B$ yang keliru, sehingga bentuk yang benar adalah $A + B - C$  
  <sub>Salah: menganggap tanda kurung membalik tanda $B$, bukan tanda $C$</sub>
- C. Tidak ada kesalahan, karena pengurangan matriks bersifat asosiatif  
  <sub>Salah: mengira asosiatif berlaku pada pengurangan</sub>
- D. Dua tanda negatif harus menjadi positif, sehingga bentuk yang benar adalah $A + B + C$  
  <sub>Salah: membalik semua tanda di dalam kurung dan di luar</sub>

**Pembahasan:** Pengurangan adalah penjumlahan dengan lawan: $A - (B - C) = A + (-B + C) = A - B + C$. Siswa lupa membalik tanda $C$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b01-c-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan penyelesaian*

Diketahui $A$ = $\begin{pmatrix} 3 & -1 & 4 \\ 2 & 5 & 0 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 6 & 2 \\ -3 & 7 \end{pmatrix}$. Seorang siswa menjumlahkannya dengan menambahkan kolom nol pada $B$ hingga berordo $2 \times 3$, lalu memperoleh $A + B$ = $\begin{pmatrix} 9 & 1 & 4 \\ -1 & 12 & 0 \end{pmatrix}$. Penilaian yang tepat terhadap penyelesaian siswa tersebut adalah ....

- A. Benar, sebab elemen yang tidak memiliki pasangan dapat dianggap bernilai nol  
  <sub>Salah: menganggap elemen kosong boleh diisi nol tanpa mengubah soal</sub>
- **B. Salah, sebab $A + B$ tidak terdefinisi: ordo $A$ ($2 \times 3$) dan $B$ ($2 \times 2$) berbeda, dan menambah kolom nol mengganti $B$ dengan matriks lain** ✅  
  <sub>Benar: penjumlahan hanya terdefinisi untuk matriks berordo sama; menambah kolom mengubah matriks $B$ menjadi matriks yang berbeda</sub>
- C. Salah, sebab kolom nol seharusnya ditambahkan pada $A$ agar $A + B$ berordo $2 \times 2$  
  <sub>Salah: mengira beda ordo bisa diperbaiki dengan memotong matriks</sub>
- D. Salah, sebab hasil penjumlahan seharusnya berordo $2 \times 2$ mengikuti ordo $B$  
  <sub>Salah: mengira ordo hasil mengikuti matriks yang lebih kecil</sub>

**Pembahasan:** Ordo $A$ adalah $2 \times 3$ dan ordo $B$ adalah $2 \times 2$, sehingga $A + B$ tidak terdefinisi. Menambah kolom nol bukan operasi pada $B$ semula.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b01-c-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: syarat parameter matriks khusus*

Diketahui $A$ = $\begin{pmatrix} 5 & 2p - 1 \\ q + 3 & 7 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & p - 8 \\ q - 11 & 2 \end{pmatrix}$. Jika $A + B$ merupakan matriks diagonal, nilai $p + q$ adalah ....

- A. $-1$  
  <sub>Salah: salah tanda pada $q$: $2q = -8$ sehingga $q = -4$</sub>
- **B. $7$** ✅  
  <sub>Benar: matriks diagonal bila elemen di luar diagonal nol: $(2p - 1) + (p - 8) = 0$ sehingga $p = 3$ dan $(q + 3) + (q - 11) = 0$ sehingga $q = 4$</sub>
- C. $-3$  
  <sub>Salah: salah tanda pada elemen $p$: $(2p - 1) - (p - 8) = 0$ sehingga $p = -7$</sub>
- D. $12$  
  <sub>Salah: yang dihitung adalah hasil kali $p \cdot q$</sub>

**Pembahasan:** $A + B$ = $\begin{pmatrix} 6 & 3p - 9 \\ 2q - 8 & 9 \end{pmatrix}$. Diagonal berarti $3p - 9 = 0$ dan $2q - 8 = 0$, jadi $p = 3$, $q = 4$, $p + q = 7$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b01-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Klaim: "Jika selisih $A - B$ merupakan matriks simetris, maka $A$ dan $B$ keduanya simetris." Pasangan $(A, B)$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- **A. $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ -2 & 0 \end{pmatrix}$** ✅  
  <sub>Benar: $A - B$ = $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$ simetris, tetapi $A$ dan $B$ tidak simetris</sub>
- B. $A$ = $\begin{pmatrix} 2 & 6 \\ 3 & 1 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$  
  <sub>Salah: selisihnya $\begin{pmatrix} 1 & 4 \\ 3 & -2 \end{pmatrix}$ tidak simetris sehingga syarat klaim tidak terpenuhi</sub>
- C. $A$ = $\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 2 \\ 2 & 0 \end{pmatrix}$  
  <sub>Salah: selisihnya $\begin{pmatrix} 2 & 3 \\ -1 & 4 \end{pmatrix}$ tidak simetris sehingga syarat klaim tidak terpenuhi</sub>
- D. $A$ = $\begin{pmatrix} 2 & 1 \\ 1 & 5 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} 1 & 4 \\ 4 & 2 \end{pmatrix}$  
  <sub>Salah: $A$ dan $B$ simetris sehingga mendukung, bukan menyangkal klaim</sub>

**Pembahasan:** Contoh penyangkal harus memenuhi premis ($A - B$ simetris) tetapi menyalahi kesimpulan. Hanya pasangan pertama yang demikian.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b01-c-hard-bt01-006
*orisinal | C6 | 5 langkah | jenis: perancangan matriks yang memenuhi dua persamaan*

Diketahui $A$ = $\begin{pmatrix} 2 & t \\ 5 & 1 \end{pmatrix}$, $B$ = $\begin{pmatrix} 9 & 7 \\ 4 & 6 \end{pmatrix}$, $C$ = $\begin{pmatrix} 3 & t \\ 0 & 2 \end{pmatrix}$, dan $D$ = $\begin{pmatrix} 4 & 1 \\ -1 & 3 \end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ harus memenuhi $X + A = B$ sekaligus $X - C = D$. Nilai $t$ yang memungkinkan adanya matriks $X$ tersebut adalah ....

- A. $4$  
  <sub>Salah: salah tanda pada $D$: $X = C - D$ untuk elemen (1,2) sehingga $7 - t = t - 1$</sub>
- B. $6$  
  <sub>Salah: $7 - t = t + 1$ diselesaikan menjadi $2t = 6$ lalu langsung ditulis $t = 6$ (lupa membagi 2)</sub>
- **C. $3$** ✅  
  <sub>Benar: $X = B - A$ dan $X = C + D$; elemen (1,2): $7 - t = t + 1$ sehingga $t = 3$ (elemen lain sudah cocok)</sub>
- D. $-3$  
  <sub>Salah: salah tanda saat memindahkan suku: $7 - t = t + 1$ dikerjakan menjadi $2t = -6$</sub>

**Pembahasan:** $X = B - A$ = $\begin{pmatrix} 7 & 7 - t \\ -1 & 5 \end{pmatrix}$ dan $X = C + D$ = $\begin{pmatrix} 7 & t + 1 \\ -1 & 5 \end{pmatrix}$. Elemen lain sama; elemen (1,2) memberi $t = 3$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b01-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: perbandingan dua cara penyelesaian*

Diketahui $A$ = $\begin{pmatrix} 8 & -3 \\ 5 & 6 \end{pmatrix}$, $B$ = $\begin{pmatrix} 2 & 4 \\ -1 & 7 \end{pmatrix}$, dan $C$ = $\begin{pmatrix} 5 & -6 \\ 3 & -2 \end{pmatrix}$. Untuk menghitung $A - B - C$, siswa P menghitung $(A - B) + C$ dan siswa Q menghitung $A - (B - C)$. Pernyataan yang benar adalah ....

- A. Hanya siswa Q yang benar, sebab kurung memisahkan $B$ dan $C$, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$  
  <sub>Salah: kurung dikira tidak mengubah tanda $C$</sub>
- B. Keduanya benar karena hasilnya sama, yaitu $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$  
  <sub>Salah: hasil yang sama dikira bukti kebenaran</sub>
- C. Hanya siswa P yang benar, sebab mengerjakan dari kiri ke kanan, hasilnya $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$  
  <sub>Salah: urutan dari kiri dikira menjamin tanda $C$ benar</sub>
- **D. Keduanya salah karena sama-sama menambahkan $C$; hasil yang benar adalah $\begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix}$** ✅  
  <sub>Benar: $(A - B) + C = A - (B - C) = A - B + C$, sedangkan $A - B - C$ memuat $-C$</sub>

**Pembahasan:** $A - B$ = $\begin{pmatrix} 6 & -7 \\ 6 & -1 \end{pmatrix}$. Hasil P: $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$. Hasil Q: $B - C$ = $\begin{pmatrix} -3 & 10 \\ -4 & 9 \end{pmatrix}$ sehingga $A - (B - C)$ = $\begin{pmatrix} 11 & -13 \\ 9 & -3 \end{pmatrix}$. Hasil benar: $\begin{pmatrix} 1 & -1 \\ 3 & 1 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b01-c-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan penyelesaian*

Siswa menghitung $\begin{pmatrix} 4 & -2 \\ -3 & 5 \end{pmatrix}$ - $\begin{pmatrix} 1 & -6 \\ -2 & 3 \end{pmatrix}$ dan menulis hasilnya $\begin{pmatrix} 3 & -8 \\ -5 & 2 \end{pmatrix}$. Pernyataan yang tepat mengenai hasil tersebut adalah ....

- A. Satu elemen salah, yaitu baris 1 kolom 2, karena $-2 - (-6)$ ditulis $-8$  
  <sub>Salah: elemen (2,1) tidak diperiksa; $-3 - (-2)$ seharusnya $-1$, bukan $-5$</sub>
- B. Seluruh elemen salah karena pengurangan matriks harus dikerjakan sebagai $B - A$  
  <sub>Salah: urutan pengurangan terbalik</sub>
- C. Dua elemen salah, yaitu baris 1 kolom 1 dan baris 2 kolom 2, karena seharusnya dijumlahkan  
  <sub>Salah: elemen (1,1) dan (2,2) justru sudah benar: $4 - 1 = 3$ dan $5 - 3 = 2$</sub>
- **D. Dua elemen salah, yaitu baris 1 kolom 2 dan baris 2 kolom 1, karena pengurang yang negatif diperlakukan sebagai bilangan positif** ✅  
  <sub>Benar: elemen (1,2): $-2 - (-6) = 4$; elemen (2,1): $-3 - (-2) = -1$; dua elemen lain sudah benar</sub>

**Pembahasan:** Hasil benar $\begin{pmatrix} 3 & 4 \\ -1 & 2 \end{pmatrix}$. Elemen (1,1) dan (2,2) sudah benar, elemen (1,2) dan (2,1) keliru karena tanda pengurang negatif.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b01-c-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim sifat operasi*

Klaim: "Jika $A + B = O$ (matriks nol), maka $A = O$ dan $B = O$." Pernyataan yang benar mengenai klaim tersebut adalah ....

- **A. Klaim salah; contohnya $A$ = $\begin{pmatrix} 2 & -1 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -2 & 1 \\ -3 & -4 \end{pmatrix}$** ✅  
  <sub>Benar: $B = -A$ memberi $A + B = O$ tanpa $A$ atau $B$ nol; contoh tersebut memenuhi premis dan menyalahi kesimpulan</sub>
- B. Klaim benar bila $A$ dan $B$ berordo $2 \times 2$  
  <sub>Salah: ordo dikira menentukan kebenaran klaim</sub>
- C. Klaim salah; contoh penyangkalnya $A$ = $\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ dan $B$ = $\begin{pmatrix} -1 & 2 \\ -3 & 4 \end{pmatrix}$  
  <sub>Salah: contoh tidak memenuhi premis: $A + B$ = $\begin{pmatrix} 0 & 4 \\ 0 & 8 \end{pmatrix}$ bukan matriks nol</sub>
- D. Klaim benar, sebab jumlah dua matriks hanya nol bila keduanya matriks nol  
  <sub>Salah: mengabaikan lawan matriks</sub>

**Pembahasan:** Jumlah elemen seletak dapat nol bila keduanya berlawanan, mis. $2 + (-2) = 0$. Jadi $B = -A$ memenuhi $A + B = O$ dengan $A \neq O$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b01-c-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: syarat parameter matriks khusus*

Matriks $A$ dan $B$ berordo $2 \times 2$ dengan elemen bilangan real, dan $B$ = $\begin{pmatrix} 2k - 6 & m + k \\ 3k - 9 & 2m + 6 \end{pmatrix}$. Jika $A + B = A - B$, nilai $k - m$ adalah ....

- A. $-6$  
  <sub>Salah: urutan terbalik: yang dihitung $m - k$</sub>
- **B. $6$** ✅  
  <sub>Benar: $A + B = A - B$ berarti $B = -B$, sehingga $B = O$: $2k - 6 = 0$ memberi $k = 3$, $m + k = 0$ memberi $m = -3$ (cocok dengan $2m + 6 = 0$), jadi $k - m = 6$</sub>
- C. $0$  
  <sub>Salah: salah tanda pada $m$: $m + k = 0$ dibaca $m = 3$</sub>
- D. $3$  
  <sub>Salah: yang dilaporkan hanya nilai $k$</sub>

**Pembahasan:** $A + B = A - B \Rightarrow B + B = O \Rightarrow B = O$. Maka $k = 3$ dan $m = -3$ memenuhi semua elemen. $k - m = 6$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b01-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim sifat operasi*

Matriks $A$, $B$, dan $C$ berordo sama. Pernyataan yang benar untuk semua matriks $A$, $B$, $C$ tersebut adalah ....

- A. $(A + B) - C = A - (B + C)$  
  <sub>Salah: ruas kiri $A + B - C$, ruas kanan $A - B - C$; tidak sama kecuali $B = O$</sub>
- B. $(A - B) - C = (A - C) + B$  
  <sub>Salah: ruas kiri $A - B - C$, ruas kanan $A - C + B$; sama hanya bila $B = O$</sub>
- **C. $(A - B) + (B - C) + (C - A) = O$** ✅  
  <sub>Benar: $(A - B) + (B - C) + (C - A) = A - A + B - B + C - C = O$ menurut sifat penjumlahan dan lawan</sub>
- D. $A - O = O - A$  
  <sub>Salah: ruas kiri $A$, ruas kanan $-A$; sama hanya bila $A = O$</sub>

**Pembahasan:** Hanya pernyataan pertama yang berlaku umum; ketiga lainnya gagal untuk $A$, $B$ bukan nol, misalnya $B = I$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b01-c-hard-bt01-012
*orisinal | C6 | 3 langkah | jenis: pencacahan pasangan matriks*

Matriks $A$ dan $B$ berordo $1 \times 2$ dengan semua elemen bilangan cacah ($0, 1, 2, \ldots$) dan $A + B$ = $\begin{pmatrix} 4 & 3 \end{pmatrix}$. Banyak pasangan terurut $(A, B)$ yang mungkin adalah ....

- A. $12$  
  <sub>Salah: nilai nol tidak dihitung: $4 	imes 3$</sub>
- B. $7$  
  <sub>Salah: yang dihitung jumlah elemen $4 + 3$</sub>
- C. $9$  
  <sub>Salah: banyak pasangan kedua elemen dijumlahkan ($5 + 4$), bukan dikalikan</sub>
- **D. $20$** ✅  
  <sub>Benar: elemen pertama: $a + b = 4$ ada 5 pasangan ($a = 0, \ldots, 4$); elemen kedua: $a + b = 3$ ada 4 pasangan; total $5 \times 4 = 20$</sub>

**Pembahasan:** Tiap elemen bebas dipilih terpisah: untuk jumlah 4 ada 5 pilihan, untuk jumlah 3 ada 4 pilihan, sehingga $5 \times 4 = 20$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
