# Lembar koreksi — kelas12_tl SMA12L-B2 subbab C: Aplikasi Turunan Fungsi

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b02-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: titik balik fungsi kuadrat*

Titik balik minimum dari fungsi $f(x) = 3x^2 - 12$ adalah ....

- A. $(2, 0)$  
  <sub>Salah: Siswa menentukan titik potong kurva dengan sumbu-$x$, bukan titik stasioner.</sub>
- **B. $(0, -12)$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 6x = 0 \implies x = 0$. Nilai $f(0) = 3(0)^2 - 12 = -12$. Jadi, titik balik minimumnya adalah $(0, -12)$.</sub>
- C. $(6, -12)$  
  <sub>Salah: Siswa menganggap koefisien turunan pertama ($6$) sebagai absis titik balik.</sub>
- D. $(0, 12)$  
  <sub>Salah: Siswa salah tanda saat menghitung nilai fungsi untuk $x = 0$.</sub>

**Pembahasan:** Turunan pertama fungsi adalah $f'(x) = 6x$.
Syarat stasioner tercapai saat $f'(x) = 0$:
$$6x = 0 \iff x = 0$$
Substitusikan $x = 0$ ke fungsi $f(x)$:
$$f(0) = 3(0)^2 - 12 = -12$$
Karena koefisien $x^2$ positif, kurva terbuka ke atas sehingga titik $(0, -12)$ merupakan titik balik minimum.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b02-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: nilai ekstrem fungsi kuadrat*

Nilai ekstrem dari fungsi $f(x) = x^2 - 8x + 12$ adalah ....

- A. Nilai minimum $-28$  
  <sub>Salah: Siswa salah menghitung tanda saat substitusi, $16 - 32 - 12 = -28$.</sub>
- B. Nilai maksimum $-4$  
  <sub>Salah: Siswa salah menentukan jenis nilai ekstrem antara minimum dan maksimum.</sub>
- **C. Nilai minimum $-4$** ✅  
  <sub>Benar: $f'(x) = 2x - 8 = 0 \implies x = 4$. Nilai ekstrem $f(4) = 4^2 - 8(4) + 12 = -4$. Karena $f''(x) = 2 > 0$, maka bernilai minimum.</sub>
- D. Nilai minimum $4$  
  <sub>Salah: Siswa menuliskan absis pembuat stasioner ($x = 4$), bukan nilai fungsinya.</sub>

**Pembahasan:** Turunan pertama fungsi:
$$f'(x) = 2x - 8$$
Syarat stasioner:
$$2x - 8 = 0 \iff x = 4$$
Substitusikan $x = 4$ ke dalam $f(x)$:
$$f(4) = (4)^2 - 8(4) + 12 = 16 - 32 + 12 = -4$$
Karena koefisien $x^2$ bernilai positif ($a = 1 > 0$), kurva terbuka ke atas sehingga nilai ekstremnya adalah nilai minimum $-4$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-13a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b02-c-easy-bt01-003
*orisinal | C2 | 2 langkah | jenis: gradien garis singgung kurva*

Gradien garis singgung kurva $f(x) = 2x^3 - 5x$ di titik dengan absis $x = 2$ adalah ....

- A. $29$  
  <sub>Salah: Siswa salah operasi tanda, menghitung $24 + 5 = 29$ alih-alih dikurangi.</sub>
- B. $6$  
  <sub>Salah: Siswa mensubstitusikan $x = 2$ ke dalam fungsi awal $f(2) = 2(8) - 10 = 6$, bukan ke turunan.</sub>
- **C. $19$** ✅  
  <sub>Benar: $f'(x) = 6x^2 - 5$. Pada $x = 2$, gradien garis singgung $m = f'(2) = 6(2)^2 - 5 = 24 - 5 = 19$.</sub>
- D. $7$  
  <sub>Salah: Siswa menurunkan $2x^3$ menjadi $6x$ (lupa menurunkan pangkat menjadi kuadrat), lalu menghitung $6(2) - 5 = 7$.</sub>

**Pembahasan:** Gradien garis singgung $m$ pada kurva di $x = a$ diperoleh dari turunan pertama $m = f'(a)$.
Turunan pertama fungsi $f(x)$ adalah:
$$f'(x) = 6x^2 - 5$$
Substitusikan $x = 2$:
$$m = f'(2) = 6(2)^2 - 5 = 6(4) - 5 = 24 - 5 = 19$$
**Acuan:** siswa — siswa hal.149

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b02-c-easy-bt01-004
*orisinal | C1 | 2 langkah | jenis: turunan kedua fungsi polinomial*

Turunan kedua $f''(x)$ dari fungsi $f(x) = 2x^4 - 5x^3 + 7x - 9$ adalah ....

- A. $24x^2 - 30x + 7$  
  <sub>Salah: Siswa tidak menghilangkan konstanta $7$ saat melakukan turunan kedua.</sub>
- B. $48x - 30$  
  <sub>Salah: Siswa menurunkan fungsi sebanyak tiga kali (turunan ketiga).</sub>
- C. $8x^3 - 15x^2 + 7$  
  <sub>Salah: Siswa hanya menyelesaikan langkah sampai turunan pertama.</sub>
- **D. $24x^2 - 30x$** ✅  
  <sub>Benar: $f'(x) = 8x^3 - 15x^2 + 7$, kemudian diturunkan sekali lagi menghasilkan $f''(x) = 24x^2 - 30x$.</sub>

**Pembahasan:** Turunan pertama fungsi $f(x)$ adalah:
$$f'(x) = \frac{d}{dx}(2x^4 - 5x^3 + 7x - 9) = 8x^3 - 15x^2 + 7$$
Turunan kedua diperoleh dengan menurunkan kembali $f'(x)$:
$$f''(x) = \frac{d}{dx}(8x^3 - 15x^2 + 7) = 24x^2 - 30x$$
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b02-c-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: persamaan garis singgung kurva di titik diketahui*

Persamaan garis singgung pada kurva $y = 10 - 3x^2$ di titik $(-1, 7)$ adalah ....

- **A. $y = 6x + 13$** ✅  
  <sub>Benar: Turunan pertama fungsi adalah $y' = -6x$. Gradien di titik $(-1, 7)$ adalah $m = -6(-1) = 6$. Persamaan garis singgungnya adalah $y - 7 = 6(x - (-1)) \iff y - 7 = 6(x + 1) \iff y = 6x + 13$.</sub>
- B. $y = -6x + 1$  
  <sub>Salah: Keliru mengalikan tanda negatif pada gradien garis singgung sehingga $m = -6$ dan menghasilkan $y - 7 = -6(x + 1)$.</sub>
- C. $y = -6x + 13$  
  <sub>Salah: Menggunakan gradien dengan tanda negatif yang salah ($m = -6$) namun memaksakan konstanta bernilai positif $13$.</sub>
- D. $y = 6x - 1$  
  <sub>Salah: Salah tanda operasi saat memindahkan konstanta dari ruas kiri ke ruas kanan ($6 - 7 = -1$ bukannya $6 + 7 = 13$).</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung ($m$):
$y = 10 - 3x^2$
$y' = -6x$
Untuk titik $(-1, 7)$, absis $x = -1$:
$m = y'(-1) = -6(-1) = 6$

Langkah 2: Menentukan persamaan garis singgung:
$y - y_1 = m(x - x_1)$
$y - 7 = 6(x - (-1))
y - 7 = 6(x + 1)
y - 7 = 6x + 6
y = 6x + 6 + 7
y = 6x + 13

Jadi, persamaan garis singgung kurva tersebut adalah $y = 6x + 13$.
**Acuan:** siswa — siswa hal.145 Contoh Soal 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b02-c-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: interval fungsi turun kurva kubik*

Interval nilai $x$ yang menyebabkan fungsi $f(x) = x^3 - 12x + 7$ merupakan fungsi turun adalah ....

- A. $0 < x < 2$  
  <sub>Salah: Mengira salah satu pembuat nol kurva turunan selalu bernilai nol.</sub>
- B. $-4 < x < 4$  
  <sub>Salah: Keliru membagi konstanta pertidaksamaan, menganggap $x^2 - 16 < 0$ bukan $x^2 - 4 < 0$.</sub>
- C. $x < -2$ atau $x > 2$  
  <sub>Salah: Tertukar dengan syarat fungsi naik yaitu $f'(x) > 0$.</sub>
- **D. $-2 < x < 2$** ✅  
  <sub>Benar: Fungsi turun jika $f'(x) < 0$. Turunan pertama adalah $f'(x) = 3x^2 - 12$. Maka $3x^2 - 12 < 0 \iff x^2 - 4 < 0 \iff -2 < x < 2$.</sub>

**Pembahasan:** Syarat fungsi $f(x)$ turun adalah $f'(x) < 0$.

Langkah 1: Menentukan turunan pertama $f'(x)$:
$f(x) = x^3 - 12x + 7$
$f'(x) = 3x^2 - 12$

Langkah 2: Menyelesaikan pertidaksamaan $f'(x) < 0$:
$3x^2 - 12 < 0$
$3(x^2 - 4) < 0$
$(x - 2)(x + 2) < 0$
Pembuat nol adalah $x = -2$ dan $x = 2$.
Dengan menguji tanda pada garis bilangan, nilai negatif berada pada rentang $-2 < x < 2$.

Jadi, fungsi turun pada interval $-2 < x < 2$.
**Acuan:** pretest — kelas12_tl-b02-p0162-latihan-soal-aplikasi-turunan-fungsi-6a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b02-c-easy-bt01-007
*orisinal | C2 | 1 langkah | jenis: interval fungsi naik kurva kuadrat*

Grafik fungsi $f(x) = x^2 - 6x + 10$ akan naik pada interval ....

- A. $x < 3$  
  <sub>Salah: Menggunakan syarat fungsi turun yaitu $f'(x) < 0$ bukannya fungsi naik.</sub>
- **B. $x > 3$** ✅  
  <sub>Benar: Syarat fungsi naik adalah $f'(x) > 0$. Turunan fungsi tersebut adalah $f'(x) = 2x - 6$. Maka $2x - 6 > 0 \iff 2x > 6 \iff x > 3$.</sub>
- C. $x < -3$  
  <sub>Salah: Salah memindahkan tanda negatif konstanta pada pertidaksamaan menjadi $-6$ dan membalik tanda pertidaksamaan.</sub>
- D. $x > 6$  
  <sub>Salah: Lupa membagi konstanta 6 dengan koefisien turunan 2 saat menyelesaikan $2x > 6$.</sub>

**Pembahasan:** Berdasarkan sifat turunan, fungsi $f(x)$ naik jika $f'(x) > 0$.

Turunan dari $f(x) = x^2 - 6x + 10$ adalah:
$f'(x) = 2x - 6$

Syarat fungsi naik:
$2x - 6 > 0$
$2x > 6$
$x > 3$

Jadi, grafik fungsi naik pada interval $x > 3$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b02-c-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: absis titik stasioner kurva kuadrat*

Absis dari titik stasioner fungsi $f(x) = 2x^2 - 16x + 11$ adalah ....

- A. $x = -8$  
  <sub>Salah: Keliru menurunkan suku kuadrat menjadi $2x$ sekaligus salah tanda pada pemindahan konstanta.</sub>
- B. $x = 8$  
  <sub>Salah: Keliru menurunkan suku kuadrat sehingga turunan dianggap $2x - 16$, menghasilkan $2x = 16 \iff x = 8$.</sub>
- C. $x = -4$  
  <sub>Salah: Salah memindahkan konstanta ke ruas kanan menjadi tanda negatif sehingga $4x = -16$.</sub>
- **D. $x = 4$** ✅  
  <sub>Benar: Kondisi stasioner kurva tercapai ketika $f'(x) = 0$. Turunan dari fungsi tersebut adalah $f'(x) = 4x - 16$. Maka $4x - 16 = 0 \iff 4x = 16 \iff x = 4$.</sub>

**Pembahasan:** Kondisi diam atau stasioner tercapai saat turunan pertama kurva sama dengan nol:
$f'(x) = 0$

Turunan pertama dari $f(x) = 2x^2 - 16x + 11$ adalah:
$f'(x) = 4x - 16$

Maka:
$4x - 16 = 0$
$4x = 16$
$x = 4$

Jadi, absis titik stasioner fungsi tersebut adalah $x = 4$.
**Acuan:** siswa — siswa hal.153

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b02-c-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: titik balik fungsi kuadrat*

Titik balik maksimum dari fungsi $f(x) = -3x^2 + 12x - 5$ adalah ....

- **A. $(2, 7)$** ✅  
  <sub>Benar: $f'(x) = -6x + 12 = 0 \implies x = 2$. Nilai $f(2) = -3(2)^2 + 12(2) - 5 = -12 + 24 - 5 = 7$.</sub>
- B. $(2, -5)$  
  <sub>Salah: Hanya mengambil konstanta $c = -5$ sebagai ordinat titik puncak.</sub>
- C. $(4, -5)$  
  <sub>Salah: Salah rumus absis titik stasioner menggunakan $-b/a$ alih-alih $-b/(2a)$.</sub>
- D. $(-2, -41)$  
  <sub>Salah: Salah tanda saat menyelesaikan persamaan $-6x + 12 = 0$ menjadi $x = -2$.</sub>

**Pembahasan:** Turunan pertama fungsi adalah:
$$f'(x) = -6x + 12$$
Titik stasioner diperoleh ketika $f'(x) = 0$:
$$-6x + 12 = 0 \iff -6x = -12 \iff x = 2$$
Substitusikan $x = 2$ ke dalam fungsi awal:
$$f(2) = -3(2)^2 + 12(2) - 5 = -12 + 24 - 5 = 7$$
Karena koefisien $x^2$ bernilai negatif ($-3 < 0$), parabola membuka ke bawah sehingga titik $(2, 7)$ merupakan titik balik maksimum.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b02-c-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: turunan kedua fungsi polinomial*

Turunan kedua $f''(x)$ dari fungsi $f(x) = 5x^3 - 7x^2 + 6x - 11$ adalah ....

- A. $15x^2 - 14x + 6$  
  <sub>Salah: Berhenti pada turunan pertama saja tanpa menurunkan kembali.</sub>
- **B. $30x - 14$** ✅  
  <sub>Benar: $f'(x) = 15x^2 - 14x + 6$, sehingga $f''(x) = 30x - 14$.</sub>
- C. $30x - 7$  
  <sub>Salah: Salah menurunkan suku $-14x$ menjadi $-7$ bukan $-14$.</sub>
- D. $30x^2 - 14x$  
  <sub>Salah: Lupa mengurangi pangkat $x$ pada langkah turunan kedua.</sub>

**Pembahasan:** Langkah I: Menentukan turunan pertama $f'(x)$:
$$f'(x) = 3 \cdot 5x^{3-1} - 2 \cdot 7x^{2-1} + 6 = 15x^2 - 14x + 6$$
Langkah II: Menentukan turunan kedua $f''(x)$:
$$f''(x) = 2 \cdot 15x^{2-1} - 14 = 30x - 14$$
**Acuan:** siswa — siswa hal.159 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b02-c-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: konsep fungsi naik turunan pertama*

Jika suatu fungsi kontinu $f(x)$ memenuhi kondisi $f'(x) > 0$ untuk setiap $x$ dalam interval $I$, maka sifat grafik $f(x)$ pada interval tersebut adalah ....

- A. stasioner atau diam  
  <sub>Salah: Tertukar dengan kondisi titik stasioner yaitu $f'(x) = 0$.</sub>
- B. memiliki nilai minimum  
  <sub>Salah: Mengira tanda lebih dari nol menunjukkan nilai minimum fungsi.</sub>
- C. selalu turun  
  <sub>Salah: Tertukar dengan syarat fungsi turun yaitu $f'(x) < 0$.</sub>
- **D. selalu naik** ✅  
  <sub>Benar: Berdasarkan sifat kemonotonan fungsi, $f'(x) > 0$ pada seluruh interval menandakan fungsi naik.</sub>

**Pembahasan:** Berdasarkan sifat turunan fungsi terkait kemonotonan kurva:
1. Jika $f'(x) > 0$ untuk setiap $x \in I$, maka fungsi $f(x)$ naik pada $I$.
2. Jika $f'(x) < 0$ untuk setiap $x \in I$, maka fungsi $f(x)$ turun pada $I$.
3. Jika $f'(x) = 0$, fungsi dalam kondisi diam (stasioner).
Dengan demikian, grafik fungsi $f(x)$ selalu naik.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b02-c-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: gradien garis singgung kurva*

Kemiringan (gradien) garis singgung pada kurva $y = 3x^2 - 4x + 1$ di titik $(2, 5)$ adalah ....

- A. $6$  
  <sub>Salah: Hanya menghitung turunan koefisien $x^2$ tanpa melibatkan suku linear.</sub>
- **B. $8$** ✅  
  <sub>Benar: Gradien garis singgung $m = y'(2) = 6(2) - 4 = 12 - 4 = 8$.</sub>
- C. $16$  
  <sub>Salah: Salah melakukan operasi penjumlahan $12 + 4 = 16$ alih-alih pengurangan $12 - 4$.</sub>
- D. $5$  
  <sub>Salah: Mengambil nilai ordinat $y = 5$ sebagai nilai gradien garis singgung.</sub>

**Pembahasan:** Langkah I: Menentukan turunan pertama kurva:
$$y' = 6x - 4$$
Langkah II: Menghitung gradien $m$ di titik dengan absis $x = 2$:
$$m = y'(2) = 6(2) - 4 = 12 - 4 = 8$$
Jadi, kemiringan garis singgung kurva tersebut adalah 8.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b02-c-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: titik balik minimum fungsi kuadrat*

Titik balik minimum dari fungsi $f(x) = \frac{1}{2}x^2 + 5$ adalah ....

- **A. $(0, 5)$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = x$. Kondisi stasioner terpenuhi saat $f'(x) = 0$, sehingga $x = 0$. Substitusi nilai $x = 0$ menghasilkan $f(0) = \frac{1}{2}(0)^2 + 5 = 5$, sehingga titik baliknya adalah $(0, 5)$.</sub>
- B. $(5, 0)$  
  <sub>Salah: Siswa menukar posisi koordinat absis dan ordinat.</sub>
- C. $(0, 10)$  
  <sub>Salah: Siswa mengalikan konstanta dengan 2 alih-alih menyubstitusikan nilai ke fungsi awal.</sub>
- D. $(0, -5)$  
  <sub>Salah: Siswa salah memperhitungkan tanda positif konstanta menjadi negatif.</sub>

**Pembahasan:** Turunan pertama dari fungsi $f(x) = \frac{1}{2}x^2 + 5$ adalah $f'(x) = x$.
Syarat titik stasioner adalah $f'(x) = 0$, sehingga diperoleh $x = 0$.
Substitusikan $x = 0$ ke rumus fungsi:
$$f(0) = \frac{1}{2}(0)^2 + 5 = 5$$
Karena turunan kedua $f''(x) = 1 > 0$, titik tersebut merupakan titik balik minimum.
Jadi, koordinat titik balik minimumnya adalah $(0, 5)$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b02-c-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: persamaan garis singgung kurva di titik diketahui*

Persamaan garis singgung pada kurva $y = 5 - 2x^2$ di titik $(2, -3)$ adalah ....

- A. $y = -8x + 19$  
  <sub>Salah: Siswa salah menghitung perpindahan ruas tanda ordinat titik singgung.</sub>
- B. $y = 8x - 19$  
  <sub>Salah: Siswa keliru menggunakan nilai gradien positif alih-alih negatif.</sub>
- **C. $y = -8x + 13$** ✅  
  <sub>Benar: Turunan kurva $y' = -4x$. Pada absis $x = 2$, gradien garis singgung $m = -4(2) = -8$. Persamaan garisnya $y - (-3) = -8(x - 2) \iff y + 3 = -8x + 16 \iff y = -8x + 13$.</sub>
- D. $y = -8x - 13$  
  <sub>Salah: Siswa salah menjumlahkan konstanta pada ruas kanan.</sub>

**Pembahasan:** Turunan pertama fungsi kurva:
$$y' = -4x$$
Kemiringan (gradien) garis singgung di titik $(2, -3)$ adalah:
$$m = y'(2) = -4(2) = -8$$
Persamaan garis singgung bergradien $m = -8$ melalui titik $(2, -3)$:
$$y - y_1 = m(x - x_1)$$
$$y - (-3) = -8(x - 2)$$
$$y + 3 = -8x + 16$$
$$y = -8x + 13$$
Jadi, persamaan garis singgung kurva tersebut adalah $y = -8x + 13$.
**Acuan:** siswa — siswa hal.145 Contoh Soal 2.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b02-c-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: titik balik minimum fungsi kuadrat*

Titik balik minimum dari fungsi $f(x) = 4x^2 - 8x + 7$ adalah ....

- **A. $(1, 3)$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 8x - 8 = 0 \iff x = 1$. Nilai fungsinya $f(1) = 4(1)^2 - 8(1) + 7 = 3$, sehingga koordinat titik balik minimumnya adalah $(1, 3)$.</sub>
- B. $(1, -3)$  
  <sub>Salah: Siswa salah menghitung hasil penjumlahan konstanta menjadi negatif.</sub>
- C. $(2, 7)$  
  <sub>Salah: Siswa salah mencari akar turunan pertama $8x - 8 = 0$ menjadi $x = 2$.</sub>
- D. $(-1, 19)$  
  <sub>Salah: Siswa keliru membagi tanda negatif sehingga mendapatkan absis $x = -1$.</sub>

**Pembahasan:** Langkah I: menentukan turunan pertama dari fungsi:
$$f'(x) = 8x - 8$$
Langkah II: menentukan nilai $x$ pembuat stasioner ($f'(x) = 0$):
$$8x - 8 = 0 \iff 8x = 8 \iff x = 1$$
Langkah III: menghitung nilai fungsi pada $x = 1$:
$$f(1) = 4(1)^2 - 8(1) + 7 = 4 - 8 + 7 = 3$$
Karena koefisien $x^2$ positif ($a = 4 > 0$), titik tersebut merupakan titik balik minimum, yaitu $(1, 3)$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b02-c-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: turunan kedua fungsi polinomial*

Turunan kedua $f''(x)$ dari fungsi $f(x) = x^4 - 2x^3 + 5x^2 - 7$ adalah ....

- A. $4x^3 - 6x^2 + 10x$  
  <sub>Salah: Siswa hanya menyelesaikan langkah turunan pertama saja.</sub>
- **B. $12x^2 - 12x + 10$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 4x^3 - 6x^2 + 10x$. Menurunkan sekali lagi menghasilkan $f''(x) = 12x^2 - 12x + 10$.</sub>
- C. $12x^2 - 6x + 10$  
  <sub>Salah: Siswa lupa mengalikan koefisien dengan pangkat pada suku kedua saat menurunkan turunan pertama.</sub>
- D. $12x^2 - 12x$  
  <sub>Salah: Siswa salah menganggap turunan dari $10x$ bernilai 0.</sub>

**Pembahasan:** Diberikan $f(x) = x^4 - 2x^3 + 5x^2 - 7$.
Langkah I: mencari turunan pertama $f'(x)$:
$$f'(x) = 4x^3 - 6x^2 + 10x$$
Langkah II: mencari turunan kedua $f''(x)$:
$$f''(x) = \frac{d}{dx}(4x^3 - 6x^2 + 10x) = 12x^2 - 12x + 10$$
Jadi, turunan kedua dari fungsi tersebut adalah $12x^2 - 12x + 10$.
**Acuan:** siswa — siswa hal.159 Contoh Soal 2.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b02-c-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: konsep fungsi turun turunan pertama*

Berdasarkan sifat turunan fungsi, kurva $y = f(x)$ merupakan fungsi turun pada suatu interval $I$ apabila turunan pertamanya memenuhi syarat ....

- A. $f''(x) < 0$ untuk setiap $x \in I$  
  <sub>Salah: Siswa keliru menggunakan turunan kedua yang merupakan uji kecekungan kurva.</sub>
- B. $f'(x) > 0$ untuk setiap $x \in I$  
  <sub>Salah: Siswa tertukar dengan syarat fungsi naik.</sub>
- C. $f'(x) = 0$ untuk setiap $x \in I$  
  <sub>Salah: Siswa tertukar dengan kondisi fungsi stasioner atau diam.</sub>
- **D. $f'(x) < 0$ untuk setiap $x \in I$** ✅  
  <sub>Benar: Sesuai sifat kemonotonan fungsi, kurva $f(x)$ turun pada interval $I$ jika nilai turunan pertamanya selalu bernilai negatif ($f'(x) < 0$) untuk setiap $x \in I$.</sub>

**Pembahasan:** Berdasarkan sifat tingkah laku fungsi:
1. Jika $f'(x) > 0$ untuk setiap $x \in I$, maka fungsi $f(x)$ naik pada $I$.
2. Jika $f'(x) < 0$ untuk setiap $x \in I$, maka fungsi $f(x)$ turun pada $I$.
3. Jika $f'(x) = 0$, maka fungsi diam (stasioner).
Jadi, syarat kurva merupakan fungsi turun pada interval $I$ adalah $f'(x) < 0$ untuk setiap $x \in I$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b02-c-easy-bt01-018
*variasi (angka) | C2 | 2 langkah | jenis: nilai ekstrem fungsi kuadrat*

Nilai ekstrem dan jenis titik ekstrem dari fungsi $f(x) = x^2 - 10x + 16$ adalah ....

- **A. Nilai minimum $-9$ pada $x = 5$** ✅  
  <sub>Benar: $f'(x) = 2x - 10 = 0 \implies x = 5$. Nilai $f(5) = 5^2 - 10(5) + 16 = -9$. Karena kurva terbuka ke atas, jenisnya minimum.</sub>
- B. Nilai minimum $9$ pada $x = -5$  
  <sub>Salah: Siswa salah menghitung absis stasioner karena lupa tanda negatif saat menyelesaikan $2x - 10 = 0$.</sub>
- C. Nilai minimum $-11$ pada $x = 5$  
  <sub>Salah: Siswa salah melakukan operasi aritmetika saat menghitung $25 - 50 + 16$.</sub>
- D. Nilai maksimum $-9$ pada $x = 5$  
  <sub>Salah: Siswa salah menentukan jenis nilai ekstrem (tertukar antara maksimum dan minimum).</sub>

**Pembahasan:** Turunan pertama fungsi adalah $f'(x) = 2x - 10$.
Fungsi mencapai nilai ekstrem saat $f'(x) = 0$:
$$2x - 10 = 0 \iff 2x = 10 \iff x = 5$$
Substitusikan $x = 5$ ke fungsi awal:
$$f(5) = (5)^2 - 10(5) + 16 = 25 - 50 + 16 = -9$$
Karena turunan kedua $f''(x) = 2 > 0$, maka fungsi memiliki nilai balik minimum.
Jadi, nilai ekstremnya adalah nilai minimum $-9$ pada $x = 5$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-13a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b02-c-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: uji turunan kedua nilai ekstrem*

Diberikan suatu fungsi kontinu $f(x)$ dengan $f'(c) = 0$. Berdasarkan sifat uji turunan kedua, jika $f''(c) < 0$, maka titik $(c, f(c))$ merupakan ....

- A. titik balik minimum  
  <sub>Salah: Siswa tertukar dengan kondisi $f''(c) > 0$.</sub>
- B. titik potong sumbu  
  <sub>Salah: Siswa keliru mengaitkan turunan kedua dengan perpotongan sumbu koordinat.</sub>
- **C. titik balik maksimum** ✅  
  <sub>Benar: Sesuai sifat uji turunan kedua pada kurva kontinu, jika $f'(c) = 0$ dan $f''(c) < 0$, maka $f(c)$ adalah nilai balik maksimum sehingga titiknya adalah titik balik maksimum.</sub>
- D. titik belok horizontal  
  <sub>Salah: Siswa mengira nilai turunan kedua bernilai negatif menghasilkan titik belok.</sub>

**Pembahasan:** Berdasarkan sifat uji turunan kedua untuk menentukan nilai ekstrem:
1. Jika $f'(c) = 0$ dan $f''(c) < 0$, maka $f(c)$ merupakan nilai balik maksimum dan titik $(c, f(c))$ adalah titik balik maksimum.
2. Jika $f'(c) = 0$ dan $f''(c) > 0$, maka $f(c)$ merupakan nilai balik minimum dan titik $(c, f(c))$ adalah titik balik minimum.

Dengan demikian, jika $f''(c) < 0$, titik tersebut merupakan titik balik maksimum.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b02-c-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: persamaan garis singgung kurva di titik diketahui*

Persamaan garis singgung pada kurva $y = x^2 - 4x + 6$ di titik $A$ dengan absis $4$ adalah ....

- A. $y = 6x - 18$  
  <sub>Salah: Siswa keliru menganggap nilai fungsi $y = 6$ sebagai gradien garis singgung.</sub>
- B. $y = 4x - 14$  
  <sub>Salah: Siswa salah menghitung ordinat titik singgung menjadi $y = 2$.</sub>
- **C. $y = 4x - 10$** ✅  
  <sub>Benar: Untuk absis $x = 4$, diperoleh ordinat $y = 4^2 - 4(4) + 6 = 6$, sehingga titik singgungnya adalah $(4, 6)$. Turunan kurva adalah $y' = 2x - 4$, sehingga gradien garis singgung $m = 2(4) - 4 = 4$. Persamaan garis singgungnya adalah $y - 6 = 4(x - 4) \iff y = 4x - 10$.</sub>
- D. $y = 4x - 22$  
  <sub>Salah: Siswa keliru memindahkan konstanta $-6$ dari ruas kiri menjadi $-16 - 6 = -22$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat titik singgung.
Substitusikan $x = 4$ ke persamaan kurva:
$$y = 4^2 - 4(4) + 6 = 16 - 16 + 6 = 6$$
Jadi, titik singgungnya adalah $(4, 6)$.

Langkah 2: Menentukan gradien dan persamaan garis singgung.
$$y' = 2x - 4$$
Untuk $x = 4$, gradien $m = 2(4) - 4 = 4$.
Persamaan garis singgung dengan gradien $m = 4$ melalui titik $(4, 6)$ adalah:
$$y - y_1 = m(x - x_1)$$
$$y - 6 = 4(x - 4)$$
$$y - 6 = 4x - 16$$
$$y = 4x - 10$$
**Acuan:** siswa — siswa hal.145 Ayo Mencoba 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b02-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: interval kemonotonan fungsi*

Interval nilai $x$ yang menyebabkan kurva fungsi $f(x) = 2x^3 - 9x^2 - 24x + 7$ turun adalah ....

- A. $-4 < x < 1$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan kuadrat menjadi $(x + 4)(x - 1)$.</sub>
- B. $x < -4$ atau $x > 1$  
  <sub>Salah: Kombinasi kesalahan pemfaktoran tanda akar dan pembalikan interval pertidaksamaan.</sub>
- C. $x < -1$ atau $x > 4$  
  <sub>Salah: Menggunakan syarat fungsi naik ($f'(x) > 0$) alih-alih fungsi turun.</sub>
- **D. $-1 < x < 4$** ✅  
  <sub>Benar: Syarat fungsi turun adalah $f'(x) < 0$. Turunan pertama $f'(x) = 6x^2 - 18x - 24 = 6(x - 4)(x + 1) < 0$, sehingga intervalnya $-1 < x < 4$.</sub>

**Pembahasan:** Turunan pertama fungsi:
$$f'(x) = 6x^2 - 18x - 24$$
Syarat kurva turun adalah $f'(x) < 0$:
$$6x^2 - 18x - 24 < 0$$
$$x^2 - 3x - 4 < 0$$
$$(x - 4)(x + 1) < 0$$
Pembuat nol adalah $x = -1$ dan $x = 4$. Melalui uji garis bilangan, nilai negatif berada pada interval $-1 < x < 4$.
**Acuan:** pretest — kelas12_tl-b02-p0162-latihan-soal-aplikasi-turunan-fungsi-6a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b02-c-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: titik balik fungsi kubik*

Titik balik maksimum dan titik balik minimum dari grafik fungsi $f(x) = \frac{1}{3}x^3 - 2x^2 + 3x + 5$ berturut-turut adalah ....

- **A. $\left(1, \frac{19}{3}\right)$ dan $(3, 5)$** ✅  
  <sub>Benar: $f'(x) = x^2 - 4x + 3 = 0$ menghasilkan $x = 1$ dan $x = 3$. Uji turunan kedua $f''(1) = -2 < 0$ (maksimum pada $\left(1, \frac{19}{3}\right)$) dan $f''(3) = 2 > 0$ (minimum pada $(3, 5)$).</sub>
- B. $\left(1, \frac{19}{3}\right)$ dan $(3, 0)$  
  <sub>Salah: Salah menghitung nilai fungsi saat $x = 3$, hanya memasukkan ke turunan pertama sehingga menghasilkan $0$.</sub>
- C. $(3, 5)$ dan $\left(1, \frac{19}{3}\right)$  
  <sub>Salah: Tertukar antara titik balik maksimum dengan titik balik minimum.</sub>
- D. $\left(-1, -\frac{1}{3}\right)$ dan $(-3, -31)$  
  <sub>Salah: Kesalahan tanda saat mencari akar-akar $f'(x) = 0$ sehingga diperoleh $x = -1$ dan $x = -3$.</sub>

**Pembahasan:** Turunan pertama fungsi:
$$f'(x) = x^2 - 4x + 3$$
Titik stasioner tercapai saat $f'(x) = 0$:
$$(x - 1)(x - 3) = 0 \implies x_1 = 1 \text{ atau } x_2 = 3$$
Turunan kedua:
$$f''(x) = 2x - 4$$
Untuk $x = 1$:
$$f''(1) = 2(1) - 4 = -2 < 0 \quad (\text{maksimum})$$
$$f(1) = \frac{1}{3}(1)^3 - 2(1)^2 + 3(1) + 5 = \frac{1}{3} - 2 + 3 + 5 = \frac{19}{3}$$
Titik balik maksimum adalah $\left(1, \frac{19}{3}\right)$.

Untuk $x = 3$:
$$f''(3) = 2(3) - 4 = 2 > 0 \quad (\text{minimum})$$
$$f(3) = \frac{1}{3}(27) - 2(9) + 3(3) + 5 = 9 - 18 + 9 + 5 = 5$$
Titik balik minimum adalah $(3, 5)$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b02-c-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: persamaan garis singgung sejajar garis*

Persamaan garis singgung kurva $y = x^2 - 3x + 4$ yang sejajar dengan garis $5x - y + 2 = 0$ adalah ....

- A. $y = -\frac{1}{5}x + \frac{44}{5}$  
  <sub>Salah: Menggunakan rumus garis tegak lurus ($m_1 m_2 = -1$) alih-alih garis sejajar ($m_1 = m_2$).</sub>
- B. $y = 5x + 12$  
  <sub>Salah: Kesalahan tanda saat memindahkan konstanta persamaan garis $y = 5(x - 4) - 8$.</sub>
- C. $y = 5x - 4$  
  <sub>Salah: Lupa mengalikan gradien dengan absis titik singgung saat ekspansi kurung.</sub>
- **D. $y = 5x - 12$** ✅  
  <sub>Benar: Gradien garis $m = 5$. Dari $y' = 2x - 3 = 5$, didapat $x = 4$. Ordinat titik singgung $y = 4^2 - 3(4) + 4 = 8$. Persamaan garis singgung adalah $y - 8 = 5(x - 4) \iff y = 5x - 12$.</sub>

**Pembahasan:** Garis $5x - y + 2 = 0$ memiliki gradien $m = 5$. Karena sejajar, garis singgung kurva juga memiliki gradien $m = 5$.
Turunan kurva:
$$y' = 2x - 3$$
$$2x - 3 = 5 \implies 2x = 8 \implies x = 4$$
Substitusikan $x = 4$ ke persamaan kurva:
$$y = (4)^2 - 3(4) + 4 = 16 - 12 + 4 = 8$$
Titik singgung adalah $(4, 8)$. Persamaan garis singgung:
$$y - y_1 = m(x - x_1)$$
$$y - 8 = 5(x - 4)$$
$$y = 5x - 20 + 8$$
$$y = 5x - 12$$
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b02-c-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: nilai balik fungsi menggunakan turunan*

Nilai balik minimum dari fungsi $f(x) = 2x^3 - 3x^2 - 12x + 10$ adalah ....

- **A. $-10$** ✅  
  <sub>Benar: $f'(x) = 6x^2 - 6x - 12 = 0 \implies x = 2$ atau $x = -1$. $f''(2) = 18 > 0$ menunjukkan titik balik minimum di $x = 2$. Nilai minimum $f(2) = 2(8) - 3(4) - 12(2) + 10 = -10$.</sub>
- B. $-12$  
  <sub>Salah: Kesalahan hitung aritmetika saat menyubstitusikan $x = 2$ ke dalam fungsi.</sub>
- C. $2$  
  <sub>Salah: Menyebutkan absis pembuat nilai minimum alih-alih nilai fungsinya.</sub>
- D. $17$  
  <sub>Salah: Menghitung nilai balik maksimum pada $x = -1$ bukan nilai balik minimum.</sub>

**Pembahasan:** Turunan pertama fungsi:
$$f'(x) = 6x^2 - 6x - 12$$
Titik stasioner tercapai saat $f'(x) = 0$:
$$6(x^2 - x - 2) = 0$$
$$(x - 2)(x + 1) = 0 \implies x = 2 \text{ atau } x = -1$$
Turunan kedua:
$$f''(x) = 12x - 6$$
Uji nilai $x$:
- Untuk $x = -1$: $f''(-1) = 12(-1) - 6 = -18 < 0$ (maksimum)
- Untuk $x = 2$: $f''(2) = 12(2) - 6 = 18 > 0$ (minimum)

Nilai balik minimum tercapai pada $x = 2$:
$$f(2) = 2(2)^3 - 3(2)^2 - 12(2) + 10 = 16 - 12 - 24 + 10 = -10$$
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b02-c-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: kecepatan partikel aplikasi turunan*

Sebuah benda bergerak lurus dengan persamaan gerak $s(t) = \frac{1}{3}t^3 - 4t^2 + 12t + 5$ ($s$ dalam meter dan $t$ dalam detik). Benda tersebut akan berhenti sesaat ketika nilai $t$ sama dengan ....

- A. $t = 1$ detik atau $t = 12$ detik  
  <sub>Salah: Siswa memfaktorkan perkalian 12 tanpa memperhatikan penjumlahan koefisien linear $-8$.</sub>
- **B. $t = 2$ detik atau $t = 6$ detik** ✅  
  <sub>Benar: Benda berhenti sesaat jika kecepatannya nol, $v(t) = s'(t) = 0$. Turunan fungsi: $s'(t) = t^2 - 8t + 12$. Persamaan $t^2 - 8t + 12 = 0 \iff (t - 2)(t - 6) = 0$, menghasilkan $t = 2$ atau $t = 6$.</sub>
- C. $t = 4$ detik saja  
  <sub>Salah: Siswa mencari nilai percepatan nol ($s''(t) = 2t - 8 = 0$), bukan kecepatan nol.</sub>
- D. $t = 3$ detik atau $t = 4$ detik  
  <sub>Salah: Siswa salah memfaktorkan $t^2 - 8t + 12$ menjadi $(t - 3)(t - 4)$ karena keliru menghitung hasil kali faktor.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi kecepatan $v(t)$.
Kecepatan merupakan turunan pertama dari fungsi posisi $s(t)$:
$v(t) = s'(t) = \frac{d}{dt}\left(\frac{1}{3}t^3 - 4t^2 + 12t + 5\right) = t^2 - 8t + 12$

Langkah 2: Menentukan nilai $t$ saat berhenti sesaat ($v(t) = 0$).
$t^2 - 8t + 12 = 0$
$(t - 2)(t - 6) = 0$
$t = 2$ atau $t = 6$

Jadi, benda berhenti sesaat saat $t = 2$ detik atau $t = 6$ detik.
**Acuan:** siswa — siswa hal.163 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b02-c-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: kemonotonan fungsi trigonometri*

Grafik fungsi $f(x) = \sin 2x$ pada interval $0 < x < \pi$ akan naik pada interval ....

- **A. $0 < x < \frac{\pi}{4}$ atau $\frac{3\pi}{4} < x < \pi$** ✅  
  <sub>Benar: Syarat fungsi naik adalah $f'(x) > 0$. $f'(x) = 2\cos 2x > 0 \iff \cos 2x > 0$. Untuk $0 < 2x < 2\pi$, $\cos 2x > 0$ terpenuhi pada $0 < 2x < \frac{\pi}{2}$ atau $\frac{3\pi}{2} < 2x < 2\pi$. Dibagi 2 menghasilkan $0 < x < \frac{\pi}{4}$ atau $\frac{3\pi}{4} < x < \pi$.</sub>
- B. $0 < x < \frac{\pi}{2}$  
  <sub>Salah: Siswa lupa membagi sudut $2x$ dengan $2$ pada batas interval kuadran pertama.</sub>
- C. $\frac{\pi}{2} < x < \frac{3\pi}{2}$  
  <sub>Salah: Siswa menggunakan batas sudut dasar trigonometri tanpa menyesuaikan dengan domain $x$.</sub>
- D. $\frac{\pi}{4} < x < \frac{3\pi}{4}$  
  <sub>Salah: Siswa menentukan interval ketika fungsi turun ($f'(x) < 0$).</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama fungsi.
$f(x) = \sin 2x$
$f'(x) = 2\cos 2x$

Langkah 2: Menentukan syarat fungsi naik.
$f'(x) > 0 \implies 2\cos 2x > 0 \implies \cos 2x > 0$

Langkah 3: Menyelesaikan pertidaksamaan pada $0 < x < \pi$ (sehingga $0 < 2x < 2\pi$).
Kosinus bernilai positif pada kuadran I dan IV:
Kuadran I: $0 < 2x < \frac{\pi}{2} \implies 0 < x < \frac{\pi}{4}$
Kuadran IV: $\frac{3\pi}{2} < 2x < 2\pi \implies \frac{3\pi}{4} < x < \pi$

Jadi, fungsi naik pada interval $0 < x < \frac{\pi}{4}$ atau $\frac{3\pi}{4} < x < \pi$.
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b02-c-medium-bt01-007
*orisinal | C4 | 4 langkah | jenis: garis singgung tegak lurus garis lain*

Persamaan garis singgung kurva $y = 2x^2 + 5x - 3$ yang tegak lurus terhadap garis $x + 9y - 4 = 0$ adalah ....

- A. $y = 9x + 5$  
  <sub>Salah: Siswa salah tanda saat menyederhanakan $y - 4 = 9x - 9$.</sub>
- B. $y = -\frac{1}{9}x + \frac{37}{9}$  
  <sub>Salah: Siswa memakai gradien yang sama dengan garis acuan (sejajar) bukan tegak lurus.</sub>
- **C. $y = 9x - 5$** ✅  
  <sub>Benar: Gradien garis $x + 9y - 4 = 0$ adalah $m_1 = -\frac{1}{9}$. Karena tegak lurus, gradien garis singgung $m = -\frac{1}{m_1} = 9$. Turunan kurva $y' = 4x + 5 = 9 \iff 4x = 4 \iff x = 1$. Ordinatnya $y = 2(1)^2 + 5(1) - 3 = 4$. Titik singgung $(1, 4)$. Persamaan garis singgung: $y - 4 = 9(x - 1) \iff y = 9x - 5$.</sub>
- D. $y = 9x - 13$  
  <sub>Salah: Siswa keliru menghitung ordinat titik singgung menjadi $-4$.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung ($m$).
Garis $x + 9y - 4 = 0 \iff 9y = -x + 4 \iff y = -\frac{1}{9}x + \frac{4}{9}$, maka $m_1 = -\frac{1}{9}$.
Karena garis singgung tegak lurus garis tersebut, maka $m \cdot m_1 = -1 \implies m = 9$.

Langkah 2: Menentukan absis titik singgung.
$m = y' = 4x + 5$
$4x + 5 = 9$
$4x = 4 \implies x = 1$

Langkah 3: Menentukan ordinat titik singgung.
$y = 2(1)^2 + 5(1) - 3 = 2 + 5 - 3 = 4$
Titik singgung adalah $(1, 4)$.

Langkah 4: Menentukan persamaan garis singgung.
$y - y_1 = m(x - x_1)$
$y - 4 = 9(x - 1)$
$y - 4 = 9x - 9$
$y = 9x - 5$
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b02-c-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung titik potong kurva*

Persamaan garis singgung kurva $y = x^2 - 5x + 9$ di titik potongnya dengan garis $y = 4x - 5$ yang memiliki absis terbesar adalah ....

- A. $y = 9x - 63$  
  <sub>Salah: Siswa lupa menambahkan ordinat titik singgung $y_1 = 23$ ke ruas kanan.</sub>
- B. $y = -x + 30$  
  <sub>Salah: Siswa menggunakan titik potong yang salah yaitu $x = 2$ sehingga $m = -1$ tetapi memasukkan titik $(7, 23)$.</sub>
- C. $y = 9x + 40$  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan konstanta ke ruas kanan.</sub>
- **D. $y = 9x - 40$** ✅  
  <sub>Benar: Titik potong ditentukan dari $x^2 - 5x + 9 = 4x - 5 \iff x^2 - 9x + 14 = 0$, sehingga $(x - 7)(x - 2) = 0$. Absis terbesar adalah $x = 7$, dengan ordinat $y = 4(7) - 5 = 23$. Gradien kurva $y' = 2x - 5$, pada $x = 7$ bernilai $m = 2(7) - 5 = 9$. Persamaan garis singgung: $y - 23 = 9(x - 7) \iff y = 9x - 40$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong dengan menyamakan kedua fungsi:
$$x^2 - 5x + 9 = 4x - 5$$
$$x^2 - 9x + 14 = 0$$
$$(x - 7)(x - 2) = 0$$
Diperoleh $x_1 = 2$ atau $x_2 = 7$. Absis terbesar adalah $x = 7$.
Substitusi $x = 7$ ke persamaan garis: $y = 4(7) - 5 = 23$. Titik singgung adalah $(7, 23)$.

Langkah 2: Menentukan gradien garis singgung kurva:
$$y' = 2x - 5$$
$$m = y'(7) = 2(7) - 5 = 9$$

Langkah 3: Menentukan persamaan garis singgung:
$$y - y_1 = m(x - x_1)$$
$$y - 23 = 9(x - 7)$$
$$y = 9x - 63 + 23$$
$$y = 9x - 40$$
**Acuan:** siswa — siswa hal.146 Ayo Mencoba 2.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b02-c-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: titik belok fungsi kubik*

Koordinat titik belok dari grafik fungsi $f(x) = x^3 - 9x^2 + 24x - 7$ adalah ....

- A. $(2, 13)$  
  <sub>Salah: Siswa menggunakan pembuat nol turunan pertama $x = 2$ yang merupakan titik stasioner, bukan titik belok.</sub>
- **B. $(3, 11)$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 3x^2 - 18x + 24$, turunan kedua $f''(x) = 6x - 18$. Titik belok terjadi saat $f''(x) = 0 \iff 6x = 18 \iff x = 3$. Nilai $f(3) = (3)^3 - 9(3)^2 + 24(3) - 7 = 27 - 81 + 72 - 7 = 11$. Koordinat titik belok adalah $(3, 11)$.</sub>
- C. $(3, 20)$  
  <sub>Salah: Siswa salah menghitung operasi aritmetika saat mensubstitusikan $x = 3$ ke rumus fungsi.</sub>
- D. $(4, 9)$  
  <sub>Salah: Siswa menggunakan pembuat nol turunan pertama $x = 4$ yang merupakan titik stasioner balik minimum.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan kedua fungsi $f(x)$:
$$f'(x) = 3x^2 - 18x + 24$$
$$f''(x) = 6x - 18$$
Syarat titik belok adalah $f''(x) = 0$:
$$6x - 18 = 0 \iff x = 3$$

Langkah 2: Menentukan ordinat titik belok dengan menghitung nilai $f(3)$:
$$f(3) = (3)^3 - 9(3)^2 + 24(3) - 7$$
$$f(3) = 27 - 81 + 72 - 7 = 11$$
Jadi, koordinat titik belok fungsi tersebut adalah $(3, 11)$.
**Acuan:** siswa — siswa hal.163 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b02-c-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung dengan sudut kemiringan*

Persamaan garis singgung pada kurva $y = 3x^2 - 13x + 8$ yang membentuk sudut $135^\circ$ terhadap sumbu-$x$ positif adalah ....

- A. $y = -x - 2$  
  <sub>Salah: Siswa lupa mengalikan tanda minus dengan suku $-x_1$ pada rumus garis singgung.</sub>
- **B. $y = -x - 4$** ✅  
  <sub>Benar: Gradien garis adalah $m = \tan 135^\circ = -1$. Turunan kurva $y' = 6x - 13$. Dari $6x - 13 = -1$, diperoleh $x = 2$. Ordinatnya $y = 3(2)^2 - 13(2) + 8 = 12 - 26 + 8 = -6$. Persamaan garis singgung: $y - (-6) = -1(x - 2) \iff y + 6 = -x + 2 \iff y = -x - 4$.</sub>
- C. $y = x - 8$  
  <sub>Salah: Siswa menganggap gradien $\tan 135^\circ = 1$, bukan $-1$.</sub>
- D. $y = -x + 8$  
  <sub>Salah: Siswa salah menjumlahkan konstanta saat memindahkan nilai ordinat titik singgung.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung dari besar sudut:
$$m = \tan 135^\circ = -1$$

Langkah 2: Menentukan koordinat titik singgung melalui turunan kurva:
$$y' = 6x - 13$$
$$6x - 13 = -1 \iff 6x = 12 \iff x = 2$$
Substitusikan $x = 2$ ke persamaan kurva:
$$y = 3(2)^2 - 13(2) + 8 = 12 - 26 + 8 = -6$$
Titik singgung adalah $(2, -6)$.

Langkah 3: Menentukan persamaan garis singgung:
$$y - y_1 = m(x - x_1)$$
$$y - (-6) = -1(x - 2)$$
$$y + 6 = -x + 2$$
$$y = -x - 4$$
**Acuan:** siswa — siswa hal.162 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b02-c-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: kemonotonan kurva rasional*

Kurva fungsi rasional $f(x) = \frac{x}{x^2 + 4}$ akan turun pada interval ....

- A. $-2 < x < 2$  
  <sub>Salah: Siswa menentukan interval kurva naik ($f'(x) > 0$), bukan kurva turun.</sub>
- **B. $x < -2$ atau $x > 2$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = \frac{1(x^2 + 4) - x(2x)}{(x^2 + 4)^2} = \frac{4 - x^2}{(x^2 + 4)^2}$. Kurva turun saat $f'(x) < 0$. Karena penyebut $(x^2 + 4)^2 > 0$ untuk setiap $x \in \mathbb{R}$, syaratnya $4 - x^2 < 0 \iff x^2 - 4 > 0 \iff x < -2$ atau $x > 2$.</sub>
- C. $x < -4$ atau $x > 4$  
  <sub>Salah: Siswa salah memfaktorkan pembilang $4 - x^2$ menjadi $(x - 4)(x + 4)$.</sub>
- D. $-4 < x < 4$  
  <sub>Salah: Siswa keliru memfaktorkan bentuk pembilang serta terbalik menentukan tanda pertidaksamaan fungsi turun.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama fungsi pecahan menggunakan aturan hasil bagi:
$$u = x \implies u' = 1$$
$$v = x^2 + 4 \implies v' = 2x$$
$$f'(x) = \frac{u'v - uv'}{v^2} = \frac{1(x^2 + 4) - x(2x)}{(x^2 + 4)^2} = \frac{4 - x^2}{(x^2 + 4)^2}$$

Langkah 2: Menentukan syarat fungsi turun:
Syarat kurva turun adalah $f'(x) < 0$:
$$\frac{4 - x^2}{(x^2 + 4)^2} < 0$$
Karena penyebut $(x^2 + 4)^2$ selalu bernilai positif untuk semua bilangan real $x$, maka tanda pecahan sepenuhnya ditentukan oleh pembilang:
$$4 - x^2 < 0$$
$$x^2 - 4 > 0$$
$$(x - 2)(x + 2) > 0$$
Diperoleh interval $x < -2$ atau $x > 2$.
**Acuan:** siswa — siswa hal.152

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b02-c-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: percepatan partikel aplikasi turunan*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = t^3 - 6t^2 + 9t + 4$ ($s$ dalam meter dan $t$ dalam detik) untuk $t \ge 0$. Nilai $t$ ketika percepatan partikel sama dengan nol adalah ....

- A. $t = 4$ detik  
  <sub>Salah: Salah melakukan turunan kedua, menurunkannya menjadi $3t - 12 = 0$.</sub>
- B. $t = 1$ detik  
  <sub>Salah: Keliru mencari nilai $t$ saat kecepatan partikel nol ($v(t) = 0$ menghasilkan $t = 1$ atau $t = 3$).</sub>
- **C. $t = 2$ detik** ✅  
  <sub>Benar: Kecepatan $v(t) = s'(t) = 3t^2 - 12t + 9$, percepatan $a(t) = s''(t) = 6t - 12$. Percepatan sama dengan nol saat $6t - 12 = 0 \iff t = 2$ detik.</sub>
- D. $t = 3$ detik  
  <sub>Salah: Keliru mengambil akar lain dari persamaan kecepatan bernilai nol.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi kecepatan dan fungsi percepatan melalui turunan bertingkat.
$$v(t) = s'(t) = 3t^2 - 12t + 9$$
$$a(t) = v'(t) = s''(t) = 6t - 12$$

Langkah 2: Menghitung $t$ ketika percepatan sama dengan nol ($a(t) = 0$).
$$6t - 12 = 0$$
$$6t = 12$$
$$t = 2$$
Jadi, percepatan partikel sama dengan nol pada saat $t = 2$ detik.
**Acuan:** siswa — siswa hal.163 Latihan Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b02-c-medium-bt01-013
*variasi (angka) | C3 | 3 langkah | jenis: interval fungsi naik kurva kubik*

Interval nilai $x$ yang menyebabkan fungsi $f(x) = 2x^3 + 3x^2 - 36x + 5$ selalu naik adalah ....

- **A. $x < -3$ atau $x > 2$** ✅  
  <sub>Benar: Syarat fungsi naik adalah $f'(x) > 0$. $f'(x) = 6x^2 + 6x - 36 > 0 \iff x^2 + x - 6 > 0 \iff (x + 3)(x - 2) > 0$, sehingga $x < -3$ atau $x > 2$.</sub>
- B. $-3 < x < 2$  
  <sub>Salah: Menghitung interval fungsi turun saat $f'(x) < 0$.</sub>
- C. $x < -2$ atau $x > 3$  
  <sub>Salah: Salah dalam memfaktorkan persamaan kuadrat sehingga tanda akar tertukar menjadi $(x - 3)(x + 2)$.</sub>
- D. $-2 < x < 3$  
  <sub>Salah: Menghitung interval turun dari persamaan kuadrat yang salah difaktorkan.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama dari fungsi $f(x)$.
$$f'(x) = 6x^2 + 6x - 36$$

Langkah 2: Menetapkan syarat fungsi naik, yaitu $f'(x) > 0$.
$$6x^2 + 6x - 36 > 0$$
Bagi kedua ruas dengan $6$:
$$x^2 + x - 6 > 0$$
$$(x + 3)(x - 2) > 0$$

Langkah 3: Menentukan interval penyelesaian.
Pembuat nol adalah $x = -3$ dan $x = 2$. Menguji tanda pada garis bilangan menghasilkan nilai positif pada $x < -3$ atau $x > 2$.
Jadi, fungsi $f(x)$ selalu naik pada interval $x < -3$ atau $x > 2$.
**Acuan:** siswa — siswa hal.150 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b02-c-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: nilai balik minimum kurva derajat empat*

Nilai balik minimum dari kurva fungsi $f(x) = x^4 - 4x + 6$ adalah ....

- A. $6$  
  <sub>Salah: Mengambil nilai suku konstan fungsi (nilai pada $x = 0$).</sub>
- B. $1$  
  <sub>Salah: Menjawab nilai absis $x = 1$, bukan nilai balik minimumnya ($f(1)$).</sub>
- **C. $3$** ✅  
  <sub>Benar: $f'(x) = 4x^3 - 4 = 0 \implies x = 1$. Karena $f''(1) = 12(1)^2 = 12 > 0$, maka $x = 1$ menghasilkan nilai balik minimum yaitu $f(1) = 1^4 - 4(1) + 6 = 3$.</sub>
- D. $-3$  
  <sub>Salah: Kesalahan tanda dalam menghitung $1 - 4 + 6$.</sub>

**Pembahasan:** Langkah 1: Mencari titik stasioner dengan menyelesaikan $f'(x) = 0$.
$$f'(x) = 4x^3 - 4 = 0$$
$$4(x^3 - 1) = 0 \implies x = 1$$

Langkah 2: Mengonfirmasi jenis nilai balik menggunakan uji turunan kedua.
$$f''(x) = 12x^2$$
$$f''(1) = 12(1)^2 = 12 > 0$$
Karena $f''(1) > 0$, maka fungsi memiliki nilai balik minimum di $x = 1$.

Langkah 3: Menghitung nilai balik minimum dengan mensubstitusi $x = 1$ ke $f(x)$.
$$f(1) = (1)^4 - 4(1) + 6 = 1 - 4 + 6 = 3$$
Jadi, nilai balik minimum fungsi tersebut adalah $3$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b02-c-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: titik potong garis singgung terhadap sumbu koordinat*

Garis singgung kurva $y = x^2 - 6x + 5$ di titik dengan absis $x = 4$ memotong sumbu-$x$ pada koordinat ....

- **A. $\left(\frac{11}{2}, 0\right)$** ✅  
  <sub>Benar: Titik singgung adalah $(4, -3)$ dan gradien $m = y'(4) = 2(4) - 6 = 2$. Persamaan garis singgung $y - (-3) = 2(x - 4) \iff y = 2x - 11$. Memotong sumbu-$x$ saat $y = 0 \implies 2x - 11 = 0 \iff x = \frac{11}{2}$.</sub>
- B. $(0, -11)$  
  <sub>Salah: Menghitung koordinat titik potong garis singgung dengan sumbu-$y$, bukan sumbu-$x$.</sub>
- C. $(4, 0)$  
  <sub>Salah: Hanya mengambil absis titik singgung dan mengubah ordinatnya menjadi 0 tanpa menghitung titik potong garis singgung.</sub>
- D. $\left(-\frac{11}{2}, 0\right)$  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan ruas $2x - 11 = 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan ordinat titik singgung untuk absis $x = 4$.
$$y = 4^2 - 6(4) + 5 = 16 - 24 + 5 = -3$$
Titik singgungnya adalah $(4, -3)$.

Langkah 2: Menentukan kemiringan (gradien) garis singgung melalui turunan pertama.
$$y' = 2x - 6$$
$$m = y'(4) = 2(4) - 6 = 2$$

Langkah 3: Menyusun persamaan garis singgung di titik $(4, -3)$ dengan gradien $m = 2$.
$$y - y_1 = m(x - x_1)$$
$$y - (-3) = 2(x - 4)$$
$$y + 3 = 2x - 8$$
$$y = 2x - 11$$

Langkah 4: Menentukan titik potong garis singgung dengan sumbu-$x$ (syarat $y = 0$).
$$0 = 2x - 11$$
$$2x = 11 \implies x = \frac{11}{2}$$
Jadi, garis singgung memotong sumbu-$x$ pada koordinat $\left(\frac{11}{2}, 0\right)$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b02-c-medium-bt01-016
*variasi (angka) | C3 | 2 langkah | jenis: nilai ekstrem fungsi kuadrat*

Nilai ekstrem dan jenis titik ekstrem dari fungsi $f(x) = 2x^2 - 12x + 11$ adalah ....

- A. Nilai ekstrem minimum $11$ pada $x = 3$  
  <sub>Salah: Siswa menyangka nilai ekstrem adalah nilai konstanta kurva $c = 11$.</sub>
- B. Nilai ekstrem maksimum $-7$ pada $x = 3$  
  <sub>Salah: Siswa keliru mengidentifikasi jenis titik ekstrem kurva terbuka ke atas sebagai maksimum.</sub>
- C. Nilai ekstrem minimum $-7$ pada $x = -3$  
  <sub>Salah: Siswa salah tanda saat menyelesaikan persamaan stasioner $4x - 12 = 0$.</sub>
- **D. Nilai ekstrem minimum $-7$ pada $x = 3$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 4x - 12 = 0 \implies x = 3$. Karena $f''(x) = 4 > 0$, maka titik tersebut menghasilkan nilai minimum $f(3) = 2(3)^2 - 12(3) + 11 = 18 - 36 + 11 = -7$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai absis stasioner kurva.
$$f'(x) = 4x - 12$$
Fungsi diam saat $f'(x) = 0$:
$$4x - 12 = 0 \implies 4x = 12 \implies x = 3$$

Langkah 2: Menentukan jenis dan nilai ekstrem.
Turunan kedua: $f''(x) = 4 > 0$, sehingga menghasilkan nilai balik minimum.
Substitusikan $x = 3$ ke rumus fungsi $f(x)$:
$$f(3) = 2(3)^2 - 12(3) + 11 = 18 - 36 + 11 = -7$$
Jadi, nilai ekstremnya adalah minimum $-7$ pada $x = 3$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-13a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b02-c-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung ordinat tertentu*

Persamaan garis singgung pada kurva $y = x^2 - 6x + 14$ di titik yang berordinat $9$ dan memiliki absis $x < 3$ adalah ....

- A. $y = 4x + 5$  
  <sub>Salah: Siswa salah tanda saat menghitung gradien $m = 2(1) - 6 = 4$ bukan $-4$.</sub>
- B. $y = 4x - 11$  
  <sub>Salah: Siswa memilih absis yang salah yaitu $x = 5$ yang melanggar syarat $x < 3$.</sub>
- **C. $y = -4x + 13$** ✅  
  <sub>Benar: Untuk $y = 9$, diperoleh $x^2 - 6x + 14 = 9 \iff x^2 - 6x + 5 = 0$, sehingga $x = 1$ (karena $x < 3$). Gradien $m = y'(1) = 2(1) - 6 = -4$. Persamaan garisnya $y - 9 = -4(x - 1) \iff y = -4x + 13$.</sub>
- D. $y = -4x + 9$  
  <sub>Salah: Siswa lupa mengalikan pergeseran absis $-4(-1)$ saat menyusun bentuk eksplisit persamaan garis.</sub>

**Pembahasan:** Langkah 1: Menentukan absis titik singgung.
Substitusikan $y = 9$ ke persamaan kurva:
$$x^2 - 6x + 14 = 9$$
$$x^2 - 6x + 5 = 0$$
$$(x - 1)(x - 5) = 0$$
Diperoleh $x = 1$ atau $x = 5$. Karena disyaratkan $x < 3$, absis yang memenuhi adalah $x = 1$. Titik singgungnya adalah $(1, 9)$.

Langkah 2: Menghitung gradien garis singgung.
$$y' = 2x - 6$$
$$m = y'(1) = 2(1) - 6 = -4$$

Langkah 3: Menentukan persamaan garis singgung.
$$y - y_1 = m(x - x_1)$$
$$y - 9 = -4(x - 1)$$
$$y - 9 = -4x + 4$$
$$y = -4x + 13$$
**Acuan:** siswa — siswa hal.162 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b02-c-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: persamaan garis singgung kurva pecahan*

Persamaan garis singgung pada kurva $y = 4x - \frac{4}{x}$ di titik potong kurva dengan sumbu-$x$ positif adalah ....

- A. $y = 4x - 4$  
  <sub>Salah: Siswa salah saat menurunkan bentuk pecahan, menganggap turunan $-\frac{4}{x}$ adalah $0$ sehingga gradien dianggap $4$.</sub>
- B. $y = -8x + 8$  
  <sub>Salah: Siswa keliru menurunkan tanda dari $-\frac{4}{x}$ menjadi $-\frac{4}{x^2}$, sehingga salah menghasilkan gradien $m = 4 - 4 = 0$ atau keliru memberi tanda gradien $-8$.</sub>
- **C. $y = 8x - 8$** ✅  
  <sub>Benar: Titik potong sumbu-$x$ saat $y = 0 \implies 4x - \frac{4}{x} = 0 \iff 4x^2 - 4 = 0 \iff x = 1$ (karena $x > 0$), sehingga titik singgungnya adalah $(1, 0)$. Turunan fungsi adalah $y' = 4 + \frac{4}{x^2}$. Gradien di $x = 1$ adalah $m = y'(1) = 4 + \frac{4}{1^2} = 8$. Persamaan garis singgungnya: $y - 0 = 8(x - 1) \iff y = 8x - 8$.</sub>
- D. $y = 8x + 8$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik singgung saat menyusun persamaan garis singgung: $y - 0 = 8(x + 1)$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik singgung.
Titik potong kurva dengan sumbu-$x$ positif diperoleh saat $y = 0$:
$$4x - \frac{4}{x} = 0$$
$$4x^2 - 4 = 0 \implies x^2 = 1$$
Karena absis positif, maka $x = 1$. Jadi titik singgungnya adalah $(1, 0)$.

Langkah 2: Menentukan gradien garis singgung.
$$y = 4x - 4x^{-1}$$
$$m = y' = 4 - 4(-1)x^{-2} = 4 + \frac{4}{x^2}$$
Substitusikan $x = 1$:
$$m = 4 + \frac{4}{1^2} = 8$$

Langkah 3: Menentukan persamaan garis singgung.
$$y - y_1 = m(x - x_1)$$
$$y - 0 = 8(x - 1)$$
$$y = 8x - 8$$
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b02-c-medium-bt01-019
*orisinal | C3 | 2 langkah | jenis: interval kecepatan negatif partikel*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = 2t^3 - 15t^2 + 24t + 10$ ($s$ dalam meter dan $t$ dalam detik) untuk $t \ge 0$. Interval waktu $t$ saat kecepatan partikel bernilai negatif adalah ....

- A. $0 \le t < 1$ atau $t > 4$ detik  
  <sub>Salah: Siswa terbalik menentukan tanda pertidaksamaan sehingga mencari interval saat kecepatan bernilai positif.</sub>
- **B. $1 < t < 4$ detik** ✅  
  <sub>Benar: Fungsi kecepatan adalah $v(t) = s'(t) = 6t^2 - 30t + 24$. Kecepatan bernilai negatif jika $v(t) < 0 \iff 6(t^2 - 5t + 4) < 0 \iff 6(t - 1)(t - 4) < 0 \iff 1 < t < 4$ detik.</sub>
- C. $2 < t < 5$ detik  
  <sub>Salah: Siswa melakukan kesalahan faktorisasi bentuk kuadrat $t^2 - 5t + 4$ menjadi $(t - 2)(t - 5)$.</sub>
- D. $1 < t < 2$ detik  
  <sub>Salah: Siswa keliru memfaktorkan bentuk kuadrat atau membaginya secara tidak lengkap.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus fungsi kecepatan partikel.
Kecepatan partikel merupakan turunan pertama dari fungsi posisi:
$$v(t) = s'(t) = \frac{d}{dt}(2t^3 - 15t^2 + 24t + 10) = 6t^2 - 30t + 24$$

Langkah 2: Menentukan interval saat kecepatan bernilai negatif ($v(t) < 0$).
$$6t^2 - 30t + 24 < 0$$
Bagi kedua ruas dengan $6$:
$$t^2 - 5t + 4 < 0$$
$$(t - 1)(t - 4) < 0$$
Pembuat nol persamaan adalah $t = 1$ dan $t = 4$. Melalui uji garis bilangan, nilai negatif berada pada rentang antara kedua pembuat nol tersebut.
Jadi, kecepatan partikel bernilai negatif pada interval $1 < t < 4$ detik.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b02-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: penentuan koefisien kurva dari interval turun*

Grafik fungsi $f(x) = x^3 + ax^2 + bx + 7$ hanya turun pada interval $-2 < x < 4$. Nilai dari $a + b$ adalah ....

- A. $-10$  
  <sub>Salah: Siswa lupa mengalikan koefisien turunan dengan 3, menganggap $f'(x) = x^2 + ax + b$ sehingga diperoleh $a = -2$ dan $b = -8$, menghasilkan $a + b = -10$.</sub>
- B. $21$  
  <sub>Salah: Siswa salah tanda pada hasil kali akar persamaan kuadrat sehingga diperoleh $b = 24$, lalu dengan $a = -3$ didapatkan $a + b = 21$.</sub>
- C. $-21$  
  <sub>Salah: Siswa salah menerapkan tanda pada rumus jumlah akar persamaan kuadrat, menganggap $\frac{2a}{3} = 2 \implies a = 3$, sehingga $a + b = 3 + (-24) = -21$.</sub>
- **D. $-27$** ✅  
  <sub>Benar: Turunan pertama fungsi adalah $f'(x) = 3x^2 + 2ax + b$. Kurva turun ketika $f'(x) < 0$. Karena kurva hanya turun pada $-2 < x < 4$, maka $x = -2$ dan $x = 4$ adalah akar-akar dari $3x^2 + 2ax + b = 0$. Berdasarkan hubungan akar persamaan kuadrat: $x_1 + x_2 = -2 + 4 = 2 = -\frac{2a}{3} \implies 2a = -6 \implies a = -3$, dan $x_1 \cdot x_2 = -2 \cdot 4 = -8 = \frac{b}{3} \implies b = -24$. Sehingga nilai $a + b = -3 + (-24) = -27$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama fungsi.
$f'(x) = 3x^2 + 2ax + b$

Langkah 2: Menghubungkan batas interval fungsi turun dengan pembuat nol turunan.
Fungsi turun jika $f'(x) < 0$. Diketahui interval turun adalah $-2 < x < 4$, artinya $x_1 = -2$ dan $x_2 = 4$ merupakan akar-akar dari persamaan kuadrat $3x^2 + 2ax + b = 0$.

Langkah 3: Menentukan nilai $a$ dan $b$ menggunakan sifat akar kuadrat.
- Jumlah akar:
$$x_1 + x_2 = -\frac{2a}{3}$$
$$-2 + 4 = -\frac{2a}{3}$$
$$2 = -\frac{2a}{3} \implies 2a = -6 \implies a = -3$$

- Hasil kali akar:
$$x_1 \cdot x_2 = \frac{b}{3}$$
$$(-2)(4) = \frac{b}{3}$$
$$-8 = \frac{b}{3} \implies b = -24$$

Langkah 4: Menghitung nilai $a + b$.
$$a + b = -3 + (-24) = -27$$

Jadi, nilai $a + b$ adalah $-27$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b02-c-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: kemonotonan bersyarat parameter*

Misalkan kurva fungsi $f(x) = kx^3 + 6x^2 - 11$ selalu naik pada interval terbuka $0 < x < 4$. Batas nilai koefisien $k$ yang memenuhi adalah ....

- A. $k \le -1$  
  <sub>Salah: Siswa membalik tanda ketaksamaan saat membagi dengan $x$ padahal $x > 0$.</sub>
- **B. $k \ge -1$** ✅  
  <sub>Benar: Syarat fungsi naik adalah $f'(x) \ge 0$ untuk setiap $x \in (0, 4)$. $f'(x) = 3kx^2 + 12x = 3x(kx + 4)$. Karena $x > 0$, syarat menjadi $kx + 4 \ge 0 \iff kx \ge -4 \iff k \ge -\frac{4}{x}$. Nilai minimum $k$ diperoleh saat $-\frac{4}{x}$ mencapai nilai maksimum pada selang $(0, 4]$, yaitu saat $x = 4$ dengan nilai $-\frac{4}{4} = -1$. Sehingga harus dipenuhi $k \ge -1$.</sub>
- C. $k \ge 0$  
  <sub>Salah: Siswa keliru menganggap koefisien $x^3$ harus selalu positif agar fungsinya naik.</sub>
- D. $k \ge -4$  
  <sub>Salah: Siswa menyubstitusikan $x = 1$ alih-alih batas supremum $x = 4$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama kurva $f(x)$:
$f(x) = kx^3 + 6x^2 - 11$
$f'(x) = 3kx^2 + 12x$

Langkah 2: Menetapkan syarat fungsi naik pada selang $0 < x < 4$:
$f'(x) \ge 0 \implies 3x(kx + 4) \ge 0$

Langkah 3: Menyederhanakan pertidaksamaan karena pada interval $0 < x < 4$ nilai $3x > 0$:
$kx + 4 \ge 0 \iff kx \ge -4$
Karena $x > 0$, maka:
$k \ge -\frac{4}{x}$

Langkah 4: Menganalisis kondisi agar ketaksamaan berlaku untuk setiap $x \in (0, 4)$:
Agar $k \ge -\frac{4}{x}$ berlaku untuk seluruh $x \in (0, 4)$, nilai $k$ harus lebih besar atau sama dengan nilai tertinggi dari fungsi $g(x) = -\frac{4}{x}$ pada selang tersebut.
Fungsi $g(x) = -\frac{4}{x}$ bernilai monoton naik untuk $x > 0$. Nilai terbesarnya pada selang $(0, 4]$ dicapai pada batas kanan $x = 4$, yaitu:
$g(4) = -\frac{4}{4} = -1$
Dengan demikian, diperoleh batas nilai $k$ adalah $k \ge -1$.
**Acuan:** siswa — siswa hal.163 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b02-c-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: garis singgung melalui titik luar*

Garis lurus $g$ ditarik melalui titik $(0, -4)$ dan menyinggung parabola $y = x^2 - 2x$ di titik $P(x_0, y_0)$ dengan absis $x_0 > 0$. Persamaan garis $g$ tersebut adalah ....

- A. $y = -6x - 4$  
  <sub>Salah: Siswa mengambil solusi $x_0 = -2$ yang melanggar syarat $x_0 > 0$ sehingga gradien $m = 2(-2)-2 = -6$.</sub>
- B. $y = 4x - 4$  
  <sub>Salah: Siswa salah menghitung turunan pertama menjadi $2x$ alih-alih $2x - 2$.</sub>
- **C. $y = 2x - 4$** ✅  
  <sub>Benar: Gradien garis dari titik $(0, -4)$ ke titik singgung $(x_0, x_0^2 - 2x_0)$ adalah $m = \frac{(x_0^2 - 2x_0) - (-4)}{x_0 - 0}$. Dari turunan fungsi, $m = y'(x_0) = 2x_0 - 2$. Menyamakan kedua ekspresi: $2x_0 - 2 = \frac{x_0^2 - 2x_0 + 4}{x_0} \implies 2x_0^2 - 2x_0 = x_0^2 - 2x_0 + 4 \implies x_0^2 = 4$. Karena $x_0 > 0$, maka $x_0 = 2$. Gradien $m = 2(2) - 2 = 2$. Maka persamaan garis singgungnya adalah $y - (-4) = 2(x - 0) \implies y = 2x - 4$.</sub>
- D. $y = 2x + 4$  
  <sub>Salah: Siswa salah memasukkan tanda ordinat titik potong sumbu-$y$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat titik singgung $P$ dan gradien kurva melalui turunan:
Misalkan titik singgung adalah $P(x_0, y_0)$ pada kurva $y = x^2 - 2x$, maka $y_0 = x_0^2 - 2x_0$.
Turunan pertama: $y' = 2x - 2$, sehingga kemiringan garis di titik singgung adalah $m = 2x_0 - 2$.

Langkah 2: Menghitung gradien garis $g$ yang menghubungkan titik $(0, -4)$ dan $(x_0, y_0)$:
$m = \frac{y_0 - (-4)}{x_0 - 0} = \frac{x_0^2 - 2x_0 + 4}{x_0}$

Langkah 3: Menyamakan kedua nilai gradien:
$2x_0 - 2 = \frac{x_0^2 - 2x_0 + 4}{x_0}$
$2x_0^2 - 2x_0 = x_0^2 - 2x_0 + 4$
$x_0^2 = 4 \implies x_0 = 2 \text{ atau } x_0 = -2$
Karena disyaratkan $x_0 > 0$, maka dipilih $x_0 = 2$.

Langkah 4: Menentukan gradien garis $g$:
$m = 2(2) - 2 = 2$

Langkah 5: Menyusun persamaan garis singgung $g$:
Melalui titik $(0, -4)$ dengan gradien $m = 2$:
$y - (-4) = 2(x - 0) \iff y + 4 = 2x \iff y = 2x - 4$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b02-c-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: karakteristik titik balik polinomial*

Fungsi kubik $f(x) = 2x^3 - 3(a+1)x^2 + 6ax + 10$ dengan konstanta $a > 1$ memiliki titik balik maksimum di $(x_1, f(x_1))$ dan titik balik minimum di $(x_2, f(x_2))$. Jika selisih absis $x_2 - x_1 = 3$, maka nilai konstanta $a$ adalah ....

- **A. $4$** ✅  
  <sub>Benar: Turunan pertama: $f'(x) = 6x^2 - 6(a+1)x + 6a = 6(x^2 - (a+1)x + a) = 6(x - 1)(x - a)$. Titik stasioner adalah $x = 1$ dan $x = a$. Turunan kedua: $f''(x) = 12x - 6(a+1)$. Untuk $x = 1$, $f''(1) = 12 - 6a - 6 = 6(1 - a)$. Karena $a > 1$, maka $f''(1) < 0$ (titik balik maksimum), sehingga $x_1 = 1$. Untuk $x = a$, $f''(a) = 12a - 6a - 6 = 6(a - 1) > 0$ (titik balik minimum), sehingga $x_2 = a$. Dari hubungan $x_2 - x_1 = 3$, diperoleh $a - 1 = 3 \implies a = 4$.</sub>
- B. $5$  
  <sub>Salah: Siswa salah dalam pemfaktoran turunan pertama sehingga menganggap salah satu akarnya adalah 2.</sub>
- C. $-2$  
  <sub>Salah: Siswa menukar posisi $x_1$ dan $x_2$ sehingga menuliskan $1 - a = 3 \implies a = -2$ dan mengabaikan syarat $a > 1$.</sub>
- D. $2$  
  <sub>Salah: Siswa salah menghitung selisih dengan formula $a - x_1 = 1$ bukan 3.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama dari fungsi $f(x)$:
$f(x) = 2x^3 - 3(a+1)x^2 + 6ax + 10$
$f'(x) = 6x^2 - 6(a+1)x + 6a$

Langkah 2: Menentukan absis titik stasioner dengan $f'(x) = 0$:
$6(x^2 - (a+1)x + a) = 0$
$6(x - 1)(x - a) = 0$
Diperoleh pembuat nol $x = 1$ atau $x = a$.

Langkah 3: Menguji jenis titik balik menggunakan turunan kedua:
$f''(x) = 12x - 6(a+1)$
- Untuk $x = 1$: $f''(1) = 12(1) - 6a - 6 = 6 - 6a = 6(1 - a)$. Karena diketahui $a > 1$, maka $f''(1) < 0$. Ini membuktikan bahwa di $x = 1$ terjadi nilai balik maksimum, sehingga $x_1 = 1$.
- Untuk $x = a$: $f''(a) = 12(a) - 6a - 6 = 6a - 6 = 6(a - 1) > 0$. Ini membuktikan bahwa di $x = a$ terjadi nilai balik minimum, sehingga $x_2 = a$.

Langkah 4: Menggunakan kondisi selisih absis yang diketahui pada soal:
$x_2 - x_1 = 3$
$a - 1 = 3$

Langkah 5: Menyelesaikan nilai $a$:
$a = 4$
Nilai $a = 4$ memenuhi syarat awal $a > 1$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b02-c-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: kemonotonan fungsi trigonometri*

Grafik fungsi trigonometri $f(x) = \cos^2 x - 2\sin x$ pada interval $0 \le x \le \pi$ akan selalu turun pada interval ....

- A. $\frac{\pi}{4} < x < \frac{3\pi}{4}$  
  <sub>Salah: Siswa keliru mengira turunan melibatkan sudut rangkap $\sin 2x = 0$ di kuadran pertama dan kedua.</sub>
- **B. $0 \le x < \frac{\pi}{2}$** ✅  
  <sub>Benar: Turunan pertama adalah $f'(x) = 2\cos x (-\sin x) - 2\cos x = -2\cos x(\sin x + 1)$. Syarat kurva turun adalah $f'(x) < 0 \implies -2\cos x(\sin x + 1) < 0$. Pada selang $0 \le x \le \pi$, nilai $\sin x \ge 0$, sehingga faktor $(\sin x + 1) \ge 1 > 0$ (selalu bernilai positif definit). Akibatnya, pertidaksamaan bergantung pada $-2\cos x < 0 \iff \cos x > 0$. Pada interval $0 \le x \le \pi$, nilai $\cos x > 0$ dipenuhi pada $0 \le x < \frac{\pi}{2}$.</sub>
- C. $\frac{\pi}{2} < x \le \pi$  
  <sub>Salah: Siswa tidak membalik tanda pertidaksamaan saat membagi dengan bilangan negatif $-2$.</sub>
- D. $0 < x < \pi$  
  <sub>Salah: Siswa mengabaikan faktor $\cos x$ dan hanya meninjau tanda $-2$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama dari fungsi $f(x)$:
$f(x) = \cos^2 x - 2\sin x$
$f'(x) = 2\cos x \cdot (-\sin x) - 2\cos x$
$f'(x) = -2\sin x \cos x - 2\cos x$

Langkah 2: Memfaktorkan turunan pertama:
$f'(x) = -2\cos x(\sin x + 1)$

Langkah 3: Menetapkan syarat fungsi turun:
$f'(x) < 0 \implies -2\cos x(\sin x + 1) < 0$

Langkah 4: Menganalisis sifat tanda dari faktor $(\sin x + 1)$ pada domain $0 \le x \le \pi$:
Pada interval $0 \le x \le \pi$, nilai $\sin x$ selalu berada dalam rentang $0 \le \sin x \le 1$.
Akibatnya, $(\sin x + 1) \ge 1 > 0$ untuk setiap $x \in [0, \pi]$ (definit positif).

Langkah 5: Menyederhanakan pertidaksamaan dan menentukan interval:
Karena $(\sin x + 1) > 0$, kedua ruas dapat dibagi dengan $(\sin x + 1)$:
$-2\cos x < 0$
Membagi kedua ruas dengan $-2$ (tanda ketidaksamaan berbalik):
$\cos x > 0$
Pada domain $0 \le x \le \pi$, fungsi kosinus bernilai positif di Kuadran I, yaitu:
$0 \le x < \frac{\pi}{2}$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b02-c-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: garis singgung memotong kurva kembali*

Garis singgung pada kurva $y = x^3 - 6x$ di titik $P(2, -4)$ memotong kembali kurva tersebut di titik $Q(x_Q, y_Q)$. Nilai dari $x_Q + y_Q$ adalah ....

- A. $44$  
  <sub>Salah: Salah menentukan tanda absis perpotongan kembali menjadi $x_Q = 4$ dan $y_Q = 40$.</sub>
- B. $-4$  
  <sub>Salah: Hanya menghitung nilai absis $x_Q$ dan lupa menjumlahkannya dengan nilai ordinat $y_Q$.</sub>
- **C. $-44$** ✅  
  <sub>Benar: Gradien garis singgung di titik $P(2, -4)$ adalah $m = y'(2) = 3(2)^2 - 6 = 6$, sehingga garisnya $y = 6x - 16$. Substitusi ke kurva menghasilkan $x^3 - 12x + 16 = 0$. Karena bersinggungan di $x = 2$, bentuk faktornya $(x - 2)^2(x + 4) = 0$, sehingga $x_Q = -4$. Ordinatnya $y_Q = 6(-4) - 16 = -40$. Maka $x_Q + y_Q = -4 + (-40) = -44$.</sub>
- D. $-36$  
  <sub>Salah: Keliru menghitung ordinat $y_Q$ sebagai $-32$ akibat salah mengalikan gradien.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung di titik $P(2, -4)$:
$y = x^3 - 6x$
$y' = 3x^2 - 6$
$m = y'(2) = 3(2)^2 - 6 = 12 - 6 = 6$

Langkah 2: Menentukan persamaan garis singgung melalui titik $P(2, -4)$:
$y - y_1 = m(x - x_1)$
$y - (-4) = 6(x - 2)$
$y + 4 = 6x - 12$
$y = 6x - 16$

Langkah 3: Menentukan titik potong garis singgung dengan kurva $y = x^3 - 6x$:
$x^3 - 6x = 6x - 16$
$x^3 - 12x + 16 = 0$

Langkah 4: Karena garis menyinggung kurva di $x = 2$, maka $(x - 2)^2$ merupakan faktor dari suku banyak tersebut:
$(x - 2)^2 (x - x_Q) = (x^2 - 4x + 4)(x - x_Q) = x^3 - 12x + 16$
Diperoleh $-4 - x_Q = 0$ atau $4(-x_Q) = 16 \implies x_Q = -4$

Langkah 5: Menentukan ordinat $y_Q$ dan menghitung jumlahnya:
$y_Q = 6(-4) - 16 = -24 - 16 = -40$
Nilai $x_Q + y_Q = -4 + (-40) = -44$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b02-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: kecekungan kurva berparameter*

Diberikan fungsi polinomial berderajat empat $f(x) = \frac{1}{12}x^4 - \frac{k}{3}x^3 + \frac{9}{2}x^2 + 2x - 1$ dengan $k$ adalah suatu konstanta bilangan bulat. Agar grafik fungsi $f(x)$ selalu cekung ke atas pada seluruh garis bilangan real $\mathbb{R}$ (sehingga kurva tidak memiliki titik belok), banyaknya nilai bilangan bulat $k$ yang memenuhi adalah ....

- **A. $7$** ✅  
  <sub>Benar: Turunan kedua adalah $f''(x) = x^2 - 2kx + 9$. Kurva selalu cekung ke atas jika $f''(x) \ge 0$ untuk seluruh $x \in \mathbb{R}$. Syaratnya adalah diskriminan $D \le 0$, yaitu $(-2k)^2 - 4(1)(9) \le 0 \implies 4k^2 - 36 \le 0 \implies k^2 \le 9 \implies -3 \le k \le 3$. Bilangan bulat yang memenuhi adalah $\{-3, -2, -1, 0, 1, 2, 3\}$, berjumlah 7.</sub>
- B. $3$  
  <sub>Salah: Hanya menghitung nilai bilangan bulat positif untuk $k$ saja ($1, 2, 3$).</sub>
- C. $6$  
  <sub>Salah: Lupa mengikutsertakan nilai $k = 0$ sebagai salah satu bilangan bulat yang memenuhi.</sub>
- D. $5$  
  <sub>Salah: Menggunakan pertidaksamaan tegas $D < 0$ sehingga $k = -3$ dan $k = 3$ tidak dihitung.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama dari $f(x)$:
$f(x) = \frac{1}{12}x^4 - \frac{k}{3}x^3 + \frac{9}{2}x^2 + 2x - 1$
$f'(x) = \frac{1}{3}x^3 - kx^2 + 9x + 2$

Langkah 2: Menentukan turunan kedua dari $f(x)$:
$f''(x) = x^2 - 2kx + 9$

Langkah 3: Kurva $f(x)$ selalu cekung ke atas di seluruh $\mathbb{R}$ apabila $f''(x) \ge 0$ untuk setiap $x \in \mathbb{R}$. Karena koefisien dari suku $x^2$ sudah bernilai positif ($1 > 0$), syarat definit tak-negatif adalah diskriminan $D \le 0$:
$D = b^2 - 4ac \le 0$
$(-2k)^2 - 4(1)(9) \le 0$
$4k^2 - 36 \le 0$
$k^2 \le 9$
$-3 \le k \le 3$

Langkah 4: Menghitung banyaknya nilai bilangan bulat $k$ yang memenuhi:
Nilai $k \in \{-3, -2, -1, 0, 1, 2, 3\}$.
Banyaknya nilai bilangan bulat $k$ adalah 7.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b02-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: kemonotonan kurva berparameter definit*

Diberikan kurva fungsi $f(x) = \frac{1}{3}x^3 - (m-1)x^2 + (m+5)x - 10$ dengan $m$ adalah konstanta bilangan bulat. Agar fungsi $f(x)$ tidak pernah turun untuk setiap bilangan real $x$, banyaknya nilai $m$ yang memenuhi adalah ....

- A. $4$  
  <sub>Salah: Siswa hanya menghitung bilangan bulat positif $\{1, 2, 3, 4\}$.</sub>
- B. $7$  
  <sub>Salah: Siswa salah memfaktorkan bentuk kuadrat menjadi $(m-5)(m+1) \le 0$.</sub>
- C. $5$  
  <sub>Salah: Siswa lupa mengikutsertakan bilangan bulat $0$ atau salah menghitung panjang interval tertutup.</sub>
- **D. $6$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = x^2 - 2(m-1)x + (m+5)$. Syarat fungsi tidak pernah turun pada $\mathbb{R}$ adalah $f'(x) \ge 0$ untuk setiap $x$. Karena koefisien $x^2$ positif ($a = 1 > 0$), syaratnya adalah diskriminan $D \le 0$. Didapat $4(m-1)^2 - 4(1)(m+5) \le 0 \iff m^2 - 3m - 4 \le 0 \iff (m-4)(m+1) \le 0$. Nilai $m$ memenuhi $-1 \le m \le 4$. Himpunan bilangan bulatnya $\{-1, 0, 1, 2, 3, 4\}$ berjumlah 6.</sub>

**Pembahasan:** Agar $f(x)$ tidak pernah turun untuk setiap $x \in \mathbb{R}$, maka harus dipenuhi $f'(x) \ge 0$ untuk setiap $x \in \mathbb{R}$.

Turunan pertama:
$f'(x) = x^2 - 2(m-1)x + (m+5)$

Bentuk kuadrat $f'(x)$ memiliki koefisien $x^2$ bernilai $1 > 0$. Agar selalu non-negatif, diskriminan kuadrat harus bernilai $D \le 0$:
$D = b^2 - 4ac \le 0$
$[-2(m-1)]^2 - 4(1)(m+5) \le 0$
$4(m^2 - 2m + 1) - 4(m + 5) \le 0$
Bagi kedua ruas dengan 4:
$m^2 - 2m + 1 - m - 5 \le 0$
$m^2 - 3m - 4 \le 0$
$(m - 4)(m + 1) \le 0$

Penyelesaian pertidaksamaan:
$-1 \le m \le 4$

Nilai bilangan bulat $m$ yang memenuhi adalah $\{-1, 0, 1, 2, 3, 4\}$, yang totalnya ada 6 nilai.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b02-c-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: pasangan garis singgung dari titik asal*

Dari titik asal $O(0, 0)$ ditarik dua garis lurus yang menyinggung kurva parabola $y = x^2 - 4x + 5$. Jika kedua garis singgung tersebut berturut-turut mempunyai gradien $m_1$ dan $m_2$, maka nilai dari $(m_1 - m_2)^2$ adalah ....

- A. $40$  
  <sub>Salah: Siswa salah melakukan operasi kuadrat suku $4\sqrt{5}$.</sub>
- B. $20$  
  <sub>Salah: Siswa lupa faktor 2 pada selisih gradien sehingga hanya mengkuadratkan $2\sqrt{5}$ menjadi 20.</sub>
- C. $96$  
  <sub>Salah: Siswa menjumlahkan $4^2 + (4\sqrt{5})^2$ karena salah menjabarkan kuadrat suku aljabar.</sub>
- **D. $80$** ✅  
  <sub>Benar: Misal titik singgung $(t, t^2 - 4t + 5)$. Gradien garis singgung $m = 2t - 4$. Persamaan garis singgung melalui $(0, 0)$ adalah $y = mx$, sehingga substitusi titik singgung menghasilkan $t^2 - 4t + 5 = (2t - 4)t \implies t^2 - 4t + 5 = 2t^2 - 4t \implies t^2 = 5 \implies t = \pm\sqrt{5}$. Gradien masing-masing adalah $m_1 = 2\sqrt{5} - 4$ dan $m_2 = -2\sqrt{5} - 4$. Selisihnya $m_1 - m_2 = 4\sqrt{5}$, sehingga $(m_1 - m_2)^2 = (4\sqrt{5})^2 = 80$.</sub>

**Pembahasan:** Misalkan titik singgung pada parabola adalah $P(t, t^2 - 4t + 5)$.
Turunan kurva menentukan gradien garis singgung:
$y' = 2x - 4 \implies m = 2t - 4$

Persamaan garis singgung di titik $P$ adalah:
$y - (t^2 - 4t + 5) = (2t - 4)(x - t)$

Karena garis singgung ditarik melalui titik asal $O(0, 0)$, substitusikan $x = 0$ dan $y = 0$:
$0 - (t^2 - 4t + 5) = (2t - 4)(0 - t)$
$-t^2 + 4t - 5 = -2t^2 + 4t$
$t^2 - 5 = 0 \implies t = \pm\sqrt{5}$

Kedua nilai gradien garis singgung:
$m_1 = 2\sqrt{5} - 4$
$m_2 = -2\sqrt{5} - 4$

Maka selisih kedua gradien:
$m_1 - m_2 = (2\sqrt{5} - 4) - (-2\sqrt{5} - 4) = 4\sqrt{5}$

Nilai dari $(m_1 - m_2)^2$:
$(4\sqrt{5})^2 = 16 \times 5 = 80$
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b02-c-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: syarat kecekungan kurva berparameter*

Grafik fungsi polinomial berderajat empat $f(x) = x^4 - 4x^3 + 6kx^2 - 8x + 3$ selalu cekung ke atas pada seluruh garis bilangan real $\mathbb{R}$ jika dan hanya jika nilai konstanta $k$ memenuhi batasan ....

- A. $k > 0$  
  <sub>Salah: Siswa hanya mensyaratkan koefisien $k$ positif tanpa memperhitungkan diskriminan.</sub>
- B. $k \le 1$  
  <sub>Salah: Siswa membalik tanda pertidaksamaan saat menyelesaikan diskriminan.</sub>
- C. $k \ge 2$  
  <sub>Salah: Siswa salah menghitung rumus diskriminan $b^2 - 2ac$ bukan $b^2 - 4ac$.</sub>
- **D. $k \ge 1$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 4x^3 - 12x^2 + 12kx - 8$. Turunan kedua $f''(x) = 12x^2 - 24x + 12k = 12(x^2 - 2x + k)$. Grafik selalu cekung ke atas jika $f''(x) \ge 0$ untuk setiap $x \in \mathbb{R}$. Syarat agar bentuk kuadrat definit tak-negatif adalah koefisien utama positif ($1 > 0$) dan diskriminan $D \le 0$. Dari $x^2 - 2x + k$, $D = (-2)^2 - 4(1)(k) = 4 - 4k \le 0 \implies k \ge 1$.</sub>

**Pembahasan:** Kurva fungsi kontinu selalu cekung ke atas pada $\mathbb{R}$ apabila turunan keduanya memenuhi $f''(x) \ge 0$ untuk setiap $x \in \mathbb{R}$.

Menentukan turunan pertama dan kedua:
$f'(x) = 4x^3 - 12x^2 + 12kx - 8$
$f''(x) = 12x^2 - 24x + 12k$

Bagi fungsi turunan kedua dengan 12:
$g(x) = x^2 - 2x + k$

Agar $x^2 - 2x + k \ge 0$ untuk setiap $x \in \mathbb{R}$, karena koefisien $x^2$ adalah $1 > 0$, maka diskriminannya harus memenuhi $D \le 0$:
$D = (-2)^2 - 4(1)(k) \le 0$
$4 - 4k \le 0$
$-4k \le -4$
$k \ge 1$
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b02-c-hard-bt01-010
*variasi (angka) | C5 | 5 langkah | jenis: persamaan garis singgung titik potong kurva*

Persamaan garis singgung pada kurva $y = 6x^2 - 11x - 8$ di titik potongnya dengan garis $y = 9x - 14$ yang mempunyai absis bilangan bulat adalah ....

- A. $y = 25x - 88$  
  <sub>Salah: Siswa salah memasukkan tanda saat mengalikan $25 \times (-3)$ menjadi $-75$ lalu mengurangkan lagi dengan $13$ bukannya menambahkan.</sub>
- B. $y = -7x + 34$  
  <sub>Salah: Siswa salah menggunakan absis pecahan $x = \frac{1}{3}$ yang menghasilkan gradien $m = 12\left(\frac{1}{3}\right) - 11 = -7$.</sub>
- **C. $y = 25x - 62$** ✅  
  <sub>Benar: Menyamakan kedua persamaan: $6x^2 - 11x - 8 = 9x - 14 \iff 6x^2 - 20x + 6 = 0 \iff 2(3x - 1)(x - 3) = 0$. Diperoleh absis bilangan bulat $x = 3$. Ordinat titik singgung adalah $y = 9(3) - 14 = 13$, sehingga titik singgungnya $(3, 13)$. Turunan kurva adalah $y' = 12x - 11$. Gradien di $x = 3$ adalah $m = 12(3) - 11 = 25$. Persamaan garis singgung: $y - 13 = 25(x - 3) \iff y = 25x - 62$.</sub>
- D. $y = 9x - 14$  
  <sub>Salah: Siswa keliru menganggap garis potong yang diberikan pada soal merupakan garis singgungnya.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong kurva dan garis.
$$6x^2 - 11x - 8 = 9x - 14$$
$$6x^2 - 20x + 6 = 0$$
$$2(3x^2 - 10x + 3) = 0$$
$$2(3x - 1)(x - 3) = 0$$
Diperoleh $x = \frac{1}{3}$ atau $x = 3$.

Langkah 2: Memilih absis bilangan bulat, yaitu $x = 3$.
Substitusikan ke persamaan garis untuk mencari ordinat:
$$y = 9(3) - 14 = 27 - 14 = 13$$
Titik singgung adalah $(3, 13)$.

Langkah 3: Menentukan turunan pertama kurva untuk menghitung gradien garis singgung.
$$y' = \frac{d}{dx}(6x^2 - 11x - 8) = 12x - 11$$

Langkah 4: Menghitung gradien di titik $x = 3$.
$$m = y'(3) = 12(3) - 11 = 36 - 11 = 25$$

Langkah 5: Menyusun persamaan garis singgung melalui $(3, 13)$ dengan gradien $m = 25$.
$$y - y_1 = m(x - x_1)$$
$$y - 13 = 25(x - 3)$$
$$y - 13 = 25x - 75$$
$$y = 25x - 62$$
**Acuan:** siswa — siswa hal.162 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b02-c-hard-bt01-011
*variasi (angka) | C5 | 5 langkah | jenis: titik balik kurva polinomial*

Titik balik maksimum dan titik balik minimum dari grafik fungsi $f(x) = 2x^3 - 21x^2 + 60x - 11$ berturut-turut adalah ....

- **A. $(2, 41)$ dan $(5, 14)$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 6x^2 - 42x + 60 = 6(x - 2)(x - 5) = 0$ menghasilkan titik stasioner $x = 2$ dan $x = 5$. Turunan kedua $f''(x) = 12x - 42$. Untuk $x = 2$, $f''(2) = -18 < 0$ (titik balik maksimum) dengan $f(2) = 2(8) - 21(4) + 60(2) - 11 = 41$. Untuk $x = 5$, $f''(5) = 18 > 0$ (titik balik minimum) dengan $f(5) = 2(125) - 21(25) + 60(5) - 11 = 14$.</sub>
- B. $(5, 14)$ dan $(2, 41)$  
  <sub>Salah: Siswa tertukar antara titik balik maksimum dan minimum karena keliru menafsirkan uji turunan kedua.</sub>
- C. $(2, 41)$ dan $(5, -14)$  
  <sub>Salah: Siswa salah melakukan operasi aritmetika saat menghitung nilai $f(5)$ sehingga menghasilkan nilai bertanda negatif.</sub>
- D. $(2, 52)$ dan $(5, 25)$  
  <sub>Salah: Siswa lupa mengalikan konstanta $-11$ pada fungsi asal ketika menyubstitusikan absis.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama fungsi $f(x)$.
$$f'(x) = 6x^2 - 42x + 60$$

Langkah 2: Menentukan pembuat nol $f'(x)$ (titik stasioner).
$$6(x^2 - 7x + 10) = 0$$
$$6(x - 2)(x - 5) = 0$$
Diperoleh absis stasioner $x = 2$ atau $x = 5$.

Langkah 3: Menggunakan turunan kedua untuk menguji jenis titik balik.
$$f''(x) = 12x - 42$$
Untuk $x = 2$: $f''(2) = 12(2) - 42 = -18 < 0$, maka di $x = 2$ terjadi titik balik maksimum.
Untuk $x = 5$: $f''(5) = 12(5) - 42 = 18 > 0$, maka di $x = 5$ terjadi titik balik minimum.

Langkah 4: Menghitung nilai fungsi untuk masing-masing titik stasioner.
$$f(2) = 2(2)^3 - 21(2)^2 + 60(2) - 11 = 16 - 84 + 120 - 11 = 41$$
$$f(5) = 2(5)^3 - 21(5)^2 + 60(5) - 11 = 250 - 525 + 300 - 11 = 14$$

Langkah 5: Menyimpulkan koordinat titik balik.
Titik balik maksimum adalah $(2, 41)$ dan titik balik minimum adalah $(5, 14)$.
**Acuan:** pretest — kelas12_tl-b02-p0163-latihan-soal-aplikasi-turunan-fungsi-11a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b02-c-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: garis singgung tegak lurus fungsi rasional*

Garis singgung kurva fungsi rasional $f(x) = \frac{x + 2}{x - 1}$ ($x \ne 1$) tegak lurus terhadap garis $3x - y + 7 = 0$. Jika garis singgung tersebut memotong sumbu-$y$ di titik berordinat positif, maka persamaan garis singgung tersebut adalah ....

- A. $3x - y - 10 = 0$  
  <sub>Salah: Siswa keliru menggunakan gradien sejajar $m = 3$ alih-alih tegak lurus $m = -\frac{1}{3}$.</sub>
- B. $x + 3y + 2 = 0$  
  <sub>Salah: Siswa memilih titik singgung $x = -2$ yang menghasilkan titik potong sumbu-$y$ negatif $\left(0, -\frac{2}{3}\right)$ sehingga melanggar syarat soal.</sub>
- **C. $x + 3y - 10 = 0$** ✅  
  <sub>Benar: Garis $3x - y + 7 = 0$ memiliki gradien $m_1 = 3$. Garis singgung tegak lurus garis tersebut sehingga $m = -\frac{1}{3}$. Turunan $f'(x) = \frac{1(x - 1) - 1(x + 2)}{(x - 1)^2} = -\frac{3}{(x - 1)^2}$. Menyamakan gradien: $-\frac{3}{(x - 1)^2} = -\frac{1}{3} \iff (x - 1)^2 = 9$, sehingga $x - 1 = 3 \implies x = 4$ atau $x - 1 = -3 \implies x = -2$. Untuk $x = 4$, $f(4) = \frac{6}{3} = 2$. Persamaan garisnya $y - 2 = -\frac{1}{3}(x - 4) \iff x + 3y - 10 = 0$ dengan titik potong sumbu-$y$ di $\left(0, \frac{10}{3}\right)$ (positif). Untuk $x = -2$, $f(-2) = 0$, garisnya $y - 0 = -\frac{1}{3}(x + 2) \iff x + 3y + 2 = 0$ dengan titik potong sumbu-$y$ di $\left(0, -\frac{2}{3}\right)$ (negatif). Jadi yang memenuhi adalah $x + 3y - 10 = 0$.</sub>
- D. $x + 3y - 6 = 0$  
  <sub>Salah: Siswa salah menyubstitusikan koordinat titik $(4, 2)$ ke dalam rumus persamaan garis singgung.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung.
Persamaan garis $3x - y + 7 = 0 \iff y = 3x + 7$, maka $m_1 = 3$.
Karena garis singgung tegak lurus garis tersebut, maka:
$$m \cdot m_1 = -1 \implies m = -\frac{1}{3}$$

Langkah 2: Menentukan turunan $f'(x)$ menggunakan aturan pembagian turunan.
$$f'(x) = \frac{(1)(x - 1) - (x + 2)(1)}{(x - 1)^2} = \frac{-3}{(x - 1)^2}$$

Langkah 3: Menentukan absis titik singgung.
$$-\frac{3}{(x - 1)^2} = -\frac{1}{3}$$
$$(x - 1)^2 = 9$$
$$x - 1 = 3 \implies x_1 = 4$$
$$x - 1 = -3 \implies x_2 = -2$$

Langkah 4: Menentukan ordinat dan persamaan garis singgung untuk masing-masing titik.
Untuk $x_1 = 4$:
$$y_1 = f(4) = \frac{4 + 2}{4 - 1} = \frac{6}{3} = 2$$
Persamaan garis:
$$y - 2 = -\frac{1}{3}(x - 4) \iff 3y - 6 = -x + 4 \iff x + 3y - 10 = 0$$
Titik potong sumbu-$y$ ($x = 0$): $3y - 10 = 0 \implies y = \frac{10}{3} > 0$ (memenuhi syarat).

Untuk $x_2 = -2$:
$$y_2 = f(-2) = \frac{-2 + 2}{-2 - 1} = 0$$
Persamaan garis:
$$y - 0 = -\frac{1}{3}(x + 2) \iff 3y = -x - 2 \iff x + 3y + 2 = 0$$
Titik potong sumbu-$y$ ($x = 0$): $3y + 2 = 0 \implies y = -\frac{2}{3} < 0$ (tidak memenuhi).

Langkah 5: Jadi, persamaan garis singgung yang memenuhi adalah $x + 3y - 10 = 0$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b02-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: titik kurva terdekat terhadap garis*

Titik pada kurva parabola $f(x) = x^2 - 6x + 10$ yang memiliki jarak paling dekat terhadap garis $4x - y - 19 = 0$ adalah ....

- A. $(5, 1)$  
  <sub>Salah: Siswa benar menemukan $x = 5$, namun salah memasukkan nilai ke fungsi menjadi $5^2 - 6(5) + 10 = -1$ lalu mengubah tanda ke positif.</sub>
- B. $\left(\frac{5}{2}, \frac{5}{4}\right)$  
  <sub>Salah: Siswa membuat kesalahan saat menurunkan fungsi sehingga turunan disamakan dengan gradien tegak lurus.</sub>
- C. $(3, 1)$  
  <sub>Salah: Siswa keliru mencari titik puncak parabola ($f'(x) = 0$) alih-alih titik dengan gradien garis yang bersesuaian.</sub>
- **D. $(5, 5)$** ✅  
  <sub>Benar: Garis $4x - y - 19 = 0$ memiliki gradien $m = 4$. Jarak terdekat kurva ke garis tercapai di titik singgung yang garis singgungnya sejajar dengan garis tersebut, sehingga turunan kurva bernilai $4$. Turunan kurva adalah $f'(x) = 2x - 6$. Menyamakan nilai gradien: $2x - 6 = 4 \iff 2x = 10 \iff x = 5$. Ordinat titik tersebut adalah $f(5) = 5^2 - 6(5) + 10 = 25 - 30 + 10 = 5$. Jadi, titik terdekatnya adalah $(5, 5)$.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis yang diberikan.
Persamaan garis: $4x - y - 19 = 0 \iff y = 4x - 19$, sehingga kemiringan garis adalah $m = 4$.

Langkah 2: Memahami kondisi jarak terdekat.
Jarak terdekat dari kurva mulus ke garis lurus terjadi di titik di mana garis singgung kurva sejajar dengan garis tersebut, yaitu ketika $f'(x) = m = 4$.

Langkah 3: Menghitung absis titik singgung.
$$f'(x) = \frac{d}{dx}(x^2 - 6x + 10) = 2x - 6$$
$$2x - 6 = 4$$
$$2x = 10 \implies x = 5$$

Langkah 4: Menentukan ordinat titik singgung.
$$f(5) = (5)^2 - 6(5) + 10 = 25 - 30 + 10 = 5$$
Jadi, koordinat titik pada kurva yang berjarak paling dekat ke garis tersebut adalah $(5, 5)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b02-c-hard-bt01-014
*variasi (angka) | C5 | 5 langkah | jenis: analisis gerak kinematika turunan*

Sebuah partikel bergerak lurus dengan persamaan posisi $s(t) = t^3 - 9t^2 + 24t + 5$ ($s$ dalam meter dan $t$ dalam detik) untuk rentang waktu $t \ge 0$. Gerak partikel tersebut mengalami perlambatan (kecepatan dan percepatan memiliki arah yang berlawanan) pada selang waktu ....

- A. $2 < t < 3$ atau $t > 4$  
  <sub>Salah: Menentukan interval saat partikel dipercepat ($v(t) \cdot a(t) > 0$) bukannya saat diperlambat.</sub>
- **B. $0 \le t < 2$ atau $3 < t < 4$** ✅  
  <sub>Benar: Fungsi kecepatan adalah $v(t) = s'(t) = 3(t - 2)(t - 4)$ dan percepatan adalah $a(t) = v'(t) = 6(t - 3)$. Partikel mengalami perlambatan jika $v(t) \cdot a(t) < 0$. Hasil analisis tanda menunjukkan $v(t) \cdot a(t) < 0$ terpenuhi pada $0 \le t < 2$ (karena $v > 0, a < 0$) serta pada $3 < t < 4$ (karena $v < 0, a > 0$).</sub>
- C. $2 < t < 4$  
  <sub>Salah: Hanya mencari interval saat kecepatan bernilai negatif ($v(t) < 0$), mengabaikan tanda dari percepatan.</sub>
- D. $0 \le t < 3$  
  <sub>Salah: Hanya mencari interval percepatan negatif ($a(t) < 0$) tanpa memperhatikan arah gerak kecepatan partikel.</sub>

**Pembahasan:** Posisi: $s(t) = t^3 - 9t^2 + 24t + 5$

Kecepatan partikel:
$$v(t) = s'(t) = 3t^2 - 18t + 24 = 3(t^2 - 6t + 8) = 3(t - 2)(t - 4)$$

Percepatan partikel:
$$a(t) = v'(t) = 6t - 18 = 6(t - 3)$$

Partikel mengalami perlambatan saat kecepatan dan percepatan berlawanan tanda, yakni $v(t) \cdot a(t) < 0$.
Pembuat nol adalah $t = 2$, $t = 3$, dan $t = 4$. Untuk $t \ge 0$, kita uji tanda:
1. Pada $0 \le t < 2$: $v(t) > 0$ dan $a(t) < 0 \implies v(t) \cdot a(t) < 0$ (melambat).
2. Pada $2 < t < 3$: $v(t) < 0$ dan $a(t) < 0 \implies v(t) \cdot a(t) > 0$ (mempercepat).
3. Pada $3 < t < 4$: $v(t) < 0$ dan $a(t) > 0 \implies v(t) \cdot a(t) < 0$ (melambat).
4. Pada $t > 4$: $v(t) > 0$ dan $a(t) > 0 \implies v(t) \cdot a(t) > 0$ (mempercepat).

Jadi, partikel mengalami perlambatan pada interval $0 \le t < 2$ atau $3 < t < 4$.
**Acuan:** siswa — siswa hal.163 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b02-c-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: banyaknya parameter kemonotonan kurva*

Diberikan kurva fungsi kubik $f(x) = 2x^3 - 3mx^2 + 6(m+4)x - 15$ dengan $m$ adalah suatu konstanta. Agar grafik fungsi $f(x)$ tidak pernah turun untuk setiap bilangan real $x \in \mathbb{R}$, maka banyaknya nilai bilangan bulat $m$ yang memenuhi adalah ....

- **A. $9$** ✅  
  <sub>Benar: Syarat tidak pernah turun adalah $f'(x) \ge 0$ untuk setiap $x \in \mathbb{R}$. Diperoleh $f'(x) = 6(x^2 - mx + m + 4)$. Karena koefisien $x^2$ positif ($1 > 0$), syarat definit tak negatif adalah $D \le 0$, yaitu $(-m)^2 - 4(1)(m+4) \le 0 \iff m^2 - 4m - 16 \le 0$. Pembuat nol adalah $m = 2 \pm 2\sqrt{5}$. Karena $2\sqrt{5} \approx 4{,}47$, intervalnya $-2{,}47 \le m \le 6{,}47$. Bilangan bulat yang memenuhi adalah $\{-2, -1, 0, 1, 2, 3, 4, 5, 6\}$, ada tepat 9 buah.</sub>
- B. $8$  
  <sub>Salah: Lupa menghitung nilai $m = 0$ sebagai anggota himpunan bilangan bulat.</sub>
- C. $10$  
  <sub>Salah: Kesalahan menghitung akar $2 + 2\sqrt{5}$ sehingga menganggap nilai $m = 7$ termasuk ke dalam penyelesaian.</sub>
- D. $7$  
  <sub>Salah: Menggunakan pertidaksamaan ketat $D < 0$ dan salah membulatkan batas akar ke dalam sehingga batas menjadi $-1 \le m \le 5$.</sub>

**Pembahasan:** Agar kurva fungsi $f(x)$ tidak pernah turun pada $\mathbb{R}$, turunan pertamanya harus memenuhi:
$$f'(x) \ge 0, \quad \forall x \in \mathbb{R}$$

Turunan pertama dari $f(x)$:
$$f'(x) = 6x^2 - 6mx + 6(m+4) = 6[x^2 - mx + (m+4)]$$

Karena faktor $6 > 0$ dan koefisien dari $x^2$ adalah $1 > 0$, bentuk kuadrat $x^2 - mx + (m+4)$ definit non-negatif jika diskriminannya memenuhi $D \le 0$:
$$D = (-m)^2 - 4(1)(m+4) \le 0$$
$$m^2 - 4m - 16 \le 0$$

Selesaikan persamaan kuadrat $m^2 - 4m - 16 = 0$:
$$m = \frac{-(-4) \pm \sqrt{(-4)^2 - 4(1)(-16)}}{2(1)} = \frac{4 \pm \sqrt{80}}{2} = 2 \pm 2\sqrt{5}$$

Karena $\sqrt{5} \approx 2{,}236$, maka $2\sqrt{5} \approx 4{,}472$.
Batas interval adalah:
$$2 - 4{,}472 \le m \le 2 + 4{,}472 \implies -2{,}472 \le m \le 6{,}472$$

Nilai bilangan bulat $m$ yang berada dalam interval tersebut adalah:
$$\{-2, -1, 0, 1, 2, 3, 4, 5, 6\}$$
Banyaknya nilai $m$ yang memenuhi adalah $9$.
**Acuan:** siswa — siswa hal.150

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b02-c-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: garis tegak lurus penghubung titik ekstrem*

Diberikan fungsi polinomial $f(x) = x^3 - 3x^2 + 5$. Titik $A$ adalah titik balik maksimum dan titik $B$ adalah titik balik minimum dari kurva fungsi tersebut. Persamaan garis lurus yang melalui titik $A$ dan tegak lurus terhadap ruas garis penghubung $AB$ adalah ....

- A. $x - 2y = 0$  
  <sub>Salah: Menggunakan titik balik minimum $B(2, 1)$ sebagai titik yang dilalui alih-alih titik balik maksimum $A(0, 5)$.</sub>
- B. $2x + y - 5 = 0$  
  <sub>Salah: Membuat persamaan garis yang sejajar dengan ruas garis $AB$ ($m = -2$) alih-alih tegak lurus.</sub>
- **C. $x - 2y + 10 = 0$** ✅  
  <sub>Benar: Turunan $f'(x) = 3x(x - 2) = 0$ memberikan absis $x = 0$ dan $x = 2$. Dari $f''(x) = 6x - 6$, $f''(0) = -6 < 0$ (maksimum di $A(0, 5)$) dan $f''(2) = 6 > 0$ (minimum di $B(2, 1)$). Gradien garis penghubung $AB$ adalah $m_{AB} = \frac{1 - 5}{2 - 0} = -2$. Gradien garis tegak lurusnya adalah $m_\perp = -\frac{1}{-2} = \frac{1}{2}$. Persamaan garis melalui $A(0, 5)$ dengan gradien $\frac{1}{2}$ adalah $y - 5 = \frac{1}{2}(x - 0) \iff x - 2y + 10 = 0$.</sub>
- D. $x + 2y - 10 = 0$  
  <sub>Salah: Salah menentukan gradien tegak lurus menjadi $-\frac{1}{2}$ karena lupa menghilangkan tanda negatif dari $-(-2)$.</sub>

**Pembahasan:** Turunan pertama kurva $f(x) = x^3 - 3x^2 + 5$:
$$f'(x) = 3x^2 - 6x = 3x(x - 2)$$

Titik stasioner saat $f'(x) = 0$, yaitu $x = 0$ atau $x = 2$.

Uji jenis ekstrem menggunakan turunan kedua $f''(x) = 6x - 6$:
- Untuk $x = 0$: $f''(0) = -6 < 0$, sehingga titik maksimum tercapai di $x = 0$.
  Ordinat $y = f(0) = 5$, sehingga titik balik maksimum adalah $A(0, 5)$.
- Untuk $x = 2$: $f''(2) = 6 > 0$, sehingga titik minimum tercapai di $x = 2$.
  Ordinat $y = f(2) = 2^3 - 3(2)^2 + 5 = 1$, sehingga titik balik minimum adalah $B(2, 1)$.

Gradien garis penghubung titik $A(0, 5)$ dan $B(2, 1)$:
$$m_{AB} = \frac{y_B - y_A}{x_B - x_A} = \frac{1 - 5}{2 - 0} = \frac{-4}{2} = -2$$

Gradien garis yang tegak lurus terhadap ruas garis $AB$ ($m_\perp$):
$$m_\perp = -\frac{1}{m_{AB}} = -\frac{1}{-2} = \frac{1}{2}$$

Persamaan garis yang melalui titik $A(0, 5)$ dengan gradien $m = \frac{1}{2}$:
$$y - 5 = \frac{1}{2}(x - 0)$$
$$2y - 10 = x \iff x - 2y + 10 = 0$$
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b02-c-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: analisis titik ekstrem parameter*

Diberikan fungsi polinomial $f(x) = x^3 - 3x^2 - 9x + k$ dengan $k$ adalah suatu konstanta real. Garis mendatar $y = c$ memotong grafik fungsi $f(x)$ tepat di tiga titik berlainan jika dan hanya jika $m < c < n$. Nilai dari $n - m$ adalah ....

- A. $14$  
  <sub>Salah: Siswa salah menghitung nilai balik maksimum dengan mensubstitusikan tanda yang salah pada absis $x = -1$ sehingga menghasilkan nilai $k - 13$ dan selisihnya menjadi $14$.</sub>
- **B. $32$** ✅  
  <sub>Benar: Selisih antara nilai balik maksimum dan nilai balik minimum kurva adalah $(k + 5) - (k - 27) = 32$.</sub>
- C. $16$  
  <sub>Salah: Siswa membagi dua selisih sebenarnya karena mengira selisih diukur dari titik belok ke nilai ekstrem.</sub>
- D. $54$  
  <sub>Salah: Siswa mengabaikan nilai balik maksimum dan menghitung dua kali nilai mutlak komponen nilai balik minimum, yaitu $2 \times 27 = 54$.</sub>

**Pembahasan:** Langkah 1: Menentukan absis titik stasioner fungsi $f(x)$.
$$f'(x) = 3x^2 - 6x - 9 = 0 \iff 3(x^2 - 2x - 3) = 0 \iff 3(x - 3)(x + 1) = 0$$
Diperoleh absis stasioner pada $x = -1$ dan $x = 3$.

Langkah 2: Menentukan jenis titik balik dengan uji turunan.
$$f''(x) = 6x - 6$$
- Untuk $x = -1$: $f''(-1) = 6(-1) - 6 = -12 < 0$, maka $x = -1$ memberikan nilai balik maksimum.
- Untuk $x = 3$: $f''(3) = 6(3) - 6 = 12 > 0$, maka $x = 3$ memberikan nilai balik minimum.

Langkah 3: Menghitung nilai balik maksimum dan minimum.
- Nilai balik maksimum: $n = f(-1) = (-1)^3 - 3(-1)^2 - 9(-1) + k = -1 - 3 + 9 + k = k + 5$.
- Nilai balik minimum: $m = f(3) = (3)^3 - 3(3)^2 - 9(3) + k = 27 - 27 - 27 + k = k - 27$.

Langkah 4: Menentukan syarat garis $y = c$ memotong grafik di tiga titik berlainan.
Garis $y = c$ memotong grafik fungsi kubik di tiga titik berlainan jika nilai $c$ berada di antara nilai balik minimum dan nilai balik maksimum, yaitu $m < c < n$.
Maka:
$$n - m = (k + 5) - (k - 27) = 32$$
**Acuan:** siswa — siswa hal.157

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b02-c-hard-bt01-018
*variasi (angka) | C5 | 4 langkah | jenis: kemonotonan kurva berparameter*

Grafik fungsi kubik $f(x) = 2x^3 + ax^2 + bx + c$ hanya turun pada interval $-4 < x < 6$. Nilai dari $a - b$ adalah ....

- A. $150$  
  <sub>Salah: Tertukar tanda akar-akar pembuat nol turunan menjadi $(x - 4)(x + 6)$ sehingga mendapatkan $a = 6$ dan $b = -144$.</sub>
- **B. $138$** ✅  
  <sub>Benar: Turunan pertama $f'(x) = 6x^2 + 2ax + b$. Karena fungsi hanya turun pada interval $-4 < x < 6$, maka $x = -4$ dan $x = 6$ merupakan pembuat nol dari $f'(x) = 0$, sehingga $f'(x) = 6(x + 4)(x - 6) = 6(x^2 - 2x - 24) = 6x^2 - 12x - 144$. Diperoleh $2a = -12 \implies a = -6$ dan $b = -144$. Maka $a - b = -6 - (-144) = 138$.</sub>
- C. $23$  
  <sub>Salah: Lupa mengalikan faktor koefisien utama 6 pada bentuk pembuat nol turunan sehingga menganggap $2a = -2$ dan $b = -24$.</sub>
- D. $-150$  
  <sub>Salah: Keliru menghitung operasi penjumlahan $a + b = -6 + (-144)$ bukan selisih $a - b$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama kurva fungsi.
$f'(x) = 6x^2 + 2ax + b$.

Langkah 2: Menentukan bentuk turunan dari batas interval turun.
Syarat fungsi turun adalah $f'(x) < 0$. Karena kurva hanya turun pada $-4 < x < 6$, maka batas-batasnya adalah akar-akar dari $f'(x) = 0$:
$f'(x) = 6(x - (-4))(x - 6) = 6(x + 4)(x - 6)$.

Langkah 3: Menjabarkan persamaan kuadrat turunan.
$f'(x) = 6(x^2 - 2x - 24) = 6x^2 - 12x - 144$.

Langkah 4: Menyamakan koefisien dan menghitung nilai yang dicari.
- $2a = -12 \implies a = -6$
- $b = -144$
Maka nilai dari $a - b = -6 - (-144) = -6 + 144 = 138$.
**Acuan:** siswa — siswa hal.163 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b02-c-hard-bt01-019
*variasi (konteks) | C5 | 5 langkah | jenis: jarak pasangan garis singgung kurva*

Dua buah garis singgung pada kurva $y = x^3 - 6x^2 + 8x - 5$ masing-masing membentuk sudut $135^\circ$ terhadap arah sumbu-$x$ positif. Jarak antara kedua garis singgung sejajar tersebut adalah ....

- A. $\sqrt{2}$  
  <sub>Salah: Keliru menghitung selisih konstanta menjadi $2$ bukan $4$, sehingga menghasilkan $\frac{2}{\sqrt{2}} = \sqrt{2}$.</sub>
- B. $2$  
  <sub>Salah: Membagi selisih konstanta dengan $(A^2 + B^2) = 2$ bukan dengan $\sqrt{A^2 + B^2} = \sqrt{2}$.</sub>
- C. $4$  
  <sub>Salah: Hanya menghitung selisih konstanta persamaan garis $|c_1 - c_2|$ tanpa membagi dengan panjang vektor normal $\sqrt{A^2 + B^2}$.</sub>
- **D. $2\sqrt{2}$** ✅  
  <sub>Benar: Gradien garis singgung $m = \tan 135^\circ = -1$. Turunan $y' = 3x^2 - 12x + 8 = -1 \implies 3(x - 1)(x - 3) = 0$, sehingga absis titik singgung adalah $x = 1$ dan $x = 3$. Titik singgung pertama $(1, -2)$ menghasilkan garis singgung $x + y + 1 = 0$, dan titik singgung kedua $(3, -8)$ menghasilkan garis singgung $x + y + 5 = 0$. Jarak antara kedua garis sejajar tersebut adalah $d = \frac{|5 - 1|}{\sqrt{1^2 + 1^2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis singgung kurva.
Sudut kemiringan $\alpha = 135^\circ$, sehingga kemiringan garis singgung adalah:
$m = \tan 135^\circ = -1$.

Langkah 2: Menentukan absis titik singgung melalui turunan pertama.
$y' = 3x^2 - 12x + 8$
Karena $y' = m$, maka:
$3x^2 - 12x + 8 = -1$
$3x^2 - 12x + 9 = 0$
$x^2 - 4x + 3 = 0$
$(x - 1)(x - 3) = 0$
Diperoleh dua titik singgung pada $x_1 = 1$ dan $x_2 = 3$.

Langkah 3: Menghitung ordinat masing-masing titik singgung.
- Untuk $x = 1$:
$y_1 = 1^3 - 6(1)^2 + 8(1) - 5 = 1 - 6 + 8 - 5 = -2$.
Titik singgung pertama adalah $(1, -2)$.
- Untuk $x = 3$:
$y_2 = 3^3 - 6(3)^2 + 8(3) - 5 = 27 - 54 + 24 - 5 = -8$.
Titik singgung kedua adalah $(3, -8)$.

Langkah 4: Menyusun persamaan kedua garis singgung.
- Garis $g_1$ melalui $(1, -2)$ bergradien $-1$:
$y - (-2) = -1(x - 1) \implies y + 2 = -x + 1 \implies x + y + 1 = 0$.
- Garis $g_2$ melalui $(3, -8)$ bergradien $-1$:
$y - (-8) = -1(x - 3) \implies y + 8 = -x + 3 \implies x + y + 5 = 0$.

Langkah 5: Menghitung jarak antara kedua garis sejajar.
$d = \frac{|c_2 - c_1|}{\sqrt{A^2 + B^2}} = \frac{|5 - 1|}{\sqrt{1^2 + 1^2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2}$.
**Acuan:** siswa — siswa hal.162 Latihan Soal Aplikasi Turunan Fungsi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b02-c-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: jarak titik potong sumbu garis singgung kurva*

Diketahui kurva parabola $y = x^2 - 5x + 8$. Garis singgung $g_1$ menyinggung kurva tersebut dan sejajar dengan garis $3x - y + 2 = 0$, serta memotong sumbu-$y$ di titik $A$. Garis singgung $g_2$ menyinggung kurva tersebut dan tegak lurus terhadap garis $x + y - 4 = 0$, serta memotong sumbu-$y$ di titik $B$. Jarak antara titik $A$ dan titik $B$ adalah ....

- **A. $7$** ✅  
  <sub>Benar: Garis $g_1$ sejajar $3x - y + 2 = 0$ memiliki gradien $m_1 = 3$. Turunan kurva $y' = 2x - 5 = 3 \implies x = 4, y = 4$, sehingga persamaan $g_1$ adalah $y - 4 = 3(x - 4) \implies y = 3x - 8$ dengan titik potong sumbu-$y$ di $A(0, -8)$. Garis $g_2$ tegak lurus $x + y - 4 = 0$ (gradien $-1$) sehingga memiliki gradien $m_2 = 1$. Dari $y' = 2x - 5 = 1 \implies x = 3, y = 2$, diperoleh persamaan $g_2$ adalah $y - 2 = 1(x - 3) \implies y = x - 1$ dengan titik potong sumbu-$y$ di $B(0, -1)$. Jarak antara titik $A$ dan $B$ adalah $|-1 - (-8)| = 7$.</sub>
- B. $5$  
  <sub>Salah: Salah menentukan absis titik singgung kedua dari syarat tegak lurus sehingga menghasilkan pergeseran ordinat titik potong.</sub>
- C. $9$  
  <sub>Salah: Keliru menjumlahkan nilai absolut ordinat kedua titik $|-8| + |-1| = 9$ meskipun keduanya berada pada bagian sumbu-$y$ yang sama.</sub>
- D. $3$  
  <sub>Salah: Hanya menghitung selisih nilai absis kedua titik singgung kurva $|4 - 3| = 1$ atau salah membaca selisih konstanta kurva.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien dan persamaan garis singgung pertama ($g_1$).
Garis $3x - y + 2 = 0 \implies y = 3x + 2$, gradiennya adalah 3.
Karena $g_1$ sejajar, maka $m_1 = 3$.
Turunan kurva: $y' = 2x - 5$.
$2x - 5 = 3 \implies 2x = 8 \implies x = 4$.
Ordinat titik singgung: $y = 4^2 - 5(4) + 8 = 16 - 20 + 8 = 4$.
Persamaan $g_1$: $y - 4 = 3(x - 4) \implies y = 3x - 8$.
Titik potong terhadap sumbu-$y$ (saat $x = 0$) adalah $A(0, -8)$.

Langkah 2: Menentukan gradien dan persamaan garis singgung kedua ($g_2$).
Garis $x + y - 4 = 0 \implies y = -x + 4$, gradiennya adalah $-1$.
Karena $g_2$ tegak lurus, maka $m_2 = -\frac{1}{-1} = 1$.
$2x - 5 = 1 \implies 2x = 6 \implies x = 3$.
Ordinat titik singgung: $y = 3^2 - 5(3) + 8 = 9 - 15 + 8 = 2$.
Persamaan $g_2$: $y - 2 = 1(x - 3) \implies y = x - 1$.
Titik potong terhadap sumbu-$y$ (saat $x = 0$) adalah $B(0, -1)$.

Langkah 3: Menghitung jarak antara titik $A$ dan $B$.
Karena kedua titik berada pada sumbu-$y$, jaraknya adalah:
$d = |y_B - y_A| = |-1 - (-8)| = |-1 + 8| = 7$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
