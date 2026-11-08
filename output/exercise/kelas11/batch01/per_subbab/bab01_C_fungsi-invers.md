# Lembar koreksi — kelas11 SMA11U-B1 subbab C: Fungsi Invers

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b01-c-easy-bt01-001
*orisinal | C1 | 1 langkah | jenis: syarat keberadaan invers*

Syarat utama agar suatu fungsi $f: A \to B$ memiliki fungsi invers $f^{-1}: B \to A$ adalah fungsi $f$ harus bersifat ....

- A. injektif saja  
  <sub>Salah: Mengira sifat satu-satu cukup tanpa memastikan seluruh anggota kodomain memiliki pasangan (surjektif).</sub>
- **B. bijektif (injektif dan surjektif)** ✅  
  <sub>Benar: Berdasarkan materi Buku Siswa halaman 50, hanya fungsi yang bijektif (gabungan injektif dan surjektif) yang memiliki fungsi invers.</sub>
- C. surjektif saja  
  <sub>Salah: Mengira sifat pada cukup tanpa memastikan setiap anggota memiliki tepat satu pasangan asal (injektif).</sub>
- D. konstan  
  <sub>Salah: Keliru mengidentifikasi jenis relasi khusus yang jelas tidak memiliki invers berupa fungsi.</sub>

**Pembahasan:** Agar relasi kebalikan dari suatu fungsi juga merupakan fungsi, setiap anggota kodomain harus memiliki tepat satu pasangan di domain. Hal ini berarti fungsi asal harus bersifat injektif (satu-satu) dan surjektif (pada), yang bersama-sama dinamakan fungsi bijektif.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b01-c-easy-bt01-002
*orisinal | C2 | 1 langkah | jenis: sifat komposisi fungsi invers*

Diketahui $f$ adalah fungsi bijektif dan $f^{-1}$ adalah fungsi invers dari $f$. Bentuk komposisi $(f \circ f^{-1})(x)$ untuk setiap $x$ pada daerah asal $f^{-1}$ adalah ....

- A. $-x$  
  <sub>Salah: Terkecoh menganggap tanda invers $-1$ sebagai perkalian dengan bilangan negatif satu.</sub>
- **B. $x$** ✅  
  <sub>Benar: Komposisi fungsi dengan inversnya selalu menghasilkan fungsi identitas, yaitu $(f \circ f^{-1})(x) = x$.</sub>
- C. $1$  
  <sub>Salah: Mengira invers berarti pembalikan nilai aritmetika seperti $x \cdot \frac{1}{x} = 1$.</sub>
- D. $0$  
  <sub>Salah: Mengira invers berarti saling meniadakan atau mengurangkan menjadi nol.</sub>

**Pembahasan:** Berdasarkan sifat fungsi invers, komposisi suatu fungsi dengan inversnya menghasilkan fungsi identitas, yaitu $(f \circ f^{-1})(x) = x$ dan $(f^{-1} \circ f)(x) = x$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b01-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi linear*

Diketahui fungsi $f(x) = 5x - 7$ dengan domain himpunan bilangan real. Rumus fungsi invers $f^{-1}(x)$ adalah ....

- A. $5x + 7$  
  <sub>Salah: Hanya mengganti tanda minus menjadi plus tanpa membagi dengan koefisien perkalian 5.</sub>
- B. $\frac{x + 5}{7}$  
  <sub>Salah: Tertukar posisi koefisien $x$ dengan nilai konstanta.</sub>
- C. $\frac{x - 7}{5}$  
  <sub>Salah: Salah dalam memindahkan konstanta $-7$ ke ruas seberang tanpa membalik tanda menjadi positif.</sub>
- **D. $\frac{x + 7}{5}$** ✅  
  <sub>Benar: Dari $y = 5x - 7$, diperoleh $5x = y + 7$ sehingga $x = \frac{y + 7}{5}$. Jadi, $f^{-1}(x) = \frac{x + 7}{5}$.</sub>

**Pembahasan:** Misalkan $y = f(x)$:
$y = 5x - 7$
$y + 7 = 5x$
$x = \frac{y + 7}{5}$
Dengan menukar variabel $y$ menjadi $x$, diperoleh $f^{-1}(x) = \frac{x + 7}{5}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b01-c-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi akar*

Diketahui fungsi $f(x) = \sqrt{x + 8}$ dengan daerah asal $x \ge -8$. Rumus fungsi invers $f^{-1}(x)$ untuk $x \ge 0$ adalah ....

- A. $x^2 - 64$  
  <sub>Salah: Mengkuadratkan nilai konstanta 8 menjadi 64.</sub>
- B. $(x - 8)^2$  
  <sub>Salah: Melakukan pengurangan sebelum pengkuadratan nilai fungsi.</sub>
- **C. $x^2 - 8$** ✅  
  <sub>Benar: Dari $y = \sqrt{x + 8}$, dikuadratkan menjadi $y^2 = x + 8$, sehingga diperoleh $x = y^2 - 8$.</sub>
- D. $x^2 + 8$  
  <sub>Salah: Salah memindahkan tanda konstanta positif ketika mengisolasi variabel $x$.</sub>

**Pembahasan:** Misalkan $y = \sqrt{x + 8}$ untuk $y \ge 0$.
Kuadratkan kedua ruas:
$y^2 = x + 8$
$x = y^2 - 8$
Substitusikan kembali variabel $x$, sehingga $f^{-1}(x) = x^2 - 8$ dengan domain $x \ge 0$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b01-c-easy-bt01-005
*variasi (konteks) | C2 | 1 langkah | jenis: invers pasangan berurutan*

Diketahui fungsi bijektif $g = \{(2, 6), (4, 8), (6, 10)\}$. Himpunan pasangan berurutan yang menyatakan fungsi invers $g^{-1}$ adalah ....

- **A. $\{(6, 2), (8, 4), (10, 6)\}$** ✅  
  <sub>Benar: Fungsi invers diperoleh dengan menukar elemen masukan dan keluaran pada setiap pasangan berurutan $(x, y)$ menjadi $(y, x)$.</sub>
- B. $\{(\frac{1}{2}, \frac{1}{6}), (\frac{1}{4}, \frac{1}{8}), (\frac{1}{6}, \frac{1}{10})\}$  
  <sub>Salah: Mengartikan invers sebagai kebalikan nilai pecahan aritmetika.</sub>
- C. $\{(-2, -6), (-4, -8), (-6, -10)\}$  
  <sub>Salah: Mengira invers berarti mengubah setiap nilai menjadi lawan negatifnya.</sub>
- D. $\{(2, -6), (4, -8), (6, -10)\}$  
  <sub>Salah: Hanya membalik tanda keluaran tanpa menukar urutan pasangan.</sub>

**Pembahasan:** Jika fungsi $g$ memetakan $x$ ke $y$ dalam bentuk pasangan berurutan $(x, y)$, maka fungsi invers $g^{-1}$ memetakan balik $y$ ke $x$, yaitu $(y, x)$. Oleh karena itu, $g^{-1} = \{(6, 2), (8, 4), (10, 6)\}$.
**Acuan:** siswa — siswa hal.57 Uji Kompetensi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b01-c-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: invers fungsi pangkat*

Rumus fungsi invers dari $f(x) = x^5$ untuk setiap bilangan real $x$ adalah ....

- **A. $f^{-1}(x) = \sqrt[5]{x}$** ✅  
  <sub>Benar: Misalkan $y = x^5$, maka $x = \sqrt[5]{y}$. Dengan mengganti variabel, diperoleh $f^{-1}(x) = \sqrt[5]{x}$.</sub>
- B. $f^{-1}(x) = 5x$  
  <sub>Salah: Siswa mengacaukan invers fungsi pangkat dengan perkalian koefisien turunan.</sub>
- C. $f^{-1}(x) = x^5$  
  <sub>Salah: Siswa mengira fungsi invers sama dengan fungsi asalnya.</sub>
- D. $f^{-1}(x) = \frac{1}{x^5}$  
  <sub>Salah: Siswa menganggap notasi invers berpangkat -1 sebagai pecahan aljabar satu per f(x).</sub>

**Pembahasan:** Langkah penyelesaian:
1. Tuliskan dalam bentuk persamaan: $y = x^5$
2. Nyatakan $x$ dalam bentuk $y$: $x = \sqrt[5]{y}$
3. Ganti $x$ dengan $f^{-1}(x)$ dan $y$ dengan $x$: $f^{-1}(x) = \sqrt[5]{x}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b01-c-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi linear negatif*

Rumus fungsi invers dari $f(x) = -4x + 7$ adalah ....

- A. $f^{-1}(x) = -4x - 7$  
  <sub>Salah: Siswa hanya membalik tanda operasi konstanta tanpa mengubah relasi perkalian x.</sub>
- **B. $f^{-1}(x) = \frac{7 - x}{4}$** ✅  
  <sub>Benar: Jika $y = -4x + 7$, maka $4x = 7 - y$, sehingga $x = \frac{7 - y}{4}$. Jadi, $f^{-1}(x) = \frac{7 - x}{4}$.</sub>
- C. $f^{-1}(x) = \frac{x - 7}{4}$  
  <sub>Salah: Siswa membalik tanda pembilang tetapi lupa membagi dengan negatif empat.</sub>
- D. $f^{-1}(x) = \frac{x + 7}{4}$  
  <sub>Salah: Siswa salah saat memindahkan tanda negatif dari variabel x.</sub>

**Pembahasan:** Misalkan $y = f(x)$:
$y = -4x + 7$
$4x = 7 - y$
$x = \frac{7 - y}{4}$

Dengan menukar variabel, diperoleh:
$f^{-1}(x) = \frac{7 - x}{4}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b01-c-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: uji keberadaan invers relasi*

Diketahui fungsi $h: \{1, 2, 3\} \to \{p, q, r\}$ dinyatakan dalam pasangan berurutan $h = \{(1, p), (2, q), (3, q)\}$. Alasan mengapa fungsi $h$ tidak memiliki fungsi invers adalah ....

- **A. fungsi $h$ tidak bersifat injektif karena terdapat dua anggota domain yang memiliki pasangan keluaran yang sama** ✅  
  <sub>Benar: Elemen 2 dan 3 keduanya dipetakan ke $q$, sehingga saat dibalik, elemen $q$ akan memiliki dua pasangan (bukan fungsi).</sub>
- B. semua anggota kodomain telah memiliki pasangan di domain  
  <sub>Salah: Siswa salah memahami konsep surjektif dan mengabaikan elemen r yang tidak berpasangan.</sub>
- C. fungsi $h$ bukan merupakan sebuah fungsi yang sah  
  <sub>Salah: Siswa mengira fungsi h sendiri bukan fungsi, padahal setiap domain memiliki tepat satu pasangan.</sub>
- D. banyaknya anggota domain tidak sama dengan banyaknya anggota kodomain  
  <sub>Salah: Siswa mengira jumlah himpunan asalnya berbeda padahal keduanya sama-sama memiliki 3 anggota.</sub>

**Pembahasan:** Suatu fungsi memiliki fungsi invers jika dan hanya jika fungsi tersebut bersifat bijektif (injektif dan surjektif).
Pada fungsi $h$, anggota domain 2 dan 3 sama-sama menghasilkan bayangan $q$. Karena ada masukan berbeda yang menghasilkan keluaran sama, fungsi $h$ tidak injektif (satu-satu). Akibatnya, relasi kebalikannya bukan merupakan fungsi.
**Acuan:** siswa — siswa hal.57 Uji Kompetensi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b01-c-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: domain dan range fungsi invers*

Suatu fungsi bijektif $f$ memiliki daerah asal (domain) $D_f = \{x \in \mathbb{R} \mid x \ge 2\}$ dan daerah hasil (range) $R_f = \{y \in \mathbb{R} \mid y \ge 0\}$. Daerah hasil (range) dari fungsi invers $f^{-1}$ adalah ....

- A. $\{y \in \mathbb{R} \mid y \le 2\}$  
  <sub>Salah: Siswa membalik tanda pertidaksamaan karena mengira invers berarti membalik arah pertidaksamaan.</sub>
- B. $\{y \in \mathbb{R} \mid y \le 0\}$  
  <sub>Salah: Siswa memakai rentang nilai range fungsi asal sekaligus membalik arah tandanya.</sub>
- C. $\{y \in \mathbb{R} \mid y \ge 0\}$  
  <sub>Salah: Siswa tertukar antara daerah asal fungsi invers dengan daerah hasil fungsi invers.</sub>
- **D. $\{y \in \mathbb{R} \mid y \ge 2\}$** ✅  
  <sub>Benar: Berdasarkan definisi fungsi invers, daerah hasil (range) dari $f^{-1}$ adalah daerah asal (domain) dari fungsi asal $f$, yaitu $y \ge 2$.</sub>

**Pembahasan:** Berdasarkan sifat fungsi invers:
- Domain $f^{-1} = \text{Range } f = \{x \in \mathbb{R} \mid x \ge 0\}$
- Range $f^{-1} = \text{Domain } f = \{y \in \mathbb{R} \mid y \ge 2\}

Oleh karena itu, daerah hasil (range) dari $f^{-1}$ adalah $\{y \in \mathbb{R} \mid y \ge 2\}$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b01-c-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: pemeriksaan fungsi invers*

Diketahui fungsi $f(x) = x + 9$. Rumus fungsi $g(x)$ yang memenuhi kondisi $(f \circ g)(x) = x$ untuk setiap bilangan real $x$ adalah ....

- A. $g(x) = \frac{x}{9}$  
  <sub>Salah: Siswa mengira invers dari penjumlahan adalah pembagian.</sub>
- B. $g(x) = x + 9$  
  <sub>Salah: Siswa mengira fungsi g sama persis dengan fungsi f.</sub>
- **C. $g(x) = x - 9$** ✅  
  <sub>Benar: Agar $(f \circ g)(x) = f(g(x)) = g(x) + 9 = x$, maka $g(x) = x - 9$.</sub>
- D. $g(x) = 9 - x$  
  <sub>Salah: Siswa tertukar urutan pengurangan antara variabel dan konstanta.</sub>

**Pembahasan:** Berdasarkan definisi:
$(f \circ g)(x) = x$
$f(g(x)) = x$
$g(x) + 9 = x$
$g(x) = x - 9$

Fungsi $g(x) = x - 9$ merupakan fungsi invers dari $f(x)$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b01-c-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi kubik*

Rumus fungsi invers dari $f(x) = x^3 - 7$ untuk setiap $x \in \mathbb{R}$ adalah ....

- A. $f^{-1}(x) = \frac{1}{x^3 - 7}$  
  <sub>Salah: Menafsirkan lambang fungsi invers sebagai pangkat negatif atau kebalikan pecahan.</sub>
- B. $f^{-1}(x) = (x + 7)^3$  
  <sub>Salah: Terbalik dalam menerapkan operasi invers, memangkatkan tiga bukannya menarik akar pangkat tiga.</sub>
- C. $f^{-1}(x) = \sqrt[3]{x - 7}$  
  <sub>Salah: Kesalahan tanda saat memindahkan konstanta ke ruas lain.</sub>
- **D. $f^{-1}(x) = \sqrt[3]{x + 7}$** ✅  
  <sub>Benar: Misalkan $y = x^3 - 7$, maka $x^3 = y + 7$, sehingga $x = \sqrt[3]{y + 7}$. Dengan demikian, diperoleh $f^{-1}(x) = \sqrt[3]{x + 7}$.</sub>

**Pembahasan:** Langkah 1: Tuliskan persamaan $y = f(x)$, yaitu $y = x^3 - 7$.
Langkah 2: Nyatakan $x$ dalam $y$:
$x^3 = y + 7$
$x = \sqrt[3]{y + 7}$
Jadi, rumus fungsi inversnya adalah $f^{-1}(x) = \sqrt[3]{x + 7}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b01-c-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi nilai invers fungsi akar*

Diketahui fungsi $f(x) = \sqrt{x - 5}$ terdefinisi untuk $x \ge 5$. Nilai dari $f^{-1}(4)$ adalah ....

- A. 11  
  <sub>Salah: Salah melakukan operasi tanda pada konstanta: 16 - 5 = 11 bukannya 16 + 5.</sub>
- B. 9  
  <sub>Salah: Lupa menguadratkan nilai masukan dan langsung menjumlahkan: 4 + 5 = 9.</sub>
- C. 13  
  <sub>Salah: Mengalikan dengan dua alih-alih menguadratkan: 4 x 2 + 5 = 13.</sub>
- **D. 21** ✅  
  <sub>Benar: Berdasarkan definisi fungsi invers, jika $f^{-1}(4) = k$, maka $f(k) = 4$. Diperoleh $\sqrt{k - 5} = 4 \implies k - 5 = 16 \implies k = 21$.</sub>

**Pembahasan:** Misalkan $f^{-1}(4) = x$, maka:
$f(x) = 4$
$\sqrt{x - 5} = 4$
Kuadratkan kedua ruas:
$x - 5 = 16$
$x = 16 + 5 = 21$
Jadi, nilai dari $f^{-1}(4) = 21$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b01-c-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi linear pecahan*

Rumus fungsi invers $f^{-1}(x)$ dari fungsi linear $f(x) = 6x + 5$ adalah ....

- A. $f^{-1}(x) = 6x - 5$  
  <sub>Salah: Hanya mengubah tanda konstanta tanpa membagi dengan koefisien x.</sub>
- B. $f^{-1}(x) = \frac{6}{x - 5}$  
  <sub>Salah: Keliru memposisikan koefisien sebagai pembilang dalam pecahan.</sub>
- C. $f^{-1}(x) = \frac{x + 5}{6}$  
  <sub>Salah: Kesalahan tanda saat memindahkan konstanta positif ke ruas kiri.</sub>
- **D. $f^{-1}(x) = \frac{x - 5}{6}$** ✅  
  <sub>Benar: Dari $y = 6x + 5$, diperoleh $6x = y - 5$, sehingga $x = \frac{y - 5}{6}$. Maka $f^{-1}(x) = \frac{x - 5}{6}$.</sub>

**Pembahasan:** Langkah 1: Misalkan $y = f(x)$:
$y = 6x + 5$
Langkah 2: Selesaikan untuk $x$:
$6x = y - 5$
$x = \frac{y - 5}{6}$
Ganti variabel $y$ dengan $x$ sehingga $f^{-1}(x) = \frac{x - 5}{6}$.
**Acuan:** siswa — siswa hal.59 Uji Kompetensi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b01-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: evaluasi invers dari pasangan nilai*

Diketahui suatu fungsi bijektif $f$ memenuhi $f(7) = 15$. Nilai dari $f^{-1}(15)$ adalah ....

- **A. 7** ✅  
  <sub>Benar: Sesuai definisi fungsi invers, jika $f(a) = b$, maka fungsi inversnya memetakan kembali nilai $b$ ke $a$, yaitu $f^{-1}(b) = a$. Karena $f(7) = 15$, maka $f^{-1}(15) = 7$.</sub>
- B. -15  
  <sub>Salah: Mengira fungsi invers bernilai lawan tanda dari keluarannya.</sub>
- C. -7  
  <sub>Salah: Mengira invers berarti membalik tanda nilai masukan menjadi negatif.</sub>
- D. $\frac{1}{15}$  
  <sub>Salah: Mengira notasi pangkat minus satu berarti kebalikan pecahan atau 1 dibagi 15.</sub>

**Pembahasan:** Fungsi invers $f^{-1}$ membalikkan arah pemetaan fungsi asal $f$. Berdasarkan definisi, $f(x) = y \iff f^{-1}(y) = x$. Karena diketahui $f(7) = 15$, maka secara langsung diperoleh $f^{-1}(15) = 7$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b01-c-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: identifikasi fungsi yang memiliki invers*

Di antara fungsi-fungsi berikut yang terdefinisi pada daerah asal seluruh bilangan real $\mathbb{R}$, manakah fungsi yang memiliki fungsi invers?

- **A. $f(x) = 4x - 9$** ✅  
  <sub>Benar: Fungsi linear $f(x) = 4x - 9$ dengan koefisien $x \ne 0$ bersifat satu-satu (injektif) dan daerah hasilnya mencakup seluruh bilangan real (surjektif), sehingga bersifat bijektif dan memiliki invers.</sub>
- B. $k(x) = 8$  
  <sub>Salah: Keliru menganggap fungsi konstan memiliki invers, padahal semua masukan memetakan ke keluaran yang sama sehingga tidak injektif.</sub>
- C. $g(x) = x^2 + 1$  
  <sub>Salah: Keliru menganggap fungsi kuadrat memiliki invers pada seluruh bilangan real, padahal tidak injektif karena $g(-1) = g(1) = 2$.</sub>
- D. $h(x) = |x|$  
  <sub>Salah: Keliru menganggap fungsi nilai mutlak memiliki invers pada seluruh bilangan real, padahal tidak injektif karena $h(-2) = h(2) = 2$.</sub>

**Pembahasan:** Syarat mutlak agar suatu fungsi memiliki fungsi invers adalah fungsi tersebut harus bersifat bijektif (injektif dan surjektif). Pada domain seluruh bilangan real $\mathbb{R}$:
- $f(x) = 4x - 9$ adalah fungsi linear tak-konstan yang selalu injektif dan surjektif (bijektif), sehingga memiliki fungsi invers.
- $g(x) = x^2 + 1$ tidak injektif (bukan bijektif).
- $h(x) = |x|$ tidak injektif (bukan bijektif).
- $k(x) = 8$ tidak injektif (bukan bijektif).
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b01-c-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: komposisi fungsi saling invers*

Diketahui $f(x) = 5x - 4$ dan $g(x) = \frac{x + 4}{5}$ untuk setiap bilangan real $x$. Rumus komposisi fungsi $(g \circ f)(x)$ adalah ....

- A. $5x$  
  <sub>Salah: Siswa lupa membagi dengan 5 pada penyebut setelah menjumlahkan pembilang.</sub>
- **B. $x$** ✅  
  <sub>Benar: $(g \circ f)(x) = g(f(x)) = \frac{(5x - 4) + 4}{5} = \frac{5x}{5} = x$.</sub>
- C. $x - 4$  
  <sub>Salah: Siswa hanya memasukkan suku konstan tanpa membagi koefisien dengan benar.</sub>
- D. $1$  
  <sub>Salah: Siswa salah mengira variabel $x$ saling menghilangkan menjadi bernilai 1.</sub>

**Pembahasan:** Hitung $(g \circ f)(x) = g(5x - 4) = \frac{(5x - 4) + 4}{5} = \frac{5x}{5} = x$. Kedua fungsi merupakan fungsi yang saling invers.
**Acuan:** siswa — siswa hal.59 Uji Kompetensi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b01-c-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: invers fungsi bentuk akar linier*

Diketahui fungsi $g(x) = \sqrt{4x - 7}$ terdefinisi untuk $x \ge \frac{7}{4}$. Rumus fungsi invers $g^{-1}(x)$ untuk $x \ge 0$ adalah ....

- A. $g^{-1}(x) = \frac{(x + 7)^2}{4}$  
  <sub>Salah: Siswa menjumlahkan 7 terlebih dahulu sebelum melakukan kuadrat.</sub>
- B. $g^{-1}(x) = 4x^2 + 7$  
  <sub>Salah: Siswa mengalikan dengan 4 bukan membagi koefisien $x$.</sub>
- **C. $g^{-1}(x) = \frac{x^2 + 7}{4}$** ✅  
  <sub>Benar: Misalkan $y = \sqrt{4x - 7} \Rightarrow y^2 = 4x - 7 \Rightarrow 4x = y^2 + 7 \Rightarrow x = \frac{y^2 + 7}{4}$.</sub>
- D. $g^{-1}(x) = \frac{x^2 - 7}{4}$  
  <sub>Salah: Siswa salah memindahkan tanda negatif saat mengisolasi variabel.</sub>

**Pembahasan:** Langkah 1: Tulis $y = \sqrt{4x - 7}$. Kuadratkan kedua sisi: $y^2 = 4x - 7$.
Langkah 2: Selesaikan untuk $x$: $4x = y^2 + 7 \Rightarrow x = \frac{y^2 + 7}{4}$. Diperoleh $g^{-1}(x) = \frac{x^2 + 7}{4}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b01-c-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: definisi hubungan dua fungsi invers*

Diketahui dua buah fungsi $f$ dan $g$ terdefinisi pada bilangan real. Jika berlaku $(f \circ g)(x) = x$ dan $(g \circ f)(x) = x$ untuk setiap nilai $x$, maka hubungan yang benar antara fungsi $f$ dan $g$ adalah ....

- A. Fungsi $g$ adalah lawan negatif dari fungsi $f$  
  <sub>Salah: Siswa mengira invers sama dengan invers aditif (negatif fungsi).</sub>
- **B. Fungsi $g$ adalah invers dari fungsi $f$** ✅  
  <sub>Benar: Sesuai definisi pada buku teks, jika komposisi timbal balik menghasilkan fungsi identitas $x$, maka kedua fungsi saling invers.</sub>
- C. Fungsi $g$ merupakan fungsi kuadrat dari $f$  
  <sub>Salah: Siswa menebak hubungan aljabar yang tidak berdasar definisi.</sub>
- D. Fungsi $g$ adalah turunan dari fungsi $f$  
  <sub>Salah: Siswa tertukar konsep invers dengan materi kalkulus turunan.</sub>

**Pembahasan:** Berdasarkan definisi fungsi invers: Jika $(f \circ g)(x) = x$ dan $(g \circ f)(x) = x$, maka $g$ merupakan fungsi invers dari $f$ (ditulis $g = f^{-1}$) dan sebaliknya.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b01-c-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: pemetaan domain kodomain invers*

Jika suatu fungsi bijektif $f$ memetakan himpunan $A$ ke himpunan $B$ ($f: A \to B$), maka fungsi invers $f^{-1}$ memetakan ....

- A. Himpunan $A$ ke himpunan $A$  
  <sub>Salah: Siswa mengira fungsi invers memetakan elemen ke himpunannya sendiri.</sub>
- B. Himpunan $B$ ke himpunan $B$  
  <sub>Salah: Siswa mengira pemetaan terjadi di dalam himpunan target saja.</sub>
- **C. Himpunan $B$ ke himpunan $A$** ✅  
  <sub>Benar: Fungsi invers membalik arah relasi pemetaan dari daerah hasil/kodomain kembali ke daerah asal.</sub>
- D. Himpunan $A$ ke himpunan $B$  
  <sub>Salah: Siswa mengira fungsi invers memiliki arah pemetaan yang sama dengan fungsi asal.</sub>

**Pembahasan:** Secara definisi, fungsi invers $f^{-1}$ membalik arah relasi fungsi asal. Jika $f: A \to B$, maka $f^{-1}: B \to A$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b01-c-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: masalah kontekstual fungsi invers*

Harga suatu pakaian setelah mendapatkan diskon 30% dan kemudian diberikan potongan harga Rp25.000,00 adalah Rp80.000,00. Berapa harga awal pakaian tersebut?

- A. Rp136.500,00  
  <sub>Salah: Siswa mengalikan Rp105.000,00 dengan 1,30 alih-alih membaginya dengan 0,70.</sub>
- B. Rp175.000,00  
  <sub>Salah: Siswa salah menghitung persentase sisa bayar menjadi 60% (105.000 / 0,6).</sub>
- **C. Rp150.000,00** ✅  
  <sub>Benar: Harga sebelum potongan langsung adalah Rp80.000,00 + Rp25.000,00 = Rp105.000,00. Karena mendapat diskon 30%, nilai ini adalah 70% dari harga awal, sehingga harga awal adalah Rp105.000,00 / 0,7 = Rp150.000,00.</sub>
- D. Rp121.428,00  
  <sub>Salah: Siswa langsung membagi harga akhir Rp80.000,00 dengan 0,70 baru menambahkan Rp25.000,00.</sub>

**Pembahasan:** Misalkan harga awal adalah $x$.
1. Setelah diskon 30%, harga menjadi $(1 - 0{,}30)x = 0{,}70x$.
2. Setelah potongan harga Rp25.000,00, harga menjadi $0{,}70x - 25.000 = 80.000$.

Selesaikan persamaan:
$$0{,}70x = 80.000 + 25.000$$
$$0{,}70x = 105.000$$
$$x = \frac{105.000}{0{,}70} = 150.000$$

Jadi, harga awal pakaian tersebut adalah Rp150.000,00.
**Acuan:** siswa — siswa hal.51 Eksplorasi 1.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b01-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: aljabar komposisi dan invers*

Diketahui fungsi $f(x) = 3x + b$ dengan $(f \circ f)(x) = 9x + 20$. Rumus fungsi invers $f^{-1}(x)$ adalah ....

- **A. $\frac{x - 5}{3}$** ✅  
  <sub>Benar: $(f \circ f)(x) = 3(3x + b) + b = 9x + 4b$. Karena $(f \circ f)(x) = 9x + 20$, diperoleh $4b = 20 \implies b = 5$. Maka $f(x) = 3x + 5$. Dengan memisalkan $y = 3x + 5$, diperoleh $x = \frac{y - 5}{3}$, sehingga $f^{-1}(x) = \frac{x - 5}{3}$.</sub>
- B. $\frac{x + 5}{3}$  
  <sub>Salah: Siswa salah mengubah tanda ketika memindahkan konstanta saat mencari fungsi invers.</sub>
- C. $\frac{x - 20}{3}$  
  <sub>Salah: Siswa langsung menggunakan nilai konstanta hasil komposisi 20 tanpa membaginya dengan 4 untuk mencari nilai b.</sub>
- D. $\frac{x - 5}{9}$  
  <sub>Salah: Siswa keliru membagi dengan koefisien hasil komposisi 9 alih-alih koefisien fungsi asal 3.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus $(f \circ f)(x)$:
$(f \circ f)(x) = f(f(x)) = 3(3x + b) + b = 9x + 4b$.

Langkah 2: Menyamakan dengan fungsi komposisi yang diketahui:
$9x + 4b = 9x + 20$
$4b = 20 \implies b = 5$.
Diperoleh rumus fungsi $f(x) = 3x + 5$.

Langkah 3: Menentukan rumus fungsi invers $f^{-1}(x)$:
$y = 3x + 5$
$3x = y - 5$
$x = \frac{y - 5}{3}$
Jadi, $f^{-1}(x) = \frac{x - 5}{3}$.
**Acuan:** pretest — kelas11-b01-p0056-latihan-15-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b01-c-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: domain fungsi invers*

Diketahui fungsi $f(x) = \sqrt{2x - 10} + 4$ yang terdefinisi untuk $x \ge 5$. Daerah asal (domain) dari fungsi invers $f^{-1}(x)$ adalah ....

- **A. $\{x \in \mathbb{R} \mid x \ge 4\}$** ✅  
  <sub>Benar: Domain fungsi invers $f^{-1}$ sama dengan range dari fungsi asal $f$. Karena untuk $x \ge 5$ nilai $\sqrt{2x - 10} \ge 0$, maka nilai $f(x) \ge 0 + 4 = 4$. Daerah hasil fungsi $f$ adalah $R_f = \{y \in \mathbb{R} \mid y \ge 4\}$, sehingga $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \ge 4\}$.</sub>
- B. $\{x \in \mathbb{R} \mid x \ge 10\}$  
  <sub>Salah: Siswa salah menentukan nilai batas bawah akar dengan mengambil angka 10 langsung.</sub>
- C. $\{x \in \mathbb{R} \mid x \ge 5\}$  
  <sub>Salah: Siswa mengira daerah asal fungsi invers sama persis dengan daerah asal fungsi asal f.</sub>
- D. $\{x \in \mathbb{R} \mid x \ge 0\}$  
  <sub>Salah: Siswa hanya menggunakan syarat non-negatif bentuk akar tanpa memperhitungkan penjumlahan konstanta 4.</sub>

**Pembahasan:** Langkah 1: Menentukan daerah hasil (range) fungsi asal $f(x)$:
Bentuk akar memiliki nilai non-negatif untuk seluruh daerah asalnya:
$\sqrt{2x - 10} \ge 0$ untuk setiap $x \ge 5$.

Langkah 2: Menentukan batas nilai $f(x)$:
$f(x) = \sqrt{2x - 10} + 4 \ge 0 + 4 = 4$.
Maka daerah hasil fungsi $f$ adalah $R_f = \{y \in \mathbb{R} \mid y \ge 4\}$.

Langkah 3: Menentukan domain fungsi invers:
Berdasarkan sifat fungsi invers, daerah asal fungsi invers sama dengan daerah hasil fungsi asal:
$D_{f^{-1}} = R_f = \{x \in \mathbb{R} \mid x \ge 4\}$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b01-c-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: fungsi invers pecahan linear*

Diketahui fungsi rasional $f(x) = \frac{2x + 5}{3x - 4}$ dengan $x \ne \frac{4}{3}$. Rumus untuk fungsi invers $f^{-1}(x)$ adalah ....

- A. $\frac{-4x + 5}{3x + 2}$  
  <sub>Salah: Siswa keliru memproses tanda negatif pada pemfaktoran variabel x.</sub>
- B. $\frac{4x - 5}{3x - 2}$  
  <sub>Salah: Siswa salah mengubah tanda konstanta 5 saat memindah ruas ke sisi kanan.</sub>
- **C. $\frac{4x + 5}{3x - 2}$** ✅  
  <sub>Benar: Misalkan $y = \frac{2x + 5}{3x - 4}$. Kalikan silang: $y(3x - 4) = 2x + 5 \iff 3xy - 4y = 2x + 5$. Kumpulkan suku berpeubah $x$: $3xy - 2x = 4y + 5 \iff x(3y - 2) = 4y + 5 \iff x = \frac{4y + 5}{3y - 2}$. Jadi, $f^{-1}(x) = \frac{4x + 5}{3x - 2}$.</sub>
- D. $\frac{3x - 4}{2x + 5}$  
  <sub>Salah: Siswa secara keliru hanya menukar posisi pembilang dan penyebut fungsi asal.</sub>

**Pembahasan:** Langkah 1: Tulis persamaan dalam bentuk $y = f(x)$ dan kalikan penyebut ke ruas kiri:
$y = \frac{2x + 5}{3x - 4}$
$y(3x - 4) = 2x + 5$
$3xy - 4y = 2x + 5$

Langkah 2: Kumpulkan semua suku yang memuat peubah $x$ ke salah satu ruas:
$3xy - 2x = 4y + 5$
$x(3y - 2) = 4y + 5$

Langkah 3: Nyatakan $x$ dalam $y$ lalu ganti peubah ke rumus $f^{-1}(x)$:
$x = \frac{4y + 5}{3y - 2}$
Jadi, rumus fungsi inversnya adalah $f^{-1}(x) = \frac{4x + 5}{3x - 2}$ untuk $x \ne \frac{2}{3}$.
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b01-c-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: evaluasi invers fungsi komposisi*

Diketahui fungsi $f(x) = 2x - 3$ dan $g(x) = \frac{x + 1}{4}$. Jika $h(x) = (f \circ g)(x)$, maka nilai dari $h^{-1}(5)$ adalah ....

- A. 10  
  <sub>Salah: Siswa mengalikan nilai 5 dengan 2 namun lupa menambahkan 5 pada langkah akhir.</sub>
- **B. 15** ✅  
  <sub>Benar: $h(x) = f(g(x)) = 2\left(\frac{x + 1}{4}\right) - 3 = \frac{x + 1}{2} - 3 = \frac{x - 5}{2}$. Untuk mencari $h^{-1}(5)$, selesaikan $h(x) = 5 \implies \frac{x - 5}{2} = 5 \implies x - 5 = 10 \implies x = 15$.</sub>
- C. 25  
  <sub>Salah: Siswa salah tanda saat menyamakan penyebut sehingga menghitung x - 15 = 10.</sub>
- D. 5  
  <sub>Salah: Siswa salah mengira bahwa invers memetakan nilai masukan yang sama.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus fungsi komposisi $h(x) = (f \circ g)(x)$:
$h(x) = f(g(x)) = 2\left(\frac{x + 1}{4}\right) - 3$
$h(x) = \frac{x + 1}{2} - 3 = \frac{x + 1 - 6}{2} = \frac{x - 5}{2}$

Langkah 2: Menggunakan definisi nilai invers $h^{-1}(5) = k \iff h(k) = 5$:
$\frac{k - 5}{2} = 5$

Langkah 3: Menyelesaikan persamaan untuk nilai $k$:
$k - 5 = 10$
$k = 15$
Jadi, nilai $h^{-1}(5) = 15$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b01-c-medium-bt01-005
*orisinal | C4 | 3 langkah | jenis: invers fungsi kuadrat terbatas*

Fungsi kuadrat $f(x) = x^2 - 6x + 14$ dibatasi pada domain $D_f = \{x \in \mathbb{R} \mid x \ge 3\}$ agar memiliki fungsi invers. Rumus fungsi invers $f^{-1}(x)$ untuk $x \ge 5$ adalah ....

- A. $-3 + \sqrt{x - 5}$  
  <sub>Salah: Siswa salah menentukan tanda pergeseran sumbu simetri saat memindahkan nilai 3 ke ruas lain.</sub>
- B. $3 - \sqrt{x - 5}$  
  <sub>Salah: Siswa memilih cabang akar negatif yang berkorespondensi dengan daerah asal x <= 3.</sub>
- **C. $3 + \sqrt{x - 5}$** ✅  
  <sub>Benar: Ubah $y = x^2 - 6x + 14$ ke bentuk kuadrat sempurna: $y = (x - 3)^2 + 5 \iff (x - 3)^2 = y - 5$. Karena $x \ge 3$, maka $x - 3 \ge 0$, sehingga $x - 3 = +\sqrt{y - 5} \iff x = 3 + \sqrt{y - 5}$. Jadi, $f^{-1}(x) = 3 + \sqrt{x - 5}$.</sub>
- D. $3 + \sqrt{x + 5}$  
  <sub>Salah: Siswa keliru memindahkan konstanta 5 sehingga bertanda positif di dalam akar.</sub>

**Pembahasan:** Langkah 1: Mengubah persamaan fungsi ke bentuk kuadrat sempurna:
$y = x^2 - 6x + 14$
$y = (x^2 - 6x + 9) + 5$
$y = (x - 3)^2 + 5$

Langkah 2: Mengisolasi variabel $x$:
$(x - 3)^2 = y - 5$
Karena daerah asal dibatasi $x \ge 3$, maka nilai $(x - 3) \ge 0$, sehingga diambil tanda positif pada akar kuadrat:
$x - 3 = \sqrt{y - 5}$
$x = 3 + \sqrt{y - 5}$

Langkah 3: Menuliskan rumus fungsi invers:
$f^{-1}(x) = 3 + \sqrt{x - 5}$ untuk $x \ge 5$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b01-c-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: aljabar nilai fungsi invers*

Diketahui fungsi linear $f(x) = 5x + b$ memenuhi $(f \circ f)(x) = 25x + 36$. Nilai dari $b + f^{-1}(11)$ adalah ....

- A. 8  
  <sub>Salah: Siswa lupa membagi nilai (11 - 6) dengan koefisien 5 sehingga menganggap f^-1(11) = 5 - 3 = 2, sehingga 6 + 2 = 8.</sub>
- B. 5  
  <sub>Salah: Siswa salah mengoperasikan invers sebagai f(11) = 5(11)+6 = 61 lalu salah menghitung pembagian, atau salah menghitung 6 - 1 = 5.</sub>
- C. 12  
  <sub>Salah: Siswa langsung menyamakan konstanta b = 36 tanpa memperhitungkan komposisi 6b = 36.</sub>
- **D. 7** ✅  
  <sub>Benar: $(f \circ f)(x) = 5(5x + b) + b = 25x + 6b$. Karena $25x + 6b = 25x + 36$, diperoleh $6b = 36 \implies b = 6$. Rumus fungsi $f(x) = 5x + 6$. Inversnya adalah $f^{-1}(x) = \frac{x - 6}{5}$. Maka $f^{-1}(11) = \frac{11 - 6}{5} = 1$. Nilai $b + f^{-1}(11) = 6 + 1 = 7$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $b$.
$(f \circ f)(x) = f(5x + b) = 5(5x + b) + b = 25x + 6b$.
Diketahui $(f \circ f)(x) = 25x + 36$, maka:
$6b = 36 \implies b = 6$.

Langkah 2: Menentukan $f^{-1}(11)$.
$f(x) = 5x + 6$.
Misalkan $y = 5x + 6 \implies 5x = y - 6 \implies x = \frac{y - 6}{5}$.
Sehingga $f^{-1}(x) = \frac{x - 6}{5}$.
Untuk $x = 11$:
$f^{-1}(11) = \frac{11 - 6}{5} = \frac{5}{5} = 1$.

Langkah 3: Menghitung nilai yang ditanyakan.
$b + f^{-1}(11) = 6 + 1 = 7$.
**Acuan:** pretest — kelas11-b01-p0056-latihan-15-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b01-c-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: fungsi invers akar dan domain*

Diketahui fungsi $f(x) = \sqrt{3x - 12}$ terdefinisi pada daerah asal $D_f = \{x \in \mathbb{R} \mid x \ge 4\}$. Rumus fungsi invers $f^{-1}(x)$ beserta daerah asalnya adalah ....

- A. $f^{-1}(x) = \frac{(x + 12)^2}{3}$ dengan domain $\{x \in \mathbb{R} \mid x \ge 0\}$  
  <sub>Salah: Siswa menjumlahkan 12 terlebih dahulu sebelum menguadratkan variabel x.</sub>
- B. $f^{-1}(x) = \frac{x^2 + 12}{3}$ dengan domain $\{x \in \mathbb{R} \mid x \ge 4\}$  
  <sub>Salah: Siswa keliru menggunakan domain fungsi asal sebagai domain fungsi invers bukannya range fungsi asal.</sub>
- **C. $f^{-1}(x) = \frac{x^2 + 12}{3}$ dengan domain $\{x \in \mathbb{R} \mid x \ge 0\}$** ✅  
  <sub>Benar: Misal $y = \sqrt{3x - 12}$ dengan $y \ge 0$. Kuadratkan kedua ruas: $y^2 = 3x - 12 \implies 3x = y^2 + 12 \implies x = \frac{y^2 + 12}{3}$. Jadi $f^{-1}(x) = \frac{x^2 + 12}{3}$. Domain $f^{-1}$ adalah range dari $f$, yaitu $x \ge 0$.</sub>
- D. $f^{-1}(x) = \frac{x^2 - 12}{3}$ dengan domain $\{x \in \mathbb{R} \mid x \ge 0\}$  
  <sub>Salah: Siswa salah tanda saat memindahkan suku -12 ke ruas lain.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus $f^{-1}(x)$.
$y = \sqrt{3x - 12}$
Karena fungsi akar menghasilkan nilai non-negatif, maka $y \ge 0$.
Kuadratkan kedua ruas:
$y^2 = 3x - 12$
$3x = y^2 + 12$
$x = \frac{y^2 + 12}{3}$
Sehingga diperoleh $f^{-1}(x) = \frac{x^2 + 12}{3}$.

Langkah 2: Menentukan domain $f^{-1}(x)$.
Domain dari $f^{-1}$ bersesuaian dengan daerah hasil (range) fungsi asal $f(x)$. Karena $f(x) = \sqrt{3x - 12} \ge 0$, maka daerah asalnya adalah $\{x \in \mathbb{R} \mid x \ge 0\}$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b01-c-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: persamaan fungsi invers bentuk akar*

Diberikan fungsi $g(x) = \sqrt{4x + 7}$ yang terdefinisi untuk $x \ge -\frac{7}{4}$. Persamaan matematis untuk fungsi invers $g^{-1}(x)$ adalah ....

- **A. $g^{-1}(x) = \frac{x^2 - 7}{4}$ untuk $x \ge 0$** ✅  
  <sub>Benar: Misal $y = \sqrt{4x + 7}$ dengan $y \ge 0$. Kuadratkan: $y^2 = 4x + 7 \implies 4x = y^2 - 7 \implies x = \frac{y^2 - 7}{4}$. Maka $g^{-1}(x) = \frac{x^2 - 7}{4}$ untuk $x \ge 0$.</sub>
- B. $g^{-1}(x) = \frac{x^2 - 7}{4}$ untuk $x \ge -\frac{7}{4}$  
  <sub>Salah: Siswa salah menetapkan domain invers dengan menggunakan batas domain fungsi asal.</sub>
- C. $g^{-1}(x) = 4x^2 - 7$ untuk $x \ge 0$  
  <sub>Salah: Siswa lupa membagi dengan koefisien x yaitu 4.</sub>
- D. $g^{-1}(x) = \frac{x^2 + 7}{4}$ untuk $x \ge 0$  
  <sub>Salah: Siswa salah saat memindahkan konstanta 7 positif ke ruas lain menjadi tetap positif.</sub>

**Pembahasan:** Langkah 1: Menyatakan variabel $x$ dalam $y$.
$y = \sqrt{4x + 7}$, dengan syarat nilai akar $y \ge 0$.
Kuadratkan kedua ruas:
$y^2 = 4x + 7$
$4x = y^2 - 7$
$x = \frac{y^2 - 7}{4}$

Langkah 2: Menuliskan rumus fungsi invers beserta daerah asalnya.
Ganti variabel $x$ menjadi $g^{-1}(x)$ dan $y$ menjadi $x$:
$g^{-1}(x) = \frac{x^2 - 7}{4}$ dengan syarat $x \ge 0$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b01-c-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: parameter invers melalui identitas komposisi*

Diketahui dua fungsi linear $f(x) = \frac{2x - 7}{3}$ dan $g(x) = \frac{3x + k}{2}$. Jika $g(x)$ merupakan fungsi invers dari $f(x)$, maka nilai konstanta $k$ adalah ....

- A. -7  
  <sub>Salah: Siswa salah tanda saat memindahkan suku -7 ke sisi berlawanan.</sub>
- B. 14  
  <sub>Salah: Siswa mengalikan konstanta dengan faktor 2 secara keliru saat menyamakan bentuk.</sub>
- **C. 7** ✅  
  <sub>Benar: Jika g adalah invers dari f, maka f^-1(x) = g(x). Dari y = (2x - 7)/3 diperoleh 3y = 2x - 7 sehingga 2x = 3y + 7 atau x = (3y + 7)/2. Jadi f^-1(x) = (3x + 7)/2. Menyamakan dengan g(x) = (3x + k)/2 menghasilkan k = 7.</sub>
- D. 3  
  <sub>Salah: Siswa keliru menyamakan nilai k dengan penyebut dari fungsi f(x).</sub>

**Pembahasan:** Langkah 1: Menentukan invers dari $f(x)$.
Misalkan $y = \frac{2x - 7}{3}$.
$3y = 2x - 7$
$2x = 3y + 7$
$x = \frac{3y + 7}{2}$
Maka $f^{-1}(x) = \frac{3x + 7}{2}$.

Langkah 2: Membandingkan dengan $g(x)$.
Diketahui bahwa $g(x)$ adalah fungsi invers dari $f(x)$, sehingga:
$g(x) = f^{-1}(x)$
$\frac{3x + k}{2} = \frac{3x + 7}{2}$

Langkah 3: Menentukan nilai $k$.
Dengan menyamakan pembilang, diperoleh $k = 7$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b01-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: pemecahan masalah invers kontekstual*

Sebuah toko elektronik memberikan promo akhir tahun berupa diskon harga sebesar 20%, kemudian dilanjutkan dengan potongan voucer belanja sebesar Rp50.000,00. Jika seorang pembeli membayar sebesar Rp350.000,00 di kasir, harga barang mula-mula sebelum dikenai promo adalah ....

- A. Rp480.000,00  
  <sub>Salah: Siswa mengurangkan voucer terlebih dahulu kemudian mengalikan dengan 1,2 (350.000 + 50.000 = 400.000 lalu 400.000 * 1,2 = 480.000).</sub>
- **B. Rp500.000,00** ✅  
  <sub>Benar: Misal harga awal x. Diskon 20% membuat harga menjadi 0,8x. Potongan voucer Rp50.000 membuat harga akhir y = 0,8x - 50.000. Dengan operasi invers: x = (y + 50.000)/0,8. Untuk y = 350.000, diperoleh x = (350.000 + 50.000)/0,8 = 400.000 / 0,8 = 500.000.</sub>
- C. Rp425.000,00  
  <sub>Salah: Siswa membagi 350.000 dengan 0,8 terlebih dahulu baru ditambah potongan Rp50.000,00.</sub>
- D. Rp450.000,00  
  <sub>Salah: Siswa menghitung diskon 20% langsung dari 400.000 lalu menambahkannya (400.000 + 80.000 = 480.000 atau salah hitung 350.000 + 100.000).</sub>

**Pembahasan:** Langkah 1: Membuat model matematis proses pemberian harga.
Misalkan harga awal barang adalah $x$.
Setelah diskon 20%, harga menjadi: $f(x) = (1 - 0{,}20)x = 0{,}8x$.
Setelah potongan voucer Rp50.000,00, harga akhir adalah:
$y = g(f(x)) = 0{,}8x - 50.000$.

Langkah 2: Menentukan fungsi invers untuk mencari harga asal dari harga akhir.
$y = 0{,}8x - 50.000$
$0{,}8x = y + 50.000$
$x = \frac{y + 50.000}{0{,}8}$

Langkah 3: Menghitung harga awal untuk $y = 350.000$.
$x = \frac{350.000 + 50.000}{0{,}8} = \frac{400.000}{0{,}8} = 500.000$.
Jadi, harga barang mula-mula adalah Rp500.000,00.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b01-c-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: invers fungsi linear pecahan*

Diketahui fungsi linear $f(x) = -\frac{2}{5}x + 4$ terdefinisi untuk setiap bilangan real $x$. Rumus fungsi invers $f^{-1}(x)$ adalah ....

- A. $f^{-1}(x) = -\frac{5}{2}x + 4$  
  <sub>Salah: Siswa hanya membalik koefisien $x$ menjadi bentuk kebalikannya tanpa mengalikan konstanta dengan faktor skala.</sub>
- **B. $f^{-1}(x) = -\frac{5}{2}x + 10$** ✅  
  <sub>Benar: Memisalkan $y = -\frac{2}{5}x + 4$, maka $\frac{2}{5}x = 4 - y \iff x = \frac{5}{2}(4 - y) = 10 - \frac{5}{2}y$, sehingga diperoleh $f^{-1}(x) = -\frac{5}{2}x + 10$.</sub>
- C. $f^{-1}(x) = \frac{5}{2}x - 10$  
  <sub>Salah: Siswa keliru memindahkan tanda negatif saat mengalikan silang pecahan.</sub>
- D. $f^{-1}(x) = -\frac{2}{5}x - 10$  
  <sub>Salah: Siswa tidak membalik kemiringan garis (gradien) dan hanya mengubah tanda konstanta.</sub>

**Pembahasan:** Langkah 1: Nyatakan fungsi ke dalam variabel $y$:
$$y = -\frac{2}{5}x + 4$$

Langkah 2: Selesaikan persamaan untuk $x$:
$$\frac{2}{5}x = 4 - y$$
$$x = \frac{5}{2}(4 - y)$$
$$x = 10 - \frac{5}{2}y$$

Langkah 3: Ganti $x$ dengan $f^{-1}(x)$ dan $y$ dengan $x$:
$$f^{-1}(x) = -\frac{5}{2}x + 10$$
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b01-c-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: invers fungsi kubik*

Diketahui fungsi bijektif $f(x) = (2x - 5)^3$ yang terdefinisi untuk seluruh bilangan real $x$. Rumus fungsi invers $f^{-1}(x)$ adalah ....

- **A. $f^{-1}(x) = \frac{\sqrt[3]{x} + 5}{2}$** ✅  
  <sub>Benar: Dengan memisalkan $y = (2x - 5)^3$, kedua ruas ditarik akar pangkat tiga menghasilkan $\sqrt[3]{y} = 2x - 5$, sehingga $2x = \sqrt[3]{y} + 5$ atau $x = \frac{\sqrt[3]{y} + 5}{2}$.</sub>
- B. $f^{-1}(x) = 2\sqrt[3]{x} + 5$  
  <sub>Salah: Siswa mengalikan dengan koefisien alih-alih membaginya saat menyelesaikan nilai $x$.</sub>
- C. $f^{-1}(x) = \sqrt[3]{\frac{x + 5}{2}}$  
  <sub>Salah: Siswa melakukan operasi penjumlahan dan pembagian sebelum menarik akar pangkat tiga.</sub>
- D. $f^{-1}(x) = \frac{\sqrt[3]{x} - 5}{2}$  
  <sub>Salah: Siswa salah memindahkan tanda negatif dari $-5$ saat mengisolasi variabel $x$.</sub>

**Pembahasan:** Langkah 1: Nyatakan fungsi dalam $y$:
$$y = (2x - 5)^3$$

Langkah 2: Tarik akar pangkat tiga pada kedua ruas:
$$\sqrt[3]{y} = 2x - 5$$

Langkah 3: Isolasi variabel $x$:
$$2x = \sqrt[3]{y} + 5$$
$$x = \frac{\sqrt[3]{y} + 5}{2}$$

Maka fungsi inversnya adalah:
$$f^{-1}(x) = \frac{\sqrt[3]{x} + 5}{2}$$
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b01-c-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: analisis parameter fungsi invers pecahan*

Diketahui fungsi rasional $f(x) = \frac{ax + 7}{3x - 4}$ dengan $x \ne \frac{4}{3}$ dan $a$ suatu konstanta real. Jika fungsi invers dari $f(x)$ sama dengan fungsi asalnya sendiri, yaitu $f^{-1}(x) = f(x)$, maka nilai konstanta $a$ adalah ....

- A. 7  
  <sub>Salah: Siswa menyamakan nilai parameter $a$ dengan konstanta pembilang.</sub>
- B. 3  
  <sub>Salah: Siswa keliru menyamakan nilai parameter $a$ dengan koefisien $x$ pada penyebut.</sub>
- C. -4  
  <sub>Salah: Siswa mengira nilai $a$ harus sama dengan konstanta penyebut tanpa memperhatikan perubahan tanda invers.</sub>
- **D. 4** ✅  
  <sub>Benar: Invers dari $f(x) = \frac{ax+b}{cx+d}$ adalah $f^{-1}(x) = \frac{-dx+b}{cx-a}$. Karena $f^{-1}(x) = f(x)$, maka $-d = a$, sehingga $-(-4) = a \implies a = 4$.</sub>

**Pembahasan:** Langkah 1: Tentukan rumus invers $f^{-1}(x)$ secara aljabar:
$$y = \frac{ax + 7}{3x - 4}$$
$$y(3x - 4) = ax + 7$$
$$3xy - 4y = ax + 7$$
$$3xy - ax = 4y + 7$$
$$x(3y - a) = 4y + 7$$
$$x = \frac{4y + 7}{3y - a}$$

Diperoleh:
$$f^{-1}(x) = \frac{4x + 7}{3x - a}$$

Langkah 2: Samakan $f^{-1}(x)$ dengan $f(x)$:
$$\frac{4x + 7}{3x - a} = \frac{ax + 7}{3x - 4}$$

Langkah 3: Bandingkan koefisien pembilang dan penyebut yang bersesuaian:
Dari pembilang: $4x = ax \implies a = 4$.
Dari penyebut: $-a = -4 \implies a = 4$.

Jadi, nilai konstanta $a$ adalah 4.
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b01-c-medium-bt01-014
*orisinal | C3 | 2 langkah | jenis: invers komposisi dua fungsi*

Diketahui fungsi $f(x) = 3x - 2$ dan $g(x) = 2x + 5$. Rumus fungsi invers dari komposisi $(g \circ f)(x)$, yaitu $(g \circ f)^{-1}(x)$, adalah ....

- A. $\frac{x + 13}{6}$  
  <sub>Salah: Siswa salah menghitung urutan komposisi sekaligus melakukan kesalahan tanda saat menginverskan.</sub>
- B. $\frac{x + 1}{6}$  
  <sub>Salah: Siswa melakukan kesalahan tanda saat memindahkan konstanta 1 pada proses invers.</sub>
- C. $\frac{x - 13}{6}$  
  <sub>Salah: Siswa tertukar menghitung invers dari $(f \circ g)(x) = 3(2x + 5) - 2 = 6x + 13$ alih-alih $(g \circ f)(x)$.</sub>
- **D. $\frac{x - 1}{6}$** ✅  
  <sub>Benar: Komposisi $(g \circ f)(x) = 2(3x - 2) + 5 = 6x + 1$. Invers dari $y = 6x + 1$ adalah $x = \frac{y - 1}{6}$, sehingga $(g \circ f)^{-1}(x) = \frac{x - 1}{6}$.</sub>

**Pembahasan:** Langkah 1: Cari fungsi komposisi $(g \circ f)(x)$:
$$(g \circ f)(x) = g(f(x)) = 2(3x - 2) + 5 = 6x - 4 + 5 = 6x + 1$$

Langkah 2: Tentukan rumus fungsi invers dari $(g \circ f)(x)$:
$$y = 6x + 1$$
$$6x = y - 1$$
$$x = \frac{y - 1}{6}$$

Dengan demikian:
$$(g \circ f)^{-1}(x) = \frac{x - 1}{6}$$
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b01-c-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: konstruksi fungsi dari nilai invers*

Diketahui $f(x) = ax + b$ adalah suatu fungsi linear. Jika diketahui nilai $f^{-1}(4) = 1$ dan $f^{-1}(10) = 3$, maka rumus fungsi asal $f(x)$ adalah ....

- A. $f(x) = \frac{1}{3}x + 1$  
  <sub>Salah: Siswa membalik gradien garis karena mengira sedang mencari turunan atau gradien invers.</sub>
- **B. $f(x) = 3x + 1$** ✅  
  <sub>Benar: Dari konsep invers, $f^{-1}(4) = 1 \iff f(1) = 4$ dan $f^{-1}(10) = 3 \iff f(3) = 10$. Sistem persamaan $a + b = 4$ dan $3a + b = 10$ menghasilkan $a = 3$ dan $b = 1$, sehingga $f(x) = 3x + 1$.</sub>
- C. $f(x) = 2x + 2$  
  <sub>Salah: Siswa salah membagi selisih nilai ordinat dengan absis saat mencari gradien $a$.</sub>
- D. $f(x) = 3x - 1$  
  <sub>Salah: Siswa salah menghitung nilai $b$ setelah memperoleh nilai $a = 3$ ($4 - 3$ dihitung menjadi $-1$).</sub>

**Pembahasan:** Langkah 1: Gunakan sifat hubungan fungsi dan inversnya:
$$f^{-1}(y) = x \iff f(x) = y$$
Maka:
$$f^{-1}(4) = 1 \implies f(1) = 4$$
$$f^{-1}(10) = 3 \implies f(3) = 10$$

Langkah 2: Substitusikan ke bentuk umum $f(x) = ax + b$:
$$a(1) + b = 4 \implies a + b = 4 \quad \text{...(persamaan 1)}$$
$$a(3) + b = 10 \implies 3a + b = 10 \quad \text{...(persamaan 2)}$$

Langkah 3: Selesaikan sistem persamaan dengan eliminasi:
$$(3a + b) - (a + b) = 10 - 4$$
$$2a = 6 \implies a = 3$$
Substitusikan $a = 3$ ke persamaan 1:
$$3 + b = 4 \implies b = 1$$

Jadi, rumus fungsi asalnya adalah $f(x) = 3x + 1$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b01-c-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: invers fungsi pecahan dan domain*

Diketahui fungsi $f(x) = \frac{4x - 7}{3x - 5}$ dengan $x \ne \frac{5}{3}$. Rumus fungsi invers $f^{-1}(x)$ beserta daerah asalnya adalah ....

- **A. $f^{-1}(x) = \frac{5x - 7}{3x - 4}$ dengan $x \ne \frac{4}{3}$** ✅  
  <sub>Benar: Misalkan $y = \frac{4x - 7}{3x - 5} \iff y(3x - 5) = 4x - 7 \iff 3xy - 5y = 4x - 7 \iff 3xy - 4x = 5y - 7 \iff x(3y - 4) = 5y - 7 \iff x = \frac{5y - 7}{3y - 4}$. Jadi, $f^{-1}(x) = \frac{5x - 7}{3x - 4}$ dengan penyebut tidak boleh nol, yaitu $3x - 4 \ne 0 \iff x \ne \frac{4}{3}$.</sub>
- B. $f^{-1}(x) = \frac{3x - 5}{4x - 7}$ dengan $x \ne \frac{7}{4}$  
  <sub>Salah: Hanya membalik posisi pembilang dan penyebut fungsi asal (kebalikan multiplikatif, bukan fungsi invers).</sub>
- C. $f^{-1}(x) = \frac{5x + 7}{3x - 4}$ dengan $x \ne \frac{4}{3}$  
  <sub>Salah: Kesalahan tanda saat memindahkan konstanta -7 ke ruas kanan.</sub>
- D. $f^{-1}(x) = \frac{5x - 7}{3x + 4}$ dengan $x \ne -\frac{4}{3}$  
  <sub>Salah: Kesalahan tanda aljabar saat mengelompokkan suku variabel x ke ruas kiri.</sub>

**Pembahasan:** Langkah 1: Misalkan $y = f(x)$,
$$y = \frac{4x - 7}{3x - 5}$$

Langkah 2: Kalikan kedua ruas dengan $(3x - 5)$ dan kelompokkan suku yang memuat $x$:
$$y(3x - 5) = 4x - 7$$
$$3xy - 5y = 4x - 7$$
$$3xy - 4x = 5y - 7$$
$$x(3y - 4) = 5y - 7$$
$$x = \frac{5y - 7}{3y - 4}$$

Langkah 3: Tuliskan rumus invers dan tentukan syarat daerah asalnya (penyebut tidak boleh nol):
$$f^{-1}(x) = \frac{5x - 7}{3x - 4}$$
Syarat penyebut: $3x - 4 \ne 0 \implies x \ne \frac{4}{3}$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b01-c-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: invers bentuk akar berdomain kuadrat*

Diketahui fungsi $g(x) = \sqrt{5x - 6}$ yang terdefinisi untuk $x \ge \frac{6}{5}$. Persamaan matematis untuk fungsi invers $g^{-1}(x)$ beserta daerah asalnya adalah ....

- A. $g^{-1}(x) = 5x^2 + 6$ untuk $x \ge 0$  
  <sub>Salah: Mengalikan koefisien 5 ke ruas variabel, bukan membaginya.</sub>
- B. $g^{-1}(x) = \frac{x^2 + 6}{5}$ untuk $x \ge \frac{6}{5}$  
  <sub>Salah: Menggunakan domain fungsi asal sebagai domain fungsi invers tanpa menyesuaikan dengan range fungsi asal.</sub>
- C. $g^{-1}(x) = \frac{x^2 - 6}{5}$ untuk $x \ge 0$  
  <sub>Salah: Kesalahan tanda operasi saat memindahkan konstanta -6 dari ruas kanan ke ruas kiri.</sub>
- **D. $g^{-1}(x) = \frac{x^2 + 6}{5}$ untuk $x \ge 0$** ✅  
  <sub>Benar: Misalkan $y = \sqrt{5x - 6}$. Karena hasil akar utama selalu non-negatif, daerah hasil $g$ adalah $y \ge 0$, yang menjadi daerah asal $g^{-1}(x) \implies x \ge 0$. Kuadratkan kedua ruas: $y^2 = 5x - 6 \iff 5x = y^2 + 6 \iff x = \frac{y^2 + 6}{5}$. Jadi, $g^{-1}(x) = \frac{x^2 + 6}{5}$ untuk $x \ge 0$.</sub>

**Pembahasan:** Langkah 1: Misalkan $y = \sqrt{5x - 6}$.
Nilai $y \ge 0$ untuk setiap nilai $x$ pada daerah asal $x \ge \frac{6}{5}$, sehingga daerah asal dari $g^{-1}(x)$ adalah $x \ge 0$.

Langkah 2: Selesaikan persamaan untuk $x$:
$$y^2 = 5x - 6$$
$$5x = y^2 + 6$$
$$x = \frac{y^2 + 6}{5}$$

Langkah 3: Ganti peubah $x$ dengan $g^{-1}(x)$ dan $y$ dengan $x$:
$$g^{-1}(x) = \frac{x^2 + 6}{5} \text{ untuk } x \ge 0$$
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b01-c-medium-bt01-018
*variasi (angka) | C3 | 2 langkah | jenis: evaluasi nilai invers fungsi linear*

Diketahui fungsi $f(x) = -4x + 9$ yang terdefinisi pada bilangan real. Nilai dari $f^{-1}(-7)$ adalah ....

- A. -½  
  <sub>Salah: Kesalahan aljabar saat memindahkan 9: -4a = -7 + 9 = 2 sehingga a = -2/4 = -1/2.</sub>
- B. -4  
  <sub>Salah: Kesalahan tanda saat membagi ruas kiri dan kanan dengan -4.</sub>
- C. 37  
  <sub>Salah: Siswa langsung mensubstitusikan -7 ke dalam f(x), yaitu f(-7) = -4(-7) + 9 = 28 + 9 = 37.</sub>
- **D. 4** ✅  
  <sub>Benar: Jika $f^{-1}(-7) = a$, maka $f(a) = -7$. Didapat $-4a + 9 = -7 \iff -4a = -16 \iff a = 4$.</sub>

**Pembahasan:** Langkah 1: Menggunakan sifat relasi invers fungsi $f^{-1}(y) = x \iff f(x) = y$.
Misalkan $f^{-1}(-7) = k$, maka:
$$f(k) = -7$$

Langkah 2: Selesaikan nilai $k$:
$$-4k + 9 = -7$$
$$-4k = -7 - 9$$
$$-4k = -16$$
$$k = \frac{-16}{-4} = 4$$

Jadi, nilai dari $f^{-1}(-7)$ adalah $4$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b01-c-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: evaluasi nilai invers komposisi terbalik*

Diketahui fungsi $f(x) = 2x - 1$ dan $g(x) = 3x + 5$. Jika $h(x) = (g \circ f)(x)$, maka nilai dari $h^{-1}(17)$ adalah ....

- A. 2  
  <sub>Salah: Salah melakukan komposisi menjadi (f o g)(x) = 2(3x + 5) - 1 = 6x + 9, lalu 6a + 9 = 17 menghasilkan 6a = 8 sehingga a bukan 5/2 melainkan dibulatkan.</sub>
- B. \frac{19}{6}  
  <sub>Salah: Kesalahan aljabar saat memindahkan konstanta: 6a = 17 + 2 = 19 sehingga a = 19/6.</sub>
- **C. \frac{5}{2}** ✅  
  <sub>Benar: Komposisi $h(x) = g(f(x)) = 3(2x - 1) + 5 = 6x - 3 + 5 = 6x + 2$. Persamaan $h^{-1}(17) = a \iff h(a) = 17 \iff 6a + 2 = 17 \iff 6a = 15 \iff a = \frac{15}{6} = \frac{5}{2}$.</sub>
- D. 3  
  <sub>Salah: Lupa mengalikan konstanta di dalam tanda kurung: g(f(x)) = 3(2x - 1) + 5 disederhanakan menjadi 6x - 1 + 5 = 6x + 4, lalu 6a + 4 = 17 disederhanakan salah menjadi 6a = 18 sehingga a = 3.</sub>

**Pembahasan:** Langkah 1: Tentukan fungsi komposisi $h(x) = (g \circ f)(x)$:
$$h(x) = g(f(x)) = 3(2x - 1) + 5 = 6x - 3 + 5 = 6x + 2$$

Langkah 2: Gunakan relasi invers $h^{-1}(17) = x \iff h(x) = 17$:
$$6x + 2 = 17$$

Langkah 3: Selesaikan nilai $x$:
$$6x = 17 - 2$$
$$6x = 15$$
$$x = \frac{15}{6} = \frac{5}{2}$$

Jadi, nilai dari $h^{-1}(17)$ adalah $\frac{5}{2}$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b01-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: pemodelan aljabar fungsi invers kontekstual*

Sebuah toko buku memberlakukan diskon sebesar 25% untuk setiap pembelian buku, kemudian pembeli mendapatkan potongan kupon langsung sebesar Rp12.000,00. Jika $x$ menyatakan harga label buku (dalam rupiah) dan $y$ menyatakan harga akhir yang dibayarkan, rumus fungsi invers yang menyatakan harga label buku $x$ sebagai fungsi dari harga akhir $y$ adalah ....

- A. $x = \frac{4}{3}(y - 12.000)$  
  <sub>Salah: Salah tanda operasi saat memindahkan suku potongan kupon -12.000 ke ruas lain.</sub>
- **B. $x = \frac{4}{3}(y + 12.000)$** ✅  
  <sub>Benar: Diskon 25% membuat harga buku menjadi (1 - 0,25)x = 0,75x = 3/4 x. Setelah dipotong kupon Rp12.000, didapat y = 3/4 x - 12.000. Untuk mencari rumus x sebagai fungsi y: y + 12.000 = 3/4 x <=> x = 4/3(y + 12.000).</sub>
- C. $x = \frac{3}{4}(y - 12.000)$  
  <sub>Salah: Tidak membalik faktor pengali 3/4 menjadi 4/3 serta salah menuliskan tanda operasi pengurangan.</sub>
- D. $x = \frac{4}{3}y + 12.000$  
  <sub>Salah: Lupa mengalikan suku konstanta Rp12.000,00 dengan faktor 4/3 saat mengalikan kedua ruas.</sub>

**Pembahasan:** Langkah 1: Susun persamaan harga akhir $y$ sebagai fungsi dari harga awal $x$.
Harga setelah diskon 25% adalah $(1 - 0{,}25)x = 0{,}75x = \frac{3}{4}x$.
Harga akhir setelah potongan kupon Rp12.000,00 adalah:
$$y = \frac{3}{4}x - 12.000$$

Langkah 2: Tambahkan kedua ruas dengan $12.000$:
$$y + 12.000 = \frac{3}{4}x$$

Langkah 3: Kalikan kedua ruas dengan $\frac{4}{3}$ untuk menyatakan $x$ dalam $y$:
$$x = \frac{4}{3}(y + 12.000)$$

Jadi, fungsi kebalikannya adalah $x = \frac{4}{3}(y + 12.000)$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b01-c-hard-bt01-001
*orisinal | C5 | 5 langkah | jenis: identitas invers fungsi rasional*

Diketahui fungsi $f(x) = \frac{px + 7}{3x - 5}$ terdefinisi untuk $x \ne \frac{5}{3}$. Jika fungsi $f$ merupakan invers dari dirinya sendiri, yaitu $f^{-1}(x) = f(x)$ untuk semua nilai $x$ pada daerah asalnya, maka nilai dari konstanta $p$ adalah ....

- **A. 5** ✅  
  <sub>Benar: Misalkan $y = \frac{px + 7}{3x - 5} \iff y(3x - 5) = px + 7 \iff 3xy - 5y = px + 7 \iff x(3y - p) = 5y + 7 \iff x = \frac{5y + 7}{3y - p}$.
Maka $f^{-1}(x) = \frac{5x + 7}{3x - p}$.
Agar $f^{-1}(x) = f(x)$, bentuk $\frac{5x + 7}{3x - p}$ harus identik dengan $\frac{px + 7}{3x - 5}$.
Dengan membandingkan koefisien pembilang dan penyebut: koefisien $x$ pada pembilang memberikan $p = 5$, dan konstanta pada penyebut memberikan $-p = -5 \implies p = 5$. Kedua perbandingan konsisten, sehingga $p = 5$.</sub>
- B. 7  
  <sub>Salah: Mengambil angka konstanta pada pembilang fungsi.</sub>
- C. \frac{5}{3}  
  <sub>Salah: Menyamakan $p$ dengan nilai pembuat nol penyebut pada daerah asal.</sub>
- D. -5  
  <sub>Salah: Kesalahan tanda minus saat membandingkan koefisien penyebut $3x - p$ dengan $3x - 5$.</sub>

**Pembahasan:** Langkah 1: Cari rumus fungsi invers $f^{-1}(x)$ dari $y = \frac{px + 7}{3x - 5}$.
Langkah 2: Kalikan silang: $3xy - 5y = px + 7$.
Langkah 3: Kelompokkan variabel $x$: $x(3y - p) = 5y + 7 \implies x = \frac{5y + 7}{3y - p}$.
Langkah 4: Tulis fungsi invers: $f^{-1}(x) = \frac{5x + 7}{3x - p}$.
Langkah 5: Syarat $f^{-1}(x) = f(x) \implies \frac{5x + 7}{3x - p} = \frac{px + 7}{3x - 5}$. Dari kesamaan kedua pecahan rasional ini, diperoleh $p = 5$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b01-c-hard-bt01-002
*variasi (angka) | C5 | 4 langkah | jenis: invers fungsi komposisi linear*

Diketahui fungsi linear $f(x) = ax + 8$ dengan konstanta $a > 0$ dan memenuhi $(f \circ f)(x) = 9x + 32$. Jika diketahui $f^{-1}(k) = 2$, nilai $k$ yang memenuhi adalah ....

- A. 10  
  <sub>Salah: Siswa salah menghitung fungsi dengan mengira $f(x) = 3x + 4$ sehingga $f(2) = 10$.</sub>
- **B. 14** ✅  
  <sub>Benar: Dari $(f \circ f)(x) = a(ax + 8) + 8 = a^2 x + 8a + 8 = 9x + 32$, diperoleh $a^2 = 9 \implies a = 3$ (karena $a > 0$). Maka $f(x) = 3x + 8$. Persamaan $f^{-1}(k) = 2$ ekuivalen dengan $f(2) = k$, sehingga $k = 3(2) + 8 = 14$.</sub>
- C. -2  
  <sub>Salah: Siswa memilih nilai $a = -3$ yang melanggar syarat $a > 0$, sehingga menghasilkan $k = -3(2) + 8 = 2$ lalu salah tanda menjadi -2.</sub>
- D. 6  
  <sub>Salah: Siswa keliru mengira $f^{-1}(k) = 2$ berarti mencari $f^{-1}(2)$ pada fungsi yang salah.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus komposisi $(f \circ f)(x)$.
$(f \circ f)(x) = f(f(x)) = a(ax + 8) + 8 = a^2 x + 8a + 8$.

Langkah 2: Menentukan nilai konstanta $a$.
Samakan koefisien dengan $9x + 32$:
$a^2 = 9 \implies a = 3$ (karena $a > 0$).
Konstanta: $8(3) + 8 = 32$ (sesuai).
Jadi, rumus fungsinya adalah $f(x) = 3x + 8$.

Langkah 3: Menentukan nilai $k$.
Berdasarkan definisi fungsi invers, jika $f^{-1}(k) = 2$, maka $f(2) = k$.
$k = f(2) = 3(2) + 8 = 6 + 8 = 14$.

Jadi, nilai $k$ yang memenuhi adalah 14.
**Acuan:** pretest — kelas11-b01-p0056-latihan-15-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b01-c-hard-bt01-003
*variasi (angka) | C5 | 4 langkah | jenis: titik potong invers linear*

Diberikan fungsi linear $f(x) = -4x + 15$. Jika grafik fungsi invers $f^{-1}(x)$ berpotongan dengan grafik garis $y = x + 5$ di titik $(p, q)$, nilai dari $p + q$ adalah ....

- A. 5  
  <sub>Salah: Siswa salah menghitung titik potong dengan mengabaikan variabel $x$ dan hanya menjumlahkan konstanta.</sub>
- B. -3  
  <sub>Salah: Siswa melakukan kesalahan tanda pada koordinat perpotongan menjadi $(1, -4)$ sehingga menghasilkan $1 + (-4) = -3$.</sub>
- **C. 3** ✅  
  <sub>Benar: Invers dari $f(x)$ adalah $f^{-1}(x) = \frac{15 - x}{4}$. Titik potong dicari dari $\frac{15 - x}{4} = x + 5 \iff 15 - x = 4x + 20 \iff 5x = -5 \iff x = -1$. Maka $p = -1$ dan $q = -1 + 5 = 4$. Jadi, $p + q = -1 + 4 = 3$.</sub>
- D. 7  
  <sub>Salah: Siswa salah memindahkan ruas persamaan menjadi $4x - x = 3x$ dan $20 - 15 = 5$, berakibat pada nilai koordinat yang keliru.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi invers $f^{-1}(x)$.
Misalkan $y = -4x + 15$.
$4x = 15 - y \iff x = \frac{15 - y}{4}$.
Maka $f^{-1}(x) = \frac{15 - x}{4}$.

Langkah 2: Menentukan absis titik potong ($p$).
Samakan nilai $y$ dari kedua persamaan:
$\frac{15 - x}{4} = x + 5$
$15 - x = 4(x + 5)$
$15 - x = 4x + 20$
$-5x = 5$
$x = -1$.
Jadi, $p = -1$.

Langkah 3: Menentukan ordinat titik potong ($q$).
Substitusi nilai $x = -1$ ke persamaan garis:
$q = -1 + 5 = 4$.

Langkah 4: Menghitung $p + q$.
$p + q = -1 + 4 = 3$.

Jadi, nilai dari $p + q$ adalah 3.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b01-c-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: titik temu invers fungsi kuadrat*

Diberikan fungsi kuadrat $f(x) = x^2 - 5x + 8$ yang dibatasi pada domain $D_f = \{x \in \mathbb{R} \mid x \ge 2{,}5\}$ sehingga memiliki fungsi invers $f^{-1}(x)$. Nilai $x$ yang memenuhi persamaan $f(x) = f^{-1}(x)$ adalah ....

- A. 2  
  <sub>Salah: Siswa mengambil akar persamaan kuadrat tanpa mengecek batasan domain $x \ge 2{,}5$.</sub>
- B. 1  
  <sub>Salah: Siswa salah melakukan faktorisasi persamaan kuadrat menjadi $(x - 1)(x - 8) = 0$.</sub>
- C. 8  
  <sub>Salah: Siswa keliru menganggap solusi perpotongan sama dengan nilai konstanta fungsi.</sub>
- **D. 4** ✅  
  <sub>Benar: Karena $f(x)$ monoton naik pada $x \ge 2{,}5$, titik temu $f(x) = f^{-1}(x)$ berada pada garis $y = x$. Persamaan $x^2 - 5x + 8 = x \iff x^2 - 6x + 8 = 0$ menghasilkan $x = 2$ atau $x = 4$. Karena $x \ge 2{,}5$, nilai $x = 2$ tidak memenuhi daerah asal, sehingga nilai yang memenuhi hanyalah $x = 4$.</sub>

**Pembahasan:** Langkah 1: Memahami sifat titik temu fungsi monoton naik dengan inversnya.
Untuk fungsi yang monoton naik pada daerah asalnya, grafik $y = f(x)$ dan grafik $y = f^{-1}(x)$ hanya dapat berpotongan pada garis simetri $y = x$.

Langkah 2: Membentuk persamaan $f(x) = x$.
$x^2 - 5x + 8 = x$
$x^2 - 6x + 8 = 0$

Langkah 3: Menyelesaikan persamaan kuadrat.
$(x - 2)(x - 4) = 0$
Diperoleh $x = 2$ atau $x = 4$.

Langkah 4: Menguji syarat daerah asal ($D_f$).
Daerah asal fungsi dibatasi pada $x \ge 2{,}5$.
- Untuk $x = 2$: tidak memenuhi karena $2 < 2{,}5$.
- Untuk $x = 4$: memenuhi karena $4 \ge 2{,}5$.

Jadi, nilai $x$ yang memenuhi persamaan tersebut adalah 4.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b01-c-hard-bt01-005
*variasi (angka) | C5 | 3 langkah | jenis: rekonstruksi fungsi invers parameter*

Diketahui fungsi linear $f(x) = 3x + b$ dan $(f \circ f)(x) = 9x + 28$. Pasangan nilai $b$ dan rumus fungsi invers $f^{-1}(x)$ yang tepat adalah ....

- A. $b = 7$ dan $f^{-1}(x) = \frac{x + 7}{3}$  
  <sub>Salah: Siswa salah mengubah tanda saat membalik persamaan linear menjadi fungsi invers.</sub>
- B. $b = 4$ dan $f^{-1}(x) = \frac{x - 4}{3}$  
  <sub>Salah: Siswa membagi 28 dengan 7 alih-alih dengan 4 sehingga mendapatkan nilai $b = 4$.</sub>
- **C. $b = 7$ dan $f^{-1}(x) = \frac{x - 7}{3}$** ✅  
  <sub>Benar: $(f \circ f)(x) = 3(3x + b) + b = 9x + 4b$. Dari $9x + 4b = 9x + 28$ diperoleh $4b = 28 \iff b = 7$. Maka $f(x) = 3x + 7$, sehingga $x = \frac{y - 7}{3}$ atau $f^{-1}(x) = \frac{x - 7}{3}$.</sub>
- D. $b = 14$ dan $f^{-1}(x) = \frac{x - 14}{3}$  
  <sub>Salah: Siswa keliru menganggap $f(f(x)) = 9x + 2b$ sehingga $2b = 28 \iff b = 14$.</sub>

**Pembahasan:** Langkah 1: Menentukan komposisi $(f \circ f)(x) = f(f(x)) = 3(3x + b) + b = 9x + 4b$.
Langkah 2: Menyamakan koefisien dengan bentuk yang diketahui: $9x + 4b = 9x + 28 \implies 4b = 28 \implies b = 7$.
Langkah 3: Menentukan rumus invers dari $f(x) = 3x + 7$. Misalkan $y = 3x + 7$, maka $3x = y - 7 \implies x = \frac{y - 7}{3}$. Jadi, $f^{-1}(x) = \frac{x - 7}{3}$.
**Acuan:** pretest — kelas11-b01-p0056-latihan-15-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b01-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: analisis domain pembatasan fungsi kuadrat*

Fungsi kuadrat $f(x) = x^2 - 8x + 11$ dibatasi pada domain $D_f = [c, \infty)$ agar memiliki invers. Jika diketahui $f^{-1}(-1) = 6$, maka nilai batas bawah domain terkecil $c$ yang memenuhi syarat tersebut adalah ....

- A. 2  
  <sub>Salah: Siswa mengira domain dapat diperluas hingga $c = 2$ padahal fungsi tidak injektif pada $[2, \infty)$ karena memuat puncak di $x = 4$.</sub>
- B. 6  
  <sub>Salah: Siswa langsung mengambil nilai $x = 6$ dari $f^{-1}(-1) = 6$ sebagai batas domain.</sub>
- C. -1  
  <sub>Salah: Siswa tertukar antara nilai domain dengan nilai keluaran $y = -1$.</sub>
- **D. 4** ✅  
  <sub>Benar: Titik puncak fungsi kuadrat berada pada $x_p = -\frac{-8}{2(1)} = 4$. Agar monoton naik dan bijektif pada interval $[c, \infty)$, haruslah $c \ge 4$. Karena $f(6) = 6^2 - 8(6) + 11 = -1$, nilai masukan $6$ berada pada cabang $x \ge 4$, sehingga batas terkecil untuk $c$ adalah 4.</sub>

**Pembahasan:** Langkah 1: Tentukan sumbu simetri fungsi kuadrat $f(x) = x^2 - 8x + 11$: $x_s = -\frac{b}{2a} = -\frac{-8}{2} = 4$.
Langkah 2: Suatu fungsi kuadrat memiliki fungsi invers pada domain berbentuk $[c, \infty)$ jika domain tersebut tidak memuat bagian yang berbalik arah, yaitu seluruhnya terletak di sebelah kanan sumbu simetri ($c \ge 4$).
Langkah 3: Periksa kondisi $f^{-1}(-1) = 6 \iff f(6) = 6^2 - 8(6) + 11 = 36 - 48 + 11 = -1$. Karena nilai $x = 6 \ge 4$, nilai ini konsisten berada pada domain $[4, \infty)$.
Langkah 4: Nilai terkecil dari $c$ yang menjamin fungsi bijektif pada $[c, \infty)$ adalah $c = x_s = 4$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b01-c-hard-bt01-007
*orisinal | C6 | 5 langkah | jenis: persamaan invers komposisi bertingkat*

Diketahui dua fungsi linear $f(x) = 2x + 5$ dan $g(x) = 3x - 1$. Jika $h(x) = (f \circ g)(x)$ dan berlaku persamaan $h^{-1}(2a + 1) = 3$, maka nilai konstanta $a$ adalah ....

- **A. 10** ✅  
  <sub>Benar: Sifat fungsi invers menyatakan $h^{-1}(2a + 1) = 3 \iff h(3) = 2a + 1$. Hitung $h(3) = f(g(3))$. Karena $g(3) = 3(3) - 1 = 8$, maka $h(3) = f(8) = 2(8) + 5 = 21$. Dengan menyamakan $2a + 1 = 21$, didapat $2a = 20 \iff a = 10$.</sub>
- B. 11  
  <sub>Salah: Siswa salah menjumlahkan $2a = 21 + 1 = 22 \implies a = 11$ saat memindahkan konstanta 1.</sub>
- C. 20  
  <sub>Salah: Siswa lupa membagi dengan 2 setelah mendapatkan $2a = 20$.</sub>
- D. 8  
  <sub>Salah: Siswa menghentikan perhitungan pada $g(3) = 8$ dan menganggap $2a + 1 = 8$ sehingga $a \approx 3{,}5$ atau salah perhitungan aljabar.</sub>

**Pembahasan:** Langkah 1: Menggunakan sifat dasar fungsi invers: $h^{-1}(y) = x \iff h(x) = y$. Maka $h^{-1}(2a + 1) = 3$ ekuivalen dengan $h(3) = 2a + 1$.
Langkah 2: Menghitung nilai fungsi bagian dalam: $g(3) = 3(3) - 1 = 9 - 1 = 8$.
Langkah 3: Menghitung nilai fungsi komposisi: $h(3) = f(g(3)) = f(8) = 2(8) + 5 = 16 + 5 = 21$.
Langkah 4: Membentuk persamaan linear: $2a + 1 = 21$.
Langkah 5: Menyelesaikan nilai $a$: $2a = 20 \implies a = 10$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b01-c-hard-bt01-008
*variasi (angka) | C5 | 4 langkah | jenis: domain dan range invers fungsi akar*

Diberikan fungsi irasional $f(x) = \sqrt{6x - 24} + 5$ yang terdefinisi pada daerah asal terbesarnya. Jika $f^{-1}(x)$ merupakan fungsi invers dari $f(x)$, manakah pernyataan berikut yang mendefinisikan rumus $f^{-1}(x)$ beserta daerah asal ($D_{f^{-1}}$) dan daerah hasil ($R_{f^{-1}}$) yang tepat?

- A. $f^{-1}(x) = \frac{x^2 - 1}{6}$ dengan $D_{f^{-1}} = [0, \infty)$ dan $R_{f^{-1}} = [4, \infty)$  
  <sub>Salah: Menguadratkan langsung kedua ruas tanpa mengisolasi bentuk akar terlebih dahulu $((y)^2 = 6x - 24 + 25)$.</sub>
- **B. $f^{-1}(x) = \frac{(x - 5)^2 + 24}{6}$ dengan $D_{f^{-1}} = [5, \infty)$ dan $R_{f^{-1}} = [4, \infty)$** ✅  
  <sub>Benar: Daerah asal $f(x)$ mensyaratkan $6x - 24 \ge 0 \iff x \ge 4$, sehingga $D_f = [4, \infty)$. Karena nilai $\sqrt{6x - 24} \ge 0$, maka $f(x) \ge 5$, sehingga daerah hasil $R_f = [5, \infty)$. Berdasarkan sifat fungsi invers, daerah asal $D_{f^{-1}} = R_f = [5, \infty)$ dan daerah hasil $R_{f^{-1}} = D_f = [4, \infty)$. Untuk menurunkan rumus invers, misalkan $y = \sqrt{6x - 24} + 5 \iff y - 5 = \sqrt{6x - 24} \iff (y - 5)^2 = 6x - 24 \iff 6x = (y - 5)^2 + 24 \iff x = \frac{(y - 5)^2 + 24}{6}$. Dengan demikian, diperoleh $f^{-1}(x) = \frac{(x - 5)^2 + 24}{6}$ dengan $D_{f^{-1}} = [5, \infty)$ dan $R_{f^{-1}} = [4, \infty)$.</sub>
- C. $f^{-1}(x) = \frac{(x + 5)^2 - 24}{6}$ dengan $D_{f^{-1}} = [5, \infty)$ dan $R_{f^{-1}} = [4, \infty)$  
  <sub>Salah: Salah tanda saat memindahkan suku konstanta $+5$ dan $-24$ dalam aljabar pembalikan.</sub>
- D. $f^{-1}(x) = \frac{(x - 5)^2 + 24}{6}$ dengan $D_{f^{-1}} = [4, \infty)$ dan $R_{f^{-1}} = [5, \infty)$  
  <sub>Salah: Tertukar antara domain fungsi invers ($R_f$) dan range fungsi invers ($D_f$).</sub>

**Pembahasan:** Langkah 1: Menentukan domain dan range fungsi asal $f(x)$.
Syarat bentuk akar: $6x - 24 \ge 0 \implies x \ge 4$. Jadi, $D_f = [4, \infty)$.
Karena $\sqrt{6x - 24} \ge 0$, maka $y = \sqrt{6x - 24} + 5 \ge 5$. Jadi, $R_f = [5, \infty)$.

Langkah 2: Menentukan domain dan range fungsi invers.
$D_{f^{-1}} = R_f = [5, \infty)$
$R_{f^{-1}} = D_f = [4, \infty)$

Langkah 3: Menentukan rumus $f^{-1}(x)$.
$y = \sqrt{6x - 24} + 5$
$y - 5 = \sqrt{6x - 24}$
Kuadratkan kedua ruas untuk $y \ge 5$:
$(y - 5)^2 = 6x - 24$
$6x = (y - 5)^2 + 24$
$x = \frac{(y - 5)^2 + 24}{6}$

Jadi, $f^{-1}(x) = \frac{(x - 5)^2 + 24}{6}$ dengan $D_{f^{-1}} = [5, \infty)$ dan $R_{f^{-1}} = [4, \infty)$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b01-c-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: evaluasi keselarasan invers fungsi pecahan*

Diberikan dua fungsi pecahan $f(x) = \frac{ax + 8}{x - 2}$ dengan $x \ne 2$ dan $g(x) = \frac{2x + b}{x - 3}$ dengan $x \ne 3$, di mana $a$ dan $b$ adalah konstanta real. Jika fungsi $g(x)$ merupakan fungsi invers dari $f(x)$, maka nilai dari $a^2 + b$ adalah ....

- **A. 17** ✅  
  <sub>Benar: Misalkan $y = \frac{ax + 8}{x - 2}$. Maka $y(x - 2) = ax + 8 \iff yx - 2y = ax + 8 \iff x(y - a) = 2y + 8 \iff x = \frac{2y + 8}{y - a}$. Dengan demikian, rumus fungsi invers adalah $f^{-1}(x) = \frac{2x + 8}{x - a}$. Karena $g(x) = f^{-1}(x)$, maka $\frac{2x + b}{x - 3} = \frac{2x + 8}{x - a}$. Dari kesamaan penyebut diperoleh $x - a = x - 3 \implies a = 3$, dan dari kesamaan pembilang diperoleh $2x + b = 2x + 8 \implies b = 8$. Jadi, $a^2 + b = 3^2 + 8 = 9 + 8 = 17$.</sub>
- B. 11  
  <sub>Salah: Siswa menjumlahkan langsung kedua parameter $a + b = 3 + 8 = 11$ karena lupa mengkuadratkan nilai $a$.</sub>
- C. 14  
  <sub>Salah: Siswa menghitung $2a + b = 2(3) + 8 = 14$ karena keliru mengalikan dua alih-alih memangkatkan dua.</sub>
- D. 1  
  <sub>Salah: Siswa salah menerapkan tanda operasi aljabar sehingga menghitung $a^2 - b = 9 - 8 = 1$.</sub>

**Pembahasan:** Langkah 1: Menentukan invers dari $f(x)$.
$y = \frac{ax + 8}{x - 2}$
$y(x - 2) = ax + 8$
$xy - 2y = ax + 8$
$xy - ax = 2y + 8$
$x(y - a) = 2y + 8$
$x = \frac{2y + 8}{y - a}$
Sehingga diperoleh $f^{-1}(x) = \frac{2x + 8}{x - a}$.

Langkah 2: Menyamakan $f^{-1}(x)$ dengan $g(x)$.
$g(x) = \frac{2x + b}{x - 3} = \frac{2x + 8}{x - a}$

Langkah 3: Menentukan nilai parameter $a$ dan $b$.
Dari penyebut: $x - 3 = x - a \implies a = 3$.
Dari pembilang: $2x + b = 2x + 8 \implies b = 8$.

Langkah 4: Menghitung nilai yang diminta.
$a^2 + b = 3^2 + 8 = 9 + 8 = 17$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b01-c-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: penyelesaian persamaan invers komposisi*

Diketahui dua fungsi bijektif $f$ dan $g$ pada himpunan bilangan real dengan rumus $f(x) = 2x + 3$ dan $g^{-1}(x) = \frac{x - 5}{4}$. Jika berlaku persamaan $(g \circ f^{-1})^{-1}(k) = 11$, maka nilai $k$ adalah ....

- A. 23  
  <sub>Salah: Siswa tidak membalik urutan fungsi komposisi saat mencari inversnya, yaitu menganggap $(g \circ f^{-1})^{-1} = g^{-1} \circ f$, sehingga menyelesaikan $g^{-1}(f(k)) = 11 \implies \frac{(2k + 3) - 5}{4} = 11 \implies 2k - 2 = 44 \implies k = 23$.</sub>
- B. 9  
  <sub>Salah: Siswa lupa mengalikan silang penyebut pada tahap akhir, langsung menghitung $k - 5 = 4 \implies k = 9$.</sub>
- C. 25  
  <sub>Salah: Siswa melakukan kesalahan aljabar pada tahap $2(g^{-1}(k)) + 3 = 11$ dengan menambahkan alih-alih mengurangkan sehingga diperoleh $2(g^{-1}(k)) = 10 \implies g^{-1}(k) = 5$, lalu $\frac{k - 5}{4} = 5 \implies k = 25$.</sub>
- **D. 21** ✅  
  <sub>Benar: Berdasarkan sifat invers dari komposisi fungsi, $((g \circ f^{-1})^{-1})(x) = ((f^{-1})^{-1} \circ g^{-1})(x) = (f \circ g^{-1})(x)$. Oleh karena itu, persamaan menjadi $(f \circ g^{-1})(k) = 11 \iff f(g^{-1}(k)) = 11$. Karena $f(x) = 2x + 3$, maka $2(g^{-1}(k)) + 3 = 11 \iff 2(g^{-1}(k)) = 8 \iff g^{-1}(k) = 4$. Substitusikan ke rumus $g^{-1}(x)$: $\frac{k - 5}{4} = 4 \iff k - 5 = 16 \iff k = 21$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat invers dari komposisi fungsi:
$(g \circ f^{-1})^{-1}(x) = (f^{-1})^{-1}(g^{-1}(x)) = (f \circ g^{-1})(x)$

Langkah 2: Terapkan ke persamaan yang diberikan:
$(f \circ g^{-1})(k) = 11 \iff f(g^{-1}(k)) = 11$

Langkah 3: Hitung nilai $g^{-1}(k)$ menggunakan rumus $f(x) = 2x + 3$:
$2(g^{-1}(k)) + 3 = 11$
$2(g^{-1}(k)) = 8$
$g^{-1}(k) = 4$

Langkah 4: Tentukan nilai $k$ dari rumus $g^{-1}(x) = \frac{x - 5}{4}$:
$\frac{k - 5}{4} = 4$
$k - 5 = 16$
$k = 21$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b01-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: invers komposisi fungsi pecahan*

Diketahui dua fungsi $f(x) = \frac{5x - 3}{x - 2}$ untuk $x \ne 2$ dan $g(x) = 3x - 3$. Jika berlaku persamaan $(f^{-1} \circ g)(m) = 3$, maka nilai dari konstanta $m$ adalah ....

- A. 4  
  <sub>Salah: Kesalahan perhitungan saat menyelesaikan persamaan $3m - 3 = 12$ menjadi $3m = 12$ sehingga $m = 4$.</sub>
- **B. 5** ✅  
  <sub>Benar: Persamaan $(f^{-1} \circ g)(m) = 3$ ekuivalen dengan $f^{-1}(g(m)) = 3 \iff g(m) = f(3)$. Dihitung $f(3) = \frac{5(3) - 3}{3 - 2} = 12$. Maka $3m - 3 = 12 \iff 3m = 15 \iff m = 5$.</sub>
- C. 7  
  <sub>Salah: Salah menggunakan operasi invers pada komposisi, menganggap $f(m) = g(3)$.</sub>
- D. 3  
  <sub>Salah: Siswa langsung menyamakan nilai input $m$ dengan hasil luar 3 tanpa memproses relasi invers.</sub>

**Pembahasan:** Berdasarkan definisi fungsi invers, relasi $f^{-1}(y) = x$ setara dengan $f(x) = y$.
Persamaan pada soal:
$$(f^{-1} \circ g)(m) = 3 \iff f^{-1}(g(m)) = 3$$
Ekuivalen dengan:
$$g(m) = f(3)$$
Hitung nilai $f(3)$:
$$f(3) = \frac{5(3) - 3}{3 - 2} = \frac{15 - 3}{1} = 12$$
Substitusikan ke fungsi $g(m)$:
$$3m - 3 = 12$$
$$3m = 15$$
$$m = 5$$
Jadi, nilai $m$ yang memenuhi adalah 5.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b01-c-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: penentuan parameter invers identitas*

Diberikan dua fungsi pecahan $f(x) = \frac{ax + 5}{2x - 3}$ dengan $x \ne \frac{3}{2}$ dan $g(x) = \frac{3x + 5}{bx - 4}$ dengan $x \ne \frac{4}{b}$. Jika berlaku $(f \circ g)(x) = x$ untuk setiap $x$ pada daerah asal yang memenuhi, maka nilai dari $a^2 + b^2$ adalah ....

- **A. 20** ✅  
  <sub>Benar: Karena $(f \circ g)(x) = x$, maka $g(x) = f^{-1}(x)$. Invers dari $f(x) = \frac{ax + 5}{2x - 3}$ adalah $f^{-1}(x) = \frac{3x + 5}{2x - a}$. Menyamakan dengan $g(x) = \frac{3x + 5}{bx - 4}$ menghasilkan $b = 2$ dan $a = 4$. Maka $a^2 + b^2 = 4^2 + 2^2 = 16 + 4 = 20$.</sub>
- B. 8  
  <sub>Salah: Siswa mengalikan nilai $a \cdot b = 4 \times 2 = 8$ alih-alih menjumlahkan kuadratnya.</sub>
- C. 12  
  <sub>Salah: Siswa salah tanda saat menyamakan penyebut sehingga menghitung $a^2 - b^2 = 16 - 4 = 12$.</sub>
- D. 6  
  <sub>Salah: Siswa menghitung nilai $a + b = 4 + 2 = 6$, bukan $a^2 + b^2$.</sub>

**Pembahasan:** Berdasarkan sifat fungsi invers, jika $(f \circ g)(x) = x$, maka $g(x) = f^{-1}(x)$.
Langkah 1: Menentukan invers dari $f(x)$:
Misalkan $y = \frac{ax + 5}{2x - 3}$
$$y(2x - 3) = ax + 5$$
$$2xy - 3y = ax + 5$$
$$2xy - ax = 3y + 5$$
$$x(2y - a) = 3y + 5$$
$$x = \frac{3y + 5}{2y - a}$$
Diperoleh rumus invers:
$$f^{-1}(x) = \frac{3x + 5}{2x - a}$$

Langkah 2: Menyamakan $f^{-1}(x)$ dengan $g(x)$:
$$\frac{3x + 5}{2x - a} = \frac{3x + 5}{bx - 4}$$
Karena pembilang sudah identik ($3x + 5$), penyebut harus bernilai sama untuk setiap $x$:
$$2x - a = bx - 4$$
Dari kesamaan koefisien suku-sejenis:
$$b = 2$$
$$-a = -4 \implies a = 4$$

Langkah 3: Menghitung nilai $a^2 + b^2$:
$$a^2 + b^2 = 4^2 + 2^2 = 16 + 4 = 20$$
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b01-c-hard-bt01-013
*orisinal | C6 | 4 langkah | jenis: pembatasan domain fungsi kuadrat*

Fungsi kuadrat $f(x) = -x^2 + 8x - 12$ dibatasi pada daerah asal $D_f = [k, \infty)$ agar memiliki fungsi invers. Jika rumus fungsi invers yang terbentuk bertanda positif di depan bentuk akar, yaitu $f^{-1}(x) = 4 + \sqrt{4 - x}$, maka nilai batas domain $k$ beserta daerah asal dari fungsi invers $f^{-1}(x)$ berturut-turut adalah ....

- A. $k = 4$ dan $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \ge 4\}$  
  <sub>Salah: Keliru menganggap range fungsi kuadrat membuka ke atas sehingga menuliskan $x \ge 4$.</sub>
- B. $k = 2$ dan $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \le 4\}$  
  <sub>Salah: Memilih salah satu pembuat nol fungsi ($x = 2$) sebagai nilai batas domain $k$ alih-alih sumbu simetri.</sub>
- **C. $k = 4$ dan $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \le 4\}$** ✅  
  <sub>Benar: Sumbu simetri kurva adalah $x = -\frac{8}{2(-1)} = 4$. Agar invers bernilai $4 + \sqrt{\dots}$, domain harus $x \ge 4$, sehingga $k = 4$. Nilai maksimum kurva adalah $f(4) = 4$, sehingga range $f(x)$ adalah $y \le 4$. Karena $D_{f^{-1}} = R_f$, maka domain fungsi invers adalah $\{x \in \mathbb{R} \mid x \le 4\}$.</sub>
- D. $k = 6$ dan $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \ge 0\}$  
  <sub>Salah: Menggunakan akar kedua fungsi sebagai pembatas dan mengasumsikan nilai di dalam akar invers harus non-negatif sederhana.</sub>

**Pembahasan:** Langkah 1: Mengubah bentuk $f(x)$ ke bentuk kuadrat sempurna:
$$f(x) = -(x^2 - 8x) - 12 = -(x^2 - 8x + 16) + 16 - 12 = -(x - 4)^2 + 4$$
Titik puncak kurva berada pada $(4, 4)$ dengan sumbu simetri $x = 4$.

Langkah 2: Menentukan nilai $k$:
$$y = -(x - 4)^2 + 4$$
$$(x - 4)^2 = 4 - y$$
$$x - 4 = \pm \sqrt{4 - y}$$
$$x = 4 \pm \sqrt{4 - y}$$
Agar rumus invers bertanda positif: $f^{-1}(x) = 4 + \sqrt{4 - x}$, maka nilai $x \ge 4$. Dengan demikian, batas daerah asal $D_f = [k, \infty)$ adalah $k = 4$.

Langkah 3: Menentukan daerah asal fungsi invers ($D_{f^{-1}}$):
Karena koefisien $x^2$ negatif ($a = -1$), titik puncak $(4, 4)$ adalah nilai maksimum, sehingga range fungsi $f$ untuk $x \ge 4$ adalah:
$$R_f = \{y \in \mathbb{R} \mid y \le 4\}$$
Berdasarkan sifat fungsi invers, daerah asal fungsi invers sama dengan daerah hasil fungsi asalnya:
$$D_{f^{-1}} = R_f = \{x \in \mathbb{R} \mid x \le 4\}$$
Jadi, $k = 4$ dan $D_{f^{-1}} = \{x \in \mathbb{R} \mid x \le 4\}$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b01-c-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: titik potong grafik fungsi dan inversnya*

Grafik fungsi linear $f(x) = \frac{3}{4}x + 2$ memotong grafik fungsi inversnya, yaitu $y = f^{-1}(x)$, pada sebuah titik koordinat $(p, q)$. Nilai dari hasil kali $p \cdot q$ adalah ....

- A. -64  
  <sub>Salah: Siswa salah tanda saat memindahkan ruas aljabar sehingga mendapatkan titik potong $(-8, 8)$.</sub>
- **B. 64** ✅  
  <sub>Benar: Grafik fungsi dan fungsi inversnya saling memotong di garis $y = x$. Menyelesaikan $\frac{3}{4}x + 2 = x$ memberikan $\frac{1}{4}x = 2 \iff x = 8$. Maka titik potongnya adalah $(8, 8)$ sehingga $p = 8$ dan $q = 8$. Hasil kali $p \cdot q = 8 \cdot 8 = 64$.</sub>
- C. 32  
  <sub>Salah: Siswa melakukan kesalahan perhitungan kelipatan atau menghitung $8 \times 4$.</sub>
- D. 16  
  <sub>Salah: Siswa menjumlahkan koordinat titik potong $p + q = 8 + 8 = 16$ alih-alih mengalikannya.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan fungsi invers $f^{-1}(x)$:
$$y = \frac{3}{4}x + 2$$
$$y - 2 = \frac{3}{4}x$$
$$x = \frac{4}{3}(y - 2) = \frac{4}{3}y - \frac{8}{3}$$
Sehingga rumus fungsi inversnya adalah $f^{-1}(x) = \frac{4}{3}x - \frac{8}{3}$.

Langkah 2: Menentukan titik potong kedua grafik:
Karena grafik $f(x)$ dan $f^{-1}(x)$ merupakan pencerminan terhadap garis $y = x$, maka titik potongnya memenuhi $f(x) = x$:
$$\frac{3}{4}x + 2 = x$$
$$2 = x - \frac{3}{4}x$$
$$2 = \frac{1}{4}x$$
$$x = 8$$
Karena titik berada pada garis $y = x$, maka nilai $y = 8$.
Titik potongnya adalah $(p, q) = (8, 8)$.

Langkah 3: Menghitung hasil kali $p \cdot q$:
$$p \cdot q = 8 \cdot 8 = 64$$
**Acuan:** siswa — siswa hal.52

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b01-c-hard-bt01-015
*variasi (angka) | C5 | 4 langkah | jenis: karakteristik domain range invers irasional*

Tentukan fungsi invers (jika ada) dari $f(x) = \sqrt{7x - 35}$, beserta daerah asal dan daerah hasilnya.

- A. $f^{-1}(x) = \frac{x^2 - 35}{7}$, dengan daerah asal $[0, \infty)$ dan daerah hasil $[5, \infty)$  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan konstanta $-35$ melewati tanda sama dengan.</sub>
- **B. $f^{-1}(x) = \frac{x^2 + 35}{7}$, dengan daerah asal $[0, \infty)$ dan daerah hasil $[5, \infty)$** ✅  
  <sub>Benar: $y = \sqrt{7x - 35} \ge 0 \iff y^2 = 7x - 35 \iff x = \frac{y^2 + 35}{7}$. Domain $f$ adalah $x \ge 5$, range $f$ adalah $y \ge 0$. Domain $f^{-1} = \text{range } f = [0, \infty)$ dan range $f^{-1} = \text{domain } f = [5, \infty)$.</sub>
- C. $f^{-1}(x) = \frac{x^2 + 35}{7}$, dengan daerah asal $(-\infty, \infty)$ dan daerah hasil $[5, \infty)$  
  <sub>Salah: Mengabaikan pembatasan daerah asal fungsi invers yang berasal dari nilai akar yang taknegatif.</sub>
- D. $f^{-1}(x) = \frac{x^2 + 35}{7}$, dengan daerah asal $[5, \infty)$ dan daerah hasil $[0, \infty)$  
  <sub>Salah: Domain dan range fungsi invers tertukar dengan domain dan range fungsi asalnya.</sub>

**Pembahasan:** Langkah 1: Tentukan domain dan range $f(x) = \sqrt{7x - 35}$. Syarat akar $7x - 35 \ge 0 \implies x \ge 5$, sehingga domain $D_f = [5, \infty)$ dan range $R_f = [0, \infty)$.
Langkah 2: Nyatakan $x$ dalam $y$: $y = \sqrt{7x - 35} \implies y^2 = 7x - 35 \implies 7x = y^2 + 35 \implies x = \frac{y^2 + 35}{7}$.
Langkah 3: Tuliskan fungsi invers $f^{-1}(x) = \frac{x^2 + 35}{7}$.
Langkah 4: Tentukan domain dan range $f^{-1}$. $D_{f^{-1}} = R_f = [0, \infty)$ dan $R_{f^{-1}} = D_f = [5, \infty)$.
**Acuan:** pretest — kelas11-b01-p0055-latihan-15-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b01-c-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi invers linear dan titik simetri*

Diberikan fungsi linear $f(x) = -7x + 24$. Jika titik perpotongan grafik $y = f(x)$ dan grafik fungsi inversnya $y = f^{-1}(x)$ adalah $(a, b)$, maka nilai dari $a + b$ adalah ....

- **A. 6** ✅  
  <sub>Benar: Grafik $y = f(x)$ dan $y = f^{-1}(x)$ berpotongan pada garis simetri $y = x$. Maka $-7x + 24 = x \iff 8x = 24 \iff x = 3$. Didapat $a = 3$ dan $b = 3$, sehingga $a + b = 3 + 3 = 6$.</sub>
- B. 3  
  <sub>Salah: Hanya menghitung nilai absis $a = 3$ saja dan lupa menjumlahkannya dengan ordinat $b$.</sub>
- C. -6  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan suku $-7x$ ke ruas kanan menghasilkan $x = -3$.</sub>
- D. 8  
  <sub>Salah: Salah membagi pada langkah akhir $-7x - x = -24$ menghasilkan nilai yang keliru atau salah operasi $24 / 6$.</sub>

**Pembahasan:** Langkah 1: Pahami sifat bahwa grafik suatu fungsi bijektif dan inversnya selalu berpotongan pada garis $y = x$ jika keduanya memiliki titik potong riil.
Langkah 2: Substitusikan $y = x$ ke dalam persamaan fungsi: $x = -7x + 24$.
Langkah 3: Selesaikan persamaan: $8x = 24 \implies x = 3$. Titik potongnya adalah $(a, b) = (3, 3)$.
Langkah 4: Hitung nilai yang diminta: $a + b = 3 + 3 = 6$.
**Acuan:** siswa — siswa hal.55 Latihan 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11-b01-c-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: analisis parameter saling invers*

Diketahui dua fungsi linear $f(x) = \frac{4x - 9}{5}$ dan $g(x) = \frac{p x + q}{8}$ memenuhi hubungan $(f \circ g)(x) = x$ untuk setiap $x \in \mathbb{R}$. Nilai dari $p - q$ adalah ....

- A. 8  
  <sub>Salah: Terbalik dalam menghitung selisih $q - p$ alih-alih $p - q$.</sub>
- B. -4  
  <sub>Salah: Lupa mengalikan pembilang dan penyebut dengan 2 saat menyamakan penyebut menjadi 8.</sub>
- C. 28  
  <sub>Salah: Salah melakukan operasi dengan menjumlahkan $p + q$ alih-alih menghitung pengurangan $p - q$.</sub>
- **D. -8** ✅  
  <sub>Benar: Fungsi $g$ harus merupakan invers dari $f$. Dari $y = \frac{4x - 9}{5}$, diperoleh $x = \frac{5y + 9}{4} = \frac{10y + 18}{8}$. Diperoleh $p = 10$ dan $q = 18$, sehingga $p - q = 10 - 18 = -8$.</sub>

**Pembahasan:** Langkah 1: Berdasarkan teorema di Buku Siswa hal 54, karena $(f \circ g)(x) = x$, maka $g(x) = f^{-1}(x)$.
Langkah 2: Cari rumus $f^{-1}(x)$. Misalkan $y = \frac{4x - 9}{5} \implies 5y = 4x - 9 \implies 4x = 5y + 9 \implies x = \frac{5y + 9}{4}$. Jadi $f^{-1}(x) = \frac{5x + 9}{4}$.
Langkah 3: Samakan bentuk $f^{-1}(x)$ dengan $g(x)$: $g(x) = \frac{p x + q}{8} = \frac{2(5x + 9)}{2(4)} = \frac{10x + 18}{8}$. Didapat $p = 10$ dan $q = 18$.
Langkah 4: Hitung nilai $p - q = 10 - 18 = -8$.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11-b01-c-hard-bt01-018
*orisinal | C6 | 5 langkah | jenis: desain pembatasan domain parabola invers*

Fungsi kuadrat $f(x) = x^2 - 10x + 31$ didefinisikan pada daerah asal $D_f = [k, \infty)$ agar memiliki fungsi invers $f^{-1}$. Jika diketahui $f^{-1}(10) = 7$, maka batas nilai $k$ terkecil yang mungkin dan rumus fungsi invers $f^{-1}(x)$ berturut-turut adalah ....

- A. $k = 6$ dan $f^{-1}(x) = 5 + \sqrt{x - 6}$  
  <sub>Salah: Keliru menganggap nilai minimum fungsi $y = 6$ sebagai batas absis domain $k$.</sub>
- B. $k = 5$ dan $f^{-1}(x) = 5 - \sqrt{x - 6}$  
  <sub>Salah: Memilih tanda negatif pada bentuk akar yang menghasilkan cabang domain $x \le 5$ dan $f^{-1}(10) = 3$ (kontradiksi dengan syarat).</sub>
- **C. $k = 5$ dan $f^{-1}(x) = 5 + \sqrt{x - 6}$** ✅  
  <sub>Benar: Sumbu simetri $x_s = -\frac{-10}{2(1)} = 5$. Agar injektif pada $[k, \infty)$, haruslah $k \ge 5$, sehingga nilai terkecil $k = 5$. Dari $y = (x - 5)^2 + 6 \implies x - 5 = +\sqrt{y - 6} \implies x = 5 + \sqrt{y - 6}$, konsisten dengan $f^{-1}(10) = 5 + \sqrt{4} = 7$.</sub>
- D. $k = 10$ dan $f^{-1}(x) = 5 + \sqrt{x - 6}$  
  <sub>Salah: Mengira koefisien nilai masukan $x=10$ sebagai nilai pembatas sumbu simetri $k$.</sub>

**Pembahasan:** Langkah 1: Ubah $f(x)$ ke bentuk kuadrat sempurna: $f(x) = (x - 5)^2 - 25 + 31 = (x - 5)^2 + 6$.
Langkah 2: Agar fungsi kuadrat memiliki invers, kurva harus monoton murni (injektif). Titik balik berada di $x = 5$. Maka daerah asal $[k, \infty)$ mengharuskan $k \ge 5$. Nilai $k$ terkecil adalah $k = 5$.
Langkah 3: Tentukan invers dari $y = (x - 5)^2 + 6$: $(x - 5)^2 = y - 6 \implies x - 5 = \pm\sqrt{y - 6}$. Karena domain $x \ge 5$, pilih tanda positif: $x = 5 + \sqrt{y - 6}$.
Langkah 4: Uji kecocokan: $f^{-1}(10) = 5 + \sqrt{10 - 6} = 5 + 2 = 7$ (sesuai).
Langkah 5: Simpulkan $k = 5$ dan $f^{-1}(x) = 5 + \sqrt{x - 6}$.
**Acuan:** siswa — siswa hal.50

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11-b01-c-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: evaluasi invers komposisi dan parameter pecahan*

Diketahui fungsi linear $f(x) = 2x - 3$ dan fungsi pecahan $g(x) = \frac{px - 2}{x - 2}$ dengan $x \ne 2$. Jika grafik fungsi invers $(f \circ g)^{-1}(x)$ melalui titik $(11, 3)$, maka nilai dari $g^{-1}(p + 1)$ adalah ....

- A. 2  
  <sub>Salah: Siswa keliru menafsirkan sifat invers dan langsung menggunakan nilai pembuat nol penyebut fungsi $g(x)$.</sub>
- B. 5  
  <sub>Salah: Siswa keliru menghitung nilai fungsi asal $g(p + 1) = g(4) = \frac{3(4)-2}{4-2} = 5$ alih-alih menghitung nilai fungsi inversnya $g^{-1}(4)$.</sub>
- **C. 6** ✅  
  <sub>Benar: Dari $(f \circ g)^{-1}(11) = 3$, diperoleh $(f \circ g)(3) = 11$. Karena $f(g(3)) = 2g(3) - 3 = 11$, maka $g(3) = 7$. Substitusi ke rumus fungsi $g(3) = \frac{3p - 2}{3 - 2} = 7 \implies 3p - 2 = 7 \implies p = 3$. Nilai yang dicari adalah $g^{-1}(3 + 1) = g^{-1}(4)$. Jika $g^{-1}(4) = k$, maka $g(k) = 4 \implies \frac{3k - 2}{k - 2} = 4 \implies 3k - 2 = 4k - 8 \implies k = 6$.</sub>
- D. 10  
  <sub>Salah: Siswa melakukan kesalahan tanda aljabar saat menyelesaikan persamaan linear $3k - 2 = 4(k - 2)$ menjadi $-k = -10$ sehingga diperoleh $k = 10$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat fungsi invers.
Grafik $(f \circ g)^{-1}(x)$ melalui titik $(11, 3)$ berarti:
$$(f \circ g)^{-1}(11) = 3 \iff (f \circ g)(3) = 11$$

Langkah 2: Tentukan nilai $g(3)$.
$$(f \circ g)(3) = f(g(3)) = 11$$
$$2(g(3)) - 3 = 11$$
$$2(g(3)) = 14 \implies g(3) = 7$$

Langkah 3: Tentukan nilai parameter $p$.
$$g(3) = \frac{p(3) - 2}{3 - 2} = 7$$
$$3p - 2 = 7$$
$$3p = 9 \implies p = 3$$
Sehingga rumus fungsi $g(x)$ adalah $g(x) = \frac{3x - 2}{x - 2}$.

Langkah 4: Hitung nilai $g^{-1}(p + 1) = g^{-1}(4)$.
Misalkan $g^{-1}(4) = k$, maka $g(k) = 4$:
$$\frac{3k - 2}{k - 2} = 4$$
$$3k - 2 = 4(k - 2)$$
$$3k - 2 = 4k - 8$$
$$-k = -6 \implies k = 6$$

Jadi, nilai dari $g^{-1}(p + 1)$ adalah 6.
**Acuan:** siswa — siswa hal.54

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas11-b01-c-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: invers komposisi berparameter pecahan*

Diketahui fungsi linear $f(x) = 2x + 1$ dan fungsi pecahan $g(x) = \frac{ax - 1}{x - 2}$ dengan $x \ne 2$. Jika berlaku $(g \circ f)^{-1}(3) = 2$ dan $(f \circ g)^{-1}(11) = k$, maka nilai dari konstanta $k$ adalah ....

- A. 5  
  <sub>Salah: Siswa berhenti pada nilai antara $g(k) = 5$ dan langsung menganggapnya sebagai nilai $k$ tanpa menyelesaikannya ke rumus fungsi $g$.</sub>
- B. 4  
  <sub>Salah: Siswa salah melakukan manipulasi aljabar pada persamaan linear $2k - 1 = 5(k - 2)$ menjadi $2k - 1 = 5k - 13$ sehingga $3k = 12$ dan $k = 4$.</sub>
- C. 2  
  <sub>Salah: Siswa tertukar antara nilai konstanta $a$ yang bernilai 2 dengan nilai $k$ yang ditanyakan.</sub>
- **D. 3** ✅  
  <sub>Benar: Dari $(g \circ f)^{-1}(3) = 2$, diperoleh $(g \circ f)(2) = 3$. Karena $f(2) = 2(2) + 1 = 5$, maka $g(5) = 3 \implies \frac{5a - 1}{5 - 2} = 3 \implies 5a - 1 = 9 \implies a = 2$. Selanjutnya, dari $(f \circ g)^{-1}(11) = k$, diperoleh $(f \circ g)(k) = 11 \implies f(g(k)) = 11 \implies 2\cdot g(k) + 1 = 11 \implies g(k) = 5$. Persamaan $\frac{2k - 1}{k - 2} = 5$ menghasilkan $2k - 1 = 5k - 10 \implies 3k = 9 \implies k = 3$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat fungsi invers $(g \circ f)^{-1}(3) = 2 \iff (g \circ f)(2) = 3$.
Langkah 2: Hitung nilai $f(2) = 2(2) + 1 = 5$.
Langkah 3: Substitusikan ke fungsi $g$ untuk mencari $a$:
$$g(5) = 3 \implies \frac{5a - 1}{5 - 2} = 3 \implies \frac{5a - 1}{3} = 3 \implies 5a - 1 = 9 \implies 5a = 10 \implies a = 2$$
Sehingga rumus fungsi $g(x) = \frac{2x - 1}{x - 2}$.
Langkah 4: Gunakan kesetaraan invers untuk mencari $k$:
$$(f \circ g)^{-1}(11) = k \iff (f \circ g)(k) = 11 \iff f(g(k)) = 11$$
$$2\cdot g(k) + 1 = 11 \implies 2\cdot g(k) = 10 \implies g(k) = 5$$
Langkah 5: Selesaikan persamaan untuk $k$:
$$\frac{2k - 1}{k - 2} = 5 \implies 2k - 1 = 5(k - 2) \implies 2k - 1 = 5k - 10 \implies 3k = 9 \implies k = 3$$
Jadi, nilai konstanta $k$ adalah 3.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
