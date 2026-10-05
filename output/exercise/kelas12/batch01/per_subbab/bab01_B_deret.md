# Lembar koreksi — kelas12 SMA12U-B1 subbab B: Deret

60 soal | easy 20, medium 20, hard 20 | variasi 22, orisinal 38

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12-b01-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: suku ke-n dan jumlah n suku aritmetika*

Suatu deret aritmetika memiliki suku pertama 7 dan beda 5. Tentukan suku ke-12 dan jumlah 12 suku pertama.

- A. $U_{12} = 62$ dan $S_{12} = 372$  
  <sub>Salah: menghitung $S_{12} = \frac{12}{2} \times U_{12}$ tanpa menambahkan suku pertama</sub>
- **B. $U_{12} = 62$ dan $S_{12} = 414$** ✅  
  <sub>Benar: $U_{12} = 7 + 11 \times 5 = 62$ dan $S_{12} = \frac{12}{2}(7 + 62) = 414$</sub>
- C. $U_{12} = 67$ dan $S_{12} = 444$  
  <sub>Salah: memakai $U_n = a + nb$ (n bukan n-1) sehingga $U_{12}$ dan $S_{12}$ ikut salah</sub>
- D. $U_{12} = 55$ dan $S_{12} = 372$  
  <sub>Salah: lupa menambahkan suku pertama pada $U_{12}$ (hanya $(n-1)b = 55$)</sub>

**Pembahasan:** Dengan $a = 7$, $b = 5$, $n = 12$: $U_{12} = 7 + 11 \times 5 = 62$. $S_{12} = \frac{12}{2}(7 + 62) = 6 \times 69 = 414$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12-b01-b-easy-bt01-002
*variasi (konteks) | C2 | 2 langkah | jenis: suku ke-n dan jumlah n suku aritmetika*

Sebuah toko kue menjual 5 kotak pada hari pertama, dan penjualan bertambah 6 kotak setiap hari. Tentukan penjualan hari ke-9 dan jumlah penjualan selama 9 hari pertama.

- A. $U_9 = 48$ dan $S_9 = 238$  
  <sub>Salah: lupa menambah suku pertama pada $U_9$ dan menghitung $S_9$ dengan pembulatan</sub>
- **B. $U_9 = 53$ dan $S_9 = 261$** ✅  
  <sub>Benar: $U_9 = 5 + 8 \times 6 = 53$ dan $S_9 = \frac{9}{2}(5 + 53) = 261$</sub>
- C. $U_9 = 59$ dan $S_9 = 288$  
  <sub>Salah: memakai $U_n = a + nb$ sehingga $U_9 = 59$ dan jumlahnya ikut salah</sub>
- D. $U_9 = 53$ dan $S_9 = 477$  
  <sub>Salah: mengira $S_9 = 9 \times U_9$</sub>

**Pembahasan:** $a = 5$, $b = 6$, $n = 9$. $U_9 = 5 + 8 \times 6 = 53$. $S_9 = \frac{9}{2}(5 + 53) = \frac{9 \times 58}{2} = 261$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12-b01-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: tumpukan menurun (banyak suku lalu jumlah)*

Seorang petani menata buah jeruk dalam tumpukan berbentuk segitiga. Tumpukan paling bawah berisi 62 jeruk, di atasnya 58 jeruk, kemudian 54 jeruk, dan seterusnya hingga tumpukan terakhir hanya berisi 6 jeruk. Hitunglah total jeruk yang ditumpuk.

- **A. 510** ✅  
  <sub>Benar: banyak tumpukan $n = \frac{62 - 6}{4} + 1 = 15$, jumlah $= \frac{15}{2}(62 + 6) = 510$</sub>
- B. 1.020  
  <sub>Salah: lupa membagi 2 pada rumus $S_n = \frac{n}{2}(a + U_n)$</sub>
- C. 544  
  <sub>Salah: salah menghitung banyak tumpukan (memakai n = 16, bukan 15)</sub>
- D. 476  
  <sub>Salah: salah menghitung banyak tumpukan (memakai n = 14, bukan 15)</sub>

**Pembahasan:** Beda $-4$, banyak tumpukan $62 - 4(n-1) = 6 \Rightarrow n = 15$. $S_{15} = \frac{15}{2}(62 + 6) = 510$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12-b01-b-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: tumpukan menurun (banyak suku lalu jumlah)*

Seorang tukang menyusun batako berbentuk tangga. Lapisan paling bawah berisi 33 batako, di atasnya 30 batako, kemudian 27 batako, dan seterusnya hingga lapisan teratas hanya berisi 3 batako. Banyak seluruh batako yang disusun adalah ....

- A. 180  
  <sub>Salah: salah menghitung banyak lapisan (memakai n = 10, bukan 11)</sub>
- B. 216  
  <sub>Salah: salah menghitung banyak lapisan (memakai n = 12, bukan 11)</sub>
- **C. 198** ✅  
  <sub>Benar: banyak lapisan $n = \frac{33 - 3}{3} + 1 = 11$, jumlah $= \frac{11}{2}(33 + 3) = 198$</sub>
- D. 396  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>

**Pembahasan:** Beda $-3$, $33 - 3(n-1) = 3 \Rightarrow n = 11$. $S_{11} = \frac{11}{2}(33 + 3) = 198$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12-b01-b-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: jumlah n suku pertama deret geometri*

Suatu deret geometri memiliki suku pertama $a = 3$ dan rasio $r = 4$. Hitunglah jumlah 4 suku pertama deret tersebut.

- A. 256  
  <sub>Salah: lupa mengurangi 1 pada $r^n - 1$ (memakai $4^4 = 256$)</sub>
- B. 63  
  <sub>Salah: memakai $n = 3$ (salah menghitung banyak suku)</sub>
- C. 765  
  <sub>Salah: lupa membagi dengan $(r - 1)$</sub>
- **D. 255** ✅  
  <sub>Benar: $S_4 = \frac{3(4^4 - 1)}{4 - 1} = \frac{3 \times 255}{3} = 255$</sub>

**Pembahasan:** $S_4 = \frac{a(r^4 - 1)}{r - 1} = \frac{3(256 - 1)}{3} = 255$.
**Acuan:** pretest — kelas12-b01-p0047-latihan-1-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12-b01-b-easy-bt01-006
*variasi (konteks) | C2 | 1 langkah | jenis: jumlah n suku pertama deret geometri*

Sebuah kabar tersebar dengan pola: pada hari pertama 7 orang mengetahuinya, dan setiap hari banyak orang yang baru mengetahuinya menjadi 3 kali lipat hari sebelumnya. Jumlah orang yang mengetahui kabar itu selama 4 hari pertama adalah ....

- A. 847  
  <sub>Salah: memakai $n = 5$ (hari berlebih)</sub>
- B. 91  
  <sub>Salah: memakai $n = 3$ (hanya 3 hari)</sub>
- **C. 280** ✅  
  <sub>Benar: deret geometri $a = 7$, $r = 3$, $n = 4$: $S_4 = \frac{7(3^4 - 1)}{3 - 1} = 280$</sub>
- D. 560  
  <sub>Salah: lupa membagi dengan $(r - 1)$</sub>

**Pembahasan:** $S_4 = \frac{7(81 - 1)}{3 - 1} = \frac{7 \times 80}{2} = 280$.
**Acuan:** pretest — kelas12-b01-p0047-latihan-1-4-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12-b01-b-easy-bt01-007
*orisinal | C1 | 1 langkah | jenis: definisi deret*

Pengertian deret bilangan yang tepat adalah ....

- A. banyaknya suku yang menyusun suatu barisan bilangan  
  <sub>Salah: mengira deret adalah banyak suku, bukan jumlah suku</sub>
- **B. jumlah suku-suku penyusun suatu barisan bilangan** ✅  
  <sub>Benar: deret diperoleh dengan menjumlahkan suku-suku barisan</sub>
- C. selisih antara dua suku yang berurutan pada suatu barisan  
  <sub>Salah: mencampuradukkan deret dengan beda barisan aritmetika</sub>
- D. susunan bilangan yang berurutan menurut suatu pola  
  <sub>Salah: mengira deret sama dengan barisan (hanya urutan, tanpa penjumlahan)</sub>

**Pembahasan:** Deret bilangan adalah jumlah suku-suku penyusun barisan bilangan, misalnya dari barisan 2, 4, 6 terbentuk deret $2 + 4 + 6$.
**Acuan:** siswa — siswa hal.37

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12-b01-b-easy-bt01-008
*orisinal | C2 | 1 langkah | jenis: mengenali jenis deret*

Deret berikut yang merupakan deret aritmetika adalah ....

- **A. $4 + 9 + 14 + 19 + \dots$** ✅  
  <sub>Benar: selisih antarsuku selalu 5 (beda tetap)</sub>
- B. $81 + 27 + 9 + 3 + \dots$  
  <sub>Salah: rasio tetap $\frac{1}{3}$, jadi deret geometri bukan aritmetika</sub>
- C. $1 + 4 + 9 + 16 + \dots$  
  <sub>Salah: selisih 3, 5, 7 tidak tetap (barisan kuadrat)</sub>
- D. $2 + 3 + 5 + 8 + \dots$  
  <sub>Salah: selisih antarsuku 1, 2, 3 tidak tetap</sub>

**Pembahasan:** Deret aritmetika memiliki beda tetap. Pada $4 + 9 + 14 + 19$: $9 - 4 = 14 - 9 = 19 - 14 = 5$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12-b01-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: jumlah n suku dari pola deret aritmetika*

Suatu deret aritmetika memiliki pola 8 + 13 + 18 + .... Berapa jumlah 20 suku pertama deret tersebut?

- A. 1.007  
  <sub>Salah: memakai $n = 19$ (salah menghitung banyak suku)</sub>
- **B. 1.110** ✅  
  <sub>Benar: $a = 8$, $b = 5$, $n = 20$: $S_{20} = \frac{20}{2}(2 \times 8 + 19 \times 5) = 1.110$</sub>
- C. 2.220  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- D. 1.160  
  <sub>Salah: memakai $(n \times b)$ bukan $(n-1)b$ pada rumus jumlah</sub>

**Pembahasan:** $b = 13 - 8 = 5$. $S_{20} = \frac{20}{2}(2 \times 8 + 19 \times 5) = 10 \times 111 = 1.110$.
**Acuan:** siswa — siswa hal.42 Contoh 1.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12-b01-b-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: jumlah n suku dari pola deret aritmetika*

Sebuah perpustakaan menerima sumbangan buku: bulan pertama 13 buku, bulan kedua 19 buku, bulan ketiga 25 buku, dan seterusnya dengan pertambahan tetap. Berapa jumlah buku yang diterima selama 14 bulan pertama?

- A. 1.456  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- B. 770  
  <sub>Salah: memakai $n \times b$ (bukan $(n-1)b$) pada rumus jumlah</sub>
- **C. 728** ✅  
  <sub>Benar: $a = 13$, $b = 6$: $S_{14} = \frac{14}{2}(2 \times 13 + 13 \times 6) = 728$</sub>
- D. 637  
  <sub>Salah: memakai $n = 13$ (salah menghitung banyak bulan)</sub>

**Pembahasan:** $b = 19 - 13 = 6$. $S_{14} = 7(26 + 78) = 7 \times 104 = 728$.
**Acuan:** siswa — siswa hal.42 Contoh 1.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12-b01-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: soal cerita deret aritmetika (kursi bertingkat)*

Tempat duduk di suatu gedung diatur mulai dari barisan depan ke belakang dengan banyak kursi di baris belakang 4 kursi lebih banyak dari baris di depannya. Jika dalam gedung tersebut terdapat 15 baris kursi dan baris terdepan ada 10 kursi, jumlah seluruh kursi dalam gedung tersebut ada ....

- A. 504  
  <sub>Salah: memakai $n = 14$ (salah menghitung banyak baris)</sub>
- B. 1.140  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- C. 600  
  <sub>Salah: memakai $n \times b$ (bukan $(n-1)b$) pada rumus jumlah</sub>
- **D. 570** ✅  
  <sub>Benar: $a = 10$, $b = 4$, $n = 15$: $S_{15} = \frac{15}{2}(20 + 14 \times 4) = 570$</sub>

**Pembahasan:** $S_{15} = \frac{15}{2}(2 \times 10 + 14 \times 4) = \frac{15}{2} \times 76 = 570$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12-b01-b-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: soal cerita deret aritmetika (kursi bertingkat)*

Pak Budi menanam pohon jati pada sebuah lahan. Baris pertama ditanami 6 pohon dan setiap baris berikutnya ditanami 5 pohon lebih banyak dari baris sebelumnya. Jika lahan itu memiliki 9 baris, banyak pohon jati seluruhnya adalah ....

- **A. 234** ✅  
  <sub>Benar: $a = 6$, $b = 5$, $n = 9$: $S_9 = \frac{9}{2}(12 + 8 \times 5) = 234$</sub>
- B. 207  
  <sub>Salah: menghitung $\frac{9 \times U_9}{2}$ tanpa menambahkan suku pertama ($U_9 = 46$)</sub>
- C. 188  
  <sub>Salah: memakai $n = 8$ (salah menghitung banyak baris)</sub>
- D. 468  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>

**Pembahasan:** $U_9 = 6 + 8 \times 5 = 46$. $S_9 = \frac{9}{2}(6 + 46) = 234$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12-b01-b-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: soal cerita deret aritmetika (hasil panen naik tetap)*

Seorang petani jeruk mencatat hasil panennya selama 9 hari pertama. Setiap harinya, hasil panen mengalami kenaikan tetap dimulai hari pertama, kedua, ketiga berturut-turut 20 kg, 24 kg, 28 kg, dan seterusnya. Jumlah hasil panen selama 9 hari pertama adalah ....

- **A. 324 kg** ✅  
  <sub>Benar: $a = 20$, $b = 4$, $n = 9$: $S_9 = \frac{9}{2}(40 + 8 \times 4) = 324$</sub>
- B. 342 kg  
  <sub>Salah: memakai $n \times b$ (bukan $(n-1)b$) pada rumus jumlah</sub>
- C. 272 kg  
  <sub>Salah: memakai $n = 8$ (salah menghitung banyak hari)</sub>
- D. 648 kg  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>

**Pembahasan:** $b = 24 - 20 = 4$. $S_9 = \frac{9}{2}(2 \times 20 + 8 \times 4) = \frac{9 \times 72}{2} = 324$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12-b01-b-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: soal cerita deret aritmetika (hasil panen naik tetap)*

Seorang nelayan mencatat tangkapan ikannya selama 13 hari pertama. Setiap harinya, tangkapan mengalami kenaikan tetap dimulai hari pertama, kedua, ketiga berturut-turut 6 kg, 10 kg, 14 kg, dan seterusnya. Jumlah tangkapan selama 13 hari pertama adalah ....

- A. 336 kg  
  <sub>Salah: memakai $n = 12$ (salah menghitung banyak hari)</sub>
- B. 780 kg  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- **C. 390 kg** ✅  
  <sub>Benar: $a = 6$, $b = 4$, $n = 13$: $S_{13} = \frac{13}{2}(12 + 12 \times 4) = 390$</sub>
- D. 416 kg  
  <sub>Salah: memakai $n \times b$ (bukan $(n-1)b$) pada rumus jumlah</sub>

**Pembahasan:** $b = 10 - 6 = 4$. $S_{13} = \frac{13}{2}(2 \times 6 + 12 \times 4) = \frac{13 \times 60}{2} = 390$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12-b01-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: penjumlahan 1 sampai N cara Gauss*

Dengan cara Gauss, suku pertama dipasangkan dengan suku terakhir, suku kedua dengan suku sebelum terakhir, dan seterusnya sehingga tiap pasangan berjumlah sama. Jumlah $1 + 2 + 3 + \dots + 80$ adalah ....

- A. 3.200  
  <sub>Salah: menjumlah tiap pasangan dengan 80 bukan 81</sub>
- **B. 3.240** ✅  
  <sub>Benar: ada 40 pasangan yang masing-masing berjumlah $1 + 80 = 81$, sehingga $40 \times 81 = 3.240$</sub>
- C. 3.321  
  <sub>Salah: menganggap ada 41 pasangan</sub>
- D. 6.480  
  <sub>Salah: mengalikan 80 dengan 81 tanpa membagi 2 (banyak pasangan dianggap 80)</sub>

**Pembahasan:** Pasangan: $(1+80), (2+79), \dots, (40+41)$, ada 40 pasangan dengan jumlah 81 tiap pasangan. Jumlah $= 40 \times 81 = 3.240$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12-b01-b-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: jumlah n suku pertama deret geometri*

Jumlah 5 suku pertama deret geometri $2 + 10 + 50 + 250 + \dots$ adalah ....

- A. 7.812  
  <sub>Salah: memakai $n = 6$ (satu suku berlebih)</sub>
- B. 312  
  <sub>Salah: memakai $n = 4$ (hanya 4 suku)</sub>
- C. 6.248  
  <sub>Salah: lupa membagi dengan $(r - 1)$</sub>
- **D. 1.562** ✅  
  <sub>Benar: $r = 5$, $S_5 = \frac{2(5^5 - 1)}{5 - 1} = \frac{2 \times 3.124}{4} = 1.562$</sub>

**Pembahasan:** $a = 2$, $r = 10 \div 2 = 5$. $S_5 = \frac{2(3.125 - 1)}{4} = \frac{6.248}{4} = 1.562$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12-b01-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: jumlah deret geometri tak hingga*

Jumlah deret geometri tak hingga $18 + 6 + 2 + \frac{2}{3} + \dots$ adalah ....

- **A. 27** ✅  
  <sub>Benar: $r = \frac{1}{3}$, $S_\infty = \frac{18}{1 - \frac{1}{3}} = 27$</sub>
- B. 12  
  <sub>Salah: mengalikan $a(1 - r)$ bukan membagi</sub>
- C. 13,5  
  <sub>Salah: memakai penyebut $(1 + r)$ sehingga $\frac{18}{4/3}$</sub>
- D. 54  
  <sub>Salah: membagi $a$ dengan $r$ bukan dengan $(1 - r)$</sub>

**Pembahasan:** $r = \frac{6}{18} = \frac{1}{3}$ dengan $|r| < 1$. $S_\infty = \frac{a}{1 - r} = \frac{18}{2/3} = 27$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12-b01-b-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: menjumlahkan suku dari data tabel*

**Tabel** Banyak Rumah Tangga yang Membuang Sampah dalam 5 Bulan

| Bulan | Agustus 2024 | September 2024 | Oktober 2024 | November 2024 | Desember 2024 |
|---|---|---|---|---|---|
| Jumlah Rumah Tangga | 2 | 6 | 18 | 54 | 162 |

Banyak rumah tangga yang membuang sampah ke sungai pada bulan September, Oktober, dan November 2024 dijumlahkan menjadi satu deret. Jumlah rumah tangga pada ketiga bulan tersebut adalah ....

- A. 80  
  <sub>Salah: ikut menjumlahkan bulan Agustus (2) sehingga 4 bulan</sub>
- B. 24  
  <sub>Salah: hanya menjumlahkan September dan Oktober</sub>
- **C. 78** ✅  
  <sub>Benar: $6 + 18 + 54 = 78$</sub>
- D. 240  
  <sub>Salah: ikut menjumlahkan bulan Desember (162) dan bukan November sebagai batas</sub>

**Pembahasan:** Banyak rumah tangga: September 6, Oktober 18, November 54. Jumlahnya $6 + 18 + 54 = 78$.
**Acuan:** siswa — siswa hal.43

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12-b01-b-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: jumlah deret dari suku pertama dan suku terakhir*

Suatu deret aritmetika memiliki suku pertama 9 dan suku ke-14 sama dengan 61. Jumlah 14 suku pertama deret tersebut adalah ....

- A. 980  
  <sub>Salah: lupa membagi 2 pada $S_n = \frac{n}{2}(a + U_n)$</sub>
- B. 364  
  <sub>Salah: mengurangi $U_n - a$ bukan menjumlahkan $a + U_n$</sub>
- C. 427  
  <sub>Salah: mengalikan $\frac{n}{2}$ dengan $U_n$ saja tanpa menambahkan $a$</sub>
- **D. 490** ✅  
  <sub>Benar: $S_{14} = \frac{14}{2}(9 + 61) = 7 \times 70 = 490$</sub>

**Pembahasan:** Karena $U_{14}$ diketahui, $S_{14} = \frac{n}{2}(a + U_{14}) = \frac{14}{2}(9 + 61) = 490$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12-b01-b-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: syarat deret geometri tak hingga memiliki jumlah*

Suatu deret geometri tak hingga memiliki suku pertama 6. Agar deret tersebut memiliki jumlah (konvergen), rasio yang mungkin adalah ....

- A. $r = -\frac{3}{2}$  
  <sub>Salah: $|r| > 1$ sehingga deret divergen (tanda negatif dikira menjamin konvergen)</sub>
- B. $r = \frac{5}{4}$  
  <sub>Salah: $|r| > 1$ sehingga deret divergen</sub>
- C. $r = 1$  
  <sub>Salah: $r = 1$ membuat tiap suku sama (6 + 6 + 6 + ...) sehingga divergen</sub>
- **D. $r = -\frac{3}{4}$** ✅  
  <sub>Benar: $|r| = \frac{3}{4} < 1$ sehingga jumlah tak hingga ada</sub>

**Pembahasan:** Deret geometri tak hingga memiliki jumlah bila $|r| < 1$. Hanya $-\frac{3}{4}$ yang memenuhi.
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12-b01-b-medium-bt01-001
*variasi (angka) | C4 | 3 langkah | jenis: mencari a dan b dari dua jumlah deret*

Diberikan deret aritmetika dengan $S_8 = 160$ dan $S_{16} = 576$. Seorang siswa menyimpulkan bahwa suku pertama ($a$) adalah 7 dan beda ($b$) adalah 3. Nilai $a$ dan $b$ yang sebenarnya adalah ....

- A. $a = 7$ dan $b = 3$  
  <sub>Salah: mengikuti kesimpulan siswa tanpa memeriksa $S_8$ dan $S_{16}$</sub>
- B. $a = 4$ dan $b = 6$  
  <sub>Salah: nilai $a$ dan $b$ tertukar</sub>
- C. $a = 5$ dan $b = 5$  
  <sub>Salah: salah eliminasi sehingga $a$ dan $b$ keliru</sub>
- **D. $a = 6$ dan $b = 4$** ✅  
  <sub>Benar: $2a + 7b = 40$ dan $2a + 15b = 72$, selisih $8b = 32$ sehingga $b = 4$, $a = 6$</sub>

**Pembahasan:** $S_8 = 4(2a + 7b) = 160 \Rightarrow 2a + 7b = 40$. $S_{16} = 8(2a + 15b) = 576 \Rightarrow 2a + 15b = 72$. Kurangkan: $8b = 32$, $b = 4$, $a = 6$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12-b01-b-medium-bt01-002
*variasi (konteks) | C4 | 3 langkah | jenis: dua jumlah deret lalu suku ke-n*

Seorang pengrajin membuat gelang dengan pertambahan produksi tetap setiap hari. Jumlah gelang yang dibuat selama 6 hari pertama adalah 75 dan selama 12 hari pertama adalah 258. Banyak gelang yang dibuat pada hari ke-10 adalah ....

- **A. 32** ✅  
  <sub>Benar: $2a + 5b = 25$ dan $2a + 11b = 43$ sehingga $b = 3$, $a = 5$, $U_{10} = 5 + 9 \times 3 = 32$</sub>
- B. 48  
  <sub>Salah: nilai $a$ dan $b$ tertukar ($a = 3$, $b = 5$)</sub>
- C. 29  
  <sub>Salah: memakai $n = 9$ (salah menghitung hari ke-10)</sub>
- D. 35  
  <sub>Salah: memakai $a + 10b$ (n bukan n-1)</sub>

**Pembahasan:** $S_6 = 3(2a + 5b) = 75$ dan $S_{12} = 6(2a + 11b) = 258$. Diperoleh $b = 3$, $a = 5$, jadi $U_{10} = 5 + 9 \times 3 = 32$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12-b01-b-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: tiga bilangan deret aritmetika*

Tiga bilangan membentuk deret aritmetika. Jika jumlah mereka 36 dan hasil kalinya 1.680, bilangan terbesar di antara ketiga bilangan tersebut adalah ....

- A. 12  
  <sub>Salah: memilih bilangan tengah</sub>
- B. 10  
  <sub>Salah: memilih bilangan terkecil</sub>
- **C. 14** ✅  
  <sub>Benar: bilangan tengah 12, $12(144 - d^2) = 1.680 \Rightarrow d^2 = 4$, bilangan 10, 12, 14</sub>
- D. 16  
  <sub>Salah: memakai $d = 4$ (lupa mengakarkan $d^2 = 4$)</sub>

**Pembahasan:** Misalkan bilangan $x - d$, $x$, $x + d$. Jumlah $3x = 36$ sehingga $x = 12$. Hasil kali $12(144 - d^2) = 1.680 \Rightarrow d^2 = 4$, $d = \pm 2$. Bilangannya 10, 12, 14.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12-b01-b-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: tiga bilangan deret aritmetika (konteks)*

Panjang tiga potong tali membentuk deret aritmetika. Jika jumlah panjang ketiga potong tali itu 45 cm dan hasil kali panjangnya 3.135 cm$^3$, panjang potongan terpendek adalah ....

- A. 15 cm  
  <sub>Salah: memilih potongan tengah</sub>
- **B. 11 cm** ✅  
  <sub>Benar: potongan tengah 15 cm, $15(225 - d^2) = 3.135 \Rightarrow d^2 = 16$, panjangnya 11, 15, 19</sub>
- C. 7 cm  
  <sub>Salah: mengira $d = 8$ (membagi 16 dengan 2 bukan mengakarkan)</sub>
- D. 19 cm  
  <sub>Salah: memilih potongan terpanjang</sub>

**Pembahasan:** Misalkan $x - d$, $x$, $x + d$. $3x = 45 \Rightarrow x = 15$. $15(225 - d^2) = 3.135 \Rightarrow d^2 = 16$, $d = 4$. Panjangnya 11, 15, 19 cm; terpendek 11 cm.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12-b01-b-medium-bt01-005
*variasi (angka) | C4 | 3 langkah | jenis: suku bergantian menjadi suku tengah*

Jika $U_n$ menyatakan suku ke-$n$ suatu barisan aritmetika dan diketahui $U_3 - U_5 + U_7 - U_9 + U_{11} = 15$, berapa jumlah 13 suku pertama barisan tersebut?

- **A. 195** ✅  
  <sub>Benar: $U_3 + U_{11} = U_5 + U_9 = 2U_7$ sehingga ekspresi $= U_7 = 15$; $S_{13} = 13 \times U_7 = 195$</sub>
- B. 105  
  <sub>Salah: mengalikan $U_7$ dengan 7 (mengira banyak suku 7)</sub>
- C. 165  
  <sub>Salah: mengalikan $U_7$ dengan 11 (mengira banyak suku 11)</sub>
- D. 390  
  <sub>Salah: memakai $S_{13} = 13(a + U_{13})$ tanpa membagi 2</sub>

**Pembahasan:** Karena $U_3 + U_{11} = 2U_7$ dan $U_5 + U_9 = 2U_7$, maka $U_3 - U_5 + U_7 - U_9 + U_{11} = U_7 = 15$. $S_{13} = \frac{13}{2}(a + U_{13}) = \frac{13}{2} \times 2U_7 = 13 \times 15 = 195$.
**Acuan:** pretest — kelas12-b01-p0042-latihan-1-3-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12-b01-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: dua suku geometri lalu jumlah deret*

Suku ke-3 suatu deret geometri dengan rasio positif adalah 24 dan suku ke-5 adalah 96. Jumlah 5 suku pertama deret tersebut adalah ....

- **A. 186** ✅  
  <sub>Benar: $r^2 = \frac{96}{24} = 4$, $r = 2$, $a = 6$, $S_5 = \frac{6(2^5 - 1)}{2 - 1} = 186$</sub>
- B. 378  
  <sub>Salah: menjumlahkan 6 suku, bukan 5</sub>
- C. 90  
  <sub>Salah: menjumlahkan 4 suku, bukan 5</sub>
- D. 93  
  <sub>Salah: salah suku pertama: $a = 3$ sehingga jumlahnya setengah</sub>

**Pembahasan:** $\frac{U_5}{U_3} = r^2 = 4$, $r = 2$ (positif). $a = \frac{24}{4} = 6$. $S_5 = \frac{6(32 - 1)}{1} = 186$.
**Acuan:** pretest — kelas12-b01-p0047-latihan-1-4-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12-b01-b-medium-bt01-007
*variasi (konteks) | C3 | 4 langkah | jenis: dua suku geometri lalu jumlah deret (konteks)*

Banyak pengunjung suatu situs bertambah dengan pola barisan geometri berrasio positif. Pengunjung pada hari kedua 60 orang dan pada hari keempat 540 orang. Jumlah pengunjung selama 4 hari pertama adalah ....

- A. 1.600 orang  
  <sub>Salah: lupa membagi dengan $(r - 1)$</sub>
- B. 2.420 orang  
  <sub>Salah: menjumlahkan 5 hari</sub>
- C. 260 orang  
  <sub>Salah: menjumlahkan 3 hari saja</sub>
- **D. 800 orang** ✅  
  <sub>Benar: $r^2 = \frac{540}{60} = 9$, $r = 3$, $a = 20$, $S_4 = \frac{20(3^4 - 1)}{3 - 1} = 800$</sub>

**Pembahasan:** $U_4 / U_2 = r^2 = 9$, $r = 3$. $a = \frac{60}{3} = 20$. $S_4 = \frac{20(81 - 1)}{2} = 800$.
**Acuan:** pretest — kelas12-b01-p0047-latihan-1-4-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12-b01-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: panjang lintasan bola memantul*

Suatu bola dijatuhkan dari ketinggian 12 meter. Setiap pantulan mencapai $\frac{3}{4}$ dari tinggi sebelumnya. Hitung total seluruh jarak yang ditempuh oleh bola tersebut hingga berhenti.

- A. 72 meter  
  <sub>Salah: hanya menjumlahkan lintasan naik dan turun setelah pantulan, tanpa jatuh awal 12 m</sub>
- B. 48 meter  
  <sub>Salah: hanya menjumlahkan lintasan turun $\frac{12}{1 - 3/4}$</sub>
- **C. 84 meter** ✅  
  <sub>Benar: naik pertama 9 m: lintasan $= 12 + 2 \times \frac{9}{1 - 3/4} = 12 + 72 = 84$</sub>
- D. 96 meter  
  <sub>Salah: menghitung lintasan turun dan naik sama-sama $\frac{12}{1 - 3/4}$ lalu dikali 2</sub>

**Pembahasan:** Jatuh awal 12 m. Setelah itu naik-turun: tinggi pantulan pertama 9 m, rasio $\frac{3}{4}$, jumlah satu arah $= \frac{9}{1 - 3/4} = 36$, dua arah 72. Total $12 + 72 = 84$ m.
**Acuan:** pretest — kelas12-b01-p0047-latihan-1-4-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12-b01-b-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: membandingkan dua deret geometri*

Diberikan dua deret geometri. Deret A dengan $a = 5$, $r = 4$, dan $n = 4$, sedangkan deret B dengan $a = 7$, $r = 5$ dan $n = 3$. Pernyataan yang benar mengenai jumlah suku kedua deret tersebut adalah ....

- A. Deret B lebih besar dengan selisih 208  
  <sub>Salah: membandingkan dengan arah terbalik</sub>
- B. Deret A lebih besar dengan selisih 63  
  <sub>Salah: memakai $n - 1$ suku pada kedua deret</sub>
- **C. Deret A lebih besar dengan selisih 208** ✅  
  <sub>Benar: $S_A = \frac{5(4^4 - 1)}{3} = 425$, $S_B = \frac{7(5^3 - 1)}{4} = 217$, selisih 208</sub>
- D. Deret A lebih besar dengan selisih 407  
  <sub>Salah: lupa membagi dengan $(r - 1)$ pada kedua deret</sub>

**Pembahasan:** $S_A = \frac{5 \times 255}{3} = 425$. $S_B = \frac{7 \times 124}{4} = 217$. $425 - 217 = 208$ sehingga deret A lebih besar.
**Acuan:** pretest — kelas12-b01-p0048-latihan-1-4-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12-b01-b-medium-bt01-010
*variasi (angka) | C4 | 4 langkah | jenis: jumlah bilangan bersyarat pada deret*

Diketahui deret bilangan $15 + 16 + 17 + 18 + \dots + 94$. Dari deret bilangan tersebut, jumlah bilangan yang habis dibagi tiga tetapi tidak habis dibagi sembilan adalah ....

- A. 1.944  
  <sub>Salah: menjumlahkan kelipatan 3 dan kelipatan 9, bukan mengurangkan</sub>
- **B. 972** ✅  
  <sub>Benar: kelipatan 3: $15, \dots, 93$ ($n = 27$) jumlah 1.458; kelipatan 9: $18, \dots, 90$ ($n = 9$) jumlah 486; selisih 972</sub>
- C. 486  
  <sub>Salah: hanya menghitung jumlah kelipatan 9</sub>
- D. 1.458  
  <sub>Salah: menjumlahkan semua kelipatan 3 tanpa mengeluarkan kelipatan 9</sub>

**Pembahasan:** Kelipatan 3: $S = \frac{27}{2}(15 + 93) = 1.458$. Kelipatan 9: $S = \frac{9}{2}(18 + 90) = 486$. Hasil: $1.458 - 486 = 972$.
**Acuan:** pretest — kelas12-b01-p0051-uji-kompetensi-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12-b01-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: dua suku diketahui lalu jumlah deret aritmetika*

Pada suatu deret aritmetika, suku ke-3 adalah 11 dan suku ke-8 adalah 31. Jumlah 10 suku pertama deret tersebut adalah ....

- A. 420  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- B. 250  
  <sub>Salah: salah suku pertama: $a = U_3 - b = 7$</sub>
- C. 230  
  <sub>Salah: memakai $n \times b$ bukan $(n-1)b$ pada rumus jumlah</sub>
- **D. 210** ✅  
  <sub>Benar: $5b = 20$, $b = 4$, $a = 3$, $S_{10} = 5(6 + 36) = 210$</sub>

**Pembahasan:** $U_8 - U_3 = 5b = 20 \Rightarrow b = 4$. $a = 11 - 2 \times 4 = 3$. $S_{10} = \frac{10}{2}(2 \times 3 + 9 \times 4) = 210$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12-b01-b-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: jumlah geometri diketahui lalu mencari suku*

Suatu deret geometri memiliki suku pertama 5 dan rasio positif. Jika jumlah 3 suku pertamanya 105, suku ke-5 deret tersebut adalah ....

- **A. 1.280** ✅  
  <sub>Benar: $5(1 + r + r^2) = 105 \Rightarrow r^2 + r - 20 = 0 \Rightarrow r = 4$, $U_5 = 5 \times 4^4 = 1.280$</sub>
- B. 1.024  
  <sub>Salah: lupa mengalikan dengan suku pertama 5</sub>
- C. 5.120  
  <sub>Salah: memakai $r^5$ (suku ke-6), bukan $r^4$</sub>
- D. 320  
  <sub>Salah: memakai $r^3$ (suku ke-4), bukan $r^4$</sub>

**Pembahasan:** $S_3 = 5(1 + r + r^2) = 105$ sehingga $r^2 + r - 20 = 0$, $(r + 5)(r - 4) = 0$, $r = 4$ (positif). $U_5 = ar^4 = 5 \times 256 = 1.280$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12-b01-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: deret tak hingga: cari rasio lalu suku*

Suatu deret geometri tak hingga memiliki suku pertama 9 dan jumlah 12. Suku ke-3 deret tersebut adalah ....

- A. $\frac{9}{64}$  
  <sub>Salah: memberi suku ke-4 ($ar^3$), bukan suku ke-3</sub>
- B. $\frac{9}{4}$  
  <sub>Salah: memberi suku ke-2 ($ar$), bukan suku ke-3</sub>
- **C. $\frac{9}{16}$** ✅  
  <sub>Benar: $12 = \frac{9}{1 - r} \Rightarrow r = \frac{1}{4}$, $U_3 = 9 \times \frac{1}{16} = \frac{9}{16}$</sub>
- D. $\frac{81}{16}$  
  <sub>Salah: memakai $r = \frac{3}{4}$ (mengambil $1 - r$ sebagai rasio)</sub>

**Pembahasan:** $S_\infty = \frac{a}{1 - r}$: $12(1 - r) = 9 \Rightarrow 1 - r = \frac{3}{4}$, $r = \frac{1}{4}$. $U_3 = ar^2 = 9 \times \frac{1}{16} = \frac{9}{16}$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12-b01-b-medium-bt01-014
*orisinal | C3 | 2 langkah | jenis: rasio dari perbandingan jumlah tak hingga*

Jumlah suatu deret geometri tak hingga sama dengan 3 kali suku pertamanya. Rasio deret tersebut adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: mengira $r$ sama dengan nilai $1 - r$</sub>
- **B. $\frac{2}{3}$** ✅  
  <sub>Benar: $\frac{a}{1 - r} = 3a \Rightarrow 1 - r = \frac{1}{3} \Rightarrow r = \frac{2}{3}$</sub>
- C. $-2$  
  <sub>Salah: menyelesaikan $1 - r = 3$</sub>
- D. $\frac{4}{3}$  
  <sub>Salah: menyelesaikan $r - 1 = \frac{1}{3}$ (tanda tertukar), padahal $|r| > 1$ tidak konvergen</sub>

**Pembahasan:** $S_\infty = \frac{a}{1 - r} = 3a \Rightarrow 1 - r = \frac{1}{3} \Rightarrow r = \frac{2}{3}$ (memenuhi $|r| < 1$).
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12-b01-b-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: jumlah kelipatan bilangan di antara dua batas*

Jumlah semua bilangan bulat kelipatan 7 yang terletak di antara 100 dan 300 adalah ....

- **A. 5.586** ✅  
  <sub>Benar: kelipatan 7 dari 105 sampai 294, $n = \frac{294 - 105}{7} + 1 = 28$, $S = 14 \times 399 = 5.586$</sub>
- B. 5.985  
  <sub>Salah: salah menghitung banyak suku ($n = 30$)</sub>
- C. 11.172  
  <sub>Salah: lupa membagi 2 pada rumus jumlah</sub>
- D. 5.187  
  <sub>Salah: salah menghitung banyak suku ($n = 26$)</sub>

**Pembahasan:** Suku pertama 105, terakhir 294, beda 7. $n = \frac{294 - 105}{7} + 1 = 28$. $S_{28} = \frac{28}{2}(105 + 294) = 5.586$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12-b01-b-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: menabung bertambah tetap: cari banyak bulan*

Rina menabung Rp50.000 pada bulan pertama, kemudian setiap bulan berikutnya tabungannya Rp10.000 lebih banyak daripada bulan sebelumnya. Rina berhenti menabung ketika jumlah seluruh tabungannya tepat Rp1.260.000. Rina menabung selama .... bulan.

- A. 13  
  <sub>Salah: $S_{13}$ = Rp1.430.000, melebihi Rp1.260.000</sub>
- **B. 12** ✅  
  <sub>Benar: $S_n = \frac{n}{2}(100 + 10(n-1)) = 5n^2 + 45n = 1.260$ (dalam ribuan) $\Rightarrow n = 12$</sub>
- C. 11  
  <sub>Salah: $S_{11}$ = Rp1.100.000, belum mencapai Rp1.260.000</sub>
- D. 14  
  <sub>Salah: $S_{14}$ = Rp1.610.000, melebihi Rp1.260.000</sub>

**Pembahasan:** Dalam ribuan rupiah: $\frac{n}{2}(2 \times 50 + (n - 1)10) = 5n^2 + 45n = 1.260 \Rightarrow n^2 + 9n - 252 = 0 \Rightarrow (n + 21)(n - 12) = 0$, $n = 12$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12-b01-b-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: mencari banyak suku deret geometri*

Deret geometri $4 + 8 + 16 + \dots$ memiliki jumlah 1.020. Banyak suku pada deret tersebut adalah ....

- A. 9  
  <sub>Salah: $S_9 = 2.044$, melebihi 1.020</sub>
- **B. 8** ✅  
  <sub>Benar: $\frac{4(2^n - 1)}{2 - 1} = 1.020 \Rightarrow 2^n = 256 \Rightarrow n = 8$</sub>
- C. 7  
  <sub>Salah: $S_7 = 508$, kurang dari 1.020</sub>
- D. 255  
  <sub>Salah: mengambil nilai $2^n - 1$ sebagai banyak suku</sub>

**Pembahasan:** $r = 2$, $a = 4$. $S_n = 4(2^n - 1) = 1.020 \Rightarrow 2^n - 1 = 255 \Rightarrow 2^n = 256 \Rightarrow n = 8$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12-b01-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: jumlah n suku dan satu suku diketahui*

Pada suatu deret aritmetika, jumlah 9 suku pertama adalah 225 dan suku ke-3 adalah 13. Suku ke-12 deret tersebut adalah ....

- A. 73  
  <sub>Salah: memakai $n = 13$ (suku ke-13)</sub>
- B. 66  
  <sub>Salah: lupa menambahkan suku pertama pada $U_{12}$</sub>
- C. 61  
  <sub>Salah: memakai $n = 11$ (suku ke-11)</sub>
- **D. 67** ✅  
  <sub>Benar: $a + 4b = 25$ dan $a + 2b = 13$ sehingga $b = 6$, $a = 1$, $U_{12} = 1 + 66 = 67$</sub>

**Pembahasan:** $S_9 = \frac{9}{2}(2a + 8b) = 9(a + 4b) = 225 \Rightarrow a + 4b = 25$. $U_3 = a + 2b = 13$. Kurangkan: $2b = 12$, $b = 6$, $a = 1$. $U_{12} = 1 + 11 \times 6 = 67$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12-b01-b-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: dua deret aritmetika dengan jumlah sama*

Deret aritmetika pertama memiliki suku pertama 5 dan beda 4, sedangkan deret aritmetika kedua memiliki suku pertama 41 dan beda $-2$. Jumlah $n$ suku pertama kedua deret itu sama untuk $n$ bilangan asli sebesar ....

- A. 12  
  <sub>Salah: salah menyelesaikan $6n = 78$ (memakai 72)</sub>
- B. 26  
  <sub>Salah: mengalikan hasil $n$ dengan 2 (mengira $\frac{n}{2} = 13$)</sub>
- **C. 13** ✅  
  <sub>Benar: $\frac{n}{2}(10 + 4(n-1)) = \frac{n}{2}(82 - 2(n-1))$, sehingga $4n + 6 = 84 - 2n$ dan $n = 13$</sub>
- D. 14  
  <sub>Salah: salah menyelesaikan $6n = 78$ (memakai 84)</sub>

**Pembahasan:** $S_n^{(1)} = \frac{n}{2}(4n + 6)$ dan $S_n^{(2)} = \frac{n}{2}(84 - 2n)$. Samakan, $n \neq 0$: $4n + 6 = 84 - 2n \Rightarrow 6n = 78 \Rightarrow n = 13$. Keduanya 377.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12-b01-b-medium-bt01-020
*orisinal | C3 | 2 langkah | jenis: deret tak hingga dalam konteks pertumbuhan*

Pertambahan tinggi sebuah tanaman pada tahun pertama 60 cm dan pada setiap tahun berikutnya sama dengan $\frac{3}{4}$ dari pertambahan tahun sebelumnya. Jika tinggi awal dianggap 0 cm, batas tinggi tanaman itu setelah waktu yang sangat lama adalah ....

- A. 45 cm  
  <sub>Salah: hanya mengambil pertambahan tahun kedua</sub>
- B. 80 cm  
  <sub>Salah: membagi 60 dengan $r$, bukan dengan $(1 - r)$</sub>
- C. 180 cm  
  <sub>Salah: hanya menjumlahkan pertambahan mulai tahun kedua ($\frac{45}{1 - 3/4}$)</sub>
- **D. 240 cm** ✅  
  <sub>Benar: $S_\infty = \frac{60}{1 - 3/4} = 240$</sub>

**Pembahasan:** Deret geometri tak hingga $a = 60$, $r = \frac{3}{4}$ ($|r| < 1$). $S_\infty = \frac{a}{1 - r} = \frac{60}{1/4} = 240$ cm.
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12-b01-b-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan rumus jumlah aritmetika*

Rina menghitung jumlah 10 suku pertama deret $4 + 7 + 10 + \dots$ dengan cara $S_{10} = \frac{10}{2}(2 \cdot 4 + 10 \cdot 3) = 190$. Pernyataan yang benar tentang pekerjaan Rina adalah ....

- A. Benar, karena $S_{10} = 190$  
  <sub>Salah: mengira penyelesaian Rina sudah sesuai rumus</sub>
- B. Salah, seharusnya memakai $(n+1)b$ sehingga $S_{10} = 205$  
  <sub>Salah: menukar $(n-1)$ dengan $(n+1)$</sub>
- **C. Salah, seharusnya memakai $(n-1)b$ sehingga $S_{10} = 175$** ✅  
  <sub>Benar: rumus $S_n = \frac{n}{2}(2a + (n-1)b)$; Rina memakai $nb$ bukan $(n-1)b$; yang benar $5(8 + 27) = 175$</sub>
- D. Salah, seharusnya tanpa faktor $\frac{n}{2}$ sehingga $S_{10} = 350$  
  <sub>Salah: salah mengira faktor $\frac{n}{2}$ yang keliru, padahal kesalahan ada pada $(n-1)b$</sub>

**Pembahasan:** Rumus yang benar $S_n = \frac{n}{2}(2a + (n-1)b)$. Rina memakai $nb$. Maka $S_{10} = 5(8 + 9 \cdot 3) = 5 \cdot 35 = 175$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12-b01-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: memilih deret tak hingga yang konvergen*

Deret geometri tak hingga berikut yang memiliki jumlah (konvergen) adalah ....

- A. $2 - 4 + 8 - 16 + \dots$  
  <sub>Salah: mengira rasio negatif selalu membuat jumlah ada, padahal $|r| = 2 > 1$</sub>
- **B. $9 - 6 + 4 - \frac{8}{3} + \dots$** ✅  
  <sub>Benar: rasio $r = -\frac{2}{3}$ sehingga $|r| < 1$ dan jumlahnya $\frac{9}{1 + \frac{2}{3}} = \frac{27}{5}$</sub>
- C. $5 + 10 + 20 + 40 + \dots$  
  <sub>Salah: rasio $r = 2$, $|r| > 1$ sehingga divergen</sub>
- D. $3 + 3 + 3 + 3 + \dots$  
  <sub>Salah: rasio $r = 1$, jumlahnya terus bertambah tanpa batas</sub>

**Pembahasan:** Deret tak hingga memiliki jumlah bila $|r| < 1$. Hanya deret $9 - 6 + 4 - \dots$ ($r = -\frac{2}{3}$) yang memenuhi.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12-b01-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: syarat parameter konvergensi*

Deret geometri tak hingga $5 + \frac{5k}{3} + \frac{5k^2}{9} + \dots$ memiliki rasio $\frac{k}{3}$ dengan $k$ bilangan bulat. Banyak nilai $k$ agar deret tersebut memiliki jumlah adalah ....

- A. 7  
  <sub>Salah: memakai $|r| \le 1$ sehingga $k = -3$ dan $k = 3$ ikut dihitung</sub>
- B. 6  
  <sub>Salah: menyertakan salah satu nilai ujung ($k = 3$ atau $k = -3$)</sub>
- C. 3  
  <sub>Salah: hanya menghitung $k$ tak negatif, yaitu $0, 1, 2$</sub>
- **D. 5** ✅  
  <sub>Benar: syarat $|\frac{k}{3}| < 1$ berarti $-3 < k < 3$; bilangan bulatnya $-2, -1, 0, 1, 2$</sub>

**Pembahasan:** $|k/3| < 1 \Rightarrow -3 < k < 3$, bilangan bulat: $-2, -1, 0, 1, 2$, yaitu 5 nilai.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12-b01-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: menguji kemungkinan hasil jumlah deret*

Panitia menata kursi pertunjukan. Baris pertama berisi 3 kursi dan setiap baris berikutnya berisi 2 kursi lebih banyak dari baris di depannya. Semua baris terisi penuh. Banyak kursi seluruhnya yang mungkin adalah ....

- A. 150  
  <sub>Salah: $n(n+2) = 150$ tidak punya akar bilangan asli (antara $11 \cdot 13$ dan $12 \cdot 14$)</sub>
- B. 200  
  <sub>Salah: $n(n+2) = 200$ tidak punya akar bilangan asli (antara $13 \cdot 15$ dan $14 \cdot 16$)</sub>
- **C. 120** ✅  
  <sub>Benar: $S_n = \frac{n}{2}(6 + 2(n-1)) = n(n+2)$; $n(n+2) = 120$ dipenuhi $n = 10$</sub>
- D. 130  
  <sub>Salah: $n(n+2) = 130$ tidak punya akar bilangan asli (antara $10 \cdot 12$ dan $11 \cdot 13$)</sub>

**Pembahasan:** $S_n = n(n+2)$. Hanya 120 yang berbentuk $n(n+2)$ ($10 \cdot 12$). Nilai 130, 150, 200 tidak.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12-b01-b-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: memilih contoh penyangkal klaim*

Dina berpendapat bahwa untuk setiap deret geometri tak hingga dengan suku pertama positif yang memiliki jumlah, jumlah tak hingganya selalu lebih besar daripada suku pertamanya. Contoh penyangkal pendapat Dina adalah ....

- A. $6 + 2 + \frac{2}{3} + \dots$  
  <sub>Salah: jumlahnya 9 > 6, mendukung pendapat Dina</sub>
- B. $8 + 4 + 2 + 1 + \dots$  
  <sub>Salah: jumlahnya 16 > 8, justru mendukung pendapat Dina</sub>
- **C. $8 - 4 + 2 - 1 + \dots$** ✅  
  <sub>Benar: $r = -\frac{1}{2}$ memberi jumlah $\frac{8}{1 + \frac{1}{2}} = \frac{16}{3} \approx 5{,}3 < 8$</sub>
- D. $8 + 16 + 32 + \dots$  
  <sub>Salah: deret divergen sehingga tidak memiliki jumlah, bukan penyangkal</sub>

**Pembahasan:** Klaim hanya berlaku bila $r > 0$. Untuk $r < 0$ jumlah $\frac{a}{1-r} < a$. Contoh penyangkal: $8 - 4 + 2 - \dots$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12-b01-b-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: membandingkan dua rencana (aritmetika vs geometri)*

Dua orang menabung setiap hari. Andi menabung Rp10.000 pada hari pertama dan setiap hari berikutnya Rp10.000 lebih banyak dari hari sebelumnya. Budi menabung Rp1.000 pada hari pertama dan setiap hari berikutnya dua kali lipat dari hari sebelumnya. Total tabungan Budi untuk pertama kali melebihi total tabungan Andi pada hari ke- ....

- A. 7  
  <sub>Salah: pada hari ke-7 total Budi Rp127.000 jauh di bawah Andi Rp280.000</sub>
- B. 8  
  <sub>Salah: total Budi hari ke-8 Rp255.000 masih di bawah Andi Rp360.000</sub>
- C. 10  
  <sub>Salah: hari ke-10 memang Budi lebih besar, tetapi bukan yang pertama</sub>
- **D. 9** ✅  
  <sub>Benar: total hari ke-9: Andi Rp450.000 dan Budi Rp511.000, sedangkan hari ke-8 Budi Rp255.000 < Andi Rp360.000</sub>

**Pembahasan:** Andi: $S_n = 5000n(n+1)$; Budi: $S_n = 1000(2^n - 1)$. $n=8$: 360.000 vs 255.000. $n=9$: 450.000 vs 511.000. Jadi hari ke-9.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12-b01-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: memperbaiki banyak suku sebelum menjumlah*

Tono menghitung banyak suku deret $7 + 11 + 15 + \dots + 95$ dengan $\frac{95 - 7}{4} = 22$ suku, lalu menjumlahkannya. Jumlah deret yang sebenarnya adalah ....

- **A. 1.173** ✅  
  <sub>Benar: banyak suku $\frac{95-7}{4} + 1 = 23$ sehingga $S_{23} = \frac{23}{2}(7 + 95) = 1.173$</sub>
- B. 2.346  
  <sub>Salah: lupa faktor $\frac{1}{2}$ pada rumus jumlah</sub>
- C. 987  
  <sub>Salah: mengurangi 1 dari banyak suku sehingga memakai 21 suku</sub>
- D. 1.078  
  <sub>Salah: memakai 22 suku seperti Tono (lupa menambah 1)</sub>

**Pembahasan:** $U_n = 7 + (n-1)4 = 95 \Rightarrow n = 23$. $S_{23} = \frac{23}{2}(7 + 95) = 1.173$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12-b01-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: pasangan ala Gauss pada deret selang-seling*

Nilai dari $1 - 2 + 3 - 4 + \dots - 2024 + 2025$ adalah ....

- **A. 1.013** ✅  
  <sub>Benar: 1.012 pasangan $(2k-1) - 2k = -1$ memberi $-1.012$, lalu ditambah suku terakhir 2.025</sub>
- B. 1.012  
  <sub>Salah: menganggap tiap pasangan bernilai $+1$</sub>
- C. -1.012  
  <sub>Salah: melupakan suku terakhir 2.025 yang tidak berpasangan</sub>
- D. -1.013  
  <sub>Salah: salah tanda hasil akhir</sub>

**Pembahasan:** Ada 2025 suku. Kelompokkan 2024 suku pertama menjadi 1012 pasangan masing-masing $-1$: $-1012$. Tambah 2025: $1013$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12-b01-b-hard-bt01-009
*orisinal | C6 | 6 langkah | jenis: syarat ganda: aritmetika berubah menjadi geometri*

Tiga bilangan membentuk deret aritmetika dengan beda positif dan berjumlah 18. Jika bilangan ketiga ditambah 1 (bilangan lain tetap), ketiganya membentuk deret geometri. Hasil kali ketiga bilangan semula adalah ....

- A. 216  
  <sub>Salah: memakai bilangan setelah ditambah 1 ($4, 6, 9$)</sub>
- B. 162  
  <sub>Salah: memakai akar $b = -3$ yang memberi beda negatif ($9, 6, 3$)</sub>
- C. 144  
  <sub>Salah: mengira bilangan ketiga sama dengan bilangan tengah ($4 \cdot 6 \cdot 6$)</sub>
- **D. 192** ✅  
  <sub>Benar: bilangan $6-b,\ 6,\ 6+b$; $(6-b)(7+b) = 36 \Rightarrow b = 2$ (beda positif); bilangannya $4, 6, 8$ hasil kalinya 192</sub>

**Pembahasan:** Misalkan $6-b, 6, 6+b$. Geometri: $6^2 = (6-b)(6+b+1)$ sehingga $b^2 + b - 6 = 0$, $b = 2$ atau $b = -3$. Beda positif: $b = 2$, bilangan $4, 6, 8$, hasil kali $192$.
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12-b01-b-hard-bt01-010
*orisinal | C6 | 4 langkah | jenis: rancang batas minimal pada deret geometri*

Pada hari pertama sebuah percobaan ada 3 sel. Setiap hari, banyak sel baru yang muncul dua kali lipat dari hari sebelumnya. Jika yang dihitung adalah jumlah seluruh sel yang pernah muncul sejak hari pertama, jumlah tersebut pertama kali melebihi 3.000 pada hari ke- ....

- A. 11  
  <sub>Salah: membandingkan sel baru hari ke-$n$ ($3 \cdot 2^{n-1} > 3.000$) bukan jumlahnya</sub>
- B. 8  
  <sub>Salah: $S_8 = 765$ masih jauh di bawah 3.000</sub>
- **C. 10** ✅  
  <sub>Benar: $S_n = 3(2^n - 1)$; $S_9 = 1.533$ dan $S_{10} = 3.069 > 3.000$</sub>
- D. 9  
  <sub>Salah: $S_9 = 1.533$ belum melebihi 3.000</sub>

**Pembahasan:** $S_n = 3(2^n - 1) > 3000 \Rightarrow 2^n > 1001$, sehingga $n \ge 10$. $S_{10} = 3.069$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12-b01-b-hard-bt01-011
*orisinal | C5 | 3 langkah | jenis: temukan kesalahan rasio negatif*

Sinta menghitung jumlah 5 suku pertama deret $3 - 6 + 12 - 24 + 48$ dengan rasio $r = 2$ sehingga $S_5 = \frac{3(2^5 - 1)}{2 - 1} = 93$. Pernyataan yang benar adalah ....

- A. Salah, rasio seharusnya $-\frac{1}{2}$ dan $S_5 = \frac{33}{16}$  
  <sub>Salah: membalik rasio suku sebelumnya terhadap suku sesudahnya</sub>
- B. Salah, rasio seharusnya $-2$ dan $S_5 = -99$  
  <sub>Salah: memakai rasio $-2$ tetapi penyebut $1 - r$ ditulis $1 - 2$</sub>
- C. Benar, karena $S_5 = 93$  
  <sub>Salah: mengabaikan tanda negatif pada rasio</sub>
- **D. Salah, rasio seharusnya $-2$ dan $S_5 = 33$** ✅  
  <sub>Benar: $r = \frac{-6}{3} = -2$, $S_5 = \frac{3(1 - (-2)^5)}{1 - (-2)} = \frac{3 \cdot 33}{3} = 33$</sub>

**Pembahasan:** $r = -6/3 = -2$. $S_5 = 3(1 - (-32))/(1 + 2) = 33$. Cek: $3 - 6 + 12 - 24 + 48 = 33$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12-b01-b-hard-bt01-012
*orisinal | C6 | 4 langkah | jenis: merancang rasio agar lintasan terbatas*

Sebuah bola dijatuhkan dari ketinggian 10 m dan setiap kali memantul mencapai tinggi $r$ kali tinggi sebelumnya dengan $0 < r < 1$. Agar total panjang lintasan bola sampai berhenti tidak lebih dari 30 m, nilai $r$ terbesar yang mungkin adalah ....

- A. $\frac{3}{5}$  
  <sub>Salah: melupakan jatuhan pertama sehingga memakai $\frac{20r}{1-r} \le 30$</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: memakai batas lintasan 20 m, bukan 30 m</sub>
- **C. $\frac{1}{2}$** ✅  
  <sub>Benar: lintasan $= 10 \cdot \frac{1 + r}{1 - r} \le 30$ memberi $1 + r \le 3 - 3r$ sehingga $r \le \frac{1}{2}$</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: memakai $\frac{10}{1-r} \le 30$, hanya jumlah tinggi naik-turun satu arah</sub>

**Pembahasan:** Total lintasan $= 10 + 2 \cdot \frac{10r}{1-r} = 10 \cdot \frac{1+r}{1-r}$. $\le 30$: $1 + r \le 3(1-r)$, $r \le \frac{1}{2}$.
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12-b01-b-hard-bt01-013
*orisinal | C6 | 4 langkah | jenis: jumlah suku bernomor ganjil deret tak hingga*

Deret geometri tak hingga memiliki suku pertama 12 dan jumlah 18. Jumlah tak hingga dari suku-suku bernomor ganjil saja ($U_1 + U_3 + U_5 + \dots$) adalah ....

- **A. $\frac{27}{2}$** ✅  
  <sub>Benar: $r = \frac{1}{3}$; suku ganjil membentuk deret dengan suku pertama 12 dan rasio $r^2 = \frac{1}{9}$, jumlah $\frac{12}{1 - \frac{1}{9}} = \frac{27}{2}$</sub>
- B. $\frac{108}{5}$  
  <sub>Salah: salah menentukan rasio ($r = \frac{2}{3}$) lalu memakai $r^2 = \frac{4}{9}$</sub>
- C. $\frac{9}{2}$  
  <sub>Salah: mencari jumlah suku bernomor genap, yaitu $18 - \frac{27}{2}$</sub>
- D. $18$  
  <sub>Salah: menganggap suku ganjil memiliki rasio yang sama sehingga jumlahnya tetap 18</sub>

**Pembahasan:** $\frac{12}{1-r} = 18 \Rightarrow r = \frac{1}{3}$. Suku ganjil: $12, 12r^2, \dots$ dengan rasio $\frac{1}{9}$, jumlah $\frac{12}{8/9} = \frac{27}{2}$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12-b01-b-hard-bt01-014
*orisinal | C6 | 6 langkah | jenis: jumlah maksimum deret aritmetika menurun*

Suatu deret aritmetika memiliki suku pertama 30 dan memenuhi $S_8 = S_{13}$. Nilai terbesar yang dapat dicapai oleh $S_n$ adalah ....

- A. 156  
  <sub>Salah: mengira jumlah maksimum terjadi pada $n = 8$</sub>
- **B. 165** ✅  
  <sub>Benar: $S_8 = S_{13}$ memberi $b = -3$; $U_n = 33 - 3n$ tak negatif sampai $n = 11$; $S_{11} = \frac{11}{2}(60 - 30) = 165$</sub>
- C. 162  
  <sub>Salah: berhenti pada $n = 12$, padahal $U_{12} = -3$ mengurangi jumlah</sub>
- D. 330  
  <sub>Salah: lupa faktor $\frac{1}{2}$ pada rumus jumlah</sub>

**Pembahasan:** $4(60 + 7b) = \frac{13}{2}(60 + 12b) \Rightarrow b = -3$. $U_n = 33 - 3n \ge 0$ untuk $n \le 11$. $S_{11} = 165$ (juga $S_{10}$).
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12-b01-b-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: menemukan a dan b dari rumus jumlah*

Jumlah $n$ suku pertama suatu deret aritmetika adalah $S_n = 3n^2 + 2n$. Suku pertama $a$ dan beda $b$ deret tersebut berturut-turut adalah ....

- **A. $a = 5$ dan $b = 6$** ✅  
  <sub>Benar: $U_1 = S_1 = 5$, $U_2 = S_2 - S_1 = 16 - 5 = 11$, sehingga $b = 6$</sub>
- B. $a = 5$ dan $b = 3$  
  <sub>Salah: mengira beda sama dengan koefisien $n^2$</sub>
- C. $a = 5$ dan $b = 11$  
  <sub>Salah: menganggap $U_2 = S_2 = 16$ sehingga $b = 16 - 5$</sub>
- D. $a = 3$ dan $b = 2$  
  <sub>Salah: membaca langsung koefisien $3n^2$ dan $2n$ sebagai $b$ dan $a$</sub>

**Pembahasan:** $a = S_1 = 5$. $U_2 = S_2 - S_1 = 11$, $b = 6$. Cek $S_3 = 27 + 6 = 33 = 5 + 11 + 17$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12-b01-b-hard-bt01-016
*orisinal | C6 | 5 langkah | jenis: jumlah suku urutan ganjil dan genap*

Suatu deret aritmetika memiliki banyak suku ganjil. Jumlah suku-suku pada urutan ganjil ($U_1 + U_3 + U_5 + \dots$) adalah 108, sedangkan jumlah suku-suku pada urutan genap ($U_2 + U_4 + \dots$) adalah 96. Banyak suku deret tersebut adalah ....

- A. 18  
  <sub>Salah: membulatkan ke bilangan genap padahal banyak suku harus ganjil</sub>
- **B. 17** ✅  
  <sub>Benar: bila ada $2k+1$ suku dan suku tengah $U_t$: $(k+1)U_t = 108$ dan $kU_t = 96$ sehingga $U_t = 12$, $k = 8$</sub>
- C. 9  
  <sub>Salah: hanya menghitung banyak suku pada urutan ganjil</sub>
- D. 16  
  <sub>Salah: mengira banyak suku genap karena $k = 8$ dikalikan 2</sub>

**Pembahasan:** Suku urutan ganjil ada $k+1$ buah dengan rata-rata $U_t$; urutan genap ada $k$ buah dengan rata-rata $U_t$. $108 - 96 = U_t = 12$, $k = 96/12 = 8$, $n = 17$.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12-b01-b-hard-bt01-017
*orisinal | C6 | 5 langkah | jenis: rancang banyak suku agar mendekati jumlah tak hingga*

Deret $80 + 40 + 20 + 10 + \dots$ dijumlahkan sebanyak $n$ suku. Agar selisih antara jumlah tak hingganya dan $S_n$ kurang dari 0,1, banyak suku minimal yang diperlukan adalah ....

- A. 12  
  <sub>Salah: menambah satu suku cadangan tanpa dasar perhitungan</sub>
- **B. 11** ✅  
  <sub>Benar: $S_\infty = 160$ dan $S_\infty - S_n = \frac{160}{2^n} < 0{,}1$, yaitu $2^n > 1.600$ sehingga $n \ge 11$</sub>
- C. 14  
  <sub>Salah: memakai batas selisih 0,01, bukan 0,1</sub>
- D. 10  
  <sub>Salah: memakai selisih $\frac{80}{2^n}$ (lupa pembagi $1 - r$) sehingga $2^n > 800$</sub>

**Pembahasan:** $S_\infty = \frac{80}{1/2} = 160$. $S_n = 160(1 - 2^{-n})$ sehingga selisihnya $160 \cdot 2^{-n}$. Syarat $2^n > 1600$, $2^{10} = 1024 < 1600 < 2048 = 2^{11}$, jadi $n = 11$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12-b01-b-hard-bt01-018
*orisinal | C5 | 3 langkah | jenis: menyimpulkan sifat yang pasti dari $S_5 = 0$*

Pada suatu deret aritmetika diketahui $S_5 = 0$. Pernyataan yang pasti benar adalah ....

- A. $U_5 = 0$  
  <sub>Salah: pada $-2, -1, 0, 1, 2$ nilai $U_5 = 2 \ne 0$</sub>
- B. $b = 0$  
  <sub>Salah: hanya benar untuk deret nol, sedangkan $-2, -1, 0, 1, 2$ beda $1$</sub>
- C. $a = 0$  
  <sub>Salah: hanya benar untuk sebagian deret, contohnya $-2, -1, 0, 1, 2$ memiliki $a = -2$</sub>
- **D. $U_3 = 0$** ✅  
  <sub>Benar: $S_5 = \frac{5}{2}(U_1 + U_5) = \frac{5}{2} \cdot 2U_3 = 5U_3$, sehingga $U_3 = 0$</sub>

**Pembahasan:** Suku-suku simetris berjumlah $2U_3$, sehingga $S_5 = 5U_3 = 0$. Contoh $-2, -1, 0, 1, 2$ menyangkal tiga pilihan lain.
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12-b01-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: batas 'lebih dari' dan nilai tepat*

Deret $4 + 7 + 10 + 13 + \dots$ dijumlahkan suku demi suku. Jumlahnya pertama kali lebih dari 1.000 setelah dijumlahkan sebanyak ... suku.

- **A. 26** ✅  
  <sub>Benar: $S_n = \frac{n(3n+5)}{2}$; $S_{25} = 1.000$ (belum lebih), $S_{26} = 1.079$</sub>
- B. 25  
  <sub>Salah: $S_{25}$ tepat 1.000, bukan lebih dari 1.000</sub>
- C. 27  
  <sub>Salah: menambah satu suku lagi setelah melewati 1.000</sub>
- D. 24  
  <sub>Salah: $S_{24} = 924$ masih kurang dari 1.000</sub>

**Pembahasan:** $3n^2 + 5n = 2000$ dipenuhi $n = 25$. Karena yang diminta lebih dari 1.000, $n = 26$ ($S_{26} = 1.079$).
**Acuan:** siswa — siswa hal.41

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12-b01-b-hard-bt01-020
*orisinal | C6 | 5 langkah | jenis: dua nilai rasio, pilih yang sesuai syarat*

Deret geometri memiliki suku pertama 3 dan jumlah tiga suku pertamanya 63. Jika rasionya negatif, jumlah empat suku pertama deret tersebut adalah ....

- A. 312  
  <sub>Salah: salah tanda pada hasil akhir</sub>
- **B. -312** ✅  
  <sub>Benar: $3(1 + r + r^2) = 63 \Rightarrow r = 4$ atau $r = -5$; dengan $r = -5$: $3 - 15 + 75 - 375 = -312$</sub>
- C. 63  
  <sub>Salah: mengira jumlah empat suku sama dengan jumlah tiga suku</sub>
- D. 255  
  <sub>Salah: memakai $r = 4$ yang positif</sub>

**Pembahasan:** $r^2 + r - 20 = 0$ sehingga $r = 4$ atau $r = -5$. Rasio negatif: $S_4 = \frac{3(1 - 625)}{6} = -312$.
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
