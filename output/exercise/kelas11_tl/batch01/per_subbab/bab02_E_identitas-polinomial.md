# Lembar koreksi — kelas11_tl SMA11L-B2 subbab E: Identitas Polinomial

43 soal | easy 20, medium 16, hard 7 | variasi 19, orisinal 24
> **Kapasitas kurang (medium): 16 dari kuota 20** — Subbab E (Identitas Polinomial) hanya 5 halaman dengan satu sifat (7 identitas) dan dua contoh; soal medium yang layak hanya lewat faktorisasi bentuk tersusun, parameter koefisien, nilai numerik dengan identitas, dan evaluasi klaim. Soal tambahan akan menjadi kembar berangka beda atau berpindah ke hard.
> **Kapasitas kurang (hard): 7 dari kuota 20** — Subbab E (Identitas Polinomial) hanya 5 halaman dengan satu sifat (7 identitas) dan dua contoh; setelah easy (20) dan medium (16), bahan hard yang bernalar sungguhan hanya Latihan E no.7 (tripel Pythagoras), evaluasi klaim/contoh penyangkal, penyamaan koefisien, dan faktorisasi non-standar. Soal tambahan akan menjadi kembar berangka beda atau hanya hitung langsung.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b02-e-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: menguji identitas dengan nilai variabel*

Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $5(x-2)^2 = (5x-10)^2$

- **A. Bukan identitas, karena untuk $x=3$ ruas kiri bernilai 5 sedangkan ruas kanan bernilai 25** ✅  
  <sub>Benar: Untuk $x=3$: ruas kiri $5(1)^2=5$, ruas kanan $(15-10)^2=25$; ada satu nilai yang membuat kedua ruas tidak sama.</sub>
- B. Bukan identitas, karena untuk $x=3$ kedua ruas sama-sama bernilai 25  
  <sub>Salah: salah hitung ruas kiri: lupa mengalikan 5 dengan kuadrat $(x-2)$ yang bernilai 1</sub>
- C. Identitas, karena kedua ruas sama-sama berbentuk kuadrat  
  <sub>Salah: bentuk yang mirip dikira otomatis identik</sub>
- D. Identitas, karena untuk $x=2$ kedua ruas sama-sama bernilai 0  
  <sub>Salah: hanya menguji satu nilai yang kebetulan cocok lalu menyimpulkan berlaku untuk semua $x$</sub>

**Pembahasan:** Uji $x=3$: kiri $5(3-2)^2=5$, kanan $(5\cdot3-10)^2=25$. Karena $5\neq25$, persamaan bukan identitas.
**Acuan:** pretest — kelas11_tl-b02-p0106-latihan-e-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b02-e-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menguji identitas dengan penjabaran*

Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $8(x+4)^2 = 8x^2 + 64x + 128$

- A. Bukan identitas, karena pangkat tertinggi kedua ruas berbeda  
  <sub>Salah: salah membaca pangkat; kedua ruas sama-sama berpangkat 2</sub>
- B. Bukan identitas, karena untuk $x=0$ ruas kiri bernilai 128 sedangkan ruas kanan bernilai 0  
  <sub>Salah: salah hitung ruas kanan: untuk $x=0$ ruas kanan bernilai 128</sub>
- **C. Identitas, karena ruas kiri dijabarkan menjadi $8x^2 + 64x + 128$** ✅  
  <sub>Benar: $8(x+4)^2 = 8(x^2+8x+16) = 8x^2+64x+128$, sama dengan ruas kanan untuk setiap $x$.</sub>
- D. Bukan identitas, karena suku tengah ruas kanan seharusnya $32x$  
  <sub>Salah: salah menghitung suku tengah: $8\cdot2\cdot4x=64x$, bukan $32x$</sub>

**Pembahasan:** $(x+4)^2=x^2+8x+16$, dikalikan 8 menjadi $8x^2+64x+128$ sehingga kedua ruas identik.
**Acuan:** pretest — kelas11_tl-b02-p0106-latihan-e-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b02-e-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: nilai kedua ruas pada nilai variabel*

Diberikan persamaan polinomial $(6b-7)(6b+7) = 36b^2 - 84b + 49$. Jika dipilih $b=0$, nilai ruas kiri dan nilai ruas kanan berturut-turut adalah ....

- A. $49$ dan $49$  
  <sub>Salah: salah tanda: $(-7)(7)$ dianggap bernilai positif</sub>
- **B. $-49$ dan $49$** ✅  
  <sub>Benar: ruas kiri $(0-7)(0+7)=-49$; ruas kanan $0-0+49=49$.</sub>
- C. $-49$ dan $-49$  
  <sub>Salah: ruas kanan dianggap ikut negatif karena tertukar tanda dengan ruas kiri</sub>
- D. $49$ dan $-49$  
  <sub>Salah: kedua nilai tertukar tempat</sub>

**Pembahasan:** Substitusi $b=0$: kiri $(-7)(7)=-49$, kanan $49$. Karena berbeda, persamaan itu bukan identitas.
**Acuan:** siswa — siswa hal.104 Contoh 2.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b02-e-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: menguji identitas dengan penjabaran*

Diberikan persamaan polinomial $(5u^2 - 3v)^2 = 25u^4 - 15u^2v + 9v^2$. Pernyataan yang benar adalah ....

- A. Bukan identitas, karena suku pertama seharusnya $25u^2$  
  <sub>Salah: salah pangkat: $(5u^2)^2=25u^4$</sub>
- B. Identitas, karena suku pertama dan suku ketiga sudah benar  
  <sub>Salah: hanya memeriksa dua suku dari tiga suku</sub>
- C. Bukan identitas, karena suku ketiga seharusnya $9v$  
  <sub>Salah: salah pangkat: $(3v)^2=9v^2$</sub>
- **D. Bukan identitas, karena suku tengah seharusnya $-30u^2v$** ✅  
  <sub>Benar: $(5u^2-3v)^2 = 25u^4 - 2(5u^2)(3v) + 9v^2 = 25u^4 - 30u^2v + 9v^2$.</sub>

**Pembahasan:** Penjabaran benar adalah $25u^4-30u^2v+9v^2$; suku tengah pada soal $-15u^2v$ berbeda, sehingga bukan identitas.
**Acuan:** siswa — siswa hal.104 Contoh 2.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b02-e-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: menguji identitas dengan penjabaran*

Diberikan persamaan polinomial $(t+4)^3 = t^3 + 12t^2 + 48t + 64$. Pernyataan yang benar adalah ....

- A. Bukan identitas, karena $(t+4)^3 = t^3 + 64$  
  <sub>Salah: mengira pangkat tiga hanya memangkatkan tiap suku</sub>
- **B. Identitas, karena $(t+4)^3 = t^3 + 3\cdot4\,t^2 + 3\cdot16\,t + 64$** ✅  
  <sub>Benar: $(t+4)^3 = t^3 + 3t^2(4) + 3t(4^2) + 4^3 = t^3+12t^2+48t+64$.</sub>
- C. Bukan identitas, karena suku konstanta seharusnya $12$  
  <sub>Salah: mengira konstanta $4\cdot3$ bukan $4^3$</sub>
- D. Bukan identitas, karena suku tengahnya seharusnya $4t^2 + 16t$  
  <sub>Salah: mengira koefisien tidak mengandung faktor 3</sub>

**Pembahasan:** Sifat 2.6 nomor 6 memberi $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ dengan $a=t$, $b=4$: hasilnya persis ruas kanan.
**Acuan:** siswa — siswa hal.105 Mari Mencoba 2.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b02-e-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: melengkapi koefisien identitas*

Agar persamaan $(m+5)^3 = m^3 + km^2 + 75m + 125$ merupakan identitas polinomial, nilai $k$ adalah ....

- **A. $15$** ✅  
  <sub>Benar: $(m+5)^3 = m^3 + 3(5)m^2 + 3(25)m + 125$, sehingga $k = 15$ (suku $75m$ dan $125$ cocok).</sub>
- B. $25$  
  <sub>Salah: mengambil $b^2$ saja tanpa faktor 3</sub>
- C. $5$  
  <sub>Salah: mengambil $b$ saja tanpa faktor 3</sub>
- D. $75$  
  <sub>Salah: tertukar dengan koefisien suku $m$</sub>

**Pembahasan:** Koefisien $m^2$ pada $(m+5)^3$ adalah $3\cdot5=15$.
**Acuan:** siswa — siswa hal.105 Mari Mencoba 2.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b02-e-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: menguji identitas dengan penjabaran*

Diberikan persamaan polinomial $(8y-9)^2 + 4 = 64y^2 - 144y + 84$. Pernyataan yang benar adalah ....

- A. Bukan identitas, karena suku $-144y$ seharusnya $-72y$  
  <sub>Salah: lupa mengalikan 2 pada suku tengah $2\cdot8\cdot9$ dengan benar</sub>
- B. Bukan identitas, karena untuk $y=0$ ruas kiri bernilai $-77$ sedangkan ruas kanan bernilai 84  
  <sub>Salah: salah hitung: $(-9)^2$ ditulis $-81$ lalu ditambah 4</sub>
- **C. Bukan identitas, karena untuk $y=0$ ruas kiri bernilai 85 sedangkan ruas kanan bernilai 84** ✅  
  <sub>Benar: ruas kiri dijabarkan menjadi $64y^2-144y+85$, sedangkan ruas kanan berkonstanta 84; untuk $y=0$: $81+4=85\neq84$.</sub>
- D. Identitas, karena $(8y-9)^2 = 64y^2 - 144y + 81$ sama dengan ruas kanan  
  <sub>Salah: lupa bahwa ruas kiri masih ditambah 4 dan konstanta 81 + 4 = 85, bukan 84</sub>

**Pembahasan:** Ruas kiri $=64y^2-144y+81+4=64y^2-144y+85$. Konstanta 85 tidak sama dengan 84, jadi bukan identitas.
**Acuan:** siswa — siswa hal.105 Mari Mencoba 2.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b02-e-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: faktorisasi dengan identitas*

Faktorkan $(5x-2)^2 - 49$.

- **A. $(5x+5)(5x-9)$** ✅  
  <sub>Benar: selisih kuadrat dengan $a=5x-2$ dan $b=7$: $(5x-2+7)(5x-2-7)=(5x+5)(5x-9)$.</sub>
- B. $(5x-7)(5x+7)$  
  <sub>Salah: mengabaikan suku $-2$ di dalam kuadrat</sub>
- C. $(5x-5)(5x+9)$  
  <sub>Salah: salah tanda saat menggabungkan $-2$ dengan $\pm7$</sub>
- D. $(5x-51)(5x+47)$  
  <sub>Salah: memakai 49 sebagai $b$ bukan 7 lalu menggabungkan dengan $-2$</sub>

**Pembahasan:** $(5x-2)^2-7^2=(5x-2+7)(5x-2-7)=(5x+5)(5x-9)$.
**Acuan:** siswa — siswa hal.105 Contoh 2.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b02-e-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: faktorisasi dengan identitas*

Faktorkan $16x^2 + 40xy + 25y^2$.

- A. $(16x+25y)^2$  
  <sub>Salah: lupa menarik akar koefisien kuadrat</sub>
- **B. $(4x+5y)^2$** ✅  
  <sub>Benar: $16x^2=(4x)^2$, $25y^2=(5y)^2$, dan $2(4x)(5y)=40xy$, jadi bentuknya $(4x+5y)^2$.</sub>
- C. $(4x+5y)(4x-5y)$  
  <sub>Salah: tertukar dengan identitas selisih dua kuadrat</sub>
- D. $(4x+10y)^2$  
  <sub>Salah: salah menentukan $b$: memakai $40/4$ sebagai $b$</sub>

**Pembahasan:** Bentuk $a^2+2ab+b^2$ dengan $a=4x$ dan $b=5y$, jadi $(4x+5y)^2$.
**Acuan:** siswa — siswa hal.106 Mari Mencoba 2.14

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b02-e-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: mencari polinomial dari identitas*

Jika $(x^2+2x-15)(x-7) = P(x)\cdot(x+5)$ adalah identitas, polinomial $P(x)$ adalah ....

- **A. $x^2-10x+21$** ✅  
  <sub>Benar: $x^2+2x-15=(x+5)(x-3)$, sehingga $P(x)=(x-3)(x-7)=x^2-10x+21$.</sub>
- B. $x^2+10x+21$  
  <sub>Salah: salah tanda saat menjabarkan $(x-3)(x-7)$</sub>
- C. $x^2+2x-15$  
  <sub>Salah: hanya mengambil faktor kuadrat dan melupakan faktor $(x-7)$</sub>
- D. $x^2-4x-21$  
  <sub>Salah: memakai faktor $(x+3)(x-7)$ karena tanda faktor kuadrat terbalik</sub>

**Pembahasan:** Faktorkan $x^2+2x-15=(x+5)(x-3)$, bagi kedua ruas dengan $(x+5)$: $P(x)=(x-3)(x-7)$.
**Acuan:** siswa — siswa hal.107 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b02-e-easy-bt01-011
*variasi (konteks) | C2 | 1 langkah | jenis: konsep identitas polinomial*

Pernyataan yang benar tentang persamaan polinomial dan identitas polinomial adalah ....

- A. Persamaan $x + 1 = x + 1$ bukan identitas, karena memuat variabel  
  <sub>Salah: mengira persamaan bervariabel tidak mungkin identitas</sub>
- B. Setiap persamaan polinomial pasti merupakan identitas polinomial  
  <sub>Salah: menyamakan persamaan polinomial dengan identitas</sub>
- C. Persamaan $x + 1 = 4$ merupakan identitas, karena ada nilai $x$ yang memenuhinya  
  <sub>Salah: satu nilai pemenuh dikira cukup untuk menjadi identitas</sub>
- **D. Persamaan $x + 1 = 4$ bukan identitas, karena hanya benar untuk $x=3$** ✅  
  <sub>Benar: identitas harus benar untuk setiap nilai variabel, sedangkan $x+1=4$ hanya benar saat $x=3$.</sub>

**Pembahasan:** Identitas polinomial benar untuk semua nilai variabel. $x+1=4$ salah untuk $x=0$, jadi bukan identitas.
**Acuan:** siswa — siswa hal.106 Latihan E Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b02-e-easy-bt01-012
*variasi (konteks) | C2 | 1 langkah | jenis: konsep identitas polinomial*

Cara yang cukup untuk menunjukkan bahwa suatu persamaan polinomial bukan identitas polinomial adalah ....

- **A. menemukan satu nilai variabel yang membuat ruas kiri tidak sama dengan ruas kanan** ✅  
  <sub>Benar: satu contoh penyangkal sudah cukup untuk membuktikan persamaan tidak berlaku untuk semua nilai variabel.</sub>
- B. memeriksa bahwa kedua ruas bernilai sama untuk satu nilai variabel tertentu  
  <sub>Salah: menjadikan satu nilai cocok sebagai bukti identitas</sub>
- C. menunjukkan bahwa kedua ruas memiliki derajat yang sama  
  <sub>Salah: derajat sama tidak menjamin kedua ruas identik</sub>
- D. menemukan satu nilai variabel yang membuat kedua ruas bernilai sama  
  <sub>Salah: satu contoh yang cocok dikira bukti bukan identitas</sub>

**Pembahasan:** Untuk membuktikan bukan identitas cukup satu nilai variabel yang membuat kedua ruas berbeda.
**Acuan:** siswa — siswa hal.106 Latihan E Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b02-e-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: mengenali identitas selisih kuadrat*

Diberikan persamaan $49n^2 - 36 = (7n+6)(7n-6)$. Pernyataan yang benar adalah ....

- A. Bukan identitas, karena $49n^2-36=(7n)^2+6^2$  
  <sub>Salah: salah tanda: selisih kuadrat dianggap jumlah kuadrat</sub>
- B. Bukan identitas, karena seharusnya $49n^2-36=(7n-6)^2$  
  <sub>Salah: menyamakan selisih kuadrat dengan kuadrat selisih</sub>
- **C. Identitas, karena $49n^2-36=(7n)^2-6^2$ sesuai bentuk $a^2-b^2=(a+b)(a-b)$** ✅  
  <sub>Benar: $(7n+6)(7n-6)=49n^2-36$ untuk setiap $n$.</sub>
- D. Bukan identitas, karena $(7n+6)(7n-6)=49n^2-84n-36$  
  <sub>Salah: salah menjabarkan: suku tengah dianggap tidak saling meniadakan</sub>

**Pembahasan:** $(7n+6)(7n-6)=(7n)^2-6^2=49n^2-36$, sehingga merupakan identitas.
**Acuan:** siswa — siswa hal.108 Uji Kompetensi Bab 2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b02-e-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: mengingat rumus identitas*

Bentuk faktor dari $a^3 + b^3$ yang merupakan identitas polinomial adalah ....

- A. $(a+b)^3$  
  <sub>Salah: mengira jumlah pangkat tiga sama dengan pangkat tiga dari jumlah</sub>
- B. $(a-b)(a^2-ab+b^2)$  
  <sub>Salah: faktor linear bertanda negatif, tertukar dengan identitas selisih pangkat tiga</sub>
- C. $(a+b)(a^2+ab+b^2)$  
  <sub>Salah: suku tengah bertanda positif, tertukar dengan identitas selisih pangkat tiga</sub>
- **D. $(a+b)(a^2-ab+b^2)$** ✅  
  <sub>Benar: identitas jumlah pangkat tiga: $a^3+b^3=(a+b)(a^2-ab+b^2)$.</sub>

**Pembahasan:** Sifat 2.6 nomor 4: $a^3+b^3=(a+b)(a^2-ab+b^2)$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b02-e-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: mengingat rumus identitas*

Pada hasil penjabaran $(x+2)^3$, koefisien dari $x$ adalah ....

- A. $4$  
  <sub>Salah: mengambil $b^2$ tanpa faktor 3</sub>
- B. $6$  
  <sub>Salah: mengambil koefisien $x^2$ yaitu $3\cdot2$</sub>
- C. $8$  
  <sub>Salah: mengambil suku konstanta $2^3$</sub>
- **D. $12$** ✅  
  <sub>Benar: $(x+2)^3=x^3+6x^2+12x+8$, koefisien $x$ adalah $3\cdot2^2=12$.</sub>

**Pembahasan:** $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ dengan $a=x$, $b=2$: suku $x$ adalah $3x\cdot4=12x$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b02-e-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: mengenali bentuk identitas*

Persamaan polinomial berikut yang merupakan identitas polinomial adalah ....

- A. $(a+b)^3 = a^3 + b^3$  
  <sub>Salah: mengira pangkat tiga jumlah hanya memangkatkan tiap suku</sub>
- **B. $(a-b)^2 = a^2 - 2ab + b^2$** ✅  
  <sub>Benar: identitas kuadrat selisih dua suku (Sifat 2.6 nomor 3).</sub>
- C. $(a+b)^2 = a^2 + b^2$  
  <sub>Salah: melupakan suku tengah $2ab$</sub>
- D. $a^2 - b^2 = (a-b)^2$  
  <sub>Salah: menyamakan selisih kuadrat dengan kuadrat selisih</sub>

**Pembahasan:** Hanya $(a-b)^2=a^2-2ab+b^2$ yang berlaku untuk semua $a$ dan $b$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b02-e-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: penerapan identitas pada bilangan*

Dengan memakai identitas $a^2-b^2=(a+b)(a-b)$, nilai dari $101^2 - 99^2$ adalah ....

- A. $800$  
  <sub>Salah: mengalikan hasil dengan 2 sekali lagi</sub>
- B. $200$  
  <sub>Salah: hanya mengambil faktor $(a+b)$</sub>
- **C. $400$** ✅  
  <sub>Benar: $101^2-99^2=(101+99)(101-99)=200\cdot2=400$.</sub>
- D. $2$  
  <sub>Salah: hanya mengambil faktor $(a-b)$</sub>

**Pembahasan:** $(101+99)(101-99)=200\cdot2=400$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b02-e-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: melengkapi koefisien identitas*

Agar persamaan $x^2 - 14x + k = (x-7)^2$ merupakan identitas polinomial, nilai $k$ adalah ....

- A. $-49$  
  <sub>Salah: salah tanda: kuadrat selalu positif</sub>
- B. $14$  
  <sub>Salah: menyamakan konstanta dengan koefisien suku $x$</sub>
- C. $7$  
  <sub>Salah: mengambil $b$ bukan $b^2$</sub>
- **D. $49$** ✅  
  <sub>Benar: $(x-7)^2=x^2-14x+49$, sehingga $k=49$.</sub>

**Pembahasan:** Konstanta $b^2=7^2=49$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b02-e-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: penerapan numerik identitas*

Seorang pesulap meminta penonton memilih sebuah bilangan $n$, mengalikan $(n+4)$ dengan $(n-4)$, menambahkan 20, lalu mengurangi hasilnya dengan $n^2$. Berapa pun $n$ yang dipilih, hasil akhirnya selalu ....

- A. $36$  
  <sub>Salah: menganggap $(n+4)(n-4)=n^2+16$</sub>
- B. $20$  
  <sub>Salah: mengabaikan hasil kali $(n+4)(n-4)$</sub>
- **C. $4$** ✅  
  <sub>Benar: $(n+4)(n-4)+20-n^2=n^2-16+20-n^2=4$.</sub>
- D. $16$  
  <sub>Salah: lupa menambahkan 20</sub>

**Pembahasan:** $(n+4)(n-4)=n^2-16$, ditambah 20 menjadi $n^2+4$, dikurangi $n^2$ menjadi 4.
**Acuan:** siswa — siswa hal.103

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b02-e-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: menyederhanakan dengan identitas*

Bentuk sederhana dari $(x+3)(x^2-3x+9)$ adalah ....

- A. $x^3 + 81$  
  <sub>Salah: menghitung $3^3$ sebagai $9\cdot9$</sub>
- **B. $x^3 + 27$** ✅  
  <sub>Benar: identitas jumlah pangkat tiga dengan $b=3$: $(x+3)(x^2-3x+9)=x^3+3^3$.</sub>
- C. $x^3 - 27$  
  <sub>Salah: salah tanda: memakai identitas selisih pangkat tiga</sub>
- D. $x^3 + 9$  
  <sub>Salah: menghitung $3^3$ sebagai $3\cdot3$</sub>

**Pembahasan:** Sifat 2.6 nomor 4: $a^3+b^3=(a+b)(a^2-ab+b^2)$ dengan $a=x$, $b=3$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b02-e-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: faktorisasi kuadrat berkoefisien*

Faktorkan $9(2x-5)^2 - 64$.

- A. $(6x+49)(6x-79)$  
  <sub>Salah: memakai 64 sebagai $b$ bukan 8</sub>
- **B. $(6x-7)(6x-23)$** ✅  
  <sub>Benar: $9(2x-5)^2=(6x-15)^2$ dan $64=8^2$, sehingga $(6x-15+8)(6x-15-8)=(6x-7)(6x-23)$.</sub>
- C. $(6x+7)(6x-23)$  
  <sub>Salah: salah tanda pada faktor pertama: $-15+8$ ditulis $+7$</sub>
- D. $(2x+3)(2x-13)$  
  <sub>Salah: lupa bahwa koefisien 9 ikut dikuadratkan: memakai $(2x-5)$ sebagai $a$ dan 8 sebagai $b$</sub>

**Pembahasan:** $9(2x-5)^2-64=(6x-15)^2-8^2=(6x-15+8)(6x-15-8)=(6x-7)(6x-23)$.
**Acuan:** siswa — siswa hal.107 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b02-e-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: faktorisasi kuadrat sempurna berpangkat*

Faktorkan $25a^6 + 40a^3b^3 + 16b^6$.

- A. $(5a^2+4b^2)^2$  
  <sub>Salah: mengambil akar pangkat enam sebagai pangkat dua, bukan pangkat tiga</sub>
- B. $(25a^3+16b^3)^2$  
  <sub>Salah: lupa menarik akar koefisien 25 dan 16</sub>
- **C. $(5a^3+4b^3)^2$** ✅  
  <sub>Benar: $25a^6=(5a^3)^2$, $16b^6=(4b^3)^2$, dan $2(5a^3)(4b^3)=40a^3b^3$, jadi bentuknya $(5a^3+4b^3)^2$.</sub>
- D. $(5a^3+4b^3)(5a^3-4b^3)$  
  <sub>Salah: tertukar dengan identitas selisih dua kuadrat</sub>

**Pembahasan:** Bentuk $A^2+2AB+B^2$ dengan $A=5a^3$ dan $B=4b^3$ sehingga $(5a^3+4b^3)^2$.
**Acuan:** siswa — siswa hal.107 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b02-e-medium-bt01-003
*variasi (angka) | C4 | 4 langkah | jenis: menemukan suku yang salah pada identitas*

Diberikan persamaan polinomial $(2p - q + 3r)^2 = 4p^2 + q^2 + 9r^2 - 4pq + 12pr + 6qr$. Pernyataan yang benar adalah ....

- A. Identitas, karena suku $p^2$, $q^2$, dan $r^2$ sudah benar  
  <sub>Salah: hanya memeriksa suku-suku kuadrat dan mengabaikan suku silang</sub>
- B. Bukan identitas, karena suku $pq$ seharusnya $+4pq$  
  <sub>Salah: salah tanda: $2(2p)(-q)=-4pq$</sub>
- C. Bukan identitas, karena suku $pr$ seharusnya $6pr$  
  <sub>Salah: lupa mengalikan 2 pada $2\cdot2p\cdot3r=12pr$ dengan benar</sub>
- **D. Bukan identitas, karena suku $qr$ seharusnya $-6qr$** ✅  
  <sub>Benar: $(2p-q+3r)^2=4p^2+q^2+9r^2-4pq+12pr-6qr$; hanya suku $qr$ yang berbeda tanda.</sub>

**Pembahasan:** Suku silang: $2(2p)(-q)=-4pq$, $2(2p)(3r)=12pr$, $2(-q)(3r)=-6qr$. Pada soal suku $qr$ bertanda $+$, sehingga bukan identitas.
**Acuan:** siswa — siswa hal.106 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b02-e-medium-bt01-004
*variasi (konteks) | C4 | 3 langkah | jenis: menganalisis pola bilangan*

Rina mencatat hasil berikut: $4^2-2^2=12$ dengan $4+2=6$; $6^2-4^2=20$ dengan $6+4=10$; $8^2-6^2=28$ dengan $8+6=14$. Rina menduga selisih kuadrat dua bilangan genap yang berurutan selalu sama dengan $k$ kali jumlah kedua bilangan itu. Bila dibuktikan secara aljabar untuk semua bilangan genap berurutan $n$ dan $n+2$, nilai $k$ adalah ....

- A. $3$  
  <sub>Salah: menaksir dari pola tanpa menjabarkan: 12 dibanding 6 dikira berselisih 3 kali</sub>
- B. $4$  
  <sub>Salah: mengambil koefisien $4n$ tanpa membandingkannya dengan jumlah $2n+2$</sub>
- **C. $2$** ✅  
  <sub>Benar: $(n+2)^2-n^2=4n+4=2(2n+2)=2(n+(n+2))$, jadi $k=2$.</sub>
- D. $1$  
  <sub>Salah: menyamakan dengan pola bilangan bulat berurutan biasa yang selisihnya sama dengan jumlah</sub>

**Pembahasan:** $(n+2)^2-n^2=(n+2+n)(n+2-n)=2(2n+2)$, dan $2n+2$ adalah jumlah $n$ dan $n+2$. Jadi selisih $=2\times$ jumlah.
**Acuan:** siswa — siswa hal.107 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b02-e-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: menguji identitas dengan penjabaran*

Apakah persamaan polinomial berikut merupakan identitas polinomial atau bukan? $64(x-5)^3 = (4x-20)^3$

- **A. Identitas, karena $(4x-20)^3=(4(x-5))^3=64(x-5)^3$** ✅  
  <sub>Benar: $4x-20=4(x-5)$ sehingga $(4x-20)^3=4^3(x-5)^3=64(x-5)^3$ untuk setiap $x$.</sub>
- B. Bukan identitas, karena $(4x-20)^3=64x^3-8000$  
  <sub>Salah: memangkatkan tiap suku saja, mengabaikan suku-suku silang</sub>
- C. Bukan identitas, karena koefisien 64 dan 4 berbeda  
  <sub>Salah: menganggap koefisien harus sama di kedua ruas tanpa mengubah bentuk</sub>
- D. Bukan identitas, karena untuk $x=0$ ruas kiri bernilai $-8000$ sedangkan ruas kanan bernilai $8000$  
  <sub>Salah: salah tanda ruas kanan: $(-5)^3=-125$, bukan 125</sub>

**Pembahasan:** Faktorkan $4x-20=4(x-5)$ lalu pangkatkan tiga: $64(x-5)^3$, sama dengan ruas kiri.
**Acuan:** pretest — kelas11_tl-b02-p0106-latihan-e-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b02-e-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: mencari polinomial dari identitas*

Jika $(x^3-125)(x+7) = P(x)\cdot(x^2+5x+25)$ adalah identitas, polinomial $P(x)$ adalah ....

- A. $x^2+12x+35$  
  <sub>Salah: salah tanda pada faktor $(x-5)$ sehingga ditulis $(x+5)(x+7)$</sub>
- **B. $x^2+2x-35$** ✅  
  <sub>Benar: $x^3-125=(x-5)(x^2+5x+25)$, sehingga $P(x)=(x-5)(x+7)=x^2+2x-35$.</sub>
- C. $x^2-12x+35$  
  <sub>Salah: salah tanda pada faktor $(x+7)$ dan $(x-5)$ sekaligus</sub>
- D. $x^2-2x-35$  
  <sub>Salah: tanda kedua konstanta tertukar: $(x+5)(x-7)$</sub>

**Pembahasan:** Identitas 5: $x^3-5^3=(x-5)(x^2+5x+25)$. Bagi kedua ruas dengan $x^2+5x+25$: $P(x)=(x-5)(x+7)=x^2+2x-35$.
**Acuan:** siswa — siswa hal.107 Latihan E

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b02-e-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: pemodelan sulap bilangan*

Seorang pesulap meminta penonton memilih bilangan $n$ yang tidak nol, lalu mengkuadratkan jumlah $n$ dan 5, mengurangi hasilnya dengan kuadrat selisih $n$ dan 5, kemudian membagi hasilnya dengan $n$. Berapa pun $n$ yang dipilih, hasil akhirnya selalu ....

- A. $40$  
  <sub>Salah: menghitung suku silang dua kali lipat dari yang seharusnya</sub>
- B. $0$  
  <sub>Salah: mengira kedua kuadrat saling meniadakan</sub>
- C. $10$  
  <sub>Salah: mengira suku silang hanya muncul satu kali ($2ab$ bukan $4ab$)</sub>
- **D. $20$** ✅  
  <sub>Benar: $(n+5)^2-(n-5)^2=20n$, dibagi $n$ menjadi 20.</sub>

**Pembahasan:** $(n^2+10n+25)-(n^2-10n+25)=20n$. Dibagi $n$ (dengan $n\neq0$) hasilnya 20.
**Acuan:** siswa — siswa hal.103

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b02-e-medium-bt01-008
*orisinal | C4 | 4 langkah | jenis: pemodelan sulap bilangan*

Seorang pesulap meminta penonton memilih bilangan bulat $n$, memangkatkan tiga jumlah $n$ dan 1, mengurangi hasilnya dengan pangkat tiga selisih $n$ dan 1, lalu mengurangi lagi dengan $6n^2$. Berapa pun $n$ yang dipilih, hasil akhirnya selalu ....

- A. $1$  
  <sub>Salah: hanya menghitung konstanta $1^3$ satu kali</sub>
- B. $0$  
  <sub>Salah: mengira suku konstanta $1$ dan $-1$ saling meniadakan, padahal $1-(-1)=2$</sub>
- C. $-2$  
  <sub>Salah: salah tanda pada suku konstanta $-(-1)^3$</sub>
- **D. $2$** ✅  
  <sub>Benar: $(n+1)^3-(n-1)^3=6n^2+2$, dikurangi $6n^2$ menjadi 2.</sub>

**Pembahasan:** $(n^3+3n^2+3n+1)-(n^3-3n^2+3n-1)=6n^2+2$. Dikurangi $6n^2$ hasilnya 2.
**Acuan:** siswa — siswa hal.103

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b02-e-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: menentukan parameter koefisien identitas*

Jika $(px+q)^3 = 8x^3 + 36x^2 + rx + 27$ adalah identitas polinomial dengan $p$ dan $q$ bilangan real positif, nilai $p+q+r$ adalah ....

- A. $32$  
  <sub>Salah: mengambil $r=q^3=27$</sub>
- B. $41$  
  <sub>Salah: mengambil $r=36$, koefisien $x^2$ tertukar dengan koefisien $x$</sub>
- C. $23$  
  <sub>Salah: menghitung $r=3pq$ (=18) bukan $3pq^2$</sub>
- **D. $59$** ✅  
  <sub>Benar: $p^3=8$ dan $q^3=27$ memberi $p=2$, $q=3$ (cocok: $3p^2q=36$); $r=3pq^2=54$, sehingga $p+q+r=59$.</sub>

**Pembahasan:** $(px+q)^3=p^3x^3+3p^2qx^2+3pq^2x+q^3$. Dari $p^3=8$, $q^3=27$ diperoleh $p=2$, $q=3$; $r=3\cdot2\cdot9=54$. Jumlahnya 59.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b02-e-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: faktorisasi dengan dua identitas*

Bentuk faktor dari $4x^2 - 12x + 9 - 25y^2$ adalah ....

- A. $(2x-3+5y)(2x+3-5y)$  
  <sub>Salah: salah tanda konstanta pada faktor kedua</sub>
- **B. $(2x-3+5y)(2x-3-5y)$** ✅  
  <sub>Benar: $4x^2-12x+9=(2x-3)^2$, sehingga $(2x-3)^2-(5y)^2=(2x-3+5y)(2x-3-5y)$.</sub>
- C. $(2x+3+5y)(2x+3-5y)$  
  <sub>Salah: mengabaikan tanda minus pada $(2x-3)^2$ (suku tengah $-12x$)</sub>
- D. $(2x-3+25y)(2x-3-25y)$  
  <sub>Salah: memakai 25 sebagai $b$ bukan 5</sub>

**Pembahasan:** $4x^2-12x+9=(2x-3)^2$ (identitas 3), lalu $(2x-3)^2-(5y)^2=(2x-3+5y)(2x-3-5y)$ (identitas 1).
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b02-e-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: penerapan identitas pada bilangan*

Dengan memakai identitas $a^3+b^3=(a+b)(a^2-ab+b^2)$, nilai dari $\dfrac{51^3+49^3}{51^2-51\cdot49+49^2}$ adalah ....

- **A. $100$** ✅  
  <sub>Benar: pembilang $=(51+49)(51^2-51\cdot49+49^2)$, faktor kuadrat dicoret sehingga tersisa $51+49=100$.</sub>
- B. $200$  
  <sub>Salah: menggandakan hasil $a+b$ setelah pencoretan</sub>
- C. $2$  
  <sub>Salah: memakai faktor selisih $(a-b)$ bukan jumlah $(a+b)$</sub>
- D. $50$  
  <sub>Salah: mengambil rata-rata $a$ dan $b$</sub>

**Pembahasan:** $51^3+49^3=(51+49)(51^2-51\cdot49+49^2)$. Faktor kuadrat sama dengan penyebut, hasil $=100$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b02-e-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: menyederhanakan pecahan dengan identitas*

Untuk $x\neq3$ dan $x\neq-3$, bentuk paling sederhana dari $\dfrac{x^3-27}{x^2-9}$ adalah ....

- A. $\dfrac{x^2+3x+9}{x-3}$  
  <sub>Salah: salah mencoret: faktor penyebut yang tersisa tertukar</sub>
- B. $x-3$  
  <sub>Salah: mencoret pangkat tiga dengan pangkat dua secara langsung</sub>
- **C. $\dfrac{x^2+3x+9}{x+3}$** ✅  
  <sub>Benar: $x^3-27=(x-3)(x^2+3x+9)$ dan $x^2-9=(x-3)(x+3)$; faktor $(x-3)$ dicoret.</sub>
- D. $\dfrac{x^2-3x+9}{x+3}$  
  <sub>Salah: salah tanda suku tengah: memakai pola jumlah pangkat tiga</sub>

**Pembahasan:** Identitas 5 dan 1: $\frac{(x-3)(x^2+3x+9)}{(x-3)(x+3)}=\frac{x^2+3x+9}{x+3}$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b02-e-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: mengevaluasi klaim identitas*

Dimas menyatakan bahwa $(a+b)^2-(a-b)^2=2ab$ merupakan identitas polinomial. Pernyataan yang tepat tentang klaim Dimas adalah ....

- A. Keliru, karena ruas kiri sama dengan $2a^2+2b^2$ untuk semua nilai  
  <sub>Salah: mencampur dengan hasil jumlah dua kuadrat $(a+b)^2+(a-b)^2$</sub>
- **B. Keliru, karena ruas kiri sama dengan $4ab$, sehingga $a=b=1$ memberi 4 lawan 2** ✅  
  <sub>Benar: $(a+b)^2-(a-b)^2=4ab$, sehingga $a=b=1$ menjadi contoh penyangkal.</sub>
- C. Benar, karena sudah diuji dengan $a=0$ dan kedua ruas sama-sama bernilai 0  
  <sub>Salah: satu nilai yang cocok dianggap cukup untuk menjadi identitas</sub>
- D. Benar, karena suku kuadrat saling meniadakan dan hanya tersisa $2ab$  
  <sub>Salah: menghitung suku silang hanya sekali padahal muncul dua kali</sub>

**Pembahasan:** $(a^2+2ab+b^2)-(a^2-2ab+b^2)=4ab\neq2ab$ untuk $a=b=1$ (4 lawan 2), sehingga bukan identitas.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b02-e-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: menerapkan identitas pada kondisi bilangan*

Jika $a$ dan $b$ bilangan real dengan $a-b=4$ dan $ab=12$, nilai $a^3-b^3$ adalah ....

- **A. $208$** ✅  
  <sub>Benar: $(a-b)^3=a^3-b^3-3ab(a-b)$, sehingga $a^3-b^3=64+3\cdot12\cdot4=208$.</sub>
- B. $64$  
  <sub>Salah: mengira $a^3-b^3=(a-b)^3$ dan melupakan suku $3ab(a-b)$</sub>
- C. $112$  
  <sub>Salah: memakai $ab(a-b)=48$ tanpa faktor 3</sub>
- D. $-80$  
  <sub>Salah: salah tanda suku $3ab(a-b)$ saat memindahkan ruas</sub>

**Pembahasan:** Dari $(a-b)^3=a^3-3a^2b+3ab^2-b^3=a^3-b^3-3ab(a-b)$ diperoleh $a^3-b^3=(a-b)^3+3ab(a-b)=64+144=208$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b02-e-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: mengenali bentuk identitas*

Persamaan polinomial berikut yang merupakan identitas polinomial adalah ....

- **A. $(a^2+ab+b^2)(a^2-ab+b^2) = a^4 + a^2b^2 + b^4$** ✅  
  <sub>Benar: $(a^2+b^2+ab)(a^2+b^2-ab)=(a^2+b^2)^2-a^2b^2=a^4+a^2b^2+b^4$.</sub>
- B. $(a^2+ab+b^2)(a^2-ab+b^2) = a^4 + 2a^2b^2 + b^4$  
  <sub>Salah: menjabarkan $(a^2+b^2)^2$ tanpa mengurangi $a^2b^2$</sub>
- C. $(a^2+ab+b^2)(a^2-ab+b^2) = a^4 + b^4$  
  <sub>Salah: mengira suku $ab$ dan $-ab$ saling meniadakan hasil kali</sub>
- D. $(a^2+ab+b^2)(a^2-ab+b^2) = a^4 - a^2b^2 + b^4$  
  <sub>Salah: salah tanda suku tengah setelah mengurangkan $a^2b^2$</sub>

**Pembahasan:** Dengan $A=a^2+b^2$ dan $B=ab$: $(A+B)(A-B)=A^2-B^2=a^4+2a^2b^2+b^4-a^2b^2=a^4+a^2b^2+b^4$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b02-e-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: faktorisasi kuadrat sempurna berpangkat*

Bentuk faktor dari $(2x+1)^2-(x-3)^2$ adalah ....

- A. $(3x-2)(x-2)$  
  <sub>Salah: salah tanda saat mengurangkan $b$: $-(x-3)$ ditulis $-x-3$</sub>
- B. $(3x+4)(x-2)$  
  <sub>Salah: salah tanda saat menjumlahkan dan mengurangkan konstanta sekaligus</sub>
- **C. $(3x-2)(x+4)$** ✅  
  <sub>Benar: $a=2x+1$ dan $b=x-3$: $(a+b)(a-b)=(3x-2)(x+4)$.</sub>
- D. $(3x+2)(x+4)$  
  <sub>Salah: salah menjumlahkan konstanta: $1-3$ ditulis $+2$</sub>

**Pembahasan:** $(2x+1+x-3)(2x+1-x+3)=(3x-2)(x+4)$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas11_tl-b02-e-hard-bt01-001
*orisinal | C6 | 5 langkah | jenis: merancang pasangan pembangkit tripel Pythagoras*

Tiga bilangan $a^2-b^2$, $2ab$, dan $a^2+b^2$ dengan $a>b$ selalu merupakan panjang sisi segitiga siku-siku dengan sisi miring $a^2+b^2$. Pesulap ingin segitiga siku-siku dengan sisi miring tepat 65 satuan, dengan $a$ dan $b$ bilangan asli, $a>b$. Nilai terbesar yang mungkin untuk $a+b$ adalah ....

- A. $7$  
  <sub>Salah: mengambil $a$ dari pasangan $(7,4)$, bukan jumlah $a+b$</sub>
- B. $3$  
  <sub>Salah: menghitung selisih $a-b$ dari pasangan $(7,4)$</sub>
- **C. $11$** ✅  
  <sub>Benar: $a^2+b^2=65$ dipenuhi $(a,b)=(8,1)$ dan $(7,4)$; jumlahnya 9 dan 11, terbesar 11 (sisi 33, 56, 65).</sub>
- D. $9$  
  <sub>Salah: hanya menemukan pasangan $(8,1)$ dan melewatkan $(7,4)$</sub>

**Pembahasan:** Karena sisi miring $a^2+b^2=65$, uji $b=1,\dots,5$: $b=1\Rightarrow a=8$, $b=4\Rightarrow a=7$, lainnya tidak bulat. $a+b$ bernilai 9 atau 11, maksimum 11.
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas11_tl-b02-e-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: mengevaluasi bukti tripel Pythagoras*

Jika $a$ dan $b$ bilangan real positif dengan $a>b$, empat siswa memberi argumen bahwa $a^2-b^2$, $2ab$, dan $a^2+b^2$ adalah panjang sisi segitiga siku-siku. Argumen yang sahih dan benar adalah ....

- **A. Identitas $(a^2-b^2)^2+(2ab)^2=(a^2+b^2)^2$ berlaku untuk semua $a>b>0$, sisi miringnya $a^2+b^2$** ✅  
  <sub>Benar: kebalikan teorema Pythagoras berlaku bila jumlah kuadrat dua sisi sama dengan kuadrat sisi ketiga untuk semua $a>b>0$.</sub>
- B. Cukup menguji $a=2$, $b=1$ yang memberi sisi 3, 4, 5, lalu berlaku untuk semua $a,b$  
  <sub>Salah: satu contoh dianggap membuktikan identitas</sub>
- C. Tidak berlaku, karena $(a^2-b^2)^2+(2ab)^2=a^4+b^4$  
  <sub>Salah: suku silang $2a^2b^2$ dari dua kuadrat terlewat</sub>
- D. Benar, dengan sisi miring $2ab$ karena suku yang memuat dua variabel paling panjang  
  <sub>Salah: sisi miring ditentukan dari bentuk suku, padahal pada $a=2$, $b=1$ nilai $2ab=4<5$</sub>

**Pembahasan:** Jabarkan: $(a^2-b^2)^2+(2ab)^2=a^4-2a^2b^2+b^4+4a^2b^2=(a^2+b^2)^2$ untuk semua $a,b$. Karena $a>b>0$, ketiganya positif, dan $a^2+b^2$ terbesar.
**Acuan:** siswa — siswa hal.107

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas11_tl-b02-e-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: menemukan kesalahan penyamaan koefisien*

Rani ingin menentukan $a$ dan $b$ agar $(x^2+ax+b)^2=x^4-6x^3+13x^2-12x+4$ merupakan identitas polinomial. Pekerjaannya: koefisien $x^3$: $2a=-6$ sehingga $a=-3$; koefisien $x^2$: $a^2+b=13$ sehingga $b=4$. Pernyataan yang benar tentang pekerjaan Rani adalah ....

- A. Koefisien $x^3$ seharusnya $a$, sehingga $a=-6$  
  <sub>Salah: mengira kuadrat tidak menggandakan koefisien $x^3$</sub>
- B. Koefisien $x$ seharusnya $a+b$, sehingga $b=-9$  
  <sub>Salah: salah menjabarkan suku silang $2ab$ menjadi $a+b$</sub>
- C. Pekerjaannya sudah benar, karena $a=-3$ dan $b=4$ memenuhi syarat koefisien $x^3$ dan $x^2$  
  <sub>Salah: tidak mengecek koefisien $x$: $2ab=-24$ bukan $-12$</sub>
- **D. Koefisien $x^2$ seharusnya $a^2+2b$, sehingga $b=2$** ✅  
  <sub>Benar: koefisien $x^2$ pada $(x^2+ax+b)^2$ adalah $a^2+2b$; dengan $a=-3$ diperoleh $b=2$, dan koefisien $x$ ($2ab=-12$) serta konstanta ($b^2=4$) cocok.</sub>

**Pembahasan:** Jabarkan $(x^2+ax+b)^2=x^4+2ax^3+(a^2+2b)x^2+2abx+b^2$. Dari $2a=-6$, $a=-3$; dari $9+2b=13$, $b=2$. Cek: $2ab=-12$, $b^2=4$. Nilai $b=4$ gagal pada koefisien $x$.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas11_tl-b02-e-hard-bt01-004
*orisinal | C5 | 6 langkah | jenis: mengevaluasi empat pernyataan identitas*

Pernyataan berikut yang merupakan identitas polinomial (benar untuk semua bilangan real $a$ dan $b$) adalah ....

- **A. $(a-b)^3=a^3-b^3-3ab(a-b)$** ✅  
  <sub>Benar: menjabarkan ruas kanan: $a^3-b^3-3a^2b+3ab^2$ sama dengan $(a-b)^3$.</sub>
- B. $(a-b)^3=(b-a)^3$  
  <sub>Salah: mengira pangkat tiga tidak mengubah tanda; $a=1$, $b=0$ memberi 1 lawan $-1$</sub>
- C. $a^3-b^3=(a-b)^3+3ab(a+b)$  
  <sub>Salah: tanda suku silang tertukar; $a=1$, $b=1$ memberi 0 lawan 6</sub>
- D. $a^4-b^4=(a^2+b^2)(a+b)$  
  <sub>Salah: faktor $(a-b)$ terlewat; $a=3$, $b=1$ memberi 80 lawan 40</sub>

**Pembahasan:** Jabarkan tiap pernyataan. Hanya pernyataan pertama yang sama untuk semua $a$ dan $b$; ketiga yang lain punya contoh penyangkal.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b02-e-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: mencari contoh penyangkal terkecil*

Rudi menguji persamaan $x^3+2x=3x^2$ dengan $x=0$, $x=1$, dan $x=2$; ketiganya benar, sehingga ia menyimpulkan persamaan itu identitas polinomial. Bilangan bulat positif terkecil yang menunjukkan kesimpulan Rudi keliru adalah ....

- A. $4$  
  <sub>Salah: $x=4$ memang penyangkal, tetapi bukan yang terkecil</sub>
- **B. $3$** ✅  
  <sub>Benar: kedua ruas sama pada $x=1,2$, tetapi pada $x=3$ ruas kiri 33 dan ruas kanan 27.</sub>
- C. $2$  
  <sub>Salah: memilih nilai yang sudah diuji Rudi, kedua ruas sama-sama 12</sub>
- D. $1$  
  <sub>Salah: memilih nilai yang sudah diuji Rudi, kedua ruas sama-sama 3</sub>

**Pembahasan:** $x^3-3x^2+2x=x(x-1)(x-2)$, nol hanya di $x=0,1,2$. Bilangan bulat positif terkecil yang membuat selisih tak nol adalah 3.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b02-e-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: mengevaluasi klaim banyak pasangan selisih kuadrat*

Budi menyatakan ada 6 pasangan bilangan asli $(a,b)$ dengan $a^2-b^2=45$, karena 45 memiliki 6 faktor positif. Pernyataan yang tepat tentang klaim Budi adalah ....

- A. Keliru; ada 2 pasangan, karena pasangan faktor $(3,15)$ menghasilkan $b$ yang bukan bilangan bulat  
  <sub>Salah: $(3,15)$ memberi $a=9$, $b=6$ yang bulat</sub>
- B. Benar, karena setiap faktor positif 45 menghasilkan satu pasangan $(a,b)$  
  <sub>Salah: menghitung faktor, bukan pasangan faktor</sub>
- C. Keliru; ada 4 pasangan, karena $a-b=45$ dan $a+b=1$ juga dihitung  
  <sub>Salah: pasangan itu memberi $b=-22$, bukan bilangan asli</sub>
- **D. Keliru; $(a-b)(a+b)=45$ dengan $a-b<a+b$ hanya memberi pasangan faktor $(1,45)$, $(3,15)$, $(5,9)$, sehingga ada 3 pasangan** ✅  
  <sub>Benar: setiap pasangan faktor dengan $p<q$ menghasilkan satu $(a,b)$: $(23,22)$, $(9,6)$, $(7,2)$.</sub>

**Pembahasan:** $a-b=p$, $a+b=q$, $pq=45$, $p<q$: $(1,45)\to(23,22)$, $(3,15)\to(9,6)$, $(5,9)\to(7,2)$. Jadi 3 pasangan.
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b02-e-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: mengevaluasi klaim bilangan prima*

Hasan menyatakan bahwa $9^4+4$ adalah bilangan prima, karena penjumlahan dua bilangan kuadrat ($(9^2)^2+2^2$) tidak dapat difaktorkan. Pernyataan yang tepat adalah ....

- A. Keliru, karena jumlah digit 6565 adalah 22 sehingga habis dibagi 3  
  <sub>Salah: salah aritmetika: 22 tidak habis dibagi 3</sub>
- **B. Keliru; $9^4+4=(9^2+2)^2-(2\cdot9)^2=101\cdot65$, sehingga bilangan komposit** ✅  
  <sub>Benar: dari $x^4+4=(x^2+2)^2-(2x)^2=(x^2+2x+2)(x^2-2x+2)$ dengan $x=9$ diperoleh $101\cdot65=6565$.</sub>
- C. Keliru; $9^4+4=(9^2+2)^2=83^2$, sehingga kuadrat sempurna  
  <sub>Salah: melupakan suku silang $2\cdot81\cdot2$ pada kuadrat binomial</sub>
- D. Benar, karena jumlah dua kuadrat tidak dapat difaktorkan  
  <sub>Salah: mengira bentuk $p^2+q^2$ tidak pernah dapat difaktorkan</sub>

**Pembahasan:** $9^4+4=6565$. Dengan $x^4+4=(x^2+2x+2)(x^2-2x+2)$ dan $x=9$: $101\cdot65=6565$, sehingga komposit (bahkan $5\cdot13\cdot101$).
**Acuan:** siswa — siswa hal.104

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
