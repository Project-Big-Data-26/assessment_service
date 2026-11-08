# Lembar koreksi — kelas12_tl SMA12L-B3 subbab B: Integral Tentu

59 soal | easy 20, medium 19, hard 20 | variasi 27, orisinal 32
> **Kapasitas kurang (medium): 19 dari kuota 20** — 4 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b03-b-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: sifat integral tentu*

Misalkan $\int_1^5 f(x)\,dx = 8$ dan $\int_1^5 g(x)\,dx = 5$. Nilai dari $\int_1^5 [4f(x) - 2g(x)]\,dx$ adalah ....

- A. $42$  
  <sub>Salah: Salah menjumlahkan bukan mengurangkan: $32 + 10 = 42$.</sub>
- B. $6$  
  <sub>Salah: Lupa mengalikan koefisien pengali: $(8 - 5) \times 2 = 6$.</sub>
- **C. $22$** ✅  
  <sub>Benar: Berdasarkan sifat kelinearan integral, $\int_1^5 [4f(x) - 2g(x)]\,dx = 4\int_1^5 f(x)\,dx - 2\int_1^5 g(x)\,dx = 4(8) - 2(5) = 32 - 10 = 22$.</sub>
- D. $26$  
  <sub>Salah: Hanya mengalikan fungsi pertama: $4(8) - 5 = 27$ atau salah hitung koefisien $4(8) - 6 = 26$.</sub>

**Pembahasan:** Menggunakan sifat kelinearan integral tentu:
$$\int_1^5 [4f(x) - 2g(x)]\,dx = 4\int_1^5 f(x)\,dx - 2\int_1^5 g(x)\,dx$$
Substitusikan nilai yang diketahui:
$$4(8) - 2(5) = 32 - 10 = 22$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b03-b-easy-bt01-002
*orisinal | C1 | 1 langkah | jenis: teorema dasar kalkulus*

Jika fungsi $F(x) = \int_1^x (t^3 + 5t)\,dt$, maka turunan pertama $F'(x)$ adalah ....

- **A. $x^3 + 5x$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, jika $F(x) = \int_a^x f(t)\,dt$, maka $F'(x) = f(x)$. Mengganti $t$ dengan $x$ menghasilkan $x^3 + 5x$.</sub>
- B. $3x^2 + 5$  
  <sub>Salah: Mendiferensialkan kembali fungsi di dalam integral alih-alih mengambil fungsi aslinya.</sub>
- C. $\frac{1}{4}x^4 + \frac{5}{2}x^2$  
  <sub>Salah: Mengintegralkan fungsi integran alih-alih mengambil fungsi itu sendiri sebagai turunan dari $F(x)$.</sub>
- D. $x^3 + 5x - 6$  
  <sub>Salah: Mengintegralkan dan menyubstitusikan batas bawah secara parsial lalu menurunkan.</sub>

**Pembahasan:** Menurut Teorema Dasar Kalkulus I:
$$\frac{d}{dx}\left[\int_a^x f(t)\,dt\right] = f(x)$$
Dengan $f(t) = t^3 + 5t$, maka:
$$F'(x) = x^3 + 5x$$
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b03-b-easy-bt01-003
*orisinal | C1 | 1 langkah | jenis: konsep luas daerah*

Bentuk integral tentu yang menyatakan luas daerah bidang datar yang dibatasi oleh kurva $y = x^2 + 2$, sumbu-$x$, garis $x = 1$, dan garis $x = 3$ adalah ....

- A. $\int_3^1 (x^2 + 2)\,dx$  
  <sub>Salah: Batas integrasi terbalik antara batas bawah dan batas atas.</sub>
- B. $\int_1^3 (2x)\,dx$  
  <sub>Salah: Menurunkan fungsi integran sebelum menuliskannya ke dalam rumus luas.</sub>
- **C. $\int_1^3 (x^2 + 2)\,dx$** ✅  
  <sub>Benar: Karena $f(x) = x^2 + 2 > 0$ pada $[1, 3]$, luas daerah di atas sumbu-$x$ dinyatakan dengan $L = \int_a^b f(x)\,dx = \int_1^3 (x^2 + 2)\,dx$.</sub>
- D. $-\int_1^3 (x^2 + 2)\,dx$  
  <sub>Salah: Keliru menggunakan rumus untuk daerah di bawah sumbu-x.</sub>

**Pembahasan:** Untuk fungsi kontinu $f(x) \ge 0$ pada selang tertutup $[a, b]$, luas daerah yang dibatasi oleh $y = f(x)$, sumbu-$x$, serta garis $x = a$ dan $x = b$ dirumuskan sebagai:
$$L = \int_a^b f(x)\,dx$$
Dengan $f(x) = x^2 + 2$, $a = 1$, dan $b = 3$, bentuk integralnya adalah $\int_1^3 (x^2 + 2)\,dx$.
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b03-b-easy-bt01-004
*variasi (angka) | C2 | 2 langkah | jenis: sifat linearitas integral tentu*

Misalkan $\int_4^8 f(x)\,dx = 15$ dan $\int_4^8 g(x)\,dx = 6$. Nilai dari $\int_4^8 [5f(x) - 7g(x)]\,dx$ adalah ....

- A. $9$  
  <sub>Salah: Siswa hanya mengurangkan nilai integral tanpa mengalikannya dengan skalar masing-masing ($15 - 6$).</sub>
- **B. $33$** ✅  
  <sub>Benar: Menggunakan sifat kelinearan: $5\int_4^8 f(x)\,dx - 7\int_4^8 g(x)\,dx = 5(15) - 7(6) = 75 - 42 = 33$.</sub>
- C. $75$  
  <sub>Salah: Siswa menukar koefisien pengali skalar fungsi ($7 \times 15 - 5 \times 6$).</sub>
- D. $117$  
  <sub>Salah: Siswa salah menjumlahkan kedua suku alih-alih mengurangkannya ($75 + 42$).</sub>

**Pembahasan:** Berdasarkan sifat kelinieran integral tentu:
$$\int_4^8 [5f(x) - 7g(x)]\,dx = 5\int_4^8 f(x)\,dx - 7\int_4^8 g(x)\,dx$$
Substitusikan nilai integral yang diketahui:
$$= 5(15) - 7(6) = 75 - 42 = 33$$
Jadi, nilai integral tersebut adalah $33$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b03-b-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu fungsi kuadrat*

Diketahui fungsi $f(x) = 3x^2$ pada interval $[0, 2]$. Nilai dari $\int_0^2 3x^2\,dx$ adalah ....

- A. $24$  
  <sub>Salah: Siswa lupa membagi koefisien dengan pangkat baru saat mengintegralkan sehingga memperoleh $3x^3$.</sub>
- **B. $8$** ✅  
  <sub>Benar: Antiturunan dari $3x^2$ adalah $x^3$, sehingga $\left[x^3\right]_0^2 = 2^3 - 0^3 = 8$.</sub>
- C. $6$  
  <sub>Salah: Siswa mengalikan koefisien dengan batas atas tanpa mengintegralkan fungsi ($3 \times 2$).</sub>
- D. $12$  
  <sub>Salah: Siswa keliru menerapkan turunan alih-alih integral ($6x$ dievaluasi dari 0 sampai 2).</sub>

**Pembahasan:** Tentukan antiturunan dari $3x^2$:
$$\int 3x^2\,dx = x^3$$
Evaluasi batas dari $0$ sampai $2$:
$$\int_0^2 3x^2\,dx = \left[x^3\right]_0^2 = 2^3 - 0^3 = 8$$
Jadi, nilai dari $\int_0^2 3x^2\,dx$ adalah $8$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b03-b-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu fungsi linear*

Misalkan terdapat fungsi $f(x) = 4x$. Nilai integral tentu dari fungsi tersebut pada interval $[0, 3]$ atau $\int_0^3 4x\,dx$ adalah ....

- A. $4$  
  <sub>Salah: Siswa menurunkan fungsi menjadi konstanta 4 alih-alih mengintegralkan.</sub>
- B. $36$  
  <sub>Salah: Siswa lupa membagi pangkat baru sehingga menggunakan antiturunan $4x^2$.</sub>
- C. $12$  
  <sub>Salah: Siswa hanya menyubstitusikan batas atas ke dalam fungsi $f(x) = 4(3)$ tanpa mengintegralkan.</sub>
- **D. $18$** ✅  
  <sub>Benar: Antiturunan dari $4x$ adalah $2x^2$, dievaluasi pada batas $[0, 3]$ menghasilkan $2(3^2) - 2(0^2) = 18$.</sub>

**Pembahasan:** Antiturunan dari $f(x) = 4x$ adalah:
$$F(x) = \frac{4}{2}x^2 = 2x^2$$
Evaluasi dari batas bawah $0$ ke batas atas $3$:
$$\int_0^3 4x\,dx = \left[2x^2\right]_0^3 = 2(3)^2 - 2(0)^2 = 18 - 0 = 18$$
Jadi, nilai integral tentu tersebut adalah $18$.
**Acuan:** siswa — siswa hal.200 Contoh Soal 3.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b03-b-easy-bt01-007
*orisinal | C1 | 1 langkah | jenis: teorema dasar kalkulus I*

Berdasarkan Teorema Dasar Kalkulus I, jika suatu fungsi didefinisikan oleh $F(x) = \int_2^x (5t^4 - 2t)\,dt$, maka turunan pertama $F'(x)$ adalah ....

- A. $x^5 - x^2$  
  <sub>Salah: Siswa mencari antiturunan dari fungsi yang ada di dalam integral.</sub>
- B. $20x^3 - 2$  
  <sub>Salah: Siswa menurunkan kembali fungsi $f(x)$ alih-alih cukup mengganti variabelnya.</sub>
- C. $5x^4 - 2$  
  <sub>Salah: Siswa salah saat mengganti variabel $t$ pada suku kedua.</sub>
- **D. $5x^4 - 2x$** ✅  
  <sub>Benar: Menurut Teorema Dasar Kalkulus I, jika $F(x) = \int_a^x f(t)\,dt$, maka $F'(x) = f(x)$.</sub>

**Pembahasan:** Teorema Dasar Kalkulus I menyatakan bahwa jika $F(x) = \int_a^x f(t)\,dt$, maka:
$$F'(x) = f(x)$$
Dengan $f(t) = 5t^4 - 2t$, diperoleh:
$$F'(x) = 5x^4 - 2x$$
Jadi, turunan pertama dari $F(x)$ adalah $5x^4 - 2x$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b03-b-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: sifat integral tentu batas sama*

Nilai dari $\int_5^5 (9x^4 - 3x^2 + 7)\,dx$ adalah ....

- A. $5.557$  
  <sub>Salah: Siswa menghitung nilai fungsi pada $x = 5$ alih-alih mengevaluasi integral.</sub>
- B. $7$  
  <sub>Salah: Siswa hanya mengambil konstanta dari fungsi integran.</sub>
- C. $1$  
  <sub>Salah: Siswa keliru menganggap pembagian batas atas dengan batas bawah ($5/5 = 1$).</sub>
- **D. $0$** ✅  
  <sub>Benar: Jika batas atas dan batas bawah suatu integral tentu bernilai sama, maka nilainya selalu nol karena $F(a) - F(a) = 0$.</sub>

**Pembahasan:** Berdasarkan Teorema Dasar Kalkulus II, untuk sebarang fungsi terintegralkan dengan batas atas sama dengan batas bawah ($a = b$):
$$\int_a^a f(x)\,dx = F(a) - F(a) = 0$$
Karena batas integrasi pada soal adalah dari $5$ ke $5$, maka nilainya adalah $0$.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b03-b-easy-bt01-009
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu fungsi kuadrat*

Diketahui fungsi $f(x) = 3x^2 - 2x + 5$ pada interval $[0, 2]$. Nilai integral tentu dari fungsi tersebut pada interval $[0, 2]$ atau $\int_0^2 (3x^2 - 2x + 5)\,dx$ adalah ....

- **A. $14$** ✅  
  <sub>Benar: Antiturunan dari $3x^2 - 2x + 5$ adalah $x^3 - x^2 + 5x$. Evaluasi pada batas $[0, 2]$ menghasilkan $(2^3 - 2^2 + 5(2)) - 0 = 8 - 4 + 10 = 14$.</sub>
- B. $22$  
  <sub>Salah: Siswa salah tanda operasi suku kedua menjadi positif sehingga menghitung $8 + 4 + 10 = 22$.</sub>
- C. $13$  
  <sub>Salah: Siswa hanya mengevaluasi nilai fungsi asli pada batas atas $f(2) = 3(4) - 2(2) + 5 = 13$ tanpa melakukan integrasi.</sub>
- D. $26$  
  <sub>Salah: Siswa lupa membagi koefisien dengan pangkat baru sehingga antiturunan menjadi $3x^3 - 2x^2 + 5x$ yang bernilai $24 - 8 + 10 = 26$.</sub>

**Pembahasan:** Langkah 1: Tentukan antiturunan fungsi.
$$\int (3x^2 - 2x + 5)\,dx = x^3 - x^2 + 5x$$

Langkah 2: Substitusikan batas atas dan batas bawah.
$$\left[x^3 - x^2 + 5x\right]_0^2 = (2^3 - 2^2 + 5(2)) - (0^3 - 0^2 + 5(0)) = (8 - 4 + 10) - 0 = 14$$

Jadi, nilai integral tentu tersebut adalah $14$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b03-b-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu fungsi linear*

Nilai dari $\int_2^6 (4x - 3)\,dx$ adalah ....

- A. $116$  
  <sub>Salah: Siswa lupa membagi koefisien dengan pangkat saat mengintegralkan suku $4x$ sehingga menjadi $4x^2 - 3x$.</sub>
- **B. $52$** ✅  
  <sub>Benar: Antiturunan dari $4x - 3$ adalah $2x^2 - 3x$. Evaluasi batas: $(2(6)^2 - 3(6)) - (2(2)^2 - 3(2)) = (72 - 18) - (8 - 6) = 54 - 2 = 52$.</sub>
- C. $54$  
  <sub>Salah: Siswa hanya menghitung nilai antiturunan pada batas atas dan mengabaikan batas bawah.</sub>
- D. $56$  
  <sub>Salah: Siswa menjumlahkan hasil evaluasi kedua batas alih-alih mengurangkannya ($54 + 2 = 56$).</sub>

**Pembahasan:** Langkah 1: Tentukan antiturunan dari $4x - 3$.
$$\int (4x - 3)\,dx = 2x^2 - 3x$$

Langkah 2: Evaluasi pada batas $x = 2$ sampai $x = 6$.
$$\left[2x^2 - 3x\right]_2^6 = (2(6)^2 - 3(6)) - (2(2)^2 - 3(2)) = (72 - 18) - (8 - 6) = 54 - 2 = 52$$

Jadi, nilai integral tersebut adalah $52$.
**Acuan:** siswa — siswa hal.210 Contoh Soal 3.10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b03-b-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu polinomial linear*

Diketahui fungsi $f(x) = 5 + 2x$ pada interval $[0, 3]$. Nilai integral tentu dari $f(x)$ pada interval $[0, 3]$ atau $\int_0^3 (5 + 2x)\,dx$ adalah ....

- A. $11$  
  <sub>Salah: Siswa hanya menghitung nilai fungsi pada batas atas $f(3) = 5 + 2(3) = 11$.</sub>
- B. $33$  
  <sub>Salah: Siswa tidak membagi pangkat sehingga suku $2x$ diintegralkan menjadi $2x^2$, menghasilkan $15 + 18 = 33$.</sub>
- C. $14$  
  <sub>Salah: Siswa lupa mengalikan konstanta $5$ dengan variabel $x$ pada antiturunan sehingga menghitung $5 + 3^2 = 14$.</sub>
- **D. $24$** ✅  
  <sub>Benar: Antiturunan dari $5 + 2x$ adalah $5x + x^2$. Evaluasi batas: $(5(3) + 3^2) - 0 = 15 + 9 = 24$.</sub>

**Pembahasan:** Langkah 1: Menentukan antiturunan fungsi.
$$\int (5 + 2x)\,dx = 5x + x^2$$

Langkah 2: Evaluasi batas interval $[0, 3]$.
$$\left[5x + x^2\right]_0^3 = (5(3) + 3^2) - (5(0) + 0^2) = (15 + 9) - 0 = 24$$

Jadi, nilai integral tentu dari $f(x)$ pada interval $[0, 3]$ adalah $24$.
**Acuan:** siswa — siswa hal.219 Latihan Soal Integral Tentu

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b03-b-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: teorema dasar kalkulus II*

Misalkan $f$ kontinu pada interval tertutup $[1, 4]$ dan $F$ adalah antiturunan dari $f$ sedemikian sehingga $F'(x) = f(x)$. Jika $F(4) = 19$ dan $F(1) = 7$, maka nilai dari $\int_1^4 f(t)\,dt$ adalah ....

- **A. $12$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus II, $\int_1^4 f(t)\,dt = F(4) - F(1) = 19 - 7 = 12$.</sub>
- B. $-12$  
  <sub>Salah: Siswa terbalik mengurangkan batas bawah dengan batas atas ($F(1) - F(4) = 7 - 19 = -12$).</sub>
- C. $26$  
  <sub>Salah: Siswa menjumlahkan kedua nilai fungsi antiturunan alih-alih mengurangkannya ($19 + 7 = 26$).</sub>
- D. $36$  
  <sub>Salah: Siswa mengalikan selisih antiturunan dengan panjang interval ($3 \times 12 = 36$).</sub>

**Pembahasan:** Berdasarkan Teorema Dasar Kalkulus II:
$$\int_a^b f(t)\,dt = F(b) - F(a)$$

Dengan $a = 1$ dan $b = 4$:
$$\int_1^4 f(t)\,dt = F(4) - F(1) = 19 - 7 = 12$$

Jadi, nilai $\int_1^4 f(t)\,dt$ adalah $12$.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b03-b-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: hubungan luas daerah dan integral tentu*

Suatu fungsi $f(x)$ bernilai kontinu dan positif pada interval $[2, 6]$. Jika luas daerah bidang datar yang dibatasi oleh kurva $y = f(x)$, sumbu-$x$, garis $x = 2$, dan garis $x = 6$ adalah $15$ satuan luas, maka nilai dari $\int_2^6 f(x)\,dx$ adalah ....

- **A. $15$** ✅  
  <sub>Benar: Untuk kurva di atas sumbu-$x$ ($f(x) \ge 0$), nilai luas daerah sama persis dengan nilai integral tentunya yaitu $15$.</sub>
- B. $0$  
  <sub>Salah: Siswa salah menduga bahwa luas di atas sumbu-$x$ saling meniadakan menjadi $0$.</sub>
- C. $60$  
  <sub>Salah: Siswa mengalikan luas dengan panjang interval ($15 \times (6 - 2) = 60$).</sub>
- D. $-15$  
  <sub>Salah: Siswa keliru menganggap daerah tersebut berada di bawah sumbu-$x$ sehingga bertanda negatif.</sub>

**Pembahasan:** Berdasarkan konsep luas daerah di atas sumbu-$x$:
Jika $f(x) \ge 0$ pada interval $[a, b]$, maka luas daerahnya dirumuskan dengan:
$$L = \int_a^b f(x)\,dx$$

Diketahui luas $L = 15$ dengan selang $[2, 6]$, maka:
$$\int_2^6 f(x)\,dx = L = 15$$

Jadi, nilai integral tentu tersebut adalah $15$.
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b03-b-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu polinomial kuadrat*

Diketahui fungsi $f(x) = 3x^2 + 6x + 2$ pada interval $[0, 3]$. Nilai dari $\int_0^3 (3x^2 + 6x + 2)\,dx$ adalah ....

- A. $33$  
  <sub>Salah: Hanya memasukkan nilai batas atas ke fungsi mula-mula tanpa diintegralkan lebih dahulu.</sub>
- B. $114$  
  <sub>Salah: Salah membagi koefisien saat integrasi sehingga antiturunannya menjadi $3x^3 + 6x^2 + 2x$.</sub>
- **C. $60$** ✅  
  <sub>Benar: Antiturunan dari $3x^2 + 6x + 2$ adalah $F(x) = x^3 + 3x^2 + 2x$. Evaluasi batas: $F(3) - F(0) = (27 + 27 + 6) - 0 = 60$.</sub>
- D. $54$  
  <sub>Salah: Lupa mengintegralkan suku konstanta 2 sehingga $2x$ tidak dihitung.</sub>

**Pembahasan:** Integralkan fungsi terhadap $x$:
$$\int_0^3 (3x^2 + 6x + 2)\,dx = \left[ x^3 + 3x^2 + 2x \right]_0^3$$
Substitusikan batas atas dan batas bawah:
$$= (3^3 + 3(3^2) + 2(3)) - (0^3 + 3(0^2) + 2(0))$$
$$= (27 + 27 + 6) - 0 = 60$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b03-b-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi integral tentu dasar*

Diketahui fungsi $f(x) = 6x^2 - 2x$ pada interval $[0, 2]$. Nilai dari $\int_0^2 (6x^2 - 2x)\,dx$ adalah ....

- A. $16$  
  <sub>Salah: Hanya menghitung suku pertama antiturunan $2x^3$ dan mengabaikan suku $-x^2$.</sub>
- B. $8$  
  <sub>Salah: Substitusi batas ke dalam fungsi mula-mula: $6(2)^2 - 2(2) = 20$, lalu dikurangi operasi lain secara keliru.</sub>
- **C. $12$** ✅  
  <sub>Benar: Antiturunan dari $6x^2 - 2x$ adalah $2x^3 - x^2$. Evaluasi batas: $(2(8) - 4) - 0 = 12$.</sub>
- D. $20$  
  <sub>Salah: Salah tanda saat integrasi sehingga menjumlahkan kedua suku: $16 + 4 = 20$.</sub>

**Pembahasan:** Hitung integral tentu fungsi:
$$\int_0^2 (6x^2 - 2x)\,dx = \left[ 2x^3 - x^2 \right]_0^2$$
$$= (2(2^3) - 2^2) - 0 = (2(8) - 4) = 16 - 4 = 12$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b03-b-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: definisi integral tentu luas daerah*

Jika fungsi $f$ kontinu dan positif pada interval $a \le x \le b$, maka luas daerah $L$ yang dibatasi oleh kurva $y = f(x)$, sumbu-$x$, garis $x = a$, dan garis $x = b$ dirumuskan dengan ....

- A. $L = -\int_a^b f(x)\,dx$  
  <sub>Salah: Tertukar dengan rumus luas daerah yang berada di bawah sumbu-$x$.</sub>
- B. $L = \int_a^b [f'(x)]\,dx$  
  <sub>Salah: Tertukar antara fungsi kontinu $f(x)$ dengan turunannya $f'(x)$.</sub>
- **C. $L = \int_a^b f(x)\,dx$** ✅  
  <sub>Benar: Berdasarkan definisi pada buku teks hal 213, luas bidang datar di atas sumbu-$x$ pada interval $[a, b]$ adalah $\int_a^b f(x)\,dx$.</sub>
- D. $L = f(b) - f(a)$  
  <sub>Salah: Hanya menghitung selisih nilai fungsi di batas-batasnya tanpa notasi integral.</sub>

**Pembahasan:** Berdasarkan konsep luas daerah di atas sumbu-$x$, jika $f(x) \ge 0$ dan kontinu pada selang $[a, b]$, maka luas daerahnya dinyatakan oleh integral tentu:
$$L = \int_a^b f(x)\,dx$$
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b03-b-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: perhitungan integral polinomial*

Diketahui fungsi $f(x) = 3x^2 - 2x + 7$ pada interval $[1, 5]$. Nilai integral tentu dari $f(x)$ pada interval $[1, 5]$ atau $\int_1^5 (3x^2 - 2x + 7)\,dx$ adalah ....

- A. $114$  
  <sub>Salah: Salah mengintegralkan suku linear, menggunakan koefisien $2x^2$ bukan $x^2$.</sub>
- B. $142$  
  <sub>Salah: Melakukan penjumlahan batas bukan pengurangan, yaitu $F(5) + F(1) = 135 + 7 = 142$.</sub>
- C. $135$  
  <sub>Salah: Hanya menghitung nilai batas atas $F(5)$ tanpa mengurangkan dengan $F(1)$.</sub>
- **D. $128$** ✅  
  <sub>Benar: Antiturunan dari $3x^2 - 2x + 7$ adalah $F(x) = x^3 - x^2 + 7x$. Menghitung $F(5) - F(1) = (5^3 - 5^2 + 7(5)) - (1^3 - 1^2 + 7(1)) = (125 - 25 + 35) - (1 - 1 + 7) = 135 - 7 = 128$.</sub>

**Pembahasan:** Berdasarkan Teorema Dasar Kalkulus II:
$$\int_1^5 (3x^2 - 2x + 7)\,dx = \left[ x^3 - x^2 + 7x \right]_1^5$$
Substitusikan batas atas dan batas bawah:
$$= (5^3 - 5^2 + 7(5)) - (1^3 - 1^2 + 7(1))$$
$$= (125 - 25 + 35) - (1 - 1 + 7)$$
$$= 135 - 7 = 128$$
Jadi, nilai integral tentu tersebut adalah $128$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b03-b-easy-bt01-018
*variasi (angka) | C2 | 2 langkah | jenis: integral tentu fungsi aljabar linear*

Diketahui fungsi $f(x) = 6 + 5x$ pada interval $[0, 4]$. Nilai integral tentu dari $f(x)$ pada interval $[0, 4]$ atau $\int_0^4 (6 + 5x)\,dx$ adalah ....

- A. $104$  
  <sub>Salah: Lupa membagi 2 saat mengintegralkan suku aljabar linear, yaitu $5x^2$ bukan $\frac{5}{2}x^2$ sehingga $24 + 80 = 104$.</sub>
- **B. $64$** ✅  
  <sub>Benar: Antiturunan dari $6 + 5x$ adalah $6x + \frac{5}{2}x^2$. Nilai pada batas $[0, 4]$ adalah $(6(4) + \frac{5}{2}(4)^2) - 0 = 24 + 40 = 64$.</sub>
- C. $44$  
  <sub>Salah: Lupa membagi dengan pangkat baru pada suku $x$, mengintegralkan $5x$ menjadi $5x$ atau $5x^2$ dibagi 4.</sub>
- D. $26$  
  <sub>Salah: Hanya menyubstitusikan $x = 4$ ke dalam fungsi awal $f(x) = 6 + 5(4) = 26$ tanpa mengintegralkan.</sub>

**Pembahasan:** Tentukan antiturunan fungsi $f(x) = 6 + 5x$:
$$F(x) = 6x + \frac{5}{2}x^2$$
Evaluasi batas dari $0$ hingga $4$:
$$\int_0^4 (6 + 5x)\,dx = \left[ 6x + \frac{5}{2}x^2 \right]_0^4$$
$$= \left( 6(4) + \frac{5}{2}(4^2) \right) - \left( 6(0) + \frac{5}{2}(0^2) \right)$$
$$= (24 + 40) - 0 = 64$$
Jadi, nilai integral tentu fungsi tersebut adalah $64$.
**Acuan:** siswa — siswa hal.219 Latihan Soal Integral Tentu

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b03-b-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi integral tentu tiga suku*

Diketahui fungsi $f(x) = 6x^2 + 8x + 9$ pada interval $[0, 3]$. Nilai dari $\int_0^3 (6x^2 + 8x + 9)\,dx$ adalah ....

- **A. $117$** ✅  
  <sub>Benar: Antiturunan $F(x) = 2x^3 + 4x^2 + 9x$. Menghitung $F(3) - F(0) = (2(27) + 4(9) + 9(3)) - 0 = 54 + 36 + 27 = 117$.</sub>
- B. $90$  
  <sub>Salah: Lupa mengintegralkan konstanta $9$, sehingga mengabaikan suku $9x$.</sub>
- C. $207$  
  <sub>Salah: Lupa membagi koefisien dengan pangkat baru sehingga mengintegralkan menjadi $6x^3 + 8x^2 + 9x$.</sub>
- D. $87$  
  <sub>Salah: Salah menentukan koefisien antiturunan $6x^2$ menjadi $x^3$ sehingga nilainya $27 + 36 + 27 = 90$, atau keliru saat menjumlahkan.</sub>

**Pembahasan:** Tentukan antiturunan fungsi aljabar:
$$\int (6x^2 + 8x + 9)\,dx = 2x^3 + 4x^2 + 9x$$
Hitung nilai integral tentu dari $0$ sampai $3$:
$$\left[ 2x^3 + 4x^2 + 9x \right]_0^3 = (2(3)^3 + 4(3)^2 + 9(3)) - 0$$
$$= 2(27) + 4(9) + 27$$
$$= 54 + 36 + 27 = 117$$
Jadi, nilai integral tentu fungsi tersebut adalah $117$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b03-b-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: turunan fungsi integral akumulasi*

Berdasarkan Teorema Dasar Kalkulus I, jika suatu fungsi didefinisikan oleh $F(x) = \int_3^x (7t^2 - 4t + 5)\,dt$, maka turunan pertama $F'(x)$ adalah ....

- A. $7x^2 - 4x$  
  <sub>Salah: Menganggap turunan dari konstanta $5$ adalah nol saat mengganti variabel.</sub>
- **B. $7x^2 - 4x + 5$** ✅  
  <sub>Benar: Teorema Dasar Kalkulus I menyatakan jika $F(x) = \int_a^x f(t)\,dt$, maka $F'(x) = f(x)$. Mengganti peubah integrasi $t$ dengan $x$ menghasilkan $7x^2 - 4x + 5$.</sub>
- C. $14x - 4$  
  <sub>Salah: Menurunkan fungsi di dalam integral terhadap $x$ alih-alih mengambil fungsi aslinya.</sub>
- D. $\frac{7}{3}x^3 - 2x^2 + 5x$  
  <sub>Salah: Mengintegralkan fungsi di dalam integral terhadap $x$ tanpa menerapkan konsep turunan dari $F(x)$.</sub>

**Pembahasan:** Teorema Dasar Kalkulus I menyatakan bahwa jika fungsi $f$ kontinu pada selang tertutup $[a, b]$ dan $F(x) = \int_a^x f(t)\,dt$, maka:
$$F'(x) = f(x)$$
Pada soal, $f(t) = 7t^2 - 4t + 5$ dan batas bawahnya $a = 3$. Oleh karena itu:
$$F'(x) = 7x^2 - 4x + 5$$
Jadi, turunan pertama fungsi tersebut adalah $7x^2 - 4x + 5$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b03-b-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: Sifat linear integral tentu*

Misalkan $\int_2^7 f(x)\,dx = 11$ dan $\int_2^7 g(x)\,dx = 4$. Nilai dari $\int_2^7 [6f(x) - 5g(x)]\,dx$ adalah ....

- A. $86$  
  <sub>Salah: Salah menggunakan operasi penjumlahan pada pengurang: $66 + 20 = 86$.</sub>
- **B. $46$** ✅  
  <sub>Benar: Berdasarkan sifat linear integral tentu, $\int_2^7 [6f(x) - 5g(x)]\,dx = 6\int_2^7 f(x)\,dx - 5\int_2^7 g(x)\,dx = 6(11) - 5(4) = 66 - 20 = 46$.</sub>
- C. $7$  
  <sub>Salah: Hanya mengurangkan nilai integral tanpa mengalikan dengan koefisien skalar: $11 - 4 = 7$.</sub>
- D. $35$  
  <sub>Salah: Tertukar koefisien pengali fungsi: $5(11) - 6(4) = 55 - 24 = 31$ lalu salah hitung, atau $(11 - 4) \times (6 - 5) \times 5$.</sub>

**Pembahasan:** Gunakan sifat linear integral tentu:
$$\int_a^b [k_1 f(x) + k_2 g(x)]\,dx = k_1 \int_a^b f(x)\,dx + k_2 \int_a^b g(x)\,dx$$

Substitusikan nilai yang diketahui:
$$\int_2^7 [6f(x) - 5g(x)]\,dx = 6\int_2^7 f(x)\,dx - 5\int_2^7 g(x)\,dx$$
$$= 6(11) - 5(4) = 66 - 20 = 46$$

Jadi, nilai integral tersebut adalah $46$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b03-b-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: Jumlahan Riemann*

Diketahui fungsi $f(x) = 2x + 1$ pada interval $[1, 5]$. Jika interval tersebut dipartisi menjadi $4$ subinterval sama panjang dan titik wakil yang digunakan adalah titik ujung kanan dari tiap subinterval, nilai Jumlahan Riemann tersebut adalah ....

- A. $28$  
  <sub>Salah: Keliru menggunakan titik tengah subinterval ($x = 1,5; 2,5; 3,5; 4,5$): $(4 + 6 + 8 + 10) \times 1 = 28$.</sub>
- B. $30$  
  <sub>Salah: Salah menghitung nilai fungsi atau salah menjumlahkan suku-suku deret.</sub>
- **C. $32$** ✅  
  <sub>Benar: Lebar subinterval $\Delta x = \frac{5 - 1}{4} = 1$. Titik ujung kanan: $x_1 = 2, x_2 = 3, x_3 = 4, x_4 = 5$. Nilai fungsi: $f(2)=5, f(3)=7, f(4)=9, f(5)=11$. Jumlahan Riemann $= (5 + 7 + 9 + 11) \times 1 = 32$.</sub>
- D. $24$  
  <sub>Salah: Keliru menggunakan titik ujung kiri ($x = 1, 2, 3, 4$): $(3 + 5 + 7 + 9) \times 1 = 24$.</sub>

**Pembahasan:** Langkah 1: Tentukan lebar tiap subinterval $(\Delta x)$:
$$\Delta x = \frac{b - a}{n} = \frac{5 - 1}{4} = 1$$

Langkah 2: Tentukan subinterval dan titik wakil ujung kanannya:
- Subinterval 1: $[1, 2] \rightarrow x_1 = 2$
- Subinterval 2: $[2, 3] \rightarrow x_2 = 3$
- Subinterval 3: $[3, 4] \rightarrow x_3 = 4$
- Subinterval 4: $[4, 5] \rightarrow x_4 = 5$

Langkah 3: Hitung nilai fungsi pada titik wakil:
$$f(2) = 2(2) + 1 = 5$$
$$f(3) = 2(3) + 1 = 7$$
$$f(4) = 2(4) + 1 = 9$$
$$f(5) = 2(5) + 1 = 11$$

Langkah 4: Hitung Jumlahan Riemann:
$$R_4 = \sum_{i=1}^4 f(x_i)\,\Delta x = (5 + 7 + 9 + 11) \times 1 = 32$$

Jadi, nilai Jumlahan Riemann tersebut adalah $32$.
**Acuan:** siswa — siswa hal.196

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b03-b-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: Integral substitusi tentu*

Nilai dari $\int_0^1 6x(x^2 + 1)^2\,dx$ adalah ....

- **A. $7$** ✅  
  <sub>Benar: Misal $u = x^2 + 1$, maka $du = 2x\,dx$ sehingga $6x\,dx = 3\,du$. Batas integrasi berubah: saat $x=0 \Rightarrow u=1$, saat $x=1 \Rightarrow u=2$. Maka $\int_1^2 3u^2\,du = [u^3]_1^2 = 2^3 - 1^3 = 8 - 1 = 7$.</sub>
- B. $21$  
  <sub>Salah: Lupa mengalikan faktor penyesuaian $\frac{1}{2}$ pada turunan $du$, sehingga mengintegralkan sebagai $6u^2$ menjadi $[2u^3]_1^2 = 16 - 2 = 14$ atau salah hitung substitusi.</sub>
- C. $8$  
  <sub>Salah: Hanya mengevaluasi batas atas $u = 2$ yaitu $2^3 = 8$ tanpa mengurangkan batas bawah.</sub>
- D. $\frac{7}{3}$  
  <sub>Salah: Lupa mengalikan koefisien 3 saat mengubah $6x\,dx$ menjadi $3\,du$, sehingga menghitung $[\frac{1}{3}u^3]_1^2 = \frac{7}{3}$.</sub>

**Pembahasan:** Gunakan metode substitusi:
Misalkan $u = x^2 + 1$, maka turunan diferensialnya adalah:
$$du = 2x\,dx \implies 3\,du = 6x\,dx$$

Ubah batas integral:
- Batas bawah: untuk $x = 0 \implies u = 0^2 + 1 = 1$
- Batas atas: untuk $x = 1 \implies u = 1^2 + 1 = 2$

Bentuk integral menjadi:
$$\int_0^1 6x(x^2 + 1)^2\,dx = \int_1^2 3u^2\,du$$
$$= [u^3]_1^2 = 2^3 - 1^3 = 8 - 1 = 7$$

Jadi, nilai integral tentu tersebut adalah $7$.
**Acuan:** siswa — siswa hal.212

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b03-b-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: Luas daerah bidang datar*

Luas bidang datar yang dibatasi oleh kurva $y = 6x - x^2$ dan sumbu-$x$ adalah .... satuan luas.

- A. $72$  
  <sub>Salah: Salah menentukan antiturunan dari $6x$ menjadi $6x^2$ alih-alih $3x^2$.</sub>
- B. $54$  
  <sub>Salah: Salah melakukan pengurangan pecahan atau keliru mengevaluasi batas atas.</sub>
- **C. $36$** ✅  
  <sub>Benar: Titik potong kurva dengan sumbu-$x$ adalah $6x - x^2 = 0 \Rightarrow x = 0$ dan $x = 6$. Karena kurva di atas sumbu-$x$ pada $[0, 6]$, maka $L = \int_0^6 (6x - x^2)\,dx = [3x^2 - \frac{1}{3}x^3]_0^6 = 3(36) - \frac{1}{3}(216) = 108 - 72 = 36$.</sub>
- D. $18$  
  <sub>Salah: Salah membagi pada langkah akhir atau salah menghitung $108 - 72 = 36$ dibagi $2$.</sub>

**Pembahasan:** Langkah 1: Tentukan batas integrasi dengan mencari perpotongan kurva terhadap sumbu-$x$ ($y = 0$):
$$6x - x^2 = 0$$
$$x(6 - x) = 0 \implies x = 0 \text{ atau } x = 6$$

Langkah 2: Untuk interval $0 \le x \le 6$, kurva $y = 6x - x^2 \ge 0$ (berada di atas sumbu-$x$). Maka luas daerahnya adalah:
$$L = \int_0^6 (6x - x^2)\,dx$$

Langkah 3: Hitung integral tentu menggunakan Teorema Dasar Kalkulus II:
$$L = \left[ 3x^2 - \frac{1}{3}x^3 \right]_0^6$$
$$L = \left( 3(6)^2 - \frac{1}{3}(6)^3 \right) - 0$$
$$L = (3 \times 36) - \left(\frac{1}{3} \times 216\right)$$
$$L = 108 - 72 = 36$$

Jadi, luas daerah bidang datar tersebut adalah $36$ satuan luas.
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b03-b-medium-bt01-005
*variasi (angka) | C3 | 3 langkah | jenis: Jumlahan Riemann ujung kiri*

Diketahui fungsi $f(x) = 3 + 2x$ pada interval $[1, 7]$. Jika interval tersebut dipartisi menjadi $3$ subinterval sama panjang dan titik wakilnya menggunakan titik ujung kiri tiap subinterval, nilai Jumlahan Riemann fungsi tersebut adalah ....

- **A. $54$** ✅  
  <sub>Benar: Lebar subinterval $\Delta x = \frac{7-1}{3} = 2$. Ujung kiri tiap subinterval adalah $x_1 = 1, x_2 = 3, x_3 = 5$. Nilai fungsi: $f(1)=5, f(3)=9, f(5)=13$. Jumlahan Riemann $= (5 + 9 + 13) \times 2 = 27 \times 2 = 54$.</sub>
- B. $27$  
  <sub>Salah: Siswa lupa mengalikan jumlahan nilai fungsi dengan lebar subinterval $\Delta x = 2$.</sub>
- C. $66$  
  <sub>Salah: Siswa keliru menggunakan titik tengah subinterval ($x = 2, 4, 6$) sehingga diperoleh $(7 + 11 + 15) \times 2 = 66$.</sub>
- D. $78$  
  <sub>Salah: Siswa keliru menggunakan titik ujung kanan ($x = 3, 5, 7$) sehingga diperoleh $(9 + 13 + 17) \times 2 = 78$.</sub>

**Pembahasan:** Langkah 1: Menentukan lebar tiap subinterval:
$$\Delta x = \frac{b - a}{n} = \frac{7 - 1}{3} = 2$$

Langkah 2: Menentukan titik ujung kiri dan nilai fungsinya pada setiap subinterval:
- Subinterval 1: $[1, 3] \implies x_1 = 1$, maka $f(1) = 3 + 2(1) = 5$
- Subinterval 2: $[3, 5] \implies x_2 = 3$, maka $f(3) = 3 + 2(3) = 9$
- Subinterval 3: $[5, 7] \implies x_3 = 5$, maka $f(5) = 3 + 2(5) = 13$

Langkah 3: Menghitung Jumlahan Riemann:
$$\sum_{i=1}^{3} f(x_i)\,\Delta x = (5 + 9 + 13) \times 2 = 27 \times 2 = 54$$

Jadi, nilai Jumlahan Riemann tersebut adalah $54$.
**Acuan:** siswa — siswa hal.218 Latihan Soal Integral Tentu

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b03-b-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: Jarak tempuh gerak partikel*

Sebuah partikel bergerak sepanjang garis lurus dengan kecepatan pada waktu $t$ ditentukan oleh $v(t) = 2t - 4$ (dalam meter per detik). Jarak yang ditempuh partikel tersebut selama periode waktu $0 \le t \le 3$ adalah ....

- A. $4\text{ meter}$  
  <sub>Salah: Siswa hanya menghitung jarak pada interval pertama saat partikel bergerak mundur ($0 \le t \le 2$).</sub>
- B. $7\text{ meter}$  
  <sub>Salah: Siswa salah saat mengevaluasi nilai integral pada interval kedua sehingga memperoleh $4 + 3 = 7$.</sub>
- C. $3\text{ meter}$  
  <sub>Salah: Siswa menghitung perpindahan net $\int_0^3 (2t - 4)\,dt = [t^2 - 4t]_0^3 = 9 - 12 = -3$ lalu memutlakkan menjadi $3$, bukan jarak tempuh total.</sub>
- **D. $5\text{ meter}$** ✅  
  <sub>Benar: Kecepatan nol pada $t = 2$. Pada interval $[0, 2]$, $v(t) \le 0$, jarak $= -\int_0^2 (2t - 4)\,dt = 4$. Pada $[2, 3]$, $v(t) \ge 0$, jarak $= \int_2^3 (2t - 4)\,dt = 1$. Total jarak $= 4 + 1 = 5\text{ meter}$.</sub>

**Pembahasan:** Langkah 1: Menentukan kapan partikel berbalik arah ($v(t) = 0$):
$$2t - 4 = 0 \iff t = 2$$
Pada $0 \le t \le 2$, $v(t) \le 0$.
Pada $2 \le t \le 3$, $v(t) \ge 0$.

Langkah 2: Menghitung jarak pada masing-masing selang waktu:
- Untuk $0 \le t \le 2$:
$$s_1 = \int_0^2 |2t - 4|\,dt = -\int_0^2 (2t - 4)\,dt = -[t^2 - 4t]_0^2 = -(4 - 8) = 4\text{ m}$$
- Untuk $2 \le t \le 3$:
$$s_2 = \int_2^3 (2t - 4)\,dt = [t^2 - 4t]_2^3 = (9 - 12) - (4 - 8) = -3 - (-4) = 1\text{ m}$$

Langkah 3: Menjumlahkan kedua jarak:
$$\text{Total jarak} = s_1 + s_2 = 4 + 1 = 5\text{ meter}$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-14b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b03-b-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: Aplikasi Teorema Dasar Kalkulus I*

Diketahui suatu fungsi didefinisikan oleh $F(x) = \int_2^x (3t^2 - 4t + 1)\,dt$. Nilai dari turunan kedua $F''(3)$ adalah ....

- A. $16$  
  <sub>Salah: Siswa mengevaluasi nilai turunan pertama $F'(3) = 3(3^2) - 4(3) + 1 = 27 - 12 + 1 = 16$, bukan turunan kedua.</sub>
- **B. $14$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, $F'(x) = 3x^2 - 4x + 1$. Maka $F''(x) = 6x - 4$. Untuk $x = 3$, $F''(3) = 6(3) - 4 = 14$.</sub>
- C. $22$  
  <sub>Salah: Siswa salah melakukan turunan kedua menjadi $F''(x) = 6x + 4$ sehingga diperoleh $6(3) + 4 = 22$.</sub>
- D. $6$  
  <sub>Salah: Siswa hanya mengambil koefisien $x$ dari turunan kedua tanpa mengevaluasi $6(3) - 4$.</sub>

**Pembahasan:** Langkah 1: Menerapkan Teorema Dasar Kalkulus I:
$$F'(x) = \frac{d}{dx}\left[ \int_2^x (3t^2 - 4t + 1)\,dt \right] = 3x^2 - 4x + 1$$

Langkah 2: Menentukan turunan kedua $F''(x)$:
$$F''(x) = \frac{d}{dx}(3x^2 - 4x + 1) = 6x - 4$$

Langkah 3: Menghitung nilai $F''(3)$:
$$F''(3) = 6(3) - 4 = 18 - 4 = 14$$
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b03-b-medium-bt01-008
*variasi (angka) | C3 | 3 langkah | jenis: Jumlahan Riemann ujung kiri*

Diketahui suatu fungsi $f(x) = x^2$ pada interval $[1, 5]$. Nilai Jumlahan Riemann dengan membuat partisi interval $[1, 5]$ menjadi $4$ subinterval sama panjang dan titik wakilnya menggunakan titik ujung kiri tiap subinterval adalah ....

- A. $42$  
  <sub>Salah: Menggunakan titik tengah subinterval ($1{,}5; 2{,}5; 3{,}5; 4{,}5$) menghasilkan $2{,}25 + 6{,}25 + 12{,}25 + 20{,}25 = 41$ lalu salah hitung menjadi $42$.</sub>
- B. $14$  
  <sub>Salah: Hanya menjumlahkan tiga subinterval pertama ($1 + 4 + 9 = 14$).</sub>
- C. $54$  
  <sub>Salah: Menggunakan titik ujung kanan subinterval ($x = 2, 3, 4, 5$) sehingga hasilnya $(4 + 9 + 16 + 25) \times 1 = 54$.</sub>
- **D. $30$** ✅  
  <sub>Benar: Lebar subinterval $\Delta x = \frac{5 - 1}{4} = 1$. Titik-titik ujung kiri subinterval adalah $x_0 = 1, x_1 = 2, x_2 = 3, x_3 = 4$. Nilai fungsi: $f(1) = 1$, $f(2) = 4$, $f(3) = 9$, $f(4) = 16$. Jumlahan Riemann $= (1 + 4 + 9 + 16) \times 1 = 30$.</sub>

**Pembahasan:** Langkah 1: Tentukan lebar tiap subinterval.
$$\Delta x = \frac{b - a}{n} = \frac{5 - 1}{4} = 1$$

Langkah 2: Tentukan titik wakil ujung kiri pada setiap subinterval $[x_{i-1}, x_i]$.
Subinterval: $[1, 2], [2, 3], [3, 4], [4, 5]$.
Titik wakil ujung kiri: $x_1^* = 1$, $x_2^* = 2$, $x_3^* = 3$, $x_4^* = 4$.

Langkah 3: Hitung Jumlahan Riemann.
$$R_4 = \sum_{i=1}^4 f(x_i^*) \Delta x = [f(1) + f(2) + f(3) + f(4)] \times 1$$
$$R_4 = (1^2 + 2^2 + 3^2 + 4^2) \times 1 = (1 + 4 + 9 + 16) \times 1 = 30$$
**Acuan:** siswa — siswa hal.197 Ayo Mencoba 3.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b03-b-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: Integral tentu polinomial*

Diketahui fungsi $f(x) = 6x - x^2$ pada interval $[0, 5]$. Nilai integral tentu dari $f(x)$ pada interval $[0, 5]$ atau $\int_0^5 (6x - x^2)\,dx$ adalah ....

- A. $\frac{200}{3}$  
  <sub>Salah: Salah mengintegralkan $6x$ menjadi $6x^2$ alih-alih $3x^2$ kemudian salah operasi aritmetika.</sub>
- **B. $\frac{100}{3}$** ✅  
  <sub>Benar: Antiturunan dari $6x - x^2$ adalah $3x^2 - \frac{1}{3}x^3$. Evaluasi pada batas $[0, 5]$ menghasilkan $[3(25) - \frac{125}{3}] - 0 = 75 - \frac{125}{3} = \frac{100}{3}$.</sub>
- C. $\frac{350}{3}$  
  <sub>Salah: Salah tanda operasi antiturunan menjadi $3x^2 + \frac{1}{3}x^3$ sehingga $75 + \frac{125}{3} = \frac{350}{3}$.</sub>
- D. $-50$  
  <sub>Salah: Lupa membagi koefisien derajat tiga dengan $3$, menghitung $3(25) - 125 = -50$.</sub>

**Pembahasan:** Langkah 1: Tentukan antiturunan dari fungsi yang diintegralkan.
$$\int (6x - x^2)\,dx = 3x^2 - \frac{1}{3}x^3 + C$$

Langkah 2: Terapkan Teorema Dasar Kalkulus II dengan batas $0$ sampai $5$.
$$\int_0^5 (6x - x^2)\,dx = \left[ 3x^2 - \frac{1}{3}x^3 \right]_0^5$$
$$= \left( 3(5)^2 - \frac{1}{3}(5)^3 \right) - \left( 3(0)^2 - \frac{1}{3}(0)^3 \right)$$
$$= \left( 75 - \frac{125}{3} \right) - 0 = \frac{225 - 125}{3} = \frac{100}{3}$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b03-b-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: Sifat kelinieran integral tentu*

Misalkan $\int_1^4 f(x)\,dx = 12$ dan $\int_1^4 g(x)\,dx = 7$. Nilai dari $\int_1^4 [3f(x) - 4g(x)]\,dx$ adalah ....

- A. $5$  
  <sub>Salah: Hanya mengurangkan nilai integral tanpa mengalikannya dengan koefisien skalar ($12 - 7 = 5$).</sub>
- **B. $8$** ✅  
  <sub>Benar: Berdasarkan sifat linear: $3\int_1^4 f(x)\,dx - 4\int_1^4 g(x)\,dx = 3(12) - 4(7) = 36 - 28 = 8$.</sub>
- C. $64$  
  <sub>Salah: Salah menggunakan tanda operasi, menjumlahkan suku-suku alih-alih mengurangkannya ($36 + 28 = 64$).</sub>
- D. $27$  
  <sub>Salah: Tertukar koefisien pengali fungsi $f(x)$ dan $g(x)$ sehingga menghitung $4(12) - 3(7) = 48 - 21 = 27$.</sub>

**Pembahasan:** Langkah 1: Gunakan sifat kelinieran integral tentu.
$$\int_1^4 [3f(x) - 4g(x)]\,dx = 3\int_1^4 f(x)\,dx - 4\int_1^4 g(x)\,dx$$

Langkah 2: Substitusikan nilai-nilai integral yang diketahui.
$$= 3(12) - 4(7) = 36 - 28 = 8$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-13

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b03-b-medium-bt01-011
*orisinal | C3 | 2 langkah | jenis: Gradien fungsi dari Teorema Dasar Kalkulus I*

Diketahui suatu fungsi didefinisikan oleh $F(x) = \int_1^x (4t^3 - 6t)\,dt$. Gradien garis singgung grafik fungsi $F(x)$ pada titik dengan absis $x = 2$ adalah ....

- A. $9$  
  <sub>Salah: Menghitung nilai fungsi $F(2)$ alih-alih turunan $F'(2)$: $[t^4 - 3t^2]_1^2 = (16 - 12) - (1 - 3) = 4 - (-2) = 6$ lalu salah substitusi batas.</sub>
- B. $8$  
  <sub>Salah: Salah menghitung pangkat pada $4(2)^3$ menjadi $4 \times 6 = 24$ sehingga $24 - 12 = 12$, atau keliru menghitung $4(2) - 6 = 2$ lalu dikali $4$.</sub>
- C. $36$  
  <sub>Salah: Turunan kedua yang dihitung alih-alih turunan pertama: $F''(x) = 12x^2 - 6 \implies F''(2) = 48 - 6 = 42$, atau salah tanda $32 + 12 = 44$ lalu salah hitung menjadi $36$.</sub>
- **D. $20$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, $F'(x) = 4x^3 - 6x$. Gradien garis singgung adalah $m = F'(2) = 4(2)^3 - 6(2) = 32 - 12 = 20$.</sub>

**Pembahasan:** Langkah 1: Tentukan turunan pertama $F'(x)$ menggunakan Teorema Dasar Kalkulus I.
Karena $F(x) = \int_1^x (4t^3 - 6t)\,dt$, maka:
$$F'(x) = 4x^3 - 6x$$

Langkah 2: Tentukan gradien garis singgung $m$ di absis $x = 2$.
$$m = F'(2) = 4(2)^3 - 6(2) = 4(8) - 12 = 32 - 12 = 20$$
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b03-b-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: Luas daerah di bawah sumbu-x*

Luas daerah bidang datar yang dibatasi oleh kurva $y = x^2 - 4x$, sumbu-$x$, garis $x = 1$, dan garis $x = 3$ adalah .... satuan luas.

- A. $\frac{16}{3}$  
  <sub>Salah: Mengintegralkan dengan batas yang salah dari $x = 0$ sampai $x = 2$ menghasilkan $\frac{16}{3}$.</sub>
- B. $\frac{32}{3}$  
  <sub>Salah: Salah tanda saat mengurangkan nilai batas bawah: $9 + \frac{5}{3} = \frac{32}{3}$.</sub>
- **C. $\frac{22}{3}$** ✅  
  <sub>Benar: Pada interval $[1, 3]$, kurva $y = x^2 - 4x \le 0$ (berada di bawah sumbu-$x$). Maka $L = -\int_1^3 (x^2 - 4x)\,dx = \int_1^3 (4x - x^2)\,dx = [2x^2 - \frac{1}{3}x^3]_1^3 = (18 - 9) - (2 - \frac{1}{3}) = 9 - \frac{5}{3} = \frac{22}{3}$.</sub>
- D. $7$  
  <sub>Salah: Lupa mengurangkan suku pecahan pada batas bawah, menghitung $9 - 2 = 7$.</sub>

**Pembahasan:** Langkah 1: Analisis kedudukan kurva terhadap sumbu-$x$.
Untuk fungsi $y = x(x - 4)$, kurva memotong sumbu-$x$ pada $x = 0$ dan $x = 4$. Pada interval $[1, 3]$, nilai $y < 0$ sehingga kurva berada di bawah sumbu-$x$.

Langkah 2: Susun integral untuk menghitung luas daerah.
$$L = -\int_1^3 (x^2 - 4x)\,dx = \int_1^3 (4x - x^2)\,dx$$

Langkah 3: Hitung nilai integral tentu.
$$L = \left[ 2x^2 - \frac{1}{3}x^3 \right]_1^3$$
$$L = \left( 2(3)^2 - \frac{1}{3}(3)^3 \right) - \left( 2(1)^2 - \frac{1}{3}(1)^3 \right)$$
$$L = (18 - 9) - \left( 2 - \frac{1}{3} \right) = 9 - \frac{5}{3} = \frac{27 - 5}{3} = \frac{22}{3}$$
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b03-b-medium-bt01-013
*variasi (angka) | C3 | 2 langkah | jenis: Aplikasi kecepatan gerak*

Tentukan panjang lintasan yang ditempuh oleh sebuah objek yang bergerak dengan kecepatan $v(t) = (9 - 3t)\text{ cm/detik}$ dari $t = 0\text{ detik}$ sampai $t = 3\text{ detik}$.

- A. $27\text{ cm}$  
  <sub>Salah: Hanya menghitung $[9t]_0^3$ dan mengabaikan suku kuadrat $-\frac{3}{2}t^2$.</sub>
- B. $18\text{ cm}$  
  <sub>Salah: Salah mengintegralkan $-3t$ menjadi $-t^2$ sehingga memperoleh $27 - 9 = 18$.</sub>
- C. $9\text{ cm}$  
  <sub>Salah: Hanya menghitung nilai kecepatan awal $v(0)$ dikurangi selisih waktu tanpa melakukan integrasi fungsi.</sub>
- **D. $13{,}5\text{ cm}$** ✅  
  <sub>Benar: $s = \int_0^3 (9 - 3t)\,dt = [9t - \frac{3}{2}t^2]_0^3 = (27 - 13{,}5) - 0 = 13{,}5\text{ cm}$.</sub>

**Pembahasan:** Panjang lintasan diperoleh dengan mengintegralkan fungsi kecepatan pada selang waktu yang diberikan:
$$
s = \int_0^3 v(t)\,dt = \int_0^3 (9 - 3t)\,dt
$$
Menentukan antiturunan:
$$
\int (9 - 3t)\,dt = 9t - \frac{3}{2}t^2
$$
Evaluasi batas dari $t = 0$ sampai $t = 3$:
$$
s = \left[9t - \frac{3}{2}t^2\right]_0^3 = \left(9(3) - \frac{3}{2}(3)^2\right) - 0 = 27 - \frac{27}{2} = 13{,}5\text{ cm}
$$
Jadi, panjang lintasan yang ditempuh adalah $13{,}5\text{ cm}$.
**Acuan:** siswa — siswa hal.210 Ayo Mencoba 3.8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b03-b-medium-bt01-014
*variasi (angka) | C3 | 2 langkah | jenis: Integral tentu fungsi kuadrat*

Diketahui fungsi $f(x) = 2x^2 - 5x + 3$ pada interval $[0, 3]$. Nilai integral tentu dari fungsi tersebut pada interval $[0, 3]$ atau $\int_0^3 (2x^2 - 5x + 3)\,dx$ adalah ....

- **A. $\frac{9}{2}$** ✅  
  <sub>Benar: Antiturunan adalah $\frac{2}{3}x^3 - \frac{5}{2}x^2 + 3x$. Substitusi batas menghasilkan $(18 - \frac{45}{2} + 9) - 0 = 27 - 22{,}5 = 4{,}5 = \frac{9}{2}$.</sub>
- B. $\frac{99}{2}$  
  <sub>Salah: Salah tanda pada suku kedua menjadi $+ \frac{5}{2}x^2$ sehingga diperoleh $18 + 22{,}5 + 9 = \frac{99}{2}$.</sub>
- C. $\frac{15}{2}$  
  <sub>Salah: Salah melakukan integrasi pada suku kuadrat menjadi $x^3$ sehingga menghasilkan $(27 - 22{,}5 + 3)$.</sub>
- D. $9$  
  <sub>Salah: Lupa membagi dengan koefisien pecahan saat evaluasi batas sehingga menghasilkan nilai bilangan bulat.</sub>

**Pembahasan:** Menghitung integral tentu:
$$
\int_0^3 (2x^2 - 5x + 3)\,dx = \left[ \frac{2}{3}x^3 - \frac{5}{2}x^2 + 3x \right]_0^3
$$
Substitusi batas atas $x = 3$ dan batas bawah $x = 0$:
$$
= \left( \frac{2}{3}(3)^3 - \frac{5}{2}(3)^2 + 3(3) \right) - 0
$$
$$
= \left( 18 - \frac{45}{2} + 9 \right) = 27 - \frac{45}{2} = \frac{54 - 45}{2} = \frac{9}{2}
$$
Jadi, nilai integral tentu tersebut adalah $\frac{9}{2}$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-9

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b03-b-medium-bt01-015
*orisinal | C3 | 3 langkah | jenis: Luas daerah antara dua kurva*

Luas daerah bidang datar yang dibatasi oleh kurva $y = 8 - x^2$ dan kurva $y = x^2$ adalah .... satuan luas.

- A. $16$  
  <sub>Salah: Hanya menghitung $[8x]_{-2}^2 = 32$ dan mengurangi nilai sembarang tanpa mengintegralkan suku $-2x^2$ dengan benar.</sub>
- B. $\frac{32}{3}$  
  <sub>Salah: Hanya menghitung separuh luas dari interval $[0, 2]$ tanpa mengalikan dua untuk interval $[-2, 2]$.</sub>
- **C. $\frac{64}{3}$** ✅  
  <sub>Benar: Titik potong kurva adalah $x = -2$ dan $x = 2$. Luas $L = \int_{-2}^2 (8 - 2x^2)\,dx = [8x - \frac{2}{3}x^3]_{-2}^2 = (16 - \frac{16}{3}) - (-16 + \frac{16}{3}) = \frac{64}{3}$.</sub>
- D. $\frac{128}{3}$  
  <sub>Salah: Salah menentukan batas integrasi menjadi $[-4, 4]$ akibat keliru menarik akar persamaan $2x^2 = 8$.</sub>

**Pembahasan:** Langkah 1: Menentukan batas integrasi dengan mencari absis titik potong kedua kurva:
$$
8 - x^2 = x^2 \implies 2x^2 = 8 \implies x^2 = 4 \implies x = -2 \text{ atau } x = 2
$$
Pada interval $[-2, 2]$, grafik $y = 8 - x^2$ berada di atas grafik $y = x^2$.

Langkah 2: Menyusun rumus luas daerah:
$$
L = \int_{-2}^2 ((8 - x^2) - x^2)\,dx = \int_{-2}^2 (8 - 2x^2)\,dx
$$

Langkah 3: Menghitung integral tentu:
$$
L = \left[ 8x - \frac{2}{3}x^3 \right]_{-2}^2
$$
$$
= \left( 8(2) - \frac{2}{3}(2)^3 \right) - \left( 8(-2) - \frac{2}{3}(-2)^3 \right)
$$
$$
= \left( 16 - \frac{16}{3} \right) - \left( -16 + \frac{16}{3} \right) = \frac{32}{3} - \left( -\frac{32}{3} \right) = \frac{64}{3}
$$
Jadi, luas daerah tersebut adalah $\frac{64}{3}$ satuan luas.
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b03-b-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: Integral substitusi tentu batas baru*

Nilai dari $\int_0^1 4x(2x^2 + 1)^3\,dx$ adalah ....

- **A. $20$** ✅  
  <sub>Benar: Substitusi $u = 2x^2 + 1 \implies du = 4x\,dx$. Batas: $x = 0 \to u = 1$ dan $x = 1 \to u = 3$. Hasil: $\int_1^3 u^3\,du = [\frac{u^4}{4}]_1^3 = \frac{81 - 1}{4} = 20$.</sub>
- B. $10$  
  <sub>Salah: Salah menurunkan diferensial dan membagi dua kembali hasil integrasi secara tidak perlu.</sub>
- C. $80$  
  <sub>Salah: Lupa membagi dengan pangkat integrasi baru 4 sehingga menghitung $[u^4]_1^3 = 81 - 1 = 80$.</sub>
- D. $\frac{81}{4}$  
  <sub>Salah: Hanya menghitung batas atas $\frac{3^4}{4}$ dan lupa mengurangkan evaluasi batas bawah $\frac{1^4}{4}$.</sub>

**Pembahasan:** Gunakan metode integrasi substitusi:
Misalkan $u = 2x^2 + 1$, maka $\frac{du}{dx} = 4x \implies du = 4x\,dx$.

Ubah batas integrasi:
- Untuk $x = 0$, maka $u = 2(0)^2 + 1 = 1$.
- Untuk $x = 1$, maka $u = 2(1)^2 + 1 = 3$.

Integral tentu menjadi:
$$
\int_0^1 4x(2x^2 + 1)^3\,dx = \int_1^3 u^3\,du
$$
Evaluasi hasil integral:
$$
= \left[ \frac{1}{4}u^4 \right]_1^3 = \frac{1}{4}(3^4) - \frac{1}{4}(1^4) = \frac{81}{4} - \frac{1}{4} = \frac{80}{4} = 20
$$
Jadi, nilai integral tersebut adalah $20$.
**Acuan:** siswa — siswa hal.212

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b03-b-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: Perhitungan integral tentu polinomial*

Diketahui fungsi $f(x) = 3x^2 - 6x + 7$ pada interval $[2, 6]$. Nilai integral tentu dari $f(x)$ pada interval $[2, 6]$ atau $\int_2^6 (3x^2 - 6x + 7)\,dx$ adalah ....

- A. $150$  
  <sub>Salah: Siswa hanya menghitung nilai antiturunan pada batas atas $F(6)$ dan lupa mengurangkan dengan nilai batas bawah $F(2)$.</sub>
- B. $119$  
  <sub>Salah: Siswa lupa mengalikan konstanta $7$ dengan variabel $x$ pada proses integrasi sehingga hanya menghitung $[x^3 - 3x^2]_2^6 + 7 = 112 + 7 = 119$.</sub>
- C. $332$  
  <sub>Salah: Siswa keliru menggunakan tanda tambah pada suku kedua saat integrasi ($x^3 + 3x^2 + 7x$), menghasilkan $366 - 34 = 332$.</sub>
- **D. $140$** ✅  
  <sub>Benar: Antiturunan dari $f(x)$ adalah $F(x) = x^3 - 3x^2 + 7x$. Evaluasi pada batas: $F(6) = 6^3 - 3(6)^2 + 7(6) = 216 - 108 + 42 = 150$, dan $F(2) = 2^3 - 3(2)^2 + 7(2) = 8 - 12 + 14 = 10$. Maka, $\int_2^6 (3x^2 - 6x + 7)\,dx = 150 - 10 = 140$.</sub>

**Pembahasan:** Gunakan Teorema Dasar Kalkulus II:
$$\int_2^6 (3x^2 - 6x + 7)\,dx = \left[ x^3 - 3x^2 + 7x \right]_2^6$$

Substitusikan batas atas ($x = 6$):
$$F(6) = 6^3 - 3(6^2) + 7(6) = 216 - 108 + 42 = 150$$

Substitusikan batas bawah ($x = 2$):
$$F(2) = 2^3 - 3(2^2) + 7(2) = 8 - 12 + 14 = 10$$

Kurangkan batas atas dengan batas bawah:
$$F(6) - F(2) = 150 - 10 = 140$$

Jadi, nilai integral tentu tersebut adalah $140$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-10

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b03-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: Penentuan batas atas integral tentu*

Diketahui $\int_0^k (3x^2 + 2x)\,dx = 12$ dengan nilai $k > 0$. Nilai $k$ yang memenuhi persamaan tersebut adalah ....

- A. $4$  
  <sub>Salah: Keliru mengintegralkan $3x^2$ menjadi $x^2$ sehingga menyelesaikan persamaan kuadrat $x^2 + x^2 = 12$ yang mendekati nilai 4.</sub>
- **B. $2$** ✅  
  <sub>Benar: Antiturunan dari $3x^2 + 2x$ adalah $x^3 + x^2$. Menghitung batas: $[x^3 + x^2]_0^k = k^3 + k^2 - 0 = k^3 + k^2$. Diperoleh persamaan $k^3 + k^2 - 12 = 0$. Dengan menguji nilai real positif, $(k - 2)(k^2 + 3k + 6) = 0$. Karena $k^2 + 3k + 6 = 0$ tidak memiliki akar real, nilai real positif yang memenuhi adalah $k = 2$.</sub>
- C. $1$  
  <sub>Salah: Hanya menghitung nilai fungsi antiturunan pada saat $x = 1$, yaitu $1^3 + 1^2 = 2$, bukan mencocokkan dengan hasil integral 12.</sub>
- D. $3$  
  <sub>Salah: Kesalahan dalam penyelesaian persamaan, menduga $k$ adalah pembagi dari 12 tanpa menyubstitusikan ke bentuk kubik.</sub>

**Pembahasan:** Langkah 1: Menentukan antiturunan fungsi integran.
$$\int (3x^2 + 2x)\,dx = x^3 + x^2$$

Langkah 2: Menghitung integral tentu dengan batas $0$ sampai $k$.
$$\int_0^k (3x^2 + 2x)\,dx = \left[ x^3 + x^2 \right]_0^k = (k^3 + k^2) - (0^3 + 0^2) = k^3 + k^2$$

Langkah 3: Menyelesaikan persamaan aljabar untuk $k > 0$.
$$k^3 + k^2 = 12$$
$$k^3 + k^2 - 12 = 0$$
$$(k - 2)(k^2 + 3k + 6) = 0$$
Untuk faktor kuadrat $k^2 + 3k + 6$, diskriminannya adalah $D = 3^2 - 4(1)(6) = -15 < 0$, sehingga tidak ada penyelesaian real lainnya.
Jadi, nilai $k$ yang memenuhi adalah $k = 2$.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b03-b-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: Sifat adisi dan kelinieran integral tentu*

Diketahui suatu fungsi $f$ kontinu pada interval $[1, 7]$ dengan $\int_1^7 f(x)\,dx = 13$ dan $\int_4^7 f(x)\,dx = 5$. Nilai dari $\int_1^4 [2f(x) + 3]\,dx$ adalah ....

- A. 19  
  <sub>Salah: Siswa lupa mengintegralkan suku konstanta terhadap selang interval dan hanya menambahkan konstanta 3 secara langsung: $2(8) + 3 = 19$.</sub>
- B. 28  
  <sub>Salah: Siswa mengalikan suku konstanta dengan batas atas saja tanpa mengurangkan batas bawah: $2(8) + 3(4) = 16 + 12 = 28$.</sub>
- **C. 25** ✅  
  <sub>Benar: Berdasarkan sifat pemecahan interval, $\int_1^4 f(x)\,dx = \int_1^7 f(x)\,dx - \int_4^7 f(x)\,dx = 13 - 5 = 8$. Selanjutnya, $\int_1^4 [2f(x) + 3]\,dx = 2\int_1^4 f(x)\,dx + \int_1^4 3\,dx = 2(8) + [3x]_1^4 = 16 + 3(4 - 1) = 16 + 9 = 25$.</sub>
- D. 45  
  <sub>Salah: Siswa keliru menjumlahkan nilai integral kedua selang alih-alih mengurangkannya sehingga $\int_1^4 f(x)\,dx = 13 + 5 = 18$, menghasilkan $2(18) + 9 = 45$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $\int_1^4 f(x)\,dx$ menggunakan sifat penjumlahan interval:
$$\int_1^7 f(x)\,dx = \int_1^4 f(x)\,dx + \int_4^7 f(x)\,dx$$
$$13 = \int_1^4 f(x)\,dx + 5 \implies \int_1^4 f(x)\,dx = 13 - 5 = 8$$

Langkah 2: Menerapkan sifat kelinieran integral tentu:
$$\int_1^4 [2f(x) + 3]\,dx = 2\int_1^4 f(x)\,dx + \int_1^4 3\,dx$$

Langkah 3: Menghitung nilai integral:
$$2(8) + [3x]_1^4 = 16 + (3(4) - 3(1)) = 16 + (12 - 3) = 16 + 9 = 25$$

Jadi, nilai dari $\int_1^4 [2f(x) + 3]\,dx$ adalah $25$.
**Acuan:** siswa — siswa hal.204

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [hard] kelas12_tl-b03-b-hard-bt01-001
*variasi (angka) | C5 | 5 langkah | jenis: penerapan fisika integral tentu*

Sebuah partikel bergerak sepanjang garis lurus sehingga kecepatannya pada waktu $t$ ditentukan oleh $v(t) = 3t^2 - 12t + 9$ (dalam meter per detik). Jarak yang ditempuh partikel tersebut selama periode waktu $0 \le t \le 4$ adalah ....

- A. $16\text{ meter}$  
  <sub>Salah: Siswa keliru menjumlahkan batas atas nilai kuadrat tanpa mengintegralkan suku konstan secara tepat.</sub>
- B. $8\text{ meter}$  
  <sub>Salah: Siswa hanya memecah pada titik stasioner pertama $t = 1$ dan mengabaikan titik pembalikan kedua $t = 3$.</sub>
- C. $4\text{ meter}$  
  <sub>Salah: Siswa menghitung perpindahan neto $\int_0^4 v(t)\,dt$ tanpa memperhatikan pembalikan arah gerak.</sub>
- **D. $12\text{ meter}$** ✅  
  <sub>Benar: Kecepatan nol saat $3(t - 1)(t - 3) = 0$, yaitu $t = 1$ dan $t = 3$. Partikel berbalik arah pada interval $[1, 3]$ sehingga jarak tempuh dihitung dari jumlahan nilai mutlak perpindahan tiap subinterval: $|\int_0^1 v(t)\,dt| + |\int_1^3 v(t)\,dt| + |\int_3^4 v(t)\,dt| = |4| + |-4| + |4| = 12\text{ meter}$.</sub>

**Pembahasan:** Langkah 1: Cari pembuat nol kecepatan $v(t) = 0$:
$$3t^2 - 12t + 9 = 0 \iff 3(t - 1)(t - 3) = 0 \iff t = 1 \text{ atau } t = 3$$
Pada $0 \le t < 1$, $v(t) > 0$.
Pada $1 < t < 3$, $v(t) < 0$.
Pada $3 < t \le 4$, $v(t) > 0$.

Langkah 2: Tentukan antiturunan fungsi kecepatan:
$$\int (3t^2 - 12t + 9)\,dt = t^3 - 6t^2 + 9t$$

Langkah 3: Hitung perpindahan tiap interval:
- Interval $[0, 1]$: $[t^3 - 6t^2 + 9t]_0^1 = (1 - 6 + 9) - 0 = 4$
- Interval $[1, 3]$: $[t^3 - 6t^2 + 9t]_1^3 = (27 - 54 + 27) - 4 = -4$
- Interval $[3, 4]$: $[t^3 - 6t^2 + 9t]_3^4 = (64 - 96 + 36) - 0 = 4$

Langkah 4: Hitung jarak total:
$$s = |4| + |-4| + |4| = 4 + 4 + 4 = 12\text{ meter}$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-14b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b03-b-hard-bt01-002
*variasi (angka) | C5 | 4 langkah | jenis: luas daerah kurva simetris*  **[warning validator]**

Luas bidang datar yang dibatasi oleh grafik fungsi $y = 9x - x^3$ dan sumbu-$x$ adalah .... satuan luas.

- A. $0$  
  <sub>Salah: Siswa mengintegralkan langsung dari $-3$ sampai $3$ tanpa membagi daerah di bawah dan di atas sumbu-$x$.</sub>
- B. $81$  
  <sub>Salah: Siswa lupa mengalikan koefisien pecahan $\frac{1}{2}$ dan $\frac{1}{4}$ pada hasil antiturunan suku aljabar.</sub>
- C. $\frac{81}{4}$  
  <sub>Salah: Siswa hanya menghitung satu sisi daerah pada interval $[0, 3]$ dan lupa memperhitungkan daerah pada $[-3, 0]$.</sub>
- **D. $\frac{81}{2}$** ✅  
  <sub>Benar: Kurva memotong sumbu-$x$ di $x = -3$, $x = 0$, dan $x = 3$. Karena kurva simetris ganjil, luas dihitung dengan $2 \int_0^3 (9x - x^3)\,dx = 2 [\frac{9}{2}x^2 - \frac{1}{4}x^4]_0^3 = 2 (\frac{81}{4}) = \frac{81}{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong dengan sumbu-$x$ ($y = 0$):
$$9x - x^3 = 0 \iff x(9 - x^2) = 0 \iff x(3 - x)(3 + x) = 0$$
Diperoleh absis titik potong $x = -3$, $x = 0$, dan $x = 3$.

Langkah 2: Menganalisis tanda fungsi pada selang:
- Pada $[-3, 0]$, grafik berada di bawah sumbu-$x$ ($y \le 0$).
- Pada $[0, 3]$, grafik berada di atas sumbu-$x$ ($y \ge 0$).

Langkah 3: Menghitung luas total dengan sifat simetri kurva ganjil:
$$L = 2 \int_0^3 (9x - x^3)\,dx$$

Langkah 4: Menghitung nilai integral:
$$L = 2 \left[ \frac{9}{2}x^2 - \frac{1}{4}x^4 \right]_0^3 = 2 \left( \frac{9}{2}(9) - \frac{1}{4}(81) \right) = 2 \left( \frac{81}{4} \right) = \frac{81}{2}$$
**Acuan:** siswa — siswa hal.216 Ayo Mencoba 3.10
**Warning:** kelas12_tl-b03-b-hard-bt01-002 sangat mirip dengan kelas12_tl-b03-b-hard-bt01-019 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b03-b-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: luas daerah antara dua kurva*

Luas daerah bidang datar yang dibatasi oleh kurva parabola $y = x^2$ dan garis $y = 2x + 3$ adalah .... satuan luas.

- **A. $\frac{32}{3}$** ✅  
  <sub>Benar: Titik potong kurva terjadi pada $x = -1$ dan $x = 3$. Garis berada di atas kurva pada selang $[-1, 3]$ sehingga luas daerahnya adalah $\int_{-1}^3 (2x + 3 - x^2)\,dx = [x^2 + 3x - \frac{1}{3}x^3]_{-1}^3 = 9 - (-\frac{5}{3}) = \frac{32}{3}$.</sub>
- B. $\frac{22}{3}$  
  <sub>Salah: Siswa keliru saat mengevaluasi batas bawah dengan mengabaikan tanda minus pada kubik $(-1)^3$.</sub>
- C. $\frac{40}{3}$  
  <sub>Salah: Siswa salah menjumlahkan pecahan pada saat substitusi batas atas dan batas bawah.</sub>
- D. $\frac{28}{3}$  
  <sub>Salah: Siswa melakukan kesalahan tanda saat mengurangkan kurva sehingga menggunakan persamaan $x^2 - 2x - 3$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong kedua kurva:
$$x^2 = 2x + 3 \iff x^2 - 2x - 3 = 0 \iff (x - 3)(x + 1) = 0$$
Diperoleh batas integrasi $x = -1$ dan $x = 3$.

Langkah 2: Menentukan kurva atas dan kurva bawah:
Untuk $x \in [-1, 3]$, garis $y = 2x + 3$ berada di atas kurva $y = x^2$.

Langkah 3: Menyusun formulasi integral luas:
$$L = \int_{-1}^3 ((2x + 3) - x^2)\,dx$$

Langkah 4: Menentukan antiturunan:
$$\int (2x + 3 - x^2)\,dx = \left[ x^2 + 3x - \frac{1}{3}x^3 \right]_{-1}^3$$

Langkah 5: Evaluasi batas integrasi:
- Batas atas $x = 3$: $(3)^2 + 3(3) - \frac{1}{3}(3)^3 = 9 + 9 - 9 = 9$
- Batas bawah $x = -1$: $(-1)^2 + 3(-1) - \frac{1}{3}(-1)^3 = 1 - 3 + \frac{1}{3} = -\frac{5}{3}$
$$L = 9 - \left( -\frac{5}{3} \right) = 9 + \frac{5}{3} = \frac{32}{3}$$
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b03-b-hard-bt01-004
*orisinal | C5 | 3 langkah | jenis: ekstremum fungsi akumulasi integral*

Diketahui fungsi $F(x)$ didefinisikan oleh $F(x) = \int_0^x (t^2 - 6t + 8)\,dt$ untuk setiap bilangan real $x$. Nilai maksimum lokal dari $F(x)$ tercapai pada saat $x = \dots.$

- A. $6$  
  <sub>Salah: Siswa salah mengintegralkan terlebih dahulu dan mencari pembuat nol secara keliru dari fungsi hasil integrasi.</sub>
- **B. $2$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, turunan pertama fungsi akumulasi adalah $F'(x) = x^2 - 6x + 8$. Titik kritis diperoleh saat $F'(x) = 0$, yaitu $(x - 2)(x - 4) = 0$ sehingga $x = 2$ atau $x = 4$. Melalui uji turunan kedua diperoleh $F''(x) = 2x - 6$. Untuk $x = 2$, $F''(2) = 2(2) - 6 = -2 < 0$, sehingga $x = 2$ memberikan nilai maksimum lokal.</sub>
- C. $3$  
  <sub>Salah: Siswa mencari sumbu simetri atau titik belok dari turunan pertamanya dengan rumus $-\frac{b}{2a}$.</sub>
- D. $4$  
  <sub>Salah: Siswa menentukan titik kritis tetapi tertukar dengan titik minimum lokal karena $F''(4) = 2 > 0$.</sub>

**Pembahasan:** Langkah 1: Terapkan Teorema Dasar Kalkulus I.
$$F'(x) = \frac{d}{dx}\left[\int_0^x (t^2 - 6t + 8)\,dt\right] = x^2 - 6x + 8$$

Langkah 2: Tentukan pembuat nol turunan pertama (titik stasioner).
$$x^2 - 6x + 8 = 0 \implies (x - 2)(x - 4) = 0$$
Diperoleh $x = 2$ atau $x = 4$.

Langkah 3: Tentukan jenis stasioner menggunakan turunan kedua.
$$F''(x) = 2x - 6$$
- Untuk $x = 2$: $F''(2) = 2(2) - 6 = -2 < 0$ (maksimum lokal).
- Untuk $x = 4$: $F''(4) = 2(4) - 6 = 2 > 0$ (minimum lokal).

Jadi, nilai maksimum lokal tercapai pada saat $x = 2$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b03-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: persamaan integral tentu*

Suatu fungsi linier $f(x) = ax + b$ memenuhi persamaan $\int_0^2 f(x)\,dx = 8$ dan $\int_0^4 f(x)\,dx = 24$. Nilai dari $\int_2^6 f(x)\,dx$ adalah ....

- A. $32$  
  <sub>Salah: Siswa mengabaikan suku konstanta $b$ dan hanya mengintegralkan $ax$.</sub>
- B. $16$  
  <sub>Salah: Siswa hanya menghitung $\int_2^4 f(x)\,dx = 24 - 8 = 16$ bukan $\int_2^6 f(x)\,dx$.</sub>
- **C. $40$** ✅  
  <sub>Benar: Integral fungsi $f(x)$ menghasilkan sistem persamaan: $2a + 2b = 8 \iff a + b = 4$ dan $8a + 4b = 24 \iff 2a + b = 6$. Diperoleh $a = 2$ dan $b = 2$, sehingga $f(x) = 2x + 2$. Nilai integral $\int_2^6 (2x + 2)\,dx = [x^2 + 2x]_2^6 = (36 + 12) - (4 + 4) = 48 - 8 = 40$.</sub>
- D. $48$  
  <sub>Salah: Siswa hanya menghitung nilai antiturunan pada batas atas $F(6)$ tanpa mengurangkan dengan $F(2)$.</sub>

**Pembahasan:** Langkah 1: Nyatakan integral tentu dalam bentuk parameter $a$ dan $b$.
$$\int_0^2 (ax + b)\,dx = \left[ \frac{1}{2}ax^2 + bx \right]_0^2 = 2a + 2b = 8 \implies a + b = 4$$
$$\int_0^4 (ax + b)\,dx = \left[ \frac{1}{2}ax^2 + bx \right]_0^4 = 8a + 4b = 24 \implies 2a + b = 6$$

Langkah 2: Selesaikan sistem persamaan untuk menemukan $a$ dan $b$.
$$(2a + b) - (a + b) = 6 - 4 \implies a = 2$$
$$b = 4 - a = 4 - 2 = 2$$
Sehingga $f(x) = 2x + 2$.

Langkah 3: Hitung integral yang diminta.
$$\int_2^6 (2x + 2)\,dx = \left[ x^2 + 2x \right]_2^6$$
$$= (6^2 + 2(6)) - (2^2 + 2(2)) = (36 + 12) - (4 + 4) = 48 - 8 = 40$$
**Acuan:** siswa — siswa hal.210

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b03-b-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi limit jumlahan riemann*

Nilai dari $\lim_{n \to \infty} \sum_{i=1}^n \frac{3}{n} \left( 2 + \frac{3i}{n} \right)^2$ adalah ....

- A. $117$  
  <sub>Salah: Siswa lupa membagi selisih kubik $125 - 8$ dengan penyebut $3$ dari rumus antiturunan $x^3/3$.</sub>
- **B. $39$** ✅  
  <sub>Benar: Bentuk limit jumlahan Riemann tersebut merepresentasikan $\int_2^5 x^2\,dx$ dengan lebar partisi $\Delta x = \frac{5 - 2}{n} = \frac{3}{n}$ dan titik ujung kanan $x_i = 2 + \frac{3i}{n}$. Nilai integralnya adalah $[\frac{1}{3}x^3]_2^5 = \frac{125 - 8}{3} = \frac{117}{3} = 39$.</sub>
- C. $35$  
  <sub>Salah: Siswa salah mengidentifikasi batas integrasi menjadi $[1, 4]$ sehingga menghitung $(64 - 1)/3$ lalu melakukan kesalahan aritmetika.</sub>
- D. $45$  
  <sub>Salah: Siswa mengira koefisien integral berubah karena faktor skala $3$ sehingga mengalikan hasil akhir.</sub>

**Pembahasan:** Langkah 1: Identifikasi komponen Jumlahan Riemann.
Bentuk umum: $\lim_{n \to \infty} \sum_{i=1}^n f(x_i) \Delta x$.
Dari soal, $\Delta x = \frac{3}{n}$ dan $x_i = 2 + i \Delta x = 2 + \frac{3i}{n}$.

Langkah 2: Tentukan batas bawah, batas atas, dan fungsi integran.
- Batas bawah $a = 2$.
- Karena $\Delta x = \frac{b - a}{n} = \frac{3}{n}$, maka $b - 2 = 3 \implies b = 5$.
- Fungsi integran adalah $f(x) = x^2$.

Langkah 3: Tuliskan dalam bentuk integral tentu.
$$\lim_{n \to \infty} \sum_{i=1}^n \frac{3}{n} \left( 2 + \frac{3i}{n} \right)^2 = \int_2^5 x^2\,dx$$

Langkah 4: Hitung nilai integral tentu.
$$\int_2^5 x^2\,dx = \left[ \frac{x^3}{3} \right]_2^5 = \frac{5^3 - 2^3}{3} = \frac{125 - 8}{3} = \frac{117}{3} = 39$$
**Acuan:** siswa — siswa hal.200

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b03-b-hard-bt01-007
*variasi (angka) | C5 | 4 langkah | jenis: jarak tempuh gerak partikel*

Sebuah partikel bergerak sepanjang garis lurus sehingga kecepatannya pada waktu $t$ ditentukan oleh $v(t) = 6t - 3t^2$ (dalam meter per detik). Jarak yang ditempuh partikel selama periode waktu $0 \le t \le 3$ detik adalah ....

- A. $12\text{ meter}$  
  <sub>Salah: Siswa salah menentukan antiturunan dengan tidak membagi koefisien pangkat.</sub>
- B. $0\text{ meter}$  
  <sub>Salah: Siswa hanya menghitung perpindahan total dengan mengintegralkan langsung $\int_0^3 v(t)\,dt = [3t^2 - t^3]_0^3 = 27 - 27 = 0$.</sub>
- C. $4\text{ meter}$  
  <sub>Salah: Siswa hanya menghitung jarak tempuh saat partikel bergerak maju pada selang waktu $0 \le t \le 2$.</sub>
- **D. $8\text{ meter}$** ✅  
  <sub>Benar: Kecepatan nol pada $t = 2$. Pada interval $[0, 2]$, $v(t) \ge 0$ dengan perpindahan $\int_0^2 (6t - 3t^2)\,dt = [3t^2 - t^3]_0^2 = 12 - 8 = 4\text{ m}$. Pada interval $[2, 3]$, $v(t) \le 0$ dengan perpindahan $\int_2^3 (6t - 3t^2)\,dt = (27 - 27) - (12 - 8) = -4\text{ m}$. Jarak total yang ditempuh adalah $4 + |-4| = 8\text{ meter}$.</sub>

**Pembahasan:** Langkah 1: Tentukan waktu ketika partikel berbalik arah ($v(t) = 0$).
$$6t - 3t^2 = 0 \implies 3t(2 - t) = 0$$
Partikel berbalik arah pada $t = 2$ detik.

Langkah 2: Bagi interval waktu pengamatan $[0, 3]$ menjadi dua subinterval.
- Pada interval $[0, 2]$, $v(t) \ge 0$ (bergerak maju).
- Pada interval $[2, 3]$, $v(t) \le 0$ (bergerak mundur).

Langkah 3: Hitung jarak pada masing-masing subinterval menggunakan fungsi posisi $s(t) = 3t^2 - t^3$.
- Jarak pada $[0, 2]$: $s(2) - s(0) = (3(2^2) - 2^3) - 0 = 12 - 8 = 4\text{ meter}$.
- Jarak pada $[2, 3]$: $|s(3) - s(2)| = |(3(3^2) - 3^3) - (3(2^2) - 2^3)| = |0 - 4| = 4\text{ meter}$.

Langkah 4: Jumlahkan jarak tempuh total.
$$s_{\text{total}} = 4 + 4 = 8\text{ meter}$$
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-14b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b03-b-hard-bt01-008
*variasi (angka) | C5 | 5 langkah | jenis: luas daerah terbagi sumbu-x*  **[warning validator]**

Luas bidang datar yang dibatasi oleh grafik fungsi $y = x^3 - 6x^2 + 8x$ dan sumbu-$x$ adalah .... satuan luas.

- A. $16$  
  <sub>Salah: Kesalahan menentukan batas integral menjadi $[0, 4]$ lalu menjumlahkan batas kuadrat tanpa membagi koefisien polinomial secara benar.</sub>
- B. $0$  
  <sub>Salah: Mengintegralkan langsung dari $0$ sampai $4$ tanpa memisahkan tanda interval di bawah sumbu-x sehingga kedua daerah saling meniadakan.</sub>
- **C. $8$** ✅  
  <sub>Benar: Akar fungsi adalah $x = 0, 2, 4$. Daerah $[0, 2]$ berada di atas sumbu-$x$ dengan luas $\int_0^2 (x^3 - 6x^2 + 8x)\,dx = 4$. Daerah $[2, 4]$ berada di bawah sumbu-$x$ dengan luas $-\int_2^4 (x^3 - 6x^2 + 8x)\,dx = 4$. Total luas adalah $4 + 4 = 8$.</sub>
- D. $4$  
  <sub>Salah: Hanya menghitung salah satu luasan pada selang $[0, 2]$ dan lupa menambahkan luasan pada selang $[2, 4]$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik potong kurva dengan sumbu-$x$ ($y = 0$):
$$x^3 - 6x^2 + 8x = 0 \iff x(x - 2)(x - 4) = 0$$
Diperoleh pembuat nol $x = 0$, $x = 2$, dan $x = 4$.

Langkah 2: Menentukan tanda fungsi pada tiap interval:
- Untuk $x \in (0, 2)$, ambil $x = 1$: $y = 1( -1 )( -3 ) = 3 > 0$ (di atas sumbu-$x$).
- Untuk $x \in (2, 4)$, ambil $x = 3$: $y = 3( 1 )( -1 ) = -3 < 0$ (di bawah sumbu-$x$).

Langkah 3: Menghitung luas daerah pertama ($L_1$):
$$L_1 = \int_0^2 (x^3 - 6x^2 + 8x)\,dx = \left[ \frac{1}{4}x^4 - 2x^3 + 4x^2 \right]_0^2 = \left( \frac{16}{4} - 2(8) + 4(4) \right) - 0 = 4 - 16 + 16 = 4$$

Langkah 4: Menghitung luas daerah kedua ($L_2$):
$$L_2 = -\int_2^4 (x^3 - 6x^2 + 8x)\,dx = -\left[ \frac{1}{4}x^4 - 2x^3 + 4x^2 \right]_2^4$$
$$\left[ \frac{1}{4}x^4 - 2x^3 + 4x^2 \right]_2^4 = (64 - 128 + 64) - 4 = 0 - 4 = -4$$
$$L_2 = -(-4) = 4$$

Langkah 5: Menghitung luas total:
$$L = L_1 + L_2 = 4 + 4 = 8\text{ satuan luas.}$$
**Acuan:** siswa — siswa hal.216 Ayo Mencoba 3.10
**Warning:** kelas12_tl-b03-b-hard-bt01-008 sangat mirip dengan kelas12_tl-b03-b-hard-bt01-019 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b03-b-hard-bt01-009
*orisinal | C5 | 4 langkah | jenis: pembagian luas daerah oleh parameter*

Daerah yang dibatasi oleh kurva $y = 3x^2$, sumbu-$x$, dan garis $x = 2$ dibagi menjadi dua daerah dengan luas yang sama oleh garis vertikal $x = k$ (dengan $0 < k < 2$). Nilai $k$ adalah ....

- A. $1$  
  <sub>Salah: Mengira garis pembagi luas kurva selalu membagi panjang interval sumbu-x secara simetris di titik tengah $k = \frac{0+2}{2} = 1$.</sub>
- **B. $\sqrt[3]{4}$** ✅  
  <sub>Benar: Luas total adalah $\int_0^2 3x^2\,dx = 8$. Syarat setengah luas adalah $\int_0^k 3x^2\,dx = k^3 = 4$, sehingga diperoleh $k = \sqrt[3]{4}$.</sub>
- C. $\sqrt{2}$  
  <sub>Salah: Salah mengintegralkan $3x^2$ menjadi $x^2$ sehingga memperoleh persamaan $k^2 = 2$.</sub>
- D. $\sqrt[3]{2}$  
  <sub>Salah: Menyamakan luas daerah dengan $2$ alih-alih setengah dari total luas yang bernilai $8$.</sub>

**Pembahasan:** Langkah 1: Menghitung luas total daerah di bawah kurva dari $x = 0$ hingga $x = 2$:
$$L_{\text{total}} = \int_0^2 3x^2\,dx = \left[ x^3 \right]_0^2 = 2^3 - 0 = 8$$

Langkah 2: Menentukan luas daerah yang dibatasi dari $x = 0$ hingga $x = k$:
$$L_1 = \int_0^k 3x^2\,dx = \left[ x^3 \right]_0^k = k^3$$

Langkah 3: Menggunakan syarat bahwa garis $x = k$ membagi dua luas daerah sama besar:
$$L_1 = \frac{1}{2} L_{\text{total}} \iff k^3 = \frac{1}{2}(8) = 4$$

Langkah 4: Menarik akar pangkat tiga:
$$k = \sqrt[3]{4}$$
**Acuan:** siswa — siswa hal.213

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b03-b-hard-bt01-010
*orisinal | C6 | 5 langkah | jenis: evaluasi integral tentu fungsi simetri*

Nilai dari $\int_{-2}^{2} (5x^7 - 3x^3 + 4x^2 - 1)\,dx$ adalah ....

- A. $0$  
  <sub>Salah: Mengira seluruh polinomial bersifat ganjil pada batas interval $[-2, 2]$ sehingga langsung menyimpulkan hasilnya nol.</sub>
- B. $\frac{26}{3}$  
  <sub>Salah: Lupa mengalikan dengan faktor $2$ saat menyederhanakan integral fungsi genap dari $0$ sampai $2$.</sub>
- **C. $\frac{52}{3}$** ✅  
  <sub>Benar: Suku berpangkat ganjil bernilai nol pada interval simetris $[-2, 2]$. Sisa suku genap menghasilkan $2\int_0^2 (4x^2 - 1)\,dx = 2[\frac{4}{3}(8) - 2] = 2[\frac{32}{3} - \frac{6}{3}] = \frac{52}{3}$.</sub>
- D. $\frac{64}{3}$  
  <sub>Salah: Mengabaikan suku konstan $-1$ dan hanya menghitung integral dari $4x^2$.</sub>

**Pembahasan:** Langkah 1: Menguraikan integral berdasarkan sifat kelinearan:
$$\int_{-2}^{2} (5x^7 - 3x^3 + 4x^2 - 1)\,dx = \int_{-2}^{2} (5x^7 - 3x^3)\,dx + \int_{-2}^{2} (4x^2 - 1)\,dx$$

Langkah 2: Menganalisis sifat kesimetrisan fungsi ganjil:
Fungsi $g(x) = 5x^7 - 3x^3$ adalah fungsi ganjil karena $g(-x) = -g(x)$.
Pada interval simetris $[-a, a]$, nilai integral fungsi ganjil adalah $0$:
$$\int_{-2}^{2} (5x^7 - 3x^3)\,dx = 0$$

Langkah 3: Menganalisis fungsi genap $h(x) = 4x^2 - 1$:
Karena $h(-x) = h(x)$, maka:
$$\int_{-2}^{2} (4x^2 - 1)\,dx = 2 \int_0^2 (4x^2 - 1)\,dx$$

Langkah 4: Menghitung integral tentu suku genap:
$$\int_0^2 (4x^2 - 1)\,dx = \left[ \frac{4}{3}x^3 - x \right]_0^2 = \left( \frac{4}{3}(8) - 2 \right) - 0 = \frac{32}{3} - \frac{6}{3} = \frac{26}{3}$$

Langkah 5: Mengalikan dengan faktor simetri:
$$\int_{-2}^{2} (4x^2 - 1)\,dx = 2 \cdot \frac{26}{3} = \frac{52}{3}$$
**Acuan:** siswa — siswa hal.204

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b03-b-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: titik belok fungsi akumulasi integral*

Diketahui suatu fungsi $F(x)$ didefinisikan oleh $F(x) = \int_0^x (t^3 - 6t^2 + 9t)\,dt$ untuk setiap bilangan real $x$. Jumlah semua absis dari titik belok grafik fungsi $F(x)$ adalah ....

- A. $6$  
  <sub>Salah: Siswa memakai rumus $-\frac{b}{a}$ dari turunan pertama alih-alih turunan kedua.</sub>
- B. $3$  
  <sub>Salah: Siswa mencari pembuat nol dari $F'(x) = x(x - 3)^2 = 0$ dan menjumlahkan nilai kritisnya ($0 + 3$).</sub>
- C. $2$  
  <sub>Salah: Siswa hanya mengambil nilai rata-rata dari kedua absis titik belok $\frac{1 + 3}{2} = 2$.</sub>
- **D. $4$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, $F'(x) = x^3 - 6x^2 + 9x$, sehingga $F''(x) = 3x^2 - 12x + 9 = 3(x - 1)(x - 3)$. Titik belok terjadi pada $x = 1$ dan $x = 3$, sehingga jumlah absisnya $1 + 3 = 4$.</sub>

**Pembahasan:** Berdasarkan Teorema Dasar Kalkulus I:
$$
F'(x) = \frac{d}{dx} \left[ \int_0^x (t^3 - 6t^2 + 9t)\,dt \right] = x^3 - 6x^2 + 9x
$$
Titik belok diperoleh saat turunan kedua $F''(x) = 0$ dan terjadi perubahan tanda kecekungan:
$$
F''(x) = 3x^2 - 12x + 9
$$
Selesaikan persamaan $F''(x) = 0$:
$$
3(x^2 - 4x + 3) = 0 \iff 3(x - 1)(x - 3) = 0
$$
Didapatkan dua nilai absis, yaitu $x_1 = 1$ dan $x_2 = 3$. Karena $F''(x)$ berganti tanda di sekitar kedua titik tersebut, maka keduanya merupakan absis titik belok.
$$
x_1 + x_2 = 1 + 3 = 4
$$
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b03-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: luas daerah dua kurva parabola*

Luas bidang datar yang dibatasi oleh kurva parabola $y = 12 - x^2$ dan $y = x^2 - 6$ adalah .... satuan luas.

- A. $54$  
  <sub>Salah: Siswa salah saat mengintegrasikan suku konstan, menghitung $18(3) - 18 = 36$ lalu dikurangi $0$.</sub>
- B. $108$  
  <sub>Salah: Siswa menjumlahkan kedua fungsi alih-alih mengurangkannya sehingga mengintegralkan $6$ atau salah mengalikan.</sub>
- **C. $72$** ✅  
  <sub>Benar: Titik potong kurva adalah $12 - x^2 = x^2 - 6 \iff 2x^2 = 18 \iff x = \pm 3$. Luas dihitung dengan $\int_{-3}^3 (18 - 2x^2)\,dx = [18x - \frac{2}{3}x^3]_{-3}^3 = 36 - (-36) = 72$.</sub>
- D. $36$  
  <sub>Salah: Siswa hanya mengintegralkan dari $0$ sampai $3$ tanpa mengalikan dua untuk keseluruhan interval simetris.</sub>

**Pembahasan:** Menentukan batas integrasi dari absis titik potong kedua kurva:
$$
12 - x^2 = x^2 - 6 \implies 2x^2 = 18 \implies x^2 = 9 \implies x = -3 \text{ atau } x = 3
$$
Pada selang $[-3, 3]$, grafik $y = 12 - x^2$ berada di atas $y = x^2 - 6$. Luas daerah:
$$
L = \int_{-3}^3 \left[ (12 - x^2) - (x^2 - 6) \right]\,dx = \int_{-3}^3 (18 - 2x^2)\,dx
$$
Memanfaatkan sifat kesimetrian fungsi genap:
$$
L = 2 \int_0^3 (18 - 2x^2)\,dx = 2 \left[ 18x - \frac{2}{3}x^3 \right]_0^3
$$
Evaluasi:
$$
L = 2 \left( 18(3) - \frac{2}{3}(27) \right) = 2(54 - 18) = 2(36) = 72\text{ satuan luas}
$$
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b03-b-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: relasi partisi interval integral tentu*

Diketahui suatu fungsi $f(x)$ kontinu pada himpunan bilangan real dan memenuhi $\int_0^3 f(x)\,dx = 7$, $\int_0^5 f(x)\,dx = 15$, serta $\int_2^5 f(x)\,dx = 11$. Nilai dari $\int_2^3 [4f(x) - 5]\,dx$ adalah ....

- **A. $7$** ✅  
  <sub>Benar: $\int_0^2 f(x)\,dx = 15 - 11 = 4$, sehingga $\int_2^3 f(x)\,dx = 7 - 4 = 3$. Maka $\int_2^3 [4f(x) - 5]\,dx = 4(3) - 5(3 - 2) = 12 - 5 = 7$.</sub>
- B. $2$  
  <sub>Salah: Siswa mengurangkan konstanta $-5$ dua kali atau salah menghitung $\int_2^3 f(x)\,dx = 2$.</sub>
- C. $17$  
  <sub>Salah: Siswa menjumlahkan $12 + 5$ karena salah tanda pada pengintegralan suku konstanta.</sub>
- D. $12$  
  <sub>Salah: Siswa menghitung $4 \int_2^3 f(x)\,dx = 12$ namun lupa mengintegralkan konstanta $-5$.</sub>

**Pembahasan:** Berdasarkan sifat penambahan selang integral tentu:
$$
\int_0^5 f(x)\,dx = \int_0^2 f(x)\,dx + \int_2^5 f(x)\,dx
$$
Substitusikan nilai yang diketahui:
$$
15 = \int_0^2 f(x)\,dx + 11 \implies \int_0^2 f(x)\,dx = 4
$$
Selanjutnya, untuk selang $[0, 3]$:
$$
\int_0^3 f(x)\,dx = \int_0^2 f(x)\,dx + \int_2^3 f(x)\,dx
$$
$$
7 = 4 + \int_2^3 f(x)\,dx \implies \int_2^3 f(x)\,dx = 3
$$
Hitung nilai dari integral yang ditanyakan:
$$
\int_2^3 [4f(x) - 5]\,dx = 4 \int_2^3 f(x)\,dx - \int_2^3 5\,dx = 4(3) - 5(3 - 2) = 12 - 5 = 7
$$
**Acuan:** siswa — siswa hal.204

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b03-b-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: penyelesaian parameter integral tentu*

Diketahui suatu persamaan integral tentu $\int_0^m (6x^2 - 10x + 3)\,dx = 0$. Jika nilai parameter $m > 1$, maka nilai $m$ yang memenuhi adalah ....

- A. $1$  
  <sub>Salah: Siswa memilih akar $m = 1$ yang tidak memenuhi syarat ketaksamaan tegas $m > 1$.</sub>
- **B. $1{,}5$** ✅  
  <sub>Benar: Integral menghasilkan $2m^3 - 5m^2 + 3m = m(2m - 3)(m - 1) = 0$. Karena $m > 1$, nilai yang memenuhi adalah $m = \frac{3}{2} = 1{,}5$.</sub>
- C. $2{,}5$  
  <sub>Salah: Siswa salah mendiferensialkan atau salah menggunakan rumus kuadratik $\frac{-b}{2a} = \frac{5}{2}$.</sub>
- D. $2$  
  <sub>Salah: Siswa salah memfaktorkan persamaan kuadrat menjadi $(m - 2)(2m - 1)$.</sub>

**Pembahasan:** Hitung integral tentu fungsi terhadap $x$ dengan batas $0$ sampai $m$:
$$
\int_0^m (6x^2 - 10x + 3)\,dx = \left[ 2x^3 - 5x^2 + 3x \right]_0^m = 2m^3 - 5m^2 + 3m
$$
Persamaan yang harus dipenuhi:
$$
2m^3 - 5m^2 + 3m = 0 \iff m(2m^2 - 5m + 3) = 0
$$
Faktorkan bagian persamaan kuadrat:
$$
m(m - 1)(2m - 3) = 0
$$
Pembuat nol persamaan adalah $m = 0$, $m = 1$, atau $m = \frac{3}{2} = 1{,}5$.
Karena diketahui syarat $m > 1$, maka nilai $m$ yang memenuhi adalah $1{,}5$.
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b03-b-hard-bt01-015
*variasi (angka) | C5 | 5 langkah | jenis: evaluasi perpindahan partikel*

Sebuah partikel bergerak sepanjang garis sehingga kecepatannya pada waktu $t$ adalah $v(t) = 3t^2 - 12t + 9$ (dalam meter per detik). Tentukan perpindahan partikel dalam periode waktu $0 \le t \le 5$.

- A. $28\text{ meter}$  
  <sub>Salah: Menghitung jarak tempuh total dengan menjumlahkan nilai mutlak luas setiap daerah alih-alih perpindahan netto.</sub>
- B. $45\text{ meter}$  
  <sub>Salah: Salah melakukan perkalian pada suku kedua saat evaluasi batas atas sehingga menganggap $6 \times 25 = 125$.</sub>
- **C. $20\text{ meter}$** ✅  
  <sub>Benar: Perpindahan partikel diperoleh dengan mengintegralkan fungsi kecepatan pada selang waktu yang diberikan: $\int_0^5 (3t^2 - 12t + 9)\,dt = [t^3 - 6t^2 + 9t]_0^5 = (125 - 150 + 45) - 0 = 20\text{ meter}$.</sub>
- D. $-20\text{ meter}$  
  <sub>Salah: Terbalik dalam mengurangkan batas integrasi batas bawah dikurangi batas atas.</sub>

**Pembahasan:** Perpindahan partikel ($s$) dalam selang waktu $0 \le t \le 5$ dihitung menggunakan integral tentu fungsi kecepatan:
$$
s = \int_0^5 v(t)\,dt = \int_0^5 (3t^2 - 12t + 9)\,dt
$$
Antiturunan dari $v(t)$ adalah:
$$
\int (3t^2 - 12t + 9)\,dt = t^3 - 6t^2 + 9t
$$
Evaluasi pada batas integrasi $[0, 5]$:
$$
s = \left[ t^3 - 6t^2 + 9t \right]_0^5 = (5^3 - 6(5)^2 + 9(5)) - (0^3 - 6(0)^2 + 9(0))
$$
$$
s = (125 - 150 + 45) - 0 = 20\text{ meter}
$$
Jadi, perpindahan partikel tersebut adalah $20\text{ meter}$.
**Acuan:** pretest — kelas12_tl-b03-p0219-latihan-soal-integral-tentu-14a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b03-b-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: nilai minimum fungsi akumulasi integral*

Diketahui fungsi $F(x)$ didefinisikan oleh $F(x) = \int_{-1}^x (3t^2 - 6t - 9)\,dt$ untuk setiap bilangan real $x$. Nilai minimum relatif dari fungsi $F(x)$ adalah ....

- **A. $-32$** ✅  
  <sub>Benar: Berdasarkan Teorema Dasar Kalkulus I, $F'(x) = 3x^2 - 6x - 9$. Titik stasioner diperoleh saat $F'(x) = 0 \iff 3(x - 3)(x + 1) = 0$, yaitu $x = -1$ atau $x = 3$. Turunan kedua $F''(x) = 6x - 6$; untuk $x = 3$ diperoleh $F''(3) = 12 > 0$ sehingga titik minimum relatif berada di $x = 3$. Nilai minimum relatifnya adalah $F(3) = \int_{-1}^3 (3t^2 - 6t - 9)\,dt = [t^3 - 3t^2 - 9t]_{-1}^3 = (27 - 27 - 27) - (-1 - 3 + 9) = -27 - 5 = -32$.</sub>
- B. $0$  
  <sub>Salah: Mengevaluasi fungsi pada absis stasioner lainnya yaitu $x = -1$ yang menghasilkan nilai maksimum relatif.</sub>
- C. $-27$  
  <sub>Salah: Hanya menghitung nilai antiturunan pada batas atas $t = 3$ dan lupa mengurangkan nilai batas bawah $t = -1$.</sub>
- D. $-22$  
  <sub>Salah: Terjadi kesalahan tanda saat mengurangkan nilai batas bawah, yaitu $-27 - (-5) = -22$.</sub>

**Pembahasan:** Langkah 1: Terapkan Teorema Dasar Kalkulus I untuk menentukan turunan $F(x)$:
$$F'(x) = 3x^2 - 6x - 9$$

Langkah 2: Tentukan titik kritis dengan memfaktorkan turunan pertama:
$$3(x^2 - 2x - 3) = 0 \iff 3(x - 3)(x + 1) = 0$$
Diperoleh $x = -1$ atau $x = 3$.

Langkah 3: Tentukan jenis stasioner menggunakan uji turunan kedua:
$$F''(x) = 6x - 6$$
Untuk $x = 3$, $F''(3) = 6(3) - 6 = 12 > 0$ (mencapai minimum relatif).

Langkah 4: Hitung nilai minimum relatif $F(3)$:
$$F(3) = \int_{-1}^3 (3t^2 - 6t - 9)\,dt = \left[ t^3 - 3t^2 - 9t \right]_{-1}^3$$
$$F(3) = (3^3 - 3(3)^2 - 9(3)) - ((-1)^3 - 3(-1)^2 - 9(-1))$$
$$F(3) = (27 - 27 - 27) - (-1 - 3 + 9) = -27 - 5 = -32$$
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b03-b-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: penentuan parameter fungsi kuadrat*

Diketahui suatu fungsi kuadrat $f(x) = 3x^2 + 2ax + b$ memenuhi $\int_0^1 f(x)\,dx = 4$ dan $\int_0^2 f(x)\,dx = 16$. Nilai dari $f(3)$ adalah ....

- A. $31$  
  <sub>Salah: Tertukar nilai parameter $a$ dan $b$ sehingga fungsi menjadi $f(x) = 3x^2 + 4x + 1$ lalu salah substitusi.</sub>
- **B. $35$** ✅  
  <sub>Benar: Evaluasi integral pertama: $\int_0^1 (3x^2 + 2ax + b)\,dx = [x^3 + ax^2 + bx]_0^1 = 1 + a + b = 4 \implies a + b = 3$. Evaluasi integral kedua: $\int_0^2 (3x^2 + 2ax + b)\,dx = [x^3 + ax^2 + bx]_0^2 = 8 + 4a + 2b = 16 \implies 4a + 2b = 8 \implies 2a + b = 4$. Dari eliminasi kedua persamaan diperoleh $a = 1$ dan $b = 2$. Maka $f(x) = 3x^2 + 2x + 2$. Nilai $f(3) = 3(3)^2 + 2(3) + 2 = 27 + 6 + 2 = 35$.</sub>
- C. $39$  
  <sub>Salah: Kesalahan eliminasi pada suku $2a + b = 4$ yang dihitung menjadi $a = 2$ sehingga $b = 1$ dan $f(3) = 27 + 12 + 1 = 40$ lalu dikurangi satu.</sub>
- D. $27$  
  <sub>Salah: Hanya menghitung suku berderajat dua $3(3)^2 = 27$ dan mengabaikan suku linear serta konstanta.</sub>

**Pembahasan:** Langkah 1: Integralkan $f(x)$ pada batas $[0, 1]$:
$$\int_0^1 (3x^2 + 2ax + b)\,dx = \left[ x^3 + ax^2 + bx \right]_0^1 = 1 + a + b = 4 \implies a + b = 3 \quad \text{...(1)}$$

Langkah 2: Integralkan $f(x)$ pada batas $[0, 2]$:
$$\int_0^2 (3x^2 + 2ax + b)\,dx = \left[ x^3 + ax^2 + bx \right]_0^2 = 8 + 4a + 2b = 16$$
$$4a + 2b = 8 \implies 2a + b = 4 \quad \text{...(2)}$$

Langkah 3: Eliminasi persamaan (2) dan (1):
$$(2a + b) - (a + b) = 4 - 3 \implies a = 1$$
Substitusikan nilai $a = 1$ ke persamaan (1):
$$1 + b = 3 \implies b = 2$$

Langkah 4: Tentukan fungsi $f(x)$ dan hitung $f(3)$:
$$f(x) = 3x^2 + 2x + 2$$
$$f(3) = 3(3)^2 + 2(3) + 2 = 27 + 6 + 2 = 35$$
**Acuan:** siswa — siswa hal.208

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b03-b-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: luas daerah irisan parabola dan garis*

Luas daerah bidang datar yang dibatasi oleh kurva parabola $y = x^2 - 2x$ dan garis $y = x + 4$ adalah .... satuan luas.

- **A. $\frac{125}{6}$** ✅  
  <sub>Benar: Titik potong kurva: $x^2 - 2x = x + 4 \iff x^2 - 3x - 4 = 0 \iff (x - 4)(x + 1) = 0$, sehingga batas integrasi adalah $x = -1$ sampai $x = 4$. Pada interval $[-1, 4]$, garis berada di atas parabola sehingga luas daerahnya adalah $L = \int_{-1}^4 ((x + 4) - (x^2 - 2x))\,dx = \int_{-1}^4 (-x^2 + 3x + 4)\,dx = [-\frac{1}{3}x^3 + \frac{3}{2}x^2 + 4x]_{-1}^4 = (-\frac{64}{3} + 24 + 16) - (\frac{1}{3} + \frac{3}{2} - 4) = \frac{56}{3} - (-\frac{13}{6}) = \frac{112}{6} + \frac{13}{6} = \frac{125}{6}$.</sub>
- B. $\frac{125}{3}$  
  <sub>Salah: Lupa membagi penyebut dengan faktor 2 saat menyamakan penyebut pecahan.</sub>
- C. $\frac{56}{3}$  
  <sub>Salah: Hanya menghitung nilai batas atas $x = 4$ dan mengabaikan batas bawah $x = -1$.</sub>
- D. $\frac{33}{2}$  
  <sub>Salah: Kesalahan tanda saat menghitung selisih nilai batas atas dan batas bawah, yaitu $\frac{56}{3} - \frac{13}{6} = \frac{99}{6} = \frac{33}{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan batas integrasi melalui absis titik potong kedua kurva:
$$x^2 - 2x = x + 4$$
$$x^2 - 3x - 4 = 0 \iff (x - 4)(x + 1) = 0$$
Diperoleh $x = -1$ (batas bawah) dan $x = 4$ (batas atas).

Langkah 2: Menentukan kurva pembatas atas dan bawah pada interval $[-1, 4]$. Untuk $x = 0$, garis bernilai $y = 4$ dan kurva bernilai $y = 0$, sehingga garis berada di atas parabola.

Langkah 3: Menyusun integral luas daerah:
$$L = \int_{-1}^4 \left((x + 4) - (x^2 - 2x)\right)\,dx = \int_{-1}^4 (-x^2 + 3x + 4)\,dx$$

Langkah 4: Menghitung nilai integral tentu:
$$L = \left[ -\frac{1}{3}x^3 + \frac{3}{2}x^2 + 4x \right]_{-1}^4$$
Substitusi batas atas $x = 4$:
$$-\frac{1}{3}(64) + \frac{3}{2}(16) + 4(4) = -\frac{64}{3} + 24 + 16 = 40 - \frac{64}{3} = \frac{56}{3}$$
Substitusi batas bawah $x = -1$:
$$-\frac{1}{3}(-1) + \frac{3}{2}(1) + 4(-1) = \frac{1}{3} + \frac{3}{2} - 4 = \frac{2 + 9 - 24}{6} = -\frac{13}{6}$$
Maka luas daerahnya adalah:
$$L = \frac{56}{3} - \left(-\frac{13}{6}\right) = \frac{112}{6} + \frac{13}{6} = \frac{125}{6}$$
**Acuan:** siswa — siswa hal.214

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b03-b-hard-bt01-019
*variasi (angka) | C5 | 4 langkah | jenis: luas kurva suku banyak berderajat tiga*  **[warning validator]**

Luas bidang datar yang dibatasi oleh grafik fungsi $y = x^3 - 16x$ dan sumbu-$x$ adalah .... satuan luas.

- **A. 128** ✅  
  <sub>Benar: Menentukan batas integrasi dari pembuat nol fungsi: $x(x - 4)(x + 4) = 0$, sehingga diperoleh $x = -4$, $x = 0$, dan $x = 4$. Pada selang $[-4, 0]$, kurva berada di atas sumbu-$x$, sedangkan pada selang $[0, 4]$, kurva berada di bawah sumbu-$x$. Luas total adalah $\int_{-4}^0 (x^3 - 16x)\,dx - \int_0^4 (x^3 - 16x)\,dx = 64 - (-64) = 128$.</sub>
- B. 0  
  <sub>Salah: Siswa langsung mengintegrasikan $\int_{-4}^4 (x^3 - 16x)\,dx$ tanpa memecah interval, sehingga kedua bagian saling meniadakan karena fungsi ganjil.</sub>
- C. 256  
  <sub>Salah: Siswa salah saat menentukan antiturunan dengan tidak membagi koefisien suku berderajat 4 secara benar.</sub>
- D. 64  
  <sub>Salah: Siswa hanya menghitung luas salah satu partisi daerah tanpa menjumlahkan kedua bagian yang simetris.</sub>

**Pembahasan:** Titik potong kurva $y = x^3 - 16x$ dengan sumbu-$x$ diperoleh ketika $y = 0$:
$$x^3 - 16x = 0 \iff x(x^2 - 16) = 0 \iff x(x - 4)(x + 4) = 0$$
Diperoleh batas-batas daerah $x = -4$, $x = 0$, dan $x = 4$.

1. Pada selang $[-4, 0]$, nilai $y \ge 0$ (daerah di atas sumbu-$x$):
$$L_1 = \int_{-4}^0 (x^3 - 16x)\,dx = \left[ \frac{1}{4}x^4 - 8x^2 \right]_{-4}^0 = 0 - \left( \frac{1}{4}(-4)^4 - 8(-4)^2 \right) = -(64 - 128) = 64$$

2. Pada selang $[0, 4]$, nilai $y \le 0$ (daerah di bawah sumbu-$x$):
$$L_2 = -\int_0^4 (x^3 - 16x)\,dx = -\left[ \frac{1}{4}x^4 - 8x^2 \right]_0^4 = -\left( \frac{1}{4}(4)^4 - 8(4)^2 - 0 \right) = -(64 - 128) = 64$$

Luas total bidang datar adalah:
$$L = L_1 + L_2 = 64 + 64 = 128\text{ satuan luas}.$$
**Acuan:** siswa — siswa hal.217 Ayo Mencoba 3.10
**Warning:** kelas12_tl-b03-b-hard-bt01-002 sangat mirip dengan kelas12_tl-b03-b-hard-bt01-019 (0.85) padahal acuan beda
**Warning:** kelas12_tl-b03-b-hard-bt01-008 sangat mirip dengan kelas12_tl-b03-b-hard-bt01-019 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b03-b-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: garis singgung fungsi akumulasi integral*

Diketahui suatu fungsi $F(x) = \int_2^x (3t^2 - 8t + 1)\,dt$ untuk setiap bilangan real $x$. Jika garis singgung grafik fungsi $F(x)$ di titik berabsis $x = a$ (dengan $a > 0$) tegak lurus terhadap garis $x + 4y - 12 = 0$, maka nilai $a$ adalah ....

- A. 1  
  <sub>Salah: Siswa salah menyamakan gradien garis singgung dengan gradien garis yang diketahui tanpa mengubah menjadi kondisi tegak lurus.</sub>
- B. -\frac{1}{3}  
  <sub>Salah: Siswa mengabaikan syarat $a > 0$ dan memilih akar yang bernilai negatif.</sub>
- C. 4  
  <sub>Salah: Siswa keliru menganggap nilai gradien sebagai nilai absis $a$.</sub>
- **D. 3** ✅  
  <sub>Benar: Garis $x + 4y - 12 = 0$ memiliki gradien $m_1 = -\frac{1}{4}$. Karena tegak lurus, gradien garis singgung adalah $m = 4$. Berdasarkan Teorema Dasar Kalkulus I, $F'(x) = 3x^2 - 8x + 1$. Persamaan $3a^2 - 8a + 1 = 4 \iff 3a^2 - 8a - 3 = 0$ menghasilkan akar $a = 3$ atau $a = -\frac{1}{3}$. Karena disyaratkan $a > 0$, maka nilai yang memenuhi adalah $a = 3$.</sub>

**Pembahasan:** Langkah 1: Menentukan gradien garis yang diketahui.
Persamaan garis $x + 4y - 12 = 0 \iff 4y = -x + 12 \iff y = -\frac{1}{4}x + 3$.
Gradien garis tersebut adalah $m_1 = -\frac{1}{4}$.

Langkah 2: Menentukan gradien garis singgung.
Karena garis singgung tegak lurus terhadap garis di atas, berlaku:
$$m \cdot m_1 = -1 \iff m \left(-\frac{1}{4}\right) = -1 \iff m = 4$$

Langkah 3: Menentukan turunan fungsi $F(x)$ menggunakan Teorema Dasar Kalkulus I.
$$F'(x) = \frac{d}{dx} \left[ \int_2^x (3t^2 - 8t + 1)\,dt \right] = 3x^2 - 8x + 1$$

Langkah 4: Menentukan nilai absis titik singgung $x = a$.
$$F'(a) = m \iff 3a^2 - 8a + 1 = 4$$
$$3a^2 - 8a - 3 = 0$$
$$(3a + 1)(a - 3) = 0$$
Diperoleh $a = -\frac{1}{3}$ atau $a = 3$.

Langkah 5: Memilih nilai yang memenuhi syarat.
Karena disyaratkan $a > 0$, maka nilai yang memenuhi adalah $a = 3$.
**Acuan:** siswa — siswa hal.206

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
