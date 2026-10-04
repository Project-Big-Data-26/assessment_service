# Lembar koreksi — kelas11_tl SMA11L-B1 subbab A: Jenis-Jenis Matriks

50 soal | easy 20, medium 20, hard 10 | variasi 20, orisinal 30
> **Kapasitas kurang (hard): 10 dari kuota 20** — Subbab A (Jenis-Jenis Matriks, sekitar 8 halaman) hanya memuat definisi jenis matriks, transpos, dan kesamaan; easy+medium sudah memakai 40 soal dan 8 jenis. Penalaran sifat yang tersisa (klaim, penyangkal, parameter dua jenis, pencacahan matriks) hanya cukup untuk sekitar 10 soal hard tanpa kembar; sisanya akan menjadi soal hitung atau di luar materi subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b01-a-easy-bt01-001
*variasi (angka) | C1 | 1 langkah | jenis: menentukan jenis dari bentuk*

$A = \begin{pmatrix} 6 & -4 \\ 5 & 8 \\ -7 & 9 \\ 4 & 12 \end{pmatrix}$

Tentukan jenis matriks $A$ tersebut.

- **A. Matriks tegak** ✅  
  <sub>Benar: Matriks $A$ berordo $4 \times 2$ dengan banyak baris lebih banyak daripada banyak kolom ($4 > 2$), sehingga disebut matriks tegak.</sub>
- B. Matriks persegi  
  <sub>Salah: mengira banyak baris sama dengan banyak kolom</sub>
- C. Matriks kolom  
  <sub>Salah: mengira matriks hanya memiliki satu kolom</sub>
- D. Matriks datar  
  <sub>Salah: tertukar: mengira banyak kolom lebih banyak daripada banyak baris</sub>

**Pembahasan:** Ordo $A$ adalah $4 \times 2$. Karena $m > n$, matriks $A$ adalah matriks tegak.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b01-a-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: menentukan jenis dari bentuk*

$B = \begin{pmatrix} 8 & -6 & 9 \\ 4 & 7 & -5 \\ 12 & 6 & 10 \end{pmatrix}$

Jenis matriks $B$ tersebut adalah ....

- A. Matriks segitiga atas  
  <sub>Salah: mengira elemen di bawah diagonal utama bernilai nol padahal ada yang tidak nol</sub>
- **B. Matriks persegi** ✅  
  <sub>Benar: Ordo $B$ adalah $3 \times 3$ (banyak baris = banyak kolom), dan elemen di bawah serta di atas diagonal utama tidak semuanya nol, sehingga $B$ matriks persegi.</sub>
- C. Matriks datar  
  <sub>Salah: mengira kolom lebih banyak daripada baris</sub>
- D. Matriks diagonal  
  <sub>Salah: mengira semua elemen di luar diagonal utama nol</sub>

**Pembahasan:** Banyak baris $= 3 =$ banyak kolom, jadi $B$ persegi. Elemen $4, 12, 6$ di bawah diagonal utama tidak nol, sehingga bukan segitiga atas maupun diagonal.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b01-a-easy-bt01-003
*variasi (angka) | C1 | 1 langkah | jenis: menentukan jenis dari bentuk*

$C = \begin{pmatrix} 4 & 0 & 0 \\ 7 & -5 & 0 \\ 8 & 6 & 9 \end{pmatrix}$

Tentukan jenis matriks $C$ tersebut.

- A. Matriks segitiga atas  
  <sub>Salah: tertukar arah: mengira elemen di bawah diagonal yang harus nol</sub>
- B. Matriks simetris  
  <sub>Salah: tidak memeriksa kesamaan $a_{ij}$ dan $a_{ji}$ (nilai $7 \neq 0$)</sub>
- **C. Matriks segitiga bawah** ✅  
  <sub>Benar: Semua elemen di atas diagonal utama $C$ bernilai nol dan elemen di bawahnya tidak semuanya nol, sehingga $C$ matriks segitiga bawah.</sub>
- D. Matriks diagonal  
  <sub>Salah: mengira cukup ada elemen nol, padahal elemen di bawah diagonal utama tidak nol</sub>

**Pembahasan:** Elemen di atas diagonal utama ($a_{12}, a_{13}, a_{23}$) semuanya $0$, sehingga $C$ matriks segitiga bawah.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b01-a-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: menentukan jenis dari bentuk*

$P = \begin{pmatrix} 5 & -2 & 8 \\ -2 & 6 & 4 \\ 8 & 4 & 9 \end{pmatrix}$

Jenis matriks $P$ tersebut adalah ....

- **A. Matriks simetris** ✅  
  <sub>Benar: Setiap pasangan elemen yang simetris terhadap diagonal utama bernilai sama: $a_{12}=a_{21}=-2$, $a_{13}=a_{31}=8$, $a_{23}=a_{32}=4$.</sub>
- B. Matriks diagonal  
  <sub>Salah: mengira semua elemen di luar diagonal utama bernilai nol</sub>
- C. Matriks segitiga bawah  
  <sub>Salah: tidak memeriksa elemen di atas diagonal utama yang tidak nol</sub>
- D. Matriks segitiga atas  
  <sub>Salah: tidak memeriksa elemen di bawah diagonal utama yang tidak nol</sub>

**Pembahasan:** Karena $a_{ij}=a_{ji}$ untuk $i \neq j$, $P$ adalah matriks simetris.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b01-a-easy-bt01-005
*variasi (konteks) | C1 | 1 langkah | jenis: hubungan antarjenis matriks*

Matriks datar termasuk ke dalam kelompok matriks ....

- A. segitiga  
  <sub>Salah: mengira matriks datar selalu memiliki elemen nol pada sisi tertentu</sub>
- B. diagonal  
  <sub>Salah: mengira matriks datar hanya terisi pada diagonal utama</sub>
- **C. persegi panjang** ✅  
  <sub>Benar: Matriks datar dan matriks tegak kerap disebut matriks persegi panjang.</sub>
- D. persegi  
  <sub>Salah: mengira ordo $m \times n$ dengan $m < n$ termasuk persegi</sub>

**Pembahasan:** Matriks datar ($m < n$) dan matriks tegak ($m > n$) disebut matriks persegi panjang.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b01-a-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: sifat matriks khusus*

Pernyataan yang benar tentang matriks diagonal adalah ....

- A. Semua elemen pada diagonal utamanya bernilai satu  
  <sub>Salah: mencampuradukkan dengan matriks identitas</sub>
- B. Elemen di atas diagonal utamanya boleh tidak nol  
  <sub>Salah: mencampuradukkan dengan matriks segitiga bawah</sub>
- **C. Semua elemen di luar diagonal utamanya bernilai nol** ✅  
  <sub>Benar: Matriks diagonal adalah matriks persegi dengan elemen bernilai nol kecuali pada diagonal utama.</sub>
- D. Banyak baris tidak sama dengan banyak kolom  
  <sub>Salah: mengira matriks diagonal berordo $m \times n$ dengan $m \neq n$</sub>

**Pembahasan:** Matriks diagonal: elemen di luar diagonal utama bernilai nol; elemen diagonal bebas.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b01-a-easy-bt01-007
*variasi (konteks) | C2 | 2 langkah | jenis: hubungan antarjenis matriks*

Jika matriks $P$ adalah matriks nol berordo $4 \times 4$, maka matriks $P$ adalah matriks ....

- **A. diagonal** ✅  
  <sub>Benar: Semua elemen $P$ nol sehingga elemen di luar diagonal utama bernilai nol; $P$ persegi, jadi memenuhi ciri matriks diagonal.</sub>
- B. kolom  
  <sub>Salah: mengira matriks nol selalu berbentuk satu kolom</sub>
- C. datar  
  <sub>Salah: mengira ordo $4 \times 4$ memiliki lebih banyak kolom</sub>
- D. identitas  
  <sub>Salah: mengira diagonal utama harus bernilai satu</sub>

**Pembahasan:** $P$ persegi dan semua elemen di luar diagonal utamanya nol, sehingga $P$ matriks diagonal.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b01-a-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: hubungan antarjenis matriks*

Sebuah matriks identitas $I_n$ selalu tergolong juga sebagai jenis matriks ....

- A. baris  
  <sub>Salah: mengira matriks identitas hanya satu baris</sub>
- **B. simetris** ✅  
  <sub>Benar: Matriks identitas hanya memiliki elemen tak nol di diagonal utama sehingga $a_{ij}=a_{ji}$ untuk semua $i \neq j$ (sama-sama nol).</sub>
- C. nol  
  <sub>Salah: mengira elemen diagonal utama juga nol</sub>
- D. datar  
  <sub>Salah: mengira banyak kolom lebih banyak daripada banyak baris</sub>

**Pembahasan:** Pada matriks identitas, $a_{ij}=a_{ji}=0$ untuk $i \neq j$, jadi simetris.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b01-a-easy-bt01-009
*variasi (konteks) | C1 | 1 langkah | jenis: hubungan antarjenis matriks*

Jika matriks $M$ adalah matriks diagonal dengan semua elemen diagonal utamanya bernilai satu, maka matriks $M$ disebut matriks ....

- A. nol  
  <sub>Salah: mengira semua elemen matriks bernilai nol</sub>
- B. tegak  
  <sub>Salah: mengira banyak baris lebih banyak daripada banyak kolom</sub>
- C. baris  
  <sub>Salah: mengira matriks hanya terdiri atas satu baris</sub>
- **D. identitas** ✅  
  <sub>Benar: Matriks diagonal dengan elemen-elemen diagonal utama bernilai satu disebut matriks identitas.</sub>

**Pembahasan:** Definisi: matriks diagonal dengan diagonal utama bernilai satu adalah matriks identitas.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b01-a-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: transpos matriks*

Jika $A$ adalah matriks kolom berordo $4 \times 1$ dan $A^t$ transposnya, maka ordo $A^t$ adalah ....

- A. $4 \times 4$  
  <sub>Salah: mengira transpos menghasilkan matriks persegi</sub>
- B. $1 \times 1$  
  <sub>Salah: mengira hanya satu elemen yang tersisa</sub>
- **C. $1 \times 4$** ✅  
  <sub>Benar: Transpos menukar baris menjadi kolom, sehingga ordo $4 \times 1$ menjadi $1 \times 4$.</sub>
- D. $4 \times 1$  
  <sub>Salah: mengira transpos tidak mengubah ordo</sub>

**Pembahasan:** Ordo $m \times n$ menjadi $n \times m$, jadi $4 \times 1$ menjadi $1 \times 4$ (matriks baris).
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b01-a-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: transpos matriks*

Transpos dari matriks datar berordo $2 \times 5$ merupakan matriks ....

- A. baris  
  <sub>Salah: mengira transpos menghasilkan satu baris</sub>
- B. datar  
  <sub>Salah: mengira transpos tidak mengubah jenis matriks</sub>
- C. persegi  
  <sub>Salah: mengira transpos selalu menghasilkan matriks persegi</sub>
- **D. tegak** ✅  
  <sub>Benar: Ordo transpos adalah $5 \times 2$ dengan $5 > 2$, yaitu matriks tegak.</sub>

**Pembahasan:** $2 \times 5$ menjadi $5 \times 2$; banyak baris lebih banyak daripada kolom, jadi tegak.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b01-a-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: ordo dan banyak elemen*

Banyak elemen pada sebuah matriks berordo $5 \times 6$ adalah ....

- A. $25$  
  <sub>Salah: mengkuadratkan banyak baris</sub>
- B. $11$  
  <sub>Salah: menjumlahkan banyak baris dan kolom</sub>
- C. $56$  
  <sub>Salah: menyambung kedua angka ordo</sub>
- **D. $30$** ✅  
  <sub>Benar: Banyak elemen = banyak baris $\times$ banyak kolom $= 5 \times 6 = 30$.</sub>

**Pembahasan:** Matriks berordo $m \times n$ memuat $m \times n$ elemen.
**Acuan:** siswa — siswa hal.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b01-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: elemen matriks*

$A = \begin{pmatrix} 12 & -3 & 8 \\ 5 & 9 & -6 \\ 7 & 4 & 10 \\ 2 & 11 & 1 \end{pmatrix}$

Nilai elemen $a_{32}$ pada matriks $A$ adalah ....

- A. $-6$  
  <sub>Salah: tertukar membaca baris ke-2 kolom ke-3 ($a_{23}$)</sub>
- **B. $4$** ✅  
  <sub>Benar: $a_{32}$ adalah elemen pada baris ke-3 dan kolom ke-2, yaitu $4$.</sub>
- C. $9$  
  <sub>Salah: salah membaca baris ke-2 kolom ke-2</sub>
- D. $11$  
  <sub>Salah: membaca baris ke-4 kolom ke-2</sub>

**Pembahasan:** Baris ke-3: $7, 4, 10$. Kolom ke-2 pada baris itu adalah $4$.
**Acuan:** siswa — siswa hal.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b01-a-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: ordo dan banyak elemen*

Nilai ulangan 7 siswa pada 3 mata pelajaran disajikan dalam sebuah matriks. Setiap baris memuat data satu siswa dan setiap kolom memuat data satu mata pelajaran. Ordo matriks tersebut adalah ....

- A. $7 \times 7$  
  <sub>Salah: mengira matriks harus persegi</sub>
- **B. $7 \times 3$** ✅  
  <sub>Benar: Ada 7 baris (siswa) dan 3 kolom (mata pelajaran), sehingga ordo $7 \times 3$.</sub>
- C. $21 \times 1$  
  <sub>Salah: menuliskan seluruh data sebagai satu kolom</sub>
- D. $3 \times 7$  
  <sub>Salah: tertukar urutan baris dan kolom</sub>

**Pembahasan:** Ordo ditulis banyak baris $\times$ banyak kolom.
**Acuan:** siswa — siswa hal.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b01-a-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: mengenali bentuk matriks*

Di antara matriks berikut, yang merupakan matriks kolom adalah ....

- A. $\begin{pmatrix} 9 & -4 & 6 \end{pmatrix}$  
  <sub>Salah: matriks baris ($1 \times 3$) dikira matriks kolom</sub>
- B. $\begin{pmatrix} 9 & -4 & 6 \\ 1 & 2 & 3 \\ 5 & 7 & 8 \end{pmatrix}$  
  <sub>Salah: matriks persegi $3 \times 3$</sub>
- C. $\begin{pmatrix} 9 & -4 \\ 6 & 2 \\ 5 & 7 \end{pmatrix}$  
  <sub>Salah: matriks berordo $3 \times 2$, memiliki dua kolom</sub>
- **D. $\begin{pmatrix} 9 \\ -4 \\ 6 \end{pmatrix}$** ✅  
  <sub>Benar: Matriks berordo $3 \times 1$ hanya memiliki satu kolom.</sub>

**Pembahasan:** Matriks kolom berordo $m \times 1$; hanya pilihan berordo $3 \times 1$ yang memenuhi.
**Acuan:** siswa — siswa hal.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b01-a-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: transpos matriks*

$A = \begin{pmatrix} 4 & -1 & 7 \\ 3 & 0 & 5 \end{pmatrix}$

Transpos dari matriks $A$, yaitu $A^t$, adalah ....

- A. $\begin{pmatrix} 7 & 5 \\ -1 & 0 \\ 4 & 3 \end{pmatrix}$  
  <sub>Salah: urutan elemen terbalik karena membaca baris dari kanan ke kiri</sub>
- B. $\begin{pmatrix} 4 & -1 \\ 7 & 3 \\ 0 & 5 \end{pmatrix}$  
  <sub>Salah: hanya menyusun ulang elemen per baris menjadi 3 baris, bukan menukar baris dan kolom</sub>
- **C. $\begin{pmatrix} 4 & 3 \\ -1 & 0 \\ 7 & 5 \end{pmatrix}$** ✅  
  <sub>Benar: Baris ke-1 $A$ ($4, -1, 7$) menjadi kolom ke-1 $A^t$ dan baris ke-2 ($3, 0, 5$) menjadi kolom ke-2.</sub>
- D. $\begin{pmatrix} -4 & -3 \\ 1 & 0 \\ -7 & -5 \end{pmatrix}$  
  <sub>Salah: mengubah tanda semua elemen</sub>

**Pembahasan:** $A^t$ berordo $3 \times 2$ dengan kolom ke-$j$ berisi baris ke-$j$ dari $A$.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b01-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: sifat matriks khusus*

Matriks $S$ berordo $3 \times 3$ adalah matriks simetris dengan $a_{12} = 9$ dan $a_{23} = -4$. Nilai $a_{21} + a_{32}$ adalah ....

- **A. $5$** ✅  
  <sub>Benar: Pada matriks simetris $a_{21}=a_{12}=9$ dan $a_{32}=a_{23}=-4$, sehingga jumlahnya $9 + (-4) = 5$.</sub>
- B. $0$  
  <sub>Salah: menganggap $a_{21}$ dan $a_{32}$ bernilai nol karena tidak diketahui</sub>
- C. $13$  
  <sub>Salah: mengabaikan tanda negatif pada $a_{32}$</sub>
- D. $-5$  
  <sub>Salah: salah tanda hasil penjumlahan</sub>

**Pembahasan:** $a_{ij}=a_{ji}$ sehingga $a_{21}=9$ dan $a_{32}=-4$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b01-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: diagonal matriks*

$K = \begin{pmatrix} 3 & 2 & 5 \\ -2 & 6 & 1 \\ 9 & 4 & 7 \end{pmatrix}$

Jumlah elemen-elemen pada diagonal utama matriks $K$ adalah ....

- A. $10$  
  <sub>Salah: menjumlahkan baris pertama</sub>
- B. $20$  
  <sub>Salah: menjumlahkan diagonal samping ($5 + 6 + 9$)</sub>
- C. $35$  
  <sub>Salah: menjumlahkan semua elemen</sub>
- **D. $16$** ✅  
  <sub>Benar: Diagonal utama memuat $a_{11}=3$, $a_{22}=6$, $a_{33}=7$, sehingga jumlahnya $16$.</sub>

**Pembahasan:** $3 + 6 + 7 = 16$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b01-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: sifat matriks khusus*

Jumlah semua elemen pada matriks identitas berordo $5 \times 5$ adalah ....

- A. $1$  
  <sub>Salah: mengira jumlah hanya satu elemen</sub>
- **B. $5$** ✅  
  <sub>Benar: Hanya 5 elemen diagonal utama yang bernilai $1$, elemen lain nol, jumlahnya $5$.</sub>
- C. $10$  
  <sub>Salah: menghitung dua kali elemen diagonal</sub>
- D. $25$  
  <sub>Salah: menganggap semua $25$ elemen bernilai satu</sub>

**Pembahasan:** Jumlah $= 5 \times 1 = 5$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b01-a-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: sifat matriks khusus*

Pada matriks segitiga atas berordo $4 \times 4$, banyak elemen yang di bawah diagonal utama (semuanya bernilai nol) adalah ....

- **A. $6$** ✅  
  <sub>Benar: Baris ke-2 punya 1, baris ke-3 punya 2, baris ke-4 punya 3 elemen di bawah diagonal: $1+2+3=6$.</sub>
- B. $4$  
  <sub>Salah: menghitung elemen diagonal utama</sub>
- C. $12$  
  <sub>Salah: menghitung semua elemen di luar diagonal utama</sub>
- D. $10$  
  <sub>Salah: menghitung elemen di bawah ditambah diagonal utama</sub>

**Pembahasan:** Total 16 elemen: 4 diagonal, 6 di atas, 6 di bawah.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b01-a-medium-bt01-001
*variasi (konteks) | C4 | 3 langkah | jenis: hubungan antarjenis matriks*

Sebuah matriks identitas berordo $4 \times 4$ tergolong ke dalam semua jenis matriks berikut, kecuali matriks ....

- A. simetris  
  <sub>Salah: mengira elemen $a_{ij}$ dan $a_{ji}$ tidak sama; padahal semua elemen di luar diagonal bernilai nol sehingga sama</sub>
- **B. tegak** ✅  
  <sub>Benar: Matriks identitas berordo $4 \times 4$ adalah matriks persegi, bukan matriks tegak (tegak mensyaratkan banyak baris lebih banyak daripada banyak kolom).</sub>
- C. diagonal  
  <sub>Salah: mengira matriks identitas bukan matriks diagonal; padahal ia adalah matriks diagonal dengan diagonal utama bernilai satu</sub>
- D. segitiga bawah  
  <sub>Salah: mengira semua elemen di atas diagonal utama tidak boleh nol; padahal semuanya nol</sub>

**Pembahasan:** Matriks identitas adalah matriks diagonal, sehingga juga segitiga bawah dan simetris. Ordonya $4 \times 4$ sehingga persegi, bukan tegak.
**Acuan:** siswa — siswa hal.24 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b01-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: menyusun matriks dari data*

Kebutuhan energi minimal atlet lari putri (dalam kalori) adalah sebagai berikut.

- Usia 14—15 tahun: normal 1.800; ditambah 3 jam latihan 2.400; ditambah 4 jam latihan 2.700; ditambah 5 jam latihan 3.000.
- Usia 16—17 tahun: normal 2.100; ditambah 3 jam latihan 2.600; ditambah 4 jam latihan 2.900; ditambah 5 jam latihan 3.300.
- Usia 18—20 tahun: normal 2.300; ditambah 3 jam latihan 2.800; ditambah 4 jam latihan 3.100; ditambah 5 jam latihan 3.500.

Data disusun menjadi matriks dengan baris menyatakan kelompok usia (urut dari yang termuda) dan kolom menyatakan kondisi (normal, tambah 3 jam, tambah 4 jam, tambah 5 jam). Pernyataan yang benar tentang matriks tersebut adalah ....

- A. Matriks tegak berordo $4 \times 3$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$  
  <sub>Salah: tertukar menentukan ordo (baris dan kolom terbalik) sehingga jenis menjadi tegak</sub>
- B. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.600$  
  <sub>Salah: salah membaca kolom: mengambil kolom ke-2 (tambah 3 jam)</sub>
- **C. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $2.900$** ✅  
  <sub>Benar: Ada 3 kelompok usia (baris) dan 4 kondisi (kolom), sehingga ordo $3 \times 4$ dengan $3 < 4$ (datar). Baris ke-2 adalah usia 16—17 tahun dan kolom ke-3 adalah tambah 4 jam latihan, yaitu $2.900$.</sub>
- D. Matriks datar berordo $3 \times 4$ dengan elemen baris ke-2 kolom ke-3 bernilai $3.100$  
  <sub>Salah: salah membaca baris: mengambil baris ke-3 (usia 18—20 tahun)</sub>

**Pembahasan:** Matriks berordo $3 \times 4$ (datar). Elemen baris ke-2 kolom ke-3 = $2.900$.
**Acuan:** siswa — siswa hal.24 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b01-a-medium-bt01-003
*variasi (angka) | C3 | 2 langkah | jenis: menyusun matriks dari data*

Kebutuhan energi lima atlet (dalam kalori) dicatat saat istirahat dan saat latihan.

| Atlet | Istirahat | Latihan |
|---|---|---|
| Andi | 1.700 | 2.300 |
| Budi | 1.900 | 2.600 |
| Candra | 2.200 | 2.900 |
| Dimas | 1.800 | 2.400 |
| Eko | 2.100 | 2.800 |

Data pada tabel disusun menjadi matriks $K$ dengan setiap baris memuat data satu kondisi (istirahat dan latihan) dan setiap kolom memuat data satu atlet. Matriks $K$ merupakan ....

- **A. matriks datar berordo $2 \times 5$** ✅  
  <sub>Benar: Ada 2 kondisi (baris) dan 5 atlet (kolom), sehingga ordo $2 \times 5$ dengan banyak kolom lebih banyak daripada banyak baris, yaitu matriks datar.</sub>
- B. matriks tegak berordo $5 \times 2$  
  <sub>Salah: menyusun baris untuk atlet dan kolom untuk kondisi, tidak sesuai susunan yang diminta</sub>
- C. matriks kolom berordo $10 \times 1$  
  <sub>Salah: menuliskan semua data dalam satu kolom</sub>
- D. matriks baris berordo $1 \times 10$  
  <sub>Salah: menuliskan semua data dalam satu baris</sub>

**Pembahasan:** Baris = kondisi (2), kolom = atlet (5), sehingga $K$ berordo $2 \times 5$ dan $2 < 5$, jadi datar.
**Acuan:** siswa — siswa hal.24 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b01-a-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: ordo dan banyak elemen*

Sebuah matriks tegak memuat $60$ elemen dan memiliki paling sedikit dua kolom. Banyak kemungkinan ordo matriks tersebut adalah ....

- A. $6$  
  <sub>Salah: ikut menghitung ordo $60 \times 1$ padahal kolomnya harus minimal dua</sub>
- B. $10$  
  <sub>Salah: menghitung semua pasangan faktor dengan kedua bilangan minimal 2 tanpa syarat $m > n$</sub>
- **C. $5$** ✅  
  <sub>Benar: Pasangan $(m, n)$ dengan $m \times n = 60$, $m > n$, dan $n \geq 2$: $(30,2), (20,3), (15,4), (12,5), (10,6)$, yaitu $5$ pasangan.</sub>
- D. $12$  
  <sub>Salah: menghitung semua pasangan faktor berurutan (termasuk $m < n$ dan $n = 1$)</sub>

**Pembahasan:** Faktor $60$: $1,2,3,4,5,6,10,12,15,20,30,60$. Dengan $m > n \geq 2$ diperoleh $n = 2,3,4,5,6$ (dan $m = 30,20,15,12,10$), yaitu $5$ ordo.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b01-a-medium-bt01-005
*variasi (konteks) | C4 | 3 langkah | jenis: parameter pada matriks khusus*

Matriks $K = \begin{pmatrix} 3 & p + 3 & 0 \\ 0 & 5 & 3q - 12 \\ 0 & 0 & 2 \end{pmatrix}$ merupakan matriks diagonal. Nilai $p \cdot q$ adalah ....

- A. $-7$  
  <sub>Salah: menghitung $p - q$, bukan $p \cdot q$</sub>
- B. $12$  
  <sub>Salah: salah tanda pada $p$ ($p = 3$)</sub>
- **C. $-12$** ✅  
  <sub>Benar: Elemen di luar diagonal utama harus nol: $p + 3 = 0$ sehingga $p = -3$ dan $3q - 12 = 0$ sehingga $q = 4$. Maka $p \cdot q = -12$.</sub>
- D. $1$  
  <sub>Salah: menjumlahkan $p + q$, bukan mengalikan</sub>

**Pembahasan:** Matriks diagonal: $p + 3 = 0 \Rightarrow p = -3$; $3q - 12 = 0 \Rightarrow q = 4$; $p \cdot q = -12$.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b01-a-medium-bt01-006
*variasi (konteks) | C4 | 3 langkah | jenis: memilih matriks dari dua sifat*

Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks simetris tetapi bukan matriks diagonal adalah ....

- A. $\begin{pmatrix} 6 & -2 & 0 \\ 2 & 4 & 5 \\ 0 & -5 & 3 \end{pmatrix}$  
  <sub>Salah: pasangan elemen simetris berlawanan tanda ($-2$ dan $2$, $5$ dan $-5$) sehingga tidak simetris</sub>
- B. $\begin{pmatrix} 6 & 0 & 0 \\ 0 & 4 & 0 \\ 0 & 0 & 3 \end{pmatrix}$  
  <sub>Salah: matriks diagonal; memang simetris tetapi melanggar syarat bukan diagonal</sub>
- C. $\begin{pmatrix} 6 & -2 & 0 \\ 0 & 4 & 5 \\ 0 & 0 & 3 \end{pmatrix}$  
  <sub>Salah: matriks segitiga atas, elemen $a_{ij}$ dan $a_{ji}$ tidak sama sehingga tidak simetris</sub>
- **D. $\begin{pmatrix} 6 & -2 & 0 \\ -2 & 4 & 5 \\ 0 & 5 & 3 \end{pmatrix}$** ✅  
  <sub>Benar: Elemen yang simetris terhadap diagonal utama sama ($-2 = -2$, $0 = 0$, $5 = 5$), dan ada elemen di luar diagonal yang tidak nol, sehingga simetris tetapi bukan diagonal.</sub>

**Pembahasan:** Hanya pilihan pertama yang memenuhi $a_{ij} = a_{ji}$ dengan elemen di luar diagonal tidak semuanya nol.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b01-a-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: ordo dan banyak elemen*

Transpos matriks $P$ adalah matriks $Q$ berordo $3 \times 7$. Pernyataan yang benar tentang matriks $P$ adalah ....

- **A. $P$ merupakan matriks tegak yang memuat $21$ elemen** ✅  
  <sub>Benar: Ordo $P$ adalah $7 \times 3$ (baris dan kolom $Q$ ditukar), sehingga $7 > 3$ (tegak) dan banyak elemen $7 \times 3 = 21$.</sub>
- B. $P$ merupakan matriks persegi yang memuat $49$ elemen  
  <sub>Salah: mengira ordo $7 \times 7$</sub>
- C. $P$ merupakan matriks datar yang memuat $21$ elemen  
  <sub>Salah: tidak menukar ordo sehingga mengira $P$ berordo $3 \times 7$</sub>
- D. $P$ merupakan matriks tegak yang memuat $10$ elemen  
  <sub>Salah: menjumlahkan banyak baris dan kolom, bukan mengalikan</sub>

**Pembahasan:** Transpos menukar ordo: $P$ berordo $7 \times 3$ (tegak) dengan $21$ elemen.
**Acuan:** siswa — siswa hal.23 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b01-a-medium-bt01-008
*variasi (angka) | C4 | 3 langkah | jenis: transpos matriks*

$U = \begin{pmatrix} 6 & -4 & 7 \\ 0 & 8 & -3 \\ 0 & 0 & 5 \end{pmatrix}$

Matriks $U$ berjenis segitiga atas. Pernyataan yang benar tentang transpos $U$, yaitu $U^t$, adalah ....

- A. $U^t$ matriks segitiga atas dan elemen baris ke-3 kolom ke-1 bernilai $7$  
  <sub>Salah: mengira transpos tidak mengubah jenis matriks</sub>
- B. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $0$  
  <sub>Salah: membaca elemen baris ke-3 kolom ke-1 pada $U$, bukan pada $U^t$</sub>
- C. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $-4$  
  <sub>Salah: salah membaca baris: mengambil elemen baris ke-2 kolom ke-1</sub>
- **D. $U^t$ matriks segitiga bawah dan elemen baris ke-3 kolom ke-1 bernilai $7$** ✅  
  <sub>Benar: $U^t = \begin{pmatrix} 6 & 0 & 0 \\ -4 & 8 & 0 \\ 7 & -3 & 5 \end{pmatrix}$; semua elemen di atas diagonal utama nol (segitiga bawah) dan baris ke-3 kolom ke-1 bernilai $7$.</sub>

**Pembahasan:** Kolom ke-$j$ pada $U^t$ adalah baris ke-$j$ pada $U$. Maka $U^t$ segitiga bawah dengan baris ke-3: $7, -3, 5$.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b01-a-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: transpos matriks*

$C = \begin{pmatrix} 7 & -8 & 9 & 4 & 6 \\ -10 & 11 & 12 & 14 & -6 \end{pmatrix}$

Tentukan jenis matriks $C^t$.

- **A. Matriks tegak** ✅  
  <sub>Benar: $C$ berordo $2 \times 5$, sehingga $C^t$ berordo $5 \times 2$ dengan banyak baris lebih banyak daripada banyak kolom: matriks tegak.</sub>
- B. Matriks persegi  
  <sub>Salah: mengira transpos menghasilkan matriks persegi</sub>
- C. Matriks kolom  
  <sub>Salah: mengira transpos hanya memiliki satu kolom</sub>
- D. Matriks datar  
  <sub>Salah: menentukan jenis $C$, bukan jenis transposnya</sub>

**Pembahasan:** Ordo $C$ adalah $2 \times 5$; ordo $C^t$ adalah $5 \times 2$ sehingga $C^t$ matriks tegak.
**Acuan:** pretest — kelas11_tl-b01-p0023-latihan-a-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b01-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: ordo dan banyak elemen*

Sebuah matriks persegi panjang memuat $35$ elemen dan banyak barisnya $2$ lebih banyak daripada banyak kolomnya. Ordo matriks tersebut adalah ....

- A. $6 \times 4$  
  <sub>Salah: hanya memenuhi selisih baris dan kolom, tetapi hanya memuat $24$ elemen</sub>
- **B. $7 \times 5$** ✅  
  <sub>Benar: Misalkan kolom $n$, baris $n + 2$: $n(n + 2) = 35$ sehingga $n = 5$ dan baris $= 7$.</sub>
- C. $5 \times 7$  
  <sub>Salah: tertukar urutan baris dan kolom</sub>
- D. $35 \times 1$  
  <sub>Salah: hanya memenuhi banyak elemen, selisih baris dan kolom bukan $2$</sub>

**Pembahasan:** $n(n + 2) = 35 \Rightarrow n = 5$, jadi ordo $7 \times 5$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b01-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: elemen dengan rumus*

Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $a_{ij} = i \cdot j - i$, dengan $i$ nomor baris dan $j$ nomor kolom. Jumlah elemen pada diagonal utama matriks $A$ adalah ....

- **A. $8$** ✅  
  <sub>Benar: Diagonal utama: $i = j$ sehingga $a_{ii} = i^2 - i$, yaitu $0, 2, 6$. Jumlahnya $8$.</sub>
- B. $20$  
  <sub>Salah: salah tanda: memakai $i \cdot j + i$ sehingga elemennya $2, 6, 12$</sub>
- C. $14$  
  <sub>Salah: memakai $a_{ii} = i^2$ (lupa mengurangi $i$)</sub>
- D. $4$  
  <sub>Salah: menjumlahkan elemen diagonal samping ($2 + 2 + 0$)</sub>

**Pembahasan:** $a_{ii} = i^2 - i$: $0 + 2 + 6 = 8$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b01-a-medium-bt01-012
*orisinal | C3 | 2 langkah | jenis: transpos matriks*

$A = \begin{pmatrix} 3 & -1 & 6 & 2 \\ 5 & 0 & -4 & -7 \\ 7 & 9 & 1 & -2 \end{pmatrix}$

Elemen pada baris ke-4 dan kolom ke-2 matriks $A^t$ bernilai ....

- A. $9$  
  <sub>Salah: salah membaca baris dan kolom: mengambil baris ke-3 kolom ke-2 pada $A$</sub>
- B. $-4$  
  <sub>Salah: salah membaca kolom: mengambil baris ke-2 kolom ke-3 pada $A$</sub>
- C. $-2$  
  <sub>Salah: salah membaca baris: mengambil baris ke-3 kolom ke-4 pada $A$</sub>
- **D. $-7$** ✅  
  <sub>Benar: Elemen baris ke-4 kolom ke-2 pada $A^t$ sama dengan elemen baris ke-2 kolom ke-4 pada $A$, yaitu $-7$.</sub>

**Pembahasan:** Pada transpos, baris dan kolom ditukar: elemen $(4,2)$ pada $A^t$ adalah elemen $(2,4)$ pada $A$, yaitu $-7$.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b01-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: parameter pada matriks khusus*

Matriks $S = \begin{pmatrix} 3 & 2x & 5 \\ 10 & 1 & y + 2 \\ 5 & 6 & 4 \end{pmatrix}$ merupakan matriks simetris. Nilai $x + y$ adalah ....

- **A. $9$** ✅  
  <sub>Benar: Simetris: $2x = 10$ sehingga $x = 5$, dan $y + 2 = 6$ sehingga $y = 4$. Maka $x + y = 9$.</sub>
- B. $11$  
  <sub>Salah: lupa mengurangi $2$ sehingga $y = 6$</sub>
- C. $13$  
  <sub>Salah: menambah $2$ (bukan mengurangi) sehingga $y = 8$</sub>
- D. $14$  
  <sub>Salah: tidak membagi dengan $2$ sehingga $x = 10$</sub>

**Pembahasan:** $a_{12} = a_{21} \Rightarrow 2x = 10$; $a_{23} = a_{32} \Rightarrow y + 2 = 6$. Jadi $x + y = 9$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b01-a-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: banyak elemen khusus*

Matriks segitiga atas berordo $6 \times 6$ dan matriks diagonal berordo $6 \times 6$ masing-masing dibuat dengan elemen tak nol sebanyak mungkin. Selisih banyak elemen tak nol kedua matriks tersebut adalah ....

- A. $21$  
  <sub>Salah: hanya menghitung banyak elemen tak nol matriks segitiga atas</sub>
- B. $27$  
  <sub>Salah: menjumlahkan, bukan mengurangkan, kedua banyak elemen</sub>
- C. $30$  
  <sub>Salah: mengurangkan banyak elemen total ($36$) dengan elemen diagonal</sub>
- **D. $15$** ✅  
  <sub>Benar: Segitiga atas: elemen pada dan di atas diagonal utama, yaitu $6 + 5 + 4 + 3 + 2 + 1 = 21$. Diagonal: $6$. Selisih $21 - 6 = 15$.</sub>

**Pembahasan:** $21 - 6 = 15$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b01-a-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: memilih matriks dari dua sifat*

Di antara matriks berordo $3 \times 3$ berikut, yang merupakan matriks segitiga atas tetapi bukan matriks diagonal adalah ....

- A. $\begin{pmatrix} 2 & 0 & 0 \\ 5 & 3 & 0 \\ 1 & 4 & 6 \end{pmatrix}$  
  <sub>Salah: matriks segitiga bawah, elemen di bawah diagonal utama tidak nol</sub>
- B. $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 7 & 0 & 6 \end{pmatrix}$  
  <sub>Salah: ada elemen tak nol di bawah diagonal utama ($7$), jadi bukan segitiga</sub>
- C. $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 6 \end{pmatrix}$  
  <sub>Salah: matriks diagonal; memang segitiga atas tetapi melanggar syarat bukan diagonal</sub>
- **D. $\begin{pmatrix} 2 & 5 & 1 \\ 0 & 3 & 4 \\ 0 & 0 & 6 \end{pmatrix}$** ✅  
  <sub>Benar: Semua elemen di bawah diagonal utama nol (segitiga atas), dan ada elemen di atas diagonal yang tidak nol sehingga bukan diagonal.</sub>

**Pembahasan:** Hanya pilihan pertama yang memiliki elemen di bawah diagonal nol sekaligus elemen di atas diagonal tidak nol.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b01-a-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: hubungan antarjenis matriks*

Matriks persegi yang sekaligus merupakan matriks segitiga atas dan matriks simetris pasti merupakan matriks ....

- A. identitas  
  <sub>Salah: mengira diagonal utama pasti bernilai satu</sub>
- B. datar  
  <sub>Salah: mengira ordo matriks tidak persegi</sub>
- **C. diagonal** ✅  
  <sub>Benar: Segitiga atas: elemen di bawah diagonal nol. Simetris: elemen di atas diagonal sama dengan pasangannya di bawah, sehingga juga nol. Semua elemen di luar diagonal nol: matriks diagonal.</sub>
- D. nol  
  <sub>Salah: mengira semua elemen termasuk diagonal utama nol</sub>

**Pembahasan:** $a_{ij} = 0$ untuk $i > j$ (segitiga atas) dan $a_{ij} = a_{ji} = 0$ untuk $i < j$ (simetris), jadi diagonal.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b01-a-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: menyusun matriks dari data*

Rekapan absensi peserta didik kelas XII di SMA Makmur dalam satu semester.

| Keterangan | XII 1 | XII 2 | XII 3 |
|---|---|---|---|
| Izin | 1 | 1 | 3 |
| Sakit | 2 | 1 | 3 |
| Tanpa keterangan | 5 | 1 | 2 |

Data pada tabel disajikan sebagai matriks dengan setiap baris menyatakan satu jenis keterangan dan setiap kolom menyatakan satu kelas. Pernyataan yang benar tentang matriks tersebut adalah ....

- A. Matriks segitiga atas dengan jumlah elemen diagonal utama $4$  
  <sub>Salah: tidak memeriksa elemen di bawah diagonal utama yang tidak nol ($2, 5, 1$)</sub>
- **B. Matriks persegi dengan jumlah elemen diagonal utama $4$** ✅  
  <sub>Benar: Matriks $\begin{pmatrix} 1 & 1 & 3 \\ 2 & 1 & 3 \\ 5 & 1 & 2 \end{pmatrix}$ berordo $3 \times 3$ (persegi); diagonal utama $1 + 1 + 2 = 4$.</sub>
- C. Matriks persegi dengan jumlah elemen diagonal utama $9$  
  <sub>Salah: menjumlahkan diagonal samping ($3 + 1 + 5$)</sub>
- D. Matriks datar dengan jumlah elemen diagonal utama $4$  
  <sub>Salah: mengira banyak kolom lebih banyak daripada banyak baris</sub>

**Pembahasan:** Ada 3 baris dan 3 kolom sehingga persegi. Diagonal utama: $1, 1, 2$ dengan jumlah $4$. Elemen di bawah diagonal tidak nol, jadi bukan segitiga.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b01-a-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: banyak elemen khusus*

Matriks simetris berordo $4 \times 4$ paling banyak memiliki elemen dengan nilai yang berbeda sebanyak ....

- A. $6$  
  <sub>Salah: hanya menghitung elemen di atas diagonal utama</sub>
- B. $16$  
  <sub>Salah: mengira semua elemen bisa berbeda tanpa memakai sifat simetris</sub>
- **C. $10$** ✅  
  <sub>Benar: Karena $a_{ij} = a_{ji}$, nilai bebas hanya pada diagonal utama ($4$) dan di atas diagonal ($6$): $4 + 6 = 10$.</sub>
- D. $12$  
  <sub>Salah: menghitung semua elemen di luar diagonal utama</sub>

**Pembahasan:** Elemen di bawah diagonal ditentukan oleh elemen di atasnya. Jadi hanya $4 + 6 = 10$ nilai yang bebas.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b01-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: parameter pada matriks khusus*

Matriks $E = \begin{pmatrix} 3p - 8 & 0 & 0 \\ 0 & q + 6 & 0 \\ 0 & 0 & 2r - 7 \end{pmatrix}$ merupakan matriks identitas. Nilai $p + q + r$ adalah ....

- A. $12$  
  <sub>Salah: salah tanda pada $q$ ($q = 5$)</sub>
- **B. $2$** ✅  
  <sub>Benar: Elemen diagonal utama bernilai satu: $3p - 8 = 1 \Rightarrow p = 3$; $q + 6 = 1 \Rightarrow q = -5$; $2r - 7 = 1 \Rightarrow r = 4$. Jumlahnya $2$.</sub>
- C. $6$  
  <sub>Salah: tidak membagi dengan $2$ sehingga $r = 8$</sub>
- D. $8$  
  <sub>Salah: tidak membagi dengan $3$ sehingga $p = 9$</sub>

**Pembahasan:** $p = 3$, $q = -5$, $r = 4$, sehingga $p + q + r = 2$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b01-a-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: elemen dengan rumus*

Matriks $D = (d_{ij})$ berordo $3 \times 3$ dengan $d_{ij} = i + 2j$. Baris pertama matriks $D^t$ adalah ....

- A. $\begin{pmatrix} 3 & 5 & 7 \end{pmatrix}$  
  <sub>Salah: membaca baris pertama $D$ (tidak mentranspos)</sub>
- **B. $\begin{pmatrix} 3 & 4 & 5 \end{pmatrix}$** ✅  
  <sub>Benar: Baris pertama $D^t$ adalah kolom pertama $D$, yaitu $d_{k1} = k + 2$ untuk $k = 1, 2, 3$: $3, 4, 5$.</sub>
- C. $\begin{pmatrix} 5 & 7 & 9 \end{pmatrix}$  
  <sub>Salah: membaca baris ke-3 matriks $D$</sub>
- D. $\begin{pmatrix} 2 & 3 & 4 \end{pmatrix}$  
  <sub>Salah: memakai aturan $i + j$ bukan $i + 2j$</sub>

**Pembahasan:** $D = \begin{pmatrix} 3 & 5 & 7 \\ 4 & 6 & 8 \\ 5 & 7 & 9 \end{pmatrix}$, kolom pertamanya $3, 4, 5$ menjadi baris pertama $D^t$.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b01-a-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim jenis matriks*

Di antara pernyataan berikut, yang benar adalah ....

- A. Setiap matriks segitiga atas adalah matriks simetris.  
  <sub>Salah: mengira segitiga atas pasti simetris; $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ adalah penyangkalnya</sub>
- B. Setiap matriks simetris adalah matriks diagonal.  
  <sub>Salah: membalik arah klaim; $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ simetris tetapi bukan diagonal</sub>
- C. Transpos dari setiap matriks segitiga atas adalah matriks segitiga atas.  
  <sub>Salah: mengira transpos tidak mengubah jenis; transpos $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ adalah segitiga bawah dan bukan segitiga atas</sub>
- **D. Setiap matriks diagonal adalah matriks simetris.** ✅  
  <sub>Benar: Pada matriks diagonal semua elemen di luar diagonal utama nol, sehingga $a_{ij} = a_{ji} = 0$ untuk $i \neq j$ dan matriks simetris.</sub>

**Pembahasan:** Klaim pertama benar karena matriks diagonal pasti simetris. Tiga klaim lain punya penyangkal $2 \times 2$: $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ dan $\begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b01-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim jenis matriks*

Sebuah matriks $M$ memenuhi $M^t = M$. Pernyataan yang pasti benar tentang $M$ adalah ....

- A. $M$ merupakan matriks identitas  
  <sub>Salah: mengira hanya matriks identitas yang sama dengan transposnya</sub>
- **B. $M$ merupakan matriks persegi** ✅  
  <sub>Benar: Jika $M$ berordo $m \times n$ maka $M^t$ berordo $n \times m$. Kedua matriks sama hanya bila $m = n$, sehingga $M$ persegi.</sub>
- C. $M$ merupakan matriks diagonal  
  <sub>Salah: menyamakan matriks simetris dengan diagonal; $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ memenuhi syarat tetapi bukan diagonal</sub>
- D. $M$ memuat paling sedikit satu elemen bernilai nol  
  <sub>Salah: mengira kesamaan dengan transpos menuntut elemen nol; $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ tidak memuat nol</sub>

**Pembahasan:** Ordo $M$ dan $M^t$ harus sama sehingga $M$ persegi. Contoh $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ menyangkal tiga pilihan lain.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b01-a-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan*

$K = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$

Seorang siswa menyatakan bahwa matriks $K$ bukan matriks diagonal karena ada elemen diagonal utama yang bernilai nol. Pernyataan yang tepat tentang penalaran siswa tersebut adalah ....

- A. Siswa benar: pada matriks diagonal semua elemen diagonal utama harus bukan nol, sehingga $K$ bukan matriks diagonal  
  <sub>Salah: membenarkan syarat yang tidak ada dalam definisi diagonal</sub>
- B. Siswa keliru: $K$ adalah matriks identitas karena semua elemen di luar diagonal utama bernilai nol  
  <sub>Salah: mencampuradukkan diagonal dengan identitas padahal diagonal utama $K$ tidak semuanya satu</sub>
- C. Siswa keliru: $K$ adalah matriks segitiga atas tetapi bukan matriks diagonal  
  <sub>Salah: mengira matriks yang memuat nol pada diagonal utama tidak lagi diagonal; elemen di bawah dan di atas diagonal nol</sub>
- **D. Siswa keliru: matriks diagonal hanya mensyaratkan elemen di luar diagonal utama bernilai nol, sehingga $K$ adalah matriks diagonal** ✅  
  <sub>Benar: Syarat matriks diagonal hanya menyangkut elemen di luar diagonal utama; elemen diagonal utama boleh bernilai nol.</sub>

**Pembahasan:** Contoh: $K = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 5 \end{pmatrix}$. Semua elemen di luar diagonal utama nol sehingga $K$ diagonal; nol pada diagonal utama diperbolehkan.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b01-a-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: banyak matriks yang memenuhi sifat*

Setiap elemen matriks simetris berordo $3 \times 3$ dipilih dari himpunan $\{0, 1\}$. Banyak matriks yang dapat dibentuk adalah ....

- A. $8$  
  <sub>Salah: hanya menghitung elemen diagonal utama ($2^3$)</sub>
- **B. $64$** ✅  
  <sub>Benar: Elemen yang bebas dipilih: $3$ pada diagonal utama dan $3$ di atas diagonal utama, yaitu $6$. Tiap elemen punya $2$ pilihan sehingga $2^6 = 64$.</sub>
- C. $512$  
  <sub>Salah: tidak memakai sifat simetris sehingga menghitung $2^9$</sub>
- D. $32$  
  <sub>Salah: salah menghitung banyak elemen bebas menjadi $5$ ($2^5$)</sub>

**Pembahasan:** $a_{ij} = a_{ji}$ sehingga hanya $3 + 3 = 6$ elemen yang bebas. Banyak matriks $= 2^6 = 64$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b01-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: banyak matriks yang memenuhi sifat*

Setiap elemen matriks persegi berordo $3 \times 3$ dipilih dari himpunan $\{0, 1, 2\}$. Banyak matriks yang sekaligus merupakan matriks segitiga bawah dan matriks simetris adalah ....

- **A. $27$** ✅  
  <sub>Benar: Segitiga bawah memaksa elemen di atas diagonal nol; simetris memaksa elemen di bawah diagonal sama dengan pasangannya, yaitu nol. Hanya $3$ elemen diagonal yang bebas: $3^3 = 27$.</sub>
- B. $729$  
  <sub>Salah: hanya memakai sifat segitiga bawah ($3^6$ untuk $6$ elemen bebas)</sub>
- C. $9$  
  <sub>Salah: mengalikan $3 \times 3$ alih-alih memangkatkan</sub>
- D. $81$  
  <sub>Salah: mengira ada empat elemen yang bebas ($3^4$)</sub>

**Pembahasan:** Matriksnya pasti diagonal. Tiga elemen diagonal masing-masing punya $3$ pilihan sehingga $3^3 = 27$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b01-a-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: syarat parameter dua jenis sekaligus*

Matriks $M = \begin{pmatrix} 3 & p + 4 & 0 \\ 3q - 6 & 6 & 2r + 2 \\ 0 & r + 1 & 8 \end{pmatrix}$ merupakan matriks segitiga atas sekaligus matriks simetris. Nilai $p + q + r$ adalah ....

- A. $5$  
  <sub>Salah: salah tanda pada $p$ ($p = 4$)</sub>
- B. $-7$  
  <sub>Salah: salah tanda pada $q$ ($q = -2$)</sub>
- **C. $-3$** ✅  
  <sub>Benar: Segitiga atas: $3q - 6 = 0$ dan $r + 1 = 0$, sehingga $q = 2$ dan $r = -1$. Simetris: $p + 4 = 3q - 6 = 0$ sehingga $p = -4$ (dan $2r + 2 = r + 1 = 0$ terpenuhi). Jadi $p + q + r = -3$.</sub>
- D. $-1$  
  <sub>Salah: salah tanda pada $r$ ($r = 1$)</sub>

**Pembahasan:** Elemen di bawah diagonal nol: $q = 2$, $r = -1$. Simetris: $p + 4 = 0$ sehingga $p = -4$. Hasil $-4 + 2 - 1 = -3$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b01-a-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: syarat parameter dua jenis sekaligus*

Matriks $A$ berordo $(k + 2) \times (10 - k)$ dengan $k$ bilangan asli. Jumlah semua kemungkinan banyak elemen $A$ jika $A$ merupakan matriks tegak tetapi bukan matriks kolom adalah ....

- A. $125$  
  <sub>Salah: ikut menghitung $k = 9$ ($11 \times 1$, matriks kolom)</sub>
- B. $150$  
  <sub>Salah: ikut menghitung $k = 4$ ($6 \times 6$, matriks persegi)</sub>
- **C. $114$** ✅  
  <sub>Benar: Tegak: $k + 2 > 10 - k$ sehingga $k > 4$. Bukan kolom: $10 - k \geq 2$ sehingga $k \leq 8$. Maka $k = 5, 6, 7, 8$ dengan banyak elemen $35, 32, 27, 20$, jumlahnya $114$.</sub>
- D. $79$  
  <sub>Salah: salah batas $k > 5$ sehingga melewatkan $k = 5$</sub>

**Pembahasan:** Syarat $k > 4$ dan $k \leq 8$ menghasilkan $k = 5, 6, 7, 8$. Jumlah $35 + 32 + 27 + 20 = 114$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b01-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Diberikan klaim: "Jika $A$ dan $A^t$ sama-sama matriks segitiga atas, maka $A$ adalah matriks identitas." Matriks berordo $3 \times 3$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- **A. $\begin{pmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 5 \end{pmatrix}$** ✅  
  <sub>Benar: Matriks ini dan transposnya (sama dengan dirinya) segitiga atas, tetapi diagonal utamanya bukan semuanya satu sehingga bukan identitas.</sub>
- B. $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$  
  <sub>Salah: ini matriks identitas, memenuhi klaim sehingga bukan penyangkal</sub>
- C. $\begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$  
  <sub>Salah: matriks ini sendiri bukan segitiga atas, sehingga syarat klaim tidak terpenuhi</sub>
- D. $\begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$  
  <sub>Salah: transposnya segitiga bawah, sehingga syarat klaim tidak terpenuhi</sub>

**Pembahasan:** Syarat klaim berarti $A$ diagonal. Penyangkal harus diagonal tetapi bukan identitas, yaitu $\operatorname{diag}(2, 3, 5)$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b01-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: rumus elemen dan sifat matriks*

Matriks $A = (a_{ij})$ berordo $3 \times 3$ dengan $i$ nomor baris dan $j$ nomor kolom. Aturan elemen yang menghasilkan matriks simetris yang bukan matriks diagonal adalah ....

- A. $a_{ij} = 2i - j$  
  <sub>Salah: $a_{12} = 0$ tetapi $a_{21} = 3$, tidak simetris</sub>
- B. $a_{ij} = i - j$  
  <sub>Salah: $a_{12} = -1$ tetapi $a_{21} = 1$, tidak simetris</sub>
- **C. $a_{ij} = i + j$** ✅  
  <sub>Benar: Untuk $i + j$: $a_{ij} = a_{ji}$ sehingga simetris, dan $a_{12} = 3 \neq 0$ sehingga bukan diagonal.</sub>
- D. $a_{ij} = i^2 j$  
  <sub>Salah: $a_{12} = 2$ tetapi $a_{21} = 4$, tidak simetris</sub>

**Pembahasan:** Periksa $a_{12}$ dan $a_{21}$: hanya $i + j$ yang memberi nilai sama ($3$ dan $3$), dan nilainya tidak nol.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b01-a-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: banyak elemen khusus*

Sebuah matriks segitiga atas berordo $n \times n$ memiliki tepat $45$ elemen yang pasti bernilai nol. Banyak elemen yang boleh bernilai tak nol pada matriks tersebut adalah ....

- A. $10$  
  <sub>Salah: hanya menghitung elemen diagonal utama</sub>
- **B. $55$** ✅  
  <sub>Benar: Elemen di bawah diagonal utama berjumlah $\frac{n(n-1)}{2} = 45$ sehingga $n = 10$. Elemen yang boleh tak nol: $\frac{n(n+1)}{2} = 55$.</sub>
- C. $45$  
  <sub>Salah: menjawab banyak elemen nol yang diketahui, bukan elemen tak nol</sub>
- D. $100$  
  <sub>Salah: menghitung semua elemen $n \times n$ tanpa memakai sifat segitiga</sub>

**Pembahasan:** $\frac{n(n-1)}{2} = 45 \Rightarrow n = 10$. Elemen pada dan di atas diagonal utama $= 55$.
**Acuan:** siswa — siswa hal.19

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
