# Lembar koreksi — kelas12_tl SMA12L-B4 subbab B: Variabel Acak Diskret

58 soal | easy 20, medium 20, hard 18 | variasi 27, orisinal 31
> **Kapasitas kurang (hard): 18 dari kuota 20** — 12 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-b-easy-bt01-001
*variasi (konteks) | C1 | 1 langkah | jenis: menentukan nilai variabel acak*

Sebuah percobaan melambungkan 3 keping uang logam seimbang secara bersamaan. Jika variabel acak $Y$ menyatakan banyaknya sisi gambar yang muncul, maka himpunan semua nilai yang mungkin dari variabel acak $Y$ adalah ....

- **A. $\{0, 1, 2, 3\}$** ✅  
  <sub>Benar: Kemungkinan sisi gambar yang muncul pada 3 keping uang logam adalah tidak ada yang muncul (0), satu keping (1), dua keping (2), atau ketiganya (3).</sub>
- B. $\{1, 2, 3, 4\}$  
  <sub>Salah: Menyertakan nilai 4 padahal uang logam yang dilempar hanya ada 3 keping.</sub>
- C. $\{0, 1, 2\}$  
  <sub>Salah: Mengabaikan kemungkinan ketiga keping uang logam seluruhnya menghasilkan sisi gambar.</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Mengabaikan kemungkinan tidak ada sisi gambar yang muncul sama sekali (semua angka / 0 gambar).</sub>

**Pembahasan:** Ruang sampel pelemparan 3 keping uang logam memiliki 8 elemen. Variabel acak $Y$ menyatakan banyaknya sisi gambar. Nilai terkecil adalah saat muncul AAA ($Y = 0$) dan terbesar saat muncul GGG ($Y = 3$). Jadi, nilai-nilai yang mungkin dari $Y$ adalah $\{0, 1, 2, 3\}$.
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-b-easy-bt01-002
*orisinal | C1 | 1 langkah | jenis: karakteristik variabel acak diskret*

Pernyataan berikut yang merupakan salah satu ciri utama dari variabel acak diskret adalah ....

- A. Grafik representasi nilainya membentuk kurva mulus tanpa jeda pada garis bilangan  
  <sub>Salah: Representasi variabel acak diskret berupa titik-titik terpisah pada garis bilangan, bukan kurva mulus kontinu.</sub>
- B. Nilai-nilainya diperoleh secara khusus melalui alat ukur seperti meteran atau timbangan  
  <sub>Salah: Hasil pengukuran dengan alat ukur menghasilkan variabel kontinu.</sub>
- **C. Nilai-nilainya diperoleh dari hasil membilang atau menghitung** ✅  
  <sub>Benar: Berdasarkan Buku Siswa halaman 248, salah satu ciri variabel acak diskret adalah nilainya diperoleh dari hasil menghitung atau membilang.</sub>
- D. Nilai-nilainya selalu berupa bilangan pecahan kontinu dalam suatu selang  
  <sub>Salah: Ciri tersebut merupakan ciri variabel acak kontinu, bukan diskret.</sub>

**Pembahasan:** Berdasarkan ciri-ciri variabel acak diskret pada Buku Siswa halaman 248: (1) Nilainya diperoleh dari hasil menghitung atau membilang; (2) Nilainya berupa bilangan bulat; (3) Hasilnya dapat direpresentasikan berupa titik-titik terpisah pada garis bilangan.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-b-easy-bt01-003
*orisinal | C2 | 2 langkah | jenis: sifat total peluang diskret*

| $x$ | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: |
| $P(X = x)$ | $\frac{1}{6}$ | $\frac{1}{3}$ | $k$ | $\frac{1}{4}$ |

Tabel di atas menyajikan distribusi peluang untuk variabel acak diskret $X$. Nilai $k$ yang memenuhi adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: Siswa salah menjumlahkan pecahan $\frac{1}{6} + \frac{2}{6} = \frac{3}{6}$, lalu langsung mengurangi $1 - \frac{5}{6}$ tanpa memperhitungkan penyebut persekutuan yang benar.</sub>
- **B. $\frac{1}{4}$** ✅  
  <sub>Benar: Total seluruh peluang harus sama dengan 1, sehingga $k = 1 - (\frac{1}{6} + \frac{1}{3} + \frac{1}{4}) = 1 - \frac{9}{12} = \frac{3}{12} = \frac{1}{4}$.</sub>
- C. $\frac{3}{4}$  
  <sub>Salah: Siswa hanya menjumlahkan peluang yang diketahui ($\frac{9}{12} = \frac{3}{4}$) dan lupa mengurangkannya dari 1.</sub>
- D. $\frac{1}{12}$  
  <sub>Salah: Siswa salah hitung pembilang saat menyamakan penyebut menjadi per-12 (misal mengira jumlah peluang lainnya adalah $\frac{11}{12}$).</sub>

**Pembahasan:** Pada variabel acak diskret, jumlah seluruh peluang harus bernilai 1:
$$\sum P(X = x) = 1$$
$$\frac{1}{6} + \frac{1}{3} + k + \frac{1}{4} = 1$$
Samakan penyebut ke 12:
$$\frac{2}{12} + \frac{4}{12} + k + \frac{3}{12} = 1$$
$$\frac{9}{12} + k = 1$$
$$k = 1 - \frac{9}{12} = \frac{3}{12} = \frac{1}{4}$$
Jadi, nilai $k = \frac{1}{4}$.
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-b-easy-bt01-004
*variasi (konteks) | C2 | 2 langkah | jenis: rentang nilai variabel acak*

Sebuah kantong berisi empat keping kartu bernomor 1, 2, 3, dan 4. Dua keping kartu diambil sekaligus secara acak. Jika variabel acak $T$ menyatakan selisih positif antara kedua nomor kartu yang terambil, nilai-nilai yang mungkin untuk variabel acak $T$ adalah ....

- A. $\{2, 3, 4\}$  
  <sub>Salah: Melewatkan selisih bernilai 1 dari pasangan bilangan yang berurutan.</sub>
- B. $\{0, 1, 2, 3\}$  
  <sub>Salah: Mengira kartu yang sama dapat terambil dua kali sehingga selisih bernilai 0, padahal pengambilan dilakukan sekaligus.</sub>
- C. $\{1, 2, 3, 4\}$  
  <sub>Salah: Memasukkan angka 4 sebagai nilai selisih, padahal selisih terbesar hanya 4 - 1 = 3.</sub>
- **D. $\{1, 2, 3\}$** ✅  
  <sub>Benar: Pasangan kartu yang mungkin diambil adalah (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), dan (3, 4). Selisih positifnya masing-masing adalah $|1-2|=1$, $|1-3|=2$, $|1-4|=3$, $|2-3|=1$, $|2-4|=2$, dan $|3-4|=1$. Himpunan nilai yang mungkin untuk $T$ adalah {1, 2, 3}.</sub>

**Pembahasan:** Dua kartu diambil sekaligus dari $\{1, 2, 3, 4\}$. Kemungkinan pasangan nomor yang terambil:
- $(1, 2) \Rightarrow |1 - 2| = 1$
- $(1, 3) \Rightarrow |1 - 3| = 2$
- $(1, 4) \Rightarrow |1 - 4| = 3$
- $(2, 3) \Rightarrow |2 - 3| = 1$
- $(2, 4) \Rightarrow |2 - 4| = 2$
- $(3, 4) \Rightarrow |3 - 4| = 1$

Nilai-nilai unik dari selisih positif $T$ adalah $\{1, 2, 3\}$.
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-b-easy-bt01-005
*variasi (konteks) | C1 | 1 langkah | jenis: identifikasi variabel acak diskret*

Berikut disajikan beberapa besaran dalam suatu pengamatan. Besaran yang tergolong sebagai variabel acak diskret adalah ....

- A. Volume curah hujan harian yang tertampung di stasiun klimatologi  
  <sub>Salah: Volume merupakan variabel kontinu karena diperoleh dari hasil pengukuran fisik.</sub>
- B. Tinggi badan siswa yang mendaftar seleksi tim basket sekolah  
  <sub>Salah: Tinggi badan merupakan variabel kontinu karena diperoleh dari hasil pengukuran.</sub>
- **C. Banyaknya panggilan telepon yang masuk ke sentra layanan dalam kurun waktu satu hari** ✅  
  <sub>Benar: Banyaknya panggilan telepon diperoleh dari hasil membilang/menghitung dan nilainya berupa bilangan bulat non-negatif terpisah (0, 1, 2, ...).</sub>
- D. Waktu yang dibutuhkan pelari untuk menyelesaikan lari maraton  
  <sub>Salah: Waktu merupakan variabel kontinu karena diperoleh dari hasil pengukuran dan nilainya berada dalam interval bilangan real.</sub>

**Pembahasan:** Variabel acak diskret memiliki nilai yang diperoleh dari hasil membilang atau menghitung (countable) serta berupa bilangan bulat terpisah.
- Waktu lari, volume air hujan, dan tinggi badan diperoleh dari hasil pengukuran, sehingga tergolong variabel acak kontinu.
- Banyaknya panggilan telepon diperoleh dari hasil membilang (0, 1, 2, 3, ...), sehingga merupakan variabel acak diskret.
**Acuan:** pretest — kelas12_tl-b04-p0252-latihan-soal-variabel-acak-diskret-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-b-easy-bt01-006
*orisinal | C1 | 1 langkah | jenis: representasi variabel acak diskret*

Berdasarkan ciri-cirinya, representasi dari nilai-nilai variabel acak diskret pada garis bilangan berupa ....

- A. daerah arsiran bidang  
  <sub>Salah: Daerah arsiran bidang merupakan representasi peluang gabungan atau daerah himpunan penyelesaian pertidaksamaan.</sub>
- B. ruas garis kontinu  
  <sub>Salah: Ruas garis kontinu merepresentasikan interval nilai pada variabel acak kontinu.</sub>
- C. garis lurus tak terputus  
  <sub>Salah: Garis lurus tak terputus merupakan representasi fungsi linear kontinu.</sub>
- **D. titik-titik terpisah** ✅  
  <sub>Benar: Berdasarkan materi Buku Siswa halaman 248, nilai-nilai variabel acak diskret direpresentasikan sebagai titik-titik terpisah pada garis bilangan.</sub>

**Pembahasan:** Salah satu ciri utama variabel acak diskret adalah nilainya berupa bilangan diskret yang terpisah satu sama lain. Oleh karena itu, jika digambarkan pada garis bilangan, representasinya berbentuk titik-titik terpisah.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-b-easy-bt01-007
*orisinal | C2 | 1 langkah | jenis: sifat peluang variabel acak diskret*

Sebuah variabel acak diskret $Y$ hanya memiliki tiga nilai yang mungkin, yaitu 1, 2, dan 3. Jika diketahui $P(Y = 1) = 0{,}25$ dan $P(Y = 2) = 0{,}40$, maka nilai $P(Y = 3)$ adalah ....

- A. $0{,}30$  
  <sub>Salah: Melakukan kesalahan aritmetika saat menghitung selisih.</sub>
- B. $0{,}65$  
  <sub>Salah: Hanya menjumlahkan P(Y = 1) + P(Y = 2) tanpa mengurangkannya dari 1.</sub>
- C. $0{,}45$  
  <sub>Salah: Melakukan kesalahan hitung pengurangan 1 - 0,65.</sub>
- **D. $0{,}35$** ✅  
  <sub>Benar: Total seluruh peluang dari variabel acak diskret harus sama dengan 1, sehingga P(Y = 3) = 1 - (0,25 + 0,40) = 1 - 0,65 = 0,35.</sub>

**Pembahasan:** Jumlah seluruh peluang untuk semua nilai variabel acak diskret sama dengan 1:
$$\sum P(Y = y) = 1$$
$$P(Y = 1) + P(Y = 2) + P(Y = 3) = 1$$
$$0{,}25 + 0{,}40 + P(Y = 3) = 1$$
$$0{,}65 + P(Y = 3) = 1$$
$$P(Y = 3) = 1 - 0{,}65 = 0{,}35$$
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-b-easy-bt01-008
*variasi (konteks) | C2 | 1 langkah | jenis: himpunan nilai variabel acak*

Seorang siswa mengerjakan 2 butir soal kuis pilihan ganda secara acak. Misalkan variabel acak $K$ menyatakan banyaknya butir soal yang dijawab dengan salah. Nilai-nilai yang mungkin untuk variabel acak $K$ adalah ....

- **A. $\{0, 1, 2\}$** ✅  
  <sub>Benar: Siswa dapat menjawab benar semua (salah 0), menjawab salah 1 butir, atau menjawab salah kedua butir soal (salah 2).</sub>
- B. $\{0, 1\}$  
  <sub>Salah: Lupa memperhitungkan kemungkinan siswa salah pada kedua butir soal sekaligus ($K = 2$).</sub>
- C. $\{0, 1, 2, 3\}$  
  <sub>Salah: Mengira ada 3 butir soal sehingga nilai maksimum salah adalah 3.</sub>
- D. $\{1, 2\}$  
  <sub>Salah: Lupa memperhitungkan kemungkinan siswa tidak membuat kesalahan sama sekali ($K = 0$).</sub>

**Pembahasan:** Karena jumlah soal yang dikerjakan hanya 2 butir, kemungkinan banyaknya jawaban salah yang diperoleh siswa adalah tidak ada yang salah (0), satu soal salah (1), atau kedua soal salah (2). Jadi, himpunan nilai yang mungkin dari $K$ adalah $\{0, 1, 2\}$.
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-b-easy-bt01-009
*variasi (konteks) | C2 | 2 langkah | jenis: operasi variabel acak diskret*

Kotak I berisi dua kartu bernomor 4 dan 6. Kotak II berisi dua kartu bernomor 1 dan 2. Dari masing-masing kotak diambil satu kartu secara acak. Jika variabel acak $X$ menyatakan nomor kartu yang terambil dari kotak I dan $Y$ menyatakan nomor kartu yang terambil dari kotak II, maka himpunan semua nilai yang mungkin dari variabel acak $Z = X - Y$ adalah ....

- A. $\{1, 2, 3, 4\}$  
  <sub>Salah: Keliru dalam mengurangkan angka kartu dan menganggap rentang selisih berurutan mulai dari 1.</sub>
- B. $\{3, 5\}$  
  <sub>Salah: Hanya menghitung selisih ketika kartu dari kotak II bernomor 1 ($4 - 1$ dan $6 - 1$).</sub>
- **C. $\{2, 3, 4, 5\}$** ✅  
  <sub>Benar: Kemungkinan nilai selisih $X - Y$ adalah $4 - 2 = 2$, $4 - 1 = 3$, $6 - 2 = 4$, dan $6 - 1 = 5$.</sub>
- D. $\{2, 4\}$  
  <sub>Salah: Hanya menghitung selisih ketika kartu dari kotak II bernomor 2 ($4 - 2$ dan $6 - 2$).</sub>

**Pembahasan:** Nilai-nilai yang mungkin untuk $X$ adalah $\{4, 6\}$ dan untuk $Y$ adalah $\{1, 2\}$. Pasangan $(X, Y)$ beserta selisihnya $Z = X - Y$:
- Untuk $X = 4$: $4 - 1 = 3$ dan $4 - 2 = 2$.
- Untuk $X = 6$: $6 - 1 = 5$ dan $6 - 2 = 4$.
Dengan demikian, himpunan semua nilai yang mungkin untuk $Z$ adalah $\{2, 3, 4, 5\}$.
**Acuan:** siswa — siswa hal.251 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-b-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: definisi variabel acak diskret*

Variabel acak yang memiliki ruang sampel berupa himpunan berhingga (*finite*) atau tak berhingga (*infinite*) yang nilainya dapat dihitung satu per satu (*countable*) disebut ....

- A. variabel acak campuran  
  <sub>Salah: Istilah pengacau yang bukan merupakan definisi variabel acak bernilai countable.</sub>
- B. variabel acak bebas  
  <sub>Salah: Terkecoh dengan konsep independensi antara dua kejadian atau dua variabel acak.</sub>
- C. variabel acak kontinu  
  <sub>Salah: Variabel acak kontinu memiliki nilai tak terhitung (uncountable) yang dinyatakan dalam selang bilangan real.</sub>
- **D. variabel acak diskret** ✅  
  <sub>Benar: Sesuai Definisi 4.2 pada buku teks, variabel acak yang nilainya countable disebut variabel acak diskret.</sub>

**Pembahasan:** Berdasarkan Definisi 4.2 pada buku teks: jika ruang sampel dari variabel acak $X$ merupakan himpunan berhingga (*finite*) atau himpunan tak berhingga (*infinite*) yang dapat dihitung satu per satu (*countable*), maka $X$ disebut variabel acak diskret.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-b-easy-bt01-011
*orisinal | C2 | 2 langkah | jenis: peluang nilai variabel acak*

Dua keping uang logam seimbang dilempar bersamaan sebanyak satu kali. Jika variabel acak $X$ menyatakan banyaknya sisi angka yang muncul, maka nilai peluang $P(X = 0)$ adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: Menganggap ada 3 kemungkinan nilai variabel acak $\{0, 1, 2\}$ dan setiap nilai berpeluang sama.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Menghitung peluang komplemen yaitu munculnya paling sedikit satu sisi angka ($P(X \ge 1)$).</sub>
- **C. $\frac{1}{4}$** ✅  
  <sub>Benar: Ruang sampel memiliki 4 anggota dan kejadian $X = 0$ hanya memiliki 1 titik sampel yaitu (G, G), sehingga peluangnya $\frac{1}{4}$.</sub>
- D. $\frac{1}{2}$  
  <sub>Salah: Menyamakan dengan peluang muncul 1 sisi angka ($P(X = 1) = \frac{2}{4}$).</sub>

**Pembahasan:** Ruang sampel pelemparan dua keping uang logam adalah $S = \{AA, AG, GA, GG\}$ dengan $n(S) = 4$.
Variabel acak $X$ menyatakan banyak sisi angka yang muncul. Kejadian $X = 0$ berarti tidak ada angka yang muncul sama sekali, yaitu kejadian munculnya sisi gambar pada kedua keping, yaitu $\{GG\}$ sehingga $n(X = 0) = 1$.
Peluang kemunculannya adalah:
$$P(X = 0) = \frac{n(X = 0)}{n(S)} = \frac{1}{4}$$
**Acuan:** siswa — siswa hal.250

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-b-easy-bt01-012
*variasi (konteks) | C2 | 1 langkah | jenis: identifikasi variabel acak diskret*

Perhatikan beberapa contoh data hasil pengukuran atau penghitungan berikut. Fenomena yang menghasilkan variabel acak diskret adalah ....

- **A. banyaknya kendaraan yang melintasi gerbang tol dalam kurun waktu satu jam** ✅  
  <sub>Benar: Banyaknya kendaraan diperoleh melalui proses mencacah atau membilang dan bernilai bilangan bulat non-negatif sehingga merupakan variabel acak diskret.</sub>
- B. volume bahan bakar yang diisikan ke dalam tangki kendaraan bermotor  
  <sub>Salah: Volume merupakan variabel kontinu karena diperoleh dari proses pengukuran cairan.</sub>
- C. waktu yang dibutuhkan pelari cepat untuk menempuh jarak 100 meter  
  <sub>Salah: Waktu tempuh merupakan data kontinu hasil pengukuran pada skala bilangan real.</sub>
- D. suhu udara harian rata-rata yang dicatat oleh stasiun klimatologi  
  <sub>Salah: Suhu adalah besaran kontinu yang nilainya berada pada suatu interval kontinu.</sub>

**Pembahasan:** Variabel acak diskret memiliki nilai yang diperoleh melalui proses membilang (mencacah) dan nilainya berupa bilangan bulat terpisah. Banyaknya kendaraan melintasi gerbang tol merupakan hasil hitungan bilangan bulat non-negatif $(0, 1, 2, \dots)$, sedangkan waktu, volume, dan suhu diperoleh dari pengukuran yang menghasilkan nilai kontinu.
**Acuan:** pretest — kelas12_tl-b04-p0252-latihan-soal-variabel-acak-diskret-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-b-easy-bt01-013
*variasi (angka) | C2 | 2 langkah | jenis: operasi variabel acak diskret*

Papan putar I memiliki kemungkinan angka terpilih $\{5, 9\}$ dan papan putar II memiliki kemungkinan angka terpilih $\{4, 8\}$. Setiap papan diputar satu kali. Jika variabel acak $X$ menyatakan angka dari papan I dan variabel acak $Y$ menyatakan angka dari papan II, maka nilai minimum dari variabel acak $Z = X + Y$ adalah ....

- A. 5  
  <sub>Salah: Mengambil nilai terkecil dari salah satu papan saja tanpa menjumlahkannya.</sub>
- **B. 9** ✅  
  <sub>Benar: Nilai terkecil $X$ adalah 5 dan nilai terkecil $Y$ adalah 4, sehingga nilai minimum $Z = 5 + 4 = 9$.</sub>
- C. 17  
  <sub>Salah: Menghitung nilai maksimum $9 + 8 = 17$ alih-alih nilai minimum.</sub>
- D. 13  
  <sub>Salah: Mengambil kombinasi nilai tengah $5 + 8$ atau $9 + 4$.</sub>

**Pembahasan:** Nilai-nilai yang mungkin untuk $X$ adalah $\{5, 9\}$ dan untuk $Y$ adalah $\{4, 8\}$. Nilai dari $Z = X + Y$ adalah:
- $5 + 4 = 9$
- $5 + 8 = 13$
- $9 + 4 = 13$
- $9 + 8 = 17$
Nilai terkecil (minimum) dari $Z$ adalah 9.
**Acuan:** siswa — siswa hal.248 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-b-easy-bt01-014
*variasi (konteks) | C2 | 1 langkah | jenis: karakteristik variabel acak diskret*

Variabel acak $X$ menyatakan banyaknya gol tim tuan rumah dan variabel acak $Y$ menyatakan banyaknya gol tim tamu dalam sebuah pertandingan bola. Kedua variabel tersebut merupakan variabel acak diskret. Jika didefinisikan variabel baru $W = X - Y$ yang menyatakan selisih gol kedua tim, maka variabel $W$ merupakan ....

- A. variabel acak tak terdefinisi  
  <sub>Salah: Menganggap pengurangan dua kejadian acak tidak menghasilkan variabel acak yang sah.</sub>
- B. variabel acak kontinu  
  <sub>Salah: Keliru mengira operasi pengurangan membuat himpunan nilai menjadi kontinu.</sub>
- C. bukan variabel acak  
  <sub>Salah: Mengira hasil selisih yang bisa bernilai negatif bukan merupakan variabel acak.</sub>
- **D. variabel acak diskret** ✅  
  <sub>Benar: Selisih dari dua variabel acak diskret menghasilkan nilai berupa bilangan bulat yang terhitung satu per satu sehingga tetap merupakan variabel acak diskret.</sub>

**Pembahasan:** Variabel $X$ dan $Y$ bernilai bilangan bulat non-negatif. Selisih $W = X - Y$ menghasilkan bilangan bulat ($\{\dots, -2, -1, 0, 1, 2, \dots\}$) yang nilainya terpisah pada garis bilangan dan dapat dihitung satu per satu (*countable*). Berdasarkan Definisi 4.2, variabel $W$ adalah variabel acak diskret.
**Acuan:** siswa — siswa hal.251 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-b-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: sifat total peluang diskret*

Suatu variabel acak diskret $Z$ hanya memiliki empat kemungkinan nilai, yaitu 1, 2, 3, dan 4. Jika diketahui $P(Z = 1) = \frac{1}{8}$, $P(Z = 2) = \frac{3}{8}$, dan $P(Z = 3) = \frac{2}{8}$, maka nilai dari $P(Z = 4)$ adalah ....

- A. $\frac{1}{8}$  
  <sub>Salah: Salah menjumlahkan peluang yang diketahui menjadi $\frac{7}{8}$.</sub>
- **B. $\frac{2}{8}$** ✅  
  <sub>Benar: Total seluruh peluang harus 1, sehingga $P(Z = 4) = 1 - \left(\frac{1}{8} + \frac{3}{8} + \frac{2}{8}\right) = \frac{2}{8}$.</sub>
- C. $\frac{6}{8}$  
  <sub>Salah: Hanya menjumlahkan ketiga peluang yang diketahui tanpa mengurangkan dari 1.</sub>
- D. $\frac{3}{8}$  
  <sub>Salah: Salah menghitung sisa pecahan dari 1.</sub>

**Pembahasan:** Jumlah seluruh peluang untuk semua nilai variabel acak diskret adalah 1:
$$P(Z = 1) + P(Z = 2) + P(Z = 3) + P(Z = 4) = 1$$
$$\frac{1}{8} + \frac{3}{8} + \frac{2}{8} + P(Z = 4) = 1$$
$$\frac{6}{8} + P(Z = 4) = 1$$
$$P(Z = 4) = 1 - \frac{6}{8} = \frac{2}{8}$$
**Acuan:** siswa — siswa hal.251

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-b-easy-bt01-016
*variasi (konteks) | C2 | 1 langkah | jenis: identifikasi variabel acak diskret*

Di antara variabel acak berikut, manakah yang merupakan variabel acak diskret?

- **A. Banyaknya siswa yang lulus ujian matematika di suatu kelas** ✅  
  <sub>Benar: Banyaknya siswa diperoleh dari proses membilang atau menghitung sehingga nilainya berupa bilangan bulat diskret.</sub>
- B. Suhu udara ruangan kelas yang diukur setiap jam  
  <sub>Salah: Suhu merupakan variabel acak kontinu yang nilainya berada pada interval kontinu.</sub>
- C. Waktu tempuh pelari maraton menuju garis finis  
  <sub>Salah: Waktu merupakan variabel acak kontinu karena diperoleh melalui pengukuran pada suatu selang bilangan real.</sub>
- D. Volume air mineral dalam sebuah botol kemasan  
  <sub>Salah: Volume merupakan variabel acak kontinu hasil pengukuran besaran fluida.</sub>

**Pembahasan:** Variabel acak diskret adalah variabel yang nilainya diperoleh dari hasil menghitung/membilang dan berupa bilangan bulat terpisah. Banyaknya siswa yang lulus diperoleh dengan membilang (0, 1, 2, ...), sehingga merupakan variabel acak diskret. Waktu, volume, dan suhu merupakan hasil pengukuran yang tergolong variabel acak kontinu.
**Acuan:** siswa — siswa hal.252 Latihan Soal Variabel Acak Diskret

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-b-easy-bt01-017
*variasi (konteks) | C2 | 2 langkah | jenis: himpunan nilai variabel acak*

Sebuah kantong berisi 4 bola merah dan 2 bola putih. Dari kantong tersebut diambil 2 bola sekaligus secara acak. Jika variabel acak $B$ menyatakan banyaknya bola putih yang terambil, maka himpunan semua nilai yang mungkin untuk $B$ adalah ....

- A. $\{1, 2\}$  
  <sub>Salah: Siswa mengabaikan kemungkinan tidak ada bola putih yang terambil sama sekali (keduanya bola merah).</sub>
- B. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Siswa keliru memasukkan jumlah bola merah ke dalam kemungkinan nilai bola putih.</sub>
- **C. $\{0, 1, 2\}$** ✅  
  <sub>Benar: Bola putih yang terambil dapat berupa 0 bola (keduanya merah), 1 bola (satu merah satu putih), atau 2 bola (keduanya putih).</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Siswa mengira nilai variabel acak dihitung mulai dari 1 dan melebihi jumlah bola yang diambil.</sub>

**Pembahasan:** Banyak bola yang diambil adalah 2 bola. Di dalam kantong terdapat 2 bola putih dan 4 bola merah. Kemungkinan terambilnya bola putih adalah:
- 0 bola putih (keduanya bola merah),
- 1 bola putih (1 putih dan 1 merah),
- 2 bola putih (keduanya bola putih).
Jadi, nilai-nilai yang mungkin untuk $B$ adalah $\{0, 1, 2\}$.
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-b-easy-bt01-018
*variasi (angka) | C2 | 1 langkah | jenis: nilai ekstrem variabel acak*

Dua roda putar angka diputar masing-masing satu kali. Roda pertama menghasilkan kemungkinan angka $X \in \{10, 20\}$ dan roda kedua menghasilkan kemungkinan angka $Y \in \{30, 50\}$. Jika variabel acak $W = X + Y$ menyatakan jumlah angka yang diperoleh, maka nilai terkecil dari $W$ adalah ....

- A. $30$  
  <sub>Salah: Siswa hanya mengambil nilai minimum dari roda kedua tanpa menjumlahkannya dengan nilai minimum roda pertama.</sub>
- **B. $40$** ✅  
  <sub>Benar: Nilai terkecil diperoleh dengan menjumlahkan nilai minimum dari $X$ dan $Y$, yaitu $10 + 30 = 40$.</sub>
- C. $70$  
  <sub>Salah: Siswa menghitung nilai terbesar ($20 + 50$) alih-alih nilai terkecil.</sub>
- D. $50$  
  <sub>Salah: Siswa menjumlahkan $20 + 30$ bukan pasangan nilai terkecil.</sub>

**Pembahasan:** Nilai yang mungkin dari $X$ adalah 10 atau 20, dan nilai yang mungkin dari $Y$ adalah 30 atau 50. Nilai $W = X + Y$ yang mungkin adalah:
- $10 + 30 = 40$
- $10 + 50 = 60$
- $20 + 30 = 50$
- $20 + 50 = 70$
Nilai terkecil dari $W$ adalah 40.
**Acuan:** siswa — siswa hal.248 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-b-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: karakteristik variabel acak diskret*

Berdasarkan ciri-cirinya, nilai yang dihasilkan oleh suatu variabel acak diskret selalu berupa ....

- A. seluruh bilangan real pada suatu interval  
  <sub>Salah: Karakteristik seluruh bilangan real pada interval adalah ciri dari variabel acak kontinu.</sub>
- **B. bilangan bulat** ✅  
  <sub>Benar: Sesuai ciri variabel acak diskret pada buku teks, nilainya berupa bilangan bulat.</sub>
- C. bilangan pecahan tak hingga  
  <sub>Salah: Nilai variabel acak diskret adalah diskret dan terpisah berupa bilangan bulat, bukan bilangan pecahan tak hingga.</sub>
- D. bilangan irasional  
  <sub>Salah: Variabel acak diskret berasal dari hasil hitungan sehingga tidak berupa bilangan irasional.</sub>

**Pembahasan:** Berdasarkan buku siswa, ciri-ciri variabel acak diskret antara lain: nilainya diperoleh dari hasil menghitung atau membilang, nilainya berupa bilangan bulat, dan hasilnya dapat direpresentasikan berupa titik-titik terpisah pada garis bilangan.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-b-easy-bt01-020
*variasi (konteks) | C2 | 1 langkah | jenis: klasifikasi variabel acak*

Dalam suatu survei peternakan, petugas mengumpulkan sejumlah data pengukuran dan pencatatan. Di antara parameter berikut, data yang merepresentasikan variabel acak diskret adalah ....

- **A. banyaknya sapi betina di peternakan** ✅  
  <sub>Benar: Banyaknya sapi betina diperoleh melalui proses membilang atau menghitung sehingga nilainya berupa bilangan bulat dan merupakan variabel acak diskret.</sub>
- B. kadar lemak pada susu per liter  
  <sub>Salah: Siswa salah membedakan persentase kadar nutrisi hasil uji laboratorium yang bersifat kontinu dengan variabel diskret.</sub>
- C. luas area kandang yang digunakan  
  <sub>Salah: Siswa keliru mengira ukuran luas wilayah dapat dihitung satu per satu, padahal merupakan besaran kontinu.</sub>
- D. volume susu sapi segar yang diproduksi  
  <sub>Salah: Siswa keliru menganggap volume cairan sebagai variabel acak diskret, padahal diperoleh dari hasil pengukuran (kontinu).</sub>

**Pembahasan:** Variabel acak diskret memiliki ciri nilainya diperoleh dari hasil menghitung/membilang dan berupa bilangan bulat (cacah). Dari keempat opsi:
- Volume susu, luas area kandang, dan kadar lemak diperoleh melalui hasil pengukuran dengan alat ukur sehingga nilainya berada pada interval kontinu (variabel kontinu).
- Banyaknya sapi betina diperoleh dari hasil membilang satu per satu (0, 1, 2, 3, ...) sehingga merupakan variabel acak diskret.
**Acuan:** siswa — siswa hal.252 Latihan Soal Variabel Acak Diskret

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-b-medium-bt01-001
*variasi (konteks) | C3 | 3 langkah | jenis: banyaknya nilai variabel acak*

Dua buah dadu bersisi empat (tetrahedral) seimbang masing-masing memiliki sisi bernomor 1, 2, 3, dan 4. Kedua dadu dilemparkan bersama-sama sebanyak satu kali. Jika variabel acak $X$ menyatakan hasil kali kedua mata dadu yang muncul, maka banyaknya nilai berbeda yang mungkin untuk variabel acak $X$ adalah ....

- A. 16  
  <sub>Salah: Menghitung total banyak pasangan titik sampel ruang sampel ($4 \times 4$), bukan banyaknya nilai unik yang dihasilkan oleh variabel acak.</sub>
- B. 7  
  <sub>Salah: Mengira hasil perkalian sama banyaknya dengan hasil penjumlahan dua mata dadu ($2$ sampai $8$, yaitu $7$ nilai).</sub>
- **C. 9** ✅  
  <sub>Benar: Pasangan mata dadu yang mungkin adalah hasil perkalian elemen himpunan $\{1, 2, 3, 4\}$. Hasil kalinya adalah $1, 2, 3, 4, 6, 8, 9, 12, 16$, sehingga terdapat tepat 9 nilai berbeda.</sub>
- D. 10  
  <sub>Salah: Keliru menganggap perkalian $2 \times 2$ dan $1 \times 4$ menghasilkan dua nilai yang berbeda.</sub>

**Pembahasan:** Ruang sampel pelemparan dua dadu bersisi 4 memiliki ukuran $4 \times 4 = 16$ pasangan $(d_1, d_2)$. Nilai variabel acak $X = d_1 \times d_2$ untuk tiap pasangan adalah:
- $1 \times 1 = 1$
- $1 \times 2 = 2, 2 \times 1 = 2$
- $1 \times 3 = 3, 3 \times 1 = 3$
- $1 \times 4 = 4, 4 \times 1 = 4, 2 \times 2 = 4$
- $2 \times 3 = 6, 3 \times 2 = 6$
- $2 \times 4 = 8, 4 \times 2 = 8$
- $3 \times 3 = 9$
- $3 \times 4 = 12, 4 \times 3 = 12$
- $4 \times 4 = 16$

Himpunan nilai-nilai unik yang mungkin untuk variabel acak $X$ adalah $\{1, 2, 3, 4, 6, 8, 9, 12, 16\}$. Jadi, terdapat 9 nilai berbeda.
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-b-medium-bt01-002
*orisinal | C3 | 3 langkah | jenis: distribusi peluang dengan parameter*

Sebuah variabel acak diskret $X$ memiliki ruang nilai $\{1, 2, 3, 4\}$. Fungsi peluang dari $X$ dirumuskan dengan $P(X = x) = c \cdot x$ untuk setiap $x \in \{1, 2, 3, 4\}$, dengan $c$ merupakan suatu konstanta. Nilai dari $P(X \ge 3)$ adalah ....

- **A. $\frac{7}{10}$** ✅  
  <sub>Benar: Karena total peluang bernilai 1, diperoleh $c(1+2+3+4) = 1 \implies c = \frac{1}{10}$. Maka $P(X \ge 3) = P(X=3) + P(X=4) = 3c + 4c = 7c = \frac{7}{10}$.</sub>
- B. $\frac{3}{10}$  
  <sub>Salah: Hanya menghitung nilai $P(X = 3) = \frac{3}{10}$ tanpa menjumlahkan dengan nilai $P(X = 4)$.</sub>
- C. $\frac{2}{5}$  
  <sub>Salah: Tertukar menghitung peluang komplemennya yang ketat, yaitu $P(X < 3) = P(X=1) + P(X=2) = \frac{3}{10}$ atau salah hitung $P(X = 4) = \frac{4}{10} = \frac{2}{5}$.</sub>
- D. $\frac{1}{10}$  
  <sub>Salah: Hanya menyelesaikan nilai konstanta $c$ dan lupa menghitung $P(X \ge 3)$.</sub>

**Pembahasan:** Berdasarkan sifat distribusi peluang variabel acak diskret, jumlah total seluruh peluang harus bernilai 1:
$$\sum_{x=1}^{4} P(X = x) = 1$$
$$c(1) + c(2) + c(3) + c(4) = 1$$
$$10c = 1 \implies c = \frac{1}{10}$$

Selanjutnya, tentukan nilai $P(X \ge 3)$:
$$P(X \ge 3) = P(X = 3) + P(X = 4)$$
$$P(X \ge 3) = 3c + 4c = 7c = 7 \times \frac{1}{10} = \frac{7}{10}$$
Jadi, nilai $P(X \ge 3)$ adalah $\frac{7}{10}$.
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-b-medium-bt01-003
*orisinal | C4 | 3 langkah | jenis: distribusi peluang pengambilan bola*

Sebuah kantong berisi 3 bola merah dan 2 bola putih. Dari kantong tersebut diambil 2 bola sekaligus secara acak. Jika variabel acak $K$ menyatakan banyaknya bola merah yang terambil, maka nilai peluang $P(K = 1)$ adalah ....

- **A. $\frac{3}{5}$** ✅  
  <sub>Benar: Banyaknya cara mengambil 2 bola dari 5 adalah $\binom{5}{2} = 10$. Banyaknya cara mengambil 1 merah dan 1 putih adalah $\binom{3}{1} \times \binom{2}{1} = 6$. Peluangnya $\frac{6}{10} = \frac{3}{5}$.</sub>
- B. $\frac{3}{10}$  
  <sub>Salah: Hanya menghitung kemungkinan terambilnya 2 bola merah $\binom{3}{2}/10 = \frac{3}{10}$, atau hanya menghitung urutan merah-putih tanpa mengalikannya dengan faktor susunan.</sub>
- C. $\frac{2}{5}$  
  <sub>Salah: Menggunakan peluang kejadian komplemen yang salah atau keliru membagi $\frac{4}{10}$.</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: Keliru menghitung peluang terambilnya 0 bola merah (2 bola putih), yaitu $\frac{\binom{2}{2}}{10} = \frac{1}{10}$, lalu menduplikasi pembilang secara acak.</sub>

**Pembahasan:** Total bola dalam kantong adalah $3 + 2 = 5$ bola. Diambil 2 bola sekaligus.
Banyaknya anggota ruang sampel adalah:
$$n(S) = \binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10$$

Variabel acak $K$ menyatakan banyaknya bola merah yang terambil. Kejadian $K = 1$ berarti terambil 1 bola merah dan 1 bola putih:
$$n(K = 1) = \binom{3}{1} \times \binom{2}{1} = 3 \times 2 = 6$$

Peluang terjadinya $K = 1$ adalah:
$$P(K = 1) = \frac{n(K = 1)}{n(S)} = \frac{6}{10} = \frac{3}{5}$$
Jadi, nilai dari $P(K = 1)$ adalah $\frac{3}{5}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-b-medium-bt01-004
*variasi (konteks) | C3 | 3 langkah | jenis: operasi selisih dua variabel acak*

Kotak I berisi dua kartu bernomor 4 dan 7 dengan peluang masing-masing terpilih adalah $0{,}4$ dan $0{,}6$. Kotak II berisi tiga kartu bernomor 1, 2, dan 3 dengan peluang terpilih masing-masing sama besar. Dari masing-masing kotak diambil satu kartu secara acak. Misalkan variabel acak $X$ menyatakan nomor kartu dari kotak I dan variabel acak $Y$ menyatakan nomor kartu dari kotak II. Jika didefinisikan variabel acak $Z = X - Y$, maka nilai peluang $P(Z = 5)$ adalah ....

- A. $0{,}133$  
  <sub>Salah: Salah mengalikan peluang $0{,}4 \times \frac{1}{3}$.</sub>
- B. $0{,}4$  
  <sub>Salah: Hanya menggunakan peluang terpilihnya kartu bernomor 4 pada Kotak I.</sub>
- **C. $0{,}2$** ✅  
  <sub>Benar: Kombinasi yang menghasilkan $X - Y = 5$ hanya pasangan $(7, 2)$, dengan peluang $0{,}6 \times \frac{1}{3} = 0{,}2$.</sub>
- D. $0{,}3$  
  <sub>Salah: Mengalikan peluang kartu 7 ($0{,}6$) dengan $\frac{1}{2}$ karena mengira isi Kotak II hanya 2 kartu.</sub>

**Pembahasan:** Nilai yang mungkin dari $X$ adalah $\{4, 7\}$ dengan $P(X = 4) = 0{,}4$ dan $P(X = 7) = 0{,}6$.

Nilai yang mungkin dari $Y$ adalah $\{1, 2, 3\}$ dengan $P(Y = 1) = P(Y = 2) = P(Y = 3) = \frac{1}{3}$.

Variabel acak $Z = X - Y = 5$ tercapai apabila:
$X - Y = 5 \implies (X, Y) = (7, 2)$
(karena jika $X = 4$, nilai $Y$ harus $-1$ yang tidak ada pada Kotak II).

Karena pengambilan dari kedua kotak bersifat bebas, peluangnya adalah:
$$P(Z = 5) = P(X = 7) \times P(Y = 2) = 0{,}6 \times \frac{1}{3} = 0{,}2$$
**Acuan:** siswa — siswa hal.251 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-b-medium-bt01-005
*orisinal | C4 | 3 langkah | jenis: distribusi peluang rumus parameter*

Sebuah variabel acak diskret $X$ memiliki himpunan nilai $\{1, 2, 3\}$. Fungsi peluang dari $X$ dinyatakan oleh:
$$P(X = x) = \frac{k}{x(x+1)}$$
untuk $x \in \{1, 2, 3\}$, dengan $k$ suatu konstanta real. Nilai dari $P(X \ge 2)$ adalah ....

- A. $\frac{2}{3}$  
  <sub>Salah: Menghitung nilai $P(X = 1)$ bukan $P(X \ge 2)$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Keliru menganggap nilai konstanta $k = 2$.</sub>
- **C. $\frac{1}{3}$** ✅  
  <sub>Benar: Dari $\sum P(X=x) = k(\frac{1}{2}+\frac{1}{6}+\frac{1}{12}) = \frac{3}{4}k = 1$, diperoleh $k = \frac{4}{3}$. Maka $P(X \ge 2) = \frac{4}{3}(\frac{1}{6}+\frac{1}{12}) = \frac{1}{3}$.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Lupa mengalikan jumlah $\frac{1}{6} + \frac{1}{12}$ dengan konstanta $k$.</sub>

**Pembahasan:** Berdasarkan sifat distribusi peluang variabel acak diskret, jumlah total peluang harus sama dengan 1:
$$\sum_{x=1}^{3} P(X = x) = 1$$

Hitung masing-masing komponen:
$$P(X = 1) = \frac{k}{1 \cdot 2} = \frac{k}{2}$$
$$P(X = 2) = \frac{k}{2 \cdot 3} = \frac{k}{6}$$
$$P(X = 3) = \frac{k}{3 \cdot 4} = \frac{k}{12}$$

Jumlahkan ketiga nilai peluang tersebut:
$$k \left( \frac{1}{2} + \frac{1}{6} + \frac{1}{12} \right) = 1$$
$$k \left( \frac{6 + 2 + 1}{12} \right) = 1 \implies k \cdot \frac{9}{12} = 1 \implies k \cdot \frac{3}{4} = 1 \implies k = \frac{4}{3}$$

Nilai dari $P(X \ge 2)$ adalah:
$$P(X \ge 2) = P(X = 2) + P(X = 3) = \frac{k}{6} + \frac{k}{12} = k \left( \frac{2 + 1}{12} \right) = \frac{4}{3} \cdot \frac{3}{12} = \frac{1}{3}$$
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-b-medium-bt01-006
*orisinal | C4 | 2 langkah | jenis: analisis konsep ruang sampel tak hingga*

Sekeping koin seimbang dilambungkan berulang-ulang sampai muncul sisi Angka untuk pertama kalinya. Misalkan variabel acak $N$ menyatakan banyaknya pelambungan yang dilakukan hingga eksperimen tersebut berhenti. Karakteristik yang tepat mengenai variabel acak $N$ berdasarkan definisinya adalah ....

- A. ruang sampelnya merupakan himpunan tak berhingga (infinite) dan tak terhitung (uncountable), sehingga $N$ bukan variabel acak diskret  
  <sub>Salah: Mengira himpunan tak berhingga selalu tak terhitung (uncountable).</sub>
- B. ruang sampelnya merupakan himpunan berhingga (finite) dan terhitung (countable), sehingga $N$ adalah variabel acak diskret  
  <sub>Salah: Keliru menganggap proses pelambungan pasti berhenti pada batas lemparan tertentu.</sub>
- C. variabel acak $N$ merupakan variabel acak kontinu karena banyaknya lemparan dapat bertambah terus-menerus tanpa batas  
  <sub>Salah: Menyamakan konsep tak hingga dengan sifat variabel kontinu.</sub>
- **D. ruang sampelnya merupakan himpunan tak berhingga (infinite) yang dapat dihitung satu per satu (countable), sehingga $N$ adalah variabel acak diskret** ✅  
  <sub>Benar: Eksperimen bisa berlanjut tanpa batas $N \in \{1, 2, 3, \dots\}$ sehingga tak berhingga, namun nilainya berupa bilangan asli yang terhitung, memenuhi definisi variabel acak diskret.</sub>

**Pembahasan:** Ruang sampel kejadian adalah:
$$S = \{\text{A}, \text{GA}, \text{GGA}, \text{GGGA}, \dots\}$$

Nilai yang mungkin dari variabel acak $N$ adalah banyaknya pelambungan:
$$N \in \{1, 2, 3, 4, \dots\}$$

Himpunan nilai ini tidak memiliki batas atas, sehingga merupakan himpunan tak berhingga (*infinite*). Akan tetapi, setiap elemennya berupa bilangan bulat positif yang dapat didaftar dan dikorespondensikan satu per satu dengan bilangan asli (*countable*).

Sesuai Definisi 4.2 di buku teks, variabel acak yang didefinisikan pada himpunan tak berhingga yang terhitung (*countable*) digolongkan sebagai variabel acak diskret.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-b-medium-bt01-007
*variasi (angka) | C3 | 3 langkah | jenis: operasi penjumlahan dua variabel acak*

Papan putar I memiliki dua sektor bernomor 3 dan 5 dengan peluang masing-masing $P(X = 3) = \frac{1}{3}$ dan $P(X = 5) = \frac{2}{3}$. Papan putar II memiliki dua sektor bernomor 2 dan 4 dengan peluang masing-masing $P(Y = 2) = \frac{1}{2}$ dan $P(Y = 4) = \frac{1}{2}$. Jika kedua papan diputar bersamaan dan didefinisikan variabel acak $Z = X + Y$, maka nilai dari $P(Z = 7)$ adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: Hanya menghitung peluang pasangan pertama $(3, 4)$ saja.</sub>
- **B. $\frac{1}{2}$** ✅  
  <sub>Benar: Nilai $Z = 7$ diperoleh dari pasangan $(X=3, Y=4)$ atau $(X=5, Y=2)$. Peluangnya adalah $(\frac{1}{3} \times \frac{1}{2}) + (\frac{2}{3} \times \frac{1}{2}) = \frac{1}{6} + \frac{2}{6} = \frac{3}{6} = \frac{1}{2}$.</sub>
- C. $\frac{1}{3}$  
  <sub>Salah: Hanya menghitung peluang pasangan kedua $(5, 2)$ saja.</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: Salah menjumlahkan peluang dengan menjumlahkan pembilang tanpa mengalikan kedua papan terlebih dahulu.</sub>

**Pembahasan:** Kombinasi nilai $(X, Y)$ yang menghasilkan $Z = X + Y = 7$ adalah:
1. $X = 3$ dan $Y = 4 \implies P(X = 3, Y = 4) = \frac{1}{3} \times \frac{1}{2} = \frac{1}{6}$
2. $X = 5$ dan $Y = 2 \implies P(X = 5, Y = 2) = \frac{2}{3} \times \frac{1}{2} = \frac{2}{6}$

Karena kedua kejadian saling lepas:
$$P(Z = 7) = \frac{1}{6} + \frac{2}{6} = \frac{3}{6} = \frac{1}{2}$$.
**Acuan:** siswa — siswa hal.248 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-b-medium-bt01-008
*orisinal | C3 | 3 langkah | jenis: sifat total peluang variabel acak*

Sebuah variabel acak diskret $W$ memiliki himpunan nilai $\{0, 1, 2, 3\}$. Distribusi peluang dari $W$ disajikan dalam fungsi berikut:
$$P(W = w) = c(2w + 1)$$
untuk $w \in \{0, 1, 2, 3\}$, dengan $c$ merupakan suatu konstanta. Nilai dari peluang $P(W > 1)$ adalah ....

- A. $\frac{7}{16}$  
  <sub>Salah: Hanya menghitung nilai peluang pada $w = 3$ saja.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Menghitung komplemennya yaitu $P(W \le 1) = \frac{1+3}{16} = \frac{4}{16} = \frac{1}{4}$.</sub>
- **C. $\frac{3}{4}$** ✅  
  <sub>Benar: Total peluang: $\sum_{w=0}^3 c(2w+1) = c(1 + 3 + 5 + 7) = 16c = 1 \implies c = \frac{1}{16}$. Kejadian $W > 1$ meliputi $w = 2$ dan $w = 3$, sehingga peluangnya $c(5 + 7) = 12c = \frac{12}{16} = \frac{3}{4}$.</sub>
- D. $\frac{5}{16}$  
  <sub>Salah: Hanya menghitung nilai peluang pada $w = 2$ saja.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $c$ menggunakan sifat total peluang bernilai 1.
$$\sum_{w=0}^3 P(W = w) = 1$$
$$c(2(0)+1) + c(2(1)+1) + c(2(2)+1) + c(2(3)+1) = 1$$
$$c(1 + 3 + 5 + 7) = 1$$
$$16c = 1 \implies c = \frac{1}{16}$$

Langkah 2: Menghitung $P(W > 1)$:
$$P(W > 1) = P(W = 2) + P(W = 3) = c(5) + c(7) = 12c$$
$$P(W > 1) = 12 \times \frac{1}{16} = \frac{12}{16} = \frac{3}{4}$$.
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-b-medium-bt01-009
*orisinal | C4 | 3 langkah | jenis: analisis sifat variabel acak*

Perhatikan tiga variabel acak berikut:
(1) $V_1$: Banyaknya mobil yang melewati sebuah pos tol dalam selang waktu 1 jam.
(2) $V_2$: Jarak tempuh sebuah mobil per liter bahan bakar.
(3) $V_3$: Banyaknya pelemparan koin yang dibutuhkan hingga muncul sisi Angka pertama kali.

Berdasarkan sifat ruang sampelnya, pernyataan yang tepat mengenai ketiga variabel acak tersebut adalah ....

- A. Ketiga variabel tersebut merupakan variabel acak diskret.  
  <sub>Salah: Keliru menganggap jarak tempuh ($V_2$) sebagai variabel diskret, padahal jarak diperoleh dari hasil pengukuran kontinu.</sub>
- B. $V_1$ dan $V_2$ adalah variabel acak diskret, sedangkan $V_3$ adalah variabel kontinu.  
  <sub>Salah: Tertukar antara variabel kontinu hasil pengukuran fisik dengan variabel diskret tak hingga yang countable.</sub>
- C. Hanya $V_1$ yang merupakan variabel acak diskret karena ruang sampelnya berhingga.  
  <sub>Salah: Keliru mengira bahwa variabel acak diskret hanya boleh memiliki ruang sampel berhingga, padahal himpunan tak hingga yang countable ($V_3$) juga diskret.</sub>
- **D. $V_1$ dan $V_3$ adalah variabel acak diskret, sedangkan $V_2$ adalah variabel kontinu.** ✅  
  <sub>Benar: $V_1$ bernilai cacah berhingga/dapat dicacah $\{0, 1, 2, \dots\}$ (diskret), $V_3$ bernilai asli tak berhingga terhitung $\{1, 2, 3, \dots\}$ (diskret countable), sedangkan $V_2$ diperoleh dari pengukuran pada interval bilangan real (kontinu).</sub>

**Pembahasan:** Berdasarkan Definisi 4.2 pada buku teks:
- Variabel acak diskret adalah variabel acak yang ruang sampelnya berhingga (*finite*) atau tak berhingga yang dapat dihitung satu per satu (*countable*).
- $V_1$ menyatakan banyaknya mobil (hasil membilang/menghitung), sehingga bernilai cacah $\{0, 1, 2, \dots\}$ (diskret).
- $V_2$ menyatakan jarak tempuh (hasil pengukuran fisik kontinu), sehingga nilainya berupa bilangan real dalam interval tertentu (kontinu).
- $V_3$ menyatakan banyaknya lemparan sampai sukses pertama, bernilai $\{1, 2, 3, \dots\}$. Ruang sampelnya tak berhingga namun dapat dihitung satu per satu (*countable infinite*), sehingga $V_3$ adalah variabel acak diskret.

Jadi, $V_1$ dan $V_3$ adalah variabel acak diskret, sedangkan $V_2$ adalah variabel kontinu.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-b-medium-bt01-010
*variasi (konteks) | C3 | 2 langkah | jenis: peluang variabel acak koin tidak seimbang*

Sekeping koin tidak seimbang memiliki peluang muncul sisi Angka sebesar $\frac{2}{3}$ dan sisi Gambar sebesar $\frac{1}{3}$. Koin tersebut dilempar sebanyak dua kali secara independen. Jika variabel acak $X$ menyatakan banyaknya sisi Angka yang muncul, berapakah nilai peluang $P(X \ge 1)$?

- A. $\frac{4}{9}$  
  <sub>Salah: Hanya menghitung peluang tepat satu sisi Angka muncul tanpa menyertakan peluang kedua lemparan menghasilkan Angka.</sub>
- B. $\frac{7}{9}$  
  <sub>Salah: Salah mengalikan kombinasi lemparan atau salah saat mengurangkan dari 1.</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: Mengira peluang muncul minimal satu Angka sama dengan peluang muncul Angka pada satu kali lemparan.</sub>
- **D. $\frac{8}{9}$** ✅  
  <sub>Benar: Kejadian komplemen dari $X \ge 1$ adalah $X = 0$ (keduanya Gambar). Peluang $P(X = 0) = P(GG) = \frac{1}{3} \times \frac{1}{3} = \frac{1}{9}$. Maka $P(X \ge 1) = 1 - \frac{1}{9} = \frac{8}{9}$.</sub>

**Pembahasan:** Ruang sampel pelemparan koin dua kali adalah $\{GG, GA, AG, AA\}$. Nilai variabel acak $X$ menyatakan banyak Angka: $X \in \{0, 1, 2\}$. Peluang tidak muncul sisi Angka sama sekali ($X = 0$) adalah $P(X = 0) = P(G) \times P(G) = \frac{1}{3} \times \frac{1}{3} = \frac{1}{9}$. Peluang muncul sekurang-kurangnya satu sisi Angka adalah $P(X \ge 1) = 1 - P(X = 0) = 1 - \frac{1}{9} = \frac{8}{9}$.
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-b-medium-bt01-011
*variasi (konteks) | C3 | 3 langkah | jenis: penjumlahan dua variabel acak independen*

Sebuah eksperimen melibatkan pengambilan satu kartu dari Kantong I dan satu kartu dari Kantong II secara acak dan independen. Variabel acak $X$ menyatakan nomor kartu terpilih dari Kantong I dengan distribusi $P(X = 1) = \frac{1}{4}$ dan $P(X = 3) = \frac{3}{4}$. Variabel acak $Y$ menyatakan nomor kartu terpilih dari Kantong II dengan distribusi $P(Y = 2) = \frac{1}{2}$ dan $P(Y = 4) = \frac{1}{2}$. Jika didefinisikan variabel acak $Z = X + Y$, berapakah nilai dari $P(Z = 5)$?

- A. $\frac{3}{16}$  
  <sub>Salah: Mengalikan peluang kedua pasangan alih-alih menjumlahkannya.</sub>
- **B. $\frac{1}{2}$** ✅  
  <sub>Benar: Nilai $Z = 5$ diperoleh dari pasangan $(X=1, Y=4)$ dan $(X=3, Y=2)$. Peluangnya adalah $(\frac{1}{4} \times \frac{1}{2}) + (\frac{3}{4} \times \frac{1}{2}) = \frac{1}{8} + \frac{3}{8} = \frac{4}{8} = \frac{1}{2}$.</sub>
- C. $\frac{1}{8}$  
  <sub>Salah: Hanya menghitung peluang pasangan $(1, 4)$ dan mengabaikan pasangan $(3, 2)$.</sub>
- D. $\frac{3}{8}$  
  <sub>Salah: Hanya menghitung peluang pasangan $(3, 2)$ dan mengabaikan pasangan $(1, 4)$.</sub>

**Pembahasan:** Variabel $Z = X + Y$ bernilai 5 jika terjadi salah satu dari dua kejadian saling lepas berikut:
1) $X = 1$ dan $Y = 4$, dengan peluang $P(X = 1, Y = 4) = \frac{1}{4} \times \frac{1}{2} = \frac{1}{8}$.
2) $X = 3$ dan $Y = 2$, dengan peluang $P(X = 3, Y = 2) = \frac{3}{4} \times \frac{1}{2} = \frac{3}{8}$.
Karena kedua kejadian saling lepas, $P(Z = 5) = \frac{1}{8} + \frac{3}{8} = \frac{4}{8} = \frac{1}{2}$.
**Acuan:** siswa — siswa hal.248 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-b-medium-bt01-012
*variasi (konteks) | C3 | 3 langkah | jenis: selisih mutlak dua variabel acak*

Dua pemutar angka diputar secara bersamaan. Pemutar I menghasilkan variabel acak $X \in \{5, 8\}$ dengan peluang $P(X = 5) = 0{,}6$ dan $P(X = 8) = 0{,}4$. Pemutar II menghasilkan variabel acak $Y \in \{2, 5\}$ dengan peluang $P(Y = 2) = 0{,}5$ dan $P(Y = 5) = 0{,}5$. Kedua pemutar bekerja secara independen. Jika dibentuk variabel acak baru $W = |X - Y|$, nilai peluang $P(W = 3)$ adalah ....

- A. $0{,}20$  
  <sub>Salah: Hanya memperhitungkan pasangan $(8, 5)$.</sub>
- B. $0{,}30$  
  <sub>Salah: Hanya menghitung salah satu kombinasi pasangan $(5, 2)$ dan lupa menambahkan pasangan $(8, 5)$.</sub>
- C. $0{,}60$  
  <sub>Salah: Salah melakukan operasi penjumlahan peluang desimal.</sub>
- **D. $0{,}50$** ✅  
  <sub>Benar: Nilai $|X - Y| = 3$ dipenuhi oleh pasangan $(5, 2)$ dengan peluang $0{,}6 \times 0{,}5 = 0{,}30$ dan pasangan $(8, 5)$ dengan peluang $0{,}4 \times 0{,}5 = 0{,}20$. Total peluangnya $0{,}30 + 0{,}20 = 0{,}50$.</sub>

**Pembahasan:** Nilai dari $W = |X - Y|$ yang menghasilkan $W = 3$ dicapai ketika:
- $X = 5$ dan $Y = 2$, sehingga $|5 - 2| = 3$. Peluangnya adalah $P(X=5) \times P(Y=2) = 0{,}6 \times 0{,}5 = 0{,}30$.
- $X = 8$ dan $Y = 5$, sehingga $|8 - 5| = 3$. Peluangnya adalah $P(X=8) \times P(Y=5) = 0{,}4 \times 0{,}5 = 0{,}20$.
Pasangan lainnya yaitu $(5, 5)$ menghasilkan $W = 0$, dan $(8, 2)$ menghasilkan $W = 6$.
Jadi, $P(W = 3) = 0{,}30 + 0{,}20 = 0{,}50$.
**Acuan:** siswa — siswa hal.251 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-b-medium-bt01-013
*variasi (konteks) | C3 | 3 langkah | jenis: banyak nilai variabel acak perkalian*

Sebuah kotak memuat lima kartu yang masing-masing bernomor 1, 2, 3, 4, dan 5. Dari kotak tersebut diambil dua keping kartu sekaligus secara acak. Misalkan variabel acak $M$ menyatakan hasil kali dari dua nomor kartu yang terambil. Banyaknya anggota dari himpunan semua nilai yang mungkin dari variabel acak $M$ adalah ....

- **A. 10** ✅  
  <sub>Benar: Ada $\binom{5}{2} = 10$ pasangan kartu yang mungkin diambil, dan kesepuluh pasangan tersebut menghasilkan nilai perkalian yang berbeda satu sama lain.</sub>
- B. 5  
  <sub>Salah: Mengira nilai variabel acak sebanyak jumlah kartu yang ada di kotak.</sub>
- C. 8  
  <sub>Salah: Mengira ada nilai perkalian yang kembar pada pasangan kartu tersebut.</sub>
- D. 9  
  <sub>Salah: Salah menganggap ada satu pasangan perkalian yang bernilai sama.</sub>

**Pembahasan:** Dua kartu diambil sekaligus dari 5 kartu bernomor $\{1, 2, 3, 4, 5\}$. Banyak pasangan titik sampel adalah $\binom{5}{2} = 10$ pasang, yaitu:
1. $\{1, 2\} \to 1 \times 2 = 2$
2. $\{1, 3\} \to 1 \times 3 = 3$
3. $\{1, 4\} \to 1 \times 4 = 4$
4. $\{1, 5\} \to 1 \times 5 = 5$
5. $\{2, 3\} \to 2 \times 3 = 6$
6. $\{2, 4\} \to 2 \times 4 = 8$
7. $\{2, 5\} \to 2 \times 5 = 10$
8. $\{3, 4\} \to 3 \times 4 = 12$
9. $\{3, 5\} \to 3 \times 5 = 15$
10. $\{4, 5\} \to 4 \times 5 = 20$
Semua hasil kali tersebut bernilai unik: $\{2, 3, 4, 5, 6, 8, 10, 12, 15, 20\}$. Dengan demikian, banyaknya nilai yang mungkin dari variabel acak $M$ adalah 10.
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-b-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: distribusi peluang fungsi kuadratik*

Sebuah variabel acak diskret $Y$ memiliki daerah nilai $\{1, 2, 3, 4\}$. Fungsi peluang dari $Y$ didefinisikan oleh:
$$P(Y = y) = \frac{y^2 + 1}{c}$$
untuk setiap $y \in \{1, 2, 3, 4\}$ dengan $c$ merupakan konstanta real positif. Nilai dari $P(Y \le 2)$ adalah ....

- **A. $\frac{7}{34}$** ✅  
  <sub>Benar: Jumlah seluruh peluang harus sama dengan 1, sehingga $\sum_{y=1}^4 (y^2 + 1) = 2 + 5 + 10 + 17 = 34$, menghasilkan $c = 34$. Maka $P(Y \le 2) = P(Y=1) + P(Y=2) = \frac{2}{34} + \frac{5}{34} = \frac{7}{34}$.</sub>
- B. $\frac{7}{30}$  
  <sub>Salah: Salah menghitung nilai konstanta $c$ karena hanya menjumlahkan $y^2$ tanpa menambahkan suku $+1$ untuk setiap titik.</sub>
- C. $\frac{5}{34}$  
  <sub>Salah: Hanya menghitung nilai $P(Y = 2)$ tanpa menyertakan $P(Y = 1)$.</sub>
- D. $\frac{2}{17}$  
  <sub>Salah: Hanya mengambil nilai $P(Y = 1) = \frac{2}{34}$ lalu disederhanakan menjadi $\frac{1}{17}$ atau salah mengalikan.</sub>

**Pembahasan:** Berdasarkan syarat fungsi peluang variabel acak diskret, jumlah total peluang seluruh nilai yang mungkin harus sama dengan 1:
$$\sum_{y=1}^{4} P(Y = y) = 1$$
$$\frac{1^2 + 1}{c} + \frac{2^2 + 1}{c} + \frac{3^2 + 1}{c} + \frac{4^2 + 1}{c} = 1$$
$$\frac{2 + 5 + 10 + 17}{c} = 1 \implies \frac{34}{c} = 1 \implies c = 34$$
Selanjutnya, nilai $P(Y \le 2)$ dihitung dengan menjumlahkan peluang untuk $y = 1$ dan $y = 2$:
$$P(Y \le 2) = P(Y = 1) + P(Y = 2) = \frac{2}{34} + \frac{5}{34} = \frac{7}{34}$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-b-medium-bt01-015
*variasi (konteks) | C4 | 2 langkah | jenis: klasifikasi jenis variabel acak*

Perhatikan empat besaran hasil pengamatan di sebuah rumah sakit berikut:
1. Kadar kolesterol dalam darah pasien.
2. Banyaknya pasien yang berkunjung ke instalasi rawat jalan setiap hari.
3. Suhu tubuh pasien yang dirawat di ruang isolasi.
4. Banyaknya botol infus yang terpakai di ruang rawat inap dalam seminggu.

Berdasarkan data di atas, besaran yang tergolong sebagai variabel acak diskret adalah ....

- A. 1 dan 2  
  <sub>Salah: Tertukar antara variabel kontinu (kadar kolesterol) dan diskret.</sub>
- **B. 2 dan 4** ✅  
  <sub>Benar: Besaran 2 dan 4 diperoleh dari hasil menghitung/membilang dan bernilai bilangan bulat non-negatif sehingga nilainya dapat dihitung satu per satu (diskret).</sub>
- C. 3 dan 4  
  <sub>Salah: Tertukar antara variabel kontinu (suhu tubuh) dan diskret.</sub>
- D. 1 dan 3  
  <sub>Salah: Memilih variabel kontinu yang diperoleh dari hasil pengukuran instrumen.</sub>

**Pembahasan:** Variabel acak diskret memiliki nilai yang diperoleh melalui proses menghitung atau membilang (*countable*), berupa bilangan bulat non-negatif.
- (1) Kadar kolesterol: hasil pengukuran pada skala kontinu (variabel acak kontinu).
- (2) Banyaknya pasien: hasil menghitung bilangan bulat (variabel acak diskret).
- (3) Suhu tubuh: hasil pengukuran alat ukur termometer (variabel acak kontinu).
- (4) Banyaknya botol infus: hasil membilang satuan barang (variabel acak diskret).

Jadi, yang tergolong variabel acak diskret adalah nomor 2 dan 4.
**Acuan:** pretest — kelas12_tl-b04-p0252-latihan-soal-variabel-acak-diskret-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-b-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: distribusi peluang fungsi kuadratik berbobot*

Suatu variabel acak diskret $Y$ memiliki daerah nilai $\{0, 1, 2, 3\}$. Distribusi peluang dari $Y$ dirumuskan dengan $P(Y = y) = c(y + 1)^2$, di mana $c$ adalah sebuah konstanta. Nilai dari $P(Y \ge 2)$ adalah ....

- A. $\frac{3}{10}$  
  <sub>Salah: Hanya menghitung nilai untuk $P(Y = 2) = \frac{9}{30} = \frac{3}{10}$.</sub>
- **B. $\frac{5}{6}$** ✅  
  <sub>Benar: Total peluang $\sum_{y=0}^3 c(y+1)^2 = c(1 + 4 + 9 + 16) = 30c = 1 \implies c = \frac{1}{30}$. Maka $P(Y \ge 2) = P(Y = 2) + P(Y = 3) = \frac{9}{30} + \frac{16}{30} = \frac{25}{30} = \frac{5}{6}$.</sub>
- C. $\frac{8}{15}$  
  <sub>Salah: Hanya menghitung nilai untuk $P(Y = 3) = \frac{16}{30} = \frac{8}{15}$.</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: Menghitung komplemennya yaitu $P(Y < 2) = \frac{1+4}{30} = \frac{5}{30} = \frac{1}{6}$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $c$ menggunakan sifat bahwa jumlah seluruh nilai peluang variabel acak diskret harus sama dengan 1.
$$\sum_{y=0}^{3} P(Y = y) = 1$$
$$c(0 + 1)^2 + c(1 + 1)^2 + c(2 + 1)^2 + c(3 + 1)^2 = 1$$
$$c(1 + 4 + 9 + 16) = 1$$
$$30c = 1 \implies c = \frac{1}{30}$$

Langkah 2: Menghitung nilai $P(Y \ge 2)$:
$$P(Y \ge 2) = P(Y = 2) + P(Y = 3)$$
$$P(Y \ge 2) = \frac{(2 + 1)^2}{30} + \frac{(3 + 1)^2}{30} = \frac{9}{30} + \frac{16}{30} = \frac{25}{30} = \frac{5}{6}$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-b-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: perkalian dua variabel acak diskret*

Kotak I berisi dua kartu bertuliskan angka 2 dan 5, dengan peluang terambil berturut-turut adalah $P(X = 2) = \frac{2}{3}$ dan $P(X = 5) = \frac{1}{3}$. Kotak II berisi dua kartu bertuliskan angka 1 dan 3, dengan peluang terambil berturut-turut adalah $P(Y = 1) = \frac{1}{4}$ dan $P(Y = 3) = \frac{3}{4}$. Satu kartu diambil secara acak dan independen dari masing-masing kotak. Jika variabel acak $W = X \cdot Y$ menyatakan hasil kali angka kedua kartu, maka nilai peluang $P(W < 6)$ adalah ....

- **A. $\frac{1}{4}$** ✅  
  <sub>Benar: Pasangan $(X, Y)$ yang menghasilkan $W < 6$ adalah $(2, 1)$ dengan hasil $2$ (peluang $\frac{2}{3} \cdot \frac{1}{4} = \frac{2}{12}$) dan $(5, 1)$ dengan hasil $5$ (peluang $\frac{1}{3} \cdot \frac{1}{4} = \frac{1}{12}$). Jumlah peluangnya adalah $\frac{2}{12} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4}$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Mengabaikan bobot peluang dan menganggap setiap pasangan dari empat kombinasi memiliki peluang yang sama besar (2/4).</sub>
- C. $\frac{1}{6}$  
  <sub>Salah: Hanya menghitung peluang pasangan $(2, 1)$ yaitu $\frac{2}{12} = \frac{1}{6}$.</sub>
- D. $\frac{3}{4}$  
  <sub>Salah: Menghitung komplemen yaitu $P(W \ge 6)$.</sub>

**Pembahasan:** Tentukan setiap kemungkinan hasil perkalian $W = X \cdot Y$ beserta peluangnya:
1. $(X=2, Y=1) \implies W = 2$, peluang $= \frac{2}{3} \times \frac{1}{4} = \frac{2}{12}$
2. $(X=2, Y=3) \implies W = 6$, peluang $= \frac{2}{3} \times \frac{3}{4} = \frac{6}{12}$
3. $(X=5, Y=1) \implies W = 5$, peluang $= \frac{1}{3} \times \frac{1}{4} = \frac{1}{12}$
4. $(X=5, Y=3) \implies W = 15$, peluang $= \frac{1}{3} \times \frac{3}{4} = \frac{3}{12}$

Nilai $W < 6$ terpenuhi saat $W = 2$ dan $W = 5$.
$$P(W < 6) = P(W = 2) + P(W = 5) = \frac{2}{12} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4}$$
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-b-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: distribusi peluang pengambilan tanpa pengembalian*

Sebuah kotak berisi 3 bola merah dan 3 bola biru. Dari kotak tersebut diambil 2 bola satu per satu secara acak tanpa pengembalian. Jika variabel acak $M$ menyatakan banyaknya bola merah yang terambil, maka nilai peluang $P(M \le 1)$ adalah ....

- A. $\frac{3}{4}$  
  <sub>Salah: Keliru menggunakan perhitungan dengan pengembalian.</sub>
- B. $\frac{3}{5}$  
  <sub>Salah: Hanya menghitung nilai untuk $P(M = 1)$.</sub>
- C. $\frac{1}{5}$  
  <sub>Salah: Hanya menghitung nilai untuk $P(M = 0)$ atau komplemen $P(M = 2)$.</sub>
- **D. $\frac{4}{5}$** ✅  
  <sub>Benar: $P(M = 0) = \frac{3}{6} \cdot \frac{2}{5} = \frac{6}{30}$, $P(M = 1) = 2 \cdot \left(\frac{3}{6} \cdot \frac{3}{5}\right) = \frac{18}{30}$. Maka $P(M \le 1) = \frac{6}{30} + \frac{18}{30} = \frac{24}{30} = \frac{4}{5}$.</sub>

**Pembahasan:** Total bola dalam kotak $= 3 + 3 = 6$ bola.
Variabel acak $M$ menyatakan banyaknya bola merah yang terambil dari 2 kali pengambilan tanpa pengembalian, dengan daerah nilai $M \in \{0, 1, 2\}$.

1. Peluang terambil 0 bola merah (keduanya biru):
$$P(M = 0) = \frac{3}{6} \times \frac{2}{5} = \frac{6}{30}$$

2. Peluang terambil 1 bola merah (merah lalu biru, atau biru lalu merah):
$$P(M = 1) = \left(\frac{3}{6} \times \frac{3}{5}\right) + \left(\frac{3}{6} \times \frac{3}{5}\right) = \frac{9}{30} + \frac{9}{30} = \frac{18}{30}$$

Dengan demikian, nilai peluang kumulatif $P(M \le 1)$ adalah:
$$P(M \le 1) = P(M = 0) + P(M = 1) = \frac{6}{30} + \frac{18}{30} = \frac{24}{30} = \frac{4}{5}$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-b-medium-bt01-019
*variasi (konteks) | C4 | 2 langkah | jenis: analisis pengelompokan variabel acak*

Perhatikan variabel-variabel acak yang diamati pada suatu laboratorium sains berikut:
(1) $P$: Jumlah tetesan reagen yang dibutuhkan hingga larutan berubah warna.
(2) $Q$: Waktu yang dibutuhkan (dalam detik) hingga reaksi kimia selesai.
(3) $R$: Suhu campuran reaksi (dalam derajat Celsius) setiap 5 menit.
(4) $S$: Banyaknya tabung reaksi yang retak selama proses pemanasan.

Berdasarkan stimulus di atas, pasangan variabel acak yang keduanya tergolong variabel acak diskret adalah ....

- A. $P$ dan $Q$  
  <sub>Salah: Mengira waktu reaksi merupakan variabel acak diskret karena diukur dalam satuan detik.</sub>
- B. $Q$ dan $R$  
  <sub>Salah: Memilih variabel kontinu alih-alih variabel acak diskret.</sub>
- **C. $P$ dan $S$** ✅  
  <sub>Benar: $P$ (jumlah tetesan) dan $S$ (banyaknya tabung retak) nilainya diperoleh dari hasil membilang/menghitung satu per satu (bilangan bulat cacah), sedangkan $Q$ (waktu) dan $R$ (suhu) merupakan hasil pengukuran pada skala kontinu.</sub>
- D. $R$ dan $S$  
  <sub>Salah: Menganggap suhu diskret karena dicatat pada interval waktu tertentu.</sub>

**Pembahasan:** Variabel acak diskret adalah variabel yang ruang sampel nilainya diperoleh dari hasil membilang atau menghitung, dan nilainya berupa bilangan bulat terpisah (countable).

Analisis setiap variabel:
- (1) $P$ (jumlah tetesan reagen): diperoleh dari membilang ($0, 1, 2, \dots$), merupakan variabel acak diskret.
- (2) $Q$ (waktu reaksi): diperoleh dari pengukuran kontinu pada selang waktu real, merupakan variabel acak kontinu.
- (3) $R$ (suhu campuran): diperoleh dari pengukuran instrumen termometer pada skala kontinu, merupakan variabel acak kontinu.
- (4) $S$ (banyak tabung reaksi retak): diperoleh dari membilang ($0, 1, 2, \dots$), merupakan variabel acak diskret.

Dengan demikian, pasangan yang keduanya merupakan variabel acak diskret adalah $P$ dan $S$.
**Acuan:** pretest — kelas12_tl-b04-p0252-latihan-soal-variabel-acak-diskret-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-b-medium-bt01-020
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi peluang variabel acak Bernoulli independen*

Dalam suatu uji kendali mutu, seorang teknisi memeriksa 3 unit komponen elektronik secara independen. Setiap komponen memiliki peluang yang sama untuk lolos atau gagal uji, yaitu masing-masing bernilai $\frac{1}{2}$. Jika variabel acak $Y$ menyatakan banyaknya komponen yang lolos uji mutu, nilai dari peluang $P(Y \ge 2)$ adalah ....

- A. $\frac{3}{8}$  
  <sub>Salah: Hanya menghitung peluang tepat dua komponen lolos uji P(Y = 2) dan melupakan kondisi Y = 3.</sub>
- **B. $\frac{1}{2}$** ✅  
  <sub>Benar: Ruang sampel pemeriksaan 3 komponen memiliki $n(S) = 2^3 = 8$ titik sampel berpeluang sama. Nilai $Y \ge 2$ mencakup kejadian $Y = 2$ (3 titik: LLG, LGL, GLL) dan $Y = 3$ (1 titik: LLL). Jadi, $P(Y \ge 2) = \frac{3 + 1}{8} = \frac{4}{8} = \frac{1}{2}$.</sub>
- C. $\frac{7}{8}$  
  <sub>Salah: Keliru mengartikan kondisi sekurang-kurangnya dua menjadi sekurang-kurangnya satu komponen lolos P(Y >= 1).</sub>
- D. $\frac{1}{8}$  
  <sub>Salah: Hanya menghitung peluang seluruh komponen lolos uji P(Y = 3).</sub>

**Pembahasan:** Pemeriksaan 3 komponen elektronik menghasilkan ruang sampel beranggotakan $2^3 = 8$ hasil yang sama mungkin, yaitu:
$$S = \{\text{LLL, LLG, LGL, LGG, GLL, GLG, GGL, GGG}\}$$
Variabel acak $Y$ menyatakan banyaknya komponen yang lolos (L).
Kejadian $Y \ge 2$ berarti terdapat 2 atau 3 komponen yang lolos:
- $Y = 2$: $\{\text{LLG, LGL, GLL}\}$ sebanyak 3 kejadian.
- $Y = 3$: $\{\text{LLL}\}$ sebanyak 1 kejadian.

Banyak kejadian yang memenuhi adalah $3 + 1 = 4$.
Dengan demikian, nilai peluangnya adalah:
$$P(Y \ge 2) = \frac{4}{8} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-b-hard-bt01-001
*orisinal | C6 | 4 langkah | jenis: perancangan distribusi peluang variabel acak*

Sebuah variabel acak diskret $K$ menyatakan banyaknya kemunculan suatu peristiwa khusus dengan ruang nilai $\{0, 1, 2, 3\}$. Diberikan model fungsi distribusi peluang:
$$P(K = k) = \frac{m \cdot 2^k}{45}$$
untuk $k \in \{0, 1, 2, 3\}$, dengan $m$ adalah suatu konstanta bilangan bulat positif.

Agar fungsi tersebut valid sebagai fungsi peluang dari variabel acak diskret $K$, nilai dari $P(K \ge 2)$ harus bernilai ....

- A. $\frac{2}{3}$  
  <sub>Salah: Siswa lupa mengalikan dengan konstanta $m = 3$ dan langsung menghitung proporsi $\frac{2^2 + 2^3}{18}$ secara keliru.</sub>
- **B. $\frac{4}{5}$** ✅  
  <sub>Benar: Syarat fungsi peluang diskret: $\sum_{k=0}^3 P(K=k) = 1$.
$\sum_{k=0}^3 \frac{m \cdot 2^k}{45} = \frac{m}{45}(2^0 + 2^1 + 2^2 + 2^3) = \frac{m}{45}(1 + 2 + 4 + 8) = \frac{15m}{45} = \frac{m}{3}$.
Agar total peluang sama dengan 1, maka $\frac{m}{3} = 1 \Rightarrow m = 3$.
Kemudian dihitung $P(K \ge 2) = P(K = 2) + P(K = 3) = \frac{3(4 + 8)}{45} = \frac{3 \times 12}{45} = \frac{36}{45} = \frac{4}{5}$.</sub>
- C. $\frac{8}{15}$  
  <sub>Salah: Siswa hanya menghitung nilai pada $K = 3$, yaitu $\frac{3 \times 8}{45} = \frac{24}{45} = \frac{8}{15}$.</sub>
- D. $\frac{1}{5}$  
  <sub>Salah: Siswa menghitung peluang komplemen $P(K < 2) = P(K = 0) + P(K = 1) = \frac{3(1 + 2)}{45} = \frac{9}{45} = \frac{1}{5}$ bukannya $P(K \ge 2)$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $m$ menggunakan syarat total peluang $\sum_{k=0}^3 P(K = k) = 1$.
$$\frac{m}{45} (2^0 + 2^1 + 2^2 + 2^3) = 1$$
$$\frac{m}{45} (1 + 2 + 4 + 8) = 1$$
$$\frac{15m}{45} = 1 \implies \frac{m}{3} = 1 \implies m = 3$$

Langkah 2: Menghitung peluang $P(K \ge 2)$:
$$P(K \ge 2) = P(K = 2) + P(K = 3)$$
$$P(K = 2) = \frac{3 \cdot 2^2}{45} = \frac{12}{45}$$
$$P(K = 3) = \frac{3 \cdot 2^3}{45} = \frac{24}{45}$$
$$P(K \ge 2) = \frac{12}{45} + \frac{24}{45} = \frac{36}{45} = \frac{4}{5}$$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-b-hard-bt01-002
*orisinal | C6 | 4 langkah | jenis: perancangan aturan variabel acak diskret*

Sebuah kantong berisi 4 bola merah dan $k$ bola hitam dengan $k \ge 2$. Dari dalam kantong diambil 2 bola sekaligus secara acak. Misalkan variabel acak diskret $X$ menyatakan banyaknya bola merah yang terambil. Agar peluang terambilnya tepat 1 bola merah bernilai tepat 2 kali lipat dari peluang tidak ada bola merah yang terambil sama sekali, nilai $k$ yang harus dipilih adalah ....

- A. 6  
  <sub>Salah: Siswa melakukan kesalahan tanda aljabar saat memindahkan konstanta dari $k - 1 = 4$ menjadi $k = 6$.</sub>
- B. 4  
  <sub>Salah: Siswa mengasumsikan jumlah bola hitam harus sama dengan bola merah agar kondisinya simetris.</sub>
- C. 3  
  <sub>Salah: Siswa lupa membagi dengan 2 pada kombinasi $\binom{k}{2}$, menghasilkan persamaan $4k = 2(k(k-1)) \implies 2 = k - 1 \implies k = 3$.</sub>
- **D. 5** ✅  
  <sub>Benar: Banyaknya ruang sampel pengambilan 2 bola dari $(4 + k)$ bola adalah $\binom{4+k}{2}$.
- Kejadian $X = 0$ (keduanya hitam): banyaknya cara $\binom{k}{2} = \frac{k(k-1)}{2}$.
- Kejadian $X = 1$ (1 merah dan 1 hitam): banyaknya cara $\binom{4}{1}\binom{k}{1} = 4k$.
Syarat yang dirancang adalah $P(X = 1) = 2 \cdot P(X = 0)$.
Karena penyebut kedua peluang sama, maka:
$\binom{4}{1}\binom{k}{1} = 2 \cdot \binom{k}{2}$
$4k = 2 \cdot \frac{k(k-1)}{2}$
$4k = k(k-1)$
Karena $k \ge 2$ ($k \ne 0$), bagi kedua ruas dengan $k$:
$4 = k - 1 \implies k = 5$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai-nilai variabel acak $X$ dan rumus peluangnya.
Pengambilan 2 bola dari total $(4 + k)$ bola memiliki ruang sampel $n(S) = \binom{4+k}{2}$.

Langkah 2: Menentukan ekspresi peluang untuk $X = 0$ dan $X = 1$:
- $P(X = 0) = \frac{\binom{4}{0}\binom{k}{2}}{\binom{4+k}{2}} = \frac{\frac{k(k-1)}{2}}{\binom{4+k}{2}}$
- $P(X = 1) = \frac{\binom{4}{1}\binom{k}{1}}{\binom{4+k}{2}} = \frac{4k}{\binom{4+k}{2}}$

Langkah 3: Menyusun persamaan sesuai ketentuan perancangan $P(X = 1) = 2 \cdot P(X = 0)$:
$$\frac{4k}{\binom{4+k}{2}} = 2 \cdot \frac{\frac{k(k-1)}{2}}{\binom{4+k}{2}}$$
$$4k = k(k-1)$$

Langkah 4: Menyelesaikan persamaan aljabar untuk nilai $k$:
Karena $k \ge 2$, kedua ruas dapat dibagi dengan $k$:
$$4 = k - 1 \implies k = 5$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-b-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: evaluasi batas validitas fungsi peluang*

Sebuah variabel acak diskret $T$ memiliki ruang nilai $\{0, 1, 2, 3\}$ dengan model distribusi peluang dinyatakan sebagai berikut:
$$\begin{aligned}
P(T = 0) &= \frac{1}{2} - k \\
P(T = 1) &= 2k \\
P(T = 2) &= \frac{1}{4} + k \\
P(T = 3) &= \frac{1}{4} - 2k
\end{aligned}$$
Batas-batas nilai real $k$ yang mungkin agar fungsi tersebut merupakan distribusi peluang variabel acak diskret yang sah adalah ....

- **A. $0 \le k \le \frac{1}{8}$** ✅  
  <sub>Benar: Jumlah seluruh peluang harus sama dengan 1:
$\sum P(T = t) = \left(\frac{1}{2} - k\right) + 2k + \left(\frac{1}{4} + k\right) + \left(\frac{1}{4} - 2k\right) = 1$.
Persamaan ini bernilai benar untuk setiap $k$ (identitas).
Syarat aksiomatis probabilitas mengharuskan $0 \le P(T = t) \le 1$ untuk setiap $t$:
1. $P(T = 0) \ge 0 \implies \frac{1}{2} - k \ge 0 \implies k \le \frac{1}{2}$
2. $P(T = 1) \ge 0 \implies 2k \ge 0 \implies k \ge 0$
3. $P(T = 2) \ge 0 \implies \frac{1}{4} + k \ge 0 \implies k \ge -\frac{1}{4}$
4. $P(T = 3) \ge 0 \implies \frac{1}{4} - 2k \ge 0 \implies k \le \frac{1}{8}$
Irisan dari seluruh pertidaksamaan tersebut adalah $0 \le k \le \frac{1}{8}$.</sub>
- B. $0 \le k \le \frac{1}{4}$  
  <sub>Salah: Siswa keliru menyelesaikan pertidaksamaan $\frac{1}{4} - 2k \ge 0$ menjadi $k \le \frac{1}{4}$ karena lupa membagi koefisien 2.</sub>
- C. $0 \le k \le \frac{1}{2}$  
  <sub>Salah: Siswa hanya menguji syarat pada $P(T = 0)$ dan $P(T = 1)$, mengabaikan pembatasan yang lebih ketat dari $P(T = 3)$.</sub>
- D. $-\frac{1}{4} \le k \le \frac{1}{8}$  
  <sub>Salah: Siswa mengambil batas bawah dari syarat $P(T = 2) \ge 0$ dan melupakan syarat non-negativitas dari $P(T = 1) = 2k \ge 0$.</sub>

**Pembahasan:** Langkah 1: Memeriksa syarat normalisasi peluang $\sum_{t=0}^{3} P(T = t) = 1$:
$$\left(\frac{1}{2} - k\right) + 2k + \left(\frac{1}{4} + k\right) + \left(\frac{1}{4} - 2k\right) = \frac{1}{2} + \frac{1}{4} + \frac{1}{4} + (-k + 2k + k - 2k) = 1$$
Karena hasilnya selalu 1, syarat normalisasi terpenuhi untuk setiap nilai real $k$.

Langkah 2: Menetapkan syarat bahwa setiap nilai peluang harus non-negatif ($P(T = t) \ge 0$):
- $P(T = 0) \ge 0 \implies \frac{1}{2} - k \ge 0 \implies k \le \frac{1}{2}$
- $P(T = 1) \ge 0 \implies 2k \ge 0 \implies k \ge 0$
- $P(T = 2) \ge 0 \implies \frac{1}{4} + k \ge 0 \implies k \ge -\frac{1}{4}$
- $P(T = 3) \ge 0 \implies \frac{1}{4} - 2k \ge 0 \implies 2k \le \frac{1}{4} \implies k \le \frac{1}{8}$

Langkah 3: Menentukan batas bawah nilai $k$ dari irisan pertidaksamaan:
$$k \ge 0 \quad \text{dan} \quad k \ge -\frac{1}{4} \implies k \ge 0$$

Langkah 4: Menentukan batas atas nilai $k$ dari irisan pertidaksamaan:
$$k \le \frac{1}{2} \quad \text{dan} \quad k \le \frac{1}{8} \implies k \le \frac{1}{8}$$
Dengan demikian, batas-batas nilai $k$ yang sah adalah $0 \le k \le \frac{1}{8}$.
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-b-hard-bt01-004
*variasi (konteks) | C5 | 5 langkah | jenis: evaluasi rentang nilai variabel acak*

Dari sebuah kotak yang berisi 5 kartu bernomor 1, 2, 3, 4, dan 5 diambil dua kartu sekaligus secara acak. Variabel acak diskret $U$ didefinisikan sebagai hasil kali nomor kedua kartu yang terambil. Banyaknya kemungkinan nilai $u$ dari variabel acak $U$ yang memenuhi pertidaksamaan $u^2 - 15u + 50 \le 0$ adalah ....

- **A. 4** ✅  
  <sub>Benar: Kombinasi 2 kartu dari 5 kartu menghasilkan $\binom{5}{2} = 10$ kemungkinan pasangan. Hasil kalinya adalah: $1\times2=2$, $1\times3=3$, $1\times4=4$, $1\times5=5$, $2\times3=6$, $2\times4=8$, $2\times5=10$, $3\times4=12$, $3\times5=15$, $4\times5=20$. Himpunan nilai yang mungkin dari variabel acak $U$ adalah $\{2, 3, 4, 5, 6, 8, 10, 12, 15, 20\}$ (ada 10 nilai berbeda). Syarat: $u^2 - 15u + 50 \le 0 \iff (u - 5)(u - 10) \le 0 \iff 5 \le u \le 10$. Nilai $u$ yang memenuhi interval $[5, 10]$ adalah $5, 6, 8, 10$. Jadi terdapat tepat 4 nilai.</sub>
- B. 3  
  <sub>Salah: Siswa menggunakan pertidaksamaan ketat $5 < u < 10$ sehingga nilai 5 dan 10 tidak dihitung atau salah mengabaikan salah satu nilai.</sub>
- C. 6  
  <sub>Salah: Siswa menghitung banyaknya pasangan kartu yang menghasilkan rentang tersebut, bukan banyaknya kemungkinan nilai diskret dari $U$.</sub>
- D. 5  
  <sub>Salah: Siswa mengira semua bilangan bulat antara 5 sampai 10 (5, 6, 7, 8, 9, 10) adalah nilai dari $U$, padahal 7 dan 9 bukan nilai yang mungkin.</sub>

**Pembahasan:** Dua kartu diambil sekaligus dari $\{1, 2, 3, 4, 5\}$. Pasangan kartu yang mungkin beserta hasil kali $u$:\n- $(1, 2) \to 2$\n- $(1, 3) \to 3$\n- $(1, 4) \to 4$\n- $(1, 5) \to 5$\n- $(2, 3) \to 6$\n- $(2, 4) \to 8$\n- $(2, 5) \to 10$\n- $(3, 4) \to 12$\n- $(3, 5) \to 15$\n- $(4, 5) \to 20$\nRuang nilai variabel acak diskret $U$ adalah $\{2, 3, 4, 5, 6, 8, 10, 12, 15, 20\}$.\nPertidaksamaan: $u^2 - 15u + 50 \le 0 \iff (u - 5)(u - 10) \le 0 \iff 5 \le u \le 10$.\nNilai $u \in U$ yang berada dalam selang $[5, 10]$ adalah $5, 6, 8,$ dan $10$. Ada 4 nilai.
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-b-hard-bt01-005
*orisinal | C5 | 4 langkah | jenis: analisis peluang variabel acak diskret bertingkat*

Sebuah kotak berisi 3 bola merah dan 3 bola putih. Dilakukan pengambilan bola satu per satu secara acak tanpa pengembalian hingga bola merah kedua terambil. Misalkan variabel acak diskret $N$ menyatakan banyaknya pengambilan bola yang dilakukan sampai percobaan berakhir. Nilai dari $P(N \le 3)$ adalah ....

- A. $\frac{3}{5}$  
  <sub>Salah: Siswa melakukan perhitungan dengan asumsi pengambilan dengan pengembalian.</sub>
- B. $\frac{3}{10}$  
  <sub>Salah: Siswa hanya menghitung peluang $P(N = 3)$ dan melupakan kasus $N = 2$.</sub>
- C. $\frac{7}{20}$  
  <sub>Salah: Siswa lupa mengalikan dengan 2 susunan yang mungkin (hanya menghitung satu urutan MPM) pada $N = 3$.</sub>
- **D. $\frac{1}{2}$** ✅  
  <sub>Benar: Bola merah kedua dapat terambil pada pengambilan ke-2, ke-3, ke-4, atau ke-5. Jadi ruang nilai $N$ adalah $\{2, 3, 4, 5\}$. Kejadian $N \le 3$ berarti $N = 2$ atau $N = 3$.\n- $N = 2$: Pengambilan ke-1 Merah dan ke-2 Merah (MM). Peluang $= \frac{3}{6} \times \frac{2}{5} = \frac{6}{30} = \frac{1}{5}$.\n- $N = 3$: Terdiri dari susunan MPM (Merah, Putih, Merah) atau PMM (Putih, Merah, Merah). Peluang MPM $= \frac{3}{6} \times \frac{3}{5} \times \frac{2}{4} = \frac{18}{120} = \frac{3}{20}$. Peluang PMM $= \frac{3}{6} \times \frac{3}{5} \times \frac{2}{4} = \frac{3}{20}$. Total $P(N = 3) = \frac{3}{20} + \frac{3}{20} = \frac{6}{20} = \frac{3}{10}$.\nJumlahkan: $P(N \le 3) = P(N = 2) + P(N = 3) = \frac{1}{5} + \frac{3}{10} = \frac{2}{10} + \frac{3}{10} = \frac{5}{10} = \frac{1}{2}$.</sub>

**Pembahasan:** Variabel acak $N$ menyatakan banyaknya pengambilan hingga terambil bola merah kedua.\nNilai $N \le 3$ mencakup $N = 2$ dan $N = 3$.\n1. Kasus $N = 2$: Bola yang terambil harus urutan MM.\n   $P(N = 2) = \frac{3}{6} \times \frac{2}{5} = \frac{6}{30} = \frac{1}{5}$.\n2. Kasus $N = 3$: Pengambilan ke-3 harus merah, dan di antara 2 pengambilan pertama ada tepat 1 merah (MPM atau PMM).\n   $P(\text{MPM}) = \frac{3}{6} \times \frac{3}{5} \times \frac{2}{4} = \frac{18}{120} = \frac{3}{20}$.\n   $P(\text{PMM}) = \frac{3}{6} \times \frac{3}{5} \times \frac{2}{4} = \frac{18}{120} = \frac{3}{20}$.\n   $P(N = 3) = \frac{3}{20} + \frac{3}{20} = \frac{6}{20} = \frac{3}{10}$.\n3. Maka, $P(N \le 3) = P(N = 2) + P(N = 3) = \frac{2}{10} + \frac{3}{10} = \frac{5}{10} = \frac{1}{2}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-b-hard-bt01-006
*orisinal | C6 | 5 langkah | jenis: perancangan fungsi variabel acak*

Sebuah variabel acak diskret $M$ memiliki ruang sampel tak berhingga dengan daerah nilai himpunan bilangan asli $\{1, 2, 3, \dots\}$. Model fungsi peluang dari $M$ didefinisikan sebagai $P(M = m) = k \left(\frac{3}{4}\right)^m$ untuk setiap $m \in \{1, 2, 3, \dots\}$, dengan $k$ suatu konstanta real. Nilai dari peluang $P(M > 2)$ adalah ....

- A. $\frac{3}{16}$  
  <sub>Salah: Siswa hanya menghitung nilai peluang tepat pada saat $M = 2$.</sub>
- **B. $\frac{9}{16}$** ✅  
  <sub>Benar: Total peluang seluruh nilai variabel acak diskret harus sama dengan 1:\n$\sum_{m=1}^{\infty} P(M = m) = 1 \implies \sum_{m=1}^{\infty} k \left(\frac{3}{4}\right)^m = 1$.\nDeret geometri dengan suku pertama $a = k \cdot \frac{3}{4}$ dan rasio $r = \frac{3}{4}$.\nJumlah deret: $S = \frac{a}{1 - r} = \frac{\frac{3}{4}k}{1 - \frac{3}{4}} = \frac{\frac{3}{4}k}{\frac{1}{4}} = 3k = 1 \implies k = \frac{1}{3}$.\nMaka $P(M = m) = \frac{1}{3} \left(\frac{3}{4}\right)^m$.\nDitanya $P(M > 2) = 1 - P(M \le 2) = 1 - [P(M=1) + P(M=2)]$.\n$P(M = 1) = \frac{1}{3} \left(\frac{3}{4}\right) = \frac{1}{4}$.\n$P(M = 2) = \frac{1}{3} \left(\frac{9}{16}\right) = \frac{3}{16}$.\n$P(M \le 2) = \frac{1}{4} + \frac{3}{16} = \frac{7}{16}$.\n$P(M > 2) = 1 - \frac{7}{16} = \frac{9}{16}$.</sub>
- C. $\frac{7}{16}$  
  <sub>Salah: Siswa menghitung nilai komplementer $P(M \le 2)$ alih-alih $P(M > 2)$.</sub>
- D. $\frac{27}{64}$  
  <sub>Salah: Siswa keliru menganggap $P(M > 2)$ dimulai dari $m = 4$ atau salah indeks deret.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$ menggunakan syarat total peluang diskret:\n$$\sum_{m=1}^{\infty} P(M = m) = 1$$\nMerupakan deret geometri tak hingga dengan suku pertama $a = k \left(\frac{3}{4}\right)$ dan rasio $r = \frac{3}{4}$:\n$$S_{\infty} = \frac{a}{1 - r} = \frac{\frac{3}{4}k}{1 - \frac{3}{4}} = 3k = 1 \implies k = \frac{1}{3}$$\n\nLangkah 2: Menghitung $P(M \le 2)$:\n$$P(M = 1) = \frac{1}{3}\left(\frac{3}{4}\right) = \frac{1}{4}$$\n$$P(M = 2) = \frac{1}{3}\left(\frac{9}{16}\right) = \frac{3}{16}$$\n$$P(M \le 2) = \frac{1}{4} + \frac{3}{16} = \frac{7}{16}$$\n\nLangkah 3: Menghitung peluang komplemen $P(M > 2)$:\n$$P(M > 2) = 1 - P(M \le 2) = 1 - \frac{7}{16} = \frac{9}{16}$$
**Acuan:** siswa — siswa hal.247

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-b-hard-bt01-007
*variasi (konteks) | C5 | 4 langkah | jenis: analisis distribusi variabel acak ekstremum*

Tiga buah dadu bersisi empat (tetrahedral) seimbang masing-masing memiliki nomor sisi 1, 2, 3, dan 4. Ketiga dadu dilempar bersamaan sebanyak satu kali. Misalkan variabel acak $M$ menyatakan nilai maksimum (angka terbesar) dari ketiga mata dadu yang muncul. Nilai dari $P(M \ge 3)$ adalah ....

- A. $\frac{37}{64}$  
  <sub>Salah: Hanya menghitung kejadian jika angka 3 atau 4 muncul minimal satu kali tanpa melibatkan pasangan ketiga dadu secara lengkap.</sub>
- B. $\frac{3}{4}$  
  <sub>Salah: Hanya menghitung proporsi angka $\ge 3$ pada satu dadu, yaitu $\frac{2}{4} = \frac{1}{2}$ lalu menambahkan peluang lain secara keliru.</sub>
- C. $\frac{27}{32}$  
  <sub>Salah: Keliru menghitung banyak kemungkinan komplemen sebagai $2 \times 2 \times 1 = 4$ kemungkinan sehingga $1 - \frac{4}{64} = \frac{15}{16}$ atau salah hitung pecahan.</sub>
- **D. $\frac{7}{8}$** ✅  
  <sub>Benar: Ruang sampel total adalah $4^3 = 64$. Peristiwa $M \ge 3$ berkomplemen dengan $M \le 2$, yaitu semua dadu hanya menghasilkan angka 1 atau 2. Banyak kejadian untuk $M \le 2$ adalah $2^3 = 8$. Maka $P(M \le 2) = \frac{8}{64} = \frac{1}{8}$. Dengan demikian, $P(M \ge 3) = 1 - \frac{1}{8} = \frac{7}{8}$.</sub>

**Pembahasan:** Banyaknya anggota ruang sampel pelambungan 3 dadu bersisi 4 adalah:
$$n(S) = 4 \times 4 \times 4 = 64$$
Variabel acak $M$ bernilai kurang dari 3 (yaitu $M \le 2$) jika setiap dadu hanya memunculkan angka 1 atau 2.
Banyaknya hasil yang memenuhi:
$$n(M \le 2) = 2 \times 2 \times 2 = 8$$
Sehingga peluang komplemennya adalah:
$$P(M \le 2) = \frac{8}{64} = \frac{1}{8}$$
Oleh karena itu, peluang nilai maksimum sekurang-kurangnya 3 adalah:
$$P(M \ge 3) = 1 - P(M \le 2) = 1 - \frac{1}{8} = \frac{7}{8}$$
**Acuan:** pretest — kelas12_tl-b04-p0253-latihan-soal-variabel-acak-diskret-2b

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-b-hard-bt01-008
*orisinal | C5 | 5 langkah | jenis: evaluasi peluang deret tak hingga variabel acak*

Sebuah eksperimen melambungkan sebuah dadu berimbang bersisi enam secara berulang-ulang sampai muncul mata dadu 6 untuk pertama kalinya. Misalkan variabel acak diskret $N$ menyatakan banyaknya lemparan yang dilakukan hingga mata dadu 6 muncul. Nilai dari peluang $P(N \text{ adalah bilangan ganjil})$ adalah ....

- A. $\frac{5}{11}$  
  <sub>Salah: Menghitung peluang bahwa $N$ adalah bilangan genap.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Mengasumsikan secara keliru bahwa peluang ganjil dan genap selalu sama pada variabel acak diskret tak hingga.</sub>
- **C. $\frac{6}{11}$** ✅  
  <sub>Benar: Peluang sukses (muncul 6) pada setiap lemparan adalah $p = \frac{1}{6}$, dan peluang gagal adalah $q = \frac{5}{6}$. Variabel acak $N \in \{1, 2, 3, \dots\}$ bernilai ganjil saat $N = 1, 3, 5, \dots$. Peluang $P(N = 2k-1) = q^{2k-2} p$. Jumlah seluruh peluang ganjil membentuk deret geometri tak hingga dengan suku pertama $a = p = \frac{1}{6}$ dan rasio $r = q^2 = \left(\frac{5}{6}\right)^2 = \frac{25}{36}$. Jumlahnya adalah $S = \frac{\frac{1}{6}}{1 - \frac{25}{36}} = \frac{\frac{1}{6}}{\frac{11}{36}} = \frac{6}{11}$.</sub>
- D. $\frac{5}{12}$  
  <sub>Salah: Keliru menggunakan rasio deret sebagai $q = \frac{5}{6}$ bukan $q^2$.</sub>

**Pembahasan:** Peluang muncul mata dadu 6 adalah $p = \frac{1}{6}$, sehingga peluang bukan mata dadu 6 adalah $q = 1 - \frac{1}{6} = \frac{5}{6}$.
Variabel acak $N$ menyatakan nomor lemparan ketika mata dadu 6 pertama kali muncul, dengan ruang nilai $\{1, 2, 3, \dots\}$.
Fungsi peluang dari $N$ adalah:
$$P(N = n) = q^{n-1} p$$
Kejadian $N$ bernilai ganjil terjadi jika $n \in \{1, 3, 5, 7, \dots\}$.
Maka peluangnya adalah jumlah deret geometri:
$$P(N \text{ ganjil}) = P(N=1) + P(N=3) + P(N=5) + \dots$$
$$P(N \text{ ganjil}) = p + q^2 p + q^4 p + \dots$$
Deret ini memiliki:
- Suku pertama: $a = p = \frac{1}{6}$
- Rasio: $r = q^2 = \left(\frac{5}{6}\right)^2 = \frac{25}{36}$
Jumlah deret geometri tak hingga:
$$P(N \text{ ganjil}) = \frac{a}{1 - r} = \frac{\frac{1}{6}}{1 - \frac{25}{36}} = \frac{\frac{1}{6}}{\frac{11}{36}} = \frac{6}{11}$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-b-hard-bt01-009
*orisinal | C6 | 5 langkah | jenis: perancangan distribusi variabel acak bertingkat*

Kotak A berisi 3 kartu bernomor 1, 2, dan 3. Kotak B berisi 3 kartu bernomor 2, 3, dan 4. Dari masing-masing kotak diambil satu kartu secara acak dan independen. Misalkan variabel acak diskret $W$ menyatakan hasil kali kedua nomor kartu yang terambil, yaitu $W = X \times Y$ dengan $X$ nomor dari kotak A dan $Y$ nomor dari kotak B. Nilai dari peluang $P(W > 4)$ adalah ....

- A. $\frac{1}{2}$  
  <sub>Salah: Mengira banyaknya kombinasi yang memenuhi genap setengah dari total tanpa mendaftar pasangan.</sub>
- B. $\frac{4}{9}$  
  <sub>Salah: Menghitung peluang $P(W \le 4)$ bukan $P(W > 4)$.</sub>
- **C. $\frac{5}{9}$** ✅  
  <sub>Benar: Banyaknya seluruh pasangan $(X, Y)$ adalah $3 \times 3 = 9$. Pasangan dengan hasil kali $W = X \times Y \le 4$ adalah: $(1, 2) \to 2$, $(1, 3) \to 3$, $(1, 4) \to 4$, $(2, 2) \to 4$. Total ada 4 pasangan. Maka peluang $P(W \le 4) = \frac{4}{9}$. Peluang $P(W > 4) = 1 - \frac{4}{9} = \frac{5}{9}$.</sub>
- D. $\frac{2}{3}$  
  <sub>Salah: Lupa menganggap pasangan $(1, 4)$ atau $(2, 2)$ memiliki hasil kali $\le 4$ sehingga menyimpulkan hanya ada 3 pasangan.</sub>

**Pembahasan:** Variabel acak $X \in \{1, 2, 3\}$ dan $Y \in \{2, 3, 4\}$.
Semua pasangan $(X, Y)$ yang mungkin berjumlah $3 \times 3 = 9$ dengan peluang masing-masing $\frac{1}{9}$:
1. $1 \times 2 = 2$
2. $1 \times 3 = 3$
3. $1 \times 4 = 4$
4. $2 \times 2 = 4$
5. $2 \times 3 = 6$
6. $2 \times 4 = 8$
7. $3 \times 2 = 6$
8. $3 \times 3 = 9$
9. $3 \times 4 = 12$

Pasangan dengan nilai $W \le 4$ adalah $\{(1,2), (1,3), (1,4), (2,2)\}$, berjumlah 4 kemungkinan.
Oleh karena itu, peluang untuk $W > 4$ adalah:
$$P(W > 4) = 1 - P(W \le 4) = 1 - \frac{4}{9} = \frac{5}{9}$$
**Acuan:** siswa — siswa hal.249

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-b-hard-bt01-010
*variasi (konteks) | C5 | 4 langkah | jenis: analisis sebaran selisih acak*

Empat keping uang logam seimbang dilambungkan secara bersamaan sebanyak satu kali. Misalkan variabel acak diskret $X$ menyatakan selisih mutlak antara banyaknya sisi Angka dan banyaknya sisi Gambar yang muncul. Nilai dari peluang $P(X = 2)$ adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Hanya memperhitungkan satu kejadian, misalnya saat $A = 3$ saja sehingga memperoleh $\frac{4}{16} = \frac{1}{4}$.</sub>
- B. $\frac{5}{8}$  
  <sub>Salah: Keliru menjumlahkan titik sampel $A=1$, $A=2$, dan $A=3$ ke dalam perhitungan.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Hanya menghitung peluang kejadian salah satu kondisi saja, yaitu ketika selisih bernilai 0 atau salah menghitung kombinasi 2 Angka 2 Gambar $\binom{4}{2}/16 = 6/16$.</sub>
- **D. $\frac{1}{2}$** ✅  
  <sub>Benar: Ruang sampel pelambungan 4 koin memiliki ukuran $2^4 = 16$. Misalkan $A$ menyatakan banyak Angka dan $G = 4 - A$ menyatakan banyak Gambar, maka $X = |A - G| = |2A - 4|$. Nilai $X = 2$ dipenuhi saat $|2A - 4| = 2$, yaitu $2A - 4 = 2 \implies A = 3$ atau $2A - 4 = -2 \implies A = 1$. Banyak kejadian untuk $A = 1$ adalah $\binom{4}{1} = 4$ dan untuk $A = 3$ adalah $\binom{4}{3} = 4$. Total titik sampel yang memenuhi adalah $4 + 4 = 8$, sehingga $P(X = 2) = \frac{8}{16} = \frac{1}{2}$.</sub>

**Pembahasan:** Ruang sampel dari pelambungan 4 keping koin adalah $n(S) = 2^4 = 16$. Variabel acak $X$ menyatakan selisih mutlak kemunculan Angka ($A$) dan Gambar ($G$). Hubungan $G = 4 - A$ menghasilkan $X = |A - (4 - A)| = |2A - 4|$. Nilai $X = 2$ diperoleh ketika $|2A - 4| = 2$, yang memiliki dua penyelesaian: $2A - 4 = 2 \implies A = 3$, atau $2A - 4 = -2 \implies A = 1$. Banyak anggota kejadian untuk $A = 1$ adalah $\binom{4}{1} = 4$ cara, dan untuk $A = 3$ adalah $\binom{4}{3} = 4$ cara. Jumlah total kejadian pendukung adalah $4 + 4 = 8$. Jadi, $P(X = 2) = \frac{8}{16} = \frac{1}{2}$.
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-b-hard-bt01-011
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi peluang hasil kali acak*

Dua buah roda putar angka diputar masing-masing satu kali secara independen. Roda A terbagi menjadi 3 sektor dengan angka 1, 2, dan 3 yang memiliki peluang kemunculan berturut-turut $P(X = 1) = \frac{1}{6}$, $P(X = 2) = \frac{2}{6}$, dan $P(X = 3) = \frac{3}{6}$. Roda B terbagi menjadi 2 sektor seimbang bernomor 2 dan 4, sehingga $P(Y = 2) = P(Y = 4) = \frac{1}{2}$. Jika variabel acak diskret didefinisikan sebagai hasil kali angka kedua roda, yaitu $W = X \cdot Y$, maka nilai peluang $P(W \ge 6)$ adalah ....

- **A. $\frac{2}{3}$** ✅  
  <sub>Benar: Pasangan $(X, Y)$ yang menghasilkan $W = X \cdot Y \ge 6$ adalah $(2, 4)$ dengan $W = 8$, $(3, 2)$ dengan $W = 6$, dan $(3, 4)$ dengan $W = 12$. Peluang masing-masing pasangan adalah: $P(2, 4) = \frac{2}{6} \times \frac{1}{2} = \frac{2}{12}$, $P(3, 2) = \frac{3}{6} \times \frac{1}{2} = \frac{3}{12}$, dan $P(3, 4) = \frac{3}{6} \times \frac{1}{2} = \frac{3}{12}$. Jumlah seluruh peluang tersebut adalah $\frac{2 + 3 + 3}{12} = \frac{8}{12} = \frac{2}{3}$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Lupa menyertakan pasangan $(2, 4)$ yang bernilai 8 sehingga hanya menjumlahkan $P(3, 2) + P(3, 4) = \frac{6}{12} = \frac{1}{2}$.</sub>
- C. $\frac{7}{12}$  
  <sub>Salah: Keliru mengalikan bobot peluang sektor roda A, menganggap peluang sektor 2 adalah $\frac{1}{6}$.</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: Menghitung pasangan secara keliru dengan memasukkan pasangan $(1, 4)$ ke dalam syarat pertidaksamaan.</sub>

**Pembahasan:** Nilai variabel acak $W = X \cdot Y$ untuk setiap pasangan $(X, Y)$ adalah sebagai berikut:
- $(1, 2) \implies W = 2$, peluang = $\frac{1}{6} \times \frac{1}{2} = \frac{1}{12}$
- $(1, 4) \implies W = 4$, peluang = $\frac{1}{6} \times \frac{1}{2} = \frac{1}{12}$
- $(2, 2) \implies W = 4$, peluang = $\frac{2}{6} \times \frac{1}{2} = \frac{2}{12}$
- $(2, 4) \implies W = 8$, peluang = $\frac{2}{6} \times \frac{1}{2} = \frac{2}{12}$
- $(3, 2) \implies W = 6$, peluang = $\frac{3}{6} \times \frac{1}{2} = \frac{3}{12}$
- $(3, 4) \implies W = 12$, peluang = $\frac{3}{6} \times \frac{1}{2} = \frac{3}{12}$

Nilai $W \ge 6$ dipenuhi oleh kejadian $W \in \{6, 8, 12\}$, yang bersesuaian dengan pasangan $(3, 2)$, $(2, 4)$, dan $(3, 4)$. Maka $P(W \ge 6) = \frac{3}{12} + \frac{2}{12} + \frac{3}{12} = \frac{8}{12} = \frac{2}{3}$.
**Acuan:** siswa — siswa hal.248 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-b-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: evaluasi peluang geometri diskret*

Sebuah eksperimen acak dilakukan dengan melambungkan koin tak seimbang berulang kali secara independen hingga muncul sisi Angka untuk pertama kalinya. Peluang muncul sisi Angka pada setiap lambungan adalah $\frac{1}{3}$. Jika variabel acak diskret $N$ menyatakan nomor lambungan saat sisi Angka pertama kali muncul, maka nilai peluang $P(N \text{ bilangan genap})$ adalah ....

- **A. $\frac{2}{5}$** ✅  
  <sub>Benar: Peluang sukses adalah $p = \frac{1}{3}$ dan peluang gagal adalah $q = 1 - p = \frac{2}{3}$. Variabel acak $N$ berdistribusi dengan peluang $P(N = k) = q^{k-1}p = (\frac{2}{3})^{k-1} \cdot \frac{1}{3}$ untuk $k \in \{1, 2, 3, \dots\}$. Nilai genap adalah $k \in \{2, 4, 6, \dots\}$. Peluangnya membentuk deret geometri tak hingga dengan suku pertama $a = P(N = 2) = (\frac{2}{3})^1 \cdot \frac{1}{3} = \frac{2}{9}$ dan rasio $r = (\frac{2}{3})^2 = \frac{4}{9}$. Jumlah deret adalah $S = \frac{a}{1 - r} = \frac{2/9}{1 - 4/9} = \frac{2/9}{5/9} = \frac{2}{5}$.</sub>
- B. $\frac{2}{9}$  
  <sub>Salah: Hanya menghitung nilai peluang pada suku pertama saja, yaitu $P(N = 2)$ tanpa menjumlahkan suku-suku genap berikutnya.</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: Mengasumsikan bahwa koin seimbang atau separuh dari total kemungkinan nilai berpeluang sama antara ganjil dan genap.</sub>
- D. $\frac{3}{5}$  
  <sub>Salah: Menghitung peluang untuk nomor pelambungan ganjil, yaitu $P(N \text{ ganjil}) = 1 - \frac{2}{5} = \frac{3}{5}$.</sub>

**Pembahasan:** Kejadian bahwa sisi Angka pertama kali muncul pada pelambungan ke-$k$ memiliki peluang $P(N = k) = (\frac{2}{3})^{k-1}(\frac{1}{3})$.
Untuk nilai $N$ berupa bilangan genap ($k = 2, 4, 6, \dots$):
$P(N = 2) = (\frac{2}{3})^1 (\frac{1}{3}) = \frac{2}{9}$
$P(N = 4) = (\frac{2}{3})^3 (\frac{1}{3}) = \frac{2}{9} \times \frac{4}{9}$
$P(N = 6) = (\frac{2}{3})^5 (\frac{1}{3}) = \frac{2}{9} \times (\frac{4}{9})^2$
Ini merupakan deret geometri tak hingga dengan suku pertama $a = \frac{2}{9}$ dan rasio $r = (\frac{2}{3})^2 = \frac{4}{9}$.
Jumlah seluruh peluang genap adalah:
$P(N \text{ genap}) = \frac{a}{1 - r} = \frac{\frac{2}{9}}{1 - \frac{4}{9}} = \frac{\frac{2}{9}}{\frac{5}{9}} = \frac{2}{5}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-b-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: evaluasi transformasi variabel acak*

Dua buah dadu seimbang bersisi enam dilempar bersamaan sebanyak satu kali. Misalkan variabel acak diskret $D$ menyatakan selisih mutlak dari kedua mata dadu yang muncul. Suatu variabel acak diskret baru didefinisikan sebagai $U = D^2 - 3D$. Nilai peluang $P(U = 0)$ adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: Hanya menghitung titik sampel saat $D = 0$ saja atau saat $D = 3$ saja sehingga memperoleh $\frac{6}{36} = \frac{1}{6}$.</sub>
- B. $\frac{5}{18}$  
  <sub>Salah: Keliru dalam mencacah pasangan mata dadu dengan selisih 3 (lupa pasangan terbalik sehingga hanya 3 titik).</sub>
- **C. $\frac{1}{3}$** ✅  
  <sub>Benar: Persamaan $U = 0 \iff D^2 - 3D = 0 \iff D(D - 3) = 0$, sehingga $D = 0$ atau $D = 3$. Kejadian $D = 0$ memiliki 6 titik sampel: $(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)$. Kejadian $D = 3$ memiliki 6 titik sampel: $(1,4), (4,1), (2,5), (5,2), (3,6), (6,3)$. Total titik sampel adalah $6 + 6 = 12$ dari 36 kemungkinan. Maka $P(U = 0) = \frac{12}{36} = \frac{1}{3}$.</sub>
- D. $\frac{4}{9}$  
  <sub>Salah: Salah memfaktorkan persamaan kuadrat, menganggap akar persamaan adalah $D = 0$ dan $D = 4$.</sub>

**Pembahasan:** Dua dadu dilempar sehingga ukuran ruang sampel adalah $n(S) = 6 \times 6 = 36$.
Variabel acak $U = D^2 - 3D$. Nilai $U = 0$ terjadi jika dan hanya jika:
$D(D - 3) = 0 \implies D = 0 \text{ atau } D = 3$.

1. Kasus $D = 0$ (kedua dadu bermata sama):
Pasangannya adalah $(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)$ $\implies 6$ titik sampel.

2. Kasus $D = 3$ (selisih mutlak kedua mata dadu bernilai 3):
Pasangannya adalah $(1,4), (4,1), (2,5), (5,2), (3,6), (6,3)$ $\implies 6$ titik sampel.

Karena kedua kejadian tersebut saling lepas, banyak seluruh titik sampel yang memenuhi adalah $6 + 6 = 12$.
Jadi, $P(U = 0) = \frac{12}{36} = \frac{1}{3}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-b-hard-bt01-014
*variasi (konteks) | C5 | 5 langkah | jenis: evaluasi peluang variabel acak binomial*

Sebuah sistem transmisi data memiliki 4 saluran independen. Masing-masing saluran memiliki peluang mengalami gangguan sebesar $\frac{1}{3}$. Misalkan variabel acak diskret $X$ menyatakan banyaknya saluran yang berfungsi normal tanpa gangguan. Sistem dinyatakan mampu mentransmisikan data jika sekurang-kurangnya 3 saluran berfungsi normal. Berapakah peluang sistem tersebut mampu mentransmisikan data?

- **A. $\frac{16}{27}$** ✅  
  <sub>Benar: Peluang satu saluran berfungsi normal adalah $p = 1 - \frac{1}{3} = \frac{2}{3}$. Nilai $X$ berdistribusi dengan daerah nilai $\{0, 1, 2, 3, 4\}$. Kejadian sistem mampu mentransmisikan data terjadi saat $X \ge 3$, yaitu $X = 3$ atau $X = 4$. Dihitung: $P(X = 3) = \binom{4}{3} \left(\frac{2}{3}\right)^3 \left(\frac{1}{3}\right)^1 = 4 \cdot \frac{8}{27} \cdot \frac{1}{3} = \frac{32}{81}$, dan $P(X = 4) = \binom{4}{4} \left(\frac{2}{3}\right)^4 \left(\frac{1}{3}\right)^0 = 1 \cdot \frac{16}{81} \cdot 1 = \frac{16}{81}$. Maka $P(X \ge 3) = \frac{32}{81} + \frac{16}{81} = \frac{48}{81} = \frac{16}{27}$.</sub>
- B. $\frac{32}{81}$  
  <sub>Salah: Hanya menghitung peluang tepat 3 saluran berfungsi dan mengabaikan kemungkinan 4 saluran berfungsi.</sub>
- C. $\frac{65}{81}$  
  <sub>Salah: Keliru menjumlahkan peluang mulai dari $X \ge 2$ bukannya $X \ge 3$.</sub>
- D. $\frac{8}{27}$  
  <sub>Salah: Tertukar menetapkan peluang sukses transmisi dengan peluang gangguan $\frac{1}{3}$.</sub>

**Pembahasan:** Diketahui peluang satu saluran berfungsi normal adalah $p = 1 - \frac{1}{3} = \frac{2}{3}$ dan peluang gangguan adalah $q = \frac{1}{3}$. Banyaknya saluran adalah $n = 4$.
Variabel acak diskret $X$ menyatakan banyaknya saluran yang berfungsi normal, sehingga sistem beroperasi ketika $X \ge 3$ (yakni $X = 3$ atau $X = 4$).
1. Hitung peluang untuk $X = 3$:
$$P(X = 3) = \binom{4}{3} \left(\frac{2}{3}\right)^3 \left(\frac{1}{3}\right)^1 = 4 \cdot \frac{8}{27} \cdot \frac{1}{3} = \frac{32}{81}$$
2. Hitung peluang untuk $X = 4$:
$$P(X = 4) = \binom{4}{4} \left(\frac{2}{3}\right)^4 \left(\frac{1}{3}\right)^0 = 1 \cdot \frac{16}{81} \cdot 1 = \frac{16}{81}$$
3. Jumlahkan kedua peluang:
$$P(X \ge 3) = P(X = 3) + P(X = 4) = \frac{32}{81} + \frac{16}{81} = \frac{48}{81} = \frac{16}{27}$$
Jadi, peluang sistem mampu mentransmisikan data adalah $\frac{16}{27}$.
**Acuan:** siswa — siswa hal.250 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-b-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: analisis parameter distribusi peluang diskret*

Sebuah variabel acak diskret $X$ memiliki himpunan nilai $\{1, 2, 3, 4\}$ dengan fungsi distribusi peluang didefinisikan oleh:
$$P(X = x) = c(k - x)$$
untuk setiap $x \in \{1, 2, 3, 4\}$, dengan $c$ dan $k$ adalah konstanta real positif. Jika diketahui bahwa $P(X = 1) = 2 \cdot P(X = 3)$, berapakah nilai konstanta $c$?

- A. $\frac{1}{15}$  
  <sub>Salah: Salah menghitung jumlahan deret koefisien dengan menambahkan suku ke-5.</sub>
- **B. $\frac{1}{10}$** ✅  
  <sub>Benar: Dari $P(X = 1) = 2 P(X = 3)$ diperoleh $c(k - 1) = 2c(k - 3)$. Karena $c > 0$, maka $k - 1 = 2k - 6 \implies k = 5$. Total peluang harus sama dengan 1: $\sum_{x=1}^{4} c(5 - x) = c(4 + 3 + 2 + 1) = 10c = 1 \implies c = \frac{1}{10}$.</sub>
- C. $\frac{1}{8}$  
  <sub>Salah: Keliru menyelesaikan persamaan rasio menjadi $k=6$ dan salah menjumlahkan bobot nilai.</sub>
- D. $\frac{1}{6}$  
  <sub>Salah: Hanya menjumlahkan suku untuk $x=1, 2, 3$ sehingga diperoleh $9c=1$ atau salah menentukan nilai $k$.</sub>

**Pembahasan:** Berdasarkan definisi fungsi peluang:
$P(X = 1) = c(k - 1)$
$P(X = 3) = c(k - 3)$

Diketahui $P(X = 1) = 2 \cdot P(X = 3)$:
$$c(k - 1) = 2c(k - 3)$$
Karena $c > 0$, bagi kedua ruas dengan $c$:
$$k - 1 = 2k - 6 \implies k = 5$$

Sifat total peluang dari variabel acak diskret mensyaratkan $\sum_{x=1}^{4} P(X = x) = 1$:
$$P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) = 1$$
$$c(5 - 1) + c(5 - 2) + c(5 - 3) + c(5 - 4) = 1$$
$$c(4 + 3 + 2 + 1) = 1$$
$$10c = 1 \implies c = \frac{1}{10}$$
Jadi, nilai konstanta $c$ adalah $\frac{1}{10}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-b-hard-bt01-016
*orisinal | C6 | 5 langkah | jenis: evaluasi model distribusi peluang tak hingga*

Sebuah variabel acak diskret $N$ menyatakan banyaknya pengulangan percobaan independen hingga suatu peristiwa berhasil terjadi untuk pertama kalinya. Diketahui $N$ memiliki daerah nilai $\{1, 2, 3, \dots\}$ dengan fungsi peluang:
$$P(N = n) = (1 - p)^{n-1} p$$
dengan $0 < p < 1$. Jika perbandingan antara peluang peristiwa berhasil pada percobaan bernomor ganjil dan peluang peristiwa berhasil pada percobaan bernomor genap adalah $7 : 3$, berapakah nilai $p$?

- A. $\frac{5}{7}$  
  <sub>Salah: Salah melakukan operasi aljabar saat menyelesaikan persamaan linear $7 - 7p = 3$.</sub>
- B. $\frac{3}{7}$  
  <sub>Salah: Tertukar menghitung nilai $1 - p$ sebagai nilai parameter $p$.</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: Keliru mengidentifikasi nilai peluang total percobaan genap sebagai nilai parameter peluang $p$.</sub>
- **D. $\frac{4}{7}$** ✅  
  <sub>Benar: Peluang $N$ ganjil adalah deret geometri tak hingga dengan suku pertama $p$ dan rasio $(1-p)^2$, yang berjumlah $\frac{p}{1-(1-p)^2} = \frac{1}{2-p}$. Peluang $N$ genap adalah $1 - \frac{1}{2-p} = \frac{1-p}{2-p}$. Rasio keduanya $\frac{1}{1-p} = \frac{7}{3} \implies 7(1-p) = 3 \implies 7 - 7p = 3 \implies p = \frac{4}{7}$.</sub>

**Pembahasan:** Variabel acak $N$ menyatakan indeks keberhasilan pertama. Peluang kejadian bernomor ganjil diperoleh dengan menjumlahkan peluang untuk $n = 1, 3, 5, \dots$:
$$P(N \text{ ganjil}) = p + p(1-p)^2 + p(1-p)^4 + \dots$$
Ini adalah deret geometri tak hingga dengan suku awal $a = p$ dan rasio $r = (1-p)^2$:
$$P(N \text{ ganjil}) = \frac{p}{1 - (1-p)^2} = \frac{p}{2p - p^2} = \frac{1}{2 - p}$$

Karena total seluruh peluang bernilai 1, maka peluang kejadian bernomor genap adalah:
$$P(N \text{ genap}) = 1 - P(N \text{ ganjil}) = 1 - \frac{1}{2-p} = \frac{1 - p}{2 - p}$$

Berdasarkan perbandingan yang diketahui:
$$\frac{P(N \text{ ganjil})}{P(N \text{ genap})} = \frac{\frac{1}{2-p}}{\frac{1-p}{2-p}} = \frac{1}{1-p} = \frac{7}{3}$$
Selesaikan persamaan tersebut:
$$7(1 - p) = 3$$
$$7 - 7p = 3$$
$$7p = 4 \implies p = \frac{4}{7}$$
Jadi, nilai parameter peluang $p$ adalah $\frac{4}{7}$.
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-b-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: analisis distribusi variabel acak bersyarat*

Kotak A berisi 2 bola merah dan 3 bola biru, sedangkan Kotak B berisi 3 bola merah dan 1 bola biru. Sebuah bola diambil secara acak dari Kotak A lalu dimasukkan ke dalam Kotak B. Setelah tercampur rata, 2 bola diambil sekaligus secara acak dari Kotak B. Misalkan variabel acak diskret $X$ menyatakan banyaknya bola merah yang terambil dari Kotak B. Jika diketahui terambil tepat 1 bola merah dari Kotak B, maka peluang bahwa bola yang dipindahkan dari Kotak A ke Kotak B adalah bola merah sebesar ....

- A. $\frac{2}{5}$  
  <sub>Salah: Siswa hanya menggunakan peluang apriori terambilnya bola merah dari Kotak A tanpa mempertimbangkan informasi hasil variabel acak $X$.</sub>
- B. $\frac{9}{13}$  
  <sub>Salah: Siswa menghitung peluang bahwa bola yang dipindahkan adalah bola biru, yaitu $\frac{18}{26}$.</sub>
- **C. $\frac{4}{13}$** ✅  
  <sub>Benar: Peluang bola merah dipindahkan adalah $P(M) = \frac{2}{5}$ dan biru $P(B) = \frac{3}{5}$. Jika merah dipindahkan, Kotak B berisi 4 merah dan 1 biru, sehingga $P(X = 1 \mid M) = \frac{\binom{4}{1}\binom{1}{1}}{\binom{5}{2}} = \frac{4}{10}$. Jika biru dipindahkan, Kotak B berisi 3 merah dan 2 biru, sehingga $P(X = 1 \mid B) = \frac{\binom{3}{1}\binom{2}{1}}{\binom{5}{2}} = \frac{6}{10}$. Peluang total $P(X = 1) = \frac{2}{5}\left(\frac{4}{10}\right) + \frac{3}{5}\left(\frac{6}{10}\right) = \frac{8 + 18}{50} = \frac{26}{50}$. Maka peluang posterior $P(M \mid X = 1) = \frac{8/50}{26/50} = \frac{8}{26} = \frac{4}{13}$.</sub>
- D. $\frac{4}{25}$  
  <sub>Salah: Siswa hanya menghitung peluang gabungan $P(M \cap X = 1) = \frac{8}{50} = \frac{4}{25}$ tanpa membaginya dengan total peluang ruang syarat $P(X = 1)$.</sub>

**Pembahasan:** Langkah 1: Tentukan peluang kejadian pemindahan bola dari Kotak A:
- Bola merah terpindah ($M$): $P(M) = \frac{2}{5}$
- Bola biru terpindah ($B$): $P(B) = \frac{3}{5}$

Langkah 2: Tentukan komposisi Kotak B setelah pemindahan:
- Jika $M$ terpindah: Kotak B berisi 4 merah dan 1 biru (total 5 bola).
- Jika $B$ terpindah: Kotak B berisi 3 merah dan 2 biru (total 5 bola).

Langkah 3: Hitung peluang bersyarat terambil tepat 1 bola merah ($X = 1$):
$$P(X = 1 \mid M) = \frac{\binom{4}{1}\binom{1}{1}}{\binom{5}{2}} = \frac{4 \times 1}{10} = \frac{4}{10}$$
$$P(X = 1 \mid B) = \frac{\binom{3}{1}\binom{2}{1}}{\binom{5}{2}} = \frac{3 \times 2}{10} = \frac{6}{10}$$

Langkah 4: Hitung peluang total terjadinya $X = 1$:
$$P(X = 1) = P(M) \cdot P(X = 1 \mid M) + P(B) \cdot P(X = 1 \mid B)$$
$$P(X = 1) = \left(\frac{2}{5} \times \frac{4}{10}\right) + \left(\frac{3}{5} \times \frac{6}{10}\right) = \frac{8}{50} + \frac{18}{50} = \frac{26}{50}$$

Langkah 5: Hitung peluang posterior bola merah terpindah dengan rumus Bayes:
$$P(M \mid X = 1) = \frac{P(M \cap X = 1)}{P(X = 1)} = \frac{\frac{8}{50}}{\frac{26}{50}} = \frac{8}{26} = \frac{4}{13}$$
**Acuan:** siswa — siswa hal.248

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-b-hard-bt01-018
*orisinal | C5 | 5 langkah | jenis: analisis fungsi distribusi kumulatif diskret*

Sebuah variabel acak diskret $X$ memiliki ruang nilai $\{1, 2, 3, 4, 5\}$. Fungsi distribusi kumulatif dari $X$ didefinisikan sebagai:
$$F(x) = P(X \le x) = \frac{x^2 + k}{30}$$
untuk setiap $x \in \{1, 2, 3, 4, 5\}$, dengan $k$ suatu konstanta real. Nilai dari peluang bersyarat $P(X \text{ ganjil} \mid X \ge 2)$ adalah ....

- A. $\frac{5}{12}$  
  <sub>Salah: Siswa salah mengidentifikasi komplemen atau menghitung $P(X \text{ genap} \mid X \ge 2) = \frac{3 + 7}{24} = \frac{10}{24} = \frac{5}{12}$.</sub>
- **B. $\frac{7}{12}$** ✅  
  <sub>Benar: Karena nilai maksimum $X$ adalah 5, maka $F(5) = 1 \implies \frac{5^2 + k}{30} = 1 \implies k = 5$. Diperoleh $F(x) = \frac{x^2 + 5}{30}$. Peluang tiap nilai: $P(X = 1) = F(1) = \frac{6}{30}$, $P(X = 2) = F(2) - F(1) = \frac{9 - 6}{30} = \frac{3}{30}$, $P(X = 3) = F(3) - F(2) = \frac{14 - 9}{30} = \frac{5}{30}$, $P(X = 4) = F(4) - F(3) = \frac{21 - 14}{30} = \frac{7}{30}$, dan $P(X = 5) = F(5) - F(4) = \frac{30 - 21}{30} = \frac{9}{30}$. Maka $P(X \ge 2) = 1 - P(X = 1) = 1 - \frac{6}{30} = \frac{24}{30}$. Nilai $X$ ganjil dan $X \ge 2$ adalah $\{3, 5\}$, dengan $P(X \in \{3, 5\}) = \frac{5 + 9}{30} = \frac{14}{30}$. Jadi, $P(X \text{ ganjil} \mid X \ge 2) = \frac{14/30}{24/30} = \frac{14}{24} = \frac{7}{12}$.</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: Siswa menghitung peluang $X$ ganjil tanpa syarat, yaitu $P(X \in \{1, 3, 5\}) = \frac{6 + 5 + 9}{30} = \frac{20}{30} = \frac{2}{3}$.</sub>
- D. $\frac{7}{15}$  
  <sub>Salah: Siswa hanya menghitung peluang gabungan $P(X \text{ ganjil} \cap X \ge 2) = \frac{14}{30} = \frac{7}{15}$ tanpa membaginya dengan peluang syarat $P(X \ge 2)$.</sub>

**Pembahasan:** Langkah 1: Menentukan nilai konstanta $k$.
Berdasarkan sifat fungsi distribusi kumulatif untuk nilai maksimum pada ruang nilai diskret:
$$F(5) = 1 \iff \frac{5^2 + k}{30} = 1 \iff 25 + k = 30 \iff k = 5$$
Sehingga rumus fungsi distribusi kumulatif menjadi $F(x) = \frac{x^2 + 5}{30}$.

Langkah 2: Menghitung fungsi massa peluang $P(X = x) = F(x) - F(x-1)$:
- $P(X = 1) = F(1) = \frac{1^2 + 5}{30} = \frac{6}{30}$
- $P(X = 2) = F(2) - F(1) = \frac{9}{30} - \frac{6}{30} = \frac{3}{30}$
- $P(X = 3) = F(3) - F(2) = \frac{14}{30} - \frac{9}{30} = \frac{5}{30}$
- $P(X = 4) = F(4) - F(3) = \frac{21}{30} - \frac{14}{30} = \frac{7}{30}$
- $P(X = 5) = F(5) - F(4) = \frac{30}{30} - \frac{21}{30} = \frac{9}{30}$

Langkah 3: Menghitung peluang kejadian syarat $X \ge 2$:
$$P(X \ge 2) = 1 - P(X = 1) = 1 - \frac{6}{30} = \frac{24}{30}$$

Langkah 4: Menghitung peluang irisan kejadian $X$ ganjil dan $X \ge 2$ (yaitu $X = 3$ atau $X = 5$):
$$P(X \in \{3, 5\}) = P(X = 3) + P(X = 5) = \frac{5}{30} + \frac{9}{30} = \frac{14}{30}$$

Langkah 5: Menghitung nilai peluang bersyarat:
$$P(X \text{ ganjil} \mid X \ge 2) = \frac{P(X \in \{3, 5\})}{P(X \ge 2)} = \frac{\frac{14}{30}}{\frac{24}{30}} = \frac{14}{24} = \frac{7}{12}$$
**Acuan:** siswa — siswa hal.247

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
