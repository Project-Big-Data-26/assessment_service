# Lembar koreksi — kelas12 SMA12U-B4 subbab A: Peluang Suatu Kejadian

60 soal | easy 20, medium 20, hard 20 | variasi 20, orisinal 40

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b04-a-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: peluang jumlah tiga dadu*

Tiga dadu standar bersisi enam yang setimbang dilempar bersama-sama. Berapakah peluang jumlah total mata dadu pada ketiga pelemparan sama dengan 10?

- **A. $\frac{1}{8}$** ✅  
  <sub>Benar: ruang sampel $6 \times 6 \times 6 = 216$ dan ada 27 susunan berurutan yang berjumlah 10, sehingga $\frac{27}{216} = \frac{1}{8}$</sub>
- B. $\frac{1}{36}$  
  <sub>Salah: hanya menghitung 6 himpunan angka tanpa memperhatikan urutan</sub>
- C. $\frac{1}{216}$  
  <sub>Salah: menganggap hanya ada satu susunan yang berjumlah 10</sub>
- D. $\frac{5}{108}$  
  <sub>Salah: menyamakan banyak susunan dengan angka 10 (10/216)</sub>

**Pembahasan:** $n(S) = 216$. Susunan berurutan berjumlah 10 ada 27 (mis. 1-3-6 ada 6 susunan, 2-2-6 ada 3 susunan, dst.). Peluang $= \frac{27}{216} = \frac{1}{8}$.
**Acuan:** pretest — kelas12-b04-p0155-latihan-4-1-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b04-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: peluang jumlah tiga dadu*

Tiga dadu standar bersisi enam yang setimbang dilempar bersama-sama. Berapakah peluang jumlah total mata dadu pada ketiga pelemparan sama dengan 8?

- A. $\frac{1}{216}$  
  <sub>Salah: menganggap hanya ada satu susunan yang berjumlah 8</sub>
- B. $\frac{5}{216}$  
  <sub>Salah: hanya menghitung 5 himpunan angka tanpa memperhatikan urutan</sub>
- **C. $\frac{7}{72}$** ✅  
  <sub>Benar: ada 21 susunan berurutan berjumlah 8 dari 216 hasil, sehingga $\frac{21}{216} = \frac{7}{72}$</sub>
- D. $\frac{1}{27}$  
  <sub>Salah: menyamakan banyak susunan dengan angka 8 (8/216)</sub>

**Pembahasan:** $n(S) = 216$. Susunan berjumlah 8: 1-1-6 (3), 1-2-5 (6), 1-3-4 (6), 2-2-4 (3), 2-3-3 (3) sehingga 21. Peluang $= \frac{21}{216} = \frac{7}{72}$.
**Acuan:** pretest — kelas12-b04-p0155-latihan-4-1-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b04-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: peluang dua pelemparan beruntun*

Pada sisi-sisi sebuah dadu setimbang terdapat angka, yakni: 3, 3, 8, 9, 9, dan 10. Berapa peluang terambilnya angka kedua lebih kecil dari angka pertama jika dadu itu dilempar sebanyak dua kali?

- A. $\frac{5}{12}$  
  <sub>Salah: menganggap keenam angka berbeda sehingga ada 15 pasangan</sub>
- B. $\frac{5}{18}$  
  <sub>Salah: menghitung pasangan dengan angka sama, bukan yang lebih kecil</sub>
- C. $\frac{23}{36}$  
  <sub>Salah: menghitung pasangan 'tidak lebih besar' (lebih kecil atau sama)</sub>
- **D. $\frac{13}{36}$** ✅  
  <sub>Benar: ada $6 \times 6 = 36$ pasangan sisi; pasangan dengan angka kedua lebih kecil ada 13, sehingga $\frac{13}{36}$</sub>

**Pembahasan:** Pasangan (pertama, kedua) dengan kedua lebih kecil: pertama 8 ada 1x2=2, pertama 9 ada 2x3=6, pertama 10 ada 1x5=5, pertama 3 ada 0. Jumlah 13 dari 36.
**Acuan:** siswa — siswa hal.155 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b04-a-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: peluang pengambilan sekaligus*

Diberikan 7 kelereng merah, 6 kelereng hijau, dan 8 kelereng biru dalam suatu kotak. Jika diambil tiga kelereng sekaligus dari kotak, berapakah peluang ketiga kelereng yang terambil semuanya berwarna merah?

- A. $\frac{1}{27}$  
  <sub>Salah: memakai pengambilan satu per satu dengan pengembalian, $(\frac{7}{21})^3$</sub>
- **B. $\frac{1}{38}$** ✅  
  <sub>Benar: $n(S) = C(21,3) = 1.330$ dan $n(A) = C(7,3) = 35$, sehingga $\frac{35}{1330} = \frac{1}{38}$</sub>
- C. $\frac{1}{3}$  
  <sub>Salah: hanya menghitung peluang satu kelereng merah, $\frac{7}{21}$</sub>
- D. $\frac{1}{190}$  
  <sub>Salah: menganggap $C(7,3) = 7$</sub>

**Pembahasan:** $n(S) = C(21,3) = 1.330$, $n(A) = C(7,3) = 35$. $P(A) = \frac{35}{1330} = \frac{1}{38}$.
**Acuan:** siswa — siswa hal.151 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b04-a-easy-bt01-005
*variasi (konteks) | C2 | 2 langkah | jenis: peluang pengambilan sekaligus*

Sebuah kantong berisi 6 bola kuning, 3 bola putih, dan 4 bola hitam. Tiga bola diambil sekaligus secara acak. Peluang terambil dua bola kuning dan satu bola hitam adalah ....

- A. $\frac{24}{143}$  
  <sub>Salah: memakai $6 \times 2$ sebagai banyak cara memilih dua bola kuning, bukan $C(6,2)$</sub>
- B. $\frac{19}{286}$  
  <sub>Salah: menjumlahkan $C(6,2) + C(4,1)$ padahal kedua pilihan terjadi bersamaan (dikalikan)</sub>
- C. $\frac{60}{2197}$  
  <sub>Salah: membagi dengan $13^3$ seolah pengambilan dengan pengembalian</sub>
- **D. $\frac{30}{143}$** ✅  
  <sub>Benar: $n(S) = C(13,3) = 286$ dan $n(A) = C(6,2) \times C(4,1) = 15 \times 4 = 60$, sehingga $\frac{60}{286} = \frac{30}{143}$</sub>

**Pembahasan:** $n(S) = C(13,3) = 286$. $n(A) = C(6,2) \cdot C(4,1) = 60$. $P = \frac{60}{286} = \frac{30}{143}$.
**Acuan:** siswa — siswa hal.152 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b04-a-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: peluang pengambilan sekaligus*

Dalam sebuah kotak terdapat 3 pulpen, 5 pensil, dan 6 penghapus. Tiga benda diambil sekaligus secara acak dari kotak. Peluang terambil masing-masing satu pulpen, satu pensil, dan satu penghapus adalah ....

- A. $\frac{15}{364}$  
  <sub>Salah: memakai penyebut berurutan $14 \times 13 \times 12$ (urutan diperhatikan) padahal pembilang tanpa urutan</sub>
- B. $\frac{45}{1372}$  
  <sub>Salah: membagi dengan $14^3$ seolah pengambilan dengan pengembalian</sub>
- C. $\frac{1}{26}$  
  <sub>Salah: menjumlahkan $3 + 5 + 6 = 14$ sebagai banyak cara, bukan dikalikan</sub>
- **D. $\frac{45}{182}$** ✅  
  <sub>Benar: $n(S) = C(14,3) = 364$ dan $n(A) = 3 \times 5 \times 6 = 90$, sehingga $\frac{90}{364} = \frac{45}{182}$</sub>

**Pembahasan:** $n(S) = C(14,3) = 364$. $n(A) = 3 \cdot 5 \cdot 6 = 90$. $P = \frac{90}{364} = \frac{45}{182}$.
**Acuan:** siswa — siswa hal.152 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b04-a-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: banyak cara memilih (kombinasi)*

Menjelang pergantian kepengurusan OSIS SMA Bhakti 27, akan dibentuk panitia inti sebanyak 5 orang saja. Calon panitia tersebut ada 12 orang. Berapa banyak cara memilih panitia inti tersebut?

- A. 95.040 cara  
  <sub>Salah: memakai permutasi $P(12,5)$ padahal susunan tidak diperhatikan</sub>
- B. 60 cara  
  <sub>Salah: mengalikan 12 dan 5</sub>
- **C. 792 cara** ✅  
  <sub>Benar: susunan tidak diperhatikan sehingga memakai kombinasi: $C(12,5) = 792$</sub>
- D. 17 cara  
  <sub>Salah: menjumlahkan 12 dan 5</sub>

**Pembahasan:** Susunan tidak diperhatikan, jadi $C(12,5) = \frac{12!}{5!\,7!} = 792$ cara.
**Acuan:** siswa — siswa hal.144 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b04-a-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: peluang satu dadu*

Sebuah dadu setimbang bersisi enam digelindingkan satu kali. Peluang sisi atas yang muncul merupakan bilangan kelipatan 3 adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: menganggap ada 3 bilangan kelipatan 3 (3, 6, 9)</sub>
- **B. $\frac{1}{3}$** ✅  
  <sub>Benar: kelipatan 3 pada dadu adalah 3 dan 6 (2 hasil dari 6): $\frac{2}{6} = \frac{1}{3}$</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: menghitung peluang bukan kelipatan 3</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: hanya menghitung angka 3</sub>

**Pembahasan:** Ruang sampel $\{1,2,3,4,5,6\}$, kejadian $\{3,6\}$, sehingga $P = \frac{2}{6} = \frac{1}{3}$.
**Acuan:** siswa — siswa hal.146 Ayo, Bereksplorasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b04-a-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: peluang pengambilan satu benda*

Sebuah kotak berisi 7 kartu bernomor 1 sampai 7 yang identik. Dengan mata tertutup, Rafi mengambil satu kartu dari kotak itu. Sebelumnya ia menebak nomor 4. Peluang kartu yang terambil sesuai tebakannya adalah ....

- A. $\frac{6}{7}$  
  <sub>Salah: menghitung peluang tebakan salah</sub>
- **B. $\frac{1}{7}$** ✅  
  <sub>Benar: hanya 1 kartu bernomor 4 dari 7 kartu yang sama mungkin terambil: $\frac{1}{7}$</sub>
- C. $\frac{4}{7}$  
  <sub>Salah: memakai nomor tebakan 4 sebagai banyak kartu yang menguntungkan</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: menganggap hanya 4 kartu yang mungkin terambil</sub>

**Pembahasan:** Ruang sampel 7 kartu, kejadian tebakan benar hanya 1 kartu: $P = \frac{1}{7}$.
**Acuan:** siswa — siswa hal.146 Ayo, Bereksplorasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b04-a-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: peluang empirik*

Sebuah koin dilempar 80 kali dan sisi angka muncul 46 kali. Peluang empirik muncul sisi angka adalah ....

- A. $\frac{40}{23}$  
  <sub>Salah: membalik pembilang dan penyebut</sub>
- B. $\frac{17}{40}$  
  <sub>Salah: menghitung peluang empirik sisi gambar</sub>
- **C. $\frac{23}{40}$** ✅  
  <sub>Benar: peluang empirik $= \frac{\text{frekuensi}}{\text{banyak percobaan}} = \frac{46}{80} = \frac{23}{40}$</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: memakai peluang teoretis koin setimbang, bukan data percobaan</sub>

**Pembahasan:** Peluang empirik $= \frac{46}{80} = \frac{23}{40}$.
**Acuan:** siswa — siswa hal.149 Ayo, Berkolaborasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b04-a-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: peluang dua pelemparan beruntun*

Sebuah papan putar dibagi menjadi lima sektor sama besar yang diberi bilangan 2, 3, 5, 7, dan 11. Papan itu diputar dua kali dan penunjuk selalu berhenti di salah satu sektor secara acak. Peluang bilangan putaran kedua lebih kecil dari bilangan putaran pertama adalah ....

- **A. $\frac{2}{5}$** ✅  
  <sub>Benar: ada $5 \times 5 = 25$ pasangan; pasangan dengan bilangan kedua lebih kecil ada $4+3+2+1 = 10$, sehingga $\frac{10}{25} = \frac{2}{5}$</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: menghitung pasangan 'lebih kecil atau sama' (10 + 5 = 15)</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: mengira lebih kecil dan lebih besar masing-masing separuh, tanpa memperhatikan pasangan sama</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: menghitung peluang kedua bilangan sama</sub>

**Pembahasan:** Pasangan berurutan 25. Kedua lebih kecil: 3 melawan 2 (1), 5 (2), 7 (3), 11 (4) sehingga 10. Peluang $\frac{10}{25} = \frac{2}{5}$.
**Acuan:** siswa — siswa hal.155 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b04-a-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: peluang pengambilan sekaligus*

Sebuah kotak berisi 12 kartu, di antaranya 5 kartu bertanda bintang. Dua kartu diambil sekaligus secara acak. Peluang kedua kartu yang terambil semuanya bertanda bintang adalah ....

- **A. $\frac{5}{33}$** ✅  
  <sub>Benar: $n(S) = C(12,2) = 66$ dan $n(A) = C(5,2) = 10$, sehingga $\frac{10}{66} = \frac{5}{33}$</sub>
- B. $\frac{25}{132}$  
  <sub>Salah: mengalikan $\frac{5}{12} \times \frac{5}{11}$ tanpa mengurangi banyak kartu bintang</sub>
- C. $\frac{25}{144}$  
  <sub>Salah: memakai pengambilan dengan pengembalian, $(\frac{5}{12})^2$</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: membagi $C(5,2) = 10$ dengan 12</sub>

**Pembahasan:** $n(S) = C(12,2) = 66$, $n(A) = C(5,2) = 10$. $P = \frac{10}{66} = \frac{5}{33}$.
**Acuan:** siswa — siswa hal.152 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b04-a-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: peluang komplemen*

Menurut prakiraan cuaca, peluang hujan turun besok adalah 0,35. Peluang besok tidak turun hujan adalah ....

- A. 0,35  
  <sub>Salah: menganggap peluang tidak hujan sama dengan peluang hujan</sub>
- B. 0,53  
  <sub>Salah: menukar posisi angka 3 dan 5 saat mengurangkan</sub>
- **C. 0,65** ✅  
  <sub>Benar: kejadian tidak hujan adalah komplemen dari hujan: $1 - 0,35 = 0,65$</sub>
- D. 1,35  
  <sub>Salah: menjumlahkan 1 dan 0,35</sub>

**Pembahasan:** $P(A^c) = 1 - P(A) = 1 - 0,35 = 0,65$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b04-a-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: kisaran nilai peluang*

Nilai berikut yang tidak mungkin menjadi peluang suatu kejadian adalah ....

- A. $0$  
  <sub>Salah: nilai 0 adalah peluang kemustahilan, masih dalam kisaran</sub>
- B. $\frac{7}{8}$  
  <sub>Salah: nilai ini berada di antara 0 dan 1 sehingga boleh menjadi peluang</sub>
- C. $1$  
  <sub>Salah: nilai 1 adalah peluang kepastian, masih dalam kisaran</sub>
- **D. $\frac{9}{8}$** ✅  
  <sub>Benar: peluang berada pada kisaran $0 \le P(A) \le 1$, sedangkan $\frac{9}{8} > 1$</sub>

**Pembahasan:** Peluang harus memenuhi $0 \le P(A) \le 1$. Hanya $\frac{9}{8}$ yang lebih dari 1.
**Acuan:** siswa — siswa hal.149

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b04-a-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: kemustahilan dan kepastian*

Dua dadu standar bersisi enam yang setimbang dilempar bersama-sama. Peluang jumlah mata kedua dadu lebih dari 12 adalah ....

- A. $\frac{1}{36}$  
  <sub>Salah: mengira jumlah 12 ikut dihitung sebagai 'lebih dari 12'</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: menebak peluang setengah tanpa memeriksa nilai jumlah terbesar</sub>
- **C. $0$** ✅  
  <sub>Benar: jumlah terbesar dua dadu adalah 12 sehingga kejadian itu mustahil dan peluangnya 0</sub>
- D. $1$  
  <sub>Salah: mengira jumlah selalu lebih dari 12 (kepastian)</sub>

**Pembahasan:** Jumlah terbesar $6 + 6 = 12$, jadi tidak ada hasil dengan jumlah lebih dari 12. Kejadian mustahil, $P = 0$.
**Acuan:** siswa — siswa hal.149

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b04-a-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: ruang sampel*

Tiga koin uang logam yang setimbang dilempar bersama-sama. Banyak anggota ruang sampelnya adalah ....

- A. 9  
  <sub>Salah: memakai $3^2$, mengira tiap sisi memiliki 3 hasil</sub>
- **B. 8** ✅  
  <sub>Benar: tiap koin punya 2 hasil sehingga ruang sampel $2 \times 2 \times 2 = 8$</sub>
- C. 5  
  <sub>Salah: menjumlahkan banyak koin dan banyak sisi, $3 + 2$</sub>
- D. 6  
  <sub>Salah: mengalikan banyak koin dengan banyak sisi, $3 \times 2$</sub>

**Pembahasan:** Setiap koin memiliki 2 hasil, jadi $n(S) = 2^3 = 8$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b04-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: peluang jumlah dua dadu*

Dua dadu standar bersisi enam yang setimbang dilempar bersama-sama. Peluang jumlah mata kedua dadu sama dengan 9 adalah ....

- A. $\frac{1}{18}$  
  <sub>Salah: tidak memperhatikan urutan, hanya (3,6) dan (4,5)</sub>
- **B. $\frac{1}{9}$** ✅  
  <sub>Benar: ada 4 pasangan berjumlah 9, yaitu (3,6), (4,5), (5,4), (6,3), dari 36 pasangan: $\frac{4}{36} = \frac{1}{9}$</sub>
- C. $\frac{1}{11}$  
  <sub>Salah: menganggap 11 jumlah yang mungkin (2 sampai 12) sama-sama mungkin</sub>
- D. $\frac{1}{36}$  
  <sub>Salah: menghitung hanya satu pasangan</sub>

**Pembahasan:** $n(S) = 36$. Pasangan berjumlah 9: (3,6), (4,5), (5,4), (6,3). $P = \frac{4}{36} = \frac{1}{9}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b04-a-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: peluang empirik*

Sebuah dadu dilempar sebanyak 90 kali dan mata dadu 4 muncul 18 kali. Peluang empirik muncul mata dadu 4 adalah ....

- **A. $\frac{1}{5}$** ✅  
  <sub>Benar: peluang empirik $= \frac{18}{90} = \frac{1}{5}$</sub>
- B. $\frac{1}{6}$  
  <sub>Salah: memakai peluang teoretis dadu setimbang, bukan data percobaan</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: membagi 18 dengan banyak lemparan yang tidak menghasilkan mata 4</sub>
- D. $\frac{1}{18}$  
  <sub>Salah: memakai frekuensi 18 sebagai penyebut</sub>

**Pembahasan:** Peluang empirik $= \frac{\text{frekuensi}}{\text{banyak percobaan}} = \frac{18}{90} = \frac{1}{5}$.
**Acuan:** siswa — siswa hal.148

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b04-a-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: peluang pengambilan satu benda*

Satu kartu diambil secara acak dari seperangkat kartu bridge standar yang terdiri dari 52 kartu tanpa joker. Peluang terambil kartu As adalah ....

- **A. $\frac{1}{13}$** ✅  
  <sub>Benar: ada 4 kartu As dari 52 kartu: $\frac{4}{52} = \frac{1}{13}$</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: memakai banyak jenis kartu (4) sebagai penyebut</sub>
- C. $\frac{1}{52}$  
  <sub>Salah: menganggap hanya ada satu kartu As</sub>
- D. $\frac{1}{12}$  
  <sub>Salah: membagi 4 dengan 48 (mengurangi banyak As dari 52)</sub>

**Pembahasan:** $n(S) = 52$ dan $n(A) = 4$, sehingga $P = \frac{4}{52} = \frac{1}{13}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b04-a-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: cara undian yang adil*

Adi dan Ani mengundi siapa yang lebih dulu memakai komputer. Cara yang adil, yaitu keduanya memiliki peluang sama, adalah ....

- A. menggelindingkan satu dadu setimbang: jika muncul mata 6 maka Ani lebih dulu, selain itu Adi lebih dulu  
  <sub>Salah: peluang Ani $\frac{1}{6}$ sedangkan Adi $\frac{5}{6}$, tidak sama</sub>
- B. menggelindingkan satu dadu setimbang: jika muncul mata 1 atau 2 maka Adi lebih dulu, selain itu Ani lebih dulu  
  <sub>Salah: peluang Adi $\frac{2}{6}$ sedangkan Ani $\frac{4}{6}$, tidak sama</sub>
- C. mengambil satu dari tiga kelereng merah, kuning, hijau yang identik: jika merah maka Adi lebih dulu, selain itu Ani lebih dulu  
  <sub>Salah: peluang Adi $\frac{1}{3}$ sedangkan Ani $\frac{2}{3}$, tidak sama</sub>
- **D. mengetos satu koin setimbang: jika muncul angka maka Adi lebih dulu, jika muncul gambar maka Ani lebih dulu** ✅  
  <sub>Benar: peluang angka dan gambar masing-masing $\frac{1}{2}$, sehingga keduanya memiliki kesempatan yang sama</sub>

**Pembahasan:** Cara adil bila peluang kedua pihak sama. Koin: $\frac{1}{2}$ dan $\frac{1}{2}$. Dadu mata 6: $\frac{1}{6}$ vs $\frac{5}{6}$. Dadu mata 1 atau 2: $\frac{1}{3}$ vs $\frac{2}{3}$. Kelereng: $\frac{1}{3}$ vs $\frac{2}{3}$.
**Acuan:** siswa — siswa hal.146

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b04-a-medium-bt01-001
*variasi (konteks) | C3 | 3 langkah | jenis: peluang jumlah tiga dadu*

Tiga siswa masing-masing mengambil satu bola secara acak dari kantong terpisah; setiap kantong berisi enam bola identik bernomor 1 sampai 6. Berapakah peluang jumlah ketiga nomor bola yang terambil sama dengan 14?

- A. $\frac{1}{18}$  
  <sub>Salah: menganggap tiap himpunan angka hanya punya 3 susunan padahal {3,5,6} punya 6 susunan</sub>
- B. $\frac{1}{54}$  
  <sub>Salah: hanya menghitung 4 himpunan angka tanpa memperhatikan urutan</sub>
- C. $\frac{7}{108}$  
  <sub>Salah: menyamakan banyak susunan dengan angka 14 (14/216)</sub>
- **D. $\frac{5}{72}$** ✅  
  <sub>Benar: himpunan angka berjumlah 14: {2,6,6} (3 susunan), {3,5,6} (6), {4,4,6} (3), {4,5,5} (3) sehingga 15 susunan dari 216: $\frac{15}{216} = \frac{5}{72}$</sub>

**Pembahasan:** $n(S) = 6^3 = 216$. Himpunan angka berjumlah 14: {2,6,6}, {3,5,6}, {4,4,6}, {4,5,5} dengan 3, 6, 3, 3 susunan, jadi 15. $P = \frac{15}{216} = \frac{5}{72}$.
**Acuan:** siswa — siswa hal.155 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b04-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: peluang dua pelemparan beruntun*

Pada sisi-sisi sebuah dadu setimbang terdapat angka, yakni: 3, 9, 9, 13, 13, dan 13. Berapa peluang terambilnya angka kedua lebih kecil dari angka pertama jika dadu itu dilempar sebanyak dua kali?

- A. $\frac{7}{18}$  
  <sub>Salah: menghitung pasangan dengan angka sama, bukan yang lebih kecil</sub>
- B. $\frac{25}{36}$  
  <sub>Salah: menghitung pasangan 'lebih kecil atau sama'</sub>
- C. $\frac{5}{12}$  
  <sub>Salah: menganggap keenam angka berbeda sehingga ada 15 pasangan</sub>
- **D. $\frac{11}{36}$** ✅  
  <sub>Benar: ada $6 \times 6 = 36$ pasangan sisi; angka pertama 9 (2 sisi) mengalahkan 1 sisi bernilai 3: $2 \times 1 = 2$; angka pertama 13 (3 sisi) mengalahkan 3 sisi lain (3, 9, 9): $3 \times 3 = 9$; jumlah 11 pasangan</sub>

**Pembahasan:** Pasangan (pertama, kedua) dengan kedua lebih kecil: pertama 3 ada 0; pertama 9 ada 2 sisi x 1 sisi (angka 3) = 2; pertama 13 ada 3 sisi x 3 sisi (3, 9, 9) = 9. Jumlah 11 dari 36, peluang $\frac{11}{36}$.
**Acuan:** siswa — siswa hal.155 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b04-a-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: peluang pengambilan sekaligus*

Diberikan 8 kelereng merah, 5 kelereng hijau, dan 7 kelereng biru dalam suatu kotak. Jika diambil empat kelereng sekaligus dari kotak, berapakah peluang keempat kelereng yang terambil semuanya berwarna merah?

- A. $\frac{16}{625}$  
  <sub>Salah: memakai pengambilan satu per satu dengan pengembalian, $(\frac{8}{20})^4$</sub>
- **B. $\frac{14}{969}$** ✅  
  <sub>Benar: $n(S) = C(20,4) = 4.845$ dan $n(A) = C(8,4) = 70$, sehingga $\frac{70}{4845} = \frac{14}{969}$</sub>
- C. $\frac{2}{5}$  
  <sub>Salah: hanya menghitung peluang satu kelereng merah</sub>
- D. $\frac{112}{323}$  
  <sub>Salah: memakai $P(8,4) = 1.680$ untuk pembilang padahal susunan tidak diperhatikan</sub>

**Pembahasan:** $n(S) = C(20,4) = 4.845$, $n(A) = C(8,4) = 70$. $P(A) = \frac{70}{4845} = \frac{14}{969}$.
**Acuan:** siswa — siswa hal.151 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b04-a-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: peluang pengambilan sekaligus*

Sebuah tim olimpiade terdiri dari 5 siswa putra dan 4 siswa putri. Tiga siswa dipilih sekaligus secara acak untuk mewakili sekolah. Peluang terpilih dua siswa putri dan satu siswa putra adalah ....

- A. $\frac{80}{243}$  
  <sub>Salah: memakai pengambilan dengan pengembalian, $3 \times (\frac{4}{9})^2 \times \frac{5}{9}$</sub>
- B. $\frac{11}{84}$  
  <sub>Salah: menjumlahkan $C(4,2) + C(5,1) = 11$ padahal dua pilihan terjadi bersamaan (dikalikan)</sub>
- C. $\frac{10}{21}$  
  <sub>Salah: menukar jumlah putra dan putri: $C(5,2) \times C(4,1) = 40$</sub>
- **D. $\frac{5}{14}$** ✅  
  <sub>Benar: $n(S) = C(9,3) = 84$ dan $n(A) = C(4,2) \times C(5,1) = 6 \times 5 = 30$, sehingga $\frac{30}{84} = \frac{5}{14}$</sub>

**Pembahasan:** $n(S) = C(9,3) = 84$. $n(A) = C(4,2) \cdot C(5,1) = 30$. $P = \frac{30}{84} = \frac{5}{14}$.
**Acuan:** siswa — siswa hal.152 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b04-a-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: peluang pengambilan sekaligus*

Dari sembilan siswa terdapat 4 siswa kelas X, 3 siswa kelas XI, dan 2 siswa kelas XII. Tiga siswa dipilih sekaligus secara acak untuk menjadi regu. Peluang regu itu beranggotakan masing-masing satu siswa dari kelas X, kelas XI, dan kelas XII adalah ....

- A. $\frac{3}{28}$  
  <sub>Salah: menjumlahkan $4 + 3 + 2 = 9$ sebagai banyak cara, bukan dikalikan</sub>
- **B. $\frac{2}{7}$** ✅  
  <sub>Benar: $n(S) = C(9,3) = 84$ dan $n(A) = 4 \times 3 \times 2 = 24$, sehingga $\frac{24}{84} = \frac{2}{7}$</sub>
- C. $\frac{1}{21}$  
  <sub>Salah: memakai penyebut permutasi $P(9,3) = 504$ padahal regu tidak memperhatikan urutan</sub>
- D. $\frac{4}{21}$  
  <sub>Salah: memakai $C(9,4) = 126$ sebagai penyebut</sub>

**Pembahasan:** $n(S) = C(9,3) = 84$. $n(A) = 4 \cdot 3 \cdot 2 = 24$. $P = \frac{24}{84} = \frac{2}{7}$.
**Acuan:** siswa — siswa hal.152 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b04-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: banyak cara memilih (permutasi)*

Menjelang pergantian kepengurusan OSIS SMA Nusantara, dibentuk panitia inti sebanyak 5 orang yang terdiri dari ketua, wakil ketua, sekretaris, bendahara, dan koordinator acara, terdapat 11 orang yang menjadi calon panitia tersebut. Berapa banyak cara memilih panitia inti?

- **A. 55.440 cara** ✅  
  <sub>Benar: jabatan berbeda sehingga susunan diperhatikan: $P(11,5) = 11 \times 10 \times 9 \times 8 \times 7 = 55.440$</sub>
- B. 161.051 cara  
  <sub>Salah: mengira satu orang boleh memegang beberapa jabatan, $11^5$</sub>
- C. 462 cara  
  <sub>Salah: memakai kombinasi $C(11,5)$ padahal tiap jabatan berbeda</sub>
- D. 7.920 cara  
  <sub>Salah: hanya mengisi 4 jabatan, $P(11,4)$</sub>

**Pembahasan:** Susunan diperhatikan: $P(11,5) = \frac{11!}{6!} = 11 \times 10 \times 9 \times 8 \times 7 = 55.440$ cara.
**Acuan:** siswa — siswa hal.143 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b04-a-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: peluang satu dadu*

Sebuah dadu setimbang bersisi dua belas dengan sisi bernomor 1 sampai 12 digelindingkan satu kali. Peluang sisi atas yang muncul merupakan bilangan prima adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: melewatkan bilangan prima 11</sub>
- **B. $\frac{5}{12}$** ✅  
  <sub>Benar: bilangan prima dari 1 sampai 12: 2, 3, 5, 7, 11 (5 hasil dari 12): $\frac{5}{12}$</sub>
- C. $\frac{5}{11}$  
  <sub>Salah: membagi dengan 11 padahal ada 12 sisi</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: menganggap 1 sebagai bilangan prima</sub>

**Pembahasan:** Ruang sampel $\{1,2,\dots,12\}$, kejadian prima $\{2,3,5,7,11\}$, sehingga $P = \frac{5}{12}$.
**Acuan:** siswa — siswa hal.146 Ayo, Bereksplorasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b04-a-medium-bt01-008
*variasi (konteks) | C3 | 3 langkah | jenis: peluang empirik*

| Mata dadu | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Frekuensi | 22 | 27 | 31 | 20 | 24 | 26 |

Sebuah dadu dilempar sebanyak 150 kali dengan hasil seperti pada tabel. Peluang empirik muncul mata dadu bilangan prima adalah ....

- A. $\frac{34}{75}$  
  <sub>Salah: menghitung peluang empirik mata yang bukan prima</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: memakai peluang teoretis dadu setimbang, bukan data percobaan</sub>
- **C. $\frac{41}{75}$** ✅  
  <sub>Benar: frekuensi mata prima (2, 3, 5) adalah $27 + 31 + 24 = 82$ dari 150 percobaan: $\frac{82}{150} = \frac{41}{75}$</sub>
- D. $\frac{29}{75}$  
  <sub>Salah: melewatkan mata 5 (frekuensi 24)</sub>

**Pembahasan:** Frekuensi mata prima $= 27 + 31 + 24 = 82$. Peluang empirik $= \frac{82}{150} = \frac{41}{75}$.
**Acuan:** siswa — siswa hal.149 Ayo, Berkolaborasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b04-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: peluang komplemen*

Empat koin uang logam yang setimbang dilempar bersama-sama. Peluang muncul paling sedikit satu sisi angka adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: menghitung tepat satu angka saja</sub>
- B. $\frac{7}{8}$  
  <sub>Salah: memakai ruang sampel 8 (seolah hanya tiga koin)</sub>
- C. $\frac{1}{16}$  
  <sub>Salah: menghitung komplemennya (semua gambar), bukan kejadian yang ditanyakan</sub>
- **D. $\frac{15}{16}$** ✅  
  <sub>Benar: komplemennya adalah keempat koin gambar dengan peluang $\frac{1}{16}$, sehingga $1 - \frac{1}{16} = \frac{15}{16}$</sub>

**Pembahasan:** $n(S) = 2^4 = 16$. Tidak ada angka hanya 1 hasil (GGGG). $P = 1 - \frac{1}{16} = \frac{15}{16}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b04-a-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: peluang jumlah dua dadu*

Dua dadu standar bersisi enam yang setimbang dilempar bersama-sama. Peluang jumlah mata kedua dadu merupakan bilangan prima adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: menghitung jumlah ganjil, bukan jumlah prima</sub>
- B. $\frac{5}{11}$  
  <sub>Salah: menganggap 11 jumlah yang mungkin sama-sama mungkin dan 5 di antaranya prima</sub>
- **C. $\frac{5}{12}$** ✅  
  <sub>Benar: banyak pasangan berjumlah 2, 3, 5, 7, 11 berturut-turut 1, 2, 4, 6, 2 sehingga total 15 dari 36: $\frac{15}{36} = \frac{5}{12}$</sub>
- D. $\frac{13}{36}$  
  <sub>Salah: melewatkan pasangan berjumlah 11 yang berjumlah 2 susunan</sub>

**Pembahasan:** $n(S) = 36$. Jumlah 2: 1; 3: 2; 5: 4; 7: 6; 11: 2. Total 15. $P = \frac{15}{36} = \frac{5}{12}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b04-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: pengambilan tanpa pengembalian*

Sebuah kotak berisi 5 bola merah dan 3 bola putih yang identik selain warnanya. Dua bola diambil satu per satu secara acak tanpa pengembalian. Peluang kedua bola yang terambil berwarna sama adalah ....

- **A. $\frac{13}{28}$** ✅  
  <sub>Benar: $n(S) = C(8,2) = 28$; dua merah $C(5,2) = 10$ dan dua putih $C(3,2) = 3$, sehingga $\frac{13}{28}$</sub>
- B. $\frac{5}{14}$  
  <sub>Salah: hanya menghitung kasus dua bola merah</sub>
- C. $\frac{13}{56}$  
  <sub>Salah: membagi pembilang kombinasi dengan $P(8,2) = 56$</sub>
- D. $\frac{17}{32}$  
  <sub>Salah: memakai pengambilan dengan pengembalian</sub>

**Pembahasan:** $n(S) = C(8,2) = 28$. Dua merah: $C(5,2) = 10$. Dua putih: $C(3,2) = 3$. $P = \frac{13}{28}$.
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b04-a-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: pengambilan dengan pengembalian*

Sebuah kotak berisi 4 bola merah dan 6 bola biru. Satu bola diambil secara acak, dicatat warnanya, lalu dikembalikan. Pengambilan dilakukan tiga kali. Peluang terambil tepat dua bola merah adalah ....

- **A. $\frac{36}{125}$** ✅  
  <sub>Benar: $n(S) = 10^3 = 1.000$; ada 3 posisi bola biru, tiap susunan $4 \times 4 \times 6 = 96$ cara, sehingga $n(A) = 288$ dan $P = \frac{288}{1000} = \frac{36}{125}$</sub>
- B. $\frac{8}{125}$  
  <sub>Salah: menghitung ketiganya merah, $(\frac{4}{10})^3$</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: memakai pengambilan tanpa pengembalian</sub>
- D. $\frac{12}{125}$  
  <sub>Salah: lupa memperhitungkan 3 posisi bola biru (urutan)</sub>

**Pembahasan:** $n(S) = 10^3 = 1.000$. Tiga susunan (MMB, MBM, BMM), masing-masing $4 \cdot 4 \cdot 6 = 96$. $n(A) = 288$. $P = \frac{288}{1000} = \frac{36}{125}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b04-a-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: peluang pemilihan dengan komplemen*

Dari 6 siswa putra dan 4 siswa putri dipilih tiga siswa sekaligus secara acak untuk menjadi panitia. Peluang panitia itu memuat paling sedikit satu siswa putri adalah ....

- A. $\frac{2}{5}$  
  <sub>Salah: menghitung peluang satu orang terpilih putri</sub>
- **B. $\frac{5}{6}$** ✅  
  <sub>Benar: komplemen: ketiganya putra, $\frac{C(6,3)}{C(10,3)} = \frac{20}{120} = \frac{1}{6}$, sehingga $1 - \frac{1}{6} = \frac{5}{6}$</sub>
- C. $\frac{1}{6}$  
  <sub>Salah: menghitung peluang tidak ada putri (komplemen), bukan kejadian yang ditanyakan</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: hanya menghitung tepat satu putri</sub>

**Pembahasan:** $n(S) = C(10,3) = 120$. Tanpa putri: $C(6,3) = 20$. $P = 1 - \frac{20}{120} = \frac{5}{6}$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b04-a-medium-bt01-014
*orisinal | C4 | 2 langkah | jenis: interpretasi nilai peluang*

Menurut prakiraan cuaca, peluang turun hujan di Kota B besok adalah 0,7. Pernyataan yang paling tepat adalah ....

- A. Tidak hujan lebih mungkin daripada hujan karena 0,7 kurang dari 1.  
  <sub>Salah: membandingkan peluang dengan 1, bukan dengan peluang komplemennya 0,3</sub>
- **B. Hujan besok lebih mungkin terjadi daripada tidak hujan.** ✅  
  <sub>Benar: peluang hujan 0,7 lebih besar dari peluang tidak hujan $1 - 0,7 = 0,3$, tetapi belum pasti</sub>
- C. Besok pasti turun hujan.  
  <sub>Salah: menganggap peluang 0,7 sama dengan kepastian</sub>
- D. Dalam 10 hari berikutnya, tepat 7 hari pasti turun hujan.  
  <sub>Salah: menganggap peluang selalu menghasilkan frekuensi persis sama pada percobaan terbatas</sub>

**Pembahasan:** Peluang hujan 0,7 dan tidak hujan 0,3. Karena 0,7 > 0,3, hujan lebih mungkin, tetapi bukan pasti (kepastian bernilai 1).
**Acuan:** siswa — siswa hal.153

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b04-a-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: peluang gabungan dua sifat*

Satu kartu diambil secara acak dari seperangkat kartu bridge standar yang terdiri dari 52 kartu tanpa joker. Peluang kartu yang terambil adalah kartu hati atau kartu As adalah ....

- **A. $\frac{4}{13}$** ✅  
  <sub>Benar: kartu hati 13 dan As 4, tetapi As hati terhitung dua kali sehingga $13 + 4 - 1 = 16$: $\frac{16}{52} = \frac{4}{13}$</sub>
- B. $\frac{3}{52}$  
  <sub>Salah: hanya menghitung 3 kartu As yang bukan hati</sub>
- C. $\frac{17}{52}$  
  <sub>Salah: menjumlahkan 13 + 4 tanpa mengurangi As hati yang terhitung dua kali</sub>
- D. $\frac{1}{13}$  
  <sub>Salah: hanya menghitung kartu As</sub>

**Pembahasan:** Hati 13 kartu, As 4 kartu, As hati terhitung dua kali. $n(A) = 13 + 4 - 1 = 16$. $P = \frac{16}{52} = \frac{4}{13}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b04-a-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: peluang bilangan hasil susunan angka*

Dari angka 1, 2, 3, 4, dan 5 disusun bilangan tiga angka dengan angka yang berbeda. Satu bilangan dipilih secara acak. Peluang bilangan yang terpilih merupakan bilangan genap adalah ....

- **A. $\frac{2}{5}$** ✅  
  <sub>Benar: $n(S) = P(5,3) = 60$; satuan 2 atau 4 (2 pilihan), ratusan 4 pilihan, puluhan 3 pilihan: $2 \times 4 \times 3 = 24$, sehingga $\frac{24}{60} = \frac{2}{5}$</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: menghitung bilangan ganjil, bukan genap</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: menganggap separuh bilangan genap padahal angka 1-5 hanya memuat dua angka genap</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: menghitung bilangan genap tanpa memperhatikan pilihan puluhan dan ratusan, hanya $2 \times 3 \times 2$</sub>

**Pembahasan:** $n(S) = 5 \times 4 \times 3 = 60$. Genap: satuan 2 atau 4 (2 cara), ratusan 4 cara, puluhan 3 cara = 24. $P = \frac{24}{60} = \frac{2}{5}$.
**Acuan:** siswa — siswa hal.143

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b04-a-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: mencari parameter dari peluang*

Sebuah kotak berisi $n$ kelereng merah dan 4 kelereng biru. Jika satu kelereng diambil secara acak, peluang terambil kelereng merah adalah $\frac{3}{5}$. Nilai $n$ adalah ....

- A. 2  
  <sub>Salah: menyelesaikan $\frac{n}{n+4} = \frac{3}{5}$ dengan $5n = 3n + 4$</sub>
- B. 3  
  <sub>Salah: menyamakan $n$ dengan pembilang peluang</sub>
- **C. 6** ✅  
  <sub>Benar: $\frac{n}{n+4} = \frac{3}{5}$ sehingga $5n = 3n + 12$ dan $n = 6$</sub>
- D. 9  
  <sub>Salah: menyusun persamaan $rac{n}{n+4} = rac{3}{5}$ lalu salah menghitung, $3 	imes 3$</sub>

**Pembahasan:** $P = \frac{n}{n+4} = \frac{3}{5}$. Kali silang: $5n = 3(n+4) = 3n + 12$, $2n = 12$, $n = 6$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b04-a-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: peluang empirik*

Sebuah koin dilempar 120 kali dan sisi angka muncul 78 kali. Selisih antara peluang empirik muncul angka dan peluang teoretis muncul angka pada koin setimbang adalah ....

- A. $\frac{13}{20}$  
  <sub>Salah: hanya menghitung peluang empirik tanpa mengurangi peluang teoretis</sub>
- B. $\frac{3}{40}$  
  <sub>Salah: membagi selisih 3/20 dengan 2</sub>
- C. $\frac{7}{20}$  
  <sub>Salah: menghitung peluang empirik sisi gambar, $rac{42}{120}$</sub>
- **D. $\frac{3}{20}$** ✅  
  <sub>Benar: peluang empirik $\frac{78}{120} = \frac{13}{20}$, peluang teoretis $\frac{1}{2} = \frac{10}{20}$, selisih $\frac{3}{20}$</sub>

**Pembahasan:** Empirik $= \frac{78}{120} = \frac{13}{20}$. Teoretis $= \frac{1}{2}$. Selisih $= \frac{13}{20} - \frac{10}{20} = \frac{3}{20}$.
**Acuan:** siswa — siswa hal.148

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b04-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: peluang gabungan dua sifat*

Dua puluh kartu identik bernomor 1 sampai 20 dimasukkan ke dalam kotak. Satu kartu diambil secara acak. Peluang nomor kartu yang terambil merupakan kelipatan 3 atau kelipatan 5 adalah ....

- A. $\frac{3}{10}$  
  <sub>Salah: hanya menghitung kelipatan 3</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: menjumlahkan 6 + 4 tanpa mengurangi kartu 15 yang terhitung dua kali</sub>
- **C. $\frac{9}{20}$** ✅  
  <sub>Benar: kelipatan 3: 3, 6, 9, 12, 15, 18 (6 kartu); kelipatan 5: 5, 10, 15, 20 (4 kartu); 15 terhitung dua kali sehingga $6 + 4 - 1 = 9$ dan $P = \frac{9}{20}$</sub>
- D. $\frac{2}{5}$  
  <sub>Salah: mengurangi 2 kartu (15 dibuang dari kedua kelompok)</sub>

**Pembahasan:** Kelipatan 3: 6 kartu; kelipatan 5: 4 kartu; irisan {15}. $n(A) = 6 + 4 - 1 = 9$. $P = \frac{9}{20}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b04-a-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: peluang pada dadu tidak setimbang*

Sebuah dadu dibuat tidak setimbang sehingga peluang muncul mata $k$ sebanding dengan $k$, untuk $k = 1, 2, \dots, 6$. Peluang muncul mata dadu genap adalah ....

- A. $\frac{3}{7}$  
  <sub>Salah: menghitung mata ganjil, bukan genap</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: memakai penyebut 36 (jumlah $k$ pada dua dadu) padahal jumlah peluang satu dadu adalah 21</sub>
- **C. $\frac{4}{7}$** ✅  
  <sub>Benar: jumlah peluang 1 sehingga $P(k) = \frac{k}{21}$; mata genap $\frac{2 + 4 + 6}{21} = \frac{12}{21} = \frac{4}{7}$</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: memakai peluang dadu setimbang padahal dadu tidak setimbang</sub>

**Pembahasan:** $P(k) = ck$ dan $c(1+2+\dots+6) = 21c = 1$, jadi $c = \frac{1}{21}$. Genap: $\frac{2+4+6}{21} = \frac{12}{21} = \frac{4}{7}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b04-a-hard-bt01-001
*orisinal | C6 | 4 langkah | jenis: rancang permainan adil*

Dua dadu setimbang bersisi enam dilempar bersama-sama. Pemain A dan pemain B ingin aturan yang adil, yaitu peluang A menang sama dengan peluang B menang, dan tidak ada hasil seri. Aturan yang adil adalah ....

- A. A menang jika jumlah kedua mata dadu 2 sampai 7 (termasuk 2 dan 7), B menang untuk jumlah lainnya  
  <sub>Salah: peluang A menang $\frac{21}{36}$; membagi 11 nilai jumlah menjadi dua kelompok seolah tiap jumlah sama mungkin</sub>
- B. A menang jika jumlah kedua mata dadu 3 sampai 7 (termasuk 3 dan 7), B menang untuk jumlah lainnya  
  <sub>Salah: peluang A menang $\frac{20}{36}$; mengira lima jumlah di bawah tengah mengimbangi lima jumlah di atasnya padahal banyak pasangan tiap jumlah berbeda</sub>
- **C. A menang jika jumlah kedua mata dadu 4 sampai 7 (termasuk 4 dan 7), B menang untuk jumlah lainnya** ✅  
  <sub>Benar: banyak pasangan berjumlah 4, 5, 6, 7 berturut-turut 3, 4, 5, 6 sehingga 18 dari 36 pasangan: peluang A menang $\frac{1}{2}$ dan B juga $\frac{1}{2}$</sub>
- D. A menang jika jumlah kedua mata dadu 2 sampai 6 (termasuk 2 dan 6), B menang untuk jumlah lainnya  
  <sub>Salah: peluang A menang hanya $\frac{15}{36}$ karena jumlah-jumlah kecil jarang muncul</sub>

**Pembahasan:** Banyak pasangan per jumlah: 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1. Rentang 4 sampai 7 berisi $3+4+5+6 = 18$ dari 36 pasangan, jadi peluang A menang $= \frac{1}{2}$.
**Acuan:** siswa — siswa hal.146

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b04-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: rancang permainan adil*

Tiga koin setimbang dilempar bersama-sama. Pemain A menang jika kejadian tertentu terjadi, dan pemain B menang jika tidak. Agar permainan adil, aturan untuk A adalah ....

- **A. A menang jika muncul paling sedikit dua sisi angka** ✅  
  <sub>Benar: dari $2^3 = 8$ hasil, paling sedikit dua angka ada $3 + 1 = 4$ hasil sehingga peluang A $= \frac{1}{2}$</sub>
- B. A menang jika muncul tepat satu sisi angka  
  <sub>Salah: peluang A hanya $\frac{3}{8}$ (3 dari 8 hasil)</sub>
- C. A menang jika muncul paling sedikit satu sisi angka  
  <sub>Salah: peluang A $\frac{7}{8}$ karena hanya GGG yang tidak termasuk</sub>
- D. A menang jika ketiga koin sama atau tepat satu angka  
  <sub>Salah: peluang A $\frac{5}{8}$ (2 + 3 hasil)</sub>

**Pembahasan:** Ruang sampel 8 hasil. Paling sedikit dua angka: tepat dua angka (3 hasil) atau tiga angka (1 hasil) $= 4$ hasil, $P = \frac{4}{8} = \frac{1}{2}$. Aturan lain bernilai $\frac{3}{8}$, $\frac{7}{8}$, $\frac{5}{8}$.
**Acuan:** siswa — siswa hal.146

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b04-a-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: rancang permainan adil*

Tiga puluh kartu identik bernomor 1 sampai 30 dikocok, lalu satu kartu diambil secara acak. Pemain A menang jika nomor kartu memenuhi aturan tertentu dan pemain B menang jika tidak. Aturan untuk A yang membuat permainan adil adalah nomor kartu ....

- A. kelipatan 2 atau kelipatan 7  
  <sub>Salah: $15 + 4 - 2 = 17$ kartu sehingga peluang A $\frac{17}{30}$, lebih dari separuh</sub>
- B. kelipatan 3 atau kelipatan 5  
  <sub>Salah: hanya $10 + 6 - 2 = 14$ kartu sehingga peluang A $\frac{7}{15}$</sub>
- C. kelipatan 4 atau kelipatan 5  
  <sub>Salah: hanya $7 + 6 - 1 = 12$ kartu sehingga peluang A $\frac{2}{5}$</sub>
- **D. kelipatan 3 atau kelipatan 4** ✅  
  <sub>Benar: kelipatan 3 ada 10, kelipatan 4 ada 7, kelipatan 12 (12 dan 24) ada 2 sehingga $10 + 7 - 2 = 15$ kartu dan peluang $\frac{15}{30} = \frac{1}{2}$</sub>

**Pembahasan:** Adil berarti peluang A menang $\frac{1}{2}$, yaitu 15 kartu. Kelipatan 3 atau 4: $10 + 7 - 2 = 15$. Aturan lain menghasilkan 14, 12, dan 17 kartu.
**Acuan:** siswa — siswa hal.146

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b04-a-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim peluang*

Rani mengatakan bahwa pada pelemparan dua dadu setimbang, jumlah mata 6 dan jumlah mata 7 sama mungkin karena keduanya sama-sama bisa dibentuk dari tiga kombinasi angka. Pernyataan yang tepat untuk mengevaluasi klaim Rani adalah ....

- A. Klaim keliru: jumlah 6 dan jumlah 7 sama-sama paling mungkin dengan peluang $\frac{1}{6}$  
  <sub>Salah: peluang jumlah 6 sebenarnya $\frac{5}{36}$, bukan $\frac{1}{6}$</sub>
- **B. Klaim keliru: jika urutan dadu diperhatikan, jumlah 6 muncul pada 5 pasangan dan jumlah 7 pada 6 pasangan dari 36 pasangan** ✅  
  <sub>Benar: pasangan berurutan jumlah 6: (1,5), (2,4), (3,3), (4,2), (5,1) = 5; jumlah 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6; peluang $\frac{5}{36} < \frac{6}{36}$</sub>
- C. Klaim keliru: jumlah 6 muncul pada 6 pasangan dan jumlah 7 pada 5 pasangan dari 36 pasangan  
  <sub>Salah: banyak pasangan kedua jumlah tertukar</sub>
- D. Klaim benar: kedua jumlah muncul pada 3 pasangan tak berurutan sehingga peluangnya sama  
  <sub>Salah: menghitung pasangan tak berurutan padahal dua dadu berbeda sehingga (1,5) dan (5,1) hasil berlainan (3,3 satu-satunya yang kembar)</sub>

**Pembahasan:** Dua dadu dibedakan, ruang sampel 36 pasangan berurutan. Jumlah 6: 5 pasangan; jumlah 7: 6 pasangan. Jadi jumlah 7 lebih mungkin dan klaim Rani keliru.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b04-a-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan penalaran*

Aldo menghitung peluang kedua dari dua koin setimbang muncul angka. Ia menulis: "Hasil yang mungkin adalah 0 angka, 1 angka, atau 2 angka, jadi ada 3 hasil dan peluang 2 angka adalah $\frac{1}{3}$." Penilaian yang tepat terhadap penalaran Aldo adalah ....

- A. Keliru: ruang sampel berisi 4 hasil tetapi peluang 2 angka adalah $\frac{1}{2}$ karena tiap koin berpeluang angka $\frac{1}{2}$  
  <sub>Salah: menyamakan peluang kedua koin dengan peluang satu koin tanpa mengalikan</sub>
- B. Keliru: ruang sampel yang benar berisi 8 hasil sehingga peluang 2 angka adalah $\frac{1}{8}$  
  <sub>Salah: memakai $2^3$ seolah tiga koin</sub>
- **C. Keliru: "1 angka" dapat terjadi dengan dua cara (AG dan GA), jadi ruang sampel yang sama mungkin berisi 4 hasil dan peluang 2 angka adalah $\frac{1}{4}$** ✅  
  <sub>Benar: ruang sampel sama mungkin $\{AA, AG, GA, GG\}$ dengan 4 hasil; 2 angka hanya AA sehingga $\frac{1}{4}$</sub>
- D. Benar: ketiga hasil sudah terdaftar sehingga peluang 2 angka tetap $\frac{1}{3}$  
  <sub>Salah: menganggap tiga hasil sama mungkin padahal 1 angka punya dua susunan</sub>

**Pembahasan:** Dua koin dibedakan: AA, AG, GA, GG (4 hasil sama mungkin). Dua angka = AA saja, $P = \frac{1}{4}$. Kesalahan Aldo: menganggap hasil 0, 1, 2 angka sama mungkin.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b04-a-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim peluang*

Sebuah koin dilempar 20 kali dan sisi angka muncul 15 kali. Dina menyimpulkan bahwa koin itu pasti tidak setimbang. Pernyataan yang paling tepat tentang kesimpulan Dina adalah ....

- A. Kesimpulan Dina tepat karena peluang empirik $\frac{3}{4}$ berbeda dari $\frac{1}{2}$  
  <sub>Salah: menganggap sembarang selisih dari $\frac{1}{2}$ pada percobaan sedikit sudah pasti</sub>
- **B. Peluang empirik angka $\frac{3}{4}$, tetapi 20 lemparan terlalu sedikit untuk memastikan koin tidak setimbang** ✅  
  <sub>Benar: peluang empirik $\frac{15}{20} = \frac{3}{4}$; hasil percobaan sedikit dapat menyimpang dari $\frac{1}{2}$ pada koin setimbang, sehingga belum cukup untuk kepastian</sub>
- C. Peluang teoretis muncul angka pada koin itu sekarang $\frac{3}{4}$ sehingga koin pasti tidak setimbang  
  <sub>Salah: mencampuradukkan peluang empirik dengan peluang teoretis</sub>
- D. Pada lemparan berikutnya sisi gambar pasti muncul agar hasilnya kembali seimbang  
  <sub>Salah: menganggap koin 'mengimbangi' hasil sebelumnya; tiap lemparan tidak terpengaruh lemparan sebelumnya</sub>

**Pembahasan:** Peluang empirik $= \frac{15}{20} = \frac{3}{4}$. Untuk koin setimbang, 15 angka dari 20 lemparan masih mungkin terjadi. Kesimpulan 'pasti' tidak beralasan; peluang empirik mendekati peluang teoretis jika percobaan diperbanyak.
**Acuan:** siswa — siswa hal.148

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b04-a-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: syarat parameter peluang*

Sebuah kotak berisi $n$ bola merah dan 4 bola biru yang identik selain warnanya, dengan $n$ bilangan bulat positif. Dua bola diambil sekaligus secara acak. Nilai $n$ terkecil agar peluang kedua bola merah lebih dari $\frac{1}{2}$ adalah ....

- **A. 11** ✅  
  <sub>Benar: $P = \frac{n(n-1)}{(n+4)(n+3)}$; untuk $n = 10$ nilainya $\frac{90}{182} < \frac{1}{2}$ dan untuk $n = 11$ nilainya $\frac{110}{210} = \frac{11}{21} > \frac{1}{2}$</sub>
- B. 10  
  <sub>Salah: peluangnya $\frac{45}{91}$, hampir $\frac{1}{2}$ tetapi masih kurang dari $\frac{1}{2}$</sub>
- C. 12  
  <sub>Salah: memenuhi syarat tetapi bukan nilai $n$ terkecil</sub>
- D. 7  
  <sub>Salah: peluangnya $\frac{21}{55}$, masih jauh di bawah $\frac{1}{2}$</sub>

**Pembahasan:** $P(n) = \frac{C(n,2)}{C(n+4,2)} = \frac{n(n-1)}{(n+4)(n+3)}$. $P(10) = \frac{90}{182} \approx 0{,}495$, $P(11) = \frac{110}{210} \approx 0{,}524$. Nilai terkecil yang memenuhi $n = 11$.
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b04-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: bandingkan dua skema pengambilan*

Sebuah kotak berisi 4 bola merah dan 6 bola biru yang identik selain warnanya. Skema I: dua bola diambil satu per satu secara acak dengan pengembalian. Skema II: dua bola diambil satu per satu secara acak tanpa pengembalian. Pernyataan yang benar tentang peluang kedua bola berwarna merah adalah ....

- A. Kedua skema sama besar karena komposisi kotak sama  
  <sub>Salah: mengabaikan perubahan komposisi kotak setelah pengambilan pertama</sub>
- B. Skema I lebih besar daripada Skema II, dengan selisih $\frac{1}{25}$  
  <sub>Salah: menghitung Skema II sebagai $\frac{4}{10} \times \frac{3}{10}$ (penyebut kedua tidak dikurangi)</sub>
- C. Skema II lebih besar daripada Skema I, dengan selisih $\frac{2}{75}$  
  <sub>Salah: mengira bola berkurang membuat bola merah lebih mudah terambil, padahal bola merah ikut berkurang</sub>
- **D. Skema I lebih besar daripada Skema II, dengan selisih $\frac{2}{75}$** ✅  
  <sub>Benar: Skema I: $\frac{4}{10} \times \frac{4}{10} = \frac{4}{25}$; Skema II: $\frac{4}{10} \times \frac{3}{9} = \frac{2}{15}$; selisih $\frac{12}{75} - \frac{10}{75} = \frac{2}{75}$</sub>

**Pembahasan:** Dengan pengembalian: $\left(\frac{4}{10}\right)^2 = \frac{4}{25} = \frac{12}{75}$. Tanpa pengembalian: $\frac{4}{10}\cdot\frac{3}{9} = \frac{2}{15} = \frac{10}{75}$. Selisih $\frac{2}{75}$.
**Acuan:** siswa — siswa hal.151

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b04-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: bandingkan dua skema pengambilan*

Kotak A berisi 3 bola merah dan 5 bola putih. Kotak B berisi 4 bola merah dan 7 bola putih. Bola-bola identik selain warnanya. Satu bola akan diambil secara acak dari salah satu kotak, dan kamu ingin peluang terambil bola merah yang lebih besar. Pilihan yang tepat beserta selisih peluang kedua kotak adalah ....

- A. Kotak B, selisih $\frac{1}{88}$  
  <sub>Salah: memilih kotak yang bola merahnya lebih banyak tanpa memperhitungkan jumlah seluruh bola</sub>
- B. Kedua kotak sama karena keduanya memuat lebih banyak bola putih daripada merah  
  <sub>Salah: membandingkan secara kualitatif saja</sub>
- C. Kotak A, selisih $\frac{1}{35}$  
  <sub>Salah: membandingkan rasio merah terhadap putih ($\frac{3}{5}$ dan $\frac{4}{7}$), bukan terhadap seluruh bola</sub>
- **D. Kotak A, selisih $\frac{1}{88}$** ✅  
  <sub>Benar: $P_A = \frac{3}{8} = \frac{33}{88}$ dan $P_B = \frac{4}{11} = \frac{32}{88}$ sehingga Kotak A lebih besar dengan selisih $\frac{1}{88}$</sub>

**Pembahasan:** $P_A = \frac{3}{8} = 0{,}375$, $P_B = \frac{4}{11} \approx 0{,}364$. Dengan penyebut 88: $\frac{33}{88}$ dan $\frac{32}{88}$. Kotak A, selisih $\frac{1}{88}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b04-a-hard-bt01-010
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan penalaran*

Rina menghitung peluang jumlah mata dua dadu setimbang sama dengan 9. Ia menulis: "Pasangan yang berjumlah 9 hanya (3,6) dan (4,5), jadi peluangnya $\frac{2}{36} = \frac{1}{18}$." Peluang yang benar adalah ....

- A. $\frac{5}{36}$  
  <sub>Salah: mengambil banyak pasangan jumlah 8, bukan jumlah 9</sub>
- **B. $\frac{1}{9}$** ✅  
  <sub>Benar: kedua dadu dibedakan sehingga pasangan berjumlah 9 adalah (3,6), (6,3), (4,5), (5,4) = 4 pasangan: $\frac{4}{36} = \frac{1}{9}$</sub>
- C. $\frac{1}{18}$  
  <sub>Salah: hasil Rina sendiri: pasangan (6,3) dan (5,4) tidak dihitung</sub>
- D. $\frac{1}{12}$  
  <sub>Salah: hanya menambah satu pasangan terlewat (3 pasangan)</sub>

**Pembahasan:** Dua dadu berbeda, jadi (3,6) dan (6,3) berlainan, demikian juga (4,5) dan (5,4). Ada 4 pasangan dari 36, $P = \frac{1}{9}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b04-a-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan penalaran*

Dedi menghitung peluang muncul paling banyak satu sisi angka pada pelemparan empat koin setimbang. Ia menulis: "Satu angka muncul pada 4 dari 16 hasil, jadi peluangnya $\frac{1}{4}$." Peluang yang benar adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: hasil Dedi: kasus tanpa angka (GGGG) terlewat</sub>
- B. $\frac{3}{8}$  
  <sub>Salah: menghitung tepat dua angka</sub>
- **C. $\frac{5}{16}$** ✅  
  <sub>Benar: paling banyak satu angka berarti 0 angka (1 hasil) atau 1 angka (4 hasil): $\frac{1 + 4}{16} = \frac{5}{16}$</sub>
- D. $\frac{11}{16}$  
  <sub>Salah: menghitung paling sedikit dua angka, kebalikan dari yang ditanyakan</sub>

**Pembahasan:** 'Paling banyak satu' mencakup 0 angka (GGGG) dan 1 angka (4 susunan). Total 5 dari $2^4 = 16$, $P = \frac{5}{16}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b04-a-hard-bt01-012
*orisinal | C6 | 4 langkah | jenis: rancang komposisi isi kotak*

Sebuah kotak berisi 5 bola merah dan 7 bola biru yang identik selain warnanya. Agar peluang terambil bola merah pada satu kali pengambilan acak lebih dari $\frac{2}{3}$, ke dalam kotak ditambahkan sejumlah bola merah. Banyak bola merah tambahan paling sedikit adalah ....

- **A. 10** ✅  
  <sub>Benar: $\frac{5 + x}{12 + x} > \frac{2}{3}$ memberi $15 + 3x > 24 + 2x$ sehingga $x > 9$ dan bilangan bulat terkecil $x = 10$</sub>
- B. 7  
  <sub>Salah: peluangnya $\frac{12}{19}$, masih kurang dari $\frac{2}{3}$</sub>
- C. 11  
  <sub>Salah: memenuhi syarat tetapi bukan yang paling sedikit</sub>
- D. 9  
  <sub>Salah: dengan 9 bola tambahan peluangnya tepat $\frac{14}{21} = \frac{2}{3}$, belum lebih dari $\frac{2}{3}$</sub>

**Pembahasan:** $\frac{5 + x}{12 + x} > \frac{2}{3} \Rightarrow 15 + 3x > 24 + 2x \Rightarrow x > 9$. Nilai bulat terkecil 10; periksa $\frac{15}{22} > \frac{2}{3}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b04-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Seorang siswa mengklaim bahwa untuk dua kejadian sebarang $A$ dan $B$ berlaku $P(A \text{ atau } B) = P(A) + P(B)$. Pada pelemparan satu dadu setimbang bersisi enam, pasangan kejadian yang merupakan contoh penyangkal klaim itu adalah ....

- A. $A$: muncul mata 1; $B$: muncul mata lebih dari 4  
  <sub>Salah: kedua kejadian saling lepas: $\frac{1}{6} + \frac{2}{6} = \frac{3}{6}$ sama dengan peluang gabungan</sub>
- **B. $A$: muncul mata genap; $B$: muncul mata kelipatan 3** ✅  
  <sub>Benar: $P(A) = \frac{3}{6}$, $P(B) = \frac{2}{6}$, jumlahnya $\frac{5}{6}$, tetapi $A \cup B = \{2,3,4,6\}$ sehingga $P(A \text{ atau } B) = \frac{4}{6}$ (mata 6 terhitung dua kali)</sub>
- C. $A$: muncul mata genap; $B$: muncul mata ganjil  
  <sub>Salah: kedua kejadian saling lepas: $\frac{3}{6} + \frac{3}{6} = 1 = P(A \text{ atau } B)$ sehingga klaim berlaku</sub>
- D. $A$: muncul mata 1 atau 2; $B$: muncul mata 5 atau 6  
  <sub>Salah: kedua kejadian saling lepas: $\frac{2}{6} + \frac{2}{6} = \frac{4}{6}$ sama dengan peluang gabungan</sub>

**Pembahasan:** Contoh penyangkal harus punya irisan tidak kosong. Genap $\{2,4,6\}$ dan kelipatan 3 $\{3,6\}$ beririsan di $\{6\}$: jumlah $\frac{5}{6}$ tetapi gabungan $\frac{4}{6}$. Tiga pasangan lain saling lepas sehingga klaim kebetulan berlaku.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b04-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim peluang*

Tono mengira bahwa pada pelemparan dua dadu setimbang, kesebelas jumlah mata (2 sampai 12) sama mungkin sehingga tiap jumlah berpeluang $\frac{1}{11}$. Banyak nilai jumlah mata yang sebenarnya berpeluang lebih besar daripada $\frac{1}{11}$ adalah ....

- A. 11  
  <sub>Salah: mengikuti klaim Tono bahwa semua jumlah sama mungkin</sub>
- B. 9  
  <sub>Salah: memakai syarat $k \geq 2$ (jumlah 3 sampai 11), padahal $\frac{2}{36} < \frac{1}{11}$</sub>
- **C. 5** ✅  
  <sub>Benar: peluang jumlah $s$ adalah $\frac{k}{36}$ dengan $k$ banyak pasangan; $\frac{k}{36} > \frac{1}{11}$ berarti $k > 3{,}27$ sehingga $k \geq 4$, yaitu jumlah 5, 6, 7, 8, 9</sub>
- D. 7  
  <sub>Salah: memakai syarat $k \geq 3$ (jumlah 4 sampai 10), padahal $\frac{3}{36} = \frac{1}{12} < \frac{1}{11}$</sub>

**Pembahasan:** Banyak pasangan per jumlah 2..12: 1,2,3,4,5,6,5,4,3,2,1. Syarat $\frac{k}{36} > \frac{1}{11}$ memberi $k \geq 4$: jumlah 5, 6, 7, 8, 9, jadi 5 nilai.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b04-a-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: dadu tidak setimbang*

Sebuah dadu bersisi enam dibuat tidak setimbang: peluang muncul setiap mata genap dua kali lipat peluang muncul setiap mata ganjil. Peluang muncul mata dadu bilangan prima adalah ....

- **A. $\frac{4}{9}$** ✅  
  <sub>Benar: misalkan peluang mata ganjil $p$: $3p + 3(2p) = 1$ sehingga $p = \frac{1}{9}$; prima 2, 3, 5 berpeluang $\frac{2}{9} + \frac{1}{9} + \frac{1}{9} = \frac{4}{9}$</sub>
- B. $\frac{2}{3}$  
  <sub>Salah: memakai peluang ganjil $\frac{1}{6}$ dan genap $\frac{2}{6}$ tanpa menormalkan jumlah menjadi 1</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: memakai peluang dadu setimbang ($\frac{3}{6}$)</sub>
- D. $\frac{2}{9}$  
  <sub>Salah: hanya menghitung mata 2 (satu-satunya prima genap)</sub>

**Pembahasan:** Misal peluang tiap mata ganjil $p$, genap $2p$. $3p + 6p = 1$, $p = \frac{1}{9}$. Prima: 2 ($\frac{2}{9}$), 3 ($\frac{1}{9}$), 5 ($\frac{1}{9}$). Jumlah $\frac{4}{9}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b04-a-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: syarat parameter peluang*

Sebuah kantong berisi $m$ bola bernomor ganjil dan 3 bola bernomor genap, dengan $m$ bilangan bulat dan $m \geq 2$. Dua bola diambil sekaligus secara acak. Nilai $m$ agar peluang jumlah kedua nomor bola genap tepat $\frac{1}{2}$ adalah ....

- A. 7  
  <sub>Salah: peluangnya $\frac{24}{45}$, bukan $\frac{1}{2}$</sub>
- B. 1  
  <sub>Salah: akar lain persamaan, tetapi melanggar syarat $m \geq 2$</sub>
- C. 3  
  <sub>Salah: peluangnya $\frac{6}{15}$, bukan $\frac{1}{2}$</sub>
- **D. 6** ✅  
  <sub>Benar: jumlah genap bila kedua ganjil atau kedua genap: $\frac{C(m,2) + C(3,2)}{C(m+3,2)} = \frac{1}{2}$ memberi $m^2 - 7m + 6 = 0$ sehingga $m = 1$ atau $m = 6$; syarat $m \geq 2$ menyisakan $m = 6$</sub>

**Pembahasan:** Jumlah genap: ganjil+ganjil atau genap+genap. $\frac{\frac{m(m-1)}{2} + 3}{\frac{(m+3)(m+2)}{2}} = \frac{1}{2}$ menghasilkan $m^2 - 7m + 6 = 0$, jadi $m = 1$ atau $6$. Karena $m \geq 2$, $m = 6$ (cek: $\frac{15 + 3}{36} = \frac{1}{2}$).
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b04-a-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan penalaran*

Satu kartu diambil secara acak dari seperangkat kartu bridge standar 52 kartu (13 hati, 4 As, dan 1 As hati). Andi menghitung peluang kartu terambil bukan hati dan bukan As: "$1 - \frac{13}{52} - \frac{4}{52} = \frac{35}{52}$." Peluang yang benar adalah ....

- A. $\frac{12}{13}$  
  <sub>Salah: hanya mengeluarkan kartu As, hati diabaikan</sub>
- B. $\frac{35}{52}$  
  <sub>Salah: hasil Andi: As hati dikurangkan dua kali</sub>
- C. $\frac{3}{4}$  
  <sub>Salah: hanya mengeluarkan kartu hati, As diabaikan</sub>
- **D. $\frac{9}{13}$** ✅  
  <sub>Benar: kartu hati atau As ada $13 + 4 - 1 = 16$ (As hati terhitung dua kali), sehingga bukan hati dan bukan As ada $52 - 16 = 36$ kartu: $\frac{36}{52} = \frac{9}{13}$</sub>

**Pembahasan:** $P(\text{hati atau As}) = \frac{13 + 4 - 1}{52} = \frac{16}{52}$. Komplemennya $\frac{36}{52} = \frac{9}{13}$. Andi mengurangkan As hati dua kali.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b04-a-hard-bt01-018
*orisinal | C5 | 5 langkah | jenis: bandingkan dua skema pengambilan*

Sebuah kotak berisi 4 bola merah dan 6 bola biru yang identik selain warnanya. Tiga bola diambil secara acak dengan tiga cara: (i) sekaligus tiga bola, (ii) satu per satu tanpa pengembalian, (iii) satu per satu dengan pengembalian. Pernyataan yang benar tentang peluang ketiga bola berwarna merah adalah ....

- **A. Cara (i) dan (ii) sama-sama $\frac{1}{30}$, sedangkan cara (iii) $\frac{8}{125}$ sehingga lebih besar** ✅  
  <sub>Benar: (i) $\frac{C(4,3)}{C(10,3)} = \frac{4}{120} = \frac{1}{30}$; (ii) $\frac{4}{10}\cdot\frac{3}{9}\cdot\frac{2}{8} = \frac{1}{30}$; (iii) $\left(\frac{4}{10}\right)^3 = \frac{8}{125} > \frac{1}{30}$</sub>
- B. Ketiga cara sama-sama $\frac{8}{125}$ karena komposisi awal kotak sama  
  <sub>Salah: menganggap pengambilan tanpa pengembalian tidak mengubah komposisi kotak</sub>
- C. Cara (iii) $\frac{8}{125}$ lebih kecil daripada cara (ii) $\frac{1}{30}$ karena bola yang dikembalikan tidak boleh terambil lagi  
  <sub>Salah: keliru membandingkan: $\frac{8}{125} > \frac{1}{30}$ karena peluang merah tidak menurun pada pengambilan dengan pengembalian</sub>
- D. Cara (i) $\frac{1}{30}$ dan cara (ii) $\frac{1}{5}$ karena cara (ii) memperhatikan urutan sehingga enam kali lebih besar  
  <sub>Salah: mengalikan dengan $3!$ padahal pembilang dan penyebut sama-sama memperhatikan urutan</sub>

**Pembahasan:** Sekaligus: $\frac{4}{120} = \frac{1}{30}$. Berurutan tanpa pengembalian: $\frac{24}{720} = \frac{1}{30}$ (sama). Dengan pengembalian: $\frac{64}{1000} = \frac{8}{125}$, lebih besar karena merah tidak berkurang.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b04-a-hard-bt01-019
*orisinal | C5 | 3 langkah | jenis: analisis permainan adil*

Dua dadu setimbang dilempar bersama-sama dan kedua matanya dikalikan. Pemain A menang jika hasil kali ganjil, pemain B menang jika hasil kali genap. Dika berpendapat permainan itu adil karena tiap dadu memuat tiga mata ganjil dan tiga mata genap. Pernyataan yang benar adalah ....

- A. Adil: peluang A menang $\frac{1}{2}$ dan peluang B menang $\frac{1}{2}$  
  <sub>Salah: hanya melihat satu dadu, padahal hasil kali ganjil menuntut kedua dadu ganjil</sub>
- B. Tidak adil: peluang A menang $\frac{3}{4}$ dan peluang B menang $\frac{1}{4}$  
  <sub>Salah: menukar peluang ganjil dan genap</sub>
- **C. Tidak adil: peluang A menang $\frac{1}{4}$ dan peluang B menang $\frac{3}{4}$** ✅  
  <sub>Benar: hasil kali ganjil hanya jika kedua mata ganjil: $3 \times 3 = 9$ dari 36, $P(A) = \frac{1}{4}$; $P(B) = 1 - \frac{1}{4} = \frac{3}{4}$</sub>
- D. Tidak adil: peluang A menang $\frac{1}{3}$ dan peluang B menang $\frac{2}{3}$  
  <sub>Salah: menghitung 12 dari 36 hasil kali ganjil, padahal hanya 9</sub>

**Pembahasan:** Ganjil $\times$ ganjil = ganjil, selain itu genap. Banyak pasangan keduanya ganjil $= 3 \times 3 = 9$. $P(A) = \frac{9}{36} = \frac{1}{4}$, $P(B) = \frac{3}{4}$.
**Acuan:** siswa — siswa hal.146

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b04-a-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: peluang gabungan dua sifat*

Dua dadu setimbang dilempar bersama-sama. Peluang jumlah kedua mata paling sedikit 9 atau kedua mata berselisih tepat 1 adalah ....

- A. $\frac{5}{18}$  
  <sub>Salah: hanya menghitung satu sifat saja (10 dari 36 pasangan)</sub>
- **B. $\frac{4}{9}$** ✅  
  <sub>Benar: jumlah paling sedikit 9 ada 10 pasangan; selisih 1 ada 10 pasangan; keduanya: (4,5), (5,4), (5,6), (6,5) = 4; $10 + 10 - 4 = 16$ dan $\frac{16}{36} = \frac{4}{9}$</sub>
- C. $\frac{5}{9}$  
  <sub>Salah: menjumlahkan $10 + 10 = 20$ tanpa mengurangi irisan 4 pasangan</sub>
- D. $\frac{1}{9}$  
  <sub>Salah: hanya menghitung 4 pasangan yang memenuhi kedua sifat sekaligus</sub>

**Pembahasan:** Himpunan jumlah $\geq 9$: 4+3+2+1 = 10 pasangan. Selisih 1: 10 pasangan. Irisan: (4,5), (5,4), (5,6), (6,5). Gabungan $10 + 10 - 4 = 16$, $P = \frac{16}{36} = \frac{4}{9}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
