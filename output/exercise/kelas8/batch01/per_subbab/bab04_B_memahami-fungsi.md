# Lembar koreksi — kelas8 SMP8-B4 subbab B: Memahami Fungsi

45 soal | easy 15, medium 15, hard 15 | variasi 18, orisinal 27

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas8-b04-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: memeriksa fungsi dari relasi dua himpunan*

Diketahui bahwa himpunan $R$ dan $S$ memiliki anggota masing-masing adalah $R = \{2, 3, 4, 6\}$ dan $S = \{10, 15, 20, 30, 35\}$. Apabila "Anggota $R$ seperlima kali anggota $S$" adalah relasi yang ditentukan, maka hubungan antara himpunan $R$ dan $S$ ....

- A. Bukan fungsi, karena banyak anggota $S$ lebih banyak daripada banyak anggota $R$  
  <sub>Salah: mengira banyak anggota kedua himpunan harus sama</sub>
- B. Bukan fungsi, karena anggota 35 di $S$ tidak mempunyai pasangan di $R$  
  <sub>Salah: memeriksa syarat dari arah yang salah (dari kodomain, bukan dari daerah asal)</sub>
- **C. Fungsi, karena setiap anggota $R$ mempunyai tepat satu pasangan di $S$** ✅  
  <sub>Benar: Relasi berarti $s = 5r$: $2 \to 10$, $3 \to 15$, $4 \to 20$, $6 \to 30$. Setiap anggota $R$ punya tepat satu pasangan di $S$, jadi fungsi.</sub>
- D. Bukan fungsi, karena ada anggota $R$ yang berpasangan dengan dua anggota $S$  
  <sub>Salah: mengira ada pasangan ganda padahal tiap anggota $R$ hanya punya satu pasangan</sub>

**Pembahasan:** Pasangan: $(2,10), (3,15), (4,20), (6,30)$. Semua anggota $R$ berpasangan tepat satu kali, sedangkan 35 di $S$ tidak berpasangan (tidak masalah). Jadi fungsi.
**Acuan:** pretest — kelas8-b04-p0194-soal-laihan-4-2-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas8-b04-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: memeriksa fungsi dari relasi dua himpunan*

Misalkan diketahui himpunan $P = \{8, 10, 13, 15\}$ dan himpunan $Q = \{6, 8, 11, 13, 14\}$. "dua lebihnya dari" adalah relasi yang ditentukan. Apakah hubungan antara $P$ dan $Q$ merupakan fungsi?

- **A. Fungsi, karena 8, 10, 13, dan 15 masing-masing berpasangan dengan tepat satu anggota $Q$** ✅  
  <sub>Benar: Pasangan $(8,6), (10,8), (13,11), (15,13)$; semua anggota $P$ berpasangan tepat satu kali.</sub>
- B. Bukan fungsi, karena bilangan 8 muncul di $P$ dan di $Q$  
  <sub>Salah: mengira anggota yang sama di dua himpunan melarang fungsi</sub>
- C. Bukan fungsi, karena anggota $Q$ lebih banyak daripada anggota $P$  
  <sub>Salah: mengira banyak anggota harus sama</sub>
- D. Bukan fungsi, karena 14 di $Q$ tidak berpasangan dengan anggota $P$  
  <sub>Salah: memeriksa anggota kodomain, padahal yang diperiksa anggota daerah asal</sub>

**Pembahasan:** Relasi "dua lebihnya dari": $p = q + 2$. $8 \to 6$, $10 \to 8$, $13 \to 11$, $15 \to 13$. Tiap anggota $P$ punya tepat satu pasangan, jadi fungsi.
**Acuan:** siswa — siswa hal.186 Contoh 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas8-b04-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: memeriksa fungsi dari relasi dua himpunan*

Misalkan diketahui himpunan $K = \{14, 21, 28, 35\}$ dan himpunan $L = \{2, 3, 7, 8, 11\}$. "Anggota $K$ adalah tujuh kali anggota $L$" merupakan relasi yang telah ditentukan. Apakah relasi himpunan $K$ dan $L$ merupakan fungsi?

- A. Fungsi, karena anggota $L$ yang tidak berpasangan (7, 8, dan 11) tidak memengaruhi status fungsi  
  <sub>Salah: mengira anggota kodomain tanpa pasangan menentukan, atau mengabaikan anggota $K$ tanpa pasangan</sub>
- B. Fungsi, karena anggota $K$ lebih sedikit daripada anggota $L$  
  <sub>Salah: mengira perbandingan banyak anggota menentukan fungsi</sub>
- C. Fungsi, karena 14 dan 21 berpasangan dengan tepat satu anggota $L$  
  <sub>Salah: hanya memeriksa sebagian anggota daerah asal</sub>
- **D. Bukan fungsi, karena 28 dan 35 di $K$ tidak mempunyai pasangan di $L$** ✅  
  <sub>Benar: $14 = 7 \times 2$ dan $21 = 7 \times 3$ berpasangan, tetapi $28 = 7 \times 4$ dan $35 = 7 \times 5$ tidak, sebab 4 dan 5 tidak ada di $L$.</sub>

**Pembahasan:** Syarat fungsi: setiap anggota $K$ punya tepat satu pasangan di $L$. 28 dan 35 tidak punya pasangan, sehingga bukan fungsi.
**Acuan:** siswa — siswa hal.187 Contoh 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas8-b04-b-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: anggota yang berpasangan dan status fungsi*

Himpunan $A = \{2, 3, 5, 7\}$ dan himpunan $B = \{6, 9, 15, 18, 30\}$. Apabila relasinya adalah "sepertiga dari", maka anggota himpunan $A$ yang mempunyai pasangan pada himpunan $B$ dan status relasi tersebut adalah ....

- **A. 2, 3, dan 5; bukan fungsi** ✅  
  <sub>Benar: $2 \to 6$, $3 \to 9$, $5 \to 15$; untuk 7 diperlukan 21 yang tidak ada di $B$, sehingga 7 tanpa pasangan dan relasi bukan fungsi.</sub>
- B. 2, 3, 5, dan 7; fungsi  
  <sub>Salah: mengira semua anggota $A$ berpasangan</sub>
- C. 2, 3, dan 5; fungsi  
  <sub>Salah: benar menemukan anggota berpasangan tetapi lupa bahwa 7 tanpa pasangan membuat relasi bukan fungsi</sub>
- D. 6, 9, dan 15; bukan fungsi  
  <sub>Salah: menyebut anggota $B$, bukan anggota $A$ yang diminta</sub>

**Pembahasan:** Anggota $A$ dengan pasangan: 2, 3, 5. Karena 7 tidak berpasangan, relasi bukan fungsi.
**Acuan:** siswa — siswa hal.192 Soal Latihan 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas8-b04-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: mencari x dari nilai fungsi*

Apabila diketahui fungsi $f(x) = 6x - 4$ dan $f(x) = 14$, maka hitunglah nilai dari $x$.

- A. $-3$  
  <sub>Salah: salah tanda pada hasil akhir</sub>
- B. $\frac{7}{3}$  
  <sub>Salah: mengabaikan $-4$ sehingga $6x = 14$</sub>
- **C. $3$** ✅  
  <sub>Benar: $6x - 4 = 14$, maka $6x = 18$, sehingga $x = 3$.</sub>
- D. $\frac{5}{3}$  
  <sub>Salah: mengurangi 4 dari 14 (seharusnya menambah) sehingga $6x = 10$</sub>

**Pembahasan:** $6x - 4 = 14 \Rightarrow 6x = 18 \Rightarrow x = 3$.
**Acuan:** siswa — siswa hal.201 Contoh 4.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas8-b04-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: daerah hasil dari rumus fungsi*

Apabila diketahui fungsi $f : A \to B$ ditentukan oleh $f(x) = 7x - 5$ dengan $A = \{-5, 0, 6, 8\}$, dan $B$ adalah himpunan bilangan riil. Maka daerah hasil dari fungsi $f$ adalah ....

- A. $\{-35, 0, 42, 56\}$  
  <sub>Salah: lupa mengurangi 5 setelah mengalikan 7</sub>
- B. $\{-10, -5, 1, 3\}$  
  <sub>Salah: mengurangi 5 dari $x$ tanpa mengalikan 7</sub>
- **C. $\{-40, -5, 37, 51\}$** ✅  
  <sub>Benar: $f(-5) = -35 - 5 = -40$, $f(0) = -5$, $f(6) = 42 - 5 = 37$, $f(8) = 56 - 5 = 51$.</sub>
- D. $\{-30, -5, 37, 51\}$  
  <sub>Salah: salah tanda saat menyubstitusi $x = -5$ ($-35 + 5$)</sub>

**Pembahasan:** Substitusikan setiap anggota $A$ ke $f(x) = 7x - 5$ sehingga diperoleh $\{-40, -5, 37, 51\}$.
**Acuan:** siswa — siswa hal.201 Contoh 4.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas8-b04-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi dari rumus*

Jika diketahui suatu fungsi $g$ dengan daerah asal $B = \{1, 3, 5, 7\}$; daerah kawan merupakan himpunan bilangan asli, dan fungsi liniernya adalah $g(x) = 4x + 5$; maka nilai $g(1)$, $g(3)$, $g(5)$, dan $g(7)$ berturut-turut adalah ....

- A. $6, 8, 10, 12$  
  <sub>Salah: hanya menambah 5 tanpa mengalikan 4</sub>
- B. $-1, 7, 15, 23$  
  <sub>Salah: mengubah $+5$ menjadi $-5$</sub>
- C. $24, 32, 40, 48$  
  <sub>Salah: mengalikan 4 terhadap $(x + 5)$ bukan hanya $x$</sub>
- **D. $9, 17, 25, 33$** ✅  
  <sub>Benar: $g(1) = 4 + 5 = 9$, $g(3) = 12 + 5 = 17$, $g(5) = 20 + 5 = 25$, $g(7) = 28 + 5 = 33$.</sub>

**Pembahasan:** Substitusikan $x$ ke $g(x) = 4x + 5$: 9, 17, 25, 33.
**Acuan:** siswa — siswa hal.207 Soal Latihan 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas8-b04-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: rumus fungsi dari cerita tarif*

Sebuah ojek daring menetapkan biaya tarif awal sebesar Rp5.000,00 dan tarif per kilometer sebesar Rp2.500,00. Berapa besar tarif yang dibutuhkan untuk perjalanan sejauh 14 km?

- A. Rp72.500,00  
  <sub>Salah: mengalikan tarif awal dengan jarak lalu menambah tarif per km</sub>
- **B. Rp40.000,00** ✅  
  <sub>Benar: Tarif $= 5.000 + 14 \times 2.500 = 5.000 + 35.000 = 40.000$.</sub>
- C. Rp105.000,00  
  <sub>Salah: menjumlahkan tarif awal dan tarif per km lebih dahulu lalu mengalikan dengan jarak</sub>
- D. Rp35.000,00  
  <sub>Salah: lupa menambahkan tarif awal</sub>

**Pembahasan:** Tarif $B(x) = 2.500x + 5.000$, untuk $x = 14$ diperoleh Rp40.000,00.
**Acuan:** siswa — siswa hal.195 Ayo Bereksplorasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas8-b04-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: koefisien dari nilai fungsi*

Diketahui suatu fungsi $k$ dengan rumus $k(x) = ax - 7$. Nilai fungsi $k$ untuk $x = 4$ adalah 13. Nilai $a$ adalah ....

- A. $\frac{3}{2}$  
  <sub>Salah: mengurangi 7 dari 13 (seharusnya menambah)</sub>
- **B. $5$** ✅  
  <sub>Benar: $k(4) = 4a - 7 = 13$, maka $4a = 20$, sehingga $a = 5$.</sub>
- C. $-5$  
  <sub>Salah: salah tanda pada hasil akhir</sub>
- D. $16$  
  <sub>Salah: menjumlahkan $4 + a - 7 = 13$ bukan mengalikan</sub>

**Pembahasan:** $4a - 7 = 13 \Rightarrow 4a = 20 \Rightarrow a = 5$.
**Acuan:** siswa — siswa hal.207 Soal Latihan 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas8-b04-b-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: definisi fungsi*

Relasi dari himpunan $A$ ke himpunan $B$ disebut fungsi apabila ....

- A. setiap anggota $A$ boleh dihubungkan dengan dua anggota $B$ atau lebih  
  <sub>Salah: mengira satu anggota daerah asal boleh punya banyak pasangan</sub>
- B. setiap anggota $B$ dihubungkan dengan tepat satu anggota $A$  
  <sub>Salah: menukar arah daerah asal dan daerah kawan</sub>
- **C. setiap anggota $A$ dihubungkan dengan tepat satu anggota $B$** ✅  
  <sub>Benar: sesuai definisi: setiap anggota daerah asal berpasangan dengan tepat satu anggota daerah kawan</sub>
- D. ada anggota $A$ yang tidak dihubungkan dengan anggota $B$ mana pun  
  <sub>Salah: mengira anggota daerah asal boleh tanpa pasangan</sub>

**Pembahasan:** Fungsi menghubungkan setiap anggota daerah asal dengan tepat satu anggota daerah kawan.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas8-b04-b-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: memilih himpunan pasangan yang merupakan fungsi*

Diketahui $P = \{1, 2, 3\}$ dan $Q = \{a, b\}$. Himpunan pasangan berurutan berikut yang merupakan fungsi dari $P$ ke $Q$ adalah ....

- A. $\{(2, a), (2, b), (3, a)\}$  
  <sub>Salah: 2 berpasangan dengan dua anggota dan 1 tidak berpasangan</sub>
- B. $\{(1, a), (1, b), (3, b)\}$  
  <sub>Salah: 1 berpasangan dengan dua anggota dan 2 tidak berpasangan</sub>
- C. $\{(1, a), (2, b)\}$  
  <sub>Salah: anggota 3 tidak berpasangan</sub>
- **D. $\{(1, b), (2, a), (3, b)\}$** ✅  
  <sub>Benar: semua anggota P (1, 2, 3) masing-masing punya tepat satu pasangan di Q</sub>

**Pembahasan:** Fungsi dari $P$ ke $Q$ harus memuat tepat satu pasangan untuk 1, 2, dan 3; hanya pilihan pertama yang demikian.
**Acuan:** siswa — siswa hal.187

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas8-b04-b-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: variabel bebas dan terikat*

Pada fungsi $f(x) = 5x - 2$, nilai $x$ disebut ....

- **A. variabel bebas** ✅  
  <sub>Benar: $x$ adalah nilai yang disubstitusikan (variabel bebas), sedangkan $f(x)$ variabel terikat</sub>
- B. variabel terikat  
  <sub>Salah: menukar peran $x$ dengan $f(x)$</sub>
- C. konstanta  
  <sub>Salah: mengira $x$ adalah bilangan tetap</sub>
- D. koefisien  
  <sub>Salah: mengira $x$ adalah angka pengali</sub>

**Pembahasan:** $x$ variabel bebas, $f(x)$ atau $y$ variabel terikat.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas8-b04-b-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: rumus fungsi dari pasangan berurutan*

Himpunan pasangan berurutan $\{(1, 3), (2, 6), (3, 9), (4, 12)\}$ dapat dinyatakan dengan rumus fungsi ....

- A. $f(x) = x + 2$  
  <sub>Salah: hanya mencocokkan pasangan pertama ($1 + 2 = 3$)</sub>
- B. $f(x) = 3x + 3$  
  <sub>Salah: menambah konstanta yang tidak ada pada pola</sub>
- C. $f(x) = \frac{x}{3}$  
  <sub>Salah: menukar peran $x$ dan $y$</sub>
- **D. $f(x) = 3x$** ✅  
  <sub>Benar: setiap $y$ sama dengan 3 kali $x$</sub>

**Pembahasan:** $3 = 3 \times 1$, $6 = 3 \times 2$, $9 = 3 \times 3$, $12 = 3 \times 4$, sehingga $f(x) = 3x$.
**Acuan:** siswa — siswa hal.197

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas8-b04-b-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: daerah hasil dari rumus fungsi*

Fungsi $f : A \to B$ dengan $A = \{1, 2, 3\}$, $B = \{1, 2, 3, 4, 5, 6\}$, dan $f(x) = x + 3$. Daerah hasil fungsi $f$ adalah ....

- A. $\{1, 2, 3\}$  
  <sub>Salah: menyebut daerah asal sebagai daerah hasil</sub>
- **B. $\{4, 5, 6\}$** ✅  
  <sub>Benar: $f(1) = 4$, $f(2) = 5$, $f(3) = 6$</sub>
- C. $\{3, 4, 5\}$  
  <sub>Salah: menambahkan 2 (bukan 3) saat substitusi</sub>
- D. $\{1, 2, 3, 4, 5, 6\}$  
  <sub>Salah: menyebut daerah kawan sebagai daerah hasil</sub>

**Pembahasan:** Daerah hasil adalah himpunan nilai $f(x)$ untuk $x$ di daerah asal.
**Acuan:** siswa — siswa hal.201

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas8-b04-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: nilai fungsi dari rumus*

Diketahui fungsi $f(x) = -2x + 9$. Nilai $f(-3)$ adalah ....

- **A. $15$** ✅  
  <sub>Benar: $f(-3) = -2(-3) + 9 = 6 + 9 = 15$</sub>
- B. $-3$  
  <sub>Salah: mengurangkan 9 dari hasil perkalian 6</sub>
- C. $4$  
  <sub>Salah: menjumlahkan $-2$, $-3$, dan $9$ bukan mengalikan</sub>
- D. $3$  
  <sub>Salah: salah tanda: $-2 	imes 3 = -6$ lalu $-6 + 9$</sub>

**Pembahasan:** Substitusi $x = -3$: $-2 \times (-3) + 9 = 15$.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas8-b04-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: rumus fungsi linear dari dua nilai*

Diketahui fungsi linier $f$ memiliki nilai 3 ketika nilai $x = 4$, dan memiliki nilai $-9$ ketika $x = 7$. Rumus fungsi $f$ adalah ....

- A. $f(x) = -4x - 13$  
  <sub>Salah: $a$ benar tetapi salah tanda saat mencari $b$ ($b = 3 - 16$)</sub>
- B. $f(x) = 4x - 13$  
  <sub>Salah: salah tanda pada $a$ ($a = 4$), lalu $b = 3 - 16 = -13$</sub>
- **C. $f(x) = -4x + 19$** ✅  
  <sub>Benar: $4a + b = 3$ dan $7a + b = -9$; dikurangkan diperoleh $3a = -12$, $a = -4$; lalu $b = 3 + 16 = 19$.</sub>
- D. $f(x) = -4x + 3$  
  <sub>Salah: mengambil $b$ sama dengan nilai fungsi pertama</sub>

**Pembahasan:** Misalkan $f(x) = ax + b$. Dari $f(4) = 3$ dan $f(7) = -9$: $4a + b = 3$ dan $7a + b = -9$. Kurangkan: $3a = -12$ sehingga $a = -4$, $b = 3 - 4(-4) = 19$. Jadi $f(x) = -4x + 19$. Cek: $f(7) = -28 + 19 = -9$.
**Acuan:** siswa — siswa hal.202 Contoh 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas8-b04-b-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: rumus fungsi linear dari dua nilai*

Suhu sebuah cairan yang dipanaskan merupakan fungsi linear dari lamanya pemanasan $t$ menit, yaitu $T(t) = at + b$ derajat Celsius. Setelah 2 menit suhunya 26 derajat Celsius dan setelah 6 menit suhunya 50 derajat Celsius. Rumus fungsi suhu $T(t)$ adalah ....

- A. $T(t) = 6t - 14$  
  <sub>Salah: salah tanda saat mencari $b$ ($b = 12 - 26$)</sub>
- B. $T(t) = 14t + 6$  
  <sub>Salah: nilai $a$ dan $b$ tertukar</sub>
- **C. $T(t) = 6t + 14$** ✅  
  <sub>Benar: $2a + b = 26$ dan $6a + b = 50$; dikurangkan $4a = 24$, $a = 6$; $b = 26 - 12 = 14$.</sub>
- D. $T(t) = 6t + 26$  
  <sub>Salah: mengambil $b$ sama dengan suhu pada menit ke-2</sub>

**Pembahasan:** Dari $2a + b = 26$ dan $6a + b = 50$ diperoleh $a = 6$ dan $b = 14$. Jadi $T(t) = 6t + 14$.
**Acuan:** siswa — siswa hal.202 Contoh 4.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas8-b04-b-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: fungsi linear dalam konteks volume*

Ketinggian air bak penampungan mencapai 38 liter setelah 4 menit, dan menjadi 86 liter setelah 10 menit. Banyaknya air setelah diisikan selama $t$ menit diberikan oleh $V(t) = V_0 + at$ liter. Banyaknya air di bak setelah 15 menit adalah ....

- **A. 126 liter** ✅  
  <sub>Benar: $a = (86 - 38) : (10 - 4) = 8$; $V_0 = 38 - 4 \times 8 = 6$; $V(15) = 6 + 8 \times 15 = 126$.</sub>
- B. 150 liter  
  <sub>Salah: menghitung $V_0 = 38 - 8 = 30$ (mengurangi $a$ sekali, bukan $4a$)</sub>
- C. 120 liter  
  <sub>Salah: lupa menambahkan $V_0$ sehingga hanya $8 \times 15$</sub>
- D. 158 liter  
  <sub>Salah: mengambil $V_0 = 38$ (volume pada menit ke-4) bukan volume awal</sub>

**Pembahasan:** Dua persamaan $V_0 + 4a = 38$ dan $V_0 + 10a = 86$ memberi $a = 8$, $V_0 = 6$. Maka $V(15) = 6 + 120 = 126$ liter.
**Acuan:** siswa — siswa hal.209 Soal Latihan 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas8-b04-b-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: fungsi linear dalam konteks volume*

Air dialirkan dari keran ke dalam sebuah drum. Setelah 2 menit drum berisi 17 liter dan setelah 5 menit berisi 38 liter. Banyaknya air dalam drum setelah $t$ menit adalah $V(t) = V_0 + at$ liter. Volume air dalam drum sebelum keran dibuka adalah ....

- **A. 3 liter** ✅  
  <sub>Benar: $V_0 + 2a = 17$ dan $V_0 + 5a = 38$; dikurangkan $3a = 21$, $a = 7$; $V_0 = 17 - 14 = 3$.</sub>
- B. 7 liter  
  <sub>Salah: mengira laju aliran $a$ adalah volume awal</sub>
- C. 10 liter  
  <sub>Salah: mengurangi $a$ sekali ($17 - 7$), padahal seharusnya $2a$</sub>
- D. 17 liter  
  <sub>Salah: menganggap volume setelah 2 menit sebagai volume awal</sub>

**Pembahasan:** Dari $a = 7$ liter per menit, $V_0 = 17 - 2 \times 7 = 3$ liter.
**Acuan:** siswa — siswa hal.209 Soal Latihan 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas8-b04-b-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: banyak fungsi dari dua himpunan*

Diketahui himpunan $K = \{a, b, c\}$ dan himpunan $L = \{5, 6, 7, 8\}$. Banyak fungsi yang dapat dibentuk dari himpunan $K$ ke himpunan $L$ adalah ....

- A. 81  
  <sub>Salah: menukar peran himpunan sehingga dihitung $3^4$</sub>
- B. 24  
  <sub>Salah: menghitung pasangan yang tidak boleh sama ($4 \times 3 \times 2$)</sub>
- C. 12  
  <sub>Salah: mengalikan banyak anggota kedua himpunan ($3 \times 4$)</sub>
- **D. 64** ✅  
  <sub>Benar: Setiap dari 3 anggota $K$ boleh berpasangan dengan salah satu dari 4 anggota $L$, sehingga $4 \times 4 \times 4 = 4^3 = 64$.</sub>

**Pembahasan:** Tiap anggota $K$ punya 4 pilihan pasangan di $L$, dan pilihan antar anggota bebas: $4^3 = 64$.
**Acuan:** siswa — siswa hal.194 Ayo Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas8-b04-b-medium-bt01-006
*variasi (konteks) | C3 | 2 langkah | jenis: banyak fungsi dari dua himpunan*

Lima siswa, yaitu Ani, Budi, Citra, Dedi, dan Eko, masing-masing mendaftar tepat satu kegiatan, yaitu pramuka atau PMR. Banyak fungsi dari himpunan siswa tersebut ke himpunan kegiatan {pramuka, PMR} adalah ....

- A. 7  
  <sub>Salah: menjumlahkan banyak anggota kedua himpunan</sub>
- **B. 32** ✅  
  <sub>Benar: Setiap siswa punya 2 pilihan kegiatan: $2^5 = 32$.</sub>
- C. 10  
  <sub>Salah: mengalikan banyak anggota kedua himpunan ($5 \times 2$)</sub>
- D. 25  
  <sub>Salah: menukar basis dan pangkat ($5^2$)</sub>

**Pembahasan:** Daerah asal 5 anggota, daerah kawan 2 anggota, banyak fungsi $2^5 = 32$.
**Acuan:** siswa — siswa hal.195 Ayo Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas8-b04-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: tarif dan jarak dalam konteks*

Sebuah taksi daring menetapkan tarif awal Rp8.000,00 dan tarif per kilometer Rp4.000,00. Sejauh berapa kilometer yang dapat ditempuh untuk uang sebesar Rp72.000,00?

- A. 18 km  
  <sub>Salah: lupa mengurangi tarif awal ($72.000 : 4.000$)</sub>
- **B. 16 km** ✅  
  <sub>Benar: Tarif $B(x) = 8.000 + 4.000x = 72.000$, maka $4.000x = 64.000$ dan $x = 16$.</sub>
- C. 20 km  
  <sub>Salah: menambahkan tarif awal ke uang ($80.000 : 4.000$)</sub>
- D. 6 km  
  <sub>Salah: membagi uang dengan jumlah tarif awal dan tarif per kilometer ($72.000 : 12.000$)</sub>

**Pembahasan:** $8.000 + 4.000x = 72.000 \Rightarrow x = 16$ km.
**Acuan:** siswa — siswa hal.196 Ayo Bereksplorasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas8-b04-b-medium-bt01-008
*variasi (angka) | C4 | 3 langkah | jenis: pasangan parameter fungsi bilangan bulat*

Diketahui fungsi $f(x) = ax + 6$ dan $f(b) = -30$ dengan $a$ bilangan asli dan $b$ bilangan bulat. Banyak pasangan $(a, b)$ yang memenuhi adalah ....

- A. 8  
  <sub>Salah: tidak menghitung $a = 36$</sub>
- **B. 9** ✅  
  <sub>Benar: $ab + 6 = -30$ sehingga $ab = -36$. Karena $a$ asli, $a$ harus faktor positif 36 (1, 2, 3, 4, 6, 9, 12, 18, 36) dan $b = -36/a$ otomatis bulat: 9 pasangan.</sub>
- C. 18  
  <sub>Salah: mengizinkan $a$ juga negatif sehingga banyak pasangan digandakan</sub>
- D. 5  
  <sub>Salah: menghitung pasangan faktor tanpa memperhatikan urutan</sub>

**Pembahasan:** Dari $f(b) = ab + 6 = -30$ diperoleh $ab = -36$. Faktor positif 36 ada 9, tiap $a$ menentukan satu $b$.
**Acuan:** siswa — siswa hal.208 Ayo Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas8-b04-b-medium-bt01-009
*variasi (angka) | C3 | 4 langkah | jenis: nilai fungsi kuadrat*

Apabila diketahui suatu fungsi $g$ dengan rumus fungsi $g(x) = 5x^2 - 4x + 7$, maka nilai $g(-4) + g(5)$ adalah ....

- A. 535  
  <sub>Salah: mengkuadratkan $5x$ sehingga $g(-4) = 423$</sub>
- **B. 215** ✅  
  <sub>Benar: $g(-4) = 5(16) + 16 + 7 = 103$ dan $g(5) = 125 - 20 + 7 = 112$, jumlahnya 215.</sub>
- C. 183  
  <sub>Salah: salah tanda pada suku $-4x$ di $x = -4$ ($80 - 16 + 7 = 71$)</sub>
- D. 55  
  <sub>Salah: $(-4)^2$ dihitung $-16$ sehingga $g(-4) = -57$</sub>

**Pembahasan:** $g(-4) = 5 \cdot 16 - 4(-4) + 7 = 103$; $g(5) = 5 \cdot 25 - 20 + 7 = 112$; jumlah 215.
**Acuan:** siswa — siswa hal.208 Soal Latihan 4.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas8-b04-b-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: daerah hasil dari interval*

Fungsi $f$ ditentukan oleh $f(x) = 5x + 2$ dengan daerah asal $\{x \mid -2 \le x < 3,\ x \in R\}$. Daerah hasil fungsi $f$ adalah ....

- A. $\{f(x) \mid -8 < f(x) \le 17\}$  
  <sub>Salah: tanda batas tertukar: batas bawah termasuk, batas atas tidak</sub>
- B. $\{f(x) \mid -4 \le f(x) < 5\}$  
  <sub>Salah: hanya menambah 2 tanpa mengalikan 5</sub>
- **C. $\{f(x) \mid -8 \le f(x) < 17\}$** ✅  
  <sub>Benar: $-2 \le x < 3$ dikali 5: $-10 \le 5x < 15$; ditambah 2: $-8 \le 5x + 2 < 17$.</sub>
- D. $\{f(x) \mid -10 \le f(x) < 15\}$  
  <sub>Salah: lupa menambahkan 2</sub>

**Pembahasan:** Ubah $-2 \le x < 3$ menjadi bentuk $5x + 2$: $-8 \le f(x) < 17$.
**Acuan:** siswa — siswa hal.203

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas8-b04-b-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: daerah hasil dari interval*

Fungsi $f$ ditentukan oleh $f(x) = -3x + 1$ dengan daerah asal $\{x \mid 1 < x \le 4,\ x \in R\}$. Daerah hasil fungsi $f$ adalah ....

- A. $\{f(x) \mid -11 \le f(x) \le -2\}$  
  <sub>Salah: menganggap $x = 1$ ikut sehingga batas atas termasuk</sub>
- B. $\{f(x) \mid -12 \le f(x) < -3\}$  
  <sub>Salah: lupa menambahkan 1</sub>
- C. $\{f(x) \mid -11 < f(x) \le -2\}$  
  <sub>Salah: arah tanda tidak dibalik sehingga jenis batas (termasuk/tidak) ikut tertukar</sub>
- **D. $\{f(x) \mid -11 \le f(x) < -2\}$** ✅  
  <sub>Benar: $1 < x \le 4$ dikali $-3$ (arah dibalik): $-12 \le -3x < -3$; ditambah 1: $-11 \le f(x) < -2$.</sub>

**Pembahasan:** Karena $x = 1$ tidak termasuk, $f(1) = -2$ tidak termasuk; $x = 4$ termasuk sehingga $f(4) = -11$ termasuk.
**Acuan:** siswa — siswa hal.203

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas8-b04-b-medium-bt01-012
*orisinal | C3 | 4 langkah | jenis: nilai fungsi linear dari dua data*

Fungsi linear $f$ ditentukan oleh $f(x) = px + q$. Diketahui $f(-3) = 14$ dan $f(1) = -2$. Nilai $f(5)$ adalah ....

- A. $18$  
  <sub>Salah: salah tanda pada $p$ ($p = 4$, $q = -2$)</sub>
- B. $-20$  
  <sub>Salah: lupa menambahkan $q$</sub>
- **C. $-18$** ✅  
  <sub>Benar: $-3p + q = 14$ dan $p + q = -2$; dikurangkan $-4p = 16$, $p = -4$, $q = 2$; $f(5) = -20 + 2 = -18$.</sub>
- D. $-22$  
  <sub>Salah: $p$ benar tetapi $q = -2$ (salah tanda)</sub>

**Pembahasan:** Eliminasi memberi $p = -4$ dan $q = 2$; $f(5) = -4(5) + 2 = -18$.
**Acuan:** siswa — siswa hal.202

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas8-b04-b-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: banyak fungsi dari dua himpunan*

Diketahui $P = \{1, 2, 3, 4\}$ dan $Q = \{a, b, c\}$. Banyak fungsi dari $P$ ke $Q$ yang memenuhi $f(1) = a$ adalah ....

- A. 64  
  <sub>Salah: menukar basis dan pangkat ($4^3$)</sub>
- B. 81  
  <sub>Salah: mengabaikan syarat $f(1) = a$ ($3^4$)</sub>
- C. 12  
  <sub>Salah: mengalikan $4 \times 3$</sub>
- **D. 27** ✅  
  <sub>Benar: $f(1)$ sudah tetap; anggota 2, 3, 4 masing-masing punya 3 pilihan: $3^3 = 27$.</sub>

**Pembahasan:** Tiga anggota bebas, masing-masing 3 pilihan: $3 \times 3 \times 3 = 27$.
**Acuan:** siswa — siswa hal.194

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas8-b04-b-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: membandingkan dua fungsi tarif*

Taksi A menetapkan tarif awal Rp3.000,00 dan Rp4.000,00 per kilometer. Taksi B menetapkan tarif awal Rp15.000,00 dan Rp2.500,00 per kilometer. Pada jarak berapa kilometer kedua taksi menetapkan tarif yang sama?

- **A. 8 km** ✅  
  <sub>Benar: $A(x) = 3.000 + 4.000x$ dan $B(x) = 15.000 + 2.500x$. Sama bila $1.500x = 12.000$, jadi $x = 8$.</sub>
- B. 10 km  
  <sub>Salah: lupa mengurangi tarif awal taksi A ($15.000 : 1.500$)</sub>
- C. 3 km  
  <sub>Salah: membagi selisih tarif awal dengan tarif per kilometer taksi A ($12.000 : 4.000$)</sub>
- D. 12 km  
  <sub>Salah: menjumlahkan tarif awal ($18.000 : 1.500$)</sub>

**Pembahasan:** $3.000 + 4.000x = 15.000 + 2.500x \Rightarrow 1.500x = 12.000 \Rightarrow x = 8$ km. Tarif keduanya Rp35.000,00.
**Acuan:** siswa — siswa hal.195

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas8-b04-b-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: banyak anggota daerah hasil*

Fungsi $f : A \to B$ ditentukan oleh $f(x) = x^2 - 1$ dengan $A = \{-3, -2, -1, 0, 1, 2, 3\}$ dan $B$ himpunan bilangan bulat. Banyak anggota daerah hasil fungsi $f$ adalah ....

- A. 7  
  <sub>Salah: mengira banyak anggota daerah hasil sama dengan daerah asal</sub>
- B. 6  
  <sub>Salah: hanya mengurangi satu karena menganggap hanya $f(-1) = f(1)$ yang sama</sub>
- C. 3  
  <sub>Salah: tidak menghitung $f(0) = -1$ karena bernilai negatif</sub>
- **D. 4** ✅  
  <sub>Benar: $f(\pm 3) = 8$, $f(\pm 2) = 3$, $f(\pm 1) = 0$, $f(0) = -1$; daerah hasil $\{-1, 0, 3, 8\}$ beranggota 4.</sub>

**Pembahasan:** Nilai $f(x)$ berulang untuk $x$ dan $-x$: $\{8, 3, 0, -1\}$, sehingga 4 anggota.
**Acuan:** siswa — siswa hal.201

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas8-b04-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim relasi fungsi*

Relasi $R$ dari $A = \{1, 2, 3, 4, 5\}$ ke $B = \{5, 7, 9\}$ dinyatakan dengan himpunan pasangan berurutan $R = \{(1, 5), (2, 5), (3, 7), (4, 7), (5, 5)\}$. Pernyataan yang benar tentang $R$ adalah ....

- **A. $R$ merupakan fungsi dengan daerah hasil $\{5, 7\}$** ✅  
  <sub>Benar: Setiap anggota $A$ tepat satu pasangan, sehingga fungsi; nilai yang muncul hanya 5 dan 7.</sub>
- B. $R$ bukan fungsi karena anggota 9 pada $B$ tidak punya pasangan  
  <sub>Salah: syarat tanda fungsi hanya berlaku untuk daerah asal, bukan daerah kawan</sub>
- C. $R$ merupakan fungsi dengan daerah hasil $\{5, 7, 9\}$  
  <sub>Salah: menyamakan daerah hasil dengan daerah kawan; 9 tidak pernah menjadi pasangan</sub>
- D. $R$ bukan fungsi karena 5 berpasangan dengan tiga anggota $A$  
  <sub>Salah: mengira satu anggota daerah kawan tidak boleh dipasangkan dengan banyak anggota daerah asal</sub>

**Pembahasan:** Tiap anggota $A$ (1 sampai 5) muncul tepat sekali sebagai komponen pertama, jadi $R$ fungsi. Nilainya 5, 5, 7, 7, 5, sehingga daerah hasil $\{5, 7\}$. Anggota 9 di $B$ tidak dipasangkan, itu tidak melanggar syarat fungsi.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas8-b04-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim arah relasi*

Relasi "bilangan yang kuadratnya adalah" dari $P = \{0, 1, 4, 9\}$ ke $Q = \{-3, -2, -1, 0, 1, 2, 3\}$ menghubungkan $x \in P$ dengan $y \in Q$ bila $y^2 = x$. Pernyataan yang paling tepat adalah ....

- A. Relasi itu fungsi karena setiap anggota $P$ memiliki pasangan di $Q$  
  <sub>Salah: hanya memeriksa adanya pasangan, lupa syarat tepat satu pasangan</sub>
- B. Relasi itu fungsi karena $Q$ memiliki lebih banyak anggota daripada $P$  
  <sub>Salah: mengira banyak anggota daerah kawan menentukan sifat fungsi</sub>
- C. Relasi itu bukan fungsi karena anggota 3 pada $Q$ berpasangan dengan lebih dari satu anggota $P$  
  <sub>Salah: keliru arah relasi; 3 hanya berpasangan dengan 9, dan syarat berlaku untuk anggota $P$</sub>
- **D. Relasi itu bukan fungsi karena anggota 1 pada $P$ berpasangan dengan dua anggota $Q$, yaitu $-1$ dan $1$** ✅  
  <sub>Benar: $y^2 = 1$ dipenuhi $y = -1$ dan $y = 1$, sehingga 1 punya dua pasangan; demikian pula 4 dan 9.</sub>

**Pembahasan:** Pasangan: $(0, 0)$, $(1, -1)$, $(1, 1)$, $(4, -2)$, $(4, 2)$, $(9, -3)$, $(9, 3)$. Anggota 1, 4, dan 9 di daerah asal masing-masing punya dua pasangan, jadi bukan fungsi.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas8-b04-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim fungsi dari banyak anggota himpunan*

Fungsi $f$ dipetakan dari himpunan $A$ yang beranggota 5 ke himpunan $B$ yang beranggota 3. Pernyataan yang pasti benar adalah ....

- A. Daerah hasil $f$ pasti beranggota 3  
  <sub>Salah: mengira daerah hasil selalu sama dengan daerah kawan; fungsi konstan punya satu anggota daerah hasil</sub>
- B. Setiap anggota $B$ pasti menjadi pasangan dari anggota $A$  
  <sub>Salah: daerah kawan tidak harus terpakai semua</sub>
- **C. Ada paling sedikit dua anggota $A$ yang mempunyai pasangan yang sama di $B$** ✅  
  <sub>Benar: Lima anggota $A$ hanya boleh dipasangkan ke 3 anggota $B$, sehingga mustahil semua pasangannya berbeda.</sub>
- D. Tidak ada fungsi dari $A$ ke $B$ karena $A$ lebih banyak anggotanya  
  <sub>Salah: mengira fungsi menuntut daerah kawan paling sedikit sama banyak dengan daerah asal; padahal ada $3^5 = 243$ fungsi</sub>

**Pembahasan:** Setiap anggota $A$ punya tepat satu pasangan di $B$, total ada $3^5 = 243$ fungsi. Karena 5 anggota $A$ hanya punya 3 nilai kemungkinan, pasti ada nilai yang dipakai dua anggota atau lebih. Daerah hasil bisa 1, 2, atau 3 anggota, dan anggota $B$ boleh tidak terpakai.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas8-b04-b-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: parameter agar relasi menjadi fungsi*

Relasi $R = \{(1, 4), (2, 7), (3, 5), (2, 2k + 1)\}$ dari $A = \{1, 2, 3\}$ ke himpunan bilangan asli dengan $k$ bilangan asli. Nilai $k$ agar $R$ merupakan fungsi adalah ....

- A. $4$  
  <sub>Salah: salah hitung $2k = 7 + 1 = 8$ sehingga $k = 4$</sub>
- **B. $3$** ✅  
  <sub>Benar: Anggota 2 punya pasangan 7 dan $2k + 1$; agar fungsi keduanya harus sama: $2k + 1 = 7$, $k = 3$.</sub>
- C. $7$  
  <sub>Salah: mengira $k$ sendiri harus sama dengan 7</sub>
- D. $2$  
  <sub>Salah: menyamakan $2k + 1$ dengan 5 (pasangan anggota 3), padahal yang bersama komponen pertama 2 adalah 7</sub>

**Pembahasan:** Dua pasangan berkomponen pertama 2 adalah $(2, 7)$ dan $(2, 2k + 1)$. Syarat fungsi: nilainya sama, $2k + 1 = 7$, jadi $k = 3$. Dengan $k = 3$, $R = \{(1, 4), (2, 7), (3, 5)\}$ fungsi.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas8-b04-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: parameter agar fungsi memenuhi daerah kawan*

Fungsi $f : A \to B$ ditentukan oleh $f(x) = px - 1$ dengan $A = \{-1, 0, 2\}$, $B = \{-5, -1, 1, 3, 7\}$, dan $p$ bilangan bulat positif. Nilai $p$ agar $f$ benar-benar fungsi dari $A$ ke $B$ adalah ....

- A. $3$  
  <sub>Salah: $f(-1) = -4$ dan $f(2) = 5$ keduanya bukan anggota $B$</sub>
- B. $1$  
  <sub>Salah: $f(2) = 1$ berada di $B$ tetapi $f(-1) = -2$ tidak di $B$</sub>
- **C. $4$** ✅  
  <sub>Benar: $p = 4$: $f(-1) = -5$, $f(0) = -1$, $f(2) = 7$, semuanya di $B$.</sub>
- D. $2$  
  <sub>Salah: $f(2) = 3$ berada di $B$ tetapi $f(-1) = -3$ tidak di $B$</sub>

**Pembahasan:** Syarat: $f(-1) = -p - 1$, $f(0) = -1$, dan $f(2) = 2p - 1$ semuanya anggota $B$. $-p - 1 \in B$ dengan $p > 0$ hanya terpenuhi $p = 4$ (nilai $-5$). Cek $f(2) = 7 \in B$.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas8-b04-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: daerah asal dari daerah hasil*

Fungsi $f$ ditentukan oleh $f(x) = -2x + 5$ dengan $x$ bilangan real. Jika daerah hasil $f$ adalah $\{f(x) \mid -3 < f(x) \le 9\}$, maka daerah asal $f$ adalah ....

- A. $\{x \mid -\frac{9}{2} \le x < \frac{3}{2},\ x \in R\}$  
  <sub>Salah: lupa mengurangi 5 sehingga langsung membagi $-3$ dan $9$ dengan $-2$</sub>
- **B. $\{x \mid -2 \le x < 4,\ x \in R\}$** ✅  
  <sub>Benar: $-3 < -2x + 5 \le 9$ dikurangi 5: $-8 < -2x \le 4$; dibagi $-2$ (arah dibalik): $-2 \le x < 4$.</sub>
- C. $\{x \mid -7 \le x < -1,\ x \in R\}$  
  <sub>Salah: menambah 5 (bukan mengurangi) pada ketiga ruas</sub>
- D. $\{x \mid -2 < x \le 4,\ x \in R\}$  
  <sub>Salah: membagi $-2$ tanpa membalik jenis batas termasuk atau tidak</sub>

**Pembahasan:** Dari $-3 < -2x + 5 \le 9$: $-8 < -2x \le 4$. Bagi $-2$ dan balik arah: $4 > x \ge -2$, yaitu $-2 \le x < 4$. Cek: $f(-2) = 9$ (termasuk), $f(4) = -3$ (tidak termasuk).
**Acuan:** siswa — siswa hal.203

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas8-b04-b-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: temukan kesalahan menentukan daerah hasil*

Seorang siswa menentukan daerah hasil $f(x) = x^2 - 2x$ dengan daerah asal $A = \{-1, 0, 1, 2, 3\}$.

| Langkah | Pekerjaan siswa |
|---|---|
| 1 | $f(-1) = (-1)^2 - 2(-1) = 1 - 2 = -1$ |
| 2 | $f(0) = 0 - 0 = 0$ |
| 3 | $f(1) = 1 - 2 = -1$ |
| 4 | $f(2) = 4 - 4 = 0$ |
| 5 | $f(3) = 9 - 6 = 3$ |
| 6 | Daerah hasil $= \{-1, 0, 3\}$ |

Pernyataan yang benar tentang pekerjaan siswa tersebut adalah ....

- A. Langkah 1 salah sehingga daerah hasil yang benar adalah $\{0, 3\}$  
  <sub>Salah: menghapus $-1$ padahal $f(1) = -1$ tetap menghasilkan $-1$</sub>
- B. Langkah 5 salah karena $f(3)$ seharusnya bernilai $15$, bukan $3$  
  <sub>Salah: mengira kesalahan ada pada langkah 5; $9 - 6 = 3$ sudah benar</sub>
- C. Semua langkah dan hasil akhir siswa benar karena nilai fungsinya cocok  
  <sub>Salah: tidak menghitung ulang; $-2(-1) = +2$, bukan $-2$</sub>
- **D. Langkah 1 salah karena seharusnya $f(-1) = 3$, tetapi daerah hasil akhirnya kebetulan tetap benar** ✅  
  <sub>Benar: $f(-1) = 1 + 2 = 3$; nilai lain benar, sehingga daerah hasil sebenarnya $\{3, 0, -1, 0, 3\} = \{-1, 0, 3\}$.</sub>

**Pembahasan:** Nilai yang benar: $f(-1) = 1 + 2 = 3$, $f(0) = 0$, $f(1) = -1$, $f(2) = 0$, $f(3) = 3$. Daerah hasil $\{-1, 0, 3\}$, sama dengan hasil siswa, tetapi langkah 1 siswa salah tanda.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas8-b04-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan menyelesaikan persamaan nilai fungsi*

Diketahui $f(x) = -4x + 7$ dan $f(a) = -9$. Penyelesaian seorang siswa:

| Langkah | Pekerjaan siswa |
|---|---|
| 1 | $-4a + 7 = -9$ |
| 2 | $-4a = -9 + 7$ |
| 3 | $-4a = -2$ |
| 4 | $a = \frac{1}{2}$ |

Pernyataan yang benar tentang pekerjaan siswa tersebut adalah ....

- A. Kesalahan pada langkah 2, nilai $a$ yang benar adalah $-4$  
  <sub>Salah: salah tanda pada hasil akhir; $f(-4) = 16 + 7 = 23$, bukan $-9$</sub>
- **B. Kesalahan pertama pada langkah 2 karena 7 dipindah ruas tanpa mengubah tanda; nilai $a$ yang benar adalah $4$** ✅  
  <sub>Benar: $-4a = -9 - 7 = -16$, sehingga $a = 4$; cek $f(4) = -16 + 7 = -9$.</sub>
- C. Tidak ada kesalahan, nilai $a$ adalah $\frac{1}{2}$  
  <sub>Salah: tidak memeriksa kembali; $f(\frac{1}{2}) = -2 + 7 = 5$, bukan $-9$</sub>
- D. Kesalahan pada langkah 4, nilai $a$ yang benar adalah $4$  
  <sub>Salah: langkah 4 konsisten dengan langkah 3 ($-2 : (-4) = \frac{1}{2}$); yang keliru adalah langkah 2</sub>

**Pembahasan:** Memindahkan $+7$ ke ruas kanan menjadi $-7$: $-4a = -9 - 7 = -16$, $a = 4$. Langkah 2 siswa salah, langkah selanjutnya mengikuti kesalahan itu.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas8-b04-b-hard-bt01-009
*orisinal | C6 | 3 langkah | jenis: rancang rumus fungsi dari daerah hasil*

Fungsi linear $f : A \to R$ dengan $A = \{-2, 0, 2, 4\}$ harus memenuhi $f(-2) = 9$ dan daerah hasil tepat $\{-3, 1, 5, 9\}$. Rumus fungsi yang memenuhi kedua syarat adalah ....

- A. $f(x) = -4x + 1$  
  <sub>Salah: memenuhi $f(-2) = 9$ tetapi $f(2) = -7$ tidak ada di daerah hasil</sub>
- B. $f(x) = -x + 7$  
  <sub>Salah: memenuhi $f(-2) = 9$ tetapi $f(0) = 7$ tidak ada di daerah hasil</sub>
- **C. $f(x) = -2x + 5$** ✅  
  <sub>Benar: $f(-2) = 9$, $f(0) = 5$, $f(2) = 1$, $f(4) = -3$; daerah hasil $\{9, 5, 1, -3\}$.</sub>
- D. $f(x) = 2x + 13$  
  <sub>Salah: memenuhi $f(-2) = 9$ tetapi $f(0) = 13$ tidak ada di daerah hasil</sub>

**Pembahasan:** Nilai terbesar 9 harus di $x = -2$ dan nilai terkecil $-3$ di $x = 4$, sehingga $a = \frac{-3 - 9}{4 - (-2)} = -2$ dan $b = 9 - (-2)(-2) = 5$. Jadi $f(x) = -2x + 5$.
**Acuan:** siswa — siswa hal.202

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas8-b04-b-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: banyak fungsi dengan syarat pasangan*

Diketahui $A = \{1, 2, 3, 4\}$ dan $B = \{a, b, c\}$. Banyak fungsi dari $A$ ke $B$ yang memenuhi $f(1) \ne f(2)$ adalah ....

- **A. $54$** ✅  
  <sub>Benar: $f(1)$ punya 3 pilihan, $f(2)$ punya 2 pilihan, $f(3)$ dan $f(4)$ masing-masing 3 pilihan: $3 \times 2 \times 3 \times 3 = 54$.</sub>
- B. $27$  
  <sub>Salah: menghitung fungsi dengan $f(1) = f(2)$ ($3 \times 1 \times 3 \times 3$), bukan yang berbeda</sub>
- C. $24$  
  <sub>Salah: menerapkan syarat "berbeda" ke semua anggota ($3 \times 2 \times 2 \times 2$)</sub>
- D. $81$  
  <sub>Salah: mengabaikan syarat $f(1) \ne f(2)$ sehingga $3^4$</sub>

**Pembahasan:** Tanpa syarat ada $3^4 = 81$ fungsi. Yang memenuhi $f(1) = f(2)$ ada $3 \times 1 \times 3 \times 3 = 27$, sisanya $81 - 27 = 54$.
**Acuan:** siswa — siswa hal.194

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas8-b04-b-hard-bt01-011
*orisinal | C6 | 5 langkah | jenis: banyak fungsi dengan daerah hasil tertentu*

Diketahui $A = \{1, 2, 3\}$ dan $B = \{a, b, c\}$. Banyak fungsi dari $A$ ke $B$ yang daerah hasilnya tepat beranggota 2 adalah ....

- **A. $18$** ✅  
  <sub>Benar: Pilih 2 anggota $B$ ada 3 cara; fungsi ke dua anggota itu ada $2^3 = 8$, dikurangi 2 fungsi konstan: $3 \times 6 = 18$.</sub>
- B. $24$  
  <sub>Salah: tidak mengurangi dua fungsi konstan ($3 \times 2^3$)</sub>
- C. $9$  
  <sub>Salah: menghitung $3 \times 3$ tanpa dasar pemilihan pasangan</sub>
- D. $8$  
  <sub>Salah: hanya menghitung fungsi ke satu pasangan anggota $B$ tertentu, lupa memilih pasangan anggota</sub>

**Pembahasan:** Total fungsi $3^3 = 27$: 3 fungsi konstan (hasil 1 anggota), 6 fungsi dengan hasil 3 anggota (bijektif, $3!$), sisanya $27 - 3 - 6 = 18$ daerah hasil tepat 2 anggota.
**Acuan:** siswa — siswa hal.194

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas8-b04-b-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: membandingkan dua fungsi tarif*

Taksi A menetapkan tarif $A(x) = 5.000 + 3.000x$ rupiah dan taksi B menetapkan tarif $B(x) = 12.000 + 2.000x$ rupiah untuk jarak $x$ kilometer. Pernyataan yang benar adalah ....

- A. Untuk jarak 5 km, kedua taksi menetapkan tarif yang sama  
  <sub>Salah: tarif sama di 7 km, bukan 5 km ($A(5) = 20.000$, $B(5) = 22.000$)</sub>
- **B. Untuk jarak 4 km, tarif taksi A lebih murah daripada taksi B** ✅  
  <sub>Benar: $A(4) = 17.000$ dan $B(4) = 20.000$, sehingga A lebih murah.</sub>
- C. Taksi B selalu lebih murah daripada taksi A  
  <sub>Salah: hanya melihat tarif per kilometer yang lebih kecil dan mengabaikan tarif awal</sub>
- D. Untuk jarak 10 km, tarif taksi A lebih murah daripada taksi B  
  <sub>Salah: $A(10) = 35.000$ lebih mahal dari $B(10) = 32.000$; titik impas ada di 7 km</sub>

**Pembahasan:** Impas: $5.000 + 3.000x = 12.000 + 2.000x$, $x = 7$. Untuk $x < 7$ taksi A lebih murah, untuk $x > 7$ taksi B lebih murah.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas8-b04-b-hard-bt01-013
*orisinal | C6 | 3 langkah | jenis: rancang fungsi tarif dari titik impas*

Taksi A menetapkan tarif $A(x) = 6.000 + 4.000x$ rupiah untuk jarak $x$ kilometer. Taksi D menetapkan tarif awal Rp2.000,00. Agar tarif taksi D sama dengan tarif taksi A pada jarak 10 km, tarif taksi D per kilometer harus ....

- A. Rp4.600,00  
  <sub>Salah: lupa mengurangi tarif awal ($46.000 : 10$)</sub>
- B. Rp4.000,00  
  <sub>Salah: mengira tarif per kilometer harus sama dengan taksi A</sub>
- **C. Rp4.400,00** ✅  
  <sub>Benar: $A(10) = 46.000$; $2.000 + 10k = 46.000$, $k = 4.400$.</sub>
- D. Rp4.800,00  
  <sub>Salah: menambah tarif awal bukan mengurangi ($48.000 : 10$)</sub>

**Pembahasan:** Tarif A pada 10 km: $6.000 + 40.000 = 46.000$. Untuk D: $2.000 + 10k = 46.000$, sehingga $10k = 44.000$, $k = 4.400$.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas8-b04-b-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: contoh penyangkal klaim nilai fungsi*

Dina berpendapat bahwa untuk fungsi $f(x) = x^2 - 6x$, jika $f(a) = f(b)$ maka pasti $a = b$. Pasangan $(a, b)$ yang dapat dipakai sebagai contoh penyangkal pendapat Dina adalah ....

- **A. $(1, 5)$** ✅  
  <sub>Benar: $f(1) = 1 - 6 = -5$ dan $f(5) = 25 - 30 = -5$, nilai sama padahal $1 \ne 5$.</sub>
- B. $(-1, 1)$  
  <sub>Salah: $f(-1) = 7$ dan $f(1) = -5$, nilainya berbeda</sub>
- C. $(2, 5)$  
  <sub>Salah: $f(2) = -8$ dan $f(5) = -5$, nilainya berbeda</sub>
- D. $(0, 3)$  
  <sub>Salah: $f(0) = 0$ dan $f(3) = -9$, nilainya berbeda</sub>

**Pembahasan:** Contoh penyangkal harus memiliki $a \ne b$ tetapi $f(a) = f(b)$. Hanya $(1, 5)$ yang memenuhi: keduanya bernilai $-5$.
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas8-b04-b-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: rancang rumus fungsi dari batas daerah hasil*

Fungsi linear $f(x) = ax + b$ memetakan daerah asal $\{x \mid 1 \le x < 5,\ x \in R\}$ tepat ke daerah hasil $\{f(x) \mid 2 < f(x) \le 10\}$. Rumus fungsi $f$ adalah ....

- A. $f(x) = -2x + 10$  
  <sub>Salah: daerah hasilnya $\{0 < f(x) \le 8\}$, memakai $b = 10$ yang salah</sub>
- B. $f(x) = -2x + 14$  
  <sub>Salah: daerah hasilnya $\{4 < f(x) \le 12\}$, memakai $b = 14$ yang salah</sub>
- C. $f(x) = 2x$  
  <sub>Salah: gradien positif memberi daerah hasil $\{2 \le f(x) < 10\}$, jenis batas tidak cocok</sub>
- **D. $f(x) = -2x + 12$** ✅  
  <sub>Benar: Batas bawah $x = 1$ termasuk tetapi nilai terbesar 10 juga termasuk, jadi $a < 0$: $f(1) = 10$ dan $f(5) = 2$, sehingga $a = -2$, $b = 12$.</sub>

**Pembahasan:** $x = 1$ termasuk dan $f(1)$ harus 10 (termasuk), $x = 5$ tidak termasuk dan $f(5) = 2$ (tidak termasuk), sehingga gradien negatif. $a + b = 10$ dan $5a + b = 2$ memberi $a = -2$, $b = 12$.
**Acuan:** siswa — siswa hal.203

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
