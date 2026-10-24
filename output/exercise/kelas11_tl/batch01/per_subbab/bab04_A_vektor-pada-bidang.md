# Lembar koreksi — kelas11_tl SMA11L-B4 subbab A: Vektor pada Bidang

52 soal | easy 20, medium 20, hard 12 | variasi 20, orisinal 32
> **Kapasitas kurang (hard): 12 dari kuota 20** — Acuan variasi habis di easy+medium dan materi subbab hanya menopang soal hard berupa evaluasi klaim, temukan kesalahan, dan rancangan sederhana; soal hitung langsung dibuang agar tidak setara medium.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b04-a-easy-bt01-001
*variasi (angka) | C1 | 1 langkah | jenis: komponen ke bentuk i dan j*

Vektor $\langle 8, -9\rangle$ dapat dituliskan ke dalam kombinasi vektor-vektor satuan baku $\mathbf{i}$ dan $\mathbf{j}$, yaitu ....

- A. $8\mathbf{i} + 9\mathbf{j}$  
  <sub>Salah: mengabaikan tanda negatif pada komponen kedua</sub>
- B. $-9\mathbf{i} + 8\mathbf{j}$  
  <sub>Salah: tertukar urutan komponen i dan j</sub>
- C. $-8\mathbf{i} + 9\mathbf{j}$  
  <sub>Salah: tanda kedua komponen dibalik</sub>
- **D. $8\mathbf{i} - 9\mathbf{j}$** ✅  
  <sub>Benar: komponen pertama 8 menjadi koefisien i dan komponen kedua -9 menjadi koefisien j</sub>

**Pembahasan:** $\langle 8,-9\rangle = 8\mathbf{i} - 9\mathbf{j}$.
**Acuan:** pretest — kelas11_tl-b04-p0191-latihan-a-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b04-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: komponen dan panjang dari dua titik*

Sebuah vektor memiliki pangkal di $(-8, 3)$ dan ujung di $(4, 8)$. Bentuk komponen vektor tersebut dan panjangnya berturut-turut adalah ....

- A. $\langle 5, 12\rangle$ dan $13$  
  <sub>Salah: tertukar urutan komponen x dan y</sub>
- B. $\langle 12, 5\rangle$ dan $17$  
  <sub>Salah: menjumlahkan komponen 12+5 alih-alih akar jumlah kuadrat</sub>
- C. $\langle -12, -5\rangle$ dan $13$  
  <sub>Salah: pangkal dikurangi ujung sehingga tanda terbalik</sub>
- **D. $\langle 12, 5\rangle$ dan $13$** ✅  
  <sub>Benar: komponen (4-(-8), 8-3) = (12,5); panjang akar(144+25)=13</sub>

**Pembahasan:** $\langle 4-(-8), 8-3\rangle = \langle 12,5\rangle$; panjang $\sqrt{12^2+5^2}=13$.
**Acuan:** pretest — kelas11_tl-b04-p0191-latihan-a-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b04-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: komponen dan panjang dari dua titik*

Ruas garis berarah $\mathbf{w}$ berpangkal di $(7, -8)$ dan berujung di $(16, -20)$. Bentuk komponen $\mathbf{w}$ dan panjangnya berturut-turut adalah ....

- **A. $\langle 9, -12\rangle$ dan $15$** ✅  
  <sub>Benar: komponen (16-7, -20-(-8)) = (9,-12); panjang akar(81+144)=15</sub>
- B. $\langle -9, 12\rangle$ dan $15$  
  <sub>Salah: pangkal dikurangi ujung sehingga tanda terbalik</sub>
- C. $\langle -12, 9\rangle$ dan $15$  
  <sub>Salah: tertukar urutan komponen</sub>
- D. $\langle 9, -12\rangle$ dan $21$  
  <sub>Salah: menjumlahkan nilai mutlak komponen 9+12</sub>

**Pembahasan:** $\langle 16-7, -20-(-8)\rangle = \langle 9,-12\rangle$; panjang $\sqrt{81+144}=15$.
**Acuan:** pretest — kelas11_tl-b04-p0191-latihan-a-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b04-a-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: mengenali vektor ekuivalen*

Misalkan $\mathbf{p}$, $\mathbf{q}$, dan $\mathbf{r}$ secara berturut-turut merupakan ruas garis berarah dari $(9, 7)$ ke $(15, 3)$, dari $(-7, 9)$ ke $(-1, 13)$, dan dari $(12, -8)$ ke $(18, -4)$. Pasangan vektor yang ekuivalen adalah ....

- **A. $\mathbf{q}$ dan $\mathbf{r}$** ✅  
  <sub>Benar: komponen $\mathbf{q}=\langle 6,4\rangle$ dan $\mathbf{r}=\langle 6,4\rangle$ sama</sub>
- B. $\mathbf{p}$ dan $\mathbf{r}$  
  <sub>Salah: komponen kedua $\mathbf{p}$ negatif sedangkan $\mathbf{r}$ positif</sub>
- C. $\mathbf{p}$, $\mathbf{q}$, dan $\mathbf{r}$ ketiganya ekuivalen  
  <sub>Salah: mengira panjang sama berarti ekuivalen padahal $\mathbf{p}$ berbeda arah</sub>
- D. $\mathbf{p}$ dan $\mathbf{q}$  
  <sub>Salah: komponen kedua $\mathbf{p}$ adalah $-4$ sehingga arahnya berbeda; hanya panjang yang sama</sub>

**Pembahasan:** $\mathbf{p}=\langle 6,-4\rangle$, $\mathbf{q}=\langle 6,4\rangle$, $\mathbf{r}=\langle 6,4\rangle$. Hanya $\mathbf{q}$ dan $\mathbf{r}$ yang komponennya sama.
**Acuan:** siswa — siswa hal.178 Mari Mencoba 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b04-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: ekuivalen dan panjang ruas garis*

Misalkan $\mathbf{u}$ menggambarkan garis berarah dari titik $(-9, 8)$ ke titik $(15, 18)$, sedangkan $\mathbf{v}$ menggambarkan garis berarah dari titik $(11, 12)$ ke titik $(35, 22)$. Pernyataan yang benar mengenai kedua ruas garis tersebut adalah ....

- A. Keduanya tidak ekuivalen karena titik pangkalnya berbeda  
  <sub>Salah: mengira vektor ekuivalen harus berpangkal sama</sub>
- B. Panjang keduanya 26 tetapi arahnya berbeda  
  <sub>Salah: tidak membandingkan komponen sehingga mengira arah berbeda</sub>
- C. Keduanya ekuivalen dan panjang masing-masing 34  
  <sub>Salah: menjumlahkan komponen 24+10 alih-alih akar jumlah kuadrat</sub>
- **D. Keduanya ekuivalen dan panjang masing-masing 26** ✅  
  <sub>Benar: kedua ruas bekomponen (24,10) sehingga sama arah; panjang akar(576+100)=26</sub>

**Pembahasan:** Komponen $\mathbf{u}=\langle 24,10\rangle$ dan $\mathbf{v}=\langle 24,10\rangle$, panjang $\sqrt{576+100}=26$; keduanya ekuivalen.
**Acuan:** siswa — siswa hal.177 Contoh 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b04-a-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: ekuivalen dan panjang ruas garis*

Dua drone bergerak pada bidang koordinat. Drone pertama terbang dari titik $(5, 9)$ ke titik $(17, 14)$, sedangkan drone kedua terbang dari titik $(-6, 8)$ ke titik $(6, 3)$. Kesimpulan yang tepat mengenai perpindahan kedua drone adalah ....

- A. Perpindahan tidak ekuivalen karena panjangnya berbeda  
  <sub>Salah: mengira panjang berbeda padahal sama-sama 13</sub>
- B. Perpindahan ekuivalen dan panjang masing-masing 17  
  <sub>Salah: menjumlahkan komponen 12+5 dan mengabaikan tanda</sub>
- C. Perpindahan ekuivalen dan panjang masing-masing 13  
  <sub>Salah: tidak memeriksa tanda komponen kedua</sub>
- **D. Panjang perpindahan sama, yaitu 13, tetapi tidak ekuivalen** ✅  
  <sub>Benar: komponen (12,5) dan (12,-5) berbeda arah tetapi panjang sama akar(144+25)=13</sub>

**Pembahasan:** $\langle 12,5\rangle$ dan $\langle 12,-5\rangle$: panjang sama $13$, komponen kedua berlawanan tanda sehingga tidak ekuivalen.
**Acuan:** siswa — siswa hal.177 Contoh 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b04-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: vektor satuan*

Diberikan vektor $\mathbf{v} = \langle -8, 15\rangle$. Berapakah panjang vektor $\mathbf{v}$? Selanjutnya, tentukan vektor $\mathbf{u}$ yang searah dengan vektor $\mathbf{v}$, tetapi memiliki panjang 1 satuan. Jawabannya adalah ....

- A. panjang $7$ dan $\mathbf{u} = \langle -\frac{8}{7}, \frac{15}{7}\rangle$  
  <sub>Salah: menjumlahkan komponen -8+15 sebagai panjang</sub>
- **B. panjang $17$ dan $\mathbf{u} = \langle -\frac{8}{17}, \frac{15}{17}\rangle$** ✅  
  <sub>Benar: panjang akar(64+225)=17; u = v dibagi 17</sub>
- C. panjang $17$ dan $\mathbf{u} = \langle \frac{8}{17}, \frac{15}{17}\rangle$  
  <sub>Salah: tanda komponen pertama hilang</sub>
- D. panjang $17$ dan $\mathbf{u} = \langle -\frac{8}{17}, -\frac{15}{17}\rangle$  
  <sub>Salah: tanda komponen kedua dibalik sehingga arah tidak searah</sub>

**Pembahasan:** $\|\mathbf{v}\|=\sqrt{64+225}=17$, lalu $\mathbf{u}=\frac{1}{17}\mathbf{v}=\langle -\frac{8}{17}, \frac{15}{17}\rangle$.
**Acuan:** siswa — siswa hal.189 Contoh 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b04-a-easy-bt01-008
*variasi (konteks) | C2 | 2 langkah | jenis: vektor satuan*

Kecepatan angin pada suatu bidang koordinat dinyatakan oleh vektor $\mathbf{w} = \langle -7, 24\rangle$ km/jam. Vektor yang searah dengan arah angin tersebut dan memiliki panjang 1 satuan adalah ....

- A. $\langle -\frac{7}{625}, \frac{24}{625}\rangle$  
  <sub>Salah: membagi dengan kuadrat panjang</sub>
- **B. $\langle -\frac{7}{25}, \frac{24}{25}\rangle$** ✅  
  <sub>Benar: panjang akar(49+576)=25; dibagi 25</sub>
- C. $\langle \frac{7}{25}, \frac{24}{25}\rangle$  
  <sub>Salah: tanda komponen pertama hilang</sub>
- D. $\langle -\frac{7}{31}, \frac{24}{31}\rangle$  
  <sub>Salah: memakai jumlah nilai mutlak komponen sebagai panjang</sub>

**Pembahasan:** $\|\mathbf{w}\|=25$, vektor satuan $=\frac{1}{25}\langle -7,24\rangle=\langle -\frac{7}{25}, \frac{24}{25}\rangle$.
**Acuan:** siswa — siswa hal.189 Contoh 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b04-a-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: panjang hasil kali skalar*

Jika $\mathbf{v} = \langle 9, 40\rangle$, tentukan $\|{-5}\mathbf{v}\|$.

- **A. $205$** ✅  
  <sub>Benar: panjang v = 41; panjang (-5)v = |-5| x 41 = 205</sub>
- B. $41$  
  <sub>Salah: lupa mengalikan dengan nilai mutlak skalar</sub>
- C. $-205$  
  <sub>Salah: panjang vektor tidak boleh negatif; tanda skalar terbawa</sub>
- D. $245$  
  <sub>Salah: menjumlahkan komponen -45 dan -200 secara mutlak</sub>

**Pembahasan:** $\|\mathbf{v}\|=\sqrt{81+1600}=41$, sehingga $\|{-5}\mathbf{v}\|=|-5|\cdot 41=205$.
**Acuan:** siswa — siswa hal.187 Contoh 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b04-a-easy-bt01-010
*variasi (konteks) | C1 | 1 langkah | jenis: mengenali besaran vektor*

Manakah besaran berikut yang merupakan vektor?

- A. lama perjalanan 3 jam  
  <sub>Salah: waktu hanya bernilai, tanpa arah (skalar)</sub>
- B. massa sebuah kotak 5 kg  
  <sub>Salah: massa hanya bernilai, tanpa arah (skalar)</sub>
- **C. gaya sebesar 20 N ke arah kanan** ✅  
  <sub>Benar: vektor memiliki nilai dan arah; gaya 20 N ke kanan menyebut keduanya</sub>
- D. suhu ruangan 30 derajat Celsius  
  <sub>Salah: suhu hanya bernilai, tanpa arah (skalar)</sub>

**Pembahasan:** Vektor memiliki besar dan arah; hanya gaya 20 N ke arah kanan yang menyebutkan keduanya.
**Acuan:** siswa — siswa hal.191 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b04-a-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: resultan gaya berlawanan*

Dua orang menarik sebuah peti dengan gaya yang sama besar, yaitu 40 N, tetapi arahnya saling berlawanan. Resultan kedua gaya pada peti tersebut adalah ....

- A. 80 N searah dengan salah satu penarik  
  <sub>Salah: menjumlahkan besar gaya tanpa memperhatikan arah berlawanan</sub>
- B. 20 N searah dengan salah satu penarik  
  <sub>Salah: membagi dua jumlah besar gaya</sub>
- **C. vektor nol** ✅  
  <sub>Benar: komponen kedua gaya saling meniadakan sehingga jumlahnya vektor nol</sub>
- D. 40 N searah dengan salah satu penarik  
  <sub>Salah: mengira satu gaya mengalahkan yang lain</sub>

**Pembahasan:** Dua vektor sama besar berlawanan arah berjumlah vektor nol.
**Acuan:** siswa — siswa hal.191 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b04-a-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: panjang cv*

Diketahui panjang vektor $\mathbf{v}$ adalah 7 dan $c = -3$. Panjang vektor $c\mathbf{v}$ adalah ....

- A. $4$  
  <sub>Salah: menjumlahkan c dan panjang v</sub>
- B. $10$  
  <sub>Salah: menjumlahkan nilai mutlak c dan panjang v</sub>
- **C. $21$** ✅  
  <sub>Benar: panjang cv = |c| x panjang v = 3 x 7 = 21</sub>
- D. $-21$  
  <sub>Salah: panjang vektor tidak boleh negatif; tanda c terbawa</sub>

**Pembahasan:** $\|c\mathbf{v}\|=|c|\,\|\mathbf{v}\|=3\cdot 7=21$.
**Acuan:** siswa — siswa hal.191 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b04-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: vektor nol*

Sebuah vektor memiliki titik pangkal $(-6, 4)$ dan titik ujung $(-6, 4)$. Nama dan bentuk komponen vektor tersebut adalah ....

- A. vektor satuan, $\langle 1, 1\rangle$  
  <sub>Salah: mengira vektor satuan memiliki komponen satu</sub>
- **B. vektor nol, $\langle 0, 0\rangle$** ✅  
  <sub>Benar: pangkal dan ujung sama sehingga komponen (0,0): vektor nol</sub>
- C. vektor posisi baku, $\langle -6, 4\rangle$  
  <sub>Salah: menyalin koordinat titik sebagai komponen</sub>
- D. vektor nol, $\langle -12, 8\rangle$  
  <sub>Salah: menjumlahkan koordinat pangkal dan ujung</sub>

**Pembahasan:** $\langle -6-(-6), 4-4\rangle=\langle 0,0\rangle$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b04-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: penjumlahan vektor*

Diketahui $\mathbf{a} = \langle 11, -6\rangle$ dan $\mathbf{b} = \langle -4, 9\rangle$. Hasil dari $\mathbf{a} + \mathbf{b}$ adalah ....

- **A. $\langle 7, 3\rangle$** ✅  
  <sub>Benar: 11+(-4)=7 dan -6+9=3</sub>
- B. $\langle 7, -15\rangle$  
  <sub>Salah: komponen kedua dikurangkan, hanya komponen pertama dijumlahkan</sub>
- C. $\langle 15, -15\rangle$  
  <sub>Salah: mengurangkan komponen a dengan b</sub>
- D. $\langle -44, -54\rangle$  
  <sub>Salah: mengalikan komponen yang bersesuaian</sub>

**Pembahasan:** $\mathbf{a}+\mathbf{b}=\langle 11+(-4), -6+9\rangle=\langle 7,3\rangle$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b04-a-easy-bt01-015
*orisinal | C2 | 1 langkah | jenis: perkalian skalar dengan vektor*

Jika $\mathbf{w} = \langle 6, -7\rangle$, maka $-3\mathbf{w}$ adalah ....

- A. $\langle -3, -10\rangle$  
  <sub>Salah: menjumlahkan skalar dengan tiap komponen</sub>
- B. $\langle 18, -21\rangle$  
  <sub>Salah: mengalikan dengan 3, bukan -3</sub>
- **C. $\langle -18, 21\rangle$** ✅  
  <sub>Benar: -3 x 6 = -18 dan -3 x (-7) = 21</sub>
- D. $\langle -18, -21\rangle$  
  <sub>Salah: tanda komponen kedua tidak ikut berubah</sub>

**Pembahasan:** $-3\langle 6,-7\rangle=\langle -18,21\rangle$.
**Acuan:** siswa — siswa hal.183

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b04-a-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: mengenali vektor satuan*

Vektor berikut yang merupakan vektor satuan adalah ....

- A. $\langle 1, \frac{1}{13}\rangle$  
  <sub>Salah: hanya komponen pertama bernilai 1, panjangnya lebih dari 1</sub>
- **B. $\langle \frac{5}{13}, \frac{12}{13}\rangle$** ✅  
  <sub>Benar: panjang akar(25/169+144/169)=1</sub>
- C. $\langle \frac{1}{2}, \frac{1}{2}\rangle$  
  <sub>Salah: mengira komponen berjumlah 1 sudah satuan, padahal panjangnya akar(1/2)</sub>
- D. $\langle \frac{5}{6}, \frac{1}{6}\rangle$  
  <sub>Salah: mengira komponen berjumlah 1 sudah satuan, padahal panjang kuadratnya 26/36</sub>

**Pembahasan:** $\left(\frac{5}{13}\right)^2+\left(\frac{12}{13}\right)^2=\frac{169}{169}=1$.
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b04-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: titik ujung dari komponen*

Vektor $\mathbf{v} = \langle 5, 9\rangle$ berpangkal di titik $(3, -7)$. Titik ujung vektor $\mathbf{v}$ adalah ....

- A. $(8, -16)$  
  <sub>Salah: komponen pertama dijumlah tetapi komponen kedua dikurangkan</sub>
- **B. $(8, 2)$** ✅  
  <sub>Benar: ujung = pangkal + komponen = (3+5, -7+9)</sub>
- C. $(2, 16)$  
  <sub>Salah: mengurangkan pangkal dari komponen</sub>
- D. $(-2, -16)$  
  <sub>Salah: mengurangkan komponen dari pangkal</sub>

**Pembahasan:** $(3+5, -7+9)=(8,2)$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b04-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: mengenali vektor ekuivalen*

Vektor $\mathbf{a} = \langle 6, -2\rangle$. Ruas garis berarah yang merepresentasikan vektor yang ekuivalen dengan $\mathbf{a}$ adalah ruas garis ....

- A. dari $(4, 9)$ ke $(7, 10)$  
  <sub>Salah: komponen (3,1), bukan (6,-2)</sub>
- B. dari $(4, 9)$ ke $(16, 5)$  
  <sub>Salah: komponen (12,-4): searah tetapi panjangnya dua kali</sub>
- C. dari $(10, 7)$ ke $(4, 9)$  
  <sub>Salah: pangkal dan ujung tertukar sehingga arah berlawanan</sub>
- **D. dari $(4, 9)$ ke $(10, 7)$** ✅  
  <sub>Benar: komponen (10-4, 7-9) = (6,-2)</sub>

**Pembahasan:** Hanya ruas dari $(4,9)$ ke $(10,7)$ yang berkomponen $\langle 6,-2\rangle$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b04-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: panjang vektor dalam bentuk i dan j*

Panjang vektor $24\mathbf{i} - 7\mathbf{j}$ adalah ....

- A. $\sqrt{527}$  
  <sub>Salah: mengurangkan kuadrat 576-49</sub>
- B. $31$  
  <sub>Salah: menjumlahkan nilai mutlak 24+7</sub>
- **C. $25$** ✅  
  <sub>Benar: komponen (24,-7); panjang akar(576+49)=25</sub>
- D. $17$  
  <sub>Salah: menjumlahkan komponen 24-7</sub>

**Pembahasan:** $\sqrt{24^2+(-7)^2}=\sqrt{625}=25$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b04-a-easy-bt01-020
*orisinal | C2 | 1 langkah | jenis: arah dan panjang kelipatan skalar*

Jika $\mathbf{v}$ adalah vektor tak nol, maka vektor $-2\mathbf{v}$ dibandingkan dengan $\mathbf{v}$ memiliki ....

- **A. panjang dua kali lipat dan arah berlawanan** ✅  
  <sub>Benar: |-2| = 2 menggandakan panjang; skalar negatif membalik arah</sub>
- B. panjang setengah kali dan arah berlawanan  
  <sub>Salah: tertukar antara mengalikan dan membagi dengan 2</sub>
- C. panjang setengah kali dan arah sama  
  <sub>Salah: kedua sifat keliru</sub>
- D. panjang dua kali lipat dan arah sama  
  <sub>Salah: mengabaikan tanda negatif pada arah</sub>

**Pembahasan:** $\|{-2}\mathbf{v}\|=2\|\mathbf{v}\|$ dan arah berlawanan karena skalar negatif.
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b04-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: perpindahan perahu menyeberangi sungai*

Misalkan kamu akan menyeberangi sebuah sungai dengan kecepatan arus 5 m/s. Untuk melakukannya, kamu mengarahkan perahu tegak lurus terhadap arah arus dengan kecepatan 12 m/s. Jika kecepatan keduanya tetap, perpindahan perahu terhadap tepi sungai setelah 10 detik adalah ....

- **A. $130$ m** ✅  
  <sub>Benar: resultan kecepatan $\langle 5,12\rangle$ berbesar 13 m/s; perpindahan 13 x 10 = 130 m</sub>
- B. $70$ m  
  <sub>Salah: mengurangkan besar kedua kecepatan</sub>
- C. $13$ m  
  <sub>Salah: memakai besar kecepatan tanpa dikalikan waktu</sub>
- D. $170$ m  
  <sub>Salah: menjumlahkan besar kecepatan 5+12 alih-alih mencari resultan vektor</sub>

**Pembahasan:** Kecepatan resultan $\langle 5,12\rangle$ dengan besar $\sqrt{25+144}=13$ m/s. Perpindahan setelah 10 detik $=13\cdot 10=130$ m.
**Acuan:** siswa — siswa hal.181 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b04-a-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: kombinasi vektor dalam i dan j*

Diketahui $\mathbf{a} = 7\mathbf{i} - 2\mathbf{j}$ dan $\mathbf{b} = -\mathbf{i} + 4\mathbf{j}$. Bentuk $2\mathbf{a} - 3\mathbf{b}$ dalam vektor-vektor satuan baku adalah ....

- A. $17\mathbf{i} + 8\mathbf{j}$  
  <sub>Salah: komponen j: -4 - 12 salah dihitung menjadi -4 + 12</sub>
- **B. $17\mathbf{i} - 16\mathbf{j}$** ✅  
  <sub>Benar: 2a = 14i - 4j; 3b = -3i + 12j; selisih 17i - 16j</sub>
- C. $11\mathbf{i} + 8\mathbf{j}$  
  <sub>Salah: tanda 3b tidak dibalik (menjumlahkan 3b)</sub>
- D. $15\mathbf{i} - 8\mathbf{j}$  
  <sub>Salah: lupa mengalikan b dengan 3</sub>

**Pembahasan:** $2\mathbf{a}-3\mathbf{b}=(14+3)\mathbf{i}+(-4-12)\mathbf{j}=17\mathbf{i}-16\mathbf{j}$.
**Acuan:** siswa — siswa hal.191

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b04-a-medium-bt01-003
*variasi (konteks) | C3 | 2 langkah | jenis: resultan kecepatan dua arah tegak lurus*

Sebuah drone diarahkan terbang lurus ke utara dengan kecepatan 8 m/s, sedangkan angin berembus tegak lurus ke timur dengan kecepatan 15 m/s. Besar kecepatan gerak drone terhadap tanah adalah ....

- A. $23$ m/s  
  <sub>Salah: menjumlahkan besar kedua kecepatan</sub>
- B. $7$ m/s  
  <sub>Salah: mengurangkan besar kedua kecepatan</sub>
- **C. $17$ m/s** ✅  
  <sub>Benar: komponen resultan $\langle 15,8\rangle$, besar $\sqrt{225+64}=17$</sub>
- D. $289$ m/s  
  <sub>Salah: tidak menarik akar jumlah kuadrat</sub>

**Pembahasan:** $\|\langle 15,8\rangle\|=\sqrt{225+64}=17$ m/s.
**Acuan:** siswa — siswa hal.181 Contoh 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b04-a-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: panjang hasil kombinasi vektor*

Jika $\mathbf{a} = \langle 4, -3\rangle$ dan $\mathbf{b} = \langle -6, 17\rangle$, panjang vektor $3\mathbf{a} + \mathbf{b}$ adalah ....

- A. $14$  
  <sub>Salah: menjumlahkan komponen hasil 6+8 sebagai panjang</sub>
- B. $15$  
  <sub>Salah: hanya menghitung panjang 3a, vektor b terlupa</sub>
- C. $100$  
  <sub>Salah: tidak menarik akar jumlah kuadrat</sub>
- **D. $10$** ✅  
  <sub>Benar: 3a + b = (6,8); panjang 10</sub>

**Pembahasan:** $3\mathbf{a}+\mathbf{b}=\langle 12-6,-9+17\rangle=\langle 6,8\rangle$, panjangnya $10$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b04-a-medium-bt01-005
*variasi (konteks) | C4 | 3 langkah | jenis: resultan kecepatan setelah perubahan*

Sebuah perahu diarahkan tegak lurus terhadap sungai dengan kecepatan 3 m/s, sedangkan arus sungai berkecepatan 2 m/s ke arah kiri. Kemudian kecepatan perahu dijadikan dua kali lipat dan arah arus sungai dibalik menjadi ke kanan dengan besar tetap. Dengan sumbu $x$ positif ke kanan dan sumbu $y$ positif searah gerak perahu, bentuk komponen kecepatan resultan yang baru dan besarnya berturut-turut adalah ....

- **A. $\langle 2, 6\rangle$ dan $2\sqrt{10}$ m/s** ✅  
  <sub>Benar: komponen $\langle 0,6\rangle+\langle 2,0\rangle=\langle 2,6\rangle$; besar $\sqrt{4+36}=2\sqrt{10}$</sub>
- B. $\langle 2, 6\rangle$ dan $8$ m/s  
  <sub>Salah: menjumlahkan komponen 2+6 sebagai besar vektor</sub>
- C. $\langle -2, 6\rangle$ dan $2\sqrt{10}$ m/s  
  <sub>Salah: arus tidak ikut dibalik sehingga komponen pertama tetap -2</sub>
- D. $\langle 2, 3\rangle$ dan $\sqrt{13}$ m/s  
  <sub>Salah: kecepatan perahu tidak digandakan</sub>

**Pembahasan:** Perahu menjadi $\langle 0,6\rangle$, arus $\langle 2,0\rangle$; resultan $\langle 2,6\rangle$ dengan besar $\sqrt{40}=2\sqrt{10}$ m/s.
**Acuan:** siswa — siswa hal.182 Mari Mencoba 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b04-a-medium-bt01-006
*orisinal | C3 | 3 langkah | jenis: titik ujung vektor ekuivalen*

Vektor $\mathbf{p}$ berpangkal di $A(2, -3)$ dan berujung di $B(7, 1)$. Vektor $\mathbf{q}$ berpangkal di $C(-4, 5)$ dan ekuivalen dengan $\mathbf{p}$. Koordinat titik ujung vektor $\mathbf{q}$ adalah ....

- A. $(-9, 1)$  
  <sub>Salah: komponen p dikurangkan dari pangkal q</sub>
- B. $(5, 4)$  
  <sub>Salah: menyalin komponen p sebagai koordinat titik</sub>
- C. $(1, 1)$  
  <sub>Salah: komponen kedua dikurangkan, komponen pertama dijumlahkan</sub>
- **D. $(1, 9)$** ✅  
  <sub>Benar: p = (5,4); ujung q = (-4+5, 5+4) = (1,9)</sub>

**Pembahasan:** $\mathbf{p}=\langle 5,4\rangle$; ekuivalen berarti komponen sama, ujung $\mathbf{q}=(-4+5,5+4)=(1,9)$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b04-a-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: kelipatan skalar dan panjangnya*

Jika $\mathbf{v} = \langle 9, -12\rangle$, maka $-4\mathbf{v}$ dan $\|{-4}\mathbf{v}\|$ berturut-turut adalah ....

- A. $\langle -36, 48\rangle$ dan $15$  
  <sub>Salah: panjang v (15) tidak dikalikan |-4|</sub>
- B. $\langle 5, -16\rangle$ dan $60$  
  <sub>Salah: menjumlahkan -4 pada tiap komponen, bukan mengalikan</sub>
- **C. $\langle -36, 48\rangle$ dan $60$** ✅  
  <sub>Benar: -4v = (-36, 48); panjang akar(1296+2304)=60</sub>
- D. $\langle -36, -48\rangle$ dan $60$  
  <sub>Salah: tanda komponen kedua tidak ikut berubah</sub>

**Pembahasan:** $-4\langle 9,-12\rangle=\langle -36,48\rangle$; $\|{-4}\mathbf{v}\|=|-4|\cdot 15=60$.
**Acuan:** siswa — siswa hal.187 Contoh 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b04-a-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: parameter komponen dari panjang dan kuadran*

Vektor $\mathbf{v} = \langle k, 24\rangle$ berpangkal di titik asal dan memiliki panjang 25. Jika titik ujung $\mathbf{v}$ berada di kuadran II, nilai $k$ adalah ....

- **A. $-7$** ✅  
  <sub>Benar: k^2 + 576 = 625 sehingga k = 7 atau -7; kuadran II (x negatif) memberi k = -7</sub>
- B. $1$  
  <sub>Salah: menganggap k + 24 = 25</sub>
- C. $-1$  
  <sub>Salah: menganggap k + 24 = 25 lalu salah tanda</sub>
- D. $7$  
  <sub>Salah: tidak memperhatikan syarat kuadran II (x harus negatif)</sub>

**Pembahasan:** $k^2+24^2=25^2\Rightarrow k=\pm 7$. Kuadran II berarti absis negatif, jadi $k=-7$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b04-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: menyederhanakan dengan sifat operasi vektor*

Diketahui $\mathbf{u} = \langle 3, -2\rangle$ dan $\mathbf{v} = \langle -1, 5\rangle$. Nilai dari $2(\mathbf{u} - 3\mathbf{v}) + 5\mathbf{v}$ adalah ....

- A. $\langle 17, -59\rangle$  
  <sub>Salah: 6v dan 5v dijumlahkan sehingga menjadi -11v</sub>
- **B. $\langle 7, -9\rangle$** ✅  
  <sub>Benar: 2u - 6v + 5v = 2u - v = (6,-4) - (-1,5) = (7,-9)</sub>
- C. $\langle 4, 6\rangle$  
  <sub>Salah: lupa mengalikan 2 pada -3v sehingga menjadi 2u + 2v</sub>
- D. $\langle 5, 1\rangle$  
  <sub>Salah: tanda -v terbalik</sub>

**Pembahasan:** $2(\mathbf{u}-3\mathbf{v})+5\mathbf{v}=2\mathbf{u}-\mathbf{v}=\langle 6,-4\rangle-\langle -1,5\rangle=\langle 7,-9\rangle$.
**Acuan:** siswa — siswa hal.187

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b04-a-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: kelipatan skalar pecahan dan panjangnya*

Jika $\mathbf{v} = \langle -9, -12\rangle$, tentukan $-\frac{1}{3}\mathbf{v}$ dan $\left\|-\frac{1}{3}\mathbf{v}\right\|$. Jawabannya berturut-turut adalah ....

- A. $\langle 27, 36\rangle$ dan $45$  
  <sub>Salah: mengalikan dengan -3, bukan -1/3</sub>
- B. $\langle -3, -4\rangle$ dan $5$  
  <sub>Salah: tanda skalar negatif diabaikan</sub>
- **C. $\langle 3, 4\rangle$ dan $5$** ✅  
  <sub>Benar: komponen (3,4); panjang 5</sub>
- D. $\langle 3, 4\rangle$ dan $15$  
  <sub>Salah: panjang v (15) dipakai tanpa dikalikan |-1/3|</sub>

**Pembahasan:** $-\frac13\langle -9,-12\rangle=\langle 3,4\rangle$ dan panjangnya $\sqrt{9+16}=5$.
**Acuan:** siswa — siswa hal.187 Contoh 4.5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b04-a-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: resultan dua gaya tegak lurus*

Sebuah objek dikenai gaya dari arah kiri sebesar 72 N dan dari arah bawah sebesar 96 N. Besar resultan gaya pada objek tersebut adalah ....

- A. $14400$ N  
  <sub>Salah: tidak menarik akar jumlah kuadrat</sub>
- B. $168$ N  
  <sub>Salah: menjumlahkan besar kedua gaya</sub>
- **C. $120$ N** ✅  
  <sub>Benar: komponen $\langle 72,96\rangle$; besar akar(5184+9216)=120</sub>
- D. $24$ N  
  <sub>Salah: mengurangkan besar kedua gaya</sub>

**Pembahasan:** $\sqrt{72^2+96^2}=\sqrt{14.400}=120$ N.
**Acuan:** siswa — siswa hal.192 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b04-a-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: vektor searah dengan panjang tertentu*

Vektor $\mathbf{w}$ searah dengan $\mathbf{v} = \langle -6, 8\rangle$ dan memiliki panjang 15. Bentuk komponen $\mathbf{w}$ adalah ....

- A. $\langle 9, -12\rangle$  
  <sub>Salah: arahnya berlawanan dengan v</sub>
- **B. $\langle -9, 12\rangle$** ✅  
  <sub>Benar: panjang v = 10; w = 15 x (v/10) = (-9,12)</sub>
- C. $\langle -90, 120\rangle$  
  <sub>Salah: mengalikan v dengan 15 tanpa normalisasi</sub>
- D. $\langle -3, 4\rangle$  
  <sub>Salah: hanya menormalkan dengan membagi 2, panjang 5 bukan 15</sub>

**Pembahasan:** $\|\mathbf{v}\|=10$, $\mathbf{w}=15\cdot\frac{1}{10}\langle -6,8\rangle=\langle -9,12\rangle$.
**Acuan:** siswa — siswa hal.188

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b04-a-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: gaya seimbang (resultan vektor nol)*

Tiga gaya bekerja pada sebuah benda dan dinyatakan oleh $\mathbf{F}_1 = \langle 3, -5\rangle$ N, $\mathbf{F}_2 = \langle -8, 2\rangle$ N, dan $\mathbf{F}_3$. Agar benda seimbang (resultan ketiga gaya adalah vektor nol), $\mathbf{F}_3$ haruslah ....

- **A. $\langle 5, 3\rangle$ N** ✅  
  <sub>Benar: F1+F2 = (-5,-3); F3 = -(F1+F2) = (5,3)</sub>
- B. $\langle 11, -7\rangle$ N  
  <sub>Salah: mengurangkan F2 dari F1</sub>
- C. $\langle 3, 5\rangle$ N  
  <sub>Salah: komponen hasil tertukar</sub>
- D. $\langle -5, -3\rangle$ N  
  <sub>Salah: memakai F1+F2 tanpa mengambil lawannya</sub>

**Pembahasan:** $\mathbf{F}_1+\mathbf{F}_2=\langle -5,-3\rangle$, sehingga $\mathbf{F}_3=\langle 5,3\rangle$ agar jumlah ketiganya $\mathbf{0}$.
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b04-a-medium-bt01-014
*variasi (konteks) | C3 | 2 langkah | jenis: resultan dua gaya tegak lurus*

Sebuah perahu karet ditarik oleh dua tali. Tali pertama menarik dari arah barat dengan gaya 45 N dan tali kedua dari arah selatan dengan gaya 28 N (arah barat dan selatan saling tegak lurus). Besar resultan gaya pada perahu karet adalah ....

- **A. $53$ N** ✅  
  <sub>Benar: komponen $\langle 45,28\rangle$; besar akar(2025+784)=53</sub>
- B. $73$ N  
  <sub>Salah: menjumlahkan besar kedua gaya</sub>
- C. $17$ N  
  <sub>Salah: mengurangkan besar kedua gaya</sub>
- D. $2.809$ N  
  <sub>Salah: tidak menarik akar jumlah kuadrat</sub>

**Pembahasan:** $\sqrt{45^2+28^2}=\sqrt{2.809}=53$ N.
**Acuan:** siswa — siswa hal.192 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b04-a-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: perpindahan total dari tiga perpindahan*

Seorang pejalan kaki pada bidang koordinat (satuan meter) bergerak tiga kali berturut-turut dengan perpindahan $\langle 10, -3\rangle$, $\langle -4, 11\rangle$, dan $\langle 6, -3\rangle$. Jarak lurus pejalan kaki dari titik awal setelah tiga perpindahan adalah ....

- A. $7$ m  
  <sub>Salah: mengurangkan komponen total 12-5</sub>
- **B. $13$ m** ✅  
  <sub>Benar: total (12,5); panjang 13</sub>
- C. $17$ m  
  <sub>Salah: menjumlahkan komponen total 12+5 sebagai jarak</sub>
- D. $169$ m  
  <sub>Salah: tidak menarik akar jumlah kuadrat</sub>

**Pembahasan:** Total $=\langle 12,5\rangle$, jarak $\sqrt{144+25}=13$ m.
**Acuan:** siswa — siswa hal.180

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b04-a-medium-bt01-016
*orisinal | C4 | 4 langkah | jenis: membandingkan panjang jumlah vektor*

Diketahui $\mathbf{u} = \langle 3, 4\rangle$ dan $\mathbf{v} = \langle 5, 12\rangle$. Pernyataan yang benar mengenai panjang vektor-vektor tersebut adalah ....

- A. $\|\mathbf{u}+\mathbf{v}\| = \|\mathbf{u}\| + \|\mathbf{v}\|$  
  <sub>Salah: mengira panjang jumlah vektor selalu sama dengan jumlah panjang (hanya berlaku bila searah)</sub>
- B. $\|\mathbf{u}+\mathbf{v}\| = \|\mathbf{v}\| - \|\mathbf{u}\|$  
  <sub>Salah: mengurangkan panjang kedua vektor, bukan menjumlahkan komponen</sub>
- C. $\|\mathbf{u}+\mathbf{v}\| > \|\mathbf{u}\| + \|\mathbf{v}\|$  
  <sub>Salah: salah membandingkan akar 320 dengan 18</sub>
- **D. $\|\mathbf{u}+\mathbf{v}\| < \|\mathbf{u}\| + \|\mathbf{v}\|$** ✅  
  <sub>Benar: ||u+v|| = akar 320 = 17,89 < 5 + 13 = 18</sub>

**Pembahasan:** $\mathbf{u}+\mathbf{v}=\langle 8,16\rangle$, $\|\mathbf{u}+\mathbf{v}\|=\sqrt{320}\approx 17{,}89<18=5+13$.
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b04-a-medium-bt01-017
*variasi (angka) | C3 | 2 langkah | jenis: vektor satuan berlawanan arah*

Diberikan vektor $\mathbf{v} = \langle -20, -21\rangle$. Berapakah panjang vektor $\mathbf{v}$? Selanjutnya, tentukan vektor $\mathbf{u}$ yang berlawanan arah dengan vektor $\mathbf{v}$ dan memiliki panjang 1 satuan. Jawabannya adalah ....

- A. panjang $41$ dan $\mathbf{u} = \langle \frac{20}{41}, \frac{21}{41}\rangle$  
  <sub>Salah: menjumlahkan nilai mutlak komponen 20+21 sebagai panjang</sub>
- **B. panjang $29$ dan $\mathbf{u} = \langle \frac{20}{29}, \frac{21}{29}\rangle$** ✅  
  <sub>Benar: panjang akar(400+441)=29; u = -v/29</sub>
- C. panjang $29$ dan $\mathbf{u} = \langle \frac{20}{29}, -\frac{21}{29}\rangle$  
  <sub>Salah: hanya satu tanda komponen yang dibalik</sub>
- D. panjang $29$ dan $\mathbf{u} = \langle -\frac{20}{29}, -\frac{21}{29}\rangle$  
  <sub>Salah: memakai vektor satuan yang searah, bukan berlawanan</sub>

**Pembahasan:** $\|\mathbf{v}\|=\sqrt{400+441}=29$; searah $=\langle -\frac{20}{29},-\frac{21}{29}\rangle$, berlawanan arah $=\langle \frac{20}{29},\frac{21}{29}\rangle$.
**Acuan:** siswa — siswa hal.189 Contoh 4.6
**Catatan generator:** variasi dengan tambahan tuntutan arah berlawanan (setingkat medium)

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b04-a-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: panjang dan arah kelipatan skalar pecahan*

Vektor $\mathbf{v}$ memiliki panjang 13 dan $\mathbf{w} = -\frac{4}{13}\mathbf{v}$. Pernyataan yang benar mengenai $\mathbf{w}$ adalah ....

- A. panjang $\mathbf{w}$ adalah 4 dan arahnya searah dengan $\mathbf{v}$  
  <sub>Salah: mengabaikan tanda negatif pada arah</sub>
- B. panjang $\mathbf{w}$ adalah 52 dan arahnya berlawanan dengan $\mathbf{v}$  
  <sub>Salah: mengalikan 13 dengan 4 dan tidak memakai pembagi 13</sub>
- **C. panjang $\mathbf{w}$ adalah 4 dan arahnya berlawanan dengan $\mathbf{v}$** ✅  
  <sub>Benar: ||w|| = 4/13 x 13 = 4; skalar negatif membalik arah</sub>
- D. panjang $\mathbf{w}$ adalah $\frac{4}{13}$ dan arahnya berlawanan dengan $\mathbf{v}$  
  <sub>Salah: lupa mengalikan |c| dengan panjang v</sub>

**Pembahasan:** $\|\mathbf{w}\|=\left|-\frac{4}{13}\right|\cdot 13=4$; $c<0$ sehingga arah berlawanan.
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b04-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: vektor satuan dari jumlah dua vektor*

Diketahui $\mathbf{a} = \langle -9, 5\rangle$ dan $\mathbf{b} = \langle 4, 7\rangle$. Vektor satuan yang searah dengan $\mathbf{a} + \mathbf{b}$ adalah ....

- A. $\langle -\frac{5}{17}, \frac{12}{17}\rangle$  
  <sub>Salah: membagi dengan jumlah nilai mutlak komponen 5+12</sub>
- B. $\langle \frac{5}{13}, \frac{12}{13}\rangle$  
  <sub>Salah: tanda komponen pertama hilang</sub>
- C. $\langle -\frac{5}{169}, \frac{12}{169}\rangle$  
  <sub>Salah: membagi dengan kuadrat panjang</sub>
- **D. $\langle -\frac{5}{13}, \frac{12}{13}\rangle$** ✅  
  <sub>Benar: a+b = (-5,12), panjang 13, vektor satuan (-5/13, 12/13)</sub>

**Pembahasan:** $\mathbf{a}+\mathbf{b}=\langle -5,12\rangle$, panjang $13$, sehingga vektor satuannya $\langle -\frac{5}{13},\frac{12}{13}\rangle$.
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b04-a-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: mencari skalar dari persamaan vektor*

Diketahui $\mathbf{a} = \langle 2, -3\rangle$ dan $\mathbf{b} = \langle -1, 4\rangle$. Jika $2\mathbf{a} + c\mathbf{b} = \langle 6, -14\rangle$, nilai $c$ adalah ....

- A. $2$  
  <sub>Salah: salah tanda pada komponen pertama: 4 + c = 6</sub>
- B. $-4$  
  <sub>Salah: komponen pertama dihitung tanpa mengalikan 2 pada a: 2 - c = 6</sub>
- C. $10$  
  <sub>Salah: salah memindah ruas pada 4 - c = 6</sub>
- **D. $-2$** ✅  
  <sub>Benar: 2a + cb = (4-c, -6+4c) = (6,-14) sehingga c = -2 (kedua komponen terpenuhi)</sub>

**Pembahasan:** Komponen pertama $4-c=6\Rightarrow c=-2$; komponen kedua $-6+4c=-14\Rightarrow c=-2$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b04-a-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: evaluasi kapan panjang jumlah sama dengan jumlah panjang*

Diketahui $\mathbf{u} = \langle 3, -4\rangle$. Vektor $\mathbf{v}$ yang membuat $\|\mathbf{u}+\mathbf{v}\| = \|\mathbf{u}\| + \|\mathbf{v}\|$ berlaku adalah ....

- A. $\mathbf{v} = \langle -6, 8\rangle$  
  <sub>Salah: berlawanan arah dengan u: panjang jumlah 5, bukan 15</sub>
- B. $\mathbf{v} = \langle 4, 3\rangle$  
  <sub>Salah: dipilih karena panjangnya 5 sama dengan u, padahal tidak searah: panjang jumlah akar 50</sub>
- **C. $\mathbf{v} = \langle 6, -8\rangle$** ✅  
  <sub>Benar: v = 2u searah dengan u: u+v = (9,-12), panjang 15 = 5 + 10</sub>
- D. $\mathbf{v} = \langle 3, 4\rangle$  
  <sub>Salah: komponen ditukar tanda: u+v = (6,0) berpanjang 6, bukan 10</sub>

**Pembahasan:** Kesamaan terjadi hanya bila kedua vektor searah (v kelipatan positif u). $\langle 6,-8\rangle=2\mathbf{u}$: $\|\mathbf{u}+\mathbf{v}\|=\|\langle 9,-12\rangle\|=15=5+10$. Untuk $\langle -6,8\rangle$ jumlahnya $\langle -3,4\rangle$ (5); $\langle 4,3\rangle$ memberi $\langle 7,-1\rangle$ ($\sqrt{50}\ne 10$); $\langle 3,4\rangle$ memberi $\langle 6,0\rangle$ (6).
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b04-a-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: evaluasi arah dua vektor sejajar dengan parameter*

Diketahui $\mathbf{a} = \langle k, 2\rangle$ dan $\mathbf{b} = \langle 8, k\rangle$. Kedua vektor sejajar bila $k^2 = 16$. Pernyataan yang benar mengenai $k$ adalah ....

- A. $k = 4$ dan $k = -4$ sama-sama membuat keduanya searah  
  <sub>Salah: mengira sejajar selalu berarti searah</sub>
- B. $k = 4$ membuat keduanya berlawanan arah, $k = -4$ membuatnya searah  
  <sub>Salah: arah kedua akar tertukar</sub>
- C. $k = 4$ dan $k = -4$ sama-sama membuat keduanya berlawanan arah  
  <sub>Salah: mengira sejajar selalu berarti berlawanan arah</sub>
- **D. $k = 4$ membuat $\mathbf{a}$ dan $\mathbf{b}$ searah, $k = -4$ membuatnya berlawanan arah** ✅  
  <sub>Benar: k=4: a=(4,2), b=(8,4)=2a searah; k=-4: a=(-4,2), b=(8,-4)=-2a berlawanan</sub>

**Pembahasan:** Sejajar berarti $\mathbf{b}=c\mathbf{a}$. Untuk $k=4$: $\mathbf{a}=\langle 4,2\rangle$, $\mathbf{b}=\langle 8,4\rangle=2\mathbf{a}$ ($c>0$, searah). Untuk $k=-4$: $\mathbf{a}=\langle -4,2\rangle$, $\mathbf{b}=\langle 8,-4\rangle=-2\mathbf{a}$ ($c<0$, berlawanan).
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b04-a-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: menemukan kesalahan langkah panjang vektor*

Seorang siswa menyelesaikan soal "vektor $\mathbf{v} = \langle t, t+7\rangle$ memiliki panjang 13" dengan menulis $t + (t+7) = 13$, sehingga $t = 3$. Penilaian yang tepat atas jawaban siswa tersebut adalah ....

- A. benar, karena panjang vektor sama dengan jumlah kedua komponennya  
  <sub>Salah: menganggap panjang vektor adalah jumlah komponen</sub>
- **B. salah, karena panjang bukan jumlah komponen; nilai $t$ yang benar adalah $5$ atau $-12$** ✅  
  <sub>Benar: t^2 + (t+7)^2 = 169 menjadi t^2 + 7t - 60 = 0, akar 5 dan -12</sub>
- C. salah, karena panjang bukan jumlah komponen; nilai $t$ yang benar adalah $12$ atau $-5$  
  <sub>Salah: akar kuadrat salah tanda</sub>
- D. salah, karena panjang bukan jumlah komponen; nilai $t$ yang benar hanya $5$  
  <sub>Salah: mengabaikan akar negatif -12 yang juga memenuhi</sub>

**Pembahasan:** Panjang $\langle t,t+7\rangle$ adalah $\sqrt{t^2+(t+7)^2}$. Dari $2t^2+14t+49=169$ diperoleh $t^2+7t-60=0$, $(t-5)(t+12)=0$. Jadi $t=5$ atau $t=-12$; $t=3$ memberi $\langle 3,10\rangle$ berpanjang $\sqrt{109}\ne 13$.
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b04-a-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: menemukan langkah salah resultan*

Diketahui $\mathbf{a} = \langle 4,-1\rangle$, $\mathbf{b} = \langle -2,5\rangle$, dan $\mathbf{c} = \langle 3,-3\rangle$. Seorang siswa menghitung $2\mathbf{a} - \mathbf{b} + \mathbf{c}$ sebagai berikut.

Langkah 1: $2\mathbf{a} = \langle 8,-2\rangle$.
Langkah 2: $-\mathbf{b} = \langle 2,-5\rangle$.
Langkah 3: komponen pertama $= 8 + 2 + 3 = 13$.
Langkah 4: komponen kedua $= -2 + (-5) + 3 = -4$.

Hasil siswa: $\langle 13,-4\rangle$. Kesalahan pertama terjadi pada ....

- **A. Langkah 4: komponen kedua $\mathbf{c}$ adalah $-3$, bukan $+3$** ✅  
  <sub>Benar: komponen kedua benar -2-5-3 = -10, hasil yang benar (13,-10)</sub>
- B. Langkah 2: $-\mathbf{b}$ seharusnya $\langle -2,5\rangle$  
  <sub>Salah: keliru: -b = (2,-5) sudah benar, lawan dari b</sub>
- C. Langkah 1: $2\mathbf{a}$ seharusnya $\langle 8,-1\rangle$  
  <sub>Salah: keliru: 2a = (8,-2) sudah benar</sub>
- D. Langkah 3: komponen pertama seharusnya $8 - 2 + 3 = 9$  
  <sub>Salah: keliru: -b memberi +2 sehingga 8+2+3 = 13 sudah benar</sub>

**Pembahasan:** $2\mathbf{a}=\langle 8,-2\rangle$ dan $-\mathbf{b}=\langle 2,-5\rangle$ benar, komponen pertama $8+2+3=13$ benar. Komponen kedua seharusnya $-2-5+(-3)=-10$, sehingga hasil benar $\langle 13,-10\rangle$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b04-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: membandingkan dua cara menentukan waktu menyeberang*

Sebuah perahu diarahkan tegak lurus tepi sungai dengan kecepatan 4 m/s menyeberangi sungai selebar 120 m. Arus sungai 3 m/s sejajar tepi. Dina menghitung waktu menyeberang dengan $120 \div 5$ karena kecepatan resultan perahu 5 m/s. Eka menghitung dengan $120 \div 4$. Pernyataan yang benar adalah ....

- A. Eka benar: waktu menyeberang 30 detik dan perahu terhanyut 150 m sepanjang tepi  
  <sub>Salah: hanyutan dihitung dengan kecepatan resultan 5 x 30, padahal itu panjang lintasan</sub>
- **B. Eka benar: waktu menyeberang 30 detik dan perahu terhanyut 90 m sepanjang tepi** ✅  
  <sub>Benar: lebar sungai ditempuh oleh komponen tegak lurus 4 m/s: t = 120/4 = 30 s; hanyut = 3 x 30 = 90 m</sub>
- C. Dina benar: waktu menyeberang 24 detik dan perahu terhanyut 72 m sepanjang tepi  
  <sub>Salah: memakai kecepatan resultan untuk jarak tegak lurus tepi, padahal lebar sungai dilalui komponen 4 m/s</sub>
- D. Eka benar: waktu menyeberang 30 detik dan perahu terhanyut 120 m sepanjang tepi  
  <sub>Salah: waktu benar tetapi hanyutan disamakan dengan lebar sungai</sub>

**Pembahasan:** Jarak tegak lurus tepi (120 m) hanya dilalui komponen kecepatan perahu 4 m/s, jadi $t=120/4=30$ s. Selama itu arus menggeser $3\cdot 30=90$ m. Resultan $\langle 3,4\rangle$ berbesar 5 m/s menempuh lintasan miring $5\cdot 30=150$ m, bukan hanyutan.
**Acuan:** siswa — siswa hal.181

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b04-a-hard-bt01-006
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim panjang kelipatan skalar*

Seorang siswa menyimpulkan bahwa $\|c\mathbf{v}\| = c\,\|\mathbf{v}\|$ berlaku untuk setiap skalar $c$ dan vektor $\mathbf{v}$. Contoh penyangkal klaim tersebut adalah ....

- A. $c = 2$ dan $\mathbf{v} = \langle -6, 8\rangle$  
  <sub>Salah: keduanya bernilai 20 sehingga klaim terpenuhi; tanda komponen vektor bukan penyebab klaim gagal</sub>
- **B. $c = -3$ dan $\mathbf{v} = \langle 5, -12\rangle$** ✅  
  <sub>Benar: ||cv|| = 39 sedangkan c||v|| = -3 x 13 = -39, tidak sama</sub>
- C. $c = 0$ dan $\mathbf{v} = \langle 5, 12\rangle$  
  <sub>Salah: keduanya bernilai 0 sehingga klaim terpenuhi</sub>
- D. $c = 3$ dan $\mathbf{v} = \langle 5, -12\rangle$  
  <sub>Salah: keduanya bernilai 39 sehingga klaim terpenuhi, bukan penyangkal</sub>

**Pembahasan:** Yang benar $\|c\mathbf{v}\|=|c|\,\|\mathbf{v}\|$. Klaim hanya gagal bila $c<0$: $c=-3$, $\mathbf{v}=\langle 5,-12\rangle$ memberi $\|c\mathbf{v}\|=\|\langle -15,36\rangle\|=39$, sedangkan $c\|\mathbf{v}\|=-39$.
**Acuan:** siswa — siswa hal.187

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b04-a-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: menilai kemungkinan panjang jumlah dua vektor*

Vektor $\mathbf{u}$ berpanjang 5 dan vektor $\mathbf{v}$ berpanjang 12, arah keduanya tidak diketahui. Nilai $\|\mathbf{u}+\mathbf{v}\|$ yang TIDAK mungkin terjadi adalah ....

- **A. $18$** ✅  
  <sub>Benar: panjang jumlah paling besar 5+12 = 17 (searah) dan paling kecil 12-5 = 7 (berlawanan)</sub>
- B. $8$  
  <sub>Salah: mungkin: berada di antara 7 dan 17 (sudut tertentu antara u dan v)</sub>
- C. $13$  
  <sub>Salah: mungkin: terjadi bila u dan v saling tegak lurus (akar 25+144)</sub>
- D. $16$  
  <sub>Salah: mungkin: berada di antara 7 dan 17</sub>

**Pembahasan:** Menyambung pangkal $\mathbf{v}$ pada ujung $\mathbf{u}$, panjang jumlah berkisar dari $12-5=7$ (berlawanan arah) sampai $5+12=17$ (searah). Jadi $8$, $13$, $16$ mungkin, sedangkan $18>17$ tidak mungkin.
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b04-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: membandingkan jumlah panjang dan panjang jumlah perpindahan*

Seorang pelari bergerak dua tahap dengan perpindahan $\langle 12, 5\rangle$ m lalu $\langle -12, 16\rangle$ m. Andi menghitung jarak pelari dari titik awal dengan menjumlahkan panjang kedua perpindahan, sedangkan Budi menjumlahkan vektornya dulu lalu mencari panjangnya. Pernyataan yang benar adalah ....

- A. Keduanya benar karena jumlah panjang vektor selalu sama dengan panjang jumlah vektor  
  <sub>Salah: mengira ||p1+p2|| = ||p1|| + ||p2|| selalu berlaku</sub>
- B. Budi benar: jarak lurus dari titik awal 21 m, sedangkan 33 m adalah selisih panjang kedua perpindahan  
  <sub>Salah: angka 33 bukan selisih; selisihnya 7, 33 adalah jumlah panjang</sub>
- **C. Budi benar: jarak lurus dari titik awal 21 m, sedangkan 33 m adalah panjang lintasan yang ditempuh** ✅  
  <sub>Benar: p1+p2 = (0,21) panjang 21; 13 + 20 = 33 adalah total jarak tempuh</sub>
- D. Andi benar: jarak lurus dari titik awal 33 m, sedangkan 21 m adalah panjang lintasan yang ditempuh  
  <sub>Salah: menukar arti jarak lurus (perpindahan) dengan jarak tempuh</sub>

**Pembahasan:** Perpindahan total $\langle 0,21\rangle$ sehingga jarak lurus dari titik awal $=21$ m (cara Budi). Jumlah panjang $13+20=33$ m adalah panjang lintasan yang ditempuh, lebih besar karena kedua perpindahan tidak searah.
**Acuan:** siswa — siswa hal.180

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b04-a-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: menilai pernyataan hubungan dua vektor*

Diketahui $\mathbf{a} = \langle 4, -10\rangle$ dan $\mathbf{b} = \langle -6, 15\rangle$. Pernyataan yang benar mengenai kedua vektor tersebut adalah ....

- **A. $\mathbf{b}$ berlawanan arah dengan $\mathbf{a}$ dan panjangnya $\frac{3}{2}$ kali panjang $\mathbf{a}$** ✅  
  <sub>Benar: b = -3/2 a: skalar negatif membalik arah, panjang |-3/2| x ||a||</sub>
- B. $\mathbf{b}$ searah dengan $\mathbf{a}$ dan panjangnya $\frac{3}{2}$ kali panjang $\mathbf{a}$  
  <sub>Salah: mengabaikan tanda negatif skalar sehingga arah dikira sama</sub>
- C. $\mathbf{b}$ berlawanan arah dengan $\mathbf{a}$ dan panjangnya $\frac{9}{4}$ kali panjang $\mathbf{a}$  
  <sub>Salah: kuadrat skalar dipakai sebagai faktor panjang</sub>
- D. $\mathbf{b}$ berlawanan arah dengan $\mathbf{a}$ dan panjangnya $\frac{2}{3}$ kali panjang $\mathbf{a}$  
  <sub>Salah: perbandingan terbalik: a dibagi b</sub>

**Pembahasan:** $\mathbf{b}=-\frac32\mathbf{a}$ karena $-\frac32\cdot4=-6$ dan $-\frac32\cdot(-10)=15$. Skalar negatif membalik arah dan $\|\mathbf{b}\|=\frac32\|\mathbf{a}\|$.
**Acuan:** siswa — siswa hal.184

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b04-a-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: merancang kecepatan perahu dan arus memenuhi dua syarat*

Sebuah perahu diarahkan tegak lurus tepi sungai. Kecepatan perahu (terhadap air) dan kecepatan arus sejajar tepi dipilih bilangan bulat dalam m/s, dengan arus tidak nol. Rancangan yang menghasilkan kecepatan resultan tepat 13 m/s dan perahu lebih cepat daripada arus adalah kecepatan perahu dan arus berturut-turut ....

- A. $9$ m/s dan $4$ m/s  
  <sub>Salah: perahu lebih cepat tetapi resultan akar 97, bukan 13</sub>
- B. $5$ m/s dan $12$ m/s  
  <sub>Salah: resultan 13 terpenuhi tetapi perahu lebih lambat daripada arus</sub>
- C. $13$ m/s dan $0$ m/s  
  <sub>Salah: resultan 13 terpenuhi tetapi arus nol, melanggar syarat arus tidak nol</sub>
- **D. $12$ m/s dan $5$ m/s** ✅  
  <sub>Benar: 12^2 + 5^2 = 169 = 13^2 dan 12 > 5</sub>

**Pembahasan:** Resultan $\langle v_a,v_p\rangle$ berbesar $\sqrt{v_a^2+v_p^2}=13$. Pasangan bulat positif: $(5,12)$ atau $(12,5)$; syarat perahu lebih cepat dari arus memilih perahu $12$, arus $5$. $(9,4)$ memberi $\sqrt{97}$; $(13,0)$ ditolak karena arus nol.
**Acuan:** siswa — siswa hal.181

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b04-a-hard-bt01-011
*orisinal | C5 | 3 langkah | jenis: contoh penyangkal klaim vektor berpanjang sama*

Seorang siswa menyimpulkan bahwa dua vektor yang berpanjang sama pasti ekuivalen. Contoh penyangkal yang tepat adalah $\mathbf{v} = \langle 5, -12\rangle$ dan ....

- A. $\mathbf{w} = \langle 5, -12\rangle$ yang digambar dari titik pangkal lain  
  <sub>Salah: panjang dan arahnya sama sehingga ekuivalen, bukan penyangkal</sub>
- B. $\mathbf{w} = \langle 10, -24\rangle$  
  <sub>Salah: arah sama tetapi panjangnya 26, bukan 13; panjang tidak sama</sub>
- C. $\mathbf{w} = \langle 6, -13\rangle$  
  <sub>Salah: panjangnya akar 205, bukan 13; panjang tidak sama</sub>
- **D. $\mathbf{w} = \langle 12, 5\rangle$** ✅  
  <sub>Benar: ||w|| = 13 = ||v|| tetapi komponennya berbeda sehingga arahnya berbeda: tidak ekuivalen</sub>

**Pembahasan:** Ekuivalen menuntut panjang DAN arah sama (komponen sama). $\|\langle 12,5\rangle\|=13=\|\mathbf{v}\|$ tetapi $\langle 12,5\rangle\ne\langle 5,-12\rangle$. Pilihan lain: komponen sama (ekuivalen), atau panjang berbeda ($26$ dan $\sqrt{205}$).
**Acuan:** siswa — siswa hal.178

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b04-a-hard-bt01-012
*orisinal | C5 | 3 langkah | jenis: penyangkal klaim ciri vektor satuan*

Seorang siswa menyimpulkan bahwa vektor $\langle p, q\rangle$ yang memenuhi $|p| + |q| = 1$ pasti merupakan vektor satuan. Contoh penyangkal klaim tersebut adalah ....

- A. $\langle 1, 0\rangle$  
  <sub>Salah: |p|+|q| = 1 dan panjangnya 1, sehingga klaim terpenuhi</sub>
- B. $\langle 0, -1\rangle$  
  <sub>Salah: |p|+|q| = 1 dan panjangnya 1, sehingga klaim terpenuhi</sub>
- **C. $\left\langle \frac{1}{2}, \frac{1}{2}\right\rangle$** ✅  
  <sub>Benar: |1/2|+|1/2| = 1 tetapi panjangnya akar(1/4+1/4) = akar(1/2), bukan 1</sub>
- D. $\left\langle \frac{3}{5}, \frac{4}{5}\right\rangle$  
  <sub>Salah: vektor satuan, tetapi |p|+|q| = 7/5 sehingga premis tidak terpenuhi</sub>

**Pembahasan:** Vektor satuan bila $p^2+q^2=1$, bukan $|p|+|q|=1$. $\langle\frac12,\frac12\rangle$ memenuhi premis tetapi panjangnya $\sqrt{1/2}\ne1$. $\langle\frac35,\frac45\rangle$ satuan namun premisnya gagal; $\langle 0,-1\rangle$ dan $\langle 1,0\rangle$ memenuhi premis dan satuan.
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
