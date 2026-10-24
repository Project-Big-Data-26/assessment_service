# Lembar koreksi — kelas11_tl SMA11L-B2 subbab D: Faktor dan Pembuat Nol Polinomial

51 soal | easy 20, medium 20, hard 11 | variasi 20, orisinal 31
> **Kapasitas kurang (hard): 11 dari kuota 20** — Subbab D (p96-p100) tipis. Hanya sebelas soal yang benar-benar menuntut penalaran C5-C6 (evaluasi klaim, contoh penyangkal, temukan kesalahan, rancang, bandingkan). Soal parameter dan hitung langsung murni C3-C4 dan sudah dipakai di medium; membuat soal kembar berangka beda hanya demi kuota ditolak.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b02-d-easy-bt01-001
*variasi (angka) | C1 | 1 langkah | jenis: Teorema Faktor: faktor dari nilai nol*

Untuk suatu polinomial $P(x)$, nilai $P(8)$ adalah nol. Dengan demikian, .... pasti merupakan faktor polinomial tersebut.

- **A. $(x - 8)$** ✅  
  <sub>Benar: Teorema Faktor: $P(c)=0$ jika dan hanya jika $x-c$ faktor $P(x)$, dengan $c=8$.</sub>
- B. $(x + 8)$  
  <sub>Salah: salah tanda: memakai $x+c$ bukan $x-c$</sub>
- C. $(x - 8)^2$  
  <sub>Salah: mengira faktornya dikuadratkan padahal belum tentu</sub>
- D. $(8x - 1)$  
  <sub>Salah: menukar peran $x$ dan konstanta 8</sub>

**Pembahasan:** Karena $P(8)=0$, menurut Teorema Faktor $x-8$ adalah faktor $P(x)$.
**Acuan:** pretest — kelas11_tl-b02-p0101-latihan-d-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b02-d-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: Teorema Faktor: faktor dari nilai nol*

Untuk suatu polinomial $Q(x)$, nilai $Q(-12)$ adalah nol. Dengan demikian, .... pasti merupakan faktor polinomial tersebut.

- A. $(x - 12)$  
  <sub>Salah: mengambil tanda angka apa adanya tanpa memperhatikan $x-c$ dengan $c$ negatif</sub>
- B. $(x + 12)^2$  
  <sub>Salah: mengira faktornya dikuadratkan padahal belum tentu</sub>
- **C. $(x + 12)$** ✅  
  <sub>Benar: $Q(-12)=0$ sehingga $x-(-12)=x+12$ adalah faktor $Q(x)$.</sub>
- D. $(12x - 1)$  
  <sub>Salah: menukar peran $x$ dan konstanta</sub>

**Pembahasan:** Teorema Faktor: $x-c$ dengan $c=-12$ menjadi $x+12$.
**Acuan:** pretest — kelas11_tl-b02-p0101-latihan-d-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b02-d-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: titik potong sumbu-x dan faktor*

Grafik fungsi polinomial $P(x)$ memotong sumbu-$x$ di titik yang berabsis 5. Pernyataan yang pasti benar adalah ....

- A. $P(0) = 5$  
  <sub>Salah: menukar absis dan ordinat titik potong</sub>
- **B. $(x - 5)$ adalah faktor $P(x)$** ✅  
  <sub>Benar: Memotong sumbu-$x$ di $x=5$ berarti $P(5)=0$, jadi $x-5$ faktor.</sub>
- C. $P(-5) = 0$  
  <sub>Salah: salah tanda pada nilai absis</sub>
- D. $(x + 5)$ adalah faktor $P(x)$  
  <sub>Salah: salah tanda: pembuat nol 5 dikira menghasilkan faktor $x+5$</sub>

**Pembahasan:** Titik potong sumbu-$x$ adalah pembuat nol: $P(5)=0$, sehingga $x-5$ faktor $P(x)$.
**Acuan:** siswa — siswa hal.102 Latihan D Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b02-d-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: titik potong dari bentuk faktor*

Grafik fungsi $f(x) = (x + 5)(x - 4)(x - 8)$ memotong sumbu-$x$ di titik-titik ....

- **A. $(-5, 0)$, $(4, 0)$, dan $(8, 0)$** ✅  
  <sub>Benar: Setiap faktor sama dengan nol: $x=-5$, $x=4$, $x=8$.</sub>
- B. $(5, 0)$, $(-4, 0)$, dan $(-8, 0)$  
  <sub>Salah: semua tanda terbalik</sub>
- C. $(-5, 0)$, $(4, 0)$, dan $(-8, 0)$  
  <sub>Salah: salah tanda pada faktor ketiga</sub>
- D. $(-5, 0)$, $(-4, 0)$, dan $(-8, 0)$  
  <sub>Salah: semua pembuat nol dianggap negatif</sub>

**Pembahasan:** $x+5=0$ memberi $x=-5$; $x-4=0$ memberi $x=4$; $x-8=0$ memberi $x=8$.
**Acuan:** siswa — siswa hal.102 Latihan D Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b02-d-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: perpotongan grafik dengan sumbu-x*

Tentukan perpotongan grafik fungsi $g(x) = x^4 - 625$ terhadap sumbu-$x$.

- A. $(5, 0)$ saja  
  <sub>Salah: lupa pembuat nol negatif</sub>
- B. $(0, -625)$  
  <sub>Salah: menghitung titik potong sumbu-$y$, bukan sumbu-$x$</sub>
- **C. $(-5, 0)$ dan $(5, 0)$** ✅  
  <sub>Benar: $x^4-625=(x^2-25)(x^2+25)=(x-5)(x+5)(x^2+25)$; faktor $x^2+25$ tidak punya pembuat nol real.</sub>
- D. $(-25, 0)$ dan $(25, 0)$  
  <sub>Salah: mengakarkan 625 sekali saja seolah $x^2=625$</sub>

**Pembahasan:** $x^4-625=0$ memberi $x^2=25$ (karena $x^2=-25$ tidak real), sehingga $x=\pm 5$.
**Acuan:** siswa — siswa hal.101 Mari Mencoba 2.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b02-d-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: perpotongan grafik dengan sumbu-x*

Tentukan perpotongan grafik fungsi $h(x) = x^5 - 16x^3$ terhadap sumbu-$x$.

- A. $(0, 0)$ dan $(16, 0)$  
  <sub>Salah: menganggap $x^2=16$ hanya menghasilkan $x=16$ dan lupa akar negatif</sub>
- B. $(-16, 0)$, $(0, 0)$, dan $(16, 0)$  
  <sub>Salah: mengambil 16 langsung sebagai pembuat nol tanpa mengakarkan</sub>
- **C. $(-4, 0)$, $(0, 0)$, dan $(4, 0)$** ✅  
  <sub>Benar: $x^5-16x^3=x^3(x-4)(x+4)$ sehingga pembuat nolnya $-4$, $0$, dan $4$.</sub>
- D. $(-4, 0)$ dan $(4, 0)$  
  <sub>Salah: lupa pembuat nol $x=0$ dari faktor $x^3$</sub>

**Pembahasan:** $x^3(x^2-16)=0$ memberi $x=0$ atau $x=\pm 4$.
**Acuan:** siswa — siswa hal.101 Mari Mencoba 2.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b02-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: jumlah koefisien nol dan faktor x - 1*

Dina mengamati bahwa jumlah semua koefisien dan konstanta $P(x) = x^4 - 7x^3 + 6x^2 + 5x - 5$ sama dengan nol. Oleh karena itu, ia menyimpulkan bahwa .... merupakan salah satu faktor $P(x)$.

- A. $x + 1$  
  <sub>Salah: salah tanda pada pembuat nol 1</sub>
- B. $x - 5$  
  <sub>Salah: mengambil konstanta $-5$ sebagai pembuat nol</sub>
- C. $x - 4$  
  <sub>Salah: mengambil derajat polinomial sebagai pembuat nol</sub>
- **D. $x - 1$** ✅  
  <sub>Benar: Jumlah koefisien sama dengan $P(1)=1-7+6+5-5=0$, jadi $x-1$ faktor.</sub>

**Pembahasan:** $P(1)=1-7+6+5-5=0$, sehingga menurut Teorema Faktor $x-1$ faktor $P(x)$.
**Acuan:** siswa — siswa hal.96 Contoh 2.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b02-d-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: jumlah koefisien genap-ganjil dan faktor x + 1*

Pada $P(x) = 3x^3 + 6x^2 - 8x - 11$, seorang siswa mendapati bahwa koefisien suku berpangkat ganjil dan koefisien suku berpangkat genap mempunyai jumlah yang sama. Menurut Teorema Faktor, faktor $P(x)$ yang pasti adalah ....

- **A. $x + 1$** ✅  
  <sub>Benar: Jumlah koefisien ganjil $3-8=-5$ sama dengan genap $6-11=-5$, sehingga $P(-1)=0$ dan $x+1$ faktor.</sub>
- B. $x - 1$  
  <sub>Salah: mengira pembuat nolnya 1 (jumlah semua koefisien)</sub>
- C. $x - 3$  
  <sub>Salah: mengambil koefisien utama sebagai pembuat nol</sub>
- D. $x + 11$  
  <sub>Salah: mengambil konstanta $-11$ lalu salah tanda</sub>

**Pembahasan:** $P(-1)=-3+6+8-11=0$, jadi $x+1$ faktor $P(x)$.
**Acuan:** siswa — siswa hal.97 Mari Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b02-d-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: pembuat nol menjadi faktor lain*

Polinomial $P(x) = x^2 - 3x - 10$ mempunyai pembuat nol $-2$. Berdasarkan hubungan pembuat nol dan faktor, faktor $P(x)$ yang lain adalah ....

- A. $x + 10$  
  <sub>Salah: mengambil konstanta $-10$ lalu salah tanda</sub>
- B. $x - 2$  
  <sub>Salah: mengambil pembuat nol $-2$ menjadi $x-2$ (salah tanda)</sub>
- C. $x + 5$  
  <sub>Salah: salah tanda pada faktor pasangan</sub>
- **D. $x - 5$** ✅  
  <sub>Benar: Pembuat nol $-2$ memberi faktor $x+2$; $x^2-3x-10=(x+2)(x-5)$.</sub>

**Pembahasan:** $x^2-3x-10=(x+2)(x-5)$; faktor lainnya $x-5$.
**Acuan:** siswa — siswa hal.96 Eksplorasi Menuju Teorema Faktor

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b02-d-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: faktor menjadi pembuat nol*

Salah satu faktor polinomial $P(x)$ adalah $(2x - 9)$. Pembuat nol $P$ yang bersesuaian dengan faktor itu adalah ....

- A. $9$  
  <sub>Salah: mengabaikan koefisien 2 pada $x$</sub>
- B. $-\frac{9}{2}$  
  <sub>Salah: salah tanda</sub>
- C. $\frac{2}{9}$  
  <sub>Salah: membalik pecahan</sub>
- **D. $\frac{9}{2}$** ✅  
  <sub>Benar: $2x-9=0$ memberi $x=\frac{9}{2}$.</sub>

**Pembahasan:** $P(c)=0$ jika $2c-9=0$, yaitu $c=\frac{9}{2}$.
**Acuan:** siswa — siswa hal.96 Eksplorasi Menuju Teorema Faktor

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b02-d-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: sifat hasil kali nol*

Jumlah semua penyelesaian real persamaan $(x - 6)(2x + 5)(x + 1) = 0$ adalah ....

- A. $\frac{15}{2}$  
  <sub>Salah: memakai $+\frac{5}{2}$ (salah tanda penyelesaian $2x+5=0$)</sub>
- B. $-\frac{5}{2}$  
  <sub>Salah: membalik semua tanda penyelesaian</sub>
- C. $10$  
  <sub>Salah: memakai $x=5$ dari $2x+5$ tanpa dibagi 2 dan tanpa tanda</sub>
- **D. $\frac{5}{2}$** ✅  
  <sub>Benar: Penyelesaian: $6$, $-\frac{5}{2}$, dan $-1$; jumlahnya $\frac{5}{2}$.</sub>

**Pembahasan:** $x=6$, $x=-\frac{5}{2}$, $x=-1$. Jumlah: $6-\frac{5}{2}-1=\frac{5}{2}$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b02-d-easy-bt01-012
*orisinal | C2 | 2 langkah | jenis: calon pembuat nol rasional*

Polinomial $P(x) = 3x^3 - 5x^2 + 7x - 10$ berkoefisien bulat. Menurut Sifat Pembuat Nol Rasional, bilangan berikut yang memenuhi syarat sebagai calon pembuat nol rasional $P$ adalah ....

- **A. $\frac{10}{3}$** ✅  
  <sub>Benar: Pembilang 10 faktor dari konstanta 10 dan penyebut 3 faktor dari koefisien utama 3.</sub>
- B. $\frac{7}{3}$  
  <sub>Salah: pembilang 7 bukan faktor dari konstanta $-10$ (diambil dari koefisien $x$)</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: menukar peran pembilang dan penyebut</sub>
- D. $\frac{5}{2}$  
  <sub>Salah: penyebut 2 bukan faktor dari koefisien utama 3</sub>

**Pembahasan:** Pembilang $p$ faktor $10$: $\pm1,\pm2,\pm5,\pm10$; penyebut $q$ faktor $3$: $\pm1,\pm3$. Hanya $\frac{10}{3}$ yang sesuai.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b02-d-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: pembuat nol dari faktor kuadrat*

Diketahui $P(x) = (x - 1)(x^2 - 5x + 6)$. Pembuat nol real terbesar $P$ adalah ....

- A. $1$  
  <sub>Salah: hanya membaca faktor linear dan mengabaikan faktor kuadrat</sub>
- **B. $3$** ✅  
  <sub>Benar: $x^2-5x+6=(x-2)(x-3)$, pembuat nolnya $1$, $2$, $3$; yang terbesar $3$.</sub>
- C. $2$  
  <sub>Salah: memilih salah satu akar kuadrat, bukan yang terbesar</sub>
- D. $6$  
  <sub>Salah: mengambil konstanta faktor kuadrat sebagai pembuat nol</sub>

**Pembahasan:** $(x-1)(x-2)(x-3)=0$ sehingga pembuat nol $1, 2, 3$.
**Acuan:** siswa — siswa hal.97

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b02-d-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: menyusun polinomial dari pembuat nol*

Polinomial berderajat tiga $P(x)$ mempunyai pembuat nol $1$, $-3$, dan $4$, serta $P(0) = 24$. Koefisien $x^3$ pada $P(x)$ adalah ....

- A. $6$  
  <sub>Salah: membagi 24 dengan 4 saja (satu faktor)</sub>
- B. $24$  
  <sub>Salah: menyamakan koefisien utama dengan $P(0)$</sub>
- **C. $2$** ✅  
  <sub>Benar: $P(x)=a(x-1)(x+3)(x-4)$ dan $P(0)=12a=24$ sehingga $a=2$.</sub>
- D. $-2$  
  <sub>Salah: salah tanda: $(-1)(3)(4)=-12$ padahal $(-4)$ bertanda negatif</sub>

**Pembahasan:** $P(0)=a(-1)(3)(-4)=12a=24$, jadi $a=2$.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b02-d-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: mencari parameter dari faktor*

Jika $x - 2$ adalah faktor $P(x) = x^3 - 3x^2 + kx + 6$, nilai $k$ adalah ....

- A. $1$  
  <sub>Salah: salah tanda saat memindahkan $2k=-2$</sub>
- **B. $-1$** ✅  
  <sub>Benar: $P(2)=8-12+2k+6=2k+2=0$ sehingga $k=-1$.</sub>
- C. $2$  
  <sub>Salah: lupa konstanta 6 pada penjumlahan</sub>
- D. $-7$  
  <sub>Salah: mensubstitusi $x=-2$ padahal pembuat nolnya $2$</sub>

**Pembahasan:** $P(2)=0 \Rightarrow 2k+2=0 \Rightarrow k=-1$.
**Acuan:** siswa — siswa hal.96

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b02-d-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: perpotongan dengan sumbu-y*

Grafik fungsi $f(x) = (x - 3)(x + 4)(2x - 1)$ memotong sumbu-$y$ di titik ....

- **A. $(0, 12)$** ✅  
  <sub>Benar: $f(0)=(-3)(4)(-1)=12$.</sub>
- B. $(0, -12)$  
  <sub>Salah: lupa bahwa $-3$ dan $-1$ keduanya negatif sehingga hasilnya positif</sub>
- C. $(0, 0)$  
  <sub>Salah: mengira grafik melalui titik asal</sub>
- D. $(12, 0)$  
  <sub>Salah: menukar absis dan ordinat</sub>

**Pembahasan:** Substitusi $x=0$: $f(0)=(-3)(4)(-1)=12$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b02-d-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: uji nilai P(c) untuk faktor*

Di antara bentuk berikut, yang merupakan faktor $P(x) = x^3 + 2x^2 - 5x - 6$ adalah ....

- A. $x - 3$  
  <sub>Salah: $P(3)=24\neq 0$; memilih faktor konstanta tanpa menguji</sub>
- B. $x - 1$  
  <sub>Salah: $P(1)=-8\neq 0$; mengira jumlah koefisien nol</sub>
- **C. $x - 2$** ✅  
  <sub>Benar: $P(2)=8+8-10-6=0$.</sub>
- D. $x + 2$  
  <sub>Salah: $P(-2)=4\neq 0$; salah tanda pembuat nol</sub>

**Pembahasan:** Hanya $P(2)=0$; nilai $P(-2)=4$, $P(1)=-8$, $P(3)=24$.
**Acuan:** siswa — siswa hal.96

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b02-d-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: banyak pembuat nol real*

Banyak pembuat nol real yang berbeda dari $P(x) = (x - 2)(x + 5)(x^2 + 4)$ adalah ....

- A. $4$  
  <sub>Salah: menghitung derajat polinomial sebagai banyak pembuat nol</sub>
- B. $3$  
  <sub>Salah: menganggap faktor $x^2+4$ memberi satu pembuat nol real</sub>
- C. $1$  
  <sub>Salah: mengira hanya faktor pertama yang menghasilkan pembuat nol</sub>
- **D. $2$** ✅  
  <sub>Benar: $x=2$ dan $x=-5$; $x^2+4=0$ tidak punya penyelesaian real.</sub>

**Pembahasan:** Faktor $x^2+4>0$ untuk semua $x$ real, sehingga pembuat nol real hanya $2$ dan $-5$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b02-d-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: menyusun polinomial dari pembuat nol*

Polinomial berderajat tiga $P(x)$ dengan koefisien $x^3$ sama dengan 1 mempunyai pembuat nol $0$, $3$, dan $-4$. Nilai $P(2)$ adalah ....

- A. $-6$  
  <sub>Salah: melupakan faktor $x$ dari pembuat nol 0</sub>
- **B. $-12$** ✅  
  <sub>Benar: $P(x)=x(x-3)(x+4)$ sehingga $P(2)=2\cdot(-1)\cdot 6=-12$.</sub>
- C. $-20$  
  <sub>Salah: memakai faktor $(x+3)$ dan $(x-4)$ (tanda pembuat nol terbalik)</sub>
- D. $4$  
  <sub>Salah: memakai faktor $(x-3)$ dan $(x-4)$ (tanda pembuat nol $-4$ salah)</sub>

**Pembahasan:** $P(2)=2(2-3)(2+4)=2\cdot(-1)\cdot 6=-12$.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b02-d-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: banyak calon pembuat nol rasional*

Menurut Sifat Pembuat Nol Rasional, banyak bilangan bulat yang mungkin menjadi pembuat nol $P(x) = x^3 - 4x^2 + x + 12$ adalah ....

- A. $24$  
  <sub>Salah: menghitung ulang tiap calon dua kali</sub>
- **B. $12$** ✅  
  <sub>Benar: Koefisien utama 1, jadi calon adalah faktor 12: $\pm1,\pm2,\pm3,\pm4,\pm6,\pm12$, yaitu 12 bilangan.</sub>
- C. $4$  
  <sub>Salah: menghitung faktor 12 selain 1 dan 12 saja tanpa tanda</sub>
- D. $6$  
  <sub>Salah: hanya menghitung faktor positif</sub>

**Pembahasan:** Faktor positif 12: 1, 2, 3, 4, 6, 12 (6 bilangan); dengan tanda $\pm$ menjadi 12.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b02-d-medium-bt01-001
*variasi (angka) | C3 | 4 langkah | jenis: faktorisasi kubik dengan pembuat nol pecahan*

Faktorkan $P(x) = 3x^3 - 8x^2 - x + 10$ secara lengkap. Bentuk faktor lengkap $P(x)$ adalah ....

- A. $(3x + 5)(x - 2)(x + 1)$  
  <sub>Salah: salah tanda pada faktor $3x-5$</sub>
- B. $\left(x - \frac{5}{3}\right)(x - 2)(x + 1)$  
  <sub>Salah: menuliskan pembuat nol pecahan sebagai $x-\frac{5}{3}$ sehingga koefisien utama 3 hilang</sub>
- **C. $(3x - 5)(x - 2)(x + 1)$** ✅  
  <sub>Benar: $P(2)=0$ sehingga $x-2$ faktor; hasil bagi $3x^2-2x-5=(3x-5)(x+1)$.</sub>
- D. $(3x - 5)(x + 2)(x - 1)$  
  <sub>Salah: membalik tanda dua pembuat nol lainnya</sub>

**Pembahasan:** $P(2)=24-32-2+10=0$, jadi $x-2$ faktor. Pembagian: $3x^3-8x^2-x+10=(x-2)(3x^2-2x-5)$, dan $3x^2-2x-5=(3x-5)(x+1)$.
**Acuan:** pretest — kelas11_tl-b02-p0102-latihan-d-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b02-d-medium-bt01-002
*variasi (angka) | C3 | 4 langkah | jenis: faktorisasi kuartik dari dua pembuat nol*

Polinomial $P(x) = x^4 + x^3 - 31x^2 - x + 30$ memenuhi $P(-6) = 0$ dan $P(5) = 0$. Bentuk faktor lengkap $P(x)$ adalah ....

- A. $(x - 6)(x + 5)(x - 1)(x + 1)$  
  <sub>Salah: membalik tanda pembuat nol $-6$ dan $5$ saat menulis faktor</sub>
- B. $(x + 6)(x - 5)(x + 1)(x + 1)$  
  <sub>Salah: salah menulis faktor dari $x^2-1$ (kedua faktor sama)</sub>
- **C. $(x + 6)(x - 5)(x - 1)(x + 1)$** ✅  
  <sub>Benar: $(x+6)(x-5)=x^2+x-30$; hasil baginya $x^2-1=(x-1)(x+1)$.</sub>
- D. $(x + 6)(x - 5)(x - 1)(x - 1)$  
  <sub>Salah: salah menulis faktor dari $x^2-1$ (kedua faktor sama)</sub>

**Pembahasan:** $(x+6)(x-5)=x^2+x-30$. $P(x)\div(x^2+x-30)=x^2-1$, sehingga $P(x)=(x+6)(x-5)(x-1)(x+1)$.
**Acuan:** siswa — siswa hal.102 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b02-d-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: selisih pembuat nol terbesar dan terkecil*

Jika $P(x) = x^4 - 4x^3 - 23x^2 + 54x + 72$ dengan $P(-1) = 0$ dan $P(3) = 0$, selisih pembuat nol terbesar dan pembuat nol terkecil $P$ adalah ....

- A. $4$  
  <sub>Salah: hanya memakai selisih dua pembuat nol yang diketahui, $3-(-1)$</sub>
- B. $24$  
  <sub>Salah: mengambil konstanta faktor kuadrat $-24$ sebagai selisih</sub>
- C. $7$  
  <sub>Salah: memakai $6-(-1)$ sehingga pembuat nol $-4$ terlewat</sub>
- **D. $10$** ✅  
  <sub>Benar: Hasil bagi oleh $(x+1)(x-3)$ adalah $x^2-2x-24=(x-6)(x+4)$; pembuat nol $-4,-1,3,6$, selisih $6-(-4)=10$.</sub>

**Pembahasan:** $(x+1)(x-3)=x^2-2x-3$. $P(x)=(x^2-2x-3)(x^2-2x-24)$ dan $x^2-2x-24=(x-6)(x+4)$. Pembuat nol: $-4,-1,3,6$; selisih terbesar-terkecil $=10$.
**Acuan:** siswa — siswa hal.102 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b02-d-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: menyusun polinomial dari pembuat nol dan koefisien*

Polinomial berderajat 4 yang pembuat nolnya $-5$, $0$, $6$, dan $8$ serta koefisien $x^2$-nya adalah $66$ ialah ....

- A. $-3x^4 - 27x^3 + 66x^2 + 720x$  
  <sub>Salah: membalik tanda semua pembuat nol saat menyusun faktor</sub>
- **B. $-3x^4 + 27x^3 + 66x^2 - 720x$** ✅  
  <sub>Benar: $P(x)=a\,x(x+5)(x-6)(x-8)$ memberi koefisien $x^2$ sebesar $-22a$; $-22a=66$ sehingga $a=-3$.</sub>
- C. $x^4 - 9x^3 - 22x^2 + 240x$  
  <sub>Salah: lupa mengalikan dengan konstanta $a$ sehingga koefisien $x^2$ menjadi $-22$</sub>
- D. $3x^4 - 27x^3 - 66x^2 + 720x$  
  <sub>Salah: memakai $a=3$ (salah tanda) padahal koefisien $x^2$ polinomial dasar adalah $-22$</sub>

**Pembahasan:** $x(x+5)(x-6)(x-8)=x^4 - 9x^3 - 22x^2 + 240x$. Koefisien $x^2$ adalah $-22$, jadi $a=-3$ dan $P(x)=-3x^4 + 27x^3 + 66x^2 - 720x$.
**Acuan:** siswa — siswa hal.102 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b02-d-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: koefisien polinomial dari pembuat nol*

Polinomial berderajat 4 mempunyai pembuat nol $-6$, $0$, $5$, dan $7$ serta koefisien $x^2$ sama dengan $74$. Koefisien $x$ pada polinomial tersebut adalah ....

- A. $-210$  
  <sub>Salah: salah tanda pada koefisien $x$ polinomial dasar lalu dikalikan $a$ yang salah tanda</sub>
- B. $420$  
  <sub>Salah: memakai $a=2$ (salah tanda) dari $37a=74$</sub>
- **C. $-420$** ✅  
  <sub>Benar: $P(x)=a\,x(x+6)(x-5)(x-7)=a(x^4-6x^3-37x^2+210x)$; $-37a=74$ sehingga $a=-2$ dan koefisien $x$ adalah $210a=-420$.</sub>
- D. $210$  
  <sub>Salah: lupa mengalikan dengan $a=-2$</sub>

**Pembahasan:** $x(x+6)(x-5)(x-7)=x^4-6x^3-37x^2+210x$. Dari $-37a=74$ diperoleh $a=-2$, sehingga koefisien $x$ sama dengan $-420$.
**Acuan:** siswa — siswa hal.102 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b02-d-medium-bt01-006
*variasi (angka) | C3 | 4 langkah | jenis: mencari dua parameter dari dua faktor*

Jika $x - 2$ dan $x + 5$ adalah faktor dari $P(x) = 3x^3 + ax^2 + bx - 40$, nilai $a$ dan $b$ berturut-turut adalah ....

- A. $a = -13$ dan $b = 18$  
  <sub>Salah: salah tanda pada kedua parameter</sub>
- B. $a = -18$ dan $b = 13$  
  <sub>Salah: menukar nilai $a$ dan $b$</sub>
- C. $a = 13$ dan $b = 18$  
  <sub>Salah: salah tanda pada $b$ saat eliminasi</sub>
- **D. $a = 13$ dan $b = -18$** ✅  
  <sub>Benar: $P(2)=0$ memberi $4a+2b=16$ dan $P(-5)=0$ memberi $25a-5b=415$, sehingga $a=13$, $b=-18$.</sub>

**Pembahasan:** $P(2)=24+4a+2b-40=0 \Rightarrow 2a+b=8$. $P(-5)=-375+25a-5b-40=0 \Rightarrow 5a-b=83$. Dijumlahkan: $7a=91$, $a=13$, $b=-18$.
**Acuan:** siswa — siswa hal.103 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b02-d-medium-bt01-007
*variasi (angka) | C3 | 4 langkah | jenis: pembuat nol ketiga dari dua faktor dan parameter*

Jika $x + 3$ dan $x - 4$ adalah faktor dari $P(x) = 4x^3 + ax^2 + bx + 60$, pembuat nol ketiga $P$ adalah ....

- A. $5$  
  <sub>Salah: mengabaikan koefisien utama 4 pada faktor $4x-5$</sub>
- **B. $\frac{5}{4}$** ✅  
  <sub>Benar: Diperoleh $a=-9$ dan $b=-43$; $P(x)=(x+3)(x-4)(4x-5)$ sehingga pembuat nol ketiga $\frac{5}{4}$.</sub>
- C. $\frac{4}{5}$  
  <sub>Salah: membalik pecahan pembuat nol</sub>
- D. $-\frac{5}{4}$  
  <sub>Salah: salah tanda pada pembuat nol dari faktor $4x-5$</sub>

**Pembahasan:** $P(-3)=0$ dan $P(4)=0$ memberi $a=-9$, $b=-43$. Bagi $P(x)$ dengan $(x+3)(x-4)=x^2-x-12$ menghasilkan $4x-5$, sehingga pembuat nol ketiga $\frac{5}{4}$.
**Acuan:** siswa — siswa hal.103 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b02-d-medium-bt01-008
*variasi (angka) | C4 | 4 langkah | jenis: pemodelan volume balok menjadi persamaan kubik*

Sebuah bak penampung berbentuk balok memiliki panjang 2 meter kurang dari tiga kali lebarnya, sedangkan tingginya 1 meter lebih dari lebarnya. Jika volume bak tersebut 390 m$^3$, luas seluruh permukaan bak tersebut adalah ....

- **A. $346$ m$^2$** ✅  
  <sub>Benar: $w(3w-2)(w+1)=390$ memberi $w=5$; $p=13$, $t=6$; luas $=2(65+78+30)=346$.</sub>
- B. $390$ m$^2$  
  <sub>Salah: memberi nilai volume sebagai luas permukaan</sub>
- C. $173$ m$^2$  
  <sub>Salah: lupa mengalikan dengan 2 pada rumus luas permukaan</sub>
- D. $286$ m$^2$  
  <sub>Salah: luas permukaan tanpa memasukkan sisi lebar kali tinggi</sub>

**Pembahasan:** Misalkan lebar $w$. $w(3w-2)(w+1)=390 \Rightarrow 3w^3+w^2-2w-390=0$, $w=5$ (satu-satunya pembuat nol positif). Ukuran $13\times5\times6$, luas $2(65+78+30)=346$.
**Acuan:** siswa — siswa hal.103 Latihan D Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b02-d-medium-bt01-009
*variasi (angka) | C3 | 4 langkah | jenis: perpotongan sumbu-x dengan pembuat nol pecahan*

Tentukan perpotongan grafik fungsi $f(x) = 2x^3 + 9x^2 - 38x - 21$ terhadap sumbu-$x$.

- A. $(7, 0)$, $\left(\frac{1}{2}, 0\right)$, dan $(-3, 0)$  
  <sub>Salah: membalik tanda semua pembuat nol</sub>
- **B. $(-7, 0)$, $\left(-\frac{1}{2}, 0\right)$, dan $(3, 0)$** ✅  
  <sub>Benar: $f(3)=0$; hasil bagi $2x^2+15x+7=(2x+1)(x+7)$ sehingga pembuat nol $3$, $-\frac{1}{2}$, $-7$.</sub>
- C. $(-7, 0)$, $(-2, 0)$, dan $(3, 0)$  
  <sub>Salah: mengambil pembuat nol $2x+1=0$ sebagai $-2$</sub>
- D. $(-7, 0)$, $\left(-\frac{1}{2}, 0\right)$, dan $(-3, 0)$  
  <sub>Salah: salah tanda pada pembuat nol 3</sub>

**Pembahasan:** Uji $x=3$: $54+81-114-21=0$. Horner: $2,\,15,\,7$ sehingga $f(x)=(x-3)(2x^2+15x+7)=(x-3)(2x+1)(x+7)$.
**Acuan:** siswa — siswa hal.100 Contoh 2.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b02-d-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: himpunan pembuat nol kubik*

Himpunan semua pembuat nol real dari $P(x) = 4x^3 - 4x^2 - 9x + 9$ adalah ....

- **A. $\left\{-\frac{3}{2}, 1, \frac{3}{2}\right\}$** ✅  
  <sub>Benar: $P(x)=4x^2(x-1)-9(x-1)=(x-1)(2x-3)(2x+3)$.</sub>
- B. $\left\{-\frac{3}{2}, \frac{3}{2}\right\}$  
  <sub>Salah: lupa pembuat nol dari faktor $x-1$</sub>
- C. $\{-3, 1, 3\}$  
  <sub>Salah: mengabaikan koefisien 2 pada faktor $2x\pm3$</sub>
- D. $\left\{-\frac{3}{2}, -1, \frac{3}{2}\right\}$  
  <sub>Salah: salah tanda pada pembuat nol dari faktor $x-1$</sub>

**Pembahasan:** $P(1)=4-4-9+9=0$. $P(x)=(x-1)(4x^2-9)=(x-1)(2x-3)(2x+3)$ sehingga pembuat nol $1$, $\frac{3}{2}$, $-\frac{3}{2}$.
**Acuan:** siswa — siswa hal.98 Mari Mencoba 2.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b02-d-medium-bt01-011
*orisinal | C3 | 4 langkah | jenis: parameter dari faktor lalu pembuat nol terkecil*

Jika $x - 2$ adalah faktor dari $P(x) = x^3 - x^2 + kx + 24$, pembuat nol terkecil $P$ adalah ....

- **A. $-4$** ✅  
  <sub>Benar: $P(2)=0$ memberi $k=-14$; $P(x)=(x-2)(x^2+x-12)=(x-2)(x+4)(x-3)$, pembuat nol terkecil $-4$.</sub>
- B. $-2$  
  <sub>Salah: mengira faktor $x-2$ memberi pembuat nol $-2$ dan berhenti di situ</sub>
- C. $4$  
  <sub>Salah: salah tanda pada pembuat nol dari faktor $x+4$</sub>
- D. $-3$  
  <sub>Salah: salah tanda pada pembuat nol dari faktor $x-3$ lalu memilihnya sebagai yang terkecil</sub>

**Pembahasan:** $P(2)=8-4+2k+24=0$ sehingga $k=-14$. Hasil bagi $x^2+x-12=(x+4)(x-3)$; pembuat nol $-4$, $2$, $3$.
**Acuan:** siswa — siswa hal.96

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b02-d-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: pembuat nol rasional bukan bilangan bulat*

Polinomial $P(x) = 3x^3 - 16x^2 + 3x + 10$ mempunyai tepat satu pembuat nol yang bukan bilangan bulat. Pembuat nol tersebut adalah ....

- **A. $-\frac{2}{3}$** ✅  
  <sub>Benar: $P(1)=0$; hasil bagi $3x^2-13x-10=(3x+2)(x-5)$, sehingga pembuat nol $1$, $5$, dan $-\frac{2}{3}$.</sub>
- B. $-\frac{3}{2}$  
  <sub>Salah: membalik pecahan pembuat nol</sub>
- C. $\frac{10}{3}$  
  <sub>Salah: memakai konstanta 10 dan koefisien utama 3 langsung tanpa menguji</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: salah tanda pada pembuat nol dari faktor $3x+2$</sub>

**Pembahasan:** $P(1)=3-16+3+10=0$. Hasil bagi oleh $x-1$ adalah $3x^2-13x-10=(3x+2)(x-5)$. Pembuat nol: $1$, $5$, $-\frac{2}{3}$.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b02-d-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: titik potong sumbu-y dari pembuat nol dan satu titik*

Grafik fungsi polinomial berderajat tiga $f$ memotong sumbu-$x$ di $(-2, 0)$, $(1, 0)$, dan $(4, 0)$, serta melalui titik $(3, 10)$. Grafik $f$ memotong sumbu-$y$ di titik ....

- A. $(0, 10)$  
  <sub>Salah: menyamakan ordinat titik potong sumbu-$y$ dengan ordinat titik yang diketahui</sub>
- B. $(-8, 0)$  
  <sub>Salah: menukar absis dan ordinat</sub>
- C. $(0, 8)$  
  <sub>Salah: memakai $a=1$ (salah tanda) sehingga ordinat positif</sub>
- **D. $(0, -8)$** ✅  
  <sub>Benar: $f(x)=a(x+2)(x-1)(x-4)$, $f(3)=-10a=10$ sehingga $a=-1$; $f(0)=-1\cdot2\cdot(-1)\cdot(-4)=-8$.</sub>

**Pembahasan:** $f(x)=a(x+2)(x-1)(x-4)$. $f(3)=a\cdot5\cdot2\cdot(-1)=-10a=10$, $a=-1$. $f(0)=-1\cdot2\cdot(-1)\cdot(-4)=-8$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b02-d-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: parameter agar jumlah koefisien genap sama dengan ganjil*

Polinomial $P(x) = 4x^3 + ax^2 - 7x + 11$ mempunyai faktor $x + 1$. Nilai $a$ adalah ....

- A. $-8$  
  <sub>Salah: memakai $P(1)=0$ padahal faktornya $x+1$ (pembuat nol $-1$)</sub>
- B. $-3$  
  <sub>Salah: lupa konstanta 11 pada penjumlahan koefisien genap</sub>
- **C. $-14$** ✅  
  <sub>Benar: $P(-1)=-4+a+7+11=a+14=0$ sehingga $a=-14$.</sub>
- D. $14$  
  <sub>Salah: salah tanda saat memindahkan $a+14=0$</sub>

**Pembahasan:** Faktor $x+1$ berarti $P(-1)=0$: koefisien ganjil $4-7=-3$ sama dengan genap $a+11$, sehingga $a=-14$.
**Acuan:** siswa — siswa hal.97

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b02-d-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: jumlah pembuat nol real berbeda dari faktor kuadrat*

Diketahui $P(x) = (x^2 - 4x + 4)(x^2 - x - 12)(x^2 + 3x + 5)$. Jumlah semua pembuat nol real yang berbeda dari $P$ adalah ....

- A. $-3$  
  <sub>Salah: membalik tanda semua pembuat nol</sub>
- B. $5$  
  <sub>Salah: menghitung pembuat nol $2$ dua kali (jumlah dengan kelipatan)</sub>
- **C. $3$** ✅  
  <sub>Benar: $x^2-4x+4=(x-2)^2$ memberi $2$; $x^2-x-12=(x-4)(x+3)$ memberi $4$ dan $-3$; $x^2+3x+5$ diskriminan $-11<0$. Jumlah $2+4-3=3$.</sub>
- D. $0$  
  <sub>Salah: ikut menjumlahkan akar tak real dari $x^2+3x+5$ (jumlahnya $-3$)</sub>

**Pembahasan:** Pembuat nol real berbeda: $2$, $4$, $-3$; faktor $x^2+3x+5$ tidak punya pembuat nol real karena diskriminannya $9-20<0$. Jumlahnya $3$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b02-d-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: jarak titik potong sumbu-x terjauh*

Grafik fungsi $f(x) = (x^2 - 4)(x^2 - 2x - 15)$ memotong sumbu-$x$ di empat titik. Jarak terjauh antara dua titik potong tersebut adalah ... satuan.

- A. $15$  
  <sub>Salah: mengambil konstanta faktor kuadrat sebagai jarak</sub>
- B. $7$  
  <sub>Salah: memakai $5-(-2)$ sehingga titik potong $x=-3$ terlewat</sub>
- C. $4$  
  <sub>Salah: hanya memakai jarak titik potong dari faktor $x^2-4$</sub>
- **D. $8$** ✅  
  <sub>Benar: $x^2-4=(x-2)(x+2)$ dan $x^2-2x-15=(x-5)(x+3)$; titik potong $x=-3,-2,2,5$; jarak terjauh $5-(-3)=8$.</sub>

**Pembahasan:** Titik potong pada $x=-3,-2,2,5$. Jarak terjauh adalah antara $x=-3$ dan $x=5$, yaitu $8$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b02-d-medium-bt01-017
*orisinal | C4 | 4 langkah | jenis: persamaan kubik dengan pengelompokan*

Jumlah kuadrat semua penyelesaian real persamaan $x^3 + 4x^2 = 9x + 36$ adalah ....

- A. $25$  
  <sub>Salah: lupa penyelesaian $x=-3$ sehingga $16+9$</sub>
- **B. $34$** ✅  
  <sub>Benar: $x^2(x+4)-9(x+4)=(x+4)(x-3)(x+3)=0$ memberi $-4$, $3$, $-3$; kuadratnya $16+9+9=34$.</sub>
- C. $18$  
  <sub>Salah: lupa penyelesaian $x=-4$ sehingga hanya $9+9$</sub>
- D. $-4$  
  <sub>Salah: menjumlahkan penyelesaian tanpa mengkuadratkan</sub>

**Pembahasan:** $x^3+4x^2-9x-36=0 \Rightarrow (x+4)(x^2-9)=0$. Penyelesaian $-4$, $3$, $-3$; jumlah kuadrat $16+9+9=34$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b02-d-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: pemodelan volume balok dan hasil bagi*

Volume sebuah balok dinyatakan oleh $V(x) = x^3 + 3x^2 - 10x - 24$ cm$^3$ dengan tinggi $(x - 3)$ cm. Untuk $x = 5$, luas alas balok tersebut adalah ... cm$^2$.

- A. $18$  
  <sub>Salah: mengalikan tinggi dengan salah satu sisi alas saja</sub>
- B. $126$  
  <sub>Salah: mengira nilai $V(5)$ (volume) sebagai luas alas</sub>
- C. $14$  
  <sub>Salah: mengalikan tinggi dengan sisi alas yang lain</sub>
- **D. $63$** ✅  
  <sub>Benar: $V(3)=0$ sehingga $x-3$ faktor; luas alas $=V(x)\div(x-3)=x^2+6x+8$, untuk $x=5$ bernilai $63$.</sub>

**Pembahasan:** Horner dengan $c=3$: $1,\,6,\,8$, sisa $0$. Luas alas $=x^2+6x+8=(x+2)(x+4)$, untuk $x=5$: $7\times9=63$.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b02-d-medium-bt01-019
*orisinal | C4 | 4 langkah | jenis: menilai kebenaran pernyataan tentang pembuat nol*

Diberikan $P(x) = 2x^3 - 3x^2 - 11x + 6$. Pernyataan yang benar adalah ....

- **A. jumlah semua pembuat nol $P$ adalah $\frac{3}{2}$** ✅  
  <sub>Benar: $P(x)=(x-3)(x+2)(2x-1)$, pembuat nolnya $3$, $-2$, $\frac{1}{2}$ dengan jumlah $\frac{3}{2}$.</sub>
- B. $P$ mempunyai tepat dua pembuat nol real  
  <sub>Salah: kubik ini mempunyai tiga pembuat nol real berbeda</sub>
- C. hasil kali semua pembuat nol $P$ adalah $3$  
  <sub>Salah: salah tanda: hasil kali sebenarnya $3\cdot(-2)\cdot\frac{1}{2}=-3$</sub>
- D. $x + 3$ adalah faktor $P(x)$  
  <sub>Salah: $P(-3)=-42\neq0$; salah tanda pada pembuat nol 3</sub>

**Pembahasan:** $P(3)=0$, hasil bagi $2x^2+3x-2=(2x-1)(x+2)$. Pembuat nol $3,-2,\frac{1}{2}$: jumlah $\frac{3}{2}$, hasil kali $-3$; ada tiga pembuat nol; $P(-3)=-42$.
**Acuan:** siswa — siswa hal.96

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b02-d-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: hasil bagi Horner setelah uji jumlah koefisien*

Jumlah semua koefisien dan konstanta $P(x) = 2x^4 - 3x^3 - 17x^2 + 27x - 9$ sama dengan nol. Hasil bagi $P(x)$ oleh faktor linear yang dijamin oleh fakta tersebut adalah ....

- A. $2x^3 - 5x^2 - 12x + 39$  
  <sub>Salah: membagi dengan $x+1$ (pembuat nol $-1$) padahal jumlah koefisien nol menjamin $x-1$</sub>
- **B. $2x^3 - x^2 - 18x + 9$** ✅  
  <sub>Benar: $P(1)=0$ sehingga $x-1$ faktor; Horner dengan $c=1$ menghasilkan koefisien $2,-1,-18,9$ dan sisa $0$.</sub>
- C. $2x^3 + x^2 - 18x + 9$  
  <sub>Salah: salah tanda pada koefisien $x^2$ (menghitung $-3+2$ sebagai $+1$)</sub>
- D. $2x^3 - x^2 - 18x$  
  <sub>Salah: menganggap sisa $0$ sebagai suku konstanta hasil bagi</sub>

**Pembahasan:** Horner $c=1$: $2$; $-3+2=-1$; $-17-1=-18$; $27-18=9$; $-9+9=0$. Hasil bagi $2x^3-x^2-18x+9$.
**Acuan:** siswa — siswa hal.97

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b02-d-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: contoh penyangkal klaim jumlah koefisien nol*

Dani mengklaim: "Jika jumlah semua koefisien dan konstanta suatu polinomial sama dengan nol, maka $(x - 1)^2$ merupakan faktor polinomial itu." Polinomial berikut yang menjadi contoh penyangkal klaim Dani adalah ....

- A. $x^3 - 3x^2 + 3x - 1$  
  <sub>Salah: jumlah koefisien nol dan memang $(x-1)^3$, sehingga klaim Dani justru terpenuhi, bukan terbantah</sub>
- B. $x^3 + 2x^2 - 5x + 3$  
  <sub>Salah: jumlah koefisiennya $1$, bukan nol; syarat klaim tidak terpenuhi sehingga bukan contoh penyangkal</sub>
- C. $x^3 - x^2 - x + 1$  
  <sub>Salah: jumlah koefisien nol dan $=(x-1)^2(x+1)$, klaim Dani terpenuhi</sub>
- **D. $x^3 + 2x^2 - 5x + 2$** ✅  
  <sub>Benar: jumlah koefisiennya $1+2-5+2=0$ sehingga $x-1$ faktor, tetapi $x^3+2x^2-5x+2=(x-1)(x^2+3x-2)$ dan $x^2+3x-2$ bernilai $2$ di $x=1$, jadi $(x-1)^2$ bukan faktor</sub>

**Pembahasan:** Contoh penyangkal harus memenuhi syarat (jumlah koefisien nol) tetapi simpulannya gagal. Jumlah koefisien: $0$, $0$, $0$, $1$. Faktorisasi: $(x-1)^3$, $(x-1)^2(x+1)$, $(x-1)(x^2+3x-2)$ dengan $x^2+3x-2$ di $x=1$ bernilai $2\neq 0$. Hanya $x^3+2x^2-5x+2$ yang memenuhi syarat tetapi tidak punya faktor $(x-1)^2$.
**Acuan:** siswa — siswa hal.96

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b02-d-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan penerapan Teorema Faktor*

Rina memfaktorkan $P(x) = x^3 - 4x^2 - 11x + 30$. Pekerjaannya: "$P(-3) = -27 - 36 + 33 + 30 = 0$. Berdasarkan Teorema Faktor, $x - 3$ adalah faktor $P(x)$."

Pernyataan yang tepat mengenai pekerjaan Rina adalah ....

- A. Hitungan $P(-3)$ keliru, nilai yang benar adalah $-12$, sehingga tidak ada faktor yang dapat disimpulkan  
  <sub>Salah: $-12$ adalah nilai $P(3)$, bukan $P(-3)$; $P(-3)=0$ memang benar</sub>
- B. Teorema Faktor tidak dapat dipakai karena $c = -3$ bukan bilangan bulat positif  
  <sub>Salah: Teorema Faktor berlaku untuk setiap bilangan real $c$</sub>
- **C. Hitungan $P(-3) = 0$ benar, tetapi faktor yang bersesuaian adalah $x + 3$, bukan $x - 3$** ✅  
  <sub>Benar: $P(-3)=0$ benar; Teorema Faktor dengan $c=-3$ memberi faktor $x-(-3)=x+3$, dan $P(3)=-12\neq 0$ sehingga $x-3$ bukan faktor</sub>
- D. Pekerjaan Rina seluruhnya benar karena $P(-3) = 0$ berarti $x - 3$ adalah faktor  
  <sub>Salah: mengabaikan tanda: faktor untuk $c=-3$ adalah $x+3$</sub>

**Pembahasan:** $P(-3)=-27-36+33+30=0$ benar. Teorema Faktor: $P(c)=0$ jika dan hanya jika $x-c$ faktor. Untuk $c=-3$ faktornya $x+3$. Pengecekan $P(3)=27-36-33+30=-12\neq 0$ menunjukkan $x-3$ bukan faktor.
**Acuan:** siswa — siswa hal.99

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b02-d-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: contoh penyangkal klaim pembuat nol rasional*

Sinta mengklaim: "Jika polinomial berkoefisien bulat memiliki pembuat nol rasional, maka polinomial itu pasti memiliki pembuat nol yang bilangan bulat." Polinomial berkoefisien bulat berikut yang menjadi contoh penyangkal klaim Sinta adalah ....

- **A. $2x^3 + x^2 + 5x - 3$** ✅  
  <sub>Benar: calon $\pm1,\pm3,\pm\frac12,\pm\frac32$; hanya $\frac12$ yang nol ($P(\frac12)=\frac14+\frac14+\frac52-3=0$), tidak ada pembuat nol bulat</sub>
- B. $x^3 - 2x^2 + x - 2$  
  <sub>Salah: punya pembuat nol bulat $2$, jadi klaim Sinta terpenuhi</sub>
- C. $2x^3 - 3x^2 - 2x + 3$  
  <sub>Salah: punya pembuat nol pecahan $\frac32$ tetapi juga pembuat nol bulat $\pm1$, sehingga bukan penyangkal</sub>
- D. $x^3 - 2x + 5$  
  <sub>Salah: tidak punya pembuat nol rasional sama sekali (calon $\pm1,\pm5$ semuanya gagal), jadi syarat klaim tidak terpenuhi</sub>

**Pembahasan:** Penyangkal harus punya pembuat nol rasional tetapi tidak satu pun bulat. $x^3-2x^2+x-2=(x-2)(x^2+1)$ punya nol bulat $2$. $x^3-2x+5$ tidak punya pembuat nol rasional. $2x^3-3x^2-2x+3=(x-1)(x+1)(2x-3)$ punya nol bulat $\pm1$. Pada $2x^3+x^2+5x-3=(2x-1)(x^2+x+3)$ satu-satunya pembuat nol real adalah $\frac12$, yang bukan bilangan bulat.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b02-d-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: kasus terlewat dalam penalaran siswa*

Diketahui $P(x) = (x - 2)(x^2 + bx + 9)$ dengan $b$ bilangan real. Dina menyimpulkan: "Agar $P$ memiliki tepat dua pembuat nol real yang berbeda, faktor kuadratnya harus punya diskriminan nol, sehingga $b = 6$ atau $b = -6$."

Dina melewatkan satu nilai $b$ lagi yang juga membuat $P$ memiliki tepat dua pembuat nol real yang berbeda. Nilai $b$ itu adalah ....

- A. $0$  
  <sub>Salah: faktor kuadrat $x^2+9$ tidak punya pembuat nol real, sehingga $P$ hanya punya satu pembuat nol</sub>
- **B. $-\frac{13}{2}$** ✅  
  <sub>Benar: dua pembuat nol berbeda juga terjadi bila $x=2$ adalah pembuat nol faktor kuadrat: $4+2b+9=0$ sehingga $b=-\frac{13}{2}$, dengan pembuat nol $2$ dan $\frac92$ (dua nilai)</sub>
- C. $\frac{13}{2}$  
  <sub>Salah: salah tanda: $4+2b+9=0$ memberi $b=-\frac{13}{2}$; untuk $b=\frac{13}{2}$ ada tiga pembuat nol berbeda ($2$, $-2$, $-\frac92$)</sub>
- D. $-\frac92$  
  <sub>Salah: mengambil pembuat nol lain $\frac92$ lalu menjadikannya $b$; $x^2-\frac92x+9$ berdiskriminan negatif sehingga $P$ hanya punya satu pembuat nol</sub>

**Pembahasan:** Ada dua cara memperoleh tepat dua pembuat nol real berbeda: (1) $x^2+bx+9$ punya pembuat nol kembar ($b^2=36$, $b=\pm6$, pembuat nol $\mp3\neq 2$), atau (2) salah satu pembuat nol $x^2+bx+9$ sama dengan $2$ (kasus yang terlewat): $4+2b+9=0$, $b=-\frac{13}{2}$, faktor kuadrat $(x-2)(x-\frac92)$, pembuat nol $P$ hanya $2$ dan $\frac92$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b02-d-hard-bt01-005
*orisinal | C5 | 6 langkah | jenis: evaluasi empat pernyataan tentang banyak pembuat nol*

Diberikan $P(x) = x^4 + ax^2 - 4a - 16$ dengan $a$ bilangan real. Pernyataan yang benar adalah ....

- **A. Untuk $a = -4$, $P$ memiliki tepat tiga pembuat nol real yang berbeda** ✅  
  <sub>Benar: $P(x)=(x^2-4)(x^2+a+4)$; untuk $a=-4$ menjadi $(x^2-4)x^2$ dengan pembuat nol $-2,0,2$</sub>
- B. Untuk setiap bilangan real $a$, $P$ memiliki paling sedikit tiga pembuat nol real yang berbeda  
  <sub>Salah: untuk $a=0$ atau $a=-3$ hanya ada dua pembuat nol real berbeda</sub>
- C. Untuk $a = 0$, $P$ memiliki tepat empat pembuat nol real yang berbeda  
  <sub>Salah: untuk $a=0$ faktor kedua $x^2+4$ tidak punya pembuat nol real, hanya $\pm2$</sub>
- D. Untuk $a = -8$, $P$ memiliki tepat empat pembuat nol real yang berbeda  
  <sub>Salah: untuk $a=-8$ faktor kedua $x^2-4$ sama dengan faktor pertama sehingga hanya ada dua pembuat nol berbeda ($\pm2$)</sub>

**Pembahasan:** Faktorkan $P(x)=(x^2-4)(x^2+a+4)$. Pembuat nol $\pm2$ selalu ada. Faktor $x^2+a+4$: $a>-4$ tanpa pembuat nol real (total 2); $a=-4$ nol ganda di $0$ (total 3); $a<-4$ memberi $\pm\sqrt{-a-4}$ (total 4, kecuali $a=-8$ yang jatuh pada $\pm2$ sehingga total 2).
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b02-d-hard-bt01-006
*orisinal | C6 | 6 langkah | jenis: merancang polinomial berkoefisien bulat*

Polinomial berderajat tiga $P(x)$ memiliki pembuat nol $\frac34$, $-\frac23$, dan $\frac52$. Semua koefisien dan konstanta $P(x)$ harus bilangan bulat. Koefisien $x^3$ positif terkecil yang mungkin adalah ....

- A. $1$  
  <sub>Salah: mengira polinomial monik; koefisien $x^2$ menjadi $-\frac{31}{12}$, bukan bulat</sub>
- B. $12$  
  <sub>Salah: memakai KPK penyebut $4,3,2$; padahal koefisien $x$ menjadi $-\frac{7}{2}$, bukan bilangan bulat</sub>
- **C. $24$** ✅  
  <sub>Benar: $P(x)=k(x-\frac34)(x+\frac23)(x-\frac52)$; koefisien $x^2$ adalah $-\frac{31}{12}k$ dan koefisien $x$ adalah $-\frac{7}{24}k$, sehingga $k$ harus kelipatan $24$; $k=24$ memberi $(4x-3)(3x+2)(2x-5)$ berkoefisien bulat</sub>
- D. $9$  
  <sub>Salah: menjumlahkan penyebut $4+3+2$ tanpa dasar; koefisien tidak bulat</sub>

**Pembahasan:** Bentuk umum $P(x)=k(x-\frac34)(x+\frac23)(x-\frac52)$. Koefisien $x^2$: $-k(\frac34-\frac23+\frac52)=-\frac{31}{12}k$. Koefisien $x$: $k(-\frac12+\frac{15}{8}-\frac53)=-\frac{7}{24}k$. Karena $31$ dan $7$ tidak berfaktor sama dengan penyebutnya, $k$ harus kelipatan $24$. Terkecil $k=24$, yaitu $(4x-3)(3x+2)(2x-5)$ dengan koefisien $x^3$ sama dengan $24$.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b02-d-hard-bt01-007
*orisinal | C5 | 6 langkah | jenis: membandingkan dua polinomial*

Diberikan $f(x) = x^3 - 2x^2 - 5x + 6$ dan $g(x) = x^3 - 3x^2 - x + 3$.

Pernyataan yang benar mengenai $f$ dan $g$ adalah ....

- A. $f$ dan $g$ berbagi dua pembuat nol, tetapi titik potong $g$ di sumbu-$y$ lebih tinggi  
  <sub>Salah: $g(0)=3$ lebih rendah daripada $f(0)=6$</sub>
- B. $f$ dan $g$ berbagi tiga pembuat nol, dan titik potong $f$ di sumbu-$y$ lebih tinggi  
  <sub>Salah: pembuat nol $f$ adalah $-2,1,3$ dan $g$ adalah $-1,1,3$; yang sama hanya dua</sub>
- C. $f$ dan $g$ berbagi dua pembuat nol, tetapi $x+1$ faktor $f$ dan $x+2$ faktor $g$  
  <sub>Salah: tertukar: $x+2$ faktor $f$ dan $x+1$ faktor $g$</sub>
- **D. $f$ dan $g$ berbagi tepat dua pembuat nol, dan titik potong $f$ di sumbu-$y$ lebih tinggi** ✅  
  <sub>Benar: $f=(x-1)(x+2)(x-3)$, $g=(x-1)(x+1)(x-3)$: pembuat nol sama $1$ dan $3$; $f(0)=6>3=g(0)$</sub>

**Pembahasan:** Jumlah koefisien $f$ dan $g$ sama dengan nol sehingga $x-1$ faktor keduanya; $f(3)=g(3)=0$. $f=(x-1)(x-3)(x+2)$ dan $g=(x-1)(x-3)(x+1)$. Pembuat nol bersama: $1$ dan $3$. $f(0)=6$ dan $g(0)=3$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b02-d-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: kemungkinan pembuat nol menurut Sifat 2.5*

$P(x) = x^3 + bx^2 + cx + 7$ adalah polinomial dengan $b$ dan $c$ bilangan bulat.

Bilangan yang tidak mungkin menjadi pembuat nol $P(x)$ untuk pilihan bilangan bulat $b$ dan $c$ mana pun adalah ....

- A. $-7$  
  <sub>Salah: pembagi $7$ dan mungkin: $P(x)=(x+7)(x^2+bx+1)$ memenuhi $P(0)=7$</sub>
- B. $7$  
  <sub>Salah: pembagi $7$ dan mungkin: $P(x)=(x-7)(x^2+bx-1)$ memenuhi $P(0)=7$</sub>
- C. $1$  
  <sub>Salah: pembagi $7$ dan mungkin: $P(x)=(x-1)(x^2+bx-7)$ memenuhi $P(0)=7$</sub>
- **D. $\frac72$** ✅  
  <sub>Benar: koefisien $x^3$ adalah $1$ sehingga penyebut $q$ hanya boleh $\pm1$; pembuat nol rasional pasti bilangan bulat pembagi $7$, jadi $\frac72$ mustahil</sub>

**Pembahasan:** Sifat 2.5 dengan $a_n=1$ dan $a_0=7$: pembuat nol rasional $\frac pq$ dengan $p$ pembagi $7$ dan $q$ pembagi $1$. Jadi hanya $\pm1,\pm7$ yang mungkin. Bilangan $7,-7,1$ dapat dicapai dengan memilih faktor, sedangkan $\frac72$ tidak termasuk calon.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b02-d-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: temukan kesalahan penerapan Sifat 2.5*

Untuk $P(x) = 3x^3 - 2x^2 - 11x + 10$, Kania menyusun daftar calon pembuat nol rasional dengan mengambil pembilang dari faktor koefisien $x^3$ (yaitu $\pm1, \pm3$) dan penyebut dari faktor konstanta (yaitu $1, 2, 5, 10$). Ia lalu hanya menguji bilangan pada daftarnya.

Pernyataan yang tepat mengenai daftar Kania adalah ....

- **A. Peran pembilang dan penyebut tertukar; akibatnya pembuat nol $-2$ dan $\frac53$ dari $P$ tidak ada pada daftarnya** ✅  
  <sub>Benar: Sifat 2.5: pembilang $p$ faktor konstanta ($10$) dan penyebut $q$ faktor koefisien utama ($3$); $P=(x-1)(x+2)(3x-5)$ sehingga $-2$ dan $\frac53$ tidak masuk daftar Kania, hanya $1$ yang masuk</sub>
- B. Peran pembilang dan penyebut tertukar; akibatnya pembuat nol $1$ dari $P$ tidak ada pada daftarnya  
  <sub>Salah: $1=\frac11$ ada pada daftar Kania; yang tidak ada adalah $-2$ dan $\frac53$</sub>
- C. Kania seharusnya memakai koefisien $x^3$ dan koefisien $x$, bukan konstanta  
  <sub>Salah: Sifat 2.5 memakai koefisien utama dan konstanta, bukan koefisien $x$</sub>
- D. Daftar Kania sudah benar sehingga memuat semua pembuat nol rasional $P$  
  <sub>Salah: daftar tertukar dan tidak memuat $-2$ maupun $\frac53$</sub>

**Pembahasan:** Sifat 2.5: $p$ faktor $a_0=10$ dan $q$ faktor $a_n=3$. Kania melakukan kebalikannya. Faktorisasi $P=(x-1)(x+2)(3x-5)$ dengan pembuat nol $1,-2,\frac53$. Pada daftar Kania ada $1$, tetapi $-2$ ($p=2$ bukan faktor $3$) dan $\frac53$ ($p=5$ bukan faktor $3$) tidak ada.
**Acuan:** siswa — siswa hal.98

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b02-d-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan membagi dengan faktor*

Ali menyelesaikan $x^3 - 3x^2 - 4x + 12 = 0$. Pekerjaannya: "$x^2(x - 3) - 4(x - 3) = 0$, sehingga $(x - 3)(x^2 - 4) = 0$. Bagi kedua ruas dengan $x - 3$, diperoleh $x^2 = 4$, jadi $x = 2$ atau $x = -2$."

Pernyataan yang tepat mengenai pekerjaan Ali adalah ....

- A. Pembagian dengan $x - 3$ tidak sah; himpunan penyelesaian sebenarnya $\{-3, -2, 2\}$  
  <sub>Salah: diagnosis benar tetapi salah tanda: faktor $x-3$ memberi $x=3$, bukan $-3$</sub>
- B. Pembagian dengan $x - 3$ sah; himpunan penyelesaiannya $\{-2, 2\}$  
  <sub>Salah: pembagian dengan faktor yang bisa nol menghilangkan penyelesaian $x=3$</sub>
- **C. Pembagian dengan $x - 3$ tidak sah karena $x - 3$ dapat bernilai nol; himpunan penyelesaian sebenarnya adalah $\{-2, 2, 3\}$** ✅  
  <sub>Benar: $(x-3)(x-2)(x+2)=0$ menurut sifat hasil kali nol memberi $x=3$, $x=2$, atau $x=-2$; membagi dengan $x-3$ menghilangkan penyelesaian $x=3$</sub>
- D. Pembagian dengan $x - 3$ tidak sah; himpunan penyelesaian sebenarnya $\{2, 3\}$  
  <sub>Salah: diagnosis benar tetapi penyelesaian $x=-2$ dari $x^2=4$ ikut terbuang</sub>

**Pembahasan:** Pengelompokan benar: $(x-3)(x^2-4)=(x-3)(x-2)(x+2)=0$. Sifat hasil kali nol: $x-3=0$ atau $x-2=0$ atau $x+2=0$. Membagi kedua ruas dengan $x-3$ mengabaikan kemungkinan $x-3=0$, sehingga $x=3$ hilang. Himpunan penyelesaian $\{-2,2,3\}$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b02-d-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan sifat hasil kali nol*

Bima menyelesaikan $(x - 2)(x + 3) = 14$. Pekerjaannya: "Berdasarkan sifat hasil kali nol, $x - 2 = 14$ atau $x + 3 = 14$, sehingga $x = 16$ atau $x = 11$."

Pernyataan yang tepat mengenai pekerjaan Bima adalah ....

- A. Penerapan sifat hasil kali nol sudah benar; hanya perhitungan akhirnya yang perlu diperiksa, penyelesaiannya $x = 16$ atau $x = 11$  
  <sub>Salah: sifat hasil kali nol tidak berlaku untuk hasil kali $14$; $x=16$ memberi $14\cdot19=266$</sub>
- **B. Sifat hasil kali nol hanya berlaku bila hasil kalinya nol; penyelesaian yang benar adalah $x = 4$ atau $x = -5$** ✅  
  <sub>Benar: ubah menjadi $x^2+x-20=0$, $(x-4)(x+5)=0$ sehingga $x=4$ atau $x=-5$; substitusi $x=16$ memberi $14\cdot19\neq14$</sub>
- C. Sifat hasil kali nol hanya berlaku bila hasil kalinya nol; penyelesaian yang benar adalah $x = 2$ atau $x = -3$  
  <sub>Salah: mengambil pembuat nol faktor-faktor semula, padahal ruas kanan $14$ bukan nol; $x=2$ memberi $0\neq14$</sub>
- D. Sifat hasil kali nol hanya berlaku bila hasil kalinya nol; penyelesaian yang benar adalah $x = -4$ atau $x = 5$  
  <sub>Salah: diagnosis benar tetapi tanda pembuat nol terbalik; $x=5$ memberi $3\cdot8=24\neq14$</sub>

**Pembahasan:** Sifat hasil kali nol: $A\cdot B=0$ jika dan hanya jika $A=0$ atau $B=0$; tidak berlaku untuk hasil kali $14$. Jabarkan: $x^2+x-6=14$, $x^2+x-20=0$, $(x-4)(x+5)=0$. Jadi $x=4$ atau $x=-5$. Cek $x=4$: $2\cdot7=14$; $x=-5$: $(-7)(-2)=14$.
**Acuan:** siswa — siswa hal.100

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
