# Lembar koreksi — kelas11_tl SMA11L-B5 subbab B: Kaitan Matriks dengan Transformasi

54 soal | easy 20, medium 20, hard 14 | variasi 21, orisinal 33
> **Kapasitas kurang (hard): 14 dari kuota 20** — Subbab B hanya memuat matriks transformasi tunggal (pencerminan, translasi, rotasi, dilatasi); komposisi transformasi ada di subbab C. Penalaran tingkat hard yang layak tanpa soal kembar hanya cukup untuk 14 soal.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b05-b-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: peta titik oleh matriks*

Peta dari titik $(6, -4)$ yang ditransformasikan dengan matriks $\begin{pmatrix} 2 & 5 \\ 4 & 3 \end{pmatrix}$ adalah ....

- A. $(32, 36)$  
  <sub>Salah: salah tanda pada perkalian dengan komponen negatif</sub>
- **B. $(-8, 12)$** ✅  
  <sub>Benar: $\begin{pmatrix} 2 & 5 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 6 \\ -4 \end{pmatrix}=\begin{pmatrix} 2\cdot 6+5\cdot(-4) \\ 4\cdot 6+3\cdot(-4) \end{pmatrix}=\begin{pmatrix} -8 \\ 12 \end{pmatrix}$</sub>
- C. $(-4, 18)$  
  <sub>Salah: memakai transpos matriks (baris dan kolom tertukar)</sub>
- D. $(12, -8)$  
  <sub>Salah: menukar absis dan ordinat hasil</sub>

**Pembahasan:** Kalikan matriks dengan vektor posisi: baris pertama $2\cdot 6+5\cdot(-4)=-8$, baris kedua $4\cdot 6+3\cdot(-4)=12$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b05-b-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: peta titik oleh matriks*

Titik $(8, 9)$ ditransformasikan oleh matriks $\begin{pmatrix} 7 & -2 \\ 5 & 6 \end{pmatrix}$. Koordinat petanya adalah ....

- **A. $(38, 94)$** ✅  
  <sub>Benar: baris pertama $7\cdot 8-2\cdot 9=38$, baris kedua $5\cdot 8+6\cdot 9=94$</sub>
- B. $(94, 38)$  
  <sub>Salah: menukar absis dan ordinat hasil</sub>
- C. $(74, -14)$  
  <sub>Salah: salah tanda pada elemen negatif matriks</sub>
- D. $(101, 38)$  
  <sub>Salah: memakai transpos matriks</sub>

**Pembahasan:** $\begin{pmatrix} 7 & -2 \\ 5 & 6 \end{pmatrix}\begin{pmatrix} 8 \\ 9 \end{pmatrix}=\begin{pmatrix} 38 \\ 94 \end{pmatrix}$, jadi petanya $(38, 94)$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b05-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: peta garis oleh matriks dilatasi*

Garis $7x + 2y - 12 = 0$ ditransformasikan oleh matriks $\begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix}$. Persamaan petanya adalah ....

- A. $7x + 2y - 432 = 0$  
  <sub>Salah: mengalikan konstanta dengan $6^2$ setelah menyederhanakan</sub>
- B. $42x + 12y - 12 = 0$  
  <sub>Salah: hanya mengalikan koefisien $x$ dan $y$ dengan 6</sub>
- **C. $7x + 2y - 72 = 0$** ✅  
  <sub>Benar: $(x', y')=(6x, 6y)$ sehingga $x=x'/6$, $y=y'/6$; substitusi dan kali 6 menghasilkan $7x'+2y'-72=0$</sub>
- D. $7x + 2y - 2 = 0$  
  <sub>Salah: mengalikan dengan $\frac{1}{6}$, bukan 6, pada konstanta</sub>

**Pembahasan:** Dengan $x=x'/6$ dan $y=y'/6$: $\frac{7x'}{6}+\frac{2y'}{6}-12=0$, kalikan 6 diperoleh $7x'+2y'-72=0$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b05-b-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: peta garis oleh matriks dilatasi*

Persamaan peta dari garis $5x + 4y - 7 = 0$ oleh transformasi dengan matriks $\begin{pmatrix} 8 & 0 \\ 0 & 8 \end{pmatrix}$ adalah ....

- A. $5x + 4y - 448 = 0$  
  <sub>Salah: mengalikan konstanta dengan $8^2$</sub>
- B. $5x + 4y - 1 = 0$  
  <sub>Salah: membagi konstanta dengan 8 dan membulatkan</sub>
- **C. $5x + 4y - 56 = 0$** ✅  
  <sub>Benar: pemetaan $(x,y)\to(8x,8y)$, sehingga konstanta garis dikali 8 menjadi $-56$</sub>
- D. $40x + 32y - 7 = 0$  
  <sub>Salah: hanya mengalikan koefisien $x$ dan $y$ dengan 8</sub>

**Pembahasan:** $x=x'/8$, $y=y'/8$; substitusi: $\frac{5x'}{8}+\frac{4y'}{8}-7=0$, kalikan 8: $5x'+4y'-56=0$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b05-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: peta titik oleh pencerminan*

Peta dari titik $(8, -5)$ yang dicerminkan terhadap sumbu-$y$ adalah ....

- A. $(8, 5)$  
  <sub>Salah: memakai matriks pencerminan terhadap sumbu-$x$</sub>
- B. $(-5, 8)$  
  <sub>Salah: memakai matriks pencerminan terhadap garis $y=x$</sub>
- **C. $(-8, -5)$** ✅  
  <sub>Benar: matriks pencerminan sumbu-$y$ $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ mengubah tanda absis saja</sub>
- D. $(-8, 5)$  
  <sub>Salah: mengubah tanda kedua koordinat</sub>

**Pembahasan:** $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 8 \\ -5 \end{pmatrix}=\begin{pmatrix} -8 \\ -5 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.241 Contoh 5.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b05-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: peta titik oleh pencerminan*

Dengan memakai perkalian matriks, titik $(-6, 9)$ yang dicerminkan terhadap garis $y = -x$ dipetakan ke ....

- **A. $(-9, 6)$** ✅  
  <sub>Benar: matriks pencerminan terhadap $y=-x$ adalah $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$: $(-6,9)\to(-9,6)$</sub>
- B. $(9, -6)$  
  <sub>Salah: memakai matriks pencerminan terhadap garis $y=x$</sub>
- C. $(6, -9)$  
  <sub>Salah: mengubah tanda kedua koordinat tanpa menukar posisinya</sub>
- D. $(-6, -9)$  
  <sub>Salah: memakai matriks pencerminan terhadap sumbu-$x$</sub>

**Pembahasan:** $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} -6 \\ 9 \end{pmatrix}=\begin{pmatrix} -9 \\ 6 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.241 Contoh 5.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b05-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: peta segitiga oleh pencerminan*

Segitiga $ABC$ memiliki titik sudut $A(5, 2)$, $B(-4, 6)$, dan $C(7, -3)$. Peta segitiga tersebut jika dicerminkan terhadap sumbu-$x$ adalah ....

- A. $A'(-5, -2)$, $B'(4, -6)$, $C'(-7, 3)$  
  <sub>Salah: mengubah tanda kedua koordinat</sub>
- **B. $A'(5, -2)$, $B'(-4, -6)$, $C'(7, 3)$** ✅  
  <sub>Benar: sumbu-$x$ hanya mengubah tanda ordinat setiap titik</sub>
- C. $A'(-5, 2)$, $B'(4, 6)$, $C'(-7, -3)$  
  <sub>Salah: mengubah tanda absis (pencerminan terhadap sumbu-$y$)</sub>
- D. $A'(2, 5)$, $B'(6, -4)$, $C'(-3, 7)$  
  <sub>Salah: menukar absis dan ordinat (pencerminan terhadap $y=x$)</sub>

**Pembahasan:** Matriks $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ dikalikan tiap titik: $A'(5,-2)$, $B'(-4,-6)$, $C'(7,3)$.
**Acuan:** siswa — siswa hal.241 Contoh 5.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b05-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: peta segitiga oleh pencerminan*

Titik-titik sudut sebuah segitiga adalah $P(4, -5)$, $Q(9, 2)$, dan $R(-7, 8)$. Segitiga itu dicerminkan terhadap garis $y = x$. Titik-titik peta segitiga tersebut adalah ....

- A. $P'(5, -4)$, $Q'(-2, -9)$, $R'(-8, 7)$  
  <sub>Salah: memakai pencerminan terhadap $y=-x$ (tanda ikut berubah)</sub>
- **B. $P'(-5, 4)$, $Q'(2, 9)$, $R'(8, -7)$** ✅  
  <sub>Benar: pencerminan terhadap $y=x$ menukar absis dan ordinat</sub>
- C. $P'(-4, 5)$, $Q'(-9, -2)$, $R'(7, -8)$  
  <sub>Salah: mengubah tanda kedua koordinat</sub>
- D. $P'(4, 5)$, $Q'(9, -2)$, $R'(-7, -8)$  
  <sub>Salah: memakai pencerminan terhadap sumbu-$x$</sub>

**Pembahasan:** $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ menukar koordinat: $P'(-5,4)$, $Q'(2,9)$, $R'(8,-7)$.
**Acuan:** siswa — siswa hal.241 Contoh 5.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b05-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: peta oleh dilatasi berpusat sembarang*

Peta dari titik $(8, -4)$ oleh dilatasi dengan titik pusat $(-3, 6)$ dan faktor skala $3$ adalah ....

- A. $(12, 12)$  
  <sub>Salah: salah tanda saat mengurangi koordinat pusat</sub>
- B. $(24, -12)$  
  <sub>Salah: memakai pusat $O(0,0)$, bukan pusat yang diberikan</sub>
- C. $(33, -30)$  
  <sub>Salah: lupa menambah koordinat pusat kembali</sub>
- **D. $(30, -24)$** ✅  
  <sub>Benar: $x'=3(8+3)-3=30$, $y'=3(-4-6)+6=-24$</sub>

**Pembahasan:** Gunakan $x'=k(x-a)+a$ dan $y'=k(y-b)+b$ dengan $k=3$, $(a,b)=(-3,6)$: $(30,-24)$.
**Acuan:** siswa — siswa hal.246 Contoh 5.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b05-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: peta oleh dilatasi berpusat sembarang*

Sebuah titik $(6, 10)$ didilatasikan dengan pusat $(7, -2)$ dan faktor skala $5$. Koordinat petanya adalah ....

- **A. $(2, 58)$** ✅  
  <sub>Benar: $x'=5(6-7)+7=2$, $y'=5(10+2)-2=58$</sub>
- B. $(30, 50)$  
  <sub>Salah: memakai pusat $O(0,0)$</sub>
- C. $(-5, 60)$  
  <sub>Salah: lupa menambah koordinat pusat kembali</sub>
- D. $(72, 38)$  
  <sub>Salah: salah tanda saat mengurangi koordinat pusat</sub>

**Pembahasan:** $(x',y')=(5(6-7)+7,\ 5(10-(-2))+(-2))=(2, 58)$.
**Acuan:** siswa — siswa hal.246 Contoh 5.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b05-b-easy-bt01-011
*variasi (konteks) | C1 | 1 langkah | jenis: menuliskan matriks pencerminan*

Matriks 2 x 2 yang berkaitan dengan pencerminan terhadap sumbu-$y$ adalah ....

- A. $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$  
  <sub>Salah: matriks pencerminan terhadap garis $y=x$</sub>
- B. $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$  
  <sub>Salah: matriks pencerminan terhadap sumbu-$x$</sub>
- **C. $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$** ✅  
  <sub>Benar: titik $(x,y)$ dipetakan ke $(-x,y)$, sehingga matriksnya $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$</sub>
- D. $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$  
  <sub>Salah: matriks yang mengubah tanda kedua koordinat (rotasi $180^\circ$)</sub>

**Pembahasan:** Syarat $\begin{pmatrix} r & s \\ t & u \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} -x \\ y \end{pmatrix}$ memberi $r=-1$, $s=0$, $t=0$, $u=1$.
**Acuan:** siswa — siswa hal.247 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b05-b-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: menuliskan matriks rotasi*

Matriks yang berkaitan dengan rotasi terhadap titik pusat $O$ sebesar $\pi$ (ekuivalen dengan $180^\circ$) adalah ....

- A. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$  
  <sub>Salah: memakai matriks rotasi $90^\circ$</sub>
- **B. $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$** ✅  
  <sub>Benar: $\cos\pi=-1$ dan $\sin\pi=0$ pada matriks rotasi</sub>
- C. $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$  
  <sub>Salah: memakai matriks identitas (rotasi $360^\circ$)</sub>
- D. $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$  
  <sub>Salah: memakai matriks pencerminan terhadap sumbu-$x$</sub>

**Pembahasan:** $\begin{pmatrix} \cos\pi & -\sin\pi \\ \sin\pi & \cos\pi \end{pmatrix}=\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.247 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b05-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: menuliskan matriks dilatasi*

Matriks yang berkaitan dengan dilatasi berpusat di $O(0, 0)$ dengan faktor skala $7$ adalah ....

- A. $\begin{pmatrix} 1 & 0 \\ 0 & 7 \end{pmatrix}$  
  <sub>Salah: hanya meregangkan sumbu-$y$, elemen pertama tetap 1</sub>
- **B. $\begin{pmatrix} 7 & 0 \\ 0 & 7 \end{pmatrix}$** ✅  
  <sub>Benar: matriks dilatasi pusat $O$ faktor $k$ adalah $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ dengan $k=7$</sub>
- C. $\begin{pmatrix} 7 & 7 \\ 0 & 0 \end{pmatrix}$  
  <sub>Salah: mengisi baris pertama dengan $k$ dan baris kedua nol</sub>
- D. $\begin{pmatrix} 0 & 7 \\ 7 & 0 \end{pmatrix}$  
  <sub>Salah: meletakkan $k$ pada diagonal samping</sub>

**Pembahasan:** Sifat 5.9: matriks dilatasi $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$, jadi $k=7$.
**Acuan:** siswa — siswa hal.246

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b05-b-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: menuliskan matriks rotasi*

Matriks yang berkaitan dengan rotasi terhadap titik pusat $O$ sebesar $-90^\circ$ (ekuivalen dengan $-\frac{\pi}{2}$) adalah ....

- **A. $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$** ✅  
  <sub>Benar: $\cos(-90^\circ)=0$ dan $\sin(-90^\circ)=-1$, sehingga matriks rotasinya $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$</sub>
- B. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$  
  <sub>Salah: memakai matriks rotasi $+90^\circ$ (arah putar terbalik)</sub>
- C. $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$  
  <sub>Salah: memakai matriks rotasi $180^\circ$</sub>
- D. $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$  
  <sub>Salah: memakai matriks pencerminan terhadap garis $y=-x$</sub>

**Pembahasan:** $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ dengan $\theta=-90^\circ$ menghasilkan $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b05-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: mengenali transformasi dari aturan*

Suatu transformasi memetakan setiap titik $(x, y)$ ke titik $(y, x)$. Matriks yang mewakili transformasi tersebut adalah ....

- A. $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$  
  <sub>Salah: memakai matriks identitas</sub>
- B. $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$  
  <sub>Salah: memakai matriks rotasi $90^\circ$</sub>
- C. $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$  
  <sub>Salah: memakai pencerminan terhadap $y=-x$ (tanda ikut berubah)</sub>
- **D. $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$** ✅  
  <sub>Benar: $\begin{pmatrix} r & s \\ t & u \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} y \\ x \end{pmatrix}$ memberi $r=0$, $s=1$, $t=1$, $u=0$</sub>

**Pembahasan:** Baris pertama menghasilkan $y$ sehingga $(r,s)=(0,1)$; baris kedua menghasilkan $x$ sehingga $(t,u)=(1,0)$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b05-b-easy-bt01-016
*orisinal | C2 | 1 langkah | jenis: mengenali transformasi dari matriks*

Matriks $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ jika dikalikan dengan vektor posisi suatu titik akan memetakan titik tersebut melalui transformasi ....

- A. rotasi $90^\circ$ terhadap titik asal  
  <sub>Salah: mengira matriks dengan elemen $\pm 1$ selalu rotasi</sub>
- B. pencerminan terhadap sumbu-$y$  
  <sub>Salah: mengira diagonal samping tidak berpengaruh</sub>
- **C. pencerminan terhadap garis $y = -x$** ✅  
  <sub>Benar: $(x,y)\to(-y,-x)$ adalah pencerminan terhadap garis $y=-x$</sub>
- D. pencerminan terhadap garis $y = x$  
  <sub>Salah: mengira tanda negatif tidak mengubah garis cermin</sub>

**Pembahasan:** $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} -y \\ -x \end{pmatrix}$, yaitu pencerminan terhadap $y=-x$.
**Acuan:** siswa — siswa hal.238

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b05-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: translasi dengan operasi matriks*

Titik $(6, -2)$ ditranslasikan oleh vektor $\begin{pmatrix} -4 \\ 9 \end{pmatrix}$ dengan operasi matriks. Peta titik tersebut adalah ....

- **A. $(2, 7)$** ✅  
  <sub>Benar: $\begin{pmatrix} 6 \\ -2 \end{pmatrix}+\begin{pmatrix} -4 \\ 9 \end{pmatrix}=\begin{pmatrix} 2 \\ 7 \end{pmatrix}$</sub>
- B. $(10, -11)$  
  <sub>Salah: mengurangkan vektor translasi, bukan menjumlahkan</sub>
- C. $(-24, -18)$  
  <sub>Salah: mengalikan komponen yang bersesuaian</sub>
- D. $(7, 2)$  
  <sub>Salah: menukar absis dan ordinat hasil</sub>

**Pembahasan:** Translasi menjumlahkan vektor posisi dengan vektor translasi: $(6-4,\,-2+9)=(2,7)$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b05-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: prapeta dari matriks dilatasi*

Dilatasi berpusat di $O$ dengan faktor skala $3$ memetakan titik $P$ ke $P'(12, -21)$. Koordinat titik $P$ adalah ....

- A. $(-4, 7)$  
  <sub>Salah: mengubah tanda kedua koordinat setelah membagi</sub>
- B. $(36, -63)$  
  <sub>Salah: mengalikan peta dengan 3, bukan membagi</sub>
- C. $(-7, 4)$  
  <sub>Salah: menukar posisi koordinat dan tandanya</sub>
- **D. $(4, -7)$** ✅  
  <sub>Benar: $(3x, 3y)=(12,-21)$ sehingga $x=4$ dan $y=-7$</sub>

**Pembahasan:** Karena $P'=3P$, maka $P=\frac{1}{3}(12,-21)=(4,-7)$.
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b05-b-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: notasi vektor posisi*

Titik $(x, y)$ pada bidang Kartesius yang ditulis sebagai vektor posisi dinyatakan dengan matriks ....

- A. $\begin{pmatrix} x \\ -y \end{pmatrix}$  
  <sub>Salah: mencampur dengan peta pencerminan terhadap sumbu-$x$</sub>
- B. $\begin{pmatrix} y \\ x \end{pmatrix}$  
  <sub>Salah: menukar urutan absis dan ordinat</sub>
- C. $\begin{pmatrix} x & y \end{pmatrix}$  
  <sub>Salah: menuliskan sebagai matriks baris</sub>
- **D. $\begin{pmatrix} x \\ y \end{pmatrix}$** ✅  
  <sub>Benar: vektor posisi berbentuk matriks kolom dengan absis di atas dan ordinat di bawah</sub>

**Pembahasan:** Vektor posisi titik $(x,y)$ adalah matriks kolom $\begin{pmatrix} x \\ y \end{pmatrix}$.
**Acuan:** siswa — siswa hal.238

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b05-b-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: peta titik oleh rotasi*

Titik $(5, 3)$ dirotasikan sebesar $90^\circ$ terhadap titik asal berlawanan arah jarum jam. Peta titik tersebut adalah ....

- A. $(-5, -3)$  
  <sub>Salah: memakai rotasi $180^\circ$</sub>
- B. $(3, 5)$  
  <sub>Salah: menukar koordinat tanpa tanda (pencerminan $y=x$)</sub>
- C. $(3, -5)$  
  <sub>Salah: memutar searah jarum jam ($-90^\circ$)</sub>
- **D. $(-3, 5)$** ✅  
  <sub>Benar: $x'=5\cos 90^\circ-3\sin 90^\circ=-3$ dan $y'=5\sin 90^\circ+3\cos 90^\circ=5$</sub>

**Pembahasan:** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 5 \\ 3 \end{pmatrix}=\begin{pmatrix} -3 \\ 5 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b05-b-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: peta titik oleh matriks*

Titik $(5, -6)$ yang ditransformasikan dengan matriks $\begin{pmatrix} -3 & 4 \\ 2 & -7 \end{pmatrix}$ memiliki peta ....

- A. $(-27, 62)$  
  <sub>Salah: memakai transpos matriks (baris dan kolom tertukar)</sub>
- B. $(9, -32)$  
  <sub>Salah: salah tanda pada perkalian elemen matriks dengan komponen negatif</sub>
- C. $(52, -39)$  
  <sub>Salah: menukar absis dan ordinat hasil</sub>
- **D. $(-39, 52)$** ✅  
  <sub>Benar: $\begin{pmatrix} -3 & 4 \\ 2 & -7 \end{pmatrix}\begin{pmatrix} 5 \\ -6 \end{pmatrix}=\begin{pmatrix} -39 \\ 52 \end{pmatrix}$</sub>

**Pembahasan:** Baris pertama $-3\cdot 5+4\cdot(-6)=-39$, baris kedua $2\cdot 5+(-7)(-6)=52$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b05-b-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: peta titik oleh matriks*

Titik $(6, -9)$ ditransformasikan dengan matriks $\begin{pmatrix} \frac{1}{2} & -3 \\ 4 & \frac{1}{3} \end{pmatrix}$. Peta titik tersebut adalah ....

- A. $(21, 30)$  
  <sub>Salah: menukar absis dan ordinat hasil</sub>
- B. $(-24, 27)$  
  <sub>Salah: salah tanda pada komponen negatif (absis $3-27$ dan ordinat $24+3$)</sub>
- **C. $(30, 21)$** ✅  
  <sub>Benar: $\frac{1}{2}\cdot 6+(-3)(-9)=30$ dan $4\cdot 6+\frac{1}{3}(-9)=21$</sub>
- D. $(-33, -21)$  
  <sub>Salah: memakai transpos matriks</sub>

**Pembahasan:** $\begin{pmatrix} \frac{1}{2} & -3 \\ 4 & \frac{1}{3} \end{pmatrix}\begin{pmatrix} 6 \\ -9 \end{pmatrix}=\begin{pmatrix} 30 \\ 21 \end{pmatrix}$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b05-b-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: peta garis oleh matriks dilatasi*

Garis $6x - 5y + 8 = 0$ yang ditransformasikan oleh $\begin{pmatrix} -4 & 0 \\ 0 & -4 \end{pmatrix}$ memiliki persamaan peta ....

- A. $24x - 20y + 8 = 0$  
  <sub>Salah: hanya mengalikan koefisien $x$, $y$, dan konstanta dengan 4</sub>
- B. $6x - 5y - 2 = 0$  
  <sub>Salah: membagi konstanta dengan $-4$, bukan mengalikan</sub>
- C. $6x - 5y + 32 = 0$  
  <sub>Salah: memakai faktor 4 (tanda negatif hilang), konstanta menjadi $+32$</sub>
- **D. $6x - 5y - 32 = 0$** ✅  
  <sub>Benar: $(x',y')=(-4x,-4y)$ sehingga $x=-\frac{x'}{4}$, $y=-\frac{y'}{4}$; substitusi dan kali $-4$ memberi $6x'-5y'-32=0$</sub>

**Pembahasan:** Dari $x=-\frac{x'}{4}$ dan $y=-\frac{y'}{4}$: $-\frac{6x'}{4}+\frac{5y'}{4}+8=0$. Kalikan $-4$: $6x'-5y'-32=0$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b05-b-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: peta garis oleh matriks rotasi*

Garis $5x + 2y - 10 = 0$ yang ditransformasikan oleh $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ memiliki persamaan peta ....

- A. $2x + 5y - 10 = 0$  
  <sub>Salah: hanya menukar koefisien $x$ dan $y$ tanpa menyesuaikan tanda</sub>
- **B. $2x - 5y + 10 = 0$** ✅  
  <sub>Benar: $(x',y')=(-y,x)$ sehingga $x=y'$ dan $y=-x'$; substitusi: $5y'-2x'-10=0$ atau $2x'-5y'+10=0$</sub>
- C. $5x - 2y + 10 = 0$  
  <sub>Salah: menukar koefisien lalu salah tanda pada koefisien $y$</sub>
- D. $2x - 5y - 10 = 0$  
  <sub>Salah: mensubstitusi $(x,y)=(-y',x')$ (memakai matriks, bukan inversnya)</sub>

**Pembahasan:** Titik peta $(x',y')=(-y,x)$, jadi $x=y'$ dan $y=-x'$. Substitusi ke $5x+2y-10=0$ menghasilkan $5y'-2x'-10=0$, yaitu $2x-5y+10=0$.
**Acuan:** pretest — kelas11_tl-b05-p0247-latihan-b-5d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b05-b-medium-bt01-005
*variasi (konteks) | C3 | 2 langkah | jenis: peta titik oleh pencerminan (cerita)*

Sebuah drone terbang pada posisi $(-9, 14)$ di bidang Kartesius. Dengan perkalian matriks, posisi bayangan drone tersebut jika dicerminkan terhadap sumbu-$x$ adalah ....

- A. $(14, -9)$  
  <sub>Salah: memakai matriks pencerminan terhadap garis $y=x$</sub>
- **B. $(-9, -14)$** ✅  
  <sub>Benar: matriks pencerminan sumbu-$x$ $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ mengubah tanda ordinat saja</sub>
- C. $(9, 14)$  
  <sub>Salah: memakai matriks pencerminan terhadap sumbu-$y$</sub>
- D. $(9, -14)$  
  <sub>Salah: mengubah tanda kedua koordinat</sub>

**Pembahasan:** $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} -9 \\ 14 \end{pmatrix}=\begin{pmatrix} -9 \\ -14 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.241 Contoh 5.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b05-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: peta segitiga oleh pencerminan*

Tentukan peta dari segitiga $ABC$ dengan titik $A(6, -2)$, titik $B(-5, 4)$, dan titik $C(8, 7)$ yang dicerminkan terhadap garis $y = -x$ dengan perkalian matriks. Titik-titik petanya adalah ....

- A. $A'(-2, 6)$, $B'(4, -5)$, $C'(7, 8)$  
  <sub>Salah: memakai pencerminan terhadap garis $y=x$ (hanya menukar koordinat)</sub>
- B. $A'(6, 2)$, $B'(-5, -4)$, $C'(8, -7)$  
  <sub>Salah: memakai pencerminan terhadap sumbu-$x$</sub>
- **C. $A'(2, -6)$, $B'(-4, 5)$, $C'(-7, -8)$** ✅  
  <sub>Benar: matriks pencerminan $y=-x$ adalah $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ dan memetakan $(x,y)\to(-y,-x)$</sub>
- D. $A'(-6, 2)$, $B'(5, -4)$, $C'(-8, -7)$  
  <sub>Salah: mengubah tanda kedua koordinat tanpa menukar posisinya</sub>

**Pembahasan:** $(x,y)\to(-y,-x)$: $A'(2,-6)$, $B'(-4,5)$, $C'(-7,-8)$.
**Acuan:** siswa — siswa hal.241 Contoh 5.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b05-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: peta oleh dilatasi berpusat sembarang*

Tentukan peta dari titik $(9, -3)$ yang ditransformasikan oleh dilatasi dengan titik pusat $(5, -6)$ dan faktor skala $-4$.

- **A. $(-11, -18)$** ✅  
  <sub>Benar: $x'=-4(9-5)+5=-11$, $y'=-4(-3+6)-6=-18$</sub>
- B. $(-16, -12)$  
  <sub>Salah: lupa menambah koordinat pusat kembali</sub>
- C. $(-51, 30)$  
  <sub>Salah: salah tanda saat mengurangi koordinat pusat</sub>
- D. $(-36, 12)$  
  <sub>Salah: memakai pusat $O(0,0)$, bukan pusat yang diberikan</sub>

**Pembahasan:** Gunakan $x'=k(x-a)+a$, $y'=k(y-b)+b$ dengan $k=-4$, $(a,b)=(5,-6)$: peta $(-11,-18)$.
**Acuan:** siswa — siswa hal.246 Contoh 5.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b05-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: peta oleh dilatasi berpusat sembarang*

Tentukan peta dari titik $(10, -7)$ yang ditransformasikan oleh dilatasi dengan titik pusat $(-2, 5)$ dan faktor skala $\frac{1}{3}$.

- A. $(34, -31)$  
  <sub>Salah: memakai faktor skala 3, bukan $\frac{1}{3}$</sub>
- B. $(4, -4)$  
  <sub>Salah: lupa menambah koordinat pusat kembali</sub>
- C. $(\frac{10}{3}, - \frac{7}{3})$  
  <sub>Salah: memakai pusat $O(0,0)$, bukan pusat yang diberikan</sub>
- **D. $(2, 1)$** ✅  
  <sub>Benar: $x'=\frac{1}{3}(10+2)-2=2$, $y'=\frac{1}{3}(-7-5)+5=1$</sub>

**Pembahasan:** $x'=k(x-a)+a$ dan $y'=k(y-b)+b$ dengan $k=\frac{1}{3}$, $(a,b)=(-2,5)$ menghasilkan $(2,1)$.
**Acuan:** siswa — siswa hal.246 Contoh 5.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b05-b-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: menuliskan matriks rotasi sudut istimewa*

Tuliskanlah matriks yang berkaitan dengan rotasi terhadap titik pusat $O$ sebesar $-\frac{1}{3}\pi$ (ekuivalen dengan $-60^\circ$). Matriksnya adalah ....

- A. $\begin{pmatrix} \frac{1}{2} & - \frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$  
  <sub>Salah: memakai rotasi $+60^\circ$ (arah putar terbalik)</sub>
- B. $\begin{pmatrix} \frac{\sqrt{3}}{2} & - \frac{1}{2} \\ \frac{1}{2} & \frac{\sqrt{3}}{2} \end{pmatrix}$  
  <sub>Salah: memakai rotasi $+30^\circ$</sub>
- **C. $\begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$** ✅  
  <sub>Benar: $\cos(-60^\circ)=\frac{1}{2}$ dan $\sin(-60^\circ)=-\frac{\sqrt{3}}{2}$ pada matriks rotasi $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$</sub>
- D. $\begin{pmatrix} \frac{\sqrt{3}}{2} & \frac{1}{2} \\ - \frac{1}{2} & \frac{\sqrt{3}}{2} \end{pmatrix}$  
  <sub>Salah: memakai sudut $-30^\circ$ (nilai sinus dan kosinus tertukar)</sub>

**Pembahasan:** $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ dengan $\theta=-60^\circ$ menghasilkan $\begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$.
**Acuan:** siswa — siswa hal.247 Latihan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b05-b-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: menentukan matriks dari aturan pemetaan*

Suatu transformasi memetakan setiap titik $(x, y)$ ke titik $(4x - 3y,\ -x + 2y)$. Matriks yang berkaitan dengan transformasi tersebut adalah ....

- **A. $\begin{pmatrix} 4 & -3 \\ -1 & 2 \end{pmatrix}$** ✅  
  <sub>Benar: $\begin{pmatrix} r & s \\ t & u \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} 4x-3y \\ -x+2y \end{pmatrix}$ memberi $r=4$, $s=-3$, $t=-1$, $u=2$</sub>
- B. $\begin{pmatrix} 4 & -1 \\ -3 & 2 \end{pmatrix}$  
  <sub>Salah: menuliskan koefisien per kolom (matriks transpos)</sub>
- C. $\begin{pmatrix} 4 & -3 \\ 2 & -1 \end{pmatrix}$  
  <sub>Salah: menulis koefisien baris kedua dengan urutan $y$ lalu $x$</sub>
- D. $\begin{pmatrix} -3 & 4 \\ 2 & -1 \end{pmatrix}$  
  <sub>Salah: menukar urutan koefisien $x$ dan $y$ pada baris pertama</sub>

**Pembahasan:** Baris pertama menggandeng koefisien $x$ dan $y$ pada $4x-3y$, yaitu $(4,-3)$; baris kedua pada $-x+2y$, yaitu $(-1,2)$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b05-b-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: peta titik oleh rotasi sudut istimewa*

Titik $(2\sqrt{3}, 2)$ dirotasikan sebesar $30^\circ$ berlawanan arah jarum jam terhadap titik asal. Peta titik tersebut adalah ....

- A. $(2, 0)$  
  <sub>Salah: salah tanda pada ordinat: memakai $x\sin\theta-y\cos\theta$</sub>
- **B. $(2, 2 \sqrt{3})$** ✅  
  <sub>Benar: $x'=2\sqrt{3}\cdot\frac{\sqrt{3}}{2}-2\cdot\frac{1}{2}=2$ dan $y'=2\sqrt{3}\cdot\frac{1}{2}+2\cdot\frac{\sqrt{3}}{2}=2\sqrt{3}$</sub>
- C. $(0, 4)$  
  <sub>Salah: memakai sudut $60^\circ$ (sinus dan kosinus $30^\circ$ tertukar)</sub>
- D. $(4, 0)$  
  <sub>Salah: memutar searah jarum jam ($-30^\circ$)</sub>

**Pembahasan:** $\begin{pmatrix} \frac{\sqrt{3}}{2} & - \frac{1}{2} \\ \frac{1}{2} & \frac{\sqrt{3}}{2} \end{pmatrix}\begin{pmatrix} 2 \sqrt{3} \\ 2 \end{pmatrix}=\begin{pmatrix} 2 \\ 2 \sqrt{3} \end{pmatrix}$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b05-b-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: prapeta oleh rotasi*

Rotasi sebesar $90^\circ$ berlawanan arah jarum jam terhadap titik asal memetakan titik $P$ ke $P'(-6, 11)$. Koordinat titik $P$ adalah ....

- **A. $(11, 6)$** ✅  
  <sub>Benar: rotasi $90^\circ$ memetakan $(x,y)\to(-y,x)$, sehingga $-y=-6$ dan $x=11$, yaitu $P(11,6)$</sub>
- B. $(6, -11)$  
  <sub>Salah: mengubah tanda kedua koordinat $P'$</sub>
- C. $(-11, -6)$  
  <sub>Salah: memutar $P'$ sebesar $90^\circ$ lagi, bukan memutar balik</sub>
- D. $(11, -6)$  
  <sub>Salah: benar pada absis tetapi salah tanda pada ordinat</sub>

**Pembahasan:** Misalkan $P(x,y)$. Maka $(-y,x)=(-6,11)$, sehingga $y=6$ dan $x=11$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b05-b-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: translasi dari pasangan titik dan peta*

Suatu translasi memetakan titik $(3, -5)$ ke titik $(-1, 4)$. Peta titik $(7, 2)$ oleh translasi yang sama adalah ....

- A. $(11, -7)$  
  <sub>Salah: mengurangkan vektor translasi, bukan menjumlahkan</sub>
- B. $(16, -2)$  
  <sub>Salah: menukar urutan komponen vektor translasi</sub>
- C. $(6, 6)$  
  <sub>Salah: menjumlahkan titik dengan peta, bukan dengan vektor translasi</sub>
- **D. $(3, 11)$** ✅  
  <sub>Benar: vektor translasi $=\begin{pmatrix} -1-3 \\ 4+5 \end{pmatrix}=\begin{pmatrix} -4 \\ 9 \end{pmatrix}$, sehingga $(7-4,\,2+9)=(3,11)$</sub>

**Pembahasan:** Vektor translasi diperoleh dari peta dikurangi titik asal: $(-4,9)$. Peta $(7,2)$ adalah $(7,2)+(-4,9)=(3,11)$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b05-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: dilatasi dari pasangan titik dan peta*

Dilatasi dengan titik pusat $O(0, 0)$ memetakan titik $(4, -6)$ ke titik $(-10, 15)$. Peta titik $(-8, 2)$ oleh dilatasi yang sama adalah ....

- A. $(-20, 5)$  
  <sub>Salah: memakai $k=\frac{5}{2}$ (tanda negatif hilang)</sub>
- B. $(-22, 23)$  
  <sub>Salah: menambahkan selisih peta dan titik pertama (anggap translasi)</sub>
- C. $(\frac{16}{5}, - \frac{4}{5})$  
  <sub>Salah: memakai $k=-\frac{2}{5}$ (kebalikan faktor skala)</sub>
- **D. $(20, -5)$** ✅  
  <sub>Benar: $(4k,-6k)=(-10,15)$ memberi $k=-\frac{5}{2}$, sehingga $\left(-\frac{5}{2}(-8),\,-\frac{5}{2}\cdot 2\right)=(20,-5)$</sub>

**Pembahasan:** Faktor skala $k=\frac{-10}{4}=-\frac{5}{2}$. Peta $(-8,2)$ adalah $(20,-5)$.
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b05-b-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: parameter elemen matriks*

Matriks $\begin{pmatrix} 2 & a \\ b & 3 \end{pmatrix}$ memetakan titik $(3, -2)$ ke titik $(12, 6)$. Nilai $a + 2b$ adalah ....

- A. $-2$  
  <sub>Salah: menghitung $b+2a$ (peran $a$ dan $b$ tertukar)</sub>
- **B. $5$** ✅  
  <sub>Benar: $6-2a=12$ memberi $a=-3$; $3b-6=6$ memberi $b=4$; jadi $a+2b=-3+8=5$</sub>
- C. $11$  
  <sub>Salah: salah tanda pada $a$: $6-2a=12$ dianggap $a=3$</sub>
- D. $1$  
  <sub>Salah: menghitung $a+b$, lupa mengalikan $b$ dengan 2</sub>

**Pembahasan:** $\begin{pmatrix} 2 & a \\ b & 3 \end{pmatrix}\begin{pmatrix} 3 \\ -2 \end{pmatrix}=\begin{pmatrix} 6-2a \\ 3b-6 \end{pmatrix}=\begin{pmatrix} 12 \\ 6 \end{pmatrix}$.
**Acuan:** siswa — siswa hal.238

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b05-b-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: mengenali transformasi dari titik dan peta*

Di antara transformasi berikut, yang memetakan titik $(6, -2)$ ke titik $(2, 6)$ adalah ....

- A. pencerminan terhadap garis $y = x$  
  <sub>Salah: pencerminan ini memetakan $(6,-2)$ ke $(-2,6)$</sub>
- B. rotasi $90^\circ$ searah jarum jam terhadap titik asal  
  <sub>Salah: rotasi $-90^\circ$ memetakan $(6,-2)$ ke $(-2,-6)$, bukan $(2,6)$</sub>
- **C. rotasi $90^\circ$ berlawanan arah jarum jam terhadap titik asal** ✅  
  <sub>Benar: matriks rotasi $90^\circ$ $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ memetakan $(6,-2)$ ke $(2,6)$</sub>
- D. pencerminan terhadap garis $y = -x$  
  <sub>Salah: pencerminan ini memetakan $(6,-2)$ ke $(2,-6)$</sub>

**Pembahasan:** Rotasi $90^\circ$: $(x,y)\to(-y,x)=(2,6)$. Rotasi $-90^\circ$ memberi $(-2,-6)$, $y=x$ memberi $(-2,6)$, dan $y=-x$ memberi $(2,-6)$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b05-b-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: prapeta dilatasi berpusat sembarang*

Dilatasi dengan titik pusat $(2, -1)$ dan faktor skala $3$ memetakan titik $P$ ke $P'(11, 8)$. Koordinat titik $P$ adalah ....

- **A. $(5, 2)$** ✅  
  <sub>Benar: $11=3(x-2)+2$ memberi $x=5$ dan $8=3(y+1)-1$ memberi $y=2$</sub>
- B. $(29, 26)$  
  <sub>Salah: menerapkan dilatasi lagi pada $P'$, bukan membaliknya</sub>
- C. $(1, 4)$  
  <sub>Salah: mengurangi koordinat pusat, bukan menambahkannya, setelah membagi</sub>
- D. $(3, 3)$  
  <sub>Salah: lupa menambahkan koordinat pusat setelah membagi dengan 3</sub>

**Pembahasan:** $x'=k(x-a)+a$ sehingga $x=\frac{x'-a}{k}+a=\frac{11-2}{3}+2=5$ dan $y=\frac{8+1}{3}-1=2$.
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b05-b-medium-bt01-018
*orisinal | C4 | 4 langkah | jenis: pencerminan dengan titik berparameter*

Titik $P(2k, k - 3)$ dicerminkan terhadap garis $y = -x$ dengan perkalian matriks. Jika absis titik petanya adalah $-4$, maka ordinat titik petanya adalah ....

- A. $14$  
  <sub>Salah: salah tanda pada ordinat peta (ordinat dianggap $2k$)</sub>
- **B. $-14$** ✅  
  <sub>Benar: $(x,y)\to(-y,-x)$ sehingga peta $P$ adalah $(3-k,\,-2k)$; $3-k=-4$ memberi $k=7$ dan ordinat $-2k=-14$</sub>
- C. $1$  
  <sub>Salah: mengira absis peta $-2k=-4$ (koordinat tidak ditukar dengan benar)</sub>
- D. $-2$  
  <sub>Salah: memakai pencerminan $y=x$: absis peta $k-3=-4$ memberi $k=-1$</sub>

**Pembahasan:** Matriks $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ memetakan $(2k,k-3)$ ke $(3-k,-2k)$. Dari $3-k=-4$ diperoleh $k=7$, sehingga ordinat $-14$.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b05-b-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: sudut rotasi dari matriks*

Matriks $\begin{pmatrix} - \frac{1}{2} & \frac{\sqrt{3}}{2} \\ - \frac{\sqrt{3}}{2} & - \frac{1}{2} \end{pmatrix}$ adalah matriks rotasi terhadap titik asal sebesar $\theta$ radian dengan $0 < \theta < 2\pi$. Nilai $\theta$ adalah ....

- A. $\frac{5\pi}{6}$  
  <sub>Salah: menukar nilai $\cos\theta$ dan $\sin\theta$ ($\cos\theta=-\frac{\sqrt{3}}{2}$)</sub>
- B. $\frac{2\pi}{3}$  
  <sub>Salah: $\cos\theta$ benar tetapi tanda $\sin\theta$ dibaca positif (kuadran II)</sub>
- **C. $\frac{4\pi}{3}$** ✅  
  <sub>Benar: $\cos\theta=-\frac{1}{2}$ dan $\sin\theta=-\frac{\sqrt{3}}{2}$ (kuadran III), sehingga $\theta=\frac{4\pi}{3}$</sub>
- D. $\frac{5\pi}{3}$  
  <sub>Salah: memilih sudut dengan $\sin\theta$ benar tetapi $\cos\theta=\frac{1}{2}$</sub>

**Pembahasan:** Matriks rotasi $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$: $\cos\theta=-\frac{1}{2}$, $\sin\theta=-\frac{\sqrt{3}}{2}$, jadi $\theta=\frac{4\pi}{3}$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b05-b-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: peta garis oleh matriks pencerminan*

Garis $3x - 2y + 6 = 0$ dicerminkan terhadap garis $y = x$ dengan perkalian matriks. Persamaan peta garis tersebut adalah ....

- **A. $2x - 3y - 6 = 0$** ✅  
  <sub>Benar: $(x',y')=(y,x)$ sehingga $x=y'$ dan $y=x'$; substitusi: $3y'-2x'+6=0$ atau $2x'-3y'-6=0$</sub>
- B. $3x + 2y - 6 = 0$  
  <sub>Salah: memakai pencerminan terhadap sumbu-$y$</sub>
- C. $3x + 2y + 6 = 0$  
  <sub>Salah: memakai pencerminan terhadap sumbu-$x$</sub>
- D. $2x - 3y + 6 = 0$  
  <sub>Salah: memakai pencerminan terhadap $y=-x$</sub>

**Pembahasan:** Matriks $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ menukar koordinat: $x=y'$ dan $y=x'$. Substitusi menghasilkan $3y'-2x'+6=0$, yaitu $2x-3y-6=0$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b05-b-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi pernyataan determinan*

Perhatikan matriks-matriks transformasi pada bidang Kartesius. Pernyataan yang benar tentang determinan matriks transformasi adalah ....

- **A. Determinan matriks pencerminan terhadap garis $y = x$ adalah $-1$, sedangkan determinan matriks rotasi sebesar $\theta$ terhadap titik asal selalu $1$.** ✅  
  <sub>Benar: matriks $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ berdeterminan $0-1=-1$; matriks rotasi berdeterminan $\cos^2\theta+\sin^2\theta=1$ untuk setiap $\theta$</sub>
- B. Determinan matriks pencerminan terhadap sumbu-$x$ adalah $1$ karena pencerminan tidak mengubah ukuran bangun.  
  <sub>Salah: determinan matriks $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ adalah $-1$; ukuran tetap tetapi tandanya negatif</sub>
- C. Determinan matriks dilatasi berpusat di $O$ dengan faktor skala $k$ adalah $k$.  
  <sub>Salah: determinan $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ adalah $k^2$, bukan $k$</sub>
- D. Determinan matriks rotasi sebesar $\theta$ terhadap titik asal adalah $\cos\theta$.  
  <sub>Salah: hanya mengambil elemen diagonal; determinan $\cos^2\theta+\sin^2\theta=1$</sub>

**Pembahasan:** Hitung: $\det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}=-1$; $\det\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}=1$; $\det\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}=k^2$; $\det\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}=-1$.
**Acuan:** siswa — siswa hal.238

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b05-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: transformasi yang mengubah jarak*

Transformasi kaku adalah transformasi yang mempertahankan jarak antara setiap dua titik. Matriks berikut mewakili transformasi pada bidang Kartesius dengan titik pusat atau garis cermin melalui titik asal. Matriks yang mewakili transformasi yang BUKAN transformasi kaku adalah ....

- A. $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$  
  <sub>Salah: pencerminan terhadap garis $y=-x$; jarak tetap</sub>
- B. $\begin{pmatrix} \frac{3}{5} & -\frac{4}{5} \\ \frac{4}{5} & \frac{3}{5} \end{pmatrix}$  
  <sub>Salah: rotasi dengan $\cos\theta=\frac{3}{5}$, $\sin\theta=\frac{4}{5}$; panjang vektor tetap, jadi kaku</sub>
- C. $\begin{pmatrix} \frac{3}{5} & \frac{4}{5} \\ \frac{4}{5} & -\frac{3}{5} \end{pmatrix}$  
  <sub>Salah: pencerminan terhadap suatu garis melalui titik asal; $M^TM=I$ sehingga jarak tetap</sub>
- **D. $\begin{pmatrix} -\frac{1}{2} & 0 \\ 0 & -\frac{1}{2} \end{pmatrix}$** ✅  
  <sub>Benar: matriks ini adalah dilatasi berfaktor $-\frac{1}{2}$: vektor $(2,0)$ dipetakan ke $(-1,0)$ sehingga panjangnya berubah menjadi setengah</sub>

**Pembahasan:** Uji $M^TM=I$ (kolom-kolomnya saling tegak lurus dan panjang 1): ketiga opsi lain memenuhi, sedangkan dilatasi berfaktor $-\frac{1}{2}$ mengalikan semua jarak dengan $\frac{1}{2}$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b05-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: syarat parameter matriks rotasi*

Matriks $\begin{pmatrix} k & -\frac{1}{2} \\ \frac{1}{2} & k \end{pmatrix}$ dengan $k$ bilangan real mewakili rotasi terhadap titik asal. Himpunan semua nilai $k$ yang mungkin adalah ....

- A. $\left\{-\frac{1}{2}, \frac{1}{2}\right\}$  
  <sub>Salah: menyamakan $k$ dengan $\sin\theta$ sehingga $k^2=\frac{1}{4}$, bukan $1-\frac{1}{4}$</sub>
- **B. $\left\{-\frac{\sqrt{3}}{2}, \frac{\sqrt{3}}{2}\right\}$** ✅  
  <sub>Benar: bentuk rotasi memerlukan $\cos\theta=k$ dan $\sin\theta=\frac{1}{2}$, sehingga $k^2+\frac{1}{4}=1$ dan $k=\pm\frac{\sqrt{3}}{2}$ ($\theta=30^\circ$ atau $150^\circ$)</sub>
- C. $\left\{-\frac{\sqrt{3}}{2}\right\}$  
  <sub>Salah: hanya mengambil akar negatif; $\theta=30^\circ$ juga memenuhi</sub>
- D. $\left\{\frac{\sqrt{3}}{2}\right\}$  
  <sub>Salah: hanya mengambil akar positif; lupa $\cos\theta$ boleh negatif ($\theta=150^\circ$)</sub>

**Pembahasan:** Matriks rotasi berbentuk $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$. Maka $\sin\theta=\frac{1}{2}$ dan $\cos\theta=k$, sehingga $k^2=1-\frac{1}{4}=\frac{3}{4}$, yaitu $k=\pm\frac{\sqrt{3}}{2}$. Keduanya sah karena $\sin\theta=\frac{1}{2}$ dipenuhi oleh $30^\circ$ dan $150^\circ$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b05-b-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: kesalahan pembentukan matriks*

Suatu transformasi memetakan setiap titik $(x, y)$ ke titik $(2x - y,\ x + 3y)$. Seorang siswa menyatakan matriksnya adalah $\begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$. Kesalahan yang dilakukan siswa tersebut adalah ....

- **A. Koefisien $x$ dan $y$ dari tiap koordinat peta ditulis per kolom, padahal seharusnya per baris: baris pertama untuk absis peta dan baris kedua untuk ordinat peta.** ✅  
  <sub>Benar: yang benar $\begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix}$; matriks siswa adalah transposnya sehingga memetakan $(x,y)$ ke $(2x+y,\ -x+3y)$</sub>
- B. Elemen $-1$ seharusnya $+1$ karena matriks transformasi tidak boleh memuat elemen negatif.  
  <sub>Salah: matriks transformasi boleh memuat elemen negatif, misalnya matriks pencerminan</sub>
- C. Matriks seharusnya memuat kolom tambahan untuk suku konstan sehingga berukuran $2 \times 3$.  
  <sub>Salah: aturan pemetaan tidak memuat suku konstan, matriks $2 \times 2$ sudah cukup</sub>
- D. Elemen diagonal utama seharusnya ditukar menjadi $3$ dan $2$.  
  <sub>Salah: diagonal utama $2$ dan $3$ sudah benar (koefisien $x$ pada absis dan koefisien $y$ pada ordinat)</sub>

**Pembahasan:** Perkalian $\begin{pmatrix} p & q \\ r & s \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix}=\begin{pmatrix} px+qy \\ rx+sy \end{pmatrix}$, sehingga $p=2$, $q=-1$, $r=1$, $s=3$. Matriks siswa menukar baris dengan kolom.
**Acuan:** siswa — siswa hal.238

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b05-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: kesalahan substitusi prapeta*

Seorang siswa mencari peta garis $x + 2y - 6 = 0$ oleh dilatasi berpusat di $O$ dengan faktor skala $3$. Ia menulis: "Karena $(x', y') = (3x, 3y)$, substitusi $x = 3x'$ dan $y = 3y'$ ke persamaan garis, diperoleh $3x' + 6y' - 6 = 0$, sehingga petanya $x + 2y - 2 = 0$." Kesalahan siswa tersebut terletak pada ....

- A. langkah menyederhanakan $3x' + 6y' - 6 = 0$ menjadi $x' + 2y' - 2 = 0$, sebab persamaan garis tidak boleh dibagi dengan bilangan yang sama  
  <sub>Salah: membagi seluruh persamaan dengan 3 sah; kesalahan ada pada arah substitusi sebelumnya</sub>
- B. anggapan bahwa dilatasi mengubah garis, padahal dilatasi berpusat di $O$ membuat petanya tetap $x + 2y - 6 = 0$  
  <sub>Salah: dilatasi faktor $3$ menggeser garis yang tidak melalui $O$; petanya $x+2y-18=0$</sub>
- C. substitusi yang seharusnya hanya dilakukan pada peubah $y$, sedangkan $x$ dibiarkan  
  <sub>Salah: kedua koordinat sama-sama dikali $3$ oleh dilatasi, jadi keduanya harus disubstitusi</sub>
- **D. penggunaan $x = 3x'$ dan $y = 3y'$; seharusnya $x = \frac{x'}{3}$ dan $y = \frac{y'}{3}$ karena $x'=3x$** ✅  
  <sub>Benar: dari $x'=3x$ diperoleh $x=\frac{x'}{3}$; substitusi benar menghasilkan $\frac{x'}{3}+\frac{2y'}{3}-6=0$, yaitu $x'+2y'-18=0$</sub>

**Pembahasan:** Titik peta $(x',y')=(3x,3y)$ berarti prapeta $(x,y)=(\frac{x'}{3},\frac{y'}{3})$. Substitusi ke $x+2y-6=0$ memberi $x'+2y'-18=0$. Siswa memakai arah sebaliknya.
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b05-b-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: kesalahan nilai trigonometri sudut negatif*

Seorang siswa menuliskan matriks rotasi sebesar $-60^\circ$ terhadap titik asal sebagai $\begin{pmatrix} \frac{1}{2} & -\frac{\sqrt{3}}{2} \\ \frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$. Pernyataan yang benar tentang hasil siswa tersebut adalah ....

- A. Matriks itu salah karena rotasi $-60^\circ$ memiliki matriks $\begin{pmatrix} -\frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & -\frac{1}{2} \end{pmatrix}$.  
  <sub>Salah: itu matriks rotasi $240^\circ$ (diagonal salah tanda), bukan $-60^\circ$</sub>
- B. Matriks itu salah karena $\cos(-60^\circ)=-\frac{1}{2}$ sehingga diagonal utama harus negatif.  
  <sub>Salah: $\cos(-60^\circ)=\frac{1}{2}$ karena kosinus fungsi genap; diagonal sudah benar</sub>
- **C. Matriks itu salah karena memakai $\sin 60^\circ$ untuk $\sin(-60^\circ)$; matriks tersebut sebenarnya mewakili rotasi $60^\circ$.** ✅  
  <sub>Benar: $\sin(-60^\circ)=-\frac{\sqrt{3}}{2}$ sehingga matriks yang benar $\begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$; matriks siswa adalah matriks rotasi $60^\circ$</sub>
- D. Matriks itu benar karena rotasi $-60^\circ$ dan $60^\circ$ memiliki matriks yang sama.  
  <sub>Salah: kedua sudut memberi $\sin$ berbeda tanda sehingga matriksnya berbeda</sub>

**Pembahasan:** Rumus $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ dengan $\theta=-60^\circ$: $\cos\theta=\frac{1}{2}$ dan $\sin\theta=-\frac{\sqrt{3}}{2}$, memberi $\begin{pmatrix} \frac{1}{2} & \frac{\sqrt{3}}{2} \\ -\frac{\sqrt{3}}{2} & \frac{1}{2} \end{pmatrix}$. Matriks siswa sama dengan matriks rotasi $+60^\circ$.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b05-b-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal*

Seorang siswa berpendapat: "Jika suatu matriks $2 \times 2$ memetakan sebuah titik bukan titik asal ke dirinya sendiri, maka matriks itu pasti matriks identitas." Pasangan matriks dan titik berikut yang merupakan contoh penyangkal pendapat tersebut adalah ....

- A. matriks identitas dan titik $(3, -3)$  
  <sub>Salah: titik tetap, tetapi matriksnya memang identitas sehingga mendukung pendapat, bukan menyangkal</sub>
- B. matriks pencerminan terhadap garis $y = x$ dan titik $(3, -3)$  
  <sub>Salah: titik dipetakan ke $(-3, 3)$, bukan ke dirinya sendiri sehingga bukan penyangkal</sub>
- **C. matriks pencerminan terhadap garis $y = -x$ dan titik $(3, -3)$** ✅  
  <sub>Benar: pencerminan terhadap $y=-x$ memetakan $(x,y)$ ke $(-y,-x)$, sehingga $(3,-3)\mapsto(3,-3)$ padahal matriksnya bukan identitas</sub>
- D. matriks rotasi $90^\circ$ terhadap titik asal dan titik $(3, 3)$  
  <sub>Salah: titik dipetakan ke $(-3, 3)$, bukan dirinya sendiri</sub>

**Pembahasan:** Penyangkal harus memetakan titik ke dirinya sendiri dan bukan identitas. Hanya pencerminan terhadap $y=-x$ dengan titik $(3,-3)$ yang memenuhi: $(-y,-x)=(3,-3)$.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b05-b-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: luas dan orientasi bangun peta*

Segitiga $ABC$ memiliki titik sudut $A(1, 1)$, $B(5, 1)$, dan $C(1, 4)$ sehingga urutan $A \to B \to C$ berlawanan arah jarum jam dan luasnya $6$ satuan luas. Segitiga ini dipetakan oleh matriks $\begin{pmatrix} -2 & 0 \\ 0 & -2 \end{pmatrix}$ menjadi segitiga $A'B'C'$. Pernyataan yang benar tentang segitiga $A'B'C'$ adalah ....

- **A. luasnya $24$ satuan luas dan urutan $A' \to B' \to C'$ tetap berlawanan arah jarum jam** ✅  
  <sub>Benar: $A'(-2,-2)$, $B'(-10,-2)$, $C'(-2,-8)$; luas $=\frac{1}{2}\cdot 8\cdot 6=24$ dan urutan tetap berlawanan arah jarum jam karena $\det=4>0$</sub>
- B. luasnya $12$ satuan luas dan urutan $A' \to B' \to C'$ tetap berlawanan arah jarum jam  
  <sub>Salah: luas dikali $|k|=2$, padahal luas dikali $k^2=4$</sub>
- C. luasnya $24$ satuan luas dan urutan $A' \to B' \to C'$ searah jarum jam  
  <sub>Salah: mengira faktor negatif membalik orientasi; determinan $4>0$ sehingga orientasi tetap</sub>
- D. luasnya $12$ satuan luas dan urutan $A' \to B' \to C'$ searah jarum jam  
  <sub>Salah: salah pada luas ($k$ bukan $k^2$) dan salah pada orientasi</sub>

**Pembahasan:** Dilatasi faktor $-2$ memetakan titik sudut ke $A'(-2,-2)$, $B'(-10,-2)$, $C'(-2,-8)$. Alasnya $8$, tingginya $6$, luas $24$. Matriksnya berdeterminan $4>0$, jadi orientasi tidak berbalik (setara dilatasi $2$ dan rotasi $180^\circ$).
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b05-b-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: memilih matriks dari perubahan luas*

Sebuah segitiga berluas $5$ satuan luas dipetakan oleh suatu matriks menjadi segitiga berluas $45$ satuan luas, dan urutan titik sudutnya tidak berbalik arah. Matriks yang mungkin digunakan adalah ....

- A. $\begin{pmatrix} 6 & 0 \\ 0 & 6 \end{pmatrix}$  
  <sub>Salah: determinan $36$, luas menjadi $36$ kali, bukan $9$ kali</sub>
- **B. $\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$** ✅  
  <sub>Benar: faktor luas $=|\det|=9$ dan orientasi tetap berarti $\det=9$; hanya $\begin{pmatrix} 3 & 0 \\ 0 & 3 \end{pmatrix}$ ($\det=9$)</sub>
- C. $\begin{pmatrix} 9 & 0 \\ 0 & 9 \end{pmatrix}$  
  <sub>Salah: memakai faktor skala $9$ langsung dari $45\div5$; luas menjadi $81$ kali ($\det=81$)</sub>
- D. $\begin{pmatrix} 0 & 3 \\ 3 & 0 \end{pmatrix}$  
  <sub>Salah: luas menjadi $9$ kali tetapi $\det=-9$ sehingga orientasi berbalik</sub>

**Pembahasan:** Luas peta $=|\det M|\times$ luas semula, sehingga $|\det M|=\frac{45}{5}=9$. Orientasi tetap berarti $\det M>0$, jadi $\det M=9$. Hanya opsi pertama memenuhi.
**Acuan:** siswa — siswa hal.246

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b05-b-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: perbandingan dua transformasi*

Untuk sembarang titik $(a, b)$ dengan $a \neq 0$ dan $b \neq 0$, misalkan $P$ adalah peta titik itu oleh rotasi $90^\circ$ berlawanan arah jarum jam terhadap titik asal, dan $Q$ adalah peta titik itu oleh pencerminan terhadap garis $y = -x$. Pernyataan yang selalu benar tentang $P$ dan $Q$ adalah ....

- A. $P$ dan $Q$ selalu berlawanan, yaitu $Q=-P$  
  <sub>Salah: $-P=(b,-a)$, sedangkan $Q=(-b,-a)$; sama hanya jika $b=0$, yang dikecualikan</sub>
- B. $P$ dan $Q$ memiliki ordinat yang sama, sedangkan absisnya berlawanan tanda  
  <sub>Salah: tertukar: absis yang sama ($-b$), bukan ordinat</sub>
- C. $P$ dan $Q$ selalu berimpit  
  <sub>Salah: berimpit hanya jika $a=0$, yang dikecualikan</sub>
- **D. $P$ dan $Q$ memiliki absis yang sama, sedangkan ordinatnya berlawanan tanda** ✅  
  <sub>Benar: $P=(-b, a)$ dan $Q=(-b, -a)$: absis sama ($-b$), ordinat $a$ dan $-a$</sub>

**Pembahasan:** $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=\begin{pmatrix} -b \\ a \end{pmatrix}$ dan $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}\begin{pmatrix} a \\ b \end{pmatrix}=\begin{pmatrix} -b \\ -a \end{pmatrix}$. Absisnya sama, ordinatnya berlawanan.
**Acuan:** siswa — siswa hal.244

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b05-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: merancang matriks dari dua pasang titik*

Suatu transformasi dengan matriks $2 \times 2$ memetakan titik $(1, 2)$ ke $(7, -1)$ dan titik $(2, 1)$ ke $(8, 1)$. Matriks transformasi tersebut adalah ....

- A. $\begin{pmatrix} 5 & 1 \\ 1 & -1 \end{pmatrix}$  
  <sub>Salah: memetakan $(1,2)$ ke $(7,-1)$ tetapi $(2,1)$ ke $(11,1)$; hanya satu pasangan diperiksa</sub>
- **B. $\begin{pmatrix} 3 & 2 \\ 1 & -1 \end{pmatrix}$** ✅  
  <sub>Benar: $\begin{pmatrix} p & q \\ r & s \end{pmatrix}$ memenuhi $p+2q=7$, $2p+q=8$ (memberi $p=3$, $q=2$) dan $r+2s=-1$, $2r+s=1$ (memberi $r=1$, $s=-1$)</sub>
- C. $\begin{pmatrix} 2 & 3 \\ -1 & 1 \end{pmatrix}$  
  <sub>Salah: memetakan $(1,2)$ ke $(8,1)$ dan $(2,1)$ ke $(7,-1)$; pasangan peta tertukar</sub>
- D. $\begin{pmatrix} 4 & 0 \\ 1 & -1 \end{pmatrix}$  
  <sub>Salah: memetakan $(2,1)$ ke $(8,1)$ tetapi $(1,2)$ ke $(4,-1)$; hanya satu pasangan diperiksa</sub>

**Pembahasan:** Misalkan matriksnya $\begin{pmatrix} p & q \\ r & s \end{pmatrix}$. Dari $(1,2)\mapsto(7,-1)$: $p+2q=7$, $r+2s=-1$. Dari $(2,1)\mapsto(8,1)$: $2p+q=8$, $2r+s=1$. Penyelesaian: $p=3,q=2,r=1,s=-1$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b05-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: merancang dilatasi dari dua pasang titik*

Dilatasi memetakan titik $A(3, 5)$ ke $A'(-3, -4)$ dan titik $B(0, 1)$ ke $B'(3, 4)$. Titik pusat dan faktor skala dilatasi tersebut berturut-turut adalah ....

- A. pusat $(-1, -2)$ dan faktor skala $-2$  
  <sub>Salah: tanda koordinat pusat terbalik; $A$ dipetakan ke $(-9, -16)$</sub>
- B. pusat $(1, 2)$ dan faktor skala $2$  
  <sub>Salah: pusat benar tetapi tanda faktor skala keliru; $A$ dipetakan ke $(5, 8)$</sub>
- C. pusat $(2, 1)$ dan faktor skala $-2$  
  <sub>Salah: absis dan ordinat pusat tertukar; $A$ dipetakan ke $(0, -7)$</sub>
- **D. pusat $(1, 2)$ dan faktor skala $-2$** ✅  
  <sub>Benar: $\overrightarrow{B'A'}=k\overrightarrow{BA}$: $(-6,-8)=k(3,4)$ sehingga $k=-2$; lalu $A'=k(A-C)+C$ memberi pusat $C=(1,2)$</sub>

**Pembahasan:** Karena $(A'-B')=k(A-B)$: $(-6,-8)=k(3,4)$ sehingga $k=-2$. Dari $A'=k(A-C)+C=kA+(1-k)C$: $(-3,-4)=(-6,-10)+3C$ sehingga $C=(1,2)$. Cek $B$: $-2(0-1)+1=3$ dan $-2(1-2)+2=4$.
**Acuan:** siswa — siswa hal.245

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b05-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: batas representasi dengan matriks 2x2*

Perkalian satu matriks $2 \times 2$ dengan vektor posisi selalu memetakan titik asal $(0, 0)$ ke dirinya sendiri. Transformasi berikut yang TIDAK dapat dinyatakan hanya dengan satu perkalian matriks $2 \times 2$ dengan vektor posisi adalah ....

- A. pencerminan terhadap sumbu-$y$  
  <sub>Salah: bermatriks $\begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$ dan titik asal tetap</sub>
- B. dilatasi dengan titik pusat $O(0, 0)$ dan faktor skala $-5$  
  <sub>Salah: bermatriks $\begin{pmatrix} -5 & 0 \\ 0 & -5 \end{pmatrix}$ dan titik asal tetap</sub>
- **C. dilatasi dengan titik pusat $(2, 3)$ dan faktor skala $2$** ✅  
  <sub>Benar: dilatasi berpusat $(2,3)$ memetakan $(0,0)$ ke $(-2,-3)$, bukan ke dirinya sendiri; perlu tambahan vektor translasi</sub>
- D. pencerminan terhadap garis $y = -x$  
  <sub>Salah: bermatriks $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$ dan titik asal tetap</sub>

**Pembahasan:** Transformasi yang bisa ditulis sebagai $M\begin{pmatrix} x \\ y \end{pmatrix}$ harus memetakan $(0,0)$ ke $(0,0)$. Dilatasi berpusat $(2,3)$ faktor $2$ memetakan $(x,y)$ ke $(2x-2,\ 2y-3)$, sehingga $(0,0)\mapsto(-2,-3)$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b05-b-hard-bt01-014
*orisinal | C5 | 3 langkah | jenis: menilai dua pendapat*

Andi berpendapat bahwa $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$ adalah matriks rotasi $180^\circ$ terhadap titik asal. Bimo berpendapat matriks yang sama adalah matriks dilatasi berpusat di $O$ dengan faktor skala $-1$. Penilaian yang benar adalah ....

- A. Hanya Andi yang benar, karena faktor skala dilatasi tidak boleh negatif.  
  <sub>Salah: Sifat dilatasi hanya mensyaratkan $k \neq 0$, jadi $k=-1$ sah</sub>
- B. Keduanya salah, karena matriks tersebut mewakili pencerminan terhadap sumbu-$x$.  
  <sub>Salah: pencerminan terhadap sumbu-$x$ bermatriks $\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$</sub>
- **C. Keduanya benar, karena kedua transformasi memetakan $(x, y)$ ke $(-x, -y)$.** ✅  
  <sub>Benar: rotasi $180^\circ$: $\cos 180^\circ=-1$, $\sin 180^\circ=0$ memberi matriks tersebut; dilatasi faktor $k=-1$ memberi $\begin{pmatrix} k & 0 \\ 0 & k \end{pmatrix}$ yang sama</sub>
- D. Hanya Bimo yang benar, karena matriks rotasi $180^\circ$ adalah matriks identitas.  
  <sub>Salah: matriks identitas adalah rotasi $0^\circ$ ($360^\circ$), bukan $180^\circ$</sub>

**Pembahasan:** Sifat 5.7 dengan $\theta=180^\circ$ memberi $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$. Sifat 5.9 dengan $k=-1$ memberi matriks yang sama. Kedua pendapat benar.
**Acuan:** siswa — siswa hal.246

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
