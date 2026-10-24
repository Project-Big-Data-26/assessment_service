# Lembar koreksi — kelas11_tl SMA11L-B6 subbab B: Fungsi Aljabar

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b06-b-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: daerah asal fungsi rasional*

Daerah asal dari fungsi rasional $f(x) = \frac{x + 9}{x - 6}$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x > 6, x \in \mathbb{R}\}$  
  <sub>Salah: Mengira penyebut harus bernilai positif seperti pada fungsi akar berakar genap.</sub>
- B. $\{x \mid x \neq -9, x \in \mathbb{R}\}$  
  <sub>Salah: Tertukar mencari pembuat nol pembilang $x + 9 = 0$ alih-alih penyebut.</sub>
- **C. $\{x \mid x \neq 6, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Penyebut tidak boleh sama dengan nol, sehingga $x - 6 \neq 0 \iff x \neq 6$.</sub>
- D. $\{x \mid x \neq -6, x \in \mathbb{R}\}$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan pembuat nol penyebut $x - 6 = 0$.</sub>

**Pembahasan:** Fungsi rasional $f(x) = \frac{x + 9}{x - 6}$ terdefinisi untuk semua bilangan real kecuali pembuat nol penyebut.
$$x - 6 = 0 \iff x = 6$$
Dengan demikian, daerah asal fungsi $f$ adalah $D_f = \{x \mid x \neq 6, x \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b06-b-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: daerah asal akar ganjil*

Daerah asal dari fungsi akar $g(x) = \sqrt[5]{x + 8}$ pada himpunan bilangan real adalah ....

- A. $\{x \mid x \ge -8, x \in \mathbb{R}\}$  
  <sub>Salah: Menerapkan syarat akar berindeks genap $x + 8 \ge 0$ pada akar berindeks ganjil.</sub>
- B. $\{x \mid x \ge 8, x \in \mathbb{R}\}$  
  <sub>Salah: Menerapkan syarat tak negatif sekaligus keliru tanda saat memindahkan konstanta.</sub>
- C. $\{x \mid x \neq -8, x \in \mathbb{R}\}$  
  <sub>Salah: Mengira fungsi akar memiliki pantangan pembuat nol seperti fungsi rasional.</sub>
- **D. $\{x \mid x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Indeks akar bernilai 5 (ganjil), sehingga fungsi terdefinisi untuk seluruh bilangan real.</sub>

**Pembahasan:** Pada fungsi akar $f(x) = \sqrt[n]{g(x)}$, jika $n$ bilangan ganjil ($n = 3, 5, \dots$), maka daerah asalnya mencakup semua bilangan real pada daerah asal $g(x)$. Karena $g(x) = x + 8$ terdefinisi untuk setiap bilangan real, daerah asal fungsi $g$ adalah seluruh himpunan bilangan real, yaitu $\{x \mid x \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b06-b-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: pemodelan fungsi aljabar*

Sebuah usaha katering memiliki biaya tetap bulanan sebesar Rp5.000.000,00 dan biaya produksi sebesar Rp25.000,00 per kotak makanan. Jika fungsi biaya total dirumuskan dengan $B(x) = \text{biaya tetap} + cx$, dengan $c$ menyatakan biaya produksi per kotak dan $x$ menyatakan banyaknya kotak makanan yang diproduksi, model matematika untuk fungsi biaya total $B(x)$ adalah ....

- A. $B(x) = 25.000 + 5.000.000x$  
  <sub>Salah: Tertukar menempatkan biaya tetap sebagai koefisien variabel dan biaya per kotak sebagai konstanta.</sub>
- B. $B(x) = 5.000.000 - 25.000x$  
  <sub>Salah: Salah menggunakan operasi pengurangan yang seharusnya penjumlahan biaya total.</sub>
- **C. $B(x) = 5.000.000 + 25.000x$** ✅  
  <sub>Benar: Substitusi biaya tetap = 5.000.000 dan $c = 25.000$ menghasilkan $B(x) = 5.000.000 + 25.000x$.</sub>
- D. $B(x) = \frac{5.000.000 + 25.000x}{x}$  
  <sub>Salah: Menuliskan fungsi biaya rata-rata alih-alih fungsi biaya total.</sub>

**Pembahasan:** Diketahui:
- Biaya tetap = Rp5.000.000,00
- Biaya per kotak ($c$) = Rp25.000,00

Maka model fungsi biaya total $B(x)$ untuk $x$ kotak adalah:
$$B(x) = 5.000.000 + 25.000x$$
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-7a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b06-b-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: asimtot fungsi rasional*

Persamaan asimtot vertikal dari grafik fungsi rasional $f(x) = \frac{5}{x - 4}$ adalah garis ....

- A. $x = -4$  
  <sub>Salah: Kesalahan tanda saat mencari pembuat nol penyebut $x - 4 = 0$.</sub>
- B. $y = 4$  
  <sub>Salah: Tertukar antara variabel garis vertikal ($x$) dengan garis horizontal ($y$).</sub>
- C. $y = 0$  
  <sub>Salah: Menyebutkan asimtot horizontal alih-alih asimtot vertikal.</sub>
- **D. $x = 4$** ✅  
  <sub>Benar: Penyebut $x - 4 = 0$ menghasilkan pembuat nol $x = 4$, yang merupakan asimtot vertikal grafik fungsi.</sub>

**Pembahasan:** Asimtot vertikal fungsi rasional bersesuaian dengan pembuat nol penyebut yang tidak membuat pembilang bernilai nol.
$$x - 4 = 0 \iff x = 4$$
Jadi, persamaan asimtot vertikal fungsi tersebut adalah $x = 4$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b06-b-easy-bt01-005
*orisinal | C2 | 1 langkah | jenis: daerah asal akar genap*  **[warning validator]**

Daerah asal dari fungsi akar $f(x) = \sqrt{x - 7}$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x \le 7, x \in \mathbb{R}\}$  
  <sub>Salah: Terbalik dalam menentukan arah tanda pertidaksamaan.</sub>
- **B. $\{x \mid x \ge 7, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat fungsi akar kuadrat terdefinisi pada bilangan real adalah bentuk di dalam akar tidak negatif: $x - 7 \ge 0 \iff x \ge 7$.</sub>
- C. $\{x \mid x \ge -7, x \in \mathbb{R}\}$  
  <sub>Salah: Keliru tanda saat memindahkan $-7$ ke ruas kanan pertidaksamaan.</sub>
- D. $\{x \mid x > 7, x \in \mathbb{R}\}$  
  <sub>Salah: Menggunakan pertidaksamaan tegas ($>$) sehingga melupakan bahwa nilai nol diperbolehkan dalam akar.</sub>

**Pembahasan:** Fungsi akar berindeks genap $f(x) = \sqrt{x - 7}$ terdefinisi pada bilangan real jika ekspresi di bawah tanda akar bernilai lebih dari atau sama dengan nol:
$$x - 7 \ge 0 \iff x \ge 7$$
Jadi, daerah asal fungsi $f$ adalah $D_f = \{x \mid x \ge 7, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283
**Warning:** kelas11_tl-b06-b-easy-bt01-005 sangat mirip dengan kelas11_tl-b06-b-easy-bt01-011 (0.88) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b06-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: daerah hasil fungsi rasional*

Daerah hasil dari fungsi rasional $f(x) = \frac{3x - 5}{x + 4}$ untuk domain alaminya pada himpunan bilangan real adalah ....

- A. $\{y \mid y \neq -3, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah tanda saat membagi rasio koefisien $x$ pada pembilang dan penyebut.</sub>
- B. $\{y \mid y \neq \frac{5}{3}, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mencari pembuat nol pembilang ($3x - 5 = 0$) dan menganggapnya sebagai batas daerah hasil.</sub>
- **C. $\{y \mid y \neq 3, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Menyatakan $y = \frac{3x - 5}{x + 4} \iff y(x + 4) = 3x - 5 \iff x(y - 3) = -4y - 5 \iff x = \frac{-4y - 5}{y - 3}$. Nilai $x$ terdefinisi di bilangan real jika $y - 3 \neq 0$, sehingga daerah hasil adalah $\{y \mid y \neq 3, y \in \mathbb{R}\}$.</sub>
- D. $\{y \mid y \neq -4, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa keliru menyebutkan batas daerah asal (pembuat nol penyebut) sebagai batas daerah hasil.</sub>

**Pembahasan:** Misalkan $y = f(x)$:
$$
y = \frac{3x - 5}{x + 4}
$$
$$y(x + 4) = 3x - 5$$
$$yx + 4y = 3x - 5$$
$$yx - 3x = -4y - 5$$
$$x(y - 3) = -(4y + 5)$$
$$x = \frac{-(4y + 5)}{y - 3}$$

Agar $x$ terdefinisi pada bilangan real, penyebut tidak boleh sama dengan nol:
$$y - 3 \neq 0 \iff y \neq 3$$

Jadi, daerah hasil fungsi $f$ adalah $\{y \mid y \neq 3, y \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b06-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: daerah hasil fungsi akar*

Daerah hasil dari fungsi akar $f(x) = \sqrt{x - 5} + 3$ pada daerah asal alaminya adalah ....

- A. $\{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengabaikan konstanta penambah $+3$ dan langsung memakai rentang standar fungsi akar non-negatif.</sub>
- **B. $\{y \mid y \ge 3, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Nilai bentuk akar berindeks genap selalu non-negatif, $\sqrt{x - 5} \ge 0$. Akibatnya, $f(x) = \sqrt{x - 5} + 3 \ge 0 + 3 = 3$.</sub>
- C. $\{y \mid y \ge 5, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa tertukar dengan batas domain/daerah asal yaitu $x \ge 5$.</sub>
- D. $\{y \mid y \ge -3, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah memindahkan tanda konstanta $+3$ menjadi $-3$.</sub>

**Pembahasan:** Daerah asal alami fungsi $f$ mensyaratkan ekspresi di dalam akar tidak negatif:
$$x - 5 \ge 0 \iff x \ge 5$$

Untuk setiap $x \ge 5$, nilai bentuk akar memenuhi:
$$\sqrt{x - 5} \ge 0$$

Tambahkan kedua ruas dengan 3:
$$\sqrt{x - 5} + 3 \ge 0 + 3$$
$$f(x) \ge 3$$

Jadi, daerah hasil fungsi $f$ adalah $\{y \mid y \ge 3, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283 Contoh 6.12 Menentukan Daerah Asal dan Daerah Hasil Fungsi Akar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b06-b-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: titik potong grafik fungsi*

Titik potong grafik fungsi rasional $f(x) = \frac{3x - 12}{x + 2}$ dengan sumbu-$y$ adalah ....

- **A. $(0, -6)$** ✅  
  <sub>Benar: Grafik memotong sumbu-$y$ saat $x = 0$, yaitu $f(0) = \frac{3(0) - 12}{0 + 2} = \frac{-12}{2} = -6$, sehingga titiknya $(0, -6)$.</sub>
- B. $(0, 6)$  
  <sub>Salah: Siswa mengabaikan tanda negatif pada konstanta $-12$.</sub>
- C. (-2, 0)  
  <sub>Salah: Siswa mengambil nilai pembuat nol penyebut yang merupakan letak asimtot vertikal.</sub>
- D. $(4, 0)$  
  <sub>Salah: Siswa menentukan titik potong dengan sumbu-$x$ ($y = 0$), bukan dengan sumbu-$y$.</sub>

**Pembahasan:** Titik potong grafik dengan sumbu-$y$ diperoleh ketika nilai $x = 0$:
$$f(0) = \frac{3(0) - 12}{0 + 2} = \frac{-12}{2} = -6$$

Jadi, koordinat titik potong grafik dengan sumbu-$y$ adalah $(0, -6)$.
**Acuan:** siswa — siswa hal.280

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b06-b-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: asimtot horizontal*

Persamaan asimtot horizontal dari fungsi rasional $f(x) = \frac{8}{x - 5}$ adalah garis ....

- **A. $y = 0$** ✅  
  <sub>Benar: Derajat pembilang (0) lebih kecil dari derajat penyebut (1), sehingga nilai fungsi mendekati 0 saat $x$ menuju tak hingga.</sub>
- B. $y = 8$  
  <sub>Salah: Siswa menganggap nilai konstanta pada pembilang sebagai letak asimtot horizontal.</sub>
- C. $x = 5$  
  <sub>Salah: Siswa menyebutkan asimtot vertikal fungsi rasional, bukan asimtot horizontal.</sub>
- D. $y = -5$  
  <sub>Salah: Siswa menggunakan konstanta penyebut dengan arah horizontal.</sub>

**Pembahasan:** Asimtot horizontal ditentukan oleh nilai limit fungsi saat $x$ mendekati $\infty$ atau $-\infty$:
$$\lim_{x \to \pm\infty} f(x) = \lim_{x \to \pm\infty} \frac{8}{x - 5} = 0$$

Karena nilai fungsi terus mendekati 0, garis $y = 0$ (sumbu-$x$) merupakan asimtot horizontal dari fungsi tersebut.

Jadi, persamaan asimtot horizontalnya adalah garis $y = 0$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b06-b-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: pemodelan biaya fungsi aljabar*

Sebuah percetakan sablon kaos mengeluarkan biaya sewa tempat sebesar Rp8.500.000,00 per bulan dan biaya bahan sablon sebesar Rp18.000,00 per potong kaos. Jika rumus fungsi biaya total adalah $B(x) = \text{biaya tetap} + cx$, dengan $c$ menyatakan biaya bahan per potong dan $x$ menyatakan banyak kaos yang disablon, model matematika dari fungsi biaya tersebut adalah ....

- **A. $B(x) = 8.500.000 + 18.000x$** ✅  
  <sub>Benar: Substitusi biaya tetap = 8.500.000 dan c = 18.000 menghasilkan B(x) = 8.500.000 + 18.000x.</sub>
- B. $B(x) = 18.000 + 8.500.000x$  
  <sub>Salah: Tertukar antara biaya tetap dan biaya per unit variabel.</sub>
- C. $B(x) = \frac{8.500.000 + 18.000x}{x}$  
  <sub>Salah: Menghitung fungsi biaya rata-rata, bukan fungsi biaya total.</sub>
- D. $B(x) = 8.500.000 - 18.000x$  
  <sub>Salah: Menggunakan operasi pengurangan alih-alih penjumlahan biaya.</sub>

**Pembahasan:** Berdasarkan rumus biaya total $B(x) = \text{biaya tetap} + cx$, diketahui biaya tetap = Rp8.500.000,00 dan $c = 18.000$. Maka diperoleh fungsi biaya total $B(x) = 8.500.000 + 18.000x$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-7a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b06-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: daerah asal akar linier*  **[warning validator]**

Daerah asal dari fungsi akar $f(x) = \sqrt{2x - 8}$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x \ge 8, x \in \mathbb{R}\}$  
  <sub>Salah: Lupa membagi dengan koefisien 2.</sub>
- **B. $\{x \mid x \ge 4, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat fungsi akar kuadrat terdefinisi pada bilangan real adalah 2x - 8 >= 0, sehingga 2x >= 8 atau x >= 4.</sub>
- C. $\{x \mid x \le 4, x \in \mathbb{R}\}$  
  <sub>Salah: Arah pertidaksamaan terbalik.</sub>
- D. $\{x \mid x > 4, x \in \mathbb{R}\}$  
  <sub>Salah: Menggunakan tanda pertidaksamaan tegas tanpa menyertakan tanda sama dengan nol.</sub>

**Pembahasan:** Agar $f(x) = \sqrt{2x - 8}$ bernilai real, nilai di dalam akar harus tidak negatif:
$$2x - 8 \ge 0$$
$$2x \ge 8$$
$$x \ge 4$$
Jadi, daerah asalnya adalah $\{x \mid x \ge 4, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283 Contoh 6.12 Menentukan Daerah Asal dan Daerah Hasil Fungsi Akar
**Warning:** kelas11_tl-b06-b-easy-bt01-005 sangat mirip dengan kelas11_tl-b06-b-easy-bt01-011 (0.88) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b06-b-easy-bt01-012
*variasi (angka) | C1 | 1 langkah | jenis: daerah hasil akar ganjil*

Daerah hasil dari fungsi $g(x) = \sqrt[3]{x - 8}$ untuk seluruh domain alaminya pada himpunan bilangan real adalah ....

- A. $\{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Menyamakan sifat akar berpangkat ganjil dengan akar berpangkat genap.</sub>
- B. $\{y \mid y \neq 0, y \in \mathbb{R}\}$  
  <sub>Salah: Menganggap nilai fungsi tidak boleh bernilai nol layaknya penyebut pecahan.</sub>
- C. $\{y \mid y \ge 8, y \in \mathbb{R}\}$  
  <sub>Salah: Mengira nilai hasil selalu lebih besar atau sama dengan konstanta di dalam akar.</sub>
- **D. $\{y \mid y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Akar pangkat tiga menghasilkan nilai bilangan real positif, nol, maupun negatif untuk setiap nilai masukan bilangan real.</sub>

**Pembahasan:** Fungsi $g(x) = \sqrt[3]{x - 8}$ memiliki pangkat akar 3 (ganjil). Akar pangkat ganjil terdefinisi untuk seluruh bilangan real dan dapat menghasilkan nilai negatif, nol, serta positif tanpa batasan. Oleh karena itu, daerah hasilnya adalah seluruh himpunan bilangan real, yaitu $\{y \mid y \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b06-b-easy-bt01-013
*orisinal | C2 | 1 langkah | jenis: nilai tak terdefinisi fungsi rasional*

Nilai $x$ yang menyebabkan fungsi rasional $f(x) = \frac{2x + 5}{3x - 12}$ tidak terdefinisi pada himpunan bilangan real adalah ....

- A. $x = -4$  
  <sub>Salah: Salah dalam memindahkan tanda konstanta saat menyelesaikan 3x = 12.</sub>
- **B. $x = 4$** ✅  
  <sub>Benar: Fungsi rasional tidak terdefinisi saat penyebut bernilai nol, yaitu 3x - 12 = 0 sehingga x = 4.</sub>
- C. $x = -\frac{5}{2}$  
  <sub>Salah: Menghitung pembuat nol dari pembilang, bukan penyebut.</sub>
- D. $x = 12$  
  <sub>Salah: Mengabaikan koefisien 3 dari variabel x pada penyebut.</sub>

**Pembahasan:** Fungsi pecahan tidak terdefinisi jika penyebutnya sama dengan nol:
$$3x - 12 = 0$$
$$3x = 12$$
$$x = 4$$
Jadi, fungsi $f(x)$ tidak terdefinisi ketika $x = 4$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b06-b-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: titik potong sumbu-x*

Titik potong grafik fungsi rasional $f(x) = \frac{2x - 10}{x + 3}$ dengan sumbu-$x$ adalah ....

- A. $(-5, 0)$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan 2x - 10 = 0.</sub>
- **B. $(5, 0)$** ✅  
  <sub>Benar: Titik potong dengan sumbu-x terjadi saat y = 0, yaitu 2x - 10 = 0 menghasilkan x = 5.</sub>
- C. $\left(0, -\frac{10}{3}\right)$  
  <sub>Salah: Menghitung titik potong grafik dengan sumbu-y saat x = 0.</sub>
- D. $(-3, 0)$  
  <sub>Salah: Menggunakan pembuat nol dari penyebut, bukan pembilang.</sub>

**Pembahasan:** Grafik memotong sumbu-$x$ jika $y = f(x) = 0$:
$$\frac{2x - 10}{x + 3} = 0$$
$$2x - 10 = 0$$
$$2x = 10$$
$$x = 5$$
Dengan demikian, koordinat titik potongnya adalah $(5, 0)$.
**Acuan:** siswa — siswa hal.280

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b06-b-easy-bt01-015
*variasi (angka) | C1 | 1 langkah | jenis: daerah hasil fungsi akar nonnegatif*

Daerah hasil dari fungsi akar $f(x) = \sqrt{x - 9}$ untuk daerah asal alaminya pada himpunan bilangan real adalah ....

- **A. $\{y \mid y \ge 0, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Akar kuadrat dari ekspresi real selalu menghasilkan nilai tak negatif, sehingga $f(x) \ge 0$.</sub>
- B. $\{y \mid y > 0, y \in \mathbb{R}\}$  
  <sub>Salah: Keliru menganggap nilai di dalam akar tidak boleh menghasilkan nilai nol.</sub>
- C. $\{y \mid y \ge 9, y \in \mathbb{R}\}$  
  <sub>Salah: Tertukar antara batas nilai variabel domain dengan batas nilai fungsi.</sub>
- D. $\{y \mid y \in \mathbb{R}\}$  
  <sub>Salah: Mengabaikan fakta bahwa akar kuadrat tidak pernah menghasilkan bilangan real negatif.</sub>

**Pembahasan:** Untuk sembarang nilai $x \ge 9$, nilai $x - 9 \ge 0$.
Berdasarkan definisi nilai akar kuadrat utama, $\sqrt{x - 9} \ge 0$.
Jadi, daerah hasil fungsi $f$ adalah $R_f = \{y \mid y \ge 0, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283 Contoh

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b06-b-easy-bt01-016
*variasi (konteks) | C2 | 2 langkah | jenis: titik potong fungsi akar*

Titik potong grafik fungsi akar $f(x) = \sqrt{x - 4}$ dengan sumbu-$x$ adalah ....

- A. $(0, 4)$  
  <sub>Salah: Tertukar antara absis dan ordinat pada titik koordinat kartesius.</sub>
- B. $(0, -2)$  
  <sub>Salah: Salah mensubstitusikan $x = 0$ dan salah menarik akar dari nilai negatif.</sub>
- **C. $(4, 0)$** ✅  
  <sub>Benar: Grafik memotong sumbu-$x$ saat $f(x) = 0$, yang menghasilkan $\sqrt{x - 4} = 0 \iff x = 4$.</sub>
- D. $(-4, 0)$  
  <sub>Salah: Salah tanda aljabar saat memindahkan konstanta ke ruas lain.</sub>

**Pembahasan:** Titik potong dengan sumbu-$x$ terjadi ketika $y = f(x) = 0$:
$\sqrt{x - 4} = 0$
$x - 4 = 0$
$x = 4$
Jadi, koordinat titik potong grafik dengan sumbu-$x$ adalah $(4, 0)$.
**Acuan:** siswa — siswa hal.284 Contoh

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b06-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: domain fungsi rasional linier*

Daerah asal dari fungsi rasional $f(x) = \frac{5x + 1}{2x + 8}$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x \neq -8, x \in \mathbb{R}\}$  
  <sub>Salah: Lupa membagi nilai konstanta dengan koefisien variabel $x$.</sub>
- B. $\{x \mid x \neq 4, x \in \mathbb{R}\}$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan linier pembuat nol penyebut.</sub>
- C. $\{x \mid x \neq -\frac{1}{5}, x \in \mathbb{R}\}$  
  <sub>Salah: Keliru mencari nilai pembuat nol dari bagian pembilang.</sub>
- **D. $\{x \mid x \neq -4, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Fungsi rasional terdefinisi jika penyebut tidak bernilai nol, yaitu $2x + 8 \neq 0 \iff x \neq -4$.</sub>

**Pembahasan:** Fungsi rasional terdefinisi ketika penyebut tidak sama dengan nol:
$2x + 8 \neq 0$
$2x \neq -8$
$x \neq -4$
Jadi, daerah asalnya adalah $\{x \mid x \neq -4, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b06-b-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: asimtot datar fungsi rasional*

Persamaan asimtot horizontal dari grafik fungsi rasional $f(x) = \frac{4x + 7}{2x - 3}$ adalah garis ....

- **A. $y = 2$** ✅  
  <sub>Benar: Karena derajat pembilang sama dengan penyebut, asimtot horizontalnya adalah hasil bagi koefisien derajat tertinggi, yaitu $y = \frac{4}{2} = 2$.</sub>
- B. $x = \frac{3}{2}$  
  <sub>Salah: Tertukar antara asimtot horizontal dengan asimtot vertikal.</sub>
- C. $y = 0$  
  <sub>Salah: Mengira asimtot horizontal fungsi rasional selalu berada di sumbu-x.</sub>
- D. $y = 4$  
  <sub>Salah: Hanya mengambil koefisien $x$ pada pembilang tanpa membaginya dengan koefisien penyebut.</sub>

**Pembahasan:** Untuk $f(x) = \frac{4x + 7}{2x - 3}$, bagi pembilang dan penyebut dengan $x$:
$f(x) = \frac{4 + \frac{7}{x}}{2 - \frac{3}{x}}$
Ketika $x \to \pm\infty$, $\frac{7}{x} \to 0$ dan $\frac{3}{x} \to 0$, sehingga nilai fungsi mendekati $\frac{4}{2} = 2$.
Jadi, persamaan asimtot horizontalnya adalah $y = 2$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b06-b-easy-bt01-019
*variasi (angka) | C2 | 1 langkah | jenis: nilai fungsi akar*

Diketahui fungsi akar $f(x) = \sqrt{x + 7}$. Nilai dari $f(18)$ adalah ....

- A. $\sqrt{11}$  
  <sub>Salah: Siswa keliru mengurangkan bilangan di dalam tanda akar menjadi 18 - 7 = 11.</sub>
- B. $25$  
  <sub>Salah: Siswa menjumlahkan bilangan di dalam akar tetapi lupa menarik nilai akar kuadratnya.</sub>
- **C. $5$** ✅  
  <sub>Benar: Substitusikan $x = 18$ ke dalam fungsi: $f(18) = \sqrt{18 + 7} = \sqrt{25} = 5$.</sub>
- D. $7$  
  <sub>Salah: Siswa salah memperkirakan hasil penarikan akar kuadrat dari 25.</sub>

**Pembahasan:** Substitusikan nilai $x = 18$ ke rumus fungsi:
$$f(18) = \sqrt{18 + 7} = \sqrt{25} = 5$$
Jadi, nilai dari $f(18)$ adalah $5$.
**Acuan:** siswa — siswa hal.284 Contoh

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b06-b-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: pemodelan biaya rata-rata*

Sebuah industri rumahan roti membutuhkan biaya bulanan Rp9.000.000,00 dan biaya produksi Rp12.000,00 per bungkus roti. Misalkan rumus fungsi biaya adalah $B(x) = \text{biaya tetap} + cx$, dengan $c$ adalah biaya produksi setiap roti dan $x$ adalah banyaknya produksi roti (tiap bungkus). Model matematika dari fungsi biaya rata-rata $\bar{B}(x)$ untuk memproduksi $x$ bungkus roti adalah ....

- A. $\bar{B}(x) = 9.000.000 + 12.000x$  
  <sub>Salah: Siswa menuliskan fungsi biaya total, bukan fungsi biaya rata-rata per unit.</sub>
- B. $\bar{B}(x) = \frac{9.000.000 + 12.000x}{12.000}$  
  <sub>Salah: Siswa membagi biaya total dengan nilai biaya per bungkus, bukan dengan jumlah produksi $x$.</sub>
- C. $\bar{B}(x) = \frac{9.000.000x + 12.000}{x}$  
  <sub>Salah: Siswa keliru mengalikan variabel $x$ pada biaya tetap alih-alih pada biaya variabel per unit.</sub>
- **D. $\bar{B}(x) = \frac{9.000.000 + 12.000x}{x}$** ✅  
  <sub>Benar: Biaya total adalah $B(x) = 9.000.000 + 12.000x$. Fungsi biaya rata-rata diperoleh dengan membagi biaya total terhadap banyak roti $x$, yaitu $\bar{B}(x) = \frac{B(x)}{x} = \frac{9.000.000 + 12.000x}{x}$.</sub>

**Pembahasan:** Diketahui:
- Biaya tetap bulanan = $\text{Rp}9.000.000,00$
- Biaya variabel per bungkus ($c$) = $\text{Rp}12.000,00$
- Banyak bungkus roti = $x$

Fungsi biaya total:
$$B(x) = 9.000.000 + 12.000x$$

Biaya rata-rata $\bar{B}(x)$ dihitung dengan membagi biaya total $B(x)$ dengan banyaknya produksi $x$:
$$\bar{B}(x) = \frac{B(x)}{x} = \frac{9.000.000 + 12.000x}{x}$$

Jadi, model fungsi biaya rata-ratanya adalah $\bar{B}(x) = \frac{9.000.000 + 12.000x}{x}$.
**Acuan:** siswa — siswa hal.287 Latihan B Fungsi Aljabar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b06-b-medium-bt01-001
*orisinal | C3 | 2 langkah | jenis: daerah asal fungsi akar kuadrat*

Daerah asal dari fungsi akar $f(x) = \sqrt{25 - x^2}$ pada himpunan bilangan real adalah ....

- A. $\{x \mid 0 \le x \le 5, x \in \mathbb{R}\}$  
  <sub>Salah: Mengira nilai $x$ harus bernilai nonnegatif saja.</sub>
- B. $\{x \mid x \le -5 \text{ atau } x \ge 5, x \in \mathbb{R}\}$  
  <sub>Salah: Terbalik dalam menentukan arah pertidaksamaan kuadrat.</sub>
- **C. $\{x \mid -5 \le x \le 5, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Fungsi akar berindeks genap terdefinisi pada himpunan bilangan real jika nilai di dalam tanda akar tidak negatif, yaitu $25 - x^2 \ge 0 \iff x^2 \le 25 \iff -5 \le x \le 5$.</sub>
- D. $\{x \mid x \ge 5, x \in \mathbb{R}\}$  
  <sub>Salah: Hanya meninjau batas atas dan mengabaikan batas bawah interval.</sub>

**Pembahasan:** Agar fungsi akar $f(x) = \sqrt{25 - x^2}$ terdefinisi pada bilangan real, nilai di bawah tanda akar harus tak-negatif:
$$25 - x^2 \ge 0$$
$$x^2 - 25 \le 0$$
$$(x - 5)(x + 5) \le 0$$
Pembuat nol adalah $x = -5$ dan $x = 5$. Melalui uji tanda pada garis bilangan, interval yang memenuhi adalah $-5 \le x \le 5$.
Jadi, daerah asalnya adalah $D_f = \{x \mid -5 \le x \le 5, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.282

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b06-b-medium-bt01-002
*orisinal | C4 | 3 langkah | jenis: pemodelan fungsi rasional*

Sebidang kebun sayur berbentuk persegi panjang memiliki luas $360\text{ m}^2$. Kebun tersebut akan dipagari kawat di sekelilingnya, kecuali satu bagian selebar $3\text{ m}$ disisakan untuk pintu masuk yang tidak dipasang kawat. Jika panjang kebun dimisalkan $p$ (dalam meter), model fungsi rasional untuk panjang kawat pagar $K(p)$ adalah ....

- A. $K(p) = 2p + \frac{360}{p} - 3$  
  <sub>Salah: Lupa mengalikan lebar dengan 2 pada rumus keliling persegi panjang.</sub>
- **B. $K(p) = 2p + \frac{720}{p} - 3$** ✅  
  <sub>Benar: Luas $L = p \times l = 360$, sehingga lebar $l = \frac{360}{p}$. Keliling kawat pagar adalah keliling persegi panjang dikurangi lebar pintu: $K(p) = 2p + 2l - 3 = 2p + 2\left(\frac{360}{p}\right) - 3 = 2p + \frac{720}{p} - 3$.</sub>
- C. $K(p) = p + \frac{720}{p} - 3$  
  <sub>Salah: Hanya menghitung satu sisi panjang kebun.</sub>
- D. $K(p) = 2p + \frac{720}{p} + 3$  
  <sub>Salah: Menjumlahkan lebar pintu alih-alih menguranginya dari keliling.</sub>

**Pembahasan:** Diketahui:
- Luas $L = 360\text{ m}^2 \implies p \times l = 360 \implies l = \frac{360}{p}$
- Keliling pagar kawat sama dengan keliling persegi panjang dikurangi lebar pintu gerbang ($3\text{ m}$):
$$K(p) = 2p + 2l - 3$$
Substitusikan nilai $l = \frac{360}{p}$:
$$K(p) = 2p + 2\left(\frac{360}{p}\right) - 3 = 2p + \frac{720}{p} - 3$$
**Acuan:** siswa — siswa hal.274

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b06-b-medium-bt01-003
*orisinal | C4 | 3 langkah | jenis: titik potong asimtot fungsi rasional*

Titik potong antara garis asimtot vertikal dan garis asimtot horizontal dari grafik fungsi rasional $f(x) = \frac{6x + 5}{2x - 8}$ adalah ....

- A. $(4, 6)$  
  <sub>Salah: Mengambil koefisien pembilang secara langsung tanpa membaginya dengan koefisien penyebut.</sub>
- B. (-4, 3)  
  <sub>Salah: Kesalahan tanda saat menyelesaikan $2x - 8 = 0$.</sub>
- C. $\left(-\frac{5}{6}, 3\right)$  
  <sub>Salah: Menggunakan pembuat nol pembilang sebagai absis asimtot vertikal.</sub>
- **D. $(4, 3)$** ✅  
  <sub>Benar: Asimtot vertikal didapat dari pembuat nol penyebut: $2x - 8 = 0 \iff x = 4$. Asimtot horizontal didapat dari rasio koefisien derajat tertinggi: $y = \frac{6}{2} = 3$. Titik potong kedua garis $x = 4$ dan $y = 3$ adalah $(4, 3)$.</sub>

**Pembahasan:** Langkah 1: Tentukan asimtot vertikal.
Penyebut bernilai nol jika $2x - 8 = 0 \iff 2x = 8 \iff x = 4$.
Karena pembilang $6(4) + 5 = 29 \neq 0$, maka asimtot vertikalnya adalah garis $x = 4$.

Langkah 2: Tentukan asimtot horizontal.
Karena derajat pembilang sama dengan derajat penyebut (sama-sama berderajat 1), asimtot horizontalnya adalah:
$$y = \lim_{x \to \pm\infty} \frac{6x + 5}{2x - 8} = \frac{6}{2} = 3$$

Langkah 3: Tentukan titik potong kedua asimtot.
Kedua garis asimtot adalah $x = 4$ dan $y = 3$, sehingga titik potongnya adalah $(4, 3)$.
**Acuan:** siswa — siswa hal.277

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b06-b-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: daerah asal dan hasil fungsi rasional*

Daerah asal dan daerah hasil dari fungsi rasional $f(x) = \frac{5x + 6}{x - 8}$ pada himpunan bilangan real berturut-turut adalah ....

- **A. $\{x \mid x \neq 8, x \in \mathbb{R}\}$ dan $\{y \mid y \neq 5, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Penyebut $x - 8 = 0 \implies x = 8$, sehingga $D_f = \{x \mid x \neq 8, x \in \mathbb{R}\}$. Menyatakan $x$ dalam $y$: $y(x - 8) = 5x + 6 \implies x(y - 5) = 8y + 6 \implies x = \frac{8y + 6}{y - 5}$, terdefinisi saat $y \neq 5$, sehingga $R_f = \{y \mid y \neq 5, y \in \mathbb{R}\}$.</sub>
- B. $\{x \mid x \neq -8, x \in \mathbb{R}\}$ dan $\{y \mid y \neq 5, y \in \mathbb{R}\}$  
  <sub>Salah: Salah tanda pada nilai pembuat nol penyebut.</sub>
- C. $\{x \mid x \neq 8, x \in \mathbb{R}\}$ dan $\{y \mid y \neq 0, y \in \mathbb{R}\}$  
  <sub>Salah: Mengira asimtot horizontal selalu berada pada sumbu-$x$ ($y=0$).</sub>
- D. $\{x \mid x \neq 8, x \in \mathbb{R}\}$ dan $\{y \mid y \neq -5, y \in \mathbb{R}\}$  
  <sub>Salah: Salah memindahkan ruas suku linear saat mencari fungsi invers $x$ terhadap $y$.</sub>

**Pembahasan:** 1. Daerah asal ($D_f$):
Penyebut pecahan tidak boleh nol:
$$x - 8 \neq 0 \implies x \neq 8$$
Jadi, $D_f = \{x \mid x \neq 8, x \in \mathbb{R}\}$.

2. Daerah hasil ($R_f$):
Nyatakan $x$ dalam bentuk variabel $y$:
$$y = \frac{5x + 6}{x - 8}$$
$$y(x - 8) = 5x + 6$$
$$xy - 8y = 5x + 6$$
$$x(y - 5) = 8y + 6$$
$$x = \frac{8y + 6}{y - 5}$$
Nilai $x$ tidak terdefinisi jika penyebut bernilai nol, yaitu $y - 5 = 0 \implies y = 5$.
Jadi, $R_f = \{y \mid y \neq 5, y \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b06-b-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: pemodelan fungsi akar*

Sebuah satelit mengorbit planet yang memiliki jari-jari $3.400\text{ km}$. Jika $h$ menyatakan ketinggian satelit (dalam km) di atas permukaan planet, model matematika fungsi jarak pandang $d$ (dalam km) dari satelit ke horizon planet adalah ....

- A. $d(h) = \sqrt{h^2 - 6.800h}$  
  <sub>Salah: Salah menggunakan tanda pengurangan pada penjabaran sisi miring segitiga siku-siku.</sub>
- B. $d(h) = h + 3.400$  
  <sub>Salah: Menarik akar kuadrat suku per suku secara keliru: $\sqrt{a^2 + b^2} = a + b$.</sub>
- C. $d(h) = \sqrt{h^2 + 3.400h}$  
  <sub>Salah: Lupa mengalikan jari-jari dengan 2 saat menjabarkan bentuk kuadrat $(R+h)^2$.</sub>
- **D. $d(h) = \sqrt{h^2 + 6.800h}$** ✅  
  <sub>Benar: Garis singgung pandang ke horizon tegak lurus jari-jari planet: $(R + h)^2 = R^2 + d^2 \implies d^2 = h^2 + 2Rh \implies d(h) = \sqrt{h^2 + 2(3.400)h} = \sqrt{h^2 + 6.800h}$.</sub>

**Pembahasan:** Misalkan titik pusat planet adalah $O$, posisi satelit adalah $S$, dan titik singgung pandang ke horizon adalah $T$.
Segitiga $OTS$ siku-siku di $T$, dengan $OT = R = 3.400\text{ km}$, $OS = R + h = 3.400 + h$, dan panjang jarak ke horizon adalah $ST = d$.
Berdasarkan teorema Pythagoras:
$$OS^2 = OT^2 + ST^2$$
$$(3.400 + h)^2 = 3.400^2 + d^2$$
$$3.400^2 + 2(3.400)h + h^2 = 3.400^2 + d^2$$
$$d^2 = h^2 + 6.800h$$
$$d(h) = \sqrt{h^2 + 6.800h}$$
**Acuan:** siswa — siswa hal.287 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b06-b-medium-bt01-006
*orisinal | C4 | 3 langkah | jenis: daerah asal fungsi akar pecahan*

Daerah asal dari fungsi $f(x) = \sqrt{\frac{x - 3}{x + 5}}$ pada himpunan bilangan real adalah ....

- A. $\{x \mid x \ge 3, x \in \mathbb{R}\}$  
  <sub>Salah: Mengabaikan daerah ketika pembilang dan penyebut sama-sama bernilai negatif.</sub>
- **B. $\{x \mid x < -5 \text{ atau } x \ge 3, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Fungsi akar genap mensyaratkan $\frac{x - 3}{x + 5} \ge 0$ dan penyebut $x + 5 \neq 0$. Melalui uji tanda diperoleh interval $x < -5$ atau $x \ge 3$.</sub>
- C. $\{x \mid x \le -5 \text{ atau } x \ge 3, x \in \mathbb{R}\}$  
  <sub>Salah: Memasukkan nilai pembuat nol penyebut $x = -5$ ke dalam himpunan penyelesaian.</sub>
- D. $\{x \mid -5 < x \le 3, x \in \mathbb{R}\}$  
  <sub>Salah: Mengambil daerah uji bertanda negatif (hasil bagi $< 0$).</sub>

**Pembahasan:** Agar fungsi terdefinisi pada bilangan real, nilai di dalam akar pangkat genap harus tidak negatif dan penyebut tidak boleh nol:
$$\frac{x - 3}{x + 5} \ge 0 \quad \text{dan} \quad x + 5 \neq 0$$
Titik pembuat nol pembilang adalah $x = 3$ (termasuk solusi karena tanda $\ge$).
Titik pembuat nol penyebut adalah $x = -5$ (tidak termasuk solusi karena penyebut tidak boleh nol, $x \neq -5$).

Uji tanda pada ketiga interval:
- Untuk $x < -5$ (misal $x = -6$): $\frac{-9}{-1} > 0$ (positif)
- Untuk $-5 < x < 3$ (misal $x = 0$): $\frac{-3}{5} < 0$ (negatif)
- Untuk $x > 3$ (misal $x = 4$): $\frac{1}{9} > 0$ (positif)

Daerah yang memenuhi adalah $x < -5$ atau $x \ge 3$.
Jadi, daerah asalnya adalah $\{x \mid x < -5 \text{ atau } x \ge 3, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b06-b-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: penerapan fungsi akar*

Kecepatan gelombang tsunami dinyatakan dengan rumus $v = \sqrt{g \cdot d}$, dengan $g$ adalah percepatan gravitasi bumi dan $d$ adalah kedalaman laut. Jika percepatan gravitasi bumi $g = 9{,}8\text{ m/s}^2$ dan kedalaman laut di suatu palung adalah $2.000\text{ meter}$, kecepatan gelombang tsunami yang melintasi palung tersebut adalah ....

- **A. $140\text{ m/s}$** ✅  
  <sub>Benar: Menghitung $v = \sqrt{9{,}8 \times 2.000} = \sqrt{19.600} = 140\text{ m/s}$.</sub>
- B. $196\text{ m/s}$  
  <sub>Salah: Mengabaikan penarikan akar kuadrat dari bilangan ratusan, hanya melihat angka $196$ lalu mengalikan $1$.</sub>
- C. $14\text{ m/s}$  
  <sub>Salah: Kesalahan perhitungan desimal dan penempatan nilai tempat puluhan/ratusan.</sub>
- D. $70\text{ m/s}$  
  <sub>Salah: Membagi hasil akhir dengan 2 karena mengira akar kuadrat sama dengan membagi dua.</sub>

**Pembahasan:** Diketahui:
- Percepatan gravitasi $g = 9{,}8\text{ m/s}^2$
- Kedalaman laut $d = 2.000\text{ m}$

Substitusikan ke dalam fungsi kecepatan:
$$v = \sqrt{g \cdot d} = \sqrt{9{,}8 \times 2.000}$$
$$v = \sqrt{19.600} = 140\text{ m/s}$$

Jadi, kecepatan gelombang tsunami adalah $140\text{ m/s}$.
**Acuan:** siswa — siswa hal.286 Eksplorasi Penerapan Fungsi Akar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b06-b-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: pemodelan gaya fungsi rasional*

Sebuah mobil derek bermassa $800\text{ kg}$ mendorong sebuah beban hingga berpindah sejauh $50\text{ meter}$. Misalkan $t$ menyatakan waktu tempuh dalam detik. Jika percepatan dinyatakan sebagai $a = \frac{v}{t}$ dan kecepatan rata-rata $v = \frac{s}{t}$, model fungsi rasional yang menyatakan besar gaya dorong $F(t)$ (dalam newton) terhadap waktu $t$ adalah ....

- A. $F(t) = \frac{16}{t^2}$  
  <sub>Salah: Membagi massa dengan jarak alih-alih mengalikannya.</sub>
- B. $F(t) = \frac{800}{50t^2}$  
  <sub>Salah: Tertukar posisi pembilang dan penyebut pada perpindahan.</sub>
- C. $F(t) = \frac{40.000}{t}$  
  <sub>Salah: Menggunakan kecepatan rata-rata langsung sebagai percepatan tanpa membaginya kembali dengan waktu $t$.</sub>
- **D. $F(t) = \frac{40.000}{t^2}$** ✅  
  <sub>Benar: Menyusun $v(t) = \frac{50}{t}$, sehingga $a(t) = \frac{50}{t^2}$, lalu $F(t) = m \cdot a = 800 \times \frac{50}{t^2} = \frac{40.000}{t^2}$.</sub>

**Pembahasan:** Langkah 1: Tentukan percepatan sebagai fungsi terhadap $t$.
$$v(t) = \frac{s}{t} = \frac{50}{t}$$
$$a(t) = \frac{v(t)}{t} = \frac{\frac{50}{t}}{t} = \frac{50}{t^2}$$

Langkah 2: Tentukan rumus besar gaya dorong $F(t)$.
$$F(t) = m \cdot a(t) = 800 \cdot \frac{50}{t^2} = \frac{40.000}{t^2}$$

Jadi, fungsi besar gayanya adalah $F(t) = \frac{40.000}{t^2}$.
**Acuan:** siswa — siswa hal.281 Eksplorasi Penerapan Fungsi Rasional

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b06-b-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: titik potong sumbu koordinat fungsi rasional*

Grafik fungsi rasional $f(x) = \frac{x^2 - 4x - 5}{x + 2}$ memotong sumbu-$x$ di titik $(x_1, 0)$ dan $(x_2, 0)$ dengan $x_1 < x_2$. Nilai dari $2x_1 + 3x_2$ adalah ....

- A. $17$  
  <sub>Salah: Menganggap nilai $x_1 = 1$ dan $x_2 = 5$ tanpa tanda negatif pada faktor pertama.</sub>
- B. $7$  
  <sub>Salah: Tertukar nilai $x_1$ dan $x_2$ sehingga menghitung $2(5) + 3(-1) = 7$.</sub>
- **C. $13$** ✅  
  <sub>Benar: Pembuat nol adalah $x = -1$ dan $x = 5$. Dengan $x_1 = -1$ dan $x_2 = 5$, diperoleh $2(-1) + 3(5) = 13$.</sub>
- D. $-13$  
  <sub>Salah: Salah dalam memfaktorkan persamaan kuadrat menjadi $(x + 5)(x - 1) = 0$.</sub>

**Pembahasan:** Titik potong grafik dengan sumbu-$x$ terjadi saat $f(x) = 0$:
$$\frac{x^2 - 4x - 5}{x + 2} = 0$$
Syarat penyebut: $x + 2 \neq 0 \iff x \neq -2$.

Selesaikan pembuat nol pembilang:
$$x^2 - 4x - 5 = 0$$
$$(x - 5)(x + 1) = 0$$
Diperoleh $x = 5$ atau $x = -1$.

Karena disyaratkan $x_1 < x_2$, maka:
$$x_1 = -1 \quad \text{dan} \quad x_2 = 5$$

Hitung nilai dari $2x_1 + 3x_2$:
$$2(-1) + 3(5) = -2 + 15 = 13$$
**Acuan:** siswa — siswa hal.280

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b06-b-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: irisan daerah asal fungsi akar*

Daerah asal dari fungsi $f(x) = \sqrt{2x - 6} + \sqrt{10 - x}$ pada himpunan bilangan real adalah $D_f$. Banyaknya bilangan bulat yang termuat di dalam $D_f$ adalah ....

- A. $7$  
  <sub>Salah: Lupa mengikutsertakan salah satu batas tepi pada pertidaksamaan non-ketat ($10 - 3 = 7$).</sub>
- B. $9$  
  <sub>Salah: Menghitung salah satu batas secara keliru dari nilai $2$.</sub>
- **C. $8$** ✅  
  <sub>Benar: Daerah asal fungsi adalah irisan dari $x \ge 3$ dan $x \le 10$, yaitu $3 \le x \le 10$, yang memuat 8 bilangan bulat.</sub>
- D. $6$  
  <sub>Salah: Menggunakan pertidaksamaan ketat $3 < x < 10$ sehingga hanya menghitung $4, 5, 6, 7, 8, 9$.</sub>

**Pembahasan:** Fungsi $f(x) = \sqrt{2x - 6} + \sqrt{10 - x}$ terdefinisi pada bilangan real jika kedua bentuk di bawah tanda akar bernilai tak negatif:
1. Syarat akar pertama:
   $$2x - 6 \ge 0 \iff 2x \ge 6 \iff x \ge 3$$
2. Syarat akar kedua:
   $$10 - x \ge 0 \iff x \le 10$$

Irisan dari kedua syarat tersebut menghasilkan daerah asal:
$$D_f = \{x \mid 3 \le x \le 10, x \in \mathbb{R}\}$$

Bilangan bulat yang terletak pada interval $[3, 10]$ adalah:
$$3, 4, 5, 6, 7, 8, 9, 10$$

Banyaknya bilangan bulat adalah $10 - 3 + 1 = 8$ buah.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b06-b-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: asimtot miring fungsi rasional*

Persamaan garis asimtot miring dari grafik fungsi rasional $f(x) = \frac{8x^3 - 6x^2 + 9}{x^2 + 7}$ adalah ....

- A. $y = 8x + 6$  
  <sub>Salah: Kesalahan tanda saat melakukan pembagian suku konstan pada pembagian bersusun.</sub>
- **B. $y = 8x - 6$** ✅  
  <sub>Benar: Hasil pembagian bersusun $(8x^3 - 6x^2 + 9) : (x^2 + 7)$ menghasilkan hasil bagi $8x - 6$ dengan sisa $-56x + 51$, sehingga asimtot miringnya adalah $y = 8x - 6$.</sub>
- C. $y = 8x$  
  <sub>Salah: Hanya membagi suku berderajat tertinggi tanpa meneruskan pembagian untuk suku berderajat satu tingkat di bawahnya.</sub>
- D. $y = -6x + 8$  
  <sub>Salah: Tertukar antara koefisien $x$ dan suku konstanta dari hasil bagi.</sub>

**Pembahasan:** Bagi pembilang $8x^3 - 6x^2 + 9$ dengan penyebut $x^2 + 7$:

1. Bagi suku pertama: $\frac{8x^3}{x^2} = 8x$.
   Kalikan: $8x(x^2 + 7) = 8x^3 + 56x$.
   Kurangkan: $(8x^3 - 6x^2 + 9) - (8x^3 + 56x) = -6x^2 - 56x + 9$.
2. Bagi suku berikutnya: $\frac{-6x^2}{x^2} = -6$.
   Kalikan: $-6(x^2 + 7) = -6x^2 - 42$.
   Kurangkan: $(-6x^2 - 56x + 9) - (-6x^2 - 42) = -56x + 51$.
3. Bentuk fungsinya menjadi:
   $$f(x) = 8x - 6 + \frac{-56x + 51}{x^2 + 7}$$
   Ketika $x \to \pm\infty$, nilai $\frac{-56x + 51}{x^2 + 7} \to 0$.

Jadi, persamaan asimtot miringnya adalah garis $y = 8x - 6$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b06-b-medium-bt01-012
*variasi (angka) | C4 | 3 langkah | jenis: nilai parameter daerah asal dan hasil*

Jika daerah asal dari fungsi rasional $f(x) = \frac{2x - 8}{3x + 9}$ adalah $D_f = \{x \mid x \neq a, x \in \mathbb{R}\}$ dan daerah hasilnya adalah $R_f = \{y \mid y \neq b, y \in \mathbb{R}\}$, nilai dari $a + 3b$ adalah ....

- A. $-5$  
  <sub>Salah: Salah tanda pada nilai $b$ menjadi $-\frac{2}{3}$, sehingga $-3 + 3\left(-\frac{2}{3}\right) = -5$.</sub>
- **B. $-1$** ✅  
  <sub>Benar: Pembuat nol penyebut adalah $3x + 9 = 0 \implies a = -3$, dan asimtot horizontal adalah $y = \frac{2}{3} \implies b = \frac{2}{3}$, sehingga $a + 3b = -3 + 3\left(\frac{2}{3}\right) = -1$.</sub>
- C. $1$  
  <sub>Salah: Keliru pada tanda operasi penjumlahan bilangan bulat, menghitung $3 - 2 = 1$.</sub>
- D. $5$  
  <sub>Salah: Salah tanda pada nilai $a$ (mengambil $a = 3$, sehingga $3 + 2 = 5$).</sub>

**Pembahasan:** Langkah 1: Tentukan daerah asal ($D_f$).
Fungsi terdefinisi jika penyebut tidak sama dengan nol:
$$3x + 9 \neq 0 \implies 3x \neq -9 \implies x \neq -3$$
Diperoleh $a = -3$.

Langkah 2: Tentukan daerah hasil ($R_f$).
Nyatakan $x$ dalam $y$:
$$y = \frac{2x - 8}{3x + 9}$$
$$y(3x + 9) = 2x - 8$$
$$3xy + 9y = 2x - 8$$
$$3xy - 2x = -9y - 8$$
$$x(3y - 2) = -9y - 8$$
$$x = \frac{-9y - 8}{3y - 2}$$
Nilai $x$ terdefinisi jika $3y - 2 \neq 0 \implies y \neq \frac{2}{3}$.
Diperoleh $b = \frac{2}{3}$.

Langkah 3: Hitung $a + 3b$.
$$a + 3b = -3 + 3\left(\frac{2}{3}\right) = -3 + 2 = -1$$
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b06-b-medium-bt01-013
*variasi (konteks) | C3 | 3 langkah | jenis: biaya rata-rata fungsi rasional*

Sebuah industri tas ransel memiliki biaya operasional tetap sebesar Rp12.000.000,00 per bulan dan biaya variabel produksi sebesar Rp60.000,00 per unit. Fungsi biaya rata-rata per unit dinyatakan sebagai $\bar{B}(x) = \frac{B(x)}{x}$, dengan $B(x)$ adalah biaya total dan $x$ adalah banyaknya unit tas yang diproduksi. Biaya rata-rata per unit untuk memproduksi 300 unit tas dalam satu bulan adalah ....

- A. Rp40.000,00  
  <sub>Salah: Hanya membagi biaya operasional tetap dengan 300 tanpa menambahkan biaya variabel per unit.</sub>
- B. Rp60.000,00  
  <sub>Salah: Hanya menyebutkan biaya variabel per unit tanpa memperhitungkan pembagian biaya operasional tetap.</sub>
- **C. Rp100.000,00** ✅  
  <sub>Benar: Biaya total untuk 300 unit adalah $12.000.000 + 60.000(300) = 30.000.000$, sehingga biaya rata-rata per unit adalah $\frac{30.000.000}{300} = 100.000$.</sub>
- D. Rp120.000,00  
  <sub>Salah: Salah menghitung total biaya variabel menjadi Rp24.000.000,00 sehingga rata-rata per unit menjadi Rp120.000,00.</sub>

**Pembahasan:** Langkah 1: Tentukan fungsi biaya total $B(x)$.
$$B(x) = 12.000.000 + 60.000x$$

Langkah 2: Tentukan fungsi biaya rata-rata $\bar{B}(x)$.
$$\bar{B}(x) = \frac{B(x)}{x} = \frac{12.000.000 + 60.000x}{x} = \frac{12.000.000}{x} + 60.000$$

Langkah 3: Hitung untuk $x = 300$.
$$\bar{B}(300) = \frac{12.000.000}{300} + 60.000 = 40.000 + 60.000 = 100.000$$

Jadi, biaya rata-rata per unit adalah Rp100.000,00.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-7a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b06-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: daerah asal fungsi akar pertidaksamaan kuadrat*

Daerah asal dari fungsi akar $f(x) = \sqrt{x^2 - 3x - 10}$ pada himpunan bilangan real adalah ....

- **A. $\{x \mid x \le -2 \text{ atau } x \ge 5, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat fungsi akar terdefinisi pada bilangan real adalah $x^2 - 3x - 10 \ge 0 \iff (x - 5)(x + 2) \ge 0$, yang dipenuhi oleh interval $x \le -2$ atau $x \ge 5$.</sub>
- B. $\{x \mid -2 \le x \le 5, x \in \mathbb{R}\}$  
  <sub>Salah: Keliru menganggap daerah penyelesaian pertidaksamaan $\ge 0$ berada di antara kedua pembuat nol.</sub>
- C. $\{x \mid x \le -5 \text{ atau } x \ge 2, x \in \mathbb{R}\}$  
  <sub>Salah: Salah memfaktorkan persamaan kuadrat menjadi $(x + 5)(x - 2)$ sehingga batas nilainya tertukar tanda.</sub>
- D. $\{x \mid -5 \le x \le 2, x \in \mathbb{R}\}$  
  <sub>Salah: Kombinasi kesalahan pemfaktoran tanda akar dan kesalahan memilih interval bagian dalam.</sub>

**Pembahasan:** Langkah 1: Terapkan syarat fungsi akar berpangkat genap.
Fungsi $f(x) = \sqrt{x^2 - 3x - 10}$ terdefinisi pada bilangan real jika radikan tak negatif:
$$x^2 - 3x - 10 \ge 0$$

Langkah 2: Faktorkan bentuk kuadrat untuk menemukan pembuat nol.
$$(x - 5)(x + 2) = 0 \implies x = 5 \text{ atau } x = -2$$

Langkah 3: Uji tanda pada garis bilangan.
- Untuk $x < -2$ (misal $x = -3$): $(-8)(-1) = 8 > 0$ (memenuhi).
- Untuk $-2 < x < 5$ (misal $x = 0$): $(-5)(2) = -10 < 0$ (tidak memenuhi).
- Untuk $x > 5$ (misal $x = 6$): $(1)(8) = 8 > 0$ (memenuhi).

Jadi, daerah asalnya adalah $\{x \mid x \le -2 \text{ atau } x \ge 5, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b06-b-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: banyaknya asimtot vertikal fungsi rasional*

Banyaknya garis asimtot vertikal dari grafik fungsi rasional $f(x) = \frac{x^2 - 16}{x^2 + 2x - 24}$ adalah ....

- A. $2$  
  <sub>Salah: Langsung menganggap kedua pembuat nol penyebut ($x = 4$ dan $x = -6$) sebagai asimtot vertikal tanpa memfaktorkan pembilang.</sub>
- **B. $1$** ✅  
  <sub>Benar: Faktorisasi menghasilkan $\frac{(x - 4)(x + 4)}{(x - 4)(x + 6)}$. Karena faktor $(x - 4)$ saling membagi, garis asimtot vertikal hanya berasal dari faktor penyebut yang tersisa yaitu $x + 6 = 0 \implies x = -6$ (hanya 1 garis).</sub>
- C. $4$  
  <sub>Salah: Menghitung total seluruh pembuat nol pembilang dan penyebut secara bersamaan.</sub>
- D. $0$  
  <sub>Salah: Keliru berasumsi bahwa karena pembilang dan penyebut memiliki faktor sekutu, fungsi tersebut tidak memiliki asimtot sama sekali.</sub>

**Pembahasan:** Langkah 1: Faktorkan pembilang dan penyebut fungsi rasional.
Pembilang: $x^2 - 16 = (x - 4)(x + 4)$
Penyebut: $x^2 + 2x - 24 = (x - 4)(x + 6)$

Langkah 2: Sederhanakan fungsi untuk nilai $x \neq 4$.
$$f(x) = \frac{(x - 4)(x + 4)}{(x - 4)(x + 6)} = \frac{x + 4}{x + 6}, \quad x \neq 4$$

Langkah 3: Identifikasi asimtot vertikal.
- Pada $x = 4$, grafik fungsi memiliki lubang (titik tak terdefinisi yang dapat dihilangkan), bukan asimtot vertikal.
- Pada $x = -6$, penyebut bernilai nol sedangkan pembilang bernilai $-6 + 4 = -2 \neq 0$. Oleh karena itu, $x = -6$ adalah satu-satunya asimtot vertikal.

Jadi, banyaknya garis asimtot vertikal adalah 1.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b06-b-medium-bt01-016
*variasi (angka) | C3 | 2 langkah | jenis: kecepatan gelombang tsunami fungsi akar*

Kecepatan gelombang tsunami di lautan ditentukan oleh fungsi akar $v = \sqrt{g \cdot d}$, dengan $g$ menyatakan percepatan gravitasi bumi dan $d$ menyatakan kedalaman laut. Jika percepatan gravitasi bumi $g = 9{,}8\text{ m/s}^2$, kecepatan gelombang tsunami pada lautan yang memiliki kedalaman $8.000\text{ meter}$ adalah ....

- A. $320\text{ m/s}$  
  <sub>Salah: Siswa salah melakukan penarikan akar kuadrat ($320^2 = 102.400$).</sub>
- B. $240\text{ m/s}$  
  <sub>Salah: Siswa salah memperkirakan nilai akar kuadrat dari $78.400$ menjadi $240$ ($240^2 = 57.600$).</sub>
- C. $140\text{ m/s}$  
  <sub>Salah: Siswa salah membagi dua hasil perkalian di bawah tanda akar sebelum menarik akar kuadrat.</sub>
- **D. $280\text{ m/s}$** ✅  
  <sub>Benar: Substitusi $g = 9{,}8$ dan $d = 8.000$ menghasilkan $v = \sqrt{9{,}8 \times 8.000} = \sqrt{78.400} = 280\text{ m/s}$.</sub>

**Pembahasan:** Diketahui:
- Rumus kecepatan tsunami: $v = \sqrt{g \cdot d}$
- $g = 9{,}8\text{ m/s}^2$
- $d = 8.000\text{ m}$

Substitusikan nilai yang diketahui ke dalam fungsi kecepatan:
$$\begin{aligned} v &= \sqrt{9{,}8 \times 8.000} \\ &= \sqrt{78.400} \\ &= 280\text{ m/s} \end{aligned}$$

Jadi, kecepatan gelombang tsunami tersebut adalah $280\text{ m/s}$.
**Acuan:** siswa — siswa hal.286 Eksplorasi Penerapan Fungsi Akar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b06-b-medium-bt01-017
*variasi (konteks) | C3 | 2 langkah | jenis: fungsi jarak horizon satelit*

Sebuah wahana antariksa mengorbit bulan pada ketinggian $h\text{ km}$ di atas permukaan bulan. Jari-jari bulan diasumsikan $1.738\text{ km}$. Berdasarkan teorema Pythagoras, jarak pandang dari wahana ke horizon bulan dapat dinyatakan dengan fungsi $d(h) = \sqrt{(r + h)^2 - r^2}$, dengan $r$ adalah jari-jari bulan. Bentuk sederhana dari fungsi jarak $d(h)$ tersebut adalah ....

- **A. $d(h) = \sqrt{h^2 + 3.476h}$** ✅  
  <sub>Benar: Menjabarkan $(h + 1.738)^2 - 1.738^2 = h^2 + 2(1.738)h + 1.738^2 - 1.738^2 = h^2 + 3.476h$.</sub>
- B. $d(h) = h + 1.738$  
  <sub>Salah: Siswa keliru menganggap $\sqrt{(r+h)^2 - r^2} = (r+h) - r$ tanpa mengoperasikannya di bawah akar.</sub>
- C. $d(h) = \sqrt{h^2 + 1.738h}$  
  <sub>Salah: Siswa lupa mengalikan dengan $2$ pada suku tengah saat menjabarkan bentuk kuadrat $(h + 1.738)^2$.</sub>
- D. $d(h) = \sqrt{h^2 - 3.476h}$  
  <sub>Salah: Siswa salah tanda operasi pengurangan pada suku tengah hasil penjabaran aljabar.</sub>

**Pembahasan:** Diketahui jari-jari bulan $r = 1.738\text{ km}$.
Substitusikan $r = 1.738$ ke dalam fungsi jarak:
$$\begin{aligned} d(h) &= \sqrt{(1.738 + h)^2 - 1.738^2} \\ &= \sqrt{h^2 + 2(1.738)h + 1.738^2 - 1.738^2} \\ &= \sqrt{h^2 + 3.476h} \end{aligned}$$

Jadi, model fungsi jarak horizon adalah $d(h) = \sqrt{h^2 + 3.476h}$.
**Acuan:** siswa — siswa hal.287 Latihan B Fungsi Aljabar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b06-b-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: asimtot miring pecahan kuadrat linear*

Persamaan garis asimtot miring dari grafik fungsi rasional $f(x) = \frac{3x^2 - 4x + 7}{x - 2}$ adalah ....

- A. $y = 3x - 4$  
  <sub>Salah: Siswa langsung mengambil koefisien suku derajat satu dan konstanta pembilang tanpa membaginya dengan penyebut.</sub>
- B. $y = 3x + 10$  
  <sub>Salah: Siswa keliru menghitung $-4x - (-6x)$ menjadi $-10x$ sehingga konstanta hasil bagi menjadi $+10$.</sub>
- C. $y = 3x - 2$  
  <sub>Salah: Siswa salah menghitung tanda pada suku konstanta saat melakukan proses pembagian bersusun.</sub>
- **D. $y = 3x + 2$** ✅  
  <sub>Benar: Hasil bagi dari $(3x^2 - 4x + 7)$ oleh $(x - 2)$ adalah $3x + 2$ dengan sisa $11$, sehingga asimtot miringnya $y = 3x + 2$.</sub>

**Pembahasan:** Untuk menentukan asimtot miring, lakukan pembagian bersusun antara pembilang dan penyebut:
$$\begin{aligned} \frac{3x^2 - 4x + 7}{x - 2} &= \frac{3x(x - 2) + 2(x - 2) + 11}{x - 2} \\ &= 3x + 2 + \frac{11}{x - 2} \end{aligned}$$

Ketika $x \to \pm\infty$, nilai $\frac{11}{x - 2} \to 0$. Dengan demikian, nilai fungsi $f(x)$ mendekati garis $y = 3x + 2$.

Jadi, persamaan asimtot miring grafik fungsi tersebut adalah $y = 3x + 2$.
**Acuan:** siswa — siswa hal.279

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b06-b-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: jarak antar titik potong sumbu koordinat*

Grafik fungsi rasional $f(x) = \frac{4x - 12}{2x + 6}$ memotong sumbu-$x$ di titik $A$ dan memotong sumbu-$y$ di titik $B$. Jarak antara titik $A$ dan titik $B$ pada bidang koordinat Cartesius adalah ....

- **A. $\sqrt{13}$** ✅  
  <sub>Benar: Titik $A$ adalah $(3, 0)$ dan titik $B$ adalah $(0, -2)$. Jarak $AB = \sqrt{(3 - 0)^2 + (0 - (-2))^2} = \sqrt{9 + 4} = \sqrt{13}$.</sub>
- B. $\sqrt{15}$  
  <sub>Salah: Siswa salah menghitung kuadrat dari $-2$ menjadi $6$ sehingga $9 + 6 = 15$.</sub>
- C. $5$  
  <sub>Salah: Siswa salah menjumlahkan absis dan ordinat tanpa rumus jarak $3 + 2 = 5$ atau mengira tripel Pythagoras $3, 4, 5$.</sub>
- D. $\sqrt{5}$  
  <sub>Salah: Siswa salah menggunakan operasi pengurangan pada rumus jarak $\sqrt{3^2 - 2^2} = \sqrt{5}$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong sumbu-$x$ ($y = 0$)
$$\begin{aligned} \frac{4x - 12}{2x + 6} &= 0 \\ 4x - 12 &= 0 \\ 4x &= 12 \\ x &= 3 \end{aligned}$$
Titik potong sumbu-$x$ adalah $A(3, 0)$.

Langkah 2: Menentukan titik potong sumbu-$y$ ($x = 0$)
$$y = f(0) = \frac{4(0) - 12}{2(0) + 6} = \frac{-12}{6} = -2$$
Titik potong sumbu-$y$ adalah $B(0, -2)$.

Langkah 3: Menghitung jarak antara titik $A(3, 0)$ dan titik $B(0, -2)$
$$\begin{aligned} d(A, B) &= \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \\ &= \sqrt{(0 - 3)^2 + (-2 - 0)^2} \\ &= \sqrt{(-3)^2 + (-2)^2} \\ &= \sqrt{9 + 4} = \sqrt{13} \end{aligned}$$

Jadi, jarak antara titik $A$ dan titik $B$ adalah $\sqrt{13}$.
**Acuan:** siswa — siswa hal.280

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b06-b-medium-bt01-020
*variasi (angka) | C3 | 3 langkah | jenis: asimtot miring fungsi rasional*

Persamaan garis asimtot miring dari fungsi $g(x) = \frac{7x^7 - 9x^6 + 8}{x^6 + 6}$ adalah ....

- A. $y = 7x + 9$  
  <sub>Salah: salah tanda pada konstanta akibat keliru membagi suku $-9x^6$ dengan $x^6$</sub>
- B. $y = 7x - 6$  
  <sub>Salah: menggunakan nilai konstanta penyebut sebagai konstanta persamaan asimtot miring</sub>
- **C. $y = 7x - 9$** ✅  
  <sub>Benar: Hasil bagi pembagian bersusun pembilang oleh penyebut adalah $7x - 9$, sehingga ketika $x \to \pm\infty$, sisa pembagian mendekati nol dan grafik mendekati garis $y = 7x - 9$.</sub>
- D. $y = 7x$  
  <sub>Salah: hanya membagi suku berpangkat tertinggi dan mengabaikan hasil bagi dari suku berderajat berikutnya</sub>

**Pembahasan:** Untuk menentukan asimtot miring dari fungsi rasional $g(x) = \frac{7x^7 - 9x^6 + 8}{x^6 + 6}$, lakukan pembagian bersusun antara pembilang dan penyebut:

1. Bagilah suku berderajat tertinggi pembilang dengan suku berderajat tertinggi penyebut:
$$\frac{7x^7}{x^6} = 7x$$
Kalikan $7x$ dengan penyebut $(x^6 + 6)$:
$$7x(x^6 + 6) = 7x^7 + 42x$$

2. Kurangkan dari pembilang:
$$(7x^7 - 9x^6 + 8) - (7x^7 + 42x) = -9x^6 - 42x + 8$$

3. Bagilah suku berderajat tertinggi sisa dengan penyebut:
$$\frac{-9x^6}{x^6} = -9$$
Kalikan $-9$ dengan penyebut $(x^6 + 6)$:
$$-9(x^6 + 6) = -9x^6 - 54$$

4. Kurangkan kembali:
$$(-9x^6 - 42x + 8) - (-9x^6 - 54) = -42x + 62$$

Dengan demikian, bentuk fungsi dapat ditulis sebagai:
$$g(x) = 7x - 9 + \frac{-42x + 62}{x^6 + 6}$$

Ketika nilai $x$ mendekati positif tak hingga atau negatif tak hingga, nilai $\frac{-42x + 62}{x^6 + 6}$ mendekati nol. Oleh karena itu, grafik fungsi $g(x)$ mendekati garis $y = 7x - 9$.

Jadi, persamaan garis asimtot miringnya adalah $y = 7x - 9$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b06-b-hard-bt01-001
*variasi (konteks) | C5 | 5 langkah | jenis: evaluasi daerah hasil fungsi akar*

Diberikan fungsi akar $f(x) = 8 - \sqrt{25 - x^2}$ pada daerah asal alaminya. Seorang siswa mengklaim bahwa daerah hasil fungsi tersebut adalah $R_f = \{y \mid y \le 8, y \in \mathbb{R}\}$. Evaluasi yang tepat mengenai klaim tersebut adalah ....

- A. Salah, karena daerah asal fungsi adalah himpunan bilangan real sehingga daerah hasilnya adalah $R_f = \{y \mid -5 \le y \le 5, y \in \mathbb{R}\}$.  
  <sub>Salah: Tertukar antara interval nilai $x$ (daerah asal) dengan daerah hasil fungsi $f(x)$.</sub>
- **B. Salah, karena nilai maksimum $\sqrt{25 - x^2}$ adalah $5$ sehingga daerah hasil yang benar adalah $R_f = \{y \mid 3 \le y \le 8, y \in \mathbb{R}\}$.** ✅  
  <sub>Benar: Nilai radikan dibatasi $0 \le 25 - x^2 \le 25$, sehingga $0 \le \sqrt{25 - x^2} \le 5$. Akibatnya, nilai $y = 8 - \sqrt{25 - x^2}$ berada pada interval $[8 - 5, 8 - 0] = [3, 8]$.</sub>
- C. Benar, karena nilai bentuk akar selalu tak negatif sehingga nilai terbesar dari $f(x)$ tercapai saat bentuk akar bernilai nol.  
  <sub>Salah: Mengabaikan batas nilai maksimum bentuk akar $\sqrt{25 - x^2}$ yang ditentukan oleh batas daerah asalnya.</sub>
- D. Salah, karena nilai di dalam akar tidak boleh negatif sehingga daerah hasilnya adalah $R_f = \{y \mid y \ge 8, y \in \mathbb{R}\}$.  
  <sub>Salah: Salah mengalikan tanda negatif pada bentuk akar sehingga mengira fungsi selalu bernilai $\ge 8$.</sub>

**Pembahasan:** Langkah 1: Tentukan syarat terdefinisi bentuk akar: $25 - x^2 \ge 0 \iff -5 \le x \le 5$.
Langkah 2: Tentukan rentang nilai dari $u = 25 - x^2$. Karena $x^2 \ge 0$, nilai minimum $x^2$ adalah $0$ (saat $x = 0$) dan nilai maksimumnya adalah $25$ (saat $x = \pm 5$). Maka $0 \le 25 - x^2 \le 25$.
Langkah 3: Ambil nilai akar kuadrat: $0 \le \sqrt{25 - x^2} \le 5$.
Langkah 4: Kalikan dengan $-1$ dan jumlahkan dengan 8:
$$-5 \le -\sqrt{25 - x^2} \le 0$$
$$8 - 5 \le 8 - \sqrt{25 - x^2} \le 8 - 0 \iff 3 \le f(x) \le 8$$
Langkah 5: Simpulkan bahwa klaim siswa salah karena daerah hasil yang benar adalah terikat dalam rentang $3 \le y \le 8$.
**Acuan:** siswa — siswa hal.287 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b06-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: parameter asimtot miring*

Diketahui fungsi rasional $f(x) = \frac{2x^2 + kx - 5}{x + 1}$ dengan $k$ adalah konstanta real. Jika garis asimtot miring dari grafik fungsi $f$ melalui titik $(3, 8)$, maka nilai $k$ adalah ....

- A. 8  
  <sub>Salah: Salah tanda saat membagi dengan $(x + 1)$, menganggap hasil bagi adalah $2x + (k + 2)$ lalu salah operasi hitung.</sub>
- B. -4  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan ruas konstanta ke sisi lain persamaan.</sub>
- **C. 4** ✅  
  <sub>Benar: Hasil bagi pembagian bersusun adalah $y = 2x + (k - 2)$. Substitusi titik $(3, 8)$ menghasilkan $8 = 2(3) + k - 2 \implies k = 4$.</sub>
- D. 0  
  <sub>Salah: Lupa mengurangkan konstanta 2 pada hasil bagi pembagian bersusun sehingga menghitung $8 = 2(3) + k$.</sub>

**Pembahasan:** Langkah 1: Lakukan pembagian bersusun pembilang $(2x^2 + kx - 5)$ oleh penyebut $(x + 1)$:
$$2x^2 + kx - 5 = (x + 1)(2x + k - 2) + (-5 - (k - 2))$$
Langkah 2: Ambil komponen hasil bagi linear untuk menentukan persamaan asimtot miring:
$$y = 2x + k - 2$$
Langkah 3: Substitusikan koordinat titik $(3, 8)$ ke dalam persamaan asimtot miring:
$$8 = 2(3) + k - 2$$
$$8 = 6 + k - 2$$
$$8 = k + 4$$
Langkah 4: Selesaikan persamaan untuk memperoleh nilai $k$:
$$k = 8 - 4 = 4$$
**Acuan:** siswa — siswa hal.279

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b06-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: analisis biaya rata-rata*

Sebuah produsen makanan ringan memodelkan fungsi biaya rata-rata produksi $x$ kotak keripik (dalam rupiah per kotak) dengan fungsi rasional $\bar{B}(x) = \frac{18.000.000 + 45.000x}{x}$. Agar biaya rata-rata per kotak tidak melebihi Rp60.000,00, jumlah minimum kotak keripik yang harus diproduksi adalah ....

- A. 300 kotak  
  <sub>Salah: Membagi biaya tetap $18.000.000$ langsung dengan target biaya rata-rata $60.000$ tanpa memperhitungkan biaya variabel $45.000x$.</sub>
- **B. 1.200 kotak** ✅  
  <sub>Benar: Pertidaksamaan $\frac{18.000.000 + 45.000x}{x} \le 60.000$ dengan $x > 0$ menghasilkan $x \ge 1.200$.</sub>
- C. 1.500 kotak  
  <sub>Salah: Kesalahan aritmetika saat membagi $18.000.000$ dengan $12.000$ bukan $15.000$.</sub>
- D. 800 kotak  
  <sub>Salah: Salah menjumlahkan biaya variabel dengan target biaya rata-rata alih-alih mengurangkannya ($18.000.000 / (60.000 - 45.000)$ salah dihitung menjadi $18.000.000 / 22.500$).</sub>

**Pembahasan:** Langkah 1: Susun pertidaksamaan berdasarkan syarat biaya rata-rata:
$$\bar{B}(x) \le 60.000 \iff \frac{18.000.000 + 45.000x}{x} \le 60.000$$
Langkah 2: Karena $x$ menyatakan banyaknya produksi barang, maka $x > 0$. Kalikan kedua ruas dengan $x$ tanpa mengubah tanda pertidaksamaan:
$$18.000.000 + 45.000x \le 60.000x$$
Langkah 3: Kurangkan kedua ruas dengan $45.000x$:
$$18.000.000 \le 60.000x - 45.000x$$
$$18.000.000 \le 15.000x$$
Langkah 4: Bagi kedua ruas dengan $15.000$:
$$x \ge \frac{18.000.000}{15.000} \iff x \ge 1.200$$
Jadi, jumlah produksi minimum adalah 1.200 kotak.
**Acuan:** siswa — siswa hal.287

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b06-b-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: daerah hasil fungsi rasional*

Daerah hasil dari fungsi rasional $f(x) = \frac{4x - 12}{x^2 - 5x + 6}$ untuk daerah asal alaminya pada himpunan bilangan real adalah ....

- A. $\{y \mid y \neq 0, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengidentifikasi asimtot horizontal $y = 0$, tetapi mengabaikan titik lubang pada kurva saat $x = 3$ sehingga nilai $y = 4$ tidak dikeluarkan dari daerah hasil.</sub>
- B. $\{y \mid y \neq 4, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa menemukan nilai lubang di $y = 4$, tetapi lupa bahwa fungsi rasional tersebut juga memiliki asimtot horizontal di $y = 0$ sehingga $0$ tidak termasuk daerah hasil.</sub>
- C. $\{y \mid y \neq 2 \text{ dan } y \neq 3, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa tertukar antara nilai terlarang pada daerah asal ($x \neq 2, x \neq 3$) dengan nilai terlarang pada daerah hasil.</sub>
- **D. $\{y \mid y \neq 0 \text{ dan } y \neq 4, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Fungsi dapat difaktorkan menjadi $f(x) = \frac{4(x - 3)}{(x - 2)(x - 3)}$. Daerah asal alaminya adalah $D_f = \{x \mid x \neq 2 \text{ dan } x \neq 3, x \in \mathbb{R}\}$. Untuk $x \neq 3$, fungsi bernilai $f(x) = \frac{4}{x - 2}$. Karena $x \neq 3$, maka nilai $f(x) \neq \frac{4}{3 - 2} = 4$. Selain itu, bentuk pecahan $\frac{4}{x - 2}$ tidak pernah bernilai nol untuk nilai real $x$ mana pun. Jadi daerah hasil fungsi adalah $R_f = \{y \mid y \neq 0 \text{ dan } y \neq 4, y \in \mathbb{R}\}$.</sub>

**Pembahasan:** Langkah 1: Tentukan domain alami dengan memfaktorkan penyebut:
$$x^2 - 5x + 6 = (x - 2)(x - 3) \neq 0 \implies x \neq 2 \text{ dan } x \neq 3$$
Langkah 2: Sederhanakan fungsi untuk $x \neq 3$:
$$f(x) = \frac{4(x - 3)}{(x - 2)(x - 3)} = \frac{4}{x - 2}$$
Langkah 3: Cari nilai tak terdefinisi dari grafik akibat titik lubang pada $x = 3$:
$$y_{\text{lubang}} = \frac{4}{3 - 2} = 4$$
Langkah 4: Tentukan asimtot horizontal fungsi:
Untuk $x \to \pm\infty$, $\frac{4}{x - 2} \to 0$, dan pembilang tidak pernah nol sehingga $y \neq 0$.
Dengan demikian, daerah hasil fungsi adalah $\{y \mid y \neq 0 \text{ dan } y \neq 4, y \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b06-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: parameter fungsi rasional*

Diketahui fungsi rasional $f(x) = \frac{a x^2 + 7x - 4}{x - 2}$ dengan $a$ adalah konstanta bilangan real bukan nol. Jika grafik fungsi $f$ memiliki garis asimtot miring $y = 3x + b$, maka nilai dari $a \cdot b$ adalah ....

- A. $3$  
  <sub>Salah: Siswa salah melakukan pembagian aljabar sehingga mendapatkan $b = 1$ dan mengalikan $3 \cdot 1 = 3$.</sub>
- B. $-39$  
  <sub>Salah: Siswa salah menghitung tanda pembagian pada suku linear sisa sehingga memperoleh $b = -13$.</sub>
- C. $21$  
  <sub>Salah: Siswa mengira $b$ diperoleh langsung dari koefisien $x$ pada pembilang yaitu $7$, sehingga menghitung $3 \cdot 7 = 21$.</sub>
- **D. $39$** ✅  
  <sub>Benar: Melalui pembagian bersusun $(ax^2 + 7x - 4) : (x - 2)$, suku pertama hasil bagi adalah $ax$. Karena persamaan asimtot miring memiliki gradien $3$, maka haruslah $a = 3$. Selanjutnya, pembagian $(3x^2 + 7x - 4) : (x - 2)$ menghasilkan $3x + 13$ dengan sisa $22$. Jadi, persamaan asimtot miringnya adalah $y = 3x + 13$, yang berarti $b = 13$. Dengan demikian, $a \cdot b = 3 \cdot 13 = 39$.</sub>

**Pembahasan:** Langkah 1: Lakukan pembagian polinomial pembilang oleh penyebut:
$$ax^2 + 7x - 4 = (x - 2)(ax + c) + r$$
$$ax^2 + 7x - 4 = ax^2 + (c - 2a)x - 2c + r$$

Langkah 2: Samakan hasil bagi $ax + c$ dengan bentuk asimtot miring $y = 3x + b$:
Koefisien derajat tertinggi: $a = 3$.

Langkah 3: Hitung suku konstanta hasil bagi $c$:
Koefisien suku $x$: $c - 2a = 7$
$$c - 2(3) = 7 \implies c - 6 = 7 \implies c = 13$$
Karena hasil bagi adalah $3x + 13$, maka $b = 13$.

Langkah 4: Hitung nilai perkalian $a \cdot b$:
$$a \cdot b = 3 \cdot 13 = 39$$
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b06-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: domain fungsi campuran akar*

Daerah asal dari fungsi $f(x) = \frac{\sqrt{25 - x^2}}{\sqrt{x - 3}}$ pada himpunan bilangan real adalah $D_f$. Jika $D_f$ dinyatakan dalam bentuk selang $(a, b]$, maka nilai dari $a^2 + b^2$ adalah ....

- A. $16$  
  <sub>Salah: Siswa salah mengoperasikan penyebut dengan mengira $a = 0$ dan $b = 4$ sehingga memperoleh nilai $16$.</sub>
- B. $26$  
  <sub>Salah: Siswa salah mencari pembuat nol dari $x - 3 > 0$ menjadi $x > 1$, sehingga menghitung $1^2 + 5^2 = 26$.</sub>
- C. $50$  
  <sub>Salah: Siswa mengabaikan syarat penyebut dan hanya memakai batas dari pembilang $-5$ dan $5$ sehingga menghitung $(-5)^2 + 5^2 = 50$.</sub>
- **D. $34$** ✅  
  <sub>Benar: Agar fungsi terdefinisi, bagian pembilang mensyaratkan $25 - x^2 \ge 0 \implies -5 \le x \le 5$. Bagian penyebut di bawah tanda akar berakar genap dan tidak boleh bernilai nol, sehingga $x - 3 > 0 \implies x > 3$. Irisan dari kedua syarat tersebut adalah $3 < x \le 5$, yang dituliskan dalam bentuk selang $(3, 5]$. Dengan demikian, diperoleh $a = 3$ dan $b = 5$, sehingga $a^2 + b^2 = 3^2 + 5^2 = 9 + 25 = 34$.</sub>

**Pembahasan:** Langkah 1: Tentukan syarat terdefinisi untuk pembilang:
Bentuk $\sqrt{25 - x^2}$ terdefinisi pada bilangan real jika radicand tidak negatif:
$$25 - x^2 \ge 0 \implies x^2 \le 25 \implies -5 \le x \le 5$$

Langkah 2: Tentukan syarat terdefinisi untuk penyebut:
Bentuk $\sqrt{x - 3}$ berada di penyebut, sehingga selain radicand tidak boleh negatif, penyebut juga tidak boleh bernilai nol:
$$x - 3 > 0 \implies x > 3$$

Langkah 3: Tentukan irisan dari kedua syarat:
$$\{-5 \le x \le 5\} \cap \{x > 3\} = 3 < x \le 5$$
Dalam notasi interval, selang ini adalah $(3, 5]$, sehingga $a = 3$ dan $b = 5$.

Langkah 4: Hitung nilai $a^2 + b^2$:
$$a^2 + b^2 = 3^2 + 5^2 = 9 + 25 = 34$$
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b06-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: pemodelan gaya fungsi rasional*

Sebuah benda bermassa $m = 600\text{ kg}$ ditarik dari keadaan diam sehingga menempuh jarak perpindahan tetap $s = 48\text{ meter}$. Besar gaya dorong yang bekerja dimodelkan sebagai fungsi rasional terhadap waktu tempuh $t$ (dalam detik), yaitu $F(t) = \frac{m \cdot s}{t^2}$. Jika gaya yang diberikan dibatasi paling sedikit $200\text{ N}$ dan paling banyak $800\text{ N}$, maka rentang waktu tempuh $t$ yang memenuhi adalah ....

- A. $t \le 6 \text{ atau } t \ge 12$  
  <sub>Salah: Siswa salah membalik arah tanda pertidaksamaan saat membalik pecahan variabel.</sub>
- **B. $6 \le t \le 12$** ✅  
  <sub>Benar: Model fungsi gaya adalah $F(t) = \frac{600 \cdot 48}{t^2} = \frac{28.800}{t^2}$. Syarat gaya yang diizinkan adalah $200 \le F(t) \le 800$, sehingga $200 \le \frac{28.800}{t^2} \le 800$. Karena $t > 0$, maka $\frac{28.800}{800} \le t^2 \le \frac{28.800}{200}$, yang menghasilkan $36 \le t^2 \le 144$. Dengan menarik akar untuk nilai $t > 0$, diperoleh $6 \le t \le 12$ detik.</sub>
- C. $36 \le t \le 144$  
  <sub>Salah: Siswa sudah menemukan batas nilai $t^2$, tetapi lupa menarik akar kuadrat untuk mendapatkan batas waktu $t$.</sub>
- D. $4 \le t \le 10$  
  <sub>Salah: Siswa salah melakukan pembagian numerik pada konstanta gaya dan perpindahan.</sub>

**Pembahasan:** Langkah 1: Susun model fungsi rasional gaya:
$$F(t) = \frac{m \cdot s}{t^2} = \frac{600 \cdot 48}{t^2} = \frac{28.800}{t^2}$$

Langkah 2: Buat model pertidaksamaan sesuai batasan nilai gaya:
$$200 \le \frac{28.800}{t^2} \le 800$$

Langkah 3: Karena $t > 0$, kalikan semua ruas dengan $t^2$ lalu bagi dengan konstanta pembatas:
$$200 t^2 \le 28.800 \implies t^2 \le \frac{28.800}{200} = 144$$
$$800 t^2 \ge 28.800 \implies t^2 \ge \frac{28.800}{800} = 36$$
Diperoleh:
$$36 \le t^2 \le 144$$

Langkah 4: Karena waktu $t$ harus bernilai positif, tarik akar kuadrat pada setiap sisi:
$$\sqrt{36} \le t \le \sqrt{144} \implies 6 \le t \le 12$$
**Acuan:** siswa — siswa hal.281

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b06-b-hard-bt01-008
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi asimtot vertikal*

Seorang siswa mengklaim bahwa grafik fungsi rasional $f(x) = \frac{x^2 - 4x - 12}{x^2 - 8x + 12}$ memiliki dua garis asimtot vertikal, yaitu $x = 2$ dan $x = 6$, karena penyebutnya bernilai nol pada kedua nilai tersebut. Manakah evaluasi yang paling tepat mengenai klaim siswa tersebut?

- **A. Klaim salah, karena grafik hanya memiliki satu asimtot vertikal yaitu $x = 2$, sedangkan pada $x = 6$ grafik membentuk lubang (hole).** ✅  
  <sub>Benar: Faktorisasi pembilang dan penyebut menghasilkan $(x - 6)(x + 2)$ dan $(x - 6)(x - 2)$. Faktor $(x - 6)$ saling menghilangkan sehingga $x = 6$ bukan asimtot melainkan lubang.</sub>
- B. Klaim salah, karena grafik tidak memiliki asimtot vertikal sama sekali melainkan hanya memiliki asimtot horizontal $y = 1$.  
  <sub>Salah: Mengira pembatalan faktor menghilangkan semua asimtot vertikal.</sub>
- C. Klaim salah, karena garis asimtot vertikal fungsi tersebut yang benar adalah $x = -2$ dan $x = 2$.  
  <sub>Salah: Menganggap pembuat nol pembilang sebagai asimtot vertikal.</sub>
- D. Klaim benar, karena setiap pembuat nol dari fungsi polinomial penyebut selalu menghasilkan garis asimtot vertikal.  
  <sub>Salah: Mengabaikan syarat bahwa pembilang dan penyebut tidak boleh memiliki faktor persekutuan.</sub>

**Pembahasan:** Faktorkan fungsi $f(x)$:
$$f(x) = \frac{x^2 - 4x - 12}{x^2 - 8x + 12} = \frac{(x - 6)(x + 2)}{(x - 6)(x - 2)}$$
Untuk $x \neq 6$, fungsi disederhanakan menjadi $f(x) = \frac{x + 2}{x - 2}$.
Pembuat nol penyebut setelah penyederhanaan adalah $x - 2 = 0 \Rightarrow x = 2$. Oleh karena itu, asimtot vertikal satu-satunya adalah garis $x = 2$. Pada nilai $x = 6$, grafik fungsi tidak terdefinisi dan membentuk titik berlubang (hole), bukan asimtot vertikal. Jadi, klaim siswa tersebut salah.
**Acuan:** siswa — siswa hal.286 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b06-b-hard-bt01-009
*variasi (angka) | C5 | 4 langkah | jenis: pemodelan jarak horizon*

Sebuah satelit pengamat dirancang mengorbit sebuah planet berkeadaan bulat sempurna dengan jari-jari $R = 4.000\text{ km}$. Jarak pandang garis singgung ke horizon dari satelit pada ketinggian $h\text{ km}$ di atas permukaan planet dimodelkan oleh fungsi akar $d(h) = \sqrt{h^2 + 2Rh}$. Jika satelit tersebut harus ditempatkan pada ketinggian tertentu agar jarak pandangnya ke horizon tepat bernilai $3.000\text{ km}$, berapakah nilai ketinggian $h$ yang harus dipilih?

- A. $1.500\text{ km}$  
  <sub>Salah: Kesalahan membagi jarak horizon dengan 2 tanpa menyelesaikan persamaan kuadrat.</sub>
- B. $2.000\text{ km}$  
  <sub>Salah: Kesalahan mengabaikan suku $h^2$ dan hanya menghitung $2Rh = 3.000^2$ dengan aproksimasi keliru.</sub>
- **C. $1.000\text{ km}$** ✅  
  <sub>Benar: Persamaan $h^2 + 8.000h = 3.000^2$ menghasilkan $h^2 + 8.000h - 9.000.000 = 0$, dengan akar positif $h = 1.000$.</sub>
- D. $9.000\text{ km}$  
  <sub>Salah: Mengambil nilai mutlak dari akar negatif pemfaktoran $(h + 9.000)(h - 1.000) = 0$.</sub>

**Pembahasan:** Diketahui model jarak horizon:
$$d(h) = \sqrt{h^2 + 2(4.000)h} = \sqrt{h^2 + 8.000h}$$
Diketahui $d(h) = 3.000$, maka:
$$\sqrt{h^2 + 8.000h} = 3.000$$
Kuadratkan kedua ruas:
$$h^2 + 8.000h = 9.000.000$$
$$h^2 + 8.000h - 9.000.000 = 0$$
Faktorkan persamaan kuadrat:
$$(h + 9.000)(h - 1.000) = 0$$
Diperoleh $h = -9.000$ atau $h = 1.000$.
Karena ketinggian $h$ harus bernilai positif, maka ketinggian orbit yang dipilih adalah $h = 1.000\text{ km}$.
**Acuan:** siswa — siswa hal.287 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b06-b-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: parameter daerah asal fungsi rasional*

Diketahui fungsi rasional $f(x) = \frac{2x + 7}{x^2 - 2mx + (m + 12)}$ terdefinisi untuk seluruh bilangan real ($D_f = \mathbb{R}$). Himpunan seluruh nilai konstanta real $m$ yang memenuhi kondisi tersebut adalah ....

- A. $\{m \mid m < -3 \text{ atau } m > 4, m \in \mathbb{R}\}$  
  <sub>Salah: Menggunakan syarat $D > 0$ yang justru membuat penyebut memiliki dua pembuat nol real.</sub>
- B. $\{m \mid -4 < m < 3, m \in \mathbb{R}\}$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan bentuk kuadrat $m^2 - m - 12$.</sub>
- C. $\{m \mid -3 \le m \le 4, m \in \mathbb{R}\}$  
  <sub>Salah: Menyertakan tanda sama dengan ($D \le 0$), padahal saat $D = 0$ terdapat satu nilai pembuat nol pada penyebut.</sub>
- **D. $\{m \mid -3 < m < 4, m \in \mathbb{R}\}$** ✅  
  <sub>Benar: Agar penyebut tidak pernah bernilai nol, diskriminan persamaan kuadrat harus memenuhi $D < 0$, menghasilkan $-3 < m < 4$.</sub>

**Pembahasan:** Daerah asal fungsi $f(x)$ adalah seluruh himpunan bilangan real jika dan hanya jika penyebut tidak pernah bernilai nol untuk setiap $x \in \mathbb{R}$:
$$x^2 - 2mx + (m + 12) \neq 0, \quad \forall x \in \mathbb{R}$$
Bentuk kuadrat dengan koefisien $x^2$ positif ($a = 1 > 0$) tidak memiliki pembuat nol real apabila diskriminannya bernilai negatif ($D < 0$):
$$D = b^2 - 4ac < 0$$
$$(-2m)^2 - 4(1)(m + 12) < 0$$
$$4m^2 - 4m - 48 < 0$$
Bagi kedua ruas dengan 4:
$$m^2 - m - 12 < 0$$
$$(m - 4)(m + 3) < 0$$
Pertaksamaan ini terpenuhi pada selang $-3 < m < 4$.
Jadi, himpunan nilai $m$ yang memenuhi adalah $\{m \mid -3 < m < 4, m \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b06-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: analisis asimtot fungsi rasional kuadrat*

Diketahui fungsi rasional $f(x) = \frac{a x^2 + 8x - 5}{2x^2 - 5x - 3}$ dengan $a$ adalah suatu konstanta bilangan real. Jika grafik fungsi $f$ memiliki garis asimtot horizontal $y = 3$ dan salah satu garis asimtot vertikalnya adalah $x = p$ dengan $p > 0$, maka nilai dari $a + 2p$ adalah ....

- A. $9$  
  <sub>Salah: Hanya menghitung nilai $a + p = 6 + 3 = 9$ tanpa mengalikan $p$ dengan 2.</sub>
- B. $5$  
  <sub>Salah: Menggunakan asimtot vertikal negatif $x = -\frac{1}{2}$ sehingga $6 + 2(-\frac{1}{2}) = 5$.</sub>
- **C. $12$** ✅  
  <sub>Benar: Dari asimtot horizontal diperoleh $a / 2 = 3 \Rightarrow a = 6$. Asimtot vertikal positif dari $(2x + 1)(x - 3) = 0$ adalah $x = 3$, sehingga $a + 2p = 6 + 2(3) = 12$.</sub>
- D. $15$  
  <sub>Salah: Salah mengidentifikasi koefisien asimtot horizontal dengan menganggap $a = 3$ dan $p = 6$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $a$.
Untuk fungsi rasional dengan derajat pembilang dan penyebut sama, asimtot horizontal ditentukan oleh perbandingan koefisien pangkat tertinggi:
$$y = \frac{a}{2}$$
Diketahui asimtot horizontal adalah $y = 3$, maka:
$$\frac{a}{2} = 3 \Rightarrow a = 6$$

Langkah 2: Menentukan asimtot vertikal.
Penyebut bernilai nol saat:
$$2x^2 - 5x - 3 = 0$$
$$(2x + 1)(x - 3) = 0$$
Diperoleh $x = -\frac{1}{2}$ atau $x = 3$.
Periksa pembilang $6x^2 + 8x - 5$:
Untuk $x = 3$, pembilang bernilai $6(3)^2 + 8(3) - 5 = 73 \neq 0$.
Karena pembilang tidak nol di $x = 3$, maka garis $x = 3$ adalah asimtot vertikal.
Karena disyaratkan $p > 0$, maka $p = 3$.

Langkah 3: Menghitung nilai yang diminta:
$$a + 2p = 6 + 2(3) = 12$$
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b06-b-hard-bt01-012
*orisinal | C6 | 5 langkah | jenis: perancangan domain fungsi akar*

Daerah asal alami dari fungsi akar $f(x) = \sqrt{\frac{x - 2}{x^2 - 7x + 12}}$ pada himpunan bilangan real dapat dinyatakan dalam bentuk selang (interval) sebagai ....

- **A. $[2, 3) \cup (4, \infty)$** ✅  
  <sub>Benar: Syarat radikan $\ge 0$ dan penyebut $\neq 0$ menghasilkan pembuat nol pembilang $x = 2$ (tertutup) dan penyebut $x = 3, 4$ (terbuka), dengan tanda positif pada $[2, 3) \cup (4, \infty)$.</sub>
- B. $(-\infty, 2] \cup (3, 4)$  
  <sub>Salah: Terbalik dalam menentukan interval hasil uji tanda positif dan negatif pada garis bilangan.</sub>
- C. $(2, 3) \cup (4, \infty)$  
  <sub>Salah: Menggunakan kurung buka pada $x = 2$, seolah-olah nilai nol pada pembilang tidak diperbolehkan.</sub>
- D. $[2, 3] \cup [4, \infty)$  
  <sub>Salah: Memasukkan nilai pembuat nol penyebut ($x = 3$ dan $x = 4$) ke dalam daerah asal.</sub>

**Pembahasan:** Fungsi $f(x)$ merupakan fungsi akar berorde genap ($n = 2$), sehingga terdefinisi pada bilangan real jika nilai di dalam akar tidak negatif dan penyebut tidak sama dengan nol:
$$\frac{x - 2}{x^2 - 7x + 12} \ge 0$$
Faktorkan penyebut:
$$\frac{x - 2}{(x - 3)(x - 4)} \ge 0$$
Syarat penyebut tidak sama dengan nol:
$$(x - 3)(x - 4) \neq 0 \Rightarrow x \neq 3 \text{ dan } x \neq 4$$
Titik kritis pembuat nol adalah $x = 2$, $x = 3$, dan $x = 4$.
Uji tanda pada interval:
- Untuk $x < 2$ (misal $x = 0$): $\frac{-}{(-)(-)} = \frac{-}{+} < 0$ (negatif)
- Untuk $2 \le x < 3$ (misal $x = 2,5$): $\frac{+}{(-)(-)} = \frac{+}{+} > 0$ (positif, termasuk $x = 2$)
- Untuk $3 < x < 4$ (misal $x = 3,5$): $\frac{+}{(+)(-)} = \frac{+}{-} < 0$ (negatif)
- Untuk $x > 4$ (misal $x = 5$): $\frac{+}{(+)(+)} = \frac{+}{+} > 0$ (positif)

Daerah yang memenuhi syarat $\ge 0$ adalah $2 \le x < 3$ atau $x > 4$.
Dalam notasi selang (interval), daerah asal tersebut ditulis sebagai $[2, 3) \cup (4, \infty)$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b06-b-hard-bt01-013
*variasi (angka) | C5 | 4 langkah | jenis: daerah asal dan hasil fungsi rasional*

Tentukan daerah asal dan daerah hasil fungsi berikut. $f(x) = \frac{x}{x^2 + 4}$

- **A. Daerah asal $\{x \mid x \in \mathbb{R}\}$ dan daerah hasil $\{y \mid -\frac{1}{4} \le y \le \frac{1}{4}, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Penyebut $x^2 + 4 > 0$ untuk setiap $x \in \mathbb{R}$, sehingga daerah asal adalah $\mathbb{R}$. Untuk daerah hasil, dari $y(x^2 + 4) = x \iff yx^2 - x + 4y = 0$. Jika $y = 0$, diperoleh $x = 0$ (terdefinisi). Jika $y \neq 0$, agar persamaan memiliki solusi real $x$, syaratnya $D \ge 0 \Rightarrow (-1)^2 - 4(y)(4y) \ge 0 \Rightarrow 1 - 16y^2 \ge 0 \Rightarrow y^2 \le \frac{1}{16}$, yaitu $-\frac{1}{4} \le y \le \frac{1}{4}$.</sub>
- B. Daerah asal $\{x \mid x \in \mathbb{R}\}$ dan daerah hasil $\{y \mid y \neq 0, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengenali domain dengan benar tetapi gagal menganalisis nilai maksimum/minimum pecahan kuadratik sehingga hanya menebak asimtot horizontal $y = 0$.</sub>
- C. Daerah asal $\{x \mid x \neq \pm 2, x \in \mathbb{R}\}$ dan daerah hasil $\{y \mid y \neq 0, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah mengira pembuat nol penyebut adalah $x^2 + 4 = 0 \Rightarrow x = \pm 2$ dan menganggap daerah hasil fungsi rasional selalu $y \neq 0$.</sub>
- D. Daerah asal $\{x \mid x \in \mathbb{R}\}$ dan daerah hasil $\{y \mid -2 \le y \le 2, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah menghitung pertidaksamaan diskriminan dengan menarik akar dari $4$ dan bukan dari $\frac{1}{16}$.</sub>

**Pembahasan:** 1. Daerah Asal:
Penyebut fungsi adalah $x^2 + 4$. Karena untuk setiap bilangan real $x$, $x^2 \ge 0$, maka $x^2 + 4 \ge 4 > 0$. Penyebut tidak pernah bernilai nol untuk bilangan real mana pun. Dengan demikian, daerah asal fungsi adalah $D_f = \{x \mid x \in \mathbb{R}\}$.

2. Daerah Hasil:
Misalkan $y = \frac{x}{x^2 + 4}$.
Kalikan kedua ruas dengan $x^2 + 4$:
$y(x^2 + 4) = x \iff yx^2 - x + 4y = 0$.
- Kasus $y = 0$:
$0 \cdot x^2 - x + 0 = 0 \Rightarrow -x = 0 \Rightarrow x = 0$.
Karena $x = 0 \in D_f$, maka $y = 0$ termasuk dalam daerah hasil.
- Kasus $y \neq 0$:
Persamaan $yx^2 - x + 4y = 0$ merupakan persamaan kuadrat dalam $x$. Agar $x$ bernilai real, nilai diskriminannya harus memenuhi $D \ge 0$:
$D = b^2 - 4ac = (-1)^2 - 4(y)(4y) \ge 0$
$1 - 16y^2 \ge 0$
$16y^2 \le 1$
$y^2 \le \frac{1}{16}$
$-\frac{1}{4} \le y \le \frac{1}{4}$.

Karena $y = 0$ termuat di dalam selang $[-\frac{1}{4}, \frac{1}{4}]$, daerah hasil fungsi adalah $R_f = \{y \mid -\frac{1}{4} \le y \le \frac{1}{4}, y \in \mathbb{R}\}$.
**Acuan:** pretest — kelas11_tl-b06-p0287-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b06-b-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: evaluasi kesamaan fungsi rasional*

Diberikan dua buah fungsi $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ dan $g(x) = x - 1$. Seorang siswa mengklaim bahwa $f(x) = g(x)$ untuk seluruh himpunan bilangan real karena bentuk aljabar pembilang dapat difaktorkan dan disederhanakan dengan membagi suku $(x - 3)$. Evaluasi yang paling tepat mengenai klaim siswa tersebut adalah ....

- A. Klaim benar, karena sifat pembagian aljabar menjamin bahwa kedua fungsi memiliki nilai keluaran yang sama untuk setiap input bilangan real  
  <sub>Salah: Siswa mengabaikan pembatasan daerah asal penyebut tidak boleh nol dalam penyederhanaan aljabar rasional.</sub>
- B. Klaim salah, karena garis $x = 3$ merupakan asimtot vertikal bagi grafik $f(x)$, sedangkan grafik $g(x)$ tidak memiliki asimtot  
  <sub>Salah: Siswa keliru membedakan antara titik berlubang (hole yang disebabkan faktor persekutuan yang saling membagi) dengan asimtot vertikal.</sub>
- **C. Klaim salah, karena $D_f = \{x \mid x \neq 3, x \in \mathbb{R}\}$ sedangkan $D_g = \mathbb{R}$, sehingga grafik $f(x)$ memiliki titik berlubang (hole) di $(3, 2)$ sedangkan grafik $g(x)$ garis lurus kontinu** ✅  
  <sub>Benar: Dua fungsi dikatakan sama jika memiliki aturan dan domain yang sama. Pada $f(x)$, nilai $x = 3$ membuat penyebut nol sehingga $3 \notin D_f$, membentuk titik lubang $(3, 2)$. Sedangkan fungsi linear $g(x)$ terdefinisi untuk seluruh bilangan real tanpa lubang.</sub>
- D. Klaim salah, karena daerah hasil kedua fungsi berbeda yaitu $R_f = \mathbb{R}$ sedangkan $R_g = \{y \mid y \neq 2, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa tertukar antara daerah hasil fungsi $f$ dan daerah hasil fungsi $g$.</sub>

**Pembahasan:** Langkah 1: Tinjau definisi kesamaan dua fungsi.
Dua fungsi $f$ dan $g$ dikatakan sama ($f = g$) jika dan hanya jika keduanya memiliki daerah asal yang sama ($D_f = D_g$) dan $f(x) = g(x)$ untuk setiap $x$ dalam daerah asal tersebut.

Langkah 2: Tentukan daerah asal masing-masing fungsi.
- Fungsi $f(x) = \frac{x^2 - 4x + 3}{x - 3}$ terdefinisi jika penyebutnya tidak sama dengan nol: $x - 3 \neq 0 \implies x \neq 3$. Jadi, $D_f = \{x \mid x \neq 3, x \in \mathbb{R}\}$.
- Fungsi $g(x) = x - 1$ adalah fungsi linear polinomial, sehingga daerah asalnya adalah seluruh bilangan real: $D_g = \mathbb{R}$.

Langkah 3: Analisis karakteristik grafik saat $x \to 3$.
Untuk setiap $x \neq 3$:
$f(x) = \frac{(x - 3)(x - 1)}{x - 3} = x - 1$.
Karena faktor persekutuan $(x - 3)$ saling membatalkan, grafik fungsi $f(x)$ tidak memiliki asimtot vertikal di $x = 3$, melainkan memiliki titik berlubang (removable discontinuity / hole) pada koordinat $(3, 3 - 1) = (3, 2)$.
Sebaliknya, grafik fungsi $g(x) = x - 1$ merupakan garis lurus penuh yang kontinu dan memuat titik $(3, 2)$.

Langkah 4: Evaluasi klaim.
Karena daerah asal kedua fungsi tidak identik ($D_f \neq D_g$), klaim siswa tersebut salah.
**Acuan:** siswa — siswa hal.275

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11_tl-b06-b-hard-bt01-015
*variasi (konteks) | C5 | 3 langkah | jenis: evaluasi relasi domain kodomain fungsi akar*

Seorang siswa mengklaim bahwa jika suatu fungsi akar berindeks genap $f(x) = \sqrt{g(x)} + c$ memiliki daerah asal seluruh himpunan bilangan real ($D_f = \mathbb{R}$), maka daerah hasilnya ($R_f$) pasti selalu berupa selang $[c, \infty)$. Untuk menguji klaim tersebut, seorang guru memberikan fungsi $f(x) = \sqrt{x^2 + 9} + 2$. Berdasarkan fungsi tersebut, kesimpulan evaluasi yang tepat terhadap klaim siswa adalah ....

- **A. Klaim salah, karena untuk setiap $x \in \mathbb{R}$ berlaku $x^2 + 9 \ge 9$, sehingga daerah hasilnya adalah $[5, \infty)$, bukan $[2, \infty)$.** ✅  
  <sub>Benar: Karena $x^2 \ge 0$, nilai minimum $x^2 + 9$ adalah 9, sehingga nilai minimum $f(x)$ adalah $\sqrt{9} + 2 = 5$. Maka daerah hasilnya $[5, \infty)$, membuktikan klaim bahwa daerah hasil selalu $[c, \infty)$ adalah salah.</sub>
- B. Klaim benar, karena setiap fungsi akar yang terdefinisi pada $\mathbb{R}$ memiliki nilai terkecil fungsi tepat di $y = c$.  
  <sub>Salah: Siswa berasumsi salah bahwa batas bawah bentuk akar $\sqrt{g(x)}$ selalu mencapai nilai nol.</sub>
- C. Klaim salah, karena fungsi akar berderajat genap tidak dapat memiliki daerah asal seluruh bilangan real $\mathbb{R}$.  
  <sub>Salah: Siswa keliru memahami syarat daerah asal akar, padahal $x^2 + 9 > 0$ untuk setiap bilangan real $x$.</sub>
- D. Klaim benar, karena pembuat nol dari bentuk akar adalah $x = 0$ sehingga nilai minimum fungsinya adalah $f(0) = 2$ dan $R_f = [2, \infty)$.  
  <sub>Salah: Siswa keliru menganggap nilai akar bernilai 0 ketika $x = 0$ tanpa menghitung $\sqrt{0 + 9} = 3$.</sub>

**Pembahasan:** Untuk fungsi $f(x) = \sqrt{x^2 + 9} + 2$:
1. Karena $x^2 \ge 0$ untuk seluruh $x \in \mathbb{R}$, maka $x^2 + 9 \ge 9 > 0$. Dengan demikian, fungsi terdefinisi untuk seluruh bilangan real ($D_f = \mathbb{R}$).
2. Nilai minimum dari bentuk $\sqrt{x^2 + 9}$ tercapai saat $x = 0$, yaitu $\sqrt{0 + 9} = 3$.
3. Nilai minimum fungsi adalah $f(0) = 3 + 2 = 5$.
4. Karena nilai $\sqrt{x^2 + 9}$ dapat membesar tanpa batas seiring $|x| \to \infty$, daerah hasil fungsinya adalah $R_f = [5, \infty)$.
Hal ini membuktikan bahwa klaim siswa salah.
**Acuan:** siswa — siswa hal.287 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11_tl-b06-b-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: daerah asal fungsi akar irasional*

Daerah asal dari fungsi $f(x) = \sqrt{6 - x - \sqrt{x + 6}}$ pada himpunan bilangan real adalah $D_f$. Banyaknya bilangan bulat yang termuat di dalam $D_f$ adalah ....

- A. 4  
  <sub>Salah: Siswa hanya memperhitungkan bilangan bulat tak negatif dalam rentang $[0, 3]$.</sub>
- **B. 10** ✅  
  <sub>Benar: Syarat domain menghasilkan $-6 \le x \le 3$, sehingga terdapat 10 bilangan bulat yaitu $-6, -5, -4, -3, -2, -1, 0, 1, 2, 3$.</sub>
- C. 7  
  <sub>Salah: Siswa keliru menyelesaikan pertidaksamaan kuadrat sehingga mendapatkan batas bawah $-3$.</sub>
- D. 9  
  <sub>Salah: Siswa menghitung selisih batas $3 - (-6) = 9$ tanpa menambahkan 1 untuk kedua batas inklusif.</sub>

**Pembahasan:** Fungsi $f(x) = \sqrt{6 - x - \sqrt{x + 6}}$ terdefinisi pada $\mathbb{R}$ jika memenuhi dua syarat:
1. Bentuk akar dalam: $x + 6 \ge 0 \implies x \ge -6$.
2. Bentuk akar luar: $6 - x - \sqrt{x + 6} \ge 0 \implies \sqrt{x + 6} \le 6 - x$.
Karena $\sqrt{x + 6} \ge 0$, maka harus berlaku $6 - x \ge 0 \implies x \le 6$.
Kuadratkan kedua ruas:
$x + 6 \le (6 - x)^2$
$x + 6 \le 36 - 12x + x^2$
$x^2 - 13x + 30 \ge 0$
$(x - 3)(x - 10) \ge 0$
Diperoleh $x \le 3$ atau $x \ge 10$.
Irisan dari seluruh syarat:
$x \ge -6$, $x \le 6$, dan ($x \le 3$ atau $x \ge 10$)
Diperoleh $D_f = [-6, 3]$.
Bilangan bulat pada $D_f$: $-6, -5, -4, -3, -2, -1, 0, 1, 2, 3$.
Banyaknya bilangan bulat = $3 - (-6) + 1 = 10$.
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11_tl-b06-b-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: parameter asimtot horizontal*

Diketahui fungsi rasional $f(x) = \frac{a x^2 + b x + 6}{2x^2 - 8}$ dengan $a$ dan $b$ adalah konstanta bilangan real. Garis $y = 3$ merupakan asimtot horizontal dari grafik fungsi $f$. Jika grafik fungsi $f$ memotong garis asimtot horizontal tersebut pada titik dengan absis $x = 5$, nilai dari $a + b$ adalah ....

- **A. 0** ✅  
  <sub>Benar: Dari asimtot didapat $a/2 = 3 \implies a = 6$, dan dari $f(5) = 3$ didapat $b = -6$, sehingga $a + b = 6 + (-6) = 0$.</sub>
- B. -6  
  <sub>Salah: Siswa hanya menyebutkan nilai dari parameter $b$.</sub>
- C. 6  
  <sub>Salah: Siswa hanya menghitung nilai parameter $a$ dan mengabaikan penjumlahan dengan parameter $b$.</sub>
- D. 12  
  <sub>Salah: Siswa salah tanda saat menyelesaikan persamaan titik potong sehingga menghasilkan $b = 6$, lalu $a + b = 12$.</sub>

**Pembahasan:** 1. Derajat pembilang sama dengan derajat penyebut (sama-sama 2). Asimtot horizontal ditentukan oleh rasio koefisien pangkat tertinggi:
$y = \frac{a}{2}$.
Diketahui asimtot horizontal adalah $y = 3$, maka:
$\frac{a}{2} = 3 \implies a = 6$.

2. Grafik fungsi memotong garis asimtot horizontal $y = 3$ di $x = 5$, artinya $f(5) = 3$:
$f(5) = \frac{6(5^2) + b(5) + 6}{2(5^2) - 8} = 3$
$\frac{6(25) + 5b + 6}{2(25) - 8} = 3$
$\frac{156 + 5b}{42} = 3$
$156 + 5b = 126$
$5b = 126 - 156$
$5b = -30 \implies b = -6$.

3. Nilai $a + b = 6 + (-6) = 0$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11_tl-b06-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: analisis asimtot miring dan parabola*

Diketahui fungsi rasional $f(x) = \frac{3x^2 + m x + 8}{x - 2}$ dengan $m$ adalah suatu konstanta bilangan real. Garis asimtot miring dari grafik fungsi $f$ melalui titik puncak dari grafik fungsi kuadrat $g(x) = -x^2 + 4x + 1$. Nilai dari konstanta $m$ adalah ....

- A. -5  
  <sub>Salah: Siswa salah menentukan ordinat puncak parabola dengan menghitung $g(2) = 3$ bukan $5$.</sub>
- B. 7  
  <sub>Salah: Siswa salah memindahkan suku saat aljabar akhir sehingga memperoleh $m = 12 - 5 = 7$.</sub>
- **C. -7** ✅  
  <sub>Benar: Asimtot miring adalah $y = 3x + m + 6$. Titik puncak $g(x)$ adalah $(2, 5)$. Substitusi $(2, 5)$ menghasilkan $5 = 3(2) + m + 6 \implies m = -7$.</sub>
- D. 1  
  <sub>Salah: Siswa salah melakukan pembagian bersusun dengan mengabaikan perkalian $(-2)$ sehingga konstanta menjadi $m - 6$.</sub>

**Pembahasan:** 1. Pembagian polinomial untuk $f(x)$:
$\frac{3x^2 + mx + 8}{x - 2} = 3x + (m + 6) + \frac{2m + 20}{x - 2}$.
Maka persamaan asimtot miring grafik fungsi $f$ adalah $y = 3x + m + 6$.

2. Menentukan titik puncak grafik fungsi kuadrat $g(x) = -x^2 + 4x + 1$:
$x_p = -\frac{b}{2a} = -\frac{4}{2(-1)} = 2$.
$y_p = g(2) = -(2)^2 + 4(2) + 1 = -4 + 8 + 1 = 5$.
Jadi titik puncak $g(x)$ adalah $(2, 5)$.

3. Garis asimtot miring melalui $(2, 5)$:
$5 = 3(2) + m + 6$
$5 = 6 + m + 6$
$5 = m + 12$
$m = 5 - 12 = -7$.
**Acuan:** siswa — siswa hal.279

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11_tl-b06-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: evaluasi perpotongan asimtot fungsi rasional*

Seorang siswa menyatakan bahwa kurva dari grafik suatu fungsi rasional tidak akan pernah memotong garis asimtotnya. Untuk menguji pernyataan tersebut, guru menyajikan fungsi rasional $f(x) = \frac{2x^2 - 4x + 6}{x^2 + 2}$. Berdasarkan analisis terhadap fungsi $f(x)$, simpulan yang paling tepat mengenai pernyataan siswa tersebut adalah ....

- A. Pernyataan siswa salah, karena grafik $f(x)$ memotong asimtot vertikal di titik $(1, 0)$  
  <sub>Salah: Tertukar antara konsep asimtot vertikal dan horizontal, padahal penyebut $x^2 + 2 > 0$ tidak memiliki pembuat nol real.</sub>
- **B. Pernyataan siswa salah, karena grafik $f(x)$ memotong asimtot horizontalnya di titik $\left(\frac{1}{2}, 2\right)$** ✅  
  <sub>Benar: Asimtot horizontal $f(x)$ adalah garis $y = 2$, dan substitusi $f(x) = 2$ menghasilkan perpotongan tepat di titik $\left(\frac{1}{2}, 2\right)$.</sub>
- C. Pernyataan siswa benar, karena persamaan $f(x) = 2$ tidak memiliki solusi pada himpunan bilangan real  
  <sub>Salah: Mengira grafik fungsi tidak boleh memotong asimtot horizontal dan salah menyelesaikan persamaan aljabar perpotongan.</sub>
- D. Pernyataan siswa benar, karena fungsi $f(x)$ tidak memiliki asimtot horizontal maupun asimtot vertikal  
  <sub>Salah: Gagal mengenali keberadaan asimtot horizontal akibat pembagian derajat polinomial yang sama.</sub>

**Pembahasan:** Langkah-langkah evaluasi:
1. Tentukan asimtot vertikal: Penyebut fungsi adalah $x^2 + 2$. Karena $x^2 + 2 > 0$ untuk setiap $x \in \mathbb{R}$, penyebut tidak pernah bernilai nol. Jadi, grafik $f(x)$ tidak memiliki asimtot vertikal.
2. Tentukan asimtot horizontal: Karena derajat pembilang dan penyebut sama, yaitu 2, maka asimtot horizontal diperoleh dari rasio koefisien pangkat tertinggi:
$$y = \lim_{x \to \pm\infty} \frac{2x^2 - 4x + 6}{x^2 + 2} = 2$$
3. Periksa titik potong grafik $f(x)$ dengan garis asimtot horizontal $y = 2$:
$$\frac{2x^2 - 4x + 6}{x^2 + 2} = 2$$
$$2x^2 - 4x + 6 = 2(x^2 + 2)$$
$$2x^2 - 4x + 6 = 2x^2 + 4$$
$$-4x + 6 = 4 \implies -4x = -2 \implies x = \frac{1}{2}$$
4. Koordinat titik potongnya adalah $\left(\frac{1}{2}, 2\right)$. Dengan demikian, pernyataan siswa salah karena kurva fungsi memotong asimtot horizontalnya di titik $\left(\frac{1}{2}, 2\right)$.
**Acuan:** siswa — siswa hal.278

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas11_tl-b06-b-hard-bt01-020
*orisinal | C5 | 4 langkah | jenis: parameter domain fungsi akar*

Diketahui fungsi akar $f(x) = \sqrt{k x^2 - 4k x + (k + 12)}$ dengan $k$ adalah suatu konstanta bilangan real. Agar fungsi $f(x)$ terdefinisi untuk seluruh bilangan real (daerah asal $D_f = \mathbb{R}$), himpunan semua nilai $k$ yang memenuhi adalah ....

- A. $\{k \mid k \le 0 \text{ atau } k \ge 4, k \in \mathbb{R}\}$  
  <sub>Salah: Keliru menerapkan syarat diskriminan dengan menggunakan $D \ge 0$ alih-alih $D \le 0$.</sub>
- B. $\{k \mid 0 < k \le 4, k \in \mathbb{R}\}$  
  <sub>Salah: Lupa menguji kasus linier/konstan ketika $k = 0$ yang juga membuat fungsi terdefinisi pada seluruh bilangan real.</sub>
- C. $\{k \mid -4 \le k \le 0, k \in \mathbb{R}\}$  
  <sub>Salah: Salah melakukan pemfaktoran pada pertidaksamaan diskriminan $12k^2 - 48k \le 0$.</sub>
- **D. $\{k \mid 0 \le k \le 4, k \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat $g(x) \ge 0$ untuk setiap $x \in \mathbb{R}$ dipenuhi saat $k = 0$ (menghasilkan fungsi konstan $\sqrt{12}$) atau saat $k > 0$ dan $D \le 0$ ($0 < k \le 4$), sehingga gabungannya adalah $0 \le k \le 4$.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Syarat agar fungsi akar $f(x) = \sqrt{g(x)}$ terdefinisi pada seluruh $\mathbb{R}$ adalah $g(x) \ge 0$ untuk setiap $x \in \mathbb{R}$, yaitu:
$$k x^2 - 4k x + (k + 12) \ge 0$$
2. Tinjau Kasus 1 ($k = 0$):
Substitusikan $k = 0$ ke dalam fungsi:
$$f(x) = \sqrt{0 \cdot x^2 - 0 \cdot x + 12} = \sqrt{12}$$
Karena $\sqrt{12}$ terdefinisi untuk semua $x \in \mathbb{R}$, maka $k = 0$ memenuhi syarat.
3. Tinjau Kasus 2 ($k \neq 0$):
Bentuk kuadrat bernilai non-negatif untuk setiap $x \in \mathbb{R}$ (definit positif atau menyinggung sumbu-$x$) jika:
- Koefisien $x^2 > 0 \implies k > 0$
- Diskriminan $D \le 0$:
$$D = (-4k)^2 - 4(k)(k + 12) \le 0$$
$$16k^2 - 4k^2 - 48k \le 0$$
$$12k^2 - 48k \le 0$$
$$12k(k - 4) \le 0$$
Penyelesaian pertidaksamaan ini adalah $0 \le k \le 4$. Karena disyaratkan $k > 0$, maka diperoleh selang $0 < k \le 4$.
4. Gabungkan hasil dari Kasus 1 dan Kasus 2:
$$\{k = 0\} \cup \{k \mid 0 < k \le 4\} = \{k \mid 0 \le k \le 4, k \in \mathbb{R}\}$$
**Acuan:** siswa — siswa hal.283

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
