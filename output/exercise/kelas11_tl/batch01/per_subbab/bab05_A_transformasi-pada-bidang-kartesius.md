# Lembar koreksi — kelas11_tl SMA11L-B5 subbab A: Transformasi pada Bidang Kartesius

52 soal | easy 20, medium 20, hard 12 | variasi 20, orisinal 32
> **Kapasitas kurang (hard): 12 dari kuota 20** — Materi subbab A (translasi, refleksi, rotasi, dilatasi) hanya menopang sekitar 12 soal hard yang benar-benar C5 tanpa menjadi soal hitung langsung atau kembar berangka beda; soal parameter dan hitung murni sudah dipakai di medium.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b05-a-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: pencerminan terhadap garis y = mx + c*

Tentukan bayangan dari titik $(-12, 10)$ yang dicerminkan terhadap garis $y = 7x - 6$.

- A. $(16, 12)$  
  <sub>Salah: memakai $c$ saja, bukan $2c$, pada ordinat</sub>
- B. $(2, 8)$  
  <sub>Salah: berhenti di titik potong dengan garis tegak lurus (titik tengah), belum dicari bayangannya</sub>
- **C. $(16, 6)$** ✅  
  <sub>Benar: $a=-12$, $b=10$, $m=7$, $c=-6$ sehingga $d=\frac{a+m(b-c)}{m^2+1}=\frac{-12+7\cdot 16}{50}=2$; bayangan $(2d-a,\,2md+2c-b)=(16,\,6)$</sub>
- D. $(16, 18)$  
  <sub>Salah: lupa suku $2c$ pada ordinat $2md + 2c - b$</sub>

**Pembahasan:** $d=2$, bayangan $(2\cdot 2+12,\ 2\cdot 7\cdot 2-12-10)=(16, 6)$.
**Acuan:** siswa — siswa hal.223 Contoh 5.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b05-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: pencerminan terhadap garis ax + by + c = 0*

Tentukan bayangan dari titik $(-9, 6)$ yang dicerminkan terhadap garis $4x + 3y - 7 = 0$.

- A. $(6, -9)$  
  <sub>Salah: mengira bayangan hanya menukar absis dan ordinat</sub>
- B. $(-17, 0)$  
  <sub>Salah: tanda salah: memakai $x_0+2ad'$ bukan $x_0-2ad'$</sub>
- **C. $(-1, 12)$** ✅  
  <sub>Benar: $a x_0+b y_0+c=-36+18-7=-25$, $a^2+b^2=25$, bayangan $(x_0-2a\cdot(-1),\ y_0-2b\cdot(-1))=(-1, 12)$</sub>
- D. $(-5, 9)$  
  <sub>Salah: hanya menghitung titik potong (kaki garis tegak lurus), bukan bayangan</sub>

**Pembahasan:** Nilai $4(-9)+3(6)-7=-25$ dibagi $25$ sama dengan $-1$; bayangan $(-9+8,\ 6+6)=(-1, 12)$.
**Acuan:** siswa — siswa hal.224 Contoh 5.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b05-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: pencerminan terhadap garis ax + by + c = 0*

Tentukan peta dari transformasi geometri berikut. Titik $(8, -4)$ yang dicerminkan terhadap garis $4x - 3y + 6 = 0$.

- A. $(24, -16)$  
  <sub>Salah: tanda salah pada pengurangan $2ad'$ dan $2bd'$</sub>
- **B. $(-8, 8)$** ✅  
  <sub>Benar: $4(8)-3(-4)+6=50$; $50/25=2$; peta $(8-2\cdot 4\cdot 2,\ -4+2\cdot 3\cdot 2)=(-8, 8)$</sub>
- C. $(0, 2)$  
  <sub>Salah: hanya menghitung kaki garis tegak lurus (titik tengah), tidak sampai bayangan</sub>
- D. $(-8, 4)$  
  <sub>Salah: mengira pencerminan sama dengan perubahan tanda kedua koordinat</sub>

**Pembahasan:** Nilai $4\cdot 8-3(-4)+6=50$, dibagi $a^2+b^2=25$ diperoleh $2$; $(8-16,\ -4+12)=(-8, 8)$.
**Acuan:** pretest — kelas11_tl-b05-p0238-latihan-a-4b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b05-a-easy-bt01-004
*variasi (angka) | C1 | 1 langkah | jenis: translasi segitiga*

Tentukan peta dari transformasi geometri berikut. Segitiga $ABC$ dengan $A(6, -2)$, $B(-4, 5)$, dan $C(7, 8)$ yang ditranslasikan oleh vektor $\begin{pmatrix} 9 \\ -7 \end{pmatrix}$.

- **A. $A'(15, -9)$, $B'(5, -2)$, $C'(16, 1)$** ✅  
  <sub>Benar: tiap titik ditambah $(9, -7)$</sub>
- B. $A'(-1, 7)$, $B'(-11, 14)$, $C'(0, 17)$  
  <sub>Salah: tanda komponen vektor tertukar dan salah</sub>
- C. $A'(-3, 5)$, $B'(-13, 12)$, $C'(-2, 15)$  
  <sub>Salah: vektor translasi dikurangkan, bukan ditambahkan</sub>
- D. $A'(15, 5)$, $B'(5, 12)$, $C'(16, 15)$  
  <sub>Salah: mengabaikan tanda minus pada komponen kedua vektor</sub>

**Pembahasan:** $A'=(6+9,-2-7)$, $B'=(-4+9,5-7)$, $C'=(7+9,8-7)$.
**Acuan:** pretest — kelas11_tl-b05-p0238-latihan-a-4c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b05-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: rotasi garis terhadap titik asal*

Tentukan peta dari garis $6x + 7y - 8 = 0$ yang dirotasikan $90^\circ$ berlawanan arah jarum jam terhadap titik asal.

- **A. $-7x + 6y - 8 = 0$** ✅  
  <sub>Benar: $(x,y)\to(-y,x)$ sehingga $x=y'$ dan $y=-x'$; substitusi memberi $-7x'+6y'-8=0$</sub>
- B. $-6x - 7y - 8 = 0$  
  <sub>Salah: memakai rotasi $180^\circ$, yakni $(x,y)\to(-x,-y)$</sub>
- C. $7x - 6y - 8 = 0$  
  <sub>Salah: memutar searah jarum jam ($-90^\circ$), bukan $90^\circ$ berlawanan arah jarum jam</sub>
- D. $6x + 7y - 8 = 0$  
  <sub>Salah: menganggap garis tidak berubah setelah rotasi</sub>

**Pembahasan:** Rotasi $90^\circ$: $x'=-y$, $y'=x$, jadi $x=y'$ dan $y=-x'$. Substitusi ke $6x+7y-8=0$ menghasilkan $6y'-7x'-8=0$.
**Acuan:** pretest — kelas11_tl-b05-p0238-latihan-a-4d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b05-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: dilatasi titik berpusat C*

Diberikan titik $C(2, -3)$, titik $A(5, 4)$, dan $k = 4$. Tentukan $D_{C,k}(A)$.

- **A. $(14, 25)$** ✅  
  <sub>Benar: $(k(x-a)+a,\ k(y-b)+b)=(4\cdot 3+2,\ 4\cdot 7-3)=(14, 25)$</sub>
- B. $(20, 16)$  
  <sub>Salah: memakai pusat $O(0,0)$ sehingga hanya mengalikan koordinat dengan $k$</sub>
- C. $(12, 28)$  
  <sub>Salah: lupa menambahkan kembali koordinat pusat $C$</sub>
- D. $(22, 13)$  
  <sub>Salah: mengalikan koordinat $A$ dengan $k$ lalu menambah $C$ (bukan $k(A-C)+C$)</sub>

**Pembahasan:** $A'=(4(5-2)+2,\ 4(4+3)-3)=(14, 25)$.
**Acuan:** siswa — siswa hal.235 Contoh 5.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b05-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: dilatasi lingkaran*

Peta dari lingkaran $L: (x + 4)^2 + (y - 6)^2 = 36$ yang didilatasikan dengan titik pusat $C(-5, 1)$ dan faktor skala $4$ adalah ....

- A. $(x + 1)^2 + (y - 21)^2 = 144$  
  <sub>Salah: mengalikan $r^2$ dengan $k$, bukan $k^2$</sub>
- B. $(x + 16)^2 + (y - 24)^2 = 576$  
  <sub>Salah: pusat lingkaran hanya dikalikan $k$ tanpa memperhatikan pusat dilatasi $C$</sub>
- **C. $(x + 1)^2 + (y - 21)^2 = 576$** ✅  
  <sub>Benar: pusat $(-4,6)\to(4(1)-5,\ 4(5)+1)=(-1,21)$; jari-jari $6\to 24$, $24^2=576$</sub>
- D. $(x + 1)^2 + (y - 21)^2 = 36$  
  <sub>Salah: jari-jari tidak ikut diperbesar</sub>

**Pembahasan:** Pusat baru $(-1, 21)$ dan jari-jari $4\cdot 6=24$, sehingga persamaannya $(x+1)^2+(y-21)^2=576$.
**Acuan:** siswa — siswa hal.238 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b05-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: pencerminan terhadap garis y = mx*

Tentukan peta dari titik $(-14, 8)$ yang dicerminkan terhadap garis $y = 5x$.

- A. $(8, -14)$  
  <sub>Salah: mengira pencerminan terhadap $y=5x$ sama dengan terhadap $y=x$</sub>
- **B. $(16, 2)$** ✅  
  <sub>Benar: $d=\frac{a+mb}{m^2+1}=\frac{-14+40}{26}=1$; peta $(2d-a,\ 2md-b)=(16, 2)$</sub>
- C. $(14, 8)$  
  <sub>Salah: mengira pencerminan terhadap sumbu-$y$</sub>
- D. $(1, 5)$  
  <sub>Salah: berhenti di titik potong (kaki garis tegak lurus), bukan bayangan</sub>

**Pembahasan:** $d=1$; $(2\cdot 1+14,\ 2\cdot 5\cdot 1-8)=(16, 2)$.
**Acuan:** siswa — siswa hal.238 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b05-a-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: translasi lingkaran*

Tentukan peta dari lingkaran dengan persamaan $x^2 + y^2 = 16$ yang ditranslasikan dengan vektor $\begin{pmatrix} -5 \\ 7 \end{pmatrix}$.

- A. $(x + 5)^2 + (y - 7)^2 = 4$  
  <sub>Salah: jari-jari dihitung salah: $r^2=16$ dibagi $4$ menjadi $4$</sub>
- **B. $(x + 5)^2 + (y - 7)^2 = 16$** ✅  
  <sub>Benar: pusat $(0,0)\to(-5,7)$ dan jari-jari tetap $4$, sehingga persamaannya $(x+5)^2+(y-7)^2=16$</sub>
- C. $(x + 7)^2 + (y - 5)^2 = 16$  
  <sub>Salah: komponen vektor tertukar</sub>
- D. $(x - 5)^2 + (y + 7)^2 = 16$  
  <sub>Salah: tanda pergeseran dibalik ($x-a$ dan $y-b$ dipakai untuk vektor yang salah)</sub>

**Pembahasan:** Translasi tidak mengubah jari-jari ($r=4$); pusat baru $(-5, 7)$.
**Acuan:** siswa — siswa hal.226 Contoh 5.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b05-a-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: sifat dilatasi*

Sebuah segitiga siku-siku dibesarkan dengan dilatasi berpusat di titik tertentu dan faktor skala $3$. Pernyataan yang benar tentang segitiga hasil dilatasinya adalah ....

- A. panjang setiap sisi menjadi $3$ kali semula dan luasnya menjadi $3$ kali semula  
  <sub>Salah: luas dikira ikut dikali $k$, padahal dikali $k^2=9$</sub>
- B. panjang setiap sisi menjadi $\frac{1}{3}$ kali semula  
  <sub>Salah: faktor skala dibalik menjadi $\frac{1}{k}$</sub>
- **C. panjang setiap sisi menjadi $3$ kali semula dan bentuknya sebangun** ✅  
  <sub>Benar: dilatasi dengan $k=3$ mengalikan semua panjang dengan $3$ sehingga bangunnya sebangun, tidak kongruen</sub>
- D. panjang setiap sisi tetap dan bentuknya kongruen  
  <sub>Salah: mengira dilatasi mempertahankan kekongruenan seperti translasi</sub>

**Pembahasan:** Faktor skala $3$ memperbesar panjang sisi tiga kali dan luas sembilan kali; bentuk tetap sebangun.
**Acuan:** siswa — siswa hal.237 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b05-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: prapeta dari translasi*

Prapeta dari $(x + 6, y - 2)$ hasil translasi oleh vektor $\begin{pmatrix} 4 \\ -7 \end{pmatrix}$ adalah ....

- **A. $(x + 2, y + 5)$** ✅  
  <sub>Benar: prapeta = peta $-$ vektor $=(x+6-4,\ y-2+7)$</sub>
- B. $(x - 2, y - 5)$  
  <sub>Salah: tanda hasil dibalik</sub>
- C. $(x + 10, y - 9)$  
  <sub>Salah: peta dijumlahkan dengan vektor, bukan dikurangi</sub>
- D. $(x + 6, y - 2)$  
  <sub>Salah: tidak mengurangkan vektor translasi sama sekali</sub>

**Pembahasan:** $(x+6-4,\ y-2-(-7))=(x+2,\ y+5)$.
**Acuan:** siswa — siswa hal.238 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b05-a-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: rotasi titik terhadap titik asal*

Tentukan peta dari titik $P(8, -6)$ yang dirotasikan terhadap titik pusat $O$ sebesar $60^\circ$.

- A. $(4 - 3\sqrt{3},\ 4\sqrt{3} + 3)$  
  <sub>Salah: tanda $-y\sin\theta$ dan $y\cos\theta$ keliru (rotasi searah jarum jam)</sub>
- B. $(4\sqrt{3} + 3,\ 4 - 3\sqrt{3})$  
  <sub>Salah: nilai $\sin 60^\circ$ dan $\cos 60^\circ$ tertukar</sub>
- C. $(4 + 3\sqrt{3},\ 4\sqrt{3} + 3)$  
  <sub>Salah: lupa tanda negatif pada $y=-6$ ketika menghitung ordinat</sub>
- **D. $(4 + 3\sqrt{3},\ 4\sqrt{3} - 3)$** ✅  
  <sub>Benar: $x'=8\cdot\frac12+6\cdot\frac{\sqrt3}{2}$, $y'=8\cdot\frac{\sqrt3}{2}-6\cdot\frac12$</sub>

**Pembahasan:** $x'=x\cos60^\circ-y\sin60^\circ=4+3\sqrt3$ dan $y'=x\sin60^\circ+y\cos60^\circ=4\sqrt3-3$.
**Acuan:** siswa — siswa hal.229 Contoh 5.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b05-a-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: garis refleksi dari titik dan bayangan*

Titik $P(2, 9)$ dicerminkan terhadap garis $l$ dan bayangannya adalah $Q(8, 5)$. Persamaan garis $l$ adalah ....

- A. $2x + 3y - 31 = 0$  
  <sub>Salah: memilih garis $PQ$ sendiri, bukan garis sumbunya</sub>
- **B. $3x - 2y - 1 = 0$** ✅  
  <sub>Benar: $l$ adalah garis sumbu $PQ$: melalui titik tengah $(5,7)$ dan tegak lurus $PQ$ (gradien $PQ=-\frac23$)</sub>
- C. $3x - 2y + 12 = 0$  
  <sub>Salah: tegak lurus $PQ$ tetapi melalui titik $P$, bukan titik tengah</sub>
- D. $3x + 2y - 29 = 0$  
  <sub>Salah: melalui titik tengah tetapi gradiennya $-\frac{3}{2}$ (kebalikan tanpa tanda yang tepat)</sub>

**Pembahasan:** Titik tengah $(5,7)$; gradien $PQ=\frac{5-9}{8-2}=-\frac23$, gradien $l=\frac32$; $y-7=\frac32(x-5)$ memberi $3x-2y-1=0$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b05-a-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: mencari vektor translasi*

Titik $(-3, 5)$ ditranslasikan oleh suatu vektor sehingga petanya adalah $(4, -1)$. Vektor translasinya adalah ....

- A. $\begin{pmatrix} 1 \\ 4 \end{pmatrix}$  
  <sub>Salah: menjumlahkan koordinat titik awal dan akhir</sub>
- B. $\begin{pmatrix} -7 \\ 6 \end{pmatrix}$  
  <sub>Salah: mengurangkan peta dari prapeta (arah dibalik)</sub>
- C. $\begin{pmatrix} 7 \\ 6 \end{pmatrix}$  
  <sub>Salah: tanda komponen kedua keliru</sub>
- **D. $\begin{pmatrix} 7 \\ -6 \end{pmatrix}$** ✅  
  <sub>Benar: $(4-(-3),\ -1-5)=(7,-6)$</sub>

**Pembahasan:** Vektor translasi = peta $-$ prapeta = $(4+3,\ -1-5)=(7, -6)$.
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b05-a-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: rotasi sudut khusus*

Peta dari titik $(5, 8)$ yang dirotasikan terhadap titik pusat $O(0, 0)$ sebesar $270^\circ$ adalah ....

- A. $(-8, 5)$  
  <sub>Salah: memakai rotasi $90^\circ$, bukan $270^\circ$</sub>
- B. $(5, -8)$  
  <sub>Salah: hanya mengubah tanda ordinat (pencerminan terhadap sumbu-$x$)</sub>
- C. $(-5, -8)$  
  <sub>Salah: memakai rotasi $180^\circ$</sub>
- **D. $(8, -5)$** ✅  
  <sub>Benar: $\cos270^\circ=0$, $\sin270^\circ=-1$ sehingga $(x',y')=(y,-x)=(8,-5)$</sub>

**Pembahasan:** $x'=5\cdot0-8\cdot(-1)=8$ dan $y'=5\cdot(-1)+8\cdot0=-5$.
**Acuan:** siswa — siswa hal.229

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b05-a-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: mencari faktor skala dilatasi*

Pada dilatasi $D_{C,k}$ dengan $C(-2, 1)$, titik $A(4, 3)$ dipetakan ke $A'(16, 7)$. Faktor skala $k$ adalah ....

- A. $2$  
  <sub>Salah: membagi selisih $AA'$ dengan $CA$ (mengira $k-1$ sebagai faktor skala)</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: memakai kebalikan: $\frac{CA}{CA'}$</sub>
- C. $4$  
  <sub>Salah: membagi absis $A'$ dengan absis $A$ tanpa memperhatikan pusat $C$</sub>
- **D. $3$** ✅  
  <sub>Benar: $\overrightarrow{CA}=(6,2)$ dan $\overrightarrow{CA'}=(18,6)=3\,\overrightarrow{CA}$</sub>

**Pembahasan:** $\overrightarrow{CA}=(4+2,3-1)=(6,2)$, $\overrightarrow{CA'}=(16+2,7-1)=(18,6)$; $k=\frac{18}{6}=3$.
**Acuan:** siswa — siswa hal.234

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b05-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: rotasi terhadap pusat sembarang*

Peta dari titik $(5, 2)$ yang dirotasikan terhadap titik pusat $C(2, 1)$ sebesar $90^\circ$ berlawanan arah jarum jam adalah ....

- A. $(-1, 3)$  
  <sub>Salah: lupa menambahkan kembali koordinat pusat $(a,b)$</sub>
- B. $(3, -2)$  
  <sub>Salah: rotasi $-90^\circ$ (searah jarum jam), bukan $90^\circ$</sub>
- C. $(-2, 5)$  
  <sub>Salah: memakai pusat $O(0,0)$, bukan $C(2,1)$</sub>
- **D. $(1, 4)$** ✅  
  <sub>Benar: $x'=-(y-b)+a=1$, $y'=(x-a)+b=4$</sub>

**Pembahasan:** $x'=(5-2)\cdot0-(2-1)\cdot1+2=1$ dan $y'=(5-2)\cdot1+(2-1)\cdot0+1=4$.
**Acuan:** siswa — siswa hal.232

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b05-a-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: dilatasi berpusat O*

Titik $P(14, -8)$ didilatasikan dengan pusat $O(0, 0)$ dan faktor skala $\frac{1}{2}$. Koordinat peta $P'$ adalah ....

- A. $(-7, 4)$  
  <sub>Salah: kedua koordinat berubah tanda (mengira faktor positif membalik arah)</sub>
- B. $(7, 4)$  
  <sub>Salah: tanda ordinat berubah (mengira dilatasi mencerminkan terhadap sumbu-$x$)</sub>
- **C. $(7, -4)$** ✅  
  <sub>Benar: $(kx, ky)=(\frac12\cdot14,\ \frac12\cdot(-8))=(7,-4)$</sub>
- D. $(28, -16)$  
  <sub>Salah: memakai faktor skala $2$, kebalikan dari $\frac12$</sub>

**Pembahasan:** $D_{O,k}(x,y)=(kx,ky)=(7,-4)$.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b05-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: titik tetap pada pencerminan*

Pada pencerminan terhadap garis $2x - y + 3 = 0$, titik yang bayangannya adalah titik itu sendiri adalah ....

- **A. $(1, 5)$** ✅  
  <sub>Benar: titik di garis refleksi bayangannya dirinya sendiri; $2(1)-5+3=0$</sub>
- B. $(5, 1)$  
  <sub>Salah: menukar absis dan ordinat titik pada garis</sub>
- C. $(3, 6)$  
  <sub>Salah: titik tidak memenuhi persamaan garis (nilai $2x-y+3\neq0$)</sub>
- D. $(-3, 3)$  
  <sub>Salah: titik tidak memenuhi persamaan garis, hanya mengubah tanda absis</sub>

**Pembahasan:** Hanya titik yang memenuhi $2x-y+3=0$ yang tetap; $(1,5)$: $2-5+3=0$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b05-a-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: perbandingan luas pada dilatasi*

Sebuah lingkaran $L$ memiliki luas $20\pi$ cm$^2$. Lingkaran $L$ didilatasikan dengan faktor skala $3$ menjadi $L'$. Luas $L'$ adalah ....

- A. $540\pi$  
  <sub>Salah: luas dikalikan $k^3$</sub>
- **B. $180\pi$** ✅  
  <sub>Benar: luas $L:L'=1:k^2=1:9$ sehingga luas $L'=9\cdot20\pi=180\pi$</sub>
- C. $60\pi$  
  <sub>Salah: luas dikalikan $k$, bukan $k^2$</sub>
- D. $\frac{20\pi}{9}$  
  <sub>Salah: luas dibagi $k^2$ (rasio dibalik)</sub>

**Pembahasan:** Rasio luas $1:3^2$; $20\pi\cdot9=180\pi$ cm$^2$.
**Acuan:** siswa — siswa hal.237

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b05-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: pencerminan terhadap garis y = mx + c gradien negatif*

Tentukan bayangan dari titik $(-14, 14)$ yang dicerminkan terhadap garis $y = -4x + 9$.

- A. $(10, 11)$  
  <sub>Salah: memakai $c$ saja, bukan $2c$, pada ordinat</sub>
- B. $(-2, 17)$  
  <sub>Salah: berhenti di titik potong dengan garis tegak lurus (titik tengah), belum dicari bayangannya</sub>
- C. $(10, 2)$  
  <sub>Salah: lupa suku $2c$ pada ordinat $2md+2c-b$</sub>
- **D. $(10, 20)$** ✅  
  <sub>Benar: $a=-14$, $b=14$, $m=-4$, $c=9$; $d=\frac{a+m(b-c)}{m^2+1}=\frac{-14-20}{17}=-2$; bayangan $(2d-a,\,2md+2c-b)=(10, 20)$</sub>

**Pembahasan:** $d=-2$, bayangan $(2(-2)+14,\ 2(-4)(-2)+18-14)=(10, 20)$.
**Acuan:** siswa — siswa hal.219 Contoh 5.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b05-a-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: pencerminan terhadap garis ax + by + c = 0 (cerita)*

Pada denah koordinat sebuah taman, sebuah lampu berdiri di titik $(-9, -7)$. Sebuah cermin datar dipasang lurus sepanjang garis $3x + 4y - 20 = 0$. Koordinat bayangan lampu pada cermin tersebut adalah ....

- **A. $(9, 17)$** ✅  
  <sub>Benar: $3(-9)+4(-7)-20=-75$, $a^2+b^2=25$, nilainya $-3$; bayangan $(x_0-2a(-3),\ y_0-2b(-3))=(9, 17)$</sub>
- B. $(-27, -31)$  
  <sub>Salah: tanda salah: memakai $x_0+2a\cdot t$ bukan $x_0-2a\cdot t$</sub>
- C. $(9, 7)$  
  <sub>Salah: mengira bayangan adalah titik yang berlawanan tanda terhadap titik asal</sub>
- D. $(0, 5)$  
  <sub>Salah: hanya menghitung kaki garis tegak lurus (titik tengah), bukan bayangan</sub>

**Pembahasan:** $\frac{3(-9)+4(-7)-20}{25}=-3$; bayangan $(-9+18,\ -7+24)=(9, 17)$.
**Acuan:** siswa — siswa hal.224 Contoh 5.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b05-a-medium-bt01-003
*variasi (angka) | C3 | 3 langkah | jenis: pencerminan titik berkoordinat pecahan terhadap garis y = mx*

Tentukan bayangan dari titik $\left(-8, \frac{7}{2}\right)$ yang dicerminkan terhadap garis $y = -2x$.

- **A. $(2, \frac{17}{2})$** ✅  
  <sub>Benar: $d=\frac{a+mb}{m^2+1}=\frac{-8-7}{5}=-3$; bayangan $(2d-a,\ 2md-b)=(-6+8,\ 12-\frac72)=(2, \frac{17}{2})$</sub>
- B. $(-3, 6)$  
  <sub>Salah: berhenti di titik potong (kaki garis tegak lurus), bukan bayangan</sub>
- C. $(-14, \frac{17}{2})$  
  <sub>Salah: tanda salah pada absis: memakai $2d+a$ bukan $2d-a$</sub>
- D. $(2, \frac{31}{2})$  
  <sub>Salah: tanda salah pada ordinat: memakai $2md+b$ bukan $2md-b$</sub>

**Pembahasan:** $d=-3$; $(2(-3)+8,\ 2(-2)(-3)-\frac72)=(2, \frac{17}{2})$.
**Acuan:** siswa — siswa hal.238 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b05-a-medium-bt01-004
*variasi (angka) | C3 | 3 langkah | jenis: rotasi garis terhadap titik asal (sudut 270 derajat)*

Tentukan peta dari garis $5x + 4y - 7 = 0$ yang ditransformasi oleh rotasi $270^\circ$ terhadap titik asal $(0, 0)$.

- A. $5x + 4y + 7 = 0$  
  <sub>Salah: memakai rotasi $180^\circ$, yakni $(x,y)\to(-x,-y)$</sub>
- **B. $4x - 5y - 7 = 0$** ✅  
  <sub>Benar: $(x,y)\to(y,-x)$ sehingga $x=-y'$ dan $y=x'$; substitusi: $-5y'+4x'-7=0$</sub>
- C. $-4x + 5y - 7 = 0$  
  <sub>Salah: memakai rotasi $90^\circ$ ($x'=-y$, $y'=x$), bukan $270^\circ$</sub>
- D. $4x + 5y - 7 = 0$  
  <sub>Salah: hanya menukar koefisien tanpa memperhatikan tanda hasil rotasi</sub>

**Pembahasan:** Rotasi $270^\circ$: $x'=y$, $y'=-x$, jadi $x=-y'$, $y=x'$. Substitusi: $5(-y')+4x'-7=0$, yaitu $4x'-5y'-7=0$.
**Acuan:** pretest — kelas11_tl-b05-p0238-latihan-a-4d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b05-a-medium-bt01-005
*variasi (angka) | C4 | 3 langkah | jenis: dilatasi lingkaran dengan faktor skala negatif*

Peta dari lingkaran $L: (x - 5)^2 + (y + 4)^2 = 9$ yang didilatasikan dengan titik pusat $C(-3, 6)$ dan faktor skala $-2$ adalah ....

- A. $(x + 10)^2 + (y - 8)^2 = 36$  
  <sub>Salah: pusat lingkaran hanya dikalikan $k$ tanpa memperhatikan pusat dilatasi $C$</sub>
- B. $(x + 19)^2 + (y - 26)^2 = 18$  
  <sub>Salah: mengalikan $r^2$ dengan $|k|$, bukan $k^2$</sub>
- **C. $(x + 19)^2 + (y - 26)^2 = 36$** ✅  
  <sub>Benar: pusat baru $(-3+(-2)(8),\ 6+(-2)(-10))=(-19, 26)$; jari-jari $|-2|\cdot3=6$, $r^2=36$</sub>
- D. $(x - 13)^2 + (y + 14)^2 = 36$  
  <sub>Salah: mengabaikan tanda negatif pada $k$ (memakai $k=2$) sehingga arah pusat peta terbalik</sub>

**Pembahasan:** Pusat $(5,-4)\to(-19, 26)$, jari-jari $6$; persamaan $(x+19)^2+(y-26)^2=36$.
**Acuan:** siswa — siswa hal.238 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b05-a-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: rotasi titik terhadap titik asal sudut tumpul*

Tentukan peta dari titik $P(9, -5)$ yang dirotasikan terhadap titik pusat $O(0, 0)$ sebesar $150^\circ$.

- A. $(\frac{5 + 9\sqrt{3}}{2}, \frac{9 - 5\sqrt{3}}{2})$  
  <sub>Salah: memakai nilai sudut acuan $30^\circ$ dan lupa $150^\circ$ di kuadran II</sub>
- B. $(\frac{-5 - 9\sqrt{3}}{2}, \frac{-9 + 5\sqrt{3}}{2})$  
  <sub>Salah: memutar searah jarum jam ($-150^\circ$), bukan berlawanan arah jarum jam</sub>
- C. $(\frac{9 - 5\sqrt{3}}{2}, \frac{-5 - 9\sqrt{3}}{2})$  
  <sub>Salah: nilai $\sin150^\circ$ dan $\cos150^\circ$ tertukar</sub>
- **D. $(\frac{5 - 9\sqrt{3}}{2}, \frac{9 + 5\sqrt{3}}{2})$** ✅  
  <sub>Benar: $\cos150^\circ=-\frac{\sqrt3}{2}$, $\sin150^\circ=\frac12$; $x'=9\cos150^\circ+5\sin150^\circ$, $y'=9\sin150^\circ-5\cos150^\circ$</sub>

**Pembahasan:** $x'=9(-\frac{\sqrt3}{2})-(-5)(\frac12)=\frac{5-9\sqrt3}{2}$ dan $y'=9(\frac12)+(-5)(-\frac{\sqrt3}{2})=\frac{9+5\sqrt3}{2}$.
**Acuan:** siswa — siswa hal.229 Contoh 5.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b05-a-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: dilatasi titik dengan faktor skala pecahan negatif*

Diberikan titik $C(-6, 4)$, titik $A(6, -8)$, dan $k = -\frac{1}{2}$. Tentukan $D_{C,k}(A)$.

- **A. $(-12, 10)$** ✅  
  <sub>Benar: $(k(x-a)+a,\ k(y-b)+b)=(-\frac12\cdot12-6,\ -\frac12\cdot(-12)+4)=(-12, 10)$</sub>
- B. $(-3, 4)$  
  <sub>Salah: memakai pusat $O(0,0)$, hanya mengalikan koordinat $A$ dengan $k$</sub>
- C. $(0, -2)$  
  <sub>Salah: mengabaikan tanda negatif pada $k$ (memakai $k=\frac12$)</sub>
- D. $(-6, 6)$  
  <sub>Salah: lupa menambahkan kembali koordinat pusat $C$</sub>

**Pembahasan:** $A'=(-\frac12(6+6)-6,\ -\frac12(-8-4)+4)=(-12, 10)$.
**Acuan:** siswa — siswa hal.235 Contoh 5.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b05-a-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: translasi lingkaran lalu bentuk umum*

Tentukan peta dari lingkaran dengan persamaan $x^2 + y^2 = 49$ yang ditranslasikan dengan vektor $\begin{pmatrix} -3 \\ 5 \end{pmatrix}$. Jika persamaan petanya ditulis $x^2 + y^2 + Ax + By + C = 0$, maka nilai $A + B + C$ adalah ....

- A. $79$  
  <sub>Salah: lupa mengurangi $49$: konstanta dijumlahkan $9+25+49=83$</sub>
- B. $-11$  
  <sub>Salah: tanda vektor dibalik: $(x-3)^2+(y+5)^2=49$ memberi $A=-6$, $B=10$, $C=-15$</sub>
- **C. $-19$** ✅  
  <sub>Benar: peta: $(x+3)^2+(y-5)^2=49$ atau $x^2+y^2+6x-10y-15=0$ sehingga $A+B+C=6-10-15=-19$</sub>
- D. $30$  
  <sub>Salah: konstanta $C=9+25=34$ tanpa mengurangi $r^2=49$</sub>

**Pembahasan:** Pusat $(0,0)\to(-3,5)$, $r=7$. $(x+3)^2+(y-5)^2=49\Rightarrow x^2+y^2+6x-10y-15=0$.
**Acuan:** siswa — siswa hal.226 Contoh 5.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b05-a-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: mencari konstanta garis refleksi dari titik dan bayangan*

Titik $P(4, -1)$ dicerminkan terhadap garis $y = 3x + c$ dan bayangannya adalah $Q(-2, 1)$. Nilai $c$ adalah ....

- A. $-13$  
  <sub>Salah: garis dianggap melalui $P$: $-1=3(4)+c$</sub>
- **B. $-3$** ✅  
  <sub>Benar: titik tengah $PQ$ adalah $(1, 0)$ dan terletak pada garis refleksi: $0=3(1)+c$ sehingga $c=-3$ (gradien $PQ=-\frac13$ tegak lurus gradien $3$)</sub>
- C. $3$  
  <sub>Salah: kesalahan tanda: $0=3(1)-c$</sub>
- D. $7$  
  <sub>Salah: garis dianggap melalui $Q$: $1=3(-2)+c$</sub>

**Pembahasan:** Garis refleksi adalah garis sumbu $PQ$ sehingga melalui titik tengah $(1,0)$; $c=0-3\cdot1=-3$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b05-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: jarak titik ke bayangannya pada pencerminan*

Titik $P(12, 6)$ dicerminkan terhadap garis $3x + 4y - 10 = 0$ menghasilkan bayangan $P'$. Jarak antara $P$ dan $P'$ adalah ... satuan.

- A. $10$  
  <sub>Salah: menghitung jarak $P$ ke garis saja, belum dikalikan dua</sub>
- B. $50$  
  <sub>Salah: memakai nilai $3x+4y-10$ tanpa membagi dengan $\sqrt{a^2+b^2}$ dan tanpa menghitung bayangan</sub>
- **C. $20$** ✅  
  <sub>Benar: $3(12)+4(6)-10=50$, $\frac{50}{25}=2$; $P'=(12-12,\ 6-16)=(0,-10)$; $PP'=\sqrt{12^2+16^2}=20$</sub>
- D. $28$  
  <sub>Salah: menjumlahkan selisih absis dan ordinat ($12+16$) bukan memakai rumus jarak</sub>

**Pembahasan:** $P'=(0,-10)$; $PP'=\sqrt{(12-0)^2+(6+10)^2}=\sqrt{400}=20$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b05-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: mencari prapeta dari bayangan pencerminan*

Bayangan titik $P$ yang dicerminkan terhadap garis $x - 2y + 3 = 0$ adalah $(11, -3)$. Koordinat titik $P$ adalah ....

- A. $(19, -19)$  
  <sub>Salah: tanda salah: memakai $+2at$ dan $+2bt$ bukan $-2at$ dan $-2bt$</sub>
- B. $(7, 5)$  
  <sub>Salah: hanya menghitung titik tengah (kaki garis tegak lurus), bukan prapeta</sub>
- C. $(-3, 11)$  
  <sub>Salah: mengira pencerminan terhadap garis $y=x$ (menukar koordinat)</sub>
- **D. $(3, 13)$** ✅  
  <sub>Benar: mencerminkan $(11,-3)$ terhadap garis yang sama memberi prapeta: $\frac{11+6+3}{5}=4$, $P=(11-2\cdot4,\ -3+4\cdot4)=(3, 13)$</sub>

**Pembahasan:** Nilai $11-2(-3)+3=20$, dibagi $a^2+b^2=5$ diperoleh $4$; $P=(11-2\cdot1\cdot4,\ -3-2\cdot(-2)\cdot4)=(3, 13)$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b05-a-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: komposisi translasi lalu rotasi*

Titik $A(4, -3)$ ditranslasikan oleh vektor $\begin{pmatrix} -2 \\ 7 \end{pmatrix}$, kemudian hasilnya dirotasikan sebesar $90^\circ$ berlawanan arah jarum jam terhadap titik pusat $O(0, 0)$. Koordinat peta akhirnya adalah ....

- A. $(2, 4)$  
  <sub>Salah: hanya mengerjakan translasi dan lupa rotasi</sub>
- B. $(4, -2)$  
  <sub>Salah: memutar searah jarum jam ($-90^\circ$): $(y,-x)$</sub>
- C. $(1, 11)$  
  <sub>Salah: urutan terbalik: dirotasi dahulu $(3, 4)$ lalu ditranslasi</sub>
- **D. $(-4, 2)$** ✅  
  <sub>Benar: translasi: $(4-2,\ -3+7)=(2, 4)$; rotasi $90^\circ$: $(x,y)\to(-y,x)$ sehingga $(-4, 2)$</sub>

**Pembahasan:** $A'=(2,4)$; $A''=(-4, 2)$.
**Acuan:** siswa — siswa hal.229

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b05-a-medium-bt01-013
*orisinal | C4 | 4 langkah | jenis: dua dilatasi berurutan*

Titik $A(4, -2)$ didilatasikan dengan pusat $O(0, 0)$ dan faktor skala $-3$, kemudian hasilnya didilatasikan dengan pusat $C(2, -4)$ dan faktor skala $\frac{1}{2}$. Koordinat peta akhirnya adalah ....

- A. $(-9, 9)$  
  <sub>Salah: urutan dilatasi dibalik</sub>
- **B. $(-5, 1)$** ✅  
  <sub>Benar: dilatasi pertama: $(-12, 6)$; kedua: $(2+\frac12(-14),\ -4+\frac12(10))=(-5, 1)$</sub>
- C. $(-6, 3)$  
  <sub>Salah: dilatasi kedua dianggap berpusat di $O$, bukan di $C(2,-4)$</sub>
- D. $(-12, 6)$  
  <sub>Salah: hanya mengerjakan dilatasi pertama</sub>

**Pembahasan:** $A'=(-12,6)$; $A''=(k(x-a)+a,\ k(y-b)+b)=(-5, 1)$.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b05-a-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: mencari pusat dilatasi*

Dilatasi dengan faktor skala $-2$ memetakan titik $A(5, 7)$ ke $A'(-7, -23)$. Titik pusat dilatasi tersebut adalah ....

- A. $(-1, -8)$  
  <sub>Salah: mengira pusat adalah titik tengah $A$ dan $A'$</sub>
- B. $(-3, 9)$  
  <sub>Salah: penyebut salah: $1+k$ bukan $1-k$</sub>
- C. $(3, -9)$  
  <sub>Salah: lupa membagi dengan $1-k$</sub>
- **D. $(1, -3)$** ✅  
  <sub>Benar: $A'=C+k(A-C)$ sehingga $C=\frac{A'-kA}{1-k}=\frac{(-7+10,\ -23+14)}{3}=(1,-3)$</sub>

**Pembahasan:** $-7=C_x-2(5-C_x)\Rightarrow 3C_x=3$; $-23=C_y-2(7-C_y)\Rightarrow 3C_y=-9$; $C=(1,-3)$.
**Acuan:** siswa — siswa hal.234

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b05-a-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: rotasi searah jarum jam terhadap pusat sembarang*

Titik $P(7, 1)$ dirotasikan terhadap titik pusat $C(3, -2)$ sebesar $-90^\circ$ (searah jarum jam). Peta dari $P$ adalah ....

- A. $(0, 2)$  
  <sub>Salah: memakai $+90^\circ$ (berlawanan arah jarum jam)</sub>
- B. $(3, -4)$  
  <sub>Salah: lupa menambahkan kembali koordinat pusat $C$</sub>
- **C. $(6, -6)$** ✅  
  <sub>Benar: $\cos(-90^\circ)=0$, $\sin(-90^\circ)=-1$: $x'=(y-b)+a=3+3=6$, $y'=-(x-a)+b=-4-2=-6$</sub>
- D. $(1, -7)$  
  <sub>Salah: memakai pusat $O(0,0)$ bukan $C(3,-2)$</sub>

**Pembahasan:** $(x-a, y-b)=(4,3)$; rotasi $-90^\circ$ memberi $(3,-4)$; ditambah $C$: $(6,-6)$.
**Acuan:** siswa — siswa hal.232

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b05-a-medium-bt01-016
*orisinal | C3 | 2 langkah | jenis: mencari pusat rotasi 180 derajat*

Rotasi sebesar $180^\circ$ dengan titik pusat $C$ memetakan titik $P(9, -4)$ ke $P'(-3, 6)$. Koordinat $C$ adalah ....

- **A. $(3, 1)$** ✅  
  <sub>Benar: $CP=CP'$ dan sudut $P C P'=180^\circ$ sehingga $C$ titik tengah $PP'$: $(\frac{9-3}{2},\ \frac{-4+6}{2})=(3,1)$</sub>
- B. $(6, 2)$  
  <sub>Salah: menjumlahkan koordinat tanpa membagi dua</sub>
- C. $(-12, 10)$  
  <sub>Salah: memakai vektor $PP'$ sebagai pusat</sub>
- D. $(6, -5)$  
  <sub>Salah: membagi selisih koordinat, bukan jumlah</sub>

**Pembahasan:** $C=\left(\frac{x_P+x_{P'}}{2},\ \frac{y_P+y_{P'}}{2}\right)=(3, 1)$.
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b05-a-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: translasi sebuah garis*

Garis $y = -3x + 5$ ditranslasikan oleh vektor $\begin{pmatrix} 2 \\ -7 \end{pmatrix}$. Persamaan garis petanya adalah ....

- A. $3x + y - 11 = 0$  
  <sub>Salah: hanya menggeser $x$ dan lupa menggeser $y$</sub>
- **B. $3x + y - 4 = 0$** ✅  
  <sub>Benar: $x=x'-2$, $y=y'+7$; substitusi: $y'+7=-3(x'-2)+5$ sehingga $3x'+y'-4=0$</sub>
- C. $3x + y - 6 = 0$  
  <sub>Salah: tanda vektor dibalik: $x=x'+2$, $y=y'-7$</sub>
- D. $3x + y + 2 = 0$  
  <sub>Salah: hanya menambahkan komponen kedua vektor ke konstanta $5-7$</sub>

**Pembahasan:** Peta: $y+7=-3(x-2)+5\Rightarrow y=-3x+4$, yaitu $3x+y-4=0$.
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b05-a-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: mencari parameter titik yang ditranslasikan*

Titik $(p, 4)$ ditranslasikan oleh vektor $\begin{pmatrix} 3 \\ -5 \end{pmatrix}$ sehingga petanya terletak pada garis $x + 2y = 10$. Nilai $p$ adalah ....

- **A. $9$** ✅  
  <sub>Benar: peta $(p+3,\ -1)$; $p+3+2(-1)=10$ sehingga $p=9$</sub>
- B. $-11$  
  <sub>Salah: ordinat peta salah dihitung sebagai $4+5=9$</sub>
- C. $-1$  
  <sub>Salah: hanya menggeser absis dan lupa menggeser ordinat</sub>
- D. $-5$  
  <sub>Salah: vektor dikurangkan, bukan ditambahkan, pada absis dan ordinat</sub>

**Pembahasan:** Peta $(p+3, 4-5)=(p+3,-1)$. Substitusi: $p+3-2=10$, $p=9$.
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b05-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: luas bangun hasil dilatasi*

Segitiga $ABC$ dengan $A(1, 1)$, $B(7, 1)$, dan $C(1, 5)$ didilatasikan dengan titik pusat $P(3, -2)$ dan faktor skala $-2$. Luas segitiga hasil dilatasi adalah ... satuan luas.

- A. $12$  
  <sub>Salah: mengira dilatasi mempertahankan luas</sub>
- B. $24$  
  <sub>Salah: luas dikalikan $|k|$, bukan $k^2$</sub>
- **C. $48$** ✅  
  <sub>Benar: luas awal $\frac12\cdot6\cdot4=12$; luas peta $=k^2\cdot12=4\cdot12=48$</sub>
- D. $96$  
  <sub>Salah: luas dikalikan $k^2$ lalu dikali $2$ lagi (alas kali tinggi tanpa $\frac12$)</sub>

**Pembahasan:** Siku-siku di $A$ dengan alas $6$ dan tinggi $4$: luas $12$; $L'=(-2)^2\cdot12=48$.
**Acuan:** siswa — siswa hal.237

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b05-a-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: rotasi lingkaran terhadap titik asal*

Lingkaran $L: (x - 3)^2 + (y + 5)^2 = 49$ dirotasikan sebesar $270^\circ$ berlawanan arah jarum jam terhadap titik asal $O(0, 0)$. Persamaan peta lingkaran $L$ adalah ....

- A. $(x + 5)^2 + (y + 3)^2 = 7$  
  <sub>Salah: mengira ruas kanan menjadi jari-jari, bukan $r^2=49$</sub>
- **B. $(x + 5)^2 + (y + 3)^2 = 49$** ✅  
  <sub>Benar: pusat $(3,-5)\to(y,-x)=(-5,-3)$, rotasi tidak mengubah jari-jari ($r^2=49$)</sub>
- C. $(x - 5)^2 + (y - 3)^2 = 49$  
  <sub>Salah: memakai rotasi $90^\circ$, bukan $270^\circ$</sub>
- D. $(x + 3)^2 + (y - 5)^2 = 49$  
  <sub>Salah: memakai rotasi $180^\circ$</sub>

**Pembahasan:** Rotasi $270^\circ$: $(x,y)\to(y,-x)$; pusat baru $(-5,-3)$ dan $r^2=49$.
**Acuan:** siswa — siswa hal.229

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b05-a-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: pasangan transformasi yang dapat dipertukarkan*

Dua transformasi $S$ dan $T$ disebut dapat dipertukarkan jika $S(T(P)) = T(S(P))$ untuk setiap titik $P$ pada bidang Kartesius. Pasangan transformasi berikut yang dapat dipertukarkan adalah ....

- A. Translasi oleh vektor $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$ dan rotasi $90^\circ$ terhadap titik pusat $O(0, 0)$  
  <sub>Salah: mengira translasi tidak terpengaruh urutan; padahal rotasi ikut memutar vektor pergeseran</sub>
- **B. Dilatasi berpusat di $O(0, 0)$ dengan faktor skala $3$ dan rotasi $90^\circ$ terhadap titik pusat $O(0, 0)$** ✅  
  <sub>Benar: dilatasi berpusat di titik asal hanya memperbesar jarak dari $O$ dan rotasi berpusat di $O$ hanya memutar, sehingga $(x, y) \to (-3y, 3x)$ untuk kedua urutan</sub>
- C. Translasi oleh vektor $\begin{pmatrix} 2 \\ 0 \end{pmatrix}$ dan dilatasi berpusat di $O(0, 0)$ dengan faktor skala $2$  
  <sub>Salah: mengira translasi dan dilatasi sama-sama tidak mengubah arah sehingga boleh ditukar; padahal dilatasi ikut melipatkan vektor pergeseran</sub>
- D. Pencerminan terhadap garis $y = x$ dan pencerminan terhadap sumbu-$x$  
  <sub>Salah: mengira dua pencerminan selalu boleh ditukar; padahal hasilnya $(y, -x)$ berbeda dengan $(-y, x)$</sub>

**Pembahasan:** Dilatasi $D_{O,3}$ dan rotasi $\rho_{O,90}$: $(x,y) \to (3x, 3y) \to (-3y, 3x)$ dan $(x,y) \to (-y, x) \to (-3y, 3x)$, sama. Pasangan lain punya contoh penyangkal, mis. translasi $(3,-2)$ dan rotasi $90^\circ$ pada titik $(0,0)$ menghasilkan $(2,3)$ atau $(3,-2)$.
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b05-a-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: menemukan langkah keliru pada rotasi berpusat sembarang*

Dito diminta menentukan peta titik $P(1, 5)$ yang dirotasikan $270^\circ$ berlawanan arah jarum jam terhadap titik pusat $C(-3, 2)$. Langkah Dito: (1) menggeser titik: $P - C = (4, 3)$; (2) memutar $(4, 3)$ sebesar $270^\circ$ terhadap $O(0, 0)$ sehingga diperoleh $(3, -4)$; (3) menulis hasil akhir $P' = (3, -4)$. Kesalahan Dito terdapat pada ....

- A. langkah (3): hasil akhir seharusnya dikurangi $C$, yaitu $(3, -4) - (-3, 2)$  
  <sub>Salah: salah arah menggeser kembali (mengurangi, bukan menambah $C$)</sub>
- B. langkah (2): rotasi $270^\circ$ memetakan $(x, y)$ ke $(-y, x)$ sehingga hasilnya $(-3, 4)$  
  <sub>Salah: tertukar dengan rumus rotasi $90^\circ$</sub>
- C. langkah (1): seharusnya titik digeser dengan $P + C$ karena pusat dipindahkan ke titik asal  
  <sub>Salah: mengira menggeser pusat ke titik asal berarti menambah $C$</sub>
- **D. langkah (3): hasil rotasi terhadap $O$ belum digeser kembali dengan menambahkan $C$** ✅  
  <sub>Benar: langkah (1) dan (2) benar; hasil akhir wajib ditambah $C$ lagi: $(3,-4) + (-3,2) = (0,-2)$</sub>

**Pembahasan:** Rotasi berpusat $C$: geser $P - C = (4,3)$, putar $270^\circ$ terhadap $O$: $(y,-x) = (3,-4)$, lalu geser balik $+C$: $(0,-2)$. Dito berhenti sebelum langkah terakhir.
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b05-a-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: transformasi tunggal pengganti dua pencerminan sejajar*

Sebuah titik dicerminkan terhadap garis $x = 2$, kemudian bayangannya dicerminkan terhadap garis $x = 7$. Komposisi dua pencerminan tersebut ekuivalen dengan satu transformasi tunggal berupa ....

- A. rotasi $180^\circ$ terhadap titik $\left(\frac{9}{2}, 0\right)$  
  <sub>Salah: mengira dua pencerminan selalu menghasilkan rotasi, padahal garis sejajar</sub>
- **B. translasi oleh vektor $\begin{pmatrix} 10 \\ 0 \end{pmatrix}$** ✅  
  <sub>Benar: $(x, y) \to (4 - x, y) \to (14 - (4 - x), y) = (x + 10, y)$</sub>
- C. translasi oleh vektor $\begin{pmatrix} -10 \\ 0 \end{pmatrix}$  
  <sub>Salah: membalik urutan pencerminan sehingga arah pergeseran terbalik</sub>
- D. translasi oleh vektor $\begin{pmatrix} 5 \\ 0 \end{pmatrix}$  
  <sub>Salah: mengira pergeseran hanya sebesar jarak kedua garis</sub>

**Pembahasan:** Pencerminan terhadap $x = a$: $(x,y) \to (2a - x, y)$. Pertama $(4-x, y)$, kedua $(14 - 4 + x, y) = (x+10, y)$, yaitu translasi sebesar $2(7-2) = 10$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b05-a-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: transformasi tunggal pengganti dua pencerminan berpotongan*

Titik $(x, y)$ dicerminkan terhadap garis $y = -x$, kemudian bayangannya dicerminkan terhadap sumbu-$y$. Komposisi tersebut ekuivalen dengan ....

- A. rotasi $90^\circ$ berlawanan arah jarum jam terhadap titik pusat $O(0, 0)$  
  <sub>Salah: membalik urutan pencerminan sehingga arah rotasi terbalik</sub>
- B. rotasi $180^\circ$ terhadap titik pusat $O(0, 0)$  
  <sub>Salah: mengira dua pencerminan yang saling tegak lurus; padahal kedua garis membentuk sudut $45^\circ$</sub>
- **C. rotasi $270^\circ$ berlawanan arah jarum jam terhadap titik pusat $O(0, 0)$** ✅  
  <sub>Benar: $(x, y) \to (-y, -x) \to (y, -x)$, yaitu rotasi $270^\circ$ terhadap $O$</sub>
- D. pencerminan terhadap garis $y = x$  
  <sub>Salah: mengira dua pencerminan menghasilkan satu pencerminan lain</sub>

**Pembahasan:** Pencerminan terhadap $y=-x$: $(x,y)\to(-y,-x)$. Pencerminan terhadap sumbu-$y$: $(a,b)\to(-a,b)$ sehingga $(y,-x)$. Rumus Sifat 5.2 untuk $270^\circ$: $(x\cos 270^\circ - y\sin 270^\circ, x\sin 270^\circ + y\cos 270^\circ) = (y, -x)$.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b05-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: transformasi tunggal pengganti dua dilatasi berpusat beda*

Titik didilatasikan dengan pusat $A(1, -2)$ dan faktor skala $3$, kemudian bayangannya didilatasikan dengan pusat $B(10, 4)$ dan faktor skala $\frac{1}{3}$. Komposisi tersebut ekuivalen dengan satu transformasi tunggal berupa ....

- **A. translasi oleh vektor $\begin{pmatrix} 6 \\ 4 \end{pmatrix}$** ✅  
  <sub>Benar: $x \to 3x - 2A \to \frac{1}{3}(3x - 2A - B) + B = x + \frac{2}{3}(B - A)$, sehingga vektor translasinya $\frac{2}{3}(9, 6) = (6, 4)$</sub>
- B. translasi oleh vektor $\begin{pmatrix} -6 \\ -4 \end{pmatrix}$  
  <sub>Salah: arah vektor terbalik ($A - B$ bukan $B - A$)</sub>
- C. translasi oleh vektor $\begin{pmatrix} 18 \\ 12 \end{pmatrix}$  
  <sub>Salah: membalik urutan dilatasi</sub>
- D. translasi oleh vektor $\begin{pmatrix} 9 \\ 6 \end{pmatrix}$  
  <sub>Salah: menganggap vektor translasi sama dengan $\overrightarrow{AB}$</sub>

**Pembahasan:** Faktor skala total $3 \cdot \frac13 = 1$, sehingga bentuknya translasi. Dengan $D_{C,k}(P) = C + k(P - C)$: $P_1 = A + 3(P-A)$, $P_2 = B + \frac13(P_1 - B) = P + \frac23(B-A)$.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b05-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi sifat luas dan orientasi hasil komposisi*

Segitiga $ABC$ dengan $A(1, 1)$, $B(5, 1)$, dan $C(1, 4)$ (urutan $A \to B \to C$ berlawanan arah jarum jam) ditransformasi berturut-turut oleh pencerminan terhadap garis $y = x + 2$, dilatasi dengan pusat $(1, 1)$ dan faktor skala $-2$, lalu rotasi $90^\circ$ terhadap $O(0, 0)$, menghasilkan segitiga $A'B'C'$. Pernyataan yang benar adalah ....

- **A. luas $A'B'C'$ sama dengan $4$ kali luas $ABC$, dan urutan $A' \to B' \to C'$ searah jarum jam** ✅  
  <sub>Benar: dilatasi faktor $-2$ melipatkan luas $4$ kali, pencerminan membalik orientasi satu kali, dilatasi negatif dan rotasi tidak membalik orientasi</sub>
- B. luas $A'B'C'$ sama dengan luas $ABC$, dan urutan $A' \to B' \to C'$ searah jarum jam  
  <sub>Salah: mengira semua transformasi mempertahankan luas</sub>
- C. luas $A'B'C'$ sama dengan $2$ kali luas $ABC$, dan urutan $A' \to B' \to C'$ searah jarum jam  
  <sub>Salah: mengira luas ikut berubah sebesar $|k|$ dan bukan $k^2$</sub>
- D. luas $A'B'C'$ sama dengan $4$ kali luas $ABC$, dan urutan $A' \to B' \to C'$ berlawanan arah jarum jam  
  <sub>Salah: mengira dilatasi negatif atau rotasi mengubah orientasi dan melupakan pencerminan yang membaliknya</sub>

**Pembahasan:** Luas $ABC$ = 6. Hasil perhitungan koordinat: luas $A'B'C'$ = 24 dan tanda luas bertanda berubah dari positif ke negatif, yaitu orientasi berbalik (searah jarum jam).
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b05-a-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: invarian jarak pada komposisi transformasi*

Titik $A(1, 2)$ dan $B(13, 7)$ ditransformasi berturut-turut oleh pencerminan terhadap garis $2x - y - 1 = 0$, dilatasi dengan pusat $(2, 3)$ dan faktor skala $-3$, translasi oleh $\begin{pmatrix} 4 \\ -5 \end{pmatrix}$, rotasi $90^\circ$ terhadap $O(0, 0)$, dan dilatasi dengan pusat $(-1, 1)$ dan faktor skala $\frac{1}{2}$, menghasilkan $A'$ dan $B'$. Panjang $A'B'$ adalah ....

- A. $39$  
  <sub>Salah: lupa dilatasi terakhir (hanya faktor $3$)</sub>
- B. $\frac{13}{2}$  
  <sub>Salah: lupa dilatasi pertama dan hanya memakai faktor $\frac{1}{2}$</sub>
- C. $\frac{13}{6}$  
  <sub>Salah: membagi dengan faktor skala ($3$ lalu $2$) bukan mengalikan</sub>
- **D. $\frac{39}{2}$** ✅  
  <sub>Benar: $AB = 13$; hanya dua dilatasi yang mengubah jarak, faktor totalnya $|-3| \cdot \frac{1}{2} = \frac{3}{2}$</sub>

**Pembahasan:** $AB = \sqrt{12^2 + 5^2} = 13$. Pencerminan, translasi, dan rotasi tidak mengubah jarak. Panjang akhir $= 13 \cdot 3 \cdot \frac12 = \frac{39}{2}$.
**Acuan:** siswa — siswa hal.235

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b05-a-hard-bt01-008
*orisinal | C5 | 3 langkah | jenis: menemukan kesalahan urutan komposisi*

Soal: titik $P(3, -2)$ dicerminkan terhadap garis $y = x$, kemudian hasilnya ditranslasikan oleh $\begin{pmatrix} 1 \\ 4 \end{pmatrix}$. Sinta mengerjakan: $(3, -2) + (1, 4) = (4, 2)$, lalu dicerminkan terhadap $y = x$ menjadi $(2, 4)$. Pernyataan yang benar tentang pekerjaan Sinta adalah ....

- A. urutan transformasinya terbalik, dan hasil yang benar adalah $(-3, -1)$  
  <sub>Salah: mengurangkan vektor translasi, bukan menambahkan</sub>
- B. urutan transformasinya terbalik, dan hasil yang benar adalah $(3, 1)$  
  <sub>Salah: mencerminkan terhadap $y = -x$, bukan $y = x$</sub>
- **C. urutan transformasinya terbalik, dan hasil yang benar adalah $(-1, 7)$** ✅  
  <sub>Benar: pencerminan dilakukan dulu: $(3,-2) \to (-2, 3)$, lalu translasi $(-2+1, 3+4) = (-1, 7)$</sub>
- D. urutannya sudah benar karena urutan tidak memengaruhi hasil, sehingga $(2, 4)$ benar  
  <sub>Salah: mengira komposisi pencerminan dan translasi selalu komutatif</sub>

**Pembahasan:** Pencerminan terhadap $y=x$ menukar koordinat: $(-2,3)$. Translasi: $(-1,7)$. Sinta menerjemahkan dulu, sehingga mendapat $(2,4)$ yang berbeda.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b05-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: banyak titik tetap pada komposisi dua transformasi*

Dalam setiap pilihan, transformasi pertama dilakukan lebih dulu. Komposisi yang memiliki tepat satu titik tetap (titik yang bayangannya adalah dirinya sendiri) adalah ....

- A. pencerminan terhadap garis $2x - y + 1 = 0$, dua kali berturut-turut  
  <sub>Salah: mengira pencerminan dua kali sama dengan satu pencerminan; padahal hasilnya identitas sehingga semua titik tetap</sub>
- B. pencerminan terhadap garis $x = 1$, kemudian pencerminan terhadap garis $x = 4$  
  <sub>Salah: mengira dua pencerminan selalu menyisakan satu titik; padahal komposisinya translasi tanpa titik tetap</sub>
- **C. pencerminan terhadap garis $y = x$, kemudian pencerminan terhadap garis $x + y - 2 = 0$** ✅  
  <sub>Benar: komposisi pilihan pertama adalah rotasi $180^\circ$ terhadap $(1, 1)$: $(x, y) \to (2 - x, 2 - y)$, titik tetapnya hanya $(1, 1)$</sub>
- D. rotasi $90^\circ$ terhadap $O(0, 0)$, kemudian rotasi $270^\circ$ terhadap $O(0, 0)$  
  <sub>Salah: mengira rotasi hanya punya satu titik tetap; padahal komposisinya identitas ($360^\circ$) sehingga semua titik tetap</sub>

**Pembahasan:** $y=x$: $(x,y)\to(y,x)$; $x+y-2=0$: $(a,b)\to(2-b,2-a)$, sehingga $(2-x,2-y)$. Titik tetap: $x=1, y=1$. Pilihan lain: translasi $(6,0)$ (tanpa titik tetap) dan dua identitas.
**Acuan:** siswa — siswa hal.218

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b05-a-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: menentukan pusat dan sudut rotasi dari dua pasang titik*

Sebuah rotasi memetakan $A(1, 1)$ ke $A'(5, 3)$ dan $B(4, 1)$ ke $B'(5, 6)$. Pusat dan sudut rotasi tersebut adalah ....

- A. pusat $(3, 2)$ dan sudut $180^\circ$ berlawanan arah jarum jam  
  <sub>Salah: hanya memetakan $A$ ke $A'$ tetapi tidak memetakan $B$ ke $B'$</sub>
- B. pusat $(4, 2)$ dan sudut $90^\circ$ berlawanan arah jarum jam  
  <sub>Salah: pusat tertukar absis dan ordinat</sub>
- C. pusat $(2, 4)$ dan sudut $270^\circ$ berlawanan arah jarum jam  
  <sub>Salah: salah arah: sudut $270^\circ$ (searah jarum jam) tidak memetakan $\overrightarrow{AB} = (3,0)$ ke $\overrightarrow{A'B'} = (0,3)$</sub>
- **D. pusat $(2, 4)$ dan sudut $90^\circ$ berlawanan arah jarum jam** ✅  
  <sub>Benar: vektor $\overrightarrow{AB} = (3, 0)$ berubah menjadi $\overrightarrow{A'B'} = (0, 3)$ sehingga sudutnya $90^\circ$; pusat dari $A' = \rho(A)$ adalah $(2, 4)$</sub>

**Pembahasan:** Sudut $90^\circ$. Dari $A' = C + (-(A_y - C_y), A_x - C_x)$: $5 = 2\cdot... $ diselesaikan menjadi $C = (2, 4)$. Uji: $B - C = (2,-3) \to (3, 2)$, $+C = (5, 6) = B'$.
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b05-a-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: mengevaluasi transformasi yang memetakan tiga titik*

Segitiga $ABC$ dengan $A(2, 1)$, $B(5, 1)$, dan $C(2, 3)$ dipetakan oleh suatu transformasi menjadi $A'(4, -1)$, $B'(4, 2)$, dan $C'(6, -1)$. Transformasi yang memetakan ketiga titik tersebut sekaligus adalah ....

- **A. pencerminan terhadap garis $y = x$, kemudian translasi oleh $\begin{pmatrix} 3 \\ -3 \end{pmatrix}$** ✅  
  <sub>Benar: hanya komposisi yang membalik orientasi (pencerminan) yang memetakan ketiga titik, karena $ABC$ berlawanan arah jarum jam sedangkan $A'B'C'$ searah</sub>
- B. rotasi $90^\circ$ berlawanan arah jarum jam terhadap titik pusat $(4, 1)$  
  <sub>Salah: memetakan $A$ dan $B$ dengan benar tetapi $C$ menjadi $(2, -1)$; dua titik saja tidak membedakan rotasi dari pencerminan</sub>
- C. rotasi $180^\circ$ terhadap titik pusat $(3, 0)$  
  <sub>Salah: titik tengah $AA'$ dipakai sebagai pusat; hanya cocok untuk $A$</sub>
- D. translasi oleh $\begin{pmatrix} 2 \\ -2 \end{pmatrix}$  
  <sub>Salah: hanya cocok untuk $A$ ($A' - A$), tidak untuk $B$ dan $C$</sub>

**Pembahasan:** Pencerminan $y=x$: $A\to(1,2)$, $B\to(1,5)$, $C\to(3,2)$. Translasi $(3,-3)$: $(4,-1)$, $(4,2)$, $(6,-1)$. Sesuai.
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b05-a-hard-bt01-012
*orisinal | C5 | 3 langkah | jenis: mengevaluasi pernyataan tentang rotasi berdasarkan definisi*

Titik $P(5, 2)$ dirotasikan $120^\circ$ berlawanan arah jarum jam terhadap titik pusat $C(1, -1)$ sehingga menghasilkan $P'$. Pernyataan yang benar adalah ....

- A. panjang $PP'$ sama dengan $2 \cdot CP$  
  <sub>Salah: hanya berlaku untuk sudut rotasi $180^\circ$</sub>
- **B. $C$ terletak pada garis sumbu ruas $PP'$** ✅  
  <sub>Benar: $CP = CP'$ (Definisi 5.3) sehingga $C$ berjarak sama dari $P$ dan $P'$, yaitu berada pada garis sumbu $PP'$</sub>
- C. panjang $PP'$ sama dengan panjang $CP$  
  <sub>Salah: hanya berlaku untuk sudut rotasi $60^\circ$; untuk $120^\circ$ panjang $PP' = \sqrt{3}\,CP$</sub>
- D. titik $C$, $P$, dan $P'$ terletak pada satu garis lurus  
  <sub>Salah: hanya berlaku bila sudut rotasi $180^\circ$</sub>

**Pembahasan:** $CP = CP' = 5$ dan $PP' = 2 \cdot 5 \sin 60^\circ = 5\sqrt3$. Segitiga $CPP'$ sama kaki sehingga $C$ ada pada garis sumbunya; tiga titik tidak segaris karena sudut $120^\circ$.
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
