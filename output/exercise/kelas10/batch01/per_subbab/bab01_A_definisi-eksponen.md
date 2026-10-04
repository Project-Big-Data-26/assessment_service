# Lembar koreksi — kelas10 SMA10-B1 subbab A: Definisi Eksponen

60 soal | easy 20, medium 20, hard 20 | variasi 18, orisinal 42

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b01-a-easy-bt01-001
*variasi (konteks) | C2 | 2 langkah | jenis: nilai pertumbuhan pada fase tertentu*

Seorang panitia mengirim undangan acara sekolah kepada 7 orang siswa. Setiap siswa yang menerima undangan meneruskannya kepada 7 siswa lain yang belum menerima, dan seterusnya. Banyak siswa yang menerima undangan pada tahap ke-5 adalah ....

- A. 117.649 orang  
  <sub>Salah: memakai tahap ke-6 ($7^6$)</sub>
- B. 78.125 orang  
  <sub>Salah: pokok dan pangkat tertukar ($5^7$)</sub>
- C. 35 orang  
  <sub>Salah: mengalikan 7 dengan 5 sebagai ganti memangkatkan</sub>
- **D. 16.807 orang** ✅  
  <sub>Benar: pada tahap ke-$n$ banyak penerima $7^n$, sehingga tahap ke-5 adalah $7^5 = 16.807$</sub>

**Pembahasan:** Tahap ke-1: 7, tahap ke-2: 49, tahap ke-3: 343, tahap ke-4: 2.401, sehingga tahap ke-5 adalah $7^5 = 16.807$.
**Acuan:** pretest — kelas10-b01-p0022-eksplorasi-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b01-a-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: rumus umum pertumbuhan eksponen*

Seorang siswa menyebarkan rumor kepada 5 temannya. Setiap teman yang menerima rumor menyebarkannya lagi kepada 5 orang lain, begitu seterusnya. Rumus banyak orang yang menerima rumor pada fase ke-$n$ adalah ....

- **A. $5^n$** ✅  
  <sub>Benar: setiap fase dikalikan 5 lagi, sehingga fase ke-$n$ adalah 5 dikalikan sebanyak $n$ faktor</sub>
- B. $5n$  
  <sub>Salah: mengira perkalian berulang sama dengan perkalian biasa</sub>
- C. $n^5$  
  <sub>Salah: pokok dan pangkat tertukar</sub>
- D. $5^{n-1}$  
  <sub>Salah: pangkat bergeser satu, padahal fase ke-1 sudah 5 orang</sub>

**Pembahasan:** Fase 1: 5, fase 2: 25, fase 3: 125, sehingga fase ke-$n$ adalah $5^n$.
**Acuan:** pretest — kelas10-b01-p0022-eksplorasi-21-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b01-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: fase minimal melewati batas*

Sebuah pesan berantai dikirim kepada 2 orang pada fase ke-1. Setiap penerima meneruskannya kepada 2 orang baru pada fase berikutnya, sehingga banyak penerima pada fase ke-$n$ adalah $2^n$. Pada fase ke berapakah banyak orang yang menerima pesan pertama kali melebihi 1.000 orang?

- **A. fase ke-10** ✅  
  <sub>Benar: $2^9 = 512$ belum melebihi 1.000, sedangkan $2^{10} = 1.024$ sudah melebihi</sub>
- B. fase ke-9  
  <sub>Salah: berhenti di 512 yang masih kurang dari 1.000</sub>
- C. fase ke-500  
  <sub>Salah: membagi 1.000 dengan 2 tanpa memakai pangkat</sub>
- D. fase ke-11  
  <sub>Salah: memilih fase setelah 1.024 padahal fase ke-10 sudah melebihi</sub>

**Pembahasan:** $2^9 = 512 < 1.000$ dan $2^{10} = 1.024 > 1.000$, jadi fase ke-10.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b01-a-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: nilai pertumbuhan pada fase tertentu*

Seekor bakteri membelah diri menjadi 2 bakteri setiap jam. Jika semua bakteri bertahan hidup dan pada awal terdapat 1 bakteri, banyak bakteri setelah 9 jam adalah ....

- A. 81 bakteri  
  <sub>Salah: pokok dan pangkat tertukar ($9^2$)</sub>
- **B. 512 bakteri** ✅  
  <sub>Benar: setelah 9 jam banyak bakteri $2^9 = 512$</sub>
- C. 256 bakteri  
  <sub>Salah: memakai pangkat 8 ($2^8$)</sub>
- D. 18 bakteri  
  <sub>Salah: mengalikan 2 dengan 9 sebagai ganti memangkatkan</sub>

**Pembahasan:** Setiap jam banyak bakteri dikalikan 2, sehingga setelah 9 jam adalah $2^9 = 512$.
**Acuan:** siswa — siswa hal.22 Ayo, Bekerja Sama

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b01-a-easy-bt01-005
*variasi (angka) | C1 | 1 langkah | jenis: perkalian berulang ke bentuk pangkat*

Perkalian berulang $9 \times 9 \times 9 \times 9 \times 9 \times 9 \times 9$ ditulis dengan bentuk pangkat ....

- A. $9^9$  
  <sub>Salah: pangkat disamakan dengan bilangan pokok</sub>
- B. $7^9$  
  <sub>Salah: pokok dan pangkat tertukar</sub>
- **C. $9^7$** ✅  
  <sub>Benar: bilangan 9 muncul sebagai faktor sebanyak 7 kali, sehingga ditulis $9^7$</sub>
- D. $9^6$  
  <sub>Salah: menghitung banyak tanda kali, bukan banyak faktor</sub>

**Pembahasan:** Ada 7 faktor 9, sehingga $9^7$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b01-a-easy-bt01-006
*variasi (angka) | C1 | 1 langkah | jenis: perkalian berulang ke bentuk pangkat*

Perkalian berulang $12 \times 12 \times 12 \times 12 \times 12 \times 12$ ditulis dengan bentuk pangkat ....

- A. $72$  
  <sub>Salah: mengalikan 12 dengan 6 sebagai ganti perkalian berulang</sub>
- **B. $12^6$** ✅  
  <sub>Benar: bilangan 12 muncul sebagai faktor sebanyak 6 kali</sub>
- C. $12^5$  
  <sub>Salah: menghitung banyak tanda kali, bukan banyak faktor</sub>
- D. $6^{12}$  
  <sub>Salah: pokok dan pangkat tertukar</sub>

**Pembahasan:** Ada 6 faktor 12, sehingga $12^6$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b01-a-easy-bt01-007
*variasi (konteks) | C1 | 1 langkah | jenis: perkalian berulang ke bentuk pangkat*

Perkalian berulang $y \times y \times y \times y \times y \times y \times y \times y \times y$ ditulis dengan bentuk pangkat ....

- A. $9^y$  
  <sub>Salah: pokok dan pangkat tertukar</sub>
- B. $y^8$  
  <sub>Salah: menghitung banyak tanda kali, bukan banyak faktor</sub>
- C. $9y$  
  <sub>Salah: mengira perkalian berulang sama dengan penjumlahan berulang</sub>
- **D. $y^9$** ✅  
  <sub>Benar: variabel $y$ muncul sebagai faktor sebanyak 9 kali</sub>

**Pembahasan:** Ada 9 faktor $y$, sehingga $y^9$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b01-a-easy-bt01-008
*variasi (angka) | C1 | 1 langkah | jenis: bentuk pangkat ke perkalian berulang*

Bentuk pangkat $8^5$ jika ditulis sebagai perkalian berulang adalah ....

- **A. $8 \times 8 \times 8 \times 8 \times 8$** ✅  
  <sub>Benar: $8^5$ berarti bilangan 8 dikalikan sebanyak 5 faktor</sub>
- B. $8 \times 8 \times 8 \times 8$  
  <sub>Salah: hanya menuliskan 4 faktor</sub>
- C. $8 \times 5$  
  <sub>Salah: mengira pangkat berarti dikalikan satu kali</sub>
- D. $5 \times 5 \times 5 \times 5 \times 5 \times 5 \times 5 \times 5$  
  <sub>Salah: bilangan pokok dan pangkat tertukar</sub>

**Pembahasan:** $8^5 = 8 \times 8 \times 8 \times 8 \times 8$ (5 faktor).
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b01-a-easy-bt01-009
*variasi (angka) | C2 | 1 langkah | jenis: nilai pertumbuhan pada fase tertentu*

Banyak penerima sebuah pesan pada fase ke-$n$ dinyatakan dengan rumus $4^n$. Gunakan rumus tersebut untuk menghitung jumlah orang pada fase ke-4.

- A. 16 orang  
  <sub>Salah: menghitung $4 \times 4$ saja</sub>
- B. 64 orang  
  <sub>Salah: memakai pangkat 3 ($4^3$)</sub>
- **C. 256 orang** ✅  
  <sub>Benar: $4^4 = 4 \times 4 \times 4 \times 4 = 256$</sub>
- D. 1.024 orang  
  <sub>Salah: memakai pangkat 5 ($4^5$)</sub>

**Pembahasan:** Substitusi $n = 4$: $4^4 = 256$.
**Acuan:** siswa — siswa hal.22 Ayo, Bekerja Sama

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b01-a-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: nilai pertumbuhan pada fase tertentu*

Sebuah video dibagikan oleh seorang pengguna kepada 10 orang pengikutnya. Setiap pengikut membagikannya lagi kepada 10 orang yang berbeda, dan seterusnya. Banyak orang yang menerima video pada fase ke-3 adalah ....

- A. 10.000 orang  
  <sub>Salah: memakai fase ke-4 ($10^4$)</sub>
- B. 100 orang  
  <sub>Salah: memakai fase ke-2 ($10^2$)</sub>
- C. 30 orang  
  <sub>Salah: mengalikan 10 dengan 3 sebagai ganti memangkatkan</sub>
- **D. 1.000 orang** ✅  
  <sub>Benar: fase ke-3 adalah $10^3 = 1.000$</sub>

**Pembahasan:** Fase 1: 10, fase 2: 100, fase 3: 1.000.
**Acuan:** pretest — kelas10-b01-p0022-eksplorasi-21-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b01-a-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: istilah eksponen*

Pada bentuk eksponen $7^4$, bilangan $7$ disebut ....

- A. hasil perpangkatan  
  <sub>Salah: mengira 7 adalah nilai hasil</sub>
- **B. bilangan pokok** ✅  
  <sub>Benar: bilangan yang diulang sebagai faktor disebut bilangan pokok</sub>
- C. pangkat  
  <sub>Salah: tertukar dengan bilangan 4</sub>
- D. bilangan berpangkat  
  <sub>Salah: bilangan berpangkat adalah seluruh bentuk $7^4$, bukan bilangan 7 saja</sub>

**Pembahasan:** Pada $a^n$, $a$ adalah bilangan pokok dan $n$ adalah pangkat; di sini bilangan pokok 7.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b01-a-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: arti notasi pangkat*

Jika $x$ adalah bilangan real, bentuk $x^6$ berarti ....

- A. hasil penjumlahan bilangan $x$ sebanyak 6 kali  
  <sub>Salah: mengira pangkat sama dengan penjumlahan berulang</sub>
- B. hasil kali bilangan 6 sebanyak $x$ faktor  
  <sub>Salah: bilangan pokok dan pangkat tertukar</sub>
- C. hasil kali $x$ dengan 6  
  <sub>Salah: mengira pangkat adalah perkalian biasa $6x$</sub>
- **D. hasil kali bilangan $x$ sebanyak 6 faktor** ✅  
  <sub>Benar: definisi $a^n$ adalah hasil kali $a$ sebanyak $n$ faktor</sub>

**Pembahasan:** $x^6 = x \times x \times x \times x \times x \times x$, yaitu $x$ sebanyak 6 faktor.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b01-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: nilai pangkat bulat positif*

Nilai dari $3^4$ adalah ....

- **A. $81$** ✅  
  <sub>Benar: $3^4 = 3 \times 3 \times 3 \times 3 = 81$</sub>
- B. $12$  
  <sub>Salah: mengalikan 3 dengan 4</sub>
- C. $64$  
  <sub>Salah: pokok dan pangkat tertukar ($4^3$)</sub>
- D. $243$  
  <sub>Salah: memakai pangkat 5 ($3^5$)</sub>

**Pembahasan:** $3^4 = 81$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b01-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: pangkat negatif*

Nilai dari $2^{-3}$ adalah ....

- A. $-6$  
  <sub>Salah: mengalikan 2 dengan -3</sub>
- B. $-8$  
  <sub>Salah: menganggap pangkat negatif membuat hasil negatif</sub>
- **C. $\frac{1}{8}$** ✅  
  <sub>Benar: $2^{-3} = \left(\frac{1}{2}\right)^3 = \frac{1}{8}$</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: mengalikan penyebut 2 dengan 3 sebagai ganti memangkatkan</sub>

**Pembahasan:** $2^{-3} = \frac{1}{2^3} = \frac{1}{8}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b01-a-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: pangkat negatif*

Menurut definisi eksponen, bentuk $7^{-3}$ sama dengan ....

- A. $-21$  
  <sub>Salah: mengalikan 7 dengan -3</sub>
- B. $\left(\frac{1}{3}\right)^7$  
  <sub>Salah: pokok dan pangkat tertukar</sub>
- **C. $\left(\frac{1}{7}\right)^3$** ✅  
  <sub>Benar: $a^{-n} = \left(\frac{1}{a}\right)^n$ dengan $a = 7$ dan $n = 3$</sub>
- D. $(-7)^3$  
  <sub>Salah: memindahkan tanda negatif ke bilangan pokok</sub>

**Pembahasan:** Definisi: $a^{-n} = \left(\frac{1}{a}\right)^n$, sehingga $7^{-3} = \left(\frac{1}{7}\right)^3$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b01-a-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: pangkat pecahan*

Nilai dari $125^{\frac{1}{3}}$ adalah ....

- **A. $5$** ✅  
  <sub>Benar: $125^{\frac{1}{3}} = p$ dengan $p^3 = 125$, yaitu $p = 5$</sub>
- B. $375$  
  <sub>Salah: mengalikan 125 dengan 3</sub>
- C. $\frac{125}{3}$  
  <sub>Salah: membagi 125 dengan 3</sub>
- D. $25$  
  <sub>Salah: mengira hasilnya $5^2$</sub>

**Pembahasan:** Karena $5^3 = 125$, maka $125^{\frac{1}{3}} = 5$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b01-a-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: nilai pangkat bulat positif*

Nilai dari $(-2)^5$ adalah ....

- A. $32$  
  <sub>Salah: mengabaikan tanda negatif</sub>
- **B. $-32$** ✅  
  <sub>Benar: bilangan negatif dikalikan sebanyak 5 faktor (ganjil) menghasilkan bilangan negatif, $2^5 = 32$</sub>
- C. $-10$  
  <sub>Salah: mengalikan -2 dengan 5</sub>
- D. $10$  
  <sub>Salah: mengalikan 2 dengan 5 dan mengabaikan tanda</sub>

**Pembahasan:** $(-2)^5 = (-2)(-2)(-2)(-2)(-2) = -32$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b01-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: pangkat pecahan*

Nilai dari $8^{\frac{2}{3}}$ adalah ....

- A. $2$  
  <sub>Salah: hanya menghitung $8^{\frac{1}{3}}$ dan lupa memangkatkan 2</sub>
- **B. $4$** ✅  
  <sub>Benar: $8^{\frac{2}{3}} = \left(8^{\frac{1}{3}}\right)^2 = 2^2 = 4$</sub>
- C. $\frac{64}{3}$  
  <sub>Salah: mengkuadratkan 8 lalu membagi dengan 3</sub>
- D. $\frac{16}{3}$  
  <sub>Salah: mengalikan 8 dengan $\frac{2}{3}$</sub>

**Pembahasan:** $8^{\frac{1}{3}} = 2$, lalu $2^2 = 4$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b01-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: syarat bilangan pokok*

Nilai $a$ berikut yang membuat bentuk $a^{-3}$ tidak terdefinisi adalah ....

- A. $1$  
  <sub>Salah: mengira bilangan 1 tidak boleh, padahal $1^{-3} = 1$</sub>
- B. $-1$  
  <sub>Salah: mengira bilangan negatif tidak boleh, padahal $(-1)^{-3} = -1$</sub>
- **C. $0$** ✅  
  <sub>Benar: definisi $a^{-n}$ mensyaratkan $a \neq 0$ karena $a^{-3} = \left(\frac{1}{a}\right)^3$ memuat pembagian oleh $a$</sub>
- D. $3$  
  <sub>Salah: mengira nilai yang sama dengan pangkat tidak boleh, padahal $3^{-3} = \frac{1}{27}$</sub>

**Pembahasan:** Syarat $a \neq 0$; hanya $a = 0$ yang melanggarnya.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b01-a-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: pangkat negatif*

Nilai dari $\left(\frac{2}{3}\right)^{-2}$ adalah ....

- A. $-\frac{4}{3}$  
  <sub>Salah: mengalikan $\frac{2}{3}$ dengan -2</sub>
- B. $\frac{4}{9}$  
  <sub>Salah: mengabaikan tanda negatif pada pangkat</sub>
- C. $-\frac{4}{9}$  
  <sub>Salah: menganggap pangkat negatif membuat hasil negatif</sub>
- **D. $\frac{9}{4}$** ✅  
  <sub>Benar: $\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$</sub>

**Pembahasan:** $\left(\frac{2}{3}\right)^{-2} = \left(\frac{3}{2}\right)^2 = \frac{9}{4}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b01-a-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: perkalian berulang bilangan negatif*

Hasil kali $(-2) \times (-2) \times (-2) \times (-2) \times (-2) \times (-2) \times (-2) \times (-2) \times (-2)$ ditulis dengan bentuk pangkat dan nilainya adalah ....

- **A. $(-2)^9 = -512$** ✅  
  <sub>Benar: ada 9 faktor $(-2)$; pangkat ganjil menghasilkan bilangan negatif, $2^9 = 512$</sub>
- B. $(-9)^2 = 81$  
  <sub>Salah: bilangan pokok dan pangkat tertukar</sub>
- C. $(-2)^9 = 512$  
  <sub>Salah: mengabaikan tanda negatif pada pangkat ganjil</sub>
- D. $(-2)^8 = 256$  
  <sub>Salah: menghitung banyak tanda kali, bukan banyak faktor</sub>

**Pembahasan:** Faktor $(-2)$ muncul 9 kali sehingga $(-2)^9$. Karena 9 ganjil, hasilnya negatif: $-2^9 = -512$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b01-a-medium-bt01-002
*variasi (konteks) | C3 | 2 langkah | jenis: perkalian berulang pecahan*

Nilai dari perkalian berulang $\frac{2}{5} \times \frac{2}{5} \times \frac{2}{5} \times \frac{2}{5}$ adalah ....

- A. $\frac{8}{625}$  
  <sub>Salah: mengalikan pembilang 2 dengan 4 sebagai ganti memangkatkan</sub>
- B. $\frac{8}{5}$  
  <sub>Salah: mengalikan pecahan $rac{2}{5}$ dengan 4</sub>
- C. $\frac{625}{16}$  
  <sub>Salah: pembilang dan penyebut tertukar</sub>
- **D. $\frac{16}{625}$** ✅  
  <sub>Benar: $\left(\frac{2}{5}\right)^4 = \frac{2^4}{5^4} = \frac{16}{625}$</sub>

**Pembahasan:** Ada 4 faktor $\frac{2}{5}$, sehingga $\left(\frac{2}{5}\right)^4 = \frac{16}{625}$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b01-a-medium-bt01-003
*variasi (konteks) | C3 | 3 langkah | jenis: total kumulatif fase*

Seorang siswa mengirim pesan kepada 3 orang pada fase ke-1. Setiap penerima meneruskannya kepada 3 orang baru pada fase berikutnya, dan seterusnya. Jumlah seluruh orang yang telah menerima pesan sampai dengan fase ke-4 adalah ....

- A. 81 orang  
  <sub>Salah: hanya menghitung penerima pada fase ke-4</sub>
- B. 243 orang  
  <sub>Salah: memakai fase ke-5 ($3^5$)</sub>
- **C. 120 orang** ✅  
  <sub>Benar: fase 1 sampai 4 menghasilkan $3 + 9 + 27 + 81 = 120$</sub>
- D. 363 orang  
  <sub>Salah: menjumlahkan sampai fase ke-5</sub>

**Pembahasan:** Penerima per fase: $3^1 = 3$, $3^2 = 9$, $3^3 = 27$, $3^4 = 81$. Totalnya $3 + 9 + 27 + 81 = 120$.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b01-a-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: pertumbuhan dengan nilai awal*

Sebuah laboratorium memulai biakan dengan 5 sel. Setiap jam, setiap sel membelah menjadi 3 sel. Jika tidak ada sel yang mati, banyak sel setelah 4 jam adalah ....

- A. 1.215 sel  
  <sub>Salah: memakai pangkat 5 ($5 \times 3^5$)</sub>
- **B. 405 sel** ✅  
  <sub>Benar: banyak sel $5 \times 3^4 = 5 \times 81 = 405$</sub>
- C. 50.625 sel  
  <sub>Salah: mengalikan 5 dengan 3 lebih dahulu lalu memangkatkan ($15^4$)</sub>
- D. 60 sel  
  <sub>Salah: mengalikan 5, 3, dan 4 sebagai ganti memangkatkan</sub>

**Pembahasan:** Setiap jam banyak sel dikalikan 3; setelah 4 jam faktor pengalinya $3^4 = 81$, sehingga $5 \times 81 = 405$.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b01-a-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: fase minimal melewati batas*

Sebuah pesan dikirim kepada 4 orang pada fase ke-1 dan setiap penerima meneruskannya kepada 4 orang baru, sehingga banyak penerima pada fase ke-$n$ adalah $4^n$. Pada fase ke berapakah banyak penerima pertama kali melebihi 10.000 orang?

- A. fase ke-6  
  <sub>Salah: berhenti di 4.096 yang masih kurang dari 10.000</sub>
- B. fase ke-2.500  
  <sub>Salah: membagi 10.000 dengan 4 tanpa memakai pangkat</sub>
- **C. fase ke-7** ✅  
  <sub>Benar: $4^6 = 4.096$ belum melebihi 10.000, sedangkan $4^7 = 16.384$ sudah melebihi</sub>
- D. fase ke-8  
  <sub>Salah: memilih fase setelah 16.384 padahal fase ke-7 sudah melebihi</sub>

**Pembahasan:** $4^5 = 1.024$, $4^6 = 4.096 < 10.000$, $4^7 = 16.384 > 10.000$, jadi fase ke-7.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b01-a-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: fase minimal melewati batas*

Sebuah koloni bakteri berawal dari 1 sel. Setiap jam, setiap sel menjadi 3 sel. Setelah berapa jam banyak sel pertama kali lebih dari 1.000.000?

- **A. 13 jam** ✅  
  <sub>Benar: $3^{12} = 531.441$ belum melebihi 1.000.000, sedangkan $3^{13} = 1.594.323$ sudah melebihi</sub>
- B. 11 jam  
  <sub>Salah: memakai 177.147 yang jauh di bawah 1.000.000</sub>
- C. 12 jam  
  <sub>Salah: berhenti di 531.441 yang masih kurang dari 1.000.000</sub>
- D. 14 jam  
  <sub>Salah: memilih jam setelah 1.594.323 padahal jam ke-13 sudah melebihi</sub>

**Pembahasan:** Setelah $n$ jam ada $3^n$ sel. $3^{12} = 531.441 < 10^6$ dan $3^{13} = 1.594.323 > 10^6$, jadi 13 jam.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b01-a-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: rumus umum dengan nilai awal*

Sebuah biakan diawali dengan 6 sel. Setiap jam, banyak sel menjadi 4 kali lipat banyak sel satu jam sebelumnya. Rumus banyak sel setelah $n$ jam adalah ....

- A. $6 \times 4n$  
  <sub>Salah: mengira perkalian berulang sama dengan perkalian biasa</sub>
- **B. $6 \times 4^n$** ✅  
  <sub>Benar: nilai awal 6 dikalikan faktor 4 sebanyak $n$ kali, yaitu $6 \times 4^n$</sub>
- C. $24^n$  
  <sub>Salah: mengalikan 6 dengan 4 lebih dahulu lalu memangkatkan</sub>
- D. $4 \times 6^n$  
  <sub>Salah: nilai awal dan faktor pengali tertukar</sub>

**Pembahasan:** Setelah 1 jam: $6 \times 4$; setelah 2 jam: $6 \times 4^2$; setelah $n$ jam: $6 \times 4^n$.
**Acuan:** siswa — siswa hal.22 Ayo, Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b01-a-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: perkalian berulang bentuk aljabar*

Hasil kali $(p+q) \times (p+q) \times (p+q) \times (p+q) \times (p+q) \times (p+q)$ ditulis dengan bentuk pangkat ....

- A. $p^6 + q^6$  
  <sub>Salah: memangkatkan tiap suku, padahal faktornya adalah jumlah $(p+q)$</sub>
- **B. $(p+q)^6$** ✅  
  <sub>Benar: faktor $(p+q)$ muncul 6 kali sehingga ditulis $(p+q)^6$</sub>
- C. $(p+q)^5$  
  <sub>Salah: menghitung banyak tanda kali, bukan banyak faktor</sub>
- D. $6(p+q)$  
  <sub>Salah: mengira perkalian berulang sama dengan perkalian biasa</sub>

**Pembahasan:** Ada 6 faktor $(p+q)$, sehingga $(p+q)^6$.
**Acuan:** siswa — siswa hal.20 Ayo, Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b01-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: ekspresi campuran pangkat negatif dan pecahan*

Nilai dari $2^{-2} + 27^{\frac{1}{3}}$ adalah ....

- A. $-1$  
  <sub>Salah: menganggap $2^{-2} = -4$ (pangkat negatif membuat hasil negatif)</sub>
- B. $\frac{37}{4}$  
  <sub>Salah: menghitung $27^{\frac{1}{3}}$ sebagai $27 \div 3 = 9$</sub>
- C. $\frac{3}{4}$  
  <sub>Salah: mengalikan $\frac{1}{4}$ dengan 3 sebagai ganti menjumlahkan</sub>
- **D. $\frac{13}{4}$** ✅  
  <sub>Benar: $2^{-2} = \frac{1}{4}$ dan $27^{\frac{1}{3}} = 3$ karena $3^3 = 27$, jumlahnya $\frac{13}{4}$</sub>

**Pembahasan:** $2^{-2} = \frac{1}{2^2} = \frac{1}{4}$; $27^{\frac{1}{3}} = 3$. Jadi $\frac{1}{4} + 3 = \frac{13}{4}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b01-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: membandingkan bilangan berpangkat*

Di antara bilangan berikut, yang bernilai terbesar adalah ....

- A. $10^3$  
  <sub>Salah: mengira bilangan pokok terbesar menghasilkan nilai terbesar</sub>
- B. $3^6$  
  <sub>Salah: menganggap pangkat 6 cukup besar tanpa menghitung</sub>
- C. $5^4$  
  <sub>Salah: menganggap pangkat dan pokok sedang menghasilkan nilai terbesar</sub>
- **D. $2^{10}$** ✅  
  <sub>Benar: $2^{10} = 1.024$, lebih besar daripada $10^3 = 1.000$, $3^6 = 729$, dan $5^4 = 625$</sub>

**Pembahasan:** $2^{10} = 1.024$; $3^6 = 729$; $5^4 = 625$; $10^3 = 1.000$. Yang terbesar adalah $2^{10}$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b01-a-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: membandingkan bilangan berpangkat*

Pernyataan yang benar di antara berikut ini adalah ....

- **A. $2^{-3} > 3^{-2}$** ✅  
  <sub>Benar: $2^{-3} = \frac{1}{8}$ dan $3^{-2} = \frac{1}{9}$, dan $\frac{1}{8} > \frac{1}{9}$</sub>
- B. $4^{-1} < 5^{-1}$  
  <sub>Salah: $\frac{1}{4} > \frac{1}{5}$; mengira pokok besar membuat nilai lebih besar</sub>
- C. $(-2)^{-3} > 2^{-3}$  
  <sub>Salah: $(-2)^{-3} = -\frac{1}{8}$ negatif sehingga lebih kecil dari $\frac{1}{8}$</sub>
- D. $\left(\frac{1}{2}\right)^{-2} < 2^{-2}$  
  <sub>Salah: $\left(\frac{1}{2}\right)^{-2} = 4$ lebih besar dari $2^{-2} = \frac{1}{4}$</sub>

**Pembahasan:** $2^{-3} = \frac{1}{8} > \frac{1}{9} = 3^{-2}$; ketiga pernyataan lain salah.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b01-a-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: nilai n dari persamaan pangkat*

Jika $5^{n-2} = 625$ dengan $n$ bilangan bulat, nilai $n$ adalah ....

- **A. $6$** ✅  
  <sub>Benar: $625 = 5^4$ sehingga $n - 2 = 4$ dan $n = 6$</sub>
- B. $7$  
  <sub>Salah: salah menghitung $625 = 5^5$</sub>
- C. $2$  
  <sub>Salah: menghitung $n = 4 - 2$ (salah arah operasi)</sub>
- D. $4$  
  <sub>Salah: menganggap $n = 4$ dan lupa mengurangkan 2 pada pangkat</sub>

**Pembahasan:** $5^4 = 625$, jadi $n - 2 = 4$, $n = 6$.
**Acuan:** siswa — siswa hal.22

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b01-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: nilai n dari persamaan pangkat*

Jika $\left(\frac{1}{3}\right)^{n} = 27$ dengan $n$ bilangan bulat, nilai $n$ adalah ....

- A. $-9$  
  <sub>Salah: membagi 27 dengan 3 dan memberi tanda negatif</sub>
- B. $9$  
  <sub>Salah: membagi 27 dengan 3</sub>
- C. $3$  
  <sub>Salah: mengabaikan tanda negatif pada pangkat</sub>
- **D. $-3$** ✅  
  <sub>Benar: $27 = 3^3 = \left(\frac{1}{3}\right)^{-3}$ menurut definisi $a^{-n} = \left(\frac{1}{a}\right)^n$, sehingga $n = -3$</sub>

**Pembahasan:** $\left(\frac{1}{3}\right)^{-3} = 3^3 = 27$, jadi $n = -3$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b01-a-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: nilai n dari persamaan pangkat*

Jika $8^{\frac{m}{3}} = 64$ dengan $m$ bilangan bulat positif, nilai $m$ adalah ....

- A. $18$  
  <sub>Salah: mengalikan 6 dengan 3</sub>
- B. $2$  
  <sub>Salah: menganggap $8^2 = 64$ dan mengabaikan penyebut 3</sub>
- **C. $6$** ✅  
  <sub>Benar: $8^{\frac{m}{3}} = \left(8^{\frac{1}{3}}\right)^m = 2^m = 64 = 2^6$ sehingga $m = 6$</sub>
- D. $24$  
  <sub>Salah: menyamakan $\frac{m}{3} = 8$ sebagai ganti pangkat dari $8^{\frac{1}{3}}$</sub>

**Pembahasan:** $8^{\frac{1}{3}} = 2$, sehingga $2^m = 64$ dan $m = 6$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b01-a-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: perbandingan antar fase*

Banyak penerima suatu pesan pada fase ke-$n$ dinyatakan dengan $4^n$. Banyak penerima pada fase ke-5 adalah ... kali banyak penerima pada fase ke-3.

- A. 2 kali  
  <sub>Salah: membagi banyak fase 5 dan 3 dengan pengurangan pangkat saja</sub>
- B. 8 kali  
  <sub>Salah: mengalikan 4 dengan selisih fase ($4 \times 2$)</sub>
- C. 64 kali  
  <sub>Salah: memakai banyak penerima fase ke-3 sebagai pengali</sub>
- **D. 16 kali** ✅  
  <sub>Benar: $4^5 = 1.024$ dan $4^3 = 64$, sehingga $1.024 \div 64 = 16$</sub>

**Pembahasan:** $\frac{4^5}{4^3} = \frac{1.024}{64} = 16$.
**Acuan:** siswa — siswa hal.22

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b01-a-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: substitusi variabel negatif*

Jika $x = -2$, nilai dari $x^3 - x^{-2}$ adalah ....

- A. $-\frac{31}{4}$  
  <sub>Salah: salah tanda saat mengurangkan, menghitung $-8 + \frac{1}{4}$</sub>
- B. $\frac{31}{4}$  
  <sub>Salah: menghitung $(-2)^3$ sebagai $8$</sub>
- **C. $-\frac{33}{4}$** ✅  
  <sub>Benar: $x^3 = -8$ dan $x^{-2} = \frac{1}{4}$, sehingga $-8 - \frac{1}{4} = -\frac{33}{4}$</sub>
- D. $-12$  
  <sub>Salah: menghitung $x^{-2}$ sebagai $4$ (mengabaikan kebalikan)</sub>

**Pembahasan:** $(-2)^3 = -8$; $(-2)^{-2} = \frac{1}{(-2)^2} = \frac{1}{4}$. Jadi $-8 - \frac{1}{4} = -\frac{33}{4}$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b01-a-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: ekspresi bertingkat pangkat negatif*

Nilai dari $\left(2^{-1} + 3^{-1}\right)^{-1}$ adalah ....

- A. $\frac{5}{6}$  
  <sub>Salah: lupa menerapkan pangkat $-1$ di luar kurung</sub>
- **B. $\frac{6}{5}$** ✅  
  <sub>Benar: $2^{-1} + 3^{-1} = \frac{5}{6}$ dan $\left(\frac{5}{6}\right)^{-1} = \frac{6}{5}$</sub>
- C. $5$  
  <sub>Salah: menjumlahkan 2 dan 3 tanpa memperhatikan pangkat negatif</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: mengubah menjadi $(2 + 3)^{-1}$, memangkatkan tiap suku dengan $-1$ terpisah dari penjumlahan</sub>

**Pembahasan:** $2^{-1} = \frac{1}{2}$, $3^{-1} = \frac{1}{3}$, jumlahnya $\frac{5}{6}$, lalu $\left(\frac{5}{6}\right)^{-1} = \frac{6}{5}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b01-a-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: pangkat pecahan*

Nilai dari $\left(\frac{4}{9}\right)^{\frac{3}{2}}$ adalah ....

- **A. $\frac{8}{27}$** ✅  
  <sub>Benar: $\left(\frac{4}{9}\right)^{\frac{1}{2}} = \frac{2}{3}$ lalu $\left(\frac{2}{3}\right)^3 = \frac{8}{27}$</sub>
- B. $\frac{16}{81}$  
  <sub>Salah: memangkatkan 2 saja tanpa menarik akar</sub>
- C. $\frac{27}{8}$  
  <sub>Salah: pembilang dan penyebut tertukar</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: hanya menghitung $\left(\frac{4}{9}\right)^{\frac{1}{2}}$ dan lupa memangkatkan 3</sub>

**Pembahasan:** $\left(\frac{4}{9}\right)^{\frac{1}{2}} = \frac{2}{3}$, kemudian $\left(\frac{2}{3}\right)^3 = \frac{8}{27}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b01-a-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: analisis kesalahan*

Seorang siswa menulis $(-2)^4 = -16$ dan $2^{-2} = -4$. Pernyataan yang benar tentang pekerjaan siswa tersebut adalah ....

- A. hanya jawaban kedua yang salah; nilai $2^{-2}$ yang benar adalah $\frac{1}{4}$  
  <sub>Salah: mengira $(-2)^4 = -16$ sudah benar</sub>
- **B. kedua jawaban salah; nilai yang benar adalah $16$ dan $\frac{1}{4}$** ✅  
  <sub>Benar: $(-2)^4 = 16$ (pangkat genap) dan $2^{-2} = \frac{1}{4}$</sub>
- C. hanya jawaban pertama yang salah; nilai $(-2)^4$ yang benar adalah $16$  
  <sub>Salah: mengira $2^{-2} = -4$ sudah benar</sub>
- D. kedua jawaban benar karena bilangan pokoknya negatif atau pangkatnya negatif  
  <sub>Salah: mengira tanda negatif selalu membuat hasil negatif</sub>

**Pembahasan:** $(-2)^4 = (-2)(-2)(-2)(-2) = 16$, bukan $-16$; $2^{-2} = \frac{1}{4}$, bukan $-4$. Keduanya salah.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b01-a-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: tanda bilangan pokok negatif*

Nilai dari $(-3)^4 - 3^4 + (-3)^3$ adalah ....

- A. $135$  
  <sub>Salah: menganggap $3^4 = -81$ lalu mengurangkan</sub>
- B. $-189$  
  <sub>Salah: menganggap $(-3)^4 = -81$</sub>
- **C. $-27$** ✅  
  <sub>Benar: $(-3)^4 = 81$, $3^4 = 81$, $(-3)^3 = -27$, sehingga $81 - 81 - 27 = -27$</sub>
- D. $27$  
  <sub>Salah: menganggap $(-3)^3 = 27$</sub>

**Pembahasan:** $81 - 81 + (-27) = -27$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b01-a-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim tentang pangkat*

Diketahui $a$ bilangan real dengan $a \neq 0$ dan $n$ bilangan bulat positif. Pernyataan yang benar untuk semua nilai $a$ tersebut adalah ....

- A. Nilai $-a^n$ selalu negatif  
  <sub>Salah: lupa bahwa $a^n$ dapat negatif, mis. $a = -2$, $n = 3$ memberi $-(-8) = 8$</sub>
- B. Jika $n$ genap, maka $(-a)^n = -a^n$  
  <sub>Salah: mengira tanda negatif selalu tersisa; padahal $(-2)^2 = 4 \neq -4$</sub>
- **C. Jika $n$ genap, maka $(-a)^n = a^n$** ✅  
  <sub>Benar: $(-a)^n$ memuat $n$ faktor $(-a)$; pada $n$ genap faktor negatif berpasangan sehingga hasilnya positif dan sama dengan $a^n$</sub>
- D. Jika $n$ ganjil, maka $(-a)^n = a^n$  
  <sub>Salah: mengira pangkat ganjil menghilangkan tanda; padahal $(-2)^3 = -8 \neq 8$</sub>

**Pembahasan:** Uji $a = 2$: $(-2)^2 = 4 = 2^2$ (genap benar), $(-2)^3 = -8 \neq 8$ (ganjil salah), $(-2)^2 = 4 \neq -4$. Untuk $a=-2$, $n=3$, $-a^n = 8 > 0$ sehingga klaim terakhir juga salah.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b01-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Seorang siswa mengklaim bahwa untuk setiap bilangan real $a$ berlaku $a^2 > a$. Nilai $a$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $6$  
  <sub>Salah: $6^2 = 36 > 6$ sehingga justru mendukung klaim</sub>
- B. $-4$  
  <sub>Salah: $(-4)^2 = 16 > -4$ sehingga justru mendukung klaim; mengira bilangan negatif pasti menyangkal</sub>
- C. $5$  
  <sub>Salah: $5^2 = 25 > 5$ sehingga justru mendukung klaim</sub>
- **D. $\frac{3}{4}$** ✅  
  <sub>Benar: $\left(\frac{3}{4}\right)^2 = \frac{9}{16}$ dan $\frac{9}{16} < \frac{3}{4}$ sehingga $a^2 > a$ tidak berlaku</sub>

**Pembahasan:** Contoh penyangkal harus membuat $a^2 \le a$. Hanya $\frac{3}{4}$ yang menghasilkan $\frac{9}{16} < \frac{3}{4}$; opsi lain memenuhi $a^2 > a$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b01-a-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Klaim: $(a+b)^2 = a^2 + b^2$ untuk semua bilangan real $a$ dan $b$. Pasangan $(a, b)$ berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- **A. $(4, 5)$** ✅  
  <sub>Benar: $(4+5)^2 = 81$ sedangkan $4^2 + 5^2 = 41$, nilainya berbeda</sub>
- B. $(7, 0)$  
  <sub>Salah: $(7+0)^2 = 49 = 7^2 + 0^2$ sehingga sama, bukan penyangkal</sub>
- C. $(0, 0)$  
  <sub>Salah: kedua ruas bernilai 0 sehingga sama, bukan penyangkal</sub>
- D. $(0, 6)$  
  <sub>Salah: $(0+6)^2 = 36 = 0^2 + 6^2$ sehingga sama, bukan penyangkal</sub>

**Pembahasan:** Hitung kedua ruas untuk tiap pasangan. Hanya $(4,5)$ memberi nilai berbeda ($81 \neq 41$); pasangan lain memuat angka 0 sehingga kedua ruas sama.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b01-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: perbandingan bilangan berpangkat besar*

Tanpa menghitung nilai lengkapnya, bilangan terbesar di antara $2^{100}$, $3^{64}$, $5^{40}$, dan $10^{30}$ adalah ....

- **A. $3^{64}$** ✅  
  <sub>Benar: tiap bilangan dapat ditulis sebagai bentuk pangkat 4: $(2^{25})^4$, $(3^{16})^4$, $(5^{10})^4$, $(10^{7,5})^4$; $2^{25} = 33.554.432$, $3^{16} = 43.046.721$, $5^{10} = 9.765.625$, dan $10^{7,5} \approx 31.622.776$, sehingga $3^{16}$ terbesar</sub>
- B. $5^{40}$  
  <sub>Salah: mengira kombinasi pokok dan pangkat yang sedang paling besar tanpa membandingkan</sub>
- C. $2^{100}$  
  <sub>Salah: mengira pangkat terbesar menghasilkan nilai terbesar</sub>
- D. $10^{30}$  
  <sub>Salah: mengira bilangan pokok terbesar menghasilkan nilai terbesar</sub>

**Pembahasan:** Semua pangkat habis dibagi 4. Bandingkan faktor ke-4: $2^{25}=33.554.432$, $3^{16}=43.046.721$, $5^{10}=9.765.625$, $10^{7,5} \approx 3,16 \times 10^7$. Yang terbesar adalah $3^{16}$, jadi $3^{64}$ terbesar.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b01-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: angka satuan dan banyak digit*

Angka satuan dari $7^{2026}$ adalah ....

- A. $1$  
  <sub>Salah: mengira 2026 habis dibagi 4 sehingga memilih angka satuan siklus terakhir</sub>
- B. $7$  
  <sub>Salah: mengira sisa bagi 2026 oleh 4 adalah 1</sub>
- **C. $9$** ✅  
  <sub>Benar: angka satuan $7^1, 7^2, 7^3, 7^4$ berturut-turut 7, 9, 3, 1 lalu berulang tiap 4 pangkat; $2026 = 4 \times 506 + 2$ sehingga sama dengan $7^2 = 49$, satuan 9</sub>
- D. $3$  
  <sub>Salah: mengira sisa bagi 2026 oleh 4 adalah 3</sub>

**Pembahasan:** Pola satuan $7^n$: 7, 9, 3, 1 (periode 4). $2026 \bmod 4 = 2$, jadi satuannya sama dengan $7^2 = 49$, yaitu 9.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b01-a-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: angka satuan dan banyak digit*

Angka satuan dari $3^{50} + 2^{50}$ adalah ....

- A. $1$  
  <sub>Salah: menganggap $2^{50}$ bersatuan 2 sehingga $9 + 2 = 11$</sub>
- B. $9$  
  <sub>Salah: hanya memakai satuan $3^{50}$</sub>
- C. $7$  
  <sub>Salah: menganggap $3^{50}$ bersatuan 3 dan $2^{50}$ bersatuan 4 (salah posisi siklus)</sub>
- **D. $3$** ✅  
  <sub>Benar: satuan $3^n$ berperiode 4 (3, 9, 7, 1) sehingga $3^{50}$ bersatuan 9; satuan $2^n$ berperiode 4 (2, 4, 8, 6) sehingga $2^{50}$ bersatuan 4; $9 + 4 = 13$, satuan 3</sub>

**Pembahasan:** $50 \bmod 4 = 2$. Satuan $3^{50}$ sama dengan $3^2 = 9$; satuan $2^{50}$ sama dengan $2^2 = 4$. Jumlahnya $9+4 = 13$, jadi satuan 3.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b01-a-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: angka satuan dan banyak digit*

Diketahui $2^{10} = 1.024$. Tanpa kalkulator, banyak digit bilangan $2^{40}$ adalah ....

- A. $14$ digit  
  <sub>Salah: menaksir nilai terlalu besar, mengira lebih dari $10^{13}$</sub>
- **B. $13$ digit** ✅  
  <sub>Benar: $2^{40}$ adalah hasil kali empat faktor $1.024$; $1.000^4 = 10^{12}$ dan $1.100^4 = 1,4641 \times 10^{12}$, sehingga $10^{12} < 2^{40} < 10^{13}$ dan bilangan itu berdigit 13</sub>
- C. $40$ digit  
  <sub>Salah: mengira banyak digit sama dengan pangkatnya</sub>
- D. $12$ digit  
  <sub>Salah: memperkirakan $2^{40} \approx 10^{12}$ lalu menghitung 12 digit; $10^{12}$ sendiri berdigit 13</sub>

**Pembahasan:** $2^{40} = (2^{10})^4$ dengan $1.000 < 1.024 < 1.100$. Maka $10^{12} < 2^{40} < 1,4641 \times 10^{12} < 10^{13}$. Bilangan di antara $10^{12}$ dan $10^{13}$ berdigit 13 (nilai sebenarnya $1.099.511.627.776$).
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b01-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: syarat n agar pernyataan benar*

Bilangan bulat positif $n$ yang memenuhi $(-5)^n + (-5)^{n+1} < 0$ adalah semua bilangan ....

- A. ganjil  
  <sub>Salah: menganggap bilangan negatif dihasilkan dari pangkat ganjil, padahal faktor $-4$ membalik tanda</sub>
- B. kelipatan 4  
  <sub>Salah: mengira kondisi hanya berlaku pada sebagian bilangan genap; $n = 2$ juga memenuhi</sub>
- C. bulat positif (semua $n$)  
  <sub>Salah: tidak memeriksa tanda $(-5)^n$</sub>
- **D. genap** ✅  
  <sub>Benar: $(-5)^n + (-5)^{n+1} = (-5)^n(1 + (-5)) = -4 \cdot (-5)^n$; hasilnya negatif jika $(-5)^n > 0$, yaitu jika $n$ genap</sub>

**Pembahasan:** Faktor bersama $(-5)^n$ memberi $-4 \cdot (-5)^n$. Pertidaksamaan terpenuhi jika $(-5)^n > 0$, yaitu $n$ genap. Uji $n=2$: $25 - 125 = -100 < 0$; $n=1$: $-5 + 25 = 20 > 0$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b01-a-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: syarat n agar pernyataan benar*

Banyak bilangan bulat $n$ dengan $1 \le n \le 20$ yang memenuhi $(-2)^n + 5 < 0$ adalah ....

- A. $8$  
  <sub>Salah: menganggap $2^3 = 8$ belum melebihi 5 sehingga $n = 3$ dikeluarkan</sub>
- **B. $9$** ✅  
  <sub>Benar: untuk $n$ genap $(-2)^n > 0$ sehingga tidak memenuhi; untuk $n$ ganjil, $-2^n + 5 < 0$ jika $2^n > 5$, yaitu $n \ge 3$; $n$ ganjil dari 3 sampai 19 ada 9</sub>
- C. $20$  
  <sub>Salah: mengira $(-2)^n$ selalu negatif</sub>
- D. $10$  
  <sub>Salah: menghitung semua $n$ ganjil termasuk $n = 1$, padahal $-2 + 5 = 3 > 0$</sub>

**Pembahasan:** $n$ genap: $2^n + 5 > 0$ (gagal). $n$ ganjil: $5 - 2^n < 0 \iff 2^n > 5$; $n=1$ gagal ($2<5$), $n=3,5,\dots,19$ memenuhi: 9 bilangan.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b01-a-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: syarat n agar pernyataan benar*

Bilangan bulat terkecil $n \ge 2$ yang memenuhi $2^n > n^3$ adalah ....

- A. $9$  
  <sub>Salah: mengira $2^9 = 512$ sudah melebihi $9^3 = 729$ (salah hitung)</sub>
- B. $11$  
  <sub>Salah: mengambil bilangan yang memenuhi tetapi bukan yang terkecil</sub>
- **C. $10$** ✅  
  <sub>Benar: untuk $n = 2, \dots, 9$ berlaku $2^n < n^3$ (mis. $2^9 = 512 < 729$), sedangkan $2^{10} = 1.024 > 1.000 = 10^3$</sub>
- D. $8$  
  <sub>Salah: menyamakan $2^3 = 8$ dengan $n = 8$ sehingga menyimpulkan 8 memenuhi</sub>

**Pembahasan:** Bandingkan: $n=8$: $256 < 512$; $n=9$: $512 < 729$; $n=10$: $1.024 > 1.000$. Jadi 10 adalah yang terkecil.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b01-a-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: syarat n agar pernyataan benar*

Bilangan bulat positif terkecil $n$ yang memenuhi $\left(\frac{3}{2}\right)^n > 100$ adalah ....

- A. $11$  
  <sub>Salah: $\left(\frac{3}{2}\right)^{11} \approx 86,5$ masih kurang dari 100</sub>
- B. $13$  
  <sub>Salah: memilih nilai yang memenuhi tetapi bukan yang terkecil</sub>
- C. $67$  
  <sub>Salah: membagi 100 dengan $\frac{3}{2}$ seperti pada perkalian biasa</sub>
- **D. $12$** ✅  
  <sub>Benar: $\left(\frac{3}{2}\right)^{11} = \frac{177.147}{2.048} \approx 86,5 < 100$ dan $\left(\frac{3}{2}\right)^{12} = \frac{531.441}{4.096} \approx 129,7 > 100$</sub>

**Pembahasan:** Pangkat $\frac{3}{2}$: $n=10 \to 57,7$; $n=11 \to 86,5$; $n=12 \to 129,7$. Yang pertama melebihi 100 adalah $n = 12$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b01-a-hard-bt01-012
*orisinal | C6 | 5 langkah | jenis: perancangan bentuk pangkat*

Banyak pasangan bilangan bulat $(a, n)$ dengan $n \ge 2$ yang memenuhi $a^n = 729$ adalah ....

- A. $3$ pasangan  
  <sub>Salah: hanya menghitung basis positif</sub>
- B. $6$ pasangan  
  <sub>Salah: memasukkan $(-9, 3)$, padahal $(-9)^3 = -729$</sub>
- C. $4$ pasangan  
  <sub>Salah: menghitung basis negatif hanya pada satu pangkat genap</sub>
- **D. $5$ pasangan** ✅  
  <sub>Benar: $729 = 3^6 = 9^3 = 27^2$; pangkat genap juga dapat berbasis negatif: $(-3)^6$ dan $(-27)^2$; pasangan: $(3,6), (-3,6), (9,3), (27,2), (-27,2)$</sub>

**Pembahasan:** $729 = 3^6$. Pangkat yang mungkin: 2 ($a=\pm 27$), 3 ($a=9$; $-9$ memberi $-729$), 6 ($a=\pm 3$). Totalnya 5 pasangan.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas10-b01-a-hard-bt01-013
*orisinal | C5 | 3 langkah | jenis: analisis kesalahan*

Seorang siswa menghitung $\left(-\frac{1}{2}\right)^{-3} = \left(-\frac{1}{2}\right)^{3} = -\frac{1}{8}$. Pernyataan yang benar tentang pekerjaan tersebut adalah ....

- **A. salah, karena pangkat negatif berarti kebalikan bilangan pokok; nilai yang benar adalah $-8$** ✅  
  <sub>Benar: $a^{-n} = \left(\frac{1}{a}\right)^n$, sehingga $\left(-\frac{1}{2}\right)^{-3} = (-2)^3 = -8$</sub>
- B. salah, nilai yang benar adalah $\frac{1}{8}$ karena pangkat negatif membuat hasil positif  
  <sub>Salah: mengira pangkat negatif selalu menghasilkan bilangan positif</sub>
- C. salah, nilai yang benar adalah $8$ karena tanda negatif hilang pada pangkat negatif  
  <sub>Salah: mengira pangkat negatif menghapus tanda bilangan pokok</sub>
- D. benar, karena pangkat ganjil menghasilkan bilangan negatif  
  <sub>Salah: hanya mengecek tanda dan tidak memeriksa bahwa pangkat negatif mengubah bilangan pokok menjadi kebalikannya</sub>

**Pembahasan:** Pangkat negatif membalik bilangan pokok: $\left(-\frac{1}{2}\right)^{-3} = (-2)^3 = -8$. Siswa hanya membuang tanda minus pada pangkat tanpa membalik bilangan pokok.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas10-b01-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: syarat keterdefinisian pangkat negatif*

Bentuk $\left(x^2 - 5x + 6\right)^{-2}$ tidak terdefinisi untuk beberapa bilangan real $x$. Jumlah semua nilai $x$ tersebut adalah ....

- A. $6$  
  <sub>Salah: mengalikan akar-akar, bukan menjumlahkan</sub>
- **B. $5$** ✅  
  <sub>Benar: definisi $a^{-n}$ mensyaratkan $a \neq 0$, sehingga bentuk tidak terdefinisi jika $x^2 - 5x + 6 = 0$, yaitu $x = 2$ atau $x = 3$; jumlahnya 5</sub>
- C. $1$  
  <sub>Salah: mengurangkan kedua akar</sub>
- D. $-5$  
  <sub>Salah: salah tanda pada jumlah akar ($x_1 + x_2 = -b/a$ dibaca terbalik)</sub>

**Pembahasan:** $a^{-n} = \frac{1}{a^n}$ hanya terdefinisi untuk $a \neq 0$. Syarat gagal: $x^2 - 5x + 6 = (x-2)(x-3) = 0$, jadi $x = 2$ atau $3$. Jumlahnya 5.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas10-b01-a-hard-bt01-015
*orisinal | C5 | 6 langkah | jenis: perbandingan bilangan berpangkat besar*

Di antara bilangan $25^{\frac{3}{2}}$, $9^{\frac{5}{2}}$, $4^{\frac{7}{2}}$, dan $27^{\frac{4}{3}}$, yang bernilai terbesar adalah ....

- **A. $9^{\frac{5}{2}}$** ✅  
  <sub>Benar: $25^{\frac{3}{2}} = 5^3 = 125$; $9^{\frac{5}{2}} = 3^5 = 243$; $4^{\frac{7}{2}} = 2^7 = 128$; $27^{\frac{4}{3}} = 3^4 = 81$; yang terbesar 243</sub>
- B. $27^{\frac{4}{3}}$  
  <sub>Salah: mengira bilangan pokok terbesar menghasilkan nilai terbesar</sub>
- C. $25^{\frac{3}{2}}$  
  <sub>Salah: salah menghitung $9^{\frac{5}{2}}$ sebagai $9^2 = 81$ sehingga 125 tampak terbesar</sub>
- D. $4^{\frac{7}{2}}$  
  <sub>Salah: mengira pangkat terbesar menghasilkan nilai terbesar</sub>

**Pembahasan:** Ubah tiap bentuk: $25^{3/2} = (\sqrt{25})^3 = 125$; $9^{5/2} = 3^5 = 243$; $4^{7/2} = 2^7 = 128$; $27^{4/3} = 3^4 = 81$. Terbesar adalah $9^{5/2}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas10-b01-a-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim tentang pangkat*

Nilai dari $(-1)^1 + (-1)^2 + (-1)^3 + \cdots + (-1)^{2025}$ adalah ....

- **A. $-1$** ✅  
  <sub>Benar: suku bergantian $-1, 1, -1, 1, \dots$; 2024 suku pertama berpasangan dan jumlahnya 0; suku terakhir $(-1)^{2025} = -1$</sub>
- B. $-2025$  
  <sub>Salah: mengira setiap suku bernilai $-1$</sub>
- C. $0$  
  <sub>Salah: mengira banyak suku genap sehingga semua suku berpasangan</sub>
- D. $1$  
  <sub>Salah: mengira suku terakhir bernilai positif</sub>

**Pembahasan:** Pangkat ganjil menghasilkan $-1$, pangkat genap $1$. Ada 2025 suku: 1012 suku $+1$ dan 1013 suku $-1$. Jumlahnya $1012 - 1013 = -1$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas10-b01-a-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: pola pertumbuhan dan klaim*

Sebuah pesan dikirim kepada 2 orang pada fase ke-1. Pada tiap fase berikutnya, setiap penerima meneruskannya kepada 2 orang baru, sehingga banyak penerima fase ke-$n$ adalah $2^n$. Untuk setiap $n \ge 2$, banyak penerima pada fase ke-$n$ dibandingkan jumlah seluruh penerima pada fase ke-1 sampai ke-$(n-1)$ adalah ....

- A. selalu sama banyak  
  <sub>Salah: menganggap fase ke-$n$ hanya menyamai jumlah seluruh fase sebelumnya</sub>
- B. selalu lebih banyak tepat 1 orang  
  <sub>Salah: ikut menghitung 1 orang pengirim awal pada jumlah sebelumnya</sub>
- **C. selalu lebih banyak tepat 2 orang** ✅  
  <sub>Benar: $n=2$: $4$ lawan $2$ (selisih 2); $n=3$: $8$ lawan $2+4 = 6$ (selisih 2); $n=4$: $16$ lawan $14$ (selisih 2); polanya $2 + 4 + \cdots + 2^{n-1} = 2^n - 2$</sub>
- D. selisihnya makin besar seiring bertambahnya $n$  
  <sub>Salah: mengira selisih mengikuti pertumbuhan $2^n$</sub>

**Pembahasan:** Jumlah fase sebelumnya: $n=2$: 2; $n=3$: 6; $n=4$: 14; $n=5$: 30. Selisihnya dengan $2^n$ selalu 2, sebab $2+4+\cdots+2^{n-1} = 2^n - 2$.
**Acuan:** siswa — siswa hal.22

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas10-b01-a-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal*

Himpunan semua bilangan real $x$ yang memenuhi $x^6 = 64$ adalah ....

- A. $\{-2\}$  
  <sub>Salah: menganggap pokok negatif saja yang memenuhi</sub>
- B. $\{2\}$  
  <sub>Salah: lupa bahwa bilangan pokok negatif pada pangkat genap juga memberi hasil positif</sub>
- **C. $\{-2,\ 2\}$** ✅  
  <sub>Benar: $2^6 = 64$ dan $(-2)^6 = 64$ karena pangkat genap menghilangkan tanda negatif; tidak ada bilangan lain yang berpangkat 6 sama dengan 64</sub>
- D. $\{-8,\ 8\}$  
  <sub>Salah: menarik akar kuadrat 64 saja tanpa memperhatikan pangkat 6</sub>

**Pembahasan:** $x^6 = 64 = 2^6$. Karena 6 genap, $(-2)^6 = 64$ juga. Jadi $x = 2$ atau $x = -2$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas10-b01-a-hard-bt01-019
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim tentang pangkat*

Diketahui $0 < a < 1$ dan $n$ bilangan bulat positif. Pernyataan yang benar adalah ....

- A. $a^{-n} < a^{n}$  
  <sub>Salah: membalik urutan nilai pangkat positif dan negatif</sub>
- **B. $a^n < 1 < a^{-n}$** ✅  
  <sub>Benar: hasil kali $n$ faktor $a$ yang kurang dari 1 bernilai kurang dari 1, sedangkan $a^{-n} = \left(\frac{1}{a}\right)^n$ dengan $\frac{1}{a} > 1$ bernilai lebih dari 1</sub>
- C. $a^{-n} < 1$  
  <sub>Salah: mengira pangkat negatif selalu memperkecil nilai</sub>
- D. $a^{n} > 1$  
  <sub>Salah: mengira pangkat positif selalu memperbesar nilai</sub>

**Pembahasan:** Uji $a = \frac{1}{2}$, $n=2$: $a^2 = \frac{1}{4} < 1$ dan $a^{-2} = 4 > 1$. Secara umum $0 < a^n < 1 < a^{-n}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas10-b01-a-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim tentang pangkat*

Diketahui $a < -1$ dan $n$ bilangan bulat positif ganjil. Pernyataan yang benar tentang $a^{-n}$ adalah ....

- A. $a^{-n} > 1$  
  <sub>Salah: mengira pangkat negatif selalu menghasilkan bilangan positif lebih dari 1</sub>
- **B. $-1 < a^{-n} < 0$** ✅  
  <sub>Benar: $a^n$ bernilai negatif dan $|a^n| > 1$, sehingga $a^{-n} = \frac{1}{a^n}$ negatif dengan nilai mutlak kurang dari 1</sub>
- C. $a^{-n} < -1$  
  <sub>Salah: mengira pangkat negatif memperbesar nilai mutlak</sub>
- D. $0 < a^{-n} < 1$  
  <sub>Salah: mengabaikan bahwa pangkat ganjil mempertahankan tanda negatif</sub>

**Pembahasan:** Uji $a=-2$, $n=3$: $(-2)^{-3} = -\frac{1}{8}$, yang terletak di antara $-1$ dan $0$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
