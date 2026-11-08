# Lembar koreksi — kelas11 SMA11U-B2 subbab B: Lingkaran dan Garis Singgung

59 soal | easy 20, medium 20, hard 19 | variasi 28, orisinal 31
> **Kapasitas kurang (hard): 19 dari kuota 20** — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b02-b-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: panjang garis singgung titik ke lingkaran*

Jari-jari lingkaran berpusat di $O$ adalah $8\text{ cm}$. Jika titik $Q$ berada di luar lingkaran dengan jarak $17\text{ cm}$ dari titik $O$, panjang garis singgung dari titik $Q$ ke titik singgung $T$ pada lingkaran adalah ....

- A. $\sqrt{353}\text{ cm}$  
  <sub>Salah: Menjumlahkan kuadrat sisi $\sqrt{17^2 + 8^2}$ seolah-olah garis singgung adalah sisi miring.</sub>
- B. $9\text{ cm}$  
  <sub>Salah: Mengurangkan langsung $17 - 8$ tanpa menguadratkan pada rumus Pythagoras.</sub>
- C. $25\text{ cm}$  
  <sub>Salah: Menjumlahkan langsung $17 + 8$.</sub>
- **D. $15\text{ cm}$** ✅  
  <sub>Benar: Segitiga $OTQ$ siku-siku di $T$, sehingga $QT = \sqrt{OQ^2 - OT^2} = \sqrt{17^2 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$.</sub>

**Pembahasan:** Garis singgung lingkaran tegak lurus dengan jari-jari di titik singgung, sehingga $\triangle OTQ$ siku-siku di $T$.
$$\begin{aligned} QT &= \sqrt{OQ^2 - OT^2} \\ &= \sqrt{17^2 - 8^2} \\ &= \sqrt{289 - 64} \\ &= \sqrt{225} \\ &= 15\text{ cm} \end{aligned}$$
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b02-b-easy-bt01-002
*variasi (angka) | C2 | 1 langkah | jenis: sudut antara dua garis singgung*

Dua garis singgung ditarik dari titik $P$ di luar lingkaran dan menyinggung lingkaran berpusat $O$ di titik $A$ dan $B$. Jika besar sudut pusat $\angle AOB = 124^\circ$, maka besar $\angle APB$ adalah ....

- **A. $56^\circ$** ✅  
  <sub>Benar: Jumlah sudut yang berhadapan pada segi empat garis singgung adalah $180^\circ$, sehingga $\angle APB = 180^\circ - 124^\circ = 56^\circ$.</sub>
- B. $62^\circ$  
  <sub>Salah: Membagi dua sudut pusat $\frac{124^\circ}{2}$.</sub>
- C. $116^\circ$  
  <sub>Salah: Mengurangkan dari $240^\circ$ atau salah mengaitkan jumlah sudut.</sub>
- D. $66^\circ$  
  <sub>Salah: Salah menghitung pengurangan $180^\circ - 124^\circ$.</sub>

**Pembahasan:** Karena garis singgung tegak lurus jari-jari pada titik singgung, maka $\angle OAP = \angle OBP = 90^\circ$. Jumlah sudut segi empat $OAPB$ adalah $360^\circ$, sehingga:
$$\angle APB = 180^\circ - \angle AOB = 180^\circ - 124^\circ = 56^\circ$$
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b02-b-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: garis singgung persekutuan luar*

Dua buah lingkaran memiliki jari-jari masing-masing $9\text{ cm}$ dan $4\text{ cm}$. Jika jarak antara pusat kedua lingkaran tersebut adalah $13\text{ cm}$, maka panjang garis singgung persekutuan luarnya adalah ....

- A. $10\text{ cm}$  
  <sub>Salah: Salah melakukan perhitungan akar atau mengira tripel Pythagoras lain.</sub>
- B. $\sqrt{138}\text{ cm}$  
  <sub>Salah: Salah mengurangkan jari-jari tanpa menguadratkannya terlebih dahulu.</sub>
- C. $\sqrt{338}\text{ cm}$  
  <sub>Salah: Menggunakan tanda tambah pada rumus garis singgung persekutuan luar sehingga menjadi $\sqrt{13^2 + 13^2}$.</sub>
- **D. $12\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung persekutuan luar $s = \sqrt{d^2 - (R - r)^2} = \sqrt{13^2 - (9 - 4)^2} = \sqrt{169 - 25} = 12\text{ cm}$.</sub>

**Pembahasan:** Rumus panjang garis singgung persekutuan luar:
$$\begin{aligned} s &= \sqrt{d^2 - (R - r)^2} \\ &= \sqrt{13^2 - (9 - 4)^2} \\ &= \sqrt{169 - 25} \\ &= \sqrt{144} \\ &= 12\text{ cm} \end{aligned}$$
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b02-b-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: sifat garis singgung dan jari-jari*

Besar sudut yang dibentuk oleh garis singgung lingkaran dan jari-jari lingkaran yang ditarik ke titik singgungnya adalah ....

- A. $45^\circ$  
  <sub>Salah: Terkecoh dengan sudut separuh siku-siku.</sub>
- B. $180^\circ$  
  <sub>Salah: Terkecoh dengan sudut garis lurus (berimpit atau berpelurus).</sub>
- **C. $90^\circ$** ✅  
  <sub>Benar: Garis singgung dan jari-jari lingkaran di titik singgung selalu berpotongan tegak lurus ($90^\circ$).</sub>
- D. $60^\circ$  
  <sub>Salah: Terkecoh dengan sudut segitiga sama sisi.</sub>

**Pembahasan:** Berdasarkan sifat lingkaran, garis singgung selalu tegak lurus terhadap jari-jari lingkaran yang melalui titik singgung tersebut, sehingga membentuk sudut $90^\circ$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b02-b-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: definisi garis pada lingkaran*

Garis lurus yang memotong suatu lingkaran tepat pada dua titik disebut garis ....

- A. tembereng  
  <sub>Salah: Tembereng adalah daerah bidang di dalam lingkaran, bukan garis.</sub>
- **B. sekan** ✅  
  <sub>Benar: Garis sekan didefinisikan sebagai garis yang memotong lingkaran pada dua titik.</sub>
- C. singgung  
  <sub>Salah: Garis singgung memotong lingkaran tepat pada satu titik, bukan dua titik.</sub>
- D. apotema  
  <sub>Salah: Apotema adalah ruas garis tegak lurus dari titik pusat ke tali busur.</sub>

**Pembahasan:** Garis yang memotong lingkaran pada dua titik disebut garis sekan, sedangkan garis yang menyentuh lingkaran tepat pada satu titik disebut garis singgung.
**Acuan:** siswa — siswa hal.79

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b02-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: panjang garis singgung persekutuan dalam*

Dua buah lingkaran memiliki pusat yang berjarak $17\text{ cm}$. Jika jari-jari kedua lingkaran tersebut masing-masing adalah $5\text{ cm}$ dan $3\text{ cm}$, panjang garis singgung persekutuan dalam kedua lingkaran adalah ....

- A. $8\text{ cm}$  
  <sub>Salah: Hanya menghitung jumlah jari-jari lingkaran ($5 + 3 = 8$) tanpa menyelesaikan rumus Pythagoras.</sub>
- B. $23\text{ cm}$  
  <sub>Salah: Salah menjumlahkan jarak pusat dengan jari-jari lingkaran kedua lingkaran ($17 + 5 + 3$ lalu dikurangi sebagian sehingga salah operasi).</sub>
- C. $9\text{ cm}$  
  <sub>Salah: Hanya mengurangkan jarak pusat dengan jumlah jari-jari ($17 - 8 = 9$) bukan menggunakan rumus kuadrat.</sub>
- **D. $15\text{ cm}$** ✅  
  <sub>Benar: Menggunakan rumus $g = \sqrt{d^2 - (R + r)^2} = \sqrt{17^2 - (5 + 3)^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$.</sub>

**Pembahasan:** Diketahui jarak antar pusat lingkaran $d = 17\text{ cm}$, $R = 5\text{ cm}$, dan $r = 3\text{ cm}$.
Panjang garis singgung persekutuan dalam ($g$):
$$g = \sqrt{d^2 - (R + r)^2}$$
$$g = \sqrt{17^2 - (5 + 3)^2}$$
$$g = \sqrt{289 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$$.
Jadi, panjang garis singgung persekutuan dalam kedua lingkaran adalah $15\text{ cm}$.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b02-b-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: garis singgung dari titik luar lingkaran*

Lingkaran $M$ memiliki jari-jari $5\text{ cm}$. Sebuah titik $K$ terletak di luar lingkaran dan berjarak $13\text{ cm}$ dari pusat $M$. Jika titik $L$ adalah titik singgung pada lingkaran, maka panjang garis singgung $KL$ adalah ....

- A. $8\text{ cm}$  
  <sub>Salah: Hanya mengurangkan jarak titik ke pusat dengan jari-jari lingkaran ($13 - 5 = 8$).</sub>
- B. $18\text{ cm}$  
  <sub>Salah: Menjumlahkan jarak titik ke pusat dengan jari-jari lingkaran ($13 + 5 = 18$).</sub>
- C. $14\text{ cm}$  
  <sub>Salah: Kesalahan perhitungan saat mengakarkan selisih kuadrat.</sub>
- **D. $12\text{ cm}$** ✅  
  <sub>Benar: Garis singgung tegak lurus jari-jari sehingga panjang garis singgung adalah $\sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\text{ cm}$.</sub>

**Pembahasan:** Garis singgung $KL$ tegak lurus dengan jari-jari $ML$ di titik singgung $L$, sehingga segitiga $MLK$ siku-siku di $L$.
Dengan Teorema Pythagoras:
$$KL = \sqrt{KM^2 - ML^2}$$
$$KL = \sqrt{13^2 - 5^2} = \sqrt{169 - 25} = \sqrt{144} = 12\text{ cm}$$.
Jadi, panjang garis singgung $KL$ adalah $12\text{ cm}$.
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b02-b-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: sudut garis singgung dan pusat lingkaran*

Garis $PB$ dan $PC$ merupakan garis singgung lingkaran berpusat di $O$ dengan titik singgung berturut-turut di $B$ dan $C$. Jika besar $\angle BOC = 110^\circ$, maka besar $\angle BPC$ adalah ....

- A. $110^\circ$  
  <sub>Salah: Mengira sudut di luar lingkaran bernilai sama persis dengan sudut pusat lingkaran.</sub>
- B. $55^\circ$  
  <sub>Salah: Menganggap sudut tersebut adalah sudut keliling yang menghadap busur yang sama (setengah dari sudut pusat: $110^\circ / 2$).</sub>
- **C. $70^\circ$** ✅  
  <sub>Benar: Karena $\angle OBP = \angle OCP = 90^\circ$, maka $\angle BPC = 180^\circ - \angle BOC = 180^\circ - 110^\circ = 70^\circ$.</sub>
- D. $20^\circ$  
  <sub>Salah: Salah mengurangkan dari sudut siku-siku ($90^\circ - 70^\circ = 20^\circ$).</sub>

**Pembahasan:** Segiempat $OBPC$ memiliki jumlah sudut $360^\circ$.
Karena $PB$ dan $PC$ adalah garis singgung, maka jari-jari $OB \perp PB$ dan $OC \perp PC$, sehingga $\angle OBP = 90^\circ$ dan $\angle OCP = 90^\circ$.
Maka:
$$\angle BPC = 180^\circ - \angle BOC$$
$$\angle BPC = 180^\circ - 110^\circ = 70^\circ$$.
Jadi, besar $\angle BPC$ adalah $70^\circ$.
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b02-b-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: banyak garis singgung dari titik luar*

Banyaknya garis singgung lingkaran yang dapat ditarik dari sebuah titik yang terletak di luar lingkaran adalah ....

- A. 1  
  <sub>Salah: Terkecoh dengan titik yang berada tepat pada lingkaran, di mana hanya bisa ditarik tepat 1 garis singgung.</sub>
- B. tak terhingga  
  <sub>Salah: Mengira dari satu titik sembarang bisa ditarik garis singgung sebanyak-banyaknya tanpa batas.</sub>
- **C. 2** ✅  
  <sub>Benar: Sesuai sifat garis singgung lingkaran, dari satu titik di luar lingkaran dapat ditarik tepat 2 garis singgung yang panjangnya sama.</sub>
- D. 3  
  <sub>Salah: Mengira ada garis tambahan yang memotong bagian tengah lingkaran.</sub>

**Pembahasan:** Berdasarkan sifat geometris lingkaran, dari sebuah titik yang berada di luar lingkaran dapat dibuat tepat 2 garis singgung ke lingkaran tersebut, dan kedua garis singgung tersebut memiliki panjang ruas garis yang sama.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b02-b-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: definisi titik persekutuan garis singgung*

Garis singgung lingkaran menyentuh lingkaran tepat pada satu titik. Titik potong atau titik temu antara garis singgung dengan keliling lingkaran tersebut dinamakan ....

- **A. titik singgung** ✅  
  <sub>Benar: Berdasarkan definisi matematis, titik persekutuan antara garis singgung dan lingkaran disebut titik singgung.</sub>
- B. titik apotema  
  <sub>Salah: Tertukar dengan istilah apotema yaitu ruas garis tegak lurus dari titik pusat ke tali busur.</sub>
- C. titik potong sekan  
  <sub>Salah: Tertukar dengan titik tembus dari garis sekan yang memotong lingkaran di dua titik.</sub>
- D. titik pusat  
  <sub>Salah: Tertukar dengan titik yang berada tepat di tengah-tengah lingkaran.</sub>

**Pembahasan:** Titik potong antara garis singgung dengan lingkaran hanya ada satu titik dan titik pertemuan tersebut dinamakan titik singgung.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b02-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: perhitungan garis singgung persekutuan luar*

Dua buah lingkaran masing-masing memiliki jari-jari $11\text{ cm}$ dan $4\text{ cm}$. Jika jarak antara kedua pusat lingkaran tersebut adalah $25\text{ cm}$, maka panjang garis singgung persekutuan luarnya adalah ....

- **A. $24\text{ cm}$** ✅  
  <sub>Benar: Menggunakan rumus garis singgung persekutuan luar $l = \sqrt{d^2 - (R - r)^2} = \sqrt{25^2 - (11 - 4)^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$.</sub>
- B. $26\text{ cm}$  
  <sub>Salah: Siswa keliru menjumlahkan suku dalam akar Teorema Pythagoras: $\sqrt{25^2 + 7^2} \approx 26\text{ cm}$.</sub>
- C. $20\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan rumus persekutuan dalam dengan menjumlahkan kedua jari-jari: $\sqrt{25^2 - (11 + 4)^2} = \sqrt{625 - 225} = 20\text{ cm}$.</sub>
- D. $18\text{ cm}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan saat mengurangkan kuadrat di dalam akar: $\sqrt{625 - 301} = 18\text{ cm}$.</sub>

**Pembahasan:** Diketahui:
- $R = 11\text{ cm}$
- $r = 4\text{ cm}$
- $d = 25\text{ cm}$

Panjang garis singgung persekutuan luar ($l$):
$$\begin{aligned} l &= \sqrt{d^2 - (R - r)^2} \\ &= \sqrt{25^2 - (11 - 4)^2} \\ &= \sqrt{625 - 7^2} \\ &= \sqrt{625 - 49} \\ &= \sqrt{576} \\ &= 24\text{ cm} \end{aligned}$$

Jadi, panjang garis singgung persekutuan luarnya adalah $24\text{ cm}$.
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b02-b-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: perbandingan garis singgung persekutuan*

Pada dua lingkaran terpisah yang memiliki garis singgung persekutuan luar dan dalam, manakah pernyataan berikut yang selalu benar mengenai panjang kedua jenis garis singgung tersebut?

- A. Garis singgung persekutuan dalam selalu sama panjang dengan garis singgung persekutuan luar.  
  <sub>Salah: Siswa mengira kedua garis singgung memiliki sifat kongruensi yang sama tanpa memperhatikan rumus pengurangnya.</sub>
- B. Panjang garis singgung persekutuan dalam tidak dapat ditentukan hubungannya dengan garis singgung persekutuan luar.  
  <sub>Salah: Siswa mengira hubungan panjang kedua garis singgung bergantung mutlak pada posisi pusat lingkaran.</sub>
- **C. Garis singgung persekutuan dalam selalu lebih pendek daripada garis singgung persekutuan luar.** ✅  
  <sub>Benar: Karena pengurang pada rumus persekutuan dalam adalah $(R+r)^2$ sedangkan pada persekutuan luar adalah $(R-r)^2$, nilai di dalam akar untuk persekutuan dalam selalu lebih kecil sehingga panjangnya selalu lebih pendek.</sub>
- D. Garis singgung persekutuan dalam selalu lebih panjang daripada garis singgung persekutuan luar.  
  <sub>Salah: Siswa terbalik menginterpretasikan perbandingan nilai kedua rumus garis singgung.</sub>

**Pembahasan:** Rumus panjang garis singgung persekutuan luar ($l$) dan dalam ($g$) adalah:
- $l = \sqrt{d^2 - (R - r)^2}$
- $g = \sqrt{d^2 - (R + r)^2}$

Karena $(R + r) > (R - r)$ untuk $R, r > 0$, maka $(R + r)^2 > (R - r)^2$. Akibatnya, nilai di bawah tanda akar untuk $g$ selalu lebih kecil daripada $l$, sehingga garis singgung persekutuan dalam selalu lebih pendek daripada garis singgung persekutuan luar.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b02-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: kesamaan panjang garis singgung titik luar*

Dari sebuah titik $P$ di luar lingkaran ditarik dua buah garis singgung yang menyentuh lingkaran di titik $A$ dan titik $B$. Jika panjang ruas garis singgung $PA = 18\text{ cm}$, maka panjang ruas garis singgung $PB$ adalah ....

- A. $36\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan atau melipatgandakan panjang garis singgung.</sub>
- **B. $18\text{ cm}$** ✅  
  <sub>Benar: Sifat garis singgung menyatakan bahwa dari satu titik di luar lingkaran dapat dibuat dua garis singgung yang sama panjang, sehingga $PB = PA = 18\text{ cm}$.</sub>
- C. $9\text{ cm}$  
  <sub>Salah: Siswa keliru membagi panjang garis singgung menjadi dua.</sub>
- D. $24\text{ cm}$  
  <sub>Salah: Siswa menebak angka tripel Pythagoras yang umum tanpa memperhatikan sifat kesamaan panjang.</sub>

**Pembahasan:** Berdasarkan sifat garis singgung lingkaran, dua garis singgung yang ditarik dari satu titik di luar lingkaran menuju lingkaran yang sama memiliki panjang yang sama.

Karena panjang $PA = 18\text{ cm}$, maka panjang $PB = PA = 18\text{ cm}$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b02-b-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: kedudukan garis singgung dan jari-jari*

Kedudukan antara garis singgung suatu lingkaran dengan jari-jari lingkaran yang ditarik melalui titik singgungnya adalah saling ....

- A. bersilangan  
  <sub>Salah: Siswa memakai istilah kedudukan garis dalam ruang tiga dimensi yang tidak tepat untuk geometri bidang datar.</sub>
- **B. tegak lurus** ✅  
  <sub>Benar: Sesuai sifat lingkaran, garis singgung selalu berpotongan tegak lurus ($90^\circ$) dengan jari-jari di titik singgungnya.</sub>
- C. berimpit  
  <sub>Salah: Siswa salah memahami konsep garis singgung sebagai bagian dari jari-jari.</sub>
- D. sejajar  
  <sub>Salah: Siswa keliru mengira garis singgung searah dengan jari-jari.</sub>

**Pembahasan:** Salah satu sifat utama garis singgung lingkaran adalah bahwa garis singgung dan jari-jari lingkaran yang melalui titik singgung selalu berpotongan tegak lurus (membentuk sudut $90^\circ$).
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b02-b-easy-bt01-015
*variasi (konteks) | C1 | 1 langkah | jenis: perbandingan panjang garis singgung persekutuan*

Dua buah lingkaran terpisah memiliki garis singgung persekutuan luar dan garis singgung persekutuan dalam. Manakah di antara kedua garis singgung tersebut yang selalu memiliki ukuran lebih pendek?

- A. Tergantung pada jarak kedua pusat lingkaran  
  <sub>Salah: Siswa menduga bahwa perbandingan panjang garis singgung luar dan dalam ditentukan oleh besarnya jarak pusat.</sub>
- B. Keduanya selalu sama panjang  
  <sub>Salah: Siswa keliru mengira garis singgung persekutuan luar dan dalam selalu memiliki panjang yang sama.</sub>
- C. Garis singgung persekutuan luar  
  <sub>Salah: Siswa terbalik mengingat sifat perbandingan panjang garis singgung persekutuan.</sub>
- **D. Garis singgung persekutuan dalam** ✅  
  <sub>Benar: Karena pengurang pada garis singgung dalam adalah $(R+r)^2$ sedangkan pada garis singgung luar adalah $(R-r)^2$, nilai garis singgung dalam selalu lebih pendek.</sub>

**Pembahasan:** Panjang garis singgung persekutuan luar adalah $s = \sqrt{d^2 - (R - r)^2}$, sedangkan garis singgung persekutuan dalam adalah $g = \sqrt{d^2 - (R + r)^2}$. Karena $(R + r) > (R - r)$ untuk $r > 0$, maka pengurang pada $g$ selalu lebih besar, sehingga garis singgung persekutuan dalam selalu lebih pendek daripada garis singgung persekutuan luar.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b02-b-easy-bt01-016
*variasi (konteks) | C1 | 1 langkah | jenis: rumus garis singgung persekutuan*

Jika jarak antara dua pusat lingkaran adalah $d$, serta jari-jari kedua lingkaran berturut-turut adalah $R$ dan $r$ (dengan $R \ge r$), maka rumus untuk menentukan panjang garis singgung persekutuan dalam ($g$) adalah ....

- **A. $g = \sqrt{d^2 - (R + r)^2}$** ✅  
  <sub>Benar: Berdasarkan teorema Pythagoras pada segitiga bantu, panjang garis singgung persekutuan dalam memenuhi $g = \sqrt{d^2 - (R + r)^2}$.</sub>
- B. $g = \sqrt{d^2 + (R + r)^2}$  
  <sub>Salah: Siswa keliru menggunakan tanda penjumlahan pada teorema Pythagoras sisi tegak.</sub>
- C. $g = \sqrt{d^2 - (R^2 + r^2)}$  
  <sub>Salah: Siswa mengkuadratkan jari-jari masing-masing sebelum menjumlahkan, bukan mengkuadratkan jumlahnya.</sub>
- D. $g = \sqrt{d^2 - (R - r)^2}$  
  <sub>Salah: Siswa tertukar dengan rumus garis singgung persekutuan luar.</sub>

**Pembahasan:** Pada garis singgung persekutuan dalam, kedua jari-jari dijumlahkan terlebih dahulu sebagai sisi tegak segitiga bantu siku-siku, sehingga berlaku $g = \sqrt{d^2 - (R + r)^2}$.
**Acuan:** siswa — siswa hal.82 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b02-b-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: jumlah titik potong garis singgung*

Berdasarkan sifat dasarnya, sebuah garis singgung memotong atau menyentuh lingkaran tepat pada ....

- A. 2 titik  
  <sub>Salah: Siswa tertukar dengan definisi garis sekan yang memotong lingkaran pada dua titik.</sub>
- B. 0 titik  
  <sub>Salah: Siswa menganggap garis di luar lingkaran yang tidak menyentuh lingkaran sama sekali.</sub>
- **C. 1 titik** ✅  
  <sub>Benar: Sesuai definisi, garis singgung lingkaran hanya bersekutu atau berpotongan dengan lingkaran pada tepat satu titik.</sub>
- D. 3 titik  
  <sub>Salah: Siswa keliru memahami sifat garis lurus terhadap bangun lingkaran lengkung tertutup.</sub>

**Pembahasan:** Garis singgung lingkaran adalah garis yang berpotongan atau menyentuh lingkaran tepat pada satu titik. Titik tersebut dinamakan titik singgung.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b02-b-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: kesamaan ruas garis singgung*

Dua buah garis singgung ditarik dari sebuah titik $M$ di luar lingkaran dan masing-masing menyinggung lingkaran di titik $P$ dan $Q$. Hubungan antara panjang ruas garis singgung $MP$ dan $MQ$ adalah ....

- **A. $MP = MQ$** ✅  
  <sub>Benar: Dua garis singgung yang ditarik dari satu titik di luar lingkaran ke sebuah lingkaran selalu memiliki panjang yang sama.</sub>
- B. $MP + MQ = 0$  
  <sub>Salah: Siswa salah memahami konsep panjang ruas garis non-negatif.</sub>
- C. $MP > MQ$  
  <sub>Salah: Siswa mengira garis singgung yang ditarik pertama lebih panjang daripada garis singgung kedua.</sub>
- D. $MP < MQ$  
  <sub>Salah: Siswa mengira ruas garis singgung memiliki panjang yang berbeda tergantung letak titik singgungnya.</sub>

**Pembahasan:** Sesuai sifat garis singgung lingkaran, dari satu titik di luar lingkaran dapat dibentuk dua garis singgung yang panjangnya sama. Oleh karena itu, $MP = MQ$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b02-b-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: kalkulasi persekutuan dalam lingkaran*

Dua buah lingkaran memiliki titik pusat yang berjarak $29\text{ cm}$. Jika kedua lingkaran tersebut masing-masing memiliki jari-jari sepanjang $13\text{ cm}$ dan $8\text{ cm}$, maka panjang garis singgung persekutuan dalam kedua lingkaran tersebut adalah ....

- A. $21\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung jumlah jari-jari $(R + r) = 13 + 8 = 21\text{ cm}$.</sub>
- **B. $20\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung persekutuan dalam dihitung dengan $g = \sqrt{d^2 - (R + r)^2} = \sqrt{29^2 - (13 + 8)^2} = \sqrt{841 - 441} = \sqrt{400} = 20\text{ cm}$.</sub>
- C. $\sqrt{816}\text{ cm}$  
  <sub>Salah: Siswa keliru menggunakan rumus garis singgung persekutuan luar: $\sqrt{29^2 - (13 - 8)^2} = \sqrt{841 - 25} = \sqrt{816}\text{ cm}$.</sub>
- D. $18\text{ cm}$  
  <sub>Salah: Kesalahan perhitungan penarikan akar kuadrat dari selisih kuadrat.</sub>

**Pembahasan:** Diketahui:
- Jarak kedua pusat ($d$) = $29\text{ cm}$
- Jari-jari lingkaran besar ($R$) = $13\text{ cm}$
- Jari-jari lingkaran kecil ($r$) = $8\text{ cm}$

Panjang garis singgung persekutuan dalam ($g$):
$$g = \sqrt{d^2 - (R + r)^2}$$
$$g = \sqrt{29^2 - (13 + 8)^2}$$
$$g = \sqrt{841 - 21^2}$$
$$g = \sqrt{841 - 441}$$
$$g = \sqrt{400} = 20\text{ cm}$$

Jadi, panjang garis singgung persekutuan dalam kedua lingkaran tersebut adalah $20\text{ cm}$.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b02-b-easy-bt01-020
*variasi (konteks) | C2 | 1 langkah | jenis: rumus jarak pusat garis singgung persekutuan*

Diketahui dua buah lingkaran memiliki garis singgung persekutuan luar sepanjang $s$. Jika jari-jari kedua lingkaran berturut-turut adalah $R$ dan $r$ (dengan $R > r$), maka jarak kedua pusat lingkaran ($d$) dapat dinyatakan dengan rumus ....

- A. $d = \sqrt{s^2 + (R + r)^2}$  
  <sub>Salah: Tertukar dengan komponen penjumlahan jari-jari pada garis singgung persekutuan dalam.</sub>
- **B. $d = \sqrt{s^2 + (R - r)^2}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pythagoras pada segitiga pembentuk garis singgung persekutuan luar, berlaku $s^2 = d^2 - (R - r)^2$, sehingga $d^2 = s^2 + (R - r)^2$ atau $d = \sqrt{s^2 + (R - r)^2}$.</sub>
- C. $d = \sqrt{s^2 - (R - r)^2}$  
  <sub>Salah: Keliru menerapkan operasi pengurangan pada suku sisi siku-siku di bawah tanda akar.</sub>
- D. $d = \sqrt{s^2 - (R + r)^2}$  
  <sub>Salah: Tertukar dengan garis singgung persekutuan dalam sekaligus salah menggunakan tanda pengurangan.</sub>

**Pembahasan:** Hubungan antara panjang garis singgung persekutuan luar ($s$), jarak kedua pusat ($d$), dan jari-jari ($R$ dan $r$) diperoleh dari Teorema Pythagoras:
$$s = \sqrt{d^2 - (R - r)^2}$$
Kuadratkan kedua ruas:
$$s^2 = d^2 - (R - r)^2$$
Pindahkan suku $(R - r)^2$ ke ruas kiri:
$$d^2 = s^2 + (R - r)^2$$
$$d = \sqrt{s^2 + (R - r)^2}$$
Jadi, rumus untuk menentukan jarak kedua pusat lingkaran adalah $d = \sqrt{s^2 + (R - r)^2}$.
**Acuan:** siswa — siswa hal.82 5. Garis singgung persekutuan luar

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b02-b-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: panjang garis singgung persekutuan luar*

Tentukan panjang garis singgung persekutuan luarnya jika jari-jari lingkaran yang lebih besar $= 14\text{ cm}$, jari-jari lingkaran yang lebih kecil $= 6\text{ cm}$, dan jarak antar kedua pusat lingkaran $= 17\text{ cm}$.

- **A. $15\text{ cm}$** ✅  
  <sub>Benar: $s = \sqrt{d^2 - (R - r)^2} = \sqrt{17^2 - (14 - 6)^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$.</sub>
- B. $13\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan jari-jari seperti pada rumus garis singgung persekutuan dalam: $\sqrt{17^2 - (14+6)^2}$ tidak terdefinisi real, lalu mengira $17 - 4$ atau salah hitung tripel.</sub>
- C. $\sqrt{353}\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan kuadrat pada Teorema Pythagoras alih-alih mengurangkannya: $\sqrt{17^2 + 8^2} = \sqrt{353}\text{ cm}$.</sub>
- D. $9\text{ cm}$  
  <sub>Salah: Siswa langsung mengurangkan jarak pusat dengan selisih jari-jari: $17 - (14 - 6) = 9\text{ cm}$ tanpa Teorema Pythagoras.</sub>

**Pembahasan:** Gunakan rumus panjang garis singgung persekutuan luar:
$$s = \sqrt{d^2 - (R - r)^2}$$
Diketahui $d = 17\text{ cm}$, $R = 14\text{ cm}$, dan $r = 6\text{ cm}$.
$$s = \sqrt{17^2 - (14 - 6)^2} = \sqrt{289 - 8^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$$
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b02-b-medium-bt01-002
*variasi (angka) | C3 | 2 langkah | jenis: panjang garis singgung persekutuan dalam*

Dua buah lingkaran, pusatnya berjarak $26\text{ cm}$. Jika kedua lingkaran tersebut masing-masing berjari-jari $4\text{ cm}$ dan $6\text{ cm}$, berapakah panjang garis singgung persekutuan dalamnya?

- A. $\sqrt{776}\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan kuadrat pada Teorema Pythagoras: $\sqrt{26^2 + 10^2} = \sqrt{776}\text{ cm}$.</sub>
- **B. $24\text{ cm}$** ✅  
  <sub>Benar: $g = \sqrt{d^2 - (R + r)^2} = \sqrt{26^2 - (6 + 4)^2} = \sqrt{676 - 100} = \sqrt{576} = 24\text{ cm}$.</sub>
- C. $16\text{ cm}$  
  <sub>Salah: Siswa mengurangkan jarak pusat langsung dengan jumlah jari-jari: $26 - (6 + 4) = 16\text{ cm}$.</sub>
- D. $25\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan rumus persekutuan luar dengan selisih jari-jari: $\sqrt{26^2 - (6-4)^2} = \sqrt{676 - 4} = \sqrt{672} \approx 25,9\text{ cm}$ lalu membulatkannya keliru.</sub>

**Pembahasan:** Gunakan rumus garis singgung persekutuan dalam:
$$g = \sqrt{d^2 - (R + r)^2}$$
Diketahui $d = 26\text{ cm}$, $R = 6\text{ cm}$, dan $r = 4\text{ cm}$.
$$g = \sqrt{26^2 - (6 + 4)^2} = \sqrt{676 - 10^2} = \sqrt{676 - 100} = \sqrt{576} = 24\text{ cm}$$
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b02-b-medium-bt01-003
*orisinal | C3 | 2 langkah | jenis: teorema Pitot*

Sebuah segiempat garis singgung $ABCD$ melingkupi sebuah lingkaran sedemikian sehingga sisi-sisi $AB$, $BC$, $CD$, dan $DA$ bertindak sebagai garis singgung lingkaran. Jika diketahui panjang sisi $AB = 12\text{ cm}$, $BC = 9\text{ cm}$, dan $CD = 15\text{ cm}$, berapakah panjang sisi $AD$?

- A. $21\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan $12 + 9 = 21\text{ cm}$ dan langsung menganggapnya panjang sisi $AD$.</sub>
- B. $12\text{ cm}$  
  <sub>Salah: Siswa mengira segiempat tersebut jajar genjang sehingga sisi yang berhadapan sama panjang ($AD = BC$ keliru dihitung).</sub>
- C. $6\text{ cm}$  
  <sub>Salah: Siswa mengira $AB + BC = CD + AD \implies 12 + 9 = 15 + AD \implies AD = 6\text{ cm}$ (memasangkan sisi yang berdekatan).</sub>
- **D. $18\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pitot, $AB + CD = BC + AD \implies 12 + 15 = 9 + AD \implies AD = 27 - 9 = 18\text{ cm}$.</sub>

**Pembahasan:** Berdasarkan Teorema Pitot, pada segiempat garis singgung, jumlah panjang dua pasang sisi yang saling berhadapan adalah sama:
$$AB + CD = BC + AD$$
Substitusikan nilai yang diketahui:
$$12 + 15 = 9 + AD$$
$$27 = 9 + AD$$
$$AD = 27 - 9 = 18\text{ cm}$$
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b02-b-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: luas layang-layang garis singgung*

Titik $P$ berada di luar lingkaran yang berpusat di titik $O$ dengan jari-jari $9\text{ cm}$. Dari titik $P$ dibuat dua garis singgung yang menyentuh lingkaran di titik $A$ dan $B$. Jika jarak titik $P$ ke titik pusat $O$ adalah $15\text{ cm}$, berapakah luas layang-layang garis singgung $OAPB$?

- **A. $108\text{ cm}^2$** ✅  
  <sub>Benar: Panjang garis singgung $PA = \sqrt{15^2 - 9^2} = 12\text{ cm}$. Luas layang-layang $= 2 \times \text{luas}(\triangle OAP) = 2 \times \left(\frac{1}{2} \times 9 \times 12\right) = 108\text{ cm}^2$.</sub>
- B. $54\text{ cm}^2$  
  <sub>Salah: Siswa hanya menghitung luas satu segitiga siku-siku $\triangle OAP$ tanpa mengalikan dua.</sub>
- C. $135\text{ cm}^2$  
  <sub>Salah: Siswa mengalikan jari-jari dengan jarak pusat titik: $9 \times 15 = 135\text{ cm}^2$.</sub>
- D. $216\text{ cm}^2$  
  <sub>Salah: Siswa lupa membagi dua pada rumus luas segitiga sebelum mengalikan dua: $2 \times (9 \times 12) = 216\text{ cm}^2$.</sub>

**Pembahasan:** Garis singgung tegak lurus terhadap jari-jari di titik singgung, sehingga $\triangle OAP$ siku-siku di $A$.
1. Tentukan panjang garis singgung $PA$:
$$PA = \sqrt{OP^2 - OA^2} = \sqrt{15^2 - 9^2} = \sqrt{225 - 81} = \sqrt{144} = 12\text{ cm}$$
2. Hitung luas layang-layang $OAPB$ yang terdiri dari dua segitiga siku-siku kongruen ($\triangle OAP$ dan $\triangle OBP$):
$$\text{Luas } OAPB = 2 \times \left(\frac{1}{2} \times OA \times PA\right) = 9 \times 12 = 108\text{ cm}^2$$
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b02-b-medium-bt01-005
*orisinal | C4 | 3 langkah | jenis: jari-jari dari garis singgung persekutuan dalam*

Panjang garis singgung persekutuan dalam dua buah lingkaran adalah $16\text{ cm}$ dan jarak kedua titik pusatnya adalah $20\text{ cm}$. Jika perbandingan panjang jari-jari lingkaran besar dan lingkaran kecil adalah $2 : 1$, berapakah panjang jari-jari lingkaran yang lebih besar?

- A. $6\text{ cm}$  
  <sub>Salah: Siswa membagi rata jumlah jari-jari: $12 : 2 = 6\text{ cm}$ tanpa memperhatikan perbandingan $2 : 1$.</sub>
- B. $4\text{ cm}$  
  <sub>Salah: Siswa menentukan jari-jari lingkaran kecil $r = \frac{1}{3} \times 12 = 4\text{ cm}$, bukan lingkaran besar.</sub>
- **C. $8\text{ cm}$** ✅  
  <sub>Benar: $R + r = \sqrt{d^2 - g^2} = \sqrt{20^2 - 16^2} = 12\text{ cm}$. Dengan rasio $2 : 1$, jari-jari lingkaran besar $R = \frac{2}{3} \times 12 = 8\text{ cm}$.</sub>
- D. $12\text{ cm}$  
  <sub>Salah: Siswa hanya menyelesaikan langkah pertama yaitu jumlah kedua jari-jari $R + r = 12\text{ cm}$.</sub>

**Pembahasan:** Rumus garis singgung persekutuan dalam adalah $g = \sqrt{d^2 - (R + r)^2}$.
1. Hitung jumlah jari-jari $(R + r)$:
$$(R + r)^2 = d^2 - g^2 = 20^2 - 16^2 = 400 - 256 = 144$$
$$R + r = \sqrt{144} = 12\text{ cm}$$
2. Tentukan panjang jari-jari lingkaran besar $R$ dengan perbandingan $R : r = 2 : 1$:
$$R = \frac{2}{2 + 1} \times 12 = \frac{2}{3} \times 12 = 8\text{ cm}$$
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b02-b-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: panjang garis singgung persekutuan luar*

Tentukan panjang garis singgung persekutuan luarnya jika jari-jari lingkaran yang lebih besar $= 16\text{ cm}$, jari-jari lingkaran yang lebih kecil $= 7\text{ cm}$, dan jarak antar kedua pusat lingkaran $= 41\text{ cm}$.

- A. $42\text{ cm}$  
  <sub>Salah: Salah melakukan penarikan akar dari hasil selisih kuadrat.</sub>
- B. $\sqrt{1762}\text{ cm}$  
  <sub>Salah: Salah menggunakan tanda tambah pada Teorema Pythagoras sehingga menghitung $\sqrt{41^2 + 9^2}$.</sub>
- C. $32\text{ cm}$  
  <sub>Salah: Mengurangkan langsung jarak titik pusat dengan selisih jari-jari tanpa Teorema Pythagoras ($41 - 9 = 32$).</sub>
- **D. $40\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung persekutuan luar dihitung dengan rumus $s = \sqrt{d^2 - (R - r)^2} = \sqrt{41^2 - (16 - 7)^2} = \sqrt{1681 - 81} = \sqrt{1600} = 40\text{ cm}$.</sub>

**Pembahasan:** Langkah 1: Tentukan selisih kedua jari-jari lingkaran:
$$R - r = 16\text{ cm} - 7\text{ cm} = 9\text{ cm}$$

Langkah 2: Hitung panjang garis singgung persekutuan luar ($s$):
$$s = \sqrt{d^2 - (R - r)^2} = \sqrt{41^2 - 9^2} = \sqrt{1681 - 81} = \sqrt{1600} = 40\text{ cm}$$
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b02-b-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: sudut antara dua garis singgung*

Dua garis singgung ditarik dari titik $P$ di luar lingkaran dan menyinggung lingkaran berpusat di $O$ masing-masing di titik $A$ dan $B$. Titik $C$ terletak pada busur mayor $AB$ sedemikian sehingga besar $\angle ACB = 68^\circ$. Berapakah besar $\angle APB$?

- A. $136^\circ$  
  <sub>Salah: Berhenti di perhitungan sudut pusat $\angle AOB = 2 \times 68^\circ$ tanpa menghitung $\angle APB$.</sub>
- B. $112^\circ$  
  <sub>Salah: Langsung mengurangkan $180^\circ - 68^\circ$ tanpa mencari besar sudut pusat terlebih dahulu.</sub>
- C. $22^\circ$  
  <sub>Salah: Salah menggunakan sifat saling berkomplemen ($90^\circ - 68^\circ$).</sub>
- **D. $44^\circ$** ✅  
  <sub>Benar: Besar sudut pusat $\angle AOB = 2 \times 68^\circ = 136^\circ$. Karena jari-jari tegak lurus garis singgung di titik singgung, maka $\angle APB = 180^\circ - 136^\circ = 44^\circ$.</sub>

**Pembahasan:** Langkah 1: Sudut keliling $\angle ACB$ dan sudut pusat $\angle AOB$ menghadap busur yang sama, sehingga:
$$\angle AOB = 2 \times \angle ACB = 2 \times 68^\circ = 136^\circ$$

Langkah 2: Karena garis singgung tegak lurus dengan jari-jari lingkaran di titik singgung, maka $\angle PAO = 90^\circ$ dan $\angle PBO = 90^\circ$. Pada segiempat $PAOB$, jumlah sudutnya $360^\circ$, sehingga:
$$\angle APB = 180^\circ - \angle AOB = 180^\circ - 136^\circ = 44^\circ$$
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b02-b-medium-bt01-008
*variasi (konteks) | C4 | 3 langkah | jenis: selisih garis singgung persekutuan*

Dua buah lingkaran memiliki jarak antarpusat sebesar $25\text{ cm}$. Jari-jari lingkaran yang besar adalah $11\text{ cm}$ dan jari-jari lingkaran yang kecil adalah $4\text{ cm}$. Berapakah selisih panjang antara garis singgung persekutuan luar dan garis singgung persekutuan dalam kedua lingkaran tersebut?

- A. $2\text{ cm}$  
  <sub>Salah: Kesalahan pembulatan atau salah operasi pengurangan nilai akhir.</sub>
- B. $15\text{ cm}$  
  <sub>Salah: Mengira selisih panjang garis singgung sama dengan jumlah kedua jari-jari ($11 + 4 = 15$).</sub>
- **C. $4\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung luar adalah $24\text{ cm}$ dan panjang garis singgung dalam adalah $20\text{ cm}$, sehingga selisihnya $24\text{ cm} - 20\text{ cm} = 4\text{ cm}$.</sub>
- D. $7\text{ cm}$  
  <sub>Salah: Mengira selisih garis singgung sama dengan selisih jari-jari lingkaran ($11 - 4 = 7$).</sub>

**Pembahasan:** Langkah 1: Hitung panjang garis singgung persekutuan luar ($s$):
$$s = \sqrt{d^2 - (R - r)^2} = \sqrt{25^2 - (11 - 4)^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$$

Langkah 2: Hitung panjang garis singgung persekutuan dalam ($g$):
$$g = \sqrt{d^2 - (R + r)^2} = \sqrt{25^2 - (11 + 4)^2} = \sqrt{625 - 225} = \sqrt{400} = 20\text{ cm}$$

Langkah 3: Hitung selisih kedua garis singgung:
$$\text{Selisih} = s - g = 24\text{ cm} - 20\text{ cm} = 4\text{ cm}$$
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b02-b-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: panjang tali busur kontak*

Dari sebuah titik $P$ di luar lingkaran yang berpusat di $O$, ditarik dua garis singgung yang menyentuh lingkaran di titik $A$ dan $B$. Jika jari-jari lingkaran tersebut adalah $30\text{ cm}$ dan jarak titik $P$ ke pusat $O$ adalah $50\text{ cm}$, berapakah panjang tali busur $AB$?

- **A. $48\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung $PA = \sqrt{50^2 - 30^2} = 40\text{ cm}$. Jarak titik singgung ke garis pusat adalah $AT = \frac{OA \times PA}{OP} = \frac{30 \times 40}{50} = 24\text{ cm}$, sehingga panjang tali busur $AB = 2 \times 24 = 48\text{ cm}$.</sub>
- B. $40\text{ cm}$  
  <sub>Salah: Hanya menghitung panjang garis singgung $PA$ dan mengiranya sebagai panjang tali busur $AB$.</sub>
- C. $36\text{ cm}$  
  <sub>Salah: Salah menggunakan perbandingan kesebangunan pada segitiga siku-siku.</sub>
- D. $24\text{ cm}$  
  <sub>Salah: Hanya menghitung setengah dari tali busur $AB$ ($AT = 24\text{ cm}$) dan lupa mengalikan dua.</sub>

**Pembahasan:** Langkah 1: Segitiga $OAP$ siku-siku di $A$. Hitung panjang ruas garis singgung $PA$:
$$PA = \sqrt{OP^2 - OA^2} = \sqrt{50^2 - 30^2} = \sqrt{2500 - 900} = \sqrt{1600} = 40\text{ cm}$$

Langkah 2: Ruas garis $OP$ memotong tegak lurus tali busur $AB$ di titik $T$. Berdasarkan kesamaan luas $\triangle OAP$:
$$\text{Luas } \triangle OAP = \frac{1}{2} \times OA \times PA = \frac{1}{2} \times OP \times AT$$
$$AT = \frac{OA \times PA}{OP} = \frac{30 \times 40}{50} = 24\text{ cm}$$

Langkah 3: Karena $OP$ membagi tali busur $AB$ menjadi dua bagian yang sama panjang:
$$AB = 2 \times AT = 2 \times 24\text{ cm} = 48\text{ cm}$$
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b02-b-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: jari-jari dari garis singgung persekutuan luar*

Panjang garis singgung persekutuan luar dua buah lingkaran adalah $21\text{ cm}$ dan jarak antara kedua titik pusatnya adalah $29\text{ cm}$. Jika jari-jari lingkaran besar bernilai $5$ kali jari-jari lingkaran kecil, tentukan panjang jari-jari lingkaran yang besar.

- A. $5\text{ cm}$  
  <sub>Salah: Menjawab panjang jari-jari lingkaran yang kecil ($r$).</sub>
- **B. $25\text{ cm}$** ✅  
  <sub>Benar: Selisih jari-jari adalah $\sqrt{29^2 - 21^2} = 20\text{ cm}$. Dengan persamaan $5r - r = 20$, diperoleh $r = 5\text{ cm}$, sehingga $R = 5 \times 5 = 25\text{ cm}$.</sub>
- C. $20\text{ cm}$  
  <sub>Salah: Berhenti pada nilai selisih kedua jari-jari ($R - r$).</sub>
- D. $30\text{ cm}$  
  <sub>Salah: Salah menghitung nilai jari-jari besar dengan menjumlahkan selisih jari-jari dan jari-jari kecil dua kali ($20 + 2 \times 5$).</sub>

**Pembahasan:** Langkah 1: Hitung selisih jari-jari kedua lingkaran ($R - r$):
$$R - r = \sqrt{d^2 - s^2} = \sqrt{29^2 - 21^2} = \sqrt{841 - 441} = \sqrt{400} = 20\text{ cm}$$

Langkah 2: Substitusikan $R = 5r$ ke dalam persamaan selisih:
$$5r - r = 20$$
$$4r = 20 \implies r = 5\text{ cm}$$

Langkah 3: Hitung panjang jari-jari lingkaran besar ($R$):
$$R = 5r = 5 \times 5\text{ cm} = 25\text{ cm}$$
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b02-b-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: panjang garis singgung lingkaran*

Jika jari-jari lingkaran $A$ adalah $20\text{ cm}$ dan titik $P$ berjarak $29\text{ cm}$ dari titik pusat $A$, berapakah panjang garis singgung $PB$ jika $B$ adalah titik singgung pada lingkaran?

- A. $9\text{ cm}$  
  <sub>Salah: Hanya mengurangkan jarak titik ke pusat dengan jari-jari tanpa menggunakan Teorema Pythagoras.</sub>
- B. $23\text{ cm}$  
  <sub>Salah: Salah menghitung akar kuadrat dari selisih kuadrat.</sub>
- **C. $21\text{ cm}$** ✅  
  <sub>Benar: Garis singgung $PB$ tegak lurus jari-jari $AB$ di titik $B$, membentuk segitiga siku-siku $ABP$. Panjang $PB = \sqrt{AP^2 - AB^2} = \sqrt{29^2 - 20^2} = \sqrt{841 - 400} = \sqrt{441} = 21\text{ cm}$.</sub>
- D. $\sqrt{1.241}\text{ cm}$  
  <sub>Salah: Menjumlahkan kuadrat sisi miring dan jari-jari alih-alih mengurangkannya.</sub>

**Pembahasan:** Diketahui:
- Jari-jari lingkaran $r = AB = 20\text{ cm}$
- Jarak titik $P$ ke pusat $A$ adalah $AP = 29\text{ cm}$

Karena garis singgung tegak lurus dengan jari-jari di titik singgung, maka $\angle ABP = 90^\circ$.
Berdasarkan Teorema Pythagoras pada $\triangle ABP$:
$$\begin{aligned} PB &= \sqrt{AP^2 - AB^2} \\ &= \sqrt{29^2 - 20^2} \\ &= \sqrt{841 - 400} \\ &= \sqrt{441} \\ &= 21\text{ cm} \end{aligned}$$

Jadi, panjang garis singgung $PB$ adalah $21\text{ cm}$.
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b02-b-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: sudut antara dua garis singgung*

Titik $D$ terletak di luar lingkaran yang berpusat di $A$. Ruas garis $BD$ dan $CD$ menyinggung lingkaran berturut-turut di titik $B$ dan $C$. Jika besar $\angle BAC = 128^\circ$, tentukan besar $\angle BDC$.

- A. $64^\circ$  
  <sub>Salah: Membagi dua besar sudut $\angle BAC$ alih-alih menghitung sudut pelurusnya terhadap $180^\circ$.</sub>
- **B. $52^\circ$** ✅  
  <sub>Benar: Pada segiempat garis singgung $ABDC$, $\angle ABD = \angle ACD = 90^\circ$. Karena jumlah sudut segiempat adalah $360^\circ$, maka $\angle BDC = 180^\circ - \angle BAC = 180^\circ - 128^\circ = 52^\circ$.</sub>
- C. $42^\circ$  
  <sub>Salah: Kesalahan pengurangan saat menghitung $180^\circ - 128^\circ$.</sub>
- D. $128^\circ$  
  <sub>Salah: Mengira sudut yang berhadapan sama besar seperti pada jajar genjang.</sub>

**Pembahasan:** Pada layang-layang garis singgung $ABDC$:
- $AB \perp BD \implies \angle ABD = 90^\circ$
- $AC \perp CD \implies \angle ACD = 90^\circ$

Jumlah sudut dalam segiempat adalah $360^\circ$:
$$\angle BAC + \angle ABD + \angle BDC + \angle ACD = 360^\circ$$
$$128^\circ + 90^\circ + \angle BDC + 90^\circ = 360^\circ$$
$$308^\circ + \angle BDC = 360^\circ$$
$$\angle BDC = 360^\circ - 308^\circ = 52^\circ$$

Secara singkat, dua sudut yang berhadapan saling berpelurus:
$$\angle BDC = 180^\circ - 128^\circ = 52^\circ$$
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b02-b-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: keliling segiempat tali busur dan garis singgung*

Sebuah segiempat garis singgung $ABCD$ melingkupi sebuah lingkaran sedemikian sehingga keempat sisinya menyinggung lingkaran tersebut. Jika panjang sisi $AB = 15\text{ cm}$ dan sisi yang saling berhadapan dengannya $CD = 17\text{ cm}$, keliling segiempat $ABCD$ adalah ....

- A. $47\text{ cm}$  
  <sub>Salah: Menjumlahkan $AB + CD$ ditambah salah satu sisi saja.</sub>
- **B. $64\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pitot, jumlah dua sisi berhadapan sama dengan jumlah dua sisi berhadapan lainnya ($AB + CD = BC + DA$). Keliling segiempat adalah $2 \times (AB + CD) = 2 \times (15 + 17) = 64\text{ cm}$.</sub>
- C. $128\text{ cm}$  
  <sub>Salah: Mengalikan hasil penjumlahan dengan 4 alih-alih 2.</sub>
- D. $32\text{ cm}$  
  <sub>Salah: Hanya menghitung jumlah satu pasang sisi yang berhadapan ($AB + CD$), lupa mengalikan dua.</sub>

**Pembahasan:** Berdasarkan Teorema Pitot, untuk sembarang segiempat garis singgung yang keempat sisinya menyinggung lingkaran berlaku:
$$AB + CD = BC + DA$$

Diketahui $AB = 15\text{ cm}$ dan $CD = 17\text{ cm}$, maka:
$$BC + DA = 15 + 17 = 32\text{ cm}$$

Keliling segiempat $ABCD$ adalah jumlah seluruh sisinya:
$$\begin{aligned} K &= AB + BC + CD + DA \\ &= (AB + CD) + (BC + DA) \\ &= 32 + 32 \\ &= 64\text{ cm} \end{aligned}$$

Jadi, keliling segiempat tersebut adalah $64\text{ cm}$.
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b02-b-medium-bt01-014
*orisinal | C3 | 2 langkah | jenis: jarak pusat dari garis singgung persekutuan luar*

Panjang garis singgung persekutuan luar dua buah lingkaran adalah $35\text{ cm}$. Jika jari-jari lingkaran yang lebih besar adalah $16\text{ cm}$ dan jari-jari lingkaran yang lebih kecil adalah $4\text{ cm}$, maka jarak antara kedua titik pusat lingkaran tersebut adalah ....

- A. $33\text{ cm}$  
  <sub>Salah: Keliru menggunakan operasi pengurangan pada akar kuadrat: $\sqrt{35^2 - 12^2}$.</sub>
- **B. $37\text{ cm}$** ✅  
  <sub>Benar: Jarak pusat $d = \sqrt{s^2 + (R - r)^2} = \sqrt{35^2 + (16 - 4)^2} = \sqrt{1.225 + 144} = \sqrt{1.369} = 37\text{ cm}$.</sub>
- C. $47\text{ cm}$  
  <sub>Salah: Menjumlahkan panjang garis singgung dengan selisih jari-jari secara langsung ($35 + 12$).</sub>
- D. $\sqrt{1.625}\text{ cm}$  
  <sub>Salah: Keliru menggunakan penjumlahan jari-jari $(R + r)$ seperti rumus persekutuan dalam.</sub>

**Pembahasan:** Diketahui:
- Panjang garis singgung persekutuan luar $s = 35\text{ cm}$
- Jari-jari lingkaran besar $R = 16\text{ cm}$
- Jari-jari lingkaran kecil $r = 4\text{ cm}$
- Selisih jari-jari $R - r = 16 - 4 = 12\text{ cm}$

Rumus garis singgung persekutuan luar adalah:
$$s = \sqrt{d^2 - (R - r)^2}$$

Untuk mencari jarak pusat $d$, kedua ruas dikuadratkan:
$$\begin{aligned} d^2 &= s^2 + (R - r)^2 \\ d &= \sqrt{35^2 + 12^2} \\ d &= \sqrt{1.225 + 144} \\ d &= \sqrt{1.369} \\ d &= 37\text{ cm} \end{aligned}$$

Jadi, jarak antara kedua pusat lingkaran tersebut adalah $37\text{ cm}$.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b02-b-medium-bt01-015
*variasi (angka) | C3 | 2 langkah | jenis: panjang garis singgung lingkaran*

Jika jari-jari lingkaran $A$ adalah $9\text{ cm}$ dan titik $P$ berjarak $41\text{ cm}$ dari titik $A$, berapakah panjang garis singgung $PB$ jika $B$ adalah titik singgung pada lingkaran?

- A. $50\text{ cm}$  
  <sub>Salah: Siswa langsung menjumlahkan kedua nilai panjang sisi yang diketahui ($41 + 9 = 50$).</sub>
- B. $42\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan kuadrat di dalam akar bukan mengurangkan, $\sqrt{41^2 + 9^2} \approx 41{,}97$ lalu dibulatkan ke $42$.</sub>
- C. $32\text{ cm}$  
  <sub>Salah: Siswa langsung mengurangkan jarak titik ke pusat dengan jari-jari lingkaran ($41 - 9 = 32$).</sub>
- **D. $40\text{ cm}$** ✅  
  <sub>Benar: Garis singgung $PB$ tegak lurus jari-jari $AB$, sehingga segitiga $ABP$ siku-siku di $B$. Dengan teorema Pythagoras, $PB = \sqrt{AP^2 - AB^2} = \sqrt{41^2 - 9^2} = \sqrt{1681 - 81} = \sqrt{1600} = 40\text{ cm}$.</sub>

**Pembahasan:** Garis singgung lingkaran selalu tegak lurus terhadap jari-jari yang melalui titik singgung, sehingga $\angle ABP = 90^\circ$.
Pada segitiga siku-siku $ABP$, berlaku:
$$PB = \sqrt{AP^2 - AB^2}$$
$$PB = \sqrt{41^2 - 9^2}$$
$$PB = \sqrt{1.681 - 81} = \sqrt{1.600} = 40\text{ cm}$$
Jadi, panjang garis singgung $PB$ adalah $40\text{ cm}$.
**Acuan:** pretest — kelas11-b02-p0081-latihan-22-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b02-b-medium-bt01-016
*variasi (konteks) | C4 | 3 langkah | jenis: jarak pandang cakrawala*

Seorang petugas mercusuar mengamati lautan dari balkon pengamatan yang berada pada ketinggian $80\text{ m}$ dari permukaan laut. Jika jari-jari bumi adalah $6.400\text{ km}$, jarak pandang terjauh menuju cakrawala yang dapat dilihat oleh petugas tersebut adalah sekitar ....

- **A. $32\text{ km}$** ✅  
  <sub>Benar: Garis pandang ke cakrawala merupakan garis singgung bumi. Ketinggian $h = 80\text{ m} = 0{,}08\text{ km}$. Jarak cakrawala $d = \sqrt{(R + h)^2 - R^2} = \sqrt{2Rh + h^2} \approx \sqrt{2 \times 6.400 \times 0{,}08} = \sqrt{1.024} = 32\text{ km}$.</sub>
- B. $64\text{ km}$  
  <sub>Salah: Siswa mengalikan dua hasil akhir jarak cakrawala ($32 \times 2 = 64$).</sub>
- C. $71{,}5\text{ km}$  
  <sub>Salah: Siswa tidak mengonversi satuan ketinggian $80\text{ m}$ ke kilometer sehingga salah mengalikan nilai akar.</sub>
- D. $16\text{ km}$  
  <sub>Salah: Siswa lupa mengalikan dengan $2$ di bawah tanda akar sehingga menghitung $\sqrt{Rh} = \sqrt{512} \approx 22{,}6$ atau salah membagi dua hasilnya.</sub>

**Pembahasan:** Garis pandang ke cakrawala membentuk garis singgung lingkaran bumi yang tegak lurus jari-jari di titik singgung cakrawala.
Diketahui:
- Jari-jari bumi ($R$) = $6.400\text{ km}$
- Ketinggian pengamat ($h$) = $80\text{ m} = 0{,}08\text{ km}$

Jarak titik pengamat ke pusat bumi adalah $R + h$.
Dengan teorema Pythagoras, jarak cakrawala ($d$) adalah:
$$d = \sqrt{(R + h)^2 - R^2}$$
$$d = \sqrt{2Rh + h^2}$$
Karena $h^2 = (0{,}08)^2 = 0{,}0064$ sangat kecil, nilai tersebut dapat diabaikan atau dimasukkan:
$$d = \sqrt{2 \times 6.400 \times 0{,}08 + 0{,}0064} = \sqrt{1.024{,}0064} \approx 32\text{ km}$$
Jadi, jarak pandang terjauh menuju cakrawala adalah sekitar $32\text{ km}$.
**Acuan:** siswa — siswa hal.81 Ayo Berpikir Kreatif

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b02-b-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: jarak titik ke pusat lingkaran*

Dari titik $K$ yang berada di luar lingkaran berpusat $O$, ditarik garis singgung yang menyentuh lingkaran di titik $L$. Jika panjang jari-jari lingkaran adalah $10\text{ cm}$ dan panjang ruas garis singgung $KL$ adalah $24\text{ cm}$, maka jarak titik $K$ ke pusat lingkaran $O$ adalah ....

- **A. $26\text{ cm}$** ✅  
  <sub>Benar: Garis singgung $KL$ tegak lurus jari-jari $OL$ di titik singgung $L$. Maka $\triangle OLK$ siku-siku di $L$ dengan hipotenusa $OK$. $OK = \sqrt{OL^2 + KL^2} = \sqrt{10^2 + 24^2} = \sqrt{100 + 576} = \sqrt{676} = 26\text{ cm}$.</sub>
- B. $21{,}8\text{ cm}$  
  <sub>Salah: Siswa keliru mengurangkan kuadrat sisi bukan menjumlahkannya, $\sqrt{24^2 - 10^2} = \sqrt{476} \approx 21{,}8\text{ cm}$.</sub>
- C. $34\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan langsung panjang jari-jari dan garis singgung ($10 + 24 = 34$).</sub>
- D. $28\text{ cm}$  
  <sub>Salah: Siswa salah dalam perhitungan kuadrat dan akar hipotenusa.</sub>

**Pembahasan:** Garis singgung $KL$ dan jari-jari $OL$ berpotongan tegak lurus di titik $L$ sehingga membentuk segitiga siku-siku $OLK$ dengan sudut siku-siku di $L$.
Jarak titik $K$ ke titik pusat $O$ merupakan sisi miring (hipotenusa) segitiga $OLK$:
$$OK = \sqrt{OL^2 + KL^2}$$
$$OK = \sqrt{10^2 + 24^2}$$
$$OK = \sqrt{100 + 576} = \sqrt{676} = 26\text{ cm}$$
Jadi, jarak titik $K$ ke pusat lingkaran adalah $26\text{ cm}$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b02-b-medium-bt01-018
*orisinal | C3 | 2 langkah | jenis: jarak pusat dari garis singgung persekutuan dalam*

Dua buah lingkaran memiliki panjang jari-jari masing-masing $7\text{ cm}$ dan $8\text{ cm}$. Jika panjang garis singgung persekutuan dalam kedua lingkaran tersebut adalah $20\text{ cm}$, maka jarak antara kedua pusat lingkaran tersebut adalah ....

- A. $20{,}6\text{ cm}$  
  <sub>Salah: Siswa keliru menggunakan rumus garis singgung persekutuan luar yaitu selisih jari-jari $(8 - 7 = 1)$ sehingga menghitung $\sqrt{20^2 + 1^2} = \sqrt{401} \approx 20{,}6\text{ cm}$.</sub>
- B. $35\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan langsung panjang garis singgung persekutuan dalam dengan kedua jari-jari ($20 + 8 + 7 = 35$).</sub>
- **C. $25\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung persekutuan dalam memenuhi $g = \sqrt{d^2 - (R + r)^2}$. Jarak antarpusat $d = \sqrt{g^2 + (R + r)^2} = \sqrt{20^2 + (8 + 7)^2} = \sqrt{400 + 225} = \sqrt{625} = 25\text{ cm}$.</sub>
- D. $13{,}2\text{ cm}$  
  <sub>Salah: Siswa salah operasi mengurangkan kuadrat garis singgung dengan kuadrat jumlah jari-jari, $\sqrt{20^2 - 15^2} = \sqrt{175} \approx 13{,}2\text{ cm}$.</sub>

**Pembahasan:** Rumus panjang garis singgung persekutuan dalam ($g$) adalah:
$$g^2 = d^2 - (R + r)^2$$
Maka jarak antara kedua pusat lingkaran ($d$) dapat dihitung dengan:
$$d = \sqrt{g^2 + (R + r)^2}$$
Diketahui $g = 20\text{ cm}$, $R = 8\text{ cm}$, dan $r = 7\text{ cm}$:
$$R + r = 8 + 7 = 15\text{ cm}$$
$$d = \sqrt{20^2 + 15^2}$$
$$d = \sqrt{400 + 225} = \sqrt{625} = 25\text{ cm}$$
Jadi, jarak antara kedua pusat lingkaran tersebut adalah $25\text{ cm}$.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b02-b-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: jari-jari dari garis singgung persekutuan luar*

Panjang garis singgung persekutuan luar dua lingkaran adalah $24\text{ cm}$, sedangkan jarak antara kedua titik pusatnya adalah $26\text{ cm}$. Jika jari-jari lingkaran yang lebih besar adalah $15\text{ cm}$, maka panjang jari-jari lingkaran yang lebih kecil adalah ....

- A. $25\text{ cm}$  
  <sub>Salah: Siswa menjumlahkan $R$ dengan selisih jari-jari ($15 + 10 = 25$) alih-alih mengurangkannya.</sub>
- B. $3\text{ cm}$  
  <sub>Salah: Siswa keliru menggunakan rumus garis singgung persekutuan dalam sehingga salah menghitung nilai jari-jari.</sub>
- C. $10\text{ cm}$  
  <sub>Salah: Siswa hanya menyelesaikan langkah sampai nilai selisih jari-jari ($R - r = 10$) dan lupa mengurangkannya dari $R$.</sub>
- **D. $5\text{ cm}$** ✅  
  <sub>Benar: Selisih jari-jari $R - r = \sqrt{d^2 - s^2} = \sqrt{26^2 - 24^2} = \sqrt{676 - 576} = \sqrt{100} = 10\text{ cm}$. Karena $R = 15\text{ cm}$, maka $r = 15 - 10 = 5\text{ cm}$.</sub>

**Pembahasan:** Panjang garis singgung persekutuan luar ($s$) dirumuskan sebagai:
$$s = \sqrt{d^2 - (R - r)^2}$$
Substitusikan nilai yang diketahui:
$$24 = \sqrt{26^2 - (15 - r)^2}$$
$$24^2 = 26^2 - (15 - r)^2$$
$$576 = 676 - (15 - r)^2$$
$$(15 - r)^2 = 676 - 576 = 100$$
$$15 - r = \sqrt{100} = 10$$
$$r = 15 - 10 = 5\text{ cm}$$
Jadi, panjang jari-jari lingkaran yang lebih kecil adalah $5\text{ cm}$.
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b02-b-medium-bt01-020
*variasi (konteks) | C3 | 3 langkah | jenis: jarak pandang cakrawala*

Seorang pengamat berdiri di puncak menara pandang dengan ketinggian $45\text{ m}$ dari permukaan laut. Jika jari-jari bumi dimodelkan sebesar $6.400\text{ km}$, berapakah jarak cakrawala terjauh yang dapat dilihat oleh pengamat tersebut?

- A. $12\text{ km}$  
  <sub>Salah: Siswa lupa mengalikan faktor 2 pada rumus hampiran $d \approx \sqrt{Rh}$, menghasilkan $\sqrt{6.400 \times 0{,}045} = \sqrt{288} \approx 17$ atau membagi dua hasil akhir ($24 / 2$).</sub>
- B. $17\text{ km}$  
  <sub>Salah: Siswa menggunakan $\sqrt{Rh}$ tanpa faktor 2, yaitu $\sqrt{288} \approx 17\text{ km}$.</sub>
- **C. $24\text{ km}$** ✅  
  <sub>Benar: Garis pandang ke cakrawala membentuk garis singgung lingkaran bumi yang tegak lurus terhadap jari-jari di titik singgung. Ketinggian pengamat $h = 45\text{ m} = 0{,}045\text{ km}$. Jarak cakrawala $d = \sqrt{(R + h)^2 - R^2} = \sqrt{2Rh + h^2} \approx \sqrt{2Rh} = \sqrt{2 \times 6.400 \times 0{,}045} = \sqrt{576} = 24\text{ km}$.</sub>
- D. $48\text{ km}$  
  <sub>Salah: Siswa salah memasukkan rumus dengan mengalikan dua hasil akhir panjang garis singgung.</sub>

**Pembahasan:** Pandangan ke cakrawala merupakan garis singgung pada permukaan bumi yang berpusat di pusat bumi.

1. Konversikan satuan ketinggian ke kilometer:
$$h = 45\text{ m} = 0{,}045\text{ km}$$

2. Gunakan Teorema Pythagoras pada segitiga siku-siku yang dibentuk oleh pusat bumi, posisi pengamat, dan titik singgung cakrawala:
$$d = \sqrt{(R + h)^2 - R^2}$$
$$d = \sqrt{2Rh + h^2}$$

Karena nilai $h^2 = (0{,}045)^2 = 0{,}002025$ sangat kecil dibandingkan $2Rh$, maka dapat dihampiri dengan:
$$d \approx \sqrt{2Rh}$$

3. Substitusikan nilai $R = 6.400\text{ km}$ dan $h = 0{,}045\text{ km}$:
$$d = \sqrt{2 \times 6.400 \times 0{,}045} = \sqrt{576} = 24\text{ km}$$

Jadi, jarak cakrawala yang dapat dilihat adalah $24\text{ km}$.
**Acuan:** siswa — siswa hal.81 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b02-b-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: analisis perubahan geometri*

Dua roda dihubungkan oleh sabuk lurus sebagai garis singgung persekutuan luar dengan panjang $48\text{ cm}$. Mula-mula, jari-jari roda besar $18\text{ cm}$ dan roda kecil $4\text{ cm}$. Jika jari-jari roda besar diganti menjadi $24\text{ cm}$ tanpa mengubah jari-jari roda kecil dan panjang garis singgung persekutuan luarnya tetap $48\text{ cm}$, berapakah pertambahan jarak antara kedua pusat roda tersebut?

- A. $52\text{ cm}$  
  <sub>Salah: Siswa menjawab jarak akhir $d_2$, bukan nilai pertambahan jaraknya.</sub>
- **B. $2\text{ cm}$** ✅  
  <sub>Benar: Jarak awal $d_1 = \sqrt{48^2 + (18 - 4)^2} = \sqrt{2304 + 196} = \sqrt{2500} = 50\text{ cm}$. Jarak baru $d_2 = \sqrt{48^2 + (24 - 4)^2} = \sqrt{2304 + 400} = \sqrt{2704} = 52\text{ cm}$. Selisih jarak $= 52 - 50 = 2\text{ cm}$.</sub>
- C. $4\text{ cm}$  
  <sub>Salah: Siswa salah menghitung selisih jari-jari baru atau salah menarik akar dari kuadrat hipotenusa.</sub>
- D. $6\text{ cm}$  
  <sub>Salah: Siswa langsung mengurangkan selisih perubahan jari-jari roda besar ($24 - 18 = 6\text{ cm}$) sebagai pertambahan jarak pusat.</sub>

**Pembahasan:** Gunakan rumus garis singgung persekutuan luar: $s^2 = d^2 - (R - r)^2 \iff d = \sqrt{s^2 + (R - r)^2}$.

1. Kondisi awal:
$d_1 = \sqrt{48^2 + (18 - 4)^2} = \sqrt{2.304 + 14^2} = \sqrt{2.304 + 196} = \sqrt{2.500} = 50\text{ cm}$.

2. Kondisi setelah diganti ($R' = 24\text{ cm}$, $r = 4\text{ cm}$, $s = 48\text{ cm}$):
$d_2 = \sqrt{48^2 + (24 - 4)^2} = \sqrt{2.304 + 20^2} = \sqrt{2.304 + 400} = \sqrt{2.704} = 52\text{ cm}$.

3. Pertambahan jarak pusat:
$\Delta d = d_2 - d_1 = 52 - 50 = 2\text{ cm}$.
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b02-b-hard-bt01-002
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi teorema segiempat garis singgung*

Sebuah lahan berbentuk trapesium sama kaki $PQRS$ dengan $PQ \parallel SR$ dirancang sebagai segiempat garis singgung (semua sisinya menyinggung lingkaran di dalamnya). Jika panjang sisi sejajar berturut-turut adalah $PQ = 32\text{ m}$ dan $SR = 18\text{ m}$, serta tinggi trapesium tersebut sama dengan diameter lingkaran di dalamnya, berapakah panjang jari-jari lingkaran tersebut?

- A. $25\text{ m}$  
  <sub>Salah: Siswa menganggap panjang sisi miring sama dengan nilai jari-jari lingkaran.</sub>
- B. $24\text{ m}$  
  <sub>Salah: Siswa menjawab diameter trapesium/lingkaran tanpa membaginya dengan 2 untuk memperoleh jari-jari.</sub>
- **C. $12\text{ m}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pitot pada trapesium sama kaki, $PQ + SR = PS + QR \implies 32 + 18 = 2 \cdot PS \implies PS = 25\text{ m}$. Proyeksi alas pada segitiga siku-siku tinggi trapesium adalah $\frac{32 - 18}{2} = 7\text{ m}$. Tinggi trapesium $t = \sqrt{25^2 - 7^2} = 24\text{ m}$. Karena tinggi sama dengan diameter lingkaran, maka jari-jari $r = \frac{24}{2} = 12\text{ m}$.</sub>
- D. $14\text{ m}$  
  <sub>Salah: Siswa salah menghitung panjang sisi miring atau salah menerapkan pengurangan proyeksi alas.</sub>

**Pembahasan:** Berdasarkan Teorema Pitot, pada segiempat garis singgung berlaku jumlah sisi yang berhadapan adalah sama:
$PQ + SR = PS + QR$

Karena trapesium sama kaki, $PS = QR$, sehingga:
$32 + 18 = 2 \cdot PS \iff 50 = 2 \cdot PS \iff PS = 25\text{ m}$.

Tarik garis tinggi dari titik $S$ dan $R$ tegak lurus ke $PQ$. Panjang alas segitiga siku-siku di tepi trapesium adalah:
$x = \frac{PQ - SR}{2} = \frac{32 - 18}{2} = 7\text{ m}$.

Dengan Teorema Pythagoras, tinggi trapesium ($t$):
$t = \sqrt{PS^2 - x^2} = \sqrt{25^2 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ m}$.

Karena lingkaran bersinggungan dengan kedua sisi sejajar, tinggi trapesium sama dengan diameter lingkaran ($2r = t$):
$r = \frac{24}{2} = 12\text{ m}$.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b02-b-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: perhitungan luas layang-layang garis singgung*

Dari titik $P$ di luar lingkaran berpusat di $O$, dibuat dua garis singgung $PA$ dan $PB$ yang menyentuh lingkaran di titik $A$ dan $B$. Jika panjang ruas garis penghubung titik singgung $AB = 9{,}6\text{ cm}$ dan panjang $OP = 10\text{ cm}$, berapakah luas layang-layang garis singgung $OAPB$?

- A. $24\text{ cm}^2$  
  <sub>Salah: Siswa hanya menghitung luas satu segitiga siku-siku $OAP$, lupa mengalikan dua untuk seluruh layang-layang.</sub>
- B. $60\text{ cm}^2$  
  <sub>Salah: Siswa keliru mengasumsikan jari-jari lingkaran bernilai $6\text{ cm}$ dan mengalikan $\frac{1}{2} \times 10 \times 12$.</sub>
- C. $96\text{ cm}^2$  
  <sub>Salah: Siswa langsung mengalikan $OP \times AB$ tanpa membaginya dengan dua pada rumus luas layang-layang.</sub>
- **D. $48\text{ cm}^2$** ✅  
  <sub>Benar: Ruas garis $OP$ membagi tali busur $AB$ menjadi dua sama panjang dan tegak lurus di titik $M$, sehingga $AM = 4{,}8\text{ cm}$. Pada segitiga siku-siku $OAP$, $AM$ merupakan garis tinggi ke hipotenusa $OP$. Maka luas $\triangle OAP = \frac{1}{2} \cdot OP \cdot AM = \frac{1}{2} \cdot 10 \cdot 4{,}8 = 24\text{ cm}^2$. Luas layang-layang $OAPB = 2 \cdot \text{Luas } \triangle OAP = 2 \cdot 24 = 48\text{ cm}^2$.</sub>

**Pembahasan:** Pada layang-layang garis singgung $OAPB$, kedua diagonalnya adalah $OP$ dan $AB$ yang saling berpotongan tegak lurus.

Panjang diagonal pertama: $d_1 = OP = 10\text{ cm}$.
Panjang diagonal kedua: $d_2 = AB = 9{,}6\text{ cm}$.

Luas layang-layang yang kedua diagonalnya saling tegak lurus diberikan oleh:
$\text{Luas} = \frac{1}{2} \times d_1 \times d_2 = \frac{1}{2} \times 10 \times 9{,}6 = 48\text{ cm}^2$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b02-b-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: kondisi singgung lingkaran luar*

Dua buah lingkaran berbeda ukuran saling bersinggungan di luar satu sama lain. Sebuah garis lurus merupakan garis singgung persekutuan luar bagi kedua lingkaran tersebut dengan titik singgung $P$ dan $Q$. Jika jari-jari kedua lingkaran tersebut berturut-turut adalah $16\text{ cm}$ dan $9\text{ cm}$, berapakah panjang ruas garis singgung $PQ$?

- A. $25\text{ cm}$  
  <sub>Salah: Siswa mengira panjang garis singgung persekutuan luar sama dengan jarak antarpusat kedua lingkaran.</sub>
- **B. $24\text{ cm}$** ✅  
  <sub>Benar: Karena kedua lingkaran saling bersinggungan di luar, jarak antara kedua titik pusat lingkaran adalah $d = R + r = 16 + 9 = 25\text{ cm}$. Panjang garis singgung persekutuan luar adalah $PQ = \sqrt{d^2 - (R - r)^2} = \sqrt{25^2 - (16 - 9)^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$ (atau melalui formula $PQ = 2\sqrt{R r} = 2\sqrt{16 \cdot 9} = 2 \cdot 12 = 24\text{ cm}$).</sub>
- C. $12\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung $\sqrt{R \cdot r}$ tanpa mengalikan dengan faktor 2.</sub>
- D. $20\text{ cm}$  
  <sub>Salah: Siswa salah mengurangkan kuadrat pada Teorema Pythagoras atau mengira selisih kuadrat menghasilkan 400.</sub>

**Pembahasan:** Untuk dua lingkaran dengan jari-jari $R$ dan $r$ yang saling bersinggungan di luar:
1. Jarak antarpusat kedua lingkaran adalah:
   $d = R + r = 16 + 9 = 25\text{ cm}$.

2. Panjang garis singgung persekutuan luar $PQ$ dihitung dengan:
   $PQ = \sqrt{d^2 - (R - r)^2}$
   $PQ = \sqrt{25^2 - (16 - 9)^2} = \sqrt{625 - 7^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$.

(Catatan: Untuk dua lingkaran yang saling bersinggungan luar, berlaku pula sifat khusus $PQ = 2\sqrt{R \cdot r} = 2\sqrt{16 \times 9} = 2 \times 12 = 24\text{ cm}$).
**Acuan:** siswa — siswa hal.82

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b02-b-hard-bt01-005
*variasi (angka) | C5 | 3 langkah | jenis: komparasi selisih garis singgung persekutuan*

Dua buah lingkaran saling lepas memiliki jarak antarpusat sebesar $25\text{ cm}$. Jika jari-jari kedua lingkaran berturut-turut adalah $11\text{ cm}$ dan $4\text{ cm}$, berapakah selisih panjang garis singgung persekutuan luar dan garis singgung persekutuan dalam kedua lingkaran tersebut?

- A. $7\text{ cm}$  
  <sub>Salah: Siswa menghitung selisih jari-jari kedua lingkaran ($11 - 4$), bukan selisih kedua garis singgung.</sub>
- B. $2\text{ cm}$  
  <sub>Salah: Siswa salah mengurangkan panjang garis singgung persekutuan luar dengan jarak antarpusat.</sub>
- C. $5\text{ cm}$  
  <sub>Salah: Siswa salah menghitung panjang garis singgung persekutuan dalam menjadi $\sqrt{25^2 - 15^2 - 4^2} \approx 19\text{ cm}$ sehingga selisihnya keliru.</sub>
- **D. $4\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung persekutuan luar adalah $s = \sqrt{25^2 - (11 - 4)^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$. Panjang garis singgung persekutuan dalam adalah $g = \sqrt{25^2 - (11 + 4)^2} = \sqrt{625 - 225} = \sqrt{400} = 20\text{ cm}$. Selisih keduanya adalah $24\text{ cm} - 20\text{ cm} = 4\text{ cm}$.</sub>

**Pembahasan:** Diketahui $d = 25\text{ cm}$, $R = 11\text{ cm}$, dan $r = 4\text{ cm}$.

1. Panjang garis singgung persekutuan luar ($s$):
$$s = \sqrt{d^2 - (R - r)^2} = \sqrt{25^2 - (11 - 4)^2} = \sqrt{625 - 49} = \sqrt{576} = 24\text{ cm}$$

2. Panjang garis singgung persekutuan dalam ($g$):
$$g = \sqrt{d^2 - (R + r)^2} = \sqrt{25^2 - (11 + 4)^2} = \sqrt{625 - 225} = \sqrt{400} = 20\text{ cm}$$

3. Selisih panjang kedua garis singgung:
$$\Delta = s - g = 24\text{ cm} - 20\text{ cm} = 4\text{ cm}$$
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b02-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: perhitungan tali busur singgung*

Dari titik $P$ di luar lingkaran yang berpusat di $O$, ditarik dua garis singgung yang menyentuh lingkaran di titik $A$ dan $B$. Jari-jari lingkaran tersebut adalah $15\text{ cm}$ dan jarak titik $P$ ke pusat lingkaran $O$ adalah $25\text{ cm}$. Panjang tali busur $AB$ yang menghubungkan kedua titik singgung tersebut adalah ....

- A. $18\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan perbandingan trigonometri atau keliru mengalikan perbandingan sisi.</sub>
- B. $20\text{ cm}$  
  <sub>Salah: Siswa mengira panjang tali busur $AB$ sama dengan panjang garis singgung $PA$.</sub>
- C. $12\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung setengah dari panjang tali busur $AB$ (jarak dari titik singgung ke ruas garis $OP$).</sub>
- **D. $24\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung $PA = \sqrt{25^2 - 15^2} = 20\text{ cm}$. Luas layang-layang $OAPB = 2 \times \left(\frac{1}{2} \times 15 \times 20\right) = 300\text{ cm}^2$. Karena luas layang-layang juga sama dengan $\frac{1}{2} \times OP \times AB$, diperoleh $\frac{1}{2} \times 25 \times AB = 300 \implies AB = \frac{600}{25} = 24\text{ cm}$.</sub>

**Pembahasan:** 1. Pada segitiga siku-siku $OAP$ (siku-siku di $A$ karena garis singgung tegak lurus jari-jari):
$$PA = \sqrt{OP^2 - OA^2} = \sqrt{25^2 - 15^2} = \sqrt{625 - 225} = \sqrt{400} = 20\text{ cm}$$

2. Hitung luas layang-layang garis singgung $OAPB$:
$$L = 2 \times L_{\triangle OAP} = 2 \times \left(\frac{1}{2} \times OA \times PA\right) = 15 \times 20 = 300\text{ cm}^2$$

3. Tali busur $AB$ dan garis sentral $OP$ saling tegak lurus dan merupakan diagonal layang-layang $OAPB$:
$$L = \frac{1}{2} \times OP \times AB$$
$$300 = \frac{1}{2} \times 25 \times AB$$
$$AB = \frac{600}{25} = 24\text{ cm}$$
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b02-b-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: analisis pergeseran jarak pusat*

Dua buah lingkaran masing-masing memiliki jari-jari $14\text{ cm}$ dan $6\text{ cm}$. Pada mulanya, jarak kedua titik pusat lingkaran adalah $17\text{ cm}$. Jika kedua lingkaran digeser saling menjauh sedemikian sehingga panjang garis singgung persekutuan dalamnya yang baru menjadi sama dengan panjang garis singgung persekutuan luar mula-mula, berapakah pertambahan jarak kedua pusat lingkaran tersebut?

- A. $6\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan jari-jari pada rumus garis singgung persekutuan dalam atau keliru menghitung tripel Pythagoras.</sub>
- B. $10\text{ cm}$  
  <sub>Salah: Siswa menghitung selisih antara jarak pusat baru $25\text{ cm}$ dengan garis singgung mula-mula $15\text{ cm}$.</sub>
- **C. $8\text{ cm}$** ✅  
  <sub>Benar: Garis singgung persekutuan luar mula-mula adalah $s = \sqrt{17^2 - (14 - 6)^2} = \sqrt{289 - 64} = 15\text{ cm}$. Agar panjang garis singgung persekutuan dalam baru bernilai $15\text{ cm}$, jarak pusat baru harus memenuhi $d_{\text{baru}} = \sqrt{15^2 + (14 + 6)^2} = \sqrt{225 + 400} = \sqrt{625} = 25\text{ cm}$. Pertambahan jarak pusat adalah $25\text{ cm} - 17\text{ cm} = 8\text{ cm}$.</sub>
- D. $25\text{ cm}$  
  <sub>Salah: Siswa menjawab jarak pusat baru, bukan pertambahan jaraknya.</sub>

**Pembahasan:** 1. Hitung panjang garis singgung persekutuan luar ($s$) pada kondisi mula-mula:
$$s = \sqrt{d_1^2 - (R - r)^2} = \sqrt{17^2 - (14 - 6)^2} = \sqrt{289 - 64} = \sqrt{225} = 15\text{ cm}$$

2. Pada kondisi baru, panjang garis singgung persekutuan dalam $g_2 = s = 15\text{ cm}$.

3. Hitung jarak kedua pusat yang baru ($d_2$):
$$d_2 = \sqrt{g_2^2 + (R + r)^2} = \sqrt{15^2 + (14 + 6)^2} = \sqrt{225 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25\text{ cm}$$

4. Hitung pertambahan jarak pusat:
$$\Delta d = d_2 - d_1 = 25\text{ cm} - 17\text{ cm} = 8\text{ cm}$$
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b02-b-hard-bt01-008
*orisinal | C6 | 4 langkah | jenis: perancangan trapesium garis singgung*

Sebuah trapesium siku-siku $ABCD$ dengan sudut siku-siku di $A$ dan $D$ memuat lingkaran dalam sedemikian sehingga keempat sisinya menyinggung lingkaran tersebut. Jika panjang sisi sejajar $AB = 12\text{ cm}$ dan $CD = 6\text{ cm}$, maka panjang jari-jari lingkaran dalam trapesium tersebut adalah ....

- A. $3\text{ cm}$  
  <sub>Salah: Siswa mengira jari-jari sama dengan setengah dari sisi atas $CD$.</sub>
- **B. $4\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pitot, $AB + CD = AD + BC \implies 12 + 6 = AD + BC \implies BC = 18 - AD$. Sisi $AD$ tegak lurus sisi sejajar sehingga $AD$ sama dengan diameter lingkaran ($2r$). Dengan menarik garis tinggi dari $C$ ke $AB$, terbentuk segitiga siku-siku dengan sisi alas $(12 - 6) = 6\text{ cm}$ dan tinggi $AD$, sehingga $BC^2 = AD^2 + 6^2$. Substitusi $BC$: $(18 - AD)^2 = AD^2 + 36 \implies 324 - 36 AD + AD^2 = AD^2 + 36 \implies 36 AD = 288 \implies AD = 8\text{ cm}$. Maka jari-jari $r = \frac{AD}{2} = 4\text{ cm}$.</sub>
- C. $8\text{ cm}$  
  <sub>Salah: Siswa menjawab diameter lingkaran ($AD$), bukan jari-jari lingkaran.</sub>
- D. $5\text{ cm}$  
  <sub>Salah: Siswa salah menghitung hasil penyelesaian persamaan kuadrat linier.</sub>

**Pembahasan:** 1. Pada trapesium siku-siku garis singgung $ABCD$ dengan $\angle A = \angle D = 90^\circ$:
Sisi $AD$ tegak lurus dengan $AB$ dan $CD$, sehingga panjang $AD$ sama dengan diameter lingkaran: $AD = 2r$.

2. Gunakan Teorema Pitot untuk segiempat garis singgung:
$$AB + CD = AD + BC$$
$$12 + 6 = AD + BC \implies BC = 18 - AD$$

3. Proyeksikan titik $C$ tegak lurus ke sisi $AB$ pada titik $E$:
$AE = CD = 6\text{ cm}$, sehingga $EB = AB - AE = 12 - 6 = 6\text{ cm}$.
Pada $\triangle CEB$ siku-siku di $E$:
$$BC^2 = CE^2 + EB^2 = AD^2 + 6^2 = AD^2 + 36$$

4. Substitusikan $BC = 18 - AD$:
$$(18 - AD)^2 = AD^2 + 36$$
$$324 - 36AD + AD^2 = AD^2 + 36$$
$$36AD = 288 \implies AD = 8\text{ cm}$$

5. Jari-jari lingkaran dalam:
$$r = \frac{AD}{2} = \frac{8}{2} = 4\text{ cm}$$
**Acuan:** siswa — siswa hal.84

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b02-b-hard-bt01-009
*orisinal | C5 | 3 langkah | jenis: pemodelan jarak jangkauan satelit*

Sebuah satelit pengamat mengorbit bumi pada ketinggian $1.600\text{ km}$ di atas permukaan bumi. Bumi dimodelkan sebagai bola dengan penampang lintang lingkaran berjari-jari $6.400\text{ km}$. Jangkauan terjauh sinyal langsung dari satelit ke permukaan bumi dibatasi oleh garis singgung yang ditarik dari satelit ke permukaan bumi. Jarak jangkauan terjauh tersebut (panjang garis singgung dari satelit ke titik singgung di permukaan bumi) adalah ....

- **A. $4.800\text{ km}$** ✅  
  <sub>Benar: Jarak titik satelit ke pusat bumi adalah $d = 6.400\text{ km} + 1.600\text{ km} = 8.000\text{ km}$. Garis singgung tegak lurus jari-jari bumi di titik singgung. Panjang garis singgung adalah $s = \sqrt{d^2 - R^2} = \sqrt{8.000^2 - 6.400^2} = \sqrt{64.000.000 - 40.960.000} = \sqrt{23.040.000} = 4.800\text{ km}$.</sub>
- B. $3.200\text{ km}$  
  <sub>Salah: Siswa salah menggunakan rumus dengan mengurangkan jari-jari langsung dari hipotenusa tanpa kuadrat.</sub>
- C. $8.000\text{ km}$  
  <sub>Salah: Siswa menjawab jarak total satelit ke pusat bumi, bukan panjang garis singgungnya.</sub>
- D. $6.000\text{ km}$  
  <sub>Salah: Siswa salah menghitung pengurangan kuadrat di dalam akar.</sub>

**Pembahasan:** 1. Tentukan jarak satelit ($P$) ke titik pusat bumi ($O$):
$$d = OP = R + h = 6.400\text{ km} + 1.600\text{ km} = 8.000\text{ km}$$

2. Garis singgung dari $P$ menyentuh permukaan bumi di titik $T$. Karena garis singgung tegak lurus dengan jari-jari $OT$ di titik singgung, segitiga $OTP$ merupakan segitiga siku-siku di $T$.

3. Hitung panjang garis singgung $PT$ menggunakan Teorema Pythagoras:
$$PT = \sqrt{OP^2 - OT^2} = \sqrt{8.000^2 - 6.400^2}$$
$$PT = \sqrt{64.000.000 - 40.960.000} = \sqrt{23.040.000} = 4.800\text{ km}$$
**Acuan:** siswa — siswa hal.81

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b02-b-hard-bt01-010
*variasi (angka) | C5 | 4 langkah | jenis: analisis selisih garis singgung gir*

Sebuah rantai menghubungkan gir depan dan gir belakang sepeda yang membentuk garis singgung persekutuan luar. Jari-jari gir besar adalah $33\text{ cm}$, jari-jari gir kecil mula-mula adalah $8\text{ cm}$, dan jarak antarpusat kedua gir selalu tetap yaitu $65\text{ cm}$. Jika gir kecil diganti dengan gir modifikasi yang berjari-jari $17\text{ cm}$, berapakah pertambahan panjang bentangan bebas rantai (garis singgung persekutuan luar) tersebut?

- A. $5\text{ cm}$  
  <sub>Salah: Siswa salah menggunakan rumus garis singgung persekutuan dalam pada salah satu perhitungan sehingga memperoleh selisih yang keliru.</sub>
- **B. $3\text{ cm}$** ✅  
  <sub>Benar: Panjang garis singgung mula-mula adalah $s_1 = \sqrt{65^2 - (33 - 8)^2} = \sqrt{4.225 - 625} = 60\text{ cm}$. Setelah gir diganti, panjangnya menjadi $s_2 = \sqrt{65^2 - (33 - 17)^2} = \sqrt{4.225 - 256} = 63\text{ cm}$. Pertambahan panjangnya adalah $63 - 60 = 3\text{ cm}$.</sub>
- C. $7\text{ cm}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan saat mengurangkan kuadrat di dalam akar pada kondisi kedua.</sub>
- D. $9\text{ cm}$  
  <sub>Salah: Siswa langsung menghitung selisih jari-jari gir kecil pengganti dan lama ($17 - 8 = 9\text{ cm}$) alih-alih menghitung selisih panjang garis singgungnya.</sub>

**Pembahasan:** Kondisi awal:
$s_1 = \sqrt{d^2 - (R - r_1)^2} = \sqrt{65^2 - (33 - 8)^2} = \sqrt{4.225 - 625} = \sqrt{3.600} = 60\text{ cm}$.

Kondisi setelah penggantian:
$s_2 = \sqrt{d^2 - (R - r_2)^2} = \sqrt{65^2 - (33 - 17)^2} = \sqrt{4.225 - 256} = \sqrt{3.969} = 63\text{ cm}$.

Pertambahan panjang bentangan rantai:
$\Delta s = s_2 - s_1 = 63 - 60 = 3\text{ cm}$.
**Acuan:** siswa — siswa hal.83 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b02-b-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: rekonstruksi jari-jari segitiga singgung*

Dari sebuah titik $P$ di luar lingkaran yang berpusat di $O$, dibuat dua garis singgung $PA$ dan $PB$ yang menyentuh lingkaran masing-masing di titik $A$ dan $B$. Sebuah garis singgung ketiga ditarik menyinggung lingkaran di titik $T$ (terletak di antara busur minor $AB$) serta memotong ruas garis $PA$ di titik $K$ dan $PB$ di titik $L$. Jika keliling segitiga $PKL$ adalah $48\text{ cm}$ dan jarak titik pusat $O$ ke titik $P$ adalah $25\text{ cm}$, berapakah panjang jari-jari lingkaran tersebut?

- **A. $7\text{ cm}$** ✅  
  <sub>Benar: Keliling $\triangle PKL = PK + KL + LP = PK + KT + TL + LP = (PK + KA) + (PL + LB) = PA + PB = 2 PA$. Karena kelilingnya $48\text{ cm}$, maka $PA = 24\text{ cm}$. Jari-jari lingkaran $r = OA = \sqrt{OP^2 - PA^2} = \sqrt{25^2 - 24^2} = \sqrt{49} = 7\text{ cm}$.</sub>
- B. $9\text{ cm}$  
  <sub>Salah: Siswa salah mengurangkan kuadrat pada teorema Pythagoras, menghitung $25 - 16 = 9$ tanpa mengakar selisih kuadrat.</sub>
- C. $14\text{ cm}$  
  <sub>Salah: Siswa menghitung panjang diameter lingkaran bukan panjang jari-jari lingkaran.</sub>
- D. $12\text{ cm}$  
  <sub>Salah: Siswa mengira panjang $PA$ sama dengan setengah jari-jari atau salah mengidentifikasi perbandingan sisi segitiga.</sub>

**Pembahasan:** Garis singgung dari satu titik ke lingkaran sama panjang:
$KA = KT$ dan $LB = LT$, serta $PA = PB$.

Keliling segitiga $PKL$:
$K_{\triangle PKL} = PK + KL + LP$
$K_{\triangle PKL} = PK + (KT + TL) + LP = (PK + KA) + (LP + LB) = PA + PB = 2PA$.

Diketahui keliling $\triangle PKL = 48\text{ cm}$, maka:
$2PA = 48 \implies PA = 24\text{ cm}$.

Karena garis singgung tegak lurus jari-jari di titik singgung ($OA \perp PA$), berlaku teorema Pythagoras pada $\triangle OAP$:
$r = OA = \sqrt{OP^2 - PA^2} = \sqrt{25^2 - 24^2} = \sqrt{625 - 576} = \sqrt{49} = 7\text{ cm}$.
**Acuan:** siswa — siswa hal.80

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b02-b-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: analisis sistem jari-jari persekutuan ganda*

Dua buah lingkaran terpisah memiliki jarak antara kedua titik pusat sebesar $20\text{ cm}$. Panjang garis singgung persekutuan dalamnya adalah $12\text{ cm}$, sedangkan panjang garis singgung persekutuan luarnya adalah $16\text{ cm}$. Berapakah panjang jari-jari lingkaran yang lebih besar?

- **A. $14\text{ cm}$** ✅  
  <sub>Benar: Dari garis singgung persekutuan dalam: $(R + r)^2 = d^2 - g^2 = 20^2 - 12^2 = 256 \implies R + r = 16$. Dari garis singgung persekutuan luar: $(R - r)^2 = d^2 - s^2 = 20^2 - 16^2 = 144 \implies R - r = 12$. Dengan menjumlahkan kedua persamaan diperoleh $2R = 28 \implies R = 14\text{ cm}$.</sub>
- B. $16\text{ cm}$  
  <sub>Salah: Siswa keliru menganggap nilai $R + r$ langsung sebagai panjang jari-jari lingkaran besar $R$.</sub>
- C. $2\text{ cm}$  
  <sub>Salah: Siswa menentukan panjang jari-jari lingkaran yang lebih kecil ($r$), bukan lingkaran yang lebih besar ($R$).</sub>
- D. $10\text{ cm}$  
  <sub>Salah: Siswa mengambil nilai rata-rata dari kedua panjang garis singgung $(12 + 16)/2$ atau setengah jarak antarpusat.</sub>

**Pembahasan:** Gunakan rumus garis singgung persekutuan dalam ($g$) dan luar ($s$):
1) $g^2 = d^2 - (R + r)^2$
$12^2 = 20^2 - (R + r)^2$
$(R + r)^2 = 400 - 144 = 256$
$R + r = 16$  ...(Persamaan 1)

2) $s^2 = d^2 - (R - r)^2$
$16^2 = 20^2 - (R - r)^2$
$(R - r)^2 = 400 - 256 = 144$
$R - r = 12$  ...(Persamaan 2)

Jumlahkan Persamaan 1 dan Persamaan 2:
$(R + r) + (R - r) = 16 + 12$
$2R = 28 \implies R = 14\text{ cm}$.
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b02-b-hard-bt01-013
*variasi (konteks) | C5 | 4 langkah | jenis: analisis selisih kuadrat garis singgung*

Dua buah lingkaran memiliki pusat yang berjarak $26\text{ cm}$. Jika kedua lingkaran tersebut masing-masing berjari-jari $17\text{ cm}$ dan $7\text{ cm}$, berapakah selisih kuadrat antara panjang garis singgung persekutuan luar dan panjang garis singgung persekutuan dalamnya?

- **A. $476\text{ cm}^2$** ✅  
  <sub>Benar: Kuadrat GSPL adalah $s^2 = d^2 - (R - r)^2$ dan kuadrat GSPD adalah $g^2 = d^2 - (R + r)^2$. Selisih kuadratnya adalah $s^2 - g^2 = (R + r)^2 - (R - r)^2 = 4Rr = 4 \times 17 \times 7 = 476\text{ cm}^2$.</sub>
- B. $376\text{ cm}^2$  
  <sub>Salah: Kesalahan aritmetika saat mengalikan $4 \times 17 \times 7$ atau salah menghitung $576 - 100$.</sub>
- C. $100\text{ cm}^2$  
  <sub>Salah: Hanya menghitung nilai kuadrat garis singgung persekutuan dalam $g^2 = 26^2 - 24^2 = 100$.</sub>
- D. $576\text{ cm}^2$  
  <sub>Salah: Hanya menghitung nilai kuadrat garis singgung persekutuan luar $s^2 = 26^2 - 10^2 = 576$.</sub>

**Pembahasan:** Diketahui jarak pusat $d = 26\text{ cm}$, jari-jari $R = 17\text{ cm}$, dan $r = 7\text{ cm}$.

1. Kuadrat panjang garis singgung persekutuan luar ($s^2$):
$$s^2 = d^2 - (R - r)^2 = 26^2 - (17 - 7)^2 = 676 - 100 = 576\text{ cm}^2$$

2. Kuadrat panjang garis singgung persekutuan dalam ($g^2$):
$$g^2 = d^2 - (R + r)^2 = 26^2 - (17 + 7)^2 = 676 - 24^2 = 676 - 576 = 100\text{ cm}^2$$

3. Menghitung selisih kuadrat keduanya:
$$s^2 - g^2 = 576 - 100 = 476\text{ cm}^2$$

Secara identitas aljabar, selisih kuadrat ini juga setara dengan $4Rr = 4(17)(7) = 476\text{ cm}^2$.
**Acuan:** siswa — siswa hal.84 Latihan 2.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b02-b-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: keliling segitiga garis singgung terpotong*

Dari sebuah titik $P$ di luar lingkaran yang berpusat di $O$, dibuat dua garis singgung yang menyentuh lingkaran di titik $A$ dan $B$ dengan panjang ruas garis singgung $PA = 18\text{ cm}$. Garis singgung ketiga ditarik memotong ruas garis $PA$ di titik $Q$, memotong ruas garis $PB$ di titik $R$, serta menyinggung busur minor lingkaran di titik $T$. Berapakah keliling segitiga $PQR$?

- A. $54\text{ cm}$  
  <sub>Salah: Mengalikan panjang ruas garis singgung $PA$ dengan 3 karena menganggap ketiga sisi segitiga sama dengan panjang garis singgung.</sub>
- **B. $36\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan sifat garis singgung dari titik luar, ruas garis $QA = QT$ dan $RB = RT$. Maka keliling $\triangle PQR = PQ + QR + RP = PQ + (QT + TR) + RP = (PQ + QA) + (RP + RB) = PA + PB = 18 + 18 = 36\text{ cm}$.</sub>
- C. $18\text{ cm}$  
  <sub>Salah: Hanya menggunakan panjang satu ruas garis singgung $PA$ tanpa memperhitungkan kedua batas singgung.</sub>
- D. $27\text{ cm}$  
  <sub>Salah: Mengasumsikan keliling segitiga adalah $1,5$ kali panjang garis singgung utama.</sub>

**Pembahasan:** Berdasarkan sifat garis singgung lingkaran:
1. Garis singgung dari titik $P$ memiliki panjang yang sama: $PA = PB = 18\text{ cm}$.
2. Garis singgung ketiga menyentuh lingkaran di $T$ dan dipotong oleh garis $PA$ di $Q$ serta $PB$ di $R$. Dari titik luar $Q$, panjang garis singgung ke lingkaran adalah $QA = QT$.
3. Dari titik luar $R$, panjang garis singgung ke lingkaran adalah $RB = RT$.
4. Keliling $\triangle PQR$ dapat diuraikan:
$$\text{Keliling } \triangle PQR = PQ + QR + RP$$
$$\text{Keliling } = PQ + (QT + TR) + RP$$
Substitusikan $QT = QA$ dan $TR = RB$:
$$\text{Keliling } = (PQ + QA) + (RB + RP) = PA + PB$$
$$\text{Keliling } = 18\text{ cm} + 18\text{ cm} = 36\text{ cm}$$
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b02-b-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: rekonstruksi parameter garis singgung ganda*

Jarak titik pusat dua buah lingkaran adalah $65\text{ cm}$. Jari-jari lingkaran besar adalah $R = (5x + 3)\text{ cm}$ dan lingkaran kecil adalah $r = (3x + 1)\text{ cm}$. Jika panjang garis singgung persekutuan dalam kedua lingkaran tersebut adalah $25\text{ cm}$, berapakah panjang garis singgung persekutuan luar kedua lingkaran tersebut?

- A. $56\text{ cm}$  
  <sub>Salah: Kesalahan menentukan nilai $x$ atau salah saat menghitung selisih kuadrat $65^2 - 16^2$.</sub>
- B. $60\text{ cm}$  
  <sub>Salah: Keliru menganggap panjang garis singgung persekutuan luar sama dengan jumlah jari-jari $(R + r) = 60$.</sub>
- **C. $63\text{ cm}$** ✅  
  <sub>Benar: Dari $g = \sqrt{d^2 - (R + r)^2}$, diperoleh $R + r = \sqrt{65^2 - 25^2} = 60$. Persamaan $(5x + 3) + (3x + 1) = 60$ menghasilkan $x = 7$, sehingga $R = 38\text{ cm}$ dan $r = 22\text{ cm}$. Selisih jari-jari $R - r = 16\text{ cm}$, maka panjang garis singgung persekutuan luar adalah $s = \sqrt{65^2 - 16^2} = 63\text{ cm}$.</sub>
- D. $48\text{ cm}$  
  <sub>Salah: Keliru menggunakan rumus garis singgung luar dengan mengurangkan $R + r$ bukan $R - r$.</sub>

**Pembahasan:** Langkah 1: Menentukan jumlah jari-jari $(R + r)$ dari garis singgung persekutuan dalam ($g$):
$$g = \sqrt{d^2 - (R + r)^2}$$
$$25 = \sqrt{65^2 - (R + r)^2} \implies (R + r)^2 = 4.225 - 625 = 3.600$$
$$R + r = 60\text{ cm}$$

Langkah 2: Menentukan nilai $x$:
$$(5x + 3) + (3x + 1) = 60$$
$$8x + 4 = 60 \implies 8x = 56 \implies x = 7$$

Langkah 3: Menghitung jari-jari masing-masing lingkaran:
$$R = 5(7) + 3 = 38\text{ cm}$$
$$r = 3(7) + 1 = 22\text{ cm}$$

Langkah 4: Menentukan selisih jari-jari:
$$R - r = 38 - 22 = 16\text{ cm}$$

Langkah 5: Menghitung panjang garis singgung persekutuan luar ($s$):
$$s = \sqrt{d^2 - (R - r)^2} = \sqrt{65^2 - 16^2} = \sqrt{4.225 - 256} = \sqrt{3.969} = 63\text{ cm}$$
**Acuan:** siswa — siswa hal.83

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b02-b-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: titik temu garis singgung luar persekutuan*

Dua penampang lingkaran sumber cahaya (lingkaran besar $A$) dan bola penghalang (lingkaran kecil $B$) masing-masing memiliki jari-jari $30\text{ cm}$ dan $6\text{ cm}$. Jarak antara kedua pusat lingkaran tersebut adalah $96\text{ cm}$. Garis singgung persekutuan luar kedua lingkaran diperpanjang sehingga berpotongan di satu titik $T$ di belakang lingkaran kecil (membentuk puncak kerucut umbra). Berapakah jarak dari titik pusat lingkaran kecil $B$ ke titik perpotongan $T$ tersebut?

- A. $20\text{ cm}$  
  <sub>Salah: Salah dalam membagi jarak pusat terhadap selisih jari-jari tanpa memperhatikan proporsi kesebangunan titik temu.</sub>
- B. $16\text{ cm}$  
  <sub>Salah: Keliru menggunakan perbandingan kesebangunan $\frac{BT}{AB} = \frac{r}{R + r}$.</sub>
- C. $32\text{ cm}$  
  <sub>Salah: Membagi jarak antar pusat lingkaran langsung dengan rasio pembesaran tanpa mengurangkan suku $BT$.</sub>
- **D. $24\text{ cm}$** ✅  
  <sub>Benar: Garis singgung tegak lurus jari-jari sehingga segitiga siku-siku yang melalui titik pusat lingkaran besar dan kecil sebangun terhadap titik $T$. Rasio $\frac{AT}{BT} = \frac{R}{r} = \frac{30}{6} = 5$. Karena $AT = AB + BT = 96 + BT$, maka $\frac{96 + BT}{BT} = 5 \implies 4BT = 96 \implies BT = 24\text{ cm}$.</sub>

**Pembahasan:** Misalkan titik pusat lingkaran besar adalah $A$, pusat lingkaran kecil adalah $B$, dan kedua garis singgung persekutuan luar berpotongan di titik $T$.

1. Karena garis hubung pusat $AB$ simetris terhadap kedua garis singgung luar, titik-titik $A$, $B$, dan $T$ berada pada satu garis lurus dengan urutan $A - B - T$, sehingga $AT = AB + BT = 96 + BT$.
2. Garis singgung tegak lurus dengan jari-jari lingkaran besar $R$ dan jari-jari lingkaran kecil $r$ pada masing-masing titik singgung.
3. Terbentuk dua segitiga siku-siku sebangun yang memiliki sudut sekutu di titik $T$, sehingga berlaku perbandingan:
$$\frac{AT}{BT} = \frac{R}{r}$$
4. Substitusikan nilai yang diketahui:
$$\frac{96 + BT}{BT} = \frac{30}{6} = 5$$
5. Selesaikan persamaan untuk $BT$:
$$96 + BT = 5BT$$
$$4BT = 96$$
$$BT = 24\text{ cm}$$

Jadi, jarak dari pusat lingkaran kecil ke titik temu $T$ adalah $24\text{ cm}$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11-b02-b-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: tali busur singgung lingkaran sepusat*

Dua buah lingkaran sepusat (konsentris) membentuk daerah cincin di antara kedua kelilingnya. Luas daerah cincin di antara kedua lingkaran tersebut adalah $576\pi\text{ cm}^2$. Sebuah ruas garis ditarik sebagai tali busur pada lingkaran besar yang sekaligus menyinggung lingkaran kecil. Berapakah panjang tali busur tersebut?

- A. $36\text{ cm}$  
  <sub>Salah: Salah melakukan operasi penarikan akar kuadrat dari selisih kuadrat jari-jari.</sub>
- B. $24\text{ cm}$  
  <sub>Salah: Hanya menghitung setengah panjang tali busur ($x = \sqrt{R^2 - r^2}$) dan lupa mengalikannya dengan 2.</sub>
- **C. $48\text{ cm}$** ✅  
  <sub>Benar: Misalkan jari-jari lingkaran luar adalah $R$ dan lingkaran dalam adalah $r$. Luas cincin adalah $\pi(R^2 - r^2) = 576\pi \implies R^2 - r^2 = 576$. Tali busur menyinggung lingkaran dalam di titik $T$ dan tegak lurus jari-jari $r$, sehingga setengah panjang tali busur memenuhi $x = \sqrt{R^2 - r^2} = \sqrt{576} = 24\text{ cm}$. Panjang tali busur utuh adalah $2x = 48\text{ cm}$.</sub>
- D. $96\text{ cm}$  
  <sub>Salah: Mengalikan panjang tali busur utuh dengan faktor 2 kembali.</sub>

**Pembahasan:** Misalkan jari-jari lingkaran besar adalah $R$ dan jari-jari lingkaran kecil adalah $r$.

1. Luas daerah cincin dinyatakan dengan:
$$L = \pi R^2 - \pi r^2 = \pi (R^2 - r^2)$$
Diketahui $L = 576\pi\text{ cm}^2$, sehingga:
$$\pi (R^2 - r^2) = 576\pi \implies R^2 - r^2 = 576$$

2. Tali busur lingkaran besar $AB$ menyinggung lingkaran kecil di titik $T$. Berdasarkan sifat garis singgung, jari-jari lingkaran kecil $OT$ tegak lurus dengan tali busur $AB$ ($OT \perp AB$), dan titik $T$ membagi dua tali busur tersebut sama panjang ($AT = TB$).

3. Pada segitiga siku-siku $OTA$, sisi miringnya adalah jari-jari lingkaran besar $OA = R$, dan salah satu sisi tegaknya adalah jari-jari lingkaran kecil $OT = r$. Berdasarkan Teorema Pythagoras:
$$AT^2 = OA^2 - OT^2 = R^2 - r^2 = 576$$
$$AT = \sqrt{576} = 24\text{ cm}$$

4. Panjang seluruh tali busur $AB$ adalah:
$$AB = 2 \times AT = 2 \times 24 = 48\text{ cm}$$
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11-b02-b-hard-bt01-018
*variasi (konteks) | C5 | 4 langkah | jenis: rekonstruksi keliling segiempat garis singgung*

Sebuah panel hiasan dinding berbentuk segiempat $ABCD$ dibuat sedemikian rupa sehingga keempat sisinya menyinggung sebuah ornamen lingkaran di dalamnya (segiempat garis singgung). Panjang sisi-sisi panel tersebut dinyatakan dalam variabel $x$, yaitu $AB = (3x - 1)\text{ cm}$, $BC = (2x + 7)\text{ cm}$, $CD = (4x - 6)\text{ cm}$, dan $DA = (3x + 4)\text{ cm}$. Keliling panel hiasan tersebut adalah ....

- **A. $112\text{ cm}$** ✅  
  <sub>Benar: Berdasarkan Teorema Pitot, jumlah panjang dua sisi yang saling berhadapan pada segiempat garis singgung adalah sama, sehingga $(3x - 1) + (4x - 6) = (2x + 7) + (3x + 4) \implies 7x - 7 = 5x + 11 \implies 2x = 18 \implies x = 9$. Keliling panel adalah $2 \times (7(9) - 7) = 112\text{ cm}$.</sub>
- B. $56\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung jumlah panjang dari satu pasang sisi berhadapan saja ($AB + CD$) dan lupa mengalikannya dengan dua untuk memperoleh keliling penuh.</sub>
- C. $126\text{ cm}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan tanda negatif saat memindahkan ruas konstanta ($7x - 7 = 5x + 11$ dianggap menghasilkan $2x = 20 \implies x = 10$) sebelum menghitung keliling.</sub>
- D. $104\text{ cm}$  
  <sub>Salah: Siswa salah menjumlahkan bentuk aljabar dengan menyamakan dua sisi yang bersebelahan ($AB + BC = CD + DA$) sehingga menghasilkan nilai $x$ yang keliru.</sub>

**Pembahasan:** Berdasarkan Teorema Pitot, pada segiempat garis singgung berlaku bahwa jumlah panjang sisi-sisi yang saling berhadapan adalah sama:
$$AB + CD = BC + DA$$

Substitusikan nilai sisi yang diketahui:
$$(3x - 1) + (4x - 6) = (2x + 7) + (3x + 4)$$
$$7x - 7 = 5x + 11$$
$$7x - 5x = 11 + 7$$
$$2x = 18$$
$$x = 9$$

Hitung panjang masing-masing sisi segiempat:
- $AB = 3(9) - 1 = 26\text{ cm}$
- $BC = 2(9) + 7 = 25\text{ cm}$
- $CD = 4(9) - 6 = 30\text{ cm}$
- $DA = 3(9) + 4 = 31\text{ cm}$

Keliling segiempat $ABCD$ adalah:
$$K = AB + BC + CD + DA = 26 + 25 + 30 + 31 = 112\text{ cm}$$
**Acuan:** siswa — siswa hal.84 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11-b02-b-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: titik singgung lingkaran dalam segitiga*

Sebuah segitiga siku-siku $ABC$ memiliki sudut siku-siku di $B$, dengan panjang sisi $AB = 15\text{ cm}$ dan $BC = 20\text{ cm}$. Sebuah lingkaran dalam menyinggung sisi $AB$, $BC$, dan $AC$ berturut-turut di titik $D$, $E$, dan $F$. Berapakah panjang ruas garis singgung $AF$?

- A. $12,5\text{ cm}$  
  <sub>Salah: Siswa mengira titik singgung $F$ membagi hipotenusa $AC$ tepat menjadi dua bagian yang sama panjang.</sub>
- B. $15\text{ cm}$  
  <sub>Salah: Siswa tertukar menghitung ruas garis singgung dari titik $C$, yaitu $CF = BC - r = 20 - 5 = 15\text{ cm}$.</sub>
- **C. $10\text{ cm}$** ✅  
  <sub>Benar: Panjang hipotenusa $AC = \sqrt{15^2 + 20^2} = 25\text{ cm}$. Jari-jari lingkaran dalam adalah $r = \frac{AB + BC - AC}{2} = \frac{15 + 20 - 25}{2} = 5\text{ cm}$. Karena garis singgung tegak lurus jari-jari dan sudut $B$ siku-siku, maka $BD = BE = r = 5\text{ cm}$. Dengan demikian, $AF = AD = AB - BD = 15 - 5 = 10\text{ cm}$.</sub>
- D. $5\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung nilai jari-jari lingkaran dalam atau panjang ruas garis singgung dari titik B ($BD$).</sub>

**Pembahasan:** Langkah 1: Hitung panjang hipotenusa $AC$ dengan Teorema Pythagoras:
$$AC = \sqrt{AB^2 + BC^2} = \sqrt{15^2 + 20^2} = \sqrt{225 + 400} = \sqrt{625} = 25\text{ cm}$$

Langkah 2: Tentukan jari-jari lingkaran dalam segitiga siku-siku ($r$):
$$r = \frac{AB + BC - AC}{2} = \frac{15 + 20 - 25}{2} = \frac{10}{2} = 5\text{ cm}$$

Langkah 3: Karena garis singgung tegak lurus dengan jari-jari lingkaran di titik singgung dan $\angle B = 90^\circ$, segiempat yang terbentuk di sudut $B$ adalah persegi bersisi $r$. Oleh karena itu:
$$BD = BE = r = 5\text{ cm}$$

Langkah 4: Dari sifat dua garis singgung dari satu titik di luar lingkaran, panjang ruas garis singgung yang ditarik dari titik $A$ ke lingkaran adalah sama:
$$AF = AD = AB - BD = 15\text{ cm} - 5\text{ cm} = 10\text{ cm}$$

Jadi, panjang ruas garis singgung $AF$ adalah $10\text{ cm}$.
**Acuan:** siswa — siswa hal.85

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
