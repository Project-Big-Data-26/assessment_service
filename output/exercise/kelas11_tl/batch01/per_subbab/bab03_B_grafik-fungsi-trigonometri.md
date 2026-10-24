# Lembar koreksi — kelas11_tl SMA11L-B3 subbab B: Grafik Fungsi Trigonometri

44 soal | easy 20, medium 14, hard 10 | variasi 17, orisinal 27
> **Kapasitas kurang (medium): 14 dari kuota 20** — Subbab B (Grafik Fungsi Trigonometri) teks-saja: acuan variasi siswa yang terbaca sudah dipakai easy (Contoh 3.12 no.1, MM3.12 no.1, Latihan B no.6a, 8a, 9a, 9c, pretest) dan sisa Latihan B/Contoh/MBK butuh grafik; sisa acuan hanya Contoh 3.12 no.2, MM3.12 no.2, Latihan B 8a/8c/9b. Soal orisinal medium (transformasi, model gelombang dua langkah+) lebih banyak akan nyaris kembar satu sama lain.
> **Kapasitas kurang (hard): 10 dari kuota 20** — Subbab B (Grafik Fungsi Trigonometri) hampir seluruh soalnya berbasis gambar grafik (Latihan B, Mari Berpikir Kreatif, Contoh sketsa) dan acuan teks sudah habis di easy/medium; hard hanya bisa berupa evaluasi klaim, contoh penyangkal, kesalahan penyusunan model, dan syarat parameter tanpa membuat soal kembar atau memakai materi di luar subbab.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b03-b-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: periode fungsi sin kx*

Grafik fungsi $h(x) = \sin 5x$ memiliki periode ....

- **A. $\frac{2\pi}{5}$** ✅  
  <sub>Benar: periode $y=\sin kx$ adalah $\frac{2\pi}{k}$ dengan $k=5$</sub>
- B. $\frac{\pi}{5}$  
  <sub>Salah: memakai $\pi$ (bukan $2\pi$) sebagai pembilang</sub>
- C. $10\pi$  
  <sub>Salah: mengalikan $2\pi$ dengan $k$, bukan membagi</sub>
- D. $\frac{5}{2\pi}$  
  <sub>Salah: pembilang dan penyebut rumus periode tertukar</sub>

**Pembahasan:** $T=\frac{2\pi}{k}=\frac{2\pi}{5}$.
**Acuan:** siswa — siswa hal.141 penjelasan Contoh 3.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b03-b-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: amplitudo fungsi sinus*

Grafik fungsi $f(x) = 9 \sin x$ dan $g(x) = -9 \sin x$ sama-sama memiliki amplitudo ....

- A. $\frac{1}{9}$  
  <sub>Salah: memakai kebalikan dari $a$</sub>
- **B. $9$** ✅  
  <sub>Benar: amplitudo $y=a\sin x$ adalah $|a|$, jadi $|9|=|-9|=9$</sub>
- C. $-9$  
  <sub>Salah: amplitudo diambil sama dengan $a$ tanpa nilai mutlak (benar hanya untuk $f$ dan amplitudo tak boleh negatif)</sub>
- D. $18$  
  <sub>Salah: menghitung selisih nilai maksimum dan minimum (tinggi gelombang penuh)</sub>

**Pembahasan:** Amplitudo $=|a|=9$ untuk keduanya.
**Acuan:** siswa — siswa hal.141 penjelasan Contoh 3.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b03-b-easy-bt01-003
*variasi (angka) | C2 | 1 langkah | jenis: arah pergeseran vertikal*

Grafik fungsi $g(x) = \cos x - 6$ dapat diperoleh dengan menggeser grafik fungsi $y = \cos x$ ....

- A. ke atas sejauh 6 satuan  
  <sub>Salah: mengabaikan tanda negatif pada konstanta</sub>
- B. ke kanan sejauh 6 satuan  
  <sub>Salah: mengira konstanta di luar fungsi menggeser secara horizontal (ke kanan)</sub>
- C. ke kiri sejauh 6 satuan  
  <sub>Salah: mengira konstanta di luar fungsi menggeser secara horizontal (ke kiri)</sub>
- **D. ke bawah sejauh 6 satuan** ✅  
  <sub>Benar: konstanta $-6$ di luar fungsi menggeser grafik vertikal ke bawah 6 satuan</sub>

**Pembahasan:** Bentuk $y=\cos x + c$ dengan $c=-6$ menggeser grafik ke bawah 6 satuan.
**Acuan:** siswa — siswa hal.141 Contoh 3.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b03-b-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: model gelombang pelampung*

Sebuah pelampung di laut naik turun mengikuti ombak. Jarak antara posisi tertinggi dan terendahnya 3,2 m. Pelampung bergerak dari posisi tertinggi ke posisi terendah setiap 9 detik. Pada saat $t=0$ detik, pelampung tepat di posisi tengah dan bergerak naik. Fungsi yang memodelkan ketinggian pelampung terhadap posisi tengah setiap $t$ detik adalah ....

- A. $y = 1{,}6 \sin\left(\frac{2\pi}{9}t\right)$  
  <sub>Salah: menganggap 9 detik adalah satu periode penuh</sub>
- B. $y = 1{,}6 \cos\left(\frac{\pi}{9}t\right)$  
  <sub>Salah: memakai kosinus padahal awal gerak di posisi tengah, bukan di puncak</sub>
- **C. $y = 1{,}6 \sin\left(\frac{\pi}{9}t\right)$** ✅  
  <sub>Benar: amplitudo $3{,}2/2=1{,}6$; periode $2\times 9=18$ sehingga $b=\frac{2\pi}{18}=\frac{\pi}{9}$; mulai di tengah dan naik sehingga memakai sinus</sub>
- D. $y = 3{,}2 \sin\left(\frac{\pi}{9}t\right)$  
  <sub>Salah: amplitudo diambil sama dengan jarak tertinggi-terendah, tidak dibagi dua</sub>

**Pembahasan:** Amplitudo $1{,}6$, periode $18$ detik, $b=\frac{\pi}{9}$, bentuk sinus: $y=1{,}6\sin\frac{\pi}{9}t$.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b03-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: model kincir ria dari puncak*

Sebuah kincir ria berdiameter 36 m membutuhkan waktu 8 menit untuk berputar satu putaran. Seseorang mula-mula berada di puncak kincir. Fungsi yang menyatakan ketinggian orang itu terhadap titik pusat kincir setiap $t$ menit adalah ....

- A. $h(t) = 36 \cos\left(\frac{\pi}{4}t\right)$  
  <sub>Salah: memakai diameter sebagai amplitudo, bukan jari-jari</sub>
- **B. $h(t) = 18 \cos\left(\frac{\pi}{4}t\right)$** ✅  
  <sub>Benar: jari-jari $18$ m menjadi amplitudo; $b=\frac{2\pi}{8}=\frac{\pi}{4}$; mulai di puncak sehingga kosinus</sub>
- C. $h(t) = 18 \sin\left(\frac{\pi}{4}t\right)$  
  <sub>Salah: memakai sinus padahal awal gerak di puncak, bukan di titik tengah</sub>
- D. $h(t) = 18 \cos\left(\frac{\pi}{8}t\right)$  
  <sub>Salah: memakai $\frac{\pi}{T}$ sebagai $b$, bukan $\frac{2\pi}{T}$</sub>

**Pembahasan:** $h(t)=18\cos\frac{2\pi}{8}t=18\cos\frac{\pi}{4}t$.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b03-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: model kincir terhadap tanah*

Sebuah kincir ria berdiameter 24 m berputar satu putaran setiap 12 menit. Titik pusatnya berada 15 m di atas tanah. Seseorang mula-mula berada di puncak kincir. Fungsi yang menyatakan ketinggian orang itu terhadap tanah setiap $t$ menit adalah ....

- A. $y = 15 + 24 \cos\left(\frac{\pi}{6}t\right)$  
  <sub>Salah: memakai diameter sebagai amplitudo</sub>
- B. $y = 12 + 15 \cos\left(\frac{\pi}{6}t\right)$  
  <sub>Salah: tertukar antara pergeseran vertikal dan amplitudo</sub>
- **C. $y = 15 + 12 \cos\left(\frac{\pi}{6}t\right)$** ✅  
  <sub>Benar: pusat $15$ m memberi pergeseran vertikal; jari-jari $12$ menjadi amplitudo; $b=\frac{2\pi}{12}=\frac{\pi}{6}$</sub>
- D. $y = 15 + 12 \cos\left(\frac{\pi}{12}t\right)$  
  <sub>Salah: memakai $b=\frac{\pi}{12}$, yaitu $\frac{\pi}{T}$ bukan $\frac{2\pi}{T}$</sub>

**Pembahasan:** $y=15+12\cos\frac{2\pi}{12}t=15+12\cos\frac{\pi}{6}t$.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b03-b-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: model pasang surut dari data tertulis*

Pada suatu hari, ketinggian air di sebuah pelabuhan 0,7 m di atas rata-ratanya saat pasang dan 0,7 m di bawah rata-ratanya saat surut. Dalam 24 jam pelabuhan itu mengalami tiga kali pasang dan tiga kali surut. Pada tengah malam ketinggian air sama dengan rata-ratanya. Fungsi $y = a \sin bx$ yang memodelkan ketinggian air $x$ jam setelah tengah malam adalah ....

- A. $y = 0{,}7 \sin\left(\frac{\pi}{12}x\right)$  
  <sub>Salah: menganggap 24 jam adalah satu periode dan mengabaikan banyak pasang</sub>
- **B. $y = 0{,}7 \sin\left(\frac{\pi}{4}x\right)$** ✅  
  <sub>Benar: tiga siklus dalam 24 jam sehingga periode $8$ jam, $b=\frac{2\pi}{8}=\frac{\pi}{4}$; amplitudo $0{,}7$</sub>
- C. $y = 1{,}4 \sin\left(\frac{\pi}{4}x\right)$  
  <sub>Salah: amplitudo dijumlahkan dari pasang dan surut</sub>
- D. $y = 0{,}7 \sin\left(\frac{\pi}{8}x\right)$  
  <sub>Salah: memakai periode 8 tetapi $b=\frac{\pi}{T}$, bukan $\frac{2\pi}{T}$</sub>

**Pembahasan:** Periode $\frac{24}{3}=8$, $b=\frac{\pi}{4}$, amplitudo $0{,}7$: $y=0{,}7\sin\frac{\pi}{4}x$.
**Acuan:** siswa — siswa hal.146 Contoh 3.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b03-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: model pasang surut bentuk kosinus*

Pada suatu hari, selisih ketinggian antara air pasang dan air surut di sebuah teluk adalah 3,6 m. Air pasang terjadi tepat tengah malam dan pukul 08.00 berikutnya (dua pasang berurutan). Fungsi $y = a \cos bx$ yang memodelkan ketinggian air terhadap rata-ratanya $x$ jam setelah tengah malam adalah ....

- **A. $y = 1{,}8 \cos\left(\frac{\pi}{4}x\right)$** ✅  
  <sub>Benar: amplitudo $3{,}6/2=1{,}8$; periode $8$ jam sehingga $b=\frac{\pi}{4}$; pasang saat $x=0$ sehingga kosinus</sub>
- B. $y = 1{,}8 \cos\left(\frac{\pi}{8}x\right)$  
  <sub>Salah: memakai $b=\frac{\pi}{T}$, bukan $\frac{2\pi}{T}$</sub>
- C. $y = 1{,}8 \sin\left(\frac{\pi}{4}x\right)$  
  <sub>Salah: memakai sinus padahal pada $x=0$ air berada di puncak</sub>
- D. $y = 3{,}6 \cos\left(\frac{\pi}{4}x\right)$  
  <sub>Salah: amplitudo diambil sama dengan selisih pasang-surut</sub>

**Pembahasan:** $y=1{,}8\cos\frac{2\pi}{8}x=1{,}8\cos\frac{\pi}{4}x$.
**Acuan:** siswa — siswa hal.147 Mari Mencoba 3.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b03-b-easy-bt01-009
*variasi (konteks) | C1 | 1 langkah | jenis: pergeseran fungsi bentuk umum*

Pada fungsi $y = a \cos k(x-b)+c$ dengan $k>0$, grafiknya mengalami pergeseran horizontal sejauh .... dan pergeseran vertikal sejauh ....

- **A. $b$ dan $c$** ✅  
  <sub>Benar: pada bentuk umum, $b$ adalah pergeseran horizontal dan $c$ pergeseran vertikal</sub>
- B. $k$ dan $a$  
  <sub>Salah: mengira $k$ dan $a$ (periode dan amplitudo) adalah pergeseran</sub>
- C. $c$ dan $b$  
  <sub>Salah: pergeseran horizontal dan vertikal tertukar</sub>
- D. $-b$ dan $-c$  
  <sub>Salah: menambahkan tanda negatif pada kedua pergeseran</sub>

**Pembahasan:** Sifat 3.3: pergeseran horizontal $b$, pergeseran vertikal $c$.
**Acuan:** pretest — kelas11_tl-b03-p0148-latihan-b-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b03-b-easy-bt01-010
*variasi (konteks) | C1 | 1 langkah | jenis: asimtot vertikal tangen*

Fungsi $y = \tan x$ tidak terdefinisi pada $x = \ldots$ untuk sembarang bilangan bulat $n$.

- A. $\frac{\pi}{4} + n\pi$  
  <sub>Salah: menyangka tidak terdefinisi di sudut istimewa $\frac{\pi}{4}$ (tangen di sana bernilai 1)</sub>
- **B. $\frac{\pi}{2} + n\pi$** ✅  
  <sub>Benar: tangen tidak terdefinisi ketika kosinus bernilai nol, yaitu $x=\frac{\pi}{2}+n\pi$</sub>
- C. $2n\pi$  
  <sub>Salah: menganggap periodenya $2\pi$ seperti sinus dan kosinus</sub>
- D. $n\pi$  
  <sub>Salah: tertukar dengan nilai $x$ tempat tangen sama dengan nol</sub>

**Pembahasan:** $\tan x=\frac{\sin x}{\cos x}$ tak terdefinisi saat $\cos x=0$.
**Acuan:** pretest — kelas11_tl-b03-p0148-latihan-b-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b03-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: amplitudo dan periode fungsi kosinus*

Diberikan fungsi $f(x) = -7 \cos\left(\frac{x}{5}\right)$. Amplitudo dan periode fungsi $f$ berturut-turut adalah ....

- A. $-7$ dan $10\pi$  
  <sub>Salah: amplitudo ditulis negatif tanpa nilai mutlak</sub>
- B. $7$ dan $5\pi$  
  <sub>Salah: memakai $\frac{\pi}{k}$ sebagai periode, lupa faktor 2</sub>
- C. $7$ dan $\frac{2\pi}{5}$  
  <sub>Salah: mengira $k=5$ sehingga periode $\frac{2\pi}{5}$</sub>
- **D. $7$ dan $10\pi$** ✅  
  <sub>Benar: amplitudo $|-7|=7$; $k=\frac{1}{5}$ sehingga periode $\frac{2\pi}{1/5}=10\pi$</sub>

**Pembahasan:** $|a|=7$, $T=2\pi\div\frac{1}{5}=10\pi$.
**Acuan:** siswa — siswa hal.148 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b03-b-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: amplitudo dan periode fungsi sinus*

Diberikan fungsi $h(x) = 6 \sin (4x + \pi)$. Amplitudo dan periode fungsi $h$ berturut-turut adalah ....

- A. $4$ dan $\frac{\pi}{2}$  
  <sub>Salah: amplitudo diambil dari koefisien $x$</sub>
- B. $6$ dan $\frac{\pi}{4}$  
  <sub>Salah: memakai $\frac{\pi}{k}$ sebagai periode, lupa faktor 2</sub>
- C. $6$ dan $8\pi$  
  <sub>Salah: mengalikan $2\pi$ dengan $k$ bukan membaginya</sub>
- **D. $6$ dan $\frac{\pi}{2}$** ✅  
  <sub>Benar: amplitudo $6$; periode $\frac{2\pi}{4}=\frac{\pi}{2}$ (konstanta $\pi$ hanya menggeser grafik)</sub>

**Pembahasan:** $|a|=6$, $T=\frac{2\pi}{4}=\frac{\pi}{2}$.
**Acuan:** siswa — siswa hal.148 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b03-b-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: nilai maksimum fungsi sinus*

Nilai maksimum fungsi $y = 4 \sin 3x + 7$ adalah ....

- A. $28$  
  <sub>Salah: mengalikan amplitudo dengan konstanta pergeseran vertikal</sub>
- B. $3$  
  <sub>Salah: mengira nilai maksimum sama dengan $k$, yaitu koefisien $x$</sub>
- **C. $11$** ✅  
  <sub>Benar: nilai tengah $7$ ditambah amplitudo $4$ menjadi $11$</sub>
- D. $4$  
  <sub>Salah: mengira nilai maksimum sama dengan amplitudo</sub>

**Pembahasan:** Maksimum $=c+|a|=7+4=11$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b03-b-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: periode bentuk k(x-b)*

Fungsi $y = 2 \cos \frac{\pi}{3}(x-1)$ memiliki periode ....

- **A. $6$** ✅  
  <sub>Benar: $k=\frac{\pi}{3}$ sehingga periode $\frac{2\pi}{k}=6$</sub>
- B. $\frac{\pi}{3}$  
  <sub>Salah: menyamakan periode dengan nilai $k$</sub>
- C. $\frac{2\pi}{3}$  
  <sub>Salah: membagi $2\pi$ dengan 3, mengabaikan $\pi$ pada $k$</sub>
- D. $3$  
  <sub>Salah: memakai $\frac{\pi}{k}$, lupa faktor 2</sub>

**Pembahasan:** $T=\frac{2\pi}{\pi/3}=6$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b03-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: pergeseran dari persamaan*

Grafik fungsi $y = -2 \cos 4\left(x - \frac{\pi}{8}\right) + 3$ diperoleh dengan menggeser grafik $y = -2\cos 4x$ sejauh ....

- **A. $\frac{\pi}{8}$ satuan ke kanan dan 3 satuan ke atas** ✅  
  <sub>Benar: bentuk $(x-b)$ dengan $b=\frac{\pi}{8}$ menggeser ke kanan; $c=3$ menggeser ke atas</sub>
- B. $\frac{\pi}{8}$ satuan ke kanan dan 2 satuan ke bawah  
  <sub>Salah: mengambil pergeseran vertikal dari koefisien $a$</sub>
- C. $\frac{\pi}{8}$ satuan ke kiri dan 3 satuan ke atas  
  <sub>Salah: tanda pada $(x-b)$ dibaca terbalik</sub>
- D. $\frac{\pi}{2}$ satuan ke kanan dan 3 satuan ke atas  
  <sub>Salah: mengalikan $b$ dengan $k=4$</sub>

**Pembahasan:** $b=\frac{\pi}{8}>0$ (kanan), $c=3>0$ (atas).
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b03-b-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: nilai sinus dengan sifat periodik*

Diketahui $\sin\frac{\pi}{3} = \frac{\sqrt{3}}{2}$. Nilai $\sin\frac{7\pi}{3}$ adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: tertukar dengan nilai kosinus pada sudut yang sama</sub>
- B. $\sqrt{3}$  
  <sub>Salah: tertukar dengan nilai tangen pada sudut yang sama</sub>
- C. $-\frac{\sqrt{3}}{2}$  
  <sub>Salah: mengira penambahan satu periode membalik tanda</sub>
- **D. $\frac{\sqrt{3}}{2}$** ✅  
  <sub>Benar: $\frac{7\pi}{3}=\frac{\pi}{3}+2\pi$ dan periode sinus $2\pi$</sub>

**Pembahasan:** $\sin\frac{7\pi}{3}=\sin\left(\frac{\pi}{3}+2\pi\right)=\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$.
**Acuan:** siswa — siswa hal.137

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b03-b-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: persamaan dari amplitudo dan periode*

Sebuah fungsi sinus tanpa pergeseran memiliki amplitudo 5 dan periode $\frac{\pi}{2}$. Persamaan fungsi tersebut adalah ....

- A. $y = 4 \sin 5x$  
  <sub>Salah: amplitudo dan $k$ tertukar</sub>
- B. $y = 5 \sin 2x$  
  <sub>Salah: menghitung $k=\frac{\pi}{T}$, lupa faktor 2</sub>
- C. $y = 5 \sin \frac{x}{4}$  
  <sub>Salah: memakai kebalikan $k$, yaitu $\frac{1}{4}$ sebagai pengali $x$</sub>
- **D. $y = 5 \sin 4x$** ✅  
  <sub>Benar: $a=5$; $k=\frac{2\pi}{\pi/2}=4$</sub>

**Pembahasan:** $k=\frac{2\pi}{T}=4$ sehingga $y=5\sin 4x$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b03-b-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: daerah hasil fungsi*

Daerah hasil (range) fungsi $y = -3 \cos x + 1$ adalah ....

- A. $-3 \le y \le 3$  
  <sub>Salah: melupakan pergeseran vertikal $+1$</sub>
- B. $-4 \le y \le 2$  
  <sub>Salah: menggeser dengan tanda terbalik ($c=-1$)</sub>
- **C. $-2 \le y \le 4$** ✅  
  <sub>Benar: amplitudo $3$ di sekitar nilai tengah $1$: dari $1-3=-2$ sampai $1+3=4$</sub>
- D. $1 \le y \le 4$  
  <sub>Salah: hanya menambahkan amplitudo ke nilai tengah, tidak menguranginya</sub>

**Pembahasan:** $y_{\min}=1-3=-2$, $y_{\max}=1+3=4$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b03-b-easy-bt01-019
*orisinal | C2 | 1 langkah | jenis: arah pergeseran horizontal tangen*

Grafik fungsi $y = \tan\left(x + \frac{\pi}{3}\right)$ diperoleh dengan menggeser grafik $y = \tan x$ ....

- A. ke kanan sejauh $\frac{\pi}{3}$ satuan  
  <sub>Salah: tanda pergeseran dibaca terbalik</sub>
- **B. ke kiri sejauh $\frac{\pi}{3}$ satuan** ✅  
  <sub>Benar: bentuk $x+\frac{\pi}{3}$ menggeser grafik ke kiri</sub>
- C. ke bawah sejauh $\frac{\pi}{3}$ satuan  
  <sub>Salah: mengira konstanta di dalam kurung menggeser secara vertikal (ke bawah)</sub>
- D. ke atas sejauh $\frac{\pi}{3}$ satuan  
  <sub>Salah: mengira konstanta di dalam kurung menggeser secara vertikal</sub>

**Pembahasan:** $\tan(x+\frac{\pi}{3})$: geser ke kiri sejauh $\frac{\pi}{3}$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b03-b-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: nilai fungsi di titik*

Jika $f(x) = 7 \sin 2x$, maka nilai $f\left(\frac{\pi}{4}\right)$ adalah ....

- A. $\frac{7\sqrt{2}}{2}$  
  <sub>Salah: lupa mengalikan $x$ dengan 2 sehingga memakai $\sin\frac{\pi}{4}$</sub>
- B. $\frac{7}{2}$  
  <sub>Salah: mengira $\sin\frac{\pi}{2}=\frac{1}{2}$</sub>
- **C. $7$** ✅  
  <sub>Benar: $f(\frac{\pi}{4})=7\sin\frac{\pi}{2}=7\cdot 1$</sub>
- D. $0$  
  <sub>Salah: menghitung $\sin\pi$ (mengalikan sudut dua kali)</sub>

**Pembahasan:** $7\sin\frac{\pi}{2}=7$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b03-b-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: evaluasi model pasang surut sinus*

Ketinggian permukaan air sebuah teluk terhadap tinggi rata-ratanya dimodelkan oleh fungsi $y = 0{,}6 \sin\left(\frac{\pi}{9}x\right)$ dengan $x$ dalam jam setelah pukul 00.00. Dengan menggunakan fungsi tersebut, perkirakan ketinggian permukaan air teluk tersebut pada pukul 21.00.

- A. sekitar $0{,}30$ m di atas tinggi rata-rata  
  <sub>Salah: memakai $\sin\frac{\pi}{3}=\frac{1}{2}$ (tertukar dengan nilai kosinus)</sub>
- B. sekitar $0{,}42$ m di atas tinggi rata-rata  
  <sub>Salah: memakai $\sin\frac{\pi}{3}=\frac{\sqrt{2}}{2}$ (tertukar dengan sudut $\frac{\pi}{4}$)</sub>
- **C. sekitar $0{,}52$ m di atas tinggi rata-rata** ✅  
  <sub>Benar: $x=21$ sehingga $\sin\frac{7\pi}{3}=\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$ dan $y=0{,}6\cdot\frac{\sqrt{3}}{2}\approx 0{,}52$ (positif berarti di atas rata-rata)</sub>
- D. sekitar $0{,}52$ m di bawah tinggi rata-rata  
  <sub>Salah: nilai sinus diberi tanda negatif (salah menentukan kuadran setelah reduksi sudut)</sub>

**Pembahasan:** $y=0{,}6\sin\frac{21\pi}{9}=0{,}6\sin\frac{7\pi}{3}=0{,}6\sin\frac{\pi}{3}=0{,}6\cdot\frac{\sqrt{3}}{2}\approx 0{,}52$ m di atas rata-rata.
**Acuan:** siswa — siswa hal.147 Contoh 3.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b03-b-medium-bt01-002
*variasi (angka) | C3 | 4 langkah | jenis: model pasang surut kosinus lalu evaluasi*

Selisih ketinggian air pasang dan air surut di sebuah teluk adalah 3,2 m. Air pasang terjadi pada pukul 00.00 dan pasang berikutnya pada pukul 09.00. Ketinggian air terhadap tinggi rata-ratanya $x$ jam setelah pukul 00.00 dimodelkan oleh $y = a\cos bx$. Perkirakan ketinggian permukaan air teluk tersebut pada pukul 15.00.

- A. $1{,}6$ m di bawah tinggi rata-rata  
  <sub>Salah: amplitudo diambil sama dengan selisih pasang-surut ($3{,}2$) dan hasil kali dengan $-\frac{1}{2}$</sub>
- B. $0{,}8$ m di atas tinggi rata-rata  
  <sub>Salah: memakai $b=\frac{\pi}{T}$ sehingga sudutnya $\frac{5\pi}{3}$ dan kosinus bernilai $+\frac{1}{2}$</sub>
- **C. $0{,}8$ m di bawah tinggi rata-rata** ✅  
  <sub>Benar: $a=\frac{3{,}2}{2}=1{,}6$, periode $9$ sehingga $b=\frac{2\pi}{9}$; $y=1{,}6\cos\frac{10\pi}{3}=1{,}6\cos\frac{4\pi}{3}=1{,}6\cdot\left(-\frac{1}{2}\right)=-0{,}8$</sub>
- D. $1{,}4$ m di bawah tinggi rata-rata  
  <sub>Salah: memakai sinus (bukan kosinus) sehingga hasilnya $1{,}6\sin\frac{10\pi}{3}\approx -1{,}4$</sub>

**Pembahasan:** $y=1{,}6\cos\left(\frac{2\pi}{9}\cdot 15\right)=1{,}6\cos\frac{10\pi}{3}=1{,}6\cos\frac{4\pi}{3}=-0{,}8$ m.
**Acuan:** siswa — siswa hal.148 Mari Mencoba 3.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b03-b-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: evaluasi model gelombang pelampung*

Sebuah pelampung penanda naik turun mengikuti ombak. Jarak antara posisi tertinggi dan terendahnya adalah 5,4 m, dan pelampung bergerak dari posisi tertinggi ke posisi terendah setiap 6 detik. Pada saat awal pelampung tepat di posisi tengah dan bergerak naik. Tentukan posisi pelampung tersebut 14 detik setelah posisi awalnya.

- A. sekitar $2{,}34$ m di bawah posisi tengah  
  <sub>Salah: salah tanda setelah mereduksi sudut $\frac{7\pi}{3}$</sub>
- **B. sekitar $2{,}34$ m di atas posisi tengah** ✅  
  <sub>Benar: $a=2{,}7$; periode $12$ detik sehingga $b=\frac{\pi}{6}$; $y=2{,}7\sin\frac{14\pi}{6}=2{,}7\sin\frac{7\pi}{3}=2{,}7\cdot\frac{\sqrt{3}}{2}\approx 2{,}34$</sub>
- C. sekitar $1{,}35$ m di atas posisi tengah  
  <sub>Salah: memakai $\sin\frac{7\pi}{3}=\frac{1}{2}$ (tertukar dengan kosinus)</sub>
- D. sekitar $4{,}68$ m di atas posisi tengah  
  <sub>Salah: amplitudo diambil sama dengan jarak tertinggi-terendah, tidak dibagi dua</sub>

**Pembahasan:** $y=2{,}7\sin\left(\frac{\pi}{6}t\right)$, sehingga $y(14)=2{,}7\sin\frac{7\pi}{3}=2{,}7\sin\frac{\pi}{3}\approx 2{,}34$ m.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b03-b-medium-bt01-004
*variasi (angka) | C3 | 4 langkah | jenis: evaluasi model kincir ria terhadap tanah*

Sebuah kincir ria berdiameter 40 m membutuhkan waktu 9 menit untuk berputar satu putaran. Titik pusat kincir ria berada 22 m di atas permukaan tanah. Seseorang mula-mula berada di puncak kincir ria. Tentukan ketinggian orang tersebut dari permukaan tanah ketika kincir ria berputar selama 6 menit.

- A. $32$ m  
  <sub>Salah: memakai $\cos\frac{4\pi}{3}=+\frac{1}{2}$ (salah tanda di kuadran III)</sub>
- B. $2$ m  
  <sub>Salah: memakai diameter $40$ sebagai amplitudo, bukan jari-jari</sub>
- C. $-10$ m  
  <sub>Salah: lupa menambahkan tinggi pusat $22$ m (ketinggian relatif terhadap pusat)</sub>
- **D. $12$ m** ✅  
  <sub>Benar: $h(t)=22+20\cos\frac{2\pi}{9}t$; $h(6)=22+20\cos\frac{4\pi}{3}=22+20\cdot\left(-\frac{1}{2}\right)=12$</sub>

**Pembahasan:** $h(t)=22+20\cos\left(\frac{2\pi}{9}t\right)$, sehingga $h(6)=22+20\cos\frac{4\pi}{3}=22-10=12$ m.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b03-b-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: model gelombang dengan arah gerak awal*

Sebuah perahu kecil di dermaga bergerak naik turun terbawa gelombang. Selisih tinggi antara puncak dan lembah gelombang yang dilalui perahu adalah 2,4 m. Perahu bergerak dari puncak ke lembah setiap 5 detik. Pada saat $t=0$ detik, perahu tepat berada di posisi tengah dan bergerak turun. Fungsi yang memodelkan ketinggian perahu terhadap posisi tengah setiap $t$ detik adalah ....

- **A. $y = -1{,}2\sin\left(\frac{\pi}{5}t\right)$** ✅  
  <sub>Benar: amplitudo $\frac{2{,}4}{2}=1{,}2$; periode $2\times 5=10$ sehingga $b=\frac{\pi}{5}$; mulai di tengah dan bergerak turun sehingga sinus dengan $a$ negatif</sub>
- B. $y = 1{,}2\sin\left(\frac{\pi}{5}t\right)$  
  <sub>Salah: mengabaikan arah gerak awal: fungsi ini justru bergerak naik pada $t=0$</sub>
- C. $y = -2{,}4\sin\left(\frac{\pi}{5}t\right)$  
  <sub>Salah: amplitudo diambil sama dengan selisih puncak-lembah, tidak dibagi dua</sub>
- D. $y = -1{,}2\sin\left(\frac{2\pi}{5}t\right)$  
  <sub>Salah: menganggap 5 detik adalah satu periode penuh</sub>

**Pembahasan:** $a=-1{,}2$ (turun lebih dulu), $b=\frac{2\pi}{10}=\frac{\pi}{5}$: $y=-1{,}2\sin\frac{\pi}{5}t$.
**Acuan:** siswa — siswa hal.149 Latihan B Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b03-b-medium-bt01-006
*orisinal | C3 | 2 langkah | jenis: nilai minimum dan periode bentuk $a\cos(kx-\phi)+c$*

Nilai minimum dan periode fungsi $y = 5 - 3\cos(4x - \pi)$ berturut-turut adalah ....

- **A. $2$ dan $\frac{\pi}{2}$** ✅  
  <sub>Benar: nilai tengah $5$ dan amplitudo $3$ sehingga minimum $5-3=2$; periode $\frac{2\pi}{4}=\frac{\pi}{2}$ (konstanta $\pi$ hanya menggeser grafik)</sub>
- B. $-3$ dan $\frac{\pi}{2}$  
  <sub>Salah: memakai $-a$ sebagai minimum, lupa nilai tengah $5$</sub>
- C. $8$ dan $\frac{\pi}{2}$  
  <sub>Salah: memberi nilai maksimum $5+3$ padahal yang ditanyakan minimum</sub>
- D. $2$ dan $8\pi$  
  <sub>Salah: mengalikan $2\pi$ dengan $k=4$, bukan membaginya</sub>

**Pembahasan:** $y_{\min}=5-3=2$; $T=\frac{2\pi}{4}=\frac{\pi}{2}$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b03-b-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: menyusun persamaan dari maksimum, minimum, periode*

Sebuah fungsi berbentuk $y = a\sin kx + c$ dengan $a>0$ dan $k>0$ memiliki nilai maksimum $5$, nilai minimum $-1$, dan periode $4$. Persamaan fungsi tersebut adalah ....

- A. $y = 2\sin\left(\frac{\pi}{2}x\right) + 3$  
  <sub>Salah: amplitudo dan nilai tengah tertukar</sub>
- B. $y = 3\sin\left(\frac{\pi}{4}x\right) + 2$  
  <sub>Salah: memakai $k=\frac{\pi}{T}$, lupa faktor 2</sub>
- C. $y = 6\sin\left(\frac{\pi}{2}x\right) + 2$  
  <sub>Salah: amplitudo diambil sama dengan $M-m$, tidak dibagi dua</sub>
- **D. $y = 3\sin\left(\frac{\pi}{2}x\right) + 2$** ✅  
  <sub>Benar: $a=\frac{M-m}{2}=3$, $c=\frac{M+m}{2}=2$, $k=\frac{2\pi}{4}=\frac{\pi}{2}$</sub>

**Pembahasan:** $a=\frac{5-(-1)}{2}=3$, $c=\frac{5+(-1)}{2}=2$, $k=\frac{2\pi}{4}=\frac{\pi}{2}$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b03-b-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: letak nilai maksimum pertama bentuk $a\sin k(x-b)+c$*

Nilai $x$ positif terkecil yang membuat fungsi $y = 5\sin 2\left(x - \frac{\pi}{6}\right) + 3$ mencapai nilai maksimumnya adalah ....

- A. $\frac{\pi}{4}$  
  <sub>Salah: mengabaikan pergeseran horizontal $\frac{\pi}{6}$</sub>
- **B. $\frac{5\pi}{12}$** ✅  
  <sub>Benar: maksimum tercapai saat $2\left(x-\frac{\pi}{6}\right)=\frac{\pi}{2}$, sehingga $x=\frac{\pi}{4}+\frac{\pi}{6}=\frac{5\pi}{12}$</sub>
- C. $\frac{\pi}{12}$  
  <sub>Salah: mengurangi pergeseran, bukan menambahkannya: $\frac{\pi}{4}-\frac{\pi}{6}$</sub>
- D. $\frac{2\pi}{3}$  
  <sub>Salah: tidak membagi dengan $k=2$: $\frac{\pi}{2}+\frac{\pi}{6}$</sub>

**Pembahasan:** $\sin 2(x-\frac{\pi}{6})=1 \Rightarrow 2x-\frac{\pi}{3}=\frac{\pi}{2}+2n\pi \Rightarrow x=\frac{5\pi}{12}+n\pi$; yang positif terkecil $\frac{5\pi}{12}$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b03-b-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: urutan transformasi grafik sinus*

Grafik fungsi $g(x) = \sin\left(\frac{\pi}{3} - x\right)$ dapat diperoleh dari grafik $y = \sin x$ dengan ....

- A. menggeser ke kanan sejauh $\frac{\pi}{3}$ satuan, kemudian mencerminkan hasilnya terhadap sumbu-$y$  
  <sub>Salah: mengira tanda negatif pada $x$ berarti pencerminan terhadap sumbu-$y$ setelah digeser</sub>
- B. menggeser ke kanan sejauh $\frac{\pi}{3}$ satuan saja, tanpa pencerminan  
  <sub>Salah: mengabaikan tanda negatif pada $x$ di dalam sinus</sub>
- C. menggeser ke kiri sejauh $\frac{\pi}{3}$ satuan, kemudian mencerminkan hasilnya terhadap sumbu-$x$  
  <sub>Salah: tanda pergeseran dibaca terbalik</sub>
- **D. menggeser ke kanan sejauh $\frac{\pi}{3}$ satuan, kemudian mencerminkan hasilnya terhadap sumbu-$x$** ✅  
  <sub>Benar: $\sin\left(\frac{\pi}{3}-x\right)=-\sin\left(x-\frac{\pi}{3}\right)$: geser kanan $\frac{\pi}{3}$, lalu cermin terhadap sumbu-$x$</sub>

**Pembahasan:** $\sin(\frac{\pi}{3}-x)=-\sin(x-\frac{\pi}{3})$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b03-b-medium-bt01-010
*orisinal | C3 | 2 langkah | jenis: asimtot vertikal tangen yang digeser*

Untuk sembarang bilangan bulat $n$, garis asimtot vertikal grafik fungsi $y = 2\tan\left(x + \frac{\pi}{6}\right)$ adalah $x = \ldots$

- A. $-\frac{\pi}{3} + n\pi$  
  <sub>Salah: menggeser asimtot ke arah yang salah: $-\frac{\pi}{2}+\frac{\pi}{6}$ dibaca sebagai $-\frac{\pi}{3}$</sub>
- **B. $\frac{\pi}{3} + n\pi$** ✅  
  <sub>Benar: tak terdefinisi saat $x+\frac{\pi}{6}=\frac{\pi}{2}+n\pi$, sehingga $x=\frac{\pi}{3}+n\pi$</sub>
- C. $\frac{\pi}{2} + n\pi$  
  <sub>Salah: mengabaikan pergeseran horizontal</sub>
- D. $-\frac{\pi}{6} + n\pi$  
  <sub>Salah: tertukar dengan letak $x$ yang membuat fungsi bernilai nol</sub>

**Pembahasan:** $x+\frac{\pi}{6}=\frac{\pi}{2}+n\pi \Rightarrow x=\frac{\pi}{3}+n\pi$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b03-b-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: waktu pertama mencapai ketinggian tertentu pada model*

Ketinggian seorang penumpang kincir ria dari permukaan tanah dimodelkan oleh $h(t) = 10 + 8\cos\left(\frac{\pi}{6}t\right)$ dengan $h$ dalam meter dan $t$ dalam menit sejak kincir mulai berputar. Pertama kali setelah kincir mulai berputar, penumpang berada pada ketinggian 14 m saat $t = \ldots$ menit.

- A. $1$  
  <sub>Salah: memakai $\cos\frac{\pi}{6}=\frac{1}{2}$ (sudut istimewa tertukar dengan $\frac{\pi}{3}$)</sub>
- B. $3$  
  <sub>Salah: menganggap $\cos\theta=\frac{1}{2}$ terjadi pada $\theta=\frac{\pi}{2}$</sub>
- C. $4$  
  <sub>Salah: memakai $\cos\theta=-\frac{1}{2}$ (salah tanda), sehingga $\theta=\frac{2\pi}{3}$</sub>
- **D. $2$** ✅  
  <sub>Benar: $10+8\cos\frac{\pi}{6}t=14 \Rightarrow \cos\frac{\pi}{6}t=\frac{1}{2} \Rightarrow \frac{\pi}{6}t=\frac{\pi}{3} \Rightarrow t=2$</sub>

**Pembahasan:** $\cos\frac{\pi}{6}t=\frac{4}{8}=\frac{1}{2}$; akar pertama $t>0$: $\frac{\pi}{6}t=\frac{\pi}{3}$, $t=2$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b03-b-medium-bt01-012
*orisinal | C4 | 4 langkah | jenis: model pasang surut dengan pergeseran horizontal dan vertikal*

Tinggi rata-rata permukaan air di sebuah pelabuhan adalah 4 m dan selisih tinggi air pasang dengan air surut adalah 3 m. Air pasang tertinggi terjadi pada pukul 02.00, dan pasang tertinggi berikutnya pada pukul 14.00. Ketinggian air $x$ jam setelah tengah malam dimodelkan oleh $y = c + a\cos k(x-b)$ dengan $a>0$, $k>0$, dan $b$ sebagai waktu pasang pertama. Model yang tepat adalah ....

- A. $y = 4 + 1{,}5\cos\left(\frac{\pi}{6}(x+2)\right)$  
  <sub>Salah: tanda pergeseran horizontal terbalik</sub>
- B. $y = 4 + 3\cos\left(\frac{\pi}{6}(x-2)\right)$  
  <sub>Salah: amplitudo diambil sama dengan selisih pasang-surut, tidak dibagi dua</sub>
- **C. $y = 4 + 1{,}5\cos\left(\frac{\pi}{6}(x-2)\right)$** ✅  
  <sub>Benar: $c=4$, $a=\frac{3}{2}=1{,}5$, periode $14-2=12$ sehingga $k=\frac{\pi}{6}$, dan pasang pada $x=2$ sehingga $b=2$</sub>
- D. $y = 4 + 1{,}5\cos\left(\frac{\pi}{12}(x-2)\right)$  
  <sub>Salah: memakai $k=\frac{\pi}{T}$, lupa faktor 2</sub>

**Pembahasan:** Periode $12$ jam, $k=\frac{2\pi}{12}=\frac{\pi}{6}$; maksimum $5{,}5$ pada $x=2$ dan $x=14$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b03-b-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: analisis bentuk $a\sin(kx-\phi)+c$ (pergeseran sebenarnya)*

Perhatikan fungsi $y = 4\sin\left(2x - \frac{\pi}{3}\right) + 1$. Pernyataan yang benar tentang grafiknya adalah ....

- **A. nilai maksimumnya $5$ dan grafiknya bergeser $\frac{\pi}{6}$ satuan ke kanan dari grafik $y = 4\sin 2x + 1$** ✅  
  <sub>Benar: $4\sin(2x-\frac{\pi}{3})+1=4\sin 2(x-\frac{\pi}{6})+1$: maksimum $1+4=5$ dan pergeseran $\frac{\pi}{6}$ ke kanan</sub>
- B. nilai maksimumnya $5$ dan grafiknya bergeser $\frac{\pi}{3}$ satuan ke kanan dari grafik $y = 4\sin 2x + 1$  
  <sub>Salah: tidak memfaktorkan $k=2$ sehingga pergeseran dibaca $\frac{\pi}{3}$</sub>
- C. nilai maksimumnya $4$ dan grafiknya bergeser $\frac{\pi}{6}$ satuan ke kanan dari grafik $y = 4\sin 2x + 1$  
  <sub>Salah: maksimum dikira sama dengan amplitudo, lupa nilai tengah $1$</sub>
- D. nilai maksimumnya $5$ dan grafiknya bergeser $\frac{\pi}{6}$ satuan ke kiri dari grafik $y = 4\sin 2x + 1$  
  <sub>Salah: arah pergeseran dibaca terbalik</sub>

**Pembahasan:** Faktorkan: $2x-\frac{\pi}{3}=2\left(x-\frac{\pi}{6}\right)$ sehingga $b=\frac{\pi}{6}$ (kanan); $y_{\max}=1+4=5$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b03-b-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: banyak titik maksimum pada interval tertutup*

Banyak titik pada grafik $y = 2\cos 3x + 1$ dengan $0 \le x \le 2\pi$ yang bernilai maksimum adalah ....

- **A. $4$** ✅  
  <sub>Benar: periode $\frac{2\pi}{3}$; maksimum di $x=0,\ \frac{2\pi}{3},\ \frac{4\pi}{3},\ 2\pi$ (ujung interval ikut dihitung)</sub>
- B. $6$  
  <sub>Salah: mengalikan $k=3$ dengan 2 tanpa memeriksa letak puncak</sub>
- C. $2$  
  <sub>Salah: mengambil koefisien $a=2$ sebagai banyak puncak</sub>
- D. $3$  
  <sub>Salah: menghitung banyak periode ($2\pi\div\frac{2\pi}{3}=3$) dan tidak menghitung titik $x=2\pi$</sub>

**Pembahasan:** $\cos 3x=1 \Rightarrow x=\frac{2n\pi}{3}$; pada $[0,2\pi]$ ada $n=0,1,2,3$, yaitu 4 titik.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [hard] kelas11_tl-b03-b-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: temukan kesalahan model kincir ria*

Sebuah kincir ria berdiameter 30 m berputar satu putaran setiap 10 menit. Titik pusatnya 20 m di atas tanah. Seorang penumpang mula-mula berada di titik terendah. Rani memodelkan tinggi penumpang $h$ (dalam meter) setelah $t$ menit dengan $h(t) = 20 + 15\cos\left(\frac{\pi}{5}t\right)$. Pernyataan yang benar tentang model Rani adalah ....

- A. Salah, karena amplitudonya harus 30; seharusnya $h(t) = 20 + 30\cos\left(\frac{\pi}{5}t\right)$  
  <sub>Salah: mengira amplitudo sama dengan diameter, bukan jari-jari</sub>
- B. Salah, karena nilai tengahnya 15; seharusnya $h(t) = 15 + 15\cos\left(\frac{\pi}{5}t\right)$  
  <sub>Salah: mengira nilai tengah sama dengan jari-jari</sub>
- C. Salah, karena periodenya 10; seharusnya $h(t) = 20 + 15\cos\left(\frac{\pi}{10}t\right)$  
  <sub>Salah: mengira $k$ sama dengan setengah periode, padahal $k=\frac{2\pi}{10}$</sub>
- **D. Salah, karena $h(0)=35$ (titik tertinggi); seharusnya $h(t) = 20 - 15\cos\left(\frac{\pi}{5}t\right)$** ✅  
  <sub>Benar: pada $t=0$ model Rani memberi 35 m, padahal penumpang di titik terendah (5 m); tanda $a$ harus negatif, sedangkan amplitudo 15, periode 10, dan nilai tengah 20 sudah benar</sub>

**Pembahasan:** $h(0)=20+15=35$ m sehingga model Rani menunjukkan titik tertinggi. Amplitudo $\frac{30}{2}=15$, $k=\frac{2\pi}{10}=\frac{\pi}{5}$, dan $c=20$ benar. Dari titik terendah diperlukan $a<0$: $h(t)=20-15\cos\left(\frac{\pi}{5}t\right)$ dengan $h(0)=5$.
**Acuan:** siswa — siswa hal.147

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [hard] kelas11_tl-b03-b-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: syarat parameter dua kondisi pada fungsi kosinus*

Diketahui fungsi $y = a\cos kx + c$ dengan $a>0$ dan $k>0$. Fungsi ini bernilai maksimum $6$ dan bernilai minimum $-2$, serta grafiknya melalui titik $\left(\frac{\pi}{4}, 0\right)$. Nilai $k$ terkecil yang mungkin adalah ....

- A. $\frac{16}{3}$  
  <sub>Salah: memakai solusi sudut kedua $\frac{4\pi}{3}$ sehingga bukan $k$ terkecil</sub>
- B. $\frac{4}{3}$  
  <sub>Salah: memakai sudut acuan $\frac{\pi}{3}$ tanpa memperhatikan nilai kosinus negatif</sub>
- **C. $\frac{8}{3}$** ✅  
  <sub>Benar: $a=4$, $c=2$; dari $4\cos\frac{k\pi}{4}+2=0$ diperoleh $\cos\frac{k\pi}{4}=-\frac{1}{2}$, sehingga sudut terkecil $\frac{2\pi}{3}$ dan $k=\frac{8}{3}$</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: mengira $\cos\theta=-\frac{1}{2}$ pada $\theta=\frac{\pi}{6}$</sub>

**Pembahasan:** $a=\frac{6-(-2)}{2}=4$, $c=\frac{6+(-2)}{2}=2$. Titik $\left(\frac{\pi}{4},0\right)$ memberi $\cos\frac{k\pi}{4}=-\frac{1}{2}$, sudut positif terkecil $\frac{2\pi}{3}$, jadi $\frac{k\pi}{4}=\frac{2\pi}{3}$ dan $k=\frac{8}{3}$.
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas11_tl-b03-b-hard-bt01-003
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim daerah hasil*

Seorang siswa mengklaim: "Untuk fungsi $y = a\sin kx + c$ dengan $k>0$ dan $a\neq 0$, selisih nilai maksimum dan nilai minimum selalu sama dengan $2a$." Fungsi berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $y = \frac{1}{2}\sin 5x - 1$  
  <sub>Salah: klaim terpenuhi ($a=\frac{1}{2}>0$, selisih $1=2a$)</sub>
- B. $y = 6\sin\frac{x}{2} + 3$  
  <sub>Salah: klaim terpenuhi ($a=6>0$, selisih $12=2a$)</sub>
- **C. $y = -5\sin 2x + 1$** ✅  
  <sub>Benar: selisih maksimum dan minimum adalah $2|a|=10$, sedangkan $2a=-10$, sehingga klaim gagal untuk $a<0$</sub>
- D. $y = 4\sin 3x - 2$  
  <sub>Salah: klaim terpenuhi ($a=4>0$, selisih $8=2a$)</sub>

**Pembahasan:** Amplitudo adalah $|a|$ sehingga selisih maksimum dan minimum adalah $2|a|$, yang sama dengan $2a$ hanya jika $a>0$. Satu-satunya fungsi dengan $a<0$ adalah $y=-5\sin 2x+1$.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas11_tl-b03-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: bandingkan beberapa model kincir ria*

Sebuah kincir ria berdiameter 24 m berputar satu putaran setiap 10 menit, pusatnya 14 m di atas tanah, dan penumpang mula-mula berada di titik terendah. Tinggi penumpang $h$ (dalam meter) setelah $t$ menit dimodelkan oleh empat siswa: Andi $h=14-12\cos\left(\frac{\pi}{5}t\right)$, Budi $h=14+12\sin\left(\frac{\pi}{5}(t-2{,}5)\right)$, Citra $h=14+12\cos\left(\frac{\pi}{5}t\right)$, dan Dewi $h=14+12\sin\left(\frac{\pi}{5}t\right)$. Pasangan siswa yang modelnya sesuai dengan data adalah ....

- **A. Andi dan Budi** ✅  
  <sub>Benar: model Budi sama dengan $14-12\cos\left(\frac{\pi}{5}t\right)$ karena $\sin\left(\theta-\frac{\pi}{2}\right)=-\cos\theta$; keduanya memberi $h(0)=2$ m dan naik setelahnya</sub>
- B. Budi dan Citra  
  <sub>Salah: Citra memberi $h(0)=26$ m (titik tertinggi)</sub>
- C. Citra dan Dewi  
  <sub>Salah: Citra mulai dari titik tertinggi dan Dewi mulai dari titik tengah</sub>
- D. Andi dan Dewi  
  <sub>Salah: Dewi memberi $h(0)=14$ m (titik tengah), bukan titik terendah</sub>

**Pembahasan:** Syarat: $h(0)=2$ dan $h$ naik, maksimum 26, periode 10. Andi: $h(0)=2$. Budi: $14+12\sin\left(\frac{\pi}{5}t-\frac{\pi}{2}\right)=14-12\cos\left(\frac{\pi}{5}t\right)$, identik dengan Andi. Citra $h(0)=26$ dan Dewi $h(0)=14$ tidak sesuai.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas11_tl-b03-b-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: temukan langkah salah menyusun model sinus*

Doni diminta menentukan fungsi $y = a\sin kx + c$ dengan $a>0$ dan $k>0$ yang bernilai maksimum $11$, bernilai minimum $-3$, dan berperiode $6$. Pengerjaannya: (1) $c=\frac{11+(-3)}{2}=4$; (2) $a=\frac{11-(-3)}{2}=7$; (3) $k=\frac{6}{2\pi}=\frac{3}{\pi}$. Pernyataan yang benar tentang pengerjaan Doni adalah ....

- **A. Langkah (3) salah; seharusnya $k=\frac{2\pi}{6}=\frac{\pi}{3}$** ✅  
  <sub>Benar: langkah (1) dan (2) benar, sedangkan langkah (3) membalik rumus periode $T=\frac{2\pi}{k}$; $k=\frac{\pi}{3}$ sehingga $y=7\sin\frac{\pi}{3}x+4$</sub>
- B. Langkah (1) salah; seharusnya $c=\frac{11+3}{2}=7$  
  <sub>Salah: mengabaikan tanda negatif pada nilai minimum</sub>
- C. Langkah (2) salah; seharusnya $a=11$ karena amplitudo sama dengan nilai maksimum  
  <sub>Salah: mengira amplitudo adalah nilai maksimum, bukan setengah selisih</sub>
- D. Langkah (3) salah; seharusnya $k=2\pi\times 6=12\pi$  
  <sub>Salah: membalik rumus periode menjadi $k=2\pi T$</sub>

**Pembahasan:** $c=4$ dan $a=7$ benar (maksimum $7+4=11$, minimum $-7+4=-3$). Dari $T=\frac{2\pi}{k}$ diperoleh $k=\frac{2\pi}{T}=\frac{\pi}{3}$; Doni menuliskan $\frac{T}{2\pi}$.
**Acuan:** siswa — siswa hal.147

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas11_tl-b03-b-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: evaluasi pernyataan tentang tangen bergeser*

Diketahui $g(x)=\tan\left(2x-\frac{\pi}{2}\right)$. Pernyataan yang benar adalah ....

- A. $g(0)=0$ dan $g$ tidak terdefinisi di $x=\frac{\pi}{4}$  
  <sub>Salah: menukar titik terdefinisi dan titik tidak terdefinisi</sub>
- B. $g\left(\frac{\pi}{4}\right)=0$ dan $g$ terdefinisi di $x=0$  
  <sub>Salah: mengira $\tan\left(-\frac{\pi}{2}\right)=0$</sub>
- C. $g\left(\frac{\pi}{4}\right)=1$ dan $g$ tidak terdefinisi di $x=0$  
  <sub>Salah: mengira $\tan 0 = 1$</sub>
- **D. $g\left(\frac{\pi}{4}\right)=0$ dan $g$ tidak terdefinisi di $x=0$** ✅  
  <sub>Benar: $g\left(\frac{\pi}{4}\right)=\tan 0=0$, sedangkan di $x=0$ argumennya $-\frac{\pi}{2}$ sehingga tidak terdefinisi</sub>

**Pembahasan:** Argumen $2x-\frac{\pi}{2}$ bernilai $0$ di $x=\frac{\pi}{4}$ dan $-\frac{\pi}{2}$ di $x=0$; tangen bernilai 0 di argumen 0 dan tidak terdefinisi di $-\frac{\pi}{2}$.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b03-b-hard-bt01-007
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim kesamaan grafik*

Seorang siswa mengklaim: "Dua fungsi berbentuk $y=a\sin kx$ atau $y=a\cos kx$ dengan $k>0$ yang amplitudonya sama dan periodenya sama pasti memiliki grafik yang berimpit." Pasangan fungsi yang merupakan contoh penyangkal klaim tersebut adalah ....

- A. $y = 3\sin 2x$ dan $y = 3\sin 4x$  
  <sub>Salah: periode berbeda sehingga syarat klaim tidak terpenuhi, bukan penyangkal</sub>
- **B. $y = 6\sin 2x$ dan $y = 6\cos 2x$** ✅  
  <sub>Benar: keduanya beramplitudo 6 dan berperiode $\pi$, tetapi $\sin 2x \neq \cos 2x$ (misalnya di $x=0$ nilainya 0 dan 6)</sub>
- C. $y = 3\sin 2x$ dan $y = 5\sin 2x$  
  <sub>Salah: amplitudo berbeda sehingga syarat klaim tidak terpenuhi, bukan penyangkal</sub>
- D. $y = 3\cos 2x$ dan $y = 5\cos 4x$  
  <sub>Salah: amplitudo dan periode berbeda sehingga bukan penyangkal</sub>

**Pembahasan:** Penyangkal harus memenuhi syarat klaim (amplitudo dan periode sama) tetapi grafik tidak berimpit. Hanya pasangan $6\sin 2x$ dan $6\cos 2x$ yang demikian: di $x=0$ nilainya 0 dan 6.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b03-b-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: syarat bilangan bulat agar dua titik ekstrem terpenuhi*

Diketahui $f(x)=\sin kx$ dengan $k$ bilangan bulat positif. Fungsi $f$ bernilai maksimum di $x=\frac{\pi}{2}$ dan bernilai minimum di $x=\frac{\pi}{6}$. Nilai $k$ terkecil yang memenuhi kedua syarat adalah ....

- A. $21$  
  <sub>Salah: memenuhi kedua syarat tetapi bukan yang terkecil</sub>
- **B. $9$** ✅  
  <sub>Benar: $\sin\frac{k\pi}{2}=1$ untuk $k=1,5,9,\ldots$; $\sin\frac{k\pi}{6}=-1$ untuk $k=9,21,\ldots$; irisan terkecil adalah 9</sub>
- C. $5$  
  <sub>Salah: $k=5$ memenuhi syarat maksimum di $\frac{\pi}{2}$ saja; di $x=\frac{\pi}{6}$ nilainya $\sin\frac{5\pi}{6}=\frac{1}{2}$</sub>
- D. $3$  
  <sub>Salah: $k=3$ memberi $\sin\frac{3\pi}{2}=-1$ di $x=\frac{\pi}{2}$ dan $\sin\frac{\pi}{2}=1$ di $x=\frac{\pi}{6}$: maksimum dan minimum tertukar</sub>

**Pembahasan:** Syarat 1: $\frac{k\pi}{2}=\frac{\pi}{2}+2m\pi\Rightarrow k=1+4m$. Syarat 2: $\frac{k\pi}{6}=\frac{3\pi}{2}+2n\pi\Rightarrow k=9+12n$. Nilai bersama terkecil $k=9$ (juga 21, 33, ...).
**Acuan:** siswa — siswa hal.141

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b03-b-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: evaluasi beberapa klaim siswa tentang fungsi sinus*

Diketahui $f(x)=5\sin\frac{x}{2}$. Tiga siswa menyampaikan klaim. Ani: "Periode $f$ adalah $\pi$." Beni: "Nilai maksimum $f$ adalah $5$." Cici: "Nilai $f(\pi)$ adalah $5$." Siswa yang klaimnya benar adalah ....

- A. Hanya Beni  
  <sub>Salah: tidak menguji klaim Cici; padahal $f(\pi)=5\sin\frac{\pi}{2}=5$</sub>
- B. Ani dan Beni  
  <sub>Salah: memakai periode $\frac{2\pi}{2}=\pi$, yaitu mengira $k=2$ padahal $k=\frac{1}{2}$</sub>
- C. Ani dan Cici  
  <sub>Salah: memakai periode $\pi$ dan melewatkan klaim Beni yang benar</sub>
- **D. Beni dan Cici** ✅  
  <sub>Benar: periode $f$ adalah $\frac{2\pi}{1/2}=4\pi$ (klaim Ani salah); maksimum $|a|=5$ (Beni benar); $f(\pi)=5\sin\frac{\pi}{2}=5$ (Cici benar)</sub>

**Pembahasan:** $k=\frac{1}{2}$ sehingga periode $4\pi$: Ani salah. Amplitudo 5 dan $c=0$ sehingga maksimum 5: Beni benar. $f(\pi)=5\sin\frac{\pi}{2}=5$: Cici benar.
**Acuan:** siswa — siswa hal.142

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b03-b-hard-bt01-010
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim titik tak terdefinisi tangen*

Seorang siswa mengklaim: "Untuk setiap bilangan bulat positif $k$, fungsi $y=\tan kx$ tidak terdefinisi pada $x=\frac{\pi}{2}+n\pi$ untuk sembarang bilangan bulat $n$." Fungsi berikut yang merupakan contoh penyangkal klaim tersebut adalah ....

- **A. $y=\tan 2x$** ✅  
  <sub>Benar: di $x=\frac{\pi}{2}$ argumennya $2x=\pi$ dan $\tan\pi=0$ terdefinisi</sub>
- B. $y=\tan x$  
  <sub>Salah: argumen $\frac{\pi}{2}+n\pi$ membuat tangen tidak terdefinisi: klaim berlaku</sub>
- C. $y=\tan 3x$  
  <sub>Salah: argumen $\frac{3\pi}{2}+3n\pi$ adalah kelipatan ganjil $\frac{\pi}{2}$: klaim berlaku</sub>
- D. $y=\tan 5x$  
  <sub>Salah: argumen $\frac{5\pi}{2}+5n\pi$ adalah kelipatan ganjil $\frac{\pi}{2}$: klaim berlaku</sub>

**Pembahasan:** Argumen $kx=\frac{k\pi}{2}+kn\pi$ adalah kelipatan ganjil $\frac{\pi}{2}$ hanya jika $k$ ganjil; untuk $k=2$ argumen $\pi+2n\pi$ sehingga $\tan 2x=0$ terdefinisi.
**Acuan:** siswa — siswa hal.144

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
