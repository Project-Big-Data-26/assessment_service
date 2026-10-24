# Lembar koreksi — kelas11_tl SMA11L-B2 subbab C: Pembagian Polinomial

57 soal | easy 20, medium 20, hard 17 | variasi 20, orisinal 37
> **Kapasitas kurang (hard): 17 dari kuota 20** — Subbab C (pembagian polinomial, p84-p95) sempit: penalaran hard hanya berkisar pada Teorema Sisa, Horner, dan sisa pembagi kuadrat; sudah dipakai easy dan medium. Soal hard tambahan akan berupa kembaran berangka berbeda atau materi faktor (subbab D), sehingga tidak dipaksakan.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b02-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: pembagian bersusun*

Hasil bagi $H(x)$ dan sisa $S(x)$ setelah $P(x) = x^3 + 4x^2 - 6x + 7$ dibagi $Q(x) = x^2 + 5x - 4$ adalah ....

- A. $H(x) = x - 1$ dan $S(x) = 3x + 11$  
  <sub>Salah: salah tanda saat mengalikan $-1$ dengan $-4$ sehingga konstanta sisa menjadi $11$</sub>
- B. $H(x) = 3x + 3$ dan $S(x) = x - 1$  
  <sub>Salah: hasil bagi dan sisa tertukar</sub>
- **C. $H(x) = x - 1$ dan $S(x) = 3x + 3$** ✅  
  <sub>Benar: $x \cdot Q = x^3 + 5x^2 - 4x$ menyisakan $-x^2 - 2x + 7$; $-1 \cdot Q = -x^2 - 5x + 4$ menyisakan $3x + 3$ yang berderajat kurang dari $Q$.</sub>
- D. $H(x) = x - 1$ dan $S(x) = -x^2 - 2x + 7$  
  <sub>Salah: berhenti satu langkah terlalu cepat; sisa masih berderajat sama dengan $Q$</sub>

**Pembahasan:** Bagi $x^3 / x^2 = x$, kurangi, lanjut $-x^2 / x^2 = -1$, kurangi: $H = x - 1$, $S = 3x + 3$. Cek: $(x-1)(x^2+5x-4) + 3x + 3 = P(x)$.
**Acuan:** siswa — siswa hal.87 Mari Mencoba 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b02-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: Horner: hasil bagi dan sisa*

Hasil bagi dan sisa dari pembagian $x^3 + 7$ oleh $x - 2$ dengan menggunakan metode Horner adalah ....

- A. hasil bagi $x^3 + 2x^2 + 4x + 15$, sisa $0$  
  <sub>Salah: menganggap semua angka pada baris hasil sebagai hasil bagi</sub>
- **B. hasil bagi $x^2 + 2x + 4$, sisa $15$** ✅  
  <sub>Benar: Koefisien $1, 0, 0, 7$ dengan $c = 2$ menghasilkan baris $1, 2, 4, 15$; tiga angka pertama hasil bagi, angka terakhir sisa.</sub>
- C. hasil bagi $x^2 + 2x + 4$, sisa $4$  
  <sub>Salah: mengambil koefisien terakhir hasil bagi sebagai sisa</sub>
- D. hasil bagi $x^2 - 2x + 4$, sisa $-1$  
  <sub>Salah: memakai $c = -2$ karena salah tanda pembagi $x - 2$</sub>

**Pembahasan:** Horner dengan $c = 2$: $1 \to 2 \to 4 \to 15$. Hasil bagi $x^2 + 2x + 4$, sisa $15$.
**Acuan:** siswa — siswa hal.89 Mari Mencoba 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b02-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: Horner: hasil bagi dan sisa*

Hasil bagi pada pembagian $4x^3 - 7x + 8$ oleh $x + 1$ dengan metode Horner adalah ....

- **A. $4x^2 - 4x - 3$** ✅  
  <sub>Benar: Pembagi $x + 1 = x - (-1)$ sehingga $c = -1$; koefisien $4, 0, -7, 8$ menghasilkan baris $4, -4, -3, 11$. Hasil bagi $4x^2 - 4x - 3$.</sub>
- B. $4x^2 + 4x - 3$  
  <sub>Salah: memakai $c = 1$ padahal pembagi $x + 1$ berarti $c = -1$</sub>
- C. $4x^2 - 4x + 11$  
  <sub>Salah: mengambil sisa $11$ sebagai suku konstan hasil bagi</sub>
- D. $4x - 11$  
  <sub>Salah: lupa menuliskan koefisien nol untuk $x^2$ sehingga hanya tiga koefisien ($4, -7, 8$) dihitung</sub>

**Pembahasan:** Baris Horner: $4$; $0 + (-1)(4) = -4$; $-7 + (-1)(-4) = -3$; $8 + (-1)(-3) = 11$. Hasil bagi $4x^2 - 4x - 3$, sisa $11$.
**Acuan:** siswa — siswa hal.88 Contoh 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b02-c-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: Teorema Sisa*

Sisa pembagian $P(x) = 9x^3 + 12x^2 - 11x + 13$ oleh $x - 2$ dengan Teorema Sisa adalah ....

- A. $11$  
  <sub>Salah: mensubstitusi $x = -2$ (salah tanda $c$)</sub>
- B. $98$  
  <sub>Salah: lupa menjumlahkan konstanta $13$</sub>
- **C. $111$** ✅  
  <sub>Benar: Menurut Teorema Sisa sisa $= P(2) = 9(8) + 12(4) - 11(2) + 13 = 72 + 48 - 22 + 13 = 111$.</sub>
- D. $23$  
  <sub>Salah: mengira sisa sama dengan $P(1)$, yaitu jumlah koefisien</sub>

**Pembahasan:** $P(2) = 72 + 48 - 22 + 13 = 111$.
**Acuan:** siswa — siswa hal.92 Mari Mencoba 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b02-c-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: Teorema Sisa*

Jika $P(x) = 7x^3 + 8x^2 - 6x + 12$ dibagi $x + 1$, diperoleh hasil bagi $7x^2 + x - 7$ dan sisa $19$. Dengan menggunakan Teorema Sisa, nilai $P(-1)$ adalah ....

- **A. $19$** ✅  
  <sub>Benar: Pembagi $x + 1 = x - (-1)$, sehingga $P(-1)$ sama dengan sisa pembagian, yaitu $19$.</sub>
- B. $-19$  
  <sub>Salah: mengira $P(-1)$ berlawanan tanda dengan sisa karena $c = -1$</sub>
- C. $-7$  
  <sub>Salah: mengambil konstanta hasil bagi sebagai nilai $P(-1)$</sub>
- D. $21$  
  <sub>Salah: menghitung $P(1)$ karena salah tanda $c$</sub>

**Pembahasan:** Teorema Sisa: sisa pembagian $P(x)$ oleh $x - (-1)$ sama dengan $P(-1)$, jadi $P(-1) = 19$ (cek langsung: $-7 + 8 + 6 + 12 = 19$).
**Acuan:** siswa — siswa hal.91 Contoh 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b02-c-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: pembagian bersusun*

Hasil pembagian $3x^3 + 8x^2 - 5x + 7$ oleh $x^2 + 5x - 2$ yang ditulis dalam bentuk algoritma pembagian adalah ....

- A. $3x^3 + 8x^2 - 5x + 7 = (x^2 + 5x - 2)(3x - 7) + 36x$  
  <sub>Salah: suku konstan sisa $-7$ terlewat</sub>
- B. $3x^3 + 8x^2 - 5x + 7 = (x^2 + 5x - 2)(3x + 7) + 36x - 7$  
  <sub>Salah: tanda suku kedua hasil bagi salah ($+7$ bukan $-7$)</sub>
- C. $3x^3 + 8x^2 - 5x + 7 = (x^2 + 5x - 2)(3x - 7) + 36x + 7$  
  <sub>Salah: salah tanda saat mengurangkan $14$ sehingga sisa menjadi $36x + 7$</sub>
- **D. $3x^3 + 8x^2 - 5x + 7 = (x^2 + 5x - 2)(3x - 7) + 36x - 7$** ✅  
  <sub>Benar: $3x \cdot Q = 3x^3 + 15x^2 - 6x$ menyisakan $-7x^2 + x + 7$; $-7 \cdot Q = -7x^2 - 35x + 14$ menyisakan $36x - 7$.</sub>

**Pembahasan:** $H = 3x - 7$, $S = 36x - 7$, sehingga $P(x) = (x^2 + 5x - 2)(3x - 7) + 36x - 7$.
**Acuan:** siswa — siswa hal.86 Contoh 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b02-c-easy-bt01-007
*variasi (konteks) | C1 | 1 langkah | jenis: konsep derajat sisa*

Sebuah polinomial dibagi oleh polinomial pembagi yang berderajat $4$. Derajat tertinggi yang mungkin dimiliki sisa pembagian tersebut adalah ....

- A. $4$  
  <sub>Salah: mengira sisa boleh berderajat sama dengan pembagi</sub>
- B. $5$  
  <sub>Salah: mengira sisa dapat berderajat lebih tinggi dari pembagi</sub>
- **C. $3$** ✅  
  <sub>Benar: Derajat sisa harus kurang dari derajat pembagi, sehingga paling tinggi $4 - 1 = 3$.</sub>
- D. $2$  
  <sub>Salah: mengira derajat sisa paling tinggi setengah derajat pembagi</sub>

**Pembahasan:** Algoritma pembagian: sisa bernilai 0 atau berderajat kurang dari pembagi. Pembagi berderajat 4 berarti sisa berderajat paling tinggi 3.
**Acuan:** siswa — siswa hal.93 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b02-c-easy-bt01-008
*variasi (konteks) | C1 | 1 langkah | jenis: Teorema Sisa*

Polinomial $P(x)$ dibagi $x + 5$ menghasilkan sisa $-8$. Nilai $P(-5)$ adalah ....

- A. $0$  
  <sub>Salah: mengira $P(c)$ selalu nol karena $x = -5$ membuat pembagi nol</sub>
- B. $8$  
  <sub>Salah: salah tanda saat menyamakan $P(c)$ dengan sisa</sub>
- **C. $-8$** ✅  
  <sub>Benar: Pembagi $x + 5 = x - (-5)$, sehingga menurut Teorema Sisa $P(-5)$ sama dengan sisa, yaitu $-8$.</sub>
- D. $5$  
  <sub>Salah: mengira nilai $P(-5)$ adalah lawan dari pembuat nol pembagi</sub>

**Pembahasan:** Teorema Sisa: sisa pembagian $P(x)$ oleh $x - c$ sama dengan $P(c)$. Dengan $c = -5$, $P(-5) = -8$.
**Acuan:** pretest — kelas11_tl-b02-p0094-latihan-c-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b02-c-easy-bt01-009
*variasi (angka) | C2 | 1 langkah | jenis: bentuk algoritma pembagian*

Diketahui $x^3 + x^2 - 33x - 42 = (x - 6)(x^2 + 7x + 9) + 12$. Jika polinomial $x^3 + x^2 - 33x - 42$ dibagi $x - 6$, hasil bagi dan sisanya berturut-turut adalah ....

- A. $12$ dan $x^2 + 7x + 9$  
  <sub>Salah: hasil bagi dan sisa tertukar</sub>
- B. $x - 6$ dan $12$  
  <sub>Salah: menganggap pembagi sebagai hasil bagi</sub>
- C. $x^2 + 7x + 9$ dan $-12$  
  <sub>Salah: salah tanda sisa</sub>
- **D. $x^2 + 7x + 9$ dan $12$** ✅  
  <sub>Benar: Bentuk $P = Q \cdot H + S$ dengan pembagi $x - 6$: hasil bagi $x^2 + 7x + 9$ dan sisa $12$.</sub>

**Pembahasan:** Dari $P(x) = (x - 6) \cdot H(x) + S(x)$ terbaca $H(x) = x^2 + 7x + 9$ dan $S(x) = 12$.
**Acuan:** siswa — siswa hal.85 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b02-c-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: Horner: hasil bagi dan sisa*

Hasil bagi dan sisa pembagian $(x^3 + 64) : (x + 4)$ adalah ....

- A. hasil bagi $x^2 - 4x + 16$, sisa $-4$  
  <sub>Salah: mengambil koefisien $x$ pada hasil bagi sebagai sisa</sub>
- B. hasil bagi $x^2 - 4x + 16$, sisa $64$  
  <sub>Salah: mengira konstanta $64$ menjadi sisa tanpa dihitung</sub>
- C. hasil bagi $x^2 + 4x + 16$, sisa $0$  
  <sub>Salah: memakai $c = 4$ padahal pembagi $x + 4$ berarti $c = -4$</sub>
- **D. hasil bagi $x^2 - 4x + 16$, sisa $0$** ✅  
  <sub>Benar: Koefisien $1, 0, 0, 64$ dengan $c = -4$: baris $1, -4, 16, 0$. Hasil bagi $x^2 - 4x + 16$, sisa $0$.</sub>

**Pembahasan:** Horner $c = -4$: $1$; $0 - 4 = -4$; $0 + 16 = 16$; $64 - 64 = 0$. Hasil bagi $x^2 - 4x + 16$, sisa $0$.
**Acuan:** siswa — siswa hal.87 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b02-c-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: Teorema Sisa*

Misalkan $P(x) = 8x^3 - 14x^2 + 9x - 10$ dan $c = \frac{1}{2}$. Dengan metode Horner dan Teorema Sisa, nilai $P(c)$ adalah ....

- A. $16$  
  <sub>Salah: mensubstitusi $c = 2$ (pecahan dibalik)</sub>
- B. $-19$  
  <sub>Salah: mensubstitusi $c = -\frac{1}{2}$ (salah tanda)</sub>
- C. $2$  
  <sub>Salah: berhenti sebelum menjumlahkan konstanta terakhir ($-10$)</sub>
- **D. $-8$** ✅  
  <sub>Benar: Horner $c = \frac{1}{2}$: $8$; $-14 + 4 = -10$; $9 - 5 = 4$; $-10 + 2 = -8$. Sisa terakhir $-8 = P(\frac{1}{2})$.</sub>

**Pembahasan:** Skema Horner dengan $c = \frac{1}{2}$ memberi baris $8, -10, 4, -8$; sisa $-8$, jadi $P(\frac{1}{2}) = -8$.
**Acuan:** pretest — kelas11_tl-b02-p0094-latihan-c-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b02-c-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: penulisan skema Horner*

Pembagi $x + 6$ dapat ditulis $x - (-6)$. Bilangan yang menggantikan pembagi tersebut dalam skema Horner adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: mengira pembagi diganti dengan kebalikannya</sub>
- B. $6$  
  <sub>Salah: tidak memperhatikan tanda: mengambil angka pada pembagi apa adanya</sub>
- **C. $-6$** ✅  
  <sub>Benar: Karena $x + 6 = x - (-6)$, bilangan pengganti pembagi pada skema Horner adalah $c = -6$.</sub>
- D. $-\frac{1}{6}$  
  <sub>Salah: mengira pembagi diganti dengan lawan kebalikannya</sub>

**Pembahasan:** $x + 6 = x - (-6)$ sehingga $c = -6$.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b02-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: penulisan skema Horner*

Polinomial $5x^4 - 2x + 7$ akan dibagi dengan metode Horner. Deretan koefisien yang ditulis pada skema Horner adalah ....

- A. $7, -2, 0, 0, 5$  
  <sub>Salah: urutan terbalik, dari suku terendah ke tertinggi</sub>
- **B. $5, 0, 0, -2, 7$** ✅  
  <sub>Benar: Koefisien ditulis dari pangkat tertinggi ke terendah: $x^4$ ($5$), $x^3$ ($0$), $x^2$ ($0$), $x$ ($-2$), konstanta ($7$).</sub>
- C. $5, -2, 7$  
  <sub>Salah: suku yang tidak ada ($x^3$ dan $x^2$) tidak ditulis sebagai koefisien nol</sub>
- D. $5, 0, -2, 7$  
  <sub>Salah: hanya satu koefisien nol yang disisipkan padahal dua pangkat hilang</sub>

**Pembahasan:** Pangkat $4, 3, 2, 1, 0$ memiliki koefisien $5, 0, 0, -2, 7$.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b02-c-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: bentuk algoritma pembagian*

Polinomial $P(x)$ dibagi $Q(x) = x - 5$ menghasilkan hasil bagi $H(x) = x + 6$ dan sisa $S(x) = 4$. Polinomial $P(x)$ adalah ....

- A. $x^2 + x - 34$  
  <sub>Salah: mengurangkan sisa, bukan menambahkan</sub>
- B. $x^2 + x - 30$  
  <sub>Salah: lupa menambahkan sisa $4$</sub>
- C. $x^2 - 11x - 26$  
  <sub>Salah: salah menjabarkan $(x - 5)(x + 6)$ dengan suku tengah $-5x - 6x$</sub>
- **D. $x^2 + x - 26$** ✅  
  <sub>Benar: $P(x) = Q(x) \cdot H(x) + S(x) = (x - 5)(x + 6) + 4 = x^2 + x - 30 + 4 = x^2 + x - 26$.</sub>

**Pembahasan:** $(x - 5)(x + 6) = x^2 + x - 30$, lalu ditambah sisa $4$ menjadi $x^2 + x - 26$.
**Acuan:** siswa — siswa hal.87

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b02-c-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: pembagian bersusun*

Sebelum dibagi secara bersusun oleh $x^2 + x - 1$, polinomial $x^3 - 5x + 2$ perlu ditulis lengkap menjadi ....

- A. $x^3 + 1x^2 - 5x + 2$  
  <sub>Salah: menyisipkan koefisien $1$ sehingga nilai polinomial berubah</sub>
- **B. $x^3 + 0x^2 - 5x + 2$** ✅  
  <sub>Benar: Suku $x^2$ tidak ada, sehingga disisipkan $0x^2$ agar suku-sukunya lengkap.</sub>
- C. $0x^3 + x^2 - 5x + 2$  
  <sub>Salah: mengira suku pangkat tertinggi yang kosong</sub>
- D. $x^3 - 5x^2 + 0x + 2$  
  <sub>Salah: memindahkan koefisien $-5$ ke suku $x^2$</sub>

**Pembahasan:** Polinomial menjadi $x^3 + 0x^2 - 5x + 2$ sebelum pembagian bersusun.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b02-c-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: Teorema Sisa*

Diketahui $P(x) = (x - 3)(x^2 + 2x + 5) + 4$. Nilai $P(3)$ adalah ....

- **A. $4$** ✅  
  <sub>Benar: Pembagi $x - 3$, hasil bagi $x^2 + 2x + 5$, sisa $4$. Menurut Teorema Sisa $P(3) = 4$ (suku pertama bernilai $0$ di $x = 3$).</sub>
- B. $0$  
  <sub>Salah: mengira faktor $x - 3 = 0$ membuat seluruh $P(3)$ bernilai nol</sub>
- C. $24$  
  <sub>Salah: menjumlahkan nilai hasil bagi di $x = 3$ ($20$) dengan sisa $4$</sub>
- D. $-4$  
  <sub>Salah: salah tanda pada sisa</sub>

**Pembahasan:** Substitusi $x = 3$: $(0)(20) + 4 = 4$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b02-c-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: membaca skema Horner*

Pembagian $3x^3 - 5x^2 + 2x + 9$ oleh $x - 2$ dengan metode Horner menghasilkan baris bawah $3, 1, 4, 17$. Hasil bagi dan sisa pembagian tersebut adalah ....

- A. hasil bagi $3x^2 + x + 4$, sisa $9$  
  <sub>Salah: mengambil konstanta awal polinomial sebagai sisa</sub>
- **B. hasil bagi $3x^2 + x + 4$, sisa $17$** ✅  
  <sub>Benar: Angka terakhir ($17$) adalah sisa; angka lainnya ($3, 1, 4$) menjadi koefisien hasil bagi yang berderajat satu lebih rendah.</sub>
- C. hasil bagi $3x^3 + x^2 + 4x + 17$, sisa $0$  
  <sub>Salah: menganggap semua angka pada baris bawah sebagai hasil bagi</sub>
- D. hasil bagi $3x^2 + x + 17$, sisa $4$  
  <sub>Salah: hasil bagi dan sisa tertukar posisi angkanya</sub>

**Pembahasan:** Baris bawah $3, 1, 4, 17$: hasil bagi $3x^2 + x + 4$, sisa $17$.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b02-c-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: pembagian bersusun*

Pada pembagian bersusun $6x^3 + 7x^2 - 4x + 5$ oleh $2x - 1$, suku pertama hasil bagi adalah ....

- **A. $3x^2$** ✅  
  <sub>Benar: Suku pertama diperoleh dari $6x^3 : 2x = 3x^2$.</sub>
- B. $\frac{1}{3}x^2$  
  <sub>Salah: membagi koefisien pembagi dengan koefisien polinomial (terbalik)</sub>
- C. $3x^3$  
  <sub>Salah: pangkat tidak dikurangi saat membagi $x^3$ dengan $x$</sub>
- D. $6x^2$  
  <sub>Salah: membagi pangkat tetapi lupa membagi koefisien dengan $2$</sub>

**Pembahasan:** $6x^3 : 2x = 3x^2$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b02-c-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: bentuk algoritma pembagian*

Bilangan $58$ dibagi $9$ memberi hasil bagi $6$ dan sisa $4$. Bentuk algoritma pembagian yang sesuai adalah ....

- **A. $58 = 9 \cdot 6 + 4$** ✅  
  <sub>Benar: Bilangan yang dibagi $=$ pembagi $\times$ hasil bagi $+$ sisa, yaitu $58 = 9 \cdot 6 + 4$.</sub>
- B. $58 = 6 \cdot 4 + 9$  
  <sub>Salah: peran pembagi dan sisa tertukar</sub>
- C. $58 = 9 \cdot 4 + 6$  
  <sub>Salah: hasil bagi dan sisa tertukar</sub>
- D. $9 = 58 \cdot 6 + 4$  
  <sub>Salah: bilangan yang dibagi dan pembagi tertukar</sub>

**Pembahasan:** $9 \cdot 6 + 4 = 58$.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b02-c-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: penulisan skema Horner*

Metode Horner dapat dipakai secara langsung jika pembaginya berbentuk $x - c$. Pembagi berikut yang dapat langsung memakai metode Horner adalah ....

- A. $x^2 - x + 1$  
  <sub>Salah: pembagi kuadrat bukan bentuk $x - c$</sub>
- **B. $x - 3$** ✅  
  <sub>Benar: Hanya $x - 3$ yang berbentuk $x - c$ (dengan $c = 3$).</sub>
- C. $x^3 + 2$  
  <sub>Salah: pembagi berderajat tiga bukan bentuk $x - c$</sub>
- D. $x^2 + 1$  
  <sub>Salah: pembagi berderajat dua bukan bentuk $x - c$</sub>

**Pembahasan:** Syarat metode Horner langsung: pembagi berbentuk $x - c$.
**Acuan:** siswa — siswa hal.87

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b02-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: Horner pembagi ax - b*

Gunakan metode Horner untuk membagi $6x^3 + 7x^2 - 6x + 29$ dengan $2x + 5$. Hasil bagi dan sisanya adalah ....

- A. hasil bagi $3x^2 - 4x + 7$, sisa $6$  
  <sub>Salah: salah tanda pada sisa</sub>
- B. hasil bagi $6x^2 - 8x + 14$, sisa $-6$  
  <sub>Salah: lupa membagi hasil bagi Horner dengan $2$ (koefisien $x$ pada pembagi)</sub>
- C. hasil bagi $3x^2 - 4x + 7$, sisa $29$  
  <sub>Salah: mengambil konstanta polinomial sebagai sisa tanpa Horner</sub>
- **D. hasil bagi $3x^2 - 4x + 7$, sisa $-6$** ✅  
  <sub>Benar: $2x + 5 = 2(x + \frac{5}{2})$ sehingga $c = -\frac{5}{2}$. Horner pada $6, 7, -6, 29$ memberi baris $6, -8, 14, -6$, yaitu $P = (x + \frac{5}{2})(6x^2 - 8x + 14) - 6$. Karena $x + \frac{5}{2} = \frac{1}{2}(2x + 5)$, hasil bagi terhadap $2x + 5$ adalah $3x^2 - 4x + 7$ dan sisa tetap $-6$.</sub>

**Pembahasan:** $2x + 5 = 2(x - (-\frac{5}{2}))$. Horner dengan $c = -\frac{5}{2}$: $6, -8, 14, -6$. Hasil bagi terhadap $x - c$ adalah $6x^2 - 8x + 14$; terhadap $2x + 5$ dibagi $2$ menjadi $3x^2 - 4x + 7$; sisa $-6$.
**Acuan:** siswa — siswa hal.89 Mari Berkolaborasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b02-c-medium-bt01-002
*variasi (angka) | C4 | 4 langkah | jenis: Horner dua kali (pembagi kuadrat terfaktor)*

Polinomial $P(x) = x^4 - 4x^3 - 39x^2 + 225x - 345$ dibagi $(x - 6)(x + 7)$ dengan metode Horner dua kali: pertama dibagi $x - 6$, lalu hasil baginya dibagi $x + 7$. Hasil bagi akhir pembagian $P(x)$ oleh $(x - 6)(x + 7)$ adalah ....

- A. $7x - 9$  
  <sub>Salah: mengambil sisa sebagai hasil bagi</sub>
- B. $x^3 + 2x^2 - 27x + 63$  
  <sub>Salah: berhenti setelah Horner pertama: itu hasil bagi oleh $x - 6$ saja</sub>
- C. $x^2 + 9x + 36$  
  <sub>Salah: memakai $c = 7$ pada Horner kedua padahal pembagi $x + 7$ berarti $c = -7$</sub>
- **D. $x^2 - 5x + 8$** ✅  
  <sub>Benar: Horner $c = 6$ memberi hasil bagi $x^3 + 2x^2 - 27x + 63$. Horner $c = -7$ pada hasil itu memberi hasil bagi $x^2 - 5x + 8$, itulah hasil bagi terhadap $(x - 6)(x + 7)$.</sub>

**Pembahasan:** Horner $c = 6$: koefisien baru [1, 2, -27, 63], sisa 33. Horner $c = -7$ pada [1, 2, -27, 63]: koefisien [1, -5, 8]. Hasil bagi akhir $x^2 - 5x + 8$ (cek: $(x-6)(x+7)(x^2 - 5x + 8) + 7x - 9 = P(x)$).
**Acuan:** siswa — siswa hal.90 Mari Berkolaborasi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b02-c-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: pembagian bersusun*

Misalkan $P(x) = x^5 - 8x^3 + 6x - 7$ dan $Q(x) = x^2 + 3x - 5$. Hasil bagi dan sisa pembagian $P(x)$ oleh $Q(x)$ dengan pembagian bersusun adalah ....

- A. $H(x) = x^3 + 3x^2 + 6x + 33$ dan $S(x) = 135x + 158$  
  <sub>Salah: tanda suku $x$ pembagi terbalik ($x^2 - 3x - 5$)</sub>
- B. $H(x) = x^3 + 3x^2 - 4x - 27$ dan $S(x) = -55x + 128$  
  <sub>Salah: kedua tanda pembagi terbalik ($x^2 - 3x + 5$)</sub>
- **C. $H(x) = x^3 - 3x^2 + 6x - 33$ dan $S(x) = 135x - 172$** ✅  
  <sub>Benar: Setelah menyisipkan suku nol, pembagian bersusun menghasilkan $H(x) = x^3 - 3x^2 + 6x - 33$ dan $S(x) = 135x - 172$.</sub>
- D. $H(x) = x^3 - 3x^2 - 4x + 27$ dan $S(x) = -55x - 142$  
  <sub>Salah: tanda konstanta pembagi terbalik ($x^2 + 3x + 5$)</sub>

**Pembahasan:** Tulis $P(x) = x^5 + 0x^4 - 8x^3 + 0x^2 + 6x - 7$ lalu bagi bersusun oleh $x^2 + 3x - 5$: $H(x) = x^3 - 3x^2 + 6x - 33$, $S(x) = 135x - 172$. Cek: $Q \cdot H + S = P$.
**Acuan:** siswa — siswa hal.94 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b02-c-medium-bt01-004
*variasi (angka) | C4 | 4 langkah | jenis: sisa pembagi kuadrat dari dua syarat sisa*

Polinomial $P(x)$ jika dibagi $x - 6$ bersisa $31$, dan jika dibagi $x + 4$ bersisa $-9$. Sisa pembagian $P(x)$ oleh $x^2 - 2x - 24$ adalah ....

- **A. $4x + 7$** ✅  
  <sub>Benar: Karena $x^2 - 2x - 24 = (x - 6)(x + 4)$, sisanya $S(x) = ax + b$. Teorema Sisa: $P(6) = 6a + b = 31$ dan $P(-4) = -4a + b = -9$. Pengurangan memberi $10a = 40$, $a = 4$, $b = 7$.</sub>
- B. $4x - 7$  
  <sub>Salah: benar $a = 4$ tetapi salah tanda saat mencari $b$ ($b = 31 - 24$)</sub>
- C. $-4x + 15$  
  <sub>Salah: dua nilai sisa tertukar saat disubstitusikan</sub>
- D. $20x - 89$  
  <sub>Salah: memakai $P(4) = -9$ (salah tanda pembuat nol $x + 4$)</sub>

**Pembahasan:** $S(x) = ax + b$. $6a + b = 31$ dan $-4a + b = -9$ sehingga $a = 4$, $b = 7$. Jadi $S(x) = 4x + 7$.
**Acuan:** siswa — siswa hal.94 Latihan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b02-c-medium-bt01-005
*variasi (angka) | C3 | 4 langkah | jenis: Teorema Sisa dengan Horner (nilai pecahan)*

Misalkan $P(x) = 16x^4 + 8x^3 - 18x^2 + 7x - 13$ dan $c = -\frac{1}{2}$. Dengan metode Horner dan Teorema Sisa, nilai $P(c)$ adalah ....

- A. $-12$  
  <sub>Salah: mensubstitusi $c = \frac{1}{2}$ (salah tanda)</sub>
- B. $93$  
  <sub>Salah: mensubstitusi $c = -2$ (pecahan dibalik)</sub>
- **C. $-21$** ✅  
  <sub>Benar: Horner $c = -\frac{1}{2}$: $16$; $8 - 8 = 0$; $-18 + 0 = -18$; $7 + 9 = 16$; $-13 - 8 = -21$. Sisa terakhir $-21 = P(-\frac{1}{2})$.</sub>
- D. $-8$  
  <sub>Salah: berhenti sebelum menjumlahkan konstanta terakhir $-13$</sub>

**Pembahasan:** Horner dengan $c = -\frac{1}{2}$ memberi baris $16, 0, -18, 16, -21$. Maka $P(-\frac{1}{2}) = -21$.
**Acuan:** pretest — kelas11_tl-b02-p0094-latihan-c-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b02-c-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: Teorema Sisa dengan Horner (hasil bagi dan P(c))*

Jika $P(x) = 7x^4 + 15x^3 - 9x^2 + 6x - 11$ dibagi dengan $x + 2$, hasil bagi dan nilai $P(-2)$ yang diperoleh dengan Teorema Sisa berturut-turut adalah ....

- A. $7x^3 + 29x^2 + 49x + 104$ dan $197$  
  <sub>Salah: memakai $c = 2$ padahal pembagi $x + 2$ berarti $c = -2$</sub>
- B. $7x^3 + x^2 - 11x + 28$ dan $67$  
  <sub>Salah: salah tanda pada sisa/nilai $P(-2)$</sub>
- **C. $7x^3 + x^2 - 11x + 28$ dan $-67$** ✅  
  <sub>Benar: $x + 2 = x - (-2)$. Horner $c = -2$: $7, 1, -11, 28, -67$. Hasil bagi $7x^3 + x^2 - 11x + 28$, sisa $-67 = P(-2)$.</sub>
- D. $7x^3 + x^2 - 11x + 28$ dan $28$  
  <sub>Salah: mengambil konstanta hasil bagi sebagai nilai $P(-2)$</sub>

**Pembahasan:** Horner $c = -2$ pada $7, 15, -9, 6, -11$: $7, 1, -11, 28, -67$. Hasil bagi $7x^3 + x^2 - 11x + 28$ dan sisa $-67$, sehingga $P(-2) = -67$.
**Acuan:** siswa — siswa hal.92 Mari Mencoba 2.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b02-c-medium-bt01-007
*variasi (angka) | C3 | 4 langkah | jenis: pembagian bersusun*

Bagilah $5x^4 - 6x^3 + 8x - 9$ dengan $x^2 + 3x - 7$. Hasil pembagian yang ditulis dalam bentuk algoritma pembagian adalah ....

- **A. $5x^4 - 6x^3 + 8x - 9 = (x^2 + 3x - 7)(5x^2 - 21x + 98) - 433x + 677$** ✅  
  <sub>Benar: Setelah menyisipkan $0x^2$, pembagian bersusun menghasilkan $H(x) = 5x^2 - 21x + 98$ dan $S(x) = -433x + 677$ sehingga $P = Q \cdot H + S$.</sub>
- B. $5x^4 - 6x^3 + 8x - 9 = (x^2 - 3x - 7)(5x^2 + 9x + 62) + 257x + 425$  
  <sub>Salah: tanda suku $x$ pembagi terbalik ($x^2 - 3x - 7$)</sub>
- C. $5x^4 - 6x^3 + 8x - 9 = (x^2 - 3x + 7)(5x^2 + 9x - 8) - 79x + 47$  
  <sub>Salah: kedua tanda pembagi terbalik ($x^2 - 3x + 7$)</sub>
- D. $5x^4 - 6x^3 + 8x - 9 = (x^2 + 3x + 7)(5x^2 - 21x + 28) + 71x - 205$  
  <sub>Salah: tanda konstanta pembagi terbalik ($x^2 + 3x + 7$)</sub>

**Pembahasan:** Bagi bersusun $5x^4 - 6x^3 + 0x^2 + 8x - 9$ oleh $x^2 + 3x - 7$: $H = 5x^2 - 21x + 98$, $S = -433x + 677$.
**Acuan:** siswa — siswa hal.86 Contoh 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b02-c-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: Horner: hasil bagi dan sisa*

Gunakan metode Horner untuk membagi $3x^4 + 7x^2 - 8$ dengan $x + 2$. Hasil baginya adalah ....

- A. $3x^3 + 6x^2 + 19x + 38$  
  <sub>Salah: memakai $c = 2$ padahal pembagi $x + 2$ berarti $c = -2$</sub>
- **B. $3x^3 - 6x^2 + 19x - 38$** ✅  
  <sub>Benar: Koefisien $3, 0, 7, 0, -8$ dengan $c = -2$ menghasilkan baris $3, -6, 19, -38, 68$. Empat angka pertama adalah koefisien hasil bagi, $68$ sisanya.</sub>
- C. $3x^3 - 6x^2 + 19x + 68$  
  <sub>Salah: mengambil sisa $68$ sebagai suku konstan hasil bagi</sub>
- D. $3x^2 - 6x + 19$  
  <sub>Salah: lupa koefisien nol untuk $x$ sehingga hanya empat koefisien ($3, 0, 7, -8$) dihitung</sub>

**Pembahasan:** Baris Horner: $3$; $0 - 6 = -6$; $7 + 12 = 19$; $0 - 38 = -38$; $-8 + 76 = 68$. Hasil bagi $3x^3 - 6x^2 + 19x - 38$, sisa $68$.
**Acuan:** siswa — siswa hal.88 Contoh 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b02-c-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: Horner: hasil bagi dan sisa*

Hasil bagi dan sisa pembagian $(x^5 - 7) : (x - 2)$ adalah ....

- A. hasil bagi $x^4 + 2x^3 + 4x^2 + 8x + 16$, sisa $16$  
  <sub>Salah: mengambil koefisien terakhir hasil bagi sebagai sisa</sub>
- B. hasil bagi $x^4 - 2x^3 + 4x^2 - 8x + 16$, sisa $-39$  
  <sub>Salah: memakai $c = -2$ padahal pembagi $x - 2$ berarti $c = 2$</sub>
- C. hasil bagi $x^4 + 2x^3 + 4x^2 + 8x + 16$, sisa $-7$  
  <sub>Salah: mengira konstanta polinomial menjadi sisa tanpa dihitung</sub>
- **D. hasil bagi $x^4 + 2x^3 + 4x^2 + 8x + 16$, sisa $25$** ✅  
  <sub>Benar: Koefisien $1, 0, 0, 0, 0, -7$ dengan $c = 2$ memberi baris $1, 2, 4, 8, 16, 25$. Lima angka pertama hasil bagi, angka terakhir sisa.</sub>

**Pembahasan:** Horner $c = 2$: $1, 2, 4, 8, 16, 25$. Hasil bagi $x^4 + 2x^3 + 4x^2 + 8x + 16$, sisa $25$.
**Acuan:** siswa — siswa hal.87 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b02-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: Teorema Sisa pembagi ax - b*

Sisa pembagian $P(x) = 8x^3 + 10x^2 - 5x + 7$ oleh $2x + 3$ adalah ....

- A. $49$  
  <sub>Salah: mensubstitusi $x = \frac{3}{2}$ (salah tanda pembuat nol)</sub>
- **B. $10$** ✅  
  <sub>Benar: Pembuat nol $2x + 3$ adalah $x = -\frac{3}{2}$, sehingga sisa $= P(-\frac{3}{2}) = -27 + \frac{45}{2} + \frac{15}{2} + 7 = 10$.</sub>
- C. $-104$  
  <sub>Salah: mensubstitusi $x = -3$ tanpa membagi dengan koefisien $2$</sub>
- D. $298$  
  <sub>Salah: mensubstitusi $x = 3$ (salah tanda dan tidak dibagi $2$)</sub>

**Pembahasan:** $2x + 3 = 0$ memberi $x = -\frac{3}{2}$. $P(-\frac{3}{2}) = 8(-\frac{27}{8}) + 10(\frac{9}{4}) - 5(-\frac{3}{2}) + 7 = -27 + 22,5 + 7,5 + 7 = 10$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b02-c-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: parameter Teorema Sisa (satu syarat)*

Polinomial $P(x) = 2x^3 + kx^2 - 5x + 7$ jika dibagi $x + 2$ bersisa $25$. Nilai $k$ yang memenuhi adalah ....

- A. $11$  
  <sub>Salah: salah tanda pada suku $-5x$: $-5(-2)$ dihitung $-10$</sub>
- B. $3$  
  <sub>Salah: mensubstitusi $x = 2$ padahal pembagi $x + 2$ berarti $x = -2$</sub>
- **C. $6$** ✅  
  <sub>Benar: Teorema Sisa: $P(-2) = 2(-8) + 4k + 10 + 7 = 4k + 1 = 25$, sehingga $k = 6$.</sub>
- D. $12$  
  <sub>Salah: menghitung $kx^2$ di $x = -2$ sebagai $2k$ (lupa mengkuadratkan)</sub>

**Pembahasan:** $P(-2) = -16 + 4k + 10 + 7 = 4k + 1$. Dari $4k + 1 = 25$ diperoleh $k = 6$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b02-c-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: parameter Teorema Sisa (dua syarat)*

Polinomial $P(x) = x^3 + ax^2 + bx - 8$ jika dibagi $x - 2$ bersisa $2$ dan jika dibagi $x + 3$ bersisa $7$. Nilai $a \cdot b$ adalah ....

- A. $8$  
  <sub>Salah: menghitung $a - b$, bukan $a \cdot b$</sub>
- B. $-2$  
  <sub>Salah: menghitung $a + b$, bukan $a \cdot b$</sub>
- **C. $-15$** ✅  
  <sub>Benar: $P(2) = 4a + 2b = 2$ atau $2a + b = 1$. $P(-3) = -35 + 9a - 3b = 7$ atau $3a - b = 14$. Penjumlahan: $5a = 15$, $a = 3$, $b = -5$, sehingga $ab = -15$.</sub>
- D. $-55$  
  <sub>Salah: memakai $x = 3$ untuk pembagi $x + 3$ sehingga $a = -5$, $b = 11$</sub>

**Pembahasan:** $P(2) = 8 + 4a + 2b - 8 = 2$ sehingga $2a + b = 1$. $P(-3) = -27 + 9a - 3b - 8 = 7$ sehingga $3a - b = 14$. Maka $a = 3$, $b = -5$, $ab = -15$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b02-c-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: menyusun polinomial dari hasil pembagian*

Pembagian polinomial $P(x)$ oleh $x + 2$ dengan metode Horner menghasilkan hasil bagi $2x^2 - 3x + 5$ dan sisa $4$. Polinomial $P(x)$ adalah ....

- **A. $2x^3 + x^2 - x + 14$** ✅  
  <sub>Benar: $P(x) = (x + 2)(2x^2 - 3x + 5) + 4 = 2x^3 + x^2 - x + 10 + 4 = 2x^3 + x^2 - x + 14$.</sub>
- B. $2x^3 + x^2 - x + 10$  
  <sub>Salah: lupa menambahkan sisa $4$</sub>
- C. $2x^3 - 7x^2 + 11x - 6$  
  <sub>Salah: memakai pembagi $x - 2$ padahal pembagi sebenarnya $x + 2$</sub>
- D. $2x^3 + x^2 - x + 6$  
  <sub>Salah: mengurangkan sisa, bukan menambahkan</sub>

**Pembahasan:** $(x + 2)(2x^2 - 3x + 5) = 2x^3 + x^2 - x + 10$. Tambah sisa $4$: $2x^3 + x^2 - x + 14$.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b02-c-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: konsep derajat hasil bagi dan sisa*

Polinomial $P(x)$ berderajat $11$ dibagi $Q(x)$ sehingga hasil baginya berderajat $7$. Pernyataan yang benar adalah ....

- A. $Q(x)$ berderajat $18$ dan sisa paling tinggi berderajat $17$  
  <sub>Salah: menjumlahkan derajat, bukan mengurangkan</sub>
- **B. $Q(x)$ berderajat $4$ dan sisa paling tinggi berderajat $3$** ✅  
  <sub>Benar: Derajat $P$ = derajat $Q$ + derajat hasil bagi, sehingga derajat $Q = 11 - 7 = 4$. Sisa berderajat kurang dari $4$, yaitu paling tinggi $3$.</sub>
- C. $Q(x)$ berderajat $5$ dan sisa paling tinggi berderajat $4$  
  <sub>Salah: salah hitung derajat pembagi ($11 - 7 + 1$)</sub>
- D. $Q(x)$ berderajat $4$ dan sisa paling tinggi berderajat $4$  
  <sub>Salah: mengira sisa boleh berderajat sama dengan pembagi</sub>

**Pembahasan:** $11 = \deg Q + 7$ sehingga $\deg Q = 4$. Sisa nol atau berderajat kurang dari $4$, jadi paling tinggi $3$.
**Acuan:** siswa — siswa hal.93

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b02-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: bentuk algoritma pembagian*

Diketahui $P(x) = 2x^3 - 5x^2 + 9x - 4$ dibagi $Q(x) = x^2 + 2x - 3$ dengan hasil bagi $H(x) = 2x - 9$. Sisa pembagian tersebut adalah ....

- A. $33x + 23$  
  <sub>Salah: salah tanda saat mengurangkan konstanta ($-4 + 27$)</sub>
- B. $-33x + 31$  
  <sub>Salah: mengurangkan terbalik: $Q \cdot H - P$</sub>
- C. $-15x - 31$  
  <sub>Salah: salah tanda saat mengurangkan suku $x$ ($9 - 24$)</sub>
- **D. $33x - 31$** ✅  
  <sub>Benar: $Q \cdot H = 2x^3 - 5x^2 - 24x + 27$. Sisa $S = P - Q \cdot H = (9 + 24)x + (-4 - 27) = 33x - 31$.</sub>

**Pembahasan:** $Q \cdot H = 2x^3 + 4x^2 - 6x - 9x^2 - 18x + 27 = 2x^3 - 5x^2 - 24x + 27$. $S = P - QH = 33x - 31$.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b02-c-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: analisis kesalahan Horner*

Dina membagi $x^3 + 5x - 3$ oleh $x + 2$ dengan metode Horner. Ia menuliskan koefisien $1, 0, 5, -3$ dan memakai $c = 2$, sehingga memperoleh baris $1, 2, 9, 15$ dan menyimpulkan sisanya $15$. Sisa pembagian yang benar adalah ....

- **A. $-21$** ✅  
  <sub>Benar: Pembagi $x + 2 = x - (-2)$ sehingga $c = -2$ (kesalahan Dina). Horner: $1, -2, 9, -21$, sisa $-21$.</sub>
- B. $-9$  
  <sub>Salah: menghilangkan koefisien nol $x^2$ sehingga hanya $1, 5, -3$ yang dihitung</sub>
- C. $21$  
  <sub>Salah: salah tanda pada sisa</sub>
- D. $15$  
  <sub>Salah: mengikuti pekerjaan Dina yang memakai $c = 2$</sub>

**Pembahasan:** Dengan $c = -2$: $1$; $0 + (-2)(1) = -2$; $5 + (-2)(-2) = 9$; $-3 + (-2)(9) = -21$. Sisa $-21$. Cek: $P(-2) = -8 - 10 - 3 = -21$.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b02-c-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: soal cerita pembagian polinomial*

Volume sebuah balok adalah $V(x) = x^3 + 4x^2 - 11x - 30$ cm$^3$ dan tingginya $(x - 3)$ cm. Jika $x = 6$, luas alas balok tersebut adalah .... cm$^2$.

- **A. $88$** ✅  
  <sub>Benar: Luas alas $= V(x) : (x - 3)$. Horner $c = 3$ pada $1, 4, -11, -30$ memberi $1, 7, 10, 0$, sehingga luas alas $x^2 + 7x + 10$. Untuk $x = 6$: $36 + 42 + 10 = 88$.</sub>
- B. $264$  
  <sub>Salah: menghitung volume $V(6)$, bukan luas alas</sub>
- C. $28$  
  <sub>Salah: memakai $c = -3$ pada Horner sehingga luas alas menjadi $x^2 + x - 14$</sub>
- D. $40$  
  <sub>Salah: mensubstitusi $x = 3$ (pembuat nol tinggi) ke $x^2 + 7x + 10$</sub>

**Pembahasan:** $V = (\text{luas alas})(\text{tinggi})$. Horner $c = 3$: $1, 7, 10, 0$; luas alas $x^2 + 7x + 10$. Di $x = 6$: $88$ cm$^2$ (cek $264 : 3 = 88$).
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b02-c-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: Teorema Sisa dari bentuk algoritma*

Diketahui $P(x) = (x + 4)(x^2 - 3x + 6) - 7$. Sisa pembagian $P(x)$ oleh $x - 2$ adalah ....

- A. $-7$  
  <sub>Salah: mengira sisa pembagian oleh $x - 2$ adalah suku konstan bentuk algoritma yang diberikan</sub>
- **B. $17$** ✅  
  <sub>Benar: Menurut Teorema Sisa, sisa $= P(2) = (6)(4 - 6 + 6) - 7 = 24 - 7 = 17$.</sub>
- C. $24$  
  <sub>Salah: lupa mengurangkan $7$ setelah mengalikan $(x + 4)$ dengan hasil bagi</sub>
- D. $25$  
  <sub>Salah: mensubstitusi $x = -2$ (salah tanda pembuat nol)</sub>

**Pembahasan:** $P(2) = (2 + 4)(4 - 6 + 6) - 7 = 6 \cdot 4 - 7 = 17$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b02-c-medium-bt01-019
*orisinal | C3 | 4 langkah | jenis: pembagian bersusun*

Hasil bagi dan sisa pembagian $x^4 - 3x^2 + 7x - 5$ oleh $x^2 - 2$ adalah ....

- A. $H(x) = 7x - 7$ dan $S(x) = x^2 - 1$  
  <sub>Salah: hasil bagi dan sisa tertukar</sub>
- B. $H(x) = x^2 - 1$ dan $S(x) = 7x - 3$  
  <sub>Salah: salah tanda saat mengurangkan konstanta ($-5 - 2$ dihitung $-5 + 2$)</sub>
- C. $H(x) = x^2 - 1$ dan $S(x) = 7x - 5$  
  <sub>Salah: lupa mengurangkan hasil kali $-1 \cdot (-2)$ pada konstanta</sub>
- **D. $H(x) = x^2 - 1$ dan $S(x) = 7x - 7$** ✅  
  <sub>Benar: $x^2 \cdot (x^2 - 2) = x^4 - 2x^2$ menyisakan $-x^2 + 7x - 5$ (dengan $0x^3$). $-1 \cdot (x^2 - 2) = -x^2 + 2$ menyisakan $7x - 7$.</sub>

**Pembahasan:** Bentuk lengkap $x^4 + 0x^3 - 3x^2 + 7x - 5$. $H = x^2 - 1$, $S = 7x - 7$. Cek: $(x^2 - 2)(x^2 - 1) + 7x - 7 = x^4 - 3x^2 + 2 + 7x - 7$.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b02-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: Horner: koefisien hasil bagi*

Polinomial $3x^4 - 11x^3 + 9x - 8$ dibagi $x - 4$ dengan metode Horner. Koefisien $x$ pada hasil bagi adalah ....

- A. $92$  
  <sub>Salah: mengambil sisa sebagai koefisien $x$</sub>
- **B. $4$** ✅  
  <sub>Benar: Koefisien $3, -11, 0, 9, -8$ dengan $c = 4$ memberi baris $3, 1, 4, 25, 92$. Hasil bagi $3x^3 + x^2 + 4x + 25$, sisa $92$. Koefisien $x$ adalah $4$.</sub>
- C. $25$  
  <sub>Salah: mengambil suku konstan hasil bagi</sub>
- D. $1$  
  <sub>Salah: mengambil koefisien $x^2$ pada hasil bagi</sub>

**Pembahasan:** Horner $c = 4$: $3$; $-11 + 12 = 1$; $0 + 4 = 4$; $9 + 16 = 25$; $-8 + 100 = 92$. Hasil bagi $3x^3 + x^2 + 4x + 25$.
**Acuan:** siswa — siswa hal.89

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b02-c-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim Teorema Sisa pembagi ax-b*

Ahmad menduga bahwa sisa pembagian $P(x)$ oleh $ax - b$ sama dengan $P\left(\frac{a}{b}\right)$. Untuk menguji dugaan itu, ia memakai $P(x) = 8x^3 + 6x^2 - 13x + 9$ yang dibagi $2x - 3$. Pernyataan yang benar adalah ....

- **A. Dugaan Ahmad salah; sisa sebenarnya $P\left(\frac{3}{2}\right) = 30$, sedangkan $P\left(\frac{2}{3}\right) = \frac{145}{27}$** ✅  
  <sub>Benar: pembuat nol $2x-3$ adalah $x=\frac{3}{2}$, sehingga sisanya $P(\frac{3}{2})=30$, berbeda dari $P(\frac{2}{3})$</sub>
- B. Dugaan Ahmad benar; sisanya $P\left(\frac{2}{3}\right) = \frac{145}{27}$  
  <sub>Salah: mengira pembuat nol $ax-b$ adalah $a/b$ (pecahan terbalik)</sub>
- C. Dugaan Ahmad salah; sisa sebenarnya $P(3) = 240$  
  <sub>Salah: memakai $b$ saja sebagai pembuat nol dan mengabaikan pembagian dengan $a$</sub>
- D. Dugaan Ahmad salah; sisa sebenarnya $P\left(-\frac{3}{2}\right) = 15$  
  <sub>Salah: salah tanda pembuat nol $2x-3$</sub>

**Pembahasan:** Pembuat nol $2x-3$ adalah $\frac{3}{2}$ sehingga sisa $=P(\frac32)=30$ (dicek dengan algoritma pembagian). Nilai $P(\frac23)=\frac{145}{27}\neq 30$, jadi dugaan Ahmad dibantah.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b02-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal klaim polinomial*

Seorang siswa mengklaim: "Jika $P(2) = P(-2)$, maka $P(x)$ habis dibagi $x^2 - 4$." Polinomial yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $x^4 - 5x^2 + 4$  
  <sub>Salah: memenuhi syarat dan juga habis dibagi $x^2-4$ (P(2)=P(-2)=0), jadi justru mendukung klaim</sub>
- B. $x^3 - 3x^2 + 2$  
  <sub>Salah: $P(2)=-2$ dan $P(-2)=-18$ tidak sama sehingga syarat klaim tidak terpenuhi, bukan penyangkal</sub>
- C. $x^3 + x^2 - 4$  
  <sub>Salah: $P(2)=8$ dan $P(-2)=-8$ tidak sama sehingga syarat klaim tidak terpenuhi, bukan penyangkal</sub>
- **D. $x^4 - 3x^2 + 5$** ✅  
  <sub>Benar: $P(2)=P(-2)=9$ sehingga syarat klaim terpenuhi, tetapi sisa pembagian oleh $x^2-4$ adalah $9\neq0$</sub>

**Pembahasan:** Penyangkal harus memenuhi syarat ($P(2)=P(-2)$) tetapi tidak memenuhi kesimpulan (sisa oleh $x^2-4$ tidak nol). Hanya $x^4-3x^2+5$: $P(\pm2)=9$, sisa $9$.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b02-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan Horner (suku nol hilang)*

Wulan membagi $P(x) = x^4 - 7x^2 + 3x - 9$ oleh $x - 2$ dengan metode Horner. Ia menuliskan koefisien $1, -7, 3, -9$ dan memakai $c = 2$ sehingga memperoleh baris bawah $1, -5, -7, -23$, lalu menyimpulkan sisanya $-23$. Pernyataan yang benar mengenai pekerjaan Wulan adalah ....

- A. Ia salah karena suku konstan tidak boleh ditulis; sisa sebenarnya $-6$  
  <sub>Salah: mengira suku konstan tidak masuk skema Horner</sub>
- B. Pekerjaannya benar karena sisa Horner selalu $-23$ walau suku nol dilewati  
  <sub>Salah: mengira suku berkoefisien nol boleh dilewati</sub>
- **C. Ia salah karena koefisien $x^3$ yang bernilai nol tidak ditulis; sisa sebenarnya $-15$** ✅  
  <sub>Benar: koefisien lengkap harus $1,0,-7,3,-9$; hasilnya baris bawah $1,2,-3,-3,-15$</sub>
- D. Ia salah karena seharusnya $c = -2$; sisa sebenarnya $-27$  
  <sub>Salah: mengira pembagi $x-2$ memakai $c=-2$</sub>

**Pembahasan:** Dengan koefisien lengkap $1,0,-7,3,-9$ dan $c=2$: baris bawah $1,2,-3,-3,-15$, sisa $-15$ (sama dengan $P(2)$). Wulan melewatkan koefisien $0$ sehingga kolomnya bergeser.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b02-c-hard-bt01-004
*orisinal | C5 | 6 langkah | jenis: temukan kesalahan Horner dua kali (pembagi kuadrat)*

Raka membagi $P(x) = 3x^3 - 4x^2 - 17x + 9$ oleh $(x - 2)(x + 1)$ dengan Horner dua kali: pertama dibagi $x - 2$, lalu hasil baginya dibagi $x + 1$. Ia memperoleh sisa tahap pertama $-17$ dan sisa tahap kedua $-12$, kemudian menyatakan bahwa sisa pembagian $P(x)$ oleh $(x - 2)(x + 1)$ adalah $-12$. Pernyataan yang benar adalah ....

- A. Raka keliru; sisa yang benar adalah $-12x - 29$  
  <sub>Salah: mengalikan sisa tahap kedua dengan faktor kedua, bukan faktor pertama</sub>
- B. Raka benar; sisanya $-12$  
  <sub>Salah: mengira hanya sisa tahap kedua yang menjadi sisa akhir</sub>
- **C. Raka keliru; sisa yang benar adalah $-12x + 7$** ✅  
  <sub>Benar: $P=(x-2)H_1+S_1$ dan $H_1=(x+1)H_2+S_2$ sehingga $P=(x-2)(x+1)H_2+S_2(x-2)+S_1$</sub>
- D. Raka keliru; sisa yang benar adalah $-29$  
  <sub>Salah: menjumlahkan kedua sisa tahap tanpa memperhatikan faktor pembagi</sub>

**Pembahasan:** $P=(x-2)H_1+S_1$, $H_1=(x+1)H_2+S_2$ sehingga sisa akhir $=S_2(x-2)+S_1=-12x + 7$.
**Acuan:** siswa — siswa hal.94

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b02-c-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan pembagian bersusun*

Doni membagi $P(x) = 2x^3 - 3x^2 - 7x + 4$ oleh $Q(x) = x^2 - 2x + 5$ secara bersusun. Suku pertama hasil bagi ia tulis $2x$, lalu ia mengurangkan $2x \cdot Q(x) = 2x^3 - 4x^2 + 10x$ dan menuliskan sisa sementara $x^2 + 3x + 4$. Lanjutannya ia peroleh hasil bagi $2x + 1$ dan sisa $5x - 1$. Pernyataan yang benar mengenai pekerjaan Doni adalah ....

- A. Doni salah pada pengurangan suku $x^2$; hasil bagi $2x + 1$ dan sisa $-15x - 1$  
  <sub>Salah: suku $x^2$ sudah benar: $-3x^2-(-4x^2)=x^2$</sub>
- B. Pekerjaan Doni benar seluruhnya; hasil bagi $2x + 1$ dan sisa $5x - 1$  
  <sub>Salah: tidak memeriksa tanda pada pengurangan suku $x$</sub>
- C. Doni salah pada pengurangan suku $x$; hasil bagi $2x + 1$ dan sisa $-15x + 4$  
  <sub>Salah: mengoreksi suku $x$ tetapi lupa mengurangkan suku konstan $5$</sub>
- **D. Doni salah pada pengurangan suku $x$ (seharusnya $-7x - 10x = -17x$); hasil bagi $2x + 1$ benar dan sisa yang benar $-15x - 1$** ✅  
  <sub>Benar: sisa sementara yang benar $x^2-17x+4$; dikurangi $Q$ memberi $-15x-1$</sub>

**Pembahasan:** $P-2xQ=x^2-17x+4$; lalu $-1\cdot Q$ menghasilkan sisa $-15x-1$ dengan hasil bagi $2x+1$. Doni menulis $-7x+10x=3x$, kesalahan tanda.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b02-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: parameter agar dua sisa sama*

Polinomial $P(x) = 2x^3 + kx^2 - 6x + 5$ dirancang agar sisa pembagian oleh $x - 3$ sama dengan sisa pembagian oleh $x + 2$. Sisa yang sama tersebut adalah ....

- A. $155/13$  
  <sub>Salah: menyamakan $P(3)$ dengan $-P(-2)$ sehingga $k=-\frac{42}{13}$</sub>
- B. $-83/5$  
  <sub>Salah: memakai $P(2)$ untuk pembagi $x+2$ sehingga $k=-\frac{32}{5}$</sub>
- **C. $-31$** ✅  
  <sub>Benar: $P(3)=9k+41$ dan $P(-2)=4k+1$; sama jika $k=-8$, sisa $-31$</sub>
- D. $133/5$  
  <sub>Salah: memakai $P(-3)$ untuk pembagi $x-3$ sehingga $k=\frac{32}{5}$</sub>

**Pembahasan:** $P(3)=54+9k-18+5=9k+41$, $P(-2)=-16+4k+12+5=4k+1$. $9k+41=4k+1\Rightarrow k=-8$; sisa $=9(-8)+41=-31$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b02-c-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: parameter ganda pada polinomial habis dibagi pembagi kuadrat*

Polinomial $P(x) = x^4 + ax^3 + bx - 12$ habis dibagi $(x - 2)(x + 1)$. Jika hasil bagi pembagian tersebut adalah $H(x)$, nilai $H(3)$ adalah ....

- A. $11$  
  <sub>Salah: menganggap pembuat nol $x+1$ adalah $1$ sehingga $a,b$ salah</sub>
- **B. $27$** ✅  
  <sub>Benar: habis dibagi berarti $P(2)=0$ dan $P(-1)=0$; diperoleh $a=3$, $b=-14$</sub>
- C. $-21$  
  <sub>Salah: membaca suku konstan sebagai $+12$ ketika menyusun $P(2)$ dan $P(-1)$</sub>
- D. $3$  
  <sub>Salah: membalik tanda kedua pembuat nol ($x-2$ dan $x+1$)</sub>

**Pembahasan:** $P(2)=8a+2b+4=0$ dan $P(-1)=-a-b-11=0$ sehingga $a=3$, $b=-14$. Pembagian oleh $x^2-x-2$ memberi hasil bagi $x^2 + 4x + 6$.
**Acuan:** siswa — siswa hal.88

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b02-c-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: kesesuaian dua sisa pembagi kuadrat*

Polinomial $P(x)$ jika dibagi $x^2 + x - 2$ bersisa $2x + 5$, dan jika dibagi $x^2 - 2x - 8$ bersisa $3x + 7$. Sisa pembagian $P(x)$ oleh $x^2 - 5x + 4$ adalah ....

- A. $-4x + 23$  
  <sub>Salah: menukar nilai $P(1)=19$ dan $P(4)=7$</sub>
- **B. $4x + 3$** ✅  
  <sub>Benar: $P(1)=7$, $P(-2)=1$ (konsisten dari kedua data), $P(4)=19$; sisa oleh $(x-1)(x-4)$ melalui $(1,7)$ dan $(4,19)$ adalah $4x+3$</sub>
- C. $5x + 12$  
  <sub>Salah: menjumlahkan kedua sisa yang diketahui</sub>
- D. $3x + 4$  
  <sub>Salah: menukar koefisien dan konstanta sisa $4x+3$</sub>

**Pembahasan:** Dari $x^2+x-2=(x-1)(x+2)$: $P(1)=7$, $P(-2)=1$. Dari $x^2-2x-8=(x+2)(x-4)$: $P(-2)=1$ (cocok), $P(4)=19$. Sisa oleh $(x-1)(x-4)$ berbentuk $px+q$ dengan $p+q=7$, $4p+q=19$: $4x+3$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b02-c-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: bandingkan dua pembagi yang setara*

Beni membagi $P(x) = 8x^3 - 4x^2 + 10x - 7$ dengan $x - \frac{1}{2}$ dan dengan $2x - 1$. Ia mengklaim bahwa kedua pembagian memberi hasil bagi yang sama dan sisa yang sama karena $2x - 1 = 2\left(x - \frac{1}{2}\right)$. Pernyataan yang benar mengenai klaim Beni adalah ....

- A. Benar: kedua hasil bagi sama $8x^2 + 10$ dan kedua sisa sama $-2$  
  <sub>Salah: tidak memperhitungkan faktor $2$ pada pembagi</sub>
- B. Salah: hasil bagi oleh $2x - 1$ adalah $16x^2 + 20$ dan sisanya $-2$  
  <sub>Salah: mengalikan hasil bagi dengan $2$ padahal seharusnya dibagi $2$</sub>
- **C. Salah: hasil baginya berbeda (hasil bagi oleh $2x - 1$ adalah $4x^2 + 5$), sedangkan sisanya sama, yaitu $-2$** ✅  
  <sub>Benar: $P=(x-\frac12)H_1+s=(2x-1)\cdot\frac{H_1}{2}+s$: hasil bagi dibagi $2$, sisa tetap</sub>
- D. Salah: hasil bagi oleh $2x - 1$ adalah $4x^2 + 5$ dan sisanya $-1$  
  <sub>Salah: ikut membagi sisa dengan $2$</sub>

**Pembahasan:** Horner dengan $c=\frac12$: hasil bagi $8x^2 + 10$, sisa $-2$. Karena $2x-1=2(x-\frac12)$, hasil bagi oleh $2x-1$ adalah $4x^2 + 5$, sisa tetap $-2$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b02-c-hard-bt01-010
*orisinal | C6 | 6 langkah | jenis: rancang polinomial dari tiga sisa*

Sebuah polinomial monik berderajat $3$, $P(x) = x^3 + ax^2 + bx + c$, dirancang agar jika dibagi $x - 1$ bersisa $1$, jika dibagi $x - 2$ bersisa $7$, dan jika dibagi $x + 1$ bersisa $-11$. Nilai $P(3)$ adalah ....

- A. $85/3$  
  <sub>Salah: salah memasukkan sisa $-11$ sebagai $11$ pada syarat $P(-1)$</sub>
- B. $23$  
  <sub>Salah: salah menghitung sisa pada syarat $x+1$ (memakai $-5$)</sub>
- C. $17$  
  <sub>Salah: membalik tanda semua pembuat nol ($x-1\to P(-1)$ dst.)</sub>
- **D. $21$** ✅  
  <sub>Benar: syarat $P(1)=1$, $P(2)=7$, $P(-1)=-11$ memberi $P(x)=x^3-2x^2+5x-3$, sehingga $P(3)=21$</sub>

**Pembahasan:** Tiga syarat menghasilkan tiga persamaan linear untuk $a,b,c$: $a=-2$, $b=5$, $c=-3$; $P(3)=27-18+15-3=21$.
**Acuan:** siswa — siswa hal.92

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b02-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: kecukupan informasi sisa pembagi kuadrat*

Untuk menentukan sisa pembagian $P(x)$ oleh $x^2 - x - 6$ secara tunggal (tanpa mengetahui $P(x)$ sepenuhnya), informasi yang cukup adalah ....

- A. sisa pembagian $P(x)$ oleh $x - 3$ dan nilai $P(3)$  
  <sub>Salah: kedua informasi sama (satu persamaan yang sama)</sub>
- **B. sisa pembagian $P(x)$ oleh $x - 3$ dan sisa pembagian $P(x)$ oleh $x + 2$** ✅  
  <sub>Benar: $x^2-x-6=(x-3)(x+2)$; sisa berbentuk $px+q$ ditentukan oleh $P(3)$ dan $P(-2)$</sub>
- C. sisa pembagian $P(x)$ oleh $x - 3$ dan sisa pembagian $P(x)$ oleh $x - 2$  
  <sub>Salah: $x-2$ bukan faktor $x^2-x-6$ sehingga tidak memberi syarat pada sisanya</sub>
- D. sisa pembagian $P(x)$ oleh $x - 3$ saja  
  <sub>Salah: hanya satu persamaan untuk dua bilangan $p$ dan $q$</sub>

**Pembahasan:** Faktor pembagi $(x-3)(x+2)$; sisa $px+q$ dengan $3p+q=P(3)$ dan $-2p+q=P(-2)$. Hanya pasangan pembuat nol yang tepat yang memberi dua persamaan bebas.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b02-c-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: hasil bagi bersarang (sisa pembagi kuadrat)*

Polinomial $P(x)$ dibagi $x - 2$ bersisa $9$ dengan hasil bagi $H(x)$, dan $H(x)$ dibagi $x + 3$ bersisa $-4$. Rina menyimpulkan bahwa sisa pembagian $P(x)$ oleh $(x - 2)(x + 3)$ adalah $5$ (jumlah kedua sisa). Pernyataan yang benar adalah ....

- **A. Rina keliru; sisa yang benar adalah $-4x + 17$** ✅  
  <sub>Benar: $P=(x-2)H+9$, $H=(x+3)K-4$ sehingga $P=(x-2)(x+3)K-4(x-2)+9$</sub>
- B. Rina keliru; sisa yang benar adalah $9x - 22$  
  <sub>Salah: mengalikan sisa pertama dengan $x-2$ dan menukar peran kedua sisa</sub>
- C. Rina keliru; sisa yang benar adalah $-4x - 3$  
  <sub>Salah: mengalikan sisa kedua dengan $x+3$, bukan $x-2$</sub>
- D. Rina benar; sisanya $5$  
  <sub>Salah: menjumlahkan kedua sisa, padahal sisa pembagi kuadrat berderajat paling tinggi $1$</sub>

**Pembahasan:** $P=(x-2)\big[(x+3)K-4\big]+9=(x-2)(x+3)K-4(x-2)+9$, sisa $-4x+8+9=-4x+17$.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b02-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan yang pasti benar (sisa umum)*

Polinomial $P(x)$ dibagi $x - c$ bersisa $s$. Polinomial berikut yang pasti habis dibagi $x - c$, untuk sembarang $P(x)$, $c$, dan $s$ yang memenuhi, adalah ....

- A. $P(x) - c$  
  <sub>Salah: bernilai $s-c$ di $x=c$; mengira sisa sama dengan $c$</sub>
- B. $P(x) + s$  
  <sub>Salah: bernilai $2s$ di $x=c$, nol hanya bila $s=0$</sub>
- C. $s \cdot P(x) - c \cdot s$  
  <sub>Salah: bernilai $s^2-cs=s(s-c)$ di $x=c$, tidak selalu nol</sub>
- **D. $P(x) - s$** ✅  
  <sub>Benar: $P(c)=s$ sehingga nilai $P(x)-s$ di $x=c$ adalah $0$</sub>

**Pembahasan:** Teorema Sisa: $P(c)=s$. Nilai di $x=c$ untuk $P(x)-s$ adalah $0$ sehingga habis dibagi $x-c$; tiga pilihan lain bernilai $2s$, $s-c$, dan $s(s-c)$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b02-c-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: parameter agar sisa konstan*

Polinomial $P(x) = 2x^3 - 5x^2 + kx + 7$ dibagi $x^2 - 1$. Sisa pembagian berbentuk $px + q$. Jika sisanya berupa konstanta (nilai $p = 0$), maka pernyataan yang benar adalah ....

- **A. $k = -2$ dan sisanya $2$** ✅  
  <sub>Benar: sisa $px+q$ memenuhi $p+q=P(1)=k+4$ dan $-p+q=P(-1)=-k$; $p=0$ jika $P(1)=P(-1)$, yaitu $k=-2$, sisa $2$</sub>
- B. $k = -4$ dan sisanya $4$  
  <sub>Salah: menyamakan $P(1)=0$ saja (salah syarat)</sub>
- C. $k = -2$ dan sisanya $7$  
  <sub>Salah: $k$ benar tetapi sisa diambil dari suku konstan $P(x)$</sub>
- D. $k = 2$ dan sisanya $6$  
  <sub>Salah: salah tanda saat menyamakan $P(1)$ dan $P(-1)$</sub>

**Pembahasan:** $P(1)=k+4$, $P(-1)=-k$. Sisa konstan $\Rightarrow P(1)=P(-1)\Rightarrow k=-2$, sisa $=P(1)=2$.
**Acuan:** siswa — siswa hal.86

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11_tl-b02-c-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: keterjangkauan data sisa (koefisien bulat)*

Polinomial $P(x)$ berkoefisien bilangan bulat. Dari empat pasangan data (sisa jika dibagi $x - 5$, sisa jika dibagi $x + 2$) berikut, pasangan yang TIDAK mungkin terjadi adalah ....

- A. $(17, -4)$  
  <sub>Salah: selisih $21$ kelipatan $7$, mungkin (mis. $P(x)=3x+2$)</sub>
- **B. $(25, 12)$** ✅  
  <sub>Benar: $P(5)-P(-2)$ selalu kelipatan $7$ untuk koefisien bulat; $25-12=13$ bukan kelipatan $7$</sub>
- C. $(-4, 10)$  
  <sub>Salah: selisih $-14$ kelipatan $7$, mungkin (mis. $P(x)=-2x+6$)</sub>
- D. $(30, 9)$  
  <sub>Salah: selisih $21$ kelipatan $7$, mungkin (mis. $P(x)=3x+15$)</sub>

**Pembahasan:** Teorema Sisa: sisa-sisanya $P(5)$ dan $P(-2)$. Untuk setiap $k$, $5^k-(-2)^k$ kelipatan $7$, jadi $P(5)-P(-2)$ kelipatan $7$. Hanya $25-12=13$ yang tidak.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11_tl-b02-c-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: kecukupan informasi polinomial kubik*

Polinomial monik berderajat $3$, $P(x) = x^3 + ax^2 + bx + c$ dengan $a, b, c$ bilangan real, ingin ditentukan secara tunggal. Informasi yang cukup untuk itu adalah ....

- **A. sisa pembagian oleh $x - 1$, oleh $x + 1$, dan oleh $x - 3$** ✅  
  <sub>Benar: tiga pembuat nol berbeda ($1,-1,3$) memberi tiga persamaan bebas untuk $a,b,c$</sub>
- B. sisa pembagian oleh $x - 1$ dan oleh $x + 1$  
  <sub>Salah: hanya dua persamaan untuk tiga bilangan</sub>
- C. sisa pembagian oleh $x - 2$ dan sisa pembagian oleh $x^2 - 4$  
  <sub>Salah: sisa oleh $x^2-4$ memberi $P(2)$ lagi (sama) dan $P(-2)$: hanya dua persamaan bebas</sub>
- D. sisa pembagian oleh $x - 1$ dan sisa pembagian oleh $x^2 - 1$  
  <sub>Salah: sisa oleh $x^2-1$ memberi $P(1)$ lagi (sama) dan $P(-1)$: hanya dua persamaan bebas</sub>

**Pembahasan:** Ada tiga bilangan yang belum diketahui sehingga perlu tiga nilai $P$ di tiga titik berbeda. Pilihan lain hanya memberi dua nilai berbeda.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11_tl-b02-c-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan sisa polinomial berpangkat besar*

Manakah pernyataan yang benar tentang pembagian oleh $x + 1$?

- A. $x^{2024} + 1$ habis dibagi $x + 1$  
  <sub>Salah: $(-1)^{2024}=1$ sehingga sisa $2$, bukan $0$</sub>
- B. $x^{2025} + x^{2024}$ bersisa $2$ jika dibagi $x + 1$  
  <sub>Salah: $(-1)^{2025}+(-1)^{2024}=-1+1=0$, bukan $2$</sub>
- **C. $x^{2025} + 1$ habis dibagi $x + 1$** ✅  
  <sub>Benar: sisa $=P(-1)=(-1)^{2025}+1=0$</sub>
- D. $x^{2025} - 1$ bersisa $0$ jika dibagi $x + 1$  
  <sub>Salah: $(-1)^{2025}=-1$ sehingga sisa $-2$</sub>

**Pembahasan:** Sisa pembagian oleh $x+1$ adalah $P(-1)$. $(-1)^{2025}=-1$, $(-1)^{2024}=1$; hanya $(-1)^{2025}+1=0$.
**Acuan:** siswa — siswa hal.91

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
