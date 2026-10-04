# Lembar koreksi — kelas10 SMA10-B2 subbab A: Barisan

57 soal | easy 20, medium 20, hard 17 | variasi 22, orisinal 35
> **Kapasitas kurang (hard): 17 dari kuota 20** — Acuan siswa subbab A (p53-p66) nyaris habis di easy/medium dan materi hanya barisan aritmetika dan geometri (rumus Un, beda, rasio); 17 soal hard orisinal yang berbeda penalaran (klaim, penyangkal, syarat jumlah/hasil kali, rancang, banding) sudah layak; tambahan akan nyaris kembar dengan medium.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b02-a-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: suku ke-n aritmetika*

Tentukan suku ke-40 dari barisan berikut: 11, 18, 25, 32, ….

- A. 277  
  <sub>Salah: memakai $n-2$ kali beda</sub>
- **B. 284** ✅  
  <sub>Benar: beda $b = 7$, $U_{40} = 11 + 39 \times 7 = 284$</sub>
- C. 291  
  <sub>Salah: memakai $n$ bukan $n-1$: $11 + 40 	imes 7$</sub>
- D. 280  
  <sub>Salah: mengalikan beda dengan $n$ tanpa menambah suku pertama</sub>

**Pembahasan:** Barisan aritmetika dengan $a = 11$ dan $b = 18 - 11 = 7$. $U_n = a + (n-1)b$ sehingga $U_{40} = 11 + 39 \times 7 = 284$.
**Acuan:** pretest — kelas10-b02-p0059-latihan-2-1-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b02-a-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: suku ke-n aritmetika*

Pak Budi menata batu bata untuk membuat tangga. Anak tangga pertama memakai 6 batu bata, anak tangga kedua 9 batu bata, anak tangga ketiga 12 batu bata, dan seterusnya dengan pola yang sama hingga anak tangga ke-12. Berapa batu bata yang dipakai pada anak tangga ke-12?

- A. 42  
  <sub>Salah: memakai $n$ bukan $n-1$: $6 + 12 	imes 3$</sub>
- B. 72  
  <sub>Salah: mengalikan suku pertama dengan banyak anak tangga</sub>
- C. 36  
  <sub>Salah: berhenti pada anak tangga ke-11 (kurang satu suku)</sub>
- **D. 39** ✅  
  <sub>Benar: $a = 6$, $b = 3$, $U_{12} = 6 + 11 \times 3 = 39$</sub>

**Pembahasan:** Pola aritmetika dengan $a = 6$ dan $b = 3$. $U_{12} = 6 + (12-1) \times 3 = 39$.
**Acuan:** pretest — kelas10-b02-p0060-latihan-2-1-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b02-a-easy-bt01-003
*variasi (konteks) | C2 | 2 langkah | jenis: suku ke-n aritmetika*

Air dalam sebuah kolam dikuras. Pada menit pertama keluar 50 liter, menit kedua 46 liter, menit ketiga 42 liter, dan seterusnya dengan pola yang sama. Berapa liter air yang keluar pada menit ke-10?

- A. 18  
  <sub>Salah: memakai $n-2$ kali beda</sub>
- B. 86  
  <sub>Salah: lupa tanda negatif pada beda</sub>
- **C. 14** ✅  
  <sub>Benar: $a = 50$, $b = -4$, $U_{10} = 50 + 9 \times (-4) = 14$</sub>
- D. 10  
  <sub>Salah: memakai $n$ bukan $n-1$: $50 - 10 	imes 4$</sub>

**Pembahasan:** Beda $b = 46 - 50 = -4$. $U_{10} = 50 + 9 \times (-4) = 14$ liter.
**Acuan:** pretest — kelas10-b02-p0060-latihan-2-1-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b02-a-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: beda dan suku pertama dari dua suku*

Diketahui suatu barisan aritmetika, suku ke-2 = 11 dan suku ke-5 = 26. Tentukan beda barisan tersebut.

- A. 15  
  <sub>Salah: tidak membagi selisih suku dengan selisih nomor suku</sub>
- **B. 5** ✅  
  <sub>Benar: $U_5 - U_2 = 3b = 15$, sehingga $b = 5$</sub>
- C. 3  
  <sub>Salah: memakai selisih nomor suku sebagai beda</sub>
- D. 7,5  
  <sub>Salah: membagi selisih suku dengan 2, bukan dengan 3</sub>

**Pembahasan:** $U_5 - U_2 = (a + 4b) - (a + b) = 3b$. Jadi $3b = 26 - 11 = 15$ dan $b = 5$.
**Acuan:** siswa — siswa hal.57 Contoh 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b02-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: beda dan suku pertama dari dua suku*

Diketahui suatu barisan aritmetika, suku ke-4 = 31 dan suku ke-7 = 55. Tentukan suku pertama barisan tersebut.

- A. 39  
  <sub>Salah: menambah, bukan mengurangi, tiga kali beda</sub>
- B. -1  
  <sub>Salah: mengurangkan $4b$ (memakai $n$ bukan $n-1$)</sub>
- **C. 7** ✅  
  <sub>Benar: $b = (55-31)/3 = 8$, $a = 31 - 3 \times 8 = 7$</sub>
- D. 23  
  <sub>Salah: hanya mundur satu suku (suku ke-3), bukan sampai suku pertama</sub>

**Pembahasan:** $3b = 55 - 31 = 24$ sehingga $b = 8$. $U_4 = a + 3b = 31$ memberi $a = 31 - 24 = 7$.
**Acuan:** siswa — siswa hal.57 Contoh 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b02-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: beda dan suku pertama dari dua suku*

Tika menyimpan uang di celengan dengan kenaikan nominal yang ditabung antarbulan tetap. Pada bulan ke-4 ia menabung Rp46.000 dan pada bulan ke-10 ia menabung Rp100.000. Berapa rupiah kenaikan nominal tabungan antarbulan tersebut?

- A. Rp10.000  
  <sub>Salah: membagi nominal bulan ke-10 dengan 10</sub>
- B. Rp54.000  
  <sub>Salah: tidak membagi selisih nominal dengan selisih bulan</sub>
- C. Rp11.500  
  <sub>Salah: membagi nominal bulan ke-4 dengan 4</sub>
- **D. Rp9.000** ✅  
  <sub>Benar: $6b = 100.000 - 46.000 = 54.000$, sehingga $b = 9.000$</sub>

**Pembahasan:** $U_{10} - U_4 = 6b$. Jadi $b = 54.000 / 6 = 9.000$.
**Acuan:** siswa — siswa hal.57 Contoh 2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b02-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: rasio dan suku geometri dari data*

Suku pertama dari suatu barisan geometri adalah 3 dan suku ke-5 adalah 48. Jika rasio barisan bernilai positif, tentukan rasio dari barisan tersebut.

- A. 4  
  <sub>Salah: membagi 16 dengan 4 (pangkat) alih-alih menarik akar</sub>
- B. 12  
  <sub>Salah: membagi 48 dengan $n - 1 = 4$</sub>
- C. 16  
  <sub>Salah: berhenti pada $r^4 = 16$ dan menganggapnya rasio</sub>
- **D. 2** ✅  
  <sub>Benar: $3r^4 = 48$, $r^4 = 16$, $r = 2$</sub>

**Pembahasan:** $U_5 = ar^4$ sehingga $48 = 3r^4$, $r^4 = 16$. Karena rasio positif, $r = 2$.
**Acuan:** siswa — siswa hal.63 Contoh 3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b02-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: rasio dan suku geometri dari data*

Suku pertama dari suatu barisan geometri adalah 2 dan suku ke-4 adalah 250. Tentukan rasio dari barisan tersebut.

- **A. 5** ✅  
  <sub>Benar: $2r^3 = 250$, $r^3 = 125$, $r = 5$</sub>
- B. 125  
  <sub>Salah: berhenti pada $r^3 = 125$ dan menganggapnya rasio</sub>
- C. 248  
  <sub>Salah: mengurangkan suku pertama dari suku keempat</sub>
- D. 62,5  
  <sub>Salah: membagi 250 dengan 4 (nomor suku)</sub>

**Pembahasan:** $U_4 = ar^3$ sehingga $250 = 2r^3$, $r^3 = 125$ dan $r = 5$.
**Acuan:** siswa — siswa hal.63 Contoh 3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b02-a-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: rasio dan suku geometri dari data*

Sebatang pita dibagi menjadi 5 bagian dengan panjang membentuk suatu barisan geometri. Jika pita yang paling pendek adalah 8 cm dan pita yang paling panjang adalah 128 cm, maka tentukan panjang pita pada potongan ketiga.

- A. 64 cm  
  <sub>Salah: menghitung potongan keempat, bukan ketiga</sub>
- B. 16 cm  
  <sub>Salah: menghitung potongan kedua, bukan ketiga</sub>
- C. 68 cm  
  <sub>Salah: memakai rata-rata panjang terpendek dan terpanjang (barisan aritmetika)</sub>
- **D. 32 cm** ✅  
  <sub>Benar: $8r^4 = 128$, $r = 2$, $U_3 = 8 \times 2^2 = 32$</sub>

**Pembahasan:** $r^4 = 128/8 = 16$ sehingga $r = 2$. $U_3 = 8 \times 2^2 = 32$ cm.
**Acuan:** siswa — siswa hal.64 Contoh 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b02-a-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: rasio dan suku geometri dari data*

Seutas kawat dibagi menjadi 4 bagian dengan panjang membentuk suatu barisan geometri. Jika kawat yang paling pendek adalah 2 cm dan kawat yang paling panjang adalah 54 cm, maka tentukan panjang kawat pada potongan kedua.

- A. 27 cm  
  <sub>Salah: membagi panjang terpanjang dengan 2</sub>
- **B. 6 cm** ✅  
  <sub>Benar: $2r^3 = 54$, $r = 3$, $U_2 = 2 \times 3 = 6$</sub>
- C. 18 cm  
  <sub>Salah: menghitung potongan ketiga, bukan kedua</sub>
- D. 28 cm  
  <sub>Salah: memakai rata-rata panjang terpendek dan terpanjang</sub>

**Pembahasan:** $r^3 = 54/2 = 27$ sehingga $r = 3$. $U_2 = 2 \times 3 = 6$ cm.
**Acuan:** siswa — siswa hal.64 Contoh 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b02-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: suku ke-n geometri*

Tentukan suku ke-7 dari barisan 4, 12, 36, 108, ….

- A. 972  
  <sub>Salah: memakai $r^{n-2}$: $4 	imes 3^5$</sub>
- **B. 2.916** ✅  
  <sub>Benar: $r = 3$, $U_7 = 4 \times 3^6 = 2.916$</sub>
- C. 8.748  
  <sub>Salah: memakai $r^n$ bukan $r^{n-1}$: $4 	imes 3^7$</sub>
- D. 52  
  <sub>Salah: menganggap barisan aritmetika dengan beda 8</sub>

**Pembahasan:** Rasio $r = 12/4 = 3$. $U_7 = ar^{6} = 4 \times 729 = 2.916$.
**Acuan:** siswa — siswa hal.65 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b02-a-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: suku ke-n geometri*

Raka mengirim sebuah pesan kepada 4 orang temannya pada hari pertama. Keesokan harinya, setiap penerima mengirim pesan itu kepada 4 orang lain yang belum menerimanya, dan begitu seterusnya setiap hari. Berapa orang yang menerima pesan pada hari kelima?

- A. 256  
  <sub>Salah: memakai pangkat 4 (hari ke-4) alih-alih hari kelima</sub>
- B. 20  
  <sub>Salah: mengalikan 4 dengan 5 (dianggap pola aritmetika)</sub>
- **C. 1.024** ✅  
  <sub>Benar: $a = 4$, $r = 4$, $U_5 = 4 \times 4^4 = 4^5 = 1.024$</sub>
- D. 1.364  
  <sub>Salah: menjumlahkan semua penerima dari hari pertama sampai kelima</sub>

**Pembahasan:** Banyak penerima tiap hari dikali 4: 4, 16, 64, 256, 1.024. Hari kelima: 1.024 orang.
**Acuan:** siswa — siswa hal.65 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b02-a-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: mengenali jenis barisan*

Barisan bilangan berikut yang merupakan barisan aritmetika adalah ….

- A. $1, 2, 4, 7, \dots$  
  <sub>Salah: selisih 1, 2, 3 tidak tetap</sub>
- B. $2, 4, 8, 16, \dots$  
  <sub>Salah: perbandingan tetap 2 (barisan geometri), bukan selisih tetap</sub>
- **C. $3, 7, 11, 15, \dots$** ✅  
  <sub>Benar: selisih dua suku berurutan selalu 4</sub>
- D. $1, 4, 9, 16, \dots$  
  <sub>Salah: selisih 3, 5, 7 tidak tetap</sub>

**Pembahasan:** Barisan aritmetika memiliki beda tetap. Hanya $3, 7, 11, 15$ yang selisihnya selalu 4.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b02-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: mengenali jenis barisan*

Barisan bilangan berikut yang merupakan barisan geometri adalah ….

- A. $1, 3, 6, 10, \dots$  
  <sub>Salah: selisih bertambah 2, 3, 4 dan rasio tidak tetap</sub>
- **B. $5, 10, 20, 40, \dots$** ✅  
  <sub>Benar: perbandingan dua suku berurutan selalu 2</sub>
- C. $6, 9, 12, 15, \dots$  
  <sub>Salah: selisih tetap 3 (barisan aritmetika), bukan rasio tetap</sub>
- D. $2, 4, 6, 12, \dots$  
  <sub>Salah: rasio 2, 1,5, 2 tidak tetap</sub>

**Pembahasan:** Barisan geometri memiliki rasio tetap. Hanya $5, 10, 20, 40$ yang rasionya selalu 2.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b02-a-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: menentukan beda atau rasio*

Beda dari barisan aritmetika $17, 12, 7, 2, \dots$ adalah ….

- A. $-10$  
  <sub>Salah: selisih dua suku berselang tanpa dibagi 2</sub>
- B. $-15$  
  <sub>Salah: selisih suku pertama dan keempat tanpa dibagi 3</sub>
- C. $5$  
  <sub>Salah: mengurangkan suku pertama dari suku kedua dengan urutan terbalik</sub>
- **D. $-5$** ✅  
  <sub>Benar: $b = U_2 - U_1 = 12 - 17 = -5$</sub>

**Pembahasan:** Beda adalah selisih suku berurutan: $b = U_2 - U_1 = 12 - 17 = -5$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b02-a-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: menentukan beda atau rasio*

Rasio dari barisan geometri $96, 48, 24, 12, \dots$ adalah ….

- **A. $\frac{1}{2}$** ✅  
  <sub>Benar: $r = \frac{48}{96} = \frac{1}{2}$</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: membagi suku ketiga dengan suku pertama (melompati satu suku)</sub>
- C. $2$  
  <sub>Salah: membagi suku pertama dengan suku kedua (terbalik)</sub>
- D. $-48$  
  <sub>Salah: mengurangkan suku kedua dengan suku pertama (memakai beda)</sub>

**Pembahasan:** Rasio adalah perbandingan suku berurutan: $r = \frac{48}{96} = \frac{1}{2}$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b02-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: melanjutkan barisan*

Dua suku berikutnya dari barisan $3, 10, 17, 24, \dots$ berturut-turut adalah ….

- **A. $31$ dan $38$** ✅  
  <sub>Benar: beda 7, sehingga $24+7 = 31$ dan $31+7 = 38$</sub>
- B. $48$ dan $96$  
  <sub>Salah: menganggap barisan geometri dengan rasio 2</sub>
- C. $32$ dan $40$  
  <sub>Salah: menganggap selisih membesar 8 dan 8</sub>
- D. $34$ dan $44$  
  <sub>Salah: menambah 10 (suku kedua), bukan beda 7</sub>

**Pembahasan:** Beda $b = 10 - 3 = 7$. Dua suku berikutnya: $24 + 7 = 31$ dan $31 + 7 = 38$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b02-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: melanjutkan barisan*

Dua suku berikutnya dari barisan geometri $2, -6, 18, -54, \dots$ berturut-turut adalah ….

- A. $-162$ dan $486$  
  <sub>Salah: tanda bergantian dimulai dari tanda yang salah</sub>
- B. $-62$ dan $-70$  
  <sub>Salah: menganggap barisan aritmetika dengan beda $-8$</sub>
- **C. $162$ dan $-486$** ✅  
  <sub>Benar: rasio $-3$, sehingga $-54 \times (-3) = 162$ dan $162 \times (-3) = -486$</sub>
- D. $162$ dan $486$  
  <sub>Salah: tanda negatif pada rasio hanya dipakai satu kali</sub>

**Pembahasan:** Rasio $r = \frac{-6}{2} = -3$. Suku berikutnya $-54 \times (-3) = 162$, lalu $162 \times (-3) = -486$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b02-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: menentukan banyak suku atau nomor suku*

Sebuah meja segi empat dilengkapi empat kursi. Jika dua meja disatukan terdapat 6 kursi, tiga meja disatukan terdapat 8 kursi, dan seterusnya bertambah dua kursi untuk setiap meja tambahan. Berapa banyak meja yang harus disatukan agar tepat tersedia 26 kursi?

- **A. 12** ✅  
  <sub>Benar: $4 + (n-1) \times 2 = 26$, sehingga $n - 1 = 11$ dan $n = 12$</sub>
- B. 10  
  <sub>Salah: menghitung dari kursi pada dua meja (6), bukan satu meja</sub>
- C. 11  
  <sub>Salah: lupa menambah 1 setelah memperoleh $n - 1 = 11$</sub>
- D. 13  
  <sub>Salah: membagi 26 dengan 2 tanpa memperhitungkan suku pertama</sub>

**Pembahasan:** $U_n = 4 + (n-1) \times 2 = 26$ sehingga $(n-1) \times 2 = 22$, $n - 1 = 11$, $n = 12$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b02-a-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: mengingat rumus*

Rumus suku ke-$n$ pada barisan geometri dengan suku pertama $a$ dan rasio $r$ adalah ….

- **A. $U_n = ar^{n-1}$** ✅  
  <sub>Benar: suku pertama dikalikan rasio sebanyak $n-1$ kali</sub>
- B. $U_n = a + (n-1)r$  
  <sub>Salah: memakai bentuk rumus barisan aritmetika</sub>
- C. $U_n = a^{n-1}r$  
  <sub>Salah: pangkat dipasang pada suku pertama, bukan pada rasio</sub>
- D. $U_n = ar^{n}$  
  <sub>Salah: pangkat rasio memakai $n$, bukan $n-1$</sub>

**Pembahasan:** Suku ke-$n$ diperoleh dari $a$ dikalikan $r$ sebanyak $(n-1)$ kali: $U_n = ar^{n-1}$.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b02-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: dua suku tak berurutan aritmetika*

Diketahui suatu barisan aritmetika, suku ke-4 = 17 dan suku ke-9 = -8. Tentukan suku ke-20 dari barisan tersebut.

- A. $-68$  
  <sub>Salah: memakai $n$ bukan $n-1$: $32 + 20 \times (-5)$</sub>
- **B. $-63$** ✅  
  <sub>Benar: $5b = -8 - 17 = -25$ sehingga $b = -5$, $a = 32$, $U_{20} = 32 + 19 \times (-5) = -63$</sub>
- C. $-58$  
  <sub>Salah: memakai $n-2$ kali beda: $32 + 18 \times (-5)$</sub>
- D. $63$  
  <sub>Salah: lupa tanda negatif pada beda</sub>

**Pembahasan:** $U_9 - U_4 = 5b = -25$ sehingga $b = -5$. $U_4 = a + 3b = 17$ memberi $a = 32$. Maka $U_{20} = 32 + 19 \times (-5) = -63$.
**Acuan:** siswa — siswa hal.57 Contoh 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b02-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: rumus suku ke-n dari dua suku*

Diketahui suatu barisan aritmetika, suku ke-5 = 22 dan suku ke-12 = 57. Tentukan rumus suku ke-$n$ dari barisan tersebut.

- **A. $U_n = 5n - 3$** ✅  
  <sub>Benar: $7b = 35$, $b = 5$, $a = 22 - 4 \times 5 = 2$, $U_n = 2 + (n-1) \times 5 = 5n - 3$</sub>
- B. $U_n = 2n + 5$  
  <sub>Salah: tertukar antara suku pertama dan beda</sub>
- C. $U_n = 5n + 17$  
  <sub>Salah: menganggap $22$ sebagai suku pertama: $22 + (n-1) \times 5$</sub>
- D. $U_n = 5n + 2$  
  <sub>Salah: menulis $U_n = a + nb$ (memakai $n$ bukan $n-1$)</sub>

**Pembahasan:** $U_{12} - U_5 = 7b = 35$ sehingga $b = 5$. $a = 22 - 4 \times 5 = 2$. $U_n = 2 + (n-1) \times 5 = 5n - 3$.
**Acuan:** siswa — siswa hal.57 Contoh 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b02-a-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: mencari nomor suku aritmetika*

Dewi menyimpan uang di celengan dengan selisih kenaikan nominal yang ditabung antarbulan tetap. Pada bulan ke-3 ia menabung Rp38.000,00 dan pada bulan ke-8 ia menabung Rp63.000,00. Pada bulan ke berapa Dewi menabung sebesar Rp118.000,00?

- **A. bulan ke-19** ✅  
  <sub>Benar: $b = 25.000/5 = 5.000$, $a = 28.000$; $28.000 + (n-1) \times 5.000 = 118.000$ sehingga $n = 19$</sub>
- B. bulan ke-11  
  <sub>Salah: hanya menghitung selisih dari bulan ke-8 tanpa menambahkan 8</sub>
- C. bulan ke-17  
  <sub>Salah: memakai tabungan bulan ke-3 sebagai suku pertama</sub>
- D. bulan ke-18  
  <sub>Salah: lupa menambah 1 setelah memperoleh $n - 1 = 18$</sub>

**Pembahasan:** $5b = 63.000 - 38.000$ sehingga $b = 5.000$ dan $a = 38.000 - 2 \times 5.000 = 28.000$. Dari $28.000 + (n-1) \times 5.000 = 118.000$ diperoleh $n - 1 = 18$ dan $n = 19$.
**Acuan:** siswa — siswa hal.57 Contoh 2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b02-a-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: dua suku tak berurutan aritmetika*

Jika diketahui barisan aritmetika dengan suku ke-6 = 9,5 dan suku ke-14 = 21,5. Tentukan suku ke-30 dari barisan tersebut.

- A. 44  
  <sub>Salah: memakai $n-2$ kali beda</sub>
- **B. 45,5** ✅  
  <sub>Benar: $8b = 12$, $b = 1,5$, $a = 9,5 - 5 \times 1,5 = 2$, $U_{30} = 2 + 29 \times 1,5 = 45,5$</sub>
- C. 47  
  <sub>Salah: memakai $n$ bukan $n-1$: $2 + 30 \times 1,5$</sub>
- D. 43,5  
  <sub>Salah: lupa menambahkan suku pertama</sub>

**Pembahasan:** $U_{14} - U_6 = 8b = 12$ sehingga $b = 1,5$. $a = 9,5 - 5 \times 1,5 = 2$. $U_{30} = 2 + 29 \times 1,5 = 45,5$.
**Acuan:** siswa — siswa hal.59 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b02-a-medium-bt01-005
*variasi (konteks) | C4 | 3 langkah | jenis: suku terakhir bernilai positif*

Kak Dani membagikan stiker kepada anak-anak dengan pola tertentu. Anak pertama mendapat 47 stiker, anak kedua mendapat 43 stiker, anak ketiga mendapat 39 stiker, dan seterusnya dengan pola yang sama. Berapa stiker yang diterima anak terakhir yang masih mendapat sedikitnya satu stiker?

- A. -1  
  <sub>Salah: tidak memperhatikan bahwa banyak stiker tidak boleh negatif (anak ke-13)</sub>
- B. 7  
  <sub>Salah: berhenti pada anak ke-11 (kurang satu anak)</sub>
- C. 12  
  <sub>Salah: menjawab nomor anak, bukan banyak stiker</sub>
- **D. 3** ✅  
  <sub>Benar: $47 - 4(n-1) \geq 1$ memberi $n \leq 12{,}5$ sehingga $n = 12$ dan $U_{12} = 47 - 44 = 3$</sub>

**Pembahasan:** $U_n = 47 + (n-1)(-4) = 51 - 4n$. Syarat $U_n \geq 1$ memberi $n \leq 12{,}5$, jadi $n = 12$ dan $U_{12} = 51 - 48 = 3$.
**Acuan:** siswa — siswa hal.60 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b02-a-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: model cerita aritmetika dengan nilai awal*

Setiap hari Sabtu, Bu Rina menyumbangkan lima belas buku bacaan ke sebuah taman baca yang sebelumnya sudah memiliki 40 buku dari donatur lain. Setelah penyumbangan pertama, pengurus mencatat jumlah buku yang ada: 55, 70, 85, dan seterusnya. Berapa jumlah buku yang tercatat setelah Sabtu ke-24?

- A. 360  
  <sub>Salah: mengabaikan 40 buku awal: $24 \times 15$</sub>
- B. 385  
  <sub>Salah: menjumlahkan 23 kali penyumbangan dengan buku awal (kurang satu minggu)</sub>
- **C. 400** ✅  
  <sub>Benar: $a = 55$, $b = 15$, $U_{24} = 55 + 23 \times 15 = 400$</sub>
- D. 415  
  <sub>Salah: memakai $n$ bukan $n-1$: $55 + 24 \times 15$</sub>

**Pembahasan:** Catatan membentuk barisan aritmetika dengan $a = 55$ dan $b = 15$. $U_{24} = 55 + 23 \times 15 = 400$ buku.
**Acuan:** siswa — siswa hal.60 Latihan 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b02-a-medium-bt01-007
*variasi (angka) | C4 | 4 langkah | jenis: suku pertama geometri dari dua suku*

Jika diketahui barisan geometri dengan suku ke-3 = 36 dan suku ke-5 = 4 serta rasio bernilai positif. Tentukan suku pertama dari barisan geometri tersebut.

- A. 972  
  <sub>Salah: mundur tiga kali (memakai $r^3$ bukan $r^2$)</sub>
- B. 108  
  <sub>Salah: mundur hanya satu suku dari suku ke-3</sub>
- C. 12  
  <sub>Salah: mengalikan suku ke-3 dengan rasio, bukan membagi</sub>
- **D. 324** ✅  
  <sub>Benar: $r^2 = 4/36 = 1/9$, $r = 1/3$, $a = 36 : r^2 = 324$</sub>

**Pembahasan:** $U_5 : U_3 = r^2 = \frac{4}{36} = \frac{1}{9}$, rasio positif sehingga $r = \frac{1}{3}$. $U_3 = ar^2$ memberi $a = 36 \times 9 = 324$.
**Acuan:** siswa — siswa hal.65 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b02-a-medium-bt01-008
*variasi (konteks) | C4 | 3 langkah | jenis: mencari nomor suku geometri*

Seorang siswa mengirimkan sebuah pengumuman kepada 5 orang temannya pada hari pertama. Keesokan harinya, setiap penerima mengirimkan pengumuman itu kepada 5 orang lain yang belum pernah menerimanya, dan demikian seterusnya setiap hari. Pada hari keberapa banyak orang yang menerima pengumuman pada hari itu tepat 3.125 orang?

- A. hari ke-4  
  <sub>Salah: memakai $U_n = 5 \times 5^n$ sehingga $n + 1 = 5$</sub>
- **B. hari ke-5** ✅  
  <sub>Benar: $U_n = 5 \times 5^{n-1} = 5^n = 3.125 = 5^5$ sehingga $n = 5$</sub>
- C. hari ke-6  
  <sub>Salah: memakai $U_n = 5^{n-1}$ sehingga $n - 1 = 5$</sub>
- D. hari ke-625  
  <sub>Salah: membagi 3.125 dengan 5 lalu menganggap hasilnya nomor hari</sub>

**Pembahasan:** $a = 5$ dan $r = 5$ sehingga $U_n = 5^n$. Karena $5^5 = 3.125$, maka $n = 5$.
**Acuan:** siswa — siswa hal.65 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b02-a-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: rasio negatif geometri*

Suku pertama dari suatu barisan geometri adalah 5 dan suku ke-4 adalah -40. Tentukan suku ke-6 dari barisan tersebut.

- A. $80$  
  <sub>Salah: menghitung suku ke-5, bukan suku ke-6</sub>
- **B. $-160$** ✅  
  <sub>Benar: $5r^3 = -40$, $r = -2$, $U_6 = 5 \times (-2)^5 = -160$</sub>
- C. $160$  
  <sub>Salah: lupa bahwa pangkat ganjil dari rasio negatif bernilai negatif</sub>
- D. $320$  
  <sub>Salah: memakai $r^{n}$ bukan $r^{n-1}$ dan tanda hilang</sub>

**Pembahasan:** $U_4 = ar^3$ sehingga $r^3 = -8$ dan $r = -2$. $U_6 = 5 \times (-2)^5 = -160$.
**Acuan:** siswa — siswa hal.63 Contoh 3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b02-a-medium-bt01-010
*variasi (angka) | C3 | 4 langkah | jenis: geometri dari suku pertama dan terakhir*

Sebatang kayu dibagi menjadi 6 bagian dengan ukuran panjang membentuk suatu barisan geometri. Jika kayu yang paling pendek adalah 6 cm dan kayu yang paling panjang adalah 192 cm, maka tentukan selisih panjang potongan kelima dan potongan ketiga.

- A. 120 cm  
  <sub>Salah: menjumlahkan, bukan mengurangkan, panjang kedua potongan</sub>
- B. 90 cm  
  <sub>Salah: mengurangkan potongan terpendek dari potongan kelima</sub>
- C. 24 cm  
  <sub>Salah: hanya menghitung panjang potongan ketiga</sub>
- **D. 72 cm** ✅  
  <sub>Benar: $6r^5 = 192$, $r = 2$, $U_5 = 96$, $U_3 = 24$, selisih $72$</sub>

**Pembahasan:** $r^5 = 192/6 = 32$ sehingga $r = 2$. $U_5 = 6 \times 2^4 = 96$ dan $U_3 = 6 \times 2^2 = 24$. Selisih $96 - 24 = 72$ cm.
**Acuan:** siswa — siswa hal.64 Contoh 4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b02-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: suku tengah aritmetika*

Pada barisan aritmetika diketahui suku ke-3 sama dengan 17 dan suku ke-11 sama dengan 49. Nilai suku ke-7 adalah ….

- A. 66  
  <sub>Salah: menjumlahkan kedua suku yang diketahui</sub>
- B. 29  
  <sub>Salah: memakai $n-1$ terlalu kecil: menambah hanya 3 kali beda dari $U_3$</sub>
- **C. 33** ✅  
  <sub>Benar: $8b = 49 - 17 = 32$, $b = 4$, $U_7 = 17 + 4 \times 4 = 33$</sub>
- D. 37  
  <sub>Salah: menambah 5 kali beda dari $U_3$ (suku ke-8)</sub>

**Pembahasan:** $U_{11} - U_3 = 8b = 32$, jadi $b = 4$. $U_7 = U_3 + 4b = 17 + 16 = 33$ (rata-rata $U_3$ dan $U_{11}$).
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b02-a-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: suku antara dari ujung barisan*

Sebuah barisan aritmetika terdiri atas 9 suku. Suku pertamanya 7 dan suku terakhirnya 47. Nilai suku ke-6 dari barisan tersebut adalah ….

- A. 27  
  <sub>Salah: memakai $n-2$ kali beda</sub>
- B. 37  
  <sub>Salah: memakai $n$ bukan $n-1$: $7 + 6 \times 5$</sub>
- C. 42  
  <sub>Salah: mundur satu beda dari suku terakhir (suku ke-8)</sub>
- **D. 32** ✅  
  <sub>Benar: $47 = 7 + 8b$, $b = 5$, $U_6 = 7 + 5 \times 5 = 32$</sub>

**Pembahasan:** Suku terakhir $U_9 = 7 + 8b = 47$ sehingga $b = 5$. $U_6 = 7 + 5 \times 5 = 32$.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b02-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: nilai dari rumus U_n kuadrat*

Suatu barisan memiliki rumus suku ke-$n$ yaitu $U_n = 2n^2 - 3n$. Nilai $U_8 - U_5$ adalah ….

- **A. 69** ✅  
  <sub>Benar: $U_8 = 128 - 24 = 104$, $U_5 = 50 - 15 = 35$, selisih $69$</sub>
- B. 104  
  <sub>Salah: hanya menghitung $U_8$</sub>
- C. 9  
  <sub>Salah: mengira $U_8 - U_5 = U_3$</sub>
- D. 139  
  <sub>Salah: menjumlahkan $U_8$ dan $U_5$</sub>

**Pembahasan:** $U_8 = 2(64) - 24 = 104$ dan $U_5 = 2(25) - 15 = 35$. Selisihnya $104 - 35 = 69$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b02-a-medium-bt01-014
*orisinal | C4 | 4 langkah | jenis: nomor suku dari rumus U_n kuadrat*

Suatu barisan memiliki rumus suku ke-$n$ yaitu $U_n = n^2 + 2n - 3$. Suku ke berapa yang bernilai 165?

- A. suku ke-55  
  <sub>Salah: membagi 165 dengan 3</sub>
- B. suku ke-83  
  <sub>Salah: membagi 165 dengan 2 lalu membulatkan</sub>
- **C. suku ke-12** ✅  
  <sub>Benar: $n^2 + 2n - 168 = 0$, $(n+14)(n-12) = 0$, $n = 12$ (nomor suku positif)</sub>
- D. suku ke-14  
  <sub>Salah: mengambil faktor $n + 14$ sebagai $n = 14$ tanpa melihat tanda</sub>

**Pembahasan:** $n^2 + 2n - 3 = 165$ menjadi $n^2 + 2n - 168 = 0$, $(n+14)(n-12) = 0$. Nomor suku positif sehingga $n = 12$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b02-a-medium-bt01-015
*orisinal | C4 | 2 langkah | jenis: mengenali barisan aritmetika dari rumus*

Rumus suku ke-$n$ berikut yang menghasilkan barisan aritmetika adalah ….

- A. $U_n = \frac{n}{n+1}$  
  <sub>Salah: selisih suku berurutan $\frac{1}{(n+1)(n+2)}$ tidak tetap</sub>
- B. $U_n = n^2 + 3$  
  <sub>Salah: selisih $2n + 1$ berubah-ubah</sub>
- **C. $U_n = 4n - 7$** ✅  
  <sub>Benar: $U_{n+1} - U_n = 4$ untuk setiap $n$ (tetap)</sub>
- D. $U_n = 3 \times 2^{n}$  
  <sub>Salah: rasio tetap 2 (barisan geometri), selisihnya tidak tetap</sub>

**Pembahasan:** Barisan aritmetika memiliki beda tetap. Untuk $U_n = 4n - 7$: $U_{n+1} - U_n = 4$. Rumus lain memberi selisih yang bergantung pada $n$ atau rasio tetap.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b02-a-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: suku geometri rasio pecahan negatif*

Pada barisan geometri $81, -27, 9, -3, \dots$ suku ke-8 adalah ….

- A. $\frac{1}{9}$  
  <sub>Salah: memakai $n-2$ sebagai pangkat rasio</sub>
- **B. $-\frac{1}{27}$** ✅  
  <sub>Benar: $r = \frac{-27}{81} = -\frac{1}{3}$, $U_8 = 81 \times (-\frac{1}{3})^7 = -\frac{1}{27}$</sub>
- C. $\frac{1}{81}$  
  <sub>Salah: memakai $n$ sebagai pangkat rasio</sub>
- D. $\frac{1}{27}$  
  <sub>Salah: tanda negatif hilang pada pangkat ganjil</sub>

**Pembahasan:** $r = -\frac{1}{3}$. $U_8 = 81 \times (-\frac{1}{3})^7 = 3^4 \times \frac{-1}{3^7} = -\frac{1}{27}$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b02-a-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: cerita penurunan geometri*

Sebuah bola dijatuhkan dari ketinggian 256 cm. Setiap kali memantul, bola mencapai ketinggian $\frac{3}{4}$ dari ketinggian sebelumnya. Tinggi pantulan ke-4 adalah ….

- **A. 81 cm** ✅  
  <sub>Benar: pantulan pertama $192$, $r = \frac{3}{4}$, $U_4 = 192 \times (\frac{3}{4})^3 = 81$</sub>
- B. 108 cm  
  <sub>Salah: menghitung pantulan ke-3</sub>
- C. 64 cm  
  <sub>Salah: memakai $1 - \frac{3}{4}$ sebagai rasio sekali saja ($256 \times \frac{1}{4}$)</sub>
- D. 60,75 cm  
  <sub>Salah: memakai pantulan pertama sebagai suku pertama lalu pangkat 4 (kelebihan satu kali)</sub>

**Pembahasan:** Pantulan ke-1 = $256 \times \frac{3}{4} = 192$. Barisan pantulan geometri dengan $a = 192$ dan $r = \frac{3}{4}$: $U_4 = 192 \times \frac{27}{64} = 81$ cm.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b02-a-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: parameter barisan aritmetika*

Tiga bilangan $x + 1$, $2x + 3$, dan $4x - 3$ membentuk barisan aritmetika dalam urutan tersebut. Beda barisan tersebut adalah ….

- A. 8  
  <sub>Salah: menjawab nilai $x$, bukan beda</sub>
- B. 19  
  <sub>Salah: menjawab suku tengah</sub>
- C. 6  
  <sub>Salah: salah tanda: menghitung $x - 2$ sebagai beda</sub>
- **D. 10** ✅  
  <sub>Benar: $(2x+3) - (x+1) = (4x-3) - (2x+3)$ memberi $x + 2 = 2x - 6$, $x = 8$, bilangannya $9, 19, 29$, beda $10$</sub>

**Pembahasan:** Beda tetap: $x + 2 = 2x - 6$ sehingga $x = 8$. Barisannya $9, 19, 29$ dengan beda $10$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b02-a-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: parameter barisan geometri*

Tiga bilangan positif $k$, $k + 6$, dan $4k$ membentuk barisan geometri dalam urutan tersebut. Nilai $k$ adalah ….

- A. 24  
  <sub>Salah: menjawab suku ketiga</sub>
- B. 12  
  <sub>Salah: menjawab suku tengah</sub>
- **C. 6** ✅  
  <sub>Benar: $\frac{k+6}{k} = \frac{4k}{k+6}$ memberi $(k+6)^2 = 4k^2$, $k + 6 = 2k$ (positif), $k = 6$</sub>
- D. 2  
  <sub>Salah: menyamakan $k + 6 = 4k$</sub>

**Pembahasan:** Rasio sama: $(k+6)^2 = k \times 4k = 4k^2$. Karena bilangan positif, $k + 6 = 2k$ sehingga $k = 6$ (barisan $6, 12, 24$).
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b02-a-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: membandingkan barisan aritmetika dan geometri*

Sebuah barisan aritmetika dan sebuah barisan geometri sama-sama memiliki suku pertama 2 dan suku kedua 6. Selisih suku ke-5 barisan geometri dan suku ke-5 barisan aritmetika adalah ….

- **A. 144** ✅  
  <sub>Benar: aritmetika $b = 4$, $U_5 = 18$; geometri $r = 3$, $U_5 = 2 \times 81 = 162$; selisih $144$</sub>
- B. 468  
  <sub>Salah: suku geometri memakai $r^5$ bukan $r^4$ ($486 - 18$)</sub>
- C. 18  
  <sub>Salah: hanya menghitung suku ke-5 aritmetika</sub>
- D. 162  
  <sub>Salah: hanya menghitung suku ke-5 geometri</sub>

**Pembahasan:** Aritmetika: $b = 4$, $U_5 = 2 + 4 \times 4 = 18$. Geometri: $r = 3$, $U_5 = 2 \times 3^4 = 162$. Selisih $162 - 18 = 144$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b02-a-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim beda tetap*

Seorang siswa menyatakan: "Jika selisih setiap dua suku berurutan pada empat suku pertama suatu barisan selalu sama, maka barisan itu pasti barisan aritmetika." Barisan manakah yang merupakan contoh penyangkal pernyataan tersebut? (Setiap barisan ditulis enam suku pertamanya.)

- A. $2, 4, 8, 16, 32, 64, \ldots$  
  <sub>Salah: barisan geometri; selisih empat suku pertamanya 2, 4, 8 sehingga syarat klaim tidak terpenuhi</sub>
- **B. $3, 6, 9, 12, 16, 20, \ldots$** ✅  
  <sub>Benar: empat suku pertama berselisih 3, tetapi selisih berikutnya 4 dan 4 sehingga selisihnya tidak tetap; syarat terpenuhi, kesimpulan gagal</sub>
- C. $3, 6, 9, 13, 17, 21, \ldots$  
  <sub>Salah: selisih empat suku pertama 3, 3, 4 sehingga syarat klaim tidak terpenuhi</sub>
- D. $3, 6, 9, 12, 15, 18, \ldots$  
  <sub>Salah: barisan aritmetika dengan beda 3; ini mendukung klaim, bukan menyangkalnya</sub>

**Pembahasan:** Contoh penyangkal harus memenuhi syarat klaim (empat suku pertama berselisih sama) tetapi bukan aritmetika. Hanya $3, 6, 9, 12, 16, 20$ yang demikian: selisihnya $3, 3, 3, 4, 4$. Barisan aritmetika menuntut selisih tetap untuk semua suku berurutan.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b02-a-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim rasio negatif*

Diketahui barisan geometri dengan suku pertama $-3$ dan rasio $-2$. Pernyataan yang benar tentang barisan tersebut adalah ....

- A. Barisan tersebut tidak monoton dan $U_7 = 192$  
  <sub>Salah: salah tanda: mengira $(-2)^6$ dikali $-3$ bernilai positif</sub>
- B. Barisan tersebut tidak monoton dan $U_7 = 384$  
  <sub>Salah: memakai pangkat $n$ bukan $n-1$: $-3 	imes (-2)^7$</sub>
- C. Barisan tersebut selalu turun karena rasionya negatif dan $U_7 = -192$  
  <sub>Salah: menganggap rasio negatif berarti barisan turun, padahal tanda suku bergantian</sub>
- **D. Barisan tersebut tidak monoton (tidak selalu naik dan tidak selalu turun) dan $U_7 = -192$** ✅  
  <sub>Benar: suku-sukunya $-3, 6, -12, 24, \ldots$ bergantian tanda; $U_7 = -3 \times (-2)^6 = -192$</sub>

**Pembahasan:** $U_1 = -3, U_2 = 6, U_3 = -12, U_4 = 24$: suku bergantian negatif dan positif sehingga tidak monoton. $U_7 = ar^{6} = -3 \times 64 = -192$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b02-a-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: dua kemungkinan rasio*

Pada suatu barisan geometri diketahui $U_2 = 6$ dan $U_6 = 96$. Tanda rasio barisan tidak diketahui. Selisih antara nilai terbesar dan nilai terkecil yang mungkin untuk $U_5$ adalah ....

- **A. $96$** ✅  
  <sub>Benar: $r^4 = 16$ sehingga $r = 2$ atau $r = -2$; $U_5 = U_2 r^3 = \pm 48$; selisihnya $48 - (-48) = 96$</sub>
- B. $192$  
  <sub>Salah: mengambil selisih memakai $U_6$ dan $-U_6$ (bukan $U_5$)</sub>
- C. $0$  
  <sub>Salah: menjumlahkan kedua kemungkinan $U_5$, bukan mencari selisihnya</sub>
- D. $48$  
  <sub>Salah: hanya memakai rasio positif sehingga mengira $U_5$ tunggal</sub>

**Pembahasan:** $U_6 / U_2 = r^4 = 16$ sehingga $r = \pm 2$. Untuk $r = 2$: $U_5 = 6 \times 8 = 48$; untuk $r = -2$: $U_5 = 6 \times (-8) = -48$. Selisih $= 96$.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b02-a-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: tiga bilangan aritmetika jumlah dan hasil kali*

Tiga bilangan positif membentuk barisan aritmetika naik. Jumlah ketiga bilangan itu 21 dan hasil kalinya 280. Selisih bilangan terbesar dan bilangan terkecil adalah ....

- A. $10$  
  <sub>Salah: mengambil bilangan terbesar sebagai jawaban</sub>
- B. $3$  
  <sub>Salah: mengambil beda $b$ sebagai selisih terbesar dan terkecil (padahal selisihnya $2b$)</sub>
- **C. $6$** ✅  
  <sub>Benar: bilangan $7-b, 7, 7+b$ dengan $7(49 - b^2) = 280$ sehingga $b = 3$ (beda positif); bilangannya 4, 7, 10 dan selisih $10 - 4 = 6$</sub>
- D. $4$  
  <sub>Salah: mengambil bilangan terkecil sebagai jawaban</sub>

**Pembahasan:** Misalkan bilangannya $7-b, 7, 7+b$ (jumlah 21 sehingga suku tengah 7). Hasil kali: $7(49-b^2)=280$ sehingga $b^2 = 9$ dan $b = 3$ (naik). Bilangannya 4, 7, 10; selisih terbesar dan terkecil $= 6$.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b02-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: tiga bilangan geometri jumlah dan hasil kali*

Tiga bilangan positif membentuk barisan geometri naik. Jumlah ketiga bilangan itu 26 dan hasil kalinya 216. Jumlah bilangan pertama dan bilangan ketiga adalah ....

- **A. $20$** ✅  
  <sub>Benar: suku tengah $6$ (karena $6^3 = 216$), $6/r + 6 + 6r = 26$ memberi $r = 3$; bilangannya 2, 6, 18 sehingga $2 + 18 = 20$</sub>
- B. $8$  
  <sub>Salah: memakai rasio $rac{1}{3}$ dan keliru menjumlahkan 2 dan 6</sub>
- C. $6$  
  <sub>Salah: mengambil suku tengah sebagai jawaban</sub>
- D. $18$  
  <sub>Salah: mengambil bilangan terbesar saja</sub>

**Pembahasan:** Misalkan $a/r, a, ar$ dengan $a^3 = 216$ sehingga $a = 6$. Dari $6/r + 6r = 20$ diperoleh $3r^2 - 10r + 3 = 0$ sehingga $r = 3$ atau $r = \tfrac{1}{3}$; naik berarti $r = 3$. Bilangannya 2, 6, 18, jumlah pertama dan ketiga 20.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b02-a-hard-bt01-006
*orisinal | C6 | 6 langkah | jenis: aritmetika menjadi geometri dengan syarat*

Tiga bilangan membentuk barisan aritmetika dengan beda positif dan jumlah 24. Jika bilangan ketiga ditambah 4, ketiga bilangan itu membentuk barisan geometri. Bilangan terbesar pada barisan aritmetika semula adalah ....

- A. $16$  
  <sub>Salah: mengambil bilangan ketiga setelah ditambah 4</sub>
- B. $4$  
  <sub>Salah: mengambil bilangan terkecil sebagai jawaban</sub>
- **C. $12$** ✅  
  <sub>Benar: bilangan $8-b, 8, 8+b$; $(8-b)(12+b) = 64$ memberi $b^2 + 4b - 32 = 0$ sehingga $b = 4$ (positif); bilangan terbesar $8 + 4 = 12$</sub>
- D. $8$  
  <sub>Salah: mengambil suku tengah sebagai jawaban</sub>

**Pembahasan:** Suku tengah 8 karena jumlah 24. Barisan geometri: $8^2 = (8-b)(8+b+4)$, yaitu $64 = 96 - 4b - b^2$ sehingga $b^2 + 4b - 32 = 0$, $(b+8)(b-4)=0$. Beda positif $b = 4$: bilangan 4, 8, 12; bilangan terbesar 12.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b02-a-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: rekursi kali dua dengan hasil kali suku*

Suatu barisan memenuhi $U_{n+1} = 2U_n$ untuk setiap $n \geq 1$, semua sukunya positif, dan $U_3 \times U_5 = 1.024$. Nilai $U_8$ adalah ....

- A. $256$  
  <sub>Salah: memakai $U_7$ (pangkat 6 bukan 7)</sub>
- B. $128$  
  <sub>Salah: memakai $U_6$ (pangkat 5 bukan 7)</sub>
- **C. $512$** ✅  
  <sub>Benar: $r=2$; $U_3 U_5 = 64a^2 = 1.024$ sehingga $a = 4$; $U_8 = 4 \times 2^7 = 512$</sub>
- D. $1.024$  
  <sub>Salah: memakai $U_9$ (pangkat 8 bukan 7)</sub>

**Pembahasan:** Dari $U_{n+1}=2U_n$ diperoleh barisan geometri dengan $r = 2$. $U_3 U_5 = a \cdot 2^2 \cdot a \cdot 2^4 = 64a^2 = 1.024$ sehingga $a^2 = 16$, $a = 4$ (positif). $U_8 = 4 \times 2^7 = 512$.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b02-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: rekursi beda tetap dengan jumlah suku simetris*

Suatu barisan memenuhi $U_{n+1} = U_n - 3$ untuk setiap $n \geq 1$ dan $U_3 + U_7 = 34$. Nilai $U_{15}$ adalah ....

- A. $-10$  
  <sub>Salah: memakai $n-2$ kali beda: $29 - 13 	imes 3$</sub>
- **B. $-13$** ✅  
  <sub>Benar: $b = -3$; $U_3 + U_7 = 2U_5 = 34$ sehingga $U_5 = 17$, $a = 29$; $U_{15} = 29 + 14 \times (-3) = -13$</sub>
- C. $13$  
  <sub>Salah: salah tanda pada hasil akhir</sub>
- D. $-16$  
  <sub>Salah: memakai $n$ bukan $n-1$: $29 - 15 	imes 3$</sub>

**Pembahasan:** Beda $b = -3$. $U_3 = a + 2b$ dan $U_7 = a + 6b$ sehingga $U_3 + U_7 = 2a + 8b = 2U_5 = 34$, $U_5 = 17$. Maka $a = 17 + 12 = 29$ dan $U_{15} = 29 + 14(-3) = -13$.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b02-a-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: kapan barisan geometri melampaui aritmetika*

Barisan $P$ adalah barisan aritmetika dengan suku pertama 50 dan beda 8. Barisan $Q$ adalah barisan geometri dengan suku pertama 5 dan rasio 2. Nomor suku terkecil $n$ sehingga $Q_n > P_n$ adalah ....

- A. $4$  
  <sub>Salah: memakai $Q_n = 5 	imes 2^n$ (pangkat $n$ bukan $n-1$): $Q_4 = 80 > P_4 = 74$</sub>
- B. $5$  
  <sub>Salah: memakai $n-2$ pada barisan aritmetika ($P_5 = 74$) sehingga mengira $Q_5 > P_5$</sub>
- C. $7$  
  <sub>Salah: menambah satu nomor suku setelah $Q_6 > P_6$ padahal sudah terpenuhi</sub>
- **D. $6$** ✅  
  <sub>Benar: $P_5 = 82 > Q_5 = 80$, tetapi $Q_6 = 160 > P_6 = 90$</sub>

**Pembahasan:** $P_n = 50 + 8(n-1)$ dan $Q_n = 5 \times 2^{n-1}$. Nilai $(P_n, Q_n)$: $(50,5), (58,10), (66,20), (74,40), (82,80), (90,160)$. Pertama kali $Q_n > P_n$ pada $n = 6$.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b02-a-hard-bt01-010
*orisinal | C6 | 4 langkah | jenis: merancang rasio dengan dua batas*

Barisan geometri memiliki suku pertama 2 dan rasio $r$ yang merupakan bilangan bulat positif. Barisan itu dirancang agar $U_2 < 10$ dan $U_3 > 30$. Nilai $r$ yang memenuhi adalah ....

- A. $5$  
  <sub>Salah: memenuhi $U_3 = 50 > 30$ tetapi $U_2 = 10$ tidak kurang dari 10 (batas tegas)</sub>
- B. $6$  
  <sub>Salah: memenuhi $U_3 = 72 > 30$ tetapi $U_2 = 12$ tidak kurang dari 10</sub>
- **C. $4$** ✅  
  <sub>Benar: $2r < 10$ memberi $r < 5$; $2r^2 > 30$ memberi $r^2 > 15$ sehingga $r \geq 4$; satu-satunya bilangan bulat adalah 4</sub>
- D. $3$  
  <sub>Salah: memenuhi $U_2 = 6 < 10$ tetapi $U_3 = 18$ tidak lebih dari 30</sub>

**Pembahasan:** $U_2 = 2r < 10$ memberi $r < 5$. $U_3 = 2r^2 > 30$ memberi $r^2 > 15$, jadi $r \geq 4$. Bilangan bulat positif yang memenuhi hanya $r = 4$ ($U_2 = 8$, $U_3 = 32$).
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b02-a-hard-bt01-011
*orisinal | C6 | 5 langkah | jenis: merancang beda dengan dua batas*

Barisan aritmetika memiliki suku pertama 7 dan beda $b$ bilangan bulat. Barisan itu dirancang agar $U_4 > 30$ dan $U_6 < 60$. Jumlah semua nilai $b$ yang mungkin adalah ....

- A. $19$  
  <sub>Salah: membuang $b = 8$ (mengira $b > 8$ karena $rac{23}{3} pprox 7{,}67$ dibulatkan ke 8 lalu dibuat tegas)</sub>
- B. $38$  
  <sub>Salah: ikut menyertakan $b = 11$ padahal $U_6 = 62$ tidak kurang dari 60</sub>
- C. $34$  
  <sub>Salah: ikut menyertakan $b = 7$ padahal $U_4 = 28$ tidak lebih dari 30</sub>
- **D. $27$** ✅  
  <sub>Benar: $7 + 3b > 30$ memberi $b \geq 8$; $7 + 5b < 60$ memberi $b \leq 10$; nilai $b$: 8, 9, 10 dan jumlahnya 27</sub>

**Pembahasan:** $U_4 = 7 + 3b > 30$ memberi $b > 7{,}67$ sehingga $b \geq 8$. $U_6 = 7 + 5b < 60$ memberi $b < 10{,}6$ sehingga $b \leq 10$. Nilai $b$: 8, 9, 10 dengan jumlah 27.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b02-a-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: mengenali rumus U_n yang menghasilkan barisan geometri*

Rumus suku ke-$n$ berikut yang menghasilkan barisan geometri untuk setiap $n$ adalah ....

- **A. $U_n = 3^n - 3^{n-1}$** ✅  
  <sub>Benar: $U_n = 3^{n-1}(3 - 1) = 2 \times 3^{n-1}$, sehingga rasio tetap $3$</sub>
- B. $U_n = 3^n + n$  
  <sub>Salah: suku-suku 4, 11, 30: rasio $rac{11}{4} 
eq rac{30}{11}$</sub>
- C. $U_n = 2^n + 2$  
  <sub>Salah: suku-suku 4, 6, 10: rasio $rac{6}{4} 
eq rac{10}{6}$</sub>
- D. $U_n = n \times 2^n$  
  <sub>Salah: suku-suku 2, 8, 24: rasio $4 
eq 3$</sub>

**Pembahasan:** $3^n - 3^{n-1} = 3^{n-1}(3-1) = 2 \times 3^{n-1}$ sehingga $U_n = 2 \times 3^{n-1}$ dan $U_{n+1}/U_n = 3$ untuk semua $n$. Tiga bentuk lain memiliki rasio berurutan yang tidak sama.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas10-b02-a-hard-bt01-013
*orisinal | C5 | 3 langkah | jenis: menemukan kesalahan menghitung suku geometri*

Seorang siswa mengerjakan: "Barisan $81, 27, 9, 3, \ldots$ memiliki $a = 81$ dan $r = \frac{1}{3}$, sehingga $U_8 = 81 \times \left(\frac{1}{3}\right)^8 = \frac{1}{81}$." Pernyataan yang benar tentang pengerjaan itu adalah ....

- A. Tidak ada kesalahan dan $U_8 = \frac{1}{81}$  
  <sub>Salah: kesalahan ada pada pangkat: seharusnya $n-1 = 7$</sub>
- **B. Pangkat seharusnya 7, sehingga $U_8 = \frac{1}{27}$** ✅  
  <sub>Benar: $U_n = ar^{n-1}$ sehingga $U_8 = 81 \times (\frac{1}{3})^7 = 3^{4-7} = \frac{1}{27}$</sub>
- C. Rasio seharusnya 3, sehingga $U_8 = 177.147$  
  <sub>Salah: rasio $rac{27}{81} = rac{1}{3}$; barisan turun sehingga rasio 3 keliru</sub>
- D. Barisan itu aritmetika dengan beda $-54$ sehingga $U_8 = -297$  
  <sub>Salah: selisih berurutan $-54, -18, -6$ tidak tetap sehingga bukan aritmetika</sub>

**Pembahasan:** Rumus $U_n = ar^{n-1}$ dengan $n = 8$ memberi pangkat $7$, bukan $8$. $U_8 = 81 \times 3^{-7} = 3^4 \times 3^{-7} = 3^{-3} = \frac{1}{27}$.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas10-b02-a-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: banyak suku genap dalam interval*

Pada barisan aritmetika $5, 12, 19, 26, \ldots$, banyak suku yang genap dan nilainya lebih dari 100 tetapi kurang dari 200 adalah ....

- **A. $7$** ✅  
  <sub>Benar: $U_n = 7n - 2$; $100 < 7n - 2 < 200$ memberi $15 \leq n \leq 28$; suku genap bila $n$ genap: $n = 16, 18, \ldots, 28$ sehingga ada 7</sub>
- B. $6$  
  <sub>Salah: melewatkan suku 194 ($n = 28$)</sub>
- C. $8$  
  <sub>Salah: ikut menghitung suku genap 208 ($n = 30$) yang lebih dari 200</sub>
- D. $14$  
  <sub>Salah: menghitung semua suku antara 100 dan 200 tanpa syarat genap</sub>

**Pembahasan:** $U_n = 5 + 7(n-1) = 7n - 2$. $7n - 2$ genap tepat saat $n$ genap. Dari $100 < 7n-2 < 200$ diperoleh $14{,}57 < n < 28{,}86$, yaitu $n = 15, \ldots, 28$. Bilangan genap di antaranya 16, 18, 20, 22, 24, 26, 28: 7 suku.
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas10-b02-a-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: hubungan antar suku lalu batas nilai*

Pada barisan aritmetika diketahui $U_5 = 2U_2$ dan $U_8 = 36$. Nomor suku pertama yang nilainya lebih dari 100 adalah suku ke-....

- A. $24$  
  <sub>Salah: suku ke-24 bernilai tepat 100, bukan lebih dari 100</sub>
- **B. $25$** ✅  
  <sub>Benar: $a = 2b$ dan $9b = 36$ sehingga $b = 4$, $a = 8$; $U_n = 4n + 4$; $U_{24} = 100$ belum lebih dari 100 sehingga $n = 25$</sub>
- C. $26$  
  <sub>Salah: menambah satu nomor setelah $n > 24$ sudah dipenuhi oleh 25</sub>
- D. $23$  
  <sub>Salah: memakai $n-2$ pada rumus suku dan bukan memeriksa batas tegas</sub>

**Pembahasan:** $a + 4b = 2(a + b)$ sehingga $a = 2b$. $U_8 = a + 7b = 9b = 36$ memberi $b = 4$ dan $a = 8$. $U_n = 8 + 4(n-1) = 4n + 4 > 100$ memberi $n > 24$; nomor suku terkecil 25 ($U_{25} = 104$).
**Acuan:** siswa — siswa hal.57

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas10-b02-a-hard-bt01-016
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim rasio kurang dari satu*

Diketahui barisan geometri dengan suku pertama $-80$ dan rasio $\frac{1}{2}$. Pernyataan yang benar tentang barisan tersebut adalah ....

- A. Suku ke-10 lebih kecil daripada suku ke-9  
  <sub>Salah: barisan naik: $U_9 = -rac{80}{256}$ dan $U_{10} = -rac{80}{512}$, sehingga $U_{10} > U_9$</sub>
- B. Barisan tersebut turun karena rasionya kurang dari 1  
  <sub>Salah: menganggap rasio kurang dari 1 selalu menurunkan barisan, padahal suku pertama negatif</sub>
- C. Ada suku yang bernilai positif karena rasionya positif  
  <sub>Salah: rasio positif dan suku pertama negatif membuat semua suku negatif</sub>
- **D. Barisan tersebut naik, yaitu $U_{n+1} > U_n$ untuk setiap $n$, walaupun rasionya kurang dari 1** ✅  
  <sub>Benar: $U_{n+1} - U_n = U_n(r-1) = -\frac{1}{2}U_n > 0$ karena $U_n < 0$; suku $-80, -40, -20, \ldots$ bertambah</sub>

**Pembahasan:** Suku-sukunya $-80, -40, -20, -10, \ldots$ semuanya negatif dan makin mendekati nol, jadi naik. Klaim "rasio kurang dari 1 berarti turun" hanya berlaku bila suku pertama positif.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas10-b02-a-hard-bt01-017
*orisinal | C6 | 6 langkah | jenis: merancang dua barisan berbagi suku*

Sebuah barisan aritmetika dan sebuah barisan geometri sama-sama memiliki suku pertama 4 dan suku kedua yang sama (suku kedua bukan 4). Suku ketiga barisan geometri lebih besar 4 daripada suku ketiga barisan aritmetika, dan rasio barisan geometri tidak nol. Selisih suku ke-6 barisan geometri dan suku ke-6 barisan aritmetika adalah ....

- **A. $104$** ✅  
  <sub>Benar: suku kedua $s$: $\frac{s^2}{4} - (2s - 4) = 4$ memberi $s = 8$; $b = 4$, $r = 2$; $U_6$ geometri $= 128$, $U_6$ aritmetika $= 24$, selisih 104</sub>
- B. $232$  
  <sub>Salah: memakai pangkat 6 pada geometri ($4 	imes 2^6 = 256$)</sub>
- C. $124$  
  <sub>Salah: mengurangkan suku pertama (4) saja sebagai suku ke-6 aritmetika</sub>
- D. $108$  
  <sub>Salah: memakai $n-2$ pada suku ke-6 aritmetika ($4 + 4 	imes 4 = 20$)</sub>

**Pembahasan:** Misalkan suku kedua $s$. Aritmetika: $b = s - 4$, $U_3 = 2s - 4$. Geometri: $r = s/4$, $U_3 = s^2/4$. Syarat: $\frac{s^2}{4} - 2s + 4 = 4$ sehingga $s(s - 8) = 0$; $s = 8$ ($s = 0$ membuat rasio nol). Maka $b = 4$, $r = 2$: $U_6 = 4 + 5 \times 4 = 24$ (aritmetika) dan $4 \times 2^5 = 128$ (geometri). Selisih 104.
**Acuan:** siswa — siswa hal.63

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
