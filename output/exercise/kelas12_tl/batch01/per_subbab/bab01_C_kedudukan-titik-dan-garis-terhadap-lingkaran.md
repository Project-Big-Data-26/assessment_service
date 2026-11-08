# Lembar koreksi — kelas12_tl SMA12L-B1 subbab C: Kedudukan Titik dan Garis terhadap Lingkaran

59 soal | easy 20, medium 20, hard 19 | variasi 28, orisinal 31
> **Kapasitas kurang (hard): 19 dari kuota 20** — 7 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b01-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik terhadap lingkaran*

Kedudukan titik $P(5, 7)$ terhadap lingkaran $L \equiv x^2 + y^2 - 4x - 6y - 12 = 0$ adalah ....

- A. di luar lingkaran  
  <sub>Salah: Mengira hasil substitusi positif karena lupa mengurangkan konstanta 12.</sub>
- B. di dalam lingkaran  
  <sub>Salah: Mengira hasil substitusi bernilai negatif karena salah menjumlahkan suku konstan.</sub>
- **C. terletak pada lingkaran** ✅  
  <sub>Benar: Substitusi titik $(5, 7)$ menghasilkan $5^2 + 7^2 - 4(5) - 6(7) - 12 = 25 + 49 - 20 - 42 - 12 = 0$, sehingga titik berada tepat pada lingkaran.</sub>
- D. berimpit dengan titik pusat lingkaran  
  <sub>Salah: Menyamakan kondisi nilai kuasa nol dengan titik pusat lingkaran.</sub>

**Pembahasan:** Substitusikan koordinat titik $P(5, 7)$ ke ruas kiri persamaan lingkaran:
$$K = 5^2 + 7^2 - 4(5) - 6(7) - 12$$
$$K = 25 + 49 - 20 - 42 - 12 = 0$$
Karena nilai kuasa $K = 0$, maka titik $P(5, 7)$ terletak pada lingkaran.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-1-a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b01-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: jarak titik ke pusat lingkaran*

Diketahui titik $A(6, 8)$ dan lingkaran $L \equiv x^2 + y^2 = 49$. Jarak titik $A$ terhadap titik pusat lingkaran $L$ adalah ....

- A. 7 satuan  
  <sub>Salah: Menyebutkan jari-jari lingkaran ($r = \sqrt{49} = 7$), bukan jarak titik ke pusat.</sub>
- B. 3 satuan  
  <sub>Salah: Menghitung selisih jarak titik ke pusat dengan jari-jari ($10 - 7 = 3$).</sub>
- C. 14 satuan  
  <sub>Salah: Menjumlahkan koordinat absis dan ordinat secara langsung ($6 + 8 = 14$).</sub>
- **D. 10 satuan** ✅  
  <sub>Benar: Pusat lingkaran berada di $(0, 0)$, sehingga jaraknya adalah $\sqrt{6^2 + 8^2} = \sqrt{36 + 64} = 10$.</sub>

**Pembahasan:** Lingkaran $L \equiv x^2 + y^2 = 49$ memiliki pusat di $O(0, 0)$.
Jarak titik $A(6, 8)$ ke pusat $O(0, 0)$ dihitung dengan rumus jarak dua titik:
$$OA = \sqrt{(6 - 0)^2 + (8 - 0)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$$
Jadi, jarak titik $A$ terhadap titik pusat lingkaran adalah 10 satuan.
**Acuan:** siswa — siswa hal.58 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b01-c-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan garis terhadap lingkaran*

Kedudukan garis $g: y = 2x$ terhadap lingkaran $L \equiv x^2 + y^2 = 20$ adalah ....

- A. memotong lingkaran tepat di satu titik saja  
  <sub>Salah: Menganggap garis memotong lingkaran hanya di satu titik tanpa menyadari sifat garis singgung atau garis secant.</sub>
- B. menyinggung lingkaran  
  <sub>Salah: Mengira diskriminan bernilai nol karena keliru dalam rumus $D = b^2 - 4ac$.</sub>
- **C. memotong lingkaran di dua titik berbeda** ✅  
  <sub>Benar: Substitusi menghasilkan $5x^2 - 20 = 0$ dengan $D = 0 - 4(5)(-20) = 400 > 0$, sehingga garis memotong di dua titik.</sub>
- D. tidak memotong maupun menyinggung lingkaran  
  <sub>Salah: Salah menghitung tanda diskriminan menjadi negatif akibat kesalahan tanda minus.</sub>

**Pembahasan:** Substitusikan $y = 2x$ ke persamaan lingkaran $x^2 + y^2 = 20$:
$$x^2 + (2x)^2 = 20$$
$$x^2 + 4x^2 - 20 = 0$$
$$5x^2 - 20 = 0$$
Nilai diskriminan dari $ax^2 + bx + c = 0$ dengan $a = 5, b = 0, c = -20$:
$$D = b^2 - 4ac = 0^2 - 4(5)(-20) = 400$$
Karena $D > 0$, maka garis $g$ memotong lingkaran di dua titik berbeda.
**Acuan:** pretest — kelas12_tl-b01-p0067-latihan-soal-kedudukan-4a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b01-c-easy-bt01-004
*orisinal | C2 | 1 langkah | jenis: nilai kuasa titik*

Nilai kuasa titik $P(-2, 4)$ terhadap lingkaran $L \equiv (x - 3)^2 + (y + 1)^2 = 25$ adalah ....

- A. 50  
  <sub>Salah: Lupa mengurangkan dengan jari-jari kuadrat ($r^2 = 25$).</sub>
- B. -25  
  <sub>Salah: Salah menghitung $(-5)^2$ menjadi $-25$ sehingga hasil akhir menjadi negatif.</sub>
- C. 0  
  <sub>Salah: Mengira titik terletak pada lingkaran tanpa menghitung dengan teliti.</sub>
- **D. 25** ✅  
  <sub>Benar: Kuasa titik dihitung dengan menyubstitusikan $(-2, 4)$ ke $(x - 3)^2 + (y + 1)^2 - 25$, diperoleh $(-5)^2 + 5^2 - 25 = 25$.</sub>

**Pembahasan:** Nilai kuasa titik $P(x_1, y_1)$ terhadap lingkaran $(x - a)^2 + (y - b)^2 = r^2$ dirumuskan dengan:
$$K = (x_1 - a)^2 + (y_1 - b)^2 - r^2$$
Substitusikan titik $P(-2, 4)$:
$$K = (-2 - 3)^2 + (4 + 1)^2 - 25$$
$$K = (-5)^2 + 5^2 - 25$$
$$K = 25 + 25 - 25 = 25$$
Jadi, nilai kuasa titik tersebut adalah 25.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b01-c-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: kriteria diskriminan kedudukan garis*

Jika persamaan suatu garis disubstitusikan ke persamaan lingkaran menghasilkan persamaan kuadrat baru dengan nilai diskriminan $D = 0$, maka kedudukan garis tersebut terhadap lingkaran adalah ....

- A. melalui titik pusat lingkaran  
  <sub>Salah: Menyamakan nilai nol pada diskriminan dengan titik koordinat pusat lingkaran.</sub>
- **B. menyinggung lingkaran** ✅  
  <sub>Benar: Berdasarkan sifat diskriminan, $D = 0$ menunjukkan garis memiliki tepat satu titik sekutu (menyinggung lingkaran).</sub>
- C. memotong lingkaran di dua titik  
  <sub>Salah: Tertukar dengan syarat untuk $D > 0$.</sub>
- D. tidak memotong maupun menyinggung lingkaran  
  <sub>Salah: Tertukar dengan syarat untuk $D < 0$.</sub>

**Pembahasan:** Kedudukan garis terhadap lingkaran ditentukan oleh nilai diskriminan ($D$) persamaan kuadrat hasil substitusi:
1. $D > 0$: garis memotong lingkaran di dua titik berbeda.
2. $D = 0$: garis menyinggung lingkaran (memiliki satu titik persekutuan).
3. $D < 0$: garis tidak memotong maupun menyinggung lingkaran.
Jadi, jika $D = 0$, garis menyinggung lingkaran.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b01-c-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: kedudukan titik terhadap lingkaran kanonik*

Kedudukan titik $B(4, 5)$ terhadap lingkaran $L \equiv x^2 + y^2 = 36$ adalah ....

- **A. di luar lingkaran** ✅  
  <sub>Benar: Substitusi titik $B(4, 5)$ ke bentuk $x^2 + y^2 - 36$ menghasilkan $4^2 + 5^2 - 36 = 16 + 25 - 36 = 5 > 0$ (kuasa positif), sehingga titik berada di luar lingkaran.</sub>
- B. pada lingkaran  
  <sub>Salah: Siswa salah menghitung $16 + 25 = 41$ disamakan dengan 36 sehingga dianggap berada pada lingkaran.</sub>
- C. di dalam lingkaran  
  <sub>Salah: Siswa salah mengira nilai kuasa positif berarti berada di dalam lingkaran.</sub>
- D. tepat di titik pusat lingkaran  
  <sub>Salah: Siswa salah memahami konsep kedudukan titik sebagai letak koordinat pusat.</sub>

**Pembahasan:** Substitusikan koordinat titik $B(4, 5)$ ke persamaan lingkaran $x^2 + y^2 - 36$:
$$K_B = 4^2 + 5^2 - 36 = 16 + 25 - 36 = 5$$
Karena nilai kuasa $K_B > 0$, maka titik $B(4, 5)$ berada di luar lingkaran.
**Acuan:** siswa — siswa hal.57 Ayo Mencoba 1.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b01-c-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik terhadap lingkaran umum*

Kedudukan titik $M(-1, 2)$ terhadap lingkaran $L \equiv x^2 + y^2 + 6x - 4y + 4 = 0$ adalah ....

- A. pada lingkaran  
  <sub>Salah: Siswa mengabaikan konstanta $+4$ sehingga mengira hasilnya 0.</sub>
- **B. di dalam lingkaran** ✅  
  <sub>Benar: Substitusi $x = -1$ dan $y = 2$ menghasilkan $(-1)^2 + 2^2 + 6(-1) - 4(2) + 4 = 1 + 4 - 6 - 8 + 4 = -5 < 0$, sehingga titik berada di dalam lingkaran.</sub>
- C. menyinggung lingkaran  
  <sub>Salah: Siswa tertukar antara istilah kedudukan garis (menyinggung) dengan kedudukan titik.</sub>
- D. di luar lingkaran  
  <sub>Salah: Siswa salah menghitung tanda negatif $(-1)^2 = -1$ atau salah operasi sehingga memperoleh hasil positif.</sub>

**Pembahasan:** Langkah 1: Substitusikan koordinat titik $M(-1, 2)$ ke ruas kiri persamaan lingkaran:
$$K_M = (-1)^2 + (2)^2 + 6(-1) - 4(2) + 4 = 1 + 4 - 6 - 8 + 4 = -5$$
Langkah 2: Karena nilai kuasa $K_M = -5 < 0$, maka titik $M(-1, 2)$ berada di dalam lingkaran.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-1-c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b01-c-easy-bt01-008
*orisinal | C2 | 1 langkah | jenis: perhitungan kuasa titik umum*

Nilai kuasa titik $P(3, 4)$ terhadap lingkaran $L \equiv x^2 + y^2 - 2x - 4y - 11 = 0$ adalah ....

- A. $-14$  
  <sub>Salah: Siswa salah mengalikan koefisien $-2(3)$ menjadi $-12$.</sub>
- B. $8$  
  <sub>Salah: Siswa salah tanda saat menjumlahkan suku negatif.</sub>
- **C. $-8$** ✅  
  <sub>Benar: $K_P = 3^2 + 4^2 - 2(3) - 4(4) - 11 = 9 + 16 - 6 - 16 - 11 = -8$.</sub>
- D. $3$  
  <sub>Salah: Siswa lupa mengikutsertakan konstanta $-11$ pada perhitungan.</sub>

**Pembahasan:** Substitusikan titik $P(3, 4)$ ke persamaan lingkaran:
$$K_P = 3^2 + 4^2 - 2(3) - 4(4) - 11$$
$$K_P = 9 + 16 - 6 - 16 - 11 = -8$$
Jadi, nilai kuasa titik tersebut adalah $-8$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b01-c-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: kedudukan garis khusus terhadap lingkaran*

Kedudukan garis $y = 6$ terhadap lingkaran $L \equiv x^2 + y^2 = 25$ adalah ....

- A. melalui titik pusat lingkaran  
  <sub>Salah: Siswa salah memahami persamaan garis $y = 6$ melalui titik $(0,0)$.</sub>
- B. menyinggung lingkaran  
  <sub>Salah: Siswa keliru mengira garis batas selisih tetap menyinggung lingkaran.</sub>
- **C. tidak memotong dan tidak menyinggung lingkaran** ✅  
  <sub>Benar: Substitusi $y = 6$ menghasilkan $x^2 + 36 = 25 \iff x^2 = -11$. Karena tidak ada nilai $x$ real yang memenuhi ($D < 0$), garis tidak memotong maupun menyinggung lingkaran.</sub>
- D. memotong lingkaran di dua titik berbeda  
  <sub>Salah: Siswa mengabaikan tanda minus pada $x^2 = -11$ dan menganggap terdapat dua solusi real.</sub>

**Pembahasan:** Substitusikan persamaan garis $y = 6$ ke persamaan lingkaran:
$$x^2 + 6^2 = 25$$
$$x^2 + 36 = 25$$
$$x^2 = -11$$
Karena kuadrat suatu bilangan real tidak pernah bernilai negatif, persamaan ini tidak memiliki penyelesaian real (diskriminan $D < 0$). Dengan demikian, garis $y = 6$ tidak memotong dan tidak menyinggung lingkaran $L$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b01-c-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik bentuk baku*

Kedudukan titik $A(10, 2)$ terhadap lingkaran $L \equiv (x - 7)^2 + (y + 3)^2 = 25$ adalah ....

- A. di dalam lingkaran  
  <sub>Salah: Mengira nilai positif berarti titik berada di dalam lingkaran.</sub>
- **B. di luar lingkaran** ✅  
  <sub>Benar: Kuasa titik $K = (10 - 7)^2 + (2 + 3)^2 - 25 = 9 + 25 - 25 = 9 > 0$, bernilai positif sehingga titik berada di luar lingkaran.</sub>
- C. pada lingkaran  
  <sub>Salah: Keliru menganggap hasil substitusi sama dengan nol tanpa menghitung secara tepat.</sub>
- D. pada pusat lingkaran  
  <sub>Salah: Menyamakan kedudukan di luar lingkaran dengan pusat lingkaran.</sub>

**Pembahasan:** Substitusikan titik $A(10, 2)$ ke persamaan lingkaran:
$K = (10 - 7)^2 + (2 + 3)^2 - 25$
$K = 3^2 + 5^2 - 25 = 9 + 25 - 25 = 9$
Karena $K > 0$, titik $A(10, 2)$ berada di luar lingkaran.
**Acuan:** siswa — siswa hal.57 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b01-c-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik bentuk umum*

Kedudukan titik $A(5, 5)$ terhadap lingkaran $L \equiv x^2 + y^2 - 4x - 2y - 20 = 0$ adalah ....

- **A. terletak pada lingkaran** ✅  
  <sub>Benar: Nilai kuasa titik $K = 5^2 + 5^2 - 4(5) - 2(5) - 20 = 25 + 25 - 20 - 10 - 20 = 0$, sehingga titik terletak pada lingkaran.</sub>
- B. di luar lingkaran  
  <sub>Salah: Kesalahan tanda operasi penjumlahan atau pengurangan menghasilkan nilai positif.</sub>
- C. tidak dapat ditentukan  
  <sub>Salah: Anggapan keliru bahwa persamaan umum tidak dapat langsung disubstitusikan.</sub>
- D. di dalam lingkaran  
  <sub>Salah: Kesalahan hitung aljabar menghasilkan nilai negatif.</sub>

**Pembahasan:** Substitusikan koordinat titik $A(5, 5)$ ke ruas kiri persamaan lingkaran:
$K = 5^2 + 5^2 - 4(5) - 2(5) - 20$
$K = 25 + 25 - 20 - 10 - 20 = 0$
Karena nilai kuasa titik bernilai $0$, maka titik $A(5, 5)$ terletak pada lingkaran.
**Acuan:** siswa — siswa hal.56 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b01-c-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: titik potong garis horizontal*

Titik potong lingkaran $L \equiv (x - 5)^2 + (y + 2)^2 = 16$ dengan garis $y = -2$ adalah ....

- A. $(1, 2)$ dan $(9, 2)$  
  <sub>Salah: Lupa tanda negatif pada koordinat $y$ dari garis.</sub>
- **B. $(1, -2)$ dan $(9, -2)$** ✅  
  <sub>Benar: Substitusi $y = -2$ menghasilkan $(x - 5)^2 = 16$, sehingga $x - 5 = \pm 4$, diperoleh $x = 1$ atau $x = 9$.</sub>
- C. $(-1, -2)$ dan $(9, -2)$  
  <sub>Salah: Salah menghitung $5 - 4$ menjadi $-1$.</sub>
- D. $(5, -2)$ dan $(16, -2)$  
  <sub>Salah: Mengambil angka langsung dari pusat lingkaran dan jari-jari tanpa menyelesaikan akar persamaan kuadrat.</sub>

**Pembahasan:** Substitusikan $y = -2$ ke persamaan lingkaran:
$(x - 5)^2 + (-2 + 2)^2 = 16$
$(x - 5)^2 + 0 = 16$
$x - 5 = \pm \sqrt{16}$
$x - 5 = \pm 4$
Untuk $x - 5 = -4 \implies x = 1$
Untuk $x - 5 = 4 \implies x = 9$
Jadi, titik potongnya adalah $(1, -2)$ dan $(9, -2)$.
**Acuan:** siswa — siswa hal.62 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b01-c-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: definisi tanda kuasa titik*

Jika koordinat suatu titik disubstitusikan ke persamaan lingkaran berbentuk baku maupun umum dan menghasilkan nilai kuasa titik yang bernilai negatif, maka kedudukan titik tersebut adalah ....

- A. di pusat lingkaran  
  <sub>Salah: Mengira hanya titik pusat yang menghasilkan nilai negatif.</sub>
- B. pada lingkaran  
  <sub>Salah: Keliru dengan syarat kuasa titik bernilai nol.</sub>
- **C. di dalam lingkaran** ✅  
  <sub>Benar: Berdasarkan definisi kuasa titik, nilai negatif menunjukkan titik berada di dalam lingkaran.</sub>
- D. di luar lingkaran  
  <sub>Salah: Keliru dengan syarat kuasa titik bernilai positif.</sub>

**Pembahasan:** Kriteria kedudukan titik berdasarkan nilai kuasa titik ($K$):
1. $K < 0$ (bernilai negatif): titik berada di dalam lingkaran.
2. $K = 0$: titik berada pada lingkaran.
3. $K > 0$ (bernilai positif): titik berada di luar lingkaran.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b01-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: kriteria diskriminan garis negatif*

Persamaan garis $g$ disubstitusikan ke persamaan lingkaran $L$ sehingga terbentuk persamaan kuadrat persekutuan. Jika nilai diskriminan dari persamaan kuadrat tersebut bernilai negatif ($D < 0$), maka kedudukan garis $g$ terhadap lingkaran $L$ adalah ....

- A. memotong lingkaran di dua titik berlainan  
  <sub>Salah: Kondisi ini terjadi jika nilai diskriminan $D > 0$.</sub>
- B. menyinggung lingkaran di satu titik  
  <sub>Salah: Kondisi ini terjadi jika nilai diskriminan $D = 0$.</sub>
- C. melalui titik pusat lingkaran  
  <sub>Salah: Diskriminan negatif tidak berkaitan dengan garis melalui pusat lingkaran.</sub>
- **D. tidak memotong dan tidak menyinggung lingkaran** ✅  
  <sub>Benar: Nilai diskriminan negatif menunjukkan persamaan kuadrat tidak memiliki penyelesaian real sehingga garis tidak bersekutu dengan lingkaran.</sub>

**Pembahasan:** Hubungan nilai diskriminan ($D$) persamaan kuadrat persekutuan garis dan lingkaran:
- $D > 0$: garis memotong lingkaran di dua titik berbeda.
- $D = 0$: garis menyinggung lingkaran (memotong di satu titik).
- $D < 0$: garis tidak memotong dan tidak menyinggung lingkaran.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b01-c-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik format pusat ab*

Kedudukan titik $B(7, 4)$ terhadap lingkaran $L \equiv (x - 5)^2 + (y - 4)^2 = 9$ adalah ....

- A. pada lingkaran  
  <sub>Salah: Mengira nilai ruas kiri sama dengan $r^2$ karena salah menghitung $2^2 = 9$.</sub>
- B. di luar lingkaran  
  <sub>Salah: Keliru menganggap nilai $4$ lebih besar dari jari-jari lingkaran ($r = 3$) tanpa mengkuadratkannya.</sub>
- C. tepat di titik pusat lingkaran  
  <sub>Salah: Mengabaikan nilai koordinat $x$ dan hanya melihat koordinat $y = 4$ yang sama dengan ordinat pusat.</sub>
- **D. di dalam lingkaran** ✅  
  <sub>Benar: Substitusi titik $B(7, 4)$ ke ruas kiri menghasilkan $(7 - 5)^2 + (4 - 4)^2 = 2^2 + 0^2 = 4$. Karena $4 < 9$, titik terletak di dalam lingkaran.</sub>

**Pembahasan:** Substitusikan titik $B(7, 4)$ ke persamaan lingkaran $L \equiv (x - 5)^2 + (y - 4)^2 = 9$:
$$(7 - 5)^2 + (4 - 4)^2 = 2^2 + 0 = 4$$
Karena $4 < 9$, maka nilai kuasa titik bernilai negatif ($4 - 9 = -5 < 0$). Dengan demikian, titik $B(7, 4)$ berada di dalam lingkaran.
**Acuan:** siswa — siswa hal.56 Contoh Soal 1.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b01-c-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: analisis kedudukan titik umum*

Kedudukan titik $P(9, 6)$ terhadap lingkaran $L \equiv x^2 + y^2 - 6x - 4y - 12 = 0$ adalah ....

- **A. di luar lingkaran** ✅  
  <sub>Benar: Substitusi $P(9, 6)$ menghasilkan $9^2 + 6^2 - 6(9) - 4(6) - 12 = 81 + 36 - 54 - 24 - 12 = 27 > 0$, sehingga titik berada di luar lingkaran.</sub>
- B. pada lingkaran  
  <sub>Salah: Mengira titik memenuhi persamaan lingkaran atau salah menjumlahkan sehingga hasilnya nol.</sub>
- C. sepusat dengan lingkaran  
  <sub>Salah: Salah memahami konsep kedudukan titik sebagai titik pusat lingkaran.</sub>
- D. di dalam lingkaran  
  <sub>Salah: Salah menghitung operasi pengurangan suku linier sehingga memperoleh hasil bertanda negatif.</sub>

**Pembahasan:** Substitusikan titik $P(9, 6)$ ke dalam bentuk umum lingkaran:
$$K = 9^2 + 6^2 - 6(9) - 4(6) - 12$$
$$K = 81 + 36 - 54 - 24 - 12 = 27$$
Karena nilai kuasa titik $K = 27 > 0$ (bernilai positif), maka titik $P(9, 6)$ terletak di luar lingkaran.
**Acuan:** siswa — siswa hal.57 Ayo Mencoba 1.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b01-c-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: kedudukan titik pada lingkaran umum*

Kedudukan titik $T(4, -1)$ terhadap lingkaran $L \equiv x^2 + y^2 - 4x + 6y + 5 = 0$ adalah ....

- **A. pada lingkaran** ✅  
  <sub>Benar: Substitusi titik $T(4, -1)$ menghasilkan $4^2 + (-1)^2 - 4(4) + 6(-1) + 5 = 16 + 1 - 16 - 6 + 5 = 0$, sehingga titik terletak tepat pada lingkaran.</sub>
- B. di dalam lingkaran  
  <sub>Salah: Salah menghitung $(-1)^2$ menjadi $-1$ sehingga hasil akhirnya $-2 < 0$.</sub>
- C. di luar lingkaran  
  <sub>Salah: Salah tanda pada perkalian $6(-1)$ menjadi $+6$ sehingga hasilnya bernilai positif.</sub>
- D. tidak dapat ditentukan  
  <sub>Salah: Menganggap bentuk persamaan umum lingkaran tidak dapat digunakan langsung untuk menguji posisi titik.</sub>

**Pembahasan:** Substitusikan titik $T(4, -1)$ ke persamaan lingkaran:
$$K = 4^2 + (-1)^2 - 4(4) + 6(-1) + 5$$
$$K = 16 + 1 - 16 - 6 + 5 = 0$$
Karena nilai kuasa titik $K = 0$, maka titik $T(4, -1)$ terletak pada lingkaran.
**Acuan:** siswa — siswa hal.59 Ayo Mencoba 1.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b01-c-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: konsep tanda kuasa positif*

Jika koordinat suatu titik disubstitusikan ke dalam persamaan lingkaran $L \equiv x^2 + y^2 + Ax + By + C = 0$ dan menghasilkan nilai kuasa titik yang bernilai positif, maka kedudukan titik tersebut adalah ....

- **A. di luar lingkaran** ✅  
  <sub>Benar: Berdasarkan definisi nilai kuasa titik, jika nilai kuasa bernilai positif ($K > 0$), maka titik berada di luar lingkaran.</sub>
- B. pada lingkaran  
  <sub>Salah: Tertukar dengan kriteria nilai kuasa sama dengan nol.</sub>
- C. di dalam lingkaran  
  <sub>Salah: Tertukar dengan kriteria nilai kuasa negatif.</sub>
- D. di pusat lingkaran  
  <sub>Salah: Mengira nilai positif menunjukkan titik berada di pusat lingkaran.</sub>

**Pembahasan:** Berdasarkan materi kuasa titik:
1. Kuasa titik bernilai negatif ($K < 0$) $\rightarrow$ titik di dalam lingkaran.
2. Kuasa titik bernilai nol ($K = 0$) $\rightarrow$ titik pada lingkaran.
3. Kuasa titik bernilai positif ($K > 0$) $\rightarrow$ titik di luar lingkaran.
Jadi, jika bernilai positif, titik tersebut berada di luar lingkaran.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b01-c-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: kedudukan garis vertikal lingkaran*

Kedudukan garis $x = 3$ terhadap lingkaran $L \equiv x^2 + y^2 = 9$ adalah ....

- A. tidak memotong dan tidak menyinggung lingkaran  
  <sub>Salah: Keliru mengira garis $x = 3$ berada di luar jangkauan lingkaran berjari-jari $3$.</sub>
- **B. menyinggung lingkaran** ✅  
  <sub>Benar: Substitusi $x = 3$ ke persamaan lingkaran menghasilkan $3^2 + y^2 = 9 \iff y^2 = 0 \iff y = 0$ (tepat satu titik potong $(3, 0)$), sehingga garis menyinggung lingkaran.</sub>
- C. melalui titik pusat lingkaran  
  <sub>Salah: Salah mengira garis $x = 3$ memuat titik pusat $(0, 0)$.</sub>
- D. memotong lingkaran di dua titik berbeda  
  <sub>Salah: Mengira persamaan kuadrat dalam $y$ selalu memiliki dua penyelesaian berlainan.</sub>

**Pembahasan:** Substitusikan persamaan garis $x = 3$ ke persamaan lingkaran $x^2 + y^2 = 9$:
$$3^2 + y^2 = 9$$
$$9 + y^2 = 9$$
$$y^2 = 0 \implies y = 0$$
Karena diperoleh tepat satu nilai penyelesaian real yaitu $y = 0$ (titik singgung di $(3, 0)$), maka garis $x = 3$ menyinggung lingkaran $L$.
**Acuan:** siswa — siswa hal.59

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b01-c-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi posisi titik baku*

Kedudukan titik $A(1, -2)$ terhadap lingkaran $L \equiv (x - 4)^2 + (y - 2)^2 = 40$ adalah ....

- A. pada lingkaran  
  <sub>Salah: Siswa salah menghitung $(-3)^2 + (-4)^2 = 9 + 16 = 25$ dan mengira sama dengan jari-jari lingkaran.</sub>
- B. di luar lingkaran  
  <sub>Salah: Siswa salah mengira bahwa ruas kiri $(1-4)^2 + (-2-2)^2 = 25$ langsung bernilai positif tanpa mengurangkannya dengan $r^2 = 40$.</sub>
- C. pada titik pusat lingkaran  
  <sub>Salah: Siswa keliru menganggap titik yang berada di dalam lingkaran selalu berimpit dengan titik pusat.</sub>
- **D. di dalam lingkaran** ✅  
  <sub>Benar: Nilai kuasa titik diperoleh dengan menyubstitusikan koordinat titik ke bentuk $(x - 4)^2 + (y - 2)^2 - 40$: $(1 - 4)^2 + (-2 - 2)^2 - 40 = (-3)^2 + (-4)^2 - 40 = 9 + 16 - 40 = -15$. Karena nilai kuasa negatif ($-15 < 0$), maka titik berada di dalam lingkaran.</sub>

**Pembahasan:** Untuk menentukan kedudukan titik $A(1, -2)$ terhadap lingkaran $L \equiv (x - 4)^2 + (y - 2)^2 = 40$, tentukan nilai kuasa titik $K$:
$$\begin{aligned} K &= (x_A - 4)^2 + (y_A - 2)^2 - 40 \\ &= (1 - 4)^2 + (-2 - 2)^2 - 40 \\ &= (-3)^2 + (-4)^2 - 40 \\ &= 9 + 16 - 40 \\ &= -15 \end{aligned}$$
Karena nilai kuasa titik $K < 0$, maka titik $A(1, -2)$ berada di dalam lingkaran.
**Acuan:** siswa — siswa hal.58 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b01-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: nilai parameter titik pada lingkaran*

Nilai $t$ yang memenuhi agar titik $P(t, -t)$ terletak pada lingkaran $L \equiv x^2 + y^2 + 6x - 2y - 24 = 0$ adalah ....

- A. $t = -3$ atau $t = 4$  
  <sub>Salah: Kesalahan menentukan pasangan faktor bilangan pembentuk $-12$ dan tanda akarnya.</sub>
- B. $t = -4$ atau $t = 3$  
  <sub>Salah: Kesalahan membagi koefisien linear saat menyederhanakan $2t^2 + 8t - 24 = 0$.</sub>
- C. $t = -2$ atau $t = 6$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan kuadrat $(t - 6)(t + 2) = 0$.</sub>
- **D. $t = -6$ atau $t = 2$** ✅  
  <sub>Benar: Substitusi $x = t$ dan $y = -t$ menghasilkan $t^2 + (-t)^2 + 6t - 2(-t) - 24 = 0 \iff 2t^2 + 8t - 24 = 0 \iff t^2 + 4t - 12 = 0$. Faktornya $(t + 6)(t - 2) = 0$, sehingga $t = -6$ atau $t = 2$.</sub>

**Pembahasan:** Agar titik $P(t, -t)$ terletak pada lingkaran, nilai kuasa titik harus sama dengan nol.
Substitusikan $x = t$ dan $y = -t$ ke persamaan lingkaran:
$$t^2 + (-t)^2 + 6(t) - 2(-t) - 24 = 0$$
$$t^2 + t^2 + 6t + 2t - 24 = 0$$
$$2t^2 + 8t - 24 = 0$$
Bagi kedua ruas dengan 2:
$$t^2 + 4t - 12 = 0$$
$$(t + 6)(t - 2) = 0$$
Diperoleh $t = -6$ atau $t = 2$.
**Acuan:** siswa — siswa hal.66 Latihan Soal Kedudukan Titik dan Garis terhadap Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b01-c-medium-bt01-002
*orisinal | C4 | 4 langkah | jenis: panjang tali busur persekutuan garis dan lingkaran*

Garis $g: y = x + 1$ memotong lingkaran $L \equiv x^2 + y^2 = 25$ di dua titik, yaitu titik $A$ dan $B$. Jarak antara titik $A$ dan titik $B$ adalah ....

- A. $5\sqrt{2}$ satuan  
  <sub>Salah: Menggunakan nilai jari-jari lingkaran dikalikan $\sqrt{2}$ tanpa menghitung titik potong sebenarnya.</sub>
- B. $14$ satuan  
  <sub>Salah: Menjumlahkan selisih absis ($7$) dan selisih ordinat ($7$) alih-alih menghitung jarak Euclidean $\sqrt{7^2 + 7^2}$.</sub>
- **C. $7\sqrt{2}$ satuan** ✅  
  <sub>Benar: Substitusi $y = x + 1$ ke $x^2 + y^2 = 25$ menghasilkan $2x^2 + 2x - 24 = 0 \iff x^2 + x - 12 = 0$. Akar-akarnya $x_1 = 3$ dan $x_2 = -4$. Titik potongnya $(3, 4)$ dan $(-4, -3)$. Jaraknya $\sqrt{(3 - (-4))^2 + (4 - (-3))^2} = \sqrt{49 + 49} = 7\sqrt{2}$.</sub>
- D. $7$ satuan  
  <sub>Salah: Hanya menghitung selisih nilai $x$ ($3 - (-4) = 7$) tanpa memasukkan komponen ordinat.</sub>

**Pembahasan:** Substitusikan $y = x + 1$ ke dalam persamaan lingkaran:
$$x^2 + (x + 1)^2 = 25$$
$$x^2 + x^2 + 2x + 1 - 25 = 0$$
$$2x^2 + 2x - 24 = 0$$
$$x^2 + x - 12 = 0$$
$$(x + 4)(x - 3) = 0$$
Diperoleh $x_1 = -4$ atau $x_2 = 3$.

Cari ordinat masing-masing titik:
- Untuk $x_1 = -4 \implies y_1 = -4 + 1 = -3$, sehingga $A(-4, -3)$
- Untuk $x_2 = 3 \implies y_2 = 3 + 1 = 4$, sehingga $B(3, 4)$

Jarak antara titik $A$ dan $B$:
$$AB = \sqrt{(3 - (-4))^2 + (4 - (-3))^2} = \sqrt{7^2 + 7^2} = \sqrt{49 + 49} = \sqrt{98} = 7\sqrt{2}$$
Jadi, jarak antara kedua titik potong adalah $7\sqrt{2}$ satuan.
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b01-c-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: nilai konstanta garis singgung lingkaran*

Agar garis $y = 2x + c$ menyinggung lingkaran $L \equiv x^2 + y^2 = 5$, nilai $c$ yang memenuhi adalah ....

- **A. $c = -5$ atau $c = 5$** ✅  
  <sub>Benar: Substitusi $y = 2x + c$ menghasilkan $5x^2 + 4cx + (c^2 - 5) = 0$. Syarat menyinggung $D = 0 \iff (4c)^2 - 4(5)(c^2 - 5) = 0 \iff 16c^2 - 20c^2 + 100 = 0 \iff -4c^2 = -100 \iff c^2 = 25 \iff c = \pm 5$.</sub>
- B. $c = -25$ atau $c = 25$  
  <sub>Salah: Lupa menarik akar kuadrat dari $c^2 = 25$.</sub>
- C. $c = -\sqrt{5}$ atau $c = \sqrt{5}$  
  <sub>Salah: Menganggap nilai $c$ langsung sama dengan $\pm r$ lingkaran.</sub>
- D. $c = -10$ atau $c = 10$  
  <sub>Salah: Kesalahan pada perhitungan diskriminan dengan rumus $b^2 - 2ac = 0$.</sub>

**Pembahasan:** Substitusikan garis $y = 2x + c$ ke dalam persamaan lingkaran $x^2 + y^2 = 5$:
$$x^2 + (2x + c)^2 = 5$$
$$x^2 + 4x^2 + 4cx + c^2 - 5 = 0$$
$$5x^2 + 4cx + (c^2 - 5) = 0$$
Dari persamaan kuadrat diperoleh $a = 5$, $b = 4c$, dan $c_k = c^2 - 5$.

Syarat garis menyinggung lingkaran adalah $D = 0$:
$$b^2 - 4ac_k = 0$$
$$(4c)^2 - 4(5)(c^2 - 5) = 0$$
$$16c^2 - 20(c^2 - 5) = 0$$
$$16c^2 - 20c^2 + 100 = 0$$
$$-4c^2 + 100 = 0$$
$$4c^2 = 100$$
$$c^2 = 25 \implies c = \pm 5$$
Jadi, nilai $c$ yang memenuhi adalah $c = -5$ atau $c = 5$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b01-c-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: batasan parameter garis memotong lingkaran*

Batasan nilai $n$ agar garis $y = 3x + n$ memotong lingkaran $L \equiv x^2 + y^2 = 10$ di dua titik berlainan adalah ....

- A. $-2\sqrt{10} < n < 2\sqrt{10}$  
  <sub>Salah: Kesalahan mengalikan koefisien $a$ saat menyusun diskriminan.</sub>
- B. $-100 < n < 100$  
  <sub>Salah: Lupa menarik akar kuadrat dari batas interval $n^2 < 100$.</sub>
- C. $n < -10$ atau $n > 10$  
  <sub>Salah: Terbalik dalam menyimpulkan tanda pertidaksamaan $-4n^2 + 400 > 0$ tanpa membalik tanda saat membagi dengan bilangan negatif.</sub>
- **D. $-10 < n < 10$** ✅  
  <sub>Benar: Substitusi menghasilkan $10x^2 + 6nx + (n^2 - 10) = 0$. Syarat memotong di dua titik berlainan $D > 0 \iff (6n)^2 - 4(10)(n^2 - 10) > 0 \iff 36n^2 - 40n^2 + 400 > 0 \iff -4n^2 + 400 > 0 \iff n^2 < 100 \iff -10 < n < 10$.</sub>

**Pembahasan:** Substitusikan $y = 3x + n$ ke dalam persamaan lingkaran $x^2 + y^2 = 10$:
$$x^2 + (3x + n)^2 = 10$$
$$x^2 + 9x^2 + 6nx + n^2 - 10 = 0$$
$$10x^2 + 6nx + (n^2 - 10) = 0$$

Diperoleh koefisien:
$a = 10$, $b = 6n$, $c = n^2 - 10$

Garis memotong lingkaran di dua titik jika diskriminan bernilai positif ($D > 0$):
$$b^2 - 4ac > 0$$
$$(6n)^2 - 4(10)(n^2 - 10) > 0$$
$$36n^2 - 40n^2 + 400 > 0$$
$$-4n^2 + 400 > 0$$
Bagi kedua ruas dengan $-4$ (tanda pertidaksamaan dibalik):
$$n^2 - 100 < 0$$
$$(n + 10)(n - 10) < 0$$
$$-10 < n < 10$$
Jadi, batas nilai $n$ adalah $-10 < n < 10$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b01-c-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: batasan parameter titik di dalam lingkaran*

Batasan nilai $k$ agar titik $M(k, -2)$ terletak di dalam lingkaran $L \equiv (x + 3)^2 + (y - 6)^2 = 100$ adalah ....

- A. $-3 < k < 9$  
  <sub>Salah: Siswa salah memindahkan tanda pada pertidaksamaan $-6 < k - 3 < 6$ bukannya $-6 < k + 3 < 6$.</sub>
- B. $-11 < k < 5$  
  <sub>Salah: Siswa salah menghitung $(-2 - 6)^2 = (-8)^2 = 64$ menjadi $(-4)^2 = 16$ sehingga $(k+3)^2 < 84$ atau keliru mengurangkan konstanta.</sub>
- C. $k < -9$ atau $k > 3$  
  <sub>Salah: Siswa tertukar dengan syarat titik berada di luar lingkaran (kuasa positif).</sub>
- **D. $-9 < k < 3$** ✅  
  <sub>Benar: Substitusi titik ke persamaan lingkaran dengan syarat kuasa titik $< 0$ menghasilkan pertidaksamaan kuadrat $(k + 3)^2 < 36$ sehingga diperoleh $-9 < k < 3$.</sub>

**Pembahasan:** Agar titik $M(k, -2)$ terletak di dalam lingkaran $L \equiv (x + 3)^2 + (y - 6)^2 = 100$, nilai kuasa titik harus bertanda negatif ($K_M < 0$):
$$
(k + 3)^2 + (-2 - 6)^2 - 100 < 0
$$
$$
(k + 3)^2 + (-8)^2 - 100 < 0
$$
$$
(k + 3)^2 + 64 - 100 < 0
$$
$$
(k + 3)^2 - 36 < 0
$$
$$
(k + 3)^2 < 36
$$
$$
-6 < k + 3 < 6
$$
Kurangkan ketiga ruas dengan 3:
$$
-9 < k < 3
$$
Jadi, batasan nilai $k$ yang memenuhi adalah $-9 < k < 3$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b01-c-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: batasan parameter titik di luar lingkaran*

Batasan nilai $b$ agar titik $Q(4, b)$ terletak di luar lingkaran $L \equiv (x - 1)^2 + (y + 5)^2 = 45$ adalah ....

- A. $-11 < b < 1$  
  <sub>Salah: Siswa salah menggunakan tanda interval titik di dalam lingkaran $(< 0)$.</sub>
- **B. $b < -11$ atau $b > 1$** ✅  
  <sub>Benar: Substitusi $x = 4$ menghasilkan $(b + 5)^2 > 36$ yang memiliki penyelesaian $b + 5 < -6$ atau $b + 5 > 6$, yaitu $b < -11$ atau $b > 1$.</sub>
- C. $b < -7$ atau $b > 7$  
  <sub>Salah: Siswa lupa memperhitungkan pergeseran ordinat pusat $+5$.</sub>
- D. $b < -1$ atau $b > 11$  
  <sub>Salah: Siswa salah mengoperasikan tanda pada pertidaksamaan nilai mutlak menjadi $b - 5 > 6$.</sub>

**Pembahasan:** Agar titik $Q(4, b)$ berada di luar lingkaran $L$, nilai kuasa titik harus lebih dari nol ($K_Q > 0$):
$$
(4 - 1)^2 + (b + 5)^2 - 45 > 0
$$
$$
3^2 + (b + 5)^2 - 45 > 0
$$
$$
9 + (b + 5)^2 - 45 > 0
$$
$$
(b + 5)^2 - 36 > 0
$$
$$
(b + 5)^2 > 36
$$
Maka diperoleh:
$$
b + 5 < -6 \quad \text{atau} \quad b + 5 > 6
$$
$$
b < -11 \quad \text{atau} \quad b > 1
$$
Jadi, batasan nilai $b$ adalah $b < -11$ atau $b > 1$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b01-c-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: jarak terdekat titik ke lingkaran*

Jarak terdekat dari titik $P(9, 12)$ ke lingkaran $L \equiv x^2 + y^2 = 25$ adalah ....

- A. 5 satuan  
  <sub>Salah: Siswa mengira jarak terdekat sama dengan panjang jari-jari lingkaran.</sub>
- **B. 10 satuan** ✅  
  <sub>Benar: Jarak titik $P(9, 12)$ ke pusat $O(0, 0)$ adalah 15 satuan, dikurangi jari-jari lingkaran $r = 5$ satuan, diperoleh jarak terdekat 10 satuan.</sub>
- C. 15 satuan  
  <sub>Salah: Siswa hanya menghitung jarak titik $P$ ke titik pusat lingkaran tanpa mengurangkan dengan jari-jari.</sub>
- D. 20 satuan  
  <sub>Salah: Siswa menghitung jarak terjauh dari titik $P$ ke lingkaran ($OP + r = 15 + 5$).</sub>

**Pembahasan:** Lingkaran $L \equiv x^2 + y^2 = 25$ berpusat di titik $O(0, 0)$ dengan jari-jari:
$$
r = \sqrt{25} = 5
$$
Jarak titik $P(9, 12)$ ke titik pusat $O(0, 0)$ adalah:
$$
OP = \sqrt{(9 - 0)^2 + (12 - 0)^2} = \sqrt{81 + 144} = \sqrt{225} = 15
$$
Karena $OP = 15 > r = 5$, titik $P$ berada di luar lingkaran.
Jarak terdekat dari titik $P$ ke lingkaran dihitung dengan mengurangkan jarak pusat terhadap jari-jari:
$$
d_{\text{terdekat}} = OP - r = 15 - 5 = 10 \text{ satuan}
$$
Jadi, jarak terdekat dari titik $P$ ke lingkaran tersebut adalah 10 satuan.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b01-c-medium-bt01-008
*variasi (angka) | C3 | 2 langkah | jenis: titik potong garis dan lingkaran*

Titik potong antara lingkaran $L \equiv (x - 4)^2 + (y + 1)^2 = 25$ dengan garis $y = 2$ adalah ....

- **A. $(0, 2)$ dan $(8, 2)$** ✅  
  <sub>Benar: Substitusi $y = 2$ ke persamaan lingkaran menghasilkan $(x - 4)^2 + 9 = 25 \iff (x - 4)^2 = 16$, sehingga $x = 0$ atau $x = 8$. Titik potongnya adalah $(0, 2)$ dan $(8, 2)$.</sub>
- B. $(1, 2)$ dan $(9, 2)$  
  <sub>Salah: Siswa mengira pusat absis adalah $x + 4$ sehingga menyelesaikan $x - 5 = \pm 4$.</sub>
- C. $(-1, 2)$ dan $(7, 2)$  
  <sub>Salah: Siswa salah menghitung $(2 + 1)^2$ menjadi $10$ sehingga $(x - 4)^2 = 15$ atau salah operasi penarikan akar.</sub>
- D. $(0, -2)$ dan $(8, -2)$  
  <sub>Salah: Siswa salah memasukkan nilai $y$ pada koordinat titik potong menjadi negatif.</sub>

**Pembahasan:** Substitusikan nilai $y = 2$ ke dalam persamaan lingkaran:
$$(x - 4)^2 + (2 + 1)^2 = 25$$
$$(x - 4)^2 + 3^2 = 25$$
$$(x - 4)^2 + 9 = 25$$
$$(x - 4)^2 = 16$$
$$x - 4 = \pm 4$$

Untuk $x - 4 = -4$, diperoleh $x = 0$.
Untuk $x - 4 = 4$, diperoleh $x = 8$.

Karena nilai $y = 2$, titik potongnya adalah $(0, 2)$ dan $(8, 2)$.
**Acuan:** siswa — siswa hal.62 Contoh Soal 1.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b01-c-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: jarak titik di luar lingkaran ke pusat*

Diketahui titik $B(7, -1)$ berada di luar lingkaran $L \equiv x^2 + y^2 = 25$. Jarak titik $B$ terhadap titik pusat lingkaran $L$ adalah ....

- A. $2\sqrt{5}\text{ satuan}$  
  <sub>Salah: Siswa salah menyederhanakan bentuk akar $\sqrt{50}$ menjadi $\sqrt{20}$.</sub>
- B. $5\text{ satuan}$  
  <sub>Salah: Siswa keliru mengira jarak titik ke pusat sama dengan panjang jari-jari lingkaran.</sub>
- **C. $5\sqrt{2}\text{ satuan}$** ✅  
  <sub>Benar: Pusat lingkaran adalah $O(0, 0)$. Jarak $OB = \sqrt{(7 - 0)^2 + (-1 - 0)^2} = \sqrt{49 + 1} = \sqrt{50} = 5\sqrt{2}\text{ satuan}$.</sub>
- D. $6\sqrt{2}\text{ satuan}$  
  <sub>Salah: Siswa salah menghitung $7^2 + (-1)^2$ menjadi $49 - 1 = 48$ lalu menyederhanakannya keliru.</sub>

**Pembahasan:** Persamaan lingkaran $L \equiv x^2 + y^2 = 25$ memiliki titik pusat di $O(0, 0)$.

Jarak titik $B(7, -1)$ ke titik pusat $O(0, 0)$ ditentukan dengan rumus jarak dua titik:
$$OB = \sqrt{(x_B - x_O)^2 + (y_B - y_O)^2}$$
$$OB = \sqrt{(7 - 0)^2 + (-1 - 0)^2}$$
$$OB = \sqrt{49 + 1} = \sqrt{50} = 5\sqrt{2}$$

Jadi, jarak titik $B$ terhadap titik pusat lingkaran adalah $5\sqrt{2}\text{ satuan}$.
**Acuan:** siswa — siswa hal.58 Contoh Soal 1.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b01-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: nilai parameter dari kuasa titik*

Nilai kuasa titik $P(m, 2)$ terhadap lingkaran $L \equiv x^2 + y^2 - 6x + 4y - 3 = 0$ bernilai $16$. Jika $m$ merupakan bilangan bulat positif, nilai $m$ yang memenuhi adalah ....

- A. $1$  
  <sub>Salah: Siswa mengambil nilai positif dari akar negatif $-1$.</sub>
- B. $5$  
  <sub>Salah: Siswa salah menghitung konstanta menjadi $m^2 - 6m + 5 = 0$ sehingga diperoleh $m = 5$.</sub>
- C. $3$  
  <sub>Salah: Siswa hanya menghitung sumbu simetri $m = -b/(2a) = 6/2 = 3$.</sub>
- **D. $7$** ✅  
  <sub>Benar: Substitusi $P(m, 2)$ ke ekspresi lingkaran menghasilkan $m^2 + 2^2 - 6m + 4(2) - 3 = 16 \iff m^2 - 6m - 7 = 0$. Faktornya $(m - 7)(m + 1) = 0$. Karena $m > 0$, maka $m = 7$.</sub>

**Pembahasan:** Berdasarkan definisi, nilai kuasa titik $P(m, 2)$ diperoleh dengan menyubstitusikan koordinat titik ke persamaan umum lingkaran:
$$K_P = m^2 + 2^2 - 6(m) + 4(2) - 3$$
$$K_P = m^2 + 4 - 6m + 8 - 3$$
$$K_P = m^2 - 6m + 9$$

Diketahui nilai kuasa $K_P = 16$, maka:
$$m^2 - 6m + 9 = 16$$
$$m^2 - 6m - 7 = 0$$
$$(m - 7)(m + 1) = 0$$
$$m = 7 \text{ atau } m = -1$$

Karena disyaratkan $m$ merupakan bilangan bulat positif, nilai yang memenuhi adalah $m = 7$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b01-c-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: garis singgung vertikal lingkaran*

Garis vertikal dengan persamaan $x = c$ menyinggung lingkaran $L \equiv x^2 + y^2 - 8x - 4y + 16 = 0$. Nilai $c$ yang memenuhi adalah ....

- A. $c = 0$ atau $c = 8$  
  <sub>Salah: Siswa salah memasukkan nilai jari-jari menjadi $4$ sehingga $c = 4 \pm 4$.</sub>
- B. $c = -2$ atau $c = -6$  
  <sub>Salah: Siswa salah menentukan tanda saat menyelesaikan $c - 4 = \pm 2$.</sub>
- C. $c = 4$ saja  
  <sub>Salah: Siswa mengira garis singgung melewati titik pusat absis lingkaran.</sub>
- **D. $c = 2$ atau $c = 6$** ✅  
  <sub>Benar: Substitusi $x = c$ menghasilkan $y^2 - 4y + (c^2 - 8c + 16) = 0$. Syarat bersinggungan $D = 0 \iff 16 - 4(c - 4)^2 = 0 \iff (c - 4)^2 = 4$, diperoleh $c = 2$ atau $c = 6$.</sub>

**Pembahasan:** Substitusikan persamaan garis vertikal $x = c$ ke dalam persamaan lingkaran:
$$c^2 + y^2 - 8c - 4y + 16 = 0$$
$$y^2 - 4y + (c^2 - 8c + 16) = 0$$

Persamaan di atas merupakan persamaan kuadrat dalam variabel $y$ dengan:
$$a = 1, \quad b = -4, \quad c_k = c^2 - 8c + 16$$

Syarat garis menyinggung lingkaran adalah diskriminan $D = 0$:
$$D = b^2 - 4ac_k = 0$$
$$(-4)^2 - 4(1)(c^2 - 8c + 16) = 0$$
$$16 - 4(c - 4)^2 = 0$$
$$4(c - 4)^2 = 16$$
$$(c - 4)^2 = 4$$
$$c - 4 = \pm 2$$

Untuk $c - 4 = -2$, diperoleh $c = 2$.
Untuk $c - 4 = 2$, diperoleh $c = 6$.

Jadi, nilai $c$ yang memenuhi adalah $c = 2$ atau $c = 6$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b01-c-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: nilai parameter titik pada lingkaran*

Nilai $m$ yang memenuhi agar titik $P(m, 2m)$ terletak pada lingkaran $L \equiv x^2 + y^2 - 9x + 2y - 30 = 0$ adalah ....

- A. $m = -6$ atau $m = 1$  
  <sub>Salah: Kesalahan memilih pasangan faktor dari konstanta $-6$ pada persamaan kuadrat.</sub>
- **B. $m = -2$ atau $m = 3$** ✅  
  <sub>Benar: Substitusi $x = m$ dan $y = 2m$ ke persamaan lingkaran menghasilkan $m^2 + (2m)^2 - 9(m) + 2(2m) - 30 = 0 \iff 5m^2 - 5m - 30 = 0 \iff m^2 - m - 6 = 0$. Faktorkan menjadi $(m - 3)(m + 2) = 0$, sehingga $m = 3$ atau $m = -2$.</sub>
- C. $m = -3$ atau $m = 2$  
  <sub>Salah: Kesalahan tanda saat menentukan akar-akar dari pemfaktoran $(m - 3)(m + 2) = 0$.</sub>
- D. $m = -1$ atau $m = 6$  
  <sub>Salah: Kesalahan tanda sekaligus memilih pasangan faktor dari konstanta $-6$.</sub>

**Pembahasan:** Agar titik $P(m, 2m)$ terletak pada lingkaran, substitusikan $x = m$ dan $y = 2m$ ke persamaan lingkaran:
$$m^2 + (2m)^2 - 9(m) + 2(2m) - 30 = 0$$
$$m^2 + 4m^2 - 9m + 4m - 30 = 0$$
$$5m^2 - 5m - 30 = 0$$
Bagi kedua ruas dengan 5:
$$m^2 - m - 6 = 0$$
$$(m - 3)(m + 2) = 0$$
Diperoleh $m = 3$ atau $m = -2$.
**Acuan:** siswa — siswa hal.66 Latihan Soal Kedudukan Titik dan Garis terhadap Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b01-c-medium-bt01-013
*variasi (angka) | C3 | 2 langkah | jenis: titik potong garis vertikal dan lingkaran*

Titik potong antara garis vertikal $x = 5$ dengan lingkaran $L \equiv (x - 1)^2 + (y - 4)^2 = 25$ adalah ....

- A. $(1, 5)$ dan $(7, 5)$  
  <sub>Salah: Tertukar antara posisi absis $x$ dan ordinat $y$ pada koordinat titik potong.</sub>
- **B. $(5, 1)$ dan $(5, 7)$** ✅  
  <sub>Benar: Substitusi $x = 5$ ke persamaan lingkaran menghasilkan $(5 - 1)^2 + (y - 4)^2 = 25 \iff 16 + (y - 4)^2 = 25 \iff (y - 4)^2 = 9$. Maka $y - 4 = \pm 3$, sehingga $y = 1$ atau $y = 7$. Titik potongnya $(5, 1)$ dan $(5, 7)$.</sub>
- C. $(5, -7)$ dan $(5, -1)$  
  <sub>Salah: Kesalahan tanda pada kedua nilai ordinat yang diperoleh.</sub>
- D. $(5, -1)$ dan $(5, 7)$  
  <sub>Salah: Kesalahan tanda saat menyelesaikan persamaan $y - 4 = -3$ yang keliru dihitung menjadi $y = -1$.</sub>

**Pembahasan:** Substitusikan nilai $x = 5$ ke dalam persamaan lingkaran:
$$(5 - 1)^2 + (y - 4)^2 = 25$$
$$4^2 + (y - 4)^2 = 25$$
$$16 + (y - 4)^2 = 25$$
$$(y - 4)^2 = 9$$
$$y - 4 = \pm 3$$
Untuk $y - 4 = 3 \implies y = 7$.
Untuk $y - 4 = -3 \implies y = 1$.

Jadi, garis $x = 5$ memotong lingkaran di titik $(5, 1)$ dan $(5, 7)$.
**Acuan:** siswa — siswa hal.62 Contoh Soal 1.18

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b01-c-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: jarak terjauh titik ke lingkaran*

Jarak terjauh dari titik $P(10, 7)$ ke lingkaran $L \equiv (x - 2)^2 + (y - 1)^2 = 36$ adalah ....

- **A. $16\text{ satuan}$** ✅  
  <sub>Benar: Pusat lingkaran $M(2, 1)$ dan jari-jari $r = \sqrt{36} = 6$. Jarak titik $P$ ke pusat adalah $PM = \sqrt{(10 - 2)^2 + (7 - 1)^2} = \sqrt{64 + 36} = 10$. Jarak terjauh adalah $PM + r = 10 + 6 = 16\text{ satuan}$.</sub>
- B. $10\text{ satuan}$  
  <sub>Salah: Hanya menghitung jarak titik $P$ ke titik pusat lingkaran tanpa menambahkan jari-jari.</sub>
- C. $22\text{ satuan}$  
  <sub>Salah: Menambahkan panjang diameter ($2r = 12$) ke jarak titik pusat bukan jari-jari.</sub>
- D. $4\text{ satuan}$  
  <sub>Salah: Menghitung jarak terdekat dari titik ke lingkaran ($PM - r = 10 - 6$).</sub>

**Pembahasan:** Berdasarkan persamaan lingkaran $L \equiv (x - 2)^2 + (y - 1)^2 = 36$:
- Titik pusat lingkaran adalah $M(2, 1)$.
- Jari-jari lingkaran adalah $r = \sqrt{36} = 6$.

Hitung jarak titik $P(10, 7)$ ke pusat lingkaran $M(2, 1)$:
$$PM = \sqrt{(10 - 2)^2 + (7 - 1)^2} = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10$$

Jarak terjauh dari titik $P$ ke lingkaran adalah jarak dari titik $P$ ke pusat lingkaran ditambah jari-jari lingkaran:
$$\text{Jarak terjauh} = PM + r = 10 + 6 = 16\text{ satuan}.$$
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b01-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: garis singgung horizontal lingkaran*

Nilai $m$ yang memenuhi agar garis horizontal $y = m$ menyinggung lingkaran $L \equiv x^2 + y^2 + 6x - 10y + 9 = 0$ adalah ....

- A. $m = -10$ atau $m = 0$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan $-4m(m - 10) = 0$ menjadi $-4m(m + 10) = 0$.</sub>
- B. $m = -5$ atau $m = 5$  
  <sub>Salah: Hanya menggunakan nilai $\pm r$ lingkaran tanpa memperhitungkan pergeseran ordinat pusat.</sub>
- **C. $m = 0$ atau $m = 10$** ✅  
  <sub>Benar: Substitusi $y = m$ menghasilkan $x^2 + 6x + (m^2 - 10m + 9) = 0$. Syarat garis menyinggung adalah $D = 0$, yaitu $6^2 - 4(1)(m^2 - 10m + 9) = 0 \iff -4m^2 + 40m = 0 \iff -4m(m - 10) = 0$, sehingga $m = 0$ atau $m = 10$.</sub>
- D. $m = 5$ atau $m = 15$  
  <sub>Salah: Kesalahan perhitungan diskriminan yang menggeser nilai ordinat ke arah positif.</sub>

**Pembahasan:** Substitusikan $y = m$ ke persamaan lingkaran:
$$x^2 + m^2 + 6x - 10m + 9 = 0$$
$$x^2 + 6x + (m^2 - 10m + 9) = 0$$

Persamaan kuadrat dalam $x$ memiliki koefisien:
$a = 1$, $b = 6$, dan $c = m^2 - 10m + 9$.

Agar garis menyinggung lingkaran, nilai diskriminan $D = 0$:
$$D = b^2 - 4ac = 0$$
$$6^2 - 4(1)(m^2 - 10m + 9) = 0$$
$$36 - 4m^2 + 40m - 36 = 0$$
$$-4m^2 + 40m = 0$$
$$-4m(m - 10) = 0$$
Diperoleh $m = 0$ atau $m = 10$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b01-c-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: batasan absis titik di dalam lingkaran*

Batasan nilai $k$ agar titik $P(k, 6)$ terletak di dalam lingkaran $L \equiv (x - 5)^2 + (y - 2)^2 = 80$ adalah ....

- A. $-8 < k < 8$  
  <sub>Salah: Lupa menambahkan koordinat pusat $x = 5$ pada batas pertidaksamaan.</sub>
- B. $k < -3$ atau $k > 13$  
  <sub>Salah: Menggunakan tanda ketaksamaan untuk titik di luar lingkaran.</sub>
- **C. $-3 < k < 13$** ✅  
  <sub>Benar: Syarat di dalam lingkaran: $(k - 5)^2 + (6 - 2)^2 < 80 \Leftrightarrow (k - 5)^2 + 16 < 80 \Leftrightarrow (k - 5)^2 < 64 \Leftrightarrow -8 < k - 5 < 8 \Leftrightarrow -3 < k < 13$.</sub>
- D. $-13 < k < 3$  
  <sub>Salah: Salah tanda pergeseran absis saat menyelesaikan nilai mutlak $|k - 5| < 8$.</sub>

**Pembahasan:** Agar titik $P(k, 6)$ berada di dalam lingkaran $L \equiv (x - 5)^2 + (y - 2)^2 = 80$, kuasa titik harus bernilai negatif:
$$(k - 5)^2 + (6 - 2)^2 - 80 < 0$$
$$(k - 5)^2 + 16 - 80 < 0$$
$$(k - 5)^2 - 64 < 0$$
$$(k - 5)^2 < 64$$
$$-8 < k - 5 < 8$$
$$-3 < k < 13$$

Jadi, batasan nilai $k$ yang memenuhi adalah $-3 < k < 13$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b01-c-medium-bt01-017
*variasi (angka) | C4 | 3 langkah | jenis: parameter garis singgung lingkaran umum*

Nilai $c$ yang memenuhi agar garis $y = 3x + c$ menyinggung lingkaran $L \equiv x^2 + y^2 - 8x - 6y + 15 = 0$ adalah ....

- A. $c = -10$ atau $c = 10$  
  <sub>Salah: Mengabaikan konstanta pergeseran pusat lingkaran.</sub>
- B. $c = -1$ atau $c = 19$  
  <sub>Salah: Salah memfaktorkan $c^2 + 18c - 19 = 0$ menjadi $(c - 19)(c + 1) = 0$.</sub>
- **C. $c = -19$ atau $c = 1$** ✅  
  <sub>Benar: Substitusi $y = 3x + c$ ke $L$ menghasilkan diskriminan $D = 0$ saat $c^2 + 18c - 19 = 0$, menghasilkan $c = 1$ atau $c = -19$.</sub>
- D. $c = -21$ atau $c = -1$  
  <sub>Salah: Salah menjumlahkan konstanta saat menyusun persamaan kuadrat persekutuan.</sub>

**Pembahasan:** Pusat lingkaran $L$ adalah $\left(-\frac{-8}{2}, -\frac{-6}{2}\right) = (4, 3)$ dengan jari-jari $r = \sqrt{4^2 + 3^2 - 15} = \sqrt{10}$.

Garis $3x - y + c = 0$ menyinggung lingkaran jika jarak pusat ke garis sama dengan $r$:
$$\frac{|3(4) - 3 + c|}{\sqrt{3^2 + (-1)^2}} = \sqrt{10}$$
$$\frac{|9 + c|}{\sqrt{10}} = \sqrt{10}$$
$$|c + 9| = 10$$

Diperoleh dua kemungkinan:
1) $c + 9 = 10 \Rightarrow c = 1$
2) $c + 9 = -10 \Rightarrow c = -19$

Jadi, nilai $c$ yang memenuhi adalah $c = -19$ atau $c = 1$.
**Acuan:** pretest — kelas12_tl-b01-p0067-latihan-soal-kedudukan-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b01-c-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: nilai parameter negatif dari kuasa titik*

Nilai kuasa titik $A(p, 3)$ terhadap lingkaran $L \equiv (x + 2)^2 + (y - 5)^2 = 25$ bernilai $15$. Jika $p$ bilangan real negatif, maka nilai $p$ adalah ....

- **A. $-8$** ✅  
  <sub>Benar: Kuasa titik bernilai 15 memberikan $(p + 2)^2 + (3 - 5)^2 - 25 = 15 \Leftrightarrow (p + 2)^2 = 36$. Nilai negatif adalah $p = -6 - 2 = -8$.</sub>
- B. $-10$  
  <sub>Salah: Salah operasi tanda aljabar saat memindahkan ruas $p + 2 = -6$.</sub>
- C. $-6$  
  <sub>Salah: Lupa memperhitungkan nilai suku konstan $(3 - 5)^2$.</sub>
- D. $4$  
  <sub>Salah: Memilih nilai positif $p = 6 - 2 = 4$ padahal disyaratkan negatif.</sub>

**Pembahasan:** Kuasa titik $A(p, 3)$ terhadap lingkaran $L \equiv (x + 2)^2 + (y - 5)^2 = 25$ dirumuskan dengan:
$$K_A = (p + 2)^2 + (3 - 5)^2 - 25$$

Diketahui $K_A = 15$, maka:
$$(p + 2)^2 + (-2)^2 - 25 = 15$$
$$(p + 2)^2 + 4 - 25 = 15$$
$$(p + 2)^2 - 21 = 15$$
$$(p + 2)^2 = 36$$
$$p + 2 = \pm 6$$

Diperoleh:
- $p + 2 = 6 \Rightarrow p = 4$
- $p + 2 = -6 \Rightarrow p = -8$

Karena disyaratkan $p$ bernilai negatif, maka $p = -8$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b01-c-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: batasan ordinat titik di luar lingkaran*

Batasan nilai $a$ agar titik $P(a, 4)$ terletak di luar lingkaran $L \equiv (x - 2)^2 + (y - 1)^2 = 34$ adalah ....

- **A. $a < -3$ atau $a > 7$** ✅  
  <sub>Benar: Substitusi titik $(a, 4)$ ke persamaan lingkaran menghasilkan $(a - 2)^2 + (4 - 1)^2 > 34$, sehingga $(a - 2)^2 > 25$, yang memberikan $a < -3$ atau $a > 7$.</sub>
- B. $a < -7$ atau $a > 3$  
  <sub>Salah: Salah dalam memindahkan tanda minus pada $(a - 2)$, menganggap solusinya berpusat di $-2$.</sub>
- C. $a < -5$ atau $a > 5$  
  <sub>Salah: Lupa memperhitungkan pergeseran nilai pusat $x = 2$ setelah menarik akar dari $25$.</sub>
- D. $-3 < a < 7$  
  <sub>Salah: Menggunakan tanda ketaksamaan terbalik seolah titik berada di dalam lingkaran.</sub>

**Pembahasan:** Agar titik $P(a, 4)$ berada di luar lingkaran $L$, kuasa titik harus bernilai positif:
$$(a - 2)^2 + (4 - 1)^2 - 34 > 0$$
$$(a - 2)^2 + 3^2 - 34 > 0$$
$$(a - 2)^2 + 9 - 34 > 0$$
$$(a - 2)^2 - 25 > 0$$
$$(a - 2)^2 > 25$$

Selesaikan pertidaksamaan kuadrat:
$$a - 2 < -5 \quad \text{atau} \quad a - 2 > 5$$
$$a < -3 \quad \text{atau} \quad a > 7$$

Jadi, batasan nilai $a$ adalah $a < -3$ atau $a > 7$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b01-c-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: koordinat titik potong garis miring dan lingkaran*

Koordinat titik potong antara garis $g: y = x + 2$ dan lingkaran $L \equiv x^2 + y^2 - 4x - 2y - 4 = 0$ adalah ....

- A. $(-1, -1)$ dan $(2, 2)$  
  <sub>Salah: Lupa menambahkan konstanta $2$ saat mencari nilai $y$, mengira $y = x$.</sub>
- **B. $(-1, 1)$ dan $(2, 4)$** ✅  
  <sub>Benar: Substitusi $y = x + 2$ menghasilkan persamaan $2x^2 - 2x - 4 = 0$ dengan akar $x = -1$ dan $x = 2$, yang menghasilkan titik $(-1, 1)$ dan $(2, 4)$.</sub>
- C. $(-2, 0)$ dan $(1, 3)$  
  <sub>Salah: Menukar tanda akar-akar kuadrat penyelesaian persamaan.</sub>
- D. $(1, 3)$ dan $(-2, 0)$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan kuadrat $(x + 1)(x - 2) = 0$ menjadi $(x - 1)(x + 2) = 0$.</sub>

**Pembahasan:** Substitusikan $y = x + 2$ ke dalam persamaan lingkaran $L$:
$$x^2 + (x + 2)^2 - 4x - 2(x + 2) - 4 = 0$$
$$x^2 + (x^2 + 4x + 4) - 4x - 2x - 4 - 4 = 0$$
$$2x^2 - 2x - 4 = 0$$

Bagi kedua ruas dengan $2$:
$$x^2 - x - 2 = 0$$
$$(x - 2)(x + 1) = 0$$
Diperoleh $x_1 = -1$ atau $x_2 = 2$.

Substitusikan nilai $x$ ke persamaan garis $y = x + 2$:
- Untuk $x = -1$, $y = -1 + 2 = 1 \implies (-1, 1)$.
- Untuk $x = 2$, $y = 2 + 2 = 4 \implies (2, 4)$.

Jadi, titik potong garis $g$ dan lingkaran $L$ adalah $(-1, 1)$ dan $(2, 4)$.
**Acuan:** siswa — siswa hal.64

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b01-c-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: nilai parameter titik pada lingkaran*

Nilai $p$ yang memenuhi agar titik $K(2p, p)$ terletak pada lingkaran $L \equiv (x - 3)^2 + (y + 1)^2 = 25$ adalah ....

- **A. $p = -1$ atau $p = 3$** ✅  
  <sub>Benar: Titik terletak pada lingkaran jika kuasanya bernilai nol: $(2p - 3)^2 + (p + 1)^2 = 25 \iff 4p^2 - 12p + 9 + p^2 + 2p + 1 - 25 = 0 \iff 5p^2 - 10p - 15 = 0 \iff p^2 - 2p - 3 = 0 \iff (p - 3)(p + 1) = 0$, sehingga $p = -1$ atau $p = 3$.</sub>
- B. $p = -3$ atau $p = 5$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan pada suku linear saat menjabarkan $(2p - 3)^2$.</sub>
- C. $p = -1$ saja  
  <sub>Salah: Siswa hanya mengambil satu akar penyelesaian dan mengabaikan nilai positifnya.</sub>
- D. $p = 1$ atau $p = -3$  
  <sub>Salah: Siswa salah menentukan tanda saat pemfaktoran dari $p^2 - 2p - 3 = 0$ menjadi $(p + 3)(p - 1) = 0$.</sub>

**Pembahasan:** Agar titik $K(2p, p)$ terletak pada lingkaran $L$, koordinat titik tersebut harus memenuhi persamaan lingkaran:
$$(2p - 3)^2 + (p + 1)^2 = 25$$
$$(4p^2 - 12p + 9) + (p^2 + 2p + 1) = 25$$
$$5p^2 - 10p + 10 = 25$$
$$5p^2 - 10p - 15 = 0$$
Bagi kedua ruas dengan 5:
$$p^2 - 2p - 3 = 0$$
$$(p - 3)(p + 1) = 0$$
$$p = 3 \quad \text{atau} \quad p = -1$$

Jadi, nilai $p$ yang memenuhi adalah $p = -1$ atau $p = 3$.
**Acuan:** siswa — siswa hal.66 Latihan Soal Kedudukan Titik dan Garis terhadap Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b01-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: batasan parameter titik di dalam lingkaran*

Batasan nilai $k$ agar titik $A(k, k - 1)$ terletak di dalam lingkaran $L \equiv x^2 + y^2 - 8x - 4y + 7 = 0$ adalah ....

- **A. $1 < k < 6$** ✅  
  <sub>Benar: Titik terletak di dalam lingkaran jika nilai kuasa titik bernilai negatif: $k^2 + (k - 1)^2 - 8k - 4(k - 1) + 7 < 0 \iff 2k^2 - 14k + 12 < 0 \iff k^2 - 7k + 6 < 0 \iff (k - 1)(k - 6) < 0$, sehingga $1 < k < 6$.</sub>
- B. $-6 < k < -1$  
  <sub>Salah: Siswa keliru memfaktorkan persamaan kuadrat dengan tanda yang terbalik.</sub>
- C. $k < 1$ atau $k > 6$  
  <sub>Salah: Siswa menggunakan syarat titik di luar lingkaran (kuasa bernilai positif).</sub>
- D. $2 < k < 5$  
  <sub>Salah: Siswa salah menghitung konstanta pada pertidaksamaan sebelum memfaktorkan.</sub>

**Pembahasan:** Titik $A(k, k - 1)$ terletak di dalam lingkaran $L \equiv x^2 + y^2 - 8x - 4y + 7 = 0$ jika kuasa titik bernilai negatif ($K_A < 0$):
$$k^2 + (k - 1)^2 - 8k - 4(k - 1) + 7 < 0$$
$$k^2 + (k^2 - 2k + 1) - 8k - 4k + 4 + 7 < 0$$
$$2k^2 - 14k + 12 < 0$$
Bagi kedua ruas dengan 2:
$$k^2 - 7k + 6 < 0$$
$$(k - 1)(k - 6) < 0$$
$$1 < k < 6$$

Jadi, batasan nilai $k$ adalah $1 < k < 6$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b01-c-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: konstanta persamaan lingkaran bersinggungan*

Garis $g \equiv 3x + 4y - 5 = 0$ menyinggung lingkaran $L \equiv x^2 + y^2 - 2x - 6y + c = 0$. Nilai konstanta $c$ yang memenuhi adalah ....

- A. $4$  
  <sub>Salah: Siswa mengira $c$ adalah kuadrat jari-jari $r^2$ langsung tanpa memperhitungkan koordinat pusat lingkaran.</sub>
- **B. $6$** ✅  
  <sub>Benar: Mengubah garis menjadi $y = \frac{5 - 3x}{4}$ dan substitusi ke lingkaran menghasilkan $25x^2 + 10x + (16c - 95) = 0$. Syarat menyinggung adalah $D = 0$, yaitu $10^2 - 4(25)(16c - 95) = 0 \iff 100 - 100(16c - 95) = 0 \iff 16c - 95 = 1 \iff 16c = 96 \iff c = 6$.</sub>
- C. $-6$  
  <sub>Salah: Siswa salah tanda saat memindahkan konstanta pada $16c - 95 = 1$ menjadi $16c = -96$.</sub>
- D. $10$  
  <sub>Salah: Siswa lupa mengalikan suku $c$ dengan 16 saat menyamakan penyebut pecahan.</sub>

**Pembahasan:** Dari persamaan garis $g$, nyatakan $y$ dalam $x$:
$$3x + 4y - 5 = 0 \implies y = \frac{5 - 3x}{4}$$
Substitusikan ke persamaan lingkaran $L$:
$$x^2 + \left(\frac{5 - 3x}{4}\right)^2 - 2x - 6\left(\frac{5 - 3x}{4}\right) + c = 0$$
Kalikan kedua ruas dengan 16:
$$16x^2 + (25 - 30x + 9x^2) - 32x - 24(5 - 3x) + 16c = 0$$
$$25x^2 - 62x + 25 - 120 + 72x + 16c = 0$$
$$25x^2 + 10x + (16c - 95) = 0$$

Agar garis menyinggung lingkaran, nilai diskriminan $D = 0$:
$$b^2 - 4ac = 0$$
$$10^2 - 4(25)(16c - 95) = 0$$
$$100 - 100(16c - 95) = 0$$
Bagi kedua ruas dengan 100:
$$1 - (16c - 95) = 0$$
$$16c - 95 = 1$$
$$16c = 96$$
$$c = 6$$

Jadi, nilai konstanta $c$ yang memenuhi adalah $6$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b01-c-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: syarat parameter gradien garis memotong lingkaran*

Batasan nilai gradien $m$ agar garis $y = mx + 10$ memotong lingkaran $L \equiv x^2 + y^2 = 20$ di dua titik yang berlainan adalah ....

- A. $-2 < m < 2$  
  <sub>Salah: Siswa menggunakan syarat garis tidak memotong lingkaran ($D < 0$).</sub>
- B. $m \le -2$ atau $m \ge 2$  
  <sub>Salah: Siswa menyertakan kondisi garis menyinggung ($D \ge 0$) padahal disyaratkan memotong di dua titik berlainan.</sub>
- C. $m < -4$ atau $m > 4$  
  <sub>Salah: Siswa salah saat menyederhanakan $80m^2 - 320 > 0$ menjadi $m^2 > 16$.</sub>
- **D. $m < -2$ atau $m > 2$** ✅  
  <sub>Benar: Substitusi $y = mx + 10$ ke $x^2 + y^2 = 20$ menghasilkan $(1 + m^2)x^2 + 20mx + 80 = 0$. Syarat memotong di dua titik berlainan adalah $D > 0$, yaitu $(20m)^2 - 4(1 + m^2)(80) > 0 \iff 400m^2 - 320 - 320m^2 > 0 \iff 80m^2 - 320 > 0 \iff m^2 > 4$, sehingga $m < -2$ atau $m > 2$.</sub>

**Pembahasan:** Substitusikan $y = mx + 10$ ke dalam persamaan lingkaran $x^2 + y^2 = 20$:
$$x^2 + (mx + 10)^2 = 20$$
$$x^2 + m^2x^2 + 20mx + 100 - 20 = 0$$
$$(1 + m^2)x^2 + 20mx + 80 = 0$$

Syarat garis memotong lingkaran di dua titik yang berlainan adalah nilai diskriminan $D > 0$:
$$D = b^2 - 4ac > 0$$
$$(20m)^2 - 4(1 + m^2)(80) > 0$$
$$400m^2 - 320(1 + m^2) > 0$$
$$400m^2 - 320 - 320m^2 > 0$$
$$80m^2 - 320 > 0$$
Bagi kedua ruas dengan 80:
$$m^2 - 4 > 0$$
$$(m - 2)(m + 2) > 0$$
$$m < -2 \quad \text{atau} \quad m > 2$$

Jadi, batasan nilai $m$ yang memenuhi adalah $m < -2$ atau $m > 2$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b01-c-hard-bt01-005
*variasi (angka) | C5 | 3 langkah | jenis: penentuan parameter titik pada lingkaran*

Nilai $t$ yang memenuhi agar titik $P(t, 2t)$ terletak pada lingkaran $L \equiv x^2 + y^2 - 6x - 2y - 15 = 0$ adalah ....

- **A. $t = -1$ atau $t = 3$** ✅  
  <sub>Benar: Substitusi koordinat $(t, 2t)$ menghasilkan $t^2 + (2t)^2 - 6t - 2(2t) - 15 = 0 \iff 5t^2 - 10t - 15 = 0 \iff t^2 - 2t - 3 = 0$. Pemfaktoran $(t - 3)(t + 1) = 0$ memberikan $t = -1$ atau $t = 3$.</sub>
- B. $t = 1$ atau $t = -3$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan kuadrat, menuliskan $(t + 3)(t - 1) = 0$ bukannya $(t - 3)(t + 1) = 0$.</sub>
- C. $t = -1$ atau $t = 5$  
  <sub>Salah: Kesalahan menjumlahkan suku linear $-6t - 4t$ menjadi $-6t$ sehingga menghasilkan pemfaktoran yang keliru.</sub>
- D. $t = 1$ atau $t = 3$  
  <sub>Salah: Kesalahan mengabaikan tanda negatif pada salah satu akar saat menentukan pembuat nol.</sub>

**Pembahasan:** Agar titik $P(t, 2t)$ terletak pada lingkaran $L$, nilai kuasa titik tersebut harus bernilai nol (memenuhi persamaan lingkaran).

Substitusikan $x = t$ dan $y = 2t$ ke dalam persamaan lingkaran:
$$(t)^2 + (2t)^2 - 6(t) - 2(2t) - 15 = 0$$
$$t^2 + 4t^2 - 6t - 4t - 15 = 0$$
$$5t^2 - 10t - 15 = 0$$

Bagi kedua ruas dengan $5$:
$$t^2 - 2t - 3 = 0$$
$$(t - 3)(t + 1) = 0$$

Diperoleh $t - 3 = 0 \implies t = 3$ atau $t + 1 = 0 \implies t = -1$.
Jadi, nilai $t$ yang memenuhi adalah $t = -1$ atau $t = 3$.
**Acuan:** siswa — siswa hal.66 Latihan Soal Kedudukan Titik dan Garis terhadap Lingkaran

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b01-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: koordinat titik tengah tali busur lingkaran*

Garis $g \equiv y = x + c$ memotong lingkaran $L \equiv x^2 + y^2 = 25$ di dua titik berbeda, yaitu $A$ dan $B$. Jika titik tengah ruas garis $AB$ memiliki absis $-1$, maka nilai $c$ yang memenuhi adalah ....

- **A. $2$** ✅  
  <sub>Benar: Substitusi $y = x + c$ ke lingkaran menghasilkan $2x^2 + 2cx + c^2 - 25 = 0$. Absis titik tengah adalah $\frac{x_1 + x_2}{2} = \frac{-2c/2}{2} = -\frac{c}{2}$. Diketahui $-\frac{c}{2} = -1$, sehingga $c = 2$.</sub>
- B. $-1$  
  <sub>Salah: Kekeliruan menganggap absis titik tengah langsung bernilai sama dengan konstanta $-c$.</sub>
- C. $-2$  
  <sub>Salah: Kesalahan tanda negatif pada rumus jumlah akar Teorema Vieta $-\frac{b}{a}$.</sub>
- D. $1$  
  <sub>Salah: Kesalahan siswa lupa membagi dengan 2 saat menghitung titik tengah dari jumlah absis akar-akar.</sub>

**Pembahasan:** Langkah 1: Substitusikan persamaan garis $y = x + c$ ke persamaan lingkaran $L$:
$$x^2 + (x + c)^2 = 25$$
$$x^2 + x^2 + 2cx + c^2 - 25 = 0$$
$$2x^2 + 2cx + (c^2 - 25) = 0$$

Langkah 2: Misalkan absis titik potong $A$ dan $B$ berturut-turut adalah $x_1$ dan $x_2$. Berdasarkan hubungan akar-akar persamaan kuadrat (Teorema Vieta):
$$x_1 + x_2 = -\frac{b}{a} = -\frac{2c}{2} = -c$$

Langkah 3: Absis dari titik tengah ruas garis $AB$ dirumuskan oleh:
$$x_m = \frac{x_1 + x_2}{2} = -\frac{c}{2}$$

Langkah 4: Diketahui bahwa absis titik tengah tersebut adalah $-1$, maka:
$$-\frac{c}{2} = -1 \implies c = 2$$

Untuk $c = 2$, nilai diskriminan $D = (2(2))^2 - 4(2)(2^2 - 25) = 16 - 8(-21) = 184 > 0$, sehingga benar memotong di dua titik berlainan.
Jadi, nilai $c$ yang memenuhi adalah $2$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b01-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: gradien garis menyinggung lingkaran*

Diketahui garis $g$ melalui titik asal $(0, 0)$ dengan persamaan $y = mx$, di mana $m > 0$. Jika garis $g$ menyinggung lingkaran $L \equiv (x - 4)^2 + y^2 = 4$, maka nilai $m$ adalah ....

- A. $\frac{1}{2}\sqrt{3}$  
  <sub>Salah: Keliru memfaktorkan persamaan kuadrat atau tertukar dengan nilai sudut istimewa trigonometri $\sin 60^\circ$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Kesalahan pada perhitungan diskriminan, mengabaikan perkalian dengan konstanta 12.</sub>
- **C. $\frac{1}{3}\sqrt{3}$** ✅  
  <sub>Benar: Substitusi $y = mx$ menghasilkan $(1 + m^2)x^2 - 8x + 12 = 0$. Syarat menyinggung $D = 0 \iff (-8)^2 - 4(1 + m^2)(12) = 0 \iff 64 - 48(1 + m^2) = 0 \iff 48m^2 = 16 \iff m = \frac{1}{\sqrt{3}} = \frac{1}{3}\sqrt{3}$.</sub>
- D. $\sqrt{3}$  
  <sub>Salah: Kesalahan saat membagi, menghitung $m^2 = \frac{48}{16} = 3$ bukannya $\frac{16}{48} = \frac{1}{3}$.</sub>

**Pembahasan:** Langkah 1: Substitusikan persamaan garis $y = mx$ ke dalam persamaan lingkaran $L$:
$$(x - 4)^2 + (mx)^2 = 4$$
$$x^2 - 8x + 16 + m^2 x^2 - 4 = 0$$
$$(1 + m^2)x^2 - 8x + 12 = 0$$

Langkah 2: Tentukan koefisien persamaan kuadrat persekutuan:
$$a = 1 + m^2, \quad b = -8, \quad c = 12$$

Langkah 3: Syarat garis menyinggung lingkaran adalah nilai diskriminan sama dengan nol ($D = 0$):
$$D = b^2 - 4ac = 0$$
$$(-8)^2 - 4(1 + m^2)(12) = 0$$
$$64 - 48(1 + m^2) = 0$$
$$64 - 48 - 48m^2 = 0$$
$$16 - 48m^2 = 0$$

Langkah 4: Selesaikan nilai $m$:
$$48m^2 = 16$$
$$m^2 = \frac{16}{48} = \frac{1}{3}$$

Karena disyaratkan $m > 0$, maka:
$$m = \sqrt{\frac{1}{3}} = \frac{1}{\sqrt{3}} = \frac{1}{3}\sqrt{3}$$

Jadi, nilai $m$ yang memenuhi adalah $\frac{1}{3}\sqrt{3}$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b01-c-hard-bt01-008
*variasi (angka) | C5 | 3 langkah | jenis: batasan parameter titik di luar lingkaran*

Batasan nilai $b$ agar titik $P(2, b)$ terletak di luar lingkaran $L \equiv (x - 5)^2 + (y + 1)^2 = 25$ adalah ....

- A. $-5 < b < 3$  
  <sub>Salah: Siswa salah menggunakan syarat untuk titik yang berada di dalam lingkaran ($K_P < 0$).</sub>
- B. $b < -4$ atau $b > 4$  
  <sub>Salah: Siswa lupa memperhitungkan pergeseran $+1$ pada $(b + 1)$ dan langsung mengambil akar dari $16$.</sub>
- **C. $b < -5$ atau $b > 3$** ✅  
  <sub>Benar: Substitusi koordinat titik $P(2, b)$ ke persamaan lingkaran dengan syarat terletak di luar lingkaran ($K_P > 0$): $(2 - 5)^2 + (b + 1)^2 - 25 > 0 \iff 9 + (b + 1)^2 - 25 > 0 \iff (b + 1)^2 > 16$. Maka $b + 1 < -4$ atau $b + 1 > 4$, sehingga $b < -5$ atau $b > 3$.</sub>
- D. $b < -3$ atau $b > 5$  
  <sub>Salah: Siswa salah menjabarkan $(b - 1)^2 > 16$ karena keliru tanda pada ordinat pusat lingkaran.</sub>

**Pembahasan:** Syarat suatu titik berada di luar lingkaran adalah nilai kuasanya lebih dari 0 ($K > 0$):
$(x_1 - 5)^2 + (y_1 + 1)^2 > 25$
Substitusikan titik $P(2, b)$:
$(2 - 5)^2 + (b + 1)^2 > 25$
$(-3)^2 + (b + 1)^2 > 25$
$9 + (b + 1)^2 > 25$
$(b + 1)^2 > 16$
$|b + 1| > 4$
$b + 1 < -4 \quad \text{atau} \quad b + 1 > 4$
$b < -5 \quad \text{atau} \quad b > 3$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b01-c-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: panjang tali busur persekutuan lingkaran*

Garis $g \equiv y = x + k$ memotong lingkaran $L \equiv x^2 + y^2 = 25$ di dua titik berbeda, yaitu $A$ dan $B$. Jika panjang ruas garis $AB$ adalah $6$ satuan, maka nilai dari $k^2$ adalah ....

- A. 16  
  <sub>Salah: Siswa menghitung $k^2 = d^2 = 16$ tanpa mengalikan dengan penyebut $\sqrt{2}^2$ dari rumus jarak garis ke titik.</sub>
- B. 64  
  <sub>Salah: Siswa salah mengalikan kuadrat jarak dengan faktor $4$ bukan $2$.</sub>
- C. 18  
  <sub>Salah: Siswa keliru menggunakan panjang tali busur penuh sebagai apotema atau salah menerapkan rumus Pythagoras.</sub>
- **D. 32** ✅  
  <sub>Benar: Jari-jari lingkaran $r = 5$. Panjang tali busur $AB = 6$, sehingga setengah tali busur adalah $3$. Jarak titik pusat $(0,0)$ ke garis $x - y + k = 0$ memenuhi rumus apotema $d = \sqrt{r^2 - 3^2} = \sqrt{25 - 9} = 4$. Jarak titik pusat ke garis adalah $d = \frac{|0 - 0 + k|}{\sqrt{1^2 + (-1)^2}} = \frac{|k|}{\sqrt{2}}$. Dengan demikian, $\frac{|k|}{\sqrt{2}} = 4 \iff |k| = 4\sqrt{2} \iff k^2 = 32$.</sub>

**Pembahasan:** Lingkaran $L \equiv x^2 + y^2 = 25$ memiliki pusat $O(0, 0)$ dan jari-jari $r = 5$.
Jika tali busur $AB$ berjarak $d$ dari pusat $O$, maka segitiga yang dibentuk oleh pusat dan tali busur adalah segitiga sama kaki dengan alas $AB = 6$.
Setengah panjang tali busur $= 3$.
Berdasarkan teorema Pythagoras:
$d = \sqrt{r^2 - 3^2} = \sqrt{5^2 - 3^2} = \sqrt{16} = 4$.

Persamaan garis $g$ diubah ke bentuk implisit: $x - y + k = 0$.
Jarak dari pusat $O(0, 0)$ ke garis $g$ adalah:
$d = \frac{|1(0) - 1(0) + k|}{\sqrt{1^2 + (-1)^2}} = \frac{|k|}{\sqrt{2}}$

Karena $d = 4$, diperoleh:
$\frac{|k|}{\sqrt{2}} = 4 \implies |k| = 4\sqrt{2}$
$k^2 = (4\sqrt{2})^2 = 32$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b01-c-hard-bt01-010
*orisinal | C5 | 5 langkah | jenis: hasil kali nilai konstanta garis menyinggung*

Diketahui garis $g \equiv y = 2x + c$ dan lingkaran $L \equiv (x - 1)^2 + (y - 3)^2 = 5$. Jika garis $g$ menyinggung lingkaran $L$, maka hasil kali semua nilai konstanta $c$ yang memenuhi adalah ....

- A. $-20$  
  <sub>Salah: Siswa salah saat mengalikan suku konstanta persamaan kuadratik sehingga konstanta akhir menjadi $-20$.</sub>
- B. $-12$  
  <sub>Salah: Siswa salah menghitung diskriminan dengan membagi koefisien tanpa menguadratkannya.</sub>
- C. 24  
  <sub>Salah: Siswa keliru tanda pada perkalian akar-akar persamaan kuadrat parameter.</sub>
- **D. $-24$** ✅  
  <sub>Benar: Substitusikan $y = 2x + c$ ke lingkaran: $(x - 1)^2 + (2x + c - 3)^2 = 5 \iff 5x^2 + (4c - 14)x + (c^2 - 6c + 4) = 0$. Syarat garis menyinggung adalah $D = 0$: $(4c - 14)^2 - 4(5)(c^2 - 6c + 4) = 0 \iff 4(2c - 7)^2 - 20(c^2 - 6c + 4) = 0 \iff (4c^2 - 28c + 49) - 5(c^2 - 6c + 4) = 0 \iff -c^2 + 2c + 29$? Mari hitung cermat: $(c-3)^2 - 5 = c^2 - 6c + 4$. Tapi $1 + (c-3)^2 - 5 = (c-3)^2 - 4 = c^2 - 6c + 5$. Diperoleh $-c^2 + 2c + 24 = 0 \iff c^2 - 2c - 24 = 0$. Nilai $c$ yang memenuhi adalah $c = 6$ atau $c = -4$. Hasil kali akar-akarnya adalah $c_1 \cdot c_2 = -24$.</sub>

**Pembahasan:** Substitusikan $y = 2x + c$ ke dalam persamaan lingkaran $L$:
$(x - 1)^2 + ((2x + c) - 3)^2 = 5$
$(x - 1)^2 + (2x + (c - 3))^2 = 5$
$x^2 - 2x + 1 + 4x^2 + 4(c - 3)x + (c - 3)^2 = 5$
$5x^2 + (4c - 14)x + ((c - 3)^2 - 4) = 0$
$5x^2 + (4c - 14)x + (c^2 - 6c + 5) = 0$

Garis menyinggung lingkaran jika $D = 0$:
$D = b^2 - 4ac = 0$
$(4c - 14)^2 - 4(5)(c^2 - 6c + 5) = 0$
$4(2c - 7)^2 - 20(c^2 - 6c + 5) = 0$
Bagi kedua ruas dengan 4:
$(2c - 7)^2 - 5(c^2 - 6c + 5) = 0$
$(4c^2 - 28c + 49) - (5c^2 - 30c + 25) = 0$
$-c^2 + 2c + 24 = 0$
$c^2 - 2c - 24 = 0$

Berdasarkan sifat perkalian akar-akar persamaan kuadrat $c_1 \cdot c_2 = \frac{C}{A}$:
$c_1 \cdot c_2 = \frac{-24}{1} = -24$.
**Acuan:** siswa — siswa hal.61

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b01-c-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: jarak terdekat titik luar ke lingkaran*

Titik $P(a, 8)$ dengan $a > 0$ terletak di luar lingkaran $L \equiv x^2 + y^2 - 4x - 6y - 12 = 0$. Jika jarak terdekat dari titik $P$ ke lingkaran $L$ adalah $8$ satuan, maka nilai $a$ adalah ....

- A. 16  
  <sub>Salah: Siswa salah menghitung jari-jari lingkaran menjadi $r = 3$ sehingga jarak pusat ke titik menjadi $11$ dan salah menghitung Pythagoras.</sub>
- B. 10  
  <sub>Salah: Siswa langsung menyamakan jarak $PM$ dengan jarak terdekat ($8$ satuan) tanpa menambahkan jari-jari lingkaran.</sub>
- C. 12  
  <sub>Salah: Siswa memperoleh $a - 2 = 12$ tetapi lupa menambahkan 2 untuk memperoleh nilai $a$.</sub>
- **D. 14** ✅  
  <sub>Benar: Pusat lingkaran adalah $M(2, 3)$ dan jari-jarinya $r = \sqrt{2^2 + 3^2 - (-12)} = \sqrt{4 + 9 + 12} = 5$. Jarak terdekat dari titik di luar lingkaran ke lingkaran adalah $d_{\text{terdekat}} = PM - r$. Diketahui $PM - 5 = 8$, sehingga jarak $PM = 13$. Rumus jarak dua titik: $(a - 2)^2 + (8 - 3)^2 = 13^2 \iff (a - 2)^2 + 25 = 169 \iff (a - 2)^2 = 144$. Karena $a > 0$, maka $a - 2 = 12 \iff a = 14$.</sub>

**Pembahasan:** Ubah persamaan lingkaran ke bentuk baku untuk memperoleh pusat dan jari-jari:
$x^2 + y^2 - 4x - 6y - 12 = 0$
$(x - 2)^2 + (y - 3)^2 - 4 - 9 - 12 = 0$
$(x - 2)^2 + (y - 3)^2 = 25$
Titik pusat lingkaran adalah $M(2, 3)$ dan jari-jari $r = \sqrt{25} = 5$.

Untuk titik $P$ di luar lingkaran, jarak terdekat titik $P$ ke keliling lingkaran dirumuskan:
$d_{\text{terdekat}} = PM - r$
$8 = PM - 5$
$PM = 13$

Gunakan rumus jarak antara titik $P(a, 8)$ dan titik pusat $M(2, 3)$:
$PM^2 = (a - 2)^2 + (8 - 3)^2$
$13^2 = (a - 2)^2 + 5^2$
$169 = (a - 2)^2 + 25$
$(a - 2)^2 = 144$
$a - 2 = 12 \quad \text{atau} \quad a - 2 = -12$
$a = 14 \quad \text{atau} \quad a = -10$

Karena disyaratkan $a > 0$, nilai $a$ yang memenuhi adalah $14$.
**Acuan:** siswa — siswa hal.58

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b01-c-hard-bt01-012
*variasi (angka) | C5 | 3 langkah | jenis: batasan parameter ordinat titik di dalam lingkaran*

Batasan nilai $k$ agar titik $P(5, k)$ terletak di dalam lingkaran $L \equiv (x + 3)^2 + (y - 2)^2 = 100$ adalah ....

- A. $-2 < k < 10$  
  <sub>Salah: Keliru menggunakan batas simpangan 6 menjadi 4 pada operasi aljabar.</sub>
- **B. $-4 < k < 8$** ✅  
  <sub>Benar: Titik berada di dalam lingkaran jika nilai kuasa titik bernilai negatif: $(5 + 3)^2 + (k - 2)^2 - 100 < 0 \Leftrightarrow 64 + (k - 2)^2 - 100 < 0 \Leftrightarrow (k - 2)^2 < 36$, sehingga $-6 < k - 2 < 6 \Leftrightarrow -4 < k < 8$.</sub>
- C. $-8 < k < 4$  
  <sub>Salah: Kesalahan tanda saat menambahkan 2 pada pertidaksamaan $-6 < k - 2 < 6$ (malah dikurangi 2).</sub>
- D. $k < -4$ atau $k > 8$  
  <sub>Salah: Menggunakan pertidaksamaan untuk titik di luar lingkaran ($K > 0$).</sub>

**Pembahasan:** Syarat titik $P(5, k)$ terletak di dalam lingkaran $L \equiv (x + 3)^2 + (y - 2)^2 = 100$ adalah nilai kuasanya negatif ($K_P < 0$):
$$(5 + 3)^2 + (k - 2)^2 < 100$$
$$8^2 + (k - 2)^2 < 100$$
$$64 + (k - 2)^2 < 100$$
$$(k - 2)^2 < 36$$
$$-6 < k - 2 < 6$$
$$-6 + 2 < k < 6 + 2$$
$$-4 < k < 8$$

Jadi, batasan nilai $k$ adalah $-4 < k < 8$.
**Acuan:** pretest — kelas12_tl-b01-p0066-latihan-soal-kedudukan-2a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b01-c-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: luas segitiga dari titik potong tali busur lingkaran*

Garis vertikal $x = 4$ memotong lingkaran $L \equiv x^2 + y^2 - 2x - 4y - 20 = 0$ di dua titik, yaitu titik $A$ dan $B$. Jika titik $P$ adalah titik pusat lingkaran $L$, maka luas segitiga $PAB$ adalah ....

- A. $6\text{ satuan luas}$  
  <sub>Salah: Keliru menggunakan setengah panjang tali busur sebagai alas segitiga ($\frac{1}{2} \times 4 \times 3 = 6$).</sub>
- B. $16\text{ satuan luas}$  
  <sub>Salah: Menggunakan nilai absis titik potong $x = 4$ sebagai tinggi segitiga (bukan selisih $4 - 1 = 3$), sehingga $\frac{1}{2} \times 8 \times 4 = 16$.</sub>
- **C. $12\text{ satuan luas}$** ✅  
  <sub>Benar: Pusat lingkaran adalah $P(1, 2)$. Substitusi $x = 4$ ke lingkaran menghasilkan titik potong $A(4, 6)$ dan $B(4, -2)$, sehingga panjang alas $AB = 8$. Tinggi segitiga adalah jarak horizontal dari $P(1, 2)$ ke garis $x = 4$, yaitu $4 - 1 = 3$. Luas segitiga $PAB = \frac{1}{2} \times 8 \times 3 = 12\text{ satuan luas}$.</sub>
- D. $24\text{ satuan luas}$  
  <sub>Salah: Lupa membagi 2 pada rumus luas segitiga ($8 \times 3 = 24$).</sub>

**Pembahasan:** Langkah 1: Menentukan pusat lingkaran $L$.
$$x^2 + y^2 - 2x - 4y - 20 = 0$$
$$(x - 1)^2 + (y - 2)^2 - 1 - 4 - 20 = 0$$
$$(x - 1)^2 + (y - 2)^2 = 25$$
Pusat lingkaran adalah $P(1, 2)$ dan jari-jari $r = 5$.

Langkah 2: Menentukan koordinat titik potong $A$ dan $B$.
Substitusikan $x = 4$ ke persamaan lingkaran:
$$(4 - 1)^2 + (y - 2)^2 = 25$$
$$3^2 + (y - 2)^2 = 25$$
$$9 + (y - 2)^2 = 25$$
$$(y - 2)^2 = 16$$
$$y - 2 = \pm 4$$
$$y_1 = 6 \quad \text{atau} \quad y_2 = -2$$
Diperoleh titik potong $A(4, 6)$ dan $B(4, -2)$.

Langkah 3: Menghitung panjang alas $AB$ dan tinggi segitiga terhadap alas $AB$.
Karena kedua titik memiliki absis yang sama ($x = 4$), panjang tali busur $AB$ adalah:
$$AB = |6 - (-2)| = 8$$
Tinggi segitiga adalah jarak titik pusat $P(1, 2)$ ke garis $x = 4$:
$$t = |4 - 1| = 3$$

Langkah 4: Menghitung luas segitiga $PAB$.
$$\text{Luas } \triangle PAB = \frac{1}{2} \times AB \times t = \frac{1}{2} \times 8 \times 3 = 12\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.62

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b01-c-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: analisis parameter kedudukan garis terhadap lingkaran*

Diberikan lingkaran $L \equiv x^2 + y^2 - 4x - 10y + 4 = 0$. Garis $g$ melalui titik $P(k, 1)$ dengan kemiringan $m$. Agar garis $g$ selalu memotong lingkaran $L$ di dua titik berlainan untuk setiap nilai real $m$, maka batasan nilai $k$ yang memenuhi adalah ....

- A. $-5 < k < 1$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan pertidaksamaan kuadrat menjadi $(k + 5)(k - 1) < 0$.</sub>
- B. $k < -5$ atau $k > 1$  
  <sub>Salah: Kombinasi kesalahan tanda pemfaktoran dan menganggap titik harus berada di luar lingkaran.</sub>
- C. $k < -1$ atau $k > 5$  
  <sub>Salah: Salah mengartikan kondisi dengan menganggap titik $P$ harus berada di luar lingkaran ($K_P > 0$).</sub>
- **D. $-1 < k < 5$** ✅  
  <sub>Benar: Garis melalui titik $P$ selalu memotong lingkaran di dua titik berbeda untuk setiap gradien $m$ jika dan hanya jika titik $P(k, 1)$ terletak di dalam lingkaran. Syarat di dalam lingkaran: $k^2 + 1^2 - 4k - 10(1) + 4 < 0 \iff k^2 - 4k - 5 < 0 \iff -1 < k < 5$.</sub>

**Pembahasan:** Garis yang melalui sebuah titik $P$ akan memotong lingkaran di dua titik yang berbeda untuk SETIAP kemungkinan nilai kemiringan (gradien) $m$ jika dan hanya jika titik $P(k, 1)$ terletak di bagian dalam lingkaran. Apabila titik $P$ terletak pada atau di luar lingkaran, terdapat garis singgung atau garis yang tidak memotong lingkaran.

Syarat titik $P(k, 1)$ terletak di dalam lingkaran $L \equiv x^2 + y^2 - 4x - 10y + 4 = 0$ adalah nilai kuasanya bernilai negatif:
$$k^2 + (1)^2 - 4(k) - 10(1) + 4 < 0$$
$$k^2 + 1 - 4k - 10 + 4 < 0$$
$$k^2 - 4k - 5 < 0$$
Faktorkan bentuk kuadrat tersebut:
$$(k - 5)(k + 1) < 0$$
Pembuat nol adalah $k = 5$ dan $k = -1$. Karena tanda pertidaksamaan $<$, daerah penyelesaiannya adalah:
$$-1 < k < 5$$
Jadi, batasan nilai $k$ yang memenuhi adalah $-1 < k < 5$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b01-c-hard-bt01-015
*variasi (angka) | C5 | 4 langkah | jenis: penentuan parameter garis tidak berpotongan*

Diketahui garis $g: y = mx - 4$ dan lingkaran $L \equiv (x - 3)^2 + y^2 = 5$. Syarat nilai $m$ agar garis $g$ tidak memotong dan tidak menyinggung lingkaran $L$ adalah ....

- A. $m < -\frac{11}{2}$ atau $m > -\frac{1}{2}$  
  <sub>Salah: Siswa keliru dalam menentukan tanda akar-akar pembuat nol dari pemfaktoran bentuk kuadrat.</sub>
- **B. $m < \frac{1}{2}$ atau $m > \frac{11}{2}$** ✅  
  <sub>Benar: Substitusi $y = mx - 4$ ke persamaan lingkaran menghasilkan $(m^2 + 1)x^2 - 2(4m + 3)x + 20 = 0$. Syarat tidak memotong dan tidak menyinggung adalah $D < 0$, yang menghasilkan $4m^2 - 24m + 11 > 0$, sehingga $m < \frac{1}{2}$ atau $m > \frac{11}{2}$.</sub>
- C. $\frac{1}{2} < m < \frac{11}{2}$  
  <sub>Salah: Siswa salah menerapkan syarat diskriminan dengan menggunakan $D > 0$ atau keliru menentukan arah daerah penyelesaian pertidaksamaan kuadrat.</sub>
- D. $-\frac{11}{2} < m < -\frac{1}{2}$  
  <sub>Salah: Siswa salah dalam memfaktorkan persamaan kuadrat sekaligus terbalik dalam menentukan interval penyelesaian pertidaksamaan.</sub>

**Pembahasan:** Substitusikan persamaan garis $y = mx - 4$ ke persamaan lingkaran $L \equiv (x - 3)^2 + y^2 = 5$:
$$(x - 3)^2 + (mx - 4)^2 = 5$$
$$x^2 - 6x + 9 + m^2x^2 - 8mx + 16 - 5 = 0$$
$$(m^2 + 1)x^2 - 2(4m + 3)x + 20 = 0$$

Agar garis $g$ tidak memotong dan tidak menyinggung lingkaran $L$, nilai diskriminan persamaan kuadrat tersebut harus negatif ($D < 0$):
$$\frac{D}{4} = [-(4m + 3)]^2 - (m^2 + 1)(20) < 0$$
$$16m^2 + 24m + 9 - 20m^2 - 20 < 0$$
$$-4m^2 + 24m - 11 < 0$$
$$4m^2 - 24m + 11 > 0$$
$$(2m - 1)(2m - 11) > 0$$

Pembuat nol adalah $m = \frac{1}{2}$ atau $m = \frac{11}{2}$.
Karena tanda pertidaksamaan adalah $> 0$, himpunan penyelesaiannya adalah $m < \frac{1}{2}$ atau $m > \frac{11}{2}$.
**Acuan:** siswa — siswa hal.65 Ayo Mencoba 1.9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b01-c-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: evaluasi kedudukan titik interior garis sekan*

Diberikan lingkaran $L \equiv (x - 4)^2 + (y - 2)^2 = 25$. Titik $P(a, 5)$ memiliki sifat bahwa setiap garis lurus yang ditarik melalui titik $P$ selalu memotong lingkaran $L$ di dua titik berlainan. Batasan nilai $a$ yang memenuhi kondisi tersebut adalah ....

- **A. $0 < a < 8$** ✅  
  <sub>Benar: Setiap garis yang melalui titik $P$ selalu memotong lingkaran di dua titik berlainan jika dan hanya jika titik $P$ terletak di dalam lingkaran, sehingga nilai kuasa titik $P$ harus negatif: $(a - 4)^2 + (5 - 2)^2 - 25 < 0 \iff (a - 4)^2 < 16 \iff 0 < a < 8$.</sub>
- B. $-8 < a < 0$  
  <sub>Salah: Siswa salah dalam menggeser nilai absis titik pusat saat menyelesaikan pertidaksamaan nilai mutlak $|a - 4| < 4$.</sub>
- C. $a < 0$ atau $a > 8$  
  <sub>Salah: Siswa keliru menganggap titik harus berada di luar lingkaran agar memotong di dua titik ($K > 0$).</sub>
- D. $-4 < a < 4$  
  <sub>Salah: Siswa lupa memperhitungkan absis titik pusat lingkaran dan hanya menyelesaikan pertidaksamaan $a^2 < 16$.</sub>

**Pembahasan:** Secara geometris, sebuah garis lurus yang melalui titik $P$ akan memotong lingkaran di dua titik berlainan untuk segala arah kemiringan jika dan hanya jika titik $P$ berada di dalam lingkaran $L$. Jika titik $P$ berada pada lingkaran, terdapat satu garis singgung (memotong di satu titik). Jika titik $P$ berada di luar lingkaran, terdapat dua garis singgung dan tak terhingga garis yang tidak memotong lingkaran.

Syarat titik $P(a, 5)$ terletak di dalam lingkaran $L$ adalah nilai kuasa titik bernilai negatif ($K_P < 0$):
$$(a - 4)^2 + (5 - 2)^2 - 25 < 0$$
$$(a - 4)^2 + 3^2 - 25 < 0$$
$$(a - 4)^2 + 9 - 25 < 0$$
$$(a - 4)^2 - 16 < 0$$
$$(a - 4)^2 < 16$$
$$-4 < a - 4 < 4$$
$$0 < a < 8$$

Jadi, batasan nilai $a$ yang memenuhi adalah $0 < a < 8$.
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b01-c-hard-bt01-017
*variasi (angka) | C5 | 4 langkah | jenis: nilai parameter garis menyinggung lingkaran*

Nilai $p$ yang memenuhi agar garis $g \equiv y = -2x + p$ menyinggung lingkaran $L \equiv x^2 + y^2 - 6x - 2y + 5 = 0$ adalah ....

- A. $p = -12$ atau $p = -2$  
  <sub>Salah: Kesalahan tanda saat memfaktorkan persamaan kuadrat, yaitu menggunakan $(p + 2)(p + 12) = 0$.</sub>
- **B. $p = 2$ atau $p = 12$** ✅  
  <sub>Benar: Substitusi $y = -2x + p$ menghasilkan persamaan kuadrat $5x^2 - (4p + 2)x + (p^2 - 2p + 5) = 0$. Syarat menyinggung adalah diskriminan $D = 0$, yang menghasilkan persamaan kuadrat $p^2 - 14p + 24 = 0$, sehingga diperoleh $p = 2$ atau $p = 12$.</sub>
- C. $p = -2$ atau $p = 12$  
  <sub>Salah: Kesalahan tanda pada salah satu akar saat menentukan pembuat nol dari faktor linier.</sub>
- D. $p = 4$ atau $p = 10$  
  <sub>Salah: Kesalahan perhitungan nilai diskriminan pada suku linier $b^2$.</sub>

**Pembahasan:** Substitusikan persamaan garis $y = -2x + p$ ke persamaan lingkaran:
$$x^2 + (-2x + p)^2 - 6x - 2(-2x + p) + 5 = 0$$
$$x^2 + 4x^2 - 4px + p^2 - 6x + 4x - 2p + 5 = 0$$
$$5x^2 - (4p + 2)x + (p^2 - 2p + 5) = 0$$

Syarat garis menyinggung lingkaran adalah nilai diskriminan $D = 0$:
$$D = b^2 - 4ac = 0$$
$$[-(4p + 2)]^2 - 4(5)(p^2 - 2p + 5) = 0$$
$$16p^2 + 16p + 4 - 20(p^2 - 2p + 5) = 0$$
$$16p^2 + 16p + 4 - 20p^2 + 40p - 100 = 0$$
$$-4p^2 + 56p - 96 = 0$$

Bagi kedua ruas dengan $-4$:
$$p^2 - 14p + 24 = 0$$
$$(p - 2)(p - 12) = 0$$
Diperoleh $p = 2$ atau $p = 12$.
**Acuan:** pretest — kelas12_tl-b01-p0067-latihan-soal-kedudukan-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b01-c-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: banyak nilai parameter garis memotong lingkaran*

Diketahui garis $g \equiv 4x - 3y + c = 0$ dan lingkaran $L \equiv x^2 + y^2 + 2x - 4y - 20 = 0$. Jika $c$ adalah bilangan bulat positif kelipatan $5$, banyak nilai $c$ yang membuat garis $g$ memotong lingkaran $L$ di dua titik berbeda adalah ....

- A. $5$  
  <sub>Salah: Kesalahan menganggap interval terbuka sebagai $c < 30$, sehingga nilai 30 tidak terhitung.</sub>
- B. $8$  
  <sub>Salah: Kesalahan mengikutsertakan kedua nilai batas $0$ dan $35$.</sub>
- **C. $6$** ✅  
  <sub>Benar: Pusat lingkaran $(-1, 2)$ dan jari-jari $r = 5$. Jarak pusat ke garis adalah $d = \frac{|c - 10|}{5}$. Garis memotong lingkaran jika $d < r \iff |c - 10| < 25$, sehingga $-15 < c < 35$. Nilai $c$ bulat positif kelipatan 5 adalah $5, 10, 15, 20, 25, 30$, yaitu sebanyak 6 nilai.</sub>
- D. $7$  
  <sub>Salah: Kesalahan mengikutsertakan nilai $0$ yang bukan bilangan bulat positif, atau mengikutsertakan batas $35$.</sub>

**Pembahasan:** Ubah persamaan lingkaran ke bentuk baku:
$$x^2 + y^2 + 2x - 4y - 20 = 0$$
$$(x + 1)^2 + (y - 2)^2 - 1 - 4 - 20 = 0$$
$$(x + 1)^2 + (y - 2)^2 = 25$$
Pusat lingkaran adalah $P(-1, 2)$ dan jari-jari $r = \sqrt{25} = 5$.

Jarak titik pusat $P(-1, 2)$ ke garis $4x - 3y + c = 0$ dirumuskan oleh:
$$d = \frac{|4(-1) - 3(2) + c|}{\sqrt{4^2 + (-3)^2}} = \frac{|c - 10|}{5}$$

Agar garis memotong lingkaran di dua titik berbeda, jarak titik pusat ke garis harus lebih kecil dari jari-jari ($d < r$):
$$\frac{|c - 10|}{5} < 5$$
$$|c - 10| < 25$$
$$-25 < c - 10 < 25$$
$$-15 < c < 35$$

Diketahui $c$ merupakan bilangan bulat positif kelipatan $5$, sehingga nilai $c$ yang memenuhi adalah:
$$c \in \{5, 10, 15, 20, 25, 30\}$$
Banyak nilai $c$ yang mungkin adalah $6$.
**Acuan:** siswa — siswa hal.60

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b01-c-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: jumlah nilai parameter bulat titik interior lingkaran*

Titik $P(k, k + 1)$ terletak di dalam lingkaran $L \equiv x^2 + y^2 - 6x - 8y + 17 = 0$. Jika $k$ adalah bilangan bulat, jumlah semua nilai $k$ yang mungkin adalah ....

- A. $15$  
  <sub>Salah: Kesalahan mengikutsertakan kedua nilai batas $1$ dan $5$ ($1 + 2 + 3 + 4 + 5 = 15$).</sub>
- B. $7$  
  <sub>Salah: Kesalahan perhitungan batas interval sehingga hanya menjumlahkan $3 + 4 = 7$.</sub>
- **C. $9$** ✅  
  <sub>Benar: Substitusi $P(k, k+1)$ menghasilkan kuasa titik $2k^2 - 12k + 10 < 0 \iff k^2 - 6k + 5 < 0 \iff 1 < k < 5$. Nilai $k$ bilangan bulat yang memenuhi adalah $2, 3, 4$, dan jumlahnya adalah $2 + 3 + 4 = 9$.</sub>
- D. $10$  
  <sub>Salah: Kesalahan menggunakan pertidaksamaan non-ketat $1 \le k < 5$, sehingga nilai $1$ ikut dijumlahkan ($1 + 2 + 3 + 4 = 10$).</sub>

**Pembahasan:** Titik $P(k, k + 1)$ terletak di dalam lingkaran apabila nilai kuasa titiknya bernilai negatif ($K < 0$):
$$K = k^2 + (k + 1)^2 - 6(k) - 8(k + 1) + 17 < 0$$
$$k^2 + k^2 + 2k + 1 - 6k - 8k - 8 + 17 < 0$$
$$2k^2 - 12k + 10 < 0$$

Bagi kedua ruas dengan 2:
$$k^2 - 6k + 5 < 0$$
$$(k - 1)(k - 5) < 0$$
Diperoleh batasan nilai $k$:
$$1 < k < 5$$

Karena $k$ merupakan bilangan bulat, maka nilai-nilai $k$ yang memenuhi adalah:
$$k \in \{2, 3, 4\}$$

Jumlah semua nilai $k$ yang mungkin adalah:
$$2 + 3 + 4 = 9$$
**Acuan:** siswa — siswa hal.55

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
