# Lembar koreksi — kelas11_tl SMA11L-B6 subbab A: Fungsi Logaritma

60 soal | easy 20, medium 20, hard 20 | variasi 28, orisinal 32

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11_tl-b06-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: evaluasi fungsi logaritma*

Diberikan fungsi logaritma $f(x) = {}^5\log x$. Nilai dari $f(125)$ adalah ....

- **A. $3$** ✅  
  <sub>Benar: Substitusi $x = 125$ menghasilkan $f(125) = {}^5\log 125 = {}^5\log(5^3) = 3$.</sub>
- B. $5$  
  <sub>Salah: Siswa mengira hasilnya adalah basis fungsi logaritma itu sendiri.</sub>
- C. $4$  
  <sub>Salah: Siswa salah menghitung perpangkatan, mengira $5^4 = 125$.</sub>
- D. $25$  
  <sub>Salah: Siswa membagi 125 dengan basis 5 ($125 : 5 = 25$), bukan mencari pangkatnya.</sub>

**Pembahasan:** Berdasarkan definisi fungsi logaritma:
$f(x) = {}^5\log x$
$f(125) = {}^5\log 125$
Karena $5^3 = 125$, maka:
$f(125) = 3$
**Acuan:** siswa — siswa hal.261 Contoh 6.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11_tl-b06-a-easy-bt01-002
*variasi (angka) | C2 | 1 langkah | jenis: aplikasi pH logaritma*

Larutan cuka memiliki konsentrasi ion hidrogen sebesar $10^{-2,8}$. Jika $\text{pH} = -\log[\text{H}^+]$, nilai pH larutan cuka tersebut adalah ....

- A. $0,28$  
  <sub>Salah: Siswa salah membagi eksponen dengan 10.</sub>
- **B. $2,8$** ✅  
  <sub>Benar: $\text{pH} = -\log(10^{-2,8}) = -(-2,8) = 2,8$.</sub>
- C. $7,2$  
  <sub>Salah: Siswa mengurangkan nilai dari skala netral atau basa ($10 - 2,8 = 7,2$).</sub>
- D. $-2,8$  
  <sub>Salah: Siswa lupa mengalikan dengan tanda negatif pada rumus pH.</sub>

**Pembahasan:** Diketahui $[\text{H}^+] = 10^{-2,8}$.
$\text{pH} = -\log[\text{H}^+]$
$\text{pH} = -\log(10^{-2,8})$
$\text{pH} = -(-2,8) = 2,8$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11_tl-b06-a-easy-bt01-003
*orisinal | C1 | 1 langkah | jenis: daerah asal fungsi logaritma*

Daerah asal (domain) dari fungsi logaritma $f(x) = {}^7\log x$ adalah ....

- A. himpunan semua bilangan bulat positif  
  <sub>Salah: Siswa mengira input hanya boleh berupa bilangan bulat (cacah).</sub>
- B. himpunan semua bilangan real  
  <sub>Salah: Siswa tertukar antara daerah asal dengan daerah hasil (range).</sub>
- C. himpunan semua bilangan real bukan nol  
  <sub>Salah: Siswa mengira bilangan negatif diperbolehkan asalkan bukan nol.</sub>
- **D. himpunan semua bilangan real positif** ✅  
  <sub>Benar: Sesuai karakteristik fungsi logaritma $f(x) = {}^a\log x$, nilai numerus $x$ harus berupa bilangan real positif ($x > 0$).</sub>

**Pembahasan:** Berdasarkan karakteristik fungsi logaritma $f(x) = {}^a\log x$, grafik fungsi hanya terdefinisi untuk nilai $x > 0$. Dengan demikian, daerah asalnya adalah himpunan semua bilangan real positif.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11_tl-b06-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: definisi fungsi logaritma*

Fungsi logaritma alami dinotasikan dengan $f(x) = \ln x$. Basis dari fungsi logaritma tersebut adalah ....

- A. $2$  
  <sub>Salah: Siswa mengira basis logaritma alami menggunakan basis biner 2.</sub>
- B. $0$  
  <sub>Salah: Siswa mengira logaritma alami tidak memiliki basis atau berbobot 0.</sub>
- **C. $e$ (dengan $e \approx 2,7183$)** ✅  
  <sub>Benar: Berdasarkan definisi fungsi logaritma alami, $\ln x$ merupakan logaritma dengan bilangan pokok/basis $e \approx 2,7183$.</sub>
- D. $10$  
  <sub>Salah: Siswa tertukar dengan basis logaritma umum.</sub>

**Pembahasan:** Fungsi logaritma dengan basis $e \approx 2,7183$ disebut fungsi logaritma alami dan dinotasikan dengan $f(x) = \ln x = {}^e\log x$. Jadi, basisnya adalah $e$.
**Acuan:** siswa — siswa hal.261

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11_tl-b06-a-easy-bt01-005
*variasi (angka) | C2 | 1 langkah | jenis: sifat pembagian logaritma*

Berdasarkan sifat logaritma, logaritma hasil bagi dua bilangan sama dengan pengurangan dari logaritma kedua bilangan tersebut. Bentuk yang senilai dengan ${}^4\log\left(\frac{67}{9}\right)$ adalah ....

- A. ${}^4\log 67 + {}^4\log 9$  
  <sub>Salah: Tertukar dengan sifat perkalian logaritma.</sub>
- **B. ${}^4\log 67 - {}^4\log 9$** ✅  
  <sub>Benar: Sesuai Sifat 6.2, ${}^b\log\left(\frac{M}{N}\right) = {}^b\log M - {}^b\log N$, sehingga ${}^4\log\left(\frac{67}{9}\right) = {}^4\log 67 - {}^4\log 9$.</sub>
- C. \frac{{}^4\log 67}{{}^4\log 9}$  
  <sub>Salah: Keliru menganggap logaritma pembagian sama dengan pembagian dua logaritma.</sub>
- D. ${}^4\log(67 - 9)$  
  <sub>Salah: Keliru mengurangkan numerus di dalam satu tanda logaritma.</sub>

**Pembahasan:** Berdasarkan sifat identitas logaritma:
$${}^b\log\left(\frac{M}{N}\right) = {}^b\log M - {}^b\log N$$
Dengan $b = 4$, $M = 67$, dan $N = 9$, diperoleh:
$${}^4\log\left(\frac{67}{9}\right) = {}^4\log 67 - {}^4\log 9$$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11_tl-b06-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: basis dan nilai fungsi logaritma*

Diberikan fungsi logaritma $f(x) = {}^6\log x$. Nilai basis dari fungsi tersebut dan nilai dari $f(36)$ berturut-turut adalah ....

- A. $6$ dan $12$  
  <sub>Salah: Mengalikan $6$ dengan $2$ alih-alih menghitung nilai eksponen.</sub>
- **B. $6$ dan $2$** ✅  
  <sub>Benar: Basis fungsi $f(x) = {}^6\log x$ adalah $6$, dan $f(36) = {}^6\log 36 = 2$ karena $6^2 = 36$.</sub>
- C. $6$ dan $6$  
  <sub>Salah: Membagi $36$ dengan basis $6$ alih-alih mencari pangkat logaritma.</sub>
- D. $36$ dan $2$  
  <sub>Salah: Tertukar antara nilai basis dengan nilai numerus.</sub>

**Pembahasan:** Berdasarkan notasi fungsi logaritma $f(x) = {}^b\log x$, basis fungsi logaritma tersebut adalah $b = 6$.
Untuk mencari nilai $f(36)$:
$$f(36) = {}^6\log 36$$
Karena $6^2 = 36$, maka ${}^6\log 36 = 2$.
Jadi, basis fungsi adalah $6$ dan nilai $f(36) = 2$.
**Acuan:** siswa — siswa hal.272 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11_tl-b06-a-easy-bt01-007
*variasi (angka) | C2 | 1 langkah | jenis: aplikasi pH logaritma*

Jika suatu larutan memiliki konsentrasi ion hidrogen sebesar $10^{-4,6}$, nilai pH larutan tersebut adalah ....

- A. $0,46$  
  <sub>Salah: Membagi eksponen dengan 10 tanpa dasar konsep.</sub>
- B. $46$  
  <sub>Salah: Kesalahan pergeseran tanda koma desimal.</sub>
- **C. $4,6$** ✅  
  <sub>Benar: $\text{pH} = -\log[\text{H}^+] = -\log(10^{-4,6}) = -(-4,6) = 4,6$.</sub>
- D. $-4,6$  
  <sub>Salah: Lupa mengalikan dengan tanda negatif pada rumus pH.</sub>

**Pembahasan:** Nilai pH dirumuskan sebagai:
$$\text{pH} = -\log[\text{H}^+]$$
Diketahui $[\text{H}^+] = 10^{-4,6}$, maka:
$$\text{pH} = -\log(10^{-4,6}) = -(-4,6) = 4,6$$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11_tl-b06-a-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: asimtot fungsi logaritma*

Persamaan asimtot tegak dari grafik fungsi logaritma $f(x) = {}^3\log x$ adalah ....

- A. $y = 0$  
  <sub>Salah: Keliru menyamakan asimtot tegak dengan asimtot datar (sumbu-x).</sub>
- B. $x = 1$  
  <sub>Salah: Tertukar dengan absis titik potong grafik terhadap sumbu-x.</sub>
- C. $y = 1$  
  <sub>Salah: Salah konsep menentukan garis asimtot.</sub>
- **D. $x = 0$** ✅  
  <sub>Benar: Grafik fungsi logaritma $f(x) = {}^a\log x$ mendekati tetapi tidak pernah menyentuh sumbu-$y$, sehingga garis $x = 0$ (sumbu-$y$) merupakan asimtot tegaknya.</sub>

**Pembahasan:** Berdasarkan karakteristik fungsi logaritma $f(x) = {}^a\log x$, grafik fungsi mendekati sumbu-$y$ saat nilai $x$ mendekati nol dari kanan, tetapi kurva tidak pernah memotong atau menyentuh sumbu-$y$. Dengan demikian, sumbu-$y$ yang berpersamaan $x = 0$ merupakan asimtot tegak grafik fungsi tersebut.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11_tl-b06-a-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: titik potong grafik logaritma*

Grafik fungsi logaritma $f(x) = {}^4\log x$ memotong sumbu-$x$ di titik ....

- **A. $(1, 0)$** ✅  
  <sub>Benar: Titik potong sumbu-$x$ terjadi saat $f(x) = 0$, yaitu ${}^4\log x = 0 \iff x = 4^0 = 1$, sehingga koordinatnya $(1, 0)$.</sub>
- B. $(0, 0)$  
  <sub>Salah: Keliru menganggap grafik melewati titik pusat koordinat.</sub>
- C. $(4, 0)$  
  <sub>Salah: Keliru mengira absis titik potong bernilai sama dengan basis logaritma.</sub>
- D. $(0, 1)$  
  <sub>Salah: Tertukar antara nilai absis dan ordinat.</sub>

**Pembahasan:** Grafik fungsi memotong sumbu-$x$ jika $y = f(x) = 0$.
$${}^4\log x = 0 \iff x = 4^0 = 1$$
Jadi, grafik memotong sumbu-$x$ tepat di titik $(1, 0)$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11_tl-b06-a-easy-bt01-010
*variasi (angka) | C2 | 1 langkah | jenis: sifat pembagian logaritma*

Logaritma hasil bagi dari dua bilangan sama dengan pengurangan dari logaritma kedua bilangan tersebut. Berdasarkan sifat tersebut, bentuk yang setara dengan ${}^{6}\log\left(\frac{745}{8}\right)$ adalah ....

- A. ${}^{6}\log 745 + {}^{6}\log 8$  
  <sub>Salah: Tertukar sifat perkalian dengan sifat pembagian.</sub>
- B. $\frac{{}^{6}\log 745}{{}^{6}\log 8}$  
  <sub>Salah: Mengira logaritma pembagian sama dengan pembagian antarlogaritma.</sub>
- **C. ${}^{6}\log 745 - {}^{6}\log 8$** ✅  
  <sub>Benar: Berdasarkan sifat identitas logaritma ${}^b\log\left(\frac{M}{N}\right) = {}^b\log M - {}^b\log N$, maka ${}^6\log\left(\frac{745}{8}\right) = {}^6\log 745 - {}^6\log 8$.</sub>
- D. ${}^{6}\log 745 \times {}^{6}\log 8$  
  <sub>Salah: Keliru mengalikan kedua bentuk logaritma.</sub>

**Pembahasan:** Berdasarkan identitas logaritma Sifat 6.2:
$${}^b\log\left(\frac{M}{N}\right) = {}^b\log M - {}^b\log N$$
Dengan $b = 6$, $M = 745$, dan $N = 8$, didapatkan:
$${}^6\log\left(\frac{745}{8}\right) = {}^6\log 745 - {}^6\log 8$$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11_tl-b06-a-easy-bt01-011
*orisinal | C1 | 1 langkah | jenis: daerah hasil fungsi logaritma*

Daerah hasil (range) dari fungsi logaritma $f(x) = {}^4\log x$ adalah ....

- A. himpunan semua bilangan bulat  
  <sub>Salah: Mengira output fungsi logaritma selalu bilangan bulat diskret.</sub>
- B. himpunan semua bilangan real positif  
  <sub>Salah: Tertukar dengan daerah asal (domain) fungsi logaritma.</sub>
- **C. himpunan semua bilangan real** ✅  
  <sub>Benar: Berdasarkan Sifat 6.1 buku teks, daerah hasil dari fungsi logaritma $f(x) = {}^a\log x$ untuk basis sembarang adalah himpunan semua bilangan real.</sub>
- D. himpunan semua bilangan real negatif  
  <sub>Salah: Mengira grafik logaritma hanya menghasilkan nilai negatif.</sub>

**Pembahasan:** Berdasarkan Sifat 6.1 (Karakteristik Fungsi Logaritma):
1. Daerah asal $f$ adalah himpunan semua bilangan real positif ($x > 0$).
2. Daerah hasil $f$ adalah himpunan semua bilangan real ($\mathbb{R}$).
Dengan demikian, daerah hasil dari $f(x) = {}^4\log x$ adalah himpunan semua bilangan real.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11_tl-b06-a-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: kemonotonan fungsi logaritma*

Diberikan fungsi logaritma $f(x) = {}^{\frac{1}{5}}\log x$. Karakteristik kemonotonan dari grafik fungsi tersebut adalah ....

- A. monoton naik  
  <sub>Salah: Karakteristik untuk basis $a > 1$.</sub>
- B. monoton naik kemudian turun  
  <sub>Salah: Menyamakan dengan karakteristik fungsi kuadrat.</sub>
- C. konstan  
  <sub>Salah: Mengira grafik berupa garis lurus mendatar.</sub>
- **D. monoton turun** ✅  
  <sub>Benar: Karena basisnya $a = \frac{1}{5}$ berada pada interval $0 < a < 1$, fungsi logaritma tersebut bersifat monoton turun.</sub>

**Pembahasan:** Berdasarkan Sifat 6.1, untuk fungsi logaritma dengan bentuk $f(x) = {}^a\log x$:
- Jika $a > 1$, fungsinya monoton naik.
- Jika $0 < a < 1$, fungsinya monoton turun.
Karena pada fungsi $f(x) = {}^{\frac{1}{5}}\log x$ nilai basis $a = \frac{1}{5}$ (memenuhi $0 < a < 1$), maka grafik fungsi tersebut bersifat monoton turun.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11_tl-b06-a-easy-bt01-013
*variasi (angka) | C2 | 1 langkah | jenis: evaluasi fungsi logaritma pangkat*

Diberikan fungsi logaritma $f(x) = {}^4\log x$. Nilai dari $f(64)$ adalah ....

- **A. $3$** ✅  
  <sub>Benar: Berdasarkan definisi fungsi logaritma, $f(64) = {}^4\log 64 = 3$ karena $4^3 = 64$.</sub>
- B. $2$  
  <sub>Salah: Siswa mengira nilai logaritma adalah akar kuadrat dari basis atau keliru dengan perpangkatan 8.</sub>
- C. $4$  
  <sub>Salah: Siswa salah menghitung perpangkatan dengan mengira $4^4 = 64$.</sub>
- D. $16$  
  <sub>Salah: Siswa membagi nilai input dengan basis: $64 : 4 = 16$.</sub>

**Pembahasan:** Substitusikan $x = 64$ ke dalam rumus fungsi:
$$f(64) = {}^4\log 64$$
Karena $4^3 = 64$, maka ${}^4\log 64 = 3$.
Jadi, nilai dari $f(64)$ adalah $3$.
**Acuan:** siswa — siswa hal.261 Contoh 6.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11_tl-b06-a-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: basis dan operasi nilai fungsi*

Diberikan fungsi logaritma $f(x) = {}^7\log x$. Basis dari fungsi tersebut serta nilai dari $f(1) + f(7)$ berturut-turut adalah ....

- A. $7$ dan $2$  
  <sub>Salah: Siswa keliru menganggap ${}^7\log 1 = 1$ sehingga menghasilkan $1 + 1 = 2$.</sub>
- **B. $7$ dan $1$** ✅  
  <sub>Benar: Basis fungsi adalah $7$, serta $f(1) + f(7) = {}^7\log 1 + {}^7\log 7 = 0 + 1 = 1$.</sub>
- C. $7$ dan $0$  
  <sub>Salah: Siswa keliru menganggap nilai ${}^7\log 7 = 0$.</sub>
- D. $1$ dan $7$  
  <sub>Salah: Siswa menukar posisi antara nilai basis dengan hasil operasi nilai fungsi.</sub>

**Pembahasan:** Dari rumus fungsi $f(x) = {}^7\log x$, diperoleh basisnya adalah $7$.
Selanjutnya, tentukan nilai fungsi:
$$f(1) = {}^7\log 1 = 0$$
$$f(7) = {}^7\log 7 = 1$$
Maka, nilai dari $f(1) + f(7) = 0 + 1 = 1$.
Jadi, basis dari fungsi tersebut serta nilai dari $f(1) + f(7)$ berturut-turut adalah $7$ dan $1$.
**Acuan:** siswa — siswa hal.272 Latihan A

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11_tl-b06-a-easy-bt01-015
*orisinal | C1 | 1 langkah | jenis: identitas perkalian logaritma*

Berdasarkan sifat identitas logaritma, bentuk yang setara dengan ${}^3\log(9 \times 27)$ adalah ....

- **A. ${}^3\log 9 + {}^3\log 27$** ✅  
  <sub>Benar: Sesuai identitas logaritma perkalian: ${}^b\log(MN) = {}^b\log M + {}^b\log N$.</sub>
- B. ${}^3\log(9 + 27)$  
  <sub>Salah: Siswa keliru menjumlahkan numerus di dalam satu logaritma.</sub>
- C. ${}^3\log 9 - {}^3\log 27$  
  <sub>Salah: Siswa tertukar dengan sifat pembagian logaritma.</sub>
- D. ${}^3\log 9 \times {}^3\log 27$  
  <sub>Salah: Siswa keliru mempertahankan operasi perkalian antar-logaritma.</sub>

**Pembahasan:** Berdasarkan Sifat 6.2 (Identitas Logaritma):
$${}^b\log(MN) = {}^b\log M + {}^b\log N$$
Dengan $b = 3$, $M = 9$, dan $N = 27$, diperoleh:
$${}^3\log(9 \times 27) = {}^3\log 9 + {}^3\log 27$$
Jadi, bentuk yang setara adalah ${}^3\log 9 + {}^3\log 27$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11_tl-b06-a-easy-bt01-016
*variasi (angka) | C2 | 1 langkah | jenis: pemodelan skala richter*

Gempa bumi di suatu wilayah memiliki intensitas sebesar $10^5$ kali intensitas gempa bumi tingkat nol ($I_0$). Berdasarkan rumus skala Richter $M = \log\left(\frac{I}{I_0}\right)$, besar kekuatan gempa bumi tersebut adalah ....

- A. $\frac{1}{5}$ skala Richter  
  <sub>Salah: Keliru membalik pangkat menjadi pecahan.</sub>
- **B. $5$ skala Richter** ✅  
  <sub>Benar: Substitusi $I = 10^5 I_0$ menghasilkan $M = \log(10^5) = 5$.</sub>
- C. $50$ skala Richter  
  <sub>Salah: Mengalikan basis 10 dengan pangkat 5.</sub>
- D. $10$ skala Richter  
  <sub>Salah: Mengambil basis 10 dan mengabaikan eksponennya.</sub>

**Pembahasan:** Diketahui intensitas gempa $I = 10^5 I_0$. Menggunakan rumus skala Richter:
$$M = \log\left(\frac{I}{I_0}\right) = \log\left(\frac{10^5 I_0}{I_0}\right) = \log(10^5) = 5$$
Jadi, kekuatan gempa bumi tersebut adalah $5$ skala Richter.
**Acuan:** siswa — siswa hal.270 Contoh 6.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11_tl-b06-a-easy-bt01-017
*variasi (angka) | C2 | 1 langkah | jenis: perhitungan kekuatan gempa*

Sebuah instrumen seismik mencatat intensitas suatu gempa bumi adalah $10^8$ kali intensitas gempa tingkat nol ($I_0$). Kekuatan gempa bumi tersebut menurut skala Richter $M = \log\left(\frac{I}{I_0}\right)$ adalah ....

- A. $4$ skala Richter  
  <sub>Salah: Salah membagi nilai eksponen 8 dengan 2.</sub>
- B. $80$ skala Richter  
  <sub>Salah: Salah mengalikan basis 10 dengan nilai eksponen 8.</sub>
- C. $\frac{8}{10}$ skala Richter  
  <sub>Salah: Membagi nilai eksponen dengan nilai basis 10.</sub>
- **D. $8$ skala Richter** ✅  
  <sub>Benar: Nilai $\log(10^8) = 8$.</sub>

**Pembahasan:** Berdasarkan rumus skala Richter:
$$M = \log\left(\frac{I}{I_0}\right) = \log\left(\frac{10^8 I_0}{I_0}\right) = \log(10^8) = 8$$
Jadi, kekuatan gempa bumi tersebut adalah $8$ skala Richter.
**Acuan:** siswa — siswa hal.270 Contoh 6.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11_tl-b06-a-easy-bt01-018
*variasi (angka) | C2 | 2 langkah | jenis: persamaan fungsi logaritma*

Jika $f(x) = \log x$, nilai $y$ yang memenuhi persamaan $f(20) + f(y) = 3$ adalah ....

- A. $15$  
  <sub>Salah: Salah melakukan operasi pengurangan $20 - 5$ atau mengabaikan eksponen basis 10.</sub>
- B. $500$  
  <sub>Salah: Salah mengira $10^3 = 10.000$ sehingga $10.000 / 20 = 500$.</sub>
- **C. $50$** ✅  
  <sub>Benar: $\log(20y) = 3 \Rightarrow 20y = 10^3 = 1.000 \Rightarrow y = 50$.</sub>
- D. $5$  
  <sub>Salah: Salah mengira $10^3 = 100$ sehingga $100 / 20 = 5$.</sub>

**Pembahasan:** Diketahui $f(x) = \log x$, maka:
$$f(20) + f(y) = 3$$
$$\log 20 + \log y = 3$$
$$\log(20y) = 3$$
Berdasarkan definisi logaritma umum (basis 10):
$$20y = 10^3$$
$$20y = 1.000$$
$$y = \frac{1.000}{20} = 50$$
Jadi, nilai $y$ adalah $50$.
**Acuan:** siswa — siswa hal.266 Contoh 6.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11_tl-b06-a-easy-bt01-019
*variasi (angka) | C1 | 1 langkah | jenis: evaluasi fungsi logaritma nol*

Diberikan fungsi logaritma $f(x) = {}^8\log x$. Nilai dari $f(1)$ adalah ....

- A. $1$  
  <sub>Salah: Salah mengingat sifat identitas logaritma dasar.</sub>
- B. $\frac{1}{8}$  
  <sub>Salah: Keliru menganggap nilai fungsi sebagai kebalikan dari basis.</sub>
- C. $8$  
  <sub>Salah: Menyamakan hasil fungsi dengan nilai basis.</sub>
- **D. $0$** ✅  
  <sub>Benar: Berdasarkan definisi eksponen dan logaritma, $8^0 = 1$ sehingga ${}^8\log 1 = 0$.</sub>

**Pembahasan:** Substitusikan $x = 1$ ke dalam fungsi:
$$f(1) = {}^8\log 1$$
Karena $8^0 = 1$, diperoleh:
$${}^8\log 1 = 0$$
Jadi, nilai $f(1)$ adalah $0$.
**Acuan:** siswa — siswa hal.261 Contoh 6.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11_tl-b06-a-easy-bt01-020
*orisinal | C1 | 1 langkah | jenis: terminologi logaritma umum*

Fungsi logaritma yang memiliki basis 10 disebut ....

- **A. fungsi logaritma umum** ✅  
  <sub>Benar: Sesuai definisi pada buku teks, logaritma berbasis 10 disebut fungsi logaritma umum.</sub>
- B. fungsi logaritma alami  
  <sub>Salah: Terkecoh dengan sebutan untuk logaritma dengan basis bilangan Euler e.</sub>
- C. fungsi logaritma biner  
  <sub>Salah: Terkecoh dengan fungsi logaritma yang berbasis 2.</sub>
- D. fungsi logaritma murni  
  <sub>Salah: Menggunakan istilah buatan yang tidak dikenal dalam materi.</sub>

**Pembahasan:** Berdasarkan Definisi 6.1 pada buku teks matematika kelas XI, fungsi logaritma yang basisnya bernilai 10 disebut fungsi logaritma umum.
**Acuan:** siswa — siswa hal.261

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11_tl-b06-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: pemodelan skala logaritma*

Dua wilayah mengalami gempa bumi. Wilayah pertama mencatat kekuatan gempa sebesar $8,4$ skala Richter, sedangkan wilayah kedua mencatat kekuatan gempa sebesar $5,4$ skala Richter. Besar kekuatan gempa dirumuskan dengan $M = \log\left(\frac{I}{I_0}\right)$, dengan $I$ adalah intensitas gempa dan $I_0$ adalah intensitas gempa tingkat nol. Berapa kali lipat intensitas gempa bumi di wilayah kedua dibandingkan dengan gempa bumi di wilayah pertama?

- A. $10^3$ kali lipat  
  <sub>Salah: Siswa membalik perbandingan dengan menghitung rasio intensitas wilayah pertama terhadap wilayah kedua.</sub>
- B. $3$ kali lipat  
  <sub>Salah: Siswa hanya mengurangkan magnitudo secara langsung ($8,4 - 5,4 = 3$) tanpa mengubahnya ke bentuk pangkat basis 10.</sub>
- C. $10^{-1,5}$ kali lipat  
  <sub>Salah: Siswa membagi nilai skala Richter ($5,4 / 8,4$) bukannya mengurangkannya dalam logaritma.</sub>
- **D. $10^{-3}$ kali lipat** ✅  
  <sub>Benar: Selisih skala Richter adalah $M_2 - M_1 = 5,4 - 8,4 = -3$. Karena $\log(I_2/I_0) - \log(I_1/I_0) = \log(I_2/I_1)$, maka $\log(I_2/I_1) = -3 \iff I_2/I_1 = 10^{-3}$.</sub>

**Pembahasan:** Diketahui:
$M_1 = 8,4 \implies \log\left(\frac{I_1}{I_0}\right) = 8,4$
$M_2 = 5,4 \implies \log\left(\frac{I_2}{I_0}\right) = 5,4$

Kurangkan kedua persamaan:
$\log\left(\frac{I_2}{I_0}\right) - \log\left(\frac{I_1}{I_0}\right) = 5,4 - 8,4$
$\log\left(\frac{I_2}{I_1}\right) = -3$
$\frac{I_2}{I_1} = 10^{-3}$

Jadi, intensitas gempa bumi di wilayah kedua adalah $10^{-3}$ kali lipat (atau $\frac{1}{1.000}$ kali lipat) intensitas gempa bumi di wilayah pertama.
**Acuan:** siswa — siswa hal.273 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11_tl-b06-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: identitas logaritma*

Diberikan fungsi logaritma $f(x) = {}^2\log x$. Jika diketahui nilai $f(7) \approx 2,81$, nilai dari $f(56)$ adalah ....

- **A. $5,81$** ✅  
  <sub>Benar: Dekomposisi $56 = 8 \times 7$, sehingga $f(56) = {}^2\log(8 \times 7) = {}^2\log 8 + {}^2\log 7 = 3 + 2,81 = 5,81$.</sub>
- B. $8,43$  
  <sub>Salah: Siswa mengalikan nilai $f(7)$ dengan $3$ ($3 \times 2,81$) karena keliru memperlakukan logaritma sebagai fungsi linear.</sub>
- C. $11,24$  
  <sub>Salah: Siswa mengalikan $f(7)$ dengan $4$ karena keliru mendekomposisi $56 = 4 \times 14$ lalu mengalikan konstanta.</sub>
- D. $4,81$  
  <sub>Salah: Siswa keliru menghitung ${}^2\log 8 = 2$ sehingga menjumlahkan $2 + 2,81$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi, $f(56) = {}^2\log 56$.
Faktorkan $56$ menjadi $8 \times 7$:
$f(56) = {}^2\log(8 \times 7)$

Gunakan sifat logaritma perkalian ${}^b\log(MN) = {}^b\log M + {}^b\log N$:
$f(56) = {}^2\log 8 + {}^2\log 7$
$f(56) = {}^2\log(2^3) + f(7)$
$f(56) = 3 + 2,81 = 5,81$

Jadi, nilai $f(56)$ adalah $5,81$.
**Acuan:** siswa — siswa hal.266 Contoh 6.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11_tl-b06-a-medium-bt01-003
*orisinal | C3 | 2 langkah | jenis: entropi kata sandi*

Sebuah sistem komputer membuat kata sandi acak dengan panjang $6$ simbol. Setiap simbol dipilih secara independen dari $16$ simbol sistem heksadesimal ($0$ sampai $9$ dan $A$ sampai $F$). Jika entropi informasi kata sandi dihitung dengan rumus $H = L \cdot {}^2\log N$, dengan $L$ adalah panjang kata sandi dan $N$ adalah banyaknya simbol yang tersedia, maka besar entropi informasi kata sandi tersebut adalah ....

- A. $16\text{ bit}$  
  <sub>Salah: Siswa salah menghitung ${}^2\log 16 = 4$ lalu menambahkan panjang simbol bukannya mengalikannya ($6 + 4$ lalu tertukar dengan angka $16$).</sub>
- **B. $24\text{ bit}$** ✅  
  <sub>Benar: $H = 6 \cdot {}^2\log 16 = 6 \cdot 4 = 24\text{ bit}$.</sub>
- C. $96\text{ bit}$  
  <sub>Salah: Siswa mengalikan langsung $L \times N = 6 \times 16$ tanpa menerapkan operasi logaritma basis 2.</sub>
- D. $4\text{ bit}$  
  <sub>Salah: Siswa hanya menghitung entropi satu karakter saja (${}^2\log 16 = 4$) tanpa mengalikan dengan panjang kata sandi $L = 6$.</sub>

**Pembahasan:** Diketahui:
Panjang kata sandi ($L$) = $6$
Banyak simbol yang mungkin ($N$) = $16$

Rumus entropi informasi:
$H = L \cdot {}^2\log N$
$H = 6 \cdot {}^2\log 16$

Karena $16 = 2^4$, maka ${}^2\log 16 = 4$.
$H = 6 \times 4 = 24\text{ bit}$

Jadi, besar entropi informasi kata sandi tersebut adalah $24\text{ bit}$.
**Acuan:** siswa — siswa hal.268

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11_tl-b06-a-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: pertidaksamaan fungsi logaritma*

Himpunan penyelesaian dari pertidaksamaan logaritma ${}^{\frac{1}{3}}\log(2x - 5) < {}^{\frac{1}{3}}\log(x + 1)$ untuk $x \in \mathbb{R}$ adalah ....

- A. $2,5 < x < 6$  
  <sub>Salah: Siswa tidak membalik tanda pertidaksamaan namun mengirisnya dengan syarat numerus $x > 2,5$.</sub>
- B. $x < 6$  
  <sub>Salah: Siswa lupa membalik tanda pertidaksamaan padahal basis logaritma pecahan ($0 < b < 1$).</sub>
- C. $x > 2,5$  
  <sub>Salah: Siswa hanya menyelesaikan syarat numerus tanpa menyelesaikan inti pertidaksamaan logaritma.</sub>
- **D. $x > 6$** ✅  
  <sub>Benar: Basis $0 < \frac{1}{3} < 1$ membalik tanda menjadi $2x - 5 > x + 1 \implies x > 6$. Syarat numerus $x > 2,5$ dan $x > -1$. Irisannya adalah $x > 6$.</sub>

**Pembahasan:** Langkah 1: Tentukan syarat numerus (harus positif).
1) $2x - 5 > 0 \iff x > \frac{5}{2} = 2,5$
2) $x + 1 > 0 \iff x > -1$
Irisan syarat numerus: $x > 2,5$.

Langkah 2: Selesaikan pertidaksamaan logaritma.
Karena basis $b = \frac{1}{3}$ memenuhi $0 < b < 1$, maka tanda pertidaksamaan berbalik:
$2x - 5 > x + 1$
$2x - x > 1 + 5$
$x > 6$

Langkah 3: Tentukan irisan dari Langkah 1 dan Langkah 2.
Irisan dari $x > 2,5$ dan $x > 6$ adalah $x > 6$.

Jadi, himpunan penyelesaiannya adalah $x > 6$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11_tl-b06-a-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: karakteristik grafik logaritma*

Diberikan fungsi logaritma $f(x) = {}^2\log(x - 3) - 2$. Titik potong grafik fungsi $f(x)$ terhadap sumbu-$x$ serta persamaan asimtot tegaknya berturut-turut adalah ....

- A. $(4, 0)$ dan $x = 0$  
  <sub>Salah: Siswa mengabaikan pergeseran grafik horizontal dan menganggap asimtot tegak selalu sumbu-$y$ ($x = 0$).</sub>
- **B. $(7, 0)$ dan $x = 3$** ✅  
  <sub>Benar: Titik potong sumbu-$x$ saat $f(x)=0 \implies {}^2\log(x-3)=2 \implies x-3=4 \implies x=7$. Asimtot tegak saat numerus mendekati nol, yaitu $x-3=0 \implies x=3$.</sub>
- C. $(7, 0)$ dan $x = -3$  
  <sub>Salah: Siswa salah menentukan tanda asimtot tegak dari pembuat nol numerus ($x - 3 = 0$ ditulis $x = -3$).</sub>
- D. $(5, 0)$ dan $x = 3$  
  <sub>Salah: Siswa keliru menghitung $2^2 = 4$ menjadi $2 \times 1 = 2$ sehingga menghasilkan $x = 2 + 3 = 5$.</sub>

**Pembahasan:** Langkah 1: Menentukan persamaan asimtot tegak.
Asimtot tegak grafik fungsi logaritma $f(x) = {}^b\log(g(x)) + c$ terjadi saat batas nilai numerus $g(x) = 0$:
$x - 3 = 0 \iff x = 3$
Jadi, persamaan asimtot tegaknya adalah $x = 3$.

Langkah 2: Menentukan titik potong dengan sumbu-$x$.
Grafik memotong sumbu-$x$ ketika $f(x) = 0$:
${}^2\log(x - 3) - 2 = 0$
${}^2\log(x - 3) = 2$

Ubah ke bentuk eksponensial:
$x - 3 = 2^2$
$x - 3 = 4$
$x = 7$

Titik potongnya adalah $(7, 0)$.

Jadi, titik potong sumbu-$x$ dan asimtot tegaknya berturut-turut adalah $(7, 0)$ dan $x = 3$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11_tl-b06-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: evaluasi fungsi logaritma*

Diberikan fungsi logaritma $f(x) = {}^4\log x$. Nilai dari $f\left(\frac{1}{16}\right) + f\left(\frac{1}{64}\right)$ adalah ....

- A. $-6$  
  <sub>Salah: Keliru menganggap 1/64 adalah 4 pangkat -4.</sub>
- B. $5$  
  <sub>Salah: Lupa tanda negatif pada pangkat pecahan.</sub>
- **C. $-5$** ✅  
  <sub>Benar: $f(1/16) = {}^4\log(4^{-2}) = -2$ dan $f(1/64) = {}^4\log(4^{-3}) = -3$, sehingga $-2 + (-3) = -5$.</sub>
- D. $-1$  
  <sub>Salah: Mengurangkan nilai kedua fungsi (-2 - (-3) = 1) alih-alih menjumlahkannya.</sub>

**Pembahasan:** Hitung masing-masing nilai fungsi:
1. $f\left(\frac{1}{16}\right) = {}^4\log\left(4^{-2}\right) = -2$
2. $f\left(\frac{1}{64}\right) = {}^4\log\left(4^{-3}\right) = -3$

Jumlahkan kedua nilai tersebut:
$f\left(\frac{1}{16}\right) + f\left(\frac{1}{64}\right) = -2 + (-3) = -5$.
**Acuan:** siswa — siswa hal.262 Mari Mencoba 6.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11_tl-b06-a-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: persamaan fungsi logaritma*

Jika $f(x) = \log x$, nilai $y$ yang memenuhi persamaan $f(25) + f(y) = 5$ adalah ....

- A. $250$  
  <sub>Salah: Membagi $10^4$ dengan $40$ atau kesalahan pembagian numerus.</sub>
- B. $400$  
  <sub>Salah: Keliru menganggap $10^5$ sebagai $10.000$ sehingga $10.000 / 25 = 400$.</sub>
- C. $2.500$  
  <sub>Salah: Salah membagi 100.000 dengan perkiraan keliru atau salah pangkat basis 10.</sub>
- **D. $4.000$** ✅  
  <sub>Benar: $\log(25y) = 5 \implies 25y = 10^5 = 100.000 \implies y = 4.000$.</sub>

**Pembahasan:** Diketahui $f(x) = \log x$, maka:
$$f(25) + f(y) = 5$$
$$\log 25 + \log y = 5$$
$$\log(25y) = 5$$

Ubah ke bentuk eksponensial:
$$25y = 10^5$$
$$25y = 100.000$$
$$y = \frac{100.000}{25} = 4.000$$.
**Acuan:** siswa — siswa hal.266 Contoh 6.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11_tl-b06-a-medium-bt01-008
*variasi (konteks) | C3 | 2 langkah | jenis: perhitungan nilai pH*

Suatu larutan pembersih memiliki konsentrasi ion hidrogen sebesar $[\text{H}^+] = 2 \times 10^{-5}\text{ M}$. Jika nilai $\text{pH} = -\log[\text{H}^+]$ dan diketahui $\log 2 \approx 0,30$, nilai pH larutan tersebut adalah ....

- A. $-4,70$  
  <sub>Salah: Lupa mengalikan tanda negatif di luar tanda kurung definisi pH.</sub>
- **B. $4,70$** ✅  
  <sub>Benar: $\text{pH} = -\log(2 \times 10^{-5}) = -(\log 2 + \log 10^{-5}) = -(0,30 - 5) = 4,70$.</sub>
- C. $4,30$  
  <sub>Salah: Keliru menghitung $5 - 2(0,30) = 4,40$ atau pengurangan yang salah.</sub>
- D. $5,30$  
  <sub>Salah: Menjumlahkan eksponen dengan log 2 alih-alih mengurangkannya ($5 + 0,30$).</sub>

**Pembahasan:** Gunakan definisi pH:
$$\text{pH} = -\log[\text{H}^+]$$
$$\text{pH} = -\log(2 \times 10^{-5})$$
$$\text{pH} = -(\log 2 + \log 10^{-5})$$
$$\text{pH} = -(0,30 - 5)$$
$$\text{pH} = -(-4,70) = 4,70$$.
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11_tl-b06-a-medium-bt01-009
*orisinal | C3 | 3 langkah | jenis: waktu pengisian baterai*

Lama waktu $t$ (dalam menit) yang diperlukan untuk mengisi daya suatu baterai dari kondisi kosong hingga mencapai daya $C$ ditentukan oleh rumus $t = -\frac{1}{k}\ln\left(1 - \frac{C}{C_0}\right)$, dengan $C_0$ adalah kapasitas maksimum baterai dan $k$ adalah konstanta pengisian. Jika nilai $k = 0,05$ dan diketahui $\ln 2 \approx 0,69$, waktu yang dibutuhkan untuk mengisi baterai hingga mencapai $75\%$ dari kapasitas maksimumnya adalah sekitar ....

- **A. $27,6\text{ menit}$** ✅  
  <sub>Benar: $1 - 0,75 = 0,25 = 2^{-2}$, $\ln(0,25) = -2\ln 2 \approx -1,38$, lalu $t = -\frac{1}{0,05}(-1,38) = 20 \times 1,38 = 27,6\text{ menit}$.</sub>
- B. $13,8\text{ menit}$  
  <sub>Salah: Lupa mengalikan dengan faktor 2 dari sifat eksponen $\ln(1/4) = -2\ln 2$.</sub>
- C. $55,2\text{ menit}$  
  <sub>Salah: Keliru membagi dengan nilai konstanta dua kali lipat.</sub>
- D. $34,5\text{ menit}$  
  <sub>Salah: Menggunakan $\ln(0,75)$ alih-alih $\ln(1 - 0,75)$.</sub>

**Pembahasan:** Baterai diisi hingga $75\%$ kapasitas maksimum, sehingga $\frac{C}{C_0} = 0,75$.
Substitusikan ke persamaan waktu:
$$t = -\frac{1}{0,05}\ln(1 - 0,75)$$
$$t = -20\ln(0,25)$$
$$t = -20\ln\left(2^{-2}\right)$$
$$t = -20(-2\ln 2)$$
$$t = 40\ln 2$$
$$t \approx 40(0,69) = 27,6\text{ menit}$$.
**Acuan:** siswa — siswa hal.270

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11_tl-b06-a-medium-bt01-010
*orisinal | C4 | 3 langkah | jenis: daerah asal fungsi logaritma*

Daerah asal (domain) dari fungsi logaritma $f(x) = {}^3\log(x^2 - 2x - 8)$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x \le -2 \text{ atau } x \ge 4,\, x \in \mathbb{R}\}$  
  <sub>Salah: Menyertakan tanda sama dengan, padahal numerus logaritma harus bernilai strictly positif ($> 0$).</sub>
- B. $\{x \mid -2 < x < 4,\, x \in \mathbb{R}\}$  
  <sub>Salah: Mengambil daerah interval bagian dalam bukan bagian luar kurva pertidaksamaan lebih dari nol.</sub>
- C. $\{x \mid x < -4 \text{ atau } x > 2,\, x \in \mathbb{R}\}$  
  <sub>Salah: Tertukar tanda akar-akar pembuat nol pada saat pemfaktoran persamaan kuadrat.</sub>
- **D. $\{x \mid x < -2 \text{ atau } x > 4,\, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat numerus $x^2 - 2x - 8 > 0 \iff (x - 4)(x + 2) > 0$, dipenuhi oleh $x < -2$ atau $x > 4$.</sub>

**Pembahasan:** Agar fungsi logaritma terdefinisi pada himpunan bilangan real, numerus harus bernilai positif:
$$x^2 - 2x - 8 > 0$$
$$(x - 4)(x + 2) > 0$$

Titik pembuat nol adalah $x = 4$ dan $x = -2$.
Uji tanda pada garis bilangan menunjukkan nilai bernilai positif untuk $x < -2$ atau $x > 4$.

Jadi, daerah asalnya adalah $\{x \mid x < -2 \text{ atau } x > 4,\, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11_tl-b06-a-medium-bt01-011
*variasi (angka) | C3 | 2 langkah | jenis: evaluasi fungsi logaritma*

Diberikan fungsi logaritma $f(x) = {}^5\log x$. Nilai dari $f\left(\frac{1}{25}\right) - f\left(\frac{1}{125}\right)$ adalah ....

- A. $5$  
  <sub>Salah: Mengabaikan tanda minus pada eksponen sehingga menghitung $2 - (-3) = 5$.</sub>
- B. $-1$  
  <sub>Salah: Tertukar urutan pengurangan $(-3 - (-2) = -1)$ atau salah tanda operasi.</sub>
- C. $-5$  
  <sub>Salah: Melakukan penjumlahan $-2 + (-3)$ bukannya pengurangan.</sub>
- **D. $1$** ✅  
  <sub>Benar: $f(1/25) = {}^5\log(5^{-2}) = -2$ dan $f(1/125) = {}^5\log(5^{-3}) = -3$. Hasil pengurangan: $-2 - (-3) = 1$.</sub>

**Pembahasan:** Berdasarkan definisi logaritma:
1. $f\left(\frac{1}{25}\right) = {}^5\log\left(5^{-2}\right) = -2$
2. $f\left(\frac{1}{125}\right) = {}^5\log\left(5^{-3}\right) = -3$

Maka, nilai dari $f\left(\frac{1}{25}\right) - f\left(\frac{1}{125}\right) = -2 - (-3) = -2 + 3 = 1$.
**Acuan:** siswa — siswa hal.262 Mari Mencoba 6.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11_tl-b06-a-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: persamaan fungsi logaritma*

Jika $f(x) = \log x$, nilai $y$ yang memenuhi persamaan $f(16) + f(y) = 2$ adalah ....

- **A. $6,25$** ✅  
  <sub>Benar: $\log(16) + \log(y) = \log(16y) = 2 \implies 16y = 10^2 = 100 \implies y = 100/16 = 6,25$.</sub>
- B. $1,25$  
  <sub>Salah: Menganggap $10^2 = 20$ sehingga menghitung $20/16 = 1,25$.</sub>
- C. $5,25$  
  <sub>Salah: Kesalahan perhitungan aritmetika pembagian $100/16$.</sub>
- D. $0,16$  
  <sub>Salah: Membagi $16$ dengan $100$ ($16/100$) bukannya $100/16$.</sub>

**Pembahasan:** Diketahui $f(x) = \log x$ dan $f(16) + f(y) = 2$.

Menggunakan sifat penjumlahan logaritma:
$$\log 16 + \log y = 2$$
$$\log(16y) = 2$$

Berdasarkan definisi fungsi logaritma umum (basis 10):
$$16y = 10^2$$
$$16y = 100$$
$$y = \frac{100}{16} = 6,25$$

Jadi, nilai $y$ yang memenuhi adalah $6,25$.
**Acuan:** siswa — siswa hal.266 Contoh 6.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11_tl-b06-a-medium-bt01-013
*orisinal | C4 | 3 langkah | jenis: pertidaksamaan fungsi logaritma*

Himpunan penyelesaian dari pertidaksamaan logaritma ${}^2\log(3x - 9) \le 3$ untuk $x \in \mathbb{R}$ adalah ....

- A. $\{x \mid x > 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Hanya menghitung syarat numerus tanpa menyelesaikan pertidaksamaan logaritma.</sub>
- B. $\{x \mid x \le \frac{17}{3},\, x \in \mathbb{R}\}$  
  <sub>Salah: Lupa menerapkan syarat numerus harus positif ($x > 3$).</sub>
- **C. $\{x \mid 3 < x \le \frac{17}{3},\, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat numerus $3x - 9 > 0 \implies x > 3$. Pertidaksamaan ${}^2\log(3x - 9) \le {}^2\log 8 \implies 3x - 9 \le 8 \implies x \le 17/3$. Irisan keduanya adalah $3 < x \le 17/3$.</sub>
- D. $\{x \mid 3 \le x \le \frac{17}{3},\, x \in \mathbb{R}\}$  
  <sub>Salah: Keliru menganggap batas syarat numerus bertanda sama dengan ($\le$).</sub>

**Pembahasan:** Langkah 1: Menentukan syarat numerus.
$$3x - 9 > 0 \implies 3x > 9 \implies x > 3$$

Langkah 2: Menyelesaikan pertidaksamaan pokok.
$${}^2\log(3x - 9) \le 3$$
$${}^2\log(3x - 9) \le {}^2\log(2^3)$$
$${}^2\log(3x - 9) \le {}^2\log 8$$

Karena basis $b = 2 > 1$, tanda pertidaksamaan tetap:
$$3x - 9 \le 8$$
$$3x \le 17$$
$$x \le \frac{17}{3}$$

Langkah 3: Menentukan irisan dari syarat numerus dan penyelesaian pokok.
$$3 < x \le \frac{17}{3}$$

Jadi, himpunan penyelesaiannya adalah $\{x \mid 3 < x \le \frac{17}{3},\, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11_tl-b06-a-medium-bt01-014
*orisinal | C3 | 2 langkah | jenis: entropi kata sandi*

Sebuah sistem keamanan menghasilkan kata sandi acak dengan panjang $5$ karakter ($L = 5$). Karakter dipilih dari $32$ jenis simbol yang tersedia ($N = 32$). Besar entropi informasi ($H$) dari kata sandi tersebut adalah ....

- A. $30\text{ bit}$  
  <sub>Salah: Mengira ${}^2\log 32 = 6$ sehingga $5 \times 6 = 30$.</sub>
- B. $160\text{ bit}$  
  <sub>Salah: Melakukan perkalian langsung $L \times N = 5 \times 32$ tanpa menerapkan logaritma.</sub>
- **C. $25\text{ bit}$** ✅  
  <sub>Benar: $H = L \cdot {}^2\log N = 5 \cdot {}^2\log 32 = 5 \cdot 5 = 25\text{ bit}$.</sub>
- D. $20\text{ bit}$  
  <sub>Salah: Mengira ${}^2\log 32 = 4$ sehingga $5 \times 4 = 20$.</sub>

**Pembahasan:** Berdasarkan rumus entropi informasi kata sandi acak:
$$H = L \cdot {}^2\log N$$

Diketahui:
- Panjang sandi ($L$) = $5$
- Banyak simbol ($N$) = $32$

Substitusikan nilai ke dalam rumus:
$$H = 5 \cdot {}^2\log(32)$$
Karena $32 = 2^5$, maka ${}^2\log(32) = 5$.
$$H = 5 \cdot 5 = 25\text{ bit}$$

Jadi, entropi kata sandi tersebut adalah $25\text{ bit}$.
**Acuan:** siswa — siswa hal.268

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11_tl-b06-a-medium-bt01-015
*orisinal | C3 | 2 langkah | jenis: karakteristik grafik logaritma*

Diketahui fungsi logaritma $f(x) = {}^3\log(x + 2) - 1$. Titik potong grafik $f(x)$ terhadap sumbu-$x$ dan persamaan asimtot tegaknya berturut-turut adalah ....

- A. $(1, 0)$ dan $x = 2$  
  <sub>Salah: Salah tanda pada asimtot tegak ($x - 2 = 0$).</sub>
- B. $(3, 0)$ dan $x = -2$  
  <sub>Salah: Keliru menyelesaikan $x + 2 = 3^1$ menjadi $x = 3$.</sub>
- **C. $(1, 0)$ dan $x = -2$** ✅  
  <sub>Benar: Potong sumbu-x: $f(x) = 0 \implies {}^3\log(x+2) = 1 \implies x+2 = 3 \implies x = 1$. Asimtot tegak: $x + 2 = 0 \implies x = -2$.</sub>
- D. (-1, 0) dan $x = 0$  
  <sub>Salah: Mengira asimtot tegak selalu $x = 0$ dan salah menghitung titik potong.</sub>

**Pembahasan:** 1. Menentukan titik potong dengan sumbu-$x$ (saat $f(x) = 0$):
$${}^3\log(x + 2) - 1 = 0$$
$${}^3\log(x + 2) = 1$$
$$x + 2 = 3^1$$
$$x + 2 = 3$$
$$x = 1$$
Titik potong sumbu-$x$ adalah $(1, 0)$.

2. Menentukan persamaan asimtot tegak:
Asimtot tegak fungsi logaritma terjadi pada batas numerus bernilai nol:
$$x + 2 = 0 \implies x = -2$$

Jadi, titik potong sumbu-$x$ dan persamaan asimtot tegaknya berturut-turut adalah $(1, 0)$ dan $x = -2$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11_tl-b06-a-medium-bt01-016
*variasi (angka) | C3 | 2 langkah | jenis: pemodelan skala logaritma*

Dua wilayah mengalami peristiwa gempa bumi. Wilayah P mencatat kekuatan gempa sebesar $8,7$ skala Richter, sedangkan wilayah Q mencatat kekuatan gempa sebesar $5,7$ skala Richter. Besar kekuatan gempa ditentukan dengan rumus $M = \log\left(\frac{I}{I_0}\right)$, dengan $I$ adalah intensitas gempa dan $I_0$ adalah intensitas gempa tingkat nol. Berapa kali lipat intensitas gempa bumi di wilayah P dibandingkan intensitas gempa bumi di wilayah Q?

- **A. $1.000\text{ kali lipat}$** ✅  
  <sub>Benar: Dari rumus skala Richter diperoleh $I = I_0 \times 10^M$. Maka perbandingan intensitasnya adalah $\frac{I_P}{I_Q} = \frac{I_0 \times 10^{8,7}}{I_0 \times 10^{5,7}} = 10^{8,7 - 5,7} = 10^3 = 1.000$ kali lipat.</sub>
- B. $30\text{ kali lipat}$  
  <sub>Salah: Mengalikan selisih skala Richter dengan basis 10 ($3 \times 10$) alih-alih memangkatkannya.</sub>
- C. $3\text{ kali lipat}$  
  <sub>Salah: Hanya mengurangkan langsung nilai skala Richter $8,7 - 5,7 = 3$ tanpa memperhitungkan basis logaritma 10.</sub>
- D. $100\text{ kali lipat}$  
  <sub>Salah: Kesalahan pengurangan pangkat eksponen menjadi $10^2 = 100$.</sub>

**Pembahasan:** Berdasarkan definisi skala Richter:
$M = \log\left(\frac{I}{I_0}\right) \iff \frac{I}{I_0} = 10^M \iff I = I_0 \times 10^M$.

Untuk kedua wilayah:
- Wilayah P: $I_P = I_0 \times 10^{8,7}$
- Wilayah Q: $I_Q = I_0 \times 10^{5,7}$

Rasio intensitas wilayah P terhadap wilayah Q:
$$\frac{I_P}{I_Q} = \frac{I_0 \times 10^{8,7}}{I_0 \times 10^{5,7}} = 10^{8,7 - 5,7} = 10^3 = 1.000$$

Jadi, intensitas gempa di wilayah P adalah $1.000\text{ kali lipat}$ dari wilayah Q.
**Acuan:** siswa — siswa hal.273 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11_tl-b06-a-medium-bt01-017
*variasi (angka) | C3 | 3 langkah | jenis: identitas logaritma*

Diberikan fungsi logaritma $f(x) = {}^5\log x$. Jika diketahui nilai $f(2) \approx 0,43$, nilai dari $f(50)$ adalah ....

- A. $2,86$  
  <sub>Salah: Mengalikan nilai $f(2)$ dengan 2 alih-alih menjumlahkannya dengan ${}^5\log 25$.</sub>
- **B. $2,43$** ✅  
  <sub>Benar: $f(50) = {}^5\log 50 = {}^5\log(25 \times 2) = {}^5\log 25 + {}^5\log 2 = 2 + 0,43 = 2,43$.</sub>
- C. $10,43$  
  <sub>Salah: Menguraikan $50$ sebagai $5 \times 10$ lalu salah menghitung ${}^5\log 50 = 10 + 0,43$.</sub>
- D. $1,43$  
  <sub>Salah: Salah menghitung ${}^5\log 25$ menjadi 1, sehingga $1 + 0,43 = 1,43$.</sub>

**Pembahasan:** Diketahui $f(x) = {}^5\log x$ dan $f(2) = {}^5\log 2 \approx 0,43$.

Uraikan nilai $50$ ke dalam faktor perpangkatan $5$ dan $2$:
$$50 = 25 \times 2 = 5^2 \times 2$$

Menggunakan identitas logaritma:
$$\begin{aligned}
f(50) &= {}^5\log(5^2 \times 2) \\
&= {}^5\log(5^2) + {}^5\log 2 \\
&= 2 + 0,43 \\
&= 2,43
\end{aligned}$$

Jadi, nilai $f(50)$ adalah $2,43$.
**Acuan:** siswa — siswa hal.266 Contoh 6.3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11_tl-b06-a-medium-bt01-018
*variasi (konteks) | C3 | 2 langkah | jenis: perhitungan nilai pH*

Suatu sampel air limbah laboratorium memiliki konsentrasi ion hidrogen sebesar $[\text{H}^+] = 5 \times 10^{-4}\text{ M}$. Jika nilai derajat keasaman dirumuskan dengan $\text{pH} = -\log[\text{H}^+]$ dan diketahui $\log 5 \approx 0,70$, nilai pH sampel air tersebut adalah ....

- A. $4,70$  
  <sub>Salah: Kesalahan tanda operasi saat memecah kurung, yaitu menghitung $4 + 0,70$ alih-alih $4 - 0,70$.</sub>
- B. $3,70$  
  <sub>Salah: Salah melakukan pengurangan desimal dari $4 - 0,70$ menjadi $3,70$.</sub>
- **C. $3,30$** ✅  
  <sub>Benar: $\text{pH} = -\log(5 \times 10^{-4}) = -(\log 5 + \log 10^{-4}) = -(0,70 - 4) = 4 - 0,70 = 3,30$.</sub>
- D. $-3,30$  
  <sub>Salah: Lupa menerapkan tanda negatif di luar rumus logaritma.</sub>

**Pembahasan:** Berdasarkan rumus pH:
$$\begin{aligned}
\text{pH} &= -\log[\text{H}^+] \\
&= -\log(5 \times 10^{-4}) \\
&= -(\log 5 + \log 10^{-4}) \\
&= -(0,70 + (-4)) \\
&= -(0,70 - 4) \\
&= -(-3,30) = 3,30
\end{aligned}$$

Jadi, nilai pH sampel air limbah tersebut adalah $3,30$.
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11_tl-b06-a-medium-bt01-019
*orisinal | C3 | 3 langkah | jenis: pemodelan pertumbuhan logaritma*

Suatu jenis bakteri membelah diri setiap 2 jam. Jika koloni mula-mula terdiri atas 50 bakteri, waktu $t$ (dalam jam) yang diperlukan agar populasi menjadi sebanyak $N$ bakteri dimodelkan dengan rumus $t = 2 \cdot {}^2\log\left(\frac{N}{50}\right)$. Waktu yang dibutuhkan agar koloni bakteri tersebut mencapai 800 bakteri adalah ....

- A. $4\text{ jam}$  
  <sub>Salah: Lupa mengalikan hasil logaritma dengan faktor waktu 2 jam, hanya menghitung ${}^2\log 16 = 4$.</sub>
- **B. $8\text{ jam}$** ✅  
  <sub>Benar: $t = 2 \cdot {}^2\log\left(\frac{800}{50}\right) = 2 \cdot {}^2\log(16) = 2 \cdot 4 = 8\text{ jam}$.</sub>
- C. $32\text{ jam}$  
  <sub>Salah: Mengalikan nilai rasio 16 langsung dengan 2 tanpa mencari nilai logaritmanya terlebih dahulu.</sub>
- D. $16\text{ jam}$  
  <sub>Salah: Mengalikan hasil pemangkatan dengan faktor 4 alih-alih mengalikan eksponen 4 dengan 2.</sub>

**Pembahasan:** Substitusikan nilai $N = 800$ ke dalam rumus yang diberikan:
$$\begin{aligned}
t &= 2 \cdot {}^2\log\left(\frac{800}{50}\right) \\
&= 2 \cdot {}^2\log(16)
\end{aligned}$$

Karena $16 = 2^4$, maka ${}^2\log 16 = 4$.
$$t = 2 \cdot 4 = 8\text{ jam}$$

Jadi, waktu yang dibutuhkan agar koloni mencapai 800 bakteri adalah $8\text{ jam}$.
**Acuan:** siswa — siswa hal.273

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11_tl-b06-a-medium-bt01-020
*orisinal | C4 | 3 langkah | jenis: daerah asal fungsi logaritma*

Daerah asal (domain) dari fungsi logaritma $f(x) = {}^2\log\left(\frac{2x - 6}{x + 5}\right)$ untuk $x \in \mathbb{R}$ adalah ....

- **A. $\{x \mid x < -5 \text{ atau } x > 3,\, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat numerus fungsi logaritma harus positif, yaitu $\frac{2x - 6}{x + 5} > 0$. Pembuat nol adalah $x = 3$ dan $x = -5$. Melalui uji tanda diperoleh interval $x < -5$ atau $x > 3$.</sub>
- B. $\{x \mid x > 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Hanya meninjau syarat pembilang $2x - 6 > 0$ dan mengabaikan nilai penyebut yang membuat pecahan bernilai positif ketika keduanya negatif.</sub>
- C. $\{x \mid -5 < x < 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Mengambil interval yang menghasilkan nilai negatif pada garis bilangan.</sub>
- D. $\{x \mid x \le -5 \text{ atau } x \ge 3,\, x \in \mathbb{R}\}$  
  <sub>Salah: Menyertakan batas pertidaksamaan padahal numerus harus bernilai positif murni ($> 0$).</sub>

**Pembahasan:** Fungsi logaritma terdefinisi jika numerusnya lebih dari nol:
$$\frac{2x - 6}{x + 5} > 0$$

Langkah 1: Menentukan pembuat nol pembilang dan penyebut.
- Pembilang: $2x - 6 = 0 \implies x = 3$
- Penyebut: $x + 5 = 0 \implies x = -5$

Langkah 2: Uji titik pada garis bilangan dengan pembuat nol $x = -5$ dan $x = 3$:
- Untuk $x < -5$ (misal $x = -6$): $\frac{2(-6) - 6}{-6 + 5} = \frac{-18}{-1} = 18 > 0$ (positif)
- Untuk $-5 < x < 3$ (misal $x = 0$): $\frac{2(0) - 6}{0 + 5} = \frac{-6}{5} < 0$ (negatif)
- Untuk $x > 3$ (misal $x = 4$): $\frac{2(4) - 6}{4 + 5} = \frac{2}{9} > 0$ (positif)

Karena dicari daerah yang bernilai positif ($> 0$), maka daerah asalnya adalah $x < -5$ atau $x > 3$.

Jadi, domain fungsi tersebut adalah $\{x \mid x < -5 \text{ atau } x > 3,\, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11_tl-b06-a-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: pemodelan tekanan atmosfer*

Hubungan antara tekanan udara $P$ (dalam kPa) dan ketinggian suatu tempat $h$ (dalam km) dimodelkan oleh fungsi logaritma alami $\ln\left(\frac{P}{104}\right) = -\frac{h}{8}$. Sebuah stasiun pengamatan $A$ berada pada ketinggian tertentu dengan tekanan udara tercatat sebesar $52\text{ kPa}$. Stasiun pengamatan $B$ berada di puncak gunung yang lebih tinggi dengan tekanan udara tepat separuh dari tekanan di stasiun $A$, yaitu $26\text{ kPa}$. Jika diketahui $\ln 2 \approx 0,693$, selisih ketinggian antara stasiun $B$ dan stasiun $A$ adalah ....

- A. $3,696\text{ km}$  
  <sub>Salah: Siswa salah menghitung $\ln(26/52)$ dengan membagi 8 menjadi $16/3$ atau salah substitusi basis.</sub>
- **B. $5,544\text{ km}$** ✅  
  <sub>Benar: Dari model, $h = -8\ln(P/104)$. Untuk stasiun $A$, $h_A = -8\ln(52/104) = -8\ln(1/2) = 8\ln 2$. Untuk stasiun $B$, $h_B = -8\ln(26/104) = -8\ln(1/4) = 16\ln 2$. Selisih ketinggian $\Delta h = h_B - h_A = 16\ln 2 - 8\ln 2 = 8\ln 2 \approx 8 \times 0,693 = 5,544\text{ km}$.</sub>
- C. $11,088\text{ km}$  
  <sub>Salah: Siswa menjumlahkan kedua ketinggian ($h_A + h_B = 24\ln 2$) alih-alih mencari selisihnya.</sub>
- D. $2,772\text{ km}$  
  <sub>Salah: Siswa salah mengalikan koefisien dengan mengambil $4\ln 2$ bukannya $8\ln 2$.</sub>

**Pembahasan:** Diketahui model: $\ln\left(\frac{P}{104}\right) = -\frac{h}{8} \iff h = -8\ln\left(\frac{P}{104}\right)$.

1. Ketinggian stasiun $A$ ($P_A = 52\text{ kPa}$):
$$h_A = -8\ln\left(\frac{52}{104}\right) = -8\ln\left(\frac{1}{2}\right) = -8(-\ln 2) = 8\ln 2$$

2. Ketinggian stasiun $B$ ($P_B = 26\text{ kPa}$):
$$h_B = -8\ln\left(\frac{26}{104}\right) = -8\ln\left(\frac{1}{4}\right) = -8(-2\ln 2) = 16\ln 2$$

3. Selisih ketinggian:
$$\Delta h = h_B - h_A = 16\ln 2 - 8\ln 2 = 8\ln 2$$
$$\Delta h \approx 8 \times 0,693 = 5,544\text{ km}$$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11_tl-b06-a-hard-bt01-002
*variasi (konteks) | C5 | 3 langkah | jenis: analisis sifat kemonotonan*

Seorang guru memberikan pernyataan berikut kepada kelasnya:
"Untuk setiap bilangan real positif $M$ dan $N$, jika ${}^b\log M < {}^b\log N$, maka selalu berlaku $M < N$."

Empat siswa memberikan evaluasi terhadap pernyataan guru tersebut:
- Andi: "Pernyataan selalu benar untuk semua basis $b > 0, b \neq 1$, karena daerah asal logaritma selalu bilangan real positif."
- Budi: "Pernyataan bernilai salah untuk semua nilai basis $b$, karena tanda ketidaksamaan logaritma selalu berbalik."
- Candra: "Pernyataan bernilai benar jika $b > 1$, tetapi salah jika $0 < b < 1$ karena fungsi logaritma dengan $0 < b < 1$ monoton turun sehingga berakibat $M > N$."
- Dodi: "Pernyataan bernilai benar jika $0 < b < 1$, tetapi salah jika $b > 1$ karena kurva fungsi dengan basis $b > 1$ berada di bawah sumbu-$x$."

Siswa yang memberikan evaluasi dan alasan paling tepat adalah ....

- A. Andi  
  <sub>Salah: Siswa mengabaikan sifat kemonotonan kurva untuk basis pecahan antara 0 dan 1.</sub>
- **B. Candra** ✅  
  <sub>Benar: Sifat 6.3 dan 6.1 menyatakan bahwa untuk $b > 1$, fungsi monoton naik sehingga ${}^b\log M < {}^b\log N \implies M < N$. Sedangkan untuk $0 < b < 1$, fungsi monoton turun sehingga tanda ketaksamaan berbalik menjadi $M > N$.</sub>
- C. Dodi  
  <sub>Salah: Siswa tertukar antara karakteristik basis $b > 1$ dan $0 < b < 1$.</sub>
- D. Budi  
  <sub>Salah: Siswa keliru menganggap pembalikan tanda berlaku untuk semua jenis basis.</sub>

**Pembahasan:** Berdasarkan Sifat 6.3 pada Buku Siswa:
1. Jika $b > 1$, fungsi logaritma bersifat monoton naik, sehingga jika ${}^b\log M < {}^b\log N$, maka $M < N$.
2. Jika $0 < b < 1$, fungsi logaritma bersifat monoton turun, sehingga jika ${}^b\log M < {}^b\log N$, maka $M > N$.

Oleh karena itu, pernyataan guru tidak selalu benar. Pernyataan tersebut hanya benar jika $b > 1$, dan menjadi salah jika $0 < b < 1$. Evaluasi yang tepat diberikan oleh Candra.
**Acuan:** siswa — siswa hal.273 Pemahaman Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11_tl-b06-a-hard-bt01-003
*orisinal | C6 | 4 langkah | jenis: rancang bangun keamanan kata sandi*

Sebuah tim keamanan siber merancang dua skema kata sandi acak. Skema $A$ menggunakan panjang $L_A = 6$ simbol yang dipilih dari sekumpulan $N_A = 64$ simbol unik. Skema $B$ hanya dapat menggunakan sekumpulan $N_B = 16$ simbol unik karena keterbatasan perangkat input. Tim tersebut menginginkan Skema $B$ memiliki entropi informasi ($H$) setidaknya $25\%$ lebih kuat daripada Skema $A$. Berdasarkan rumus $H = L \cdot {}^2\log N$, panjang minimal simbol ($L_B$) yang harus dirancang untuk Skema $B$ adalah ....

- **A. $12\text{ simbol}$** ✅  
  <sub>Benar: $H_A = 6 \times {}^2\log 64 = 6 \times 6 = 36\text{ bit}$. Target $H_B \ge 1,25 \times 36 = 45\text{ bit}$. Untuk Skema $B$, $H_B = L_B \times {}^2\log 16 = 4 L_B$. Maka $4 L_B \ge 45 \implies L_B \ge 11,25$. Karena panjang simbol harus bilangan bulat, $L_B$ minimal adalah 12.</sub>
- B. $9\text{ simbol}$  
  <sub>Salah: Siswa hanya menyamakan entropi $H_B = H_A = 36\text{ bit}$ ($36/4 = 9$) tanpa memperhitungkan kenaikan 25%.</sub>
- C. $11\text{ simbol}$  
  <sub>Salah: Siswa melakukan pembulatan ke bawah dari 11,25 sehingga entropinya belum mencapai target 45 bit.</sub>
- D. $15\text{ simbol}$  
  <sub>Salah: Siswa salah menghitung kenaikan dengan mengalikan panjang simbol langsung $6 \times 1,25$ lalu dikali basis.</sub>

**Pembahasan:** Langkah 1: Hitung entropi Skema $A$ ($N_A = 64 = 2^6$, $L_A = 6$):
$$H_A = L_A \cdot {}^2\log N_A = 6 \cdot {}^2\log(2^6) = 6 \cdot 6 = 36\text{ bit}$$

Langkah 2: Tentukan target entropi Skema $B$ (minimal $25\%$ lebih besar):
$$H_B \ge H_A + 0,25 H_A = 36 + 9 = 45\text{ bit}$$

Langkah 3: Hitung panjang $L_B$ untuk Skema $B$ ($N_B = 16 = 2^4$):
$$H_B = L_B \cdot {}^2\log 16 = L_B \cdot 4$$
$$4 L_B \ge 45 \implies L_B \ge \frac{45}{4} = 11,25$$

Langkah 4: Karena panjang karakter harus bilangan bulat, ambil pembulatan ke atas terkecil:
$$L_B = 12\text{ simbol}$$
**Acuan:** siswa — siswa hal.268

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11_tl-b06-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: pertidaksamaan logaritma bersyarat*

Banyaknya bilangan bulat $x$ yang memenuhi pertidaksamaan logaritma:
$${}^{\frac{1}{2}}\log(x^2 - 2x - 3) \ge -3$$
adalah ....

- A. $7$  
  <sub>Salah: Siswa lupa menguji syarat numerus $x^2 - 2x - 3 > 0$ sehingga menghitung seluruh bilangan bulat dari $-2$ sampai $4$.</sub>
- B. $0$  
  <sub>Salah: Siswa tidak membalik tanda pertidaksamaan pada basis pecahan sehingga menghasilkan daerah tanpa irisan.</sub>
- C. $3$  
  <sub>Salah: Siswa memasukkan nilai $-1$ atau $3$ yang seharusnya tidak termasuk karena numerus harus strictly positif.</sub>
- **D. $2$** ✅  
  <sub>Benar: Syarat numerus: $x^2 - 2x - 3 > 0 \implies x < -1$ atau $x > 3$. Pertidaksamaan: basis $1/2 < 1$ membalik tanda menjadi $x^2 - 2x - 3 \le (1/2)^{-3} = 8 \implies x^2 - 2x - 11 \le 0 \implies 1 - 2\sqrt{3} \le x \le 1 + 2\sqrt{3}$ (kira-kira $-2,46 \le x \le 4,46$). Irisannya adalah $[-2,46; -1) \cup (3; 4,46]$. Bilangan bulat di dalamnya adalah $x = -2$ dan $x = 4$, yaitu sebanyak 2.</sub>

**Pembahasan:** Langkah 1 (Syarat numerus):
$$x^2 - 2x - 3 > 0 \iff (x - 3)(x + 1) > 0$$
$$x < -1 \quad \text{atau} \quad x > 3$$

Langkah 2 (Penyelesaian pertidaksamaan):
Karena basis $b = \frac{1}{2}$ berada pada interval $0 < b < 1$, tanda pertidaksamaan berbalik:
$${}^{\frac{1}{2}}\log(x^2 - 2x - 3) \ge -3 \iff x^2 - 2x - 3 \le \left(\frac{1}{2}\right)^{-3}$$
$$x^2 - 2x - 3 \le 8$$
$$x^2 - 2x - 11 \le 0$$

Akar-akar persamaan $x^2 - 2x - 11 = 0$:
$$x = \frac{2 \pm \sqrt{4 - 4(1)(-11)}}{2} = 1 \pm 2\sqrt{3}$$
Karena $2\sqrt{3} \approx 3,46$, batas nilai $x$ adalah:
$$1 - 3,46 \le x \le 1 + 3,46 \iff -2,46 \le x \le 4,46$$

Langkah 3 (Irisan solusi dan syarat numerus):
$$x \in [-2,46; -1) \cup (3; 4,46]$$

Langkah 4 (Menentukan bilangan bulat):
- Pada interval $[-2,46; -1)$, bilangan bulat yang memenuhi adalah $x = -2$.
- Pada interval $(3; 4,46]$, bilangan bulat yang memenuhi adalah $x = 4$.

Jadi, terdapat tepat 2 bilangan bulat yang memenuhi.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11_tl-b06-a-hard-bt01-005
*variasi (angka) | C5 | 4 langkah | jenis: analisis rasio pengisian baterai*

Lama waktu $t$ (dalam menit) yang diperlukan untuk mengisi daya suatu baterai dari kondisi kosong hingga mencapai daya $C$ dimodelkan oleh fungsi logaritma alami $t = -\frac{1}{k}\ln\left(1 - \frac{C}{C_0}\right)$, dengan $C_0$ adalah kapasitas daya maksimum dan $k$ adalah konstanta pengisian. Rasio lama waktu yang diperlukan untuk mengisi daya baterai hingga $87,5\%$ penuh terhadap lama waktu hingga $50\%$ penuh dengan konstanta $k$ yang sama adalah ....

- A. $1,75 : 1$  
  <sub>Salah: Menganggap hubungan pengisian bersifat linear sehingga membagi langsung persentase kapasitas $87,5 : 50 = 1,75$.</sub>
- B. $2 : 1$  
  <sub>Salah: Keliru mengira pengisian $87,5\%$ setara dengan pengisian $75\%$ di mana $\ln(0,25) = -2\ln 2$.</sub>
- **C. $3 : 1$** ✅  
  <sub>Benar: Waktu hingga $50\%$ penuh adalah $t_1 = -\frac{1}{k}\ln(1 - 0,5) = -\frac{1}{k}\ln(0,5) = \frac{\ln 2}{k}$. Waktu hingga $87,5\%$ penuh adalah $t_2 = -\frac{1}{k}\ln(1 - 0,875) = -\frac{1}{k}\ln(0,125) = -\frac{1}{k}\ln\left(2^{-3}\right) = \frac{3\ln 2}{k}$. Maka rasionya adalah $\frac{t_2}{t_1} = \frac{3\ln 2 / k}{\ln 2 / k} = \frac{3}{1}$.</sub>
- D. $4 : 1$  
  <sub>Salah: Salah menghitung pemangkatan basis pecahan dengan menganggap $0,125 = 2^{-4}$.</sub>

**Pembahasan:** Diketahui model waktu pengisian daya baterai:
$$t = -\frac{1}{k}\ln\left(1 - \frac{C}{C_0}\right)$$

1. Waktu untuk mengisi hingga $50\%$ penuh ($C = 0,5C_0$):
$$t_{50\%} = -\frac{1}{k}\ln(1 - 0,5) = -\frac{1}{k}\ln\left(\frac{1}{2}\right) = -\frac{1}{k}(-\ln 2) = \frac{\ln 2}{k}$$

2. Waktu untuk mengisi hingga $87,5\%$ penuh ($C = 0,875C_0$):
$$t_{87,5\%} = -\frac{1}{k}\ln(1 - 0,875) = -\frac{1}{k}\ln(0,125) = -\frac{1}{k}\ln\left(\frac{1}{8}\right) = -\frac{1}{k}\ln\left(2^{-3}\right) = \frac{3\ln 2}{k}$$

3. Rasio kedua waktu pengisian:
$$\frac{t_{87,5\%}}{t_{50\%}} = \frac{\frac{3\ln 2}{k}}{\frac{\ln 2}{k}} = 3$$

Jadi, rasio waktu yang diperlukan adalah $3 : 1$.
**Acuan:** siswa — siswa hal.271 Contoh 6.7

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11_tl-b06-a-hard-bt01-006
*orisinal | C5 | 5 langkah | jenis: evaluasi perpotongan grafik fungsi logaritma*

Dua grafik fungsi logaritma $f(x) = {}^2\log(x + 4)$ dan $g(x) = {}^2\log(x^2 - 2x - 4)$ diselidiki titik potongnya. Dua orang siswa memberikan argumen berikut:
- **Arya:** "Kedua grafik berpotongan di dua titik karena persamaan $x + 4 = x^2 - 2x - 4$ memiliki dua akar real berbeda dan kedua akar tersebut menghasilkan nilai numerus yang positif."
- **Bella:** "Kedua grafik hanya berpotongan di satu titik karena salah satu akar persamaan bernilai negatif, dan bilangan negatif tidak boleh menjadi nilai $x$ pada fungsi logaritma."

Pernyataan evaluasi yang benar mengenai kedua argumen tersebut adalah ....

- **A. Argumen Arya benar karena kedua nilai $x$ memenuhi syarat numerus $x + 4 > 0$ dan $x^2 - 2x - 4 > 0$** ✅  
  <sub>Benar: Persamaan $x + 4 = x^2 - 2x - 4$ menghasilkan $x^2 - 3x - 8 = 0$ dengan akar-akar $x_1 = \frac{3 + \sqrt{41}}{2} \approx 4,70$ dan $x_2 = \frac{3 - \sqrt{41}}{2} \approx -1,70$. Kedua nilai $x$ ini memenuhi syarat numerus $x > -4$, sehingga numerus $x + 4 > 0$ dan otomatis $x^2 - 2x - 4 = x + 4 > 0$. Nilai $x$ boleh negatif asalkan nilai numerus $(x + 4)$ tetap positif.</sub>
- B. Argumen Arya salah karena titik potong hanya ada jika kedua fungsi memiliki nilai basis yang berbeda  
  <sub>Salah: Miskonsepsi bahwa penyamaan numerus hanya berlaku untuk basis logaritma yang tidak sama.</sub>
- C. Kedua argumen salah karena persamaan kuadrat yang terbentuk tidak memiliki akar real pada himpunan bilangan real  
  <sub>Salah: Salah menghitung nilai diskriminan $D = (-3)^2 - 4(1)(-8) = 41 > 0$.</sub>
- D. Argumen Bella benar karena nilai $x$ pada daerah asal fungsi logaritma selalu disyaratkan harus bernilai positif ($x > 0$)  
  <sub>Salah: Keliru mengira syarat numerus positif selalu berarti variabel $x > 0$, padahal numerusnya adalah $x + 4 > 0$.</sub>

**Pembahasan:** 1. Titik potong diperoleh saat $f(x) = g(x)$:
$${}^2\log(x + 4) = {}^2\log(x^2 - 2x - 4)$$
Berdasarkan identitas logaritma jika ${}^b\log M = {}^b\log N$, maka $M = N$:
$$x + 4 = x^2 - 2x - 4 \iff x^2 - 3x - 8 = 0$$

2. Menentukan akar-akar persamaan kuadrat:
$$x = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(1)(-8)}}{2(1)} = \frac{3 \pm \sqrt{41}}{2}$$
Diperoleh $x_1 = \frac{3 + \sqrt{41}}{2} \approx 4,70$ dan $x_2 = \frac{3 - \sqrt{41}}{2} \approx -1,70$.

3. Uji syarat numerus:
- Syarat fungsi $f(x)$: $x + 4 > 0 \implies x > -4$.
Karena $-1,70 > -4$ dan $4,70 > -4$, kedua nilai $x$ memenuhi syarat numerus $f(x)$.
- Karena pada absis titik potong berlaku $x^2 - 2x - 4 = x + 4$, maka nilai $x^2 - 2x - 4$ juga pasti bernilai positif untuk kedua nilai $x$ tersebut.

4. Kesimpulan:
Nilai variabel $x$ boleh bertanda negatif asalkan membuat bentuk numerus bernilai positif. Oleh karena itu, kedua grafik berpotongan di dua titik dan argumen Arya benar.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11_tl-b06-a-hard-bt01-007
*orisinal | C5 | 5 langkah | jenis: rancang bangun kebijakan keamanan kata sandi*

Sebuah administrator sistem membandingkan dua opsi kebijakan pembuatan kata sandi acak:
- **Kebijakan X:** Menggunakan simbol dari himpunan heksadesimal ($N_X = 16$ simbol) dengan panjang kata sandi $L_X$ karakter.
- **Kebijakan Y:** Menggunakan simbol dari himpunan Base64 ($N_Y = 64$ simbol) dengan panjang kata sandi $L_Y$ karakter.

Diketahui panjang kata sandi Kebijakan Y dirancang $3$ karakter lebih pendek daripada Kebijakan X ($L_Y = L_X - 3$), namun menghasilkan entropi informasi $6\text{ bit}$ lebih besar daripada Kebijakan X ($H_Y - H_X = 6$). Jumlah panjang karakter dari kedua kebijakan kata sandi tersebut ($L_X + L_Y$) adalah ....

- A. $17\text{ karakter}$  
  <sub>Salah: Salah memformulasikan selisih entropi menjadi $6(L_X - 3) - 4L_X = 0$, menghasilkan $L_X = 9$ dan $L_Y = 6$, total 15, lalu menambah 2.</sub>
- B. $27\text{ karakter}$  
  <sub>Salah: Tertukar menghitung basis logaritma dengan menganggap ${}^2\log 16 = 2$ dan ${}^2\log 64 = 3$.</sub>
- C. $25\text{ karakter}$  
  <sub>Salah: Keliru pada tanda kurung saat distribusi menjadi $6L_X - 18 - 4L_X = 6$ dihitung $2L_X = 28 \implies L_X = 14$ dan $L_Y = 11$, total 25.</sub>
- **D. $21\text{ karakter}$** ✅  
  <sub>Benar: $H_X = L_X \cdot {}^2\log 16 = 4L_X$ dan $H_Y = (L_X - 3) \cdot {}^2\log 64 = 6(L_X - 3)$. Persamaan $6(L_X - 3) - 4L_X = 6 \implies 2L_X - 18 = 6 \implies 2L_X = 24 \implies L_X = 12$. Maka $L_Y = 12 - 3 = 9$, sehingga $L_X + L_Y = 12 + 9 = 21$.</sub>

**Pembahasan:** 1. Rumus entropi informasi kata sandi acak:
$$H = L \cdot {}^2\log N$$

2. Menentukan fungsi entropi untuk masing-masing kebijakan:
- Kebijakan X: $N_X = 16 = 2^4$
$$H_X = L_X \cdot {}^2\log(2^4) = 4L_X$$
- Kebijakan Y: $N_Y = 64 = 2^6$ dan $L_Y = L_X - 3$
$$H_Y = (L_X - 3) \cdot {}^2\log(2^6) = 6(L_X - 3) = 6L_X - 18$$

3. Membentuk persamaan berdasarkan informasi $H_Y - H_X = 6\text{ bit}$:
$$(6L_X - 18) - 4L_X = 6$$
$$2L_X - 18 = 6$$
$$2L_X = 24 \iff L_X = 12$$

4. Menghitung panjang kata sandi Kebijakan Y:
$$L_Y = L_X - 3 = 12 - 3 = 9$$

5. Menghitung jumlah panjang kedua kebijakan:
$$L_X + L_Y = 12 + 9 = 21\text{ karakter}$$
**Acuan:** siswa — siswa hal.268

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11_tl-b06-a-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: analisis parameter fungsi logaritma*

Diketahui fungsi logaritma $f(x) = {}^a\log(x^2 - 2bx + c)$ dengan $a > 1$. Grafik fungsi $f(x)$ mencapai nilai minimum sebesar $2$ pada saat $x = 4$. Jika grafik fungsi $f(x)$ memotong sumbu-$y$ di titik $(0, {}^a\log 25)$, nilai dari $a + b + c$ adalah ....

- A. $35$  
  <sub>Salah: Keliru menentukan basis $a$ dengan menyelesaikan $2a = 9 \implies a = 4,5$ lalu membulatkannya.</sub>
- **B. $32$** ✅  
  <sub>Benar: Nilai numerus minimum dicapai pada sumbu simetri $x = b = 4$. Memotong sumbu-$y$ di $x = 0$ menghasilkan numerus $c = 25$. Nilai numerus saat $x = 4$ adalah $4^2 - 2(4)(4) + 25 = 9$. Karena $a > 1$, nilai minimum $f(x)$ tercapai saat numerus minimum: ${}^a\log 9 = 2 \implies a^2 = 9 \implies a = 3$. Maka $a + b + c = 3 + 4 + 25 = 32$.</sub>
- C. $29$  
  <sub>Salah: Lupa menjumlahkan konstanta basis $a$, hanya menghitung $b + c = 4 + 25 = 29$.</sub>
- D. $38$  
  <sub>Salah: Keliru menghitung nilai minimum numerus menjadi $16 - 8 + 25 = 33$ sehingga salah memperoleh nilai parameter.</sub>

**Pembahasan:** 1. Misalkan $g(x) = x^2 - 2bx + c$. Karena $a > 1$, fungsi $f(x) = {}^a\log(g(x))$ monoton naik terhadap $g(x)$, sehingga $f(x)$ mencapai nilai minimum saat fungsi kuadrat $g(x)$ mencapai nilai minimum.

2. Nilai minimum dari $g(x) = x^2 - 2bx + c$ terjadi pada absis titik puncak:
$$x_p = -\frac{-2b}{2(1)} = b$$
Diketahui nilai minimum dicapai pada $x = 4$, maka $b = 4$.

3. Grafik memotong sumbu-$y$ saat $x = 0$:
$$f(0) = {}^a\log(0^2 - 2b(0) + c) = {}^a\log c$$
Diketahui titik potong adalah $(0, {}^a\log 25)$, maka $c = 25$.

4. Menghitung nilai minimum dari $g(x)$ pada $x = 4$:
$$g(4) = 4^2 - 2(4)(4) + 25 = 16 - 32 + 25 = 9$$

5. Menentukan nilai basis $a$:
$$f(4) = {}^a\log(g(4)) = {}^a\log 9 = 2$$
Sesuai definisi logaritma:
$$a^2 = 9 \implies a = 3 \quad (\text{karena } a > 1)$$

6. Menghitung nilai $a + b + c$:
$$a + b + c = 3 + 4 + 25 = 32$$
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11_tl-b06-a-hard-bt01-009
*orisinal | C5 | 6 langkah | jenis: analisis penggabungan intensitas gempa bumi*

Dua peristiwa gempa bumi tercatat pada stasiun pengamatan seismik. Gempa bumi pertama berkekuatan $M_1 = 6,2$ skala Richter, sedangkan gempa bumi kedua berkekuatan $M_2 = 7,2$ skala Richter. Besar kekuatan gempa ditentukan oleh rumus $M = \log\left(\frac{I}{I_0}\right)$, dengan $I$ adalah intensitas gempa dan $I_0$ adalah intensitas gempa tingkat nol. Jika suatu gempa ketiga memiliki intensitas sebesar jumlah intensitas kedua gempa tersebut ($I_3 = I_1 + I_2$), dan diketahui $\log 1,1 \approx 0,041$, kekuatan gempa ketiga dalam skala Richter adalah sekitar ....

- **A. $7,241\text{ skala Richter}$** ✅  
  <sub>Benar: $I_1 = I_0 \cdot 10^{6,2}$ dan $I_2 = I_0 \cdot 10^{7,2} = 10 I_1$. Maka $I_3 = 11 I_1 = 11 \cdot I_0 \cdot 10^{6,2}$. Kekuatan gempa $M_3 = \log(11 \cdot 10^{6,2}) = 6,2 + \log 11 = 6,2 + \log(1,1 \times 10) = 6,2 + 1 + 0,041 = 7,241$ skala Richter.</sub>
- B. $6,700\text{ skala Richter}$  
  <sub>Salah: Menghitung rata-rata aritmetika dari kedua skala gempa $\frac{6,2 + 7,2}{2} = 6,7$.</sub>
- C. $13,400\text{ skala Richter}$  
  <sub>Salah: Langsung menjumlahkan nilai skala Richter $6,2 + 7,2 = 13,4$ tanpa memperhitungkan skala logaritmik.</sub>
- D. $7,204\text{ skala Richter}$  
  <sub>Salah: Lupa mengalikan faktor $10$ pada penguraian $\log 11$ sehingga hanya menambahkan $\log 1,1 = 0,041$ ke $M_1$.</sub>

**Pembahasan:** 1. Hubungan skala Richter dan intensitas gempa:
$$M = \log\left(\frac{I}{I_0}\right) \iff \frac{I}{I_0} = 10^M \iff I = I_0 \cdot 10^M$$

2. Nyatakan intensitas gempa pertama dan kedua:
$$I_1 = I_0 \cdot 10^{6,2}$$
$$I_2 = I_0 \cdot 10^{7,2} = I_0 \cdot 10^{6,2 + 1} = I_0 \cdot 10^{6,2} \cdot 10^1 = 10 I_1$$

3. Menentukan intensitas gempa ketiga ($I_3$):
$$I_3 = I_1 + I_2 = I_1 + 10 I_1 = 11 I_1 = 11 \cdot I_0 \cdot 10^{6,2}$$

4. Menghitung skala Richter gempa ketiga ($M_3$):
$$M_3 = \log\left(\frac{I_3}{I_0}\right) = \log\left(\frac{11 \cdot I_0 \cdot 10^{6,2}}{I_0}\right) = \log(11 \cdot 10^{6,2})$$

5. Menerapkan sifat perkalian logaritma:
$$M_3 = \log 11 + \log(10^{6,2}) = \log(1,1 \times 10) + 6,2$$
$$M_3 = \log 1,1 + \log 10 + 6,2$$

6. Substitusikan nilai $\log 1,1 \approx 0,041$ dan $\log 10 = 1$:
$$M_3 \approx 0,041 + 1 + 6,2 = 7,241\text{ skala Richter}$$

Jadi, kekuatan gempa ketiga adalah sekitar $7,241$ skala Richter.
**Acuan:** siswa — siswa hal.269

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11_tl-b06-a-hard-bt01-010
*variasi (angka) | C5 | 4 langkah | jenis: pemodelan kesetaraan waktu pertumbuhan bakteri*

Dua kultur mikroorganisme diteliti dalam laboratorium. Kultur $A$ membelah diri setiap $2$ jam dengan populasi awal $25$ sel, sehingga waktu yang dibutuhkan untuk mencapai populasi $N$ dirumuskan oleh $t = 2 \cdot {}^2\log\left(\frac{N}{25}\right)$ jam. Kultur $B$ membelah diri setiap $3$ jam dengan populasi awal $200$ sel, dengan waktu yang dibutuhkan memenuhi $t = 3 \cdot {}^2\log\left(\frac{N}{200}\right)$ jam. Jika kedua kultur berkembang biak secara bersamaan dari waktu $t = 0$, lama waktu $t$ yang dibutuhkan hingga kedua kultur memiliki banyak populasi yang sama ($N$) adalah ....

- A. $9\text{ jam}$  
  <sub>Salah: Siswa menghitung nilai ${}^2\log(512) = 9$, tetapi lupa mengalikan dengan pengali 2 pada rumus waktu.</sub>
- B. $24\text{ jam}$  
  <sub>Salah: Siswa menyamakan argumen tanpa memangkatkan dengan koefisien: $\frac{N}{25} = \frac{N}{200}$, lalu mengambil KPK waktu pembelahan $2 \times 3 \times 4$.</sub>
- **C. $18\text{ jam}$** ✅  
  <sub>Benar: Menyetarakan kedua fungsi waktu: $2 \cdot {}^2\log\left(\frac{N}{25}\right) = 3 \cdot {}^2\log\left(\frac{N}{200}\right) \iff \left(\frac{N}{25}\right)^2 = \left(\frac{N}{200}\right)^3$. Diperoleh $\frac{N^2}{625} = \frac{N^3}{8.000.000} \iff N = \frac{8.000.000}{625} = 12.800$. Substitusi nilai $N$ ke rumus waktu: $t = 2 \cdot {}^2\log\left(\frac{12.800}{25}\right) = 2 \cdot {}^2\log(512) = 2 \cdot 9 = 18\text{ jam}$.</sub>
- D. $12\text{ jam}$  
  <sub>Salah: Siswa salah mengoperasikan pangkat identitas logaritma menjadi perkalian koefisien, menghasilkan nilai $N$ yang keliru sehingga $t = 12\text{ jam}$.</sub>

**Pembahasan:** Diketahui:
$$t = 2 \cdot {}^2\log\left(\frac{N}{25}\right)$$
$$t = 3 \cdot {}^2\log\left(\frac{N}{200}\right)$$

Karena waktu $t$ dan populasi $N$ sama, samakan kedua persamaan:
$$2 \cdot {}^2\log\left(\frac{N}{25}\right) = 3 \cdot {}^2\log\left(\frac{N}{200}\right)$$

Gunakan sifat logaritma $p \cdot {}^b\log M = {}^b\log(M^p)$:
$${}^2\log\left(\left(\frac{N}{25}\right)^2\right) = {}^2\log\left(\left(\frac{N}{200}\right)^3\right)$$
$$\left(\frac{N}{25}\right)^2 = \left(\frac{N}{200}\right)^3$$
$$\frac{N^2}{625} = \frac{N^3}{8.000.000}$$

Bagi kedua ruas dengan $N^2$ ($N \ne 0$):
$$\frac{1}{625} = \frac{N}{8.000.000} \implies N = \frac{8.000.000}{625} = 12.800$$

Substitusikan $N = 12.800$ ke salah satu rumus waktu:
$$t = 2 \cdot {}^2\log\left(\frac{12.800}{25}\right) = 2 \cdot {}^2\log(512) = 2 \cdot 9 = 18\text{ jam}$$

Jadi, waktu yang dibutuhkan adalah $18\text{ jam}$.
**Acuan:** siswa — siswa hal.273 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11_tl-b06-a-hard-bt01-011
*orisinal | C5 | 5 langkah | jenis: pertidaksamaan logaritma bersarang*

Banyaknya bilangan bulat $x$ yang memenuhi pertidaksamaan logaritma bersarang:
$${}^{\frac{1}{2}}\log\left({}^3\log(x^2 - 7)\right) \ge -1$$
adalah ....

- A. $6$  
  <sub>Salah: Siswa memakai syarat numerus terdalam $x^2 - 7 > 0 \implies x^2 > 7$, sehingga memasukkan nilai yang keliru atau salah mengiriskan rentang.</sub>
- **B. $4$** ✅  
  <sub>Benar: Syarat numerus luar: ${}^3\log(x^2 - 7) > 0 \iff x^2 - 7 > 1 \iff x^2 > 8$. Menyelesaikan pertidaksamaan utama dengan basis $0 < \frac{1}{2} < 1$: tanda berbalik sehingga ${}^3\log(x^2 - 7) \le \left(\frac{1}{2}\right)^{-1} = 2$. Karena basis $3 > 1$, didapat $x^2 - 7 \le 3^2 = 9 \iff x^2 \le 16$. Irisan keduanya menghasilkan $8 < x^2 \le 16$. Nilai bilangan bulat $x$ yang memenuhi adalah $x \in \{-4, -3, 3, 4\}$, sehingga totalnya ada 4 bilangan bulat.</sub>
- C. $2$  
  <sub>Salah: Siswa hanya memperhitungkan nilai bulat positif $x \in \{3, 4\}$ dan mengabaikan nilai negatif.</sub>
- D. $8$  
  <sub>Salah: Siswa tidak membalik tanda pertidaksamaan pada basis $\frac{1}{2}$ sehingga batas penyelesaian menjadi kacau.</sub>

**Pembahasan:** Selesaikan pertidaksamaan secara bertahap:
1. Syarat numerus terdalam:
$$x^2 - 7 > 0 \iff x^2 > 7$$

2. Syarat numerus terluar:
$${}^3\log(x^2 - 7) > 0 \iff x^2 - 7 > 3^0 \iff x^2 - 7 > 1 \iff x^2 > 8$$
Irisan syarat numerus adalah $x^2 > 8$.

3. Pertidaksamaan utama:
$${}^{\frac{1}{2}}\log\left({}^3\log(x^2 - 7)\right) \ge -1$$
Karena basis $b = \frac{1}{2}$ berada pada interval $0 < b < 1$, arah pertidaksamaan berbalik:
$${}^3\log(x^2 - 7) \le \left(\frac{1}{2}\right)^{-1}$$
$${}^3\log(x^2 - 7) \le 2$$

Karena basis $3 > 1$, arah pertidaksamaan tetap:
$$x^2 - 7 \le 3^2 \iff x^2 - 7 \le 9 \iff x^2 \le 16$$

4. Menggabungkan hasil pertidaksamaan dan syarat numerus:
$$8 < x^2 \le 16$$

5. Menentukan bilangan bulat $x$:
Nilai $x^2$ yang memenuhi dengan $x \in \mathbb{Z}$ adalah $x^2 = 9$ atau $x^2 = 16$.
- Untuk $x^2 = 9 \implies x = -3$ atau $x = 3$
- Untuk $x^2 = 16 \implies x = -4$ atau $x = 4$

Nilai bulat yang memenuhi adalah $\{-4, -3, 3, 4\}$, yaitu ada sebanyak $4$ bilangan bulat.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11_tl-b06-a-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: analisis parameter fungsi logaritma ekstremum*

Diberikan suatu fungsi logaritma $f(x) = {}^a\log(kx - x^2)$ dengan basis $a > 1$ dan $k$ adalah konstanta real positif. Grafik fungsi $f(x)$ memiliki sumbu simetri pada garis $x = 6$ serta mencapai nilai maksimum sebesar $2$. Nilai dari $a + k$ adalah ....

- A. $14$  
  <sub>Salah: Siswa salah menentukan nilai puncak numerus menjadi $64$ sehingga $a^2 = 64 \implies a = 8$, lalu $k = 6$ menghasilkan $14$.</sub>
- B. $12$  
  <sub>Salah: Siswa salah mengira $k = 6$ (mengambil langsung dari sumbu simetri tanpa membagi 2), sehingga $a + k = 6 + 6 = 12$.</sub>
- C. $24$  
  <sub>Salah: Siswa menghitung $k = 12$, tetapi menyimpulkan $a = \sqrt{144} = 12$ akibat salah menghitung nilai puncak numerus.</sub>
- **D. $18$** ✅  
  <sub>Benar: Numerus $g(x) = kx - x^2$ merupakan parabola membuka ke bawah dengan sumbu simetri $x = -\frac{k}{2(-1)} = \frac{k}{2}$. Karena sumbu simetri $x = 6$, didapat $\frac{k}{2} = 6 \iff k = 12$. Nilai maksimum numerus terjadi pada $x = 6$, yaitu $g(6) = 12(6) - 6^2 = 36$. Karena basis $a > 1$, fungsi logaritma monoton naik sehingga nilai maksimum $f(x)$ terjadi saat numerus maksimum: $f_{\max} = {}^a\log(36) = 2 \iff a^2 = 36$. Karena $a > 1$, maka $a = 6$. Diperoleh $a + k = 6 + 12 = 18$.</sub>

**Pembahasan:** Misalkan $g(x) = kx - x^2 = -x^2 + kx$ adalah numerus dari $f(x)$.

1. Sumbu simetri dari fungsi kuadrat $g(x)$ adalah:
$$x = -\frac{b}{2a_{\text{kuadrat}}} = -\frac{k}{2(-1)} = \frac{k}{2}$$
Diketahui sumbu simetri berada di $x = 6$:
$$\frac{k}{2} = 6 \implies k = 12$$

2. Fungsi numerus menjadi $g(x) = 12x - x^2$. Nilai maksimum numerus tercapai pada sumbu simetrinya ($x = 6$):
$$g(6) = 12(6) - 6^2 = 72 - 36 = 36$$

3. Karena basis $a > 1$, fungsi logaritma $f(x) = {}^a\log(g(x))$ bersifat monoton naik. Oleh karena itu, $f(x)$ mencapai nilai maksimum ketika $g(x)$ mencapai nilai maksimumnya:
$$f_{\max} = {}^a\log(36)$$

Diketahui $f_{\max} = 2$, sehingga:
$${}^a\log(36) = 2 \iff a^2 = 36$$
Karena syarat basis logaritma $a > 1$, maka $a = 6$.

4. Menghitung nilai $a + k$:
$$a + k = 6 + 12 = 18$$

Jadi, nilai dari $a + k$ adalah $18$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11_tl-b06-a-hard-bt01-013
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi rasio tekanan atmosfer*

Hubungan antara tekanan udara $P$ (dalam $\text{kPa}$) dan ketinggian tempat $h$ (dalam $\text{km}$) di atas permukaan laut dimodelkan oleh persamaan logaritma alami:
$$\ln\left(\frac{P}{100}\right) = -\frac{h}{7}$$
Sebuah wahana penelitian mengukur tekanan udara pada ketinggian $h_1 = 2,1\text{ km}$ dan mencatat tekanan sebesar $P_1$. Wahana tersebut kemudian naik ke ketinggian $h_2 = 9,1\text{ km}$ dan mencatat tekanan sebesar $P_2$. Rasio tekanan udara $\frac{P_2}{P_1}$ adalah ....

- A. $\frac{1}{e^2}$  
  <sub>Salah: Salah menghitung selisih ketinggian menjadi 14 km sehingga didapat pangkat -2.</sub>
- B. $\frac{1}{10}$  
  <sub>Salah: Keliru menganggap basis fungsi adalah logaritma umum (basis 10) bukan logaritma alami (basis e).</sub>
- C. $e$  
  <sub>Salah: Terbalik menempatkan pembilang dan penyebut pada rasio tekanan sehingga menghasilkan nilai resiprokal.</sub>
- **D. $\frac{1}{e}$** ✅  
  <sub>Benar: Pengurangan kedua persamaan logaritma menghasilkan $\ln(P_2/P_1) = -(9,1 - 2,1)/7 = -1$, sehingga rasio $P_2/P_1 = e^{-1} = \frac{1}{e}$.</sub>

**Pembahasan:** Diketahui model: $\ln\left(\frac{P}{100}\right) = -\frac{h}{7}$.
1. Untuk ketinggian $h_1 = 2,1\text{ km}$:
$$\ln P_1 - \ln 100 = -\frac{2,1}{7} = -0,3$$
2. Untuk ketinggian $h_2 = 9,1\text{ km}$:
$$\ln P_2 - \ln 100 = -\frac{9,1}{7} = -1,3$$
3. Kurangkan kedua persamaan:
$$(\ln P_2 - \ln 100) - (\ln P_1 - \ln 100) = -1,3 - (-0,3)$$
$$\ln\left(\frac{P_2}{P_1}\right) = -1,0 = -1$$
4. Berdasarkan definisi logaritma alami (basis $e$):
$$\frac{P_2}{P_1} = e^{-1} = \frac{1}{e}$$
**Acuan:** siswa — siswa hal.273 Penerapan Konsep

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11_tl-b06-a-hard-bt01-014
*orisinal | C5 | 5 langkah | jenis: evaluasi validitas penyelesaian logaritma*

Seorang siswa menyelesaikan persamaan logaritma ${}^3\log(x - 2) + {}^3\log(x - 4) = 1$ dengan tahapan berikut:
- **Langkah 1:** Menggunakan sifat penjumlahan: ${}^3\log((x - 2)(x - 4)) = 1$
- **Langkah 2:** Mengubah ke bentuk eksponen: $(x - 2)(x - 4) = 3^1$
- **Langkah 3:** Menjabarkan persamaan kuadrat: $x^2 - 6x + 8 = 3 \iff x^2 - 6x + 5 = 0$
- **Langkah 4:** Memfaktorkan: $(x - 5)(x - 1) = 0$, diperoleh $x = 5$ atau $x = 1$
- **Langkah 5:** Menyimpulkan bahwa himpunan penyelesaian persamaan tersebut adalah $\{1, 5\}$.

Evaluasi yang tepat terhadap hasil penyelesaian siswa tersebut adalah ....

- **A. Kesimpulan salah pada Langkah 5 karena $x = 1$ menyebabkan numerus bernilai negatif sehingga penyelesaiannya hanya $x = 5$** ✅  
  <sub>Benar: Untuk $x = 1$, nilai numerus $(x - 2) = -1 < 0$ dan $(x - 4) = -3 < 0$, melanggar syarat numerus logaritma real.</sub>
- B. Kesimpulan salah pada Langkah 2 karena seharusnya bentuk eksponennya adalah $(x - 2)(x - 4) = 1^3$  
  <sub>Salah: Tertukar antara penempatan basis dan hasil nilai logaritma saat konversi ke bentuk eksponensial.</sub>
- C. Kesimpulan benar karena kedua nilai $x = 1$ dan $x = 5$ memenuhi persamaan kuadrat pada Langkah 3  
  <sub>Salah: Mengabaikan syarat eksistensi numerus fungsi logaritma awal dan hanya terpaku pada persamaan kuadrat turunan.</sub>
- D. Kesimpulan salah sejak Langkah 1 karena sifat penjumlahan logaritma hanya berlaku jika basisnya berbeda  
  <sub>Salah: Keliru memahami sifat penjumlahan logaritma yang justru mewajibkan basisnya bernilai sama.</sub>

**Pembahasan:** 1. Pada Langkah 1 hingga 4 aljabar penyelesaian telah benar.
2. Namun, berdasarkan Definisi dan Sifat 6.2, fungsi ${}^3\log(u)$ hanya terdefinisi untuk numerus positif ($u > 0$).
3. Syarat numerus:
- $x - 2 > 0 \implies x > 2$
- $x - 4 > 0 \implies x > 4$
Irisan kedua syarat mengharuskan $x > 4$.
4. Uji nilai yang diperoleh:
- Untuk $x = 5$: $5 > 4$ (memenuhi syarat).
- Untuk $x = 1$: $1 < 4$, menyebabkan $(1 - 2) = -1 < 0$ (tidak memenuhi syarat numerus).
5. Jadi, Langkah 5 salah menarik kesimpulan karena $x = 1$ bukan penyelesaian valid; solusinya hanya $x = 5$.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11_tl-b06-a-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: perancangan optimasi entropi kata sandi*

Sebuah sistem autentikasi perbankan awalnya menggunakan kata sandi dengan panjang $L_1 = 8$ karakter yang dipilih secara acak dari sekumpulan $N_1 = 64$ simbol. Untuk mempermudah input pengguna pada perangkat layar sentuh, penyedia layanan memutuskan untuk mempersempit pilihan simbol menjadi hanya $N_2 = 8$ simbol. Agar entropi informasi ($H$) dari kata sandi baru minimal sama dengan kekuatan kata sandi lama, panjang karakter minimal ($L_2$) yang harus dirancang adalah ....

- A. $24\text{ karakter}$  
  <sub>Salah: Keliru menganggap ${}^2\log 8 = 2$ sehingga $48 / 2 = 24$.</sub>
- B. $12\text{ karakter}$  
  <sub>Salah: Keliru membagi $48$ dengan $4$ bukan dengan basis logaritma ${}^2\log 8 = 3$.</sub>
- **C. $16\text{ karakter}$** ✅  
  <sub>Benar: $H_1 = 8 \cdot {}^2\log 64 = 8 \times 6 = 48\text{ bit}$. Untuk sistem baru: $L_2 \cdot {}^2\log 8 \ge 48 \iff 3L_2 \ge 48 \iff L_2 \ge 16$.</sub>
- D. $64\text{ karakter}$  
  <sub>Salah: Menggunakan perkalian linear proporsi simbol tanpa menerapkan relasi logaritmik.</sub>

**Pembahasan:** Rumus entropi informasi: $H = L \cdot {}^2\log N$.
1. Hitung entropi sistem mula-mula:
$$H_1 = L_1 \cdot {}^2\log(N_1) = 8 \cdot {}^2\log(64)$$
Karena $64 = 2^6$, maka ${}^2\log 64 = 6$.
$$H_1 = 8 \times 6 = 48\text{ bit}$$
2. Tentukan syarat entropi sistem baru:
$$H_2 \ge H_1 \implies L_2 \cdot {}^2\log(N_2) \ge 48$$
3. Diketahui $N_2 = 8 = 2^3$, sehingga ${}^2\log 8 = 3$:
$$L_2 \cdot 3 \ge 48$$
$$L_2 \ge \frac{48}{3} = 16$$
Jadi, panjang karakter minimal yang harus dirancang adalah $16$ karakter.
**Acuan:** siswa — siswa hal.268

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11_tl-b06-a-hard-bt01-016
*variasi (angka) | C5 | 4 langkah | jenis: analisis selisih ketinggian model atmosfer*

Hubungan antara tekanan udara $P$ (dalam kPa) dan ketinggian tempat $h$ (dalam km) di atas permukaan laut dimodelkan oleh persamaan logaritma alami:
$$\ln\left(\frac{P}{120}\right) = -\frac{h}{8}$$
Dua stasiun meteorologi $A$ dan $B$ mengukur tekanan udara pada saat yang sama. Stasiun $A$ mencatat tekanan udara sebesar $60\text{ kPa}$, sedangkan stasiun $B$ yang berada pada tempat lebih tinggi mencatat tekanan udara sebesar $15\text{ kPa}$. Selisih ketinggian antara stasiun $B$ dan stasiun $A$ ($h_B - h_A$) adalah ....

- A. $32\ln 2\text{ km}$  
  <sub>Salah: Siswa menjumlahkan kedua ketinggian ($h_B + h_A = 24\ln 2 + 8\ln 2$) bukan mencari selisihnya.</sub>
- **B. $16\ln 2\text{ km}$** ✅  
  <sub>Benar: Dari model $\ln(P/120) = -h/8$, diperoleh fungsi ketinggian $h = -8\ln(P/120) = 8\ln(120/P)$. Maka $h_A = 8\ln(120/60) = 8\ln 2$ dan $h_B = 8\ln(120/15) = 8\ln 8 = 8\ln(2^3) = 24\ln 2$. Selisih ketinggiannya adalah $h_B - h_A = 24\ln 2 - 8\ln 2 = 16\ln 2\text{ km}$.</sub>
- C. $8\ln 2\text{ km}$  
  <sub>Salah: Siswa hanya menghitung ketinggian stasiun $A$ ($8\ln 2$) dan lupa mengurangkannya dari ketinggian stasiun $B$.</sub>
- D. $24\ln 2\text{ km}$  
  <sub>Salah: Siswa hanya menghitung ketinggian stasiun $B$ ($24\ln 2$) tanpa menghitung selisihnya terhadap stasiun $A$.</sub>

**Pembahasan:** Dari rumus pemodelan:
$$\ln\left(\frac{P}{120}\right) = -\frac{h}{8} \iff h = 8\ln\left(\frac{120}{P}\right)$$
Ketinggian stasiun $A$ ($P_A = 60\text{ kPa}$):
$$h_A = 8\ln\left(\frac{120}{60}\right) = 8\ln 2$$
Ketinggian stasiun $B$ ($P_B = 15\text{ kPa}$):
$$h_B = 8\ln\left(\frac{120}{15}\right) = 8\ln 8 = 8\ln(2^3) = 24\ln 2$$
Selisih ketinggian antara stasiun $B$ dan stasiun $A$:
$$h_B - h_A = 24\ln 2 - 8\ln 2 = 16\ln 2\text{ km}$$
**Acuan:** pretest — kelas11_tl-b06-p0273-latihan-a-8

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas11_tl-b06-a-hard-bt01-017
*orisinal | C5 | 4 langkah | jenis: analisis pertidaksamaan logaritma rasional*

Himpunan semua bilangan real $x$ yang memenuhi pertidaksamaan logaritma:
$${}^{\frac{1}{3}}\log\left(\frac{x - 1}{x + 5}\right) \ge -1$$
adalah ....

- A. $\{x \mid x \le -8 \text{ atau } x > -5,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa lupa mengiriskan hasil pertidaksamaan dengan syarat keberadaan numerus logaritma $((x - 1)/(x + 5) > 0)$.</sub>
- B. $\{x \mid -8 \le x < -5,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa lupa membalik tanda pertidaksamaan saat mengoperasikan basis antara 0 dan 1, sehingga menyelesaikan $(x - 1)/(x + 5) \ge 3$.</sub>
- C. $\{x \mid x < -5 \text{ atau } x \ge 8,\, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa melakukan kesalahan tanda aljabar saat memindahkan konstanta 3 sehingga mendapatkan pembuat nol $x = 8$ bukan $x = -8$.</sub>
- **D. $\{x \mid x \le -8 \text{ atau } x > 1,\, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat numerus mengharuskan $(x - 1)/(x + 5) > 0$, yaitu $x < -5$ atau $x > 1$. Karena basis $b = 1/3$ berada pada interval $0 < b < 1$, tanda pertidaksamaan berbalik menjadi $(x - 1)/(x + 5) \le (1/3)^{-1} = 3$. Penyelesaian dari $(x - 1)/(x + 5) - 3 \le 0$ menghasilkan $(x + 8)/(x + 5) \ge 0$, yaitu $x \le -8$ atau $x > -5$. Irisan kedua syarat tersebut adalah $x \le -8$ atau $x > 1$.</sub>

**Pembahasan:** Langkah 1: Tentukan syarat numerus:
$$\frac{x - 1}{x + 5} > 0 \iff x < -5 \text{ atau } x > 1$$

Langkah 2: Selesaikan pertidaksamaan logaritma. Karena basis $0 < \frac{1}{3} < 1$, arah pertidaksamaan berbalik:
$${}^{\frac{1}{3}}\log\left(\frac{x - 1}{x + 5}\right) \ge -1 \iff \frac{x - 1}{x + 5} \le \left(\frac{1}{3}\right)^{-1} = 3$$

Langkah 3: Selesaikan pertidaksamaan pecahan:
$$\frac{x - 1}{x + 5} - 3 \le 0 \iff \frac{x - 1 - 3(x + 5)}{x + 5} \le 0$$
$$\frac{-2x - 16}{x + 5} \le 0 \iff \frac{-2(x + 8)}{x + 5} \le 0 \iff \frac{x + 8}{x + 5} \ge 0$$
Pembuat nol adalah $x = -8$ dan $x = -5$. Nilai yang memenuhi adalah $x \le -8$ atau $x > -5$.

Langkah 4: Iriskan dengan syarat numerus:
$$(x \le -8 \text{ atau } x > -5) \cap (x < -5 \text{ atau } x > 1)$$
- Untuk $x \le -8$, seluruh interval ini terletak pada $x < -5$, sehingga memenuhi.
- Untuk interval $(-5, \infty)$, irisannya dengan $(x < -5 \text{ atau } x > 1)$ adalah $x > 1$.

Dengan demikian, himpunan penyelesaiannya adalah $\{x \mid x \le -8 \text{ atau } x > 1,\, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.266

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas11_tl-b06-a-hard-bt01-018
*orisinal | C5 | 4 langkah | jenis: rekonstruksi fungsi logaritma kurva*

Suatu fungsi logaritma memiliki bentuk umum $f(x) = {}^a\log(x - h) + k$ dengan $a > 0$ dan $a \ne 1$. Grafik fungsi $f(x)$ memiliki asimtot tegak pada garis $x = 3$, memotong sumbu-$x$ di titik $(7, 0)$, serta melalui titik $(19, 2)$. Nilai dari $f(67)$ adalah ....

- A. $2$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan logaritma dasar dengan menganggap ${}^2\log 64 = 4$, lalu mengurangkannya dengan 2.</sub>
- B. $8$  
  <sub>Salah: Siswa keliru menentukan tanda pergeseran vertikal menjadi $k = +2$, menghasilkan $6 + 2 = 8$.</sub>
- **C. $4$** ✅  
  <sub>Benar: Dari asimtot tegak diperoleh $h = 3$. Titik potong sumbu-$x$ memberikan $k = -{}^a\log 4$, dan titik $(19, 2)$ menghasilkan persamaan ${}^a\log 16 - {}^a\log 4 = 2 \iff {}^a\log 4 = 2 \iff a = 2$. Dengan demikian $k = -2$, sehingga $f(67) = {}^2\log(67 - 3) - 2 = 6 - 2 = 4$.</sub>
- D. $6$  
  <sub>Salah: Siswa lupa memperhitungkan translasi vertikal $k = -2$, sehingga hanya menghitung nilai ${}^2\log 64 = 6$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $h$.
Asimtot tegak grafik fungsi logaritma terjadi ketika nilai numerus sama dengan nol, yaitu $x - h = 0$. Karena diketahui garis asimtot tegaknya adalah $x = 3$, maka diperoleh:
$$h = 3$$
Fungsi menjadi $f(x) = {}^a\log(x - 3) + k$.

Langkah 2: Menggunakan titik potong sumbu-$x$ pada $(7, 0)$.
$$f(7) = {}^a\log(7 - 3) + k = 0$$
$${}^a\log(4) + k = 0 \implies k = -{}^a\log 4$$

Langkah 3: Menggunakan titik $(19, 2)$ untuk mencari basis $a$ dan nilai $k$.
$$f(19) = {}^a\log(19 - 3) + k = 2$$
$${}^a\log(16) + (-{}^a\log 4) = 2$$
Berdasarkan identitas logaritma pembagian:
$${}^a\log\left(\frac{16}{4}\right) = 2$$
$${}^a\log 4 = 2 \implies a^2 = 4$$
Karena basis $a > 0$ dan $a \ne 1$, diperoleh $a = 2$.
Maka nilai pergeseran vertikal adalah:
$$k = -{}^2\log 4 = -2$$
Rumus fungsi secara lengkap adalah $f(x) = {}^2\log(x - 3) - 2$.

Langkah 4: Menghitung nilai $f(67)$.
$$f(67) = {}^2\log(67 - 3) - 2 = {}^2\log(64) - 2 = 6 - 2 = 4$$
Jadi, nilai dari $f(67)$ adalah $4$.
**Acuan:** siswa — siswa hal.264

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas11_tl-b06-a-hard-bt01-019
*orisinal | C5 | 4 langkah | jenis: evaluasi keabsahan akar persamaan logaritma*

Dua orang siswa, Budi dan Sinta, menganalisis banyaknya penyelesaian real dari persamaan logaritma:
$${}^2\log(x^2 - 2x) = {}^2\log(4x - 5)$$
Budi menyatakan ada 2 penyelesaian real, yaitu $x = 1$ dan $x = 5$, karena kedua nilai tersebut diperoleh dari persamaan aljabar $x^2 - 2x = 4x - 5$.
Sinta menyatakan hanya ada 1 penyelesaian real, yaitu $x = 5$, karena $x = 1$ tidak memenuhi syarat numerus logaritma.

Evaluasi yang paling tepat terhadap pernyataan kedua siswa tersebut adalah ....

- **A. Argumen Sinta benar karena untuk $x = 1$ nilai numerus menjadi negatif sehingga fungsi logaritma tidak terdefinisi pada bilangan real.** ✅  
  <sub>Benar: Menyamakan numerus menghasilkan $x^2 - 6x + 5 = 0$ dengan akar $x = 1$ dan $x = 5$. Namun, syarat numerus mensyaratkan $x^2 - 2x > 0$ dan $4x - 5 > 0$. Nilai $x = 1$ menghasilkan $1^2 - 2(1) = -1 < 0$, sehingga bukan solusi yang sah.</sub>
- B. Argumen keduanya salah karena baik $x = 1$ maupun $x = 5$ tidak memenuhi persamaan awal jika disubstitusikan kembali.  
  <sub>Salah: Siswa keliru menguji nilai $x = 5$, padahal $x = 5$ menghasilkan ${}^2\log(15) = {}^2\log(15)$ yang valid.</sub>
- C. Argumen Budi benar karena pemfaktoran persamaan kuadrat telah dilakukan secara benar dan menghasilkan dua nilai real berbeda.  
  <sub>Salah: Siswa mengabaikan syarat keharusan numerus bernilai positif pada fungsi logaritma.</sub>
- D. Argumen keduanya salah karena persamaan kuadrat $x^2 - 6x + 5 = 0$ memiliki nilai diskriminan negatif sehingga tidak memiliki akar real.  
  <sub>Salah: Siswa salah menghitung diskriminan persamaan kuadrat ($D = 36 - 20 = 16 > 0$).</sub>

**Pembahasan:** Langkah 1: Menentukan penyelesaian persamaan aljabar dari kesamaan numerus.
Berdasarkan identitas jika ${}^b\log M = {}^b\log N$, maka $M = N$, diperoleh:
$$x^2 - 2x = 4x - 5$$
$$x^2 - 6x + 5 = 0$$
$$(x - 1)(x - 5) = 0$$
Maka diperoleh calon penyelesaian $x = 1$ atau $x = 5$.

Langkah 2: Menentukan syarat numerus fungsi logaritma.
Definisi fungsi logaritma mengharuskan numerus bernilai positif ($M > 0$ dan $N > 0$):
1) $x^2 - 2x > 0 \iff x(x - 2) > 0 \iff x < 0$ atau $x > 2$
2) $4x - 5 > 0 \iff x > \frac{5}{4}$
Irisan kedua syarat tersebut adalah $x > 2$.

Langkah 3: Menguji calon penyelesaian terhadap syarat numerus.
- Untuk $x = 1$:
Numerus pertama: $1^2 - 2(1) = -1 \le 0$ (tidak memenuhi syarat numerus).
Numerus kedua: $4(1) - 5 = -1 \le 0$ (tidak memenuhi syarat numerus).
Karena logaritma dari bilangan negatif tidak terdefinisi pada himpunan bilangan real, $x = 1$ bukan penyelesaian.
- Untuk $x = 5$:
Numerus pertama: $5^2 - 2(5) = 15 > 0$ (memenuhi).
Numerus kedua: $4(5) - 5 = 15 > 0$ (memenuhi).
Nilai $x = 5$ berada dalam daerah $x > 2$, sehingga $x = 5$ merupakan penyelesaian yang sah.

Langkah 4: Mengevaluasi klaim.
Argumen Sinta benar karena memperhitungkan syarat numerus yang menggugurkan $x = 1$, sedangkan Budi salah karena mengabaikan syarat domain logaritma.
**Acuan:** siswa — siswa hal.265

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 60. [hard] kelas11_tl-b06-a-hard-bt01-020
*orisinal | C5 | 5 langkah | jenis: pemodelan kesetaraan peluruhan nilai*

Nilai jual dua unit mesin pabrik, yaitu mesin A dan mesin B, mengalami penyusutan seiring berjalannya waktu $t$ (dalam tahun) mengikuti model peluruhan $H(t) = c e^{-kt}$. Mesin A dibeli baru seharga Rp80 juta dan setelah 2 tahun nilainya menjadi Rp40 juta. Sementara itu, mesin B dibeli baru seharga Rp270 juta dan setelah 2 tahun nilainya menjadi Rp90 juta. Jika laju peluruhan masing-masing mesin konstan, setelah berapa tahun pemakaian nilai jual kedua mesin tersebut akan bernilai sama?

- A. $4\text{ tahun}$  
  <sub>Salah: Siswa salah saat menyederhanakan rasio perpangkatan dan mengira eksponen yang terbentuk adalah $t/2 = 2$ sehingga $t = 4$.</sub>
- B. $3\text{ tahun}$  
  <sub>Salah: Siswa lupa memperhitungkan faktor periode 2 tahun pada eksponen, sehingga langsung menyimpulkan $t = 3$ dari pangkat $(2/3)^3$.</sub>
- **C. $6\text{ tahun}$** ✅  
  <sub>Benar: Menyamakan kedua fungsi peluruhan $H_A(t) = H_B(t)$ menghasilkan $80 \cdot 2^{-t/2} = 270 \cdot 3^{-t/2}$, yang ekuivalen dengan $(2/3)^{t/2} = 8/27 = (2/3)^3$, sehingga $t/2 = 3$ atau $t = 6\text{ tahun}$.</sub>
- D. $8\text{ tahun}$  
  <sub>Salah: Siswa keliru mengidentifikasi $8/27$ sebagai $(2/3)^4$ sehingga menyimpulkan $t/2 = 4$ atau $t = 8$.</sub>

**Pembahasan:** Berdasarkan model peluruhan $H(t) = c e^{-kt}$:

1. **Untuk Mesin A:**
- Pada saat $t = 0$, $H_A(0) = c_A = 80$.
- Pada saat $t = 2$, $H_A(2) = 80 e^{-2k_A} = 40 \implies e^{-2k_A} = \frac{1}{2} \implies e^{-k_A} = 2^{-1/2}$.
- Rumus fungsi nilainya adalah $H_A(t) = 80(2^{-1/2})^t = 80 \cdot 2^{-t/2}$.

2. **Untuk Mesin B:**
- Pada saat $t = 0$, $H_B(0) = c_B = 270$.
- Pada saat $t = 2$, $H_B(2) = 270 e^{-2k_B} = 90 \implies e^{-2k_B} = \frac{1}{3} \implies e^{-k_B} = 3^{-1/2}$.
- Rumus fungsi nilainya adalah $H_B(t) = 270(3^{-1/2})^t = 270 \cdot 3^{-t/2}$.

3. **Menentukan Waktu Nilai Jual Sama ($H_A(t) = H_B(t)$):**
$$
\begin{aligned}
80 \cdot 2^{-t/2} &= 270 \cdot 3^{-t/2} \\
\frac{80}{270} &= \frac{3^{-t/2}}{2^{-t/2}} \\
\frac{8}{27} &= \left(\frac{2}{3}\right)^{t/2} \\
\left(\frac{2}{3}\right)^3 &= \left(\frac{2}{3}\right)^{t/2}
\end{aligned}
$$

Karena bilangan pokok kedua ruas sama, diperoleh:
$$
\frac{t}{2} = 3 \implies t = 6
$$

Jadi, nilai jual kedua mesin tersebut akan bernilai sama setelah $6\text{ tahun}$ pemakaian.
**Acuan:** siswa — siswa hal.271

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
