# Lembar koreksi — kelas12_tl SMA12L-B2 subbab A: Definisi Turunan Fungsi

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b02-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: limit fungsi aljabar*

Gunakan sifat-sifat limit fungsi untuk menentukan nilai dari $\lim_{x\to 5}(x^2 - 6)$.

- **A. $19$** ✅  
  <sub>Benar: Substitusikan $x = 5$ ke dalam fungsi: $5^2 - 6 = 25 - 6 = 19$.</sub>
- B. $31$  
  <sub>Salah: Siswa menjumlahkan konstanta alih-alih mengurangkannya: $25 + 6 = 31$.</sub>
- C. $21$  
  <sub>Salah: Siswa salah menerapkan tanda operasi menjadi penjumlahan: $25 - 6$ dihitung sebagai $25 - 4$ atau salah hitung aritmetika dasar.</sub>
- D. $4$  
  <sub>Salah: Siswa salah mengalikan koefisien dan konstanta alih-alih memangkatkan: $5 \times 2 - 6 = 10 - 6 = 4$.</sub>

**Pembahasan:** Berdasarkan sifat-sifat limit fungsi polinomial:
$$\lim_{x\to 5}(x^2 - 6) = (\lim_{x\to 5} x)^2 - \lim_{x\to 5} 6 = 5^2 - 6 = 25 - 6 = 19$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b02-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi turunan fungsi kuadrat*

Diketahui fungsi $f(x) = \frac{1}{3}x^2$. Nilai dari $f'(6)$ adalah ....

- **A. $4$** ✅  
  <sub>Benar: Turunan pertama fungsi adalah $f'(x) = 2 \cdot \frac{1}{3}x = \frac{2}{3}x$. Nilai $f'(6) = \frac{2}{3}(6) = 4$.</sub>
- B. $6$  
  <sub>Salah: Siswa hanya mengambil nilai $x$ yang diminta tanpa memproses fungsi turunan secara benar.</sub>
- C. $12$  
  <sub>Salah: Siswa menyubstitusikan nilai ke fungsi awal $f(6) = \frac{1}{3}(36) = 12$ tanpa melakukan turunan.</sub>
- D. $2$  
  <sub>Salah: Siswa lupa mengalikan dengan eksponen saat menurunkan, sehingga menghitung $\frac{1}{3}(6) = 2$.</sub>

**Pembahasan:** Turunan pertama dari $f(x) = \frac{1}{3}x^2$ diperoleh dengan aturan pangkat:
$$f'(x) = 2 \cdot \frac{1}{3}x^{2-1} = \frac{2}{3}x$$
Substitusikan $x = 6$:
$$f'(6) = \frac{2}{3}(6) = 4$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b02-a-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: limit fungsi polinomial di nol*

Tentukan nilai dari $\lim_{x\to 0}(3x^2 - 7x + 9)$ dengan menerapkan sifat-sifat limit fungsi.

- A. $-7$  
  <sub>Salah: Siswa keliru mengambil koefisien suku linear $x$.</sub>
- **B. $9$** ✅  
  <sub>Benar: Substitusi langsung $x = 0$ menghasilkan $3(0)^2 - 7(0) + 9 = 9$.</sub>
- C. $5$  
  <sub>Salah: Siswa menjumlahkan seluruh koefisien fungsi: $3 - 7 + 9 = 5$.</sub>
- D. $0$  
  <sub>Salah: Siswa menganggap limit mendekati 0 selalu menghasilkan nilai 0.</sub>

**Pembahasan:** Menerapkan sifat-sifat dasar limit fungsi:
$$\lim_{x\to 0}(3x^2 - 7x + 9) = 3(\lim_{x\to 0}x)^2 - 7(\lim_{x\to 0}x) + \lim_{x\to 0}9 = 3(0) - 7(0) + 9 = 9$$
**Acuan:** siswa — siswa hal.103 Contoh Soal 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b02-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: syarat kekontinuan fungsi*

Berdasarkan definisi kekontinuan fungsi, suatu fungsi $f(x)$ dikatakan kontinu di titik $x = c$ jika memenuhi tiga syarat. Manakah di antara pernyataan berikut yang merupakan salah satu syarat tersebut?

- A. $\lim_{x\to c} f(x) = c$  
  <sub>Salah: Siswa keliru mengira nilai limit harus sama dengan nilai absis pendekatan $c$.</sub>
- **B. $\lim_{x\to c} f(x) = f(c)$** ✅  
  <sub>Benar: Syarat ketiga pada definisi kekontinuan menyatakan bahwa nilai limit fungsi di titik $c$ harus sama dengan nilai fungsinya di titik tersebut.</sub>
- C. $f'(c) = 0$  
  <sub>Salah: Siswa tertukar dengan syarat titik stasioner pada turunan fungsi.</sub>
- D. $\lim_{x\to c} f(x) = 0$  
  <sub>Salah: Siswa mengira limit pada titik kontinu harus bernilai nol.</sub>

**Pembahasan:** Menurut Definisi 2.2 Buku Siswa, fungsi $f(x)$ kontinu di $x = c$ jika:
1. $f(c)$ terdefinisi (ada),
2. $\lim_{x\to c} f(x)$ ada, dan
3. $\lim_{x\to c} f(x) = f(c)$.
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b02-a-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: gradien garis sekan*

Suatu garis sekan menghubungkan titik $P(1, 2)$ dan $R(4, 11)$ pada kurva $f(x)$. Kemiringan (gradien) garis sekan $PR$ tersebut adalah ....

- A. $\frac{13}{5}$  
  <sub>Salah: Siswa menjumlahkan koordinat alih-alih mengurangkannya: $\frac{11+2}{4+1} = \frac{13}{5}$.</sub>
- B. $9$  
  <sub>Salah: Siswa hanya menghitung selisih ordinat $\Delta y = 11 - 2 = 9$ tanpa membaginya dengan $\Delta x$.</sub>
- C. $\frac{1}{3}$  
  <sub>Salah: Siswa membalik rumus gradien menjadi perubahan absis dibagi perubahan ordinat: $\frac{\Delta x}{\Delta y} = \frac{3}{9} = \frac{1}{3}$.</sub>
- **D. $3$** ✅  
  <sub>Benar: Kemiringan garis sekan dihitung dengan gradien dua titik: $m = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$.</sub>

**Pembahasan:** Berdasarkan Definisi 2.3, kemiringan garis sekan yang melalui titik $P(x_1, y_1)$ dan $R(x_2, y_2)$ adalah:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{11 - 2}{4 - 1} = \frac{9}{3} = 3$$
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b02-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi turunan fungsi berpangkat negatif*

Diketahui fungsi $f(x) = -4x^2$. Nilai dari $f'(-3)$ adalah ....

- **A. $24$** ✅  
  <sub>Benar: Turunan pertama fungsi $f(x) = -4x^2$ adalah $f'(x) = -8x$. Nilai $f'(-3) = -8(-3) = 24$.</sub>
- B. $-24$  
  <sub>Salah: Siswa salah mengalikan dua bilangan bertanda negatif sehingga menghasilkan nilai negatif.</sub>
- C. $12$  
  <sub>Salah: Siswa salah menurunkan fungsi menjadi $f'(x) = -4x$, lalu menghitung $-4(-3) = 12$.</sub>
- D. $-36$  
  <sub>Salah: Siswa menyubstitusikan nilai $-3$ ke fungsi asal $f(x)$, bukan ke turunan pertamanya.</sub>

**Pembahasan:** Turunan pertama dari $f(x) = -4x^2$ diperoleh dengan aturan pangkat:
$$f'(x) = 2 \cdot (-4)x^{2-1} = -8x$$
Substitusikan $x = -3$:
$$f'(-3) = -8(-3) = 24$$
Jadi, nilai dari $f'(-3)$ adalah $24$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b02-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: limit fungsi bentuk akar*

Gunakan sifat-sifat limit untuk menentukan nilai dari $\displaystyle\lim_{y\to 1}\sqrt{\dfrac{y^2+3}{5y+11}}$.

- A. $1$  
  <sub>Salah: Siswa salah menjumlahkan pembilang dan penyebut sehingga memperoleh nilai pecahan senilai 1.</sub>
- B. $\dfrac{1}{8}$  
  <sub>Salah: Siswa membagi $\frac{1}{4}$ dengan 2 alih-alih menarik nilai akar kuadratnya.</sub>
- C. $\dfrac{1}{4}$  
  <sub>Salah: Siswa menghitung nilai di dalam akar $\frac{4}{16} = \frac{1}{4}$, tetapi lupa menarik akar kuadratnya.</sub>
- **D. $\dfrac{1}{2}$** ✅  
  <sub>Benar: Substitusi $y=1$ menghasilkan $\sqrt{\frac{1^2+3}{5(1)+11}} = \sqrt{\frac{4}{16}} = \sqrt{\frac{1}{4}} = \frac{1}{2}$.</sub>

**Pembahasan:** Berdasarkan sifat limit akar dan limit rasional:
$$\lim_{y\to 1}\sqrt{\dfrac{y^2+3}{5y+11}} = \sqrt{\lim_{y\to 1}\dfrac{y^2+3}{5y+11}}$$
Substitusikan $y = 1$:
$$\sqrt{\dfrac{1^2+3}{5(1)+11}} = \sqrt{\dfrac{4}{16}} = \sqrt{\dfrac{1}{4}} = \dfrac{1}{2}$$
Jadi, nilai limit tersebut adalah $\dfrac{1}{2}$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b02-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: perkalian limit fungsi aljabar*

Diketahui $\displaystyle\lim_{x\to 4} g(x) = 6$. Nilai dari $\displaystyle\lim_{x\to 4} \left(g(x) \cdot \dfrac{5}{\sqrt{x} + 3}\right)$ adalah ....

- A. $3$  
  <sub>Salah: Siswa salah mengevaluasi penyebut menjadi $4+3=7$ lalu melakukan pembulatan yang keliru.</sub>
- B. $30$  
  <sub>Salah: Siswa mengalikan nilai 6 dengan 5 di pembilang, namun lupa membaginya dengan penyebut $(\sqrt{4}+3) = 5$.</sub>
- C. $5$  
  <sub>Salah: Siswa hanya menghitung nilai pecahan $\frac{5}{\sqrt{4}+3} = 1$ lalu mengalikannya dengan 5, melupakan nilai $\lim g(x) = 6$.</sub>
- **D. $6$** ✅  
  <sub>Benar: Limit perkalian sama dengan hasil kali limit: $6 \cdot \frac{5}{\sqrt{4}+3} = 6 \cdot \frac{5}{2+3} = 6 \cdot 1 = 6$.</sub>

**Pembahasan:** Gunakan sifat perkalian limit fungsi:
$$\lim_{x\to 4}\left(g(x) \cdot \dfrac{5}{\sqrt{x}+3}\right) = \left(\lim_{x\to 4} g(x)\right) \cdot \left(\lim_{x\to 4}\dfrac{5}{\sqrt{x}+3}\right)$$
Substitusikan nilai limit yang diketahui:
$$= 6 \cdot \dfrac{5}{\sqrt{4}+3} = 6 \cdot \dfrac{5}{2+3} = 6 \cdot \dfrac{5}{5} = 6 \cdot 1 = 6$$
Jadi, nilai limit tersebut adalah $6$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b02-a-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: limit fungsi konstan*

Berdasarkan Sifat Limit 1 untuk fungsi konstan, jika $f(x) = 15$ untuk setiap bilangan real $x$, maka nilai dari $\displaystyle\lim_{x\to 8} f(x)$ adalah ....

- **A. $15$** ✅  
  <sub>Benar: Limit dari suatu fungsi konstan $f(x) = k$ untuk $x$ mendekati nilai $c$ berapapun selalu sama dengan konstanta $k$ itu sendiri, yaitu 15.</sub>
- B. $120$  
  <sub>Salah: Siswa mengalikan nilai konstanta 15 dengan nilai pendekatan $x = 8$.</sub>
- C. $0$  
  <sub>Salah: Siswa mengira limit fungsi konstan selalu bernilai nol seperti aturan turunan fungsi konstan.</sub>
- D. $8$  
  <sub>Salah: Siswa tertukar antara nilai pendekatan $x \to c$ dengan nilai limit fungsi konstanta.</sub>

**Pembahasan:** Berdasarkan Sifat Limit 1:
Untuk fungsi konstan $f(x) = k$, berlaku:
$$\lim_{x\to c} f(x) = \lim_{x\to c} k = k$$
Karena $f(x) = 15$ dan $c = 8$, maka:
$$\lim_{x\to 8} f(x) = \lim_{x\to 8} 15 = 15$$
Jadi, nilai limit tersebut adalah $15$.
**Acuan:** siswa — siswa hal.101

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b02-a-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: definisi kontinuitas pada interval*

Berdasarkan Definisi 2.2 mengenai kontinuitas fungsi, suatu fungsi $f(x)$ dikatakan kontinu pada suatu interval $I$ jika ....

- A. fungsi tersebut memiliki nilai limit yang sama dengan nol di interval $I$  
  <sub>Salah: Siswa salah memahami syarat kontinuitas dengan mengaitkannya pada nilai limit bernilai nol.</sub>
- B. fungsi tersebut hanya terdefinisi pada kedua ujung interval $I$  
  <sub>Salah: Siswa mengabaikan titik-titik di bagian dalam interval dan hanya memperhatikan ujung batas.</sub>
- **C. fungsi tersebut kontinu pada setiap titik di $I$** ✅  
  <sub>Benar: Definisi 2.2 menyatakan bahwa suatu fungsi kontinu pada suatu interval I jika fungsi tersebut kontinu pada setiap titik di I.</sub>
- D. grafik fungsinya memotong sumbu-$X$ di sekurang-kurangnya satu titik pada $I$  
  <sub>Salah: Siswa mengacaukan konsep kontinuitas dengan teorema nilai antara atau perpotongan sumbu grafik.</sub>

**Pembahasan:** Berdasarkan Definisi 2.2 pada Buku Siswa halaman 112:
"Suatu fungsi kontinu pada suatu interval $I$ jika fungsi tersebut kontinu pada setiap titik di $I$."
Jadi, pernyataan yang tepat adalah fungsi tersebut kontinu pada setiap titik di $I$.
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b02-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: limit fungsi kuadrat sederhana*

Gunakan sifat-sifat limit untuk menyelesaikan masalah berikut. Tentukan nilai dari $\displaystyle\lim_{x\to 4} (2x^2 - 7)$.

- A. $39$  
  <sub>Salah: Siswa salah tanda operasi pengurangan menjadi penjumlahan sehingga menghitung $32 + 7 = 39$.</sub>
- B. $9$  
  <sub>Salah: Siswa tidak mengkuadratkan $x$, melainkan menghitung $2(4) - 7 = 8 - 7 = 1$ lalu ditambah 8, atau menghitung $2(4^2) = 16$ sehingga $16 - 7 = 9$.</sub>
- **C. $25$** ✅  
  <sub>Benar: Substitusi langsung $x = 4$ menghasilkan $2(4)^2 - 7 = 2(16) - 7 = 32 - 7 = 25$.</sub>
- D. $57$  
  <sub>Salah: Siswa menghitung $(2 \times 4)^2 - 7 = 8^2 - 7 = 64 - 7 = 57$.</sub>

**Pembahasan:** Berdasarkan sifat-sifat limit fungsi polinomial, limit dapat dihitung dengan substitusi langsung:
$$\lim_{x\to 4} (2x^2 - 7) = 2(4)^2 - 7 = 2(16) - 7 = 32 - 7 = 25.$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b02-a-easy-bt01-012
*variasi (angka) | C1 | 1 langkah | jenis: evaluasi limit fungsi aljabar di titik nol*

Tentukan nilai dari $\displaystyle\lim_{x\to 0} (5x^2 - 4x + 8)$ dengan menerapkan sifat-sifat limit fungsi.

- A. $-8$  
  <sub>Salah: Siswa salah memperlakukan tanda suku konstanta.</sub>
- B. $9$  
  <sub>Salah: Siswa menjumlahkan koefisien $5 - 4 + 8 = 9$ tanpa mengalikan dengan $x = 0$.</sub>
- **C. $8$** ✅  
  <sub>Benar: Substitusi $x = 0$ menghasilkan $5(0)^2 - 4(0) + 8 = 8$.</sub>
- D. $0$  
  <sub>Salah: Siswa menganggap limit menuju nol selalu bernilai nol.</sub>

**Pembahasan:** Menerapkan sifat limit penjumlahan dan perkalian skalar:
$$\lim_{x\to 0}(5x^2 - 4x + 8) = 5(0)^2 - 4(0) + 8 = 8.$$
**Acuan:** siswa — siswa hal.103 Contoh Soal 2.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b02-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: limit fungsi identitas*

Berdasarkan Sifat Limit 1 untuk fungsi identitas $g(x) = x$, nilai dari $\displaystyle\lim_{x\to -7} x$ adalah ....

- A. $7$  
  <sub>Salah: Siswa mengabaikan tanda negatif pada nilai $c$.</sub>
- **B. $-7$** ✅  
  <sub>Benar: Menurut sifat limit fungsi identitas $\lim_{x\to c} x = c$, maka untuk $c = -7$ nilai limitnya adalah $-7$.</sub>
- C. $1$  
  <sub>Salah: Siswa menjawab koefisien dari $x$.</sub>
- D. $0$  
  <sub>Salah: Siswa mengira limit fungsi aljabar selalu menuju ke nol.</sub>

**Pembahasan:** Berdasarkan Sifat Limit 1 pada buku, untuk fungsi identitas $g(x) = x$ berlaku:
$$\lim_{x\to c} x = c$$
Dengan demikian:
$$\lim_{x\to -7} x = -7.$$
**Acuan:** siswa — siswa hal.101

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b02-a-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: kemiringan garis sekan dua titik*

Sebuah garis sekan memotong kurva $f(x)$ di dua titik, yaitu $A(2, 3)$ dan $B(6, 23)$. Kemiringan garis sekan yang melalui kedua titik tersebut adalah ....

- A. $\dfrac{1}{5}$  
  <sub>Salah: Siswa membalik rumus gradien menjadi $\dfrac{x_2 - x_1}{y_2 - y_1} = \dfrac{4}{20} = \dfrac{1}{5}$.</sub>
- B. $4$  
  <sub>Salah: Siswa menghitung selisih absis $6 - 2 = 4$ dan menganggapnya sebagai kemiringan.</sub>
- C. $10$  
  <sub>Salah: Siswa salah membagi selisih ordinat $20$ dengan $2$ bukan dengan $4$.</sub>
- **D. $5$** ✅  
  <sub>Benar: Kemiringan garis sekan adalah $m = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{23 - 3}{6 - 2} = \dfrac{20}{4} = 5$.</sub>

**Pembahasan:** Sesuai Definisi 2.3 garis sekan, kemiringan garis sekan yang melalui titik $A(x_1, y_1)$ dan $B(x_2, y_2)$ adalah:
$$m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{23 - 3}{6 - 2} = \frac{20}{4} = 5.$$
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b02-a-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: limit fungsi bentuk akar pecahan*

Gunakan sifat-sifat limit untuk menentukan nilai dari $\displaystyle\lim_{y\to 5}\sqrt{\dfrac{y-1}{6y+6}}$.

- A. $\dfrac{1}{6}$  
  <sub>Salah: Salah menghitung nilai penyebut $6(5)+6=36$ lalu menganggap akarnya langsung menjadi penyebut tanpa pembilang.</sub>
- **B. $\dfrac{1}{3}$** ✅  
  <sub>Benar: Substitusi $y = 5$: $\sqrt{\dfrac{5-1}{6(5)+6}} = \sqrt{\dfrac{4}{36}} = \sqrt{\dfrac{1}{9}} = \dfrac{1}{3}$.</sub>
- C. $\dfrac{2}{9}$  
  <sub>Salah: Hanya menarik akar dari pembilang $\sqrt{4}=2$, penyebut tetap $36$ lalu disederhanakan menjadi $\frac{2}{36}$ yang salah hitung.</sub>
- D. $\dfrac{1}{9}$  
  <sub>Salah: Lupa menarik akar kuadrat dari hasil pecahan $\frac{1}{9}$.</sub>

**Pembahasan:** Berdasarkan sifat limit fungsi aljabar dan akar:
$$\lim_{y\to 5}\sqrt{\dfrac{y-1}{6y+6}} = \sqrt{\dfrac{\lim_{y\to 5}(y-1)}{\lim_{y\to 5}(6y+6)}} = \sqrt{\dfrac{5-1}{6(5)+6}} = \sqrt{\dfrac{4}{36}} = \sqrt{\dfrac{1}{9}} = \dfrac{1}{3}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b02-a-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: perkalian limit fungsi dan pecahan*

Diketahui $\displaystyle\lim_{x\to 5} g(x) = 8$. Tentukan nilai dari $\displaystyle\lim_{x\to 5}\left(g(x)\cdot\dfrac{7}{x+9}\right)$.

- A. $\dfrac{1}{2}$  
  <sub>Salah: Lupa mengalikan dengan nilai limit $g(x) = 8$.</sub>
- B. $2$  
  <sub>Salah: Hanya menghitung nilai pecahan $\frac{7}{5+9} = \frac{1}{2}$ lalu membagi limit fungsi dengan nilai tersebut secara keliru.</sub>
- **C. $4$** ✅  
  <sub>Benar: Sifat perkalian limit: $\lim_{x\to 5} g(x) \cdot \frac{7}{5+9} = 8 \cdot \frac{7}{14} = 8 \cdot \frac{1}{2} = 4$.</sub>
- D. $8$  
  <sub>Salah: Hanya menuliskan nilai dari limit $g(x)$ tanpa memperhitungkan faktor pecahan.</sub>

**Pembahasan:** Dengan menggunakan sifat limit perkalian dua fungsi:
$$\lim_{x\to 5}\left(g(x)\cdot\dfrac{7}{x+9}\right) = \left(\lim_{x\to 5} g(x)\right) \cdot \left(\lim_{x\to 5}\dfrac{7}{x+9}\right) = 8 \cdot \dfrac{7}{5+9} = 8 \cdot \dfrac{7}{14} = 8 \cdot \dfrac{1}{2} = 4$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b02-a-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: turunan fungsi kuadrat koefisien negatif*

Tentukan nilai dari $f'(-1)$ untuk fungsi $f(x) = -5x^2$.

- A. $-5$  
  <sub>Salah: Hanya memasukkan $x = -1$ ke turunan tanpa mengalikan eksponen 2 ke koefisien.</sub>
- B. $-10$  
  <sub>Salah: Kesalahan tanda negatif saat mengalikan $-10$ dengan $-1$.</sub>
- **C. $10$** ✅  
  <sub>Benar: Turunan dari $f(x) = -5x^2$ adalah $f'(x) = -10x$, sehingga $f'(-1) = -10(-1) = 10$.</sub>
- D. $5$  
  <sub>Salah: Hanya mengambil koefisien tanpa turunan yang benar.</sub>

**Pembahasan:** Turunan pertama dari $f(x) = ax^2$ adalah $f'(x) = 2ax$.
Untuk $f(x) = -5x^2$, diperoleh:
$$f'(x) = 2(-5)x = -10x$$
Substitusikan $x = -1$:
$$f'(-1) = -10(-1) = 10$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b02-a-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: tokoh sejarah kalkulus*

Matematikawan terkemuka yang meletakkan fondasi aritmetis dan limit yang kokoh pada kalkulus sehingga sering disebut sebagai Bapak Analisis Modern adalah ....

- A. Gottfried Wilhelm Leibniz  
  <sub>Salah: Penemu notasi kalkulus tetapi bukan tokoh yang mendefinisikan ulang kalkulus secara aritmetis formal.</sub>
- B. René Descartes  
  <sub>Salah: Bapak Geometri Analitis, bukan Bapak Analisis Modern.</sub>
- C. Isaac Newton  
  <sub>Salah: Salah satu penemu awal kalkulus namun bukan tokoh yang dijuluki Bapak Analisis Modern.</sub>
- **D. Karl Theodor Wilhelm Weierstrass** ✅  
  <sub>Benar: Berdasarkan materi Buku Siswa halaman 97, Karl Theodor Wilhelm Weierstrass sering disebut sebagai Bapak Analisis Modern.</sub>

**Pembahasan:** Pada materi Buku Siswa halaman 97 disebutkan bahwa Karl Theodor Wilhelm Weierstrass (1815–1897) merupakan salah satu pendiri teori fungsi modern dan sering disebut sebagai Bapak Analisis Modern berkat kontribusinya meletakkan dasar aritmetis yang ketat pada konsep limit dan turunan.
**Acuan:** siswa — siswa hal.97

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b02-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: interpretasi definisi limit fungsi*

Berdasarkan Definisi 2.1 mengenai limit fungsi secara intuitif, pernyataan $\displaystyle\lim_{x\to c} f(x) = L$ memiliki arti bahwa ....

- **A. untuk $x$ mendekati $c$ dari kiri dan kanan, maka $f(x)$ mendekati $L$** ✅  
  <sub>Benar: Sesuai Definisi 2.1 pada buku, notasi $\lim_{x\to c} f(x) = L$ berarti untuk $x$ mendekati $c$ dari kiri dan kanan, nilai $f(x)$ mendekati $L$.</sub>
- B. nilai $x$ sama dengan $c$ mengakibatkan $f(x)$ bernilai nol  
  <sub>Salah: Salah menganggap limit selalu menghasilkan nilai nol.</sub>
- C. nilai fungsi $f(c)$ harus selalu sama persis dengan $L$  
  <sub>Salah: Keliru menyamakan konsep limit dengan nilai fungsi di titik $c$ ($f(c)$ tidak harus terdefinisi untuk memiliki limit).</sub>
- D. untuk $x$ menjauhi $c$, nilai $f(x)$ akan menuju tak hingga  
  <sub>Salah: Konsep terbalik dari definisi pendekatan limit.</sub>

**Pembahasan:** Berdasarkan Definisi 2.1 di Buku Siswa halaman 100, notasi $\lim_{x\to c} f(x) = L$ berarti bahwa ketika $x$ mendekati $c$ dari arah kiri maupun arah kanan, maka nilai fungsi $f(x)$ mendekati $L$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b02-a-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi nilai turunan fungsi kuadrat pecahan*

Tentukan nilai dari $f'(-6)$ dan $f'(8)$ untuk fungsi $f(x) = \dfrac{3}{4}x^2$.

- A. $f'(-6) = -18$ dan $f'(8) = 24$  
  <sub>Salah: Siswa mengalikan koefisien dengan 2 tetapi lupa membaginya dengan penyebut sehingga memakai $f'(x) = 3x$.</sub>
- **B. $f'(-6) = -9$ dan $f'(8) = 12$** ✅  
  <sub>Benar: Turunan pertama fungsi adalah $f'(x) = 2 \cdot \frac{3}{4}x = \frac{3}{2}x$. Untuk $x = -6$, diperoleh $f'(-6) = \frac{3}{2}(-6) = -9$. Untuk $x = 8$, diperoleh $f'(8) = \frac{3}{2}(8) = 12$.</sub>
- C. $f'(-6) = 9$ dan $f'(8) = -12$  
  <sub>Salah: Siswa melakukan kesalahan tanda negatif pada hasil evaluasi kedua titik.</sub>
- D. $f'(-6) = -\dfrac{9}{2}$ dan $f'(8) = 6$  
  <sub>Salah: Siswa lupa mengalikan dengan pangkat 2 saat menurunkan fungsi sehingga menggunakan rumus $f'(x) = \frac{3}{4}x$.</sub>

**Pembahasan:** Langkah 1: Menentukan turunan pertama dari fungsi $f(x) = \frac{3}{4}x^2$.
$$f'(x) = \frac{d}{dx}\left(\frac{3}{4}x^2\right) = 2 \cdot \frac{3}{4}x = \frac{3}{2}x$$

Langkah 2: Menghitung nilai $f'(-6)$ dan $f'(8)$ dengan substitusi nilai $x$.
- Untuk $x = -6$:
$$f'(-6) = \frac{3}{2}(-6) = -9$$
- Untuk $x = 8$:
$$f'(8) = \frac{3}{2}(8) = 12$$

Jadi, nilai dari $f'(-6) = -9$ dan $f'(8) = 12$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b02-a-medium-bt01-001
*variasi (konteks) | C3 | 3 langkah | jenis: parameter kontinuitas fungsi*

Diberikan fungsi $f(x) = \begin{cases} 2x + a, & x \le 3 \\ x^2 - 5, & x > 3 \end{cases}$. Agar fungsi $f(x)$ kontinu pada seluruh bilangan real $\mathbb{R}$, nilai $a$ harus sama dengan ....

- A. $2$  
  <sub>Salah: Salah transposisi tanda saat menyelesaikan persamaan, menghitung $a = 6 - 4$.</sub>
- B. $-10$  
  <sub>Salah: Salah tanda pada nilai ruas kanan menjadi $-4 - 6$.</sub>
- C. $10$  
  <sub>Salah: Menjumlahkan kedua ruas $6 + 4$ alih-alih mengurangkannya.</sub>
- **D. $-2$** ✅  
  <sub>Benar: Syarat kontinu di $x = 3$ mengharuskan $\lim_{x\to 3^-} f(x) = \lim_{x\to 3^+} f(x)$, yaitu $2(3) + a = 3^2 - 5 \iff 6 + a = 4 \iff a = -2$.</sub>

**Pembahasan:** Fungsi $f(x)$ terdiri atas fungsi polinomial yang kontinu di setiap interval kecuali kemungkinan di titik batas $x = 3$. Agar kontinu di $x = 3$, limit kiri harus sama dengan limit kanan:
$$\lim_{x\to 3^-} (2x + a) = \lim_{x\to 3^+} (x^2 - 5)$$
$$2(3) + a = 3^2 - 5$$
$$6 + a = 4$$
$$a = 4 - 6 = -2.$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b02-a-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: kemiringan garis sekan*

Garis sekan memotong kurva $f(x) = x^2 + 3x$ di titik $P(1, f(1))$ dan titik $R(1 + \Delta x, f(1 + \Delta x))$ dengan $\Delta x = 2$. Kemiringan garis sekan $PR$ tersebut adalah ....

- A. $9$  
  <sub>Salah: Salah membagi ordinat akhir dengan selisih absis, yaitu $\frac{18}{2} = 9$ tanpa mengurangkan $f(1)$.</sub>
- B. $5$  
  <sub>Salah: Menghitung nilai turunan fungsi di titik $x = 1$ ($f'(1) = 2(1) + 3 = 5$) bukan garis sekan.</sub>
- C. $14$  
  <sub>Salah: Hanya menghitung selisih ordinat $f(3) - f(1)$ tanpa membaginya dengan $\Delta x$.</sub>
- **D. $7$** ✅  
  <sub>Benar: Koordinat titik adalah $P(1, 4)$ dan $R(3, 18)$. Kemiringan $m = \frac{18 - 4}{3 - 1} = \frac{14}{2} = 7$.</sub>

**Pembahasan:** 1. Tentukan nilai $f(1)$:
$$f(1) = 1^2 + 3(1) = 4$$
2. Karena $\Delta x = 2$, titik absis kedua adalah $x_2 = 1 + 2 = 3$:
$$f(3) = 3^2 + 3(3) = 9 + 9 = 18$$
3. Hitung kemiringan garis sekan:
$$m = \dfrac{f(1 + \Delta x) - f(1)}{\Delta x} = \dfrac{18 - 4}{2} = \dfrac{14}{2} = 7.$$
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b02-a-medium-bt01-003
*orisinal | C3 | 2 langkah | jenis: limit fungsi trigonometri*

Nilai dari $\displaystyle\lim_{x\to 0}\dfrac{6x + \sin 4x}{5x - \tan 2x}$ adalah ....

- A. $2$  
  <sub>Salah: Hanya membagi suku pertama $\frac{6x}{5x - 2x}$ atau kesalahan aritmetika membagi koefisien.</sub>
- **B. $\dfrac{10}{3}$** ✅  
  <sub>Benar: Membagi pembilang dan penyebut dengan $x$ menghasilkan $\frac{6 + 4}{5 - 2} = \frac{10}{3}$.</sub>
- C. $\dfrac{2}{3}$  
  <sub>Salah: Hanya menghitung perbandingan limit fungsi trigonometri tanpa melibatkan suku linier aljabar.</sub>
- D. $\dfrac{10}{7}$  
  <sub>Salah: Salah tanda operasi pada penyebut sehingga menghitung $5 + 2 = 7$.</sub>

**Pembahasan:** Bagi pembilang dan penyebut dengan $x$:
$$\lim_{x\to 0}\dfrac{6x + \sin 4x}{5x - \tan 2x} = \lim_{x\to 0}\dfrac{\frac{6x}{x} + \frac{\sin 4x}{x}}{\frac{5x}{x} - \frac{\tan 2x}{x}}$$
$$= \dfrac{6 + \lim_{x\to 0}\frac{\sin 4x}{x}}{5 - \lim_{x\to 0}\frac{\tan 2x}{x}} = \dfrac{6 + 4}{5 - 2} = \dfrac{10}{3}.$$
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b02-a-medium-bt01-004
*orisinal | C3 | 2 langkah | jenis: kontinuitas fungsi aljabar*

Diketahui fungsi $f(x) = \begin{cases} \dfrac{x^2 - 16}{x - 4}, & x \neq 4 \\ c, & x = 4 \end{cases}$. Agar fungsi $f(x)$ kontinu di titik $x = 4$, nilai $c$ yang memenuhi adalah ....

- A. $4$  
  <sub>Salah: Mengira nilai konstanta $c$ harus sama dengan nilai absis titik $x = 4$.</sub>
- **B. $8$** ✅  
  <sub>Benar: Syarat kontinu adalah $f(4) = \lim_{x\to 4} f(x)$. Nilai $\lim_{x\to 4}\frac{x^2-16}{x-4} = \lim_{x\to 4}(x+4) = 8$, sehingga $c = 8$.</sub>
- C. $0$  
  <sub>Salah: Langsung menyubstitusikan $x=4$ ke pembilang dan penyebut sehingga memperoleh bentuk $0/0$ lalu menyimpulkan bernilai $0$.</sub>
- D. $-8$  
  <sub>Salah: Salah mengalikan tanda faktor menjadi $x - 4$ sehingga menghasilkan $-4 - 4 = -8$.</sub>

**Pembahasan:** Berdasarkan definisi kekontinuan, fungsi $f(x)$ kontinu di $x = 4$ jika $\lim_{x\to 4} f(x) = f(4)$.
Hitung nilai limit fungsi untuk $x \to 4$:
$$\lim_{x\to 4} \dfrac{x^2 - 16}{x - 4} = \lim_{x\to 4} \dfrac{(x - 4)(x + 4)}{x - 4} = \lim_{x\to 4} (x + 4) = 4 + 4 = 8.$$
Karena $f(4) = c$, maka agar kontinu diperoleh $c = 8$.
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b02-a-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: limit perkalian fungsi aljabar*

Diketahui $\displaystyle\lim_{x\to 5} g(x) = 6$. Nilai dari $\displaystyle\lim_{x\to 5}\left(g(x)\cdot\dfrac{4}{\sqrt{x}+\sqrt{5}}\right)$ adalah ....

- **A. $\dfrac{12}{5}\sqrt{5}$** ✅  
  <sub>Benar: Menggunakan sifat limit perkalian diperoleh $6 \cdot \frac{4}{\sqrt{5}+\sqrt{5}} = \frac{24}{2\sqrt{5}} = \frac{12}{\sqrt{5}} = \frac{12}{5}\sqrt{5}$.</sub>
- B. $\dfrac{24}{5}\sqrt{5}$  
  <sub>Salah: Siswa keliru menjumlahkan $\sqrt{5} + \sqrt{5}$ menjadi $\sqrt{5}$ sehingga tidak membagi koefisien dengan 2.</sub>
- C. $\dfrac{6}{5}\sqrt{5}$  
  <sub>Salah: Siswa lupa mengalikan dengan pembilang 4.</sub>
- D. $12\sqrt{5}$  
  <sub>Salah: Siswa salah saat merasionalkan penyebut, lupa membagi dengan 5.</sub>

**Pembahasan:** Berdasarkan sifat limit perkalian dan substitusi langsung:
$$\begin{aligned} \lim_{x\to 5}\left(g(x)\cdot\dfrac{4}{\sqrt{x}+\sqrt{5}}\right) &= \left(\lim_{x\to 5} g(x)\right) \cdot \left(\lim_{x\to 5}\dfrac{4}{\sqrt{x}+\sqrt{5}}\right) \\ &= 6 \cdot \dfrac{4}{\sqrt{5}+\sqrt{5}} \\ &= 6 \cdot \dfrac{4}{2\sqrt{5}} \\ &= \dfrac{12}{\sqrt{5}} \\ &= \dfrac{12}{5}\sqrt{5} \end{aligned}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b02-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: limit bentuk akar fungsi rasional*

Gunakan sifat-sifat limit untuk menentukan nilai dari $\displaystyle\lim_{y\to 3}\sqrt{\dfrac{3y^2+9}{2y^2+y+4}}$.

- **A. $\dfrac{6}{5}$** ✅  
  <sub>Benar: Menghitung limit di dalam akar diperoleh $\frac{3(9)+9}{2(9)+3+4} = \frac{36}{25}$, kemudian ditarik akar menghasilkan $\frac{6}{5}$.</sub>
- B. $\dfrac{36}{25}$  
  <sub>Salah: Siswa lupa menarik akar kuadrat dari hasil pembagian.</sub>
- C. $\dfrac{5}{6}$  
  <sub>Salah: Siswa membalik posisi pembilang dan penyebut.</sub>
- D. $\dfrac{4}{5}$  
  <sub>Salah: Siswa salah menghitung pembilang $3(3^2)+9$ menjadi $16$ bukan $36$.</sub>

**Pembahasan:** Menggunakan sifat limit akar:
$$\lim_{y\to 3}\sqrt{\dfrac{3y^2+9}{2y^2+y+4}} = \sqrt{\lim_{y\to 3}\dfrac{3y^2+9}{2y^2+y+4}}$$
Substitusikan $y = 3$:
$$= \sqrt{\dfrac{3(3)^2+9}{2(3)^2+3+4}} = \sqrt{\dfrac{27+9}{18+3+4}} = \sqrt{\dfrac{36}{25}} = \dfrac{6}{5}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b02-a-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: definisi turunan fungsi*

Berdasarkan definisi turunan fungsi $f'(a) = \displaystyle\lim_{h\to 0}\dfrac{f(a+h) - f(a)}{h}$, nilai dari $f'(3)$ untuk fungsi $f(x) = 2x^2 - 3x$ adalah ....

- **A. $9$** ✅  
  <sub>Benar: Ekspansi $\frac{f(3+h)-f(3)}{h} = \frac{9h+2h^2}{h} = 9+2h$, saat $h\to 0$ bernilai 9.</sub>
- B. $12$  
  <sub>Salah: Siswa hanya menghitung turunan dari suku pertama $2x^2$ di $x=3$ yaitu $4(3) = 12$ dan mengabaikan suku $-3x$.</sub>
- C. $15$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada suku linear sehingga diperoleh $12 + 3 = 15$.</sub>
- D. $6$  
  <sub>Salah: Siswa salah saat menguraikan kuadrat $(3+h)^2$ menjadi $9+h^2$ tanpa suku tengah $6h$.</sub>

**Pembahasan:** Hitung $f(3)$ dan $f(3+h)$:
$$f(3) = 2(3)^2 - 3(3) = 18 - 9 = 9$$
$$\begin{aligned} f(3+h) &= 2(3+h)^2 - 3(3+h) \\ &= 2(9 + 6h + h^2) - 9 - 3h \\ &= 18 + 12h + 2h^2 - 9 - 3h \\ &= 9 + 9h + 2h^2 \end{aligned}$$
Substitusikan ke dalam rumus definisi turunan:
$$\begin{aligned} f'(3) &= \lim_{h\to 0}\dfrac{f(3+h) - f(3)}{h} \\ &= \lim_{h\to 0}\dfrac{(9 + 9h + 2h^2) - 9}{h} \\ &= \lim_{h\to 0}\dfrac{h(9 + 2h)}{h} \\ &= \lim_{h\to 0}(9 + 2h) = 9 \end{aligned}$$
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b02-a-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: parameter kontinuitas fungsi*

Diketahui fungsi:
$$g(x) = \begin{cases} \dfrac{x^2 + 2x - 15}{x - 3}, & x \neq 3 \\ 2k + 1, & x = 3 \end{cases}$$
Agar fungsi $g(x)$ kontinu di titik $x = 3$, nilai konstanta $k$ harus bernilai ....

- A. $7$  
  <sub>Salah: Siswa menyelesaikan $2k = 7$ tetapi lupa membagi dengan koefisien $2$.</sub>
- B. $\dfrac{9}{2}$  
  <sub>Salah: Siswa salah mengoperasikan persamaan menjadi $2k - 1 = 8$ sehingga $k = \frac{9}{2}$.</sub>
- C. $\dfrac{5}{2}$  
  <sub>Salah: Siswa salah menghitung limit menjadi $6$ sehingga $2k + 1 = 6 \implies k = \frac{5}{2}$.</sub>
- **D. $\dfrac{7}{2}$** ✅  
  <sub>Benar: Nilai limit $\lim_{x\to 3}\frac{(x-3)(x+5)}{x-3} = 8$, disamakan dengan $g(3) = 2k+1$ sehingga $k = \frac{7}{2}$.</sub>

**Pembahasan:** Agar $g(x)$ kontinu di $x = 3$, maka harus dipenuhi syarat:
$$\lim_{x\to 3} g(x) = g(3)$$
Hitung nilai limit $x \to 3$:
$$\begin{aligned} \lim_{x\to 3}\dfrac{x^2 + 2x - 15}{x - 3} &= \lim_{x\to 3}\dfrac{(x - 3)(x + 5)}{x - 3} \\ &= \lim_{x\to 3}(x + 5) \\ &= 3 + 5 = 8 \end{aligned}$$
Samakan dengan $g(3) = 2k + 1$:
$$2k + 1 = 8 \implies 2k = 7 \implies k = \dfrac{7}{2}$$
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b02-a-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: limit fungsi trigonometri*

Tentukan nilai dari $\displaystyle\lim_{x\to \frac{\pi}{4}}\left(\dfrac{2 - 2\tan x}{\cos x - \sin x}\right)$.

- **A. $2\sqrt{2}$** ✅  
  <sub>Benar: Mengubah bentuk $2 - 2\tan x = 2\left(1 - \frac{\sin x}{\cos x}\right) = 2\left(\frac{\cos x - \sin x}{\cos x}\right)$, sehingga limit menjadi $\lim_{x\to \frac{\pi}{4}} \frac{2}{\cos x} = \frac{2}{\cos(\pi/4)} = \frac{2}{\frac{1}{2}\sqrt{2}} = 2\sqrt{2}$.</sub>
- B. $\sqrt{2}$  
  <sub>Salah: Lupa mengalikan dengan konstanta 2 pada pembilang.</sub>
- C. $-2\sqrt{2}$  
  <sub>Salah: Tertukar tanda saat menyederhanakan pembilang $(\cos x - \sin x)$ dengan penyebut.</sub>
- D. $-\sqrt{2}$  
  <sub>Salah: Salah tanda dan lupa mengalikan dengan faktor 2.</sub>

**Pembahasan:** Ubah bentuk pembilang dengan identitas tangen:
$$\begin{aligned} 2 - 2\tan x &= 2(1 - \tan x) = 2\left(1 - \frac{\sin x}{\cos x}\right) = \frac{2(\cos x - \sin x)}{\cos x} \end{aligned}$$
Substitusikan kembali ke limit:
$$\begin{aligned} \lim_{x\to \frac{\pi}{4}}\left(\frac{\frac{2(\cos x - \sin x)}{\cos x}}{\cos x - \sin x}\right) &= \lim_{x\to \frac{\pi}{4}} \frac{2}{\cos x} \\ &= \frac{2}{\cos\frac{\pi}{4}} = \frac{2}{\frac{1}{2}\sqrt{2}} = \frac{4}{\sqrt{2}} = 2\sqrt{2} \end{aligned}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b02-a-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: parameter kontinuitas fungsi*

Diberikan fungsi $g(x) = \begin{cases} mx + 5, & x \le 2 \\ 3x^2 - 1, & x > 2 \end{cases}$. Tentukan nilai $m$ agar fungsi $g(x)$ kontinu di seluruh $\mathbb{R}$.

- A. $8$  
  <sub>Salah: Salah operasi aljabar dengan menjumlahkan $11 + 5 = 16$ lalu membaginya dengan 2.</sub>
- B. $\dfrac{11}{2}$  
  <sub>Salah: Mengabaikan konstanta 5 pada cabang kiri dan langsung menyamakan $2m = 11$.</sub>
- **C. $3$** ✅  
  <sub>Benar: Syarat kontinu di $x = 2$ adalah $\lim_{x\to 2^-} g(x) = \lim_{x\to 2^+} g(x) = g(2)$. Diperoleh $2m + 5 = 3(2)^2 - 1 = 11$, sehingga $2m = 6 \implies m = 3$.</sub>
- D. $-3$  
  <sub>Salah: Salah tanda saat memindahkan konstanta 5 ke ruas kanan.</sub>

**Pembahasan:** Agar $g(x)$ kontinu di seluruh $\mathbb{R}$, $g(x)$ harus kontinu di titik batas $x = 2$:
1. Nilai fungsi dan limit kiri:
$$g(2) = \lim_{x\to 2^-} (mx + 5) = 2m + 5$$
2. Limit kanan:
$$\lim_{x\to 2^+} (3x^2 - 1) = 3(2)^2 - 1 = 12 - 1 = 11$$
3. Syarat kekontinuan $\lim_{x\to 2^-} g(x) = \lim_{x\to 2^+} g(x)$:
$$2m + 5 = 11 \iff 2m = 6 \iff m = 3$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b02-a-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: limit perkalian fungsi aljabar*

Diketahui $\displaystyle\lim_{x\to 6} g(x) = 4$. Tentukan nilai dari $\displaystyle\lim_{x\to 6}\left(g(x)\cdot\dfrac{3}{\sqrt{x}+\sqrt{6}}\right)$.

- A. $6$  
  <sub>Salah: Salah konsep merasionalkan bentuk akar dengan menghilangkan tanda akar pada penyelesaian akhir.</sub>
- B. $\dfrac{1}{2}\sqrt{6}$  
  <sub>Salah: Salah membagi saat merasionalkan pecahan sehingga menghasilkan setengah dari nilai sebenarnya.</sub>
- C. $2\sqrt{6}$  
  <sub>Salah: Lupa menjumlahkan dua suku akar di penyebut sehingga penyebut dianggap hanya $\sqrt{6}$.</sub>
- **D. $\sqrt{6}$** ✅  
  <sub>Benar: Dengan sifat perkalian limit, diperoleh $4 \cdot \frac{3}{\sqrt{6}+\sqrt{6}} = 4 \cdot \frac{3}{2\sqrt{6}} = \frac{6}{\sqrt{6}} = \sqrt{6}$.</sub>

**Pembahasan:** Gunakan sifat limit perkalian:
$$\begin{aligned} \lim_{x\to 6}\left(g(x)\cdot\frac{3}{\sqrt{x}+\sqrt{6}}\right) &= \lim_{x\to 6} g(x) \cdot \lim_{x\to 6} \frac{3}{\sqrt{x}+\sqrt{6}} \\ &= 4 \cdot \frac{3}{\sqrt{6}+\sqrt{6}} \\ &= 4 \cdot \frac{3}{2\sqrt{6}} \\ &= \frac{12}{2\sqrt{6}} = \frac{6}{\sqrt{6}} = \sqrt{6} \end{aligned}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b02-a-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: kemiringan garis sekan*

Sebuah garis sekan menghubungkan titik $P(1, f(1))$ dan $R(1 + \Delta x, f(1 + \Delta x))$ pada kurva fungsi $f(x) = 2x^2 + 5x$. Jika $\Delta x = 3$, tentukan kemiringan garis sekan $PR$ tersebut.

- A. $13$  
  <sub>Salah: Salah menghitung nilai fungsi $f(4)$ menjadi 46 sehingga $(46-7)/3 = 13$.</sub>
- B. $45$  
  <sub>Salah: Hanya menghitung selisih ordinat $f(4) - f(1)$ tanpa membaginya dengan $\Delta x = 3$.</sub>
- C. $9$  
  <sub>Salah: Menghitung turunan sesaat $f'(1) = 4(1) + 5 = 9$ alih-alih kemiringan garis sekan.</sub>
- **D. $15$** ✅  
  <sub>Benar: $f(1) = 7$, $f(4) = 52$, sehingga kemiringan garis sekan adalah $m = \frac{f(4) - f(1)}{\Delta x} = \frac{52 - 7}{3} = \frac{45}{3} = 15$.</sub>

**Pembahasan:** Diketahui $x_1 = 1$ dan $\Delta x = 3$, maka $x_2 = 1 + 3 = 4$.
Hitung nilai fungsi pada kedua titik:
- $f(1) = 2(1)^2 + 5(1) = 2 + 5 = 7$
- $f(4) = 2(4)^2 + 5(4) = 2(16) + 20 = 52$

Kemiringan garis sekan $PR$ adalah:
$$m = \frac{f(x_1 + \Delta x) - f(x_1)}{\Delta x} = \frac{52 - 7}{3} = \frac{45}{3} = 15$$
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b02-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: laju perubahan sesaat fungsi*

Laju perubahan sesaat fungsi $f(x) = \sqrt{x + 1}$ pada titik $x = 3$ ditentukan oleh nilai limit $\displaystyle\lim_{h\to 0}\dfrac{f(3+h)-f(3)}{h}$. Nilai laju perubahan sesaat tersebut adalah ....

- A. $4$  
  <sub>Salah: Terbalik menempatkan hasil perhitungan antara pembilang dan penyebut.</sub>
- B. $\dfrac{1}{8}$  
  <sub>Salah: Salah mengalikan sekawan sehingga menghasilkan penyebut dua kali lipat lebih besar.</sub>
- **C. $\dfrac{1}{4}$** ✅  
  <sub>Benar: Bentuk $\frac{\sqrt{4+h}-2}{h}$ dikalikan sekawannya menjadi $\frac{1}{\sqrt{4+h}+2}$, yang bernilai $\frac{1}{2+2} = \frac{1}{4}$ saat $h \to 0$.</sub>
- D. $\dfrac{1}{2}$  
  <sub>Salah: Hanya menghitung $\frac{1}{\sqrt{4}}$ tanpa menjumlahkan dengan 2 pada penyebut hasil kali sekawan.</sub>

**Pembahasan:** Hitung $f(3) = \sqrt{3 + 1} = \sqrt{4} = 2$ dan $f(3+h) = \sqrt{(3+h)+1} = \sqrt{4+h}$.
Susun limit definisi laju perubahan sesaat:
$$\lim_{h\to 0}\frac{\sqrt{4+h} - 2}{h}$$
Kalikan pembilang dan penyebut dengan bentuk sekawan $(\sqrt{4+h} + 2)$:
$$\begin{aligned} \lim_{h\to 0}\frac{(\sqrt{4+h} - 2)(\sqrt{4+h} + 2)}{h(\sqrt{4+h} + 2)} &= \lim_{h\to 0}\frac{(4+h) - 4}{h(\sqrt{4+h} + 2)} \\ &= \lim_{h\to 0}\frac{h}{h(\sqrt{4+h} + 2)} \\ &= \lim_{h\to 0}\frac{1}{\sqrt{4+h} + 2} \\ &= \frac{1}{\sqrt{4+0} + 2} = \frac{1}{2+2} = \frac{1}{4} \end{aligned}$$
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b02-a-medium-bt01-014
*variasi (angka) | C3 | 3 langkah | jenis: limit bentuk akar fungsi rasional*

Dengan menggunakan sifat-sifat limit fungsi, tentukan nilai dari $\displaystyle\lim_{y\to 4}\sqrt{\dfrac{y^2 + 9}{2y^2 - 7y + 12}}$.

- A. $\dfrac{5}{2}$  
  <sub>Salah: Siswa salah menghitung penyebut menjadi 4 alih-alih 16 sebelum menarik akar kuadrat.</sub>
- **B. $\dfrac{5}{4}$** ✅  
  <sub>Benar: Berdasarkan sifat limit, $\lim\sqrt{f(y)} = \sqrt{\lim f(y)}$. Nilai pembilang saat $y\to 4$ adalah $4^2+9 = 25$ dan penyebut $2(4)^2 - 7(4) + 12 = 32 - 28 + 12 = 16$. Maka hasilnya $\sqrt{\frac{25}{16}} = \frac{5}{4}$.</sub>
- C. $\dfrac{4}{5}$  
  <sub>Salah: Siswa terbalik menempatkan pembilang dan penyebut sehingga memperoleh kebalikan dari jawaban yang benar.</sub>
- D. $\dfrac{25}{16}$  
  <sub>Salah: Siswa menghitung nilai limit pecahan di dalam akar dengan benar namun lupa menarik akar kuadratnya.</sub>

**Pembahasan:** Langkah 1: Terapkan sifat limit fungsi akar:
$$\lim_{y\to 4}\sqrt{\dfrac{y^2 + 9}{2y^2 - 7y + 12}} = \sqrt{\lim_{y\to 4}\dfrac{y^2 + 9}{2y^2 - 7y + 12}}$$

Langkah 2: Terapkan sifat limit pembagian fungsi:
$$\lim_{y\to 4}\dfrac{y^2 + 9}{2y^2 - 7y + 12} = \dfrac{4^2 + 9}{2(4^2) - 7(4) + 12} = \dfrac{16 + 9}{32 - 28 + 12} = \dfrac{25}{16}$$

Langkah 3: Tarik akar dari hasil limit:
$$\sqrt{\dfrac{25}{16}} = \dfrac{5}{4}$$

Jadi, nilai limit tersebut adalah $\dfrac{5}{4}$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b02-a-medium-bt01-015
*variasi (angka) | C3 | 3 langkah | jenis: turunan fungsi aljabar*

Diketahui fungsi $f(x) = \dfrac{3}{2}x^2$. Nilai dari $f'(-4) \cdot f'(2)$ adalah ....

- **A. $-72$** ✅  
  <sub>Benar: Turunan pertama fungsi $f(x) = \frac{3}{2}x^2$ adalah $f'(x) = 3x$. Nilai $f'(-4) = 3(-4) = -12$ dan $f'(2) = 3(2) = 6$. Hasil kalinya adalah $(-12) \cdot 6 = -72$.</sub>
- B. $72$  
  <sub>Salah: Siswa mengabaikan tanda negatif pada saat menghitung $f'(-4)$.</sub>
- C. $-36$  
  <sub>Salah: Siswa salah menurunkan fungsi dengan lupa mengalikan koefisien dengan pangkat, mengira $f'(x) = \frac{3}{2}x$.</sub>
- D. $-24$  
  <sub>Salah: Siswa menjumlahkan $f'(-4) + f'(2) = -12 + 6 = -6$ lalu dikalikan 4 secara keliru.</sub>

**Pembahasan:** Langkah 1: Tentukan turunan fungsi $f(x)$ dengan rumus dasar turunan:
$$f'(x) = \lim_{h\to 0}\dfrac{\frac{3}{2}(x+h)^2 - \frac{3}{2}x^2}{h} = 3x$$

Langkah 2: Hitung nilai $f'(-4)$ dan $f'(2)$:
$$f'(-4) = 3(-4) = -12$$
$$f'(2) = 3(2) = 6$$

Langkah 3: Hitung hasil kali kedua nilai tersebut:
$$f'(-4) \cdot f'(2) = -12 \cdot 6 = -72$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b02-a-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: laju perubahan rata-rata dan sesaat*

Sebuah benda bergerak sepanjang lintasan lurus dengan posisi yang dinyatakan oleh $s(t) = 3t^2 + 2t$ ($s$ dalam meter dan $t$ dalam detik). Selisih antara kecepatan rata-rata benda dari $t = 1$ hingga $t = 4$ detik dengan kecepatan sesaat benda pada $t = 2$ detik adalah ....

- A. $14\text{ m/s}$  
  <sub>Salah: Siswa hanya menghitung nilai kecepatan sesaat pada $t = 2$ detik.</sub>
- **B. $3\text{ m/s}$** ✅  
  <sub>Benar: Kecepatan rata-rata dari $t = 1$ ke $t = 4$ adalah $\frac{s(4)-s(1)}{4-1} = \frac{56-5}{3} = 17\text{ m/s}$. Kecepatan sesaat pada $t = 2$ adalah $s'(2) = 6(2)+2 = 14\text{ m/s}$. Selisihnya adalah $17 - 14 = 3\text{ m/s}$.</sub>
- C. $5\text{ m/s}$  
  <sub>Salah: Siswa salah menghitung selang waktu pembagi pada kecepatan rata-rata atau salah mengevaluasi nilai fungsi.</sub>
- D. $17\text{ m/s}$  
  <sub>Salah: Siswa hanya menghitung nilai kecepatan rata-rata dan lupa menguranginya dengan kecepatan sesaat.</sub>

**Pembahasan:** Langkah 1: Hitung kecepatan rata-rata pada interval $[1, 4]$:
$$s(4) = 3(4^2) + 2(4) = 48 + 8 = 56$$
$$s(1) = 3(1^2) + 2(1) = 3 + 2 = 5$$
$$v_{\text{rata-rata}} = \dfrac{s(4) - s(1)}{4 - 1} = \dfrac{56 - 5}{3} = \dfrac{51}{3} = 17\text{ m/s}$$

Langkah 2: Tentukan kecepatan sesaat pada $t = 2$ menggunakan turunan fungsi posisi:
$$v(t) = s'(t) = 6t + 2$$
$$v(2) = s'(2) = 6(2) + 2 = 14\text{ m/s}$$

Langkah 3: Hitung selisih kedua besaran tersebut:
$$\Delta v = 17\text{ m/s} - 14\text{ m/s} = 3\text{ m/s}$$
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b02-a-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: limit trigonometri identitas*

Nilai dari $\displaystyle\lim_{x\to 0}\dfrac{1 - \cos 4x}{x\sin 2x}$ adalah ....

- A. $1$  
  <sub>Salah: Siswa membagi koefisien langsung tanpa menguraikan rumus sudut rangkap kosinus dengan tepat.</sub>
- **B. $4$** ✅  
  <sub>Benar: Identitas $1 - \cos 4x = 2\sin^2(2x)$. Bentuk limit menjadi $\lim_{x\to 0}\frac{2\sin(2x)\sin(2x)}{x\sin(2x)} = \lim_{x\to 0}\frac{2\sin(2x)}{x} = 2 \cdot 2 = 4$.</sub>
- C. $8$  
  <sub>Salah: Siswa salah mengalikan kuadrat koefisien sehingga mendapatkan hasil dua kali lipat.</sub>
- D. $2$  
  <sub>Salah: Siswa melupakan faktor perkalian 2 dari turunan sudut atau identitas sudut rangkap.</sub>

**Pembahasan:** Langkah 1: Ubah $1 - \cos 4x$ menggunakan identitas trigonometri sudut rangkap:
$$1 - \cos 4x = 2\sin^2(2x)$$

Langkah 2: Substitusikan ke dalam bentuk limit dan sederhanakan:
$$\lim_{x\to 0}\dfrac{2\sin^2(2x)}{x\sin 2x} = \lim_{x\to 0}\dfrac{2\sin(2x)\cdot\sin(2x)}{x\sin 2x} = \lim_{x\to 0}\dfrac{2\sin 2x}{x}$$

Langkah 3: Terapkan sifat limit trigonometri $\lim_{x\to 0}\dfrac{\sin ax}{x} = a$:
$$\lim_{x\to 0} 2 \cdot \dfrac{\sin 2x}{x} = 2 \cdot 2 = 4$$
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b02-a-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: garis tangen kurva*

Garis tangen (garis singgung) pada kurva $f(x) = 4 - x^2$ di titik berabsis $x = 1$ memotong sumbu-$Y$ di titik $(0, c)$. Nilai $c$ yang memenuhi adalah ....

- A. $3$  
  <sub>Salah: Siswa mengira nilai $c$ langsung sama dengan nilai ordinat titik singgung $f(1) = 3$.</sub>
- B. $-2$  
  <sub>Salah: Siswa mengira nilai $c$ adalah gradien garis tangen $m = -2$.</sub>
- **C. $5$** ✅  
  <sub>Benar: Titik singgung adalah $(1, f(1)) = (1, 3)$. Kemiringan garis tangen adalah $m = f'(1) = -2(1) = -2$. Persamaan garis tangen adalah $y - 3 = -2(x - 1) \implies y = -2x + 5$. Titik potong sumbu-$Y$ berada pada $(0, 5)$, sehingga $c = 5$.</sub>
- D. $1$  
  <sub>Salah: Siswa salah saat menyusun persamaan garis singgung menjadi $y - 3 = -2x - 2$ sehingga $y = -2x + 1$.</sub>

**Pembahasan:** Langkah 1: Tentukan titik singgung $(x_1, y_1)$:
$$x_1 = 1 \implies y_1 = f(1) = 4 - 1^2 = 3$$
Titik singgung adalah $(1, 3)$.

Langkah 2: Tentukan gradien garis tangen ($m$) menggunakan turunan di $x = 1$:
$$m = f'(1) = \lim_{h\to 0}\dfrac{f(1+h)-f(1)}{h} = -2(1) = -2$$

Langkah 3: Susun persamaan garis tangen dan tentukan titik potong sumbu-$Y$:
$$y - y_1 = m(x - x_1)$$
$$y - 3 = -2(x - 1)$$
$$y - 3 = -2x + 2 \implies y = -2x + 5$$
Garis memotong sumbu-$Y$ di saat $x = 0$, sehingga $y = 5$. Maka diperoleh nilai $c = 5$.
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b02-a-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: turunan fungsi aljabar*

Diketahui fungsi $f(x) = \dfrac{5}{3}x^2$. Nilai dari $f'(-6) + f'(9)$ adalah ....

- A. $-50$  
  <sub>Salah: Siswa salah mengoperasikan tanda pada kedua suku menjadi $-20 - 30 = -50$.</sub>
- B. $50$  
  <sub>Salah: Siswa mengabaikan tanda negatif pada $f'(-6)$ sehingga menghitung $20 + 30 = 50$.</sub>
- **C. $10$** ✅  
  <sub>Benar: Turunan dari $f(x) = \frac{5}{3}x^2$ adalah $f'(x) = \frac{10}{3}x$. Diperoleh $f'(-6) = \frac{10}{3}(-6) = -20$ dan $f'(9) = \frac{10}{3}(9) = 30$, sehingga $f'(-6) + f'(9) = -20 + 30 = 10$.</sub>
- D. $-10$  
  <sub>Salah: Siswa tertukar tanda saat menjumlahkan nilai turunan, yaitu $20 - 30 = -10$.</sub>

**Pembahasan:** Berdasarkan definisi turunan fungsi aljabar:
$$f'(x) = \lim_{h\to 0}\dfrac{f(x+h)-f(x)}{h} = \lim_{h\to 0}\dfrac{\frac{5}{3}(x+h)^2 - \frac{5}{3}x^2}{h}$$
$$f'(x) = \lim_{h\to 0}\dfrac{\frac{5}{3}(2xh+h^2)}{h} = \lim_{h\to 0}\left(\dfrac{10}{3}x + \dfrac{5}{3}h\right) = \dfrac{10}{3}x$$

Selanjutnya, substitusikan nilai $x = -6$ dan $x = 9$ ke dalam fungsi turunan:
1. $f'(-6) = \dfrac{10}{3}(-6) = -20$
2. $f'(9) = \dfrac{10}{3}(9) = 30$

Jumlah dari kedua nilai tersebut adalah:
$$f'(-6) + f'(9) = -20 + 30 = 10$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b02-a-medium-bt01-020
*variasi (angka) | C3 | 3 langkah | jenis: limit fungsi trigonometri*

Tentukan nilai dari $\displaystyle\lim_{x\to 0}\dfrac{\tan 8x + 7x}{\sin 5x + 4x}$.

- A. $\dfrac{3}{5}$  
  <sub>Salah: Siswa terbalik meletakkan pembilang dan penyebut pada hasil akhir (resiprokal).</sub>
- B. $\dfrac{7}{4}$  
  <sub>Salah: Siswa mengabaikan fungsi trigonometri dan hanya membagi koefisien dari suku aljabar $\frac{7x}{4x}$.</sub>
- **C. $\dfrac{5}{3}$** ✅  
  <sub>Benar: Membagi pembilang dan penyebut dengan $x$ menghasilkan $\dfrac{\frac{\tan 8x}{x} + 7}{\frac{\sin 5x}{x} + 4}$. Dengan sifat limit fungsi trigonometri $\lim_{x\to 0}\frac{\tan 8x}{x} = 8$ dan $\lim_{x\to 0}\frac{\sin 5x}{x} = 5$, diperoleh $\dfrac{8 + 7}{5 + 4} = \dfrac{15}{9} = \dfrac{5}{3}$.</sub>
- D. $\dfrac{8}{5}$  
  <sub>Salah: Siswa mengabaikan koefisien sudut fungsi trigonometri dan menganggap nilai $\lim_{x\to 0}\frac{\tan 8x}{x} = 1$ serta $\lim_{x\to 0}\frac{\sin 5x}{x} = 1$, sehingga menghitung $\frac{1 + 7}{1 + 4} = \frac{8}{5}$.</sub>

**Pembahasan:** Untuk menentukan nilai limit bentuk tak tentu $\frac{0}{0}$, kalikan pembilang dan penyebut dengan $\frac{1}{x}$:
$$\lim_{x\to 0}\dfrac{\tan 8x + 7x}{\sin 5x + 4x} = \lim_{x\to 0}\dfrac{\dfrac{\tan 8x}{x} + 7}{\dfrac{\sin 5x}{x} + 4}$$

Berdasarkan sifat limit fungsi trigonometri:
$$\lim_{x\to 0}\dfrac{\tan ax}{x} = a \implies \lim_{x\to 0}\dfrac{\tan 8x}{x} = 8$$
$$\lim_{x\to 0}\dfrac{\sin bx}{x} = b \implies \lim_{x\to 0}\dfrac{\sin 5x}{x} = 5$$

Substitusikan nilai limit tersebut:
$$= \dfrac{8 + 7}{5 + 4} = \dfrac{15}{9} = \dfrac{5}{3}$$
**Acuan:** siswa — siswa hal.108 Ayo Mencoba 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b02-a-hard-bt01-001
*orisinal | C5 | 5 langkah | jenis: keterdiferensiasian fungsi*

Diberikan fungsi berikut:
$$f(x) = \begin{cases} ax^2 + 5x, & x \le 2 \\ 2x^2 + bx + 4, & x > 2 \end{cases}$$
Agar fungsi $f(x)$ mempunyai turunan di titik $x = 2$, nilai dari $a + b$ adalah ....

- A. $7$  
  <sub>Salah: Siswa hanya menyamakan turunan sepihak tanpa mengindahkan syarat kontinuitas fungsi.</sub>
- B. $0$  
  <sub>Salah: Siswa menghitung nilai $a - b = 1 - 1 = 0$ alih-alih nilai $a + b$.</sub>
- C. $5$  
  <sub>Salah: Siswa salah melakukan eliminasi sistem persamaan sehingga mendapatkan $a = 2$ dan $b = 3$.</sub>
- **D. $2$** ✅  
  <sub>Benar: Fungsi harus kontinu di $x = 2$, sehingga $4a + 10 = 12 + 2b \implies 2a - b = 1$. Turunan kiri harus sama dengan turunan kanan: $f'_-(2) = 4a + 5$ dan $f'_+(2) = 8 + b$, sehingga $4a - b = 3$. Mengurangkan kedua persamaan menghasilkan $2a = 2 \implies a = 1$, lalu $b = 1$. Jadi, $a + b = 2$.</sub>

**Pembahasan:** Agar $f(x)$ mempunyai turunan di $x = 2$, fungsi harus memenuhi dua syarat:
1. Kontinu di $x = 2$:
$$\lim_{x\to 2^-} f(x) = \lim_{x\to 2^+} f(x) = f(2)$$
$$a(2)^2 + 5(2) = 2(2)^2 + b(2) + 4$$
$$4a + 10 = 8 + 2b + 4$$
$$4a - 2b = 2 \iff 2a - b = 1 \quad \text{...(Persamaan 1)}$$

2. Turunan sepihak kiri sama dengan turunan sepihak kanan di $x = 2$:
Turunan kiri:
$$f'_-(2) = \lim_{h\to 0^-} \dfrac{a(2+h)^2 + 5(2+h) - (4a+10)}{h} = 4a + 5$$
Turunan kanan:
$$f'_+(2) = \lim_{h\to 0^+} \dfrac{2(2+h)^2 + b(2+h) + 4 - (12+2b)}{h} = 8 + b$$
Menyamakan kedua turunan sepihak:
$$4a + 5 = 8 + b \iff 4a - b = 3 \quad \text{...(Persamaan 2)}$$

3. Mengeliminasi Persamaan (2) dan Persamaan (1):
$$(4a - b) - (2a - b) = 3 - 1$$
$$2a = 2 \implies a = 1$$
Substitusikan $a = 1$ ke Persamaan 1:
$$2(1) - b = 1 \implies b = 1$$

Maka, nilai $a + b = 1 + 1 = 2$.
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b02-a-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: limit fungsi trigonometri*

Diketahui nilai limit trigonometri berikut:
$$\lim_{x\to 0} \dfrac{\cos(ax) - \cos(bx)}{x^2} = 16$$
Jika $a$ dan $b$ adalah bilangan bulat positif dengan $a + b = 8$, tentukan nilai dari $b - a$.

- A. $2$  
  <sub>Salah: Siswa lupa mengalikan faktor 2 pada identitas trigonometri sehingga menganggap $b^2 - a^2 = 16$ dan $b - a = 2$.</sub>
- **B. $4$** ✅  
  <sub>Benar: Menggunakan identitas $\cos(ax) - \cos(bx) = -2\sin\left(\frac{a+b}{2}x\right)\sin\left(\frac{a-b}{2}x\right)$, nilai limitnya adalah $\frac{b^2 - a^2}{2}$. Dengan $\frac{b^2 - a^2}{2} = 16$, diperoleh $(b - a)(b + a) = 32$. Karena $a + b = 8$, maka $b - a = \frac{32}{8} = 4$.</sub>
- C. $-4$  
  <sub>Salah: Siswa terbalik dalam melakukan pengurangan tanda pada rumus selisih kosinus.</sub>
- D. $8$  
  <sub>Salah: Siswa keliru mengira nilai $b - a$ sama dengan nilai $a + b$ yang diberikan pada soal.</sub>

**Pembahasan:** Gunakan identitas selisih kosinus:
$$\cos A - \cos B = -2\sin\left(\dfrac{A+B}{2}\right)\sin\left(\dfrac{A-B}{2}\right)$$
Sehingga:
$$\cos(ax) - \cos(bx) = -2\sin\left(\dfrac{a+b}{2}x\right)\sin\left(\dfrac{a-b}{2}x\right) = 2\sin\left(\dfrac{a+b}{2}x\right)\sin\left(\dfrac{b-a}{2}x\right)$$

Hitung nilai limitnya saat $x \to 0$:
$$\lim_{x\to 0} \dfrac{\cos(ax) - \cos(bx)}{x^2} = \lim_{x\to 0} 2 \cdot \dfrac{\sin\left(\frac{a+b}{2}x\right)}{x} \cdot \dfrac{\sin\left(\frac{b-a}{2}x\right)}{x}$$
$$= 2 \cdot \left(\dfrac{a+b}{2}\right) \cdot \left(\dfrac{b-a}{2}\right) = \dfrac{b^2 - a^2}{2}$$

Diketahui nilai limit sama dengan 16:
$$\dfrac{b^2 - a^2}{2} = 16 \iff b^2 - a^2 = 32$$

Faktorkan bentuk selisih kuadrat:
$$(b - a)(b + a) = 32$$
Diketahui bahwa $a + b = 8$, sehingga:
$$(b - a) \cdot 8 = 32 \implies b - a = 4$$
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b02-a-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: laju perubahan sesaat dan rata-rata*

Sebuah partikel bergerak sepanjang lintasan lurus dengan fungsi posisi $s(t) = t^3 - 6t^2 + 15t$, dengan $s$ dalam meter dan $t$ dalam detik ($t \ge 0$). Kecepatan sesaat partikel pada saat $t = 3$ detik diketahui bernilai sama persis dengan kecepatan rata-rata partikel pada selang waktu $1 \le t \le k$ detik (dengan $k > 1$ dan $k \neq 3$). Nilai $k$ yang memenuhi adalah ....

- A. $2$  
  <sub>Salah: Siswa keliru menghitung kecepatan sesaat menjadi 4 m/s sehingga persamaan kuadrat yang diselesaikan menghasilkan akar $k = 2$.</sub>
- B. $1$  
  <sub>Salah: Siswa mengambil akar $k = 1$ yang melanggar syarat batas selang $k > 1$.</sub>
- **C. $4$** ✅  
  <sub>Benar: Kecepatan sesaat pada $t = 3$ adalah $s'(3) = 3(3)^2 - 12(3) + 15 = 6$ m/s. Kecepatan rata-rata pada interval $[1, k]$ adalah $\frac{s(k)-s(1)}{k-1} = \frac{k^3 - 6k^2 + 15k - 10}{k-1} = k^2 - 5k + 10$. Menyamakan keduanya: $k^2 - 5k + 10 = 6 \implies k^2 - 5k + 4 = 0 \implies (k-1)(k-4) = 0$. Karena $k > 1$, nilai yang memenuhi adalah $k = 4$.</sub>
- D. $5$  
  <sub>Salah: Siswa salah menjumlahkan kedua akar persamaan kuadrat ($1 + 4 = 5$) sebagai nilai solusi.</sub>

**Pembahasan:** 1. Menentukan kecepatan sesaat pada $t = 3$ detik menggunakan definisi turunan:
$$v(t) = s'(t) = 3t^2 - 12t + 15$$
$$v(3) = 3(3)^2 - 12(3) + 15 = 27 - 36 + 15 = 6\text{ m/s}$$

2. Menentukan posisi pada $t = 1$ dan $t = k$:
$$s(1) = 1^3 - 6(1)^2 + 15(1) = 10$$
$$s(k) = k^3 - 6k^2 + 15k$$

3. Menentukan rumus kecepatan rata-rata pada selang waktu $[1, k]$:
$$v_{\text{rata-rata}} = \dfrac{s(k) - s(1)}{k - 1} = \dfrac{k^3 - 6k^2 + 15k - 10}{k - 1}$$
Faktorkan pembilang dengan membaginya dengan $(k - 1)$:
$$k^3 - 6k^2 + 15k - 10 = (k - 1)(k^2 - 5k + 10)$$
Sehingga:
$$v_{\text{rata-rata}} = k^2 - 5k + 10$$

4. Menyamakan kecepatan rata-rata dengan kecepatan sesaat:
$$k^2 - 5k + 10 = 6$$
$$k^2 - 5k + 4 = 0$$
$$(k - 1)(k - 4) = 0$$
Diperoleh $k = 1$ atau $k = 4$.
Karena disyaratkan $k > 1$, nilai $k$ yang tepat adalah $k = 4$.
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b02-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: persamaan fungsional definisi turunan*

Suatu fungsi $f(x)$ terdefinisi untuk seluruh bilangan real dan memenuhi persamaan fungsional $f(x + y) = f(x) + f(y) + 4xy$ untuk setiap bilangan real $x$ dan $y$. Jika diketahui $\displaystyle\lim_{h\to 0} \frac{f(h)}{h} = 3$, tentukan nilai dari $f'(5)$ berdasarkan definisi limit turunan fungsi.

- A. $19$  
  <sub>Salah: Kesalahan tanda operasi saat memindahkan $f(x)$ sehingga menghitung $4x - 3 = 20 - 3 = 17$, atau salah hitung aritmetika $4(4)+3=19$.</sub>
- **B. $23$** ✅  
  <sub>Benar: Berdasarkan definisi turunan, $f'(x) = \lim_{h\to 0}\frac{f(x+h)-f(x)}{h}$. Dengan persamaan fungsional, $f(x+h)-f(x) = f(h) + 4xh$. Maka $f'(x) = \lim_{h\to 0}\frac{f(h)}{h} + \lim_{h\to 0} 4x = 3 + 4x$. Untuk $x = 5$, diperoleh $f'(5) = 3 + 4(5) = 23$.</sub>
- C. $20$  
  <sub>Salah: Hanya menghitung nilai dari limit suku aljabar $4x = 4(5) = 20$ dan melupakan nilai dari $\lim_{h\to 0}\frac{f(h)}{h}$.</sub>
- D. $35$  
  <sub>Salah: Salah menjumlahkan limit $f(h)/h$ dengan memasukkan nilai $h=3$ bukan nilai limitnya.</sub>

**Pembahasan:** Gunakan definisi turunan fungsi:
$$f'(x) = \lim_{h\to 0} \frac{f(x + h) - f(x)}{h}$$
Dari persamaan fungsional yang diberikan:
$$f(x + h) = f(x) + f(h) + 4xh \iff f(x + h) - f(x) = f(h) + 4xh$$
Substitusikan ke dalam definisi limit turunan:
$$f'(x) = \lim_{h\to 0} \frac{f(h) + 4xh}{h} = \lim_{h\to 0} \frac{f(h)}{h} + \lim_{h\to 0} \frac{4xh}{h}$$
Diketahui $\lim_{h\to 0}\frac{f(h)}{h} = 3$, maka:
$$f'(x) = 3 + 4x$$
Untuk $x = 5$:
$$f'(5) = 3 + 4(5) = 3 + 20 = 23$$
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b02-a-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: evaluasi kekontinuan fungsi*

Diberikan fungsi $f(x)$ sebagai berikut:
$$f(x) = \begin{cases} \dfrac{\sqrt{x + 7} - 3}{x - 2}, & x > 2 \\ a, & x = 2 \\ bx^2 + \dfrac{1}{12}, & x < 2 \end{cases}$$
Agar fungsi $f(x)$ kontinu di titik $x = 2$, nilai dari $\dfrac{a}{b}$ adalah ....

- A. $\dfrac{1}{8}$  
  <sub>Salah: Terbalik dalam menghitung rasio yang ditanyakan menjadi $\frac{b}{a}$.</sub>
- B. $2$  
  <sub>Salah: Lupa membagi dengan koefisien 4 saat mencari $b$ dari persamaan $4b = 1/12$, sehingga menganggap $b = 1/12$ lalu memperoleh rasio $(1/6)/(1/12) = 2$.</sub>
- C. $\dfrac{16}{3}$  
  <sub>Salah: Salah melakukan perkalian sekawan sehingga nilai limit kanan terhitung $\frac{1}{3}$ bukan $\frac{1}{6}$.</sub>
- **D. $8$** ✅  
  <sub>Benar: Limit kanan dihitung dengan merasionalkan pembilang sehingga diperoleh $\lim_{x\to 2^+} f(x) = \frac{1}{6}$, sehingga $a = f(2) = \frac{1}{6}$. Limit kiri $\lim_{x\to 2^-} f(x) = 4b + \frac{1}{12} = \frac{1}{6} \implies 4b = \frac{1}{12} \implies b = \frac{1}{48}$. Maka rasio $\frac{a}{b} = \frac{1/6}{1/48} = 8$.</sub>

**Pembahasan:** Agar $f(x)$ kontinu di $x = 2$, harus dipenuhi:
$$\lim_{x\to 2^+} f(x) = \lim_{x\to 2^-} f(x) = f(2) = a$$
1. Hitung limit kanan:
$$\lim_{x\to 2^+} \frac{\sqrt{x + 7} - 3}{x - 2} = \lim_{x\to 2^+} \frac{(\sqrt{x + 7} - 3)(\sqrt{x + 7} + 3)}{(x - 2)(\sqrt{x + 7} + 3)} = \lim_{x\to 2^+} \frac{x - 2}{(x - 2)(\sqrt{x + 7} + 3)}$$
$$= \lim_{x\to 2^+} \frac{1}{\sqrt{x + 7} + 3} = \frac{1}{\sqrt{9} + 3} = \frac{1}{6}$$
Maka nilai $a = f(2) = \frac{1}{6}$.

2. Hitung limit kiri dan samakan dengan limit kanan:
$$\lim_{x\to 2^-} \left(bx^2 + \frac{1}{12}\right) = b(2)^2 + \frac{1}{12} = 4b + \frac{1}{12}$$
$$4b + \frac{1}{12} = \frac{1}{6} \iff 4b = \frac{2}{12} - \frac{1}{12} = \frac{1}{12} \iff b = \frac{1}{48}$$

3. Hitung perbandingan $\frac{a}{b}$:
$$\frac{a}{b} = \frac{\frac{1}{6}}{\frac{1}{48}} = \frac{48}{6} = 8$$
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b02-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: hubungan garis sekan dan tangen*

Sebuah garis sekan $g_1$ memotong kurva $f(x) = x^2 - 2x$ di titik $P(2, f(2))$ dan titik $Q(2 + h, f(2 + h))$ dengan $h \neq 0$. Garis tangen $g_2$ menyinggung kurva $f(x)$ di titik $P(2, f(2))$. Jika kemiringan garis sekan $g_1$ bernilai dua kali lipat dari kemiringan garis tangen $g_2$, tentukan nilai dari $h$.

- A. $4$  
  <sub>Salah: Mengira kemiringan garis sekan sama dengan $h$ saja, sehingga $h = 4$.</sub>
- **B. $2$** ✅  
  <sub>Benar: Kemiringan tangen di $x = 2$ dihitung dengan limit turunan: $m_{\text{tangen}} = \lim_{h\to 0} \frac{(2+h)^2 - 2(2+h) - 0}{h} = \lim_{h\to 0} (2 + h) = 2$. Kemiringan garis sekan adalah $m_{\text{sekan}} = \frac{f(2+h)-f(2)}{h} = 2 + h$. Diketahui $m_{\text{sekan}} = 2 \cdot m_{\text{tangen}} \implies 2 + h = 2(2) = 4 \implies h = 2$.</sub>
- C. $6$  
  <sub>Salah: Salah menghitung turunan fungsi $f(x)$ dengan mengabaikan suku $-2x$, menghasilkan $m_{\text{tangen}} = 4$ dan $2 + h = 8 \implies h = 6$.</sub>
- D. $-1$  
  <sub>Salah: Terbalik menerapkan rasio perbandingan menjadi $m_{\text{tangen}} = 2 \cdot m_{\text{sekan}}$, menghasilkan $2 = 2(2 + h) \implies h = -1$.</sub>

**Pembahasan:** 1. Tentukan nilai $f(2)$:
$$f(2) = 2^2 - 2(2) = 0$$
2. Hitung kemiringan garis tangen $g_2$ menggunakan limit laju perubahan sesaat di $x = 2$:
$$m_{\text{tangen}} = \lim_{h\to 0} \frac{f(2 + h) - f(2)}{h} = \lim_{h\to 0} \frac{(2 + h)^2 - 2(2 + h) - 0}{h}$$
$$= \lim_{h\to 0} \frac{4 + 4h + h^2 - 4 - 2h}{h} = \lim_{h\to 0} \frac{2h + h^2}{h} = \lim_{h\to 0} (2 + h) = 2$$
3. Hitung kemiringan garis sekan $g_1$:
$$m_{\text{sekan}} = \frac{f(2 + h) - f(2)}{h} = \frac{2h + h^2}{h} = 2 + h$$
4. Terapkan hubungan $m_{\text{sekan}} = 2 \cdot m_{\text{tangen}}$:
$$2 + h = 2(2) \iff 2 + h = 4 \iff h = 2$$
**Acuan:** siswa — siswa hal.116

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b02-a-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: analisis kecepatan rata-rata dan sesaat*

Sebuah roket uji coba bergerak vertikal ke atas dengan persamaan lintasan $s(t) = 40t - 5t^2$, di mana $s$ menyatakan ketinggian roket dalam meter dan $t$ menyatakan waktu dalam detik. Kecepatan rata-rata roket pada interval waktu $t \in [2, 2 + \Delta t]$ bernilai sama dengan kecepatan sesaat roket tepat pada saat $t = 3$ detik. Nilai dari selang waktu $\Delta t$ tersebut adalah ....

- A. $4\text{ detik}$  
  <sub>Salah: Mengira kecepatan sesaat di $t=3$ adalah nol (saat titik puncak roket), sehingga $20 - 5\Delta t = 0 \implies \Delta t = 4\text{ detik}$.</sub>
- B. $1\text{ detik}$  
  <sub>Salah: Menghitung kecepatan sesaat pada $t=3$ menggunakan posisi dibagi waktu $s(3)/3 = 75/3 = 25$, lalu menyamakan $20 - 5\Delta t = 15$ atau salah hitung aritmetika tanda.</sub>
- **C. $2\text{ detik}$** ✅  
  <sub>Benar: Kecepatan rata-rata roket pada $[2, 2+\Delta t]$ adalah $\frac{s(2+\Delta t)-s(2)}{\Delta t} = 20 - 5\Delta t$. Kecepatan sesaat pada $t = 3$ dihitung dengan limit turunan: $v(3) = \lim_{h\to 0}\frac{s(3+h)-s(3)}{h} = 40 - 10(3) = 10\text{ m/s}$. Menyamakan keduanya: $20 - 5\Delta t = 10 \implies 5\Delta t = 10 \implies \Delta t = 2\text{ detik}$.</sub>
- D. $3\text{ detik}$  
  <sub>Salah: Salah menghitung kecepatan sesaat pada $t = 3$ menjadi $5\text{ m/s}$, sehingga $20 - 5\Delta t = 5 \implies \Delta t = 3\text{ detik}$.</sub>

**Pembahasan:** 1. Tentukan rumus kecepatan rata-rata pada interval waktu $[2, 2 + \Delta t]$:
$$s(2) = 40(2) - 5(2^2) = 80 - 20 = 60$$
$$s(2 + \Delta t) = 40(2 + \Delta t) - 5(2 + \Delta t)^2 = 80 + 40\Delta t - 5(4 + 4\Delta t + (\Delta t)^2)$$
$$= 80 + 40\Delta t - 20 - 20\Delta t - 5(\Delta t)^2 = 60 + 20\Delta t - 5(\Delta t)^2$$
$$v_{\text{rata-rata}} = \frac{s(2 + \Delta t) - s(2)}{\Delta t} = \frac{20\Delta t - 5(\Delta t)^2}{\Delta t} = 20 - 5\Delta t$$

2. Tentukan kecepatan sesaat pada $t = 3$ detik dengan limit turunan:
$$v(3) = \lim_{h\to 0} \frac{s(3 + h) - s(3)}{h}$$
$$s(3) = 40(3) - 5(3^2) = 120 - 45 = 75$$
$$s(3 + h) = 40(3 + h) - 5(3 + h)^2 = 120 + 40h - 5(9 + 6h + h^2) = 75 + 10h - 5h^2$$
$$v(3) = \lim_{h\to 0} \frac{10h - 5h^2}{h} = \lim_{h\to 0} (10 - 5h) = 10\text{ m/s}$$

3. Samakan kecepatan rata-rata dan kecepatan sesaat:
$$20 - 5\Delta t = 10 \iff 5\Delta t = 10 \iff \Delta t = 2\text{ detik}$$
**Acuan:** siswa — siswa hal.113

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b02-a-hard-bt01-008
*variasi (konteks) | C5 | 5 langkah | jenis: analisis kekontinuan fungsi piecewise*

Diberikan fungsi sebagai berikut:
$$h(x) = \begin{cases} \dfrac{x^2 + ax + b}{x - 3}, & x > 3 \\ 7, & x = 3 \\ 2x + c, & x < 3 \end{cases}$$
Jika fungsi $h(x)$ kontinu di seluruh himpunan bilangan real $\mathbb{R}$, tentukan nilai dari $a + b + c$.

- **A. $-10$** ✅  
  <sub>Benar: Syarat kekontinuan di $x = 3$ menghasilkan $c = 1$, $a = 1$, dan $b = -12$, sehingga $a + b + c = -10$.</sub>
- B. $-12$  
  <sub>Salah: Mengira nilai akhir sama dengan nilai konstanta $b$.</sub>
- C. $2$  
  <sub>Salah: Menghitung hanya $a + c$ dan mengabaikan nilai $b$.</sub>
- D. $-8$  
  <sub>Salah: Kesalahan tanda ketika menentukan nilai parameter $b$.</sub>

**Pembahasan:** Agar $h(x)$ kontinu di $\mathbb{R}$, syarat utama adalah kontinu di titik batas $x = 3$, yaitu $\lim_{x\to 3^-} h(x) = \lim_{x\to 3^+} h(x) = h(3) = 7$.
1. Dari limit kiri: $\lim_{x\to 3^-} (2x + c) = 2(3) + c = 6 + c = 7 \implies c = 1$.
2. Dari limit kanan: $\lim_{x\to 3^+} \dfrac{x^2 + ax + b}{x - 3} = 7$.
Karena penyebut mendekati 0, pembilang juga harus bernilai 0 di $x = 3$:
$$3^2 + 3a + b = 0 \implies b = -3a - 9$$
3. Faktorkan pembilang:
$$x^2 + ax - 3a - 9 = (x - 3)(x + 3) + a(x - 3) = (x - 3)(x + 3 + a)$$
4. Hitung limit kanannya:
$$\lim_{x\to 3^+} (x + 3 + a) = 3 + 3 + a = 6 + a = 7 \implies a = 1$$
5. Nilai $b = -3(1) - 9 = -12$.
Jadi, $a + b + c = 1 + (-12) + 1 = -10$.
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b02-a-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: evaluasi limit bentuk turunan*

Diketahui suatu fungsi $f(x)$ mempunyai turunan di $x = 2$ dengan nilai $f(2) = 5$ dan $f'(2) = -3$. Nilai dari $\displaystyle\lim_{x\to 2} \dfrac{x^2 f(2) - 4f(x)}{x - 2}$ adalah ....

- A. $8$  
  <sub>Salah: Kesalahan tanda operasi menjadi $4f(2) + 4f'(2) = 20 - 12 = 8$.</sub>
- B. $20$  
  <sub>Salah: Hanya menghitung suku pertama dan mengabaikan suku turunan.</sub>
- C. $-32$  
  <sub>Salah: Tertukar urutan pengurangan pada pemfaktoran limit turunan.</sub>
- **D. $32$** ✅  
  <sub>Benar: Memisahkan limit menjadi $\lim_{x\to 2}\frac{(x^2-4)f(2)}{x-2} - 4\lim_{x\to 2}\frac{f(x)-f(2)}{x-2}$ menghasilkan $4f(2) - 4f'(2) = 20 + 12 = 32$.</sub>

**Pembahasan:** Gunakan manipulasi aljabar dengan menambah dan mengurang suku $4f(2)$ pada pembilang:
$$\lim_{x\to 2} \dfrac{x^2 f(2) - 4f(x)}{x - 2} = \lim_{x\to 2} \dfrac{[x^2 f(2) - 4f(2)] - [4f(x) - 4f(2)]}{x - 2}$$
Pisahkan menjadi dua bentuk limit:
$$= \lim_{x\to 2} \dfrac{(x^2 - 4)f(2)}{x - 2} - 4\lim_{x\to 2}\dfrac{f(x) - f(2)}{x - 2}$$
Sederhanakan suku pertama menggunakan faktorisasi $(x - 2)(x + 2)$ dan kenali suku kedua sebagai $f'(2)$:
$$= \lim_{x\to 2} (x + 2)f(2) - 4f'(2)$$
Substitusikan nilai yang diketahui:
$$= (2 + 2)f(2) - 4f'(2) = 4(5) - 4(-3) = 20 + 12 = 32$$
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b02-a-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: transformasi identitas limit trigonometri*

Tentukan nilai dari limit trigonometri berikut:
$$\lim_{x\to 0} \dfrac{x\sin(3x)}{\cos(2x) - \cos(6x)}$$

- **A. $\dfrac{3}{16}$** ✅  
  <sub>Benar: Mengubah selisih kosinus menjadi $2\sin(4x)\sin(2x)$ lalu menerapkan sifat limit dasar trigonometri menghasilkan $\frac{3}{16}$.</sub>
- B. $\dfrac{3}{4}$  
  <sub>Salah: Hanya menghitung rasio koefisien pembilang terhadap salah satu faktor penyebut.</sub>
- C. $-\dfrac{3}{16}$  
  <sub>Salah: Kesalahan tanda negatif pada rumus identitas selisih kosinus.</sub>
- D. $\dfrac{3}{8}$  
  <sub>Salah: Lupa mengalikan faktor 2 dari rumus identitas selisih kosinus.</sub>

**Pembahasan:** 1. Gunakan identitas selisih kosinus: $\cos A - \cos B = -2\sin\left(\frac{A+B}{2}\right)\sin\left(\frac{A-B}{2}\right)$.
Untuk $A = 2x$ dan $B = 6x$:
$$\cos(2x) - \cos(6x) = -2\sin(4x)\sin(-2x) = 2\sin(4x)\sin(2x)$$
2. Substitusikan ke dalam limit:
$$\lim_{x\to 0} \dfrac{x\sin(3x)}{2\sin(4x)\sin(2x)}$$
3. Bagi pembilang dan penyebut dengan $x^2$:
$$= \dfrac{1}{2} \lim_{x\to 0} \left( \dfrac{\sin(3x)}{x} \cdot \dfrac{x}{\sin(4x)} \cdot \dfrac{x}{\sin(2x)} \right)$$
4. Terapkan sifat-sifat limit fungsi trigonometri dasar:
$$= \dfrac{1}{2} \cdot 3 \cdot \dfrac{1}{4} \cdot \dfrac{1}{2} = \dfrac{3}{16}$$
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b02-a-hard-bt01-011
*variasi (angka) | C5 | 4 langkah | jenis: limit fungsi irasional tak tentu*

Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut. Tentukan nilai dari $\displaystyle\lim_{y\to 4}\sqrt{\dfrac{y^3 - 16y}{3y^2 - 10y - 8}}$.

- A. $\dfrac{2}{7}\sqrt{7}$  
  <sub>Salah: Siswa keliru memfaktorkan $y^2 - 16$ menjadi $(y - 4)(y + 2)$ sehingga pembilang bernilai $4(6) = 24$ dan pecahan menjadi $\frac{12}{7}$.</sub>
- B. $\dfrac{16}{7}$  
  <sub>Salah: Siswa sudah benar menghitung limit pecahan di dalam tanda akar tetapi lupa menarik nilai akarnya.</sub>
- **C. $\dfrac{4}{7}\sqrt{7}$** ✅  
  <sub>Benar: Substitusi $y = 4$ menghasilkan bentuk tak tentu $\frac{0}{0}$. Faktorkan pembilang menjadi $y(y - 4)(y + 4)$ dan penyebut menjadi $(3y + 2)(y - 4)$. Setelah membagi faktor $(y - 4)$, diperoleh $\lim_{y\to 4}\frac{y(y + 4)}{3y + 2} = \frac{4(8)}{3(4) + 2} = \frac{32}{14} = \frac{16}{7}$. Menarik akar menghasilkan $\sqrt{\frac{16}{7}} = \frac{4}{\sqrt{7}} = \frac{4}{7}\sqrt{7}$.</sub>
- D. $\dfrac{4}{5}\sqrt{5}$  
  <sub>Salah: Siswa melakukan kesalahan saat memfaktorkan penyebut menjadi $(3y - 2)(y + 4)$ lalu salah menghitung pembagian bentuk sekutu.</sub>

**Pembahasan:** Berdasarkan sifat limit, limit bentuk akar dapat dihitung dengan memasukkan limit ke dalam akar:
$$\lim_{y\to 4}\sqrt{\dfrac{y^3 - 16y}{3y^2 - 10y - 8}} = \sqrt{\lim_{y\to 4}\dfrac{y(y^2 - 16)}{(3y + 2)(y - 4)}}$$
Faktorkan selisih kuadrat pada pembilang:
$$= \sqrt{\lim_{y\to 4}\dfrac{y(y - 4)(y + 4)}{(3y + 2)(y - 4)}}$$
Karena $y \to 4$ dengan $y \neq 4$, bagi pembilang dan penyebut dengan $(y - 4)$:
$$= \sqrt{\lim_{y\to 4}\dfrac{y(y + 4)}{3y + 2}}$$
Terapkan sifat limit substitusi:
$$= \sqrt{\dfrac{4(4 + 4)}{3(4) + 2}} = \sqrt{\dfrac{32}{14}} = \sqrt{\dfrac{16}{7}} = \dfrac{4}{\sqrt{7}} = \dfrac{4}{7}\sqrt{7}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b02-a-hard-bt01-012
*variasi (angka) | C5 | 4 langkah | jenis: limit fungsi trigonometri campuran*

Tentukan nilai dari $\displaystyle\lim_{x\to 0}\dfrac{\tan(9x) - 3\sin(2x)}{4x + \sin(8x)}$.

- A. $\dfrac{1}{2}$  
  <sub>Salah: Siswa salah memperhitungkan faktor $3$ pada $-3\sin(2x)$ menjadi hanya $3$ tanpa dikalikan $2$ sehingga pembilang menjadi $9 - 3 = 6$, menghasilkan $\frac{6}{12} = \frac{1}{2}$.</sub>
- **B. $\dfrac{1}{4}$** ✅  
  <sub>Benar: Membagi pembilang dan penyebut dengan $x$ menghasilkan $\frac{\frac{\tan 9x}{x} - 3\frac{\sin 2x}{x}}{4 + \frac{\sin 8x}{x}}$. Nilai limitnya adalah $\frac{9 - 3(2)}{4 + 8} = \frac{9 - 6}{12} = \frac{3}{12} = \frac{1}{4}$.</sub>
- C. $1$  
  <sub>Salah: Siswa mengabaikan koefisien dan langsung mengambil jawaban acuan asli.</sub>
- D. $\dfrac{5}{4}$  
  <sub>Salah: Siswa salah tanda operasi di pembilang menjadi penjumlahan $9 + 6 = 15$, sehingga menghasilkan $\frac{15}{12} = \frac{5}{4}$.</sub>

**Pembahasan:** Bagi pembilang dan penyebut fungsi dengan $x$:
$$\lim_{x\to 0}\dfrac{\tan(9x) - 3\sin(2x)}{4x + \sin(8x)} = \lim_{x\to 0}\dfrac{\dfrac{\tan(9x)}{x} - 3\cdot\dfrac{\sin(2x)}{x}}{4 + \dfrac{\sin(8x)}{x}}$$
Terapkan sifat dasar limit trigonometri $\lim_{x\to 0}\frac{\sin(kx)}{x} = k$ dan $\lim_{x\to 0}\frac{\tan(kx)}{x} = k$:
$$= \dfrac{9 - 3(2)}{4 + 8} = \dfrac{9 - 6}{12} = \dfrac{3}{12} = \dfrac{1}{4}$$
**Acuan:** siswa — siswa hal.108 Ayo Mencoba 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b02-a-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: keterdiferensiasian fungsi piecewise*

Diberikan fungsi piecewise berikut:
$$f(x) = \begin{cases} ax^2 + bx, & x \le 1 \\ 4\sqrt{x} - 1, & x > 1 \end{cases}$$
Agar fungsi $f(x)$ mempunyai turunan (terdiferensialkan) di titik $x = 1$, tentukan nilai dari $a^2 + b^2$.

- A. $10$  
  <sub>Salah: Siswa salah saat mencari nilai $b$ yaitu $b = 3 - 0 = 3$ dan $a = -1$, sehingga $(-1)^2 + 3^2 = 10$.</sub>
- B. $25$  
  <sub>Salah: Siswa salah menurunkan $4\sqrt{x}$ menjadi $4$, sehingga $2a + b = 4$, yang menghasilkan $a = 1$ dan $b = 2$, lalu menghitung $(1 + 2)^2$ atau salah substitusi.</sub>
- **C. $17$** ✅  
  <sub>Benar: Agar terdiferensialkan di $x = 1$, fungsi harus kontinu dan turunan kiri sama dengan turunan kanan. Syarat kontinu: $a(1)^2 + b(1) = 4\sqrt{1} - 1 \implies a + b = 3$. Syarat keterdiferensiasian: turunan kiri $f'_-(1) = 2a(1) + b = 2a + b$, turunan kanan $f'_+(1) = \frac{4}{2\sqrt{1}} = 2$, sehingga $2a + b = 2$. Dari sistem persamaan didapat $a = -1$ dan $b = 4$. Maka $a^2 + b^2 = (-1)^2 + 4^2 = 1 + 16 = 17$.</sub>
- D. $13$  
  <sub>Salah: Siswa salah menghitung eliminasi sehingga memperoleh $a = -2$ dan $b = 3$, menghasilkan $(-2)^2 + 3^2 = 13$.</sub>

**Pembahasan:** Langkah 1: Syarat kontinu di $x = 1$:
$$\lim_{x\to 1^-} f(x) = \lim_{x\to 1^+} f(x) = f(1)$$
$$a(1)^2 + b(1) = 4\sqrt{1} - 1 \implies a + b = 3 \quad \text{...(Persamaan 1)}$$

Langkah 2: Syarat memiliki turunan di $x = 1$ (turunan kiri sama dengan turunan kanan):
$$f'_-(1) = \lim_{h\to 0^-}\dfrac{f(1+h) - f(1)}{h} = \left. \dfrac{d}{dx}(ax^2 + bx) \right|_{x=1} = 2a(1) + b = 2a + b$$
$$f'_+(1) = \lim_{h\to 0^+}\dfrac{f(1+h) - f(1)}{h} = \left. \dfrac{d}{dx}(4\sqrt{x} - 1) \right|_{x=1} = \dfrac{4}{2\sqrt{1}} = 2$$
$$2a + b = 2 \quad \text{...(Persamaan 2)}$$

Langkah 3: Selesaikan sistem persamaan linear:
$$(2a + b) - (a + b) = 2 - 3 \implies a = -1$$
$$b = 3 - a = 3 - (-1) = 4$$

Langkah 4: Hitung nilai $a^2 + b^2$:
$$a^2 + b^2 = (-1)^2 + 4^2 = 1 + 16 = 17$$
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b02-a-hard-bt01-014
*orisinal | C6 | 5 langkah | jenis: rekonstruksi fungsi dari garis tangen dan sekan*

Suatu fungsi kuadrat $f(x) = px^2 + qx + r$ melalui titik $(1, 2)$ dan $(2, 7)$. Kemiringan garis tangen (garis singgung) kurva tersebut di titik dengan absis $x = 1$ adalah $3$. Kemiringan garis sekan yang menghubungkan titik pada kurva saat $x = 0$ dan $x = 3$ adalah ....

- **A. $5$** ✅  
  <sub>Benar: Melalui $(1, 2) \implies p + q + r = 2$. Melalui $(2, 7) \implies 4p + 2q + r = 7$. Garis tangen di $x = 1$ bernilai $f'(1) = 2p + q = 3$. Dari eliminasi didapatkan $3p + q = 5$, sehingga $p = 2$, $q = -1$, dan $r = 1$. Fungsi kuadrat adalah $f(x) = 2x^2 - x + 1$. Maka $f(0) = 1$ dan $f(3) = 2(9) - 3 + 1 = 16$. Kemiringan garis sekan $m = \frac{f(3) - f(0)}{3 - 0} = \frac{16 - 1}{3} = 5$.</sub>
- B. $3$  
  <sub>Salah: Siswa menyamakan kemiringan garis sekan dengan kemiringan garis tangen di $x = 1$.</sub>
- C. $4$  
  <sub>Salah: Siswa salah menghitung selisih koordinat dengan memakai interval $x = 1$ ke $x = 3$ sehingga memperoleh $\frac{16 - 2}{3 - 1} = 7$ lalu salah membagi.</sub>
- D. $6$  
  <sub>Salah: Siswa salah menentukan nilai $r = 0$ sehingga $f(0) = 0$ dan menghitung $\frac{18 - 0}{3} = 6$.</sub>

**Pembahasan:** Langkah 1: Bentuk sistem persamaan dari informasi yang diketahui:
- Melalui titik $(1, 2)$: $p(1)^2 + q(1) + r = 2 \implies p + q + r = 2$ ...(i)
- Melalui titik $(2, 7)$: $p(2)^2 + q(2) + r = 7 \implies 4p + 2q + r = 7$ ...(ii)
- Kemiringan garis tangen di $x = 1$ adalah $f'(1) = 3$:
$$f'(x) = \lim_{h\to 0}\dfrac{f(x+h)-f(x)}{h} = 2px + q \implies 2p(1) + q = 3 \implies 2p + q = 3 \quad \text{...(iii)}$$

Langkah 2: Eliminasi persamaan (ii) dan (i):
$$(4p + 2q + r) - (p + q + r) = 7 - 2 \implies 3p + q = 5 \quad \text{...(iv)}$$

Langkah 3: Tentukan nilai parameter $p, q, r$:
Kurangkan (iv) dengan (iii):
$$(3p + q) - (2p + q) = 5 - 3 \implies p = 2$$
Substitusikan $p = 2$ ke (iii):
$$2(2) + q = 3 \implies q = -1$$
Substitusikan ke (i):
$$2 + (-1) + r = 2 \implies r = 1$$
Sehingga rumus fungsi adalah $f(x) = 2x^2 - x + 1$.

Langkah 4: Hitung nilai fungsi pada titik-titik garis sekan:
$$f(0) = 2(0)^2 - (0) + 1 = 1$$
$$f(3) = 2(3)^2 - 3 + 1 = 18 - 3 + 1 = 16$$

Langkah 5: Tentukan kemiringan garis sekan:
$$m_{\text{sekan}} = \dfrac{f(3) - f(0)}{3 - 0} = \dfrac{16 - 1}{3} = \dfrac{15}{3} = 5$$
**Acuan:** siswa — siswa hal.117

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b02-a-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: limit kombinasi bentuk akar dan trigonometri*

Tentukan nilai dari limit kombinasi aljabar dan trigonometri berikut:
$$\lim_{x\to 0} \dfrac{x\left(\sqrt{9 + 4x} - 3\right)}{1 - \cos(2x)}$$

- A. $\dfrac{2}{3}$  
  <sub>Salah: Siswa lupa faktor 2 pada rumus identitas trigonometri $1 - \cos(2x) = 2\sin^2 x$ dan menganggapnya hanya $\sin^2 x$.</sub>
- B. $\dfrac{1}{6}$  
  <sub>Salah: Siswa salah menghitung koefisien pada pembilang menjadi $2x^2$ alih-alih $4x^2$.</sub>
- C. $\dfrac{4}{3}$  
  <sub>Salah: Siswa salah saat menyederhanakan pecahan di penyebut akar sehingga mendapat nilai akhir terbalik.</sub>
- **D. $\dfrac{1}{3}$** ✅  
  <sub>Benar: Rasionalkan pembilang dengan mengalikan sekawan $\sqrt{9 + 4x} + 3$, menghasilkan $\frac{x(9 + 4x - 9)}{\sqrt{9 + 4x} + 3} = \frac{4x^2}{\sqrt{9 + 4x} + 3}$. Ubah penyebut menggunakan identitas $1 - \cos(2x) = 2\sin^2 x$. Limit menjadi $\lim_{x\to 0} \left[ \frac{4x^2}{2\sin^2 x} \cdot \frac{1}{\sqrt{9 + 4x} + 3} \right] = 2 \cdot 1 \cdot \frac{1}{6} = \frac{1}{3}$.</sub>

**Pembahasan:** Langkah 1: Kalikan pembilang dan penyebut dengan bentuk sekawan dari $(\sqrt{9 + 4x} - 3)$:
$$\lim_{x\to 0} \dfrac{x\left(\sqrt{9 + 4x} - 3\right)}{1 - \cos(2x)} \cdot \dfrac{\sqrt{9 + 4x} + 3}{\sqrt{9 + 4x} + 3}$$

Langkah 2: Sederhanakan hasil perkalian sekawan pada pembilang:
$$x\left((9 + 4x) - 9\right) = x(4x) = 4x^2$$

Langkah 3: Gunakan identitas trigonometri untuk penyebut:
$$1 - \cos(2x) = 2\sin^2 x$$

Langkah 4: Tuliskan kembali bentuk limit secara terpisah:
$$\lim_{x\to 0} \left( \dfrac{4x^2}{2\sin^2 x} \cdot \dfrac{1}{\sqrt{9 + 4x} + 3} \right)$$

Langkah 5: Hitung nilai masing-masing limit:
$$= 2 \cdot \left(\lim_{x\to 0} \dfrac{x}{\sin x}\right)^2 \cdot \left(\lim_{x\to 0} \dfrac{1}{\sqrt{9 + 4x} + 3}\right)$$
$$= 2 \cdot (1)^2 \cdot \dfrac{1}{\sqrt{9 + 0} + 3} = 2 \cdot \dfrac{1}{3 + 3} = \dfrac{2}{6} = \dfrac{1}{3}$$
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b02-a-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: kekontinuan fungsi trigonometri parametrik*

Diberikan fungsi $f(x)$ sebagai berikut:
$$f(x) = \begin{cases} \dfrac{1 - \cos(kx)}{x^2}, & x < 0 \\ m + 1, & x = 0 \\ \dfrac{\tan(6x)}{\sin(2x)}, & x > 0 \end{cases}$$
Jika fungsi $f(x)$ kontinu di $x = 0$ dan $k > 0$, nilai dari $k^2 - 2m$ adalah ....

- **A. $2$** ✅  
  <sub>Benar: Agar kontinu di $x = 0$, harus dipenuhi $\lim_{x\to 0^-} f(x) = f(0) = \lim_{x\to 0^+} f(x)$. Limit kanan bernilai $\lim_{x\to 0^+} \frac{\tan(6x)}{\sin(2x)} = \frac{6}{2} = 3$. Nilai $f(0) = m + 1 = 3 \implies m = 2$. Limit kiri bernilai $\lim_{x\to 0^-} \frac{1 - \cos(kx)}{x^2} = \frac{k^2}{2} = 3 \implies k^2 = 6$. Maka nilai $k^2 - 2m = 6 - 2(2) = 2$.</sub>
- B. $10$  
  <sub>Salah: Siswa salah menjumlahkan operasi akhir menjadi $k^2 + 2m = 6 + 4 = 10$.</sub>
- C. $0$  
  <sub>Salah: Siswa salah saat menentukan nilai $m$ dari $m + 1 = 3$ menjadi $m = 3$, sehingga menghasilkan $6 - 2(3) = 0$.</sub>
- D. $-1$  
  <sub>Salah: Siswa lupa faktor $\frac{1}{2}$ pada bentuk limit $1 - \cos(kx)$ sehingga memperoleh $k^2 = 3$ dan menghitung $3 - 4 = -1$.</sub>

**Pembahasan:** Berdasarkan Definisi 2.2, syarat suatu fungsi kontinu di titik $x = 0$ adalah:
$$\lim_{x\to 0^-} f(x) = f(0) = \lim_{x\to 0^+} f(x)$$

1. Hitung limit dari arah kanan:
$$\lim_{x\to 0^+} f(x) = \lim_{x\to 0^+} \dfrac{\tan(6x)}{\sin(2x)} = \dfrac{6}{2} = 3$$

2. Tentukan nilai $m$ dari $f(0)$:
$$f(0) = m + 1 = 3 \implies m = 2$$

3. Hitung limit dari arah kiri dan tentukan $k^2$:
$$\lim_{x\to 0^-} f(x) = \lim_{x\to 0^-} \dfrac{1 - \cos(kx)}{x^2} = \lim_{x\to 0^-} \dfrac{2\sin^2\left(\frac{kx}{2}\right)}{x^2} = 2 \cdot \left(\dfrac{k}{2}\right)^2 = \dfrac{k^2}{2}$$
Karena fungsi kontinu, maka:
$$\dfrac{k^2}{2} = 3 \implies k^2 = 6$$

4. Hitung nilai $k^2 - 2m$:
$$k^2 - 2m = 6 - 2(2) = 6 - 4 = 2$$
**Acuan:** siswa — siswa hal.112

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b02-a-hard-bt01-017
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi limit perkalian bentuk tak tentu*

Diketahui $\displaystyle\lim_{x\to 5} g(x) = 10$. Tentukan nilai dari $$\lim_{x\to 5}\left(g(x)\cdot\dfrac{x-5}{\sqrt{x+4}-3}\right)$$

- A. $0$  
  <sub>Salah: Siswa langsung menyubstitusi $x = 5$ ke pembilang $(5 - 5 = 0)$ tanpa merasionalkan bentuk tak tentu penyebut.</sub>
- B. $30$  
  <sub>Salah: Siswa lupa menjumlahkan suku konstan pada akar sekawan, hanya menghitung nilai akarnya saja $\sqrt{5+4}=3$, sehingga memperoleh $10 \times 3 = 30$.</sub>
- **C. $60$** ✅  
  <sub>Benar: Menerapkan sifat limit perkalian: $\lim_{x\to 5} g(x) \cdot \lim_{x\to 5} \frac{x-5}{\sqrt{x+4}-3}$. Pada suku kedua, bentuk tak tentu $\frac{0}{0}$ diselesaikan dengan mengalikan sekawan $(\sqrt{x+4}+3)$, menghasilkan $\frac{(x-5)(\sqrt{x+4}+3)}{(x+4)-9} = \sqrt{x+4}+3$. Nilai limit suku kedua saat $x \to 5$ adalah $\sqrt{9}+3 = 6$. Nilai akhir adalah $10 \times 6 = 60$.</sub>
- D. $\dfrac{5}{3}$  
  <sub>Salah: Siswa membalik operasi penyederhanaan sekawan menjadi penyebut bernilai $6$, menghasilkan $\frac{10}{6} = \frac{5}{3}$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat perkalian limit:
$$\lim_{x\to 5}\left(g(x)\cdot\dfrac{x-5}{\sqrt{x+4}-3}\right) = \left(\lim_{x\to 5} g(x)\right) \cdot \left(\lim_{x\to 5}\dfrac{x-5}{\sqrt{x+4}-3}\right)$$

Langkah 2: Diketahui $\lim_{x\to 5} g(x) = 10$. Evaluasi bagian limit kedua:
Substitusi $x = 5$ memberikan $\frac{5-5}{\sqrt{9}-3} = \frac{0}{0}$ (bentuk tak tentu).

Langkah 3: Rasionalkan penyebut dengan mengalikan bentuk sekawan $\dfrac{\sqrt{x+4}+3}{\sqrt{x+4}+3}$:
$$\lim_{x\to 5}\dfrac{x-5}{\sqrt{x+4}-3} = \lim_{x\to 5}\dfrac{(x-5)(\sqrt{x+4}+3)}{(\sqrt{x+4})^2 - 3^2}$$
$$= \lim_{x\to 5}\dfrac{(x-5)(\sqrt{x+4}+3)}{(x+4)-9}$$
$$= \lim_{x\to 5}\dfrac{(x-5)(\sqrt{x+4}+3)}{x-5}$$

Langkah 4: Eliminasi faktor pembuat nol $(x-5)$ untuk $x \neq 5$:
$$= \lim_{x\to 5} (\sqrt{x+4}+3)$$
Substitusikan $x = 5$:
$$= \sqrt{5+4} + 3 = \sqrt{9} + 3 = 3 + 3 = 6$$

Langkah 5: Kalikan kedua hasil limit sesuai sifat perkalian:
$$\text{Nilai limit} = 10 \cdot 6 = 60$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b02-a-hard-bt01-018
*variasi (angka) | C5 | 4 langkah | jenis: limit trigonometri manipulasi aljabar*

Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut. Tentukan nilai dari:
$$\lim_{x\to \frac{\pi}{3}}\left(\dfrac{4\sin x - 4\sqrt{3}\cos x}{5\sqrt{3} - 5\tan x}\right)$$

- A. $-\dfrac{2}{5}\sqrt{3}$  
  <sub>Salah: Tertukar mensubstitusikan nilai $\sin\left(\frac{\pi}{3}\right) = \frac{1}{2}\sqrt{3}$ ke dalam bentuk $-\frac{4}{5}\cos x$.</sub>
- B. $-\dfrac{4}{5}$  
  <sub>Salah: Keliru menganggap $\cos\left(\frac{\pi}{3}\right) = 1$ setelah menyederhanakan bentuk pecahan.</sub>
- C. $\dfrac{2}{5}$  
  <sub>Salah: Kesalahan tanda akibat mengabaikan faktor negatif saat menyederhanakan $\frac{\sin x - \sqrt{3}\cos x}{\sqrt{3}\cos x - \sin x} = -1$.</sub>
- **D. $-\dfrac{2}{5}$** ✅  
  <sub>Benar: Mengubah $\tan x$ menjadi $\frac{\sin x}{\cos x}$, menyamakan penyebut sehingga diperoleh $\frac{4(\sin x - \sqrt{3}\cos x)}{-5(\sin x - \sqrt{3}\cos x)/\cos x} = -\frac{4}{5}\cos x$. Nilai limit saat $x \to \frac{\pi}{3}$ adalah $-\frac{4}{5}\cos\left(\frac{\pi}{3}\right) = -\frac{4}{5}\left(\frac{1}{2}\right) = -\frac{2}{5}$.</sub>

**Pembahasan:** Substitusi langsung $x = \frac{\pi}{3}$ menghasilkan bentuk tak tentu $\frac{0}{0}$:
$$\lim_{x\to \frac{\pi}{3}}\left(\dfrac{4\sin x - 4\sqrt{3}\cos x}{5\sqrt{3} - 5\tan x}\right)$$

Faktorkan koefisien dari pembilang dan ubah bentuk tangen pada penyebut:
$$= \lim_{x\to \frac{\pi}{3}}\left(\dfrac{4(\sin x - \sqrt{3}\cos x)}{5\left(\sqrt{3} - \dfrac{\sin x}{\cos x}\right)}\right)$$
$$= \lim_{x\to \frac{\pi}{3}}\left(\dfrac{4(\sin x - \sqrt{3}\cos x)}{5\left(\dfrac{\sqrt{3}\cos x - \sin x}{\cos x}\right)}\right)$$
$$= \lim_{x\to \frac{\pi}{3}}\left(\dfrac{4(\sin x - \sqrt{3}\cos x) \cdot \cos x}{-5(\sin x - \sqrt{3}\cos x)}\right)$$

Bagi pembilang dan penyebut dengan faktor sekutu $(\sin x - \sqrt{3}\cos x) \neq 0$:
$$= \lim_{x\to \frac{\pi}{3}}\left(-\dfrac{4}{5}\cos x\right)$$
$$= -\dfrac{4}{5}\cos\left(\dfrac{\pi}{3}\right) = -\dfrac{4}{5} \cdot \dfrac{1}{2} = -\dfrac{2}{5}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b02-a-hard-bt01-019
*variasi (angka) | C5 | 5 langkah | jenis: limit bentuk akar sekawan*

Gunakanlah sifat-sifat limit untuk menyelesaikan masalah berikut. Tentukan nilai dari:
$$\lim_{x\to 3}\dfrac{\sqrt{3x + 16} - 5}{x^2 - 2x - 3}$$

- **A. $\dfrac{3}{40}$** ✅  
  <sub>Benar: Substitusi $x = 3$ menghasilkan bentuk $\frac{0}{0}$. Kalikan pembilang dan penyebut dengan sekawan $(\sqrt{3x+16}+5)$ menghasilkan $\frac{3x - 9}{(x-3)(x+1)(\sqrt{3x+16}+5)} = \frac{3(x-3)}{(x-3)(x+1)(\sqrt{3x+16}+5)} = \frac{3}{(x+1)(\sqrt{3x+16}+5)}$. Evaluasi limit untuk $x\to 3$ menghasilkan $\frac{3}{(4)(10)} = \frac{3}{40}$.</sub>
- B. $\dfrac{3}{4}$  
  <sub>Salah: Siswa lupa mengalikan bentuk sekawan pada penyebut dan hanya membagi $(3x-9)$ dengan $(x^2-2x-3)$.</sub>
- C. $\dfrac{3}{20}$  
  <sub>Salah: Siswa salah memfaktorkan penyebut menjadi $(x - 3)(x - 1)$, sehingga penyebut bernilai $(2)(10) = 20$.</sub>
- D. $\dfrac{1}{40}$  
  <sub>Salah: Siswa lupa memfaktorkan koefisien 3 dari $(3x - 9)$, menganggap pembilang setelah disederhanakan bernilai 1.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Substitusi langsung $x = 3$:
   $$\dfrac{\sqrt{3(3) + 16} - 5}{3^2 - 2(3) - 3} = \dfrac{5 - 5}{9 - 6 - 3} = \dfrac{0}{0}\quad \text{(bentuk tak tentu)}$$
2. Kalikan pembilang dan penyebut dengan bentuk sekawan dari pembilang, yaitu $(\sqrt{3x+16} + 5)$:
   $$\lim_{x\to 3}\dfrac{(\sqrt{3x + 16} - 5)(\sqrt{3x + 16} + 5)}{(x^2 - 2x - 3)(\sqrt{3x + 16} + 5)}$$
3. Sederhanakan bentuk pembilang dan faktorkan penyebut:
   Pembilang: $(\sqrt{3x + 16})^2 - 5^2 = 3x + 16 - 25 = 3x - 9 = 3(x - 3)$
   Penyebut: $x^2 - 2x - 3 = (x - 3)(x + 1)$
4. Bentuk limit menjadi:
   $$\lim_{x\to 3}\dfrac{3(x - 3)}{(x - 3)(x + 1)(\sqrt{3x + 16} + 5)}$$
5. Karena $x \to 3$ maka $x \neq 3$, sehingga faktor $(x - 3)$ dapat saling membagi:
   $$= \lim_{x\to 3}\dfrac{3}{(x + 1)(\sqrt{3x + 16} + 5)}$$
   $$= \dfrac{3}{(3 + 1)(\sqrt{3(3) + 16} + 5)} = \dfrac{3}{4 \cdot (5 + 5)} = \dfrac{3}{40}$$
**Acuan:** pretest — kelas12_tl-b02-p0118-latihan-soal-definisi-turunan-fungsi-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b02-a-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: aplikasi laju perubahan rata-rata dan sesaat*

Sebuah pabrik memproduksi sepatu dengan kurva total produksi $N(t) = at^2 + bt$ pasang sepatu setelah $t$ jam kerja ($0 \le t \le 8$). Rata-rata laju produksi sepatu dari jam ke-1 hingga jam ke-3 ($t = 1$ sampai $t = 3$) adalah $48$ pasang per jam. Sementara itu, laju produksi sesaat pada jam ke-4 ($t = 4$) yang dihitung melalui limit pergerakan garis tangen $\displaystyle\lim_{h\to 0}\dfrac{N(4+h)-N(4)}{h}$ adalah $68$ pasang per jam. Nilai dari $a + b$ adalah ....

- A. $23$  
  <sub>Salah: Siswa menghitung nilai selisih $b - a = 28 - 5 = 23$, bukan penjumlahan $a + b$.</sub>
- **B. $33$** ✅  
  <sub>Benar: Rata-rata laju produksi $\frac{N(3)-N(1)}{3-1} = \frac{(9a+3b)-(a+b)}{2} = 4a + b = 48$. Laju produksi sesaat pada $t = 4$ adalah $N'(4) = 8a + b = 68$. Mengeliminasi kedua persamaan menghasilkan $4a = 20 \implies a = 5$, sehingga $b = 48 - 4(5) = 28$. Nilai $a + b = 5 + 28 = 33$.</sub>
- C. $41$  
  <sub>Salah: Siswa salah menurunkan $N(t)$ dengan mengabaikan pangkat 2 sehingga menganggap $N'(4) = a + b = 68$, lalu salah mengurangkan.</sub>
- D. $25$  
  <sub>Salah: Siswa membagi selisih total produksi pada laju rata-rata dengan 3 (bukan selang waktu $\Delta t = 3 - 1 = 2$).</sub>

**Pembahasan:** Langkah penyelesaian:
1. Tentukan laju perubahan rata-rata produksi sepatu pada selang $t = 1$ hingga $t = 3$:
   $$m_{\text{sekan}} = \dfrac{N(3) - N(1)}{3 - 1}$$
   $$N(3) = a(3)^2 + b(3) = 9a + 3b$$
   $$N(1) = a(1)^2 + b(1) = a + b$$
   $$m_{\text{sekan}} = \dfrac{(9a + 3b) - (a + b)}{2} = \dfrac{8a + 2b}{2} = 4a + b$$
   Diketahui rata-rata laju produksi adalah 48 pasang/jam, maka diperoleh persamaan (1):
   $$4a + b = 48$$

2. Tentukan laju perubahan sesaat pada $t = 4$ menggunakan definisi limit:
   $$N'(4) = \lim_{h\to 0}\dfrac{N(4+h) - N(4)}{h}$$
   $$N(4+h) = a(4+h)^2 + b(4+h) = a(16 + 8h + h^2) + 4b + bh$$
   $$N(4) = 16a + 4b$$
   $$N(4+h) - N(4) = 8ah + ah^2 + bh = h(8a + b + ah)$$
   $$N'(4) = \lim_{h\to 0}\dfrac{h(8a + b + ah)}{h} = \lim_{h\to 0}(8a + b + ah) = 8a + b$$
   Diketahui laju produksi sesaat pada $t = 4$ adalah 68 pasang/jam, maka diperoleh persamaan (2):
   $$8a + b = 68$$

3. Eliminasi $b$ dari persamaan (2) dan persamaan (1):
   $$(8a + b) - (4a + b) = 68 - 48$$
   $$4a = 20 \implies a = 5$$

4. Substitusikan $a = 5$ ke persamaan (1):
   $$4(5) + b = 48 \implies 20 + b = 48 \implies b = 28$$

5. Hitung nilai $a + b$:
   $$a + b = 5 + 28 = 33$$
**Acuan:** siswa — siswa hal.115

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
