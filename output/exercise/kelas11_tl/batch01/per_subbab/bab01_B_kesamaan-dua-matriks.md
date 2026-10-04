# Lembar koreksi — kelas11_tl SMA11L-B1 subbab B: Kesamaan Dua Matriks

50 soal | easy 20, medium 20, hard 10 | variasi 18, orisinal 32
> **Kapasitas kurang (hard): 10 dari kuota 20** — Subbab B hanya ~2 halaman (Definisi 1.1: ordo sama dan elemen seletak sama). Easy dan medium sudah memakai 40 soal; hard yang bermakna hanya penalaran sifat kesamaan (evaluasi klaim, contoh penyangkal, kesalahan ordo, parameter, pencacahan, rantai). Menambah ke 20 akan memunculkan soal nyaris kembar atau materi di luar subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b01-b-easy-bt01-001
*orisinal | C2 | 2 langkah | jenis: memeriksa kesamaan dua matriks*

Diketahui matriks $P = \begin{pmatrix} 2 & 5 \\ 7 & 3 \end{pmatrix}$. Matriks berikut yang sama dengan $P$ adalah ....

- A. $\begin{pmatrix} 2 & 7 \\ 5 & 3 \end{pmatrix}$  
  <sub>Salah: elemen baris dan kolom tertukar sehingga elemen seletak berbeda</sub>
- B. $\begin{pmatrix} 2 & 5 & 0 \\ 7 & 3 & 0 \end{pmatrix}$  
  <sub>Salah: ordo berbeda (2 x 3), padahal syarat pertama adalah ordo sama</sub>
- **C. $\begin{pmatrix} \frac{4}{2} & 5 \\ 7 & \frac{6}{2} \end{pmatrix}$** ✅  
  <sub>Benar: ordo sama (2 x 2) dan semua elemen seletak bernilai sama setelah dihitung: 4/2 = 2, 6/2 = 3</sub>
- D. $\begin{pmatrix} 2 & 5 \\ 3 & 7 \end{pmatrix}$  
  <sub>Salah: urutan elemen baris kedua terbalik sehingga tidak seletak</sub>

**Pembahasan:** Dua matriks sama jika ordo sama dan elemen seletak sama. Pilihan benar berordo 2 x 2 dengan elemen 2, 5, 7, 3 seperti $P$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b01-b-easy-bt01-002
*orisinal | C1 | 1 langkah | jenis: elemen seletak*

Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ keduanya berordo $3 \times 3$ dan $A = B$. Jika $a_{23} = 9$, maka ....

- A. $b_{32} = 9$  
  <sub>Salah: indeks baris dan kolom tertukar</sub>
- B. $b_{13} = 9$  
  <sub>Salah: salah mengambil baris, mengira letaknya baris ke-1</sub>
- C. $b_{22} = 9$  
  <sub>Salah: salah mengambil kolom, mengira letaknya baris ke-2 kolom ke-2</sub>
- **D. $b_{23} = 9$** ✅  
  <sub>Benar: elemen seletak pada baris ke-2 kolom ke-3 bernilai sama, sehingga $b_{23} = a_{23}$</sub>

**Pembahasan:** Karena $A = B$, $a_{ij} = b_{ij}$ untuk semua $i$ dan $j$, sehingga $b_{23} = a_{23} = 9$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b01-b-easy-bt01-003
*orisinal | C2 | 1 langkah | jenis: mencari nilai satu variabel*

Diketahui $\begin{pmatrix} 2x & 5 \\ 1 & 7 \end{pmatrix} = \begin{pmatrix} 18 & 5 \\ 1 & 7 \end{pmatrix}$. Nilai $x$ adalah ....

- **A. 9** ✅  
  <sub>Benar: elemen seletak: $2x = 18$ sehingga $x = 9$</sub>
- B. 36  
  <sub>Salah: mengalikan 18 dengan 2, bukan membagi</sub>
- C. -9  
  <sub>Salah: salah tanda pada hasil</sub>
- D. 16  
  <sub>Salah: mengurangkan 2 dari 18</sub>

**Pembahasan:** Elemen lain sudah sama. Dari $2x = 18$ diperoleh $x = 9$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b01-b-easy-bt01-004
*orisinal | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Diketahui $\begin{pmatrix} 3a - 2 & 0 \\ 4 & b + 6 \end{pmatrix} = \begin{pmatrix} 10 & 0 \\ 4 & 1 \end{pmatrix}$. Nilai $a + b$ adalah ....

- A. 4  
  <sub>Salah: hanya menghitung nilai $a$</sub>
- **B. -1** ✅  
  <sub>Benar: $3a - 2 = 10$ memberi $a = 4$; $b + 6 = 1$ memberi $b = -5$; jadi $a + b = -1$</sub>
- C. 11  
  <sub>Salah: salah memindahkan 6: $b = 1 + 6 = 7$ sehingga $a + b = 11$</sub>
- D. -5  
  <sub>Salah: hanya menghitung nilai $b$</sub>

**Pembahasan:** $3a = 12$ maka $a = 4$. $b = 1 - 6 = -5$. Jadi $a + b = 4 + (-5) = -1$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b01-b-easy-bt01-005
*orisinal | C2 | 1 langkah | jenis: memeriksa kesamaan dua matriks*

Diketahui $P = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$. Pernyataan yang benar adalah ....

- A. $P = Q$ karena kedua matriks mempunyai 6 elemen  
  <sub>Salah: mengira banyak elemen yang sama cukup untuk kesamaan</sub>
- B. $P = Q$ karena kedua matriks memuat elemen 1, 2, 3, 4, 5, 6  
  <sub>Salah: hanya melihat daftar elemen, mengabaikan ordo dan letak elemen</sub>
- **C. $P \neq Q$ karena ordo kedua matriks berbeda** ✅  
  <sub>Benar: $P$ berordo $2 \times 3$ sedangkan $Q$ berordo $3 \times 2$, sehingga syarat pertama kesamaan tidak terpenuhi</sub>
- D. $P \neq Q$ karena elemen pada baris ke-1 kolom ke-1 berbeda  
  <sub>Salah: elemen seletak (1, 1) keduanya 1, jadi alasannya salah</sub>

**Pembahasan:** Ordo $P$ adalah $2 \times 3$ dan ordo $Q$ adalah $3 \times 2$, ordonya berbeda sehingga $P \neq Q$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b01-b-easy-bt01-006
*orisinal | C2 | 2 langkah | jenis: mencari nilai satu variabel*

Diketahui $\begin{pmatrix} m^2 & 1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 16 & 1 \\ 0 & 5 \end{pmatrix}$ dengan $m > 0$. Nilai $m$ adalah ....

- A. 256  
  <sub>Salah: mengkuadratkan 16, bukan menarik akar</sub>
- B. 8  
  <sub>Salah: membagi 16 dengan 2 alih-alih menarik akar</sub>
- C. -4  
  <sub>Salah: mengabaikan syarat $m > 0$</sub>
- **D. 4** ✅  
  <sub>Benar: $m^2 = 16$ dan $m > 0$ sehingga $m = 4$</sub>

**Pembahasan:** Elemen seletak: $m^2 = 16$, maka $m = \pm 4$. Karena $m > 0$, $m = 4$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b01-b-easy-bt01-007
*orisinal | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Matriks $\begin{pmatrix} a - 3 & 2b \\ c + 5 & d \end{pmatrix}$ sama dengan matriks nol berordo $2 \times 2$. Nilai $a + b + c + d$ adalah ....

- **A. -2** ✅  
  <sub>Benar: $a = 3$, $b = 0$, $c = -5$, $d = 0$, sehingga jumlahnya $-2$</sub>
- B. 8  
  <sub>Salah: salah tanda: $c = 5$ sehingga jumlah 8</sub>
- C. 3  
  <sub>Salah: hanya menghitung nilai $a$</sub>
- D. -5  
  <sub>Salah: hanya menghitung nilai $c$</sub>

**Pembahasan:** Setiap elemen sama dengan 0: $a - 3 = 0$, $2b = 0$, $c + 5 = 0$, $d = 0$. Jumlah: $3 + 0 - 5 + 0 = -2$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b01-b-easy-bt01-008
*orisinal | C2 | 2 langkah | jenis: mencari beberapa variabel*

Diketahui $A = \begin{pmatrix} 1 & x \\ y & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 8 \\ 3 & 4 \end{pmatrix}$. Jika $A = B$, nilai $x - y$ adalah ....

- A. 24  
  <sub>Salah: mengalikan $x$ dan $y$</sub>
- B. -5  
  <sub>Salah: $x$ dan $y$ tertukar letaknya sehingga $x = 3$, $y = 8$</sub>
- C. 11  
  <sub>Salah: menjumlahkan, bukan mengurangkan</sub>
- **D. 5** ✅  
  <sub>Benar: $x = 8$ (baris 1 kolom 2) dan $y = 3$ (baris 2 kolom 1), sehingga $x - y = 5$</sub>

**Pembahasan:** Elemen seletak: $x = 8$ dan $y = 3$. Maka $x - y = 8 - 3 = 5$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b01-b-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: syarat kesamaan*

Matriks $A = (a_{ij})$ dan $B = (b_{ij})$ berordo sama. Syarat kedua agar $A = B$ adalah ....

- A. $a_{11} = b_{11}$ saja  
  <sub>Salah: hanya memeriksa satu elemen, bukan semua elemen seletak</sub>
- **B. $a_{ij} = b_{ij}$ untuk semua $i$ dan $j$** ✅  
  <sub>Benar: setiap elemen yang seletak harus bernilai sama</sub>
- C. jumlah semua $a_{ij}$ sama dengan jumlah semua $b_{ij}$  
  <sub>Salah: mengira jumlah elemen yang sama sudah cukup</sub>
- D. $a_{ij} = b_{ji}$ untuk semua $i$ dan $j$  
  <sub>Salah: mengira indeks baris dan kolom boleh ditukar</sub>

**Pembahasan:** Menurut definisi, $A = B$ bila ordonya sama dan $a_{ij} = b_{ij}$ untuk semua $i$ dan $j$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b01-b-easy-bt01-010
*variasi (konteks) | C1 | 1 langkah | jenis: syarat kesamaan*

Agar matriks $P$ dan matriks $Q$ dapat dikatakan sama, syarat pertama yang harus dipenuhi adalah ....

- **A. keduanya berordo sama** ✅  
  <sub>Benar: syarat pertama dalam definisi kesamaan dua matriks adalah ordo yang sama</sub>
- B. keduanya mempunyai determinan yang sama  
  <sub>Salah: memakai sifat yang bukan syarat kesamaan</sub>
- C. keduanya matriks persegi  
  <sub>Salah: mengira kedua matriks harus persegi</sub>
- D. hanya baris pertama keduanya yang sama  
  <sub>Salah: mengira cukup memeriksa sebagian elemen</sub>

**Pembahasan:** Definisi 1.1: dua matriks sama jika ordonya sama dan elemen seletaknya sama.
**Acuan:** siswa — siswa hal.26 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b01-b-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: menentukan ordo*

Matriks $A$ berordo $2 \times 4$. Jika $A = B$, maka ordo matriks $B$ adalah ....

- **A. $2 \times 4$** ✅  
  <sub>Benar: dua matriks yang sama pasti berordo sama</sub>
- B. $8 \times 1$  
  <sub>Salah: hanya mencocokkan banyak elemen, bukan ordo</sub>
- C. $4 \times 2$  
  <sub>Salah: banyak baris dan kolom tertukar</sub>
- D. $2 \times 2$  
  <sub>Salah: hanya mengambil banyak baris</sub>

**Pembahasan:** Karena $A = B$, ordo $B$ sama dengan ordo $A$, yaitu $2 \times 4$.
**Acuan:** siswa — siswa hal.26 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b01-b-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: mencari beberapa variabel*

Diketahui matriks $K = \begin{pmatrix} 3p & 7 \\ -q & 5 \end{pmatrix}$ dan $L = \begin{pmatrix} 12 & 7 \\ 6 & 5 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$, nilai $p$ dan $q$ berturut-turut adalah ....

- A. $p = 9$ dan $q = -6$  
  <sub>Salah: mengurangkan 3 dari 12, bukan membagi</sub>
- B. $p = 4$ dan $q = 6$  
  <sub>Salah: lupa tanda negatif pada $-q = 6$</sub>
- C. $p = 36$ dan $q = -6$  
  <sub>Salah: mengalikan 12 dengan 3, bukan membagi</sub>
- **D. $p = 4$ dan $q = -6$** ✅  
  <sub>Benar: $3p = 12$ memberi $p = 4$; $-q = 6$ memberi $q = -6$</sub>

**Pembahasan:** Elemen seletak: $3p = 12 \Rightarrow p = 4$ dan $-q = 6 \Rightarrow q = -6$.
**Acuan:** siswa — siswa hal.25 Contoh 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b01-b-easy-bt01-013
*variasi (konteks) | C2 | 2 langkah | jenis: mencari beberapa variabel*

Diketahui matriks $K = \begin{pmatrix} -r & 4 \\ 2s & t^2 \end{pmatrix}$ dan $L = \begin{pmatrix} -8 & 4 \\ 10 & 49 \end{pmatrix}$. Jika matriks $K$ sama dengan matriks $L$ dan $t > 0$, nilai $r$, $s$, dan $t$ berturut-turut adalah ....

- A. $r = 8$, $s = 5$, $t = \frac{49}{2}$  
  <sub>Salah: membagi 49 dengan 2 alih-alih menarik akar</sub>
- B. $r = 8$, $s = 20$, $t = 7$  
  <sub>Salah: mengalikan 10 dengan 2, bukan membagi</sub>
- C. $r = -8$, $s = 5$, $t = 7$  
  <sub>Salah: mengabaikan tanda negatif pada $-r = -8$</sub>
- **D. $r = 8$, $s = 5$, $t = 7$** ✅  
  <sub>Benar: $-r = -8$ memberi $r = 8$; $2s = 10$ memberi $s = 5$; $t^2 = 49$ dengan $t > 0$ memberi $t = 7$</sub>

**Pembahasan:** Elemen seletak: $r = 8$, $s = 5$, dan $t^2 = 49$ sehingga $t = 7$ karena $t > 0$.
**Acuan:** siswa — siswa hal.25 Contoh 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b01-b-easy-bt01-014
*variasi (konteks) | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Diketahui matriks $A = \begin{pmatrix} c & 2a \\ b + 4 & 9 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 10 \\ 1 & d \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $a + b + c + d$ adalah ....

- A. 22  
  <sub>Salah: mengabaikan tanda negatif: $b = 3$</sub>
- **B. 16** ✅  
  <sub>Benar: $c = 5$, $2a = 10$ sehingga $a = 5$, $b + 4 = 1$ sehingga $b = -3$, $d = 9$; jumlah $= 16$</sub>
- C. 24  
  <sub>Salah: salah memindahkan 4: $b = 5$</sub>
- D. 21  
  <sub>Salah: lupa membagi 2: $a = 10$</sub>

**Pembahasan:** $a = 5$, $b = -3$, $c = 5$, $d = 9$. Jumlah: $5 - 3 + 5 + 9 = 16$.
**Acuan:** siswa — siswa hal.26 Mari Mencoba 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b01-b-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 4a & b + 8 \\ c - 6 & 3d \end{pmatrix} = \begin{pmatrix} 20 & 15 \\ 2 & 21 \end{pmatrix}$

- A. 83  
  <sub>Salah: mengalikan 21 dengan 3, bukan membagi: $d = 63$</sub>
- **B. 27** ✅  
  <sub>Benar: $a = 5$, $b = 7$, $c = 8$, $d = 7$, sehingga jumlahnya 27</sub>
- C. 15  
  <sub>Salah: salah tanda: $c = -4$</sub>
- D. 43  
  <sub>Salah: salah memindahkan 8: $b = 23$</sub>

**Pembahasan:** $4a = 20 \Rightarrow a = 5$; $b = 15 - 8 = 7$; $c = 2 + 6 = 8$; $3d = 21 \Rightarrow d = 7$. Jumlah $= 27$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b01-b-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: kesamaan dengan matriks identitas*

Jika $A = \begin{pmatrix} 4x - 3 & y + 5 \\ z - 9 & 6w - 5 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $x + y + z + w$.

- A. 16  
  <sub>Salah: salah tanda: $y = 5$</sub>
- B. -12  
  <sub>Salah: salah tanda: $z = -9$</sub>
- **C. 6** ✅  
  <sub>Benar: $4x - 3 = 1$ memberi $x = 1$; $y + 5 = 0$ memberi $y = -5$; $z - 9 = 0$ memberi $z = 9$; $6w - 5 = 1$ memberi $w = 1$; jumlah 6</sub>
- D. 8  
  <sub>Salah: menyamakan elemen di luar diagonal dengan 1, bukan 0</sub>

**Pembahasan:** Elemen diagonal $I$ bernilai 1, elemen lainnya 0. Maka $x = 1$, $y = -5$, $z = 9$, $w = 1$, jumlah $= 6$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b01-b-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Hitunglah nilai $p + q + r$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 3p & q - 5 & r + 2 \end{pmatrix} = \begin{pmatrix} 18 & 4 & 9 \end{pmatrix}$

- **A. 22** ✅  
  <sub>Benar: $p = 6$, $q = 9$, $r = 7$, jumlahnya 22</sub>
- B. 70  
  <sub>Salah: mengalikan 18 dengan 3, bukan membagi: $p = 54$</sub>
- C. 12  
  <sub>Salah: salah memindahkan 5: $q = -1$</sub>
- D. 26  
  <sub>Salah: salah memindahkan 2: $r = 11$</sub>

**Pembahasan:** $3p = 18 \Rightarrow p = 6$; $q = 4 + 5 = 9$; $r = 9 - 2 = 7$. Jumlah $= 22$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b01-b-easy-bt01-018
*variasi (konteks) | C2 | 2 langkah | jenis: menjumlahkan nilai variabel*

Diketahui matriks $A = \begin{pmatrix} 2p \\ q + 1 \\ r - 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 8 \\ 0 \\ 5 \end{pmatrix}$. Jika matriks $A$ sama dengan matriks $B$, nilai $p + q + r$ adalah ....

- A. 13  
  <sub>Salah: salah tanda: $q = 1$</sub>
- **B. 11** ✅  
  <sub>Benar: $p = 4$, $q = -1$, $r = 8$, sehingga jumlahnya 11</sub>
- C. 5  
  <sub>Salah: salah memindahkan 3: $r = 2$</sub>
- D. 23  
  <sub>Salah: mengalikan 8 dengan 2, bukan membagi: $p = 16$</sub>

**Pembahasan:** $2p = 8 \Rightarrow p = 4$; $q + 1 = 0 \Rightarrow q = -1$; $r - 3 = 5 \Rightarrow r = 8$. Jumlah $= 11$.
**Acuan:** siswa — siswa hal.26 Mari Mencoba 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b01-b-easy-bt01-019
*variasi (konteks) | C2 | 1 langkah | jenis: elemen seletak*

Matriks $G$ dan matriks $H$ keduanya berordo $3 \times 5$ dan $G = H$. Banyak persamaan yang terbentuk dari kesamaan elemen-elemen seletak $G$ dan $H$ adalah ....

- A. 5  
  <sub>Salah: hanya menghitung banyak kolom</sub>
- B. 8  
  <sub>Salah: menjumlahkan banyak baris dan kolom (3 + 5)</sub>
- **C. 15** ✅  
  <sub>Benar: setiap pasang elemen seletak menghasilkan satu persamaan; banyaknya 3 x 5 = 15</sub>
- D. 3  
  <sub>Salah: hanya menghitung banyak baris</sub>

**Pembahasan:** Ada $3 \times 5 = 15$ pasang elemen seletak, sehingga terbentuk 15 persamaan.
**Acuan:** siswa — siswa hal.26 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b01-b-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: mencari beberapa variabel*

Diketahui $\begin{pmatrix} x + 1 & 2y \end{pmatrix} = \begin{pmatrix} 6 & -8 \end{pmatrix}$. Nilai $xy$ adalah ....

- A. -80  
  <sub>Salah: lupa membagi 2: $y = -8$</sub>
- B. 20  
  <sub>Salah: salah tanda: $y = 4$</sub>
- **C. -20** ✅  
  <sub>Benar: $x = 5$ dan $y = -4$, sehingga $xy = -20$</sub>
- D. -28  
  <sub>Salah: salah memindahkan 1: $x = 7$</sub>

**Pembahasan:** $x + 1 = 6 \Rightarrow x = 5$ dan $2y = -8 \Rightarrow y = -4$. Maka $xy = 5 \times (-4) = -20$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b01-b-medium-bt01-001
*variasi (angka) | C3 | 4 langkah | jenis: sistem persamaan dari elemen*

Hitunglah nilai $a + b + c + d$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} a + 4b & 3a + b \\ c + 3d & 2c + d \end{pmatrix} = \begin{pmatrix} -4 & 10 \\ 15 & 0 \end{pmatrix}$

- A. -7  
  <sub>Salah: salah tanda pada $d$: $d = -6$ sehingga jumlah $4 - 2 - 3 - 6 = -7$</sub>
- B. 11  
  <sub>Salah: salah tanda pada $c$: $c = 3$ sehingga jumlah $4 - 2 + 3 + 6 = 11$</sub>
- C. 9  
  <sub>Salah: salah tanda pada $b$: $b = 2$ sehingga jumlah $4 + 2 - 3 + 6 = 9$</sub>
- **D. 5** ✅  
  <sub>Benar: $a + 4b = -4$ dan $3a + b = 10$ memberi $a = 4$, $b = -2$; $c + 3d = 15$ dan $2c + d = 0$ memberi $c = -3$, $d = 6$; jumlah 5</sub>

**Pembahasan:** Elemen seletak: $a + 4b = -4$, $3a + b = 10$ sehingga $b = 10 - 3a$, $a + 40 - 12a = -4$, $a = 4$, $b = -2$. $c + 3d = 15$, $2c + d = 0$ sehingga $d = -2c$, $c - 6c = 15$, $c = -3$, $d = 6$. Jumlah $= 4 - 2 - 3 + 6 = 5$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b01-b-medium-bt01-002
*variasi (angka) | C3 | 4 langkah | jenis: sistem persamaan dari elemen*

Tentukan nilai $ab + cd$ yang memenuhi kesamaan matriks berikut. $\begin{pmatrix} 2a - b & a + b \\ 3c + d & c - d \end{pmatrix} = \begin{pmatrix} 6 & 9 \\ -13 & 5 \end{pmatrix}$

- **A. 34** ✅  
  <sub>Benar: $2a - b = 6$ dan $a + b = 9$ memberi $a = 5$, $b = 4$; $3c + d = -13$ dan $c - d = 5$ memberi $c = -2$, $d = -7$; $ab + cd = 20 + 14 = 34$</sub>
- B. 0  
  <sub>Salah: menjumlahkan keempat variabel $5 + 4 - 2 - 7$, bukan $ab + cd$</sub>
- C. 20  
  <sub>Salah: hanya menghitung $ab$ dan melupakan $cd$</sub>
- D. 6  
  <sub>Salah: salah tanda pada $cd$: mengira $cd = -14$ sehingga $20 - 14 = 6$</sub>

**Pembahasan:** Eliminasi: $3a = 15$ sehingga $a = 5$, $b = 4$. $4c = -8$ sehingga $c = -2$, $d = c - 5 = -7$. $ab + cd = 20 + 14 = 34$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b01-b-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: kesamaan dengan matriks identitas*

Jika $A = \begin{pmatrix} 9x - y & 0 \\ (4x - y)^2 & 1 \end{pmatrix}$ dan $I$ adalah matriks identitas yang seordo dengan $A$. Jika $A = I$, tentukan nilai $x + 5y$.

- A. $4$  
  <sub>Salah: hanya menghitung suku $5y$ dan melupakan $x$</sub>
- B. $\frac{9}{35}$  
  <sub>Salah: salah relasi: memakai $x = 4y$ sehingga $35y = 1$ dan $x + 5y = \frac{9}{35}$</sub>
- C. $\frac{21}{13}$  
  <sub>Salah: salah tanda: memakai $9x + y = 1$ sehingga $x = \frac{1}{13}$ dan $x + 5y = \frac{21}{13}$</sub>
- **D. $\frac{21}{5}$** ✅  
  <sub>Benar: $(4x - y)^2 = 0$ memberi $y = 4x$; $9x - y = 1$ memberi $5x = 1$, $x = \frac{1}{5}$, $y = \frac{4}{5}$, sehingga $x + 5y = \frac{21}{5}$</sub>

**Pembahasan:** Elemen baris 2 kolom 1 harus 0: $(4x - y)^2 = 0$ sehingga $y = 4x$. Elemen $a_{11} = 1$: $9x - 4x = 1$, $x = \frac{1}{5}$, $y = \frac{4}{5}$. Jadi $x + 5y = \frac{1}{5} + 4 = \frac{21}{5}$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b01-b-medium-bt01-004
*variasi (angka) | C4 | 4 langkah | jenis: kesamaan dengan matriks identitas*

Jika $A = \begin{pmatrix} 2x + y & (x - 4y)^2 \\ 0 & x + 5y \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $2 \times 2$ dengan $A = I$, tentukan nilai $5x - y$.

- **A. $\frac{19}{9}$** ✅  
  <sub>Benar: $(x - 4y)^2 = 0$ memberi $x = 4y$; $2x + y = 1$ memberi $y = \frac{1}{9}$, $x = \frac{4}{9}$ (dan $x + 5y = 1$ terpenuhi); $5x - y = \frac{19}{9}$</sub>
- B. $\frac{19}{7}$  
  <sub>Salah: salah tanda: memakai $2x - y = 1$ sehingga $x = \frac{4}{7}$, $y = \frac{1}{7}$</sub>
- C. $\frac{1}{6}$  
  <sub>Salah: salah relasi: memakai $y = 4x$ sehingga $x = \frac{1}{6}$, $y = \frac{2}{3}$</sub>
- D. $\frac{20}{9}$  
  <sub>Salah: hanya menghitung suku $5x$ dan melupakan $-y$</sub>

**Pembahasan:** Elemen baris 1 kolom 2 harus 0, jadi $x = 4y$. Elemen $a_{11} = 1$: $9y = 1$, $y = \frac{1}{9}$, $x = \frac{4}{9}$. Cek $a_{22} = \frac{4}{9} + \frac{5}{9} = 1$. $5x - y = \frac{20}{9} - \frac{1}{9} = \frac{19}{9}$.
**Acuan:** pretest — kelas11_tl-b01-p0026-latihan-b-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b01-b-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: persamaan kuadrat pada elemen*

Matriks $K = \begin{pmatrix} 3x - 1 & 4 \\ -y & z^2 \end{pmatrix}$ dan $L = \begin{pmatrix} 8 & 4 \\ 5 & 36 \end{pmatrix}$ memenuhi $K = L$. Nilai terkecil yang mungkin bagi $x + y + z$ adalah ....

- A. 4  
  <sub>Salah: mengambil $z = 6$ sehingga yang diperoleh nilai terbesar, bukan terkecil</sub>
- **B. -8** ✅  
  <sub>Benar: $x = 3$, $y = -5$, dan $z = \pm 6$; jumlah terkecil dicapai saat $z = -6$ yaitu $3 - 5 - 6 = -8$</sub>
- C. 14  
  <sub>Salah: salah tanda pada $y$ dan hanya memakai $z = 6$</sub>
- D. 2  
  <sub>Salah: salah tanda pada $y$: $y = 5$ dan $z = -6$ sehingga $3 + 5 - 6 = 2$</sub>

**Pembahasan:** $3x - 1 = 8$ sehingga $x = 3$; $-y = 5$ sehingga $y = -5$; $z^2 = 36$ sehingga $z = 6$ atau $z = -6$. Nilai terkecil: $3 - 5 - 6 = -8$.
**Acuan:** siswa — siswa hal.25 Contoh 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b01-b-medium-bt01-006
*variasi (konteks) | C4 | 4 langkah | jenis: persamaan kuadrat pada elemen*

Diketahui $P = \begin{pmatrix} (m - 2)^2 & 5 \\ 2n & 1 \end{pmatrix}$ dan $Q = \begin{pmatrix} 49 & 5 \\ -6 & 1 \end{pmatrix}$. Jika $P = Q$, nilai terbesar yang mungkin bagi $m + n$ adalah ....

- **A. 6** ✅  
  <sub>Benar: $(m - 2)^2 = 49$ memberi $m = 9$ atau $m = -5$; $2n = -6$ memberi $n = -3$; nilai terbesar $m + n = 9 - 3 = 6$</sub>
- B. 12  
  <sub>Salah: salah tanda: $n = 3$ sehingga $9 + 3 = 12$</sub>
- C. 4  
  <sub>Salah: menarik akar tanpa menggeser 2: $m = 7$ sehingga $7 - 3 = 4$</sub>
- D. -8  
  <sub>Salah: mengambil $m = -5$ sehingga diperoleh nilai terkecil, bukan terbesar</sub>

**Pembahasan:** $m - 2 = \pm 7$ sehingga $m = 9$ atau $m = -5$. $n = -3$. Nilai $m + n$ adalah $6$ atau $-8$, yang terbesar 6.
**Acuan:** siswa — siswa hal.25 Contoh 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b01-b-medium-bt01-007
*variasi (konteks) | C3 | 4 langkah | jenis: variabel di kedua ruas*

Diketahui $A = \begin{pmatrix} 2a - 3 & b + 1 \\ c & 2d \end{pmatrix}$ dan $B = \begin{pmatrix} a + 4 & 2b - 3 \\ 3 & d + 6 \end{pmatrix}$. Jika $A = B$, nilai $a + b + c + d$ adalah ....

- A. 18  
  <sub>Salah: salah mengurangkan: $b = 3 - 1 = 2$</sub>
- **B. 20** ✅  
  <sub>Benar: $2a - 3 = a + 4$ memberi $a = 7$; $b + 1 = 2b - 3$ memberi $b = 4$; $c = 3$; $2d = d + 6$ memberi $d = 6$; jumlah 20</sub>
- C. 17  
  <sub>Salah: salah menyelesaikan $2d = d + 6$ sebagai $d = 3$</sub>
- D. 14  
  <sub>Salah: salah memindahkan suku: $2a - a = 4 - 3$ sehingga $a = 1$</sub>

**Pembahasan:** Semua elemen seletak disamakan: $a = 7$, $b = 4$, $c = 3$, $d = 6$. Jumlah $= 20$.
**Acuan:** siswa — siswa hal.26 Mari Mencoba 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b01-b-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: matriks kolom*

Diketahui $A = \begin{pmatrix} p + q \\ p - q \\ 2r - 1 \end{pmatrix}$ dan $B = \begin{pmatrix} 10 \\ 4 \\ -7 \end{pmatrix}$. Jika $A = B$, nilai $pq + r$ adalah ....

- A. 24  
  <sub>Salah: salah tanda: $r = 3$ sehingga $21 + 3 = 24$</sub>
- B. 21  
  <sub>Salah: hanya menghitung $pq$ dan melupakan $r$</sub>
- **C. 18** ✅  
  <sub>Benar: $p + q = 10$ dan $p - q = 4$ memberi $p = 7$, $q = 3$; $2r - 1 = -7$ memberi $r = -3$; $pq + r = 21 - 3 = 18$</sub>
- D. 7  
  <sub>Salah: menghitung $p + q + r = 7 + 3 - 3$, bukan $pq + r$</sub>

**Pembahasan:** Dari $p + q = 10$ dan $p - q = 4$: $p = 7$, $q = 3$. Dari $2r - 1 = -7$: $r = -3$. $pq + r = 21 + (-3) = 18$.
**Acuan:** siswa — siswa hal.26 Mari Mencoba 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b01-b-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: sistem persamaan dari elemen*

Diketahui $\begin{pmatrix} 2x + y & 3 \\ 5 & x - y \end{pmatrix} = \begin{pmatrix} 11 & 3 \\ 5 & 1 \end{pmatrix}$. Nilai $x^2 + y^2$ adalah ....

- A. 49  
  <sub>Salah: mengira $x^2 + y^2 = (x + y)^2$</sub>
- B. 12  
  <sub>Salah: menghitung hasil kali $xy$, bukan $x^2 + y^2$</sub>
- **C. 25** ✅  
  <sub>Benar: $2x + y = 11$ dan $x - y = 1$ memberi $x = 4$, $y = 3$; $x^2 + y^2 = 16 + 9 = 25$</sub>
- D. 7  
  <sub>Salah: hanya menghitung $x + y$</sub>

**Pembahasan:** Elemen seletak: $2x + y = 11$ dan $x - y = 1$. Dijumlahkan: $3x = 12$ sehingga $x = 4$, $y = 3$. Maka $x^2 + y^2 = 25$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b01-b-medium-bt01-010
*orisinal | C4 | 4 langkah | jenis: kesamaan dengan transpos*

Transpos matriks $B$, ditulis $B^T$, adalah matriks yang diperoleh dengan menukar baris menjadi kolom. Diketahui $A = \begin{pmatrix} 2a & 5 \\ b - 1 & 7 \end{pmatrix}$ dan $B = \begin{pmatrix} 6 & 9 \\ 5 & 7 \end{pmatrix}$. Jika $A = B^T$, nilai $a + b$ adalah ....

- A. 12  
  <sub>Salah: lupa memindahkan $-1$: $b = 9$</sub>
- **B. 13** ✅  
  <sub>Benar: $B^T = \begin{pmatrix} 6 & 5 \\ 9 & 7 \end{pmatrix}$; $2a = 6$ memberi $a = 3$; $b - 1 = 9$ memberi $b = 10$; $a + b = 13$</sub>
- C. 9  
  <sub>Salah: lupa menukar baris dan kolom: memakai $b - 1 = 5$ sehingga $b = 6$</sub>
- D. 11  
  <sub>Salah: salah memindahkan $-1$: $b = 9 - 1 = 8$</sub>

**Pembahasan:** $B^T$ memiliki baris pertama $6, 5$ dan baris kedua $9, 7$. Elemen seletak dengan $A$: $2a = 6$, $5 = 5$, $b - 1 = 9$, $7 = 7$. Jadi $a = 3$, $b = 10$, $a + b = 13$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b01-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: parameter agar dua matriks sama*

Nilai $k$ agar $\begin{pmatrix} 2k - 1 & 7 \\ 0 & k^2 \end{pmatrix} = \begin{pmatrix} 9 & 7 \\ 0 & 25 \end{pmatrix}$ adalah ....

- A. -5  
  <sub>Salah: hanya memenuhi $k^2 = 25$ tetapi tidak memenuhi $2k - 1 = 9$</sub>
- **B. 5** ✅  
  <sub>Benar: $2k - 1 = 9$ memberi $k = 5$ dan $k^2 = 25$ juga dipenuhi oleh $k = 5$</sub>
- C. 4  
  <sub>Salah: salah memindahkan $-1$: $2k = 8$</sub>
- D. 10  
  <sub>Salah: lupa membagi 2: $2k = 10$ dianggap $k = 10$</sub>

**Pembahasan:** Elemen seletak: $2k - 1 = 9$ sehingga $k = 5$. Cek $k^2 = 25$, terpenuhi. $k = -5$ gagal pada elemen pertama.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b01-b-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: persamaan kuadrat pada elemen*

Diketahui $\begin{pmatrix} k^2 - 5k & 3 \\ 0 & k \end{pmatrix} = \begin{pmatrix} -6 & 3 \\ 0 & 2 \end{pmatrix}$. Nilai $k$ yang memenuhi kesamaan tersebut adalah ....

- A. 3  
  <sub>Salah: akar persamaan pertama tetapi tidak memenuhi $k = 2$ pada elemen baris 2 kolom 2</sub>
- **B. 2** ✅  
  <sub>Benar: $k^2 - 5k = -6$ memberi $k = 2$ atau $k = 3$, tetapi elemen lain mensyaratkan $k = 2$; hanya $k = 2$ yang memenuhi kedua elemen</sub>
- C. -2  
  <sub>Salah: salah tanda akar saat memfaktorkan</sub>
- D. 6  
  <sub>Salah: memakai hasil kali kedua akar, bukan nilai $k$</sub>

**Pembahasan:** $k^2 - 5k + 6 = 0$ memberi $(k - 2)(k - 3) = 0$, sehingga $k = 2$ atau $k = 3$. Elemen baris 2 kolom 2: $k = 2$. Jadi $k = 2$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b01-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: ordo dua matriks sama*

Matriks $A$ berordo $(2m - 1) \times (3n + 2)$ dan matriks $B$ berordo $9 \times 11$. Jika $A = B$, nilai $mn$ adalah ....

- A. 8  
  <sub>Salah: menjumlahkan $m + n$, bukan mengalikan</sub>
- B. 45  
  <sub>Salah: lupa membagi 3: $n = 9$ sehingga $mn = 45$</sub>
- **C. 15** ✅  
  <sub>Benar: ordo sama: $2m - 1 = 9$ memberi $m = 5$ dan $3n + 2 = 11$ memberi $n = 3$; $mn = 15$</sub>
- D. 12  
  <sub>Salah: salah memindahkan $-1$: $m = 4$ sehingga $mn = 12$</sub>

**Pembahasan:** Syarat pertama kesamaan: ordo sama. Banyak baris $2m - 1 = 9$ sehingga $m = 5$; banyak kolom $3n + 2 = 11$ sehingga $n = 3$. $mn = 15$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b01-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: soal cerita*

Toko A dan Toko B menjual dua jenis barang dengan harga (dalam ribuan rupiah) yang sama. Daftar harga Toko A disajikan dalam matriks $A = \begin{pmatrix} 25 & 2x + 5 \\ 30 & 3y - 1 \end{pmatrix}$ dan Toko B dalam matriks $B = \begin{pmatrix} 25 & 45 \\ 30 & 38 \end{pmatrix}$. Nilai $x + y$ adalah ....

- A. 59  
  <sub>Salah: lupa membagi 3: $3y = 39$ dianggap $y = 39$</sub>
- B. 53  
  <sub>Salah: lupa membagi 2: $2x = 40$ dianggap $x = 40$</sub>
- **C. 33** ✅  
  <sub>Benar: harga sama berarti $A = B$: $2x + 5 = 45$ memberi $x = 20$ dan $3y - 1 = 38$ memberi $y = 13$; $x + y = 33$</sub>
- D. 38  
  <sub>Salah: salah membagi: $2x = 50$ sehingga $x = 25$</sub>

**Pembahasan:** Harga kedua toko sama sehingga $A = B$. $2x + 5 = 45$ memberi $x = 20$; $3y - 1 = 38$ memberi $y = 13$. Jadi $x + y = 33$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b01-b-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: variabel di kedua ruas*

Diketahui $A = \begin{pmatrix} x + 2 & 3y \\ 7 & 1 \end{pmatrix}$ dan $B = \begin{pmatrix} y + 5 & 12 \\ 7 & 1 \end{pmatrix}$. Jika $A = B$, nilai $xy$ adalah ....

- A. 44  
  <sub>Salah: salah memindahkan suku: $x = y + 7 = 11$</sub>
- B. 11  
  <sub>Salah: menjumlahkan $x + y$, bukan mengalikan</sub>
- C. 36  
  <sub>Salah: lupa mengurangkan 2: $x = 9$ sehingga $xy = 36$</sub>
- **D. 28** ✅  
  <sub>Benar: $3y = 12$ memberi $y = 4$; $x + 2 = y + 5$ memberi $x = 7$; $xy = 28$</sub>

**Pembahasan:** Elemen $(1,2)$: $3y = 12$, $y = 4$. Elemen $(1,1)$: $x + 2 = 4 + 5 = 9$, $x = 7$. $xy = 28$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b01-b-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: kesamaan dengan matriks identitas*

Diketahui $A = \begin{pmatrix} x + y & 0 & z + 1 \\ 0 & 3x + 4y & 0 \\ 0 & 0 & z^2 \end{pmatrix}$ dan $I$ adalah matriks identitas berordo $3 \times 3$. Jika $A = I$ dan $z < 0$, nilai $xyz$ adalah ....

- A. 3  
  <sub>Salah: hanya memberikan nilai $x$</sub>
- B. -1  
  <sub>Salah: hanya memberikan nilai $z$</sub>
- C. -6  
  <sub>Salah: mengabaikan syarat $z < 0$: memakai $z = 1$</sub>
- **D. 6** ✅  
  <sub>Benar: $x + y = 1$ dan $3x + 4y = 1$ memberi $x = 3$, $y = -2$; $z^2 = 1$ dengan $z < 0$ memberi $z = -1$ (dan $z + 1 = 0$ terpenuhi); $xyz = 6$</sub>

**Pembahasan:** Matriks identitas: diagonal 1, lainnya 0. $x + y = 1$, $3x + 4y = 1$ sehingga $y = -2$, $x = 3$. $z^2 = 1$ dan $z < 0$ sehingga $z = -1$. $xyz = 3 \times (-2) \times (-1) = 6$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b01-b-medium-bt01-017
*orisinal | C3 | 4 langkah | jenis: matriks dengan rumus elemen*

Matriks $A = (a_{ij})$ berordo $2 \times 2$ dengan $a_{ij} = (i + j)^2$. Jika $A = \begin{pmatrix} p^2 & 3q \\ r + 2 & 4s \end{pmatrix}$ dan $p > 0$, nilai $p + q + r + s$ adalah ....

- **A. 16** ✅  
  <sub>Benar: $A = \begin{pmatrix} 4 & 9 \\ 9 & 16 \end{pmatrix}$; $p = 2$, $q = 3$, $r = 7$, $s = 4$; jumlah 16</sub>
- B. 18  
  <sub>Salah: lupa mengurangkan 2: $r = 9$</sub>
- C. 28  
  <sub>Salah: lupa membagi 4: $s = 16$</sub>
- D. 12  
  <sub>Salah: mengabaikan syarat $p > 0$: memakai $p = -2$</sub>

**Pembahasan:** $a_{11} = 4$, $a_{12} = 9$, $a_{21} = 9$, $a_{22} = 16$. Maka $p^2 = 4$ ($p = 2$), $3q = 9$ ($q = 3$), $r + 2 = 9$ ($r = 7$), $4s = 16$ ($s = 4$). Jumlah 16.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b01-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: soal cerita*

Catatan penjualan buah (dalam kg) pada hari Senin dan Selasa ternyata sama. Penjualan hari Senin ditulis $P = \begin{pmatrix} 3x + 2 & 20 \\ 15 & 2y - 4 \end{pmatrix}$ dan hari Selasa ditulis $Q = \begin{pmatrix} 17 & 20 \\ 15 & 26 \end{pmatrix}$. Nilai $y - x$ adalah ....

- **A. 10** ✅  
  <sub>Benar: $P = Q$: $3x + 2 = 17$ memberi $x = 5$ dan $2y - 4 = 26$ memberi $y = 15$; $y - x = 10$</sub>
- B. 6  
  <sub>Salah: salah memindahkan $-4$: $y = 11$</sub>
- C. 20  
  <sub>Salah: menjumlahkan $x + y$, bukan menghitung selisih</sub>
- D. -10  
  <sub>Salah: membalik urutan pengurangan: $x - y$</sub>

**Pembahasan:** $3x = 15$ sehingga $x = 5$; $2y = 30$ sehingga $y = 15$. $y - x = 10$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b01-b-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: variabel di kedua ruas*

Diketahui $P = \begin{pmatrix} 2x & k + 1 \\ y & 4 \end{pmatrix}$ dan $Q = \begin{pmatrix} x + 3 & 9 \\ 5 & y - 1 \end{pmatrix}$. Jika $P = Q$, nilai $xy + k$ adalah ....

- A. 24  
  <sub>Salah: lupa mengurangkan 1: $k = 9$</sub>
- B. 7  
  <sub>Salah: mengurangkan $xy - k$, bukan menjumlahkan</sub>
- C. 15  
  <sub>Salah: hanya menghitung $xy$ dan melupakan $k$</sub>
- **D. 23** ✅  
  <sub>Benar: $2x = x + 3$ memberi $x = 3$; $y = 5$ (dan $4 = y - 1$ terpenuhi); $k + 1 = 9$ memberi $k = 8$; $xy + k = 15 + 8 = 23$</sub>

**Pembahasan:** $x = 3$, $y = 5$, $k = 8$. $xy + k = 23$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b01-b-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: variabel di kedua ruas*

Diketahui $A = \begin{pmatrix} 3 & x \\ y & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2y - 1 \\ x - 6 & 5 \end{pmatrix}$. Jika $A = B$, nilai $2x - y$ adalah ....

- A. -17  
  <sub>Salah: salah tanda: $y = x + 6$ sehingga $x = -11$, $y = -5$</sub>
- B. 13  
  <sub>Salah: salah menjabarkan: $x = 2x - 6 - 1$ sehingga $x = 7$, $y = 1$</sub>
- **C. 19** ✅  
  <sub>Benar: $x = 2y - 1$ dan $y = x - 6$; substitusi memberi $x = 2(x - 6) - 1$ sehingga $x = 13$, $y = 7$; $2x - y = 19$</sub>
- D. 20  
  <sub>Salah: menjumlahkan $x + y$, bukan menghitung $2x - y$</sub>

**Pembahasan:** Elemen $(1,2)$: $x = 2y - 1$. Elemen $(2,1)$: $y = x - 6$. Substitusi: $x = 2(x - 6) - 1 = 2x - 13$ sehingga $x = 13$, $y = 7$. $2x - y = 19$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b01-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim jumlah elemen*

Diketahui $A = \begin{pmatrix} 1 & 4 \\ 3 & 2 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & 3 \\ 4 & 2 \end{pmatrix}$. Seorang siswa berpendapat bahwa $A = B$ karena kedua matriks berordo sama dan jumlah semua elemennya sama. Pernyataan yang benar mengenai pendapat tersebut adalah ....

- **A. $A \neq B$, sebab $a_{12} = 4$ berbeda dengan $b_{12} = 3$ walaupun ordo dan jumlah semua elemennya sama** ✅  
  <sub>Benar: kesamaan menuntut semua elemen seletak bernilai sama; elemen baris 1 kolom 2 berbeda ($4 \neq 3$), sehingga $A \neq B$</sub>
- B. $A = B$, sebab kedua matriks memuat elemen-elemen yang sama dan hanya urutannya berbeda  
  <sub>Salah: mengabaikan bahwa elemen harus sama pada posisi seletak</sub>
- C. $A = B$, sebab ordo sama dan jumlah semua elemen sama ($10$)  
  <sub>Salah: menganggap ordo dan jumlah elemen cukup sebagai syarat kesamaan</sub>
- D. $A \neq B$, sebab ordo $A$ berbeda dengan ordo $B$  
  <sub>Salah: salah mengira ordo berbeda; keduanya berordo $2 	imes 2$</sub>

**Pembahasan:** Ordo keduanya $2 \times 2$ dan jumlah elemennya $10$, tetapi $a_{12} = 4 \neq 3 = b_{12}$ dan $a_{21} = 3 \neq 4 = b_{21}$. Syarat elemen seletak tidak terpenuhi, jadi $A \neq B$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b01-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Klaim: "Jika dua matriks berordo sama dan jumlah semua elemennya sama, maka kedua matriks itu sama." Pasangan matriks yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 & 7 & 6 \end{pmatrix}$  
  <sub>Salah: ordo berbeda ($2 	imes 2$ dan $1 	imes 4$), hipotesis tidak terpenuhi</sub>
- **B. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 6 & 7 \\ 2 & 5 \end{pmatrix}$** ✅  
  <sub>Benar: keduanya berordo $2 \times 2$ dengan jumlah elemen $20$ (hipotesis terpenuhi), tetapi $5 \neq 6$ pada elemen seletak (kesimpulan salah)</sub>
- C. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$  
  <sub>Salah: kedua matriks sama, justru sesuai dengan klaim sehingga bukan penyangkal</sub>
- D. $\begin{pmatrix} 5 & 2 \\ 7 & 6 \end{pmatrix}$ dan $\begin{pmatrix} 5 & 2 \\ 7 & 7 \end{pmatrix}$  
  <sub>Salah: jumlah elemen berbeda ($20$ dan $21$), hipotesis tidak terpenuhi sehingga bukan penyangkal</sub>

**Pembahasan:** Penyangkal harus memenuhi syarat klaim (ordo sama, jumlah elemen sama) tetapi kedua matriks tidak sama. Hanya pasangan pertama yang demikian: jumlah elemen $20$ untuk keduanya dan $5 \neq 6$ pada baris 1 kolom 1.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b01-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan ordo*

Seorang siswa menyimpulkan $A = B$ untuk $A = \begin{pmatrix} 3 & 1 & 4 \\ 2 & 5 & 6 \end{pmatrix}$ dan $B = \begin{pmatrix} 3 & 2 \\ 1 & 5 \\ 4 & 6 \end{pmatrix}$ dengan alasan keenam elemennya sama. Pernyataan yang benar mengenai kesimpulan siswa itu adalah ....

- **A. salah, sebab $A$ berordo $2 \times 3$ sedangkan $B$ berordo $3 \times 2$ sehingga syarat ordo yang sama tidak terpenuhi** ✅  
  <sub>Benar: kesamaan dua matriks mensyaratkan ordo sama lebih dulu; $2 \times 3 \neq 3 \times 2$, jadi $A \neq B$</sub>
- B. salah, sebab elemen $1$ dan $2$ seharusnya diurutkan menaik pada $B$  
  <sub>Salah: mengira kesamaan menuntut elemen terurut, padahal syaratnya ordo dan elemen seletak</sub>
- C. benar, sebab banyak elemen kedua matriks sama yaitu $6$  
  <sub>Salah: mengira banyak elemen yang sama menggantikan syarat ordo</sub>
- D. benar, sebab kedua matriks memuat elemen yang sama persis  
  <sub>Salah: mengira kesamaan cukup dengan elemen yang sama tanpa memperhatikan ordo</sub>

**Pembahasan:** Syarat pertama: ordo sama. $A$ memiliki 2 baris dan 3 kolom, $B$ memiliki 3 baris dan 2 kolom. Ordo berbeda, sehingga $A \neq B$ walaupun semua elemennya muncul pada kedua matriks.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b01-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: syarat ordo dan elemen sekaligus*

Matriks $A$ berordo $(p + 1) \times (2p - 1)$ dan $B = \begin{pmatrix} 4 & 1 & 7 \\ 2 & 9 & 5 \end{pmatrix}$. Pernyataan yang benar mengenai nilai $p$ agar $A = B$ adalah ....

- A. $p = 2$, sebab banyak kolom sudah sama  
  <sub>Salah: hanya memeriksa banyak kolom dan melupakan banyak baris</sub>
- B. $p = 1$, sebab banyak baris sudah sama  
  <sub>Salah: hanya memeriksa banyak baris dan melupakan banyak kolom</sub>
- C. $p = 3$, sebab $p + 1 = 4$ dan $2p - 1 = 5$ jika dijumlahkan menghasilkan ordo yang cocok  
  <sub>Salah: salah memahami syarat ordo dengan menjumlahkan ordo</sub>
- **D. tidak ada $p$ yang memenuhi, sebab banyak baris menuntut $p = 1$ sedangkan banyak kolom menuntut $p = 2$** ✅  
  <sub>Benar: $p + 1 = 2$ memberi $p = 1$, $2p - 1 = 3$ memberi $p = 2$; kedua syarat ordo tidak dapat dipenuhi bersama</sub>

**Pembahasan:** Ordo $B$ adalah $2 \times 3$. Baris: $p + 1 = 2$ sehingga $p = 1$. Kolom: $2p - 1 = 3$ sehingga $p = 2$. Tidak ada $p$ yang memenuhi keduanya, jadi $A \neq B$ untuk setiap $p$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b01-b-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim syarat parameter*

Diketahui $A = \begin{pmatrix} x & 2 \\ 3 & y \end{pmatrix}$ dan $B = \begin{pmatrix} y & 2 \\ 3 & x \end{pmatrix}$ dengan $x$ dan $y$ bilangan real. Pernyataan yang benar adalah ....

- **A. $A = B$ tepat ketika $x = y$** ✅  
  <sub>Benar: elemen $2$ dan $3$ selalu sama; baris 1 kolom 1 menuntut $x = y$ dan baris 2 kolom 2 menuntut $y = x$ (syarat yang sama)</sub>
- B. $A \neq B$ untuk semua bilangan real $x$ dan $y$  
  <sub>Salah: mengira tertukarnya posisi $x$ dan $y$ selalu membuat matriks berbeda</sub>
- C. $A = B$ untuk semua bilangan real $x$ dan $y$  
  <sub>Salah: mengira matriks yang memuat elemen sama selalu sama tanpa melihat posisi</sub>
- D. $A = B$ hanya jika $x = y = 2$  
  <sub>Salah: mengira nilai $x$ dan $y$ harus sama dengan elemen lain pada matriks</sub>

**Pembahasan:** Elemen seletak: $x = y$, $2 = 2$, $3 = 3$, $y = x$. Satu-satunya syarat adalah $x = y$, sehingga $A = B$ tepat ketika $x = y$ (misalnya $x = y = 5$).
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b01-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: banyak nilai parameter*

Diketahui $A = \begin{pmatrix} k^2 & 7 \\ 3 & 4k \end{pmatrix}$ dan $B = \begin{pmatrix} 5k & 7 \\ 3 & 4k \end{pmatrix}$. Banyak nilai real $k$ yang membuat $A = B$ adalah ....

- A. $3$  
  <sub>Salah: memasukkan $k = -5$ yang tidak memenuhi $k^2 = 5k$</sub>
- B. $1$  
  <sub>Salah: membagi kedua ruas dengan $k$ sehingga akar $k = 0$ hilang</sub>
- C. $4$  
  <sub>Salah: mengira $k^2 = 5k$ memberi $k = \pm 0$ dan $k = \pm 5$</sub>
- **D. $2$** ✅  
  <sub>Benar: hanya elemen baris 1 kolom 1 yang menjadi syarat: $k^2 = 5k$ memberi $k = 0$ atau $k = 5$; elemen lain sudah sama untuk setiap $k$</sub>

**Pembahasan:** Elemen $(1,2)$, $(2,1)$, dan $(2,2)$ sama untuk setiap $k$. Syarat tersisa $k^2 = 5k$, yaitu $k(k - 5) = 0$, sehingga $k = 0$ atau $k = 5$. Ada $2$ nilai.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b01-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: pencacahan pasangan nilai*

Diketahui $A = \begin{pmatrix} x^2 - 4 & y \\ 0 & 5 \end{pmatrix}$ dan $B = \begin{pmatrix} 0 & y^3 \\ 0 & 5 \end{pmatrix}$. Banyak pasangan terurut $(x, y)$ bilangan real yang membuat $A = B$ adalah ....

- A. $2$  
  <sub>Salah: hanya menghitung banyak nilai $x$ dan menganggap $y$ tunggal</sub>
- B. $5$  
  <sub>Salah: menjumlahkan banyak nilai $x$ dan $y$ ($2 + 3$), bukan mengalikan</sub>
- **C. $6$** ✅  
  <sub>Benar: $x^2 - 4 = 0$ memberi $x = 2$ atau $x = -2$; $y = y^3$ memberi $y = 0$, $1$, atau $-1$; syarat $x$ dan $y$ bebas sehingga ada $2 \times 3 = 6$ pasangan</sub>
- D. $3$  
  <sub>Salah: hanya menghitung banyak nilai $y$</sub>

**Pembahasan:** Elemen $(1,1)$: $x^2 = 4$ sehingga dua nilai $x$. Elemen $(1,2)$: $y^3 - y = 0$, $y(y - 1)(y + 1) = 0$ sehingga tiga nilai $y$. Kedua syarat tidak saling bergantung, jadi ada $2 \times 3 = 6$ pasangan.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b01-b-hard-bt01-008
*orisinal | C6 | 4 langkah | jenis: pencacahan matriks*

Matriks $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ dengan $a, b, c, d \in \{1, 2, 3\}$ dan $N = \begin{pmatrix} b & a \\ d & c \end{pmatrix}$. Banyak matriks $M$ yang memenuhi $M = N$ adalah ....

- A. $6$  
  <sub>Salah: mengira $a$ dan $c$ harus berbeda ($3 	imes 2$)</sub>
- **B. $9$** ✅  
  <sub>Benar: $M = N$ memberi $a = b$ dan $c = d$; $a$ dan $c$ masing-masing bebas dari $\{1, 2, 3\}$ sehingga $3 \times 3 = 9$</sub>
- C. $27$  
  <sub>Salah: hanya menerapkan $a = b$ lalu memilih $a, c, d$ bebas ($3^3$)</sub>
- D. $3$  
  <sub>Salah: hanya menghitung satu pasangan ($a = b$) dan melupakan pasangan $c = d$</sub>

**Pembahasan:** Kesamaan elemen seletak: $a = b$, $b = a$, $c = d$, $d = c$. Syaratnya hanya $a = b$ dan $c = d$. Pilihan $a$ ada 3 dan pilihan $c$ ada 3, jadi $9$ matriks.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b01-b-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: kesamaan berantai*

Diketahui $A = \begin{pmatrix} 2a & b \\ 4 & c + 1 \end{pmatrix}$, $B = \begin{pmatrix} p & 5 \\ d & 9 \end{pmatrix}$, dan $C = \begin{pmatrix} 6 & q - 1 \\ 4 & r \end{pmatrix}$. Jika $A = B$ dan $B = C$, nilai $a + b + c + q + r$ adalah ....

- A. $22$  
  <sub>Salah: tidak menyertakan $r$ dalam jumlah</sub>
- B. $34$  
  <sub>Salah: lupa membagi $2$: $a = p = 6$</sub>
- **C. $31$** ✅  
  <sub>Benar: $A = B$ memberi $b = 5$, $c = 8$, $d = 4$, $p = 2a$; $B = C$ memberi $p = 6$ sehingga $a = 3$, $q = 6$, $r = 9$; jumlah $3 + 5 + 8 + 6 + 9 = 31$</sub>
- D. $30$  
  <sub>Salah: lupa menambah $1$: $q = 5$</sub>

**Pembahasan:** Dari $B = C$: $p = 6$, $5 = q - 1$ sehingga $q = 6$, $d = 4$, $9 = r$. Dari $A = B$: $2a = p = 6$ sehingga $a = 3$, $b = 5$, $c + 1 = 9$ sehingga $c = 8$. Jumlah $= 31$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b01-b-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: elemen saling bergantung*

Matriks $\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} b + 1 & c + 1 \\ d + 1 & 2 \end{pmatrix}$ dengan $a, b, c, d$ bilangan real. Nilai $a + b + c + d$ adalah ....

- A. $11$  
  <sub>Salah: lupa menambah $1$ pada $c$: $c = 2$ sehingga $b = 3$, $a = 4$</sub>
- **B. $14$** ✅  
  <sub>Benar: $d = 2$, $c = d + 1 = 3$, $b = c + 1 = 4$, $a = b + 1 = 5$; jumlah $14$</sub>
- C. $10$  
  <sub>Salah: mengira $d = 1$ (elemen $2$ dikurangi $1$): $c = 2$, $b = 3$, $a = 4$</sub>
- D. $120$  
  <sub>Salah: mengalikan $a \cdot b \cdot c \cdot d$, bukan menjumlahkan</sub>

**Pembahasan:** Elemen seletak: $d = 2$, $c = d + 1 = 3$, $b = c + 1 = 4$, $a = b + 1 = 5$. Jumlah $5 + 4 + 3 + 2 = 14$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
