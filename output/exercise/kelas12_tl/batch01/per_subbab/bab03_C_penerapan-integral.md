# Lembar koreksi — kelas12_tl SMA12L-B3 subbab C: Penerapan Integral

53 soal | easy 20, medium 16, hard 17 | variasi 23, orisinal 30
> **Kapasitas kurang (medium): 16 dari kuota 20** — 6 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis
> **Kapasitas kurang (hard): 17 dari kuota 20** — 5 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b03-c-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: aplikasi ekonomi*

Kecepatan penghematan biaya operasional suatu mesin produksi dinyatakan dengan fungsi $f(t) = 6.000t + 2.000$ (dalam rupiah per tahun), dengan $t$ menyatakan lama pemakaian dalam tahun untuk $0 \le t \le 5$. Berapa jumlah penghematan biaya operasional yang diperoleh selama 3 tahun pertama?

- A. Rp60.000,00  
  <sub>Salah: Lupa membagi koefisien suku linear saat integrasi sehingga menghitung $6.000t^2 + 2.000t$.</sub>
- **B. Rp33.000,00** ✅  
  <sub>Benar: Total penghematan adalah $\int_0^3 (6.000t + 2.000)\,dt = [3.000t^2 + 2.000t]_0^3 = 3.000(9) + 2.000(3) = 27.000 + 6.000 = 33.000$.</sub>
- C. Rp20.000,00  
  <sub>Salah: Hanya menghitung nilai sesaat $f(3) = 6.000(3) + 2.000$ tanpa mengintegralkan fungsi.</sub>
- D. Rp29.000,00  
  <sub>Salah: Lupa mengalikan suku konstan dengan batas atas integrasi: $27.000 + 2.000$.</sub>

**Pembahasan:** Jumlah penghematan biaya operasional selama 3 tahun pertama dihitung dengan integral tentu:
$$\int_{0}^{3} (6.000t + 2.000)\,dt = \left[ 3.000t^2 + 2.000t \right]_{0}^{3}$$
Substitusikan batas:
$$(3.000(3)^2 + 2.000(3)) - 0 = 3.000(9) + 6.000 = 27.000 + 6.000 = 33.000$$
Jadi, jumlah penghematan biaya operasional adalah Rp33.000,00.
**Acuan:** siswa — siswa hal.224 Ayo Mencoba 3.12

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b03-c-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: aplikasi kinematika*

Seorang pengendara sepeda mencatat bahwa kecepatannya (dalam km/jam) mengikuti fungsi $v(t) = -4t + 24$, dengan $t$ menyatakan waktu dalam jam sejak mulai bersepeda. Jika pengendara berhenti pada saat $t = 6$ jam, berapakah total jarak yang telah ditempuh selama 6 jam tersebut?

- A. 144 km  
  <sub>Salah: Hanya mengalikan kecepatan awal $v(0) = 24$ dengan selang waktu 6 jam tanpa memperhitungkan perlambatan.</sub>
- B. 0 km  
  <sub>Salah: Menghitung kecepatan akhir $v(6) = 0$ dan menganggap jarak tempuhnya nol.</sub>
- **C. 72 km** ✅  
  <sub>Benar: Jarak total $s = \int_0^6 (-4t + 24)\,dt = [-2t^2 + 24t]_0^6 = -2(36) + 24(6) = -72 + 144 = 72\text{ km}$.</sub>
- D. 36 km  
  <sub>Salah: Salah menghitung koefisien integral sehingga memperoleh $-3t^2 + 24t$ yang bernilai $-108 + 144 = 36$.</sub>

**Pembahasan:** Jarak tempuh adalah integral dari fungsi kecepatan terhadap waktu:
$$s = \int_{0}^{6} (-4t + 24)\,dt = \left[ -2t^2 + 24t \right]_{0}^{6}$$
Evaluasi nilai batas:
$$s = (-2(6)^2 + 24(6)) - 0 = -2(36) + 144 = -72 + 144 = 72\text{ km}$$
Jadi, total jarak yang ditempuh adalah 72 km.
**Acuan:** siswa — siswa hal.233 C. Penerapan Integral

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b03-c-easy-bt01-003
*variasi (konteks) | C2 | 2 langkah | jenis: aplikasi fisika*

Sebuah peti ditarik di atas lantai mendatar sehingga bekerja gaya sebesar $F(x) = 3x^2 + 4x$ (dalam Newton), dengan $x$ menyatakan posisi peti dalam meter dari titik asal. Besar usaha yang dilakukan oleh gaya tersebut untuk memindahkan peti dari posisi $x = 0$ meter hingga $x = 2$ meter adalah ....

- **A. $16\text{ Joule}$** ✅  
  <sub>Benar: $W = \int_0^2 (3x^2 + 4x)\,dx = [x^3 + 2x^2]_0^2 = (2^3 + 2(2^2)) - 0 = 8 + 8 = 16\text{ Joule}$.</sub>
- B. $8\text{ Joule}$  
  <sub>Salah: Hanya mengintegralkan suku pertama $3x^2$ menjadi $x^3 = 8$ dan mengabaikan suku kedua.</sub>
- C. $12\text{ Joule}$  
  <sub>Salah: Lupa mengkuadratkan $x$ pada suku kedua hasil integral: menghitung $x^3 + 2x$ sehingga diperoleh $8 + 4 = 12$.</sub>
- D. $20\text{ Joule}$  
  <sub>Salah: Menghitung nilai gaya di titik akhir $F(2) = 3(4) + 4(2) = 20$ tanpa mengintegralkan fungsi gaya terhadap posisi.</sub>

**Pembahasan:** Usaha $W$ diperoleh dengan mengintegralkan fungsi gaya terhadap perpindahan:
$$W = \int_{0}^{2} (3x^2 + 4x)\,dx$$
$$W = \left[ x^3 + 2x^2 \right]_{0}^{2}$$
Substitusikan nilai batas:
$$W = (2^3 + 2(2)^2) - 0 = 8 + 2(4) = 8 + 8 = 16\text{ Joule}$$
Jadi, usaha yang dilakukan adalah 16 Joule.
**Acuan:** siswa — siswa hal.225 Contoh Soal 3.15

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b03-c-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: rumus luas kurva*

Bentuk integral tentu yang menyatakan luas daerah di bawah kurva $f(x) = 2x + 5$ yang dibatasi oleh sumbu-$x$, garis $x = 1$, dan garis $x = 4$ adalah ....

- A. $\int_{1}^{4} 2\,dx$  
  <sub>Salah: Mengintegralkan turunan dari fungsi $f(x)$ bukan fungsi kurva itu sendiri.</sub>
- B. $\int_{0}^{4} (2x + 5)\,dx$  
  <sub>Salah: Salah menetapkan batas bawah integrasi, mengasumsikan batas dimulai dari 0 bukan 1.</sub>
- C. $\int_{1}^{4} (2x + 5)^2\,dx$  
  <sub>Salah: Tertukar dengan rumus volume benda putar yang menggunakan kuadrat fungsi.</sub>
- **D. $\int_{1}^{4} (2x + 5)\,dx$** ✅  
  <sub>Benar: Untuk kurva positif pada interval $[a, b]$, luas daerah terhadap sumbu-$x$ dirumuskan dengan $\int_a^b f(x)\,dx$, dengan $a = 1$ dan $b = 4$.</sub>

**Pembahasan:** Berdasarkan definisi penerapan integral, luas daerah $L$ di bawah kurva $y = f(x)$ di atas sumbu-$x$ pada interval $[a, b]$ dirumuskan sebagai:
$$L = \int_{a}^{b} f(x)\,dx$$
Karena kurva adalah $f(x) = 2x + 5$ dengan batas $x = 1$ hingga $x = 4$, maka bentuk integralnya adalah $\int_{1}^{4} (2x + 5)\,dx$.
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b03-c-easy-bt01-005
*orisinal | C2 | 2 langkah | jenis: aplikasi laju perubahan*

Laju alir air yang masuk ke dalam sebuah tangki penampungan dinyatakan dengan fungsi $r(t) = 4t + 3$ (dalam liter per menit), dengan $t$ adalah waktu dalam menit sejak pengisian dimulai. Berapa total volume air yang telah masuk ke dalam tangki selama 3 menit pertama?

- A. $15\text{ liter}$  
  <sub>Salah: Hanya menghitung nilai laju alir sesaat pada menit ke-3: $r(3) = 4(3) + 3 = 15$.</sub>
- B. $18\text{ liter}$  
  <sub>Salah: Hanya mengintegralkan suku pertama $4t$ menjadi $2t^2 = 18$ dan melupakan suku konstan $3$.</sub>
- C. $45\text{ liter}$  
  <sub>Salah: Lupa membagi koefisien $4$ dengan pangkat baru saat integrasi sehingga menghitung $4(9) + 9 = 45$.</sub>
- **D. $27\text{ liter}$** ✅  
  <sub>Benar: $V = \int_0^3 (4t + 3)\,dt = [2t^2 + 3t]_0^3 = 2(9) + 3(3) = 18 + 9 = 27\text{ liter}$.</sub>

**Pembahasan:** Total volume air akumulatif dihitung dengan mengintegralkan fungsi laju alir terhadap waktu dari $t = 0$ sampai $t = 3$:
$$V = \int_{0}^{3} (4t + 3)\,dt = \left[ 2t^2 + 3t \right]_{0}^{3}$$
Substitusikan batas:
$$V = (2(3)^2 + 3(3)) - 0 = 2(9) + 9 = 18 + 9 = 27\text{ liter}$$
Jadi, total volume air yang masuk adalah 27 liter.
**Acuan:** siswa — siswa hal.230

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b03-c-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: akumulasi laju konsumsi*

Laju konsumsi minyak goreng suatu gerai kuliner dinyatakan dengan fungsi $f'(x) = 6x + 5$ (dalam liter per hari), dengan $x$ adalah waktu dalam hari. Total konsumsi minyak goreng dari hari ke-1 hingga hari ke-3 adalah ....

- A. 42 liter  
  <sub>Salah: Siswa hanya menghitung nilai antiturunan pada batas atas $F(3) = 42$ dan lupa mengurangkannya dengan $F(1)$.</sub>
- B. 23 liter  
  <sub>Salah: Siswa langsung mensubstitusikan nilai $x = 3$ ke fungsi turunan $f'(3) = 6(3) + 5 = 23$ tanpa diintegralkan.</sub>
- **C. 34 liter** ✅  
  <sub>Benar: Total konsumsi didapat dari $\int_{1}^{3} (6x + 5)\,dx = \left[3x^2 + 5x\right]_1^3 = (3(9) + 5(3)) - (3(1) + 5(1)) = 42 - 8 = 34$.</sub>
- D. 60 liter  
  <sub>Salah: Siswa tidak membagi dengan 2 saat mengintegralkan $6x$, sehingga menghitung $[6x^2 + 5x]_1^3 = 69 - 11 = 58$, lalu salah hitung menjadi 60.</sub>

**Pembahasan:** Total konsumsi dari hari ke-1 sampai hari ke-3 adalah:
$$\int_{1}^{3} (6x + 5)\,dx = \left[ 3x^2 + 5x \right]_{1}^{3}$$
Substitusikan batas-batasnya:
$$F(3) = 3(3)^2 + 5(3) = 27 + 15 = 42$$
$$F(1) = 3(1)^2 + 5(1) = 3 + 5 = 8$$
$$F(3) - F(1) = 42 - 8 = 34\text{ liter.}$$
**Acuan:** siswa — siswa hal.233 Pengayaan B

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b03-c-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: akumulasi laju inflasi*

Laju inflasi bulanan suatu daerah dimodelkan dengan fungsi $i(t) = 0,4t + 3$, dengan $t$ menyatakan waktu dalam bulan dan $i(t)$ dalam persen per bulan. Total inflasi kumulatif selama 5 bulan pertama ($t = 0$ hingga $t = 5$) adalah ....

- **A. $20\%$** ✅  
  <sub>Benar: Total inflasi kumulatif dihitung dengan $\int_0^5 (0,4t + 3)\,dt = \left[0,2t^2 + 3t\right]_0^5 = 0,2(25) + 3(5) = 5 + 15 = 20\%$.</sub>
- B. $25\%$  
  <sub>Salah: Siswa tidak membagi koefisien $0,4$ dengan $2$ saat integrasi, sehingga menghitung $0,4(25) + 3(5) = 10 + 15 = 25\%$.</sub>
- C. $5\%$  
  <sub>Salah: Siswa hanya mensubstitusikan $t = 5$ ke rumus fungsi $i(5) = 0,4(5) + 3 = 5$ tanpa mengintegralkan.</sub>
- D. $17\%$  
  <sub>Salah: Siswa salah mengalikan $0,2 \times 25$ menjadi $2$, sehingga perhitungannya menjadi $2 + 15 = 17\%$.</sub>

**Pembahasan:** Total inflasi kumulatif selama 5 bulan pertama dinyatakan oleh integral tentu:
$$\int_{0}^{5} (0,4t + 3)\,dt = \left[ 0,2t^2 + 3t \right]_{0}^{5}$$
Substitusikan batas atas dan bawah:
$$\left(0,2(5)^2 + 3(5)\right) - 0 = 0,2(25) + 15 = 5 + 15 = 20\%.$$
**Acuan:** siswa — siswa hal.229 Uji Kompetensi Bab 3 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b03-c-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: rumus usaha fisika*

Sebuah benda bergerak pada garis lurus dan dipengaruhi oleh gaya $F(x) = 5x + 4$ (dalam satuan Newton), dengan $x$ menyatakan posisi benda dalam meter. Bentuk integral tentu yang menyatakan usaha yang dilakukan oleh gaya tersebut untuk memindahkan benda dari $x = 2\text{ m}$ ke $x = 6\text{ m}$ adalah ....

- A. $\int_{2}^{6} 5\,dx$  
  <sub>Salah: Siswa keliru menggunakan turunan dari fungsi gaya alih-alih mengintegralkan fungsi gayanya sendiri.</sub>
- B. $\int_{6}^{2} (5x + 4)\,dx$  
  <sub>Salah: Siswa menukar posisi batas atas dan batas bawah integrasi.</sub>
- C. $\int_{0}^{4} (5x + 4)\,dx$  
  <sub>Salah: Siswa mengurangkan batas atas dengan batas bawah ($6 - 2 = 4$) lalu menggunakan interval $[0, 4]$ alih-alih batas posisi aslinya.</sub>
- **D. $\int_{2}^{6} (5x + 4)\,dx$** ✅  
  <sub>Benar: Usaha $W$ didefinisikan sebagai integral gaya terhadap perpindahan $W = \int_{a}^{b} F(x)\,dx$, sehingga dari posisi $x = 2$ ke $x = 6$ bentuknya adalah $\int_{2}^{6} (5x + 4)\,dx$.</sub>

**Pembahasan:** Dalam fisika, usaha ($W$) yang dilakukan oleh gaya variabel $F(x)$ sepanjang sumbu-$x$ dari posisi $x = a$ hingga $x = b$ dirumuskan sebagai:
$$W = \int_{a}^{b} F(x)\,dx$$
Dengan $F(x) = 5x + 4$, batas bawah $a = 2$, dan batas atas $b = 6$, maka integral yang menyatakan usaha tersebut adalah:
$$\int_{2}^{6} (5x + 4)\,dx.$$
**Acuan:** siswa — siswa hal.225

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b03-c-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: interpretasi luas kurva*

Fungsi $r(t)$ menyatakan laju pertambahan volume air (dalam liter/menit) yang dialirkan ke dalam tangki penampungan, dengan $t$ menyatakan waktu dalam menit. Luas daerah di bawah kurva $y = r(t)$ pada selang waktu $[0, 10]$ merepresentasikan ....

- **A. total volume air yang masuk ke tangki selama 10 menit pertama** ✅  
  <sub>Benar: Integral dari laju perubahan $\int_0^{10} r(t)\,dt$, yang merupakan luas daerah di bawah kurva laju alir, menghasilkan akumulasi total kuantitas (volume) selama selang waktu tersebut.</sub>
- B. lama waktu yang dibutuhkan hingga tangki terisi penuh  
  <sub>Salah: Siswa menyamakan besaran luas di bawah kurva dengan variabel waktu pada sumbu horizontal.</sub>
- C. percepatan peningkatan debit air di dalam tangki  
  <sub>Salah: Siswa tertukar antara konsep integral (akumulasi total) dengan konsep turunan (laju perubahan laju).</sub>
- D. laju aliran air rata-rata tepat pada menit ke-10  
  <sub>Salah: Siswa mengira luas di bawah kurva menyatakan nilai sesaat pada batas akhir.</sub>

**Pembahasan:** Berdasarkan penerapan integral tentu, integral dari fungsi laju perubahan $\int_{a}^{b} r(t)\,dt$ sama dengan luas daerah di bawah kurva $y = r(t)$ dari $t = a$ sampai $t = b$. Nilai ini merepresentasikan perubahan total atau akumulasi kumulatif besaran tersebut. Oleh karena itu, pada selang $[0, 10]$, luas kurva menyatakan total volume air yang masuk ke tangki selama 10 menit pertama.
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b03-c-easy-bt01-010
*variasi (konteks) | C2 | 2 langkah | jenis: akumulasi produksi barang*

Laju perakitan komputer tablet di sebuah pabrik dinyatakan dengan fungsi $f(t) = 4.000t + 2.000$ (unit per tahun), dengan $t$ adalah waktu dalam tahun sejak pabrik beroperasi ($0 \le t \le 5$). Jumlah total komputer tablet yang dirakit selama 3 tahun pertama adalah ....

- A. $42.000\text{ unit}$  
  <sub>Salah: Salah menentukan antiturunan dari $4.000t$ menjadi $4.000t^2$ sehingga $4.000(9) + 6.000 = 42.000$.</sub>
- **B. $24.000\text{ unit}$** ✅  
  <sub>Benar: Total perakitan adalah $\int_{0}^{3} (4.000t + 2.000)\,dt = [2.000t^2 + 2.000t]_{0}^{3} = 2.000(3)^2 + 2.000(3) = 18.000 + 6.000 = 24.000\text{ unit}$.</sub>
- C. $20.000\text{ unit}$  
  <sub>Salah: Menggunakan jawaban pada soal acuan tanpa menghitung fungsi baru.</sub>
- D. $14.000\text{ unit}$  
  <sub>Salah: Hanya mengevaluasi nilai fungsi laju pada $t = 3$, yaitu $4.000(3) + 2.000 = 14.000$.</sub>

**Pembahasan:** Total produksi selama 3 tahun pertama diperoleh dari integral tentu laju produksi:
$$N = \int_{0}^{3} (4.000t + 2.000)\,dt$$
$$N = \left[ 2.000t^2 + 2.000t \right]_{0}^{3}$$
$$N = (2.000(9) + 2.000(3)) - 0 = 18.000 + 6.000 = 24.000\text{ unit}.$$
**Acuan:** siswa — siswa hal.223 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b03-c-easy-bt01-011
*variasi (konteks) | C2 | 2 langkah | jenis: akumulasi volume cairan*

Laju pengisian bahan bakar minyak ke dalam tangki penampungan dinyatakan dengan fungsi $v(t) = 6t^2 + 6t + 4$ (liter per jam), dengan $t$ menyatakan waktu dalam jam sejak pengisian dimulai. Total bahan bakar yang dialirkan ke dalam tangki selama 2 jam pertama adalah ....

- A. $48\text{ liter}$  
  <sub>Salah: Salah melakukan integrasi koefisien menjadi $3t^3 + 3t^2 + 4t$ sehingga hasilnya $24 + 12 + 8 = 44$, lalu salah menjumlah menjadi 48.</sub>
- **B. $36\text{ liter}$** ✅  
  <sub>Benar: Total bahan bakar dihitung dengan $\int_{0}^{2} (6t^2 + 6t + 4)\,dt = [2t^3 + 3t^2 + 4t]_{0}^{2} = 2(8) + 3(4) + 4(2) = 16 + 12 + 8 = 36\text{ liter}$.</sub>
- C. $40\text{ liter}$  
  <sub>Salah: Hanya menghitung nilai laju sesaat pada $t = 2$, yaitu $6(2)^2 + 6(2) + 4 = 40$.</sub>
- D. $28\text{ liter}$  
  <sub>Salah: Lupa mengintegralkan konstanta 4 sehingga perhitungannya $2(8) + 3(4) = 28$.</sub>

**Pembahasan:** Total bahan bakar yang terkumpul selama 2 jam pertama:
$$V = \int_{0}^{2} (6t^2 + 6t + 4)\,dt$$
$$V = \left[ 2t^3 + 3t^2 + 4t \right]_{0}^{2}$$
$$V = (2(2)^3 + 3(2)^2 + 4(2)) - 0 = 16 + 12 + 8 = 36\text{ liter}.$$
**Acuan:** siswa — siswa hal.230 Uji Kompetensi Bab 3 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b03-c-easy-bt01-012
*variasi (konteks) | C2 | 2 langkah | jenis: luas penampang kurva*

Sebuah panel kaca hias dirancang menyerupai bidang datar di bawah kurva $y = 8 - 2x^2$, di atas sumbu-$x$, serta dibatasi oleh garis $x = -1$ dan garis $x = 1$. Luas permukaan panel kaca tersebut adalah ....

- A. $\frac{40}{3}\text{ satuan luas}$  
  <sub>Salah: Salah antiturunan suku kuadrat menjadi $-x^3$ sehingga $\left[8x - x^3\right]_{-1}^{1} = 7 - (-7) = 14$ lalu salah penyesuaian pecahan.</sub>
- B. $12\text{ satuan luas}$  
  <sub>Salah: Salah melakukan integrasi aljabar menjadi $8(1) - 2(1) = 6$ lalu dikalikan 2.</sub>
- C. $\frac{22}{3}\text{ satuan luas}$  
  <sub>Salah: Hanya mengintegralkan dari batas $0$ sampai $1$, lupa mengalikan dua atau memperhitungkan batas bawah $-1$.</sub>
- **D. $\frac{44}{3}\text{ satuan luas}$** ✅  
  <sub>Benar: Luas dihitung dengan $\int_{-1}^{1} (8 - 2x^2)\,dx = \left[8x - \frac{2}{3}x^3\right]_{-1}^{1} = \left(8 - \frac{2}{3}\right) - \left(-8 + \frac{2}{3}\right) = \frac{22}{3} - \left(-\frac{22}{3}\right) = \frac{44}{3}\text{ satuan luas}$.</sub>

**Pembahasan:** Karena fungsi $y = 8 - 2x^2$ bernilai positif pada $[-1, 1]$:
$$L = \int_{-1}^{1} (8 - 2x^2)\,dx$$
$$L = \left[ 8x - \frac{2}{3}x^3 \right]_{-1}^{1}$$
$$L = \left(8(1) - \frac{2}{3}(1)^3\right) - \left(8(-1) - \frac{2}{3}(-1)^3\right)$$
$$L = \left(8 - \frac{2}{3}\right) - \left(-8 + \frac{2}{3}\right) = \frac{22}{3} + \frac{22}{3} = \frac{44}{3}\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.234 Pengayaan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b03-c-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: usaha gaya pegas*

Sebuah pegas memerlukan gaya sebesar $F(x) = 80x$ Newton untuk meregangkannya sejauh $x$ meter dari panjang alaminya. Besar usaha yang diperlukan untuk meregangkan pegas tersebut dari posisi alami $x = 0$ meter hingga $x = 0,5$ meter adalah ....

- **A. $10\text{ Joule}$** ✅  
  <sub>Benar: Usaha diperoleh dari $W = \int_{0}^{0,5} 80x\,dx = [40x^2]_{0}^{0,5} = 40(0,5)^2 = 40(0,25) = 10\text{ Joule}$.</sub>
- B. $40\text{ Joule}$  
  <sub>Salah: Hanya menghitung nilai gaya sesaat pada $x = 0,5$, yaitu $80(0,5) = 40\text{ N}$.</sub>
- C. $20\text{ Joule}$  
  <sub>Salah: Lupa membagi koefisien dengan 2 saat mengintegralkan: $80(0,5)^2 = 20\text{ Joule}$.</sub>
- D. $5\text{ Joule}$  
  <sub>Salah: Salah membagi koefisien dengan 4 saat mengintegralkan: $20(0,5)^2 = 5\text{ Joule}$.</sub>

**Pembahasan:** Berdasarkan definisi usaha pada pegas:
$$W = \int_{0}^{0,5} F(x)\,dx = \int_{0}^{0,5} 80x\,dx$$
$$W = \left[ 40x^2 \right]_{0}^{0,5} = 40(0,5)^2 - 0 = 40(0,25) = 10\text{ Joule}.$$
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b03-c-easy-bt01-014
*orisinal | C1 | 1 langkah | jenis: rumus luas di bawah sumbu-x*

Jika suatu fungsi kontinu $y = f(x)$ bernilai nonpositif ($f(x) \le 0$) pada interval tertutup $[a, b]$, maka luas daerah $L$ yang dibatasi oleh kurva tersebut, sumbu-$x$, serta garis $x = a$ dan garis $x = b$ dirumuskan dengan ....

- A. $L = f(b) - f(a)$  
  <sub>Salah: Tertukar dengan selisih nilai fungsi ujung interval, bukan bentuk integrasi luas.</sub>
- B. $L = \int_{a}^{b} (f(x))^2\,dx$  
  <sub>Salah: Tertukar dengan bentuk kuadrat pada integrasi volume benda putar.</sub>
- **C. $L = -\int_{a}^{b} f(x)\,dx$** ✅  
  <sub>Benar: Karena kurva berada di bawah sumbu-$x$ ($f(x) \le 0$), integral tentu menghasilkan nilai negatif sehingga luas didefinisikan dengan memberi tanda negatif di depan integral agar bernilai positif.</sub>
- D. $L = \int_{a}^{b} f(x)\,dx$  
  <sub>Salah: Mengabaikan fakta bahwa kurva di bawah sumbu-$x$ sehingga integral tentu akan bernilai negatif, bukan menyatakan ukuran luas.</sub>

**Pembahasan:** Untuk daerah yang terletak seluruhnya di bawah sumbu-$x$ ($f(x) \le 0$) pada interval $[a, b]$, nilai integral tentunya bernilai negatif. Oleh karena itu, ukuran luas daerah yang bernilai selalu positif dinyatakan dengan:
$$L = -\int_{a}^{b} f(x)\,dx \quad \text{atau} \quad L = \int_{a}^{b} -f(x)\,dx.$$
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b03-c-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: akumulasi pertumbuhan tanaman*

Laju pertumbuhan tinggi suatu bibit tanaman dinyatakan oleh fungsi $f'(t) = 8t$ (dalam cm per hari), dengan $t$ menyatakan waktu dalam hari. Jika tinggi awal bibit tersebut saat $t = 0$ adalah $5\text{ cm}$, tinggi tanaman tersebut setelah $3\text{ hari}$ adalah ....

- A. $29\text{ cm}$  
  <sub>Salah: Siswa mengintegrasikan $8t$ menjadi $8t$ (turunan konstan) bukan $4t^2$ sehingga $8(3)+5 = 29$.</sub>
- B. $36\text{ cm}$  
  <sub>Salah: Siswa lupa menjumlahkan tinggi awal tanaman ($C = 5$).</sub>
- C. $77\text{ cm}$  
  <sub>Salah: Siswa mengintegrasikan menjadi $8t^2 + 5$ tanpa membagi koefisien dengan 2.</sub>
- **D. $41\text{ cm}$** ✅  
  <sub>Benar: $f(t) = \int 8t\,dt = 4t^2 + C$. Karena $f(0) = 5$, maka $C = 5$. Untuk $t = 3$, $f(3) = 4(3)^2 + 5 = 36 + 5 = 41\text{ cm}$.</sub>

**Pembahasan:** Fungsi tinggi tanaman merupakan antiturunan dari laju pertumbuhannya:
$$f(t) = \int 8t\,dt = 4t^2 + C$$
Dengan tinggi awal $f(0) = 5\text{ cm}$:
$$4(0)^2 + C = 5 \implies C = 5$$
$$f(t) = 4t^2 + 5$$
Setelah $t = 3\text{ hari}$:
$$f(3) = 4(3)^2 + 5 = 36 + 5 = 41\text{ cm}.$$
**Acuan:** siswa — siswa hal.233 Pengayaan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b03-c-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: perhitungan usaha gaya*

Sebuah partikel bergerak di sepanjang sumbu-$x$ dan dipengaruhi oleh gaya $F(x) = 8x - 4$ (dalam satuan Newton), dengan $x$ menyatakan posisi partikel dalam meter. Besar usaha yang dilakukan gaya tersebut untuk memindahkan partikel dari posisi $x = 1\text{ meter}$ ke posisi $x = 3\text{ meter}$ adalah ....

- A. $20\text{ Joule}$  
  <sub>Salah: Siswa hanya menghitung nilai gaya akhir pada $x = 3$, yaitu $F(3) = 24 - 4 = 20$.</sub>
- **B. $24\text{ Joule}$** ✅  
  <sub>Benar: $W = \int_{1}^{3} (8x - 4)\,dx = \left[4x^2 - 4x\right]_{1}^{3} = (4(9) - 4(3)) - (4(1) - 4(1)) = (36 - 12) - 0 = 24\text{ Joule}$.</sub>
- C. $28\text{ Joule}$  
  <sub>Salah: Siswa salah mengoperasikan tanda pada batas bawah menjadi $(36 - 12) - (4 - 8) = 24 - (-4) = 28$.</sub>
- D. $56\text{ Joule}$  
  <sub>Salah: Siswa tidak membagi koefisien dengan 2 saat integrasi sehingga menghitung $[8x^2 - 4x]_1^3 = 60 - 4 = 56$.</sub>

**Pembahasan:** Besar usaha ($W$) dinyatakan oleh rumus:
$$W = \int_{a}^{b} F(x)\,dx$$
$$W = \int_{1}^{3} (8x - 4)\,dx = \left[4x^2 - 4x\right]_{1}^{3}$$
$$W = (4(3)^2 - 4(3)) - (4(1)^2 - 4(1)) = (36 - 12) - (4 - 4) = 24\text{ Joule}.$$
**Acuan:** siswa — siswa hal.225

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b03-c-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: luas daerah di bawah kurva*

Luas daerah di kuadran pertama yang dibatasi oleh kurva $f(x) = 4x + 1$, sumbu-$x$, sumbu-$y$, dan garis $x = 2$ adalah ....

- A. $18\text{ satuan luas}$  
  <sub>Salah: Siswa mengintegrasikan $4x$ menjadi $4x^2$ tanpa membagi dengan 2, menghasilkan $4(4) + 2 = 18$.</sub>
- **B. $10\text{ satuan luas}$** ✅  
  <sub>Benar: Luas diperoleh dari $\int_{0}^{2} (4x + 1)\,dx = \left[2x^2 + x\right]_{0}^{2} = 2(2)^2 + 2 - 0 = 8 + 2 = 10\text{ satuan luas}$.</sub>
- C. $9\text{ satuan luas}$  
  <sub>Salah: Siswa hanya menghitung nilai ordinat saat $x = 2$, yaitu $4(2) + 1 = 9$.</sub>
- D. $8\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengintegrasikan suku konstan $+1$.</sub>

**Pembahasan:** Karena kurva berada di kuadran pertama di atas sumbu-$x$ dari $x = 0$ (sumbu-$y$) sampai $x = 2$, luasnya adalah:
$$L = \int_{0}^{2} (4x + 1)\,dx$$
$$L = \left[2x^2 + x\right]_{0}^{2} = (2(2)^2 + 2) - 0 = 8 + 2 = 10\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.220

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b03-c-easy-bt01-018
*variasi (angka) | C2 | 2 langkah | jenis: luas daerah kuadran keempat*

Tentukan luas daerah di kuadran keempat yang dibatasi oleh fungsi $f(x) = x - 8$, sumbu-$x$, garis $x = 5$, dan garis $x = 7$.

- A. $2\text{ satuan luas}$  
  <sub>Salah: Hanya menghitung selisih nilai ordinat $|f(7) - f(5)| = |-1 - (-3)| = 2$.</sub>
- B. $6\text{ satuan luas}$  
  <sub>Salah: Keliru mengintegralkan $x$ menjadi $x^2$ tanpa membagi 2 sehingga perhitungannya menjadi $(8(7)-49)-(8(5)-25) = 7 - 15 = -8$ lalu dimutlakkan atau salah aritmetika.</sub>
- **C. $4\text{ satuan luas}$** ✅  
  <sub>Benar: Pada selang $[5, 7]$, kurva berada di bawah sumbu-$x$ sehingga luas daerah dihitung dengan $L = -\int_{5}^{7} (x - 8)\,dx = \int_{5}^{7} (8 - x)\,dx = \left[8x - \frac{1}{2}x^2\right]_5^7 = (56 - 24,5) - (40 - 12,5) = 31,5 - 27,5 = 4\text{ satuan luas}$.</sub>
- D. $-4\text{ satuan luas}$  
  <sub>Salah: Mengintegralkan langsung $\int_5^7 (x - 8)\,dx$ tanpa mengubah tanda negatif untuk luas di bawah sumbu-$x$.</sub>

**Pembahasan:** Karena kurva $f(x) = x - 8$ bernilai negatif pada interval $[5, 7]$, luas daerah yang dibatasi oleh kurva dan sumbu-$x$ adalah:
$$L = -\int_{5}^{7} (x - 8)\,dx = \int_{5}^{7} (8 - x)\,dx$$
$$L = \left[ 8x - \frac{1}{2}x^2 \right]_{5}^{7}$$
$$L = \left(8(7) - \frac{1}{2}(7)^2\right) - \left(8(5) - \frac{1}{2}(5)^2\right)$$
$$L = (56 - 24,5) - (40 - 12,5) = 31,5 - 27,5 = 4\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.221 Ayo Mencoba 3.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b03-c-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: akumulasi penghematan biaya*

Laju penghematan biaya operasional sebuah mesin pabrik dinyatakan oleh fungsi $f(x) = 6.000x + 8.000$ (dalam rupiah per tahun), dengan $x$ menyatakan lama waktu pemakaian mesin dalam tahun ($0 \le x \le 9$). Berapa jumlah total penghematan biaya operasional mesin tersebut selama 2 tahun pertama?

- **A. Rp28.000,00** ✅  
  <sub>Benar: Total penghematan diperoleh dari integral tentu $\int_{0}^{2} (6.000x + 8.000)\,dx = \left[3.000x^2 + 8.000x\right]_{0}^{2} = 3.000(4) + 8.000(2) = 12.000 + 16.000 = 28.000$.</sub>
- B. Rp14.000,00  
  <sub>Salah: Menghitung rata-rata penghematan per tahun atau membagi dua hasil akhir integral.</sub>
- C. Rp20.000,00  
  <sub>Salah: Hanya menghitung nilai laju pada tahun ke-2, yaitu $f(2) = 6.000(2) + 8.000 = 20.000$.</sub>
- D. Rp40.000,00  
  <sub>Salah: Lupa membagi koefisien $x$ saat mengintegralkan, sehingga menghitung $[6.000x^2 + 8.000x]_0^2 = 24.000 + 16.000 = 40.000$.</sub>

**Pembahasan:** Jumlah total penghematan selama 2 tahun pertama dihitung dengan mengintegralkan fungsi laju penghematan dari $x = 0$ hingga $x = 2$:
$$S = \int_{0}^{2} (6.000x + 8.000)\,dx$$
$$S = \left[ 3.000x^2 + 8.000x \right]_{0}^{2}$$
$$S = (3.000(2)^2 + 8.000(2)) - 0 = 12.000 + 16.000 = 28.000.$$
Jadi, jumlah penghematan biaya operasional selama 2 tahun pertama adalah Rp28.000,00.
**Acuan:** siswa — siswa hal.224 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b03-c-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: perhitungan jarak tempuh*

Sebuah kendaraan uji bergerak dengan kecepatan yang memenuhi fungsi $v(t) = -6t + 24$ (dalam km/jam), dengan $t$ menyatakan waktu tempuh dalam jam. Kendaraan berhenti tepat saat kecepatannya nol pada $t = 4$. Berapakah jarak total yang ditempuh kendaraan tersebut selama 4 jam perjalanan?

- A. $36\text{ km}$  
  <sub>Salah: Salah mengalikan saat substitusi batas atas, menghitung $-3(16) + 24(4)$ menjadi $-60 + 96 = 36$.</sub>
- B. $96\text{ km}$  
  <sub>Salah: Lupa membagi dengan 2 pada antiturunan suku berderajat satu, menghitung $[-6t^2 + 24t]$ secara keliru.</sub>
- **C. $48\text{ km}$** ✅  
  <sub>Benar: Jarak total diperoleh dengan mengintegralkan fungsi kecepatan pada selang $[0, 4]$: $s = \int_{0}^{4} (-6t + 24)\,dt = \left[-3t^2 + 24t\right]_{0}^{4} = -3(16) + 24(4) = -48 + 96 = 48\text{ km}$.</sub>
- D. $24\text{ km}$  
  <sub>Salah: Hanya mengambil kecepatan awal $v(0) = 24$ atau salah menghitung nilai integral.</sub>

**Pembahasan:** Jarak total yang ditempuh merupakan integral dari fungsi kecepatan terhadap waktu:
$$s = \int_{0}^{4} v(t)\,dt = \int_{0}^{4} (-6t + 24)\,dt$$
$$s = \left[ -3t^2 + 24t \right]_{0}^{4}$$
$$s = (-3(4)^2 + 24(4)) - 0 = -48 + 96 = 48\text{ km}.$$
Jadi, jarak total yang ditempuh kendaraan tersebut adalah 48 km.
**Acuan:** siswa — siswa hal.233 Pengayaan C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b03-c-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: luas daerah antara dua kurva*

Luas daerah yang dibatasi oleh parabola $y = x^2$ dan $y = 6x - x^2$ adalah ....

- A. $\frac{9}{2}\text{ satuan luas}$  
  <sub>Salah: Siswa membagi hasil akhir dengan 2 karena mengira bentuk daerah simetris terhadap titik puncak.</sub>
- B. $18\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengurangkan suku kedua saat integrasi atau hanya mengintegralkan fungsi atas tanpa dikurangi fungsi bawah: $\int_0^3 (6x-x^2)dx = 27 - 9 = 18$.</sub>
- C. $27\text{ satuan luas}$  
  <sub>Salah: Siswa salah saat mengevaluasi integral, hanya menghitung $3(3)^2$ dan lupa mengurangkan $\frac{2}{3}(3)^3$.</sub>
- **D. $9\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva: $x^2 = 6x - x^2 \Leftrightarrow 2x^2 - 6x = 0 \Leftrightarrow 2x(x - 3) = 0$, diperoleh $x = 0$ dan $x = 3$. Pada interval $[0, 3]$, $6x - x^2 \ge x^2$. Luas $L = \int_{0}^{3} ((6x - x^2) - x^2)\,dx = \int_{0}^{3} (6x - 2x^2)\,dx = \left[ 3x^2 - \frac{2}{3}x^3 \right]_{0}^{3} = 3(9) - \frac{2}{3}(27) = 27 - 18 = 9\text{ satuan luas}$.</sub>

**Pembahasan:** Menentukan absis titik potong:
$$x^2 = 6x - x^2$$
$$2x^2 - 6x = 0$$
$$2x(x - 3) = 0$$
Diperoleh batas integrasi $x = 0$ sampai $x = 3$.

Menghitung luas daerah:
$$L = \int_{0}^{3} ((6x - x^2) - x^2)\,dx$$
$$L = \int_{0}^{3} (6x - 2x^2)\,dx$$
$$L = \left[ 3x^2 - \frac{2}{3}x^3 \right]_{0}^{3}$$
$$L = \left(3(3)^2 - \frac{2}{3}(3)^3\right) - 0 = 27 - 18 = 9\text{ satuan luas}.$$
**Acuan:** pretest — kelas12_tl-b03-p0228-latihan-soal-penerapan-integral-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b03-c-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: aplikasi ekonomi titik impas*

Sebuah perusahaan membeli mesin baru seharga Rp60.000,00. Kecepatan penghematan biaya operasional perusahaan setelah mesin beroperasi selama $t$ tahun dinyatakan dengan $f(t) = 4.000t + 2.000$ (dalam rupiah per tahun). Dalam berapa tahun harga pembelian mesin tersebut dapat kembali dari akumulasi penghematan operasional?

- A. $15\text{ tahun}$  
  <sub>Salah: Siswa langsung membagi harga beli Rp60.000,00 dengan koefisien $4.000$ tanpa melakukan integrasi.</sub>
- **B. $5\text{ tahun}$** ✅  
  <sub>Benar: Akumulasi penghematan selama $T$ tahun adalah $\int_0^T (4.000t + 2.000)\,dt = 2.000T^2 + 2.000T$. Nilai ini sama dengan harga beli Rp60.000,00, sehingga $2.000T^2 + 2.000T = 60.000 \Leftrightarrow T^2 + T - 30 = 0 \Leftrightarrow (T + 6)(T - 5) = 0$. Karena waktu bernilai positif, diperoleh $T = 5\text{ tahun}$.</sub>
- C. $6\text{ tahun}$  
  <sub>Salah: Siswa mengambil nilai mutlak dari akar negatif persamaan kuadrat $(T = -6)$.</sub>
- D. $4\text{ tahun}$  
  <sub>Salah: Siswa salah saat memfaktorkan persamaan kuadrat, mengira faktornya adalah $(T - 4)(T + 5) = 0$.</sub>

**Pembahasan:** Akumulasi penghematan selama $T$ tahun dirumuskan dengan:
$$S(T) = \int_{0}^{T} (4.000t + 2.000)\,dt = \left[ 2.000t^2 + 2.000t \right]_{0}^{T} = 2.000T^2 + 2.000T$$

Harga pembelian kembali saat $S(T) = 60.000$:
$$2.000T^2 + 2.000T = 60.000$$
$$T^2 + T - 30 = 0$$
$$(T - 5)(T + 6) = 0$$
Karena $T > 0$, maka $T = 5$.

Jadi, harga peralatan itu kembali dalam jangka waktu $5\text{ tahun}$.
**Acuan:** siswa — siswa hal.224

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b03-c-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: aplikasi fisika usaha pegas*

Sebuah pegas memiliki panjang alami $20\text{ cm}$. Sebuah gaya sebesar $30\text{ N}$ diperlukan untuk menahan pegas saat direntangkan hingga panjangnya menjadi $25\text{ cm}$. Usaha yang diperlukan untuk meregangkan pegas tersebut dari panjang $25\text{ cm}$ menjadi $30\text{ cm}$ adalah ....

- A. $0,75\text{ Joule}$  
  <sub>Salah: Siswa hanya menghitung usaha untuk meregangkan dari panjang alami hingga $5\text{ cm}$: $300(0,05)^2 = 0,75\text{ Joule}$.</sub>
- B. $3,00\text{ Joule}$  
  <sub>Salah: Siswa menghitung usaha total dari panjang alami hingga $10\text{ cm}$: $300(0,10)^2 = 3,00\text{ Joule}$, tanpa mengurangkan usaha regangan awal.</sub>
- **C. $2,25\text{ Joule}$** ✅  
  <sub>Benar: Pertambahan panjang awal: $x = 25 - 20 = 5\text{ cm} = 0,05\text{ m}$. Menurut Hukum Hooke: $F = kx \Rightarrow 30 = k(0,05) \Rightarrow k = 600\text{ N/m}$. Batas peregangan dari panjang alami adalah dari $a = 25 - 20 = 5\text{ cm} = 0,05\text{ m}$ sampai $b = 30 - 20 = 10\text{ cm} = 0,10\text{ m}$. Usaha: $W = \int_{0,05}^{0,10} 600x\,dx = \left[ 300x^2 \right]_{0,05}^{0,10} = 300(0,01 - 0,0025) = 300(0,0075) = 2,25\text{ Joule}$.</sub>
- D. $225\text{ Joule}$  
  <sub>Salah: Siswa lupa mengonversi satuan centimeter ke meter saat menghitung batas integrasi.</sub>

**Pembahasan:** 1. Menentukan konstanta pegas $k$:
Pertambahan panjang awal: $\Delta x = 25 - 20 = 5\text{ cm} = 0,05\text{ m}$.
$$f(x) = kx \implies 30 = k(0,05) \implies k = \frac{30}{0,05} = 600\text{ N/m}$$

2. Menentukan batas integrasi di luar panjang alami:
$x_1 = 25 - 20 = 5\text{ cm} = 0,05\text{ m}$
$x_2 = 30 - 20 = 10\text{ cm} = 0,10\text{ m}$

3. Menghitung usaha $W$:
$$W = \int_{0,05}^{0,10} 600x\,dx = \left[ 300x^2 \right]_{0,05}^{0,10}$$
$$W = 300(0,10)^2 - 300(0,05)^2 = 300(0,01) - 300(0,0025) = 3 - 0,75 = 2,25\text{ Joule}.$$
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b03-c-medium-bt01-004
*orisinal | C3 | 3 langkah | jenis: aplikasi biaya total fungsi marjinal*

Biaya tambahan produksi (biaya marjinal) suatu kerajinan tangan setiap minggu dimodelkan oleh $f'(x) = 3x^2 - 12x + 15$ (dalam ratusan ribu rupiah), dengan $x$ menyatakan minggu ke-$x$. Jika biaya tetap awal saat sebelum produksi dimulai ($x = 0$) adalah Rp1.000.000,00, maka total biaya produksi pada akhir minggu ke-3 adalah ....

- A. Rp3.400.000,00  
  <sub>Salah: Siswa salah menghitung tanda minus pada $-6(3^2)$ menjadi $+54$.</sub>
- B. Rp1.800.000,00  
  <sub>Salah: Siswa lupa menambahkan nilai konstanta biaya awal $C = 10$ ratusan ribu rupiah ($27 - 54 + 45 = 18$).</sub>
- **C. Rp2.800.000,00** ✅  
  <sub>Benar: Fungsi biaya total diperoleh dari antiturunan biaya marjinal: $f(x) = \int (3x^2 - 12x + 15)\,dx = x^3 - 6x^2 + 15x + C$. Pada $x = 0$, biaya Rp1.000.000,00 dinyatakan sebagai $10$ (dalam ratusan ribu rupiah), sehingga $C = 10$. Untuk $x = 3$: $f(3) = 3^3 - 6(3^2) + 15(3) + 10 = 27 - 54 + 45 + 10 = 28$ ratusan ribu rupiah, yaitu Rp2.800.000,00.</sub>
- D. Rp2.200.000,00  
  <sub>Salah: Siswa salah mengintegralkan $-12x$ menjadi $-12x^2$ alih-alih $-6x^2$.</sub>

**Pembahasan:** Fungsi biaya total $f(x)$ adalah antiturunan dari laju biaya tambahan $f'(x)$:
$$f(x) = \int (3x^2 - 12x + 15)\,dx = x^3 - 6x^2 + 15x + C$$

Biaya awal pada $x = 0$ adalah Rp1.000.000,00 = 10 ratusan ribu rupiah:
$$f(0) = C = 10$$
Sehingga fungsi biaya totalnya:
$$f(x) = x^3 - 6x^2 + 15x + 10$$

Pada akhir minggu ke-3 ($x = 3$):
$$f(3) = (3)^3 - 6(3)^2 + 15(3) + 10$$
$$f(3) = 27 - 54 + 45 + 10 = 28$$

Karena satuan dalam ratusan ribu rupiah, total biaya adalah $28 \times \text{Rp}100.000{,}00 = \text{Rp}2.800.000{,}00$.
**Acuan:** siswa — siswa hal.234

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b03-c-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: luas daerah kurva dengan sumbu x*

Luas daerah yang dibatasi oleh kurva $y = x^2 - 2x - 8$ dan sumbu-$x$ adalah ....

- **A. $36\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva dengan sumbu-$x$ diperoleh dari $x^2 - 2x - 8 = 0 \iff (x - 4)(x + 2) = 0$, sehingga $x = -2$ dan $x = 4$. Pada interval $[-2, 4]$, kurva berada di bawah sumbu-$x$ ($y \le 0$). Maka luasnya adalah $L = \int_{-2}^{4} -(x^2 - 2x - 8)\,dx = \left[-\frac{1}{3}x^3 + x^2 + 8x\right]_{-2}^{4} = \left(-\frac{64}{3} + 16 + 32\right) - \left(\frac{8}{3} + 4 - 16\right) = \frac{80}{3} - \left(-\frac{28}{3}\right) = \frac{108}{3} = 36$.</sub>
- B. $40\text{ satuan luas}$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada suku linear $2x$ saat mengintegralkan fungsi negatif.</sub>
- C. $18\text{ satuan luas}$  
  <sub>Salah: Siswa keliru hanya menghitung integral dari $x = 0$ sampai $x = 4$ atau membagi dua hasil akhir.</sub>
- D. $\frac{100}{3}\text{ satuan luas}$  
  <sub>Salah: Siswa salah menjumlahkan suku pecahan saat substitusi batas atas dan batas bawah.</sub>

**Pembahasan:** Tentukan pembuat nol fungsi:
$$x^2 - 2x - 8 = 0 \iff (x - 4)(x + 2) = 0 \iff x = -2 \text{ atau } x = 4$$
Karena kurva membuka ke atas, daerah yang dibatasi sumbu-$x$ berada di bawah sumbu-$x$ ($y \le 0$).
$$L = -\int_{-2}^{4} (x^2 - 2x - 8)\,dx = \int_{-2}^{4} (-x^2 + 2x + 8)\,dx$$
$$L = \left[ -\frac{1}{3}x^3 + x^2 + 8x \right]_{-2}^{4}$$
Substitusi batas:
$$L = \left(-\frac{64}{3} + 16 + 32\right) - \left(-\frac{1}{3}(-8) + 4 - 16\right)$$
$$L = \left(48 - \frac{64}{3}\right) - \left(\frac{8}{3} - 12\right) = \frac{80}{3} - \left(-\frac{28}{3}\right) = \frac{108}{3} = 36\text{ satuan luas}$$
**Acuan:** pretest — kelas12_tl-b03-p0227-latihan-soal-penerapan-integral-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b03-c-medium-bt01-006
*variasi (konteks) | C3 | 2 langkah | jenis: aplikasi konsumsi zat akumulatif*

Laju pemakaian bahan pelumas sebuah mesin pabrik dinyatakan oleh fungsi $r(t) = 3t^2 + 4t + 5$ (dalam liter per jam), dengan $t$ menyatakan lama mesin beroperasi dalam satuan jam. Total bahan pelumas yang digunakan mesin tersebut selama $3$ jam pertama pengoperasian adalah ....

- A. $45\text{ liter}$  
  <sub>Salah: Siswa lupa mengintegralkan suku konstanta $5$ sehingga menghasilkan $27 + 18 = 45$.</sub>
- **B. $60\text{ liter}$** ✅  
  <sub>Benar: Total pelumas yang terpakai dihitung dengan integral tentu dari $t = 0$ sampai $t = 3$: $V = \int_{0}^{3} (3t^2 + 4t + 5)\,dt = \left[t^3 + 2t^2 + 5t\right]_{0}^{3} = (3^3 + 2(3^2) + 5(3)) - 0 = 27 + 18 + 15 = 60\text{ liter}$.</sub>
- C. $44\text{ liter}$  
  <sub>Salah: Siswa hanya menghitung nilai laju sesaat pada akhir jam ke-3, yaitu $r(3) = 3(9) + 4(3) + 5 = 44$, bukan mengintegralkannya.</sub>
- D. $66\text{ liter}$  
  <sub>Salah: Siswa keliru mengintegralkan $4t$ menjadi $4t^2$ sehingga perhitungannya menjadi $27 + 36 + 15 = 78$ atau salah substitusi suku linear.</sub>

**Pembahasan:** Total pemakaian pelumas kumulatif diperoleh dari integral laju pemakaian terhadap waktu:
$$V = \int_{0}^{3} r(t)\,dt = \int_{0}^{3} (3t^2 + 4t + 5)\,dt$$
$$V = \left[ \frac{3}{3}t^3 + \frac{4}{2}t^2 + 5t \right]_{0}^{3} = \left[ t^3 + 2t^2 + 5t \right]_{0}^{3}$$
Substitusikan batas $t = 3$ dan $t = 0$:
$$V = (3^3 + 2(3^2) + 5(3)) - 0 = 27 + 18 + 15 = 60\text{ liter}$$
**Acuan:** siswa — siswa hal.230 Uji Kompetensi Bab 3 C

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b03-c-medium-bt01-007
*orisinal | C3 | 2 langkah | jenis: aplikasi fisika usaha gaya variabel*

Sebuah partikel bergerak di sepanjang lintasan lurus dan dipengaruhi oleh gaya $F(x) = 6x^2 - 4x + 3$ (dalam satuan Newton), dengan $x$ menyatakan posisi partikel dalam meter. Usaha yang dilakukan oleh gaya tersebut untuk memindahkan partikel dari posisi $x = 1\text{ m}$ ke posisi $x = 3\text{ m}$ adalah ....

- **A. $42\text{ Joule}$** ✅  
  <sub>Benar: Usaha dihitung dengan formula $W = \int_{x_1}^{x_2} F(x)\,dx = \int_{1}^{3} (6x^2 - 4x + 3)\,dx = \left[2x^3 - 2x^2 + 3x\right]_{1}^{3} = (2(27) - 2(9) + 3(3)) - (2(1) - 2(1) + 3(1)) = (54 - 18 + 9) - (2 - 2 + 3) = 45 - 3 = 42\text{ Joule}$.</sub>
- B. $39\text{ Joule}$  
  <sub>Salah: Siswa salah tanda saat mengevaluasi batas atas, menghitung $54 - 18 - 9 = 27$ atau keliru pada pengoperasian aljabar.</sub>
- C. $48\text{ Joule}$  
  <sub>Salah: Siswa salah menjumlahkan batas bawah alih-alih mengurangkannya ($45 + 3 = 48$).</sub>
- D. $45\text{ Joule}$  
  <sub>Salah: Siswa hanya menghitung hasil substitusi batas atas $x = 3$ dan lupa mengurangkan hasil substitusi batas bawah $x = 1$.</sub>

**Pembahasan:** Usaha $W$ oleh gaya variabel didefinisikan sebagai integral tentu dari gaya terhadap posisi:
$$W = \int_{1}^{3} F(x)\,dx = \int_{1}^{3} (6x^2 - 4x + 3)\,dx$$
$$W = \left[ 2x^3 - 2x^2 + 3x \right]_{1}^{3}$$
Evaluasi batas integral:
$$W = \left(2(3)^3 - 2(3)^2 + 3(3)\right) - \left(2(1)^3 - 2(1)^2 + 3(1)\right)$$
$$W = (54 - 18 + 9) - (2 - 2 + 3) = 45 - 3 = 42\text{ Joule}$$
**Acuan:** siswa — siswa hal.225

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b03-c-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: aplikasi nilai awal laju pertumbuhan*

Laju pertambahan tinggi suatu bibit tanaman dimodelkan oleh persamaan $\frac{dh}{dt} = 12\sqrt{t}$ (dalam cm per hari), dengan $t$ adalah waktu dalam hari sejak pengamatan dimulai. Jika tinggi bibit pada hari ke-$1$ ($t = 1$) adalah $18\text{ cm}$, maka tinggi bibit tanaman tersebut pada hari ke-$4$ ($t = 4$) adalah ....

- A. $64\text{ cm}$  
  <sub>Salah: Siswa mengabaikan konstanta integrasi $C$ dan langsung menghitung $8(4)^{3/2} = 64$.</sub>
- **B. $74\text{ cm}$** ✅  
  <sub>Benar: Tinggi tanaman diperoleh dari integrasi: $h(t) = \int 12t^{1/2}\,dt = 12 \cdot \frac{2}{3}t^{3/2} + C = 8t\sqrt{t} + C$. Diketahui $h(1) = 18$, maka $8(1) + C = 18 \implies C = 10$. Pada hari ke-4, tinggi bibit adalah $h(4) = 8(4)\sqrt{4} + 10 = 8(8) + 10 = 64 + 10 = 74\text{ cm}$.</sub>
- C. $56\text{ cm}$  
  <sub>Salah: Siswa hanya menghitung pertambahan tinggi kumulatif dari hari ke-1 sampai ke-4 ($\int_1^4 12\sqrt{t}\,dt = 56$) tanpa menambahkan tinggi awal $18\text{ cm}$.</sub>
- D. $82\text{ cm}$  
  <sub>Salah: Siswa keliru menentukan konstanta $C$, menjumlahkan $18 + 8 = 26$ sehingga $64 + 26 = 90$ atau salah hitung koefisien integral antiturunan.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi antiturunan dari laju pertumbuhan:
$$h(t) = \int 12\sqrt{t}\,dt = \int 12t^{\frac{1}{2}}\,dt = 12 \cdot \frac{2}{3}t^{\frac{3}{2}} + C = 8t^{\frac{3}{2}} + C$$

Langkah 2: Menggunakan nilai awal $h(1) = 18$ untuk menentukan $C$:
$$8(1)^{\frac{3}{2}} + C = 18 \iff 8 + C = 18 \iff C = 10$$
Sehingga fungsi tinggi bibit tanaman adalah $h(t) = 8t^{\frac{3}{2}} + 10$.

Langkah 3: Menghitung tinggi bibit pada hari ke-4 ($t = 4$):
$$h(4) = 8(4)^{\frac{3}{2}} + 10 = 8(8) + 10 = 64 + 10 = 74\text{ cm}$$
**Acuan:** siswa — siswa hal.233

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b03-c-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: luas daerah kurva dengan sumbu x*

Luas daerah yang dibatasi oleh kurva $y = x^2 - x - 6$ dan sumbu-$x$ adalah ....

- A. $\frac{115}{6}\text{ satuan luas}$  
  <sub>Salah: Siswa melakukan kesalahan aritmetika saat menjumlahkan pecahan pada batas bawah.</sub>
- B. $\frac{35}{6}\text{ satuan luas}$  
  <sub>Salah: Siswa keliru menggunakan batas integrasi dari $0$ ke $3$ alih-alih dari $-2$ ke $3$.</sub>
- C. $\frac{125}{3}\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengalikan koefisien setengah pada suku $x^2$ saat mencari antiturunan.</sub>
- **D. $\frac{125}{6}\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva dengan sumbu-$x$ dicari dari $x^2 - x - 6 = 0 \iff (x - 3)(x + 2) = 0$, menghasilkan $x = -2$ dan $x = 3$. Pada interval $[-2, 3]$, kurva berada di bawah sumbu-$x$, sehingga $L = -\int_{-2}^{3} (x^2 - x - 6)\,dx = \left[-\frac{1}{3}x^3 + \frac{1}{2}x^2 + 6x\right]_{-2}^{3} = \left(-9 + \frac{9}{2} + 18\right) - \left(\frac{8}{3} + 2 - 12\right) = \frac{27}{2} - \left(-\frac{22}{3}\right) = \frac{81 + 44}{6} = \frac{125}{6}\text{ satuan luas}$.</sub>

**Pembahasan:** Langkah 1: Menentukan batas integrasi melalui titik potong dengan sumbu-$x$ ($y = 0$):
$$x^2 - x - 6 = 0 \implies (x - 3)(x + 2) = 0 \implies x = -2 \text{ atau } x = 3$$

Langkah 2: Pada interval $[-2, 3]$, nilai fungsi $y \le 0$ (berada di bawah sumbu-$x$), sehingga luasnya adalah:
$$
\begin{aligned}
L &= -\int_{-2}^{3} (x^2 - x - 6)\,dx = \int_{-2}^{3} (-x^2 + x + 6)\,dx \\
&= \left[ -\frac{1}{3}x^3 + \frac{1}{2}x^2 + 6x \right]_{-2}^{3} \\
&= \left(-\frac{1}{3}(27) + \frac{1}{2}(9) + 6(3)\right) - \left(-\frac{1}{3}(-8) + \frac{1}{2}(4) + 6(-2)\right) \\
&= \left(-9 + \frac{9}{2} + 18\right) - \left(\frac{8}{3} + 2 - 12\right) \\
&= \frac{27}{2} - \left(-\frac{22}{3}\right) = \frac{27}{2} + \frac{22}{3} = \frac{81 + 44}{6} = \frac{125}{6}\text{ satuan luas}.
\end{aligned}
$$
**Acuan:** pretest — kelas12_tl-b03-p0227-latihan-soal-penerapan-integral-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b03-c-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: aplikasi fisika usaha pegas lanjut*

Sebuah gaya sebesar $50\text{ N}$ diperlukan untuk meregangkan sebuah pegas sejauh $0,1\text{ meter}$ melampaui panjang alaminya. Besar usaha yang diperlukan untuk meregangkan pegas tersebut lebih lanjut dari regangan $0,1\text{ meter}$ menjadi $0,3\text{ meter}$ adalah ....

- A. $10\text{ Joule}$  
  <sub>Salah: Siswa salah mengalikan faktor $1/2$ sebanyak dua kali sehingga menghasilkan setengah dari nilai yang benar.</sub>
- B. $40\text{ Joule}$  
  <sub>Salah: Siswa lupa membagi dengan 2 saat mencari antiturunan dari $kx$ ($W = k(x_2^2 - x_1^2)$).</sub>
- **C. $20\text{ Joule}$** ✅  
  <sub>Benar: Berdasarkan Hukum Hooke $F = kx$, maka $50 = k(0,1) \iff k = 500\text{ N/m}$. Usaha untuk meregangkan dari $x = 0,1\text{ m}$ ke $x = 0,3\text{ m}$ adalah $W = \int_{0,1}^{0,3} 500x\,dx = \left[250x^2\right]_{0,1}^{0,3} = 250(0,3^2 - 0,1^2) = 250(0,09 - 0,01) = 250(0,08) = 20\text{ Joule}$.</sub>
- D. $22,5\text{ Joule}$  
  <sub>Salah: Siswa menghitung usaha dari posisi setimbang $x = 0$ hingga $x = 0,3$ tanpa mengurangkan usaha awal dari $0$ ke $0,1$.</sub>

**Pembahasan:** Langkah 1: Menentukan konstanta pegas $k$ menggunakan Hukum Hooke:
$$f(x) = kx \implies 50 = k(0,1) \implies k = 500\text{ N/m}$$

Langkah 2: Menghitung usaha dengan integral tentu:
$$
\begin{aligned}
W &= \int_{0,1}^{0,3} 500x\,dx \\
&= \left[ 250x^2 \right]_{0,1}^{0,3} \\
&= 250(0,3)^2 - 250(0,1)^2 \\
&= 250(0,09) - 250(0,01) \\
&= 22,5 - 2,5 = 20\text{ Joule}.
\end{aligned}
$$
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b03-c-medium-bt01-011
*orisinal | C3 | 2 langkah | jenis: aplikasi akumulasi laju pemanenan*

Laju pemetikan buah kopi di sebuah perkebunan dinyatakan oleh fungsi $h(t) = -3t^2 + 18t$ (dalam kg per jam), dengan $t$ menyatakan waktu dalam jam sejak pemetikan dimulai pada pukul 07.00 ($t = 0$). Total hasil panen buah kopi yang dipetik dari pukul 07.00 hingga pukul 11.00 ($t = 4$) adalah ....

- A. $96\text{ kg}$  
  <sub>Salah: Siswa salah mengintegrasikan koefisien $-3t^2$ menjadi $-3t^3$ alih-alih $-t^3$.</sub>
- B. $144\text{ kg}$  
  <sub>Salah: Siswa hanya menghitung suku kedua $9t^2$ dan mengabaikan suku $-t^3$.</sub>
- C. $64\text{ kg}$  
  <sub>Salah: Siswa hanya menghitung nilai $t^3$ pada batas atas tanpa memperhatikan suku kedua.</sub>
- **D. $80\text{ kg}$** ✅  
  <sub>Benar: Total panen adalah integral dari fungsi laju panen pada interval $[0, 4]$: $\int_{0}^{4} (-3t^2 + 18t)\,dt = \left[-t^3 + 9t^2\right]_0^4 = -4^3 + 9(4^2) = -64 + 144 = 80\text{ kg}$.</sub>

**Pembahasan:** Waktu dari pukul 07.00 hingga 11.00 bersesuaian dengan interval waktu $t = 0$ sampai $t = 4$.
Total hasil panen diperoleh dengan mengintegralkan fungsi laju panen:
$$
\begin{aligned}
\text{Total Panen} &= \int_{0}^{4} (-3t^2 + 18t)\,dt \\
&= \left[ -\frac{3}{3}t^3 + \frac{18}{2}t^2 \right]_0^4 \\
&= \left[ -t^3 + 9t^2 \right]_0^4 \\
&= \left( -(4)^3 + 9(4)^2 \right) - 0 \\
&= -64 + 9(16) \\
&= -64 + 144 = 80\text{ kg}.
\end{aligned}
$$
**Acuan:** siswa — siswa hal.231

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b03-c-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: luas daerah antara dua kurva kuadrat*

Luas daerah yang dibatasi oleh kurva $y = 2x^2$ dan kurva $y = 12x - x^2$ adalah ....

- A. $16\text{ satuan luas}$  
  <sub>Salah: Siswa salah saat mengintegrasikan koefisien $12x$ menjadi $3x^2$ alih-alih $6x^2$.</sub>
- B. $48\text{ satuan luas}$  
  <sub>Salah: Siswa salah menjumlahkan kedua kurva alih-alih mengurangkan kurva atas dengan kurva bawah.</sub>
- C. $64\text{ satuan luas}$  
  <sub>Salah: Siswa lupa mengurangkan nilai batas atas pada suku berderajat tiga.</sub>
- **D. $32\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong dicari dengan menyamakan kedua kurva: $2x^2 = 12x - x^2 \iff 3x^2 - 12x = 0 \iff 3x(x - 4) = 0$, diperoleh batas $x = 0$ hingga $x = 4$. Pada interval $[0, 4]$, kurva $y = 12x - x^2$ berada di atas $y = 2x^2$. Luas daerah: $L = \int_{0}^{4} ((12x - x^2) - 2x^2)\,dx = \int_{0}^{4} (12x - 3x^2)\,dx = [6x^2 - x^3]_{0}^{4} = (6(16) - 64) - 0 = 96 - 64 = 32\text{ satuan luas}$.</sub>

**Pembahasan:** Menentukan titik potong kedua kurva:
$$2x^2 = 12x - x^2$$
$$3x^2 - 12x = 0$$
$$3x(x - 4) = 0$$
Diperoleh batas integrasi $x = 0$ sampai $x = 4$.

Menghitung luas daerah:
$$L = \int_{0}^{4} (12x - x^2 - 2x^2)\,dx$$
$$L = \int_{0}^{4} (12x - 3x^2)\,dx$$
$$L = \left[ 6x^2 - x^3 \right]_{0}^{4}$$
$$L = (6(4)^2 - 4^3) - 0 = 96 - 64 = 32\text{ satuan luas}.$$
**Acuan:** pretest — kelas12_tl-b03-p0228-latihan-soal-penerapan-integral-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b03-c-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: aplikasi nilai aset laju kenaikan harga*

Sebuah lukisan antik dibeli oleh seorang kolektor seharga Rp20.000.000,00. Laju pertambahan nilai jual lukisan tersebut terhadap waktu memenuhi persamaan $\frac{dV}{dt} = 6t^2 + 4t + 10$ (dalam ratusan ribu rupiah per tahun), dengan $t$ menyatakan waktu dalam tahun sejak pembelian. Nilai jual lukisan tersebut setelah 3 tahun adalah ....

- **A. Rp30.200.000,00** ✅  
  <sub>Benar: Pertambahan nilai lukisan selama 3 tahun pertama adalah $\Delta V = \int_{0}^{3} (6t^2 + 4t + 10)\,dt = [2t^3 + 2t^2 + 10t]_{0}^{3} = 2(27) + 2(9) + 10(3) = 54 + 18 + 30 = 102$ ratusan ribu rupiah, yang setara dengan Rp10.200.000,00. Nilai jual lukisan setelah 3 tahun: $V(3) = V(0) + \Delta V = \text{Rp}20.000.000,00 + \text{Rp}10.200.000,00 = \text{Rp}30.200.000,00$.</sub>
- B. Rp10.200.000,00  
  <sub>Salah: Siswa hanya menghitung besar pertambahan nilai lukisan tanpa menjumlahkannya dengan harga beli awal.</sub>
- C. Rp32.400.000,00  
  <sub>Salah: Siswa salah menyubstitusikan nilai $t = 3$ pada suku berderajat satu.</sub>
- D. Rp28.200.000,00  
  <sub>Salah: Siswa keliru mengintegralkan $6t^2$ menjadi $3t^3$ alih-alih $2t^3$.</sub>

**Pembahasan:** Menghitung akumulasi pertambahan nilai jual selama 3 tahun:
$$\Delta V = \int_{0}^{3} \left(6t^2 + 4t + 10\right)\,dt$$
$$\Delta V = \left[ 2t^3 + 2t^2 + 10t \right]_{0}^{3}$$
$$\Delta V = \left(2(3)^3 + 2(3)^2 + 10(3)\right) - 0$$
$$\Delta V = 54 + 18 + 30 = 102\text{ ratusan ribu rupiah}$$
$$\Delta V = \text{Rp}10.200.000,00$$

Nilai jual total setelah 3 tahun:
$$V(3) = V(0) + \Delta V = \text{Rp}20.000.000,00 + \text{Rp}10.200.000,00 = \text{Rp}30.200.000,00.$$
**Acuan:** siswa — siswa hal.232

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b03-c-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: aplikasi kesehatan laju penyembuhan luka*

Luas luka seorang pasien berkurang seiring berjalannya proses penyembuhan. Laju perubahan luas luka tersebut dimodelkan dengan fungsi $A'(t) = -0,6t + 0,4$ (dalam $\text{cm}^2/\text{hari}$), dengan $t$ menyatakan waktu dalam hari sejak perawatan dimulai. Jika pada hari ke-1 ($t = 1$) luas luka terukur $5,8\text{ cm}^2$, luas luka pasien tersebut yang diharapkan pada hari ke-4 ($t = 4$) adalah ....

- A. $2,1\text{ cm}^2$  
  <sub>Salah: Siswa salah saat mengintegrasikan $-0,6t$ menjadi $-0,6t^2$ alih-alih $-0,3t^2$.</sub>
- **B. $2,5\text{ cm}^2$** ✅  
  <sub>Benar: Perubahan luas luka dari hari ke-1 sampai ke-4 dihitung melalui integral tentu: $\Delta A = \int_{1}^{4} (-0,6t + 0,4)\,dt = [-0,3t^2 + 0,4t]_{1}^{4} = (-0,3(16) + 0,4(4)) - (-0,3(1) + 0,4(1)) = (-4,8 + 1,6) - (-0,3 + 0,4) = -3,2 - 0,1 = -3,3\text{ cm}^2$. Luas luka pada hari ke-4: $A(4) = A(1) + \Delta A = 5,8 + (-3,3) = 2,5\text{ cm}^2$.</sub>
- C. $4,1\text{ cm}^2$  
  <sub>Salah: Siswa salah mengevaluasi batas bawah integral sehingga perubahan luas terhitung $-1,7\text{ cm}^2$.</sub>
- D. $3,3\text{ cm}^2$  
  <sub>Salah: Siswa hanya menghitung besar penyusutan luas luka tanpa mengurangkannya dari luas luka pada hari ke-1.</sub>

**Pembahasan:** Menghitung total perubahan luas luka antara $t = 1$ dan $t = 4$:
$$\Delta A = \int_{1}^{4} (-0,6t + 0,4)\,dt$$
$$\Delta A = \left[ -0,3t^2 + 0,4t \right]_{1}^{4}$$
Evaluasi batas atas ($t = 4$):
$$-0,3(4)^2 + 0,4(4) = -4,8 + 1,6 = -3,2$$
Evaluasi batas bawah ($t = 1$):
$$-0,3(1)^2 + 0,4(1) = -0,3 + 0,4 = 0,1$$
$$\Delta A = -3,2 - 0,1 = -3,3\text{ cm}^2$$

Luas luka pada hari ke-4:
$$A(4) = A(1) + \Delta A = 5,8 + (-3,3) = 2,5\text{ cm}^2.$$
**Acuan:** siswa — siswa hal.227

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b03-c-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: aplikasi ekonomi penerimaan total*

Laju pendapatan sebuah gerai UMKM dinyatakan oleh fungsi $R'(t) = 60 - 4t$ (dalam puluhan ribu rupiah per jam), dengan $t$ menyatakan waktu operasional dalam jam sejak gerai dibuka ($0 \le t \le 10$). Total pendapatan yang diperoleh gerai tersebut selama $5$ jam pertama operasional adalah ....

- A. Rp1.250.000,00  
  <sub>Salah: Salah membagi hasil integral dengan dua karena keliru menerapkan rumus luas segitiga.</sub>
- B. Rp3.500.000,00  
  <sub>Salah: Kesalahan tanda operasi pada antiturunan sehingga menghitung $300 + 50 = 350$ puluhan ribu rupiah.</sub>
- **C. Rp2.500.000,00** ✅  
  <sub>Benar: Total pendapatan diperoleh dari $\int_{0}^{5} (60 - 4t)\,dt = [60t - 2t^2]_0^5 = 60(5) - 2(5)^2 = 300 - 50 = 250$ puluhan ribu rupiah, yang setara dengan Rp2.500.000,00.</sub>
- D. Rp2.000.000,00  
  <sub>Salah: Lupa membagi koefisien dengan pangkat baru saat mengintegralkan $4t$ sehingga memperoleh $60(5) - 4(25) = 200$ puluhan ribu rupiah.</sub>

**Pembahasan:** Total pendapatan $R$ selama $5$ jam pertama ($t = 0$ hingga $t = 5$) dihitung dengan mengintegralkan fungsi laju pendapatan:
$$\begin{aligned} R &= \int_{0}^{5} R'(t)\,dt \\ &= \int_{0}^{5} (60 - 4t)\,dt \\ &= \left[ 60t - 2t^2 \right]_{0}^{5} \\ &= \left(60(5) - 2(5)^2\right) - 0 \\ &= 300 - 50 = 250 \text{ puluhan ribu rupiah} \end{aligned}$$
Nilai dalam rupiah:
$$250 \times \text{Rp}10.000,00 = \text{Rp}2.500.000,00$$
**Acuan:** siswa — siswa hal.223

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b03-c-medium-bt01-016
*variasi (angka) | C3 | 3 langkah | jenis: luas daerah kurva bentuk akar*

Luas daerah di kuadran pertama yang dibatasi oleh kurva $f(x) = x\sqrt{x^2 + 16}$, sumbu-$x$, dan garis $x = 3$ adalah ....

- **A. $\frac{61}{3}\text{ satuan luas}$** ✅  
  <sub>Benar: Batas integrasi di kuadran pertama adalah $x = 0$ sampai $x = 3$. Melalui substitusi $u = x^2 + 16$, diperoleh $\int_0^3 x\sqrt{x^2+16}\,dx = \frac{1}{3}\left[(x^2+16)^{3/2}\right]_0^3 = \frac{1}{3}(125 - 64) = \frac{61}{3}\text{ satuan luas}$.</sub>
- B. $\frac{61}{2}\text{ satuan luas}$  
  <sub>Salah: Salah menentukan antiturunan dari $u^{1/2}$, menggunakan koefisien $\frac{1}{2}$ bukannya $\frac{2}{3}$.</sub>
- C. $\frac{125}{3}\text{ satuan luas}$  
  <sub>Salah: Lupa menyubstitusikan batas bawah $x = 0$ ke dalam $(x^2 + 16)^{3/2}$, menganggap nilainya 0.</sub>
- D. $\frac{122}{3}\text{ satuan luas}$  
  <sub>Salah: Lupa membagi dengan faktor 2 dari turunan $du = 2x\,dx$ saat melakukan integrasi substitusi.</sub>

**Pembahasan:** Daerah berada di kuadran pertama, sehingga batas kirinya adalah perpotongan kurva dengan sumbu-$x$, yaitu $x = 0$, dan batas kanannya adalah garis $x = 3$.

Luas daerah dinyatakan oleh integral tentu:
$$L = \int_{0}^{3} x\sqrt{x^2 + 16}\,dx$$

Gunakan metode substitusi:
Misalkan $u = x^2 + 16$, sehingga $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,du$.
Ubah batas integrasi:
- Untuk $x = 0 \implies u = 0^2 + 16 = 16$
- Untuk $x = 3 \implies u = 3^2 + 16 = 25$

Substitusikan ke dalam integral:
$$L = \int_{16}^{25} \frac{1}{2} u^{1/2}\,du = \frac{1}{2} \left[ \frac{2}{3}u^{3/2} \right]_{16}^{25} = \frac{1}{3} \left[ u^{3/2} \right]_{16}^{25}$$
$$L = \frac{1}{3} \left( 25^{3/2} - 16^{3/2} \right) = \frac{1}{3} \left( 125 - 64 \right) = \frac{61}{3}$$

Jadi, luas daerah tersebut adalah $\frac{61}{3}\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.220 Contoh Soal 3.13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [hard] kelas12_tl-b03-c-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: usaha peregangan/pengangkatan fisika*

Sebuah rantai derek seberat 120 kg memiliki panjang 40 meter dan tergantung vertikal pada derek pelabuhan. Dengan percepatan gravitasi $g = 10\text{ m/s}^2$, usaha yang diperlukan untuk menarik seluruh rantai tersebut sampai ke puncak derek adalah ....

- A. $12.000\text{ Joule}$  
  <sub>Salah: Membagi dua kembali hasil akhir usaha yang sudah benar.</sub>
- B. $48.000\text{ Joule}$  
  <sub>Salah: Mengalikan berat total langsung dengan panjang rantai ($1.200 \times 40$) tanpa memperhitungkan bahwa beban berkurang secara kontinu saat rantai ditarik ke atas.</sub>
- **C. $24.000\text{ Joule}$** ✅  
  <sub>Benar: Rapat massa linear rantai adalah $\lambda = \frac{120\text{ kg}}{40\text{ m}} = 3\text{ kg/m}$. Elemen rantai sepanjang $dx$ di kedalaman $x$ meter memiliki berat $dF = \lambda g dx = 3 \times 10 \, dx = 30 \, dx$ Newton. Usaha untuk mengangkat elemen tersebut sejauh $x$ meter adalah $dW = x \, dF = 30x \, dx$. Total usaha mengangkat seluruh rantai: $W = \int_{0}^{40} 30x \, dx = \left[15x^2\right]_{0}^{40} = 15 \times (40)^2 = 15 \times 1.600 = 24.000\text{ Joule}$.</sub>
- D. $2.400\text{ Joule}$  
  <sub>Salah: Lupa mengalikan dengan percepatan gravitasi $g = 10\text{ m/s}^2$.</sub>

**Pembahasan:** Rapat massa rantai per satuan panjang:
$$\lambda = \frac{M}{L} = \frac{120\text{ kg}}{40\text{ m}} = 3\text{ kg/m}$$
Gaya berat elemen rantai sepanjang $dx$ pada jarak $x$ dari puncak:
$$dF = (\lambda \, dx) \cdot g = 3 \cdot 10 \, dx = 30 \, dx\text{ N}$$
Elemen ini harus ditarik ke atas sejauh $x$, sehingga usaha elemennya adalah:
$$dW = x \cdot dF = 30x \, dx$$
Total usaha untuk menarik seluruh rantai dari $x = 0$ hingga $x = 40$:
$$W = \int_{0}^{40} 30x \, dx = \left[ 15x^2 \right]_{0}^{40} = 15(40^2) - 0 = 15 \times 1.600 = 24.000\text{ Joule}.$$
**Acuan:** siswa — siswa hal.228 Latihan Soal Penerapan Integral

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [hard] kelas12_tl-b03-c-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: penentuan parameter luas*

Daerah tertutup dibatasi oleh kurva parabola $y = ax - x^2$ dan $y = x^2 - ax$ dengan $a > 0$. Jika luas daerah yang terbentuk sama dengan $72\text{ satuan luas}$, nilai $a$ yang memenuhi adalah ....

- A. $4$  
  <sub>Salah: Salah melakukan integrasi suku $2ax$ menjadi $ax$ sehingga koefisien luas menjadi keliru.</sub>
- B. $3$  
  <sub>Salah: Keliru menggunakan rumus luas parabola tunggal terhadap sumbu-$x$ yaitu $\frac{1}{6}a^3 = 72$ yang menghasilkan perhitungan keliru.</sub>
- C. $8$  
  <sub>Salah: Salah menarik akar pangkat tiga dari $216$ menjadi $8$.</sub>
- **D. $6$** ✅  
  <sub>Benar: Titik potong kedua kurva dicari dari $ax - x^2 = x^2 - ax \iff 2x^2 - 2ax = 0 \iff 2x(x - a) = 0$, yaitu $x = 0$ dan $x = a$. Pada interval $[0, a]$, kurva $y = ax - x^2$ berada di atas $y = x^2 - ax$. Luas daerahnya: $L = \int_{0}^{a} ((ax - x^2) - (x^2 - ax)) \, dx = \int_{0}^{a} (2ax - 2x^2) \, dx = \left[ ax^2 - \frac{2}{3}x^3 \right]_{0}^{a} = a^3 - \frac{2}{3}a^3 = \frac{1}{3}a^3$. Diketahui luas daerah $= 72$, sehingga $\frac{1}{3}a^3 = 72 \iff a^3 = 216 \iff a = 6$.</sub>

**Pembahasan:** Tentukan titik potong kedua kurva:
$$ax - x^2 = x^2 - ax \implies 2x^2 - 2ax = 0 \implies 2x(x - a) = 0$$
Maka titik potong berada pada $x = 0$ dan $x = a$.

Untuk $0 \le x \le a$, $ax - x^2 \ge x^2 - ax$, sehingga luasnya adalah:
$$L = \int_{0}^{a} \left((ax - x^2) - (x^2 - ax)\right) dx = \int_{0}^{a} (2ax - 2x^2) dx$$
$$L = \left[ ax^2 - \frac{2}{3}x^3 \right]_{0}^{a} = a(a^2) - \frac{2}{3}a^3 = \frac{1}{3}a^3$$

Diketahui luas $L = 72\text{ satuan luas}$:
$$\frac{1}{3}a^3 = 72 \implies a^3 = 216 \implies a = 6.$$
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [hard] kelas12_tl-b03-c-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: aplikasi ekonomi integrasi netto*

Sebuah pabrik mengoperasikan mesin baru. Laju penghematan biaya operasional dinyatakan oleh fungsi $f(t) = 6.000t + 3.000$ (rupiah per tahun), sedangkan laju biaya pemeliharaan mesin bertambah menurut fungsi $g(t) = 2.000t + 1.000$ (rupiah per tahun), dengan $t$ menyatakan waktu pemakaian dalam tahun. Total keuntungan finansial bersih kumulatif mesin tersebut mencapai Rp60.000,00 setelah beroperasi selama ....

- A. $6\text{ tahun}$  
  <sub>Salah: Mengambil nilai mutlak dari akar negatif persamaan kuadrat $(T = -6)$.</sub>
- **B. $5\text{ tahun}$** ✅  
  <sub>Benar: Laju keuntungan finansial bersih adalah $r(t) = f(t) - g(t) = (6.000t + 3.000) - (2.000t + 1.000) = 4.000t + 2.000$ rupiah per tahun. Keuntungan bersih kumulatif selama $T$ tahun adalah $K(T) = \int_{0}^{T} (4.000t + 2.000) \, dt = \left[2.000t^2 + 2.000t\right]_{0}^{T} = 2.000T^2 + 2.000T$. Kita menginginkan $K(T) = 60.000$, maka $2.000T^2 + 2.000T = 60.000 \iff T^2 + T - 30 = 0 \iff (T + 6)(T - 5) = 0$. Karena $T > 0$, diperoleh $T = 5\text{ tahun}$.</sub>
- C. $10\text{ tahun}$  
  <sub>Salah: Menghitung tanpa integral, hanya membagi Rp60.000 dengan keuntungan tahun pertama $r(1) = 6.000$.</sub>
- D. $4\text{ tahun}$  
  <sub>Salah: Hanya mengintegralkan laju penghematan $f(t)$ tanpa memperhitungkan biaya pemeliharaan $g(t)$ ($3.000T^2 + 3.000T = 60.000 \implies T = 4$).</sub>

**Pembahasan:** Tentukan fungsi laju keuntungan bersih per tahun:
$$r(t) = f(t) - g(t) = (6.000t + 3.000) - (2.000t + 1.000) = 4.000t + 2.000$$

Total keuntungan bersih kumulatif selama $T$ tahun diperoleh dari integral tentu:
$$K(T) = \int_{0}^{T} (4.000t + 2.000) \, dt = \left[ 2.000t^2 + 2.000t \right]_{0}^{T} = 2.000T^2 + 2.000T$$

Samakan dengan Rp60.000,00:
$$2.000T^2 + 2.000T = 60.000$$
Bagi kedua ruas dengan $2.000$:
$$T^2 + T - 30 = 0$$
$$(T + 6)(T - 5) = 0$$
Karena waktu pemakaian $T > 0$, maka $T = 5\text{ tahun}$.
**Acuan:** siswa — siswa hal.224

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas12_tl-b03-c-hard-bt01-004
*orisinal | C5 | 4 langkah | jenis: luas daerah kurva kubik*

Luas total daerah tertutup yang dibatasi oleh kurva $y = x^3 - 4x$ dan sumbu-$x$ adalah ....

- **A. $8\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva dengan sumbu-$x$ diperoleh dari $x^3 - 4x = 0 \iff x(x - 2)(x + 2) = 0$, yaitu $x = -2, 0, 2$. Pada interval $[-2, 0]$, fungsi bernilai nonnegatif ($y \ge 0$), sedangkan pada $[0, 2]$, fungsi bernilai nonpositif ($y \le 0$). Luas total harus dihitung terpisah: $L = \int_{-2}^{0} (x^3 - 4x) \, dx - \int_{0}^{2} (x^3 - 4x) \, dx$. Antiturunan dari $x^3 - 4x$ adalah $F(x) = \frac{1}{4}x^4 - 2x^2$. Pada $[-2, 0]$: $F(0) - F(-2) = 0 - (4 - 8) = 4$. Pada $[0, 2]$: $-(F(2) - F(0)) = -(4 - 8 - 0) = 4$. Jadi luas total $L = 4 + 4 = 8\text{ satuan luas}$.</sub>
- B. $4\text{ satuan luas}$  
  <sub>Salah: Hanya menghitung salah satu subinterval saja ($[-2, 0]$ atau $[0, 2]$).</sub>
- C. $16\text{ satuan luas}$  
  <sub>Salah: Keliru dalam mencari antiturunan menjadi $x^4 - 4x^2$ tanpa membagi pangkatnya.</sub>
- D. $0\text{ satuan luas}$  
  <sub>Salah: Mengintegrasikan langsung kurva dari $-2$ sampai $2$ tanpa memecah subinterval, sehingga luas daerah positif dan negatif saling menghilangkan.</sub>

**Pembahasan:** Tentukan titik potong dengan sumbu-$x$ ($y = 0$):
$$x^3 - 4x = 0 \implies x(x - 2)(x + 2) = 0$$
Akar-akarnya adalah $x = -2$, $x = 0$, dan $x = 2$.

Periksa tanda fungsi:
- Pada $[-2, 0]$: grafik berada di atas sumbu-$x$ ($y \ge 0$).
- Pada $[0, 2]$: grafik berada di bawah sumbu-$x$ ($y \le 0$).

Maka luas total adalah jumlahan dari kedua daerah:
$$L = \int_{-2}^{0} (x^3 - 4x) \, dx + \int_{0}^{2} -(x^3 - 4x) \, dx$$
Antiturunan dari $x^3 - 4x$ adalah $F(x) = \frac{1}{4}x^4 - 2x^2$.
$$L_1 = \left[ \frac{1}{4}x^4 - 2x^2 \right]_{-2}^{0} = 0 - \left(\frac{1}{4}(-2)^4 - 2(-2)^2\right) = -(4 - 8) = 4$$
$$L_2 = -\left[ \frac{1}{4}x^4 - 2x^2 \right]_{0}^{2} = -\left(\frac{1}{4}(2)^4 - 2(2)^2 - 0\right) = -(4 - 8) = 4$$
$$L = L_1 + L_2 = 4 + 4 = 8\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.221

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b03-c-hard-bt01-005
*variasi (angka) | C5 | 4 langkah | jenis: usaha pegas fisika*

Sebuah gaya sebesar $60\text{ N}$ diperlukan untuk menahan sebuah pegas yang direntangkan dari panjang alaminya $20\text{ cm}$ menjadi sepanjang $26\text{ cm}$. Berdasarkan Hukum Hooke, besar usaha yang diperlukan untuk meregangkan pegas tersebut lebih lanjut dari panjang $26\text{ cm}$ menjadi $30\text{ cm}$ adalah ....

- A. $5,0\text{ Joule}$  
  <sub>Salah: Mengintegrasikan dari $x = 0$ hingga batas akhir $0,10\text{ m}$ tanpa mengurangkan usaha regangan awal.</sub>
- B. $320\text{ Joule}$  
  <sub>Salah: Lupa mengonversi satuan pertambahan panjang sentimeter ke meter saat proses integrasi.</sub>
- C. $1,8\text{ Joule}$  
  <sub>Salah: Menggunakan selisih regangan $0,04\text{ m}$ langsung ke dalam rumus $\frac{1}{2}k(\Delta x)^2 = 500(0,04)^2$.</sub>
- **D. $3,2\text{ Joule}$** ✅  
  <sub>Benar: Pertambahan panjang awal $x_0 = 26\text{ cm} - 20\text{ cm} = 6\text{ cm} = 0,06\text{ m}$. Berdasarkan $F = kx$, diperoleh $60 = k(0,06) \iff k = 1.000\text{ N/m}$. Batas regangan terhadap panjang alami adalah $x_1 = 0,06\text{ m}$ dan $x_2 = 30\text{ cm} - 20\text{ cm} = 0,10\text{ m}$. Usaha dihitung dengan $W = \int_{0,06}^{0,10} 1.000x\,dx = \left[500x^2\right]_{0,06}^{0,10} = 500(0,01 - 0,0036) = 500(0,0064) = 3,2\text{ Joule}$.</sub>

**Pembahasan:** Berdasarkan Hukum Hooke, besar gaya pegas adalah $F(x) = kx$, di mana $x$ menyatakan pertambahan panjang dari posisi seimbang.
1. Menentukan konstanta pegas $k$:
$\Delta x = 26\text{ cm} - 20\text{ cm} = 6\text{ cm} = 0,06\text{ m}$.
$F = kx \implies 60 = k(0,06) \implies k = 1.000\text{ N/m}$.
2. Menentukan batas integrasi dari panjang alami:
$x_1 = 26\text{ cm} - 20\text{ cm} = 0,06\text{ m}$
$x_2 = 30\text{ cm} - 20\text{ cm} = 0,10\text{ m}$
3. Menghitung usaha $W$:
$W = \int_{x_1}^{x_2} kx\,dx = \int_{0,06}^{0,10} 1.000x\,dx = \left[ 500x^2 \right]_{0,06}^{0,10} = 500(0,10^2 - 0,06^2) = 500(0,01 - 0,0036) = 500(0,0064) = 3,2\text{ Joule}$.
**Acuan:** siswa — siswa hal.226 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b03-c-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: penentuan parameter kurva*

Diketahui kurva $f(x) = x\sqrt{x^2 + c}$ dengan $c > 0$. Jika luas daerah di kuadran pertama yang dibatasi oleh kurva $y = f(x)$, sumbu-$x$, sumbu-$y$, dan garis $x = 2\sqrt{2}$ sama dengan $\frac{26}{3}\text{ satuan luas}$, nilai konstanta $c$ adalah ....

- A. $9$  
  <sub>Salah: Tertukar antara nilai $(8 + c)$ dengan nilai $c$ itu sendiri.</sub>
- B. $4$  
  <sub>Salah: Lupa mengurangkan batas bawah $c^{3/2}$ saat evaluasi integral sehingga menghitung $(8+c)^{3/2} = 26$ lalu menebak $c = 4$.</sub>
- C. $2$  
  <sub>Salah: Menyamakan hasil substitusi langsung $8 + c = 26$ sehingga mengira nilai $c$ mendekati bilangan bulat genap.</sub>
- **D. $1$** ✅  
  <sub>Benar: Luas daerah dinyatakan oleh $\int_0^{2\sqrt{2}} x\sqrt{x^2 + c}\,dx = \left[ \frac{1}{3}(x^2 + c)^{3/2} \right]_0^{2\sqrt{2}} = \frac{1}{3}\left((8 + c)^{3/2} - c^{3/2}\right)$. Disetarakan dengan $\frac{26}{3}$, diperoleh $(8 + c)^{3/2} - c^{3/2} = 26$. Untuk $c = 1$, $(9)^{3/2} - (1)^{3/2} = 27 - 1 = 26$, sehingga $c = 1$.</sub>

**Pembahasan:** 1. Integral luas daerah di kuadran I:
$L = \int_{0}^{2\sqrt{2}} x\sqrt{x^2 + c}\,dx$.
2. Gunakan substitusi $u = x^2 + c$, sehingga $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}du$:
$\int x(x^2 + c)^{1/2}\,dx = \frac{1}{2} \cdot \frac{2}{3}(x^2 + c)^{3/2} = \frac{1}{3}(x^2 + c)^{3/2}$.
3. Masukkan batas $x = 0$ hingga $x = 2\sqrt{2}$:
$L = \left[ \frac{1}{3}(x^2 + c)^{3/2} \right]_0^{2\sqrt{2}} = \frac{1}{3}\left( ((2\sqrt{2})^2 + c)^{3/2} - (0^2 + c)^{3/2} \right) = \frac{1}{3}\left( (8 + c)^{3/2} - c^{3/2} \right)$.
4. Menentukan nilai $c$:
$\frac{1}{3}\left( (8 + c)^{3/2} - c^{3/2} \right) = \frac{26}{3} \iff (8 + c)^{3/2} - c^{3/2} = 26$.
Uji $c = 1$:
$(8 + 1)^{3/2} - 1^{3/2} = 9^{3/2} - 1 = (\sqrt{9})^3 - 1 = 27 - 1 = 26$ (memenuhi).
Jadi, nilai konstanta $c = 1$.
**Acuan:** siswa — siswa hal.220

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b03-c-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: laju penghematan investasi*

Sebuah perusahaan manufaktur membeli mesin pendingin baru seharga $\text{Rp}60.000,00$. Pengoperasian mesin tersebut menghasilkan penghematan biaya operasional dengan laju $f(t) = 9.000t + 4.000$ (rupiah per tahun). Namun, mesin memerlukan biaya perawatan berkala dengan laju penambahan biaya $g(t) = 3.000t + 1.000$ (rupiah per tahun), dengan $t$ menyatakan waktu pemakaian dalam tahun. Dalam berapa tahun penghematan operasional neto akan menutup seluruh harga pembelian mesin tersebut?

- **A. $4\text{ tahun}$** ✅  
  <sub>Benar: Laju penghematan neto adalah $h(t) = f(t) - g(t) = (9.000t + 4.000) - (3.000t + 1.000) = 6.000t + 3.000$. Total penghematan neto selama $T$ tahun adalah $\int_0^T (6.000t + 3.000)\,dt = 3.000T^2 + 3.000T$. Disetarakan dengan harga beli: $3.000T^2 + 3.000T = 60.000 \iff T^2 + T - 20 = 0 \iff (T + 5)(T - 4) = 0$. Karena $T > 0$, diperoleh $T = 4\text{ tahun}$.</sub>
- B. $6\text{ tahun}$  
  <sub>Salah: Salah membagi saat menyederhanakan koefisien persamaan kuadrat $3.000T^2 + 3.000T = 60.000$.</sub>
- C. $3\text{ tahun}$  
  <sub>Salah: Hanya menghitung dari laju $f(t)$ tanpa mengurangi laju biaya perawatan $g(t)$ sehingga menghasilkan $T$ lebih cepat.</sub>
- D. $5\text{ tahun}$  
  <sub>Salah: Mengambil akar negatif persamaan kuadrat $T = -5$ dan memutlakkan nilainya.</sub>

**Pembahasan:** 1. Tentukan laju penghematan neto per tahun:
$h(t) = f(t) - g(t) = (9.000t + 4.000) - (3.000t + 1.000) = 6.000t + 3.000$.
2. Total penghematan neto dalam $T$ tahun dirumuskan sebagai integral tentu:
$S(T) = \int_0^T (6.000t + 3.000)\,dt = \left[ 3.000t^2 + 3.000t \right]_0^T = 3.000T^2 + 3.000T$.
3. Titik impas (harga beli kembali) tercapai saat $S(T) = 60.000$:
$3.000T^2 + 3.000T = 60.000$.
Bagi kedua ruas dengan $3.000$:
$T^2 + T = 20 \iff T^2 + T - 20 = 0$.
4. Faktorkan persamaan kuadrat:
$(T + 5)(T - 4) = 0 \implies T = -5 \text{ atau } T = 4$.
Karena waktu $T$ harus bernilai positif, maka $T = 4\text{ tahun}$.
**Acuan:** siswa — siswa hal.224

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b03-c-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: luas daerah kurva dan garis singgung*

Sebuah bidang datar di kuadran pertama dibatasi oleh sumbu-$y$, kurva parabola $y = 4 - x^2$, dan garis singgung kurva tersebut di titik $(1, 3)$. Luas bidang datar tersebut adalah ....

- A. $1\text{ satuan luas}$  
  <sub>Salah: Hanya menghitung luas segitiga di bawah garis singgung tanpa mengurangkan luas di bawah kurva parabola.</sub>
- B. $\frac{5}{3}\text{ satuan luas}$  
  <sub>Salah: Tertukar posisi batas fungsi atas dan fungsi bawah sehingga menambahkan luas daerah di bawah parabola.</sub>
- **C. $\frac{1}{3}\text{ satuan luas}$** ✅  
  <sub>Benar: Turunan kurva adalah $y' = -2x$. Di titik $(1, 3)$, gradiennya $m = -2(1) = -2$, sehingga persamaan garis singgung adalah $y - 3 = -2(x - 1) \iff y = -2x + 5$. Di kuadran pertama antara $x = 0$ dan $x = 1$, garis singgung berada di atas parabola. Luas daerah $L = \int_0^1 ((-2x + 5) - (4 - x^2))\,dx = \int_0^1 (x^2 - 2x + 1)\,dx = \left[ \frac{1}{3}x^3 - x^2 + x \right]_0^1 = \frac{1}{3} - 1 + 1 = \frac{1}{3}\text{ satuan luas}$.</sub>
- D. $\frac{2}{3}\text{ satuan luas}$  
  <sub>Salah: Keliru mengintegrasikan selisih fungsi menjadi $(x^2 - 2x + 2)$.</sub>

**Pembahasan:** 1. Menentukan persamaan garis singgung kurva $y = 4 - x^2$ di titik $(1, 3)$:
$y' = \frac{dy}{dx} = -2x$.
Gradien di titik $(1, 3)$ adalah $m = -2(1) = -2$.
Persamaan garis singgung:
$y - y_1 = m(x - x_1) \implies y - 3 = -2(x - 1) \implies y = -2x + 5$.
2. Menentukan interval integrasi dan posisi kurva:
Daerah dibatasi oleh sumbu-$y$ ($x = 0$) hingga titik singgung ($x = 1$).
Pada interval $0 \le x \le 1$, garis $y = -2x + 5$ selalu berada di atas kurva parabola $y = 4 - x^2$.
3. Menyusun rumus luas daerah:
$L = \int_{0}^{1} \left[ (-2x + 5) - (4 - x^2) \right]\,dx = \int_{0}^{1} (x^2 - 2x + 1)\,dx$.
4. Menghitung integral tentu:
$L = \left[ \frac{1}{3}x^3 - x^2 + x \right]_0^1 = \left( \frac{1}{3}(1)^3 - (1)^2 + 1 \right) - 0 = \frac{1}{3} - 1 + 1 = \frac{1}{3}\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.234

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b03-c-hard-bt01-009
*variasi (angka) | C5 | 4 langkah | jenis: luas daerah kuadran tertentu*

Tentukan luas daerah di kuadran keempat yang dibatasi oleh fungsi $f(x) = x^2 - 8x$, sumbu-$x$, garis $x = 2$, dan garis $x = 6$.

- **A. $\frac{176}{3}\text{ satuan luas}$** ✅  
  <sub>Benar: Pada interval $[2, 6]$, kurva $f(x) = x(x - 8) \le 0$ berada di bawah sumbu-$x$ (kuadran IV). Luas daerahnya adalah $L = -\int_{2}^{6} (x^2 - 8x)\,dx = \int_{2}^{6} (8x - x^2)\,dx = \left[4x^2 - \frac{1}{3}x^3\right]_{2}^{6} = \left(4(36) - \frac{216}{3}\right) - \left(4(4) - \frac{8}{3}\right) = 72 - \frac{40}{3} = \frac{176}{3}\text{ satuan luas}$.</sub>
- B. $-\frac{176}{3}\text{ satuan luas}$  
  <sub>Salah: Lupa mengalikan dengan tanda negatif untuk daerah di bawah sumbu-$x$ sehingga menghasilkan luas bernilai negatif.</sub>
- C. $\frac{208}{3}\text{ satuan luas}$  
  <sub>Salah: Kesalahan tanda operasi saat proses integrasi menjadi $4x^2 + \frac{1}{3}x^3$.</sub>
- D. $\frac{160}{3}\text{ satuan luas}$  
  <sub>Salah: Kesalahan perhitungan tanda saat mengevaluasi batas bawah integral sehingga batas bawah bernilai $\frac{56}{3}$.</sub>

**Pembahasan:** Langkah 1: Periksa posisi kurva pada interval $[2, 6]$. Karena pembuat nol dari $f(x) = x^2 - 8x$ adalah $x = 0$ dan $x = 8$, maka untuk setiap $x \in [2, 6]$ nilai $f(x) \le 0$ (kurva berada di bawah sumbu-$x$).
Langkah 2: Rumuskan integral luas daerah: $L = -\int_{2}^{6} (x^2 - 8x)\,dx = \int_{2}^{6} (8x - x^2)\,dx$.
Langkah 3: Tentukan antiturunan fungsinya: $\int (8x - x^2)\,dx = 4x^2 - \frac{1}{3}x^3$.
Langkah 4: Hitung nilai tentu pada batas-batasnya:
$L = \left[4(6)^2 - \frac{1}{3}(6)^3\right] - \left[4(2)^2 - \frac{1}{3}(2)^3\right] = (144 - 72) - \left(16 - \frac{8}{3}\right) = 72 - \frac{40}{3} = \frac{176}{3}\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.221 Ayo Mencoba 3.11

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b03-c-hard-bt01-010
*variasi (angka) | C5 | 4 langkah | jenis: luas daerah perpotongan dua kurva*

Tentukan luas daerah yang dibatasi oleh kurva parabola $y = 2x^2$ dan $y = 15x - x^2$.

- A. $\frac{75}{2}\text{ satuan luas}$  
  <sub>Salah: Salah menentukan titik potong atas kedua kurva dengan mengambil nilai $x = 3$.</sub>
- **B. $\frac{125}{2}\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva diperoleh dari $2x^2 = 15x - x^2 \iff 3x^2 - 15x = 0 \iff 3x(x - 5) = 0$, yaitu $x = 0$ dan $x = 5$. Pada interval $[0, 5]$, kurva $y = 15x - x^2$ berada di atas $y = 2x^2$. Maka luas daerahnya adalah $L = \int_{0}^{5} ((15x - x^2) - 2x^2)\,dx = \int_{0}^{5} (15x - 3x^2)\,dx = \left[\frac{15}{2}x^2 - x^3\right]_{0}^{5} = \frac{15(25)}{2} - 125 = \frac{375}{2} - \frac{250}{2} = \frac{125}{2}\text{ satuan luas}$.</sub>
- C. $\frac{275}{2}\text{ satuan luas}$  
  <sub>Salah: Salah mengurangkan kedua kurva, malah menjumlahkan kedua persamaan kurva di dalam integral.</sub>
- D. $125\text{ satuan luas}$  
  <sub>Salah: Lupa membagi dengan koefisien $2$ saat mengintegralkan suku derajat satu $15x$.</sub>

**Pembahasan:** Langkah 1: Menentukan batas integrasi melalui titik potong kedua kurva:
$2x^2 = 15x - x^2 \implies 3x^2 - 15x = 0 \implies 3x(x - 5) = 0$.
Diperoleh batas integrasi dari $x = 0$ hingga $x = 5$.
Langkah 2: Menentukan kurva atas dan kurva bawah pada $x \in [0, 5]$. Untuk $x = 1$, $y_1 = 2(1)^2 = 2$ dan $y_2 = 15(1) - 1^2 = 14$, sehingga $y_2 \ge y_1$.
Langkah 3: Menyusun integral luas daerah:
$L = \int_{0}^{5} ((15x - x^2) - 2x^2)\,dx = \int_{0}^{5} (15x - 3x^2)\,dx$.
Langkah 4: Menghitung nilai integral:
$L = \left[\frac{15}{2}x^2 - x^3\right]_{0}^{5} = \left(\frac{15}{2}(25) - 5^3\right) - 0 = \frac{375}{2} - 125 = \frac{125}{2}\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.228 Latihan Soal Penerapan Integral

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b03-c-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: luas daerah partisi ganda kurva kubik*

Luas total daerah tertutup yang dibatasi oleh kurva $y = x^3 - 6x$ dan garis $y = 3x$ adalah ....

- A. $81\text{ satuan luas}$  
  <sub>Salah: Kesalahan mengintegralkan suku derajat tiga tanpa pembagi $4$ dan suku derajat satu tanpa pembagi $2$.</sub>
- **B. $\frac{81}{2}\text{ satuan luas}$** ✅  
  <sub>Benar: Titik potong kurva dan garis dicari dari $x^3 - 6x = 3x \iff x^3 - 9x = 0 \iff x(x - 3)(x + 3) = 0$, yaitu $x = -3$, $x = 0$, dan $x = 3$. Daerah terbagi menjadi dua bagian: pada $[-3, 0]$, kurva berada di atas garis sehingga $L_1 = \int_{-3}^{0} (x^3 - 9x)\,dx = \left[\frac{1}{4}x^4 - \frac{9}{2}x^2\right]_{-3}^{0} = 0 - \left(\frac{81}{4} - \frac{81}{2}\right) = \frac{81}{4}$. Pada $[0, 3]$, garis berada di atas kurva sehingga $L_2 = \int_{0}^{3} (9x - x^3)\,dx = \left[\frac{9}{2}x^2 - \frac{1}{4}x^4\right]_{0}^{3} = \frac{81}{2} - \frac{81}{4} = \frac{81}{4}$. Luas total adalah $L_1 + L_2 = \frac{81}{4} + \frac{81}{4} = \frac{81}{2}\text{ satuan luas}$.</sub>
- C. $0\text{ satuan luas}$  
  <sub>Salah: Langsung mengintegralkan selisih fungsi dari $-3$ ke $3$ tanpa memecah interval sehingga kedua bagian bernilai saling meniadakan.</sub>
- D. $\frac{81}{4}\text{ satuan luas}$  
  <sub>Salah: Hanya menghitung luas daerah pada salah satu interval saja dan lupa menjumlahkannya.</sub>

**Pembahasan:** Langkah 1: Menentukan titik-titik potong antara kurva dan garis:
$x^3 - 6x = 3x \implies x^3 - 9x = 0 \implies x(x + 3)(x - 3) = 0$.
Titik potong berada pada $x = -3$, $x = 0$, dan $x = 3$.
Langkah 2: Menganalisis kedudukan kurva pada masing-masing subinterval:
- Pada interval $[-3, 0]$, uji $x = -1$: $y_{\text{kurva}} = (-1)^3 - 6(-1) = 5$ dan $y_{\text{garis}} = 3(-1) = -3$. Kurva kubik berada di atas garis.
- Pada interval $[0, 3]$, uji $x = 1$: $y_{\text{kurva}} = 1 - 6 = -5$ dan $y_{\text{garis}} = 3$. Garis berada di atas kurva kubik.
Langkah 3: Menghitung luas bagian pertama ($L_1$):
$L_1 = \int_{-3}^{0} ((x^3 - 6x) - 3x)\,dx = \int_{-3}^{0} (x^3 - 9x)\,dx = \left[\frac{1}{4}x^4 - \frac{9}{2}x^2\right]_{-3}^{0} = 0 - \left(\frac{81}{4} - \frac{81}{2}\right) = \frac{81}{4}$.
Langkah 4: Menghitung luas bagian kedua ($L_2$):
$L_2 = \int_{0}^{3} (3x - (x^3 - 6x))\,dx = \int_{0}^{3} (9x - x^3)\,dx = \left[\frac{9}{2}x^2 - \frac{1}{4}x^4\right]_{0}^{3} = \frac{81}{2} - \frac{81}{4} = \frac{81}{4}$.
Langkah 5: Menjumlahkan kedua luas:
$L_{\text{total}} = L_1 + L_2 = \frac{81}{4} + \frac{81}{4} = \frac{81}{2}\text{ satuan luas}$.
**Acuan:** siswa — siswa hal.222

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b03-c-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: kesetaraan usaha sistem pegas*

Dua buah pegas, yaitu pegas A dan pegas B, mula-mula berada pada panjang alaminya masing-masing. Sebuah gaya sebesar $60\text{ N}$ diperlukan untuk menahan pegas A tetap teregang sejauh $0,1\text{ m}$ dari panjang alaminya. Pegas B kemudian diregangkan sejauh $0,4\text{ m}$ dari panjang alaminya dan menghasilkan usaha yang sama besar dengan usaha untuk meregangkan pegas A sejauh $0,2\text{ m}$ dari panjang alaminya. Nilai konstanta dari pegas B adalah ....

- A. $300\text{ N/m}$  
  <sub>Salah: Menggunakan hubungan linier $W = kx$ tanpa mengintegralkan fungsi gaya terhadap perpindahan.</sub>
- **B. $150\text{ N/m}$** ✅  
  <sub>Benar: Menurut Hukum Hooke, konstanta pegas A adalah $k_A = \frac{F}{x} = \frac{60}{0,1} = 600\text{ N/m}$. Usaha untuk meregangkan pegas A sejauh $0,2\text{ m}$ adalah $W_A = \int_{0}^{0,2} 600x\,dx = \left[300x^2\right]_{0}^{0,2} = 300(0,04) = 12\text{ Joule}$. Usaha meregangkan pegas B sejauh $0,4\text{ m}$ adalah $W_B = \int_{0}^{0,4} k_B x\,dx = \frac{1}{2}k_B (0,4)^2 = 0,08k_B$. Karena $W_B = W_A$, maka $0,08k_B = 12 \iff k_B = \frac{12}{0,08} = 150\text{ N/m}$.</sub>
- C. $75\text{ N/m}$  
  <sub>Salah: Lupa mengalikan faktor $\frac{1}{2}$ pada integral pegas B sehingga persamaan menjadi $0,16k_B = 12$.</sub>
- D. $600\text{ N/m}$  
  <sub>Salah: Menganggap konstanta pegas B sama persis dengan konstanta pegas A.</sub>

**Pembahasan:** Langkah 1: Menentukan konstanta pegas A ($k_A$) menggunakan Hukum Hooke $F(x) = k_A x$:
$60 = k_A (0,1) \implies k_A = 600\text{ N/m}$.
Langkah 2: Menghitung usaha peregangan pegas A dari $0$ hingga $0,2\text{ m}$:
$W_A = \int_{0}^{0,2} 600x\,dx = \left[300x^2\right]_{0}^{0,2} = 300(0,2)^2 = 300(0,04) = 12\text{ Joule}$.
Langkah 3: Merumuskan usaha peregangan pegas B dari $0$ hingga $0,4\text{ m}$:
$W_B = \int_{0}^{0,4} k_B x\,dx = \left[\frac{1}{2}k_B x^2\right]_{0}^{0,4} = \frac{1}{2}k_B (0,4)^2 = 0,08 k_B$.
Langkah 4: Menyamakan usaha kedua pegas ($W_B = W_A$):
$0,08 k_B = 12 \implies k_B = \frac{12}{0,08} = 150\text{ N/m}$.
**Acuan:** siswa — siswa hal.226

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b03-c-hard-bt01-013
*variasi (konteks) | C5 | 4 langkah | jenis: usaha pengangkatan tambang dan beban*

Sebuah tambang baja penarik beban seberat $120\text{ kg}$ memiliki panjang $60\text{ meter}$ tergantung vertikal dari tepi atas tebing yang tinggi. Pada ujung bawah tambang tersebut terikat sebuah kotak sampel geologi seberat $40\text{ kg}$. Jika percepatan gravitasi bumi $g = 10\text{ m/s}^2$, besar usaha yang diperlukan untuk menarik seluruh tambang beserta kotak tersebut sampai ke puncak tebing adalah ....

- A. $36.000\text{ Joule}$  
  <sub>Salah: Hanya menghitung usaha pengangkatan tambang baja dan melupakan usaha pengangkatan kotak beban.</sub>
- B. $96.000\text{ Joule}$  
  <sub>Salah: Menganggap seluruh massa tambang diangkat sejauh 60 meter penuh tanpa integrasi terhadap titik berat tambang.</sub>
- **C. $60.000\text{ Joule}$** ✅  
  <sub>Benar: Rapat massa tambang adalah $\lambda = \frac{120\text{ kg}}{60\text{ m}} = 2\text{ kg/m}$. Usaha untuk menarik elemen tambang sepanjang $dx$ pada kedalaman $x$ meter ke puncak tebing adalah $dW_1 = (\lambda dx) g x = 20x\,dx$. Usaha total menarik tambang adalah $W_1 = \int_{0}^{60} 20x\,dx = [10x^2]_{0}^{60} = 10(3.600) = 36.000\text{ Joule}$. Kotak bermassa $40\text{ kg}$ ditarik setinggi $60\text{ m}$ secara penuh, sehingga usaha untuk mengangkat kotak adalah $W_2 = m g h = 40 \times 10 \times 60 = 24.000\text{ Joule}$. Jadi, usaha totalnya adalah $W = W_1 + W_2 = 36.000 + 24.000 = 60.000\text{ Joule}$.</sub>
- D. $48.000\text{ Joule}$  
  <sub>Salah: Membagi dua seluruh beban termasuk kotak sampel seolah-olah titik tangkap beban berada di tengah panjang tambang.</sub>

**Pembahasan:** Usaha total terdiri atas dua bagian:
1. Usaha pengangkatan tambang:
$$\lambda = \frac{120}{60} = 2\text{ kg/m}$$
$$W_{\text{tambang}} = \int_{0}^{60} \lambda g x\,dx = \int_{0}^{60} 20x\,dx = [10x^2]_{0}^{60} = 36.000\text{ Joule}$$
2. Usaha pengangkatan kotak sampel:
$$W_{\text{kotak}} = m_{\text{kotak}} g h = 40 \times 10 \times 60 = 24.000\text{ Joule}$$
Usaha total:
$$W = W_{\text{tambang}} + W_{\text{kotak}} = 36.000 + 24.000 = 60.000\text{ Joule}$$
**Acuan:** siswa — siswa hal.228 Latihan Soal Penerapan Integral

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b03-c-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: pembagian luas kurva simetris horizontal*

Daerah tertutup $R$ terletak di atas sumbu-$x$ dan dibatasi oleh kurva parabola $y = 9 - x^2$ serta sumbu-$x$. Sebuah garis horizontal $y = k$ (dengan $0 < k < 9$) membagi luas daerah $R$ menjadi dua bagian yang sama besar. Nilai dari $(9 - k)^3$ adalah ....

- A. $729$  
  <sub>Salah: Lupa membagi dua luas total, sehingga menyamakan luas bagian atas dengan 36.</sub>
- B. $\frac{243}{2}$  
  <sub>Salah: Melakukan kesalahan perhitungan aljabar saat menguadratkan bentuk pecahan 27/2.</sub>
- **C. $\frac{729}{4}$** ✅  
  <sub>Benar: Luas total daerah $R$ adalah $L = \int_{-3}^{3} (9 - x^2)\,dx = 2 \left[9x - \frac{1}{3}x^3\right]_{0}^{3} = 2(27 - 9) = 36\text{ satuan luas}$. Garis $y = k$ memotong parabola di $x = \pm\sqrt{9 - k}$. Luas daerah di atas garis $y = k$ adalah $L_{\text{atas}} = \int_{-\sqrt{9-k}}^{\sqrt{9-k}} ((9 - x^2) - k)\,dx = 2 \int_{0}^{\sqrt{9-k}} ((9 - k) - x^2)\,dx = 2 \left[(9 - k)x - \frac{1}{3}x^3\right]_{0}^{\sqrt{9-k}} = \frac{4}{3}(9 - k)^{3/2}$. Karena membagi dua sama besar, maka $L_{\text{atas}} = \frac{1}{2} L = 18$. Didapat $\frac{4}{3}(9 - k)^{3/2} = 18 \iff (9 - k)^{3/2} = \frac{27}{2}$. Menguadratkan kedua sisi menghasilkan $(9 - k)^3 = \left(\frac{27}{2}\right)^2 = \frac{729}{4}$.</sub>
- D. $576$  
  <sub>Salah: Terbalik mengalikan faktor pecahan 4/3 menjadi 18 kali 4/3 sama dengan 24 lalu dikuadratkan.</sub>

**Pembahasan:** 1. Luas daerah total $R$:
$$L = 2\int_{0}^{3} (9 - x^2)\,dx = 2\left[9x - \frac{x^3}{3}\right]_{0}^{3} = 36$$
2. Misalkan $u = \sqrt{9 - k}$, maka kurva dan garis berpotongan di $x = \pm u$. Luas bagian atas:
$$L_{\text{atas}} = 2\int_{0}^{u} (u^2 - x^2)\,dx = 2\left[u^2 x - \frac{x^3}{3}\right]_{0}^{u} = \frac{4}{3}u^3 = \frac{4}{3}(9 - k)^{3/2}$$
3. Syarat pembagian sama luas:
$$\frac{4}{3}(9 - k)^{3/2} = \frac{36}{2} = 18 \implies (9 - k)^{3/2} = \frac{27}{2}$$
4. Menguadratkan kedua sisi:
$$(9 - k)^3 = \left(\frac{27}{2}\right)^2 = \frac{729}{4}$$
**Acuan:** siswa — siswa hal.228

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b03-c-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: usaha pemompaan fluida tangki kerucut*

Sebuah tangki penampung air berbentuk kerucut dengan posisi ujung runcing di bawah memiliki tinggi $6\text{ meter}$ dan jari-jari lingkaran penampang atas $3\text{ meter}$. Tangki tersebut mula-mula terisi penuh cairan dengan massa jenis $\rho = 1.000\text{ kg/m}^3$. Cairan dipompa keluar melalui bibir atas tangki hingga kedalaman cairan di dalam tangki berkurang dan hanya tersisa setinggi $3\text{ meter}$ dari ujung bawah. Jika percepatan gravitasi bumi $g = 10\text{ m/s}^2$, besar usaha yang telah dilakukan untuk memompa cairan tersebut adalah ....

- A. $270.000\pi\text{ Joule}$  
  <sub>Salah: Menghitung usaha untuk memompa seluruh isi tangki hingga kosong total dari batas 0 hingga 6.</sub>
- B. $84.375\pi\text{ Joule}$  
  <sub>Salah: Mengintegrasikan dari batas 0 hingga 3, yakni menghitung usaha untuk memompa setengah volume kerucut bagian bawah.</sub>
- C. $759.375\pi\text{ Joule}$  
  <sub>Salah: Salah menentukan jarak angkat fluida, mengalikan dengan kedalaman y bukan (6 - y).</sub>
- **D. $185.625\pi\text{ Joule}$** ✅  
  <sub>Benar: Misalkan sumbu-$y$ vertikal dengan $y = 0$ di ujung runcing kerucut dan bibir tangki di $y = 6$. Jari-jari penampang horizontal pada ketinggian $y$ adalah $r(y) = \frac{3}{6}y = \frac{1}{2}y$. Luas penampang horizontal adalah $A(y) = \pi (r(y))^2 = \frac{\pi}{4}y^2$. Elemen volume $dV = \frac{\pi}{4}y^2\,dy$. Tiap lapisan air pada ketinggian $y$ harus diangkat sejauh $(6 - y)$ meter ke puncak tangki. Karena air dipompa dari penuh ($y = 6$) hingga tersisa setinggi $3\text{ m}$, batas integrasi lapisan air yang dipompa adalah dari $y = 3$ hingga $y = 6$. Usaha total adalah $W = \int_{3}^{6} \rho g (6 - y) A(y)\,dy = 10.000 \int_{3}^{6} (6 - y) \left(\frac{\pi}{4}y^2\right)\,dy = 2.500\pi \int_{3}^{6} (6y^2 - y^3)\,dy$. Hasil integrasi: $[2y^3 - \frac{1}{4}y^4]_{3}^{6} = \left(2(216) - \frac{1.296}{4}\right) - \left(2(27) - \frac{81}{4}\right) = (432 - 324) - (54 - 20,25) = 108 - 33,75 = 74,25$. Maka $W = 2.500\pi \times 74,25 = 185.625\pi\text{ Joule}$.</sub>

**Pembahasan:** 1. Jari-jari penampang pada ketinggian $y$:
$$r(y) = \frac{3}{6}y = \frac{y}{2}$$
2. Elemen gaya berat pada irisan setebal $dy$:
$$dF = \rho g dV = 1.000 \times 10 \times \pi \left(\frac{y}{2}\right)^2 dy = 2.500\pi y^2 dy$$
3. Jarak angkat ke tepi tangki adalah $(6 - y)$. Cairan yang dipindahkan berada pada interval $3 \le y \le 6$:
$$W = \int_{3}^{6} 2.500\pi y^2 (6 - y)\,dy = 2.500\pi \left[2y^3 - \frac{y^4}{4}\right]_{3}^{6}$$
4. Evaluasi nilai integral:
$$\left[2(6)^3 - \frac{6^4}{4}\right] - \left[2(3)^3 - \frac{3^4}{4}\right] = 108 - 33,75 = 74,25$$
$$W = 2.500\pi \times 74,25 = 185.625\pi\text{ Joule}$$
**Acuan:** siswa — siswa hal.232

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b03-c-hard-bt01-016
*orisinal | C5 | 5 langkah | jenis: estimasi luas luka laju nol*

Laju perubahan luas permukaan suatu luka pada pasien berkurang secara bertahap dan dimodelkan oleh persamaan laju $\frac{dA}{dt} = -k(6 - t)\text{ cm}^2/\text{hari}$ untuk rentang waktu $0 \le t \le 6$, dengan $t$ menyatakan waktu dalam hari sejak perawatan intensif dimulai dan $k$ adalah konstanta positif. Diketahui luas luka pada saat awal perawatan ($t = 0$) adalah $26\text{ cm}^2$, dan setelah $2\text{ hari}$ perlakuan luas luka berkurang menjadi $16\text{ cm}^2$. Luas luka yang tersisa pada saat laju penyembuhan mencapai nol adalah ....

- **A. $8\text{ cm}^2$** ✅  
  <sub>Benar: Fungsi luas luka diperoleh dari integral laju perubahan: $A(t) = \int -k(6 - t)\,dt = k\left(\frac{1}{2}t^2 - 6t\right) + C$. Pada saat $t = 0$, $A(0) = C = 26$. Pada saat $t = 2$, $A(2) = k\left(\frac{1}{2}(4) - 6(2)\right) + 26 = -10k + 26$. Diketahui $A(2) = 16$, sehingga $-10k + 26 = 16 \implies 10k = 10 \implies k = 1$. Laju penyembuhan mencapai nol ketika $\frac{dA}{dt} = 0 \iff -1(6 - t) = 0 \iff t = 6$. Luas luka yang tersisa pada $t = 6$ adalah $A(6) = 1\left(\frac{1}{2}(36) - 6(6)\right) + 26 = 18 - 36 + 26 = 8\text{ cm}^2$.</sub>
- B. $0\text{ cm}^2$  
  <sub>Salah: Mengira luka sudah sembuh total tanpa sisa karena nilai laju penyembuhannya telah mencapai nol.</sub>
- C. $18\text{ cm}^2$  
  <sub>Salah: Menghitung besarnya total pengurangan luas luka selama 6 hari bukan sisa luas luka yang tertinggal.</sub>
- D. $10\text{ cm}^2$  
  <sub>Salah: Melakukan substitusi pada t = 4 alih-alih pada t = 6 saat laju penyembuhan nol.</sub>

**Pembahasan:** 1. Bentuk fungsi antiturunan luas luka:
$$A(t) = \int -k(6 - t)\,dt = k\left(\frac{t^2}{2} - 6t\right) + C$$
2. Substitusi nilai awal $t = 0$:
$$A(0) = C = 26$$
3. Menentukan konstanta $k$ menggunakan data $t = 2$:
$$A(2) = k(2 - 12) + 26 = 16 \implies -10k = -10 \implies k = 1$$
Fungsi luas luka menjadi $A(t) = \frac{t^2}{2} - 6t + 26$.
4. Kondisi laju nol:
$$\frac{dA}{dt} = 0 \iff -(6 - t) = 0 \iff t = 6$$
5. Luas luka pada $t = 6$:
$$A(6) = \frac{6^2}{2} - 6(6) + 26 = 18 - 36 + 26 = 8\text{ cm}^2$$
**Acuan:** siswa — siswa hal.227

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b03-c-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: optimasi keuntungan akumulatif marjinal*

Sebuah unit mesin industri menghasilkan laju pendapatan operasional sebesar $R'(t) = 18 - 2t$ (dalam puluhan juta rupiah per tahun) dan membutuhkan laju biaya perawatan sebesar $C'(t) = 2t + 2$ (dalam puluhan juta rupiah per tahun), dengan $t$ menyatakan lama mesin beroperasi dalam tahun ($t \ge 0$). Perusahaan memutuskan untuk menghentikan pengoperasian mesin tepat saat pengoperasiannya tidak lagi memberikan tambahan laba bersih (laju pendapatan sama dengan laju biaya perawatan). Total laba bersih akumulatif maksimum yang diperoleh selama masa pengoperasian mesin tersebut adalah ....

- A. $\text{Rp}480.000.000,00$  
  <sub>Salah: Siswa keliru mengintegralkan suku $-4t$ menjadi $-t^2$ (lupa membagi koefisien dengan 2), sehingga menghasilkan $16(4) - 4^2 = 48$ puluhan juta rupiah.</sub>
- B. $\text{Rp}560.000.000,00$  
  <sub>Salah: Siswa hanya mengintegralkan laju pendapatan $\int_{0}^{4} (18 - 2t)\,dt = 56$ puluhan juta rupiah tanpa mengurangkan laju biaya perawatannya.</sub>
- C. $\text{Rp}240.000.000,00$  
  <sub>Salah: Siswa salah menentukan waktu efisiensi operasional menjadi $t = 2$ tahun akibat kekeliruan membagi saat menyelesaikan $4t = 8$, menghasilkan $\left[ 16t - 2t^2 \right]_0^2 = 24$ puluhan juta rupiah.</sub>
- **D. $\text{Rp}320.000.000,00$** ✅  
  <sub>Benar: Waktu penghentian optimal terjadi saat $R'(t) = C'(t) \iff 18 - 2t = 2t + 2 \iff 4t = 16 \iff t = 4$ tahun. Total laba bersih akumulatif maksimum diperoleh dari $P = \int_{0}^{4} [R'(t) - C'(t)]\,dt = \int_{0}^{4} (16 - 4t)\,dt = \left[ 16t - 2t^2 \right]_0^4 = 16(4) - 2(4)^2 = 64 - 32 = 32$ puluhan juta rupiah, setara dengan $\text{Rp}320.000.000,00$.</sub>

**Pembahasan:** Laba bersih operasional bertambah selama laju pendapatan marjinal lebih besar daripada laju biaya perawatan, dan mencapai nilai maksimum ketika $R'(t) = C'(t)$:
$$18 - 2t = 2t + 2$$
$$4t = 16 \implies t = 4\text{ tahun}$$

Total laba bersih akumulatif maksimum diperoleh dari integral selisih kedua laju tersebut pada interval $[0, 4]$:
$$\begin{aligned}
P &= \int_{0}^{4} [R'(t) - C'(t)]\,dt \\
&= \int_{0}^{4} [(18 - 2t) - (2t + 2)]\,dt \\
&= \int_{0}^{4} (16 - 4t)\,dt \\
&= \left[ 16t - 2t^2 \right]_{0}^{4} \\
&= \left(16(4) - 2(4)^2\right) - 0 \\
&= 64 - 32 = 32\text{ (dalam puluhan juta rupiah)}
\end{aligned}$$

Nilai dalam rupiah:
$$32 \times \text{Rp}10.000.000,00 = \text{Rp}320.000.000,00$$
**Acuan:** siswa — siswa hal.224

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
