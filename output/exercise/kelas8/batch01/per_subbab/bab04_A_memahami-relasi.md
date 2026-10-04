# Lembar koreksi — kelas8 SMP8-B4 subbab A: Memahami Relasi

45 soal | easy 15, medium 15, hard 15 | variasi 15, orisinal 30

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas8-b04-a-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: menyusun himpunan pasangan berurutan*

Diketahui himpunan $C = \{6, 8\}$ dan himpunan $D = \{7, 9, 10\}$. Relasi dari himpunan $C$ ke $D$ adalah "kurang dari". Himpunan pasangan berurutan dari relasi tersebut adalah ....

- A. $\{(7, 6), (9, 6), (10, 6), (9, 8), (10, 8)\}$  
  <sub>Salah: urutan pasangan terbalik (dari $D$ ke $C$)</sub>
- **B. $\{(6, 7), (6, 9), (6, 10), (8, 9), (8, 10)\}$** ✅  
  <sub>Benar: pasangan $(c, d)$ yang memenuhi $c < d$: $6<7$, $6<9$, $6<10$, $8<9$, $8<10$</sub>
- C. $\{(6, 7), (6, 9), (6, 10), (8, 9)\}$  
  <sub>Salah: lupa memasukkan pasangan terakhir $(8, 10)$</sub>
- D. $\{(6, 7), (8, 9)\}$  
  <sub>Salah: hanya memasangkan bilangan yang berurutan dan melewatkan pasangan lain yang juga memenuhi</sub>

**Pembahasan:** Periksa semua pasangan: $6<7$, $6<9$, $6<10$, $8<9$, $8<10$ benar; $8<7$ salah. Jadi relasinya $\{(6, 7), (6, 9), (6, 10), (8, 9), (8, 10)\}$.
**Acuan:** pretest — kelas8-b04-p0179-soal-laihan-4-1-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas8-b04-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menyusun himpunan pasangan berurutan*

Apabila relasi himpunan $E$ ke $F$ merupakan "akar dari" (anggota $E$ adalah akar kuadrat anggota $F$) dengan $E = \{7, 8, 9, 10\}$ dan $F = \{49, 64, 72, 81, 90, 100\}$, maka himpunan pasangan berurutan relasi tersebut adalah ....

- **A. $\{(7, 49), (8, 64), (9, 81), (10, 100)\}$** ✅  
  <sub>Benar: $7^2=49$, $8^2=64$, $9^2=81$, $10^2=100$ semuanya ada di $F$</sub>
- B. $\{(49, 7), (64, 8), (81, 9), (100, 10)\}$  
  <sub>Salah: urutan pasangan terbalik ($F$ ke $E$)</sub>
- C. $\{(7, 49), (8, 72), (9, 81), (10, 100)\}$  
  <sub>Salah: memasangkan 8 dengan 72 ($8 \times 9$) bukan 64 ($8 \times 8$)</sub>
- D. $\{(7, 49), (8, 64), (9, 90), (10, 100)\}$  
  <sub>Salah: memasangkan 9 dengan 90 ($9 \times 10$) bukan 81 ($9 \times 9$)</sub>

**Pembahasan:** Kuadratkan tiap anggota $E$: $49$, $64$, $81$, $100$, semuanya ada di $F$. Jadi $\{(7, 49), (8, 64), (9, 81), (10, 100)\}$.
**Acuan:** pretest — kelas8-b04-p0179-soal-laihan-4-1-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas8-b04-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: menentukan range relasi*

Diketahui dua himpunan bilangan, yaitu $A = \{\text{bilangan bulat antara } 4 \text{ dan } 9\}$ dan $B = \{\text{delapan bilangan cacah pertama}\}$. Relasi dari himpunan $A$ ke himpunan $B$ adalah "satu lebihnya dari". Daerah hasil (range) relasi tersebut adalah ....

- A. $\{0, 1, 2, 3, 4, 5, 6, 7\}$  
  <sub>Salah: menulis seluruh kodomain (himpunan $B$) sebagai range</sub>
- **B. $\{4, 5, 6, 7\}$** ✅  
  <sub>Benar: $A=\{5,6,7,8\}$, $B=\{0,1,\dots,7\}$; pasangannya $(5,4),(6,5),(7,6),(8,7)$ sehingga range = $\{4,5,6,7\}$</sub>
- C. $\{5, 6, 7, 8\}$  
  <sub>Salah: menulis domain (himpunan $A$) sebagai range</sub>
- D. $\{6, 7\}$  
  <sub>Salah: membalik relasi menjadi 'satu kurangnya dari' sehingga hanya 6 dan 7 yang ada di $B$</sub>

**Pembahasan:** $A=\{5, 6, 7, 8\}$ dan $B=\{0, 1, 2, 3, 4, 5, 6, 7\}$. Anggota $A$ adalah satu lebihnya dari anggota $B$: $(5, 4)$, $(6, 5)$, $(7, 6)$, $(8, 7)$. Range = $\{4, 5, 6, 7\}$.
**Acuan:** siswa — siswa hal.175 Ayo Berkomunikasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas8-b04-a-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: menyusun himpunan pasangan berurutan*

Diketahui $T = \{5, 6, 7\}$ dan $U = \{10, 14, 15, 30\}$. Himpunan pasangan berurutan dari himpunan $T$ ke himpunan $U$ yang relasinya "faktor dari" adalah ....

- A. $\{(10, 5), (15, 5), (30, 5), (30, 6), (14, 7)\}$  
  <sub>Salah: urutan pasangan terbalik sehingga menjadi 'kelipatan dari'</sub>
- B. $\{(5, 10), (5, 15), (6, 30), (7, 14)\}$  
  <sub>Salah: lupa pasangan $(5, 30)$ karena 30 tidak diperiksa untuk faktor 5</sub>
- **C. $\{(5, 10), (5, 15), (5, 30), (6, 30), (7, 14)\}$** ✅  
  <sub>Benar: 5 faktor dari 10, 15, 30; 6 faktor dari 30; 7 faktor dari 14</sub>
- D. $\{(5, 10), (5, 15), (5, 30), (6, 30), (7, 14), (7, 15)\}$  
  <sub>Salah: menyertakan pasangan $(7, 15)$ padahal 7 bukan faktor dari 15</sub>

**Pembahasan:** Periksa tiap anggota $T$: $5$ membagi $10$, $15$, $30$; $6$ membagi $30$; $7$ membagi $14$. Jadi $\{(5, 10), (5, 15), (5, 30), (6, 30), (7, 14)\}$.
**Acuan:** siswa — siswa hal.180 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas8-b04-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: menyusun himpunan pasangan berurutan*

Diketahui himpunan $A = \{15, 21, 24, 27, 30\}$ dan himpunan $B = \{5, 7, 8, 9\}$. Relasi dari himpunan $A$ ke himpunan $B$ adalah "tiga kali dari". Himpunan pasangan berurutan dari relasi tersebut adalah ....

- A. $\{(15, 5), (21, 7), (24, 8), (27, 9), (30, 10)\}$  
  <sub>Salah: menyertakan pasangan $(30, 10)$ padahal 10 bukan anggota $B$</sub>
- B. $\{(15, 5), (21, 7), (24, 8)\}$  
  <sub>Salah: lupa pasangan terakhir $(27, 9)$</sub>
- C. $\{(5, 15), (7, 21), (8, 24), (9, 27)\}$  
  <sub>Salah: urutan pasangan terbalik ($B$ ke $A$)</sub>
- **D. $\{(15, 5), (21, 7), (24, 8), (27, 9)\}$** ✅  
  <sub>Benar: $15=3\times5$, $21=3\times7$, $24=3\times8$, $27=3\times9$, sedangkan 30 memerlukan 10 yang tidak ada di $B$</sub>

**Pembahasan:** Cari anggota $A$ yang tiga kali anggota $B$: $15 = 3 \times 5$, $21 = 3 \times 7$, $24 = 3 \times 8$, $27 = 3 \times 9$. Anggota $30$ tidak punya pasangan karena $10 \notin B$. Jadi $\{(15, 5), (21, 7), (24, 8), (27, 9)\}$.
**Acuan:** siswa — siswa hal.178 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas8-b04-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: mengenali anggota relasi*

Diketahui $R = \{16, 18, 21, 25\}$ dan $S = \{15, 17, 20, 23\}$. Relasi dari himpunan $R$ ke himpunan $S$ adalah "satu lebihnya dari". Pasangan berurutan berikut yang merupakan anggota relasi tersebut adalah ....

- A. $(17, 18)$  
  <sub>Salah: urutan terbalik: 17 bukan anggota $R$ sehingga tidak bisa menjadi anggota pertama pasangan</sub>
- **B. $(18, 17)$** ✅  
  <sub>Benar: 18 ada di $R$, 17 ada di $S$, dan $18 = 17 + 1$</sub>
- C. $(25, 23)$  
  <sub>Salah: selisihnya dua, bukan satu</sub>
- D. $(16, 17)$  
  <sub>Salah: memakai 'satu kurangnya dari' ($16 + 1 = 17$), bukan 'satu lebihnya dari'</sub>

**Pembahasan:** Anggota pertama harus dari $R$, anggota kedua dari $S$, dan anggota pertama = anggota kedua + 1. Pasangan yang memenuhi: $(16, 15)$, $(18, 17)$, $(21, 20)$. Di antara pilihan, hanya $(18, 17)$.
**Acuan:** siswa — siswa hal.180 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas8-b04-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: domain, kodomain, dan range*

Diketahui himpunan $A = \{7, 9, 12\}$ dan himpunan $B = \{6, 8, 10, 13\}$. Relasi dari himpunan $A$ ke himpunan $B$ adalah "lebih dari". Pernyataan yang benar tentang domain, kodomain, dan range relasi tersebut adalah ....

- A. Domain = $\{7, 9, 12\}$, kodomain = $\{6, 8, 10, 13\}$, range = $\{7, 9, 12\}$  
  <sub>Salah: mengambil range dari anggota $A$, bukan dari anggota $B$ yang mendapat pasangan</sub>
- B. Domain = $\{7, 9, 12\}$, kodomain = $\{6, 8, 10, 13\}$, range = $\{6, 8, 10, 13\}$  
  <sub>Salah: mengira range sama dengan kodomain padahal 13 tidak mendapat pasangan</sub>
- **C. Domain = $\{7, 9, 12\}$, kodomain = $\{6, 8, 10, 13\}$, range = $\{6, 8, 10\}$** ✅  
  <sub>Benar: domain = $A$, kodomain = $B$, range = anggota $B$ yang mendapat pasangan: 6, 8, 10 (13 tidak lebih kecil dari anggota $A$ mana pun)</sub>
- D. Domain = $\{6, 8, 10, 13\}$, kodomain = $\{7, 9, 12\}$, range = $\{6, 8, 10\}$  
  <sub>Salah: domain dan kodomain tertukar</sub>

**Pembahasan:** Domain = $A$, kodomain = $B$. Pasangan 'lebih dari': $(7, 6)$, $(9, 6)$, $(9, 8)$, $(12, 6)$, $(12, 8)$, $(12, 10)$. Anggota $B$ yang terpakai: 6, 8, 10, jadi range = $\{6, 8, 10\}$.
**Acuan:** siswa — siswa hal.174 Contoh 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas8-b04-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: banyak anggota range*

Enam siswa memakai sepatu dengan ukuran berbeda. Rani dan Tika memakai sepatu ukuran 35. Udin memakai sepatu ukuran 36. Vino memakai sepatu ukuran 41. Wawan dan Yani sama-sama memakai sepatu ukuran 42. Toko hanya menyediakan sepatu ukuran 35, 36, 37, 38, 41, 42, dan 43. Pada relasi "memakai sepatu ukuran" dari himpunan siswa ke himpunan ukuran sepatu di toko, banyak anggota daerah hasil (range) adalah ....

- A. 6  
  <sub>Salah: menghitung banyak siswa (anggota domain), bukan banyak ukuran berbeda</sub>
- B. 2  
  <sub>Salah: hanya menghitung ukuran yang dipakai satu siswa (36 dan 41)</sub>
- **C. 4** ✅  
  <sub>Benar: ukuran yang dipakai: 35, 36, 41, 42 (ukuran kembar dihitung sekali)</sub>
- D. 7  
  <sub>Salah: menghitung seluruh ukuran di toko (anggota kodomain)</sub>

**Pembahasan:** Ukuran yang benar-benar dipakai: $35$, $36$, $41$, $42$. Ukuran kembar dihitung sekali, jadi range memiliki 4 anggota.
**Acuan:** siswa — siswa hal.181 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas8-b04-a-easy-bt01-009
*variasi (angka) | C2 | 1 langkah | jenis: notasi pembentuk himpunan ke enumerasi*

Himpunan $P = \{x \mid 4 < x < 15,\ \text{dengan } x \text{ merupakan bilangan ganjil}\}$. Jika dinyatakan dengan cara enumerasi, himpunan $P$ adalah ....

- A. $\{4, 6, 8, 10, 12, 14\}$  
  <sub>Salah: memilih bilangan genap, bukan ganjil</sub>
- B. $\{5, 7, 9, 11, 13, 15\}$  
  <sub>Salah: memasukkan batas atas 15 padahal tanda $<$ berarti 15 tidak termasuk</sub>
- C. $\{5, 7, 9, 11\}$  
  <sub>Salah: berhenti sebelum 13 sehingga anggota terakhir terlewat</sub>
- **D. $\{5, 7, 9, 11, 13\}$** ✅  
  <sub>Benar: bilangan ganjil di antara 4 dan 15 (batas tidak ikut): 5, 7, 9, 11, 13</sub>

**Pembahasan:** Bilangan ganjil yang lebih dari $4$ dan kurang dari $15$: $5, 7, 9, 11, 13$. Jadi $P = $ $\{5, 7, 9, 11, 13\}$.
**Acuan:** siswa — siswa hal.165 Contoh 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas8-b04-a-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: relasi kebalikan*

Diketahui $P = \{\text{Pak Tomi}, \text{Bu Rina}\}$ dan $Q = \{\text{Dedi}, \text{Siti}, \text{Rudi}\}$. Relasi dari himpunan $P$ ke himpunan $Q$ adalah "orang tua dari". Hubungan sebaliknya, yaitu relasi dari himpunan $Q$ ke himpunan $P$, adalah ....

- **A. "anak dari"** ✅  
  <sub>Benar: hubungan sebaliknya dari 'orang tua dari' adalah 'anak dari'</sub>
- B. "cucu dari"  
  <sub>Salah: mengira generasi di bawahnya berarti cucu</sub>
- C. "kakak dari"  
  <sub>Salah: mencampur dengan hubungan antarsaudara</sub>
- D. "orang tua dari"  
  <sub>Salah: mengira relasi sebaliknya sama dengan relasi semula</sub>

**Pembahasan:** Jika $P$ orang tua dari $Q$, maka dari $Q$ ke $P$ hubungannya adalah anak dari.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas8-b04-a-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: kardinalitas himpunan*

Diketahui himpunan $A = \{\text{bilangan prima kurang dari } 20\}$. Nilai $n(A)$ adalah ....

- A. 7  
  <sub>Salah: tidak memasukkan 2 sebagai bilangan prima</sub>
- B. 19  
  <sub>Salah: mengambil bilangan prima terbesar, bukan banyaknya anggota</sub>
- C. 9  
  <sub>Salah: menganggap 1 sebagai bilangan prima</sub>
- **D. 8** ✅  
  <sub>Benar: anggota $A$: 2, 3, 5, 7, 11, 13, 17, 19 (8 bilangan)</sub>

**Pembahasan:** $A = \{2, 3, 5, 7, 11, 13, 17, 19\}$, sehingga $n(A) = 8$.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas8-b04-a-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: menentukan aturan relasi dari pasangan*

Relasi dari himpunan $A = \{2, 3, 4\}$ ke himpunan $B = \{5, 6, 7\}$ dinyatakan dengan pasangan berurutan $\{(2, 5), (3, 6), (4, 7)\}$. Aturan relasi tersebut adalah ....

- A. "faktor dari"  
  <sub>Salah: mengira anggota $A$ selalu membagi anggota $B$, padahal 2 tidak membagi 5</sub>
- **B. "tiga kurangnya dari"** ✅  
  <sub>Benar: $2=5-3$, $3=6-3$, $4=7-3$</sub>
- C. "dua kali dari"  
  <sub>Salah: memakai aturan perkalian padahal selisih tetap</sub>
- D. "tiga lebihnya dari"  
  <sub>Salah: membalik arah selisih: anggota $A$ dianggap lebih besar</sub>

**Pembahasan:** Selisih tiap pasangan: $5-2=3$, $6-3=3$, $7-4=3$. Anggota $A$ selalu 3 kurangnya dari anggota $B$.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas8-b04-a-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: enumerasi ke notasi himpunan*

Himpunan $K = \{2, 4, 6, 8, 10\}$ jika dinyatakan dengan notasi pembentuk himpunan adalah ....

- A. $\{x \mid 2 \leq x \leq 12,\ x \text{ bilangan genap}\}$  
  <sub>Salah: batas atas 12 ikut sehingga ada anggota tambahan 12</sub>
- B. $\{x \mid 2 < x < 10,\ x \text{ bilangan genap}\}$  
  <sub>Salah: memakai batas yang membuang anggota 2 dan 10</sub>
- **C. $\{x \mid 0 < x < 12,\ x \text{ bilangan genap}\}$** ✅  
  <sub>Benar: bilangan genap di antara 0 dan 12: 2, 4, 6, 8, 10</sub>
- D. $\{x \mid 0 < x < 12,\ x \text{ bilangan ganjil}\}$  
  <sub>Salah: memakai bilangan ganjil, bukan genap</sub>

**Pembahasan:** Anggota $K$ semuanya genap dan terletak antara $0$ dan $12$, sehingga $K = \{x \mid 0 < x < 12,\ x \text{ bilangan genap}\}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas8-b04-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: himpunan berhingga dan tak berhingga*

Himpunan berikut yang merupakan himpunan tak berhingga adalah ....

- **A. $\{x \mid x > 10,\ x \text{ bilangan asli}\}$** ✅  
  <sub>Benar: bilangan asli lebih dari 10 terus bertambah tanpa batas</sub>
- B. $\{x \mid -5 < x < 5,\ x \text{ bilangan bulat}\}$  
  <sub>Salah: mengira bilangan bulat selalu tak berhingga padahal dibatasi dua sisi</sub>
- C. $\{x \mid x < 20,\ x \text{ bilangan prima}\}$  
  <sub>Salah: mengira himpunan dengan batas atas tetap tak berhingga; padahal anggotanya 2, 3, 5, 7, 11, 13, 17, 19</sub>
- D. $\{\text{huruf vokal alfabet latin}\}$  
  <sub>Salah: mengira himpunan huruf tak berhingga padahal hanya 5 huruf</sub>

**Pembahasan:** Bilangan asli yang lebih dari $10$ ($11, 12, 13, \dots$) tidak pernah habis, sedangkan pilihan lain anggotanya dapat dihitung.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas8-b04-a-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: pasangan berurutan dari himpunan asal ke kawan*

Diketahui himpunan $A = \{1, 2, 3\}$ dan himpunan $B = \{x, y\}$. Pasangan berurutan yang TIDAK mungkin menjadi anggota relasi dari himpunan $A$ ke himpunan $B$ adalah ....

- A. $(2, x)$  
  <sub>Salah: pasangan sah: 2 dari $A$ dan $x$ dari $B$</sub>
- B. $(1, y)$  
  <sub>Salah: pasangan sah: 1 dari $A$ dan $y$ dari $B$</sub>
- C. $(3, y)$  
  <sub>Salah: pasangan sah: 3 dari $A$ dan $y$ dari $B$</sub>
- **D. $(x, 2)$** ✅  
  <sub>Benar: anggota pertama $x$ bukan anggota $A$, sehingga bukan pasangan dari $A$ ke $B$</sub>

**Pembahasan:** Pasangan relasi dari $A$ ke $B$ memiliki anggota pertama dari $A$ dan anggota kedua dari $B$. Pada $(x, 2)$ urutannya terbalik.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas8-b04-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: banyak anggota relasi kelipatan dari*

Diketahui himpunan $P = \{28, 30, 39, 42, 52, 60, 77\}$ dan $Q = \{6, 10, 13, 14\}$. Relasi dari himpunan $P$ ke himpunan $Q$ adalah "kelipatan dari". Banyak anggota himpunan pasangan berurutan relasi tersebut adalah ....

- **A. 9** ✅  
  <sub>Benar: 28: (28,14); 30: (30,6),(30,10); 39: (39,13); 42: (42,6),(42,14); 52: (52,13); 60: (60,6),(60,10); 77 tidak punya pasangan; total 9</sub>
- B. 6  
  <sub>Salah: menghitung banyak anggota $P$ yang punya pasangan, bukan banyak pasangannya</sub>
- C. 28  
  <sub>Salah: menghitung seluruh pasangan $P \times Q$ ($7 \times 4$) tanpa menyaring</sub>
- D. 8  
  <sub>Salah: melewatkan satu pasangan, yaitu $(60, 10)$</sub>

**Pembahasan:** Periksa kelipatan: $28$ kelipatan $14$; $30$ kelipatan $6$ dan $10$; $39$ kelipatan $13$; $42$ kelipatan $6$ dan $14$; $52$ kelipatan $13$; $60$ kelipatan $6$ dan $10$; $77$ bukan kelipatan satu pun. Banyak pasangan $1+2+1+2+1+2 = 9$.
**Acuan:** siswa — siswa hal.179 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas8-b04-a-medium-bt01-002
*variasi (angka) | C4 | 4 langkah | jenis: anggota kawan dengan pasangan terbanyak*

Diketahui himpunan $P = \{20, 24, 33, 40, 44, 48, 55\}$ dan $Q = \{4, 5, 8, 11, 12\}$. Relasi dari himpunan $P$ ke himpunan $Q$ adalah "kelipatan dari". Anggota himpunan $Q$ yang berpasangan dengan paling banyak anggota $P$, beserta banyak pasangannya, adalah ....

- A. $4$ dengan $4$ pasangan  
  <sub>Salah: melewatkan $48$ sebagai kelipatan $4$</sub>
- B. $24$ dengan $3$ pasangan  
  <sub>Salah: menghitung dari sisi $P$ sehingga memilih anggota $P$, padahal diminta anggota $Q$</sub>
- C. $5$ dengan $3$ pasangan  
  <sub>Salah: memilih anggota $Q$ lain yang pasangannya lebih sedikit ($20, 40, 55$)</sub>
- **D. $4$ dengan $5$ pasangan** ✅  
  <sub>Benar: kelipatan 4 di $P$: 20, 24, 40, 44, 48 (5 anggota); anggota $Q$ lain paling banyak 3 pasangan</sub>

**Pembahasan:** Pasangan: $4$: $20,24,40,44,48$ (5); $5$: $20,40,55$ (3); $8$: $24,40,48$ (3); $11$: $33,44,55$ (3); $12$: $24,48$ (2). Terbanyak adalah $4$ dengan $5$ pasangan.
**Acuan:** siswa — siswa hal.179 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas8-b04-a-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: pernyataan tentang relasi*

Apabila diketahui suatu himpunan $A = \{4, 7, 9, 12\}$; himpunan $B = \{3, 8, 10, 13, 15\}$; dan relasi dari $A$ ke $B$ adalah "kurang dari", maka pernyataan yang benar tentang relasi tersebut adalah ....

- A. Range relasi tersebut sama dengan himpunan $B$  
  <sub>Salah: mengira range = kodomain padahal $3$ tidak lebih dari anggota $A$ mana pun</sub>
- B. Pasangan $(9, 8)$ merupakan anggota relasi tersebut  
  <sub>Salah: tidak memeriksa arah: $9 < 8$ salah</sub>
- **C. Anggota $12$ berpasangan dengan tepat dua anggota $B$** ✅  
  <sub>Benar: 12 kurang dari 13 dan 15 saja, sehingga tepat dua pasangan: (12,13), (12,15)</sub>
- D. Anggota $4$ berpasangan dengan tepat tiga anggota $B$  
  <sub>Salah: 4 kurang dari $8, 10, 13, 15$ sehingga ada empat pasangan, bukan tiga</sub>

**Pembahasan:** Pasangan: $4$: $8,10,13,15$; $7$: $8,10,13,15$; $9$: $10,13,15$; $12$: $13,15$. Range $= \{8,10,13,15\}$ (3 tidak ikut). $(9,8)$ bukan anggota. $4$ punya 4 pasangan, $12$ punya 2 pasangan.
**Acuan:** siswa — siswa hal.174 Contoh 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas8-b04-a-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: banyak anggota perkalian himpunan*

Apabila diketahui himpunan $D = \{\text{suatu bilangan kurang dari } 60 \text{ dan merupakan bilangan ganjil yang habis dibagi lima}\}$ dan himpunan $E = \{2, 3, 5\}$, maka banyak anggota himpunan semua pasangan berurutan dari $D$ ke $E$ (yaitu $D \times E$) adalah ....

- A. 9  
  <sub>Salah: menjumlahkan $n(D)+n(E)$ bukan mengalikan</sub>
- **B. 18** ✅  
  <sub>Benar: $D=\{5,15,25,35,45,55\}$ sehingga $n(D)=6$ dan $n(D\times E)=6\times3=18$</sub>
- C. 33  
  <sub>Salah: menghitung semua kelipatan lima (11 bilangan) tanpa menyaring ganjil, lalu dikali 3</sub>
- D. 15  
  <sub>Salah: membuang $55$ sehingga $n(D)=5$</sub>

**Pembahasan:** Bilangan ganjil kelipatan lima di bawah $60$: $5,15,25,35,45,55$ (6 bilangan). Banyak pasangan $D \times E = 6 \times 3 = 18$.
**Acuan:** siswa — siswa hal.166 Ayo Berkomunikasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas8-b04-a-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: relasi kebalikan dari konteks*

Pada sebuah lomba lari, Raka dan Sari memakai nomor punggung 7. Tono memakai nomor punggung 9. Uci memakai nomor punggung 10, sedangkan Vera dan Wira sama-sama memakai nomor punggung 12. Relasi dari himpunan nomor punggung ke himpunan peserta adalah "dipakai oleh". Himpunan pasangan berurutan relasi tersebut adalah ....

- A. $\{(7, \text{Raka}), (9, \text{Tono}), (10, \text{Uci}), (12, \text{Vera})\}$  
  <sub>Salah: mengira satu nomor hanya untuk satu peserta</sub>
- B. $\{(\text{Raka}, 7), (\text{Sari}, 7), (\text{Tono}, 9), (\text{Uci}, 10), (\text{Vera}, 12), (\text{Wira}, 12)\}$  
  <sub>Salah: arah terbalik (peserta ke nomor, relasi 'memakai')</sub>
- **C. $\{(7, \text{Raka}), (7, \text{Sari}), (9, \text{Tono}), (10, \text{Uci}), (12, \text{Vera}), (12, \text{Wira})\}$** ✅  
  <sub>Benar: arah dari nomor ke peserta, nomor 7 dan 12 masing-masing dipakai dua peserta</sub>
- D. $\{(7, \text{Raka}), (7, \text{Sari}), (9, \text{Tono}), (10, \text{Uci}), (12, \text{Vera}), (12, \text{Wira}), (10, \text{Vera})\}$  
  <sub>Salah: menambahkan pasangan $(10, \text{Vera})$ yang tidak ada di cerita</sub>

**Pembahasan:** Nomor 7 dipakai Raka dan Sari, 9 dipakai Tono, 10 dipakai Uci, 12 dipakai Vera dan Wira. Anggota pertama nomor, anggota kedua peserta.
**Acuan:** siswa — siswa hal.181 Soal Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas8-b04-a-medium-bt01-006
*variasi (angka) | C4 | 4 langkah | jenis: daerah hasil dari himpunan deskripsi*

Apabila diketahui himpunan $D = \{\text{suatu bilangan kurang dari } 45 \text{ dan merupakan bilangan genap yang habis dibagi enam}\}$ dan himpunan $F = \{4, 5, 9\}$, maka daerah hasil (range) relasi "faktor dari" dari himpunan $F$ ke himpunan $D$ adalah ....

- A. $\{12, 18, 24, 30\}$  
  <sub>Salah: melewatkan $36$ yang merupakan kelipatan $4$ dan $9$</sub>
- B. $\{4, 5, 9\}$  
  <sub>Salah: menulis himpunan $F$ (domain) sebagai range</sub>
- C. $\{6, 12, 18, 24, 30, 36, 42\}$  
  <sub>Salah: menulis seluruh himpunan $D$ (kodomain) sebagai range</sub>
- **D. $\{12, 18, 24, 30, 36\}$** ✅  
  <sub>Benar: $D=\{6,12,18,24,30,36,42\}$; 4 faktor 12, 24, 36; 5 faktor 30; 9 faktor 18, 36</sub>

**Pembahasan:** $D = \{6,12,18,24,30,36,42\}$. Pasangan: $(4,12),(4,24),(4,36),(5,30),(9,18),(9,36)$. Range adalah anggota $D$ yang mendapat pasangan: $\{12,18,24,30,36\}$.
**Acuan:** siswa — siswa hal.166 Ayo Berkomunikasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas8-b04-a-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: menafsirkan pasangan dalam konteks*

Relasi "gemar" dari himpunan siswa $\{\text{Ani}, \text{Budi}, \text{Citra}, \text{Dedi}\}$ ke himpunan mata pelajaran dinyatakan dengan himpunan pasangan berurutan $\{(\text{Ani}, \text{Seni}), (\text{Ani}, \text{IPA}), (\text{Budi}, \text{IPA}), (\text{Citra}, \text{Seni}), (\text{Citra}, \text{IPS}), (\text{Citra}, \text{IPA}), (\text{Dedi}, \text{Olahraga}), (\text{Dedi}, \text{IPA})\}$. Banyak siswa yang gemar lebih dari satu mata pelajaran adalah ....

- **A. 3** ✅  
  <sub>Benar: Ani 2 mapel, Budi 1, Citra 3, Dedi 2; siswa dengan lebih dari satu mapel: Ani, Citra, Dedi</sub>
- B. 2  
  <sub>Salah: hanya menghitung siswa dengan tepat dua mata pelajaran (tidak termasuk Citra)</sub>
- C. 8  
  <sub>Salah: menghitung banyak pasangan berurutan, bukan banyak siswa</sub>
- D. 4  
  <sub>Salah: menghitung semua anggota domain tanpa menyaring</sub>

**Pembahasan:** Hitung pasangan tiap siswa: Ani 2, Budi 1, Citra 3, Dedi 2. Yang lebih dari satu: Ani, Citra, Dedi, yaitu 3 siswa.
**Acuan:** siswa — siswa hal.173

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas8-b04-a-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: relasi sebagai himpunan bagian A x B*

Diketahui $A = \{2, 4, 6\}$ dan $B = \{3, 4, 5, 8\}$. Relasi $R$ dari $A$ ke $B$ adalah "kurang dari", yang merupakan himpunan bagian dari $A \times B$. Banyak anggota $A \times B$ yang bukan anggota $R$ adalah ....

- A. 12  
  <sub>Salah: menghitung seluruh $A \times B$</sub>
- **B. 5** ✅  
  <sub>Benar: $n(A\times B)=12$, $n(R)=7$, selisihnya 5</sub>
- C. 7  
  <sub>Salah: menghitung banyak anggota $R$, bukan yang bukan anggota $R$</sub>
- D. 6  
  <sub>Salah: keliru menghitung anggota $R$ sebagai 6 sehingga selisihnya 6</sub>

**Pembahasan:** $R=\{(2,3),(2,4),(2,5),(2,8),(4,5),(4,8),(6,8)\}$ sehingga $n(R)=7$. $n(A \times B)=3\times4=12$. Yang bukan anggota $R$: $12-7=5$.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas8-b04-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: relasi turunan dari silsilah keluarga*

Pak Hadi memiliki dua anak, yaitu Rina dan Dodi. Rina memiliki dua anak, yaitu Tia dan Udin. Dodi memiliki satu anak, yaitu Vina. Relasi "cucu dari" dari himpunan $\{\text{Tia}, \text{Udin}, \text{Vina}\}$ ke himpunan $\{\text{Pak Hadi}, \text{Rina}, \text{Dodi}\}$ dinyatakan dengan himpunan pasangan berurutan ....

- **A. $\{(\text{Tia}, \text{Pak Hadi}), (\text{Udin}, \text{Pak Hadi}), (\text{Vina}, \text{Pak Hadi})\}$** ✅  
  <sub>Benar: Tia, Udin, dan Vina semuanya anak dari anak Pak Hadi, sehingga cucu Pak Hadi</sub>
- B. $\{(\text{Pak Hadi}, \text{Tia}), (\text{Pak Hadi}, \text{Udin}), (\text{Pak Hadi}, \text{Vina})\}$  
  <sub>Salah: urutan pasangan terbalik (arah dari kakek ke cucu)</sub>
- C. $\{(\text{Tia}, \text{Rina}), (\text{Udin}, \text{Rina}), (\text{Vina}, \text{Dodi})\}$  
  <sub>Salah: menukar relasi cucu dengan relasi 'anak dari'</sub>
- D. $\{(\text{Tia}, \text{Pak Hadi}), (\text{Udin}, \text{Pak Hadi})\}$  
  <sub>Salah: mengira hanya anak dari Rina yang cucu Pak Hadi, Vina terlewat</sub>

**Pembahasan:** Tia dan Udin anak Rina; Vina anak Dodi; Rina dan Dodi anak Pak Hadi. Jadi ketiganya cucu Pak Hadi.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas8-b04-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: menentukan aturan relasi dari pasangan*

Relasi dari himpunan $A = \{3, 4, 5, 6\}$ ke himpunan $B = \{10, 17, 26, 37\}$ dinyatakan dengan himpunan pasangan berurutan $\{(3, 10), (4, 17), (5, 26), (6, 37)\}$. Jika $a$ anggota $A$ dan $b$ anggota $B$, aturan yang berlaku untuk semua pasangan adalah ....

- A. $b = 2a + 4$  
  <sub>Salah: hanya cocok untuk pasangan pertama $(3, 10)$, tetapi gagal pada $(4, 17)$</sub>
- **B. $b = a^2 + 1$** ✅  
  <sub>Benar: $3^2+1=10$, $4^2+1=17$, $5^2+1=26$, $6^2+1=37$</sub>
- C. $b = a^2 - 1$  
  <sub>Salah: salah tanda: mengurangi 1, bukan menambah</sub>
- D. $b = a^2$  
  <sub>Salah: lupa menambah 1 setelah mengkuadratkan</sub>

**Pembahasan:** Selisih $b-a^2$ pada tiap pasangan: $10-9=1$, $17-16=1$, $26-25=1$, $37-36=1$. Aturannya $b=a^2+1$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas8-b04-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: menentukan aturan lalu menerapkannya pada anggota baru*

Pada pemaparan koordinat relasi dari himpunan $A$ ke himpunan $B$ (anggota $A$ pada sumbu mendatar dan anggota $B$ pada sumbu tegak) terdapat titik $(1, 4)$, $(2, 7)$, $(3, 10)$, dan $(5, 16)$. Jika aturan yang sama berlaku untuk semua anggota, anggota $B$ yang berpasangan dengan anggota $A$ bernilai $9$ adalah ....

- A. 12  
  <sub>Salah: hanya melihat pasangan pertama sebagai $b=a+3$</sub>
- B. 36  
  <sub>Salah: hanya melihat pasangan pertama sebagai $b=4a$</sub>
- C. 27  
  <sub>Salah: memakai $b = 3a$ dan lupa menambah 1</sub>
- **D. 28** ✅  
  <sub>Benar: aturan $b=3a+1$; untuk $a=9$ diperoleh $b=28$</sub>

**Pembahasan:** Naik 1 pada $a$ membuat $b$ naik 3, dan $a=1$ memberi $b=4$, sehingga $b=3a+1$. Untuk $a=9$: $b=3\times9+1=28$.
**Acuan:** siswa — siswa hal.173

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas8-b04-a-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: anggota kawan tanpa pasangan dari notasi himpunan*

Diketahui himpunan $A = \{x \mid 2 < x < 8,\ x \text{ bilangan asli}\}$ dan himpunan $B = \{y \mid 10 < y < 25,\ y \text{ bilangan genap}\}$. Pada relasi "faktor dari" dari himpunan $A$ ke himpunan $B$, anggota $B$ yang tidak mendapat pasangan adalah ....

- A. 14  
  <sub>Salah: mengira 7 bukan faktor dari 14</sub>
- B. 20  
  <sub>Salah: mengira 4 dan 5 bukan faktor dari 20</sub>
- C. 16  
  <sub>Salah: mengira 4 bukan faktor dari 16</sub>
- **D. 22** ✅  
  <sub>Benar: $A=\{3,4,5,6,7\}$, $B=\{12,14,16,18,20,22,24\}$; 22 tidak habis dibagi satu pun anggota $A$</sub>

**Pembahasan:** $A=\{3,4,5,6,7\}$, $B=\{12,14,16,18,20,22,24\}$. $12$: 3,4,6; $14$: 7; $16$: 4; $18$: 3,6; $20$: 4,5; $24$: 3,4,6. $22$ hanya habis dibagi 2, 11, 22, tidak ada di $A$.
**Acuan:** siswa — siswa hal.165

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas8-b04-a-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: pernyataan tentang relasi*

Lima anak memesan makanan di sebuah warung dengan relasi "memesan" dari himpunan anak ke himpunan menu $B = \{\text{nasi goreng}, \text{sate}, \text{bakso}, \text{soto}, \text{rawon}\}$. Pasangan berurutan relasinya adalah $\{(\text{Ali}, \text{soto}), (\text{Bina}, \text{bakso}), (\text{Cici}, \text{soto}), (\text{Dodi}, \text{sate}), (\text{Eka}, \text{bakso})\}$. Pernyataan yang benar adalah ....

- A. Pasangan $(\text{soto}, \text{Dodi})$ adalah anggota relasi "dipesan oleh"  
  <sub>Salah: Dodi memesan sate, bukan soto</sub>
- B. Relasi "dipesan oleh" memiliki 3 pasangan berurutan karena ada 3 jenis makanan yang dipesan  
  <sub>Salah: mengira banyak pasangan sama dengan banyak jenis makanan; kebalikannya tetap 5 pasangan</sub>
- **C. Range relasi "memesan" adalah $\{\text{soto}, \text{bakso}, \text{sate}\}$** ✅  
  <sub>Benar: makanan yang dipesan: soto, bakso, sate (tiap makanan dihitung sekali)</sub>
- D. Kodomain dan range relasi "memesan" sama  
  <sub>Salah: kodomain adalah seluruh menu (5), sedangkan nasi goreng dan rawon tidak dipesan</sub>

**Pembahasan:** Range = menu yang dipesan = $\{\text{soto}, \text{bakso}, \text{sate}\}$. Kodomain memiliki 5 menu. Relasi kebalikan memiliki 5 pasangan dan memuat $(\text{soto}, \text{Ali})$, $(\text{soto}, \text{Cici})$, bukan $(\text{soto}, \text{Dodi})$.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas8-b04-a-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: membandingkan banyak pasangan antar relasi*

Diketahui $K = \{1, 2, 3, 4\}$ dan $L = \{2, 4, 6, 8, 10\}$. Relasi dari himpunan $K$ ke himpunan $L$ yang menghasilkan pasangan berurutan paling banyak di antara pilihan berikut adalah ....

- **A. "kurang dari"** ✅  
  <sub>Benar: kurang dari: 16 pasangan; faktor dari: 13; kelipatan dari: 3; lebih dari: 2</sub>
- B. "kelipatan dari"  
  <sub>Salah: hanya 3 pasangan: $(2,2),(4,2),(4,4)$</sub>
- C. "faktor dari"  
  <sub>Salah: hanya 13 pasangan, kurang dari 16 pasangan relasi 'kurang dari'</sub>
- D. "lebih dari"  
  <sub>Salah: hanya 2 pasangan: $(3,2),(4,2)$</sub>

**Pembahasan:** Kurang dari: $1$ dengan 5, $2$ dengan 4, $3$ dengan 4, $4$ dengan 3 anggota $L$ = 16. Faktor dari: $5+5+1+2=13$. Kelipatan dari: 3. Lebih dari: 2. Terbanyak: "kurang dari".
**Acuan:** siswa — siswa hal.180

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas8-b04-a-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: relasi kebalikan akar dan kuadrat*

Diketahui himpunan $A = \{3, 4, 6, 9\}$ dan $B = \{9, 16, 25, 36, 81\}$. Relasi "akar dari" dari himpunan $A$ ke himpunan $B$ berarti anggota $A$ adalah akar kuadrat anggota $B$. Himpunan pasangan berurutan relasi "kuadrat dari" dari himpunan $B$ ke himpunan $A$ adalah ....

- A. $\{(9, 3), (16, 4), (25, 5), (36, 6), (81, 9)\}$  
  <sub>Salah: menyertakan $(25, 5)$ padahal $5$ bukan anggota $A$</sub>
- **B. $\{(9, 3), (16, 4), (36, 6), (81, 9)\}$** ✅  
  <sub>Benar: $3^2=9$, $4^2=16$, $6^2=36$, $9^2=81$; 25 tidak punya akar di $A$; relasi kuadrat dari: anggota $B$ adalah kuadrat anggota $A$ sehingga pasangan ($B$, $A$)</sub>
- C. $\{(9, 3), (16, 4), (36, 6)\}$  
  <sub>Salah: melewatkan $(81, 9)$ karena tidak menguji anggota terakhir</sub>
- D. $\{(3, 9), (4, 16), (6, 36), (9, 81)\}$  
  <sub>Salah: urutan terbalik: itu relasi 'akar dari' dari $A$ ke $B$, bukan 'kuadrat dari' dari $B$ ke $A$</sub>

**Pembahasan:** Akar kuadrat: $\sqrt9=3$, $\sqrt{16}=4$, $\sqrt{36}=6$, $\sqrt{81}=9$ ada di $A$; $\sqrt{25}=5$ tidak ada di $A$. Relasi "kuadrat dari" dari $B$ ke $A$ memasangkan $B$ dulu: $\{(9,3),(16,4),(36,6),(81,9)\}$.
**Acuan:** siswa — siswa hal.176

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas8-b04-a-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi diagram dengan anggota di luar kodomain*

Diketahui $A = \{1, 2, 3, 4\}$ dan $B = \{a, b, c\}$. Sebuah diagram panah dari $A$ ke $B$ digambar dengan pasangan berurutan $\{(1, a), (2, b), (3, c), (4, d)\}$, dengan $d$ bukan anggota $B$. Relasi dari $A$ ke $B$ adalah himpunan bagian dari $A \times B$. Pernyataan yang benar adalah ....

- **A. Himpunan pasangan itu bukan relasi dari $A$ ke $B$ karena $(4, d)$ bukan anggota $A \times B$** ✅  
  <sub>Benar: relasi dari A ke B harus himpunan bagian A x B; (4,d) tidak ada di A x B</sub>
- B. Himpunan pasangan itu adalah relasi dari $A$ ke $B$ karena relasi boleh memuat pasangan dengan anggota di luar $B$  
  <sub>Salah: mengira relasi tidak dibatasi oleh kodomain</sub>
- C. Himpunan pasangan itu adalah relasi dari $A$ ke $B$ karena setiap anggota $A$ mempunyai pasangan  
  <sub>Salah: hanya memeriksa anggota $A$ dan mengabaikan kodomain</sub>
- D. Himpunan pasangan itu adalah relasi dari $B$ ke $A$ karena ada huruf yang dipasangkan dengan bilangan  
  <sub>Salah: salah arah: anggota pertama pasangan berasal dari $A$, bukan $B$</sub>

**Pembahasan:** $A \times B$ hanya memuat pasangan dengan anggota kedua $a$, $b$, atau $c$. Pasangan $(4, d)$ tidak ada di $A \times B$, sehingga himpunan itu bukan himpunan bagian $A \times B$ dan bukan relasi dari $A$ ke $B$.
**Acuan:** siswa — siswa hal.177

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas8-b04-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi relasi kosong*

Diketahui $A = \{1, 2, 3\}$ dan $B = \{5, 6, 7\}$. Relasi dari $A$ ke $B$ adalah "lebih dari". Pernyataan yang benar tentang relasi tersebut adalah ....

- A. Relasinya sama dengan $A \times B$ sehingga memiliki 9 pasangan berurutan  
  <sub>Salah: membalik syarat: $A \times B$ memuat semua pasangan, bukan pasangan yang memenuhi syarat</sub>
- B. Rangenya sama dengan $B$ karena range selalu sama dengan kodomain  
  <sub>Salah: mengira range = kodomain padahal tidak ada anggota $B$ yang mendapat pasangan</sub>
- C. Bukan relasi karena tidak ada anggota $A$ yang berpasangan dengan anggota $B$  
  <sub>Salah: mengira relasi harus memuat paling sedikit satu pasangan</sub>
- **D. Relasinya himpunan kosong, tetap merupakan relasi karena himpunan kosong adalah himpunan bagian $A \times B$, dan rangenya kosong** ✅  
  <sub>Benar: tidak ada anggota $A$ yang lebih dari anggota $B$; $\emptyset \subset A \times B$</sub>

**Pembahasan:** Karena $1, 2, 3$ lebih kecil dari $5, 6, 7$, tidak ada pasangan yang memenuhi "lebih dari". Relasinya $\emptyset$, himpunan bagian $A \times B$, sehingga tetap relasi dengan range $\emptyset$.
**Acuan:** siswa — siswa hal.181

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas8-b04-a-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan menentukan range*

Rani menyatakan bahwa daerah hasil (range) relasi "kurang dari" dari $A = \{2, 5, 7\}$ ke $B = \{1, 3, 5, 8\}$ adalah $\{1, 3, 5, 8\}$. Pernyataan yang benar tentang jawaban Rani adalah ....

- **A. Keliru, karena $1$ tidak lebih dari anggota $A$ mana pun; range yang benar $\{3, 5, 8\}$** ✅  
  <sub>Benar: Rani menulis seluruh kodomain; $1$ tidak mendapat pasangan</sub>
- B. Keliru, range yang benar adalah $\{2, 5, 7\}$  
  <sub>Salah: menulis anggota $A$ (domain) sebagai range</sub>
- C. Keliru, range yang benar adalah $\{5, 8\}$  
  <sub>Salah: membuang $3$ padahal $2 < 3$</sub>
- D. Benar, karena range selalu sama dengan kodomain  
  <sub>Salah: menyamakan range dengan kodomain</sub>

**Pembahasan:** Pasangan: $(2,3),(2,5),(2,8),(5,8),(7,8)$. Anggota $B$ yang mendapat pasangan adalah $3, 5, 8$; $1$ tidak. Range $=\{3,5,8\}$ berbeda dari kodomain.
**Acuan:** siswa — siswa hal.174

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas8-b04-a-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Klaim: "Pada setiap relasi dari $A$ ke $B$, banyak anggota range sama dengan banyak anggota domain." Diketahui $A = \{1, 2, 3\}$ dan $B = \{a, b, c, d\}$ dengan domain $A$. Relasi dari $A$ ke $B$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $\{(1, a), (2, b), (3, c)\}$  
  <sub>Salah: range $\{a,b,c\}$ berjumlah 3 sehingga justru mendukung klaim</sub>
- B. $\{(1, d), (2, a), (3, c)\}$  
  <sub>Salah: range $\{d,a,c\}$ berjumlah 3 sehingga mendukung klaim</sub>
- C. $\{(1, b), (2, c), (3, d)\}$  
  <sub>Salah: range $\{b,c,d\}$ berjumlah 3 sehingga mendukung klaim</sub>
- **D. $\{(1, a), (2, a), (3, b)\}$** ✅  
  <sub>Benar: domain 3 anggota, range $\{a, b\}$ 2 anggota</sub>

**Pembahasan:** Contoh penyangkal harus punya range yang banyaknya bukan 3. Hanya $\{(1,a),(2,a),(3,b)\}$ yang rangenya $\{a,b\}$ (2 anggota).
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas8-b04-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: parameter agar banyak pasangan tertentu*

Diketahui $A = \{2, 3, 5\}$ dan $B = \{6, 10, k\}$. Relasi dari $A$ ke $B$ adalah "faktor dari". Nilai $k$ yang membuat relasi tersebut memiliki tepat $5$ pasangan berurutan adalah ....

- A. $15$  
  <sub>Salah: faktor di $A$ ada dua ($3$ dan $5$) sehingga total 6</sub>
- B. $30$  
  <sub>Salah: faktor di $A$ ada tiga ($2, 3, 5$) sehingga total 7</sub>
- C. $49$  
  <sub>Salah: tidak ada faktor di $A$ sehingga total tetap 4</sub>
- **D. $21$** ✅  
  <sub>Benar: 6 dan 10 memberi 4 pasangan; 21 hanya punya faktor 3 di A sehingga total 5</sub>

**Pembahasan:** Pasangan dari $6$: $(2,6),(3,6)$; dari $10$: $(2,10),(5,10)$ sehingga 4 pasangan. Perlu tepat satu pasangan lagi dari $k$: $21$ hanya habis dibagi $3$.
**Acuan:** siswa — siswa hal.180

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas8-b04-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: parameter pada aturan relasi*

Diketahui $A = \{1, 2, 3, 4\}$ dan $B = \{5, 6, 7, 8, 9\}$. Relasi dari $A$ ke $B$ memiliki aturan $b = a + p$ dengan $p$ bilangan asli. Jika setiap anggota $A$ harus mempunyai pasangan di $B$, nilai $p$ terbesar yang mungkin adalah ....

- A. $8$  
  <sub>Salah: hanya $a = 1$ yang menghasilkan anggota $B$ ($9$)</sub>
- **B. $5$** ✅  
  <sub>Benar: p=5 memberi 6,7,8,9 semuanya di B; p=6 memberi 10 yang di luar B</sub>
- C. $4$  
  <sub>Salah: nilai $p$ yang memenuhi tetapi bukan yang terbesar</sub>
- D. $6$  
  <sub>Salah: $a = 4$ menghasilkan $10$ yang bukan anggota $B$</sub>

**Pembahasan:** Untuk $p=5$: $1\to6$, $2\to7$, $3\to8$, $4\to9$ semuanya di $B$. Untuk $p=6$: $4\to10$ tidak di $B$. Jadi $p$ terbesar $5$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas8-b04-a-hard-bt01-007
*orisinal | C6 | 4 langkah | jenis: merancang relasi dari beberapa syarat*

Diketahui $A = \{1, 2, 3, 4\}$ dan $B = \{2, 3, 4, 5, 6\}$. Sebuah relasi dari $A$ ke $B$ harus memenuhi tiga syarat: memuat pasangan $(1, 3)$, memiliki tepat $5$ pasangan berurutan, dan rangenya tepat $\{3, 4\}$. Relasi yang memenuhi ketiga syarat adalah ....

- A. $\{(1, 4), (2, 3), (2, 4), (3, 3), (4, 4)\}$  
  <sub>Salah: tidak memuat pasangan $(1, 3)$</sub>
- B. $\{(1, 3), (1, 5), (2, 3), (3, 4), (4, 3)\}$  
  <sub>Salah: range memuat $5$ sehingga bukan $\{3, 4\}$</sub>
- **C. $\{(1, 3), (1, 4), (2, 3), (3, 4), (4, 3)\}$** ✅  
  <sub>Benar: memuat (1,3), 5 pasangan, range {3,4}</sub>
- D. $\{(1, 3), (2, 3), (3, 4), (4, 4)\}$  
  <sub>Salah: hanya 4 pasangan</sub>

**Pembahasan:** Periksa tiap pilihan terhadap tiga syarat. Hanya pilihan pertama yang memenuhi semuanya; tiap pilihan lain melanggar tepat satu syarat.
**Acuan:** siswa — siswa hal.180

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas8-b04-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: membandingkan dua aturan relasi*

Dina mengusulkan aturan $b = a^2 + 2$ dan Edo mengusulkan aturan $b = 3a$ untuk relasi dari $A = \{1, 2, 3, 4, 5, 6\}$. Banyak anggota $A$ yang oleh kedua aturan dipasangkan dengan anggota $B$ yang sama adalah ....

- A. $6$  
  <sub>Salah: menyangka kedua aturan menghasilkan nilai sama untuk semua anggota $A$</sub>
- **B. $2$** ✅  
  <sub>Benar: a=1: 3 dan 3; a=2: 6 dan 6; a=3..6 berbeda</sub>
- C. $3$  
  <sub>Salah: mengira $a = 3$ cocok karena $3 \times 3 = 9$ dan $3^2 = 9$, lupa menambah $2$</sub>
- D. $1$  
  <sub>Salah: hanya menemukan $a = 1$ dan lupa $a = 2$</sub>

**Pembahasan:** Bandingkan: $a=1$: $3$ dan $3$; $a=2$: $6$ dan $6$; $a=3$: $11$ dan $9$; $a=4$: $18$ dan $12$; $a=5$: $27$ dan $15$; $a=6$: $38$ dan $18$. Hanya 2 anggota.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas8-b04-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: evaluasi relasi kebalikan*

Diketahui $A = \{1, 2, 3, 4\}$ dan $B = \{x, y\}$. Relasi $R$ dari $A$ ke $B$ adalah $\{(1, x), (2, x), (3, y)\}$. Relasi kebalikan $R$ adalah relasi dari $B$ ke $A$ dengan arah pasangan dibalik. Pernyataan yang benar tentang relasi kebalikan tersebut adalah ....

- A. Rangenya sama dengan $A$, yaitu $\{1, 2, 3, 4\}$  
  <sub>Salah: menganggap range = kodomain; $4$ tidak berpasangan</sub>
- **B. Rangenya $\{1, 2, 3\}$ dan banyak pasangannya $3$** ✅  
  <sub>Benar: pasangan kebalikan $(x,1),(x,2),(y,3)$; anggota 4 tidak berpasangan</sub>
- C. Rangenya $\{x, y\}$  
  <sub>Salah: mengambil anggota $B$ yang kini menjadi domain</sub>
- D. Pasangan $(1, x)$ merupakan anggota relasi kebalikan  
  <sub>Salah: arah pasangan tidak dibalik</sub>

**Pembahasan:** Kebalikan $R$ adalah $\{(x,1),(x,2),(y,3)\}$. Range kebalikan adalah anggota $A$ yang berpasangan, yaitu $\{1,2,3\}$; ada 3 pasangan.
**Acuan:** siswa — siswa hal.162

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas8-b04-a-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan jawaban siswa*  **[warning validator]**

Diketahui $A =$ {bilangan bulat antara $3$ dan $9$} dan $B =$ {enam bilangan cacah pertama}. Relasi dari $A$ ke $B$ adalah "satu lebihnya dari". Seorang siswa menulis: Domain $= \{4, 5, 6, 7, 8\}$, Kodomain $= \{0, 1, 2, 3, 4, 5\}$, Range $= \{3, 4, 5, 6, 7\}$. Kesalahan siswa tersebut adalah ....

- **A. Range memuat $6$ dan $7$ yang bukan anggota $B$; range yang benar $\{3, 4, 5\}$** ✅  
  <sub>Benar: pasangan yang ada: (4,3),(5,4),(6,5); 7 dan 8 tidak punya pasangan</sub>
- B. Range seharusnya $\{4, 5, 6, 7, 8\}$  
  <sub>Salah: menulis domain sebagai range</sub>
- C. Domain seharusnya $\{5, 6, 7, 8\}$  
  <sub>Salah: domain adalah seluruh $A$, jadi tulisan siswa sudah benar</sub>
- D. Kodomain seharusnya $\{1, 2, 3, 4, 5, 6\}$  
  <sub>Salah: bilangan cacah dimulai dari $0$, jadi kodomain siswa benar</sub>

**Pembahasan:** $A=\{4,5,6,7,8\}$, $B=\{0,1,2,3,4,5\}$. Pasangan $(a, a-1)$ dengan $a-1 \in B$: $(4,3),(5,4),(6,5)$. Range $=\{3,4,5\}$; siswa memasukkan $6$ dan $7$.
**Acuan:** siswa — siswa hal.175
**Warning:** kelas8-b04-a-hard-bt01-010: jawaban benar jauh lebih panjang dari distraktor (mudah ditebak)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas8-b04-a-hard-bt01-011
*orisinal | C5 | 3 langkah | jenis: membaca titik koordinat relasi*

Relasi dari himpunan $A = \{1, 2, 3, 4\}$ ke himpunan $B = \{1, 2, 3, 4, 5\}$ dipaparkan pada koordinat dengan anggota $A$ pada sumbu mendatar dan anggota $B$ pada sumbu tegak. Titik yang tergambar adalah $(1, 3)$, $(2, 3)$, $(3, 3)$, dan $(4, 3)$. Pernyataan yang benar adalah ....

- A. Relasi tersebut memiliki $3$ pasangan berurutan  
  <sub>Salah: mengira banyak pasangan sama dengan koordinat tegak $3$</sub>
- B. Anggota $1$ dari $A$ berpasangan dengan tiga anggota $B$  
  <sub>Salah: menafsirkan titik tegak 3 sebagai banyak pasangan</sub>
- C. Range relasi tersebut adalah $\{1, 2, 3, 4\}$  
  <sub>Salah: mengambil koordinat mendatar (anggota $A$) sebagai range</sub>
- **D. Range hanya $\{3\}$ dan anggota $3$ berpasangan dengan keempat anggota $A$** ✅  
  <sub>Benar: keempat titik memiliki koordinat tegak 3</sub>

**Pembahasan:** Titik $(a, b)$: $a \in A$ mendatar, $b \in B$ tegak. Semua titik tegaknya $3$, sehingga range $\{3\}$ dan ada 4 pasangan.
**Acuan:** siswa — siswa hal.173

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas8-b04-a-hard-bt01-012
*orisinal | C5 | 3 langkah | jenis: batas banyak pasangan relasi*

Relasi $R$ dari himpunan $A$ ke himpunan $B$ dengan $n(A) = 5$ dan $n(B) = 4$ dapat berupa relasi apa saja (himpunan bagian $A \times B$). Pernyataan yang pasti benar untuk setiap relasi $R$ tersebut adalah ....

- A. Banyak pasangan berurutan paling sedikit $5$ sebab $n(A) = 5$  
  <sub>Salah: mengira setiap anggota $A$ pasti berpasangan; relasi kosong punya 0 pasangan</sub>
- B. Banyak anggota range selalu $5$ sebab $n(A) = 5$  
  <sub>Salah: mengambil $n(A)$ padahal range himpunan bagian $B$</sub>
- **C. Banyak pasangan berurutan paling banyak $20$ dan banyak anggota range paling banyak $4$** ✅  
  <sub>Benar: $R \subset A\times B$ sehingga $n(R)\le 20$; range subset $B$ sehingga paling banyak 4</sub>
- D. Banyak pasangan berurutan selalu $20$ dan range selalu $B$  
  <sub>Salah: mengira setiap relasi sama dengan $A \times B$</sub>

**Pembahasan:** $n(A \times B) = 5 \times 4 = 20$ dan $R$ adalah himpunan bagian, jadi $n(R) \le 20$. Range himpunan bagian $B$ sehingga paling banyak 4. Relasi kosong membantah dua pilihan lain.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas8-b04-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: parameter agar semua pasangan memenuhi*

Diketahui $A$ memiliki tiga anggota berbeda, yaitu $2$, $5$, dan bilangan asli $k$, dan $B = \{6, 7, 8, 9\}$. Agar relasi "kurang dari" dari $A$ ke $B$ sama dengan seluruh $A \times B$, nilai $k$ terbesar yang mungkin adalah ....

- A. $6$  
  <sub>Salah: $6$ tidak kurang dari $6$ sehingga $(6, 6)$ tidak memenuhi</sub>
- B. $5$  
  <sub>Salah: lupa bahwa $k$ harus berbeda dari anggota $5$ yang sudah ada</sub>
- **C. $4$** ✅  
  <sub>Benar: semua anggota A harus kurang dari 6, k berbeda dari 2 dan 5, jadi k terbesar 4</sub>
- D. $8$  
  <sub>Salah: mengambil anggota $B$ sebagai batas atas</sub>

**Pembahasan:** Agar $A \times B$ seluruhnya memenuhi "kurang dari", setiap anggota $A$ harus kurang dari $6$. Bilangan asli $k<6$ yang berbeda dari $2$ dan $5$: $1,3,4$. Terbesar $4$.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas8-b04-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: evaluasi A x B dan B x A*

Diketahui $A = \{1, 2\}$ dan $B = \{2, 3, 4\}$. Pernyataan yang benar tentang $A \times B$ dan $B \times A$ adalah ....

- A. $A \times B = B \times A$ karena banyak anggotanya sama  
  <sub>Salah: menyamakan himpunan hanya karena banyak anggotanya sama</sub>
- **B. $n(A \times B) = n(B \times A) = 6$, tetapi $(1, 2)$ hanya anggota $A \times B$** ✅  
  <sub>Benar: $A\times B$ dan $B\times A$ sama banyak (6); $(1,2)$ tidak ada di $B \times A$ karena $1 \notin B$</sub>
- C. $(2, 2)$ hanya anggota $A \times B$  
  <sub>Salah: $2$ ada di $A$ dan $B$ sehingga $(2,2)$ ada di keduanya</sub>
- D. $n(B \times A) = 5$ karena $2$ dihitung sekali  
  <sub>Salah: mengira anggota yang muncul di dua himpunan dihitung sekali; $3 \times 2 = 6$</sub>

**Pembahasan:** $A\times B=\{(1,2),(1,3),(1,4),(2,2),(2,3),(2,4)\}$ dan $B\times A=\{(2,1),(3,1),(4,1),(2,2),(3,2),(4,2)\}$. Sama banyak tetapi anggotanya berbeda.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas8-b04-a-hard-bt01-015
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan menyusun relasi akar dari*

Diketahui $A = \{2, 3, 4, 5, 6, 7\}$ dan $B = \{4, 9, 16, 25, 36, 49\}$. Seorang siswa menuliskan relasi "akar dari" dari $A$ ke $B$ sebagai $\{(2, 4), (3, 9), (5, 25), (6, 36), (7, 49)\}$. Kesalahan siswa tersebut adalah ....

- A. Urutan pasangan terbalik, seharusnya $(4, 2), (9, 3), (25, 5), (36, 6), (49, 7)$  
  <sub>Salah: pasangan relasi dari $A$ ke $B$ memuat anggota $A$ terlebih dahulu</sub>
- B. Kurang pasangan $(4, 4)$ karena $4$ adalah akar dari $4$  
  <sub>Salah: mengira bilangan adalah akar dari dirinya sendiri</sub>
- **C. Kurang pasangan $(4, 16)$ karena $4$ adalah akar dari $16$** ✅  
  <sub>Benar: $\sqrt{16}=4$ dan $4 \in A$, $16 \in B$ sehingga $(4,16)$ harus ada</sub>
- D. Pasangan $(7, 49)$ keliru karena akar dari $49$ adalah $9$  
  <sub>Salah: salah menghitung akar kuadrat $49$</sub>

**Pembahasan:** Akar kuadrat anggota $B$: $2,3,4,5,6,7$, semuanya di $A$, jadi ada 6 pasangan. Siswa melewatkan $(4,16)$.
**Acuan:** siswa — siswa hal.176

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
