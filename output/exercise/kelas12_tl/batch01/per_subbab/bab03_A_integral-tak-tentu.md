# Lembar koreksi — kelas12_tl SMA12L-B3 subbab A: Integral Tak Tentu

58 soal | easy 20, medium 20, hard 18 | variasi 28, orisinal 30
> **Kapasitas kurang (hard): 18 dari kuota 20** — 11 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b03-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: integral aljabar suku tunggal*

Tentukan integral tak tentu dari $\int 6x^5\,dx$.

- A. $30x^4 + C$  
  <sub>Salah: Melakukan operasi turunan (diferensiasi), bukan pengintegralan.</sub>
- B. $6x^6 + C$  
  <sub>Salah: Menaikkan pangkat variabel menjadi $6$ tetapi lupa membagi koefisien dengan pangkat baru.</sub>
- **C. $x^6 + C$** ✅  
  <sub>Benar: Menggunakan aturan dasar $\int a x^n\,dx = \frac{a}{n+1}x^{n+1}+C$, sehingga diperoleh $\frac{6}{5+1}x^{5+1}+C = \frac{6}{6}x^6+C = x^6+C$.</sub>
- D. $\frac{6}{5}x^6 + C$  
  <sub>Salah: Membagi koefisien dengan pangkat lama ($5$), bukan pangkat baru ($5+1=6$).</sub>

**Pembahasan:** Berdasarkan sifat integral tak tentu:
$$\int a x^n\,dx = \frac{a}{n+1}x^{n+1} + C$$
Untuk $\int 6x^5\,dx$:
$$= \frac{6}{5+1}x^{5+1} + C = \frac{6}{6}x^6 + C = x^6 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b03-a-easy-bt01-002
*variasi (angka) | C1 | 1 langkah | jenis: integral fungsi aljabar berpangkat*

Tentukan antiturunan atau integral dari fungsi $f(x) = x^8$.

- **A. $\frac{1}{9}x^9 + C$** ✅  
  <sub>Benar: Sesuai rumus dasar integral tak tentu $\int x^n\,dx = \frac{1}{n+1}x^{n+1}+C$, untuk $n=8$ diperoleh $\frac{1}{8+1}x^{8+1}+C = \frac{1}{9}x^9+C$.</sub>
- B. $\frac{1}{9}x^8 + C$  
  <sub>Salah: Membagi dengan pangkat baru tetapi lupa menambahkan $1$ pada eksponen variabel $x$.</sub>
- C. $8x^7 + C$  
  <sub>Salah: Menghitung turunan dari fungsi, bukan integralnya.</sub>
- D. $\frac{1}{8}x^9 + C$  
  <sub>Salah: Membagi dengan nilai pangkat mula-mula ($8$), bukan dengan pangkat baru ($9$).</sub>

**Pembahasan:** Berdasarkan definisi antiturunan dan Sifat 3.2:
$$\int x^n\,dx = \frac{1}{n+1}x^{n+1} + C$$
Untuk $f(x) = x^8$:
$$\int x^8\,dx = \frac{1}{8+1}x^{8+1} + C = \frac{1}{9}x^9 + C$$
**Acuan:** siswa — siswa hal.186 Contoh Soal 3.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b03-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: integral polinomial dua suku*

Tentukan integral tak tentu dari $\int (8x^3 - 6x)\,dx$.

- **A. $2x^4 - 3x^2 + C$** ✅  
  <sub>Benar: Mengintegralkan setiap suku: $\int 8x^3\,dx = \frac{8}{4}x^4 = 2x^4$ dan $\int 6x\,dx = \frac{6}{2}x^2 = 3x^2$, sehingga diperoleh $2x^4 - 3x^2 + C$.</sub>
- B. $8x^4 - 6x^2 + C$  
  <sub>Salah: Menaikkan pangkat masing-masing variabel tanpa membagi dengan nilai pangkat baru.</sub>
- C. $24x^2 - 6 + C$  
  <sub>Salah: Melakukan proses diferensiasi terhadap fungsi yang diberikan.</sub>
- D. $2x^4 - 6x^2 + C$  
  <sub>Salah: Lupa membagi koefisien suku kedua ($6$) dengan pangkat barunya ($2$).</sub>

**Pembahasan:** Gunakan sifat kelinieran integral tak tentu:
$$\int (8x^3 - 6x)\,dx = \int 8x^3\,dx - \int 6x\,dx$$
$$= \frac{8}{3+1}x^{3+1} - \frac{6}{1+1}x^{1+1} + C$$
$$= \frac{8}{4}x^4 - \frac{6}{2}x^2 + C = 2x^4 - 3x^2 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b03-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: integral fungsi trigonometri dasar*

Hasil dari $\int 7\cos x\,dx$ adalah ....

- A. $-7\sin x + C$  
  <sub>Salah: Tertukar tanda dengan hasil integral $\sin x$ atau turunan dari $\cos x$.</sub>
- B. $-7\cos x + C$  
  <sub>Salah: Mengubah fungsi secara keliru disertai kesalahan penetapan tanda minus.</sub>
- C. $7\cos x + C$  
  <sub>Salah: Mengabaikan perubahan fungsi trigonometri pada saat pengintegralan.</sub>
- **D. $7\sin x + C$** ✅  
  <sub>Benar: Konstanta dapat dikeluarkan: $\int 7\cos x\,dx = 7\int \cos x\,dx$. Berdasarkan Sifat 3.8, $\int \cos x\,dx = \sin x + C$, sehingga hasilnya $7\sin x + C$.</sub>

**Pembahasan:** Berdasarkan Sifat 3.8 Aturan Integral Trigonometri:
$$\int \cos x\,dx = \sin x + C$$
Dengan mengeluarkan faktor konstanta:
$$\int 7\cos x\,dx = 7\int \cos x\,dx = 7\sin x + C$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b03-a-easy-bt01-005
*orisinal | C1 | 1 langkah | jenis: integral fungsi konstanta*

Hasil dari integral tak tentu $\int 9\,dx$ adalah ....

- A. $9 + C$  
  <sub>Salah: Hanya menambahkan konstanta integrasi tanpa memunculkan variabel $x$.</sub>
- B. $\frac{9}{2}x^2 + C$  
  <sub>Salah: Menganggap integrand sebagai fungsi $9x$ berpangkat 1.</sub>
- **C. $9x + C$** ✅  
  <sub>Benar: Berdasarkan Sifat 3.1 dan perkalian skalar, $\int k\,dx = kx + C$, sehingga untuk $k=9$ diperoleh $9x + C$.</sub>
- D. $0$  
  <sub>Salah: Mengira integral dari konstanta bernilai nol seperti pada proses turunan.</sub>

**Pembahasan:** Berdasarkan sifat pengintegralan fungsi konstan:
$$\int k\,dx = k \int dx = kx + C$$
Untuk $k = 9$:
$$\int 9\,dx = 9x + C$$
**Acuan:** siswa — siswa hal.183

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b03-a-easy-bt01-006
*variasi (angka) | C2 | 1 langkah | jenis: integral aljabar koefisien bulat*

Tentukan integral tak tentu berikut.
$$\int 12x^2\,dx$$

- A. $24x + C$  
  <sub>Salah: Melakukan proses turunan (diferensiasi), bukan pengintegralan.</sub>
- B. $6x^3 + C$  
  <sub>Salah: Membagi koefisien 12 dengan pangkat lama (2), bukan pangkat baru (3).</sub>
- **C. $4x^3 + C$** ✅  
  <sub>Benar: $$\int 12x^2\,dx = \frac{12}{2 + 1}x^{2 + 1} + C = \frac{12}{3}x^3 + C = 4x^3 + C$$</sub>
- D. $4x^2 + C$  
  <sub>Salah: Membagi koefisien dengan 3 tetapi lupa menambah eksponen $x$ dengan 1.</sub>

**Pembahasan:** Berdasarkan aturan integral fungsi aljabar $\int a x^n\,dx = \frac{a}{n+1}x^{n+1} + C$ untuk $n \neq -1$:
$$\int 12x^2\,dx = \frac{12}{2+1}x^{2+1} + C = \frac{12}{3}x^3 + C = 4x^3 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b03-a-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: integral aljabar pecahan*

Tentukan integral dari $f(x) = x^7$.

- A. $7x^6 + C$  
  <sub>Salah: Menurunkan fungsi (turunan) alih-alih mencari antiturunan/integral.</sub>
- B. $\frac{1}{7}x^8 + C$  
  <sub>Salah: Membagi dengan eksponen lama bukan eksponen baru.</sub>
- **C. $\frac{1}{8}x^8 + C$** ✅  
  <sub>Benar: $$\int x^7\,dx = \frac{1}{7+1}x^{7+1} + C = \frac{1}{8}x^8 + C$$</sub>
- D. $\frac{1}{8}x^7 + C$  
  <sub>Salah: Membagi koefisien dengan 8 tetapi pangkat tidak ditambah 1.</sub>

**Pembahasan:** Gunakan aturan pangkat integral tak tentu $\int x^n\,dx = \frac{1}{n+1}x^{n+1} + C$:
$$\int x^7\,dx = \frac{1}{7+1}x^{7+1} + C = \frac{1}{8}x^8 + C$$
**Acuan:** siswa — siswa hal.186 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b03-a-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: integral trigonometri secan kuadrat*

Hasil dari $\int 5\sec^2 x\,dx$ adalah ....

- A. $\frac{5}{3}\sec^3 x + C$  
  <sub>Salah: Menggunakan aturan fungsi pangkat aljabar secara keliru pada fungsi trigonometri.</sub>
- **B. $5\tan x + C$** ✅  
  <sub>Benar: Berdasarkan aturan dasar $\int \sec^2 x\,dx = \tan x + C$, maka $\int 5\sec^2 x\,dx = 5\tan x + C$.</sub>
- C. $5\cot x + C$  
  <sub>Salah: Tertukar dengan antiturunan dari $\csc^2 x$.</sub>
- D. $-5\tan x + C$  
  <sub>Salah: Tertukar dengan tanda negatif pada integral fungsi sinus.</sub>

**Pembahasan:** Mengacu pada Sifat 3.8 (Aturan Integral Trigonometri), $\int \sec^2 x\,dx = \tan x + C$.
Dengan mengeluarkan konstanta skalar 5 dari integral:
$$\int 5\sec^2 x\,dx = 5\int \sec^2 x\,dx = 5\tan x + C$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b03-a-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: konsep antiturunan*

Berdasarkan definisi integral tak tentu, jika $F(x)$ merupakan antiturunan dari $f(x)$ untuk setiap $x$ pada suatu interval, maka hubungan turunan $F'(x)$ dengan $f(x)$ adalah ....

- A. $F'(x) = \int f(x)\,dx$  
  <sub>Salah: Tertukar antara proses penurunan dan pengintegralan.</sub>
- B. $F'(x) = f'(x)$  
  <sub>Salah: Menganggap turunan antiturunan sama dengan turunan fungsi asal.</sub>
- C. $F'(x) = -f(x)$  
  <sub>Salah: Menambahkan tanda negatif akibat kerancuan tanda pada aturan kalkulus.</sub>
- **D. $F'(x) = f(x)$** ✅  
  <sub>Benar: Menurut definisi, pengintegralan merupakan kebalikan turunan sehingga turunan dari antiturunan $F(x)$ mengembalikan fungsi mula-mula $f(x)$.</sub>

**Pembahasan:** Berdasarkan Definisi 3.1 pada Buku Siswa halaman 182, antiturunan atau integral dari $f(x)$ merupakan fungsi $F(x) + C$ sedemikian sehingga $\frac{d}{dx}[F(x) + C] = f(x)$. Karena turunan dari konstanta $C$ adalah nol, maka $\frac{d}{dx}[F(x)] = F'(x) = f(x)$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b03-a-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: integral suku banyak pengurangan*

Tentukan integral tak tentu berikut.
$$\int (9x^8 - 4x^7)\,dx$$

- **A. $x^9 - \frac{1}{2}x^8 + C$** ✅  
  <sub>Benar: Mengintegralkan tiap suku: $\int 9x^8\,dx = \frac{9}{9}x^9 = x^9$ dan $\int 4x^7\,dx = \frac{4}{8}x^8 = \frac{1}{2}x^8$, sehingga hasilnya $x^9 - \frac{1}{2}x^8 + C$.</sub>
- B. $9x^9 - 4x^8 + C$  
  <sub>Salah: Lupa membagi koefisien dengan pangkat baru setelah diintegralkan.</sub>
- C. $x^9 - \frac{1}{4}x^8 + C$  
  <sub>Salah: Salah menyederhanakan pecahan 4/8 menjadi 1/4.</sub>
- D. $72x^7 - 28x^6 + C$  
  <sub>Salah: Melakukan proses turunan (diferensiasi), bukan pengintegralan.</sub>

**Pembahasan:** Gunakan aturan integral fungsi aljabar $\int x^n\,dx = \frac{1}{n+1}x^{n+1} + C$ pada masing-masing suku:
$$\int (9x^8 - 4x^7)\,dx = \frac{9}{8+1}x^{8+1} - \frac{4}{7+1}x^{7+1} + C = x^9 - \frac{4}{8}x^8 + C = x^9 - \frac{1}{2}x^8 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b03-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: integral substitusi aljabar dasar*

Tentukan hasil dari $\int x(x^2 + 5)^3\,dx$ dengan menggunakan teknik substitusi.

- **A. $\frac{1}{8}(x^2 + 5)^4 + C$** ✅  
  <sub>Benar: Dengan memisalkan $u = x^2 + 5$, diperoleh $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,du$. Integral menjadi $\frac{1}{2} \int u^3\,du = \frac{1}{2} \cdot \frac{1}{4}u^4 + C = \frac{1}{8}(x^2+5)^4 + C$.</sub>
- B. $\frac{1}{6}(x^2 + 5)^4 + C$  
  <sub>Salah: Keliru mengalikan penyebut 2 dengan 3 (pangkat lama) bukannya 4 (pangkat baru).</sub>
- C. $\frac{1}{2}(x^2 + 5)^4 + C$  
  <sub>Salah: Lupa membagi dengan pangkat baru 4 saat mengintegralkan u^3.</sub>
- D. $\frac{1}{4}(x^2 + 5)^4 + C$  
  <sub>Salah: Lupa mengalikan dengan faktor 1/2 yang berasal dari diferensial du = 2x dx.</sub>

**Pembahasan:** Misalkan $u = x^2 + 5$, maka $\frac{du}{dx} = 2x \implies x\,dx = \frac{1}{2}\,du$.
Substitusikan ke dalam integral:
$$\int x(x^2 + 5)^3\,dx = \int u^3 \left(\frac{1}{2}\,du\right) = \frac{1}{2} \int u^3\,du = \frac{1}{2} \left(\frac{1}{4}u^4\right) + C = \frac{1}{8}(x^2 + 5)^4 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b03-a-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: integral substitusi koefisien kelipatan*

Tentukan hasil dari integral tak tentu berikut.
$$\int 8x(x^2 - 7)^3\,dx$$

- A. $4(x^2 - 7)^4 + C$  
  <sub>Salah: Lupa membagi koefisien 4 dengan pangkat baru 4 setelah pengintegralan.</sub>
- **B. $(x^2 - 7)^4 + C$** ✅  
  <sub>Benar: Substitusi $u = x^2 - 7$ menghasilkan $du = 2x\,dx$, sehingga $8x\,dx = 4\,du$. Integral menjadi $\int 4u^3\,du = u^4 + C = (x^2 - 7)^4 + C$.</sub>
- C. $\frac{1}{4}(x^2 - 7)^4 + C$  
  <sub>Salah: Salah memperlakukan koefisien luar 8x terhadap turunan 2x sehingga menghasilkan faktor pecahan keliru.</sub>
- D. $2(x^2 - 7)^4 + C$  
  <sub>Salah: Keliru membagi 8 dengan 4 langsung tanpa mengintegralkan bentuk pangkat.</sub>

**Pembahasan:** Misalkan $u = x^2 - 7$, maka $du = 2x\,dx$.
Bentuk $8x\,dx$ dapat ditulis sebagai $4(2x\,dx) = 4\,du$.
Maka:
$$\int 8x(x^2 - 7)^3\,dx = \int 4u^3\,du = 4 \cdot \frac{1}{4}u^4 + C = u^4 + C = (x^2 - 7)^4 + C$$
**Acuan:** siswa — siswa hal.188 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b03-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: integral trigonometri sinus bertanda*

Hasil dari integral tak tentu $\int -6\sin x\,dx$ adalah ....

- A. $-6\sin x + C$  
  <sub>Salah: Mengabaikan perubahan fungsi trigonometri pada saat proses pengintegralan.</sub>
- B. $-6\cos x + C$  
  <sub>Salah: Lupa bahwa integral dari sin x menghasilkan tanda negatif (-cos x), sehingga tanda negatif awal tidak hilang.</sub>
- C. $6\sin x + C$  
  <sub>Salah: Keliru menganggap antiturunan sin x tetap berupa sin x.</sub>
- **D. $6\cos x + C$** ✅  
  <sub>Benar: Karena $\int \sin x\,dx = -\cos x + C$, maka $-6 \int \sin x\,dx = -6(-\cos x) + C = 6\cos x + C$.</sub>

**Pembahasan:** Berdasarkan aturan dasar integral trigonometri:
$$\int \sin x\,dx = -\cos x + C$$
Dengan mengeluarkan faktor pengali konstanta $-6$:
$$\int -6\sin x\,dx = -6 \int \sin x\,dx = -6(-\cos x) + C = 6\cos x + C$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b03-a-easy-bt01-014
*orisinal | C2 | 2 langkah | jenis: aplikasi integral menentukan kecepatan*

Sebuah partikel bergerak sepanjang garis lurus dengan percepatan konstan $a(t) = 6\text{ m/s}^2$. Jika kecepatan awal partikel pada saat $t = 0$ detik adalah $v(0) = 4\text{ m/s}$, persamaan kecepatan partikel $v(t)$ adalah ....

- A. $v(t) = 6t$  
  <sub>Salah: Lupa memperhitungkan nilai kecepatan awal v(0) sebagai konstanta integrasi C.</sub>
- **B. $v(t) = 6t + 4$** ✅  
  <sub>Benar: $v(t) = \int 6\,dt = 6t + C$. Dari syarat $v(0) = 4$, didapat $6(0) + C = 4 \implies C = 4$, sehingga $v(t) = 6t + 4$.</sub>
- C. $v(t) = 3t^2 + 4$  
  <sub>Salah: Keliru mengintegralkan percepatan konstan 6 seolah-olah bernilai 6t.</sub>
- D. $v(t) = 6t - 4$  
  <sub>Salah: Salah menentukan tanda konstanta integrasi dari nilai awal.</sub>

**Pembahasan:** Kecepatan merupakan antiturunan dari percepatan:
$$v(t) = \int a(t)\,dt = \int 6\,dt = 6t + C$$
Diketahui kecepatan awal $v(0) = 4$:
$$v(0) = 6(0) + C = 4 \implies C = 4$$
Substitusikan kembali nilai $C$:
$$v(t) = 6t + 4$$
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b03-a-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: integral substitusi pangkat tinggi*

Tentukan hasil dari $\int x(x^2 - 4)^5\,dx$ dengan menggunakan teknik substitusi.

- A. $\frac{1}{24}(x^2 - 4)^6 + C$  
  <sub>Salah: Secara keliru membagi koefisien dengan 4 bukannya 2.</sub>
- B. $\frac{1}{10}(x^2 - 4)^5 + C$  
  <sub>Salah: Lupa menambahkan 1 pada pangkat ketika melakukan integrasi.</sub>
- **C. $\frac{1}{12}(x^2 - 4)^6 + C$** ✅  
  <sub>Benar: Misalkan $u = x^2 - 4$, sehingga $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,du$. Maka integral menjadi $\int \frac{1}{2}u^5\,du = \frac{1}{12}u^6 + C = \frac{1}{12}(x^2 - 4)^6 + C$.</sub>
- D. $\frac{1}{6}(x^2 - 4)^6 + C$  
  <sub>Salah: Lupa membagi dengan faktor 2 dari turunan variabel substitusi.</sub>

**Pembahasan:** Misalkan $u = x^2 - 4$, maka turunan pertamanya adalah:
$$\frac{du}{dx} = 2x \implies x\,dx = \frac{1}{2}\,du$$
Substitusikan ke dalam bentuk integral:
$$\int x(x^2 - 4)^5\,dx = \int u^5 \left(\frac{1}{2}\,du\right) = \frac{1}{2} \left(\frac{1}{6}u^6\right) + C = \frac{1}{12}(x^2 - 4)^6 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b03-a-easy-bt01-016
*variasi (angka) | C2 | 2 langkah | jenis: integral substitusi koefisien dua*

Tentukan hasil dari integral tak tentu berikut.
$$\int 2x(x^2 + 3)^6\,dx$$

- A. $\frac{2}{7}(x^2 + 3)^7 + C$  
  <sub>Salah: Koefisien 2 tidak dieliminasi bersama $x\,dx$ oleh diferensial $du$.</sub>
- **B. $\frac{1}{7}(x^2 + 3)^7 + C$** ✅  
  <sub>Benar: Dengan memisalkan $u = x^2 + 3$, didapat $du = 2x\,dx$. Bentuk integral langsung menjadi $\int u^6\,du = \frac{1}{7}u^7 + C = \frac{1}{7}(x^2 + 3)^7 + C$.</sub>
- C. $\frac{1}{6}(x^2 + 3)^6 + C$  
  <sub>Salah: Lupa menaikkan nilai pangkat saat proses integrasi.</sub>
- D. $\frac{1}{14}(x^2 + 3)^7 + C$  
  <sub>Salah: Membagi kembali integral dengan turunan dalam 2 padahal faktor $2x\,dx$ sudah utuh menjadi $du$.</sub>

**Pembahasan:** Misalkan $g(x) = x^2 + 3$, maka:
$$g'(x)\,dx = 2x\,dx$$
Sehingga:
$$\int 2x(x^2 + 3)^6\,dx = \int [g(x)]^6 g'(x)\,dx = \frac{1}{6+1}[g(x)]^{6+1} + C = \frac{1}{7}(x^2 + 3)^7 + C$$
**Acuan:** siswa — siswa hal.188 Contoh Soal 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b03-a-easy-bt01-017
*orisinal | C2 | 2 langkah | jenis: aplikasi integral menentukan posisi*

Sebuah benda bergerak pada garis lurus dengan kecepatan $v(t) = 4t + 3$ (dalam m/s). Jika posisi awal benda pada saat $t = 0$ detik adalah $s(0) = 5$ meter, persamaan posisi $s(t)$ benda tersebut adalah ....

- A. $s(t) = 2t^2 + 3t - 5$  
  <sub>Salah: Salah tanda pada konstanta integrasi.</sub>
- **B. $s(t) = 2t^2 + 3t + 5$** ✅  
  <sub>Benar: $s(t) = \int (4t + 3)\,dt = 2t^2 + 3t + C$. Dari nilai awal $s(0) = 5$, didapat $C = 5$, sehingga $s(t) = 2t^2 + 3t + 5$.</sub>
- C. $s(t) = 4t^2 + 3t + 5$  
  <sub>Salah: Lupa membagi koefisien suku pertama dengan pangkat baru.</sub>
- D. $s(t) = 2t^2 + 3t$  
  <sub>Salah: Mengabaikan konstanta integrasi dari syarat posisi awal.</sub>

**Pembahasan:** Posisi $s(t)$ diperoleh dari integral kecepatan:
$$s(t) = \int v(t)\,dt = \int (4t + 3)\,dt = 2t^2 + 3t + C$$
Diketahui $s(0) = 5$:
$$s(0) = 2(0)^2 + 3(0) + C = 5 \implies C = 5$$
Jadi, fungsi posisinya adalah $s(t) = 2t^2 + 3t + 5$.
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b03-a-easy-bt01-018
*orisinal | C2 | 2 langkah | jenis: integral penjumlahan trigonometri*

Tentukan hasil dari integral tak tentu berikut.
$$\int (4\cos x + 3\sin x)\,dx$$

- A. $-4\sin x + 3\cos x + C$  
  <sub>Salah: Tertukar tanda negatif pada integral sinus dan kosinus.</sub>
- B. $4\sin x + 3\cos x + C$  
  <sub>Salah: Salah mengira bahwa integral dari $\sin x$ adalah $\cos x$ bertanda positif.</sub>
- C. $4\cos x - 3\sin x + C$  
  <sub>Salah: Tidak mengubah fungsi trigonometri saat melakukan integrasi.</sub>
- **D. $4\sin x - 3\cos x + C$** ✅  
  <sub>Benar: $\int 4\cos x\,dx = 4\sin x$ dan $\int 3\sin x\,dx = -3\cos x$, sehingga hasil penjumlahannya adalah $4\sin x - 3\cos x + C$.</sub>

**Pembahasan:** Berdasarkan sifat kelinearan integral dan aturan integral trigonometri:
$$\int (4\cos x + 3\sin x)\,dx = 4 \int \cos x\,dx + 3 \int \sin x\,dx$$
Karena $\int \cos x\,dx = \sin x$ dan $\int \sin x\,dx = -\cos x$:
$$= 4\sin x + 3(-\cos x) + C = 4\sin x - 3\cos x + C$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b03-a-easy-bt01-019
*variasi (angka) | C2 | 2 langkah | jenis: integral substitusi aljabar berpangkat*

Tentukan hasil dari integral tak tentu berikut.
$$\int x(6x^2 + 5)^4\,dx$$

- **A. $\frac{1}{60}(6x^2 + 5)^5 + C$** ✅  
  <sub>Benar: Menggunakan substitusi $u = 6x^2 + 5$ menghasilkan $du = 12x\,dx$ atau $x\,dx = \frac{1}{12}\,du$, sehingga $\int u^4 \cdot \frac{1}{12}\,du = \frac{1}{60}u^5 + C = \frac{1}{60}(6x^2 + 5)^5 + C$.</sub>
- B. $\frac{1}{30}(6x^2 + 5)^5 + C$  
  <sub>Salah: Salah menghitung turunan $6x^2$ menjadi $6x$ alih-alih $12x$, sehingga pembaginya $6 \times 5 = 30$.</sub>
- C. $\frac{1}{12}(6x^2 + 5)^5 + C$  
  <sub>Salah: Hanya membagi dengan turunan fungsi dalam tanpa membagi dengan pangkat baru 5.</sub>
- D. $\frac{1}{5}(6x^2 + 5)^5 + C$  
  <sub>Salah: Hanya mengintegralkan pangkat luar tanpa mengalikan dengan faktor turunan fungsi dalam (1/12).</sub>

**Pembahasan:** Misalkan $u = 6x^2 + 5$.
Maka turunan dari $u$ adalah:
$$\frac{du}{dx} = 12x \implies x\,dx = \frac{1}{12}\,du$$
Substitusikan ke bentuk integral:
$$\int x(6x^2 + 5)^4\,dx = \int u^4 \left(\frac{1}{12}\,du\right) = \frac{1}{12} \int u^4\,du$$
$$= \frac{1}{12} \cdot \frac{1}{5} u^5 + C = \frac{1}{60}(6x^2 + 5)^5 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b03-a-easy-bt01-020
*variasi (konteks) | C2 | 1 langkah | jenis: integral fungsi eksponensial bertanda*

Laju peluruhan intensitas berkas radiasi terhadap ketebalan bahan $y$ dinyatakan oleh $f(y) = -e^{-y}$. Bentuk umum dari fungsi intensitas radiasi $F(y) = \int f(y)\,dy$ adalah ....

- A. $-e^{-y} + C$  
  <sub>Salah: Lupa membagi dengan koefisien pangkat $(-1)$ sehingga tanda negatif di depan fungsi tidak berubah.</sub>
- B. $-e^y + C$  
  <sub>Salah: Mengubah pangkat menjadi positif sekaligus mempertahankan tanda negatif pada koefisien.</sub>
- C. $e^y + C$  
  <sub>Salah: Keliru menghilangkan tanda negatif pada eksponen variabel $y$.</sub>
- **D. $e^{-y} + C$** ✅  
  <sub>Benar: Integral dari $e^{ky}\,dy$ adalah $\frac{1}{k}e^{ky} + C$. Dengan $k = -1$ dan koefisien $-1$, diperoleh $(-1) \cdot \frac{1}{-1}e^{-y} + C = e^{-y} + C$.</sub>

**Pembahasan:** Diberikan $f(y) = -e^{-y}$.
Maka fungsi antiturunannya adalah:
$$F(y) = \int -e^{-y}\,dy = -\int e^{-y}\,dy$$
Karena $\int e^{-y}\,dy = -e^{-y} + C$, maka:
$$F(y) = -(-e^{-y}) + C = e^{-y} + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b03-a-medium-bt01-001
*orisinal | C3 | 2 langkah | jenis: integral trigonometri*

Hasil dari $\int \tan^2 x\,dx$ adalah ....

- A. $\tan x - 1 + C$  
  <sub>Salah: Lupa mengintegralkan konstanta $1$ terhadap variabel $x$.</sub>
- **B. $\tan x - x + C$** ✅  
  <sub>Benar: Menggunakan identitas $\tan^2 x = \sec^2 x - 1$, sehingga $\int (\sec^2 x - 1)\,dx = \tan x - x + C$.</sub>
- C. $x - \tan x + C$  
  <sub>Salah: Salah menggunakan tanda pada identitas trigonometri menjadi $\tan^2 x = 1 - \sec^2 x$.</sub>
- D. $\frac{1}{3}\tan^3 x + C$  
  <sub>Salah: Menerapkan aturan pangkat secara keliru langsung pada fungsi trigonometri tanpa substitusi.</sub>

**Pembahasan:** Gunakan identitas trigonometri dasar:
$$\tan^2 x = \sec^2 x - 1$$

Substitusikan ke bentuk integral:
$$\int \tan^2 x\,dx = \int (\sec^2 x - 1)\,dx$$

Pisahkan berdasarkan sifat integral tak tentu:
$$= \int \sec^2 x\,dx - \int 1\,dx$$

Berdasarkan Sifat 3.8 Aturan Integral Trigonometri:
$$= \tan x - x + C$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b03-a-medium-bt01-002
*orisinal | C4 | 3 langkah | jenis: kinematika gerak*

Sebuah partikel bergerak di sepanjang garis lurus dengan percepatan $a(t) = 6t - 4\text{ m/s}^2$. Partikel tersebut mula-mula diam pada saat $t = 0$ detik dengan posisi awal berada pada jarak $4\text{ meter}$ di sebelah kanan titik acuan. Posisi partikel pada saat $t = 3$ detik adalah ....

- **A. $13\text{ meter}$** ✅  
  <sub>Benar: Integrasi percepatan menghasilkan $v(t) = 3t^2 - 4t$ (karena $v(0)=0$). Integrasi kecepatan menghasilkan $s(t) = t^3 - 2t^2 + 4$ (karena $s(0)=4$). Pada $t = 3$, $s(3) = 27 - 18 + 4 = 13\text{ meter}$.</sub>
- B. $15\text{ meter}$  
  <sub>Salah: Hanya menghitung nilai kecepatan partikel pada saat $t = 3$ detik ($v(3) = 3(9) - 4(3) = 15$) bukan posisinya.</sub>
- C. $9\text{ meter}$  
  <sub>Salah: Mengabaikan posisi awal $s(0) = 4\text{ meter}$ sehingga konstanta $C_2$ dianggap bernilai nol.</sub>
- D. $49\text{ meter}$  
  <sub>Salah: Salah melakukan integrasi pada kecepatan dengan tidak membagi koefisien terhadap pangkat baru ($s(t) = 3t^3 - 4t^2 + 4$).</sub>

**Pembahasan:** 1. Menentukan fungsi kecepatan $v(t)$:
$$v(t) = \int a(t)\,dt = \int (6t - 4)\,dt = 3t^2 - 4t + C_1$$
Karena benda mula-mula diam ($v(0) = 0$):
$$v(0) = 0 \implies 3(0)^2 - 4(0) + C_1 = 0 \implies C_1 = 0$$
Sehingga, $v(t) = 3t^2 - 4t$.

2. Menentukan fungsi posisi $s(t)$:
$$s(t) = \int v(t)\,dt = \int (3t^2 - 4t)\,dt = t^3 - 2t^2 + C_2$$
Karena posisi awal $s(0) = 4\text{ meter}$:
$$s(0) = 4 \implies (0)^3 - 2(0)^2 + C_2 = 4 \implies C_2 = 4$$
Sehingga, $s(t) = t^3 - 2t^2 + 4$.

3. Menghitung posisi pada saat $t = 3$ detik:
$$s(3) = (3)^3 - 2(3)^2 + 4 = 27 - 18 + 4 = 13\text{ meter}$$
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b03-a-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: integral parsial*

Tentukan hasil dari integral tak tentu berikut.
$$\int (2x - 3)\cos x\,dx$$

- **A. $(2x - 3)\sin x + 2\cos x + C$** ✅  
  <sub>Benar: Menggunakan integral parsial dengan $u = 2x - 3$ dan $dv = \cos x\,dx$, sehingga diperoleh $(2x - 3)\sin x - \int 2\sin x\,dx = (2x - 3)\sin x + 2\cos x + C$.</sub>
- B. $(2x - 3)\sin x + \cos x + C$  
  <sub>Salah: Lupa mengalikan diferensial $du = 2\,dx$ ke dalam integral suku kedua.</sub>
- C. $-(2x - 3)\sin x - 2\cos x + C$  
  <sub>Salah: Keliru menentukan antiturunan dari $\cos x$ menjadi $-\sin x$.</sub>
- D. $(2x - 3)\sin x - 2\cos x + C$  
  <sub>Salah: Salah tanda pada integrasi suku kedua (menganggap $\int \sin x\,dx = \cos x$).</sub>

**Pembahasan:** Gunakan aturan integrasi parsial: $\int u\,dv = uv - \int v\,du$.

1. Tetapkan bagian $u$ dan $dv$:
- $u = 2x - 3 \implies du = 2\,dx$
- $dv = \cos x\,dx \implies v = \int \cos x\,dx = \sin x$

2. Terapkan rumus integrasi parsial:
$$\int (2x - 3)\cos x\,dx = (2x - 3)\sin x - \int \sin x (2\,dx)$$
$$= (2x - 3)\sin x - 2\int \sin x\,dx$$

3. Selesaikan integral yang tersisa:
Karena $\int \sin x\,dx = -\cos x + C$, maka:
$$= (2x - 3)\sin x - 2(-\cos x) + C$$
$$= (2x - 3)\sin x + 2\cos x + C$$
**Acuan:** siswa — siswa hal.191

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b03-a-medium-bt01-004
*variasi (angka) | C3 | 2 langkah | jenis: integral bentuk akar*

Tentukan hasil dari integral tak tentu berikut.
$$\int \sqrt{7x - 2}\,dx$$

- **A. $\frac{2}{21}(7x - 2)\sqrt{7x - 2} + C$** ✅  
  <sub>Benar: Menggunakan substitusi $u = 7x - 2$, diperoleh $dx = \frac{du}{7}$. Maka $\int u^{\frac{1}{2}} \frac{du}{7} = \frac{1}{7} \cdot \frac{2}{3} u^{\frac{3}{2}} + C = \frac{2}{21}(7x - 2)\sqrt{7x - 2} + C$.</sub>
- B. $\frac{3}{14}(7x - 2)\sqrt{7x - 2} + C$  
  <sub>Salah: Siswa keliru membalik pecahan pangkat saat mengintegralkan ($u^{\frac{3}{2}}$ dibagi $\frac{2}{3}$, bukan dikali $\frac{2}{3}$).</sub>
- C. $\frac{14}{3}(7x - 2)\sqrt{7x - 2} + C$  
  <sub>Salah: Siswa mengalikan dengan turunan fungsi dalam alih-alih membaginya.</sub>
- D. $\frac{2}{3}(7x - 2)\sqrt{7x - 2} + C$  
  <sub>Salah: Siswa lupa membagi dengan turunan dari fungsi dalam (faktor $\frac{1}{7}$ terlewat).</sub>

**Pembahasan:** Misalkan $u = 7x - 2$, maka $\frac{du}{dx} = 7 \implies dx = \frac{du}{7}$.
Substitusikan ke dalam integral:
$$\int \sqrt{7x - 2}\,dx = \int u^{\frac{1}{2}} \cdot \frac{du}{7} = \frac{1}{7} \int u^{\frac{1}{2}}\,du$$
$$= \frac{1}{7} \left( \frac{1}{\frac{1}{2} + 1} u^{\frac{1}{2} + 1} \right) + C = \frac{1}{7} \left( \frac{2}{3} u^{\frac{3}{2}} \right) + C = \frac{2}{21} u^{\frac{3}{2}} + C$$
Kembalikan ke variabel $x$:
$$= \frac{2}{21} (7x - 2)^{\frac{3}{2}} + C = \frac{2}{21}(7x - 2)\sqrt{7x - 2} + C$$
**Acuan:** siswa — siswa hal.189 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b03-a-medium-bt01-005
*variasi (angka) | C3 | 2 langkah | jenis: integral substitusi aljabar*

Tentukan hasil dari $\int x(3x^2 + 4)^3\,dx$ dengan menggunakan teknik substitusi.

- **A. $\frac{1}{24}(3x^2 + 4)^4 + C$** ✅  
  <sub>Benar: Dengan memisalkan $u = 3x^2 + 4$, maka $du = 6x\,dx$ sehingga $x\,dx = \frac{du}{6}$. Integral menjadi $\int \frac{1}{6}u^3\,du = \frac{u^4}{24} + C = \frac{1}{24}(3x^2 + 4)^4 + C$.</sub>
- B. $\frac{1}{12}(3x^2 + 4)^4 + C$  
  <sub>Salah: Siswa salah menurunkan $3x^2$ menjadi $3x$ (bukan $6x$), sehingga hanya membagi dengan 3.</sub>
- C. $\frac{1}{4}(3x^2 + 4)^4 + C$  
  <sub>Salah: Siswa lupa memperhitungkan faktor diferensial $\frac{1}{6}$ yang dihasilkan dari turunan fungsi dalam.</sub>
- D. $\frac{1}{18}(3x^2 + 4)^3 + C$  
  <sub>Salah: Siswa lupa menambahkan 1 pada pangkat bentuk aljabar setelah proses pengintegralan.</sub>

**Pembahasan:** Gunakan aturan integrasi substitusi.
Misalkan $u = 3x^2 + 4$.
Turunan dari $u$ adalah:
$$du = 6x\,dx \implies x\,dx = \frac{du}{6}$$
Substitusikan ke integral semula:
$$\int x(3x^2 + 4)^3\,dx = \int u^3 \cdot \frac{du}{6} = \frac{1}{6} \int u^3\,du$$
$$= \frac{1}{6} \left( \frac{1}{4} u^4 \right) + C = \frac{1}{24} u^4 + C$$
Kembalikan nilai $u$:
$$= \frac{1}{24}(3x^2 + 4)^4 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b03-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: integral substitusi pangkat*

Tentukan hasil dari integral tak tentu berikut.
$$\int x(8x^2 - 1)^6\,dx$$

- A. $\frac{1}{96}(8x^2 - 1)^7 + C$  
  <sub>Salah: Siswa melakukan kesalahan aritmetika saat mengalikan penyebut $16 \times 7 = 96$ (seharusnya 112).</sub>
- **B. $\frac{1}{112}(8x^2 - 1)^7 + C$** ✅  
  <sub>Benar: Misalkan $u = 8x^2 - 1$, maka $du = 16x\,dx$ atau $x\,dx = \frac{du}{16}$. Hasil integralnya adalah $\frac{1}{16} \cdot \frac{1}{7} u^7 + C = \frac{1}{112}(8x^2 - 1)^7 + C$.</sub>
- C. $\frac{1}{56}(8x^2 - 1)^7 + C$  
  <sub>Salah: Siswa keliru menganggap turunan dari $8x^2$ adalah $8x$ sehingga membagi dengan 8, bukan 16.</sub>
- D. $\frac{1}{7}(8x^2 - 1)^7 + C$  
  <sub>Salah: Siswa mengabaikan faktor konstanta $\frac{1}{16}$ dari hasil turunan fungsi dalam.</sub>

**Pembahasan:** Misalkan $u = 8x^2 - 1$.
Maka $\frac{du}{dx} = 16x \implies x\,dx = \frac{du}{16}$.
Substitusi ke bentuk integral:
$$\int x(8x^2 - 1)^6\,dx = \int u^6 \cdot \frac{du}{16} = \frac{1}{16} \int u^6\,du$$
$$= \frac{1}{16} \left( \frac{1}{7} u^7 \right) + C = \frac{1}{112} u^7 + C$$
Substitusikan kembali nilai $u$:
$$= \frac{1}{112}(8x^2 - 1)^7 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b03-a-medium-bt01-007
*orisinal | C3 | 3 langkah | jenis: persamaan kurva*

Gradien garis singgung suatu kurva $y = f(x)$ pada sembarang titik $(x, y)$ ditentukan oleh $f'(x) = 6x^2 - 4x + 1$. Jika kurva tersebut melalui titik $(1, 5)$, rumus fungsi kurva $f(x)$ adalah ....

- A. $f(x) = 2x^3 - 2x^2 + 5$  
  <sub>Salah: Siswa lupa mengintegralkan suku konstanta 1 menjadi $x$.</sub>
- B. $f(x) = 2x^3 - 2x^2 + x + 5$  
  <sub>Salah: Siswa langsung memasukkan ordinat titik yang dilalui sebagai konstanta $C = 5$ tanpa menghitung nilai $f(1)$.</sub>
- C. $f(x) = 2x^3 + 2x^2 + x$  
  <sub>Salah: Siswa salah tanda saat mengintegralkan $-4x$ menjadi $+2x^2$ dan salah menghitung konstanta $C$.</sub>
- **D. $f(x) = 2x^3 - 2x^2 + x + 4$** ✅  
  <sub>Benar: Integral dari $6x^2 - 4x + 1$ adalah $2x^3 - 2x^2 + x + C$. Nilai $f(1) = 5 \implies 2(1)^3 - 2(1)^2 + 1 + C = 5 \implies 1 + C = 5 \implies C = 4$. Jadi, $f(x) = 2x^3 - 2x^2 + x + 4$.</sub>

**Pembahasan:** Langkah 1: Menentukan antiturunan umum dari $f'(x)$:
$$f(x) = \int (6x^2 - 4x + 1)\,dx = \frac{6}{3}x^3 - \frac{4}{2}x^2 + x + C = 2x^3 - 2x^2 + x + C$$

Langkah 2: Menentukan nilai konstanta $C$ menggunakan titik $(1, 5)$:
$$f(1) = 5$$
$$2(1)^3 - 2(1)^2 + 1 + C = 5$$
$$2 - 2 + 1 + C = 5$$
$$1 + C = 5 \implies C = 4$$

Langkah 3: Menuliskan persamaan kurva lengkap:
$$f(x) = 2x^3 - 2x^2 + x + 4$$
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b03-a-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: antiturunan fungsi trigonometri*

Diketahui turunan pertama fungsi $g(x)$ adalah $g'(x) = 3\cos x + 4\sec^2 x$. Jika grafik fungsi $g(x)$ melalui titik $(0, 2)$, tentukan rumus fungsi $g(x)$.

- A. $g(x) = 3\sin x + 4\sec x$  
  <sub>Salah: Siswa salah mengingat integral dari $\sec^2 x$ menjadi $\sec x$ dan mengabaikan nilai konstanta.</sub>
- B. $g(x) = -3\sin x + 4\tan x + 2$  
  <sub>Salah: Siswa keliru menganggap integral dari $\cos x$ adalah $-\sin x$ (tertukar dengan rumus turunan).</sub>
- C. $g(x) = 3\sin x + 4\tan x$  
  <sub>Salah: Siswa mengabaikan syarat nilai awal $g(0) = 2$ sehingga menganggap konstanta integrasi $C = 0$.</sub>
- **D. $g(x) = 3\sin x + 4\tan x + 2$** ✅  
  <sub>Benar: Integral tak tentu dari $3\cos x + 4\sec^2 x$ adalah $3\sin x + 4\tan x + C$. Karena $g(0) = 2$, diperoleh $3\sin 0 + 4\tan 0 + C = 2 \implies C = 2$. Jadi, $g(x) = 3\sin x + 4\tan x + 2$.</sub>

**Pembahasan:** Langkah 1: Menentukan integral tak tentu dari $g'(x)$ menggunakan Sifat 3.8:
$$g(x) = \int (3\cos x + 4\sec^2 x)\,dx$$
$$g(x) = 3\int \cos x\,dx + 4\int \sec^2 x\,dx$$
$$g(x) = 3\sin x + 4\tan x + C$$

Langkah 2: Menentukan nilai $C$ menggunakan informasi titik $(0, 2)$:
$$g(0) = 2$$
$$3\sin(0) + 4\tan(0) + C = 2$$
$$3(0) + 4(0) + C = 2 \implies C = 2$$

Langkah 3: Menyusun rumus fungsi $g(x)$:
$$g(x) = 3\sin x + 4\tan x + 2$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b03-a-medium-bt01-009
*variasi (angka) | C3 | 2 langkah | jenis: integral tak tentu polinomial*

Tentukan integral tak tentu berikut.
$$\int (5x^4 - 6x^2 + 7)\,dx$$

- A. $5x^5 - 6x^3 + 7x + C$  
  <sub>Salah: Menambah pangkat variabel tanpa membagi dengan pangkat baru.</sub>
- B. $20x^3 - 12x + C$  
  <sub>Salah: Melakukan proses turunan (diferensiasi), bukan antiturunan (integrasi).</sub>
- C. $x^5 - 3x^3 + 7x + C$  
  <sub>Salah: Salah membagi koefisien $-6$ dengan $2$, bukan dengan $3$.</sub>
- **D. $x^5 - 2x^3 + 7x + C$** ✅  
  <sub>Benar: Integralkan per suku: $\int 5x^4\,dx = x^5$, $\int -6x^2\,dx = -2x^3$, dan $\int 7\,dx = 7x$. Jumlahkan semua suku dan tambahkan konstanta $C$.</sub>

**Pembahasan:** Terapkan sifat kelinieran integral tak tentu:
$$\int (5x^4 - 6x^2 + 7)\,dx = 5 \int x^4\,dx - 6 \int x^2\,dx + 7 \int dx$$
$$= 5\left(\frac{1}{5}x^5\right) - 6\left(\frac{1}{3}x^3\right) + 7x + C$$
$$= x^5 - 2x^3 + 7x + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b03-a-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: integral substitusi bentuk pecahan*

Hasil dari $\int \frac{2x + 3}{(x^2 + 3x - 1)^4}\,dx$ adalah ....

- A. $\frac{1}{3(x^2 + 3x - 1)^3} + C$  
  <sub>Salah: Lupa tanda minus yang muncul akibat pembagian dengan $-3$.</sub>
- B. $-\frac{1}{4(x^2 + 3x - 1)^4} + C$  
  <sub>Salah: Pangkat tidak ditambah satu saat pengintegralan.</sub>
- **C. $-\frac{1}{3(x^2 + 3x - 1)^3} + C$** ✅  
  <sub>Benar: Misalkan $u = x^2 + 3x - 1$, maka $du = (2x + 3)\,dx$. Integral menjadi $\int u^{-4}\,du = -\frac{1}{3}u^{-3} + C = -\frac{1}{3(x^2 + 3x - 1)^3} + C$.</sub>
- D. $\frac{1}{5(x^2 + 3x - 1)^5} + C$  
  <sub>Salah: Menambah pangkat penyebut menjadi $5$ bukan mengintegralkan pangkat $-4$ menjadi $-3$.</sub>

**Pembahasan:** 1. Nyatakan integral dalam bentuk pangkat negatif:
   $$\int (2x + 3)(x^2 + 3x - 1)^{-4}\,dx$$
2. Misalkan $u = x^2 + 3x - 1$, sehingga $du = (2x + 3)\,dx$.
3. Bentuk integral menjadi:
   $$\int u^{-4}\,du = \frac{u^{-4+1}}{-4+1} + C = -\frac{1}{3}u^{-3} + C$$
4. Substitusikan kembali $u$:
   $$-\frac{1}{3(x^2 + 3x - 1)^3} + C$$
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b03-a-medium-bt01-011
*orisinal | C4 | 3 langkah | jenis: nilai fungsi dari turunan*

Diketahui turunan pertama fungsi $f(x)$ adalah $f'(x) = 4x - 6$. Jika grafik fungsi $f(x)$ melalui titik $(2, -1)$, nilai dari $f(3)$ adalah ....

- A. $6$  
  <sub>Salah: Lupa mengalikan faktor saat menghitung turunan antiturunan $2x^2$ sebagai $x^2$.</sub>
- B. $0$  
  <sub>Salah: Mengabaikan konstanta integrasi ($C = 0$) sehingga $2(3)^2 - 6(3) = 0$.</sub>
- **C. $3$** ✅  
  <sub>Benar: $f(x) = \int (4x - 6)\,dx = 2x^2 - 6x + C$. Titik $(2, -1) \implies 2(2)^2 - 6(2) + C = -1 \implies 8 - 12 + C = -1 \implies C = 3$. Maka $f(x) = 2x^2 - 6x + 3$, sehingga $f(3) = 2(9) - 6(3) + 3 = 18 - 18 + 3 = 3$.</sub>
- D. $-1$  
  <sub>Salah: Kesalahan menghitung konstanta integrasi $C$, menghasilkan $C = -1$.</sub>

**Pembahasan:** 1. Cari antiturunan dari $f'(x)$:
   $$f(x) = \int (4x - 6)\,dx = 2x^2 - 6x + C$$
2. Tentukan nilai $C$ melalui titik $(2, -1)$:
   $$f(2) = 2(2)^2 - 6(2) + C = -1$$
   $$8 - 12 + C = -1 \implies -4 + C = -1 \implies C = 3$$
   Jadi, $f(x) = 2x^2 - 6x + 3$.
3. Hitung $f(3)$:
   $$f(3) = 2(3)^2 - 6(3) + 3 = 18 - 18 + 3 = 3$$
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b03-a-medium-bt01-012
*variasi (angka) | C3 | 2 langkah | jenis: integral substitusi polinomial*

Tentukan hasil dari integral tak tentu berikut.
$$\int 8x(4x^2 + 9)^3\,dx$$

- A. $\frac{1}{3}(4x^2 + 9)^4 + C$  
  <sub>Salah: Membagi dengan pangkat awal sebelum ditambah satu.</sub>
- B. $(4x^2 + 9)^4 + C$  
  <sub>Salah: Lupa membagi dengan pangkat baru setelah integrasi.</sub>
- C. \frac{1}{32}(4x^2 + 9)^4 + C  
  <sub>Salah: Mengalikan penyebut dengan koefisien 8 dua kali.</sub>
- **D. $\frac{1}{4}(4x^2 + 9)^4 + C$** ✅  
  <sub>Benar: Misalkan $u = 4x^2 + 9$, maka $du = 8x\,dx$. Bentuk integral menjadi $\int u^3\,du = \frac{1}{4}u^4 + C = \frac{1}{4}(4x^2 + 9)^4 + C$.</sub>

**Pembahasan:** Gunakan aturan integrasi substitusi:
1. Misalkan $u = 4x^2 + 9$, sehingga didapat $\frac{du}{dx} = 8x \iff du = 8x\,dx$.
2. Substitusikan ke dalam bentuk integral:
$$\int 8x(4x^2 + 9)^3\,dx = \int u^3\,du = \frac{1}{3 + 1}u^{3+1} + C = \frac{1}{4}u^4 + C$$
3. Kembalikan variabel $u$ ke dalam $x$:
$$= \frac{1}{4}(4x^2 + 9)^4 + C$$
**Acuan:** siswa — siswa hal.188 Contoh Soal 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b03-a-medium-bt01-013
*variasi (angka) | C3 | 3 langkah | jenis: integral substitusi bentuk akar*

Tentukan hasil dari integral tak tentu berikut.
$$\int \sqrt{5x + 6}\,dx$$

- A. $\frac{2}{5}(5x + 6)\sqrt{5x + 6} + C$  
  <sub>Salah: Lupa membagi dengan pangkat baru pecahan $\frac{3}{2}$.</sub>
- **B. $\frac{2}{15}(5x + 6)\sqrt{5x + 6} + C$** ✅  
  <sub>Benar: Misalkan $u = 5x + 6$, maka $dx = \frac{1}{5}\,du$. Hasil integral adalah $\frac{1}{5} \cdot \frac{2}{3}u^{3/2} + C = \frac{2}{15}(5x + 6)^{3/2} + C = \frac{2}{15}(5x + 6)\sqrt{5x + 6} + C$.</sub>
- C. $\frac{2}{3}(5x + 6)\sqrt{5x + 6} + C$  
  <sub>Salah: Lupa mengalikan dengan faktor diferensial $\frac{1}{5}$ dari turunan fungsi dalam.</sub>
- D. $\frac{1}{15}(5x + 6)\sqrt{5x + 6} + C$  
  <sub>Salah: Salah mengalikan koefisien $\frac{1}{5}$ dengan $\frac{1}{3}$ alih-alih $\frac{2}{3}$.</sub>

**Pembahasan:** Ubah bentuk akar menjadi bentuk pangkat pecahan:
$$\int \sqrt{5x + 6}\,dx = \int (5x + 6)^{\frac{1}{2}}\,dx$$
1. Misalkan $u = 5x + 6$, maka $du = 5\,dx \iff dx = \frac{1}{5}\,du$.
2. Lakukan substitusi ke integral:
$$\int u^{\frac{1}{2}} \cdot \frac{1}{5}\,du = \frac{1}{5} \int u^{\frac{1}{2}}\,du = \frac{1}{5} \left( \frac{1}{\frac{1}{2} + 1} u^{\frac{1}{2} + 1} \right) + C$$
$$= \frac{1}{5} \cdot \frac{2}{3} u^{\frac{3}{2}} + C = \frac{2}{15} u^{\frac{3}{2}} + C$$
3. Nyatakan kembali dalam variabel $x$ dan bentuk akar:
$$= \frac{2}{15}(5x + 6)^{\frac{3}{2}} + C = \frac{2}{15}(5x + 6)\sqrt{5x + 6} + C$$
**Acuan:** siswa — siswa hal.189 Ayo Mencoba 3.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b03-a-medium-bt01-014
*variasi (angka) | C3 | 2 langkah | jenis: integral tak tentu aljabar*

Tentukan hasil dari integral tak tentu berikut.
$$\int (7x^6 - 8x^3)\,dx$$

- A. $x^7 - 4x^4 + C$  
  <sub>Salah: Membagi 8 dengan 2 bukan dengan pangkat baru 4.</sub>
- B. $\frac{7}{6}x^7 - 2x^4 + C$  
  <sub>Salah: Membagi koefisien suku pertama dengan pangkat lama 6 bukan 7.</sub>
- **C. $x^7 - 2x^4 + C$** ✅  
  <sub>Benar: $\int 7x^6\,dx - \int 8x^3\,dx = 7 \cdot \frac{1}{7}x^7 - 8 \cdot \frac{1}{4}x^4 + C = x^7 - 2x^4 + C$.</sub>
- D. $42x^5 - 24x^2 + C$  
  <sub>Salah: Melakukan proses diferensiasi (turunan) alih-alih integrasi.</sub>

**Pembahasan:** Gunakan aturan integral tak tentu untuk fungsi aljabar:
$$\int (7x^6 - 8x^3)\,dx = 7 \int x^6\,dx - 8 \int x^3\,dx$$
$$= 7 \left( \frac{1}{6+1} x^{6+1} \right) - 8 \left( \frac{1}{3+1} x^{3+1} \right) + C$$
$$= 7 \cdot \frac{1}{7}x^7 - 8 \cdot \frac{1}{4}x^4 + C$$
$$= x^7 - 2x^4 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-1c

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b03-a-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: masalah gerak lurus*

Sebuah partikel bergerak di sepanjang garis lurus dengan percepatan setiap saat dinyatakan oleh $a(t) = 6t - 2\text{ m/s}^2$. Jika pada saat $t = 1$ detik kecepatan partikel adalah $7\text{ m/s}$ dan pada saat $t = 2$ detik posisi partikel berada pada $s = 20\text{ meter}$, tentukan rumus fungsi posisi $s(t)$ partikel tersebut.

- A. $s(t) = t^3 - t^2 + 7t + 4$  
  <sub>Salah: Menggunakan nilai $v(1) = 7$ langsung sebagai koefisien $t$ tanpa mencari konstanta $C_1$.</sub>
- B. $s(t) = t^3 - t^2 + 6t + 20$  
  <sub>Salah: Mengira posisi pada $t = 2$ langsung menjadi konstanta posisi $C_2$.</sub>
- **C. $s(t) = t^3 - t^2 + 6t + 4$** ✅  
  <sub>Benar: Integrasikan $a(t)$ untuk mendapatkan $v(t) = 3t^2 - 2t + 6$, kemudian integrasikan $v(t)$ untuk memperoleh $s(t) = t^3 - t^2 + 6t + 4$.</sub>
- D. $s(t) = 3t^3 - 2t^2 + 6t + 4$  
  <sub>Salah: Lupa membagi koefisien dengan pangkat baru saat mengintegralkan percepatan kedua kalinya.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Menentukan fungsi kecepatan $v(t)$:
$$v(t) = \int a(t)\,dt = \int (6t - 2)\,dt = 3t^2 - 2t + C_1$$
Diketahui $v(1) = 7$:
$$3(1)^2 - 2(1) + C_1 = 7 \implies 1 + C_1 = 7 \implies C_1 = 6$$
Sehingga, $v(t) = 3t^2 - 2t + 6$.

2. Menentukan fungsi posisi $s(t)$:
$$s(t) = \int v(t)\,dt = \int (3t^2 - 2t + 6)\,dt = t^3 - t^2 + 6t + C_2$$
Diketahui $s(2) = 20$:
$$(2)^3 - (2)^2 + 6(2) + C_2 = 20$$
$$8 - 4 + 12 + C_2 = 20 \implies 16 + C_2 = 20 \implies C_2 = 4$$

3. Maka rumus posisi partikel adalah:
$$s(t) = t^3 - t^2 + 6t + 4$$
**Acuan:** siswa — siswa hal.190

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b03-a-medium-bt01-016
*orisinal | C3 | 2 langkah | jenis: integral substitusi pangkat negatif*

Tentukan hasil dari integral tak tentu berikut.
$$\int \frac{3x^2}{(x^3 + 2)^5}\,dx$$

- A. $\frac{1}{4(x^3 + 2)^4} + C$  
  <sub>Salah: Lupa tanda negatif dari pembagi pangkat baru $-4$.</sub>
- **B. $-\frac{1}{4(x^3 + 2)^4} + C$** ✅  
  <sub>Benar: Substitusi $u = x^3 + 2$ menghasilkan $\int u^{-5}\,du = -\frac{1}{4}u^{-4} + C = -\frac{1}{4(x^3 + 2)^4} + C$.</sub>
- C. $-\frac{1}{5(x^3 + 2)^4} + C$  
  <sub>Salah: Membagi dengan pangkat lama $-5$ alih-alih $-4$.</sub>
- D. $-\frac{1}{6(x^3 + 2)^6} + C$  
  <sub>Salah: Menambah nilai mutlak pangkat pada penyebut seolah-olah pangkat positif.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Tuliskan integral dalam bentuk pangkat:
$$\int \frac{3x^2}{(x^3 + 2)^5}\,dx = \int 3x^2(x^3 + 2)^{-5}\,dx$$
2. Misalkan $u = x^3 + 2$, maka $du = 3x^2\,dx$.
3. Bentuk integral menjadi:
$$\int u^{-5}\,du = \frac{1}{-5 + 1}u^{-5 + 1} + C = -\frac{1}{4}u^{-4} + C = -\frac{1}{4u^4} + C$$
4. Kembalikan variabel $u$:
$$= -\frac{1}{4(x^3 + 2)^4} + C$$
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b03-a-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: integral substitusi trigonometri*

Hasil dari integral tak tentu $\int \sin^3 x \cos x\,dx$ adalah ....

- A. $\frac{1}{4}\sin^4 x \cos x + C$  
  <sub>Salah: Tidak menghilangkan faktor turunan $\cos x$ setelah melakukan pengintegralan substitusi.</sub>
- **B. $\frac{1}{4}\sin^4 x + C$** ✅  
  <sub>Benar: Dengan memisalkan $u = \sin x$, diperoleh $du = \cos x\,dx$, sehingga $\int u^3\,du = \frac{1}{4}u^4 + C = \frac{1}{4}\sin^4 x + C$.</sub>
- C. $\frac{1}{3}\sin^3 x + C$  
  <sub>Salah: Lupa menambahkan 1 pada pangkat ketika mengintegralkan suku berpangkat.</sub>
- D. -\frac{1}{4}\cos^4 x + C$  
  <sub>Salah: Tertukar fungsi yang dimisalkan dan salah menggunakan antiturunan trigonometri.</sub>

**Pembahasan:** Bentuk $\int [g(x)]^n g'(x)\,dx$ diselesaikan menggunakan aturan integrasi substitusi:
1. Misalkan $u = \sin x \implies \frac{du}{dx} = \cos x \implies du = \cos x\,dx$.
2. Substitusikan ke dalam integral:
   $$\int \sin^3 x \cos x\,dx = \int u^3\,du = \frac{1}{3 + 1}u^{3 + 1} + C = \frac{1}{4}u^4 + C$$
3. Kembalikan ke variabel $x$:
   $$= \frac{1}{4}\sin^4 x + C$$
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b03-a-medium-bt01-018
*variasi (angka) | C3 | 2 langkah | jenis: teknik substitusi fungsi kuadrat*

Tentukan hasil dari $\int x(x^2 - 16)^3\,dx$ dengan menggunakan teknik substitusi.

- A. $\frac{1}{6}(x^2 - 16)^4 + C$  
  <sub>Salah: Salah mengalikan penyebut, yaitu mengalikan 2 dengan 3 bukan dengan 4.</sub>
- B. $\frac{1}{8}(x^2 - 16)^3 + C$  
  <sub>Salah: Lupa menambahkan 1 pada pangkat saat melakukan integrasi.</sub>
- **C. $\frac{1}{8}(x^2 - 16)^4 + C$** ✅  
  <sub>Benar: Misalkan $u = x^2 - 16$, maka $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,du$. Integral menjadi $\int \frac{1}{2}u^3\,du = \frac{1}{8}u^4 + C = \frac{1}{8}(x^2 - 16)^4 + C$.</sub>
- D. $\frac{1}{4}(x^2 - 16)^4 + C$  
  <sub>Salah: Lupa membagi dengan turunan fungsi dalam (faktor 1/2).</sub>

**Pembahasan:** Gunakan metode substitusi:
1. Misalkan $u = x^2 - 16$, sehingga $\frac{du}{dx} = 2x \implies x\,dx = \frac{1}{2}\,du$.
2. Substitusikan ke integral:
$$\int x(x^2 - 16)^3\,dx = \int u^3 \cdot \frac{1}{2}\,du = \frac{1}{2} \left(\frac{1}{4}u^4\right) + C = \frac{1}{8}u^4 + C$$
3. Kembalikan ke variabel $x$:
$$\frac{1}{8}(x^2 - 16)^4 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b03-a-medium-bt01-019
*variasi (angka) | C3 | 2 langkah | jenis: integral substitusi aljabar berpangkat*

Tentukan integral tak tentu berikut.
$$\int x(8x^2 + 9)^4\,dx$$

- **A. $\frac{1}{80}(8x^2 + 9)^5 + C$** ✅  
  <sub>Benar: Dengan memisalkan $u = 8x^2 + 9$, diperoleh $du = 16x\,dx$ sehingga $x\,dx = \frac{du}{16}$. Integral menjadi $\frac{1}{16} \int u^4\,du = \frac{1}{80}u^5 + C = \frac{1}{80}(8x^2 + 9)^5 + C$.</sub>
- B. $\frac{1}{80}(8x^2 + 9)^4 + C$  
  <sub>Salah: Lupa menaikkan pangkat fungsi setelah proses integrasi.</sub>
- C. $\frac{1}{40}(8x^2 + 9)^5 + C$  
  <sub>Salah: Mengira turunan dari $8x^2$ adalah $8x$ sehingga hanya membagi dengan 8.</sub>
- D. $\frac{1}{5}(8x^2 + 9)^5 + C$  
  <sub>Salah: Mengabaikan turunan fungsi dalam sehingga tidak membagi dengan 16.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Misalkan $u = 8x^2 + 9$, maka $du = 16x\,dx \implies x\,dx = \frac{du}{16}$.
2. Tuliskan integral dalam variabel $u$:
$$\int x(8x^2 + 9)^4\,dx = \int u^4 \cdot \frac{du}{16} = \frac{1}{16} \left(\frac{1}{5}u^5\right) + C = \frac{1}{80}u^5 + C$$
3. Ganti kembali $u = 8x^2 + 9$:
$$\frac{1}{80}(8x^2 + 9)^5 + C$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-3a

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b03-a-medium-bt01-020
*variasi (konteks) | C4 | 3 langkah | jenis: aplikasi integral laju perubahan*

Laju pertumbuhan massa suatu kristal pada $t$ jam setelah pemanasan dimulai dinyatakan oleh persamaan $m'(t) = (15 - t)^{-2}$ gram per jam ($0 \le t \le 12$). Jika pada saat $t = 5$ jam massa kristal tersebut tercatat $4$ gram, tentukan massa kristal tersebut pada saat $t = 10$ jam.

- A. $3,8\text{ gram}$  
  <sub>Salah: Kesalahan tanda saat mengintegralkan $(15 - t)^{-2}$ menjadi $-(15 - t)^{-1}$.</sub>
- B. $4,0\text{ gram}$  
  <sub>Salah: Mengabaikan perubahan laju dan berasumsi massa kristal tidak bertambah secara signifikan.</sub>
- C. $4,2\text{ gram}$  
  <sub>Salah: Salah menghitung nilai desimal pecahan 1/5 menjadi 0,3.</sub>
- **D. $4,1\text{ gram}$** ✅  
  <sub>Benar: Antiturunan dari $m'(t) = (15 - t)^{-2}$ adalah $m(t) = (15 - t)^{-1} + C$. Dari $m(5) = 4$, diperoleh $\frac{1}{10} + C = 4 \implies C = 3,9$. Maka $m(10) = \frac{1}{5} + 3,9 = 0,2 + 3,9 = 4,1\text{ gram}$.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Tentukan fungsi massa $m(t)$ melalui integral tak tentu:
$$m(t) = \int (15 - t)^{-2}\,dt$$
Misalkan $u = 15 - t$, maka $du = -dt \implies dt = -du$.
$$m(t) = \int -u^{-2}\,du = -\left(-u^{-1}\right) + C = \frac{1}{15 - t} + C$$
2. Tentukan konstanta $C$ menggunakan kondisi $m(5) = 4$:
$$4 = \frac{1}{15 - 5} + C \implies 4 = \frac{1}{10} + C \implies C = 4 - 0,1 = 3,9$$
Sehingga, rumus massa adalah $m(t) = \frac{1}{15 - t} + 3,9$.
3. Hitung massa pada saat $t = 10$ jam:
$$m(10) = \frac{1}{15 - 10} + 3,9 = \frac{1}{5} + 3,9 = 0,2 + 3,9 = 4,1\text{ gram}$$
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b03-a-hard-bt01-001
*variasi (angka) | C5 | 5 langkah | jenis: gerak partikel*

Sebuah partikel bergerak pada suatu garis lurus dengan arah positif ke kanan dari titik pusat. Kecepatan partikel pada saat $t$ detik dinyatakan oleh $v(t) = 12\cos(3t)\text{ cm/detik}$. Jika pada saat awal ($t = 0$) posisi partikel berada $7\text{ cm}$ di sebelah kanan titik pusat, tentukan posisi partikel pada saat kecepatannya bernilai nol untuk pertama kali setelah $t = 0$.

- A. $19\text{ cm}$ di sebelah kanan titik pusat  
  <sub>Salah: Siswa lupa membagi dengan turunan fungsi dalam (faktor 3) saat mengintegralkan, sehingga mendapatkan $s(t) = 12\sin(3t) + 7$ dan menghasilkan $12 + 7 = 19$.</sub>
- B. $7\text{ cm}$ di sebelah kanan titik pusat  
  <sub>Salah: Siswa hanya menggunakan nilai konstanta integrasi awal tanpa menambahkan perubahan posisi dari integral.</sub>
- **C. $11\text{ cm}$ di sebelah kanan titik pusat** ✅  
  <sub>Benar: Kecepatan nol pertama kali saat $3t = \frac{\pi}{2} \iff t = \frac{\pi}{6}$. Fungsi posisi $s(t) = \int 12\cos(3t)\,dt = 4\sin(3t) + 7$. Pada $t = \frac{\pi}{6}$, $s = 4\sin(\frac{\pi}{2}) + 7 = 11\text{ cm}$.</sub>
- D. $3\text{ cm}$ di sebelah kanan titik pusat  
  <sub>Salah: Siswa salah tanda saat mengintegralkan kosinus menjadi $-\sin$, sehingga menghitung $-4 + 7 = 3$.</sub>

**Pembahasan:** Langkah 1: Menentukan waktu $t$ saat kecepatan bernilai nol pertama kali setelah $t = 0$.
$$v(t) = 12\cos(3t) = 0$$
Nilai nol terkecil positif tercapai saat:
$$3t = \frac{\pi}{2} \implies t = \frac{\pi}{6}\text{ detik}$$

Langkah 2: Menentukan fungsi posisi $s(t)$ dengan mengintegralkan fungsi kecepatan.
$$s(t) = \int v(t)\,dt = \int 12\cos(3t)\,dt = 4\sin(3t) + C$$

Langkah 3: Menentukan nilai konstanta integrasi $C$ dari kondisi awal $s(0) = 7$.
$$s(0) = 4\sin(0) + C = 7 \implies C = 7$$
Sehingga persamaan posisi adalah:
$$s(t) = 4\sin(3t) + 7$$

Langkah 4: Menghitung posisi pada saat $t = \frac{\pi}{6}$ detik.
$$s\left(\frac{\pi}{6}\right) = 4\sin\left(3 \cdot \frac{\pi}{6}\right) + 7 = 4\sin\left(\frac{\pi}{2}\right) + 7 = 4(1) + 7 = 11\text{ cm}$$

Jadi, posisi partikel saat kecepatannya nol pertama kali adalah $11\text{ cm}$ di sebelah kanan titik pusat.
**Acuan:** siswa — siswa hal.190 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b03-a-hard-bt01-002
*variasi (konteks) | C5 | 4 langkah | jenis: pemodelan laju perubahan*

Suatu tangki penyimpanan bahan kimia mengalami penumpukan kerak pada dindingnya. Laju pertambahan ketebalan kerak pada jam ke-$t$ pemanasan ($0 \le t < 9$) dinyatakan oleh persamaan $\frac{dh}{dt} = 18(9 - t)^{-2}\text{ mm/jam}$. Jika setelah $3\text{ jam}$ pemanasan ketebalan kerak terukur $5\text{ mm}$, berapakah ketebalan kerak setelah $6\text{ jam}$ pemanasan?

- A. $2\text{ mm}$  
  <sub>Salah: Siswa keliru tanda negatif dari turunan substitusi $u = 9 - t$ sehingga memperoleh $h(t) = -\frac{18}{9-t} + 8$ yang menghasilkan $-6 + 8 = 2$.</sub>
- **B. $8\text{ mm}$** ✅  
  <sub>Benar: Fungsi ketebalan $h(t) = \int 18(9-t)^{-2}\,dt = \frac{18}{9-t} + C$. Dari $h(3) = 5$ diperoleh $\frac{18}{6} + C = 5 \implies C = 2$. Pada $t = 6$, $h(6) = \frac{18}{3} + 2 = 8\text{ mm}$.</sub>
- C. $11\text{ mm}$  
  <sub>Salah: Siswa salah menentukan nilai $C$ dengan langsung menganggap $C = 5$, sehingga menghitung $\frac{18}{3} + 5 = 11$.</sub>
- D. $6\text{ mm}$  
  <sub>Salah: Siswa lupa memperhitungkan konstanta integrasi $C = 2$ sehingga hanya menghitung $\frac{18}{9-6} = 6$.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi ketebalan kerak $h(t)$ melalui integrasi laju perubahan.
$$h(t) = \int 18(9 - t)^{-2}\,dt$$
Gunakan substitusi $u = 9 - t$, sehingga $du = -dt$ atau $dt = -du$:
$$h(t) = \int 18 u^{-2}(-du) = -18 \left(-\frac{1}{u}\right) + C = \frac{18}{9 - t} + C$$

Langkah 2: Menentukan nilai konstanta $C$ menggunakan kondisi $h(3) = 5$.
$$h(3) = \frac{18}{9 - 3} + C = 5$$
$$\frac{18}{6} + C = 5 \implies 3 + C = 5 \implies C = 2$$

Langkah 3: Menuliskan persamaan fungsi ketebalan kerak secara lengkap.
$$h(t) = \frac{18}{9 - t} + 2$$

Langkah 4: Menghitung ketebalan kerak pada saat $t = 6\text{ jam}$.
$$h(6) = \frac{18}{9 - 6} + 2 = \frac{18}{3} + 2 = 6 + 2 = 8\text{ mm}$$

Jadi, ketebalan kerak setelah 6 jam pemanasan adalah $8\text{ mm}$.
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b03-a-hard-bt01-003
*orisinal | C5 | 6 langkah | jenis: persamaan integral fungsional*

Fungsi $f(x)$ terdiferensialkan untuk semua bilangan real dan memenuhi hubungan $\int x f'(x)\,dx = 4x^3 - 6x^2 + C$. Jika diketahui bahwa $f(1) = 8$, berapakah nilai dari $f(2)$?

- A. $26$  
  <sub>Salah: Siswa lupa membagi dengan 2 saat mengintegralkan $12x$ sehingga menganggap integralnya adalah $12x^2$.</sub>
- B. $2$  
  <sub>Salah: Siswa salah tanda aljabar saat mencari konstanta: $-6 + K = 8$ keliru dihitung sebagai $K = 8 - 6 = 2$, sehingga $f(2) = 2$.</sub>
- C. $12$  
  <sub>Salah: Siswa keliru mengira yang ditanyakan adalah nilai dari turunan $f'(2) = 12(2) - 12 = 12$.</sub>
- **D. $14$** ✅  
  <sub>Benar: Turunkan kedua ruas diperoleh $x f'(x) = 12x^2 - 12x \implies f'(x) = 12x - 12$. Integralkan kembali: $f(x) = 6x^2 - 12x + K$. Dari $f(1) = 8 \implies 6 - 12 + K = 8 \implies K = 14$. Maka $f(2) = 6(4) - 12(2) + 14 = 14$.</sub>

**Pembahasan:** Langkah 1: Menurunkan kedua ruas terhadap $x$ dengan memanfaatkan definisi bahwa turunan dari integral tak tentu suatu fungsi adalah fungsi di dalam integral tersebut:
$$\frac{d}{dx}\left(\int x f'(x)\,dx\right) = \frac{d}{dx}\left(4x^3 - 6x^2 + C\right)$$
$$x f'(x) = 12x^2 - 12x$$

Langkah 2: Menentukan $f'(x)$ dengan membagi kedua ruas dengan $x$ untuk $x \ne 0$:
$$f'(x) = 12x - 12$$

Langkah 3: Mengintegralkan $f'(x)$ untuk mendapatkan bentuk umum $f(x)$:
$$f(x) = \int (12x - 12)\,dx = 6x^2 - 12x + K$$

Langkah 4: Menentukan konstanta $K$ menggunakan informasi $f(1) = 8$:
$$f(1) = 6(1)^2 - 12(1) + K = 8$$
$$-6 + K = 8 \implies K = 14$$

Langkah 5: Menuliskan rumus fungsi $f(x)$ secara eksplisit:
$$f(x) = 6x^2 - 12x + 14$$

Langkah 6: Menghitung nilai $f(2)$:
$$f(2) = 6(2)^2 - 12(2) + 14 = 24 - 24 + 14 = 14$$

Jadi, nilai dari $f(2)$ adalah $14$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b03-a-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: fungsi marginal ekonomi*

Sebuah distributor barang elektronik mencatat bahwa laju perubahan harga terhadap jumlah permintaan mingguan (fungsi marginal harga) memenuhi persamaan $p'(x) = -0,06e^{-0,02x}$ (dalam ribuan rupiah), dengan $x$ menyatakan banyaknya unit barang yang diminta per minggu. Jika saat permintaan mencapai $40$ unit harga yang terbentuk adalah Rp78.000,00 per unit, berapakah harga per unit yang harus ditetapkan jika permintaan meningkat menjadi $90$ unit per minggu? (Gunakan pendekatan $e^{-0,8} \approx 0,45$ dan $e^{-1,8} \approx 0,165$)

- A. Rp77.505,00  
  <sub>Salah: Siswa keliru membagi koefisien menjadi $-3$ alih-alih $+3$ saat mengintegralkan, lalu melakukan pengurangan yang terbalik.</sub>
- **B. Rp77.145,00** ✅  
  <sub>Benar: Fungsi harga $p(x) = \int -0,06e^{-0,02x}\,dx = \frac{-0,06}{-0,02}e^{-0,02x} + C = 3e^{-0,02x} + C$. Diketahui $p(40) = 78$ (ribu), maka $3e^{-0,02(40)} + C = 78 \iff 3(0,45) + C = 78 \iff 1,35 + C = 78 \iff C = 76,65$. Untuk $x = 90$, diperoleh $p(90) = 3e^{-0,02(90)} + 76,65 = 3(0,165) + 76,65 = 0,495 + 76,65 = 77,145$ ribu rupiah, yaitu Rp77.145,00.</sub>
- C. Rp78.855,00  
  <sub>Salah: Siswa salah mengalikan turunan dalam integrasi eksponensial sehingga suku berubah menjadi $-0,06 \times (-0,02)$.</sub>
- D. Rp76.650,00  
  <sub>Salah: Siswa hanya menghitung nilai konstanta $C$ dan mengabaikan nilai suku eksponensial $3e^{-1,8}$.</sub>

**Pembahasan:** Langkah 1: Menentukan fungsi harga $p(x)$ dari fungsi marginal:
$$p(x) = \int p'(x)\,dx = \int -0,06e^{-0,02x}\,dx = \frac{-0,06}{-0,02}e^{-0,02x} + C = 3e^{-0,02x} + C$$

Langkah 2: Menentukan konstanta $C$ menggunakan kondisi $p(40) = 78$:
$$3e^{-0,02(40)} + C = 78$$
$$3e^{-0,8} + C = 78$$
$$3(0,45) + C = 78$$
$$1,35 + C = 78 \implies C = 76,65$$

Langkah 3: Menghitung harga per unit untuk $x = 90$:
$$p(90) = 3e^{-0,02(90)} + 76,65$$
$$p(90) = 3e^{-1,8} + 76,65$$
$$p(90) = 3(0,165) + 76,65 = 0,495 + 76,65 = 77,145$$

Jadi, harga yang harus ditetapkan adalah Rp77.145,00.
**Acuan:** siswa — siswa hal.193 Latihan Soal Integral Tak Tentu

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b03-a-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: titik balik fungsi antiturunan*

Grafik fungsi $y = F(x)$ merupakan salah satu antiturunan dari fungsi $f(x) = 3x^2 - 12x + 9$. Jika grafik fungsi $F(x)$ mempunyai titik balik maksimum lokal di titik $(p, 10)$, nilai minimum lokal dari fungsi $F(x)$ adalah ....

- A. 2  
  <sub>Salah: Siswa salah menentukan nilai konstanta $C$, menganggap $C = 2$ karena keliru saat mengoperasikan $1 - 6 + 9$.</sub>
- B. 4  
  <sub>Salah: Siswa lupa memperhitungkan suku konstan $C$ pada fungsi hasil integrasi saat menghitung nilai $F(3)$.</sub>
- **C. 6** ✅  
  <sub>Benar: $F'(x) = f(x) = 3(x - 1)(x - 3) = 0 \implies x = 1$ atau $x = 3$. Karena $F''(1) = -6 < 0$, titik maksimum lokal tercapai di $x = 1$, sehingga $p = 1$ dan $F(1) = 10$. Antiturunannya adalah $F(x) = x^3 - 6x^2 + 9x + C$. Dengan $F(1) = 1 - 6 + 9 + C = 10$, diperoleh $C = 6$. Nilai minimum lokal terjadi pada $x = 3$, yaitu $F(3) = 3^3 - 6(3^2) + 9(3) + 6 = 6$.</sub>
- D. 8  
  <sub>Salah: Siswa salah mengidentifikasi absis titik balik, menukar titik minimum pada $x = 1$ dan maksimum pada $x = 3$.</sub>

**Pembahasan:** Langkah 1: Menentukan titik stasioner fungsi $F(x)$:
Karena $F'(x) = f(x)$, maka:
$$3x^2 - 12x + 9 = 0 \iff 3(x - 1)(x - 3) = 0 \iff x = 1 \text{ atau } x = 3$$

Langkah 2: Menentukan jenis titik stasioner:
$$F''(x) = 6x - 12$$
Untuk $x = 1 \implies F''(1) = 6(1) - 12 = -6 < 0$ (titik maksimum lokal).
Untuk $x = 3 \implies F''(3) = 6(3) - 12 = 6 > 0$ (titik minimum lokal).
Diketahui titik maksimum di $(p, 10)$, maka $p = 1$ dan $F(1) = 10$.

Langkah 3: Menentukan rumus fungsi $F(x)$:
$$F(x) = \int (3x^2 - 12x + 9)\,dx = x^3 - 6x^2 + 9x + C$$
$$F(1) = 1^3 - 6(1^2) + 9(1) + C = 10 \iff 4 + C = 10 \implies C = 6$$
Jadi, $F(x) = x^3 - 6x^2 + 9x + 6$.

Langkah 4: Menghitung nilai minimum lokal di $x = 3$:
$$F(3) = 3^3 - 6(3^2) + 9(3) + 6 = 27 - 54 + 27 + 6 = 6$$
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b03-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: analisis asimtot dan ekstrem kurva*

Diketahui turunan pertama fungsi $f(x)$ adalah $f'(x) = \frac{6x - 6}{(x^2 - 2x + 3)^2}$. Kurva $y = f(x)$ memiliki asimtot datar $y = 2$ ketika $x \to \infty$. Nilai minimum mutlak fungsi $f(x)$ pada domain bilangan real adalah ....

- A. 1  
  <sub>Salah: Siswa salah menyubstitusikan nilai penyebut dengan mengabaikan konstanta $+2$ pada kuadrat sempurna.</sub>
- **B. \frac{1}{2}** ✅  
  <sub>Benar: Dengan substitusi $u = x^2 - 2x + 3$, didapat $du = (2x - 2)\,dx$, sehingga $f(x) = \int 3u^{-2}\,du = -\frac{3}{u} + C = -\frac{3}{x^2 - 2x + 3} + C$. Karena $\lim_{x \to \infty} f(x) = 2$, maka $0 + C = 2 \implies C = 2$. Bentuk penyebut $x^2 - 2x + 3 = (x - 1)^2 + 2$ bernilai minimum $2$ saat $x = 1$. Akibatnya, nilai minimum fungsi $f(x)$ tercapai di $x = 1$, yaitu $f(1) = -\frac{3}{2} + 2 = \frac{1}{2}$.</sub>
- C. -\frac{1}{2}  
  <sub>Salah: Siswa keliru menganggap $C = 1$ saat menganalisis asimtot datar.</sub>
- D. \frac{3}{2}  
  <sub>Salah: Siswa menghitung nilai suku $\frac{3}{x^2 - 2x + 3}$ saja tanpa menyertakan konstanta $C$ dan tanda negatif.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus $f(x)$ menggunakan aturan substitusi:
Misalkan $u = x^2 - 2x + 3$, maka $du = (2x - 2)\,dx$.
Pembilang dapat ditulis sebagai $3(2x - 2)\,dx = 3\,du$.
$$f(x) = \int \frac{3\,du}{u^2} = \int 3u^{-2}\,du = -3u^{-1} + C = -\frac{3}{x^2 - 2x + 3} + C$$

Langkah 2: Menentukan nilai konstanta $C$ dari asimtot datar:
$$\lim_{x \to \infty} f(x) = \lim_{x \to \infty} \left(-\frac{3}{x^2 - 2x + 3} + C\right) = 0 + C = 2 \implies C = 2$$
Sehingga $f(x) = 2 - \frac{3}{x^2 - 2x + 3}$.

Langkah 3: Menganalisis nilai minimum fungsi:
Fungsi $f(x) = 2 - \frac{3}{x^2 - 2x + 3}$ akan bernilai minimum ketika pecahan $\frac{3}{x^2 - 2x + 3}$ bernilai maksimum, yaitu saat penyebutnya $x^2 - 2x + 3 = (x - 1)^2 + 2$ bernilai minimum.
Nilai minimum penyebut adalah $2$ (tercapai saat $x = 1$).

Langkah 4: Menghitung nilai minimum fungsi:
$$f(1) = 2 - \frac{3}{(1 - 1)^2 + 2} = 2 - \frac{3}{2} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b03-a-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: rekonstruksi kurva antiturunan tingkat dua*

Turunan kedua suatu fungsi adalah $f''(x) = 4\cos(2x) - 6\sin(3x)$ untuk setiap $x \in \mathbb{R}$. Kurva $y = f(x)$ memiliki garis singgung horizontal di titik $(0, 5)$. Nilai dari $f(\pi)$ adalah ....

- A. 7 - 2\pi  
  <sub>Salah: Siswa salah tanda saat mengintegralkan $\sin(2x)$, menuliskan $+\cos(2x)$ alih-alih $-\cos(2x)$ sehingga $C_2 = 4$ dan evaluasi menghasilkan $7 - 2\pi$.</sub>
- B. 6 - 2\pi  
  <sub>Salah: Siswa mengabaikan suku $-\cos(2\pi) = -1$ saat melakukan evaluasi akhir pada nilai $x = \pi$.</sub>
- **C. 5 - 2\pi** ✅  
  <sub>Benar: Pengintegralan pertama menghasilkan $f'(x) = 2\sin(2x) + 2\cos(3x) + C_1$. Garis singgung horizontal di $x = 0$ berarti $f'(0) = 0 \implies 0 + 2 + C_1 = 0 \implies C_1 = -2$. Pengintegralan kedua menghasilkan $f(x) = -\cos(2x) + \frac{2}{3}\sin(3x) - 2x + C_2$. Kurva melalui $(0, 5) \implies -1 + 0 - 0 + C_2 = 5 \implies C_2 = 6$. Maka $f(\pi) = -\cos(2\pi) + \frac{2}{3}\sin(3\pi) - 2\pi + 6 = -1 + 0 - 2\pi + 6 = 5 - 2\pi$.</sub>
- D. 5 + 2\pi  
  <sub>Salah: Siswa salah menentukan tanda dari konstanta $C_1$, mendapatkan $C_1 = +2$ dan menghasilkan suku $+2\pi$.</sub>

**Pembahasan:** Langkah 1: Menentukan $f'(x)$ melalui integral pertama:
$$f'(x) = \int (4\cos(2x) - 6\sin(3x))\,dx = 2\sin(2x) + 2\cos(3x) + C_1$$

Langkah 2: Menentukan $C_1$ menggunakan syarat garis singgung horizontal di $x = 0$ ($f'(0) = 0$):
$$f'(0) = 2\sin(0) + 2\cos(0) + C_1 = 0 \iff 0 + 2(1) + C_1 = 0 \implies C_1 = -2$$
Sehingga $f'(x) = 2\sin(2x) + 2\cos(3x) - 2$.

Langkah 3: Menentukan $f(x)$ melalui integral kedua:
$$f(x) = \int (2\sin(2x) + 2\cos(3x) - 2)\,dx = -\cos(2x) + \frac{2}{3}\sin(3x) - 2x + C_2$$

Langkah 4: Menentukan $C_2$ menggunakan titik $(0, 5)$ yang dilalui kurva:
$$f(0) = -\cos(0) + \frac{2}{3}\sin(0) - 2(0) + C_2 = 5 \iff -1 + 0 - 0 + C_2 = 5 \implies C_2 = 6$$
Jadi, $f(x) = -\cos(2x) + \frac{2}{3}\sin(3x) - 2x + 6$.

Langkah 5: Menghitung nilai $f(\pi)$:
$$f(\pi) = -\cos(2\pi) + \frac{2}{3}\sin(3\pi) - 2\pi + 6 = -(1) + \frac{2}{3}(0) - 2\pi + 6 = 5 - 2\pi$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b03-a-hard-bt01-008
*variasi (konteks) | C5 | 4 langkah | jenis: pemodelan peluruhan eksponensial fisika*

Laju perubahan intensitas berkas radiasi terhadap ketebalan medium penyerap $x$ (dalam cm) dinyatakan oleh fungsi intensitas marginal $I'(x) = -40 e^{-0,02x}$ (dalam $\text{W}/\text{m}^2$ per cm). Pada ketebalan $50\text{ cm}$, intensitas radiasi terukur sebesar $1.200\text{ W}/\text{m}^2$. Diketahui aproksimasi nilai $e^{-1} \approx 0,368$ dan $e^{-2} \approx 0,135$. Berapakah intensitas radiasi yang lolos ketika ketebalan medium mencapai $100\text{ cm}$?

- A. $270\text{ W}/\text{m}^2$  
  <sub>Salah: Siswa lupa menambahkan nilai konstanta integrasi $C = 464$ ke dalam perhitungan akhir.</sub>
- B. $1.004\text{ W}/\text{m}^2$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada pembagian eksponen sehingga $C = 1.200 - (-736) = 1.936$ atau salah mengoperasikan nilai $C$.</sub>
- C. $600\text{ W}/\text{m}^2$  
  <sub>Salah: Siswa salah menggunakan ekstrapolasi linear dengan mengira intensitas berkurang secara proporsional tetap dari ketebalan 50 cm ke 100 cm.</sub>
- **D. $734\text{ W}/\text{m}^2$** ✅  
  <sub>Benar: $I(x) = \int -40 e^{-0,02x}\,dx = \frac{-40}{-0,02}e^{-0,02x} + C = 2.000 e^{-0,02x} + C$. Dari $I(50) = 1.200$: $2.000 e^{-1} + C = 1.200 \implies 2.000(0,368) + C = 1.200 \implies 736 + C = 1.200 \implies C = 464$. Untuk $x = 100$: $I(100) = 2.000 e^{-2} + 464 = 2.000(0,135) + 464 = 270 + 464 = 734\text{ W}/\text{m}^2$.</sub>

**Pembahasan:** Langkah 1: Menentukan rumus umum intensitas $I(x)$ melalui integrasi tak tentu:
$$I(x) = \int I'(x)\,dx = \int -40 e^{-0,02x}\,dx$$
$$I(x) = \frac{-40}{-0,02} e^{-0,02x} + C = 2.000 e^{-0,02x} + C$$

Langkah 2: Menghitung nilai konstanta integrasi $C$ dari kondisi batas $I(50) = 1.200$:
$$I(50) = 2.000 e^{-0,02(50)} + C = 1.200$$
$$2.000 e^{-1} + C = 1.200$$
$$2.000(0,368) + C = 1.200 \implies 736 + C = 1.200 \implies C = 464$$

Langkah 3: Menghitung intensitas pada ketebalan $x = 100\text{ cm}$:
$$I(100) = 2.000 e^{-0,02(100)} + 464 = 2.000 e^{-2} + 464$$
$$I(100) = 2.000(0,135) + 464 = 270 + 464 = 734\text{ W}/\text{m}^2$$
**Acuan:** siswa — siswa hal.193 Latihan Soal Integral Tak Tentu

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b03-a-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: analisis titik ekstrem fungsi antiturunan*

Grafik fungsi $y = F(x)$ merupakan antiturunan dari fungsi $f(x) = 6x^2 - 18x + 12$. Jika grafik fungsi $y = F(x)$ memiliki titik balik minimum lokal yang menyinggung sumbu-$X$, berapakah nilai ordinat dari titik balik maksimum lokal kurva tersebut?

- **A. $1$** ✅  
  <sub>Benar: $F'(x) = f(x) = 6(x - 1)(x - 2) = 0 \implies x = 1$ (maksimum lokal) dan $x = 2$ (minimum lokal). $F(x) = \int (6x^2 - 18x + 12)\,dx = 2x^3 - 9x^2 + 12x + C$. Titik balik minimum lokal di sumbu-$X \implies F(2) = 0 \implies 2(8) - 9(4) + 12(2) + C = 0 \implies 4 + C = 0 \implies C = -4$. Nilai maksimum lokal adalah $F(1) = 2(1) - 9(1) + 12(1) - 4 = 1$.</sub>
- B. $4$  
  <sub>Salah: Siswa langsung mengambil nilai $F(2) - C = 4$ sebagai nilai ordinat tanpa menghitung $F(1)$ secara utuh.</sub>
- C. $-1$  
  <sub>Salah: Siswa salah tanda saat menyelesaikan persamaan $4 + C = 0$ menjadi $C = 4$, sehingga $F(1) = 5 + 4 = 9$ atau salah mengurangkan pada $F(2)$.</sub>
- D. $5$  
  <sub>Salah: Siswa tertukar antara titik maksimum dan titik minimum, menetapkan $F(1) = 0$ sehingga $5 + C = 0 \implies C = -5$, lalu menghitung $F(2) = 4 - 5 = -1$ atau mengira nilai puncak adalah 5.</sub>

**Pembahasan:** Langkah 1: Menentukan titik kritis dari antiturunan $F(x)$.
Karena $F'(x) = f(x)$, maka:
$$F'(x) = 6x^2 - 18x + 12 = 0$$
$$6(x^2 - 3x + 2) = 0 \implies 6(x - 1)(x - 2) = 0$$
Titik kritis adalah $x = 1$ dan $x = 2$.
Berdasarkan uji turunan kedua $F''(x) = 12x - 18$:
- Untuk $x = 1$, $F''(1) = -6 < 0$ (titik balik maksimum lokal).
- Untuk $x = 2$, $F''(2) = 6 > 0$ (titik balik minimum lokal).

Langkah 2: Menentukan rumus umum fungsi $F(x)$:
$$F(x) = \int (6x^2 - 18x + 12)\,dx = 2x^3 - 9x^2 + 12x + C$$

Langkah 3: Titik balik minimum lokal menyinggung sumbu-$X$, artinya $F(2) = 0$:
$$F(2) = 2(2)^3 - 9(2)^2 + 12(2) + C = 0$$
$$16 - 36 + 24 + C = 0$$
$$4 + C = 0 \implies C = -4$$

Langkah 4: Menghitung nilai ordinat titik balik maksimum lokal di $x = 1$:
$$F(1) = 2(1)^3 - 9(1)^2 + 12(1) + (-4)$$
$$F(1) = 2 - 9 + 12 - 4 = 1$$
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b03-a-hard-bt01-010
*orisinal | C6 | 5 langkah | jenis: kombinasi substitusi dan integrasi parsial*

Suatu fungsi $f(x)$ terdiferensialkan untuk setiap bilangan real dan memenuhi persamaan turunan $f'(x) = x^3 e^{x^2}$. Jika grafik fungsi $y = f(x)$ melalui titik $(0, 1)$, berapakah nilai dari $f(2)$?

- A. $3e^4 + 3$  
  <sub>Salah: Siswa lupa mengalikan faktor $\frac{1}{2}$ yang berasal dari turunan substitusi $dt = 2x dx$.</sub>
- B. $\frac{5e^4 + 3}{2}$  
  <sub>Salah: Siswa melakukan kesalahan tanda pada integrasi parsial menjadi $(t + 1)e^t$ sehingga $(x^2 + 1) = 5$ pada $x = 2$.</sub>
- C. $\frac{3e^4 + 1}{2}$  
  <sub>Salah: Siswa mengabaikan suku $-1/2$ dari $-\frac{1}{2}e^0$ sehingga menganggap $C = 1$ bukan $\frac{3}{2}$.</sub>
- **D. $\frac{3e^4 + 3}{2}$** ✅  
  <sub>Benar: Substitusi $t = x^2 \implies dt = 2x dx$. Maka $\int x^3 e^{x^2}\,dx = \int x^2 e^{x^2} \cdot x\,dx = \frac{1}{2}\int t e^t\,dt$. Dengan integrasi parsial, $\int t e^t\,dt = t e^t - e^t + C_1$. Jadi $f(x) = \frac{1}{2}(x^2 e^{x^2} - e^{x^2}) + C = \frac{1}{2}(x^2 - 1)e^{x^2} + C$. Dari $f(0) = 1$: $\frac{1}{2}(0 - 1)e^0 + C = 1 \implies -\frac{1}{2} + C = 1 \implies C = \frac{3}{2}$. Maka $f(2) = \frac{1}{2}(4 - 1)e^4 + \frac{3}{2} = \frac{3}{2}e^4 + \frac{3}{2} = \frac{3e^4 + 3}{2}$.</sub>

**Pembahasan:** Langkah 1: Menentukan bentuk integral tak tentu dari $f'(x)$:
$$f(x) = \int x^3 e^{x^2}\,dx$$

Langkah 2: Lakukan substitusi awal. Misalkan $t = x^2$, maka $dt = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,dt$:
$$\int x^3 e^{x^2}\,dx = \int x^2 e^{x^2} (x\,dx) = \int t e^t \left(\frac{1}{2}\,dt\right) = \frac{1}{2}\int t e^t\,dt$$

Langkah 3: Terapkan integrasi parsial pada $\int t e^t\,dt$.
Misalkan $u = t \implies du = dt$ dan $dv = e^t\,dt \implies v = e^t$:
$$\int t e^t\,dt = t e^t - \int e^t\,dt = t e^t - e^t = (t - 1)e^t$$
Kembalikan ke variabel $x$:
$$f(x) = \frac{1}{2}(x^2 - 1)e^{x^2} + C$$

Langkah 4: Tentukan nilai konstanta $C$ menggunakan titik $(0, 1)$:
$$f(0) = \frac{1}{2}(0^2 - 1)e^0 + C = 1$$
$$\frac{1}{2}(-1)(1) + C = 1 \implies -\frac{1}{2} + C = 1 \implies C = \frac{3}{2}$$

Langkah 5: Evaluasi nilai $f(2)$:
$$f(2) = \frac{1}{2}(2^2 - 1)e^{2^2} + \frac{3}{2} = \frac{1}{2}(3)e^4 + \frac{3}{2} = \frac{3e^4 + 3}{2}$$
**Acuan:** siswa — siswa hal.186

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b03-a-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: evaluasi kesalahan prosedur integrasi*

Seorang siswa diminta menyelesaikan $\int \frac{x}{\sqrt{x^2 + 9}}\,dx$. Berikut adalah tahapan yang dikerjakannya:

- **Langkah 1**: Menuliskan integral ke dalam bentuk eksponen: $\int x(x^2 + 9)^{-\frac{1}{2}}\,dx$.
- **Langkah 2**: Memilih substitusi $u = x^2 + 9$, sehingga $du = 2x\,dx$ atau $x\,dx = \frac{1}{2}\,du$.
- **Langkah 3**: Mengubah bentuk integral menjadi $\frac{1}{2} \int u^{-\frac{1}{2}}\,du$.
- **Langkah 4**: Mengintegralkan terhadap $u$: $\frac{1}{2} \cdot \left(-\frac{1}{2} u^{\frac{1}{2}}\right) + C = -\frac{1}{4} \sqrt{x^2 + 9} + C$.

Berdasarkan langkah penyelesaian tersebut, pada langkah berapakah kesalahan pertama kali terjadi, dan bagaimana perbaikannya yang tepat?

- **A. Langkah 4 salah; seharusnya antiturunan dari $u^{-\frac{1}{2}}$ dikalikan $\frac{1}{-\frac{1}{2} + 1} = 2$, sehingga diperoleh $\sqrt{x^2 + 9} + C$.** ✅  
  <sub>Benar: Pada Langkah 4, siswa mengalikan dengan pangkat lama ($-\frac{1}{2}$) bukannya membagi dengan pangkat baru ($n + 1 = \frac{1}{2}$), yang seharusnya menghasilkan koefisien $\frac{1}{1/2} = 2$.</sub>
- B. Langkah 1 salah; bentuk akar pada penyebut seharusnya diubah menjadi pangkat $\frac{1}{2}$, bukan $-\frac{1}{2}$.  
  <sub>Salah: Salah memahami sifat eksponen pecahan negatif pada posisi penyebut pecahan.</sub>
- C. Langkah 3 salah; substitusi diferensial seharusnya menghasilkan pengali 2 di luar integral, yaitu $2 \int u^{-\frac{1}{2}}\,du$.  
  <sub>Salah: Kebalikan operasi pembagian konstanta saat menyatakan $x\,dx$ dalam $du$.</sub>
- D. Langkah 2 salah; diferensial dari $u = x^2 + 9$ seharusnya menghasilkan $du = x\,dx$ tanpa faktor 2.  
  <sub>Salah: Kesalahan menurunkan fungsi $x^2$ yang seharusnya berkoefisien 2.</sub>

**Pembahasan:** Evaluasi per langkah:
- Langkah 1 benar: $\frac{1}{\sqrt{x^2+9}} = (x^2+9)^{-\frac{1}{2}}$.
- Langkah 2 benar: $u = x^2+9 \implies du = 2x\,dx \implies x\,dx = \frac{1}{2}\,du$.
- Langkah 3 benar: $\int x(x^2+9)^{-\frac{1}{2}}\,dx = \int u^{-\frac{1}{2}} \left(\frac{1}{2}\,du\right) = \frac{1}{2} \int u^{-\frac{1}{2}}\,du$.
- Langkah 4 salah: Menggunakan aturan $\int u^n\,du = \frac{1}{n+1}u^{n+1}+C$ dengan $n = -\frac{1}{2}$, diperoleh $\frac{1}{-\frac{1}{2}+1} u^{-\frac{1}{2}+1} = \frac{1}{1/2} u^{1/2} = 2u^{1/2}$. Jadi, hasil sebenarnya adalah $\frac{1}{2} \cdot 2u^{1/2} + C = \sqrt{u} + C = \sqrt{x^2+9} + C$. Siswa melakukan kesalahan dengan mengalikan pangkat lama.
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b03-a-hard-bt01-012
*variasi (angka) | C5 | 4 langkah | jenis: akumulasi laju pertumbuhan sel*

Dalam 15 hari pertama bulan Januari, sebuah sel suatu tanaman bertumbuh sedemikian rupa sehingga pada $t$ hari sesudah tanggal 1 Januari, volume sel itu bertambah dengan kecepatan $(18 - t)^{-2}$ mikrometer kubik per hari. Jika pada tanggal 9 Januari volume sel itu adalah 7 mikrometer kubik, berapa volumenya pada tanggal 14 Januari?

- **A. 7,1 mikrometer kubik** ✅  
  <sub>Benar: Kecepatan pertambahan volume adalah laju perubahan volume terhadap waktu, $V'(t) = (18 - t)^{-2}$. Antiturunan dari fungsi tersebut diperoleh melalui substitusi $u = 18 - t$ sehingga $du = -dt$, menghasilkan $V(t) = \int (18 - t)^{-2}\,dt = \frac{1}{18 - t} + C$. Waktu $t$ dihitung sesudah 1 Januari: tanggal 9 Januari bersesuaian dengan $t = 9 - 1 = 8$, sehingga $V(8) = \frac{1}{18 - 8} + C = 7 \iff 0,1 + C = 7 \iff C = 6,9$. Pada tanggal 14 Januari ($t = 14 - 1 = 13$), volume sel adalah $V(13) = \frac{1}{18 - 13} + 6,9 = \frac{1}{5} + 6,9 = 0,2 + 6,9 = 7,1\text{ mikrometer kubik}$.</sub>
- B. 7,4 mikrometer kubik  
  <sub>Salah: Siswa salah mengubah pecahan $\frac{1}{5}$ menjadi desimal $0,5$ (tertukar dengan $\frac{1}{2}$), sehingga menghitung $0,5 + 6,9 = 7,4$.</sub>
- C. 7,2 mikrometer kubik  
  <sub>Salah: Siswa mengabaikan kontribusi nilai fungsi pada $t = 8$ dan langsung menambahkan nilai $\frac{1}{18 - 13} = 0,2$ ke volume 7 mikrometer kubik seolah-olah 7 adalah nilai konstanta awal.</sub>
- D. 6,9 mikrometer kubik  
  <sub>Salah: Siswa keliru tidak memperhitungkan tanda negatif dari turunan fungsi dalam ($du = -dt$) saat melakukan substitusi, sehingga memperoleh antiturunan $V(t) = -\frac{1}{18 - t} + C$, menghasilkan $C = 7,1$ dan $V(13) = -0,2 + 7,1 = 6,9$.</sub>

**Pembahasan:** Langkah-langkah penyelesaian:
1. Tentukan rumus fungsi volume $V(t)$:
$$\frac{dV}{dt} = (18 - t)^{-2}$$
$$V(t) = \int (18 - t)^{-2}\,dt$$
Misalkan $u = 18 - t$, maka $du = -dt$ atau $dt = -du$.
$$V(t) = \int u^{-2}(-du) = -\left(-u^{-1}\right) + C = \frac{1}{18 - t} + C$$

2. Tentukan nilai $t$ untuk tanggal 9 Januari:
Karena $t$ menyatakan hari sesudah 1 Januari, maka pada tanggal 9 Januari berlaku $t = 9 - 1 = 8$.
Diketahui $V(8) = 7$:
$$\frac{1}{18 - 8} + C = 7$$
$$\frac{1}{10} + C = 7$$
$$0,1 + C = 7 \implies C = 6,9$$

3. Tentukan fungsi volume sel secara lengkap:
$$V(t) = \frac{1}{18 - t} + 6,9$$

4. Hitung volume sel pada tanggal 14 Januari ($t = 14 - 1 = 13$):
$$V(13) = \frac{1}{18 - 13} + 6,9 = \frac{1}{5} + 6,9 = 0,2 + 6,9 = 7,1\text{ mikrometer kubik}$$

Jadi, volume sel pada tanggal 14 Januari adalah 7,1 mikrometer kubik.
**Acuan:** pretest — kelas12_tl-b03-p0193-latihan-soal-integral-tak-tentu-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b03-a-hard-bt01-013
*orisinal | C5 | 5 langkah | jenis: rekonstruksi polinomial antiturunan*

Diketahui turunan pertama fungsi $F(x)$ adalah $F'(x) = 6x^2 - 6(a + 1)x + 6a$ dengan $a$ merupakan suatu konstanta real di mana $a > 1$. Jika selisih antara nilai balik maksimum lokal dan nilai balik minimum lokal dari kurva $y = F(x)$ adalah $27$, tentukan nilai dari konstanta $a$.

- A. 5  
  <sub>Salah: Siswa salah menghitung pengali koefisien polinomial sehingga memperoleh (a - 1)^3 = 64.</sub>
- B. 3  
  <sub>Salah: Siswa menganggap a = 3 dari hasil akar kubik 27 tanpa menambahkan 1.</sub>
- C. 2  
  <sub>Salah: Siswa menyamakan (a - 1)^3 = 1 bukan 27, atau salah mengakar pangkat tiga.</sub>
- **D. 4** ✅  
  <sub>Benar: F'(x) = 6(x - 1)(x - a) = 0 menghasilkan titik kritis x = 1 (maksimum) dan x = a (minimum). Selisih nilai ekstremnya adalah F(1) - F(a) = (a - 1)^3 = 27 sehingga a - 1 = 3, maka a = 4.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Menentukan titik stasioner:
$F'(x) = 6(x^2 - (a + 1)x + a) = 6(x - 1)(x - a) = 0$.
Karena $a > 1$, uji tanda turunan menunjukkan bahwa $F(x)$ mencapai maksimum lokal di $x = 1$ dan minimum lokal di $x = a$.
2. Menentukan rumus antiturunan $F(x)$:
$$F(x) = \int [6x^2 - 6(a + 1)x + 6a]\,dx = 2x^3 - 3(a + 1)x^2 + 6ax + C$$
3. Menghitung nilai fungsi di titik stasioner:
- $F(1) = 2 - 3(a + 1) + 6a + C = 3a - 1 + C$
- $F(a) = 2a^3 - 3(a + 1)a^2 + 6a^2 + C = -a^3 + 3a^2 + C$
4. Selisih nilai ekstrem:
$$F(1) - F(a) = (3a - 1 + C) - (-a^3 + 3a^2 + C) = a^3 - 3a^2 + 3a - 1 = (a - 1)^3$$
5. Menyelesaikan persamaan:
$$(a - 1)^3 = 27 \implies a - 1 = 3 \implies a = 4$$
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b03-a-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: analisis titik belok kurva antiturunan*

Turunan kedua suatu fungsi polinomial dinyatakan oleh $f''(x) = 12x - 18$ untuk setiap bilangan real $x$. Kurva $y = f(x)$ memiliki titik belok di mana garis singgung kurva di titik tersebut merupakan garis horizontal $y = 5$. Nilai dari $f(0)$ adalah ....

- A. $\frac{7}{4}$  
  <sub>Salah: Siswa salah tanda saat memindahkan ruas konstanta integrasi kedua.</sub>
- B. $5$  
  <sub>Salah: Siswa keliru mengira f(0) sama dengan ordinat garis singgung horizontal.</sub>
- **C. $-\frac{7}{4}$** ✅  
  <sub>Benar: Titik belok terjadi di f''(x) = 0 yaitu x = 3/2. Garis singgung horizontal berarti f'(3/2) = 0, menghasilkan C1 = 27/2. Kurva melalui (3/2, 5) menghasilkan f(0) = C2 = -7/4.</sub>
- D. $-\frac{27}{4}$  
  <sub>Salah: Siswa lupa memperhitungkan nilai y = 5 dan langsung menggunakan C2 = -f(3/2) tanpa konstanta.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Menentukan absis titik belok:
$$f''(x) = 0 \implies 12x - 18 = 0 \implies x = \frac{3}{2}$$
2. Menentukan fungsi turunan pertama $f'(x)$:
$$f'(x) = \int (12x - 18)\,dx = 6x^2 - 18x + C_1$$
Karena garis singgung di titik belok horizontal, maka gradiennya nol:
$$f'\left(\frac{3}{2}\right) = 0 \implies 6\left(\frac{9}{4}\right) - 18\left(\frac{3}{2}\right) + C_1 = 0 \implies \frac{27}{2} - 27 + C_1 = 0 \implies C_1 = \frac{27}{2}$$
3. Menentukan fungsi $f(x)$:
$$f(x) = \int \left(6x^2 - 18x + \frac{27}{2}\right)dx = 2x^3 - 9x^2 + \frac{27}{2}x + C_2$$
4. Titik belok berada pada garis $y = 5$, sehingga $f(3/2) = 5$:
$$2\left(\frac{27}{8}\right) - 9\left(\frac{9}{4}\right) + \frac{27}{2}\left(\frac{3}{2}\right) + C_2 = 5$$
$$\frac{27}{4} - \frac{81}{4} + \frac{81}{4} + C_2 = 5 \implies \frac{27}{4} + C_2 = 5 \implies C_2 = 5 - \frac{27}{4} = -\frac{7}{4}$$
5. Nilai $f(0) = C_2 = -\frac{7}{4}$.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b03-a-hard-bt01-015
*orisinal | C5 | 4 langkah | jenis: evaluasi batas nilai antiturunan aljabar*

Fungsi $F(x)$ merupakan antiturunan dari $f(x) = (3x - 1)(x + 2)$. Garis lurus $g: y = 4x - 7$ memotong kurva $y = F(x)$ tepat di titik potong kurva tersebut dengan sumbu-$y$. Nilai dari $2 \cdot F(2)$ adalah ....

- A. 7  
  <sub>Salah: Siswa lupa mengalikan dengan faktor 2 di akhir soal.</sub>
- B. 28  
  <sub>Salah: Siswa salah mengintegralkan suku 5x menjadi 5x^2 bukan (5/2)x^2.</sub>
- **C. 14** ✅  
  <sub>Benar: f(x) = 3x^2 + 5x - 2, sehingga F(x) = x^3 + (5/2)x^2 - 2x + C. Titik potong sumbu-y adalah (0, -7) sehingga C = -7. F(2) = 7, sehingga 2 * F(2) = 14.</sub>
- D. 0  
  <sub>Salah: Siswa mengabaikan konstanta C = -7 sehingga F(2) menjadi 14 - 14 = 0.</sub>

**Pembahasan:** Langkah penyelesaian:
1. Menjabarkan integran:
$$f(x) = (3x - 1)(x + 2) = 3x^2 + 5x - 2$$
2. Mengintegralkan $f(x)$ untuk memperoleh $F(x)$:
$$F(x) = \int (3x^2 + 5x - 2)\,dx = x^3 + \frac{5}{2}x^2 - 2x + C$$
3. Menentukan konstanta $C$:
Titik potong garis $y = 4x - 7$ dengan sumbu-$y$ ($x = 0$) adalah $(0, -7)$. Karena kurva memotong garis di titik potong sumbu-$y$, maka $F(0) = -7 \implies C = -7$.
Rumus fungsi: $F(x) = x^3 + \frac{5}{2}x^2 - 2x - 7$.
4. Menghitung $F(2)$ dan $2 \cdot F(2)$:
$$F(2) = 2^3 + \frac{5}{2}(2^2) - 2(2) - 7 = 8 + 10 - 4 - 7 = 7$$
$$2 \cdot F(2) = 2 \cdot 7 = 14$$
**Acuan:** siswa — siswa hal.185

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b03-a-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: kinematika gerak partikel trigonometri*

Sebuah partikel bergerak pada suatu garis lurus dengan arah positif ke kanan dari titik pusat. Kecepatan partikel dinyatakan oleh persamaan $v(t) = 6\cos(3\pi t)$ (dalam cm/detik). Jika pada saat awal ($t = 0$) partikel berada pada posisi $4\text{ cm}$ di sebelah kanan titik pusat, berapakah posisi partikel pada saat $t = \frac{1}{2}$ detik?

- A. $4\text{ cm}$  
  <sub>Salah: Mengira sin(3pi/2) = 0 sehingga suku trigonometri lenyap.</sub>
- **B. $\left(4 - \frac{2}{\pi}\right)\text{ cm}$** ✅  
  <sub>Benar: $s(t) = \int 6\cos(3\pi t)\,dt = \frac{2}{\pi}\sin(3\pi t) + C$. Kondisi $s(0) = 4 \implies C = 4$. Saat $t = 1/2$, $s(1/2) = \frac{2}{\pi}\sin(3\pi/2) + 4 = 4 - \frac{2}{\pi}$.</sub>
- C. $\left(4 + \frac{2}{\pi}\right)\text{ cm}$  
  <sub>Salah: Salah menentukan tanda sin(3pi/2) menjadi +1 bukan -1.</sub>
- D. $\left(4 - \frac{6}{\pi}\right)\text{ cm}$  
  <sub>Salah: Lupa membagi koefisien dengan 3 saat mengintegralkan cos(3pi t).</sub>

**Pembahasan:** Posisi $s(t) = \int v(t)\,dt = \int 6\cos(3\pi t)\,dt = \frac{6}{3\pi}\sin(3\pi t) + C = \frac{2}{\pi}\sin(3\pi t) + C$. Karena $s(0) = 4$, diperoleh $0 + C = 4 \implies C = 4$. Pada saat $t = \frac{1}{2}$, $s\left(\frac{1}{2}\right) = \frac{2}{\pi}\sin\left(\frac{3\pi}{2}\right) + 4 = \frac{2}{\pi}(-1) + 4 = 4 - \frac{2}{\pi}\text{ cm}$.
**Acuan:** siswa — siswa hal.190 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b03-a-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: evaluasi kesetaraan integrasi parsial*

Jika $\int x^2 \cos x\,dx = (x^2 + a)\sin x + bx\cos x + C$, dengan $a$ dan $b$ merupakan bilangan bulat serta $C$ konstanta integrasi, maka nilai dari $a - b$ adalah ....

- **A. $-4$** ✅  
  <sub>Benar: Integrasi parsial menghasilkan $(x^2 - 2)\sin x + 2x\cos x + C$, sehingga $a = -2$ dan $b = 2$, maka $a - b = -2 - 2 = -4$.</sub>
- B. $-2$  
  <sub>Salah: Menghitung hanya nilai a saja dan mengabaikan suku -b.</sub>
- C. $0$  
  <sub>Salah: Menganggap a = 2 dan b = 2 karena kesalahan tanda pada antiturunan pertama.</sub>
- D. $4$  
  <sub>Salah: Terbalik tanda sehingga memperoleh a = 2 dan b = -2.</sub>

**Pembahasan:** Gunakan integrasi parsial bertahap:
1. Misalkan $u = x^2, dv = \cos x\,dx \implies du = 2x\,dx, v = \sin x$.
Maka $\int x^2\cos x\,dx = x^2\sin x - \int 2x\sin x\,dx$.
2. Untuk $\int 2x\sin x\,dx$, misalkan $u_1 = 2x, dv_1 = \sin x\,dx \implies du_1 = 2\,dx, v_1 = -\cos x$.
$\int 2x\sin x\,dx = -2x\cos x - \int (-2\cos x)\,dx = -2x\cos x + 2\sin x$.
3. Gabungkan kedua hasil:
$\int x^2\cos x\,dx = x^2\sin x - (-2x\cos x + 2\sin x) + C = (x^2 - 2)\sin x + 2x\cos x + C$.
Dengan demikian, $a = -2$ dan $b = 2$. Maka nilai $a - b = -2 - 2 = -4$.
**Acuan:** siswa — siswa hal.191

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b03-a-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: evaluasi validitas prosedur integral*

Diberikan penyelesaian seorang siswa dalam menentukan $\int x(x - 3)^5\,dx$ berikut:
- **Langkah 1**: Menuliskan $x = (x - 3) + 3$, sehingga bentuk integral menjadi $\int [(x - 3) + 3](x - 3)^5\,dx$.
- **Langkah 2**: Mengalikan ke dalam tanda kurung menjadi $\int \left((x - 3)^6 + 3(x - 3)^5\right)\,dx$.
- **Langkah 3**: Memisahkan menjadi dua integral: $\int (x - 3)^6\,dx + 3\int (x - 3)^5\,dx$.
- **Langkah 4**: Mengintegralkan masing-masing suku menjadi $\frac{1}{6}(x - 3)^7 + \frac{3}{5}(x - 3)^6 + C$.
- **Langkah 5**: Menuliskan hasil akhir $\frac{1}{6}(x - 3)^7 + \frac{3}{5}(x - 3)^6 + C$.

Berdasarkan tahapan penyelesaian tersebut, pada langkah keberapakah kesalahan pertama kali terjadi, dan bagaimana perbaikannya yang tepat?

- A. Langkah 2 salah; operasi distributif gagal karena $(x - 3)^5$ tidak boleh dikalikan suku per suku.  
  <sub>Salah: Distribusi perkalian terhadap penjumlahan bersifat valid secara aljabar.</sub>
- B. Langkah 1 salah; manipulasi aljabar $x = (x - 3) + 3$ tidak sah dalam integrasi tak tentu.  
  <sub>Salah: Manipulasi aljabar tersebut sah dan sering digunakan untuk teknik integrasi substitusi aljabar.</sub>
- C. Langkah 3 salah; sifat kelinearan integral tak tentu hanya berlaku jika variabelnya berbentuk $x$ tunggal bukan $(x - 3)$.  
  <sub>Salah: Sifat penjumlahan integral berlaku untuk sembarang fungsi f1 dan f2 pada interval yang sama.</sub>
- **D. Langkah 4 salah; seharusnya hasil pengintegralan suku pertama adalah $\frac{1}{7}(x - 3)^7$ dan suku kedua $\frac{1}{2}(x - 3)^6 + C$.** ✅  
  <sub>Benar: Aturan pangkat menyatakan $\int u^n\,du = \frac{1}{n+1}u^{n+1}$. Untuk pangkat 6 menjadi pembagi 7, dan untuk $3\int (x-3)^5\,dx$ menjadi $3 \cdot \frac{1}{6}(x-3)^6 = \frac{1}{2}(x-3)^6$. Siswa tidak menambahkan 1 pada penyebut di suku-suku tersebut.</sub>

**Pembahasan:** Mari kita tinjau setiap langkah:
- Langkah 1: Mengubah $x$ menjadi $(x - 3) + 3$ adalah manipulasi aljabar yang benar.
- Langkah 2: Mengalikan ke dalam kurung menjadi $(x - 3)^6 + 3(x - 3)^5$ adalah benar secara distributif.
- Langkah 3: Menggunakan sifat linear integral $\int (f + g)\,dx = \int f\,dx + \int g\,dx$ adalah benar.
- Langkah 4: Menggunakan aturan integral substitusi $u = x - 3 \implies du = dx$:
  $\int (x - 3)^6\,dx = \frac{1}{7}(x - 3)^7$
  $3\int (x - 3)^5\,dx = 3 \cdot \frac{1}{6}(x - 3)^6 = \frac{1}{2}(x - 3)^6$.
Siswa menuliskan penyebut 6 dan 5 (bukan $n+1$), sehingga Langkah 4 memuat kesalahan pertama.
**Acuan:** siswa — siswa hal.182

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
