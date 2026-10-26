# Lembar koreksi — kelas9 SMP9-B3 subbab A: Translasi (Pergeseran)

45 soal | easy 15, medium 15, hard 15 | variasi 21, orisinal 24

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas9-b03-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: bayangan titik*

Bayangan titik $K(7, -4)$ oleh translasi $\binom{-5}{8}$ adalah ...

- **A. $K'(2, 4)$** ✅  
  <sub>Benar: Koordinat bayangan dihitung dengan menjumlahkan koordinat awal dan translasi: $x' = 7 + (-5) = 2$ dan $y' = -4 + 8 = 4$.</sub>
- B. $K'(12, -12)$  
  <sub>Salah: Melakukan operasi pengurangan koordinat titik awal dengan vektor translasi alih-alih penjumlahan.</sub>
- C. $K'(4, 2)$  
  <sub>Salah: Posisi absis dan ordinat pada bayangan tertukar.</sub>
- D. $K'(-2, -4)$  
  <sub>Salah: Kesalahan tanda pada saat menjumlahkan absis dan ordinat.</sub>

**Pembahasan:** Berdasarkan sifat translasi titik, bayangan dari titik $(x, y)$ oleh translasi $\binom{a}{b}$ adalah $(x + a, y + b)$.

Untuk titik $K(7, -4)$ dan translasi $\binom{-5}{8}$:
$x' = 7 + (-5) = 2$
$y' = -4 + 8 = 4$

Jadi, bayangan titik $K$ adalah $K'(2, 4)$.
**Acuan:** pretest — kelas9-b03-p0164-latihan-a-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas9-b03-a-easy-bt01-002
*variasi (konteks) | C2 | 1 langkah | jenis: translasi posisi objek*

Sebuah kapal selam mula-mula berada pada koordinat titik $P(-3, 6)$. Jika kapal tersebut bergerak melakukan pergeseran dengan translasi $\binom{8}{-5}$, maka posisi koordinat akhir kapal selam tersebut adalah ...

- A. $(1, 5)$  
  <sub>Salah: Tertukar antara komponen horizontal dan komponen vertikal hasil akhir.</sub>
- B. $(-11, 11)$  
  <sub>Salah: Mengurangkan posisi awal dengan vektor translasi: $-3 - 8 = -11$ dan $6 - (-5) = 11$.</sub>
- **C. $(5, 1)$** ✅  
  <sub>Benar: Posisi akhir dihitung dengan menjumlahkan posisi awal dan pergeseran: $-3 + 8 = 5$ dan $6 + (-5) = 1$.</sub>
- D. $(5, -1)$  
  <sub>Salah: Kesalahan perhitungan tanda pada koordinat vertikal $6 + (-5)$ menjadi $-1$.</sub>

**Pembahasan:** Posisi akhir diperoleh dengan menjumlahkan koordinat awal terhadap komponen translasi:
$x' = -3 + 8 = 5$
$y' = 6 + (-5) = 1$

Dengan demikian, posisi koordinat akhir kapal selam tersebut adalah $(5, 1)$.
**Acuan:** pretest — kelas9-b03-p0164-latihan-a-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas9-b03-a-easy-bt01-003
*variasi (angka) | C1 | 1 langkah | jenis: notasi translasi*

Pergeseran sejauh 6 satuan ke kiri dan 7 satuan ke atas dapat dinotasikan dalam bentuk translasi $\binom{a}{b}$ sebagai ...

- **A. $\binom{-6}{7}$** ✅  
  <sub>Benar: Arah ke kiri bernilai negatif ($a = -6$) dan arah ke atas bernilai positif ($b = 7$).</sub>
- B. $\binom{7}{-6}$  
  <sub>Salah: Tertukar antara komponen mendatar (horizontal) dan komponen tegak (vertikal).</sub>
- C. $\binom{6}{7}$  
  <sub>Salah: Lupa memberikan tanda negatif untuk pergeseran ke arah kiri.</sub>
- D. $\binom{6}{-7}$  
  <sub>Salah: Tertukar tanda positif dan negatif untuk arah pergeseran.</sub>

**Pembahasan:** Pada translasi $\binom{a}{b}$:
- $a$ menyatakan pergeseran horizontal: positif jika ke kanan, negatif jika ke kiri. Karena 6 satuan ke kiri, maka $a = -6$.
- $b$ menyatakan pergeseran vertikal: positif jika ke atas, negatif jika ke bawah. Karena 7 satuan ke atas, maka $b = 7$.

Jadi, bentuk translasi yang tepat adalah $\binom{-6}{7}$.
**Acuan:** siswa — siswa hal.164 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas9-b03-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: arah pergeseran translasi*

Translasi $\binom{5}{-8}$ memindahkan setiap titik pada bidang koordinat dengan aturan ...

- A. $5$ satuan ke kanan dan $8$ satuan ke atas  
  <sub>Salah: Mengabaikan tanda negatif pada komponen kedua sehingga diartikan bergerak ke atas.</sub>
- B. $5$ satuan ke kiri dan $8$ satuan ke atas  
  <sub>Salah: Terbalik dalam mengartikan tanda positif dan negatif pada masing-masing komponen.</sub>
- C. $5$ satuan ke atas dan $8$ satuan ke kiri  
  <sub>Salah: Tertukar antara peran komponen mendatar (pertama) dan komponen tegak (kedua).</sub>
- **D. $5$ satuan ke kanan dan $8$ satuan ke bawah** ✅  
  <sub>Benar: Nilai $a = 5 > 0$ berarti bergerak ke kanan, dan $b = -8 < 0$ berarti bergerak ke bawah.</sub>

**Pembahasan:** Aturan pergeseran translasi $\binom{a}{b}$ menyatakan:
- Komponen pertama $a = 5 > 0$, artinya bergerak 5 satuan ke kanan.
- Komponen kedua $b = -8 < 0$, artinya bergerak 8 satuan ke bawah.

Dengan demikian, translasi tersebut memindahkan titik sejauh $5$ satuan ke kanan dan $8$ satuan ke bawah.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas9-b03-a-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: koordinat titik awal*

Titik $B$ ditranslasikan oleh $\binom{4}{-5}$ menghasilkan bayangan $B'(1, 3)$. Koordinat titik $B$ mula-mula adalah ...

- A. $B(5, -2)$  
  <sub>Salah: Menjumlahkan koordinat bayangan dengan vektor translasi: $(1 + 4, 3 + (-5))$ alih-alih mengurangkannya.</sub>
- B. $B(-3, -2)$  
  <sub>Salah: Benar pada koordinat $x$, tetapi keliru pada koordinat $y$ dengan menghitung $3 - 5 = -2$.</sub>
- C. $B(8, -3)$  
  <sub>Salah: Posisi nilai absis dan ordinat hasil akhir saling tertukar.</sub>
- **D. $B(-3, 8)$** ✅  
  <sub>Benar: Menghitung koordinat awal melalui pembalikan operasi: $x = 1 - 4 = -3$ dan $y = 3 - (-5) = 8$.</sub>

**Pembahasan:** Diketahui $B(x, y)$ ditranslasikan oleh $\binom{4}{-5}$ menghasilkan $B'(1, 3)$.
Berdasarkan rumus translasi:
$x' = x + a \implies 1 = x + 4 \implies x = 1 - 4 = -3$
$y' = y + b \implies 3 = y + (-5) \implies y = 3 + 5 = 8$

Jadi, koordinat titik awal adalah $B(-3, 8)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas9-b03-a-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: bayangan koordinat translasi*

Bayangan titik $M(6, -3)$ oleh translasi $\binom{-2}{7}$ adalah ...

- A. $M'(4, -10)$  
  <sub>Salah: Salah melakukan operasi pada koordinat ordinat, yaitu $-3 - 7 = -10$.</sub>
- B. $M'(-12, -21)$  
  <sub>Salah: Mengalikan komponen titik dengan translasi alih-alih menjumlahkannya.</sub>
- **C. $M'(4, 4)$** ✅  
  <sub>Benar: Berdasarkan Sifat 3.1, bayangan diperoleh dengan menjumlahkan koordinat: $x' = 6 + (-2) = 4$ dan $y' = -3 + 7 = 4$. Jadi, $M'(4, 4)$.</sub>
- D. $M'(8, -10)$  
  <sub>Salah: Melakukan pengurangan koordinat titik dengan komponen translasi bukan penjumlahan.</sub>

**Pembahasan:** Berdasarkan rumus translasi titik $(x, y)$ oleh $\binom{a}{b}$ diperoleh bayangan $(x', y') = (x + a, y + b)$.
$x' = 6 + (-2) = 4$
$y' = -3 + 7 = 4$
Jadi, koordinat bayangan titik $M$ adalah $M'(4, 4)$.
**Acuan:** siswa — siswa hal.164 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas9-b03-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: menentukan komponen translasi*

Titik $P(-2, 5)$ ditranslasikan oleh $\binom{a}{b}$ sehingga menghasilkan bayangan $P'(3, 1)$. Nilai translasi $\binom{a}{b}$ tersebut adalah ...

- A. $\binom{1}{6}$  
  <sub>Salah: Menjumlahkan koordinat titik asal dengan titik bayangan alih-alih mencari selisihnya.</sub>
- B. $\binom{5}{4}$  
  <sub>Salah: Salah menghitung tanda pada komponen vertikal ($1 - 5$ dihitung $4$).</sub>
- C. $\binom{-5}{4}$  
  <sub>Salah: Terbalik mengurangkan titik asal dengan titik bayangan ($x - x'$ dan $y - y'$).</sub>
- **D. $\binom{5}{-4}$** ✅  
  <sub>Benar: Komponen pergeseran dihitung dari selisih bayangan dengan titik asal: $a = 3 - (-2) = 5$ dan $b = 1 - 5 = -4$.</sub>

**Pembahasan:** Diketahui $P(x, y) = (-2, 5)$ dan $P'(x', y') = (3, 1)$.
Sesuai aturan translasi:
$x' = x + a \Rightarrow 3 = -2 + a \Rightarrow a = 3 - (-2) = 5$
$y' = y + b \Rightarrow 1 = 5 + b \Rightarrow b = 1 - 5 = -4$
Dengan demikian, translasi $\binom{a}{b} = \binom{5}{-4}$.
**Acuan:** pretest — kelas9-b03-p0165-latihan-a-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas9-b03-a-easy-bt01-008
*variasi (angka) | C1 | 1 langkah | jenis: notasi vektor translasi*

Translasi yang memindahkan suatu objek sejauh $5$ satuan ke kanan dan $9$ satuan ke bawah dinotasikan dalam bentuk $\binom{a}{b}$ sebagai ...

- A. $\binom{-9}{5}$  
  <sub>Salah: Menukar letak komponen horizontal dan vertikal.</sub>
- **B. $\binom{5}{-9}$** ✅  
  <sub>Benar: Arah ke kanan bernilai positif ($a = 5$) dan arah ke bawah bernilai negatif ($b = -9$).</sub>
- C. $\binom{-5}{-9}$  
  <sub>Salah: Menganggap pergeseran ke arah kanan bernilai negatif.</sub>
- D. $\binom{5}{9}$  
  <sub>Salah: Mengabaikan tanda negatif untuk pergeseran ke arah bawah.</sub>

**Pembahasan:** Berdasarkan definisi aturan translasi:
- Gerak horizontal: ke kanan bernilai positif ($+5$).
- Gerak vertikal: ke bawah bernilai negatif ($-9$).
Sehingga bentuk translasinya adalah $\binom{5}{-9}$.
**Acuan:** siswa — siswa hal.164 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas9-b03-a-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: definisi translasi*

Perubahan posisi suatu objek (titik, garis, atau bangun) dengan jarak dan arah tertentu pada bidang datar disebut ...

- A. refleksi  
  <sub>Salah: Refleksi merupakan transformasi pencerminan terhadap garis/titik, bukan pergeseran searah.</sub>
- **B. translasi** ✅  
  <sub>Benar: Definisi 3.1 menyatakan bahwa translasi adalah perubahan posisi suatu objek dengan jarak dan arah tertentu.</sub>
- C. rotasi  
  <sub>Salah: Rotasi merupakan transformasi perputaran terhadap suatu pusat dan sudut tertentu.</sub>
- D. dilatasi  
  <sub>Salah: Dilatasi merupakan transformasi pengali ukuran bangun, bukan sekadar perubahan posisi.</sub>

**Pembahasan:** Menurut Definisi 3.1 pada Buku Siswa Matematika Kelas IX halaman 159, translasi (pergeseran) adalah perubahan posisi suatu objek (titik, garis, atau bangun) dengan jarak dan arah tertentu.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas9-b03-a-easy-bt01-010
*orisinal | C2 | 1 langkah | jenis: interpretasi komponen horizontal*

Pada notasi translasi $\binom{-7}{6}$, komponen bilangan $-7$ menunjukkan pergeseran objek sejauh ...

- A. $7$ satuan ke atas  
  <sub>Salah: Tertukar dengan komponen vertikal dan salah memaknai tanda negatif.</sub>
- **B. $7$ satuan ke kiri** ✅  
  <sub>Benar: Komponen pertama menyatakan arah horizontal; tanda negatif berarti bergeser ke arah kiri.</sub>
- C. $7$ satuan ke kanan  
  <sub>Salah: Keliru mengartikan tanda negatif sebagai pergeseran ke arah kanan.</sub>
- D. $7$ satuan ke bawah  
  <sub>Salah: Tertukar antara komponen horizontal ($x$) dengan komponen vertikal ($y$).</sub>

**Pembahasan:** Dalam translasi $\binom{a}{b}$, komponen atas ($a$) menyatakan pergeseran mendatar (horizontal). Karena bernilai negatif ($a = -7 < 0$), maka pergeseran dilakukan sejauh $7$ satuan ke kiri.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas9-b03-a-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: komponen translasi perpindahan*

Sebuah partikel bergerak dari posisi $P(-5, 2)$ menuju posisi $Q(3, -4)$. Pasangan bilangan translasi $\binom{a}{b}$ yang mewakili perpindahan partikel tersebut adalah ...

- A. $\binom{-2}{-2}$  
  <sub>Salah: Menjumlahkan koordinat kedua titik alih-alih mengurangkannya.</sub>
- B. $\binom{-8}{6}$  
  <sub>Salah: Terbalik mengurangkan titik awal dengan titik akhir ($P - Q$).</sub>
- **C. $\binom{8}{-6}$** ✅  
  <sub>Benar: Translasi dari $P$ ke $Q$ dihitung dengan $a = 3 - (-5) = 8$ dan $b = -4 - 2 = -6$.</sub>
- D. $\binom{8}{6}$  
  <sub>Salah: Salah tanda pada operasi pengurangan komponen ordinat.</sub>

**Pembahasan:** Translasi $\binom{a}{b}$ dari titik awal $P(x_1, y_1)$ ke titik tujuan $Q(x_2, y_2)$ dicari dengan rumus:
$$a = x_2 - x_1 = 3 - (-5) = 8$$
$$b = y_2 - y_1 = -4 - 2 = -6$$
Jadi, translasi perpindahannya adalah $\binom{8}{-6}$.
**Acuan:** pretest — kelas9-b03-p0165-latihan-a-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas9-b03-a-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: penjumlahan absis ordinat bayangan*

Titik $A(5, -6)$ ditranslasikan oleh $\binom{-4}{9}$ menghasilkan bayangan $A'(x', y')$. Nilai dari $x' + y'$ adalah ...

- **A. $4$** ✅  
  <sub>Benar: $x' = 5 + (-4) = 1$ dan $y' = -6 + 9 = 3$, sehingga $x' + y' = 1 + 3 = 4$.</sub>
- B. $3$  
  <sub>Salah: Hanya mengambil nilai ordinat $y'$ tanpa menjumlahkannya dengan $x'$.</sub>
- C. $-6$  
  <sub>Salah: Mengurangkan koordinat titik awal dengan matriks translasi ($x' = 9, y' = -15 \Rightarrow 9 + (-15) = -6$).</sub>
- D. $-14$  
  <sub>Salah: Salah menghitung nilai $y'$ menjadi $-6 - 9 = -15$ sehingga $1 + (-15) = -14$.</sub>

**Pembahasan:** Berdasarkan Sifat 3.1:
$$x' = x + a = 5 + (-4) = 1$$
$$y' = y + b = -6 + 9 = 3$$
Koordinat bayangan adalah $A'(1, 3)$.
Nilai dari $x' + y' = 1 + 3 = 4$.
**Acuan:** siswa — siswa hal.164 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas9-b03-a-easy-bt01-013
*variasi (angka) | C2 | 1 langkah | jenis: absis titik bayangan*

Diketahui titik $B(7, -8)$ adalah salah satu titik sudut segitiga. Jika titik $B$ ditranslasikan oleh $\binom{-9}{4}$, absis dari titik bayangan $B'$ adalah ...

- A. $2$  
  <sub>Salah: Salah tanda pada saat menjumlahkan bilangan bulat $7 + (-9)$.</sub>
- B. $16$  
  <sub>Salah: Melakukan operasi pengurangan absis dengan translasi ($7 - (-9) = 16$).</sub>
- C. $-4$  
  <sub>Salah: Keliru mengira absis sebagai ordinat hasil pergeseran ($y' = -8 + 4 = -4$).</sub>
- **D. $-2$** ✅  
  <sub>Benar: Absis bayangan dihitung dari $x' = 7 + (-9) = -2$.</sub>

**Pembahasan:** Translasi titik $B(x, y)$ oleh $\binom{a}{b}$ menghasilkan bayangan $B'(x', y')$ dengan:
$$x' = x + a$$
Absis titik bayangan adalah:
$$x' = 7 + (-9) = -2$$.
**Acuan:** siswa — siswa hal.162 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas9-b03-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: komponen translasi berlawanan arah*

Jika pergeseran dari titik $K$ ke titik $L$ diwakili oleh translasi $\binom{6}{-8}$, maka translasi yang mewakili pergeseran dari titik $L$ ke titik $K$ adalah ...

- A. $\binom{6}{8}$  
  <sub>Salah: Hanya mengubah tanda pada komponen vertikal.</sub>
- **B. $\binom{-6}{8}$** ✅  
  <sub>Benar: Arah berlawanan membalik tanda setiap komponen translasi: $-(6) = -6$ dan $-(-8) = 8$.</sub>
- C. $\binom{-6}{-8}$  
  <sub>Salah: Hanya mengubah tanda pada komponen horizontal.</sub>
- D. $\binom{-8}{6}$  
  <sub>Salah: Menukar posisi komponen horizontal dan vertikal sekaligus keliru tanda.</sub>

**Pembahasan:** Jika translasi dari $K$ ke $L$ adalah $\binom{a}{b}$, maka translasi yang berlawanan arah (dari $L$ ke $K$) adalah kebalikannya, yaitu $\binom{-a}{-b}$.
Dengan demikian, translasi dari $L$ ke $K$ adalah $\binom{-(6)}{-(-8)} = \binom{-6}{8}$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas9-b03-a-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: interpretasi komponen vertikal*

Pada bentuk translasi $\binom{a}{b}$, nilai komponen kedua memenuhi $b < 0$. Hal ini menunjukkan bahwa objek mengalami pergeseran ke arah ...

- **A. bawah** ✅  
  <sub>Benar: Sesuai aturan translasi, nilai $b < 0$ menunjukkan pergeseran ke bawah.</sub>
- B. kanan  
  <sub>Salah: Tertukar dengan arah horizontal pada komponen pertama saat $a > 0$.</sub>
- C. kiri  
  <sub>Salah: Tertukar dengan arah horizontal pada komponen pertama saat $a < 0$.</sub>
- D. atas  
  <sub>Salah: Keliru mengingat kondisi $b > 0$ sebagai arah pergeseran ke atas.</sub>

**Pembahasan:** Berdasarkan definisi komponen translasi $\binom{a}{b}$:
- Komponen mendatar $a$: bernilai positif ($a > 0$) ke kanan, bernilai negatif ($a < 0$) ke kiri.
- Komponen tegak $b$: bernilai positif ($b > 0$) ke atas, bernilai negatif ($b < 0$) ke bawah.
Karena $b < 0$, maka arah pergeserannya adalah ke bawah.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [medium] kelas9-b03-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: translasi titik banyak*

Diketahui segitiga $KLM$ dengan koordinat titik $K(-3, 1)$, $L(1, -2)$, dan $M(5, 4)$ ditranslasikan oleh suatu pergeseran sehingga diperoleh bayangan titik $K'(2, 5)$. Koordinat titik $L'$ dan $M'$ berturut-turut adalah ...

- A. $L'(5, 2)$ dan $M'(9, 8)$  
  <sub>Salah: Keliru menghitung komponen horizontal translasi $2 - (-3) = 4$ bukan $5$.</sub>
- B. $L'(-4, -6)$ dan $M'(0, 0)$  
  <sub>Salah: Terbalik menghitung vektor translasi sebagai titik awal dikurangi titik bayangan yaitu $\binom{-5}{-4}$.</sub>
- C. $L'(6, -6)$ dan $M'(10, 0)$  
  <sub>Salah: Salah menjumlahkan tanda komponen vertikal translasi, mengurangkan bukannya menjumlahkan ordinat.</sub>
- **D. $L'(6, 2)$ dan $M'(10, 8)$** ✅  
  <sub>Benar: Vektor translasi dihitung dari $K$ ke $K'$: $a = 2 - (-3) = 5$ dan $b = 5 - 1 = 4$, jadi translasi adalah $\binom{5}{4}$. Koordinat $L' = (1 + 5, -2 + 4) = (6, 2)$ dan $M' = (5 + 5, 4 + 4) = (10, 8)$.</sub>

**Pembahasan:** Langkah 1: Menentukan komponen translasi $\binom{a}{b}$ dari titik $K(-3, 1)$ ke $K'(2, 5)$:
$$a = 2 - (-3) = 5$$
$$b = 5 - 1 = 4$$
Sehingga matriks translasinya adalah $\binom{5}{4}$.

Langkah 2: Menentukan koordinat bayangan $L'$:
$$L'(1 + 5, -2 + 4) = L'(6, 2)$$

Langkah 3: Menentukan koordinat bayangan $M'$:
$$M'(5 + 5, 4 + 4) = M'(10, 8)$$

Jadi, koordinat bayangan titik $L'$ dan $M'$ berturut-turut adalah $L'(6, 2)$ dan $M'(10, 8)$.
**Acuan:** pretest — kelas9-b03-p0165-latihan-a-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [medium] kelas9-b03-a-medium-bt01-002
*variasi (angka) | C4 | 3 langkah | jenis: bayangan dan titik asal segitiga*

Segitiga $DEF$ ditranslasikan sehingga menghasilkan bayangan segitiga $KLM$, dengan titik $D$ berkorespondensi dengan $K$, $E$ dengan $L$, dan $F$ dengan $M$. Jika diketahui $D(-2, 4)$, $E(5, 1)$, $K(4, -1)$, dan $M(1, 6)$, maka koordinat titik $L$ dan titik $F$ berturut-turut adalah ...

- **A. $L(11, -4)$ dan $F(-5, 11)$** ✅  
  <sub>Benar: Translasi didapat dari $D \to K$: $\binom{a}{b} = \binom{4 - (-2)}{-1 - 4} = \binom{6}{-5}$. Maka $L = E + T = (5 + 6, 1 + (-5)) = (11, -4)$. Untuk mencari $F$, gunakan $F = M - T = (1 - 6, 6 - (-5)) = (-5, 11)$.</sub>
- B. $L(11, 6)$ dan $F(-5, 1)$  
  <sub>Salah: Salah tanda komponen vertikal translasi $b = 5$ bukannya $-5$.</sub>
- C. $L(-1, 6)$ dan $F(-5, 11)$  
  <sub>Salah: Menghitung titik $L$ dengan mengurangkan translasi dari titik $E$ alih-alih menjumlahkannya.</sub>
- D. $L(11, -4)$ dan $F(7, 1)$  
  <sub>Salah: Keliru menghitung titik asal $F$ dengan menjumlahkan vektor translasi ke $M$, bukan mengurangkannya.</sub>

**Pembahasan:** Langkah 1: Menentukan komponen translasi dari pasangan titik yang bersesuaian, yaitu $D(-2, 4)$ dan $K(4, -1)$:
$$a = 4 - (-2) = 6$$
$$b = -1 - 4 = -5$$
Translasi yang bersangkutan adalah $\binom{6}{-5}$.

Langkah 2: Menentukan koordinat bayangan titik $L$ dari titik asal $E(5, 1)$:
$$L = (5 + 6, 1 + (-5)) = (11, -4)$$

Langkah 3: Menentukan koordinat titik asal $F$ dari bayangannya $M(1, 6)$:
$$F = (1 - 6, 6 - (-5)) = (-5, 11)$$

Jadi, koordinat titik $L$ dan $F$ berturut-turut adalah $L(11, -4)$ dan $F(-5, 11)$.
**Acuan:** siswa — siswa hal.165 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [medium] kelas9-b03-a-medium-bt01-003
*orisinal | C4 | 3 langkah | jenis: translasi berurutan*

Titik $P(a, b)$ digeser oleh translasi $T_1 = \binom{5}{-7}$ menghasilkan titik $Q$. Selanjutnya, titik $Q$ digeser kembali oleh translasi $T_2 = \binom{-8}{3}$ sehingga menghasilkan bayangan akhir $P'(-1, 2)$. Nilai dari $2a + b$ adalah ...

- **A. 10** ✅  
  <sub>Benar: Translasi gabungan adalah $\binom{5 + (-8)}{-7 + 3} = \binom{-3}{-4}$. Maka $-1 = a - 3 \implies a = 2$ dan $2 = b - 4 \implies b = 6$. Nilai $2a + b = 2(2) + 6 = 10$.</sub>
- B. 2  
  <sub>Salah: Menghitung translasi gabungan dengan membalik tanda sehingga $a = -4$ dan $b = -2$, lalu $2(-4) + (-2) = -10$ atau salah hitung tanda menghasilkan 2.</sub>
- C. 14  
  <sub>Salah: Keliru memperoleh $a = 4$ dan $b = 6$ sehingga $2(4) + 6 = 14$.</sub>
- D. -6  
  <sub>Salah: Menghitung $P'$ dari titik asal dengan mengurangkan translasi bukan menjumlahkan, sehingga menghasilkan $a = -4, b = -2$, nilai $2a + b = -10$ atau keliru tanda ordinat.</sub>

**Pembahasan:** Langkah 1: Menentukan translasi total pergeseran berurutan:
$$T = T_1 + T_2 = \binom{5 + (-8)}{-7 + 3} = \binom{-3}{-4}$$

Langkah 2: Menghitung koordinat titik asal $P(a, b)$ dari bayangan akhir $P'(-1, 2)$:
$$a + (-3) = -1 \implies a = -1 + 3 = 2$$
$$b + (-4) = 2 \implies b = 2 + 4 = 6$$
Diperoleh $a = 2$ dan $b = 6$.

Langkah 3: Menghitung nilai $2a + b$:
$$2a + b = 2(2) + 6 = 4 + 6 = 10$$

Jadi, nilai dari $2a + b$ adalah 10.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [medium] kelas9-b03-a-medium-bt01-004
*orisinal | C3 | 2 langkah | jenis: translasi titik sudut bangun datar*

Sebuah persegi panjang $ABCD$ memiliki titik-titik sudut dengan koordinat $A(2, -1)$, $B(8, -1)$, dan $D(2, 3)$. Jika persegi panjang tersebut ditranslasikan oleh $\binom{-5}{4}$, maka koordinat bayangan titik $C'$ adalah ...

- A. (-3, 3)  
  <sub>Salah: Keliru mentranslasikan titik $A(2, -1)$ alih-alih titik $C(8, 3)$.</sub>
- B. (13, -1)  
  <sub>Salah: Mengurangkan komponen translasi dari koordinat titik $C$ bukannya menjumlahkannya.</sub>
- **C. $(3, 7)$** ✅  
  <sub>Benar: Titik $C$ memiliki absis sama dengan $B$ ($x = 8$) dan ordinat sama dengan $D$ ($y = 3$), sehingga $C(8, 3)$. Bayangannya $C' = (8 + (-5), 3 + 4) = (3, 7)$.</sub>
- D. (3, 3)  
  <sub>Salah: Keliru mentranslasikan titik $B(8, -1)$ alih-alih titik $C(8, 3)$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat titik $C$ pada persegi panjang $ABCD$.
Karena sisi-sisi persegi panjang sejajar sumbu koordinat:
- Titik $C$ sejajar vertikal dengan titik $B(8, -1)$, sehingga absis titik $C$ adalah $x = 8$.
- Titik $C$ sejajar horizontal dengan titik $D(2, 3)$, sehingga ordinat titik $C$ adalah $y = 3$.
Maka koordinat titik $C$ adalah $(8, 3)$.

Langkah 2: Mentranslasikan titik $C(8, 3)$ oleh $\binom{-5}{4}$:
$$x' = 8 + (-5) = 3$$
$$y' = 3 + 4 = 7$$

Jadi, koordinat bayangan titik $C'$ adalah $(3, 7)$.
**Acuan:** siswa — siswa hal.161

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [medium] kelas9-b03-a-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: menentukan bayangan dan translasi segitiga*

Segitiga $PQR$ dengan titik sudut $P(6, -5)$, $Q(9, -1)$, dan $R(8, 4)$ ditranslasikan oleh suatu pergeseran sehingga menghasilkan bayangan titik $P'(11, -8)$. Koordinat bayangan titik $R'$ dan translasi yang digunakan berturut-turut adalah ...

- **A. $R'(13, 1)$ dan $\binom{5}{-3}$** ✅  
  <sub>Benar: Vektor translasi dihitung dari pergeseran titik $P$ ke $P'$: $\binom{a}{b} = \binom{11 - 6}{-8 - (-5)} = \binom{5}{-3}$. Selanjutnya, bayangan titik $R(8, 4)$ adalah $R'(8 + 5, 4 + (-3)) = R'(13, 1)$.</sub>
- B. $R'(13, -4)$ dan $\binom{5}{-8}$  
  <sub>Salah: Siswa langsung mengambil ordinat titik bayangan $P'$ sebagai komponen pergeseran vertikal tanpa mengurangkan ordinat titik mula-mula.</sub>
- C. $R'(13, 7)$ dan $\binom{5}{3}$  
  <sub>Salah: Siswa salah melakukan operasi pengurangan pada ordinat translasi ($-8 - (-5)$ dihitung $+3$ alih-alih $-3$).</sub>
- D. $R'(3, 7)$ dan $\binom{-5}{3}$  
  <sub>Salah: Siswa terbalik mengurangkan koordinat titik asal dikurangi bayangan ($P - P'$) sehingga tanda komponen translasi berkebalikan.</sub>

**Pembahasan:** Langkah 1: Menentukan komponen translasi $\binom{a}{b}$.
$\binom{a}{b} = \binom{x_{P'} - x_P}{y_{P'} - y_P} = \binom{11 - 6}{-8 - (-5)} = \binom{5}{-3}$.

Langkah 2: Menentukan koordinat bayangan $R'$.
$x_{R'} = x_R + a = 8 + 5 = 13$
$y_{R'} = y_R + b = 4 + (-3) = 1$
Jadi, bayangan titik $R$ adalah $R'(13, 1)$ dan translasinya adalah $\binom{5}{-3}$.
**Acuan:** pretest — kelas9-b03-p0165-latihan-a-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas9-b03-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: translasi titik sudut persegi*

Sebuah persegi $ABCD$ memiliki koordinat titik-titik sudut $A(5, 6)$, $B(9, 6)$, $C(9, 10)$, dan $D(5, 10)$. Jika persegi tersebut ditranslasikan sejauh $7$ satuan ke kiri dan $8$ satuan ke bawah, koordinat bayangan titik $C$ adalah ...

- A. $(16, 18)$  
  <sub>Salah: Siswa mengabaikan arah 'ke kiri' dan 'ke bawah' sehingga menganggap semua komponen pergeseran bernilai positif ($+7$ dan $+8$).</sub>
- **B. $(2, 2)$** ✅  
  <sub>Benar: Pergeseran $7$ satuan ke kiri berarti $a = -7$, dan $8$ satuan ke bawah berarti $b = -8$. Bayangan titik $C(9, 10)$ adalah $C'(9 + (-7), 10 + (-8)) = C'(2, 2)$.</sub>
- C. $(16, 2)$  
  <sub>Salah: Siswa salah menganggap pergeseran ke kiri bernilai positif dan hanya mengurangkan pergeseran vertikal.</sub>
- D. $(2, 18)$  
  <sub>Salah: Siswa hanya menerapkan tanda negatif pada pergeseran horizontal namun salah menganggap pergeseran ke bawah bernilai positif.</sub>

**Pembahasan:** Langkah 1: Menentukan notasi translasi $\binom{a}{b}$.
Pergeseran $7$ satuan ke kiri $\Rightarrow a = -7$.
Pergeseran $8$ satuan ke bawah $\Rightarrow b = -8$.
Bentuk translasi: $\binom{-7}{-8}$.

Langkah 2: Menghitung koordinat bayangan titik $C(9, 10)$.
$x' = 9 + (-7) = 2$
$y' = 10 + (-8) = 2$
Jadi, koordinat bayangan titik $C$ adalah $(2, 2)$.
**Acuan:** siswa — siswa hal.161 Contoh 3.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas9-b03-a-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: translasi dua titik sudut segitiga*

Titik $K(-4, 7)$, $L(3, 5)$, dan $M(-2, -3)$ adalah koordinat titik-titik sudut $\Delta KLM$. Jika $\Delta KLM$ ditranslasikan oleh $\binom{6}{-8}$, maka koordinat bayangan titik $K$ dan titik $M$ berturut-turut adalah ...

- A. $K'(-10, 15)$ dan $M'(-8, 5)$  
  <sub>Salah: Siswa melakukan operasi pengurangan ($x - a, y - b$) alih-alih penjumlahan ($x + a, y + b$).</sub>
- B. $K'(2, 15)$ dan $M'(4, 5)$  
  <sub>Salah: Siswa salah tanda saat menjumlahkan komponen vertikal translasi, menganggap $-8$ sebagai $+8$.</sub>
- **C. $K'(2, -1)$ dan $M'(4, -11)$** ✅  
  <sub>Benar: Bayangan titik $K(-4, 7)$ adalah $K'(-4 + 6, 7 + (-8)) = K'(2, -1)$. Bayangan titik $M(-2, -3)$ adalah $M'(-2 + 6, -3 + (-8)) = M'(4, -11)$.</sub>
- D. $K'(-10, -1)$ dan $M'(-8, -11)$  
  <sub>Salah: Siswa salah tanda pada komponen horizontal, mengurangkan absis dengan $6$.</sub>

**Pembahasan:** Langkah 1: Menentukan bayangan titik $K(-4, 7)$ oleh translasi $\binom{6}{-8}$.
$x_{K'} = -4 + 6 = 2$
$y_{K'} = 7 + (-8) = -1$
Diperoleh $K'(2, -1)$.

Langkah 2: Menentukan bayangan titik $M(-2, -3)$ oleh translasi $\binom{6}{-8}$.
$x_{M'} = -2 + 6 = 4$
$y_{M'} = -3 + (-8) = -11$
Diperoleh $M'(4, -11)$.
**Acuan:** siswa — siswa hal.162 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas9-b03-a-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: translasi berurutan titik berparameter*

Sebuah titik $A(p, q)$ ditranslasikan berturut-turut oleh $T_1 = \binom{-3}{7}$ kemudian dilanjutkan oleh $T_2 = \binom{8}{-5}$ sehingga menghasilkan bayangan akhir $A''(9, 4)$. Nilai dari $2p - q$ adalah ...

- A. $10$  
  <sub>Salah: Siswa salah menghitung nilai ekspresi aljabar dengan menjumlahkan alih-alih mengurangkan ($2(4) + 2 = 10$).</sub>
- **B. $6$** ✅  
  <sub>Benar: Translasi gabungan $T = T_1 + T_2 = \binom{-3 + 8}{7 + (-5)} = \binom{5}{2}$. Dari $A''(p + 5, q + 2) = (9, 4)$, didapat $p = 4$ dan $q = 2$. Maka $2p - q = 2(4) - 2 = 6$.</sub>
- C. $2$  
  <sub>Salah: Siswa tertukar memasukkan nilai $p$ dan $q$ ke bentuk aljabar sehingga menghitung $2(2) - 4 = 0$ atau sekadar menghitung $p - q = 4 - 2 = 2$.</sub>
- D. $-6$  
  <sub>Salah: Siswa melakukan kesalahan tanda saat membalik operasi translasi sehingga memperoleh $p = -4$ dan $q = -2$.</sub>

**Pembahasan:** Langkah 1: Menghitung komponen translasi total.
$T = T_1 + T_2 = \binom{-3}{7} + \binom{8}{-5} = \binom{5}{2}$.

Langkah 2: Menentukan nilai $p$ dan $q$ dari titik akhir $A''(9, 4)$.
$p + 5 = 9 \Rightarrow p = 4$
$q + 2 = 4 \Rightarrow q = 2$

Langkah 3: Menghitung nilai $2p - q$.
$2p - q = 2(4) - 2 = 8 - 2 = 6$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas9-b03-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: menentukan parameter translasi titik*

Titik $P(-2, 3a)$ digeser oleh translasi $\binom{b + 1}{-4}$ sehingga menghasilkan bayangan $P'(5, 8)$. Nilai dari $a + b$ adalah ...

- A. $12$  
  <sub>Salah: Siswa salah menyederhanakan ruas kiri absis sehingga mengira $b = 8$ lalu menjumlahkan dengan $a = 4$ menjadi $12$.</sub>
- B. $6$  
  <sub>Salah: Siswa salah saat memindahkan tanda $-2$ pada persamaan absis sehingga mendapatkan $b = 2$ dan menghasilkan $a + b = 4 + 2 = 6$.</sub>
- C. $7$  
  <sub>Salah: Siswa salah tanda saat memindahkan ruas pada ordinat sehingga menghitung $3a = 8 - 4 = 4$, lalu membulatkan nilai $a$ menjadi $1$ dan memperoleh $1 + 6 = 7$.</sub>
- **D. $10$** ✅  
  <sub>Benar: Dari absis: $-2 + (b + 1) = 5 \Rightarrow b - 1 = 5 \Rightarrow b = 6$. Dari ordinat: $3a + (-4) = 8 \Rightarrow 3a = 12 \Rightarrow a = 4$. Maka $a + b = 4 + 6 = 10$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $b$ dari kesamaan absis.
$x_{P'} = x_P + (b + 1)$
$5 = -2 + b + 1$
$5 = b - 1$
$b = 6$

Langkah 2: Menentukan nilai $a$ dari kesamaan ordinat.
$y_{P'} = y_P + (-4)$
$8 = 3a - 4$
$3a = 12$
$a = 4$

Langkah 3: Menghitung nilai $a + b$.
$a + b = 4 + 6 = 10$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas9-b03-a-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: translasi titik bangun datar*

Sebuah jajargenjang $ABCD$ memiliki koordinat titik $A(-4, 1)$, $B(2, 1)$, $C(4, 5)$, dan $D(-2, 5)$. Jika jajargenjang tersebut ditranslasikan oleh $\binom{-3}{4}$, maka koordinat bayangan titik $B$ dan $D$ berturut-turut adalah ...

- A. $B'(5, -3)$ dan $D'(1, 1)$  
  <sub>Salah: Siswa mengurangkan koordinat titik awal dengan komponen translasi, bukan menjumlahkannya.</sub>
- B. $B'(1, 5)$ dan $D'(-5, 9)$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada perhitungan absis titik $B$, yaitu $2 + (-3)$ dihitung $1$.</sub>
- **C. $B'(-1, 5)$ dan $D'(-5, 9)$** ✅  
  <sub>Benar: Bayangan titik dihitung dengan menjumlahkan koordinat awal dan komponen translasi: $B'(2 + (-3), 1 + 4) = B'(-1, 5)$ dan $D'(-2 + (-3), 5 + 4) = D'(-5, 9)$.</sub>
- D. $B'(-1, 5)$ dan $D'(-1, 9)$  
  <sub>Salah: Siswa salah menjumlahkan bilangan bulat pada absis titik $D$, yaitu $-2 + (-3)$ dihitung $-1$.</sub>

**Pembahasan:** Berdasarkan sifat translasi titik, bayangan titik $(x, y)$ oleh translasi $\binom{a}{b}$ adalah $(x + a, y + b)$.

1. Menentukan bayangan titik $B(2, 1)$:
$B'(2 + (-3), 1 + 4) = B'(-1, 5)$

2. Menentukan bayangan titik $D(-2, 5)$:
$D'(-2 + (-3), 5 + 4) = D'(-5, 9)$

Jadi, koordinat bayangan titik $B$ dan $D$ berturut-turut adalah $B'(-1, 5)$ dan $D'(-5, 9)$.
**Acuan:** siswa — siswa hal.165 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas9-b03-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: translasi titik dua tahap aljabar*

Titik $A(m, -3)$ ditranslasikan oleh $\binom{4}{n}$ sehingga menghasilkan bayangan $A'(2, 5)$. Jika titik $B(2m, n)$ ditranslasikan oleh $\binom{-n}{m}$, maka koordinat bayangan titik $B'$ adalah ...

- A. $B'(-12, 10)$  
  <sub>Salah: Siswa salah melakukan operasi tanda pada ordinat: menghitung $8 - (-2) = 10$ alih-alih $8 + (-2)$.</sub>
- B. $B'(4, 6)$  
  <sub>Salah: Siswa salah melakukan operasi pada absis: menghitung $-4 - (-8) = 4$ alih-alih $-4 + (-8)$.</sub>
- C. $B'(-4, 6)$  
  <sub>Salah: Siswa lupa menggeser komponen absis titik $B$ dan hanya mentranslasikan komponen ordinatnya.</sub>
- **D. $B'(-12, 6)$** ✅  
  <sub>Benar: Dari translasi titik $A$, diperoleh $m + 4 = 2 \implies m = -2$ dan $-3 + n = 5 \implies n = 8$. Maka titik $B(2(-2), 8) = B(-4, 8)$ dan translasinya adalah $\binom{-8}{-2}$. Hasil bayangannya $B'(-4 + (-8), 8 + (-2)) = B'(-12, 6)$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $m$ dan $n$.
Titik $A(m, -3)$ oleh translasi $\binom{4}{n}$ menghasilkan $A'(2, 5)$:
$m + 4 = 2 \iff m = 2 - 4 = -2$
$-3 + n = 5 \iff n = 5 + 3 = 8$

Langkah 2: Menentukan koordinat titik $B$ dan vektor translasi barunya.
Titik $B(2m, n) = B(2(-2), 8) = B(-4, 8)$
Translasi $\binom{-n}{m} = \binom{-8}{-2}$

Langkah 3: Menentukan bayangan titik $B'$:
$B'(-4 + (-8), 8 + (-2)) = B'(-12, 6)$

Jadi, koordinat bayangan titik $B'$ adalah $B'(-12, 6)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas9-b03-a-medium-bt01-012
*orisinal | C3 | 2 langkah | jenis: pergerakan translasi dua tahap*

Sebuah drone pemantau berada pada koordinat titik $P(-6, 9)$. Drone tersebut digerakkan melalui translasi tahap pertama sejauh $8$ satuan ke kanan dan $5$ satuan ke bawah, kemudian dilanjutkan dengan translasi tahap kedua oleh $\binom{-4}{-7}$. Posisi akhir drone tersebut berada pada koordinat ...

- A. $(-2, 7)$  
  <sub>Salah: Siswa menganggap kata 'ke bawah' bernilai positif $+5$ saat membentuk translasi tahap pertama.</sub>
- B. $(2, -3)$  
  <sub>Salah: Siswa salah menghitung tanda pada absis akhir, menghitung $2 + (-4) = 2$.</sub>
- **C. $(-2, -3)$** ✅  
  <sub>Benar: Translasi tahap pertama adalah $\binom{8}{-5}$, sehingga posisi perantara adalah $(-6 + 8, 9 - 5) = (2, 4)$. Translasi tahap kedua oleh $\binom{-4}{-7}$ menghasilkan posisi akhir $(2 + (-4), 4 + (-7)) = (-2, -3)$.</sub>
- D. $(-10, -3)$  
  <sub>Salah: Siswa salah menafsirkan arah pergeseran tahap pertama 'ke kanan' sebagai $-8$ satuan.</sub>

**Pembahasan:** Langkah 1: Menentukan translasi total atau bertahap.
- Pergeseran tahap pertama sejauh $8$ satuan ke kanan dan $5$ satuan ke bawah ditulis sebagai translasi $T_1 = \binom{8}{-5}$.
- Posisi setelah tahap pertama:
$P'(-6 + 8, 9 + (-5)) = P'(2, 4)$

Langkah 2: Menentukan posisi setelah translasi tahap kedua $T_2 = \binom{-4}{-7}$:
$P''(2 + (-4), 4 + (-7)) = P''(-2, -3)$

Jadi, posisi akhir drone tersebut berada pada koordinat $(-2, -3)$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas9-b03-a-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: translasi titik puncak segitiga*

Segitiga sama kaki $ABC$ memiliki alas yang sejajar sumbu-$X$ dengan koordinat ujung-ujung alasnya $A(1, 2)$ dan $B(7, 2)$. Jika titik puncak $C$ memiliki ordinat $6$ dan segitiga tersebut ditranslasikan oleh $\binom{-5}{3}$, maka koordinat bayangan titik puncak $C'$ adalah ...

- A. $C'(2, 9)$  
  <sub>Salah: Siswa keliru menggunakan absis titik $B$ ($x = 7$) sebagai absis puncak $C$, sehingga $7 + (-5) = 2$.</sub>
- **B. $C'(-1, 9)$** ✅  
  <sub>Benar: Karena segitiga sama kaki dengan alas mendatar dari $x = 1$ hingga $x = 7$, absis puncak $C$ berada tepat di tengah alas: $x_C = \frac{1 + 7}{2} = 4$. Jadi titik puncak adalah $C(4, 6)$. Ditranslasikan oleh $\binom{-5}{3}$, diperoleh $C'(4 + (-5), 6 + 3) = C'(-1, 9)$.</sub>
- C. $C'(-1, 3)$  
  <sub>Salah: Siswa mengurangkan komponen vertikal alih-alih menjumlahkannya: $6 - 3 = 3$.</sub>
- D. $C'(9, 9)$  
  <sub>Salah: Siswa salah operasi pengurangan pada absis: $4 - (-5) = 9$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat titik puncak $C$.
Pada segitiga sama kaki dengan alas sejajar sumbu-$X$, sumbu simetri berada tepat di tengah-tengah kedua titik alas.
$x_C = \frac{x_A + x_B}{2} = \frac{1 + 7}{2} = 4$
Karena ordinat titik $C$ adalah $6$, maka koordinat titik puncak adalah $C(4, 6)$.

Langkah 2: Menentukan bayangan titik puncak oleh translasi $\binom{-5}{3}$:
$x' = 4 + (-5) = -1$
$y' = 6 + 3 = 9$

Diperoleh koordinat bayangan $C'(-1, 9)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas9-b03-a-medium-bt01-014
*variasi (angka) | C3 | 3 langkah | jenis: translasi garis lurus*

Hasil translasi garis lurus $4x + 5y = 20$ oleh $\binom{-1}{7}$ adalah ...

- **A. $4x + 5y = 51$** ✅  
  <sub>Benar: Dua titik pada garis $4x + 5y = 20$ adalah $(5, 0)$ dan $(0, 4)$. Ditranslasikan oleh $\binom{-1}{7}$ menjadi $(5-1, 0+7) = (4, 7)$ dan $(0-1, 4+7) = (-1, 11)$. Persamaan garis melalui $(4, 7)$ dan $(-1, 11)$ adalah $y - 7 = \frac{11 - 7}{-1 - 4}(x - 4) \iff y - 7 = -\frac{4}{5}(x - 4) \iff 5y - 35 = -4x + 16 \iff 4x + 5y = 51$.</sub>
- B. $4x + 5y = 20$  
  <sub>Salah: Siswa mengira garis yang digeser memiliki persamaan yang sama persis tanpa mengubah konstanta.</sub>
- C. $4x + 5y = -11$  
  <sub>Salah: Siswa salah memasukkan pergeseran tanpa membalik tanda operasi pada substitusi variabel: $4(x - 1) + 5(y + 7) = 20 \iff 4x + 5y + 31 = 20 \iff 4x + 5y = -11$.</sub>
- D. $5x + 4y = 51$  
  <sub>Salah: Siswa tertukar menempatkan koefisien variabel $x$ dan $y$ saat menyusun persamaan garis bayangan.</sub>

**Pembahasan:** Langkah 1: Tentukan dua titik sembarang pada garis $4x + 5y = 20$.
- Jika $y = 0$, maka $4x = 20 \implies x = 5$, sehingga diperoleh titik $(5, 0)$.
- Jika $x = 0$, maka $5y = 20 \implies y = 4$, sehingga diperoleh titik $(0, 4)$.

Langkah 2: Translasikan kedua titik tersebut oleh $\binom{-1}{7}$.
- Titik $(5, 0) \to (5 + (-1), 0 + 7) = (4, 7)$.
- Titik $(0, 4) \to (0 + (-1), 4 + 7) = (-1, 11)$.

Langkah 3: Tentukan persamaan garis yang melalui titik $(4, 7)$ dan $(-1, 11)$.
$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$$
$$\frac{y - 7}{11 - 7} = \frac{x - 4}{-1 - 4}$$
$$\frac{y - 7}{4} = \frac{x - 4}{-5}$$
$$-5(y - 7) = 4(x - 4)$$
$$-5y + 35 = 4x - 16$$
$$4x + 5y = 35 + 16$$
$$4x + 5y = 51$$

Jadi, hasil translasi garis tersebut adalah $4x + 5y = 51$.
**Acuan:** siswa — siswa hal.162 Contoh 3.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas9-b03-a-medium-bt01-015
*variasi (angka) | C3 | 3 langkah | jenis: translasi garis lurus*

Hasil translasi garis lurus $5x - 7y = 35$ oleh $\binom{2}{-1}$ adalah ...

- A. $5x - 7y = 18$  
  <sub>Salah: Siswa salah memasukkan pergeseran tanpa membalik tanda operasi pada substitusi variabel: $5(x + 2) - 7(y - 1) = 35 \iff 5x - 7y + 17 = 35 \iff 5x - 7y = 18$.</sub>
- B. $5x - 7y = 35$  
  <sub>Salah: Siswa mengira translasi tidak mengubah nilai konstanta pada persamaan garis.</sub>
- C. $7x - 5y = 52$  
  <sub>Salah: Siswa tertukar menempatkan koefisien $x$ dan $y$ pada persamaan garis akhir.</sub>
- **D. $5x - 7y = 52$** ✅  
  <sub>Benar: Dua titik pada garis $5x - 7y = 35$ adalah $(7, 0)$ dan $(0, -5)$. Ditranslasikan oleh $\binom{2}{-1}$ menjadi $(7+2, 0-1) = (9, -1)$ dan $(0+2, -5-1) = (2, -6)$. Persamaan garis melalui $(9, -1)$ dan $(2, -6)$ adalah $y - (-1) = \frac{-6 - (-1)}{2 - 9}(x - 9) \iff y + 1 = \frac{5}{7}(x - 9) \iff 7y + 7 = 5x - 45 \iff 5x - 7y = 52$.</sub>

**Pembahasan:** Langkah 1: Tentukan dua titik sembarang pada garis $5x - 7y = 35$.
- Jika $y = 0$, maka $5x = 35 \implies x = 7$, didapat titik $(7, 0)$.
- Jika $x = 0$, maka $-7y = 35 \implies y = -5$, didapat titik $(0, -5)$.

Langkah 2: Translasikan kedua titik tersebut oleh $\binom{2}{-1}$.
- Titik $(7, 0) \to (7 + 2, 0 + (-1)) = (9, -1)$.
- Titik $(0, -5) \to (0 + 2, -5 + (-1)) = (2, -6)$.

Langkah 3: Tentukan persamaan garis yang melalui titik $(9, -1)$ dan $(2, -6)$.
$$\frac{y - y_1}{y_2 - y_1} = \frac{x - x_1}{x_2 - x_1}$$
$$\frac{y - (-1)}{-6 - (-1)} = \frac{x - 9}{2 - 9}$$
$$\frac{y + 1}{-5} = \frac{x - 9}{-7}$$
$$-7(y + 1) = -5(x - 9)$$
$$-7y - 7 = -5x + 45$$
$$5x - 7y = 45 + 7$$
$$5x - 7y = 52$$

Jadi, hasil translasi garis tersebut adalah $5x - 7y = 52$.
**Acuan:** siswa — siswa hal.163 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [hard] kelas9-b03-a-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: rekonstruksi translasi segitiga*

Segitiga $DEF$ ditranslasikan oleh suatu pergeseran sehingga menghasilkan bayangan segitiga $XYZ$, dengan $D$ berkorespondensi ke $X$, $E$ ke $Y$, dan $F$ ke $Z$. Diketahui koordinat $D(-4, 7)$, $E(5, -1)$, $X(3, 2)$, dan bayangan titik $F$ adalah $Z(-2, 9)$. Koordinat titik $Y$ dan titik $F$ berturut-turut adalah ...

- **A. $Y(12, -6)$ dan $F(-9, 14)$** ✅  
  <sub>Benar: Vektor translasi dihitung dari pasangan titik sekawan $D$ dan $X$: $T = X - D = (3 - (-4), 2 - 7) = \binom{7}{-5}$. Koordinat $Y$ adalah bayangan $E$: $Y = E + T = (5 + 7, -1 + (-5)) = (12, -6)$. Titik awal $F$ diperoleh dari $F = Z - T = (-2 - 7, 9 - (-5)) = (-9, 14)$.</sub>
- B. $Y(-2, 4)$ dan $F(-9, 14)$  
  <sub>Salah: Siswa menggunakan translasi terbalik $\binom{-7}{5}$ untuk mencari $Y$, namun benar mencari $F$.</sub>
- C. $Y(12, -6)$ dan $F(5, 4)$  
  <sub>Salah: Siswa salah saat mencari titik awal $F$ dengan menjumlahkan translasi ke bayangan $Z$ ($Z + T$), bukan mengurangkannya.</sub>
- D. $Y(-2, 4)$ dan $F(5, 4)$  
  <sub>Salah: Siswa terbalik menentukan vektor translasi menjadi $D - X = \binom{-7}{5}$ lalu menerapkan secara keliru ke semua titik.</sub>

**Pembahasan:** Langkah 1: Tentukan komponen translasi $T = \binom{a}{b}$ dari pergeseran titik $D(-4, 7)$ ke $X(3, 2)$:
$$a = 3 - (-4) = 7$$
$$b = 2 - 7 = -5$$
Jadi, translasinya adalah $T = \binom{7}{-5}$.

Langkah 2: Tentukan bayangan $Y$ dari titik $E(5, -1)$:
$$Y = (5 + 7, -1 + (-5)) = (12, -6)$$

Langkah 3: Tentukan titik asal $F$ dari bayangannya $Z(-2, 9)$:
$$x_F + 7 = -2 \implies x_F = -2 - 7 = -9$$
$$y_F + (-5) = 9 \implies y_F = 9 - (-5) = 14$$
Sehingga $F(-9, 14)$.

Jadi, koordinat titik $Y$ dan $F$ berturut-turut adalah $Y(12, -6)$ dan $F(-9, 14)$.
**Acuan:** siswa — siswa hal.165 Latihan A Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [hard] kelas9-b03-a-hard-bt01-002
*orisinal | C5 | 6 langkah | jenis: evaluasi translasi segitiga*

Segitiga $ABC$ memiliki koordinat titik $A(4, -2)$, $B(8, -2)$, dan $C(6, 4)$. Segitiga tersebut ditranslasikan oleh $T_1 = \binom{-5}{3}$ menghasilkan segitiga $A'B'C'$, kemudian dilanjutkan dengan translasi $T_2 = \binom{a}{b}$ sehingga menghasilkan segitiga $A''B''C''$. Jika titik $C''$ terletak pada sumbu-$Y$ dan ordinat dari titik $A''$ adalah $5$, maka koordinat titik $B''$ adalah ...

- **A. $(2, 5)$** ✅  
  <sub>Benar: Translasi $T_1$ menghasilkan $C'(1, 7)$ dan $A'(-1, 1)$. Syarat $C''$ pada sumbu-$Y$ memberi $1 + a = 0 \implies a = -1$. Syarat ordinat $A'' = 5$ memberi $1 + b = 5 \implies b = 4$. Bayangan $B(8, -2)$ oleh $T_1$ adalah $B'(3, 1)$, lalu oleh $T_2 = \binom{-1}{4}$ menghasilkan $B''(2, 5)$.</sub>
- B. $(2, 4)$  
  <sub>Salah: Siswa salah mengurangkan pada persamaan ordinat sehingga memperoleh $b = 3$ lalu menghasilkan ordinat $4$.</sub>
- C. $(3, 5)$  
  <sub>Salah: Siswa lupa menggeser absis titik $B'$ dengan komponen $a = -1$ sehingga tetap menggunakan absis $3$.</sub>
- D. (-2, 5)  
  <sub>Salah: Siswa keliru menuliskan koordinat titik $A''$ sebagai jawaban akhir bukannya koordinat titik $B''$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat $C'$ setelah $T_1$:
$C' = (6 + (-5), 4 + 3) = (1, 7)$.

Langkah 2: Menentukan nilai $a$ dari posisi titik $C''$:
$C'' = (1 + a, 7 + b)$. Karena $C''$ berada pada sumbu-$Y$, maka absisnya bernilai $0$:
$1 + a = 0 \implies a = -1$.

Langkah 3: Menentukan koordinat $A'$ setelah $T_1$:
$A' = (4 + (-5), -2 + 3) = (-1, 1)$.

Langkah 4: Menentukan nilai $b$ dari ordinat titik $A''$:
$A'' = (-1 + a, 1 + b)$. Karena ordinat $A'' = 5$:
$1 + b = 5 \implies b = 4$.

Langkah 5: Menentukan koordinat $B'$ setelah $T_1$:
$B' = (8 + (-5), -2 + 3) = (3, 1)$.

Langkah 6: Menerapkan translasi $T_2 = \binom{-1}{4}$ pada $B'$:
$B'' = (3 + (-1), 1 + 4) = (2, 5)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [hard] kelas9-b03-a-hard-bt01-003
*variasi (konteks) | C5 | 4 langkah | jenis: translasi garis kontekstual*

Sebuah jalur rel kereta api pada peta pemodelan dinyatakan oleh persamaan garis lurus $4x - 3y = 24$. Akibat adanya perbaikan rute, jalur rel tersebut digeser dengan translasi sejauh $5$ satuan ke kanan dan $2$ satuan ke bawah. Persamaan garis lurus yang menyatakan rute jalur rel kereta api yang baru adalah ...

- A. $4x - 3y = 10$  
  <sub>Salah: Siswa langsung mengurangi konstanta $24$ dengan komponen translasi tanpa memperhatikan perkalian koefisien.</sub>
- **B. $4x - 3y = 50$** ✅  
  <sub>Benar: Translasi $5$ ke kanan dan $2$ ke bawah dinotasikan $\binom{5}{-2}$. Substitusi $x = x' - 5$ dan $y = y' + 2$ menghasilkan $4(x' - 5) - 3(y' + 2) = 24 \implies 4x - 3y = 50$.</sub>
- C. $4x - 3y = -2$  
  <sub>Salah: Siswa salah menggunakan rumus substitusi translasi menjadi $x = x' + 5$ dan $y = y' - 2$.</sub>
- D. $4x - 3y = 38$  
  <sub>Salah: Siswa salah menghitung tanda saat mendistribusikan $-3(y' + 2)$ menjadi $-3y' + 6$.</sub>

**Pembahasan:** Langkah 1: Menyatakan arah translasi ke dalam bentuk vektor $\binom{a}{b}$:
Pergeseran $5$ satuan ke kanan dan $2$ satuan ke bawah adalah $T = \binom{5}{-2}$.

Langkah 2: Menentukan substitusi titik awal $(x, y)$:
$x' = x + 5 \implies x = x' - 5$
$y' = y - 2 \implies y = y' + 2$.

Langkah 3: Mensubstitusikan ke dalam persamaan garis awal:
$4(x' - 5) - 3(y' + 2) = 24$
$4x' - 20 - 3y' - 6 = 24$
$4x' - 3y' - 26 = 24$.

Langkah 4: Menyederhanakan persamaan garis:
$4x' - 3y' = 24 + 26$
$4x - 3y = 50$.
**Acuan:** siswa — siswa hal.162 Contoh 3.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [hard] kelas9-b03-a-hard-bt01-004
*orisinal | C5 | 6 langkah | jenis: rekonstruksi titik berimpit*

Titik $P(2a - 3, b + 1)$ ditranslasikan oleh $T_1 = \binom{3}{-2}$ menghasilkan bayangan $P'$, sedangkan titik $Q(a + 4, 2b - 3)$ ditranslasikan oleh $T_2 = \binom{2}{1}$ menghasilkan bayangan $Q'$. Jika bayangan titik $P$ dan titik $Q$ berimpit pada satu titik yang sama, maka koordinat titik bayangan persekutuan tersebut adalah ...

- A. $(6, 0)$  
  <sub>Salah: Siswa lupa mengalikan nilai $a = 6$ dengan $2$ saat mensubstitusikan ke absis bayangan.</sub>
- B. $(12, 2)$  
  <sub>Salah: Siswa salah menyelesaikan persamaan ordinat sehingga memperoleh $b = 3$ lalu bayangannya menjadi $(12, 2)$.</sub>
- C. $(6, 1)$  
  <sub>Salah: Siswa mengira nilai pasangan parameter $(a, b)$ merupakan koordinat titik bayangan akhir.</sub>
- **D. $(12, 0)$** ✅  
  <sub>Benar: Bayangan $P'$ adalah $(2a, b - 1)$ dan $Q'$ adalah $(a + 6, 2b - 2)$. Syarat berimpit menghasilkan $2a = a + 6 \implies a = 6$ dan $b - 1 = 2b - 2 \implies b = 1$. Koordinat bayangannya adalah $(2(6), 1 - 1) = (12, 0)$.</sub>

**Pembahasan:** Langkah 1: Menentukan koordinat bayangan $P'$ oleh translasi $T_1 = \binom{3}{-2}$:
$x_{P'} = (2a - 3) + 3 = 2a$
$y_{P'} = (b + 1) + (-2) = b - 1$.
Jadi, $P'(2a, b - 1)$.

Langkah 2: Menentukan koordinat bayangan $Q'$ oleh translasi $T_2 = \binom{2}{1}$:
$x_{Q'} = (a + 4) + 2 = a + 6$
$y_{Q'} = (2b - 3) + 1 = 2b - 2$.
Jadi, $Q'(a + 6, 2b - 2)$.

Langkah 3: Menggunakan syarat kedua bayangan berimpit pada absis:
$x_{P'} = x_{Q'}$
$2a = a + 6 \implies a = 6$.

Langkah 4: Menggunakan syarat kedua bayangan berimpit pada ordinat:
$y_{P'} = y_{Q'}$
$b - 1 = 2b - 2 \implies 2b - b = -1 + 2 \implies b = 1$.

Langkah 5: Mensubstitusikan nilai $a = 6$ dan $b = 1$ ke koordinat bayangan:
Absis: $2a = 2(6) = 12$.
Ordinat: $b - 1 = 1 - 1 = 0$.

Langkah 6: Menuliskan hasil akhir koordinat bayangan persekutuan:
Titik bayangannya adalah $(12, 0)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas9-b03-a-hard-bt01-005
*variasi (angka) | C5 | 3 langkah | jenis: rekonstruksi koordinat bangun datar*

Diketahui segitiga $KLM$ dengan koordinat $K(-7, 5)$, $L(3, -2)$, dan $M(1, 6)$ ditranslasikan oleh translasi $T$ sehingga menghasilkan bayangan $K'(-1, 1)$. Pasangan translasi $T$ serta koordinat titik $L'$ dan $M'$ berturut-turut adalah ...

- A. $\binom{6}{6}$, $L'(9, 4)$, dan $M'(7, 12)$  
  <sub>Salah: Salah melakukan operasi tanda pada komponen kedua translasi ($1 - (-5)$ alih-alih $1 - 5$).</sub>
- B. $\binom{6}{-4}$, $L'(9, -2)$, dan $M'(7, 6)$  
  <sub>Salah: Hanya mentranslasikan absis titik $L$ dan $M$, ordinat tidak ditambahkan dengan komponen vertikal translasi.</sub>
- **C. $\binom{6}{-4}$, $L'(9, -6)$, dan $M'(7, 2)$** ✅  
  <sub>Benar: Vektor translasi $T = K' - K = \binom{-1 - (-7)}{1 - 5} = \binom{6}{-4}$. Bayangan $L' = (3 + 6, -2 + (-4)) = (9, -6)$ dan $M' = (1 + 6, 6 + (-4)) = (7, 2)$.</sub>
- D. $\binom{-6}{4}$, $L'(-3, 2)$, dan $M'(-5, 10)$  
  <sub>Salah: Terbalik mengurangkan koordinat titik awal dengan bayangan saat mencari komponen translasi ($T = K - K'$).</sub>

**Pembahasan:** Langkah 1: Menentukan komponen translasi $T = \binom{a}{b}$.
$K(-7, 5) \xrightarrow{\binom{a}{b}} K'(-1, 1)$
$-7 + a = -1 \implies a = -1 + 7 = 6$
$5 + b = 1 \implies b = 1 - 5 = -4$
Jadi, translasi $T = \binom{6}{-4}$.

Langkah 2: Menentukan bayangan titik $L(3, -2)$.
$L' = (3 + 6, -2 + (-4)) = (9, -6)$

Langkah 3: Menentukan bayangan titik $M(1, 6)$.
$M' = (1 + 6, 6 + (-4)) = (7, 2)$

Jadi, translasi yang memenuhi adalah $\binom{6}{-4}$, $L'(9, -6)$, dan $M'(7, 2)$.
**Acuan:** pretest — kelas9-b03-p0165-latihan-a-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas9-b03-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: translasi titik berat segitiga*

Segitiga $ABC$ memiliki titik-titik sudut $A(1, 2)$, $B(7, 2)$, dan $C(1, 8)$. Segitiga tersebut ditranslasikan berturut-turut oleh $T_1 = \binom{a}{5}$ dan dilanjutkan oleh $T_2 = \binom{-2}{b}$. Jika titik berat dari segitiga bayangan akhir berada tepat pada titik asal $(0, 0)$, maka nilai dari $a - b$ adalah ...

- A. -8  
  <sub>Salah: Terbalik menghitung pengurangan menjadi $b - a = -9 - (-1)$.</sub>
- B. -10  
  <sub>Salah: Menghitung nilai dari $a + b = -1 + (-9)$ alih-alih $a - b$.</sub>
- C. 10  
  <sub>Salah: Salah menghitung titik berat dengan hanya menjumlahkan koordinat titik sudut tanpa membaginya dengan 3.</sub>
- **D. 8** ✅  
  <sub>Benar: Titik berat awal adalah $(3, 4)$. Translasi total adalah $\binom{a - 2}{b + 5}$. Titik berat akhir $(3 + a - 2, 4 + b + 5) = (0, 0)$ menghasilkan $a = -1$ dan $b = -9$, sehingga $a - b = -1 - (-9) = 8$.</sub>

**Pembahasan:** Langkah 1: Tentukan koordinat titik berat segitiga awal $G(x_G, y_G)$.
$x_G = \frac{1 + 7 + 1}{3} = \frac{9}{3} = 3$
$y_G = \frac{2 + 2 + 8}{3} = \frac{12}{3} = 4$
Jadi, $G(3, 4)$.

Langkah 2: Tentukan translasi gabungan $T = T_1 + T_2$.
$T = \binom{a}{5} + \binom{-2}{b} = \binom{a - 2}{b + 5}$

Langkah 3: Tentukan nilai $a$ dan $b$ dari bayangan titik berat $G'$.
$G'(3 + a - 2, 4 + b + 5) = G'(a + 1, b + 9)$
Karena $G'$ berada di $(0, 0)$:
$a + 1 = 0 \implies a = -1$
$b + 9 = 0 \implies b = -9$

Langkah 4: Hitung nilai $a - b$.
$a - b = -1 - (-9) = -1 + 9 = 8$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas9-b03-a-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: analisis irisan translasi persegi*

Sebuah persegi $ABCD$ memiliki koordinat titik sudut $A(2, 3)$, $B(8, 3)$, $C(8, 9)$, dan $D(2, 9)$. Persegi tersebut ditranslasikan oleh $T = \binom{a}{b}$ dengan $a > 0$ dan $b > 0$. Jika daerah persekutuan (irisan) antara persegi $ABCD$ dan bayangannya $A'B'C'D'$ berbentuk persegi dengan luas $9\text{ satuan luas}$, maka nilai dari $a + b$ adalah ...

- A. 9  
  <sub>Salah: Mengira nilai penjumlahan komponen translasi sama dengan luas daerah irisan.</sub>
- B. 12  
  <sub>Salah: Menjumlahkan panjang sisi persegi mula-mula ($6 + 6$).</sub>
- **C. 6** ✅  
  <sub>Benar: Panjang sisi persegi asal adalah $8 - 2 = 6$. Luas daerah irisan 9 satuan luas berbentuk persegi memiliki sisi 3. Karena digeser ke kanan dan atas, pergeserannya adalah $a = 6 - 3 = 3$ dan $b = 6 - 3 = 3$. Maka $a + b = 3 + 3 = 6$.</sub>
- D. 3  
  <sub>Salah: Hanya menyebutkan nilai salah satu komponen translasi ($a$ atau $b$).</sub>

**Pembahasan:** Langkah 1: Menghitung panjang sisi persegi mula-mula $ABCD$.
$s = x_B - x_A = 8 - 2 = 6$

Langkah 2: Menghitung panjang sisi daerah persekutuan (irisan).
Daerah irisan berbentuk persegi dengan luas $9\text{ satuan luas}$, sehingga panjang sisi irisan adalah:
$s_{\text{irisan}} = \sqrt{9} = 3$

Langkah 3: Menganalisis pergeseran horizontal ($a$) dan vertikal ($b$).
Karena $a > 0$ dan $b > 0$, persegi digeser ke kanan sejauh $a$ dan ke atas sejauh $b$.
Panjang overlap horizontal: $s - a = s_{\text{irisan}} \implies 6 - a = 3 \implies a = 3$
Panjang overlap vertikal: $s - b = s_{\text{irisan}} \implies 6 - b = 3 \implies b = 3$

Langkah 4: Menghitung nilai $a + b$.
$a + b = 3 + 3 = 6$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas9-b03-a-hard-bt01-008
*variasi (angka) | C5 | 4 langkah | jenis: rekonstruksi translasi segitiga berpasangan*

Segitiga $DEF$ ditranslasikan sehingga menghasilkan bayangan segitiga $JKL$, dengan titik $D$ berkorespondensi ke titik $J$, $E$ ke $K$, dan $F$ ke $L$. Diketahui koordinat $D(-4, 7)$, $E(6, -2)$, bayangan titik $D$ adalah $J(5, -1)$, dan bayangan titik $F$ adalah $L(1, 4)$. Jika titik $K$ berkoordinat $(x_K, y_K)$ dan titik $F$ berkoordinat $(x_F, y_F)$, nilai dari $(x_K + y_K) - (x_F + y_F)$ adalah ...

- A. -1  
  <sub>Salah: Siswa terbalik melakukan pengurangan $(x_F + y_F) - (x_K + y_K) = 4 - 5 = -1$.</sub>
- **B. 1** ✅  
  <sub>Benar: Vektor translasi $T = J - D = \binom{5 - (-4)}{-1 - 7} = \binom{9}{-8}$. Titik $K = E + T = (6 + 9, -2 + (-8)) = (15, -10)$, sehingga $x_K + y_K = 15 + (-10) = 5$. Titik $F = L - T = (1 - 9, 4 - (-8)) = (-8, 12)$, sehingga $x_F + y_F = -8 + 12 = 4$. Maka, $(x_K + y_K) - (x_F + y_F) = 5 - 4 = 1$.</sub>
- C. 9  
  <sub>Salah: Siswa menjumlahkan kedua nilai $(5 + 4)$ alih-alih mengurangkannya.</sub>
- D. -31  
  <sub>Salah: Siswa salah menentukan $F$ dengan menjumlahkan $L + T = (10, -4)$ sehingga $x_F + y_F = 6$, dan salah menghitung $K$ menjadi $(-3, 6)$ sehingga $(-3 + 6) - 6 = -3$ atau salah tanda pada operasi komponen vertikal.</sub>

**Pembahasan:** Langkah 1: Menentukan vektor translasi $T = \binom{a}{b}$.
Karena titik $D$ berpindah ke $J$:
$a = x_J - x_D = 5 - (-4) = 9$
$b = y_J - y_D = -1 - 7 = -8$
Jadi, translasi yang memetakan segitiga adalah $T = \binom{9}{-8}$.

Langkah 2: Menentukan koordinat titik $K$.
Karena titik $E$ berkorespondensi ke $K$:
$x_K = x_E + a = 6 + 9 = 15$
$y_K = y_E + b = -2 + (-8) = -10$
Maka, koordinat $K(15, -10)$ dan diperoleh $x_K + y_K = 15 + (-10) = 5$.

Langkah 3: Menentukan koordinat titik $F$.
Karena titik $F$ berkorespondensi ke $L$, maka $L = F + T \Rightarrow F = L - T$:
$x_F = x_L - a = 1 - 9 = -8$
$y_F = y_L - b = 4 - (-8) = 12$
Maka, koordinat $F(-8, 12)$ dan diperoleh $x_F + y_F = -8 + 12 = 4$.

Langkah 4: Menghitung nilai yang ditanyakan:
$(x_K + y_K) - (x_F + y_F) = 5 - 4 = 1$.
**Acuan:** siswa — siswa hal.165 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas9-b03-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: parameter translasi pusat simetri*

Sebuah persegi panjang $ABCD$ memiliki dua titik sudut yang saling berhadapan di $A(-3, -2)$ dan $C(5, 4)$. Persegi panjang tersebut ditranslasikan berturut-turut oleh translasi $T_1 = \binom{m}{-3}$ dan dilanjutkan oleh $T_2 = \binom{2}{n}$. Jika pusat simetri putar dari bayangan persegi panjang tersebut berada tepat pada titik asal $(0, 0)$, maka nilai dari $m \times n$ adalah ...

- A. 6  
  <sub>Salah: Siswa salah menentukan tanda salah satu parameter (misalnya $m = 3$ dan $n = 2$).</sub>
- B. -10  
  <sub>Salah: Siswa menggunakan titik $A$ sebagai acuan alih-alih titik pusat simetri diagonal.</sub>
- **C. -6** ✅  
  <sub>Benar: Pusat simetri awal persegi panjang adalah titik tengah diagonal $AC$, yaitu $M\left(\frac{-3+5}{2}, \frac{-2+4}{2}\right) = (1, 1)$. Translasi gabungannya adalah $T = T_1 + T_2 = \binom{m + 2}{n - 3}$. Titik pusat bayangan menjadi $M'(1 + m + 2, 1 + n - 3) = (m + 3, n - 2)$. Karena $M'$ berimpit dengan $(0, 0)$, maka $m + 3 = 0 \Rightarrow m = -3$ dan $n - 2 = 0 \Rightarrow n = 2$. Hasil kalinya adalah $m \times n = -3 \times 2 = -6$.</sub>
- D. -4  
  <sub>Salah: Siswa keliru menjumlahkan komponen translasi sehingga memperoleh $m = -2$ dan $n = 2$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat simetri awal persegi panjang $ABCD$.
Titik pusat simetri persegi panjang adalah titik tengah diagonal yang menghubungkan dua titik sudut yang saling berhadapan ($A$ dan $C$):
$x_M = \frac{-3 + 5}{2} = \frac{2}{2} = 1$
$y_M = \frac{-2 + 4}{2} = \frac{2}{2} = 1$
Jadi, pusat simetri mula-mula berada pada titik $M(1, 1)$.

Langkah 2: Menentukan translasi gabungan $T$.
Translasi pertama $T_1 = \binom{m}{-3}$ dan translasi kedua $T_2 = \binom{2}{n}$.
Translasi gabungan $T = T_1 + T_2 = \binom{m + 2}{-3 + n} = \binom{m + 2}{n - 3}$.

Langkah 3: Menentukan koordinat bayangan pusat simetri $M'$.
$x_{M'} = x_M + (m + 2) = 1 + m + 2 = m + 3$
$y_{M'} = y_M + (n - 3) = 1 + n - 3 = n - 2$.

Karena pusat simetri bayangan berada di titik asal $(0, 0)$, maka:
$m + 3 = 0 \Rightarrow m = -3$
$n - 2 = 0 \Rightarrow n = 2$.

Langkah 4: Menghitung nilai $m \times n$:
$m \times n = (-3) \times 2 = -6$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas9-b03-a-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: rekonstruksi posisi translasi berantai*

Sebuah objek bergerak pada bidang koordinat mulai dari titik $P_0(2, -5)$. Objek tersebut mengalami empat pergeseran berturut-turut:
- Pergeseran pertama oleh $T_1 = \binom{a}{3}$
- Pergeseran kedua oleh $T_2 = \binom{-4}{b}$
- Pergeseran ketiga oleh $T_3 = \binom{2a}{-1}$
- Pergeseran keempat oleh $T_4 = \binom{5}{2b}$

Setelah pergeseran keempat selesai, objek berada di titik $P_4(18, 9)$. Koordinat posisi objek setelah pergeseran kedua ($P_2$) adalah ...

- A. (1, 4)  
  <sub>Salah: Siswa salah tanda saat menyelesaikan nilai $a$ dan $b$ sehingga pergeseran menghasilkan titik yang keliru.</sub>
- B. (13, 1)  
  <sub>Salah: Siswa menghitung posisi setelah pergeseran ketiga ($P_3$).</sub>
- C. (7, -2)  
  <sub>Salah: Siswa hanya menghitung posisi setelah pergeseran pertama ($P_1$).</sub>
- **D. (3, 2)** ✅  
  <sub>Benar: Total pergeseran horizontal adalah $a - 4 + 2a + 5 = 3a + 1$, sehingga $2 + 3a + 1 = 18 \Rightarrow 3a = 15 \Rightarrow a = 5$. Total pergeseran vertikal adalah $3 + b - 1 + 2b = 3b + 2$, sehingga $-5 + 3b + 2 = 9 \Rightarrow 3b = 12 \Rightarrow b = 4$. Posisi setelah pergeseran pertama adalah $P_1 = (2 + 5, -5 + 3) = (7, -2)$. Posisi setelah pergeseran kedua adalah $P_2 = (7 - 4, -2 + 4) = (3, 2)$.</sub>

**Pembahasan:** Langkah 1: Menyusun persamaan pergeseran horizontal total dari $P_0$ ke $P_4$.
$x_4 = x_0 + a + (-4) + 2a + 5$
$18 = 2 + 3a + 1$
$18 = 3a + 3$
$3a = 15 \Rightarrow a = 5$.

Langkah 2: Menyusun persamaan pergeseran vertikal total dari $P_0$ ke $P_4$.
$y_4 = y_0 + 3 + b + (-1) + 2b$
$9 = -5 + 3b + 2$
$9 = 3b - 3$
$3b = 12 \Rightarrow b = 4$.

Langkah 3: Menentukan komponen vektor pergeseran $T_1$ dan $T_2$.
Dengan $a = 5$ dan $b = 4$, diperoleh:
$T_1 = \binom{5}{3}$
$T_2 = \binom{-4}{4}$.

Langkah 4: Menghitung posisi setelah pergeseran pertama ($P_1$).
$P_1 = (x_0 + 5, y_0 + 3) = (2 + 5, -5 + 3) = (7, -2)$.

Langkah 5: Menghitung posisi setelah pergeseran kedua ($P_2$).
$P_2 = (x_1 - 4, y_1 + 4) = (7 - 4, -2 + 4) = (3, 2)$.

Jadi, koordinat posisi objek setelah pergeseran kedua adalah $(3, 2)$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas9-b03-a-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: analisis translasi jajargenjang bersyarat*

Jajargenjang $ABCD$ memiliki koordinat titik-titik sudut $A(-2, 1)$, $B(4, 1)$, $C(6, 5)$, dan $D(0, 5)$. Jajargenjang tersebut ditranslasikan berturut-turut oleh $T_1 = \binom{p}{-3}$ dan $T_2 = \binom{2}{q}$ sehingga menghasilkan bayangan $A'B'C'D'$. Jika titik $A'$ terletak pada sumbu-$Y$ dan titik $C'$ terletak pada sumbu-$X$, maka koordinat bayangan titik $B'$ adalah ...

- A. $B'(6, 4)$  
  <sub>Salah: Kesalahan tanda saat menghitung nilai ordinat translasi gabungan, mengabaikan tanda minus pada pengurangan komponen vertikal.</sub>
- B. $B'(-2, 0)$  
  <sub>Salah: Tertukar konsep titik pada sumbu koordinat, yaitu menganggap titik pada sumbu-Y memiliki ordinat nol ($q - 2 = 0 \implies q = 2$) dan titik pada sumbu-X memiliki absis nol ($p + 8 = 0 \implies p = -8$).</sub>
- C. $B'(4, -2)$  
  <sub>Salah: Hanya menerapkan translasi pertama $T_1 = \binom{0}{-3}$ pada titik $B$ dan lupa menambahkan pergeseran oleh $T_2$.</sub>
- **D. $B'(6, -4)$** ✅  
  <sub>Benar: Translasi gabungan dari $T_1$ dan $T_2$ adalah $T = \binom{p + 2}{q - 3}$. Berdasarkan Sifat 3.1, bayangan titik $A(-2, 1)$ adalah $A'(-2 + p + 2, 1 + q - 3) = A'(p, q - 2)$. Karena $A'$ terletak pada sumbu-$Y$, maka absisnya bernilai nol sehingga $p = 0$. Bayangan titik $C(6, 5)$ adalah $C'(6 + p + 2, 5 + q - 3) = C'(p + 8, q + 2)$. Karena $C'$ terletak pada sumbu-$X$, maka ordinatnya bernilai nol sehingga $q + 2 = 0 \iff q = -2$. Dengan demikian, translasi gabungannya adalah $T = \binom{0 + 2}{-2 - 3} = \binom{2}{-5}$. Koordinat bayangan titik $B(4, 1)$ adalah $B'(4 + 2, 1 + (-5)) = B'(6, -4)$.</sub>

**Pembahasan:** Langkah 1: Menentukan vektor translasi gabungan $T = T_1 + T_2$.
$T = \binom{p}{-3} + \binom{2}{q} = \binom{p + 2}{q - 3}$

Langkah 2: Menentukan nilai $p$ dari syarat titik $A'$.
Bayangan titik $A(-2, 1)$ oleh $T$ adalah:
$A'(-2 + (p + 2), 1 + (q - 3)) = A'(p, q - 2)$
Karena $A'$ berada pada sumbu-$Y$, absis $x = 0$:
$p = 0$

Langkah 3: Menentukan nilai $q$ dari syarat titik $C'$.
Bayangan titik $C(6, 5)$ oleh $T$ adalah:
$C'(6 + (p + 2), 5 + (q - 3)) = C'(p + 8, q + 2)$
Karena $C'$ berada pada sumbu-$X$, ordinat $y = 0$:
$q + 2 = 0 \iff q = -2$

Langkah 4: Menentukan translasi gabungan $T$.
$T = \binom{0 + 2}{-2 - 3} = \binom{2}{-5}$

Langkah 5: Menghitung koordinat bayangan titik $B(4, 1)$.
$B'(4 + 2, 1 + (-5)) = B'(6, -4)$

Jadi, koordinat titik bayangan $B'$ adalah $B'(6, -4)$.
**Acuan:** siswa — siswa hal.160

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas9-b03-a-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: parameter translasi perpotongan garis*

Dua garis lurus pada bidang koordinat memiliki persamaan $g_1: 2x - y = 3$ dan $g_2: 4x + y = 14$. Garis $g_1$ ditranslasikan oleh $T_1 = \binom{4}{a}$ menghasilkan garis $g_1'$, sedangkan garis $g_2$ ditranslasikan oleh $T_2 = \binom{b}{-2}$ menghasilkan garis $g_2'$. Jika kedua garis bayangan $g_1'$ dan $g_2'$ berpotongan di titik $P'(5, 4)$, maka nilai dari $a + b$ adalah ...

- **A. $8$** ✅  
  <sub>Benar: Jika garis $g_1$ ditranslasikan oleh $T_1 = \binom{4}{a}$ dan melalui titik $P'(5, 4)$, maka prapeta dari $P'$ pada garis $g_1$ adalah titik $(5 - 4, 4 - a) = (1, 4 - a)$. Substitusi titik tersebut ke persamaan $g_1$: $2(1) - (4 - a) = 3 \implies -2 + a = 3 \implies a = 5$. Serupa untuk $g_2$, prapeta dari $P'$ oleh translasi $T_2 = \binom{b}{-2}$ pada $g_2$ adalah $(5 - b, 4 - (-2)) = (5 - b, 6)$. Substitusi titik tersebut ke persamaan $g_2$: $4(5 - b) + 6 = 14 \implies 20 - 4b + 6 = 14 \implies 26 - 4b = 14 \implies 4b = 12 \implies b = 3$. Dengan demikian, nilai $a + b = 5 + 3 = 8$.</sub>
- B. $12$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan linear $4(5 - b) = 8$ menjadi $5 - b = -2$, menghasilkan $b = 7$ lalu dijumlahkan dengan $a = 5$.</sub>
- C. $9$  
  <sub>Salah: Kesalahan aturan pergeseran terbalik pada garis, menggunakan $(x + 4)$ dan $(y + a)$ saat mensubstitusikan translasi sehingga menghasilkan $a = 11$ dan $b = -2$.</sub>
- D. $2$  
  <sub>Salah: Siswa menghitung nilai selisih $a - b = 5 - 3 = 2$ padahal yang ditanyakan adalah nilai $a + b$.</sub>

**Pembahasan:** Langkah 1: Menggunakan sifat bahwa jika bayangan garis melalui $P'(x', y')$, maka titik asal $(x' - h, y' - k)$ harus terletak pada garis mula-mula.
Untuk garis $g_1: 2x - y = 3$ dengan translasi $T_1 = \binom{4}{a}$, prapeta dari $P'(5, 4)$ adalah:
$(x_1, y_1) = (5 - 4, 4 - a) = (1, 4 - a)$

Langkah 2: Menentukan nilai $a$ dengan mensubstitusikan $(1, 4 - a)$ ke $g_1$.
$2(1) - (4 - a) = 3$
$2 - 4 + a = 3$
$-2 + a = 3$
$a = 5$

Langkah 3: Untuk garis $g_2: 4x + y = 14$ dengan translasi $T_2 = \binom{b}{-2}$, prapeta dari $P'(5, 4)$ adalah:
$(x_2, y_2) = (5 - b, 4 - (-2)) = (5 - b, 6)$

Langkah 4: Menentukan nilai $b$ dengan mensubstitusikan $(5 - b, 6)$ ke $g_2$.
$4(5 - b) + 6 = 14$
$20 - 4b + 6 = 14$
$26 - 4b = 14$
$4b = 12$
$b = 3$

Langkah 5: Menghitung nilai $a + b$.
$a + b = 5 + 3 = 8$

Jadi, nilai dari $a + b$ adalah $8$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas9-b03-a-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: rekonstruksi translasi berantai bersyarat garis*

Segitiga $ABC$ memiliki titik sudut $A(2, 3)$ dan $C(2, 7)$. Segitiga tersebut ditranslasikan berturut-turut oleh $T_1 = \binom{p}{-2}$ kemudian dilanjutkan oleh $T_2 = \binom{3}{q}$ sehingga menghasilkan bayangan akhir $\Delta A''B''C''$. Jika titik $A''$ terletak pada garis $y = 2x - 1$ dan titik $C''$ terletak pada garis $y = x + 4$, maka nilai dari $p + q$ adalah ...

- A. 8  
  <sub>Salah: Siswa salah dalam proses eliminasi SPLDV sehingga memperoleh nilai $p = 4$ dan $q = 4$, yang menghasilkan jumlah $8$.</sub>
- B. 4  
  <sub>Salah: Siswa melakukan kesalahan tanda saat mengurangkan dua persamaan aljabar sehingga mendapatkan $p = 4$ dan $q = 0$.</sub>
- **C. -4** ✅  
  <sub>Benar: Translasi gabungan adalah $\binom{p+3}{q-2}$. Titik $A''(p+5, q+1)$ pada garis $y = 2x - 1$ menghasilkan $q - 2p = 8$. Titik $C''(p+5, q+5)$ pada garis $y = x + 4$ menghasilkan $q - p = 4$. Melalui eliminasi diperoleh $p = -4$ dan $q = 0$, sehingga $p + q = -4$.</sub>
- D. -8  
  <sub>Salah: Siswa keliru menjumlahkan kedua persamaan alih-alih mengurangkannya sehingga nilai variabel berbalik tanda menjadi $p = -8$ dan $q = 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan translasi gabungan dari dua translasi berturut-turut.
Translasi total $T = T_1 + T_2 = \binom{p}{-2} + \binom{3}{q} = \binom{p + 3}{q - 2}$.

Langkah 2: Menentukan koordinat bayangan titik $A$ dan $C$.
- Bayangan titik $A(2, 3)$:
$$A''(2 + p + 3, 3 + q - 2) = A''(p + 5, q + 1)$$
- Bayangan titik $C(2, 7)$:
$$C''(2 + p + 3, 7 + q - 2) = C''(p + 5, q + 5)$$

Langkah 3: Menyusun persamaan dari garis yang memuat titik $A''$.
Titik $A''(p + 5, q + 1)$ terletak pada garis $y = 2x - 1$:
$$q + 1 = 2(p + 5) - 1$$
$$q + 1 = 2p + 10 - 1$$
$$q + 1 = 2p + 9$$
$$q - 2p = 8 \quad \text{...(Persamaan 1)}$$

Langkah 4: Menyusun persamaan dari garis yang memuat titik $C''$.
Titik $C''(p + 5, q + 5)$ terletak pada garis $y = x + 4$:
$$q + 5 = (p + 5) + 4$$
$$q + 5 = p + 9$$
$$q - p = 4 \quad \text{...(Persamaan 2)}$$

Langkah 5: Menyelesaikan sistem persamaan untuk mencari nilai $p$ dan $q$, lalu menentukan $p + q$.
Kurangkan Persamaan 1 dari Persamaan 2:
$$(q - p) - (q - 2p) = 4 - 8$$
$$p = -4$$
Substitusikan $p = -4$ ke Persamaan 2:
$$q - (-4) = 4$$
$$q + 4 = 4 \implies q = 0$$

Dengan demikian, nilai dari $p + q$ adalah:
$$p + q = -4 + 0 = -4$$

Jadi, nilai dari $p + q$ adalah -4.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas9-b03-a-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: analisis translasi bangun bersyarat garis*

Sebuah trapesium siku-siku $ABCD$ memiliki koordinat titik sudut $A(1, 1)$, $B(7, 1)$, $C(4, 5)$, dan $D(1, 5)$. Trapesium tersebut ditranslasikan oleh $T = \binom{m}{n}$ menghasilkan bayangan $A'B'C'D'$. Diketahui bahwa titik $A'$ terletak di kuadran IV dengan absis bernilai $9$, dan bayangan titik $D$ yaitu $D'$ terletak pada garis lurus $y = -2x + 10$. Jika koordinat titik $C'$ adalah $(x_c, y_c)$, nilai dari $x_c + y_c$ adalah ...

- A. 20  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan garis sehingga diperoleh $5 + n = 8 \implies n = 3$, menghasilkan $C'(12, 8)$ dan jumlah $12 + 8 = 20$.</sub>
- **B. 4** ✅  
  <sub>Benar: Dari absis titik $A'$ diperoleh $1 + m = 9 \implies m = 8$. Koordinat titik $D'$ adalah $(1 + 8, 5 + n) = (9, 5 + n)$. Karena $D'$ terletak pada garis $y = -2x + 10$, maka $5 + n = -2(9) + 10 \implies 5 + n = -8 \implies n = -13$. Titik $A'$ menjadi $(9, -12)$ yang tepat berada di kuadran IV. Bayangan titik $C(4, 5)$ oleh translasi $\binom{8}{-13}$ adalah $C'(4 + 8, 5 - 13) = C'(12, -8)$. Jadi nilai $x_c + y_c = 12 + (-8) = 4$.</sub>
- C. 1  
  <sub>Salah: Menjumlahkan koordinat titik $D'(9, -8)$ alih-alih mencari koordinat titik $C'$ terlebih dahulu.</sub>
- D. 14  
  <sub>Salah: Kesalahan substitusi absis pada garis menggunakan absis titik asal $D(1)$ bukan $D'(9)$ sehingga didapat $n = 3$, lalu $C'(12, 2)$ menghasilkan $14$.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Tentukan nilai $m$ dari absis bayangan titik $A(1, 1)$:
   $x_{A'} = x_A + m \implies 9 = 1 + m \implies m = 8$.
2. Tentukan koordinat titik $D'$:
   Titik $D(1, 5)$ ditranslasikan oleh $\binom{8}{n}$ menghasilkan $D'(1 + 8, 5 + n) = D'(9, 5 + n)$.
3. Tentukan nilai $n$ menggunakan persamaan garis $y = -2x + 10$:
   Substitusikan $(x, y) = (9, 5 + n)$:
   $5 + n = -2(9) + 10$
   $5 + n = -18 + 10$
   $5 + n = -8 \implies n = -13$.
4. Verifikasi letak titik $A'$:
   $A'(1 + 8, 1 - 13) = A'(9, -12)$. Karena absis positif dan ordinat negatif, titik $A'$ benar terletak di kuadran IV.
5. Tentukan koordinat titik $C'(x_c, y_c)$:
   $C(4, 5)$ ditranslasikan oleh $\binom{8}{-13}$:
   $C'(4 + 8, 5 + (-13)) = C'(12, -8)$.
   Maka $x_c = 12$ dan $y_c = -8$.
6. Hitung nilai $x_c + y_c$:
   $x_c + y_c = 12 + (-8) = 4$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas9-b03-a-hard-bt01-015
*orisinal | C5 | 6 langkah | jenis: analisis translasi bertingkat segitiga siku-siku*

Segitiga siku-siku $PQR$ siku-siku di $P$ memiliki koordinat titik $P(-2, 1)$ dan $Q(4, 1)$. Titik sudut $R$ terletak di atas ruas garis $PQ$ dengan panjang sisi $PR = 8$ satuan. Segitiga tersebut ditranslasikan berturut-turut oleh translasi $T_1 = \binom{a}{-3}$ kemudian dilanjutkan oleh $T_2 = \binom{5}{b}$ sehingga menghasilkan bayangan akhir segitiga $P''Q''R''$. Jika titik $P''$ terletak tepat pada sumbu-$Y$ dan titik $R''$ terletak tepat pada sumbu-$X$, maka nilai dari absis dikurangi ordinat titik $Q''$ ($x_{Q''} - y_{Q''}$) adalah ...

- A. -2  
  <sub>Salah: Menghitung penjumlahan koordinat $x_{Q''} + y_{Q''} = 6 + (-8) = -2$ alih-alih selisihnya.</sub>
- **B. 14** ✅  
  <sub>Benar: Koordinat titik $R$ adalah $(-2, 1 + 8) = (-2, 9)$. Translasi total adalah $T = T_1 + T_2 = \binom{a + 5}{b - 3}$. Titik $P''$ berada pada sumbu-$Y$ sehingga absisnya nol: $-2 + a + 5 = 0 \implies a = -3$. Titik $R''$ berada pada sumbu-$X$ sehingga ordinatnya nol: $9 + b - 3 = 0 \implies b = -6$. Translasi total menjadi $\binom{2}{-9}$. Bayangan titik $Q(4, 1)$ adalah $Q''(4 + 2, 1 - 9) = Q''(6, -8)$. Maka $x_{Q''} - y_{Q''} = 6 - (-8) = 14$.</sub>
- C. -14  
  <sub>Salah: Terbalik dalam mengurangkan nilai, yaitu menghitung ordinat dikurangi absis: $-8 - 6 = -14$.</sub>
- D. 6  
  <sub>Salah: Tertukar menerapkan sifat sumbu koordinat (menganggap sumbu-$Y$ bernilai ordinat nol dan sumbu-$X$ bernilai absis nol).</sub>

**Pembahasan:** Langkah penyelesaian:
1. Menentukan koordinat titik $R$:
   Karena segitiga siku-siku di $P(-2, 1)$ dan ruas garis $PQ$ terletak pada garis horizontal $y = 1$, maka sisi $PR$ tegak lurus terhadap $PQ$ (garis vertikal $x = -2$).
   Karena titik $R$ berada di atas $PQ$ dengan panjang $PR = 8$ satuan, maka ordinat $R$ adalah $1 + 8 = 9$.
   Jadi, $R(-2, 9)$.
2. Menentukan translasi komposisi $T$:
   $T = T_1 + T_2 = \binom{a + 5}{-3 + b} = \binom{a + 5}{b - 3}$.
3. Menentukan nilai $a$ dari letak titik $P''$:
   Titik $P''(-2 + a + 5, 1 + b - 3) = P''(a + 3, b - 2)$.
   Karena $P''$ berada pada sumbu-$Y$, maka absisnya bernilai $0$:
   $a + 3 = 0 \implies a = -3$.
4. Menentukan nilai $b$ dari letak titik $R''$:
   Titik $R''(-2 + a + 5, 9 + b - 3) = R''(a + 3, b + 6)$.
   Karena $R''$ berada pada sumbu-$X$, maka ordinatnya bernilai $0$:
   $b + 6 = 0 \implies b = -6$.
5. Menentukan translasi total:
   $T = \binom{-3 + 5}{-6 - 3} = \binom{2}{-9}$.
6. Menentukan koordinat bayangan $Q''$:
   Titik awal $Q(4, 1)$ ditranslasikan oleh $\binom{2}{-9}$:
   $Q''(4 + 2, 1 - 9) = Q''(6, -8)$.
   Maka $x_{Q''} = 6$ dan $y_{Q''} = -8$.
7. Menghitung nilai yang diminta:
   $x_{Q''} - y_{Q''} = 6 - (-8) = 6 + 8 = 14$.
**Acuan:** siswa — siswa hal.159

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
