# Lembar koreksi — kelas9 SMP9-B3 subbab E: Dilatasi

44 soal | easy 15, medium 15, hard 14 | variasi 21, orisinal 23
> **Kapasitas kurang (hard): 14 dari kuota 15** — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas9-b03-e-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: koordinat bayangan pusat O*

Bayangan titik $D(8, -12)$ oleh dilatasi dengan pusat $O(0,0)$ dan faktor skala $\frac{1}{4}$ adalah ....

- A. $(-3, 2)$  
  <sub>Salah: Posisi absis dan ordinat tertukar.</sub>
- **B. $(2, -3)$** ✅  
  <sub>Benar: Koordinat bayangan diperoleh dari $(kx, ky) = (\frac{1}{4} \times 8, \frac{1}{4} \times (-12)) = (2, -3)$.</sub>
- C. $(-2, 3)$  
  <sub>Salah: Keliru memberi tanda negatif pada faktor skala.</sub>
- D. $(32, -48)$  
  <sub>Salah: Mengalikan koordinat dengan penyebut skala (dikalikan 4, bukan $\frac{1}{4}$).</sub>

**Pembahasan:** Bayangan titik $(x, y)$ oleh dilatasi $[O, k]$ adalah $(kx, ky)$.\n$x' = \frac{1}{4} \times 8 = 2$\n$y' = \frac{1}{4} \times (-12) = -3$\nJadi, bayangan titik $D$ adalah $(2, -3)$.
**Acuan:** pretest — kelas9-b03-p0217-ayo-mencoba-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas9-b03-e-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: luas bayangan dilatasi*

Suatu segitiga $KLM$ siku-siku di $L$ memiliki panjang $KL = 6\text{ cm}$ dan $LM = 8\text{ cm}$. Jika segitiga $KLM$ didilatasikan dengan faktor skala 2, maka luas bayangan segitiga $K'L'M'$ adalah ....

- A. $48\text{ cm}^2$  
  <sub>Salah: Hanya mengalikan luas awal dengan $k$ bukan $k^2$ ($24 \times 2$).</sub>
- B. $24\text{ cm}^2$  
  <sub>Salah: Hanya menghitung luas segitiga mula-mula tanpa mendilatasi.</sub>
- C. $192\text{ cm}^2$  
  <sub>Salah: Lupa membagi dua saat menghitung luas segitiga mula-mula ($6 \times 8 = 48$, lalu $48 \times 4$).</sub>
- **D. $96\text{ cm}^2$** ✅  
  <sub>Benar: Luas awal segitiga adalah $\frac{1}{2} \times 6 \times 8 = 24\text{ cm}^2$. Luas setelah dilatasi dengan faktor skala $k = 2$ adalah $k^2 \times \text{luas awal} = 2^2 \times 24 = 4 \times 24 = 96\text{ cm}^2$.</sub>

**Pembahasan:** Langkah 1: Hitung luas awal segitiga $KLM$.\n$\text{Luas} = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 6 \times 8 = 24\text{ cm}^2$.\n\nLangkah 2: Hitung luas segitiga setelah dilatasi dengan faktor skala $k = 2$.\n$\text{Luas bayangan} = k^2 \times \text{Luas awal} = 2^2 \times 24 = 4 \times 24 = 96\text{ cm}^2$.
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas9-b03-e-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: koordinat bayangan pusat P(a,b)*

Titik $A(5, 7)$ didilatasikan terhadap titik pusat $P(1, 3)$ dengan faktor skala 3. Koordinat bayangan titik $A$ adalah ....

- A. $(12, 12)$  
  <sub>Salah: Hanya menghitung $k(x - a)$ dan $k(y - b)$ serta lupa menjumlahkannya kembali dengan pusat $(a, b)$.</sub>
- **B. $(13, 15)$** ✅  
  <sub>Benar: $x' = 3(5 - 1) + 1 = 12 + 1 = 13$ dan $y' = 3(7 - 3) + 3 = 12 + 3 = 15$.</sub>
- C. $(11, 15)$  
  <sub>Salah: Salah melakukan pengurangan pada koordinat $x$ saat menghitung $x'$.</sub>
- D. $(15, 21)$  
  <sub>Salah: Mengalikan langsung koordinat $A$ dengan faktor skala 3 tanpa memperhitungkan pusat $P(1, 3)$.</sub>

**Pembahasan:** Rumus dilatasi titik $(x, y)$ terhadap pusat $(a, b)$ dengan faktor skala $k$:\n$x' = k(x - a) + a$\n$y' = k(y - b) + b$\n\nDiketahui $(x, y) = (5, 7)$, $(a, b) = (1, 3)$, dan $k = 3$:\n$x' = 3(5 - 1) + 1 = 3(4) + 1 = 12 + 1 = 13$\n$y' = 3(7 - 3) + 3 = 3(4) + 3 = 12 + 3 = 15$\n\nJadi, koordinat bayangan titik $A$ adalah $(13, 15)$.
**Acuan:** siswa — siswa hal.218 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas9-b03-e-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: menentukan faktor skala*

Titik $B(3, -4)$ didilatasikan terhadap titik pusat $O(0,0)$ sehingga menghasilkan bayangan $B'(-12, 16)$. Faktor skala dilatasi tersebut adalah ....

- **A. $-4$** ✅  
  <sub>Benar: Faktor skala $k = \frac{x'}{x} = \frac{-12}{3} = -4$.</sub>
- B. $-\frac{1}{4}$  
  <sub>Salah: Terbalik menghitung rasio dengan membagi titik asal terhadap bayangan ($x / x'$).</sub>
- C. $4$  
  <sub>Salah: Mengabaikan perubahan tanda negatif pada koordinat hasil dilatasi.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Terbalik menghitung rasio dan mengabaikan tanda negatif.</sub>

**Pembahasan:** Pada dilatasi terhadap pusat $O(0,0)$:\n$x' = k \times x$\n$-12 = k \times 3$\n$k = \frac{-12}{3} = -4$\n\nJadi, faktor skala dilatasi tersebut adalah $-4$.
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas9-b03-e-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: sifat faktor skala dilatasi*

Pernyataan berikut yang benar mengenai hubungan antara nilai faktor skala $k$ dan ukuran bayangan pada transformasi dilatasi adalah ....

- **A. Bangun bayangan mengalami pengecilan jika $0 < |k| < 1$.** ✅  
  <sub>Benar: Ukuran bangun bayangan lebih kecil dari bangun awal jika nilai mutlak faktor skalanya berada di antara 0 dan 1 ($0 < |k| < 1$).</sub>
- B. Bangun bayangan mengalami perbesaran jika $0 < |k| < 1$.  
  <sub>Salah: Tertukar antara syarat pengecilan dan perbesaran ukuran bangun.</sub>
- C. Bangun bayangan selalu memiliki ukuran yang sama dengan bangun asal untuk setiap nilai $k$.  
  <sub>Salah: Menganggap dilatasi sebagai transformasi isometri seperti translasi atau refleksi.</sub>
- D. Bangun bayangan mengalami pengecilan jika $|k| > 1$.  
  <sub>Salah: Tertukar pengertian batasan nilai faktor skala untuk perbesaran.</sub>

**Pembahasan:** Pada dilatasi:\n- Jika $|k| > 1$, bayangan mengalami perbesaran.\n- Jika $0 < |k| < 1$, bayangan mengalami pengecilan.\n- Jika $|k| = 1$, bayangan memiliki ukuran yang sama dengan bangun aslinya.
**Acuan:** siswa — siswa hal.215

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas9-b03-e-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: koordinat bayangan dilatasi faktor negatif pecahan*

Titik $A(-9, 15)$ didilatasikan terhadap titik pusat $O(0,0)$ dengan faktor skala $-\frac{1}{3}$. Koordinat bayangan titik $A$ adalah ....

- A. $(-5, 3)$  
  <sub>Salah: Siswa menukar posisi koordinat $x$ dan $y$ setelah menghitung.</sub>
- B. $(-3, 5)$  
  <sub>Salah: Siswa lupa mengalikan dengan tanda negatif dari faktor skala.</sub>
- C. $(27, -45)$  
  <sub>Salah: Siswa membagi koordinat dengan $-\frac{1}{3}$ (mengalikan dengan $-3$) alih-alih mengalikannya.</sub>
- **D. $(3, -5)$** ✅  
  <sub>Benar: Bayangan diperoleh dari $x' = -\frac{1}{3} \times (-9) = 3$ dan $y' = -\frac{1}{3} \times 15 = -5$, sehingga bayangannya adalah $(3, -5)$.</sub>

**Pembahasan:** Berdasarkan rumus dilatasi terhadap pusat $O(0,0)$ dengan faktor skala $k$:
$$A'(x', y') = (kx, ky)$$
Diketahui $x = -9$, $y = 15$, dan $k = -\frac{1}{3}$, maka:
$$x' = -\frac{1}{3} \times (-9) = 3$$
$$y' = -\frac{1}{3} \times 15 = -5$$
Jadi, koordinat bayangan titik $A$ adalah $(3, -5)$.
**Acuan:** pretest — kelas9-b03-p0217-ayo-mencoba-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas9-b03-e-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: koordinat bayangan pusat P skala negatif*

Bayangan titik $Q(7, -3)$ oleh dilatasi dengan pusat $P(3, 1)$ dan faktor skala $-2$ adalah ....

- A. $(11, -7)$  
  <sub>Salah: Siswa menggunakan faktor skala positif $2$ bukan $-2$.</sub>
- B. $(-5, 7)$  
  <sub>Salah: Siswa salah menjumlahkan pada koordinat $y$ dengan menghitung $-2(-3 - 1) - 1$ bukannya ditambah 1.</sub>
- **C. $(-5, 9)$** ✅  
  <sub>Benar: $x' = -2(7 - 3) + 3 = -8 + 3 = -5$ dan $y' = -2(-3 - 1) + 1 = 8 + 1 = 9$.</sub>
- D. $(-14, 6)$  
  <sub>Salah: Siswa mengalikan langsung titik $Q$ dengan faktor skala tanpa memperhitungkan titik pusat $P(3,1)$.</sub>

**Pembahasan:** Bayangan titik $(x, y)$ oleh dilatasi terhadap pusat $P(a, b)$ dan faktor skala $k$ adalah:
$$x' = k(x - a) + a$$
$$y' = k(y - b) + b$$
Substitusikan $x = 7$, $y = -3$, $a = 3$, $b = 1$, dan $k = -2$:
$$x' = -2(7 - 3) + 3 = -2(4) + 3 = -8 + 3 = -5$$
$$y' = -2(-3 - 1) + 1 = -2(-4) + 1 = 8 + 1 = 9$$
Jadi, bayangan titik $Q$ adalah $(-5, 9)$.
**Acuan:** siswa — siswa hal.218 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas9-b03-e-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: keliling bayangan hasil dilatasi*

Segitiga $DEF$ siku-siku di $E$ memiliki panjang sisi $DE = 9\text{ cm}$, $EF = 12\text{ cm}$, dan $DF = 15\text{ cm}$. Jika segitiga $DEF$ didilatasikan dengan faktor skala 2, maka keliling segitiga bayangannya adalah ....

- **A. $72\text{ cm}$** ✅  
  <sub>Benar: Keliling awal $= 9 + 12 + 15 = 36\text{ cm}$, sehingga keliling bayangan $= 2 \times 36\text{ cm} = 72\text{ cm}$.</sub>
- B. $144\text{ cm}$  
  <sub>Salah: Siswa mengalikan keliling dengan $k^2$ ($2^2 = 4$), yang merupakan aturan untuk perubahan luas bukan keliling.</sub>
- C. $38\text{ cm}$  
  <sub>Salah: Siswa menambahkan faktor skala $2$ ke keliling awal bukan mengalikannya.</sub>
- D. $36\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung keliling segitiga awal tanpa mengalikannya dengan faktor skala.</sub>

**Pembahasan:** Keliling segitiga $DEF$ mula-mula:
$$\text{Keliling} = 9 + 12 + 15 = 36\text{ cm}$$
Pada dilatasi dengan faktor skala $k$, panjang setiap sisi bayangan menjadi $k$ kali panjang sisi mula-mula, sehingga keliling bayangannya adalah:
$$\text{Keliling bayangan} = k \times \text{Keliling awal} = 2 \times 36\text{ cm} = 72\text{ cm}$$
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas9-b03-e-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: panjang ruas garis hasil dilatasi*

Titik $P$ didilatasikan terhadap pusat titik asal $O(0,0)$ dengan faktor skala 6 menghasilkan bayangan $P'$. Jika panjang ruas garis $OP = 5\text{ cm}$, maka panjang ruas garis $OP'$ adalah ....

- A. $\frac{5}{6}\text{ cm}$  
  <sub>Salah: Siswa membagi jarak awal dengan faktor skala alih-alih mengalikannya.</sub>
- B. $180\text{ cm}$  
  <sub>Salah: Siswa mengalikan dengan kuadrat faktor skala ($5 \times 6^2$).</sub>
- **C. $30\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan sifat dilatasi, $OP' = k \times OP = 6 \times 5\text{ cm} = 30\text{ cm}$.</sub>
- D. $11\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan panjang ruas garis dengan faktor skala ($5 + 6$).</sub>

**Pembahasan:** Sesuai Sifat 3.9 pada dilatasi dengan pusat $O$ dan faktor skala $k$, jarak bayangan ke pusat dilatasi memenuhi:
$$OP' = |k| \times OP$$
Diketahui $OP = 5\text{ cm}$ dan $k = 6$, maka:
$$OP' = 6 \times 5\text{ cm} = 30\text{ cm}$$
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas9-b03-e-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: menentukan koordinat titik asal*

Titik $B'$ adalah bayangan dari titik $B$ oleh dilatasi dengan pusat $O(0,0)$ dan faktor skala 4. Jika koordinat titik $B'$ adalah $(-16, 28)$, koordinat titik awal $B$ adalah ....

- A. $(-20, 24)$  
  <sub>Salah: Siswa mengurangkan 4 dari masing-masing koordinat bayangan.</sub>
- B. $(-64, 112)$  
  <sub>Salah: Siswa salah langkah dengan mengalikan kembali koordinat bayangan dengan faktor skala 4.</sub>
- C. $(4, -7)$  
  <sub>Salah: Siswa membalik tanda negatif dan positif koordinat titik.</sub>
- **D. $(-4, 7)$** ✅  
  <sub>Benar: Koordinat titik asal diperoleh dengan membagi koordinat bayangan dengan faktor skala: $x = \frac{-16}{4} = -4$ dan $y = \frac{28}{4} = 7$.</sub>

**Pembahasan:** Jika titik $B(x, y)$ didilatasikan terhadap $[O, k]$, bayangannya adalah $B'(kx, ky)$.
Diketahui $B'(-16, 28)$ dan $k = 4$, maka:
$$4x = -16 \implies x = \frac{-16}{4} = -4$$
$$4y = 28 \implies y = \frac{28}{4} = 7$$
Jadi, koordinat titik $B$ adalah $(-4, 7)$.
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas9-b03-e-easy-bt01-011
*variasi (angka) | C2 | 1 langkah | jenis: koordinat bayangan faktor skala bulat negatif*

Bayangan titik $M(6, -8)$ oleh dilatasi dengan pusat $O(0,0)$ dan faktor skala $-3$ adalah ....

- **A. $(-18, 24)$** ✅  
  <sub>Benar: Mengalikan kedua koordinat titik dengan faktor skala $-3$: $x' = -3 \times 6 = -18$ dan $y' = -3 \times (-8) = 24$.</sub>
- B. $(-2, \frac{8}{3})$  
  <sub>Salah: Membagi koordinat dengan faktor skala alih-alih mengalikannya.</sub>
- C. $(18, -24)$  
  <sub>Salah: Lupa mengalikan dengan tanda negatif dari faktor skala.</sub>
- D. $(-18, -24)$  
  <sub>Salah: Hanya mengalikan tanda negatif pada absis, sedangkan ordinat tidak dikalikan dengan tanda negatif.</sub>

**Pembahasan:** Rumus bayangan dilatasi $[O, k]$ adalah $(x', y') = (kx, ky)$.
Dengan $k = -3$ dan titik $M(6, -8)$:
$x' = -3 \times 6 = -18$
$y' = -3 \times (-8) = 24$
Jadi, koordinat bayangannya adalah $(-18, 24)$.
**Acuan:** siswa — siswa hal.216 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas9-b03-e-easy-bt01-012
*variasi (angka) | C2 | 1 langkah | jenis: perbandingan luas akibat dilatasi*

Sebuah bangun datar didilatasikan dengan faktor skala 5. Perbandingan antara luas bangun datar awal dan luas bangun datar bayangannya adalah ....

- A. $1 : 10$  
  <sub>Salah: Mengalikan faktor skala dengan 2 alih-alih menguadratkannya ($5 \times 2$ bukan $5^2$).</sub>
- B. $1 : 5$  
  <sub>Salah: Menganggap perbandingan luas sama dengan faktor skala tanpa menguadratkannya.</sub>
- **C. $1 : 25$** ✅  
  <sub>Benar: Perbandingan luas bangun awal terhadap bangun bayangan setelah dilatasi dengan faktor skala $k$ adalah $1 : k^2 = 1 : 5^2 = 1 : 25$.</sub>
- D. $1 : 125$  
  <sub>Salah: Memangkatkan tiga faktor skala seperti pada perbandingan volume bangun ruang.</sub>

**Pembahasan:** Jika suatu bangun datar didilatasikan dengan faktor skala $k$, perbandingan luas bangun mula-mula ($L$) dan luas bayangan ($L'$) memenuhi:
$\frac{L}{L'} = \frac{1}{k^2}$
Untuk $k = 5$, perbandingannya adalah:
$1 : 5^2 = 1 : 25$.
**Acuan:** siswa — siswa hal.221 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas9-b03-e-easy-bt01-013
*variasi (konteks) | C1 | 1 langkah | jenis: sifat perubahan ukuran pada transformasi*

Di antara jenis transformasi geometri berikut, transformasi yang menghasilkan bayangan dengan ukuran yang dapat berubah (memperbesar atau memperkecil) dari bangun semula adalah ....

- A. rotasi  
  <sub>Salah: Rotasi hanya memutar bangun terhadap titik tertentu tanpa mengubah ukurannya.</sub>
- **B. dilatasi** ✅  
  <sub>Benar: Dilatasi adalah transformasi pembesaran atau pengecilan suatu bangun dengan faktor skala tertentu, sedangkan translasi, refleksi, dan rotasi bersifat isometri (ukuran tetap).</sub>
- C. refleksi  
  <sub>Salah: Refleksi hanya membalik posisi bangun melalui pencerminan tanpa mengubah ukurannya.</sub>
- D. translasi  
  <sub>Salah: Translasi hanya menggeser posisi bangun tanpa mengubah ukurannya.</sub>

**Pembahasan:** Transformasi geometri translasi, refleksi, dan rotasi tidak mengubah bentuk maupun ukuran bangun (kongruen). Satu-satunya transformasi yang mengubah ukuran bangun (memperbesar atau memperkecil) adalah dilatasi.
**Acuan:** siswa — siswa hal.224 Uji Pemahaman

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas9-b03-e-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: karakteristik arah bayangan dilatasi*

Pada proses dilatasi dengan pusat titik asal $O$, jika posisi bayangan titik $A'$ terletak berlawanan arah dengan letak titik awal $A$ terhadap titik pusat $O$, maka faktor skala $k$ dilatasi tersebut ....

- A. bernilai nol ($k = 0$)  
  <sub>Salah: Faktor skala bernilai nol tidak terdefinisi sebagai dilatasi bangun karena menghasilkan satu titik pusat saja.</sub>
- B. bernilai pecahan positif ($0 < k < 1$)  
  <sub>Salah: Faktor skala $0 < k < 1$ menunjukkan pengecilan searah, bukan posisi berlawanan arah.</sub>
- **C. bernilai negatif ($k < 0$)** ✅  
  <sub>Benar: Berdasarkan sifat dilatasi, faktor skala $k$ bernilai negatif jika arah bayangan berlawanan dengan arah titik semula terhadap pusat dilatasi.</sub>
- D. bernilai positif ($k > 0$)  
  <sub>Salah: Faktor skala positif menghasilkan bayangan yang searah dengan titik awal terhadap pusat dilatasi.</sub>

**Pembahasan:** Sesuai Sifat 3.9 Buku Siswa Matematika Kelas IX, faktor skala $k$ dapat bernilai negatif apabila $AO'$ berlawanan arah dengan $AO$. Jadi, nilai faktor skalanya memenuhi $k < 0$.
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas9-b03-e-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: faktor skala dilatasi pusat P(a,b)*

Titik $B(6, 3)$ didilatasikan terhadap titik pusat $P(2, 3)$ sehingga menghasilkan bayangan $B'(18, 3)$. Faktor skala dari dilatasi tersebut adalah ....

- A. -4  
  <sub>Salah: Keliru memberi tanda negatif padahal letak bayangan searah dengan titik awal terhadap pusat $P$.</sub>
- B. 3  
  <sub>Salah: Mengabaikan titik pusat dilatasi dan langsung membagi absis bayangan dengan absis awal ($18 : 6 = 3$).</sub>
- C. 5  
  <sub>Salah: Salah menghitung selisih koordinat menjadi $18 - 3 = 15$ lalu dibagi $3$.</sub>
- **D. 4** ✅  
  <sub>Benar: Menggunakan hubungan $x' - a = k(x - a)$: $18 - 2 = k(6 - 2) \iff 16 = 4k \iff k = 4$.</sub>

**Pembahasan:** Rumus dilatasi terhadap pusat $P(a,b)$ adalah $x' = k(x - a) + a$.
Diketahui $x = 6$, $a = 2$, dan $x' = 18$.
$18 = k(6 - 2) + 2$
$18 - 2 = 4k$
$16 = 4k$
$k = \frac{16}{4} = 4$.
Jadi, faktor skala dilatasi tersebut adalah 4.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas9-b03-e-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: koordinat bayangan dilatasi segitiga*

Diketahui segitiga $PQR$ dengan koordinat titik sudut $P(-6, 9)$, $Q(3, -6)$, dan $R(12, 15)$. Koordinat bayangan titik-titik sudut segitiga $PQR$ setelah didilatasikan terhadap pusat titik asal $O(0,0)$ dengan faktor skala $\frac{1}{3}$ adalah ....

- A. $P'(-18, 27)$, $Q'(9, -18)$, dan $R'(36, 45)$  
  <sub>Salah: Siswa mengalikan koordinat dengan 3, bukan membagi dengan 3 (salah operasi faktor skala pecahan).</sub>
- B. $P'(3, -2)$, $Q'(-2, 1)$, dan $R'(5, 4)$  
  <sub>Salah: Siswa menukar posisi nilai absis dan ordinat pada koordinat bayangan.</sub>
- C. $P'(2, -3)$, $Q'(-1, 2)$, dan $R'(-4, -5)$  
  <sub>Salah: Siswa salah memasukkan tanda faktor skala menjadi negatif ($-\frac{1}{3}$).</sub>
- **D. $P'(-2, 3)$, $Q'(1, -2)$, dan $R'(4, 5)$** ✅  
  <sub>Benar: Mengalikan setiap absis dan ordinat titik sudut dengan faktor skala $\frac{1}{3}$: $P'(\frac{1}{3} \times (-6), \frac{1}{3} \times 9) = P'(-2, 3)$, $Q'(\frac{1}{3} \times 3, \frac{1}{3} \times (-6)) = Q'(1, -2)$, dan $R'(\frac{1}{3} \times 12, \frac{1}{3} \times 15) = R'(4, 5)$.</sub>

**Pembahasan:** Rumus bayangan titik $(x, y)$ oleh dilatasi $[O, k]$ adalah $(kx, ky)$.\n1. Untuk titik $P(-6, 9)$:\n$x' = \frac{1}{3} \times (-6) = -2$\n$y' = \frac{1}{3} \times 9 = 3$\nDiperoleh $P'(-2, 3)$.\n\n2. Untuk titik $Q(3, -6)$:\n$x' = \frac{1}{3} \times 3 = 1$\n$y' = \frac{1}{3} \times (-6) = -2$\nDiperoleh $Q'(1, -2)$.\n\n3. Untuk titik $R(12, 15)$:\n$x' = \frac{1}{3} \times 12 = 4$\n$y' = \frac{1}{3} \times 15 = 5$\nDiperoleh $R'(4, 5)$.\n\nJadi, koordinat bayangannya adalah $P'(-2, 3)$, $Q'(1, -2)$, dan $R'(4, 5)$.
**Acuan:** pretest — kelas9-b03-p0217-ayo-mencoba-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas9-b03-e-medium-bt01-002
*variasi (angka) | C3 | 2 langkah | jenis: bayangan dilatasi titik pusat P(a,b)*

Bayangan titik $A(5, -1)$ oleh dilatasi dengan pusat $P(2, 1)$ dan faktor skala $-2$ adalah ....

- A. $(-4, -3)$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan tanda negatif saat menghitung ordinat: $-2(-1 - 1) = -4$, lalu $-4 + 1 = -3$.</sub>
- B. $(-10, 2)$  
  <sub>Salah: Siswa memperlakukan dilatasi seolah-olah berpusat di titik asal $O(0,0)$ dengan langsung mengalikan $(kx, ky)$.</sub>
- C. $(-6, 4)$  
  <sub>Salah: Siswa lupa menambahkan kembali koordinat pusat $(a, b)$ di akhir perhitungan sehingga hanya menghitung $k(x - a)$ dan $k(y - b)$.</sub>
- **D. $(-4, 5)$** ✅  
  <sub>Benar: Menggunakan rumus dilatasi pusat $(a, b)$: $x' = k(x - a) + a = -2(5 - 2) + 2 = -4$ dan $y' = k(y - b) + b = -2(-1 - 1) + 1 = 5$.</sub>

**Pembahasan:** Rumus bayangan dilatasi titik $A(x, y)$ terhadap pusat $P(a, b)$ dengan faktor skala $k$ adalah:\n$A'(k(x - a) + a, k(y - b) + b)$\n\nDiketahui $x = 5$, $y = -1$, $a = 2$, $b = 1$, dan $k = -2$.\n1. Menentukan absis $x'$:\n$x' = -2(5 - 2) + 2$\n$x' = -2(3) + 2$\n$x' = -6 + 2 = -4$\n\n2. Menentukan ordinat $y'$:\n$y' = -2(-1 - 1) + 1$\n$y' = -2(-2) + 1$\n$y' = 4 + 1 = 5$\n\nJadi, bayangan titik $A$ adalah $(-4, 5)$.
**Acuan:** siswa — siswa hal.218 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas9-b03-e-medium-bt01-003
*variasi (konteks) | C4 | 2 langkah | jenis: faktor skala dilatasi bertingkat*

Titik $A(6, -8)$ didilatasikan terhadap titik pusat $O(0,0)$ dengan faktor skala $\frac{1}{2}$ menghasilkan bayangan titik $A'$. Jika bayangan lanjutan dari titik $A'$ oleh suatu dilatasi dengan pusat $O(0,0)$ adalah titik $A''(9, -12)$, maka faktor skala dilatasi dari titik $A'$ ke titik $A''$ adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: Siswa membalik perbandingan titik akhir dengan titik awal ($A'$ terhadap $A''$).</sub>
- **B. 3** ✅  
  <sub>Benar: Koordinat $A'$ adalah $(3, -4)$. Dilatasi dari $A'(3, -4)$ ke $A''(9, -12)$ memiliki faktor skala $k = \frac{9}{3} = 3$.</sub>
- C. $\frac{3}{2}$  
  <sub>Salah: Siswa menghitung faktor skala total dari titik awal $A(6, -8)$ langsung ke $A''(9, -12)$.</sub>
- D. 6  
  <sub>Salah: Siswa mengalikan selisih koordinat atau salah melakukan operasi pembagian.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat bayangan pertama $A'$.\nTitik $A(6, -8)$ didilatasikan dengan pusat $O(0,0)$ dan faktor skala $k_1 = \frac{1}{2}$:\n$A' = \left(\frac{1}{2} \times 6, \frac{1}{2} \times (-8)\right) = (3, -4)$\n\nLangkah 2: Menentukan faktor skala dilatasi dari $A'$ ke $A''$.\nTitik $A'(3, -4)$ didilatasikan ke $A''(9, -12)$ dengan pusat $O(0,0)$ dan faktor skala $k_2$:\n$x'' = k_2 \times x' \implies 9 = k_2 \times 3 \implies k_2 = 3$\n$y'' = k_2 \times y' \implies -12 = k_2 \times (-4) \implies k_2 = 3$\n\nJadi, faktor skala dilatasi dari $A'$ ke $A''$ adalah 3.
**Acuan:** siswa — siswa hal.221 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas9-b03-e-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: titik asal dari dilatasi pusat P(a,b)*

Titik $A(x, y)$ didilatasikan terhadap titik pusat $P(3, -2)$ dengan faktor skala 3 sehingga menghasilkan bayangan $A'(9, 7)$. Nilai dari $x + y$ adalah ....

- A. 4  
  <sub>Salah: Siswa menghitung nilai selisih $x - y = 5 - 1 = 4$, bukan penjumlahan $x + y$.</sub>
- B. 10  
  <sub>Salah: Siswa salah memasukkan tanda ordinat titik pusat $P$ menjadi $b = 2$ sehingga memperoleh $y = 5$ dan $x + y = 10$.</sub>
- **C. 6** ✅  
  <sub>Benar: Mencari $x$: $9 = 3(x - 3) + 3 \implies x = 5$. Mencari $y$: $7 = 3(y - (-2)) + (-2) \implies y = 1$. Maka $x + y = 5 + 1 = 6$.</sub>
- D. 8  
  <sub>Salah: Siswa salah mengoperasikan persamaan aljabar pada absis sehingga memperoleh $x = 6$ dan $y = 2$.</sub>

**Pembahasan:** Berdasarkan rumus dilatasi terhadap pusat $P(a, b)$ dengan faktor skala $k$:\n$x' = k(x - a) + a$\n$y' = k(y - b) + b$\n\nDiketahui $a = 3$, $b = -2$, $k = 3$, $x' = 9$, dan $y' = 7$.\n\n1. Menentukan nilai $x$:\n$9 = 3(x - 3) + 3$\n$9 - 3 = 3(x - 3)$\n$6 = 3(x - 3)$\n$2 = x - 3 \implies x = 5$\n\n2. Menentukan nilai $y$:\n$7 = 3(y - (-2)) + (-2)$\n$7 = 3(y + 2) - 2$\n$7 + 2 = 3(y + 2)$\n$9 = 3(y + 2)$\n$3 = y + 2 \implies y = 1$\n\n3. Menghitung $x + y$:\n$x + y = 5 + 1 = 6$.\n\nJadi, nilai dari $x + y$ adalah 6.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas9-b03-e-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: luas bayangan hasil dilatasi*

Persegi panjang $ABCD$ memiliki koordinat titik sudut $A(1, 1)$, $B(5, 1)$, $C(5, 4)$, dan $D(1, 4)$. Jika persegi panjang tersebut didilatasikan terhadap titik pusat $O(0,0)$ dengan faktor skala $-2$, maka luas bayangan persegi panjang $A'B'C'D'$ adalah ....

- A. $56\text{ satuan luas}$  
  <sub>Salah: Siswa mengalikan keliling bangun awal dengan $k^2$ ($14 \times 4 = 56$).</sub>
- B. $28\text{ satuan luas}$  
  <sub>Salah: Siswa menghitung keliling dari bayangan persegi panjang, bukan luasnya ($2 \times (8 + 6) = 28$).</sub>
- C. $24\text{ satuan luas}$  
  <sub>Salah: Siswa mengalikan luas awal dengan $|k|$ bukan dengan $k^2$ ($12 \times 2 = 24$).</sub>
- **D. $48\text{ satuan luas}$** ✅  
  <sub>Benar: Panjang awal $= 5 - 1 = 4$, lebar awal $= 4 - 1 = 3$. Luas awal $= 4 \times 3 = 12$. Luas bayangan $= k^2 \times \text{Luas awal} = (-2)^2 \times 12 = 4 \times 12 = 48\text{ satuan luas}$.</sub>

**Pembahasan:** Langkah 1: Menentukan ukuran panjang dan lebar persegi panjang awal $ABCD$.\n- Panjang $AB = 5 - 1 = 4\text{ satuan}$\n- Lebar $BC = 4 - 1 = 3\text{ satuan}$\n\nLangkah 2: Menghitung luas persegi panjang awal.\n$\text{Luas awal} = 4 \times 3 = 12\text{ satuan luas}$\n\nLangkah 3: Menghitung luas bayangan hasil dilatasi.\nPada dilatasi dengan faktor skala $k$, luas bayangan memenuhi hubungan:\n$\text{Luas bayangan} = k^2 \times \text{Luas awal}$\n\nDengan $k = -2$:\n$\text{Luas bayangan} = (-2)^2 \times 12 = 4 \times 12 = 48\text{ satuan luas}$.\n\nJadi, luas bayangan persegi panjang tersebut adalah $48\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas9-b03-e-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: luas bayangan segitiga siku-siku*

Suatu segitiga $PQR$ siku-siku di titik $Q$ memiliki panjang sisi $PQ = 12\text{ cm}$, $QR = 16\text{ cm}$, dan $PR = 20\text{ cm}$. Jika segitiga $P'Q'R'$ merupakan hasil dilatasi dari segitiga $PQR$ dengan faktor skala $\frac{1}{2}$, maka luas segitiga $P'Q'R'$ adalah ....

- **A. $24\text{ cm}^2$** ✅  
  <sub>Benar: Luas awal segitiga $PQR$ adalah $\frac{1}{2} \times 12 \times 16 = 96\text{ cm}^2$. Luas hasil dilatasi segitiga $P'Q'R'$ adalah $k^2 \times \text{Luas } PQR = \left(\frac{1}{2}\right)^2 \times 96 = \frac{1}{4} \times 96 = 24\text{ cm}^2$.</sub>
- B. $48\text{ cm}^2$  
  <sub>Salah: Hanya mengalikan luas awal dengan faktor skala $k = \frac{1}{2}$, bukan dengan $k^2$.</sub>
- C. $12\text{ cm}^2$  
  <sub>Salah: Mengalikan luas awal dengan $k^3 = \frac{1}{8}$ seolah-olah menghitung perbesaran volume.</sub>
- D. $96\text{ cm}^2$  
  <sub>Salah: Hanya menghitung luas segitiga mula-mula tanpa melakukan dilatasi.</sub>

**Pembahasan:** Langkah 1: Menghitung luas segitiga siku-siku awal $PQR$.
$$\text{Luas } PQR = \frac{1}{2} \times PQ \times QR = \frac{1}{2} \times 12 \times 16 = 96\text{ cm}^2$$

Langkah 2: Menghitung luas segitiga bayangan $P'Q'R'$ setelah didilatasi dengan faktor skala $k = \frac{1}{2}$.
$$\text{Luas } P'Q'R' = k^2 \times \text{Luas } PQR = \left(\frac{1}{2}\right)^2 \times 96 = \frac{1}{4} \times 96 = 24\text{ cm}^2$$

Jadi, luas segitiga $P'Q'R'$ adalah $24\text{ cm}^2$.
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas9-b03-e-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: keliling bayangan persegi panjang*

Diketahui persegi panjang $KLMN$ memiliki titik-titik sudut $K(2, 1)$, $L(8, 1)$, $M(8, 5)$, dan $N(2, 5)$. Jika persegi panjang tersebut didilatasikan terhadap pusat $P(3, 2)$ dengan faktor skala 3, keliling bayangan persegi panjang $K'L'M'N'$ adalah ....

- A. $20\text{ satuan}$  
  <sub>Salah: Hanya menghitung keliling bangun awal dan lupa mengalikannya dengan faktor skala.</sub>
- B. $30\text{ satuan}$  
  <sub>Salah: Hanya mengalikan setengah keliling (panjang ditambah lebar) dengan faktor skala.</sub>
- **C. $60\text{ satuan}$** ✅  
  <sub>Benar: Panjang awal $KL = 8 - 2 = 6\text{ satuan}$ dan lebar $LM = 5 - 1 = 4\text{ satuan}$. Keliling awal $= 2 \times (6 + 4) = 20\text{ satuan}$. Keliling bayangan $= |k| \times \text{keliling awal} = 3 \times 20 = 60\text{ satuan}$.</sub>
- D. $180\text{ satuan}$  
  <sub>Salah: Keliru mengalikan keliling dengan faktor skala kuadrat $k^2 = 9$ (rumus luas).</sub>

**Pembahasan:** Langkah 1: Menghitung keliling persegi panjang awal $KLMN$.
- Panjang $p = 8 - 2 = 6\text{ satuan}$
- Lebar $l = 5 - 1 = 4\text{ satuan}$
$$\text{Keliling awal} = 2 \times (p + l) = 2 \times (6 + 4) = 20\text{ satuan}$$

Langkah 2: Menghitung keliling bayangan persegi panjang $K'L'M'N'$.
Perubahan keliling pada dilatasi berbanding lurus dengan nilai mutlak faktor skala $|k|$.
$$\text{Keliling bayangan} = |k| \times \text{Keliling awal} = 3 \times 20 = 60\text{ satuan}$$

Jadi, keliling bayangan persegi panjang $K'L'M'N'$ adalah $60\text{ satuan}$.
**Acuan:** siswa — siswa hal.217 Contoh 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas9-b03-e-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: menentukan pusat dilatasi P(a,b)*

Titik $A(5, 3)$ didilatasikan dengan faktor skala $k = 3$ sehingga menghasilkan bayangan $A'(11, 7)$. Jika dilatasi tersebut berpusat di titik $P(a, b)$, koordinat titik $P$ adalah ....

- **A. $(2, 1)$** ✅  
  <sub>Benar: Menggunakan rumus bayangan $x' = k(x - a) + a$ diperoleh $11 = 3(5 - a) + a \iff 11 = 15 - 2a \iff 2a = 4 \iff a = 2$. Untuk sumbu $y$, $y' = k(y - b) + b$ diperoleh $7 = 3(3 - b) + b \iff 7 = 9 - 2b \iff 2b = 2 \iff b = 1$. Pusat dilatasi adalah $(2, 1)$.</sub>
- B. $(-2, -1)$  
  <sub>Salah: Salah tanda aljabar saat memindahkan suku pada persamaan linier.</sub>
- C. $(1, 2)$  
  <sub>Salah: Tertukar antara nilai absis $a$ dan ordinat $b$.</sub>
- D. $(3, 2)$  
  <sub>Salah: Salah dalam operasi aljabar saat membagi koefisien variabel.</sub>

**Pembahasan:** Rumus bayangan dilatasi terhadap pusat $P(a, b)$ dengan faktor skala $k$ adalah:
$$x' = k(x - a) + a$$
$$y' = k(y - b) + b$$

Langkah 1: Menentukan absis titik pusat $a$.
$$11 = 3(5 - a) + a$$
$$11 = 15 - 3a + a$$
$$11 = 15 - 2a$$
$$2a = 15 - 11$$
$$2a = 4 \implies a = 2$$

Langkah 2: Menentukan ordinat titik pusat $b$.
$$7 = 3(3 - b) + b$$
$$7 = 9 - 3b + b$$
$$7 = 9 - 2b$$
$$2b = 9 - 7$$
$$2b = 2 \implies b = 1$$

Jadi, koordinat pusat dilatasi $P$ adalah $(2, 1)$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas9-b03-e-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: titik awal dari dilatasi berurutan*

Titik $M(p, q)$ didilatasikan terhadap pusat $O(0,0)$ dengan faktor skala $-3$, kemudian bayangannya didilatasikan kembali terhadap pusat $O(0,0)$ dengan faktor skala $\frac{1}{2}$ sehingga menghasilkan bayangan akhir $M''(-6, 9)$. Nilai dari $p - q$ adalah ....

- A. $-10$  
  <sub>Salah: Terbalik mengurangkan menjadi $q - p = -6 - 4 = -10$.</sub>
- B. 2  
  <sub>Salah: Keliru menentukan tanda koordinat $p = -4$ dan $q = -6$ sehingga $-4 - (-6) = 2$.</sub>
- **C. 10** ✅  
  <sub>Benar: Faktor skala gabungan adalah $k = -3 \times \frac{1}{2} = -\frac{3}{2}$. Maka $-\frac{3}{2}p = -6 \iff p = 4$, dan $-\frac{3}{2}q = 9 \iff q = -6$. Nilai $p - q = 4 - (-6) = 10$.</sub>
- D. $-2$  
  <sub>Salah: Menghitung penjumlahan $p + q = 4 + (-6) = -2$ bukan pengurangan $p - q$.</sub>

**Pembahasan:** Langkah 1: Menentukan faktor skala total dari dua dilatasi berpusat di $O(0,0)$.
$$k_{\text{total}} = k_1 \times k_2 = -3 \times \frac{1}{2} = -\frac{3}{2}$$

Langkah 2: Menentukan nilai $p$ dan $q$ dari koordinat bayangan akhir $M''(-6, 9)$.
$$p' = k_{\text{total}} \times p \implies -6 = -\frac{3}{2}p \implies p = -6 \times \left(-\frac{2}{3}\right) = 4$$
$$q' = k_{\text{total}} \times q \implies 9 = -\frac{3}{2}q \implies q = 9 \times \left(-\frac{2}{3}\right) = -6$$

Langkah 3: Menghitung nilai $p - q$.
$$p - q = 4 - (-6) = 4 + 6 = 10$$

Jadi, nilai dari $p - q$ adalah 10.
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas9-b03-e-medium-bt01-010
*orisinal | C3 | 2 langkah | jenis: menentukan faktor skala dilatasi pusat P(a,b)*

Titik $B(2, -3)$ didilatasikan terhadap titik pusat $P(-1, 1)$ menghasilkan bayangan $B'(-10, 13)$. Faktor skala dilatasi tersebut adalah ....

- A. 3  
  <sub>Salah: Lupa tanda negatif saat membagi $-9$ dengan $3$.</sub>
- **B. $-3$** ✅  
  <sub>Benar: Berdasarkan rumus $x' = k(x - a) + a$, diperoleh $-10 = k(2 - (-1)) + (-1) \iff -10 = 3k - 1 \iff 3k = -9 \iff k = -3$. Hasil ini konsisten pada ordinat $y' = -3(-3 - 1) + 1 = 13$.</sub>
- C. $-\frac{1}{3}$  
  <sub>Salah: Terbalik membagi pembilang dan penyebut saat menghitung nilai $k$.</sub>
- D. $-4$  
  <sub>Salah: Salah memindahkan konstanta sehingga menghitung $-10 - 2 = -12$ lalu dibagi $3$.</sub>

**Pembahasan:** Rumus bayangan dilatasi dengan pusat $P(a, b)$ dan faktor skala $k$ adalah:
$$x' = k(x - a) + a$$

Diketahui $x = 2$, $y = -3$, $a = -1$, $b = 1$, $x' = -10$, dan $y' = 13$.

Langkah 1: Substitusi nilai-nilai absis ke dalam rumus untuk mencari $k$.
$$-10 = k(2 - (-1)) + (-1)$$
$$-10 = k(2 + 1) - 1$$
$$-10 = 3k - 1$$
$$3k = -10 + 1$$
$$3k = -9$$
$$k = -3$$

Langkah 2: Memeriksa kesesuaian nilai $k$ pada koordinat ordinat $y$.
$$y' = k(y - b) + b = -3(-3 - 1) + 1 = -3(-4) + 1 = 12 + 1 = 13 \quad (\text{sesuai})$$

Jadi, faktor skala dilatasi tersebut adalah $-3$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas9-b03-e-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: koordinat bayangan segitiga dilatasi pusat O*

Diketahui segitiga $KLM$ memiliki koordinat titik-titik sudut $K(-1, 3)$, $L(4, 2)$, dan $M(2, -3)$. Jika segitiga tersebut didilatasikan terhadap pusat titik asal dengan faktor skala $-3$, koordinat bayangan titik-titik sudutnya adalah ....

- A. $K'(-3, 9)$, $L'(12, 6)$, dan $M'(6, -9)$  
  <sub>Salah: Siswa mengalikan dengan 3 tanpa memperhatikan tanda negatif pada faktor skala.</sub>
- **B. $K'(3, -9)$, $L'(-12, -6)$, dan $M'(-6, 9)$** ✅  
  <sub>Benar: Mengalikan setiap absis dan ordinat titik dengan faktor skala $k = -3$ menghasilkan $K'(-1 \times (-3), 3 \times (-3)) = K'(3, -9)$, $L'(4 \times (-3), 2 \times (-3)) = L'(-12, -6)$, dan $M'(2 \times (-3), -3 \times (-3)) = M'(-6, 9)$.</sub>
- C. $K'(3, -9)$, $L'(-12, -6)$, dan $M'(-6, -9)$  
  <sub>Salah: Siswa lupa mengalikan tanda minus saat mengalikan ordinat $M(-3)$ dengan $-3$.</sub>
- D. $K'(-4, 0)$, $L'(1, -1)$, dan $M'(-1, -6)$  
  <sub>Salah: Siswa menjumlahkan koordinat titik dengan faktor skala $-3$, bukan mengalikannya.</sub>

**Pembahasan:** Rumus bayangan dilatasi dengan pusat $O(0,0)$ dan faktor skala $k$ adalah $A'(kx, ky)$.
Dengan $k = -3$:
- $K(-1, 3) \rightarrow K'(-3 \times (-1), -3 \times 3) = K'(3, -9)$
- $L(4, 2) \rightarrow L'(-3 \times 4, -3 \times 2) = L'(-12, -6)$
- $M(2, -3) \rightarrow M'(-3 \times 2, -3 \times (-3)) = M'(-6, 9)$

Jadi, bayangan segitiga $KLM$ adalah $K'(3, -9)$, $L'(-12, -6)$, dan $M'(-6, 9)$.
**Acuan:** siswa — siswa hal.216 Contoh 3.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas9-b03-e-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: luas bayangan segitiga siku-siku dilatasi*

Suatu segitiga siku-siku $DEF$ siku-siku di titik $E$ memiliki panjang $DE = 5\text{ cm}$, $EF = 12\text{ cm}$, dan $DF = 13\text{ cm}$. Jika segitiga $D'E'F'$ merupakan hasil dilatasi dari segitiga $DEF$ dengan faktor skala 4, maka luas segitiga $D'E'F'$ adalah ....

- A. $960\text{ cm}^2$  
  <sub>Salah: Siswa tidak membagi dua pada rumus luas segitiga siku-siku sebelum dikalikan $k^2$ ($60 \times 16 = 960$).</sub>
- B. $120\text{ cm}^2$  
  <sub>Salah: Siswa mengalikan luas awal dengan $k$, bukan $k^2$ ($30 \times 4 = 120$).</sub>
- C. $240\text{ cm}^2$  
  <sub>Salah: Siswa lupa membagi dua pada perhitungan luas segitiga awal lalu mengalikan dengan $k$ ($60 \times 4 = 240$).</sub>
- **D. $480\text{ cm}^2$** ✅  
  <sub>Benar: Luas segitiga awal adalah $\frac{1}{2} \times 5 \times 12 = 30\text{ cm}^2$. Luas hasil dilatasi dengan faktor skala $k = 4$ adalah $k^2 \times \text{luas awal} = 16 \times 30 = 480\text{ cm}^2$.</sub>

**Pembahasan:** Langkah 1: Menghitung luas $\Delta DEF$ mula-mula:
$$\text{Luas} = \frac{1}{2} \times DE \times EF = \frac{1}{2} \times 5\text{ cm} \times 12\text{ cm} = 30\text{ cm}^2$$

Langkah 2: Menghitung luas bayangan setelah dilatasi dengan faktor skala $k = 4$:
$$\text{Luas } \Delta D'E'F' = k^2 \times \text{Luas } \Delta DEF = 4^2 \times 30 = 16 \times 30 = 480\text{ cm}^2$$
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas9-b03-e-medium-bt01-013
*variasi (angka) | C3 | 3 langkah | jenis: bayangan dua titik dilatasi pusat P(a,b)*

Diketahui titik $A(5, -1)$ dan $B(1, 4)$. Jika kedua titik tersebut didilatasikan terhadap pusat $P(2, 1)$ dengan faktor skala $-3$, koordinat bayangan titik $A$ dan $B$ berturut-turut adalah ....

- A. $A'(-9, 6)$ dan $B'(3, -9)$  
  <sub>Salah: Siswa lupa menambahkan kembali $(a, b)$ di akhir perhitungan rumus dilatasi.</sub>
- **B. $A'(-7, 7)$ dan $B'(5, -8)$** ✅  
  <sub>Benar: Menggunakan rumus $(k(x-a)+a, k(y-b)+b)$, untuk $A(5, -1)$ diperoleh $(-3(5-2)+2, -3(-1-1)+1) = (-7, 7)$ dan untuk $B(1, 4)$ diperoleh $(-3(1-2)+2, -3(4-1)+1) = (5, -8)$.</sub>
- C. $A'(-15, 3)$ dan $B'(-3, -12)$  
  <sub>Salah: Siswa mendilatasikan langsung terhadap pusat titik asal $O(0,0)$ dan mengabaikan pusat $P(2,1)$.</sub>
- D. $A'(-7, -5)$ dan $B'(5, 10)$  
  <sub>Salah: Siswa salah memperlakukan tanda negatif pada pengalian ordinat.</sub>

**Pembahasan:** Rumus bayangan dilatasi terhadap pusat $P(a, b)$ dengan faktor skala $k$:
$$x' = k(x - a) + a$$
$$y' = k(y - b) + b$$

Pusat $P(2, 1)$ sehingga $a = 2$, $b = 1$, dan $k = -3$.

Untuk titik $A(5, -1)$:
$$x' = -3(5 - 2) + 2 = -3(3) + 2 = -9 + 2 = -7$$
$$y' = -3(-1 - 1) + 1 = -3(-2) + 1 = 6 + 1 = 7$$
Jadi, $A'(-7, 7)$.

Untuk titik $B(1, 4)$:
$$x' = -3(1 - 2) + 2 = -3(-1) + 2 = 3 + 2 = 5$$
$$y' = -3(4 - 1) + 1 = -3(3) + 1 = -9 + 1 = -8$$
Jadi, $B'(5, -8)$.
**Acuan:** siswa — siswa hal.218 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas9-b03-e-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: nilai variabel koordinat dilatasi pusat P(a,b)*

Titik $A(p, -2)$ didilatasikan terhadap titik pusat $P(1, 2)$ dengan faktor skala 2 menghasilkan bayangan $A'(7, q)$. Nilai dari $p + q$ adalah ....

- **A. $-2$** ✅  
  <sub>Benar: Dari $x' = 2(p - 1) + 1 = 7$, didapat $p = 4$. Dari $y' = 2(-2 - 2) + 2 = q$, didapat $q = -6$. Nilai $p + q = 4 + (-6) = -2$.</sub>
- B. $10$  
  <sub>Salah: Siswa mengabaikan tanda minus pada $q$ sehingga menghitung $4 + 6 = 10$.</sub>
- C. $-4$  
  <sub>Salah: Siswa lupa menambahkan pusat $a=1$ pada persamaan absis sehingga diperoleh $p = 4,5$ atau keliru dalam operasi penjumlahan aljabar.</sub>
- D. $2$  
  <sub>Salah: Siswa salah tanda saat menghitung ordinat sehingga memperoleh $q = -2$ dan $p+q = 2$.</sub>

**Pembahasan:** Rumus dilatasi terhadap pusat $P(a, b)$ dengan faktor skala $k$ adalah:
$$x' = k(x - a) + a$$
$$y' = k(y - b) + b$$

Diketahui $P(1, 2) \rightarrow a = 1, b = 2$, dan faktor skala $k = 2$.

1. Menentukan nilai $p$ dari absis bayangan:
$$7 = 2(p - 1) + 1$$
$$6 = 2(p - 1)$$
$$3 = p - 1 \implies p = 4$$

2. Menentukan nilai $q$ dari ordinat bayangan:
$$q = 2(-2 - 2) + 2$$
$$q = 2(-4) + 2 = -8 + 2 = -6$$

3. Menghitung $p + q$:
$$p + q = 4 + (-6) = -2$$
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas9-b03-e-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: panjang ruas garis bayangan dilatasi*

Diketahui ruas garis menghubungkan titik $A(2, 1)$ dan $B(5, 5)$. Ruas garis tersebut didilatasikan terhadap titik pusat tertentu dengan faktor skala $-3$ sehingga menghasilkan bayangan ruas garis $A'B'$. Panjang ruas garis $A'B'$ adalah ....

- A. $45\text{ satuan}$  
  <sub>Salah: Siswa mengalikan panjang ruas garis dengan $k^2 = 9$ karena tertukar dengan sifat perbesaran luas.</sub>
- B. $-15\text{ satuan}$  
  <sub>Salah: Siswa mengalikan panjang ruas garis dengan faktor skala negatif tanpa mengambil nilai mutlak panjang garis.</sub>
- **C. $15\text{ satuan}$** ✅  
  <sub>Benar: Panjang awal $AB = \sqrt{(5-2)^2 + (5-1)^2} = \sqrt{9+16} = 5\text{ satuan}$. Panjang bayangan adalah $|k| \times AB = |-3| \times 5 = 15\text{ satuan}$.</sub>
- D. $5\text{ satuan}$  
  <sub>Salah: Siswa hanya menghitung panjang ruas garis awal $AB$ dan lupa mengalikannya dengan faktor skala.</sub>

**Pembahasan:** Langkah 1: Menghitung panjang ruas garis $AB$ mula-mula dengan rumus jarak dua titik:
$$AB = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$
$$AB = \sqrt{(5 - 2)^2 + (5 - 1)^2} = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5\text{ satuan}$$

Langkah 2: Sifat dilatasi menyatakan bahwa panjang bayangan suatu segmen garis berbanding lurus dengan nilai mutlak faktor skalanya:
$$A'B' = |k| \times AB$$
$$A'B' = |-3| \times 5 = 3 \times 5 = 15\text{ satuan}$$
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas9-b03-e-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi koordinat dilatasi*

Titik $D(5, -1)$ dan $E(-3, 7)$ didilatasikan terhadap pusat $P(1, 3)$ dengan faktor skala $k = -2$ berturut-turut menghasilkan bayangan $D'$ dan $E'$. Seorang siswa menyatakan bahwa titik tengah ruas garis yang menghubungkan bayangan $D'$ dan $E'$ terletak di titik $(-1, 3)$. Evaluasi yang tepat terhadap pernyataan siswa tersebut adalah ....

- A. salah, titik tengah ruas garis $D'E'$ yang sebenarnya berada di titik $(-7, 11)$  
  <sub>Salah: Siswa keliru mengira titik bayangan pertama sebagai titik tengah ruas garis.</sub>
- B. benar, titik tengah ruas garis $D'E'$ memang terletak di titik $(-1, 3)$  
  <sub>Salah: Siswa salah menghitung tanda saat mencari rata-rata absis bayangan $(-7+9)/2$ menjadi $-1$.</sub>
- **C. salah, titik tengah ruas garis $D'E'$ yang sebenarnya berada di titik $(1, 3)$** ✅  
  <sub>Benar: Koordinat bayangan $D'$ adalah $(-2(5-1)+1, -2(-1-3)+3) = (-7, 11)$ dan bayangan $E'$ adalah $(-2(-3-1)+1, -2(7-3)+3) = (9, -5)$. Titik tengah ruas garis $D'E'$ adalah $(\frac{-7+9}{2}, \frac{11+(-5)}{2}) = (1, 3)$, sehingga klaim siswa salah.</sub>
- D. salah, titik tengah ruas garis $D'E'$ yang sebenarnya berada di titik $(1, -3)$  
  <sub>Salah: Siswa salah menerapkan tanda positif pada koordinat pusat saat menghitung titik tengah.</sub>

**Pembahasan:** Langkah 1: Menentukan bayangan titik $D(5, -1)$ oleh dilatasi $[P(1, 3), -2]$:
$x_{D'} = -2(5 - 1) + 1 = -2(4) + 1 = -7$
$y_{D'} = -2(-1 - 3) + 3 = -2(-4) + 3 = 11$
Diperoleh $D'(-7, 11)$.

Langkah 2: Menentukan bayangan titik $E(-3, 7)$ oleh dilatasi $[P(1, 3), -2]$:
$x_{E'} = -2(-3 - 1) + 1 = -2(-4) + 1 = 9$
$y_{E'} = -2(7 - 3) + 3 = -2(4) + 3 = -5$
Diperoleh $E'(9, -5)$.

Langkah 3: Menghitung koordinat titik tengah ruas garis $D'E'$:
$x_m = \frac{-7 + 9}{2} = \frac{2}{2} = 1$
$y_m = \frac{11 + (-5)}{2} = \frac{6}{2} = 3$
Titik tengah ruas garis $D'E'$ adalah $(1, 3)$.

Langkah 4: Evaluasi klaim:
Klaim siswa bahwa titik tengah berada di $(-1, 3)$ bernilai salah. Koordinat yang tepat adalah $(1, 3)$.
**Acuan:** siswa — siswa hal.218 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas9-b03-e-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: evaluasi garis invarian*

Garis $g$ memiliki persamaan $2x - 3y + 6 = 0$. Garis tersebut didilatasikan dengan faktor skala $k = -3$ terhadap pusat titik asal $O(0,0)$ menghasilkan bayangan garis $g'$. Perhatikan pernyataan-pernyataan berikut:
(1) Gradien garis bayangan $g'$ berlawanan tanda dengan gradien garis $g$.
(2) Persamaan bayangan garis $g'$ adalah $2x - 3y - 18 = 0$.
(3) Garis $g$ sejajar dengan garis bayangan $g'$.
(4) Jarak titik asal $O(0,0)$ ke garis bayangan $g'$ adalah 3 kali jarak titik asal ke garis $g$.

Pernyataan yang bernilai BENAR adalah ....

- A. (1) dan (3) saja  
  <sub>Salah: Siswa salah dalam aljabar penentuan persamaan bayangan garis serta menganggap pernyataan (1) benar.</sub>
- B. (1), (2), dan (3)  
  <sub>Salah: Siswa mengira tanda negatif pada faktor skala dilatasi membalikkan nilai kemiringan/gradien garis.</sub>
- C. (2) dan (4) saja  
  <sub>Salah: Siswa keliru mengira garis bayangan tidak sejajar karena orientasi bayangan berlawanan arah dari pusat.</sub>
- **D. (2), (3), dan (4)** ✅  
  <sub>Benar: Substitusi $x = -\frac{x'}{3}$ dan $y = -\frac{y'}{3}$ ke $2x-3y+6=0$ menghasilkan $2x'-3y'-18=0$ (pernyataan (2) benar). Dilatasi memetakan garis ke garis yang sejajar dengannya, sehingga gradien garis sama dan pernyataan (3) benar, sedangkan (1) salah. Jarak garis ke pusat dilatasi berubah sesuai $|k| = 3$ kali (pernyataan (4) benar).</sub>

**Pembahasan:** Langkah 1: Menentukan hubungan koordinat awal $(x, y)$ dan bayangan $(x', y')$ oleh dilatasi $[O, -3]$:
$x' = -3x \Rightarrow x = -\frac{x'}{3}$
$y' = -3y \Rightarrow y = -\frac{y'}{3}$.

Langkah 2: Menentukan persamaan bayangan garis $g'$:
Substitusikan ke persamaan $2x - 3y + 6 = 0$:
$2\left(-\frac{x'}{3}\right) - 3\left(-\frac{y'}{3}\right) + 6 = 0$
$-\frac{2}{3}x' + y' + 6 = 0$
Kalikan kedua ruas dengan $-3$:
$2x' - 3y' - 18 = 0$.
Maka pernyataan (2) BENAR.

Langkah 3: Menganalisis gradien dan kedudukan garis:
Gradien garis $g$ adalah $m = -\frac{2}{-3} = \frac{2}{3}$.
Gradien garis $g'$ adalah $m' = -\frac{2}{-3} = \frac{2}{3}$.
Karena gradiennya sama ($m = m'$), kedua garis saling sejajar (pernyataan (3) BENAR) dan pernyataan (1) SALAH.

Langkah 4: Menganalisis jarak dari titik asal ke garis:
Pada transformasi dilatasi dengan pusat $O(0,0)$ dan faktor skala $k$, jarak setiap titik dan garis bayangan terhadap titik pusat menjadi $|k|$ kali jarak semula. Karena $|k| = |-3| = 3$, jarak titik pusat ke garis $g'$ adalah 3 kali jarak ke garis $g$ (pernyataan (4) BENAR).

Jadi, pernyataan yang bernilai benar adalah (2), (3), dan (4).
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas9-b03-e-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: kombinasi dilatasi dan translasi*

Titik $A(p, 4)$ didilatasikan terhadap titik pusat $P(2, -1)$ dengan faktor skala $k = 3$ menghasilkan bayangan $A'$. Selanjutnya, titik $A'$ ditranslasikan oleh $\begin{pmatrix} -4 \\ 5 \end{pmatrix}$ sehingga menghasilkan bayangan akhir $A''(4, q)$. Nilai dari $2p - q$ adalah ....

- **A. -11** ✅  
  <sub>Benar: Dari translasi, absis bayangan pertama $x_{A'} - 4 = 4 \Rightarrow x_{A'} = 8$. Menggunakan rumus dilatasi: $8 = 3(p - 2) + 2 \Rightarrow 6 = 3(p - 2) \Rightarrow p = 4$. Ordinat dilatasi: $y_{A'} = 3(4 - (-1)) + (-1) = 3(5) - 1 = 14$. Ordinat akhir setelah translasi: $q = 14 + 5 = 19$. Maka $2p - q = 2(4) - 19 = 8 - 19 = -11$.</sub>
- B. 5  
  <sub>Salah: Siswa salah tanda saat translasi atau keliru mengurangkan pada langkah akhir.</sub>
- C. -19  
  <sub>Salah: Siswa lupa mengalikan $p$ dengan koefisien 2 sehingga hanya menghitung $p - q = 4 - 19 = -15$ atau salah perhitungan aljabar.</sub>
- D. -3  
  <sub>Salah: Siswa salah menghitung rumus ordinat bayangan dilatasi menjadi $3(4) - 1 = 11$, sehingga $q = 16$ dan $2p - q = 8 - 16 = -8$ atau salah substitusi lainnya.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat $A'(x', y')$ dari proses translasi ke bayangan akhir $A''(4, q)$:
$x'' = x' + (-4) \Rightarrow 4 = x' - 4 \Rightarrow x' = 8$.
$y'' = y' + 5 \Rightarrow q = y' + 5$.

Langkah 2: Menentukan nilai $p$ dari dilatasi titik asal $A(p, 4)$ dengan pusat $P(2, -1)$ dan $k = 3$:
$x' = k(x - a) + a$
$8 = 3(p - 2) + 2$
$6 = 3(p - 2)$
$p - 2 = 2$
$p = 4$.

Langkah 3: Menentukan ordinat hasil dilatasi $y'$:
$y' = k(y - b) + b$
$y' = 3(4 - (-1)) + (-1)$
$y' = 3(5) - 1$
$y' = 14$.

Langkah 4: Menentukan nilai $q$:
$q = y' + 5 = 14 + 5 = 19$.

Langkah 5: Menghitung nilai $2p - q$:
$2p - q = 2(4) - 19 = 8 - 19 = -11$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas9-b03-e-hard-bt01-004
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi sifat dilatasi*

Perhatikan pernyataan berikut:
"Jika suatu segitiga sama sisi didilatasikan terhadap titik pusat asal $O(0,0)$ dengan faktor skala $k = -3$, maka luas bayangan segitiga tersebut menjadi $9$ kali luas segitiga awal dan letak bayangannya berlawanan arah terhadap pusat dilatasi dari posisi awal."

Evaluasi yang paling tepat mengenai kebenaran pernyataan tersebut beserta alasannya adalah ....

- A. Salah, karena perbesaran luas sebanding langsung dengan nilai mutlak faktor skala, sehingga luas bayangan seharusnya hanya menjadi $3$ kali luas segitiga awal.  
  <sub>Salah: Siswa keliru menganggap rasio luas sebanding dengan $|k|$, bukan $k^2$.</sub>
- **B. Benar, karena perbandingan luas bayangan dengan luas awal adalah $k^2 = (-3)^2 = 9$ dan tanda negatif pada faktor skala menunjukkan letak bayangan berlawanan arah dari titik pusat dilatasi.** ✅  
  <sub>Benar: Rasio luas bayangan terhadap luas awal adalah $k^2 = (-3)^2 = 9$, dan faktor skala negatif $k < 0$ menunjukkan letak bayangan berlawanan arah terhadap pusat dari titik asal.</sub>
- C. Salah, karena faktor skala bernilai negatif sehingga luas bayangan seharusnya bernilai negatif, yaitu $-9$ kali luas segitiga awal.  
  <sub>Salah: Siswa keliru menganggap nilai luas bangun dapat bertanda negatif akibat faktor skala bernilai negatif.</sub>
- D. Salah, karena tanda negatif pada faktor skala selalu menyebabkan bayangan mengalami pengecilan ukuran dari bentuk aslinya.  
  <sub>Salah: Siswa keliru mengira tanda minus selalu berarti pengecilan ukuran, tanpa melihat bahwa $|k| = 3 > 1$.</sub>

**Pembahasan:** Pada transformasi dilatasi dengan faktor skala $k$:
1. Hubungan luas bayangan ($L'$) dengan luas awal ($L$) memenuhi rumus perbandingan luas $L' = k^2 \times L$. Dengan $k = -3$, diperoleh $L' = (-3)^2 \times L = 9L$. Jadi, luas bayangan benar menjadi 9 kali luas semula.
2. Berdasarkan Sifat 3.9, faktor skala bernilai negatif ($k < 0$) menunjukkan bahwa arah posisi titik bayangan $A'$ berlawanan arah dengan ruas garis $OA$ terhadap titik pusat $O$.
Oleh karena kedua bagian klaim tepat, maka pernyataan tersebut bernilai benar.
**Acuan:** siswa — siswa hal.224 Uji Pemahaman

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas9-b03-e-hard-bt01-005
*variasi (konteks) | C5 | 4 langkah | jenis: perhitungan selisih luas dilatasi*

Suatu trapesium siku-siku $ABCD$ memiliki panjang sisi sejajar $AB = 10\text{ cm}$ dan $CD = 6\text{ cm}$, serta tinggi $AD = 8\text{ cm}$. Trapesium $A'B'C'D'$ merupakan hasil dilatasi dari trapesium $ABCD$ dengan faktor skala $k = -\frac{5}{2}$. Selisih luas antara trapesium bayangan $A'B'C'D'$ dan trapesium mula-mula $ABCD$ adalah ....

- **A. $336\text{ cm}^2$** ✅  
  <sub>Benar: Luas awal $= 64\text{ cm}^2$, luas bayangan $= 64 \times (-\frac{5}{2})^2 = 400\text{ cm}^2$, sehingga selisihnya $= 400 - 64 = 336\text{ cm}^2$.</sub>
- B. $464\text{ cm}^2$  
  <sub>Salah: Siswa keliru menjumlahkan luas bayangan dan luas awal alih-alih mencari selisihnya.</sub>
- C. $400\text{ cm}^2$  
  <sub>Salah: Siswa hanya menghitung luas trapesium bayangan tanpa menghitung selisihnya terhadap trapesium awal.</sub>
- D. $96\text{ cm}^2$  
  <sub>Salah: Siswa keliru mengalikan luas dengan $|k| = 2{,}5$ bukan $k^2 = 6{,}25$, sehingga $160 - 64 = 96\text{ cm}^2$.</sub>

**Pembahasan:** Langkah 1: Hitung luas trapesium awal $ABCD$.
$L = \frac{AB + CD}{2} \times AD = \frac{10 + 6}{2} \times 8 = 8 \times 8 = 64\text{ cm}^2$.

Langkah 2: Tentukan faktor pengali luas oleh dilatasi dengan $k = -\frac{5}{2}$.
Pengali luas $= k^2 = \left(-\frac{5}{2}\right)^2 = \frac{25}{4}$.

Langkah 3: Hitung luas trapesium bayangan $A'B'C'D'$.
$L' = \frac{25}{4} \times 64 = 25 \times 16 = 400\text{ cm}^2$.

Langkah 4: Hitung selisih luas trapesium bayangan dan trapesium awal.
$\Delta L = L' - L = 400\text{ cm}^2 - 64\text{ cm}^2 = 336\text{ cm}^2$.
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas9-b03-e-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi komposisi dilatasi*

Perhatikan empat pernyataan berikut terkait segitiga $ABC$ dengan koordinat $A(1, 2)$, $B(5, 2)$, dan $C(3, 6)$ yang didilatasikan berturut-turut terhadap pusat titik asal $O(0,0)$ dengan faktor skala $k_1 = -2$ menghasilkan $\Delta A_1B_1C_1$, kemudian bayangan tersebut didilatasikan kembali terhadap pusat $O(0,0)$ dengan faktor skala $k_2 = \frac{3}{2}$ menghasilkan $\Delta A_2B_2C_2$:
(1) Faktor skala total dilatasi dari segitiga awal ke segitiga $\Delta A_2B_2C_2$ adalah $-3$.
(2) Luas $\Delta A_2B_2C_2$ adalah $9$ kali luas $\Delta ABC$.
(3) Koordinat titik sudut $C_2$ adalah $(-9, -18)$.
(4) Keliling $\Delta A_2B_2C_2$ adalah $-3$ kali keliling $\Delta ABC$.

Pernyataan yang benar adalah ....

- A. (1), (2), (3), dan (4)  
  <sub>Salah: Siswa tidak menyadari bahwa panjang dan keliling tidak mungkin bernilai rasio negatif terhadap ukuran awal.</sub>
- B. (2) dan (4) saja  
  <sub>Salah: Siswa keliru menganggap rasio keliling boleh bernilai negatif dan salah menganalisis faktor skala total.</sub>
- **C. (1), (2), dan (3)** ✅  
  <sub>Benar: Pernyataan (1), (2), dan (3) benar; sedangkan (4) salah karena keliling merupakan besaran panjang geometris yang selalu bernilai positif sehingga perbandingannya adalah $|k| = 3$.</sub>
- D. (1) dan (3) saja  
  <sub>Salah: Siswa keliru mengira luas bayangan tidak mengikuti aturan kuadrat faktor skala total.</sub>

**Pembahasan:** Langkah 1: Menentukan faktor skala total.
Komposisi dua dilatasi berturut-turut terhadap pusat yang sama memiliki faktor skala total:
$k = k_1 \times k_2 = (-2) \times \frac{3}{2} = -3$. (Pernyataan 1 BENAR)

Langkah 2: Menentukan rasio luas.
Rasio perbesaran luas dari dilatasi adalah $k^2 = (-3)^2 = 9$.
Jadi luas $\Delta A_2B_2C_2 = 9 \times \text{luas } \Delta ABC$. (Pernyataan 2 BENAR)

Langkah 3: Menentukan koordinat bayangan titik $C$.
Koordinat titik $C(3, 6)$ didilatasikan dengan faktor skala $k = -3$ terhadap pusat $O(0,0)$:
$C_2 = (-3 \times 3, -3 \times 6) = (-9, -18)$. (Pernyataan 3 BENAR)

Langkah 4: Menentukan rasio keliling.
Keliling merupakan ukuran panjang, sehingga faktor pengali keliling adalah nilai mutlak dari faktor skala, yaitu $|k| = |-3| = 3$. Ukuran keliling tidak dapat berbanding negatif. (Pernyataan 4 SALAH)

Dengan demikian, pernyataan yang benar adalah (1), (2), dan (3).
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas9-b03-e-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: analisis perbandingan luas bertingkat*

Persegi panjang $ABCD$ berukuran panjang $12\text{ cm}$ dan lebar $8\text{ cm}$. Persegi panjang tersebut didilatasikan oleh $[P, -\frac{3}{2}]$ menghasilkan $A'B'C'D'$. Selanjutnya, $A'B'C'D'$ didilatasikan kembali oleh $[Q, \frac{1}{3}]$ menghasilkan $A''B''C''D''$. Selisih luas antara bangun awal $ABCD$ dan bangun akhir $A''B''C''D''$ adalah ....

- A. $120\text{ cm}^2$  
  <sub>Salah: Menjumlahkan luas awal dan luas akhir</sub>
- **B. $72\text{ cm}^2$** ✅  
  <sub>Benar: Luas awal $L_0 = 12 \times 8 = 96\text{ cm}^2$. Luas setelah dilatasi pertama: $L_1 = k_1^2 \times L_0 = (-\frac{3}{2})^2 \times 96 = \frac{9}{4} \times 96 = 216\text{ cm}^2$. Luas akhir: $L_2 = k_2^2 \times L_1 = (\frac{1}{3})^2 \times 216 = \frac{1}{9} \times 216 = 24\text{ cm}^2$. Selisih luas bangun awal dan akhir = $|96 - 24| = 72\text{ cm}^2$.</sub>
- C. $48\text{ cm}^2$  
  <sub>Salah: Menggunakan faktor linear bukan kuadrat: $k = (3/2) \times (1/3) = 1/2$, $L_2 = 96 \times (1/2) = 48$, selisih $96 - 48 = 48$</sub>
- D. $64\text{ cm}^2$  
  <sub>Salah: Salah mengalikan kuadrat pecahan skala</sub>

**Pembahasan:** Luas awal $L_0 = 12 \times 8 = 96\text{ cm}^2$. Faktor skala gabungan kedua dilatasi pada luas adalah $K = k_1^2 \times k_2^2 = (-\frac{3}{2})^2 \times (\frac{1}{3})^2 = \frac{9}{4} \times \frac{1}{9} = \frac{1}{4}$. Luas bayangan akhir $L_2 = \frac{1}{4} \times 96 = 24\text{ cm}^2$. Selisih luas awal dan akhir $= 96 - 24 = 72\text{ cm}^2$.
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas9-b03-e-hard-bt01-008
*variasi (konteks) | C5 | 5 langkah | jenis: penentuan faktor skala dilatasi*

Segitiga $KLM$ memiliki koordinat titik-titik sudut $K(4, 2)$, $L(10, 2)$, dan $M(7, 6)$. Segitiga tersebut didilatasikan terhadap titik pusat $P(-1, 5)$ dengan faktor skala $k$ sehingga menghasilkan segitiga $K'L'M'$. Jika luas bayangan segitiga $K'L'M'$ adalah $192\text{ satuan luas}$ dan letak bangun bayangan berlawanan arah dengan bangun awal terhadap titik pusat dilatasi, maka nilai faktor skala $k$ adalah ....

- **A. $-4$** ✅  
  <sub>Benar: Luas awal segitiga adalah $\frac{1}{2} \times (10 - 4) \times (6 - 2) = 12\text{ satuan luas}$. Dari hubungan luas dilatasi, $k^2 = \frac{192}{12} = 16$. Karena letak bayangan berlawanan arah terhadap pusat dilatasi, faktor skala bernilai negatif, yaitu $k = -4$.</sub>
- B. $16$  
  <sub>Salah: Siswa menganggap rasio luas bayangan terhadap luas mula-mula adalah faktor skala dilatasi itu sendiri.</sub>
- C. $4$  
  <sub>Salah: Siswa mengabaikan keterangan letak bayangan berlawanan arah sehingga hanya mengambil akar kuadrat positif.</sub>
- D. $-16$  
  <sub>Salah: Siswa keliru menganggap rasio luas sebanding secara linier dengan $k$ (bukan $k^2$) lalu memberi tanda negatif.</sub>

**Pembahasan:** Langkah 1: Menentukan panjang alas segitiga $KLM$.
Karena titik $K(4, 2)$ dan $L(10, 2)$ memiliki ordinat sama, panjang alasnya adalah:
$\text{alas} = 10 - 4 = 6\text{ satuan}$.

Langkah 2: Menentukan tinggi segitiga $KLM$.
Tinggi segitiga adalah jarak vertikal dari titik puncak $M(7, 6)$ ke garis alas $y = 2$:
$\text{tinggi} = 6 - 2 = 4\text{ satuan}$.

Langkah 3: Menghitung luas awal segitiga $KLM$.
$L = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 6 \times 4 = 12\text{ satuan luas}$.

Langkah 4: Menghitung nilai $k^2$ menggunakan hubungan luas dilatasi.
$L' = k^2 \times L$
$192 = k^2 \times 12$
$k^2 = \frac{192}{12} = 16$
$k = 4$ atau $k = -4$.

Langkah 5: Mengevaluasi nilai $k$ berdasarkan arah bayangan.
Berdasarkan sifat dilatasi, jika letak bayangan berlawanan arah dengan letak bangun awal terhadap titik pusat dilatasi, maka faktor skala harus bernilai negatif ($k < 0$).
Oleh karena itu, nilai faktor skala yang memenuhi adalah $k = -4$.
**Acuan:** pretest — kelas9-b03-p0221-latihan-e-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas9-b03-e-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: analisis jarak bayangan dilatasi*

Titik $A(4, 6)$ didilatasikan terhadap titik pusat $P(1, 2)$ dengan faktor skala $k = -3$ sehingga menghasilkan bayangan titik $A'$. Jarak antara titik bayangan $A'$ dengan titik $C(4, -5)$ adalah ....

- A. $15\text{ satuan}$  
  <sub>Salah: Menghitung jarak bayangan $A'$ ke pusat dilatasi $P$, bukan ke titik $C$.</sub>
- B. $17\text{ satuan}$  
  <sub>Salah: Menjumlahkan langsung selisih koordinat $|12| + |5| = 17$ tanpa menggunakan rumus jarak Euclidean.</sub>
- C. $11\text{ satuan}$  
  <sub>Salah: Menghitung jarak titik awal $A(4, 6)$ ke titik $C(4, -5)$, yaitu $|6 - (-5)| = 11$.</sub>
- **D. $13\text{ satuan}$** ✅  
  <sub>Benar: Koordinat bayangan adalah $A'(-3(4 - 1) + 1, -3(6 - 2) + 2) = A'(-8, -10)$. Jarak $A'$ ke $C(4, -5)$ adalah $\sqrt{(4 - (-8))^2 + (-5 - (-10))^2} = \sqrt{12^2 + 5^2} = 13\text{ satuan}$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat bayangan $A'$ hasil dilatasi titik $A(4, 6)$ terhadap pusat $P(1, 2)$ dengan faktor skala $k = -3$:
$$x' = k(x - a) + a = -3(4 - 1) + 1 = -3(3) + 1 = -9 + 1 = -8$$
$$y' = k(y - b) + b = -3(6 - 2) + 2 = -3(4) + 2 = -12 + 2 = -10$$
Diperoleh $A'(-8, -10)$.

Langkah 2: Menghitung jarak antara titik $A'(-8, -10)$ dan titik $C(4, -5)$:
$$d = \sqrt{(x_C - x')^2 + (y_C - y')^2}$$
$$d = \sqrt{(4 - (-8))^2 + (-5 - (-10))^2}$$
$$d = \sqrt{12^2 + 5^2} = \sqrt{144 + 25} = \sqrt{169} = 13\text{ satuan}$$

Jadi, jarak antara titik $A'$ dan titik $C$ adalah $13\text{ satuan}$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas9-b03-e-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: pemecahan masalah keliling dilatasi*

Belah ketupat $ABCD$ memiliki koordinat titik-titik sudut $A(-4, 0)$, $B(0, 3)$, $C(4, 0)$, dan $D(0, -3)$. Belah ketupat tersebut didilatasikan terhadap pusat $O(0,0)$ dengan faktor skala $k$ sehingga menghasilkan bayangan $A'B'C'D'$. Jika luas belah ketupat $A'B'C'D'$ adalah $216\text{ satuan luas}$, keliling dari belah ketupat bayangan $A'B'C'D'$ adalah ....

- A. $84\text{ satuan}$  
  <sub>Salah: Salah menghitung panjang sisi dengan menjumlahkan langsung setengah diagonal $4 + 3 = 7$ tanpa menggunakan rumus Pythagoras, lalu mengalikannya dengan 4 dan $|k| = 3$.</sub>
- **B. $60\text{ satuan}$** ✅  
  <sub>Benar: Luas awal adalah $\frac{1}{2} \times 8 \times 6 = 24$. Faktor skala memenuhi $k^2 = \frac{216}{24} = 9 \implies |k| = 3$. Panjang sisi awal adalah $\sqrt{4^2 + 3^2} = 5$, sehingga keliling awal $4 \times 5 = 20$. Keliling bayangan adalah $|k| \times 20 = 3 \times 20 = 60\text{ satuan}$.</sub>
- C. $20\text{ satuan}$  
  <sub>Salah: Hanya menghitung keliling belah ketupat awal dan lupa mengalikannya dengan faktor skala dilatasi.</sub>
- D. $180\text{ satuan}$  
  <sub>Salah: Mengalikan keliling awal dengan perbandingan luas $k^2 = 9$, bukan dengan faktor skala $|k| = 3$.</sub>

**Pembahasan:** Langkah 1: Menghitung panjang diagonal dan luas belah ketupat awal $ABCD$:
$$d_1 = AC = 4 - (-4) = 8$$
$$d_2 = BD = 3 - (-3) = 6$$
$$L_0 = \frac{1}{2} \times d_1 \times d_2 = \frac{1}{2} \times 8 \times 6 = 24\text{ satuan luas}$$

Langkah 2: Menentukan nilai mutlak faktor skala $|k|$ dari perbandingan luas:
$$L' = k^2 \times L_0$$
$$216 = k^2 \times 24$$
$$k^2 = \frac{216}{24} = 9 \implies |k| = 3$$

Langkah 3: Menghitung panjang sisi dan keliling belah ketupat awal:
$$s = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5\text{ satuan}$$
$$K_0 = 4 \times s = 4 \times 5 = 20\text{ satuan}$$

Langkah 4: Menghitung keliling belah ketupat bayangan $A'B'C'D'$:
$$K' = |k| \times K_0 = 3 \times 20 = 60\text{ satuan}$$

Jadi, keliling belah ketupat bayangan adalah $60\text{ satuan}$.
**Acuan:** siswa — siswa hal.216

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas9-b03-e-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: rekonstruksi koordinat dilatasi*

Titik $A(4, -1)$ didilatasikan terhadap titik pusat $P(a, b)$ dengan faktor skala $-2$ menghasilkan bayangan $A'(-5, 8)$. Titik lain, yaitu $B(p, q)$, didilatasikan terhadap titik pusat $P(a, b)$ yang sama dengan faktor skala 3 sehingga menghasilkan bayangan $B'(13, -10)$. Nilai dari $p - q$ adalah ....

- **A. 7** ✅  
  <sub>Benar: Dari dilatasi titik $A$ diperoleh pusat $P(1, 2)$. Dari dilatasi titik $B$ dengan pusat $P(1, 2)$ dan faktor skala 3 diperoleh $p = 5$ dan $q = -2$, sehingga nilai $p - q = 5 - (-2) = 7$.</sub>
- B. 3  
  <sub>Salah: Siswa menjumlahkan nilai $p$ dan $q$ alih-alih mengurangkannya ($5 + (-2) = 3$).</sub>
- C. 11  
  <sub>Salah: Siswa melakukan kesalahan tanda saat memindahkan ruas pada persamaan $3q - 4 = -10$ sehingga diperoleh $q = -6$, lalu menghitung $5 - (-6) = 11$.</sub>
- D. -7  
  <sub>Salah: Siswa terbalik melakukan pengurangan koordinat menjadi $q - p = -2 - 5 = -7$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat pusat dilatasi $P(a, b)$ menggunakan titik $A(4, -1)$, faktor skala $k_1 = -2$, dan bayangan $A'(-5, 8)$:
$x_{A'} = k_1(x_A - a) + a$
$-5 = -2(4 - a) + a$
$-5 = -8 + 2a + a$
$-5 = 3a - 8$
$3a = 3 \implies a = 1$

$y_{A'} = k_1(y_A - b) + b$
$8 = -2(-1 - b) + b$
$8 = 2 + 2b + b$
$8 = 3b + 2$
$3b = 6 \implies b = 2$
Diperoleh pusat dilatasi $P(1, 2)$.

Langkah 2: Menentukan koordinat titik awal $B(p, q)$ dari bayangan $B'(13, -10)$ dengan pusat $P(1, 2)$ dan faktor skala $k_2 = 3$:
$x_{B'} = k_2(p - a) + a$
$13 = 3(p - 1) + 1$
$13 = 3p - 3 + 1$
$13 = 3p - 2$
$3p = 15 \implies p = 5$

$y_{B'} = k_2(q - b) + b$
$-10 = 3(q - 2) + 2$
$-10 = 3q - 6 + 2$
$-10 = 3q - 4$
$3q = -6 \implies q = -2$

Langkah 3: Menghitung nilai $p - q$:
$p - q = 5 - (-2) = 5 + 2 = 7$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas9-b03-e-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: analisis sistem dilatasi*

Titik $A(3, 5)$ dan $B(-1, 4)$ didilatasikan terhadap titik pusat yang sama, yaitu $P(a, b)$, dengan faktor skala $k$. Dilatasi tersebut menghasilkan bayangan berturut-turut $A'(-3, -4)$ dan $B'(5, -2)$. Nilai dari $k + a + b$ adalah ....

- A. 5  
  <sub>Salah: Siswa mengabaikan tanda negatif pada faktor skala sehingga mengambil nilai mutlak $k = 2$, lalu menghitung $2 + 1 + 2 = 5$.</sub>
- **B. 1** ✅  
  <sub>Benar: Perubahan koordinat dari $A$ ke $B$ adalah $\Delta x = -1 - 3 = -4$ dan $\Delta y = 4 - 5 = -1$. Perubahan koordinat dari $A'$ ke $B'$ adalah $\Delta x' = 5 - (-3) = 8$ dan $\Delta y' = -2 - (-4) = 2$. Faktor skala diperoleh dari perbandingan: $k = \frac{8}{-4} = \frac{2}{-1} = -2$. Menggunakan rumus dilatasi terhadap $P(a, b)$: $x_{A'} = k(x_A - a) + a \implies -3 = -2(3 - a) + a \implies -3 = -6 + 3a \implies 3a = 3 \implies a = 1$. Lalu, $y_{A'} = k(y_A - b) + b \implies -4 = -2(5 - b) + b \implies -4 = -10 + 3b \implies 3b = 6 \implies b = 2$. Jadi, $k + a + b = -2 + 1 + 2 = 1$.</sub>
- C. 3  
  <sub>Salah: Siswa hanya menjumlahkan koordinat titik pusat $a + b = 1 + 2 = 3$ dan lupa mengikutsertakan nilai $k$.</sub>
- D. 7  
  <sub>Salah: Siswa melakukan kesalahan aljabar saat membagi koefisien variabel pusat: $3a = 3$ disimpulkan $a = 3$ dan $3b = 6$ disimpulkan $b = 6$, sehingga $-2 + 3 + 6 = 7$.</sub>

**Pembahasan:** Langkah 1: Menentukan komponen pergeseran titik awal dan titik bayangan.
$\vec{AB} = (-1 - 3, 4 - 5) = (-4, -1)$
$\vec{A'B'} = (5 - (-3), -2 - (-4)) = (8, 2)$

Langkah 2: Menentukan nilai faktor skala $k$.
$\vec{A'B'} = k \cdot \vec{AB} \implies (8, 2) = k(-4, -1) \implies k = -2$

Langkah 3: Menentukan koordinat pusat dilatasi $P(a, b)$ dari bayangan titik $A(3, 5) \to A'(-3, -4)$.
$x' = k(x - a) + a$
$-3 = -2(3 - a) + a$
$-3 = -6 + 2a + a$
$-3 + 6 = 3a$
$3a = 3 \implies a = 1$

$y' = k(y - b) + b$
$-4 = -2(5 - b) + b$
$-4 = -10 + 2b + b$
$-4 + 10 = 3b$
$3b = 6 \implies b = 2$

Langkah 4: Menghitung nilai $k + a + b$.
$k + a + b = -2 + 1 + 2 = 1$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas9-b03-e-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi kebenaran sifat dilatasi*

Persegi panjang $PQRS$ memiliki koordinat titik-titik sudut $P(-1, 1)$, $Q(5, 1)$, $R(5, 4)$, dan $S(-1, 4)$. Bangun tersebut didilatasikan terhadap titik pusat $T(2, 2)$ dengan faktor skala $k = -\frac{1}{2}$ menghasilkan bayangan $P'Q'R'S'$.

Perhatikan pernyataan-pernyataan berikut:
(1) Koordinat titik bayangan $R'$ adalah $(0,5; 1)$.
(2) Luas persegi panjang bayangan $P'Q'R'S'$ adalah $4,5\text{ satuan luas}$.
(3) Keliling persegi panjang bayangan $P'Q'R'S'$ adalah $9\text{ satuan}$.
(4) Letak bangun bayangan $P'Q'R'S'$ searah dengan letak bangun awal terhadap titik pusat $T$.

Pernyataan yang benar berdasarkan stimulus tersebut ditunjukkan oleh nomor ....

- A. (1) dan (3) saja  
  <sub>Salah: Siswa keliru mengira perbandingan luas berbanding lurus dengan nilai $|k|$, bukan $k^2$.</sub>
- B. (1), (2), (3), dan (4)  
  <sub>Salah: Siswa menganggap semua pernyataan benar tanpa mengevaluasi implikasi arah dari faktor skala negatif pada pernyataan (4).</sub>
- **C. (1), (2), dan (3)** ✅  
  <sub>Benar: Pernyataan (1) benar karena $R'(0,5; 1)$, pernyataan (2) benar karena luas bayangan $(-1/2)^2 \times 18 = 4,5$, dan pernyataan (3) benar karena keliling bayangan $|-1/2| \times 18 = 9$. Pernyataan (4) salah karena nilai $k$ negatif menyebabkan letak bayangan berlawanan arah terhadap pusat.</sub>
- D. (2) dan (4) saja  
  <sub>Salah: Siswa salah memahami konsep arah faktor skala negatif, mengira tanda negatif tidak membalik arah letak bangun.</sub>

**Pembahasan:** Evaluasi tiap pernyataan:
1. Titik $R(5, 4)$ didilatasikan oleh $[T(2, 2), -\frac{1}{2}]$:
$x' = -\frac{1}{2}(5 - 2) + 2 = -\frac{1}{2}(3) + 2 = -1,5 + 2 = 0,5$
$y' = -\frac{1}{2}(4 - 2) + 2 = -\frac{1}{2}(2) + 2 = -1 + 2 = 1$
Koordinat $R'$ adalah $(0,5; 1)$. (Pernyataan 1 BENAR)

2. Panjang awal $= 5 - (-1) = 6$, lebar awal $= 4 - 1 = 3$.
Luas awal $= 6 \times 3 = 18\text{ satuan luas}$.
Luas bayangan $= k^2 \times \text{luas awal} = \left(-\frac{1}{2}\right)^2 \times 18 = \frac{1}{4} \times 18 = 4,5\text{ satuan luas}$. (Pernyataan 2 BENAR)

3. Keliling awal $= 2(6 + 3) = 18\text{ satuan}$.
Keliling bayangan $= |k| \times \text{keliling awal} = \left|-\frac{1}{2}\right| \times 18 = 9\text{ satuan}$. (Pernyataan 3 BENAR)

4. Karena faktor skala $k = -\frac{1}{2} < 0$, letak bangun bayangan berlawanan arah dengan letak bangun awal terhadap titik pusat $T$. (Pernyataan 4 SALAH)

Jadi, pernyataan yang benar adalah (1), (2), dan (3).
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas9-b03-e-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: rekonstruksi titik asal dilatasi*

Titik $A(1, 2)$ dan $B(4, 5)$ didilatasikan terhadap titik pusat yang sama $P(a, b)$ dengan faktor skala $k$ berturut-turut menghasilkan bayangan $A'(-7, -10)$ dan $B'(2, -1)$. Jika titik $C$ didilatasikan terhadap pusat $P$ dan faktor skala $k$ yang sama menghasilkan bayangan $C'(-1, -4)$, koordinat titik $C$ adalah ....

- A. $(4, 3)$  
  <sub>Salah: Siswa tertukar posisi absis dan ordinat ketika menentukan koordinat titik $C$.</sub>
- B. $(-2, -4)$  
  <sub>Salah: Siswa keliru menggunakan rumus tanpa mengurangkan pusat terlebih dahulu, menganggap $C' = kC + P$ sehingga $3x + 5 = -1$ dan $3y + 8 = -4$.</sub>
- C. $(-7, -12)$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada pemindahan ruas aljabar terakhir, yaitu $x = -2 - 5 = -7$ dan $y = -4 - 8 = -12$.</sub>
- **D. $(3, 4)$** ✅  
  <sub>Benar: Menentukan faktor skala $k = \frac{x_{B'} - x_{A'}}{x_B - x_A} = \frac{2 - (-7)}{4 - 1} = 3$. Menentukan titik pusat $P(a, b)$ melalui rumus bayangan: $-7 = 3(1 - a) + a \Rightarrow -7 = 3 - 2a \Rightarrow a = 5$, serta $-10 = 3(2 - b) + b \Rightarrow -10 = 6 - 2b \Rightarrow b = 8$, sehingga $P(5, 8)$. Mencari koordinat titik awal $C(x, y)$: $-1 = 3(x - 5) + 5 \Rightarrow -6 = 3(x - 5) \Rightarrow x - 5 = -2 \Rightarrow x = 3$, dan $-4 = 3(y - 8) + 8 \Rightarrow -12 = 3(y - 8) \Rightarrow y - 8 = -4 \Rightarrow y = 4$. Jadi, $C(3, 4)$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai faktor skala $k$.
Selisih koordinat absis bayangan sebanding dengan selisih koordinat awal dikalikan faktor skala:
$$x_{B'} - x_{A'} = k(x_B - x_A)$$
$$2 - (-7) = k(4 - 1)$$
$$9 = 3k \implies k = 3$$

Langkah 2: Menentukan koordinat pusat dilatasi $P(a, b)$.
Berdasarkan rumus dilatasi titik terhadap pusat $P(a, b)$:
$$x' = k(x - a) + a$$
$$-7 = 3(1 - a) + a$$
$$-7 = 3 - 2a \implies 2a = 10 \implies a = 5$$

$$y' = k(y - b) + b$$
$$-10 = 3(2 - b) + b$$
$$-10 = 6 - 2b \implies 2b = 16 \implies b = 8$$
Pusat dilatasi adalah $P(5, 8)$.

Langkah 3: Menentukan titik awal $C(x, y)$ dari bayangan $C'(-1, -4)$.
$$-1 = 3(x - 5) + 5$$
$$-6 = 3(x - 5)$$
$$x - 5 = -2 \implies x = 3$$

$$-4 = 3(y - 8) + 8$$
$$-12 = 3(y - 8)$$
$$y - 8 = -4 \implies y = 4$$

Dengan demikian, koordinat titik $C$ adalah $(3, 4)$.
**Acuan:** siswa — siswa hal.219

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
