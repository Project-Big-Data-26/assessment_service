# Lembar koreksi — kelas11_tl SMA11L-B2 subbab B: Penjumlahan, Pengurangan, dan Perkalian Polinomial

56 soal | easy 20, medium 20, hard 16 | variasi 21, orisinal 35
> **Kapasitas kurang (hard): 16 dari kuota 20** — Hard subbab B (penjumlahan, pengurangan, perkalian polinomial) hanya menyediakan penalaran C5-C6 pada evaluasi klaim derajat, temuan kesalahan langkah, contoh penyangkal, dan perancangan polinomial; soal hitung langsung, parameter, atau soal sistem polinomial bersifat C3-C4 sehingga tidak dilabeli hard. Sisanya akan menjadi soal nyaris kembar.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b02-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: penjumlahan polinomial*

Sederhanakan bentuk berikut: $(6p^4q + pq - 9) + (5p^4q - pq^4 + 8)$

- A. $11p^4q + pq^4 + pq - 1$  
  <sub>Salah: tanda suku $-pq^4$ berubah jadi positif</sub>
- **B. $11p^4q - pq^4 + pq - 1$** ✅  
  <sub>Benar: $6p^4q + 5p^4q = 11p^4q$, suku $-pq^4$ dan $pq$ tidak punya pasangan, $-9 + 8 = -1$</sub>
- C. $p^4q - pq^4 + pq - 1$  
  <sub>Salah: $6 - 5 = 1$ (dikurangkan, bukan dijumlahkan)</sub>
- D. $11p^4q - pq^4 + pq - 17$  
  <sub>Salah: konstanta dijumlahkan sebagai $-9 - 8 = -17$</sub>

**Pembahasan:** Kelompokkan suku sejenis: $(6+5)p^4q = 11p^4q$; $-pq^4$ dan $pq$ tetap; konstanta $-9+8=-1$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b02-b-easy-bt01-002
*orisinal | C2 | 1 langkah | jenis: sifat operasi*

Penjumlahan $8x^2 + 5x^2 = (8 + 5)x^2$ menggunakan sifat ....

- A. komutatif penjumlahan  
  <sub>Salah: sifat komutatif hanya menukar urutan suku, tidak mengeluarkan faktor</sub>
- B. asosiatif penjumlahan  
  <sub>Salah: sifat asosiatif hanya mengubah pengelompokan, tidak mengeluarkan faktor</sub>
- **C. distributif perkalian terhadap penjumlahan** ✅  
  <sub>Benar: faktor $x^2$ dikeluarkan dari kedua suku, itulah sifat distributif</sub>
- D. identitas penjumlahan  
  <sub>Salah: sifat identitas melibatkan penambahan nol</sub>

**Pembahasan:** $8x^2 + 5x^2 = (8+5)x^2$ memanfaatkan sifat distributif.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b02-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: pengurangan polinomial*

Hasil dari $(9y^7 - 5y^4 + 7y - 8) - (4y^7 + 8y^4 - y^5 + 9)$ adalah ....

- A. $5y^7 - y^5 - 13y^4 + 7y - 17$  
  <sub>Salah: lupa mengubah tanda suku $-y^5$</sub>
- **B. $5y^7 + y^5 - 13y^4 + 7y - 17$** ✅  
  <sub>Benar: tanda tiap suku polinomial kedua berubah: $-(-y^5) = +y^5$, $-5y^4 - 8y^4 = -13y^4$, $-8 - 9 = -17$</sub>
- C. $5y^7 + y^5 - 3y^4 + 7y - 17$  
  <sub>Salah: $-5y^4 - 8y^4$ dihitung $-5y^4 + 8y^4$</sub>
- D. $5y^7 + y^5 - 13y^4 + 7y + 1$  
  <sub>Salah: konstanta $-8 - 9$ dihitung $-8 + 9 = 1$</sub>

**Pembahasan:** $9y^7 - 5y^4 + 7y - 8 - 4y^7 - 8y^4 + y^5 - 9 = 5y^7 + y^5 - 13y^4 + 7y - 17$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b02-b-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: mengenali suku sejenis*

Pasangan suku yang merupakan suku-suku sejenis adalah ....

- A. $6x^2y$ dan $-4xy^2$  
  <sub>Salah: eksponen $x$ dan $y$ tertukar sehingga bukan sejenis</sub>
- **B. $6x^2y$ dan $-4yx^2$** ✅  
  <sub>Benar: variabel $x$ dan $y$ sama dengan eksponen sama ($x^2$, $y$); urutan penulisan tidak berpengaruh</sub>
- C. $5x^3y$ dan $5x^3$  
  <sub>Salah: variabel berbeda (ada $y$ dan tidak ada $y$)</sub>
- D. $2x^4$ dan $2x^5$  
  <sub>Salah: variabel sama tetapi eksponen berbeda</sub>

**Pembahasan:** Suku sejenis punya variabel sama dengan eksponen sama; hanya $6x^2y$ dan $-4yx^2$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b02-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: pengurangan polinomial*

Bentuk paling sederhana dari $(7c^6 - c^5 + 9c - 15) - (c^6 + 8c^5 - c^4 - 5)$ adalah ....

- A. $6c^6 + 7c^5 + c^4 + 9c - 10$  
  <sub>Salah: $-c^5$ dan $+8c^5$ dijumlahkan langsung menjadi $+7c^5$</sub>
- B. $6c^6 - 9c^5 - c^4 + 9c - 10$  
  <sub>Salah: lupa mengubah tanda suku $-c^4$</sub>
- C. $6c^6 - 9c^5 + c^4 + 9c - 20$  
  <sub>Salah: lupa mengubah tanda konstanta $-5$ sehingga $-15 - 5$</sub>
- **D. $6c^6 - 9c^5 + c^4 + 9c - 10$** ✅  
  <sub>Benar: $7c^6 - c^6 = 6c^6$; $-c^5 - 8c^5 = -9c^5$; $-(-c^4) = +c^4$; $-15 + 5 = -10$</sub>

**Pembahasan:** $7c^6 - c^5 + 9c - 15 - c^6 - 8c^5 + c^4 + 5 = 6c^6 - 9c^5 + c^4 + 9c - 10$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b02-b-easy-bt01-006
*orisinal | C2 | 1 langkah | jenis: menghilangkan tanda kurung*

Bentuk $(7x - 2) - (4x - 9)$ tanpa tanda kurung adalah ....

- A. $7x + 2 - 4x + 9$  
  <sub>Salah: salah mengubah tanda $-2$ yang berada di kurung pertama</sub>
- B. $7x - 2 + 4x - 9$  
  <sub>Salah: tanda $4x$ tidak diubah sama sekali</sub>
- **C. $7x - 2 - 4x + 9$** ✅  
  <sub>Benar: tanda tiap suku di kurung kedua berubah: $-(4x) = -4x$ dan $-(-9) = +9$</sub>
- D. $7x - 2 - 4x - 9$  
  <sub>Salah: tanda $-9$ tidak diubah</sub>

**Pembahasan:** Kurung kedua didahului tanda minus sehingga semua tanda di dalamnya berbalik.
**Acuan:** siswa — siswa hal.79

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b02-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: penjumlahan polinomial*

Tentukan hasil dari $(6t^5 + 8t^4 - 7t + 15) + (9t^5 - 5t^4 + 6t - 10)$.

- A. $15t^5 + 13t^4 - t + 5$  
  <sub>Salah: $8 - 5$ dihitung $8 + 5$</sub>
- B. $15t^5 + 3t^4 - 13t + 5$  
  <sub>Salah: $-7 - 6$ (tanda $+6t$ diabaikan)</sub>
- **C. $15t^5 + 3t^4 - t + 5$** ✅  
  <sub>Benar: $6+9=15$, $8-5=3$, $-7+6=-1$, $15-10=5$</sub>
- D. $15t^5 + 3t^4 - t + 25$  
  <sub>Salah: $15 - 10$ dihitung $15 + 10$</sub>

**Pembahasan:** Gabungkan suku sejenis: $15t^5 + 3t^4 - t + 5$.
**Acuan:** siswa — siswa hal.78 Contoh 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b02-b-easy-bt01-008
*orisinal | C2 | 2 langkah | jenis: koefisien hasil penjumlahan*

Pada hasil penjumlahan $(5x^3 + 4x^2 - 7x) + (2x^3 - 9x^2 + x)$ yang sudah disederhanakan, koefisien $x^2$ adalah ....

- A. $5$  
  <sub>Salah: tanda hasil salah ($9 - 4$ dipakai sebagai positif)</sub>
- **B. $-5$** ✅  
  <sub>Benar: $4 + (-9) = -5$</sub>
- C. $-36$  
  <sub>Salah: $4$ dikalikan $-9$ bukan dijumlahkan</sub>
- D. $13$  
  <sub>Salah: $4 + 9$ (tanda $-9$ diabaikan)</sub>

**Pembahasan:** Suku $x^2$ hanya $4x^2$ dan $-9x^2$; jumlah koefisien $4 - 9 = -5$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b02-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: pengurangan polinomial*

Hasil dari $(w^6 - 8w^4 + 5w - 12) - (9w^5 + 7w^4 - w - 10)$ adalah ....

- A. $w^6 + 9w^5 - 15w^4 + 6w - 2$  
  <sub>Salah: tanda suku $9w^5$ tidak diubah</sub>
- B. $w^6 - 9w^5 - 15w^4 + 6w - 22$  
  <sub>Salah: konstanta $-12 - 10$ (tanda $-10$ tidak diubah)</sub>
- C. $w^6 - 9w^5 - 15w^4 + 4w - 2$  
  <sub>Salah: $5w - w$ (tanda $-w$ tidak diubah)</sub>
- **D. $w^6 - 9w^5 - 15w^4 + 6w - 2$** ✅  
  <sub>Benar: $-9w^5$, $-8w^4 - 7w^4 = -15w^4$, $5w + w = 6w$, $-12 + 10 = -2$</sub>

**Pembahasan:** $w^6 - 8w^4 + 5w - 12 - 9w^5 - 7w^4 + w + 10 = w^6 - 9w^5 - 15w^4 + 6w - 2$.
**Acuan:** siswa — siswa hal.78 Contoh 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b02-b-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: banyak suku hasil distribusi*

Polinomial $3x^3 - x^2 + 4x - 6$ dikalikan dengan $x^2 + 5$. Sebelum suku-suku sejenis digabung, banyak suku hasil perkalian tersebut adalah ....

- A. $4$  
  <sub>Salah: hanya menghitung banyak suku polinomial pertama</sub>
- B. $2$  
  <sub>Salah: hanya menghitung banyak suku polinomial kedua</sub>
- C. $6$  
  <sub>Salah: menjumlahkan banyak suku ($4 + 2$) alih-alih mengalikan</sub>
- **D. $8$** ✅  
  <sub>Benar: tiap dari 4 suku dikalikan dengan tiap dari 2 suku sehingga $4 \times 2 = 8$</sub>

**Pembahasan:** Distribusi: setiap suku polinomial pertama dikalikan setiap suku polinomial kedua, jadi $4 \times 2 = 8$ suku.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b02-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: perkalian dua polinomial*

Hasil perkalian $(x^3 + 4x - 6)(4x + 9)$ adalah ....

- A. $4x^4 + 9x^3 + 16x^2 + 60x - 54$  
  <sub>Salah: $-6 \cdot 4x = +24x$ (tanda salah) sehingga $36x + 24x$</sub>
- B. $4x^4 + 9x^3 + 16x^2 + 12x + 54$  
  <sub>Salah: $-6 \cdot 9 = +54$ (tanda salah)</sub>
- **C. $4x^4 + 9x^3 + 16x^2 + 12x - 54$** ✅  
  <sub>Benar: $4x^4 + 9x^3 + 16x^2 + 36x - 24x - 54$ dan $36x - 24x = 12x$</sub>
- D. $4x^4 + 9x^3 + 16x^2 + 36x - 54$  
  <sub>Salah: suku $-24x$ tidak ikut dijumlahkan</sub>

**Pembahasan:** Kalikan: $x^3(4x+9) + 4x(4x+9) - 6(4x+9) = 4x^4 + 9x^3 + 16x^2 + 36x - 24x - 54$.
**Acuan:** siswa — siswa hal.81 Contoh 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b02-b-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: model tabel luas*

| | $x$ | $4$ |
|---|---|---|
| $x$ | $x^2$ | $4x$ |
| $7$ | $7x$ | $28$ |

Tabel berikut memodelkan perkalian $(x + 7)(x + 4)$ sebagai luas daerah. Hasil kali tersebut dalam bentuk paling sederhana adalah ....

- A. $x^2 + 11x + 11$  
  <sub>Salah: konstanta $4 + 7$ dijumlahkan, bukan dikalikan</sub>
- B. $x^2 + 28$  
  <sub>Salah: suku $4x$ dan $7x$ terlewat</sub>
- C. $x^2 + 3x + 28$  
  <sub>Salah: $7x - 4x$ (dikurangkan, bukan dijumlahkan)</sub>
- **D. $x^2 + 11x + 28$** ✅  
  <sub>Benar: jumlah seluruh sel: $x^2 + 4x + 7x + 28$, lalu $4x + 7x = 11x$</sub>

**Pembahasan:** Jumlah semua sel tabel: $x^2 + 4x + 7x + 28 = x^2 + 11x + 28$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b02-b-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: perkalian dua polinomial*

Tentukan hasil perkalian $(4y^2 - 7y + 9)(3y - 8)$.

- A. $12y^3 - 11y^2 + 83y - 72$  
  <sub>Salah: $-32y^2 + 21y^2$ (tanda $-7y \cdot 3y$ salah)</sub>
- **B. $12y^3 - 53y^2 + 83y - 72$** ✅  
  <sub>Benar: $12y^3 - 32y^2 - 21y^2 + 56y + 27y - 72$</sub>
- C. $12y^3 - 53y^2 + 83y + 72$  
  <sub>Salah: $9 \cdot (-8) = +72$</sub>
- D. $12y^3 - 53y^2 + 29y - 72$  
  <sub>Salah: $56y - 27y$ (tanda salah)</sub>

**Pembahasan:** $(4y^2 - 7y + 9)(3y - 8) = 12y^3 - 32y^2 - 21y^2 + 56y + 27y - 72 = 12y^3 - 53y^2 + 83y - 72$.
**Acuan:** siswa — siswa hal.81 Contoh 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b02-b-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: pengertian pengurangan polinomial*

Pernyataan yang benar tentang cara menghitung $P(x) - Q(x)$ adalah ....

- A. hanya suku pertama $Q(x)$ yang diubah tandanya  
  <sub>Salah: tanda hanya satu suku diubah, seharusnya semua suku</sub>
- B. setiap suku $P(x)$ diubah tandanya, lalu dijumlahkan dengan $Q(x)$  
  <sub>Salah: itu menghasilkan $-P(x) + Q(x)$, yaitu lawan dari hasil yang benar</sub>
- C. tanda semua suku $Q(x)$ dipertahankan, lalu dijumlahkan dengan $P(x)$  
  <sub>Salah: itu sama dengan $P(x) + Q(x)$, bukan pengurangan</sub>
- **D. setiap suku $Q(x)$ diubah tandanya, lalu hasilnya dijumlahkan dengan $P(x)$** ✅  
  <sub>Benar: pengurangan sama dengan penjumlahan dengan lawan dari $Q(x)$</sub>

**Pembahasan:** $P(x) - Q(x) = P(x) + (-Q(x))$, jadi semua suku $Q(x)$ berubah tanda.
**Acuan:** siswa — siswa hal.79

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b02-b-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: perkalian dua polinomial*

Tentukan hasil dari $(5u^4 - u + 6)(u^5 - 7)$.

- **A. $5u^9 - u^6 + 6u^5 - 35u^4 + 7u - 42$** ✅  
  <sub>Benar: $5u^4 \cdot u^5 = 5u^9$, $-u \cdot u^5 = -u^6$, $6u^5$, $-35u^4$, $+7u$, $-42$</sub>
- B. $5u^9 + u^6 + 6u^5 - 35u^4 + 7u - 42$  
  <sub>Salah: $-u \cdot u^5$ dihitung $+u^6$</sub>
- C. $5u^9 - u^6 + 6u^5 - 35u^4 - 7u - 42$  
  <sub>Salah: $-u \cdot (-7) = -7u$ (tanda salah)</sub>
- D. $5u^9 - u^6 + 6u^5 - 35u^4 + 7u + 42$  
  <sub>Salah: $6 \cdot (-7) = +42$</sub>

**Pembahasan:** Kalikan tiap suku $5u^4 - u + 6$ dengan $u^5$ lalu dengan $-7$ dan gabungkan.
**Acuan:** siswa — siswa hal.81 Mari Mencoba 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b02-b-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: bentuk distribusi perkalian*

Bentuk $(x + 4)(x^2 - 2x + 3)$ sama dengan ....

- **A. $x(x^2 - 2x + 3) + 4(x^2 - 2x + 3)$** ✅  
  <sub>Benar: tiap suku $x$ dan $4$ dari faktor pertama dikalikan dengan seluruh faktor kedua</sub>
- B. $x(x^2 - 2x + 3) + 4$  
  <sub>Salah: $4$ tidak dikalikan ke seluruh faktor kedua</sub>
- C. $x^2 - 2x + 3 + 4(x^2 - 2x + 3)$  
  <sub>Salah: faktor $x$ tidak dikalikan ke faktor kedua</sub>
- D. $x(x^2 - 2x + 3) - 4(x^2 - 2x + 3)$  
  <sub>Salah: tanda $+4$ berubah menjadi minus</sub>

**Pembahasan:** Sifat distributif: $(x+4)Q = xQ + 4Q$ dengan $Q = x^2 - 2x + 3$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b02-b-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: perkalian dua polinomial*

Hasil perkalian $(4p - 7q + 8)(p + 6q - 9)$ adalah ....

- **A. $4p^2 + 17pq - 42q^2 - 28p + 111q - 72$** ✅  
  <sub>Benar: $4p^2 + 24pq - 36p - 7pq - 42q^2 + 63q + 8p + 48q - 72$</sub>
- B. $4p^2 + 17pq - 42q^2 - 28p + 111q + 72$  
  <sub>Salah: $8 \cdot (-9) = +72$</sub>
- C. $4p^2 + 31pq - 42q^2 - 28p + 111q - 72$  
  <sub>Salah: $24pq + 7pq$ (tanda $-7pq$ diabaikan)</sub>
- D. $4p^2 + 17pq + 42q^2 - 28p + 111q - 72$  
  <sub>Salah: $-7q \cdot 6q = +42q^2$</sub>

**Pembahasan:** Distribusikan tiap suku: $24pq - 7pq = 17pq$, $-36p + 8p = -28p$, $63q + 48q = 111q$.
**Acuan:** siswa — siswa hal.83 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b02-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: suku konstan hasil kali*

Suku konstan pada hasil perkalian $(2x + 3)(x^2 - 4x + 7)$ adalah ....

- A. $-12$  
  <sub>Salah: $3 \times (-4)$, memakai koefisien $x$ pada faktor kedua</sub>
- B. $14$  
  <sub>Salah: $2 \times 7$, memakai koefisien $x$ bukan konstanta</sub>
- **C. $21$** ✅  
  <sub>Benar: suku konstan hanya dari $3 \times 7 = 21$</sub>
- D. $10$  
  <sub>Salah: konstanta $3 + 7$ dijumlahkan</sub>

**Pembahasan:** Konstan hasil kali = konstan pertama $\times$ konstan kedua = $3 \times 7 = 21$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b02-b-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: perkalian dua polinomial*

Hasil dari $(x + 8)(x^3 - 4x + 7)$ adalah ....

- **A. $x^4 + 8x^3 - 4x^2 - 25x + 56$** ✅  
  <sub>Benar: $x^4 - 4x^2 + 7x + 8x^3 - 32x + 56$, dengan $7x - 32x = -25x$</sub>
- B. $x^4 + 8x^3 - 4x^2 - 25x + 15$  
  <sub>Salah: konstanta $8 + 7$ (dijumlah, bukan dikali)</sub>
- C. $x^4 + 8x^3 - 25x + 56$  
  <sub>Salah: suku $-4x^2$ terlewat</sub>
- D. $x^4 + 8x^3 - 4x^2 - 39x + 56$  
  <sub>Salah: $-32x - 7x$ (tanda $+7x$ salah)</sub>

**Pembahasan:** $(x+8)(x^3 - 4x + 7) = x^4 + 8x^3 - 4x^2 - 32x + 7x + 56 = x^4 + 8x^3 - 4x^2 - 25x + 56$.
**Acuan:** siswa — siswa hal.81 Eksplorasi Mengalikan Dua Polinomial

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b02-b-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: penjumlahan polinomial*

Jumlahkan $(7k^3m - 4km^3 + 8)$ dengan $(5k^3m + 9km^3 - 6)$.

- **A. $12k^3m + 5km^3 + 2$** ✅  
  <sub>Benar: $7+5=12$, $-4+9=5$, $8-6=2$</sub>
- B. $2k^3m + 5km^3 + 2$  
  <sub>Salah: $7 - 5$ (dikurangkan, bukan dijumlahkan)</sub>
- C. $12k^3m + 5km^3 + 14$  
  <sub>Salah: $8 - (-6) = 14$</sub>
- D. $12k^3m - 13km^3 + 2$  
  <sub>Salah: $-4 - 9$ (tanda $+9km^3$ diabaikan)</sub>

**Pembahasan:** Suku sejenis: $12k^3m + 5km^3 + 2$.
**Acuan:** siswa — siswa hal.79 Mari Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b02-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: penjumlahan polinomial dua variabel*

Sederhanakan bentuk berikut: (8a^4b - 5ab^3 + 6a^2 - 9) + (-3a^4b + 5ab^3 - 4a^2 + 7)

- A. $5a^4b - 10ab^3 + 2a^2 - 2$  
  <sub>Salah: tanda suku $5ab^3$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- B. $5a^4b + 2a^2 - 16$  
  <sub>Salah: tanda suku $7$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- C. $5a^4b + 10a^2 - 2$  
  <sub>Salah: tanda suku $-4a^2$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- **D. $5a^4b + 2a^2 - 2$** ✅  
  <sub>Benar: suku $-5ab^3$ dan $5ab^3$ saling meniadakan; $8a^4b - 3a^4b = 5a^4b$; $6a^2 - 4a^2 = 2a^2$; $-9 + 7 = -2$</sub>

**Pembahasan:** Kelompokkan suku sejenis: $5a^4b + 2a^2 - 2$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b02-b-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: penjumlahan polinomial dua variabel*

Sederhanakan bentuk berikut: (9p^2q^3 - 4p^3 + 8pq - 11) + (-6p^2q^3 + 5p^3 + 3pq^2 + 4)

- A. $3p^2q^3 + p^3 + 11pq^2 - 7$  
  <sub>Salah: $8pq$ dan $3pq^2$ digabung padahal bukan suku sejenis (eksponen $q$ berbeda)</sub>
- B. $3p^2q^3 - 9p^3 + 3pq^2 + 8pq - 7$  
  <sub>Salah: tanda suku $5p^3$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- **C. $3p^2q^3 + p^3 + 3pq^2 + 8pq - 7$** ✅  
  <sub>Benar: $9p^2q^3 - 6p^2q^3 = 3p^2q^3$; $-4p^3 + 5p^3 = p^3$; $8pq$ dan $3pq^2$ tidak sejenis; $-11 + 4 = -7$</sub>
- D. $15p^2q^3 + p^3 + 3pq^2 + 8pq - 7$  
  <sub>Salah: tanda suku $-6p^2q^3$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>

**Pembahasan:** Pasangkan suku sejenis: $3p^2q^3 + p^3 + 3pq^2 + 8pq - 7$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b02-b-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: pengurangan polinomial*

Hasil dari (8r^6 - 5r^4 + 6r^2 + 9r - 14) - (3r^6 - 5r^4 - 7r^3 + 6r^2 + 4) adalah ....

- A. $5r^6 + 7r^3 + 9r - 10$  
  <sub>Salah: tanda suku $4$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- B. $11r^6 + 7r^3 + 9r - 18$  
  <sub>Salah: tanda suku $3r^6$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- C. $5r^6 - 7r^3 + 9r - 18$  
  <sub>Salah: tanda suku $-7r^3$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- **D. $5r^6 + 7r^3 + 9r - 18$** ✅  
  <sub>Benar: $-5r^4 - (-5r^4) = 0$ dan $6r^2 - 6r^2 = 0$ habis; $-(-7r^3) = +7r^3$; $-14 - 4 = -18$</sub>

**Pembahasan:** Hilangkan kurung dengan membalik tanda semua suku pengurang, lalu gabungkan suku sejenis: $5r^6 + 7r^3 + 9r - 18$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b02-b-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: pengurangan polinomial*

Hasil dari (11s^5 - 6s^3 + s^2 - 8s + 13) - (4s^5 + 9s^3 - 5s^2 + 8s - 6) adalah ....

- **A. $7s^5 - 15s^3 + 6s^2 - 16s + 19$** ✅  
  <sub>Benar: $11s^5 - 4s^5 = 7s^5$; $-6s^3 - 9s^3 = -15s^3$; $s^2 + 5s^2 = 6s^2$; $-8s - 8s = -16s$; $13 + 6 = 19$</sub>
- B. $7s^5 - 15s^3 - 4s^2 - 16s + 19$  
  <sub>Salah: tanda suku $-5s^2$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- C. $7s^5 + 3s^3 + 6s^2 - 16s + 19$  
  <sub>Salah: tanda suku $9s^3$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- D. $7s^5 - 15s^3 + 6s^2 - 16s + 7$  
  <sub>Salah: tanda suku $-6$ pada polinomial kedua tidak diubah saat dikurangkan</sub>

**Pembahasan:** Hilangkan kurung dengan membalik tanda semua suku pengurang, lalu gabungkan suku sejenis: $7s^5 - 15s^3 + 6s^2 - 16s + 19$.
**Acuan:** pretest — kelas11_tl-b02-p0082-latihan-b-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b02-b-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: penjumlahan polinomial satu variabel*

Tentukan hasil dari: (7h^5 - 9h^3 + 4h - 10) + (-7h^5 + 6h^4 + 9h^3 - h + 16)

- **A. $6h^4 + 3h + 6$** ✅  
  <sub>Benar: $7h^5 - 7h^5 = 0$ dan $-9h^3 + 9h^3 = 0$ habis; $6h^4$ tanpa pasangan; $4h - h = 3h$; $-10 + 16 = 6$</sub>
- B. $6h^4 + 3h - 26$  
  <sub>Salah: tanda suku $16$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- C. $14h^5 + 6h^4 + 3h + 6$  
  <sub>Salah: tanda suku $-7h^5$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- D. $6h^4 + 5h + 6$  
  <sub>Salah: tanda suku $-h$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>

**Pembahasan:** Kelompokkan suku sejenis: $6h^4 + 3h + 6$.
**Acuan:** siswa — siswa hal.78 Contoh 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b02-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: pengurangan polinomial*

Tentukan hasil dari: (8z^7 + 9z^4 - 6z^3 + 11z - 5) - (5z^7 - 7z^6 + 9z^4 + 12z^3 - 13)

- A. $3z^7 + 7z^6 - 18z^3 + 11z - 18$  
  <sub>Salah: tanda suku $-13$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- **B. $3z^7 + 7z^6 - 18z^3 + 11z + 8$** ✅  
  <sub>Benar: $8z^7 - 5z^7 = 3z^7$; $-(-7z^6) = +7z^6$; $9z^4 - 9z^4 = 0$; $-6z^3 - 12z^3 = -18z^3$; $-5 + 13 = 8$</sub>
- C. $3z^7 - 7z^6 - 18z^3 + 11z + 8$  
  <sub>Salah: tanda suku $-7z^6$ pada polinomial kedua tidak diubah saat dikurangkan</sub>
- D. $3z^7 + 7z^6 + 6z^3 + 11z + 8$  
  <sub>Salah: tanda suku $12z^3$ pada polinomial kedua tidak diubah saat dikurangkan</sub>

**Pembahasan:** Hilangkan kurung dengan membalik tanda semua suku pengurang, lalu gabungkan suku sejenis: $3z^7 + 7z^6 - 18z^3 + 11z + 8$.
**Acuan:** siswa — siswa hal.78 Contoh 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b02-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: perkalian binomial dengan polinomial bersuku hilang*

Tentukan hasil perkalian (4m^3 - 7m + 6)(5m - 8).

- A. $20m^4 - 32m^3 - 35m^2 + 86m + 48$  
  <sub>Salah: hasil kali $-48$ ditulis dengan tanda yang berlawanan</sub>
- B. $20m^4 - 32m^3 + 35m^2 + 86m - 48$  
  <sub>Salah: hasil kali $-35m^2$ ditulis dengan tanda yang berlawanan</sub>
- **C. $20m^4 - 32m^3 - 35m^2 + 86m - 48$** ✅  
  <sub>Benar: $20m^4 - 32m^3 - 35m^2 + 56m + 30m - 48$, lalu $56m + 30m = 86m$</sub>
- D. $20m^4 - 32m^3 - 35m^2 - 26m - 48$  
  <sub>Salah: hasil kali $56m$ ditulis dengan tanda yang berlawanan</sub>

**Pembahasan:** Kalikan tiap suku faktor pertama dengan tiap suku faktor kedua, lalu gabungkan suku sejenis: $20m^4 - 32m^3 - 35m^2 + 86m - 48$.
**Acuan:** siswa — siswa hal.81 Contoh 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b02-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: perkalian polinomial pangkat tinggi*

Tentukan hasil dari (2n^3 - 5n^2 + 9)(n^2 - 6).

- A. $2n^5 - 5n^4 - 12n^3 + 39n^2 + 54$  
  <sub>Salah: hasil kali $-54$ ditulis dengan tanda yang berlawanan</sub>
- **B. $2n^5 - 5n^4 - 12n^3 + 39n^2 - 54$** ✅  
  <sub>Benar: $2n^5 - 12n^3 - 5n^4 + 30n^2 + 9n^2 - 54$, lalu $30n^2 + 9n^2 = 39n^2$</sub>
- C. $2n^5 - 5n^4 + 12n^3 + 39n^2 - 54$  
  <sub>Salah: hasil kali $-12n^3$ ditulis dengan tanda yang berlawanan</sub>
- D. $2n^5 - 5n^4 - 12n^3 - 21n^2 - 54$  
  <sub>Salah: hasil kali $30n^2$ ditulis dengan tanda yang berlawanan</sub>

**Pembahasan:** Kalikan tiap suku faktor pertama dengan tiap suku faktor kedua, lalu gabungkan suku sejenis: $2n^5 - 5n^4 - 12n^3 + 39n^2 - 54$.
**Acuan:** siswa — siswa hal.81 Mari Mencoba 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b02-b-medium-bt01-009
*variasi (angka) | C3 | 4 langkah | jenis: perkalian dua trinomial tiga variabel*

Tentukan hasil perkalian (6a - 7b + 4c)(5a + 3b - 8c).

- A. $30a^2 - 17ab - 28ac + 21b^2 + 68bc - 32c^2$  
  <sub>Salah: hasil kali $-21b^2$ ditulis dengan tanda yang berlawanan</sub>
- B. $30a^2 - 17ab - 68ac - 21b^2 + 68bc - 32c^2$  
  <sub>Salah: hasil kali $20ac$ ditulis dengan tanda yang berlawanan</sub>
- **C. $30a^2 - 17ab - 28ac - 21b^2 + 68bc - 32c^2$** ✅  
  <sub>Benar: sembilan hasil kali parsial dikalikan satu per satu, lalu suku sejenis ($ab$, $ac$, $bc$) digabung sehingga diperoleh $30a^2 - 17ab - 28ac - 21b^2 + 68bc - 32c^2$</sub>
- D. $30a^2 - 17ab - 28ac - 21b^2 - 44bc - 32c^2$  
  <sub>Salah: hasil kali $56bc$ ditulis dengan tanda yang berlawanan</sub>

**Pembahasan:** Kalikan tiap suku, lalu gabungkan: $30a^2 - 17ab - 28ac - 21b^2 + 68bc - 32c^2$.
**Acuan:** siswa — siswa hal.83 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b02-b-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: penjumlahan polinomial tiga variabel*

Jumlahkan (8x^2y - 5yz^2 + 9xz) dengan (-3x^2y + 4yz^2 - xz - 6).

- **A. $5x^2y - yz^2 + 8xz - 6$** ✅  
  <sub>Benar: $8x^2y - 3x^2y = 5x^2y$; $-5yz^2 + 4yz^2 = -yz^2$; $9xz - xz = 8xz$; konstanta $-6$ tanpa pasangan</sub>
- B. $5x^2y - 9yz^2 + 8xz - 6$  
  <sub>Salah: tanda suku $4yz^2$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- C. $11x^2y - yz^2 + 8xz - 6$  
  <sub>Salah: tanda suku $-3x^2y$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>
- D. $5x^2y - yz^2 + 10xz - 6$  
  <sub>Salah: tanda suku $-xz$ pada polinomial kedua salah dibalik saat dijumlahkan</sub>

**Pembahasan:** Gabungkan suku sejenis: $5x^2y - yz^2 + 8xz - 6$.
**Acuan:** siswa — siswa hal.79 Mari Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b02-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: koefisien suku tertentu hasil kali*

Pada hasil perkalian (3x^3 - 2x^2 + 5x - 4)(2x^2 - 7x + 6) yang telah disederhanakan, koefisien $x^4$ adalah ....

- A. $6$  
  <sub>Salah: koefisien $x^5$ (kali suku pangkat tertinggi $3 \cdot 2$), bukan $x^4$</sub>
- **B. $-25$** ✅  
  <sub>Benar: $3 \cdot (-7) + (-2) \cdot 2 = -21 - 4 = -25$</sub>
- C. $17$  
  <sub>Salah: hasil kali $3x^3 \cdot (-7x)$ dianggap $+21x^4$ sehingga dihitung $21 - 4$</sub>
- D. $-21$  
  <sub>Salah: hanya pasangan $3x^3 \cdot (-7x)$ yang dihitung, pasangan $-2x^2 \cdot 2x^2$ terlewat</sub>

**Pembahasan:** Suku $x^4$ muncul dari $3x^3 \cdot (-7x) = -21x^4$ dan $-2x^2 \cdot 2x^2 = -4x^4$, jumlahnya $-25$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b02-b-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: parameter pada hasil kali*

Hasil perkalian $(2x^2 + kx - 5)(3x - 6)$ yang telah disederhanakan memuat suku $15x^2$. Nilai $k$ adalah ....

- **A. $9$** ✅  
  <sub>Benar: $3k - 12 = 15$ sehingga $3k = 27$ dan $k = 9$</sub>
- B. $5$  
  <sub>Salah: suku $2x^2 \cdot (-6)$ terlewat sehingga $3k = 15$</sub>
- C. $1$  
  <sub>Salah: $-6 \cdot 2x^2 = +12x^2$ (tanda salah) sehingga $3k + 12 = 15$</sub>
- D. $-1$  
  <sub>Salah: koefisien $x^2$ disamakan dengan $-15$ (tanda ruas kanan terbalik)</sub>

**Pembahasan:** Suku $x^2$ berasal dari $2x^2 \cdot (-6) = -12x^2$ dan $kx \cdot 3x = 3kx^2$, sehingga $3k - 12 = 15$ dan $k = 9$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b02-b-medium-bt01-013
*orisinal | C3 | 4 langkah | jenis: pemodelan luas daerah*

Sebuah taman berbentuk persegi panjang berukuran panjang $(3x + 8)$ meter dan lebar $(2x + 5)$ meter. Di dalam taman terdapat kolam berbentuk persegi panjang berukuran panjang $(x + 4)$ meter dan lebar $(x + 2)$ meter. Luas taman di luar kolam (dalam meter persegi) adalah ....

- A. $2x^2 + 10x + 12$  
  <sub>Salah: panjang dan lebar dikurangkan lebih dulu: $(2x + 4)(x + 3)$, bukan selisih luas</sub>
- **B. $5x^2 + 25x + 32$** ✅  
  <sub>Benar: luas taman $6x^2 + 31x + 40$ dikurangi luas kolam $x^2 + 6x + 8$ memberi $5x^2 + 25x + 32$</sub>
- C. $5x^2 + 25x + 48$  
  <sub>Salah: tanda $+8$ pada hasil kali kolam tidak diubah saat dikurangkan (lupa membalik tanda $x^2 + 6x + 8$)</sub>
- D. $7x^2 + 37x + 48$  
  <sub>Salah: luas taman dan luas kolam dijumlahkan, bukan dikurangkan</sub>

**Pembahasan:** Luas taman $6x^2 + 31x + 40$, luas kolam $x^2 + 6x + 8$. Luas di luar kolam = $5x^2 + 25x + 32$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b02-b-medium-bt01-014
*orisinal | C3 | 4 langkah | jenis: pemodelan volume balok (tiga faktor)*

Sebuah balok memiliki panjang $(x + 5)$ cm, lebar $(x - 2)$ cm, dan tinggi $(2x + 1)$ cm. Volume balok tersebut (dalam cm$^3$) dinyatakan dengan ....

- A. $2x^3 + 15x^2 - 13x - 10$  
  <sub>Salah: $(x + 5)(x - 2)$ dihitung $x^2 + 7x - 10$ ($5 + 2$ bukan $5 - 2$)</sub>
- **B. $2x^3 + 7x^2 - 17x - 10$** ✅  
  <sub>Benar: $(x^2 + 3x - 10)(2x + 1) = 2x^3 + x^2 + 6x^2 + 3x - 20x - 10$</sub>
- C. $2x^3 + 7x^2 + 23x - 10$  
  <sub>Salah: suku $-20x$ pada penjabaran kedua ditulis $+20x$ (tanda salah)</sub>
- D. $2x^3 - 5x^2 - 23x - 10$  
  <sub>Salah: $(x + 5)(x - 2)$ dihitung $x^2 - 3x - 10$ (tanda suku tengah salah)</sub>

**Pembahasan:** $(x+5)(x-2) = x^2 + 3x - 10$; kalikan dengan $(2x+1)$: $2x^3 + 7x^2 - 17x - 10$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b02-b-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: kombinasi perkalian dan pengurangan*

Diketahui $P(x) = 3x^2 - 5x + 2$, $Q(x) = x^2 + 4x - 7$, dan $R(x) = 2x - 3$. Bentuk paling sederhana dari $P(x) - Q(x) \cdot R(x)$ adalah ....

- A. $-2x^3 + 8x^2 - 31x + 23$  
  <sub>Salah: hanya tanda suku pertama $Q(x) \cdot R(x)$ yang diubah, suku lain tidak</sub>
- B. $4x^3 - 24x^2 + 45x - 27$  
  <sub>Salah: pengurangan dikerjakan lebih dulu: $(P - Q) \cdot R$ (urutan operasi salah)</sub>
- **C. $-2x^3 - 2x^2 + 21x - 19$** ✅  
  <sub>Benar: $Q(x) \cdot R(x) = 2x^3 + 5x^2 - 26x + 21$ lalu dikurangkan dari $P(x)$</sub>
- D. $2x^3 + 8x^2 - 31x + 23$  
  <sub>Salah: tanda semua suku $Q(x) \cdot R(x)$ tidak diubah (menjadi penjumlahan)</sub>

**Pembahasan:** $Q \cdot R = 2x^3 + 5x^2 - 26x + 21$; $P - QR = -2x^3 - 2x^2 + 21x - 19$.
**Acuan:** siswa — siswa hal.79

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b02-b-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: mencari polinomial yang hilang*

Polinomial yang jika dijumlahkan dengan $3x^3 - 5x + 8$ menghasilkan $x^3 + 2x^2 + x - 4$ adalah ....

- A. $4x^3 + 2x^2 - 4x + 4$  
  <sub>Salah: kedua polinomial dijumlahkan, bukan dikurangkan</sub>
- B. $2x^3 - 2x^2 - 6x + 12$  
  <sub>Salah: urutan pengurangan terbalik: $A - C$ bukan $C - A$</sub>
- C. $-2x^3 + 2x^2 - 4x - 12$  
  <sub>Salah: $x - (-5x)$ dihitung $1 - 5 = -4$ (tanda suku $-5x$ tidak diubah)</sub>
- **D. $-2x^3 + 2x^2 + 6x - 12$** ✅  
  <sub>Benar: polinomial yang dicari adalah hasil dikurangi polinomial yang diketahui</sub>

**Pembahasan:** Polinomial yang dicari $= C - A = -2x^3 + 2x^2 + 6x - 12$.
**Acuan:** siswa — siswa hal.79

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b02-b-medium-bt01-017
*orisinal | C3 | 4 langkah | jenis: kuadrat polinomial*

Bentuk paling sederhana dari $(x^2 - 2x + 3)^2$ adalah ....

- A. $x^4 - 4x^3 + 10x^2 + 9$  
  <sub>Salah: dua suku $-6x$ dari perkalian silang saling meniadakan karena tanda salah</sub>
- B. $x^4 - 4x^3 + 4x^2 - 12x + 9$  
  <sub>Salah: hasil kali $x^2 \cdot 3$ salah tanda sehingga koefisien $x^2$ menjadi $4$</sub>
- C. $x^4 + 4x^2 + 9$  
  <sub>Salah: hanya tiap suku dikuadratkan, suku silang tidak dihitung</sub>
- **D. $x^4 - 4x^3 + 10x^2 - 12x + 9$** ✅  
  <sub>Benar: $x^4 - 2x^3 + 3x^2 - 2x^3 + 4x^2 - 6x + 3x^2 - 6x + 9$ lalu digabung</sub>

**Pembahasan:** $(x^2 - 2x + 3)(x^2 - 2x + 3) = x^4 - 4x^3 + 10x^2 - 12x + 9$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b02-b-medium-bt01-018
*orisinal | C4 | 3 langkah | jenis: jumlah koefisien hasil kali*

Hasil perkalian (3x^2 - 2x + 5)(2x^3 - x^2 - 4) disederhanakan menjadi polinomial berderajat 5. Jumlah semua koefisiennya (termasuk suku konstan) adalah ....

- **A. $-18$** ✅  
  <sub>Benar: jumlah koefisien hasil kali $= 6 \cdot (-3) = -18$</sub>
- B. $3$  
  <sub>Salah: jumlah koefisien kedua faktor dijumlahkan, $6 + (-3)$, bukan dikalikan</sub>
- C. $-20$  
  <sub>Salah: hanya suku konstan $5 \cdot (-4)$ yang diambil sebagai jumlah</sub>
- D. $18$  
  <sub>Salah: salah tanda pada jumlah koefisien faktor kedua ($2 - 1 - 4$ dihitung $+3$ sehingga $6 \cdot 3$)</sub>

**Pembahasan:** Jumlah koefisien faktor pertama $3 - 2 + 5 = 6$, faktor kedua $2 - 1 - 4 = -3$; hasil kali $6 \cdot (-3) = -18$ (dicek dengan penjabaran: 6x^5 - 7x^4 + 12x^3 - 17x^2 + 8x - 20).
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b02-b-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: soal cerita laba*

Sebuah toko menjual $(2x + 10)$ pensil per hari dengan harga $(x + 5)$ ribu rupiah per pensil. Biaya operasional per hari adalah $(x^2 + 9x + 4)$ ribu rupiah. Laba per hari (dalam ribu rupiah) dinyatakan dengan ....

- A. $x^2 - 9x + 46$  
  <sub>Salah: perkalian $(2x + 10)(x + 5)$ hanya dihitung suku ujungnya ($2x^2 + 50$), suku tengah terlewat</sub>
- B. $x^2 + 11x + 54$  
  <sub>Salah: tanda suku $+4$ pada biaya tidak diubah saat dikurangkan</sub>
- **C. $x^2 + 11x + 46$** ✅  
  <sub>Benar: pendapatan $2x^2 + 20x + 50$ dikurangi biaya $x^2 + 9x + 4$ memberi $x^2 + 11x + 46$</sub>
- D. $-x^2 - 6x + 11$  
  <sub>Salah: banyak pensil dan harga dijumlahkan, bukan dikalikan</sub>

**Pembahasan:** Pendapatan = $2x^2 + 20x + 50$; laba = pendapatan - biaya = $x^2 + 11x + 46$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b02-b-medium-bt01-020
*orisinal | C4 | 4 langkah | jenis: evaluasi pernyataan hasil kali*

Pernyataan yang benar tentang hasil perkalian (x^3 + 2x - 1)(x^2 - 4x + 5) adalah ....

- A. berderajat 5 dan suku konstannya $5$  
  <sub>Salah: suku konstan $(-1) \cdot 5 = -5$ ditulis $+5$ (tanda diabaikan)</sub>
- B. berderajat 5 dan koefisien $x^4$ sama dengan $4$  
  <sub>Salah: koefisien $x^4$ berasal dari $x^3 \cdot (-4x) = -4x^4$, bukan $+4$</sub>
- C. berderajat 6 dan suku konstannya $-5$  
  <sub>Salah: pangkat tertinggi dijumlahkan salah ($3 + 3$), padahal $3 + 2 = 5$</sub>
- **D. berderajat 5 dan suku konstannya $-5$** ✅  
  <sub>Benar: derajat $3 + 2 = 5$ dan suku konstan $(-1) \cdot 5 = -5$</sub>

**Pembahasan:** Pangkat tertinggi $x^3 \cdot x^2 = x^5$, suku konstan $(-1)(5) = -5$, koefisien $x^4$ adalah $-4$ (hasil lengkap: x^5 - 4x^4 + 7x^3 - 9x^2 + 14x - 5).
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b02-b-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim derajat*

Diketahui $P(x)$ berderajat $3$ dan $Q(x)$ berderajat $2$. Misalkan $R(x) = [P(x)]^2 - [Q(x)]^3$ dan $R(x)$ bukan polinomial nol. Pernyataan yang pasti benar adalah ....

- A. derajat $R(x)$ tepat $5$  
  <sub>Salah: mengurangkan derajat dengan cara $3\cdot 2 - 1$ tanpa dasar; contoh $P=x^3+1$, $Q=x^2$ memberi derajat $3$</sub>
- **B. derajat $R(x)$ tidak lebih dari $6$** ✅  
  <sub>Benar: $[P(x)]^2$ dan $[Q(x)]^3$ sama-sama berderajat $6$, sehingga suku $x^6$ dapat saling meniadakan dan derajat selisihnya paling tinggi $6$</sub>
- C. derajat $R(x)$ tepat $12$  
  <sub>Salah: menjumlahkan derajat kedua pangkat ($6+6$) padahal pada pengurangan derajat tidak dijumlahkan</sub>
- D. derajat $R(x)$ tepat $6$  
  <sub>Salah: mengira selisih dua polinomial berderajat sama pasti berderajat sama; contoh $P=x^3+1$, $Q=x^2$ memberi $R=2x^3+1$</sub>

**Pembahasan:** $P^2$ berderajat 6 dan $Q^3$ berderajat 6. Selisih dua polinomial berderajat 6 berderajat paling tinggi 6 (bisa lebih rendah jika koefisien $x^6$ sama). Contoh penyangkal: $P=x^3+1$, $Q=x^2$ menghasilkan $R=2x^3+1$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b02-b-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim derajat*

Pernyataan berikut yang pasti benar untuk sembarang polinomial $P(x)$ dan $Q(x)$ yang memenuhi syaratnya adalah ....

- A. Jika $P(x)$ dan $Q(x)$ keduanya berderajat $6$, maka $P(x) - Q(x)$ berderajat $0$.  
  <sub>Salah: mengira dua polinomial berderajat sama saling meniadakan semua suku; contoh $x^6+x$ dan $x^6+3$ memberi selisih $x-3$ yang berderajat $1$</sub>
- **B. Jika $P(x)$ berderajat $5$ dan $Q(x)$ berderajat $2$, maka $P(x) - Q(x)$ berderajat $5$.** ✅  
  <sub>Benar: suku $x^5$ hanya dimiliki $P(x)$ sehingga tidak ada yang meniadakannya dan derajat selisih tetap $5$</sub>
- C. Jika $P(x)$ dan $Q(x)$ keduanya berderajat $4$, maka $P(x) + Q(x)$ berderajat $4$.  
  <sub>Salah: mengabaikan kemungkinan koefisien $x^4$ saling meniadakan, mis. $x^4+x$ dan $-x^4+2$</sub>
- D. Jika $P(x)$ dan $Q(x)$ keduanya berderajat $3$, maka $P(x) \cdot Q(x)$ berderajat $9$.  
  <sub>Salah: mengalikan derajat, bukan menjumlahkan; hasilnya berderajat $6$</sub>

**Pembahasan:** Hanya pernyataan pertama yang berlaku untuk semua polinomial. Yang lain punya contoh penyangkal.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b02-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan*

$(6x^3 - 4x^2 + 5x - 8) - (2x^3 - 7x^2 - 3x + 4)$

(1) $= 6x^3 - 4x^2 + 5x - 8 - 2x^3 - 7x^2 + 3x - 4$

(2) $= 6x^3 - 2x^3 - 4x^2 - 7x^2 + 5x + 3x - 8 - 4$

(3) $= 4x^3 - 11x^2 + 8x - 12$

Seorang siswa menyelesaikan pengurangan polinomial pada stimulus. Langkah pertama yang mengandung kesalahan adalah ....

- A. langkah (3), karena koefisien hasil penjumlahan salah  
  <sub>Salah: penjumlahan koefisien pada langkah (3) benar terhadap langkah (2)</sub>
- B. langkah (2), karena suku-suku sejenis dikelompokkan dengan salah  
  <sub>Salah: langkah (2) hanya mengelompokkan ulang suku-suku langkah (1) dan benar</sub>
- C. tidak ada langkah yang salah  
  <sub>Salah: hasil akhir $4x^3 - 11x^2 + 8x - 12$ berbeda dari hasil benar $4x^3 + 3x^2 + 8x - 12$</sub>
- **D. langkah (1), karena $-(-7x^2)$ seharusnya menjadi $+7x^2$** ✅  
  <sub>Benar: pada langkah (1) tanda $-7x^2$ tidak dibalik; langkah (2) dan (3) konsisten dengan langkah (1)</sub>

**Pembahasan:** Langkah (1) seharusnya memberi $6x^3-4x^2+5x-8-2x^3+7x^2+3x-4$. Hasil benar $4x^3+3x^2+8x-12$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b02-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan*

(1) $(4x - 3)(2x^2 - x + 6) = 4x(2x^2 - x + 6) - 3(2x^2 - x + 6)$

(2) $= 8x^3 - 4x^2 + 24x - 6x^2 - 3x - 18$

(3) $= 8x^3 - 10x^2 + 21x - 18$

Seorang siswa mengalikan $(4x - 3)(2x^2 - x + 6)$ seperti pada stimulus. Pernyataan yang benar tentang pekerjaan siswa adalah ....

- A. langkah (3) salah karena $24x - 3x$ seharusnya $27x$, sedangkan langkah (2) benar  
  <sub>Salah: langkah (3) konsisten dengan langkah (2); sumber kesalahan sebenarnya ada di langkah (2)</sub>
- B. semua langkah benar dan hasil akhirnya $8x^3 - 10x^2 + 21x - 18$  
  <sub>Salah: tidak memeriksa tanda $-3 \cdot (-x) = +3x$</sub>
- C. langkah (1) salah karena faktor $(4x-3)$ tidak boleh dipecah menjadi dua suku, dan hasil benar $8x^3 - 10x^2 + 21x - 18$  
  <sub>Salah: menganggap distribusi pada langkah (1) salah; padahal itu penerapan sifat distributif yang benar</sub>
- **D. langkah (2) salah karena $-3 \cdot (-x)$ seharusnya $+3x$, dan hasil yang benar adalah $8x^3 - 10x^2 + 27x - 18$** ✅  
  <sub>Benar: langkah (1) benar; pada langkah (2) suku $-3x$ seharusnya $+3x$ sehingga koefisien $x$ menjadi $24+3=27$</sub>

**Pembahasan:** Hasil benar: $8x^3-4x^2+24x-6x^2+3x-18 = 8x^3-10x^2+27x-18$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b02-b-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: menemukan kesalahan*

Seorang siswa menulis $(2x - 7)^2 = 4x^2 + 49$. Jika bentuk yang benar dikurangi bentuk tulisan siswa, hasilnya adalah ....

- **A. $-28x$** ✅  
  <sub>Benar: $(2x-7)^2 = (2x-7)(2x-7) = 4x^2 - 28x + 49$, sehingga selisihnya $-28x$</sub>
- B. $28x$  
  <sub>Salah: membalik urutan pengurangan (tulisan siswa dikurangi bentuk benar)</sub>
- C. $-14x$  
  <sub>Salah: menghitung suku tengah $2 \cdot 2x \cdot 7$ tanpa mengalikan koefisien $2x$ dengan benar</sub>
- D. $0$  
  <sub>Salah: membenarkan klaim siswa tanpa memeriksa suku silang $-14x$ dan $-14x$</sub>

**Pembahasan:** $(2x-7)(2x-7) = 4x^2-14x-14x+49 = 4x^2-28x+49$. Selisih dengan $4x^2+49$ adalah $-28x$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b02-b-hard-bt01-006
*orisinal | C6 | 6 langkah | jenis: merancang polinomial*

Diketahui $P(x) = 5x^3 - 4x^2 + x + 3$. Polinomial $Q(x) = 5x^3 + ax^2 + bx + c$ dirancang sehingga $P(x) - Q(x)$ berderajat $1$ dengan koefisien $x$ sama dengan $6$, dan suku konstan $P(x) + Q(x)$ sama dengan $11$. Nilai $a + b + c$ adalah ....

- A. $-17$  
  <sub>Salah: memakai $a=-4$, $b=-5$, dan $c=-8$ (suku konstan dihitung dari $3-c=11$)</sub>
- B. $17$  
  <sub>Salah: memakai $a=4$, $b=5$, $c=8$ (salah tanda pada $a$ dan $b$)</sub>
- **C. $-1$** ✅  
  <sub>Benar: $P-Q$ berderajat 1 mensyaratkan $-4-a=0$ dan $1-b=6$; suku konstan $3+c=11$</sub>
- D. $9$  
  <sub>Salah: menyelesaikan $1-b=6$ sebagai $b=5$ (salah memindahkan ruas), sehingga $a+b+c=-4+5+8$</sub>

**Pembahasan:** $P-Q = (-4-a)x^2+(1-b)x+(3-c)$, berderajat 1 jika $a=-4$; $1-b=6 \Rightarrow b=-5$; $P+Q$ suku konstan $3+c=11 \Rightarrow c=8$; jumlah $= -1$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b02-b-hard-bt01-007
*orisinal | C6 | 4 langkah | jenis: merancang polinomial*

Polinomial $R(x) = x^2 + px + q$ dirancang sehingga hasil perkalian $(x - 3)R(x)$ hanya terdiri dari dua suku. Polinomial $R(x)$ tersebut adalah ....

- A. $x^2 + 3x - 9$  
  <sub>Salah: salah tanda $q$; hasilnya $x^3-18x+27$ masih tiga suku</sub>
- B. $x^2 - 3x + 9$  
  <sub>Salah: salah tanda $p$; hasilnya $x^3-6x^2+18x-27$ masih empat suku</sub>
- **C. $x^2 + 3x + 9$** ✅  
  <sub>Benar: $(x-3)(x^2+px+q) = x^3+(p-3)x^2+(q-3p)x-3q$; suku $x^2$ dan $x$ lenyap bila $p=3$ dan $q=9$ sehingga hasilnya $x^3-27$</sub>
- D. $x^2 + 9$  
  <sub>Salah: mengira cukup menghilangkan suku $x$ pada $R$; hasilnya $x^3-3x^2+9x-27$ empat suku</sub>

**Pembahasan:** Samakan koefisien $x^2$ dan $x$ dengan $0$: $p=3$, $q=9$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b02-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim hasil operasi*

Tiga siswa memberi klaim tentang bentuk paling sederhana dari $(x + 3)(x^2 - 3x + 9) - (x - 3)(x^2 + 3x + 9)$. Klaim yang benar adalah ....

- A. hasilnya $0$ karena kedua hasil kali tampak serupa  
  <sub>Salah: mengabaikan suku konstan $+27$ dan $-27$ yang berbeda tanda</sub>
- **B. hasilnya $54$, bernilai sama untuk setiap $x$** ✅  
  <sub>Benar: $(x+3)(x^2-3x+9)=x^3+27$ dan $(x-3)(x^2+3x+9)=x^3-27$, selisihnya $54$</sub>
- C. hasilnya $27$, bernilai sama untuk setiap $x$  
  <sub>Salah: hanya memakai satu suku konstan dan lupa mengurangkan $-27$</sub>
- D. hasilnya $2x^3$, berderajat $3$  
  <sub>Salah: mengira suku $x^3$ dijumlahkan padahal harus dikurangkan</sub>

**Pembahasan:** $x^3+27-(x^3-27)=54$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b02-b-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: evaluasi klaim hasil operasi*

Pernyataan yang benar tentang hasil perkalian $(x^5 + x^4 + x^3 + x^2 + x + 1)(x - 1)$ setelah disederhanakan adalah ....

- **A. terdiri dari $2$ suku dan berderajat $6$** ✅  
  <sub>Benar: setiap suku $x^k$ pada hasil distribusi $x\cdot(\dots)$ meniadakan $-x^k$ dari $-1\cdot(\dots)$, tersisa $x^6-1$</sub>
- B. terdiri dari $12$ suku dan berderajat $6$  
  <sub>Salah: menghitung banyak suku sebelum disederhanakan ($6 \times 2$)</sub>
- C. terdiri dari $6$ suku dan berderajat $5$  
  <sub>Salah: menganggap banyak suku sama dengan faktor pertama dan derajat tidak naik karena dikalikan $x$</sub>
- D. terdiri dari $7$ suku dan berderajat $6$  
  <sub>Salah: menjumlahkan suku $x^6$ dengan keenam suku lain tanpa memeriksa pasangan yang meniadakan</sub>

**Pembahasan:** Hasilnya $x^6-1$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b02-b-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: evaluasi klaim hasil operasi*

Hasil perkalian $(x^2 + ax + 4)(x^2 - 3x + b)$ yang telah disederhanakan tidak memuat suku $x^3$ dan suku $x$. Pernyataan yang benar adalah ....

- A. $a = 3$, $b = 4$, dan koefisien $x^2$ adalah $8$  
  <sub>Salah: koefisien $x^2$ hanya dari $b+4$ tanpa suku silang $-3a x^2$</sub>
- B. $a = 3$, $b = -4$, dan koefisien $x^2$ adalah $-9$  
  <sub>Salah: menghitung koefisien $x$ sebagai $ab+12=0$ (salah tanda $4 \cdot (-3)$)</sub>
- **C. $a = 3$, $b = 4$, dan koefisien $x^2$ adalah $-1$** ✅  
  <sub>Benar: koefisien $x^3$: $a-3=0$; koefisien $x$: $ab-12=0$ sehingga $b=4$; koefisien $x^2$: $b+4-3a=-1$</sub>
- D. $a = -3$, $b = 4$, dan koefisien $x^2$ adalah $17$  
  <sub>Salah: menyelesaikan $a-3=0$ menjadi $a=-3$</sub>

**Pembahasan:** Koefisien $x^3$: $a-3$; koefisien $x$: $ab-12$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b02-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: pemodelan dan evaluasi hasil*

Selembar karton berbentuk persegi dengan sisi $20$ cm. Dari setiap sudutnya dipotong persegi dengan sisi $x$ cm, lalu karton dilipat menjadi kotak tanpa tutup dengan tinggi $x$ cm. Volume kotak $V(x)$ dinyatakan dalam $x$. Pernyataan yang benar tentang $V(x)$ yang telah disederhanakan adalah ....

- A. berderajat $3$ dan koefisien $x^2$ adalah $-40$  
  <sub>Salah: suku tengah dihitung $-2\cdot 20x$ bukan $-2\cdot 2\cdot 20x$</sub>
- **B. berderajat $3$ dan koefisien $x^2$ adalah $-80$** ✅  
  <sub>Benar: alas kotak berukuran $(20-2x)$ kali $(20-2x)$ sehingga $V=x(20-2x)^2=4x^3-80x^2+400x$</sub>
- C. berderajat $2$ dan koefisien $x^2$ adalah $-2$  
  <sub>Salah: menghitung alas sebagai $(20-2x)$ saja (satu faktor) sehingga $V=x(20-2x)$</sub>
- D. berderajat $3$ dan tidak memuat suku $x^2$  
  <sub>Salah: mengkuadratkan $(20-2x)$ menjadi $400-4x^2$ tanpa suku tengah</sub>

**Pembahasan:** $V=x(400-80x+4x^2)=4x^3-80x^2+400x$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b02-b-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: pemodelan dan evaluasi hasil*

Persegi $A$ bersisi $(2x + 7)$ cm dan persegi $B$ bersisi $(2x - 7)$ cm dengan $x > 3{,}5$. Selisih luas $A - B$ (dalam cm$^2$) yang benar adalah ....

- **A. $56x$** ✅  
  <sub>Benar: $(2x+7)^2-(2x-7)^2=(4x^2+28x+49)-(4x^2-28x+49)=56x$</sub>
- B. $8x^2 + 98$  
  <sub>Salah: menjumlahkan luas kedua persegi, bukan menghitung selisihnya</sub>
- C. $98$, konstan  
  <sub>Salah: mengira suku silang saling meniadakan lalu menjumlahkan $49$ dan $49$ alih-alih menghitung selisih</sub>
- D. $28x$  
  <sub>Salah: hanya menghitung satu suku silang ($28x$), padahal ada dua suku silang berbeda tanda</sub>

**Pembahasan:** Luas A $=4x^2+28x+49$, luas B $=4x^2-28x+49$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b02-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim derajat*

Perhatikan $(\square x^2 + \square x + 1)(\square x - 1) = A(x)$. Jika tanda kotak diganti sembarang bilangan real (boleh nol), pernyataan yang benar tentang $A(x)$ adalah ....

- A. $A(x)$ dapat berderajat $4$ jika kotak diisi bilangan besar  
  <sub>Salah: mengira derajat naik bila koefisien besar; derajat hanya ditentukan pangkat variabel, maksimum $2+1=3$</sub>
- B. $A(x)$ tidak selalu polinomial karena kotak dapat diisi $0$  
  <sub>Salah: mengira koefisien nol menghasilkan bentuk yang bukan polinomial</sub>
- C. $A(x)$ selalu berderajat tepat $3$  
  <sub>Salah: melupakan bahwa kotak boleh diisi nol, mis. $(x^2+1)(0\cdot x-1)=-x^2-1$ berderajat $2$</sub>
- **D. $A(x)$ selalu polinomial bukan nol, dan derajatnya paling tinggi $3$ (dapat kurang dari $3$)** ✅  
  <sub>Benar: hasil kali polinomial adalah polinomial; suku konstan $A(x)$ selalu $-1$ sehingga tidak nol; derajat $3$ terjadi hanya bila koefisien $x^2$ dan $x$ pada kedua faktor tidak nol</sub>

**Pembahasan:** Derajat maksimum $2+1=3$; koefisien nol menurunkannya; konstanta $-1$ menjamin tidak nol.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b02-b-hard-bt01-014
*orisinal | C5 | 3 langkah | jenis: evaluasi sifat operasi*

Untuk sembarang polinomial $P(x)$, $Q(x)$, dan $R(x)$, kesamaan yang selalu berlaku adalah ....

- A. $P(x) - Q(x) = Q(x) - P(x)$  
  <sub>Salah: mengira pengurangan komutatif; hanya berlaku bila $P=Q$</sub>
- B. $P(x) - [Q(x) + R(x)] = P(x) - Q(x) + R(x)$  
  <sub>Salah: tidak membalik tanda $R(x)$ saat menghilangkan tanda kurung</sub>
- **C. $P(x) - Q(x) = -[Q(x) - P(x)]$** ✅  
  <sub>Benar: mengubah tanda setiap suku $Q - P$ menghasilkan $P - Q$</sub>
- D. $P(x) - Q(x) = -[P(x) + Q(x)]$  
  <sub>Salah: mengira selisih sama dengan negatif jumlah; contoh $P=x$, $Q=1$</sub>

**Pembahasan:** $-(Q-P)=P-Q$. Contoh $P=x$, $Q=1$, $R=1$ menyangkal tiga kesamaan lain.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11_tl-b02-b-hard-bt01-015
*orisinal | C6 | 4 langkah | jenis: kemungkinan derajat jumlah dan selisih*

Diketahui $P(x)$ dan $Q(x)$ masing-masing berderajat $4$. Kejadian yang mungkin terjadi adalah ....

- **A. $P(x) + Q(x)$ berderajat $2$ dan $P(x) - Q(x)$ berderajat $4$** ✅  
  <sub>Benar: jika koefisien $x^4$ adalah $p$ dan $q$ dengan $p+q=0$, maka $p-q=2p\neq 0$; contoh $3x^4+2x^3+x^2-5$ dan $-3x^4-2x^3+4x^2+1$</sub>
- B. $P(x) + Q(x)$ berderajat $8$  
  <sub>Salah: menjumlahkan derajat seperti pada perkalian; jumlah tidak pernah melebihi derajat $4$</sub>
- C. $P(x) + Q(x)$ dan $P(x) - Q(x)$ keduanya berderajat $2$  
  <sub>Salah: tidak mungkin: $p+q=0$ dan $p-q=0$ mengakibatkan $p=0$, bertentangan dengan derajat $4$</sub>
- D. $P(x) + Q(x)$ dan $P(x) - Q(x)$ keduanya berderajat $3$  
  <sub>Salah: tidak mungkin: agar suku $x^4$ lenyap pada jumlah dan selisih sekaligus, harus $p=q=0$</sub>

**Pembahasan:** Suku $x^4$ tidak dapat lenyap pada jumlah dan selisih sekaligus.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11_tl-b02-b-hard-bt01-016
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Budi mengklaim: "Jumlah dua polinomial berderajat $3$ selalu berderajat $3$." Diketahui $P(x) = 2x^3 - 5x^2 + x + 4$. Polinomial $Q(x)$ yang bersama $P(x)$ merupakan contoh penyangkal klaim Budi adalah ....

- A. $Q(x) = -x^3 + 4x + 2$  
  <sub>Salah: koefisien $x^3$ menjadi $1$ (tidak nol), jumlahnya tetap berderajat $3$</sub>
- B. $Q(x) = x^2 - 3x + 7$  
  <sub>Salah: $Q$ tidak berderajat $3$, sehingga tidak memenuhi syarat klaim; jumlahnya tetap berderajat $3$</sub>
- C. $Q(x) = 2x^3 + x - 1$  
  <sub>Salah: koefisien $x^3$ dijumlahkan menjadi $4$, jumlahnya berderajat $3$ sehingga mendukung klaim</sub>
- **D. $Q(x) = -2x^3 + x^2 + 6$** ✅  
  <sub>Benar: $Q$ berderajat $3$ dan $P+Q=-4x^2+x+10$ berderajat $2$, bukan $3$</sub>

**Pembahasan:** Agar jumlah turun derajat, koefisien $x^3$ $Q$ harus $-2$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
