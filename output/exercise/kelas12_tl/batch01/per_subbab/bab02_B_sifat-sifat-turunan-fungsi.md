# Lembar koreksi — kelas12_tl SMA12L-B2 subbab B: Sifat-Sifat Turunan Fungsi

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b02-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: turunan perkalian aljabar trigonometri*

Tentukan turunan pertama dari fungsi $y = (4x^2 + 7)\sin x$.

- **A. $y' = 8x\sin x + (4x^2 + 7)\cos x$** ✅  
  <sub>Benar: Menggunakan aturan perkalian $(uv)' = u'v + uv'$, dengan $u = 4x^2 + 7 \implies u' = 8x$ dan $v = \sin x \implies v' = \cos x$.</sub>
- B. $y' = 8x\cos x + (4x^2 + 7)\sin x$  
  <sub>Salah: Tertukar pasangan fungsi asli dengan turunannya pada aturan perkalian.</sub>
- C. $y' = 8x\sin x - (4x^2 + 7)\cos x$  
  <sub>Salah: Salah menggunakan tanda operasi pengurangan pada aturan hasil kali.</sub>
- D. $y' = 8x\cos x$  
  <sub>Salah: Hanya mengalikan turunan masing-masing faktor tanpa menerapkan aturan perkalian turunan.</sub>

**Pembahasan:** Misalkan $u(x) = 4x^2 + 7$ sehingga $u'(x) = 8x$, dan $v(x) = \sin x$ sehingga $v'(x) = \cos x$.
Berdasarkan aturan turunan perkalian dua fungsi:
$$y' = u'(x)v(x) + u(x)v'(x)$$
$$y' = 8x\sin x + (4x^2 + 7)\cos x$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b02-b-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: turunan fungsi eksponen dasar*

Tentukan turunan pertama dari fungsi $y = 6^x$.

- **A. $y' = 6^x \ln 6$** ✅  
  <sub>Benar: Berdasarkan sifat turunan fungsi eksponensial $a^x$, turunannya adalah $a^x \ln a$.</sub>
- B. $y' = x \cdot 6^{x-1}$  
  <sub>Salah: Salah menerapkan aturan pangkat fungsi aljabar pada fungsi eksponen.</sub>
- C. $y' = \dfrac{6^x}{\ln 6}$  
  <sub>Salah: Membagi dengan logaritma natural bukan mengalikannya.</sub>
- D. $y' = 6^x$  
  <sub>Salah: Mengira turunan basis sebarang sama seperti turunan basis natural e.</sub>

**Pembahasan:** Berdasarkan sifat turunan fungsi eksponensial dengan basis $a > 0$ dan $a \ne 1$:
$$\frac{d}{dx}(a^x) = a^x \ln a$$
Untuk $y = 6^x$, diperoleh:
$$y' = 6^x \ln 6$$
**Acuan:** siswa — siswa hal.142 Ayo Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b02-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: turunan fungsi eksponen rantai*

Tentukan turunan pertama dari fungsi $y = e^{\sqrt{x+5}}$.

- A. $y' = e^{\sqrt{x+5}}$  
  <sub>Salah: Lupa mengalikan dengan turunan fungsi pangkat di dalamnya.</sub>
- B. $y' = \dfrac{e^{\sqrt{x+5}}}{\sqrt{x+5}}$  
  <sub>Salah: Lupa mengikutsertakan penyebut 2 dari rumus turunan akar kuadrat.</sub>
- C. $y' = 2\sqrt{x+5}\,e^{\sqrt{x+5}}$  
  <sub>Salah: Terbalik mengalikan dengan turunan akar bukannya membagi.</sub>
- **D. $y' = \dfrac{e^{\sqrt{x+5}}}{2\sqrt{x+5}}$** ✅  
  <sub>Benar: Menurunkan fungsi eksponen luar dikalikan dengan turunan fungsi pangkat $\frac{1}{2\sqrt{x+5}}$.</sub>

**Pembahasan:** Misalkan $u = \sqrt{x+5} = (x+5)^{\frac{1}{2}}$, maka $u' = \frac{1}{2\sqrt{x+5}}$.
Berdasarkan aturan rantai untuk $y = e^u$:
$$y' = e^u \cdot u' = e^{\sqrt{x+5}} \cdot \frac{1}{2\sqrt{x+5}} = \frac{e^{\sqrt{x+5}}}{2\sqrt{x+5}}$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b02-b-easy-bt01-004
*orisinal | C2 | 2 langkah | jenis: turunan fungsi trigonometri tangen*

Tentukan turunan pertama dari fungsi $f(x) = 4\tan x - 7x$.

- A. $f'(x) = 4\sec^2 x$  
  <sub>Salah: Lupa menurunkan suku aljabar linier $-7x$.</sub>
- **B. $f'(x) = 4\sec^2 x - 7$** ✅  
  <sub>Benar: Menerapkan sifat turunan tangen $\frac{d}{dx}(\tan x) = \sec^2 x$ dan turunan aljabar linier $\frac{d}{dx}(-7x) = -7$.</sub>
- C. $f'(x) = 4\sec x\tan x - 7$  
  <sub>Salah: Tertukar dengan rumus turunan fungsi sekan.</sub>
- D. $f'(x) = -4\csc^2 x - 7$  
  <sub>Salah: Tertukar dengan rumus turunan fungsi kotangen.</sub>

**Pembahasan:** Gunakan sifat kelipatan konstan dan turunan pengurangan fungsi:
$$f'(x) = 4 \cdot \frac{d}{dx}(\tan x) - \frac{d}{dx}(7x)$$
Karena $\frac{d}{dx}(\tan x) = \sec^2 x$ dan $\frac{d}{dx}(7x) = 7$, maka:
$$f'(x) = 4\sec^2 x - 7$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b02-b-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: turunan kombinasi aljabar trigonometri*

Tentukan turunan pertama dari fungsi $f(x) = 6x^3 - 8\cos x + 15$.

- A. $f'(x) = 18x^2 - 8\cos x$  
  <sub>Salah: Tidak menurunkan fungsi kosinus trigonometri.</sub>
- B. $f'(x) = 18x^2 + 8\sin x + 15$  
  <sub>Salah: Turunan konstanta tidak dijadikan nol melainkan tetap ditulis.</sub>
- C. $f'(x) = 18x^2 - 8\sin x$  
  <sub>Salah: Lupa bahwa turunan dari $\cos x$ menghasilkan tanda negatif.</sub>
- **D. $f'(x) = 18x^2 + 8\sin x$** ✅  
  <sub>Benar: Menurunkan suku polinomial menjadi $18x^2$, kosinus menjadi $-\sin x$ sehingga $-8(-\sin x) = +8\sin x$, dan turunan konstanta 15 adalah 0.</sub>

**Pembahasan:** Turunkan setiap suku fungsi secara terpisah:
- Turunan dari $6x^3$ adalah $6 \cdot 3x^2 = 18x^2$.
- Turunan dari $-8\cos x$ adalah $-8(-\sin x) = 8\sin x$.
- Turunan dari konstanta $15$ adalah $0$.
Jadi, $f'(x) = 18x^2 + 8\sin x$.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b02-b-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: turunan eksponen linear*

Tentukan turunan pertama dari fungsi $y = e^{5x}$.

- A. $y' = \dfrac{1}{5}e^{5x}$  
  <sub>Salah: Tertukar dengan rumus antiturunan (integral) fungsi eksponensial.</sub>
- B. $y' = e^{5x}$  
  <sub>Salah: Lupa mengalikan dengan turunan dari fungsi pangkat $5x$.</sub>
- **C. $y' = 5e^{5x}$** ✅  
  <sub>Benar: Berdasarkan sifat turunan fungsi $e^{f(x)}$, turunannya adalah $f'(x)e^{f(x)}$. Dengan $f(x) = 5x$, diperoleh $f'(x) = 5$, sehingga $y' = 5e^{5x}$.</sub>
- D. $y' = 5x e^{5x-1}$  
  <sub>Salah: Menerapkan aturan pangkat aljabar pada fungsi eksponensial.</sub>

**Pembahasan:** Berdasarkan sifat turunan fungsi eksponensial alami $y = e^{f(x)}$:
$y' = f'(x) \cdot e^{f(x)}$

Untuk $f(x) = 5x$, kita peroleh $f'(x) = 5$.
Jadi:
$y' = 5e^{5x}$.
**Acuan:** siswa — siswa hal.142 Ayo Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b02-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: turunan eksponen bentuk akar rantai*

Tentukan turunan pertama dari fungsi $y = e^{\sqrt{x-3}}$.

- **A. $y' = \dfrac{e^{\sqrt{x-3}}}{2\sqrt{x-3}}$** ✅  
  <sub>Benar: Turunan dari $e^{u}$ adalah $u'e^u$. Untuk $u = \sqrt{x-3} = (x-3)^{1/2}$, turunannya adalah $u' = \dfrac{1}{2\sqrt{x-3}}$, sehingga $y' = \dfrac{e^{\sqrt{x-3}}}{2\sqrt{x-3}}$.</sub>
- B. $y' = \dfrac{e^{\sqrt{x-3}}}{2(x-3)}$  
  <sub>Salah: Menghilangkan akar pada penyebut hasil turunan rantai.</sub>
- C. $y' = \dfrac{e^{\sqrt{x-3}}}{\sqrt{x-3}}$  
  <sub>Salah: Lupa faktor pembagi 2 pada turunan bentuk akar kuadrat.</sub>
- D. $y' = 2\sqrt{x-3}e^{\sqrt{x-3}}$  
  <sub>Salah: Mengalikan turunan akar bukan membaginya dengan $2\sqrt{x-3}$.</sub>

**Pembahasan:** Misalkan $u = \sqrt{x-3} = (x-3)^{\frac{1}{2}}$.
Turunan dari $u$ terhadap $x$ adalah:
$u' = \frac{1}{2}(x-3)^{-\frac{1}{2}} = \frac{1}{2\sqrt{x-3}}$

Dengan aturan rantai untuk fungsi eksponen:
$y' = u' \cdot e^u = \dfrac{1}{2\sqrt{x-3}} \cdot e^{\sqrt{x-3}} = \dfrac{e^{\sqrt{x-3}}}{2\sqrt{x-3}}$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b02-b-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: turunan fungsi trigonometri sekan*

Tentukan turunan pertama dari fungsi $f(x) = 5\sec x$.

- A. $f'(x) = 5\tan x$  
  <sub>Salah: Hanya mengganti fungsi sekan menjadi tangen tanpa faktor sekan.</sub>
- **B. $f'(x) = 5\sec x \tan x$** ✅  
  <sub>Benar: Turunan dari $\sec x$ adalah $\sec x \tan x$, dikalikan dengan skalar 5 menjadi $5\sec x \tan x$.</sub>
- C. $f'(x) = -5\sec x \tan x$  
  <sub>Salah: Salah mengira turunan sekan memiliki tanda negatif seperti kosekan.</sub>
- D. $f'(x) = 5\sec^2 x$  
  <sub>Salah: Tertukar dengan turunan fungsi tangen.</sub>

**Pembahasan:** Berdasarkan Sifat Turunan Trigonometri 4 (STT 4):
Jika $g(x) = \sec x$, maka $g'(x) = \sec x \tan x$.

Dengan sifat kelipatan konstanta:
$f'(x) = 5 \cdot g'(x) = 5\sec x \tan x$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b02-b-easy-bt01-009
*orisinal | C2 | 2 langkah | jenis: turunan fungsi trigonometri kotangen*

Tentukan turunan pertama dari fungsi $f(x) = 3\cot x + 8$.

- **A. $f'(x) = -3\csc^2 x$** ✅  
  <sub>Benar: Turunan dari $\cot x$ adalah $-\csc^2 x$ dan turunan dari konstanta 8 adalah 0, sehingga $f'(x) = -3\csc^2 x$.</sub>
- B. $f'(x) = 3\csc^2 x$  
  <sub>Salah: Lupa tanda negatif pada turunan fungsi kotangen.</sub>
- C. $f'(x) = -3\cot x \csc x$  
  <sub>Salah: Tertukar dengan rumus turunan fungsi kosekan.</sub>
- D. $f'(x) = -3\csc^2 x + 8$  
  <sub>Salah: Tidak menurunkan suku konstanta (salah menganggap turunan konstanta tetap).</sub>

**Pembahasan:** Berdasarkan sifat turunan trigonometri (STT 3):
Turunan dari $\cot x$ adalah $-\csc^2 x$.
Berdasarkan turunan fungsi konstan, turunan dari konstanta $8$ adalah $0$.

Maka:
$f'(x) = 3(-\csc^2 x) + 0 = -3\csc^2 x$.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b02-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: turunan perkalian aljabar trigonometri cosinus*

Tentukan turunan pertama dari fungsi $y = (7x^4 - 9)\cos x$.

- A. $y' = 28x^3\cos x + (7x^4 - 9)\sin x$  
  <sub>Salah: Lupa bahwa turunan dari $\cos x$ menghasilkan tanda negatif ($-\sin x$).</sub>
- B. $y' = 7x^3\cos x - (7x^4 - 9)\sin x$  
  <sub>Salah: Salah menghitung turunan aljabar dengan tidak mengalikan pangkat lama dengan koefisien awal.</sub>
- **C. $y' = 28x^3\cos x - (7x^4 - 9)\sin x$** ✅  
  <sub>Benar: Menggunakan aturan perkalian $(uv)' = u'v + uv'$ dengan $u = 7x^4 - 9$ dan $v = \cos x$.</sub>
- D. $y' = -28x^3\sin x$  
  <sub>Salah: Hanya mengalikan turunan dari masing-masing fungsi tanpa menerapkan aturan perkalian turunan.</sub>

**Pembahasan:** Misalkan $u(x) = 7x^4 - 9$ dan $v(x) = \cos x$.
Maka diperoleh:
$u'(x) = 4 \cdot 7x^{4-1} = 28x^3$
$v'(x) = -\sin x$

Berdasarkan aturan perkalian turunan fungsi:
$y' = u'(x)v(x) + u(x)v'(x)$
$y' = 28x^3 \cos x + (7x^4 - 9)(-\sin x)$
$y' = 28x^3 \cos x - (7x^4 - 9)\sin x$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b02-b-easy-bt01-011
*variasi (angka) | C2 | 1 langkah | jenis: turunan penjumlahan sinus aljabar*

Tentukan turunan pertama dari fungsi $y = 8\sin x + 9x$.

- A. $y' = 8\cos x$  
  <sub>Salah: Lupa menurunkan suku linear $9x$ atau menganggapnya bernilai nol.</sub>
- B. $y' = 8\sin x + 9$  
  <sub>Salah: Lupa menurunkan fungsi trigonometri $\sin x$.</sub>
- **C. $y' = 8\cos x + 9$** ✅  
  <sub>Benar: Turunan dari $\sin x$ adalah $\cos x$ dan turunan dari $9x$ adalah $9$.</sub>
- D. $y' = -8\cos x + 9$  
  <sub>Salah: Keliru menganggap turunan $\sin x$ bernilai negatif.</sub>

**Pembahasan:** Gunakan sifat turunan penjumlahan dan turunan fungsi dasar:
$y = 8\sin x + 9x$
$y' = 8(\cos x) + 9(1)$
$y' = 8\cos x + 9$
**Acuan:** siswa — siswa hal.134 Contoh Soal 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b02-b-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: turunan eksponen basis a aturan rantai*

Tentukan turunan pertama dari fungsi $y = 7^{6x}$.

- A. $y' = 7^{6x} \ln 7$  
  <sub>Salah: Lupa mengalikan dengan turunan dari fungsi pangkat $6x$.</sub>
- **B. $y' = 6 \cdot 7^{6x} \ln 7$** ✅  
  <sub>Benar: Turunan dari $a^{g(x)}$ adalah $g'(x) \cdot a^{g(x)} \ln a$.</sub>
- C. $y' = 6 \cdot 7^{6x}$  
  <sub>Salah: Lupa mengalikan dengan faktor logaritma natural dari basis ($\,\ln 7$).</sub>
- D. $y' = 6x \cdot 7^{6x-1}$  
  <sub>Salah: Salah menerapkan rumus fungsi pangkat aljabar pada fungsi eksponensial.</sub>

**Pembahasan:** Berdasarkan sifat turunan fungsi eksponensial dengan aturan rantai:
Jika $y = a^{g(x)}$, maka $y' = g'(x) \cdot a^{g(x)} \ln a$.
Di sini $a = 7$ dan $g(x) = 6x$, sehingga $g'(x) = 6$.
Diperoleh:
$y' = 6 \cdot 7^{6x} \ln 7$
**Acuan:** siswa — siswa hal.141 Contoh Soal 2.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b02-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: turunan fungsi trigonometri kosekan*

Tentukan turunan pertama dari fungsi $f(x) = 6\csc x$.

- A. $f'(x) = -6\csc^2 x$  
  <sub>Salah: Tertukar dengan bentuk turunan fungsi kotangen.</sub>
- B. $f'(x) = -6\cot x$  
  <sub>Salah: Kehilangan faktor $\csc x$ pada hasil turunan.</sub>
- C. $f'(x) = 6\csc x \cot x$  
  <sub>Salah: Lupa menyertakan tanda negatif pada hasil turunan fungsi kosekan.</sub>
- **D. $f'(x) = -6\csc x \cot x$** ✅  
  <sub>Benar: Berdasarkan STT 5, turunan dari $\csc x$ adalah $-\csc x \cot x$.</sub>

**Pembahasan:** Berdasarkan Sifat Turunan Trigonometri 5 (STT 5):
Jika $g(x) = \csc x$, maka $g'(x) = -\csc x \cot x$.
Maka untuk $f(x) = 6\csc x$:
$f'(x) = 6(-\csc x \cot x) = -6\csc x \cot x$.
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b02-b-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: turunan fungsi konstan*

Tentukan turunan pertama dari fungsi konstan $f(x) = -85$.

- A. $f'(x) = -1$  
  <sub>Salah: Mengira turunan konstanta negatif menghasilkan $-1$.</sub>
- B. $f'(x) = -85$  
  <sub>Salah: Mengira hasil turunan fungsi konstan adalah nilai konstanta tersebut.</sub>
- **C. $f'(x) = 0$** ✅  
  <sub>Benar: Turunan dari fungsi konstan apapun selalu bernilai 0.</sub>
- D. $f'(x) = 1$  
  <sub>Salah: Tertukar dengan turunan dari fungsi linear $x$.</sub>

**Pembahasan:** Berdasarkan sifat Turunan Fungsi Konstan (TFK):
Untuk setiap fungsi konstan $f(x) = c$ dengan $c \in \mathbb{R}$, berlaku:
$f'(x) = 0$.
Karena $f(x) = -85$ adalah fungsi konstan, maka $f'(x) = 0$.
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b02-b-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: turunan fungsi eksponen natural rantai polinomial*

Tentukan turunan pertama dari fungsi $y = e^{5x^2}$.

- A. $y' = 10x e^{5x}$  
  <sub>Salah: Siswa salah menerapkan aturan eksponen dengan mengurangi pangkat pada fungsi asal.</sub>
- **B. $y' = 10x e^{5x^2}$** ✅  
  <sub>Benar: Berdasarkan aturan turunan fungsi eksponensial $y = e^{f(x)}$, diperoleh $y' = f'(x)e^{f(x)}$. Karena $f(x) = 5x^2$, maka $f'(x) = 10x$, sehingga $y' = 10x e^{5x^2}$.</sub>
- C. $y' = 5x e^{5x^2}$  
  <sub>Salah: Siswa salah menurunkan pangkat kuadrat tanpa mengalikan koefisien 5 dengan pangkat 2.</sub>
- D. $y' = e^{5x^2}$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan dari fungsi pangkat (aturan rantai).</sub>

**Pembahasan:** Misalkan $f(x) = 5x^2$, maka $f'(x) = 10x$.
Turunan dari $y = e^{f(x)}$ adalah:
$y' = f'(x)e^{f(x)} = 10x e^{5x^2}$.
**Acuan:** siswa — siswa hal.142 Ayo Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b02-b-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: turunan fungsi trigonometri sinus aturan rantai*

Tentukan turunan pertama dari fungsi trigonometri $f(x) = 8 - 5\sin(3x)$.

- A. $f'(x) = -15\sin(3x)$  
  <sub>Salah: Siswa lupa mengubah fungsi sinus menjadi kosinus saat melakukan penurunan.</sub>
- B. $f'(x) = 15\cos(3x)$  
  <sub>Salah: Siswa salah menentukan tanda turunan sinus, mengira turunan $-\sin$ menghasilkan positif $\cos$.</sub>
- C. $f'(x) = -5\cos(3x)$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan fungsi di dalam sinus yaitu 3.</sub>
- **D. $f'(x) = -15\cos(3x)$** ✅  
  <sub>Benar: Turunan dari konstanta 8 adalah 0. Turunan dari $-5\sin(3x)$ adalah $-5 \cdot (\cos(3x)) \cdot 3 = -15\cos(3x)$.</sub>

**Pembahasan:** Diketahui $f(x) = 8 - 5\sin(3x)$.
Turunan dari konstanta 8 adalah $0$.
Dengan aturan rantai untuk $-5\sin(3x)$:
$\frac{d}{dx}[-5\sin(3x)] = -5 \cdot \cos(3x) \cdot \frac{d}{dx}[3x] = -5 \cdot 3\cos(3x) = -15\cos(3x)$.
Jadi, $f'(x) = -15\cos(3x)$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b02-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: turunan kombinasi linear sinus cosinus*

Tentukan turunan pertama dari fungsi $f(x) = 5\cos x - 3\sin x$.

- **A. $f'(x) = -5\sin x - 3\cos x$** ✅  
  <sub>Benar: Turunan dari $\cos x$ adalah $-\sin x$ dan turunan dari $\sin x$ adalah $\cos x$, sehingga $f'(x) = 5(-\sin x) - 3(\cos x) = -5\sin x - 3\cos x$.</sub>
- B. $f'(x) = 5\sin x - 3\cos x$  
  <sub>Salah: Siswa lupa tanda minus pada turunan $\cos x$.</sub>
- C. $f'(x) = 5\cos x - 3\sin x$  
  <sub>Salah: Siswa menganggap fungsi trigonometri tidak berubah bentuk ketika diturunkan.</sub>
- D. $f'(x) = -5\sin x + 3\cos x$  
  <sub>Salah: Siswa salah menyimpulkan turunan $\sin x$ bernilai negatif sehingga tanda berubah menjadi penjumlahan.</sub>

**Pembahasan:** Gunakan Sifat Turunan Trigonometri 1:
- $\frac{d}{dx}[\cos x] = -\sin x$
- $\frac{d}{dx}[\sin x] = \cos x$

Maka:
$f'(x) = 5(-\sin x) - 3(\cos x) = -5\sin x - 3\cos x$.
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b02-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: turunan kombinasi fungsi eksponen natural dan aljabar*

Tentukan turunan pertama dari fungsi $f(x) = 7e^x + 4x^3$.

- A. $f'(x) = 7x e^{x-1} + 12x^2$  
  <sub>Salah: Siswa salah memperlakukan fungsi eksponen $e^x$ seperti variabel berpangkat $x^n$.</sub>
- B. $f'(x) = 7e^x + 4x^2$  
  <sub>Salah: Siswa hanya mengurangi pangkat aljabar tanpa mengalikannya ke koefisien depan.</sub>
- **C. $f'(x) = 7e^x + 12x^2$** ✅  
  <sub>Benar: Turunan dari $7e^x$ adalah $7e^x$ dan turunan dari $4x^3$ adalah $4 \cdot 3x^2 = 12x^2$. Jumlah keduanya adalah $7e^x + 12x^2$.</sub>
- D. $f'(x) = e^x + 12x^2$  
  <sub>Salah: Siswa menghilangkan koefisien pengali pada suku eksponen natural.</sub>

**Pembahasan:** Berdasarkan sifat penjumlahan dan kaidah dasar turunan:
1. $\frac{d}{dx}[7e^x] = 7 \cdot \frac{d}{dx}[e^x] = 7e^x$
2. $\frac{d}{dx}[4x^3] = 4 \cdot (3x^2) = 12x^2$

Sehingga diperoleh:
$f'(x) = 7e^x + 12x^2$.
**Acuan:** siswa — siswa hal.139

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b02-b-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: turunan fungsi trigonometri rantai sudut pecahan pi*

Diketahui persamaan fungsi trigonometri $f(x) = 7 - 9\sin\left(\frac{1}{5}\pi x\right)$ didefinisikan pada daerah asal $D_f = \{x \mid 0 \le x \le 10, x \in \mathbb{R}\}$. Tentukan turunan pertama dari $f(x)$.

- A. $f'(x) = \frac{9}{5}\pi\cos\left(\frac{1}{5}\pi x\right)$  
  <sub>Salah: Kesalahan tanda akibat mengabaikan tanda negatif di depan koefisien sinus.</sub>
- **B. $f'(x) = -\frac{9}{5}\pi\cos\left(\frac{1}{5}\pi x\right)$** ✅  
  <sub>Benar: Turunan dari konstanta 7 adalah 0, turunan dari $\sin(u)$ adalah $\cos(u)$, dan turunan dari $u = \frac{1}{5}\pi x$ adalah $\frac{1}{5}\pi$, sehingga $f'(x) = -9 \cdot \frac{1}{5}\pi \cos\left(\frac{1}{5}\pi x\right) = -\frac{9}{5}\pi\cos\left(\frac{1}{5}\pi x\right)$.</sub>
- C. $f'(x) = -9\pi\cos\left(\frac{1}{5}\pi x\right)$  
  <sub>Salah: Lupa membagi dengan faktor penyebut 5 pada turunan argumen dalam.</sub>
- D. $f'(x) = -\frac{9}{5}\pi\sin\left(\frac{1}{5}\pi x\right)$  
  <sub>Salah: Lupa mengubah fungsi sinus menjadi kosinus saat melakukan diferensiasi.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan dari konstanta dan fungsi trigonometri.
Turunan dari konstanta 7 adalah 0.
Dengan aturan rantai, jika $g(x) = \sin(u)$ dengan $u = \frac{1}{5}\pi x$, maka $g'(x) = u' \cdot \cos(u)$.

Langkah 2: Menghitung turunan rantai.
$u' = \frac{d}{dx}\left(\frac{1}{5}\pi x\right) = \frac{1}{5}\pi$
$f'(x) = 0 - 9 \cdot \frac{1}{5}\pi \cos\left(\frac{1}{5}\pi x\right) = -\frac{9}{5}\pi\cos\left(\frac{1}{5}\pi x\right)$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b02-b-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: turunan eksponen basis a aturan rantai polinomial*

Tentukan turunan pertama dari fungsi $y = 7^{x^3 + 6}$.

- A. $y' = 3x^2 \cdot 7^{x^3 + 6}$  
  <sub>Salah: Lupa mengalikan dengan $\ln 7$ karena memperlakukan basis seperti bilangan natural $e$.</sub>
- B. $y' = (x^3 + 6) \cdot 7^{x^3 + 5}$  
  <sub>Salah: Keliru menerapkan aturan turunan fungsi pangkat aljabar biasa $n \cdot x^{n-1}$ pada fungsi eksponensial.</sub>
- C. $y' = 7^{x^3 + 6} \ln 7$  
  <sub>Salah: Lupa mengalikan dengan turunan fungsi pangkatnya ($3x^2$).</sub>
- **D. $y' = 3x^2 \cdot 7^{x^3 + 6} \ln 7$** ✅  
  <sub>Benar: Turunan dari $y = a^{u(x)}$ adalah $y' = u'(x) \cdot a^{u(x)} \ln a$. Dengan $u(x) = x^3 + 6$, diperoleh $u'(x) = 3x^2$, sehingga $y' = 3x^2 \cdot 7^{x^3 + 6} \ln 7$.</sub>

**Pembahasan:** Misalkan $u(x) = x^3 + 6$, maka $u'(x) = 3x^2$.
Berdasarkan sifat turunan fungsi eksponensial $y = a^u$, turunannya adalah:
$$y' = u'(x) \cdot a^{u(x)} \ln a$$
Substitusikan $u(x)$ dan $a = 7$:
$$y' = 3x^2 \cdot 7^{x^3 + 6} \ln 7$$
**Acuan:** siswa — siswa hal.142 Ayo Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b02-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: turunan fungsi aljabar berpangkat pecahan*

Tentukan turunan pertama dari fungsi $y = \sqrt{\dfrac{1}{(4x + 5)^5}}$.

- A. $y' = \dfrac{10}{(4x + 5)^{7/2}}$  
  <sub>Salah: Lupa tanda minus dari pangkat eksponen negatif saat diturunkan.</sub>
- B. $y' = -\dfrac{10}{(4x + 5)^{3/2}}$  
  <sub>Salah: Salah melakukan pengurangan eksponen, $-5/2 - 1$ dihitung menjadi $-3/2$.</sub>
- **C. $y' = -\dfrac{10}{(4x + 5)^{7/2}}$** ✅  
  <sub>Benar: Bentuk diubah menjadi $y = (4x + 5)^{-5/2}$. Turunannya adalah $y' = -\frac{5}{2}(4x + 5)^{-7/2} \cdot 4 = -10(4x + 5)^{-7/2} = -\frac{10}{(4x + 5)^{7/2}}$.</sub>
- D. $y' = -\dfrac{5}{2(4x + 5)^{7/2}}$  
  <sub>Salah: Lupa mengalikan dengan turunan fungsi dalam rantai, yaitu 4.</sub>

**Pembahasan:** Ubah bentuk akar menjadi pangkat pecahan:
$$y = ((4x + 5)^{-5})^{1/2} = (4x + 5)^{-5/2}$$

Gunakan aturan rantai:
$$y' = -\frac{5}{2}(4x + 5)^{-\frac{5}{2} - 1} \cdot \frac{d}{dx}(4x + 5)$$
$$y' = -\frac{5}{2}(4x + 5)^{-7/2} \cdot 4$$
$$y' = -10(4x + 5)^{-7/2} = -\frac{10}{(4x + 5)^{7/2}}$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b02-b-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: turunan fungsi hasil bagi trigonometri*

Tentukan turunan pertama dari fungsi $f(x) = \dfrac{\sin x}{x^2 + 1}$.

- A. $f'(x) = \dfrac{\cos x}{2x}$  
  <sub>Salah: Menurunkan langsung pembilang dan penyebut secara terpisah tanpa sifat hasil bagi.</sub>
- B. $f'(x) = \dfrac{(x^2 + 1)\cos x + 2x\sin x}{(x^2 + 1)^2}$  
  <sub>Salah: Tertukar rumus pembagian dengan penjumlahan pada pembilang ($u'v + uv'$).</sub>
- **C. $f'(x) = \dfrac{(x^2 + 1)\cos x - 2x\sin x}{(x^2 + 1)^2}$** ✅  
  <sub>Benar: Dengan memisalkan $u(x) = \sin x$ dan $v(x) = x^2 + 1$, diperoleh $u'(x) = \cos x$ dan $v'(x) = 2x$. Melalui sifat turunan pembagian, $f'(x) = \frac{u'v - uv'}{v^2} = \frac{(x^2 + 1)\cos x - 2x\sin x}{(x^2 + 1)^2}$.</sub>
- D. $f'(x) = \dfrac{2x\sin x - (x^2 + 1)\cos x}{(x^2 + 1)^2}$  
  <sub>Salah: Urutan pengurangan pada pembilang terbalik ($uv' - u'v$).</sub>

**Pembahasan:** Gunakan aturan pembagian $f(x) = \frac{u(x)}{v(x)}$:
- $u(x) = \sin x \implies u'(x) = \cos x$
- $v(x) = x^2 + 1 \implies v'(x) = 2x$

Rumus turunan pembagian:
$$f'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2}$$
$$f'(x) = \frac{(\cos x)(x^2 + 1) - (\sin x)(2x)}{(x^2 + 1)^2} = \frac{(x^2 + 1)\cos x - 2x\sin x}{(x^2 + 1)^2}$$
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b02-b-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: nilai turunan fungsi eksponensial*

Diketahui fungsi $f(x) = (3x - 2)e^{2x}$. Tentukan nilai dari $f'(1)$.

- A. $7e^2$  
  <sub>Salah: Salah melakukan operasi aljabar di dalam tanda kurung menjadi $(6x + 1)e^{2x}$.</sub>
- B. $3e^2$  
  <sub>Salah: Hanya menurunkan bagian aljabar $(3x - 2)$ dan tidak menerapkan aturan perkalian.</sub>
- **C. $5e^2$** ✅  
  <sub>Benar: Turunan $f'(x) = 3e^{2x} + (3x - 2)(2e^{2x}) = (6x - 1)e^{2x}$. Untuk $x = 1$, diperoleh $f'(1) = (6(1) - 1)e^{2(1)} = 5e^2$.</sub>
- D. $4e^2$  
  <sub>Salah: Lupa mengalikan turunan pangkat dari $e^{2x}$ (mengabaikan faktor 2 pada turunan rantai).</sub>

**Pembahasan:** Gunakan aturan perkalian $f(x) = u(x)v(x)$:
- $u(x) = 3x - 2 \implies u'(x) = 3$
- $v(x) = e^{2x} \implies v'(x) = 2e^{2x}$ (menggunakan aturan rantai)

Turunan pertama:
$$f'(x) = u'(x)v(x) + u(x)v'(x)$$
$$f'(x) = 3e^{2x} + (3x - 2)(2e^{2x}) = e^{2x}(3 + 6x - 4) = (6x - 1)e^{2x}$$

Substitusi nilai $x = 1$:
$$f'(1) = (6(1) - 1)e^{2(1)} = 5e^2$$
**Acuan:** siswa — siswa hal.139

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b02-b-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: aturan rantai fungsi trigonometri*

Tentukan turunan pertama dari fungsi $f(x) = \sin^3(4x)$.

- A. $f'(x) = 12\sin^2(4x)$  
  <sub>Salah: Lupa menuliskan turunan dari fungsi sinus yaitu $\cos(4x)$.</sub>
- B. $f'(x) = -12\sin^2(4x)\cos(4x)$  
  <sub>Salah: Tertukar tanda turunan sinus dengan turunan kosinus (mengira turunan sinus bernilai negatif).</sub>
- C. $f'(x) = 3\sin^2(4x)\cos(4x)$  
  <sub>Salah: Lupa mengalikan dengan turunan sudut dalamnya yaitu 4.</sub>
- **D. $f'(x) = 12\sin^2(4x)\cos(4x)$** ✅  
  <sub>Benar: Berdasarkan aturan rantai, $f'(x) = 3\sin^2(4x) \cdot \frac{d}{dx}(\sin(4x)) = 3\sin^2(4x) \cdot (4\cos(4x)) = 12\sin^2(4x)\cos(4x)$.</sub>

**Pembahasan:** Fungsi berbentuk komposisi $f(x) = (u(x))^3$ dengan $u(x) = \sin(4x)$.

Langkah-langkah dengan aturan rantai:
1) Turunkan bentuk pangkat terluar:
$$\frac{d}{du}(u^3) = 3u^2 = 3\sin^2(4x)$$

2) Turunkan fungsi trigonometri beserta sudutnya:
$$\frac{du}{dx} = \frac{d}{dx}(\sin(4x)) = \cos(4x) \cdot 4 = 4\cos(4x)$$

3) Kalikan kedua turunan tersebut:
$$f'(x) = 3\sin^2(4x) \cdot 4\cos(4x) = 12\sin^2(4x)\cos(4x)$$
**Acuan:** siswa — siswa hal.126

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b02-b-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: laju perubahan luas permukaan*

Jari-jari sebuah bola bertambah panjang dengan laju $5\text{ cm}$ per detik. Misalkan jari-jari bola tersebut $40\text{ cm}$. Tentukan laju bertambahnya luas permukaan bola.

- **A. $1.600\pi\text{ cm}^2/\text{detik}$** ✅  
  <sub>Benar: Luas permukaan bola dinyatakan dengan $L = 4\pi r^2$. Dengan aturan rantai terhadap waktu $t$, laju perubahannya adalah $\frac{dL}{dt} = 8\pi r \frac{dr}{dt}$. Dengan mensubstitusikan $r = 40\text{ cm}$ dan $\frac{dr}{dt} = 5\text{ cm/detik}$, didapatkan $\frac{dL}{dt} = 8\pi(40)(5) = 1.600\pi\text{ cm}^2/\text{detik}$.</sub>
- B. $3.200\pi\text{ cm}^2/\text{detik}$  
  <sub>Salah: Menggunakan nilai diameter $80\text{ cm}$ sebagai ganti jari-jari $40\text{ cm}$.</sub>
- C. $800\pi\text{ cm}^2/\text{detik}$  
  <sub>Salah: Lupa mengalikan turunan pangkat 2 pada rumus luas sehingga menggunakan $4\pi r \frac{dr}{dt}$.</sub>
- D. $1.600\text{ cm}^2/\text{detik}$  
  <sub>Salah: Lupa mengikutsertakan konstanta $\pi$ pada hasil akhir perhitungan.</sub>

**Pembahasan:** Rumus luas permukaan bola adalah $L(r) = 4\pi r^2$.
Berdasarkan aturan rantai turunan terhadap waktu $t$:
$$\frac{dL}{dt} = \frac{dL}{dr} \cdot \frac{dr}{dt} = 8\pi r \cdot \frac{dr}{dt}$$
Diketahui $r = 40\text{ cm}$ dan $\frac{dr}{dt} = 5\text{ cm/detik}$.
$$\frac{dL}{dt} = 8\pi(40)(5) = 1.600\pi\text{ cm}^2/\text{detik}$$
Jadi, laju bertambahnya luas permukaan bola adalah $1.600\pi\text{ cm}^2/\text{detik}$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b02-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: laju perubahan volume*

Jari-jari sebuah bola bertambah panjang dengan laju $4\text{ cm}$ per detik. Misalkan jari-jari bola tersebut $15\text{ cm}$. Tentukan laju bertambahnya volume bola.

- A. $3.600\text{ cm}^3/\text{detik}$  
  <sub>Salah: Lupa menuliskan konstanta $\pi$ pada hasil akhir.</sub>
- B. $900\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Hanya menghitung $\pi r^2 \frac{dr}{dt}$ dan melupakan faktor pengali 4.</sub>
- C. $1.200\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Keliru membagi hasil akhir dengan 3 karena mengira koefisien $\frac{4}{3}$ belum hilang saat menurunkan $r^3$.</sub>
- **D. $3.600\pi\text{ cm}^3/\text{detik}$** ✅  
  <sub>Benar: Volume bola dinyatakan dengan $V = \frac{4}{3}\pi r^3$. Laju perubahan volume terhadap waktu adalah $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$. Dengan mensubstitusi $r = 15$ dan $\frac{dr}{dt} = 4$, diperoleh $\frac{dV}{dt} = 4\pi (15)^2 (4) = 4\pi (225)(4) = 3.600\pi\text{ cm}^3/\text{detik}$.</sub>

**Pembahasan:** Rumus volume bola adalah $V(r) = \frac{4}{3}\pi r^3$.
Turunan volume terhadap waktu $t$ menggunakan aturan rantai:
$$\frac{dV}{dt} = \frac{dV}{dr} \cdot \frac{dr}{dt} = 4\pi r^2 \cdot \frac{dr}{dt}$$
Substitusikan $r = 15\text{ cm}$ dan $\frac{dr}{dt} = 4\text{ cm/detik}$:
$$\frac{dV}{dt} = 4\pi (15)^2 (4) = 4\pi (225)(4) = 3.600\pi\text{ cm}^3/\text{detik}$$
Jadi, laju bertambahnya volume bola adalah $3.600\pi\text{ cm}^3/\text{detik}$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b02-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: turunan fungsi aljabar irasional*

Tentukan turunan pertama dari fungsi $y = \sqrt{\dfrac{1}{(5x - 4)^7}}$.

- A. $y' = -\dfrac{35}{(5x - 4)^{9/2}}$  
  <sub>Salah: Lupa membagi dengan 2 dari penyebut pangkat pecahan $-\frac{7}{2}$.</sub>
- **B. $y' = -\dfrac{35}{2(5x - 4)^{9/2}}$** ✅  
  <sub>Benar: Fungsi dapat diubah menjadi $y = (5x - 4)^{-7/2}$. Menggunakan aturan rantai, $y' = -\frac{7}{2}(5x - 4)^{-9/2} \cdot \frac{d}{dx}(5x - 4) = -\frac{7}{2}(5x - 4)^{-9/2} \cdot 5 = -\frac{35}{2(5x - 4)^{9/2}}$.</sub>
- C. $y' = \dfrac{35}{2(5x - 4)^{9/2}}$  
  <sub>Salah: Salah tanda minus pada penurunan pangkat negatif.</sub>
- D. $y' = -\dfrac{7}{2(5x - 4)^{9/2}}$  
  <sub>Salah: Lupa mengalikan dengan turunan fungsi bagian dalam yaitu 5.</sub>

**Pembahasan:** Ubah bentuk fungsi ke bentuk eksponen:
$$y = \left((5x - 4)^{-7}\right)^{1/2} = (5x - 4)^{-7/2}$$
Terapkan aturan rantai turunan:
$$y' = -\frac{7}{2}(5x - 4)^{-\frac{7}{2} - 1} \cdot \frac{d}{dx}(5x - 4)$$
$$y' = -\frac{7}{2}(5x - 4)^{-9/2} \cdot 5 = -\frac{35}{2(5x - 4)^{9/2}}$$
Jadi, turunan pertamanya adalah $y' = -\dfrac{35}{2(5x - 4)^{9/2}}$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b02-b-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: titik stasioner fungsi eksponensial*

Diketahui fungsi $f(x) = e^{x^2 - 6x + 8}$. Nilai $x$ yang memenuhi $f'(x) = 0$ adalah ....

- A. $6$  
  <sub>Salah: Salah menyelesaikan persamaan linear $2x - 6 = 0$ menjadi $x = 6$.</sub>
- **B. $3$** ✅  
  <sub>Benar: Turunan fungsi adalah $f'(x) = (2x - 6)e^{x^2 - 6x + 8}$. Karena $e^{x^2 - 6x + 8} > 0$ untuk setiap $x \in \mathbb{R}$, maka $f'(x) = 0$ dipenuhi saat $2x - 6 = 0$, yaitu $x = 3$.</sub>
- C. $2$  
  <sub>Salah: Keliru mencari pembuat nol dari fungsi pangkat $x^2 - 6x + 8 = (x - 2)(x - 4) = 0$.</sub>
- D. $4$  
  <sub>Salah: Keliru mengambil akar pembuat nol lainnya dari fungsi pangkat eksponen.</sub>

**Pembahasan:** Diberikan $f(x) = e^{x^2 - 6x + 8}$.
Berdasarkan aturan turunan fungsi eksponensial $h(x) = e^{g(x)} \implies h'(x) = g'(x)e^{g(x)}$:
$$f'(x) = (2x - 6)e^{x^2 - 6x + 8}$$
Syarat $f'(x) = 0$:
$$(2x - 6)e^{x^2 - 6x + 8} = 0$$
Karena nilai $e^{x^2 - 6x + 8} \neq 0$ untuk seluruh $x$ bilangan real, maka:
$$2x - 6 = 0 \implies 2x = 6 \implies x = 3$$
Jadi, nilai $x$ yang memenuhi adalah $3$.
**Acuan:** siswa — siswa hal.140

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b02-b-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: laju perubahan volume bola*

Jari-jari sebuah bola bertambah panjang dengan laju $3\text{ cm}$ per detik. Misalkan jari-jari bola tersebut $20\text{ cm}$. Tentukan laju bertambahnya volume bola.

- A. $1.600\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa lupa mengalikan dengan laju pertambahan jari-jari $\frac{dr}{dt} = 3$.</sub>
- B. $14.400\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa tidak membagi dengan 3 saat menurunkan formula volume (turunan $r^3$ tidak dikalikan $\frac{4}{3}$, melainkan $4 \times 3$).</sub>
- C. $2.400\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa salah menggunakan rumus turunan volume menjadi $2\pi r^2 \frac{dr}{dt}$.</sub>
- **D. $4.800\pi\text{ cm}^3/\text{detik}$** ✅  
  <sub>Benar: Volume bola adalah $V = \frac{4}{3}\pi r^3$. Berdasarkan aturan rantai, $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$. Dengan $r = 20\text{ cm}$ dan $\frac{dr}{dt} = 3\text{ cm/detik}$, diperoleh $\frac{dV}{dt} = 4\pi (20)^2 (3) = 4\pi (400)(3) = 4.800\pi\text{ cm}^3/\text{detik}$.</sub>

**Pembahasan:** Rumus volume bola adalah $V = \frac{4}{3}\pi r^3$.
Turunan volume terhadap waktu dengan aturan rantai:
$$\frac{dV}{dt} = \frac{dV}{dr} \cdot \frac{dr}{dt} = 4\pi r^2 \frac{dr}{dt}$$
Substitusikan nilai $r = 20\text{ cm}$ dan $\frac{dr}{dt} = 3\text{ cm/detik}$:
$$\frac{dV}{dt} = 4\pi (20)^2 (3) = 4\pi (400)(3) = 4.800\pi\text{ cm}^3/\text{detik}$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b02-b-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: laju perubahan luas permukaan bola*

Jari-jari sebuah bola bertambah panjang dengan laju $6\text{ cm}$ per detik. Misalkan jari-jari bola tersebut $25\text{ cm}$. Tentukan laju bertambahnya luas permukaan bola.

- **A. $1.200\pi\text{ cm}^2/\text{detik}$** ✅  
  <sub>Benar: Luas permukaan bola $L = 4\pi r^2$. Laju perubahan luas terhadap waktu adalah $\frac{dL}{dt} = 8\pi r \frac{dr}{dt}$. Untuk $r = 25\text{ cm}$ dan $\frac{dr}{dt} = 6\text{ cm/detik}$, diperoleh $\frac{dL}{dt} = 8\pi(25)(6) = 1.200\pi\text{ cm}^2/\text{detik}$.</sub>
- B. $600\pi\text{ cm}^2/\text{detik}$  
  <sub>Salah: Siswa menurunkan luas bola menjadi $4\pi r \frac{dr}{dt}$ (koefisien 2 tidak dikalikan dengan 4).</sub>
- C. $2.400\pi\text{ cm}^2/\text{detik}$  
  <sub>Salah: Siswa salah mengalikan konstanta atau mengalikan dua kali turunan.</sub>
- D. $200\pi\text{ cm}^2/\text{detik}$  
  <sub>Salah: Siswa lupa mengalikan dengan laju perubahan $\frac{dr}{dt} = 6$.</sub>

**Pembahasan:** Rumus luas permukaan bola adalah $L = 4\pi r^2$.
Turunan luas terhadap waktu menggunakan aturan rantai:
$$\frac{dL}{dt} = 8\pi r \frac{dr}{dt}$$
Substitusikan $r = 25\text{ cm}$ dan $\frac{dr}{dt} = 6\text{ cm/detik}$:
$$\frac{dL}{dt} = 8\pi(25)(6) = 1.200\pi\text{ cm}^2/\text{detik}$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b02-b-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: turunan penyederhanaan trigonometri*

Tentukan turunan pertama dari fungsi $f(x) = \dfrac{\cos x}{1 + \sin x}$.

- A. $-\dfrac{1}{(1 + \sin x)^2}$  
  <sub>Salah: Siswa langsung mencoret $(1 + \sin x)$ di pembilang tanpa menyederhanakan pangkat penyebut dengan benar.</sub>
- B. $-\dfrac{\cos 2x}{(1 + \sin x)^2}$  
  <sub>Salah: Siswa salah mengoperasikan pembilang menjadi $-\sin x - \sin^2 x - \cos^2 x$ tanpa mengenali identitas $\sin^2 x + \cos^2 x = 1$.</sub>
- C. $\dfrac{1}{1 + \sin x}$  
  <sub>Salah: Siswa salah tanda negatif saat menurunkan $\cos x$ menjadi $\sin x$.</sub>
- **D. $-\dfrac{1}{1 + \sin x}$** ✅  
  <sub>Benar: Menggunakan aturan turunan hasil bagi $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ dengan $u = \cos x$ dan $v = 1 + \sin x$: $u' = -\sin x$, $v' = \cos x$. Maka pembilangnya adalah $-\sin x(1 + \sin x) - \cos x(\cos x) = -\sin x - (\sin^2 x + \cos^2 x) = -(\sin x + 1)$. Dibagi dengan $(1 + \sin x)^2$, diperoleh $-\frac{1}{1 + \sin x}$.</sub>

**Pembahasan:** Misalkan $u(x) = \cos x \implies u'(x) = -\sin x$ dan $v(x) = 1 + \sin x \implies v'(x) = \cos x$.
Berdasarkan aturan turunan hasil bagi:
$$f'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2}$$
$$f'(x) = \frac{-\sin x(1 + \sin x) - \cos x(\cos x)}{(1 + \sin x)^2}$$
$$f'(x) = \frac{-\sin x - \sin^2 x - \cos^2 x}{(1 + \sin x)^2}$$
$$f'(x) = \frac{-\sin x - (\sin^2 x + \cos^2 x)}{(1 + \sin x)^2}$$
Karena $\sin^2 x + \cos^2 x = 1$:
$$f'(x) = \frac{-\sin x - 1}{(1 + \sin x)^2} = \frac{-(1 + \sin x)}{(1 + \sin x)^2} = -\frac{1}{1 + \sin x}$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b02-b-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: aplikasi turunan eksponensial*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = t^2 e^{-t}$ untuk $t \ge 0$. Waktu $t > 0$ saat kecepatan partikel bernilai nol adalah ....

- **A. $t = 2$** ✅  
  <sub>Benar: Kecepatan merupakan turunan pertama dari fungsi posisi $v(t) = s'(t)$. Menggunakan aturan perkalian: $u = t^2 \implies u' = 2t$, $v = e^{-t} \implies v' = -e^{-t}$. Sehingga $v(t) = 2t e^{-t} - t^2 e^{-t} = t(2 - t)e^{-t}$. Karena $e^{-t} > 0$ untuk setiap nilai $t$ dan disyaratkan $t > 0$, maka $2 - t = 0 \implies t = 2$.</sub>
- B. $t = 4$  
  <sub>Salah: Siswa mengira turunan menghasilkan $t(4 - t)$ karena mengalikan pangkat dengan 2.</sub>
- C. $t = \frac{1}{2}$  
  <sub>Salah: Siswa salah menyamakan $2t - t^2 = 0$ menjadi pembagian $t = \frac{1}{2}$.</sub>
- D. $t = 1$  
  <sub>Salah: Siswa salah menurunkan $t^2$ menjadi $t$ sehingga menghasilkan $t(1 - t)e^{-t} = 0$.</sub>

**Pembahasan:** Kecepatan partikel adalah turunan pertama dari posisi:
$$v(t) = s'(t)$$
Misalkan $u(t) = t^2 \implies u'(t) = 2t$ dan $w(t) = e^{-t} \implies w'(t) = -e^{-t}$.
Menggunakan aturan perkalian:
$$s'(t) = u'(t)w(t) + u(t)w'(t)$$
$$s'(t) = 2t e^{-t} + t^2(-e^{-t}) = (2t - t^2)e^{-t} = t(2 - t)e^{-t}$$
Kecepatan sama dengan nol saat $s'(t) = 0$:
$$t(2 - t)e^{-t} = 0$$
Karena $e^{-t} > 0$ untuk semua bilangan real $t$, pembuat nolnya adalah $t = 0$ atau $2 - t = 0 \implies t = 2$.
Karena diminta waktu $t > 0$, maka nilai yang memenuhi adalah $t = 2$.
**Acuan:** siswa — siswa hal.139

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b02-b-medium-bt01-013
*variasi (angka) | C3 | 2 langkah | jenis: aturan rantai fungsi eksponensial akar*

Tentukan turunan pertama dari fungsi $y = e^{\sqrt{6x - 5}}$.

- **A. $y' = \dfrac{3e^{\sqrt{6x - 5}}}{\sqrt{6x - 5}}$** ✅  
  <sub>Benar: Dengan memisalkan $u = \sqrt{6x - 5} = (6x - 5)^{1/2}$, maka $u' = \frac{1}{2}(6x - 5)^{-1/2} \cdot 6 = \frac{3}{\sqrt{6x - 5}}$. Sehingga $y' = e^u \cdot u' = \frac{3e^{\sqrt{6x - 5}}}{\sqrt{6x - 5}}$.</sub>
- B. $y' = \dfrac{e^{\sqrt{6x - 5}}}{2\sqrt{6x - 5}}$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan fungsi dalam $(6x - 5)' = 6$.</sub>
- C. $y' = \dfrac{6e^{\sqrt{6x - 5}}}{\sqrt{6x - 5}}$  
  <sub>Salah: Siswa lupa mengalikan koefisien $\frac{1}{2}$ saat menurunkan bentuk akar.</sub>
- D. $y' = 3\sqrt{6x - 5}e^{\sqrt{6x - 5}}$  
  <sub>Salah: Siswa menempatkan suku turunan akar di pembilang bukan di penyebut.</sub>

**Pembahasan:** Misalkan $u = \sqrt{6x - 5}$.
Turunan $u$ terhadap $x$ adalah:
$$u' = \frac{1}{2\sqrt{6x - 5}} \cdot \frac{\mathrm{d}}{\mathrm{d}x}(6x - 5) = \frac{6}{2\sqrt{6x - 5}} = \frac{3}{\sqrt{6x - 5}}$$

Berdasarkan sifat turunan $y = e^{u(x)}$, diperoleh:
$$y' = e^{u(x)} \cdot u'(x) = e^{\sqrt{6x - 5}} \cdot \frac{3}{\sqrt{6x - 5}} = \frac{3e^{\sqrt{6x - 5}}}{\sqrt{6x - 5}}$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1e

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b02-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: nilai turunan fungsi trigonometri*

Diketahui fungsi $f(x) = (2x - 1)\tan x$. Nilai dari $f'(\pi)$ adalah ....

- A. $2\pi + 1$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada faktor aljabar $(2x - 1)$ menjadi $(2x + 1)$.</sub>
- B. $2$  
  <sub>Salah: Siswa mengabaikan suku kedua dan hanya menghitung $u'v = 2\tan(\pi)$ yang disalahartikan atau sebaliknya.</sub>
- **C. $2\pi - 1$** ✅  
  <sub>Benar: $f'(x) = 2\tan x + (2x - 1)\sec^2 x$. Untuk $x = \pi$, $\tan\pi = 0$ dan $\sec\pi = -1 \implies \sec^2\pi = 1$. Jadi $f'(\pi) = 2(0) + (2\pi - 1)(1) = 2\pi - 1$.</sub>
- D. $1 - 2\pi$  
  <sub>Salah: Siswa menganggap $\sec^2\pi = -1$ sehingga tanda suku berubah menjadi $-(2\pi - 1) = 1 - 2\pi$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan $f(x)$ menggunakan aturan perkalian $u \cdot v$:
Misalkan $u(x) = 2x - 1 \implies u'(x) = 2$
$v(x) = \tan x \implies v'(x) = \sec^2 x$

Maka:
$$f'(x) = u'(x)v(x) + u(x)v'(x) = 2\tan x + (2x - 1)\sec^2 x$$

Langkah 2: Menghitung nilai $f'(\pi)$:
Substitusi $x = \pi$:
$$\tan\pi = 0$$
$$\sec\pi = \frac{1}{\cos\pi} = \frac{1}{-1} = -1 \implies \sec^2\pi = (-1)^2 = 1$$

Langkah 3: Evaluasi hasil akhir:
$$f'(\pi) = 2(0) + (2\pi - 1)(1) = 2\pi - 1$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b02-b-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: garis singgung kurva eksponensial*

Gradien garis singgung kurva $f(x) = e^{2x^2 - 4x + 1}$ di titik yang berabsis $x = 2$ adalah ....

- A. $8e$  
  <sub>Salah: Siswa salah menurunkan $2x^2$ menjadi $4x$ lalu lupa mengurangi turunan $-4x$ sehingga menghitung $4(2)e = 8e$.</sub>
- **B. $4e$** ✅  
  <sub>Benar: $f'(x) = (4x - 4)e^{2x^2 - 4x + 1}$. Untuk $x = 2$, gradien $m = f'(2) = (4(2) - 4)e^{2(4) - 4(2) + 1} = 4e^1 = 4e$.</sub>
- C. $4$  
  <sub>Salah: Siswa hanya mengambil turunan pangkat $(4x - 4)$ saat $x = 2$ dan melupakan faktor eksponensialnya.</sub>
- D. $e$  
  <sub>Salah: Siswa hanya menghitung nilai fungsi $f(2)$ tanpa menurunkan fungsi.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama kurva $f(x)$ menggunakan aturan turunan $e^{u(x)}$:
Misalkan $u(x) = 2x^2 - 4x + 1$, sehingga $u'(x) = 4x - 4$.
$$f'(x) = u'(x)e^{u(x)} = (4x - 4)e^{2x^2 - 4x + 1}$$

Langkah 2: Menghitung nilai gradien $m = f'(2)$:
Substitusi $x = 2$:
$$m = f'(2) = (4(2) - 4)e^{2(2)^2 - 4(2) + 1}$$
$$m = (8 - 4)e^{8 - 8 + 1} = 4e^1 = 4e$$
**Acuan:** siswa — siswa hal.140

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b02-b-medium-bt01-016
*variasi (angka) | C3 | 2 langkah | jenis: turunan eksponensial aturan rantai*

Tentukan turunan pertama dari fungsi eksponensial $y = 6^{2x^3 - 5}$.

- **A. $y' = 6x^2 \cdot 6^{2x^3 - 5} \ln 6$** ✅  
  <sub>Benar: Turunan dari $a^{g(x)}$ adalah $g'(x) \cdot a^{g(x)} \ln a$. Dengan $g(x) = 2x^3 - 5$, maka $g'(x) = 6x^2$, sehingga $y' = 6x^2 \cdot 6^{2x^3 - 5} \ln 6$.</sub>
- B. $y' = 2x^2 \cdot 6^{2x^3 - 5} \ln 6$  
  <sub>Salah: Siswa salah menurunkan eksponen $2x^3 - 5$ menjadi $2x^2$, bukan $6x^2$.</sub>
- C. $y' = 6x^2 \cdot 6^{2x^3 - 5}$  
  <sub>Salah: Siswa lupa mengalikan dengan faktor $\ln a$ pada turunan fungsi eksponensial non-natural.</sub>
- D. $y' = (2x^3 - 5) \cdot 6^{2x^3 - 6} \ln 6$  
  <sub>Salah: Siswa keliru menerapkan aturan pangkat aljabar biasa pada fungsi eksponensial.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan dari fungsi pangkat $g(x) = 2x^3 - 5$.
$$g'(x) = 2(3x^2) = 6x^2$$

Langkah 2: Menggunakan aturan turunan eksponensial $y = a^{g(x)} \implies y' = g'(x) \cdot a^{g(x)} \ln a$.
$$y' = 6x^2 \cdot 6^{2x^3 - 5} \ln 6$$
**Acuan:** siswa — siswa hal.142 Ayo Mencoba 2.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b02-b-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: turunan perkalian fungsi trigonometri*

Tentukan turunan pertama dari fungsi trigonometri $y = 5\cos x \cot x$.

- A. $y' = 5\sin x \csc^2 x$  
  <sub>Salah: Siswa menurunkan fungsi secara terpisah tanpa menggunakan kaidah turunan hasil kali.</sub>
- **B. $y' = -5(\cos x + \cot x \csc x)$** ✅  
  <sub>Benar: Dengan aturan perkalian $(uv)' = u'v + uv'$, turunan dari $5\cos x \cot x$ adalah $5(-\sin x \cot x - \cos x \csc^2 x)$. Karena $\sin x \cot x = \cos x$ dan $\cos x \csc^2 x = \cot x \csc x$, maka hasilnya $-5(\cos x + \cot x \csc x)$.</sub>
- C. $y' = -5(\cos x - \cot x \csc x)$  
  <sub>Salah: Siswa salah mengingat turunan $\cot x$ sebagai $\csc^2 x$ positif.</sub>
- D. $y' = 5(\cos x - \cot x \csc x)$  
  <sub>Salah: Siswa salah mengingat turunan $\cos x$ sebagai $\sin x$ positif.</sub>

**Pembahasan:** Langkah 1: Misalkan $u(x) = \cos x$ dan $v(x) = \cot x$.
Turunannya masing-masing:
$$u'(x) = -\sin x$$
$$v'(x) = -\csc^2 x$$

Langkah 2: Gunakan aturan turunan perkalian $y' = 5(u'v + uv')$.
$$y' = 5\left[(-\sin x)(\cot x) + (\cos x)(-\csc^2 x)\right]$$
$$y' = -5\left(\sin x \cot x + \cos x \csc^2 x\right)$$

Langkah 3: Sederhanakan menggunakan identitas trigonometri:
$$\sin x \cot x = \sin x \cdot \frac{\cos x}{\sin x} = \cos x$$
$$\cos x \csc^2 x = \cos x \cdot \frac{1}{\sin^2 x} = \frac{\cos x}{\sin x} \cdot \frac{1}{\sin x} = \cot x \csc x$$
Diperoleh:
$$y' = -5(\cos x + \cot x \csc x)$$
**Acuan:** siswa — siswa hal.134 Contoh Soal 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b02-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: nilai turunan pembagian trigonometri*

Diketahui fungsi $f(x) = \dfrac{\cos x}{2 - \sin x}$. Nilai dari $f'(0)$ adalah ....

- A. $0$  
  <sub>Salah: Siswa langsung menurunkan pembilang menjadi $-\sin 0 = 0$ dan menyimpulkan nilai turunan sama dengan nol.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Siswa lupa mengkuadratkan penyebut pada rumus turunan hasil bagi sehingga membagi dengan $2$ bukan $4$.</sub>
- **C. $\frac{1}{4}$** ✅  
  <sub>Benar: Turunan pertama adalah $f'(x) = \frac{-\sin x(2 - \sin x) - \cos x(-\cos x)}{(2 - \sin x)^2} = \frac{1 - 2\sin x}{(2 - \sin x)^2}$. Substitusi $x = 0$ menghasilkan $f'(0) = \frac{1 - 0}{(2 - 0)^2} = \frac{1}{4}$.</sub>
- D. $-\frac{1}{4}$  
  <sub>Salah: Siswa tertukar tanda dalam rumus pembagian $(u'v + uv')$ bukan $(u'v - uv')$, sehingga pembilang menjadi $\sin^2 x - \cos^2 x - 2\sin x$, menghasilkan $-\frac{1}{4}$.</sub>

**Pembahasan:** Langkah 1: Menentukan komponen aturan hasil bagi $f(x) = \frac{u}{v}$.
$$u = \cos x \implies u' = -\sin x$$
$$v = 2 - \sin x \implies v' = -\cos x$$

Langkah 2: Menerapkan aturan hasil bagi $f'(x) = \frac{u'v - uv'}{v^2}$.
$$f'(x) = \frac{-\sin x(2 - \sin x) - \cos x(-\cos x)}{(2 - \sin x)^2}$$
$$f'(x) = \frac{-2\sin x + \sin^2 x + \cos^2 x}{(2 - \sin x)^2}$$
Karena $\sin^2 x + \cos^2 x = 1$, maka:
$$f'(x) = \frac{1 - 2\sin x}{(2 - \sin x)^2}$$

Langkah 3: Menghitung nilai $f'(0)$.
$$f'(0) = \frac{1 - 2\sin(0)}{(2 - \sin(0))^2} = \frac{1 - 0}{(2 - 0)^2} = \frac{1}{4}$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b02-b-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: turunan perkalian aljabar dan cosinus*

Tentukan turunan pertama dari fungsi $y = (8x^2 + 7)\cos x$.

- A. $y' = 16x\sin x + (8x^2 + 7)\cos x$  
  <sub>Salah: Tertukar memasangkan fungsi dan turunannya pada aturan perkalian.</sub>
- **B. $y' = 16x\cos x - (8x^2 + 7)\sin x$** ✅  
  <sub>Benar: Menggunakan aturan perkalian fungsi $y = u(x)v(x)$ dengan $u(x) = 8x^2 + 7$ dan $v(x) = \cos x$, maka $u'(x) = 16x$ dan $v'(x) = -\sin x$, sehingga $y' = u'v + uv' = 16x\cos x - (8x^2 + 7)\sin x$.</sub>
- C. $y' = -16x\sin x$  
  <sub>Salah: Mengalikan langsung turunan kedua faktor $u'(x) \cdot v'(x)$ tanpa menggunakan sifat turunan perkalian.</sub>
- D. $y' = 16x\cos x + (8x^2 + 7)\sin x$  
  <sub>Salah: Lupa tanda negatif saat menurunkan fungsi cosinus sehingga menganggap turunan $\cos x$ adalah $\sin x$.</sub>

**Pembahasan:** Misalkan fungsi dinyatakan sebagai perkalian dua fungsi $y = u(x)v(x)$, dengan:
- $u(x) = 8x^2 + 7 \implies u'(x) = 16x$
- $v(x) = \cos x \implies v'(x) = -\sin x$

Berdasarkan sifat turunan perkalian dua fungsi:
$$y' = u'(x)v(x) + u(x)v'(x)$$
$$y' = 16x(\cos x) + (8x^2 + 7)(-\sin x)$$
$$y' = 16x\cos x - (8x^2 + 7)\sin x$$

Jadi, turunan pertama fungsi tersebut adalah $y' = 16x\cos x - (8x^2 + 7)\sin x$.
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b02-b-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: nilai turunan fungsi trigonometri secan*

Diketahui fungsi $f(x) = \sec^2(2x)$. Nilai dari $f'\left(\dfrac{\pi}{8}\right)$ adalah ....

- A. 16  
  <sub>Salah: Keliru menentukan nilai $\sec(\pi/4) = 2$ sehingga menghasilkan $4(2^2)(1) = 16$.</sub>
- B. 2  
  <sub>Salah: Hanya menurunkan pangkat luar tanpa mengalikan turunan dari fungsi dalam $\sec(2x)$.</sub>
- C. 4  
  <sub>Salah: Lupa mengalikan dengan turunan fungsi dalam sudut $2x$.</sub>
- **D. 8** ✅  
  <sub>Benar: Menggunakan aturan rantai: $f'(x) = 2\sec(2x) \cdot \frac{d}{dx}(\sec(2x)) = 2\sec(2x) \cdot (2\sec(2x)\tan(2x)) = 4\sec^2(2x)\tan(2x)$. Untuk $x = \frac{\pi}{8}$, diperoleh $2x = \frac{\pi}{4}$. Maka $f'\left(\frac{\pi}{8}\right) = 4\sec^2\left(\frac{\pi}{4}\right)\tan\left(\frac{\pi}{4}\right) = 4(\sqrt{2})^2(1) = 8$.</sub>

**Pembahasan:** Berdasarkan aturan rantai, jika $f(x) = [\sec(2x)]^2$, maka:
$$\begin{aligned} f'(x) &= 2\sec(2x) \cdot \frac{d}{dx}(\sec(2x)) \\ &= 2\sec(2x) \cdot (\sec(2x)\tan(2x) \cdot 2) \\ &= 4\sec^2(2x)\tan(2x) \end{aligned}$$
Substitusikan $x = \dfrac{\pi}{8}$:
$$\begin{aligned} f'\left(\dfrac{\pi}{8}\right) &= 4\sec^2\left(2 \cdot \dfrac{\pi}{8}\right)\tan\left(2 \cdot \dfrac{\pi}{8}\right) \\ &= 4\sec^2\left(\dfrac{\pi}{4}\right)\tan\left(\dfrac{\pi}{4}\right) \\ &= 4(\sqrt{2})^2(1) \\ &= 4(2)(1) = 8 \end{aligned}$$
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b02-b-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: analisis pembuat nol turunan*

Diketahui persamaan fungsi trigonometri $f(x) = 6 - 8\sin\left(\frac{1}{6}\pi x\right)$ didefinisikan pada daerah asal $D_f = \{x \mid 0 \le x \le 12, x \in \mathbb{R}\}$. Jika $f'(x)$ bernilai nol pada $x = x_1$ dan $x = x_2$ dengan $x_1 < x_2$, tentukan nilai dari $x_1^2 + x_2^2$.

- **A. $90$** ✅  
  <sub>Benar: Turunan pertama adalah $f'(x) = -8\left(\frac{\pi}{6}\right)\cos\left(\frac{\pi x}{6}\right) = -\frac{4\pi}{3}\cos\left(\frac{\pi x}{6}\right)$. Pembuat nol terjadi ketika $\cos\left(\frac{\pi x}{6}\right) = 0$. Dalam interval $0 \le x \le 12$, nilai $\frac{\pi x}{6} \in [0, 2\pi]$, sehingga $\frac{\pi x}{6} = \frac{\pi}{2} \implies x_1 = 3$ dan $\frac{\pi x}{6} = \frac{3\pi}{2} \implies x_2 = 9$. Maka $x_1^2 + x_2^2 = 3^2 + 9^2 = 9 + 81 = 90$.</sub>
- B. $80$  
  <sub>Salah: Salah menyelesaikan persamaan kosinus nol menjadi $\frac{\pi x}{6} = \frac{\pi}{3}$ dan $\frac{5\pi}{3}$, menghasilkan $x_1 = 2$ dan $x_2 = 10$ sehingga $4 + 100 = 104$ lalu salah hitung menjadi $80$.</sub>
- C. $72$  
  <sub>Salah: Mengira pembuat nol terjadi saat sinus bernilai nol, yaitu pada $x_1 = 0$ dan $x_2 = 6$ atau $x = 6$ saja sehingga $6^2 + 6^2 = 72$.</sub>
- D. $144$  
  <sub>Salah: Menghitung $(x_1 + x_2)^2 = (3 + 9)^2 = 144$ alih-alih $x_1^2 + x_2^2$.</sub>

**Pembahasan:** Turunkan fungsi menggunakan aturan rantai:
$$f'(x) = -8 \cdot \frac{d}{dx}\left[\sin\left(\frac{\pi x}{6}\right)\right] = -8 \cdot \frac{\pi}{6}\cos\left(\frac{\pi x}{6}\right) = -\frac{4\pi}{3}\cos\left(\frac{\pi x}{6}\right)$$
Syarat $f'(x) = 0$:
$$-\frac{4\pi}{3}\cos\left(\frac{\pi x}{6}\right) = 0 \implies \cos\left(\frac{\pi x}{6}\right) = 0$$
Untuk $x \in [0, 12]$, sudut $\theta = \frac{\pi x}{6} \in [0, 2\pi]$:
$$\frac{\pi x}{6} = \frac{\pi}{2} \implies x_1 = 3$$
$$\frac{\pi x}{6} = \frac{3\pi}{2} \implies x_2 = 9$$
Hitung nilai yang diminta:
$$x_1^2 + x_2^2 = 3^2 + 9^2 = 9 + 81 = 90$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-3b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b02-b-hard-bt01-002
*variasi (konteks) | C5 | 5 langkah | jenis: kecepatan gerak partikel*

Sebuah partikel bergerak pada bidang datar sehingga posisinya pada saat $t$ detik dinyatakan oleh $(x(t), y(t))$ dengan $x(t) = 3t^2 - 5t$ dan $y(t) = 2t^3 - 9t^2 + 12t + 1$. Besar kecepatan partikel dinyatakan oleh $v(t) = \sqrt{[x'(t)]^2 + [y'(t)]^2}$. Tentukan besar kecepatan partikel pada saat laju perubahan vertikalnya bernilai nol ($y'(t) = 0$) untuk waktu $t > 1$.

- A. $\sqrt{17}$  
  <sub>Salah: Mensubstitusikan nilai $t = 2$ ke posisi $x(t)$ dan $y(t)$ alih-alih komponen kecepatan $x'(t)$.</sub>
- **B. $7$** ✅  
  <sub>Benar: Turunan posisi vertikal adalah $y'(t) = 6t^2 - 18t + 12$. Menyelesaikan $y'(t) = 0$ menghasilkan $6(t - 1)(t - 2) = 0$, sehingga $t = 1$ atau $t = 2$. Karena disyaratkan $t > 1$, dipilih $t = 2$. Turunan posisi horizontal adalah $x'(t) = 6t - 5$. Pada $t = 2$, diperoleh $x'(2) = 6(2) - 5 = 7$. Maka besar kecepatannya adalah $v(2) = \sqrt{7^2 + 0^2} = 7$.</sub>
- C. $1$  
  <sub>Salah: Memilih akar $t = 1$ yang melanggar batasan $t > 1$, sehingga menghitung $x'(1) = 6(1) - 5 = 1$.</sub>
- D. $5$  
  <sub>Salah: Salah menghitung turunan $x'(t)$ menjadi $6t - 7$ sehingga menghasilkan $6(2) - 7 = 5$.</sub>

**Pembahasan:** Langkah 1: Menentukan $y'(t)$ dan nilai pembuat nolnya:
$$y'(t) = \frac{d}{dt}(2t^3 - 9t^2 + 12t + 1) = 6t^2 - 18t + 12$$
$$6t^2 - 18t + 12 = 0 \implies t^2 - 3t + 2 = 0 \implies (t - 1)(t - 2) = 0$$
Diperoleh $t = 1$ atau $t = 2$. Syarat pada soal $t > 1$, maka waktu yang diambil adalah $t = 2$ detik.

Langkah 2: Menentukan $x'(t)$ pada $t = 2$:
$$x'(t) = \frac{d}{dt}(3t^2 - 5t) = 6t - 5$$
$$x'(2) = 6(2) - 5 = 7$$

Langkah 3: Menghitung besar kecepatan $v(2)$:
$$v(2) = \sqrt{[x'(2)]^2 + [y'(2)]^2} = \sqrt{7^2 + 0^2} = 7$$
**Acuan:** siswa — siswa hal.136 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b02-b-hard-bt01-003
*orisinal | C5 | 6 langkah | jenis: penyelesaian persamaan turunan trigonometri*

Diketahui fungsi $f(x) = \dfrac{\sin x - \cos x}{\sin x + \cos x}$ terdefinisi pada interval $0 < x < \pi$ dengan $x \ne \frac{3\pi}{4}$. Jika nilai turunan pertama fungsi tersebut memenuhi $f'(x) = 4$, tentukan jumlah seluruh nilai $x$ yang memenuhi persamaan tersebut.

- **A. $\dfrac{3\pi}{2}$** ✅  
  <sub>Benar: Dengan aturan pembagian, $f'(x) = \frac{(\cos x + \sin x)(\sin x + \cos x) - (\sin x - \cos x)(\cos x - \sin x)}{(\sin x + \cos x)^2} = \frac{(\sin x + \cos x)^2 + (\sin x - \cos x)^2}{(\sin x + \cos x)^2} = \frac{2(\sin^2 x + \cos^2 x)}{1 + 2\sin x \cos x} = \frac{2}{1 + \sin(2x)}$. Persamaan $f'(x) = 4$ menjadi $\frac{2}{1 + \sin(2x)} = 4 \implies 1 + \sin(2x) = \frac{1}{2} \implies \sin(2x) = -\frac{1}{2}$. Untuk $x \in (0, \pi)$, sudut $2x \in (0, 2\pi)$, sehingga $2x = \frac{7\pi}{6}$ atau $2x = \frac{11\pi}{6}$. Diperoleh $x_1 = \frac{7\pi}{12}$ dan $x_2 = \frac{11\pi}{12}$. Jumlahnya adalah $\frac{7\pi}{12} + \frac{11\pi}{12} = \frac{18\pi}{12} = \frac{3\pi}{2}$.</sub>
- B. $\dfrac{7\pi}{6}$  
  <sub>Salah: Lupa membagi nilai sudut rangkap $2x = \frac{7\pi}{6}$ dengan $2$ dan hanya mengambil satu nilai sudut.</sub>
- C. $\dfrac{5\pi}{4}$  
  <sub>Salah: Kesalahan menentukan sudut di kuadran III dan IV, mengira sudut penyelesaian adalah $\frac{5\pi}{4}$.</sub>
- D. $\pi$  
  <sub>Salah: Salah menyederhanakan turunan sehingga memperoleh $\sin(2x) = 0$ yang menghasilkan akar-akar dengan jumlah $\pi$.</sub>

**Pembahasan:** Langkah 1: Menurunkan $f(x)$ dengan aturan hasil bagi $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
Misalkan $u = \sin x - \cos x \implies u' = \cos x + \sin x$.
Misalkan $v = \sin x + \cos x \implies v' = \cos x - \sin x$.

Langkah 2: Menyederhanakan pembilang:
$$u'v - uv' = (\sin x + \cos x)^2 - (\sin x - \cos x)(\cos x - \sin x)$$
$$= (\sin x + \cos x)^2 + (\sin x - \cos x)^2$$
$$= (\sin^2 x + 2\sin x\cos x + \cos^2 x) + (\sin^2 x - 2\sin x\cos x + \cos^2 x) = 2$$

Langkah 3: Menyederhanakan penyebut:
$$v^2 = (\sin x + \cos x)^2 = \sin^2 x + \cos^2 x + 2\sin x\cos x = 1 + \sin(2x)$$
Diperoleh $f'(x) = \frac{2}{1 + \sin(2x)}$.

Langkah 4: Menyelesaikan persamaan $f'(x) = 4$:
$$\frac{2}{1 + \sin(2x)} = 4 \implies 1 + \sin(2x) = \frac{1}{2} \implies \sin(2x) = -\frac{1}{2}$$

Langkah 5: Mencari himpunan penyelesaian untuk $2x \in (0, 2\pi)$:
Nilai sinus negatif di kuadran III dan IV:
$$2x_1 = \pi + \frac{\pi}{6} = \frac{7\pi}{6} \implies x_1 = \frac{7\pi}{12}$$
$$2x_2 = 2\pi - \frac{\pi}{6} = \frac{11\pi}{6} \implies x_2 = \frac{11\pi}{12}$$
Kedua nilai memenuhi batasan $0 < x < \pi$ dan $x \ne \frac{3\pi}{4}$.

Langkah 6: Menjumlahkan kedua nilai $x$:
$$x_1 + x_2 = \frac{7\pi}{12} + \frac{11\pi}{12} = \frac{18\pi}{12} = \frac{3\pi}{2}$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b02-b-hard-bt01-004
*variasi (konteks) | C5 | 4 langkah | jenis: laju perubahan terkait*

Sebuah balon berbentuk bola dipompa sehingga jari-jarinya bertambah dengan laju konstan $1{,}5\text{ cm/detik}$. Pada saat luas permukaan balon tersebut mencapai $64\pi\text{ cm}^2$, laju pertambahan volume balon tersebut adalah ....

- A. $48\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa keliru menggunakan turunan volume terhadap jari-jari sebagai $2\pi r^2$ alih-alih $4\pi r^2$.</sub>
- **B. $96\pi\text{ cm}^3/\text{detik}$** ✅  
  <sub>Benar: Luas permukaan bola $L = 4\pi r^2 = 64\pi \implies r = 4\text{ cm}$. Volume bola $V = \frac{4}{3}\pi r^3$. Melalui aturan rantai, $\frac{dV}{dt} = \frac{dV}{dr} \cdot \frac{dr}{dt} = 4\pi r^2 \frac{dr}{dt} = 4\pi (4^2)(1{,}5) = 4\pi(16)(1{,}5) = 96\pi\text{ cm}^3/\text{detik}$.</sub>
- C. $64\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa lupa mengalikan luas permukaan dengan laju pertambahan jari-jari ($dr/dt$).</sub>
- D. $144\pi\text{ cm}^3/\text{detik}$  
  <sub>Salah: Siswa salah menentukan jari-jari dengan menganggap $4\pi r = 64\pi$ sehingga $r = 16$ atau salah mengalikan koefisien.</sub>

**Pembahasan:** Diketahui $\frac{dr}{dt} = 1{,}5\text{ cm/detik}$ dan $L = 64\pi\text{ cm}^2$.
1. Cari jari-jari $r$:
$$4\pi r^2 = 64\pi \implies r^2 = 16 \implies r = 4\text{ cm}$$
2. Tentukan laju perubahan volume $V = \frac{4}{3}\pi r^3$ terhadap waktu menggunakan aturan rantai:
$$\frac{dV}{dt} = \frac{dV}{dr} \cdot \frac{dr}{dt} = 4\pi r^2 \cdot \frac{dr}{dt}$$
$$\frac{dV}{dt} = 4\pi (4)^2 \cdot 1{,}5 = 64\pi \cdot 1{,}5 = 96\pi\text{ cm}^3/\text{detik}$$
**Acuan:** siswa — siswa hal.142 Latihan Soal Sifat-Sifat Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b02-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: analisis gradien garis singgung tegak lurus*

Diketahui kurva fungsi $f(x) = e^{2x} \sin(kx)$ dengan konstanta $k > 0$. Jika garis singgung kurva di titik $(0, f(0))$ tegak lurus dengan garis $x + 5y - 10 = 0$, maka nilai dari $k$ adalah ....

- A. $3$  
  <sub>Salah: Siswa salah menurunkan $f'(0)$ dengan mengabaikan turunan perkalian sehingga $f'(0) = k - 2 = 5 \implies k = 7$ atau keliru menjumlahkan suku.</sub>
- **B. $5$** ✅  
  <sub>Benar: Garis $x + 5y - 10 = 0$ memiliki gradien $m_1 = -\frac{1}{5}$. Garis singgung tegak lurus sehingga $m_2 = -\frac{1}{m_1} = 5$. Turunan pertama $f'(x) = 2e^{2x}\sin(kx) + ke^{2x}\cos(kx)$. Di $x = 0$, $f'(0) = 2(1)(0) + k(1)(1) = k$. Maka $k = 5$.</sub>
- C. $-5$  
  <sub>Salah: Siswa menggunakan relasi gradien sejajar $m_2 = m_1$ atau salah menerapkan tanda saling tegak lurus.</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: Siswa membalik tanda gradien tanpa menegatifkannya ($m_2 = -1/m_1$ terbalik).</sub>

**Pembahasan:** 1. Cari gradien garis singgung $m$:
Garis $x + 5y - 10 = 0 \iff y = -\frac{1}{5}x + 2$ mempunyai gradien $m_1 = -\frac{1}{5}$.
Karena tegak lurus, maka $m \cdot m_1 = -1 \implies m = 5$.

2. Tentukan turunan $f(x)$ menggunakan aturan perkalian dan rantai:
$$f'(x) = \frac{d}{dx}[e^{2x}]\sin(kx) + e^{2x}\frac{d}{dx}[\sin(kx)]$$
$$f'(x) = 2e^{2x}\sin(kx) + ke^{2x}\cos(kx)$$

3. Substitusi $x = 0$:
$$f'(0) = 2e^0\sin(0) + ke^0\cos(0) = 0 + k(1)(1) = k$$

4. Samakan dengan nilai gradien:
$$k = m = 5$$
**Acuan:** siswa — siswa hal.140

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b02-b-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: analisis jumlah pembuat nol turunan*

Diketahui fungsi $f(x) = \dfrac{\sin x - \cos x}{e^x}$ terdefinisi pada interval tertutup $[0, 2\pi]$. Jumlah seluruh nilai $x$ yang memenuhi $f'(x) = 0$ pada interval tersebut adalah ....

- **A. $2\pi$** ✅  
  <sub>Benar: Turunan $f'(x) = \frac{(\cos x + \sin x)e^x - (\sin x - \cos x)e^x}{e^{2x}} = \frac{2\cos x}{e^x}$. $f'(x) = 0 \iff 2\cos x = 0 \iff \cos x = 0$. Pada $[0, 2\pi]$, nilai $x$ adalah $\frac{\pi}{2}$ dan $\frac{3\pi}{2}$. Jumlahnya $\frac{\pi}{2} + \frac{3\pi}{2} = 2\pi$.</sub>
- B. $3\pi$  
  <sub>Salah: Siswa salah menurunkan $u'$ menjadi $\cos x - \sin x$ sehingga menghasilkan $\sin x = 0$ dengan penyelesaian $0 + \pi + 2\pi = 3\pi$.</sub>
- C. $\pi$  
  <sub>Salah: Siswa keliru mengira hanya ada satu solusi yaitu $\pi$ atau salah menurunkan suku pembilang.</sub>
- D. $\frac{3\pi}{2}$  
  <sub>Salah: Siswa hanya mengambil solusi terbesar dalam interval.</sub>

**Pembahasan:** Gunakan aturan pembagian $f'(x) = \dfrac{u'v - uv'}{v^2}$:
1. Misalkan:
$u(x) = \sin x - \cos x \implies u'(x) = \cos x - (-\sin x) = \cos x + \sin x$
$v(x) = e^x \implies v'(x) = e^x$

2. Hitung $f'(x)$:
$$f'(x) = \frac{(\cos x + \sin x)e^x - (\sin x - \cos x)e^x}{(e^x)^2}$$
$$f'(x) = \frac{e^x[(\cos x + \sin x) - (\sin x - \cos x)]}{e^{2x}} = \frac{2\cos x}{e^x}$$

3. Tentukan pembuat nol $f'(x) = 0$:
$$\frac{2\cos x}{e^x} = 0 \implies 2\cos x = 0 \implies \cos x = 0$$

4. Pada interval $[0, 2\pi]$, nilai $x$ yang memenuhi adalah:
$$x_1 = \frac{\pi}{2}, \quad x_2 = \frac{3\pi}{2}$$

5. Jumlah seluruh nilai $x$:
$$x_1 + x_2 = \frac{\pi}{2} + \frac{3\pi}{2} = 2\pi$$
**Acuan:** siswa — siswa hal.134

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b02-b-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: jumlah ordinat titik stasioner*

Diketahui kurva fungsi $f(x) = x^2 e^{-x}$ memiliki dua titik stasioner $(x_1, y_1)$ dan $(x_2, y_2)$ dengan $x_1 < x_2$. Nilai dari $y_1 + y_2$ adalah ....

- A. $\dfrac{2}{e^2}$  
  <sub>Salah: Siswa salah memasukkan $x_2 = 2$ ke dalam fungsi menjadi $2e^{-2}$ bukannya $2^2 e^{-2}$.</sub>
- B. $2$  
  <sub>Salah: Siswa menjumlahkan absis $x_1 + x_2 = 0 + 2 = 2$ bukan ordinatnya.</sub>
- C. $\dfrac{4}{e}$  
  <sub>Salah: Siswa salah mensubstitusi eksponen menjadi $e^{-1}$ alih-alih $e^{-2}$.</sub>
- **D. $\dfrac{4}{e^2}$** ✅  
  <sub>Benar: Turunan $f'(x) = 2x e^{-x} - x^2 e^{-x} = x(2 - x)e^{-x}$. Syarat stasioner $f'(x) = 0 \implies x_1 = 0$ dan $x_2 = 2$. Ordinatnya $y_1 = f(0) = 0$ dan $y_2 = f(2) = 4e^{-2} = \frac{4}{e^2}$. Maka $y_1 + y_2 = \frac{4}{e^2}$.</sub>

**Pembahasan:** 1. Tentukan turunan $f'(x)$ menggunakan aturan perkalian dan rantai:
$$f'(x) = 2x \cdot e^{-x} + x^2 \cdot (-e^{-x}) = (2x - x^2)e^{-x} = x(2 - x)e^{-x}$$

2. Titik stasioner terjadi saat $f'(x) = 0$:
$$x(2 - x)e^{-x} = 0$$
Karena $e^{-x} > 0$ untuk setiap bilangan real $x$, maka:
$$x(2 - x) = 0 \implies x_1 = 0 \text{ atau } x_2 = 2$$

3. Hitung ordinat masing-masing titik:
$$y_1 = f(0) = 0^2 \cdot e^0 = 0$$
$$y_2 = f(2) = 2^2 \cdot e^{-2} = \frac{4}{e^2}$$

4. Hitung jumlah ordinat:
$$y_1 + y_2 = 0 + \frac{4}{e^2} = \frac{4}{e^2}$$
**Acuan:** siswa — siswa hal.139

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b02-b-hard-bt01-008
*orisinal | C6 | 6 langkah | jenis: penentuan parameter fungsi trigonometri*

Diketahui fungsi $f(x) = \dfrac{a\sin x + b}{\cos x}$ dengan konstanta real $a$ dan $b$. Jika $f\left(\frac{\pi}{3}\right) = 2\sqrt{3}$ dan $f'\left(\frac{\pi}{3}\right) = 8$, tentukan nilai dari $a^2 + b^2$.

- A. $12$  
  <sub>Salah: Siswa salah mengkuadratkan $2\sqrt{3}$ alih-alih nilai masing-masing konstanta.</sub>
- B. $2$  
  <sub>Salah: Siswa hanya menjumlahkan $a + b = 2 + 0 = 2$ tanpa menguadratkannya.</sub>
- **C. $4$** ✅  
  <sub>Benar: Dari $f(\pi/3)$, diperoleh $\frac{a\sqrt{3}/2 + b}{1/2} = a\sqrt{3} + 2b = 2\sqrt{3}$. Dari turunan $f'(x) = \frac{a + b\sin x}{\cos^2 x}$, diperoleh $\frac{a + b\sqrt{3}/2}{1/4} = 4a + 2\sqrt{3}b = 8 \implies 2a + \sqrt{3}b = 4$. Eliminasi kedua persamaan menghasilkan $a = 2$ dan $b = 0$, sehingga $a^2 + b^2 = 2^2 + 0^2 = 4$.</sub>
- D. $8$  
  <sub>Salah: Siswa salah menghitung dan mendapatkan $a = 2, b = 2$ sehingga $a^2 + b^2 = 8$.</sub>

**Pembahasan:** 1. Evaluasi persamaan dari $f\left(\frac{\pi}{3}\right) = 2\sqrt{3}$:
$$f\left(\frac{\pi}{3}\right) = \frac{a\sin(\pi/3) + b}{\cos(\pi/3)} = \frac{a\left(\frac{\sqrt{3}}{2}\right) + b}{\frac{1}{2}} = a\sqrt{3} + 2b = 2\sqrt{3} \quad \text{...(1)}$$

2. Tentukan turunan $f'(x)$ menggunakan sifat pembagian:
$$u = a\sin x + b \implies u' = a\cos x$$
$$v = \cos x \implies v' = -\sin x$$
$$f'(x) = \frac{a\cos^2 x - (a\sin x + b)(-\sin x)}{\cos^2 x} = \frac{a(\cos^2 x + \sin^2 x) + b\sin x}{\cos^2 x} = \frac{a + b\sin x}{\cos^2 x}$$

3. Evaluasi $f'\left(\frac{\pi}{3}\right) = 8$:
$$f'\left(\frac{\pi}{3}\right) = \frac{a + b\left(\frac{\sqrt{3}}{2}\right)}{\left(\frac{1}{2}\right)^2} = \frac{a + \frac{\sqrt{3}}{2}b}{\frac{1}{4}} = 4a + 2\sqrt{3}b = 8$$
Bagi kedua ruas dengan 2:
$$2a + \sqrt{3}b = 4 \quad \text{...(2)}$$

4. Selesaikan sistem persamaan (1) dan (2):
Dari (1): $2b = \sqrt{3}(2 - a) \implies b = \frac{\sqrt{3}(2 - a)}{2}$.
Substitusikan ke (2):
$$2a + \sqrt{3}\left(\frac{\sqrt{3}(2 - a)}{2}\right) = 4$$
$$2a + \frac{3(2 - a)}{2} = 4 \iff 4a + 6 - 3a = 8 \iff a = 2$$
Maka $b = \frac{\sqrt{3}(2 - 2)}{2} = 0$.

5. Hitung $a^2 + b^2$:
$$a^2 + b^2 = 2^2 + 0^2 = 4$$
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b02-b-hard-bt01-009
*variasi (angka) | C5 | 4 langkah | jenis: analisis pembuat nol turunan trigonometri*

Diketahui persamaan fungsi trigonometri $f(x) = 9 - 8\sin\left(\frac{1}{8}\pi x\right)$ didefinisikan pada daerah asal $D_f = \{x \mid 0 \le x \le 16, x \in \mathbb{R}\}$. Jika $f'(x)$ bernilai nol pada $x = x_1$ dan $x = x_2$ dengan $x_1 < x_2$, tentukan nilai dari $x_1^2 + x_2^2$.

- A. 208  
  <sub>Salah: Keliru menganggap pembuat nol terjadi saat $\sin\left(\frac{\pi x}{8}\right) = 0$ tanpa menurunkan fungsi terlebih dahulu.</sub>
- **B. 160** ✅  
  <sub>Benar: Turunan pertama adalah $f'(x) = -8 \cdot \frac{\pi}{8} \cos\left(\frac{\pi x}{8}\right) = -\pi \cos\left(\frac{\pi x}{8}\right)$. Syarat $f'(x) = 0$ menghasilkan $\cos\left(\frac{\pi x}{8}\right) = 0$. Pada interval $0 \le x \le 16$, nilai $\frac{\pi x}{8}$ berada pada $[0, 2\pi]$, sehingga sudut yang memenuhi adalah $\frac{\pi}{2}$ dan $\frac{3\pi}{2}$. Diperoleh $x_1 = 4$ dan $x_2 = 12$. Maka $x_1^2 + x_2^2 = 4^2 + 12^2 = 16 + 144 = 160$.</sub>
- C. 128  
  <sub>Salah: Keliru mengambil solusi $\frac{\pi x}{8} = \frac{\pi}{4}$ dan $\frac{7\pi}{4}$ sehingga menghasilkan $x_1 = 2$ dan $x_2 = 14$, menghasilkan $4 + 196 = 200$, atau salah hitung kuadrat.</sub>
- D. 80  
  <sub>Salah: Hanya menghitung salah satu kuadrat lalu dikalikan dua atau salah mengambil pembuat nol sinus bukan kosinus.</sub>

**Pembahasan:** Turunan fungsi $f(x)$ diperoleh menggunakan turunan fungsi konstan dan turunan sinus dengan aturan rantai:
$$f'(x) = 0 - 8 \cdot \cos\left(\frac{1}{8}\pi x\right) \cdot \frac{1}{8}\pi = -\pi \cos\left(\frac{\pi x}{8}\right)$$
Agar $f'(x) = 0$, maka:
$$-\pi \cos\left(\frac{\pi x}{8}\right) = 0 \iff \cos\left(\frac{\pi x}{8}\right) = 0$$
Karena $0 \le x \le 16$, maka rentang argumen adalah $0 \le \frac{\pi x}{8} \le 2\pi$. Nilai argumen yang membuat kosinus bernilai nol pada rentang tersebut adalah:
$$\frac{\pi x_1}{8} = \frac{\pi}{2} \implies x_1 = 4$$
$$\frac{\pi x_2}{8} = \frac{3\pi}{2} \implies x_2 = 12$$
Dengan demikian, nilai dari $x_1^2 + x_2^2$ adalah:
$$x_1^2 + x_2^2 = 4^2 + 12^2 = 16 + 144 = 160$$
**Acuan:** pretest — kelas12_tl-b02-p0142-latihan-soal-sifat-sifat-turunan-fungsi-3b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b02-b-hard-bt01-010
*variasi (angka) | C5 | 4 langkah | jenis: kecepatan gerak partikel parametrik*

Sebuah objek bergerak pada bidang Kartesius dengan posisi $(x(t), y(t))$ pada saat $t$ detik memenuhi persamaan $x(t) = 2t^2 - 2t + 1$ dan $y(t) = t^3 - t^2$. Kecepatan objek dirumuskan sebagai laju perubahan posisi $v(t) = \sqrt{(x'(t))^2 + (y'(t))^2}$. Tentukan besar kecepatan objek tersebut pada saat $t = 2$ detik.

- A. 14  
  <sub>Salah: Menjumlahkan langsung komponen kecepatan $x'(2) + y'(2) = 6 + 8 = 14$ tanpa menghitung resultan vektor.</sub>
- B. 2\sqrt{7}  
  <sub>Salah: Salah memasukkan tanda operasi pada turunan $x'(t)$ atau $y'(t)$ sehingga menghasilkan perhitungan kuadrat yang salah.</sub>
- **C. 10** ✅  
  <sub>Benar: $x'(t) = 4t - 2 \implies x'(2) = 6$. $y'(t) = 3t^2 - 2t \implies y'(2) = 12 - 4 = 8$. Maka $v(2) = \sqrt{6^2 + 8^2} = 10$.</sub>
- D. 8  
  <sub>Salah: Hanya mengambil komponen kecepatan vertikal $y'(2)$.</sub>

**Pembahasan:** Komponen kecepatan horizontal ditentukan oleh turunan $x(t)$ terhadap $t$:
$$x'(t) = \frac{d}{dt}(2t^2 - 2t + 1) = 4t - 2$$
Pada $t = 2$:
$$x'(2) = 4(2) - 2 = 6$$
Komponen kecepatan vertikal ditentukan oleh turunan $y(t)$ terhadap $t$:
$$y'(t) = \frac{d}{dt}(t^3 - t^2) = 3t^2 - 2t$$
Pada $t = 2$:
$$y'(2) = 3(2)^2 - 2(2) = 12 - 4 = 8$$
Besar kecepatan pada saat $t = 2$ detik adalah:
$$v(2) = \sqrt{(x'(2))^2 + (y'(2))^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$$
**Acuan:** siswa — siswa hal.136 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b02-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: analisis parameter titik stasioner eksponensial*

Diketahui fungsi $f(x) = e^{2x}(x^2 + ax + b)$ dengan $a$ dan $b$ adalah konstanta real. Kurva $y = f(x)$ memiliki titik stasioner di $x = 0$ dan $x = 1$. Nilai dari $a + b$ adalah ....

- A. 1  
  <sub>Salah: Kesalahan tanda saat menyelesaikan sistem persamaan linier sehingga mendapatkan $a = 2$ dan $b = -1$.</sub>
- B. 0  
  <sub>Salah: Keliru mengasumsikan $a = b$ langsung dari syarat titik stasioner di nol.</sub>
- C. -3  
  <sub>Salah: Lupa mengalikan turunan dari pangkat eksponen ($2$) pada suku pertama aturan perkalian.</sub>
- **D. -1** ✅  
  <sub>Benar: $f'(x) = 2e^{2x}(x^2 + ax + b) + e^{2x}(2x + a) = e^{2x}(2x^2 + (2a + 2)x + 2b + a)$. Titik stasioner di $x = 0 \implies 2b + a = 0$. Titik stasioner di $x = 1 \implies 2 + 2a + 2 + 2b + a = 0 \implies 3a + 2b + 4 = 0$. Substitusi $2b = -a$ menghasilkan $2a + 4 = 0 \implies a = -2$, sehingga $b = 1$. Maka $a + b = -2 + 1 = -1$.</sub>

**Pembahasan:** Gunakan aturan perkalian turunan $y = u \cdot v$ dengan $u = e^{2x}$ dan $v = x^2 + ax + b$:
$$u'(x) = 2e^{2x}$$
$$v'(x) = 2x + a$$
Maka turunan pertama $f'(x)$ adalah:
$$f'(x) = 2e^{2x}(x^2 + ax + b) + e^{2x}(2x + a) = e^{2x}(2x^2 + (2a + 2)x + 2b + a)$$
Karena kurva memiliki titik stasioner di $x = 0$ dan $x = 1$, maka $f'(0) = 0$ dan $f'(1) = 0$.
Untuk $x = 0$ (ingat $e^0 = 1$):
$$f'(0) = 1 \cdot (2(0)^2 + (2a + 2)(0) + 2b + a) = 0 \implies 2b + a = 0 \implies a = -2b$$
Untuk $x = 1$ (karena $e^2 \ne 0$):
$$2(1)^2 + (2a + 2)(1) + 2b + a = 0 \implies 2 + 2a + 2 + 2b + a = 0 \implies 3a + 2b + 4 = 0$$
Substitusikan $a = -2b$ ke dalam persamaan kedua:
$$3(-2b) + 2b + 4 = 0 \implies -4b + 4 = 0 \implies b = 1$$
Diperoleh $a = -2(1) = -2$.
Nilai $a + b$ adalah:
$$a + b = -2 + 1 = -1$$
**Acuan:** siswa — siswa hal.140

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b02-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: analisis parameter garis singgung trigonometri*

Diketahui fungsi $f(x) = \dfrac{\sin x}{p + \cos x}$ dengan parameter $p > 0$. Jika garis singgung kurva $y = f(x)$ pada absis $x = \frac{\pi}{2}$ memiliki gradien $\frac{1}{4}$, tentukan nilai dari $f\left(\frac{\pi}{3}\right)$.

- **A. \frac{\sqrt{3}}{5}** ✅  
  <sub>Benar: Turunan $f'(x) = \frac{\cos x(p + \cos x) - \sin x(-\sin x)}{(p + \cos x)^2} = \frac{p\cos x + 1}{(p + \cos x)^2}$. Pada $x = \frac{\pi}{2}$, $f'\left(\frac{\pi}{2}\right) = \frac{1}{p^2} = \frac{1}{4} \implies p = 2$ (karena $p > 0$). Maka $f\left(\frac{\pi}{3}\right) = \frac{\sin(\pi/3)}{2 + \cos(\pi/3)} = \frac{\frac{1}{2}\sqrt{3}}{2 + \frac{1}{2}} = \frac{\sqrt{3}}{5}$.</sub>
- B. \frac{\sqrt{3}}{4}  
  <sub>Salah: Lupa menambahkan nilai $\cos(\pi/3)$ pada penyebut fungsi $f(x)$.</sub>
- C. \frac{\sqrt{3}}{3}  
  <sub>Salah: Salah menentukan nilai $p$ menjadi $p = 1$ akibat lupa mengkuadratkan penyebut pada turunan pembagian.</sub>
- D. \frac{1}{5}  
  <sub>Salah: Tertukar antara $\sin(\pi/3)$ dan $\cos(\pi/3)$ pada pembilang.</sub>

**Pembahasan:** Gunakan aturan turunan fungsi pecahan $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$ dengan $u = \sin x$ dan $v = p + \cos x$:
$$u'(x) = \cos x$$
$$v'(x) = -\sin x$$
Maka:
$$f'(x) = \frac{\cos x(p + \cos x) - \sin x(-\sin x)}{(p + \cos x)^2} = \frac{p\cos x + \cos^2 x + \sin^2 x}{(p + \cos x)^2}$$
Dengan identitas trigonometri $\cos^2 x + \sin^2 x = 1$:
$$f'(x) = \frac{p\cos x + 1}{(p + \cos x)^2}$$
Diketahui gradien di $x = \frac{\pi}{2}$ adalah $\frac{1}{4}$:
$$f'\left(\frac{\pi}{2}\right) = \frac{p\cos(\pi/2) + 1}{(p + \cos(\pi/2))^2} = \frac{p(0) + 1}{(p + 0)^2} = \frac{1}{p^2}$$
$$\frac{1}{p^2} = \frac{1}{4} \implies p^2 = 4$$
Karena $p > 0$, maka $p = 2$.
Fungsi menjadi $f(x) = \dfrac{\sin x}{2 + \cos x}$. Nilai fungsi pada $x = \frac{\pi}{3}$ adalah:
$$f\left(\frac{\pi}{3}\right) = \frac{\sin(\pi/3)}{2 + \cos(\pi/3)} = \frac{\frac{1}{2}\sqrt{3}}{2 + \frac{1}{2}} = \frac{\frac{1}{2}\sqrt{3}}{\frac{5}{2}} = \frac{\sqrt{3}}{5}$$
**Acuan:** siswa — siswa hal.135

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b02-b-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: analisis parameter kurva berpangkat*

Kurva suatu fungsi didefinisikan sebagai $y = (ax^2 + bx - 1)^3$. Garis singgung kurva di titik berabsis $x = 1$ sejajar dengan sumbu-$X$. Jika kurva tersebut melalui titik $(1, 8)$, tentukan nilai dari $b - a$.

- A. 5  
  <sub>Salah: Lupa menurunkan bagian dalam kurung $(2ax + b)$ sehingga persamaan kedua keliru.</sub>
- B. 3  
  <sub>Salah: Keliru menghitung $a + b$ dan mengiranya sebagai nilai $b - a$.</sub>
- C. -9  
  <sub>Salah: Terbalik menghitung $a - b = -3 - 6 = -9$.</sub>
- **D. 9** ✅  
  <sub>Benar: Kurva melalui $(1, 8) \implies (a(1)^2 + b(1) - 1)^3 = 8 \implies a + b - 1 = 2 \implies a + b = 3$. Garis singgung sejajar sumbu-$X$ di $x = 1 \implies y'(1) = 0$. Turunan $y' = 3(ax^2 + bx - 1)^2 (2ax + b)$. Di $x = 1$, $y'(1) = 3(2)^2 (2a + b) = 12(2a + b) = 0 \implies 2a + b = 0$. Dari sistem $a + b = 3$ dan $2a + b = 0$, diperoleh $a = -3$ dan $b = 6$. Maka $b - a = 6 - (-3) = 9$.</sub>

**Pembahasan:** Kurva melalui titik $(1, 8)$, sehingga substitusi $x = 1$ dan $y = 8$ memberikan:
$$(a(1)^2 + b(1) - 1)^3 = 8$$
$$a + b - 1 = \sqrt[3]{8} = 2 \implies a + b = 3 \quad \text{...(Persamaan 1)}$$
Turunan pertama $y$ terhadap $x$ dicari dengan aturan rantai:
$$y' = 3(ax^2 + bx - 1)^2 \cdot \frac{d}{dx}(ax^2 + bx - 1) = 3(ax^2 + bx - 1)^2 (2ax + b)$$
Karena garis singgung pada $x = 1$ sejajar sumbu-$X$, maka gradiennya nol ($y'(1) = 0$):
$$y'(1) = 3(a(1)^2 + b(1) - 1)^2 (2a(1) + b) = 0$$
$$3(2)^2 (2a + b) = 0 \implies 12(2a + b) = 0 \implies 2a + b = 0 \quad \text{...(Persamaan 2)}$$
Eliminasi Persamaan 1 dan Persamaan 2:
$$(2a + b) - (a + b) = 0 - 3 \implies a = -3$$
Substitusikan nilai $a = -3$ ke Persamaan 1:
$$-3 + b = 3 \implies b = 6$$
Dengan demikian, nilai dari $b - a$ adalah:
$$b - a = 6 - (-3) = 9$$
**Acuan:** siswa — siswa hal.126

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b02-b-hard-bt01-014
*variasi (angka) | C5 | 5 langkah | jenis: laju perubahan terkait laju volume terhadap luas*

Sebuah balon udara berbentuk bola ditiup sehingga jari-jarinya bertambah dengan laju tetap $0{,}5\text{ cm/detik}$. Pada saat jari-jari bola mencapai $10\text{ cm}$, rasio laju pertambahan volume terhadap laju pertambahan luas permukaan balon tersebut adalah ....

- A. $10\text{ cm}$  
  <sub>Salah: Siswa lupa membagi dengan faktor 2 dari turunan luas permukaan terhadap jari-jari.</sub>
- B. $20\text{ cm}$  
  <sub>Salah: Siswa membalik rumus rasio sehingga menjadi $\frac{2}{r}$ lalu dikalikan kuadrat jari-jari.</sub>
- C. $2{,}5\text{ cm}$  
  <sub>Salah: Siswa mengalikan lagi dengan nilai laju $\frac{dr}{dt} = 0{,}5$ pada hasil akhir rasio.</sub>
- **D. $5\text{ cm}$** ✅  
  <sub>Benar: $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$ dan $\frac{dL}{dt} = 8\pi r \frac{dr}{dt}$, sehingga $\frac{dV/dt}{dL/dt} = \frac{4\pi r^2}{8\pi r} = \frac{r}{2} = \frac{10}{2} = 5\text{ cm}$.</sub>

**Pembahasan:** Diketahui laju pertambahan jari-jari $\frac{dr}{dt} = 0{,}5\text{ cm/detik}$ saat $r = 10\text{ cm}$.
Volume bola: $V = \frac{4}{3}\pi r^3 \implies \frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}$.
Luas permukaan bola: $L = 4\pi r^2 \implies \frac{dL}{dt} = 8\pi r \frac{dr}{dt}$.
Rasio laju pertambahan volume terhadap laju pertambahan luas permukaan adalah:
$$\frac{\frac{dV}{dt}}{\frac{dL}{dt}} = \frac{4\pi r^2 \frac{dr}{dt}}{8\pi r \frac{dr}{dt}} = \frac{r}{2}$$
Substitusi $r = 10\text{ cm}$ menghasilkan $\frac{10}{2} = 5\text{ cm}$.
**Acuan:** siswa — siswa hal.142 Latihan Soal Sifat-Sifat Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b02-b-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: evaluasi turunan fungsi komposisi trigonometri*

Diketahui fungsi $f(x) = \cos^4(2x) - \sin^4(2x)$. Jika turunan pertama $f'(x) = k \sin(4x)$, maka nilai dari konstanta real $k$ adalah ....

- A. $-2$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan sudut $4x$ yaitu 4, hanya memperhitungkan 2.</sub>
- B. $-8$  
  <sub>Salah: Siswa menurunkan tiap suku secara terpisah dan salah mengalikan faktor turunan rantai secara berlebih.</sub>
- **C. $-4$** ✅  
  <sub>Benar: $f(x) = \cos(4x)$, sehingga $f'(x) = -4\sin(4x)$, diperoleh $k = -4$.</sub>
- D. $4$  
  <sub>Salah: Siswa lupa tanda negatif dari turunan fungsi cosinus.</sub>

**Pembahasan:** Gunakan identitas aljabar dan trigonometri terlebih dahulu:
$$f(x) = (\cos^2(2x) - \sin^2(2x))(\cos^2(2x) + \sin^2(2x))$$
Karena $\cos^2(2x) + \sin^2(2x) = 1$ dan $\cos^2(2x) - \sin^2(2x) = \cos(4x)$, maka:
$$f(x) = \cos(4x)$$
Turunkan menggunakan aturan rantai:
$$f'(x) = -\sin(4x) \cdot 4 = -4\sin(4x)$$
Karena $f'(x) = k\sin(4x)$, diperoleh nilai $k = -4$.
**Acuan:** siswa — siswa hal.127

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b02-b-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: evaluasi nilai turunan fungsi trigonometri rasional*

Diketahui fungsi $g(x) = \dfrac{\tan x}{1 + \tan x}$ untuk $x \ne \frac{\pi}{2} + k\pi$ dan $\tan x \ne -1$. Nilai dari $g'\left(\frac{\pi}{4}\right)$ adalah ....

- A. $\dfrac{1}{4}$  
  <sub>Salah: Siswa menghitung pembilang sebagai $1$ bukan $\sec^2(\pi/4) = 2$.</sub>
- B. $1$  
  <sub>Salah: Siswa salah menyangka $\sec^2(\pi/4) = 4$ atau salah hitung penyebut menjadi 2.</sub>
- C. $2$  
  <sub>Salah: Siswa hanya menghitung turunan pembilang tanpa membagi dengan $(v(x))^2$.</sub>
- **D. $\dfrac{1}{2}$** ✅  
  <sub>Benar: $g'(x) = \frac{\sec^2 x}{(1 + \tan x)^2}$. Untuk $x = \frac{\pi}{4}$, didapat $\frac{2}{(1 + 1)^2} = \frac{2}{4} = \frac{1}{2}$.</sub>

**Pembahasan:** Misalkan $u(x) = \tan x \implies u'(x) = \sec^2 x$ dan $v(x) = 1 + \tan x \implies v'(x) = \sec^2 x$.
Menggunakan sifat turunan pembagian fungsi aljabar/trigonometri:
$$g'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2}$$
$$g'(x) = \frac{\sec^2 x(1 + \tan x) - \tan x(\sec^2 x)}{(1 + \tan x)^2} = \frac{\sec^2 x}{(1 + \tan x)^2}$$
Substitusikan $x = \frac{\pi}{4}$:
$\tan\left(\frac{\pi}{4}\right) = 1$
$\sec\left(\frac{\pi}{4}\right) = \sqrt{2} \implies \sec^2\left(\frac{\pi}{4}\right) = 2$
Maka:
$$g'\left(\frac{\pi}{4}\right) = \frac{2}{(1 + 1)^2} = \frac{2}{4} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b02-b-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: persamaan garis singgung eksponensial umum*

Garis singgung kurva $f(x) = 2^{3x - 1}$ di titik yang berabsis $x = 1$ memotong sumbu-$Y$ di titik $(0, c)$. Nilai dari konstanta $c$ adalah ....

- A. $1 - 12\ln 2$  
  <sub>Salah: Siswa salah menghitung nilai ordinat $f(1) = 2^2 = 4$ menjadi $1$.</sub>
- B. $4(1 - \ln 2)$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan rantai pangkat $3x - 1$ yaitu 3.</sub>
- **C. $4(1 - 3\ln 2)$** ✅  
  <sub>Benar: $y_1 = 4$, gradien $m = 12\ln 2$. Persamaan garis singgung $y - 4 = 12\ln 2(x - 1)$, titik potong sumbu-Y ($x=0$) menghasilkan $c = 4 - 12\ln 2 = 4(1 - 3\ln 2)$.</sub>
- D. $4(1 + 3\ln 2)$  
  <sub>Salah: Siswa salah tanda saat memindahkan suku konstanta ke ruas kanan.</sub>

**Pembahasan:** Langkah 1: Menentukan ordinat titik singgung untuk $x_1 = 1$:
$$y_1 = f(1) = 2^{3(1) - 1} = 2^2 = 4$$
Titik singgung berada di $(1, 4)$.

Langkah 2: Menentukan gradien garis singgung $m = f'(1)$.
Turunan $f(x) = 2^{3x - 1}$ menggunakan sifat turunan $a^{g(x)}$:
$$f'(x) = 2^{3x - 1} \cdot \ln 2 \cdot 3 = 3\ln 2 \cdot 2^{3x - 1}$$
Untuk $x = 1$:
$$m = f'(1) = 3\ln 2 \cdot 2^2 = 12\ln 2$$

Langkah 3: Persamaan garis singgung di titik $(1, 4)$:
$$y - y_1 = m(x - x_1) \implies y - 4 = 12\ln 2(x - 1)$$

Langkah 4: Menentukan titik potong dengan sumbu-$Y$ ($x = 0$):
$$y - 4 = 12\ln 2(0 - 1)$$
$$y = 4 - 12\ln 2 = 4(1 - 3\ln 2)$$
Jadi nilai $c = 4(1 - 3\ln 2)$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b02-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: analisis nilai kosinus selisih absis stasioner*

Diketahui fungsi $f(x) = \dfrac{\sin x}{2 + \cos x}$ didefinisikan pada interval $[0, 2\pi]$. Jika $x_1$ dan $x_2$ merupakan dua absis dari titik stasioner kurva $y = f(x)$ dengan $x_1 < x_2$, nilai dari $\cos(x_1 - x_2)$ adalah ....

- **A. $-\dfrac{1}{2}$** ✅  
  <sub>Benar: Turunan $f'(x) = \frac{\cos x(2 + \cos x) - \sin x(-\sin x)}{(2 + \cos x)^2} = \frac{2\cos x + 1}{(2 + \cos x)^2}$. Titik stasioner diperoleh saat $f'(x) = 0 \iff 2\cos x + 1 = 0 \iff \cos x = -\frac{1}{2}$. Pada selang $[0, 2\pi]$, nilai absisnya adalah $x_1 = \frac{2\pi}{3}$ dan $x_2 = \frac{4\pi}{3}$. Nilai $\cos(x_1 - x_2) = \cos\left(\frac{2\pi}{3} - \frac{4\pi}{3}\right) = \cos\left(-\frac{2\pi}{3}\right) = \cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$.</sub>
- B. $\dfrac{1}{2}$  
  <sub>Salah: Siswa salah menentukan tanda kuadran atau mengabaikan tanda minus pada kosinus sudut tumpul</sub>
- C. $\dfrac{\sqrt{3}}{2}$  
  <sub>Salah: Siswa tertukar antara sinus dan kosinus serta keliru menentukan tanda kuadran</sub>
- D. $-\dfrac{\sqrt{3}}{2}$  
  <sub>Salah: Siswa tertukar nilai sudut istimewa antara sinus dan kosinus untuk sudut berpenyiku</sub>

**Pembahasan:** Gunakan aturan turunan fungsi pecahan $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
Misalkan $u(x) = \sin x \implies u'(x) = \cos x$ dan $v(x) = 2 + \cos x \implies v'(x) = -\sin x$.

Maka turunan pertamanya adalah:
$$f'(x) = \frac{\cos x(2 + \cos x) - \sin x(-\sin x)}{(2 + \cos x)^2} = \frac{2\cos x + \cos^2 x + \sin^2 x}{(2 + \cos x)^2} = \frac{2\cos x + 1}{(2 + \cos x)^2}$$

Titik stasioner tercapai saat $f'(x) = 0$:
$$2\cos x + 1 = 0 \iff \cos x = -\frac{1}{2}$$

Pada interval $[0, 2\pi]$, nilai $x$ yang memenuhi adalah:
$$x_1 = \frac{2\pi}{3} \quad \text{dan} \quad x_2 = \frac{4\pi}{3}$$

Sehingga nilai dari $\cos(x_1 - x_2)$ adalah:
$$\cos\left(\frac{2\pi}{3} - \frac{4\pi}{3}\right) = \cos\left(-\frac{2\pi}{3}\right) = \cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$$
**Acuan:** siswa — siswa hal.133

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b02-b-hard-bt01-019
*orisinal | C5 | 6 langkah | jenis: luas daerah garis singgung kurva eksponensial*

Garis singgung kurva $f(x) = x e^{2 - x^2}$ pada titik yang berabsis $x = 1$ memotong sumbu-$X$ di titik $(p, 0)$ dan sumbu-$Y$ di titik $(0, q)$. Luas daerah segitiga yang dibatasi oleh garis singgung tersebut dan kedua sumbu koordinat adalah ....

- A. $e$  
  <sub>Salah: Siswa keliru membagi dua nilai titik potong sumbu-Y atau salah substitusi titik potong</sub>
- B. $4e$  
  <sub>Salah: Siswa lupa mengalikan dengan faktor setengah pada rumus luas segitiga</sub>
- **C. $2e$** ✅  
  <sub>Benar: Nilai $f(1) = 1 \cdot e^{2-1} = e$. Turunan fungsi $f'(x) = 1 \cdot e^{2-x^2} + x(-2x)e^{2-x^2} = (1 - 2x^2)e^{2-x^2}$, sehingga gradien garis singgung $m = f'(1) = (1 - 2)e = -e$. Persamaan garis singgung: $y - e = -e(x - 1) \iff ex + y = 2e$. Titik potong sumbu-$X$ adalah $(2, 0)$ dan sumbu-$Y$ adalah $(0, 2e)$. Luas segitiga $L = \frac{1}{2} \cdot |2| \cdot |2e| = 2e$.</sub>
- D. $\dfrac{e}{2}$  
  <sub>Salah: Siswa salah menentukan absis titik potong sumbu-X menjadi 1/2</sub>

**Pembahasan:** Langkah 1: Tentukan titik singgung pada kurva saat $x = 1$:
$$y_1 = f(1) = 1 \cdot e^{2 - 1^2} = e$$
Titik singgung berada di $(1, e)$.

Langkah 2: Tentukan turunan pertama menggunakan aturan perkalian dan aturan rantai:
$$u = x \implies u' = 1$$
$$v = e^{2 - x^2} \implies v' = -2x e^{2 - x^2}$$
$$f'(x) = u'v + uv' = e^{2 - x^2} + x(-2x e^{2 - x^2}) = (1 - 2x^2)e^{2 - x^2}$$

Langkah 3: Tentukan gradien garis singgung $m$ di $x = 1$:
$$m = f'(1) = (1 - 2(1^2))e^{2 - 1} = -1 \cdot e = -e$$

Langkah 4: Tentukan persamaan garis singgung:
$$y - y_1 = m(x - x_1)$$
$$y - e = -e(x - 1)$$
$$y - e = -ex + e \iff ex + y = 2e$$

Langkah 5: Tentukan titik potong dengan sumbu koordinat:
- Titik potong sumbu-$X$ ($y = 0$): $ex = 2e \implies x = 2$, sehingga $p = 2$.
- Titik potong sumbu-$Y$ ($x = 0$): $y = 2e$, sehingga $q = 2e$.

Langkah 6: Hitung luas segitiga:
$$L = \frac{1}{2} \cdot |p| \cdot |q| = \frac{1}{2} \cdot 2 \cdot 2e = 2e$$
**Acuan:** siswa — siswa hal.139

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b02-b-hard-bt01-020
*orisinal | C5 | 6 langkah | jenis: hasil kali nilai stasioner fungsi eksponensial*

Diketahui fungsi $f(x) = (x^2 - 4x + 1)e^x$. Jika $x_1$ dan $x_2$ adalah absis dari titik stasioner fungsi $f(x)$ dengan $x_1 < x_2$, maka nilai dari $f(x_1) \cdot f(x_2)$ adalah ....

- A. $-12e^4$  
  <sub>Salah: Siswa keliru menjumlahkan pangkat eksponen pada perkalian e^(-1) dan e^3</sub>
- **B. $-12e^2$** ✅  
  <sub>Benar: Turunan $f'(x) = (2x - 4)e^x + (x^2 - 4x + 1)e^x = (x^2 - 2x - 3)e^x = (x - 3)(x + 1)e^x$. Stasioner saat $f'(x) = 0 \implies x_1 = -1$ dan $x_2 = 3$. Nilai $f(-1) = ((-1)^2 - 4(-1) + 1)e^{-1} = 6e^{-1}$. Nilai $f(3) = (3^2 - 4(3) + 1)e^3 = -2e^3$. Hasil kali $f(x_1) \cdot f(x_2) = (6e^{-1})(-2e^3) = -12e^2$.</sub>
- C. $-6e^2$  
  <sub>Salah: Siswa salah saat menghitung nilai f(-1) karena keliru tanda kuadrat atau perkalian negatif</sub>
- D. $12e^2$  
  <sub>Salah: Siswa salah tanda negatif saat mengevaluasi nilai fungsi f(3)</sub>

**Pembahasan:** Langkah 1: Tentukan turunan $f'(x)$ menggunakan sifat perkalian fungsi $(uv)' = u'v + uv'$:
Misalkan $u = x^2 - 4x + 1 \implies u' = 2x - 4$
Misalkan $v = e^x \implies v' = e^x$
$$f'(x) = (2x - 4)e^x + (x^2 - 4x + 1)e^x$$

Langkah 2: Sederhanakan bentuk turunan:
$$f'(x) = (x^2 - 2x - 3)e^x$$

Langkah 3: Faktorkan untuk menemukan absis titik stasioner saat $f'(x) = 0$:
$$(x - 3)(x + 1)e^x = 0$$
Karena $e^x > 0$ untuk seluruh $x \in \mathbb{R}$, maka:
$$(x - 3)(x + 1) = 0 \implies x = 3 \quad \text{atau} \quad x = -1$$
Karena $x_1 < x_2$, maka diperoleh $x_1 = -1$ dan $x_2 = 3$.

Langkah 4: Hitung nilai fungsi di $x_1 = -1$:
$$f(-1) = ((-1)^2 - 4(-1) + 1)e^{-1} = (1 + 4 + 1)e^{-1} = 6e^{-1}$$

Langkah 5: Hitung nilai fungsi di $x_2 = 3$:
$$f(3) = (3^2 - 4(3) + 1)e^3 = (9 - 12 + 1)e^3 = -2e^3$$

Langkah 6: Hitung hasil kali nilai stasioner:
$$f(x_1) \cdot f(x_2) = (6e^{-1}) \cdot (-2e^3) = -12e^{-1 + 3} = -12e^2$$
**Acuan:** siswa — siswa hal.121

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
