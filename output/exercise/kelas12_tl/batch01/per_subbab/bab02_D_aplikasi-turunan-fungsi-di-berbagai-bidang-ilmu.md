# Lembar koreksi — kelas12_tl SMA12L-B2 subbab D: Aplikasi Turunan Fungsi di Berbagai Bidang Ilmu

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b02-d-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: nilai optimum ekonomi*

Keuntungan produksi suatu barang dinyatakan dengan fungsi $f(x) = 360x - 3x^2$, dengan $f(x)$ dalam ribuan rupiah dan $x$ menyatakan banyak unit barang. Tentukan jumlah unit barang yang harus diproduksi agar keuntungan mencapai maksimum.

- A. $30$ unit  
  <sub>Salah: Membagi kembali hasil stasioner dengan dua tanpa dasar.</sub>
- B. $120$ unit  
  <sub>Salah: Lupa mengalikan koefisien dengan pangkat turunan sehingga menghitung $360 - 3x = 0$.</sub>
- **C. $60$ unit** ✅  
  <sub>Benar: Keuntungan maksimum tercapai saat turunan pertama bernilai nol: $f'(x) = 360 - 6x = 0 \iff 6x = 360 \iff x = 60$.</sub>
- D. $180$ unit  
  <sub>Salah: Hanya membagi koefisien linier dengan 2 tanpa memedulikan turunan fungsi kuadrat.</sub>

**Pembahasan:** Fungsi keuntungan: $f(x) = 360x - 3x^2$.
Syarat keuntungan maksimum: $f'(x) = 0$.
$f'(x) = 360 - 6x = 0$
$6x = 360$
$x = 60$
Jadi, banyak barang yang harus diproduksi agar keuntungan maksimum adalah $60$ unit.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b02-d-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: kecepatan sesaat*

Ketinggian sebuah bola yang dilempar vertikal ke atas dari tanah setelah $t$ detik diberikan oleh fungsi $h(t) = 48t - 6t^2$ meter. Kecepatan sesaat bola pada saat $t = 3$ detik adalah ....

- **A. $12\text{ m/s}$** ✅  
  <sub>Benar: Turunan pertama $h'(t) = 48 - 12t$. Untuk $t = 3$, $v(3) = 48 - 12(3) = 12\text{ m/s}$.</sub>
- B. $6\text{ m/s}$  
  <sub>Salah: Kesalahan aritmetika saat menghitung $48 - 36$.</sub>
- C. $30\text{ m/s}$  
  <sub>Salah: Salah menurunkan fungsi kuadrat menjadi $48 - 6t$ sehingga menghasilkan $48 - 18 = 30$.</sub>
- D. $90\text{ m/s}$  
  <sub>Salah: Menyubstitusikan langsung nilai $t = 3$ ke fungsi posisi $h(t)$, bukan ke fungsi kecepatan.</sub>

**Pembahasan:** Kecepatan sesaat merupakan turunan pertama dari fungsi ketinggian:
$v(t) = h'(t) = 48 - 12t$
Pada saat $t = 3$ detik:
$v(3) = 48 - 12(3) = 48 - 36 = 12\text{ m/s}$.
**Acuan:** siswa — siswa hal.170 Uji Kompetensi Bab 2 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b02-d-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: laju perubahan sesaat*

Sebuah perusahaan memproduksi $x$ unit barang dengan fungsi biaya total $C(x) = 0,25x^2 + 40x + 500$ (dalam ribuan rupiah). Jika perusahaan saat ini memproduksi $80$ unit barang, laju perubahan biaya total terhadap perubahan jumlah produksi adalah ....

- A. $40$ ribu rupiah per unit  
  <sub>Salah: Hanya mengambil turunan suku linier dan mengabaikan turunan suku kuadrat.</sub>
- B. $60$ ribu rupiah per unit  
  <sub>Salah: Lupa mengalikan dengan pangkat pada saat menurunkan suku kuadrat sehingga $C'(x) = 0,25x + 40$.</sub>
- C. $100$ ribu rupiah per unit  
  <sub>Salah: Salah melakukan perkalian desimal $0,5 \times 80 = 60$.</sub>
- **D. $80$ ribu rupiah per unit** ✅  
  <sub>Benar: Laju perubahan biaya diperoleh dari $C'(x) = 0,5x + 40$. Untuk $x = 80$, diperoleh $C'(80) = 0,5(80) + 40 = 80$.</sub>

**Pembahasan:** Laju perubahan biaya total terhadap produksi adalah fungsi turunan pertama $C'(x)$:
$C'(x) = 2(0,25)x + 40 = 0,5x + 40$
Untuk $x = 80$ unit:
$C'(80) = 0,5(80) + 40 = 40 + 40 = 80$ ribu rupiah per unit.
**Acuan:** siswa — siswa hal.170 Uji Kompetensi Bab 2 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b02-d-easy-bt01-004
*orisinal | C2 | 2 langkah | jenis: percepatan sesaat*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = t^3 - 3t^2 + 8t$ ($s$ dalam meter dan $t$ dalam detik). Percepatan partikel tersebut pada saat $t = 4$ detik adalah ....

- A. $32\text{ m/s}^2$  
  <sub>Salah: Hanya menghitung kecepatan sesaat (turunan pertama) pada $t = 4$.</sub>
- B. $24\text{ m/s}^2$  
  <sub>Salah: Lupa menurunkan suku $-6t$ pada turunan kedua sehingga hanya menghitung $6t$.</sub>
- **C. $18\text{ m/s}^2$** ✅  
  <sub>Benar: Percepatan merupakan turunan kedua: $v(t) = s'(t) = 3t^2 - 6t + 8$, lalu $a(t) = v'(t) = 6t - 6$. Untuk $t = 4$, $a(4) = 6(4) - 6 = 18\text{ m/s}^2$.</sub>
- D. $12\text{ m/s}^2$  
  <sub>Salah: Kesalahan aritmetika saat menghitung $6(4) - 6$.</sub>

**Pembahasan:** Fungsi kecepatan:
$v(t) = s'(t) = 3t^2 - 6t + 8$
Fungsi percepatan:
$a(t) = v'(t) = 6t - 6$
Pada $t = 4$ detik:
$a(4) = 6(4) - 6 = 24 - 6 = 18\text{ m/s}^2$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b02-d-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: kecepatan gerak lurus*

Posisi sebuah benda yang bergerak dinyatakan oleh rumus $s(t) = 5t^2 - 4t + 10$, dengan $s$ dalam meter dan $t$ dalam detik. Kecepatan benda saat $t = 3$ detik adalah ....

- **A. $26\text{ m/s}$** ✅  
  <sub>Benar: $v(t) = s'(t) = 10t - 4$. Saat $t = 3$, $v(3) = 10(3) - 4 = 26\text{ m/s}$.</sub>
- B. $43\text{ m/s}$  
  <sub>Salah: Menyubstitusikan nilai $t = 3$ langsung ke rumus posisi $s(t)$.</sub>
- C. $22\text{ m/s}$  
  <sub>Salah: Salah melakukan turunan suku pertama menjadi $5t$ sehingga $5(3) - 4$ atau salah hitung aritmetika.</sub>
- D. $30\text{ m/s}$  
  <sub>Salah: Mengabaikan suku konstan $-4$ pada saat menurunkan rumus posisi.</sub>

**Pembahasan:** Kecepatan benda didapatkan dari turunan pertama fungsi posisi:
$v(t) = s'(t) = 10t - 4$
Untuk $t = 3$ detik:
$v(3) = 10(3) - 4 = 30 - 4 = 26\text{ m/s}$.
**Acuan:** siswa — siswa hal.165

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b02-d-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: laju perubahan konsentrasi*

Konsentrasi suatu obat dalam darah pasien (dalam mg/L) setelah $t$ jam diberikan oleh fungsi $C(t) = \frac{18t}{t + 2}$. Laju perubahan konsentrasi obat terhadap waktu saat $t = 4$ jam adalah ....

- A. $12\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Menghitung konsentrasi obat $C(4) = \frac{18(4)}{4+2} = 12$, bukan laju perubahannya.</sub>
- B. $0,5\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Lupa mengalikan suku konstanta turunan pembilang dengan benar sehingga mendapatkan 18 / 36 = 0,5.</sub>
- C. $3\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Turunan keliru diturunkan pembilang dan penyebut secara terpisah: 18 / 1 = 18 lalu dibagi nilai lain, atau salah operasi penyebut.</sub>
- **D. $1\text{ mg/(L}\cdot\text{jam)}$** ✅  
  <sub>Benar: Turunan $C'(t) = \frac{18(t+2) - 18t(1)}{(t+2)^2} = \frac{36}{(t+2)^2}$. Untuk $t=4$, $C'(4) = \frac{36}{6^2} = 1\text{ mg/(L}\cdot\text{jam)}$.</sub>

**Pembahasan:** Gunakan aturan turunan hasil bagi $u/v$:
$$u = 18t \implies u' = 18$$
$$v = t + 2 \implies v' = 1$$
$$C'(t) = \frac{u'v - uv'}{v^2} = \frac{18(t + 2) - 18t(1)}{(t + 2)^2} = \frac{36}{(t + 2)^2}$$
Substitusikan $t = 4$:
$$C'(4) = \frac{36}{(4 + 2)^2} = \frac{36}{36} = 1\text{ mg/(L}\cdot\text{jam)}$$
**Acuan:** siswa — siswa hal.170 Uji Kompetensi Bab 2 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b02-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: jumlah produksi laba maksimum*

Keuntungan penjualan suatu produk rumahan dinyatakan oleh fungsi $f(x) = 180x - 2x^2$ (dalam ribuan rupiah), dengan $x$ menyatakan banyak unit barang yang terjual. Banyaknya barang yang harus terjual agar diperoleh keuntungan maksimum adalah ....

- **A. $45\text{ unit}$** ✅  
  <sub>Benar: Syarat stasioner $f'(x) = 0 \implies 180 - 4x = 0 \implies x = 45$.</sub>
- B. $4.050\text{ unit}$  
  <sub>Salah: Menghitung nilai keuntungan maksimumnya f(45) = 4.050, bukan banyak unit barang x.</sub>
- C. $30\text{ unit}$  
  <sub>Salah: Salah membagi koefisien: 180 dibagi 6 menghasilkan 30.</sub>
- D. $90\text{ unit}$  
  <sub>Salah: Lupa menurunkan pangkat dua secara penuh, menyelesaikan 180 - 2x = 0 sehingga x = 90.</sub>

**Pembahasan:** Keuntungan maksimum tercapai saat turunan pertama bernilai nol ($f'(x) = 0$):
$$f(x) = 180x - 2x^2$$
$$f'(x) = 180 - 4x = 0$$
$$4x = 180$$
$$x = 45$$
Jadi, barang yang harus terjual agar keuntungan maksimum adalah $45\text{ unit}$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b02-d-easy-bt01-008
*orisinal | C1 | 2 langkah | jenis: fungsi percepatan benda*

Posisi sebuah partikel yang bergerak lurus dinyatakan oleh persamaan $s(t) = 2t^3 - 5t^2 + 4t$ (dengan $s$ dalam meter dan $t$ dalam detik). Rumus fungsi percepatan $a(t)$ dari gerak partikel tersebut adalah ....

- A. $a(t) = 6t^2 - 10t + 4$  
  <sub>Salah: Hanya menurunkan satu kali (baru fungsi kecepatan v(t), belum percepatan).</sub>
- **B. $a(t) = 12t - 10$** ✅  
  <sub>Benar: Percepatan adalah turunan kedua: s'(t) = 6t^2 - 10t + 4, lalu s''(t) = 12t - 10.</sub>
- C. $a(t) = 12t - 5$  
  <sub>Salah: Salah saat menurunkan turunan pertama: turunan dari -10t ditulis -5.</sub>
- D. $a(t) = 6t - 10$  
  <sub>Salah: Salah saat menurunkan suku pertama turunan kedua: mengalikan 6 dengan 1 bukan dengan 2.</sub>

**Pembahasan:** Fungsi kecepatan $v(t)$ merupakan turunan pertama fungsi posisi:
$$v(t) = s'(t) = 6t^2 - 10t + 4$$
Fungsi percepatan $a(t)$ merupakan turunan kedua fungsi posisi (turunan pertama kecepatan):
$$a(t) = s''(t) = v'(t) = 12t - 10$$
Jadi, fungsi percepatan partikel tersebut adalah $a(t) = 12t - 10$.
**Acuan:** siswa — siswa hal.166

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b02-d-easy-bt01-009
*orisinal | C2 | 2 langkah | jenis: kecepatan sesaat trigonometri*

Sebuah objek berosilasi pada suatu lintasan dengan persamaan posisi $s(t) = \sin(2t) + 5t$ ($s$ dalam meter dan $t$ dalam detik). Kecepatan objek saat $t = 0$ detik adalah ....

- A. $5\text{ m/s}$  
  <sub>Salah: Mengabaikan turunan rantai atau menganggap cos(0) bernilai 0 sehingga 2(0) + 5 = 5.</sub>
- B. $6\text{ m/s}$  
  <sub>Salah: Lupa aturan rantai turunan sudut sin(2t) menjadi cos(2t), menghasilkan cos(0) + 5 = 1 + 5 = 6.</sub>
- **C. $7\text{ m/s}$** ✅  
  <sub>Benar: v(t) = s'(t) = 2 cos(2t) + 5. Pada t = 0, v(0) = 2 cos(0) + 5 = 2(1) + 5 = 7 m/s.</sub>
- D. $0\text{ m/s}$  
  <sub>Salah: Langsung menyubstitusikan t = 0 ke fungsi posisi s(0) = sin(0) + 5(0) = 0.</sub>

**Pembahasan:** Kecepatan merupakan turunan pertama dari fungsi lintasan posisi:
$$v(t) = s'(t) = \frac{d}{dt}(\sin(2t) + 5t) = 2\cos(2t) + 5$$
Pada saat $t = 0$ detik:
$$v(0) = 2\cos(2 \cdot 0) + 5 = 2\cos(0) + 5 = 2(1) + 5 = 7\text{ m/s}$$
**Acuan:** siswa — siswa hal.165

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b02-d-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: dua bilangan jumlah minimum*

Tentukan dua bilangan real positif dengan jumlah kedua bilangan itu minimum dan mempunyai hasil kali $100$.

- A. Kedua bilangan bernilai sama, yaitu $20$  
  <sub>Salah: Membagi 100 dengan perkiraan salah satu faktor persekutuan 5.</sub>
- **B. Kedua bilangan bernilai sama, yaitu $10$** ✅  
  <sub>Benar: Misalkan bilangan tersebut $x$ dan $y$ dengan $x \cdot y = 100$, sehingga $y = \frac{100}{x}$. Jumlahnya $S(x) = x + \frac{100}{x}$. Nilai minimum diperoleh saat $S'(x) = 1 - \frac{100}{x^2} = 0 \implies x^2 = 100 \implies x = 10$. Maka $y = \frac{100}{10} = 10$.</sub>
- C. Kedua bilangan bernilai sama, yaitu $5\sqrt{2}$  
  <sub>Salah: Salah menghitung akar kuadrat dari 100.</sub>
- D. Kedua bilangan bernilai sama, yaitu $50$  
  <sub>Salah: Membagi 100 dengan 2 tanpa meminimumkan jumlah fungsi kuadrat/turunan.</sub>

**Pembahasan:** Misalkan kedua bilangan adalah $x$ dan $y$.
Diketahui $x \cdot y = 100$, maka $y = \frac{100}{x}$.
Fungsi jumlah kedua bilangan:
$$S(x) = x + y = x + \frac{100}{x}$$
Agar jumlah minimum, syarat stasioner $S'(x) = 0$:
$$S'(x) = 1 - \frac{100}{x^2} = 0$$
$$x^2 = 100 \implies x = 10 \quad (x > 0)$$
Nilai bilangan kedua:
$$y = \frac{100}{10} = 10$$
Jadi, kedua bilangan bernilai sama, yaitu $10$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b02-d-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: biaya marjinal produksi*

Sebuah perusahaan memproduksi $x$ unit barang dengan fungsi biaya total $C(x) = 0,05x^2 + 20x + 500$ (dalam ribuan rupiah). Jika perusahaan saat ini memproduksi $200$ unit barang, laju perubahan biaya total terhadap perubahan jumlah produksi adalah ....

- A. $50$ ribu rupiah per unit  
  <sub>Salah: Kesalahan aritmetika pada hasil kali $0,1 \times 200$ menjadi $30$.</sub>
- **B. $40$ ribu rupiah per unit** ✅  
  <sub>Benar: Laju perubahan biaya diperoleh dari $C'(x) = 0,1x + 20$. Untuk $x = 200$, diperoleh $C'(200) = 0,1(200) + 20 = 20 + 20 = 40$ ribu rupiah per unit.</sub>
- C. $25$ ribu rupiah per unit  
  <sub>Salah: Hanya menghitung biaya rata-rata sederhana bukan turunan fungsi biaya total.</sub>
- D. $30$ ribu rupiah per unit  
  <sub>Salah: Salah menghitung turunan koefisien $0,05x^2$ menjadi $0,05x$ sehingga $0,05(200) + 20 = 30$.</sub>

**Pembahasan:** Laju perubahan biaya total terhadap jumlah produksi adalah turunan pertama dari fungsi biaya $C(x)$:
$$C'(x) = \frac{d}{dx}(0,05x^2 + 20x + 500) = 0,1x + 20$$
Substitusikan $x = 200$:
$$C'(200) = 0,1(200) + 20 = 20 + 20 = 40$$
Jadi, laju perubahannya adalah $40$ ribu rupiah per unit.
**Acuan:** siswa — siswa hal.170 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b02-d-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: kecepatan sesaat vertikal*

Ketinggian sebuah bola yang dilempar vertikal ke atas dari tanah setelah $t$ detik diberikan oleh fungsi $h(t) = 60t - 5t^2$ meter. Kecepatan sesaat bola pada saat $t = 4$ detik adalah ....

- A. $40\text{ m/s}$  
  <sub>Salah: Hanya menghitung bagian pengurang $10(4) = 40$ tanpa mengurangkannya dari 60.</sub>
- **B. $20\text{ m/s}$** ✅  
  <sub>Benar: Turunan pertama fungsi posisi adalah kecepatan $v(t) = h'(t) = 60 - 10t$. Untuk $t = 4$, diperoleh $v(4) = 60 - 10(4) = 20\text{ m/s}$.</sub>
- C. $160\text{ m/s}$  
  <sub>Salah: Langsung menyubstitusikan $t = 4$ ke persamaan ketinggian $h(t)$ bukan ke turunan kecepatannya.</sub>
- D. $10\text{ m/s}$  
  <sub>Salah: Menggunakan koefisien percepatan tanpa mengalikan dengan waktu saat evaluasi.</sub>

**Pembahasan:** Persamaan ketinggian: $h(t) = 60t - 5t^2$.
Kecepatan sesaat ditentukan oleh turunan pertama terhadap waktu $t$:
$$v(t) = h'(t) = 60 - 10t$$
Untuk $t = 4$ detik:
$$v(4) = 60 - 10(4) = 60 - 40 = 20\text{ m/s}$$
Jadi, kecepatan sesaat bola adalah $20\text{ m/s}$.
**Acuan:** siswa — siswa hal.170 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b02-d-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: definisi kecepatan sesaat*

Jika suatu partikel bergerak sepanjang garis lurus dengan posisi dinyatakan oleh fungsi $s(t)$, laju perubahan sesaat dari posisi terhadap waktu $t$, yaitu $\frac{ds}{dt}$, menyatakan ....

- A. percepatan sesaat partikel  
  <sub>Salah: Tertukar dengan turunan kedua dari fungsi posisi.</sub>
- B. posisi awal partikel  
  <sub>Salah: Tertukar dengan nilai fungsi posisi saat $t = 0$.</sub>
- C. jarak tempuh total partikel  
  <sub>Salah: Tertukar dengan panjang lintasan atau nilai skalar posisi.</sub>
- **D. kecepatan sesaat partikel** ✅  
  <sub>Benar: Berdasarkan konsep turunan dalam fisika, turunan pertama fungsi posisi terhadap waktu merupakan definisi dari kecepatan sesaat.</sub>

**Pembahasan:** Dalam aplikasi turunan fungsi pada bidang fisika kinetika, laju perubahan sesaat dari posisi $s(t)$ terhadap waktu $t$, yang dinyatakan dengan notasi $\frac{ds}{dt}$, merepresentasikan nilai kecepatan sesaat ($v$) partikel tersebut.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b02-d-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: percepatan dari fungsi kecepatan*

Kecepatan sebuah partikel yang bergerak sepanjang garis lurus dimodelkan oleh $v(t) = 8t + 3$ (dalam m/s). Besar percepatan partikel tersebut pada saat $t = 5$ detik adalah ....

- A. $16\text{ m/s}^2$  
  <sub>Salah: Mengalikan koefisien turunan dengan 2 karena mengira aturan pangkat.</sub>
- B. $43\text{ m/s}^2$  
  <sub>Salah: Langsung menyubstitusikan nilai $t = 5$ ke dalam rumus fungsi kecepatan $v(t)$ tanpa menurunkannya.</sub>
- C. $40\text{ m/s}^2$  
  <sub>Salah: Mengalikan koefisien 8 langsung dengan nilai waktu $t = 5$.</sub>
- **D. $8\text{ m/s}^2$** ✅  
  <sub>Benar: Percepatan adalah turunan pertama dari kecepatan terhadap waktu, $a(t) = v'(t) = \frac{d}{dt}(8t + 3) = 8\text{ m/s}^2$ (konstan untuk setiap $t$).</sub>

**Pembahasan:** Percepatan $a(t)$ diperoleh dari turunan pertama fungsi kecepatan $v(t)$ terhadap waktu:
$$a(t) = v'(t) = \frac{d}{dt}(8t + 3) = 8\text{ m/s}^2$$
Karena percepatan bernilai konstan, pada saat $t = 5$ detik percepatannya tetap $8\text{ m/s}^2$.
**Acuan:** siswa — siswa hal.166

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b02-d-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: laju perubahan obat*

Konsentrasi obat dalam aliran darah pasien setelah $t$ jam disuntikkan diberikan oleh fungsi $C(t) = \frac{36t}{t + 1}$ mg/L. Laju perubahan konsentrasi obat terhadap waktu pada saat $t = 2$ jam adalah ....

- **A. $4\text{ mg/(L}\cdot\text{jam)}$** ✅  
  <sub>Benar: Turunan $C'(t) = \frac{36(t+1) - 36t(1)}{(t+1)^2} = \frac{36}{(t+1)^2}$. Untuk $t = 2$, diperoleh $C'(2) = \frac{36}{(2+1)^2} = \frac{36}{9} = 4$.</sub>
- B. $9\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Salah menghitung turunan pembilang menjadi sekadar penyebut kuadrat yaitu $(2+1)^2 = 9$.</sub>
- C. $24\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Menghitung nilai konsentrasi langsung $C(2) = \frac{72}{3} = 24$, bukan laju perubahannya.</sub>
- D. $12\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Lupa mengkuadratkan penyebut: menghitung $36 / (2 + 1) = 12$.</sub>

**Pembahasan:** Laju perubahan konsentrasi obat terhadap waktu diperoleh dari turunan pertama fungsi $C(t)$ terhadap $t$:
$$
C'(t) = \frac{36 \cdot (t + 1) - 36t \cdot 1}{(t + 1)^2} = \frac{36t + 36 - 36t}{(t + 1)^2} = \frac{36}{(t + 1)^2}
$$
Pada saat $t = 2$ jam:
$$
C'(2) = \frac{36}{(2 + 1)^2} = \frac{36}{3^2} = \frac{36}{9} = 4\text{ mg/(L}\cdot\text{jam)}
$$
**Acuan:** siswa — siswa hal.170 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b02-d-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: kecepatan gerak vertikal*

Sebuah anak panah ditembakkan secara vertikal ke udara dan lintasannya setelah $t$ detik diberikan oleh persamaan $s(t) = -5t^2 + 70t$ ($s$ dalam meter dan $t$ dalam detik). Kecepatan anak panah setelah $4$ detik adalah ....

- **A. $30\text{ m/s}$** ✅  
  <sub>Benar: Turunan pertama fungsi lintasan adalah $v(t) = s'(t) = -10t + 70$. Untuk $t = 4$, diperoleh $v(4) = -10(4) + 70 = 30\text{ m/s}$.</sub>
- B. $110\text{ m/s}$  
  <sub>Salah: Salah tanda pada turunan menjadi $10t + 70$, sehingga $10(4) + 70 = 110$.</sub>
- C. $200\text{ m/s}$  
  <sub>Salah: Menghitung jarak tempuh $s(4) = -5(16) + 280 = 200$, bukan kecepatan.</sub>
- D. $50\text{ m/s}$  
  <sub>Salah: Salah menurunkan $-5t^2$ menjadi $-5t$, sehingga menghitung $-5(4) + 70 = 50$.</sub>

**Pembahasan:** Kecepatan sesaat merupakan turunan pertama dari fungsi posisi terhadap waktu:
$$
v(t) = s'(t) = \frac{d}{dt}(-5t^2 + 70t) = -10t + 70
$$
Kecepatan setelah $t = 4$ detik:
$$
v(4) = -10(4) + 70 = -40 + 70 = 30\text{ m/s}
$$
**Acuan:** siswa — siswa hal.172 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b02-d-easy-bt01-017
*orisinal | C1 | 1 langkah | jenis: penentuan fungsi percepatan*

Kecepatan sesaat suatu partikel yang bergerak lurus dinyatakan oleh fungsi $v(t) = 6t^2 - 4t + 5$ (dalam m/s). Fungsi percepatan sesaat $a(t)$ dari partikel tersebut adalah ....

- A. $a(t) = 12t + 5$  
  <sub>Salah: Salah menurunkan konstanta $+5$ dan melupakan turunan dari $-4t$.</sub>
- **B. $a(t) = 12t - 4$** ✅  
  <sub>Benar: Percepatan merupakan turunan pertama fungsi kecepatan terhadap waktu: $a(t) = v'(t) = 12t - 4$.</sub>
- C. $a(t) = 2t^3 - 2t^2 + 5t$  
  <sub>Salah: Melakukan integrasi alih-alih diferensiasi.</sub>
- D. $a(t) = 6t - 4$  
  <sub>Salah: Pangkat pada $t^2$ tidak dikalikan ke koefisien saat menurunkan.</sub>

**Pembahasan:** Percepatan sesaat $a(t)$ adalah laju perubahan kecepatan terhadap waktu, yang dinyatakan sebagai turunan pertama dari fungsi kecepatan $v(t)$:
$$
a(t) = v'(t) = \frac{d}{dt}(6t^2 - 4t + 5) = 12t - 4
$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b02-d-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: waktu tinggi maksimum*

Ketinggian sebuah roket air dinyatakan oleh fungsi $h(t) = 40t - 5t^2$ (dalam meter, $t$ dalam detik). Roket air tersebut akan mencapai ketinggian maksimum saat waktu $t$ bernilai ....

- A. $8\text{ detik}$  
  <sub>Salah: Menghitung waktu roket kembali jatuh ke tanah ($h(t) = 0$).</sub>
- B. $5\text{ detik}$  
  <sub>Salah: Mengira $t$ sama dengan koefisien kuadrat $5$.</sub>
- **C. $4\text{ detik}$** ✅  
  <sub>Benar: Ketinggian maksimum terjadi saat $h'(t) = 0 \iff 40 - 10t = 0 \iff t = 4$ detik.</sub>
- D. $2\text{ detik}$  
  <sub>Salah: Salah menurunkan $-5t^2$ menjadi $-20t$ sehingga $40 - 20t = 0 \iff t = 2$.</sub>

**Pembahasan:** Ketinggian maksimum tercapai saat turunan pertama dari $h(t)$ bernilai nol ($h'(t) = 0$):
$$
h'(t) = 40 - 10t = 0
$$
$$
10t = 40 \implies t = 4\text{ detik}
$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b02-d-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: dimensi luas maksimum*

Seorang petani memiliki $80\text{ meter}$ kawat pagar untuk membuat kandang berbentuk persegi panjang. Agar luas kandang maksimum, panjang dan lebar kandang berturut-turut adalah ....

- A. $40\text{ meter}$ dan $40\text{ meter}$  
  <sub>Salah: Siswa tidak membagi keliling dengan 2 saat merumuskan panjang dan lebar.</sub>
- B. $10\text{ meter}$ dan $10\text{ meter}$  
  <sub>Salah: Siswa keliru membagi total keliling dengan 8.</sub>
- C. $30\text{ meter}$ dan $10\text{ meter}$  
  <sub>Salah: Siswa memilih pasangan sembarang yang jumlahnya 40 tanpa memaksimumkan fungsi luas.</sub>
- **D. $20\text{ meter}$ dan $20\text{ meter}$** ✅  
  <sub>Benar: Keliling kandang $2(p + l) = 80 \Rightarrow l = 40 - p$. Luas $L(p) = p(40 - p) = 40p - p^2$. Luas maksimum dicapai saat $L'(p) = 40 - 2p = 0 \Rightarrow p = 20\text{ meter}$ dan $l = 20\text{ meter}$.</sub>

**Pembahasan:** Misalkan panjang kandang adalah $p$ dan lebar kandang adalah $l$.
Keliling persegi panjang:
$$K = 2(p + l) = 80 \implies p + l = 40 \implies l = 40 - p$$
Fungsi luas kandang:
$$L(p) = p \cdot l = p(40 - p) = 40p - p^2$$
Agar luas maksimum, turunan pertama fungsi luas harus bernilai nol ($L'(p) = 0$):
$$L'(p) = 40 - 2p = 0 \implies 2p = 40 \implies p = 20\text{ meter}$$
Lebar kandang:
$$l = 40 - 20 = 20\text{ meter}$$
Jadi, panjang dan lebar kandang berturut-turut adalah $20\text{ meter}$ dan $20\text{ meter}$.
**Acuan:** siswa — siswa hal.170 A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b02-d-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: kecepatan gerak proyektil*

Sebuah anak panah ditembakkan secara vertikal ke udara dan jaraknya (dalam meter) setelah $t$ detik diberikan oleh persamaan $s(t) = -4t^2 + 48t$. Berapakah kecepatan anak panah setelah $3$ detik?

- A. $108\text{ m/s}$  
  <sub>Salah: Siswa menyubstitusikan nilai $t = 3$ langsung ke fungsi posisi $s(t)$ bukan ke fungsi kecepatan $v(t)$.</sub>
- B. $36\text{ m/s}$  
  <sub>Salah: Siswa salah menurunkan pangkat variabel kuadrat sehingga persamaannya menjadi $48 - 4t$ dan menghasilkan $48 - 12 = 36$.</sub>
- **C. $24\text{ m/s}$** ✅  
  <sub>Benar: Turunan pertama fungsi posisi adalah $v(t) = s'(t) = -8t + 48$. Untuk $t = 3$, $v(3) = -8(3) + 48 = 24\text{ m/s}$.</sub>
- D. $40\text{ m/s}$  
  <sub>Salah: Siswa salah melakukan operasi turunan $-8(3) + 48$ menjadi $-8 + 48 = 40$ karena lupa mengalikan koefisien dengan waktu.</sub>

**Pembahasan:** Fungsi kecepatan sesaat $v(t)$ diperoleh dari turunan pertama fungsi posisi $s(t)$:
$$v(t) = s'(t) = \frac{d}{dt}(-4t^2 + 48t) = -8t + 48$$

Substitusikan $t = 3$ ke dalam rumus kecepatan:
$$v(3) = -8(3) + 48 = -24 + 48 = 24\text{ m/s}$$

Jadi, kecepatan anak panah setelah $3$ detik adalah $24\text{ m/s}$.
**Acuan:** siswa — siswa hal.172 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b02-d-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: optimasi talang air*

Sebuah talang air akan dibuat dari selembar pelat seng selebar $48\text{ cm}$ dengan cara melipat kedua sisi sampingnya tegak lurus ke atas sama panjang. Tentukan ukuran lebar dasar dan tinggi talang air tersebut agar kapasitas penampung airnya maksimum.

- **A. Lebar dasar $24\text{ cm}$ dan tinggi $12\text{ cm}$** ✅  
  <sub>Benar: Misal tinggi lipatan adalah $x\text{ cm}$, maka lebar dasar talang adalah $(48 - 2x)\text{ cm}$. Luas penampang $L(x) = x(48 - 2x) = 48x - 2x^2$. Nilai maksimum dicapai saat $L'(x) = 0$, yaitu $48 - 4x = 0 \implies x = 12\text{ cm}$. Jadi tinggi talang $12\text{ cm}$ dan lebar dasarnya $48 - 2(12) = 24\text{ cm}$.</sub>
- B. Lebar dasar $16\text{ cm}$ dan tinggi $16\text{ cm}$  
  <sub>Salah: Siswa membagi lebar total seng langsung menjadi 3 bagian yang sama panjang ($48/3 = 16$).</sub>
- C. Lebar dasar $36\text{ cm}$ dan tinggi $6\text{ cm}$  
  <sub>Salah: Siswa salah menurunkan $2x^2$ menjadi $2x$, sehingga menghasilkan $48 - 2x = 0 \implies x = 6$ (tinggi $6\text{ cm}$, dasar $36\text{ cm}$).</sub>
- D. Lebar dasar $20\text{ cm}$ dan tinggi $14\text{ cm}$  
  <sub>Salah: Siswa membuat kesalahan dalam memfaktorkan persamaan turunan.</sub>

**Pembahasan:** Misalkan tinggi penampang talang adalah $x\text{ cm}$. Karena seng selebar $48\text{ cm}$ dilipat pada kedua sisinya, maka panjang dasar talang adalah $(48 - 2x)\text{ cm}$.

Fungsi luas penampang talang:
$$L(x) = x(48 - 2x) = 48x - 2x^2$$

Agar luas penampang (debit air) maksimum, turunan pertama fungsi luas terhadap $x$ harus bernilai nol:
$$L'(x) = 48 - 4x = 0$$
$$4x = 48 \implies x = 12$$

Ukuran talang:
- Tinggi talang $= x = 12\text{ cm}$
- Lebar dasar talang $= 48 - 2(12) = 24\text{ cm}$

Jadi, kapasitas maksimum tercapai saat lebar dasar $24\text{ cm}$ dan tinggi $12\text{ cm}$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b02-d-medium-bt01-002
*variasi (angka) | C4 | 3 langkah | jenis: optimasi luas bidang*

Sebuah persegi panjang dibentuk di atas sumbu-$X$ dan di bawah kurva parabola $y = 27 - x^2$. Dua titik sudut alas persegi panjang terletak pada sumbu-$X$ dan dua titik sudut lainnya terletak pada kurva tersebut. Luas maksimum persegi panjang tersebut adalah ....

- A. $162\text{ satuan luas}$  
  <sub>Salah: Siswa hanya menghitung suku pertama $54(3)$ dan lupa mengurangkan dengan $2x^3$.</sub>
- B. $54\text{ satuan luas}$  
  <sub>Salah: Siswa menganggap panjang alas persegi panjang hanya $x$, bukan $2x$, sehingga luas terhitung setengahnya.</sub>
- C. $72\text{ satuan luas}$  
  <sub>Salah: Siswa salah menghitung turunan $54x - 2x^3$ menjadi $54 - 3x^2 = 0$ atau salah evaluasi nilai luas.</sub>
- **D. $108\text{ satuan luas}$** ✅  
  <sub>Benar: Titik sudut pada kurva adalah $(x, 27 - x^2)$ untuk $x > 0$. Panjang alas persegi panjang adalah $2x$ dan tingginya $y = 27 - x^2$. Luas $L(x) = 2x(27 - x^2) = 54x - 2x^3$. Luas maksimum tercapai saat $L'(x) = 54 - 6x^2 = 0 \implies x^2 = 9 \implies x = 3$. Luas maksimum $= 54(3) - 2(3)^3 = 162 - 54 = 108\text{ satuan luas}$.</sub>

**Pembahasan:** Karena kurva simetris terhadap sumbu-$Y$, titik-titik sudut persegi panjang yang berada pada kurva adalah $(-x, 27 - x^2)$ dan $(x, 27 - x^2)$ dengan $x > 0$.

Ukuran persegi panjang:
- Panjang alas $= x - (-x) = 2x$
- Tinggi $= 27 - x^2$

Fungsi luas persegi panjang:
$$L(x) = 2x(27 - x^2) = 54x - 2x^3$$

Syarat luas maksimum adalah $L'(x) = 0$:
$$L'(x) = 54 - 6x^2 = 0$$
$$6x^2 = 54 \implies x^2 = 9 \implies x = 3$$

Substitusikan $x = 3$ ke fungsi luas:
$$L(3) = 54(3) - 2(3)^3 = 162 - 54 = 108\text{ satuan luas}$$

Jadi, luas maksimum persegi panjang tersebut adalah $108\text{ satuan luas}$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b02-d-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: optimasi keuntungan*

Biaya total untuk memproduksi $x$ unit barang dinyatakan oleh fungsi $C(x) = x^2 + 30x + 400$ (dalam ribuan rupiah). Jika setiap unit barang dijual dengan harga Rp90.000,00, keuntungan maksimum yang dapat diperoleh perusahaan tersebut adalah ....

- **A. Rp500.000,00** ✅  
  <sub>Benar: Pendapatan total $R(x) = 90x$ (dalam ribuan rupiah). Fungsi keuntungan $U(x) = R(x) - C(x) = 90x - (x^2 + 30x + 400) = -x^2 + 60x - 400$. Keuntungan maksimum saat $U'(x) = -2x + 60 = 0 \implies x = 30$. Nilai keuntungan maksimum $U(30) = -(30)^2 + 60(30) - 400 = -900 + 1800 - 400 = 500$ (ribu rupiah) = Rp500.000,00.</sub>
- B. Rp450.000,00  
  <sub>Salah: Siswa salah menghitung titik puncak atau keliru dalam operasi aritmetika saat substitusi nilai $x$.</sub>
- C. Rp900.000,00  
  <sub>Salah: Siswa menghitung nilai $-x^2 + 60x$ pada $x = 30$ namun lupa mengurangkan biaya tetap $400$ ribu rupiah.</sub>
- D. Rp300.000,00  
  <sub>Salah: Siswa mengira jumlah unit $x = 30$ langsung dikalikan $10$ tanpa evaluasi ke fungsi keuntungan lengkap.</sub>

**Pembahasan:** Diketahui:
- Fungsi biaya total: $C(x) = x^2 + 30x + 400$ (dalam ribuan rupiah)
- Harga jual per unit: Rp90.000,00 $= 90$ ribu rupiah
- Fungsi penerimaan total: $R(x) = 90x$ (dalam ribuan rupiah)

Fungsi keuntungan perusahaan:
$$U(x) = R(x) - C(x)$$
$$U(x) = 90x - (x^2 + 30x + 400) = -x^2 + 60x - 400$$

Keuntungan maksimum tercapai saat turunan pertama bernilai nol ($U'(x) = 0$):
$$U'(x) = -2x + 60 = 0$$
$$2x = 60 \implies x = 30$$

Substitusikan $x = 30$ ke dalam fungsi keuntungan:
$$U(30) = -(30)^2 + 60(30) - 400$$
$$U(30) = -900 + 1800 - 400 = 500\text{ (ribu rupiah)}$$

Keuntungan maksimum adalah $500 \times \text{Rp}1.000,00 = \text{Rp}500.000,00$.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b02-d-medium-bt01-004
*orisinal | C4 | 4 langkah | jenis: optimasi volume kotak*

Sebuah kotak tanpa tutup dibuat dari selembar karton berbentuk persegi dengan panjang sisi $24\text{ cm}$. Pada setiap pojok karton dipotong persegi identik berukuran sisi $x\text{ cm}$, kemudian sisi-sisinya dilipat ke atas. Volume maksimum kotak yang dapat dibuat adalah ....

- A. $1.152\text{ cm}^3$  
  <sub>Salah: Siswa salah saat ekspansi kuadrat sehingga menurunkan persamaan $V'(x) = 0$ secara keliru.</sub>
- B. $256\text{ cm}^3$  
  <sub>Salah: Siswa hanya menghitung luas alas kotak $(16\text{ cm} \times 16\text{ cm} = 256\text{ cm}^2)$ dan lupa mengalikannya dengan tinggi kotak $x = 4\text{ cm}$.</sub>
- **C. $1.024\text{ cm}^3$** ✅  
  <sub>Benar: Dimensi kotak: panjang = $24 - 2x$, lebar = $24 - 2x$, tinggi = $x$. Volume $V(x) = x(24 - 2x)^2 = 4x^3 - 96x^2 + 576x$. $V'(x) = 12x^2 - 192x + 576 = 0 \implies x^2 - 16x + 48 = 0 \implies (x - 4)(x - 12) = 0$. Karena $0 < x < 12$, nilai yang memenuhi adalah $x = 4\text{ cm}$. Maka $V(4) = 4(24 - 8)^2 = 4(16)^2 = 4 \times 256 = 1.024\text{ cm}^3$.</sub>
- D. $576\text{ cm}^3$  
  <sub>Salah: Siswa salah menentukan akar turunan menjadi $x = 6$, lalu menghitung $V(6) = 6(12)^2 = 864$ atau salah hitung lainnya.</sub>

**Pembahasan:** Karton berbentuk persegi dengan sisi $24\text{ cm}$. Jika keempat sudutnya dipotong bujur sangkar dengan sisi $x\text{ cm}$, maka ukuran kotak tanpa tutup adalah:
- Panjang alas $(p) = 24 - 2x$
- Lebar alas $(l) = 24 - 2x$
- Tinggi kotak $(t) = x$
- Domain fisis: $0 < x < 12$

Fungsi volume kotak:
$$V(x) = p \cdot l \cdot t = x(24 - 2x)^2 = x(576 - 96x + 4x^2) = 4x^3 - 96x^2 + 576x$$

Syarat volume maksimum adalah $V'(x) = 0$:
$$V'(x) = 12x^2 - 192x + 576 = 0$$
Bagi kedua ruas dengan 12:
$$x^2 - 16x + 48 = 0$$
$$(x - 4)(x - 12) = 0$$
$$x = 4 \quad \text{atau} \quad x = 12$$

Karena $x = 12$ menghasilkan ukuran alas $0$, maka nilai yang memenuhi adalah $x = 4\text{ cm}$.

Substitusikan $x = 4$ ke rumus volume:
$$V(4) = 4(24 - 2(4))^2 = 4(16)^2 = 4 \times 256 = 1.024\text{ cm}^3$$

Jadi, volume maksimum kotak tersebut adalah $1.024\text{ cm}^3$.
**Acuan:** siswa — siswa hal.166

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b02-d-medium-bt01-005
*orisinal | C3 | 2 langkah | jenis: ekstremum gerak vertikal*

Sebuah peluru kendali ditembakkan vertikal ke atas dengan persamaan lintasan ketinggian $s(t) = 120t - 5t^2$, dengan $s$ menyatakan tinggi dalam meter dan $t$ menyatakan waktu dalam detik. Ketinggian maksimum yang dapat dicapai peluru kendali tersebut adalah ....

- A. $360\text{ meter}$  
  <sub>Salah: Siswa salah memasukkan nilai waktu $t = 6$ (membagi dua waktu puncak).</sub>
- **B. $720\text{ meter}$** ✅  
  <sub>Benar: Tinggi maksimum tercapai saat kecepatan sesaat $v(t) = s'(t) = 0$. $s'(t) = 120 - 10t = 0 \implies 10t = 120 \implies t = 12\text{ detik}$. Ketinggian maksimum $s(12) = 120(12) - 5(12)^2 = 1.440 - 5(144) = 1.440 - 720 = 720\text{ meter}$.</sub>
- C. $600\text{ meter}$  
  <sub>Salah: Siswa salah mencari turunan dengan menganggap $s'(t) = 120 - 12t = 0 \implies t = 10$, sehingga $s(10) = 1200 - 500 = 700$, atau salah hitung aritmetika menghasilkan $600\text{ meter}$.</sub>
- D. $1.440\text{ meter}$  
  <sub>Salah: Siswa hanya menghitung suku linear $120 \times 12$ dan lupa mengurangkan suku perlambatan gravitasi $-5t^2$.</sub>

**Pembahasan:** Persamaan lintasan ketinggian peluru: $s(t) = 120t - 5t^2$.

Kecepatan sesaat merupakan turunan pertama dari fungsi posisi:
$$v(t) = s'(t) = 120 - 10t$$

Peluru mencapai tinggi maksimum ketika kecepatannya sama dengan nol ($v(t) = 0$):
$$120 - 10t = 0$$
$$10t = 120 \implies t = 12\text{ detik}$$

Substitusikan $t = 12$ ke dalam fungsi ketinggian $s(t)$:
$$s(12) = 120(12) - 5(12)^2$$
$$s(12) = 1.440 - 5(144)$$
$$s(12) = 1.440 - 720 = 720\text{ meter}$$

Jadi, ketinggian maksimum yang dicapai peluru kendali adalah $720\text{ meter}$.
**Acuan:** siswa — siswa hal.172

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b02-d-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: tinggi maksimum proyektil*

Sebuah roket mainan ditembakkan vertikal ke udara dan lintasannya setelah $t$ detik diberikan oleh persamaan $s(t) = 72t - 6t^2$, dengan $s$ dalam meter. Berapakah ketinggian maksimum yang dicapai roket tersebut sebelum mulai jatuh kembali ke tanah?

- **A. $216\text{ meter}$** ✅  
  <sub>Benar: Roket mencapai ketinggian maksimum saat kecepatan nol: $s'(t) = 72 - 12t = 0 \implies t = 6\text{ s}$. Ketinggian maksimum $s(6) = 72(6) - 6(6^2) = 432 - 216 = 216\text{ meter}$.</sub>
- B. $432\text{ meter}$  
  <sub>Salah: Hanya menghitung nilai suku pertama $72t$ pada saat $t = 6$ dan lupa mengurangkan dengan $6t^2$.</sub>
- C. $180\text{ meter}$  
  <sub>Salah: Keliru menentukan waktu puncak menjadi $t = 5$ detik, menghasilkan $s(5) = 360 - 150 = 210$ atau salah hitung aritmetika ke 180.</sub>
- D. $72\text{ meter}$  
  <sub>Salah: Menyimpulkan koefisien kecepatan awal $72$ sebagai ketinggian maksimum.</sub>

**Pembahasan:** Fungsi lintasan: $s(t) = 72t - 6t^2$.
1. Waktu saat mencapai tinggi puncak dicari dengan syarat $v(t) = 0$:
$$v(t) = s'(t) = 72 - 12t = 0 \implies 12t = 72 \implies t = 6\text{ detik}$$
2. Substitusikan $t = 6$ ke persamaan $s(t)$:
$$s(6) = 72(6) - 6(6^2) = 432 - 216 = 216\text{ meter}$$
Jadi, ketinggian maksimum yang dicapai adalah $216\text{ meter}$.
**Acuan:** siswa — siswa hal.172 Uji Kompetensi Bab 2 Bagian C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b02-d-medium-bt01-007
*variasi (angka) | C3 | 2 langkah | jenis: laju perubahan gerak vertikal*

Ketinggian sebuah pesawat tanpa awak (*drone*) di atas permukaan tanah setelah $t$ detik diterbangkan dinyatakan oleh fungsi $h(t) = 28t - 2t^2$ (dengan $h$ dalam meter dan $t$ dalam detik). Berapakah laju perubahan ketinggian *drone* pada saat $t = 8$ detik dan bagaimana arah pergerakannya saat itu?

- A. $4\text{ m/s}$, bergerak naik  
  <sub>Salah: Mengabaikan tanda negatif pada hasil turunan sehingga menyimpulkan *drone* bergerak naik.</sub>
- B. $-20\text{ m/s}$, bergerak turun  
  <sub>Salah: Salah melakukan diferensiasi dengan menganggap $h'(t) = 28 - 6t$ sehingga $28 - 48 = -20$.</sub>
- C. $-4\text{ m/s}$, bergerak naik  
  <sub>Salah: Benar menghitung nilai negatif tetapi salah mengartikan makna fisis nilai negatif.</sub>
- **D. $-4\text{ m/s}$, bergerak turun** ✅  
  <sub>Benar: Laju perubahan ketinggian adalah $h'(t) = 28 - 4t$. Pada $t = 8$, diperoleh $h'(8) = 28 - 4(8) = -4\text{ m/s}$. Tanda negatif menyatakan *drone* sedang bergerak turun.</sub>

**Pembahasan:** Fungsi ketinggian: $h(t) = 28t - 2t^2$.
1. Laju perubahan ketinggian diperoleh dari turunan pertama fungsi $h(t)$:
$$v(t) = h'(t) = 28 - 4t$$
2. Pada saat $t = 8\text{ detik}$:
$$h'(8) = 28 - 4(8) = 28 - 32 = -4\text{ m/s}$$
Karena bernilai negatif, arah pergerakan *drone* pada saat itu adalah sedang bergerak turun.
**Acuan:** siswa — siswa hal.172 Pengayaan

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b02-d-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: minimasi biaya rata-rata*

Biaya total untuk memproduksi $x$ unit suatu komoditas dinyatakan oleh persamaan $C(x) = 2x^2 + 80x + 1.800$ (dalam ribuan rupiah). Agar biaya rata-rata per unit barang menjadi minimum, banyak barang yang harus diproduksi adalah ....

- A. $60\text{ unit}$  
  <sub>Salah: Lupa membagi 1.800 dengan 2 sehingga $x^2 = 1.800$ atau salah faktor dua menjadi $x = 60$.</sub>
- **B. $30\text{ unit}$** ✅  
  <sub>Benar: Fungsi biaya rata-rata $A(x) = \frac{C(x)}{x} = 2x + 80 + \frac{1.800}{x}$. Syarat minimum $A'(x) = 2 - \frac{1.800}{x^2} = 0 \implies 2x^2 = 1.800 \implies x^2 = 900 \implies x = 30$ unit.</sub>
- C. $20\text{ unit}$  
  <sub>Salah: Salah menurunkan fungsi biaya langsung $C'(x) = 4x + 80 = 0$ dan mengambil nilai mutlak dari $x = -20$.</sub>
- D. $45\text{ unit}$  
  <sub>Salah: Kesalahan membagi saat menurunkan yaitu mengira $x^2 = \frac{1.800}{4} = 450$ atau salah hitung kuadrat.</sub>

**Pembahasan:** 1. Fungsi biaya rata-rata per unit ($A(x)$):
$$A(x) = \frac{C(x)}{x} = \frac{2x^2 + 80x + 1.800}{x} = 2x + 80 + 1.800x^{-1}$$
2. Menentukan nilai stasioner dengan $A'(x) = 0$:
$$A'(x) = 2 - 1.800x^{-2} = 0$$
$$2 = \frac{1.800}{x^2}$$
$$2x^2 = 1.800 \iff x^2 = 900$$
3. Karena jumlah produksi $x > 0$, maka:
$$x = \sqrt{900} = 30\text{ unit}$$
Uji turunan kedua: $A''(x) = \frac{3.600}{x^3} > 0$ untuk $x = 30$ (titik minimum).
Jadi, biaya rata-rata per unit mencapai minimum saat produksi sebanyak $30\text{ unit}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b02-d-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: optimasi kerangka bangun ruang*

Kawat sepanjang $120\text{ cm}$ akan digunakan seluruhnya untuk membuat kerangka sebuah balok tegak dengan alas berbentuk persegi (sisi alas $= x\text{ cm}$ dan tinggi balok $= t\text{ cm}$). Volume balok maksimum yang dapat dibentuk dari kawat tersebut adalah ....

- A. $750\text{ cm}^3$  
  <sub>Salah: Memilih $x = 5\text{ cm}$ sehingga volume $V = 5^2 \times (30 - 10) = 500$ atau salah hitung substitusi.</sub>
- **B. $1.000\text{ cm}^3$** ✅  
  <sub>Benar: Keliling kerangka balok beralas persegi: $4x + 4x + 4t = 120 \implies 2x + t = 30 \implies t = 30 - 2x$. Volume $V(x) = x^2(30 - 2x) = 30x^2 - 2x^3$. Syarat optimum $V'(x) = 60x - 6x^2 = 0 \implies 6x(10 - x) = 0 \implies x = 10\text{ cm}$. Maka $t = 30 - 2(10) = 10\text{ cm}$. Volume maksimum $V = 10 \times 10 \times 10 = 1.000\text{ cm}^3$.</sub>
- C. $2.000\text{ cm}^3$  
  <sub>Salah: Menggunakan nilai $t = 20$ karena salah mengeliminasi hubungan keliling menjadi $x + t = 30$.</sub>
- D. $1.200\text{ cm}^3$  
  <sub>Salah: Menghitung secara langsung dari pembagian panjang kawat dikali ukuran tanpa optimasi turunan.</sub>

**Pembahasan:** 1. Hubungan dimensi balok dengan panjang kawat:
Balok memiliki 4 rusuk panjang ($x$), 4 rusuk lebar ($x$), dan 4 rusuk tinggi ($t$).
$$4x + 4x + 4t = 120 \iff 8x + 4t = 120 \iff 2x + t = 30 \iff t = 30 - 2x$$
2. Fungsi volume balok:
$$V(x) = x \cdot x \cdot t = x^2(30 - 2x) = 30x^2 - 2x^3$$
3. Syarat volume maksimum ($V'(x) = 0$):
$$V'(x) = 60x - 6x^2 = 0$$
$$6x(10 - x) = 0$$
Karena ukuran sisi $x > 0$, maka $x = 10\text{ cm}$.
Tinggi balok $t = 30 - 2(10) = 10\text{ cm}$.
Volume maksimum balok adalah:
$$V = 10^2 \times 10 = 1.000\text{ cm}^3$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b02-d-medium-bt01-010
*variasi (konteks) | C4 | 3 langkah | jenis: dinamika gerak partikel*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = \frac{1}{3}t^3 - 4t^2 + 15t$, dengan $s$ dalam meter dan $t$ dalam detik. Kecepatan partikel pada saat percepatannya sama dengan nol adalah ....

- **A. $-1\text{ m/s}$** ✅  
  <sub>Benar: Kecepatan $v(t) = s'(t) = t^2 - 8t + 15$. Percepatan $a(t) = v'(t) = 2t - 8$. Nilai $a(t) = 0 \implies 2t - 8 = 0 \implies t = 4\text{ detik}$. Kecepatan saat $t = 4$ adalah $v(4) = 4^2 - 8(4) + 15 = 16 - 32 + 15 = -1\text{ m/s}$.</sub>
- B. $0\text{ m/s}$  
  <sub>Salah: Siswa keliru menganggap bahwa saat percepatan bernilai nol, kecepatan partikel juga pasti bernilai nol.</sub>
- C. $-5\text{ m/s}$  
  <sub>Salah: Siswa salah menjumlahkan hasil perhitungan $16 - 32 + 15$ menjadi $-5$.</sub>
- D. $3\text{ m/s}$  
  <sub>Salah: Siswa salah mencari pembuat nol percepatan menjadi $t = 2$, lalu menghitung $v(2) = 4 - 16 + 15 = 3\text{ m/s}$.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan kecepatan sesaat.
$$v(t) = s'(t) = t^2 - 8t + 15$$

Langkah 2: Menentukan persamaan percepatan sesaat dan mencari waktu $t$ saat $a(t) = 0$.
$$a(t) = v'(t) = 2t - 8$$
$$a(t) = 0 \implies 2t - 8 = 0 \implies 2t = 8 \implies t = 4\text{ detik}$$

Langkah 3: Menghitung kecepatan saat $t = 4\text{ detik}$.
$$v(4) = 4^2 - 8(4) + 15 = 16 - 32 + 15 = -1\text{ m/s}$$

Jadi, kecepatan partikel pada saat percepatannya nol adalah $-1\text{ m/s}$.
**Acuan:** siswa — siswa hal.165 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b02-d-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: kinematika gerak vertikal*

Sebuah anak panah ditembakkan vertikal ke udara dengan ketinggian setelah $t$ detik memenuhi persamaan $s(t) = 60t - 5t^2$ (jarak $s$ dalam meter). Ketinggian anak panah pada saat kecepatannya $20\text{ m/s}$ adalah ....

- A. $140\text{ meter}$  
  <sub>Salah: Siswa keliru menghitung $5 \times 4^2$ menjadi $100$ sehingga diperoleh $240 - 100 = 140\text{ meter}$.</sub>
- B. $100\text{ meter}$  
  <sub>Salah: Siswa salah menghitung waktu $t$ dari $60 - 10t = 20$ menjadi $t = 2$, sehingga $s(2) = 120 - 20 = 100\text{ meter}$.</sub>
- **C. $160\text{ meter}$** ✅  
  <sub>Benar: Kecepatan sesaat $v(t) = s'(t) = 60 - 10t$. Syarat kecepatan $20\text{ m/s}$: $60 - 10t = 20 \implies 10t = 40 \implies t = 4\text{ detik}$. Ketinggian saat $t = 4$: $s(4) = 60(4) - 5(4^2) = 240 - 80 = 160\text{ meter}$.</sub>
- D. $180\text{ meter}$  
  <sub>Salah: Siswa menghitung ketinggian maksimum saat $v(t) = 0$ ($t = 6$), yaitu $s(6) = 360 - 180 = 180\text{ meter}$.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi kecepatan sesaat anak panah dengan menurunkan fungsi posisi.
$$v(t) = s'(t) = 60 - 10t$$

Langkah 2: Menentukan nilai $t$ saat kecepatan $v(t) = 20\text{ m/s}$.
$$60 - 10t = 20$$
$$10t = 40 \implies t = 4\text{ detik}$$

Langkah 3: Menghitung ketinggian $s(4)$.
$$s(4) = 60(4) - 5(4)^2 = 240 - 5(16) = 240 - 80 = 160\text{ meter}$$

Jadi, ketinggian anak panah saat kecepatannya $20\text{ m/s}$ adalah $160\text{ meter}$.
**Acuan:** siswa — siswa hal.172 Uji Kompetensi Bab 2 Bagian C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b02-d-medium-bt01-012
*variasi (angka) | C4 | 3 langkah | jenis: luas maksimum kurva*

Sebuah persegi panjang dibuat dengan alas berada pada sumbu-$X$ dan simetris terhadap sumbu-$Y$, sedangkan dua titik sudut bagian atasnya terletak pada kurva parabola $y = 54 - 2x^2$ di atas sumbu-$X$. Luas maksimum persegi panjang tersebut adalah ....

- A. $108\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengalikan panjang alas dengan $2$, hanya menggunakan panjang alas sebesar $x$ sehingga diperoleh luas separuh yaitu $108$.</sub>
- **B. $216\text{ satuan luas}$** ✅  
  <sub>Benar: Koordinat titik sudut kanan atas adalah $(x, y) = (x, 54 - 2x^2)$ dengan $x > 0$. Panjang alas $= 2x$ dan tinggi $= 54 - 2x^2$. Luas $L(x) = 2x(54 - 2x^2) = 108x - 4x^3$. Stasioner: $L'(x) = 108 - 12x^2 = 0 \implies x^2 = 9 \implies x = 3$. Luas maksimum $L(3) = 108(3) - 4(27) = 324 - 108 = 216\text{ satuan luas}$.</sub>
- C. $144\text{ satuan luas}$  
  <sub>Salah: Siswa salah mencari turunan $108 - 12x^2 = 0$ menjadi $x^2 = 4 \implies x = 2$, lalu menghitung $L(2) = 2(2)(54 - 8) = 184$ atau keliru hitung menjadi $144$.</sub>
- D. $288\text{ satuan luas}$  
  <sub>Salah: Siswa salah menyubstitusikan nilai $y$ saat $x = 0$ ($y = 54$) dan mengalikannya dengan panjang alas $2x = 6$ sehingga menghasilkan nilai yang salah.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi luas persegi panjang.
Karena persegi panjang simetris terhadap sumbu-$Y$, panjang alas adalah $2x$ dan tingginya adalah $y = 54 - 2x^2$ untuk $x > 0$.
$$L(x) = 2x \cdot (54 - 2x^2) = 108x - 4x^3$$

Langkah 2: Menentukan nilai $x$ agar luas maksimum menggunakan $L'(x) = 0$.
$$L'(x) = 108 - 12x^2 = 0$$
$$12x^2 = 108$$
$$x^2 = 9 \implies x = 3\quad (\text{karena } x > 0)$$

Langkah 3: Menghitung luas maksimum.
$$L(3) = 108(3) - 4(3)^3 = 324 - 4(27) = 324 - 108 = 216\text{ satuan luas}$$

Jadi, luas maksimum persegi panjang tersebut adalah $216\text{ satuan luas}$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b02-d-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: keuntungan maksimum perusahaan*

Sebuah usaha rumahan memproduksi $x$ lusin suvenir. Penerimaan total dari penjualan dinyatakan oleh $R(x) = 140x - x^2$ dan biaya total produksi dinyatakan oleh $C(x) = x^2 + 20x + 200$ (keduanya dalam ribuan rupiah). Jumlah suvenir yang harus diproduksi agar keuntungan mencapai maksimum adalah ....

- A. $70\text{ lusin}$  
  <sub>Salah: Siswa memaksimumkan fungsi penerimaan $R(x)$ saja dengan menyelesaikan $R'(x) = 140 - 2x = 0 \implies x = 70$.</sub>
- B. $60\text{ lusin}$  
  <sub>Salah: Siswa hanya menurunkan fungsi $120x$ tanpa membagi dengan turunan dari koefisien kuadrat $2x^2$ (lupa faktor $2$ dari turunan $-2x^2$).</sub>
- C. $25\text{ lusin}$  
  <sub>Salah: Siswa salah mengurangkan koefisien $x$ menjadi $140 - 20 = 100$, sehingga $-4x + 100 = 0 \implies x = 25$.</sub>
- **D. $30\text{ lusin}$** ✅  
  <sub>Benar: Keuntungan $P(x) = R(x) - C(x) = (140x - x^2) - (x^2 + 20x + 200) = -2x^2 + 120x - 200$. Keuntungan maksimum tercapai saat $P'(x) = 0 \implies -4x + 120 = 0 \implies 4x = 120 \implies x = 30\text{ lusin}$.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi keuntungan $P(x) = R(x) - C(x)$.
$$P(x) = (140x - x^2) - (x^2 + 20x + 200)$$
$$P(x) = -2x^2 + 120x - 200$$

Langkah 2: Mencari nilai $x$ agar keuntungan maksimum dengan syarat $P'(x) = 0$.
$$P'(x) = -4x + 120 = 0$$
$$4x = 120$$
$$x = 30$$

Jadi, banyak suvenir yang harus diproduksi agar memperoleh keuntungan maksimum adalah $30\text{ lusin}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b02-d-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: percepatan sudut rotasi*

Posisi sudut sebuah roda yang berputar dinyatakan oleh fungsi $\theta(t) = 4t + 2\cos(2t)$ dengan $\theta$ dalam radian dan $t$ dalam detik. Besar percepatan sudut roda tersebut pada saat $t = \frac{\pi}{2}\text{ detik}$ adalah ....

- A. $0\text{ rad/s}^2$  
  <sub>Salah: Siswa keliru menganggap $\cos(\pi) = 0$ atau menyamakan perhitungan dengan $\sin(\pi) = 0$.</sub>
- B. $-8\text{ rad/s}^2$  
  <sub>Salah: Siswa salah mengevaluasi nilai $\cos(\pi) = 1$ sehingga $-8(1) = -8$.</sub>
- **C. $8\text{ rad/s}^2$** ✅  
  <sub>Benar: Kecepatan sudut $\omega(t) = \theta'(t) = 4 - 4\sin(2t)$. Percepatan sudut $\alpha(t) = \omega'(t) = -8\cos(2t)$. Pada saat $t = \frac{\pi}{2}$, didapat $\alpha\left(\frac{\pi}{2}\right) = -8\cos\left(2 \cdot \frac{\pi}{2}\right) = -8\cos(\pi) = -8(-1) = 8\text{ rad/s}^2$.</sub>
- D. $4\text{ rad/s}^2$  
  <sub>Salah: Siswa lupa menerapkan aturan rantai saat menurunkan $2\cos(2t)$, sehingga turunan keduanya hanya $-2\cos(2t)$ yang menghasilkan $-2(-1) = 2$ atau keliru menghitung nilai konstanta awal.</sub>

**Pembahasan:** Langkah 1: Menentukan kecepatan sudut $\omega(t)$ dengan mencari turunan pertama $\theta(t)$.
$$\omega(t) = \theta'(t) = 4 + 2(-\sin(2t) \cdot 2) = 4 - 4\sin(2t)$$

Langkah 2: Menentukan percepatan sudut $\alpha(t)$ dengan mencari turunan kedua $\theta(t)$.
$$\alpha(t) = \omega'(t) = -4(\cos(2t) \cdot 2) = -8\cos(2t)$$

Langkah 3: Menghitung percepatan sudut saat $t = \frac{\pi}{2}\text{ detik}$.
$$\alpha\left(\frac{\pi}{2}\right) = -8\cos\left(2 \cdot \frac{\pi}{2}\right) = -8\cos(\pi)$$
Karena $\cos(\pi) = -1$, maka:
$$\alpha\left(\frac{\pi}{2}\right) = -8(-1) = 8\text{ rad/s}^2$$

Jadi, besar percepatan sudut roda tersebut adalah $8\text{ rad/s}^2$.
**Acuan:** siswa — siswa hal.165

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b02-d-medium-bt01-015
*variasi (angka) | C3 | 3 langkah | jenis: optimasi luas penampang*

Sebuah talang air dibuat dari selembar pelat seng berpenampang datar dengan lebar $40\text{ cm}$. Kedua tepi sisi seng ditekuk tegak lurus ke atas dengan ketinggian yang sama, yaitu $x\text{ cm}$. Luas penampang maksimum talang air yang terbentuk adalah ....

- A. $100\text{ cm}^2$  
  <sub>Salah: Siswa salah memodelkan lebar alas menjadi $40 - x$ sehingga memperoleh titik balik yang keliru.</sub>
- B. $400\text{ cm}^2$  
  <sub>Salah: Siswa mengalikan langsung seluruh lebar seng dengan tinggi optimum ($40 \times 10$).</sub>
- **C. $200\text{ cm}^2$** ✅  
  <sub>Benar: Lebar alas talang adalah $(40 - 2x)\text{ cm}$ dan tingginya $x\text{ cm}$, sehingga luas penampang dinyatakan oleh $L(x) = x(40 - 2x) = 40x - 2x^2$. Nilai stasioner tercapai saat $L'(x) = 0 \Leftrightarrow 40 - 4x = 0 \Leftrightarrow x = 10\text{ cm}$. Luas maksimumnya adalah $L(10) = 40(10) - 2(10)^2 = 400 - 200 = 200\text{ cm}^2$.</sub>
- D. $150\text{ cm}^2$  
  <sub>Salah: Siswa salah menghitung turunan pertama menjadi $40 - 2x = 0$ dan salah menyubstitusikan nilai ke fungsi luas.</sub>

**Pembahasan:** Misalkan tinggi tekukan adalah $x\text{ cm}$. Karena kedua sisi dilipat sebesar $x$, lebar dasar penampang adalah $40 - 2x\text{ cm}$.
Fungsi luas penampang:
$$L(x) = (40 - 2x)x = 40x - 2x^2$$
Agar luas penampang maksimum, turunan pertama sama dengan nol:
$$L'(x) = 40 - 4x = 0 \implies 4x = 40 \implies x = 10$$
Substitusikan $x = 10$ ke $L(x)$:
$$L(10) = 40(10) - 2(10)^2 = 400 - 200 = 200\text{ cm}^2$$
Jadi, luas penampang maksimumnya adalah $200\text{ cm}^2$.
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b02-d-medium-bt01-016
*orisinal | C4 | 3 langkah | jenis: biaya marjinal minimum*

Biaya total (dalam ribuan rupiah) untuk memproduksi $x$ unit barang ditentukan oleh fungsi $C(x) = x^3 - 12x^2 + 60x + 200$. Biaya marjinal didefinisikan sebagai laju perubahan sesaat biaya total terhadap banyak barang yang diproduksi, $MC(x) = C'(x)$. Nilai biaya marjinal minimum yang dapat dicapai perusahaan adalah ....

- A. $60$ ribu rupiah per unit  
  <sub>Salah: Siswa hanya mengambil konstanta dari fungsi biaya marjinal saat $x = 0$.</sub>
- B. $4$ ribu rupiah per unit  
  <sub>Salah: Siswa menjawab jumlah unit produk ($x = 4$) bukan nilai biaya marjinalnya.</sub>
- **C. $12$ ribu rupiah per unit** ✅  
  <sub>Benar: Biaya marjinal adalah $MC(x) = C'(x) = 3x^2 - 24x + 60$. Biaya marjinal mencapai nilai minimum saat turunan pertamanya nol, yaitu $MC'(x) = 6x - 24 = 0 \Leftrightarrow x = 4$. Nilai minimum tersebut adalah $MC(4) = 3(4)^2 - 24(4) + 60 = 48 - 96 + 60 = 12$ ribu rupiah per unit.</sub>
- D. $24$ ribu rupiah per unit  
  <sub>Salah: Siswa salah menghitung nilai fungsi stasioner $MC(4)$ menjadi $3(16) - 24 + 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus fungsi biaya marjinal $MC(x)$:
$$MC(x) = C'(x) = 3x^2 - 24x + 60$$

Langkah 2: Menentukan nilai $x$ agar $MC(x)$ minimum:
$$MC'(x) = 6x - 24 = 0 \implies 6x = 24 \implies x = 4$$

Langkah 3: Menghitung nilai minimum biaya marjinal pada $x = 4$:
$$MC(4) = 3(4)^2 - 24(4) + 60 = 3(16) - 96 + 60 = 48 - 96 + 60 = 12$$
Jadi, nilai biaya marjinal minimum adalah $12$ ribu rupiah per unit.
**Acuan:** siswa — siswa hal.170

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b02-d-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: laju perubahan suhu*

Suhu suatu ruangan penyimpan vaksin (dalam $^{\circ}\text{C}$) dipantau selama 12 jam dan dimodelkan oleh fungsi $T(t) = 20 + 4\sin\left(\frac{\pi t}{6}\right)$, dengan $t$ menyatakan waktu dalam jam setelah pemantauan dimulai ($0 \le t \le 12$). Laju perubahan suhu ruangan pada saat $t = 2\text{ jam}$ adalah ....

- A. $\frac{2}{3}\pi\,^{\circ}\text{C/jam}$  
  <sub>Salah: Siswa lupa mengalikan dengan nilai $\cos(\pi/3) = 1/2$.</sub>
- **B. $\frac{1}{3}\pi\,^{\circ}\text{C/jam}$** ✅  
  <sub>Benar: Turunan dari fungsi suhu adalah $T'(t) = 4 \cdot \frac{\pi}{6}\cos\left(\frac{\pi t}{6}\right) = \frac{2\pi}{3}\cos\left(\frac{\pi t}{6}\right)$. Pada saat $t = 2$, diperoleh $T'(2) = \frac{2\pi}{3}\cos\left(\frac{2\pi}{6}\right) = \frac{2\pi}{3}\cos\left(\frac{\pi}{3}\right) = \frac{2\pi}{3} \cdot \frac{1}{2} = \frac{1}{3}\pi\,^{\circ}\text{C/jam}$.</sub>
- C. $\frac{\sqrt{3}}{3}\pi\,^{\circ}\text{C/jam}$  
  <sub>Salah: Siswa tertukar menggunakan nilai $\sin(\pi/3) = \frac{1}{2}\sqrt{3}$ alih-alih kosinus.</sub>
- D. $2\,^{\circ}\text{C/jam}$  
  <sub>Salah: Siswa lupa mengalikan dengan turunan sudut dalam (faktor $\pi/6$).</sub>

**Pembahasan:** Fungsi suhu ruangan: $T(t) = 20 + 4\sin\left(\frac{\pi t}{6}\right)$.
Laju perubahan suhu merupakan turunan pertama $T'(t)$ terhadap waktu $t$:
$$T'(t) = 4 \cdot \frac{\mathrm{d}}{\mathrm{d}t}\left[\sin\left(\frac{\pi t}{6}\right)\right] = 4 \cdot \frac{\pi}{6} \cos\left(\frac{\pi t}{6}\right) = \frac{2\pi}{3}\cos\left(\frac{\pi t}{6}\right)$$
Substitusikan nilai $t = 2$:
$$T'(2) = \frac{2\pi}{3}\cos\left(\frac{2\pi}{6}\right) = \frac{2\pi}{3}\cos\left(\frac{\pi}{3}\right) = \frac{2\pi}{3} \cdot \frac{1}{2} = \frac{1}{3}\pi\,^{\circ}\text{C/jam}$$
Jadi, laju perubahan suhu ruangan saat $t = 2\text{ jam}$ adalah $\frac{1}{3}\pi\,^{\circ}\text{C/jam}$.
**Acuan:** siswa — siswa hal.171

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b02-d-medium-bt01-018
*variasi (angka) | C4 | 3 langkah | jenis: optimasi dimensi kotak*

Sebuah kotak tanpa tutup dibuat dari selembar karton berbentuk persegi dengan panjang sisi $30\text{ cm}$. Pembuatan dilakukan dengan cara memotong persegi identik berukuran $x \times x\text{ cm}^2$ pada keempat pojok karton, kemudian melipat sisi-sisinya ke atas. Tentukan ukuran kotak (panjang, lebar, dan tinggi) agar volume kotak yang terbentuk bernilai maksimum.

- A. Panjang $10\text{ cm}$, lebar $10\text{ cm}$, dan tinggi $10\text{ cm}$  
  <sub>Salah: Siswa salah membagi sisi karton menjadi tiga bagian sama besar ($x = 10\text{ cm}$).</sub>
- B. Panjang $15\text{ cm}$, lebar $15\text{ cm}$, dan tinggi $7,5\text{ cm}$  
  <sub>Salah: Siswa mengabaikan faktor kuadrat pada pelipatan dua sisi dan memotong tepat seperempat lebar karton.</sub>
- C. Panjang $24\text{ cm}$, lebar $24\text{ cm}$, dan tinggi $3\text{ cm}$  
  <sub>Salah: Siswa langsung memakai tinggi $x = 3\text{ cm}$ dari contoh soal acuan tanpa menghitung turunan fungsi baru.</sub>
- **D. Panjang $20\text{ cm}$, lebar $20\text{ cm}$, dan tinggi $5\text{ cm}$** ✅  
  <sub>Benar: Volume kotak adalah $V(x) = x(30 - 2x)^2 = 4x^3 - 120x^2 + 900x$. Turunan pertamanya $V'(x) = 12x^2 - 240x + 900 = 0 \iff x^2 - 20x + 75 = 0 \iff (x - 5)(x - 15) = 0$. Karena $0 < x < 15$, maka $x = 5\text{ cm}$. Sehingga tinggi $= 5\text{ cm}$, panjang $= 30 - 2(5) = 20\text{ cm}$, dan lebar $= 20\text{ cm}$.</sub>

**Pembahasan:** Misalkan $x$ adalah tinggi kotak (panjang sisi persegi pojok yang dipotong).
Dimensi kotak setelah dilipat:
- Tinggi ($t$) $= x$
- Panjang ($p$) $= 30 - 2x$
- Lebar ($l$) $= 30 - 2x$

Fungsi volume kotak:
$$V(x) = p \cdot l \cdot t = (30 - 2x)^2 \cdot x$$
$$V(x) = (900 - 120x + 4x^2)x = 4x^3 - 120x^2 + 900x$$

Syarat volume stasioner ($V'(x) = 0$):
$$V'(x) = 12x^2 - 240x + 900 = 0$$
Bagi kedua ruas dengan 12:
$$x^2 - 20x + 75 = 0$$
$$(x - 5)(x - 15) = 0$$
$$x = 5 \quad \text{atau} \quad x = 15$$

Karena panjang sisi harus positif ($30 - 2x > 0 \implies x < 15$), nilai yang memenuhi adalah $x = 5\text{ cm}$.

Ukuran kotak agar volume maksimum:
- Panjang $= 30 - 2(5) = 20\text{ cm}$
- Lebar $= 30 - 2(5) = 20\text{ cm}$
- Tinggi $= 5\text{ cm}$
**Acuan:** siswa — siswa hal.166 Contoh Soal 2.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b02-d-medium-bt01-019
*variasi (angka) | C3 | 2 langkah | jenis: laju perubahan konsentrasi*

Konsentrasi suatu obat dalam aliran darah pasien setelah $t$ jam disuntikkan dimodelkan oleh fungsi $C(t) = \frac{50t}{t + 4}\text{ mg/L}$. Laju perubahan konsentrasi obat terhadap waktu pada saat $t = 6\text{ jam}$ adalah ....

- A. $5\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Siswa menghitung laju rata-rata dari awal pemberian obat sampai jam ke-6: $\frac{C(6)}{6} = \frac{30}{6} = 5$.</sub>
- B. $3\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Siswa menghitung nilai konsentrasi obat dibagi 10, bukan turunan fungsi: $C(6) = 30$, lalu $30 / 10 = 3$.</sub>
- C. $20\text{ mg/(L}\cdot\text{jam)}$  
  <sub>Salah: Siswa lupa mengkuadratkan penyebut pada rumus turunan pembagian: $\frac{200}{6 + 4} = 20$.</sub>
- **D. $2\text{ mg/(L}\cdot\text{jam)}$** ✅  
  <sub>Benar: Turunan pertama $C'(t) = \frac{50(t + 4) - 50t(1)}{(t + 4)^2} = \frac{200}{(t + 4)^2}$. Pada saat $t = 6$, $C'(6) = \frac{200}{(6 + 4)^2} = \frac{200}{100} = 2\text{ mg/(L}\cdot\text{jam)}$.</sub>

**Pembahasan:** Laju perubahan konsentrasi obat terhadap waktu dinyatakan oleh turunan pertama fungsi $C(t)$, yaitu $C'(t)$.

Menggunakan aturan turunan bentuk pecahan $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
- $u = 50t \implies u' = 50$
- $v = t + 4 \implies v' = 1$

$$C'(t) = \frac{50(t + 4) - 50t(1)}{(t + 4)^2}$$
$$C'(t) = \frac{50t + 200 - 50t}{(t + 4)^2} = \frac{200}{(t + 4)^2}$$

Substitusikan $t = 6\text{ jam}$:
$$C'(6) = \frac{200}{(6 + 4)^2} = \frac{200}{10^2} = \frac{200}{100} = 2\text{ mg/(L}\cdot\text{jam)}$$
**Acuan:** siswa — siswa hal.170 Uji Kompetensi Bab 2 Bagian A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b02-d-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: minimasi biaya proyek*

Sebuah proyek perbaikan jalan dapat diselesaikan dalam $x$ hari dengan biaya proyek per hari sebesar $\left(3x - 180 + \frac{3.000}{x}\right)$ juta rupiah. Biaya minimum proyek perbaikan jalan tersebut adalah ....

- **A. Rp300.000.000,00** ✅  
  <sub>Benar: Total biaya proyek adalah $B(x) = x\left(3x - 180 + \frac{3.000}{x}\right) = 3x^2 - 180x + 3.000$ juta rupiah. Nilai minimum tercapai saat $B'(x) = 6x - 180 = 0$, sehingga $x = 30$ hari. Biaya minimumnya adalah $B(30) = 3(30)^2 - 180(30) + 3.000 = 2.700 - 5.400 + 3.000 = 300$ juta rupiah atau Rp300.000.000,00.</sub>
- B. Rp450.000.000,00  
  <sub>Salah: Siswa melakukan kesalahan perhitungan aritmetika saat menghitung $B(30)$, yaitu menghitung $2.700 - 5.250 + 3.000 = 450$ juta rupiah.</sub>
- C. Rp975.000.000,00  
  <sub>Salah: Siswa salah menurunkan $3x^2$ menjadi $12x$, sehingga menyelesaikan $12x - 180 = 0$ dan memperoleh $x = 15$ hari dengan biaya $B(15) = 975$ juta rupiah.</sub>
- D. Rp600.000.000,00  
  <sub>Salah: Siswa salah memasukkan nilai $x$ menjadi dua kali lipat dari titik stasioner pada perhitungan biaya per hari.</sub>

**Pembahasan:** Misalkan $B(x)$ menyatakan total biaya proyek selama $x$ hari.
$$B(x) = x \cdot \left(3x - 180 + \frac{3.000}{x}\right) = 3x^2 - 180x + 3.000 \text{ (dalam juta rupiah)}$$

Agar biaya minimum, turunan pertama $B'(x)$ harus bernilai nol:
$$B'(x) = 6x - 180 = 0$$
$$6x = 180 \implies x = 30$$

Substitusikan $x = 30$ ke dalam fungsi biaya total $B(x)$:
$$\begin{aligned} B(30) &= 3(30)^2 - 180(30) + 3.000 \\ &= 3(900) - 5.400 + 3.000 \\ &= 2.700 - 5.400 + 3.000 \\ &= 300 \text{ juta rupiah} \end{aligned}$$

Jadi, biaya minimum proyek perbaikan jalan tersebut adalah Rp300.000.000,00.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b02-d-hard-bt01-001
*variasi (angka) | C5 | 5 langkah | jenis: optimasi ekonomi*

Sebuah pabrik manufaktur memodelkan total pendapatan $R(Q)$ dan total biaya produksi $C(Q)$ dengan persamaan $R(Q) = -5Q^2 + 1.125Q$ dan $C(Q) = Q^3 - 50Q^2 + 1.500Q + 1.000$, dengan $Q$ menyatakan jumlah barang dalam ribuan unit serta $R(Q)$ dan $C(Q)$ dalam juta rupiah. Berdasarkan model tersebut, tentukan jumlah produksi $Q$ agar pabrik memperoleh keuntungan maksimum dan tentukan besar keuntungan maksimum tersebut.

- A. $5.000\text{ unit}$ dengan kerugian $\text{Rp}1.875.000.000,00$  
  <sub>Salah: Siswa mengambil titik stasioner minimum lokal ($Q = 5$) yang menghasilkan titik balik rugi maksimum.</sub>
- B. $15.000\text{ unit}$ dengan keuntungan $\text{Rp}1.500.000.000,00$  
  <sub>Salah: Siswa mengambil titik belok $P''(Q) = 0$ yaitu $Q = 15$ sebagai titik keuntungan maksimum.</sub>
- **C. $25.000\text{ unit}$ dengan keuntungan $\text{Rp}2.125.000.000,00$** ✅  
  <sub>Benar: Fungsi keuntungan $P(Q) = R(Q) - C(Q) = -Q^3 + 45Q^2 - 375Q - 1.000$. Turunan pertama $P'(Q) = -3Q^2 + 90Q - 375 = -3(Q - 5)(Q - 25) = 0$, diperoleh titik kritis $Q = 5$ dan $Q = 25$. Turunan kedua $P''(Q) = -6Q + 90$; untuk $Q = 25$, $P''(25) = -60 < 0$ (maksimum). Keuntungan maksimum $P(25) = -(25)^3 + 45(25)^2 - 375(25) - 1.000 = 2.125$ juta rupiah, dengan $Q = 25$ ribu unit ($25.000$ unit).</sub>
- D. $25.000\text{ unit}$ dengan keuntungan $\text{Rp}3.125.000.000,00$  
  <sub>Salah: Siswa lupa mengurangkan konstanta biaya tetap ($1.000$ juta rupiah) pada fungsi biaya saat menghitung laba.</sub>

**Pembahasan:** Fungsi keuntungan dinyatakan oleh:
$$P(Q) = R(Q) - C(Q)$$
$$P(Q) = (-5Q^2 + 1.125Q) - (Q^3 - 50Q^2 + 1.500Q + 1.000)$$
$$P(Q) = -Q^3 + 45Q^2 - 375Q - 1.000$$

Syarat stasioner tercapai saat $P'(Q) = 0$:
$$P'(Q) = -3Q^2 + 90Q - 375 = 0$$
$$-3(Q^2 - 30Q + 125) = 0$$
$$-3(Q - 5)(Q - 25) = 0$$
Diperoleh $Q = 5$ atau $Q = 25$.

Uji jenis stasioner dengan turunan kedua:
$$P''(Q) = -6Q + 90$$
- Untuk $Q = 5$: $P''(5) = -6(5) + 90 = 60 > 0$ (titik minimum lokal).
- Untuk $Q = 25$: $P''(25) = -6(25) + 90 = -60 < 0$ (titik maksimum lokal).

Jadi, keuntungan maksimum terjadi saat $Q = 25$ (dalam ribuan unit, yaitu $25.000$ unit).
Besar keuntungan maksimum:
$$P(25) = -(25)^3 + 45(25)^2 - 375(25) - 1.000$$
$$P(25) = -15.625 + 28.125 - 9.375 - 1.000 = 2.125\text{ juta rupiah}$$
$$P(25) = \text{Rp}2.125.000.000,00$$
**Acuan:** siswa — siswa hal.171 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b02-d-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: optimasi biaya produksi*

Sebuah tangki penampung air berbentuk tabung silinder tanpa tutup dirancang memiliki kapasitas volume sebesar $16\pi\text{ m}^3$. Biaya material pembuatan alas tabung adalah Rp$200.000,00$ per $\text{m}^2$, sedangkan biaya material untuk dinding selimut adalah Rp$100.000,00$ per $\text{m}^2$. Agar total biaya material yang dikeluarkan seminimum mungkin, ukuran jari-jari alas ($r$) dan tinggi ($h$) tabung tersebut berturut-turut adalah ....

- A. $r = 2\text{ m}$ dan $h = 2\text{ m}$  
  <sub>Salah: Siswa mengabaikan faktor bobot biaya yang berbeda antara alas dan selimut sehingga menganggap $h = r$.</sub>
- **B. $r = 2\text{ m}$ dan $h = 4\text{ m}$** ✅  
  <sub>Benar: Volume $V = \pi r^2 h = 16\pi \implies h = \frac{16}{r^2}$. Biaya total $C(r) = 200.000(\pi r^2) + 100.000(2\pi rh) = 100.000\pi\left(2r^2 + \frac{32}{r}\right)$. Turunan $C'(r) = 100.000\pi\left(4r - \frac{32}{r^2}\right) = 0 \implies 4r^3 = 32 \implies r = 2\text{ m}$. Maka $h = \frac{16}{2^2} = 4\text{ m}$.</sub>
- C. $r = 1\text{ m}$ dan $h = 16\text{ m}$  
  <sub>Salah: Siswa menyamakan turunan fungsi luas selimut saja terhadap jari-jari tanpa melibatkan fungsi biaya alas.</sub>
- D. $r = 4\text{ m}$ dan $h = 1\text{ m}$  
  <sub>Salah: Siswa salah menyelesaikan persamaan stasioner menjadi $r^2 = 16 \implies r = 4$.</sub>

**Pembahasan:** 1. Hubungan volume silinder:
$$V = \pi r^2 h = 16\pi \implies h = \frac{16}{r^2}$$

2. Fungsi biaya total material (dalam ribuan rupiah):
$$C(r) = 200 \cdot (\pi r^2) + 100 \cdot (2\pi r h)$$
Substitusikan $h = \frac{16}{r^2}$:
$$C(r) = 200\pi r^2 + 200\pi r \left(\frac{16}{r^2}\right) = 200\pi r^2 + \frac{3.200\pi}{r}$$

3. Syarat biaya minimum tercapai saat $C'(r) = 0$:
$$C'(r) = 400\pi r - \frac{3.200\pi}{r^2} = 0$$
$$400\pi r = \frac{3.200\pi}{r^2}$$
$$r^3 = \frac{3.200}{400} = 8 \implies r = 2\text{ m}$$

4. Menentukan tinggi tabung:
$$h = \frac{16}{r^2} = \frac{16}{2^2} = 4\text{ m}$$

Uji turunan kedua:
$$C''(r) = 400\pi + \frac{6.400\pi}{r^3}$$
Untuk $r = 2$, $C''(2) = 400\pi + 800\pi = 1.200\pi > 0$ (terbukti nilai minimum).

Jadi, ukuran tabung agar biaya minimum adalah $r = 2\text{ m}$ dan $h = 4\text{ m}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b02-d-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: laju perubahan jarak*

Dua buah kapal laut $A$ dan $B$ bergerak pada lintasan lurus yang saling tegak lurus. Pada saat $t = 0$, kapal $A$ berada tepat di sebuah pelabuhan $O$ dan bergerak lurus ke arah timur dengan laju tetap $16\text{ km/jam}$. Pada saat yang sama, kapal $B$ berada $50\text{ km}$ di sebelah utara pelabuhan $O$ dan bergerak lurus ke arah selatan menuju pelabuhan $O$ dengan laju tetap $12\text{ km/jam}$. Jarak terdekat yang dapat dicapai antara kapal $A$ dan kapal $B$ adalah ....

- A. $30\text{ km}$  
  <sub>Salah: Siswa menghitung jarak kapal $B$ ke pelabuhan saat $t = 1,5$ yaitu $50 - 12(1,5) = 32\text{ km}$, lalu keliru mengira hasilnya $30\text{ km}$.</sub>
- B. $50\text{ km}$  
  <sub>Salah: Siswa mengira jarak terdekat adalah jarak awal saat kedua kapal mulai diamati ($t = 0$).</sub>
- **C. $40\text{ km}$** ✅  
  <sub>Benar: Posisi kapal $A$ terhadap pelabuhan adalah $(16t, 0)$ dan kapal $B$ adalah $(0, 50 - 12t)$. Kuadrat jarak $f(t) = (16t)^2 + (50 - 12t)^2 = 400t^2 - 1.200t + 2.500$. Nilai minimum terjadi saat $f'(t) = 800t - 1.200 = 0 \implies t = 1,5\text{ jam}$. Jarak minimum $D = \sqrt{f(1,5)} = \sqrt{400(2,25) - 1.200(1,5) + 2.500} = \sqrt{1.600} = 40\text{ km}$.</sub>
- D. $24\text{ km}$  
  <sub>Salah: Siswa hanya menghitung jarak tempuh kapal $A$ saat mencapai kondisi minimum ($16 \times 1,5 = 24\text{ km}$).</sub>

**Pembahasan:** 1. Modelkan posisi kedua kapal pada bidang koordinat dengan pelabuhan sebagai titik asal $(0,0)$:
- Kapal $A$ bergerak ke timur (sumbu-$X$ positif): $x_A(t) = 16t$ dan $y_A(t) = 0$.
- Kapal $B$ bergerak ke selatan dari titik $(0, 50)$: $x_B(t) = 0$ dan $y_B(t) = 50 - 12t$.

2. Jarak antara kapal $A$ dan kapal $B$ setelah $t$ jam adalah $D(t)$:
$$D(t) = \sqrt{(x_A - x_B)^2 + (y_A - y_B)^2}$$
$$D^2(t) = (16t - 0)^2 + (0 - (50 - 12t))^2$$
$$D^2(t) = 256t^2 + (2.500 - 1.200t + 144t^2)$$
$$D^2(t) = 400t^2 - 1.200t + 2.500$$

3. Misalkan $f(t) = D^2(t)$. Jarak $D(t)$ mencapai minimum pada saat yang sama dengan $f(t)$ mencapai minimum, yaitu saat $f'(t) = 0$:
$$f'(t) = 800t - 1.200 = 0$$
$$800t = 1.200 \implies t = \frac{1.200}{800} = 1,5\text{ jam}$$

4. Menghitung jarak minimum:
Substitusikan $t = 1,5$ ke dalam fungsi kuadrat jarak:
$$f(1,5) = 400(1,5)^2 - 1.200(1,5) + 2.500$$
$$f(1,5) = 400(2,25) - 1.800 + 2.500$$
$$f(1,5) = 900 - 1.800 + 2.500 = 1.600$$
Maka jarak minimum adalah:
$$D = \sqrt{1.600} = 40\text{ km}$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b02-d-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: optimasi luas gabungan geometri*

Seutas kawat dengan panjang $40\text{ cm}$ dipotong menjadi dua bagian. Potongan pertama ditekuk untuk membentuk sebuah persegi, sedangkan potongan kedua ditekuk untuk membentuk sebuah lingkaran. Agar jumlah luas persegi dan lingkaran tersebut minimum, perbandingan panjang sisi persegi ($s$) terhadap jari-jari lingkaran ($r$) adalah ....

- **A. $2 : 1$** ✅  
  <sub>Benar: Keliling kawat $4s + 2\pi r = 40 \implies s = \frac{40 - 2\pi r}{4} = 10 - \frac{1}{2}\pi r$. Luas gabungan $L(r) = s^2 + \pi r^2 = \left(10 - \frac{1}{2}\pi r\right)^2 + \pi r^2$. Turunan $L'(r) = 2\left(10 - \frac{1}{2}\pi r\right)\left(-\frac{1}{2}\pi\right) + 2\pi r = -\pi\left(10 - \frac{1}{2}\pi r\right) + 2\pi r = -\pi s + 2\pi r = 0 \implies 2\pi r = \pi s \implies s = 2r$. Maka rasio $s : r = 2 : 1$.</sub>
- B. $\pi : 2$  
  <sub>Salah: Siswa terbalik dalam menyederhanakan turunan implisit dari persamaan stasioner.</sub>
- C. $4 : \pi$  
  <sub>Salah: Siswa membandingkan keliling total bangun alih-alih menurunkan fungsi luas gabungan.</sub>
- D. $1 : 1$  
  <sub>Salah: Siswa mengira luas minimum terjadi ketika sisi persegi sama panjang dengan jari-jari lingkaran.</sub>

**Pembahasan:** 1. Misalkan panjang sisi persegi adalah $s$ dan jari-jari lingkaran adalah $r$.
Panjang kawat total:
$$4s + 2\pi r = 40$$
$$s = \frac{40 - 2\pi r}{4} = 10 - \frac{1}{2}\pi r$$

2. Jumlah luas kedua bangun datar dinyatakan sebagai fungsi terhadap $r$:
$$L(r) = L_{\text{persegi}} + L_{\text{lingkaran}} = s^2 + \pi r^2$$
$$L(r) = \left(10 - \frac{1}{2}\pi r\right)^2 + \pi r^2$$

3. Syarat luas minimum tercapai saat $L'(r) = 0$:
$$L'(r) = 2\left(10 - \frac{1}{2}\pi r\right) \cdot \left(-\frac{1}{2}\pi\right) + 2\pi r = 0$$
$$-\pi\left(10 - \frac{1}{2}\pi r\right) + 2\pi r = 0$$
Perhatikan bahwa $\left(10 - \frac{1}{2}\pi r\right) = s$, sehingga persamaan dapat ditulis:
$$-\pi s + 2\pi r = 0$$
$$\pi s = 2\pi r$$
Bagi kedua ruas dengan $\pi$:
$$s = 2r$$

4. Menentukan perbandingan:
$$\frac{s}{r} = \frac{2}{1} = 2 : 1$$

Uji turunan kedua:
$$L''(r) = \frac{1}{2}\pi^2 + 2\pi > 0$$
Karena turunan kedua selalu positif, nilai stasioner ini pasti memberikan luas gabungan yang minimum.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b02-d-hard-bt01-005
*variasi (angka) | C5 | 5 langkah | jenis: optimasi dimensi baliho*

Sebuah papan baliho berbentuk persegi panjang dipasang di bawah sebuah gapura melengkung yang memenuhi persamaan parabola $y = 48 - x^2$ (satuan dalam meter). Sisi alas baliho terletak mendatar pada permukaan tanah (sumbu-$X$, $y = 0$) dan simetris terhadap sumbu-$Y$, sedangkan kedua sudut atasnya menyentuh lengkungan gapura. Agar luas permukaan baliho tersebut maksimum, berapakah rasio antara tinggi baliho terhadap panjang sisi alasnya?

- A. $1 : 4$  
  <sub>Salah: Siswa terbalik meletakkan rasio, yaitu menghitung panjang alas terhadap tinggi bukan tinggi terhadap panjang alas.</sub>
- B. $8 : 1$  
  <sub>Salah: Siswa salah menurunkan $L(x) = 48x - x^3$ (luas setengah bidang) tetapi langsung membandingkan tinggi terhadap setengah alas.</sub>
- C. $2 : 1$  
  <sub>Salah: Siswa lupa mengalikan koordinat $x$ dengan 2 untuk panjang alas, sehingga menghitung rasio tinggi terhadap $x$ yaitu $32 : 16 = 2 : 1$.</sub>
- **D. $4 : 1$** ✅  
  <sub>Benar: Jika titik sudut atas adalah $(x, 48 - x^2)$ dengan $x > 0$, maka panjang alas $= 2x$ dan tinggi $= 48 - x^2$. Luas $L(x) = 2x(48 - x^2) = 96x - 2x^3$. Turunan pertama $L'(x) = 96 - 6x^2 = 0 \implies x^2 = 16 \implies x = 4$. Diperoleh panjang alas $= 2(4) = 8\text{ m}$ dan tinggi $= 48 - 4^2 = 32\text{ m}$. Rasio tinggi terhadap panjang alas $= 32 : 8 = 4 : 1$.</sub>

**Pembahasan:** Misalkan koordinat sudut kanan atas baliho adalah $(x, y)$ pada kurva $y = 48 - x^2$ dengan $x > 0$.
Panjang alas baliho $= 2x$ meter.
Tinggi baliho $= y = 48 - x^2$ meter.
Fungsi luas baliho:
$$L(x) = 2x(48 - x^2) = 96x - 2x^3$$
Syarat stasioner agar luas maksimum adalah $L'(x) = 0$:
$$L'(x) = 96 - 6x^2 = 0$$
$$6x^2 = 96 \implies x^2 = 16 \implies x = 4\text{ (karena } x > 0)$$
Uji turunan kedua: $L''(x) = -12x \implies L''(4) = -48 < 0$ (terbukti maksimum).
Ukuran baliho saat luas maksimum:
- Panjang alas $= 2x = 2(4) = 8\text{ meter}$
- Tinggi $= 48 - (4)^2 = 32\text{ meter}$
Rasio tinggi terhadap panjang alas adalah:
$$\frac{\text{tinggi}}{\text{panjang alas}} = \frac{32}{8} = \frac{4}{1} = 4 : 1$$
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b02-d-hard-bt01-006
*variasi (konteks) | C5 | 6 langkah | jenis: analisis keuntungan maksimum*

Sebuah perusahaan manufaktur komponen elektronik merancang pemodelan finansial untuk produksi chip semikonduktor. Besar pendapatan total $R(x)$ dan biaya total $C(x)$ berturut-turut dimodelkan oleh persamaan $R(x) = -4x^2 + 2.400x$ dan $C(x) = x^3 - 49x^2 + 1.200x + 5.000$, dengan $x$ menyatakan banyak produksi (dalam puluhan unit), sedangkan $R$ dan $C$ dalam jutaan rupiah. Berdasarkan model tersebut, tentukan banyak produksi chip semikonduktor dan besar keuntungan maksimum yang dapat dicapai perusahaan.

- A. $400\text{ unit}$ dengan keuntungan maksimum Rp56.000.000.000,00  
  <sub>Salah: Siswa salah saat mengurangkan biaya tetap 5.000 (menjadi ditambah 5.000 pada fungsi laba).</sub>
- B. $40\text{ unit}$ dengan keuntungan maksimum Rp51.000.000.000,00  
  <sub>Salah: Siswa lupa mengonversi nilai $x$ dari puluhan unit menjadi unit sebenarnya ($x = 40$ langsung dianggap 40 unit bukan 400 unit).</sub>
- **C. $400\text{ unit}$ dengan keuntungan maksimum Rp51.000.000.000,00** ✅  
  <sub>Benar: Fungsi keuntungan $\pi(x) = R(x) - C(x) = -x^3 + 45x^2 + 1.200x - 5.000$. Turunan pertamanya $\pi'(x) = -3x^2 + 90x + 1.200 = 0 \implies x^2 - 30x - 400 = 0 \implies (x - 40)(x + 10) = 0$. Nilai positif $x = 40$ puluh unit $= 400$ unit. Uji $\pi''(40) = -6(40) + 90 = -150 < 0$ (maksimum). Keuntungan $\pi(40) = -(40)^3 + 45(40)^2 + 1.200(40) - 5.000 = 51.000$ juta rupiah $=$ Rp51.000.000.000,00.</sub>
- D. $100\text{ unit}$ dengan keuntungan maksimum Rp11.000.000.000,00  
  <sub>Salah: Siswa mengambil akar dari pemfaktoran yang salah tanda ($x = 10$) yang sebenarnya merupakan titik ekstrem negatif/titik belok yang salah.</sub>

**Pembahasan:** Fungsi keuntungan (laba) $\pi(x)$ didefinisikan sebagai:
$$\pi(x) = R(x) - C(x)$$
$$\pi(x) = (-4x^2 + 2.400x) - (x^3 - 49x^2 + 1.200x + 5.000)$$
$$\pi(x) = -x^3 + 45x^2 + 1.200x - 5.000$$
Syarat keuntungan maksimum adalah $\pi'(x) = 0$ dan $\pi''(x) < 0$:
$$\pi'(x) = -3x^2 + 90x + 1.200 = 0$$
Bagi kedua ruas dengan $-3$:
$$x^2 - 30x - 400 = 0$$
$$(x - 40)(x + 10) = 0$$
Karena $x > 0$, maka $x = 40$.
Uji turunan kedua:
$$\pi''(x) = -6x + 90 \implies \pi''(40) = -6(40) + 90 = -150 < 0\text{ (maksimum)}$$
Karena $x$ dalam puluhan unit, maka banyak produksi $= 40 \times 10 = 400\text{ unit}$.
Besar keuntungan maksimum:
$$\pi(40) = -(40)^3 + 45(40)^2 + 1.200(40) - 5.000$$
$$\pi(40) = -64.000 + 72.000 + 48.000 - 5.000 = 51.000\text{ juta rupiah}$$
Keuntungan maksimum $= \text{Rp}51.000.000.000,00$.
**Acuan:** siswa — siswa hal.171 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b02-d-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: analisis laju perubahan maksimum*

Estimasi jumlah kasus kumulatif suatu wabah penyakit di suatu kota dalam $t$ hari pertama ($0 \le t \le 15$) dimodelkan oleh fungsi $N(t) = -t^3 + 18t^2 + 120t$, dengan $N(t)$ menyatakan banyak orang yang terinfeksi. Tim tanggap darurat ingin mengetahui kapan laju penambahan harian kasus baru mengalami puncaknya (laju penyebaran tercepat), serta berapa laju pertambahan kasus pada saat puncak tersebut. Hasil analisis yang benar adalah ....

- **A. Terjadi pada hari ke-$6$ dengan laju $228\text{ kasus/hari}$** ✅  
  <sub>Benar: Laju penambahan kasus adalah $v(t) = N'(t) = -3t^2 + 36t + 120$. Puncak laju penambahan dicapai saat $v'(t) = N''(t) = -6t + 36 = 0 \implies t = 6$. Karena $v''(6) = -6 < 0$, laju maksimum terjadi pada $t = 6$. Nilai laju maksimum adalah $v(6) = -3(6)^2 + 36(6) + 120 = -108 + 216 + 120 = 228\text{ kasus/hari}$.</sub>
- B. Terjadi pada hari ke-$12$ dengan laju $120\text{ kasus/hari}$  
  <sub>Salah: Siswa salah menyamakan $N'(t) = 0$ untuk mencari nilai puncak kasus kumulatif, bukan puncak laju penambahan kasus.</sub>
- C. Terjadi pada hari ke-$6$ dengan laju $1.152\text{ kasus/hari}$  
  <sub>Salah: Siswa menyubstitusikan $t = 6$ ke fungsi kumulatif $N(t)$, bukan ke fungsi laju $v(t) = N'(t)$.</sub>
- D. Terjadi pada hari ke-$3$ dengan laju $201\text{ kasus/hari}$  
  <sub>Salah: Siswa salah saat menurunkan turunan kedua, menulis $-12t + 36 = 0$ sehingga diperoleh $t = 3$.</sub>

**Pembahasan:** Laju penambahan kasus harian didefinisikan sebagai turunan pertama dari fungsi jumlah kasus kumulatif $N(t)$:
$$v(t) = N'(t) = \frac{d}{dt}(-t^3 + 18t^2 + 120t) = -3t^2 + 36t + 120$$
Untuk mencari kapan laju penambahan kasus $v(t)$ mencapai puncak (maksimum), kita gunakan turunan pertama dari $v(t)$ yang disamakan dengan nol ($v'(t) = 0$ atau $N''(t) = 0$):
$$v'(t) = N''(t) = -6t + 36 = 0$$
$$-6t = -36 \implies t = 6$$
Uji kecekungan: $v''(t) = -6 < 0$, sehingga terbukti bahwa pada $t = 6$ fungsi $v(t)$ mencapai nilai maksimum lokal.
Besar laju pertambahan kasus pada hari ke-6 adalah:
$$v(6) = -3(6)^2 + 36(6) + 120 = -108 + 216 + 120 = 228\text{ kasus/hari}$$
**Acuan:** siswa — siswa hal.168

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b02-d-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: analisis kinematika gerak*

Sebuah wahana uji coba melaju sepanjang rel lurus dengan persamaan lintasan $s(t) = t^3 - 9t^2 + 24t + 4$, dengan $s$ menyatakan posisi dalam meter dan $t$ menyatakan waktu dalam detik ($t \ge 0$). Wahana dikatakan mengalami gerak diperlambat jika besar kelajuannya berkurang seiring berjalannya waktu. Pada interval waktu manakah wahana tersebut mengalami gerak diperlambat?

- **A. $0 < t < 2$ dan $3 < t < 4$** ✅  
  <sub>Benar: Kecepatan $v(t) = 3t^2 - 18t + 24 = 3(t - 2)(t - 4)$. Percepatan $a(t) = 6t - 18 = 6(t - 3)$. Gerak diperlambat terjadi jika $v(t)$ dan $a(t)$ berlawanan tanda, yaitu $v(t) \cdot a(t) < 0$. Uji tanda pada garis bilangan menghasilkan interval $0 < t < 2$ (di mana $v > 0, a < 0$) dan $3 < t < 4$ (di mana $v < 0, a > 0$).</sub>
- B. $2 < t < 4$  
  <sub>Salah: Siswa hanya mengidentifikasi interval saat kecepatan negatif ($v(t) < 0$), mengira kecepatan negatif selalu berarti diperlambat.</sub>
- C. $0 \le t < 3$  
  <sub>Salah: Siswa hanya meninjau saat percepatannya negatif ($a(t) < 0$), tanpa memperhatikan tanda kecepatannya.</sub>
- D. $2 < t < 3$ dan $t > 4$  
  <sub>Salah: Siswa salah mengartikan syarat perlambatan dan justru mencari interval gerak dipercepat ($v(t) \cdot a(t) > 0$).</sub>

**Pembahasan:** Suatu benda mengalami gerak diperlambat (kelajuan menurun) jika tanda kecepatan $v(t)$ berlawanan dengan tanda percepatan $a(t)$, yakni ketika $v(t) \cdot a(t) < 0$.
1. Tentukan fungsi kecepatan $v(t)$:
$$v(t) = s'(t) = 3t^2 - 18t + 24 = 3(t - 2)(t - 4)$$
Titik pembuat nol kecepatan: $t = 2$ dan $t = 4$.
2. Tentukan fungsi percepatan $a(t)$:
$$a(t) = v'(t) = 6t - 18 = 6(t - 3)$$
Titik pembuat nol percepatan: $t = 3$.
3. Analisis tanda untuk tiap interval waktu $t > 0$:
- Untuk $0 < t < 2$: $v(t) > 0$ dan $a(t) < 0 \implies v(t) \cdot a(t) < 0$ (diperlambat)
- Untuk $2 < t < 3$: $v(t) < 0$ dan $a(t) < 0 \implies v(t) \cdot a(t) > 0$ (dipercepat)
- Untuk $3 < t < 4$: $v(t) < 0$ dan $a(t) > 0 \implies v(t) \cdot a(t) < 0$ (diperlambat)
- Untuk $t > 4$: $v(t) > 0$ dan $a(t) > 0 \implies v(t) \cdot a(t) > 0$ (dipercepat)
Dengan demikian, gerak diperlambat terjadi pada interval $0 < t < 2$ dan $3 < t < 4$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b02-d-hard-bt01-009
*orisinal | C6 | 6 langkah | jenis: optimasi biaya perancangan wadah*

Sebuah industri pengemasan merancang kotak tertutup berbentuk balok dengan alas persegi. Kotak tersebut harus memiliki volume tepat $250\text{ cm}^3$. Biaya bahan untuk bidang alas dan bidang tutup atas adalah $\text{Rp}600,00\text{ per cm}^2$, sedangkan biaya bahan untuk keempat bidang dinding samping adalah $\text{Rp}300,00\text{ per cm}^2$. Tentukan tinggi kotak balok tersebut agar biaya pembuatan bahan kotak mencapai nilai minimum.

- A. $5\text{ cm}$  
  <sub>Salah: Siswa keliru mengira yang ditanyakan adalah panjang sisi alas ($x$) dan bukan tinggi balok ($y$).</sub>
- **B. $10\text{ cm}$** ✅  
  <sub>Benar: Misal sisi alas $x$ dan tinggi $y$, maka volume $x^2 y = 250 \implies y = \frac{250}{x^2}$. Fungsi biaya $B(x) = 600(2x^2) + 300(4xy) = 1.200x^2 + 1.200x\left(\frac{250}{x^2}\right) = 1.200x^2 + \frac{300.000}{x}$. Syarat minimum $B'(x) = 2.400x - \frac{300.000}{x^2} = 0 \implies 2.400x^3 = 300.000 \implies x^3 = 125 \implies x = 5\text{ cm}$. Tinggi kotak $y = \frac{250}{5^2} = 10\text{ cm}$.</sub>
- C. $8\text{ cm}$  
  <sub>Salah: Siswa salah saat menyederhanakan pecahan $\frac{300.000}{2.400}$ menjadi $64$ sehingga memperoleh $x = 4$ dan tinggi $15,625$ lalu membulatkan.</sub>
- D. $12\text{ cm}$  
  <sub>Salah: Siswa menghitung kotak tanpa tutup sehingga fungsi luas sisi atas terabaikan.</sub>

**Pembahasan:** Misalkan:
- Panjang sisi alas kotak $= x\text{ cm}$
- Lebar sisi alas kotak $= x\text{ cm}$
- Tinggi kotak $= y\text{ cm}$
Volume kotak balok:
$$V = x^2 y = 250 \implies y = \frac{250}{x^2}$$
Luas bidang alas dan tutup $= 2x^2\text{ cm}^2$.
Luas keempat dinding samping $= 4xy\text{ cm}^2$.
Fungsi total biaya pembuatan wadah $B(x)$ dalam rupiah:
$$B(x) = 600(2x^2) + 300(4xy)$$
$$B(x) = 1.200x^2 + 1.200xy$$
Substitusikan $y = \frac{250}{x^2}$:
$$B(x) = 1.200x^2 + 1.200x\left(\frac{250}{x^2}\right) = 1.200x^2 + \frac{300.000}{x}$$
Biaya minimum dicapai saat $B'(x) = 0$:
$$B'(x) = 2.400x - \frac{300.000}{x^2} = 0$$
$$2.400x = \frac{300.000}{x^2}$$
$$x^3 = \frac{300.000}{2.400} = 125 \implies x = 5\text{ cm}$$
Uji kecekungan: $B''(x) = 2.400 + \frac{600.000}{x^3} > 0$ untuk $x = 5$ (terbukti nilai minimum).
Menentukan tinggi kotak ($y$):
$$y = \frac{250}{x^2} = \frac{250}{5^2} = \frac{250}{25} = 10\text{ cm}$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b02-d-hard-bt01-010
*variasi (konteks) | C5 | 5 langkah | jenis: optimasi kapasitas penampang talang air*

Sebuah talang air dirancang dari selembar pelat logam selebar $60\text{ cm}$ dengan cara melipat kedua tepi sisinya selebar $20\text{ cm}$ ke atas membentuk sudut lancip $\theta$ terhadap bidang alas berlebar $20\text{ cm}$. Luas penampang tegak talang air tersebut dinyatakan sebagai fungsi dari sudut kemiringan $\theta$. Berapakah luas penampang maksimum talang air yang dapat dihasilkan?

- A. $200\sqrt{3}\text{ cm}^2$  
  <sub>Salah: Keliru menentukan sudut stasioner menjadi $\theta = 30^\circ$ dan melakukan kesalahan perhitungan trigonometri.</sub>
- B. $400\text{ cm}^2$  
  <sub>Salah: Mengasumsikan sudut tegak lurus $\theta = 90^\circ$ sehingga penampang berbentuk persegi panjang biasa berukuran $20\text{ cm} \times 20\text{ cm}$.</sub>
- **C. $300\sqrt{3}\text{ cm}^2$** ✅  
  <sub>Benar: Penampang talang membentuk trapesium sama kaki dengan sisi alas $b = 20\text{ cm}$, sisi miring $s = 20\text{ cm}$, tinggi $h = 20\sin\theta$, dan sisi atas $B = 20 + 2(20\cos\theta) = 20 + 40\cos\theta$. Luas penampang: $A(\theta) = \frac{1}{2}(b + B)h = \frac{1}{2}(40 + 40\cos\theta)(20\sin\theta) = 400(1 + \cos\theta)\sin\theta$. Turunan pertama terhadap $\theta$: $A'(\theta) = 400(-\sin^2\theta + \cos\theta + \cos^2\theta) = 400(2\cos^2\theta + \cos\theta - 1)$. Nilai stasioner tercapai saat $2\cos^2\theta + \cos\theta - 1 = 0 \iff (2\cos\theta - 1)(\cos\theta + 1) = 0$. Untuk sudut lancip $\theta$, diperoleh $\cos\theta = \frac{1}{2}$, sehingga $\theta = 60^\circ$. Substitusi nilai $\theta = 60^\circ$ ke rumus luas: $A(60^\circ) = 400\left(1 + \frac{1}{2}\right)\sin(60^\circ) = 400 \cdot \frac{3}{2} \cdot \frac{\sqrt{3}}{2} = 300\sqrt{3}\text{ cm}^2$.</sub>
- D. $400\sqrt{3}\text{ cm}^2$  
  <sub>Salah: Lupa membagi dua dalam rumus luas trapesium saat menyusun pemodelan fungsi.</sub>

**Pembahasan:** Penampang talang berbentuk trapesium dengan panjang sisi sejajar $b_1 = 20$ dan $b_2 = 20 + 40\cos\theta$, serta tinggi $t = 20\sin\theta$.
Luas penampang:
$$A(\theta) = \frac{b_1 + b_2}{2} \cdot t = (20 + 20\cos\theta)(20\sin\theta) = 400\sin\theta + 400\sin\theta\cos\theta = 400\sin\theta + 200\sin(2\theta)$$
Syarat optimum $A'(\theta) = 0$:
$$400\cos\theta + 400\cos(2\theta) = 0$$
$$400\cos\theta + 400(2\cos^2\theta - 1) = 0$$
$$2\cos^2\theta + \cos\theta - 1 = 0$$
$$(2\cos\theta - 1)(\cos\theta + 1) = 0$$
Karena $0 < \theta < 90^\circ$, maka $\cos\theta = \frac{1}{2} \implies \theta = 60^\circ$.
Maka luas maksimumnya adalah:
$$A(60^\circ) = 400\left(1 + \frac{1}{2}\right)\left(\frac{\sqrt{3}}{2}\right) = 300\sqrt{3}\text{ cm}^2.$$
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b02-d-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: optimasi volume tabung dalam bola*

Sebuah wadah berbentuk tabung tegak tertutup dirancang agar dapat termuat secara pas di dalam ruang berbentuk bola dengan panjang jari-jari $R = 6\sqrt{3}\text{ cm}$. Volume maksimum dari tabung tertutup tersebut adalah ....

- **A. $864\pi\text{ cm}^3$** ✅  
  <sub>Benar: Jika jari-jari alas tabung adalah $r$ dan tinggi tabung adalah $h$, maka berdasarkan dalil Pythagoras pada penampang bola berlaku $(2r)^2 + h^2 = (2R)^2 \iff 4r^2 + h^2 = 4(6\sqrt{3})^2 = 432 \iff r^2 = 108 - \frac{1}{4}h^2$. Volume tabung: $V(h) = \pi r^2 h = \pi\left(108h - \frac{1}{4}h^3\right)$. Agar volume maksimum, $V'(h) = 0 \iff \pi\left(108 - \frac{3}{4}h^2\right) = 0 \iff \frac{3}{4}h^2 = 108 \iff h^2 = 144 \iff h = 12\text{ cm}$. Diperoleh $r^2 = 108 - \frac{1}{4}(144) = 72$. Maka volume maksimumnya adalah $V = \pi(72)(12) = 864\pi\text{ cm}^3$.</sub>
- B. $576\sqrt{2}\pi\text{ cm}^3$  
  <sub>Salah: Keliru menukar nilai $r$ dan $h$ pada langkah substitusi volume akhir.</sub>
- C. $1.296\pi\text{ cm}^3$  
  <sub>Salah: Mengabaikan hubungan kendala Pythagoras dan langsung menganggap jari-jari tabung sama dengan jari-jari bola.</sub>
- D. $432\pi\text{ cm}^3$  
  <sub>Salah: Menggunakan setengah tinggi tabung $h = 6\text{ cm}$ langsung ke dalam rumus volume tanpa mengalikan dua tinggi total.</sub>

**Pembahasan:** Hubungan dimensi tabung dan bola berjari-jari $R$:
$$r^2 + \left(\frac{h}{2}\right)^2 = R^2 \implies r^2 = (6\sqrt{3})^2 - \frac{h^2}{4} = 108 - \frac{h^2}{4}$$
Fungsi volume tabung:
$$V(h) = \pi r^2 h = \pi\left(108h - \frac{h^3}{4}\right)$$
Turunan pertama disamadengankan nol:
$$V'(h) = \pi\left(108 - \frac{3}{4}h^2\right) = 0$$
$$\frac{3}{4}h^2 = 108 \implies h^2 = 144 \implies h = 12\text{ cm}$$
Substitusi ke nilai $r^2$:
$$r^2 = 108 - \frac{144}{4} = 72\text{ cm}^2$$
Volume maksimum tabung:
$$V_{\max} = \pi r^2 h = \pi \cdot 72 \cdot 12 = 864\pi\text{ cm}^3.$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b02-d-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: analisis jarak relatif dua partikel*

Dua partikel $A$ dan $B$ bergerak sepanjang lintasan garis lurus yang sama. Posisi partikel $A$ pada saat $t$ detik dinyatakan oleh $s_A(t) = t^3 - 4t^2 + 7t + 12$ dan posisi partikel $B$ dinyatakan oleh $s_B(t) = 2t^2 - 2t + 2$, dengan $s$ dalam meter dan $t \ge 0$. Pada selang waktu $1 \le t \le 4$ detik, berapakah jarak terdekat antara kedua partikel tersebut dan kapan kondisi tersebut tercapai?

- A. $6\text{ meter}$ pada saat $t = 2\text{ detik}$  
  <sub>Salah: Mengira nilai minimum terjadi di titik tengah antara $t = 1$ dan $t = 3$ lalu salah melakukan pengurangan fungsi.</sub>
- **B. $10\text{ meter}$ pada saat $t = 3\text{ detik}$** ✅  
  <sub>Benar: Fungsi jarak pemisah kedua partikel adalah $D(t) = s_A(t) - s_B(t) = t^3 - 6t^2 + 9t + 10$. Turunan pertamanya: $D'(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3)$. Titik stasioner pada interval adalah $t = 1$ dan $t = 3$. Uji nilai fungsi: untuk $t = 1$, $D(1) = 1 - 6 + 9 + 10 = 14\text{ m}$; untuk $t = 3$, $D(3) = 27 - 54 + 27 + 10 = 10\text{ m}$; dan pada batas akhir $t = 4$, $D(4) = 64 - 96 + 36 + 10 = 14\text{ m}$. Dengan demikian, jarak terdekat pada selang $1 \le t \le 4$ adalah $10\text{ meter}$ pada saat $t = 3\text{ detik}$.</sub>
- C. $2\text{ meter}$ pada saat $t = 3\text{ detik}$  
  <sub>Salah: Lupa mengikutsertakan selisih suku konstanta $(12 - 2 = 10)$ pada rumus fungsi jarak $D(t)$.</sub>
- D. $14\text{ meter}$ pada saat $t = 1\text{ detik}$  
  <sub>Salah: Menukar titik balik minimum dengan titik balik maksimum lokal.</sub>

**Pembahasan:** Fungsi posisi selisih (jarak):
$$D(t) = s_A(t) - s_B(t) = (t^3 - 4t^2 + 7t + 12) - (2t^2 - 2t + 2) = t^3 - 6t^2 + 9t + 10$$
Turunan pertama:
$$D'(t) = 3t^2 - 12t + 9 = 0 \iff 3(t^2 - 4t + 3) = 0 \iff (t - 1)(t - 3) = 0$$
Diperoleh titik stasioner $t = 1$ dan $t = 3$.
Evaluasi nilai fungsi pada titik kritis dalam domain $1 \le t \le 4$:
- $D(1) = (1)^3 - 6(1)^2 + 9(1) + 10 = 14$
- $D(3) = (3)^3 - 6(3)^2 + 9(3) + 10 = 27 - 54 + 27 + 10 = 10$
- $D(4) = (4)^3 - 6(4)^2 + 9(4) + 10 = 64 - 96 + 36 + 10 = 14$
Nilai minimum absolut terjadi saat $t = 3\text{ detik}$ dengan jarak $10\text{ meter}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b02-d-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: optimasi biaya instalasi kabel*

Sebuah instalasi pembangkit listrik berada di tepi sungai yang memiliki lebar $900\text{ meter}$. Sebuah pabrik pengolahan berada di seberang sungai sejauh $3.000\text{ meter}$ ke arah hilir dari titik yang persis berseberangan dengan stasiun pembangkit. Kabel listrik akan dipasang melintasi sungai ke suatu titik $P$ di tepi seberang, lalu dilanjutkan menyusuri daratan menuju pabrik. Jika biaya penarikan kabel di bawah air adalah $\text{Rp}500.000,00$ per meter dan biaya di daratan adalah $\text{Rp}300.000,00$ per meter, berapakah total biaya minimum yang diperlukan untuk instalasi kabel tersebut?

- A. Rp1.566.000.000,00  
  <sub>Salah: Menarik kabel diagonal langsung di bawah air dari stasiun ke pabrik tanpa jalur darat.</sub>
- **B. Rp1.260.000.000,00** ✅  
  <sub>Benar: Misalkan titik $P$ berada pada jarak $x$ meter ke arah hilir dari titik seberang stasiun ($0 \le x \le 3.000$). Jarak kabel bawah air adalah $\sqrt{900^2 + x^2}$ meter dan jarak kabel darat adalah $(3.000 - x)$ meter. Fungsi biaya: $C(x) = 500.000\sqrt{900^2 + x^2} + 300.000(3.000 - x)$. Menentukan turunan $C'(x) = 0$: $500.000 \cdot \frac{x}{\sqrt{900^2 + x^2}} - 300.000 = 0 \iff 5x = 3\sqrt{900^2 + x^2} \iff 25x^2 = 9(900^2 + x^2) \iff 16x^2 = 9(810.000) \iff 4x = 3(900) \iff x = 675\text{ m}$. Panjang kabel air: $\sqrt{900^2 + 675^2} = \sqrt{810.000 + 455.625} = 1.125\text{ m}$. Panjang kabel darat: $3.000 - 675 = 2.325\text{ m}$. Biaya minimum: $(1.125 \times 500.000) + (2.325 \times 300.000) = 562.500.000 + 697.500.000 = \text{Rp}1.260.000.000,00$.</sub>
- C. Rp1.350.000.000,00  
  <sub>Salah: Memilih rute ortogonal (menyeberang tegak lurus $900\text{ m}$ lalu menyusuri daratan penuh $3.000\text{ m}$).</sub>
- D. Rp1.125.000.000,00  
  <sub>Salah: Hanya menghitung biaya penarikan kabel bawah air dan melupakan biaya penarikan kabel darat.</sub>

**Pembahasan:** Model fungsi biaya penarikan kabel (dalam ribuan rupiah):
$$C(x) = 500\sqrt{900^2 + x^2} + 300(3.000 - x)$$
Turunan terhadap $x$:
$$C'(x) = 500 \cdot \frac{x}{\sqrt{900^2 + x^2}} - 300$$
Syarat stasioner $C'(x) = 0$:
$$\frac{5x}{\sqrt{900^2 + x^2}} = 3 \implies 25x^2 = 9(900^2 + x^2)$$
$$16x^2 = 9 \cdot 900^2 \implies 4x = 3 \cdot 900 \implies x = 675\text{ meter}$$
Panjang segmen:
- Di air $= \sqrt{900^2 + 675^2} = \sqrt{810.000 + 455.625} = \sqrt{1.265.625} = 1.125\text{ meter}$
- Di darat $= 3.000 - 675 = 2.325\text{ meter}$
Total biaya minimum:
$$C = (1.125 \times \text{Rp}500.000,00) + (2.325 \times \text{Rp}300.000,00)$$
$$C = \text{Rp}562.500.000,00 + \text{Rp}697.500.000,00 = \text{Rp}1.260.000.000,00.$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b02-d-hard-bt01-014
*orisinal | C6 | 5 langkah | jenis: analisis kestabilan via limit turunan*

Model kestabilan suhu fluktuatif suatu fluida reaktor dinyatakan oleh fungsi limit $L = \lim_{x \to 0} \frac{a\cos(2x) + bx\sin(x) - 4}{x^4}$. Agar sistem termal berada dalam keadaan stabil, nilai limit $L$ harus ada dan bernilai bilangan real berhingga. Nilai dari $a + b + 3L$ yang memenuhi kondisi tersebut adalah ....

- A. $20$  
  <sub>Salah: Keliru dalam faktor konstanta aturan rantai turunan $\cos(2x)$ saat menerapkan dalil L'Hopital tahap ke-4 sehingga memperoleh $L = \frac{8}{3}$.</sub>
- B. $14$  
  <sub>Salah: Salah melakukan turunan perkalian pada suku $bx\sin(x)$ sehingga memperoleh nilai $b = 6$.</sub>
- C. $12$  
  <sub>Salah: Hanya menjumlahkan nilai konstanta $a + b$ dan melupakan nilai limit $3L$.</sub>
- **D. $16$** ✅  
  <sub>Benar: Agar $\lim_{x \to 0} \frac{a\cos(2x) + bx\sin(x) - 4}{x^4}$ ada berhingga saat penyebut menuju $0$, pembilang harus bernilai $0$ pada $x = 0$, yaitu $a(1) + 0 - 4 = 0 \implies a = 4$. Menerapkan aturan L'Hopital tahap 1: $\lim_{x \to 0} \frac{-8\sin(2x) + b\sin(x) + bx\cos(x)}{4x^3}$. Karena bernilai $0/0$, turunkan tahap 2: $\lim_{x \to 0} \frac{-16\cos(2x) + 2b\cos(x) - bx\sin(x)}{12x^2}$. Agar ada limit saat penyebut $12(0)^2 = 0$, pembilang pada $x=0$ harus bernilai nol: $-16(1) + 2b(1) - 0 = 0 \implies 2b = 16 \implies b = 8$. Turunkan tahap 3: $\lim_{x \to 0} \frac{32\sin(2x) - 24\sin(x) - 8x\cos(x)}{24x}$, bentuk $0/0$. Turunkan tahap 4: $\lim_{x \to 0} \frac{64\cos(2x) - 24\cos(x) - 8\cos(x) + 8x\sin(x)}{24} = \frac{64 - 32 + 0}{24} = \frac{32}{24} = \frac{4}{3}$. Jadi $L = \frac{4}{3}$. Nilai $a + b + 3L = 4 + 8 + 3\left(\frac{4}{3}\right) = 4 + 8 + 4 = 16$.</sub>

**Pembahasan:** Evaluasi limit bentuk tak tentu:
1. Syarat pembilang di $x = 0$:
$$a\cos(0) + b(0)\sin(0) - 4 = 0 \implies a - 4 = 0 \implies a = 4$$
2. Turunan pertama pembilang dan penyebut (L'Hopital):
$$\lim_{x \to 0} \frac{-8\sin(2x) + b\sin(x) + bx\cos(x)}{4x^3}$$
3. Turunan kedua:
$$\lim_{x \to 0} \frac{-16\cos(2x) + 2b\cos(x) - bx\sin(x)}{12x^2}$$
Syarat pembilang bernilai 0 di $x = 0$:
$$-16(1) + 2b(1) - 0 = 0 \implies 2b = 16 \implies b = 8$$
4. Turunan ketiga:
$$\lim_{x \to 0} \frac{32\sin(2x) - 16\sin(x) - 8\sin(x) - 8x\cos(x)}{24x} = \lim_{x \to 0} \frac{32\sin(2x) - 24\sin(x) - 8x\cos(x)}{24x}$$
5. Turunan keempat:
$$L = \lim_{x \to 0} \frac{64\cos(2x) - 24\cos(x) - 8\cos(x) + 8x\sin(x)}{24} = \frac{64 - 32 + 0}{24} = \frac{32}{24} = \frac{4}{3}$$
Diperoleh:
$$a + b + 3L = 4 + 8 + 3\left(\frac{4}{3}\right) = 16.$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b02-d-hard-bt01-015
*variasi (angka) | C5 | 4 langkah | jenis: optimasi rasio dimensi kotak*

Sebuah kotak terbuka dirancang dari selembar karton berbentuk persegi dengan panjang sisi $60\text{ cm}$. Pada setiap pojok karton dipotong persegi identik berukuran $x\text{ cm} \times x\text{ cm}$, kemudian sisi-sisinya dilipat ke atas. Pada saat volume kotak yang terbentuk mencapai nilai maksimum, berapakah perbandingan antara luas alas kotak dengan jumlah luas keempat sisi tegaknya?

- A. $2 : 1$  
  <sub>Salah: Hanya menghitung dua sisi tegak berhadapan, bukan seluruh keempat sisi tegak.</sub>
- B. $4 : 1$  
  <sub>Salah: Membandingkan luas alas dengan luas satu sisi tegak saja.</sub>
- **C. $1 : 1$** ✅  
  <sub>Benar: Volume kotak $V(x) = x(60 - 2x)^2 = 4x^3 - 240x^2 + 3.600x$. Turunan pertama $V'(x) = 12x^2 - 480x + 3.600 = 0 \iff x^2 - 40x + 300 = 0$, menghasilkan $x = 10\text{ cm}$ (karena $0 < x < 30$). Dimensi kotak adalah alas $40\text{ cm} \times 40\text{ cm}$ dan tinggi $10\text{ cm}$. Luas alas $= 40 \times 40 = 1.600\text{ cm}^2$ dan jumlah luas 4 sisi tegak $= 4 \times (40 \times 10) = 1.600\text{ cm}^2$, sehingga perbandingannya $1 : 1$.</sub>
- D. $1 : 2$  
  <sub>Salah: Terbalik menempatkan posisi antara luas sisi tegak dan luas alas.</sub>

**Pembahasan:** Misalkan panjang potongan pada setiap sudut adalah $x\text{ cm}$. Maka ukuran kotak terbuka yang terbentuk:
- Panjang alas: $p = 60 - 2x$
- Lebar alas: $l = 60 - 2x$
- Tinggi kotak: $t = x$
Domain nilai $x$ adalah $0 < x < 30$.

Fungsi volume kotak:
$$V(x) = x(60 - 2x)^2 = x(3.600 - 240x + 4x^2) = 4x^3 - 240x^2 + 3.600x$$

Volume maksimum terjadi ketika $V'(x) = 0$:
$$V'(x) = 12x^2 - 480x + 3.600 = 0$$
Bagi kedua ruas dengan 12:
$$x^2 - 40x + 300 = 0$$
$$(x - 10)(x - 30) = 0$$
Diperoleh $x = 10$ atau $x = 30$. Karena $0 < x < 30$, nilai yang memenuhi adalah $x = 10\text{ cm}$.

Ukuran kotak saat volume maksimum:
- Sisi alas $= 60 - 2(10) = 40\text{ cm}$
- Tinggi $= 10\text{ cm}$

Perhitungan luas:
- Luas alas $= 40 \times 40 = 1.600\text{ cm}^2$
- Luas seluruh sisi tegak $= 4 \times (40 \times 10) = 1.600\text{ cm}^2$

Perbandingan luas alas terhadap luas seluruh sisi tegak adalah:
$$\frac{1.600}{1.600} = \frac{1}{1} \Rightarrow 1 : 1$$
**Acuan:** siswa — siswa hal.166 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b02-d-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi keliling luas kurva*

Sebuah persegi panjang dibuat simetris terhadap sumbu-$Y$ dengan alasnya terletak pada sumbu-$X$ dan dua titik sudut atasnya terletak pada kurva parabola $y = 54 - 2x^2$ di atas sumbu-$X$. Jika luas persegi panjang tersebut mencapai nilai maksimum, berapakah keliling persegi panjang tersebut?

- A. $42\text{ satuan}$  
  <sub>Salah: Hanya menghitung setengah keliling (panjang alas ditambah tinggi).</sub>
- B. $78\text{ satuan}$  
  <sub>Salah: Keliru menggunakan panjang alas sebesar $x = 3$ bukan $2x = 6$ saat menghitung keliling.</sub>
- C. $216\text{ satuan}$  
  <sub>Salah: Menghitung nilai luas maksimumnya, bukan kelilingnya.</sub>
- **D. $84\text{ satuan}$** ✅  
  <sub>Benar: Titik sudut kanan atas berada di $(x, 54 - 2x^2)$ dengan $x > 0$. Luas persegi panjang $L(x) = 2x(54 - 2x^2) = 108x - 4x^3$. Syarat stasioner $L'(x) = 108 - 12x^2 = 0 \implies x = 3$. Panjang alas $= 2x = 6$ dan tinggi $= 54 - 2(3)^2 = 36$. Keliling $= 2(\text{alas} + \text{tinggi}) = 2(6 + 36) = 84\text{ satuan}$.</sub>

**Pembahasan:** Misalkan koordinat salah satu titik sudut atas pada kuadran I adalah $(x, y)$ dengan $y = 54 - 2x^2$ dan $x > 0$.
Karena bangun simetris terhadap sumbu-$Y$:
- Panjang alas $= 2x$
- Tinggi $= y = 54 - 2x^2$

Fungsi luas persegi panjang:
$$L(x) = 2x(54 - 2x^2) = 108x - 4x^3$$

Luas maksimum tercapai saat $L'(x) = 0$:
$$L'(x) = 108 - 12x^2 = 0$$
$$12x^2 = 108$$
$$x^2 = 9 \implies x = 3\quad (\text{karena } x > 0)$$

Dimensi persegi panjang saat luas maksimum:
- Alas $= 2(3) = 6\text{ satuan}$
- Tinggi $= 54 - 2(3)^2 = 54 - 18 = 36\text{ satuan}$

Keliling persegi panjang:
$$K = 2(\text{alas} + \text{tinggi}) = 2(6 + 36) = 2(42) = 84\text{ satuan}$$
**Acuan:** pretest — kelas12_tl-b02-p0169-latihan-soal-aplikasi-turunan-fungsi-di-berbagai-bidang-ilmu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b02-d-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: evaluasi dinamika gerak melambat*

Sebuah partikel bergerak sepanjang lintasan lurus dengan persamaan posisi $s(t) = \frac{1}{4}t^4 - 2t^3 + \frac{9}{2}t^2 - 8$ untuk $t \ge 0$, dengan $s$ dalam meter dan $t$ dalam detik. Partikel dikatakan mengalami gerak diperlambat jika kecepatan dan percepatannya memiliki arah yang berlawanan (berbeda tanda). Pada interval waktu manakah partikel tersebut bergerak diperlambat?

- A. $0 < t < 3$  
  <sub>Salah: Mengabaikan perubahan tanda percepatan pada titik belok $t = 1$.</sub>
- **B. $1 < t < 3$** ✅  
  <sub>Benar: Kecepatan $v(t) = s'(t) = t(t - 3)^2 \ge 0$ untuk seluruh $t \ge 0$. Percepatan $a(t) = v'(t) = 3(t - 1)(t - 3)$. Tanda $a(t) < 0$ terjadi tepat pada $1 < t < 3$. Karena $v(t) > 0$ dan $a(t) < 0$ pada $1 < t < 3$, perkalian $v(t)a(t) < 0$, sehingga partikel diperlambat pada interval $1 < t < 3$.</sub>
- C. $t > 3$  
  <sub>Salah: Pada selang ini $v(t) > 0$ dan $a(t) > 0$, partikel bergerak dipercepat searah.</sub>
- D. $0 < t < 1$  
  <sub>Salah: Pada interval ini nilai percepatan $a(t) > 0$ dan kecepatan $v(t) > 0$, sehingga gerak justru dipercepat.</sub>

**Pembahasan:** Kecepatan sesaat partikel diperoleh dari turunan pertama fungsi posisi:
$$v(t) = s'(t) = t^3 - 6t^2 + 9t = t(t^2 - 6t + 9) = t(t - 3)^2$$
Untuk $t > 0$ dengan $t \ne 3$, nilai $t > 0$ dan $(t - 3)^2 > 0$, sehingga $v(t) > 0$ (partikel selalu bergerak ke arah positif).

Percepatan sesaat partikel diperoleh dari turunan kedua fungsi posisi:
$$a(t) = v'(t) = 3t^2 - 12t + 9 = 3(t^2 - 4t + 3) = 3(t - 1)(t - 3)$$

Titik pembuat nol percepatan adalah $t = 1$ dan $t = 3$. Uji tanda untuk $a(t)$:
- Untuk $0 < t < 1$: $a(t) > 0$
- Untuk $1 < t < 3$: $a(t) < 0$
- Untuk $t > 3$: $a(t) > 0$

Syarat partikel mengalami gerak diperlambat adalah $v(t)$ dan $a(t)$ berlawanan tanda, yaitu $v(t) \cdot a(t) < 0$:
Karena $v(t) > 0$ untuk $t \in (1, 3)$, dan pada interval tersebut $a(t) < 0$, maka perkaliannya bernilai negatif.
Jadi, partikel bergerak diperlambat pada interval $1 < t < 3$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b02-d-hard-bt01-018
*orisinal | C5 | 5 langkah | jenis: evaluasi parameter limit laju*

Model fluktuasi laju dispersi zat terlarut dalam suatu wadah melibatkan bentuk limit fungsi tak tentu berikut:
$$\lim_{x \to 0} \frac{\cos(ax) - \cos(bx)}{x^2} = 16$$
Jika diketahui $a$ dan $b$ merupakan bilangan bulat positif dengan $b > a$ serta memenuhi $a + b = 8$, berapakah nilai dari hasil kali $a \cdot b$?

- A. $7$  
  <sub>Salah: Memperoleh pasangan nilai $a = 1$ dan $b = 7$ yang tidak memenuhi hasil limit.</sub>
- B. $16$  
  <sub>Salah: Keliru menetapkan $b^2 - a^2 = 16$ karena lupa membagi penyebut dengan faktor 2 dari turunan $x^2$.</sub>
- C. $15$  
  <sub>Salah: Memperoleh pasangan nilai $a = 3$ dan $b = 5$ yang menghasilkan selisih kuadrat 16 bukan 32.</sub>
- **D. $12$** ✅  
  <sub>Benar: Substitusi $x = 0$ menghasilkan bentuk $\frac{0}{0}$. Terapkan aturan L'Hôpital dua kali berturut-turut: turunan pertama $\frac{-a\sin(ax) + b\sin(bx)}{2x}$, turunan kedua $\frac{-a^2\cos(ax) + b^2\cos(bx)}{2}$. Saat $x \to 0$, limit bernilai $\frac{b^2 - a^2}{2} = 16 \iff b^2 - a^2 = 32$. Karena $(b - a)(b + a) = 32$ dan $a + b = 8$, maka $b - a = 4$. Diperoleh $b = 6$ dan $a = 2$, sehingga $a \cdot b = 12$.</sub>

**Pembahasan:** Bentuk limit $\lim_{x \to 0} \frac{\cos(ax) - \cos(bx)}{x^2}$ menghasilkan bentuk tak tentu $\frac{0}{0}$.

Menggunakan aturan turunan (dalil L'Hôpital) pertama:
$$L = \lim_{x \to 0} \frac{\frac{d}{dx}[\cos(ax) - \cos(bx)]}{\frac{d}{dx}[x^2]} = \lim_{x \to 0} \frac{-a\sin(ax) + b\sin(bx)}{2x}$$
Karena substitusi masih menghasilkan $\frac{0}{0}$, gunakan aturan L'Hôpital kedua:
$$L = \lim_{x \to 0} \frac{\frac{d}{dx}[-a\sin(ax) + b\sin(bx)]}{\frac{d}{dx}[2x]} = \lim_{x \to 0} \frac{-a^2\cos(ax) + b^2\cos(bx)}{2}$$
Substitusikan $x = 0$:
$$L = \frac{-a^2\cos(0) + b^2\cos(0)}{2} = \frac{b^2 - a^2}{2}$$

Diketahui nilai limit adalah 16:
$$\frac{b^2 - a^2}{2} = 16 \implies b^2 - a^2 = 32$$

Faktorkan bentuk selisih kuadrat:
$$(b - a)(b + a) = 32$$
Karena $b + a = 8$, maka:
$$(b - a)(8) = 32 \implies b - a = 4$$

Selesaikan sistem persamaan linear:
$$b + a = 8$$
$$b - a = 4$$
Jumlahkan kedua persamaan:
$$2b = 12 \implies b = 6$$
$$a = 8 - 6 = 2$$

Maka hasil kali $a \cdot b = 2 \times 6 = 12$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b02-d-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: optimasi perancangan wadah kerucut*

Sebuah corong penyaring berbentuk kerucut lingkaran tegak tanpa tutup dirancang dengan panjang garis pelukis tetap $s = 9\sqrt{3}\text{ cm}$. Agar kapasitas volume corong yang dihasilkan bernilai maksimum, perbandingan antara panjang jari-jari alas kerucut ($r$) terhadap tinggi kerucut ($h$) adalah ....

- **A. $\sqrt{2} : 1$** ✅  
  <sub>Benar: Volume kerucut $V = \frac{1}{3}\pi r^2 h$ dengan $r^2 = s^2 - h^2 = 243 - h^2$. Fungsi volume menjadi $V(h) = \frac{1}{3}\pi(243h - h^3)$. Turunan pertama $V'(h) = \frac{1}{3}\pi(243 - 3h^2) = 0$ menghasilkan $h = 9\text{ cm}$. Nilai $r = \sqrt{243 - 9^2} = \sqrt{162} = 9\sqrt{2}\text{ cm}$. Dengan demikian, rasio $r : h = 9\sqrt{2} : 9 = \sqrt{2} : 1$.</sub>
- B. $2 : 1$  
  <sub>Salah: Siswa membandingkan kuadrat jari-jari terhadap kuadrat tinggi ($r^2 : h^2 = 162 : 81 = 2 : 1$) tanpa menarik akar kuadratnya.</sub>
- C. $\sqrt{3} : 1$  
  <sub>Salah: Siswa salah memasukkan nilai kuadrat garis pelukis saat menghitung $r$, menghasilkan rasio yang keliru.</sub>
- D. $1 : \sqrt{2}$  
  <sub>Salah: Siswa menghitung perbandingan secara terbalik antara tinggi terhadap jari-jari ($h : r$).</sub>

**Pembahasan:** Hubungan antara jari-jari alas $r$, tinggi kerucut $h$, dan garis pelukis $s$ pada kerucut tegak memenuhi teorema Pythagoras:
$$r^2 + h^2 = s^2$$
Karena $s = 9\sqrt{3}\text{ cm}$, maka $s^2 = (9\sqrt{3})^2 = 243$, sehingga diperoleh:
$$r^2 = 243 - h^2$$

Rumus volume kerucut adalah:
$$V = \frac{1}{3}\pi r^2 h$$
Substitusikan $r^2 = 243 - h^2$ ke dalam rumus volume:
$$V(h) = \frac{1}{3}\pi (243 - h^2)h = \frac{1}{3}\pi (243h - h^3)$$

Untuk memperoleh volume maksimum, cari titik stasioner dengan menyelesaikan $V'(h) = 0$:
$$V'(h) = \frac{1}{3}\pi (243 - 3h^2) = 0$$
$$243 - 3h^2 = 0$$
$$3h^2 = 243$$
$$h^2 = 81 \implies h = 9\text{ cm} \quad (h > 0)$$

Periksa turunan kedua untuk konfirmasi nilai maksimum:
$$V''(h) = \frac{1}{3}\pi (-6h) = -2\pi h$$
Untuk $h = 9$, $V''(9) = -18\pi < 0$ (terbukti titik balik maksimum).

Hitung panjang jari-jari alas kerucut $r$:
$$r = \sqrt{243 - h^2} = \sqrt{243 - 9^2} = \sqrt{243 - 81} = \sqrt{162} = 9\sqrt{2}\text{ cm}$$

Dengan demikian, perbandingan antara jari-jari alas ($r$) dan tinggi kerucut ($h$) adalah:
$$\frac{r}{h} = \frac{9\sqrt{2}}{9} = \frac{\sqrt{2}}{1} \implies \sqrt{2} : 1$$
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas12_tl-b02-d-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: evaluasi kelajuan gerak harmonik*

Sebuah partikel bergerak sepanjang garis lurus dengan persamaan posisi $s(t) = 4\cos(t) + \cos(2t)$ untuk selang waktu $0 \le t \le 2\pi$, dengan $s$ dalam meter dan $t$ dalam detik. Kelajuan maksimum yang dicapai partikel tersebut adalah ....

- A. $2\sqrt{3}\text{ m/s}$  
  <sub>Salah: Siswa hanya menghitung kontribusi suku pertama saat substitusi $t = \frac{\pi}{3}$ yaitu $|-4\sin(\frac{\pi}{3})| = 2\sqrt{3}\text{ m/s}$ dan mengabaikan suku kedua.</sub>
- B. $6\text{ m/s}$  
  <sub>Salah: Siswa salah mengasumsikan nilai maksimum terjadi saat kedua komponen sinus bernilai maksimum secara bersamaan dengan menjumlahkan nilai mutlak koefisiennya: $|-4| + |-2| = 6$.</sub>
- C. $4\sqrt{2}\text{ m/s}$  
  <sub>Salah: Siswa salah menggunakan sudut kritis $t = \frac{\pi}{4}$ sehingga menghitung $|-4\sin(\frac{\pi}{4}) - 2\sin(\frac{\pi}{2})| = |-2\sqrt{2} - 2|$ lalu membulatkannya secara keliru.</sub>
- **D. $3\sqrt{3}\text{ m/s}$** ✅  
  <sub>Benar: Turunan pertama memberikan kecepatan $v(t) = -4\sin(t) - 2\sin(2t)$. Nilai ekstrem kecepatan diperoleh saat $v'(t) = a(t) = -4\cos(t) - 4\cos(2t) = 0$. Substitusi $\cos(2t) = 2\cos^2(t) - 1$ menghasilkan $2\cos^2(t) + \cos(t) - 1 = 0 \iff (2\cos(t) - 1)(\cos(t) + 1) = 0$, sehingga $\cos(t) = \frac{1}{2}$ atau $\cos(t) = -1$. Pada selang $[0, 2\pi]$, diperoleh $t = \frac{\pi}{3}, \pi, \frac{5\pi}{3}$. Kelajuan $|v(t)|$ pada $t = \frac{\pi}{3}$ dan $t = \frac{5\pi}{3}$ adalah $|-4(\frac{\sqrt{3}}{2}) - 2(\frac{\sqrt{3}}{2})| = |-3\sqrt{3}| = 3\sqrt{3}\text{ m/s}$, yang lebih besar dari nilai di batas interval ($0\text{ m/s}$).</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Tentukan fungsi kecepatan $v(t)$ sebagai turunan pertama dari lintasan posisi $s(t)$:
   $$v(t) = s'(t) = -4\sin(t) - 2\sin(2t)$$
2. Tentukan fungsi percepatan $a(t)$ untuk mencari titik stasioner kecepatan:
   $$a(t) = v'(t) = -4\cos(t) - 4\cos(2t)$$
3. Terapkan identitas sudut ganda $\cos(2t) = 2\cos^2(t) - 1$ dan atur $a(t) = 0$:
   $$-4\cos(t) - 4(2\cos^2(t) - 1) = 0$$
   $$-4(2\cos^2(t) + \cos(t) - 1) = 0$$
   $$(2\cos(t) - 1)(\cos(t) + 1) = 0$$
   Diperoleh $\cos(t) = \frac{1}{2}$ atau $\cos(t) = -1$.
4. Tentukan titik kritis pada selang $0 \le t \le 2\pi$:
   - Dari $\cos(t) = \frac{1}{2}$ diperoleh $t = \frac{\pi}{3}$ atau $t = \frac{5\pi}{3}$.
   - Dari $\cos(t) = -1$ diperoleh $t = \pi$.
   - Batas interval: $t = 0$ dan $t = 2\pi$.
5. Evaluasi kelajuan $|v(t)|$ pada setiap titik kritis:
   - Untuk $t = 0, \pi, 2\pi$: $|v(t)| = 0\text{ m/s}$.
   - Untuk $t = \frac{\pi}{3}$:
     $$v\left(\frac{\pi}{3}\right) = -4\sin\left(\frac{\pi}{3}\right) - 2\sin\left(\frac{2\pi}{3}\right) = -4\left(\frac{\sqrt{3}}{2}\right) - 2\left(\frac{\sqrt{3}}{2}\right) = -3\sqrt{3}\text{ m/s}$$
     Kelajuan: $|v| = 3\sqrt{3}\text{ m/s}$.
   - Untuk $t = \frac{5\pi}{3}$:
     $$v\left(\frac{5\pi}{3}\right) = -4\left(-\frac{\sqrt{3}}{2}\right) - 2\left(-\frac{\sqrt{3}}{2}\right) = 3\sqrt{3}\text{ m/s}$$
     Kelajuan: $|v| = 3\sqrt{3}\text{ m/s}$.

Jadi, kelajuan maksimum partikel tersebut adalah $3\sqrt{3}\text{ m/s}$.
**Acuan:** siswa — siswa hal.164

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
