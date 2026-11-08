# Lembar koreksi — kelas12_tl SMA12L-B1 subbab D: Persamaan Garis Singgung Lingkaran

59 soal | easy 20, medium 20, hard 19 | variasi 28, orisinal 31
> **Kapasitas kurang (hard): 19 dari kuota 20** — 5 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b01-d-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: PGS titik pada lingkaran pusat (0,0)*

Diketahui titik $B(5, -12)$ terletak pada lingkaran $L \equiv x^2 + y^2 = 169$. Persamaan garis singgung lingkaran $L$ yang melalui titik $B$ adalah ....

- A. $5x + 12y = 169$  
  <sub>Salah: Siswa lupa tanda negatif pada ordinat titik singgung.</sub>
- B. $-12x + 5y = 169$  
  <sub>Salah: Siswa menukar posisi absis dan ordinat pada variabel x dan y.</sub>
- **C. $5x - 12y = 169$** ✅  
  <sub>Benar: Rumus garis singgung lingkaran $x^2+y^2=r^2$ di $(x_1, y_1)$ adalah $x_1x + y_1y = r^2$, sehingga $5x - 12y = 169$.</sub>
- D. $5x - 12y = 13$  
  <sub>Salah: Siswa mengganti $r^2$ dengan $r$ di ruas kanan.</sub>

**Pembahasan:** Persamaan garis singgung pada lingkaran $x^2 + y^2 = r^2$ di titik singgung $(x_1, y_1)$ adalah $x_1x + y_1y = r^2$.
Substitusikan $(x_1, y_1) = (5, -12)$ dan $r^2 = 169$:
$5x + (-12)y = 169 \iff 5x - 12y = 169$.
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b01-d-easy-bt01-002
*variasi (angka) | C2 | 1 langkah | jenis: PGS titik pada lingkaran pusat (0,0)*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 25$ yang melalui titik singgung $P(-4, 3)$ adalah ....

- **A. $-4x + 3y = 25$** ✅  
  <sub>Benar: Prinsip bagi adil menghasilkan $(-4)x + (3)y = 25$.</sub>
- B. $4x + 3y = 25$  
  <sub>Salah: Siswa mengabaikan tanda negatif pada absis titik singgung.</sub>
- C. $3x - 4y = 25$  
  <sub>Salah: Siswa menukar koefisien x dan y.</sub>
- D. $-4x + 3y = 5$  
  <sub>Salah: Siswa menuliskan jari-jari $r=5$ bukan $r^2=25$ pada ruas kanan.</sub>

**Pembahasan:** Prinsip pembagian adil untuk lingkaran $x^2 + y^2 = r^2$ di $(x_1, y_1)$ adalah $x_1x + y_1y = r^2$.
Dengan $(x_1, y_1) = (-4, 3)$ dan $r^2 = 25$:
$(-4)x + (3)y = 25 \iff -4x + 3y = 25$.
**Acuan:** siswa — siswa hal.70 Ayo Mencoba 1.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b01-d-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: PGS dengan gradien tertentu*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 9$ yang memiliki kemiringan $m = 3$ adalah ....

- A. $y = 3x \pm 9\sqrt{10}$  
  <sub>Salah: Siswa mengalikan dengan $r^2 = 9$ bukan $r = 3$.</sub>
- **B. $y = 3x \pm 3\sqrt{10}$** ✅  
  <sub>Benar: Menggunakan rumus $y = mx \pm r\sqrt{m^2+1}$ dengan $r=3$ dan $m=3$ menghasilkan $y = 3x \pm 3\sqrt{10}$.</sub>
- C. $y = 3x \pm \sqrt{10}$  
  <sub>Salah: Siswa lupa mengalikan bentuk akar dengan jari-jari r.</sub>
- D. $y = 3x \pm 3\sqrt{7}$  
  <sub>Salah: Siswa salah menghitung $m^2 - 1$ di dalam akar bukan $m^2 + 1$.</sub>

**Pembahasan:** Persamaan garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$ adalah:
$y = mx \pm r\sqrt{m^2 + 1}$
Dari persamaan $L$, diperoleh $r^2 = 9 \implies r = 3$. Kemiringan $m = 3$.
$y = 3x \pm 3\sqrt{3^2 + 1} = 3x \pm 3\sqrt{10}$.
**Acuan:** siswa — siswa hal.73 Contoh Soal 1.22

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b01-d-easy-bt01-004
*orisinal | C2 | 2 langkah | jenis: PGS titik pada lingkaran pusat (a,b)*

Persamaan garis singgung lingkaran $(x - 1)^2 + (y + 2)^2 = 25$ di titik $T(4, 2)$ adalah ....

- A. $3x + 4y + 20 = 0$  
  <sub>Salah: Siswa salah tanda saat memindahkan konstanta ke ruas kiri.</sub>
- **B. $3x + 4y - 20 = 0$** ✅  
  <sub>Benar: Substitusi titik $(4, 2)$ ke rumus $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$ menghasilkan $3(x - 1) + 4(y + 2) = 25 \iff 3x + 4y - 20 = 0$.</sub>
- C. $4x + 2y - 20 = 0$  
  <sub>Salah: Siswa langsung memakai koordinat titik singgung sebagai koefisien tanpa dikurangi pusat.</sub>
- D. $3x + 4y - 25 = 0$  
  <sub>Salah: Siswa lupa menjumlahkan konstanta dari hasil kali suku aljabar.</sub>

**Pembahasan:** Lingkaran berpusat di $(a, b) = (1, -2)$ dengan $r^2 = 25$.
Titik singgung $(x_1, y_1) = (4, 2)$.
Rumus garis singgung:
$(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$
$(4 - 1)(x - 1) + (2 - (-2))(y + 2) = 25$
$3(x - 1) + 4(y + 2) = 25$
$3x - 3 + 4y + 8 = 25$
$3x + 4y + 5 - 25 = 0$
$3x + 4y - 20 = 0$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b01-d-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: PGS dengan sudut kemiringan*  **[warning validator]**

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 16$ yang membentuk sudut $45^\circ$ terhadap sumbu-$x$ positif adalah ....

- A. $y = -x \pm 4\sqrt{2}$  
  <sub>Salah: Siswa salah menentukan nilai $\tan 45^\circ$ menjadi $-1$.</sub>
- B. $y = x \pm 4$  
  <sub>Salah: Siswa lupa mengalikan dengan faktor $\sqrt{m^2+1}$.</sub>
- C. $y = x \pm 16\sqrt{2}$  
  <sub>Salah: Siswa menggunakan $r^2 = 16$ alih-alih jari-jari $r = 4$.</sub>
- **D. $y = x \pm 4\sqrt{2}$** ✅  
  <sub>Benar: Kemiringan $m = \tan 45^\circ = 1$ dan $r = 4$, sehingga $y = 1x \pm 4\sqrt{1^2+1} = x \pm 4\sqrt{2}$.</sub>

**Pembahasan:** Kemiringan garis singgung dihitung melalui nilai tangen:
$m = \tan 45^\circ = 1$
Dari persamaan lingkaran $x^2 + y^2 = 16$, diperoleh jari-jari $r = \sqrt{16} = 4$.
Persamaan garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$:
$y = mx \pm r\sqrt{m^2 + 1}$
$y = (1)x \pm 4\sqrt{1^2 + 1} = x \pm 4\sqrt{2}$.
**Acuan:** siswa — siswa hal.74
**Warning:** kelas12_tl-b01-d-easy-bt01-005 sangat mirip dengan kelas12_tl-b01-d-easy-bt01-013 (0.86) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b01-d-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: PGS titik pada lingkaran pusat (a,b)*

Diketahui persamaan lingkaran $L \equiv (x - 3)^2 + (y + 1)^2 = 25$. Persamaan garis singgung lingkaran tersebut yang melalui titik $A(3, 4)$ adalah ....

- **A. $y = 4$** ✅  
  <sub>Benar: Substitusi titik $(x_1, y_1) = (3, 4)$ ke rumus pembagian adil $(x - 3)(x_1 - 3) + (y + 1)(y_1 - 1) = 25$ menghasilkan $(x - 3)(0) + (y + 1)(5) = 25$, sehingga $5(y + 1) = 25 \Leftrightarrow y = 4$.</sub>
- B. $y = 6$  
  <sub>Salah: Salah melakukan operasi pembagian dan pengurangan di akhir ($25 / 5 + 1 = 6$ bukannya $5 - 1 = 4$).</sub>
- C. $y = 5$  
  <sub>Salah: Lupa menambahkan suku ordinat pusat, langsung mengambil $y = r$.</sub>
- D. $x = 3$  
  <sub>Salah: Tertukar antara variabel yang koefisiennya nol dengan variabel yang memiliki koefisien.</sub>

**Pembahasan:** Persamaan garis singgung lingkaran $(x - a)^2 + (y - b)^2 = r^2$ di titik $(x_1, y_1)$ adalah:
$$(x - a)(x_1 - a) + (y - b)(y_1 - b) = r^2$$
Substitusikan pusat $(3, -1)$ dan titik $(3, 4)$:
$$(x - 3)(3 - 3) + (y + 1)(4 + 1) = 25$$
$$(x - 3)(0) + (y + 1)(5) = 25$$
$$5(y + 1) = 25$$
$$y + 1 = 5 \implies y = 4$$
**Acuan:** siswa — siswa hal.69 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b01-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: PGS sejajar garis lain*

Persamaan garis singgung pada lingkaran $L \equiv x^2 + y^2 = 5$ yang sejajar dengan garis $g: 2x - y + 7 = 0$ adalah ....

- A. $y = 2x \pm 25$  
  <sub>Salah: Menggunakan $r^2$ bukan $r$ pada rumus garis singgung.</sub>
- B. $y = -\tfrac{1}{2}x \pm 5$  
  <sub>Salah: Menggunakan syarat tegak lurus alih-alih sejajar.</sub>
- C. $y = 2x \pm \sqrt{5}$  
  <sub>Salah: Lupa mengalikan jari-jari dengan faktor $\sqrt{m^2 + 1}$.</sub>
- **D. $y = 2x \pm 5$** ✅  
  <sub>Benar: Gradien garis $g$ adalah $m = 2$. Jari-jari lingkaran $r = \sqrt{5}$. Menggunakan rumus $y = mx \pm r\sqrt{m^2 + 1}$, diperoleh $y = 2x \pm \sqrt{5}\sqrt{2^2 + 1} = 2x \pm 5$.</sub>

**Pembahasan:** Garis $g: 2x - y + 7 = 0 \implies y = 2x + 7$, maka gradien $m = 2$.
Karena sejajar, gradien garis singgung juga $m = 2$.
Lingkaran $x^2 + y^2 = 5$ memiliki pusat $(0, 0)$ dan jari-jari $r = \sqrt{5}$.
Persamaan garis singgung:
$$y = mx \pm r\sqrt{m^2 + 1}$$
$$y = 2x \pm \sqrt{5}\sqrt{2^2 + 1}$$
$$y = 2x \pm \sqrt{5}\sqrt{5}$$
$$y = 2x \pm 5$$
**Acuan:** siswa — siswa hal.74 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b01-d-easy-bt01-008
*variasi (angka) | C1 | 1 langkah | jenis: PGS titik pada lingkaran pusat (0,0)*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 50$ di titik $Q(7, 1)$ adalah ....

- A. $7x - y = 50$  
  <sub>Salah: Salah tanda pada variabel y.</sub>
- B. $7x + y = 25$  
  <sub>Salah: Salah membagi nilai $r^2$ dengan 2.</sub>
- C. $x + 7y = 50$  
  <sub>Salah: Tertukar antara nilai absis dan ordinat titik singgung.</sub>
- **D. $7x + y = 50$** ✅  
  <sub>Benar: Substitusi langsung titik $(x_1, y_1) = (7, 1)$ ke rumus pembagian adil $x_1x + y_1y = r^2$ menghasilkan $7x + y = 50$.</sub>

**Pembahasan:** Titik $Q(7, 1)$ terletak pada lingkaran $x^2 + y^2 = 50$ karena $7^2 + 1^2 = 49 + 1 = 50$.
Persamaan garis singgung di titik $(x_1, y_1)$ pada lingkaran $x^2 + y^2 = r^2$ adalah:
$$x_1x + y_1y = r^2$$
Dengan $(x_1, y_1) = (7, 1)$ dan $r^2 = 50$, diperoleh:
$$7x + 1y = 50 \iff 7x + y = 50$$
**Acuan:** siswa — siswa hal.70 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b01-d-easy-bt01-009
*orisinal | C2 | 2 langkah | jenis: PGS dengan gradien tertentu*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 8$ yang memiliki kemiringan $m = 1$ adalah ....

- **A. $y = x \pm 4$** ✅  
  <sub>Benar: Dengan rumus $y = mx \pm r\sqrt{m^2 + 1}$, dengan $m = 1$ dan $r = \sqrt{8}$, diperoleh $y = x \pm \sqrt{8}\sqrt{1^2 + 1} = x \pm \sqrt{16} = x \pm 4$.</sub>
- B. $y = x \pm 2$  
  <sub>Salah: Salah menghitung nilai $\sqrt{8}\sqrt{2} = \sqrt{16} = 4$ menjadi $2$.</sub>
- C. $y = x \pm 2\sqrt{2}$  
  <sub>Salah: Lupa mengalikan dengan $\sqrt{m^2 + 1}$.</sub>
- D. $y = x \pm 8$  
  <sub>Salah: Menggunakan nilai $r^2$ bukan $r$ di depan akar.</sub>

**Pembahasan:** Lingkaran $x^2 + y^2 = 8$ berpusat di $(0,0)$ dengan jari-jari $r = \sqrt{8} = 2\sqrt{2}$.
Persamaan garis singgung dengan kemiringan $m$ adalah:
$$y = mx \pm r\sqrt{m^2 + 1}$$
Substitusikan $m = 1$ dan $r = \sqrt{8}$:
$$y = 1x \pm \sqrt{8}\sqrt{1^2 + 1}$$
$$y = x \pm \sqrt{8}\sqrt{2}$$
$$y = x \pm \sqrt{16}$$
$$y = x \pm 4$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b01-d-easy-bt01-010
*orisinal | C1 | 2 langkah | jenis: PGS titik pada lingkaran pusat (a,b)*

Persamaan garis singgung lingkaran $(x + 5)^2 + (y - 2)^2 = 9$ di titik $T(-5, 5)$ adalah ....

- A. $y = 1$  
  <sub>Salah: Salah melakukan pengurangan tanda saat memindahkan ruas ($3 - 2 = 1$ alih-alih $3 + 2 = 5$).</sub>
- B. $y = 3$  
  <sub>Salah: Lupa menambahkan nilai ordinat pusat ($b = 2$) setelah menyelesaikan $3(y - 2) = 9$.</sub>
- **C. $y = 5$** ✅  
  <sub>Benar: Substitusi titik $(-5, 5)$ ke rumus $(x - a)(x_1 - a) + (y - b)(y_1 - b) = r^2$ menghasilkan $(x + 5)(-5 + 5) + (y - 2)(5 - 2) = 9 \iff 3(y - 2) = 9 \iff y = 5$.</sub>
- D. $x = -5$  
  <sub>Salah: Mengira variabel yang bernilai nol pada suku pengali adalah variabel yang menjadi persamaan garis.</sub>

**Pembahasan:** Cek titik pada lingkaran:
$$(-5 + 5)^2 + (5 - 2)^2 = 0^2 + 3^2 = 9 \quad \text{(benar pada lingkaran)}$$
Persamaan garis singgung lingkaran $(x - a)(x_1 - a) + (y - b)(y_1 - b) = r^2$:
$$(x + 5)(-5 + 5) + (y - 2)(5 - 2) = 9$$
$$(x + 5)(0) + (y - 2)(3) = 9$$
$$3(y - 2) = 9$$
$$y - 2 = 3 \implies y = 5$$
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b01-d-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: PGS dengan gradien tertentu*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 20$ yang mempunyai kemiringan $-2$ adalah ....

- **A. $y = -2x \pm 10$** ✅  
  <sub>Benar: Menggunakan rumus $y = mx \pm r\sqrt{m^2 + 1}$ dengan $m = -2$ dan $r^2 = 20$, diperoleh $y = -2x \pm \sqrt{20}\sqrt{(-2)^2 + 1} = -2x \pm \sqrt{100} = -2x \pm 10$.</sub>
- B. $y = -2x \pm 2\sqrt{5}$  
  <sub>Salah: Siswa lupa mengalikan jari-jari dengan faktor $\sqrt{m^2 + 1}$.</sub>
- C. $y = -2x \pm 20$  
  <sub>Salah: Siswa tidak mengakarkan nilai konstanta $r^2$ atau salah memasukkan nilai konstanta tanpa akar.</sub>
- D. $y = 2x \pm 10$  
  <sub>Salah: Siswa salah tanda pada gradien garis singgung.</sub>

**Pembahasan:** Persamaan garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$ adalah:
$$y = mx \pm r\sqrt{m^2 + 1}$$
Diketahui $r^2 = 20$ sehingga $r = \sqrt{20}$, dan kemiringan $m = -2$.
$$y = -2x \pm \sqrt{20}\sqrt{(-2)^2 + 1}$$
$$y = -2x \pm \sqrt{20}\sqrt{5}$$
$$y = -2x \pm \sqrt{100}$$
$$y = -2x \pm 10$$
**Acuan:** siswa — siswa hal.73 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b01-d-easy-bt01-012
*variasi (angka) | C2 | 1 langkah | jenis: PGS titik pada lingkaran pusat (0,0)*

Diketahui titik $K(-8, 15)$ terletak pada lingkaran $L \equiv x^2 + y^2 = 289$. Persamaan garis singgung lingkaran $L$ di titik tersebut adalah ....

- A. $8x + 15y = 289$  
  <sub>Salah: Siswa lupa tanda negatif pada absis titik singgung.</sub>
- B. $-8x + 15y = 17$  
  <sub>Salah: Siswa keliru mengganti ruas kanan dengan jari-jari $r$ alih-alih $r^2$.</sub>
- C. $15x - 8y = 289$  
  <sub>Salah: Siswa menukar koordinat absis dan ordinat.</sub>
- **D. $-8x + 15y = 289$** ✅  
  <sub>Benar: Persamaan garis singgung di titik $(x_1, y_1)$ pada $x^2 + y^2 = r^2$ adalah $x_1x + y_1y = r^2$. Dengan $(x_1, y_1) = (-8, 15)$, diperoleh $-8x + 15y = 289$.</sub>

**Pembahasan:** Karena titik $K(-8, 15)$ terletak pada lingkaran $x^2 + y^2 = 289$ ($(-8)^2 + 15^2 = 64 + 225 = 289$), maka persamaan garis singgungnya dapat ditentukan dengan rumus pembagian adil:
$$x_1x + y_1y = r^2$$
$$-8x + 15y = 289$$
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b01-d-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: PGS dengan sudut kemiringan*  **[warning validator]**

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 = 12$ yang membentuk sudut $60^\circ$ terhadap sumbu-$x$ positif adalah ....

- **A. $y = \sqrt{3}x \pm 4\sqrt{3}$** ✅  
  <sub>Benar: Kemiringan $m = \tan 60^\circ = \sqrt{3}$. Dengan $r = \sqrt{12}$, persamaan garis singgungnya adalah $y = \sqrt{3}x \pm \sqrt{12}\sqrt{(\sqrt{3})^2 + 1} = \sqrt{3}x \pm \sqrt{12}\cdot 2 = \sqrt{3}x \pm 4\sqrt{3}$.</sub>
- B. $y = \sqrt{3}x \pm 2\sqrt{3}$  
  <sub>Salah: Siswa lupa mengalikan jari-jari dengan faktor $\sqrt{m^2 + 1}$.</sub>
- C. $y = \frac{1}{3}\sqrt{3}x \pm 4$  
  <sub>Salah: Siswa keliru mengira $\tan 60^\circ = \frac{1}{3}\sqrt{3}$ (tertukar dengan $\tan 30^\circ$).</sub>
- D. $y = \sqrt{3}x \pm 12$  
  <sub>Salah: Siswa langsung memasukkan $r^2$ ke dalam konstanta pergeseran.</sub>

**Pembahasan:** Garis singgung membentuk sudut $60^\circ$ terhadap sumbu-$x$ positif, sehingga gradien garis adalah:
$$m = \tan 60^\circ = \sqrt{3}$$
Lingkaran $x^2 + y^2 = 12$ memiliki jari-jari $r = \sqrt{12} = 2\sqrt{3}$.
Persamaan garis singgung:
$$y = mx \pm r\sqrt{m^2 + 1}$$
$$y = \sqrt{3}x \pm \sqrt{12}\sqrt{(\sqrt{3})^2 + 1}$$
$$y = \sqrt{3}x \pm \sqrt{12}\sqrt{4}$$
$$y = \sqrt{3}x \pm 2\sqrt{12} = \sqrt{3}x \pm 4\sqrt{3}$$
**Acuan:** siswa — siswa hal.74 Contoh Soal
**Warning:** kelas12_tl-b01-d-easy-bt01-005 sangat mirip dengan kelas12_tl-b01-d-easy-bt01-013 (0.86) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b01-d-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: PGS bentuk umum di titik singgung*

Persamaan garis singgung pada lingkaran $L \equiv x^2 + y^2 - 6x + 8y = 0$ di titik $(0, 0)$ adalah ....

- A. $6x - 8y = 0$  
  <sub>Salah: Siswa lupa membagi koefisien $A$ dan $B$ dengan 2.</sub>
- **B. $3x - 4y = 0$** ✅  
  <sub>Benar: Dengan prinsip bagi adil di titik $(0,0)$, $x_1x + y_1y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$ menjadi $-3(x + 0) + 4(y + 0) = 0 \iff -3x + 4y = 0 \iff 3x - 4y = 0$.</sub>
- C. $3x + 4y = 0$  
  <sub>Salah: Siswa salah tanda saat memindahkan suku atau salah tanda koefisien.</sub>
- D. $4x - 3y = 0$  
  <sub>Salah: Siswa menukar koefisien $x$ dan $y$.</sub>

**Pembahasan:** Prinsip pembagian adil untuk lingkaran $x^2 + y^2 + Ax + By + C = 0$ di titik singgung $(x_1, y_1)$ adalah:
$$x_1x + y_1y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$$
Substitusikan titik $(x_1, y_1) = (0, 0)$ serta $A = -6$, $B = 8$, dan $C = 0$:
$$0\cdot x + 0\cdot y - 3(x + 0) + 4(y + 0) = 0$$
$$-3x + 4y = 0$$
$$3x - 4y = 0$$
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b01-d-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: Persamaan garis polar*

Persamaan garis polar lingkaran $L \equiv x^2 + y^2 = 25$ yang ditarik dari titik $T(6, 8)$ di luar lingkaran adalah ....

- A. $8x + 6y = 25$  
  <sub>Salah: Siswa menukar absis dan ordinat titik $T$.</sub>
- **B. $6x + 8y = 25$** ✅  
  <sub>Benar: Persamaan garis polar dari titik $(x_1, y_1)$ terhadap lingkaran $x^2 + y^2 = r^2$ adalah $x_1x + y_1y = r^2$, sehingga menghasilkan $6x + 8y = 25$.</sub>
- C. $6x - 8y = 25$  
  <sub>Salah: Siswa salah memberi tanda minus pada ordinat.</sub>
- D. $6x + 8y = 5$  
  <sub>Salah: Siswa menuliskan jari-jari $r$ alih-alih $r^2$ pada ruas kanan.</sub>

**Pembahasan:** Persamaan garis polar (kutub) untuk lingkaran $x^2 + y^2 = r^2$ yang ditarik dari titik $T(x_1, y_1)$ di luar lingkaran dirumuskan dengan:
$$x_1x + y_1y = r^2$$
Dengan $(x_1, y_1) = (6, 8)$ dan $r^2 = 25$, diperoleh persamaan garis polar:
$$6x + 8y = 25$$
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b01-d-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: PGS titik pada lingkaran pusat (a,b)*

Diketahui persamaan lingkaran $L \equiv (x - 1)^2 + (y - 6)^2 = 36$. Persamaan garis singgung lingkaran tersebut yang melalui titik $A(7, 6)$ adalah ....

- A. $y = 6$  
  <sub>Salah: Siswa tertukar antara variabel $x$ dan $y$ saat menyederhanakan suku yang bernilai nol.</sub>
- **B. $x = 7$** ✅  
  <sub>Benar: Substitusi titik $(7,6)$ ke persamaan bagi adil: $(x - 1)(7 - 1) + (y - 6)(6 - 6) = 36 \iff 6(x - 1) = 36 \iff x - 1 = 6 \iff x = 7$.</sub>
- C. $x + y = 13$  
  <sub>Salah: Siswa salah menerapkan rumus bagi adil dengan langsung menjumlahkan koordinat titik.</sub>
- D. $x = 6$  
  <sub>Salah: Siswa salah menjumlahkan hasil bagi sehingga memperoleh $x = 6$ bukannya $x = 7$.</sub>

**Pembahasan:** Titik $A(7, 6)$ terletak pada lingkaran karena $(7 - 1)^2 + (6 - 6)^2 = 6^2 + 0 = 36$.
Berdasarkan prinsip pembagian adil, persamaan garis singgung di titik $(x_1, y_1)$ adalah:
$$(x - a)(x_1 - a) + (y - b)(y_1 - b) = r^2$$
$$(x - 1)(7 - 1) + (y - 6)(6 - 6) = 36$$
$$6(x - 1) + 0 = 36$$
$$x - 1 = 6$$
$$x = 7$$
Jadi, persamaan garis singgungnya adalah $x = 7$.
**Acuan:** siswa — siswa hal.69 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b01-d-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: PGS bentuk umum di titik singgung*

Persamaan garis singgung lingkaran $L \equiv x^2 + y^2 - 4x + 6y - 12 = 0$ di titik $A(5, 1)$ adalah ....

- A. $5x + y - 12 = 0$  
  <sub>Salah: Siswa lupa membagi adil suku linear $-4x$ dan $+6y$.</sub>
- B. $3x + 4y + 19 = 0$  
  <sub>Salah: Siswa salah tanda saat mengoperasikan konstanta $-10 + 3 - 12$.</sub>
- **C. $3x + 4y - 19 = 0$** ✅  
  <sub>Benar: Prinsip bagi adil: $x_1x + y_1y - 2(x + x_1) + 3(y + y_1) - 12 = 0 \iff 5x + y - 2(x + 5) + 3(y + 1) - 12 = 0 \iff 3x + 4y - 19 = 0$.</sub>
- D. $7x + 2y - 19 = 0$  
  <sub>Salah: Siswa salah tanda saat mendistribusikan suku $-2(x + 5)$ menjadi $+2x$.</sub>

**Pembahasan:** Titik $A(5, 1)$ terletak pada lingkaran $L$ karena $5^2 + 1^2 - 4(5) + 6(1) - 12 = 25 + 1 - 20 + 6 - 12 = 0$.
Dengan prinsip pembagian adil:
$$x_1x + y_1y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$$
$$5x + 1y - 2(x + 5) + 3(y + 1) - 12 = 0$$
$$5x + y - 2x - 10 + 3y + 3 - 12 = 0$$
$$3x + 4y - 19 = 0$$
Jadi, persamaan garis singgungnya adalah $3x + 4y - 19 = 0$.
**Acuan:** siswa — siswa hal.69 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b01-d-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: PGS tegak lurus garis lain*

Persamaan garis singgung pada lingkaran $L \equiv x^2 + y^2 = 20$ yang tegak lurus terhadap garis $h: 2x + y - 3 = 0$ adalah ....

- A. $y = -2x \pm 5$  
  <sub>Salah: Siswa menggunakan gradien garis $h$ secara langsung tanpa membalik tandanya untuk garis tegak lurus.</sub>
- B. $y = -\frac{1}{2}x \pm 5$  
  <sub>Salah: Siswa lupa mengalikan dengan $-1$ saat mencari lawan kebalikan dari gradien garis $h$.</sub>
- **C. $y = \frac{1}{2}x \pm 5$** ✅  
  <sub>Benar: Gradien garis $h$ adalah $m_h = -2$. Karena tegak lurus, kemiringan garis singgung $m = \frac{1}{2}$. Rumus $y = mx \pm r\sqrt{m^2+1} = \frac{1}{2}x \pm \sqrt{20}\sqrt{\frac{1}{4}+1} = \frac{1}{2}x \pm \sqrt{25} = \frac{1}{2}x \pm 5$.</sub>
- D. $y = \frac{1}{2}x \pm 10$  
  <sub>Salah: Siswa keliru mengalikan nilai di dalam akar dengan 2.</sub>

**Pembahasan:** Garis $h: 2x + y - 3 = 0 \iff y = -2x + 3$, sehingga gradien $m_h = -2$.
Karena garis singgung tegak lurus dengan garis $h$:
$$m \cdot m_h = -1 \implies m(-2) = -1 \implies m = \frac{1}{2}$$
Lingkaran $x^2 + y^2 = 20$ memiliki jari-jari $r = \sqrt{20}$.
Persamaan garis singgung lingkaran dengan gradien $m$ adalah:
$$y = mx \pm r\sqrt{m^2 + 1}$$
$$y = \frac{1}{2}x \pm \sqrt{20}\sqrt{\left(\frac{1}{2}\right)^2 + 1}$$
$$y = \frac{1}{2}x \pm \sqrt{20}\sqrt{\frac{5}{4}}$$
$$y = \frac{1}{2}x \pm \sqrt{25}$$
$$y = \frac{1}{2}x \pm 5$$
Jadi, persamaan garis singgungnya adalah $y = \frac{1}{2}x \pm 5$.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b01-d-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: PGS sejajar garis lain*

Persamaan garis singgung pada lingkaran $L \equiv x^2 + y^2 = 18$ yang sejajar dengan garis $g: 7x - y + 9 = 0$ adalah ....

- A. $y = 7x \pm 12\sqrt{6}$  
  <sub>Salah: Siswa salah menggunakan rumus di dalam akar menjadi $\sqrt{m^2-1}$ alih-alih $\sqrt{m^2+1}$.</sub>
- B. $y = -7x \pm 30$  
  <sub>Salah: Siswa salah menentukan tanda gradien dari garis sejajar menjadi $m = -7$.</sub>
- C. $y = 7x \pm 90\sqrt{2}$  
  <sub>Salah: Siswa tidak menarik akar dari $r^2 = 18$, melainkan langsung mengalikan $18$ dengan $\sqrt{m^2+1}$.</sub>
- **D. $y = 7x \pm 30$** ✅  
  <sub>Benar: Gradien garis $g$ adalah $m = 7$. Garis singgung sejajar sehingga gradiennya sama ($m = 7$). Dengan $r = \sqrt{18}$, diperoleh $y = mx \pm r\sqrt{m^2+1} = 7x \pm \sqrt{18(49+1)} = 7x \pm \sqrt{900} = 7x \pm 30$.</sub>

**Pembahasan:** Garis $g: 7x - y + 9 = 0 \iff y = 7x + 9$ memiliki gradien $m = 7$.
Karena garis singgung sejajar dengan garis $g$, kemiringan garis singgung adalah $m = 7$.

Lingkaran $L \equiv x^2 + y^2 = 18$ berpusat di $(0,0)$ dengan jari-jari $r = \sqrt{18}$.

Persamaan garis singgung dengan gradien $m$ adalah:
$$y = mx \pm r\sqrt{m^2 + 1}$$
$$y = 7x \pm \sqrt{18}\sqrt{7^2 + 1}$$
$$y = 7x \pm \sqrt{18}\sqrt{50}$$
$$y = 7x \pm \sqrt{900}$$
$$y = 7x \pm 30$$

Jadi, persamaan garis singgungnya adalah $y = 7x \pm 30$.
**Acuan:** siswa — siswa hal.74 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b01-d-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: Persamaan garis polar*

Persamaan garis polar lingkaran $L \equiv (x - 2)^2 + (y - 3)^2 = 25$ yang ditarik dari titik $T(7, 5)$ di luar lingkaran adalah ....

- A. $2x + 5y - 41 = 0$  
  <sub>Salah: Siswa tertukar memasukkan nilai absis dan ordinat titik $T(7, 5)$ ke rumus garis polar.</sub>
- B. $5x + 2y - 9 = 0$  
  <sub>Salah: Siswa salah memindahkan ruas konstanta, yaitu $25 - 16 = 9$ bukannya $25 + 16 = 41$.</sub>
- **C. $5x + 2y - 41 = 0$** ✅  
  <sub>Benar: Menggunakan rumus garis polar $(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$ menghasilkan $(7 - 2)(x - 2) + (5 - 3)(y - 3) = 25 \Leftrightarrow 5(x - 2) + 2(y - 3) = 25 \Leftrightarrow 5x + 2y - 41 = 0$.</sub>
- D. $5x + 2y - 25 = 0$  
  <sub>Salah: Siswa mengabaikan konstanta hasil perkalian suku di dalam kurung dan langsung menyamakannya dengan 25.</sub>

**Pembahasan:** Persamaan garis polar lingkaran $(x - a)^2 + (y - b)^2 = r^2$ dari titik $T(x_1, y_1)$ dirumuskan sebagai:
$$(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$$

Diketahui $a = 2$, $b = 3$, $r^2 = 25$, serta titik $T(7, 5)$ sehingga $x_1 = 7$ dan $y_1 = 5$.

Substitusikan nilai-nilai tersebut ke rumus garis polar:
$$\begin{aligned} (7 - 2)(x - 2) + (5 - 3)(y - 3) &= 25 \\ 5(x - 2) + 2(y - 3) &= 25 \\ 5x - 10 + 2y - 6 &= 25 \\ 5x + 2y - 16 &= 25 \\ 5x + 2y - 41 &= 0 \end{aligned}$$

Jadi, persamaan garis polar lingkaran tersebut adalah $5x + 2y - 41 = 0$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b01-d-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: titik pada lingkaran berabsis diketahui*

Salah satu persamaan garis singgung lingkaran $L \equiv (x - 2)^2 + (y + 3)^2 = 25$ di titik yang berabsis $5$ adalah ....

- **A. $3x + 4y - 19 = 0$** ✅  
  <sub>Benar: Substitusi $x = 5$ ke lingkaran menghasilkan $(5-2)^2 + (y+3)^2 = 25 \iff 9 + (y+3)^2 = 25 \iff (y+3)^2 = 16 \iff y = 1$ atau $y = -7$. Garis singgung di $(5, 1)$ adalah $(5-2)(x-2) + (1+3)(y+3) = 25 \iff 3x - 6 + 4y + 12 = 25 \iff 3x + 4y - 19 = 0$.</sub>
- B. $5x + y - 25 = 0$  
  <sub>Salah: Menerapkan rumus garis singgung di pusat $(0,0)$ yaitu $x_1 x + y_1 y = r^2$ secara langsung.</sub>
- C. $3x + 4y - 25 = 0$  
  <sub>Salah: Lupa menambahkan konstanta hasil kali suku $(-6 + 12)$ ke ruas kiri.</sub>
- D. $3x - 4y - 19 = 0$  
  <sub>Salah: Salah tanda pada faktor $(y + 3)$ saat menerapkan pembagian adil.</sub>

**Pembahasan:** Substitusikan $x = 5$ ke persamaan lingkaran:
$$(5 - 2)^2 + (y + 3)^2 = 25$$
$$9 + (y + 3)^2 = 25$$
$$(y + 3)^2 = 16 \iff y + 3 = \pm 4$$
Diperoleh $y = 1$ atau $y = -7$. Titik singgungnya adalah $(5, 1)$ dan $(5, -7)$.

Persamaan garis singgung di titik $(5, 1)$ menggunakan prinsip pembagian adil:
$$(x_1 - 2)(x - 2) + (y_1 + 3)(y + 3) = 25$$
$$(5 - 2)(x - 2) + (1 + 3)(y + 3) = 25$$
$$3(x - 2) + 4(y + 3) = 25$$
$$3x - 6 + 4y + 12 = 25$$
$$3x + 4y - 19 = 0$$

Opsi yang tersedia memuat persamaan $3x + 4y - 19 = 0$.
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b01-d-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: garis singgung tegak lurus*

Salah satu persamaan garis singgung pada lingkaran $L \equiv (x - 1)^2 + (y + 2)^2 = 10$ yang tegak lurus terhadap garis $g: x - 3y + 5 = 0$ adalah ....

- A. $3x - y - 11 = 0$  
  <sub>Salah: Salah tanda koefisien $y$ saat memindahkan ruas persamaan.</sub>
- B. $3x + y - 9 = 0$  
  <sub>Salah: Kesalahan tanda konstanta saat memindahkan ruas $y + 2 = -3x + 3 - 10$.</sub>
- C. $x - 3y - 17 = 0$  
  <sub>Salah: Menggunakan gradien sejajar $m = \frac{1}{3}$ alih-alih gradien garis tegak lurus.</sub>
- **D. $3x + y - 11 = 0$** ✅  
  <sub>Benar: Kemiringan garis $g$ adalah $m_g = \frac{1}{3}$. Karena tegak lurus, kemiringan garis singgung $m = -3$. Pusat lingkaran $(1, -2)$ dan $r = \sqrt{10}$. Persamaan garis singgung: $y - b = m(x - a) \pm r\sqrt{m^2 + 1} \iff y + 2 = -3(x - 1) \pm \sqrt{10}\sqrt{(-3)^2 + 1} \iff y + 2 = -3x + 3 \pm 10 \iff 3x + y - 1 \pm 10 = 0$. Garisnya adalah $3x + y + 9 = 0$ atau $3x + y - 11 = 0$.</sub>

**Pembahasan:** 1. Tentukan kemiringan garis singgung:
Garis $g: x - 3y + 5 = 0 \iff y = \frac{1}{3}x + \frac{5}{3}$, sehingga $m_g = \frac{1}{3}$.
Karena tegak lurus, maka $m \cdot m_g = -1 \iff m = -3$.

2. Identifikasi parameter lingkaran:
Lingkaran $(x - 1)^2 + (y + 2)^2 = 10$ memiliki pusat $(a, b) = (1, -2)$ dan jari-jari $r = \sqrt{10}$.

3. Substitusi ke rumus persamaan garis singgung:
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - (-2) = -3(x - 1) \pm \sqrt{10}\sqrt{(-3)^2 + 1}$$
$$y + 2 = -3x + 3 \pm \sqrt{10}\cdot\sqrt{10}$$
$$y + 2 = -3x + 3 \pm 10$$
$$3x + y - 1 \pm 10 = 0$$

Diperoleh dua persamaan garis singgung:
- $3x + y + 9 = 0$
- $3x + y - 11 = 0$
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b01-d-medium-bt01-003
*orisinal | C4 | 4 langkah | jenis: garis singgung sejajar garis*

Persamaan salah satu garis singgung pada lingkaran $L \equiv x^2 + y^2 - 4x + 2y - 20 = 0$ yang sejajar dengan garis $3x - 4y + 7 = 0$ adalah ....

- **A. $3x - 4y + 15 = 0$** ✅  
  <sub>Benar: Bentuk baku lingkaran: $(x - 2)^2 + (y + 1)^2 = 20 + 2^2 + (-1)^2 = 25$, sehingga pusat $(2, -1)$ dan $r = 5$. Gradien garis $3x - 4y + 7 = 0$ adalah $m = \frac{3}{4}$. Garis singgung: $y - (-1) = \frac{3}{4}(x - 2) \pm 5\sqrt{\left(\frac{3}{4}\right)^2 + 1} \iff 4(y + 1) = 3(x - 2) \pm 25 \iff 4y + 4 = 3x - 6 \pm 25 \iff 3x - 4y - 10 \pm 25 = 0$, yaitu $3x - 4y + 15 = 0$ atau $3x - 4y - 35 = 0$.</sub>
- B. $3x - 4y + 25 = 0$  
  <sub>Salah: Lupa mengalikan dan menggabungkan konstanta dari pusat $(-6 - 4 = -10)$.</sub>
- C. $4x + 3y + 15 = 0$  
  <sub>Salah: Menggunakan gradien garis tegak lurus $-\frac{4}{3}$ alih-alih gradien garis sejajar.</sub>
- D. $3x - 4y - 15 = 0$  
  <sub>Salah: Salah menghitung $-10 + 25$ menjadi $-15$ karena tertukar tanda.</sub>

**Pembahasan:** 1. Ubah persamaan lingkaran ke bentuk baku:
$$x^2 + y^2 - 4x + 2y - 20 = 0$$
$$(x - 2)^2 + (y + 1)^2 = 20 + 2^2 + (-1)^2 = 25$$
Pusat lingkaran $P(2, -1)$ dan jari-jari $r = \sqrt{25} = 5$.

2. Tentukan gradien:
Garis $3x - 4y + 7 = 0 \iff y = \frac{3}{4}x + \frac{7}{4}$, sehingga $m = \frac{3}{4}$.
Karena sejajar, gradien garis singgung juga $m = \frac{3}{4}$.

3. Terapkan rumus garis singgung bergradien $m$:
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - (-1) = \frac{3}{4}(x - 2) \pm 5\sqrt{\left(\frac{3}{4}\right)^2 + 1}$$
$$y + 1 = \frac{3}{4}(x - 2) \pm 5\left(\frac{5}{4}\right)$$
Kalikan kedua ruas dengan $4$:
$$4(y + 1) = 3(x - 2) \pm 25$$
$$4y + 4 = 3x - 6 \pm 25$$
$$3x - 4y - 10 \pm 25 = 0$$

Diperoleh dua persamaan garis singgung:
- $3x - 4y - 10 + 25 = 0 \iff 3x - 4y + 15 = 0$
- $3x - 4y - 10 - 25 = 0 \iff 3x - 4y - 35 = 0$

Salah satu persamaan yang terdapat pada pilihan adalah $3x - 4y + 15 = 0$.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b01-d-medium-bt01-004
*variasi (angka) | C3 | 2 langkah | jenis: lingkaran menyinggung garis*

Persamaan lingkaran yang berpusat di titik $P(-1, 4)$ dan menyinggung garis $l: 5x + 12y + 9 = 0$ adalah ....

- **A. $(x + 1)^2 + (y - 4)^2 = 16$** ✅  
  <sub>Benar: Jari-jari lingkaran adalah jarak titik $P(-1, 4)$ ke garis $5x + 12y + 9 = 0$:
$r = \frac{|5(-1) + 12(4) + 9|}{\sqrt{5^2 + 12^2}} = \frac{|-5 + 48 + 9|}{\sqrt{169}} = \frac{52}{13} = 4$.
Persamaan lingkaran dengan pusat $(-1, 4)$ dan $r = 4$ adalah $(x + 1)^2 + (y - 4)^2 = 4^2 = 16$.</sub>
- B. $(x + 1)^2 + (y - 4)^2 = 4$  
  <sub>Salah: Lupa menguadratkan jari-jari pada ruas kanan persamaan lingkaran.</sub>
- C. $(x + 1)^2 + (y - 4)^2 = 25$  
  <sub>Salah: Kesalahan perhitungan pembilang saat menghitung jarak titik ke garis sehingga diperoleh $r = 5$.</sub>
- D. $(x - 1)^2 + (y + 4)^2 = 16$  
  <sub>Salah: Tertukar tanda koordinat pusat pada persamaan lingkaran.</sub>

**Pembahasan:** Langkah 1: Tentukan jari-jari lingkaran ($r$) dengan menghitung jarak dari titik pusat $P(-1, 4)$ ke garis $5x + 12y + 9 = 0$:
$$r = \frac{|Ax_1 + By_1 + C|}{\sqrt{A^2 + B^2}} = \frac{|5(-1) + 12(4) + 9|}{\sqrt{5^2 + 12^2}} = \frac{|-5 + 48 + 9|}{\sqrt{169}} = \frac{52}{13} = 4$$

Langkah 2: Susun persamaan lingkaran dengan pusat $(-1, 4)$ dan jari-jari $r = 4$:
$$(x - a)^2 + (y - b)^2 = r^2$$
$$(x - (-1))^2 + (y - 4)^2 = 4^2$$
$$(x + 1)^2 + (y - 4)^2 = 16$$
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b01-d-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: lingkaran menyinggung sumbu koordinat*

Diketahui lingkaran $L \equiv x^2 + y^2 - 12x + ky + 36 = 0$. Nilai $k$ yang memenuhi agar lingkaran tersebut menyinggung sumbu-$y$ adalah ....

- A. $k = 12$ saja  
  <sub>Salah: Lupa bahwa persamaan kuadrat murni $k^2 = 144$ memiliki dua solusi simetris (positif dan negatif).</sub>
- B. $k = 6$ atau $k = -6$  
  <sub>Salah: Hanya menghitung $\sqrt{36}$ tanpa mengalikan dengan faktor 4 pada diskriminan.</sub>
- C. $k = 24$ atau $k = -24$  
  <sub>Salah: Mengalikan dengan 2 bukan mengambil akar kuadrat dari 144.</sub>
- **D. $k = 12$ atau $k = -12$** ✅  
  <sub>Benar: Sumbu-$y$ memiliki persamaan $x = 0$. Substitusikan ke persamaan lingkaran:
$0^2 + y^2 - 12(0) + ky + 36 = 0 \implies y^2 + ky + 36 = 0$.
Agar garis menyinggung lingkaran, nilai diskriminan persamaan kuadrat harus sama dengan nol:
$D = k^2 - 4(1)(36) = 0 \implies k^2 - 144 = 0 \implies k = \pm 12$.</sub>

**Pembahasan:** Langkah 1: Substitusikan persamaan sumbu-$y$, yaitu $x = 0$, ke dalam persamaan lingkaran:
$$x^2 + y^2 - 12x + ky + 36 = 0$$
$$y^2 + ky + 36 = 0$$

Langkah 2: Syarat menyinggung adalah nilai diskriminan $D = 0$:
$$D = b^2 - 4ac = 0$$
$$k^2 - 4(1)(36) = 0$$
$$k^2 - 144 = 0$$
$$k^2 = 144$$
$$k = 12 \text{ atau } k = -12$$
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b01-d-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: garis singgung gradien diketahui*

Salah satu persamaan garis singgung lingkaran $L \equiv (x + 2)^2 + (y - 5)^2 = 20$ yang memiliki kemiringan $m = 2$ adalah ....

- A. $2x - y + 9 = 0$  
  <sub>Salah: Lupa menjumlahkan konstanta dari penguraian $m(x - a)$ yaitu $2(2) = 4$.</sub>
- **B. $2x - y + 19 = 0$** ✅  
  <sub>Benar: Dari persamaan lingkaran diperoleh $a = -2$, $b = 5$, dan $r = \sqrt{20}$.
Kemiringan $m = 2$.
Rumus garis singgung: $y - b = m(x - a) \pm r\sqrt{m^2 + 1}$
$y - 5 = 2(x + 2) \pm \sqrt{20}\sqrt{2^2 + 1}$
$y - 5 = 2x + 4 \pm \sqrt{20}\sqrt{5}$
$y - 5 = 2x + 4 \pm 10$
Untuk tanda positif: $y - 5 = 2x + 14 \implies 2x - y + 19 = 0$.</sub>
- C. $2x - y + 11 = 0$  
  <sub>Salah: Salah tanda koordinat titik pusat saat substitusi ke rumus garis singgung.</sub>
- D. $2x - y - 19 = 0$  
  <sub>Salah: Salah memindahkan ruas suku-suku persamaan garis.</sub>

**Pembahasan:** Langkah 1: Identifikasi parameter lingkaran dari $(x + 2)^2 + (y - 5)^2 = 20$:
$$a = -2, \quad b = 5, \quad r = \sqrt{20}$$
Diketahui kemiringan garis singgung $m = 2$.

Langkah 2: Hitung nilai batas $r\sqrt{m^2 + 1}$:
$$r\sqrt{m^2 + 1} = \sqrt{20}\sqrt{2^2 + 1} = \sqrt{20}\sqrt{5} = \sqrt{100} = 10$$

Langkah 3: Masukkan ke rumus persamaan garis singgung lingkaran berpusat $(a, b)$:
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - 5 = 2(x - (-2)) \pm 10$$
$$y - 5 = 2x + 4 \pm 10$$
$$2x - y + 9 \pm 10 = 0$$

Diperoleh dua garis singgung:
1) $2x - y + 9 + 10 = 0 \implies 2x - y + 19 = 0$
2) $2x - y + 9 - 10 = 0 \implies 2x - y - 1 = 0$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b01-d-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: garis singgung dari titik di luar lingkaran*

Salah satu persamaan garis singgung pada lingkaran $L \equiv x^2 + y^2 = 9$ yang ditarik dari titik $T(0, 5)$ di luar lingkaran adalah ....

- A. $4x + 3y + 15 = 0$  
  <sub>Salah: Salah tanda konstanta ketika memindahkan ruas persamaan garis.</sub>
- **B. $4x + 3y - 15 = 0$** ✅  
  <sub>Benar: Garis polar dari $T(0, 5)$ terhadap $x^2 + y^2 = 9$ adalah $x_1x + y_1y = 9 \implies 0\cdot x + 5y = 9 \implies y = \frac{9}{5}$.
Substitusi ke persamaan lingkaran:
$x^2 + \left(\frac{9}{5}\right)^2 = 9 \implies x^2 + \frac{81}{25} = 9 \implies x^2 = \frac{144}{25} \implies x = \pm \frac{12}{5}$.
Titik singgung pertama adalah $\left(\frac{12}{5}, \frac{9}{5}\right)$.
Persamaan garis singgungnya:
$\frac{12}{5}x + \frac{9}{5}y = 9 \implies 12x + 9y = 45 \implies 4x + 3y - 15 = 0$.</sub>
- C. $3x + 4y - 15 = 0$  
  <sub>Salah: Tertukar koefisien absis dan ordinat titik singgung.</sub>
- D. $4x - 3y - 15 = 0$  
  <sub>Salah: Salah tanda pada ordinat titik singgung.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan garis polar lingkaran $x^2 + y^2 = 9$ dari titik $T(0, 5)$:
$$x_1x + y_1y = r^2$$
$$0\cdot x + 5y = 9 \implies y = \frac{9}{5}$$

Langkah 2: Menentukan titik singgung dengan menyubstitusikan $y = \frac{9}{5}$ ke persamaan lingkaran:
$$x^2 + \left(\frac{9}{5}\right)^2 = 9$$
$$x^2 = 9 - \frac{81}{25} = \frac{144}{25} \implies x = \pm \frac{12}{5}$$
Titik singgungnya adalah $A\left(\frac{12}{5}, \frac{9}{5}\right)$ dan $B\left(-\frac{12}{5}, \frac{9}{5}\right)$.

Langkah 3: Menentukan persamaan garis singgung melalui titik singgung $A\left(\frac{12}{5}, \frac{9}{5}\right)$:
$$\frac{12}{5}x + \frac{9}{5}y = 9$$
Kalikan kedua ruas dengan 5:
$$12x + 9y = 45$$
Bagi kedua ruas dengan 3:
$$4x + 3y - 15 = 0$$

(Untuk titik $B$, garis singgungnya adalah $-4x + 3y - 15 = 0$ atau $4x - 3y + 15 = 0$).
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b01-d-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: garis bagi lingkaran sejajar garis lain*

Persamaan garis yang sejajar dengan $3x - 4y + 8 = 0$ dan membagi lingkaran $L \equiv x^2 + y^2 - 4x + 8y - 5 = 0$ menjadi dua bagian dengan luas yang sama adalah ....

- A. $3x - 4y - 10 = 0$  
  <sub>Salah: Siswa keliru menentukan titik pusat lingkaran menjadi $(-2, 4)$ sehingga $3(-2) - 4(4) + c = 0 \iff c = 22$, lalu salah mengurangkan.</sub>
- B. $4x + 3y + 4 = 0$  
  <sub>Salah: Siswa mencari garis yang tegak lurus bukan yang sejajar.</sub>
- **C. $3x - 4y - 22 = 0$** ✅  
  <sub>Benar: Garis yang membagi luas lingkaran menjadi dua sama besar adalah garis yang melalui titik pusat lingkaran. Titik pusat $L$ adalah $\left(-\frac{-4}{2}, -\frac{8}{2}\right) = (2, -4)$. Garis yang sejajar $3x - 4y + 8 = 0$ berbentuk $3x - 4y + c = 0$. Substitusi $(2, -4)$ menghasilkan $3(2) - 4(-4) + c = 0 \iff 6 + 16 + c = 0 \iff c = -22$. Jadi, persamaannya adalah $3x - 4y - 22 = 0$.</sub>
- D. $3x - 4y + 22 = 0$  
  <sub>Salah: Siswa salah tanda saat memindahkan nilai konstanta ke ruas kiri.</sub>

**Pembahasan:** Garis yang membagi lingkaran menjadi dua bagian dengan luas yang sama merupakan garis yang melalui titik pusat lingkaran.

Menentukan titik pusat lingkaran $L \equiv x^2 + y^2 - 4x + 8y - 5 = 0$:
$$P\left(-\frac{A}{2}, -\frac{B}{2}\right) = P\left(-\frac{-4}{2}, -\frac{8}{2}\right) = (2, -4)$$

Garis yang sejajar dengan $3x - 4y + 8 = 0$ memiliki bentuk $3x - 4y + c = 0$.
Substitusikan titik pusat $(2, -4)$:
$$3(2) - 4(-4) + c = 0$$
$$6 + 16 + c = 0$$
$$22 + c = 0 \iff c = -22$$

Jadi, persamaan garis tersebut adalah $3x - 4y - 22 = 0$.
**Acuan:** pretest — kelas12_tl-b01-p0084-uji-kompetensi-bab-1-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b01-d-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: garis singgung di titik potong garis dan lingkaran*

Diketahui lingkaran $L \equiv (x - 5)^2 + (y + 2)^2 = 25$ memotong garis $y = -2$. Salah satu persamaan garis singgung lingkaran $L$ yang melalui titik potong lingkaran dan garis tersebut adalah ....

- A. $x = -5$  
  <sub>Salah: Salah tanda saat menyelesaikan persamaan nilai mutlak $(x - 5) = -5$ menjadi $x = -5$.</sub>
- B. $x = 5$  
  <sub>Salah: Menggunakan absis titik pusat lingkaran sebagai persamaan garis singgung.</sub>
- **C. $x = 10$** ✅  
  <sub>Benar: Substitusi $y = -2$ ke lingkaran menghasilkan $(x - 5)^2 + (-2 + 2)^2 = 25 \implies (x - 5)^2 = 25$, sehingga $x - 5 = 5$ atau $x - 5 = -5$, diperoleh titik potong $(10, -2)$ dan $(0, -2)$. Garis singgung di titik $(10, -2)$ adalah $(10 - 5)(x - 5) + (-2 + 2)(y + 2) = 25 \implies 5(x - 5) = 25 \implies x = 10$.</sub>
- D. $y = 10$  
  <sub>Salah: Tertukar antara variabel garis vertikal $x$ dengan variabel horizontal $y$.</sub>

**Pembahasan:** Langkah 1: Tentukan titik potong garis $y = -2$ dengan lingkaran $L$.
Substitusikan $y = -2$ ke persamaan lingkaran:
$$(x - 5)^2 + (-2 + 2)^2 = 25$$
$$(x - 5)^2 = 25$$
$$x - 5 = \pm 5$$
$$x_1 = 10 \quad \text{atau} \quad x_2 = 0$$
Titik potongnya adalah $(10, -2)$ dan $(0, -2)$.

Langkah 2: Tentukan persamaan garis singgung di titik potong tersebut.
Untuk titik $(10, -2)$:
$$(x_1 - 5)(x - 5) + (y_1 + 2)(y + 2) = 25$$
$$(10 - 5)(x - 5) + (-2 + 2)(y + 2) = 25$$
$$5(x - 5) + 0 = 25$$
$$x - 5 = 5 \implies x = 10$$

Untuk titik $(0, -2)$:
$$(0 - 5)(x - 5) + (-2 + 2)(y + 2) = 25$$
$$-5(x - 5) = 25$$
$$x - 5 = -5 \implies x = 0$$

Jadi, salah satu persamaan garis singgungnya adalah $x = 10$.
**Acuan:** pretest — kelas12_tl-b01-p0084-uji-kompetensi-bab-1-6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b01-d-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: garis singgung lingkaran di titik pada lingkaran*

Diketahui persamaan lingkaran $L \equiv x^2 + y^2 - 2x - 8y - 8 = 0$. Persamaan garis singgung lingkaran $L$ yang melalui titik $P(5, 7)$ adalah ....

- A. $5x + 7y - 41 = 0$  
  <sub>Salah: Salah rumus pembagian adil dengan langsung memasang koordinat titik sebagai koefisien suku linear.</sub>
- **B. $4x + 3y - 41 = 0$** ✅  
  <sub>Benar: Titik $P(5, 7)$ terletak pada lingkaran karena $5^2 + 7^2 - 2(5) - 8(7) - 8 = 0$. Garis singgung diperoleh dengan prinsip bagi adil: $x_1 x + y_1 y - \frac{2}{2}(x + x_1) - \frac{8}{2}(y + y_1) - 8 = 0 \implies 5x + 7y - (x + 5) - 4(y + 7) - 8 = 0 \implies 4x + 3y - 41 = 0$.</sub>
- C. $4x + 3y + 41 = 0$  
  <sub>Salah: Kesalahan tanda saat menghitung konstanta $-5 - 28 - 8$ menjadi positif.</sub>
- D. $3x + 4y - 41 = 0$  
  <sub>Salah: Tertukar koefisien variabel $x$ dan $y$.</sub>

**Pembahasan:** Langkah 1: Periksa kedudukan titik $P(5, 7)$ terhadap lingkaran $L$:
$$5^2 + 7^2 - 2(5) - 8(7) - 8 = 25 + 49 - 10 - 56 - 8 = 0$$
Titik $P(5, 7)$ terletak pada lingkaran.

Langkah 2: Tentukan persamaan garis singgung menggunakan prinsip pembagian adil:
$$x_1 x + y_1 y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$$
$$5x + 7y - 1(x + 5) - 4(y + 7) - 8 = 0$$
$$5x + 7y - x - 5 - 4y - 28 - 8 = 0$$
$$4x + 3y - 41 = 0$$

Jadi, persamaan garis singgung lingkaran tersebut adalah $4x + 3y - 41 = 0$.
**Acuan:** pretest — kelas12_tl-b01-p0082-latihan-soal-garis-singgung-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b01-d-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung tegak lurus garis lain*

Salah satu persamaan garis singgung lingkaran $L \equiv (x - 7)^2 + (y + 5)^2 = 64$ yang tegak lurus terhadap garis $l: 4x - 3y + 9 = 0$ adalah ....

- A. $4x - 3y + 39 = 0$  
  <sub>Salah: Menggunakan gradien garis sejajar, bukan garis tegak lurus.</sub>
- B. $3x + 4y + 19 = 0$  
  <sub>Salah: Lupa mengalikan suku konstanta $\pm 10$ dengan 4 ketika menghilangkan penyebut pecahan.</sub>
- C. $3x + 4y - 39 = 0$  
  <sub>Salah: Kesalahan tanda saat memindahkan konstanta dari ruas kanan ke ruas kiri.</sub>
- **D. $3x + 4y + 39 = 0$** ✅  
  <sub>Benar: Gradien garis $l$ adalah $m_l = \frac{4}{3}$. Karena tegak lurus, kemiringan garis singgung $m = -\frac{3}{4}$. Persamaan garis singgung berpusat $(7, -5)$ dengan jari-jari $r = 8$ adalah $y - (-5) = -\frac{3}{4}(x - 7) \pm 8\sqrt{\left(-\frac{3}{4}\right)^2 + 1} \implies y + 5 = -\frac{3}{4}(x - 7) \pm 10$. Dikalikan 4 diperoleh $4y + 20 = -3x + 21 \pm 40 \implies 3x + 4y - 1 \pm 40 = 0$, menghasilkan $3x + 4y + 39 = 0$ atau $3x + 4y - 41 = 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan kemiringan garis singgung.
Garis $l: 4x - 3y + 9 = 0 \implies 3y = 4x + 9 \implies y = \frac{4}{3}x + 3$.
Kemiringan garis $l$ adalah $m_l = \frac{4}{3}$.
Karena garis singgung tegak lurus dengan $l$, maka:
$$m \cdot m_l = -1 \implies m = -\frac{1}{m_l} = -\frac{3}{4}$$

Langkah 2: Menentukan komponen lingkaran.
Dari $L \equiv (x - 7)^2 + (y + 5)^2 = 64$, diperoleh pusat $(a, b) = (7, -5)$ dan jari-jari $r = \sqrt{64} = 8$.

Langkah 3: Menghitung persamaan garis singgung.
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - (-5) = -\frac{3}{4}(x - 7) \pm 8\sqrt{\left(-\frac{3}{4}\right)^2 + 1}$$
$$y + 5 = -\frac{3}{4}(x - 7) \pm 8\sqrt{\frac{25}{16}}$$
$$y + 5 = -\frac{3}{4}(x - 7) \pm 8 \cdot \frac{5}{4}$$
$$y + 5 = -\frac{3}{4}(x - 7) \pm 10$$
Kalikan kedua ruas dengan 4:
$$4(y + 5) = -3(x - 7) \pm 40$$
$$4y + 20 = -3x + 21 \pm 40$$
$$3x + 4y - 1 \pm 40 = 0$$
Diperoleh dua garis:
1) $3x + 4y - 1 + 40 = 0 \implies 3x + 4y + 39 = 0$
2) $3x + 4y - 1 - 40 = 0 \implies 3x + 4y - 41 = 0$

Jadi, salah satu persamaan garis singgungnya adalah $3x + 4y + 39 = 0$.
**Acuan:** siswa — siswa hal.75 Contoh Soal 1.25

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b01-d-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: luas daerah segitiga oleh garis singgung*

Garis singgung lingkaran $L \equiv x^2 + y^2 = 50$ di titik $T(5, 5)$ memotong sumbu-$x$ di titik $A$ dan memotong sumbu-$y$ di titik $B$. Luas daerah segitiga $AOB$ (dengan $O$ adalah titik pangkal koordinat) adalah ....

- **A. $50$ satuan luas** ✅  
  <sub>Benar: Garis singgung di $T(5, 5)$ adalah $5x + 5y = 50 \iff x + y = 10$. Titik potong sumbu-$x$ adalah $A(10, 0)$ dan sumbu-$y$ adalah $B(0, 10)$. Luas segitiga siku-siku $AOB = \frac{1}{2} \times 10 \times 10 = 50$ satuan luas.</sub>
- B. $25\sqrt{2}$ satuan luas  
  <sub>Salah: Mengalikan panjang jari-jari dengan jarak titik ke pusat.</sub>
- C. $25$ satuan luas  
  <sub>Salah: Menggunakan koordinat titik singgung $T(5, 5)$ sebagai alas dan tinggi: $\frac{1}{2} \times 5 \times 5 = 12{,}5$ atau $\frac{1}{2} \times 5 \times 10 = 25$.</sub>
- D. $100$ satuan luas  
  <sub>Salah: Lupa mengalikan dengan faktor $\frac{1}{2}$ pada rumus luas segitiga.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan garis singgung lingkaran di titik $T(5, 5)$.
Dengan prinsip bagi adil:
$$x_1 x + y_1 y = r^2$$
$$5x + 5y = 50$$
Bagi kedua ruas dengan 5:
$$x + y = 10$$

Langkah 2: Menentukan titik potong terhadap sumbu-sumbu koordinat.
- Titik potong sumbu-$x$ ($y = 0$):
  $$x + 0 = 10 \implies x = 10 \implies A(10, 0)$$
- Titik potong sumbu-$y$ ($x = 0$):
  $$0 + y = 10 \implies y = 10 \implies B(0, 10)$$

Langkah 3: Menghitung luas segitiga $AOB$.
Segitiga $AOB$ siku-siku di $O(0, 0)$ dengan panjang alas $OA = 10$ dan tinggi $OB = 10$:
$$\text{Luas } \triangle AOB = \frac{1}{2} \times OA \times OB = \frac{1}{2} \times 10 \times 10 = 50$$

Jadi, luas daerah segitiga $AOB$ adalah $50$ satuan luas.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b01-d-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: panjang tali busur polar*

Dua garis singgung pada lingkaran $L \equiv x^2 + y^2 = 16$ ditarik dari titik $P(5, 0)$ di luar lingkaran dan masing-masing menyinggung lingkaran di titik $A$ dan titik $B$. Jarak antara titik $A$ dan titik $B$ adalah ....

- A. $\frac{32}{5}$  
  <sub>Salah: Mengalikan nilai absis $x = \frac{16}{5}$ dengan 2 alih-alih selisih ordinat.</sub>
- B. $\frac{16}{5}$  
  <sub>Salah: Mengambil nilai absis garis polar sebagai panjang tali busur polar.</sub>
- C. $\frac{12}{5}$  
  <sub>Salah: Hanya menghitung nilai ordinat positif titik singgung tanpa mengalikan dua.</sub>
- **D. $\frac{24}{5}$** ✅  
  <sub>Benar: Persamaan garis polar dari $P(5, 0)$ adalah $5x + 0y = 16 \implies x = \frac{16}{5}$. Substitusikan ke lingkaran: $\left(\frac{16}{5}\right)^2 + y^2 = 16 \implies y^2 = 16 - \frac{256}{25} = \frac{144}{25} \implies y = \pm \frac{12}{5}$. Maka jarak $AB = \frac{12}{5} - \left(-\frac{12}{5}\right) = \frac{24}{5}$.</sub>

**Pembahasan:** Langkah 1: Tentukan persamaan garis polar dari titik $P(5, 0)$ terhadap lingkaran $L \equiv x^2 + y^2 = 16$.
$$x_1 x + y_1 y = r^2$$
$$5x + 0y = 16 \implies x = \frac{16}{5}$$

Langkah 2: Tentukan titik-titik singgung $A$ dan $B$.
Substitusikan $x = \frac{16}{5}$ ke persamaan lingkaran:
$$\left(\frac{16}{5}\right)^2 + y^2 = 16$$
$$\frac{256}{25} + y^2 = 16$$
$$y^2 = 16 - \frac{256}{25} = \frac{400 - 256}{25} = \frac{144}{25}$$
$$y = \pm \frac{12}{5}$$
Titik singgungnya adalah $A\left(\frac{16}{5}, \frac{12}{5}\right)$ dan $B\left(\frac{16}{5}, -\frac{12}{5}\right)$.

Langkah 3: Hitung jarak antara titik $A$ dan titik $B$.
Karena kedua titik memiliki absis yang sama, jaraknya adalah selisih ordinatnya:
$$AB = \left| \frac{12}{5} - \left(-\frac{12}{5}\right) \right| = \frac{24}{5}$$

Jadi, jarak antara titik $A$ dan titik $B$ adalah $\frac{24}{5}$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b01-d-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: panjang ruas garis singgung*

Dari titik $P(8, 6)$ ditarik garis singgung ke lingkaran $L \equiv x^2 + y^2 = 36$. Panjang ruas garis singgung dari titik $P$ ke titik singgung pada lingkaran tersebut adalah ....

- A. $10$  
  <sub>Salah: Siswa hanya menghitung jarak dari titik $P$ ke pusat lingkaran tanpa menguranginya dengan jari-jari kuadrat.</sub>
- B. $4$  
  <sub>Salah: Siswa langsung menghitung selisih jarak titik ke pusat dengan jari-jari ($10 - 6 = 4$) bukan Teorema Pythagoras.</sub>
- **C. $8$** ✅  
  <sub>Benar: Jarak titik $P(8, 6)$ ke pusat $(0, 0)$ adalah $d = 10$, sedangkan jari-jari $r = 6$. Panjang garis singgung adalah $\sqrt{d^2 - r^2} = \sqrt{100 - 36} = 8$.</sub>
- D. $6$  
  <sub>Salah: Siswa mengira panjang ruas garis singgung sama dengan jari-jari lingkaran.</sub>

**Pembahasan:** Titik pusat lingkaran $L \equiv x^2 + y^2 = 36$ adalah $O(0, 0)$ dan jari-jarinya $r = \sqrt{36} = 6$.

1. Hitung jarak titik $P(8, 6)$ ke pusat lingkaran $O(0, 0)$:
$$OP = \sqrt{(8 - 0)^2 + (6 - 0)^2} = \sqrt{64 + 36} = \sqrt{100} = 10$$

2. Ruas garis singgung dari titik $P$ ke titik singgung $T$ pada lingkaran tegak lurus terhadap jari-jari $OT$. Berdasarkan Teorema Pythagoras pada segitiga siku-siku $OTP$:
$$PT = \sqrt{OP^2 - r^2}$$
$$PT = \sqrt{10^2 - 6^2} = \sqrt{100 - 36} = \sqrt{64} = 8$$

Jadi, panjang ruas garis singgung dari titik $P$ ke titik singgung pada lingkaran adalah $8$.
**Acuan:** siswa — siswa hal.67

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b01-d-medium-bt01-015
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung sejajar garis tertentu*

Persamaan salah satu garis singgung lingkaran $L \equiv x^2 + y^2 = 65$ yang sejajar dengan garis $l: 8x - y + 13 = 0$ adalah ....

- A. $8x - y + 13 = 0$  
  <sub>Salah: Menggunakan konstanta garis acuan $l$ alih-alih menghitung $r\sqrt{m^2 + 1}$.</sub>
- B. $x - 8y + 65 = 0$  
  <sub>Salah: Menggunakan gradien kebalikan tegak lurus bukan gradien garis yang sejajar.</sub>
- **C. $8x - y + 65 = 0$** ✅  
  <sub>Benar: Gradien garis $l$ adalah $m = 8$ dan jari-jari lingkaran adalah $r = \sqrt{65}$. Persamaan garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$ adalah $y = mx \pm r\sqrt{m^2 + 1} = 8x \pm \sqrt{65}\sqrt{8^2 + 1} = 8x \pm 65$, yang ekuivalen dengan $8x - y \pm 65 = 0$. Salah satunya adalah $8x - y + 65 = 0$.</sub>
- D. $8x + y + 65 = 0$  
  <sub>Salah: Kesalahan tanda saat memindahkan ruas dari $y = 8x + 65$ menjadi $8x + y + 65 = 0$.</sub>

**Pembahasan:** Langkah 1: Tentukan kemiringan garis singgung.
Garis $l: 8x - y + 13 = 0 \iff y = 8x + 13$, sehingga kemiringan garis $m_l = 8$.
Karena garis singgung sejajar garis $l$, maka kemiringan garis singgung $m = m_l = 8$.

Langkah 2: Tentukan jari-jari lingkaran.
Dari persamaan $L \equiv x^2 + y^2 = 65$, diperoleh $r = \sqrt{65}$.

Langkah 3: Hitung persamaan garis singgung.
$$y = mx \pm r\sqrt{m^2 + 1}$$
$$y = 8x \pm \sqrt{65}\sqrt{8^2 + 1}$$
$$y = 8x \pm \sqrt{65}\sqrt{65}$$
$$y = 8x \pm 65$$
Diperoleh dua garis singgung: $8x - y + 65 = 0$ atau $8x - y - 65 = 0$.

Jadi, salah satu persamaan garis singgungnya adalah $8x - y + 65 = 0$.
**Acuan:** siswa — siswa hal.74 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b01-d-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: garis singgung ordinat titik diketahui*

Salah satu persamaan garis singgung lingkaran $L \equiv (x - 3)^2 + (y - 2)^2 = 25$ di titik yang berordinat $5$ adalah ....

- A. $4x + 3y - 25 = 0$  
  <sub>Salah: Siswa lupa mengurangkan konstanta dari penguraian $(x - a)$ dan $(y - b)$, langsung menyamakan $4x + 3y = 25$.</sub>
- B. $4x - 3y - 13 = 0$  
  <sub>Salah: Siswa salah memasukkan tanda koordinat pusat lingkaran menjadi $(y + 2)$ bukannya $(y - 2)$.</sub>
- **C. $4x + 3y - 43 = 0$** ✅  
  <sub>Benar: Substitusi $y = 5$ ke persamaan lingkaran menghasilkan $(x - 3)^2 + (5 - 2)^2 = 25 \iff (x - 3)^2 = 16$, sehingga $x - 3 = 4 \implies x = 7$ atau $x - 3 = -4 \implies x = -1$. Untuk titik singgung $(7, 5)$, persamaan garis singgungnya adalah $(7 - 3)(x - 3) + (5 - 2)(y - 2) = 25 \iff 4(x - 3) + 3(y - 2) = 25 \iff 4x + 3y - 43 = 0$.</sub>
- D. $7x + 5y - 25 = 0$  
  <sub>Salah: Siswa keliru menggunakan rumus lingkaran berpusat di $(0,0)$ yaitu $x_1x + y_1y = r^2$.</sub>

**Pembahasan:** Langkah 1: Menentukan absis titik singgung.
Substitusikan ordinat $y = 5$ ke persamaan lingkaran:
$$(x - 3)^2 + (5 - 2)^2 = 25$$
$$(x - 3)^2 + 9 = 25$$
$$(x - 3)^2 = 16$$
$$x - 3 = \pm 4$$
Diperoleh $x_1 = 7$ atau $x_2 = -1$.
Jadi, titik singgungnya adalah $(7, 5)$ dan $(-1, 5)$.

Langkah 2: Menentukan persamaan garis singgung di titik $(7, 5)$.
Gunakan rumus bagi adil untuk lingkaran $(x - a)^2 + (y - b)^2 = r^2$:
$$(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$$
$$(7 - 3)(x - 3) + (5 - 2)(y - 2) = 25$$
$$4(x - 3) + 3(y - 2) = 25$$
$$4x - 12 + 3y - 6 = 25$$
$$4x + 3y - 43 = 0$$

Untuk titik $(-1, 5)$, persamaannya adalah $-4(x - 3) + 3(y - 2) = 25 \iff -4x + 3y - 19 = 0 \iff 4x - 3y + 19 = 0$.
Dengan demikian, salah satu garis singgungnya adalah $4x + 3y - 43 = 0$.
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b01-d-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: nilai parameter garis singgung lingkaran*

Garis $g: y = 2x + c$ menyinggung lingkaran $L \equiv x^2 + y^2 = 20$. Jika $c > 0$, nilai $c$ yang memenuhi adalah ....

- A. $20$  
  <sub>Salah: Siswa tidak menarik akar dari $r^2(m^2 + 1)$ atau salah mengira $c = r^2$.</sub>
- **B. $10$** ✅  
  <sub>Benar: Gradien garis $m = 2$ dan jari-jari lingkaran $r = \sqrt{20}$. Garis $y = mx + c$ menyinggung lingkaran jika $c = \pm r\sqrt{m^2 + 1} = \pm \sqrt{20}\sqrt{2^2 + 1} = \pm \sqrt{100} = \pm 10$. Karena $c > 0$, nilai $c = 10$.</sub>
- C. $2\sqrt{5}$  
  <sub>Salah: Siswa hanya mengambil nilai jari-jari $r = \sqrt{20} = 2\sqrt{5}$ tanpa mengalikan dengan faktor $\sqrt{m^2 + 1}$.</sub>
- D. $5$  
  <sub>Salah: Siswa salah menghitung nilai di dalam akar, hanya menghitung $m^2 + 1 = 5$ lalu mengabaikan $r$.</sub>

**Pembahasan:** Berdasarkan rumus garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$:
$$y = mx \pm r\sqrt{m^2 + 1}$$

Dari garis $g: y = 2x + c$, diperoleh $m = 2$.
Dari lingkaran $L: x^2 + y^2 = 20$, diperoleh $r^2 = 20$ sehingga $r = \sqrt{20}$.

Maka konstanta $c$ memenuhi:
$$c = \pm r\sqrt{m^2 + 1} = \pm \sqrt{20}\sqrt{2^2 + 1} = \pm \sqrt{20 \times 5} = \pm \sqrt{100} = \pm 10$$

Karena diberikan syarat $c > 0$, maka $c = 10$.
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b01-d-medium-bt01-018
*variasi (angka) | C3 | 3 langkah | jenis: persamaan garis singgung di titik berabsis tertentu*

Salah satu persamaan garis singgung lingkaran $L \equiv x^2 + y^2 + 10x - 16y + 64 = 0$ di titik yang berabsis $-8$ adalah ....

- **A. $3x + 4y + 8 = 0$** ✅  
  <sub>Benar: Substitusi $x = -8$ ke persamaan lingkaran menghasilkan ordinat titik singgung $y = 4$ dan $y = 12$. Garis singgung di titik $(-8, 4)$ adalah $3x + 4y + 8 = 0$.</sub>
- B. $4x + 3y + 8 = 0$  
  <sub>Salah: Tertukar antara koefisien variabel $x$ dan $y$.</sub>
- C. $3x - 4y + 8 = 0$  
  <sub>Salah: Kesalahan tanda operasi pada suku variabel $y$.</sub>
- D. $3x + 4y - 8 = 0$  
  <sub>Salah: Kesalahan tanda aljabar saat menjumlahkan konstanta pada rumus pembagian adil.</sub>

**Pembahasan:** Langkah 1: Menentukan titik singgung dengan menyubstitusikan $x = -8$ ke persamaan lingkaran:
$$(-8)^2 + y^2 + 10(-8) - 16y + 64 = 0$$
$$64 + y^2 - 80 - 16y + 64 = 0$$
$$y^2 - 16y + 48 = 0$$
$$(y - 4)(y - 12) = 0$$
Diperoleh $y = 4$ atau $y = 12$, sehingga titik singgungnya adalah $(-8, 4)$ dan $(-8, 12)$.

Langkah 2: Menentukan persamaan garis singgung di titik $(-8, 4)$ menggunakan rumus bagi adil:
$$x_1x + y_1y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$$
$$-8x + 4y + 5(x - 8) - 8(y + 4) + 64 = 0$$
$$-8x + 4y + 5x - 40 - 8y - 32 + 64 = 0$$
$$-3x - 4y - 8 = 0$$
$$3x + 4y + 8 = 0$$

Jadi, salah satu persamaan garis singgungnya adalah $3x + 4y + 8 = 0$.
**Acuan:** pretest — kelas12_tl-b01-p0083-latihan-soal-garis-singgung-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b01-d-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: titik potong garis polar dengan sumbu koordinat*

Garis polar lingkaran $L \equiv x^2 + y^2 - 4x - 6y + 9 = 0$ yang ditarik dari titik $P(4, 5)$ memotong sumbu-$x$ di titik ....

- A. $(0, 7)$  
  <sub>Salah: Tertukar antara titik potong terhadap sumbu-x dan titik potong terhadap sumbu-y.</sub>
- B. $\left(\frac{9}{4}, 0\right)$  
  <sub>Salah: Menggunakan rumus garis polar untuk lingkaran berpusat di $(0,0)$, yaitu $x_1x + y_1y = r^2$ ($4x + 5(0) = 9$).</sub>
- C. $(-7, 0)$  
  <sub>Salah: Salah tanda pada konstanta saat menyederhanakan persamaan garis polar menjadi $x + y = -7$.</sub>
- **D. $(7, 0)$** ✅  
  <sub>Benar: Persamaan garis polar titik $P(x_1, y_1) = (4, 5)$ terhadap lingkaran $x^2 + y^2 - 4x - 6y + 9 = 0$ adalah $x_1x + y_1y - 2(x + x_1) - 3(y + y_1) + 9 = 0 \iff 4x + 5y - 2(x + 4) - 3(y + 5) + 9 = 0 \iff 2x + 2y - 14 = 0 \iff x + y = 7$. Titik potong dengan sumbu-$x$ diperoleh saat $y = 0$, yaitu $x = 7$, sehingga koordinatnya adalah $(7, 0)$.</sub>

**Pembahasan:** Persamaan garis polar lingkaran $x^2 + y^2 + Ax + By + C = 0$ dari titik $P(x_1, y_1)$ dirumuskan sebagai:
$$x_1x + y_1y + \frac{A}{2}(x + x_1) + \frac{B}{2}(y + y_1) + C = 0$$

Substitusikan $x_1 = 4$, $y_1 = 5$, $A = -4$, $B = -6$, dan $C = 9$:
$$4x + 5y - 2(x + 4) - 3(y + 5) + 9 = 0$$
$$4x + 5y - 2x - 8 - 3y - 15 + 9 = 0$$
$$2x + 2y - 14 = 0$$
$$x + y = 7$$

Titik potong garis polar terhadap sumbu-$x$ terjadi ketika $y = 0$:
$$x + 0 = 7 \implies x = 7$$

Jadi, garis polar memotong sumbu-$x$ di titik $(7, 0)$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b01-d-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: garis singgung di titik potong sumbu koordinat*

Diketahui lingkaran $L \equiv (x - 2)^2 + (y - 3)^2 = 13$ memotong sumbu-$x$ di titik $A$ dan titik $B$. Jika absis titik $A$ lebih besar dari absis titik $B$, persamaan garis singgung lingkaran $L$ di titik $A$ adalah ....

- A. $2x + 3y = 0$  
  <sub>Salah: Menentukan garis singgung di titik B(0, 0), bukan di titik A(4, 0).</sub>
- **B. $2x - 3y - 8 = 0$** ✅  
  <sub>Benar: Titik potong dengan sumbu-$x$ ($y = 0$) adalah $(x - 2)^2 + (-3)^2 = 13 \iff (x - 2)^2 = 4 \iff x = 4$ atau $x = 0$. Karena absis $A$ lebih besar, maka titik $A$ adalah $(4, 0)$. Persamaan garis singgung di titik $A(4, 0)$ menggunakan prinsip bagi adil: $(4 - 2)(x - 2) + (0 - 3)(y - 3) = 13 \iff 2(x - 2) - 3(y - 3) = 13 \iff 2x - 3y + 5 = 13 \iff 2x - 3y - 8 = 0$.</sub>
- C. $2x - 3y + 8 = 0$  
  <sub>Salah: Salah memindahkan ruas konstanta, $5 - 13$ dihitung menjadi $+8$.</sub>
- D. $2x + 3y - 8 = 0$  
  <sub>Salah: Salah memasukkan tanda ordinat titik singgung saat melakukan bagi adil pada suku $(y - 3)$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong lingkaran dengan sumbu-$x$ ($y = 0$).
$$(x - 2)^2 + (0 - 3)^2 = 13$$
$$(x - 2)^2 + 9 = 13$$
$$(x - 2)^2 = 4$$
$$x - 2 = 2 \implies x = 4$$
$$x - 2 = -2 \implies x = 0$$
Diperoleh dua titik potong, yaitu $(4, 0)$ dan $(0, 0)$. Karena absis titik $A$ lebih besar dari titik $B$, maka koordinat titik $A$ adalah $(4, 0)$.

Langkah 2: Menentukan persamaan garis singgung di titik $A(4, 0)$ menggunakan prinsip pembagian adil:
$$(x_1 - 2)(x - 2) + (y_1 - 3)(y - 3) = 13$$
$$(4 - 2)(x - 2) + (0 - 3)(y - 3) = 13$$
$$2(x - 2) - 3(y - 3) = 13$$
$$2x - 4 - 3y + 9 = 13$$
$$2x - 3y + 5 = 13$$
$$2x - 3y - 8 = 0$$

Jadi, persamaan garis singgung lingkaran di titik $A$ adalah $2x - 3y - 8 = 0$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b01-d-hard-bt01-001
*orisinal | C5 | 6 langkah | jenis: garis singgung persekutuan luar*

Dua garis singgung pada lingkaran $L \equiv x^2 + y^2 - 6x + 8y = 0$ sejajar dengan garis $4x - 3y + 1 = 0$. Jarak antara kedua garis singgung tersebut adalah ....

- A. $20$  
  <sub>Salah: Keliru mengalikan diameter dengan faktor gradien.</sub>
- **B. $10$** ✅  
  <sub>Benar: Ubah bentuk lingkaran: $(x - 3)^2 + (y + 4)^2 = 3^2 + (-4)^2 = 25$, sehingga jari-jari $r = 5$. Dua garis singgung yang sejajar pada sebuah lingkaran merupakan garis singgung di kedua ujung diameter lingkaran. Oleh karena itu, jarak tegak lurus antara kedua garis singgung sejajar tersebut tepat sama dengan diameter lingkaran, yaitu $d = 2r = 2 \times 5 = 10$.</sub>
- C. $5$  
  <sub>Salah: Hanya menghitung panjang jari-jari lingkaran, bukan diameter.</sub>
- D. $25$  
  <sub>Salah: Mengira jarak kedua garis singgung adalah nilai $r^2$.</sub>

**Pembahasan:** Persamaan lingkaran $L \equiv x^2 + y^2 - 6x + 8y = 0$ diubah ke bentuk baku:
$$(x - 3)^2 + (y + 4)^2 = 3^2 + (-4)^2 = 25$$
Diperoleh pusat lingkaran $(3, -4)$ dan jari-jari $r = \sqrt{25} = 5$.

Karena kedua garis singgung pada lingkaran tersebut saling sejajar (keduanya memiliki gradien yang sama dengan gradien garis $4x - 3y + 1 = 0$), maka kedua garis tersebut menyinggung lingkaran di titik-titik ujung diameter yang bersesuaian.

Jarak antara dua garis singgung sejajar pada suatu lingkaran selalu sama dengan panjang diameter lingkaran tersebut:
$$\text{Jarak} = 2r = 2 \times 5 = 10$$
**Acuan:** siswa — siswa hal.73

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b01-d-hard-bt01-002
*orisinal | C5 | 6 langkah | jenis: garis polar dan segitiga singgung*

Dari titik $T(4, 8)$ ditarik garis polar terhadap lingkaran $L \equiv x^2 + y^2 = 16$. Garis polar tersebut memotong sumbu-$x$ di titik $A$ dan memotong sumbu-$y$ di titik $B$. Luas daerah segitiga $OAB$ dengan $O(0, 0)$ adalah ....

- A. $8$ satuan luas  
  <sub>Salah: Lupa membagi dua pada rumus luas segitiga ($OA \times OB$).</sub>
- B. $16$ satuan luas  
  <sub>Salah: Menggunakan nilai $r^2$ sebagai luas segitiga.</sub>
- C. $2$ satuan luas  
  <sub>Salah: Salah menentukan titik potong pada sumbu-$x$ menjadi $2$.</sub>
- **D. $4$ satuan luas** ✅  
  <sub>Benar: Persamaan garis polar titik $T(x_1, y_1) = (4, 8)$ terhadap lingkaran $x^2 + y^2 = 16$ adalah $x_1 x + y_1 y = 16 \Rightarrow 4x + 8y = 16 \Rightarrow x + 2y = 4$. Titik potong dengan sumbu-$x$ (saat $y = 0$) adalah $A(4, 0)$, sehingga alas $OA = 4$. Titik potong dengan sumbu-$y$ (saat $x = 0$) adalah $B(0, 2)$, sehingga tinggi $OB = 2$. Luas $\triangle OAB = \frac{1}{2} \times OA \times OB = \frac{1}{2} \times 4 \times 2 = 4$ satuan luas.</sub>

**Pembahasan:** Persamaan garis polar dari titik $T(x_1, y_1) = (4, 8)$ terhadap lingkaran $x^2 + y^2 = r^2 = 16$ adalah:
$$x_1 x + y_1 y = r^2$$
$$4x + 8y = 16$$
$$x + 2y = 4$$

Menentukan titik potong dengan sumbu-sumbu koordinat:
- Perpotongan dengan sumbu-$x$ ($y = 0$):
$$x + 2(0) = 4 \implies x = 4 \implies A(4, 0)$$
- Perpotongan dengan sumbu-$y$ ($x = 0$):
$$0 + 2y = 4 \implies y = 2 \implies B(0, 2)$$

Segitiga $OAB$ merupakan segitiga siku-siku di $O(0, 0)$ dengan panjang sisi alas $OA = 4$ dan tinggi $OB = 2$.
Luas daerah segitiga $OAB$:
$$\text{Luas} = \frac{1}{2} \times OA \times OB = \frac{1}{2} \times 4 \times 2 = 4\text{ satuan luas}$$
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b01-d-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: garis singgung saling tegak lurus*

Titik $P(a, b)$ dengan $a > b$ terletak pada garis $x + y = 4$. Jika dua garis singgung yang ditarik dari titik $P$ ke lingkaran $L \equiv x^2 + y^2 = 5$ saling tegak lurus, nilai dari $2a - b$ adalah ....

- A. $7$  
  <sub>Salah: Keliru menghitung operasi akhir menjadi $2a + b$.</sub>
- B. $4$  
  <sub>Salah: Salah menerapkan syarat tegak lurus sehingga memakai persamaan $a^2 + b^2 = 5$ bukannya lingkaran ortoptik.</sub>
- C. $1$  
  <sub>Salah: Menggunakan pasangan solusi $a = 1$ dan $b = 3$ tanpa mengindahkan syarat $a > b$.</sub>
- **D. $5$** ✅  
  <sub>Benar: Garis singgung bergradien $m$ melalui $P(a, b)$ memenuhi $(b - ma)^2 = 5(m^2 + 1) \iff (a^2 - 5)m^2 - 2abm + (b^2 - 5) = 0$. Karena kedua garis saling tegak lurus, $m_1 m_2 = \frac{b^2 - 5}{a^2 - 5} = -1 \implies a^2 + b^2 = 10$. Substitusi $b = 4 - a$ menghasilkan $a^2 - 4a + 3 = 0$. Karena $a > b$, diperoleh $a = 3$ dan $b = 1$. Jadi, $2a - b = 2(3) - 1 = 5$.</sub>

**Pembahasan:** Persamaan garis singgung lingkaran $x^2 + y^2 = r^2$ dengan gradien $m$ adalah:
$$y = mx \pm r\sqrt{m^2 + 1}$$

Karena garis melalui $P(a, b)$:
$$b - ma = \pm \sqrt{5(m^2 + 1)}$$
Kuadratkan kedua ruas:
$$(b - ma)^2 = 5(m^2 + 1)$$
$$b^2 - 2abm + a^2 m^2 = 5m^2 + 5$$
$$(a^2 - 5)m^2 - 2abm + (b^2 - 5) = 0$$

Kedua garis singgung saling tegak lurus, sehingga hasil kali gradiennya $m_1 m_2 = -1$:
$$\frac{b^2 - 5}{a^2 - 5} = -1$$
$$b^2 - 5 = -(a^2 - 5) \implies a^2 + b^2 = 10$$

Karena titik $P(a, b)$ terletak pada garis $x + y = 4$, substitusikan $b = 4 - a$:
$$a^2 + (4 - a)^2 = 10$$
$$a^2 + 16 - 8a + a^2 = 10$$
$$2a^2 - 8a + 6 = 0 \implies a^2 - 4a + 3 = 0$$
$$(a - 3)(a - 1) = 0$$

Diperoleh $a = 3$ atau $a = 1$. Karena $a > b$:
- Untuk $a = 3 \implies b = 4 - 3 = 1$ (memenuhi $3 > 1$).
- Untuk $a = 1 \implies b = 4 - 1 = 3$ (tidak memenuhi $1 > 3$).

Maka nilai $2a - b = 2(3) - 1 = 5$.
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b01-d-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: jarak titik ke garis singgung*

Diketahui titik $T(4, -1)$ terletak pada lingkaran $L \equiv (x - 1)^2 + (y + 2)^2 = 10$. Jika garis $g$ merupakan garis singgung lingkaran $L$ di titik $T$, jarak titik $Q(8, 7)$ ke garis $g$ adalah ....

- A. $\sqrt{10}$  
  <sub>Salah: Kesalahan aritmetika pada pembilang jarak titik ke garis menjadi 10.</sub>
- B. $3\sqrt{10}$  
  <sub>Salah: Kesalahan substitusi koordinat titik $Q$ ke dalam persamaan garis.</sub>
- **C. $2\sqrt{10}$** ✅  
  <sub>Benar: Persamaan garis singgung di $T(4, -1)$ adalah $(4 - 1)(x - 1) + (-1 + 2)(y + 2) = 10 \iff 3x + y - 11 = 0$. Jarak titik $Q(8, 7)$ ke garis tersebut dihitung dengan $d = \frac{|3(8) + 1(7) - 11|}{\sqrt{3^2 + 1^2}} = \frac{20}{\sqrt{10}} = 2\sqrt{10}$.</sub>
- D. $4\sqrt{10}$  
  <sub>Salah: Lupa membagi dengan akar kuadrat jumlah koefisien $\sqrt{A^2+B^2}$.</sub>

**Pembahasan:** Cek kedudukan titik $T(4, -1)$ terhadap lingkaran:
$$(4 - 1)^2 + (-1 + 2)^2 = 3^2 + 1^2 = 10$$
Titik $T$ terletak tepat pada lingkaran.

Persamaan garis singgung di titik $T(4, -1)$ menggunakan prinsip bagi adil:
$$(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$$
$$(4 - 1)(x - 1) + (-1 + 2)(y + 2) = 10$$
$$3(x - 1) + 1(y + 2) = 10$$
$$3x - 3 + y + 2 - 10 = 0$$
$$3x + y - 11 = 0$$

Jarak titik $Q(8, 7)$ ke garis singgung $3x + y - 11 = 0$:
$$d = \frac{|Ax_0 + By_0 + C|}{\sqrt{A^2 + B^2}}$$
$$d = \frac{|3(8) + 1(7) - 11|}{\sqrt{3^2 + 1^2}} = \frac{|24 + 7 - 11|}{\sqrt{10}} = \frac{20}{\sqrt{10}} = 2\sqrt{10}$$

Jadi, jarak titik $Q$ ke garis $g$ adalah $2\sqrt{10}$.
**Acuan:** siswa — siswa hal.69

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b01-d-hard-bt01-005
*variasi (angka) | C5 | 5 langkah | jenis: layang-layang garis singgung*

Titik $A$ dan $B$ terletak pada lingkaran $L \equiv x^2 + y^2 + 4x - 6y + c = 0$. Garis-garis singgung lingkaran yang ditarik melalui titik $A$ dan $B$ berpotongan di titik $T(4, 11)$. Jika luas layang-layang yang dibentuk oleh titik $A$, $B$, $T$, dan pusat lingkaran adalah $48$ satuan luas serta jari-jari lingkaran $r < 7$, maka nilai $c$ adalah ....

- A. $-11$  
  <sub>Salah: Lupa menguadratkan koordinat titik pusat dalam rumus jari-jari lingkaran.</sub>
- **B. $-23$** ✅  
  <sub>Benar: Pusat lingkaran $P(-2, 3)$. Jarak $PT = \sqrt{(4 - (-2))^2 + (11 - 3)^2} = 10$. Luas layang-layang $= 2 \times (\frac{1}{2} r \sqrt{PT^2 - r^2}) = r\sqrt{100 - r^2} = 48$. Dikuadratkan: $r^2(100 - r^2) = 2304 \implies (r^2)^2 - 100r^2 + 2304 = 0$. Pemfaktoran: $(r^2 - 36)(r^2 - 64) = 0$. Karena $r < 7$, maka $r^2 = 36$. Jari-jari lingkaran: $r^2 = (-2)^2 + 3^2 - c = 13 - c \implies 13 - c = 36 \implies c = -23$.</sub>
- C. $-51$  
  <sub>Salah: Memilih akar $r^2 = 64$ yang melanggar syarat batas $r < 7$.</sub>
- D. $23$  
  <sub>Salah: Kesalahan tanda aljabar saat menyelesaikan $13 - c = 36$.</sub>

**Pembahasan:** Dari persamaan lingkaran $L \equiv x^2 + y^2 + 4x - 6y + c = 0$, diperoleh pusat $P(-2, 3)$ dan jari-jari $r = \sqrt{(-2)^2 + 3^2 - c} = \sqrt{13 - c}$.

Jarak titik $P$ ke titik $T(4, 11)$ adalah:
$$PT = \sqrt{(4 - (-2))^2 + (11 - 3)^2} = \sqrt{6^2 + 8^2} = 10$$

Segiempat $PATB$ merupakan layang-layang yang tersusun atas dua segitiga siku-siku kongruen, yaitu $\triangle PAT$ dan $\triangle PBT$ dengan siku-siku di $A$ dan $B$.
Panjang garis singgung $AT = \sqrt{PT^2 - r^2} = \sqrt{100 - r^2}$.

Luas layang-layang $PATB$ adalah:
$$\text{Luas} = 2 \times \left(\frac{1}{2} \cdot r \cdot \sqrt{100 - r^2}\right) = r\sqrt{100 - r^2} = 48$$

Kuadratkan kedua ruas:
$$r^2(100 - r^2) = 2304$$
$$(r^2)^2 - 100r^2 + 2304 = 0$$
$$(r^2 - 36)(r^2 - 64) = 0$$
Diperoleh $r^2 = 36$ atau $r^2 = 64$.

Karena diberikan syarat $r < 7$, maka nilai yang memenuhi adalah $r^2 = 36$.
Substitusikan ke rumus jari-jari:
$$13 - c = 36 \implies c = 13 - 36 = -23$$
**Acuan:** siswa — siswa hal.84 Uji Kompetensi Bab 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b01-d-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: garis singgung bergradien tertentu*

Dua garis singgung pada lingkaran $L \equiv (x - 1)^2 + (y - 2)^2 = 20$ memiliki kemiringan $m = 2$. Kedua garis singgung tersebut masing-masing memotong sumbu-$x$ di titik $P$ dan titik $Q$. Panjang ruas garis $PQ$ adalah ....

- A. $4\sqrt{5}$  
  <sub>Salah: Keliru menghitung jarak tegak lurus antargaris singgung alih-alih panjang ruas garis pada sumbu-x.</sub>
- B. $5$  
  <sub>Salah: Hanya menghitung nilai absis dari salah satu titik potong tanpa mencari selisih keduanya.</sub>
- **C. $10$** ✅  
  <sub>Benar: Persamaan garis singgung bergradien $m=2$ pada lingkaran berpusat $(1, 2)$ dan $r = \sqrt{20}$ adalah $y - 2 = 2(x - 1) \pm \sqrt{20}\sqrt{2^2 + 1} = 2x - 2 \pm 10 \implies y = 2x \pm 10$. Titik potong dengan sumbu-$x$ ($y = 0$): $0 = 2x + 10 \implies x_1 = -5$, dan $0 = 2x - 10 \implies x_2 = 5$. Panjang ruas garis $PQ = |5 - (-5)| = 10$.</sub>
- D. $20$  
  <sub>Salah: Menjumlahkan nilai konstanta kedua garis singgung alih-alih menghitung jarak titik potong sumbu-x.</sub>

**Pembahasan:** Lingkaran $L \equiv (x - 1)^2 + (y - 2)^2 = 20$ memiliki titik pusat $(a, b) = (1, 2)$ dan jari-jari $r = \sqrt{20}$.

Persamaan garis singgung dengan kemiringan $m = 2$ ditentukan oleh rumus:
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - 2 = 2(x - 1) \pm \sqrt{20}\sqrt{2^2 + 1}$$
$$y - 2 = 2x - 2 \pm \sqrt{20 \times 5}$$
$$y - 2 = 2x - 2 \pm 10$$
$$y = 2x \pm 10$$

Diperoleh dua persamaan garis singgung:
1. $g_1 \equiv y = 2x + 10$
2. $g_2 \equiv y = 2x - 10$

Tentukan titik potong masing-masing garis dengan sumbu-$x$ ($y = 0$):
- Untuk garis $g_1$:
$$0 = 2x + 10 \implies x = -5 \implies P(-5, 0)$$
- Untuk garis $g_2$:
$$0 = 2x - 10 \implies x = 5 \implies Q(5, 0)$$

Panjang ruas garis $PQ$ adalah:
$$PQ = |x_2 - x_1| = |5 - (-5)| = 10$$
**Acuan:** siswa — siswa hal.76

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b01-d-hard-bt01-007
*orisinal | C6 | 5 langkah | jenis: garis singgung saling tegak lurus*

Dari sebuah titik $P(k, 0)$ dengan $k > 0$ ditarik dua garis singgung ke lingkaran $L \equiv x^2 + y^2 = 18$. Jika kedua garis singgung tersebut saling tegak lurus, maka nilai $k$ adalah ....

- A. $18$  
  <sub>Salah: Mengira $k^2 - 18 = 0$ sehingga mengambil nilai $k^2$ langsung.</sub>
- B. $36$  
  <sub>Salah: Lupa menarik akar kuadrat dari $k^2 = 36$.</sub>
- C. $3\sqrt{2}$  
  <sub>Salah: Menganggap nilai $k$ sama dengan panjang jari-jari lingkaran.</sub>
- **D. $6$** ✅  
  <sub>Benar: Garis melalui $P(k, 0)$ dengan gradien $m$ adalah $y = m(x - k) \implies mx - y - mk = 0$. Jarak pusat $(0, 0)$ ke garis adalah jari-jari $r = \sqrt{18}$: $\frac{|-mk|}{\sqrt{m^2 + 1}} = \sqrt{18} \implies m^2 k^2 = 18(m^2 + 1) \implies (k^2 - 18)m^2 - 18 = 0$. Syarat kedua garis saling tegak lurus adalah $m_1 m_2 = -1$. Dari teorema Vieta: $m_1 m_2 = \frac{-18}{k^2 - 18} = -1 \implies k^2 - 18 = 18 \implies k^2 = 36$. Karena $k > 0$, diperoleh $k = 6$.</sub>

**Pembahasan:** Persamaan garis yang melalui titik $P(k, 0)$ dengan kemiringan $m$ adalah:
$$y - 0 = m(x - k) \implies mx - y - mk = 0$$

Karena garis ini menyinggung lingkaran $L \equiv x^2 + y^2 = 18$, maka jarak dari pusat lingkaran $O(0, 0)$ ke garis singgung sama dengan jari-jari $r = \sqrt{18}$:
$$\frac{|m(0) - (0) - mk|}{\sqrt{m^2 + (-1)^2}} = \sqrt{18}$$
$$\frac{|-mk|}{\sqrt{m^2 + 1}} = \sqrt{18}$$

Kuadratkan kedua ruas:
$$\frac{m^2 k^2}{m^2 + 1} = 18$$
$$m^2 k^2 = 18m^2 + 18$$
$$(k^2 - 18)m^2 - 18 = 0$$

Persamaan kuadrat dalam $m$ ini memiliki dua akar kemiringan garis singgung, yaitu $m_1$ dan $m_2$. Karena kedua garis singgung saling tegak lurus, maka berlaku:
$$m_1 \cdot m_2 = -1$$

Berdasarkan hasil kali akar-akar persamaan kuadrat:
$$m_1 \cdot m_2 = \frac{-18}{k^2 - 18}$$
$$\frac{-18}{k^2 - 18} = -1$$
$$k^2 - 18 = 18$$
$$k^2 = 36$$

Karena disyaratkan $k > 0$, maka:
$$k = \sqrt{36} = 6$$
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b01-d-hard-bt01-008
*orisinal | C6 | 6 langkah | jenis: tali busur kontak lingkaran*

Dari titik $P(5, 5)$ di luar lingkaran ditarik dua garis singgung ke lingkaran $L \equiv x^2 + y^2 = 25$. Jika kedua garis tersebut masing-masing menyinggung lingkaran di titik $A$ dan titik $B$, panjang ruas garis $AB$ adalah ....

- **A. $5\sqrt{2}$** ✅  
  <sub>Benar: Garis polar dari $P(5, 5)$ terhadap $x^2 + y^2 = 25$ adalah $5x + 5y = 25 \iff x + y = 5$. Jarak pusat $O(0, 0)$ ke garis polar adalah $d = \frac{|0 + 0 - 5|}{\sqrt{1^2 + 1^2}} = \frac{5}{\sqrt{2}}$. Jari-jari lingkaran $r = 5$. Setengah panjang tali busur $AB$ adalah $\sqrt{r^2 - d^2} = \sqrt{25 - \frac{25}{2}} = \sqrt{\frac{25}{2}} = \frac{5}{\sqrt{2}}$. Maka panjang $AB = 2 \times \frac{5}{\sqrt{2}} = 5\sqrt{2}$.</sub>
- B. $5$  
  <sub>Salah: Siswa mengira panjang tali busur sama dengan panjang jari-jari lingkaran.</sub>
- C. $\frac{5\sqrt{2}}{2}$  
  <sub>Salah: Siswa hanya menghitung setengah panjang tali busur dan lupa mengalikan dua.</sub>
- D. $10$  
  <sub>Salah: Siswa mengira tali busur kontak sama dengan diameter lingkaran.</sub>

**Pembahasan:** Persamaan garis polar yang ditarik dari titik $P(x_1, y_1) = (5, 5)$ terhadap lingkaran $x^2 + y^2 = 25$ adalah:
$$x_1x + y_1y = 25 \implies 5x + 5y = 25 \iff x + y - 5 = 0$$
Garis polar ini merupakan garis yang melalui titik-titik singgung $A$ dan $B$.
Jarak dari pusat lingkaran $O(0, 0)$ ke garis polar $x + y - 5 = 0$ adalah:
$$d = \frac{|0 + 0 - 5|}{\sqrt{1^2 + 1^2}} = \frac{5}{\sqrt{2}}$$
Panjang ruas garis $AB$ merupakan panjang tali busur lingkaran berjejari $r = 5$ yang berjarak $d$ dari pusat:
$$AB = 2\sqrt{r^2 - d^2} = 2\sqrt{5^2 - \left(\frac{5}{\sqrt{2}}\right)^2} = 2\sqrt{25 - \frac{25}{2}} = 2\sqrt{\frac{25}{2}} = 2\left(\frac{5}{\sqrt{2}}\right) = 5\sqrt{2}$$
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b01-d-hard-bt01-009
*variasi (angka) | C5 | 5 langkah | jenis: garis singgung lingkaran dari titik luar*

Persamaan salah satu garis singgung lingkaran $L \equiv x^2 + y^2 - 8x + 10y + 16 = 0$ yang melalui titik $T(-7, -3)$ adalah ....

- A. $7x - 24y + 23 = 0$  
  <sub>Salah: Siswa salah memasukkan tanda konstanta pada persamaan garis singgung kedua ($m = \frac{7}{24}$).</sub>
- B. $4x - 3y + 19 = 0$  
  <sub>Salah: Siswa keliru menggunakan gradien garis normal $m = \frac{4}{3}$ alih-alih gradien garis singgung $m = -\frac{3}{4}$.</sub>
- C. $3x + 4y - 33 = 0$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada konstanta saat memindahkan ruas dari bentuk gradien-titik.</sub>
- **D. $3x + 4y + 33 = 0$** ✅  
  <sub>Benar: Pusat lingkaran adalah $P(4, -5)$ dengan jari-jari $r = \sqrt{4^2 + (-5)^2 - 16} = 5$. Garis yang melalui $T(-7, -3)$ dengan gradien $m$ adalah $mx - y + (7m - 3) = 0$. Jarak $P$ ke garis singgung sama dengan jari-jari: $\frac{|4m - (-5) + 7m - 3|}{\sqrt{m^2 + 1}} = 5 \iff \frac{|11m + 2|}{\sqrt{m^2 + 1}} = 5$. Mengkuadratkan kedua ruas menghasilkan $(11m + 2)^2 = 25(m^2 + 1) \iff 96m^2 + 44m - 21 = 0$, yang difaktorkan menjadi $(24m - 7)(4m + 3) = 0$, sehingga $m = -\frac{3}{4}$ atau $m = \frac{7}{24}$. Untuk $m = -\frac{3}{4}$, persamaannya adalah $-\frac{3}{4}x - y + \left(7\left(-\frac{3}{4}\right) - 3\right) = 0 \iff 3x + 4y + 33 = 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik pusat dan jari-jari lingkaran.
Dari persamaan $L \equiv x^2 + y^2 - 8x + 10y + 16 = 0$, diperoleh pusat $P(a, b) = \left(-\frac{-8}{2}, -\frac{10}{2}\right) = (4, -5)$ dan jari-jari $r = \sqrt{4^2 + (-5)^2 - 16} = \sqrt{16 + 25 - 16} = 5$.

Langkah 2: Memeriksa kedudukan titik $T(-7, -3)$.
Substitusi ke persamaan lingkaran:
$(-7)^2 + (-3)^2 - 8(-7) + 10(-3) + 16 = 49 + 9 + 56 - 30 + 16 = 100 > 0$.
Karena nilainya positif, titik $T(-7, -3)$ berada di luar lingkaran.

Langkah 3: Menyusun persamaan garis yang melalui $T(-7, -3)$ dengan gradien $m$.
$y - (-3) = m(x - (-7)) \implies mx - y + (7m - 3) = 0$.

Langkah 4: Menghitung nilai $m$ menggunakan syarat jarak titik pusat ke garis singgung sama dengan jari-jari.
$d = \frac{|m(4) - (-5) + 7m - 3|}{\sqrt{m^2 + 1}} = 5$
$\frac{|11m + 2|}{\sqrt{m^2 + 1}} = 5$
Kuadratkan kedua ruas:
$(11m + 2)^2 = 25(m^2 + 1)$
$121m^2 + 44m + 4 = 25m^2 + 25$
$96m^2 + 44m - 21 = 0$
Faktorkan persamaan kuadrat:
$(4m + 3)(24m - 7) = 0$
Diperoleh $m_1 = -\frac{3}{4}$ atau $m_2 = \frac{7}{24}$.

Langkah 5: Menentukan persamaan garis singgung.
Untuk $m = -\frac{3}{4}$:
$y + 3 = -\frac{3}{4}(x + 7)$
$4(y + 3) = -3(x + 7)$
$4y + 12 = -3x - 21$
$3x + 4y + 33 = 0$.

Untuk $m = \frac{7}{24}$:
$y + 3 = \frac{7}{24}(x + 7)$
$24(y + 3) = 7(x + 7)$
$24y + 72 = 7x + 49$
$7x - 24y - 23 = 0$.

Jadi, salah satu persamaan garis singgung lingkaran tersebut adalah $3x + 4y + 33 = 0$.
**Acuan:** siswa — siswa hal.80 Contoh Soal 1.27

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b01-d-hard-bt01-010
*variasi (angka) | C5 | 5 langkah | jenis: garis singgung tegak lurus lingkaran*

Diketahui lingkaran $L \equiv (x - 3)^2 + (y + 4)^2 = 169$. Garis singgung pada lingkaran $L$ ditarik tegak lurus terhadap garis $l \equiv 5x + 12y - 7 = 0$. Jika salah satu garis singgung tersebut memotong sumbu-$x$ di titik $(p, 0)$ dengan $p > 0$, maka nilai dari $4p$ adalah ....

- **A. $75$** ✅  
  <sub>Benar: Gradien garis $l$ adalah $m_l = -\frac{5}{12}$, sehingga gradien garis singgung adalah $m = \frac{12}{5}$. Persamaan garis singgung adalah $y + 4 = \frac{12}{5}(x - 3) \pm 13\sqrt{1 + \left(\frac{12}{5}\right)^2} = \frac{12}{5}(x - 3) \pm \frac{169}{5}$. Dikalikan 5 menghasilkan $12x - 5y - 56 \pm 169 = 0$. Garis dengan konstanta negatif memberikan $12x - 5y - 225 = 0$. Titik potong sumbu-$x$ ($y=0$) adalah $x = \frac{225}{12} = \frac{75}{4} > 0$, sehingga $p = \frac{75}{4}$ dan nilai $4p = 75$.</sub>
- B. $\frac{113}{3}$  
  <sub>Salah: Siswa menggunakan garis singgung satunya, yaitu $12x - 5y + 113 = 0$ yang menghasilkan absis negatif, lalu mengambil nilai mutlaknya dikalikan 4.</sub>
- C. $-75$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada pemindahan ruas konstanta sehingga menghasilkan absis negatif.</sub>
- D. $56$  
  <sub>Salah: Siswa lupa memperhitungkan komponen jari-jari $r\sqrt{1+m^2}$ pada rumus garis singgung.</sub>

**Pembahasan:** Garis $l \equiv 5x + 12y - 7 = 0$ memiliki kemiringan:
$m_l = -\frac{5}{12}$

Karena garis singgung tegak lurus garis $l$, kemiringan garis singgung $m$ memenuhi:
$m \cdot m_l = -1 \implies m = \frac{12}{5}$

Lingkaran memiliki pusat $(a, b) = (3, -4)$ dan jari-jari $r = \sqrt{169} = 13$.
Persamaan garis singgung bergradien $m$ adalah:
$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$
$y - (-4) = \frac{12}{5}(x - 3) \pm 13\sqrt{\left(\frac{12}{5}\right)^2 + 1}$
$y + 4 = \frac{12}{5}(x - 3) \pm 13\left(\frac{13}{5}\right)$
$y + 4 = \frac{12}{5}(x - 3) \pm \frac{169}{5}$

Kalikan kedua ruas dengan 5:
$5(y + 4) = 12(x - 3) \pm 169$
$5y + 20 = 12x - 36 \pm 169$
$12x - 5y - 56 \pm 169 = 0$

Diperoleh dua garis singgung:
1) $12x - 5y + 113 = 0$
2) $12x - 5y - 225 = 0$

Cari titik potong masing-masing garis dengan sumbu-$x$ ($y = 0$):
- Untuk garis pertama: $12x + 113 = 0 \implies x = -\frac{113}{12}$ (tidak memenuhi syarat $p > 0$).
- Untuk garis kedua: $12x - 225 = 0 \implies x = \frac{225}{12} = \frac{75}{4}$ (memenuhi syarat $p > 0$).

Maka $p = \frac{75}{4}$.
Nilai dari $4p = 4 \times \frac{75}{4} = 75$.
**Acuan:** siswa — siswa hal.75 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b01-d-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: garis singgung tegak lurus bergradien*

Diketahui lingkaran $L \equiv (x - 1)^2 + (y - 1)^2 = 5$. Garis $g$ merupakan garis singgung lingkaran $L$ di titik $A(3, 0)$. Garis $h$ tegak lurus terhadap garis $g$ dan juga menyinggung lingkaran $L$. Jika garis $h$ memotong sumbu-$x$ di titik $(p, 0)$ dengan $p > 0$, maka nilai $p$ adalah ....

- **A. $8$** ✅  
  <sub>Benar: Garis singgung di $A(3, 0)$ adalah $(3-1)(x-1) + (0-1)(y-1) = 5 \implies 2x - y - 6 = 0$ dengan gradien $m_g = 2$. Garis $h$ tegak lurus $g$, sehingga $m_h = -\frac{1}{2}$. Garis singgung bergradien $-\frac{1}{2}$ pada lingkaran $(x-1)^2 + (y-1)^2 = 5$ adalah $y - 1 = -\frac{1}{2}(x - 1) \pm \sqrt{5}\sqrt{(-\frac{1}{2})^2 + 1} \implies x + 2y = 3 \pm 5$. Untuk titik potong sumbu-$x$ ($y=0$), absisnya adalah $x = 3 \pm 5$. Karena $p > 0$, maka $p = 3 + 5 = 8$.</sub>
- B. $6$  
  <sub>Salah: Kesalahan pergeseran absis pusat pada rumus garis singgung lingkaran bergradien $m$.</sub>
- C. $2$  
  <sub>Salah: Mengabaikan tanda negatif pada titik potong lainnya yaitu $x = 3 - 5 = -2$ dan mengambil nilainya sebagai positif.</sub>
- D. $10$  
  <sub>Salah: Keliru menggunakan gradien $m = 2$ pada persamaan garis singgung kedua alih-alih gradien garis tegak lurusnya.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan garis $g$ di titik $A(3, 0)$ pada lingkaran $(x - 1)^2 + (y - 1)^2 = 5$.
$$(x_1 - a)(x - a) + (y_1 - b)(y - b) = r^2$$
$$(3 - 1)(x - 1) + (0 - 1)(y - 1) = 5$$
$$2(x - 1) - (y - 1) = 5$$
$$2x - 2 - y + 1 = 5 \implies 2x - y - 6 = 0$$
Gradien garis $g$ adalah $m_g = 2$.

Langkah 2: Menentukan gradien garis $h$.
Karena garis $h \perp g$, maka:
$$m_h = -\frac{1}{m_g} = -\frac{1}{2}$$

Langkah 3: Menentukan persamaan garis singgung $h$ dengan gradien $m_h = -\frac{1}{2}$.
$$y - b = m(x - a) \pm r\sqrt{m^2 + 1}$$
$$y - 1 = -\frac{1}{2}(x - 1) \pm \sqrt{5}\sqrt{\left(-\frac{1}{2}\right)^2 + 1}$$
$$y - 1 = -\frac{1}{2}x + \frac{1}{2} \pm \sqrt{5}\cdot\frac{\sqrt{5}}{2}$$
$$y - 1 = -\frac{1}{2}x + \frac{1}{2} \pm \frac{5}{2}$$
Kalikan kedua ruas dengan $2$:
$$2y - 2 = -x + 1 \pm 5$$
$$x + 2y = 3 \pm 5$$

Langkah 4: Menentukan titik potong dengan sumbu-$x$ ($y = 0$).
$$x + 2(0) = 3 \pm 5 \implies x = 8 \text{ atau } x = -2$$
Karena $p > 0$, maka $p = 8$.
**Acuan:** siswa — siswa hal.75

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b01-d-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: garis singgung dan garis normal*

Garis $g$ merupakan garis singgung lingkaran $L \equiv x^2 + y^2 - 4x - 2y = 0$ di titik $A(4, 2)$. Garis normal $k$ tegak lurus terhadap garis $g$ di titik $A$. Jika garis $g$ dan garis normal $k$ masing-masing memotong sumbu-$y$ di titik $Q$ dan $P$, maka panjang ruas garis $PQ$ adalah ....

- A. $5$  
  <sub>Salah: Hanya menghitung nilai jari-jari kuadrat atau setengah dari panjang ruas garis yang sebenarnya.</sub>
- **B. $10$** ✅  
  <sub>Benar: Persamaan garis singgung $g$ di titik $A(4, 2)$ adalah $x(4) + y(2) - 2(x + 4) - (y + 2) = 0 \implies 2x + y - 10 = 0$, sehingga memotong sumbu-$y$ di titik $Q(0, 10)$. Garis normal $k$ selalu melalui titik pusat $M(2, 1)$ dan titik $A(4, 2)$, sehingga persamaannya adalah $y - 1 = \frac{2 - 1}{4 - 2}(x - 2) \implies y = \frac{1}{2}x$. Garis $k$ memotong sumbu-$y$ di titik $P(0, 0)$. Jarak $PQ = |10 - 0| = 10$.</sub>
- C. $8$  
  <sub>Salah: Kesalahan pada pembagian adil untuk suku linier persamaan lingkaran sehingga konstanta garis singgung menjadi $8$.</sub>
- D. $12$  
  <sub>Salah: Kesalahan tanda aljabar saat memindahkan konstanta persamaan garis singgung sehingga ordinat titik potong bernilai $12$.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan garis singgung $g$ di titik $A(4, 2)$ menggunakan prinsip bagi adil.
$$x_1x + y_1y - 2(x + x_1) - 1(y + y_1) = 0$$
$$4x + 2y - 2(x + 4) - (y + 2) = 0$$
$$4x + 2y - 2x - 8 - y - 2 = 0$$
$$2x + y - 10 = 0$$

Langkah 2: Menentukan titik potong garis $g$ dengan sumbu-$y$ (substitusi $x = 0$):
$$2(0) + y - 10 = 0 \implies y = 10$$
Diperoleh koordinat $Q(0, 10)$.

Langkah 3: Menentukan persamaan garis normal $k$.
Garis normal pada lingkaran selalu melalui titik pusat lingkaran $M$ dan titik singgung $A(4, 2)$.
Titik pusat lingkaran $L \equiv x^2 + y^2 - 4x - 2y = 0$ adalah $M\left(-\frac{-4}{2}, -\frac{-2}{2}\right) = M(2, 1)$.
Gradien garis normal:
$$m_k = \frac{y_A - y_M}{x_A - x_M} = \frac{2 - 1}{4 - 2} = \frac{1}{2}$$
Persamaan garis normal melalui $M(2, 1)$:
$$y - 1 = \frac{1}{2}(x - 2) \implies y = \frac{1}{2}x$$

Langkah 4: Menentukan titik potong garis normal $k$ dengan sumbu-$y$ (substitusi $x = 0$):
$$y = \frac{1}{2}(0) = 0$$
Diperoleh koordinat $P(0, 0)$.

Langkah 5: Menghitung panjang ruas garis $PQ$:
$$PQ = \sqrt{(0 - 0)^2 + (10 - 0)^2} = 10$$
**Acuan:** siswa — siswa hal.68

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b01-d-hard-bt01-013
*orisinal | C6 | 5 langkah | jenis: luas segitiga tali busur singgung*

Dari titik $T(0, 25)$ ditarik dua garis singgung ke lingkaran $L \equiv x^2 + y^2 = 225$. Garis-garis singgung tersebut masing-masing menyinggung lingkaran $L$ di titik $A$ dan titik $B$. Luas segitiga $TAB$ adalah .... satuan luas.

- **A. $192$** ✅  
  <sub>Benar: Persamaan garis polar dari $T(0, 25)$ adalah $0\cdot x + 25y = 225 \implies y = 9$. Substitusi ke lingkaran: $x^2 + 9^2 = 225 \implies x^2 = 144 \implies x = \pm 12$. Titik kontak adalah $A(-12, 9)$ dan $B(12, 9)$, sehingga panjang alas $AB = 24$. Tinggi segitiga dari titik $T(0, 25)$ ke garis $AB$ ($y = 9$) adalah $t = 25 - 9 = 16$. Luas segitiga $TAB = \frac{1}{2} \times 24 \times 16 = 192$.</sub>
- B. $108$  
  <sub>Salah: Menghitung luas segitiga yang dibentuk oleh titik pusat dan kedua titik singgung ($OAB$), yaitu $\frac{1}{2} \times 24 \times 9 = 108$.</sub>
- C. $384$  
  <sub>Salah: Lupa mengalikan dengan faktor $\frac{1}{2}$ pada rumus luas segitiga, menghitung $24 \times 16 = 384$.</sub>
- D. $144$  
  <sub>Salah: Keliru menggunakan nilai absis titik singgung ($12$) sebagai tinggi segitiga sehingga menghitung $\frac{1}{2} \times 24 \times 12 = 144$.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan garis polar lingkaran dari titik $T(0, 25)$.
$$x_1x + y_1y = r^2$$
$$0\cdot x + 25y = 225$$
$$y = 9$$

Langkah 2: Menentukan koordinat titik singgung $A$ dan $B$ dengan menyubstitusikan $y = 9$ ke persamaan lingkaran $x^2 + y^2 = 225$:
$$x^2 + 9^2 = 225$$
$$x^2 + 81 = 225$$
$$x^2 = 144 \implies x = 12 \text{ atau } x = -12$$
Diperoleh titik kontak $A(-12, 9)$ dan $B(12, 9)$.

Langkah 3: Menentukan panjang alas segitiga $AB$:
Karena kedua titik memiliki ordinat sama ($y = 9$), maka alasnya horizontal:
$$\text{alas} = |12 - (-12)| = 24$$

Langkah 4: Menentukan tinggi segitiga dari titik $T(0, 25)$ ke garis $AB$ ($y = 9$):
$$\text{tinggi} = 25 - 9 = 16$$

Langkah 5: Menghitung luas segitiga $TAB$:
$$\text{Luas} = \frac{1}{2} \times \text{alas} \times \text{tinggi} = \frac{1}{2} \times 24 \times 16 = 192 \text{ satuan luas}$$
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b01-d-hard-bt01-014
*variasi (angka) | C5 | 4 langkah | jenis: garis singgung sumbu koordinat*

Tentukan nilai $k > 0$ agar lingkaran $L \equiv (x - 8k)^2 + (y + 10)^2 - 64k^2 = 36$ menyinggung sumbu-$x$. Selanjutnya, carilah titik singgung antara lingkaran $L$ dan sumbu-$x$ tersebut.

- A. $k = 1$ dan $(1, 0)$  
  <sub>Salah: Siswa mengira nilai parameter $k$ langsung menjadi absis dari titik singgung pada sumbu-$x$.</sub>
- B. $k = 2$ dan $(16, 0)$  
  <sub>Salah: Siswa salah saat menyelesaikan persamaan $64k^2 = 64$ sehingga memperoleh $k = 2$ dan titik singgung $(16, 0)$.</sub>
- **C. $k = 1$ dan $(8, 0)$** ✅  
  <sub>Benar: Pusat lingkaran adalah $(8k, -10)$ dan $r^2 = 64k^2 + 36$. Karena menyinggung sumbu-$x$, berlaku $r = |-10| = 10$, sehingga $64k^2 + 36 = 100 \iff 64k^2 = 64 \iff k = 1$ (karena $k > 0$). Titik singgung pada sumbu-$x$ adalah $(8k, 0) = (8, 0)$.</sub>
- D. $k = 1$ dan $(10, 0)$  
  <sub>Salah: Siswa keliru menggunakan nilai mutlak ordinat pusat sebagai absis titik singgung lingkaran pada sumbu-$x$.</sub>

**Pembahasan:** Persamaan lingkaran dapat ditulis ulang menjadi $(x - 8k)^2 + (y + 10)^2 = 64k^2 + 36$.

1. Titik pusat lingkaran adalah $P(8k, -10)$ dan kuadrat jari-jarinya $r^2 = 64k^2 + 36$.
2. Garis yang disinggung adalah sumbu-$x$ ($y = 0$). Jarak dari pusat $P(8k, -10)$ ke garis $y = 0$ adalah $|-10| = 10$. Karena lingkaran menyinggung garis tersebut, maka jari-jarinya adalah $r = 10$, sehingga $r^2 = 100$.
3. Substitusikan nilai $r^2$ ke bentuk kuadrat jari-jari:
$$64k^2 + 36 = 100$$
$$64k^2 = 64$$
$$k^2 = 1$$
Karena disyaratkan $k > 0$, maka $k = 1$.
4. Titik singgung pada sumbu-$x$ memiliki ordinat $y = 0$. Substitusikan $y = 0$ dan $k = 1$ ke persamaan lingkaran:
$$(x - 8(1))^2 + (0 + 10)^2 = 64(1)^2 + 36$$
$$(x - 8)^2 + 100 = 100$$
$$(x - 8)^2 = 0 \iff x = 8$$

Jadi, diperoleh nilai $k = 1$ dan titik singgungnya adalah $(8, 0)$.
**Acuan:** siswa — siswa hal.83 Latihan Soal Persamaan Garis Singgung Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b01-d-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: perpotongan dua garis singgung*

Dua garis singgung pada lingkaran $L \equiv x^2 + y^2 = 25$ masing-masing ditarik di titik $A(3, 4)$ dan titik $B(-4, 3)$. Jika kedua garis singgung tersebut berpotongan di titik $P(x_0, y_0)$, nilai dari $x_0 + y_0$ adalah ....

- A. $8$  
  <sub>Salah: Siswa salah menghitung koordinat titik potong menjadi $(1, 7)$ akibat keliru tanda saat eliminasi.</sub>
- B. $4$  
  <sub>Salah: Siswa salah melakukan operasi eliminasi sehingga mendapatkan koordinat $(-1, 5)$.</sub>
- C. $-6$  
  <sub>Salah: Siswa tertukar tanda koordinat titik potong menjadi $(1, -7)$.</sub>
- **D. $6$** ✅  
  <sub>Benar: Persamaan garis singgung di $A$ adalah $3x + 4y = 25$ dan di $B$ adalah $-4x + 3y = 25$. Titik potong diperoleh $x_0 = -1$ dan $y_0 = 7$, sehingga $x_0 + y_0 = -1 + 7 = 6$.</sub>

**Pembahasan:** Langkah 1: Tentukan persamaan garis singgung di titik $A(3, 4)$ pada lingkaran $x^2 + y^2 = 25$:
$$x_1x + y_1y = r^2 \implies 3x + 4y = 25 \quad \text{...(1)}$$

Langkah 2: Tentukan persamaan garis singgung di titik $B(-4, 3)$ pada lingkaran $x^2 + y^2 = 25$:
$$x_2x + y_2y = r^2 \implies -4x + 3y = 25 \quad \text{...(2)}$$

Langkah 3: Tentukan titik potong kedua garis dengan mengeliminasi $y$:
Kalikan persamaan (1) dengan $3$ dan persamaan (2) dengan $4$:
$$9x + 12y = 75$$
$$-16x + 12y = 100$$
Kurangkan kedua persamaan:
$$25x = -25 \implies x_0 = -1$$

Langkah 4: Substitusikan $x_0 = -1$ ke persamaan (1):
$$3(-1) + 4y = 25$$
$$-3 + 4y = 25 \implies 4y = 28 \implies y_0 = 7$$

Langkah 5: Hitung nilai $x_0 + y_0$:
$$x_0 + y_0 = -1 + 7 = 6$$
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b01-d-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: garis singgung berparameter lingkaran*

Tentukan nilai $p$ jika sebuah lingkaran $L \equiv x^2 + y^2 - 4px + q = 0$ berjari-jari $6$ dan menyinggung garis $3x - 4y = 0$.

- A. $p = 6$ atau $p = -6$  
  <sub>Salah: Siswa langsung menyamakan nilai parameter $p$ dengan jari-jari lingkaran.</sub>
- B. $p = 10$ atau $p = -10$  
  <sub>Salah: Siswa salah menentukan titik pusat menjadi $(p, 0)$ karena lupa membagi koefisien $-4p$ dengan $-2$.</sub>
- **C. $p = 5$ atau $p = -5$** ✅  
  <sub>Benar: Pusat lingkaran adalah $(2p, 0)$ dan jari-jari $r = 6$. Syarat menyinggung garis $3x - 4y = 0$ adalah jarak titik pusat ke garis sama dengan jari-jari, yaitu $\frac{|3(2p) - 4(0)|}{\sqrt{3^2 + (-4)^2}} = 6 \iff \frac{|6p|}{5} = 6 \iff |p| = 5$, sehingga diperoleh $p = 5$ atau $p = -5$.</sub>
- D. $p = \frac{5}{2}$ atau $p = -\frac{5}{2}$  
  <sub>Salah: Siswa menganggap titik pusat adalah $(4p, 0)$ tanpa membaginya dengan dua.</sub>

**Pembahasan:** Persamaan lingkaran $L \equiv x^2 + y^2 - 4px + q = 0$ memiliki titik pusat:
$$P\left(-\frac{-4p}{2}, -\frac{0}{2}\right) = (2p, 0)$$

Diketahui jari-jari lingkaran $r = 6$.

Agar lingkaran menyinggung garis $3x - 4y = 0$, jarak titik pusat $P(2p, 0)$ ke garis tersebut harus sama dengan panjang jari-jarinya ($d = r$):
$$d = \frac{|3(2p) - 4(0)|}{\sqrt{3^2 + (-4)^2}}$$
$$6 = \frac{|6p|}{\sqrt{9 + 16}}$$
$$6 = \frac{|6p|}{5}$$
$$|6p| = 30$$
$$|p| = 5$$
$$p = 5 \text{ atau } p = -5$$

Jadi, nilai $p$ yang memenuhi adalah $p = 5$ atau $p = -5$.
**Acuan:** siswa — siswa hal.83 Latihan Soal Persamaan Garis Singgung Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b01-d-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: titik tetap berkas garis polar*

Titik $P(x_0, y_0)$ selalu terletak pada garis $x + 2y = 10$. Dari titik $P$ ditarik garis polar terhadap lingkaran $L \equiv x^2 + y^2 = 25$. Untuk setiap posisi titik $P$ pada garis tersebut, garis polar yang terbentuk selalu melalui satu titik tetap $Q(a, b)$. Nilai dari $a + b$ adalah ....

- A. $\frac{5}{2}$  
  <sub>Salah: Siswa hanya menyebutkan nilai absis $a$ dari titik tetap tanpa menjumlahkannya dengan ordinat $b$.</sub>
- **B. $\frac{15}{2}$** ✅  
  <sub>Benar: Substitusi $x_0 = 10 - 2y_0$ ke persamaan garis polar $x_0 x + y_0 y = 25$ menghasilkan $(10x - 25) + y_0(y - 2x) = 0$. Titik tetap diperoleh saat $10x - 25 = 0 \implies a = \frac{5}{2}$ dan $y - 2x = 0 \implies b = 5$. Jadi, $a + b = \frac{5}{2} + 5 = \frac{15}{2}$.</sub>
- C. $\frac{25}{2}$  
  <sub>Salah: Siswa keliru menetapkan persamaan garis polar menjadi $(10x - 25) + y_0(y + 2x) = 0$ sehingga diperoleh $b = -5$ lalu menjumlahkan kuadratnya atau salah menjumlahkan.</sub>
- D. $5$  
  <sub>Salah: Siswa hanya menyebutkan nilai ordinat $b$ dari titik tetap tanpa menjumlahkannya dengan absis $a$.</sub>

**Pembahasan:** Titik $P(x_0, y_0)$ terletak pada garis $x + 2y = 10$, sehingga berlaku:
$x_0 = 10 - 2y_0$.

Persamaan garis polar dari titik $P(x_0, y_0)$ terhadap lingkaran $x^2 + y^2 = 25$ adalah:
$x_0 x + y_0 y = 25$.

Substitusikan $x_0 = 10 - 2y_0$ ke persamaan garis polar:
$(10 - 2y_0)x + y_0 y = 25$
$10x - 2y_0 x + y_0 y - 25 = 0$
$(10x - 25) + y_0(y - 2x) = 0$.

Agar persamaan tersebut selalu bernilai benar untuk setiap nilai $y_0$, maka suku-suku pembentuknya harus bernilai nol:
1) $10x - 25 = 0 \implies x = \frac{25}{10} = \frac{5}{2}$
2) $y - 2x = 0 \implies y = 2x = 2\left(\frac{5}{2}\right) = 5$.

Dengan demikian, titik tetap yang selalu dilalui oleh garis polar tersebut adalah $Q(a, b) = \left(\frac{5}{2}, 5\right)$.

Nilai dari $a + b$ adalah:
$a + b = \frac{5}{2} + 5 = \frac{15}{2}$.
**Acuan:** siswa — siswa hal.78

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b01-d-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: sudut apit dua garis singgung*

Dua buah garis singgung ditarik dari titik $P(x_1, y_1)$ di luar lingkaran $L \equiv x^2 + y^2 = 16$. Kedua garis singgung tersebut saling berpotongan di titik $P$ dan membentuk sudut $60^\circ$. Jika titik $P$ terletak di kuadran I dan berada pada garis $y = \sqrt{3}x$, koordinat titik $P$ adalah ....

- A. $(2\sqrt{3}, 6)$  
  <sub>Salah: Siswa keliru menggunakan perbandingan kosinus $\cos 30^\circ = \frac{r}{OP}$ sehingga jarak $OP = \frac{8}{\sqrt{3}}$.</sub>
- **B. $(4, 4\sqrt{3})$** ✅  
  <sub>Benar: Sudut antara garis singgung dan garis hubung pusat ke $P$ adalah $30^\circ$. Jarak $OP = \frac{r}{\sin 30^\circ} = \frac{4}{1/2} = 8$. Substitusi $y = \sqrt{3}x$ ke $x^2 + y^2 = 64$ menghasilkan $4x^2 = 64 \implies x = 4$ dan $y = 4\sqrt{3}$.</sub>
- C. $(2, 2\sqrt{3})$  
  <sub>Salah: Siswa salah mengira jarak titik $P$ ke pusat lingkaran sama dengan panjang jari-jari lingkaran ($OP = 4$).</sub>
- D. $(8, 8\sqrt{3})$  
  <sub>Salah: Siswa mengira nilai absis $x$ sama dengan panjang jarak $OP = 8$.</sub>

**Pembahasan:** Lingkaran $L \equiv x^2 + y^2 = 16$ memiliki pusat di $O(0, 0)$ dan jari-jari $r = \sqrt{16} = 4$.

Misalkan titik singgung kedua garis tersebut pada lingkaran adalah $A$ dan $B$. Ruas garis $OP$ membagi sudut antara kedua garis singgung menjadi dua bagian sama besar, sehingga:
$\angle APO = \frac{60^\circ}{2} = 30^\circ$.

Pada segitiga siku-siku $OAP$ (siku-siku di $A$ karena garis singgung tegak lurus jari-jari):
$\sin(\angle APO) = \frac{OA}{OP}$
$\sin 30^\circ = \frac{4}{OP}$
$\frac{1}{2} = \frac{4}{OP} \implies OP = 8$.

Jarak dari titik $O(0, 0)$ ke titik $P(x_1, y_1)$ adalah:
$x_1^2 + y_1^2 = OP^2 = 8^2 = 64$.

Karena titik $P$ terletak pada garis $y = \sqrt{3}x$, substitusikan ke persamaan jarak:
$x_1^2 + (\sqrt{3}x_1)^2 = 64$
$x_1^2 + 3x_1^2 = 64$
$4x_1^2 = 64 \implies x_1^2 = 16$.

Karena titik $P$ berada di kuadran I, maka $x_1 > 0$:
$x_1 = 4$.
$y_1 = \sqrt{3}(4) = 4\sqrt{3}$.

Jadi, koordinat titik $P$ adalah $(4, 4\sqrt{3})$.
**Acuan:** siswa — siswa hal.77

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b01-d-hard-bt01-019
*variasi (angka) | C5 | 5 langkah | jenis: layang-layang garis singgung*

Misalkan titik $P$ dan titik $Q$ berada pada lingkaran $L \equiv x^2 + y^2 - 8x + 4y + m = 0$, serta garis-garis singgung lingkaran yang melalui kedua titik tersebut berpotongan di titik $T(4, 11)$. Jika luas layang-layang yang melalui titik $P$, titik $Q$, titik $T$, dan titik pusat lingkaran adalah $60$, serta panjang jari-jari lingkaran lebih kecil daripada panjang ruas garis singgungnya, nilai $m$ adalah ....

- **A. $-5$** ✅  
  <sub>Benar: Titik pusat lingkaran $M(4, -2)$ dengan $r^2 = 4^2 + (-2)^2 - m = 20 - m$. Jarak titik $M$ ke $T(4, 11)$ adalah $d = \sqrt{(4-4)^2 + (11 - (-2))^2} = 13$. Panjang garis singgung $t = \sqrt{d^2 - r^2} = \sqrt{169 - r^2}$. Luas layang-layang adalah $L = r \cdot t = 60$, sehingga $r^2(169 - r^2) = 3600 \iff r^4 - 169r^2 + 3600 = 0$. Diperoleh $(r^2 - 25)(r^2 - 144) = 0$. Karena jari-jari lebih kecil daripada ruas garis singgung ($r < t$), maka $r^2 = 25$ (sehingga $r = 5$ dan $t = 12$). Akibatnya, $20 - m = 25 \iff m = -5$.</sub>
- B. $-124$  
  <sub>Salah: Siswa memilih nilai $r^2 = 144$ yang membuat jari-jari lebih besar daripada panjang ruas garis singgung ($r = 12$ dan $t = 5$), melanggar syarat $r < t$, sehingga memperoleh $20 - m = 144 \iff m = -124$.</sub>
- C. $-40$  
  <sub>Salah: Siswa keliru menganggap kuadrat jari-jari sama dengan luas layang-layang garis singgung ($r^2 = 60$), sehingga menghitung $20 - m = 60 \iff m = -40$.</sub>
- D. $5$  
  <sub>Salah: Siswa melakukan kesalahan aljabar tanda saat menyelesaikan persamaan linear akhir, menghitung $20 - m = 25$ menjadi $m = 25 - 20 = 5$.</sub>

**Pembahasan:** Persamaan lingkaran $L \equiv x^2 + y^2 - 8x + 4y + m = 0$ memiliki titik pusat:
$$M\left(-\frac{-8}{2}, -\frac{4}{2}\right) = (4, -2)$$
Jari-jari lingkaran memenuhi:
$$r^2 = 4^2 + (-2)^2 - m = 20 - m$$

Jarak antara titik pusat $M(4, -2)$ dan titik potong garis singgung $T(4, 11)$ adalah:
$$d = MT = \sqrt{(4 - 4)^2 + (11 - (-2))^2} = \sqrt{0 + 13^2} = 13$$

Karena garis singgung tegak lurus jari-jari di titik singgung, segitiga $MPT$ dan $MQT$ merupakan segitiga siku-siku yang kongruen dengan panjang ruas garis singgung $t = \sqrt{d^2 - r^2} = \sqrt{169 - r^2}$.

Luas layang-layang $MPTQ$ adalah:
$$L = 2 \times \left(\frac{1}{2} \cdot r \cdot t\right) = r \cdot t = 60$$
Substitusikan nilai $t$:
$$r\sqrt{169 - r^2} = 60$$
Kuadratkan kedua ruas:
$$r^2(169 - r^2) = 3600$$
$$r^4 - 169r^2 + 3600 = 0$$
$$(r^2 - 25)(r^2 - 144) = 0$$

Diperoleh dua kemungkinan:
1. $r^2 = 25 \implies r = 5$, sehingga $t = \sqrt{169 - 25} = 12$ (memenuhi syarat $r < t$).
2. $r^2 = 144 \implies r = 12$, sehingga $t = \sqrt{169 - 144} = 5$ (tidak memenuhi syarat $r < t$).

Dengan mengambil $r^2 = 25$:
$$20 - m = 25 \implies m = 20 - 25 = -5$$

Jadi, nilai $m$ yang memenuhi adalah $-5$.
**Acuan:** siswa — siswa hal.84 Uji Kompetensi Bab 1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
