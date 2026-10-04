# Lembar koreksi — kelas11_tl SMA11L-B1 subbab E: Determinan Matriks dan Invers Matriks

54 soal | easy 20, medium 20, hard 14 | variasi 18, orisinal 36
> **Kapasitas kurang (hard): 14 dari kuota 20** — Hard bermakna hanya lewat penalaran sifat |AB|=|A||B|, |kA|, invers, adjoin, syarat Cramer, parameter dua syarat, dan contoh penyangkal; materi inti (hitung determinan/invers/SPL) sudah habis terpakai di easy dan medium (40 soal) dan bentuk lain akan nyaris kembar atau di luar subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b01-e-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: sifat determinan*

Misalkan $A$ dan $B$ dua matriks persegi dengan ordo yang sama. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....

- **A. $|AB| = |A|\,|B|$** ✅  
  <sub>Benar: sesuai Sifat 1.4: determinan hasil kali sama dengan hasil kali determinan</sub>
- B. $|A+B| = |A| + |B|$  
  <sub>Salah: mengira determinan bersifat linear terhadap penjumlahan</sub>
- C. $|AB| = |A| + |B|$  
  <sub>Salah: mengganti operasi kali dengan tambah</sub>
- D. $|A+B| = |A|\,|B|$  
  <sub>Salah: mencampur sifat penjumlahan matriks dengan perkalian determinan</sub>

**Pembahasan:** Sifat 1.4: $|AB| = |A||B|$ untuk matriks persegi berordo sama. Determinan tidak aditif, jadi pernyataan lain tidak berlaku umum.
**Acuan:** siswa — siswa hal.52 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b01-e-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: sifat determinan*

Dua matriks persegi $A$ dan $B$ yang berordo sama memiliki $|A| = 3$ dan $|B| = -4$. Nilai $|AB|$ adalah ....

- A. $7$  
  <sub>Salah: mengurangkan, $3 - (-4)$</sub>
- B. $12$  
  <sub>Salah: melupakan tanda negatif pada $|B|$</sub>
- C. $-1$  
  <sub>Salah: menjumlahkan determinan, $3 + (-4)$</sub>
- **D. $-12$** ✅  
  <sub>Benar: $|AB| = |A||B| = 3 \times (-4) = -12$</sub>

**Pembahasan:** Berdasarkan $|AB| = |A||B|$, maka $|AB| = 3 \times (-4) = -12$.
**Acuan:** siswa — siswa hal.52 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b01-e-easy-bt01-003
*variasi (konteks) | C2 | 2 langkah | jenis: sifat determinan*

Matriks $A$ berordo $2 \times 2$ dan $|A| = 5$. Nilai $|3A|$ adalah ....

- A. $135$  
  <sub>Salah: memangkatkan $k$ dengan 3, bukan dengan ordo 2</sub>
- B. $30$  
  <sub>Salah: mengalikan ordo, skalar, dan determinan: $2 \cdot 3 \cdot 5$</sub>
- C. $15$  
  <sub>Salah: memakai $k|A|$, lupa memangkatkan $k$ dengan ordo</sub>
- **D. $45$** ✅  
  <sub>Benar: $|3A| = 3^2 \cdot 5 = 45$</sub>

**Pembahasan:** Untuk matriks berordo $n \times n$ berlaku $|kA| = k^n|A|$. Maka $|3A| = 3^2 \times 5 = 45$.
**Acuan:** siswa — siswa hal.48 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b01-e-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: sifat determinan*

Matriks $C$ berordo $3 \times 3$ dan $|C| = 2$. Nilai $|2C|$ adalah ....

- A. $64$  
  <sub>Salah: memangkatkan hasil $k|C|$: $(2 \cdot 2)^3$</sub>
- B. $8$  
  <sub>Salah: hanya menghitung $2^3$ dan melupakan $|C|$</sub>
- **C. $16$** ✅  
  <sub>Benar: $|2C| = 2^3 \cdot 2 = 16$</sub>
- D. $4$  
  <sub>Salah: memakai $k|C|$, lupa memangkatkan $k$</sub>

**Pembahasan:** Berlaku $|kC| = k^n|C|$ dengan $n = 3$: $|2C| = 2^3 \times 2 = 16$.
**Acuan:** siswa — siswa hal.48 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b01-e-easy-bt01-005
*variasi (konteks) | C2 | 1 langkah | jenis: sifat determinan*

Matriks persegi $A$, $B$, dan $C$ berordo sama dengan $|A| = 2$, $|B| = -3$, dan $|C| = 4$. Nilai $|ABC|$ adalah ....

- A. $24$  
  <sub>Salah: melupakan tanda negatif pada $|B|$</sub>
- B. $-6$  
  <sub>Salah: hanya mengalikan $|A|$ dan $|B|$, melupakan $|C|$</sub>
- **C. $-24$** ✅  
  <sub>Benar: $|ABC| = |A||B||C| = 2 \times (-3) \times 4 = -24$</sub>
- D. $3$  
  <sub>Salah: menjumlahkan ketiga determinan</sub>

**Pembahasan:** Dengan sifat determinan hasil kali: $|ABC| = 2 \times (-3) \times 4 = -24$.
**Acuan:** siswa — siswa hal.48 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b01-e-easy-bt01-006
*variasi (konteks) | C1 | 1 langkah | jenis: sifat invers*

Jika $A$ dan $B$ matriks persegi berordo sama yang masing-masing mempunyai invers, maka $(AB)^{-1}$ sama dengan ....

- A. $A^{-1}B^{-1}$  
  <sub>Salah: tidak membalik urutan perkalian</sub>
- B. $(A+B)^{-1}$  
  <sub>Salah: mengganti perkalian dengan penjumlahan di dalam tanda invers</sub>
- **C. $B^{-1}A^{-1}$** ✅  
  <sub>Benar: invers hasil kali membalik urutan faktor: $(AB)^{-1} = B^{-1}A^{-1}$</sub>
- D. $A^{-1} + B^{-1}$  
  <sub>Salah: mengira invers hasil kali menjadi jumlah invers</sub>

**Pembahasan:** Karena $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = I$, maka $(AB)^{-1} = B^{-1}A^{-1}$.
**Acuan:** siswa — siswa hal.53 Uji Kompetensi Bab 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b01-e-easy-bt01-007
*variasi (konteks) | C1 | 1 langkah | jenis: sifat invers*

Matriks persegi $A$ mempunyai invers $A^{-1}$ dan $I$ adalah matriks identitas yang berordo sama. Hasil kali $A \cdot A^{-1}$ adalah ....

- A. matriks nol $O$  
  <sub>Salah: mengira hasil kali dengan invers menghapus semua elemen</sub>
- B. $A$  
  <sub>Salah: mengira hasil kali dengan invers mengembalikan $A$</sub>
- C. $A^{2}$  
  <sub>Salah: mengira $A^{-1}$ sama dengan $A$</sub>
- **D. $I$** ✅  
  <sub>Benar: menurut Definisi 1.10, $A \cdot A^{-1} = A^{-1} \cdot A = I$</sub>

**Pembahasan:** Definisi invers: $A \cdot A^{-1} = A^{-1} \cdot A = I$.
**Acuan:** siswa — siswa hal.53 Uji Kompetensi Bab 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b01-e-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: invers matriks 2x2*

Diketahui $X = \begin{pmatrix} 9 & 5 \\ 7 & 4 \end{pmatrix}$. Invers matriks $X$ adalah ....

- A. $\begin{pmatrix} 4 & -7 \\ -5 & 9 \end{pmatrix}$  
  <sub>Salah: memindahkan (transpos) elemen diagonal samping, bukan mengubah tandanya saja</sub>
- **B. $\begin{pmatrix} 4 & -5 \\ -7 & 9 \end{pmatrix}$** ✅  
  <sub>Benar: $|X| = 36 - 35 = 1$, lalu tukar diagonal utama dan ubah tanda diagonal samping</sub>
- C. $\begin{pmatrix} 4 & 5 \\ 7 & 9 \end{pmatrix}$  
  <sub>Salah: diagonal utama ditukar tetapi tanda diagonal samping tidak diubah</sub>
- D. $\begin{pmatrix} 9 & -5 \\ -7 & 4 \end{pmatrix}$  
  <sub>Salah: diagonal utama tidak ditukar, hanya tanda diagonal samping yang diubah</sub>

**Pembahasan:** $|X| = 9 \cdot 4 - 5 \cdot 7 = 1$. $X^{-1} = \frac{1}{1}\begin{pmatrix} 4 & -5 \\ -7 & 9 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.49 Mari Mencoba 1.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b01-e-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: invers matriks 2x2*

Diketahui $Y = \begin{pmatrix} 6 & 4 \\ 7 & 5 \end{pmatrix}$. Invers matriks $Y$ adalah ....

- **A. $\frac{1}{2}\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$** ✅  
  <sub>Benar: $|Y| = 30 - 28 = 2$, maka $Y^{-1} = \frac{1}{2}\,Adjoin(Y)$</sub>
- B. $\frac{1}{2}\begin{pmatrix} 6 & -4 \\ -7 & 5 \end{pmatrix}$  
  <sub>Salah: diagonal utama tidak ditukar</sub>
- C. $\frac{1}{2}\begin{pmatrix} 5 & 4 \\ 7 & 6 \end{pmatrix}$  
  <sub>Salah: tanda diagonal samping tidak diubah</sub>
- D. $\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{|Y|}$</sub>

**Pembahasan:** $|Y| = 6 \cdot 5 - 4 \cdot 7 = 2$. $Y^{-1} = \frac{1}{2}\begin{pmatrix} 5 & -4 \\ -7 & 6 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.49 Mari Mencoba 1.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b01-e-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: sifat invers*

Tentukan $(AB^{-1})^{-1}$ jika diketahui $A^{-1} = \begin{pmatrix} 6 & 7 \\ 0 & 8 \end{pmatrix}$ dan $B = \begin{pmatrix} 9 & 0 \\ 6 & 7 \end{pmatrix}$.

- A. $\begin{pmatrix} 96 & 48 \\ 49 & 56 \end{pmatrix}$  
  <sub>Salah: urutan tertukar sekaligus transpos</sub>
- B. $\begin{pmatrix} 54 & 36 \\ 63 & 98 \end{pmatrix}$  
  <sub>Salah: hasil benar yang barisnya dan kolomnya tertukar (transpos)</sub>
- **C. $\begin{pmatrix} 54 & 63 \\ 36 & 98 \end{pmatrix}$** ✅  
  <sub>Benar: $(AB^{-1})^{-1} = BA^{-1}$, lalu dikalikan</sub>
- D. $\begin{pmatrix} 96 & 49 \\ 48 & 56 \end{pmatrix}$  
  <sub>Salah: urutan perkalian tertukar: $A^{-1}B$</sub>

**Pembahasan:** $(AB^{-1})^{-1} = (B^{-1})^{-1}A^{-1} = BA^{-1} = \begin{pmatrix} 54 & 63 \\ 36 & 98 \end{pmatrix}$.
**Acuan:** pretest — kelas11_tl-b01-p0052-latihan-e-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b01-e-easy-bt01-011
*orisinal | C2 | 1 langkah | jenis: determinan 2x2*

Nilai determinan matriks $A = \begin{pmatrix} 6 & 4 \\ 3 & 5 \end{pmatrix}$ adalah ....

- A. $-18$  
  <sub>Salah: mengurangkan dalam urutan terbalik: $a_{21}a_{12} - a_{11}a_{22}$</sub>
- B. $30$  
  <sub>Salah: hanya mengalikan diagonal utama</sub>
- **C. $18$** ✅  
  <sub>Benar: $|A| = 6 \cdot 5 - 3 \cdot 4 = 18$</sub>
- D. $42$  
  <sub>Salah: menjumlahkan dua hasil kali, bukan mengurangkan</sub>

**Pembahasan:** $|A| = a_{11}a_{22} - a_{21}a_{12} = 30 - 12 = 18$.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b01-e-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: determinan 2x2*

Nilai $\det B$ untuk $B = \begin{pmatrix} -3 & 5 \\ 2 & -4 \end{pmatrix}$ adalah ....

- **A. $2$** ✅  
  <sub>Benar: $\det B = (-3)(-4) - (5)(2) = 12 - 10 = 2$</sub>
- B. $-2$  
  <sub>Salah: mengurangkan dalam urutan terbalik</sub>
- C. $22$  
  <sub>Salah: salah tanda pada $-(5)(2)$ sehingga dijumlahkan</sub>
- D. $-22$  
  <sub>Salah: salah tanda pada kedua hasil kali</sub>

**Pembahasan:** $\det B = (-3)(-4) - (5)(2) = 12 - 10 = 2$.
**Acuan:** siswa — siswa hal.43

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b01-e-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: matriks singular*

Matriks $A = \begin{pmatrix} x & 10 \\ 3 & 5 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....

- A. $\frac{3}{2}$  
  <sub>Salah: salah menempatkan elemen: $10x - 15 = 0$</sub>
- B. $30$  
  <sub>Salah: tidak membagi dengan koefisien $x$ setelah memperoleh $5x = 30$</sub>
- C. $-6$  
  <sub>Salah: salah tanda: $5x + 30 = 0$</sub>
- **D. $6$** ✅  
  <sub>Benar: singular berarti $|A| = 5x - 30 = 0$, sehingga $x = 6$</sub>

**Pembahasan:** $|A| = 5x - 30$. Singular jika $|A| = 0$, jadi $x = 6$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b01-e-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: syarat memiliki invers*

Di antara matriks berikut, matriks yang mempunyai invers adalah ....

- **A. $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$** ✅  
  <sub>Benar: $|A| = 5 \cdot 1 - 2 \cdot 3 = -1 \neq 0$, sedangkan tiga matriks lain berdeterminan 0</sub>
- B. $\begin{pmatrix} 2 & 4 \\ 3 & 6 \end{pmatrix}$  
  <sub>Salah: determinan $12 - 12 = 0$ sehingga singular; baris kedua kelipatan baris pertama</sub>
- C. $\begin{pmatrix} 1 & -2 \\ -3 & 6 \end{pmatrix}$  
  <sub>Salah: determinan $6 - 6 = 0$ sehingga singular</sub>
- D. $\begin{pmatrix} 3 & 9 \\ 1 & 3 \end{pmatrix}$  
  <sub>Salah: determinan $9 - 9 = 0$ sehingga singular</sub>

**Pembahasan:** Matriks mempunyai invers jika determinannya tidak nol. Hanya $\begin{pmatrix} 5 & 2 \\ 3 & 1 \end{pmatrix}$ berdeterminan $-1$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b01-e-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: istilah singular dan nonsingular*

Matriks persegi $A$ dengan $|A| = 0$ disebut ....

- A. matriks adjoin  
  <sub>Salah: mengira nama itu merujuk pada hasil transpos matriks kofaktor</sub>
- **B. matriks singular** ✅  
  <sub>Benar: menurut Catatan Definisi 1.10, $|A| = 0$ berarti matriks singular</sub>
- C. matriks identitas  
  <sub>Salah: mengira determinan nol berarti matriks identitas</sub>
- D. matriks nonsingular  
  <sub>Salah: tertukar dengan matriks yang determinannya tidak nol</sub>

**Pembahasan:** Matriks persegi disebut singular jika $|A| = 0$ dan nonsingular jika $|A| \neq 0$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b01-e-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: invers matriks 2x2*

Diketahui $A = \begin{pmatrix} 4 & 3 \\ 1 & 2 \end{pmatrix}$. Elemen pada baris pertama kolom kedua dari $A^{-1}$ adalah ....

- A. $\frac{3}{5}$  
  <sub>Salah: tanda elemen diagonal samping tidak diubah</sub>
- **B. $-\frac{3}{5}$** ✅  
  <sub>Benar: $|A| = 5$, $A^{-1} = \frac{1}{5}\begin{pmatrix} 2 & -3 \\ -1 & 4 \end{pmatrix}$, elemen $(1,2)$ adalah $-\frac{3}{5}$</sub>
- C. $-\frac{1}{5}$  
  <sub>Salah: mengambil elemen baris kedua kolom pertama (transpos)</sub>
- D. $-3$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{|A|}$</sub>

**Pembahasan:** $|A| = 8 - 3 = 5$, sehingga $A^{-1} = \frac{1}{5}\begin{pmatrix} 2 & -3 \\ -1 & 4 \end{pmatrix}$. Elemen baris 1 kolom 2 adalah $-\frac{3}{5}$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b01-e-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: adjoin matriks 2x2*

Untuk $A = \begin{pmatrix} 6 & -2 \\ 5 & 3 \end{pmatrix}$, matriks $Adjoin(A)$ adalah ....

- **A. $\begin{pmatrix} 3 & 2 \\ -5 & 6 \end{pmatrix}$** ✅  
  <sub>Benar: $Adjoin(A) = \begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix}$ dengan $a_{11} = 6$, $a_{12} = -2$, $a_{21} = 5$, $a_{22} = 3$</sub>
- B. $\begin{pmatrix} 3 & -5 \\ 2 & 6 \end{pmatrix}$  
  <sub>Salah: menukar letak $a_{12}$ dan $a_{21}$ (transpos), bukan mengubah tandanya</sub>
- C. $\begin{pmatrix} 3 & -2 \\ 5 & 6 \end{pmatrix}$  
  <sub>Salah: diagonal ditukar tetapi tanda diagonal samping tidak diubah</sub>
- D. $\begin{pmatrix} 6 & 2 \\ -5 & 3 \end{pmatrix}$  
  <sub>Salah: diagonal utama tidak ditukar</sub>

**Pembahasan:** Tukar diagonal utama dan ubah tanda diagonal samping: $\begin{pmatrix} 3 & 2 \\ -5 & 6 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b01-e-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: persamaan matriks AX = B*

Diketahui $A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$ dan $AX = B$ dengan $B = \begin{pmatrix} 4 \\ 9 \end{pmatrix}$. Matriks $X$ adalah ....

- A. $\begin{pmatrix} -33 \\ 14 \end{pmatrix}$  
  <sub>Salah: memakai transpos $A^{-1}$ dalam perkalian</sub>
- B. $\begin{pmatrix} 21 \\ -38 \end{pmatrix}$  
  <sub>Salah: mengabaikan tanda negatif elemen $A^{-1}$ ketika mengalikan</sub>
- C. $\begin{pmatrix} -3 \\ 2 \end{pmatrix}$  
  <sub>Salah: salah tanda pada seluruh hasil perkalian</sub>
- **D. $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$** ✅  
  <sub>Benar: $X = A^{-1}B = \begin{pmatrix} 3 \\ -2 \end{pmatrix}$</sub>

**Pembahasan:** $X = A^{-1}B$. Baris 1: $3 \cdot 4 + (-1) \cdot 9 = 3$. Baris 2: $(-5) \cdot 4 + 2 \cdot 9 = -2$.
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b01-e-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: minor dan kofaktor*

Diketahui $A = \begin{pmatrix} 2 & 1 & 3 \\ 4 & 0 & 5 \\ 1 & 6 & 2 \end{pmatrix}$. Kofaktor $k_{12}$ dari matriks $A$ adalah ....

- A. $-16$  
  <sub>Salah: menghapus baris ke-2 dan kolom ke-1 (minor $M_{21}$), bukan $M_{12}$</sub>
- **B. $-3$** ✅  
  <sub>Benar: $M_{12} = \begin{vmatrix} 4 & 5 \\ 1 & 2 \end{vmatrix} = 3$ dan $k_{12} = (-1)^{1+2} M_{12} = -3$</sub>
- C. $13$  
  <sub>Salah: salah operasi minor: $4 \cdot 2 + 5 \cdot 1$, tanda faktor $(-1)^{1+2}$ terlewat</sub>
- D. $3$  
  <sub>Salah: melupakan faktor $(-1)^{1+2}$</sub>

**Pembahasan:** Hapus baris 1 dan kolom 2: $M_{12} = 8 - 5 = 3$. Kofaktor $k_{12} = (-1)^3 \cdot 3 = -3$.
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b01-e-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: determinan 3x3 (Sarrus)*

Dengan Metode Sarrus, nilai determinan $\begin{vmatrix} 2 & 1 & 0 \\ 1 & 3 & 2 \\ 4 & 0 & 1 \end{vmatrix}$ adalah ....

- A. $14$  
  <sub>Salah: hanya menjumlahkan tiga diagonal turun, melupakan pengurangan diagonal naik</sub>
- **B. $13$** ✅  
  <sub>Benar: jumlah diagonal turun 14 dikurangi jumlah diagonal naik 1</sub>
- C. $-13$  
  <sub>Salah: mengurangkan dalam urutan terbalik (diagonal naik dikurangi diagonal turun)</sub>
- D. $15$  
  <sub>Salah: menjumlahkan keenam hasil kali tanpa pengurangan</sub>

**Pembahasan:** Diagonal turun: $2\cdot3\cdot1 + 1\cdot2\cdot4 + 0\cdot1\cdot0 = 14$. Diagonal naik: $0\cdot3\cdot4 + 2\cdot2\cdot0 + 1\cdot1\cdot1 = 1$. Determinan $= 14 - 1 = 13$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b01-e-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: determinan dari persamaan matriks*

Diketahui $A = \begin{pmatrix} 7 & 3 \\ 4 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 9 & -4 \\ 5 & 6 \end{pmatrix}$, dan matriks $C$ memenuhi $AC = B$. Nilai determinan $C$ adalah ....

- **A. $37$** ✅  
  <sub>Benar: $|A| = 2$ dan $|B| = 74$; dari $|A||C| = |B|$ diperoleh $|C| = 37$</sub>
- B. $72$  
  <sub>Salah: mengurangkan determinan, bukan membagi</sub>
- C. $76$  
  <sub>Salah: menjumlahkan determinan, bukan membagi</sub>
- D. $148$  
  <sub>Salah: mengalikan $|B|$ dengan $|A|$, bukan membagi</sub>

**Pembahasan:** $AC = B$ sehingga $|A||C| = |B|$. $|A| = 14 - 12 = 2$, $|B| = 54 + 20 = 74$, jadi $|C| = \frac{74}{2} = 37$.
**Acuan:** pretest — kelas11_tl-b01-p0052-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b01-e-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: determinan dari persamaan matriks*

Matriks $P = \begin{pmatrix} 2 & 7 \\ 3 & 6 \end{pmatrix}$ dan $Q = \begin{pmatrix} 4 & -5 \\ 6 & 6 \end{pmatrix}$. Jika matriks $R$ memenuhi $PR = Q$, nilai $|R|$ adalah ....

- **A. $-6$** ✅  
  <sub>Benar: $|P| = -9$, $|Q| = 54$, sehingga $|R| = \frac{54}{-9} = -6$</sub>
- B. $6$  
  <sub>Salah: mengabaikan tanda negatif pada $|P|$</sub>
- C. $-486$  
  <sub>Salah: mengalikan $|Q|$ dengan $|P|$, bukan membagi</sub>
- D. $63$  
  <sub>Salah: mengurangkan, $54 - (-9)$, bukan membagi</sub>

**Pembahasan:** Dari $PR = Q$ diperoleh $|P||R| = |Q|$. $|P| = 12 - 21 = -9$ dan $|Q| = 24 + 30 = 54$. Jadi $|R| = \frac{54}{-9} = -6$.
**Acuan:** pretest — kelas11_tl-b01-p0052-latihan-e-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b01-e-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: SPL tiga variabel dengan determinan*

Tabel berikut menunjukkan banyak satuan makanan yang dikonsumsi setiap bakteri per hari.

| Makanan | Strain I | Strain II | Strain III |
|---|---|---|---|
| A | 2 | 1 | 3 |
| B | 1 | 2 | 2 |
| C | 3 | 1 | 1 |

Seorang peneliti menempatkan tiga jenis bakteri dalam satu tabung. Setiap hari tersedia 630 satuan makanan A, 580 satuan makanan B, dan 590 satuan makanan C, dan semuanya habis dikonsumsi. Berdasarkan tabel, banyak bakteri Strain II adalah ....

- A. 120  
  <sub>Salah: mengambil banyak bakteri Strain I ($x$), bukan Strain II</sub>
- B. -1500  
  <sub>Salah: memakai $D_y$ tanpa membaginya dengan $D$</sub>
- **C. 150** ✅  
  <sub>Benar: model: $2x + y + 3z = 630$, $x + 2y + 2z = 580$, $3x + y + z = 590$; $D = -10$, $D_y = -1500$, $y = 150$</sub>
- D. 80  
  <sub>Salah: mengambil banyak bakteri Strain III ($z$), bukan Strain II</sub>

**Pembahasan:** Misalkan banyak bakteri Strain I, II, III adalah $x$, $y$, $z$. Model: $2x+y+3z=630$, $x+2y+2z=580$, $3x+y+z=590$. $D = -10$, $D_y = -1500$, sehingga $y = \frac{D_y}{D} = 150$.
**Acuan:** siswa — siswa hal.52 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b01-e-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: SPL tiga variabel dengan determinan*

Banyak kilogram pakan yang dihabiskan seekor ternak per bulan.

| Pakan | Ayam | Bebek | Puyuh |
|---|---|---|---|
| Dedak | 1 | 2 | 1 |
| Jagung | 2 | 1 | 3 |
| Konsentrat | 1 | 1 | 2 |

Sebuah peternakan memelihara ayam, bebek, dan puyuh. Selama sebulan, tersedia 120 kg dedak, 195 kg jagung, dan 125 kg konsentrat yang habis terpakai sesuai tabel. Banyak puyuh yang dipelihara adalah ....

- **A. 30** ✅  
  <sub>Benar: model: $a + 2b + c = 120$, $2a + b + 3c = 195$, $a + b + 2c = 125$; $D = -2$, $D_c = -60$, $c = 30$</sub>
- B. 40  
  <sub>Salah: mengambil banyak ayam, bukan puyuh</sub>
- C. 25  
  <sub>Salah: mengambil banyak bebek, bukan puyuh</sub>
- D. -60  
  <sub>Salah: memakai $D_c$ tanpa membaginya dengan $D$</sub>

**Pembahasan:** Misalkan banyak ayam, bebek, puyuh adalah $a$, $b$, $c$. Model: $a+2b+c=120$, $2a+b+3c=195$, $a+b+2c=125$. $D = -2$, $D_c = -60$, sehingga $c = \frac{D_c}{D} = 30$.
**Acuan:** siswa — siswa hal.52 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b01-e-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: jumlah invers dua matriks 2x2*

Diketahui $X = \begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$ dan $Y = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$. Matriks $X^{-1} + Y^{-1}$ adalah ....

- A. $\begin{pmatrix} \frac{7}{2} & -\frac{3}{2} \\ -7 & 4 \end{pmatrix}$  
  <sub>Salah: adjoin $Y$ ditranspos (diagonal samping saling bertukar tempat)</sub>
- B. $\begin{pmatrix} -1 & 1 \\ \frac{6}{5} & -1 \end{pmatrix}$  
  <sub>Salah: menghitung $(X+Y)^{-1}$, mengira sama dengan $X^{-1} + Y^{-1}$</sub>
- C. $\begin{pmatrix} 5 & -5 \\ -6 & 5 \end{pmatrix}$  
  <sub>Salah: lupa mengalikan adjoin $Y$ dengan $\frac{1}{|Y|}$</sub>
- **D. $\begin{pmatrix} \frac{7}{2} & -3 \\ -\frac{11}{2} & 4 \end{pmatrix}$** ✅  
  <sub>Benar: $X^{-1} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$, $Y^{-1} = \begin{pmatrix} \frac{3}{2} & -2 \\ -\frac{1}{2} & 1 \end{pmatrix}$, lalu dijumlahkan</sub>

**Pembahasan:** $|X| = 6 - 5 = 1$ sehingga $X^{-1} = \begin{pmatrix} 2 & -1 \\ -5 & 3 \end{pmatrix}$. $|Y| = 6 - 4 = 2$ sehingga $Y^{-1} = \frac{1}{2}\begin{pmatrix} 3 & -4 \\ -1 & 2 \end{pmatrix}$. Jumlahnya $\begin{pmatrix} \frac{7}{2} & -3 \\ -\frac{11}{2} & 4 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.49 Mari Mencoba 1.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b01-e-medium-bt01-006
*variasi (angka) | C4 | 3 langkah | jenis: invers jumlah dua matriks*

Diketahui $X = \begin{pmatrix} 4 & 3 \\ 1 & 1 \end{pmatrix}$ dan $Y = \begin{pmatrix} 5 & 2 \\ 3 & 2 \end{pmatrix}$. Elemen baris pertama kolom kedua dari matriks $(X + Y)^{-1}$ adalah ....

- **A. $-\frac{5}{7}$** ✅  
  <sub>Benar: $X + Y = \begin{pmatrix} 9 & 5 \\ 4 & 3 \end{pmatrix}$, $|X+Y| = 7$, $(X+Y)^{-1} = \frac{1}{7}\begin{pmatrix} 3 & -5 \\ -4 & 9 \end{pmatrix}$</sub>
- B. $-5$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{|X+Y|}$</sub>
- C. $-\frac{7}{2}$  
  <sub>Salah: memakai $X^{-1} + Y^{-1}$ sebagai pengganti $(X+Y)^{-1}$</sub>
- D. $\frac{5}{7}$  
  <sub>Salah: tanda elemen diagonal samping tidak diubah</sub>

**Pembahasan:** $X + Y = \begin{pmatrix} 9 & 5 \\ 4 & 3 \end{pmatrix}$ dengan $|X+Y| = 27 - 20 = 7$. Maka $(X+Y)^{-1} = \frac{1}{7}\begin{pmatrix} 3 & -5 \\ -4 & 9 \end{pmatrix}$ dan elemen baris 1 kolom 2 adalah $-\frac{5}{7}$.
**Acuan:** siswa — siswa hal.49 Mari Mencoba 1.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b01-e-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: determinan skalar kali matriks 3x3*

Diketahui $M = \begin{pmatrix} 2 & -1 & 4 \\ 0 & 3 & 1 \\ 5 & 2 & -2 \end{pmatrix}$. Nilai $|2M|$ adalah ....

- A. $-324$  
  <sub>Salah: memangkatkan $k$ dengan 2 (ordo dikira $2 \times 2$)</sub>
- B. $-162$  
  <sub>Salah: memakai $k|M|$, lupa memangkatkan $k$ dengan ordo</sub>
- **C. $-648$** ✅  
  <sub>Benar: $|M| = -81$ dan $|2M| = 2^3 \cdot (-81) = -648$</sub>
- D. $648$  
  <sub>Salah: salah tanda pada determinan $M$</sub>

**Pembahasan:** Dengan Metode Sarrus diperoleh $|M| = -81$. Karena $M$ berordo $3 \times 3$, $|2M| = 2^3 |M| = 8 \cdot (-81) = -648$.
**Acuan:** siswa — siswa hal.48 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b01-e-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: determinan hasil kali tiga matriks*

Diketahui $A = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 1 & -2 \\ 3 & 5 \end{pmatrix}$. Jika $C$ matriks berordo $2 \times 2$ dengan $|C| = -2$, nilai $|ABC|$ adalah ....

- A. $220$  
  <sub>Salah: mengabaikan tanda negatif pada $|C|$</sub>
- **B. $-220$** ✅  
  <sub>Benar: $|A| = 10$, $|B| = 11$, sehingga $|ABC| = 10 \cdot 11 \cdot (-2) = -220$</sub>
- C. $-20$  
  <sub>Salah: melupakan $|B|$ dalam hasil kali</sub>
- D. $19$  
  <sub>Salah: menjumlahkan ketiga determinan, $10 + 11 + (-2)$</sub>

**Pembahasan:** $|A| = 12 - 2 = 10$ dan $|B| = 5 + 6 = 11$. Karena $|ABC| = |A||B||C|$, maka $|ABC| = 10 \cdot 11 \cdot (-2) = -220$.
**Acuan:** siswa — siswa hal.48 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b01-e-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: determinan 3x3 (Sarrus)*

Dengan Metode Sarrus, nilai $\begin{vmatrix} 2 & -1 & 3 \\ 4 & 0 & -2 \\ 1 & 5 & 3 \end{vmatrix}$ adalah ....

- **A. $94$** ✅  
  <sub>Benar: diagonal turun $0 + 2 + 60 = 62$, diagonal naik $0 - 20 - 12 = -32$, determinan $62 - (-32) = 94$</sub>
- B. $30$  
  <sub>Salah: menjumlahkan jumlah diagonal naik ($-32$) tanpa mengubah tandanya: $62 + (-32)$</sub>
- C. $-94$  
  <sub>Salah: mengurangkan dalam urutan terbalik (diagonal naik dikurangi diagonal turun)</sub>
- D. $62$  
  <sub>Salah: hanya memakai tiga diagonal turun</sub>

**Pembahasan:** Diagonal turun: $2\cdot0\cdot3 + (-1)(-2)(1) + 3\cdot4\cdot5 = 62$. Diagonal naik: $3\cdot0\cdot1 + 2(-2)(5) + (-1)\cdot4\cdot3 = -32$. Determinan $= 62 - (-32) = 94$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b01-e-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: determinan 3x3 (ekspansi kofaktor)*

Determinan $\begin{vmatrix} 0 & 3 & 2 \\ 5 & 1 & -1 \\ 0 & 4 & 6 \end{vmatrix}$ jika dihitung dengan ekspansi kofaktor sepanjang kolom pertama adalah ....

- A. $50$  
  <sub>Salah: lupa faktor tanda $(-1)^{2+1}$ pada kofaktor $k_{21}$</sub>
- **B. $-50$** ✅  
  <sub>Benar: hanya $a_{21} = 5$ yang tidak nol; $M_{21} = 18 - 8 = 10$, $k_{21} = (-1)^{3} \cdot 10 = -10$, determinan $5 \cdot (-10) = -50$</sub>
- C. $-130$  
  <sub>Salah: minor dihitung dengan menjumlahkan hasil kali: $18 + 8 = 26$, lalu $5 \cdot (-26)$</sub>
- D. $-10$  
  <sub>Salah: lupa mengalikan kofaktor dengan elemen $a_{21} = 5$</sub>

**Pembahasan:** Pada kolom pertama hanya $a_{21} = 5$ yang tidak nol. $M_{21} = \begin{vmatrix} 3 & 2 \\ 4 & 6 \end{vmatrix} = 10$, $k_{21} = (-1)^{2+1} \cdot 10 = -10$. Jadi determinan $= 5 \cdot (-10) = -50$.
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b01-e-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: parameter matriks singular 3x3*

Matriks $A = \begin{pmatrix} 2 & 3 & 1 \\ 1 & x & 2 \\ 4 & 1 & 3 \end{pmatrix}$ merupakan matriks singular. Nilai $x$ adalah ....

- A. $-24$  
  <sub>Salah: mengalikan dengan 2, bukan membagi, dari $2x = -12$</sub>
- B. $-12$  
  <sub>Salah: tidak membagi dengan koefisien $x$ setelah memperoleh $2x = -12$</sub>
- **C. $-6$** ✅  
  <sub>Benar: $|A| = 2x + 12 = 0$ sehingga $x = -6$</sub>
- D. $6$  
  <sub>Salah: salah tanda: $2x - 12 = 0$</sub>

**Pembahasan:** Metode Sarrus: diagonal turun $6x + 24 + 1 = 6x + 25$, diagonal naik $4x + 4 + 9 = 4x + 13$. $|A| = 2x + 12$. Singular jika $|A| = 0$, jadi $x = -6$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b01-e-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: parameter matriks singular kuadrat*

Matriks $A = \begin{pmatrix} x & 6 \\ 1 & x - 5 \end{pmatrix}$ tidak mempunyai invers. Nilai $x$ terbesar yang mungkin adalah ....

- A. $-1$  
  <sub>Salah: mengambil akar yang lain, bukan yang terbesar</sub>
- B. $5$  
  <sub>Salah: mengambil konstanta $-5$ pada $x - 5$ sebagai nilai $x$</sub>
- **C. $6$** ✅  
  <sub>Benar: $|A| = x(x-5) - 6 = x^2 - 5x - 6 = (x-6)(x+1) = 0$, akar terbesar $6$</sub>
- D. $1$  
  <sub>Salah: salah tanda pada faktor: akar dikira $x = 1$ dan $x = -6$</sub>

**Pembahasan:** Tidak mempunyai invers berarti $|A| = 0$: $x(x-5) - 6 = x^2 - 5x - 6 = (x-6)(x+1) = 0$, sehingga $x = 6$ atau $x = -1$. Nilai terbesar adalah $6$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b01-e-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: invers 2x2 berparameter*

Diketahui $A = \begin{pmatrix} 3 & x \\ 2 & 5 \end{pmatrix}$. Jika elemen baris pertama kolom kedua dari $A^{-1}$ bernilai $2$, nilai $x$ adalah ....

- A. $8$  
  <sub>Salah: mengambil elemen baris kedua kolom pertama ($-2$) sebagai elemen yang dimaksud</sub>
- **B. $10$** ✅  
  <sub>Benar: $A^{-1} = \frac{1}{15-2x}\begin{pmatrix} 5 & -x \\ -2 & 3 \end{pmatrix}$; $\frac{-x}{15-2x} = 2$ memberi $x = 10$</sub>
- C. $30$  
  <sub>Salah: dari $3x = 30$ tidak dibagi 3</sub>
- D. $6$  
  <sub>Salah: tanda diagonal samping tidak diubah: $\frac{x}{15-2x} = 2$ memberi $x = 6$</sub>

**Pembahasan:** $|A| = 15 - 2x$ dan $A^{-1} = \frac{1}{15-2x}\begin{pmatrix} 5 & -x \\ -2 & 3 \end{pmatrix}$. Elemen $(1,2)$: $\frac{-x}{15-2x} = 2$, sehingga $-x = 30 - 4x$ dan $x = 10$. (Determinan $= -5 \neq 0$.)
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b01-e-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: persamaan matriks AX = B*

Diketahui $A = \begin{pmatrix} 2 & 1 \\ 5 & 4 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 17 & 6 \end{pmatrix}$. Matriks $X$ yang memenuhi $AX = B$ adalah ....

- A. $\begin{pmatrix} 3 & 6 \\ 9 & -3 \end{pmatrix}$  
  <sub>Salah: lupa mengalikan adjoin dengan $\frac{1}{|A|}$</sub>
- B. $\begin{pmatrix} \frac{37}{3} & 6 \\ \frac{59}{3} & 9 \end{pmatrix}$  
  <sub>Salah: diagonal samping tidak diubah tandanya saat menyusun adjoin</sub>
- **C. $\begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$** ✅  
  <sub>Benar: $A^{-1} = \frac{1}{3}\begin{pmatrix} 4 & -1 \\ -5 & 2 \end{pmatrix}$, $X = A^{-1}B$</sub>
- D. $\begin{pmatrix} \frac{5}{3} & \frac{1}{3} \\ \frac{38}{3} & -\frac{5}{3} \end{pmatrix}$  
  <sub>Salah: urutan perkalian tertukar: $BA^{-1}$</sub>

**Pembahasan:** $|A| = 8 - 5 = 3$, $A^{-1} = \frac{1}{3}\begin{pmatrix} 4 & -1 \\ -5 & 2 \end{pmatrix}$. Maka $X = A^{-1}B = \frac{1}{3}\begin{pmatrix} 4 & -1 \\ -5 & 2 \end{pmatrix}\begin{pmatrix} 5 & 3 \\ 17 & 6 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & -1 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b01-e-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: persamaan matriks XA = B*

Diketahui $A = \begin{pmatrix} 4 & 3 \\ 3 & 3 \end{pmatrix}$ dan $B = \begin{pmatrix} 5 & 3 \\ 13 & 12 \end{pmatrix}$. Matriks $X$ yang memenuhi $XA = B$ adalah ....

- A. $\begin{pmatrix} -8 & -9 \\ \frac{37}{3} & 13 \end{pmatrix}$  
  <sub>Salah: mengalikan $A^{-1}$ dari kiri, $X = A^{-1}B$, padahal persamaannya $XA = B$</sub>
- **B. $\begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$** ✅  
  <sub>Benar: $X = BA^{-1}$ dengan $A^{-1} = \frac{1}{3}\begin{pmatrix} 3 & -3 \\ -3 & 4 \end{pmatrix}$</sub>
- C. $\begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$  
  <sub>Salah: hasil benar yang barisnya dan kolomnya tertukar (transpos)</sub>
- D. $\begin{pmatrix} 6 & -3 \\ 3 & 9 \end{pmatrix}$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{|A|}$</sub>

**Pembahasan:** $XA = B$ dikalikan $A^{-1}$ dari kanan: $X = BA^{-1}$. $|A| = 12 - 9 = 3$, $A^{-1} = \frac{1}{3}\begin{pmatrix} 3 & -3 \\ -3 & 4 \end{pmatrix}$. $X = \begin{pmatrix} 5 & 3 \\ 13 & 12 \end{pmatrix} A^{-1} = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b01-e-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: soal cerita SPLDV dengan matriks*

Anto membeli 3 buku dan 2 pensil dengan membayar Rp21.000,00. Budi membeli 5 buku dan 4 pensil dengan membayar Rp37.000,00. Jika sistem persamaannya diselesaikan dengan invers matriks, harga 4 buku dan 3 pensil adalah ....

- A. Rp58.000,00  
  <sub>Salah: lupa mengalikan adjoin dengan $\frac{1}{|A|}$ sehingga harga satuan dua kali lipat</sub>
- **B. Rp29.000,00** ✅  
  <sub>Benar: $3x + 2y = 21.000$ dan $5x + 4y = 37.000$ memberi $x = 5.000$ dan $y = 3.000$; $4x + 3y = 29.000$</sub>
- C. Rp8.000,00  
  <sub>Salah: hanya menjumlahkan harga satu buku dan satu pensil</sub>
- D. Rp27.000,00  
  <sub>Salah: harga buku dan pensil tertukar: $4 \cdot 3.000 + 3 \cdot 5.000$</sub>

**Pembahasan:** Misalkan harga buku $x$ dan pensil $y$ (ribu rupiah). $\begin{pmatrix} 3 & 2 \\ 5 & 4 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 21 \\ 37 \end{pmatrix}$, $|A| = 2$, $X = \frac{1}{2}\begin{pmatrix} 4 & -2 \\ -5 & 3 \end{pmatrix}\begin{pmatrix} 21 \\ 37 \end{pmatrix} = \begin{pmatrix} 5 \\ 3 \end{pmatrix}$. Jadi $4(5.000) + 3(3.000) = 29.000$.
**Acuan:** siswa — siswa hal.42

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b01-e-medium-bt01-017
*orisinal | C3 | 4 langkah | jenis: invers matriks 3x3 (satu elemen)*

Diketahui $A = \begin{pmatrix} 1 & 2 & 1 \\ 0 & 3 & 1 \\ 2 & 1 & 4 \end{pmatrix}$. Elemen baris pertama kolom ketiga dari $A^{-1}$ adalah ....

- A. $-1$  
  <sub>Salah: lupa mengalikan dengan $\frac{1}{|A|}$</sub>
- B. $\frac{1}{9}$  
  <sub>Salah: salah tanda kofaktor</sub>
- C. $-\frac{2}{3}$  
  <sub>Salah: memakai kofaktor $k_{13} = -6$ (adjoin tidak ditranspos)</sub>
- **D. $-\frac{1}{9}$** ✅  
  <sub>Benar: $|A| = 9$; elemen $(1,3)$ dari $Adjoin(A)$ adalah kofaktor $k_{31} = (-1)^{4}\begin{vmatrix} 2 & 1 \\ 3 & 1 \end{vmatrix} = -1$, sehingga $-\frac{1}{9}$</sub>

**Pembahasan:** Dengan Sarrus $|A| = 9$. $Adjoin(A)$ adalah transpos matriks kofaktor, sehingga elemen $(1,3)$ adjoin $= k_{31} = (-1)^{3+1}M_{31} = \begin{vmatrix} 2 & 1 \\ 3 & 1 \end{vmatrix} = -1$. Jadi elemen $(1,3)$ dari $A^{-1}$ adalah $-\frac{1}{9}$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b01-e-medium-bt01-018
*orisinal | C3 | 4 langkah | jenis: aturan Cramer SPL tiga variabel*

Dengan determinan, nilai $z$ dari sistem $\begin{cases} 2x + y + z = 6 \\ x - y + 3z = 12 \\ 3x + 2y - z = 1 \end{cases}$ adalah ....

- A. $15$  
  <sub>Salah: memakai $D_z$ tanpa membaginya dengan $D$</sub>
- B. $-1$  
  <sub>Salah: mengambil nilai $y$ (kolom yang diganti tertukar)</sub>
- C. $2$  
  <sub>Salah: mengambil nilai $x$ (kolom yang diganti tertukar)</sub>
- **D. $3$** ✅  
  <sub>Benar: $D = 5$, $D_z = 15$, sehingga $z = \frac{D_z}{D} = 3$</sub>

**Pembahasan:** $D = \begin{vmatrix} 2 & 1 & 1 \\ 1 & -1 & 3 \\ 3 & 2 & -1 \end{vmatrix} = 5$. $D_z = \begin{vmatrix} 2 & 1 & 6 \\ 1 & -1 & 12 \\ 3 & 2 & 1 \end{vmatrix} = 15$. Jadi $z = \frac{15}{5} = 3$.
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b01-e-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: minor dan kofaktor berparameter*

Pada matriks $A = \begin{pmatrix} 2 & x & 1 \\ 4 & 3 & x \\ 1 & 5 & 2 \end{pmatrix}$, kofaktor $k_{23} = -4$. Nilai $x$ adalah ....

- A. $-6$  
  <sub>Salah: minor ditulis $10 + x$ sehingga $-(10 + x) = -4$</sub>
- B. $4$  
  <sub>Salah: memakai minor $M_{32}$ (baris ke-3, kolom ke-2 dihapus)</sub>
- C. $14$  
  <sub>Salah: lupa faktor $(-1)^{2+3}$: $10 - x = -4$</sub>
- **D. $6$** ✅  
  <sub>Benar: $M_{23} = \begin{vmatrix} 2 & x \\ 1 & 5 \end{vmatrix} = 10 - x$, $k_{23} = -(10 - x) = -4$ sehingga $x = 6$</sub>

**Pembahasan:** Hapus baris ke-2 dan kolom ke-3: $M_{23} = 2 \cdot 5 - x \cdot 1 = 10 - x$. $k_{23} = (-1)^{2+3}M_{23} = x - 10 = -4$, sehingga $x = 6$.
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b01-e-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: sifat determinan gabungan*

Matriks $A$ dan $B$ berordo $3 \times 3$ dengan $|A| = 2$ dan $|B| = -3$. Nilai $|2AB|$ adalah ....

- A. $-12$  
  <sub>Salah: memakai $k|AB|$, lupa memangkatkan $k$ dengan ordo</sub>
- B. $-24$  
  <sub>Salah: memangkatkan $k$ dengan 2, bukan ordo 3</sub>
- C. $48$  
  <sub>Salah: salah tanda hasil kali $|A||B|$</sub>
- **D. $-48$** ✅  
  <sub>Benar: $|2AB| = 2^3|AB| = 8 \cdot (2)(-3) = -48$</sub>

**Pembahasan:** $|AB| = |A||B| = 2 \cdot (-3) = -6$. Karena $2AB$ berordo $3 \times 3$, $|2AB| = 2^3 \cdot (-6) = -48$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b01-e-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim sifat determinan*

Misalkan $A$ dan $B$ matriks persegi berordo sama yang keduanya mempunyai invers. Pernyataan yang berlaku untuk setiap pasangan $A$ dan $B$ tersebut adalah ....

- A. $|A + B| = |A| + |B|$  
  <sub>Salah: mengira determinan bersifat linear terhadap penjumlahan</sub>
- B. $(AB)^{-1} = A^{-1}B^{-1}$  
  <sub>Salah: lupa urutan berbalik: seharusnya $B^{-1}A^{-1}$</sub>
- **C. $|AB| = |BA|$** ✅  
  <sub>Benar: $|AB| = |A||B| = |B||A| = |BA|$ karena perkalian bilangan real bersifat komutatif</sub>
- D. $AB = BA$  
  <sub>Salah: mengira perkalian matriks komutatif karena determinannya sama</sub>

**Pembahasan:** Dari $|AB| = |A||B|$ dan komutatifnya perkalian bilangan, $|AB| = |BA|$. Klaim lain memiliki penyangkal: $|A+B| \neq |A|+|B|$ pada $A=B=I_2$ ($|2I| = 4 \neq 2$), $(AB)^{-1} = B^{-1}A^{-1}$, dan $AB \ne BA$ pada umumnya.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b01-e-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: determinan invers dan skalar*

Matriks $A$ berordo $3 \times 3$ dengan $|A| = 4$. Nilai $|2A^{-1}|$ adalah ....

- A. $8$  
  <sub>Salah: mengalikan $2^3$ saja tanpa memperhitungkan $|A^{-1}|$</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: memakai $2 \cdot \frac{1}{4}$, lupa bahwa skalar dipangkatkan ordo ($2^3$)</sub>
- C. $32$  
  <sub>Salah: memakai $2^3 \cdot 4$, lupa membalik determinan untuk invers</sub>
- **D. $2$** ✅  
  <sub>Benar: $|A^{-1}| = \frac{1}{|A|} = \frac{1}{4}$, lalu $|2A^{-1}| = 2^3 \cdot \frac{1}{4} = 2$</sub>

**Pembahasan:** Dari $AA^{-1} = I$ diperoleh $|A||A^{-1}| = 1$, sehingga $|A^{-1}| = \frac{1}{4}$. Karena ordo $3$, $|2A^{-1}| = 2^3 \cdot \frac{1}{4} = 2$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b01-e-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan invers 2x2*

Seorang siswa menghitung invers dari $A = \begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}$ dan menulis $A^{-1} = \begin{pmatrix} 3 & 2 \\ 7 & 5 \end{pmatrix}$. Kesalahan siswa tersebut adalah ....

- A. elemen diagonal utama tidak ditukar  
  <sub>Salah: diagonal utama $5$ dan $3$ sudah ditukar menjadi $3$ dan $5$</sub>
- **B. elemen diagonal samping tidak diubah tandanya** ✅  
  <sub>Benar: $|A| = 15 - 14 = 1$, jadi $A^{-1} = \begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix}$; siswa sudah menukar diagonal utama tetapi lupa mengganti tanda elemen $2$ dan $7$</sub>
- C. determinan $A$ dihitung salah sehingga pengali $\frac{1}{|A|}$ keliru  
  <sub>Salah: determinannya $1$ sehingga pengali $1$ memang tidak mengubah apa pun</sub>
- D. elemen diagonal utama ikut diubah tandanya seharusnya  
  <sub>Salah: diagonal utama tidak berubah tanda pada rumus invers</sub>

**Pembahasan:** Rumus: $A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$. Hasil benar $\begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix}$, berbeda dari hasil siswa hanya pada tanda diagonal samping.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b01-e-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: temukan kesalahan ekspansi kofaktor*

Untuk $M = \begin{pmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 6 & 7 & 1 \end{pmatrix}$, seorang siswa menghitung determinan dengan ekspansi baris pertama memakai minor langsung tanpa pola tanda, yaitu $2M_{11} + 1M_{12} + 3M_{13}$. Determinan sebenarnya lebih besar daripada hasil siswa tersebut sebesar ....

- A. 30  
  <sub>Salah: memakai $|a_{12}M_{12}|$ saja, lupa selisihnya dua kali karena suku itu berganti tanda</sub>
- **B. 60** ✅  
  <sub>Benar: hasil siswa $=-164$, determinan sebenarnya $=-104$; selisih $=-2 a_{12}M_{12}=60$</sub>
- C. -104  
  <sub>Salah: mengira selisihnya sama dengan determinan sebenarnya</sub>
- D. -60  
  <sub>Salah: membalik arah selisih (hasil siswa dikurangi determinan benar)</sub>

**Pembahasan:** $M_{11}=-31$, $M_{12}=-30$, $M_{13}=-24$. Siswa: $2(-31)+1(-30)+3(-24)=-164$. Benar: $2(-31)-1(-30)+3(-24)=-104$. Selisih $60$.
**Acuan:** siswa — siswa hal.45

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b01-e-hard-bt01-005
*orisinal | C5 | 6 langkah | jenis: parameter dua matriks, satu singular satu tidak*

Diketahui $A = \begin{pmatrix} x+1 & 3 \\ 2 & x \end{pmatrix}$ dan $B = \begin{pmatrix} x & 4 \\ 1 & 2 \end{pmatrix}$. Jika $A$ singular tetapi $B$ mempunyai invers, nilai $x$ yang memenuhi adalah ....

- **A. $-3$** ✅  
  <sub>Benar: $|A| = x^2 + x - 6 = 0$ memberi $x = 2$ atau $x = -3$; $|B| = 2x - 4 = 0$ saat $x = 2$, sehingga $x = 2$ membuat $B$ singular dan hanya $x = -3$ yang memenuhi</sub>
- B. $-1$  
  <sub>Salah: menjumlahkan kedua akar $2 + (-3)$ tanpa menyaring syarat $B$</sub>
- C. $6$  
  <sub>Salah: mengambil hasil kali akar sebagai jawaban ($-6$ lalu salah tanda)</sub>
- D. $2$  
  <sub>Salah: hanya memeriksa $A$ singular, lupa bahwa $x=2$ membuat $B$ ikut singular</sub>

**Pembahasan:** $|A| = x(x+1) - 6 = (x-2)(x+3)$, jadi $x = 2$ atau $x = -3$. $|B| = 2x - 4$, nol di $x = 2$. Maka $B$ punya invers hanya jika $x \ne 2$, sehingga $x = -3$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b01-e-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: matriks sama dengan inversnya*

Matriks $A = \begin{pmatrix} 2 & p \\ q & -2 \end{pmatrix}$ memenuhi $A = A^{-1}$. Nilai $pq$ adalah ....

- A. $-5$  
  <sub>Salah: memakai $|A| = 1$ (mengira $A = A^{-1}$ berarti determinan $1$) sehingga $-4 - pq = 1$</sub>
- B. $-1$  
  <sub>Salah: menyamakan $pq$ dengan $|A|$ yang bernilai $-1$</sub>
- **C. $-3$** ✅  
  <sub>Benar: $|A| = -4 - pq$ dan $A^{-1} = \frac{1}{|A|}\begin{pmatrix} -2 & -p \\ -q & 2 \end{pmatrix}$; kesamaan elemen $2 = \frac{-2}{|A|}$ memberi $|A| = -1$ sehingga $pq = -3$</sub>
- D. $3$  
  <sub>Salah: salah tanda saat memindahkan $pq$ dari $-4 - pq = -1$</sub>

**Pembahasan:** Dari $A = A^{-1}$ diperoleh $A^2 = I$: elemen diagonal $4 + pq = 1$, jadi $pq = -3$. Pemeriksaan: $|A| = -4 + 3 = -1$ dan $\frac{-2}{-1} = 2$ cocok dengan elemen $a_{11}$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b01-e-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: hubungan Adjoin dan determinan*

Matriks $A$ berordo $3 \times 3$ dengan $|A| = -3$. Karena $A^{-1} = \frac{1}{|A|}\,Adjoin(A)$, nilai $|Adjoin(A)|$ adalah ....

- A. $-9$  
  <sub>Salah: salah tanda: memakai $|A|^3 \cdot \frac{1}{|A|}$ lalu menghitung $(-3)^2$ sebagai $-9$</sub>
- B. $-3$  
  <sub>Salah: mengira determinan adjoin sama dengan determinan matriksnya</sub>
- C. $-27$  
  <sub>Salah: mengira $|Adjoin(A)| = |A|^3$ tanpa memperhitungkan $|A^{-1}|$</sub>
- **D. $9$** ✅  
  <sub>Benar: $Adjoin(A) = |A|\,A^{-1}$ sehingga $|Adjoin(A)| = |A|^3 \cdot \frac{1}{|A|} = |A|^2 = 9$</sub>

**Pembahasan:** $Adjoin(A) = |A| A^{-1}$. Untuk ordo $3$: $|Adjoin(A)| = |A|^3 |A^{-1}| = |A|^3 \cdot \frac{1}{|A|} = |A|^2 = 9$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b01-e-hard-bt01-008
*orisinal | C6 | 4 langkah | jenis: merancang matriks dengan invers bulat*

Semua elemen suatu matriks berordo $2 \times 2$ adalah bilangan bulat. Di antara matriks berikut, yang semua elemen inversnya juga bilangan bulat adalah ....

- A. $\begin{pmatrix} 5 & 2 \\ 4 & 1 \end{pmatrix}$  
  <sub>Salah: determinan $-3$ sehingga invers memuat pecahan berpenyebut $3$</sub>
- B. $\begin{pmatrix} 4 & 1 \\ 3 & 2 \end{pmatrix}$  
  <sub>Salah: determinan $5$ sehingga invers memuat pecahan berpenyebut $5$</sub>
- **C. $\begin{pmatrix} 2 & 3 \\ 3 & 4 \end{pmatrix}$** ✅  
  <sub>Benar: $|A| = 2 \cdot 4 - 3 \cdot 3 = -1$ sehingga $A^{-1} = -\begin{pmatrix} 4 & -3 \\ -3 & 2 \end{pmatrix}$ berelemen bulat</sub>
- D. $\begin{pmatrix} 3 & 4 \\ 1 & 2 \end{pmatrix}$  
  <sub>Salah: determinan $2$ sehingga invers memuat pecahan berpenyebut $2$</sub>

**Pembahasan:** Invers $= \frac{1}{|A|}\,Adjoin(A)$ dan adjoin berelemen bulat. Elemen invers bulat untuk semua entri hanya dijamin bila $|A| = \pm 1$ (di sini $-1$); determinan lain meninggalkan pecahan.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b01-e-hard-bt01-009
*orisinal | C6 | 5 langkah | jenis: syarat determinan sama dengan determinan inversnya*

Diketahui $A = \begin{pmatrix} x & x+1 \\ 1 & x \end{pmatrix}$. Banyak nilai real $x$ yang membuat $A$ mempunyai invers dengan $|A| = |A^{-1}|$ adalah ....

- **A. $4$** ✅  
  <sub>Benar: $|A| = x^2 - x - 1$ dan $|A^{-1}| = \frac{1}{|A|}$; $|A| = \frac{1}{|A|}$ memberi $|A| = 1$ atau $|A| = -1$. Kasus $1$: $x^2 - x - 2 = 0$ (dua akar $2$ dan $-1$); kasus $-1$: $x^2 - x = 0$ (dua akar $0$ dan $1$); total $4$</sub>
- B. $3$  
  <sub>Salah: menghitung akar yang sama dua kali atau melewatkan satu akar</sub>
- C. $6$  
  <sub>Salah: menambahkan akar dari kasus $|A| = 0$ yang justru membuat $A$ singular</sub>
- D. $2$  
  <sub>Salah: hanya memperhitungkan $|A| = 1$ dan melupakan $|A| = -1$</sub>

**Pembahasan:** $|A|^2 = 1$ sehingga $|A| = \pm 1$. Dua persamaan kuadrat, masing-masing dua akar berbeda ($2, -1$ dan $0, 1$), semuanya real dan berbeda, jadi $4$ nilai.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b01-e-hard-bt01-010
*orisinal | C6 | 6 langkah | jenis: contoh penyangkal pada kekeliruan menghapus faktor matriks*

Pernyataan: \"Jika $AB = AC$, maka $B = C$.\" Pernyataan ini salah. Pasangan $A$, $B$, $C$ berordo $2 \times 2$ yang merupakan contoh penyangkal pernyataan tersebut adalah ....

- A. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 5 \end{pmatrix}$  
  <sub>Salah: $AB \neq AC$ (kolom kedua $C$ diubah), sehingga premis pernyataan tidak terpenuhi</sub>
- B. $A = \begin{pmatrix} 2 & 4 \\ 1 & 3 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$  
  <sub>Salah: $A$ mempunyai invers dan $AB \neq AC$; premis tidak terpenuhi</sub>
- C. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$  
  <sub>Salah: $AB = AC$ tetapi $B = C$ sehingga bukan penyangkal</sub>
- **D. $A = \begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$, $B = \begin{pmatrix} 3 & 1 \\ 1 & 2 \end{pmatrix}$, $C = \begin{pmatrix} 1 & -3 \\ 2 & 4 \end{pmatrix}$** ✅  
  <sub>Benar: $|A| = 0$ sehingga $A$ tidak punya invers; $AB = AC = \begin{pmatrix} 10 & 10 \\ 5 & 5 \end{pmatrix}$ padahal $B \neq C$</sub>

**Pembahasan:** Bila $A$ mempunyai invers, mengalikan kedua ruas dengan $A^{-1}$ memberi $B = C$. Contoh penyangkal harus memakai $A$ singular dengan $AB = AC$ tetapi $B \neq C$.
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b01-e-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: implikasi dari A kuadrat sama dengan A*

Matriks persegi $A$ mempunyai invers dan memenuhi $A^2 = A$. Kesimpulan yang pasti benar adalah ....

- A. $|A| = 0$  
  <sub>Salah: matriks yang mempunyai invers pasti determinannya tidak nol</sub>
- B. $|A| = 2$  
  <sub>Salah: dari $|A|^2 = |A|$ diperoleh $|A| = 1$ (bukan $2$)</sub>
- C. $A = O$  
  <sub>Salah: $O$ tidak mempunyai invers (determinan $0$), bertentangan dengan premis</sub>
- **D. $A = I$** ✅  
  <sub>Benar: Kalikan kedua ruas $A^2 = A$ dengan $A^{-1}$: $A = I$</sub>

**Pembahasan:** $A^{-1}A^2 = A^{-1}A$ memberi $A = I$. Cek determinan: $|A|^2 = |A|$ dan $|A| \neq 0$ menghasilkan $|A| = 1$, konsisten dengan $A = I$.
**Acuan:** siswa — siswa hal.49

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b01-e-hard-bt01-012
*orisinal | C5 | 3 langkah | jenis: syarat Aturan Cramer pada SPL tiga variabel*

Sebuah sistem persamaan linear tiga variabel mempunyai $D = D_x = D_y = D_z = 0$. Pernyataan yang pasti benar tentang sistem tersebut adalah ....

- **A. sistem tidak mungkin mempunyai tepat satu penyelesaian** ✅  
  <sub>Benar: Penyelesaian tunggal mensyaratkan $D \neq 0$; karena $D = 0$ sistem tidak punya tepat satu penyelesaian (tidak ada atau tak hingga banyak, tergantung sistemnya)</sub>
- B. sistem pasti mempunyai tak hingga banyak penyelesaian  
  <sub>Salah: sistem seperti $x+y+z=1$, $x+y+z=2$, $x+y+z=3$ memenuhi semua determinan nol tetapi tidak punya solusi</sub>
- C. penyelesaiannya adalah $x = y = z = 0$  
  <sub>Salah: rumus $x = \frac{D_x}{D}$ tidak berlaku karena $D = 0$; $\frac{0}{0}$ tidak tentu</sub>
- D. sistem pasti tidak mempunyai penyelesaian  
  <sub>Salah: $D=0$ tidak berarti tidak ada solusi: sistem homogen selalu punya solusi $(0,0,0)$ dan beberapa sistem punya tak hingga banyak</sub>

**Pembahasan:** Aturan Cramer hanya berlaku untuk $D \neq 0$. Dengan $D = 0$ sistem tidak bisa bersolusi tunggal; kemungkinan lain (tak ada atau tak hingga) bergantung pada sistemnya, contoh $x+y+z=k$ tiga kali dengan $k$ berbeda tidak punya solusi.
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b01-e-hard-bt01-013
*orisinal | C5 | 6 langkah | jenis: temukan kesalahan: matriks kofaktor tanpa transpos*

Untuk $B = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}$, seorang siswa menentukan $B^{-1}$ sebagai $\frac{1}{|B|}K$ dengan $K$ matriks kofaktor (tanpa transpos). Elemen baris kedua kolom pertama hasil yang benar dikurangi hasil siswa adalah ....

- A. 20  
  <sub>Salah: hanya menyebut elemen yang benar, bukan selisihnya</sub>
- **B. 2** ✅  
  <sub>Benar: $|B|=1$. Benar: $(B^{-1})_{21}=k_{12}/|B|=20$; siswa: $k_{21}/|B|=18$; selisih $2$</sub>
- C. 18  
  <sub>Salah: hanya menyebut elemen hasil siswa, bukan selisihnya</sub>
- D. -2  
  <sub>Salah: mengurangkan dengan urutan terbalik (hasil siswa dikurangi hasil benar)</sub>

**Pembahasan:** $k_{12}=20$ dan $k_{21}=18$, $|B|=1$. Adjoin $=K^T$ sehingga $(B^{-1})_{21}=k_{12}/|B|=20$, sedangkan siswa memakai $k_{21}/|B|=18$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b01-e-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: determinan hasil kali berantai dengan invers*

Matriks $A$ dan $P$ berordo sama dengan $|A| = 5$ dan $|P| = -2$, dan $P$ mempunyai invers. Nilai $|P^{-1}AP|$ adalah ....

- **A. $5$** ✅  
  <sub>Benar: $|P^{-1}AP| = |P^{-1}||A||P| = \frac{1}{|P|}\cdot|A|\cdot|P| = |A| = 5$</sub>
- B. $-10$  
  <sub>Salah: mengalikan $|A|$ dengan $|P|$ saja dan mengabaikan $|P^{-1}|$</sub>
- C. $-\frac{5}{2}$  
  <sub>Salah: memakai $|P^{-1}||A|$ dan lupa faktor $|P|$ di ujung</sub>
- D. $20$  
  <sub>Salah: memakai $|P|^2|A|$ karena mengira $|P^{-1}| = |P|$</sub>

**Pembahasan:** Dengan $|AB| = |A||B|$: $|P^{-1}||A||P| = \frac{1}{-2}\cdot 5 \cdot (-2) = 5$.
**Acuan:** siswa — siswa hal.48

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
