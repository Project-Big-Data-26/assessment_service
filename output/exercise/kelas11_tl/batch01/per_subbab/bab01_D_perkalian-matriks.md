# Lembar koreksi — kelas11_tl SMA11L-B1 subbab D: Perkalian Matriks

58 soal | easy 20, medium 20, hard 18 | variasi 20, orisinal 38
> **Kapasitas kurang (hard): 18 dari kuota 20** — Hard subbab D bermakna hanya lewat penalaran sifat perkalian matriks (klaim, penyangkal, parameter, pangkat, perancangan, pengelompokan). Setelah easy dan medium memakai 40 soal dan acuan siswa/pretest habis, bahan penalaran orisinal yang tidak nyaris kembar hanya cukup untuk sekitar belasan soal, bukan 20.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b01-d-easy-bt01-001
*variasi (konteks) | C2 | 1 langkah | jenis: ordo perkalian skalar*

Matriks $P$ berordo $p \times q$ dan $h$ adalah suatu skalar. Pernyataan yang benar mengenai matriks $hP$ adalah ....

- A. $hP$ berordo $1 \times 1$  
  <sub>Salah: mengira hasil kali dengan skalar adalah satu bilangan</sub>
- B. $hP$ berordo $p \times p$  
  <sub>Salah: mengira ordo mengikuti banyak baris saja</sub>
- **C. $hP$ berordo $p \times q$** ✅  
  <sub>Benar: perkalian skalar mengalikan setiap elemen sehingga banyak baris dan kolom tetap</sub>
- D. $hP$ berordo $q \times p$  
  <sub>Salah: menukar baris dan kolom</sub>

**Pembahasan:** Menurut definisi perkalian skalar, setiap elemen $P$ dikalikan $h$, sehingga ordo $hP$ tetap $p \times q$.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b01-d-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: banyak elemen perkalian skalar*

Matriks $M$ berordo $4 \times 3$ dikalikan dengan skalar $5$ sehingga diperoleh matriks $5M$. Banyak elemen pada matriks $5M$ adalah ....

- A. 7  
  <sub>Salah: menjumlahkan banyak baris dan kolom</sub>
- **B. 12** ✅  
  <sub>Benar: ordo $5M$ tetap $4 \times 3$, banyak elemen $4 \cdot 3 = 12$</sub>
- C. 20  
  <sub>Salah: mengalikan banyak baris dengan skalar</sub>
- D. 60  
  <sub>Salah: mengalikan banyak elemen dengan skalar</sub>

**Pembahasan:** Perkalian skalar tidak mengubah ordo, jadi $5M$ berordo $4 \times 3$ dan memiliki $12$ elemen.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b01-d-easy-bt01-003
*variasi (konteks) | C2 | 1 langkah | jenis: sifat matriks nol*

Diketahui $A$ matriks nol berordo $2 \times 2$ dan $B = \begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$. Hasil perkalian $AB$ adalah ....

- **A. $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$** ✅  
  <sub>Benar: setiap elemen baris matriks nol bernilai 0 sehingga semua jumlah hasil kali bernilai 0</sub>
- B. $\begin{pmatrix}7 & 0 \\ 0 & 9\end{pmatrix}$  
  <sub>Salah: hanya mengalikan elemen diagonal</sub>
- C. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$  
  <sub>Salah: mengira hasil kali dengan matriks nol adalah matriks identitas</sub>
- D. $\begin{pmatrix}7 & -4 \\ 5 & 9\end{pmatrix}$  
  <sub>Salah: mengira matriks nol berperan sebagai identitas</sub>

**Pembahasan:** Setiap elemen $AB$ adalah jumlah hasil kali dengan elemen $A$ yang semuanya $0$, sehingga $AB$ matriks nol berordo $2 \times 2$.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b01-d-easy-bt01-004
*variasi (konteks) | C2 | 1 langkah | jenis: sifat matriks nol*

Misalkan $O$ matriks nol berordo $3 \times 3$ dan $C$ sembarang matriks berordo $3 \times 3$. Pernyataan yang benar adalah ....

- A. $CO = C$  
  <sub>Salah: mengira matriks nol bersifat identitas pada perkalian</sub>
- B. $CO = I$  
  <sub>Salah: mengira hasil kali berupa matriks identitas</sub>
- C. $CO$ tidak terdefinisi  
  <sub>Salah: mengira ordo tidak memenuhi syarat padahal sama-sama $3 	imes 3$</sub>
- **D. $CO = O$** ✅  
  <sub>Benar: semua elemen $CO$ adalah jumlah hasil kali dengan elemen nol</sub>

**Pembahasan:** Karena $C$ dan $O$ sama-sama berordo $3 \times 3$, $CO$ terdefinisi dan setiap elemennya $0$, sehingga $CO = O$.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b01-d-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: matriks idempoten*

Matriks bukan nol berordo $2 \times 2$ berikut yang memenuhi $AA = A$ adalah ....

- A. $\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix}$  
  <sub>Salah: $AA = 4I$, bukan $A$</sub>
- **B. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$** ✅  
  <sub>Benar: $II = I$ sehingga memenuhi sifat</sub>
- C. $\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$  
  <sub>Salah: $AA = I$, bukan $A$</sub>
- D. $\begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix}$  
  <sub>Salah: $AA = I$, bukan $A$</sub>

**Pembahasan:** Hitung kuadratnya: hanya matriks identitas yang memberikan $AA = A$ di antara pilihan ini.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b01-d-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: matriks idempoten*

Diketahui $A = \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$. Pernyataan yang benar adalah ....

- A. $AA = O$  
  <sub>Salah: mengira hasil kuadrat nol karena ada elemen nol</sub>
- B. $AA = 2A$  
  <sub>Salah: menjumlahkan $A + A$ bukan mengalikan</sub>
- **C. $A$ bukan matriks nol dan $AA = A$** ✅  
  <sub>Benar: $AA = \begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix} = A$</sub>
- D. $AA = I$  
  <sub>Salah: mengira hasil kali matriks bernilai identitas</sub>

**Pembahasan:** $AA$ dihitung baris kali kolom dan hasilnya sama dengan $A$.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b01-d-easy-bt01-007
*variasi (konteks) | C2 | 1 langkah | jenis: sifat komutatif*

Pernyataan yang benar tentang perkalian dua matriks $A$ dan $B$ yang berordo $2 \times 2$ adalah ....

- A. $AB = BA$ selalu berlaku jika semua elemen $A$ dan $B$ bukan nol  
  <sub>Salah: mengira syarat elemen tak nol menjamin komutatif</sub>
- **B. Ada pasangan $A$ dan $B$ sehingga $AB \neq BA$** ✅  
  <sub>Benar: perkalian matriks tidak bersifat komutatif secara umum</sub>
- C. $AB$ terdefinisi tetapi $BA$ tidak terdefinisi  
  <sub>Salah: mengira ordo berbeda padahal keduanya persegi sama</sub>
- D. $AB = BA$ berlaku untuk setiap pasangan $A$ dan $B$  
  <sub>Salah: mengira perkalian matriks komutatif seperti perkalian bilangan</sub>

**Pembahasan:** Contoh $A = \begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$, $B = \begin{pmatrix}1 & 0 \\ 1 & 1\end{pmatrix}$ memberi $AB \neq BA$.
**Acuan:** siswa — siswa hal.40 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b01-d-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: aplikasi perkalian baris-kolom*

Sebuah bengkel memiliki $6$ montir tetap dan $4$ montir paruh waktu. Gaji per hari montir tetap Rp150.000,00 dan montir paruh waktu Rp90.000,00. Gaji dalam ribu rupiah dinyatakan oleh matriks $\begin{pmatrix}6 & 4\end{pmatrix}\begin{pmatrix}150 \\ 90\end{pmatrix}$. Total gaji yang harus dibayar bengkel per hari adalah ....

- A. Rp1.140.000,00  
  <sub>Salah: menukar banyak montir: $4 \cdot 150 + 6 \cdot 90$</sub>
- B. Rp126.000,00  
  <sub>Salah: salah satuan ribu rupiah</sub>
- C. Rp240.000,00  
  <sub>Salah: hanya menjumlahkan kedua gaji tanpa mengalikan banyak montir</sub>
- **D. Rp1.260.000,00** ✅  
  <sub>Benar: $6 \cdot 150 + 4 \cdot 90 = 900 + 360 = 1260$ ribu rupiah</sub>

**Pembahasan:** Hasil kali $\begin{pmatrix}6 & 4\end{pmatrix}\begin{pmatrix}150 \\ 90\end{pmatrix} = (1260)$ dalam ribu rupiah, yaitu Rp1.260.000,00.
**Acuan:** siswa — siswa hal.38 Eksplorasi Perkalian Dua Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b01-d-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: aplikasi perkalian baris-kolom*

Dua cabang usaha memiliki karyawan tetap dan karyawan paruh waktu yang dinyatakan oleh matriks $A = \begin{pmatrix}300 & 90 \\ 260 & 110\end{pmatrix}$ (baris: cabang I dan II; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}175 \\ 60\end{pmatrix}$. Dana gaji per hari untuk cabang II adalah ....

- A. Rp57.900.000,00  
  <sub>Salah: mengambil baris pertama (cabang I)</sub>
- B. Rp5.210.000,00  
  <sub>Salah: salah satuan, kurang satu nol</sub>
- C. Rp34.850.000,00  
  <sub>Salah: menukar gaji tetap dan paruh waktu</sub>
- **D. Rp52.100.000,00** ✅  
  <sub>Benar: baris 2: $260 \cdot 175 + 110 \cdot 60 = 45500 + 6600 = 52100$ ribu</sub>

**Pembahasan:** Elemen baris 2 hasil $AB$ adalah 52100 ribu rupiah.
**Acuan:** siswa — siswa hal.38 Eksplorasi Perkalian Dua Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b01-d-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: aplikasi perkalian baris-kolom*

Sebuah toko roti menjual roti tawar, roti manis, dan roti keju. Banyak roti yang terjual dinyatakan oleh $\begin{pmatrix}14 & 9 & 11\end{pmatrix}$ dan harga per buah (ribu rupiah) oleh $\begin{pmatrix}25 \\ 35 \\ 18\end{pmatrix}$. Pendapatan toko jika semua roti terjual adalah ....

- A. Rp86.300,00  
  <sub>Salah: salah satuan ribu rupiah</sub>
- B. Rp913.000,00  
  <sub>Salah: menukar harga roti tawar dan roti manis</sub>
- **C. Rp863.000,00** ✅  
  <sub>Benar: $14 \cdot 25 + 9 \cdot 35 + 11 \cdot 18 = 350 + 315 + 198 = 863$ ribu</sub>
- D. Rp2.652.000,00  
  <sub>Salah: menjumlahkan semua banyak lalu mengalikannya dengan jumlah semua harga</sub>

**Pembahasan:** Pendapatan = 863 ribu rupiah = Rp863.000,00.
**Acuan:** siswa — siswa hal.42 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b01-d-easy-bt01-011
*variasi (angka) | C2 | 1 langkah | jenis: aplikasi perkalian skalar*

Matriks tabungan tiga anggota koperasi (dalam rupiah) adalah $\begin{pmatrix}1500000 \\ 2800000 \\ 5000000\end{pmatrix}$. Jika suku bunga tunggal $8\%$ per tahun, matriks besarnya bunga setelah satu tahun (dalam rupiah) adalah ....

- A. $\begin{pmatrix}1580000 \\ 2880000 \\ 5080000\end{pmatrix}$  
  <sub>Salah: menambahkan bunga tetap pada setiap tabungan</sub>
- B. $\begin{pmatrix}12000 \\ 22400 \\ 40000\end{pmatrix}$  
  <sub>Salah: memakai skalar $0{,}008$ (salah menggeser koma)</sub>
- **C. $\begin{pmatrix}120000 \\ 224000 \\ 400000\end{pmatrix}$** ✅  
  <sub>Benar: $0{,}08 \times \begin{pmatrix}1500000 \\ 2800000 \\ 5000000\end{pmatrix}$</sub>
- D. $\begin{pmatrix}1200000 \\ 2240000 \\ 4000000\end{pmatrix}$  
  <sub>Salah: memakai $0{,}8$ sebagai skalar</sub>

**Pembahasan:** Kalikan setiap elemen dengan $0{,}08$.
**Acuan:** siswa — siswa hal.41 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b01-d-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: ordo hasil perkalian*

Matriks $A$ berordo $3 \times 2$ dan matriks $B$ berordo $2 \times 5$. Ordo matriks $AB$ adalah ....

- **A. $3 \times 5$** ✅  
  <sub>Benar: ordo hasil adalah baris $A$ kali kolom $B$</sub>
- B. $2 \times 2$  
  <sub>Salah: mengambil ordo bagian dalam</sub>
- C. $3 \times 2$  
  <sub>Salah: mengambil ordo $A$ saja</sub>
- D. $5 \times 3$  
  <sub>Salah: menukar baris dan kolom</sub>

**Pembahasan:** $A$ berordo $3 \times 2$, $B$ berordo $2 \times 5$, kolom $A$ = baris $B$ = 2, sehingga $AB$ berordo $3 \times 5$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b01-d-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: syarat perkalian*

Matriks $P$ berordo $2 \times 3$. Agar hasil kali $PQ$ terdefinisi, ordo matriks $Q$ yang mungkin adalah ....

- A. $2 \times 2$  
  <sub>Salah: banyak baris $Q$ 2, tidak sama dengan kolom $P$</sub>
- B. $4 \times 3$  
  <sub>Salah: menukar baris dan kolom ordo yang benar</sub>
- **C. $3 \times 4$** ✅  
  <sub>Benar: banyak baris $Q$ harus sama dengan banyak kolom $P$, yaitu 3</sub>
- D. $2 \times 3$  
  <sub>Salah: banyak baris $Q$ disamakan dengan banyak baris $P$</sub>

**Pembahasan:** Syarat: kolom $P$ = baris $Q$ = 3, sehingga ordo $Q$ adalah $3 \times k$, yaitu $3 \times 4$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b01-d-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: syarat perkalian*

Matriks $A$ berordo $4 \times 2$ dan matriks $B$ berordo $3 \times 4$. Pernyataan yang benar adalah ....

- **A. $BA$ terdefinisi dan berordo $3 \times 2$** ✅  
  <sub>Benar: kolom $B$ = 4 = baris $A$</sub>
- B. $BA$ terdefinisi dan berordo $4 \times 3$  
  <sub>Salah: menukar ordo hasil</sub>
- C. $AB$ terdefinisi dan berordo $4 \times 3$  
  <sub>Salah: kolom $A$ (2) tidak sama dengan baris $B$ (3)</sub>
- D. $BA$ tidak terdefinisi  
  <sub>Salah: salah memeriksa syarat</sub>

**Pembahasan:** Kolom $B$ = 4 sama dengan baris $A$ = 4 sehingga $BA$ terdefinisi berordo $3 \times 2$; $AB$ tidak terdefinisi karena $2 \neq 3$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b01-d-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: menghitung satu elemen hasil*

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 0 \\ -2 & 6\end{pmatrix}$. Elemen baris ke-2 kolom ke-1 pada $AB$ adalah ....

- A. 24  
  <sub>Salah: mengambil elemen baris ke-2 kolom ke-2</sub>
- B. 23  
  <sub>Salah: salah tanda pada $4 \cdot (-2)$</sub>
- C. 12  
  <sub>Salah: mengambil elemen baris ke-1 kolom ke-1</sub>
- **D. 7** ✅  
  <sub>Benar: $3 \cdot 5 + 4 \cdot (-2) = 15 - 8 = 7$</sub>

**Pembahasan:** $c_{21} = 3 \cdot 5 + 4 \cdot (-2) = 7$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b01-d-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: hitung perkalian skalar*

Diketahui $A = \begin{pmatrix}4 & -2 \\ 1 & 6\end{pmatrix}$. Matriks $-3A$ adalah ....

- **A. $\begin{pmatrix}-12 & 6 \\ -3 & -18\end{pmatrix}$** ✅  
  <sub>Benar: setiap elemen dikalikan $-3$</sub>
- B. $\begin{pmatrix}1 & -5 \\ -2 & 3\end{pmatrix}$  
  <sub>Salah: mengurangkan 3 dari setiap elemen</sub>
- C. $\begin{pmatrix}12 & -6 \\ 3 & 18\end{pmatrix}$  
  <sub>Salah: lupa tanda negatif</sub>
- D. $\begin{pmatrix}-12 & -2 \\ -3 & -18\end{pmatrix}$  
  <sub>Salah: tanda negatif hanya pada sebagian elemen</sub>

**Pembahasan:** $-3A$ diperoleh dengan mengalikan semua elemen $A$ dengan $-3$.
**Acuan:** siswa — siswa hal.36

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b01-d-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: sifat asosiatif skalar*

Diketahui $A = \begin{pmatrix}1 & -2 \\ 4 & 3\end{pmatrix}$. Matriks $2(3A)$ adalah ....

- A. $\begin{pmatrix}8 & -16 \\ 32 & 24\end{pmatrix}$  
  <sub>Salah: memangkatkan $2^3$</sub>
- **B. $\begin{pmatrix}6 & -12 \\ 24 & 18\end{pmatrix}$** ✅  
  <sub>Benar: $2(3A) = 6A$</sub>
- C. $\begin{pmatrix}5 & -10 \\ 20 & 15\end{pmatrix}$  
  <sub>Salah: menjumlahkan skalar $2+3$</sub>
- D. $\begin{pmatrix}6 & -2 \\ 4 & 3\end{pmatrix}$  
  <sub>Salah: hanya elemen pertama yang dikalikan</sub>

**Pembahasan:** $2(3A) = (2 \cdot 3)A = 6A$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b01-d-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: hitung perkalian dua matriks*

Diketahui $A = \begin{pmatrix}2 & 1 \\ -1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -2 \\ 0 & 5\end{pmatrix}$. Matriks $AB$ adalah ....

- **A. $\begin{pmatrix}8 & 1 \\ -4 & 17\end{pmatrix}$** ✅  
  <sub>Benar: baris kali kolom untuk keempat elemen</sub>
- B. $\begin{pmatrix}10 & -2 \\ -5 & 15\end{pmatrix}$  
  <sub>Salah: mengalikan dengan urutan terbalik ($BA$)</sub>
- C. $\begin{pmatrix}8 & -2 \\ 0 & 15\end{pmatrix}$  
  <sub>Salah: mengalikan elemen seletak</sub>
- D. $\begin{pmatrix}8 & 9 \\ -4 & 13\end{pmatrix}$  
  <sub>Salah: salah tanda pada hasil kali dengan $-2$</sub>

**Pembahasan:** $AB$ dihitung baris kali kolom.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b01-d-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: sifat identitas*

Diketahui $A = \begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $AI$ adalah ....

- A. $\begin{pmatrix}2 & 0 \\ 0 & 7\end{pmatrix}$  
  <sub>Salah: hanya mengalikan elemen diagonal</sub>
- **B. $\begin{pmatrix}2 & -3 \\ 5 & 7\end{pmatrix}$** ✅  
  <sub>Benar: $AI = A$</sub>
- C. $\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$  
  <sub>Salah: mengira hasil selalu $I$</sub>
- D. $\begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix}$  
  <sub>Salah: mengira hasil matriks nol</sub>

**Pembahasan:** Sifat identitas: $AI = IA = A$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b01-d-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: perkalian dengan skalar nol*

Matriks $A$ berordo $3 \times 2$. Hasil $0 \cdot A$ adalah ....

- A. Matriks $A$ sendiri  
  <sub>Salah: mengira skalar nol tidak mengubah apa pun</sub>
- B. Bilangan $0$  
  <sub>Salah: mengira hasilnya bilangan, bukan matriks</sub>
- C. Matriks nol berordo $2 \times 3$  
  <sub>Salah: menukar ordo</sub>
- **D. Matriks nol berordo $3 \times 2$** ✅  
  <sub>Benar: semua elemen menjadi 0 dan ordo tetap</sub>

**Pembahasan:** $kA = O$ untuk $k = 0$ dengan ordo sama dengan $A$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b01-d-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: persamaan matriks aljabar skalar*

Diketahui $P = \begin{pmatrix}50 & 21 \\ 12 & 63\end{pmatrix}$ dan $Q = \begin{pmatrix}6 & 9 \\ -4 & 7\end{pmatrix}$. Matriks $X$ berordo $2 \times 2$ yang memenuhi $P - 4X = 5Q$ adalah ....

- A. $\begin{pmatrix}11 & 3 \\ 4 & 14\end{pmatrix}$  
  <sub>Salah: lupa mengalikan $Q$ dengan 5</sub>
- B. $\begin{pmatrix}-20 & 24 \\ -32 & -28\end{pmatrix}$  
  <sub>Salah: salah memindahkan ruas sehingga tanda $X$ terbalik</sub>
- C. $\begin{pmatrix}20 & -24 \\ 32 & 28\end{pmatrix}$  
  <sub>Salah: lupa membagi dengan 4 setelah $P - 5Q$</sub>
- **D. $\begin{pmatrix}5 & -6 \\ 8 & 7\end{pmatrix}$** ✅  
  <sub>Benar: $X = \frac{1}{4}(P - 5Q)$ dihitung per elemen</sub>

**Pembahasan:** $4X = P - 5Q = \begin{pmatrix}20 & -24 \\ 32 & 28\end{pmatrix}$, sehingga $X = \frac{1}{4}(P - 5Q) = \begin{pmatrix}5 & -6 \\ 8 & 7\end{pmatrix}$.
**Acuan:** pretest — kelas11_tl-b01-p0041-latihan-d-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b01-d-medium-bt01-002
*variasi (angka) | C3 | 4 langkah | jenis: persamaan matriks aljabar skalar*

Diketahui $A = \begin{pmatrix}17 & -11 & -9 \\ 25 & 18 & -35\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -3 & 8 \\ -5 & 4 & 5\end{pmatrix}$. Jika $X$ memenuhi $5X - A = 3B$, jumlah semua elemen matriks $X$ adalah ....

- A. 4  
  <sub>Salah: lupa mengalikan $B$ dengan 3</sub>
- B. -8  
  <sub>Salah: salah memindahkan $A$ sehingga memakai $A - 3B$</sub>
- C. 50  
  <sub>Salah: lupa membagi dengan 5 setelah $A + 3B$</sub>
- **D. 10** ✅  
  <sub>Benar: $X = \frac{1}{5}(A + 3B)$, kemudian semua elemennya dijumlahkan</sub>

**Pembahasan:** $X = \frac{1}{5}(A + 3B) = \begin{pmatrix}7 & -4 & 3 \\ 2 & 6 & -4\end{pmatrix}$. Jumlah elemennya $7 - 4 + 3 + 2 + 6 - 4 = 10$.
**Acuan:** pretest — kelas11_tl-b01-p0041-latihan-d-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b01-d-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: kesamaan matriks hasil kali*

Diketahui $egin{pmatrix}x+5 & 7 \ 6 & -8\end{pmatrix}egin{pmatrix}8 & 0 \ 5 & y-6\end{pmatrix} = egin{pmatrix}35 & 14 \ 8 & -16\end{pmatrix}$. Nilai $x - 2y$ adalah ....

- **A. -21** ✅  
  <sub>Benar: elemen (1,1): $8x + 75 = 35$ sehingga $x = -5$; elemen (1,2): $7y - 42 = 14$ sehingga $y = 8$</sub>
- B. -11  
  <sub>Salah: salah tanda saat menyelesaikan $8x + 75 = 35$ sehingga $x = 5$</sub>
- C. -56  
  <sub>Salah: tidak membagi dengan 8 pada $8x = -40$ sehingga $x = -40$</sub>
- D. 3  
  <sub>Salah: salah memindahkan $-42$ pada $7y - 42 = 14$ sehingga $y = -4$</sub>

**Pembahasan:** Elemen baris 1 kolom 1: $8(x+5) + 7 \cdot 5 = 8x + 75 = 35$, sehingga $x = -5$. Elemen baris 1 kolom 2: $7(y-6) = 14$, sehingga $y = 8$. Elemen (2,2): $-8(y-6) = -16$ cocok. Jadi $x - 2y = -5 - 16 = -21$.
**Acuan:** pretest — kelas11_tl-b01-p0041-latihan-d-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b01-d-medium-bt01-004
*variasi (angka) | C3 | 4 langkah | jenis: kesamaan matriks hasil kali*

Diketahui $egin{pmatrix}7 & x \ 6 & 5\end{pmatrix}egin{pmatrix}y & 8 \ -5 & 11\end{pmatrix} = egin{pmatrix}79 & -10 \ 17 & 103\end{pmatrix}$. Nilai $2x - y$ adalah ....

- **A. -19** ✅  
  <sub>Benar: elemen (1,2): $56 + 11x = -10$ sehingga $x = -6$; elemen (2,1): $6y - 25 = 17$ sehingga $y = 7$</sub>
- B. -15  
  <sub>Salah: salah hitung $-10 - 56$ sehingga $x = -4$</sub>
- C. -5  
  <sub>Salah: salah tanda pada $x$ dan $y$</sub>
- D. 5  
  <sub>Salah: salah tanda pada $x$: dari $56 + 11x = -10$ diambil $x = 6$</sub>

**Pembahasan:** Elemen baris 1 kolom 2: $7 \cdot 8 + 11x = 56 + 11x = -10$, sehingga $x = -6$. Elemen baris 2 kolom 1: $6y + 5(-5) = 6y - 25 = 17$, sehingga $y = 7$. Elemen (1,1): $7y - 5x = 49 + 30 = 79$ cocok. Jadi $2x - y = -12 - 7 = -19$.
**Acuan:** pretest — kelas11_tl-b01-p0041-latihan-d-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b01-d-medium-bt01-005
*variasi (konteks) | C4 | 3 langkah | jenis: aplikasi harga kali jumlah*

Sebuah usaha rumahan membuat sabun, lilin, dan dupa yang dikirim ke Toko X, Toko Y, dan Toko Z. Banyak barang (lusin) dinyatakan oleh matriks $P = \begin{pmatrix}17 & 13 & 21 \\ 24 & 19 & 11 \\ 14 & 26 & 18\end{pmatrix}$, dengan baris berturut-turut sabun, lilin, dan dupa, serta kolom berturut-turut Toko X, Toko Y, dan Toko Z. Harga per lusin (ribu rupiah) untuk sabun, lilin, dan dupa berturut-turut adalah 9, 14, dan 7. Pendapatan usaha tersebut dari Toko Y jika semua barang terjual adalah ....

- A. Rp56.500,00  
  <sub>Salah: salah satuan: kurang satu nol</sub>
- **B. Rp565.000,00** ✅  
  <sub>Benar: $13 \cdot 9 + 19 \cdot 14 + 26 \cdot 7 = 117 + 266 + 182 = 565$ ribu rupiah</sub>
- C. Rp559.000,00  
  <sub>Salah: memakai baris ke-2 (produk kedua) padahal kolom menunjukkan tempat</sub>
- D. Rp1.740.000,00  
  <sub>Salah: menjumlahkan semua banyak produk di Toko Y lalu mengalikan dengan jumlah semua harga</sub>

**Pembahasan:** Toko Y ada pada kolom ke-2, yaitu 13, 19, 26 lusin. Pendapatan = $13 \cdot 9 + 19 \cdot 14 + 26 \cdot 7 = 565$ ribu rupiah = Rp565.000,00.
**Acuan:** siswa — siswa hal.40 Mari Berpikir Kritis keripik

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b01-d-medium-bt01-006
*variasi (konteks) | C4 | 4 langkah | jenis: aplikasi harga kali jumlah*

Sebuah peternakan memasok telur, susu, dan madu ke Toko I dan Toko II. Banyak barang (kemasan) dinyatakan oleh matriks $P = \begin{pmatrix}30 & 25 \\ 18 & 40 \\ 12 & 16\end{pmatrix}$ dengan baris berturut-turut telur, susu, dan madu, serta kolom berturut-turut Toko I dan Toko II. Harga per kemasan (ribu rupiah) untuk telur, susu, dan madu berturut-turut adalah 22, 15, dan 60. Matriks baris pendapatan (dalam ribu rupiah) untuk Toko I dan Toko II berturut-turut adalah ....

- **A. $\begin{pmatrix}1650 & 2110\end{pmatrix}$** ✅  
  <sub>Benar: Toko I: $30 \cdot 22 + 18 \cdot 15 + 12 \cdot 60 = 1650$; Toko II: $25 \cdot 22 + 40 \cdot 15 + 16 \cdot 60 = 2110$</sub>
- B. $\begin{pmatrix}2110 & 1650\end{pmatrix}$  
  <sub>Salah: menukar Toko I dan Toko II</sub>
- C. $\begin{pmatrix}1566 & 2215\end{pmatrix}$  
  <sub>Salah: menukar harga telur dan susu</sub>
- D. $\begin{pmatrix}2334 & 2452\end{pmatrix}$  
  <sub>Salah: menukar harga telur dan madu</sub>

**Pembahasan:** Hasil kali baris $P$ dengan harga tidak sesuai karena baris $P$ menunjukkan jenis barang. Pendapatan tiap toko = kolom $P$ dikalikan harga: Toko I $= 660 + 270 + 720 = 1650$, Toko II $= 550 + 600 + 960 = 2110$.
**Acuan:** siswa — siswa hal.40 Mari Berpikir Kritis keripik

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b01-d-medium-bt01-007
*variasi (konteks) | C3 | 3 langkah | jenis: aplikasi harga kali jumlah*

Toko oleh-oleh memiliki dua cabang, yaitu Bandung dan Malang. Banyak stoples bakpia, keripik, dan dodol yang tersedia dinyatakan oleh $A = \begin{pmatrix}24 & 31 & 18 \\ 29 & 22 & 35\end{pmatrix}$ (baris: Bandung dan Malang; kolom: bakpia, keripik, dodol). Harga normal per stoples (ribu rupiah) berturut-turut adalah 45, 38, dan 52. Jika semua harga diberi potongan 20% dan semua stoples terjual, pendapatan cabang Malang adalah ....

- A. Rp3.961.000,00  
  <sub>Salah: lupa memperhitungkan potongan harga 20%</sub>
- B. Rp2.555.200,00  
  <sub>Salah: memakai baris pertama (Bandung) padahal yang ditanya Malang</sub>
- C. Rp792.200,00  
  <sub>Salah: memakai 20% sebagai pengali (hanya potongannya), bukan sisa 80%</sub>
- **D. Rp3.168.800,00** ✅  
  <sub>Benar: $0{,}8 \times (29 \cdot 45 + 22 \cdot 38 + 35 \cdot 52) = 0{,}8 \times 3961$ ribu rupiah</sub>

**Pembahasan:** Pendapatan Malang tanpa potongan: $29 \cdot 45 + 22 \cdot 38 + 35 \cdot 52 = 1305 + 836 + 1820 = 3961$ ribu rupiah. Setelah potongan 20%, pendapatan $= 0{,}8 \times 3961 = 3168{,}8$ ribu rupiah $=$ Rp3.168.800,00.
**Acuan:** siswa — siswa hal.42 Latihan D

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b01-d-medium-bt01-008
*variasi (konteks) | C4 | 3 langkah | jenis: sifat komutatif dengan bukti numerik*

Diketahui $A = \begin{pmatrix}3 & 1 \\ -2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 5 \\ 1 & -3\end{pmatrix}$. Pernyataan yang benar mengenai $AB$ dan $BA$ adalah ....

- **A. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $7$ sedangkan pada $BA$ adalah $-4$** ✅  
  <sub>Benar: elemen (1,1) $AB$ adalah $3 \cdot 2 + 1 \cdot 1 = 7$ dan elemen (1,1) $BA$ adalah $2 \cdot 3 + 5(-2) = -4$</sub>
- B. $AB = BA$, sebab elemen baris 1 kolom 1 keduanya bernilai $7$  
  <sub>Salah: mengira perkalian matriks komutatif</sub>
- C. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $-4$ sedangkan pada $BA$ adalah $7$  
  <sub>Salah: menukar hasil $AB$ dan $BA$</sub>
- D. $AB \neq BA$, sebab elemen baris 1 kolom 1 pada $AB$ adalah $6$ sedangkan pada $BA$ adalah $-4$  
  <sub>Salah: hanya mengalikan elemen seletak pada $AB$ dan salah menghitung $BA$</sub>

**Pembahasan:** $AB = \begin{pmatrix}7 & 12 \\ 0 & -22\end{pmatrix}$ dan $BA = \begin{pmatrix}-4 & 22 \\ 9 & -11\end{pmatrix}$. Kedua matriks berbeda sehingga perkalian matriks tidak komutatif.
**Acuan:** siswa — siswa hal.40 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b01-d-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: aplikasi harga kali jumlah*

Sebuah perusahaan memiliki tiga lokasi. Banyak karyawan tetap dan paruh waktu dinyatakan oleh $A = \begin{pmatrix}40 & 25 \\ 55 & 30 \\ 35 & 45\end{pmatrix}$ (baris: lokasi 1, 2, 3; kolom: tetap dan paruh waktu). Gaji per hari (ribu rupiah) dinyatakan oleh $B = \begin{pmatrix}210 \\ 95\end{pmatrix}$ (baris: tetap dan paruh waktu). Selisih dana gaji per hari antara lokasi 2 dan lokasi 3 adalah ....

- A. Rp3.625.000,00  
  <sub>Salah: membandingkan lokasi 1 dan lokasi 2, bukan lokasi 2 dan lokasi 3</sub>
- **B. Rp2.775.000,00** ✅  
  <sub>Benar: $AB$ baris 2 $= 55 \cdot 210 + 30 \cdot 95 = 14400$ dan baris 3 $= 35 \cdot 210 + 45 \cdot 95 = 11625$; selisih $2775$ ribu</sub>
- C. Rp1.250.000,00  
  <sub>Salah: menukar gaji karyawan tetap dan paruh waktu</sub>
- D. Rp277.500,00  
  <sub>Salah: salah satuan: kurang satu nol</sub>

**Pembahasan:** Elemen $AB$: lokasi 2 $= 11550 + 2850 = 14400$ ribu; lokasi 3 $= 7350 + 4275 = 11625$ ribu. Selisih $= 2775$ ribu rupiah $=$ Rp2.775.000,00.
**Acuan:** siswa — siswa hal.38 Eksplorasi Perkalian Dua Matriks

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b01-d-medium-bt01-010
*orisinal | C3 | 4 langkah | jenis: hitung perkalian dua matriks*

Diketahui $A = \begin{pmatrix}3 & -1 & 2 \\ 0 & 4 & -2\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ -3 & 2 \\ 4 & -1\end{pmatrix}$. Matriks $AB$ adalah ....

- A. $\begin{pmatrix}8 & 11 \\ -20 & 10\end{pmatrix}$  
  <sub>Salah: salah tanda pada hasil kali $(-1)(-3)$</sub>
- B. $\begin{pmatrix}14 & -20 \\ 11 & 10\end{pmatrix}$  
  <sub>Salah: menukar baris dan kolom hasil (hasil transpos)</sub>
- **C. $\begin{pmatrix}14 & 11 \\ -20 & 10\end{pmatrix}$** ✅  
  <sub>Benar: baris $A$ dikalikan kolom $B$, tiga suku dijumlahkan untuk tiap elemen</sub>
- D. $\begin{pmatrix}3 & 19 & -8 \\ -9 & 11 & -10 \\ 12 & -8 & 10\end{pmatrix}$  
  <sub>Salah: mengalikan dengan urutan terbalik ($BA$) sehingga ordo hasil $3 \times 3$</sub>

**Pembahasan:** $A$ berordo $2 \times 3$ dan $B$ berordo $3 \times 2$ sehingga $AB$ berordo $2 \times 2$: $AB = \begin{pmatrix}14 & 11 \\ -20 & 10\end{pmatrix}$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b01-d-medium-bt01-011
*orisinal | C3 | 4 langkah | jenis: hasil perkalian ordo tak sama*

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4 \\ -2 & 5\end{pmatrix}$ dan $B = \begin{pmatrix}2 & 3 & -2 \\ 4 & -1 & 2\end{pmatrix}$. Jumlah elemen pada diagonal utama matriks $AB$ adalah ....

- A. 15  
  <sub>Salah: menjumlahkan diagonal samping, bukan diagonal utama</sub>
- B. -1  
  <sub>Salah: salah tanda pada hasil kali $5 \cdot 2$ di elemen baris 3 kolom 3</sub>
- **C. 19** ✅  
  <sub>Benar: $AB$ berordo $3 \times 3$; hitung $c_{11}$, $c_{22}$, dan $c_{33}$ lalu jumlahkan</sub>
- D. 49  
  <sub>Salah: menjumlahkan semua elemen $AB$</sub>

**Pembahasan:** $AB = \begin{pmatrix}0 & 7 & -6 \\ 22 & 5 & 2 \\ 16 & -11 & 14\end{pmatrix}$. Diagonal utama: $0$, $5$, $14$ sehingga jumlahnya $19$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b01-d-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: pangkat matriks*

Diketahui $A = \begin{pmatrix}3 & -2 \\ 1 & 4\end{pmatrix}$. Matriks $A^2$ adalah ....

- A. $\begin{pmatrix}6 & -4 \\ 2 & 8\end{pmatrix}$  
  <sub>Salah: mengira $A^2 = 2A$</sub>
- B. $\begin{pmatrix}9 & 4 \\ 1 & 16\end{pmatrix}$  
  <sub>Salah: mengkuadratkan setiap elemen</sub>
- C. $\begin{pmatrix}7 & 2 \\ 7 & 14\end{pmatrix}$  
  <sub>Salah: salah tanda pada hasil kali baris 1 dengan kolom 2</sub>
- **D. $\begin{pmatrix}7 & -14 \\ 7 & 14\end{pmatrix}$** ✅  
  <sub>Benar: $A^2 = AA$ dihitung dengan baris kali kolom</sub>

**Pembahasan:** $A^2 = AA = \begin{pmatrix}7 & -14 \\ 7 & 14\end{pmatrix}$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b01-d-medium-bt01-013
*orisinal | C3 | 4 langkah | jenis: bentuk polinom matriks*

Diketahui $A = \begin{pmatrix}2 & 1 \\ -3 & 4\end{pmatrix}$ dan $I$ matriks identitas berordo $2 \times 2$. Matriks $A^2 - 2A + 3I$ adalah ....

- A. $\begin{pmatrix}-3 & 4 \\ -12 & 5\end{pmatrix}$  
  <sub>Salah: lupa menambahkan $3I$</sub>
- **B. $\begin{pmatrix}0 & 4 \\ -12 & 8\end{pmatrix}$** ✅  
  <sub>Benar: hitung $A^2$, $2A$, dan $3I$ lalu jumlahkan per elemen</sub>
- C. $\begin{pmatrix}0 & 7 \\ -9 & 8\end{pmatrix}$  
  <sub>Salah: menambahkan 3 pada semua elemen, bukan hanya pada diagonal utama ($3I$)</sub>
- D. $\begin{pmatrix}3 & -1 \\ 15 & 11\end{pmatrix}$  
  <sub>Salah: mengkuadratkan setiap elemen untuk memperoleh $A^2$</sub>

**Pembahasan:** $A^2 = \begin{pmatrix}1 & 6 \\ -18 & 13\end{pmatrix}$, $2A = \begin{pmatrix}4 & 2 \\ -6 & 8\end{pmatrix}$, $3I = \begin{pmatrix}3 & 0 \\ 0 & 3\end{pmatrix}$. Hasil: $\begin{pmatrix}0 & 4 \\ -12 & 8\end{pmatrix}$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b01-d-medium-bt01-014
*orisinal | C3 | 4 langkah | jenis: perkalian tiga matriks*

Diketahui $A = \begin{pmatrix}1 & 2 \\ 3 & -1\end{pmatrix}$, $B = \begin{pmatrix}2 & 0 \\ -1 & 3\end{pmatrix}$, dan $C = \begin{pmatrix}4 \\ -2\end{pmatrix}$. Matriks $ABC$ adalah ....

- **A. $\begin{pmatrix}-12 \\ 34\end{pmatrix}$** ✅  
  <sub>Benar: $ABC = A(BC)$ dengan urutan perkalian tetap</sub>
- B. $\begin{pmatrix}12 \\ 22\end{pmatrix}$  
  <sub>Salah: salah menghitung $BC$ pada baris kedua: $-4 + 6$ dianggap $2$</sub>
- C. $\begin{pmatrix}0 \\ 42\end{pmatrix}$  
  <sub>Salah: mengalikan dengan urutan $BAC$ (perkalian matriks tidak komutatif)</sub>
- D. $\begin{pmatrix}8 \\ -10\end{pmatrix}$  
  <sub>Salah: hanya menghitung $BC$ dan lupa mengalikan dengan $A$</sub>

**Pembahasan:** $BC = \begin{pmatrix}8 \\ -10\end{pmatrix}$, kemudian $A(BC) = \begin{pmatrix}-12 \\ 34\end{pmatrix}$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b01-d-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: persamaan matriks AX=B*

Diketahui $\begin{pmatrix}2 & 3 \\ 1 & -4\end{pmatrix}\begin{pmatrix}p \\ q\end{pmatrix} = \begin{pmatrix}1 \\ 17\end{pmatrix}$. Nilai $3p - q$ adalah ....

- A. -14  
  <sub>Salah: menukar nilai $p$ dan $q$</sub>
- B. 12  
  <sub>Salah: salah tanda pada $q$ (diambil $q = 3$)</sub>
- **C. 18** ✅  
  <sub>Benar: $2p + 3q = 1$ dan $p - 4q = 17$ memberi $p = 5$ dan $q = -3$</sub>
- D. -18  
  <sub>Salah: salah tanda pada seluruh bentuk $3p - q$</sub>

**Pembahasan:** Perkalian matriks memberi $2p + 3q = 1$ dan $p - 4q = 17$. Dari persamaan kedua $p = 17 + 4q$, sehingga $34 + 8q + 3q = 1$, $q = -3$, $p = 5$. Jadi $3p - q = 15 + 3 = 18$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b01-d-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: syarat ordo dua urutan perkalian*

Matriks $A$ berordo $2 \times 3$ dan matriks $B$ berordo $(x+1) \times (y-2)$. Jika $AB$ dan $BA$ sama-sama terdefinisi, nilai $2x + y$ adalah ....

- A. 7  
  <sub>Salah: menukar syarat: $x + 1 = 2$ dan $y - 2 = 3$</sub>
- **B. 8** ✅  
  <sub>Benar: $AB$: kolom $A$ = baris $B$ sehingga $x + 1 = 3$; $BA$: kolom $B$ = baris $A$ sehingga $y - 2 = 2$</sub>
- C. 9  
  <sub>Salah: mengambil $y - 2 = 3$ (kolom $A$) untuk kedua syarat</sub>
- D. 6  
  <sub>Salah: mengambil $x + 1 = 2$ (baris $A$) untuk kedua syarat</sub>

**Pembahasan:** $AB$ terdefinisi jika $3 = x + 1$ sehingga $x = 2$. $BA$ terdefinisi jika $y - 2 = 2$ sehingga $y = 4$. Jadi $2x + y = 8$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b01-d-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: sifat distributif*

Matriks $A$, $B$, dan $C$ berordo $2 \times 2$ dengan $AB = \begin{pmatrix}4 & -3 \\ 7 & 2\end{pmatrix}$ dan $AC = \begin{pmatrix}1 & 5 \\ -2 & 6\end{pmatrix}$. Matriks $A(B - C)$ adalah ....

- A. $\begin{pmatrix}-3 & 8 \\ -9 & 4\end{pmatrix}$  
  <sub>Salah: mengurangkan dengan urutan terbalik</sub>
- **B. $\begin{pmatrix}3 & -8 \\ 9 & -4\end{pmatrix}$** ✅  
  <sub>Benar: $A(B - C) = AB - AC$ lalu kurangkan per elemen</sub>
- C. $\begin{pmatrix}3 & -8 \\ 9 & 4\end{pmatrix}$  
  <sub>Salah: salah tanda pada $2 - 6$</sub>
- D. $\begin{pmatrix}5 & 2 \\ 5 & 8\end{pmatrix}$  
  <sub>Salah: memakai $AB + AC$ padahal bentuknya $A(B - C)$</sub>

**Pembahasan:** Sifat distributif: $A(B - C) = AB - AC = \begin{pmatrix}3 & -8 \\ 9 & -4\end{pmatrix}$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b01-d-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: parameter pada hasil perkalian*

Diketahui $A = \begin{pmatrix}2 & x \\ 1 & 3\end{pmatrix}$ dan $B = \begin{pmatrix}4 & -1 \\ -2 & 3\end{pmatrix}$. Jika jumlah elemen pada baris pertama matriks $AB$ sama dengan $1$, nilai $x$ adalah ....

- A. -3  
  <sub>Salah: menyederhanakan $8 - 2x + 3x - 2$ menjadi $4 + x$</sub>
- B. -7  
  <sub>Salah: lupa menghitung suku $-2$ pada elemen baris 1 kolom 2</sub>
- **C. -5** ✅  
  <sub>Benar: baris 1 $AB$: $8 - 2x$ dan $3x - 2$; jumlahnya $6 + x = 1$</sub>
- D. 5  
  <sub>Salah: salah tanda saat memindahkan 6 ke ruas kanan</sub>

**Pembahasan:** Elemen baris 1 kolom 1: $2 \cdot 4 + x(-2) = 8 - 2x$. Elemen baris 1 kolom 2: $2(-1) + 3x = 3x - 2$. Jumlahnya $6 + x = 1$ sehingga $x = -5$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b01-d-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: cerita perkalian tiga matriks*

Sebuah toko roti membuat kue A dan kue B. Banyak kue yang dipesan pada hari pertama dan kedua dinyatakan oleh $P = \begin{pmatrix}12 & 8 \\ 15 & 10\end{pmatrix}$ (baris: hari pertama dan kedua; kolom: kue A dan B). Bahan per kue dinyatakan oleh $N = \begin{pmatrix}3 & 2 & 1 \\ 2 & 4 & 2\end{pmatrix}$ (baris: kue A dan B; kolom: tepung (kg), gula (kg), telur (butir)). Harga bahan (ribu rupiah) per kg tepung, per kg gula, dan per butir telur berturut-turut adalah 12, 20, dan 2. Biaya bahan yang diperlukan pada hari kedua adalah ....

- A. Rp2.400.000,00  
  <sub>Salah: menukar biaya bahan kue A dan kue B</sub>
- B. Rp225.000,00  
  <sub>Salah: salah satuan: kurang satu nol</sub>
- **C. Rp2.250.000,00** ✅  
  <sub>Benar: $N$ dikalikan harga memberi biaya per kue: kue A 78 ribu dan kue B 108 ribu; hari kedua $15 \cdot 78 + 10 \cdot 108 = 2250$ ribu</sub>
- D. Rp1.800.000,00  
  <sub>Salah: mengambil hari pertama padahal yang ditanya hari kedua</sub>

**Pembahasan:** Biaya bahan per kue $= N \cdot H = \begin{pmatrix}78 \\ 108\end{pmatrix}$ (ribu rupiah). Hari kedua: $15 \cdot 78 + 10 \cdot 108 = 1170 + 1080 = 2250$ ribu rupiah $=$ Rp2.250.000,00.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b01-d-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: penjabaran bentuk aljabar matriks*

Matriks $A$ dan $B$ berordo $2 \times 2$. Bentuk $(A + B)(A + B)$ yang pasti benar untuk sembarang $A$ dan $B$ tersebut adalah ....

- A. $A^2 + 2AB + B^2$  
  <sub>Salah: mengira $AB = BA$ sehingga suku tengah digabung</sub>
- B. $A^2 + 2BA + B^2$  
  <sub>Salah: mengira $AB = BA$ lalu menuliskan $2BA$</sub>
- C. $A^2 + B^2$  
  <sub>Salah: melupakan dua suku silang hasil penjabaran</sub>
- **D. $A^2 + AB + BA + B^2$** ✅  
  <sub>Benar: $(A + B)(A + B) = A(A + B) + B(A + B) = A^2 + AB + BA + B^2$</sub>

**Pembahasan:** Distributif: $(A + B)(A + B) = A(A + B) + B(A + B) = A^2 + AB + BA + B^2$. Karena $AB$ dan $BA$ umumnya tidak sama, kedua suku tidak boleh digabung menjadi $2AB$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b01-d-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: klaim hasil kali nol*

Seorang siswa menyatakan bahwa jika $AB = O$ maka $A = O$ atau $B = O$. Diketahui $A = \begin{pmatrix}2 & 4 \\ 1 & 2\end{pmatrix}$ dan $B = \begin{pmatrix}6 & -2 \\ -3 & 1\end{pmatrix}$. Pernyataan yang benar tentang $A$ dan $B$ adalah ....

- A. $B = O$ karena semua elemen $AB$ bernilai nol  
  <sub>Salah: memakai sifat bilangan real pada matriks</sub>
- B. $AB = O$, $A \neq O$, $B \neq O$, dan $BA = O$  
  <sub>Salah: mengira BA ikut nol karena AB nol (menganggap komutatif)</sub>
- **C. $AB = O$ padahal $A \neq O$ dan $B \neq O$, tetapi $BA \neq O$** ✅  
  <sub>Benar: AB dihitung nol semua, sedangkan BA memuat elemen tak nol</sub>
- D. $AB \neq O$ karena $A \neq O$ dan $B \neq O$  
  <sub>Salah: menganggap hasil kali matriks tak nol pasti tak nol</sub>

**Pembahasan:** $AB = \begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix} = O$ dan $BA = \begin{pmatrix}10 & 20 \\ -5 & -10\end{pmatrix} \neq O$. Jadi $A \neq O$, $B \neq O$ namun $AB = O$: klaim siswa tidak berlaku pada matriks.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b01-d-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal pencoretan matriks*

Seorang siswa menyimpulkan bahwa $AB = AC$ berarti $B = C$ karena $A$ boleh dicoret. Diketahui $A = \begin{pmatrix}1 & 2 \\ 2 & 4\end{pmatrix}$, $B = \begin{pmatrix}3 & 6 \\ 3 & -1\end{pmatrix}$, dan $C = \begin{pmatrix}1 & 0 \\ 4 & 2\end{pmatrix}$. Pernyataan yang benar adalah ....

- A. $AB \neq AC$, sehingga $B \neq C$  
  <sub>Salah: salah menghitung AB atau AC</sub>
- B. $BA = CA$, sehingga $B = C$  
  <sub>Salah: mengira BA = CA; padahal hasil BA dan CA berbeda</sub>
- C. $AB = AC$ dan $B = C$  
  <sub>Salah: menganggap B = C karena AB = AC</sub>
- **D. $AB = AC$ walaupun $B \neq C$** ✅  
  <sub>Benar: AB dan AC dihitung sama, sedangkan B dan C berbeda</sub>

**Pembahasan:** $AB = AC = \begin{pmatrix}9 & 4 \\ 18 & 8\end{pmatrix}$, tetapi $B \neq C$. Matriks $BA = \begin{pmatrix}15 & 30 \\ 1 & 2\end{pmatrix}$ dan $CA = \begin{pmatrix}1 & 2 \\ 8 & 16\end{pmatrix}$ berbeda. Jadi pencoretan $A$ tidak berlaku.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b01-d-hard-bt01-003
*orisinal | C5 | 6 langkah | jenis: selisih ekspresi tidak komutatif*

Diketahui $A = \begin{pmatrix}2 & 1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & 5 \\ 2 & 3\end{pmatrix}$. Seorang siswa menyatakan $(A-B)^2 = A^2 - 2AB + B^2$. Matriks $(A-B)^2 - (A^2 - 2AB + B^2)$ sebenarnya sama dengan ....

- A. $\begin{pmatrix}21 & 34 \\ 24 & 41\end{pmatrix}$  
  <sub>Salah: salah tanda pada $-2AB$ sehingga menjadi $AB + BA$</sub>
- B. $O$  
  <sub>Salah: menganggap $AB = BA$ sehingga selisih nol</sub>
- **C. $\begin{pmatrix}-13 & -8 \\ -2 & 13\end{pmatrix}$** ✅  
  <sub>Benar: $(A-B)^2 = A^2 - AB - BA + B^2$, sehingga selisihnya $AB - BA$</sub>
- D. $\begin{pmatrix}13 & 8 \\ 2 & -13\end{pmatrix}$  
  <sub>Salah: tertukar tanda: $BA - AB$</sub>

**Pembahasan:** $(A-B)^2 = A^2 - AB - BA + B^2$. Selisih dengan $A^2 - 2AB + B^2$ adalah $AB - BA = \begin{pmatrix}4 & 13 \\ 11 & 27\end{pmatrix} - \begin{pmatrix}17 & 21 \\ 13 & 14\end{pmatrix} = \begin{pmatrix}-13 & -8 \\ -2 & 13\end{pmatrix}$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b01-d-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: parameter syarat komutatif*

Diketahui $A = \begin{pmatrix}2 & 5 \\ 3 & x\end{pmatrix}$ dan $B = \begin{pmatrix}7 & 10 \\ 6 & 9\end{pmatrix}$. Nilai $x$ yang membuat $AB = BA$ adalah ....

- **A. $3$** ✅  
  <sub>Benar: elemen baris 1 kolom 2: $65 = 35 + 10x$ sehingga $x = 3$, dan elemen baris 2 kolom 1: $21 + 6x = 39$ juga memberi $x = 3$</sub>
- B. $6$  
  <sub>Salah: membagi $39 - 21 = 18$ dengan 3, bukan dengan 6</sub>
- C. $5$  
  <sub>Salah: mengambil nilai elemen $a_{12}$ sebagai $x$</sub>
- D. $4$  
  <sub>Salah: salah mengurangi $65 - 35 = 40$ sehingga $x = 4$</sub>

**Pembahasan:** $AB = \begin{pmatrix}44 & 65 \\ 21+6x & 30+9x\end{pmatrix}$ dan $BA = \begin{pmatrix}44 & 35+10x \\ 39 & 30+9x\end{pmatrix}$. Dari $65 = 35 + 10x$ diperoleh $x = 3$ dan dari $21 + 6x = 39$ juga $x = 3$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b01-d-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: pola pangkat matriks segitiga*

Diketahui $A = \begin{pmatrix}1 & 7 \\ 0 & 1\end{pmatrix}$. Elemen baris 1 kolom 2 dari $A^{12}$ adalah ....

- A. $77$  
  <sub>Salah: memakai $n-1 = 11$ sebagai pengali</sub>
- **B. $84$** ✅  
  <sub>Benar: $A^n = \begin{pmatrix}1 & 7n \\ 0 & 1\end{pmatrix}$, maka $7 \times 12 = 84$</sub>
- C. $12$  
  <sub>Salah: lupa mengalikan dengan 7</sub>
- D. $19$  
  <sub>Salah: menjumlahkan $7 + 12$ bukan mengalikan</sub>

**Pembahasan:** $A^2 = \begin{pmatrix}1 & 14 \\ 0 & 1\end{pmatrix}$, $A^3 = \begin{pmatrix}1 & 21 \\ 0 & 1\end{pmatrix}$, sehingga $A^n = \begin{pmatrix}1 & 7n \\ 0 & 1\end{pmatrix}$ dan $A^{12}$ berelemen $84$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b01-d-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: pola pangkat matriks periodik*

Diketahui $A = \begin{pmatrix}0 & 1 \\ -1 & 0\end{pmatrix}$. Jumlah semua elemen matriks $A^{2026}$ adalah ....

- A. $0$  
  <sub>Salah: memakai jumlah elemen $A$ sendiri</sub>
- B. $2$  
  <sub>Salah: mengira $A^{2026} = I$ karena genap</sub>
- C. $-1$  
  <sub>Salah: hanya menjumlahkan satu elemen diagonal dari $-I$</sub>
- **D. $-2$** ✅  
  <sub>Benar: $A^2 = -I$, $A^4 = I$, dan $2026 = 4 \times 506 + 2$ sehingga $A^{2026} = -I$</sub>

**Pembahasan:** $A^2 = \begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix} = -I$, $A^4 = I$. Karena $2026 = 4 \times 506 + 2$, $A^{2026} = A^2 = -I$ dengan jumlah elemen $-2$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b01-d-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: parameter matriks idempoten*

Matriks $A = \begin{pmatrix}3 & -6 \\ 1 & x\end{pmatrix}$ memenuhi $AA = A$. Nilai $x$ adalah ....

- A. $3$  
  <sub>Salah: mengambil elemen $a_{11}$ sebagai $x$</sub>
- **B. $-2$** ✅  
  <sub>Benar: $AA$ elemen baris 2 kolom 1 adalah $3 + x = 1$ sehingga $x = -2$; elemen lain terpenuhi</sub>
- C. $-3$  
  <sub>Salah: menetapkan $3 + x = 0$ (bukan $=1$)</sub>
- D. $2$  
  <sub>Salah: salah tanda saat memindahkan ruas</sub>

**Pembahasan:** $AA = \begin{pmatrix}3 & -18-6x \\ 3+x & -6+x^2\end{pmatrix}$. Samakan dengan $A$: $3 + x = 1$ memberi $x = -2$; cek $-18-6x = -6$ dan $-6 + x^2 = x$ juga benar.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b01-d-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: parameter pangkat dua matriks nol*

Matriks $A = \begin{pmatrix}3 & -9 \\ 1 & x\end{pmatrix}$ memenuhi $AA = O$. Nilai $x$ adalah ....

- A. $9$  
  <sub>Salah: mengambil nilai dari $x^2 = 9$ tanpa memeriksa semua elemen</sub>
- B. $-1$  
  <sub>Salah: mengira elemen $a_{21}$ menjadi nilai $x$ dengan tanda negatif</sub>
- **C. $-3$** ✅  
  <sub>Benar: $AA$ elemen baris 2 kolom 1: $3 + x = 0$ sehingga $x = -3$; elemen lain terpenuhi</sub>
- D. $3$  
  <sub>Salah: salah tanda saat menyelesaikan $3 + x = 0$</sub>

**Pembahasan:** $AA = \begin{pmatrix}0 & -27-9x \\ 3+x & -9+x^2\end{pmatrix} = O$. Dari $3 + x = 0$ diperoleh $x = -3$; cek $-27 - 9x = 0$ dan $-9 + x^2 = 0$ juga benar. Nilai $x=3$ gagal pada $3+x=0$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b01-d-hard-bt01-009
*orisinal | C6 | 4 langkah | jenis: merancang matriks pembuat hasil kali nol*

Diketahui $A = \begin{pmatrix}2 & 6 \\ 1 & 3\end{pmatrix}$. Matriks $B$ yang bukan matriks nol dan memenuhi $AB = O$ adalah ....

- A. $\begin{pmatrix}-1 & 2 \\ 3 & -6\end{pmatrix}$  
  <sub>Salah: baris-baris B dibalik: kolom $(-1,3)$ tidak memenuhi</sub>
- B. $\begin{pmatrix}1 & 3 \\ -2 & -6\end{pmatrix}$  
  <sub>Salah: memakai kolom yang sejajar baris A, bukan yang tegak lurus</sub>
- **C. $\begin{pmatrix}3 & -6 \\ -1 & 2\end{pmatrix}$** ✅  
  <sub>Benar: tiap kolom $B$ harus kelipatan $(3, -1)^T$ agar $2a + 6b = 0$ dan $a + 3b = 0$</sub>
- D. $\begin{pmatrix}3 & -6 \\ 1 & -2\end{pmatrix}$  
  <sub>Salah: tanda elemen baris kedua salah sehingga kolom pertama $(3,1)$ gagal</sub>

**Pembahasan:** Kolom $(a, b)^T$ dari $B$ harus memenuhi $a + 3b = 0$, jadi kelipatan $(3, -1)^T$. $AB = \begin{pmatrix}0 & 0 \\ 0 & 0\end{pmatrix} = O$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b01-d-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan elemen hasil kali*

Diketahui $A = \begin{pmatrix}2 & -1 \\ 3 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}5 & 1 \\ -2 & 6\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}12 & 8 \\ 7 & 27\end{pmatrix}$ dan hanya satu elemen yang salah. Elemen yang salah beserta nilai yang benar adalah ....

- A. baris 2 kolom 2, seharusnya $8$  
  <sub>Salah: salah menentukan posisi dan nilai</sub>
- **B. baris 1 kolom 2, seharusnya $-4$** ✅  
  <sub>Benar: $2 \times 1 + (-1) \times 6 = -4$, sedangkan elemen lain sudah benar</sub>
- C. baris 1 kolom 2, seharusnya $4$  
  <sub>Salah: salah tanda pada hasil kali $(-1) \times 6$</sub>
- D. baris 2 kolom 1, seharusnya $-4$  
  <sub>Salah: salah menentukan posisi elemen yang keliru</sub>

**Pembahasan:** $AB = \begin{pmatrix}12 & -4 \\ 7 & 27\end{pmatrix}$. Elemen baris 1 kolom 2: $2(1) + (-1)(6) = -4$; siswa menulis $8$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b01-d-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: temukan kesalahan urutan perkalian*

Diketahui $A = \begin{pmatrix}3 & 1 \\ 2 & 4\end{pmatrix}$ dan $B = \begin{pmatrix}1 & -2 \\ 5 & 0\end{pmatrix}$. Seorang siswa menuliskan $AB = \begin{pmatrix}-1 & -7 \\ 15 & 5\end{pmatrix}$. Kesalahan siswa dan jumlah semua elemen $AB$ yang benar adalah ....

- A. siswa menghitung $BA$ (urutan tertukar); jumlahnya $12$  
  <sub>Salah: memakai jumlah elemen hasil siswa, bukan AB yang benar</sub>
- **B. siswa menghitung $BA$ (urutan tertukar); jumlahnya $20$** ✅  
  <sub>Benar: hasil siswa sama dengan BA; AB yang benar berjumlah 20</sub>
- C. siswa salah tanda pada satu elemen; jumlahnya $12$  
  <sub>Salah: hasil siswa salah pada semua elemen karena urutan, bukan satu tanda</sub>
- D. siswa menjumlahkan, bukan mengalikan; jumlahnya $20$  
  <sub>Salah: kesalahan salah dikenali: hasil siswa bukan $A+B$</sub>

**Pembahasan:** $AB = \begin{pmatrix}8 & -6 \\ 22 & -4\end{pmatrix}$ berjumlah $8 - 6 + 22 - 4 = 20$, sedangkan $BA = \begin{pmatrix}-1 & -7 \\ 15 & 5\end{pmatrix}$ sama dengan tulisan siswa.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b01-d-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: perbandingan pengelompokan ABC*

Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $10 \times 2$, $B$ berordo $2 \times 10$, dan $C$ berordo $10 \times 1$. Hasil $ABC$ sama saja, tetapi selisih banyak perkalian bilangan antara cara $(AB)C$ dan cara $A(BC)$ adalah ....

- A. $340$  
  <sub>Salah: menjumlahkan kedua cara, bukan mengurangkan</sub>
- B. $40$  
  <sub>Salah: hanya mengambil banyak perkalian cara $A(BC)$</sub>
- C. $300$  
  <sub>Salah: hanya mengambil banyak perkalian cara $(AB)C$</sub>
- **D. $260$** ✅  
  <sub>Benar: $(AB)C$: $200 + 100 = 300$; $A(BC)$: $20 + 20 = 40$; selisih $260$</sub>

**Pembahasan:** $(AB)$ berordo $10 \times 10$: $10 \cdot 2 \cdot 10 = 200$, lalu $\times C$: $10 \cdot 10 \cdot 1 = 100$. $(BC)$ berordo $2 \times 1$: $20$, lalu $A(BC)$: $10 \cdot 2 \cdot 1 = 20$. Selisih $300 - 40 = 260$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b01-d-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: perbandingan pengelompokan ABC*

Banyak perkalian bilangan untuk mengalikan matriks berordo $m \times n$ dengan $n \times p$ adalah $m \cdot n \cdot p$. Matriks $A$ berordo $3 \times 40$, $B$ berordo $40 \times 2$, dan $C$ berordo $2 \times 50$. Banyak perkalian bilangan paling sedikit untuk memperoleh $ABC$ dengan memilih salah satu pengelompokan adalah ....

- **A. $540$** ✅  
  <sub>Benar: $(AB)C$: $240 + 300 = 540$, sedangkan $A(BC)$: $4000 + 6000 = 10000$</sub>
- B. $4.240$  
  <sub>Salah: mencampur $BC$ dari satu cara dengan $AB$ dari cara lain</sub>
- C. $10.540$  
  <sub>Salah: menjumlahkan kedua pengelompokan</sub>
- D. $10.000$  
  <sub>Salah: memilih pengelompokan $A(BC)$ yang lebih boros</sub>

**Pembahasan:** $(AB)$ berordo $3 \times 2$: $3 \cdot 40 \cdot 2 = 240$; $(AB)C$: $3 \cdot 2 \cdot 50 = 300$; total $540$. $(BC)$ berordo $40 \times 50$: $4000$; $A(BC)$: $3 \cdot 40 \cdot 50 = 6000$; total $10000$. Jadi minimum $540$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b01-d-hard-bt01-014
*orisinal | C6 | 4 langkah | jenis: aljabar matriks dengan syarat idempoten*

Matriks $A$ bukan matriks nol dan memenuhi $AA = A$, sedangkan $I$ matriks identitas seordo dengan $A$. Untuk $B = 2A - I$, hasil $B^2$ sama dengan ....

- A. $O$  
  <sub>Salah: menganggap suku $4A - 4A$ menghabiskan semua suku</sub>
- B. $A$  
  <sub>Salah: menganggap $B$ ikut idempoten sehingga hasilnya sama dengan $A$</sub>
- C. $4A - I$  
  <sub>Salah: lupa suku silang $-4A$ sehingga hanya $4A^2 - I$</sub>
- **D. $I$** ✅  
  <sub>Benar: $B^2 = 4A^2 - 4A + I = 4A - 4A + I = I$</sub>

**Pembahasan:** $(2A - I)(2A - I) = 4AA - 2AI - 2IA + II = 4A - 2A - 2A + I = I$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11_tl-b01-d-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: aljabar matriks dengan syarat pangkat dua nol*

Matriks $A$ bukan matriks nol, memenuhi $AA = O$, dan $I$ matriks identitas seordo dengan $A$. Hasil $(I + A)^4$ sama dengan ....

- A. $I + 6A$  
  <sub>Salah: memakai koefisien binomial tengah 6 untuk $A$</sub>
- **B. $I + 4A$** ✅  
  <sub>Benar: $(I+A)^2 = I + 2A$, lalu $(I + 2A)^2 = I + 4A$</sub>
- C. $I$  
  <sub>Salah: menganggap $A$ lenyap pada setiap pangkat</sub>
- D. $I + A$  
  <sub>Salah: mengira $(I+A)^n = I + A$ untuk semua $n$</sub>

**Pembahasan:** $(I + A)^2 = I + 2A + A^2 = I + 2A$. Kemudian $(I + 2A)^2 = I + 4A + 4A^2 = I + 4A$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11_tl-b01-d-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: kombinasi linear matriks dan identitas*

Diketahui $A = \begin{pmatrix}2 & 3 \\ 4 & 1\end{pmatrix}$ dan $I$ matriks identitas ordo $2 \times 2$. Jika $A^2 = pA + qI$, nilai $q - p$ adalah ....

- **A. $7$** ✅  
  <sub>Benar: $A^2 = \begin{pmatrix}16 & 9 \\ 12 & 13\end{pmatrix}$; elemen baris 1 kolom 2: $3p = 9$ sehingga $p = 3$; elemen baris 1 kolom 1: $2p + q = 16$ sehingga $q = 10$</sub>
- B. $10$  
  <sub>Salah: hanya mengambil nilai $q$</sub>
- C. $13$  
  <sub>Salah: menghitung $p + q$, bukan $q - p$</sub>
- D. $-7$  
  <sub>Salah: mengurangkan terbalik: $p - q$</sub>

**Pembahasan:** $A^2 = \begin{pmatrix}16 & 9 \\ 12 & 13\end{pmatrix}$ dan $pA + qI = \begin{pmatrix}2p + q & 3p \\ 4p & p + q\end{pmatrix}$. Maka $p = 3$, $q = 10$ (cek $p + q = 13$), sehingga $q - p = 7$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11_tl-b01-d-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: klaim sifat yang selalu berlaku*

Matriks $A$, $B$, $C$ semuanya persegi seordo. Pernyataan yang selalu benar adalah ....

- **A. $(A + B)C = AC + BC$** ✅  
  <sub>Benar: sifat distributif dari kanan</sub>
- B. $(AB)^2 = A^2 B^2$  
  <sub>Salah: menganggap faktor boleh dipertukarkan</sub>
- C. $(A + B)^2 = A^2 + 2AB + B^2$  
  <sub>Salah: menganggap $AB = BA$</sub>
- D. jika $AB = AC$ maka $B = C$  
  <sub>Salah: mencoret $A$ seperti pada bilangan real</sub>

**Pembahasan:** Hanya sifat distributif $(A + B)C = AC + BC$ yang berlaku untuk semua matriks persegi seordo. Tiga klaim lain memerlukan $AB = BA$ atau pencoretan, yang tidak berlaku umum.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11_tl-b01-d-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: klaim sifat yang selalu berlaku*

Matriks $A$ dan $B$ persegi seordo, dan $I$ matriks identitas seordo. Pernyataan yang selalu benar adalah ....

- A. jika $AB = O$ maka $BA = O$  
  <sub>Salah: menganggap perkalian komutatif untuk hasil nol</sub>
- B. $(A + B)(A - B) = A^2 - B^2$  
  <sub>Salah: suku $-AB + BA$ tidak saling meniadakan bila $AB \neq BA$</sub>
- **C. $(A + I)(A - I) = A^2 - I$** ✅  
  <sub>Benar: $I$ komutatif terhadap $A$ sehingga suku $-A + A$ saling meniadakan</sub>
- D. jika $A^2 = I$ maka $A = I$ atau $A = -I$  
  <sub>Salah: menyamakan dengan akar bilangan real; ada matriks lain, misalnya $\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$</sub>

**Pembahasan:** $(A + I)(A - I) = A^2 - AI + IA - I^2 = A^2 - I$. Tiga klaim lain punya penyangkal sederhana pada matriks $2 \times 2$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
