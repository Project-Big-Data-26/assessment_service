# Lembar koreksi — kelas12_tl SMA12L-B4 subbab D: Fungsi Peluang

59 soal | easy 20, medium 20, hard 19 | variasi 28, orisinal 31
> **Kapasitas kurang (hard): 19 dari kuota 20** — 9 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-d-easy-bt01-001
*variasi (angka) | C2 | 2 langkah | jenis: peluang variabel acak hipergeometrik sederhana*

Sebuah kotak berisi 8 butir telur, 2 di antaranya retak. Dika mengambil 2 butir telur sekaligus secara acak. Jika $X$ menyatakan banyak telur retak yang terambil, nilai dari $P(X = 0)$ adalah ....

- A. $\frac{1}{28}$  
  <sub>Salah: Siswa menghitung peluang terambilnya 2 telur retak sekaligus ($P(X=2)$).</sub>
- **B. $\frac{15}{28}$** ✅  
  <sub>Benar: Banyak cara memilih 2 telur dari 8 telur adalah $\binom{8}{2} = 28$. Kejadian terambil 0 telur retak berarti mengambil 2 telur baik dari 6 telur tidak retak, yaitu $\binom{6}{2} = 15$. Jadi, $P(X = 0) = \frac{15}{28}$.</sub>
- C. $\frac{13}{28}$  
  <sub>Salah: Siswa menghitung komplemen dari nilai yang salah.</sub>
- D. $\frac{6}{28}$  
  <sub>Salah: Siswa salah menghitung kombinasi 2 dari 6 sebagai 6.</sub>

**Pembahasan:** Banyak anggota ruang sampel memilih 2 dari 8 telur:
$$n(S) = \binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$$
Kejadian $X = 0$ berarti terambil 0 telur retak dan 2 telur baik dari 6 telur baik:
$$n(X = 0) = \binom{2}{0} \times \binom{6}{2} = 1 \times 15 = 15$$
Maka, nilai peluangnya adalah:
$$P(X = 0) = \frac{15}{28}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-d-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: peluang variabel acak binomial sederhana*

Dalam sebuah kuis singkat, terdapat 4 soal bertipe benar atau salah. Seorang siswa menjawab semua soal secara acak. Jika $X$ menyatakan banyak jawaban benar yang diperoleh siswa tersebut, nilai $P(X = 4)$ adalah ....

- A. $\frac{1}{4}$  
  <sub>Salah: Siswa langsung membagi 1 dengan banyak soal.</sub>
- B. $\frac{1}{8}$  
  <sub>Salah: Siswa salah menganggap ruang sampel 4 soal benar-salah adalah $2 \times 4 = 8$.</sub>
- **C. $\frac{1}{16}$** ✅  
  <sub>Benar: Total kemungkinan jawaban dari 4 soal adalah $2^4 = 16$. Kejadian semua jawaban benar hanya ada 1 kemungkinan, sehingga $P(X = 4) = \frac{1}{16}$.</sub>
- D. $\frac{4}{16}$  
  <sub>Salah: Siswa mengira ada 4 kemungkinan cara memperoleh semua jawaban benar.</sub>

**Pembahasan:** Setiap soal memiliki 2 kemungkinan jawaban (benar atau salah), sehingga untuk 4 soal:
$$n(S) = 2^4 = 16$$
Kejadian $X = 4$ artinya keempat soal dijawab dengan benar seluruhnya, yang hanya ada 1 kemungkinan:
$$n(X = 4) = 1$$
Jadi, nilai peluangnya adalah:
$$P(X = 4) = \frac{1}{16}$$
**Acuan:** pretest — kelas12_tl-b04-p0264-latihan-soal-fungsi-peluang-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-d-easy-bt01-003
*orisinal | C2 | 1 langkah | jenis: sifat total peluang*

| $X = x$ | 1 | 2 | 3 |
|---|---|---|---|
| $P(X = x)$ | 0,2 | $k$ | 0,5 |

Tabel di atas menyajikan distribusi peluang untuk variabel acak diskret $X$. Nilai $k$ yang memenuhi adalah ....

- A. 0,4  
  <sub>Salah: Siswa salah melakukan pengurangan desimal.</sub>
- **B. 0,3** ✅  
  <sub>Benar: Total peluang seluruh nilai variabel acak diskret harus sama dengan 1, sehingga $k = 1 - (0,2 + 0,5) = 0,3$.</sub>
- C. 0,1  
  <sub>Salah: Siswa salah mengurangkan dari nilai acuan yang keliru.</sub>
- D. 0,7  
  <sub>Salah: Siswa hanya menjumlahkan peluang yang diketahui ($0,2 + 0,5$).</sub>

**Pembahasan:** Berdasarkan syarat fungsi peluang diskret, jumlah seluruh peluang harus bernilai 1:
$$\sum P(X = x) = 1$$
$$0,2 + k + 0,5 = 1$$
$$0,7 + k = 1$$
$$k = 1 - 0,7 = 0,3$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-d-easy-bt01-004
*orisinal | C1 | 1 langkah | jenis: distribusi peluang uang logam*

Dua keping uang logam setimbang dilempar bersamaan satu kali. Jika $X$ menyatakan variabel acak banyaknya sisi angka yang muncul, nilai dari $P(X = 1)$ adalah ....

- **A. $\frac{1}{2}$** ✅  
  <sub>Benar: Ruang sampel pelemparan 2 koin adalah $\{AA, AG, GA, GG\}$ dengan $n(S) = 4$. Muncul tepat 1 angka terjadi pada $\{AG, GA\}$ sehingga peluangnya $\frac{2}{4} = \frac{1}{2}$.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Siswa hanya menghitung salah satu kejadian ($AG$ saja).</sub>
- C. $\frac{3}{4}$  
  <sub>Salah: Siswa menghitung peluang munculnya paling sedikit 1 angka ($P(X \ge 1)$).</sub>
- D. 1  
  <sub>Salah: Siswa salah memahami konsep peluang total sebagai peluang kejadian tersebut.</sub>

**Pembahasan:** Ruang sampel pelemparan dua koin:
$$S = \{AA, AG, GA, GG\} \implies n(S) = 4$$
Kejadian $X = 1$ (muncul 1 sisi angka):
$$A = \{AG, GA\} \implies n(A) = 2$$
Maka diperoleh nilai peluang:
$$P(X = 1) = \frac{2}{4} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-d-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: nilai peluang fungsi distribusi diskret*

Diketahui fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{x}{15}, & \text{untuk } x = 4, 5, 6 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \ge 5)$ adalah …

- A. $\frac{5}{15}$  
  <sub>Salah: Hanya menghitung nilai $P(X = 5)$ tanpa menjumlahkan untuk $x = 6$.</sub>
- B. $\frac{6}{15}$  
  <sub>Salah: Hanya menghitung nilai untuk $x = 6$.</sub>
- **C. $\frac{11}{15}$** ✅  
  <sub>Benar: $P(X \ge 5) = f(5) + f(6) = \frac{5}{15} + \frac{6}{15} = \frac{11}{15}$.</sub>
- D. $\frac{4}{15}$  
  <sub>Salah: Menghitung komplemen yang salah atau hanya menghitung $P(X < 5) = f(4) = \frac{4}{15}$.</sub>

**Pembahasan:** Nilai variabel acak yang memenuhi $X \ge 5$ adalah $x = 5$ dan $x = 6$.
$$P(X \ge 5) = f(5) + f(6) = \frac{5}{15} + \frac{6}{15} = \frac{11}{15}$$
**Acuan:** siswa — siswa hal.263 Latihan Soal Fungsi Peluang

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-d-easy-bt01-006
*variasi (konteks) | C2 | 2 langkah | jenis: peluang variabel acak hipergeometrik*

Sebuah toples berisi 4 kelereng biru dan 2 kelereng kuning. Dari dalam toples tersebut diambil 2 butir kelereng sekaligus secara acak. Jika variabel acak $Y$ menyatakan banyaknya kelereng kuning yang terambil, nilai dari $P(Y = 2)$ adalah …

- A. $\frac{2}{15}$  
  <sub>Salah: Menuliskan jumlah kelereng kuning (2) langsung sebagai pembilang.</sub>
- B. $\frac{6}{15}$  
  <sub>Salah: Menghitung peluang terambilnya 0 kelereng kuning: $\frac{\binom{4}{2}}{15} = \frac{6}{15}$.</sub>
- C. $\frac{8}{15}$  
  <sub>Salah: Menghitung peluang terambilnya 1 kelereng kuning dan 1 kelereng biru: $\frac{\binom{2}{1}\binom{4}{1}}{15} = \frac{8}{15}$.</sub>
- **D. $\frac{1}{15}$** ✅  
  <sub>Benar: Banyak cara memilih 2 kelereng kuning dari 2 yang ada adalah $\binom{2}{2} = 1$. Total cara memilih 2 kelereng dari 6 kelereng adalah $\binom{6}{2} = 15$. Jadi, $P(Y = 2) = \frac{1}{15}$.</sub>

**Pembahasan:** Banyak cara memilih 2 kelereng dari total 6 kelereng:
$$n(S) = \binom{6}{2} = \frac{6 \times 5}{2 \times 1} = 15$$
Banyak cara terambil 2 kelereng kuning:
$$n(Y = 2) = \binom{2}{2} \times \binom{4}{0} = 1 \times 1 = 1$$
Sehingga peluangnya adalah:
$$P(Y = 2) = \frac{1}{15}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-d-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: peluang terambil tanpa cacat*

Sebuah kotak memuat 7 bohlam lampu, dengan 3 di antaranya dalam keadaan rusak. Seorang petugas mengambil 2 bohlam secara acak sekaligus. Jika variabel acak $X$ menyatakan banyak bohlam rusak yang terambil, nilai peluang terambilnya semua bohlam dalam keadaan baik ($P(X = 0)$) adalah …

- A. $\frac{3}{7}$  
  <sub>Salah: Menggunakan rasio langsung banyak bohlam rusak terhadap total tanpa kombinasi.</sub>
- B. $\frac{1}{7}$  
  <sub>Salah: Menghitung peluang kedua bohlam rusak: $\frac{\binom{3}{2}}{21} = \frac{3}{21} = \frac{1}{7}$.</sub>
- C. $\frac{4}{7}$  
  <sub>Salah: Menghitung peluang terambilnya 1 bohlam rusak: $\frac{\binom{3}{1}\binom{4}{1}}{21} = \frac{12}{21} = \frac{4}{7}$.</sub>
- **D. $\frac{2}{7}$** ✅  
  <sub>Benar: Bohlam baik berjumlah $7 - 3 = 4$. $P(X = 0) = \frac{\binom{4}{2}\binom{3}{0}}{\binom{7}{2}} = \frac{6}{21} = \frac{2}{7}$.</sub>

**Pembahasan:** Banyak bohlam baik $= 7 - 3 = 4$.
Total kemungkinan mengambil 2 bohlam dari 7 bohlam:
$$n(S) = \binom{7}{2} = \frac{7 \times 6}{2 \times 1} = 21$$
Banyak cara mengambil 0 bohlam rusak (keduanya bohlam baik):
$$n(X = 0) = \binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6$$
Peluang terambil semua baik:
$$P(X = 0) = \frac{6}{21} = \frac{2}{7}$$
**Acuan:** siswa — siswa hal.261 Ayo Mencoba 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-d-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: syarat fungsi peluang diskret*

Misalkan $X$ adalah suatu variabel acak diskret dengan nilai-nilai $x$ yang mungkin. Suatu fungsi $f(x)$ sah menjadi fungsi peluang (distribusi peluang) dari $X$ jika memenuhi syarat …

- A. $f(x) \le 1$ untuk setiap $x$, dan $\sum f(x) > 1$  
  <sub>Salah: Keliru menganggap jumlah total peluang boleh lebih dari 1.</sub>
- B. $f(x) > 0$ untuk setiap $x$, dan $\sum f(x) = 0$  
  <sub>Salah: Keliru menganggap jumlah total peluang bernilai 0.</sub>
- C. $f(x) = 1$ untuk setiap $x$, dan $\sum f(x) = 1$  
  <sub>Salah: Menyamakan setiap nilai fungsi harus bernilai 1.</sub>
- **D. $f(x) \ge 0$ untuk setiap $x$, dan $\sum f(x) = 1$** ✅  
  <sub>Benar: Sesuai definisi fungsi peluang diskret, setiap nilai peluang harus tak negatif ($f(x) \ge 0$) dan jumlah total seluruh peluang harus sama dengan 1 ($\sum f(x) = 1$).</sub>

**Pembahasan:** Berdasarkan sifat fungsi peluang untuk variabel acak diskret, fungsi $f(x)$ harus memenuhi dua syarat utama:
1. $f(x) \ge 0$ untuk setiap nilai $x$ yang mungkin.
2. $\sum f(x) = 1$ (jumlah seluruh peluang adalah 1).
**Acuan:** siswa — siswa hal.259

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-d-easy-bt01-009
*orisinal | C1 | 1 langkah | jenis: peluang pelemparan uang logam*

Sebuah uang logam setimbang dilemparkan sebanyak tiga kali. Jika variabel acak $X$ menyatakan banyaknya sisi gambar (G) yang muncul dalam tiga kali pelemparan tersebut, nilai dari $P(X = 3)$ adalah …

- **A. $\frac{1}{8}$** ✅  
  <sub>Benar: Ruang sampel pelemparan 3 uang logam memiliki $2^3 = 8$ titik sampel. Kejadian muncul 3 gambar hanya memiliki 1 titik sampel, yaitu $(GGG)$, sehingga peluangnya adalah $\frac{1}{8}$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Menggunakan peluang muncul gambar pada satu kali lemparan saja.</sub>
- C. $\frac{3}{8}$  
  <sub>Salah: Keliru menghitung untuk kejadian muncul 1 atau 2 gambar, yaitu $\binom{3}{1} = \binom{3}{2} = 3$ cara.</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: Salah membagi banyak kejadian sukses dengan total lemparan (3).</sub>

**Pembahasan:** Ruang sampel dari 3 pelemparan uang logam adalah:
$$S = \{AAA, AAG, AGA, AGG, GAA, GAG, GGA, GGG\}$$
Banyaknya titik sampel adalah $n(S) = 8$.
Kejadian $X = 3$ (muncul 3 sisi gambar) hanya terjadi pada hasil $\{GGG\}$, sehingga $n(X = 3) = 1$.
$$P(X = 3) = \frac{1}{8}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-d-easy-bt01-010
*variasi (angka) | C2 | 2 langkah | jenis: peluang binomial kuis*

Sebuah kuis terdiri dari 3 butir pertanyaan bertipe benar atau salah. Seseorang menjawab seluruh soal secara acak dengan peluang menjawab benar pada tiap soal adalah $\frac{1}{2}$. Jika variabel acak $X$ menyatakan banyak soal yang dijawab dengan benar, nilai dari $P(X = 2)$ adalah ....

- A. $\frac{2}{3}$  
  <sub>Salah: Menghitung perbandingan 2 benar dari total 3 soal tanpa memperhitungkan peluang ruang sampel acak.</sub>
- B. $\frac{1}{8}$  
  <sub>Salah: Hanya menghitung satu kejadian spesifik tanpa memperhitungkan faktor kombinasi $\binom{3}{2}$.</sub>
- C. $\frac{2}{8}$  
  <sub>Salah: Keliru menganggap ada 2 cara memilih karena yang dicari adalah 2 jawaban benar.</sub>
- **D. $\frac{3}{8}$** ✅  
  <sub>Benar: Banyaknya cara memilih 2 soal benar dari 3 soal adalah $\binom{3}{2} = 3$, dan tiap kombinasi memiliki peluang $\left(\frac{1}{2}\right)^3 = \frac{1}{8}$, sehingga totalnya $\frac{3}{8}$.</sub>

**Pembahasan:** Ruang sampel penulisan jawaban terdiri dari $2^3 = 8$ kemungkinan dengan bobot peluang sama.
Banyak kombinasi mendapatkan tepat 2 jawaban benar adalah $\binom{3}{2} = \frac{3!}{2!1!} = 3$ cara (BBS, BSB, SBB).
Jadi, peluangnya adalah:
$$P(X = 2) = \frac{3}{8}$$
**Acuan:** pretest — kelas12_tl-b04-p0264-latihan-soal-fungsi-peluang-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-d-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: peluang hipergeometrik bola*

Sebuah kotak berisi 4 bola merah dan 2 bola putih. Dua bola diambil sekaligus secara acak. Jika variabel acak $X$ menyatakan banyak bola putih yang terambil, nilai peluang $P(X = 1)$ adalah ....

- **A. $\frac{8}{15}$** ✅  
  <sub>Benar: Banyak kejadian memilih 1 bola putih dan 1 bola merah adalah $\binom{2}{1} \times \binom{4}{1} = 2 \times 4 = 8$. Total cara memilih 2 bola dari 6 bola adalah $\binom{6}{2} = 15$. Jadi, peluangnya $\frac{8}{15}$.</sub>
- B. $\frac{1}{3}$  
  <sub>Salah: Keliru membagi banyak bola putih terhadap total bola, yaitu $\frac{2}{6} = \frac{1}{3}$.</sub>
- C. $\frac{2}{15}$  
  <sub>Salah: Hanya menghitung $\binom{2}{1} = 2$ pada pembilang tanpa mengalikannya dengan cara memilih bola merah.</sub>
- D. $\frac{4}{15}$  
  <sub>Salah: Hanya menghitung $\binom{4}{1} = 4$ pada pembilang tanpa mengalikannya dengan cara memilih bola putih.</sub>

**Pembahasan:** Total bola = $4 + 2 = 6$.
Jumlah kemungkinan pengambilan 2 bola dari 6 bola:
$$n(S) = \binom{6}{2} = \frac{6 \times 5}{2} = 15$$
Kejadian $X = 1$ berarti terambil 1 bola putih dan 1 bola merah:
$$n(X = 1) = \binom{2}{1} \times \binom{4}{1} = 2 \times 4 = 8$$
Dengan demikian:
$$P(X = 1) = \frac{8}{15}$$
**Acuan:** siswa — siswa hal.259 Contoh Soal 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-d-easy-bt01-012
*orisinal | C2 | 1 langkah | jenis: penentuan parameter distribusi peluang*

| $X = x$ | 0 | 1 | 2 |
| :--- | :---: | :---: | :---: |
| $P(X = x)$ | 0,25 | $c$ | 0,35 |

Tabel di atas menyajikan fungsi peluang untuk suatu variabel acak diskret $X$. Nilai $c$ yang memenuhi fungsi peluang tersebut adalah ....

- A. 0,60  
  <sub>Salah: Hanya menjumlahkan peluang yang ada ($0,25 + 0,35$) tanpa mengurangkannya dari 1.</sub>
- B. 0,50  
  <sub>Salah: Mengira nilai tengah distribusi peluang selalu merupakan rata-rata atau setengah dari total.</sub>
- **C. 0,40** ✅  
  <sub>Benar: Jumlah seluruh peluang harus bernilai 1, sehingga $c = 1 - (0,25 + 0,35) = 1 - 0,60 = 0,40$.</sub>
- D. 0,30  
  <sub>Salah: Salah menjumlahkan 0,25 dan 0,35 menjadi 0,70 sehingga memperoleh hasil $1 - 0,70 = 0,30$.</sub>

**Pembahasan:** Berdasarkan syarat fungsi peluang diskret, jumlah seluruh peluang harus sama dengan 1:
$$\sum f(x) = 1$$
$$P(X = 0) + P(X = 1) + P(X = 2) = 1$$
$$0,25 + c + 0,35 = 1$$
$$c + 0,60 = 1$$
$$c = 0,40$$
**Acuan:** siswa — siswa hal.259

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-d-easy-bt01-013
*orisinal | C1 | 1 langkah | jenis: himpunan nilai variabel acak diskret*

Dalam suatu ulangan harian, seorang siswa mengerjakan 4 butir soal. Jika variabel acak $X$ menyatakan banyak soal yang dijawab salah oleh siswa tersebut, himpunan seluruh nilai yang mungkin untuk variabel acak $X$ adalah ....

- A. $\{1, 2, 3, 4\}$  
  <sub>Salah: Lupa menyertakan nilai 0 saat tidak ada jawaban yang salah sama sekali.</sub>
- **B. $\{0, 1, 2, 3, 4\}$** ✅  
  <sub>Benar: Banyaknya jawaban salah yang dapat terjadi berkisar dari tidak ada yang salah (0) sampai semuanya salah (4).</sub>
- C. $\{0, 1, 2, 3\}$  
  <sub>Salah: Lupa menyertakan nilai maksimum 4 saat seluruh butir soal dijawab salah.</sub>
- D. $\{1, 2, 3, 4, 5\}$  
  <sub>Salah: Keliru menganggap banyak kemungkinan nilai sama dengan jumlah soal ditambah satu yang dimulai dari 1.</sub>

**Pembahasan:** Banyaknya soal yang dijawab salah dapat berupa:
- Tidak ada yang salah sama sekali ($X = 0$)
- Tepat 1 soal salah ($X = 1$)
- Tepat 2 soal salah ($X = 2$)
- Tepat 3 soal salah ($X = 3$)
- Semua soal salah ($X = 4$)

Jadi, himpunan seluruh nilai yang mungkin untuk variabel acak $X$ adalah $\{0, 1, 2, 3, 4\}$.
**Acuan:** siswa — siswa hal.260

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-d-easy-bt01-014
*variasi (angka) | C2 | 2 langkah | jenis: peluang variabel acak cacat*

Pabrik ponsel Sigma mengirim 7 ponsel pintar ke sebuah toko elektronik, dan ternyata sebanyak 3 ponsel pintar cacat. Beta membeli 3 ponsel pintar dari toko tersebut secara acak. Jika variabel acak $Y$ menyatakan banyak ponsel pintar cacat yang dibeli Beta, nilai peluang $P(Y = 1)$ adalah …

- A. $\frac{1}{35}$  
  <sub>Salah: Hanya menghitung peluang untuk 3 ponsel cacat terpilih semua $\binom{3}{3} = 1$.</sub>
- **B. $\frac{18}{35}$** ✅  
  <sub>Benar: Total cara memilih 3 ponsel dari 7 ponsel adalah $\binom{7}{3} = 35$. Banyak cara memilih 1 ponsel cacat dari 3 ponsel cacat dan 2 ponsel baik dari 4 ponsel baik adalah $\binom{3}{1} \times \binom{4}{2} = 3 \times 6 = 18$. Jadi, $P(Y = 1) = \frac{18}{35}$.</sub>
- C. $\frac{12}{35}$  
  <sub>Salah: Salah menghitung $\binom{4}{2}$ menjadi 4 sehingga pembilang menjadi $3 \times 4 = 12$.</sub>
- D. $\frac{9}{35}$  
  <sub>Salah: Menghitung $\binom{3}{1} \times 3 = 9$ karena salah menentukan jumlah ponsel baik.</sub>

**Pembahasan:** Diketahui total ponsel $n = 7$, ponsel cacat $= 3$, dan ponsel baik $= 4$. Beta membeli $3$ ponsel.
Total kemungkinan memilih 3 ponsel:
$$n(S) = \binom{7}{3} = \frac{7 \times 6 \times 5}{3 \times 2 \times 1} = 35$$

Banyak cara terpilih 1 ponsel cacat ($Y = 1$) dan 2 ponsel baik:
$$n(Y = 1) = \binom{3}{1} \times \binom{4}{2} = 3 \times \frac{4 \times 3}{2 \times 1} = 3 \times 6 = 18$$

Sehingga diperoleh nilai peluang:
$$P(Y = 1) = \frac{n(Y = 1)}{n(S)} = \frac{18}{35}$$
**Acuan:** siswa — siswa hal.261 Ayo Mencoba 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-d-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: peluang variabel acak dua bola*

Dalam sebuah kotak terdapat 6 bola hijau dan 4 bola kuning. Dari kotak tersebut diambil 2 bola secara acak sekaligus. Jika variabel acak $X$ menyatakan banyak bola kuning yang terambil, nilai dari $P(X = 2)$ adalah …

- A. $\frac{4}{15}$  
  <sub>Salah: Salah menghitung banyak cara memilih 2 bola kuning sebagai $\binom{4}{1} \times 3 = 12$ sehingga $12/45 = 4/15$.</sub>
- B. $\frac{8}{15}$  
  <sub>Salah: Menghitung peluang terambil tepat 1 bola kuning, yaitu $\binom{4}{1}\binom{6}{1}/45 = 24/45 = 8/15$.</sub>
- **C. $\frac{2}{15}$** ✅  
  <sub>Benar: Banyak cara memilih 2 bola dari 10 bola adalah $\binom{10}{2} = 45$. Banyak cara memilih 2 bola kuning dari 4 bola kuning adalah $\binom{4}{2} = 6$. Maka, $P(X = 2) = \frac{6}{45} = \frac{2}{15}$.</sub>
- D. $\frac{1}{15}$  
  <sub>Salah: Hanya menghitung 1 kemungkinan dibagi total sampel per kelompok atau salah membagi.</sub>

**Pembahasan:** Jumlah seluruh bola dalam kotak $= 6 + 4 = 10$ bola.
Banyak cara mengambil 2 bola sekaligus dari 10 bola:
$$n(S) = \binom{10}{2} = \frac{10 \times 9}{2 \times 1} = 45$$

Kejadian $X = 2$ berarti terambil 2 bola kuning dari 4 bola kuning yang tersedia:
$$n(X = 2) = \binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6$$

Maka nilai peluangnya adalah:
$$P(X = 2) = \frac{n(X = 2)}{n(S)} = \frac{6}{45} = \frac{2}{15}$$
**Acuan:** siswa — siswa hal.259 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-d-easy-bt01-016
*variasi (konteks) | C2 | 2 langkah | jenis: peluang variabel acak buah*

Sebuah keranjang memuat 8 buah mangga, dan 2 di antaranya masih mentah. Pak Made memilih 3 buah mangga secara acak sekaligus. Jika variabel acak $K$ menyatakan banyak mangga mentah yang terpilih, nilai dari $P(K = 0)$ adalah …

- A. $\frac{15}{28}$  
  <sub>Salah: Menghitung peluang $P(K = 1)$, yaitu $\binom{2}{1}\binom{6}{2}/56 = 30/56 = 15/28$.</sub>
- **B. $\frac{5}{14}$** ✅  
  <sub>Benar: Total mangga $= 8$ (2 mentah, 6 matang). Memilih 3 mangga menghasilkan $\binom{8}{3} = 56$ cara. Terpilih 0 mangga mentah berarti ketiga mangga matang, yaitu $\binom{6}{3} = 20$ cara. Peluangnya $\frac{20}{56} = \frac{5}{14}$.</sub>
- C. $\frac{9}{14}$  
  <sub>Salah: Menghitung komplemen $1 - P(K = 0) = 1 - 5/14 = 9/14$.</sub>
- D. $\frac{3}{14}$  
  <sub>Salah: Salah menghitung kombinasi mangga matang menjadi 12 sehingga diperoleh $12/56 = 3/14$.</sub>

**Pembahasan:** Diketahui total mangga $= 8$, mangga mentah $= 2$, dan mangga matang $= 6$.
Pak Made memilih 3 mangga, sehingga ruang sampel:
$$n(S) = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

Variabel acak $K = 0$ artinya tidak ada mangga mentah yang terambil, sehingga ketiganya adalah mangga matang:
$$n(K = 0) = \binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$$

Nilai peluangnya:
$$P(K = 0) = \frac{20}{56} = \frac{5}{14}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-d-easy-bt01-017
*variasi (angka) | C2 | 2 langkah | jenis: peluang variabel acak kelereng tiga warna*

Sebuah kantong berisi 7 bola putih, 1 bola hitam, dan 4 bola merah. Sebanyak 2 bola diambil secara acak sekaligus. Jika variabel acak $M$ menyatakan banyak bola merah yang terambil, nilai peluang $P(M = 1)$ adalah …

- A. $\frac{17}{33}$  
  <sub>Salah: Menghitung komplemen dari jawaban yang benar, yaitu $1 - 16/33 = 17/33$.</sub>
- B. $\frac{1}{11}$  
  <sub>Salah: Menghitung peluang terambilnya 2 bola merah ($M = 2$), yaitu $\binom{4}{2}/66 = 6/66 = 1/11$.</sub>
- **C. $\frac{16}{33}$** ✅  
  <sub>Benar: Total bola $= 7 + 1 + 4 = 12$. Banyak cara memilih 2 bola adalah $\binom{12}{2} = 66$. Terambil 1 bola merah dan 1 bola bukan merah (dari 8 bola) adalah $\binom{4}{1} \times \binom{8}{1} = 32$. Maka peluangnya $\frac{32}{66} = \frac{16}{33}$.</sub>
- D. $\frac{8}{33}$  
  <sub>Salah: Lupa mengalikan dengan kombinasi bola merah sehingga hanya menghitung $16/66$ atau salah membagi.</sub>

**Pembahasan:** Total bola dalam kantong adalah $7 + 1 + 4 = 12$ bola.
Bola bukan merah $= 7 + 1 = 8$ bola, dan bola merah $= 4$ bola.

Banyak cara mengambil 2 bola dari 12 bola:
$$n(S) = \binom{12}{2} = \frac{12 \times 11}{2 \times 1} = 66$$

Banyak cara terambil 1 bola merah ($M = 1$) dan 1 bola bukan merah:
$$n(M = 1) = \binom{4}{1} \times \binom{8}{1} = 4 \times 8 = 32$$

Sehingga nilai peluangnya:
$$P(M = 1) = \frac{32}{66} = \frac{16}{33}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-d-easy-bt01-018
*orisinal | C2 | 1 langkah | jenis: peluang kumulatif distribusi diskret*

| $X = x$ | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: |
| $P(X = x)$ | $\frac{1}{10}$ | $\frac{2}{10}$ | $\frac{3}{10}$ | $\frac{4}{10}$ |

Tabel di atas menyajikan distribusi peluang dari suatu variabel acak diskret $X$. Nilai dari $P(X > 2)$ adalah …

- **A. $\frac{7}{10}$** ✅  
  <sub>Benar: $P(X > 2) = P(X = 3) + P(X = 4) = \frac{3}{10} + \frac{4}{10} = \frac{7}{10}$.</sub>
- B. $\frac{9}{10}$  
  <sub>Salah: Menghitung $P(X \ge 2)$ sehingga menyertakan nilai $P(X = 2)$.</sub>
- C. $\frac{4}{10}$  
  <sub>Salah: Hanya mengambil nilai $P(X = 4)$.</sub>
- D. $\frac{3}{10}$  
  <sub>Salah: Hanya mengambil nilai $P(X = 3)$ dan mengabaikan $P(X = 4)$.</sub>

**Pembahasan:** Berdasarkan tabel distribusi peluang, nilai-nilai $X$ yang memenuhi pertidaksamaan $X > 2$ adalah $x = 3$ dan $x = 4$.

Maka:
$$P(X > 2) = P(X = 3) + P(X = 4) = \frac{3}{10} + \frac{4}{10} = \frac{7}{10}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-d-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: distribusi peluang seragam dadu*

Sebuah dadu setimbang bersisi enam dilempar satu kali. Jika variabel acak $X$ menyatakan mata dadu yang muncul, yaitu $X \in \{1, 2, 3, 4, 5, 6\}$, nilai dari $P(X = 4)$ adalah …

- **A. $\frac{1}{6}$** ✅  
  <sub>Benar: Masing-masing dari 6 mata dadu setimbang memiliki peluang muncul yang sama, yaitu $P(X = x) = \frac{1}{6}$ untuk setiap $x \in \{1, 2, 3, 4, 5, 6\}$.</sub>
- B. $\frac{2}{3}$  
  <sub>Salah: Menghitung keliru dengan membagi nilai $x$ dengan jumlah sisi dadu, yaitu $\frac{4}{6} = \frac{2}{3}$.</sub>
- C. $\frac{1}{4}$  
  <sub>Salah: Membagi 1 dengan nilai mata dadu yang ditanyakan ($x = 4$).</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: Menghitung peluang komplemen yaitu peluang muncul selain mata 4 ($P(X \ne 4)$).</sub>

**Pembahasan:** Ruang sampel pelemparan sebuah dadu bersisi enam adalah $S = \{1, 2, 3, 4, 5, 6\}$ dengan banyak anggota $n(S) = 6$.
Karena dadu setimbang, setiap mata dadu memiliki kemungkinan yang sama untuk muncul.
Oleh karena itu, fungsi peluangnya adalah:
$$P(X = x) = \frac{1}{6}, \quad \text{untuk } x = 1, 2, 3, 4, 5, 6$$
Dengan demikian, nilai $P(X = 4) = \frac{1}{6}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-d-easy-bt01-020
*variasi (angka) | C2 | 2 langkah | jenis: evaluasi fungsi peluang diskret*

Diketahui fungsi peluang dari suatu variabel acak diskret $X$ dinyatakan oleh:
$$f(x) = \begin{cases} \frac{x}{20}, & \text{untuk } x = 4, 7, 9 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \ge 7)$ adalah ....

- A. $\frac{9}{20}$  
  <sub>Salah: Mengira tanda pertidaksamaan adalah strictly greater than, $P(X > 7) = P(X = 9) = \frac{9}{20}$.</sub>
- B. $\frac{11}{20}$  
  <sub>Salah: Tertukar menghitung $P(X \le 7) = P(X = 4) + P(X = 7) = \frac{4+7}{20} = \frac{11}{20}$.</sub>
- C. $\frac{7}{20}$  
  <sub>Salah: Hanya menghitung nilai $P(X = 7)$ tanpa menjumlahkan dengan nilai $x$ yang lebih besar.</sub>
- **D. $\frac{4}{5}$** ✅  
  <sub>Benar: $P(X \ge 7) = P(X = 7) + P(X = 9) = \frac{7}{20} + \frac{9}{20} = \frac{16}{20} = \frac{4}{5}$.</sub>

**Pembahasan:** Nilai variabel acak diskret yang memenuhi kondisi $X \ge 7$ adalah $x = 7$ dan $x = 9$.
Maka peluangnya adalah:
$$P(X \ge 7) = f(7) + f(9) = \frac{7}{20} + \frac{9}{20} = \frac{16}{20} = \frac{4}{5}$$
Jadi, nilai dari $P(X \ge 7)$ adalah $\frac{4}{5}$.
**Acuan:** siswa — siswa hal.263 Latihan Soal Fungsi Peluang

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-d-medium-bt01-001
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi peluang hipergeometrik*

Sebuah panitia menyediakan 9 amplop tertutup yang terdiri atas 4 amplop berisi voucer belanja dan 5 amplop berisi kertas kosong. Seseorang dipersilakan mengambil 3 amplop secara acak sekaligus. Jika variabel acak $X$ menyatakan banyak amplop berisi voucer belanja yang terambil, nilai dari $P(X = 2)$ adalah ....

- A. $\frac{15}{28}$  
  <sub>Salah: Keliru menghitung untuk kejadian $X = 1$, yaitu $\binom{4}{1} \times \binom{5}{2} / 84 = 40/84$, disederhanakan keliru.</sub>
- B. $\frac{10}{21}$  
  <sub>Salah: Keliru menghitung kombinasi semesta sebagai $\binom{9}{2} = 36$ dan kejadian sebagai $\binom{4}{2} \times \binom{5}{1} = 30$, lalu disederhanakan salah.</sub>
- C. $\frac{1}{14}$  
  <sub>Salah: Hanya menghitung kemungkinan terambil 2 amplop voucer tanpa mengalikan sisa 1 amplop kosong, yaitu $6/84 = 1/14$.</sub>
- **D. $\frac{5}{14}$** ✅  
  <sub>Benar: $n(S) = \binom{9}{3} = 84$, $n(X = 2) = \binom{4}{2} \times \binom{5}{1} = 6 \times 5 = 30$, sehingga $P(X = 2) = \frac{30}{84} = \frac{5}{14}$.</sub>

**Pembahasan:** Langkah 1: Tentukan banyak anggota ruang sampel memilih 3 amplop dari total 9 amplop:
$$n(S) = \binom{9}{3} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = 84$$

Langkah 2: Tentukan banyak cara memilih 2 amplop voucer dari 4 amplop voucer dan 1 amplop kosong dari 5 amplop kosong:
$$n(X = 2) = \binom{4}{2} \times \binom{5}{1} = \frac{4 \times 3}{2 \times 1} \times 5 = 6 \times 5 = 30$$

Langkah 3: Hitung nilai peluang $P(X = 2)$:
$$P(X = 2) = \frac{n(X = 2)}{n(S)} = \frac{30}{84} = \frac{5}{14}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-d-medium-bt01-002
*orisinal | C4 | 3 langkah | jenis: parameter fungsi peluang*

Diketahui fungsi peluang dari suatu variabel acak diskret $X$ dinyatakan oleh:
$$f(x) = \begin{cases} k(x^2 - 1), & \text{untuk } x = 2, 3, 4 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X > 2)$ adalah ....

- A. $\frac{3}{26}$  
  <sub>Salah: Menghitung $P(X = 2) = f(2)$ alih-alih $P(X > 2)$.</sub>
- **B. $\frac{23}{26}$** ✅  
  <sub>Benar: $f(2)+f(3)+f(4) = k(3+8+15) = 26k = 1 \Rightarrow k = \frac{1}{26}$. Maka $P(X > 2) = f(3) + f(4) = 23k = \frac{23}{26}$.</sub>
- C. $\frac{15}{26}$  
  <sub>Salah: Hanya menghitung nilai untuk $f(4) = 15k = 15/26$.</sub>
- D. $\frac{4}{13}$  
  <sub>Salah: Hanya menghitung nilai untuk $f(3) = 8k = 8/26 = 4/13$.</sub>

**Pembahasan:** Langkah 1: Berdasarkan syarat fungsi peluang, $\sum f(x) = 1$.
$$f(2) + f(3) + f(4) = 1$$
$$k(2^2 - 1) + k(3^2 - 1) + k(4^2 - 1) = 1$$
$$k(3) + k(8) + k(15) = 1$$
$$26k = 1 \implies k = \frac{1}{26}$$

Langkah 2: Tentukan nilai yang memenuhi $X > 2$, yaitu $x = 3$ dan $x = 4$.

Langkah 3: Hitung $P(X > 2)$:
$$P(X > 2) = f(3) + f(4) = 8k + 15k = 23k = 23 \times \frac{1}{26} = \frac{23}{26}$$
**Acuan:** siswa — siswa hal.259

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-d-medium-bt01-003
*orisinal | C3 | 3 langkah | jenis: fungsi peluang variabel acak diskret*

Dua buah dadu setimbang bersisi enam dilemparkan secara bersamaan satu kali. Misalkan variabel acak $X$ menyatakan selisih mutlak mata dadu yang muncul pada kedua dadu tersebut. Nilai dari $P(X \ge 4)$ adalah ....

- A. $\frac{5}{18}$  
  <sub>Salah: Salah menghitung pasangan selisih 4 sebagai tidak memperhitungkan urutan sehingga hanya memperoleh 2 pasangan dan salah menghitung total peluang.</sub>
- B. $\frac{1}{9}$  
  <sub>Salah: Hanya menghitung kejadian selisih mutlak 4 saja ($4/36 = 1/9$) dan melupakan selisih mutlak 5.</sub>
- C. $\frac{1}{18}$  
  <sub>Salah: Hanya menghitung kejadian selisih mutlak 5 saja ($2/36 = 1/18$).</sub>
- **D. $\frac{1}{6}$** ✅  
  <sub>Benar: Ruang sampel $n(S) = 36$. Titik sampel dengan selisih mutlak $\ge 4$ ada 6 buah, sehingga $P(X \ge 4) = \frac{6}{36} = \frac{1}{6}$.</sub>

**Pembahasan:** Langkah 1: Menentukan total kemungkinan hasil pelemparan dua dadu:
$$n(S) = 6 \times 6 = 36$$

Langkah 2: Menentukan pasangan mata dadu $(a, b)$ yang menghasilkan selisih mutlak $|a - b| \ge 4$:
- Untuk selisih mutlak $= 4$: $(1, 5), (5, 1), (2, 6), (6, 2)$ $\rightarrow 4$ pasangan.
- Untuk selisih mutlak $= 5$: $(1, 6), (6, 1)$ $\rightarrow 2$ pasangan.
Total kejadian = $4 + 2 = 6$ pasangan.

Langkah 3: Menghitung peluang $P(X \ge 4)$:
$$P(X \ge 4) = \frac{6}{36} = \frac{1}{6}$$
**Acuan:** siswa — siswa hal.257

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-d-medium-bt01-004
*orisinal | C3 | 2 langkah | jenis: nilai peluang variabel acak tabel*

| $W = w$ | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: |
| $P(W = w)$ | $2a$ | $3a$ | $0,25$ | $0,15$ |

Tabel di atas menyajikan distribusi peluang untuk variabel acak diskret $W$. Nilai dari $P(2 \le W \le 4)$ adalah ....

- A. 0,24  
  <sub>Salah: Menghitung $P(W = 1) = 2a = 0,24$, bukan $P(2 \le W \le 4)$.</sub>
- B. 0,40  
  <sub>Salah: Hanya menjumlahkan nilai numerik yang sudah diketahui, yaitu $P(W = 3) + P(W = 4) = 0,25 + 0,15 = 0,40$.</sub>
- **C. 0,76** ✅  
  <sub>Benar: $\sum P = 5a + 0,40 = 1 \Rightarrow a = 0,12$. Maka $P(2 \le W \le 4) = 1 - P(W = 1) = 1 - 2(0,12) = 0,76$.</sub>
- D. 0,64  
  <sub>Salah: Hanya menghitung $P(W = 2) + P(W = 3) = 3(0,12) + 0,25 = 0,61$ lalu dibulatkan secara keliru atau melewatkan $W = 4$.</sub>

**Pembahasan:** Langkah 1: Sifat fungsi peluang mensyaratkan jumlah semua peluang bernilai 1:
$$\sum_{w=1}^{4} P(W = w) = 1$$
$$2a + 3a + 0,25 + 0,15 = 1$$
$$5a + 0,40 = 1$$
$$5a = 0,60 \implies a = 0,12$$

Langkah 2: Hitung nilai $P(2 \le W \le 4)$:
$$P(2 \le W \le 4) = 1 - P(W = 1) = 1 - 2a = 1 - 2(0,12) = 1 - 0,24 = 0,76$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-d-medium-bt01-005
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi peluang hipergeometrik*

Sebuah kotak perkakas memuat 8 buah obeng, dengan 3 di antaranya bermata minus dan sisanya bermata plus. Seorang teknisi mengambil 3 buah obeng secara acak sekaligus dari kotak tersebut. Jika $X$ menyatakan banyak obeng bermata minus yang terambil, nilai dari $P(X = 2)$ adalah ....

- A. $\frac{3}{56}$  
  <sub>Salah: Lupa mengalikan dengan cara memilih obeng bermata plus $\binom{5}{1}$, hanya menghitung $\frac{\binom{3}{2}}{\binom{8}{3}} = \frac{3}{56}$.</sub>
- **B. $\frac{15}{56}$** ✅  
  <sub>Benar: Banyak cara memilih total 3 obeng dari 8 adalah $\binom{8}{3} = 56$. Banyak cara memilih 2 obeng minus dari 3 dan 1 obeng plus dari 5 adalah $\binom{3}{2} \times \binom{5}{1} = 3 \times 5 = 15$. Peluangnya $\frac{15}{56}$.</sub>
- C. $\frac{5}{14}$  
  <sub>Salah: Keliru menghitung kombinasi $P(X = 1) = \frac{\binom{3}{1}\binom{5}{2}}{\binom{8}{3}} = \frac{30}{56} = \frac{15}{28}$ lalu membaginya salah sehingga menghasilkan $\frac{5}{14}$.</sub>
- D. $\frac{5}{28}$  
  <sub>Salah: Menghitung $\frac{\binom{3}{2}}{\binom{8}{3}} = \frac{3}{56}$ atau salah hitung perkalian kombinasi menjadi $10/56 = 5/28$.</sub>

**Pembahasan:** Diketahui:
- Total obeng $= 8$
- Banyak obeng minus $= 3$
- Banyak obeng plus $= 8 - 3 = 5$
- Diambil 3 obeng sekaligus.

Banyak cara mengambil 3 obeng dari 8 obeng:
$$n(S) = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56$$

Kejadian $X = 2$ berarti terambil 2 obeng minus dan 1 obeng plus:
$$n(X = 2) = \binom{3}{2} \times \binom{5}{1} = 3 \times 5 = 15$$

Maka, nilai peluangnya adalah:
$$P(X = 2) = \frac{n(X = 2)}{n(S)} = \frac{15}{56}$$

Jadi, nilai dari $P(X = 2)$ adalah $\frac{15}{56}$.
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-d-medium-bt01-006
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi binomial sederhana*

Sebuah keluarga merencanakan untuk memiliki 4 orang anak. Asumsikan peluang kelahiran anak laki-laki dan anak perempuan adalah sama, yaitu $\frac{1}{2}$. Jika $X$ menyatakan variabel acak banyaknya anak perempuan dalam keluarga tersebut, nilai dari $P(X = 3)$ adalah ....

- A. $\frac{1}{8}$  
  <sub>Salah: Hanya menghitung $\left(\frac{1}{2}\right)^3 = \frac{1}{8}$ tanpa memperhatikan total 4 kelahiran dan faktor kombinasi.</sub>
- **B. $\frac{1}{4}$** ✅  
  <sub>Benar: $P(X = 3) = \binom{4}{3} \left(\frac{1}{2}\right)^3 \left(\frac{1}{2}\right)^1 = 4 \times \frac{1}{16} = \frac{4}{16} = \frac{1}{4}$.</sub>
- C. $\frac{1}{16}$  
  <sub>Salah: Hanya menghitung salah satu urutan tanpa memperhitungkan banyaknya susunan $\binom{4}{3}$, yaitu $\frac{1}{16}$.</sub>
- D. $\frac{3}{8}$  
  <sub>Salah: Tertukar dengan peluang memperoleh 2 anak perempuan ($X = 2$), yaitu $\binom{4}{2}/16 = 6/16 = 3/8$.</sub>

**Pembahasan:** Setiap kelahiran memiliki 2 kemungkinan (Laki-laki atau Perempuan) dengan peluang masing-masing $\frac{1}{2}$.
Total kemungkinan susunan jenis kelamin dari 4 orang anak adalah $2^4 = 16$.

Variabel acak $X$ menyatakan banyaknya anak perempuan. Nilai $X = 3$ berarti terdapat 3 anak perempuan dan 1 anak laki-laki.
Banyaknya susunan yang mungkin adalah:
$$\binom{4}{3} = 4$$

Susunan tersebut adalah: (P, P, P, L), (P, P, L, P), (P, L, P, P), (L, P, P, P).

Peluang terjadinya $X = 3$ adalah:
$$P(X = 3) = \frac{\binom{4}{3}}{16} = \frac{4}{16} = \frac{1}{4}$$

Jadi, nilai dari $P(X = 3)$ adalah $\frac{1}{4}$.
**Acuan:** pretest — kelas12_tl-b04-p0264-latihan-soal-fungsi-peluang-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-d-medium-bt01-007
*orisinal | C4 | 3 langkah | jenis: syarat keabsahan fungsi peluang*  **[warning validator]**

Fungsi peluang suatu variabel acak diskret $X$ didefinisikan oleh:
$$f(x) = \begin{cases} c(5 - x), & \text{untuk } x = 1, 2, 3, 4 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \le 2)$ adalah ....

- A. $\frac{2}{5}$  
  <sub>Salah: Hanya menghitung nilai dari $f(1) = \frac{4}{10} = \frac{2}{5}$ tanpa menjumlahkan dengan $f(2)$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Salah menjumlahkan koefisien $c$, mengira totalnya 8 sehingga $c = \frac{1}{8}$ dan $f(1)+f(2) = \frac{4}{8} = \frac{1}{2}$.</sub>
- C. $\frac{3}{10}$  
  <sub>Salah: Menghitung $P(X > 2) = f(3) + f(4) = \frac{2}{10} + \frac{1}{10} = \frac{3}{10}$ (kebalikan dari pertidaksamaan).</sub>
- **D. $\frac{7}{10}$** ✅  
  <sub>Benar: Total $\sum f(x) = c(4 + 3 + 2 + 1) = 10c = 1 \implies c = \frac{1}{10}$. Maka $P(X \le 2) = f(1) + f(2) = \frac{4}{10} + \frac{3}{10} = \frac{7}{10}$.</sub>

**Pembahasan:** Agar $f(x)$ merupakan fungsi peluang diskret, syarat $\sum f(x) = 1$ harus dipenuhi:
$$\sum_{x=1}^{4} c(5 - x) = 1$$
$$c(5 - 1) + c(5 - 2) + c(5 - 3) + c(5 - 4) = 1$$
$$c(4 + 3 + 2 + 1) = 1$$
$$10c = 1 \implies c = \frac{1}{10}$$

Selanjutnya, tentukan nilai $P(X \le 2)$:
$$P(X \le 2) = f(1) + f(2)$$
$$P(X \le 2) = \frac{1}{10}(4) + \frac{1}{10}(3) = \frac{4}{10} + \frac{3}{10} = \frac{7}{10}$$

Jadi, nilai dari $P(X \le 2)$ adalah $\frac{7}{10}$.
**Acuan:** siswa — siswa hal.259
**Warning:** kelas12_tl-b04-d-medium-bt01-007 sangat mirip dengan kelas12_tl-b04-d-medium-bt01-016 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-d-medium-bt01-008
*orisinal | C4 | 3 langkah | jenis: distribusi peluang jumlah mata dadu*

Dua buah dadu setimbang bersisi enam dilempar bersamaan sebanyak satu kali. Misalkan $S$ adalah variabel acak yang menyatakan jumlah kedua mata dadu yang muncul. Nilai dari $P(S > 9)$ adalah ....

- A. $\frac{5}{18}$  
  <sub>Salah: Keliru memasukkan jumlah 9 yang memiliki 4 cara, sehingga $(4 + 6)/36 = 10/36 = 5/18$.</sub>
- B. $\frac{1}{12}$  
  <sub>Salah: Hanya menghitung untuk jumlah 10, yaitu $\frac{3}{36} = \frac{1}{12}$, melupakan jumlah 11 dan 12.</sub>
- **C. $\frac{1}{6}$** ✅  
  <sub>Benar: Pasangan mata dadu berjumlah > 9 adalah jumlah 10 (3 cara), jumlah 11 (2 cara), dan jumlah 12 (1 cara). Total ada $3 + 2 + 1 = 6$ cara dari 36 kemungkinan. Peluangnya $\frac{6}{36} = \frac{1}{6}$.</sub>
- D. $\frac{5}{36}$  
  <sub>Salah: Salah mencacah banyak titik sampel untuk jumlah 10, 11, dan 12 sehingga totalnya dihitung 5 bukan 6.</sub>

**Pembahasan:** Pada pelemparan dua buah dadu, total ruang sampel adalah $n = 6 \times 6 = 36$.

Variabel acak $S$ menyatakan jumlah kedua mata dadu. Kejadian $S > 9$ mencakup $S = 10$, $S = 11$, dan $S = 12$.

Titik sampel untuk masing-masing nilai $S$:
- $S = 10$: $(4,6), (5,5), (6,4)$ $\rightarrow 3$ cara
- $S = 11$: $(5,6), (6,5)$ $\rightarrow 2$ cara
- $S = 12$: $(6,6)$ $\rightarrow 1$ cara

Total titik sampel untuk $S > 9$:
$$n(S > 9) = 3 + 2 + 1 = 6$$

Maka peluangnya adalah:
$$P(S > 9) = \frac{6}{36} = \frac{1}{6}$$

Jadi, nilai dari $P(S > 9)$ adalah $\frac{1}{6}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-d-medium-bt01-009
*variasi (angka) | C3 | 3 langkah | jenis: distribusi peluang pengambilan tanpa pengembalian*

Pabrik ponsel Sigma mengirim 12 ponsel pintar ke sebuah toko elektronik. Ternyata sebanyak 5 ponsel pintar di antaranya cacat. Beta membeli 3 ponsel pintar dari toko tersebut secara acak. Jika $Y$ adalah variabel acak yang menyatakan banyak ponsel pintar cacat yang dibeli Beta, nilai dari $P(Y = 2)$ adalah ....

- A. $\frac{7}{11}$  
  <sub>Salah: Siswa salah menghitung ruang sampel menjadi $\binom{12}{2} = 66$ lalu memperoleh $\frac{42}{66} = \frac{7}{11}$.</sub>
- B. $\frac{5}{22}$  
  <sub>Salah: Siswa keliru menghitung banyak ponsel baik yang tersedia sebagai 5 sehingga $\frac{10 \times 5}{220} = \frac{50}{220} = \frac{5}{22}$.</sub>
- C. $\frac{7}{66}$  
  <sub>Salah: Siswa menghitung peluang urutan tunggal $\frac{5}{12} \times \frac{4}{11} \times \frac{7}{10} = \frac{7}{66}$ tanpa mengalikan dengan faktor kombinasi 3 susunan.</sub>
- **D. $\frac{7}{22}$** ✅  
  <sub>Benar: Banyak cara memilih 3 dari 12 ponsel adalah $\binom{12}{3} = 220$. Kejadian $Y = 2$ berarti memilih 2 ponsel cacat dari 5 dan 1 ponsel baik dari 7, yaitu $\binom{5}{2} \times \binom{7}{1} = 10 \times 7 = 70$. Peluangnya adalah $\frac{70}{220} = \frac{7}{22}$.</sub>

**Pembahasan:** Diketahui:
- Total ponsel = $12$
- Ponsel cacat = $5$
- Ponsel tidak cacat = $12 - 5 = 7$
- Diambil = $3$ ponsel

1. Menentukan ukuran ruang sampel:
$$n(S) = \binom{12}{3} = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$$

2. Menentukan banyak cara memilih $Y = 2$ (2 cacat dan 1 baik):
$$n(Y = 2) = \binom{5}{2} \times \binom{7}{1} = \frac{5 \times 4}{2 \times 1} \times 7 = 10 \times 7 = 70$$

3. Menghitung nilai peluang:
$$P(Y = 2) = \frac{n(Y = 2)}{n(S)} = \frac{70}{220} = \frac{7}{22}$$

Jadi, nilai dari $P(Y = 2)$ adalah $\frac{7}{22}$.
**Acuan:** siswa — siswa hal.261 Ayo Mencoba 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-d-medium-bt01-010
*variasi (angka) | C3 | 3 langkah | jenis: distribusi peluang binomial tes*

Dalam sebuah kuis, diberikan 5 butir soal yang masing-masing jawabannya bertipe benar atau salah. Seorang peserta menjawab semua soal dengan menebak secara acak. Jika variabel acak $X$ menyatakan banyak soal yang dijawab dengan benar oleh peserta tersebut, nilai dari $P(X \ge 4)$ adalah ....

- A. $\frac{3}{8}$  
  <sub>Salah: Siswa salah menghitung ukuran ruang sampel sebagai $2^4 = 16$ sehingga memperoleh $\frac{6}{16} = \frac{3}{8}$.</sub>
- **B. $\frac{3}{16}$** ✅  
  <sub>Benar: Peluang menjawab benar pada tiap butir adalah $\frac{1}{2}$. $P(X \ge 4) = P(X = 4) + P(X = 5) = \binom{5}{4}\left(\frac{1}{2}\right)^5 + \binom{5}{5}\left(\frac{1}{2}\right)^5 = \frac{5}{32} + \frac{1}{32} = \frac{6}{32} = \frac{3}{16}$.</sub>
- C. $\frac{5}{32}$  
  <sub>Salah: Siswa hanya menghitung nilai $P(X = 4)$ dan lupa menambahkan $P(X = 5)$.</sub>
- D. $\frac{1}{16}$  
  <sub>Salah: Siswa keliru mengira $\binom{5}{4} = 1$ sehingga menghitung $\frac{1}{32} + \frac{1}{32} = \frac{2}{32} = \frac{1}{16}$.</sub>

**Pembahasan:** Setiap butir soal memiliki 2 kemungkinan dengan peluang benar $p = \frac{1}{2}$ dan peluang salah $q = \frac{1}{2}$.
Total kemungkinan jawaban untuk 5 butir soal adalah $2^5 = 32$.

1. Menghitung $P(X = 4)$:
$$P(X = 4) = \binom{5}{4}\left(\frac{1}{2}\right)^4\left(\frac{1}{2}\right)^1 = 5 \times \frac{1}{32} = \frac{5}{32}$$

2. Menghitung $P(X = 5)$:
$$P(X = 5) = \binom{5}{5}\left(\frac{1}{2}\right)^5 = 1 \times \frac{1}{32} = \frac{1}{32}$$

3. Menghitung $P(X \ge 4)$:
$$P(X \ge 4) = P(X = 4) + P(X = 5) = \frac{5}{32} + \frac{1}{32} = \frac{6}{32} = \frac{3}{16}$$

Jadi, nilai dari $P(X \ge 4)$ adalah $\frac{3}{16}$.
**Acuan:** pretest — kelas12_tl-b04-p0264-latihan-soal-fungsi-peluang-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-d-medium-bt01-011
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi peluang pemilihan objek acak*

Sebuah rak buku memuat 4 novel fiksi, 3 komik, dan 5 buku ensiklopedia. Seorang pustakawan mengambil 2 buku secara acak sekaligus untuk dipajang. Jika variabel acak $K$ menyatakan banyak buku komik yang terambil, nilai dari $P(K = 1)$ adalah ....

- **A. $\frac{9}{22}$** ✅  
  <sub>Benar: Total buku adalah $4 + 3 + 5 = 12$. Banyak cara mengambil 2 buku adalah $\binom{12}{2} = 66$. Terambil 1 komik berarti 1 dari 3 komik dan 1 dari 9 buku bukan komik, yaitu $\binom{3}{1} \times \binom{9}{1} = 27$. Peluangnya adalah $\frac{27}{66} = \frac{9}{22}$.</sub>
- B. $\frac{1}{4}$  
  <sub>Salah: Siswa hanya membagi jumlah komik dengan total buku tanpa memperhitungkan pengambilan 2 buku: $\frac{3}{12} = \frac{1}{4}$.</sub>
- C. $\frac{7}{22}$  
  <sub>Salah: Siswa salah menghitung jumlah buku bukan komik menjadi $4 + 3 = 7$ sehingga $\frac{3 \times 7}{66} = \frac{21}{66} = \frac{7}{22}$.</sub>
- D. $\frac{3}{22}$  
  <sub>Salah: Siswa lupa mengalikan dengan banyaknya cara memilih buku bukan komik, hanya menghitung $\frac{3 \times 3}{66} = \frac{9}{66} = \frac{3}{22}$.</sub>

**Pembahasan:** Total buku dalam rak = $4 + 3 + 5 = 12$ buku.
Jumlah buku komik = $3$, dan buku bukan komik = $4 + 5 = 9$.

1. Menghitung ukuran ruang sampel memilih 2 buku:
$$n(S) = \binom{12}{2} = \frac{12 \times 11}{2 \times 1} = 66$$

2. Menghitung banyak cara terambil tepat 1 buku komik ($K = 1$):
$$n(K = 1) = \binom{3}{1} \times \binom{9}{1} = 3 \times 9 = 27$$

3. Menghitung peluang $P(K = 1)$:
$$P(K = 1) = \frac{27}{66} = \frac{9}{22}$$

Jadi, nilai dari $P(K = 1)$ adalah $\frac{9}{22}$.
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-d-medium-bt01-012
*orisinal | C4 | 3 langkah | jenis: penentuan konstanta fungsi peluang*

Fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{k}{x(x+1)}, & \text{untuk } x = 1, 2, 3, 4 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \ge 3)$ adalah ....

- A. $\frac{5}{48}$  
  <sub>Salah: Siswa hanya menghitung nilai $f(3)$ dan mengabaikan $f(4)$.</sub>
- B. $\frac{2}{15}$  
  <sub>Salah: Siswa lupa mengalikan dengan konstanta $k = \frac{5}{4}$, langsung menghitung $\frac{1}{12} + \frac{1}{20} = \frac{2}{15}$.</sub>
- **C. $\frac{1}{6}$** ✅  
  <sub>Benar: Dari $\sum f(x) = 1$, diperoleh $k\left(\frac{1}{2} + \frac{1}{6} + \frac{1}{12} + \frac{1}{20}\right) = k\left(1 - \frac{1}{5}\right) = \frac{4}{5}k = 1 \implies k = \frac{5}{4}$. Maka $P(X \ge 3) = f(3) + f(4) = \frac{5}{4}\left(\frac{1}{12} + \frac{1}{20}\right) = \frac{5}{4} \times \frac{8}{60} = \frac{1}{6}$.</sub>
- D. $\frac{5}{6}$  
  <sub>Salah: Siswa salah menentukan batas dengan menghitung komplemen $P(X < 3) = 1 - \frac{1}{6} = \frac{5}{6}$.</sub>

**Pembahasan:** 1. Menggunakan sifat total fungsi peluang $\sum_{x=1}^{4} f(x) = 1$:
$$\sum_{x=1}^{4} \frac{1}{x(x+1)} = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \left(\frac{1}{3} - \frac{1}{4}\right) + \left(\frac{1}{4} - \frac{1}{5}\right) = 1 - \frac{1}{5} = \frac{4}{5}$$
Sehingga:
$$k \cdot \frac{4}{5} = 1 \implies k = \frac{5}{4}$$

2. Menghitung $f(3)$ dan $f(4)$:
$$f(3) = \frac{5}{4} \cdot \frac{1}{3 \times 4} = \frac{5}{48}$$
$$f(4) = \frac{5}{4} \cdot \frac{1}{4 \times 5} = \frac{1}{16} = \frac{3}{48}$$

3. Menghitung $P(X \ge 3)$:
$$P(X \ge 3) = f(3) + f(4) = \frac{5}{48} + \frac{3}{48} = \frac{8}{48} = \frac{1}{6}$$

Jadi, nilai dari $P(X \ge 3)$ adalah $\frac{1}{6}$.
**Acuan:** siswa — siswa hal.259

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-d-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: distribusi peluang variabel acak jumlah kartu*

Empat lembar kartu masing-masing bertuliskan angka 1, 2, 3, dan 4. Dua lembar kartu diambil sekaligus secara acak. Misalkan variabel acak $S$ menyatakan jumlah dari kedua angka pada kartu yang terambil. Nilai dari $P(S > 5)$ adalah ....

- A. $\frac{1}{6}$  
  <sub>Salah: Siswa hanya memperhitungkan satu kejadian jumlah terbesar yaitu pasangan {3,4}.</sub>
- B. $\frac{2}{3}$  
  <sub>Salah: Siswa keliru menghitung $P(S \ge 5)$ sehingga memasukkan jumlah 5 yang memiliki 4 kejadian: $\frac{4}{6} = \frac{2}{3}$.</sub>
- C. $\frac{1}{2}$  
  <sub>Salah: Siswa mengira terdapat 3 pasangan yang memenuhi yaitu {1,4}, {2,4}, dan {3,4} sehingga $\frac{3}{6} = \frac{1}{2}$.</sub>
- **D. $\frac{1}{3}$** ✅  
  <sub>Benar: Banyak cara mengambil 2 dari 4 kartu adalah $\binom{4}{2} = 6$. Pasangan kartu yang mungkin adalah {1,2} jumlah 3; {1,3} jumlah 4; {1,4} jumlah 5; {2,3} jumlah 5; {2,4} jumlah 6; {3,4} jumlah 7. Nilai $S > 5$ diperoleh dari {2,4} dan {3,4} (2 kejadian). Peluangnya adalah $\frac{2}{6} = \frac{1}{3}$.</sub>

**Pembahasan:** 1. Menentukan ruang sampel memilih 2 kartu dari 4 kartu:
$$n(S) = \binom{4}{2} = \frac{4 \times 3}{2 \times 1} = 6$$
Pasangan kartu yang mungkin beserta jumlahnya:
- $\{1, 2\} \rightarrow S = 3$
- $\{1, 3\} \rightarrow S = 4$
- $\{1, 4\} \rightarrow S = 5$
- $\{2, 3\} \rightarrow S = 5$
- $\{2, 4\} \rightarrow S = 6$
- $\{3, 4\} \rightarrow S = 7$

2. Menentukan kejadian yang memenuhi syarat $S > 5$:
Hasil yang memiliki jumlah lebih dari 5 adalah $\{2, 4\}$ (jumlah 6) dan $\{3, 4\}$ (jumlah 7), sehingga ada 2 kejadian.

3. Menghitung peluang:
$$P(S > 5) = \frac{2}{6} = \frac{1}{3}$$

Jadi, nilai dari $P(S > 5)$ adalah $\frac{1}{3}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-d-medium-bt01-014
*variasi (angka) | C3 | 3 langkah | jenis: peluang kumulatif hipergeometrik*

Sebuah distributor mengirim 11 unit laptop ke sebuah toko komputer, dan ternyata 3 unit di antaranya cacat. Seseorang membeli 2 unit laptop secara acak sekaligus. Jika variabel acak $Y$ menyatakan banyak laptop cacat yang dibeli, nilai dari $P(Y \ge 1)$ adalah ....

- A. $\frac{3}{55}$  
  <sub>Salah: Siswa hanya menghitung $P(Y = 2)$.</sub>
- B. $\frac{28}{55}$  
  <sub>Salah: Siswa menghitung peluang komplemen $P(Y = 0)$ bukan $P(Y \ge 1)$.</sub>
- **C. $\frac{27}{55}$** ✅  
  <sub>Benar: Total cara memilih 2 dari 11 laptop adalah $\binom{11}{2} = 55$. Banyak cara memilih 0 laptop cacat (keduanya baik dari 8 unit) adalah $\binom{8}{2} = 28$. Peluang komplemennya adalah $P(Y \ge 1) = 1 - P(Y = 0) = 1 - \frac{28}{55} = \frac{27}{55}$.</sub>
- D. $\frac{24}{55}$  
  <sub>Salah: Siswa hanya menghitung nilai $P(Y = 1)$ dan melupakan kasus $Y = 2$.</sub>

**Pembahasan:** Banyak anggota ruang sampel memilih 2 laptop dari 11 laptop:
$$n(S) = \binom{11}{2} = \frac{11 \times 10}{2} = 55$$
Laptop cacat ada 3 dan laptop baik ada 8.
Kejadian $Y \ge 1$ mencakup $Y = 1$ dan $Y = 2$, atau dapat dihitung melalui komplemen $1 - P(Y = 0)$.
$$P(Y = 0) = \frac{\binom{8}{2}}{\binom{11}{2}} = \frac{28}{55}$$
Maka:
$$P(Y \ge 1) = 1 - \frac{28}{55} = \frac{27}{55}$$
**Acuan:** siswa — siswa hal.261 Ayo Mencoba 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-d-medium-bt01-015
*variasi (konteks) | C4 | 3 langkah | jenis: distribusi peluang pengambilan tiga objek*

Sebuah laci memuat 5 kaus kaki hitam, 3 kaus kaki putih, dan 2 kaus kaki abu-abu. Tiga kaus kaki diambil secara acak sekaligus. Jika variabel acak $P$ menyatakan banyak kaus kaki putih yang terambil, nilai dari $P(P = 2)$ adalah ....

- **A. $\frac{7}{40}$** ✅  
  <sub>Benar: Total kaus kaki adalah 10. $n(S) = \binom{10}{3} = 120$. Banyak cara terambil 2 kaus kaki putih dan 1 kaus kaki bukan putih adalah $\binom{3}{2} \times \binom{7}{1} = 3 \times 7 = 21$. Maka $P(P = 2) = \frac{21}{120} = \frac{7}{40}$.</sub>
- B. $\frac{7}{24}$  
  <sub>Salah: Siswa menghitung peluang tidak terambil kaus kaki putih sama sekali ($P(P = 0) = \frac{35}{120} = \frac{7}{24}$).</sub>
- C. $\frac{21}{40}$  
  <sub>Salah: Siswa menghitung peluang terambilnya 1 kaus kaki putih ($P(P = 1) = \frac{63}{120} = \frac{21}{40}$).</sub>
- D. $\frac{1}{120}$  
  <sub>Salah: Siswa menghitung peluang ketiganya kaus kaki putih ($P(P = 3) = \frac{1}{120}$).</sub>

**Pembahasan:** Total kaus kaki = $5 + 3 + 2 = 10$.
Banyak anggota ruang sampel memilih 3 dari 10 kaus kaki:
$$n(S) = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$
Kaus kaki putih berjumlah 3, sedangkan kaus kaki bukan putih berjumlah $5 + 2 = 7$.
Banyak cara mengambil 2 kaus kaki putih dan 1 kaus kaki bukan putih:
$$n(P = 2) = \binom{3}{2} \times \binom{7}{1} = 3 \times 7 = 21$$
Peluang kejadian tersebut:
$$P(P = 2) = \frac{21}{120} = \frac{7}{40}$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-d-medium-bt01-016
*orisinal | C3 | 3 langkah | jenis: penentuan peluang dari fungsi kuadrat diskret*  **[warning validator]**

Fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} c x^2, & \text{untuk } x = 1, 2, 3 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \ge 2)$ adalah ....

- **A. $\frac{13}{14}$** ✅  
  <sub>Benar: Jumlah seluruh peluang harus sama dengan 1: $c(1^2 + 2^2 + 3^2) = 14c = 1 \implies c = \frac{1}{14}$. Maka $P(X \ge 2) = f(2) + f(3) = \frac{4}{14} + \frac{9}{14} = \frac{13}{14}$.</sub>
- B. $\frac{9}{14}$  
  <sub>Salah: Siswa hanya menghitung $f(3)$ saja.</sub>
- C. $\frac{1}{14}$  
  <sub>Salah: Siswa menghitung nilai komplemen $P(X < 2) = f(1) = \frac{1}{14}$.</sub>
- D. $\frac{5}{14}$  
  <sub>Salah: Siswa menghitung $f(1) + f(2) = \frac{1+4}{14} = \frac{5}{14}$.</sub>

**Pembahasan:** Agar $f(x)$ menjadi fungsi peluang yang sah, jumlahan seluruh peluang harus sama dengan 1:
$$\sum_{x=1}^3 f(x) = 1$$
$$c(1^2) + c(2^2) + c(3^2) = 1$$
$$c(1 + 4 + 9) = 1 \implies 14c = 1 \implies c = \frac{1}{14}$$
Maka peluang untuk $X \ge 2$ adalah:
$$P(X \ge 2) = f(2) + f(3) = \frac{4}{14} + \frac{9}{14} = \frac{13}{14}$$
**Acuan:** siswa — siswa hal.258
**Warning:** kelas12_tl-b04-d-medium-bt01-007 sangat mirip dengan kelas12_tl-b04-d-medium-bt01-016 (0.85) padahal acuan beda

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-d-medium-bt01-017
*orisinal | C4 | 3 langkah | jenis: variabel acak selisih pelemparan koin*

Empat keping uang logam setimbang dilemparkan secara bersamaan sebanyak satu kali. Misalkan $X$ adalah variabel acak yang menyatakan selisih mutlak antara banyaknya sisi angka (A) dan banyaknya sisi gambar (G) yang muncul. Nilai dari $P(X = 2)$ adalah ....

- A. $\frac{3}{8}$  
  <sub>Salah: Siswa tertukar dengan kejadian $X = 0$, yaitu muncul 2 angka dan 2 gambar yang berpeluang $\frac{6}{16} = \frac{3}{8}$.</sub>
- **B. $\frac{1}{2}$** ✅  
  <sub>Benar: Total ruang sampel pelemparan 4 koin adalah $2^4 = 16$. Nilai $X = |A - G| = 2$ terjadi ketika muncul 3A dan 1G (selisih $|3-1|=2$, ada $\binom{4}{1}=4$ cara) atau 1A dan 3G (selisih $|1-3|=2$, ada $\binom{4}{3}=4$ cara). Total kejadian adalah $4 + 4 = 8$ cara, sehingga $P(X = 2) = \frac{8}{16} = \frac{1}{2}$.</sub>
- C. $\frac{1}{8}$  
  <sub>Salah: Siswa hanya menghitung kejadian ekstrim 4 angka atau 4 gambar yang menghasilkan selisih 4 ($\frac{2}{16} = \frac{1}{8}$).</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Siswa hanya menghitung kejadian 3 angka 1 gambar ($\frac{4}{16} = \frac{1}{4}$) dan melupakan kejadian 1 angka 3 gambar.</sub>

**Pembahasan:** Banyak anggota ruang sampel dari pelemparan 4 keping uang logam:
$$n(S) = 2^4 = 16$$
Variabel acak $X = |\text{banyak A} - \text{banyak G}|$.
Kemungkinan komposisi dan nilai $X$:
- 4A, 0G: $X = |4 - 0| = 4$ (sebanyak $\binom{4}{0} = 1$ cara)
- 3A, 1G: $X = |3 - 1| = 2$ (sebanyak $\binom{4}{1} = 4$ cara)
- 2A, 2G: $X = |2 - 2| = 0$ (sebanyak $\binom{4}{2} = 6$ cara)
- 1A, 3G: $X = |1 - 3| = 2$ (sebanyak $\binom{4}{3} = 4$ cara)
- 0A, 4G: $X = |0 - 4| = 4$ (sebanyak $\binom{4}{4} = 1$ cara)

Kejadian $X = 2$ diperoleh dari komposisi (3A, 1G) dan (1A, 3G):
$$n(X = 2) = 4 + 4 = 8$$
Maka:
$$P(X = 2) = \frac{8}{16} = \frac{1}{2}$$
**Acuan:** siswa — siswa hal.257

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-d-medium-bt01-018
*variasi (konteks) | C3 | 3 langkah | jenis: distribusi peluang pengambilan dokumen*

Sebuah map arsip memuat 6 lembar sertifikat pelatihan dan 4 lembar piagam penghargaan. Dari map tersebut diambil 2 lembar dokumen secara acak sekaligus. Jika variabel acak $K$ menyatakan banyaknya piagam penghargaan yang terambil, nilai dari $P(K \ge 1)$ adalah ....

- **A. $\frac{2}{3}$** ✅  
  <sub>Benar: Total cara pengambilan 2 dari 10 dokumen adalah $\binom{10}{2} = 45$. Peluang terambil 0 piagam adalah $P(K = 0) = \frac{\binom{6}{2}\binom{4}{0}}{45} = \frac{15}{45} = \frac{1}{3}$. Maka $P(K \ge 1) = 1 - P(K = 0) = 1 - \frac{1}{3} = \frac{2}{3}$.</sub>
- B. $\frac{2}{15}$  
  <sub>Salah: Siswa hanya menghitung peluang terambil tepat 2 piagam penghargaan ($P(K = 2) = \frac{6}{45} = \frac{2}{15}$).</sub>
- C. $\frac{8}{15}$  
  <sub>Salah: Siswa hanya menghitung peluang terambil tepat 1 piagam penghargaan ($P(K = 1) = \frac{24}{45} = \frac{8}{15}$), melupakan kasus $K = 2$.</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: Siswa hanya menghitung peluang komplemennya, yaitu saat tidak ada piagam penghargaan yang terambil ($P(K = 0)$).</sub>

**Pembahasan:** Banyaknya seluruh cara mengambil 2 lembar dokumen dari total 10 lembar dokumen adalah:
$$n(S) = \binom{10}{2} = \frac{10 \times 9}{2 \times 1} = 45$$

Variabel acak $K$ menyatakan banyaknya piagam penghargaan yang terambil, dengan nilai yang mungkin $K \in \{0, 1, 2\}$.

Kejadian $K \ge 1$ mencakup $K = 1$ atau $K = 2$, yang dapat dihitung menggunakan aturan komplemen:
$$P(K \ge 1) = 1 - P(K = 0)$$

Banyaknya cara mengambil 0 piagam (artinya kedua dokumen adalah sertifikat pelatihan):
$$n(K = 0) = \binom{6}{2} \times \binom{4}{0} = 15 \times 1 = 15$$
$$P(K = 0) = \frac{15}{45} = \frac{1}{3}$$

Dengan demikian:
$$P(K \ge 1) = 1 - \frac{1}{3} = \frac{2}{3}$$
**Acuan:** siswa — siswa hal.259 Contoh Soal 4.6

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-d-medium-bt01-019
*variasi (angka) | C3 | 2 langkah | jenis: peluang variabel acak diskret linear*

Fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{x}{25}, & \text{untuk } x = 4, 5, 7, 9 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X \ge 7)$ adalah ....

- **A. $\frac{16}{25}$** ✅  
  <sub>Benar: $P(X \ge 7) = f(7) + f(9) = \frac{7}{25} + \frac{9}{25} = \frac{16}{25}$.</sub>
- B. $\frac{21}{25}$  
  <sub>Salah: Siswa salah memasukkan nilai $x = 5$ ke dalam perhitungan ($f(5) + f(7) + f(9)$).</sub>
- C. $\frac{9}{25}$  
  <sub>Salah: Siswa keliru menafsirkan tanda pertidaksamaan sebagai ketaksamaan ketat $P(X > 7)$, sehingga hanya mengambil nilai $f(9)$.</sub>
- D. $\frac{7}{25}$  
  <sub>Salah: Siswa salah mengira $P(X \ge 7)$ hanya menanyakan nilai tepat di batas bawah, yaitu $f(7)$.</sub>

**Pembahasan:** Berdasarkan fungsi peluang yang diberikan, nilai $x$ yang memenuhi kondisi $X \ge 7$ pada domain fungsi adalah $x = 7$ dan $x = 9$.

Maka nilai peluangnya adalah:
$$P(X \ge 7) = f(7) + f(9)$$
$$P(X \ge 7) = \frac{7}{25} + \frac{9}{25} = \frac{16}{25}$$
**Acuan:** siswa — siswa hal.263 Latihan Soal Fungsi Peluang

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-d-medium-bt01-020
*orisinal | C3 | 2 langkah | jenis: distribusi peluang diskret linear*

Fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} c(2x + 1), & \text{untuk } x = 0, 1, 2, 3 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Nilai dari $P(X > 1)$ adalah ....

- A. $\frac{15}{16}$  
  <sub>Salah: Keliru menganggap $P(X > 1)$ sebagai $P(X \ge 1) = f(1) + f(2) + f(3) = \frac{3+5+7}{16} = \frac{15}{16}$.</sub>
- B. $\frac{5}{16}$  
  <sub>Salah: Keliru hanya menghitung nilai $f(2)$ tanpa menyertakan $f(3)$.</sub>
- **C. $\frac{3}{4}$** ✅  
  <sub>Benar: Jumlah seluruh peluang harus bernilai 1:
$$\sum_{x=0}^3 f(x) = c[(2(0)+1) + (2(1)+1) + (2(2)+1) + (2(3)+1)] = 1$$
$$c(1 + 3 + 5 + 7) = 1 \implies 16c = 1 \implies c = \frac{1}{16}$$
Nilai peluang untuk $X > 1$ adalah:
$$P(X > 1) = f(2) + f(3) = \frac{2(2)+1}{16} + \frac{2(3)+1}{16} = \frac{5}{16} + \frac{7}{16} = \frac{12}{16} = \frac{3}{4}$$</sub>
- D. $\frac{4}{5}$  
  <sub>Salah: Lupa memperhitungkan nilai $x = 0$ saat menghitung konstanta $c$, sehingga diperoleh $c(3 + 5 + 7) = 1 \implies c = \frac{1}{15}$, lalu menghitung $\frac{5+7}{15} = \frac{12}{15} = \frac{4}{5}$.</sub>

**Pembahasan:** Agar $f(x)$ merupakan fungsi peluang variabel acak diskret, syarat $\sum f(x) = 1$ harus terpenuhi:
$$\sum_{x=0}^3 f(x) = f(0) + f(1) + f(2) + f(3) = 1$$
$$c(1) + c(3) + c(5) + c(7) = 1$$
$$16c = 1 \implies c = \frac{1}{16}$$

Selanjutnya, tentukan peluang $P(X > 1)$:
$$P(X > 1) = f(2) + f(3)$$
$$P(X > 1) = \frac{5}{16} + \frac{7}{16} = \frac{12}{16} = \frac{3}{4}$$

Jadi, nilai dari $P(X > 1)$ adalah $\frac{3}{4}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-d-hard-bt01-001
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi perbandingan peluang*

Sebuah etalase memuat 10 buah kalkulator, dengan 4 di antaranya dalam keadaan rusak. Seorang guru mengambil 3 kalkulator secara acak sekaligus untuk keperluan ujian. Jika variabel acak $X$ menyatakan banyaknya kalkulator rusak yang terambil, perbandingan nilai peluang $P(X \ge 2)$ terhadap $P(X = 1)$ adalah ....

- **A. $\frac{2}{3}$** ✅  
  <sub>Benar: Banyak ruang sampel: $\binom{10}{3} = 120$. Peluang $P(X = 1) = \frac{\binom{4}{1} \times \binom{6}{2}}{120} = \frac{4 \times 15}{120} = \frac{60}{120}$. Peluang $P(X = 2) = \frac{\binom{4}{2} \times \binom{6}{1}}{120} = \frac{36}{120}$, dan $P(X = 3) = \frac{\binom{4}{3} \times \binom{6}{0}}{120} = \frac{4}{120}$. Maka $P(X \ge 2) = \frac{36 + 4}{120} = \frac{40}{120}$. Perbandingan $\frac{P(X \ge 2)}{P(X = 1)} = \frac{40/120}{60/120} = \frac{2}{3}$.</sub>
- B. $\frac{1}{2}$  
  <sub>Salah: Siswa salah menghitung kombinasi $\binom{6}{2}$ menjadi 12 sehingga mengira $P(X=1) = \frac{48}{120}$ lalu menyederhanakan pecahan keliru.</sub>
- C. $\frac{3}{5}$  
  <sub>Salah: Siswa lupa memperhitungkan kejadian $X = 3$, hanya menghitung $\frac{P(X = 2)}{P(X = 1)} = \frac{36}{60} = \frac{3}{5}$.</sub>
- D. $\frac{3}{2}$  
  <sub>Salah: Siswa membalik posisi perbandingan menjadi $P(X = 1) : P(X \ge 2)$.</sub>

**Pembahasan:** Banyak anggota ruang sampel memilih 3 kalkulator dari 10 kalkulator adalah:
$$n(S) = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

Distribusi peluang variabel acak $X$ (banyak kalkulator rusak dari 4 rusak dan 6 baik):
1. Untuk $X = 1$:
$$P(X = 1) = \frac{\binom{4}{1} \times \binom{6}{2}}{120} = \frac{4 \times 15}{120} = \frac{60}{120}$$

2. Untuk $X \ge 2$, yaitu $X = 2$ atau $X = 3$:
$$P(X = 2) = \frac{\binom{4}{2} \times \binom{6}{1}}{120} = \frac{6 \times 6}{120} = \frac{36}{120}$$
$$P(X = 3) = \frac{\binom{4}{3} \times \binom{6}{0}}{120} = \frac{4 \times 1}{120} = \frac{4}{120}$$
$$P(X \ge 2) = P(X = 2) + P(X = 3) = \frac{36}{120} + \frac{4}{120} = \frac{40}{120}$$

Perbandingan yang diminta:
$$\frac{P(X \ge 2)}{P(X = 1)} = \frac{\frac{40}{120}}{\frac{60}{120}} = \frac{40}{60} = \frac{2}{3}$$
**Acuan:** siswa — siswa hal.263 Latihan Soal Fungsi Peluang

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-d-hard-bt01-002
*orisinal | C5 | 4 langkah | jenis: penalaran distribusi bersyarat proporsi*

Sebuah variabel acak diskret $X$ memiliki ruang nilai $\{1, 2, 3, 4, 5\}$. Fungsi peluang $X$ didefinisikan sebagai:
$$P(X = x) = \begin{cases} kx, & \text{untuk } x = 1, 2, 3 \\ c(6 - x), & \text{untuk } x = 4, 5 \end{cases}$$
Jika diketahui $P(X = 2) = P(X = 4)$, nilai dari $P(2 \le X \le 4)$ adalah ....

- A. $\frac{8}{9}$  
  <sub>Salah: Siswa menjumlahkan $P(X \ge 2)$ secara keseluruhan dari $x = 2$ sampai $x = 5$.</sub>
- B. $\frac{5}{9}$  
  <sub>Salah: Siswa hanya menjumlahkan $P(X = 2) + P(X = 3) = 5k = 5/9$, lupa mengikutsertakan $X = 4$.</sub>
- C. $\frac{2}{3}$  
  <sub>Salah: Siswa salah menghitung total probabilitas $6k + 2c = 8k = 1$ sehingga menghasilkan nilai $k = 1/8$ lalu keliru menjumlahkan.</sub>
- **D. $\frac{7}{9}$** ✅  
  <sub>Benar: $P(X = 2) = 2k$ dan $P(X = 4) = 2c$, sehingga $2k = 2c \implies k = c$. Jumlah total peluang: $(k + 2k + 3k) + (2c + c) = 6k + 3k = 9k = 1 \implies k = 1/9$. Maka $P(2 \le X \le 4) = P(X = 2) + P(X = 3) + P(X = 4) = 2k + 3k + 2k = 7k = 7/9$.</sub>

**Pembahasan:** Diketahui hubungan:
$$P(X = 2) = 2k$$
$$P(X = 4) = c(6 - 4) = 2c$$
Karena $P(X = 2) = P(X = 4)$, maka:
$$2k = 2c \implies k = c$$

Syarat total fungsi peluang adalah 1:
$$\sum_{x=1}^{5} P(X = x) = 1$$
$$P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) + P(X = 5) = 1$$
$$(k) + (2k) + (3k) + c(6 - 4) + c(6 - 5) = 1$$
$$6k + 2c + c = 1$$
Karena $c = k$:
$$6k + 3k = 1 \implies 9k = 1 \implies k = \frac{1}{9}$$
Dengan demikian $c = \frac{1}{9}$.

Nilai $P(2 \le X \le 4)$:
$$P(2 \le X \le 4) = P(X = 2) + P(X = 3) + P(X = 4)$$
$$P(2 \le X \le 4) = 2k + 3k + 2c = 2k + 3k + 2k = 7k = 7\left(\frac{1}{9}\right) = \frac{7}{9}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-d-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: evaluasi pernyataan fungsi peluang*

Fungsi peluang suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{k - x^2}{20}, & \text{untuk } x \in \{-2, -1, 0, 1, 2\} \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Perhatikan pernyataan-pernyataan berikut:
(1) Nilai konstanta $k = 6$.
(2) Nilai peluang $P(X = 0) = \frac{3}{10}$.
(3) Nilai peluang $P(X > 0) = \frac{1}{4}$.
(4) Fungsi peluang bersifat simetris terhadap titik 0, yaitu $P(X = x) = P(X = -x)$ untuk semua $x$.

Pernyataan yang bernilai benar adalah ....

- A. (1) dan (4) saja  
  <sub>Salah: Siswa mengira $P(X = 0)$ harus bernilai 0 karena menganggap variabel di titik asal tidak berpeluang.</sub>
- **B. (1), (2), dan (4)** ✅  
  <sub>Benar: Total $\sum f(x) = \frac{5k - (4+1+0+1+4)}{20} = \frac{5k - 10}{20} = 1 \implies k = 6$ (pernyataan 1 benar). $P(X=0) = 6/20 = 3/10$ (pernyataan 2 benar). $P(X>0) = f(1) + f(2) = 5/20 + 2/20 = 7/20 \ne 1/4$ (pernyataan 3 salah). Karena $x^2 = (-x)^2$, maka $f(x) = f(-x)$ (pernyataan 4 benar).</sub>
- C. (1), (2), dan (3)  
  <sub>Salah: Siswa salah menghitung $P(X > 0)$ hanya mengambil $f(1) = 5/20 = 1/4$, lupa bahwa $x = 2$ juga bernilai lebih dari 0.</sub>
- D. (2), (3), dan (4)  
  <sub>Salah: Siswa salah menentukan nilai $k$ dari pembagi yang tidak dikalikan silang dengan benar.</sub>

**Pembahasan:** Uji setiap pernyataan secara bertahap:

1. Menentukan nilai $k$:
$$\sum_{x=-2}^{2} f(x) = 1$$
$$\frac{(k - 4) + (k - 1) + (k - 0) + (k - 1) + (k - 4)}{20} = 1$$
$$\frac{5k - 10}{20} = 1 \implies 5k - 10 = 20 \implies 5k = 30 \implies k = 6$$
Untuk $k = 6$, $f(x) \ge 0$ terpenuhi untuk seluruh domain (nilai minimum $f(\pm 2) = 2/20 > 0$).
Maka pernyataan (1) BENAR.

2. Menentukan $P(X = 0)$:
$$P(X = 0) = f(0) = \frac{6 - 0^2}{20} = \frac{6}{20} = \frac{3}{10}$$
Maka pernyataan (2) BENAR.

3. Menentukan $P(X > 0)$:
$$P(X > 0) = f(1) + f(2) = \frac{6 - 1^2}{20} + \frac{6 - 2^2}{20} = \frac{5}{20} + \frac{2}{20} = \frac{7}{20}$$
Karena $\frac{7}{20} \ne \frac{1}{4}$ (dimana $\frac{1}{4} = \frac{5}{20}$), maka pernyataan (3) SALAH.

4. Memeriksa simetri terhadap 0:
Untuk sembarang $x \in \{-2, -1, 0, 1, 2\}$:
$$f(-x) = \frac{6 - (-x)^2}{20} = \frac{6 - x^2}{20} = f(x)$$
Maka pernyataan (4) BENAR.

Jadi, pernyataan yang bernilai benar adalah (1), (2), dan (4).
**Acuan:** siswa — siswa hal.260

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-d-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: perancangan parameter ganda fungsi peluang*

Diberikan calon fungsi peluang untuk variabel acak diskret $X$ dengan daerah nilai $x \in \{1, 2, 3, 4\}$ sebagai berikut:
$$f(x) = \begin{cases} \frac{k - x}{8}, & \text{untuk } x = 1, 2 \\ \frac{2x - m}{8}, & \text{untuk } x = 3, 4 \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Jika $f(x)$ sah merupakan fungsi peluang yang membagi dua probabilitas sama besar pada $P(X \le 2) = P(X \ge 3)$, nilai dari $2k - m$ adalah ....

- A. 1  
  <sub>Salah: Siswa salah menghitung $14 - 2m = 4$ menjadi $2m = 12 \implies m = 6$, sehingga $7 - 6 = 1$.</sub>
- B. 4  
  <sub>Salah: Siswa lupa mengalikan silang penyebut 8 dengan $1/2$ sehingga mengira ruas kanan bernilai 1.</sub>
- **C. 2** ✅  
  <sub>Benar: Karena $P(X \le 2) + P(X \ge 3) = 1$ dan nilainya sama besar, maka masing-masing bernilai $1/2$. Dari $P(X \le 2) = \frac{(k-1) + (k-2)}{8} = \frac{2k-3}{8} = \frac{1}{2}$, diperoleh $2k - 3 = 4 \implies 2k = 7$. Dari $P(X \ge 3) = \frac{(6-m) + (8-m)}{8} = \frac{14-2m}{8} = \frac{1}{2}$, diperoleh $14 - 2m = 4 \implies 2m = 10 \implies m = 5$. Maka $2k - m = 7 - 5 = 2$.</sub>
- D. 3  
  <sub>Salah: Siswa salah menghitung persamaan $2k - 3 = 4$ menjadi $2k = 8$ sehingga $2k - m = 8 - 5 = 3$.</sub>

**Pembahasan:** Fungsi $f(x)$ merupakan fungsi peluang sah, sehingga:
$$P(X \le 2) + P(X \ge 3) = 1$$
Karena diketahui $P(X \le 2) = P(X \ge 3)$, maka:
$$P(X \le 2) = \frac{1}{2} \quad \text{dan} \quad P(X \ge 3) = \frac{1}{2}$$

1. Dari $P(X \le 2) = \frac{1}{2}$:
$$f(1) + f(2) = \frac{1}{2}$$
$$\frac{k - 1}{8} + \frac{k - 2}{8} = \frac{1}{2}$$
$$\frac{2k - 3}{8} = \frac{4}{8} \implies 2k - 3 = 4 \implies 2k = 7 \implies k = 3,5$$

2. Dari $P(X \ge 3) = \frac{1}{2}$:
$$f(3) + f(4) = \frac{1}{2}$$
$$\frac{2(3) - m}{8} + \frac{2(4) - m}{8} = \frac{1}{2}$$
$$\frac{6 - m + 8 - m}{8} = \frac{4}{8} \implies 14 - 2m = 4 \implies 2m = 10 \implies m = 5$$

3. Uji syarat $f(x) \ge 0$:
- $f(1) = \frac{3,5 - 1}{8} = \frac{2,5}{8} > 0$
- $f(2) = \frac{3,5 - 2}{8} = \frac{1,5}{8} > 0$
- $f(3) = \frac{6 - 5}{8} = \frac{1}{8} > 0$
- $f(4) = \frac{8 - 5}{8} = \frac{3}{8} > 0$
Semua nilai peluang tak negatif dan totalnya tepat 1.

4. Menghitung nilai $2k - m$:
$$2k - m = 7 - 5 = 2$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-d-hard-bt01-005
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi perbandingan peluang kumulatif*

Sebuah repositori kode memuat 8 berkas program, dengan 3 di antaranya mengandung celah keamanan (_bug_). Seorang auditor keamanan siber memilih 3 berkas secara acak sekaligus untuk diperiksa. Misalkan variabel acak $X$ menyatakan banyak berkas ber-_bug_ yang terpilih. Perbandingan peluang terpilih paling banyak 1 berkas ber-_bug_ terhadap peluang terpilih minimal 2 berkas ber-_bug_ adalah ....

- **A. $5 : 2$** ✅  
  <sub>Benar: Menghitung P(X <= 1) = 40/56 dan P(X >= 2) = 16/56, lalu menyederhanakan rasio 40 : 16 menjadi 5 : 2.</sub>
- B. $3 : 1$  
  <sub>Salah: Siswa salah menghitung kombinasi C(3, 2) * C(5, 1) sehingga rasio tereduksi salah.</sub>
- C. $2 : 5$  
  <sub>Salah: Siswa menyusun urutan perbandingan terbalik antara kejadian pertama dan kedua.</sub>
- D. $4 : 3$  
  <sub>Salah: Siswa lupa memperhitungkan kejadian X = 0 pada saat menghitung peluang paling banyak 1.</sub>

**Pembahasan:** Langkah 1: Menentukan total kemungkinan memilih 3 berkas dari 8 berkas.
$$n(S) = \binom{8}{3} = \frac{8 \times 7 \times 6}{3 \times 2 \times 1} = 56.$$

Langkah 2: Menentukan distribusi peluang $X$ untuk setiap nilai $x \in \{0, 1, 2, 3\}$.
- $P(X = 0) = \frac{\binom{3}{0} \binom{5}{3}}{56} = \frac{1 \times 10}{56} = \frac{10}{56}$
- $P(X = 1) = \frac{\binom{3}{1} \binom{5}{2}}{56} = \frac{3 \times 10}{56} = \frac{30}{56}$
- $P(X = 2) = \frac{\binom{3}{2} \binom{5}{1}}{56} = \frac{3 \times 5}{56} = \frac{15}{56}$
- $P(X = 3) = \frac{\binom{3}{3} \binom{5}{0}}{56} = \frac{1 \times 1}{56} = \frac{1}{56}$

Langkah 3: Menghitung $P(X \le 1)$ dan $P(X \ge 2)$.
$$P(X \le 1) = P(X = 0) + P(X = 1) = \frac{10}{56} + \frac{30}{56} = \frac{40}{56}$$
$$P(X \ge 2) = P(X = 2) + P(X = 3) = \frac{15}{56} + \frac{1}{56} = \frac{16}{56}$$

Langkah 4: Menentukan perbandingan.
$$P(X \le 1) : P(X \ge 2) = \frac{40}{56} : \frac{16}{56} = 40 : 16 = 5 : 2.$$
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-3

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-d-hard-bt01-006
*orisinal | C6 | 4 langkah | jenis: perancangan batas daerah nilai fungsi peluang*

Sebuah fungsi peluang dari variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} \frac{c}{x(x+1)}, & \text{untuk } x \in \{1, 2, 3, \dots, n\} \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Jika diketahui nilai konstanta $c = \frac{6}{5}$, nilai batas atas bilangan bulat positif $n$ yang membuat $f(x)$ menjadi fungsi peluang yang sah adalah ....

- A. 7  
  <sub>Salah: Siswa melakukan kesalahan perhitungan pada penjumlahan suku-suku deret parsial.</sub>
- B. 4  
  <sub>Salah: Siswa keliru memproses persamaan aljabar saat perkalian silang menjadi 6n - 6 = 5n.</sub>
- C. 6  
  <sub>Salah: Siswa salah menuliskan bentuk akhir deret pecahan parsial menjadi (n+1)/n bukannya n/(n+1).</sub>
- **D. 5** ✅  
  <sub>Benar: Menggunakan deret teleskopik sum 1/(x(x+1)) = n/(n+1), lalu menetapkan c * n/(n+1) = 1 dengan c = 6/5 menghasilkan 6n = 5(n+1) sehingga n = 5.</sub>

**Pembahasan:** Langkah 1: Menguraikan bentuk pecahan ke dalam pecahan parsial.
$$\frac{1}{x(x+1)} = \frac{1}{x} - \frac{1}{x+1}.$$

Langkah 2: Menghitung jumlah deret dengan sifat teleskopik.
$$\sum_{x=1}^n \frac{1}{x(x+1)} = \sum_{x=1}^n \left(\frac{1}{x} - \frac{1}{x+1}\right)$$
$$= \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right) = 1 - \frac{1}{n+1} = \frac{n}{n+1}.$$

Langkah 3: Menerapkan syarat fungsi peluang $\sum_{x=1}^n f(x) = 1$.
$$\sum_{x=1}^n \frac{c}{x(x+1)} = c \cdot \frac{n}{n+1} = 1.$$

Langkah 4: Menyubstitusikan $c = \frac{6}{5}$ dan menyelesaikan persamaan untuk $n$.
$$\frac{6}{5} \cdot \frac{n}{n+1} = 1 \implies 6n = 5(n + 1) \implies 6n = 5n + 5 \implies n = 5.$$
Karena $n = 5$ menghasilkan $f(x) > 0$ untuk setiap $x \in \{1, 2, 3, 4, 5\}$, fungsi tersebut sah memenuhi seluruh syarat fungsi peluang.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-d-hard-bt01-007
*orisinal | C5 | 4 langkah | jenis: evaluasi selisih peluang variabel acak*

Sebuah kotak memuat 8 kartu yang masing-masing diberi nomor 1 sampai 8. Dua lembar kartu diambil secara acak sekaligus. Misalkan variabel acak $D$ menyatakan selisih mutlak dari kedua nomor kartu yang terambil. Nilai dari $P(D \le 2) - P(D \ge 5)$ adalah ....

- A. $\frac{9}{28}$  
  <sub>Salah: Siswa melewatkan pasangan yang memiliki selisih 5 sehingga pengurangnya bernilai terlalu kecil.</sub>
- B. $\frac{5}{28}$  
  <sub>Salah: Siswa salah menghitung cacah pasangan selisih 2 menjadi hanya 5 pasang.</sub>
- **C. $\frac{1}{4}$** ✅  
  <sub>Benar: Banyak pasangan dengan D <= 2 adalah 13 dan D >= 5 adalah 6 dari total 28 kombinasi, sehingga selisih peluangnya adalah 13/28 - 6/28 = 7/28 = 1/4.</sub>
- D. $\frac{3}{14}$  
  <sub>Salah: Siswa hanya menghitung nilai P(D >= 5) yaitu 6/28 = 3/14 tanpa mengurangkannya dari P(D <= 2).</sub>

**Pembahasan:** Langkah 1: Menentukan banyak anggota ruang sampel.
Pengambilan 2 kartu dari 8 kartu sekaligus:
$$n(S) = \binom{8}{2} = \frac{8 \times 7}{2} = 28.$$

Langkah 2: Menghitung banyak kemungkinan untuk kejadian $D \le 2$ (yaitu selisih mutlak bernilai 1 atau 2).
- Selisih 1: $\{1,2\}, \{2,3\}, \{3,4\}, \{4,5\}, \{5,6\}, \{6,7\}, \{7,8\}$ (ada 7 pasang).
- Selisih 2: $\{1,3\}, \{2,4\}, \{3,5\}, \{4,6\}, \{5,7\}, \{6,8\}$ (ada 6 pasang).
Total untuk $D \le 2$ adalah $7 + 6 = 13$ pasang, sehingga:
$$P(D \le 2) = \frac{13}{28}.$$

Langkah 3: Menghitung banyak kemungkinan untuk kejadian $D \ge 5$ (yaitu selisih mutlak bernilai 5, 6, atau 7).
- Selisih 5: $\{1,6\}, \{2,7\}, \{3,8\}$ (ada 3 pasang).
- Selisih 6: $\{1,7\}, \{2,8\}$ (ada 2 pasang).
- Selisih 7: $\{1,8\}$ (ada 1 pasang).
Total untuk $D \ge 5$ adalah $3 + 2 + 1 = 6$ pasang, sehingga:
$$P(D \ge 5) = \frac{6}{28}.$$

Langkah 4: Menghitung nilai selisih peluang.
$$P(D \le 2) - P(D \ge 5) = \frac{13}{28} - \frac{6}{28} = \frac{7}{28} = \frac{1}{4}.$$
**Acuan:** siswa — siswa hal.260

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-d-hard-bt01-008
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi peluang komplementer*

Sebuah laboratorium komputer menerima kiriman 15 unit diska lepas (_flashdisk_), dengan 5 di antaranya terinfeksi virus. Seorang laboran mengambil 4 unit diska lepas secara acak sekaligus untuk diuji. Misalkan variabel acak $V$ menyatakan banyaknya diska lepas terinfeksi virus yang terambil. Nilai perbandingan $P(V \ge 2) : P(V < 2)$ adalah ....

- A. $54 : 37$  
  <sub>Salah: Siswa terbalik meletakkan rasio antara $P(V < 2) : P(V \ge 2)$.</sub>
- **B. $37 : 54$** ✅  
  <sub>Benar: Banyak anggota ruang sampel adalah $\binom{15}{4} = 1.365$. Peluang masing-masing kejadian dihitung: $P(V = 0) = \frac{\binom{5}{0}\binom{10}{4}}{1.365} = \frac{210}{1.365}$ dan $P(V = 1) = \frac{\binom{5}{1}\binom{10}{3}}{1.365} = \frac{600}{1.365}$. Maka $P(V < 2) = \frac{210 + 600}{1.365} = \frac{810}{1.365}$, dan $P(V \ge 2) = 1 - \frac{810}{1.365} = \frac{555}{1.365}$. Perbandingannya adalah $555 : 810 = 37 : 54$.</sub>
- C. $37 : 91$  
  <sub>Salah: Siswa membandingkan $P(V \ge 2)$ terhadap peluang total 1, bukan terhadap $P(V < 2)$.</sub>
- D. $31 : 60$  
  <sub>Salah: Siswa salah menghitung kombinasi $\binom{10}{3}$ menjadi 100 sehingga mengira $P(V=1) = \frac{500}{1.365}$.</sub>

**Pembahasan:** Banyak cara memilih 4 diska lepas dari total 15 diska lepas:
$$n(S) = \binom{15}{4} = \frac{15 \times 14 \times 13 \times 12}{4 \times 3 \times 2 \times 1} = 1.365$$

Nilai $V$ yang memenuhi $V < 2$ adalah $V = 0$ dan $V = 1$:
- $P(V = 0) = \frac{\binom{5}{0} \times \binom{10}{4}}{1.365} = \frac{1 \times 210}{1.365} = \frac{210}{1.365}$
- $P(V = 1) = \frac{\binom{5}{1} \times \binom{10}{3}}{1.365} = \frac{5 \times 120}{1.365} = \frac{600}{1.365}$

Diperoleh:
$$P(V < 2) = P(V = 0) + P(V = 1) = \frac{210 + 600}{1.365} = \frac{810}{1.365}$$
$$P(V \ge 2) = 1 - P(V < 2) = 1 - \frac{810}{1.365} = \frac{555}{1.365}$$

Maka rasio perbandingannya:
$$\frac{P(V \ge 2)}{P(V < 2)} = \frac{555}{810} = \frac{555 \div 15}{810 \div 15} = \frac{37}{54}$$
Jadi, perbandingannya adalah $37 : 54$.
**Acuan:** siswa — siswa hal.261 Ayo Mencoba 4.4

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-d-hard-bt01-009
*variasi (angka) | C5 | 4 langkah | jenis: analisis perbandingan peluang kejadian*

Dalam suatu kuis cepat, diberikan 6 butir soal bertipe benar atau salah. Seorang peserta menjawab seluruh butir soal dengan menebak secara acak tanpa persiapan. Jika variabel acak $X$ menyatakan banyaknya soal yang dijawab dengan benar, nilai perbandingan $P(X \ge 5) : P(X = 4)$ adalah ....

- A. $1 : 2$  
  <sub>Salah: Siswa salah menjumlahkan $\binom{6}{5} + \binom{6}{6}$ menjadi 8 sehingga menghasilkan rasio $8 : 16 = 1 : 2$.</sub>
- B. $15 : 7$  
  <sub>Salah: Siswa terbalik menuliskan urutan perbandingan kejadian yang ditanyakan.</sub>
- **C. $7 : 15$** ✅  
  <sub>Benar: Ruang sampel pelemparan 6 soal benar-salah adalah $2^6 = 64$. Diperoleh $P(X = 4) = \frac{\binom{6}{4}}{64} = \frac{15}{64}$, $P(X = 5) = \frac{\binom{6}{5}}{64} = \frac{6}{64}$, dan $P(X = 6) = \frac{\binom{6}{6}}{64} = \frac{1}{64}$. Maka $P(X \ge 5) = \frac{6 + 1}{64} = \frac{7}{64}$. Rasio perbandingannya adalah $7 : 15$.</sub>
- D. $2 : 5$  
  <sub>Salah: Siswa hanya menghitung $P(X = 5)$ tanpa menambahkan $P(X = 6)$ pada $P(X \ge 5)$, sehingga rasionya $6 : 15 = 2 : 5$.</sub>

**Pembahasan:** Peluang menjawab benar pada tiap soal adalah $p = \frac{1}{2}$ dan salah $q = \frac{1}{2}$.
Total kemungkinan jawaban untuk 6 butir soal adalah $n(S) = 2^6 = 64$.

Fungsi peluang untuk variabel acak $X$ adalah:
$$P(X = x) = \frac{\binom{6}{x}}{64}$$

1. Menghitung $P(X = 4)$:
$$P(X = 4) = \frac{\binom{6}{4}}{64} = \frac{15}{64}$$

2. Menghitung $P(X \ge 5)$:
$$P(X \ge 5) = P(X = 5) + P(X = 6) = \frac{\binom{6}{5} + \binom{6}{6}}{64} = \frac{6 + 1}{64} = \frac{7}{64}$$

3. Membandingkan kedua peluang:
$$P(X \ge 5) : P(X = 4) = \frac{7}{64} : \frac{15}{64} = 7 : 15$$
**Acuan:** pretest — kelas12_tl-b04-p0264-latihan-soal-fungsi-peluang-5

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-d-hard-bt01-010
*orisinal | C5 | 4 langkah | jenis: analisis rasio parameter peluang*

Diberikan suatu fungsi peluang untuk variabel acak diskret $X$ dengan daerah nilai $x \in \{1, 2, 3, 4, 5\}$ didefinisikan sebagai:
$$f(x) = \begin{cases} c(k - |x - 3|), & \text{untuk } x \in \{1, 2, 3, 4, 5\} \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Jika fungsi tersebut memenuhi seluruh syarat fungsi peluang dan diketahui $P(X = 3) = \frac{1}{3}$, nilai konstanta $k$ yang memenuhi adalah ....

- A. 4  
  <sub>Salah: Siswa salah menjumlahkan suku konstan $|x-3|$ menjadi $2+1+0+1+2 = 4$ bukan 6.</sub>
- B. 2  
  <sub>Salah: Siswa hanya menggunakan batas syarat non-negatif $k - 2 \ge 0$ sehingga mengira $k = 2$.</sub>
- C. 5  
  <sub>Salah: Siswa salah menyelesaikan persamaan aljabar $5k - 6 = 3k$ menjadi $5k - 3k = 10$.</sub>
- **D. 3** ✅  
  <sub>Benar: Nilai $|x - 3|$ untuk $x = 1, 2, 3, 4, 5$ berturut-turut adalah $2, 1, 0, 1, 2$. Total peluang $\sum f(x) = c[(k-2) + (k-1) + k + (k-1) + (k-2)] = c(5k - 6) = 1$. Diketahui $P(X = 3) = ck = \frac{1}{3}$, sehingga $c = \frac{1}{3k}$. Substitusikan ke persamaan total peluang: $\frac{5k - 6}{3k} = 1 \iff 5k - 6 = 3k \iff 2k = 6 \iff k = 3$.</sub>

**Pembahasan:** Hitung nilai $f(x)$ untuk setiap $x \in \{1, 2, 3, 4, 5\}$:
- $f(1) = c(k - |1 - 3|) = c(k - 2)$
- $f(2) = c(k - |2 - 3|) = c(k - 1)$
- $f(3) = c(k - |3 - 3|) = c(k)$
- $f(4) = c(k - |4 - 3|) = c(k - 1)$
- $f(5) = c(k - |5 - 3|) = c(k - 2)$

Syarat fungsi peluang diskret mensyaratkan $\sum_{x=1}^{5} f(x) = 1$:
$$c[(k - 2) + (k - 1) + k + (k - 1) + (k - 2)] = 1$$
$$c(5k - 6) = 1 \implies c = \frac{1}{5k - 6}$$

Diketahui pada soal bahwa:
$$P(X = 3) = f(3) = c \cdot k = \frac{1}{3}$$

Substitusikan nilai $c$:
$$\frac{k}{5k - 6} = \frac{1}{3}$$
$$3k = 5k - 6$$
$$2k = 6 \implies k = 3$$

Periksa keabsahan: untuk $k = 3$, $c = \frac{1}{5(3) - 6} = \frac{1}{9}$. Nilai $f(x) \ge 0$ untuk setiap $x \in \{1, 2, 3, 4, 5\}$, sehingga memenuhi seluruh kriteria fungsi peluang.
**Acuan:** siswa — siswa hal.259

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-d-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: evaluasi kesetaraan distribusi peluang*

Fungsi peluang suatu variabel acak diskret $Y$ didefinisikan sebagai:
$$g(y) = \begin{cases} \frac{a y^2 + 1}{34}, & \text{untuk } y \in \{-2, -1, 1, 2\} \\ 0, & \text{untuk } y \text{ lainnya} \end{cases}$$
Jika $g(y)$ merupakan fungsi peluang yang sah dan didefinisikan variabel acak baru $W = Y^2$, nilai dari $P(W = 4)$ adalah ....

- **A. $\frac{13}{17}$** ✅  
  <sub>Benar: Syarat total peluang $\sum g(y) = 1$: $\frac{(4a+1) + (a+1) + (a+1) + (4a+1)}{34} = \frac{10a + 4}{34} = 1 \implies 10a + 4 = 34 \implies a = 3$. Kejadian $W = 4$ terjadi saat $Y^2 = 4$, yaitu $Y = -2$ atau $Y = 2$. Maka $P(W = 4) = g(-2) + g(2) = \frac{3(-2)^2 + 1}{34} + \frac{3(2)^2 + 1}{34} = \frac{13}{34} + \frac{13}{34} = \frac{26}{34} = \frac{13}{17}$.</sub>
- B. $\frac{9}{17}$  
  <sub>Salah: Siswa salah mencari nilai $a$ menjadi $a = 2$ sehingga mendapatkan $P(W = 4) = \frac{9+9}{34} = \frac{9}{17}$.</sub>
- C. $\frac{4}{17}$  
  <sub>Salah: Siswa salah menentukan nilai kejadian $W = 4$ dengan menghitung $P(W = 1)$ yang nilainya $\frac{8}{34} = \frac{4}{17}$.</sub>
- D. $\frac{13}{34}$  
  <sub>Salah: Siswa hanya menghitung salah satu cabang peluang, yaitu $P(Y = 2)$, tanpa memperhitungkan bahwa $(-2)^2$ juga menghasilkan 4.</sub>

**Pembahasan:** 1. Menentukan nilai parameter $a$:
Syarat utama fungsi peluang adalah $\sum_{y} g(y) = 1$.
$$g(-2) + g(-1) + g(1) + g(2) = 1$$
$$\frac{a(-2)^2 + 1}{34} + \frac{a(-1)^2 + 1}{34} + \frac{a(1)^2 + 1}{34} + \frac{a(2)^2 + 1}{34} = 1$$
$$\frac{(4a + 1) + (a + 1) + (a + 1) + (4a + 1)}{34} = 1$$
$$\frac{10a + 4}{34} = 1$$
$$10a + 4 = 34 \implies 10a = 30 \implies a = 3$$

Periksa non-negatif: untuk $a = 3$, $g(y) > 0$ untuk setiap daerah asal, sehingga $g(y)$ sah.

2. Menentukan nilai peluang untuk setiap nilai $y$:
- $g(-2) = \frac{3(4) + 1}{34} = \frac{13}{34}$
- $g(2) = \frac{3(4) + 1}{34} = \frac{13}{34}$

3. Menghitung $P(W = 4)$ dengan $W = Y^2$:
Nilai $W = 4$ terjadi ketika $Y^2 = 4$, yaitu saat $Y = -2$ atau $Y = 2$.
$$P(W = 4) = P(Y = -2) + P(Y = 2) = \frac{13}{34} + \frac{13}{34} = \frac{26}{34} = \frac{13}{17}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-d-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: penalaran pola barisan fungsi peluang*

Sebuah variabel acak diskret $X$ memiliki ruang nilai $x \in \{1, 2, 3, 4, 5\}$. Nilai-nilai peluang $f(x) = P(X = x)$ diketahui membentuk barisan aritmetika dengan beda tetap $d$. Jika $P(X \le 2) = \frac{1}{5}$, nilai dari $P(X \ge 4)$ adalah ....

- A. $\frac{2}{5}$  
  <sub>Salah: Salah mengurangkan atau menghitung nilai komplemen yang keliru.</sub>
- B. $\frac{4}{15}$  
  <sub>Salah: Hanya menghitung nilai titik $P(X = 4) = f(4)$, lupa menjumlahkan dengan $f(5)$.</sub>
- **C. $\frac{3}{5}$** ✅  
  <sub>Benar: Berdasarkan sifat total peluang $\sum_{x=1}^{5} f(x) = 1$, diperoleh $5a + 10d = 1 \iff a + 2d = \frac{1}{5}$. Diketahui pula $P(X \le 2) = f(1) + f(2) = 2a + d = \frac{1}{5}$. Dari kedua persamaan ini didapat $a = \frac{1}{15}$ dan $d = \frac{1}{15}$. Dengan demikian, $P(X \ge 4) = f(4) + f(5) = (a + 3d) + (a + 4d) = \frac{4}{15} + \frac{5}{15} = \frac{9}{15} = \frac{3}{5}$.</sub>
- D. $\frac{1}{3}$  
  <sub>Salah: Salah menafsirkan tanda pertidaksamaan sebagai $P(X > 4) = f(5) = \frac{5}{15} = \frac{1}{3}$.</sub>

**Pembahasan:** Misalkan $f(1) = a$. Karena membentuk barisan aritmetika dengan beda $d$, maka:
- $f(1) = a$
- $f(2) = a + d$
- $f(3) = a + 2d$
- $f(4) = a + 3d$
- $f(5) = a + 4d$

1. Sifat fungsi peluang mensyaratkan total seluruh peluang sama dengan 1:
$$\sum_{x=1}^{5} f(x) = 1$$
$$5a + 10d = 1 \implies a + 2d = \frac{1}{5} \quad \text{...(Persamaan 1)}$$

2. Dari informasi soal:
$$P(X \le 2) = f(1) + f(2) = a + (a + d) = 2a + d = \frac{1}{5} \quad \text{...(Persamaan 2)}$$

3. Eliminasi Persamaan (1) dan (2):
$$2(a + 2d) - (2a + d) = 2\left(\frac{1}{5}\right) - \frac{1}{5}$$
$$3d = \frac{1}{5} \implies d = \frac{1}{15}$$

Substitusikan nilai $d$ ke Persamaan (1):
$$a + 2\left(\frac{1}{15}\right) = \frac{3}{15} \implies a = \frac{1}{15}$$

4. Menghitung nilai $P(X \ge 4)$:
$$P(X \ge 4) = f(4) + f(5)$$
$$f(4) = a + 3d = \frac{1}{15} + \frac{3}{15} = \frac{4}{15}$$
$$f(5) = a + 4d = \frac{1}{15} + \frac{4}{15} = \frac{5}{15}$$
$$P(X \ge 4) = \frac{4}{15} + \frac{5}{15} = \frac{9}{15} = \frac{3}{5}$$

Jadi, nilai dari $P(X \ge 4)$ adalah $\frac{3}{5}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-d-hard-bt01-013
*variasi (konteks) | C5 | 4 langkah | jenis: analisis perbandingan peluang kumulatif*

Sebuah kotak suku cadang memuat 6 mur baja, 3 mur tembaga, dan 5 mur kuningan. Sebanyak 3 butir mur diambil secara acak sekaligus dari dalam kotak tersebut. Jika variabel acak $K$ menyatakan banyaknya mur kuningan yang terambil, perbandingan nilai $P(K \le 1)$ terhadap $P(K \ge 2)$ adalah ....

- A. $33 : 19$  
  <sub>Salah: Siswa salah menghitung kombinasi non-kuningan untuk $K=0$ menjadi $\binom{9}{3} = 72$.</sub>
- B. $25 : 66$  
  <sub>Salah: Siswa membalik urutan perbandingan menjadi $P(K \ge 2) : P(K \le 1)$.</sub>
- **C. $66 : 25$** ✅  
  <sub>Benar: Total mur adalah $6 + 3 + 5 = 14$. Banyak cara memilih 3 mur dari 14 mur adalah $\binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 364$. Mur kuningan berjumlah 5 dan non-kuningan berjumlah 9. Nilai peluang masing-masing: $P(K=0) = \frac{\binom{5}{0}\binom{9}{3}}{364} = \frac{1 \times 84}{364} = \frac{84}{364}$, $P(K=1) = \frac{\binom{5}{1}\binom{9}{2}}{364} = \frac{5 \times 36}{364} = \frac{180}{364}$, $P(K=2) = \frac{\binom{5}{2}\binom{9}{1}}{364} = \frac{10 \times 9}{364} = \frac{90}{364}$, dan $P(K=3) = \frac{\binom{5}{3}\binom{9}{0}}{364} = \frac{10 \times 1}{364} = \frac{10}{364}$. Dengan demikian, $P(K \le 1) = \frac{84 + 180}{364} = \frac{264}{364}$ dan $P(K \ge 2) = \frac{90 + 10}{364} = \frac{100}{364}$. Perbandingannya adalah $264 : 100 = 66 : 25$.</sub>
- D. $45 : 19$  
  <sub>Salah: Siswa lupa memperhitungkan kasus $K=0$ pada $P(K \le 1)$ sehingga hanya menghitung $P(K=1) : P(K \ge 2) = 180 : 100$.</sub>

**Pembahasan:** Langkah 1: Menghitung ukuran ruang sampel:
$$n(S) = \binom{14}{3} = \frac{14 \times 13 \times 12}{3 \times 2 \times 1} = 364$$

Langkah 2: Menghitung nilai peluang untuk setiap nilai $K \in \{0, 1, 2, 3\}$:
- $P(K = 0) = \frac{\binom{5}{0}\binom{9}{3}}{364} = \frac{1 \times 84}{364} = \frac{84}{364}$
- $P(K = 1) = \frac{\binom{5}{1}\binom{9}{2}}{364} = \frac{5 \times 36}{364} = \frac{180}{364}$
- $P(K = 2) = \frac{\binom{5}{2}\binom{9}{1}}{364} = \frac{10 \times 9}{364} = \frac{90}{364}$
- $P(K = 3) = \frac{\binom{5}{3}\binom{9}{0}}{364} = \frac{10 \times 1}{364} = \frac{10}{364}$

Langkah 3: Menghitung peluang kumulatif yang diminta:
- $P(K \le 1) = P(K = 0) + P(K = 1) = \frac{84 + 180}{364} = \frac{264}{364}$
- $P(K \ge 2) = P(K = 2) + P(K = 3) = \frac{90 + 10}{364} = \frac{100}{364}$

Langkah 4: Menentukan perbandingan:
$$\frac{P(K \le 1)}{P(K \ge 2)} = \frac{264}{100} = \frac{66}{25}$$
Jadi, perbandingannya adalah $66 : 25$.
**Acuan:** pretest — kelas12_tl-b04-p0263-latihan-soal-fungsi-peluang-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-d-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: evaluasi kebenaran fungsi peluang nilai mutlak*

Fungsi peluang suatu variabel acak diskret $W$ didefinisikan sebagai:
$$f(w) = \begin{cases} c(3 - |w|), & \text{untuk } w \in \{-2, -1, 0, 1, 2\} \\ 0, & \text{untuk } w \text{ lainnya} \end{cases}$$
Perhatikan pernyataan-pernyataan berikut:
(1) Nilai $c = \frac{1}{9}$.
(2) Nilai $P(W > 0) = \frac{1}{3}$.
(3) Nilai $P(W \le 0) = \frac{5}{9}$.
(4) Nilai $P(|W| = 1) = \frac{4}{9}$.

Pernyataan yang bernilai benar adalah ....

- A. (1) dan (2) saja  
  <sub>Salah: Siswa tidak menyadari bahwa $|W| = 1$ mencakup $w = -1$ dan $w = 1$ sehingga mengira pernyataan (4) bernilai salah.</sub>
- B. (1), (3), dan (4)  
  <sub>Salah: Siswa salah mengira $P(W \le 0)$ tidak mengikutsertakan $w = 0$ sehingga mendapatkan $\frac{3}{9}$ lalu salah hitung menjadi $\frac{5}{9}$.</sub>
- C. (2) dan (3) saja  
  <sub>Salah: Siswa salah menentukan nilai konstanta $c$ dan salah mengevaluasi pernyataan (3).</sub>
- **D. (1), (2), dan (4)** ✅  
  <sub>Benar: Total peluang: $\sum_{w=-2}^{2} c(3 - |w|) = c[(3-2) + (3-1) + (3-0) + (3-1) + (3-2)] = c[1 + 2 + 3 + 2 + 1] = 9c = 1 \implies c = \frac{1}{9}$ (Pernyataan 1 BENAR). Untuk pernyataan 2: $P(W > 0) = f(1) + f(2) = \frac{2}{9} + \frac{1}{9} = \frac{3}{9} = \frac{1}{3}$ (BENAR). Untuk pernyataan 3: $P(W \le 0) = f(-2) + f(-1) + f(0) = \frac{1}{9} + \frac{2}{9} + \frac{3}{9} = \frac{6}{9} = \frac{2}{3} \ne \frac{5}{9}$ (SALAH). Untuk pernyataan 4: $P(|W| = 1) = f(-1) + f(1) = \frac{2}{9} + \frac{2}{9} = \frac{4}{9}$ (BENAR). Jadi, pernyataan yang benar adalah (1), (2), dan (4).</sub>

**Pembahasan:** Langkah 1: Menentukan nilai $c$ agar $\sum f(w) = 1$:
$$\sum_{w=-2}^{2} c(3 - |w|) = c(1 + 2 + 3 + 2 + 1) = 9c = 1 \implies c = \frac{1}{9}$$
Karena $3 - |w| > 0$ untuk seluruh $w \in \{-2, -1, 0, 1, 2\}$, syarat $f(w) \ge 0$ terpenuhi. Maka pernyataan (1) BENAR.

Langkah 2: Memeriksa pernyataan (2):
$$P(W > 0) = f(1) + f(2) = \frac{3 - 1}{9} + \frac{3 - 2}{9} = \frac{2}{9} + \frac{1}{9} = \frac{3}{9} = \frac{1}{3}$$
Pernyataan (2) BENAR.

Langkah 3: Memeriksa pernyataan (3):
$$P(W \le 0) = f(-2) + f(-1) + f(0) = \frac{1}{9} + \frac{2}{9} + \frac{3}{9} = \frac{6}{9} = \frac{2}{3} \ne \frac{5}{9}$$
Pernyataan (3) SALAH.

Langkah 4: Memeriksa pernyataan (4):
Kejadian $|W| = 1$ terjadi jika $w = -1$ atau $w = 1$.
$$P(|W| = 1) = f(-1) + f(1) = \frac{2}{9} + \frac{2}{9} = \frac{4}{9}$$
Pernyataan (4) BENAR.

Dengan demikian, pernyataan yang benar adalah (1), (2), dan (4).
**Acuan:** siswa — siswa hal.261

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-d-hard-bt01-015
*orisinal | C5 | 5 langkah | jenis: pemodelan fungsi peluang nilai maksimum*

Sebuah kantong memuat 4 bola bernomor 1, 2, 3, dan 4. Dua bola diambil satu per satu tanpa pengembalian. Misalkan variabel acak $M$ menyatakan nilai terbesar (maksimum) di antara kedua nomor bola yang terambil. Jika fungsi peluang dari $M$ dinyatakan dalam bentuk:
$$P(M = m) = \begin{cases} \frac{a \cdot m + b}{12}, & \text{untuk } m \in \{2, 3, 4\} \\ 0, & \text{untuk } m \text{ lainnya} \end{cases}$$
maka nilai dari $a^2 + b^2$ adalah ....

- **A. 8** ✅  
  <sub>Benar: Ruang sampel penarikan 2 bola berurutan tanpa pengembalian memiliki $4 \times 3 = 12$ anggota. Nilai $M$ yang mungkin adalah 2, 3, dan 4. Nilai $M=2$ terjadi pada pasangan (1,2) dan (2,1) (2 hasil), sehingga $P(M=2) = \frac{2}{12}$. Nilai $M=3$ terjadi pada (1,3), (3,1), (2,3), (3,2) (4 hasil), sehingga $P(M=3) = \frac{4}{12}$. Nilai $M=4$ terjadi pada (1,4), (4,1), (2,4), (4,2), (3,4), (4,3) (6 hasil), sehingga $P(M=4) = \frac{6}{12}$. Dari rumus fungsi peluang: untuk $m=2 \implies 2a + b = 2$, dan untuk $m=3 \implies 3a + b = 4$. Mengurangkan kedua persamaan menghasilkan $a = 2$. Substitusi ke $2(2) + b = 2$ menghasilkan $b = -2$. Untuk $m=4$, $4(2) + (-2) = 6$ (konsisten). Maka $a^2 + b^2 = 2^2 + (-2)^2 = 4 + 4 = 8$.</sub>
- B. 10  
  <sub>Salah: Siswa keliru menyelesaikan eliminasi sehingga memperoleh $a=3$ dan $b=-1$, menghasilkan $3^2 + (-1)^2 = 10$.</sub>
- C. 0  
  <sub>Salah: Siswa keliru menjumlahkan $(a+b)^2 = (2 + (-2))^2 = 0$ alih-alih $a^2 + b^2$.</sub>
- D. 4  
  <sub>Salah: Siswa hanya menghitung nilai $a^2$ dan mengabaikan $b^2$ karena mengira $b=0$.</sub>

**Pembahasan:** Langkah 1: Menentukan ruang sampel penarikan 2 bola satu per satu tanpa pengembalian:
$$n(S) = 4 \times 3 = 12$$

Langkah 2: Menentukan frekuensi kemunculan nilai maksimum $M$:
- $M = 2$: pasangan $\{(1,2), (2,1)\} \implies n = 2 \implies P(M=2) = \frac{2}{12}$
- $M = 3$: pasangan $\{(1,3), (3,1), (2,3), (3,2)\} \implies n = 4 \implies P(M=3) = \frac{4}{12}$
- $M = 4$: pasangan $\{(1,4), (4,1), (2,4), (4,2), (3,4), (4,3)\} \implies n = 6 \implies P(M=4) = \frac{6}{12}$

Langkah 3: Membentuk sistem persamaan linier dari $P(M = m) = \frac{am + b}{12}$:
Untuk $m = 2$: $2a + b = 2$
Untuk $m = 3$: $3a + b = 4$

Langkah 4: Menyelesaikan nilai $a$ dan $b$:
Kurangkan kedua persamaan:
$$(3a + b) - (2a + b) = 4 - 2 \implies a = 2$$
Substitusikan nilai $a = 2$ ke dalam persamaan pertama:
$$2(2) + b = 2 \implies 4 + b = 2 \implies b = -2$$
Cek pada $m = 4$: $am + b = 2(4) + (-2) = 6$ (sesuai).

Langkah 5: Menghitung nilai $a^2 + b^2$:
$$a^2 + b^2 = 2^2 + (-2)^2 = 4 + 4 = 8$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-d-hard-bt01-016
*orisinal | C6 | 5 langkah | jenis: konstruksi parameter sistem fungsi peluang*

Sebuah fungsi peluang dari variabel acak diskret $Y$ didefinisikan sebagai:
$$f(y) = \begin{cases} a y + b, & \text{untuk } y \in \{1, 2, 3\} \\ 0, & \text{untuk } y \text{ lainnya} \end{cases}$$
Diketahui $f(y)$ memenuhi definisi fungsi peluang diskret. Jika nilai peluang $P(Y = 3)$ tepat bernilai dua kali lipat dari $P(Y = 1)$, nilai dari $f(2)$ adalah ....

- **A. $\frac{1}{3}$** ✅  
  <sub>Benar: Dari syarat total peluang: $(a+b) + (2a+b) + (3a+b) = 1 \implies 6a + 3b = 1$. Dari syarat perbandingan: $f(3) = 2f(1) \implies 3a + b = 2(a + b) \implies a = b$. Substitusi $a=b$ ke $6a + 3b = 1$ menghasilkan $9a = 1 \implies a = b = \frac{1}{9}$. Maka $f(2) = 2a + b = 2\left(\frac{1}{9}\right) + \frac{1}{9} = \frac{3}{9} = \frac{1}{3}$. Nilai ini juga memenuhi $f(y) \ge 0$ untuk setiap $y$.</sub>
- B. $\frac{2}{9}$  
  <sub>Salah: Siswa hanya menghitung komponen $2a$ dari rumus $2a+b$ dan lupa menambahkan suku $+b$.</sub>
- C. $\frac{4}{9}$  
  <sub>Salah: Siswa salah menjumlahkan koefisien $a$ pada total peluang menjadi $4a+3b=1$ sehingga nilai parameter menjadi tidak tepat.</sub>
- D. $\frac{1}{4}$  
  <sub>Salah: Siswa keliru menganggap pembagi total adalah 12 sehingga memperoleh $f(2) = \frac{3}{12} = \frac{1}{4}$.</sub>

**Pembahasan:** Langkah 1: Menuliskan nilai peluang untuk tiap domain $y \in \{1, 2, 3\}$.
$f(1) = a(1) + b = a + b$
$f(2) = a(2) + b = 2a + b$
$f(3) = a(3) + b = 3a + b$

Langkah 2: Menggunakan syarat fungsi peluang $\sum f(y) = 1$.
$$(a + b) + (2a + b) + (3a + b) = 1$$
$$6a + 3b = 1 \quad \text{--- (Persamaan 1)}$$

Langkah 3: Menggunakan hubungan $P(Y = 3) = 2 \cdot P(Y = 1)$.
$$3a + b = 2(a + b)$$
$$3a + b = 2a + 2b \implies a = b \quad \text{--- (Persamaan 2)}$$

Langkah 4: Menyelesaikan sistem persamaan linier.
Substitusi $b = a$ ke Persamaan 1:
$$6a + 3(a) = 1 \implies 9a = 1 \implies a = \frac{1}{9}$$
Karena $a = b$, maka $b = \frac{1}{9}$.
Semua nilai peluang tak negatif ($f(1) = \frac{2}{9} > 0$, $f(2) = \frac{3}{9} > 0$, $f(3) = \frac{4}{9} > 0$), sehingga fungsi peluang sah.

Langkah 5: Menghitung $f(2)$.
$$f(2) = 2a + b = 2\left(\frac{1}{9}\right) + \frac{1}{9} = \frac{3}{9} = \frac{1}{3}$$
Jadi, nilai $f(2) = \frac{1}{3}$.
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-d-hard-bt01-017
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi rasio fungsi peluang*

Sebuah inkubator riset memuat 6 bibit tanaman varietas unggul dan 4 bibit varietas lokal. Sebanyak 3 bibit diambil secara acak sekaligus untuk ditanam di lahan percobaan. Jika variabel acak $Y$ menyatakan banyak bibit varietas lokal yang terambil dengan fungsi peluang $f(y) = P(Y = y)$, nilai dari $\frac{f(1) \cdot f(2)}{f(0) \cdot f(3)}$ adalah ....

- A. 18  
  <sub>Salah: Siswa salah menghitung nilai $f(2)$ dengan mengalikan $\binom{4}{2} = 6$ dengan 3 bibit unggul tersisa alih-alih $\binom{6}{1} = 6$, menghasilkan pembilang yang terbagi dua.</sub>
- **B. 27** ✅  
  <sub>Benar: Banyak cara memilih 3 bibit dari total 10 bibit adalah $n(S) = \binom{10}{3} = 120$. Nilai $Y$ yang mungkin adalah $y \in \{0, 1, 2, 3\}$. Nilai peluang untuk tiap $y$ diperoleh melalui rumus kombinasi: $f(0) = \frac{\binom{4}{0}\binom{6}{3}}{120} = \frac{1 \times 20}{120} = \frac{20}{120}$, $f(1) = \frac{\binom{4}{1}\binom{6}{2}}{120} = \frac{4 \times 15}{120} = \frac{60}{120}$, $f(2) = \frac{\binom{4}{2}\binom{6}{1}}{120} = \frac{6 \times 6}{120} = \frac{36}{120}$, dan $f(3) = \frac{\binom{4}{3}\binom{6}{0}}{120} = \frac{4 \times 1}{120} = \frac{4}{120}$. Maka rasio yang dicari adalah $\frac{f(1) \cdot f(2)}{f(0) \cdot f(3)} = \frac{60 \times 36}{20 \times 4} = \frac{2160}{80} = 27$.</sub>
- C. 54  
  <sub>Salah: Siswa salah menghitung kombinasi $\binom{6}{2}$ menjadi 30 (bukan 15) karena lupa membagi dengan $2!$, sehingga memperoleh $f(1) = \frac{120}{120}$ dan hasil rasio menjadi 54.</sub>
- D. 4  
  <sub>Salah: Siswa keliru mengevaluasi operasi perkalian menjadi penjumlahan, yaitu menghitung $\frac{f(1) + f(2)}{f(0) + f(3)} = \frac{60 + 36}{20 + 4} = \frac{96}{24} = 4$.</sub>

**Pembahasan:** Langkah 1: Menentukan banyak anggota ruang sampel.
Total bibit adalah $6 + 4 = 10$ bibit. Diambil 3 bibit sekaligus:
$$n(S) = \binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

Langkah 2: Menentukan fungsi peluang $f(y)$ untuk $y \in \{0, 1, 2, 3\}$.
$$f(y) = P(Y = y) = \frac{\binom{4}{y}\binom{6}{3-y}}{\binom{10}{3}}$$

Langkah 3: Menghitung nilai peluang untuk masing-masing nilai $y$:
- $f(0) = \frac{\binom{4}{0}\binom{6}{3}}{120} = \frac{1 \times 20}{120} = \frac{20}{120}$
- $f(1) = \frac{\binom{4}{1}\binom{6}{2}}{120} = \frac{4 \times 15}{120} = \frac{60}{120}$
- $f(2) = \frac{\binom{4}{2}\binom{6}{1}}{120} = \frac{6 \times 6}{120} = \frac{36}{120}$
- $f(3) = \frac{\binom{4}{3}\binom{6}{0}}{120} = \frac{4 \times 1}{120} = \frac{4}{120}$

Langkah 4: Menghitung nilai ekspresi yang ditanyakan:
$$\frac{f(1) \cdot f(2)}{f(0) \cdot f(3)} = \frac{\frac{60}{120} \times \frac{36}{120}}{\frac{20}{120} \times \frac{4}{120}} = \frac{60 \times 36}{20 \times 4} = 3 \times 9 = 27$$

Jadi, nilai dari $\frac{f(1) \cdot f(2)}{f(0) \cdot f(3)}$ adalah 27.
**Acuan:** siswa — siswa hal.259 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 58. [hard] kelas12_tl-b04-d-hard-bt01-018
*orisinal | C5 | 5 langkah | jenis: analisis rasio peluang himpunan bagian*

Fungsi peluang dari suatu variabel acak diskret $X$ didefinisikan sebagai:
$$f(x) = \begin{cases} c(6 - |x - 4|), & \text{untuk } x \in \{1, 2, 3, 4, 5, 6\} \\ 0, & \text{untuk } x \text{ lainnya} \end{cases}$$
Rasio antara peluang terpilihnya $X$ bernilai bilangan prima terhadap peluang terpilihnya $X$ bukan bilangan prima adalah ....

- A. $13 : 14$  
  <sub>Salah: Siswa membalik urutan pembanding (bukan prima terhadap prima).</sub>
- **B. $14 : 13$** ✅  
  <sub>Benar: Evaluasi bobot $w(x) = 6 - |x - 4|$ untuk tiap $x \in \{1, 2, 3, 4, 5, 6\}$ menghasilkan berturut-turut $3, 4, 5, 6, 5, 4$. Total bobot adalah $\sum w(x) = 3 + 4 + 5 + 6 + 5 + 4 = 27$, sehingga $c = \frac{1}{27}$. Himpunan bilangan prima pada daerah nilai adalah $\{2, 3, 5\}$, dengan peluang $P(X \text{ prima}) = c(4 + 5 + 5) = 14c = \frac{14}{27}$. Himpunan bukan prima adalah $\{1, 4, 6\}$, dengan peluang $P(X \text{ bukan prima}) = c(3 + 6 + 4) = 13c = \frac{13}{27}$. Jadi, rasionya adalah $14 : 13$.</sub>
- C. $1 : 1$  
  <sub>Salah: Siswa berasumsi peluangnya sama karena masing-masing himpunan memiliki tepat 3 anggota tanpa memperhitungkan bobot fungsi peluangnya.</sub>
- D. $17 : 10$  
  <sub>Salah: Siswa salah menganggap bilangan 1 sebagai bilangan prima sehingga peluang prima dihitung $f(1)+f(2)+f(3)+f(5) = \frac{17}{27}$.</sub>

**Pembahasan:** Langkah 1: Hitung nilai $6 - |x - 4|$ untuk tiap nilai $x$:
- $f(1) = c(6 - |-3|) = 3c$
- $f(2) = c(6 - |-2|) = 4c$
- $f(3) = c(6 - |-1|) = 5c$
- $f(4) = c(6 - |0|) = 6c$
- $f(5) = c(6 - |1|) = 5c$
- $f(6) = c(6 - |2|) = 4c$

Langkah 2: Gunakan syarat $\sum f(x) = 1$:
$$(3 + 4 + 5 + 6 + 5 + 4)c = 1 \implies 27c = 1 \implies c = \frac{1}{27}$$

Langkah 3: Kelompokkan nilai $x$:
- Bilangan prima: $\{2, 3, 5\}$
- Bukan bilangan prima: $\{1, 4, 6\}$

Langkah 4: Hitung peluang masing-masing kelompok:
$$P(X \text{ prima}) = f(2) + f(3) + f(5) = \frac{4 + 5 + 5}{27} = \frac{14}{27}$$
$$P(X \text{ bukan prima}) = f(1) + f(4) + f(6) = \frac{3 + 6 + 4}{27} = \frac{13}{27}$$

Langkah 5: Tentukan rasio perbandingannya:
$$\text{Rasio} = \frac{14}{27} : \frac{13}{27} = 14 : 13$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 59. [hard] kelas12_tl-b04-d-hard-bt01-019
*orisinal | C5 | 5 langkah | jenis: evaluasi selisih peluang komposit*

Sebuah variabel acak diskret $Y$ memiliki daerah nilai $y \in \{0, 1, 2, 3\}$. Distribusi peluang dari $Y$ diketahui memenuhi:
- $P(Y = 0) = a$
- $P(Y = 1) = b$
- $P(Y = 2) = 2a$
- $P(Y = 3) = a + b$

Jika diketahui bahwa peluang diperolehnya nilai $Y$ bilangan cacah genap bernilai dua kali lipat dari peluang diperolehnya nilai $Y$ bilangan ganjil, maka nilai dari $P(Y \ge 2) - P(Y < 2)$ adalah ....

- A. $\frac{1}{3}$  
  <sub>Salah: Siswa keliru menyelesaikan relasi $3a = 2(a+2b)$ menjadi $a = 2b$, sehingga memperoleh parameter yang salah.</sub>
- B. $\frac{5}{9}$  
  <sub>Salah: Siswa salah menghitung selisih dan justru menghitung $1 - 2 P(Y < 2)$ dengan nilai $P(Y < 2) = \frac{2}{9}$ akibat salah aljabar.</sub>
- C. $\frac{7}{18}$  
  <sub>Salah: Siswa lupa mengikutsertakan $P(Y = 3)$ pada perhitungan interval $P(Y \ge 2)$ sehingga didapat $P(Y=2) - P(Y < 2) = \frac{8}{18} - \frac{5}{18} = \frac{3}{18}$, lalu salah menjumlahkannya.</sub>
- **D. $\frac{4}{9}$** ✅  
  <sub>Benar: Syarat total peluang: $a + b + 2a + (a + b) = 1 \implies 4a + 2b = 1$. Peluang $Y$ genap adalah $P(Y=0) + P(Y=2) = 3a$. Peluang $Y$ ganjil adalah $P(Y=1) + P(Y=3) = a + 2b$. Diketahui $3a = 2(a + 2b) \implies a = 4b$. Substitusi ke persamaan total menghasilkan $4(4b) + 2b = 1 \implies 18b = 1 \implies b = \frac{1}{18}$ dan $a = \frac{4}{18}$. Dihitung $P(Y \ge 2) = 2a + (a + b) = 3a + b = 3\left(\frac{4}{18}\right) + \frac{1}{18} = \frac{13}{18}$, serta $P(Y < 2) = a + b = \frac{4}{18} + \frac{1}{18} = \frac{5}{18}$. Selisihnya adalah $\frac{13}{18} - \frac{5}{18} = \frac{8}{18} = \frac{4}{9}$.</sub>

**Pembahasan:** Langkah 1: Terapkan sifat fungsi peluang $\sum_{y=0}^3 P(Y = y) = 1$:
$$a + b + 2a + (a + b) = 1 \implies 4a + 2b = 1 \quad \dots (1)$$

Langkah 2: Tentukan relasi peluang genap dan ganjil:
- $Y$ genap: $\{0, 2\} \implies P(Y \text{ genap}) = P(Y = 0) + P(Y = 2) = a + 2a = 3a$
- $Y$ ganjil: $\{1, 3\} \implies P(Y \text{ ganjil}) = P(Y = 1) + P(Y = 3) = b + (a + b) = a + 2b$

Dari $P(Y \text{ genap}) = 2 P(Y \text{ ganjil})$:
$$3a = 2(a + 2b) \implies 3a = 2a + 4b \implies a = 4b \quad \dots (2)$$

Langkah 3: Substitusi persamaan (2) ke (1):
$$4(4b) + 2b = 1 \implies 18b = 1 \implies b = \frac{1}{18}$$
$$a = 4\left(\frac{1}{18}\right) = \frac{4}{18}$$

Langkah 4: Hitung peluang komposit yang ditanyakan:
$$P(Y \ge 2) = P(Y = 2) + P(Y = 3) = 2a + (a + b) = 3a + b = 3\left(\frac{4}{18}\right) + \frac{1}{18} = \frac{13}{18}$$
$$P(Y < 2) = P(Y = 0) + P(Y = 1) = a + b = \frac{4}{18} + \frac{1}{18} = \frac{5}{18}$$

Langkah 5: Hitung selisihnya:
$$P(Y \ge 2) - P(Y < 2) = \frac{13}{18} - \frac{5}{18} = \frac{8}{18} = \frac{4}{9}$$
**Acuan:** siswa — siswa hal.258

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
