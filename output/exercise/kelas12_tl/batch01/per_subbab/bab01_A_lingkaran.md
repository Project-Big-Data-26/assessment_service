# Lembar koreksi — kelas12_tl SMA12L-B1 subbab A: Lingkaran

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b01-a-easy-bt01-001
*variasi (angka) | C1 | 1 langkah | jenis: Persamaan lingkaran pusat O(0,0)*

Diketahui pusat lingkaran terletak pada titik pusat $O(0,0)$. Tentukan persamaan lingkaran tersebut jika jari-jarinya $r = 2\sqrt{7}$.

- A. $x^2 + y^2 = 2\sqrt{7}$  
  <sub>Salah: Siswa lupa menguadratkan nilai $r$ pada ruas kanan rumus.</sub>
- B. $x^2 + y^2 = 14$  
  <sub>Salah: Siswa mengalikan $2 \times 7$ tanpa menguadratkan angka 2.</sub>
- **C. $x^2 + y^2 = 28$** ✅  
  <sub>Benar: Bentuk persamaan lingkaran berpusat di $O(0,0)$ adalah $x^2 + y^2 = r^2$. Dengan $r = 2\sqrt{7}$, maka $r^2 = (2\sqrt{7})^2 = 4 \times 7 = 28$, sehingga persamaannya $x^2 + y^2 = 28$.</sub>
- D. $x^2 + y^2 = 56$  
  <sub>Salah: Siswa menguadratkan $2\sqrt{7}$ lalu mengalikannya dengan 2.</sub>

**Pembahasan:** Persamaan lingkaran yang berpusat di titik $O(0,0)$ dan berjari-jari $r$ adalah:
$$x^2 + y^2 = r^2$$
Diketahui $r = 2\sqrt{7}$, sehingga:
$$r^2 = (2\sqrt{7})^2 = 4 \times 7 = 28$$
Jadi, persamaan lingkaran tersebut adalah $x^2 + y^2 = 28$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b01-a-easy-bt01-002
*variasi (angka) | C2 | 1 langkah | jenis: Bentuk baku persamaan lingkaran*

Diketahui sebuah lingkaran berpusat di titik $P(3, -5)$ dan berjari-jari $r = 7$. Bentuk baku persamaan lingkaran tersebut adalah ....

- A. $(x - 3)^2 + (y - 5)^2 = 49$  
  <sub>Salah: Siswa salah memperlakukan tanda negatif pada ordinat pusat lingkaran.</sub>
- B. $(x + 3)^2 + (y - 5)^2 = 49$  
  <sub>Salah: Siswa terbalik memasukkan tanda koordinat titik pusat lingkaran.</sub>
- C. $(x - 3)^2 + (y + 5)^2 = 7$  
  <sub>Salah: Siswa lupa menguadratkan nilai jari-jari $r$.</sub>
- **D. $(x - 3)^2 + (y + 5)^2 = 49$** ✅  
  <sub>Benar: Bentuk baku persamaan lingkaran berpusat di $(a, b)$ dengan jari-jari $r$ adalah $(x - a)^2 + (y - b)^2 = r^2$. Untuk $(a, b) = (3, -5)$ dan $r = 7$, diperoleh $(x - 3)^2 + (y - (-5))^2 = 7^2 \Leftrightarrow (x - 3)^2 + (y + 5)^2 = 49$.</sub>

**Pembahasan:** Persamaan baku lingkaran dengan pusat $P(a, b)$ dan jari-jari $r$ dirumuskan sebagai:
$$(x - a)^2 + (y - b)^2 = r^2$$
Diketahui $a = 3$, $b = -5$, dan $r = 7$.
Substitusikan nilai-nilai tersebut ke dalam rumus:
$$(x - 3)^2 + (y - (-5))^2 = 7^2$$
$$(x - 3)^2 + (y + 5)^2 = 49$$
Jadi, bentuk baku persamaan lingkaran tersebut adalah $(x - 3)^2 + (y + 5)^2 = 49$.
**Acuan:** siswa — siswa hal.25 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b01-a-easy-bt01-003
*orisinal | C1 | 1 langkah | jenis: Definisi lingkaran*

Kurva tertutup sederhana pada bidang datar yang setiap titik pada kurva tersebut memiliki jarak yang selalu sama terhadap suatu titik tertentu dinamakan ....

- A. hiperbola  
  <sub>Salah: Siswa menebak kurva terbuka irisan kerucut lainnya.</sub>
- B. parabola  
  <sub>Salah: Siswa keliru membedakan irisan kerucut yang memiliki satu titik pusat dengan irisan kerucut berpuncak dan berdirektriks.</sub>
- **C. lingkaran** ✅  
  <sub>Benar: Berdasarkan definisi pada buku teks, kurva tertutup sederhana dengan ciri semua titik pada kurva berjarak sama terhadap titik tertentu (titik pusat) adalah lingkaran.</sub>
- D. elips  
  <sub>Salah: Siswa keliru menganggap elips memiliki jarak yang selalu sama terhadap satu titik pusat, padahal jumlah jarak ke dua titik fokuslah yang tetap.</sub>

**Pembahasan:** Menurut definisi geometri pada buku teks, lingkaran adalah kurva tertutup sederhana dengan ciri semua titik pada kurva tersebut memiliki jarak yang selalu sama terhadap suatu titik tertentu. Jarak yang sama tersebut disebut jari-jari dan titik tertentu disebut titik pusat.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b01-a-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: Menentukan jari-jari lingkaran*

Sebuah lingkaran memiliki persamaan $x^2 + y^2 = 81$. Panjang diameter lingkaran tersebut adalah ....

- **A. $18$** ✅  
  <sub>Benar: Persamaan $x^2 + y^2 = r^2$ menghasilkan $r^2 = 81$, sehingga $r = 9$. Panjang diameter lingkaran adalah $d = 2r = 2 \times 9 = 18$.</sub>
- B. $40,5$  
  <sub>Salah: Siswa langsung membagi 81 dengan 2 tanpa menarik akar kuadrat terlebih dahulu.</sub>
- C. $36$  
  <sub>Salah: Siswa menarik akar kuadrat secara keliru atau salah mengalikan nilai jari-jari.</sub>
- D. $9$  
  <sub>Salah: Siswa hanya menghitung panjang jari-jari ($r = 9$) dan lupa mengalikannya dengan 2 untuk mendapatkan diameter.</sub>

**Pembahasan:** Persamaan lingkaran $x^2 + y^2 = 81$ berpusat di $O(0,0)$ dengan jari-jari $r$ memenuhi:
$$r^2 = 81 \implies r = \sqrt{81} = 9$$
Diameter lingkaran ($d$) memiliki panjang dua kali jari-jari:
$$d = 2r = 2 \times 9 = 18$$
Jadi, panjang diameter lingkaran tersebut adalah 18.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b01-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: Persamaan lingkaran diketahui pusat dan diameter*

Pusat suatu lingkaran berada pada titik $P(4, -3)$ dan memiliki diameter $d = 10$. Persamaan lingkaran tersebut adalah ....

- A. $(x + 4)^2 + (y - 3)^2 = 25$  
  <sub>Salah: Tertukar tanda koordinat titik pusat lingkaran saat dimasukkan ke dalam bentuk baku.</sub>
- **B. $(x - 4)^2 + (y + 3)^2 = 25$** ✅  
  <sub>Benar: Jari-jari lingkaran adalah $r = \frac{d}{2} = 5$. Persamaan lingkaran berpusat di $(a, b) = (4, -3)$ dengan jari-jari $r = 5$ adalah $(x - 4)^2 + (y - (-3))^2 = 5^2 \Leftrightarrow (x - 4)^2 + (y + 3)^2 = 25$.</sub>
- C. $(x - 4)^2 + (y + 3)^2 = 100$  
  <sub>Salah: Lupa membagi dua diameter sehingga menggunakan nilai diameter langsung sebagai jari-jari ($10^2 = 100$).</sub>
- D. $(x - 4)^2 + (y + 3)^2 = 5$  
  <sub>Salah: Lupa menguadratkan nilai jari-jari pada ruas kanan persamaan.</sub>

**Pembahasan:** Diketahui pusat lingkaran $P(a, b) = P(4, -3)$ dan diameter $d = 10$.
Jari-jari lingkaran:
$r = \frac{d}{2} = \frac{10}{2} = 5$

Bentuk baku persamaan lingkaran dengan pusat $(a, b)$ dan jari-jari $r$:
$(x - a)^2 + (y - b)^2 = r^2$
$(x - 4)^2 + (y - (-3))^2 = 5^2$
$(x - 4)^2 + (y + 3)^2 = 25$
**Acuan:** siswa — siswa hal.26 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b01-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: Persamaan lingkaran pusat O melalui titik*

Diketahui pusat lingkaran terletak pada titik pusat $O(0, 0)$. Tentukan persamaan lingkaran tersebut jika lingkaran melalui titik $K(-4, 7)$.

- A. $x^2 + y^2 = 33$  
  <sub>Salah: Salah menghitung $(-4)^2$ menjadi $-16$, sehingga $r^2 = -16 + 49 = 33$.</sub>
- B. $x^2 + y^2 = 11$  
  <sub>Salah: Menjumlahkan nilai mutlak koordinat bukannya menjumlahkan kuadrat koordinat ($4 + 7 = 11$).</sub>
- C. $x^2 + y^2 = \sqrt{65}$  
  <sub>Salah: Menuliskan nilai jari-jari $r = \sqrt{65}$ pada ruas kanan, bukan $r^2$.</sub>
- **D. $x^2 + y^2 = 65$** ✅  
  <sub>Benar: Nilai $r^2 = x_1^2 + y_1^2 = (-4)^2 + 7^2 = 16 + 49 = 65$, sehingga persamaannya adalah $x^2 + y^2 = 65$.</sub>

**Pembahasan:** Persamaan lingkaran yang berpusat di $O(0, 0)$ adalah $x^2 + y^2 = r^2$.
Karena lingkaran melalui titik $K(-4, 7)$, substitusikan $x = -4$ dan $y = 7$:
$r^2 = (-4)^2 + 7^2 = 16 + 49 = 65$

Jadi, persamaan lingkaran tersebut adalah $x^2 + y^2 = 65$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b01-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: Menentukan pusat dan jari-jari dari bentuk umum*

Sebuah lingkaran memiliki persamaan $x^2 + y^2 - 6x + 10y + 9 = 0$. Titik pusat dan jari-jari lingkaran tersebut berturut-turut adalah ....

- A. pusat $(-3, 5)$ dan jari-jari $5$  
  <sub>Salah: Lupa mengalikan tanda negatif saat menentukan koordinat titik pusat dari nilai A dan B.</sub>
- B. pusat $(3, -5)$ dan jari-jari $\sqrt{43}$  
  <sub>Salah: Salah rumus jari-jari dengan menjumlahkan konstanta $C$ bukannya mengurangkan ($9 + 25 + 9 = 43$).</sub>
- **C. pusat $(3, -5)$ dan jari-jari $5$** ✅  
  <sub>Benar: Pusat lingkaran adalah $\left(-\frac{A}{2}, -\frac{B}{2}\right) = (3, -5)$ dan jari-jari $r = \sqrt{3^2 + (-5)^2 - 9} = \sqrt{25} = 5$.</sub>
- D. pusat $(-6, 10)$ dan jari-jari $25$  
  <sub>Salah: Menggunakan koefisien $A$ dan $B$ langsung sebagai pusat tanpa membaginya dengan $-2$, serta lupa menarik akar pada nilai kuadrat jari-jari.</sub>

**Pembahasan:** Dari persamaan $x^2 + y^2 - 6x + 10y + 9 = 0$, diperoleh $A = -6$, $B = 10$, dan $C = 9$.
Titik pusat $(a, b)$:
$a = -\frac{A}{2} = -\frac{-6}{2} = 3$
$b = -\frac{B}{2} = -\frac{10}{2} = -5$
Jadi, pusatnya adalah $(3, -5)$.

Jari-jari lingkaran $r$:
$r = \sqrt{a^2 + b^2 - C} = \sqrt{3^2 + (-5)^2 - 9} = \sqrt{9 + 25 - 9} = \sqrt{25} = 5$.

Jadi, lingkaran tersebut berpusat di $(3, -5)$ dan berjari-jari $5$.
**Acuan:** siswa — siswa hal.30 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b01-a-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: Konsep dasar unsur lingkaran*

Berdasarkan definisi lingkaran sebagai himpunan titik-titik yang berjarak sama terhadap titik tertentu pada bidang datar, jarak yang selalu sama tersebut dinamakan ....

- **A. jari-jari** ✅  
  <sub>Benar: Menurut definisi lingkaran, jarak yang selalu sama dari kurva ke titik pusat disebut jari-jari.</sub>
- B. titik pusat  
  <sub>Salah: Tertukar antara istilah jarak tetap (jari-jari) dengan titik acuan tertentu (titik pusat).</sub>
- C. diameter  
  <sub>Salah: Terkecoh dengan tali busur terpanjang yang melalui titik pusat (panjangnya dua kali jari-jari).</sub>
- D. tali busur  
  <sub>Salah: Terkecoh dengan ruas garis yang menghubungkan dua titik pada lingkaran.</sub>

**Pembahasan:** Pada definisi lingkaran, lingkaran adalah lintasan atau himpunan titik-titik yang berjarak sama terhadap suatu titik tertentu. Jarak yang selalu sama tersebut disebut jari-jari, sedangkan titik tertentu tersebut disebut titik pusat.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b01-a-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: Analisis parameter bentuk umum lingkaran*  **[warning validator]**

Pada bentuk umum persamaan lingkaran $x^2 + y^2 + Ax + By + C = 0$, jika nilai koefisien $B = 0$ dan $A \neq 0$, maka titik pusat lingkaran tersebut dipastikan terletak pada ....

- **A. sumbu-$x$** ✅  
  <sub>Benar: Koordinat pusat lingkaran adalah $(a, b) = \left(-\frac{A}{2}, -\frac{B}{2}\right)$. Jika $B = 0$, maka $b = 0$, sehingga pusat terletak pada $\left(-\frac{A}{2}, 0\right)$ yang berada pada sumbu-$x$.</sub>
- B. garis $y = x$  
  <sub>Salah: Terkecoh dengan kondisi gradien garis simetri atau anggapan nilai koordinat sama.</sub>
- C. titik asal $(0, 0)$  
  <sub>Salah: Mengira lingkaran berpusat di titik asal, padahal itu terjadi hanya jika $A = 0$ dan $B = 0$.</sub>
- D. sumbu-$y$  
  <sub>Salah: Tertukar antara kondisi $A = 0$ (ordinat pada sumbu-$y$) dengan $B = 0$.</sub>

**Pembahasan:** Titik pusat lingkaran dari bentuk umum $x^2 + y^2 + Ax + By + C = 0$ ditentukan oleh:
$P(a, b) = P\left(-\frac{A}{2}, -\frac{B}{2}\right)$

Jika nilai $B = 0$, maka koordinat ordinat pusatnya adalah:
$b = -\frac{0}{2} = 0$

Karena titik pusat memiliki ordinat $y = 0$, maka titik pusat tersebut berada pada sumbu-$x$.
**Acuan:** siswa — siswa hal.32
**Warning:** kelas12_tl-b01-a-easy-bt01-009 sangat mirip dengan kelas12_tl-b01-a-easy-bt01-019 (0.87) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b01-a-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: Identifikasi unsur lingkaran dari bentuk umum*

Titik pusat dan jari-jari dari lingkaran dengan persamaan $x^2 + y^2 + 4x - 12y - 9 = 0$ berturut-turut adalah ....

- A. pusat $(-4, 12)$ dan jari-jari $7$  
  <sub>Salah: Siswa lupa membagi nilai koefisien $A$ dan $B$ dengan $2$ saat menentukan titik pusat.</sub>
- **B. pusat $(-2, 6)$ dan jari-jari $7$** ✅  
  <sub>Benar: Dari persamaan diperoleh $A = 4$, $B = -12$, dan $C = -9$. Titik pusat adalah $(a, b) = \left(-\frac{A}{2}, -\frac{B}{2}\right) = (-2, 6)$. Jari-jari lingkaran adalah $r = \sqrt{a^2 + b^2 - C} = \sqrt{(-2)^2 + 6^2 - (-9)} = \sqrt{4 + 36 + 9} = \sqrt{49} = 7$.</sub>
- C. pusat $(-2, 6)$ dan jari-jari $5$  
  <sub>Salah: Siswa salah menjumlahkan di dalam akar karena mengurangkan nilai $C$ positif ($4 + 36 - 15 = 25$ bukannya $4 + 36 - (-9) = 49$).</sub>
- D. pusat $(2, -6)$ dan jari-jari $7$  
  <sub>Salah: Siswa lupa mengalikan koordinat pusat dengan tanda negatif saat menggunakan rumus pusat $(-A/2, -B/2)$.</sub>

**Pembahasan:** Persamaan umum lingkaran: $x^2 + y^2 + Ax + By + C = 0$.
Diketahui $A = 4$, $B = -12$, dan $C = -9$.

1. Menentukan titik pusat $(a, b)$:
$a = -\frac{A}{2} = -\frac{4}{2} = -2$
$b = -\frac{B}{2} = -\frac{-12}{2} = 6$
Jadi, titik pusatnya adalah $(-2, 6)$.

2. Menentukan jari-jari $r$:
$r = \sqrt{a^2 + b^2 - C} = \sqrt{(-2)^2 + 6^2 - (-9)} = \sqrt{4 + 36 + 9} = \sqrt{49} = 7$.

Jadi, titik pusat lingkaran adalah $(-2, 6)$ dan jari-jarinya adalah $7$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b01-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: Persamaan lingkaran koefisien tak satu*

Sebuah lingkaran memiliki persamaan $2x^2 + 2y^2 - 8x + 12y - 24 = 0$. Titik pusat lingkaran tersebut adalah ....

- A. (-2, 3)  
  <sub>Salah: Siswa benar membagi persamaan dengan 2 tetapi lupa mengalikan dengan $-1$ saat menghitung pusat lingkaran.</sub>
- B. (-4, 6)  
  <sub>Salah: Siswa langsung membagi koefisien asli dengan 2 untuk koordinat pusat tanpa mengalikan dengan $-1/2$.</sub>
- C. (4, -6)  
  <sub>Salah: Siswa langsung mengambil $(-A/2, -B/2)$ dari persamaan asli tanpa membagi kedua ruas dengan 2 terlebih dahulu.</sub>
- **D. $(2, -3)$** ✅  
  <sub>Benar: Bagi kedua ruas dengan 2 diperoleh $x^2 + y^2 - 4x + 6y - 12 = 0$. Nilai $A = -4$ dan $B = 6$, sehingga koordinat pusat adalah $(a, b) = \left(-\frac{-4}{2}, -\frac{6}{2}\right) = (2, -3)$.</sub>

**Pembahasan:** Persamaan lingkaran:
$2x^2 + 2y^2 - 8x + 12y - 24 = 0$

Bagi seluruh suku dengan $2$ agar menjadi bentuk umum $x^2 + y^2 + Ax + By + C = 0$:
$x^2 + y^2 - 4x + 6y - 12 = 0$

Diperoleh $A = -4$ dan $B = 6$.
Titik pusat lingkaran $P(a, b)$:
$a = -\frac{A}{2} = -\frac{-4}{2} = 2$
$b = -\frac{B}{2} = -\frac{6}{2} = -3$

Jadi, titik pusat lingkaran tersebut adalah $(2, -3)$.
**Acuan:** siswa — siswa hal.31 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b01-a-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: Definisi geometris lingkaran*

Lintasan suatu titik yang berjarak sama terhadap suatu titik tertentu dan terletak pada bidang datar merupakan definisi dari ....

- A. hiperbola  
  <sub>Salah: Siswa tertukar dengan hiperbola yang didefinisikan dari selisih jarak terhadap dua titik fokus.</sub>
- **B. lingkaran** ✅  
  <sub>Benar: Sesuai definisi pada buku siswa, lintasan suatu titik yang berjarak sama terhadap titik tertentu pada bidang datar adalah lingkaran.</sub>
- C. parabola  
  <sub>Salah: Siswa tertukar dengan parabola yang didefinisikan dari jarak ke titik fokus dan garis direktris.</sub>
- D. elips  
  <sub>Salah: Siswa tertukar dengan elips yang didefinisikan berdasarkan jumlah jarak terhadap dua titik fokus.</sub>

**Pembahasan:** Berdasarkan Buku Matematika Tingkat Lanjut Kelas XII, lingkaran didefinisikan sebagai lintasan suatu titik yang berjarak sama terhadap titik tertentu dan terletak pada bidang datar. Jarak yang sama tersebut adalah jari-jari dan titik tertentu tersebut adalah titik pusat.
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b01-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: Titik pusat dari bentuk baku lingkaran*

Sebuah lingkaran memiliki persamaan $(x - 7)^2 + (y + 4)^2 = 81$. Titik pusat lingkaran tersebut adalah ....

- **A. $(7, -4)$** ✅  
  <sub>Benar: Bentuk baku persamaan lingkaran adalah $(x - a)^2 + (y - b)^2 = r^2$. Dari persamaan $(x - 7)^2 + (y - (-4))^2 = 81$, diperoleh titik pusat $(a, b) = (7, -4)$.</sub>
- B. (-7, 4)  
  <sub>Salah: Siswa salah mengenali tanda pada bentuk baku dan langsung mengambil angka di dalam kurung tanpa membalik tanda.</sub>
- C. (7, 4)  
  <sub>Salah: Siswa benar pada koordinat $x$, tetapi salah tanda pada koordinat $y$.</sub>
- D. (-7, -4)  
  <sub>Salah: Siswa benar pada tanda koordinat $y$, tetapi salah tanda pada koordinat $x$.</sub>

**Pembahasan:** Bentuk baku persamaan lingkaran yang berpusat di titik $(a, b)$ dan berjari-jari $r$ adalah:
$(x - a)^2 + (y - b)^2 = r^2$

Berdasarkan persamaan $(x - 7)^2 + (y + 4)^2 = 81$:
- $x - a = x - 7 \Rightarrow a = 7$
- $y - b = y + 4 \Rightarrow b = -4$

Dengan demikian, titik pusat lingkaran adalah $(7, -4)$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b01-a-easy-bt01-014
*variasi (angka) | C1 | 1 langkah | jenis: Persamaan lingkaran sederhana pusat O*

Misalkan suatu lingkaran berpusat di $O(0, 0)$ dan berjari-jari $r = 9$. Persamaan lingkaran tersebut adalah ....

- A. $x^2 - y^2 = 81$  
  <sub>Salah: Salah tanda operasi antara $x^2$ dan $y^2$ (tertukar dengan persamaan hiperbola).</sub>
- B. $x^2 + y^2 = 9$  
  <sub>Salah: Lupa mengkuadratkan nilai jari-jari $r$.</sub>
- C. $x^2 + y^2 = 18$  
  <sub>Salah: Mengalikan jari-jari dengan 2 ($2r$) alih-alih mengkuadratkannya ($r^2$).</sub>
- **D. $x^2 + y^2 = 81$** ✅  
  <sub>Benar: Persamaan lingkaran berpusat di $O(0, 0)$ adalah $x^2 + y^2 = r^2$. Dengan $r = 9$, diperoleh $x^2 + y^2 = 9^2 = 81$.</sub>

**Pembahasan:** Persamaan lingkaran dengan pusat di titik $O(0, 0)$ dan jari-jari $r$ dirumuskan sebagai:
$$x^2 + y^2 = r^2$$
Diketahui $r = 9$, maka:
$$x^2 + y^2 = 9^2$$
$$x^2 + y^2 = 81$$
**Acuan:** siswa — siswa hal.23 Contoh Soal 1.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b01-a-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: Persamaan lingkaran diketahui diameter berpusat O*

Diketahui suatu lingkaran memiliki titik pusat $O(0, 0)$ dan diameter lingkaran $d = 6\sqrt{2}$. Persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 = 6\sqrt{2}$  
  <sub>Salah: Menyamakan ruas kanan langsung dengan nilai diameter tanpa membagi dan mengkuadratkannya.</sub>
- **B. $x^2 + y^2 = 18$** ✅  
  <sub>Benar: Jari-jari lingkaran adalah $r = \frac{d}{2} = 3\sqrt{2}$. Persamaan lingkarannya adalah $x^2 + y^2 = (3\sqrt{2})^2 = 9 \times 2 = 18$.</sub>
- C. $x^2 + y^2 = 72$  
  <sub>Salah: Langsung mengkuadratkan diameter tanpa membaginya dengan 2 terlebih dahulu.</sub>
- D. $x^2 + y^2 = 36$  
  <sub>Salah: Hanya mengkuadratkan koefisien $6$ tanpa menyertakan $\sqrt{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan jari-jari lingkaran dari diameter yang diketahui.
$$r = \frac{d}{2} = \frac{6\sqrt{2}}{2} = 3\sqrt{2}$$

Langkah 2: Menyubstitusikan $r$ ke dalam persamaan lingkaran berpusat di $O(0, 0)$.
$$x^2 + y^2 = r^2$$
$$x^2 + y^2 = (3\sqrt{2})^2 = 9 \times 2 = 18$$
**Acuan:** siswa — siswa hal.24 Ayo Mencoba 1.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b01-a-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: Menentukan pusat dan jari-jari lingkaran umum*

Titik pusat dan jari-jari dari lingkaran dengan persamaan $x^2 + y^2 - 10x - 4y - 7 = 0$ berturut-turut adalah ....

- **A. pusat $(5, 2)$ dan jari-jari $6$** ✅  
  <sub>Benar: Pusat lingkaran adalah $\left(-\frac{-10}{2}, -\frac{-4}{2}\right) = (5, 2)$ dan jari-jari $r = \sqrt{5^2 + 2^2 - (-7)} = \sqrt{25 + 4 + 7} = \sqrt{36} = 6$.</sub>
- B. pusat $(-10, -4)$ dan jari-jari $7$  
  <sub>Salah: Mengambil nilai koefisien $A$ dan $B$ langsung sebagai pusat dan mengabaikan perhitungan kuadrat untuk jari-jari.</sub>
- C. pusat $(5, 2)$ dan jari-jari $\sqrt{22}$  
  <sub>Salah: Salah tanda konstanta di dalam akar: menggunakan $+C$ ($+7$) bukan $-C$ ($-(-7)$), sehingga $\sqrt{29 - 7} = \sqrt{22}$.</sub>
- D. pusat $(-5, -2)$ dan jari-jari $6$  
  <sub>Salah: Lupa membagi koefisien dengan $-2$ (hanya membagi 2 tanpa membalik tanda).</sub>

**Pembahasan:** Dari persamaan $x^2 + y^2 - 10x - 4y - 7 = 0$, diperoleh $A = -10$, $B = -4$, dan $C = -7$.

Langkah 1: Menentukan pusat lingkaran $(a, b)$:
$$a = -\frac{A}{2} = -\frac{-10}{2} = 5$$
$$b = -\frac{B}{2} = -\frac{-4}{2} = 2$$
Jadi, pusat lingkaran adalah $(5, 2)$.

Langkah 2: Menentukan jari-jari lingkaran $r$:
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{5^2 + 2^2 - (-7)} = \sqrt{25 + 4 + 7} = \sqrt{36} = 6$$
Jadi, lingkaran berpusat di $(5, 2)$ dan berjari-jari $6$.
**Acuan:** siswa — siswa hal.31 Ayo Mencoba 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b01-a-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: Persamaan umum lingkaran dari pusat dan diameter*

Titik pusat suatu lingkaran adalah $(4, 5)$ dengan panjang diameter $6\text{ cm}$. Persamaan umum lingkaran tersebut adalah ....

- A. $x^2 + y^2 - 4x - 5y + 32 = 0$  
  <sub>Salah: Lupa mengalikan koordinat pusat dengan 2 saat ekspansi bentuk kuadrat.</sub>
- **B. $x^2 + y^2 - 8x - 10y + 32 = 0$** ✅  
  <sub>Benar: Jari-jari $r = 3\text{ cm}$. Persamaan $(x - 4)^2 + (y - 5)^2 = 3^2 \iff x^2 - 8x + 16 + y^2 - 10y + 25 = 9 \iff x^2 + y^2 - 8x - 10y + 32 = 0$.</sub>
- C. $x^2 + y^2 - 8x - 10y + 5 = 0$  
  <sub>Salah: Menggunakan diameter $d = 6$ sebagai jari-jari sehingga ruas kanan menjadi $36$, lalu $16 + 25 - 36 = 5$.</sub>
- D. $x^2 + y^2 + 8x + 10y + 32 = 0$  
  <sub>Salah: Salah tanda pada suku linear $x$ dan $y$ (menggunakan tanda positif alih-alih negatif).</sub>

**Pembahasan:** Langkah 1: Menghitung jari-jari dari diameter yang diketahui.
$$r = \frac{d}{2} = \frac{6}{2} = 3\text{ cm}$$

Langkah 2: Menulis bentuk baku dan menjabarkannya ke bentuk umum.
$$(x - 4)^2 + (y - 5)^2 = 3^2$$
$$(x^2 - 8x + 16) + (y^2 - 10y + 25) = 9$$
$$x^2 + y^2 - 8x - 10y + 41 - 9 = 0$$
$$x^2 + y^2 - 8x - 10y + 32 = 0$$
**Acuan:** siswa — siswa hal.29 Contoh Soal 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b01-a-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: Konsep tali busur terpanjang lingkaran*

Tali busur terpanjang pada suatu lingkaran yang melalui titik pusat lingkaran disebut ....

- A. jari-jari  
  <sub>Salah: Tertukar dengan ruas garis dari titik pusat ke kurva lingkaran (setengah diameter).</sub>
- B. busur  
  <sub>Salah: Tertukar dengan garis lengkung bagian dari keliling lingkaran.</sub>
- **C. diameter** ✅  
  <sub>Benar: Berdasarkan definisi pada geometri lingkaran, diameter merupakan tali busur terpanjang yang melalui titik pusat.</sub>
- D. apotema  
  <sub>Salah: Tertukar dengan jarak terpendek dari pusat lingkaran ke suatu tali busur.</sub>

**Pembahasan:** Sesuai dengan konsep unsur-unsur lingkaran, ruas garis lurus yang menghubungkan dua titik pada kurva lingkaran disebut tali busur. Tali busur terpanjang yang melalui titik pusat lingkaran dinamakan diameter.
**Acuan:** siswa — siswa hal.24

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b01-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: Karakteristik koefisien bentuk umum lingkaran*  **[warning validator]**

Pada bentuk umum persamaan lingkaran $x^2 + y^2 + Ax + By + C = 0$, jika nilai $A = 0$ dan $B \neq 0$, maka titik pusat lingkaran tersebut terletak pada ....

- A. sumbu-$x$  
  <sub>Salah: Siswa tertukar antara koefisien $A$ dengan $B$ dalam menentukan absis dan ordinat pusat.</sub>
- B. garis $y = x$  
  <sub>Salah: Siswa menduga nilai nol menyebabkan kesamaan nilai antara absis dan ordinat.</sub>
- C. titik asal $(0, 0)$  
  <sub>Salah: Siswa mengira $A = 0$ cukup untuk membuat pusat lingkaran berada di titik pusat koordinat tanpa melihat $B$.</sub>
- **D. sumbu-$y$** ✅  
  <sub>Benar: Titik pusat lingkaran adalah $P\left(-\frac{A}{2}, -\frac{B}{2}\right)$. Jika $A = 0$, maka absis pusat adalah $0$, sehingga titik pusat $(0, b)$ berada pada sumbu-$y$.</sub>

**Pembahasan:** Pusat lingkaran dari bentuk umum $x^2 + y^2 + Ax + By + C = 0$ ditentukan oleh:
$$P\left(-\frac{A}{2}, -\frac{B}{2}\right)$$
Jika $A = 0$, maka koordinat pusat menjadi:
$$P\left(0, -\frac{B}{2}\right)$$
Karena absis bernilai $0$ dan ordinat tidak nol ($B \neq 0$), titik pusat tersebut terletak pada sumbu-$y$.
**Acuan:** siswa — siswa hal.32
**Warning:** kelas12_tl-b01-a-easy-bt01-009 sangat mirip dengan kelas12_tl-b01-a-easy-bt01-019 (0.87) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b01-a-easy-bt01-020
*variasi (angka) | C2 | 1 langkah | jenis: Persamaan lingkaran dengan pusat P(a, b)*

Diketahui sebuah lingkaran berpusat di titik $P(-6, 8)$ dan berjari-jari $r = 5$. Tentukan persamaan lingkaran tersebut.

- A. $(x - 6)^2 + (y + 8)^2 = 25$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik pusat lingkaran ke dalam rumus $(x - a)^2 + (y - b)^2 = r^2$.</sub>
- B. $(x - 6)^2 + (y + 8)^2 = 10$  
  <sub>Salah: Siswa keliru tanda koordinat titik pusat serta mengalikan jari-jari dengan 2 alih-alih menguadratkannya.</sub>
- **C. $(x + 6)^2 + (y - 8)^2 = 25$** ✅  
  <sub>Benar: Bentuk baku persamaan lingkaran yang berpusat di $P(a, b)$ dengan jari-jari $r$ adalah $(x - a)^2 + (y - b)^2 = r^2$. Dengan menyubstitusikan $a = -6$, $b = 8$, dan $r = 5$, diperoleh $(x - (-6))^2 + (y - 8)^2 = 5^2 \Leftrightarrow (x + 6)^2 + (y - 8)^2 = 25$.</sub>
- D. $(x + 6)^2 + (y - 8)^2 = 5$  
  <sub>Salah: Siswa lupa menguadratkan nilai jari-jari pada ruas kanan persamaan.</sub>

**Pembahasan:** Bentuk baku persamaan lingkaran dengan titik pusat $P(a, b)$ dan jari-jari $r$ dirumuskan sebagai:
$$(x - a)^2 + (y - b)^2 = r^2$$

Diketahui:
- Titik pusat $P(-6, 8)$, sehingga $a = -6$ dan $b = 8$
- Jari-jari $r = 5$

Substitusikan nilai-nilai tersebut ke dalam rumus:
$$(x - (-6))^2 + (y - 8)^2 = 5^2$$
$$(x + 6)^2 + (y - 8)^2 = 25$$

Jadi, persamaan lingkaran tersebut adalah $(x + 6)^2 + (y - 8)^2 = 25$.
**Acuan:** siswa — siswa hal.25 Contoh Soal 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b01-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: persamaan lingkaran dari ujung diameter*

Tentukan persamaan lingkaran yang melalui titik $A(4, -1)$ dan titik $B(-2, 7)$ dengan ruas garis $AB$ adalah diameter lingkaran tersebut.

- A. $(x + 1)^2 + (y + 3)^2 = 25$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik pusat ke dalam bentuk baku persamaan lingkaran.</sub>
- **B. $(x - 1)^2 + (y - 3)^2 = 25$** ✅  
  <sub>Benar: Titik pusat lingkaran adalah titik tengah $AB$, yaitu $((4 + (-2))/2, (-1 + 7)/2) = (1, 3)$. Kuadrat jari-jari adalah $r^2 = (4 - 1)^2 + (-1 - 3)^2 = 3^2 + (-4)^2 = 25$. Jadi, persamaan lingkarannya $(x - 1)^2 + (y - 3)^2 = 25$.</sub>
- C. $(x - 1)^2 + (y - 3)^2 = 100$  
  <sub>Salah: Siswa tidak membagi diameter dengan dua sehingga menggunakan kuadrat diameter ($d^2 = 100$) sebagai $r^2$.</sub>
- D. $(x - 2)^2 + (y - 6)^2 = 25$  
  <sub>Salah: Siswa lupa membagi jumlah koordinat titik ujung diameter dengan 2 saat menentukan titik pusat.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat $P(a, b)$ dari titik tengah diameter $AB$.
$a = \frac{4 + (-2)}{2} = 1$
$b = \frac{-1 + 7}{2} = 3$
Titik pusat lingkaran adalah $P(1, 3)$.

Langkah 2: Menghitung jari-jari $r$ dari jarak titik $P(1, 3)$ ke titik $A(4, -1)$.
$r^2 = (4 - 1)^2 + (-1 - 3)^2 = 3^2 + (-4)^2 = 9 + 16 = 25$

Langkah 3: Menyusun persamaan lingkaran dengan bentuk baku $(x - a)^2 + (y - b)^2 = r^2$.
$(x - 1)^2 + (y - 3)^2 = 25$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b01-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: kombinasi unsur lingkaran*

Diketahui $P(h, k)$ dan $r$ berturut-turut menyatakan koordinat titik pusat dan jari-jari lingkaran dengan persamaan $x^2 + y^2 - 12x + 6y - 19 = 0$. Nilai dari $r + k - h$ adalah ....

- A. 5  
  <sub>Salah: Siswa salah menghitung jari-jari dengan mengurangkan konstanta positif ($36 + 9 - 19 = 26$) lalu melakukan pembulatan, atau tertukar urutan tanda operasi.</sub>
- B. 11  
  <sub>Salah: Siswa salah menentukan tanda koordinat pusat lingkaran menjadi $h = -6$ dan $k = 3$, sehingga $8 + 3 - (-6) = 17$ atau salah hitung tanda pengurangan $8 - 3 - 6$ menjadi $8 - 3 + 6 = 11$.</sub>
- C. -7  
  <sub>Salah: Siswa menghitung $r - k - h$ alih-alih $r + k - h$, yaitu $8 - (-3) - 6 = 5$ atau kesalahan tanda pada $k$ menjadi $-8 - 3 + 4$.</sub>
- **D. $-1$** ✅  
  <sub>Benar: Dari persamaan diperoleh $h = -(-12)/2 = 6$, $k = -(6)/2 = -3$, dan $r = \sqrt{6^2 + (-3)^2 - (-19)} = \sqrt{36 + 9 + 19} = \sqrt{64} = 8$. Maka $r + k - h = 8 + (-3) - 6 = -1$.</sub>

**Pembahasan:** Langkah 1: Menentukan pusat lingkaran $P(h, k)$ dari bentuk umum $x^2 + y^2 + Ax + By + C = 0$.
$A = -12$, $B = 6$, $C = -19$
$h = -\frac{A}{2} = -\frac{-12}{2} = 6$
$k = -\frac{B}{2} = -\frac{6}{2} = -3$

Langkah 2: Menghitung panjang jari-jari $r$.
$r = \sqrt{h^2 + k^2 - C} = \sqrt{6^2 + (-3)^2 - (-19)} = \sqrt{36 + 9 + 19} = \sqrt{64} = 8$

Langkah 3: Menghitung nilai $r + k - h$.
$r + k - h = 8 + (-3) - 6 = -1$.
**Acuan:** pretest — kelas12_tl-b01-p0083-uji-kompetensi-bab-1-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b01-a-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: persamaan lingkaran menyinggung sumbu*

Sebuah lingkaran berpusat di titik $P(-3, 4)$ dan menyinggung sumbu-$y$. Bentuk umum persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 + 6x - 8y + 9 = 0$  
  <sub>Salah: Siswa tertukar menggunakan ordinat pusat sebagai jari-jari ($r = 4$) sehingga $r^2 = 16$ dan konstanta menjadi $9 + 16 - 16 = 9$.</sub>
- B. $x^2 + y^2 + 6x - 8y + 25 = 0$  
  <sub>Salah: Siswa lupa mengurangkan $r^2 = 9$ dari ruas kanan sehingga konstanta menjadi $9 + 16 = 25$.</sub>
- **C. $x^2 + y^2 + 6x - 8y + 16 = 0$** ✅  
  <sub>Benar: Karena lingkaran menyinggung sumbu-$y$, jari-jari lingkaran sama dengan jarak absis pusat ke sumbu-$y$, yaitu $r = |-3| = 3$. Persamaan bentuk baku lingkaran adalah $(x + 3)^2 + (y - 4)^2 = 3^2 = 9$. Dijabarkan menjadi $x^2 + 6x + 9 + y^2 - 8y + 16 = 9 \iff x^2 + y^2 + 6x - 8y + 16 = 0$.</sub>
- D. $x^2 + y^2 - 6x + 8y + 16 = 0$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik pusat saat menyusun bentuk baku persamaan lingkaran.</sub>

**Pembahasan:** Langkah 1: Menentukan jari-jari lingkaran.
Lingkaran berpusat di titik $P(-3, 4)$ dan menyinggung sumbu-$y$, sehingga jari-jarinya adalah jarak titik pusat ke sumbu-$y$:
$r = |a| = |-3| = 3$

Langkah 2: Menyusun bentuk baku persamaan lingkaran.
$(x - (-3))^2 + (y - 4)^2 = 3^2$
$(x + 3)^2 + (y - 4)^2 = 9$

Langkah 3: Menjabarkan ke bentuk umum persamaan lingkaran.
$(x^2 + 6x + 9) + (y^2 - 8y + 16) = 9$
$x^2 + y^2 + 6x - 8y + 25 - 9 = 0$
$x^2 + y^2 + 6x - 8y + 16 = 0$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b01-a-medium-bt01-004
*orisinal | C3 | 2 langkah | jenis: parameter persamaan lingkaran*

Persamaan lingkaran $x^2 + y^2 - 4x + 6y + c = 0$ memiliki panjang jari-jari $r = 5$. Nilai konstanta $c$ pada persamaan tersebut adalah ....

- A. 38  
  <sub>Salah: Siswa menjumlahkan $13 + 25$ karena mengira rumusnya adalah $c = a^2 + b^2 + r^2$.</sub>
- B. -38  
  <sub>Salah: Siswa melakukan kesalahan tanda ganda pada rumus konstanta dan jari-jari.</sub>
- C. 12  
  <sub>Salah: Siswa melakukan kesalahan aljabar tanda saat memindahkan variabel $-c$ dan 25.</sub>
- **D. $-12$** ✅  
  <sub>Benar: Pusat lingkaran adalah $(a, b) = (2, -3)$. Rumus jari-jari adalah $r^2 = a^2 + b^2 - c$. Dengan $r = 5$, diperoleh $25 = 2^2 + (-3)^2 - c = 4 + 9 - c = 13 - c \iff c = 13 - 25 = -12$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat pusat lingkaran $(a, b)$ dari koefisien $A$ dan $B$.
$A = -4 \implies a = -\frac{-4}{2} = 2$
$B = 6 \implies b = -\frac{6}{2} = -3$

Langkah 2: Menggunakan rumus hubungan jari-jari dengan konstanta $c$.
$r = \sqrt{a^2 + b^2 - c}$
$5 = \sqrt{2^2 + (-3)^2 - c}$
Kuadratkan kedua ruas:
$25 = 4 + 9 - c$
$25 = 13 - c$
$c = 13 - 25 = -12$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b01-a-medium-bt01-005
*orisinal | C4 | 3 langkah | jenis: persamaan lingkaran dari perpotongan garis*

Titik pusat suatu lingkaran merupakan titik potong garis $2x - y = 4$ dan garis $x + y = 5$. Jika lingkaran tersebut melalui titik asal $O(0, 0)$, maka persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 - 4x - 6y = 0$  
  <sub>Salah: Siswa tertukar menentukan nilai $x$ dan $y$ saat menyelesaikan sistem persamaan garis, menghasilkan pusat $(2, 3)$.</sub>
- B. $x^2 + y^2 + 6x + 4y = 0$  
  <sub>Salah: Siswa salah mengubah tanda pusat $(3, 2)$ saat menyusun bentuk baku persamaan lingkaran.</sub>
- **C. $x^2 + y^2 - 6x - 4y = 0$** ✅  
  <sub>Benar: Eliminasi/substitusi kedua persamaan garis menghasilkan titik potong $x = 3$ dan $y = 2$, sehingga pusat lingkaran adalah $P(3, 2)$. Karena melalui $O(0, 0)$, kuadrat jari-jarinya adalah $r^2 = (0 - 3)^2 + (0 - 2)^2 = 9 + 4 = 13$. Persamaan lingkarannya $(x - 3)^2 + (y - 2)^2 = 13 \iff x^2 - 6x + 9 + y^2 - 4y + 4 = 13 \iff x^2 + y^2 - 6x - 4y = 0$.</sub>
- D. $x^2 + y^2 - 6x - 4y - 13 = 0$  
  <sub>Salah: Siswa menambahkan nilai $-r^2 = -13$ padahal konstanta $9 + 4 - 13$ habis bernilai $0$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong kedua garis sebagai titik pusat lingkaran.
$2x - y = 4$
$x + y = 5$
Jumlahkan kedua persamaan:
$3x = 9 \implies x = 3$
Substitusikan ke $x + y = 5$:
$3 + y = 5 \implies y = 2$
Pusat lingkaran adalah $P(3, 2)$.

Langkah 2: Menghitung jari-jari lingkaran yang melalui titik $O(0, 0)$.
$r^2 = (3 - 0)^2 + (2 - 0)^2 = 9 + 4 = 13$

Langkah 3: Menyusun persamaan umum lingkaran.
$(x - 3)^2 + (y - 2)^2 = 13$
$x^2 - 6x + 9 + y^2 - 4y + 4 = 13$
$x^2 + y^2 - 6x - 4y = 0$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b01-a-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: syarat keberadaan lingkaran*

Tentukan batas-batas nilai $m$ agar persamaan $x^2 + y^2 - 4x + my + 13 = 0$ merepresentasikan suatu lingkaran nyata.

- A. $m < -12$ atau $m > 12$  
  <sub>Salah: Siswa lupa membagi nilai $B$ dengan 2 ketika menghitung titik pusat sehingga memperoleh $m^2 - 9 > 0$ dan salah menghitung akarnya.</sub>
- B. $-6 < m < 6$  
  <sub>Salah: Siswa salah menyelesaikan pertidaksamaan kuadrat $m^2 > 36$ menjadi interval tertutup $-6 < m < 6$.</sub>
- C. $m < -3$ atau $m > 3$  
  <sub>Salah: Siswa lupa mengalikan kembali dengan 4 saat memindahkan $-9$ ke ruas kanan sehingga menganggap $m^2 > 9$.</sub>
- **D. $m < -6$ atau $m > 6$** ✅  
  <sub>Benar: Bentuk umum lingkaran $x^2 + y^2 + Ax + By + C = 0$ bernilai nyata jika kuadrat jari-jarinya $r^2 > 0$. Dari persamaan, diperoleh $A = -4$, $B = m$, dan $C = 13$. Maka $r^2 = \left(-\frac{A}{2}\right)^2 + \left(-\frac{B}{2}\right)^2 - C = 2^2 + \left(-\frac{m}{2}\right)^2 - 13 = 4 + \frac{m^2}{4} - 13 = \frac{m^2}{4} - 9$. Syarat lingkaran nyata adalah $\frac{m^2}{4} - 9 > 0 \iff m^2 > 36 \iff m < -6$ atau $m > 6$.</sub>

**Pembahasan:** Diketahui persamaan $x^2 + y^2 - 4x + my + 13 = 0$ dengan $A = -4$, $B = m$, dan $C = 13$.

Syarat agar suatu persamaan kuadrat dua variabel membentuk lingkaran nyata adalah $r^2 > 0$:
$$\left(-\frac{A}{2}\right)^2 + \left(-\frac{B}{2}\right)^2 - C > 0$$
$$\left(-\frac{-4}{2}\right)^2 + \left(-\frac{m}{2}\right)^2 - 13 > 0$$
$$2^2 + \frac{m^2}{4} - 13 > 0$$
$$4 + \frac{m^2}{4} - 13 > 0$$
$$\frac{m^2}{4} - 9 > 0$$
$$\frac{m^2}{4} > 9$$
$$m^2 > 36$$
$$m < -6 \text{ atau } m > 6$$

Jadi, batas nilai $m$ adalah $m < -6$ atau $m > 6$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b01-a-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: unsur lingkaran bentuk tak baku*

Sebuah lingkaran memiliki persamaan $4x^2 + 4y^2 - 24x + 32y - 44 = 0$. Titik pusat dan panjang jari-jari lingkaran tersebut berturut-turut adalah ....

- A. pusat $(3, -4)$ dan jari-jari $\sqrt{14}$  
  <sub>Salah: Siswa salah memasukkan tanda suku konstanta menjadi $9 + 16 - 11 = 14$ alih-alih dikurangi $-11$.</sub>
- B. pusat $(-3, 4)$ dan jari-jari $6$  
  <sub>Salah: Siswa salah tanda saat menentukan titik pusat dari nilai koefisien $A$ dan $B$.</sub>
- **C. pusat $(3, -4)$ dan jari-jari $6$** ✅  
  <sub>Benar: Persamaan dibagi 4 menjadi $x^2 + y^2 - 6x + 8y - 11 = 0$. Diperoleh $A = -6$, $B = 8$, dan $C = -11$. Titik pusatnya $\left(-\frac{-6}{2}, -\frac{8}{2}\right) = (3, -4)$. Panjang jari-jari $r = \sqrt{3^2 + (-4)^2 - (-11)} = \sqrt{9 + 16 + 11} = \sqrt{36} = 6$.</sub>
- D. pusat $(12, -16)$ dan jari-jari $6$  
  <sub>Salah: Siswa lupa membagi persamaan dengan 4 sebelum mencari koordinat titik pusat.</sub>

**Pembahasan:** Bentuk umum persamaan lingkaran mensyaratkan koefisien $x^2$ dan $y^2$ bernilai $1$. Oleh karena itu, bagi kedua ruas persamaan dengan $4$:
$$\frac{4x^2 + 4y^2 - 24x + 32y - 44}{4} = 0$$
$$x^2 + y^2 - 6x + 8y - 11 = 0$$

Dari bentuk $x^2 + y^2 + Ax + By + C = 0$, diperoleh:
$$A = -6, \quad B = 8, \quad C = -11$$

1. Menentukan titik pusat $P(a, b)$:
$$a = -\frac{A}{2} = -\frac{-6}{2} = 3$$
$$b = -\frac{B}{2} = -\frac{8}{2} = -4$$
Jadi, titik pusatnya adalah $(3, -4)$.

2. Menentukan panjang jari-jari $r$:
$$r = \sqrt{a^2 + b^2 - C}$$
$$r = \sqrt{3^2 + (-4)^2 - (-11)}$$
$$r = \sqrt{9 + 16 + 11} = \sqrt{36} = 6$$

Jadi, lingkaran tersebut berpusat di $(3, -4)$ dan berjari-jari $6$.
**Acuan:** siswa — siswa hal.31 Ayo Mencoba 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b01-a-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: persamaan lingkaran konsentris*

Suatu lingkaran konsentris (memiliki titik pusat yang sama) dengan lingkaran $x^2 + y^2 - 4x + 8y - 5 = 0$. Jika lingkaran baru tersebut melalui titik $A(7, 8)$, persamaan bentuk baku lingkaran baru tersebut adalah ....

- A. $(x - 2)^2 + (y + 4)^2 = 25$  
  <sub>Salah: Siswa memakai nilai $r^2$ dari lingkaran awal ($r^2 = 2^2 + (-4)^2 - (-5) = 25$) alih-alih menghitung jarak ke titik yang dilalui.</sub>
- B. $(x - 2)^2 + (y + 4)^2 = 13$  
  <sub>Salah: Siswa tidak mengkuadratkan nilai jari-jari pada ruas kanan persamaan baku ($r = 13$ bukan $r^2$).</sub>
- **C. $(x - 2)^2 + (y + 4)^2 = 169$** ✅  
  <sub>Benar: Pusat lingkaran acuan diperoleh dari $-\frac{A}{2} = 2$ dan $-\frac{B}{2} = -4$, sehingga pusatnya $P(2, -4)$. Jari-jari lingkaran baru dihitung dari kuadrat jarak titik $P(2, -4)$ ke titik $A(7, 8)$: $r^2 = (7 - 2)^2 + (8 - (-4))^2 = 5^2 + 12^2 = 25 + 144 = 169$. Maka persamaan bentuk bakunya adalah $(x - 2)^2 + (y + 4)^2 = 169$.</sub>
- D. $(x + 2)^2 + (y - 4)^2 = 169$  
  <sub>Salah: Siswa keliru memasukkan tanda koordinat titik pusat ke dalam bentuk baku $(x - a)^2 + (y - b)^2 = r^2$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat lingkaran acuan $x^2 + y^2 - 4x + 8y - 5 = 0$.
$$A = -4, \quad B = 8$$
$$a = -\frac{-4}{2} = 2, \quad b = -\frac{8}{2} = -4$$
Pusat lingkaran adalah $P(2, -4)$. Karena lingkaran baru konsentris, pusat lingkaran baru juga $P(2, -4)$.

Langkah 2: Menghitung jari-jari lingkaran baru yang melalui titik $A(7, 8)$.
$$r^2 = (x_A - a)^2 + (y_A - b)^2$$
$$r^2 = (7 - 2)^2 + (8 - (-4))^2 = 5^2 + 12^2 = 25 + 144 = 169$$

Langkah 3: Menyusun bentuk baku persamaan lingkaran baru.
$$(x - a)^2 + (y - b)^2 = r^2$$
$$(x - 2)^2 + (y + 4)^2 = 169$$
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b01-a-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: luas daerah lingkaran*

Sebuah lingkaran memiliki persamaan $x^2 + y^2 + 6x - 10y - 2 = 0$. Luas daerah yang dibatasi oleh lingkaran tersebut adalah ....

- A. $12\pi\text{ satuan luas}$  
  <sub>Salah: Siswa menghitung keliling lingkaran ($2\pi r = 12\pi$) alih-alih luas lingkaran.</sub>
- B. $6\pi\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengkuadratkan nilai jari-jari saat menggunakan rumus luas lingkaran.</sub>
- **C. $36\pi\text{ satuan luas}$** ✅  
  <sub>Benar: Dari persamaan, $A = 6$, $B = -10$, dan $C = -2$. Jari-jari lingkaran adalah $r = \sqrt{\left(-\frac{6}{2}\right)^2 + \left(-\frac{-10}{2}\right)^2 - (-2)} = \sqrt{(-3)^2 + 5^2 + 2} = \sqrt{9 + 25 + 2} = \sqrt{36} = 6$. Luas daerah lingkaran adalah $L = \pi r^2 = \pi (6^2) = 36\pi\text{ satuan luas}$.</sub>
- D. $32\pi\text{ satuan luas}$  
  <sub>Salah: Siswa salah operasi tanda pada konstanta $C$, menghitung $9 + 25 - 2 = 32$ sehingga menghasilkan luas $32\pi$.</sub>

**Pembahasan:** Langkah 1: Menentukan panjang jari-jari lingkaran.
Dari persamaan $x^2 + y^2 + 6x - 10y - 2 = 0$, diperoleh $A = 6$, $B = -10$, dan $C = -2$.
$$a = -\frac{6}{2} = -3$$
$$b = -\frac{-10}{2} = 5$$
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{(-3)^2 + 5^2 - (-2)} = \sqrt{9 + 25 + 2} = \sqrt{36} = 6$$

Langkah 2: Menghitung luas daerah lingkaran.
$$\text{Luas} = \pi r^2 = \pi (6)^2 = 36\pi\text{ satuan luas}$$
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b01-a-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: transformasi lingkaran*

Diketahui lingkaran $L_1 \equiv x^2 + y^2 - 10x - 4y - 20 = 0$. Dibuat lingkaran kedua $L_2$ dengan titik pusat merupakan hasil pencerminan titik pusat $L_1$ terhadap sumbu-$y$, sedangkan jari-jarinya diperbesar menjadi dua kali jari-jari $L_1$. Persamaan lingkaran $L_2$ adalah ....

- **A. $(x + 5)^2 + (y - 2)^2 = 196$** ✅  
  <sub>Benar: Pusat $L_1$ adalah $(-\frac{-10}{2}, -\frac{-4}{2}) = (5, 2)$ dan $r_1 = \sqrt{5^2 + 2^2 - (-20)} = \sqrt{49} = 7$. Pencerminan $(5, 2)$ terhadap sumbu-$y$ menghasilkan pusat $(-5, 2)$. Jari-jari baru $r_2 = 2 \times 7 = 14$, sehingga persamaannya $(x + 5)^2 + (y - 2)^2 = 14^2 = 196$.</sub>
- B. $(x + 5)^2 + (y - 2)^2 = 28$  
  <sub>Salah: Siswa mengalikan jari-jari dengan 2 menjadi 14 tetapi lupa menguadratkannya pada ruas kanan ($2 \times 14 = 28$).</sub>
- C. $(x - 5)^2 + (y + 2)^2 = 196$  
  <sub>Salah: Siswa mencerminkan pusat terhadap sumbu-$x$ bukan sumbu-$y$, sehingga koordinat pusat menjadi $(5, -2)$.</sub>
- D. $(x - 5)^2 + (y - 2)^2 = 196$  
  <sub>Salah: Siswa tidak mengubah koordinat pusat hasil pencerminan terhadap sumbu-$y$.</sub>

**Pembahasan:** Langkah 1: Menentukan pusat dan jari-jari $L_1$.
$A = -10, B = -4, C = -20$.
Pusat $P_1(a, b) = (5, 2)$.
Jari-jari $r_1 = \sqrt{5^2 + 2^2 - (-20)} = \sqrt{25 + 4 + 20} = \sqrt{49} = 7$.

Langkah 2: Menentukan unsur lingkaran $L_2$.
Titik pusat $P_1(5, 2)$ dicerminkan terhadap sumbu-$y$ menghasilkan $P_2(-5, 2)$.
Jari-jari $r_2 = 2 \times r_1 = 2 \times 7 = 14$.

Langkah 3: Menyusun persamaan $L_2$.
$(x - (-5))^2 + (y - 2)^2 = 14^2$
$(x + 5)^2 + (y - 2)^2 = 196$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b01-a-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: translasi lingkaran*

Diketahui lingkaran $L$ berpusat di titik $P(1, -3)$ dan melalui titik $A(5, 0)$. Jika lingkaran $L$ digeser ke kiri sejauh 4 satuan dan digeser ke atas sejauh 6 satuan, persamaan lingkaran hasil pergeseran tersebut adalah ....

- **A. $(x + 3)^2 + (y - 3)^2 = 25$** ✅  
  <sub>Benar: Jari-jari kuadrat: $r^2 = (5 - 1)^2 + (0 - (-3))^2 = 4^2 + 3^2 = 25$. Pusat awal $(1, -3)$ digeser $(-4, +6)$ menghasilkan pusat baru $(1 - 4, -3 + 6) = (-3, 3)$. Persamaan lingkaran menjadi $(x - (-3))^2 + (y - 3)^2 = 25 \implies (x + 3)^2 + (y - 3)^2 = 25$.</sub>
- B. $(x + 3)^2 + (y - 3)^2 = 5$  
  <sub>Salah: Siswa menuliskan $r = 5$ pada ruas kanan, bukan $r^2$.</sub>
- C. $(x - 5)^2 + (y + 9)^2 = 25$  
  <sub>Salah: Siswa terbalik menerapkan arah pergeseran (ke kiri ditambah 4, ke atas dikurang 6 sehingga pusat $(5, -9)$).</sub>
- D. $(x - 3)^2 + (y + 3)^2 = 25$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat pusat $(-3, 3)$ ke dalam bentuk $(x - a)^2 + (y - b)^2$.</sub>

**Pembahasan:** Langkah 1: Menentukan jari-jari lingkaran $L$.
$r^2 = (x_A - x_P)^2 + (y_A - y_P)^2 = (5 - 1)^2 + (0 - (-3))^2 = 4^2 + 3^2 = 25$.
Maka $r = 5$.

Langkah 2: Menentukan koordinat pusat setelah pergeseran.
Pusat awal $P(1, -3)$.
Pergeseran ke kiri 4 satuan dan ke atas 6 satuan:
$P'(1 - 4, -3 + 6) = P'(-3, 3)$.

Langkah 3: Menyusun persamaan lingkaran baru.
$(x - (-3))^2 + (y - 3)^2 = r^2$
$(x + 3)^2 + (y - 3)^2 = 25$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b01-a-medium-bt01-012
*variasi (angka) | C4 | 3 langkah | jenis: lingkaran dalam persegi*

Sebuah persegi $ABCD$ memiliki titik-titik sudut $A(-2, -3)$, $B(6, -3)$, $C(6, 5)$, dan $D(-2, 5)$. Persamaan lingkaran yang menyinggung keempat sisi persegi tersebut adalah ....

- A. $(x - 2)^2 + (y - 1)^2 = 64$  
  <sub>Salah: Siswa menggunakan panjang sisi penuh $s = 8$ sebagai jari-jari sehingga $r^2 = 64$.</sub>
- **B. $(x - 2)^2 + (y - 1)^2 = 16$** ✅  
  <sub>Benar: Panjang sisi persegi $s = 6 - (-2) = 8$. Titik pusat lingkaran adalah titik potong diagonal atau titik tengah persegi: $(\frac{-2 + 6}{2}, \frac{-3 + 5}{2}) = (2, 1)$. Jari-jari lingkaran dalam adalah $r = \frac{s}{2} = \frac{8}{2} = 4$. Persamaan lingkaran adalah $(x - 2)^2 + (y - 1)^2 = 4^2 = 16$.</sub>
- C. $(x + 2)^2 + (y + 1)^2 = 16$  
  <sub>Salah: Siswa salah tanda saat menyubstitusikan koordinat pusat $(2, 1)$ ke persamaan baku.</sub>
- D. $(x - 2)^2 + (y - 1)^2 = 32$  
  <sub>Salah: Siswa menggunakan jari-jari lingkaran luar (lingkaran yang melalui keempat titik sudut, $r^2 = 32$) bukan lingkaran dalam.</sub>

**Pembahasan:** Langkah 1: Menentukan panjang sisi persegi.
Panjang sisi $s = x_B - x_A = 6 - (-2) = 8$.

Langkah 2: Menentukan titik pusat dan jari-jari lingkaran.
Titik pusat lingkaran berada di tengah persegi:
$P(a, b) = \left(\frac{-2 + 6}{2}, \frac{-3 + 5}{2}\right) = (2, 1)$.
Karena lingkaran menyinggung keempat sisi persegi, jari-jarinya setengah dari panjang sisi:
$r = \frac{s}{2} = \frac{8}{2} = 4$.

Langkah 3: Menyusun persamaan lingkaran.
$(x - 2)^2 + (y - 1)^2 = 4^2$
$(x - 2)^2 + (y - 1)^2 = 16$.
**Acuan:** siswa — siswa hal.33 Latihan Soal Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b01-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: keliling lingkaran*

Sebuah lingkaran memiliki persamaan $x^2 + y^2 - 8x + 6y - 11 = 0$. Keliling lingkaran tersebut adalah ....

- **A. $12\pi\text{ satuan}$** ✅  
  <sub>Benar: Dari persamaan, $A = -8, B = 6, C = -11$. Titik pusat $P(4, -3)$. Jari-jari $r = \sqrt{4^2 + (-3)^2 - (-11)} = \sqrt{16 + 9 + 11} = \sqrt{36} = 6$. Keliling lingkaran $K = 2\pi r = 2\pi(6) = 12\pi\text{ satuan}$.</sub>
- B. $24\pi\text{ satuan}$  
  <sub>Salah: Siswa menggunakan nilai diameter $d = 12$ ke dalam rumus $2\pi d$.</sub>
- C. $36\pi\text{ satuan}$  
  <sub>Salah: Siswa menghitung luas lingkaran ($L = \pi r^2$) bukan keliling.</sub>
- D. $6\pi\text{ satuan}$  
  <sub>Salah: Siswa menggunakan rumus keliling $K = \pi r$ bukan $2\pi r$.</sub>

**Pembahasan:** Langkah 1: Menentukan pusat lingkaran $(a, b)$.
$a = -\frac{A}{2} = -\frac{-8}{2} = 4$
$b = -\frac{B}{2} = -\frac{6}{2} = -3$

Langkah 2: Menghitung jari-jari lingkaran $r$.
$r = \sqrt{a^2 + b^2 - C} = \sqrt{4^2 + (-3)^2 - (-11)} = \sqrt{16 + 9 + 11} = \sqrt{36} = 6$.

Langkah 3: Menghitung keliling lingkaran.
$K = 2\pi r = 2\pi(6) = 12\pi\text{ satuan}$.
**Acuan:** siswa — siswa hal.24

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b01-a-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: persamaan umum melalui titik*

Sebuah lingkaran berpusat di titik $P(3, -2)$ dan melalui titik $T(7, 1)$. Bentuk umum persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 + 6x - 4y - 12 = 0$  
  <sub>Salah: Siswa terbalik tanda pada koefisien $x$ dan $y$ saat ekspansi $(-2a$ dan $-2b)$.</sub>
- **B. $x^2 + y^2 - 6x + 4y - 12 = 0$** ✅  
  <sub>Benar: Jari-jari kuadrat: $r^2 = (7 - 3)^2 + (1 - (-2))^2 = 4^2 + 3^2 = 25$. Bentuk baku: $(x - 3)^2 + (y + 2)^2 = 25 \iff x^2 - 6x + 9 + y^2 + 4y + 4 - 25 = 0 \iff x^2 + y^2 - 6x + 4y - 12 = 0$.</sub>
- C. $x^2 + y^2 - 6x + 4y + 38 = 0$  
  <sub>Salah: Siswa menjumlahkan $r^2$ ke ruas kiri alih-alih mengurangkannya ($9 + 4 + 25 = 38$).</sub>
- D. $x^2 + y^2 - 6x + 4y + 12 = 0$  
  <sub>Salah: Siswa salah menghitung suku konstan: $9 + 4 - 25 = -12$, namun ditulis $+12$.</sub>

**Pembahasan:** Langkah 1: Menghitung jari-jari kuadrat ($r^2$).
$r^2 = (x_T - a)^2 + (y_T - b)^2 = (7 - 3)^2 + (1 - (-2))^2 = 4^2 + 3^2 = 16 + 9 = 25$.

Langkah 2: Menyusun bentuk baku persamaan lingkaran.
$(x - 3)^2 + (y - (-2))^2 = 25$
$(x - 3)^2 + (y + 2)^2 = 25$

Langkah 3: Menjabarkan ke bentuk umum.
$x^2 - 6x + 9 + y^2 + 4y + 4 = 25$
$x^2 + y^2 - 6x + 4y + 13 - 25 = 0$
$x^2 + y^2 - 6x + 4y - 12 = 0$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b01-a-medium-bt01-015
*variasi (angka) | C3 | 3 langkah | jenis: unsur lingkaran dari bentuk tak tereduksi*

Sebuah lingkaran memiliki persamaan $3x^2 + 3y^2 - 18x + 24y - 21 = 0$. Titik pusat dan panjang jari-jari lingkaran tersebut berturut-turut adalah ....

- A. pusat $(9, -12)$ dan jari-jari $2\sqrt{47}$  
  <sub>Salah: Siswa langsung mencari titik pusat tanpa membagi persamaan dengan 3 terlebih dahulu.</sub>
- **B. pusat $(3, -4)$ dan jari-jari $4\sqrt{2}$** ✅  
  <sub>Benar: Bagi kedua ruas dengan 3 sehingga menjadi $x^2 + y^2 - 6x + 8y - 7 = 0$. Titik pusat adalah $\left(-\frac{-6}{2}, -\frac{8}{2}\right) = (3, -4)$. Jari-jari $r = \sqrt{3^2 + (-4)^2 - (-7)} = \sqrt{9 + 16 + 7} = \sqrt{32} = 4\sqrt{2}$.</sub>
- C. pusat $(3, -4)$ dan jari-jari $3\sqrt{2}$  
  <sub>Salah: Siswa salah tanda saat memasukkan nilai $C$, menghitung $r = \sqrt{9 + 16 - 7} = \sqrt{18} = 3\sqrt{2}$.</sub>
- D. pusat $(-3, 4)$ dan jari-jari $4\sqrt{2}$  
  <sub>Salah: Siswa lupa mengalikan dengan tanda negatif pada rumus koordinat titik pusat.</sub>

**Pembahasan:** Bagi persamaan dengan $3$:
$$x^2 + y^2 - 6x + 8y - 7 = 0$$
Diperoleh $A = -6$, $B = 8$, dan $C = -7$.
1. Titik pusat:
$$P(a, b) = \left(-\frac{-6}{2}, -\frac{8}{2}\right) = (3, -4)$$
2. Jari-jari:
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{3^2 + (-4)^2 - (-7)} = \sqrt{9 + 16 + 7} = \sqrt{32} = 4\sqrt{2}$$
Jadi, pusatnya adalah $(3, -4)$ dan jari-jarinya $4\sqrt{2}$.
**Acuan:** siswa — siswa hal.31 Ayo Mencoba 1.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b01-a-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: persamaan lingkaran menyinggung garis vertikal*

Sebuah lingkaran berpusat di titik $P(5, -3)$ dan menyinggung garis vertikal $x = 1$. Bentuk umum persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 + 10x - 6y + 18 = 0$  
  <sub>Salah: Siswa tertukar tanda koordinat pusat lingkaran dalam penjabaran aljabar.</sub>
- **B. $x^2 + y^2 - 10x + 6y + 18 = 0$** ✅  
  <sub>Benar: Jari-jari lingkaran adalah jarak titik pusat $(5, -3)$ ke garis $x = 1$, yaitu $r = |5 - 1| = 4$. Persamaan baku lingkaran adalah $(x - 5)^2 + (y + 3)^2 = 4^2 = 16$. Dijabarkan menjadi $x^2 - 10x + 25 + y^2 + 6y + 9 - 16 = 0 \iff x^2 + y^2 - 10x + 6y + 18 = 0$.</sub>
- C. $x^2 + y^2 - 10x + 6y - 2 = 0$  
  <sub>Salah: Siswa salah menghitung jari-jari dengan menjumlahkan koordinat $r = 5 + 1 = 6$, sehingga $r^2 = 36$ dan $34 - 36 = -2$.</sub>
- D. $x^2 + y^2 - 10x + 6y + 34 = 0$  
  <sub>Salah: Siswa lupa mengurangkan $r^2 = 16$ ke ruas kiri, melainkan membiarkan $25 + 9 = 34$.</sub>

**Pembahasan:** 1. Jari-jari lingkaran adalah jarak horizontal dari pusat $P(5, -3)$ ke garis $x = 1$:
$$r = |5 - 1| = 4$$
2. Bentuk baku persamaan lingkaran:
$$(x - 5)^2 + (y - (-3))^2 = 4^2$$
$$(x - 5)^2 + (y + 3)^2 = 16$$
3. Jabarkan ke bentuk umum:
$$x^2 - 10x + 25 + y^2 + 6y + 9 = 16$$
$$x^2 + y^2 - 10x + 6y + 18 = 0$$
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b01-a-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: persamaan lingkaran dari kondisi garis dan garis singgung*

Sebuah lingkaran yang berpusat di kuadran I menyinggung sumbu-$y$ dan memiliki jari-jari $4$. Jika titik pusat lingkaran tersebut terletak pada garis $y = 2x$, maka bentuk baku persamaan lingkaran tersebut adalah ....

- A. $(x - 8)^2 + (y - 4)^2 = 16$  
  <sub>Salah: Siswa tertukar antara absis dan ordinat pusat lingkaran.</sub>
- B. $(x - 4)^2 + (y - 8)^2 = 4$  
  <sub>Salah: Siswa lupa menguadratkan nilai jari-jari pada ruas kanan bentuk baku.</sub>
- C. $(x - 2)^2 + (y - 4)^2 = 16$  
  <sub>Salah: Siswa menganggap $a = \frac{r}{2} = 2$ sehingga $b = 4$.</sub>
- **D. $(x - 4)^2 + (y - 8)^2 = 16$** ✅  
  <sub>Benar: Karena lingkaran menyinggung sumbu-$y$ dan berpusat di kuadran I, maka jarak pusat $(a, b)$ ke sumbu-$y$ sama dengan jari-jari, yaitu $a = r = 4$. Titik pusat terletak pada garis $y = 2x$, maka ordinat pusat adalah $b = 2(4) = 8$. Titik pusat lingkaran adalah $(4, 8)$ dan jari-jarinya $4$, sehingga persamaannya $(x - 4)^2 + (y - 8)^2 = 16$.</sub>

**Pembahasan:** 1. Karena lingkaran menyinggung sumbu-$y$ dan berpusat di kuadran I, maka absis titik pusat adalah $a = r = 4$.
2. Pusat $(a, b)$ berada pada garis $y = 2x$, sehingga ordinatnya adalah $b = 2(4) = 8$.
3. Titik pusat adalah $(4, 8)$ dan $r = 4$. Bentuk baku persamaan lingkaran adalah:
$$(x - 4)^2 + (y - 8)^2 = 4^2 \iff (x - 4)^2 + (y - 8)^2 = 16$$
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b01-a-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: jari-jari lingkaran melalui titik berparameter*

Lingkaran dengan persamaan $x^2 + y^2 - 8x + 4y + C = 0$ melalui titik $A(2, 2)$. Panjang jari-jari lingkaran tersebut adalah ....

- **A. $2\sqrt{5}$** ✅  
  <sub>Benar: Substitusikan titik $A(2, 2)$ ke persamaan lingkaran: $2^2 + 2^2 - 8(2) + 4(2) + C = 0 \iff 4 + 4 - 16 + 8 + C = 0 \iff C = 0$. Titik pusat lingkaran adalah $P\left(-\frac{-8}{2}, -\frac{4}{2}\right) = (4, -2)$. Panjang jari-jari lingkaran adalah $r = \sqrt{4^2 + (-2)^2 - C} = \sqrt{16 + 4 - 0} = \sqrt{20} = 2\sqrt{5}$.</sub>
- B. $4\sqrt{2}$  
  <sub>Salah: Siswa salah menghitung kuadrat koordinat pusat saat menghitung jari-jari.</sub>
- C. $\sqrt{10}$  
  <sub>Salah: Siswa menjumlahkan $A$ dan $B$ atau salah dalam menerapkan rumus $r = \sqrt{a^2 + b^2 - C}$.</sub>
- D. $2\sqrt{3}$  
  <sub>Salah: Siswa salah menghitung nilai $C$ menjadi $C = 8$, sehingga $r = \sqrt{20 - 8} = \sqrt{12} = 2\sqrt{3}$.</sub>

**Pembahasan:** 1. Substitusikan titik $(2, 2)$ ke dalam persamaan:
$$2^2 + 2^2 - 8(2) + 4(2) + C = 0$$
$$4 + 4 - 16 + 8 + C = 0$$
$$C = 0$$
2. Hitung pusat dan jari-jari lingkaran:
$$a = -\frac{-8}{2} = 4, \quad b = -\frac{4}{2} = -2$$
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{4^2 + (-2)^2 - 0} = \sqrt{16 + 4} = \sqrt{20} = 2\sqrt{5}$$
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b01-a-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: syarat batas lingkaran berparameter*

Tentukan batas nilai $k$ agar persamaan $x^2 + y^2 - 6x + ky + 25 = 0$ merepresentasikan sebuah lingkaran nyata.

- **A. $k < -8$ atau $k > 8$** ✅  
  <sub>Benar: Syarat lingkaran nyata adalah $r^2 > 0$. Dari persamaan diperoleh $A = -6$, $B = k$, dan $C = 25$, sehingga $r^2 = \left(-\frac{A}{2}\right)^2 + \left(-\frac{B}{2}\right)^2 - C = 3^2 + \left(-\frac{k}{2}\right)^2 - 25 = \frac{k^2}{4} - 16 > 0$. Diperoleh $k^2 > 64$, yaitu $k < -8$ atau $k > 8$.</sub>
- B. $-8 < k < 8$  
  <sub>Salah: Salah menyelesaikan pertidaksamaan $k^2 > 64$ menjadi bentuk interval tertutup $-8 < k < 8$ seolah-olah $k^2 < 64$.</sub>
- C. $k < -10$ atau $k > 10$  
  <sub>Salah: Salah menjumlahkan konstanta menjadi $9 + 25 = 34$ lalu dikurangi nilai lain atau salah perhitungan aljabar dasar.</sub>
- D. $k < -4$ atau $k > 4$  
  <sub>Salah: Lupa membagi koefisien $B$ dengan $2$ saat menghitung komponen kuadrat pusat sehingga memperoleh $k^2 - 16 > 0$.</sub>

**Pembahasan:** Bentuk umum persamaan lingkaran adalah $x^2 + y^2 + Ax + By + C = 0$.
Dari persamaan $x^2 + y^2 - 6x + ky + 25 = 0$, diperoleh $A = -6$, $B = k$, dan $C = 25$.

Lingkaran bernilai nyata jika kuadrat jari-jarinya positif ($r^2 > 0$):
$$\left(-\frac{A}{2}\right)^2 + \left(-\frac{B}{2}\right)^2 - C > 0$$
$$3^2 + \left(-\frac{k}{2}\right)^2 - 25 > 0$$
$$9 + \frac{k^2}{4} - 25 > 0$$
$$\frac{k^2}{4} - 16 > 0$$
$$\frac{k^2}{4} > 16$$
$$k^2 > 64$$
$$k < -8 \text{ atau } k > 8$$

Jadi, batas nilai $k$ agar persamaan merepresentasikan lingkaran nyata adalah $k < -8$ atau $k > 8$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b01-a-medium-bt01-020
*variasi (angka) | C3 | 3 langkah | jenis: kombinasi koordinat pusat dan jari-jari*

Diketahui $P(h, k)$ dan $r$ berturut-turut menyatakan koordinat titik pusat dan panjang jari-jari lingkaran dengan persamaan $x^2 + y^2 - 10x - 4y - 7 = 0$. Nilai dari $r + k - h$ adalah ....

- A. 9  
  <sub>Salah: Tertukar menghitung $r + h - k$ bukan $r + k - h$ ($6 + 5 - 2 = 9$).</sub>
- B. -1  
  <sub>Salah: Salah mengurangkan ordinat pusat sehingga menghitung $r - k - h$ ($6 - 2 - 5 = -1$).</sub>
- C. 13  
  <sub>Salah: Menjumlahkan seluruh komponen $r + h + k$ ($6 + 5 + 2 = 13$).</sub>
- **D. 3** ✅  
  <sub>Benar: Dari persamaan $x^2 + y^2 - 10x - 4y - 7 = 0$, diperoleh $A = -10$, $B = -4$, dan $C = -7$. Titik pusat $P(h, k) = \left(-\frac{A}{2}, -\frac{B}{2}\right) = (5, 2)$, sehingga $h = 5$ dan $k = 2$. Jari-jari lingkaran $r = \sqrt{h^2 + k^2 - C} = \sqrt{5^2 + 2^2 - (-7)} = \sqrt{25 + 4 + 7} = \sqrt{36} = 6$. Maka, nilai $r + k - h = 6 + 2 - 5 = 3$.</sub>

**Pembahasan:** Bentuk umum persamaan lingkaran adalah $x^2 + y^2 + Ax + By + C = 0$.

Dari persamaan $x^2 + y^2 - 10x - 4y - 7 = 0$, diperoleh:
- $A = -10$
- $B = -4$
- $C = -7$

1. Menentukan koordinat pusat $P(h, k)$:
$$h = -\frac{A}{2} = -\frac{-10}{2} = 5$$
$$k = -\frac{B}{2} = -\frac{-4}{2} = 2$$
Jadi, pusat lingkaran adalah $P(5, 2)$, dengan $h = 5$ dan $k = 2$.

2. Menentukan panjang jari-jari $r$:
$$r = \sqrt{h^2 + k^2 - C} = \sqrt{5^2 + 2^2 - (-7)} = \sqrt{25 + 4 + 7} = \sqrt{36} = 6$$

3. Menghitung nilai $r + k - h$:
$$r + k - h = 6 + 2 - 5 = 3$$

Jadi, nilai dari $r + k - h$ adalah 3.
**Acuan:** pretest — kelas12_tl-b01-p0083-uji-kompetensi-bab-1-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b01-a-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: transformasi persamaan lingkaran*

Diketahui lingkaran $L$ berpusat di titik $(4, -1)$ dan melalui titik $(7, 3)$. Misalkan lingkaran $L$ diputar $90^\circ$ searah jarum jam terhadap titik asal $O(0, 0)$, kemudian digeser ke kiri sejauh $3$ satuan. Persamaan lingkaran yang dihasilkan adalah ....

- A. $(x + 4)^2 + (y - 4)^2 = 25$  
  <sub>Salah: Menerapkan rumus rotasi berlawanan arah jarum jam bukannya searah jarum jam.</sub>
- B. $(x - 4)^2 + (y + 4)^2 = 25$  
  <sub>Salah: Keliru melakukan translasi ke arah kanan bukannya ke kiri.</sub>
- C. $(x + 1)^2 + (y + 4)^2 = 25$  
  <sub>Salah: Lupa menerapkan pergeseran translasi sejauh 3 satuan pada absis titik pusat.</sub>
- **D. $(x + 4)^2 + (y + 4)^2 = 25$** ✅  
  <sub>Benar: Jari-jari lingkaran adalah $\sqrt{(7-4)^2+(3-(-1))^2}=5$. Titik pusat $(4, -1)$ diputar $90^\circ$ searah jarum jam menjadi $(-1, -4)$, lalu digeser ke kiri 3 satuan menjadi $(-4, -4)$, sehingga persamaannya $(x+4)^2+(y+4)^2=25$.</sub>

**Pembahasan:** Langkah 1: Menentukan jari-jari lingkaran $L$.
Pusat lingkaran adalah $P(4, -1)$ dan melalui $(7, 3)$:
$r^2 = (7 - 4)^2 + (3 - (-1))^2 = 3^2 + 4^2 = 9 + 16 = 25$

Langkah 2: Transformasi rotasi titik pusat.
Rotasi sebesar $90^\circ$ searah jarum jam (sudut $-90^\circ$) terhadap titik asal memetakan $(x, y) \to (y, -x)$.
Maka koordinat pusat baru $P'$ adalah:
$P'(x', y') = (-1, -4)$

Langkah 3: Transformasi translasi titik pusat.
Lingkaran kemudian digeser ke kiri sejauh 3 satuan, sehingga absis berkurang 3:
$x'' = -1 - 3 = -4$
$y'' = -4$
Pusat akhir lingkaran adalah $P''(-4, -4)$.

Langkah 4: Menentukan persamaan lingkaran hasil transformasi.
Karena transformasi berupa isometri, panjang jari-jari tidak berubah ($r^2 = 25$). Persamaan lingkaran akhirnya adalah:
$(x - (-4))^2 + (y - (-4))^2 = 25 \iff (x + 4)^2 + (y + 4)^2 = 25$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b01-a-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: persamaan lingkaran berdasar simetri garis*

Sebuah lingkaran terletak di kuadran I dan menyinggung sumbu-$x$ sekaligus sumbu-$y$. Jika garis $4x - 3y = 5$ membagi lingkaran tersebut menjadi dua bagian dengan luas yang sama, maka persamaan umum lingkaran tersebut adalah ....

- A. $x^2 + y^2 - 5x - 5y + 25 = 0$  
  <sub>Salah: Koefisien suku derajat satu langsung menggunakan nilai $r$, bukan $-2r$.</sub>
- **B. $x^2 + y^2 - 10x - 10y + 25 = 0$** ✅  
  <sub>Benar: Garis pembagi memuat titik pusat $(r, r)$. Substitusi ke $4r-3r=5$ menghasilkan $r=5$, sehingga persamaan lingkarannya $(x-5)^2+(y-5)^2=25$ atau $x^2+y^2-10x-10y+25=0$.</sub>
- C. $x^2 + y^2 + 10x + 10y + 25 = 0$  
  <sub>Salah: Salah menentukan tanda koordinat pusat lingkaran yang berada di kuadran I.</sub>
- D. $x^2 + y^2 - 10x - 10y + 50 = 0$  
  <sub>Salah: Keliru tidak mengurangkan suku $r^2$ saat menjabarkan bentuk baku ke bentuk umum.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat pusat lingkaran.
Lingkaran berada di kuadran I dan menyinggung sumbu-$x$ serta sumbu-$y$, sehingga jarak dari pusat ke kedua sumbu sama dengan jari-jari $r$ ($r > 0$). Oleh karena itu, koordinat pusat lingkaran adalah $P(r, r)$.

Langkah 2: Menghubungkan garis dengan pusat lingkaran.
Berdasarkan sifat lingkaran, garis lurus yang membagi lingkaran menjadi dua bagian dengan luas yang sama adalah garis yang memuat diameter, yang berarti garis tersebut wajib melewati titik pusat lingkaran $P(r, r)$.

Langkah 3: Menghitung nilai $r$.
Substitusikan titik $(r, r)$ ke dalam persamaan garis $4x - 3y = 5$:
$4(r) - 3(r) = 5 \implies r = 5$
Dengan demikian, pusat lingkaran berada di $(5, 5)$ dan jari-jarinya adalah $r = 5$.

Langkah 4: Menentukan persamaan umum lingkaran.
Bentuk baku persamaan lingkaran:
$(x - 5)^2 + (y - 5)^2 = 5^2$
$(x^2 - 10x + 25) + (y^2 - 10y + 25) = 25$
$x^2 + y^2 - 10x - 10y + 25 = 0$.
**Acuan:** siswa — siswa hal.24

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b01-a-hard-bt01-003
*variasi (angka) | C5 | 4 langkah | jenis: transformasi dilatasi dan refleksi lingkaran*

Diketahui sebuah lingkaran $L_1 \equiv x^2 + y^2 + 10x - 4y - 7 = 0$. Dibuat lingkaran kedua $L_2$ dengan titik pusat lingkaran $L_1$ dicerminkan terhadap sumbu-$x$ dan panjang jari-jarinya diperbesar dua kali dari jari-jari $L_1$. Bentuk umum persamaan lingkaran $L_2$ adalah ....

- **A. $x^2 + y^2 + 10x + 4y - 115 = 0$** ✅  
  <sub>Benar: Pusat lingkaran $L_1$ adalah $(-5, 2)$ dan jari-jarinya $r_1 = \sqrt{(-5)^2 + 2^2 - (-7)} = \sqrt{36} = 6$. Refleksi titik pusat terhadap sumbu-$x$ menghasilkan pusat baru $(-5, -2)$. Jari-jari lingkaran baru adalah $r_2 = 2 \times 6 = 12$. Persamaan lingkaran $L_2$ adalah $(x + 5)^2 + (y + 2)^2 = 12^2 \iff x^2 + y^2 + 10x + 4y - 115 = 0$.</sub>
- B. $x^2 + y^2 + 10x - 4y - 115 = 0$  
  <sub>Salah: Lupa mencerminkan ordinat pusat lingkaran terhadap sumbu-$x$ sehingga tanda koefisien $y$ tidak berubah.</sub>
- C. $x^2 + y^2 - 10x - 4y - 115 = 0$  
  <sub>Salah: Tertukar menerapkan pencerminan terhadap sumbu-$y$ dan bukan sumbu-$x$ sehingga tanda absis yang berubah.</sub>
- D. $x^2 + y^2 + 10x + 4y + 5 = 0$  
  <sub>Salah: Lupa mengkuadratkan jari-jari baru saat menyusun persamaan lingkaran (menggunakan nilai 24 bukan 144).</sub>

**Pembahasan:** Dari persamaan $L_1 \equiv x^2 + y^2 + 10x - 4y - 7 = 0$, diperoleh $A = 10$, $B = -4$, dan $C = -7$.
1. Menentukan pusat $P_1$ dan jari-jari $r_1$:
$$P_1 = \left(-\frac{10}{2}, -\frac{-4}{2}\right) = (-5, 2)$$
$$r_1 = \sqrt{(-5)^2 + 2^2 - (-7)} = \sqrt{25 + 4 + 7} = \sqrt{36} = 6$$
2. Menentukan pusat $P_2$ hasil pencerminan terhadap sumbu-$x$:
$$P_2 = (-5, -2)$$
3. Menentukan jari-jari $r_2$:
$$r_2 = 2 \times r_1 = 2 \times 6 = 12$$
4. Menyusun persamaan lingkaran $L_2$:
$$(x - (-5))^2 + (y - (-2))^2 = 12^2$$
$$(x + 5)^2 + (y + 2)^2 = 144$$
$$x^2 + 10x + 25 + y^2 + 4y + 4 - 144 = 0$$
$$x^2 + y^2 + 10x + 4y - 115 = 0$$
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b01-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: karakteristik persamaan umum lingkaran melalui titik asal*

Diketahui persamaan $x^2 + y^2 + (m + 5)x + (m^2 - 9)y + (2m + 6) = 0$. Jika persamaan tersebut merepresentasikan sebuah lingkaran nyata yang berpusat pada sumbu-$x$, melalui titik asal $O(0, 0)$, dan memiliki panjang jari-jari bukan nol, maka panjang diameter lingkaran tersebut adalah ....

- A. $1$  
  <sub>Salah: Menjawab panjang jari-jari lingkaran, bukan panjang diameter yang ditanyakan.</sub>
- **B. $2$** ✅  
  <sub>Benar: Syarat pusat di sumbu-$x$ mengharuskan koefisien $y$ bernilai nol: $m^2 - 9 = 0 \implies m = \pm 3$. Syarat melalui titik asal mengharuskan konstanta nol: $2m + 6 = 0 \implies m = -3$. Untuk $m = -3$, persamaan menjadi $x^2 + y^2 + 2x = 0$ dengan jari-jari $r = 1$, sehingga diameter bernilai $2r = 2$.</sub>
- C. $4$  
  <sub>Salah: Keliru mengalikan nilai koefisien $x$ secara langsung sebagai diameter.</sub>
- D. $6$  
  <sub>Salah: Menggunakan nilai mutlak parameter $2|m|$ sebagai diameter lingkaran.</sub>

**Pembahasan:** 1. Agar pusat lingkaran terletak pada sumbu-$x$, maka ordinat titik pusat harus bernilai nol, yang berarti koefisien variabel $y$ bernilai nol:
$$m^2 - 9 = 0 \implies m = 3 \text{ atau } m = -3$$
2. Agar lingkaran melalui titik asal $O(0, 0)$, konstanta persamaan lingkaran harus bernilai nol:
$$2m + 6 = 0 \implies m = -3$$
3. Nilai $m$ yang memenuhi kedua kondisi tersebut adalah $m = -3$.
4. Substitusikan $m = -3$ ke persamaan lingkaran:
$$x^2 + y^2 + (-3 + 5)x + ((-3)^2 - 9)y + (2(-3) + 6) = 0$$
$$x^2 + y^2 + 2x = 0$$
5. Menentukan jari-jari lingkaran:
$$r = \sqrt{\left(-\frac{2}{2}\right)^2 + 0^2 - 0} = \sqrt{1} = 1$$
Panjang diameter lingkaran adalah $d = 2r = 2 \times 1 = 2$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b01-a-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: evaluasi parameter lingkaran menyinggung garis horizontal*

Diketahui persamaan $x^2 + y^2 - 2(a + 1)x - 4ay + 5a^2 + 2a - 8 = 0$ merepresentasikan lingkaran untuk setiap nilai real $a$. Jika lingkaran tersebut menyinggung garis horizontal $y = 10$, maka jumlah semua nilai $a$ yang memenuhi adalah ....

- A. $5$  
  <sub>Salah: Membagi dua hasil penjumlahan akar-akar tanpa memperhitungkan koefisien $2a$.</sub>
- B. $13$  
  <sub>Salah: Hanya mengambil salah satu solusi persamaan mutlak yaitu saat $2a = 13$.</sub>
- C. $8$  
  <sub>Salah: Keliru menghitung jari-jari lingkaran menjadi $r = 2$ sehingga $|2a - 10| = 2$.</sub>
- **D. $10$** ✅  
  <sub>Benar: Pusat lingkaran adalah $(a+1, 2a)$ dan jari-jarinya tetap $r = 3$. Syarat menyinggung $y = 10$ adalah $|2a - 10| = 3$, menghasilkan nilai $a_1 = 6{,}5$ dan $a_2 = 3{,}5$ dengan jumlah $10$.</sub>

**Pembahasan:** Langkah 1: Mengubah persamaan lingkaran ke bentuk kuadrat sempurna:
$x^2 - 2(a + 1)x + y^2 - 4ay = -5a^2 - 2a + 8$
$(x - (a + 1))^2 + (y - 2a)^2 = (a + 1)^2 + (2a)^2 - (5a^2 + 2a - 8)$
$= a^2 + 2a + 1 + 4a^2 - 5a^2 - 2a + 8 = 9$.

Langkah 2: Menentukan titik pusat dan jari-jari:
Titik pusat lingkaran adalah $P(a + 1, 2a)$ dan jari-jari $r = \sqrt{9} = 3$ (konstan untuk setiap nilai $a$).

Langkah 3: Menerapkan syarat menyinggung garis horizontal $y = 10$:
Jarak ordinat titik pusat ke garis $y = 10$ harus sama dengan jari-jari lingkaran:
$|2a - 10| = 3$.

Langkah 4: Menyelesaikan persamaan nilai mutlak:
$2a - 10 = 3 \implies 2a_1 = 13 \implies a_1 = 6{,}5$
$2a - 10 = -3 \implies 2a_2 = 7 \implies a_2 = 3{,}5$.

Langkah 5: Menghitung jumlah nilai-nilai $a$:
$a_1 + a_2 = 6{,}5 + 3{,}5 = 10$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b01-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: rekonstruksi persamaan lingkaran dari tali busur*

Sebuah lingkaran berpusat di titik $P(-2, 3)$. Garis vertikal $x = 1$ memotong lingkaran tersebut sehingga menghasilkan tali busur dengan panjang $8$ satuan. Bentuk umum persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 + 4x - 6y + 12 = 0$  
  <sub>Salah: Salah melakukan operasi pengurangan konstanta $4 + 9 - 25$.</sub>
- B. $x^2 + y^2 - 4x + 6y - 12 = 0$  
  <sub>Salah: Keliru tanda koefisien $x$ dan $y$ pada penjabaran titik pusat $(-2, 3)$.</sub>
- C. $x^2 + y^2 + 4x - 6y - 60 = 0$  
  <sub>Salah: Menggunakan seluruh panjang tali busur ($8$) bukan setengahnya saat menghitung teorema Pythagoras ($3^2 + 8^2 = 73$).</sub>
- **D. $x^2 + y^2 + 4x - 6y - 12 = 0$** ✅  
  <sub>Benar: Jarak pusat ke garis adalah $3$, setengah panjang tali busur adalah $4$, sehingga jari-jari kuadrat $r^2 = 3^2 + 4^2 = 25$. Bentuk umumnya adalah $x^2 + y^2 + 4x - 6y - 12 = 0$.</sub>

**Pembahasan:** Langkah 1: Menghitung jarak titik pusat ke tali busur pada garis $x = 1$:
Jarak titik pusat $P(-2, 3)$ ke garis $x = 1$ adalah $d = |1 - (-2)| = 3$ satuan.

Langkah 2: Menghitung jari-jari lingkaran menggunakan teorema Pythagoras:
Panjang tali busur adalah $8$, sehingga setengah panjangnya adalah $\frac{8}{2} = 4$.
$r^2 = d^2 + 4^2 = 3^2 + 4^2 = 9 + 16 = 25$.

Langkah 3: Menyusun bentuk baku persamaan lingkaran:
$(x - (-2))^2 + (y - 3)^2 = 25 \iff (x + 2)^2 + (y - 3)^2 = 25$.

Langkah 4: Menjabarkan ke bentuk umum:
$x^2 + 4x + 4 + y^2 - 6y + 9 = 25$
$x^2 + y^2 + 4x - 6y + 13 - 25 = 0$
$x^2 + y^2 + 4x - 6y - 12 = 0$.
**Acuan:** siswa — siswa hal.24

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b01-a-hard-bt01-007
*variasi (angka) | C5 | 4 langkah | jenis: batas parameter keberadaan lingkaran*

Tentukan batas-batas nilai $p$ agar persamaan $x^2 + y^2 + 6x + 2py + 2p + 24 = 0$ merepresentasikan sebuah lingkaran nyata.

- **A. $p < -3$ atau $p > 5$** ✅  
  <sub>Benar: Dari persamaan $x^2 + y^2 + 6x + 2py + (2p + 24) = 0$, diperoleh $A = 6$, $B = 2p$, dan $C = 2p + 24$. Titik pusat lingkaran adalah $(a, b) = \left(-\frac{A}{2}, -\frac{B}{2}\right) = (-3, -p)$. Syarat terbentuknya lingkaran nyata adalah $r^2 > 0$, yaitu $a^2 + b^2 - C > 0$. Substitusi nilai ke pertidaksamaan: $(-3)^2 + (-p)^2 - (2p + 24) > 0 \iff 9 + p^2 - 2p - 24 > 0 \iff p^2 - 2p - 15 > 0$. Pemfaktoran memberikan $(p - 5)(p + 3) > 0$. Dengan demikian, himpunan penyelesaiannya adalah $p < -3$ atau $p > 5$.</sub>
- B. $-5 < p < 3$  
  <sub>Salah: Salah memfaktorkan sekaligus salah menentukan daerah pertidaksamaan kuadrat.</sub>
- C. $-3 < p < 5$  
  <sub>Salah: Mengambil daerah dalam interval pertidaksamaan bukannya daerah luar bertanda positif.</sub>
- D. $p < -5$ atau $p > 3$  
  <sub>Salah: Salah dalam memfaktorkan persamaan kuadrat menjadi $(p + 5)(p - 3) > 0$.</sub>

**Pembahasan:** Diketahui bentuk umum lingkaran $x^2 + y^2 + Ax + By + C = 0$ dengan $A = 6$, $B = 2p$, dan $C = 2p + 24$.
Titik pusat lingkaran adalah $(a, b) = (-3, -p)$.
Syarat lingkaran nyata adalah $r^2 > 0$:
$$a^2 + b^2 - C > 0$$
$$(-3)^2 + (-p)^2 - (2p + 24) > 0$$
$$9 + p^2 - 2p - 24 > 0$$
$$p^2 - 2p - 15 > 0$$
$$(p - 5)(p + 3) > 0$$
Pembuat nol adalah $p = -3$ dan $p = 5$. Menggunakan garis bilangan untuk tanda $> 0$, diperoleh $p < -3$ atau $p > 5$.
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b01-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: panjang tali busur perpotongan sumbu*

Sebuah lingkaran berpusat di titik $P(3, k)$ dengan $k > 0$ dan memiliki jari-jari $5$. Jika sumbu-$x$ memotong lingkaran tersebut sehingga terbentuk tali busur dengan panjang $8$ satuan, maka bentuk umum persamaan lingkaran tersebut adalah ....

- **A. $x^2 + y^2 - 6x - 6y - 7 = 0$** ✅  
  <sub>Benar: Jarak dari pusat $P(3, k)$ ke sumbu-$x$ ($y = 0$) adalah $|k| = k$. Garis dari pusat yang tegak lurus sumbu-$x$ membagi tali busur menjadi dua bagian sama panjang, yaitu $\frac{8}{2} = 4$. Berdasarkan teorema Pythagoras pada segitiga siku-siku antara jarak pusat, setengah tali busur, dan jari-jari lingkaran: $k^2 + 4^2 = 5^2 \implies k^2 + 16 = 25 \implies k^2 = 9$. Karena $k > 0$, maka $k = 3$. Pusat lingkaran adalah $(3, 3)$ dengan jari-jari $r = 5$. Persamaan lingkarannya: $(x - 3)^2 + (y - 3)^2 = 5^2 \iff x^2 - 6x + 9 + y^2 - 6y + 9 = 25 \iff x^2 + y^2 - 6x - 6y - 7 = 0$.</sub>
- B. $x^2 + y^2 - 6x - 8y + 9 = 0$  
  <sub>Salah: Keliru menganggap nilai $k$ sama dengan setengah panjang tali busur, yaitu $k = 4$.</sub>
- C. $x^2 + y^2 - 6x - 6y + 25 = 0$  
  <sub>Salah: Lupa mengurangkan suku konstan dari kuadrat jari-jari ke ruas kiri ($9 + 9 - 25$ dihitung tanpa menjumlahkan konstanta kuadrat).</sub>
- D. $x^2 + y^2 - 6x - 6y + 11 = 0$  
  <sub>Salah: Salah menghitung nilai kuadrat jari-jari atau salah mengurangkan konstanta.</sub>

**Pembahasan:** Diketahui pusat lingkaran $P(3, k)$ dengan $k > 0$ dan $r = 5$.
Sumbu-$x$ mempunyai persamaan $y = 0$, sehingga jarak tegak lurus dari $P(3, k)$ ke sumbu-$x$ adalah $d = |k| = k$.
Tali busur pada sumbu-$x$ terbagi dua oleh garis proyeksi dari pusat, masing-masing dengan panjang $4$.
Berdasarkan teorema Pythagoras:
$$d^2 + 4^2 = r^2$$
$$k^2 + 16 = 25 \implies k^2 = 9 \implies k = 3 \text{ (karena } k > 0)$$
Pusat lingkaran adalah $(3, 3)$. Persamaan lingkaran:
$$(x - 3)^2 + (y - 3)^2 = 5^2$$
$$x^2 - 6x + 9 + y^2 - 6y + 9 = 25$$
$$x^2 + y^2 - 6x - 6y - 7 = 0$$
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b01-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: lingkaran luar segitiga siku-siku*

Sebuah segitiga pada bidang Kartesius memiliki titik-titik sudut di $A(1, 2)$, $B(7, 2)$, dan $C(1, 10)$. Bentuk umum persamaan lingkaran luar yang membatasi segitiga $ABC$ tersebut adalah ....

- A. $x^2 + y^2 - 4x - 6y - 12 = 0$  
  <sub>Salah: Keliru menggunakan koordinat titik pusat $(4, 6)$ secara langsung sebagai koefisien $A$ dan $B$ tanpa dikalikan $-2$.</sub>
- B. $x^2 + y^2 - 8x - 12y - 27 = 0$  
  <sub>Salah: Salah tanda pada konstanta $C$.</sub>
- C. $x^2 + y^2 - 8x - 12y + 52 = 0$  
  <sub>Salah: Lupa mengurangkan $r^2 = 25$ pada konstanta $16 + 36 = 52$.</sub>
- **D. $x^2 + y^2 - 8x - 12y + 27 = 0$** ✅  
  <sub>Benar: Ruas garis $AB$ sejajar sumbu-$x$ (karena ordinat kedua titik sama, yaitu $y = 2$) dan ruas garis $AC$ sejajar sumbu-$y$ (karena absis kedua titik sama, yaitu $x = 1$). Karena $AB \perp AC$, maka $\triangle ABC$ siku-siku di $A$. Berdasarkan sifat lingkaran, sudut siku-siku menghadap busur setengah lingkaran, sehingga sisi miring $BC$ merupakan diameter lingkaran luar. Titik pusat lingkaran adalah titik tengah $BC$, yaitu $P = \left(\frac{7+1}{2}, \frac{2+10}{2}\right) = (4, 6)$. Jari-jari lingkaran adalah setengah dari panjang $BC$, atau jarak $P$ ke $A$: $r^2 = (4 - 1)^2 + (6 - 2)^2 = 3^2 + 4^2 = 25$. Persamaan lingkaran: $(x - 4)^2 + (y - 6)^2 = 25 \iff x^2 - 8x + 16 + y^2 - 12y + 36 = 25 \iff x^2 + y^2 - 8x - 12y + 27 = 0$.</sub>

**Pembahasan:** Perhatikan koordinat titik sudut $\triangle ABC$:
- Garis $AB$ mendatar karena ordinat $A(1, 2)$ dan $B(7, 2)$ sama.
- Garis $AC$ tegak karena absis $A(1, 2)$ dan $C(1, 10)$ sama.
Karena garis mendatar tegak lurus garis tegak, maka sudut $\angle A = 90^\circ$.
Dalam lingkaran luar segitiga siku-siku, sisi miring $BC$ adalah diameter lingkaran.
Pusat lingkaran adalah titik tengah $BC$:
$$P(a, b) = \left(\frac{7 + 1}{2}, \frac{2 + 10}{2}\right) = (4, 6)$$
Panjang jari-jari kuadrat:
$$r^2 = (4 - 1)^2 + (6 - 2)^2 = 3^2 + 4^2 = 9 + 16 = 25$$
Persamaan lingkaran:
$$(x - 4)^2 + (y - 6)^2 = 25$$
$$x^2 - 8x + 16 + y^2 - 12y + 36 - 25 = 0$$
$$x^2 + y^2 - 8x - 12y + 27 = 0$$
**Acuan:** siswa — siswa hal.24

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b01-a-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: hubungan dua lingkaran konsentris dan tali busur*

Dua lingkaran $L_1$ dan $L_2$ konsentris (memiliki titik pusat yang sama) dengan pusat di $P(2, -3)$. Jari-jari lingkaran $L_1$ adalah $4$ satuan. Sebuah tali busur pada lingkaran $L_2$ menyinggung lingkaran $L_1$ dan memiliki panjang $6$ satuan. Bentuk umum persamaan lingkaran $L_2$ adalah ....

- A. $x^2 + y^2 - 4x + 6y + 13 = 0$  
  <sub>Salah: Lupa mengurangkan $r_2^2 = 25$ ke ruas kiri persamaan lingkaran.</sub>
- B. $x^2 + y^2 + 4x - 6y - 12 = 0$  
  <sub>Salah: Terbalik tanda koordinat pusat lingkaran saat menyusun persamaan umum.</sub>
- **C. $x^2 + y^2 - 4x + 6y - 12 = 0$** ✅  
  <sub>Benar: Kedua lingkaran memiliki pusat yang sama, yaitu $P(2, -3)$. Tali busur lingkaran $L_2$ menyinggung $L_1$, sehingga jarak tegak lurus dari titik pusat $P$ ke tali busur tersebut tepat sama dengan jari-jari lingkaran $L_1$, yaitu $d = r_1 = 4$. Garis dari pusat yang tegak lurus tali busur membagi tali busur sama panjang menjadi dua bagian, masing-masing $\frac{6}{2} = 3$ satuan. Segitiga siku-siku dibentuk oleh jari-jari $L_1$, setengah tali busur, dan jari-jari lingkaran luar $r_2$. Maka: $r_2^2 = d^2 + 3^2 = 4^2 + 3^2 = 16 + 9 = 25$. Persamaan lingkaran $L_2$ adalah $(x - 2)^2 + (y + 3)^2 = 25 \iff x^2 - 4x + 4 + y^2 + 6y + 9 = 25 \iff x^2 + y^2 - 4x + 6y - 12 = 0$.</sub>
- D. $x^2 + y^2 - 4x + 6y - 39 = 0$  
  <sub>Salah: Keliru menggunakan panjang tali busur utuh $6$ bukannya setengah tali busur, sehingga $r_2^2 = 4^2 + 6^2 = 52$ dan $C = 13 - 52 = -39$.</sub>

**Pembahasan:** Karena $L_1$ dan $L_2$ konsentris, pusat lingkaran $L_2$ sama dengan $L_1$, yaitu $P(2, -3)$.
Tali busur $L_2$ menyinggung lingkaran dalam $L_1$, yang berarti jarak dari pusat ke tali busur adalah jari-jari $L_1$, yaitu $d = 4$.
Garis dari pusat membagi tali busur menjadi dua bagian sama panjang, masing-masing sepanjang $\frac{6}{2} = 3$ satuan.
Dengan teorema Pythagoras pada segitiga siku-siku antara pusat, titik singgung, dan salah satu ujung tali busur, diperoleh kuadrat jari-jari $L_2$ ($r_2$):
$$r_2^2 = 4^2 + 3^2 = 16 + 9 = 25$$
Persamaan lingkaran $L_2$:
$$(x - 2)^2 + (y + 3)^2 = 25$$
$$x^2 - 4x + 4 + y^2 + 6y + 9 - 25 = 0$$
$$x^2 + y^2 - 4x + 6y - 12 = 0$$
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b01-a-hard-bt01-011
*variasi (angka) | C5 | 4 langkah | jenis: lingkaran dalam persegi koordinat*

Sebuah persegi $ABCD$ memiliki titik-titik sudut yang berturut-turut terletak pada $A(-4, -2)$, $B(6, -2)$, $C(6, 8)$, dan $D(-4, 8)$. Persamaan lingkaran yang menyinggung keempat sisi persegi $ABCD$ tersebut adalah ....

- A. $(x + 1)^2 + (y + 3)^2 = 25$  
  <sub>Salah: Siswa melakukan kesalahan tanda koordinat titik pusat lingkaran saat mensubstitusikan ke bentuk baku persamaan lingkaran.</sub>
- B. $(x - 1)^2 + (y - 3)^2 = 100$  
  <sub>Salah: Siswa menggunakan panjang seluruh sisi persegi ($10$) sebagai panjang jari-jari lingkaran, bukan setengahnya.</sub>
- **C. $(x - 1)^2 + (y - 3)^2 = 25$** ✅  
  <sub>Benar: Panjang sisi persegi adalah $6 - (-4) = 10$. Pusat lingkaran merupakan titik potong kedua diagonal (titik tengah $A$ dan $C$), yaitu $\left(\frac{-4 + 6}{2}, \frac{-2 + 8}{2}\right) = (1, 3)$. Karena lingkaran menyinggung keempat sisi persegi, jari-jarinya adalah setengah panjang sisi, yaitu $r = \frac{10}{2} = 5$. Persamaannya $(x - 1)^2 + (y - 3)^2 = 5^2 = 25$.</sub>
- D. $(x - 1)^2 + (y - 3)^2 = 50$  
  <sub>Salah: Siswa keliru menghitung persamaan lingkaran luar persegi yang melalui keempat titik sudutnya dengan $r^2 = 5^2 + 5^2 = 50$.</sub>

**Pembahasan:** Langkah 1: Menentukan panjang sisi persegi.
$s = x_B - x_A = 6 - (-4) = 10$.

Langkah 2: Menentukan koordinat pusat lingkaran ($P$).
Titik pusat lingkaran dalam tepat berada di titik tengah diagonal $AC$:
$x_P = \frac{-4 + 6}{2} = 1$
$y_P = \frac{-2 + 8}{2} = 3$
Jadi, pusat lingkaran adalah $P(1, 3)$.

Langkah 3: Menentukan jari-jari lingkaran ($r$).
Karena lingkaran menyinggung keempat sisi persegi, jari-jarinya adalah setengah dari panjang sisi persegi:
$r = \frac{s}{2} = \frac{10}{2} = 5$.

Langkah 4: Menyusun persamaan baku lingkaran.
$(x - a)^2 + (y - b)^2 = r^2$
$(x - 1)^2 + (y - 3)^2 = 5^2$
$(x - 1)^2 + (y - 3)^2 = 25$.
**Acuan:** siswa — siswa hal.33 Latihan Soal Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b01-a-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: nilai ekstrem kuadrat jarak pada lingkaran*

Sebuah partikel bergerak di sepanjang lintasan lingkaran dengan persamaan $x^2 + y^2 - 8x - 6y + 21 = 0$. Jika $(x, y)$ menyatakan posisi partikel tersebut, nilai maksimum dari $x^2 + y^2$ adalah ....

- A. $25$  
  <sub>Salah: Siswa hanya menghitung kuadrat jarak dari titik asal ke pusat lingkaran tanpa menambahkan jari-jari ($5^2 = 25$).</sub>
- B. $9$  
  <sub>Salah: Siswa keliru menghitung nilai minimum kuadrat jarak, yaitu $(d - r)^2 = (5 - 2)^2 = 9$.</sub>
- **C. $49$** ✅  
  <sub>Benar: Nilai $x^2 + y^2$ menyatakan kuadrat jarak dari titik asal $O(0, 0)$ ke titik $(x, y)$ pada lingkaran. Lingkaran memiliki pusat $(4, 3)$ dan jari-jari $r = \sqrt{4^2 + 3^2 - 21} = 2$. Jarak titik asal ke pusat adalah $d = \sqrt{4^2 + 3^2} = 5$. Jarak maksimum titik pada lingkaran ke titik asal adalah $d + r = 5 + 2 = 7$. Maka nilai maksimum dari $x^2 + y^2$ adalah $7^2 = 49$.</sub>
- D. $29$  
  <sub>Salah: Siswa menjumlahkan kuadrat jarak pusat ke titik asal dengan kuadrat jari-jari ($5^2 + 2^2 = 29$) alih-alih menguadratkan jarak total maksimum.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat dan jari-jari lingkaran.
Dari persamaan $x^2 + y^2 - 8x - 6y + 21 = 0$:
$A = -8$, $B = -6$, $C = 21$.
Pusat $P(a, b) = \left(-\frac{1}{2}(-8), -\frac{1}{2}(-6)\right) = (4, 3)$.
Jari-jari $r = \sqrt{4^2 + 3^2 - 21} = \sqrt{16 + 9 - 21} = \sqrt{4} = 2$.

Langkah 2: Menghubungkan $x^2 + y^2$ dengan konsep jarak.
Bentuk $x^2 + y^2$ merepresentasikan kuadrat dari jarak titik $(x, y)$ pada lingkaran ke titik asal $O(0, 0)$.

Langkah 3: Menghitung jarak terjauh dari titik asal ke lingkaran.
Jarak dari titik asal $O(0, 0)$ ke pusat lingkaran $P(4, 3)$ adalah:
$OP = \sqrt{(4 - 0)^2 + (3 - 0)^2} = \sqrt{16 + 9} = 5$.
Jarak terjauh dari $O(0, 0)$ ke titik pada lingkaran tercapai pada titik yang segaris dengan $OP$, yaitu:
$d_{\max} = OP + r = 5 + 2 = 7$.

Langkah 4: Menghitung nilai maksimum $x^2 + y^2$.
$(x^2 + y^2)_{\max} = (d_{\max})^2 = 7^2 = 49$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b01-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: panjang perpotongan tali busur garis*

Titik pusat sebuah lingkaran terletak pada garis $y = x + 1$. Lingkaran tersebut melalui titik asal $O(0, 0)$ dan memotong sumbu-$x$ positif di titik $(4, 0)$. Panjang tali busur yang terbentuk ketika lingkaran tersebut dipotong oleh garis horizontal $y = 1$ adalah ....

- A. $4$  
  <sub>Salah: Mengira panjang tali busur pada garis $y = 1$ sama dengan panjang tali busur pada sumbu-$x$ yaitu $4$ satuan.</sub>
- **B. $6$** ✅  
  <sub>Benar: Karena lingkaran melalui $(0,0)$ dan $(4,0)$, titik tengah tali busur di sumbu-$x$ berabsis $x = 2$, sehingga absis pusat lingkaran adalah $a = 2$. Pusat terletak pada $y = x + 1$, sehingga ordinat pusat adalah $b = 2 + 1 = 3$. Jari-jari kuadrat lingkaran adalah $r^2 = (2 - 0)^2 + (3 - 0)^2 = 13$, dengan persamaan $(x - 2)^2 + (y - 3)^2 = 13$. Substitusi garis $y = 1$ menghasilkan $(x - 2)^2 + (1 - 3)^2 = 13 \iff (x - 2)^2 + 4 = 13 \iff (x - 2)^2 = 9$. Diperoleh $x - 2 = 3 \implies x = 5$ atau $x - 2 = -3 \implies x = -1$. Panjang tali busur adalah $|5 - (-1)| = 6$.</sub>
- C. $3$  
  <sub>Salah: Hanya menghitung nilai simpangan $|x - 2| = 3$ dari sumbu simetri, bukan panjang tali busur utuh.</sub>
- D. $8$  
  <sub>Salah: Kesalahan perhitungan kuadrat jarak saat menentukan jari-jari kuadrat menjadi $17$, menghasilkan $x - 2 = \pm 4$ sehingga panjangnya $8$.</sub>

**Pembahasan:** 1. Menentukan titik pusat $P(a, b)$:
Lingkaran melalui $(0, 0)$ dan $(4, 0)$ pada sumbu-$x$. Garis sumbu dari ruas garis ini adalah garis vertikal $x = \frac{0 + 4}{2} = 2$. Karena pusat lingkaran harus terletak pada garis sumbu tali busur, maka $a = 2$.
Substitusikan $a = 2$ ke persamaan garis tempat pusat berada $y = x + 1$:
$b = 2 + 1 = 3$.
Jadi, pusat lingkaran adalah $P(2, 3)$.

2. Menentukan jari-jari lingkaran:
Karena lingkaran melalui $(0, 0)$, maka:
$r^2 = (2 - 0)^2 + (3 - 0)^2 = 4 + 9 = 13$.
Persamaan lingkaran adalah $(x - 2)^2 + (y - 3)^2 = 13$.

3. Menentukan titik potong dengan garis $y = 1$:
Substitusikan $y = 1$ ke persamaan lingkaran:
$(x - 2)^2 + (1 - 3)^2 = 13$
$(x - 2)^2 + 4 = 13$
$(x - 2)^2 = 9$
$x - 2 = 3 \implies x_1 = 5$
$x - 2 = -3 \implies x_2 = -1$

4. Menghitung panjang tali busur:
Panjang tali busur $= |x_1 - x_2| = |5 - (-1)| = 6$.
**Acuan:** siswa — siswa hal.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b01-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: rekonstruksi persamaan lingkaran bersyarat garis singgung*

Sebuah lingkaran berpusat di titik $P(h, k)$ pada kuadran IV. Titik pusat lingkaran tersebut terletak pada garis $x + y = 1$. Jika lingkaran tersebut menyinggung sumbu-$x$ dan menyinggung garis vertikal $x = 7$, bentuk umum persamaan lingkaran tersebut adalah ....

- A. $x^2 + y^2 - 8x - 6y + 16 = 0$  
  <sub>Salah: Tertukar tanda ordinat pusat menjadi $(4, 3)$ di kuadran I, mengabaikan syarat pusat di kuadran IV.</sub>
- **B. $x^2 + y^2 - 8x + 6y + 16 = 0$** ✅  
  <sub>Benar: Pusat $P(h, k)$ di kuadran IV ($h > 0, k < 0$). Karena pusat terletak pada $x + y = 1$, maka $k = 1 - h$. Lingkaran menyinggung sumbu-$x$, sehingga jari-jarinya $r = |k| = -(1 - h) = h - 1$. Lingkaran menyinggung garis $x = 7$, sehingga $r = |7 - h|$. Karena $r = h - 1$ dan $r = |7 - h|$, diperoleh $h - 1 = |7 - h|$. Untuk $h < 7$, $h - 1 = 7 - h \iff 2h = 8 \iff h = 4$. Diperoleh $k = 1 - 4 = -3$ dan jari-jari $r = 3$. Persamaan lingkaran: $(x - 4)^2 + (y + 3)^2 = 3^2 \iff x^2 - 8x + 16 + y^2 + 6y + 9 = 9 \iff x^2 + y^2 - 8x + 6y + 16 = 0$.</sub>
- C. $x^2 + y^2 + 8x - 6y + 16 = 0$  
  <sub>Salah: Tertukar tanda absis dan ordinat pusat lingkaran menjadi $(-4, 3)$ di kuadran II.</sub>
- D. $x^2 + y^2 - 8x + 6y + 22 = 0$  
  <sub>Salah: Lupa menguadratkan nilai jari-jari pada ruas kanan persamaan baku (menggunakan $r = 3$ bukan $r^2 = 9$).</sub>

**Pembahasan:** 1. Menentukan relasi koordinat pusat $P(h, k)$:
Karena $P(h, k)$ terletak pada garis $x + y = 1$, maka:
$k = 1 - h$.
Karena $P$ berada di kuadran IV, maka $h > 0$ dan $k < 0$. Dari $k = 1 - h < 0$, diperoleh $h > 1$.

2. Menganalisis syarat jari-jari ($r$):
- Menyinggung sumbu-$x$: jarak pusat ke sumbu-$x$ adalah $r = |k| = -k = -(1 - h) = h - 1$.
- Menyinggung garis $x = 7$: jarak pusat ke garis $x = 7$ adalah $r = |h - 7|$.

3. Menyelesaikan nilai $h$ dan $k$:
$h - 1 = |7 - h|$
Karena $h > 1$ dan jika $h < 7$:
$h - 1 = 7 - h$
$2h = 8 \implies h = 4$.
(Jika $h \ge 7$: $h - 1 = h - 7 \implies -1 = -7$, tidak ada solusi).
Dengan $h = 4$, maka $k = 1 - 4 = -3$.
Jari-jari $r = 4 - 1 = 3$.

4. Menyusun bentuk umum persamaan lingkaran:
Persamaan baku: $(x - 4)^2 + (y - (-3))^2 = 3^2$
$(x - 4)^2 + (y + 3)^2 = 9$
$x^2 - 8x + 16 + y^2 + 6y + 9 = 9$
$x^2 + y^2 - 8x + 6y + 16 = 0$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b01-a-hard-bt01-015
*variasi (angka) | C5 | 4 langkah | jenis: transformasi rotasi dan translasi lingkaran*

Diketahui lingkaran $L$ berpusat di titik $(3, 4)$ dan melalui titik $(7, 7)$. Misalkan lingkaran $L$ diputar $90^\circ$ searah jarum jam terhadap titik asal $O(0, 0)$, kemudian digeser ke atas sejauh 3 satuan. Bentuk baku persamaan lingkaran yang dihasilkan adalah ....

- A. $(x - 3)^2 + (y - 7)^2 = 25$  
  <sub>Salah: Salah menerapkan aturan rotasi searah jarum jam dan menggeser langsung titik pusat asal tanpa rotasi yang tepat.</sub>
- B. $(x - 4)^2 + (y + 6)^2 = 25$  
  <sub>Salah: Salah mengartikan pergeseran ke atas sebagai pengurangan pada koordinat $y$ sehingga diperoleh $-3 - 3 = -6$ bukannya $-3 + 3 = 0$.</sub>
- C. $(x + 4)^2 + y^2 = 25$  
  <sub>Salah: Tertukar arah rotasi menjadi berlawanan arah jarum jam sehingga koordinat pusat menjadi $(-4, 3)$, lalu digeser ke atas menjadi $(-4, 6)$ atau salah menentukan tanda absis hasil rotasi.</sub>
- **D. $(x - 4)^2 + y^2 = 25$** ✅  
  <sub>Benar: Jari-jari lingkaran mula-mula adalah $r = \sqrt{(7 - 3)^2 + (7 - 4)^2} = \sqrt{16 + 9} = 5$. Rotasi $90^\circ$ searah jarum jam terhadap titik asal memetakan $(x, y) \to (y, -x)$, sehingga pusat $(3, 4)$ berpindah ke $(4, -3)$. Pergeseran ke atas sejauh 3 satuan mengubah koordinat titik pusat menjadi $(4, -3 + 3) = (4, 0)$. Karena jari-jari tidak berubah ($r = 5$), persamaan lingkaran akhir adalah $(x - 4)^2 + (y - 0)^2 = 5^2 \iff (x - 4)^2 + y^2 = 25$.</sub>

**Pembahasan:** Langkah 1: Menentukan jari-jari lingkaran mula-mula:
$$r^2 = (7 - 3)^2 + (7 - 4)^2 = 4^2 + 3^2 = 16 + 9 = 25$$

Langkah 2: Menentukan koordinat pusat setelah rotasi $90^\circ$ searah jarum jam terhadap $O(0, 0)$:
Matriks rotasi $-90^\circ$ memetakan $(x, y) \to (y, -x)$.
Pusat awal $(3, 4) \to (4, -3)$.

Langkah 3: Menentukan koordinat pusat setelah pergeseran ke atas sejauh 3 satuan:
$$(x', y') = (4, -3 + 3) = (4, 0)$$

Langkah 4: Menyusun persamaan lingkaran dengan pusat $(4, 0)$ dan $r^2 = 25$:
$$(x - 4)^2 + (y - 0)^2 = 25 \iff (x - 4)^2 + y^2 = 25$$
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b01-a-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: transformasi refleksi sumbu dan dilatasi jari-jari*

Diketahui sebuah lingkaran $L_1 \equiv x^2 + y^2 - 4x + 12y + 15 = 0$. Dibuat lingkaran kedua $L_2$ dengan titik pusat lingkaran $L_1$ dicerminkan terhadap sumbu-$y$ dan panjang jari-jarinya diperbesar dua kali dari jari-jari $L_1$. Bentuk umum persamaan lingkaran $L_2$ tersebut adalah ....

- A. $x^2 + y^2 - 4x - 12y - 60 = 0$  
  <sub>Salah: Siswa mencerminkan titik pusat terhadap sumbu-$x$ bukan sumbu-$y$, sehingga koordinat pusat tertukar menjadi $(2, 6)$.</sub>
- B. $x^2 + y^2 + 4x + 12y - 10 = 0$  
  <sub>Salah: Siswa mengalikan nilai $r^2$ dengan dua ($25 \times 2 = 50$) bukan mengalikan panjang jari-jari $r$ dengan dua.</sub>
- **C. $x^2 + y^2 + 4x + 12y - 60 = 0$** ✅  
  <sub>Benar: Dari persamaan $L_1$, diperoleh $A = -4$, $B = 12$, dan $C = 15$. Titik pusat $L_1$ adalah $\left(-\frac{-4}{2}, -\frac{12}{2}\right) = (2, -6)$, dan jari-jarinya $r_1 = \sqrt{2^2 + (-6)^2 - 15} = \sqrt{4 + 36 - 15} = \sqrt{25} = 5$. Hasil pencerminan pusat $(2, -6)$ terhadap sumbu-$y$ adalah $(-2, -6)$. Jari-jari lingkaran $L_2$ adalah $r_2 = 2 \times 5 = 10$. Persamaan lingkaran $L_2$ adalah $(x + 2)^2 + (y + 6)^2 = 10^2 \iff x^2 + y^2 + 4x + 12y + 40 - 100 = 0 \iff x^2 + y^2 + 4x + 12y - 60 = 0$.</sub>
- D. $x^2 + y^2 + 4x + 12y + 15 = 0$  
  <sub>Salah: Siswa lupa mengalikan jari-jari dengan faktor skala dua dan tetap memakai nilai konstanta $C$ yang lama.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat dan jari-jari lingkaran $L_1$:
- $a = -\frac{A}{2} = -\frac{-4}{2} = 2$
- $b = -\frac{B}{2} = -\frac{12}{2} = -6$
- Pusat $L_1 = (2, -6)$
- $r_1 = \sqrt{a^2 + b^2 - C} = \sqrt{2^2 + (-6)^2 - 15} = \sqrt{25} = 5$

Langkah 2: Menentukan titik pusat lingkaran $L_2$ setelah dicerminkan terhadap sumbu-$y$:
Refleksi terhadap sumbu-$y$ memetakan $(x, y) \to (-x, y)$, sehingga pusat baru adalah $(-2, -6)$.

Langkah 3: Menentukan jari-jari lingkaran $L_2$:
$$r_2 = 2 \times r_1 = 2 \times 5 = 10$$

Langkah 4: Menyusun bentuk umum persamaan lingkaran $L_2$:
$$(x - (-2))^2 + (y - (-6))^2 = 10^2$$
$$(x + 2)^2 + (y + 6)^2 = 100$$
$$x^2 + 4x + 4 + y^2 + 12y + 36 = 100$$
$$x^2 + y^2 + 4x + 12y - 60 = 0$$
**Acuan:** pretest — kelas12_tl-b01-p0033-latihan-soal-lingkaran-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b01-a-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: evaluasi parameter tali busur lingkaran*

Diketahui persamaan $x^2 + y^2 - 4x - 6y + k = 0$ merepresentasikan sebuah lingkaran. Jika garis horizontal $y = 1$ memotong lingkaran tersebut sehingga terbentuk tali busur dengan panjang $8$ satuan, maka nilai $k$ yang memenuhi adalah ....

- **A. $-7$** ✅  
  <sub>Benar: Pusat lingkaran adalah $P(a, b) = \left(-\frac{-4}{2}, -\frac{-6}{2}\right) = (2, 3)$. Jarak tegak lurus dari titik pusat $(2, 3)$ ke garis $y = 1$ adalah $d = |3 - 1| = 2$. Panjang setengah tali busur adalah $\frac{8}{2} = 4$. Berdasarkan teorema Pythagoras pada segitiga siku-siku antara jarak pusat ke tali busur, setengah panjang tali busur, dan jari-jari lingkaran, diperoleh $r^2 = d^2 + 4^2 = 2^2 + 4^2 = 4 + 16 = 20$. Dari rumus jari-jari lingkaran, $r^2 = a^2 + b^2 - k = 2^2 + 3^2 - k = 13 - k$. Maka $13 - k = 20 \iff k = 13 - 20 = -7$.</sub>
- B. $7$  
  <sub>Salah: Siswa salah tanda saat memindahkan variabel aljabar dari persamaan $13 - k = 20$, menganggap $k = 20 - 13 = 7$.</sub>
- C. $-12$  
  <sub>Salah: Siswa salah menentukan jarak titik pusat ke garis $y = 1$, menggunakan nilai ordinat $b = 3$ secara langsung sebagai $d$, sehingga $r^2 = 3^2 + 4^2 = 25$ dan $k = 13 - 25 = -12$.</sub>
- D. $-55$  
  <sub>Salah: Siswa tidak membagi panjang tali busur menjadi dua (menggunakan panjang penuh 8), sehingga menghitung $r^2 = 2^2 + 8^2 = 68$ dan $k = 13 - 68 = -55$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat titik pusat lingkaran:
$$a = -\frac{-4}{2} = 2, \quad b = -\frac{-6}{2} = 3 \implies P(2, 3)$$

Langkah 2: Menentukan jarak titik pusat $P(2, 3)$ ke garis $y = 1$:
Karena garis bersifat horizontal sejajar sumbu-$x$, jarak tegak lurusnya adalah:
$$d = |y_P - 1| = |3 - 1| = 2$$

Langkah 3: Menggunakan hubungan tali busur dan teorema Pythagoras untuk mencari $r^2$:
Setengah panjang tali busur adalah $L_{setengah} = \frac{8}{2} = 4$.
$$r^2 = d^2 + (L_{setengah})^2 = 2^2 + 4^2 = 4 + 16 = 20$$

Langkah 4: Menentukan nilai konstanta $k$ menggunakan rumus jari-jari:
$$r^2 = a^2 + b^2 - k$$
$$20 = 2^2 + 3^2 - k$$
$$20 = 4 + 9 - k$$
$$20 = 13 - k \implies k = 13 - 20 = -7$$
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b01-a-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: titik terdekat pada lingkaran*

Diberikan persamaan lingkaran $L \equiv x^2 + y^2 - 2x - 4y - 20 = 0$ dan sebuah titik $A(7, 10)$ di luar lingkaran. Jika titik $P(x_0, y_0)$ terletak pada keliling lingkaran $L$ dan memiliki jarak terdekat ke titik $A$, maka nilai dari $2x_0 + y_0$ adalah ....

- A. 18  
  <sub>Salah: Siswa keliru menganggap titik $P$ diperoleh dengan menggeser titik $A$ ke kiri dan ke bawah sebesar komponen jari-jari secara langsung tanpa rasio panjang garis.</sub>
- B. -6  
  <sub>Salah: Siswa menentukan titik pada lingkaran yang memiliki jarak terjauh dari titik $A$, yaitu titik $P'(-2, -2)$, sehingga memperoleh $2(-2) + (-2) = -6$.</sub>
- **C. 14** ✅  
  <sub>Benar: Pusat lingkaran adalah $M(1, 2)$ dan jari-jarinya $r = \sqrt{1^2 + 2^2 - (-20)} = 5$. Jarak $MA = \sqrt{(7-1)^2 + (10-2)^2} = 10$. Titik terdekat $P$ terletak pada ruas garis $MA$ dengan jarak $MP = 5$, sehingga $P$ tepat merupakan titik tengah $MA$, yaitu $P(4, 6)$. Maka $2x_0 + y_0 = 2(4) + 6 = 14$.</sub>
- D. 10  
  <sub>Salah: Siswa sudah menemukan koordinat $P(4, 6)$ dengan benar, tetapi hanya menjumlahkan $x_0 + y_0$ dan lupa mengalikan $x_0$ dengan koefisien 2.</sub>

**Pembahasan:** Persamaan lingkaran $x^2 + y^2 - 2x - 4y - 20 = 0$ memiliki nilai $A = -2$, $B = -4$, dan $C = -20$.

1. Menentukan titik pusat $M(a, b)$ dan jari-jari $r$:
$$a = -\frac{A}{2} = -\frac{-2}{2} = 1$$
$$b = -\frac{B}{2} = -\frac{-4}{2} = 2$$
Pusat lingkaran adalah $M(1, 2)$.
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{1^2 + 2^2 - (-20)} = \sqrt{1 + 4 + 20} = \sqrt{25} = 5$$

2. Menghitung jarak dari pusat $M(1, 2)$ ke titik $A(7, 10)$:
$$MA = \sqrt{(7 - 1)^2 + (10 - 2)^2} = \sqrt{6^2 + 8^2} = \sqrt{36 + 64} = \sqrt{100} = 10$$

3. Menentukan koordinat titik $P(x_0, y_0)$:
Titik pada lingkaran yang terdekat ke $A$ berada pada ruas garis $MA$ dan berjarak $r = 5$ satuan dari $M$. Karena panjang $MA = 10$ dan $MP = 5$, maka titik $P$ adalah titik tengah dari ruas garis $MA$:
$$x_0 = \frac{1 + 7}{2} = 4$$
$$y_0 = \frac{2 + 10}{2} = 6$$
Sehingga koordinat titik terdekat adalah $P(4, 6)$.

4. Menghitung nilai $2x_0 + y_0$:
$$2x_0 + y_0 = 2(4) + 6 = 8 + 6 = 14$$
**Acuan:** siswa — siswa hal.21

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b01-a-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: panjang tali busur pada sumbu koordinat*

Sebuah lingkaran berpusat di titik $P$ yang terletak pada garis $x - y - 1 = 0$. Lingkaran tersebut melalui titik $A(1, 1)$ dan titik $B(5, 3)$. Panjang ruas garis yang terbentuk oleh perpotongan lingkaran tersebut dengan sumbu-$x$ adalah ....

- A. $4$  
  <sub>Salah: Siswa hanya mengambil nilai absis titik potong terbesar pada sumbu-$x$ tanpa mengurangkannya dengan titik potong lainnya.</sub>
- **B. $2$** ✅  
  <sub>Benar: Pusat lingkaran memenuhi jarak yang sama ke titik $A$ dan $B$ serta terletak pada garis $x - y - 1 = 0$, menghasilkan persamaan lingkaran $(x - 3)^2 + (y - 2)^2 = 5$. Perpotongan dengan sumbu-$x$ ($y = 0$) menghasilkan absis $x = 2$ dan $x = 4$, sehingga panjang ruas garisnya adalah $4 - 2 = 2$.</sub>
- C. $2\sqrt{5}$  
  <sub>Salah: Siswa salah menghitung panjang diameter lingkaran ($2r$) alih-alih panjang tali busur pada sumbu-$x$.</sub>
- D. $1$  
  <sub>Salah: Siswa keliru menganggap nilai ruas kanan $(x - 3)^2 = 1$ langsung sebagai panjang ruas garis.</sub>

**Pembahasan:** Misalkan koordinat titik pusat lingkaran adalah $P(a, b)$.
Karena $P$ terletak pada garis $x - y - 1 = 0$, maka $b = a - 1$.

Karena lingkaran melalui titik $A(1, 1)$ dan $B(5, 3)$, maka panjang jari-jari $PA = PB$, sehingga $PA^2 = PB^2$:
$$(a - 1)^2 + (b - 1)^2 = (a - 5)^2 + (b - 3)^2$$
$$a^2 - 2a + 1 + b^2 - 2b + 1 = a^2 - 10a + 25 + b^2 - 6b + 9$$
$$-2a - 2b + 2 = -10a - 6b + 34$$
$$8a + 4b = 32 \implies 2a + b = 8$$

Substitusikan $b = a - 1$ ke dalam persamaan tersebut:
$$2a + (a - 1) = 8 \implies 3a = 9 \implies a = 3$$
$$b = 3 - 1 = 2$$
Titik pusat lingkaran adalah $P(3, 2)$.

Kuadrat jari-jari lingkaran adalah:
$$r^2 = (3 - 1)^2 + (2 - 1)^2 = 2^2 + 1^2 = 5$$
Persamaan lingkarannya adalah:
$$(x - 3)^2 + (y - 2)^2 = 5$$

Untuk mencari titik potong dengan sumbu-$x$, substitusikan $y = 0$:
$$(x - 3)^2 + (0 - 2)^2 = 5$$
$$(x - 3)^2 + 4 = 5$$
$$(x - 3)^2 = 1$$
$$x - 3 = \pm 1$$
$$x_1 = 3 + 1 = 4 \quad \text{atau} \quad x_2 = 3 - 1 = 2$$

Panjang ruas garis yang terbentuk pada sumbu-$x$ adalah:
$$|x_1 - x_2| = |4 - 2| = 2$$
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b01-a-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: luas maksimum segitiga pada lingkaran*

Sebuah lingkaran memiliki persamaan $x^2 + y^2 - 4x - 6y - 12 = 0$. Lingkaran tersebut memotong sumbu-$x$ di dua titik, yaitu titik $A$ dan titik $B$. Jika titik $C$ terletak pada busur lingkaran di atas sumbu-$x$, luas maksimum yang mungkin untuk segitiga $ABC$ adalah ....

- **A. $32\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong dengan sumbu-$x$ diperoleh saat $y = 0$, yaitu $x^2 - 4x - 12 = 0 \iff (x - 6)(x + 2) = 0$, sehingga koordinat titik potong adalah $A(-2, 0)$ dan $B(6, 0)$. Panjang alas segitiga adalah ruas garis $AB = 6 - (-2) = 8$ satuan. Dari persamaan lingkaran, pusat lingkaran adalah $P(2, 3)$ dan jari-jarinya $r = \sqrt{2^2 + 3^2 - (-12)} = \sqrt{25} = 5$. Karena alas $AB$ berada pada garis $y = 0$, tinggi maksimum segitiga dicapai pada titik di lingkaran dengan ordinat tertinggi, yaitu $y_{\text{maks}} = b + r = 3 + 5 = 8$. Jadi, luas maksimum segitiga $ABC$ adalah $\frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 8 \times 8 = 32\text{ satuan luas}$.</sub>
- B. $24\text{ satuan luas}$  
  <sub>Salah: Siswa salah menentukan ordinat pusat atau salah menghitung ordinat maksimum menjadi $6$, sehingga memperoleh $\frac{1}{2} \times 8 \times 6 = 24$.</sub>
- C. $20\text{ satuan luas}$  
  <sub>Salah: Siswa keliru menganggap tinggi segitiga maksimum sama dengan panjang jari-jari lingkaran ($r = 5$), sehingga menghitung $\frac{1}{2} \times 8 \times 5 = 20$.</sub>
- D. $40\text{ satuan luas}$  
  <sub>Salah: Siswa menggunakan panjang diameter ($d = 10$) sebagai alas segitiga alih-alih panjang tali busur $AB$, sehingga menghitung $\frac{1}{2} \times 10 \times 8 = 40$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong lingkaran dengan sumbu-$x$ ($y = 0$).
$$x^2 + (0)^2 - 4x - 6(0) - 12 = 0 \iff x^2 - 4x - 12 = 0$$
$$(x - 6)(x + 2) = 0 \implies x_1 = -2 \text{ atau } x_2 = 6$$
Maka titik potongnya adalah $A(-2, 0)$ dan $B(6, 0)$.

Langkah 2: Menghitung panjang alas segitiga $AB$.
$$\text{Alas} = |6 - (-2)| = 8$$

Langkah 3: Menentukan titik pusat $P(a, b)$ dan jari-jari $r$ lingkaran.
$$a = -\frac{A}{2} = -\frac{-4}{2} = 2$$
$$b = -\frac{B}{2} = -\frac{-6}{2} = 3$$
$$r = \sqrt{a^2 + b^2 - C} = \sqrt{2^2 + 3^2 - (-12)} = \sqrt{4 + 9 + 12} = \sqrt{25} = 5$$

Langkah 4: Menentukan tinggi maksimum segitiga terhadap garis $y = 0$.
Tinggi segitiga merupakan jarak tegak dari titik $C(x, y)$ pada lingkaran ke sumbu-$x$, yaitu nilai $y$. Nilai $y$ maksimum pada lingkaran tercapai di titik puncak teratas:
$$y_{\text{maks}} = b + r = 3 + 5 = 8$$

Langkah 5: Menghitung luas maksimum segitiga $ABC$.
$$L_{\text{maks}} = \frac{1}{2} \times \text{alas} \times \text{tinggi}_{\text{maks}} = \frac{1}{2} \times 8 \times 8 = 32\text{ satuan luas}$$

Dengan demikian, luas maksimum segitiga $ABC$ adalah $32\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
