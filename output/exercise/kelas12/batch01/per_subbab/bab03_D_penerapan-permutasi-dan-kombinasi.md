# Lembar koreksi — kelas12 SMA12U-B3 subbab D: Penerapan Permutasi dan Kombinasi

60 soal | easy 20, medium 20, hard 20 | variasi 20, orisinal 40

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b03-d-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: koefisien suku penjabaran*

Koefisien suku yang memuat $x^3$ dari penjabaran $(3 + x)^5$ adalah ....

- A. $30$  
  <sub>Salah: memangkatkan 3 hanya satu kali</sub>
- B. $270$  
  <sub>Salah: memangkatkan 3 dengan pangkat 3 (pangkat $x$) bukan $5-3$</sub>
- C. $10$  
  <sub>Salah: lupa mengalikan dengan $3^2$</sub>
- **D. $90$** ✅  
  <sub>Benar: $C_3^5 \cdot 3^{2} = 10 \times 9 = 90$</sub>

**Pembahasan:** Suku memuat $x^3$ berarti $r=3$, sehingga suku itu $C_3^5 \cdot 3^{5-3} x^3 = 10 \cdot 9 x^3 = 90x^3$. Koefisiennya 90.
**Acuan:** siswa — siswa hal.134 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b03-d-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: koefisien suku penjabaran*

Tentukan koefisien suku yang memuat $x^4$ dari penjabaran $(5 + x)^6$.

- A. $9.375$  
  <sub>Salah: memangkatkan 5 dengan pangkat 4 (pangkat $x$)</sub>
- B. $15$  
  <sub>Salah: lupa mengalikan dengan $5^2$</sub>
- **C. $375$** ✅  
  <sub>Benar: $C_4^6 \cdot 5^{2} = 15 \times 25 = 375$</sub>
- D. $75$  
  <sub>Salah: memangkatkan 5 hanya satu kali</sub>

**Pembahasan:** Koefisien suku $x^4$ adalah $C_4^6 \cdot 5^{6-4} = 15 \cdot 25 = 375$.
**Acuan:** siswa — siswa hal.134 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b03-d-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: banyak susunan tepat r berhasil*

Dalam suatu adu penalti, terdapat 7 penendang. Banyak susunan penendang di mana tepat 2 penendang berhasil mencetak gol adalah ....

- A. 14 cara  
  <sub>Salah: mengalikan $7 	imes 2$</sub>
- **B. 21 cara** ✅  
  <sub>Benar: urutan tidak diperhatikan: $C_2^7 = \frac{7 \times 6}{2} = 21$</sub>
- C. 42 cara  
  <sub>Salah: memakai permutasi $P(7,2)$ sehingga lupa membagi $2!$</sub>
- D. 35 cara  
  <sub>Salah: menghitung $C_3^7$ (tertukar jumlah yang berhasil)</sub>

**Pembahasan:** Memilih 2 penendang yang berhasil dari 7 tanpa memperhatikan urutan: $C_2^7 = 21$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b03-d-easy-bt01-004
*variasi (konteks) | C2 | 1 langkah | jenis: banyak susunan tepat r berhasil*

Seorang siswa mengerjakan 6 soal pilihan ganda. Banyak susunan soal yang dijawab benar jika tepat 4 soal dijawab benar adalah ....

- **A. 15 cara** ✅  
  <sub>Benar: $C_4^6 = \frac{6 \times 5}{2} = 15$</sub>
- B. 24 cara  
  <sub>Salah: mengalikan $6 	imes 4$</sub>
- C. 360 cara  
  <sub>Salah: memakai permutasi $P(6,4)$</sub>
- D. 20 cara  
  <sub>Salah: menghitung $C_3^6$</sub>

**Pembahasan:** Memilih 4 soal yang benar dari 6 soal: $C_4^6 = C_2^6 = 15$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b03-d-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: peluang binomial tepat r*

Seorang penjaga gawang berhasil menahan tendangan penalti dengan peluang 0,9. Jika ada 3 tendangan, peluang tepat 2 tendangan berhasil ditahan adalah ....

- A. $0,729$  
  <sub>Salah: menghitung peluang ketiganya berhasil ($0,9^3$)</sub>
- B. $0,081$  
  <sub>Salah: lupa mengalikan dengan $C_2^3 = 3$</sub>
- **C. $0,243$** ✅  
  <sub>Benar: $C_2^3 (0,9)^2 (0,1)^1 = 3 \times 0,81 \times 0,1 = 0,243$</sub>
- D. $0,27$  
  <sub>Salah: memangkatkan 0,9 hanya satu kali</sub>

**Pembahasan:** $P(2) = C_2^3 (0,9)^2 (0,1)^{3-2} = 3 \times 0,81 \times 0,1 = 0,243$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b03-d-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: peluang binomial tepat r*

Seorang pemain basket memiliki peluang 0,5 memasukkan bola pada setiap lemparan bebas. Dari 4 lemparan bebas, peluang tepat 2 lemparan masuk adalah ....

- **A. $0,375$** ✅  
  <sub>Benar: $C_2^4 (0,5)^2 (0,5)^2 = 6 \times 0,0625 = 0,375$</sub>
- B. $0,0625$  
  <sub>Salah: lupa mengalikan dengan $C_2^4 = 6$</sub>
- C. $0,25$  
  <sub>Salah: memakai $C_1^4 = 4$</sub>
- D. $0,75$  
  <sub>Salah: menghitung pangkat total hanya tiga kali ($6 \times 0,5^3$)</sub>

**Pembahasan:** $P(2) = C_2^4 (0,5)^2 (0,5)^{2} = 6 \times 0,0625 = 0,375$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b03-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: peluang binomial tepat r*

Tim voli sekolah akan bermain dalam 4 pertandingan. Peluang menang setiap pertandingan adalah 0,3. Peluang tim tersebut menang tepat 1 dari 4 pertandingan adalah ....

- A. $0,1029$  
  <sub>Salah: lupa mengalikan dengan $C_1^4 = 4$</sub>
- B. $0,588$  
  <sub>Salah: memangkatkan 0,7 dengan pangkat 2 saja</sub>
- C. $0,0756$  
  <sub>Salah: menukar peluang menang dan kalah</sub>
- **D. $0,4116$** ✅  
  <sub>Benar: $C_1^4 (0,3)^1 (0,7)^3 = 4 \times 0,3 \times 0,343 = 0,4116$</sub>

**Pembahasan:** $P(1) = C_1^4 (0,3)(0,7)^3 = 4 \times 0,3 \times 0,343 = 0,4116$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b03-d-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: peluang binomial tepat r*

Dari 5 siswa yang mengikuti simulasi, peluang seorang siswa lolos adalah 0,4. Peluang tepat 4 siswa lolos adalah ....

- A. $0,01536$  
  <sub>Salah: lupa mengalikan dengan $C_4^5 = 5$</sub>
- B. $0,128$  
  <sub>Salah: lupa mengalikan dengan peluang gagal $0,6$</sub>
- C. $0,2592$  
  <sub>Salah: menukar peluang lolos dan gagal</sub>
- **D. $0,0768$** ✅  
  <sub>Benar: $C_4^5 (0,4)^4 (0,6)^1 = 5 \times 0,0256 \times 0,6 = 0,0768$</sub>

**Pembahasan:** $P(4) = C_4^5 (0,4)^4 (0,6) = 5 \times 0,0256 \times 0,6 = 0,0768$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b03-d-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: koefisien model peluang*

Dina mengerjakan 6 soal pilihan ganda. Model peluang jawabannya ditulis $(b + 3s)^6$ dengan $b$ untuk jawaban benar dan $s$ untuk jawaban salah. Banyak cara Dina menjawab tepat 4 soal benar adalah koefisien suku $b^4 s^2$, yaitu ....

- A. $15$  
  <sub>Salah: lupa mengalikan dengan $3^2$</sub>
- **B. $135$** ✅  
  <sub>Benar: $C_4^6 \cdot 3^2 = 15 \times 9 = 135$</sub>
- C. $405$  
  <sub>Salah: memangkatkan 3 dengan pangkat 3</sub>
- D. $1.215$  
  <sub>Salah: memangkatkan 3 dengan pangkat 4 (pangkat $b$)</sub>

**Pembahasan:** Suku $b^4 s^2$ berkoefisien $C_4^6 \cdot 3^2 = 15 \cdot 9 = 135$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b03-d-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: koefisien model peluang*

Seorang atlet melakukan 4 kali tembakan. Model hasil tembakannya ditulis $(m + 2k)^4$ dengan $m$ untuk tembakan masuk dan $k$ untuk tembakan meleset. Banyak cara atlet itu mencetak tepat 3 tembakan masuk adalah koefisien suku $m^3 k$, yaitu ....

- A. $4$  
  <sub>Salah: lupa mengalikan dengan $2^1$</sub>
- B. $16$  
  <sub>Salah: memangkatkan 2 dengan pangkat 2</sub>
- C. $32$  
  <sub>Salah: memangkatkan 2 dengan pangkat 3 (pangkat $m$)</sub>
- **D. $8$** ✅  
  <sub>Benar: $C_3^4 \cdot 2^1 = 4 \times 2 = 8$</sub>

**Pembahasan:** Suku $m^3 k$ berkoefisien $C_3^4 \cdot 2 = 4 \cdot 2 = 8$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b03-d-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: banyak suku penjabaran*

Banyak suku pada penjabaran $(2x + y)^{11}$ adalah ....

- A. $22$  
  <sub>Salah: menggandakan pangkat karena ada dua variabel</sub>
- **B. $12$** ✅  
  <sub>Benar: penjabaran $(a+b)^n$ memiliki $n+1$ suku, yaitu $r = 0, 1, \dots, 11$</sub>
- C. $11$  
  <sub>Salah: mengira banyak suku sama dengan pangkat</sub>
- D. $10$  
  <sub>Salah: mengurangi pangkat dengan 1</sub>

**Pembahasan:** Indeks $r$ berjalan dari 0 sampai $n=11$, sehingga ada $11+1 = 12$ suku.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b03-d-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: segitiga Pascal*

Berdasarkan aturan segitiga Pascal, koefisien-koefisien pada penjabaran $(a + b)^4$ secara berurutan adalah ....

- A. $1, 5, 10, 10, 5, 1$  
  <sub>Salah: memakai baris untuk pangkat 5</sub>
- B. $1, 3, 3, 1$  
  <sub>Salah: memakai baris untuk pangkat 3</sub>
- C. $1, 4, 8, 4, 1$  
  <sub>Salah: mengira koefisien tengah dua kali koefisien kedua</sub>
- **D. $1, 4, 6, 4, 1$** ✅  
  <sub>Benar: baris ke-4 segitiga Pascal: $C_0^4, C_1^4, \dots, C_4^4 = 1, 4, 6, 4, 1$</sub>

**Pembahasan:** Baris untuk $n=4$ pada segitiga Pascal adalah 1, 4, 6, 4, 1.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b03-d-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: koefisien suku penjabaran*

Koefisien suku yang memuat $x^2 y^3$ pada penjabaran $(x + y)^5$ adalah ....

- A. $60$  
  <sub>Salah: memakai permutasi $P(5,3)$</sub>
- B. $20$  
  <sub>Salah: memakai permutasi $P(5,2)$</sub>
- **C. $10$** ✅  
  <sub>Benar: $C_2^5 = \frac{5 \times 4}{2} = 10$</sub>
- D. $5$  
  <sub>Salah: mengambil nilai $n$ sebagai koefisien</sub>

**Pembahasan:** Koefisien suku $x^2 y^3$ adalah $C_2^5 = 10$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b03-d-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: pemilihan posisi pemain*

Pelatih futsal memiliki 3 kandidat kiper, 5 kandidat anchor, dan 4 kandidat pivot. Banyak cara memilih satu kiper, satu anchor, dan satu pivot adalah ....

- A. 12 cara  
  <sub>Salah: menjumlahkan ketiga banyak kandidat</sub>
- B. 15 cara  
  <sub>Salah: melupakan satu posisi (pivot)</sub>
- **C. 60 cara** ✅  
  <sub>Benar: $3 \times 5 \times 4 = 60$</sub>
- D. 20 cara  
  <sub>Salah: melupakan satu posisi (kiper)</sub>

**Pembahasan:** Setiap posisi dipilih bebas, sehingga banyak cara $3 \times 5 \times 4 = 60$.
**Acuan:** siswa — siswa hal.132

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b03-d-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: peluang kejadian khusus*

Peluang seorang pasien sembuh setelah menjalani terapi adalah 0,9. Jika ada 4 pasien yang menjalani terapi, peluang keempat pasien sembuh adalah ....

- **A. $0,6561$** ✅  
  <sub>Benar: $C_4^4 (0,9)^4 (0,1)^0 = 1 \times 0,6561 = 0,6561$</sub>
- B. $0,3439$  
  <sub>Salah: menghitung peluang paling sedikit satu pasien tidak sembuh</sub>
- C. $0,729$  
  <sub>Salah: memangkatkan 0,9 hanya tiga kali</sub>
- D. $0,0001$  
  <sub>Salah: menghitung peluang keempatnya tidak sembuh</sub>

**Pembahasan:** $P(4) = C_4^4 (0,9)^4 (0,1)^0 = 0,6561$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b03-d-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: menentukan suku ke-k*

Suku ke-4 pada penjabaran $(a + b)^7$ dalam urutan pangkat $a$ menurun adalah ....

- **A. $35a^4b^3$** ✅  
  <sub>Benar: suku ke-4 berarti $r=3$: $C_3^7 a^{4} b^{3} = 35a^4b^3$</sub>
- B. $35a^3b^4$  
  <sub>Salah: pangkat $a$ dan $b$ tertukar</sub>
- C. $7a^6b$  
  <sub>Salah: mengambil suku ke-2 ($r=1$)</sub>
- D. $21a^5b^2$  
  <sub>Salah: mengambil suku ke-3 ($r=2$)</sub>

**Pembahasan:** Suku ke-$(r+1)$ adalah $C_r^7 a^{7-r} b^r$; untuk $r=3$ diperoleh $35a^4b^3$.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b03-d-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: menjabarkan binomial*

Hasil penjabaran $(x + 2)^3$ adalah ....

- A. $x^3 + 2x^2 + 4x + 8$  
  <sub>Salah: lupa koefisien segitiga Pascal 1, 3, 3, 1</sub>
- B. $x^3 + 6x^2 + 6x + 8$  
  <sub>Salah: pada suku ketiga memakai $3 \times 2$ bukan $3 \times 2^2$</sub>
- **C. $x^3 + 6x^2 + 12x + 8$** ✅  
  <sub>Benar: $x^3 + 3(2)x^2 + 3(2^2)x + 2^3$</sub>
- D. $x^3 + 3x^2 + 3x + 8$  
  <sub>Salah: lupa memangkatkan konstanta 2 pada suku tengah</sub>

**Pembahasan:** Koefisien Pascal 1, 3, 3, 1 dikalikan pangkat 2: $x^3 + 6x^2 + 12x + 8$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b03-d-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: segitiga Pascal*

Koefisien suku tengah pada penjabaran $(a + b)^6$ adalah ....

- A. $6$  
  <sub>Salah: mengambil koefisien suku kedua dari baris pangkat 6</sub>
- **B. $20$** ✅  
  <sub>Benar: suku tengah adalah suku ke-4: $C_3^6 = 20$</sub>
- C. $15$  
  <sub>Salah: mengambil koefisien suku kedua atau keenam</sub>
- D. $40$  
  <sub>Salah: menggandakan nilai koefisien tengah</sub>

**Pembahasan:** Baris pangkat 6: 1, 6, 15, 20, 15, 6, 1. Suku tengah berkoefisien 20.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b03-d-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: pengenalan rumus peluang binomial*

Peluang sukses setiap percobaan adalah $p$ dan peluang gagal $q = 1 - p$. Peluang tepat 3 sukses dari 5 percobaan dirumuskan sebagai ....

- A. $5\, p^3 q^2$  
  <sub>Salah: mengganti $C_3^5$ dengan $n$</sub>
- **B. $C_3^5\, p^3 q^2$** ✅  
  <sub>Benar: $P(r) = C_r^n p^r q^{n-r}$ dengan $n=5$, $r=3$</sub>
- C. $C_3^5\, p^2 q^3$  
  <sub>Salah: pangkat $p$ dan $q$ tertukar</sub>
- D. $C_3^5\, p^3 q^3$  
  <sub>Salah: pangkat $q$ ditulis $r$ bukan $n-r$</sub>

**Pembahasan:** Peluang tepat $r$ sukses dari $n$ percobaan adalah $C_r^n p^r q^{n-r}$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b03-d-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: peluang kejadian khusus*

Sebuah koin setimbang dilempar 5 kali. Peluang muncul sisi angka tepat 2 kali adalah ....

- **A. $0,3125$** ✅  
  <sub>Benar: $C_2^5 (0,5)^2 (0,5)^3 = 10 \times \frac{1}{32} = 0,3125$</sub>
- B. $0,625$  
  <sub>Salah: memangkatkan 0,5 empat kali bukan lima</sub>
- C. $0,15625$  
  <sub>Salah: memakai $C_1^5 = 5$</sub>
- D. $0,03125$  
  <sub>Salah: lupa mengalikan dengan $C_2^5 = 10$</sub>

**Pembahasan:** $P(2) = C_2^5 (0,5)^5 = 10 \times 0,03125 = 0,3125$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b03-d-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: koefisien (a+bx)^n*

Koefisien suku yang memuat $x^4$ dari penjabaran $(3 + 2x)^7$ adalah ....

- A. $22.680$  
  <sub>Salah: pangkat 3 dan 2 tertukar ($3^4 \cdot 2^3$)</sub>
- **B. $15.120$** ✅  
  <sub>Benar: $C_4^7 \cdot 3^{3} \cdot 2^{4} = 35 \times 27 \times 16 = 15.120$</sub>
- C. $945$  
  <sub>Salah: lupa mengalikan dengan $2^4$</sub>
- D. $3.780$  
  <sub>Salah: mengalikan 2 hanya empat kali pangkat dua ($2^2$ bukan $2^4$)</sub>

**Pembahasan:** Suku memuat $x^4$ berarti $r=4$: $C_4^7 \cdot 3^{7-4} \cdot (2x)^4 = 35 \cdot 27 \cdot 16 x^4 = 15.120x^4$. Koefisiennya 15.120.
**Acuan:** siswa — siswa hal.134 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b03-d-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: koefisien dengan tanda negatif*

Koefisien suku yang memuat $x^7$ dari penjabaran $(2 - x)^9$ adalah ....

- **A. $-144$** ✅  
  <sub>Benar: $C_7^9 \cdot 2^{2} \cdot (-1)^7 = 36 \times 4 \times (-1) = -144$</sub>
- B. $-36$  
  <sub>Salah: lupa mengalikan dengan $2^2$</sub>
- C. $-72$  
  <sub>Salah: memangkatkan 2 hanya satu kali</sub>
- D. $144$  
  <sub>Salah: mengabaikan tanda negatif pada $(-x)^7$</sub>

**Pembahasan:** Tulis $(2 + (-x))^9$. Untuk $r=7$: $C_7^9 \cdot 2^{9-7} \cdot (-x)^7 = 36 \cdot 4 \cdot (-x^7) = -144x^7$.
**Acuan:** siswa — siswa hal.134 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b03-d-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: peluang paling sedikit r*

Dalam adu penalti terdapat 6 penendang. Peluang paling sedikit 5 penendang mencetak gol, jika peluang setiap penendang adalah 0,7, adalah ....

- A. $0,302526$  
  <sub>Salah: hanya menghitung tepat 5 penendang</sub>
- B. $0,117649$  
  <sub>Salah: hanya menghitung keenam penendang berhasil</sub>
- **C. $0,420175$** ✅  
  <sub>Benar: $P(5)+P(6) = C_5^6 (0,7)^5 (0,3) + (0,7)^6 = 0,302526 + 0,117649 = 0,420175$</sub>
- D. $0,579825$  
  <sub>Salah: menghitung peluang paling banyak 4 penendang (komplemen)</sub>

**Pembahasan:** Paling sedikit 5 berarti tepat 5 atau tepat 6. $P(5) = 6 \cdot 0,16807 \cdot 0,3 = 0,302526$; $P(6) = 0,7^6 = 0,117649$. Jumlahnya 0,420175.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b03-d-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: peluang paling sedikit satu (komplemen)*

Seorang penembak memiliki peluang 0,6 mengenai sasaran pada setiap tembakan. Jika ia menembak 4 kali, peluang ia mengenai sasaran paling sedikit satu kali adalah ....

- **A. $0,9744$** ✅  
  <sub>Benar: $1 - P(0) = 1 - (0,4)^4 = 1 - 0,0256 = 0,9744$</sub>
- B. $0,8704$  
  <sub>Salah: menghitung peluang tidak semua tembakan mengenai ($1-0,6^4$)</sub>
- C. $0,0256$  
  <sub>Salah: menghitung peluang keempat tembakan meleset</sub>
- D. $0,1296$  
  <sub>Salah: menghitung peluang keempat tembakan mengenai sasaran</sub>

**Pembahasan:** Peluang tidak ada yang mengenai: $C_0^4 (0,6)^0 (0,4)^4 = 0,0256$. Paling sedikit satu mengenai: $1 - 0,0256 = 0,9744$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b03-d-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: banyak susunan paling sedikit r*

Dalam suatu adu penalti terdapat 9 penendang. Banyak susunan penendang di mana paling sedikit 7 penendang berhasil adalah ....

- A. 36 cara  
  <sub>Salah: hanya menghitung tepat 7 penendang berhasil</sub>
- **B. 46 cara** ✅  
  <sub>Benar: $C_7^9 + C_8^9 + C_9^9 = 36 + 9 + 1 = 46$</sub>
- C. 45 cara  
  <sub>Salah: melupakan kasus semua penendang berhasil</sub>
- D. 72 cara  
  <sub>Salah: memakai permutasi $P(9,2)$ untuk kasus tepat 7</sub>

**Pembahasan:** Paling sedikit 7 berarti tepat 7, 8, atau 9 berhasil: $C_7^9 + C_8^9 + C_9^9 = 36 + 9 + 1 = 46$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b03-d-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: banyak susunan dengan syarat tambahan*

Pada adu penalti dengan 8 penendang, dua penendang pertama dipastikan berhasil. Banyak susunan hasil yang mungkin jika tepat 5 penendang berhasil adalah ....

- **A. 20 cara** ✅  
  <sub>Benar: sisa 3 keberhasilan dipilih dari 6 penendang lain: $C_3^6 = 20$</sub>
- B. 56 cara  
  <sub>Salah: mengabaikan syarat dua penendang pertama ($C_5^8$)</sub>
- C. 35 cara  
  <sub>Salah: hanya satu penendang yang dianggap pasti berhasil ($C_4^7$)</sub>
- D. 15 cara  
  <sub>Salah: mengira tinggal 2 keberhasilan yang harus dipilih ($C_2^6$)</sub>

**Pembahasan:** Dua penendang pertama sudah berhasil, sehingga 3 keberhasilan lagi dipilih dari 6 penendang sisa: $C_3^6 = 20$.
**Acuan:** siswa — siswa hal.135 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b03-d-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: peluang paling sedikit r*

Tim voli sekolah dijadwalkan bermain dalam 5 pertandingan. Peluang menang setiap pertandingan adalah 0,9. Peluang tim tersebut menang paling sedikit 4 dari 5 pertandingan adalah ....

- **A. $0,91854$** ✅  
  <sub>Benar: $P(4)+P(5) = 5(0,9)^4(0,1) + (0,9)^5 = 0,32805 + 0,59049 = 0,91854$</sub>
- B. $0,08146$  
  <sub>Salah: menghitung peluang paling banyak 3 kemenangan</sub>
- C. $0,32805$  
  <sub>Salah: hanya menghitung tepat 4 pertandingan</sub>
- D. $0,59049$  
  <sub>Salah: hanya menghitung menang di semua pertandingan</sub>

**Pembahasan:** Paling sedikit 4 menang berarti tepat 4 atau 5. $P(4) = 5 \cdot 0,6561 \cdot 0,1 = 0,32805$ dan $P(5) = 0,59049$. Jumlahnya 0,91854.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b03-d-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: peluang binomial tepat r (pecahan)*

Dari 10 siswa peserta simulasi, peluang seorang siswa lolos adalah 0,5. Peluang tepat 9 siswa lolos adalah ....

- A. $\frac{5}{256}$  
  <sub>Salah: memangkatkan $rac{1}{2}$ hanya sembilan kali</sub>
- B. $\frac{1}{1024}$  
  <sub>Salah: lupa mengalikan dengan $C_9^{10} = 10$</sub>
- **C. $\frac{5}{512}$** ✅  
  <sub>Benar: $C_9^{10} (0,5)^9 (0,5)^1 = 10 \times \frac{1}{1024} = \frac{5}{512}$</sub>
- D. $\frac{45}{1024}$  
  <sub>Salah: memakai $C_2^{10} = 45$ (tertukar $r$ dengan banyak yang gagal)</sub>

**Pembahasan:** $P(9) = C_9^{10} (0,5)^9 (0,5)^1 = 10 \cdot \frac{1}{1024} = \frac{5}{512}$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b03-d-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: koefisien model dua koefisien*

Rina mengerjakan 6 soal pilihan ganda. Model peluang jawabannya ditulis $(4b + 3s)^6$ dengan $b$ untuk jawaban benar dan $s$ untuk jawaban salah. Koefisien suku $b^4 s^2$ pada model tersebut adalah ....

- A. $3.840$  
  <sub>Salah: lupa mengalikan dengan $3^2$</sub>
- **B. $34.560$** ✅  
  <sub>Benar: $C_4^6 \cdot 4^4 \cdot 3^2 = 15 \times 256 \times 9 = 34.560$</sub>
- C. $19.440$  
  <sub>Salah: pangkat 4 dan 3 tertukar ($4^2 \cdot 3^4$)</sub>
- D. $135$  
  <sub>Salah: lupa mengalikan dengan $4^4$</sub>

**Pembahasan:** Suku $b^4 s^2$ berkoefisien $C_4^6 \cdot 4^4 \cdot 3^2 = 15 \cdot 256 \cdot 9 = 34.560$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b03-d-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: peluang binomial tepat r*

Tim futsal dijadwalkan mengikuti 5 pertandingan awal dalam suatu turnamen. Peluang menang setiap pertandingan diperkirakan sebesar 0,9. Peluang tim futsal memenangkan tepat 3 dari 5 pertandingan tersebut adalah ....

- A. $0,0081$  
  <sub>Salah: menukar peluang menang dan kalah ($10 \times 0,001 \times 0,81$)</sub>
- B. $0,729$  
  <sub>Salah: hanya menghitung $(0,9)^3$ tanpa $C_3^5$ dan $(0,1)^2$</sub>
- C. $0,00729$  
  <sub>Salah: lupa mengalikan dengan $C_3^5 = 10$</sub>
- **D. $0,0729$** ✅  
  <sub>Benar: $C_3^5 (0,9)^3 (0,1)^2 = 10 \times 0,729 \times 0,01 = 0,0729$</sub>

**Pembahasan:** $P(3) = C_3^5 (0,9)^3 (0,1)^2 = 10 \cdot 0,729 \cdot 0,01 = 0,0729$.
**Acuan:** pretest — kelas12-b03-p0136-latihan-3-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b03-d-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: menentukan suku ke-k*

Suku ke-4 pada penjabaran $(3x + 2)^6$ dalam urutan pangkat $x$ menurun adalah ....

- A. $540x^3$  
  <sub>Salah: lupa memangkatkan 2 ($2^3$)</sub>
- B. $2.160x^2$  
  <sub>Salah: mengambil suku ke-5 ($r=4$)</sub>
- **C. $4.320x^3$** ✅  
  <sub>Benar: suku ke-4: $r=3$, $C_3^6 (3x)^3 (2)^3 = 20 \times 27 \times 8 \, x^3 = 4.320x^3$</sub>
- D. $4.860x^4$  
  <sub>Salah: mengambil suku ke-3 ($r=2$)</sub>

**Pembahasan:** Suku ke-$(r+1)$ adalah $C_r^6 (3x)^{6-r} 2^r$. Untuk $r=3$ diperoleh $20 \cdot 27x^3 \cdot 8 = 4.320x^3$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b03-d-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: suku tanpa variabel*

Koefisien suku yang tidak memuat $x$ (suku tetap) pada penjabaran $\left(x^2 + \frac{2}{x}\right)^6$ adalah ....

- A. $160$  
  <sub>Salah: memakai $r=3$ ($C_3^6 \cdot 2^3$) padahal pangkat $x$ nol terjadi pada $r=4$</sub>
- B. $60$  
  <sub>Salah: memangkatkan 2 hanya dua kali ($15 \times 2^2$)</sub>
- C. $15$  
  <sub>Salah: lupa mengalikan dengan $2^4$</sub>
- **D. $240$** ✅  
  <sub>Benar: suku umum: $C_r^6 \, x^{2(6-r)} \cdot 2^r x^{-r} = C_r^6 \, 2^r x^{12-3r}$; $12-3r=0$ sehingga $r=4$: $15 \times 16 = 240$</sub>

**Pembahasan:** Suku umum $C_r^6 (x^2)^{6-r} (2/x)^r = C_r^6 \, 2^r x^{12-3r}$. Pangkat $x$ nol bila $r=4$, sehingga koefisiennya $C_4^6 \cdot 2^4 = 15 \cdot 16 = 240$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b03-d-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: jumlah koefisien penjabaran*

Jumlah semua koefisien pada penjabaran $(2x + 3y)^4$ adalah ....

- A. $97$  
  <sub>Salah: menjumlahkan $2^4 + 3^4$ (hanya dua suku ujung)</sub>
- B. $20$  
  <sub>Salah: mengalikan 4 dengan jumlah koefisien dasar 5</sub>
- C. $125$  
  <sub>Salah: memangkatkan 5 dengan pangkat 3</sub>
- **D. $625$** ✅  
  <sub>Benar: substitusi $x=y=1$: $(2+3)^4 = 5^4 = 625$</sub>

**Pembahasan:** Jumlah koefisien didapat dengan $x=y=1$: $(2+3)^4 = 625$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b03-d-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: segitiga Pascal*

Diketahui baris segitiga Pascal untuk $(a + b)^6$ adalah 1, 6, 15, 20, 15, 6, 1. Jumlah koefisien suku ke-3 dan suku ke-4 pada penjabaran $(a + b)^7$ adalah ....

- **A. $56$** ✅  
  <sub>Benar: baris pangkat 7: $1, 7, 21, 35, 35, 21, 7, 1$; suku ke-3 dan ke-4: $21 + 35 = 56$</sub>
- B. $35$  
  <sub>Salah: memakai baris pangkat 6 ($15 + 20$)</sub>
- C. $41$  
  <sub>Salah: menjumlahkan 21 dengan 20 (suku ke-4 baris pangkat 6)</sub>
- D. $70$  
  <sub>Salah: menjumlahkan suku ke-4 dan ke-5 ($35 + 35$)</sub>

**Pembahasan:** Setiap bilangan sama dengan jumlah dua bilangan di atasnya: baris pangkat 7 adalah 1, 7, 21, 35, 35, 21, 7, 1. Suku ke-3 dan ke-4 berkoefisien 21 dan 35, jumlahnya 56.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b03-d-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: mencari n dari koefisien*

Koefisien suku ke-2 pada penjabaran $(1 + x)^n$ adalah 12. Koefisien suku ke-3 pada penjabaran tersebut adalah ....

- A. $24$  
  <sub>Salah: mengalikan $n$ dengan 2</sub>
- B. $132$  
  <sub>Salah: memakai permutasi $P(12,2)$</sub>
- C. $78$  
  <sub>Salah: mengambil $n=13$ ($C_2^{13}$)</sub>
- **D. $66$** ✅  
  <sub>Benar: suku ke-2: $C_1^n = n = 12$; suku ke-3: $C_2^{12} = \frac{12 \times 11}{2} = 66$</sub>

**Pembahasan:** Suku ke-2 berkoefisien $C_1^n = n$, sehingga $n=12$. Koefisien suku ke-3 adalah $C_2^{12} = 66$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b03-d-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: perbandingan peluang binomial*

Peluang seorang penendang mencetak gol adalah 0,6. Dari 5 tendangan, perbandingan peluang tepat 3 tendangan berhasil terhadap peluang tepat 2 tendangan berhasil adalah ....

- A. $2 : 3$  
  <sub>Salah: perbandingan tertukar</sub>
- B. $9 : 4$  
  <sub>Salah: mengira perbandingan $p : q$ dikuadratkan</sub>
- **C. $3 : 2$** ✅  
  <sub>Benar: $\frac{C_3^5 (0,6)^3 (0,4)^2}{C_2^5 (0,6)^2 (0,4)^3} = \frac{0,6}{0,4} = \frac{3}{2}$</sub>
- D. $1 : 1$  
  <sub>Salah: mengira $C_3^5 = C_2^5$ membuat kedua peluang sama</sub>

**Pembahasan:** $P(3) = 10 (0,6)^3 (0,4)^2$ dan $P(2) = 10 (0,6)^2 (0,4)^3$. Perbandingannya $0,6 : 0,4 = 3 : 2$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b03-d-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: suku tengah dari banyak suku*

Penjabaran $(x + y)^n$ memiliki 15 suku. Koefisien suku tengahnya adalah ....

- A. $3.003$  
  <sub>Salah: mengambil suku ke-7 ($C_6^{14}$)</sub>
- B. $6.435$  
  <sub>Salah: mengambil $n=15$ ($C_7^{15}$)</sub>
- C. $1.716$  
  <sub>Salah: mengambil $n=13$ ($C_6^{13}$)</sub>
- **D. $3.432$** ✅  
  <sub>Benar: $n+1=15$ sehingga $n=14$; suku tengah adalah suku ke-8: $C_7^{14} = 3.432$</sub>

**Pembahasan:** Banyak suku $n+1 = 15$ sehingga $n=14$. Suku tengah adalah suku ke-8 dengan koefisien $C_7^{14} = 3.432$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b03-d-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: peluang binomial pecahan (dadu)*

Sebuah dadu setimbang dilempar 4 kali. Peluang muncul mata dadu 6 tepat 2 kali adalah ....

- A. $\frac{25}{108}$  
  <sub>Salah: memakai permutasi $P(4,2)=12$ sebagai pengganti $C_2^4$</sub>
- **B. $\frac{25}{216}$** ✅  
  <sub>Benar: $C_2^4 \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^2 = 6 \times \frac{25}{1296} = \frac{25}{216}$</sub>
- C. $\frac{1}{216}$  
  <sub>Salah: mengira peluang bukan mata 6 juga $rac{1}{6}$</sub>
- D. $\frac{25}{1296}$  
  <sub>Salah: lupa mengalikan dengan $C_2^4 = 6$</sub>

**Pembahasan:** $P(2) = C_2^4 (1/6)^2 (5/6)^2 = 6 \cdot \frac{25}{1296} = \frac{25}{216}$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b03-d-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: gabungan dua koefisien*

Jumlah koefisien suku yang memuat $x^3$ dan koefisien suku yang memuat $x^2$ pada penjabaran $(2x - 3)^4$ adalah ....

- A. $312$  
  <sub>Salah: mengabaikan tanda negatif pada koefisien $x^3$</sub>
- B. $248$  
  <sub>Salah: koefisien $x^3$ dihitung tanpa faktor $-3$ ($4 \times 8 = 32$)</sub>
- **C. $120$** ✅  
  <sub>Benar: koefisien $x^3$: $C_3^4 \cdot 2^3 \cdot (-3) = -96$; koefisien $x^2$: $C_2^4 \cdot 2^2 \cdot (-3)^2 = 216$; jumlah $= 120$</sub>
- D. $216$  
  <sub>Salah: hanya menghitung koefisien $x^2$</sub>

**Pembahasan:** Koefisien $x^3$: $4 \cdot 8 \cdot (-3) = -96$. Koefisien $x^2$: $6 \cdot 4 \cdot 9 = 216$. Jumlahnya $-96 + 216 = 120$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b03-d-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: mencari parameter dari koefisien*

Diketahui $a > 0$ dan koefisien suku ke-3 pada penjabaran $(1 + ax)^6$ dalam urutan pangkat $x$ naik adalah 60. Nilai $a$ adalah ....

- A. $10$  
  <sub>Salah: memakai $r=1$ ($C_1^6 a = 6a = 60$)</sub>
- **B. $2$** ✅  
  <sub>Benar: suku ke-3: $r=2$, koefisien $C_2^6 a^2 = 15a^2 = 60$ sehingga $a^2 = 4$ dan $a = 2$</sub>
- C. $4$  
  <sub>Salah: berhenti pada $a^2 = 4$ tanpa mengambil akar</sub>
- D. $3$  
  <sub>Salah: memakai $r=3$ ($C_3^6 a^3 = 20a^3 = 60$)</sub>

**Pembahasan:** Suku ke-3 adalah $C_2^6 (ax)^2 = 15a^2 x^2$. Dari $15a^2 = 60$ diperoleh $a^2=4$ dan, karena $a>0$, $a=2$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b03-d-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan indeks suku ke-k*

Dina menentukan suku ke-4 pada penjabaran $(x + 2)^8$ (pangkat $x$ menurun) sebagai $C_4^8 \, x^4 \cdot 2^4 = 1.120x^4$. Koefisien suku ke-4 yang benar adalah ....

- A. $1.792$  
  <sub>Salah: pangkat $x$ dan pangkat 2 tertukar ($C_3^8 \cdot 2^5$)</sub>
- **B. $448$** ✅  
  <sub>Benar: suku ke-4 berarti $r=3$: $C_3^8 \, x^5 \cdot 2^3 = 56 \times 8 \, x^5 = 448x^5$</sub>
- C. $1.120$  
  <sub>Salah: mengulang kesalahan Dina: memakai $r=4$ untuk suku ke-4</sub>
- D. $56$  
  <sub>Salah: lupa mengalikan dengan $2^3$</sub>

**Pembahasan:** Suku ke-$(r+1)$ memakai $r$, sehingga suku ke-4 memakai $r=3$ (bukan 4). Suku tersebut $C_3^8 x^{5} 2^3 = 448x^5$. Kesalahan Dina: menyamakan $r$ dengan nomor suku.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b03-d-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: parameter dari suku tetap*

Diketahui $a > 0$. Suku tetap (suku yang tidak memuat $x$) pada penjabaran $\left(x^2 + \frac{a}{x}\right)^6$ bernilai $1.215$. Nilai $a$ adalah ....

- A. $81$  
  <sub>Salah: memakai nilai $a^4 = 81$ sebagai $a$</sub>
- B. $9$  
  <sub>Salah: berhenti pada $a^2 = 9$ tanpa menyelesaikan pangkat empat</sub>
- C. $27$  
  <sub>Salah: mengira suku tetap memakai $a^3$ dan mengambil $a^3 = 27$ sebagai nilai $a$</sub>
- **D. $3$** ✅  
  <sub>Benar: suku umum $C_r^6 a^r x^{12-3r}$; $r=4$ sehingga $15a^4 = 1.215$, $a^4 = 81$, $a = 3$</sub>

**Pembahasan:** Suku umum: $C_r^6 (x^2)^{6-r} (a/x)^r = C_r^6 a^r x^{12-3r}$. Suku tetap: $12-3r=0$, $r=4$, koefisien $15a^4 = 1.215$, $a^4 = 81$, $a=3$ karena $a>0$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b03-d-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: syarat adanya suku tetap*

Penjabaran $\left(x^3 + \frac{1}{x^2}\right)^n$ dengan $n$ bilangan bulat positif memuat suku tetap (tanpa $x$). Nilai $n$ terkecil yang memenuhi adalah ....

- A. $3$  
  <sub>Salah: mengambil pangkat $x$ pada suku pertama sebagai nilai $n$</sub>
- **B. $5$** ✅  
  <sub>Benar: pangkat $x$: $3(n-r) - 2r = 3n - 5r = 0$; $n$ harus kelipatan 5, terkecil $n=5$ ($r=3$)</sub>
- C. $6$  
  <sub>Salah: mengira $n$ harus kelipatan 3</sub>
- D. $2$  
  <sub>Salah: mengambil pangkat $x$ pada suku kedua sebagai nilai $n$</sub>

**Pembahasan:** Suku umum $C_r^n x^{3(n-r)} x^{-2r} = C_r^n x^{3n-5r}$. Agar pangkat nol, $3n = 5r$, sehingga $n$ kelipatan 5. $n$ terkecil adalah 5 dengan $r=3$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b03-d-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan tentang penjabaran*

Pernyataan yang benar tentang penjabaran $(a + b)^9$ adalah ....

- A. jumlah semua koefisiennya 18  
  <sub>Salah: jumlah koefisien adalah $2^9 = 512$, bukan $2 \times 9$</sub>
- B. suku ke-4 dan suku ke-5 memiliki koefisien yang sama  
  <sub>Salah: $C_3^9 = 84$ sedangkan $C_4^9 = 126$ (simetri terjadi pada suku ke-5 dan ke-6)</sub>
- **C. suku ke-5 dan suku ke-6 memiliki koefisien yang sama** ✅  
  <sub>Benar: $C_4^9 = C_5^9 = 126$, jadi koefisien suku ke-5 dan ke-6 sama</sub>
- D. penjabaran tersebut memiliki 9 suku  
  <sub>Salah: banyak suku $n+1 = 10$, bukan $n$</sub>

**Pembahasan:** Penjabaran $(a+b)^9$ punya 10 suku, jumlah koefisien $2^9 = 512$, koefisien suku ke-4 $=84$, suku ke-5 dan ke-6 sama-sama 126 (simetri $C_4^9 = C_5^9$).
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b03-d-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: identitas Pascal tanpa hitung penuh*

Nilai $C_2^8 + C_3^8 + C_4^9$ sama dengan ....

- A. $C_5^{10}$ dan bernilai $252$  
  <sub>Salah: salah menaikkan indeks bawah menjadi 5</sub>
- B. $C_5^9$ dan bernilai $126$  
  <sub>Salah: hanya menjumlahkan sekali dan keliru memakai simetri</sub>
- **C. $C_4^{10}$ dan bernilai $210$** ✅  
  <sub>Benar: $C_2^8 + C_3^8 = C_3^9$ (aturan Pascal), lalu $C_3^9 + C_4^9 = C_4^{10} = 210$</sub>
- D. $C_3^{10}$ dan bernilai $120$  
  <sub>Salah: salah memilih bilangan: mengira $C_3^9 + C_4^9 = C_3^{10}$</sub>

**Pembahasan:** Aturan Pascal: $C_{r-1}^{n} + C_r^{n} = C_r^{n+1}$. Maka $C_2^8 + C_3^8 = C_3^9$ dan $C_3^9 + C_4^9 = C_4^{10} = 210$.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b03-d-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: jumlah koefisien pangkat ganjil*

Jumlah semua koefisien suku berpangkat ganjil (yaitu $x$, $x^3$, $x^5$) pada penjabaran $(3x - 2)^5$ adalah ....

- **A. $1.563$** ✅  
  <sub>Benar: $f(1) = 1$ dan $f(-1) = (-5)^5 = -3.125$; jumlah koefisien pangkat ganjil $= \frac{f(1) - f(-1)}{2} = \frac{3.126}{2} = 1.563$</sub>
- B. $1$  
  <sub>Salah: mengira jumlah koefisien ganjil sama dengan jumlah semua koefisien $f(1)$</sub>
- C. $3.126$  
  <sub>Salah: lupa membagi dengan 2</sub>
- D. $-1.562$  
  <sub>Salah: itu jumlah koefisien berpangkat genap ($\frac{f(1)+f(-1)}{2}$)</sub>

**Pembahasan:** $f(x) = (3x-2)^5$. Jumlah koefisien pangkat ganjil $= \frac{f(1)-f(-1)}{2} = \frac{1-(-3.125)}{2} = \frac{3.126}{2} = 1.563$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b03-d-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: peluang binomial parameter p tak diketahui*

Seorang pemain memiliki peluang $p$ untuk berhasil pada setiap percobaan (saling bebas). Dari 3 percobaan, peluang tepat 2 kali berhasil sama dengan 4 kali peluang tepat 1 kali berhasil. Nilai $p$ adalah ....

- **A. $0,8$** ✅  
  <sub>Benar: $\frac{P(2)}{P(1)} = \frac{3p^2q}{3pq^2} = \frac{p}{q} = 4$ sehingga $p = 4q$ dan $p = 0,8$</sub>
- B. $0,25$  
  <sub>Salah: mengira $p = \frac{1}{4}$ dari perbandingan $p:q = 4$</sub>
- C. $0,2$  
  <sub>Salah: tertukar: nilai $q$ diambil sebagai $p$</sub>
- D. $0,75$  
  <sub>Salah: memakai perbandingan $3:1$ (mengambil $n=3$ sebagai angka perbandingan)</sub>

**Pembahasan:** $P(2) = 3p^2q$ dan $P(1) = 3pq^2$. Syarat $3p^2q = 4 \cdot 3pq^2$ memberi $p = 4q$. Karena $p+q=1$, $5q=1$, $q=0,2$, $p=0,8$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b03-d-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: peluang binomial n tak diketahui*

Sebuah koin setimbang dilempar $n$ kali. Peluang muncul tepat 2 sisi angka sama dengan peluang muncul tepat 5 sisi angka. Peluang muncul tepat 3 sisi angka dalam $n$ lemparan tersebut adalah ....

- **A. $\frac{35}{128}$** ✅  
  <sub>Benar: $C_2^n = C_5^n$ sehingga $n = 2 + 5 = 7$; $P(3) = C_3^7 \left(\frac{1}{2}\right)^7 = \frac{35}{128}$</sub>
- B. $\frac{21}{128}$  
  <sub>Salah: itu peluang tepat 2 (atau 5) sisi angka, bukan tepat 3</sub>
- C. $\frac{35}{256}$  
  <sub>Salah: memakai $\left(\frac{1}{2}\right)^8$ (mengira $n=8$)</sub>
- D. $\frac{35}{64}$  
  <sub>Salah: lupa memangkatkan penyebut sebanyak $n=7$ (memakai $2^6$)</sub>

**Pembahasan:** Karena $p=q=\frac{1}{2}$, $P(2)=P(5)$ berarti $C_2^n = C_5^n$, sehingga $n=7$. Maka $P(3) = C_3^7 \cdot \frac{1}{2^7} = \frac{35}{128}$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b03-d-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: peluang binomial parameter p tak diketahui*

Dalam 3 percobaan saling bebas, peluang semuanya berhasil adalah $\frac{8}{27}$. Peluang tepat 2 percobaan berhasil adalah ....

- A. $\frac{4}{27}$  
  <sub>Salah: lupa mengalikan dengan $C_2^3 = 3$</sub>
- B. $\frac{2}{9}$  
  <sub>Salah: memakai $p^1 q^2$ untuk tepat 2 berhasil ($3 \cdot \frac{2}{3} \cdot \frac{1}{9}$)</sub>
- C. $\frac{8}{27}$  
  <sub>Salah: menyalin peluang semua berhasil sebagai peluang tepat 2</sub>
- **D. $\frac{4}{9}$** ✅  
  <sub>Benar: $p^3 = \frac{8}{27}$ sehingga $p = \frac{2}{3}$; $P(2) = C_2^3 \left(\frac{2}{3}\right)^2 \left(\frac{1}{3}\right) = \frac{4}{9}$</sub>

**Pembahasan:** $p^3 = \frac{8}{27}$ memberi $p = \frac{2}{3}$, $q = \frac{1}{3}$. $P(2) = 3 \cdot \frac{4}{9} \cdot \frac{1}{3} = \frac{4}{9}$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b03-d-hard-bt01-010
*orisinal | C6 | 4 langkah | jenis: merancang n peluang paling sedikit satu*

Seorang pemain melempar koin setimbang sebanyak $n$ kali. Banyak lemparan $n$ minimum agar peluang muncul sisi angka paling sedikit satu kali lebih dari $0,99$ adalah ....

- A. $9$  
  <sub>Salah: memenuhi syarat tetapi bukan yang minimum dan salah menghitung kebutuhan $2^n$</sub>
- B. $6$  
  <sub>Salah: $1 - \frac{1}{64} \approx 0,984$ masih kurang dari $0,99$</sub>
- C. $8$  
  <sub>Salah: memenuhi syarat tetapi bukan yang minimum</sub>
- **D. $7$** ✅  
  <sub>Benar: $1 - \left(\frac{1}{2}\right)^n > 0,99$ berarti $2^n > 100$; $2^6 = 64$ belum cukup, $2^7 = 128$ cukup, jadi $n=7$</sub>

**Pembahasan:** Paling sedikit satu angka = $1 - P(0) = 1 - 2^{-n}$. Syarat $2^{-n} < 0,01$ berarti $2^n > 100$, sehingga $n$ minimum 7 ($1 - \frac{1}{128} \approx 0,992$).
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b03-d-hard-bt01-011
*orisinal | C6 | 4 langkah | jenis: merancang n peluang paling sedikit satu*

Sebuah perangkat mengirim sinyal berulang. Peluang sinyal diterima pada setiap pengiriman adalah $0,8$ (saling bebas). Banyak pengiriman minimum agar peluang paling sedikit satu sinyal diterima tidak kurang dari $0,999$ adalah ....

- A. $3$  
  <sub>Salah: $1 - 0,008 = 0,992$ jauh kurang dari $0,999$</sub>
- B. $4$  
  <sub>Salah: $1 - 0,0016 = 0,9984$ masih kurang dari $0,999$</sub>
- **C. $5$** ✅  
  <sub>Benar: $1 - (0,2)^n \geq 0,999$ berarti $(0,2)^n \leq 0,001$; $(0,2)^4 = 0,0016$ belum cukup, $(0,2)^5 = 0,00032$ cukup, jadi $n=5$</sub>
- D. $6$  
  <sub>Salah: memenuhi syarat tetapi bukan yang minimum</sub>

**Pembahasan:** Peluang tak ada sinyal diterima adalah $(0,2)^n$. Dibutuhkan $(0,2)^n \leq 0,001$. $n=4$ memberi $0,0016$ (belum), $n=5$ memberi $0,00032$ (cukup).
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b03-d-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: membandingkan dua peluang*

Peluang Ani menang pada setiap game adalah $0,6$ (saling bebas). Misalkan $X$ peluang Ani menang paling sedikit 2 dari 3 game dan $Y$ peluang Ani menang paling sedikit 3 dari 5 game. Pernyataan yang benar adalah ....

- A. $X = 0,216$ dan $Y = 0,07776$, sehingga $X > Y$  
  <sub>Salah: hanya menghitung kasus semua game dimenangkan</sub>
- **B. $X = 0,648$ dan $Y = 0,68256$, sehingga $Y > X$** ✅  
  <sub>Benar: $X = 3(0,6)^2(0,4) + (0,6)^3 = 0,648$; $Y = 10(0,6)^3(0,4)^2 + 5(0,6)^4(0,4) + (0,6)^5 = 0,3456 + 0,2592 + 0,07776 = 0,68256$</sub>
- C. $X = 0,648$ dan $Y = 0,3456$, sehingga $X > Y$  
  <sub>Salah: $Y$ hanya menghitung tepat 3 dari 5</sub>
- D. $X = 0,432$ dan $Y = 0,3456$, sehingga $X > Y$  
  <sub>Salah: hanya menghitung kasus tepat 2 dan tepat 3</sub>

**Pembahasan:** $X = 0,432 + 0,216 = 0,648$. $Y = 0,3456 + 0,2592 + 0,07776 = 0,68256$. Jadi $Y > X$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b03-d-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: membandingkan dua ekspansi*

Koefisien suku yang memuat $x^2$ pada penjabaran $(3 + x)^5$ lebih besar daripada koefisien suku yang memuat $x^2$ pada penjabaran $(1 + 3x)^5$. Selisih keduanya adalah ....

- **A. $180$** ✅  
  <sub>Benar: $(3+x)^5$: $C_2^5 \cdot 3^3 = 270$; $(1+3x)^5$: $C_2^5 \cdot 3^2 = 90$; selisih $= 180$</sub>
- B. $240$  
  <sub>Salah: memakai $3^3 \cdot 10 = 270$ tetapi koefisien kedua $30$ ($C_2^5 \cdot 3$)</sub>
- C. $90$  
  <sub>Salah: salah satu koefisien dianggap nol dan hanya $(1+3x)^5$ yang dipakai</sub>
- D. $360$  
  <sub>Salah: menjumlahkan kedua koefisien ($270 + 90$)</sub>

**Pembahasan:** Pada $(3+x)^5$, suku $x^2$: $C_2^5 3^3 x^2 = 270x^2$. Pada $(1+3x)^5$: $C_2^5 (3x)^2 = 90x^2$. Selisihnya 180.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b03-d-hard-bt01-014
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim*

Rani menyatakan bahwa jumlah semua bilangan pada baris untuk $(a+b)^n$ dalam segitiga Pascal selalu sama dengan $2n$. Nilai $n$ asli terkecil yang menjadi contoh penyangkal klaim Rani adalah ....

- A. $2$  
  <sub>Salah: baris pangkat 2 berjumlah $1+2+1=4=2 \cdot 2$ sehingga klaim masih benar</sub>
- B. $4$  
  <sub>Salah: memang menyangkal ($16 \neq 8$) tetapi bukan yang terkecil</sub>
- **C. $3$** ✅  
  <sub>Benar: jumlah baris $= 2^n$: $n=1$ (2 = 2) dan $n=2$ (4 = 4) cocok, $n=3$: $8 \neq 6$</sub>
- D. $1$  
  <sub>Salah: baris pangkat 1 berjumlah $1+1=2=2 \cdot 1$ sehingga klaim masih benar</sub>

**Pembahasan:** Jumlah bilangan baris pangkat $n$ adalah $2^n$. Klaim $2^n = 2n$ benar untuk $n=1,2$ tetapi salah untuk $n=3$ ($1+3+3+1=8 \neq 6$).
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b03-d-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: parameter dari rasio koefisien*

Pada penjabaran $(1 + 2x)^n$ dalam pangkat $x$ naik, koefisien suku ke-3 sama dengan 6 kali koefisien suku ke-2. Koefisien suku ke-4 adalah ....

- **A. $280$** ✅  
  <sub>Benar: $\frac{C_2^n \cdot 4}{C_1^n \cdot 2} = n - 1 = 6$ sehingga $n=7$; suku ke-4: $C_3^7 \cdot 2^3 = 35 \times 8 = 280$</sub>
- B. $140$  
  <sub>Salah: memangkatkan 2 hanya dua kali ($35 \times 4$)</sub>
- C. $560$  
  <sub>Salah: mengambil suku ke-5 ($C_4^7 \cdot 2^4$)</sub>
- D. $35$  
  <sub>Salah: lupa mengalikan dengan $2^3$</sub>

**Pembahasan:** Koefisien suku ke-2 $= 2n$, suku ke-3 $= 4C_2^n = 2n(n-1)$. Rasio $n-1 = 6$ memberi $n=7$. Suku ke-4: $C_3^7 2^3 = 280$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b03-d-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: peluang paling mungkin*

Sebuah koin setimbang dilempar 5 kali. Banyak nilai $r$ (dengan $r = 0, 1, \ldots, 5$) yang membuat peluang muncul tepat $r$ sisi angka bernilai paling besar adalah ....

- A. $1$  
  <sub>Salah: mengira nilai tengah tunggal ($r=2,5$ dibulatkan)</sub>
- **B. $2$** ✅  
  <sub>Benar: $P(r) = C_r^5 / 32$; $C_r^5$ terbesar $=10$ untuk $r=2$ dan $r=3$, jadi ada 2 nilai</sub>
- C. $6$  
  <sub>Salah: mengira semua nilai $r$ berpeluang sama</sub>
- D. $3$  
  <sub>Salah: mengira $r=2,3$ dan $r=4$ ikut terbesar</sub>

**Pembahasan:** Nilai $C_r^5$ untuk $r=0..5$: 1, 5, 10, 10, 5, 1. Terbesar 10 pada $r=2$ dan $r=3$, sehingga ada 2 nilai $r$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b03-d-hard-bt01-017
*orisinal | C5 | 3 langkah | jenis: evaluasi ekspresi peluang paling sedikit*

Peluang tepat $r$ keberhasilan dari 6 percobaan saling bebas dinyatakan $P(r)$. Ekspresi yang tepat untuk peluang paling sedikit 3 keberhasilan adalah ....

- A. $P(3) + P(4) + P(5)$  
  <sub>Salah: melupakan $P(6)$</sub>
- B. $1 - P(3)$  
  <sub>Salah: mengira komplemen 'paling sedikit 3' adalah 'tepat 3'</sub>
- C. $1 - P(0) - P(1) - P(2) - P(3)$  
  <sub>Salah: ikut mengurangkan $P(3)$ sehingga hasilnya paling sedikit 4</sub>
- **D. $1 - P(0) - P(1) - P(2)$** ✅  
  <sub>Benar: paling sedikit 3 $= P(3)+\ldots+P(6) = 1 - (P(0)+P(1)+P(2))$</sub>

**Pembahasan:** Himpunan 'paling sedikit 3' adalah $r=3,4,5,6$. Komplemennya $r=0,1,2$, sehingga peluangnya $1 - P(0) - P(1) - P(2)$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b03-d-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: peluang banyak keberhasilan genap*

Peluang sebuah sensor menyala pada setiap percobaan adalah $0,3$ (saling bebas). Dalam 4 percobaan, peluang banyak sensor yang menyala adalah bilangan genap (termasuk 0) adalah ....

- A. $0,2646$  
  <sub>Salah: hanya menghitung tepat 2</sub>
- B. $0,5$  
  <sub>Salah: mengira peluang genap dan ganjil selalu sama</sub>
- **C. $0,5128$** ✅  
  <sub>Benar: $P(0)+P(2)+P(4) = 0,2401 + 0,2646 + 0,0081 = 0,5128$</sub>
- D. $0,4872$  
  <sub>Salah: itu peluang banyak menyala ganjil ($P(1)+P(3)$)</sub>

**Pembahasan:** $P(0) = 0,7^4 = 0,2401$; $P(2) = 6(0,09)(0,49) = 0,2646$; $P(4) = 0,0081$. Jumlah $= 0,5128$.
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b03-d-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: suku tetap dengan evaluasi langkah*

Siti menyelesaikan suku tetap pada $\left(2x + \frac{1}{x^2}\right)^9$ dan hanya menulis $r=3$. Koefisien suku tetap pada penjabaran tersebut adalah ....

- A. $672$  
  <sub>Salah: memakai $2^r = 2^3$, bukan $2^{9-r} = 2^6$</sub>
- B. $43.008$  
  <sub>Salah: memangkatkan 2 dengan 9 ($84 \times 2^9$)</sub>
- C. $84$  
  <sub>Salah: lupa mengalikan dengan $2^6$</sub>
- **D. $5.376$** ✅  
  <sub>Benar: suku umum $C_r^9 2^{9-r} x^{9-3r}$; $r=3$: $C_3^9 \cdot 2^6 = 84 \times 64 = 5.376$</sub>

**Pembahasan:** $C_r^9 (2x)^{9-r} (x^{-2})^r = C_r^9 2^{9-r} x^{9-3r}$. Pangkat nol saat $r=3$, sehingga koefisiennya $84 \cdot 64 = 5.376$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b03-d-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: dua parameter dari dua koefisien*

Pada penjabaran $(1 + ax)^n$ dengan $a > 0$ dalam pangkat $x$ naik, koefisien suku ke-2 adalah 12 dan koefisien suku ke-3 adalah 54. Nilai $n + a$ adalah ....

- A. $5$  
  <sub>Salah: memakai $n=2$ dan $a=3$ (salah membagi dua persamaan)</sub>
- **B. $7$** ✅  
  <sub>Benar: $na = 12$ dan $\frac{n(n-1)}{2}a^2 = 54$; dibagi menghasilkan $n=4$ dan $a=3$, jadi $n+a=7$</sub>
- C. $16$  
  <sub>Salah: mengira $n+a = 12 + 4$ (mengambil $na$ dan $n$)</sub>
- D. $12$  
  <sub>Salah: menyalin $na=12$ sebagai $n+a$</sub>

**Pembahasan:** Suku ke-2: $na=12$. Suku ke-3: $\frac{n(n-1)}{2}a^2 = 54$. Dari $(na)^2\frac{n-1}{n} = 108$ diperoleh $144\cdot\frac{n-1}{n}=108$, $n=4$, $a=3$. Jadi $n+a=7$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
