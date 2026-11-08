# Lembar koreksi — kelas11 SMA11U-B1 subbab A: Fungsi

56 soal | easy 20, medium 20, hard 16 | variasi 28, orisinal 28
> **Kapasitas kurang (hard): 16 dari kuota 20** — 10 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas11-b01-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: domain fungsi irasional*

Domain dari fungsi $f(x) = \sqrt{x - 7} + 9$ pada himpunan bilangan riil adalah ....

- A. $\{x \mid x \ge -7, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah memindahkan tanda negatif saat menyelesaikan pertidaksamaan linear $x - 7 \ge 0$.</sub>
- B. $\{x \mid x > 7, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah mengira bentuk di dalam akar harus positif ketat, padahal nilai nol juga diperbolehkan.</sub>
- **C. $\{x \mid x \ge 7, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Bentuk akar terdefinisi pada bilangan riil jika bilangan di dalam akar tak negatif, sehingga $x - 7 \ge 0 \iff x \ge 7$.</sub>
- D. $\{x \mid x \ge 9, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa tertukar antara syarat nilai masukan (domain) dengan konstanta luaran (range).</sub>

**Pembahasan:** Agar $f(x) = \sqrt{x - 7} + 9$ terdefinisi pada bilangan riil, ekspresi di dalam tanda akar harus tak negatif:
$$x - 7 \ge 0 \implies x \ge 7$$
Konstanta $+9$ memengaruhi daerah hasil (range), bukan domain.
Jadi, domain fungsi tersebut adalah $\{x \mid x \ge 7, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas11-b01-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: nilai fungsi eksponensial*

Berdasarkan data pencatatan, pada tahun 2010 sebuah toko berhasil menjual $4$ unit printer. Pada tahun 2011 dan 2012 toko tersebut berturut-turut berhasil menjual $8$ dan $16$ unit printer. Apabila pola penjualan antar-tahun tersebut membentuk fungsi eksponensial, berapa banyak penjualan printer pada tahun 2015?

- A. $64$ unit  
  <sub>Salah: Siswa salah menghitung selisih tahun, menghitung untuk tahun 2014 ($4 \times 2^4 = 64$).</sub>
- B. $24$ unit  
  <sub>Salah: Siswa mengira pola merupakan fungsi linear berbaris aritmetika dengan beda $4$ per tahun ($4 + 5 \times 4 = 24$).</sub>
- **C. $128$ unit** ✅  
  <sub>Benar: Penjualan berlipat ganda setiap tahun ($r = 2$), sehingga pada tahun 2015 penjualannya adalah $4 \times 2^{5} = 128$ unit.</sub>
- D. $256$ unit  
  <sub>Salah: Siswa kelebihan satu pangkat dalam menghitung perkalian eksponen ($4 \times 2^6 = 256$).</sub>

**Pembahasan:** Fungsi penjualan printer dapat dimodelkan sebagai fungsi eksponensial:
$$P(t) = P_0 \cdot r^{t - 2010}$$
Diketahui:
- Tahun 2010 ($t = 2010$): $P = 4$
- Tahun 2011 ($t = 2011$): $P = 8$
Rasio pengali $r = \frac{8}{4} = 2$.
Untuk tahun 2015 ($t = 2015$):
$$P(2015) = 4 \times 2^{2015 - 2010} = 4 \times 2^5 = 4 \times 32 = 128\text{ unit}.$$
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas11-b01-a-easy-bt01-003
*variasi (konteks) | C1 | 1 langkah | jenis: identifikasi fungsi*

Hubungan konversi ukuran suhu dari derajat Celsius ($C$) ke skala Fahrenheit ($F$) dirumuskan dengan $F = \frac{9}{5}C + 32$. Apakah relasi yang memetakan suhu dalam Celsius ke Fahrenheit tersebut merupakan suatu fungsi?

- A. Bukan, karena ada nilai suhu Celsius yang dapat menghasilkan dua nilai suhu Fahrenheit berbeda.  
  <sub>Salah: Siswa salah memahami konsep pemetaan rumus aljabar linear.</sub>
- **B. Ya, karena setiap nilai suhu Celsius dipasangkan dengan tepat satu nilai suhu Fahrenheit.** ✅  
  <sub>Benar: Setiap satu nilai masukan $C$ menghasilkan tepat satu nilai keluaran unik $F$ melalui rumus linear tersebut.</sub>
- C. Bukan, karena suhu Fahrenheit selalu memiliki angka yang lebih besar daripada suhu Celsius.  
  <sub>Salah: Siswa mengaitkan status fungsi dengan besar-kecilnya nilai angka keluaran.</sub>
- D. Ya, karena nilai suhu pada skala Fahrenheit tidak pernah bernilai negatif.  
  <sub>Salah: Siswa berasumsi salah mengenai daerah hasil fungsi tanpa merujuk definisi pemetaan tunggal.</sub>

**Pembahasan:** Suatu relasi dikatakan fungsi jika setiap anggota himpunan masukan (domain) terhubung ke tepat satu anggota himpunan keluaran (kodomain).
Pada rumus $F = \frac{9}{5}C + 32$, substitusi sebuah nilai $C$ tertentu selalu menghasilkan nilai tunggal yang pasti untuk $F$. Oleh karena itu, relasi konversi suhu tersebut merupakan fungsi.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas11-b01-a-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: tes garis vertikal*

Berdasarkan tes garis vertikal, suatu relasi pada bidang Kartesius dinyatakan bukan merupakan fungsi apabila ....

- A. grafik relasi tidak melalui titik asal $(0, 0)$ pada bidang koordinat  
  <sub>Salah: Siswa membuat aturan keliru bahwa fungsi harus melewati titik pusat koordinat.</sub>
- B. terdapat garis horizontal yang memotong grafik di dua atau lebih titik yang berbeda  
  <sub>Salah: Siswa tertukar antara tes garis vertikal (uji fungsi) dengan tes garis horizontal (uji fungsi satu-satu/invers).</sub>
- **C. terdapat garis vertikal yang memotong grafik di dua atau lebih titik yang berbeda** ✅  
  <sub>Benar: Jika garis vertikal memotong di lebih dari satu titik, berarti satu nilai masukan $x$ memiliki lebih dari satu nilai luaran $y$, melanggar syarat fungsi.</sub>
- D. setiap garis vertikal memotong grafik tepat pada satu titik  
  <sub>Salah: Siswa menyebutkan kriteria untuk relasi yang merupakan fungsi.</sub>

**Pembahasan:** Tes garis vertikal digunakan untuk menguji apakah suatu kurva pada grafik Kartesius adalah fungsi. Jika kita dapat menemukan setidaknya satu garis vertikal yang memotong grafik di dua titik atau lebih, itu berarti ada nilai $x$ yang memiliki lebih dari satu pasangan nilai $y$. Oleh karena itu, relasi tersebut bukan fungsi.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas11-b01-a-easy-bt01-005
*orisinal | C2 | 1 langkah | jenis: pasangan berurutan fungsi*

Diketahui himpunan $A = \{1, 2, 3\}$ dan himpunan $B = \{a, b, c\}$. Di antara himpunan pasangan berurutan berikut, manakah yang merupakan fungsi dari himpunan $A$ ke himpunan $B$?

- **A. $\{(1, a), (2, b), (3, b)\}$** ✅  
  <sub>Benar: Setiap anggota $A$ ($1, 2, 3$) muncul tepat satu kali sebagai elemen pertama dalam pasangan.</sub>
- B. $\{(1, a), (3, c)\}$  
  <sub>Salah: Siswa tidak menyadari elemen $2 \in A$ tidak memiliki pasangan sama sekali.</sub>
- C. $\{(1, b), (1, c), (3, a)\}$  
  <sub>Salah: Siswa mengabaikan elemen $1$ bercabang dan elemen $2$ tidak dipasangkan.</sub>
- D. $\{(1, a), (2, b), (2, c), (3, a)\}$  
  <sub>Salah: Siswa tidak menyadari elemen $2 \in A$ memiliki dua pasangan yang berbeda ($b$ dan $c$).</sub>

**Pembahasan:** Syarat relasi dari $A$ ke $B$ merupakan fungsi:
1. Setiap anggota $A$ harus memiliki pasangan di $B$.
2. Setiap anggota $A$ hanya boleh memiliki tepat satu pasangan di $B$.

Pemeriksaan opsi:
- $\{(1, a), (2, b), (3, b)\}$: Anggota $1, 2, 3$ masing-masing dipasangkan tepat satu kali. Ini adalah fungsi.
- $\{(1, a), (2, b), (2, c), (3, a)\}$: Bukan fungsi karena $2$ bercabang ke $b$ dan $c$.
- $\{(1, a), (3, c)\}$: Bukan fungsi karena $2$ tidak memiliki pasangan.
- $\{(1, b), (1, c), (3, a)\}$: Bukan fungsi karena $1$ bercabang dan $2$ tidak memiliki pasangan.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas11-b01-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: range fungsi kuadrat*

Daerah hasil (*range*) dari fungsi kuadrat $f(x) = x^2 + 5$ dengan domain $x \in \mathbb{R}$ adalah ....

- A. $\{y \mid y \le 5, y \in \mathbb{R}\}$  
  <sub>Salah: Terbalik mengartikan nilai minimum parabola terbuka ke atas sebagai batas atas (maksimum).</sub>
- B. $\{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Hanya melihat sifat non-negatif dari $x^2$ tanpa menambahkan konstanta $+5$.</sub>
- C. $\{y \mid y \ge -5, y \in \mathbb{R}\}$  
  <sub>Salah: Salah tanda pada konstanta saat menentukan nilai puncak fungsi.</sub>
- **D. $\{y \mid y \ge 5, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Karena $x^2 \ge 0$ untuk setiap $x \in \mathbb{R}$, nilai minimum tercapai di $x = 0$ yaitu $f(0) = 5$. Jadi, daerah hasil fungsi adalah $y \ge 5$.</sub>

**Pembahasan:** Fungsi kuadrat $f(x) = x^2 + 5$ memiliki grafik berupa parabola terbuka ke atas dengan titik puncak $(0, 5)$. Karena nilai kuadrat bilangan riil selalu memenuhi $x^2 \ge 0$, maka:
$$f(x) = x^2 + 5 \ge 0 + 5 = 5$$
Dengan demikian, daerah hasil (*range*) dari fungsi tersebut adalah $\{y \mid y \ge 5, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas11-b01-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: range fungsi irasional*

Daerah hasil (*range*) dari fungsi $f(x) = \sqrt{x - 6} + 8$ pada himpunan bilangan riil adalah ....

- **A. $\{y \mid y \ge 8, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Nilai bentuk akar $\sqrt{x - 6} \ge 0$ untuk setiap $x \ge 6$, sehingga nilai terkecil $f(x)$ adalah $0 + 8 = 8$.</sub>
- B. $\{y \mid y \ge 6, y \in \mathbb{R}\}$  
  <sub>Salah: Tertukar antara batas domain ($x \ge 6$) dengan batas range.</sub>
- C. $\{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Mengabaikan penjumlahan konstanta $+8$ di luar tanda akar.</sub>
- D. $\{y \mid y \le 8, y \in \mathbb{R}\}$  
  <sub>Salah: Salah menggunakan tanda ketaksamaan sehingga nilai minimum dianggap sebagai nilai maksimum.</sub>

**Pembahasan:** Agar terdefinisi pada bilangan riil, bentuk di dalam tanda akar harus tak-negatif: $x - 6 \ge 0 \implies x \ge 6$.
Nilai akar kuadrat prinsipal selalu non-negatif, yaitu $\sqrt{x - 6} \ge 0$.
Oleh karena itu, nilai fungsi memenuhi:
$$f(x) = \sqrt{x - 6} + 8 \ge 0 + 8 = 8$$
Jadi, daerah hasil (*range*) dari fungsi tersebut adalah $\{y \mid y \ge 8, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas11-b01-a-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: evaluasi relasi fungsi*

Hubungan konversi satuan panjang dari kaki ($k$) ke satuan meter ($m$) didefinisikan dengan relasi $m = 0,3k$. Apakah relasi yang memasangkan setiap ukuran dalam kaki ke meter merupakan fungsi?

- A. Ya, karena satu ukuran dalam kaki dapat menghasilkan dua nilai berbeda dalam meter tergantung pembulatan.  
  <sub>Salah: Menyetujui relasi adalah fungsi namun dengan alasan bercabang yang justru melanggar syarat fungsi.</sub>
- **B. Ya, karena setiap satu nilai panjang dalam satuan kaki berkorespondensi dengan tepat satu nilai panjang dalam satuan meter.** ✅  
  <sub>Benar: Sesuai definisi fungsi, setiap elemen daerah asal (kaki) dipetakan ke tepat satu elemen daerah kawan (meter).</sub>
- C. Bukan, karena faktor pengali $0,3$ merupakan bilangan desimal berulang.  
  <sub>Salah: Mengira jenis bilangan koefisien mempengaruhi status relasi sebagai fungsi atau bukan.</sub>
- D. Bukan, karena satu nilai panjang dalam meter dapat memiliki lebih dari satu nilai dalam kaki.  
  <sub>Salah: Terbalik meninjau pemetaan dari meter ke kaki dan salah memahami sifat relasi satu-satu.</sub>

**Pembahasan:** Suatu relasi disebut fungsi jika setiap anggota daerah asal memiliki tepat satu pasangan di daerah kawan. Pada persamaan $m = 0,3k$, untuk setiap nilai $k$ tertentu hanya akan menghasilkan tepat satu nilai $m$ yang tunggal. Oleh karena itu, relasi tersebut merupakan fungsi.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas11-b01-a-easy-bt01-009
*orisinal | C2 | 1 langkah | jenis: nilai fungsi*

Sebuah fungsi didefinisikan dengan rumus $f(x) = 5x - 7$. Jika nilai masukan (*input*) adalah $x = 4$, maka nilai keluaran (*output*) $f(x)$ adalah ....

- **A. $13$** ✅  
  <sub>Benar: Substitusi nilai $x = 4$ menghasilkan $f(4) = 5(4) - 7 = 20 - 7 = 13$.</sub>
- B. $27$  
  <sub>Salah: Salah operasi pada konstanta dengan melakukan penjumlahan: $20 + 7 = 27$ bukannya pengurangan.</sub>
- C. $9$  
  <sub>Salah: Lupa mengalikan dengan $5$, hanya menghitung $(5 + 4) - 7$ atau salah hitung aritmetika dasar.</sub>
- D. $-15$  
  <sub>Salah: Salah urutan operasi: menghitung $5 \times (4 - 7) = 5 \times (-3) = -15$.</sub>

**Pembahasan:** Diketahui fungsi $f(x) = 5x - 7$. Untuk masukan $x = 4$, kita substitusikan langsung ke dalam persamaan:
$$f(4) = 5(4) - 7 = 20 - 7 = 13$$
Jadi, nilai keluaran yang dihasilkan adalah $13$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas11-b01-a-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: definisi daerah fungsi*

Dalam konsep pemetaan atau fungsi, himpunan semua nilai keluaran (*output*) nyata yang dihasilkan dari pemetaan anggota daerah asal disebut ....

- A. *domain* (daerah asal)  
  <sub>Salah: Tertukar dengan himpunan semua nilai masukan (*input*).</sub>
- **B. *range* (daerah hasil)** ✅  
  <sub>Benar: *Range* adalah himpunan seluruh elemen keluaran aktual yang diperoleh dari hasil pemetaan nilai masukan.</sub>
- C. *kodomain* (daerah kawan)  
  <sub>Salah: Tertukar dengan himpunan sasaran yang memuat kemungkinan hasil, bukan hasil nyata.</sub>
- D. *relasi* (hubungan himpunan)  
  <sub>Salah: Menyebutkan konsep umum hubungan dua himpunan, bukan himpunan nilai keluaran.</sub>

**Pembahasan:** Berdasarkan definisi dasar fungsi:
- *Domain* adalah daerah asal (himpunan semua nilai masukan).
- *Kodomain* adalah daerah kawan (himpunan yang memuat seluruh kemungkinan keluaran).
- *Range* adalah daerah hasil, yaitu himpunan semua nilai keluaran nyata yang diperoleh dari pemetaan *domain*.
Jadi, istilah yang dimaksud adalah *range* (daerah hasil).
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas11-b01-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: pertumbuhan eksponensial*

Berdasarkan catatan penjualan, pada tahun 2015 sebuah toko berhasil menjual $5$ unit sepeda. Pada tahun 2016 dan 2017, toko tersebut berturut-turut menjual $15$ dan $45$ unit sepeda. Apabila relasi antara tahun dan jumlah penjualan membentuk fungsi eksponensial, berapakah jumlah penjualan sepeda pada tahun 2019?

- A. $1.215$ unit  
  <sub>Salah: Kelebihan satu periode pemangkatan ($5 \times 3^5 = 1.215$).</sub>
- B. $85$ unit  
  <sub>Salah: Menganggap bertambah konstan menurut beda aritmetika $+40$ tiap tahun ($45 + 40 = 85$).</sub>
- **C. $405$ unit** ✅  
  <sub>Benar: Rasio penjualan per tahun adalah $\frac{15}{5} = 3$. Penjualan pada tahun 2019 ($t = 4$ tahun setelah 2015) adalah $5 \times 3^4 = 5 \times 81 = 405$ unit.</sub>
- D. $135$ unit  
  <sub>Salah: Hanya menghitung penjualan sampai tahun 2018 ($5 \times 3^3 = 135$).</sub>

**Pembahasan:** Model penjualan eksponensial dinyatakan dengan rumus $f(t) = a \cdot r^t$, dengan $a = 5$ pada tahun dasar 2015 ($t = 0$).
Rasio pertumbuhan per tahun:
$$r = \frac{15}{5} = 3$$
Untuk tahun 2019, selisih tahun dari 2015 adalah $t = 2019 - 2015 = 4$.
Jumlah penjualan pada tahun 2019:
$$f(4) = 5 \times 3^4 = 5 \times 81 = 405\text{ unit}$$
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas11-b01-a-easy-bt01-012
*variasi (konteks) | C1 | 1 langkah | jenis: formulasi fungsi konversi*

Hubungan antara ukuran suhu dalam derajat Reamur ($R$) dan derajat Celsius ($C$) dinyatakan dengan kesetaraan $R = \frac{4}{5}C$. Rumus fungsi yang menyatakan suhu Reamur sebagai fungsi dari suhu Celsius adalah ....

- A. $R(C) = \frac{4}{5}C + 32$  
  <sub>Salah: Tercampur dengan konstanta konversi skala Fahrenheit.</sub>
- **B. $R(C) = \frac{4}{5}C$** ✅  
  <sub>Benar: Variabel masukan adalah suhu Celsius ($C$) dan keluarannya adalah Reamur ($R$), sehingga dirumuskan $R(C) = \frac{4}{5}C$.</sub>
- C. $R(C) = C - \frac{4}{5}$  
  <sub>Salah: Keliru menggunakan operasi pengurangan alih-alih pengali rasio skala.</sub>
- D. $R(C) = \frac{5}{4}C$  
  <sub>Salah: Tertukar dengan rumus fungsi invers (suhu Celsius dari Reamur).</sub>

**Pembahasan:** Karena suhu dalam derajat Reamur dinyatakan terhadap suhu dalam derajat Celsius, maka suhu Celsius ($C$) menjadi variabel input dan suhu Reamur ($R$) menjadi variabel output. Dengan hubungan $R = \frac{4}{5}C$, rumus fungsinya adalah $R(C) = \frac{4}{5}C$.
**Acuan:** siswa — siswa hal.32 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas11-b01-a-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: variabel fungsi*

Pada notasi fungsi $y = f(x)$, variabel $x$ dan $y$ masing-masing berperan sebagai ....

- A. variabel keluaran (*output*) dan variabel masukan (*input*)  
  <sub>Salah: Posisi peran input dan output tertukar.</sub>
- B. variabel bebas yang keduanya merupakan keluaran (*output*)  
  <sub>Salah: Keliru menganggap kedua variabel memiliki fungsi keluaran yang sama.</sub>
- C. daerah hasil (*range*) dan daerah kawan (*kodomain*)  
  <sub>Salah: Mengacaukan nama variabel nilai tunggal dengan nama himpunan relasi.</sub>
- **D. variabel masukan (*input*) dan variabel keluaran (*output*)** ✅  
  <sub>Benar: Sesuai definisi fungsi $y = f(x)$, $x$ adalah elemen yang dimasukkan (*input*) dan $y$ adalah hasil yang diperoleh (*output*).</sub>

**Pembahasan:** Pada bentuk formal $f(x) = y$, nilai $x$ adalah elemen asal yang dimasukkan ke dalam mesin fungsi (variabel masukan/input), sedangkan $y$ adalah nilai yang dihasilkan oleh aturan pemetaan fungsi tersebut (variabel keluaran/output).
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas11-b01-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: syarat relasi fungsi*

Suatu relasi dari himpunan $A$ ke himpunan $B$ disebut sebagai fungsi jika dan hanya jika ....

- A. semua anggota di $A$ dan $B$ saling berpasangan tanpa ada yang tersisa  
  <sub>Salah: Merupakan definisi korespondensi satu-satu (bijektif), bukan definisi umum fungsi.</sub>
- **B. setiap anggota di $A$ dipasangkan dengan tepat satu anggota di $B$** ✅  
  <sub>Benar: Definisi fungsi mengharuskan setiap anggota daerah asal memiliki pasangan dan pasangannya tunggal.</sub>
- C. setidaknya ada satu anggota di $A$ yang memiliki lebih dari satu pasangan di $B$  
  <sub>Salah: Kondisi ini justru menyebabkan relasi bukan merupakan fungsi.</sub>
- D. setiap anggota di $B$ dipasangkan dengan tepat satu anggota di $A$  
  <sub>Salah: Tertukar dengan syarat pemetaan satu-satu atau fungsi invers.</sub>

**Pembahasan:** Berdasarkan definisi dasar matematika sekolah, relasi dari himpunan masukan $A$ ke himpunan keluaran $B$ merupakan fungsi apabila setiap anggota himpunan $A$ dihubungkan dengan tepat satu anggota di himpunan $B$. Anggota di $A$ tidak boleh bercabang pasangannya dan tidak boleh ada anggota $A$ yang tidak memiliki pasangan.
**Acuan:** siswa — siswa hal.22

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas11-b01-a-easy-bt01-015
*variasi (konteks) | C2 | 1 langkah | jenis: klasifikasi fungsi waktu*

Apakah relasi antara suhu udara di suatu stasiun cuaca terhadap waktu pencatatan selama satu hari merupakan suatu fungsi? Jelaskan alasannya.

- A. Bukan fungsi, karena nilai suhu udara yang sama dapat terjadi pada beberapa waktu pencatatan yang berbeda.  
  <sub>Salah: Keliru mengira output tidak boleh bernilai sama untuk input berbeda.</sub>
- B. Bukan fungsi, karena suhu udara di stasiun cuaca dapat mengalami fluktuasi tajam sewaktu-waktu.  
  <sub>Salah: Terkecoh faktor fisik cuaca alih-alih definisi matematis fungsi.</sub>
- C. Ya, merupakan fungsi karena nilai suhu udara selalu meningkat seiring berjalannya waktu pencatatan.  
  <sub>Salah: Mengira fungsi harus selalu monoton naik.</sub>
- **D. Ya, merupakan fungsi karena pada setiap satu waktu pencatatan hanya terdapat tepat satu nilai suhu udara yang terukur.** ✅  
  <sub>Benar: Berdasarkan definisi fungsi, setiap elemen waktu pencatatan (domain) berpasangan dengan tepat satu nilai suhu udara (kodomain).</sub>

**Pembahasan:** Suatu relasi disebut fungsi jika setiap anggota himpunan masukan dipasangkan dengan tepat satu anggota himpunan keluaran. Karena pada setiap waktu pemantauan suhu udara hanya memiliki tepat satu nilai terukur, maka relasi tersebut merupakan fungsi.
**Acuan:** siswa — siswa hal.24 Latihan 1.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas11-b01-a-easy-bt01-016
*variasi (konteks) | C2 | 1 langkah | jenis: relasi besaran waktu*

Apakah relasi antara ketinggian permukaan air pada suatu bendungan terhadap waktu pemantauan dalam satu hari merupakan suatu fungsi? Jelaskan alasannya.

- A. Bukan fungsi, karena ketinggian air yang sama dapat terulang pada beberapa jam pemantauan yang berbeda.  
  <sub>Salah: Tertukar antara syarat pemetaan relasi dengan relasi satu-satu (injektif).</sub>
- B. Ya, merupakan fungsi karena ketinggian air selalu bernilai positif pada setiap pemantauan.  
  <sub>Salah: Mengaitkan fungsi dengan kepositifan nilai variabel keluaran.</sub>
- C. Bukan fungsi, karena volume air bendungan selalu berubah dipengaruhi oleh debit air hujan.  
  <sub>Salah: Menghubungkan sifat fungsi dengan dinamika fisis air bendungan.</sub>
- **D. Ya, merupakan fungsi karena pada setiap satu waktu pemantauan hanya terdapat tepat satu nilai ketinggian air.** ✅  
  <sub>Benar: Setiap titik waktu pengukuran hanya menghasilkan satu tinggi permukaan air spesifik sehingga memenuhi syarat fungsi.</sub>

**Pembahasan:** Dalam relasi ini, waktu pemantauan bertindak sebagai variabel masukan (domain) dan ketinggian air sebagai keluaran (range). Karena setiap saat dipantau ketinggian air hanya bernilai tunggal, relasi ini memenuhi syarat sebagai fungsi.
**Acuan:** siswa — siswa hal.24 Latihan 1.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas11-b01-a-easy-bt01-017
*variasi (konteks) | C2 | 1 langkah | jenis: fungsi konversi ukuran*

Diketahui hubungan konversi satuan panjang dari meter ($m$) ke sentimeter ($s$) adalah $1\text{ m} = 100\text{ cm}$. Rumus fungsi $s(m)$ yang menyatakan ukuran panjang dalam sentimeter terhadap ukuran panjang dalam meter adalah ....

- **A. $s(m) = 100m$** ✅  
  <sub>Benar: Setiap $m$ meter bernilai $100 \times m$ sentimeter, sehingga rumusnya $s(m) = 100m$.</sub>
- B. $s(m) = \frac{100}{m}$  
  <sub>Salah: Membuat fungsi perbandingan berbalik nilai.</sub>
- C. $s(m) = m + 100$  
  <sub>Salah: Menggunakan operasi penjumlahan karena salah menafsirkan kesetaraan satuan.</sub>
- D. $s(m) = \frac{m}{100}$  
  <sub>Salah: Salah menggunakan operasi pembagian alih-alih perkalian.</sub>

**Pembahasan:** Karena $1\text{ m} = 100\text{ cm}$, maka untuk nilai panjang $m$ meter berlaku $s = 100 \times m$. Dalam notasi fungsi diperoleh $s(m) = 100m$.
**Acuan:** siswa — siswa hal.32 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas11-b01-a-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: pemahaman sumbu grafik fungsi*

Jika suatu relasi disajikan dalam bentuk grafik pada bidang koordinat Kartesius, daerah asal (*domain*) dan daerah hasil (*range*) dari grafik fungsi tersebut masing-masing ditentukan oleh nilai-nilai pada ....

- A. sumbu $x$ untuk *domain* dan titik potong sumbu $y$ untuk *range*  
  <sub>Salah: Mengira range hanya berupa nilai konstanta perpotongan sumbu y.</sub>
- B. sumbu $y$ untuk *domain* dan sumbu $x$ untuk *range*  
  <sub>Salah: Tertukar antara variabel bebas masukan (sumbu x) dan variabel terikat keluaran (sumbu y).</sub>
- C. titik asal $(0,0)$ untuk *domain* dan gradien garis untuk *range*  
  <sub>Salah: Salah konsep mengaitkan titik pusat dan kemiringan garis.</sub>
- **D. sumbu $x$ untuk *domain* dan sumbu $y$ untuk *range*** ✅  
  <sub>Benar: Berdasarkan representasi grafik koordinat Kartesius, sumbu horizontal ($x$) memuat domain dan sumbu vertikal ($y$) memuat range.</sub>

**Pembahasan:** Pada bidang koordinat Kartesius, sumbu horizontal ($x$) memuat nilai variabel masukan yang menjadi daerah asal (*domain*), sedangkan sumbu vertikal ($y$) memuat nilai keluaran yang menjadi daerah hasil (*range*).
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas11-b01-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: definisi daerah asal*

Dalam konsep fungsi matematika, himpunan seluruh nilai masukan (*input*) yang diperbolehkan untuk diproses oleh suatu fungsi disebut ....

- A. *range* (daerah hasil)  
  <sub>Salah: Tertukar antara himpunan nilai masukan dengan himpunan nilai keluaran nyata.</sub>
- B. *kodomain* (daerah kawan)  
  <sub>Salah: Terkecoh menganggap kodomain sebagai masukan.</sub>
- **C. *domain* (daerah asal)** ✅  
  <sub>Benar: Himpunan semua nilai masukan yang sah ke dalam suatu fungsi secara baku disebut domain atau daerah asal.</sub>
- D. relasi  
  <sub>Salah: Menyebutkan istilah hubungan umum dua himpunan, bukan daerah masukan.</sub>

**Pembahasan:** Himpunan semua nilai masukan (*input*) pada suatu fungsi disebut *domain* (daerah asal). Himpunan nilai yang mungkin menjadi pasangan keluaran disebut *kodomain* (daerah kawan), dan hasil pemetaan sebenarnya disebut *range* (daerah hasil).
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas11-b01-a-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: daerah hasil fungsi kuadrat*

Daerah hasil (*range*) dari fungsi kuadrat $f(x) = x^2 - 16$ dengan daerah asal himpunan bilangan riil adalah ....

- **A. $\{y \mid y \ge -16, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Karena $x^2 \ge 0$ untuk setiap bilangan riil $x$, maka nilai minimum $f(x)$ dicapai saat $x = 0$ yaitu $f(0) = -16$. Dengan demikian, daerah hasilnya adalah $\{y \mid y \ge -16, y \in \mathbb{R}\}$.</sub>
- B. $\{y \mid y \le -16, y \in \mathbb{R}\}$  
  <sub>Salah: Terbalik dalam menentukan arah pertidaksamaan nilai ekstrim, menganggap -16 sebagai nilai maksimum.</sub>
- C. $\{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Hanya meninjau sifat non-negatif dari $x^2 \ge 0$ tanpa mengurangkannya dengan 16.</sub>
- D. $\{y \mid y \ge 16, y \in \mathbb{R}\}$  
  <sub>Salah: Mengalami kesalahan tanda pada konstanta fungsi kuadrat sehingga mengira nilai minimumnya adalah 16.</sub>

**Pembahasan:** Diketahui fungsi kuadrat $f(x) = x^2 - 16$ dengan domain $x \in \mathbb{R}$.
Untuk setiap bilangan riil $x$, berlaku sifat $x^2 \ge 0$.
Kurangkan kedua ruas dengan 16:
$x^2 - 16 \ge 0 - 16$
$f(x) \ge -16$

Jadi, daerah hasil (*range*) fungsi tersebut adalah $\{y \mid y \ge -16, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas11-b01-a-medium-bt01-001
*variasi (angka) | C3 | 3 langkah | jenis: fungsi eksponensial*

Berdasarkan data penjualan, pada tahun 2020 sebuah perusahaan rintisan berhasil menjual $6$ unit produk. Pada tahun 2021 dan 2022, perusahaan tersebut berhasil menjual masing-masing $24$ dan $96$ unit produk. Apabila relasi antara tahun dan jumlah penjualan produk membentuk fungsi eksponensial, berapa perkiraan penjualan produk tersebut pada tahun 2025?

- A. $1.536$ unit  
  <sub>Salah: Siswa salah menghitung selisih tahun menjadi 4 tahun ($6 \times 4^4 = 1.536$).</sub>
- **B. $6.144$ unit** ✅  
  <sub>Benar: Rasio pertumbuhan tiap tahun adalah $r = \frac{24}{6} = 4$. Model penjualan pada tahun ke-$t$ dihitung dengan $f(t) = 6 \times 4^{t - 2020}$. Untuk tahun 2025 ($t - 2020 = 5$), penjualannya adalah $f(2025) = 6 \times 4^5 = 6 \times 1.024 = 6.144$ unit.</sub>
- C. $2.400$ unit  
  <sub>Salah: Siswa salah menganggap model linier dengan kenaikan tetap selisih awal.</sub>
- D. $24.576$ unit  
  <sub>Salah: Siswa salah menghitung pangkat tahun menjadi 6 tahun ($6 \times 4^6 = 24.576$).</sub>

**Pembahasan:** Langkah 1: Tentukan rasio pertumbuhan penjualan per tahun: $r = \frac{24}{6} = 4$.
Langkah 2: Tuliskan rumus fungsi penjualan untuk tahun $t$: $P(t) = 6 \times 4^{t - 2020}$.
Langkah 3: Hitung penjualan untuk tahun 2025: $P(2025) = 6 \times 4^{2025 - 2020} = 6 \times 4^5 = 6 \times 1.024 = 6.144$ unit.
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas11-b01-a-medium-bt01-002
*variasi (angka) | C3 | 3 langkah | jenis: domain dan range fungsi*

Diketahui fungsi $f(x) = \sqrt{2x - 8} + 5$ terdefinisi pada himpunan bilangan riil $\mathbb{R}$. Daerah asal (*domain*) dan daerah hasil (*range*) dari fungsi $f(x)$ berturut-turut adalah ....

- A. $D_f = \{x \mid x \ge 4, x \in \mathbb{R}\}$ dan $R_f = \{y \mid y \ge 0, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengabaikan konstanta $+5$ dalam menentukan nilai minimum daerah hasil.</sub>
- B. $D_f = \{x \mid x \le 4, x \in \mathbb{R}\}$ dan $R_f = \{y \mid y \le 5, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa membalik tanda pertidaksamaan daerah asal dan daerah hasil.</sub>
- **C. $D_f = \{x \mid x \ge 4, x \in \mathbb{R}\}$ dan $R_f = \{y \mid y \ge 5, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat bentuk akar terdefinisi adalah $2x - 8 \ge 0 \Leftrightarrow x \ge 4$. Karena nilai $\sqrt{2x - 8} \ge 0$, maka $f(x) = \sqrt{2x - 8} + 5 \ge 5$, sehingga daerah hasilnya adalah $y \ge 5$.</sub>
- D. $D_f = \{x \mid x \ge 8, x \in \mathbb{R}\}$ dan $R_f = \{y \mid y \ge 5, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa lupa membagi 8 dengan koefisien 2 pada pertidaksamaan pembuat nol.</sub>

**Pembahasan:** Langkah 1: Tentukan syarat daerah asal (domain): bentuk di dalam akar harus tak-negatif:
$2x - 8 \ge 0 \Rightarrow 2x \ge 8 \Rightarrow x \ge 4$.
Jadi, $D_f = \{x \mid x \ge 4, x \in \mathbb{R}\}$.
Langkah 2: Tentukan daerah hasil (range): karena nilai $\sqrt{2x - 8} \ge 0$, maka nilai terkecil dari $\sqrt{2x - 8}$ adalah $0$.
$f(x) = \sqrt{2x - 8} + 5 \ge 0 + 5 = 5$.
Jadi, $R_f = \{y \mid y \ge 5, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas11-b01-a-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: pemodelan fungsi linear*

Sebuah mesin pencetak keripik memproses ubi jalar menjadi keripik dengan aturan fungsi linear $y = f(x) = 8x$, di mana $x$ menyatakan massa ubi masukan dalam kilogram dan $y$ menyatakan jumlah kemasan keripik yang dihasilkan. Mesin tersebut hanya dapat beroperasi dengan kapasitas bahan masukan $25 \le x \le 80$. Selisih antara jumlah kemasan keripik maksimum dan minimum yang dapat diproduksi oleh mesin tersebut adalah ....

- A. $200$ kemasan  
  <sub>Salah: Siswa hanya menghitung hasil keluaran minimum $f(25)$.</sub>
- B. $640$ kemasan  
  <sub>Salah: Siswa hanya menghitung hasil keluaran maksimum $f(80)$.</sub>
- C. $55$ kemasan  
  <sub>Salah: Siswa hanya mencari selisih masukan $80 - 25 = 55$ tanpa mengalikan rasio fungsi.</sub>
- **D. $440$ kemasan** ✅  
  <sub>Benar: Keluaran minimum: $f(25) = 8 \times 25 = 200$. Keluaran maksimum: $f(80) = 8 \times 80 = 640$. Selisihnya adalah $640 - 200 = 440$ kemasan.</sub>

**Pembahasan:** Langkah 1: Hitung produksi minimum saat bahan masukan $x = 25$ kg:
$y_{\text{min}} = 8 \times 25 = 200$ kemasan.
Langkah 2: Hitung produksi maksimum saat bahan masukan $x = 80$ kg:
$y_{\text{max}} = 8 \times 80 = 640$ kemasan.
Langkah 3: Hitung selisih produksi maksimum dan minimum:
$\Delta y = 640 - 200 = 440$ kemasan.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas11-b01-a-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: analisis domain dan range*

Hubungan antara suhu dalam skala Kelvin ($K$) dan suhu dalam skala Celsius ($C$) dinyatakan oleh fungsi $K(C) = C + 273,15$. Mengingat batas temperatur mutlak terendah di alam semesta bernilai $0\text{ K}$ (nol mutlak), maka daerah asal (*domain*) yang valid bagi nilai suhu $C$ agar suhu dalam Kelvin bernilai riil dan mungkin terjadi di alam semesta adalah ....

- **A. $\{C \mid C \ge -273,15, C \in \mathbb{R}\}$** ✅  
  <sub>Benar: Suhu terendah dalam Kelvin adalah $K \ge 0$. Karena $K = C + 273,15$, maka $C + 273,15 \ge 0 \Leftrightarrow C \ge -273,15$.</sub>
- B. $\{C \mid C \ge 273,15, C \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah mengoperasikan tanda saat memindahkan konstanta ke ruas lain.</sub>
- C. $\{C \mid C \ge 0, C \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengira batas bawah Celsius bernilai 0 sama seperti titik beku air.</sub>
- D. $\{C \mid C \le -273,15, C \in \mathbb{R}\}$  
  <sub>Salah: Siswa membalik tanda pertidaksamaan menjadi lebih kecil atau sama dengan.</sub>

**Pembahasan:** Langkah 1: Identifikasi batasan fisis suhu Kelvin di alam semesta, yaitu tidak ada suhu Kelvin yang negatif: $K \ge 0$.
Langkah 2: Substitusikan rumus relasi fungsi suhu Kelvin: $C + 273,15 \ge 0$.
Langkah 3: Selesaikan pertidaksamaan untuk daerah asal variabel $C$: $C \ge -273,15$.
Jadi, domainnya adalah $\{C \mid C \ge -273,15, C \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.32

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas11-b01-a-medium-bt01-005
*orisinal | C4 | 2 langkah | jenis: analisis tes garis vertikal*

Berdasarkan tes garis vertikal, suatu relasi pada bidang Kartesius merupakan fungsi jika setiap garis vertikal memotong grafiknya di paling banyak satu titik. Di antara persamaan relasi berikut, manakah yang merupakan suatu fungsi $y = f(x)$ untuk semua $x$ pada daerah definisinya?

- **A. $x^2 + y = 4$** ✅  
  <sub>Benar: Bentuk $x^2 + y = 4$ dapat dinyatakan sebagai $y = 4 - x^2$. Untuk setiap nilai masukan $x$, hanya menghasilkan tepat satu nilai keluaran $y$. Garis vertikal $x = c$ memotong grafik tepat di satu titik $(c, 4 - c^2)$.</sub>
- B. $|y| = x + 4$  
  <sub>Salah: Untuk nilai $x > -4$, terdapat dua nilai $y = \pm(x + 4)$ sehingga gagal dalam tes garis vertikal.</sub>
- C. $x^2 + y^2 = 4$  
  <sub>Salah: Grafik lingkaran ini dipotong oleh garis vertikal seperti $x = 0$ di dua titik, yaitu $(0, 2)$ dan $(0, -2)$.</sub>
- D. $x + y^2 = 4$  
  <sub>Salah: Untuk nilai $x < 4$, terdapat dua nilai $y = \pm \sqrt{4 - x}$ sehingga garis vertikal memotong grafik di dua titik.</sub>

**Pembahasan:** Langkah 1: Uji apakah tiap nilai $x$ menghasilkan tepat satu nilai $y$ (lolos tes garis vertikal):
- Pada $x + y^2 = 4 \Leftrightarrow y = \pm \sqrt{4 - x}$, untuk $x = 0$ terdapat dua nilai $y = 2$ dan $y = -2$ (bukan fungsi).
- Pada $x^2 + y^2 = 4$, grafik berbentuk lingkaran di mana garis $x = 0$ memotong di $(0, 2)$ dan $(0, -2)$ (bukan fungsi).
- Pada $|y| = x + 4$, untuk $x = 0$ terdapat $y = 4$ dan $y = -4$ (bukan fungsi).
Langkah 2: Pada persamaan $x^2 + y = 4$, diperoleh $y = 4 - x^2$. Untuk setiap nilai $x \in \mathbb{R}$, nilai $y$ tunggal sehingga setiap garis vertikal memotong grafik tepat pada satu titik. Oleh karena itu, relasi ini merupakan fungsi.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas11-b01-a-medium-bt01-006
*variasi (angka) | C3 | 3 langkah | jenis: penjualan eksponensial*

Berdasarkan data penjualan sebuah gerai gawai, pada tahun 2018 gerai tersebut menjual $8$ unit tablet. Pada tahun 2019 dan 2020 berturut-turut terjual $24$ dan $72$ unit tablet. Jika tren penjualan tahunan tersebut membentuk suatu model fungsi eksponensial, perkiraan penjualan tablet pada tahun 2024 adalah ....

- A. $17.496$ unit  
  <sub>Salah: Siswa kelebihan satu periode pemangkatan menjadi pangkat $7$ ($8 \cdot 3^7 = 17.496$).</sub>
- B. $1.944$ unit  
  <sub>Salah: Siswa salah menghitung selisih tahun menjadi $5$ tahun ($8 \cdot 3^5 = 1.944$).</sub>
- C. $2.187$ unit  
  <sub>Salah: Siswa hanya menghitung nilai perpangkatan $3^7$ tanpa mengalikan dengan nilai awal $8$.</sub>
- **D. $5.832$ unit** ✅  
  <sub>Benar: Rasio pertumbuhan penjualan per tahun adalah $r = \frac{24}{8} = 3$. Fungsi eksponensial penjualan dapat dimodelkan sebagai $f(t) = 8 \cdot 3^{t - 2018}$. Pada tahun 2024, nilai $t - 2018 = 6$, sehingga $f(2024) = 8 \cdot 3^6 = 8 \cdot 729 = 5.832$ unit.</sub>

**Pembahasan:** Penjualan tablet membentuk barisan geometri dengan suku awal $a = 8$ pada tahun $2018$.
Rasio pertumbuhan per tahun:
$$r = \frac{24}{8} = \frac{72}{24} = 3$$
Fungsi penjualan pada tahun ke-$t$ adalah:
$$f(t) = 8 \cdot 3^{t - 2018}$$
Untuk tahun 2024, selisih waktu adalah $t - 2018 = 2024 - 2018 = 6$.
$$f(2024) = 8 \cdot 3^6 = 8 \cdot 729 = 5.832$$
Jadi, penjualan tablet pada tahun 2024 adalah $5.832$ unit.
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas11-b01-a-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: daerah hasil fungsi kuadrat berbatas*

Diketahui fungsi kuadrat $f(x) = 2x^2 - 8$ terdefinisi pada daerah asal terbatas $D_f = \{x \mid -1 \le x \le 3, x \in \mathbb{R}\}$. Daerah hasil (*range*) dari fungsi $f$ adalah ....

- A. $\{y \mid -6 \le y \le 10, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa hanya menghitung nilai ujung interval $f(-1)$ dan $f(3)$ tanpa memperhitungkan nilai minimum di titik puncak $x = 0$.</sub>
- **B. $\{y \mid -8 \le y \le 10, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Parabola terbuka ke atas dengan titik puncak pada sumbu simetri $x_p = 0$. Karena $0 \in [-1, 3]$, nilai minimumnya adalah $f(0) = -8$. Nilai fungsi di ujung domain adalah $f(-1) = 2(-1)^2 - 8 = -6$ dan $f(3) = 2(3)^2 - 8 = 10$. Dengan demikian, nilai maksimumnya adalah $10$, sehingga daerah hasilnya adalah $[-8, 10]$.</sub>
- C. $\{y \mid -8 \le y \le 18, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan saat menentukan $f(3)$ dengan menghitung $2(3^2) = 18$ tanpa menguranginya dengan $8$.</sub>
- D. $\{y \mid y \ge -8, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengabaikan batas atas daerah asal sehingga menganggap daerah hasil tidak terbatas ke atas.</sub>

**Pembahasan:** Fungsi kuadrat $f(x) = 2x^2 - 8$ memiliki kurva parabola dengan $a = 2 > 0$ (terbuka ke atas).
1. Sumbu simetri berada pada $x_p = -\frac{b}{2a} = 0$.
Karena $x = 0$ berada di dalam interval $[-1, 3]$, nilai minimum kurva berada di titik puncak:
$$y_{\text{min}} = f(0) = 2(0)^2 - 8 = -8$$
2. Hitung nilai pada batas-batas interval domain:
$$f(-1) = 2(-1)^2 - 8 = 2 - 8 = -6$$
$$f(3) = 2(3)^2 - 8 = 18 - 8 = 10$$
Nilai terbesar di antara nilai-nilai tersebut adalah $y_{\text{maks}} = 10$.
3. Maka, daerah hasil (*range*) fungsi adalah $\{y \mid -8 \le y \le 10, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas11-b01-a-medium-bt01-008
*orisinal | C3 | 2 langkah | jenis: domain fungsi rasional irasional*

Diketahui fungsi $g(x) = \frac{5x - 2}{\sqrt{6 - 2x}}$ terdefinisi pada himpunan bilangan riil. Daerah asal (*domain*) alami dari fungsi $g(x)$ adalah ....

- A. $\{x \mid x \le 3, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa menyertakan tanda sama dengan sehingga membuat penyebut bernilai nol yang menyebabkan fungsi tidak terdefinisi.</sub>
- **B. $\{x \mid x < 3, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Penyebut pecahan tidak boleh sama dengan nol dan radikan di dalam akar harus bernilai tak negatif. Gabungan kedua syarat tersebut menghasilkan syarat tunggal $6 - 2x > 0 \implies 6 > 2x \implies x < 3$.</sub>
- C. $\{x \mid x > 3, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa lupa membalik arah pertidaksamaan saat membagi dengan koefisien negatif $-2$.</sub>
- D. $\{x \mid x \ge 3, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah membalik arah tanda pertidaksamaan sekaligus menyertakan titik batas pembuat nol pada penyebut.</sub>

**Pembahasan:** Agar fungsi aljabar $g(x) = \frac{5x - 2}{\sqrt{6 - 2x}}$ terdefinisi pada himpunan bilangan riil:
1. Syarat bentuk akar: $6 - 2x \ge 0$
2. Syarat pecahan: $\sqrt{6 - 2x} \ne 0$, sehingga $6 - 2x \ne 0$

Gabungan kedua syarat tersebut adalah radikan harus bernilai positif murni:
$$6 - 2x > 0$$
$$-2x > -6$$
Bagi kedua ruas dengan $-2$ (tanda pertidaksamaan berbalik):
$$x < 3$$

Jadi, daerah asal alaminya adalah $\{x \mid x < 3, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas11-b01-a-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: analisis persamaan fungsi aljabar*

Di antara persamaan-persamaan relasi berikut yang memetakan bilangan riil $x$ ke bilangan riil $y$, persamaan yang mendefinisikan $y$ sebagai fungsi dari $x$ adalah ....

- A. $|y| - 3x = 1$  
  <sub>Salah: Siswa mengabaikan bahwa bentuk nilai mutlak $|y| = 3x + 1$ menghasilkan dua nilai $y = \pm (3x + 1)$ untuk $x > -\frac{1}{3}$.</sub>
- B. $x + y^2 = 16$  
  <sub>Salah: Siswa terkecoh mengira derajat satu pada $x$ menjadikannya fungsi, padahal $y = \pm \sqrt{16 - x}$ menghasilkan dua nilai $y$ untuk satu nilai $x < 16$.</sub>
- **C. $x^2 - 2y = 8$** ✅  
  <sub>Benar: Persamaan $x^2 - 2y = 8$ dapat dinyatakan secara eksplisit menjadi $y = \frac{1}{2}x^2 - 4$. Untuk setiap nilai masukan $x \in \mathbb{R}$, nilai $y$ terdefinisi tunggal (tepat satu nilai keluaran).</sub>
- D. $x^2 - y^2 = 9$  
  <sub>Salah: Siswa mengabaikan bahwa untuk nilai $x > 3$, nilai $y = \pm \sqrt{x^2 - 9}$ menghasilkan dua nilai keluaran berbeda.</sub>

**Pembahasan:** Suatu relasi mendefinisikan $y$ sebagai fungsi dari $x$ apabila untuk setiap masukan $x$, terdapat tepat satu keluaran $y$.
- Opsi $x + y^2 = 16 \implies y = \pm \sqrt{16 - x}$. Untuk $x = 0$, didapat dua nilai $y = 4$ dan $y = -4$ (bukan fungsi).
- Opsi $x^2 - y^2 = 9 \implies y = \pm \sqrt{x^2 - 9}$. Untuk $x = 5$, didapat dua nilai $y = 4$ dan $y = -4$ (bukan fungsi).
- Opsi $|y| - 3x = 1 \implies |y| = 3x + 1$. Untuk $x = 1$, didapat dua nilai $y = 4$ dan $y = -4$ (bukan fungsi).
- Opsi $x^2 - 2y = 8 \implies 2y = x^2 - 8 \implies y = \frac{1}{2}x^2 - 4$. Karena setiap nilai $x$ menghasilkan tepat satu nilai $y$, relasi ini merupakan fungsi.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas11-b01-a-medium-bt01-010
*variasi (angka) | C3 | 2 langkah | jenis: daerah hasil fungsi irasional*

Diketahui fungsi irasional $f(x) = 6 - \sqrt{2x + 8}$ yang terdefinisi pada daerah asal alaminya. Daerah hasil (*range*) dari fungsi $f(x)$ adalah ....

- A. $\{y \mid y \ge -4, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa tertukar antara daerah hasil (*range*) dengan batas daerah asal (*domain*) alami fungsi yaitu $x \ge -4$.</sub>
- B. $\{y \mid y \le -4, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mencampurkan batas daerah asal $x \ge -4$ dengan pembalikan arah pertidaksamaan.</sub>
- C. $\{y \mid y \ge 6, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengabaikan tanda minus di depan bentuk akar sehingga menganggap nilainya selalu lebih besar atau sama dengan $6$.</sub>
- **D. $\{y \mid y \le 6, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Nilai bentuk akar $\sqrt{2x + 8} \ge 0$, sehingga nilai $6 - \sqrt{2x + 8} \le 6 - 0 = 6$.</sub>

**Pembahasan:** Fungsi terdefinisi jika nilai di dalam tanda akar tak negatif:
$$2x + 8 \ge 0 \iff 2x \ge -8 \iff x \ge -4$$
Untuk setiap $x \ge -4$, nilai dari akar kuadrat bernilai tak negatif:
$$\sqrt{2x + 8} \ge 0$$
Kalikan kedua ruas dengan $-1$ (tanda pertidaksamaan berbalik):
$$-\sqrt{2x + 8} \le 0$$
Tambahkan kedua ruas dengan $6$:
$$6 - \sqrt{2x + 8} \le 6$$
$$f(x) \le 6$$
Jadi, daerah hasil (*range*) fungsi tersebut adalah $R_f = \{y \mid y \le 6, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas11-b01-a-medium-bt01-011
*variasi (konteks) | C3 | 2 langkah | jenis: evaluasi relasi fungsi dan nilai fungsi*

Hubungan konversi satuan tekanan dari atmosfer ($\text{atm}$) ke kiloPascal ($\text{kPa}$) didefinisikan dengan kesetaraan $1\text{ atm} = 101,3\text{ kPa}$. Sebuah relasi dirumuskan dengan $q = 101,3p$, di mana $p$ menyatakan tekanan dalam satuan $\text{atm}$ dan $q$ menyatakan tekanan dalam satuan $\text{kPa}$. Nilai tekanan $q$ untuk $p = 4,5\text{ atm}$ serta kesimpulan sifat relasi tersebut adalah ....

- A. $455,85\text{ kPa}$ dan bukan fungsi karena menghubungkan dua satuan ukuran yang berbeda  
  <sub>Salah: Siswa menghitung nilai dengan benar tetapi salah memahami konsep relasi dan fungsi pada konversi satuan fisika.</sub>
- B. $45,585\text{ kPa}$ dan merupakan fungsi karena setiap nilai $p$ berpasangan dengan tepat satu nilai $q$  
  <sub>Salah: Siswa salah dalam meletakkan koma desimal pada hasil perkalian bilangan berkoma.</sub>
- C. $506,5\text{ kPa}$ dan merupakan fungsi karena setiap nilai $p$ berpasangan dengan tepat satu nilai $q$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan aritmetika dengan mengalikan $101,3$ dengan $5$ alih-alih $4,5$.</sub>
- **D. $455,85\text{ kPa}$ dan merupakan fungsi karena setiap nilai $p$ berpasangan dengan tepat satu nilai $q$** ✅  
  <sub>Benar: Perhitungan $101,3 \times 4,5 = 455,85\text{ kPa}$, dan relasi linear memasangkan setiap satu nilai masukan dengan tepat satu nilai keluaran sehingga memenuhi definisi fungsi.</sub>

**Pembahasan:** Langkah 1: Menghitung nilai tekanan $q$ saat $p = 4,5\text{ atm}$:
$$q = 101,3 \times 4,5 = 455,85\text{ kPa}$$
Langkah 2: Menganalisis sifat relasi:
Relasi $q = 101,3p$ menghubungkan setiap satu nilai tekanan dalam $\text{atm}$ ($p$) ke tepat satu nilai tekanan dalam $\text{kPa}$ ($q$). Tidak ada satu nilai $p$ yang menghasilkan lebih dari satu nilai $q$. Oleh karena itu, relasi ini merupakan fungsi.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas11-b01-a-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: uji tes garis vertikal persamaan lingkaran*

Sebuah relasi pada bidang Kartesius dinyatakan oleh persamaan $(x - 3)^2 + (y + 1)^2 = 25$. Jika dilakukan uji tes garis vertikal dengan menarik garis lurus $x = 3$, titik potong yang dihasilkan dan kesimpulan mengenai relasi tersebut adalah ....

- **A. memotong di $(3, 4)$ dan $(3, -6)$, sehingga relasi tersebut bukan merupakan fungsi** ✅  
  <sub>Benar: Substitusi $x = 3$ menghasilkan $(y + 1)^2 = 25$, sehingga $y + 1 = \pm 5$ yang memberi dua nilai $y = 4$ dan $y = -6$. Karena memotong di dua titik berbeda, relasi bukan fungsi.</sub>
- B. memotong di $(3, 5)$ dan $(3, -5)$, sehingga relasi tersebut bukan merupakan fungsi  
  <sub>Salah: Siswa lupa memperhitungkan translasi $y + 1$ dan langsung menganggap $y = \pm 5$.</sub>
- C. memotong di $(3, 4)$ dan $(3, -6)$, sehingga relasi tersebut merupakan fungsi karena memiliki nilai keluaran simetris  
  <sub>Salah: Siswa menemukan titik potong dengan benar namun salah memahami tes garis vertikal dengan menganggap keberadaan dua titik simetris memenuhi syarat fungsi.</sub>
- D. memotong hanya di $(3, 4)$, sehingga relasi tersebut merupakan fungsi  
  <sub>Salah: Siswa hanya mengambil akar kuadrat bernilai positif sehingga menarik kesimpulan yang keliru.</sub>

**Pembahasan:** Uji tes garis vertikal dilakukan dengan mensubstitusikan persamaan garis $x = 3$ ke dalam persamaan relasi:
$$(3 - 3)^2 + (y + 1)^2 = 25$$
$$0 + (y + 1)^2 = 25$$
$$y + 1 = \pm \sqrt{25}$$
$$y + 1 = 5 \implies y = 4$$
$$y + 1 = -5 \implies y = -6$$
Garis vertikal $x = 3$ memotong grafik relasi di dua titik berbeda, yaitu $(3, 4)$ dan $(3, -6)$.
Sesuai konsep tes garis vertikal, jika terdapat garis vertikal yang memotong grafik di dua atau lebih titik berbeda, maka relasi tersebut **bukan merupakan fungsi**.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas11-b01-a-medium-bt01-013
*orisinal | C3 | 2 langkah | jenis: domain fungsi pecahan bentuk akar*

Daerah asal alami (*domain*) dari fungsi $h(x) = \frac{\sqrt{3x + 12}}{x - 5}$ pada himpunan bilangan riil $\mathbb{R}$ adalah ....

- A. $\{x \mid x > -4 \text{ dan } x \ne 5, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa keliru mengira nilai di dalam akar tidak boleh bernilai nol padahal letaknya di pembilang.</sub>
- B. $\{x \mid x \ne 5, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa hanya memperhatikan syarat penyebut tidak sama dengan nol dan melupakan syarat terdefinisi bentuk akar pada pembilang.</sub>
- C. $\{x \mid x \ge 4 \text{ dan } x \ne 5, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah melakukan operasi tanda saat menyelesaikan pertidaksamaan $3x + 12 \ge 0$.</sub>
- **D. $\{x \mid x \ge -4 \text{ dan } x \ne 5, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Syarat pembilang akar adalah $3x + 12 \ge 0 \iff x \ge -4$, dan syarat penyebut adalah $x - 5 \ne 0 \iff x \ne 5$. Irisannya adalah $x \ge -4$ dan $x \ne 5$.</sub>

**Pembahasan:** Agar fungsi pecahan $h(x) = \frac{\sqrt{3x + 12}}{x - 5}$ terdefinisi pada bilangan riil, harus dipenuhi dua syarat:
1. Syarat bentuk akar pada pembilang:
$$3x + 12 \ge 0 \iff 3x \ge -12 \iff x \ge -4$$
2. Syarat penyebut tidak boleh sama dengan nol:
$$x - 5 \ne 0 \iff x \ne 5$$
Menggabungkan kedua syarat tersebut menghasilkan daerah asal:
$$D_h = \{x \mid x \ge -4 \text{ dan } x \ne 5, x \in \mathbb{R}\}$$
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas11-b01-a-medium-bt01-014
*variasi (konteks) | C3 | 2 langkah | jenis: konversi besaran fisika*

Daya mekanik sering dinyatakan dalam satuan daya kuda (*horsepower* atau $\text{HP}$) dan watt ($\text{W}$) dengan kesetaraan $1\text{ HP} = 746\text{ W}$. Apakah relasi yang memetakan daya dalam satuan $\text{HP}$ ke satuan watt merupakan suatu fungsi, dan berapakah daya keluaran dalam watt jika sebuah mesin motor menghasilkan daya sebesar $6\text{ HP}$?

- A. Bukan fungsi; daya keluarannya adalah $4.476\text{ W}$  
  <sub>Salah: Siswa salah memahami definisi fungsi dan mengira relasi konversi fisis bukan merupakan fungsi.</sub>
- **B. Ya, merupakan fungsi; daya keluarannya adalah $4.476\text{ W}$** ✅  
  <sub>Benar: Setiap nilai daya masukan dalam satuan HP berkorespondensi tepat ke satu nilai keluaran dalam watt sesuai relasi linear $W = 746 \times \text{HP}$, dan untuk masukan $6\text{ HP}$ keluarannya adalah $746 \times 6 = 4.476\text{ W}$.</sub>
- C. Ya, merupakan fungsi; daya keluarannya adalah $752\text{ W}$  
  <sub>Salah: Siswa salah operasi dengan menjumlahkan $746 + 6$ alih-alih mengalikannya.</sub>
- D. Ya, merupakan fungsi; daya keluarannya adalah $4.276\text{ W}$  
  <sub>Salah: Siswa salah melakukan operasi perkalian aritmetika $746 \times 6$.</sub>

**Pembahasan:** Relasi konversi daya dari $\text{HP}$ ke watt dirumuskan oleh fungsi $W(h) = 746h$, di mana $h$ adalah daya dalam $\text{HP}$. Karena setiap nilai masukan $h$ dipasangkan tepat ke satu nilai keluaran $W$, maka relasi ini merupakan suatu fungsi. Untuk mesin berdaya $h = 6\text{ HP}$, daya keluarannya adalah $W(6) = 746 \times 6 = 4.476\text{ W}$.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas11-b01-a-medium-bt01-015
*variasi (konteks) | C3 | 2 langkah | jenis: domain operasional mesin*

Sebuah mesin pemroses di pabrik sari buah hanya dapat mulai bekerja jika dimasukkan minimal $40\text{ kg}$ buah jeruk dan sistem pengaman akan secara otomatis menghentikan mesin jika muatan melebihi $160\text{ kg}$. Jika $x$ menyatakan massa buah jeruk (dalam $\text{kg}$) yang dimasukkan ke dalam mesin sebagai variabel masukan, notasi himpunan yang tepat untuk menyatakan daerah asal (*domain*) dari fungsi operasional mesin tersebut adalah ....

- **A. $\{x \mid 40 \le x \le 160, x \in \mathbb{R}\}$** ✅  
  <sub>Benar: Mesin beroperasi mulai batas minimum $40\text{ kg}$ inklusif hingga batas maksimum $160\text{ kg}$ inklusif, sehingga daerah asalnya adalah selang tertutup $[40, 160]$ pada bilangan riil.</sub>
- B. $\{x \mid x \ge 40, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengabaikan batas maksimum operasional mesin sebesar 160 kg.</sub>
- C. $\{x \mid 0 \le x \le 160, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah menentukan nilai batas bawah dengan menganggap masukan dapat dimulai dari 0 kg.</sub>
- D. $\{x \mid 40 < x < 160, x \in \mathbb{R}\}$  
  <sub>Salah: Siswa salah menggunakan tanda ketaksamaan murni sehingga tidak menyertakan batas operasional 40 dan 160.</sub>

**Pembahasan:** Daerah asal (*domain*) fungsi merupakan himpunan semua nilai masukan yang dapat diproses oleh fungsi. Karena mesin beroperasi dengan masukan minimal $40\text{ kg}$ dan berhenti jika melebihi $160\text{ kg}$, maka nilai masukan $x$ yang diperbolehkan memenuhi $40 \le x \le 160$. Dalam notasi pembentuk himpunan bilangan riil, domainnya ditulis $\{x \mid 40 \le x \le 160, x \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.28 Eksplorasi 1.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas11-b01-a-medium-bt01-016
*variasi (konteks) | C3 | 3 langkah | jenis: pemodelan dan nilai fungsi konversi suhu*

Hubungan antara suhu dalam derajat Fahrenheit ($F$) dan derajat Celsius ($C$) merupakan fungsi linear. Diketahui air membeku pada suhu $0^\circ\text{C}$ yang setara dengan $32^\circ\text{F}$ dan mendidih pada suhu $100^\circ\text{C}$ yang setara dengan $212^\circ\text{F}$. Rumus fungsi linear $F(C)$ dan nilai suhu dalam derajat Fahrenheit ketika termometer Celsius menunjukkan angka $35^\circ\text{C}$ berturut-turut adalah ....

- A. $F(C) = \frac{9}{5}C - 32$ dan $31^\circ\text{F}$  
  <sub>Salah: Siswa salah tanda pada konstanta titik beku dengan menulis $-32$.</sub>
- B. $F(C) = \frac{9}{5}C + 32$ dan $67^\circ\text{F}$  
  <sub>Salah: Siswa salah substitusi dengan menjumlahkan nilai $C$ secara langsung ke 32 tanpa mengalikan $\frac{9}{5}$ terlebih dahulu.</sub>
- **C. $F(C) = \frac{9}{5}C + 32$ dan $95^\circ\text{F}$** ✅  
  <sub>Benar: Gradien fungsi adalah $\frac{212 - 32}{100 - 0} = \frac{180}{100} = \frac{9}{5}$ dengan titik potong sumbu $F$ di $32$, sehingga $F(C) = \frac{9}{5}C + 32$. Nilai untuk $C = 35$ adalah $\frac{9}{5}(35) + 32 = 63 + 32 = 95^\circ\text{F}$.</sub>
- D. $F(C) = \frac{5}{9}C + 32$ dan $51,4^\circ\text{F}$  
  <sub>Salah: Siswa terbalik menentukan gradien fungsi sebagai perbandingan $\frac{5}{9}$ alih-alih $\frac{9}{5}$.</sub>

**Pembahasan:** Fungsi linear berpasangan melalui titik $(0, 32)$ dan $(100, 212)$. Kemiringan fungsi:
$$m = \frac{212 - 32}{100 - 0} = \frac{180}{100} = \frac{9}{5}$$
Karena untuk $C = 0$ nilai $F = 32$, maka persamaan fungsinya adalah $F(C) = \frac{9}{5}C + 32$. Untuk $C = 35^\circ\text{C}$:
$$F(35) = \frac{9}{5}(35) + 32 = 63 + 32 = 95^\circ\text{F}$$
**Acuan:** siswa — siswa hal.32 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas11-b01-a-medium-bt01-017
*orisinal | C3 | 2 langkah | jenis: parameter relasi fungsi berurutan*

Diketahui suatu relasi dinyatakan dalam himpunan pasangan berurutan $R = \{(3, 7), (p^2 - p, 4), (5, 11), (3, 3p - 2)\}$. Agar relasi $R$ tersebut merupakan suatu fungsi, maka nilai bilangan bulat positif $p$ yang memenuhi adalah ....

- **A. $3$** ✅  
  <sub>Benar: Agar relasi merupakan fungsi, anggota masukan $x = 3$ harus memetakan ke keluaran yang tunggal, sehingga $3p - 2 = 7 \implies 3p = 9 \implies p = 3$. Untuk $p = 3$, masukan kedua bernilai $p^2 - p = 6$ yang tidak menimbulkan kontradiksi pemetaan.</sub>
- B. $2$  
  <sub>Salah: Siswa salah menyelesaikan persamaan $3p - 2 = 7$ atau salah menguji nilai $p$.</sub>
- C. $1$  
  <sub>Salah: Siswa keliru menyamakan $p^2 - p = 0$ lalu mengambil salah satu pembuat nolnya.</sub>
- D. $4$  
  <sub>Salah: Siswa keliru menjumlahkan konstanta dan koefisien secara tidak tepat.</sub>

**Pembahasan:** Definisi fungsi mengharuskan setiap anggota masukan terhubung tepat ke satu anggota keluaran. Pada pasangan berurutan terdapat dua titik dengan masukan yang sama, yaitu $(3, 7)$ dan $(3, 3p - 2)$. Agar relasi ini tetap merupakan fungsi, kedua keluaran harus bernilai sama:
$$3p - 2 = 7 \implies 3p = 9 \implies p = 3$$
Jika $p = 3$, maka komponen pertama titik kedua adalah $p^2 - p = 3^2 - 3 = 6$, sehingga pasangan berurutannya menjadi $\{(3, 7), (6, 4), (5, 11)\}$. Setiap nilai masukan $3, 6, 5$ berpasangan tepat satu nilai keluaran, sehingga syarat fungsi terpenuhi dengan $p = 3$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas11-b01-a-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: daerah hasil fungsi pecahan linear*

Diketahui fungsi pecahan linear $f(x) = \frac{6x - 5}{2x + 4}$ dengan daerah asal alami $D_f = \{x \in \mathbb{R} \mid x \ne -2\}$. Daerah hasil (*range*) dari fungsi $f(x)$ pada himpunan bilangan riil adalah ....

- A. $\{y \in \mathbb{R} \mid y \ne -\frac{5}{4}\}$  
  <sub>Salah: Siswa mengambil perbandingan suku konstanta $-\frac{5}{4}$ sebagai nilai asimtot/pantangan.</sub>
- **B. $\{y \in \mathbb{R} \mid y \ne 3\}$** ✅  
  <sub>Benar: Dengan mengubah persamaan menjadi bentuk $x = g(y)$, diperoleh $x = \frac{-4y - 5}{2y - 6}$. Agar nilai $x$ terdefinisi pada bilangan riil, penyebut tidak boleh nol, yaitu $2y - 6 \ne 0 \iff y \ne 3$.</sub>
- C. $\{y \in \mathbb{R} \mid y \ne -2\}$  
  <sub>Salah: Siswa keliru menyamakan daerah hasil dengan batasan daerah asal ($x \ne -2$).</sub>
- D. $\{y \in \mathbb{R} \mid y \ne 6\}$  
  <sub>Salah: Siswa hanya memperhatikan koefisien pembilang tanpa membaginya dengan koefisien penyebut.</sub>

**Pembahasan:** Misalkan $y = f(x)$, maka:
$$y = \frac{6x - 5}{2x + 4}$$
$$y(2x + 4) = 6x - 5$$
$$2xy + 4y = 6x - 5$$
$$2xy - 6x = -4y - 5$$
$$x(2y - 6) = -4y - 5$$
$$x = \frac{-4y - 5}{2y - 6}$$
Agar nilai masukan $x$ riil terdefinisi, nilai penyebut tidak boleh sama dengan nol:
$$2y - 6 \ne 0 \implies 2y \ne 6 \implies y \ne 3$$
Jadi daerah hasil (*range*) dari fungsi tersebut adalah $R_f = \{y \in \mathbb{R} \mid y \ne 3\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas11-b01-a-medium-bt01-019
*variasi (angka) | C3 | 3 langkah | jenis: daerah hasil fungsi kuadrat*

Diketahui fungsi kuadrat $f(x) = x^2 - 6x + 14$ terdefinisi pada himpunan bilangan riil $\mathbb{R}$. Daerah hasil (*range*) dari fungsi $f(x)$ adalah ....

- A. $\{y \mid y \ge -5, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa melakukan kesalahan tanda saat menghitung nilai minimum: $9 - 18 - 14$ atau salah tanda pada absis titik puncak.</sub>
- B. $\{y \mid y \ge 14, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa mengira nilai konstanta $c = 14$ sebagai nilai minimum fungsi kuadrat tanpa mencari titik balik.</sub>
- **C. $\{y \mid y \ge 5, y \in \mathbb{R}\}$** ✅  
  <sub>Benar: Parabola $f(x) = x^2 - 6x + 14$ terbuka ke atas ($a = 1 > 0$), sehingga memiliki nilai minimum pada absis titik puncak $x_p = -\frac{b}{2a} = -\frac{-6}{2(1)} = 3$. Nilai minimum fungsinya adalah $y_{\min} = f(3) = 3^2 - 6(3) + 14 = 9 - 18 + 14 = 5$. Jadi, daerah hasilnya adalah $\{y \mid y \ge 5, y \in \mathbb{R}\}$.</sub>
- D. $\{y \mid y \le 5, y \in \mathbb{R}\}$  
  <sub>Salah: Siswa keliru menentukan arah pertidaksamaan karena mengira kurva memiliki nilai maksimum.</sub>

**Pembahasan:** Untuk menentukan daerah hasil (*range*) dari fungsi kuadrat $f(x) = ax^2 + bx + c$ dengan domain $\mathbb{R}$:
1. Perhatikan nilai koefisien $a = 1$. Karena $a > 0$, parabola terbuka ke atas sehingga fungsi memiliki nilai minimum.
2. Tentukan koordinat titik puncak pada sumbu simetri:
$$x_p = -\frac{b}{2a} = -\frac{-6}{2(1)} = 3$$
3. Hitung nilai minimum dengan mensubstitusikan $x_p$ ke $f(x)$:
$$f(3) = (3)^2 - 6(3) + 14 = 9 - 18 + 14 = 5$$
Dengan demikian, nilai keluaran $y$ selalu lebih besar atau sama dengan $5$. Jadi, daerah hasilnya adalah $R_f = \{y \mid y \ge 5, y \in \mathbb{R}\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas11-b01-a-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: domain fungsi rasional kuadrat*

Daerah asal alami (*domain*) dari fungsi rasional $f(x) = \frac{2x + 7}{x^2 - 4x - 12}$ pada himpunan bilangan riil $\mathbb{R}$ adalah ....

- A. $\{x \in \mathbb{R} \mid -2 < x < 6\}$  
  <sub>Salah: Siswa keliru menganggap syarat pecahan sama dengan pertidaksamaan bentuk akar dan mengambil interval tertutup di antaranya.</sub>
- B. $\{x \in \mathbb{R} \mid x \ne -\frac{7}{2}\}$  
  <sub>Salah: Siswa menyamakan pembilang dengan nol alih-alih memeriksa syarat penyebut tidak boleh nol.</sub>
- **C. $\{x \in \mathbb{R} \mid x \ne -2 \text{ dan } x \ne 6\}$** ✅  
  <sub>Benar: Fungsi rasional terdefinisi pada bilangan riil jika penyebutnya tidak bernilai nol: $x^2 - 4x - 12 \ne 0 \iff (x - 6)(x + 2) \ne 0$. Diperoleh syarat $x \ne 6$ dan $x \ne -2$.</sub>
- D. $\{x \in \mathbb{R} \mid x \ne -6 \text{ dan } x \ne 2\}$  
  <sub>Salah: Siswa salah menentukan tanda saat memfaktorkan persamaan kuadrat penyebut.</sub>

**Pembahasan:** Agar fungsi rasional $f(x) = \frac{2x + 7}{x^2 - 4x - 12}$ terdefinisi pada himpunan bilangan riil, penyebut tidak boleh sama dengan nol:
$$x^2 - 4x - 12 \ne 0$$
Faktorkan bentuk kuadrat pada penyebut:
$$(x - 6)(x + 2) \ne 0$$
Pembuat nol penyebut adalah $x = 6$ atau $x = -2$. Dengan demikian, nilai $x$ yang memenuhi syarat domain alami adalah seluruh bilangan riil kecuali $x = -2$ dan $x = 6$.
Jadi, daerah asal alaminya adalah $D_f = \{x \in \mathbb{R} \mid x \ne -2 \text{ dan } x \ne 6\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas11-b01-a-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: analisis parameter fungsi bentuk akar*

Diketahui suatu fungsi bentuk akar didefinisikan sebagai $f(x) = \sqrt{px - 28} + q$ dengan domain $D_f = \{x \in \mathbb{R} \mid x \ge 7\}$ dan daerah hasil (*range*) $R_f = \{y \in \mathbb{R} \mid y \ge -5\}$. Berdasarkan karakteristik fungsi tersebut, nilai dari ekspresi $2p - 3q$ adalah ....

- **A. $23$** ✅  
  <sub>Benar: Syarat domain $px - 28 \ge 0 \iff x \ge \frac{28}{p}$. Karena domain $x \ge 7$, maka $\frac{28}{p} = 7 \implies p = 4$. Nilai minimum akar kuadrat utama adalah $0$, sehingga nilai minimum dari $f(x)$ adalah $0 + q = q$. Karena range $y \ge -5$, maka $q = -5$. Nilai ekspresi $2p - 3q = 2(4) - 3(-5) = 8 + 15 = 23$.</sub>
- B. -7  
  <sub>Salah: Siswa keliru menghitung tanda pada operasi pengurangan bilangan negatif: $8 - 15 = -7$.</sub>
- C. -23  
  <sub>Salah: Siswa tertukar tanda saat mengidentifikasi nilai $q = 5$ sehingga memperoleh $8 - 3(5) = -7$ atau salah tanda total.</sub>
- D. 17  
  <sub>Salah: Siswa salah menentukan nilai $p = 1$ dari pembagian $28 - 7$ atau salah hitung parameter.</sub>

**Pembahasan:** Berdasarkan definisi fungsi bentuk akar $f(x) = \sqrt{px - 28} + q$:
1. Agar terdefinisi pada bilangan riil, nilai di dalam akar harus tak negatif: $px - 28 \ge 0 \iff px \ge 28 \iff x \ge \frac{28}{p}$ (dengan $p > 0$).
2. Diketahui batas domain adalah $x \ge 7$, sehingga $\frac{28}{p} = 7 \iff p = 4$.
3. Karena nilai $\sqrt{4x - 28} \ge 0$, nilai keluaran fungsi adalah $f(x) \ge q$.
4. Diketahui batas range adalah $y \ge -5$, sehingga $q = -5$.
5. Nilai $2p - 3q = 2(4) - 3(-5) = 8 + 15 = 23$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas11-b01-a-hard-bt01-002
*orisinal | C5 | 5 langkah | jenis: analisis domain alami fungsi kombinasi*

Sebuah fungsi terdefinisi melalui bentuk aljabar $f(x) = \frac{\sqrt{15 - 3x}}{\sqrt{x^2 - 4}}$. Agar fungsi $f(x)$ terdefinisi dan menghasilkan nilai pada himpunan bilangan riil $\mathbb{R}$, maka daerah asal alami (*domain*) dari fungsi tersebut adalah ....

- A. $\{x \in \mathbb{R} \mid 2 < x \le 5\}$  
  <sub>Salah: Siswa melupakan domain untuk interval bilangan negatif $x < -2$ yang juga memenuhi syarat $x^2 - 4 > 0$ dan $x \le 5$.</sub>
- B. $\{x \in \mathbb{R} \mid x \le -2 \text{ atau } 2 \le x \le 5\}$  
  <sub>Salah: Siswa lupa bahwa penyebut tidak boleh sama dengan nol, sehingga memasukkan tanda sama dengan pada nilai $x = -2$ dan $x = 2$.</sub>
- **C. $\{x \in \mathbb{R} \mid x < -2 \text{ atau } 2 < x \le 5\}$** ✅  
  <sub>Benar: Syarat pembilang: $15 - 3x \ge 0 \iff 3x \le 15 \iff x \le 5$. Syarat penyebut: karena berada di bawah akar dan sebagai pembagi, maka $x^2 - 4 > 0 \iff (x - 2)(x + 2) > 0 \iff x < -2$ atau $x > 2$. Irisan dari kedua syarat tersebut: $(x \le 5) \cap (x < -2 \text{ atau } x > 2)$, yang menghasilkan $x < -2$ atau $2 < x \le 5$.</sub>
- D. $\{x \in \mathbb{R} \mid -2 < x < 2 \text{ atau } x \ge 5\}$  
  <sub>Salah: Siswa salah menentukan tanda interval penyelesaian pertidaksamaan kuadrat $x^2 - 4 > 0$ menjadi di antara akar-akarnya.</sub>

**Pembahasan:** Untuk menentukan daerah asal alami (*domain*) fungsi aljabar $f(x) = \frac{\sqrt{15 - 3x}}{\sqrt{x^2 - 4}}$:
1. Syarat numerus akar pada pembilang: $15 - 3x \ge 0 \implies -3x \ge -15 \implies x \le 5$.
2. Syarat numerus akar pada penyebut: bernilai positif murni (karena penyebut pecahan tidak boleh nol): $x^2 - 4 > 0 \implies (x - 2)(x + 2) > 0 \implies x < -2$ atau $x > 2$.
3. Mengambil irisan dari kedua syarat:
- Untuk $x < -2$: seluruh nilai ini memenuhi $x \le 5$, sehingga daerah ini memenuhi.
- Untuk $x > 2$: dipadukan dengan $x \le 5$, didapat $2 < x \le 5$.
Jadi, domain fungsi adalah $\{x \in \mathbb{R} \mid x < -2 \text{ atau } 2 < x \le 5\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas11-b01-a-hard-bt01-003
*orisinal | C6 | 5 langkah | jenis: desain dan pembatasan daerah hasil fungsi rasional*

Diketahui suatu fungsi rasional $f(x) = \frac{4x - 9}{2x + 6}$ dengan daerah asal alaminya $D_f$. Jika daerah hasil fungsi tersebut dinyatakan dalam bentuk himpunan $R_f = \{y \in \mathbb{R} \mid y \ne k\}$, maka nilai $k$ yang tidak mungkin pernah dicapai oleh fungsi tersebut adalah ....

- A. -1,5  
  <sub>Salah: Siswa membagi konstanta pembilang dengan penyebut secara keliru: $-9 / 6 = -1,5$.</sub>
- B. 4  
  <sub>Salah: Siswa hanya mengambil koefisien $x$ pada pembilang tanpa membaginya dengan koefisien $x$ pada penyebut.</sub>
- C. -3  
  <sub>Salah: Siswa tertukar antara pembuat nol penyebut fungsi asal (nilai yang dikeluarkan dari domain: $2x + 6 = 0 \implies x = -3$) dengan nilai yang dikeluarkan dari range.</sub>
- **D. $2$** ✅  
  <sub>Benar: Misalkan $y = \frac{4x - 9}{2x + 6}$. Maka $y(2x + 6) = 4x - 9 \iff 2xy + 6y = 4x - 9 \iff x(2y - 4) = -6y - 9 \iff x = \frac{-6y - 9}{2y - 4}$. Agar nilai $x$ riil dapat ditemukan untuk suatu masukan $y$, penyebut tidak boleh nol, yaitu $2y - 4 \ne 0 \iff 2y \ne 4 \iff y \ne 2$. Jadi nilai yang dikecualikan dari range adalah $k = 2$.</sub>

**Pembahasan:** Untuk mencari daerah hasil (*range*) fungsi rasional $y = \frac{4x - 9}{2x + 6}$:
1. Nyatakan $x$ dalam variabel $y$:
   $$y(2x + 6) = 4x - 9$$
   $$2xy + 6y = 4x - 9$$
   $$2xy - 4x = -6y - 9$$
   $$x(2y - 4) = -(6y + 9)$$
   $$x = \frac{-(6y + 9)}{2y - 4}$$
2. Nilai $x$ terdefinisi pada bilangan riil jika dan hanya jika penyebut pecahan tidak sama dengan nol:
   $$2y - 4 \ne 0 \implies 2y \ne 4 \implies y \ne 2$$
3. Dengan demikian, himpunan daerah hasil (*range*) adalah $R_f = \{y \in \mathbb{R} \mid y \ne 2\}$. Nilai $k$ adalah $2$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas11-b01-a-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi relasi konversi satuan*

Satuan daya dalam teknik mesin dinyatakan dalam daya kuda metrik (PS) dan kilowatt (kW) dengan kesetaraan $1\text{ PS} = 0,735\text{ kW}$. Sebuah laboratorium memodelkan rugi-rugi disipasi daya $P_d$ (dalam $\text{kW}$) sebagai fungsi terhadap daya mesin $x$ (dalam $\text{PS}$) melalui relasi $P_d^2 - 0,735 x P_d = 0$. Agar relasi tersebut mendefinisikan disipasi daya positif $P_d$ sebagai fungsi tunggal dari $x$ untuk $x > 0$, evaluasi bentuk rumus fungsi $P_d(x)$ yang valid beserta alasannya.

- **A. $P_d(x) = 0,735x$, karena setiap nilai masukan $x > 0$ menghasilkan tepat satu keluaran positif bernilai nyata** ✅  
  <sub>Benar: Persamaan $P_d^2 - 0,735xP_d = 0$ menghasilkan dua cabang yaitu $P_d = 0$ atau $P_d = 0,735x$. Karena disyaratkan disipasi daya bernilai positif ($P_d > 0$) untuk masukan $x > 0$, cabang $P_d = 0$ gugur, menyisakan relasi tunggal $P_d(x) = 0,735x$ yang memenuhi definisi fungsi.</sub>
- B. $P_d(x) = \frac{x}{0,735}$, karena satuan PS dikonversi terbalik terhadap kilowatt  
  <sub>Salah: Siswa salah melakukan operasi pembagian konversi alih-alih memanfaatkan relasi faktorisasi yang diberikan.</sub>
- C. Relasi tidak dapat dijadikan fungsi karena persamaan berderajat dua selalu menghasilkan dua nilai keluaran berbeda  
  <sub>Salah: Siswa gagal melihat bahwa pembatasan domain/kondisi fisis $P_d > 0$ mereduksi relasi menjadi fungsi tunggal.</sub>
- D. $P_d(x) = \pm 0,735x$, karena persamaan kuadrat memiliki dua akar penyelesaian untuk setiap nilai $x$  
  <sub>Salah: Siswa mempertahankan tanda plus-minus tanpa mengeliminasi nilai non-positif sehingga melanggar syarat tunggal keluaran fungsi.</sub>

**Pembahasan:** Persamaan $P_d^2 - 0,735x P_d = 0$ difaktorkan menjadi $P_d(P_d - 0,735x) = 0$.
Akar-akarnya adalah $P_d = 0$ atau $P_d = 0,735x$.
Karena disyaratkan $P_d > 0$ untuk setiap nilai masukan $x > 0$, maka akar $P_d = 0$ tidak memenuhi syarat fisis yang ditentukan.
Dengan demikian, tersisa $P_d = 0,735x$. Setiap masukan $x > 0$ memetakan tepat ke satu nilai keluaran positif, sehingga $P_d(x) = 0,735x$ merupakan fungsi.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas11-b01-a-hard-bt01-005
*orisinal | C5 | 5 langkah | jenis: analisis domain alami fungsi irasional bersyarat*

Daerah asal alami (*domain*) dari fungsi $f(x) = \sqrt{\frac{2x - 6}{8 - x}} + \frac{1}{\sqrt{x^2 - 16}}$ pada himpunan bilangan riil $\mathbb{R}$ adalah ....

- A. $\{x \in \mathbb{R} \mid 3 \le x < 4 \text{ atau } 4 < x < 8\}$  
  <sub>Salah: Siswa salah menentukan himpunan penyelesaian untuk $x^2 - 16 > 0$ dengan menganggap nilai di antara $-4$ dan $4$ memenuhi.</sub>
- **B. $\{x \in \mathbb{R} \mid 4 < x < 8\}$** ✅  
  <sub>Benar: Syarat suku pertama: $\frac{2x - 6}{8 - x} \ge 0 \iff 3 \le x < 8$. Syarat suku kedua: $x^2 - 16 > 0 \iff x < -4$ atau $x > 4$. Irisan keduanya menghasilkan interval terbuka $4 < x < 8$.</sub>
- C. $\{x \in \mathbb{R} \mid 4 \le x < 8\}$  
  <sub>Salah: Siswa memasukkan $x = 4$ padahal penyebut tidak boleh bernilai nol ($x^2 - 16 > 0$, bukan $\ge 0$).</sub>
- D. $\{x \in \mathbb{R} \mid 3 \le x \le 8\}$  
  <sub>Salah: Siswa hanya menyelesaikan syarat tanda akar pertama dan mengabaikan batas penyebut pada suku kedua.</sub>

**Pembahasan:** Agar fungsi $f(x)$ terdefinisi pada bilangan riil, kedua suku harus terdefinisi sekaligus:

1. Suku pertama: $\sqrt{\frac{2x - 6}{8 - x}}$
Syarat di bawah akar: $\frac{2(x - 3)}{8 - x} \ge 0$ dengan penyebut $8 - x \ne 0$.
Uji garis bilangan dengan pembuat nol $x = 3$ dan $x = 8$:
Diperoleh interval: $3 \le x < 8$.

2. Suku kedua: $\frac{1}{\sqrt{x^2 - 16}}$
Karena berada di penyebut dalam akar, maka radikan harus bernilai positif murni:
$x^2 - 16 > 0 \iff (x - 4)(x + 4) > 0$
Diperoleh interval: $x < -4$ atau $x > 4$.

3. Menentukan irisan dari kedua syarat:
$[3, 8) \cap ((-\infty, -4) \cup (4, \infty)) = (4, 8)$

Jadi, daerah asal alaminya adalah $\{x \in \mathbb{R} \mid 4 < x < 8\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas11-b01-a-hard-bt01-006
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi model eksponensial*

Berdasarkan catatan laboratorium biologi, suatu koloni kultur mikroba pada jam ke-$1$ berjumlah $12$ ribu sel. Pada jam ke-$2$ dan jam ke-$3$, populasi koloni tersebut berkembang berturut-turut menjadi $36$ ribu dan $108$ ribu sel. Jika pertumbuhan populasi mikroba tersebut konsisten mengikuti model fungsi eksponensial $P(t) = a \cdot b^{t-1}$ dengan $t$ menyatakan waktu dalam jam dan $P(t)$ menyatakan jumlah sel dalam ribuan, populasi mikroba tersebut pada jam ke-$6$ adalah ....

- **A. $2.916$ ribu sel** ✅  
  <sub>Benar: Rasio pertumbuhan $b = \frac{36}{12} = 3$ dan nilai awal $a = 12$. Pada jam ke-$6$, $P(6) = 12 \cdot 3^{6-1} = 12 \cdot 3^5 = 12 \cdot 243 = 2.916$ ribu sel.</sub>
- B. $972$ ribu sel  
  <sub>Salah: Siswa salah menghitung pangkat dengan mengurangkan eksponen satu tingkat terlalu rendah, yaitu $12 \cdot 3^4 = 972$.</sub>
- C. $1.458$ ribu sel  
  <sub>Salah: Siswa salah mengasumsikan suku pertama $a = 6$ bukannya $12$, sehingga $6 \cdot 3^5 = 1.458$.</sub>
- D. $8.748$ ribu sel  
  <sub>Salah: Siswa salah menggunakan eksponen $t$ langsung tanpa pergeseran awal, yaitu menghitung $12 \cdot 3^6 = 12 \cdot 729 = 8.748$.</sub>

**Pembahasan:** Model fungsi eksponensial pertumbuhan populasi mikroba berbentuk $P(t) = a \cdot b^{t-1}$.
1. Dari data awal jam ke-1 ($t = 1$): $P(1) = a = 12$.
2. Dari data jam ke-2 ($t = 2$): $P(2) = 12 \cdot b^{2-1} = 36 \implies b = 3$.
3. Cek data jam ke-3 ($t = 3$): $P(3) = 12 \cdot 3^2 = 12 \cdot 9 = 108$ (konsisten).
4. Hitung populasi pada jam ke-6 ($t = 6$):
$P(6) = 12 \cdot 3^{6-1} = 12 \cdot 3^5 = 12 \cdot 243 = 2.916$ ribu sel.
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas11-b01-a-hard-bt01-007
*variasi (angka) | C5 | 5 langkah | jenis: analisis range kuadratik domain terbatas*

Diketahui fungsi kuadrat $f(x) = 2x^2 - 12x + 11$ dibatasi pada domain tertutup $D_f = \{x \in \mathbb{R} \mid 1 \le x \le 5\}$. Daerah hasil (*range*) dari fungsi $f(x)$ pada domain tersebut adalah ....

- A. $\{y \in \mathbb{R} \mid -1 \le y \le 1\}$  
  <sub>Salah: Siswa melakukan kesalahan perhitungan saat menentukan koordinat puncak parabola.</sub>
- **B. $\{y \in \mathbb{R} \mid -7 \le y \le 1\}$** ✅  
  <sub>Benar: Titik puncak berada pada $x_p = -\frac{-12}{2(2)} = 3 \in [1, 5]$. Nilai minimum $f(3) = 2(9) - 12(3) + 11 = -7$. Uji batas domain: $f(1) = 2(1) - 12(1) + 11 = 1$ dan $f(5) = 2(25) - 12(5) + 11 = 1$. Maka daerah hasil $[-7, 1]$.</sub>
- C. $\{y \in \mathbb{R} \mid -7 \le y \le 11\}$  
  <sub>Salah: Siswa memasukkan nilai titik balik minimum $-7$, namun untuk batas atas mengambil nilai potong sumbu $y$ saat $x=0$ ($f(0)=11$) yang sebenarnya di luar domain tertutup.</sub>
- D. $\{y \in \mathbb{R} \mid 1 \le y \le 11\}$  
  <sub>Salah: Siswa hanya mengevaluasi ujung-ujung interval $x=1$ dan mengira nilai konstanta $c=11$ sebagai nilai maksimum tanpa memeriksa titik balik.</sub>

**Pembahasan:** Langkah pengerjaan:
1. Tentukan sumbu simetri fungsi kuadrat $f(x) = 2x^2 - 12x + 11$:
$x_p = -\frac{b}{2a} = -\frac{-12}{2 \cdot 2} = 3$.
2. Cek apakah sumbu simetri berada dalam domain $D_f = [1, 5]$. Karena $3 \in [1, 5]$, titik balik adalah nilai ekstrem (minimum karena $a = 2 > 0$).
3. Hitung nilai minimum di puncak:
$y_{\min} = f(3) = 2(3)^2 - 12(3) + 11 = 18 - 36 + 11 = -7$.
4. Hitung nilai fungsi pada kedua ujung interval domain:
$f(1) = 2(1)^2 - 12(1) + 11 = 1$
$f(5) = 2(5)^2 - 12(5) + 11 = 50 - 60 + 11 = 1$
5. Jadi, nilai minimum adalah $-7$ dan nilai maksimum adalah $1$. Daerah hasil (*range*) adalah $\{y \in \mathbb{R} \mid -7 \le y \le 1\}$.
**Acuan:** siswa — siswa hal.31 Latihan 1.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas11-b01-a-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: evaluasi tes garis vertikal berparameter*

Sebuah kurva relasi pada bidang Kartesius dinyatakan oleh persamaan $x = -y^2 + 6y - 5$. Berdasarkan tes garis vertikal, relasi ini bukan merupakan fungsi dari $x$ ke $y$. Agar relasi tersebut dapat dijadikan suatu fungsi $y = f(x)$, daerah nilai ($y$) harus dibatasi. Batasan himpunan $y$ berikut yang tepat untuk mengubah relasi tersebut menjadi suatu fungsi adalah ....

- A. $\{y \in \mathbb{R} \mid y \ge 4\}$  
  <sub>Salah: Siswa salah menggunakan nilai puncak absis $x_p = 4$ sebagai batas variabel $y$.</sub>
- **B. $\{y \in \mathbb{R} \mid y \ge 3\}$** ✅  
  <sub>Benar: Parabola horizontal terbuka ke kiri dengan puncak pada ordinat $y_p = -\frac{6}{2(-1)} = 3$. Garis vertikal akan memotong kurva tepat satu kali jika cabang parabola dipisah pada $y \ge 3$ atau $y \le 3$.</sub>
- C. $\{y \in \mathbb{R} \mid y \le 6\}$  
  <sub>Salah: Siswa salah mengira koefisien linear variabel $y$ yaitu $6$ sebagai batas pembagi cabang parabola.</sub>
- D. $\{y \in \mathbb{R} \mid 1 \le y \le 5\}$  
  <sub>Salah: Siswa memilih interval di antara titik potong sumbu $y$ saat $x=0$, di mana garis vertikal justru masih memotong kurva di dua titik.</sub>

**Pembahasan:** Langkah pengerjaan:
1. Persamaan $x = -y^2 + 6y - 5$ menyatakan parabola horizontal yang terbuka ke kiri.
2. Tentukan koordinat ordinat titik puncak parabola horizontal:
$y_p = -\frac{b}{2a} = -\frac{6}{2(-1)} = 3$.
3. Untuk setiap nilai $x < 4$, terdapat dua nilai $y$ simetris terhadap garis horizontal $y = 3$, sehingga tes garis vertikal $x = c$ akan memotong kurva di dua titik berbeda.
4. Agar kurva lolos tes garis vertikal (setiap $x$ berpasangan tepat dengan satu $y$), relasi harus dibatasi hanya pada salah satu cabang di atas atau di bawah puncaknya, yaitu $y \ge 3$ atau $y \le 3$.
5. Di antara pilihan yang diberikan, batasan yang tepat adalah $\{y \in \mathbb{R} \mid y \ge 3\}$.
**Acuan:** siswa — siswa hal.23

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas11-b01-a-hard-bt01-009
*orisinal | C6 | 6 langkah | jenis: desain dan evaluasi rentang fungsi rasional*

Diketahui fungsi $f(x) = \frac{2x}{x^2 + 4}$ terdefinisi untuk setiap bilangan riil $x \in \mathbb{R}$. Daerah hasil (*range*) dari fungsi $f(x)$ adalah ....

- A. $\{y \in \mathbb{R} \mid -\frac{1}{4} \le y \le \frac{1}{4}\}$  
  <sub>Salah: Siswa membagi diskriminan secara keliru sehingga menduga batas nilai berada pada interval $\pm \frac{1}{4}$.</sub>
- B. $\{y \in \mathbb{R} \mid -2 \le y \le 2\}$  
  <sub>Salah: Siswa salah menghitung pertidaksamaan diskriminan dengan mengabaikan pembagian koefisien sehingga memperoleh $y^2 \le 4$.</sub>
- C. $\{y \in \mathbb{R} \mid y \ne 0\}$  
  <sub>Salah: Siswa mengira fungsi pecahan tidak pernah menghasilkan nilai $0$, padahal untuk $x=0$, $f(0)=0$.</sub>
- **D. $\{y \in \mathbb{R} \mid -\frac{1}{2} \le y \le \frac{1}{2}\}$** ✅  
  <sub>Benar: Memisalkan $y = \frac{2x}{x^2 + 4} \iff yx^2 - 2x + 4y = 0$. Syarat $x \in \mathbb{R}$ adalah diskriminan $D \ge 0 \implies (-2)^2 - 4(y)(4y) \ge 0 \implies 4 - 16y^2 \ge 0 \implies y^2 \le \frac{1}{4} \implies -\frac{1}{2} \le y \le \frac{1}{2}$.</sub>

**Pembahasan:** Langkah pengerjaan:
1. Misalkan $y = f(x)$, maka $y = \frac{2x}{x^2 + 4}$.
2. Kalikan silang: $y(x^2 + 4) = 2x \implies yx^2 - 2x + 4y = 0$.
3. Kasus $y = 0$: persamaan menjadi $-2x = 0 \implies x = 0 \in \mathbb{R}$, sehingga $y = 0$ merupakan anggota range.
4. Kasus $y \ne 0$: persamaan merupakan persamaan kuadrat dalam $x$. Agar menghasilkan $x \in \mathbb{R}$, diskriminan harus memenuhi $D \ge 0$:
$D = b^2 - 4ac = (-2)^2 - 4(y)(4y) = 4 - 16y^2 \ge 0$.
5. Selesaikan pertidaksamaan:
$16y^2 \le 4 \implies y^2 \le \frac{4}{16} = \frac{1}{4} \implies -\frac{1}{2} \le y \le \frac{1}{2}$.
6. Rentang tersebut mencakup $y = 0$, sehingga daerah hasil dari fungsi $f(x)$ adalah $\{y \in \mathbb{R} \mid -\frac{1}{2} \le y \le \frac{1}{2}\}$.
**Acuan:** siswa — siswa hal.28

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas11-b01-a-hard-bt01-010
*orisinal | C6 | 5 langkah | jenis: analisis daerah asal alami gabungan irasional dan rasional*

Daerah asal alami (*domain*) dari fungsi $f(x) = \sqrt{\frac{3x - 15}{x + 2}} + \frac{1}{\sqrt{36 - x^2}}$ pada himpunan bilangan riil $\mathbb{R}$ adalah ....

- A. $\{x \in \mathbb{R} \mid -2 < x \le 5\}$  
  <sub>Salah: Siswa keliru menyelesaikan pertidaksamaan pecahan $\frac{3x - 15}{x + 2} \ge 0$ dengan mengambil interval di antara pembuat nol.</sub>
- B. $\{x \in \mathbb{R} \mid 5 \le x < 6\}$  
  <sub>Salah: Siswa melupakan bagian interval negatif $x < -2$ yang juga menghasilkan pecahan positif di dalam tanda akar.</sub>
- **C. $\{x \in \mathbb{R} \mid -6 < x < -2 \text{ atau } 5 \le x < 6\}$** ✅  
  <sub>Benar: Syarat pertama untuk $\sqrt{\frac{3x - 15}{x + 2}}$: $\frac{3(x - 5)}{x + 2} \ge 0$ dan $x + 2 \ne 0$. Uji tanda menghasilkan $x < -2$ atau $x \ge 5$. Syarat kedua untuk penyebut $\frac{1}{\sqrt{36 - x^2}}$: bentuk di dalam akar harus positif murni (tidak boleh nol karena di penyebut), sehingga $36 - x^2 > 0 \iff x^2 < 36 \iff -6 < x < 6$. Irisan kedua syarat: $(-6 < x < 6) \cap (x < -2 \text{ atau } x \ge 5) = (-6 < x < -2) \cup [5, 6)$, atau ditulis $\{x \in \mathbb{R} \mid -6 < x < -2 \text{ atau } 5 \le x < 6\}$.</sub>
- D. $\{x \in \mathbb{R} \mid -6 \le x \le -2 \text{ atau } 5 \le x \le 6\}$  
  <sub>Salah: Siswa tidak memperhatikan bahwa penyebut tidak boleh bernilai nol sehingga memasukkan titik $x = \pm 6$ dan $x = -2$ ke dalam daerah asal.</sub>

**Pembahasan:** Langkah 1: Menentukan syarat pertama dari bentuk akar pecahan $\sqrt{\frac{3x - 15}{x + 2}}$.
Bentuk pecahan di dalam akar harus tak negatif dan penyebut tidak boleh nol:
$$\frac{3x - 15}{x + 2} \ge 0 \quad \text{dan} \quad x + 2 \ne 0$$
Pembuat nol pembilang: $3x - 15 = 0 \implies x = 5$.
Pembuat nol penyebut: $x + 2 = 0 \implies x = -2$.
Uji garis bilangan:
- Untuk $x < -2$: pecahan bertanda $\frac{(-)}{(-)} = (+) > 0$ (memenuhi).
- Untuk $-2 < x < 5$: pecahan bertanda $\frac{(-)}{(+)} = (-) < 0$ (tidak memenuhi).
- Untuk $x \ge 5$: pecahan bertanda $\frac{(+)}{(+)} = (+) \ge 0$ (memenuhi).
Diperoleh daerah syarat 1: $D_1 = (-\infty, -2) \cup [5, \infty)$.

Langkah 2: Menentukan syarat kedua dari bentuk pecahan berakar $\frac{1}{\sqrt{36 - x^2}}$.
Karena berada di penyebut, bentuk di dalam akar harus positif murni:
$$36 - x^2 > 0$$
$$x^2 < 36$$
$$-6 < x < 6$$
Diperoleh daerah syarat 2: $D_2 = (-6, 6)$.

Langkah 3: Mengiriskan kedua daerah syarat ($D_f = D_1 \cap D_2$).
$$(-6, 6) \cap ((-\infty, -2) \cup [5, \infty))$$
Bagian pertama: $(-6, 6) \cap (-\infty, -2) = (-6, -2)$
Bagian kedua: $(-6, 6) \cap [5, \infty) = [5, 6)$

Gabungan kedua irisan: $(-6, -2) \cup [5, 6)$ atau dalam notasi himpunan:
$$\{x \in \mathbb{R} \mid -6 < x < -2 \text{ atau } 5 \le x < 6\}$$

Jadi, daerah asal alaminya adalah $\{x \in \mathbb{R} \mid -6 < x < -2 \text{ atau } 5 \le x < 6\}$.
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas11-b01-a-hard-bt01-011
*variasi (konteks) | C5 | 4 langkah | jenis: analisis model pertumbuhan eksponensial*

Berdasarkan data sensus di sebuah kawasan konservasi alam, pada tahun 2012 populasi suatu spesies tercatat sebanyak $18$ ekor. Pada tahun 2013 dan 2014, populasi satwa tersebut berturut-turut tercatat sebanyak $54$ dan $162$ ekor. Apabila pertumbuhan populasi terhadap tahun membentuk fungsi eksponensial $P(t) = a \cdot b^{t - 2012}$, pada tahun berapakah populasi satwa tersebut untuk pertama kalinya melampaui $40.000$ ekor?

- A. 2022  
  <sub>Salah: Menggunakan rasio pertumbuhan sebesar $2$ alih-alih $3$ dari pola data yang diberikan.</sub>
- B. 2019  
  <sub>Salah: Mengira $3^7 = 2.187$ sudah melampaui rasio pembagian karena salah menghitung nilai $18 \times 2.187 = 39.366$ yang ternyata belum mencapai $40.000$.</sub>
- **C. 2020** ✅  
  <sub>Benar: Rasio pertumbuhan tahunan konstan $b = \frac{54}{18} = 3$ dengan $a = 18$. Pertidaksamaan $18 \cdot 3^{t - 2012} > 40.000$ menghasilkan $3^{t - 2012} > 2.222,\bar{2}$. Karena $3^7 = 2.187$ dan $3^8 = 6.561$, nilai pangkat terkecil adalah $t - 2012 = 8$, sehingga $t = 2020$.</sub>
- D. 2021  
  <sub>Salah: Menghitung indeks tahun awal sebagai $t = 1$ pada rumus eksponen sehingga bergeser satu tahun lebih lambat.</sub>

**Pembahasan:** Fungsi populasi: $P(t) = a \cdot b^{t - 2012}$.\nDari data tahun 2012 ($t = 2012$): $P(2012) = a \cdot b^0 = a = 18$.\nDari data tahun 2013 ($t = 2013$): $P(2013) = 18 \cdot b^1 = 54 \implies b = 3$.\nData tahun 2014: $P(2014) = 18 \cdot 3^2 = 162$ (konsisten).\nMaka $P(t) = 18 \cdot 3^{t - 2012}$.\n\nSyarat populasi melampaui $40.000$:\n$$18 \cdot 3^{t - 2012} > 40.000$$\n$$3^{t - 2012} > \frac{40.000}{18} \approx 2.222,22$$\n\nPerpangkatan bilangan 3:\n- $3^7 = 2.187 < 2.222,22$ (populasi $18 \times 2.187 = 39.366$)\n- $3^8 = 6.561 > 2.222,22$ (populasi $18 \times 6.561 = 118.098$)\n\nSehingga nilai bulat terkecil untuk $t - 2012$ adalah $8$:\n$$t - 2012 = 8 \implies t = 2020$$\nPopulasi pertama kali melampaui $40.000$ ekor terjadi pada tahun 2020.
**Acuan:** pretest — kelas11-b01-p0025-latihan-11-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas11-b01-a-hard-bt01-012
*orisinal | C5 | 4 langkah | jenis: analisis rentang nilai fungsi rasional kuadratik*

Diketahui fungsi aljabar $f(x) = \frac{x^2 - 4x + 8}{x - 2}$ yang terdefinisi pada daerah asal alaminya $D_f = \{x \in \mathbb{R} \mid x \ne 2\}$. Daerah hasil (*range*) dari fungsi $f(x)$ adalah ....

- A. $\{y \in \mathbb{R} \mid y \ne 0\}$  
  <sub>Salah: Hanya mengasumsikan range tidak bernilai nol tanpa menganalisis nilai ekstrem kurva rasional.</sub>
- B. $\{y \in \mathbb{R} \mid -4 \le y \le 4\}$  
  <sub>Salah: Terbalik dalam menyelesaikan pertidaksamaan kuadrat $y^2 - 16 \ge 0$ menjadi interval tertutup bagian dalam.</sub>
- C. $\{y \in \mathbb{R} \mid y \le -2 \text{ atau } y \ge 2\}$  
  <sub>Salah: Salah menghitung diskriminan menjadi $y^2 - 4 \ge 0$ akibat keliru mengalikan konstanta $4ac$.</sub>
- **D. $\{y \in \mathbb{R} \mid y \le -4 \text{ atau } y \ge 4\}$** ✅  
  <sub>Benar: Menyusun persamaan kuadrat $x^2 - (y + 4)x + (2y + 8) = 0$ dan menuntut nilai $x$ riil ($D \ge 0$) menghasilkan $y^2 - 16 \ge 0$, yaitu $y \le -4$ atau $y \ge 4$.</sub>

**Pembahasan:** Misalkan $y = f(x)$:\n$$y = \frac{x^2 - 4x + 8}{x - 2}$$\n$$y(x - 2) = x^2 - 4x + 8$$\n$$yx - 2y = x^2 - 4x + 8$$\n$$x^2 - (y + 4)x + (2y + 8) = 0$$\n\nAgar $x$ merupakan bilangan riil, nilai diskriminan $D \ge 0$:\n$$D = [-(y + 4)]^2 - 4(1)(2y + 8) \ge 0$$\n$$(y^2 + 8y + 16) - (8y + 32) \ge 0$$\n$$y^2 - 16 \ge 0$$\n$$(y - 4)(y + 4) \ge 0$$\n$$y \le -4 \text{ atau } y \ge 4$$\n\nPeriksa apakah ada $y$ yang menyebabkan $x = 2$:\nJika $x = 2$, maka $2^2 - (y + 4)(2) + 2y + 8 = 4 - 2y - 8 + 2y + 8 = 4 \ne 0$. Tidak ada nilai $y$ yang menghasilkan $x = 2$.\n\nJadi, daerah hasil fungsi tersebut adalah $\{y \in \mathbb{R} \mid y \le -4 \text{ atau } y \ge 4\}$.
**Acuan:** siswa — siswa hal.31

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas11-b01-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi konsistensi relasi fungsi berparameter*

Diketahui suatu relasi $R$ pada himpunan bilangan riil didefinisikan sebagai himpunan pasangan berurutan:\n$$R = \{(2, a^2 - 3a), (5, 9), (2, 2a + 6), (a - 1, 14)\}$$\nAgar relasi $R$ tersebut merupakan suatu fungsi, nilai $a$ yang memenuhi adalah ....

- A. $5$  
  <sub>Salah: Menjumlahkan kedua akar persamaan kuadrat $a_1 + a_2 = 5$ tanpa menguji konsistensi fungsi.</sub>
- B. $6$  
  <sub>Salah: Hanya menyamakan keluaran pada masukan 2 dan memilih nilai positif tanpa mengevaluasi kontradiksi pasangan terurut terakhir.</sub>
- **C. $-1$** ✅  
  <sub>Benar: Syarat keluaran bernilai tunggal untuk masukan $2$ menghasilkan $a = 6$ atau $a = -1$. Jika $a = 6$, elemen terakhir menjadi $(5, 14)$ yang bertentangan dengan $(5, 9)$, sehingga hanya $a = -1$ yang valid.</sub>
- D. $-6$  
  <sub>Salah: Melakukan kesalahan tanda saat memfaktorkan persamaan kuadrat $a^2 - 5a - 6 = 0$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi, setiap elemen masukan (*input*) harus memiliki tepat satu elemen keluaran (*output*).\n\n1. Perhatikan elemen dengan masukan $x = 2$, yaitu $(2, a^2 - 3a)$ dan $(2, 2a + 6)$. Agar keluarannya tunggal:\n$$a^2 - 3a = 2a + 6$$\n$$a^2 - 5a - 6 = 0$$\n$$(a - 6)(a + 1) = 0$$\nMaka $a = 6$ atau $a = -1$.\n\n2. Uji nilai $a = 6$ ke seluruh himpunan $R$:\n- Pasangan $(2, 6^2 - 3(6)) = (2, 18)$\n- Pasangan $(5, 9)$\n- Pasangan $(2, 2(6) + 6) = (2, 18)$\n- Pasangan $(6 - 1, 14) = (5, 14)$\nKarena ada $(5, 9)$ dan $(5, 14)$, masukan $5$ memiliki dua keluaran berbeda. Jadi $a = 6$ bukan fungsi.\n\n3. Uji nilai $a = -1$:\n- Pasangan $(2, (-1)^2 - 3(-1)) = (2, 4)$\n- Pasangan $(5, 9)$\n- Pasangan $(2, 2(-1) + 6) = (2, 4)$\n- Pasangan $((-1) - 1, 14) = (-2, 14)$\nHimpunan masukan adalah $\{2, 5, -2\}$, masing-masing memiliki tepat satu keluaran. Relasi $R$ merupakan fungsi.\n\nJadi, nilai $a$ yang memenuhi adalah $-1$.
**Acuan:** siswa — siswa hal.20

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas11-b01-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: analisis daerah asal alami gabungan bentuk irasional*

Daerah asal alami (*domain*) dari fungsi $f(x) = \sqrt{\frac{2x - 10}{x^2 - 4x - 12}} + \frac{3}{\sqrt{7 - x}}$ pada himpunan bilangan riil $\mathbb{R}$ adalah ....

- **A. $\{x \in \mathbb{R} \mid -2 < x \le 5 \text{ atau } 6 < x < 7\}$** ✅  
  <sub>Benar: Syarat bentuk akar pertama $\frac{2(x - 5)}{(x - 6)(x + 2)} \ge 0$ menghasilkan $-2 < x \le 5$ atau $x > 6$. Diiriskan dengan syarat penyebut akar kedua $7 - x > 0 \implies x < 7$ menghasilkan $-2 < x \le 5$ atau $6 < x < 7$.</sub>
- B. $\{x \in \mathbb{R} \mid -2 < x < 7\}$  
  <sub>Salah: Mengabaikan interval negatif pada pecahan di dalam tanda akar antara $5 < x < 6$.</sub>
- C. $\{x \in \mathbb{R} \mid -2 \le x \le 5 \text{ atau } 6 \le x < 7\}$  
  <sub>Salah: Memasukkan nilai pembuat nol penyebut $x = -2$ dan $x = 6$ ke dalam pertidaksamaan.</sub>
- D. $\{x \in \mathbb{R} \mid x \le 5 \text{ atau } 6 < x < 7\}$  
  <sub>Salah: Mengabaikan batas asimtot bawah $x > -2$ pada pecahan di dalam akar pertama.</sub>

**Pembahasan:** Agar $f(x)$ terdefinisi pada bilangan riil, harus dipenuhi dua syarat:\n\n1. Syarat pada suku $\sqrt{\frac{2x - 10}{x^2 - 4x - 12}}$:\nBentuk di dalam akar harus non-negatif dan penyebut tidak boleh nol:\n$$\frac{2(x - 5)}{(x - 6)(x + 2)} \ge 0 \quad \text{dengan } x \ne -2, x \ne 6$$\nTitik-titik kritis pada garis bilangan: $x = -2$, $x = 5$, $x = 6$.\nUji tanda interval:\n- Untuk $x < -2$: negatif $(-)$\n- Untuk $-2 < x \le 5$: positif $(+)$\n- Untuk $5 \le x < 6$: negatif $(-)$\n- Untuk $x > 6$: positif $(+)$\nSehingga himpunan penyelesaian pertama adalah: $-2 < x \le 5$ atau $x > 6$.\n\n2. Syarat pada suku $\frac{3}{\sqrt{7 - x}}$:\nBentuk di dalam akar pada penyebut harus positif tegas:\n$$7 - x > 0 \implies x < 7$$\n\n3. Mengiriskan kedua syarat:\n$$(-2 < x \le 5 \text{ atau } x > 6) \cap (x < 7)$$\nHasil irisan adalah $-2 < x \le 5$ atau $6 < x < 7$.\n\nJadi, domain fungsi adalah $\{x \in \mathbb{R} \mid -2 < x \le 5 \text{ atau } 6 < x < 7\}$.
**Acuan:** siswa — siswa hal.30

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas11-b01-a-hard-bt01-015
*orisinal | C5 | 6 langkah | jenis: analisis batas daerah hasil fungsi rasional*

Diketahui fungsi rasional $f(x) = \frac{3x^2 - 2x + 3}{x^2 + 1}$ terdefinisi untuk setiap bilangan riil $x \in \mathbb{R}$. Jika daerah hasil (*range*) dari fungsi tersebut adalah $R_f = \{y \in \mathbb{R} \mid m \le y \le n\}$, maka nilai dari $m^2 + n^2$ adalah ....

- A. 16  
  <sub>Salah: Siswa hanya menghitung kuadrat dari batas atas daerah hasil saja, yaitu $n^2 = 4^2 = 16$.</sub>
- **B. 20** ✅  
  <sub>Benar: Batas daerah hasil diperoleh dari syarat diskriminan persamaan kuadrat $D \ge 0$, menghasilkan selang $2 \le y \le 4$, sehingga $2^2 + 4^2 = 20$.</sub>
- C. 10  
  <sub>Salah: Siswa keliru menyelesaikan pertidaksamaan $(y - 3)^2 \le 1$ menjadi $1 \le y \le 3$, lalu menghitung $1^2 + 3^2 = 10$.</sub>
- D. 25  
  <sub>Salah: Siswa salah menentukan nilai batas $m = 3$ dan $n = 4$ akibat mengabaikan solusi simpangan kiri, sehingga menghitung $3^2 + 4^2 = 25$.</sub>

**Pembahasan:** Misalkan $y = f(x)$:
$$y = \frac{3x^2 - 2x + 3}{x^2 + 1}$$
Karena $x^2 + 1 > 0$ untuk seluruh $x \in \mathbb{R}$, kalikan kedua ruas dengan $(x^2 + 1)$:
$$y(x^2 + 1) = 3x^2 - 2x + 3$$
$$yx^2 + y = 3x^2 - 2x + 3$$
$$(y - 3)x^2 + 2x + (y - 3) = 0$$

1. Jika $y = 3$, maka persamaan menjadi $2x = 0 \iff x = 0 \in \mathbb{R}$. Jadi $y = 3$ termasuk anggota daerah hasil.
2. Jika $y \ne 3$, persamaan tersebut merupakan persamaan kuadrat dalam $x$. Agar menghasilkan nilai masukan $x$ yang riil, diskriminan persamaan harus memenuhi $D \ge 0$:
$$D = b^2 - 4ac \ge 0$$
$$2^2 - 4(y - 3)(y - 3) \ge 0$$
$$4 - 4(y - 3)^2 \ge 0$$
Bagi kedua ruas dengan $4$:
$$1 - (y - 3)^2 \ge 0$$
$$(y - 3)^2 \le 1$$
$$-1 \le y - 3 \le 1$$
$$2 \le y \le 4$$

Dengan demikian, daerah hasil fungsi $f(x)$ adalah $R_f = \{y \in \mathbb{R} \mid 2 \le y \le 4\}$, sehingga $m = 2$ dan $n = 4$.
Nilai dari $m^2 + n^2$ adalah:
$$m^2 + n^2 = 2^2 + 4^2 = 4 + 16 = 20$$
**Acuan:** siswa — siswa hal.29

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas11-b01-a-hard-bt01-016
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi relasi fisik dan pembatasan fungsi*

Dalam suatu eksperimen osilasi pegas, hubungan antara waktu tempuh $t$ (dalam sekon) dan simpangan beban $y$ (dalam $\text{cm}$) dimodelkan oleh persamaan $4t^2 + y^2 = 36$ pada rentang $-3 \le t \le 3$. Berdasarkan definisi fungsi, apakah relasi yang memasangkan waktu $t$ ke simpangan $y$ tersebut merupakan suatu fungsi? Jika bukan, bagaimana pembatasan pada variabel simpangan $y$ agar relasi tersebut menjadi suatu fungsi $y = f(t)$ yang bernilai tak-negatif, dan berapa nilai simpangan maksimumnya?

- A. Bukan fungsi; nilai keluaran dibatasi $y \ge 0$ dengan simpangan maksimum $36\text{ cm}$  
  <sub>Salah: Siswa lupa menarik akar kuadrat dari konstanta 36 saat mencari nilai puncak $y$ pada saat $t = 0$.</sub>
- B. Merupakan fungsi; tidak memerlukan pembatasan nilai keluaran dengan simpangan maksimum $6\text{ cm}$  
  <sub>Salah: Siswa keliru mengira bahwa setiap persamaan tertutup yang terdefinisi pada interval domain otomatis merupakan fungsi tanpa memeriksa keunikan nilai output.</sub>
- C. Bukan fungsi; nilai masukan dibatasi $t \ge 0$ dengan simpangan maksimum $3\text{ cm}$  
  <sub>Salah: Siswa salah membatasi domain masukan $t$ alih-alih rentang keluaran $y$, serta menukar nilai simpangan maksimum dengan batas domain $t$.</sub>
- **D. Bukan fungsi; nilai keluaran dibatasi $y \ge 0$ dengan simpangan maksimum $6\text{ cm}$** ✅  
  <sub>Benar: Untuk setiap $t \in (-3, 3)$, terdapat dua nilai $y$ berbeda yaitu $y = \pm\sqrt{36 - 4t^2}$, sehingga relasi bukan fungsi. Pembatasan $y \ge 0$ menghasilkan satu nilai tunggal $y = \sqrt{36 - 4t^2}$ yang mencapai maksimum $6\text{ cm}$ saat $t = 0$.</sub>

**Pembahasan:** Langkah 1: Menentukan apakah relasi $t \mapsto y$ merupakan fungsi.
Dari persamaan $4t^2 + y^2 = 36$, diperoleh:
$$y^2 = 36 - 4t^2 \implies y = \pm\sqrt{36 - 4t^2}$$
Untuk nilai $t$ di dalam interval $(-3, 3)$, misalnya saat $t = 0$:
$$y = \pm\sqrt{36 - 0} = \pm 6$$
Karena ada nilai masukan $t$ yang dipasangkan dengan dua nilai keluaran $y$ yang berbeda ($6$ dan $-6$), maka relasi tersebut **bukan merupakan fungsi**.

Langkah 2: Membatasi nilai keluaran agar menjadi fungsi tak-negatif.
Agar relasi menjadi fungsi yang bernilai tak-negatif, cabang keluaran negatif dihilangkan dengan menetapkan syarat pembatasan $y \ge 0$. Dengan demikian diperoleh rumus fungsi tunggal:
$$y = f(t) = \sqrt{36 - 4t^2}$$

Langkah 3: Menentukan nilai simpangan maksimum.
Fungsi $f(t) = \sqrt{36 - 4t^2}$ bernilai maksimum ketika suku pengurang $4t^2$ bernilai minimum, yaitu saat $t = 0$:
$$y_{\text{maks}} = \sqrt{36 - 4(0)^2} = \sqrt{36} = 6\text{ cm}$$

Jadi, relasi tersebut bukan fungsi; agar menjadi fungsi tak-negatif nilai keluaran dibatasi $y \ge 0$ dengan simpangan maksimum $6\text{ cm}$.
**Acuan:** pretest — kelas11-b01-p0024-latihan-11-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
