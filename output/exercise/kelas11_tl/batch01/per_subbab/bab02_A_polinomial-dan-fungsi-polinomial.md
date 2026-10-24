# Lembar koreksi — kelas11_tl SMA11L-B2 subbab A: Polinomial dan Fungsi Polinomial

49 soal | easy 20, medium 20, hard 9 | variasi 20, orisinal 29
> **Kapasitas kurang (hard): 9 dari kuota 20** — Materi subbab A tipis (definisi, derajat, koefisien utama, nilai fungsi, perilaku ujung, pemodelan). Hanya 9 soal hard yang benar-benar bernalar (evaluasi klaim, temukan kesalahan, penyangkal, rancang); sisanya hanya hitung langsung atau mengulang pola easy/medium sehingga tidak dipaksa.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b02-a-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: perilaku ujung grafik*

Perilaku ujung fungsi polinomial $f(x) = 6x^4 - 9x^3 + 3$ adalah ....

- A. Turun di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira koefisien $-9$ pada suku tengah menentukan tanda ujung</sub>
- B. Naik di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira derajat ganjil (suku $x^3$ dipilih) padahal suku utamanya $6x^4$</sub>
- C. Turun di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengira koefisien utama negatif dan derajat ganjil</sub>
- **D. Naik di ujung kiri dan naik di ujung kanan** ✅  
  <sub>Benar: Suku utama $6x^4$ berderajat genap dengan koefisien positif, sehingga kedua ujung grafik mengarah ke atas.</sub>

**Pembahasan:** Suku utama $6x^4$: derajat 4 (genap), koefisien $6 > 0$. Grafik naik di kiri dan naik di kanan.
**Acuan:** pretest — kelas11_tl-b02-p0074-latihan-a-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b02-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: perilaku ujung grafik*

Perilaku ujung grafik fungsi polinomial $g(x) = 8x^5 - 6x^3 + 9$ adalah ....

- **A. Turun di ujung kiri dan naik di ujung kanan** ✅  
  <sub>Benar: Suku utama $8x^5$ berderajat ganjil dengan koefisien positif: kiri turun, kanan naik.</sub>
- B. Naik di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengira derajat 5 genap sehingga kedua ujung sama arah</sub>
- C. Naik di ujung kiri dan turun di ujung kanan  
  <sub>Salah: tertukar: menganggap koefisien utama negatif</sub>
- D. Turun di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira derajat genap dengan koefisien negatif</sub>

**Pembahasan:** Suku utama $8x^5$: derajat 5 (ganjil), koefisien $8 > 0$, sehingga ujung kiri turun dan ujung kanan naik.
**Acuan:** pretest — kelas11_tl-b02-p0074-latihan-a-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b02-a-easy-bt01-003
*variasi (angka) | C1 | 1 langkah | jenis: derajat polinomial*

$x^8 - 15x^5 + 7x^3 - 9$

Cari derajat polinomial berikut.

- A. $15$  
  <sub>Salah: mengambil koefisien terbesar sebagai derajat</sub>
- **B. $8$** ✅  
  <sub>Benar: Derajat polinomial adalah pangkat tertinggi, yaitu pangkat $x$ pada suku $x^8$.</sub>
- C. $5$  
  <sub>Salah: mengambil pangkat suku kedua, bukan pangkat tertinggi</sub>
- D. $16$  
  <sub>Salah: menjumlahkan pangkat semua suku bervariabel ($8+5+3$)</sub>

**Pembahasan:** Pangkat tertinggi adalah 8, sehingga derajatnya $8$.
**Acuan:** pretest — kelas11_tl-b02-p0074-latihan-a-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b02-a-easy-bt01-004
*variasi (angka) | C1 | 1 langkah | jenis: derajat polinomial*

$9 + 4x^5 - 6x^{11} + 8x^7$

Cari derajat polinomial berikut.

- A. $7$  
  <sub>Salah: mengambil pangkat suku terakhir</sub>
- B. $23$  
  <sub>Salah: menjumlahkan semua pangkat ($5+11+7$)</sub>
- **C. $11$** ✅  
  <sub>Benar: Pangkat tertinggi berada pada suku $-6x^{11}$, jadi derajat polinomial adalah $11$.</sub>
- D. $5$  
  <sub>Salah: mengambil pangkat suku bervariabel pertama yang ditulis</sub>

**Pembahasan:** Pangkat variabel: 5, 11, dan 7. Yang tertinggi adalah 11.
**Acuan:** pretest — kelas11_tl-b02-p0074-latihan-a-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b02-a-easy-bt01-005
*variasi (konteks) | C2 | 1 langkah | jenis: mengidentifikasi polinomial*

Bentuk aljabar yang merupakan polinomial adalah ....

- A. $x + \sqrt{x}$  
  <sub>Salah: tidak menyadari $\sqrt{x} = x^{\frac{1}{2}}$ berpangkat bukan cacah</sub>
- B. $3x^{-2} + 5x$  
  <sub>Salah: mengabaikan pangkat $-2$ yang bukan bilangan cacah</sub>
- **C. $2,5x^2 - 1,8x + 4,6$** ✅  
  <sub>Benar: Semua pangkat variabel adalah bilangan cacah dan koefisien desimal adalah bilangan real, sehingga berupa polinomial.</sub>
- D. $\frac{4}{x} + 2$  
  <sub>Salah: tidak menyadari $\frac{4}{x} = 4x^{-1}$ berpangkat bukan cacah</sub>

**Pembahasan:** Polinomial hanya memuat pangkat variabel bilangan cacah. Hanya $2,5x^2 - 1,8x + 4,6$ yang memenuhi.
**Acuan:** siswa — siswa hal.74 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b02-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi pada grafik*

Grafik $f(x) = 5x^2 - 8x + 9$ melalui titik $(-1, k)$. Nilai $k$ adalah ....

- **A. $22$** ✅  
  <sub>Benar: Titik pada grafik memenuhi $k = f(-1) = 5(1) - 8(-1) + 9 = 22$.</sub>
- B. $4$  
  <sub>Salah: salah tanda pada suku $-8x$ dan konstanta $+9$ dihitung $-9$</sub>
- C. $12$  
  <sub>Salah: salah tanda: $5(-1)^2$ dihitung $-5$</sub>
- D. $6$  
  <sub>Salah: salah tanda: $-8 \cdot (-1)$ dihitung $-8$</sub>

**Pembahasan:** $f(-1) = 5 \cdot 1 + 8 + 9 = 22$.
**Acuan:** siswa — siswa hal.74 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b02-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi pada grafik*

Grafik $h(x) = 6x^3 - 7x + 5$ melalui titik $(2, m)$. Nilai $m$ adalah ....

- A. $27$  
  <sub>Salah: menghitung $6x^3$ sebagai $6 \cdot 6 = 36$ (mengalikan bukan memangkatkan)</sub>
- B. $34$  
  <sub>Salah: lupa menambahkan konstanta $+5$</sub>
- C. $67$  
  <sub>Salah: salah tanda: $-7x$ dihitung $+14$</sub>
- **D. $39$** ✅  
  <sub>Benar: Titik pada grafik memenuhi $m = h(2) = 6(8) - 14 + 5 = 39$.</sub>

**Pembahasan:** $h(2) = 6 \cdot 8 - 7 \cdot 2 + 5 = 48 - 14 + 5 = 39$.
**Acuan:** siswa — siswa hal.74 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b02-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: derajat polinomial*

Cari derajat polinomial $7x^3y^2 - 4xy^5z + 9$.

- A. $6$  
  <sub>Salah: mengabaikan eksponen $z$ yang tidak tertulis (bernilai 1)</sub>
- B. $12$  
  <sub>Salah: menjumlahkan derajat dua suku ($5+7$)</sub>
- C. $5$  
  <sub>Salah: hanya menghitung suku pertama</sub>
- **D. $7$** ✅  
  <sub>Benar: Derajat suku: $7x^3y^2$ adalah $3+2=5$; $-4xy^5z$ adalah $1+5+1=7$; konstanta 0. Tertinggi 7.</sub>

**Pembahasan:** Suku kedua $-4xy^5z$ berderajat $1+5+1 = 7$, lebih tinggi dari suku pertama (5).
**Acuan:** siswa — siswa hal.74 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b02-a-easy-bt01-009
*variasi (angka) | C1 | 1 langkah | jenis: derajat polinomial*

Tentukan derajat polinomial $4x^5 - 20x^3 + 7x - 13$.

- A. $4$  
  <sub>Salah: mengambil koefisien suku utama</sub>
- **B. $5$** ✅  
  <sub>Benar: Derajat polinomial sama dengan derajat suku tertingginya, yaitu $4x^5$ berderajat 5.</sub>
- C. $20$  
  <sub>Salah: mengambil koefisien terbesar</sub>
- D. $3$  
  <sub>Salah: mengambil pangkat suku kedua</sub>

**Pembahasan:** Derajat tertinggi suku-sukunya adalah 5.
**Acuan:** siswa — siswa hal.67 Contoh 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b02-a-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: derajat polinomial*

Tentukan derajat $6,5x^4y^3z^2 - 2,4xy^3z^2 + 8,1$.

- A. $6$  
  <sub>Salah: hanya menghitung suku kedua</sub>
- B. $4$  
  <sub>Salah: mengambil pangkat variabel tunggal tertinggi saja</sub>
- C. $15$  
  <sub>Salah: menjumlahkan derajat dua suku ($9+6$)</sub>
- **D. $9$** ✅  
  <sub>Benar: Suku pertama berderajat $4+3+2=9$, suku kedua $1+3+2=6$; tertinggi 9.</sub>

**Pembahasan:** Derajat suku pertama 9, suku kedua 6, konstanta 0. Derajat polinomial 9.
**Acuan:** siswa — siswa hal.67 Mari Mencoba 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b02-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: perilaku ujung grafik*

Perilaku ujung grafik $f(x) = -4x^6 + 5x^2 - 9$ adalah ....

- **A. Turun di ujung kiri dan turun di ujung kanan** ✅  
  <sub>Benar: Suku utama $-4x^6$ berderajat genap dengan koefisien negatif, sehingga kedua ujung mengarah ke bawah.</sub>
- B. Turun di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengira derajat ganjil dengan koefisien positif</sub>
- C. Naik di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira derajat ganjil sehingga arah kedua ujung berlawanan</sub>
- D. Naik di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengabaikan tanda negatif koefisien utama</sub>

**Pembahasan:** Suku utama $-4x^6$: derajat 6 (genap), koefisien negatif, sehingga turun di kiri dan turun di kanan.
**Acuan:** siswa — siswa hal.72 Mari Mencoba 2.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b02-a-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: pemodelan banyak pertandingan*

Sebuah liga terdiri atas 7 tim. Setiap dua tim bertanding dua kali (kandang dan tandang). Jumlah seluruh pertandingan dalam liga tersebut adalah ....

- **A. $42$** ✅  
  <sub>Benar: Tiap tim melawan 6 tim lain sebagai tuan rumah, sehingga $7 \times 6 = 42$.</sub>
- B. $49$  
  <sub>Salah: mengira tim juga melawan dirinya sendiri ($7 \times 7$)</sub>
- C. $14$  
  <sub>Salah: mengalikan banyak tim dengan 2</sub>
- D. $21$  
  <sub>Salah: menghitung tiap pasangan hanya sekali ($\frac{7 \times 6}{2}$)</sub>

**Pembahasan:** Setiap tim menjadi tuan rumah melawan 6 tim lain: $7 \times 6 = 42$ pertandingan.
**Acuan:** siswa — siswa hal.68 Eksplorasi Pertandingan dalam Liga

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b02-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: mengidentifikasi monomial*

Bentuk aljabar berikut yang merupakan monomial adalah ....

- A. $\frac{5}{x}$  
  <sub>Salah: tidak menyadari $\frac{5}{x} = 5x^{-1}$ berpangkat bukan cacah</sub>
- B. $2x + 5y$  
  <sub>Salah: mengira penjumlahan dua suku masih berupa monomial</sub>
- **C. $-7x^3y$** ✅  
  <sub>Benar: Monomial berupa satu suku dengan variabel berpangkat bilangan cacah; $-7x^3y$ memenuhi.</sub>
- D. $4x^{-2}$  
  <sub>Salah: mengabaikan bahwa pangkat $-2$ bukan bilangan cacah</sub>

**Pembahasan:** Hanya $-7x^3y$ yang satu suku dan variabelnya berpangkat bilangan cacah.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b02-a-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: istilah suku polinomial*

Koefisien dari monomial $-9x^2y^3$ adalah ....

- A. $3$  
  <sub>Salah: mengambil pangkat variabel $y$</sub>
- **B. $-9$** ✅  
  <sub>Benar: Koefisien adalah faktor numerik monomial, yaitu $-9$ lengkap dengan tandanya.</sub>
- C. $5$  
  <sub>Salah: mengambil derajat monomial ($2+3$)</sub>
- D. $9$  
  <sub>Salah: mengabaikan tanda negatif</sub>

**Pembahasan:** Faktor numerik dari $-9x^2y^3$ adalah $-9$.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b02-a-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: istilah suku polinomial*

Suku konstanta dari polinomial $4x^3 - 7x^2 + 3x - 12$ adalah ....

- A. $4$  
  <sub>Salah: mengambil koefisien suku pertama</sub>
- **B. $-12$** ✅  
  <sub>Benar: Konstanta adalah suku yang tidak memuat variabel, yaitu $-12$.</sub>
- C. $3$  
  <sub>Salah: mengambil koefisien suku $x$</sub>
- D. $12$  
  <sub>Salah: mengabaikan tanda negatif</sub>

**Pembahasan:** Satu-satunya suku tanpa variabel adalah $-12$.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b02-a-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: derajat monomial*

Derajat monomial $-4m^3n^5r^2$ adalah ....

- **A. $10$** ✅  
  <sub>Benar: Derajat monomial adalah jumlah eksponen semua variabel: $3+5+2=10$.</sub>
- B. $30$  
  <sub>Salah: mengalikan eksponen, bukan menjumlahkan</sub>
- C. $-4$  
  <sub>Salah: mengambil koefisien sebagai derajat</sub>
- D. $8$  
  <sub>Salah: menjumlahkan eksponen hanya dua variabel pertama</sub>

**Pembahasan:** $3+5+2 = 10$.
**Acuan:** siswa — siswa hal.66

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b02-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: derajat polinomial*

Derajat polinomial $3x^2y^4 + x^3y - 5xy^2$ adalah ....

- A. $3$  
  <sub>Salah: mengambil pangkat tertinggi $x$ saja</sub>
- B. $13$  
  <sub>Salah: menjumlahkan derajat semua suku ($6+4+3$)</sub>
- **C. $6$** ✅  
  <sub>Benar: Derajat suku: $2+4=6$, $3+1=4$, $1+2=3$. Derajat tertinggi adalah 6.</sub>
- D. $4$  
  <sub>Salah: mengambil derajat suku tengah</sub>

**Pembahasan:** Derajat tiap suku 6, 4, dan 3, sehingga derajat polinomial 6.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b02-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: istilah suku polinomial*

Koefisien utama dari polinomial $P(x) = 3x - 8x^4 + 5x^2 + 1$ adalah ....

- A. $4$  
  <sub>Salah: mengambil derajat polinomial, bukan koefisiennya</sub>
- **B. $-8$** ✅  
  <sub>Benar: Suku utama adalah suku berderajat tertinggi, yaitu $-8x^4$, sehingga koefisien utamanya $-8$.</sub>
- C. $8$  
  <sub>Salah: mengabaikan tanda negatif</sub>
- D. $3$  
  <sub>Salah: mengambil koefisien suku yang ditulis pertama</sub>

**Pembahasan:** Derajat tertinggi 4 pada suku $-8x^4$, koefisien utamanya $-8$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b02-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: nilai fungsi pada grafik*

Jika $g(x) = x^3 - 4x^2 + 6$, nilai $g(3)$ adalah ....

- A. $21$  
  <sub>Salah: menghitung $4x^2$ sebagai $4 \cdot 3 = 12$</sub>
- B. $69$  
  <sub>Salah: salah tanda pada suku $-4x^2$ (dihitung $+36$)</sub>
- C. $-9$  
  <sub>Salah: lupa menambahkan konstanta $+6$</sub>
- **D. $-3$** ✅  
  <sub>Benar: $g(3) = 27 - 36 + 6 = -3$.</sub>

**Pembahasan:** $g(3) = 3^3 - 4 \cdot 3^2 + 6 = 27 - 36 + 6 = -3$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b02-a-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: perilaku ujung grafik*

Fungsi polinomial yang grafiknya mengarah ke kiri bawah dan ke kanan bawah adalah ....

- A. $h(x) = -3x^3 + x$  
  <sub>Salah: mengira koefisien negatif cukup, padahal derajat ganjil (kiri atas, kanan bawah)</sub>
- B. $k(x) = x^5 - 4x$  
  <sub>Salah: mengira derajat ganjil menghasilkan ujung sama arah (sebenarnya kiri bawah, kanan atas)</sub>
- **C. $f(x) = -2x^4 + 9x^3 + 1$** ✅  
  <sub>Benar: Suku utama $-2x^4$ berderajat genap dan koefisien negatif, sehingga kedua ujung ke bawah.</sub>
- D. $g(x) = 2x^4 - 9x^3 + 1$  
  <sub>Salah: memilih berdasarkan tanda suku kedua, padahal suku utama $2x^4$ bernilai positif (kedua ujung ke atas)</sub>

**Pembahasan:** Dibutuhkan derajat genap dan koefisien utama negatif; hanya $f$ yang memenuhi.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b02-a-medium-bt01-001
*variasi (angka) | C4 | 3 langkah | jenis: derajat hasil kali tanpa penjabaran*

Tanpa menjabarkan, derajat polinomial $(8x^9 - 3)^4 (9x^4 + 4)^7$ adalah ....

- A. $1.008$  
  <sub>Salah: mengalikan derajat kedua faktor ($36 \times 28$) padahal derajat hasil kali dijumlahkan</sub>
- **B. $64$** ✅  
  <sub>Benar: Derajat $(8x^9-3)^4$ adalah $9 \cdot 4 = 36$ dan derajat $(9x^4+4)^7$ adalah $4 \cdot 7 = 28$. Derajat hasil kali adalah jumlahnya, $36 + 28 = 64$.</sub>
- C. $13$  
  <sub>Salah: menjumlahkan derajat kedua faktor dalam kurung ($9+4$) tanpa memperhitungkan pangkat luar</sub>
- D. $24$  
  <sub>Salah: menjumlahkan semua bilangan pangkat ($9+4+4+7$)</sub>

**Pembahasan:** Derajat faktor pertama $9 \cdot 4 = 36$, faktor kedua $4 \cdot 7 = 28$. Derajat hasil kali $36 + 28 = 64$.
**Acuan:** siswa — siswa hal.68 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b02-a-medium-bt01-002
*variasi (angka) | C4 | 3 langkah | jenis: derajat hasil kali tanpa penjabaran*

Tanpa menjabarkan, derajat polinomial $(x^3 - 4)^8 (x^6 + 7)^5$ adalah ....

- A. $720$  
  <sub>Salah: mengalikan derajat kedua faktor ($24 \times 30$)</sub>
- B. $22$  
  <sub>Salah: menjumlahkan semua bilangan pangkat ($3+8+6+5$)</sub>
- **C. $54$** ✅  
  <sub>Benar: Derajat $(x^3-4)^8$ adalah $3 \cdot 8 = 24$ dan derajat $(x^6+7)^5$ adalah $6 \cdot 5 = 30$. Jumlahnya $54$.</sub>
- D. $13$  
  <sub>Salah: menjumlahkan pangkat luar saja ($8+5$)</sub>

**Pembahasan:** Derajat faktor pertama $24$, faktor kedua $30$, hasil kali berderajat $24 + 30 = 54$.
**Acuan:** siswa — siswa hal.68 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b02-a-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: derajat hasil kali tanpa penjabaran*

Tanpa menjabarkan, derajat polinomial $(7 - 9x^3)^4 (2 - x^5)^3 (8 + x^2)^5$ adalah ....

- **A. $37$** ✅  
  <sub>Benar: Derajat tiap faktor: $3 \cdot 4 = 12$, $5 \cdot 3 = 15$, $2 \cdot 5 = 10$. Jumlahnya $12 + 15 + 10 = 37$.</sub>
- B. $27$  
  <sub>Salah: melewatkan faktor ketiga ($12+15$)</sub>
- C. $12$  
  <sub>Salah: menjumlahkan pangkat luar saja ($4+3+5$)</sub>
- D. $10$  
  <sub>Salah: menjumlahkan pangkat variabel di dalam kurung ($3+5+2$)</sub>

**Pembahasan:** Derajat: $12$, $15$, dan $10$; jumlahnya $37$.
**Acuan:** siswa — siswa hal.68 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b02-a-medium-bt01-004
*variasi (angka) | C3 | 2 langkah | jenis: perilaku ujung dengan suku tak berurutan*

Perilaku ujung fungsi polinomial $f(x) = 6x^3 - x^{10} + 9x^5 - 12$ adalah ....

- A. Naik di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengabaikan tanda negatif pada $-x^{10}$</sub>
- B. Turun di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengambil suku pertama $6x^3$ (derajat ganjil, koefisien positif) sebagai suku utama</sub>
- C. Naik di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira derajat ganjil dengan koefisien utama negatif</sub>
- **D. Turun di ujung kiri dan turun di ujung kanan** ✅  
  <sub>Benar: Suku utama adalah $-x^{10}$ (derajat 10 genap, koefisien $-1$ negatif), sehingga kedua ujung mengarah ke bawah.</sub>

**Pembahasan:** Derajat tertinggi 10 pada suku $-x^{10}$. Derajat genap dengan koefisien negatif: kiri turun, kanan turun.
**Acuan:** pretest — kelas11_tl-b02-p0074-latihan-a-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b02-a-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: pemodelan fungsi kuadrat dari cerita*

Dalam sebuah pertemuan hadir $x$ orang. Setiap dua orang berjabat tangan tepat satu kali. Fungsi yang menyatakan banyak jabat tangan seluruhnya adalah ....

- A. $f(x) = x^2 - x$  
  <sub>Salah: tidak membagi dua sehingga setiap pasangan dihitung dua kali</sub>
- B. $f(x) = \frac{1}{2}x^2 + \frac{1}{2}x$  
  <sub>Salah: mengira tiap orang juga berjabat tangan dengan dirinya sendiri ($\frac{x(x+1)}{2}$)</sub>
- C. $f(x) = \frac{1}{2}x^2$  
  <sub>Salah: melupakan pengurangan $x$ (orang tidak berjabat dengan dirinya sendiri)</sub>
- **D. $f(x) = \frac{1}{2}x^2 - \frac{1}{2}x$** ✅  
  <sub>Benar: Tiap orang berjabat dengan $x-1$ orang lain, total $x(x-1)$ dihitung dua kali per pasangan, sehingga $\frac{x(x-1)}{2} = \frac{1}{2}x^2 - \frac{1}{2}x$.</sub>

**Pembahasan:** $\frac{x(x-1)}{2} = \frac{1}{2}x^2 - \frac{1}{2}x$.
**Acuan:** siswa — siswa hal.68 Eksplorasi Pertandingan dalam Liga

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b02-a-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: pemodelan koefisien fungsi kuadrat*

Dalam sebuah turnamen voli yang diikuti $x$ tim, setiap dua tim bertemu enam kali, dan ditambah 9 pertandingan eksibisi. Banyak seluruh pertandingan dinyatakan sebagai $f(x) = ax^2 + bx + c$. Nilai $a$, $b$, dan $c$ berturut-turut adalah ....

- **A. $3$, $-3$, dan $9$** ✅  
  <sub>Benar: Banyak pasangan tim $\frac{x(x-1)}{2}$, tiap pasangan 6 kali: $3x(x-1) = 3x^2 - 3x$, ditambah 9 sehingga $f(x) = 3x^2 - 3x + 9$.</sub>
- B. $3$, $3$, dan $9$  
  <sub>Salah: salah tanda pada suku $x$ karena mengira $x(x+1)$</sub>
- C. $6$, $-6$, dan $9$  
  <sub>Salah: setiap pasangan dihitung dua kali (tidak dibagi dua)</sub>
- D. $3$, $-3$, dan $0$  
  <sub>Salah: melupakan 9 pertandingan eksibisi</sub>

**Pembahasan:** $6 \cdot \frac{x(x-1)}{2} + 9 = 3x^2 - 3x + 9$, sehingga $a=3$, $b=-3$, $c=9$.
**Acuan:** siswa — siswa hal.68 Eksplorasi Pertandingan dalam Liga

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b02-a-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: koefisien utama hasil kali*

Koefisien utama polinomial $P(x) = (2x^3 - 1)^2 (3x^2 + 4)^3$ adalah ....

- A. $12$  
  <sub>Salah: mengambil derajat polinomial sebagai koefisien utama</sub>
- **B. $108$** ✅  
  <sub>Benar: Suku utama $(2x^3-1)^2$ adalah $4x^6$ dan suku utama $(3x^2+4)^3$ adalah $27x^6$. Suku utama $P(x)$ adalah $4 \cdot 27 x^{12} = 108x^{12}$.</sub>
- C. $31$  
  <sub>Salah: menjumlahkan koefisien utama kedua faktor ($4 + 27$)</sub>
- D. $36$  
  <sub>Salah: menghitung $(2 \cdot 3)^2$, memangkatkan koefisien dengan pangkat yang sama untuk kedua faktor</sub>

**Pembahasan:** $(2x^3)^2 = 4x^6$, $(3x^2)^3 = 27x^6$, hasil kali $108x^{12}$, koefisien utama $108$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b02-a-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: nilai fungsi dalam cerita biaya*

Biaya produksi $x$ unit barang (dalam ribu rupiah) dinyatakan dengan fungsi polinomial $C(x) = 2x^3 - 30x^2 + 150x + 400$. Biaya untuk memproduksi 6 unit barang adalah ....

- **A. Rp652.000** ✅  
  <sub>Benar: $C(6) = 2(216) - 30(36) + 150(6) + 400 = 432 - 1.080 + 900 + 400 = 652$ ribu rupiah.</sub>
- B. Rp2.812.000  
  <sub>Salah: salah tanda pada suku $-30x^2$ (dihitung $+1.080$)</sub>
- C. Rp252.000  
  <sub>Salah: lupa menambahkan konstanta 400</sub>
- D. Rp1.948.000  
  <sub>Salah: menghitung $2x^3$ sebagai $(2x)^3 = 1.728$</sub>

**Pembahasan:** $C(6) = 432 - 1.080 + 900 + 400 = 652$, yaitu Rp652.000.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b02-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: parameter dari titik pada grafik*

Grafik fungsi $f(x) = 2x^3 + kx^2 - 5x + 1$ melalui titik $(-2, 15)$. Nilai $k$ adalah ....

- A. $-3$  
  <sub>Salah: menghitung $2(-2)^3$ sebagai $+16$</sub>
- **B. $5$** ✅  
  <sub>Benar: $f(-2) = -16 + 4k + 10 + 1 = 4k - 5 = 15$, sehingga $k = 5$.</sub>
- C. $-5$  
  <sub>Salah: menghitung $(-2)^2$ sebagai $-4$</sub>
- D. $10$  
  <sub>Salah: salah tanda pada suku $-5x$ (dihitung $-10$)</sub>

**Pembahasan:** $-16 + 4k + 10 + 1 = 15 \Rightarrow 4k = 20 \Rightarrow k = 5$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b02-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: syarat bentuk polinomial dengan parameter*

Bentuk aljabar $6x^{2m-9} + 4x^2 - 1$ merupakan polinomial jika pangkat $2m - 9$ adalah bilangan cacah. Nilai bilangan bulat $m$ terkecil yang memenuhi adalah ....

- A. $4$  
  <sub>Salah: membulatkan $4,5$ ke bawah; padahal untuk $m=4$ pangkatnya $-1$, bukan bilangan cacah</sub>
- B. $9$  
  <sub>Salah: mengambil konstanta $9$ sebagai nilai $m$</sub>
- **C. $5$** ✅  
  <sub>Benar: Pangkat harus cacah: $2m - 9 \geq 0$, sehingga $m \geq 4,5$. Bilangan bulat terkecil adalah $5$.</sub>
- D. $3$  
  <sub>Salah: tidak memeriksa bahwa pangkat $-3$ bukan bilangan cacah</sub>

**Pembahasan:** $2m - 9 \geq 0 \Rightarrow m \geq 4,5$. Untuk $m = 5$ pangkatnya $1$ (cacah).
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b02-a-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: parameter derajat hasil kali*

Derajat polinomial $(x^a - 2)^4 (x^3 + 5)^6$ adalah 38. Nilai $a$ adalah ....

- **A. $5$** ✅  
  <sub>Benar: Derajat faktor pertama $4a$, faktor kedua $3 \cdot 6 = 18$. Jadi $4a + 18 = 38$, sehingga $a = 5$.</sub>
- B. $8$  
  <sub>Salah: menganggap derajat faktor kedua hanya $6$ sehingga $4a + 6 = 38$</sub>
- C. $16$  
  <sub>Salah: menjumlahkan $a + 4 + 18 = 38$ tanpa mengalikan $a$ dengan 4</sub>
- D. $20$  
  <sub>Salah: lupa membagi $4a = 20$ dengan 4</sub>

**Pembahasan:** $4a + 18 = 38 \Rightarrow a = 5$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b02-a-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: perilaku ujung bentuk faktor*

Perilaku ujung grafik fungsi $f(x) = (4 - 3x)(x^2 + 2)(x^2 - 7)$ adalah ....

- A. Turun di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira derajat genap dengan koefisien negatif</sub>
- B. Naik di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengira derajat genap (menghitung dari $x^2 \cdot x^2$ saja)</sub>
- **C. Naik di ujung kiri dan turun di ujung kanan** ✅  
  <sub>Benar: Suku utama adalah hasil kali suku berderajat tertinggi tiap faktor: $(-3x)(x^2)(x^2) = -3x^5$. Derajat 5 (ganjil), koefisien negatif: kiri naik, kanan turun.</sub>
- D. Turun di ujung kiri dan naik di ujung kanan  
  <sub>Salah: mengambil suku konstanta $4$ sebagai bagian suku utama sehingga koefisien dianggap positif</sub>

**Pembahasan:** Suku utama $-3x \cdot x^2 \cdot x^2 = -3x^5$ sehingga kiri naik dan kanan turun.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b02-a-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: perilaku ujung dengan parameter*

Grafik fungsi $f(x) = (3 - m)x^4 + 2x^3 - 5$ mengarah ke bawah di kedua ujung. Nilai bilangan bulat $m$ terkecil yang memenuhi adalah ....

- A. $-4$  
  <sub>Salah: salah membalik tanda pertidaksamaan menjadi $m < -3$</sub>
- B. $3$  
  <sub>Salah: memasukkan batas $m=3$; koefisien menjadi $0$ sehingga suku $x^4$ hilang dan derajatnya 3</sub>
- **C. $4$** ✅  
  <sub>Benar: Derajat 4 genap, sehingga kedua ujung ke bawah jika koefisien utama negatif: $3 - m < 0$, yaitu $m > 3$. Bilangan bulat terkecil adalah $4$.</sub>
- D. $2$  
  <sub>Salah: menganggap koefisien utama harus positif ($3 - m > 0$)</sub>

**Pembahasan:** $3 - m < 0 \Rightarrow m > 3$, sehingga $m$ bulat terkecil adalah $4$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b02-a-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: perilaku ujung setelah penyederhanaan*

Perilaku ujung grafik fungsi $f(x) = (x^2 + 1)^2 - x^4 + 3x - 2$ adalah ....

- **A. Naik di ujung kiri dan naik di ujung kanan** ✅  
  <sub>Benar: $(x^2+1)^2 = x^4 + 2x^2 + 1$, sehingga $f(x) = 2x^2 + 3x - 1$. Suku utama $2x^2$ (genap, positif): kedua ujung naik.</sub>
- B. Turun di ujung kiri dan turun di ujung kanan  
  <sub>Salah: memakai $-x^4$ sebagai suku utama tanpa menyederhanakan</sub>
- C. Naik di ujung kiri dan turun di ujung kanan  
  <sub>Salah: mengira suku konstanta $-2$ menentukan arah dengan derajat ganjil</sub>
- D. Turun di ujung kiri dan naik di ujung kanan  
  <sub>Salah: memakai suku $3x$ (derajat ganjil, positif) sebagai suku utama</sub>

**Pembahasan:** $f(x) = x^4 + 2x^2 + 1 - x^4 + 3x - 2 = 2x^2 + 3x - 1$; derajat 2, koefisien utama positif.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b02-a-medium-bt01-015
*orisinal | C3 | 4 langkah | jenis: pemodelan volume sebagai fungsi*

Kawat sepanjang 168 cm dipakai sebagai kerangka sebuah kotak berbentuk balok. Alas dan tutup kotak berbentuk persegi dengan sisi $x$ cm, dan tinggi kotak $y$ cm (kerangka memuat 8 rusuk sepanjang $x$ dan 4 rusuk sepanjang $y$). Volume kotak sebagai fungsi $x$ adalah ....

- A. $V(x) = 168x^2 - 8x^3$  
  <sub>Salah: menganggap $8x + y = 168$ sehingga $y = 168 - 8x$</sub>
- B. $V(x) = 42x^2 - x^3$  
  <sub>Salah: menganggap kerangka $4x + 4y = 168$ sehingga $y = 42 - x$</sub>
- C. $V(x) = 84x^2 - 2x^3$  
  <sub>Salah: menganggap kerangka $4x + 2y = 168$ sehingga $y = 84 - 2x$</sub>
- **D. $V(x) = 42x^2 - 2x^3$** ✅  
  <sub>Benar: Panjang kerangka $8x + 4y = 168$, sehingga $y = 42 - 2x$. Volume $V = x^2 y = 42x^2 - 2x^3$.</sub>

**Pembahasan:** $y = 42 - 2x$, jadi $V(x) = x^2(42 - 2x) = 42x^2 - 2x^3$.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b02-a-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: daerah asal sesuai konteks*

Kawat sepanjang 120 cm dipakai sebagai kerangka kotak berbentuk balok dengan alas dan tutup persegi bersisi $x$ cm dan tinggi $y$ cm (8 rusuk sepanjang $x$ dan 4 rusuk sepanjang $y$). Volume kotak $V(x) = x^2(30 - 2x)$. Daerah asal $V$ yang sesuai dengan keadaan kotak tersebut adalah ....

- A. semua bilangan real $x$  
  <sub>Salah: memakai daerah asal polinomial umum tanpa memperhatikan konteks ukuran</sub>
- **B. $0 < x < 15$** ✅  
  <sub>Benar: Panjang sisi dan tinggi harus positif: $x > 0$ dan $y = 30 - 2x > 0$, sehingga $x < 15$.</sub>
- C. $0 \leq x \leq 15$  
  <sub>Salah: menyertakan ujung sehingga sisi bernilai $0$ atau tinggi $0$ (bukan balok)</sub>
- D. $0 < x < 30$  
  <sub>Salah: menganggap $30 - x > 0$ (lupa koefisien 2 pada $2x$)</sub>

**Pembahasan:** $x > 0$ dan $30 - 2x > 0$ memberikan $0 < x < 15$.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b02-a-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: menghitung bentuk yang berupa polinomial*

(1) $\sqrt{3}x^2 - 4$; (2) $\frac{x^3 + 2x}{5}$; (3) $x^{-1} + 3$; (4) $2^x + 1$; (5) $\sqrt{x} + x$

Banyak bentuk aljabar yang merupakan polinomial dari kelima bentuk pada stimulus adalah ....

- A. $3$  
  <sub>Salah: menganggap $\sqrt{x} + x$ polinomial karena memuat suku $x$</sub>
- B. $1$  
  <sub>Salah: mengira koefisien $\sqrt{3}$ atau $\frac{1}{5}$ bukan bilangan real yang sah</sub>
- C. $4$  
  <sub>Salah: menganggap $x^{-1} + 3$ atau $2^x + 1$ sebagai polinomial</sub>
- **D. $2$** ✅  
  <sub>Benar: Hanya (1) dan (2) yang polinomial; (3) berpangkat $-1$, (4) variabel sebagai pangkat, (5) $\sqrt{x} = x^{\frac{1}{2}}$ berpangkat bukan cacah.</sub>

**Pembahasan:** (1) $\sqrt{3}x^2 - 4$ ya; (2) $\frac{x^3 + 2x}{5}$ ya; (3) tidak; (4) tidak; (5) tidak. Jadi 2.
**Acuan:** siswa — siswa hal.65

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b02-a-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: evaluasi pernyataan tentang polinomial*

Diketahui $P(x) = 7 - 3x^2 + 5x^6 - x$. Pernyataan yang benar tentang $P(x)$ adalah ....

- A. Derajatnya $6$ dan koefisien utamanya $7$  
  <sub>Salah: mengambil suku yang ditulis pertama (konstanta) sebagai suku utama</sub>
- B. Derajatnya $9$ dan koefisien utamanya $5$  
  <sub>Salah: menjumlahkan semua pangkat ($6+2+1$) sebagai derajat</sub>
- **C. Derajatnya $6$ dan kedua ujung grafiknya naik** ✅  
  <sub>Benar: Suku utama $5x^6$ berderajat genap dengan koefisien positif sehingga kedua ujung naik.</sub>
- D. Derajatnya $6$ dan grafiknya melalui titik $(1, 6)$  
  <sub>Salah: salah menghitung: $P(1) = 7 - 3 + 5 - 1 = 8$, bukan $6$</sub>

**Pembahasan:** Derajat 6, suku utama $5x^6$, koefisien utama 5, dan $P(1)=8$. Hanya pernyataan tentang suku utama dan ujung grafik yang benar.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b02-a-medium-bt01-019
*variasi (angka) | C4 | 3 langkah | jenis: derajat hasil kali tanpa penjabaran*

Tanpa menjabarkan, derajat polinomial $(x^8 - 5)^3 (x^2 + 6)^9$ adalah ....

- A. $22$  
  <sub>Salah: menjumlahkan semua bilangan pangkat ($8+3+2+9$)</sub>
- B. $432$  
  <sub>Salah: mengalikan derajat kedua faktor ($24 \times 18$)</sub>
- C. $12$  
  <sub>Salah: menjumlahkan pangkat luar saja ($3+9$)</sub>
- **D. $42$** ✅  
  <sub>Benar: Derajat $(x^8-5)^3$ adalah $8 \cdot 3 = 24$ dan derajat $(x^2+6)^9$ adalah $2 \cdot 9 = 18$. Jumlahnya $42$.</sub>

**Pembahasan:** Derajat faktor pertama $24$, faktor kedua $18$, jadi derajat hasil kali $42$.
**Acuan:** siswa — siswa hal.68 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b02-a-medium-bt01-020
*variasi (angka) | C4 | 4 langkah | jenis: derajat hasil kali tanpa penjabaran*

Tanpa menjabarkan, derajat polinomial $(6 + 5x^2)^7 (3x^4 - 2)^2 (9 - x)^6$ adalah ....

- A. $15$  
  <sub>Salah: menjumlahkan pangkat luar saja ($7+2+6$)</sub>
- **B. $28$** ✅  
  <sub>Benar: Derajat tiap faktor: $2 \cdot 7 = 14$, $4 \cdot 2 = 8$, dan $1 \cdot 6 = 6$. Jumlahnya $14 + 8 + 6 = 28$.</sub>
- C. $22$  
  <sub>Salah: menghitung $(9-x)^6$ berderajat $0$ sehingga hanya $14 + 8$</sub>
- D. $7$  
  <sub>Salah: menjumlahkan derajat faktor dalam kurung tanpa pangkat luar ($2+4+1$)</sub>

**Pembahasan:** Derajat: $14$, $8$, dan $6$; jumlahnya $28$.
**Acuan:** siswa — siswa hal.68 Mari Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b02-a-hard-bt01-001
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim derajat jumlah*

Seorang siswa menyatakan: "Jika $P(x)$ dan $Q(x)$ sama-sama berderajat 4, maka $P(x) + Q(x)$ pasti berderajat 4." Pasangan $P(x)$ dan $Q(x)$ berikut, yang keduanya berderajat 4, yang merupakan contoh penyangkal pernyataan tersebut adalah ....

- A. $P(x) = 7x^4 - 2x + 1$ dan $Q(x) = 7x^4 + 3x^2 - 5$  
  <sub>Salah: mengira koefisien utama yang sama membuat suku $x^4$ hilang; padahal jumlahnya $14x^4 + \dots$</sub>
- B. $P(x) = 7x^4 - 2x + 1$ dan $Q(x) = 5x^4 - x^3 + 2$  
  <sub>Salah: menganggap suku berderajat 3 ikut menurunkan derajat jumlah; jumlahnya $12x^4 + \dots$</sub>
- **C. $P(x) = 7x^4 - 2x + 1$ dan $Q(x) = -7x^4 + 3x^2 - 5$** ✅  
  <sub>Benar: Jumlahnya $3x^2 - 2x - 4$ berderajat 2, bukan 4, sehingga klaim tidak selalu berlaku.</sub>
- D. $P(x) = 7x^4 - 2x + 1$ dan $Q(x) = -4x^4 + x^2 - 5$  
  <sub>Salah: koefisien utama berlawanan tanda dianggap cukup; jumlahnya $3x^4 + \dots$ tetap berderajat 4</sub>

**Pembahasan:** Contoh penyangkal harus menghilangkan suku $x^4$: koefisien utamanya berlawanan tepat. $7x^4 + (-7x^4) = 0$, sisanya $3x^2 - 2x - 4$ berderajat 2.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b02-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: batas derajat hasil operasi*

Misalkan $P(x)$ dan $Q(x)$ polinomial yang masing-masing berderajat 6, dan $P(x) + Q(x)$ bukan polinomial nol. Nilai berikut yang TIDAK mungkin menjadi derajat $P(x) + Q(x)$ adalah ....

- A. $1$  
  <sub>Salah: mungkin, mis. $x^6 + x$ dan $-x^6 + 2x$ berjumlah $3x$</sub>
- B. $4$  
  <sub>Salah: mungkin, mis. $x^6 + x^4$ dan $-x^6 + 3$ berjumlah $x^4 + 3$</sub>
- C. $6$  
  <sub>Salah: mungkin, mis. $x^6 + 1$ dan $x^6 + x$ berjumlah derajat 6</sub>
- **D. $7$** ✅  
  <sub>Benar: Derajat jumlah tidak pernah melebihi derajat tertinggi kedua polinomial, yaitu 6.</sub>

**Pembahasan:** Suku berderajat di atas 6 tidak ada pada $P$ maupun $Q$, jadi derajat jumlah paling besar 6. Nilai 6, 4, dan 1 dapat dicapai dengan contoh yang sesuai, sedangkan 7 mustahil.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b02-a-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan perilaku ujung*

Dina menentukan perilaku ujung grafik $f(x) = x^3(2 - x)^2(1 - 3x)$ dengan langkah berikut.
(1) Suku utama tiap faktor: $x^3$, $-x^2$ (dari $(2-x)^2$), dan $-3x$.
(2) Suku utama $f$ adalah $x^3 \cdot (-x^2) \cdot (-3x) = 3x^6$.
(3) Derajat 6 genap dan koefisien utama positif, jadi kedua ujung grafik naik.
Pernyataan yang benar tentang pekerjaan Dina adalah ....

- **A. Langkah (1) salah: suku utama $(2-x)^2$ adalah $x^2$, sehingga suku utama $f$ adalah $-3x^6$ dan kedua ujung turun** ✅  
  <sub>Benar: $(2-x)^2 = x^2 - 4x + 4$ bersuku utama $x^2$ (kuadrat menghilangkan tanda negatif). Suku utama $f$ adalah $x^3 \cdot x^2 \cdot (-3x) = -3x^6$, derajat genap dan koefisien negatif.</sub>
- B. Langkah (3) salah: derajat genap dengan koefisien utama positif membuat kedua ujung turun  
  <sub>Salah: terbalik: koefisien utama positif pada derajat genap justru membuat kedua ujung naik</sub>
- C. Tidak ada kesalahan; kedua ujung grafik $f$ memang naik  
  <sub>Salah: tidak memeriksa suku utama $(2-x)^2$ yang sebenarnya $x^2$</sub>
- D. Langkah (2) salah: $x^3 \cdot (-x^2) \cdot (-3x)$ bernilai negatif sehingga suku utamanya $-3x^6$  
  <sub>Salah: salah mengalikan tanda: dua faktor negatif menghasilkan hasil kali positif</sub>

**Pembahasan:** Jabarkan suku utama $(2-x)^2$: $x^2$. Maka suku utama $f$ = $x^3 \cdot x^2 \cdot (-3x) = -3x^6$ (derajat genap, koefisien negatif), kedua ujung turun. Kesalahan Dina ada pada langkah (1).
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b02-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: evaluasi klaim derajat selisih*

Rani menyatakan bahwa polinomial $(x^3 + 2)^4 - (x^4 - 1)^3$ berderajat 12 karena kedua suku berderajat 12. Pernyataan yang benar tentang klaim Rani adalah ....

- A. Salah; suku $x^{12}$ saling meniadakan dan derajat sebenarnya 8  
  <sub>Salah: mengambil $3x^8$ dari polinomial kedua dan mengabaikan suku $8x^9$</sub>
- B. Salah; derajat selisih adalah $12 - 12 = 0$  
  <sub>Salah: mengurangkan derajat kedua polinomial, padahal yang hilang hanya suku $x^{12}$</sub>
- C. Benar; selisih dua polinomial berderajat 12 selalu berderajat 12  
  <sub>Salah: tidak memeriksa bahwa koefisien $x^{12}$ kedua polinomial sama sehingga hilang</sub>
- **D. Salah; suku $x^{12}$ saling meniadakan dan derajat sebenarnya 9** ✅  
  <sub>Benar: $(x^3+2)^4 = x^{12} + 8x^9 + 24x^6 + 32x^3 + 16$ dan $(x^4-1)^3 = x^{12} - 3x^8 + 3x^4 - 1$. Selisihnya $8x^9 + 3x^8 + \dots$, suku tertinggi $8x^9$.</sub>

**Pembahasan:** Suku $x^{12}$ hilang. Suku berikutnya $8x^9$ dari polinomial pertama (polinomial kedua tidak punya $x^9$), jadi derajat 9.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b02-a-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: evaluasi dua nilai parameter*

Fungsi $f(x) = (k - 1)x^4 + k^2x^2 - 7$ memenuhi $f(2) = 25$, sehingga $k = 2$ atau $k = -6$. Jika grafik $f$ juga mengarah ke bawah di kedua ujungnya, pernyataan yang benar adalah ....

- A. Kedua nilai $k$ memenuhi karena derajat 4 genap  
  <sub>Salah: hanya memeriksa derajat, tidak tanda koefisien utama</sub>
- **B. Hanya $k = -6$ yang memenuhi karena koefisien utama $k - 1 = -7$ negatif** ✅  
  <sub>Benar: Derajat 4 genap, kedua ujung turun bila $k - 1 < 0$. Untuk $k=2$: $1 > 0$ (naik, gugur). Untuk $k=-6$: $-7 < 0$ (turun, memenuhi).</sub>
- C. Hanya $k = 2$ yang memenuhi karena koefisien utama $k - 1 = 1$ positif  
  <sub>Salah: membalik kriteria: koefisien utama positif membuat kedua ujung naik</sub>
- D. Hanya $k = -6$ yang memenuhi karena suku $k^2x^2$ bernilai positif  
  <sub>Salah: memakai suku $k^2x^2$ (bukan suku utama) sebagai penentu ujung</sub>

**Pembahasan:** Ujung kedua-duanya turun jika derajat genap dan koefisien utama negatif: $k-1<0$. $k=-6$ memberikan $-7$, $k=2$ memberikan $1$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b02-a-hard-bt01-006
*orisinal | C6 | 4 langkah | jenis: merancang polinomial memenuhi syarat*

Sebuah polinomial $P(x)$ dirancang agar berderajat 5, berkoefisien utama positif, $P(0) = -2$, dan $P(1) = 4$. Polinomial yang memenuhi semua syarat itu adalah ....

- **A. $P(x) = 2x^5 + x^3 + 3x - 2$** ✅  
  <sub>Benar: Derajat 5, koefisien utama 2 positif, $P(0) = -2$, $P(1) = 2 + 1 + 3 - 2 = 4$.</sub>
- B. $P(x) = 2x^6 + 4x - 2$  
  <sub>Salah: derajatnya 6, bukan 5</sub>
- C. $P(x) = -2x^5 + 8x - 2$  
  <sub>Salah: koefisien utama $-2$ negatif, padahal harus positif</sub>
- D. $P(x) = 2x^5 + x^3 - x + 2$  
  <sub>Salah: $P(0) = 2$, bukan $-2$ (konstanta tertukar tanda)</sub>

**Pembahasan:** Periksa tiap syarat: hanya $2x^5 + x^3 + 3x - 2$ yang memenuhi keempatnya.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b02-a-hard-bt01-007
*orisinal | C6 | 5 langkah | jenis: merancang polinomial memenuhi syarat*

Sebuah fungsi polinomial $P(x)$ dirancang agar berderajat 3, grafiknya naik di ujung kiri dan turun di ujung kanan, $P(0) = 4$, dan $P(2) = 0$. Fungsi yang memenuhi semua syarat itu adalah ....

- **A. $P(x) = -x^3 + x^2 + 4$** ✅  
  <sub>Benar: Suku utama $-x^3$ (derajat ganjil, koefisien negatif) memberi kiri naik dan kanan turun; $P(0) = 4$; $P(2) = -8 + 4 + 4 = 0$.</sub>
- B. $P(x) = x^3 - 3x^2 + 4$  
  <sub>Salah: koefisien utama positif sehingga ujung kiri turun dan kanan naik (terbalik)</sub>
- C. $P(x) = -x^3 + 3x^2 - 4$  
  <sub>Salah: $P(0) = -4$, bukan $4$</sub>
- D. $P(x) = -x^3 + 2x^2 + 4$  
  <sub>Salah: $P(2) = -8 + 8 + 4 = 4$, bukan $0$</sub>

**Pembahasan:** Cek arah ujung dari suku utama, lalu $P(0)$ dan $P(2)$. Hanya $-x^3 + x^2 + 4$ yang memenuhi ketiganya.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b02-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan model fungsi*

Selembar karton berbentuk persegi bersisi 36 cm digunting pada keempat pojoknya berupa persegi kecil bersisi $x$ cm, lalu sisi-sisinya dilipat sehingga terbentuk kotak tanpa tutup. Rita menulis volume kotak sebagai $V(x) = x(36 - x)^2$. Pernyataan yang benar tentang model Rita adalah ....

- A. Salah; $V(x) = x(36 - x)(36 - 2x)$ karena panjang dan lebar alas berbeda  
  <sub>Salah: mengira panjang dan lebar alas berbeda padahal karton persegi</sub>
- B. Benar; sisi alas adalah $36 - x$ karena hanya satu pojok yang digunting  
  <sub>Salah: tidak menyadari bahwa tiap sisi kehilangan dua potongan $x$</sub>
- **C. Salah; sisi alas adalah $36 - 2x$ sehingga $V(x) = x(36 - 2x)^2$** ✅  
  <sub>Benar: Dari tiap sisi karton terpotong dua pojok sehingga sisi alas $36 - 2x$ dan tinggi $x$. Volume $V(x) = x(36-2x)^2 = 4x^3 - 144x^2 + 1.296x$.</sub>
- D. Salah; tinggi kotak $2x$ sehingga $V(x) = 2x(36 - 2x)^2$  
  <sub>Salah: mengira tinggi lipatan dua kali sisi pojok</sub>

**Pembahasan:** Tiap sisi 36 cm kehilangan $x$ di kedua ujungnya, sisi alas $36 - 2x$. Maka $V(x) = x(36-2x)^2$, polinomial derajat 3.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b02-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: evaluasi sifat ujung hasil operasi*

Grafik fungsi polinomial $f$ dan $g$ keduanya turun di ujung kiri maupun ujung kanan. Pernyataan yang pasti benar tentang $f + g$ dan $f \cdot g$ adalah ....

- A. $f + g$ dan $f \cdot g$ keduanya turun di kedua ujung  
  <sub>Salah: mengira hasil kali mempertahankan tanda negatif</sub>
- **B. $f + g$ turun di kedua ujung dan $f \cdot g$ naik di kedua ujung** ✅  
  <sub>Benar: Keduanya berderajat genap dengan koefisien utama negatif. Suku utama $f+g$ bertanda negatif berderajat genap (turun-turun); suku utama $f \cdot g$ hasil kali dua bilangan negatif, positif, berderajat genap (naik-naik).</sub>
- C. $f + g$ naik di kedua ujung dan $f \cdot g$ turun di kedua ujung  
  <sub>Salah: menukar sifat jumlah dan hasil kali</sub>
- D. $f + g$ dan $f \cdot g$ keduanya naik di kedua ujung  
  <sub>Salah: mengira jumlah dua fungsi bertanda negatif menjadi positif</sub>

**Pembahasan:** Contoh $f = -3x^2 + x$, $g = -2x^4 + 5$: jumlah bersuku utama $-2x^4$, hasil kali bersuku utama $6x^6$. Sifat ini berlaku umum.
**Acuan:** siswa — siswa hal.71

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
