# Lembar koreksi — kelas12_tl SMA12L-B1 subbab B: Elips

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b01-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips vertikal pusat O(0,0)*  **[warning validator]**

Suatu elips memiliki titik pusat $O(0,0)$. Salah satu fokusnya terletak pada titik $(0,6)$ dan panjang sumbu mayornya adalah 20. Persamaan elips tersebut adalah ....

- A. $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$  
  <sub>Salah: Tertukar antara bentuk elips horizontal dan vertikal ($a^2$ ditaruh di bawah $x^2$).</sub>
- **B. $\dfrac{x^2}{64} + \dfrac{y^2}{100} = 1$** ✅  
  <sub>Benar: Fokus di sumbu-$y$ $((0,6))$ menunjukkan elips vertikal dengan $c = 6$. Panjang sumbu mayor $2a = 20 \iff a = 10$. Nilai $b^2 = a^2 - c^2 = 10^2 - 6^2 = 100 - 36 = 64$. Bentuk baku elips vertikal berpusat di $(0,0)$ adalah $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$, sehingga persamaannya $\frac{x^2}{64} + \frac{y^2}{100} = 1$.</sub>
- C. $\dfrac{x^2}{64} + \dfrac{y^2}{400} = 1$  
  <sub>Salah: Menganggap panjang sumbu mayor 20 sebagai nilai $a$, sehingga $a^2 = 400$.</sub>
- D. $\dfrac{x^2}{36} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Salah memasukkan nilai $c^2 = 36$ sebagai penyebut $x^2$ alih-alih menghitung $b^2$.</sub>

**Pembahasan:** Dari letak fokus di $(0,6)$, elips berbentuk vertikal dengan titik pusat di $(0,0)$ dan $c = 6$.
Panjang sumbu mayor $= 2a = 20 \implies a = 10$.
Menghitung $b^2$:
$$b^2 = a^2 - c^2 = 10^2 - 6^2 = 100 - 36 = 64$$
Persamaan umum elips vertikal berpusat di $(0,0)$:
$$\dfrac{x^2}{b^2} + \dfrac{y^2}{a^2} = 1 \iff \dfrac{x^2}{64} + \dfrac{y^2}{100} = 1$$
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-5
**Warning:** kelas12_tl-b01-b-easy-bt01-001 sangat mirip dengan kelas12_tl-b01-b-medium-bt01-007 [exercise:batch01/B_medium.json] (0.89)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b01-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips horizontal dari titik fokus*

Persamaan elips dengan titik pusat $O(0,0)$, titik-titik fokus $(6,0)$ dan $(-6,0)$, serta panjang sumbu mayor 16 adalah ....

- **A. $\dfrac{x^2}{64} + \dfrac{y^2}{28} = 1$** ✅  
  <sub>Benar: Fokus pada sumbu-$x$ menunjukkan elips horizontal dengan $c = 6$. Panjang sumbu mayor $2a = 16 \iff a = 8$. Maka $b^2 = a^2 - c^2 = 8^2 - 6^2 = 64 - 36 = 28$. Persamaan elips: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \iff \frac{x^2}{64} + \frac{y^2}{28} = 1$.</sub>
- B. $\dfrac{x^2}{64} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Salah rumus dengan menjumlahkan $a^2 + c^2$ untuk mencari $b^2$ alih-alih mengurangkan.</sub>
- C. $\dfrac{x^2}{64} + \dfrac{y^2}{36} = 1$  
  <sub>Salah: Menggunakan nilai $c^2 = 36$ sebagai penyebut $y^2$ alih-alih $b^2$.</sub>
- D. $\dfrac{x^2}{28} + \dfrac{y^2}{64} = 1$  
  <sub>Salah: Tertukar antara $a^2$ dan $b^2$ pada persamaan elips horizontal.</sub>

**Pembahasan:** Fokus terletak pada $(\pm 6, 0)$ yang berada pada sumbu-$x$, sehingga elips berbentuk horizontal dengan $c = 6$.
Panjang sumbu mayor $= 2a = 16 \implies a = 8$.
Menghitung $b^2$:
$$b^2 = a^2 - c^2 = 8^2 - 6^2 = 64 - 36 = 28$$
Bentuk baku elips horizontal:
$$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 \iff \dfrac{x^2}{64} + \dfrac{y^2}{28} = 1$$
**Acuan:** siswa — siswa hal.43 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b01-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips dari eksentrisitas*

Persamaan elips horizontal yang berpusat pada titik $O(0,0)$ dengan nilai eksentrisitas $\frac{3}{5}$ dan jarak kedua fokusnya 12 adalah ....

- **A. $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$** ✅  
  <sub>Benar: Jarak antarfokus $2c = 12 \iff c = 6$. Eksentrisitas $e = \frac{c}{a} = \frac{3}{5} \iff \frac{6}{a} = \frac{3}{5} \iff a = 10$. Nilai $b^2 = a^2 - c^2 = 10^2 - 6^2 = 100 - 36 = 64$. Persamaan elips: $\frac{x^2}{100} + \frac{y^2}{64} = 1$.</sub>
- B. $\dfrac{x^2}{64} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Keliru menggunakan persamaan elips vertikal untuk elips yang didefinisikan horizontal.</sub>
- C. $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$  
  <sub>Salah: Menggunakan nilai perbandingan eksentrisitas ($a=5, c=3$) tanpa mengalikan skala jarak fokus sebenarnya.</sub>
- D. $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$  
  <sub>Salah: Memakai $c^2 = 36$ langsung pada penyebut variabel $y^2$.</sub>

**Pembahasan:** Jarak kedua fokus $= 2c = 12 \implies c = 6$.
Eksentrisitas $e = \dfrac{c}{a} = \dfrac{3}{5}$:
$$\dfrac{6}{a} = \dfrac{3}{5} \implies a = \dfrac{6 \times 5}{3} = 10$$
Mencari $b^2$:
$$b^2 = a^2 - c^2 = 10^2 - 6^2 = 100 - 36 = 64$$
Karena elips horizontal dengan pusat $(0,0)$, persamaannya adalah:
$$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 \iff \dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$$
**Acuan:** siswa — siswa hal.50 Ayo Mencoba 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b01-b-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: menentukan panjang sumbu elips*

Panjang sumbu minor dari elips dengan persamaan $\dfrac{x^2}{81} + \dfrac{y^2}{36} = 1$ adalah ....

- A. 36  
  <sub>Salah: Mengambil nilai penyebut $b^2$ langsung sebagai panjang sumbu minor.</sub>
- **B. 12** ✅  
  <sub>Benar: Pada elips $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ dengan $a^2 = 81$ dan $b^2 = 36$, diperoleh $b = \sqrt{36} = 6$. Panjang sumbu minor adalah $2b = 2 \times 6 = 12$.</sub>
- C. 6  
  <sub>Salah: Hanya menghitung nilai $b$ tanpa mengalikan dua untuk panjang sumbu minor.</sub>
- D. 18  
  <sub>Salah: Menghitung panjang sumbu mayor ($2a = 2 \times 9 = 18$) alih-alih sumbu minor.</sub>

**Pembahasan:** Berdasarkan persamaan baku $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$:
$a^2 = 81 \implies a = 9$
$b^2 = 36 \implies b = 6$
Panjang sumbu minor $= 2b = 2(6) = 12$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b01-b-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: menentukan koordinat fokus elips*

Koordinat titik-titik fokus dari elips $\dfrac{x^2}{169} + \dfrac{y^2}{25} = 1$ adalah ....

- A. $(13,0)$ dan $(-13,0)$  
  <sub>Salah: Mengira koordinat puncak $(a,0)$ sebagai koordinat fokus.</sub>
- B. $(0,12)$ dan $(0,-12)$  
  <sub>Salah: Menganggap elips vertikal sehingga meletakkan fokus pada sumbu-$y$.</sub>
- C. $(5,0)$ dan $(-5,0)$  
  <sub>Salah: Menggunakan nilai $b = 5$ sebagai koordinat fokus.</sub>
- **D. $(12,0)$ dan $(-12,0)$** ✅  
  <sub>Benar: Karena penyebut $x^2$ lebih besar ($a^2 = 169 > b^2 = 25$), elips horizontal. Nilai $c = \sqrt{a^2 - b^2} = \sqrt{169 - 25} = \sqrt{144} = 12$. Koordinat fokus adalah $(\pm c, 0) = (12,0)$ dan $(-12,0)$.</sub>

**Pembahasan:** Dari persamaan $\dfrac{x^2}{169} + \dfrac{y^2}{25} = 1$:
$a^2 = 169$ dan $b^2 = 25$.
Karena $a^2$ berada di bawah $x^2$, sumbu utama terletak pada sumbu-$x$ (elips horizontal).
Menghitung jarak fokus $c$:
$$c^2 = a^2 - b^2 = 169 - 25 = 144 \implies c = 12$$
Jadi, koordinat kedua titik fokusnya adalah $(12,0)$ dan $(-12,0)$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b01-b-easy-bt01-006
*variasi (angka) | C1 | 1 langkah | jenis: menentukan titik puncak elips*

Koordinat titik-titik puncak pada sumbu mayor dari elips $\dfrac{x^2}{64} + \dfrac{y^2}{49} = 1$ adalah ....

- A. $(0,8)$ dan $(0,-8)$  
  <sub>Salah: Tertukar letak sumbu mayor pada sumbu-y alih-alih sumbu-x.</sub>
- B. $(64,0)$ dan $(-64,0)$  
  <sub>Salah: Lupa menarik akar kuadrat dari $a^2=64$.</sub>
- **C. $(8,0)$ dan $(-8,0)$** ✅  
  <sub>Benar: Pada elips horizontal $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$, karena $64 > 49$, diperoleh $a^2=64$ sehingga $a=8$. Puncak pada sumbu mayor terletak di $(a,0)$ dan $(-a,0)$, yaitu $(8,0)$ dan $(-8,0)$.</sub>
- D. $(7,0)$ dan $(-7,0)$  
  <sub>Salah: Menggunakan nilai b dari sumbu minor sebagai puncak sumbu mayor.</sub>

**Pembahasan:** Bentuk umum elips dengan pusat $(0,0)$ adalah $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$. Karena penyebut $x^2$ bernilai $64$ dan penyebut $y^2$ bernilai $49$, maka $a^2 = 64$ dan $b^2 = 49$. Dengan demikian, elips ini merupakan elips horizontal dengan $a = 8$. Titik puncak pada sumbu mayor adalah $(a, 0)$ dan $(-a, 0)$, yaitu $(8,0)$ dan $(-8,0)$.
**Acuan:** pretest — kelas12_tl-b01-p0052-latihan-soal-elips-1d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b01-b-easy-bt01-007
*orisinal | C1 | 1 langkah | jenis: konsep definisi elips*

Titik $P(x,y)$ terletak pada suatu elips dengan titik fokus $F_1$ dan $F_2$. Jika panjang sumbu mayor elips tersebut adalah 18, nilai dari penjumlahan jarak $PF_1 + PF_2$ adalah ....

- A. 81  
  <sub>Salah: Mengkuadratkan nilai setengah sumbu mayor ($a^2 = 9^2 = 81$).</sub>
- B. 9  
  <sub>Salah: Mengira jumlah jarak sama dengan nilai semimayor a alih-alih 2a.</sub>
- C. 36  
  <sub>Salah: Mengalikan panjang sumbu mayor dengan 2.</sub>
- **D. 18** ✅  
  <sub>Benar: Berdasarkan definisi elips, jumlah jarak titik sebarang pada elips terhadap kedua titik fokusnya selalu tetap dan bernilai sama dengan panjang sumbu mayor ($2a$), yaitu 18.</sub>

**Pembahasan:** Berdasarkan definisi elips, elips adalah kumpulan titik-titik pada bidang datar yang jumlah jaraknya terhadap dua titik tertentu (titik fokus $F_1$ dan $F_2$) selalu tetap. Nilai penjumlahan jarak tersebut sama dengan panjang sumbu mayor elips, yaitu $2a$. Karena diketahui panjang sumbu mayor elips adalah 18, maka $PF_1 + PF_2 = 2a = 18$.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b01-b-easy-bt01-008
*variasi (angka) | C2 | 1 langkah | jenis: menentukan titik puncak sumbu minor*

Koordinat titik-titik puncak elips $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$ yang terletak pada sumbu minor adalah ....

- A. $(10, 0)$ dan $(-10, 0)$  
  <sub>Salah: Menghitung titik puncak pada sumbu mayor, bukan sumbu minor.</sub>
- **B. $(0, 6)$ dan $(0, -6)$** ✅  
  <sub>Benar: Bentuk baku elips horizontal $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ memiliki $a^2 = 100$ dan $b^2 = 36$. Sumbu minor berada pada sumbu-$y$ dengan puncak $(0, \pm b) = (0, \pm 6)$.</sub>
- C. $(6, 0)$ dan $(-6, 0)$  
  <sub>Salah: Tertukar meletakkan nilai b pada sumbu-x.</sub>
- D. $(0, 10)$ dan $(0, -10)$  
  <sub>Salah: Tertukar menganggap nilai a berada pada sumbu-y.</sub>

**Pembahasan:** Persamaan elips $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$ memiliki titik pusat $O(0,0)$ dengan $a^2 = 100$ dan $b^2 = 36$. Karena $a^2 > b^2$, elips merupakan elips horizontal. Puncak-puncak pada sumbu minor terletak pada sumbu-$y$, yaitu di titik $(0, b)$ dan $(0, -b)$. Dengan $b = \sqrt{36} = 6$, koordinat puncaknya adalah $(0, 6)$ dan $(0, -6)$.
**Acuan:** pretest — kelas12_tl-b01-p0052-latihan-soal-elips-1d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b01-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips dari fokus dan sumbu mayor*

Persamaan elips dengan titik pusat $O(0,0)$, titik-titik fokus $(8,0)$ dan $(-8,0)$, serta panjang sumbu mayor $20$ adalah ....

- A. $\dfrac{x^2}{400} + \dfrac{y^2}{64} = 1$  
  <sub>Salah: Memasukkan 2a dan c langsung sebagai a dan b ke persamaan.</sub>
- **B. $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$** ✅  
  <sub>Benar: Fokus pada sumbu-$x$ menunjukkan elips horizontal dengan $c = 8$. Panjang sumbu mayor $2a = 20 \implies a = 10$. Nilai $b^2 = a^2 - c^2 = 100 - 64 = 36$, sehingga persamaannya $\frac{x^2}{100} + \frac{y^2}{36} = 1$.</sub>
- C. $\dfrac{x^2}{36} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Tertukar antara penyebut variabel x dan y (tertukar menjadi elips vertikal).</sub>
- D. $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$  
  <sub>Salah: Menggunakan nilai c^2 = 64 sebagai b^2 tanpa menghitung b^2 = a^2 - c^2.</sub>

**Pembahasan:** Dari fokus $(\pm 8, 0)$, diketahui elips horizontal berpusat di $(0,0)$ dengan $c = 8$. Panjang sumbu mayor $2a = 20 \implies a = 10$, sehingga $a^2 = 100$. Nilai $b^2$ dihitung menggunakan hubungan $b^2 = a^2 - c^2 = 10^2 - 8^2 = 100 - 64 = 36$. Persamaan elips baku horizontal adalah $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$, yaitu $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$.
**Acuan:** siswa — siswa hal.43 Contoh Soal 1.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b01-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips dari jarak fokus*

Persamaan elips horizontal yang berpusat pada titik $O(0,0)$ dengan nilai eksentrisitas $\dfrac{5}{13}$ dan jarak kedua fokusnya $10$ adalah ....

- **A. $\dfrac{x^2}{169} + \dfrac{y^2}{144} = 1$** ✅  
  <sub>Benar: Jarak kedua fokus $2c = 10 \implies c = 5$. Eksentrisitas $e = \frac{c}{a} = \frac{5}{13} \implies a = 13$. Diperoleh $b^2 = a^2 - c^2 = 169 - 25 = 144$. Maka persamaannya $\frac{x^2}{169} + \frac{y^2}{144} = 1$.</sub>
- B. $\dfrac{x^2}{169} + \dfrac{y^2}{25} = 1$  
  <sub>Salah: Menggunakan c^2 = 25 sebagai b^2.</sub>
- C. $\dfrac{x^2}{100} + \dfrac{y^2}{25} = 1$  
  <sub>Salah: Memakai jarak kedua fokus 2c = 10 sebagai a = 10.</sub>
- D. $\dfrac{x^2}{144} + \dfrac{y^2}{169} = 1$  
  <sub>Salah: Tertukar antara sumbu mayor dan sumbu minor.</sub>

**Pembahasan:** Jarak kedua fokus adalah $2c = 10$, sehingga $c = 5$. Nilai eksentrisitas $e = \dfrac{c}{a} = \dfrac{5}{13}$, sehingga $a = 13$ dan $a^2 = 169$. Menghitung $b^2$: $b^2 = a^2 - c^2 = 13^2 - 5^2 = 169 - 25 = 144$. Jadi, persamaan elips horizontal tersebut adalah $\dfrac{x^2}{169} + \dfrac{y^2}{144} = 1$.
**Acuan:** siswa — siswa hal.50 Ayo Mencoba 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b01-b-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: menentukan nilai parameter sumbu elips*

Jika panjang sumbu mayor dan panjang sumbu minor suatu elips berturut-turut adalah $14$ dan $10$, nilai $a$ dan $b$ elips tersebut berturut-turut adalah ....

- A. $28$ dan $20$  
  <sub>Salah: Mengalikan panjang sumbu dengan 2 bukannya membagi dengan 2.</sub>
- B. $14$ dan $10$  
  <sub>Salah: Mengira panjang sumbu langsung sama dengan nilai a dan b.</sub>
- C. $5$ dan $7$  
  <sub>Salah: Tertukar antara nilai a (sumbu mayor) dan nilai b (sumbu minor).</sub>
- **D. $7$ dan $5$** ✅  
  <sub>Benar: Panjang sumbu mayor adalah $2a = 14 \implies a = 7$, dan panjang sumbu minor adalah $2b = 10 \implies b = 5$.</sub>

**Pembahasan:** Berdasarkan definisi unsur-unsur elips, panjang sumbu mayor dirumuskan dengan $2a$ dan panjang sumbu minor dengan $2b$. Diketahui $2a = 14$, maka $a = \dfrac{14}{2} = 7$. Diketahui $2b = 10$, maka $b = \dfrac{10}{2} = 5$. Jadi, nilai $a$ dan $b$ berturut-turut adalah $7$ dan $5$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b01-b-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: definisi geometris elips*

Kumpulan titik-titik pada bidang datar yang jumlah jaraknya terhadap dua titik tertentu selalu bernilai konstan disebut ....

- A. hiperbola  
  <sub>Salah: Hiperbola didefinisikan dengan selisih jarak ke dua titik fokus yang selalu tetap, bukan jumlah jarak.</sub>
- B. parabola  
  <sub>Salah: Parabola merupakan himpunan titik dengan jarak yang sama ke suatu titik fokus dan garis direktriks.</sub>
- C. lingkaran  
  <sub>Salah: Lingkaran adalah himpunan titik yang berjarak sama terhadap satu titik tertentu (titik pusat).</sub>
- **D. elips** ✅  
  <sub>Benar: Sesuai definisi, bangun datar yang jumlah jarak ke dua titik tertentu (titik fokus) selalu sama adalah elips.</sub>

**Pembahasan:** Berdasarkan buku siswa, elips adalah kumpulan titik-titik pada bidang datar yang jumlah jaraknya terhadap kedua titik tertentu (titik fokus) selalu sama atau konstan.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b01-b-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: menentukan persamaan elips dari fokus pada sumbu-y*  **[warning validator]**

Suatu elips memiliki titik pusat $O(0,0)$. Salah satu fokusnya terletak pada titik $(0,5)$ dan panjang sumbu mayornya adalah $26$. Persamaan elips tersebut adalah ....

- **A. $\dfrac{x^2}{144} + \dfrac{y^2}{169} = 1$** ✅  
  <sub>Benar: Fokus pada sumbu-$y$ menunjukkan elips vertikal dengan $c = 5$. Panjang sumbu mayor $2a = 26 \implies a = 13$, sehingga $a^2 = 169$. Nilai $b^2 = a^2 - c^2 = 169 - 25 = 144$. Bentuk baku elips vertikal adalah $\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1$, yaitu $\frac{x^2}{144} + \frac{y^2}{169} = 1$.</sub>
- B. $\dfrac{x^2}{25} + \dfrac{y^2}{169} = 1$  
  <sub>Salah: Keliru menggunakan nilai $c^2 = 25$ langsung sebagai penyebut tanpa mencari $b^2 = a^2 - c^2$.</sub>
- C. $\dfrac{x^2}{144} + \dfrac{y^2}{676} = 1$  
  <sub>Salah: Tidak membagi dua panjang sumbu mayor sehingga menganggap $a = 26$ dan $a^2 = 676$.</sub>
- D. $\dfrac{x^2}{169} + \dfrac{y^2}{144} = 1$  
  <sub>Salah: Tertukar antara bentuk elips vertikal dan horizontal (memasang $a^2$ di bawah $x^2$).</sub>

**Pembahasan:** Diketahui pusat elips $O(0,0)$ dan salah satu fokus di $(0,5)$, artinya elips berorientasi vertikal dan $c = 5$.
Panjang sumbu mayor adalah $2a = 26$, sehingga:
$$a = 13 \implies a^2 = 169$$
Menghitung nilai $b^2$:
$$b^2 = a^2 - c^2 = 13^2 - 5^2 = 169 - 25 = 144$$
Persamaan umum elips vertikal berpusat di $(0,0)$ adalah:
$$\frac{x^2}{b^2} + \frac{y^2}{a^2} = 1 \implies \frac{x^2}{144} + \frac{y^2}{169} = 1$$
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-5
**Warning:** kelas12_tl-b01-b-easy-bt01-013 sangat mirip dengan kelas12_tl-b01-b-medium-bt01-007 [exercise:batch01/B_medium.json] (0.89)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b01-b-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: menentukan panjang sumbu mayor bentuk implisit*

Panjang sumbu mayor dari elips dengan persamaan $16x^2 + 25y^2 = 400$ adalah ....

- A. $20$  
  <sub>Salah: Keliru mengambil koefisien $y^2 = 25$ lalu dikurangi $5$ atau mengalikan $a$ dengan $4$.</sub>
- B. $8$  
  <sub>Salah: Menghitung panjang sumbu minor $2b = 2(4) = 8$ alih-alih sumbu mayor.</sub>
- **C. $10$** ✅  
  <sub>Benar: Membagi persamaan dengan $400$ menghasilkan $\frac{x^2}{25} + \frac{y^2}{16} = 1$. Karena penyebut terbesar di bawah $x^2$, diperoleh $a^2 = 25 \implies a = 5$. Panjang sumbu mayor adalah $2a = 2(5) = 10$.</sub>
- D. $5$  
  <sub>Salah: Hanya menghitung nilai semi-sumbu mayor $a$, lupa mengalikannya dengan $2$.</sub>

**Pembahasan:** Ubah persamaan ke bentuk baku elips dengan membagi kedua ruas dengan $400$:
$$\frac{16x^2}{400} + \frac{25y^2}{400} = \frac{400}{400} \implies \frac{x^2}{25} + \frac{y^2}{16} = 1$$
Dari bentuk baku diperoleh:
- $a^2 = 25 \implies a = 5$
- $b^2 = 16 \implies b = 4$
Panjang sumbu mayor adalah $2a = 2 \times 5 = 10$.
**Acuan:** siswa — siswa hal.44 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b01-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: menentukan nilai eksentrisitas elips*

Nilai eksentrisitas dari elips $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$ adalah ....

- A. $\dfrac{3}{4}$  
  <sub>Salah: Menghitung rasio $\frac{c}{b} = \frac{3}{4}$ alih-alih membaginya dengan $a$.</sub>
- **B. $\dfrac{3}{5}$** ✅  
  <sub>Benar: Dari persamaan diketahui $a^2 = 25 \implies a = 5$ dan $b^2 = 16$. Nilai $c = \sqrt{a^2 - b^2} = \sqrt{25 - 16} = \sqrt{9} = 3$. Eksentrisitas $e = \frac{c}{a} = \frac{3}{5}$.</sub>
- C. $\dfrac{9}{25}$  
  <sub>Salah: Menghitung rasio kuadrat $\frac{c^2}{a^2} = \frac{9}{25}$ tanpa menarik akar.</sub>
- D. $\dfrac{4}{5}$  
  <sub>Salah: Menghitung rasio $\frac{b}{a} = \frac{4}{5}$ alih-alih $\frac{c}{a}$.</sub>

**Pembahasan:** Dari persamaan elips $\frac{x^2}{25} + \frac{y^2}{16} = 1$, diketahui:
- $a^2 = 25 \implies a = 5$
- $b^2 = 16 \implies b = 4$
Jarak fokus ke titik pusat ($c$):
$$c = \sqrt{a^2 - b^2} = \sqrt{25 - 16} = \sqrt{9} = 3$$
Nilai eksentrisitas ($e$):
$$e = \frac{c}{a} = \frac{3}{5}$$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b01-b-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: menentukan jarak antartitik fokus*

Jarak antartitik fokus dari elips dengan persamaan $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$ adalah ....

- A. $36$  
  <sub>Salah: Menggunakan nilai $c^2 = 36$ secara langsung tanpa menarik akar.</sub>
- B. $6$  
  <sub>Salah: Hanya menghitung nilai $c$ (jarak fokus ke pusat), bukan jarak antarkedua titik fokus ($2c$).</sub>
- **C. $12$** ✅  
  <sub>Benar: Dari persamaan diperoleh $a^2 = 100$ dan $b^2 = 64$. Nilai $c = \sqrt{100 - 64} = \sqrt{36} = 6$. Jarak antartitik fokus adalah $2c = 2(6) = 12$.</sub>
- D. $16$  
  <sub>Salah: Menghitung selisih panjang sumbu mayor dan minor: $2a - 2b = 20 - 16 = 4$, atau salah mengurangkan kuadrat.</sub>

**Pembahasan:** Dari persamaan elips $\frac{x^2}{100} + \frac{y^2}{64} = 1$, diketahui:
- $a^2 = 100$
- $b^2 = 64$
Jarak dari pusat ke fokus ($c$):
$$c = \sqrt{a^2 - b^2} = \sqrt{100 - 64} = \sqrt{36} = 6$$
Jarak antartitik fokus adalah ruas garis $F_1F_2$ dengan panjang:
$$\text{Jarak fokus} = 2c = 2 \times 6 = 12$$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b01-b-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: menentukan panjang latus rectum*

Panjang *latus rectum* dari elips dengan persamaan $25x^2 + 16y^2 = 400$ adalah ....

- A. $\dfrac{25}{2}$  
  <sub>Salah: Siswa terbalik menggunakan rumus menjadi $\dfrac{2a^2}{b}$.</sub>
- B. $\dfrac{16}{5}$  
  <sub>Salah: Siswa lupa mengalikan dengan 2 pada rumus latus rectum sehingga menghitung $\dfrac{b^2}{a}$.</sub>
- C. $\dfrac{32}{25}$  
  <sub>Salah: Siswa membagi dengan $a^2$ bukan $a$ sehingga menghitung $\dfrac{2b^2}{a^2}$.</sub>
- **D. $\dfrac{32}{5}$** ✅  
  <sub>Benar: Bentuk baku elips adalah $\dfrac{x^2}{16} + \dfrac{y^2}{25} = 1$, sehingga elips vertikal dengan $a^2 = 25$ ($a = 5$) dan $b^2 = 16$. Panjang *latus rectum* adalah $\dfrac{2b^2}{a} = \dfrac{2(16)}{5} = \dfrac{32}{5}$.</sub>

**Pembahasan:** Bagi kedua ruas persamaan $25x^2 + 16y^2 = 400$ dengan 400:
$$\dfrac{x^2}{16} + \dfrac{y^2}{25} = 1$$
Karena penyebut $y^2$ lebih besar daripada penyebut $x^2$, elips merupakan elips vertikal dengan $a^2 = 25 \Rightarrow a = 5$ dan $b^2 = 16$.
Panjang *latus rectum* elips vertikal dirumuskan sebagai:
$$\text{Panjang } L = \dfrac{2b^2}{a} = \dfrac{2 \times 16}{5} = \dfrac{32}{5}$$
**Acuan:** siswa — siswa hal.44 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b01-b-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: menentukan titik pusat elips dari persamaan baku*

Koordinat titik pusat dari elips dengan persamaan $\dfrac{(x - 5)^2}{36} + \dfrac{(y + 2)^2}{9} = 1$ adalah ....

- **A. $(5, -2)$** ✅  
  <sub>Benar: Bentuk umum elips dengan pusat $(m, n)$ adalah $\dfrac{(x - m)^2}{a^2} + \dfrac{(y - n)^2}{b^2} = 1$. Dengan $x - m = x - 5 \Rightarrow m = 5$ dan $y - n = y + 2 \Rightarrow n = -2$, pusat elips adalah $(5, -2)$.</sub>
- B. $(-5, 2)$  
  <sub>Salah: Siswa salah tanda pada kedua komponen koordinat pusat.</sub>
- C. $(-5, -2)$  
  <sub>Salah: Siswa salah tanda pada absis $x$ saat mengidentifikasi $x - m = x - 5$.</sub>
- D. $(5, 2)$  
  <sub>Salah: Siswa salah tanda pada ordinat $y$ saat mengidentifikasi $y - n = y + 2$.</sub>

**Pembahasan:** Persamaan baku elips dengan titik pusat $P(m, n)$ adalah:
$$\dfrac{(x - m)^2}{a^2} + \dfrac{(y - n)^2}{b^2} = 1$$
Berdasarkan persamaan $\dfrac{(x - 5)^2}{36} + \dfrac{(y + 2)^2}{9} = 1$:
- $x - m = x - 5 \Rightarrow m = 5$
- $y - n = y + 2 \Rightarrow n = -2$
Dengan demikian, koordinat titik pusat elips tersebut adalah $(5, -2)$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b01-b-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: persamaan elips dari sumbu mayor dan eksentrisitas*

Tentukan persamaan elips jika titik fokus terletak pada sumbu-$x$ dan simetris terhadap titik pusat koordinat, panjang sumbu mayor sebesar $10$, serta nilai eksentrisitas sebesar $\dfrac{4}{5}$.

- A. $\dfrac{x^2}{9} + \dfrac{y^2}{25} = 1$  
  <sub>Salah: Tertukar menganggap elips vertikal sehingga posisi a kuadrat dan b kuadrat terbalik.</sub>
- B. $\dfrac{x^2}{100} + \dfrac{y^2}{36} = 1$  
  <sub>Salah: Menganggap panjang sumbu mayor 10 sebagai nilai a tanpa membaginya dengan dua terlebih dahulu.</sub>
- **C. $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$** ✅  
  <sub>Benar: Panjang sumbu mayor $2a = 10 \implies a = 5$. Eksentrisitas $e = \dfrac{c}{a} = \dfrac{4}{5} \implies c = 4$. Nilai $b^2 = a^2 - c^2 = 25 - 16 = 9$. Karena fokus di sumbu-$x$ dan simetris terhadap $(0,0)$, persamaannya $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.</sub>
- D. $\dfrac{x^2}{25} + \dfrac{y^2}{16} = 1$  
  <sub>Salah: Menggunakan nilai c kuadrat sebagai penyebut variabel y alih-alih menghitung b kuadrat.</sub>

**Pembahasan:** Dari soal diketahui titik fokus berada pada sumbu-$x$ dan simetris terhadap titik pusat koordinat, artinya elips berbentuk horizontal berpusat di $O(0, 0)$.\nPanjang sumbu mayor $= 2a = 10 \implies a = 5$, sehingga $a^2 = 25$.\nNilai eksentrisitas $e = \dfrac{c}{a} = \dfrac{4}{5} \implies c = \dfrac{4}{5} \times 5 = 4$.\nHubungan antarnilai $a$, $b$, dan $c$ pada elips:\n$b^2 = a^2 - c^2 = 5^2 - 4^2 = 25 - 16 = 9$.\nBentuk baku elips horizontal berpusat di $O(0, 0)$ adalah:\n$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 \implies \dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.
**Acuan:** siswa — siswa hal.51 Ayo Mencoba 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b01-b-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: persamaan elips dari fokus dan sumbu minor*

Tentukan persamaan elips dengan titik pusat $(0, 0)$ jika salah satu titik fokusnya adalah $(0, 4)$ dan panjang sumbu minornya adalah $6$.

- A. $\dfrac{x^2}{36} + \dfrac{y^2}{52} = 1$  
  <sub>Salah: Menganggap panjang sumbu minor 6 langsung sebagai nilai b tanpa membaginya dengan dua.</sub>
- B. $\dfrac{x^2}{9} + \dfrac{y^2}{16} = 1$  
  <sub>Salah: Menggunakan nilai c kuadrat sebagai penyebut suku y alih-alih menghitung a kuadrat.</sub>
- **C. $\dfrac{x^2}{9} + \dfrac{y^2}{25} = 1$** ✅  
  <sub>Benar: Pusat $(0,0)$ dan fokus $(0,4)$ menunjukkan elips vertikal dengan $c = 4$. Sumbu minor $2b = 6 \implies b = 3 \implies b^2 = 9$. Nilai $a^2 = b^2 + c^2 = 9 + 16 = 25$. Persamaannya adalah $\dfrac{x^2}{9} + \dfrac{y^2}{25} = 1$.</sub>
- D. $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$  
  <sub>Salah: Keliru menganggap elips horizontal sehingga meletakkan a kuadrat di bawah suku x.</sub>

**Pembahasan:** Pusat elips berada di $(0, 0)$ dan salah satu fokusnya di $(0, 4)$ yang terletak pada sumbu-$y$, sehingga elips berbentuk vertikal dengan nilai $c = 4$.\nPanjang sumbu minor $= 2b = 6 \implies b = 3$, sehingga $b^2 = 9$.\nPada elips berlaku hubungan:\n$a^2 = b^2 + c^2 = 3^2 + 4^2 = 9 + 16 = 25$.\nPersamaan baku elips vertikal berpusat di $(0, 0)$ adalah:\n$\dfrac{x^2}{b^2} + \dfrac{y^2}{a^2} = 1 \implies \dfrac{x^2}{9} + \dfrac{y^2}{25} = 1$.
**Acuan:** siswa — siswa hal.43 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b01-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips*

Diketahui koordinat titik-titik fokus suatu elips adalah $F_1(9, 2)$ dan $F_2(-3, 2)$ serta salah satu koordinat ujung sumbu minornya adalah $(3, 10)$. Persamaan elips tersebut adalah ....

- A. $\dfrac{(x - 3)^2}{100} + \dfrac{(y - 2)^2}{28} = 1$  
  <sub>Salah: Salah menghitung nilai $b^2$ dengan mengurangkan $a^2 - c^2$ menggunakan $a = 8$ dari ujung minor alih-alih $b = 8$.</sub>
- B. $\dfrac{(x + 3)^2}{100} + \dfrac{(y + 2)^2}{64} = 1$  
  <sub>Salah: Salah tanda saat menyusun pergeseran titik pusat $(m, n)$ ke dalam $(x - m)^2$ dan $(y - n)^2$.</sub>
- C. $\dfrac{(x - 3)^2}{64} + \dfrac{(y - 2)^2}{100} = 1$  
  <sub>Salah: Tertukar menetapkan elips horizontal sebagai elips vertikal sehingga posisi $a^2$ dan $b^2$ terbalik.</sub>
- **D. $\dfrac{(x - 3)^2}{100} + \dfrac{(y - 2)^2}{64} = 1$** ✅  
  <sub>Benar: Pusat elips berada di titik tengah kedua fokus: $P\left(\frac{9 + (-3)}{2}, 2\right) = (3, 2)$. Jarak fokus ke pusat adalah $c = 9 - 3 = 6$. Karena kedua fokus memiliki ordinat yang sama ($y = 2$), sumbu mayor sejajar sumbu-$x$ (elips horizontal). Ujung sumbu minor di $(3, 10)$ memberikan panjang semi-sumbu minor $b = 10 - 2 = 8$, sehingga $b^2 = 64$. Nilai $a^2 = b^2 + c^2 = 64 + 6^2 = 64 + 36 = 100$. Persamaan baku elips adalah $\dfrac{(x - 3)^2}{100} + \dfrac{(y - 2)^2}{64} = 1$.</sub>

**Pembahasan:** 1. Menentukan titik pusat elips $P(m, n)$:
$$m = \frac{9 + (-3)}{2} = 3, \quad n = 2 \implies P(3, 2)$$
2. Menentukan nilai $c$:
$$c = 9 - 3 = 6$$
3. Menentukan nilai $b$:
Karena elips horizontal (fokus sejajar sumbu-$x$), sumbu minor sejajar sumbu-$y$. Ujung sumbu minor $(3, 10)$ memiliki jarak vertikal terhadap pusat:
$$b = |10 - 2| = 8 \implies b^2 = 64$$
4. Menentukan nilai $a^2$:
$$a^2 = b^2 + c^2 = 64 + 6^2 = 64 + 36 = 100$$
5. Persamaan elips:
$$\frac{(x - 3)^2}{100} + \frac{(y - 2)^2}{64} = 1$$
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b01-b-medium-bt01-002
*orisinal | C4 | 3 langkah | jenis: terapan elips kontekstual*

Sebuah terowongan jalan raya memiliki penampang berbentuk setengah elips dengan lebar alas $12\text{ meter}$ dan tinggi $4\text{ meter}$ di titik tertingginya. Sebuah truk pengangkut peti kemas memiliki lebar $6\text{ meter}$ dan akan melintas tepat di tengah jalan. Tinggi maksimum truk tersebut agar bagian atasnya tepat menyentuh atap terowongan adalah ....

- **A. $2\sqrt{3}\text{ meter}$** ✅  
  <sub>Benar: Tempatkan pusat elips pada titik $(0,0)$ di tengah alas jalan. Sumbu mayor terletak pada sumbu-$x$ dengan panjang $2a = 12\text{ m} \implies a = 6\text{ m}$. Tinggi terowongan merupakan semi-sumbu minor tegak, yaitu $b = 4\text{ m}$. Persamaan elips adalah $\dfrac{x^2}{36} + \dfrac{y^2}{16} = 1$. Karena truk selebar $6\text{ meter}$ melintas tepat di tengah, tepi truk berada pada $x = 3$ dan $x = -3$. Substitusikan $x = 3$ ke dalam persamaan elips:
$\dfrac{3^2}{36} + \dfrac{y^2}{16} = 1 \implies \dfrac{1}{4} + \dfrac{y^2}{16} = 1 \implies \dfrac{y^2}{16} = \dfrac{3}{4} \implies y^2 = 12 \implies y = 2\sqrt{3}\text{ meter}$.</sub>
- B. $3\text{ meter}$  
  <sub>Salah: Mengasumsikan bentuk terowongan sebagai segitiga/lurus sehingga tinggi berkurang linier $\frac{6}{12} \times 4$ atau salah hitung akar dari 12 menjadi 3.</sub>
- C. $2\sqrt{2}\text{ meter}$  
  <sub>Salah: Memasukkan nilai $x = 6$ (menggunakan seluruh lebar truk ke satu sisi) bukan $x = 3$.</sub>
- D. $3\sqrt{2}\text{ meter}$  
  <sub>Salah: Keliru mengalikan silang pada persamaan pecahan $\frac{y^2}{16} = \frac{3}{4}$ menjadi $y^2 = 18$.</sub>

**Pembahasan:** 1. Memodelkan persamaan elips:
Pusat lengkungan di $(0,0)$.
- Panjang sumbu alas elips $2a = 12 \implies a = 6$
- Tinggi elips $b = 4$
Persamaan elips:
$$\frac{x^2}{6^2} + \frac{y^2}{4^2} = 1 \iff \frac{x^2}{36} + \frac{y^2}{16} = 1$$

2. Menentukan absis batas tepi truk:
Truk memiliki lebar $6\text{ meter}$ dan melaju di tengah jalan secara simetris, maka tepi kanan truk berada pada $x = \frac{6}{2} = 3\text{ meter}$.

3. Menghitung tinggi maksimum ($y$):
$$\frac{3^2}{36} + \frac{y^2}{16} = 1$$
$$\frac{9}{36} + \frac{y^2}{16} = 1$$
$$\frac{1}{4} + \frac{y^2}{16} = 1$$
$$\frac{y^2}{16} = \frac{3}{4}$$
$$y^2 = 12 \implies y = \sqrt{12} = 2\sqrt{3}\text{ meter}$$
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b01-b-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: menentukan panjang sumbu mayor*

Sebuah elips horizontal memiliki titik pusat $(3, -1)$ dan salah satu fokusnya berada pada titik $(7, -1)$. Jika elips tersebut melalui titik $(3, 2)$, panjang sumbu mayor elips tersebut adalah ....

- A. $5$  
  <sub>Salah: Hanya menghitung panjang semi-sumbu mayor $a = 5$, lupa mengalikan 2.</sub>
- **B. $10$** ✅  
  <sub>Benar: Jarak fokus ke pusat adalah $c = 7 - 3 = 4$. Karena elips horizontal, persamaannya adalah $\dfrac{(x - 3)^2}{a^2} + \dfrac{(y + 1)^2}{b^2} = 1$. Elips melalui titik $(3, 2)$, sehingga $\dfrac{(3 - 3)^2}{a^2} + \dfrac{(2 + 1)^2}{b^2} = 1 \implies \dfrac{9}{b^2} = 1 \implies b^2 = 9$. Karena $a^2 = b^2 + c^2$, diperoleh $a^2 = 9 + 4^2 = 9 + 16 = 25$, sehingga $a = 5$. Panjang sumbu mayor adalah $2a = 2(5) = 10$.</sub>
- C. $8$  
  <sub>Salah: Menghitung jarak antarfokus $2c = 2(4) = 8$ bukan panjang sumbu mayor.</sub>
- D. $6$  
  <sub>Salah: Menghitung panjang sumbu minor $2b = 2(3) = 6$ bukan sumbu mayor.</sub>

**Pembahasan:** 1. Menentukan nilai $c$:
Pusat $(3, -1)$ dan fokus $(7, -1)$ terletak pada garis horizontal $y = -1$.
$$c = |7 - 3| = 4$$

2. Menentukan nilai $b^2$:
Persamaan baku elips horizontal berpusat di $(3, -1)$:
$$\frac{(x - 3)^2}{a^2} + \frac{(y + 1)^2}{b^2} = 1$$
Substitusikan titik $(3, 2)$ yang dilalui elips:
$$\frac{(3 - 3)^2}{a^2} + \frac{(2 + 1)^2}{b^2} = 1 \implies 0 + \frac{9}{b^2} = 1 \implies b^2 = 9$$

3. Menentukan nilai $a$ dan panjang sumbu mayor:
$$a^2 = b^2 + c^2 = 9 + 4^2 = 9 + 16 = 25 \implies a = 5$$
Panjang sumbu mayor $= 2a = 2 \times 5 = 10$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b01-b-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: menentukan titik fokus dari parameter*

Sebuah elips vertikal yang berpusat di titik $O(0, 0)$ memiliki panjang sumbu mayor $26$ dan panjang *latus rectum* sebesar $\dfrac{50}{13}$. Koordinat titik-titik fokus elips tersebut adalah ....

- A. $(12, 0)$ dan $(-12, 0)$  
  <sub>Salah: Salah menganggap elips sebagai elips horizontal sehingga fokus diletakkan pada sumbu-$x$.</sub>
- **B. $(0, 12)$ dan $(0, -12)$** ✅  
  <sub>Benar: Panjang sumbu mayor adalah $2a = 26 \implies a = 13$. Panjang *latus rectum* elips adalah $\dfrac{2b^2}{a} = \dfrac{50}{13}$. Substitusikan nilai $a = 13$:
$\dfrac{2b^2}{13} = \dfrac{50}{13} \implies 2b^2 = 50 \implies b^2 = 25$.
Nilai $c^2 = a^2 - b^2 = 13^2 - 25 = 169 - 25 = 144 \implies c = 12$.
Karena elips merupakan elips vertikal dengan pusat $(0,0)$, fokusnya terletak pada sumbu-$y$, yaitu $(0, 12)$ dan $(0, -12)$.</sub>
- C. $(0, 13)$ dan $(0, -13)$  
  <sub>Salah: Mengira titik fokus sama dengan titik puncak sumbu mayor.</sub>
- D. $(0, 5)$ dan $(0, -5)$  
  <sub>Salah: Menggunakan nilai $b = 5$ sebagai jarak fokus ke pusat $c$.</sub>

**Pembahasan:** 1. Menentukan nilai $a$:
Panjang sumbu mayor $= 2a = 26 \implies a = 13$

2. Menentukan nilai $b^2$ melalui panjang *latus rectum*:
$$\text{Panjang latus rectum} = \frac{2b^2}{a} = \frac{50}{13}$$
$$\frac{2b^2}{13} = \frac{50}{13} \implies 2b^2 = 50 \implies b^2 = 25$$

3. Menentukan nilai $c$ dan titik fokus:
$$c^2 = a^2 - b^2 = 169 - 25 = 144 \implies c = 12$$
Karena elips vertikal berpusat di titik asal $O(0, 0)$, titik fokus berada di $(0, c)$ dan $(0, -c)$, yaitu $(0, 12)$ dan $(0, -12)$.
**Acuan:** siswa — siswa hal.43

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b01-b-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan dari puncak dan fokus*

Persamaan elips yang memiliki titik-titik fokus $(1, -2)$ dan $(7, -2)$ serta titik-titik puncak mayor $(0, -2)$ dan $(8, -2)$ adalah ....

- A. $\dfrac{(x - 4)^2}{7} + \dfrac{(y + 2)^2}{16} = 1$  
  <sub>Salah: Siswa tertukar menempatkan elips sebagai elips vertikal.</sub>
- B. $\dfrac{(x - 4)^2}{16} + \dfrac{(y + 2)^2}{9} = 1$  
  <sub>Salah: Siswa keliru menggunakan nilai $c^2 = 9$ sebagai penyebut $y$, bukan mencari $b^2$.</sub>
- **C. $\dfrac{(x - 4)^2}{16} + \dfrac{(y + 2)^2}{7} = 1$** ✅  
  <sub>Benar: Pusat elips adalah titik tengah kedua fokus, yaitu $\left(\frac{1 + 7}{2}, -2\right) = (4, -2)$. Jarak antarpuncak adalah $2a = 8 - 0 = 8 \Rightarrow a = 4 \Rightarrow a^2 = 16$. Jarak antarfokus adalah $2c = 7 - 1 = 6 \Rightarrow c = 3$. Nilai $b^2 = a^2 - c^2 = 16 - 9 = 7$. Karena sumbu mayor sejajar sumbu-$x$, persamaannya $\frac{(x - 4)^2}{16} + \frac{(y + 2)^2}{7} = 1$.</sub>
- D. $\dfrac{(x + 4)^2}{16} + \dfrac{(y - 2)^2}{7} = 1$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik pusat ke dalam bentuk baku.</sub>

**Pembahasan:** 1. Koordinat pusat $(m, n) = \left(\frac{1 + 7}{2}, -2\right) = (4, -2)$.\n2. Sumbu mayor horizontal: $2a = 8 - 0 = 8 \Rightarrow a = 4 \Rightarrow a^2 = 16$.\n3. Jarak fokus: $2c = 7 - 1 = 6 \Rightarrow c = 3 \Rightarrow c^2 = 9$.\n4. Hitung $b^2$: $b^2 = a^2 - c^2 = 16 - 9 = 7$.\n5. Persamaan elips: $\frac{(x - 4)^2}{16} + \frac{(y + 2)^2}{7} = 1$.
**Acuan:** siswa — siswa hal.46 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b01-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan dari eksentrisitas*

Sebuah elips horizontal berpusat di titik $O(0, 0)$ memiliki nilai eksentrisitas $\dfrac{3}{5}$ dan jarak antartitik fokusnya adalah $18$. Persamaan elips tersebut adalah ....

- **A. $\dfrac{x^2}{225} + \dfrac{y^2}{144} = 1$** ✅  
  <sub>Benar: Jarak antarfokus $2c = 18 \Rightarrow c = 9$. Eksentrisitas $e = \frac{c}{a} = \frac{3}{5} \Rightarrow \frac{9}{a} = \frac{3}{5} \Rightarrow a = 15 \Rightarrow a^2 = 225$. Nilai $b^2 = a^2 - c^2 = 225 - 81 = 144$. Maka persamaan elips adalah $\frac{x^2}{225} + \frac{y^2}{144} = 1$.</sub>
- B. $\dfrac{x^2}{144} + \dfrac{y^2}{225} = 1$  
  <sub>Salah: Siswa menganggap elips berbentuk vertikal sehingga membalik posisi $a^2$ dan $b^2$.</sub>
- C. $\dfrac{x^2}{225} + \dfrac{y^2}{81} = 1$  
  <sub>Salah: Siswa memasukkan nilai $c^2$ langsung sebagai penyebut $y^2$.</sub>
- D. $\dfrac{x^2}{225} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Siswa salah menghitung selisih kuadrat $225 - 81$ menjadi $100$.</sub>

**Pembahasan:** 1. $2c = 18 \Rightarrow c = 9$.\n2. $e = \frac{c}{a} \Rightarrow \frac{3}{5} = \frac{9}{a} \Rightarrow a = 15 \Rightarrow a^2 = 225$.\n3. $b^2 = a^2 - c^2 = 15^2 - 9^2 = 225 - 81 = 144$.\n4. Persamaan elips horizontal berpusat di $(0, 0)$: $\frac{x^2}{225} + \frac{y^2}{144} = 1$.
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b01-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips dari fokus dan sumbu mayor*  **[warning validator]**

Suatu elips memiliki titik pusat $O(0, 0)$. Salah satu fokusnya terletak pada titik $(8, 0)$ dan panjang sumbu mayornya adalah $34$. Persamaan elips tersebut adalah ....

- A. $\dfrac{x^2}{289} + \dfrac{y^2}{64} = 1$  
  <sub>Salah: Langsung memasukkan $c^2 = 64$ sebagai penyebut pada suku $y^2$ tanpa mencari nilai $b^2$.</sub>
- B. $\dfrac{x^2}{289} + \dfrac{y^2}{353} = 1$  
  <sub>Salah: Keliru menjumlahkan $a^2 + c^2 = 289 + 64 = 353$ untuk memperoleh nilai $b^2$.</sub>
- C. $\dfrac{x^2}{225} + \dfrac{y^2}{289} = 1$  
  <sub>Salah: Salah mengenali bentuk elips sebagai elips vertikal sehingga posisi $a^2$ dan $b^2$ tertukar.</sub>
- **D. $\dfrac{x^2}{289} + \dfrac{y^2}{225} = 1$** ✅  
  <sub>Benar: Fokus pada $(8, 0)$ menunjukkan elips horizontal dengan $c = 8$. Panjang sumbu mayor $2a = 34 \implies a = 17$, sehingga $a^2 = 289$. Nilai $b^2 = a^2 - c^2 = 17^2 - 8^2 = 289 - 64 = 225$. Persamaan elipsnya adalah $\dfrac{x^2}{289} + \dfrac{y^2}{225} = 1$.</sub>

**Pembahasan:** Pusat elips di $(0,0)$ dan salah satu fokus di $(8,0)$, terletak pada sumbu-$x$, sehingga elips berbentuk horizontal dan $c = 8$.
Panjang sumbu mayor $= 2a = 34 \implies a = 17$, maka $a^2 = 289$.
Nilai $b^2 = a^2 - c^2 = 17^2 - 8^2 = 289 - 64 = 225$.
Persamaan elips horizontal berpusat $(0,0)$ adalah $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$, sehingga diperoleh $\dfrac{x^2}{289} + \dfrac{y^2}{225} = 1$.
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips
**Warning:** kelas12_tl-b01-b-medium-bt01-007 sangat mirip dengan kelas12_tl-b01-b-easy-bt01-001 [exercise:batch01/B_easy.json] (0.89)
**Warning:** kelas12_tl-b01-b-medium-bt01-007 sangat mirip dengan kelas12_tl-b01-b-easy-bt01-013 [exercise:batch01/B_easy.json] (0.89)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b01-b-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: menentukan eksentrisitas elips*

Nilai eksentrisitas dari elips dengan persamaan $\dfrac{(x - 2)^2}{16} + \dfrac{(y + 3)^2}{25} = 1$ adalah ....

- A. $\dfrac{3}{4}$  
  <sub>Salah: Membagi jarak fokus $c$ dengan semi-sumbu minor $b$ yaitu $\dfrac{c}{b} = \dfrac{3}{4}$.</sub>
- B. $\dfrac{4}{5}$  
  <sub>Salah: Keliru menghitung rasio semi-sumbu minor terhadap semi-sumbu mayor $\dfrac{b}{a} = \dfrac{4}{5}$.</sub>
- C. $\dfrac{5}{3}$  
  <sub>Salah: Terbalik dalam menuliskan perbandingan rumus eksentrisitas menjadi $\dfrac{a}{c} = \dfrac{5}{3}$.</sub>
- **D. $\dfrac{3}{5}$** ✅  
  <sub>Benar: Penyebut terbesar berada di bawah suku $y$, maka $a^2 = 25 \implies a = 5$ dan $b^2 = 16$. Nilai $c = \sqrt{a^2 - b^2} = \sqrt{25 - 16} = \sqrt{9} = 3$. Eksentrisitas $e = \dfrac{c}{a} = \dfrac{3}{5}$.</sub>

**Pembahasan:** Dari persamaan $\dfrac{(x - 2)^2}{16} + \dfrac{(y + 3)^2}{25} = 1$, penyebut suku $y$ lebih besar, sehingga elips berbentuk vertikal dengan:
$a^2 = 25 \implies a = 5$
$b^2 = 16 \implies b = 4$
Jarak fokus $c$ dihitung dengan:
$c = \sqrt{a^2 - b^2} = \sqrt{25 - 16} = \sqrt{9} = 3$
Rumus eksentrisitas adalah $e = \dfrac{c}{a}$, sehingga:
$e = \dfrac{3}{5}$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b01-b-medium-bt01-009
*orisinal | C4 | 4 langkah | jenis: menentukan sumbu minor dari unsur elips*

Sebuah elips memiliki titik-titik puncak $(1, 8)$ dan $(1, -4)$ serta salah satu titik fokusnya berada di $(1, 6)$. Panjang sumbu minor elips tersebut adalah ....

- A. $4\sqrt{13}$  
  <sub>Salah: Salah rumus relasi fokus dengan menjumlahkan $b = \sqrt{a^2 + c^2} = \sqrt{36 + 16} = \sqrt{52} = 2\sqrt{13}$, sehingga $2b = 4\sqrt{13}$.</sub>
- B. $2\sqrt{5}$  
  <sub>Salah: Hanya menghitung nilai semi-sumbu minor $b$, lupa mengalikannya dengan 2 untuk mendapatkan panjang sumbu minor.</sub>
- **C. $4\sqrt{5}$** ✅  
  <sub>Benar: Kedua puncak memiliki absis sama, yaitu $x=1$, sehingga sumbu mayor vertikal. Pusat elips terletak di titik tengah kedua puncak: $\left(1, \frac{8 + (-4)}{2}\right) = (1, 2)$. Panjang sumbu mayor $2a = 8 - (-4) = 12 \implies a = 6$. Jarak titik fokus $(1, 6)$ ke pusat $(1, 2)$ adalah $c = 6 - 2 = 4$. Semi-sumbu minor $b = \sqrt{a^2 - c^2} = \sqrt{6^2 - 4^2} = \sqrt{36 - 16} = \sqrt{20} = 2\sqrt{5}$. Jadi, panjang sumbu minor adalah $2b = 4\sqrt{5}$.</sub>
- D. $8$  
  <sub>Salah: Mengira $b = c = 4$, sehingga panjang sumbu minor dihitung sebagai $2c = 8$.</sub>

**Pembahasan:** 1. Puncak elips adalah $(1, 8)$ dan $(1, -4)$. Karena absisnya sama, sumbu mayor sejajar sumbu-$y$.
Titik pusat $P(m, n) = \left(1, \dfrac{8 + (-4)}{2}\right) = (1, 2)$.
2. Panjang sumbu mayor $= 2a = 8 - (-4) = 12 \implies a = 6$.
3. Titik fokus terletak pada $(1, 6)$, maka nilai $c = |6 - 2| = 4$.
4. Menentukan nilai $b$:
$b = \sqrt{a^2 - c^2} = \sqrt{6^2 - 4^2} = \sqrt{36 - 16} = \sqrt{20} = 2\sqrt{5}$.
Panjang sumbu minor adalah $2b = 2(2\sqrt{5}) = 4\sqrt{5}$.
**Acuan:** siswa — siswa hal.46

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b01-b-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: menentukan sumbu minor dari bentuk umum*

Panjang sumbu minor dari elips dengan persamaan $25x^2 + 9y^2 - 100x + 54y - 44 = 0$ adalah ....

- A. $3$  
  <sub>Salah: Hanya menghitung nilai semi-sumbu minor $b$, tidak mengalikan 2.</sub>
- B. $10$  
  <sub>Salah: Keliru menghitung panjang sumbu mayor $2a = 2(5) = 10$.</sub>
- C. $5$  
  <sub>Salah: Keliru mengambil nilai semi-sumbu mayor $a = 5$.</sub>
- **D. $6$** ✅  
  <sub>Benar: Melengkapkan kuadrat sempurna:
$25(x^2 - 4x) + 9(y^2 + 6y) = 44$
$25(x - 2)^2 - 100 + 9(y + 3)^2 - 81 = 44$
$25(x - 2)^2 + 9(y + 3)^2 = 225$
Dibagi 225 menghasilkan $\dfrac{(x - 2)^2}{9} + \dfrac{(y + 3)^2}{25} = 1$.
Diperoleh $a^2 = 25$ dan $b^2 = 9 \implies b = 3$. Panjang sumbu minor adalah $2b = 2(3) = 6$.</sub>

**Pembahasan:** Kelompokkan variabel $x$ dan $y$ untuk melengkapkan kuadrat sempurna:
$25(x^2 - 4x) + 9(y^2 + 6y) = 44$
$25((x - 2)^2 - 4) + 9((y + 3)^2 - 9) = 44$
$25(x - 2)^2 - 100 + 9(y + 3)^2 - 81 = 44$
$25(x - 2)^2 + 9(y + 3)^2 = 44 + 100 + 81$
$25(x - 2)^2 + 9(y + 3)^2 = 225$

Bagi kedua ruas dengan 225:
$\dfrac{(x - 2)^2}{9} + \dfrac{(y + 3)^2}{25} = 1$

Karena $25 > 9$, maka $a^2 = 25$ dan $b^2 = 9$.
Nilai $b = \sqrt{9} = 3$.
Panjang sumbu minor adalah $2b = 2 \times 3 = 6$.
**Acuan:** siswa — siswa hal.36

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b01-b-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: menentukan titik puncak dari bentuk umum*

Koordinat titik-titik puncak pada sumbu mayor dari elips dengan persamaan $4x^2 + 9y^2 + 24x - 36y + 36 = 0$ adalah ....

- A. (0, -2) dan (-6, -2)  
  <sub>Salah: Kesalahan tanda pada ordinat pusat, mengira pusat $(-3, -2)$ bukan $(-3, 2)$.</sub>
- **B. $(0, 2)$ dan $(-6, 2)$** ✅  
  <sub>Benar: Bentuk kuadrat sempurna: $4(x+3)^2 + 9(y-2)^2 = 36 \iff \frac{(x+3)^2}{9} + \frac{(y-2)^2}{4} = 1$. Pusat $(-3, 2)$, $a = 3$ sepanjang sumbu horizontal. Puncak mayor di $(-3 \pm 3, 2)$, yaitu $(0, 2)$ dan $(-6, 2)$.</sub>
- C. (-3, 4) dan (-3, 0)  
  <sub>Salah: Mengambil titik puncak pada sumbu minor (menggunakan $b = 2$ pada sumbu vertikal), bukan sumbu mayor.</sub>
- D. (6, 2) dan (0, 2)  
  <sub>Salah: Kesalahan tanda saat melengkapkan kuadrat sempurna, mengira titik pusat adalah $(3, 2)$.</sub>

**Pembahasan:** Kelompokkan suku-suku sejenis:
$4(x^2 + 6x) + 9(y^2 - 4y) = -36$
$4(x + 3)^2 - 36 + 9(y - 2)^2 - 36 = -36$
$4(x + 3)^2 + 9(y - 2)^2 = 36$
Bagi kedua ruas dengan 36:
$\dfrac{(x + 3)^2}{9} + \dfrac{(y - 2)^2}{4} = 1$
Diperoleh pusat elips $(m, n) = (-3, 2)$. Karena penyebut suku $x$ lebih besar ($a^2 = 9 > b^2 = 4$), maka elips horizontal dengan $a = 3$.
Titik puncak pada sumbu mayor terletak di $(m \pm a, n)$:
$(-3 + 3, 2) = (0, 2)$
$(-3 - 3, 2) = (-6, 2)$
**Acuan:** pretest — kelas12_tl-b01-p0052-latihan-soal-elips-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b01-b-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips dari eksentrisitas dan fokus*

Persamaan elips horizontal yang berpusat pada titik $O(0, 0)$ jika nilai eksentrisitasnya sebesar $\dfrac{5}{13}$ dan jarak kedua fokusnya adalah $20$ adalah ....

- **A. $\dfrac{x^2}{676} + \dfrac{y^2}{576} = 1$** ✅  
  <sub>Benar: Jarak fokus $2c = 20 \implies c = 10$. Eksentrisitas $e = \frac{c}{a} = \frac{5}{13} \implies a = 26$. Nilai $b^2 = a^2 - c^2 = 26^2 - 10^2 = 576$. Persamaan elips: $\frac{x^2}{26^2} + \frac{y^2}{576} = 1 \implies \frac{x^2}{676} + \frac{y^2}{576} = 1$.</sub>
- B. $\dfrac{x^2}{169} + \dfrac{y^2}{144} = 1$  
  <sub>Salah: Mengira $a = 13$ dan $b = 12$ tanpa mengalikan dengan faktor skala dari $c = 10$.</sub>
- C. $\dfrac{x^2}{676} + \dfrac{y^2}{100} = 1$  
  <sub>Salah: Memakai $c^2 = 100$ sebagai penyebut $y^2$ alih-alih menghitung $b^2 = a^2 - c^2$.</sub>
- D. $\dfrac{x^2}{576} + \dfrac{y^2}{676} = 1$  
  <sub>Salah: Tertukar menempatkan nilai $a^2$ dan $b^2$, menghasilkan elips vertikal.</sub>

**Pembahasan:** Diketahui:
Jarak kedua fokus $= 2c = 20 \implies c = 10$.
Nilai eksentrisitas $e = \dfrac{c}{a} = \dfrac{5}{13}$.
Substitusi $c = 10$:
$\dfrac{10}{a} = \dfrac{5}{13} \implies a = \dfrac{10 \times 13}{5} = 26$
Menentukan nilai $b^2$:
$b^2 = a^2 - c^2 = 26^2 - 10^2 = 676 - 100 = 576$
Karena elips horizontal dengan pusat $O(0, 0)$, persamaannya adalah:
$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 \implies \dfrac{x^2}{676} + \dfrac{y^2}{576} = 1$
**Acuan:** siswa — siswa hal.50 Ayo Mencoba 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b01-b-medium-bt01-013
*variasi (angka) | C4 | 4 langkah | jenis: menentukan persamaan elips menyinggung sumbu-y*

Persamaan elips yang memiliki titik-titik fokus pada koordinat $(4, 3)$ dan $(4, -5)$ serta menyinggung sumbu-$y$ adalah ....

- A. $\dfrac{(x - 4)^2}{16} + \dfrac{(y - 1)^2}{32} = 1$  
  <sub>Salah: Kesalahan penentuan ordinat titik pusat, menggunakan $+1$ bukan $-1$.</sub>
- B. $\dfrac{(x - 4)^2}{32} + \dfrac{(y + 1)^2}{16} = 1$  
  <sub>Salah: Tertukar menempatkan nilai $a^2$ di bawah $(x-4)^2$ padahal elips adalah elips vertikal.</sub>
- C. $\dfrac{(x + 4)^2}{16} + \dfrac{(y - 1)^2}{32} = 1$  
  <sub>Salah: Tanda koordinat pusat elips terbalik seluruhnya.</sub>
- **D. $\dfrac{(x - 4)^2}{16} + \dfrac{(y + 1)^2}{32} = 1$** ✅  
  <sub>Benar: Pusat elips di tengah kedua fokus: $(4, \frac{3 + (-5)}{2}) = (4, -1)$. Jarak fokus $2c = 8 \implies c = 4$. Garis fokus sejajar sumbu-y (vertikal). Karena elips menyinggung sumbu-y ($x = 0$), maka jarak horizontal pusat ke sumbu-y adalah $b = |4 - 0| = 4$. Maka $a^2 = b^2 + c^2 = 4^2 + 4^2 = 32$. Persamaan: $\frac{(x - 4)^2}{16} + \dfrac{(y + 1)^2}{32} = 1$.</sub>

**Pembahasan:** 1. Menentukan titik pusat $P(m, n)$:
$m = 4$
$n = \dfrac{3 + (-5)}{2} = -1$
Jadi pusat elips adalah $P(4, -1)$.
2. Menentukan nilai $c$:
$2c = 3 - (-5) = 8 \implies c = 4$.
3. Sumbu mayor sejajar sumbu-$y$ (elips vertikal). Karena elips menyinggung sumbu-$y$, jarak horizontal dari pusat $(4, -1)$ ke garis singgung $x = 0$ merupakan panjang semi-minor, yaitu $b = 4$.
4. Menentukan nilai $a^2$:
$a^2 = b^2 + c^2 = 4^2 + 4^2 = 16 + 16 = 32$.
5. Persamaan elips vertikal:
$\dfrac{(x - m)^2}{b^2} + \dfrac{(y - n)^2}{a^2} = 1 \implies \dfrac{(x - 4)^2}{16} + \dfrac{(y + 1)^2}{32} = 1$
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b01-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: menentukan jarak antarfokus elips*

Jarak antara kedua titik fokus dari elips dengan persamaan $\dfrac{(x + 2)^2}{64} + \dfrac{(y - 5)^2}{39} = 1$ adalah ....

- A. $2\sqrt{103}$  
  <sub>Salah: Menggunakan rumus hiperbola $c^2 = a^2 + b^2 = 64 + 39 = 103$ sehingga $2c = 2\sqrt{103}$.</sub>
- B. $5$  
  <sub>Salah: Hanya menghitung nilai fokus $c$, lupa mengalikan dua untuk jarak kedua fokus.</sub>
- **C. $10$** ✅  
  <sub>Benar: Dari persamaan baku, diperoleh $a^2 = 64$ dan $b^2 = 39$. Karena $a^2 > b^2$, maka $c^2 = a^2 - b^2 = 64 - 39 = 25$, sehingga $c = 5$. Jarak antara kedua titik fokus adalah $2c = 2(5) = 10$.</sub>
- D. $16$  
  <sub>Salah: Menghitung panjang sumbu mayor $2a = 2(8) = 16$.</sub>

**Pembahasan:** Persamaan elips:
$\dfrac{(x + 2)^2}{64} + \dfrac{(y - 5)^2}{39} = 1$
Berdasarkan persamaan di atas:
$a^2 = 64 \implies a = 8$
$b^2 = 39$
Hubungan antarnilai $a$, $b$, dan $c$ pada elips adalah:
$c^2 = a^2 - b^2$
$c^2 = 64 - 39 = 25$
$c = \sqrt{25} = 5$
Jarak antartitik fokus adalah ruas garis penghubung kedua fokus sebesar $2c$:
$2c = 2 \times 5 = 10$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b01-b-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: menentukan sumbu minor dari direktriks dan eksentrisitas*

Sebuah elips horizontal berpusat di titik $O(0, 0)$ memiliki persamaan garis-garis direktriks $x = 8$ dan $x = -8$. Jika nilai eksentrisitas elips tersebut adalah $\dfrac{1}{2}$, panjang sumbu minor elips tersebut adalah ....

- **A. $4\sqrt{3}$** ✅  
  <sub>Benar: Direktriks elips horizontal adalah $x = \pm \frac{a}{e} \implies \frac{a}{1/2} = 8 \implies a = 4$. Karena $e = \frac{c}{a} = \frac{1}{2}$, diperoleh $c = 2$. Maka $b = \sqrt{a^2 - c^2} = \sqrt{16 - 4} = \sqrt{12} = 2\sqrt{3}$. Panjang sumbu minor adalah $2b = 2(2\sqrt{3}) = 4\sqrt{3}$.</sub>
- B. $2\sqrt{3}$  
  <sub>Salah: Hanya menghitung nilai $b$ (semi-sumbu minor), lupa mengalikan dua untuk panjang sumbu minor.</sub>
- C. $8$  
  <sub>Salah: Menghitung panjang sumbu mayor $2a = 2(4) = 8$.</sub>
- D. $4\sqrt{5}$  
  <sub>Salah: Keliru menggunakan rumus $b^2 = a^2 + c^2 = 16 + 4 = 20$ sehingga $2b = 2\sqrt{20} = 4\sqrt{5}$.</sub>

**Pembahasan:** Persamaan garis direktriks elips horizontal berpusat di $O(0, 0)$ adalah $x = \pm \dfrac{a}{e}$.
Diketahui persamaan direktriks $x = \pm 8$ dan $e = \dfrac{1}{2}$:
$\dfrac{a}{e} = 8 \implies a = 8 \times \dfrac{1}{2} = 4$
Dari rumus eksentrisitas $e = \dfrac{c}{a}$:
$c = a \times e = 4 \times \dfrac{1}{2} = 2$
Hitung nilai $b$:
$b^2 = a^2 - c^2 = 4^2 - 2^2 = 16 - 4 = 12$
$b = \sqrt{12} = 2\sqrt{3}$
Panjang sumbu minor adalah:
$2b = 2 \times 2\sqrt{3} = 4\sqrt{3}$
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b01-b-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: menentukan latus rectum dari bentuk umum*

Panjang *latus rectum* dari elips dengan persamaan $9x^2 + 25y^2 + 18x - 100y - 116 = 0$ adalah ....

- A. $\dfrac{6}{5}$  
  <sub>Salah: Menggunakan nilai $b$ bukan $b^2$ pada pembilang: $\frac{2b}{a} = \frac{2(3)}{5} = \frac{6}{5}$.</sub>
- **B. $\dfrac{18}{5}$** ✅  
  <sub>Benar: Persamaan diubah menjadi bentuk baku: $9(x + 1)^2 + 25(y - 2)^2 = 225 \iff \frac{(x + 1)^2}{25} + \frac{(y - 2)^2}{9} = 1$. Diperoleh $a^2 = 25 \Rightarrow a = 5$ dan $b^2 = 9$. Panjang latus rectum dihitung dengan $\frac{2b^2}{a} = \frac{2(9)}{5} = \frac{18}{5}$.</sub>
- C. $\dfrac{50}{3}$  
  <sub>Salah: Tertukar menggunakan rumus $\frac{2a^2}{b} = \frac{2(25)}{3} = \frac{50}{3}$.</sub>
- D. $\dfrac{9}{5}$  
  <sub>Salah: Lupa mengalikan dengan faktor 2 pada rumus latus rectum, sehingga menghitung $\frac{b^2}{a}$.</sub>

**Pembahasan:** 1. Mengubah persamaan ke bentuk baku:
$$9(x^2 + 2x) + 25(y^2 - 4y) = 116$$
$$9((x + 1)^2 - 1) + 25((y - 2)^2 - 4) = 116$$
$$9(x + 1)^2 - 9 + 25(y - 2)^2 - 100 = 116$$
$$9(x + 1)^2 + 25(y - 2)^2 = 225$$

Bagi kedua ruas dengan 225:
$$\dfrac{(x + 1)^2}{25} + \dfrac{(y - 2)^2}{9} = 1$$

2. Mengidentifikasi nilai $a$ dan $b$:
Karena penyebut terbesar berada di bawah suku $x$, maka elips horizontal dengan:
$$a^2 = 25 \implies a = 5$$
$$b^2 = 9 \implies b = 3$$

3. Menghitung panjang *latus rectum*:
$$\text{Panjang latus rectum} = \dfrac{2b^2}{a} = \dfrac{2(9)}{5} = \dfrac{18}{5}$$
**Acuan:** siswa — siswa hal.44

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b01-b-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips*

Diketahui koordinat titik-titik fokus suatu elips adalah $F_1(6, 3)$ dan $F_2(-6, 3)$ serta salah satu koordinat ujung sumbu minornya adalah $(0, 11)$. Persamaan elips tersebut adalah ....

- A. $\dfrac{x^2}{64} + \dfrac{(y - 3)^2}{100} = 1$  
  <sub>Salah: Tertukar antara penyebut suku $x$ dan $y$ (menganggap elips vertikal).</sub>
- **B. $\dfrac{x^2}{100} + \dfrac{(y - 3)^2}{64} = 1$** ✅  
  <sub>Benar: Kedua fokus memiliki ordinat $y = 3$, sehingga elips berbentuk horizontal dengan pusat $(0, 3)$ dan $c = 6$. Ujung sumbu minor $(0, 11)$ menghasilkan $b = |11 - 3| = 8$. Diperoleh $a^2 = b^2 + c^2 = 64 + 36 = 100$. Jadi, persamaannya adalah $\dfrac{x^2}{100} + \dfrac{(y - 3)^2}{64} = 1$.</sub>
- C. $\dfrac{x^2}{64} + \dfrac{(y - 3)^2}{28} = 1$  
  <sub>Salah: Keliru menganggap panjang semi-sumbu minor sebagai $a$ sehingga menghitung $b^2 = a^2 - c^2 = 64 - 36 = 28$.</sub>
- D. $\dfrac{x^2}{100} + \dfrac{(y + 3)^2}{64} = 1$  
  <sub>Salah: Salah tanda pada koordinat pusat ordinat $y$.</sub>

**Pembahasan:** 1. **Menentukan titik pusat dan nilai $c$:**
Titik fokus berada pada $F_1(6, 3)$ dan $F_2(-6, 3)$. Karena ordinatnya sama, sumbu utama sejajar sumbu-$x$ (elips horizontal).
Titik pusat $P(m, n) = \left(\dfrac{6 + (-6)}{2}, \dfrac{3 + 3}{2}\right) = (0, 3)$.
Jarak antarfokus adalah $2c = 6 - (-6) = 12 \implies c = 6$.

2. **Menentukan nilai $b$:**
Ujung sumbu minor terletak pada $(0, 11)$. Jarak ujung sumbu minor ke pusat adalah:
$b = |11 - 3| = 8 \implies b^2 = 64$.

3. **Menentukan nilai $a^2$ dan persamaan elips:**
Pada elips berlaku $a^2 = b^2 + c^2$:
$a^2 = 64 + 6^2 = 64 + 36 = 100$.

Bentuk baku elips horizontal berpusat di $(m, n)$ adalah:
$\dfrac{(x - m)^2}{a^2} + \dfrac{(y - n)^2}{b^2} = 1$
$\dfrac{(x - 0)^2}{100} + \dfrac{(y - 3)^2}{64} = 1 \iff \dfrac{x^2}{100} + \dfrac{(y - 3)^2}{64} = 1$.
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b01-b-medium-bt01-018
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips dari puncak dan fokus vertikal*

Persamaan elips yang memiliki titik-titik fokus $(2, 1)$ dan $(2, 7)$ serta kedua titik puncak pada sumbu mayor $(2, -1)$ dan $(2, 9)$ adalah ....

- A. $\dfrac{(x - 2)^2}{34} + \dfrac{(y - 4)^2}{25} = 1$  
  <sub>Salah: Salah rumus parameter, menghitung b kuadrat sebagai jumlah a kuadrat ditambah c kuadrat.</sub>
- B. $\dfrac{(x + 2)^2}{16} + \dfrac{(y + 4)^2}{25} = 1$  
  <sub>Salah: Salah tanda pergeseran koordinat pusat saat memasukkan ke rumus baku.</sub>
- **C. $\dfrac{(x - 2)^2}{16} + \dfrac{(y - 4)^2}{25} = 1$** ✅  
  <sub>Benar: Pusat elips adalah titik tengah fokus, yaitu $(2, 4)$. Sumbu mayor sejajar sumbu-$y$ karena absis titik-titiknya konstan ($x = 2$). Jarak puncak $2a = 9 - (-1) = 10 \implies a = 5$, sehingga $a^2 = 25$. Jarak antarfokus $2c = 7 - 1 = 6 \implies c = 3$. Nilai $b^2 = a^2 - c^2 = 25 - 9 = 16$. Persamaan elips vertikal adalah $\dfrac{(x - 2)^2}{16} + \dfrac{(y - 4)^2}{25} = 1$.</sub>
- D. $\dfrac{(x - 2)^2}{25} + \dfrac{(y - 4)^2}{16} = 1$  
  <sub>Salah: Tertukar orientasi elips horizontal dan vertikal sehingga posisi penyebut a kuadrat dan b kuadrat terbalik.</sub>

**Pembahasan:** Titik-titik fokus $(2, 1)$ dan $(2, 7)$ memiliki absis sama ($x = 2$), sehingga elips berorientasi vertikal.
Titik pusat elips:
$P(m, n) = \left(2, \dfrac{1 + 7}{2}\right) = (2, 4)$

Jarak titik-titik puncak:
$2a = 9 - (-1) = 10 \implies a = 5 \implies a^2 = 25$

Jarak titik-titik fokus:
$2c = 7 - 1 = 6 \implies c = 3$

Nilai $b^2$:
$b^2 = a^2 - c^2 = 5^2 - 3^2 = 25 - 9 = 16$

Bentuk umum elips vertikal:
$\dfrac{(x - m)^2}{b^2} + \dfrac{(y - n)^2}{a^2} = 1 \implies \dfrac{(x - 2)^2}{16} + \dfrac{(y - 4)^2}{25} = 1$
**Acuan:** siswa — siswa hal.46 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b01-b-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: menentukan persamaan elips dari eksentrisitas*

Persamaan elips yang titik fokusnya terletak pada sumbu-$x$ dan simetris terhadap titik pusat koordinat dengan panjang sumbu mayor $30$ serta nilai eksentrisitas $\dfrac{4}{5}$ adalah ....

- A. $\dfrac{x^2}{81} + \dfrac{y^2}{225} = 1$  
  <sub>Salah: Tertukar menempatkan nilai $a^2$ di bawah $y^2$ dan $b^2$ di bawah $x^2$ (tertukar antara elips vertikal dan horizontal).</sub>
- B. $\dfrac{x^2}{225} + \dfrac{y^2}{369} = 1$  
  <sub>Salah: Salah menggunakan hubungan Pythagoras menjadi $b^2 = a^2 + c^2 = 225 + 144 = 369$.</sub>
- **C. $\dfrac{x^2}{225} + \dfrac{y^2}{81} = 1$** ✅  
  <sub>Benar: Karena simetris terhadap titik asal dan fokus pada sumbu-$x$, pusat elips adalah $O(0,0)$ dan elips horizontal. Panjang sumbu mayor $2a = 30 \implies a = 15$ sehingga $a^2 = 225$. Dari eksentrisitas $e = \dfrac{c}{a} = \dfrac{4}{5}$, diperoleh $c = \dfrac{4}{5} \times 15 = 12$. Nilai $b^2 = a^2 - c^2 = 15^2 - 12^2 = 225 - 144 = 81$. Persamaan elips adalah $\dfrac{x^2}{225} + \dfrac{y^2}{81} = 1$.</sub>
- D. $\dfrac{x^2}{900} + \dfrac{y^2}{324} = 1$  
  <sub>Salah: Menganggap panjang sumbu mayor adalah nilai $a$, bukan $2a$ ($a = 30$, $c = 24$, $b^2 = 324$).</sub>

**Pembahasan:** Diketahui:
- Fokus pada sumbu-$x$ dan simetris terhadap pusat koordinat, sehingga elips horizontal berpusat di $O(0, 0)$.
- Panjang sumbu mayor $2a = 30 \implies a = 15$, maka $a^2 = 225$.
- Eksentrisitas $e = \dfrac{c}{a} = \dfrac{4}{5} \implies c = \dfrac{4}{5}(15) = 12$.

Menentukan nilai $b^2$:
$$b^2 = a^2 - c^2 = 15^2 - 12^2 = 225 - 144 = 81$$

Bentuk baku elips horizontal berpusat di $(0,0)$ adalah:
$$\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1 \implies \dfrac{x^2}{225} + \dfrac{y^2}{81} = 1$$
**Acuan:** siswa — siswa hal.51 Ayo Mencoba 1.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b01-b-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: menentukan koordinat ujung sumbu minor*

Koordinat titik-titik ujung sumbu minor dari elips dengan persamaan $\dfrac{(x - 3)^2}{25} + \dfrac{(y + 1)^2}{169} = 1$ adalah ....

- **A. $(8, -1)$ dan $(-2, -1)$** ✅  
  <sub>Benar: Dari persamaan, penyebut suku $y$ lebih besar dari penyebut suku $x$ ($169 > 25$), sehingga elips berbentuk vertikal dengan titik pusat $(m, n) = (3, -1)$. Nilai $b^2 = 25$ sehingga $b = 5$. Karena sumbu mayor vertikal, sumbu minor sejajar dengan sumbu-$x$, sehingga koordinat ujung-ujung sumbu minor adalah $(m \pm b, n) = (3 \pm 5, -1)$, yaitu $(8, -1)$ dan $(-2, -1)$.</sub>
- B. $(3, 12)$ dan $(3, -14)$  
  <sub>Salah: Siswa tertukar antara sumbu minor dan sumbu mayor, sehingga mencari koordinat titik puncak pada sumbu mayor: $(3, -1 \pm 13)$.</sub>
- C. $(3, 4)$ dan $(3, -6)$  
  <sub>Salah: Siswa mengira elips berbentuk horizontal sehingga menggeser ordinat titik pusat sebesar $b = 5$ bukannya absis: $(3, -1 \pm 5)$.</sub>
- D. $(2, 1)$ dan $(-8, 1)$  
  <sub>Salah: Siswa salah menentukan tanda koordinat titik pusat elips menjadi $(-3, 1)$, lalu menggeser sejajar sumbu-$x$ sebesar $5$: $(-3 \pm 5, 1)$.</sub>

**Pembahasan:** Persamaan elips yang diberikan adalah $\dfrac{(x - 3)^2}{25} + \dfrac{(y + 1)^2}{169} = 1$.
1. Bentuk baku elips vertikal adalah $\dfrac{(x - m)^2}{b^2} + \dfrac{(y - n)^2}{a^2} = 1$ dengan $a^2 > b^2$.
   Diperoleh titik pusat $(m, n) = (3, -1)$, $a^2 = 169$ ($a = 13$), dan $b^2 = 25$ ($b = 5$).
2. Karena sumbu mayor sejajar sumbu-$y$, maka sumbu minor sejajar sumbu-$x$.
3. Koordinat titik-titik ujung sumbu minor diperoleh dengan menggeser absis titik pusat sejauh $b$ satuan ke kanan dan ke kiri:
   $B_1(m + b, n) = (3 + 5, -1) = (8, -1)$
   $B_2(m - b, n) = (3 - 5, -1) = (-2, -1)$
Jadi, koordinat titik-titik ujung sumbu minor elips tersebut adalah $(8, -1)$ dan $(-2, -1)$.
**Acuan:** siswa — siswa hal.36

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b01-b-hard-bt01-001
*orisinal | C5 | 5 langkah | jenis: karakteristik tali busur elips*

Titik $P(x, y)$ bergerak sedemikian rupa sehingga jumlah jaraknya terhadap titik $F_1(-2, 1)$ dan $F_2(6, 1)$ selalu konstan bernilai $10$. Ruas garis vertikal terpanjang yang menghubungkan dua titik pada kurva tersebut memiliki panjang $L_1$, sedangkan ruas garis vertikal yang melalui salah satu fokus dan menghubungkan dua titik pada kurva (*latus rectum*) memiliki panjang $L_2$. Selisih panjang $L_1 - L_2$ adalah ....

- **A. $\dfrac{12}{5}$** ✅  
  <sub>Benar: Jarak kedua fokus $2c = \sqrt{(6 - (-2))^2} = 8 \implies c = 4$. Jumlah jarak konstan $2a = 10 \implies a = 5$. Karena ordinat fokus sama, sumbu mayor horizontal, sehingga $b^2 = a^2 - c^2 = 25 - 16 = 9 \implies b = 3$. Ruas garis vertikal terpanjang adalah sumbu minor dengan panjang $L_1 = 2b = 6$. Panjang latus rectum vertikal adalah $L_2 = \dfrac{2b^2}{a} = \dfrac{2(9)}{5} = \dfrac{18}{5}$. Selisih $L_1 - L_2 = 6 - \dfrac{18}{5} = \dfrac{12}{5}$.</sub>
- B. $\dfrac{16}{5}$  
  <sub>Salah: Siswa lupa mengalikan dua pada rumus latus rectum sehingga menggunakan $\dfrac{b^2}{a} = \dfrac{9}{5}$, menghasilkan selisih $6 - \dfrac{9}{5} = \dfrac{21}{5}$ lalu keliru menghitung menjadi $\dfrac{16}{5}$.</sub>
- C. $\dfrac{7}{5}$  
  <sub>Salah: Siswa mengurangkan setengah sumbu minor dengan latus rectum, yaitu $a - L_2 = 5 - \dfrac{18}{5} = \dfrac{7}{5}$.</sub>
- D. $\dfrac{32}{5}$  
  <sub>Salah: Siswa keliru menganggap garis vertikal terpanjang adalah sumbu mayor $2a = 10$, sehingga menghitung $10 - \dfrac{18}{5} = \dfrac{32}{5}$.</sub>

**Pembahasan:** Berdasarkan definisi elips, kurva yang terbentuk adalah elips dengan titik fokus $F_1(-2, 1)$ dan $F_2(6, 1)$.
1. Sumbu fokus sejajar dengan sumbu-$x$ (ordinat kedua fokus bernilai sama, $y = 1$).
2. Jarak kedua fokus: $2c = 6 - (-2) = 8 \iff c = 4$.
3. Jumlah jarak titik ke kedua fokus adalah $2a = 10 \iff a = 5$.
4. Nilai $b^2 = a^2 - c^2 = 5^2 - 4^2 = 25 - 16 = 9 \iff b = 3$.
5. Ruas garis vertikal yang menghubungkan dua titik pada elips horizontal terpanjang dicapai pada garis yang melalui pusat, yaitu sumbu minor: $L_1 = 2b = 2(3) = 6$.
6. Ruas garis vertikal yang melalui fokus adalah *latus rectum*, dengan panjang: $L_2 = \dfrac{2b^2}{a} = \dfrac{2(9)}{5} = \dfrac{18}{5}$.
7. Maka selisih panjangnya adalah: $L_1 - L_2 = 6 - \dfrac{18}{5} = \dfrac{30 - 18}{5} = \dfrac{12}{5}$.
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b01-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: menentukan persamaan elips dari jarak direktriks dan fokus*

Sebuah elips horizontal memiliki titik pusat $P(1, -2)$. Jika jarak antara kedua garis direktriksnya adalah $18$ dan jarak antara kedua titik fokusnya adalah $8$, persamaan elips tersebut adalah ....

- A. $\dfrac{(x - 1)^2}{20} + \dfrac{(y + 2)^2}{36} = 1$  
  <sub>Salah: Siswa tertukar menempatkan nilai sumbu mayor pada variabel $y$, menghasilkan elips vertikal.</sub>
- **B. $\dfrac{(x - 1)^2}{36} + \dfrac{(y + 2)^2}{20} = 1$** ✅  
  <sub>Benar: Jarak kedua fokus $2c = 8 \implies c = 4$. Jarak kedua direktriks pada elips horizontal adalah $\dfrac{2a^2}{c} = 18 \implies \dfrac{a^2}{4} = 9 \implies a^2 = 36$. Nilai $b^2 = a^2 - c^2 = 36 - 16 = 20$. Dengan pusat $(1, -2)$, persamaan elips adalah $\dfrac{(x - 1)^2}{36} + \dfrac{(y + 2)^2}{20} = 1$.</sub>
- C. $\dfrac{(x + 1)^2}{36} + \dfrac{(y - 2)^2}{20} = 1$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat titik pusat elips $(m, n) = (1, -2)$.</sub>
- D. $\dfrac{(x - 1)^2}{36} + \dfrac{(y + 2)^2}{16} = 1$  
  <sub>Salah: Siswa keliru menggunakan nilai $c^2 = 16$ sebagai $b^2$.</sub>

**Pembahasan:** 1. Jarak antara kedua titik fokus adalah $2c = 8$, sehingga $c = 4$.
2. Persamaan garis direktriks elips horizontal berpusat di $(m, n)$ adalah $x = m \pm \dfrac{a^2}{c}$. Jarak antara kedua garis direktriks adalah:
   $$2 \cdot \dfrac{a^2}{c} = 18 \iff \dfrac{a^2}{c} = 9$$
3. Karena $c = 4$, diperoleh:
   $$a^2 = 9c = 9(4) = 36$$
4. Hitung nilai $b^2$ melalui hubungan dasar elips:
   $$b^2 = a^2 - c^2 = 36 - 4^2 = 36 - 16 = 20$$
5. Karena elips horizontal berpusat di $P(1, -2)$, persamaannya adalah:
   $$\dfrac{(x - 1)^2}{36} + \dfrac{(y - (-2))^2}{20} = 1 \iff \dfrac{(x - 1)^2}{36} + \dfrac{(y + 2)^2}{20} = 1$$
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b01-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: aplikasi pemodelan elips*

Sebuah gerbang masuk cagar budaya dirancang menyerupai setengah elips horizontal dengan lebar dasar $16\text{ meter}$ dan tinggi puncak lengkungan $6\text{ meter}$. Sebuah truk kontainer dengan penampang berbentuk balok yang memiliki lebar $8\text{ meter}$ hendak melintasi tepat di bagian tengah gerbang tersebut. Tinggi maksimum truk kontainer agar dapat melewati gerbang dengan aman adalah ....

- **A. $3\sqrt{3}\text{ meter}$** ✅  
  <sub>Benar: Model elips dengan pusat $(0, 0)$ pada dasar jalan memiliki $a = 8$ dan $b = 6$, persamaannya $\dfrac{x^2}{64} + \dfrac{y^2}{36} = 1$. Kontainer selebar $8\text{ m}$ tepat di tengah dibatasi oleh $x = -4$ hingga $x = 4$. Tinggi maksimum dicapai saat $x = 4$: $\dfrac{16}{64} + \dfrac{y^2}{36} = 1 \implies \dfrac{y^2}{36} = \dfrac{3}{4} \implies y = \sqrt{27} = 3\sqrt{3}\text{ m}$.</sub>
- B. $2\sqrt{6}\text{ meter}$  
  <sub>Salah: Siswa membuat kesalahan dalam menyederhanakan bentuk akar dari $\sqrt{24}$ alih-alih $\sqrt{27}$.</sub>
- C. $4\sqrt{2}\text{ meter}$  
  <sub>Salah: Siswa keliru menukar posisi parameter $a$ dan $b$ dalam pemodelan elips.</sub>
- D. $3\sqrt{2}\text{ meter}$  
  <sub>Salah: Siswa salah melakukan manipulasi pecahan dengan menganggap $1 - \dfrac{1}{4} = \dfrac{1}{2}$ sehingga $y^2 = 18$.</sub>

**Pembahasan:** 1. Letakkan sistem koordinat Cartesius dengan titik pusat $(0, 0)$ berada di tengah-tengah dasar gerbang di permukaan tanah.
2. Lebar dasar gerbang adalah $16\text{ meter}$, sehingga panjang sumbu mayor adalah $2a = 16 \implies a = 8$.
3. Tinggi puncak lengkungan adalah $6\text{ meter}$, sehingga panjang semi-sumbu minor adalah $b = 6$.
4. Persamaan setengah elips bagian atas ($y \ge 0$) adalah:
   $$\dfrac{x^2}{8^2} + \dfrac{y^2}{6^2} = 1 \iff \dfrac{x^2}{64} + \dfrac{y^2}{36} = 1$$
5. Truk kontainer memiliki lebar $8\text{ meter}$ dan melintas tepat di tengah gerbang, sehingga posisi tepi kontainer berada pada rentang $-4 \le x \le 4$. Batas ketinggian gerbang ditentukan pada $x = 4$:
   $$\dfrac{4^2}{64} + \dfrac{y^2}{36} = 1$$
   $$\dfrac{16}{64} + \dfrac{y^2}{36} = 1$$
   $$\dfrac{1}{4} + \dfrac{y^2}{36} = 1 \iff \dfrac{y^2}{36} = \dfrac{3}{4}$$
   $$y^2 = 36 \times \dfrac{3}{4} = 27$$
   $$y = \sqrt{27} = 3\sqrt{3}\text{ meter}$$
Jadi, tinggi maksimum truk kontainer yang diperbolehkan adalah $3\sqrt{3}\text{ meter}$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b01-b-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: aplikasi persamaan lintasan elips*

Sebuah satelit mengitari Bumi dengan lintasan berbentuk elips dan Bumi berada pada salah satu fokusnya. Jarak terdekat satelit ke Bumi adalah $100\text{ mil}$ dan jarak terjauhnya adalah $900\text{ mil}$. Jika pusat lintasan satelit berada pada koordinat $(3, -2)$ dan sumbu mayor elips sejajar dengan sumbu-$x$, persamaan baku elips lintasan satelit tersebut adalah ....

- A. $\dfrac{(x - 3)^2}{90.000} + \dfrac{(y + 2)^2}{250.000} = 1$  
  <sub>Salah: Siswa salah mengasumsikan elips berbentuk vertikal sehingga menukar posisi $a^2$ dan $b^2$.</sub>
- B. $\dfrac{(x + 3)^2}{250.000} + \dfrac{(y - 2)^2}{90.000} = 1$  
  <sub>Salah: Siswa melakukan kesalahan substitusi tanda koordinat pusat $(m, n) = (3, -2)$ pada rumus baku.</sub>
- C. $\dfrac{(x - 3)^2}{250.000} + \dfrac{(y + 2)^2}{160.000} = 1$  
  <sub>Salah: Siswa keliru menggunakan nilai $c^2 = 400^2 = 160.000$ sebagai pengganti nilai $b^2$.</sub>
- **D. $\dfrac{(x - 3)^2}{250.000} + \dfrac{(y + 2)^2}{90.000} = 1$** ✅  
  <sub>Benar: Jarak terdekat $a - c = 100$ dan jarak terjauh $a + c = 900$. Penjumlahan keduanya: $2a = 1000 \implies a = 500 \implies a^2 = 250.000$. Pengurangan keduanya: $2c = 800 \implies c = 400$. Parameter $b^2 = a^2 - c^2 = 250.000 - 160.000 = 90.000$. Dengan pusat $(3, -2)$ dan orientasi horizontal, persamaannya adalah $\dfrac{(x - 3)^2}{250.000} + \dfrac{(y + 2)^2}{90.000} = 1$.</sub>

**Pembahasan:** 1. Pada lintasan elips dengan Bumi di salah satu titik fokus:
   - Jarak terdekat (*perihelion/perigee*): $a - c = 100$
   - Jarak terjauh (*aphelion/apogee*): $a + c = 900$
2. Menentukan nilai $a$ dan $c$:
   $$(a + c) + (a - c) = 900 + 100 \iff 2a = 1.000 \iff a = 500$$
   $$(a + c) - (a - c) = 900 - 100 \iff 2c = 800 \iff c = 400$$
3. Menentukan nilai $a^2$ dan $b^2$:
   $$a^2 = 500^2 = 250.000$$
   $$b^2 = a^2 - c^2 = 500^2 - 400^2 = 250.000 - 160.000 = 90.000$$
4. Titik pusat elips berada di $(m, n) = (3, -2)$ dan sumbu mayor sejajar dengan sumbu-$x$ (elips horizontal), sehingga persamaan bakunya adalah:
   $$\dfrac{(x - m)^2}{a^2} + \dfrac{(y - n)^2}{b^2} = 1$$
   $$\dfrac{(x - 3)^2}{250.000} + \dfrac{(y - (-2))^2}{90.000} = 1 \iff \dfrac{(x - 3)^2}{250.000} + \dfrac{(y + 2)^2}{90.000} = 1$$
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b01-b-hard-bt01-005
*variasi (angka) | C5 | 4 langkah | jenis: persamaan elips menyinggung garis koordinat*

Persamaan elips yang memiliki titik-titik fokus pada koordinat $(-2, 3)$ dan $(-2, 7)$ serta menyinggung sumbu-$y$ adalah ....

- A. $\dfrac{(x + 2)^2}{8} + \dfrac{(y - 5)^2}{4} = 1$  
  <sub>Salah: Tertukar menempatkan sumbu mayor pada variabel x untuk elips vertikal</sub>
- **B. $\dfrac{(x + 2)^2}{4} + \dfrac{(y - 5)^2}{8} = 1$** ✅  
  <sub>Benar: Fokus $(-2, 3)$ dan $(-2, 7)$ memiliki absis sama, sehingga elips vertikal dengan pusat $P(-2, 5)$ dan $2c = 7 - 3 = 4 \implies c = 2$. Karena elips menyinggung sumbu-$y$ ($x = 0$), jarak mendatar dari pusat ke sumbu-$y$ adalah $b = |-2 - 0| = 2$. Pada elips vertikal, $a^2 = b^2 + c^2 = 2^2 + 2^2 = 8$. Persamaannya adalah $\frac{(x+2)^2}{4} + \frac{(y-5)^2}{8} = 1$.</sub>
- C. $\dfrac{(x - 2)^2}{4} + \dfrac{(y + 5)^2}{8} = 1$  
  <sub>Salah: Salah tanda translasi koordinat titik pusat $(-2, 5)$</sub>
- D. $\dfrac{(x + 2)^2}{4} + \dfrac{(y - 5)^2}{6} = 1$  
  <sub>Salah: Salah menghitung $a^2 = b^2 + c = 4 + 2 = 6$</sub>

**Pembahasan:** 1. Menentukan pusat dan orientasi: Kedua fokus memiliki absis sama, yaitu $x = -2$. Sumbu mayor sejajar sumbu-$y$ (elips vertikal). Titik pusat elips berada di tengah kedua fokus: $P\left(-2, \frac{3+7}{2}\right) = (-2, 5)$.
2. Menentukan nilai $c$: Jarak kedua fokus $2c = 7 - 3 = 4 \implies c = 2$.
3. Menentukan nilai $b$: Karena sumbu utama vertikal, sumbu sekawan horizontal sejajar sumbu-$x$. Elips menyinggung sumbu-$y$ ($x = 0$), sehingga jarak horizontal dari titik pusat $(-2, 5)$ ke sumbu-$y$ adalah panjang semi-sumbu minor $b = |0 - (-2)| = 2$, maka $b^2 = 4$.
4. Menentukan nilai $a$: Untuk elips vertikal, $a^2 = b^2 + c^2 = 2^2 + 2^2 = 8$.
5. Persamaan elips: $\dfrac{(x + 2)^2}{4} + \dfrac{(y - 5)^2}{8} = 1$.
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b01-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: persamaan elips dari direktriks dan fokus*

Sebuah elips horizontal memiliki titik pusat $P(2, -3)$ dan jarak antara kedua titik fokusnya adalah $6$. Jika salah satu garis direktriks elips tersebut memiliki persamaan $x = 8$, maka persamaan elips tersebut adalah ....

- **A. $\dfrac{(x - 2)^2}{18} + \dfrac{(y + 3)^2}{9} = 1$** ✅  
  <sub>Benar: Pusat $(m, n) = (2, -3)$ dan jarak kedua fokus $2c = 6 \implies c = 3$. Persamaan garis direktriks elips horizontal berpusat $(m, n)$ di sebelah kanan adalah $x = m + \frac{a^2}{c}$. Karena direktriks $x = 8$, maka $2 + \frac{a^2}{3} = 8 \implies \frac{a^2}{3} = 6 \implies a^2 = 18$. Nilai $b^2 = a^2 - c^2 = 18 - 3^2 = 9$. Persamaan elips adalah $\frac{(x-2)^2}{18} + \frac{(y+3)^2}{9} = 1$.</sub>
- B. $\dfrac{(x - 2)^2}{36} + \dfrac{(y + 3)^2}{27} = 1$  
  <sub>Salah: Keliru mengalikan jarak pusat ke direktriks dengan 2c alih-alih c</sub>
- C. $\dfrac{(x + 2)^2}{18} + \dfrac{(y - 3)^2}{9} = 1$  
  <sub>Salah: Tertukar tanda positif dan negatif koordinat pusat pada bentuk kuadrat</sub>
- D. $\dfrac{(x - 2)^2}{18} + \dfrac{(y + 3)^2}{15} = 1$  
  <sub>Salah: Salah menghitung $b^2 = a^2 - c = 18 - 3 = 15$</sub>

**Pembahasan:** 1. Identifikasi unsur yang diketahui:
Pusat elips $(m, n) = (2, -3)$.
Jarak antarfokus $2c = 6 \implies c = 3$.
2. Gunakan rumus garis direktriks elips horizontal:
Direktriks elips horizontal berpusat di $(m, n)$ adalah $x = m \pm \dfrac{a^2}{c}$.
Karena direktriks yang diketahui $x = 8 > 2$, garis tersebut berada di sebelah kanan pusat, sehingga:
$2 + \dfrac{a^2}{3} = 8$
$\dfrac{a^2}{3} = 6 \implies a^2 = 18$.
3. Hitung nilai $b^2$:
$b^2 = a^2 - c^2 = 18 - 3^2 = 18 - 9 = 9$.
4. Susun persamaan elips horizontal:
$\dfrac{(x - m)^2}{a^2} + \dfrac{(y - n)^2}{b^2} = 1 \implies \dfrac{(x - 2)^2}{18} + \dfrac{(y + 3)^2}{9} = 1$.
**Acuan:** siswa — siswa hal.40

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b01-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: keliling segitiga fokal elips*

Titik $P(x_1, y_1)$ terletak pada elips dengan persamaan $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$ dengan $y_1 \neq 0$. Jika $F_1$ dan $F_2$ adalah kedua titik fokus elips tersebut, keliling segitiga $PF_1F_2$ bernilai tetap yaitu ....

- A. $20$  
  <sub>Salah: Siswa hanya menghitung jumlah jarak titik ke kedua fokus ($2a = 20$) tanpa menambahkan panjang sisi alas segitiga ($F_1F_2$).</sub>
- B. $36$  
  <sub>Salah: Siswa keliru menjumlahkan $2a + 2b = 20 + 16 = 36$ alih-alih melibatkan jarak antarfokus $2c$.</sub>
- **C. $32$** ✅  
  <sub>Benar: Keliling $\triangle PF_1F_2 = PF_1 + PF_2 + F_1F_2$. Berdasarkan definisi elips, $PF_1 + PF_2 = 2a$. Dari persamaan, $a^2 = 100 \implies a = 10$, $b^2 = 64 \implies c = \sqrt{100 - 64} = 6$. Jarak antarfokus $F_1F_2 = 2c = 12$. Maka keliling $= 2a + 2c = 20 + 12 = 32$.</sub>
- D. $26$  
  <sub>Salah: Siswa hanya menjumlahkan $a + b + c = 10 + 8 + 6 = 24$ atau menjumlahkan $2a + c = 26$ karena lupa bahwa jarak kedua fokus adalah $2c$.</sub>

**Pembahasan:** Keliling segitiga $PF_1F_2$ adalah:
$$K = PF_1 + PF_2 + F_1F_2$$

Berdasarkan definisi elips, jumlah jarak sebarang titik pada elips ke kedua titik fokusnya adalah konstan sebesar $2a$:
$$PF_1 + PF_2 = 2a$$

Dari persamaan elips $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$:
- $a^2 = 100 \implies a = 10$
- $b^2 = 64$
- $c = \sqrt{a^2 - b^2} = \sqrt{100 - 64} = \sqrt{36} = 6$

Jarak antara kedua fokus adalah:
$$F_1F_2 = 2c = 2(6) = 12$$

Sehingga keliling segitiga $PF_1F_2$ adalah:
$$K = 2a + 2c = 2(10) + 12 = 20 + 12 = 32$$
**Acuan:** siswa — siswa hal.34

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b01-b-hard-bt01-008
*orisinal | C6 | 5 langkah | jenis: analisis parameter eksentrisitas elips*

Sebuah elips horizontal berpusat di $O(0, 0)$ memiliki karakteristik unik di mana panjang *latus rectum*-nya sama dengan jarak antara kedua titik fokusnya. Nilai eksentrisitas ($e$) dari elips tersebut adalah ....

- A. $\dfrac{1}{2}$  
  <sub>Salah: Siswa mengasumsikan secara keliru bahwa rasio $c/a$ bernilai tepat setengah.</sub>
- B. $\dfrac{\sqrt{5} + 1}{2}$  
  <sub>Salah: Siswa mengambil akar positif rumus kuadrat tanpa memperhatikan syarat bahwa eksentrisitas elips harus $0 < e < 1$ sehingga nilai $> 1$ tidak memenuhi.</sub>
- C. $\dfrac{\sqrt{3} - 1}{2}$  
  <sub>Salah: Siswa salah menghitung diskriminan persamaan kuadrat menjadi $D = 1 + 2 = 3$ alih-alih $D = 1 - 4(1)(-1) = 5$.</sub>
- **D. $\dfrac{\sqrt{5} - 1}{2}$** ✅  
  <sub>Benar: Panjang latus rectum $\dfrac{2b^2}{a} = 2c \implies b^2 = ac$. Karena $b^2 = a^2 - c^2$, maka $a^2 - c^2 = ac \implies a^2 - ac - c^2 = 0$. Bagi dengan $a^2$ menghasilkan $1 - e - e^2 = 0 \implies e^2 + e - 1 = 0$. Dengan rumus kuadrat dan syarat $0 < e < 1$, diperoleh $e = \dfrac{-1 + \sqrt{5}}{2}$.</sub>

**Pembahasan:** Diketahui:
- Panjang *latus rectum* $= \dfrac{2b^2}{a}$
- Jarak kedua fokus $= 2c$

Berdasarkan keterangan soal:
$$\dfrac{2b^2}{a} = 2c \iff b^2 = ac$$

Substitusikan hubungan $b^2 = a^2 - c^2$:
$$a^2 - c^2 = ac \iff a^2 - ac - c^2 = 0$$

Bagi kedua ruas dengan $a^2$ (dengan $a > 0$):
$$1 - \dfrac{c}{a} - \left(\dfrac{c}{a}\right)^2 = 0$$

Karena nilai eksentrisitas adalah $e = \dfrac{c}{a}$:
$$1 - e - e^2 = 0 \iff e^2 + e - 1 = 0$$

Selesaikan persamaan kuadrat untuk $e$:
$$e = \dfrac{-1 \pm \sqrt{1^2 - 4(1)(-1)}}{2(1)} = \dfrac{-1 \pm \sqrt{5}}{2}$$

Karena eksentrisitas elips berada pada rentang $0 < e < 1$, maka nilai yang memenuhi adalah:
$$e = \dfrac{\sqrt{5} - 1}{2}$$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b01-b-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: analisis direktriks dan latus rectum elips*

Sebuah elips horizontal memiliki titik pusat di $P(1, 2)$ dan salah satu titik fokusnya berada di $F(4, 2)$. Jika salah satu garis direktriks dari elips tersebut memiliki persamaan $x = \dfrac{28}{3}$, panjang *latus rectum* elips tersebut adalah ....

- A. $\dfrac{18}{5}$  
  <sub>Salah: Siswa salah menghitung nilai $b^2$ menjadi $a^2 - 2c = 25 - 6 = 19$ atau keliru subtraksi.</sub>
- B. $\dfrac{16}{5}$  
  <sub>Salah: Siswa lupa mengalikan dengan $2$ pada rumus latus rectum (hanya menghitung $\dfrac{b^2}{a}$).</sub>
- **C. $\dfrac{32}{5}$** ✅  
  <sub>Benar: Pusat $(m, n) = (1, 2)$, fokus $(m+c, n) = (4, 2) \implies c = 3$. Garis direktriks elips horizontal berpusat di $(m, n)$ adalah $x = m + \dfrac{a^2}{c} \implies 1 + \dfrac{a^2}{3} = \dfrac{28}{3} \implies \dfrac{a^2}{3} = \dfrac{25}{3} \implies a^2 = 25 \implies a = 5$. Nilai $b^2 = a^2 - c^2 = 25 - 9 = 16$. Maka panjang latus rectum adalah $\dfrac{2b^2}{a} = \dfrac{2(16)}{5} = \dfrac{32}{5}$.</sub>
- D. $\dfrac{64}{5}$  
  <sub>Salah: Siswa mengalikan rumus dengan $4$ alih-alih $2$.</sub>

**Pembahasan:** Dari pusat $P(1, 2)$ dan salah satu fokus $F(4, 2)$:
- Karena ordinatnya sama, elips merupakan elips horizontal.
- Jarak pusat ke fokus: $c = 4 - 1 = 3$.

Persamaan direktriks elips horizontal dengan pusat $(m, n)$ adalah:
$$x = m + \dfrac{a^2}{c}$$
Substitusikan nilai $m = 1$, $c = 3$, dan direktriks $x = \dfrac{28}{3}$:
$$1 + \dfrac{a^2}{3} = \dfrac{28}{3} \implies \dfrac{a^2}{3} = \dfrac{25}{3} \implies a^2 = 25 \implies a = 5$$

Menghitung $b^2$:
$$b^2 = a^2 - c^2 = 25 - 3^2 = 16$$

Panjang *latus rectum*:
$$\text{Panjang } L = \dfrac{2b^2}{a} = \dfrac{2(16)}{5} = \dfrac{32}{5}$$
**Acuan:** siswa — siswa hal.39

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b01-b-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: pemodelan orbit satelit elips*

Sebuah satelit buatan bergerak mengitari sebuah planet dalam lintasan berbentuk elips dengan pusat planet berada di salah satu titik fokusnya. Ketinggian terendah satelit dari permukaan planet adalah $400\text{ km}$ dan ketinggian tertingginya adalah $3.600\text{ km}$. Jika jari-jari planet tersebut adalah $6.000\text{ km}$, nilai eksentrisitas orbit satelit tersebut adalah ....

- A. $0,25$  
  <sub>Salah: Siswa membagi $c$ dengan jarak terdekat $a - c$: $\dfrac{1.600}{6.400} = 0,25$ alih-alih membaginya dengan $a$.</sub>
- **B. $0,20$** ✅  
  <sub>Benar: Jarak terdekat ke pusat planet $r_{\min} = 6.000 + 400 = 6.400\text{ km}$. Jarak terjauh ke pusat planet $r_{\max} = 6.000 + 3.600 = 9.600\text{ km}$. Karena $r_{\min} = a - c$ dan $r_{\max} = a + c$, maka $2a = 16.000 \implies a = 8.000\text{ km}$ dan $2c = 3.200 \implies c = 1.600\text{ km}$. Eksentrisitas $e = \dfrac{c}{a} = \dfrac{1.600}{8.000} = 0,20$.</sub>
- C. $0,16$  
  <sub>Salah: Siswa salah menghitung $c$ sebagai selisih ketinggian dibagi 4 atau salah aritmetika pembagian.</sub>
- D. $0,80$  
  <sub>Salah: Siswa langsung menghitung eksentrisitas dari rasio ketinggian terhadap permukaan tanpa menambahkan jari-jari planet: $\dfrac{3.600 - 400}{3.600 + 400} = \dfrac{3.200}{4.000} = 0,80$.</sub>

**Pembahasan:** Pusat planet merupakan salah satu fokus elips. Jarak diukur dari pusat planet:
- Jarak terdekat (periapsis): 
  $$r_{\min} = R_{\text{planet}} + h_{\min} = 6.000 + 400 = 6.400\text{ km}$$
- Jarak terjauh (apoapsis): 
  $$r_{\max} = R_{\text{planet}} + h_{\max} = 6.000 + 3.600 = 9.600\text{ km}$$

Berdasarkan sifat elips:
$$a - c = 6.400$$
$$a + c = 9.600$$

Jumlahkan kedua persamaan:
$$2a = 16.000 \implies a = 8.000\text{ km}$$

Kurangkan kedua persamaan:
$$2c = 3.200 \implies c = 1.600\text{ km}$$

Nilai eksentrisitas orbit satelit:
$$e = \dfrac{c}{a} = \dfrac{1.600}{8.000} = 0,20$$
**Acuan:** siswa — siswa hal.47

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b01-b-hard-bt01-011
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi persamaan dari parameter fokal*

Diketahui suatu elips berpusat di $O(0,0)$ memiliki nilai eksentrisitas $e = \dfrac{4}{5}$ dan jarak antartitik fokusnya adalah $24$. Jika titik puncak elips tersebut pada sumbu mayor berada pada sumbu-$y$, persamaan elips tersebut yang benar adalah ....

- A. $\dfrac{x^2}{144} + \dfrac{y^2}{225} = 1$  
  <sub>Salah: Menyubstitusikan $c^2 = 144$ sebagai penyebut $x^2$, bukan $b^2$.</sub>
- **B. $\dfrac{x^2}{81} + \dfrac{y^2}{225} = 1$** ✅  
  <sub>Benar: $2c = 24 \implies c = 12$. Dari $e = \dfrac{c}{a} = \dfrac{4}{5}$, diperoleh $a = 15 \implies a^2 = 225$. Karena $b^2 = a^2 - c^2$, diperoleh $b^2 = 225 - 144 = 81$. Karena elips vertikal, persamaannya $\dfrac{x^2}{81} + \dfrac{y^2}{225} = 1$.</sub>
- C. $\dfrac{x^2}{81} + \dfrac{y^2}{144} = 1$  
  <sub>Salah: Menggunakan nilai $c^2$ sebagai pengganti nilai $a^2$.</sub>
- D. $\dfrac{x^2}{225} + \dfrac{y^2}{81} = 1$  
  <sub>Salah: Tertukar orientasi elips menjadi elips horizontal.</sub>

**Pembahasan:** Jarak antarfokus $2c = 24$, sehingga $c = 12$. Eksentrisitas $e = \dfrac{c}{a} = \dfrac{4}{5} \implies a = 15$. Nilai $b^2 = a^2 - c^2 = 15^2 - 12^2 = 81$. Karena titik puncak sumbu mayor berada pada sumbu-$y$, elips berbentuk vertikal dengan persamaan $\dfrac{x^2}{81} + \dfrac{y^2}{225} = 1$.
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b01-b-hard-bt01-012
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi persamaan elips tak berpusat di nol*

Sebuah elips memiliki koordinat titik-titik fokus $F_1(7, -3)$ dan $F_2(-5, -3)$. Jika salah satu titik ujung sumbu minornya adalah $(1, 5)$, persamaan elips tersebut adalah ....

- A. $\dfrac{(x - 1)^2}{64} + \dfrac{(y + 3)^2}{100} = 1$  
  <sub>Salah: Tertukar menetapkan sumbu mayor pada sumbu vertikal.</sub>
- B. $\dfrac{(x + 1)^2}{100} + \dfrac{(y - 3)^2}{64} = 1$  
  <sub>Salah: Salah tanda translasi koordinat pusat $(h, k)$.</sub>
- C. $\dfrac{(x - 1)^2}{100} + \dfrac{(y + 3)^2}{36} = 1$  
  <sub>Salah: Menempatkan nilai $c^2 = 36$ pada penyebut suku $y$ bukan $b^2$.</sub>
- **D. $\dfrac{(x - 1)^2}{100} + \dfrac{(y + 3)^2}{64} = 1$** ✅  
  <sub>Benar: Titik pusat $P = \left(\dfrac{7+(-5)}{2}, -3\right) = (1, -3)$. Jarak fokal $2c = 7 - (-5) = 12 \implies c = 6$. Ujung sumbu minor $(1, 5)$ berjarak $b = 5 - (-3) = 8$ dari pusat, sehingga $b^2 = 64$. Maka $a^2 = b^2 + c^2 = 64 + 36 = 100$. Karena fokus sejajar sumbu-$x$, persamaan elips adalah $\dfrac{(x - 1)^2}{100} + \dfrac{(y + 3)^2}{64} = 1$.</sub>

**Pembahasan:** Pusat elips adalah titik tengah $F_1(7,-3)$ dan $F_2(-5,-3)$, yaitu $(1, -3)$. Jarak antar fokus adalah $12$, sehingga $c = 6$. Jarak pusat ke ujung sumbu minor $(1, 5)$ adalah $b = 8$, sehingga $b^2 = 64$. Nilai $a^2 = b^2 + c^2 = 64 + 36 = 100$. Jadi persamaan elips adalah $\dfrac{(x-1)^2}{100} + \dfrac{(y+3)^2}{64} = 1$.
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b01-b-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: analisis hubungan geometri titik fokus dan minor*

Diketahui elips $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ dengan $a > b > 0$ memiliki fokus $F_1$ dan $F_2$. Titik $B$ adalah salah satu titik puncak pada sumbu minor. Jika $\triangle F_1 B F_2$ membentuk segitiga sama sisi, nilai eksentrisitas $e$ dari elips tersebut adalah ....

- A. $\dfrac{\sqrt{3}}{3}$  
  <sub>Salah: Menggunakan nilai rasio $\tan 30^\circ$ secara keliru.</sub>
- B. $\dfrac{1}{\sqrt{2}}$  
  <sub>Salah: Mengasumsikan segitiga sama kaki siku-siku di $B$ ($a^2 + a^2 = 4c^2$).</sub>
- **C. $\dfrac{1}{2}$** ✅  
  <sub>Benar: Pada elips, jarak $B F_1 = B F_2 = a$, dan jarak $F_1 F_2 = 2c$. Karena segitiga $F_1 B F_2$ sama sisi, maka $F_1 F_2 = B F_1 = a$, sehingga $2c = a$. Oleh karena itu, $e = \dfrac{c}{a} = \dfrac{1}{2}$.</sub>
- D. $\dfrac{\sqrt{3}}{2}$  
  <sub>Salah: Menghitung perbandingan tinggi segitiga $\dfrac{b}{a} = \dfrac{\sqrt{3}}{2}$ dan mengiranya sebagai eksentrisitas.</sub>

**Pembahasan:** Diketahui bahwa $B(0, b)$, $F_1(-c, 0)$, dan $F_2(c, 0)$. Jarak $B F_1 = \sqrt{b^2 + c^2} = a$ dan jarak $F_1 F_2 = 2c$. Agar $\triangle F_1 B F_2$ sama sisi, ketiga sisinya harus sama panjang, yaitu $a = 2c$. Dengan demikian, nilai eksentrisitas $e = \dfrac{c}{a} = \dfrac{c}{2c} = \dfrac{1}{2}$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b01-b-hard-bt01-014
*variasi (angka) | C5 | 4 langkah | jenis: persamaan elips menyinggung sumbu koordinat*

Persamaan elips yang memiliki titik-titik fokus pada koordinat $(3, 2)$ dan $(3, -6)$ serta menyinggung sumbu-$y$ adalah ....

- A. $\dfrac{(x - 3)^2}{9} + \dfrac{(y + 2)^2}{7} = 1$  
  <sub>Salah: Keliru menggunakan hubungan fokus dengan menghitung $a^2 = c^2 - b^2 = 16 - 9 = 7$ alih-alih $a^2 = b^2 + c^2$.</sub>
- B. $\dfrac{(x - 3)^2}{25} + \dfrac{(y + 2)^2}{9} = 1$  
  <sub>Salah: Tertukar antara orientasi elips horizontal dan vertikal sehingga posisi $a^2$ dan $b^2$ terbalik.</sub>
- C. $\dfrac{(x + 3)^2}{9} + \dfrac{(y - 2)^2}{25} = 1$  
  <sub>Salah: Kesalahan tanda aljabar saat memasukkan koordinat titik pusat $(3, -2)$ ke dalam bentuk baku persamaan elips.</sub>
- **D. $\dfrac{(x - 3)^2}{9} + \dfrac{(y + 2)^2}{25} = 1$** ✅  
  <sub>Benar: Kedua fokus memiliki absis yang sama ($x = 3$), sehingga elips berorientasi vertikal. Titik pusat elips berada di tengah kedua fokus, yaitu $\left(3, \dfrac{2 + (-6)}{2}\right) = (3, -2)$. Jarak fokus ke pusat adalah $c = 2 - (-2) = 4$. Karena elips berpusat di $(3, -2)$ dan sumbu minornya horizontal sejajar sumbu-$x$, elips menyinggung sumbu-$y$ ($x = 0$) pada jarak horizontal sebesar $b = |3 - 0| = 3$. Dengan demikian, $b^2 = 9$. Nilai $a^2 = b^2 + c^2 = 9 + 4^2 = 25$. Persamaan elips vertikal tersebut adalah $\dfrac{(x - 3)^2}{9} + \dfrac{(y + 2)^2}{25} = 1$.</sub>

**Pembahasan:** Langkah 1: Menentukan arah sumbu utama. Karena kedua fokus $(3, 2)$ dan $(3, -6)$ memiliki absis sama, elips berbentuk vertikal dengan persamaan baku $\dfrac{(x - m)^2}{b^2} + \dfrac{(y - n)^2}{a^2} = 1$.
Langkah 2: Menghitung koordinat pusat $(m, n) = \left(3, \dfrac{2 + (-6)}{2}\right) = (3, -2)$ dan jarak fokus $c = 2 - (-2) = 4$.
Langkah 3: Menentukan panjang semi-sumbu minor $b$. Karena elips berpusat di $(3, -2)$ dan menyinggung sumbu-$y$ ($x = 0$), jarak terdekat dari pusat ke sumbu-$y$ adalah $b = |3 - 0| = 3$, sehingga $b^2 = 9$.
Langkah 4: Menghitung $a^2 = b^2 + c^2 = 9 + 16 = 25$. Maka, persamaan elips adalah $\dfrac{(x - 3)^2}{9} + \dfrac{(y + 2)^2}{25} = 1$.
**Acuan:** pretest — kelas12_tl-b01-p0053-latihan-soal-elips-2c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b01-b-hard-bt01-015
*variasi (angka) | C5 | 5 langkah | jenis: menentukan persamaan elips dari fokus dan titik sembarang*

Sebuah elips memiliki titik pusat di $(3, -2)$ dan salah satu titik fokusnya adalah $(5, -2)$. Jika elips tersebut melalui titik $(5, 1)$, persamaan elips tersebut adalah ....

- **A. $\dfrac{(x - 3)^2}{16} + \dfrac{(y + 2)^2}{12} = 1$** ✅  
  <sub>Benar: Pusat $(3, -2)$ dan fokus $(5, -2)$ memiliki ordinat sama, sehingga elips horizontal dengan jarak fokal $c = 5 - 3 = 2$ ($c^2 = 4$). Persamaan elips berbentuk $\dfrac{(x - 3)^2}{a^2} + \dfrac{(y + 2)^2}{b^2} = 1$ dengan $b^2 = a^2 - 4$. Substitusi titik $(5, 1)$ menghasilkan $\dfrac{(5 - 3)^2}{a^2} + \dfrac{(1 + 2)^2}{a^2 - 4} = 1 \iff \dfrac{4}{a^2} + \dfrac{9}{a^2 - 4} = 1$. Misalkan $u = a^2$, diperoleh $4(u - 4) + 9u = u(u - 4) \iff u^2 - 17u + 16 = 0$. Faktornya adalah $(u - 16)(u - 1) = 0$. Karena $a^2 > c^2 = 4$, nilai yang memenuhi adalah $a^2 = 16$. Akibatnya $b^2 = 16 - 4 = 12$. Persamaan elips adalah $\dfrac{(x - 3)^2}{16} + \dfrac{(y + 2)^2}{12} = 1$.</sub>
- B. $\dfrac{(x - 3)^2}{16} + \dfrac{(y + 2)^2}{20} = 1$  
  <sub>Salah: Keliru menggunakan relasi $b^2 = a^2 + c^2 = 16 + 4 = 20$ (rumus hiperbola) alih-alih $b^2 = a^2 - c^2$.</sub>
- C. $\dfrac{(x - 3)^2}{12} + \dfrac{(y + 2)^2}{16} = 1$  
  <sub>Salah: Tertukar menetapkan elips sebagai elips vertikal sehingga posisi penyebut $16$ dan $12$ tertukar.</sub>
- D. $\dfrac{(x - 3)^2}{1} + \dfrac{(y + 2)^2}{5} = 1$  
  <sub>Salah: Memilih akar persamaan kuadrat $u = 1$ tanpa memperhatikan syarat batas bahwa $a^2 > c^2 = 4$.</sub>

**Pembahasan:** Langkah 1: Identifikasi orientasi dan nilai $c$. Ordinat pusat $(3, -2)$ dan fokus $(5, -2)$ sama, maka elips horizontal dengan $c = 5 - 3 = 2$ sehingga $c^2 = 4$.
Langkah 2: Gunakan relasi $b^2 = a^2 - c^2 = a^2 - 4$, sehingga persamaan elips adalah $\dfrac{(x - 3)^2}{a^2} + \dfrac{(y + 2)^2}{a^2 - 4} = 1$.
Langkah 3: Substitusikan titik $(5, 1)$ ke dalam persamaan:
$\dfrac{(5 - 3)^2}{a^2} + \dfrac{(1 - (-2))^2}{a^2 - 4} = 1 \iff \dfrac{4}{a^2} + \dfrac{9}{a^2 - 4} = 1$.
Langkah 4: Selesaikan persamaan rasional dengan memisalkan $u = a^2$:
$4(u - 4) + 9u = u^2 - 4u \iff 13u - 16 = u^2 - 4u \iff u^2 - 17u + 16 = 0$.
Diperoleh $u = 16$ atau $u = 1$. Karena $a^2 > c^2 = 4$, maka $a^2 = 16$.
Langkah 5: Hitung $b^2 = a^2 - 4 = 16 - 4 = 12$. Diperoleh persamaan $\dfrac{(x - 3)^2}{16} + \dfrac{(y + 2)^2}{12} = 1$.
**Acuan:** siswa — siswa hal.53 Latihan Soal Elips

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b01-b-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: pemodelan lengkungan elips terapan*

Sebuah terowongan jalan raya dirancang dengan penampang berbentuk setengah elips horizontal dengan tinggi puncak $8\text{ meter}$ dan lebar jalan di dasar terowongan $20\text{ meter}$. Sebuah truk boks bermuatan memiliki lebar kontainer $12\text{ meter}$ dan berjalan tepat di tengah terowongan. Agar bagian atas kontainer truk dapat melintasi terowongan tanpa menyentuh atap lengkungan, batas tinggi maksimum kontainer truk tersebut adalah ....

- A. $4,8\text{ meter}$  
  <sub>Salah: Keliru memasukkan nilai lebar penuh $x = 12$ ke dalam persamaan lengkungan alih-alih separuh lebar $x = 6$ dari titik tengah simetri.</sub>
- B. $5,6\text{ meter}$  
  <sub>Salah: Menggunakan perkiraan interpolasi linier segitiga antara tinggi puncak ($8$) dan ujung dasar ($0$) alih-alih kurva elips.</sub>
- **C. $6,4\text{ meter}$** ✅  
  <sub>Benar: Pusat dasar terowongan diletakkan pada titik asal $O(0, 0)$. Lebar dasar adalah panjang sumbu mayor $2a = 20 \implies a = 10$. Tinggi puncak adalah semi-sumbu minor $b = 8$. Persamaan elips penampang terowongan adalah $\dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$ untuk $y \ge 0$. Karena truk selebar $12\text{ meter}$ berjalan tepat di tengah, sisi terluar kontainer berada pada absis $x = \pm \dfrac{12}{2} = \pm 6$. Ketinggian lengkungan terowongan pada titik terluar tersebut diperoleh dengan menyubstitusikan $x = 6$: $\dfrac{6^2}{100} + \dfrac{y^2}{64} = 1 \implies \dfrac{36}{100} + \dfrac{y^2}{64} = 1 \implies \dfrac{y^2}{64} = \dfrac{64}{100} \implies y^2 = \dfrac{4.096}{100} = 40,96$. Maka, tinggi maksimum adalah $y = \sqrt{40,96} = 6,4\text{ meter}$.</sub>
- D. $5,12\text{ meter}$  
  <sub>Salah: Lupa mengalikan dengan $b^2 = 64$ sebelum menarik akar kuadrat, melainkan langsung mengalikan nilai fraksi dengan tinggi $8$.</sub>

**Pembahasan:** Langkah 1: Membuat model koordinat elips dengan titik pusat dasar di $(0,0)$. Lebar alas $2a = 20\text{ m} \implies a = 10$, dan tinggi lengkungan $b = 8\text{ m}$.
Langkah 2: Menuliskan persamaan lengkungan setengah elips bagian atas: $\dfrac{x^2}{10^2} + \dfrac{y^2}{8^2} = 1 \iff \dfrac{x^2}{100} + \dfrac{y^2}{64} = 1$ dengan $y > 0$.
Langkah 3: Menentukan posisi kritis truk. Karena truk berada di tengah jalan dengan lebar $12\text{ m}$, titik terluar atap boks berada pada jarak $x = \dfrac{12}{2} = 6\text{ m}$ dari pusat.
Langkah 4: Substitusikan $x = 6$ ke persamaan elips:
$\dfrac{36}{100} + \dfrac{y^2}{64} = 1 \iff \dfrac{y^2}{64} = 1 - \dfrac{36}{100} = \dfrac{64}{100}$.
Langkah 5: Selesaikan nilai $y$:
$y^2 = \dfrac{64 \times 64}{100} = \dfrac{4.096}{100} = 40,96 \iff y = \sqrt{40,96} = 6,4\text{ meter}$.
Jadi, tinggi maksimum kontainer truk adalah $6,4\text{ meter}$.
**Acuan:** siswa — siswa hal.51

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b01-b-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: analisis geometri segitiga fokus elips*

Sebuah elips horizontal berpusat di $O(0,0)$ memiliki titik-titik fokus di $F_1(-c, 0)$ dan $F_2(c, 0)$. Salah satu titik puncak pada sumbu minor elips tersebut adalah $B(0, 6)$. Jika ruas garis $F_1B$ tegak lurus terhadap ruas garis $F_2B$, panjang *latus rectum* dari elips tersebut adalah ....

- A. $12\sqrt{2}$  
  <sub>Salah: Siswa salah menggunakan rumus $\frac{2a^2}{b}$ seolah-olah elips vertikal sehingga menghasilkan $\frac{2 \cdot 72}{6} = 24$ lalu dirasionalkan secara keliru menjadi $12\sqrt{2}$.</sub>
- B. $12$  
  <sub>Salah: Siswa mengira panjang latus rectum sama dengan panjang sumbu minor $2b = 12$.</sub>
- **C. $6\sqrt{2}$** ✅  
  <sub>Benar: Karena segitiga $F_1BF_2$ siku-siku di $B$ dan simetris terhadap sumbu-$y$, segitiga $OBF_2$ adalah segitiga siku-siku sama kaki dengan $OF_2 = OB$, sehingga $c = b = 6$. Diperoleh $a^2 = b^2 + c^2 = 36 + 36 = 72$, sehingga $a = \sqrt{72} = 6\sqrt{2}$. Panjang *latus rectum* adalah $\frac{2b^2}{a} = \frac{2 \cdot 36}{6\sqrt{2}} = 6\sqrt{2}$.</sub>
- D. $3\sqrt{2}$  
  <sub>Salah: Siswa lupa mengalikan 2 pada rumus panjang latus rectum sehingga menghitung $\frac{b^2}{a} = \frac{36}{6\sqrt{2}} = 3\sqrt{2}$.</sub>

**Pembahasan:** Diketahui titik puncak sumbu minor adalah $B(0, 6)$, sehingga $b = 6$. Koordinat fokus adalah $F_1(-c, 0)$ dan $F_2(c, 0)$. Karena ruas garis $F_1B$ tegak lurus terhadap ruas garis $F_2B$, maka $\angle F_1BF_2 = 90^\circ$. Oleh karena simetri elips terhadap sumbu-$y$, garis $OB$ membagi $\angle F_1BF_2$ menjadi dua sudut sama besar, yaitu $\angle OBF_2 = 45^\circ$. Dengan demikian, segitiga siku-siku $OBF_2$ adalah segitiga siku-siku sama kaki, yang berarti $c = OF_2 = OB = b = 6$. Selanjutnya, hitung nilai $a^2$:
$$a^2 = b^2 + c^2 = 6^2 + 6^2 = 36 + 36 = 72 \implies a = \sqrt{72} = 6\sqrt{2}$$
Panjang *latus rectum* dari elips horizontal dirumuskan dengan:
$$\text{Panjang } L = \frac{2b^2}{a} = \frac{2 \cdot 36}{6\sqrt{2}} = \frac{72}{6\sqrt{2}} = \frac{12}{\sqrt{2}} = 6\sqrt{2}$$
Jadi, panjang *latus rectum* elips tersebut adalah $6\sqrt{2}$.
**Acuan:** siswa — siswa hal.36

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b01-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: penentuan persamaan elips dari fokus dan direktriks*

Sebuah elips horizontal berpusat di titik $O(0, 0)$ memiliki panjang sumbu minor $12$. Jika jarak antara salah satu titik fokus dengan garis direktriks terdekatnya adalah $9$, persamaan elips tersebut adalah ....

- A. $\dfrac{x^2}{400} + \dfrac{y^2}{144} = 1$  
  <sub>Salah: Siswa menganggap panjang sumbu minor adalah $b = 12$ (bukan $2b = 12$), sehingga $b^2 = 144$, $c = 144/9 = 16$, dan $a^2 = 144 + 256 = 400$.</sub>
- B. $\dfrac{x^2}{20} + \dfrac{y^2}{36} = 1$  
  <sub>Salah: Siswa salah menggunakan rumus hubungan parameter dengan mengurangkan $a^2 = b^2 - c^2 = 36 - 16 = 20$.</sub>
- C. $\dfrac{x^2}{36} + \dfrac{y^2}{52} = 1$  
  <sub>Salah: Siswa tertukar menempatkan nilai $a^2$ dan $b^2$ sehingga menghasilkan persamaan elips vertikal bukan horizontal.</sub>
- **D. $\dfrac{x^2}{52} + \dfrac{y^2}{36} = 1$** ✅  
  <sub>Benar: Panjang sumbu minor $2b = 12 \implies b = 6$, sehingga $b^2 = 36$. Garis direktriks elips horizontal adalah $x = \dfrac{a^2}{c}$ dan fokus terdekatnya adalah $F(c, 0)$, sehingga jarak fokus ke direktriks terdekat adalah $\dfrac{a^2}{c} - c = \dfrac{a^2 - c^2}{c} = \dfrac{b^2}{c}$. Dari $\dfrac{36}{c} = 9$, diperoleh $c = 4$. Selanjutnya, $a^2 = b^2 + c^2 = 36 + 4^2 = 52$. Karena elips horizontal berpusat di $(0,0)$, persamaannya adalah $\dfrac{x^2}{52} + \dfrac{y^2}{36} = 1$.</sub>

**Pembahasan:** Diketahui:
1. Elips horizontal berpusat di $O(0, 0)$.
2. Panjang sumbu minor $= 2b = 12 \iff b = 6 \iff b^2 = 36$.
3. Persamaan direktriks untuk fokus di sebelah kanan ($x = c$) adalah $x = \dfrac{a^2}{c}$.
4. Jarak dari titik fokus $(c, 0)$ ke garis direktriks $x = \dfrac{a^2}{c}$ adalah:
$$d = \frac{a^2}{c} - c = \frac{a^2 - c^2}{c} = \frac{b^2}{c}$$
Diketahui $d = 9$, maka:
$$\frac{36}{c} = 9 \iff c = 4$$
5. Menentukan nilai $a^2$:
$$a^2 = b^2 + c^2 = 36 + 4^2 = 36 + 16 = 52$$
Bentuk baku elips horizontal berpusat di $(0, 0)$ adalah:
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 \iff \frac{x^2}{52} + \frac{y^2}{36} = 1$$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b01-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: evaluasi luas segitiga titik fokus dan elips*

Diberikan elips dengan persamaan $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$. Titik $F_1$ dan $F_2$ merupakan titik-titik fokus dari elips tersebut. Jika titik $P$ terletak pada elips dan tidak berada pada sumbu mayor, maka luas maksimum segitiga $P F_1 F_2$ adalah ....

- **A. $12$** ✅  
  <sub>Benar: Dari persamaan elips, $a^2 = 25$ sehingga $a = 5$, dan $b^2 = 9$ sehingga $b = 3$. Nilai $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = 4$. Jarak kedua fokus sebagai alas segitiga adalah $F_1 F_2 = 2c = 2(4) = 8$. Tinggi segitiga adalah jarak tegak lurus titik $P(x, y)$ ke garis sumbu mayor (sumbu-$x$), yaitu $|y|$. Nilai $|y|$ maksimum pada elips adalah $b = 3$ (tercapai di titik puncak minor). Luas maksimum segitiga adalah $L = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 8 \times 3 = 12$.</sub>
- B. $6$  
  <sub>Salah: Menggunakan jarak fokus ke pusat $c = 4$ sebagai panjang alas segitiga, bukan jarak antarfokus $2c = 8$, sehingga memperoleh $\frac{1}{2} \times 4 \times 3 = 6$.</sub>
- C. $15$  
  <sub>Salah: Menggunakan panjang semi-sumbu mayor $a = 5$ sebagai alas segitiga alih-alih fokus, sehingga menghitung $\frac{1}{2} \times 2a \times b = a \cdot b = 5 \times 3 = 15$.</sub>
- D. $24$  
  <sub>Salah: Lupa mengalikan dengan faktor $\frac{1}{2}$ pada rumus luas segitiga, sehingga menghitung $2c \times b = 8 \times 3 = 24$.</sub>

**Pembahasan:** Diketahui persamaan elips horizontal $\dfrac{x^2}{25} + \dfrac{y^2}{9} = 1$.
1. Tentukan nilai $a$, $b$, dan $c$:
   $a^2 = 25 \implies a = 5$
   $b^2 = 9 \implies b = 3$
   $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = \sqrt{16} = 4$

2. Tentukan panjang alas segitiga $P F_1 F_2$:
   Kedua fokus terletak pada sumbu-$x$ di $F_1(-4, 0)$ dan $F_2(4, 0)$.
   Panjang alas segitiga $= F_1 F_2 = 2c = 2(4) = 8$.

3. Tentukan tinggi maksimum segitiga:
   Tinggi segitiga dari titik $P(x, y)$ ke sumbu-$x$ adalah $|y|$.
   Berdasarkan persamaan elips, nilai $|y|$ terbesar tercapai saat $x = 0$, yaitu $|y| = b = 3$.

4. Hitung luas maksimum:
   $\text{Luas}_{\text{maks}} = \dfrac{1}{2} \times \text{alas} \times \text{tinggi}_{\text{maks}} = \dfrac{1}{2} \times 8 \times 3 = 12$.

Jadi, luas maksimum segitiga $P F_1 F_2$ adalah $12$.
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b01-b-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: analisis geometri segiempat fokal elips*

Sebuah elips horizontal berpusat di titik $O(0, 0)$ memiliki kedua titik fokus $F_1$ dan $F_2$ serta kedua titik puncak pada sumbu minor $B_1$ dan $B_2$. Jika segiempat $F_1 B_1 F_2 B_2$ membentuk sebuah bangun persegi dengan luas $32$, panjang *latus rectum* elips tersebut adalah ....

- A. $4$  
  <sub>Salah: Siswa keliru mengira panjang latus rectum sama dengan nilai setengah sumbu minor ($b = 4$).</sub>
- **B. $4\sqrt{2}$** ✅  
  <sub>Benar: Diagonal-diagonal segiempat $F_1 B_1 F_2 B_2$ terletak pada sumbu koordinat dengan panjang $2c$ dan $2b$. Karena segiempat tersebut merupakan persegi, kedua diagonalnya harus sama panjang, sehingga $2c = 2b \implies c = b$. Luas persegi tersebut adalah $\frac{1}{2} \times d_1 \times d_2 = \frac{1}{2}(2c)(2b) = 2b^2 = 32$, sehingga $b^2 = 16$ dan $b = c = 4$. Nilai $a^2 = b^2 + c^2 = 16 + 16 = 32$, sehingga $a = \sqrt{32} = 4\sqrt{2}$. Dengan demikian, panjang *latus rectum* elips adalah $\dfrac{2b^2}{a} = \dfrac{2(16)}{4\sqrt{2}} = \dfrac{32}{4\sqrt{2}} = 4\sqrt{2}$.</sub>
- C. $8$  
  <sub>Salah: Siswa keliru menganggap panjang latus rectum sama dengan panjang sumbu minor ($2b = 2 \times 4 = 8$).</sub>
- D. $2\sqrt{2}$  
  <sub>Salah: Siswa lupa mengalikan dengan faktor 2 pada rumus panjang latus rectum, sehingga menghitung $\dfrac{b^2}{a} = \dfrac{16}{4\sqrt{2}} = 2\sqrt{2}$.</sub>

**Pembahasan:** 1. Titik fokus elips horizontal berpusat di $(0,0)$ adalah $F_1(-c, 0)$ dan $F_2(c, 0)$, sehingga panjang diagonal horizontalnya adalah $2c$.
2. Titik puncak pada sumbu minor adalah $B_1(0, b)$ dan $B_2(0, -b)$, sehingga panjang diagonal vertikalnya adalah $2b$.
3. Karena kedua diagonal saling tegak lurus di titik $(0,0)$ dan bangun yang terbentuk adalah persegi, maka panjang kedua diagonal harus sama:
   $$2c = 2b \implies c = b$$
4. Luas persegi adalah:
   $$L = \frac{1}{2} \times d_1 \times d_2 = \frac{1}{2}(2c)(2b) = 2b^2 = 32 \implies b^2 = 16 \implies b = 4$$
   Karena $b = c$, maka $c = 4$.
5. Nilai $a^2$ dihitung menggunakan hubungan fokus elips:
   $$a^2 = b^2 + c^2 = 16 + 16 = 32 \implies a = \sqrt{32} = 4\sqrt{2}$$
6. Panjang *latus rectum* elips:
   $$\text{Panjang latus rectum} = \frac{2b^2}{a} = \frac{2(16)}{4\sqrt{2}} = \frac{32}{4\sqrt{2}} = 4\sqrt{2}$$
**Acuan:** siswa — siswa hal.38

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
