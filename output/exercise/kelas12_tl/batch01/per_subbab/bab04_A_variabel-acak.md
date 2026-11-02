# Lembar koreksi — kelas12_tl SMA12L-B4 subbab A: Variabel Acak

57 soal | easy 20, medium 20, hard 17 | variasi 28, orisinal 29
> **Kapasitas kurang (hard): 17 dari kuota 20** — 9 soal dibuang karena tidak cocok dengan solver independen setelah 2 perbaikan otomatis

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas12_tl-b04-a-easy-bt01-001
*variasi (konteks) | C2 | 1 langkah | jenis: menentukan nilai variabel acak*

Sebuah kuis memuat 4 butir pertanyaan tipe Benar/Salah. Seorang peserta menjawab semua pertanyaan secara acak tanpa membaca soal. Jika variabel acak $W$ menyatakan banyaknya jawaban yang benar dari peserta tersebut, himpunan semua nilai $w$ yang mungkin dari variabel acak $W$ adalah ....

- A. $\{1, 2, 3, 4\}$  
  <sub>Salah: Mengabaikan kemungkinan peserta salah menjawab semua soal (nilai 0).</sub>
- B. $\{0, 1, 2, 3\}$  
  <sub>Salah: Mengabaikan kemungkinan peserta berhasil menjawab benar seluruh pertanyaan (nilai 4).</sub>
- **C. $\{0, 1, 2, 3, 4\}$** ✅  
  <sub>Benar: Peserta dapat menjawab benar sebanyak 0, 1, 2, 3, atau 4 soal dari total 4 butir pertanyaan.</sub>
- D. $\{0, 4\}$  
  <sub>Salah: Mengira hasil hanya berupa kejadian serba salah atau serba benar.</sub>

**Pembahasan:** Terdapat 4 butir pertanyaan. Setiap pertanyaan dapat dijawab benar atau salah. Variabel acak $W$ menyatakan banyaknya jawaban yang benar. Nilai $w$ yang mungkin mencakup tidak ada yang benar ($w = 0$), hingga seluruhnya benar ($w = 4$). Jadi, himpunan nilai yang mungkin adalah $\{0, 1, 2, 3, 4\}$.
**Acuan:** siswa — siswa hal.244 Contoh Soal 4.2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas12_tl-b04-a-easy-bt01-002
*orisinal | C1 | 1 langkah | jenis: identifikasi konsep variabel acak*

Di antara variabel-variabel berikut, manakah yang merupakan contoh variabel acak?

- A. Banyaknya sisi pada sebuah dadu standar bersisi enam  
  <sub>Salah: Merupakan besaran konstan bernilai 6, bukan hasil percobaan acak.</sub>
- B. Banyaknya huruf vokal dalam abjad bahasa Indonesia  
  <sub>Salah: Merupakan besaran tetap bernilai 5, tidak bergantung pada percobaan acak.</sub>
- C. Banyaknya hari dalam satu minggu kalender  
  <sub>Salah: Merupakan besaran tetap bernilai 7, bukan hasil percobaan acak.</sub>
- **D. Banyaknya sisi gambar yang muncul pada pelemparan 3 koin seimbang** ✅  
  <sub>Benar: Nilai kemunculan sisi gambar bergantung pada hasil percobaan acak.</sub>

**Pembahasan:** Variabel acak adalah variabel yang nilainya ditentukan melalui hasil suatu percobaan acak. Banyaknya sisi gambar yang muncul pada pelemparan 3 koin seimbang tidak dapat dipastikan sebelum pelemparan dilakukan, sehingga nilainya bergantung pada hasil eksperimen acak. Sementara itu, jumlah sisi dadu, jumlah hari dalam seminggu, dan jumlah huruf vokal adalah nilai pasti/konstan.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas12_tl-b04-a-easy-bt01-003
*orisinal | C2 | 1 langkah | jenis: evaluasi pemetaan variabel acak*

Dua buah dadu seimbang bersisi enam dilempar bersamaan sekali. Variabel acak $X$ didefinisikan bernilai 1 jika muncul pasangan mata dadu kembar, dan bernilai 0 jika muncul pasangan bukan kembar. Manakah pasangan hasil pelemparan berikut yang dipetakan ke nilai $X = 0$?

- **A. $(2, 5)$** ✅  
  <sub>Benar: Pasangan $(2, 5)$ memiliki mata dadu berbeda (bukan kembar), sehingga dipetakan ke nilai 0.</sub>
- B. $(5, 5)$  
  <sub>Salah: Merupakan pasangan mata dadu kembar sehingga dipetakan ke $X = 1$.</sub>
- C. $(3, 3)$  
  <sub>Salah: Merupakan pasangan mata dadu kembar sehingga dipetakan ke $X = 1$.</sub>
- D. $(1, 1)$  
  <sub>Salah: Merupakan pasangan mata dadu kembar sehingga dipetakan ke $X = 1$.</sub>

**Pembahasan:** Sesuai definisi, variabel acak $X$ bernilai 1 jika mata dadu kembar dan bernilai 0 jika bukan kembar. Pada pilihan $(2, 5)$, angka pada dadu pertama adalah 2 dan kedua adalah 5 (berbeda/bukan kembar), sehingga $(2, 5)$ dipetakan ke nilai $X = 0$.
**Acuan:** siswa — siswa hal.242

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas12_tl-b04-a-easy-bt01-004
*variasi (angka) | C2 | 1 langkah | jenis: menentukan nilai variabel acak koin*

Sekeping uang logam seimbang dilempar sebanyak 5 kali. Jika variabel acak $X$ menyatakan banyaknya sisi angka yang muncul, tentukan himpunan semua nilai $x$ yang mungkin dari variabel acak $X$.

- **A. $\{0, 1, 2, 3, 4, 5\}$** ✅  
  <sub>Benar: Banyaknya sisi angka pada 5 lemparan koin berkisar dari minimal 0 (semua gambar) hingga maksimal 5 (semua angka), sehingga nilainya adalah $\{0, 1, 2, 3, 4, 5\}$.</sub>
- B. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Siswa lupa menghitung kemungkinan seluruh lemparan menghasilkan sisi angka (5 angka).</sub>
- C. $\{1, 2, 3, 4, 5\}$  
  <sub>Salah: Siswa lupa memperhitungkan kemungkinan tidak ada angka yang muncul sama sekali (0 angka).</sub>
- D. $\{1, 5\}$  
  <sub>Salah: Siswa hanya menuliskan nilai ekstrem minimum kemunculan angka positif dan total lemparan.</sub>

**Pembahasan:** Dalam 5 kali pelemparan uang logam, sisi angka dapat muncul sebanyak 0 kali, 1 kali, 2 kali, 3 kali, 4 kali, atau 5 kali. Dengan demikian, himpunan nilai $x$ yang mungkin untuk variabel acak $X$ adalah $\{0, 1, 2, 3, 4, 5\}$.
**Acuan:** siswa — siswa hal.243 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas12_tl-b04-a-easy-bt01-005
*variasi (konteks) | C2 | 1 langkah | jenis: menentukan nilai variabel acak inspeksi*

Seorang petugas laboratorium memeriksa kondisi 4 tabung reaksi setelah proses sterilisasi. Setiap tabung dikategorikan dalam kondisi 'retak' atau 'utuh'. Jika variabel acak $K$ menyatakan banyaknya tabung reaksi yang retak, himpunan seluruh nilai $k$ yang mungkin dari variabel acak $K$ adalah ....

- A. $\{1, 2, 3, 4\}$  
  <sub>Salah: Siswa mengabaikan kemungkinan seluruh tabung reaksi utuh atau 0 retak.</sub>
- B. $\{0, 1, 2, 3\}$  
  <sub>Salah: Siswa lupa bahwa ada kemungkinan semua tabung (keempatnya) retak.</sub>
- C. $\{0, 4\}$  
  <sub>Salah: Siswa hanya menyebutkan nilai batas bawah dan batas atas tanpa nilai antara.</sub>
- **D. $\{0, 1, 2, 3, 4\}$** ✅  
  <sub>Benar: Banyaknya tabung retak dari total 4 tabung yang diperiksa dapat bernilai dari 0 hingga 4.</sub>

**Pembahasan:** Petugas mengamati 4 tabung reaksi. Banyaknya tabung yang retak ($K$) bisa jadi tidak ada sama sekali (0), ada 1, 2, 3, atau semuanya retak (4). Maka himpunan seluruh nilai $k$ yang mungkin adalah $\{0, 1, 2, 3, 4\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas12_tl-b04-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: menentukan nilai variabel acak pengambilan bola*

Sebuah kotak berisi 7 kelereng biru dan 8 kelereng kuning. Dari kotak tersebut diambil sebanyak 5 kelereng sekaligus secara acak. Jika variabel acak $M$ menyatakan banyaknya kelereng kuning yang terambil, tentukan himpunan semua nilai $m$ yang mungkin untuk variabel acak $M$.

- A. $\{1, 2, 3, 4, 5\}$  
  <sub>Salah: Siswa mengira minimal harus terambil 1 kelereng kuning, padahal bisa saja kelima kelereng yang terambil semuanya biru.</sub>
- **B. $\{0, 1, 2, 3, 4, 5\}$** ✅  
  <sub>Benar: Karena jumlah kelereng biru (7) $\ge 5$, maka kelereng kuning yang terambil bisa 0 buah. Jumlah kelereng kuning (8) $\ge 5$, sehingga kuning yang terambil bisa mencapai 5 buah.</sub>
- C. $\{5, 6, 7, 8\}$  
  <sub>Salah: Siswa keliru menggunakan jumlah kelereng yang tersisa di dalam kotak.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Siswa mengira maksimal kelereng kuning yang terambil hanya 4.</sub>

**Pembahasan:** Jumlah kelereng biru ada 7 dan kuning ada 8. Diambil 5 kelereng secara acak. Karena kelereng biru $\ge 5$, ada kemungkinan seluruh yang terambil kelereng biru (0 kelereng kuning). Karena kelereng kuning $\ge 5$, ada kemungkinan seluruh yang terambil kelereng kuning (5 kelereng kuning). Jadi nilai $m$ yang mungkin adalah $\{0, 1, 2, 3, 4, 5\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas12_tl-b04-a-easy-bt01-007
*orisinal | C1 | 1 langkah | jenis: definisi variabel acak*

Fungsi yang memetakan setiap hasil dari suatu percobaan acak ke bilangan real disebut ....

- A. variabel tidak acak  
  <sub>Salah: Variabel tidak acak nilainya tidak bergantung pada hasil percobaan acak.</sub>
- B. titik sampel  
  <sub>Salah: Titik sampel adalah anggota atau elemen dari ruang sampel, bukan fungsi.</sub>
- **C. variabel acak** ✅  
  <sub>Benar: Definisi langsung dari Buku Siswa: fungsi yang memetakan setiap hasil percobaan acak ke bilangan real disebut variabel acak.</sub>
- D. ruang sampel  
  <sub>Salah: Ruang sampel adalah himpunan semua hasil yang mungkin dari percobaan acak, bukan fungsi pemetaannya.</sub>

**Pembahasan:** Berdasarkan Definisi pada materi bab ini, variabel acak merupakan fungsi yang mengaitkan atau memetakan setiap hasil dari suatu ruang sampel percobaan acak ke bilangan real.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas12_tl-b04-a-easy-bt01-008
*orisinal | C1 | 1 langkah | jenis: notasi variabel acak*

Dalam penulisan matematika standar pada teori peluang, konvensi notasi yang benar untuk menyatakan suatu variabel acak dan nilai-nilai yang mungkin dimilikinya adalah ....

- A. baik variabel acak maupun nilai-nilainya selalu dinyatakan dengan huruf kapital  
  <sub>Salah: Siswa mengabaikan perbedaan notasi antara fungsi acak dan nilai real hasil pemetaannya.</sub>
- **B. variabel acak dinyatakan dengan huruf kapital, sedangkan nilainya dinyatakan dengan huruf kecil** ✅  
  <sub>Benar: Variabel acak disimbolkan dengan huruf kapital ($X, Y, Z$) dan nilai-nilainya disimbolkan dengan huruf kecil ($x, y, z$).</sub>
- C. variabel acak dinyatakan dengan huruf kecil, sedangkan nilainya dinyatakan dengan huruf kapital  
  <sub>Salah: Siswa tertukar antara konvensi penamaan variabel acak dan nilainya.</sub>
- D. baik variabel acak maupun nilai-nilainya selalu dinyatakan dengan huruf Yunani  
  <sub>Salah: Siswa mengira simbol variabel acak mengikuti parameter populasi seperti $\mu$ atau $\sigma$.</sub>

**Pembahasan:** Sesuai konvensi notasi pada buku teks, variabel acak dilambangkan dengan huruf kapital (seperti $X, Y, Z$), sedangkan nilai-nilai yang dapat diasumsikan oleh variabel acak tersebut dinyatakan dengan huruf kecil yang bersesuaian (seperti $x, y, z$).
**Acuan:** siswa — siswa hal.242

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas12_tl-b04-a-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: menentukan nilai variabel acak pengujian*

Seorang teknisi listrik menguji 2 buah lampu bohlam secara berurutan. Hasil uji tiap bohlam dikategorikan sebagai 'nyala' atau 'mati'. Jika $Y$ adalah variabel acak yang menyatakan banyak bohlam yang mati, nilai $y$ yang mungkin dari variabel acak $Y$ adalah ....

- A. $\{1, 2\}$  
  <sub>Salah: Mengabaikan kondisi di mana kedua lampu menyala sehingga banyak lampu mati adalah 0.</sub>
- B. $\{0, 1, 2, 3\}$  
  <sub>Salah: Menyalin pola jumlah kemungkinan dari pemeriksaan 3 unit pada soal acuan.</sub>
- C. $\{0, 1\}$  
  <sub>Salah: Hanya menghitung nilai biner untuk satu pengujian bohlam.</sub>
- **D. $\{0, 1, 2\}$** ✅  
  <sub>Benar: Jumlah bohlam mati dari 2 pengujian dapat berupa 0, 1, atau 2.</sub>

**Pembahasan:** Ruang sampel hasil pengujian 2 bohlam adalah $\{NN, NM, MN, MM\}$, dengan $N$ menyatakan bohlam nyala dan $M$ menyatakan bohlam mati. Variabel acak $Y$ menyatakan banyaknya bohlam mati. Pada luaran $NN$, $y = 0$. Pada luaran $NM$ dan $MN$, $y = 1$. Pada luaran $MM$, $y = 2$. Dengan demikian, nilai $y$ yang mungkin adalah $\{0, 1, 2\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas12_tl-b04-a-easy-bt01-010
*orisinal | C1 | 1 langkah | jenis: klasifikasi variabel acak dan tidak acak*

Di antara variabel-variabel berikut, manakah yang merupakan variabel tidak acak?

- **A. Bilangan kelipatan 5 yang bernilai kurang dari 25** ✅  
  <sub>Benar: Nilai-nilainya pasti dan tidak bergantung pada hasil percobaan acak.</sub>
- B. Jumlah mata dadu yang muncul pada pelemparan dua dadu seimbang  
  <sub>Salah: Besaran ini bergantung pada hasil pelemparan acak dua dadu sehingga merupakan variabel acak.</sub>
- C. Banyaknya bola merah yang terambil dalam pengambilan 3 bola secara acak  
  <sub>Salah: Hasil pengambilan dilakukan secara acak sehingga termasuk variabel acak.</sub>
- D. Banyaknya kemunculan sisi angka pada pelemparan 4 koin seimbang  
  <sub>Salah: Besaran ini merupakan variabel acak karena nilainya diperoleh melalui percobaan acak.</sub>

**Pembahasan:** Berdasarkan definisi, variabel yang nilainya tidak bergantung pada hasil percobaan acak disebut variabel tidak acak. 'Bilangan kelipatan 5 yang bernilai kurang dari 25' memiliki nilai pasti (yaitu 5, 10, 15, 20) dan nilainya tidak ditentukan oleh suatu percobaan acak, sehingga merupakan variabel tidak acak. Tiga pilihan lainnya merupakan hasil percobaan acak, sehingga merupakan variabel acak.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas12_tl-b04-a-easy-bt01-011
*orisinal | C2 | 1 langkah | jenis: evaluasi pemetaan variabel acak*

Dua buah dadu seimbang dilemparkan bersama-sama sekali. Variabel acak $W$ didefinisikan sebagai selisih positif antara mata dadu pertama dan mata dadu kedua. Jika hasil lemparan yang muncul adalah pasangan $(2, 6)$, nilai fungsi variabel acak $W(2, 6)$ adalah ....

- A. 12  
  <sub>Salah: Mengalikan kedua mata dadu ($2 \times 6$) alih-alih menghitung selisih.</sub>
- **B. 4** ✅  
  <sub>Benar: Selisih positif antara 2 dan 6 adalah $|2 - 6| = 4$.</sub>
- C. $-4$  
  <sub>Salah: Mengurangkan langsung $2 - 6$ tanpa memperhatikan bahwa selisih bernilai positif (selisih mutlak).</sub>
- D. 8  
  <sub>Salah: Menjumlahkan kedua mata dadu ($2 + 6$) alih-alih mencari selisihnya.</sub>

**Pembahasan:** Variabel acak $W$ memetakan setiap anggota ruang sampel ke bilangan real berupa selisih positif antara kedua mata dadu. Untuk pasangan $(2, 6)$, selisih positifnya adalah $|2 - 6| = |6 - 2| = 4$. Jadi, $W(2, 6) = 4$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas12_tl-b04-a-easy-bt01-012
*variasi (angka) | C2 | 2 langkah | jenis: nilai variabel acak sampel terbatas*

Dari 7 unit genset di sebuah gudang, terdapat 3 unit yang mengalami kerusakan kabel. Sebuah proyek konstruksi menyewa 4 unit genset secara acak. Variabel acak $X$ menyatakan banyaknya genset dengan kerusakan kabel yang disewa oleh proyek tersebut. Himpunan semua nilai $x$ yang mungkin dari variabel acak $X$ adalah ....

- A. $\{1, 2, 3\}$  
  <sub>Salah: Menganggap minimal 1 genset rusak harus ikut tersewa, padahal ada 4 genset baik yang mencukupi untuk sewa 4 unit tanpa genset rusak sama sekali.</sub>
- B. $\{1, 2, 3, 4\}$  
  <sub>Salah: Mengabaikan kemungkinan tidak ada genset rusak (nilai 0) dan keliru menetapkan batas atas sebanyak unit yang disewa.</sub>
- **C. $\{0, 1, 2, 3\}$** ✅  
  <sub>Benar: Genset baik berjumlah $7 - 3 = 4$ unit. Karena disewa 4 unit, proyek dapat memperoleh 0 genset rusak jika semua yang disewa dalam kondisi baik. Maksimal genset rusak yang dapat terambil adalah seluruh genset rusak yang ada, yaitu 3 unit. Jadi nilai $x$ yang mungkin adalah 0, 1, 2, atau 3.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Mengira nilai maksimum mengikuti jumlah unit yang disewa (4 unit), padahal genset rusak yang tersedia hanya ada 3 unit.</sub>

**Pembahasan:** Diketahui total genset ada 7 unit, dengan 3 unit rusak dan $7 - 3 = 4$ unit baik.
Disewa sebanyak 4 unit genset secara acak.
- Nilai minimum $X$: Karena tersedia 4 unit genset baik, seluruh genset yang disewa bisa semuanya baik, sehingga nilai minimum $X = 0$.
- Nilai maksimum $X$: Karena genset rusak hanya tersedia 3 unit, maka paling banyak genset rusak yang terambil adalah 3 unit, sehingga nilai maksimum $X = 3$.
Dengan demikian, himpunan nilai $x$ yang mungkin adalah $\{0, 1, 2, 3\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas12_tl-b04-a-easy-bt01-013
*variasi (konteks) | C2 | 1 langkah | jenis: nilai variabel acak percobaan berkecambah*

Seorang petani menanam 4 butir benih jagung unggul pada petak lahan percobaan. Jika variabel acak $Y$ menyatakan banyaknya benih jagung yang berhasil berkecambah, tentukan himpunan semua nilai $y$ yang mungkin dari variabel acak $Y$.

- A. $\{0, 1, 2, 3\}$  
  <sub>Salah: Lupa memperhitungkan kemungkinan seluruh benih berhasil berkecambah (nilai 4).</sub>
- B. $\{1, 2, 3\}$  
  <sub>Salah: Mengabaikan kedua kondisi ekstrem, yaitu ketika tidak ada benih yang berkecambah dan ketika semua benih berkecambah.</sub>
- C. $\{1, 2, 3, 4\}$  
  <sub>Salah: Lupa memperhitungkan kemungkinan semua benih gagal berkecambah (nilai 0).</sub>
- **D. $\{0, 1, 2, 3, 4\}$** ✅  
  <sub>Benar: Setiap benih dapat berkecambah atau gagal. Dari 4 benih, jumlah benih yang berkecambah bisa 0, 1, 2, 3, atau 4 benih.</sub>

**Pembahasan:** Setiap benih dari 4 butir benih memiliki dua kemungkinan: berkecambah atau tidak berkecambah.
Variabel acak $Y$ menyatakan banyaknya benih yang berkecambah:
- Jika tidak ada satu pun benih yang berkecambah, maka $y = 0$.
- Jika ada 1, 2, 3, atau seluruh 4 benih berkecambah, berturut-turut nilai $y = 1, 2, 3, 4$.
Jadi, himpunan semua nilai $y$ yang mungkin adalah $\{0, 1, 2, 3, 4\}$.
**Acuan:** siswa — siswa hal.244 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas12_tl-b04-a-easy-bt01-014
*variasi (konteks) | C2 | 2 langkah | jenis: nilai variabel acak pengambilan kartu*

Sebuah kartu diambil secara acak dari sebuah kotak yang berisi sepuluh kartu bernomor 1 sampai 10, dicatat hasilnya, lalu dikembalikan ke dalam kotak. Percobaan pengambilan ini dilakukan sebanyak 2 kali. Jika $W$ adalah variabel acak yang menyatakan banyaknya terambil kartu bernomor prima, himpunan semua nilai $w$ yang mungkin dari variabel acak $W$ adalah ....

- A. $\{1, 2\}$  
  <sub>Salah: Lupa bahwa kedua kartu yang terambil bisa saja keduanya bukan bilangan prima sehingga nilai 0 mungkin terjadi.</sub>
- B. $\{2, 3, 5, 7\}$  
  <sub>Salah: Mendaftar bilangan prima yang ada pada rentang 1 sampai 10, bukan menyatakan banyaknya kemunculan kartu prima.</sub>
- **C. $\{0, 1, 2\}$** ✅  
  <sub>Benar: Pengambilan dilakukan 2 kali. Pada setiap pengambilan, kartu yang terambil bisa prima atau bukan prima. Banyaknya kartu prima yang terambil dari 2 kali percobaan bisa bernilai 0, 1, atau 2.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Menyertakan jumlah total bilangan prima yang tersedia di dalam kotak, bukan batas pengulangan percobaan yang hanya 2 kali.</sub>

**Pembahasan:** Percobaan dilakukan sebanyak 2 kali.
Pada setiap kali pengambilan, kejadian terambil kartu prima dikategorikan sebagai sukses, dan bukan prima sebagai gagal.
Banyaknya kemunculan kartu prima dalam 2 kali pengambilan dapat berupa:
- Tidak ada kartu prima yang terambil sama sekali ($w = 0$)
- Tepat satu kartu prima yang terambil ($w = 1$)
- Kedua kartu yang terambil adalah prima ($w = 2$)
Jadi, himpunan nilai $w$ yang mungkin adalah $\{0, 1, 2\}$.
**Acuan:** siswa — siswa hal.243 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas12_tl-b04-a-easy-bt01-015
*variasi (angka) | C2 | 2 langkah | jenis: nilai variabel acak batas minimum*

Sebuah kotak berisi 2 bola merah dan 8 bola putih. Diambil sebanyak 5 bola satu per satu tanpa pengembalian. Jika $Z$ menyatakan banyaknya bola putih yang terambil, tentukan himpunan semua nilai $z$ yang mungkin dari variabel acak $Z$.

- A. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Mengasumsikan bola putih bisa bernilai 0, 1, atau 2, padahal bola merah hanya ada 2 butir sehingga bola putih minimal yang terambil adalah 3 butir.</sub>
- **B. $\{3, 4, 5\}$** ✅  
  <sub>Benar: Bola merah hanya ada 2 butir, sehingga dari 5 bola yang diambil, paling banyak terambil 2 bola merah. Akibatnya, paling sedikit harus terambil 5 - 2 = 3 bola putih. Karena bola putih ada 8 butir, paling banyak terambil 5 bola putih. Nilai z yang mungkin adalah {3, 4, 5}.</sub>
- C. $\{3, 4, 5, 6, 7, 8\}$  
  <sub>Salah: Mendaftar sampai batas total bola putih di dalam kotak (8 butir), padahal bola yang diambil hanya 5 butir.</sub>
- D. $\{2, 3, 4, 5\}$  
  <sub>Salah: Salah menghitung selisih minimum; mengira bola putih minimal sama dengan jumlah bola merah yang ada.</sub>

**Pembahasan:** Total bola diambil = 5 butir.
Jumlah bola merah = 2 butir, jumlah bola putih = 8 butir.
- Nilai minimum $Z$: Jika semua bola merah terambil (2 butir), sisa bola yang harus terambil adalah bola putih sebanyak $5 - 2 = 3$ butir. Jadi, nilai minimum $z = 3$.
- Nilai maksimum $Z$: Karena bola putih yang tersedia (8 butir) lebih banyak daripada jumlah bola yang diambil (5 butir), kelima bola tersebut dapat seluruhnya berwarna putih. Jadi, nilai maksimum $z = 5$.
Dengan demikian, himpunan nilai $z$ yang mungkin adalah $\{3, 4, 5\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas12_tl-b04-a-easy-bt01-016
*orisinal | C1 | 1 langkah | jenis: terminologi dasar peluang*

Himpunan dari semua hasil yang mungkin terjadi dalam suatu percobaan acak disebut ....

- **A. ruang sampel** ✅  
  <sub>Benar: Berdasarkan definisi pada buku teks, ruang sampel adalah himpunan dari semua hasil yang mungkin terjadi dalam suatu percobaan acak.</sub>
- B. variabel acak  
  <sub>Salah: Variabel acak adalah fungsi yang memetakan hasil percobaan acak ke bilangan real, bukan himpunan dari semua hasil percobaan itu sendiri.</sub>
- C. peluang kejadian  
  <sub>Salah: Peluang kejadian merupakan nilai kemungkinan terjadinya suatu peristiwa tertentu, bukan himpunan seluruh hasil.</sub>
- D. titik sampel  
  <sub>Salah: Titik sampel merupakan setiap elemen tunggal di dalam ruang sampel, bukan himpunan keseluruhan hasil.</sub>

**Pembahasan:** Dalam teori peluang, himpunan dari seluruh kemungkinan hasil yang dapat terjadi dari suatu percobaan acak didefinisikan sebagai ruang sampel (biasanya dilambangkan dengan huruf $S$).
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas12_tl-b04-a-easy-bt01-017
*variasi (konteks) | C2 | 1 langkah | jenis: identifikasi variabel tidak tunggal*

Variabel merupakan suatu besaran yang memiliki nilai tidak tunggal. Di antara pernyataan berikut, manakah besaran yang BUKAN merupakan variabel (bernilai tunggal)?

- **A. Banyaknya hari dalam bulan Februari pada tahun kabisat** ✅  
  <sub>Benar: Tahun kabisat secara definitif dan tetap memiliki tepat 29 hari di bulan Februari, sehingga nilainya tunggal (konstan) dan bukan merupakan variabel.</sub>
- B. Suhu udara maksimum harian di sebuah kota  
  <sub>Salah: Besaran ini memiliki nilai bervariasi setiap harinya sehingga merupakan variabel.</sub>
- C. Waktu tempuh seorang siswa dari rumah ke sekolah setiap pagi  
  <sub>Salah: Waktu tempuh bergantung pada kondisi lalu lintas sehingga nilainya tidak tunggal.</sub>
- D. Banyaknya kendaraan yang melintas di jalan protokol setiap jam  
  <sub>Salah: Besaran ini bernilai tidak tunggal karena jumlah kendaraan berfluktuasi tiap jam.</sub>

**Pembahasan:** Variabel didefinisikan sebagai besaran yang memiliki nilai tidak tunggal. Banyaknya hari pada bulan Februari di tahun kabisat selalu tetap bernilai 29 hari (nilai tunggal), sehingga besaran tersebut bukan merupakan variabel melainkan konstanta.
**Acuan:** siswa — siswa hal.240 Ayo Berdiskusi

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas12_tl-b04-a-easy-bt01-018
*variasi (konteks) | C2 | 2 langkah | jenis: peluang kejadian percobaan dadu*

Dua buah dadu seimbang bersisi enam dilempar bersama-sama sekali. Berapakah peluang munculnya pasangan mata dadu yang berjumlah 11?

- A. $\frac{1}{36}$  
  <sub>Salah: Hanya menghitung salah satu urutan pasangan saja, yaitu (5, 6), dan melupakan (6, 5).</sub>
- **B. $\frac{1}{18}$** ✅  
  <sub>Benar: Pasangan mata dadu berjumlah 11 ada 2, yaitu (5, 6) dan (6, 5). Total ruang sampel dua dadu adalah 36, sehingga peluangnya $\frac{2}{36} = \frac{1}{18}$.</sub>
- C. $\frac{1}{9}$  
  <sub>Salah: Salah melakukan penyederhanaan pecahan dari 2/36 menjadi 1/9 atau mengira ada 4 titik sampel.</sub>
- D. $\frac{1}{12}$  
  <sub>Salah: Keliru mengira ada 3 titik sampel yang berjumlah 11 sehingga menghitung 3/36 = 1/12.</sub>

**Pembahasan:** Banyaknya anggota ruang sampel pelemparan dua buah dadu seimbang adalah $n(S) = 6 \times 6 = 36$.
Kejadian munculnya mata dadu berjumlah 11 adalah $A = \{(5, 6), (6, 5)\}$, sehingga $n(A) = 2$.
Peluang kejadian $A$ adalah:
$$P(A) = \frac{n(A)}{n(S)} = \frac{2}{36} = \frac{1}{18}$$
**Acuan:** siswa — siswa hal.241 Ayo Bereksplorasi 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas12_tl-b04-a-easy-bt01-019
*orisinal | C1 | 1 langkah | jenis: menentukan ukuran ruang sampel*

Tiga keping uang logam seimbang dilempar bersamaan sekali. Banyaknya anggota ruang sampel $n(S)$ dari percobaan acak tersebut adalah ....

- A. $3$  
  <sub>Salah: Hanya menyebutkan banyaknya uang logam yang dilempar.</sub>
- B. $6$  
  <sub>Salah: Mengalikan jumlah sisi dengan jumlah koin secara keliru ($2 \times 3 = 6$), bukan aturan perkalian pemangkatan.</sub>
- C. $9$  
  <sub>Salah: Terbalik menerapkan rumus pemangkatan menjadi $3^2 = 9$ bukannya $2^3$.</sub>
- **D. $8$** ✅  
  <sub>Benar: Setiap keping uang logam memiliki 2 kemungkinan hasil (Angka atau Gambar), sehingga untuk 3 keping banyaknya anggota ruang sampel adalah $2^3 = 8$.</sub>

**Pembahasan:** Ruang sampel adalah himpunan semua hasil yang mungkin dari suatu percobaan acak.
Pada pelemparan satu keping uang logam terdapat 2 hasil mungkin: Angka (A) atau Gambar (G).
Untuk pelemparan tiga keping uang logam seimbang sekaligus, banyaknya anggota ruang sampel adalah:
$$n(S) = 2 \times 2 \times 2 = 2^3 = 8$$
Anggota ruang sampelnya adalah $\{AAA, AAG, AGA, AGG, GAA, GAG, GGA, GGG\}$.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas12_tl-b04-a-easy-bt01-020
*variasi (konteks) | C2 | 2 langkah | jenis: nilai variabel acak seleksi objek*

Dari 10 buah semangka di sebuah kios buah, sebanyak 4 buah merupakan semangka tanpa biji dan sisanya berbiji. Seorang pelanggan membeli 3 buah semangka yang dipilih secara acak. Jika variabel acak $X$ menyatakan banyaknya semangka tanpa biji yang dibeli oleh pelanggan tersebut, tentukan himpunan semua nilai $x$ yang mungkin untuk variabel acak $X$.

- A. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Siswa memasukkan angka 4 karena terdapat 4 semangka tanpa biji di kios, padahal buah yang dibeli hanya 3.</sub>
- B. $\{0, 1, 2\}$  
  <sub>Salah: Siswa langsung meniru nilai variabel acak pada contoh acuan tanpa menyesuaikan dengan banyak semangka yang dibeli.</sub>
- **C. $\{0, 1, 2, 3\}$** ✅  
  <sub>Benar: Banyak semangka berbiji ada $10 - 4 = 6$ buah. Karena semangka berbiji $\ge 3$, mungkin terambil 0 semangka tanpa biji. Karena semangka tanpa biji ada 4 buah ($\ge 3$), pembeli dapat memperoleh hingga 3 semangka tanpa biji. Jadi nilai $x$ yang mungkin adalah 0, 1, 2, atau 3.</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Siswa mengira pembeli harus mendapatkan setidaknya 1 semangka tanpa biji (mengabaikan kemungkinan nilai 0).</sub>

**Pembahasan:** Diketahui:
- Total semangka = 10 buah
- Semangka tanpa biji = 4 buah
- Semangka berbiji = $10 - 4 = 6$ buah
- Banyak semangka yang dibeli = 3 buah

Variabel acak $X$ menyatakan banyak semangka tanpa biji yang dibeli:
1. Nilai terkecil: Jika ketiga semangka yang dibeli semuanya berbiji (tersedia 6 buah, cukup untuk diambil 3), maka banyaknya semangka tanpa biji adalah $X = 0$.
2. Nilai terbesar: Karena semangka tanpa biji tersedia 4 buah (cukup untuk diambil 3), maka ketiga semangka yang dibeli bisa semuanya tanpa biji, sehingga $X = 3$.

Dengan demikian, nilai-nilai $x$ yang mungkin untuk variabel acak $X$ adalah $0, 1, 2, 3$, atau dalam bentuk himpunan $\{0, 1, 2, 3\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas12_tl-b04-a-medium-bt01-001
*variasi (angka) | C3 | 2 langkah | jenis: himpunan nilai variabel acak pengambilan*

Sebuah kantong berisi 3 bola merah dan 7 bola putih. Dari kantong tersebut diambil 5 bola sekaligus secara acak tanpa pengembalian. Jika variabel acak $Z$ menyatakan banyaknya bola merah yang terambil, himpunan semua nilai $z$ yang mungkin untuk variabel acak $Z$ adalah ....

- A. $\{0, 1, 2\}$  
  <sub>Salah: Salah menghitung batas maksimum bola merah yang terambil kurang satu.</sub>
- **B. $\{0, 1, 2, 3\}$** ✅  
  <sub>Benar: Total bola merah hanya ada 3 dan bola putih ada 7, sehingga pada pengambilan 5 bola, banyaknya bola merah yang terambil paling sedikit 0 (semua 5 putih) dan paling banyak 3 (semua merah terambil), menghasilkan nilai {0, 1, 2, 3}.</sub>
- C. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Mengabaikan batas ketersediaan bola merah yang hanya berjumlah 3 dan menganggap nilai bisa mencapai jumlah pengambilan (5).</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Mengira bola merah pasti terambil minimal 1 butir padahal bola putih cukup untuk diambil kelimanya.</sub>

**Pembahasan:** Diketahui:
- Jumlah bola merah = 3
- Jumlah bola putih = 7
- Banyak bola yang diambil = 5

Karena jumlah bola putih (7) lebih banyak dari jumlah bola yang diambil (5), kasus terambil 0 bola merah mungkin terjadi (yaitu jika kelima bola yang terambil semuanya putih).
Batas maksimum bola merah yang dapat terambil dibatasi oleh total bola merah yang tersedia, yaitu 3 butir.

Dengan demikian, kemungkinan banyak bola merah yang terambil adalah 0, 1, 2, atau 3.
Jadi, himpunan semua nilai $z$ yang mungkin adalah $\{0, 1, 2, 3\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas12_tl-b04-a-medium-bt01-002
*variasi (konteks) | C3 | 3 langkah | jenis: variabel acak selisih kelahiran*

Sebuah keluarga merencanakan memiliki 3 orang anak. Asumsikan peluang kelahiran anak laki-laki dan perempuan sama pada setiap kelahiran. Jika variabel acak $W$ menyatakan selisih mutlak antara banyaknya anak laki-laki dan banyaknya anak perempuan, tentukan himpunan semua nilai $w$ yang mungkin dari variabel acak $W$.

- A. $\{0, 1, 2\}$  
  <sub>Salah: Menyalin pola nilai acuan dan mengasumsikan nilai mulai dari 0 sampai n-1.</sub>
- B. $\{0, 1, 2, 3\}$  
  <sub>Salah: Mengira selisih dapat bernilai genap termasuk 0 padahal total 3 anak ganjil sehingga selisih selalu ganjil.</sub>
- **C. $\{1, 3\}$** ✅  
  <sub>Benar: Kombinasi banyak anak (L, P) yang mungkin dari 3 anak adalah (3, 0), (2, 1), (1, 2), dan (0, 3) dengan selisih mutlak berturut-turut |3 - 0| = 3 dan |2 - 1| = 1.</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Memasukkan nilai selisih 2 yang secara kombinasi mustahil terbentuk dari total 3 anak.</sub>

**Pembahasan:** Ruang sampel untuk jenis kelamin dari 3 kelahiran berurutan:
$S = \{LLL, LLP, LPL, LPP, PLL, PLP, PPL, PPP\}$

Banyak kemungkinan susunan (laki-laki, perempuan):
1. 3 laki-laki dan 0 perempuan: selisih mutlak $|3 - 0| = 3$
2. 2 laki-laki dan 1 perempuan: selisih mutlak $|2 - 1| = 1$
3. 1 laki-laki dan 2 perempuan: selisih mutlak $|1 - 2| = 1$
4. 0 laki-laki dan 3 perempuan: selisih mutlak $|0 - 3| = 3$

Nilai-nilai unik selisih mutlak yang diperoleh adalah 1 dan 3.
Jadi, himpunan semua nilai $w$ yang mungkin dari variabel acak $W$ adalah $\{1, 3\}$.
**Acuan:** siswa — siswa hal.244 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas12_tl-b04-a-medium-bt01-003
*orisinal | C3 | 2 langkah | jenis: banyak anggota prapeta variabel acak*

Dua buah dadu seimbang bersisi enam dilemparkan bersamaan satu kali. Jika variabel acak $X$ menyatakan hasil kali kedua mata dadu yang muncul, banyaknya elemen dalam ruang sampel yang memetakan nilai $X = 12$ adalah ....

- A. 6  
  <sub>Salah: Menyertakan pasangan pembagi 12 yang tidak terdapat pada mata dadu seperti (1, 12) dan (12, 1).</sub>
- B. 3  
  <sub>Salah: Lupa menghitung salah satu pasangan kebalikan seperti (4, 3).</sub>
- C. 2  
  <sub>Salah: Hanya menghitung pasangan tak berurutan {2, 6} dan {3, 4} tanpa memperhatikan urutan dadu.</sub>
- **D. 4** ✅  
  <sub>Benar: Pasangan mata dadu (dadu 1, dadu 2) yang hasil kalinya 12 adalah (2, 6), (3, 4), (4, 3), dan (6, 2).</sub>

**Pembahasan:** Mata dadu yang mungkin pada setiap dadu adalah $\{1, 2, 3, 4, 5, 6\}$.
Variabel acak $X(a, b) = a \times b = 12$.

Pasangan $(a, b)$ yang memenuhi:
1. $(2, 6) \rightarrow 2 \times 6 = 12$
2. $(3, 4) \rightarrow 3 \times 4 = 12$
3. $(4, 3) \rightarrow 4 \times 3 = 12$
4. $(6, 2) \rightarrow 6 \times 2 = 12$

Pasangan $(1, 12)$ tidak mungkin karena angka dadu maksimal 6.
Jadi, banyaknya elemen dalam ruang sampel yang menghasilkan nilai $X = 12$ adalah 4.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas12_tl-b04-a-medium-bt01-004
*orisinal | C4 | 3 langkah | jenis: himpunan nilai variabel acak bersyarat*

Dua buah dadu seimbang bersisi enam dilemparkan secara bersamaan satu kali. Misalkan variabel acak $K$ didefinisikan sebagai jumlah kedua mata dadu HANYA jika jumlah tersebut merupakan bilangan prima, dan tidak terdefinisi untuk kondisi lainnya. Himpunan semua nilai yang mungkin dari variabel acak $K$ adalah ....

- A. $\{3, 5, 7, 11\}$  
  <sub>Salah: Mengira jumlah terkecil prima adalah 3, lupa bahwa pasangan (1, 1) berjumlah 2 yang juga merupakan bilangan prima.</sub>
- B. $\{1, 2, 3, 5, 7, 11\}$  
  <sub>Salah: Memasukkan 1 sebagai bilangan prima.</sub>
- **C. $\{2, 3, 5, 7, 11\}$** ✅  
  <sub>Benar: Jumlah dua mata dadu bernilai antara 2 hingga 12, dan bilangan prima dalam rentang tersebut adalah 2, 3, 5, 7, dan 11.</sub>
- D. $\{2, 3, 5, 7, 9, 11\}$  
  <sub>Salah: Memasukkan 9 sebagai bilangan prima padahal 9 bilangan komposit (dapat dibagi 3).</sub>

**Pembahasan:** Langkah 1: Menentukan batas nilai jumlah mata dadu dari dua dadu bersisi enam.
Nilai minimum: $1 + 1 = 2$
Nilai maksimum: $6 + 6 = 12$
Rentang kemungkinan jumlah: $\{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12\}$.

Langkah 2: Memilih bilangan prima dari rentang [2, 12].
Bilangan prima yang berada di antara 2 dan 12 adalah 2, 3, 5, 7, dan 11.

Langkah 3: Memastikan setiap nilai prima tersebut dapat terbentuk dari pelemparan dua dadu:
- 2 didapat dari $(1, 1)$
- 3 didapat dari $(1, 2), (2, 1)$
- 5 didapat dari $(1, 4), (2, 3), (3, 2), (4, 1)$
- 7 didapat dari $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)$
- 11 didapat dari $(5, 6), (6, 5)$

Jadi, himpunan semua nilai yang mungkin dari variabel acak $K$ adalah $\{2, 3, 5, 7, 11\}$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas12_tl-b04-a-medium-bt01-005
*orisinal | C3 | 3 langkah | jenis: penentuan nilai variabel acak kartu*

Dari sebuah kotak yang berisi 4 kartu bernomor 1, 2, 3, dan 4, diambil 2 kartu secara acak sekaligus. Jika variabel acak $X$ menyatakan jumlah kedua angka pada kartu yang terambil, tentukan himpunan semua nilai $x$ yang mungkin dari variabel acak $X$.

- **A. $\{3, 4, 5, 6, 7\}$** ✅  
  <sub>Benar: Kombinasi dua kartu yang terambil adalah {1,2}, {1,3}, {1,4}, {2,3}, {2,4}, dan {3,4} dengan jumlah berturut-turut 3, 4, 5, 5, 6, dan 7.</sub>
- B. $\{3, 4, 5, 6\}$  
  <sub>Salah: Lupa menghitung kemungkinan pasangan kartu bernomor tertinggi {3, 4} yang berjumlah 7.</sub>
- C. $\{2, 3, 4, 5, 6, 7, 8\}$  
  <sub>Salah: Memasukkan jumlah kartu kembar seperti (1, 1) dan (4, 4) padahal kartu diambil sekaligus tanpa pengembalian.</sub>
- D. $\{3, 5, 7\}$  
  <sub>Salah: Hanya menghitung jumlah yang bernilai ganjil dan melewatkan jumlah genap 4 dan 6.</sub>

**Pembahasan:** Pengambilan 2 kartu sekaligus dari 4 kartu yang berbeda $\{1, 2, 3, 4\}$ memiliki ruang sampel sebanyak $\binom{4}{2} = 6$ anggota:
1. Kartu $\{1, 2\} \rightarrow x = 1 + 2 = 3$
2. Kartu $\{1, 3\} \rightarrow x = 1 + 3 = 4$
3. Kartu $\{1, 4\} \rightarrow x = 1 + 4 = 5$
4. Kartu $\{2, 3\} \rightarrow x = 2 + 3 = 5$
5. Kartu $\{2, 4\} \rightarrow x = 2 + 4 = 6$
6. Kartu $\{3, 4\} \rightarrow x = 3 + 4 = 7$

Nilai unik yang dihasilkan untuk variabel acak $X$ adalah 3, 4, 5, 6, dan 7.
Jadi, himpunan nilai $x$ yang mungkin adalah $\{3, 4, 5, 6, 7\}$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas12_tl-b04-a-medium-bt01-006
*variasi (angka) | C3 | 2 langkah | jenis: himpunan nilai variabel acak hipergeometrik*

Dari 8 unit laptop yang dikirim ke gudang, terdapat 5 unit dalam kondisi rusak dan 3 unit dalam kondisi baik. Sebuah kantor membeli 4 unit laptop secara acak sekaligus dari gudang tersebut. Jika variabel acak $X$ menyatakan banyaknya laptop rusak yang diterima kantor, himpunan semua nilai $x$ yang mungkin adalah ....

- A. $\{0, 1, 2, 3\}$  
  <sub>Salah: Memakai himpunan nilai variabel acak dari jumlah laptop baik alih-alih laptop rusak.</sub>
- B. $\{1, 2, 3\}$  
  <sub>Salah: Mengira laptop rusak yang terambil paling banyak 3 mengikuti batas ketersediaan laptop baik.</sub>
- **C. $\{1, 2, 3, 4\}$** ✅  
  <sub>Benar: Karena laptop baik hanya 3 unit, dari 4 laptop yang diambil minimal harus ada 1 unit rusak ($4 - 3 = 1$). Maksimal laptop rusak yang terambil adalah 4 unit karena stok laptop rusak ada 5 unit. Jadi, nilai $x$ yang mungkin adalah 1, 2, 3, 4.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Mengabaikan batas ketersediaan laptop baik yang hanya berjumlah 3 unit sehingga menganggap 0 laptop rusak mungkin terjadi.</sub>

**Pembahasan:** Kondisi awal:
- Total laptop $= 8$
- Rusak $= 5$
- Baik $= 3$

Banyak laptop yang diambil $= 4$ unit.
- Nilai minimum laptop rusak yang terambil: jika semua laptop baik terambil (3 unit), sisanya harus rusak, yaitu $4 - 3 = 1$ unit.
- Nilai maksimum laptop rusak yang terambil: seluruh 4 unit yang diambil dapat berupa laptop rusak karena persediaan rusak ada 5 unit ($4 \le 5$).

Maka nilai variabel acak $X$ yang mungkin adalah $\{1, 2, 3, 4\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas12_tl-b04-a-medium-bt01-007
*variasi (konteks) | C3 | 2 langkah | jenis: himpunan nilai variabel acak selisih mutlak koin*

Sekeping uang logam seimbang dilempar sebanyak 4 kali berturut-turut. Jika variabel acak $W$ menyatakan selisih mutlak antara banyaknya sisi angka dan banyaknya sisi gambar yang muncul, himpunan semua nilai $w$ yang mungkin dari variabel acak $W$ adalah ....

- A. $\{-4, -2, 0, 2, 4\}$  
  <sub>Salah: Menghitung selisih bertanda tanpa menerapkan operasi nilai mutlak.</sub>
- **B. $\{0, 2, 4\}$** ✅  
  <sub>Benar: Kombinasi (angka, gambar) yang mungkin dari 4 lemparan adalah (4,0), (3,1), (2,2), (1,3), dan (0,4). Selisih mutlaknya masing-masing adalah $|4-0|=4$, $|3-1|=2$, $|2-2|=0$, $|1-3|=2$, dan $|0-4|=4$, sehingga menghasilkan himpunan nilai {0, 2, 4}.</sub>
- C. $\{2, 4\}$  
  <sub>Salah: Lupa memperhitungkan kejadian saat muncul 2 angka dan 2 gambar yang menghasilkan selisih 0.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Menganggap semua bilangan cacah dari 0 sampai 4 dapat muncul sebagai selisih, padahal selisih pada 4 lemparan selalu bilangan genap.</sub>

**Pembahasan:** Pelemparan koin 4 kali menghasilkan pasangan banyak sisi Angka ($A$) dan Gambar ($G$) dengan $A + G = 4$:
1. 4 Angka, 0 Gambar: $|4 - 0| = 4$
2. 3 Angka, 1 Gambar: $|3 - 1| = 2$
3. 2 Angka, 2 Gambar: $|2 - 2| = 0$
4. 1 Angka, 3 Gambar: $|1 - 3| = 2$
5. 0 Angka, 4 Gambar: $|0 - 4| = 4$

Himpunan semua nilai $w$ yang mungkin adalah $\{0, 2, 4\}$.
**Acuan:** siswa — siswa hal.243 Contoh Soal 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas12_tl-b04-a-medium-bt01-008
*variasi (konteks) | C3 | 2 langkah | jenis: himpunan nilai variabel acak selisih uji mutu*

Seorang petugas pengendali mutu memeriksa 4 unit lampu LED. Setiap lampu dikategorikan 'layak' atau 'rusak'. Misalkan variabel acak $Y$ didefinisikan sebagai banyaknya lampu layak dikurangi banyaknya lampu rusak. Himpunan semua nilai $y$ yang mungkin dari variabel acak $Y$ adalah ....

- A. $\{-4, -3, -2, -1, 0, 1, 2, 3, 4\}$  
  <sub>Salah: Menuliskan seluruh bilangan bulat di antara rentang tanpa menyadari selisih selalu bernilai genap karena total lampu genap (4).</sub>
- **B. $\{-4, -2, 0, 2, 4\}$** ✅  
  <sub>Benar: Pasangan (layak, rusak) dari 4 unit yang diperiksa adalah (0,4), (1,3), (2,2), (3,1), dan (4,0). Hasil pengurangannya adalah 0-4=-4, 1-3=-2, 2-2=0, 3-1=2, dan 4-0=4.</sub>
- C. $\{0, 2, 4\}$  
  <sub>Salah: Menggunakan nilai mutlak dari selisih sehingga nilai-nilai negatif terabaikan.</sub>
- D. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Hanya menghitung banyaknya lampu layak tanpa mengurangkan dengan banyaknya lampu rusak.</sub>

**Pembahasan:** Banyak lampu yang diperiksa $= 4$.
Misalkan $L =$ banyak lampu layak dan $R =$ banyak lampu rusak, maka $L + R = 4$ dan $Y = L - R$.

Kemungkinan pasangan $(L, R)$ dan nilai $y$:
- $L = 0, R = 4 \implies y = 0 - 4 = -4$
- $L = 1, R = 3 \implies y = 1 - 3 = -2$
- $L = 2, R = 2 \implies y = 2 - 2 = 0$
- $L = 3, R = 1 \implies y = 3 - 1 = 2$
- $L = 4, R = 0 \implies y = 4 - 0 = 4$

Jadi, himpunan semua nilai $y$ yang mungkin adalah $\{-4, -2, 0, 2, 4\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas12_tl-b04-a-medium-bt01-009
*orisinal | C3 | 2 langkah | jenis: banyak anggota prapeta selisih mata dadu*

Dua buah dadu seimbang bersisi enam dilempar bersama-sama sekali. Didefinisikan variabel acak $X$ sebagai selisih positif antara mata dadu pertama dan mata dadu kedua. Banyaknya titik sampel dalam ruang sampel yang dipetakan ke nilai $X = 3$ adalah ....

- A. 3  
  <sub>Salah: Hanya menghitung pasangan tanpa memperhatikan urutan dadu, yaitu (1, 4), (2, 5), dan (3, 6).</sub>
- B. 8  
  <sub>Salah: Memasukkan pasangan yang jumlahnya 3 atau salah menambah titik sampel di luar batas 1 sampai 6.</sub>
- **C. 6** ✅  
  <sub>Benar: Pasangan mata dadu $(d_1, d_2)$ dengan $|d_1 - d_2| = 3$ adalah (1, 4), (4, 1), (2, 5), (5, 2), (3, 6), dan (6, 3), totalnya ada 6 titik sampel.</sub>
- D. 4  
  <sub>Salah: Tertukar dengan pasangan mata dadu yang selisih positifnya 2 atau salah mencacah titik sampel.</sub>

**Pembahasan:** Ruang sampel pelemparan dua dadu memiliki $6 \times 6 = 36$ anggota.
Variabel acak $X = |d_1 - d_2|$.
Untuk mencari prapeta dari $X = 3$, cari pasangan $(d_1, d_2)$ dengan $|d_1 - d_2| = 3$:
- $d_1 - d_2 = 3 \implies (4, 1), (5, 2), (6, 3)$
- $d_2 - d_1 = 3 \implies (1, 4), (2, 5), (3, 6)$

Total titik sampel yang dipetakan ke $X = 3$ adalah $3 + 3 = 6$ anggota.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas12_tl-b04-a-medium-bt01-010
*orisinal | C3 | 3 langkah | jenis: himpunan nilai variabel acak skor koin*

Dua keping uang logam seimbang dilempar secara bersamaan sekali. Sisi koin terdiri dari Angka ($A$) dan Gambar ($G$). Didefinisikan suatu variabel acak $S$ yang memberikan skor untuk setiap hasil pelemparan: setiap sisi Angka yang muncul diberi skor $+3$, dan setiap sisi Gambar yang muncul diberi skor $-2$. Himpunan semua nilai $s$ yang mungkin dari variabel acak $S$ adalah ....

- **A. $\{-4, 1, 6\}$** ✅  
  <sub>Benar: Elemen ruang sampel adalah {GG, GA, AG, AA}. Skor masing-masing: GG = 2(-2) = -4; GA dan AG = 3 + (-2) = 1; AA = 2(3) = 6.</sub>
- B. $\{-4, 0, 6\}$  
  <sub>Salah: Salah menjumlahkan skor $3 + (-2)$ menjadi 0 alih-alih 1.</sub>
- C. $\{-4, -1, 1, 6\}$  
  <sub>Salah: Membedakan hasil AG dan GA sebagai nilai yang berlawanan tanda padahal keduanya menghasilkan skor sama yaitu 1.</sub>
- D. $\{-2, 1, 3\}$  
  <sub>Salah: Salah menghitung skor saat kedua koin kembar (GG dianggap -2 dan AA dianggap 3).</sub>

**Pembahasan:** Ruang sampel dari pelemparan 2 keping uang logam:
$S = \{AA, AG, GA, GG\}$

Aturan fungsi variabel acak $S$:
- Skor $A = +3$
- Skor $G = -2$

Evaluasi setiap titik sampel:
1. Hasil $GG$: $2 \times (-2) = -4$
2. Hasil $AG$ dan $GA$: $1 \times 3 + 1 \times (-2) = 1$
3. Hasil $AA$: $2 \times 3 = 6$

Jadi, himpunan semua nilai $s$ yang mungkin dari variabel acak $S$ adalah $\{-4, 1, 6\}$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas12_tl-b04-a-medium-bt01-011
*variasi (angka) | C3 | 3 langkah | jenis: himpunan nilai variabel acak cacat tanpa pengembalian*

Dari 9 unit sepeda motor yang dikirim oleh pabrik ke sebuah diler, sebanyak 6 unit mengalami cacat cat bodi dan sisanya dalam kondisi mulus. Diler tersebut memilih 5 unit secara acak untuk dipajang di ruang pamer. Jika variabel acak $X$ menyatakan banyaknya sepeda motor dengan cacat cat bodi yang terpilih, himpunan semua nilai $x$ yang mungkin untuk variabel acak $X$ adalah ....

- **A. $\{2, 3, 4, 5\}$** ✅  
  <sub>Benar: Banyak motor mulus hanya ada $9 - 6 = 3$ unit, sehingga dari 5 unit terpilih paling sedikit memuat $5 - 3 = 2$ unit cacat, dan paling banyak $\min(5, 6) = 5$ unit cacat.</sub>
- B. $\{1, 2, 3, 4, 5\}$  
  <sub>Salah: Salah menghitung batas bawah terambilnya motor cacat, mengira nilai 1 masih dapat dicapai.</sub>
- C. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Mengabaikan batas ketersediaan motor mulus sehingga menganggap nilai 0 dan 1 cacat mungkin terjadi padahal motor mulus hanya 3 unit.</sub>
- D. $\{2, 3, 4, 5, 6\}$  
  <sub>Salah: Memasukkan nilai 6 padahal motor yang diambil secara keseluruhan hanya 5 unit.</sub>

**Pembahasan:** Diketahui total motor $N = 9$, motor cacat $K = 6$, dan motor mulus $N - K = 3$. Diambil sebanyak $n = 5$ unit.
Nilai minimum dari $X$ terjadi jika seluruh motor mulus terambil:
$x_{\min} = 5 - 3 = 2$.
Nilai maksimum dari $X$ dibatasi oleh jumlah sampel yang diambil:
$x_{\max} = \min(5, 6) = 5$.
Jadi, himpunan nilai $x$ yang mungkin adalah $\{2, 3, 4, 5\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas12_tl-b04-a-medium-bt01-012
*variasi (angka) | C3 | 3 langkah | jenis: himpunan nilai variabel acak bola tanpa pengembalian*

Sebuah kotak memuat 3 bola merah dan 8 bola putih. Dari dalam kotak tersebut diambil sebanyak 6 bola satu per satu tanpa pengembalian. Jika variabel acak $Z$ menyatakan banyaknya bola putih yang terambil, himpunan semua kemungkinan nilai $z$ dari variabel acak $Z$ adalah ....

- A. $\{3, 4, 5, 6, 7, 8\}$  
  <sub>Salah: Memasukkan total kapasitas bola putih (hingga 8) padahal pengambilan hanya dilakukan sebanyak 6 kali.</sub>
- **B. $\{3, 4, 5, 6\}$** ✅  
  <sub>Benar: Jika semua 3 bola merah terambil, bola putih minimal terambil $6 - 3 = 3$ buah, dan bola putih maksimal yang dapat diambil adalah 6 buah.</sub>
- C. $\{0, 1, 2, 3, 4, 5, 6\}$  
  <sub>Salah: Mengasumsikan bola putih bisa bernilai 0, 1, atau 2 padahal bola merah hanya tersedia 3 butir.</sub>
- D. $\{2, 3, 4, 5, 6\}$  
  <sub>Salah: Salah menghitung batas bawah pengambilan dengan mengurangkan 6 - 4 alih-alih 6 - 3.</sub>

**Pembahasan:** Banyak bola merah = 3 dan bola putih = 8. Pengambilan dilakukan sebanyak 6 bola tanpa pengembalian.
Nilai $Z$ menyatakan banyaknya bola putih yang terambil.
Batas bawah $Z$ terjadi saat bola non-putih (merah) terambil maksimal, yaitu 3 bola merah. Sisa $6 - 3 = 3$ bola harus putih, sehingga $z_{\min} = 3$.
Batas atas $Z$ adalah saat semua bola yang terambil putih, yaitu $z_{\max} = 6$.
Jadi, nilai-nilai yang mungkin untuk variabel acak $Z$ adalah $\{3, 4, 5, 6\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas12_tl-b04-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: banyak prapeta variabel acak kuadrat selisih*

Dua buah dadu seimbang bersisi enam dilempar bersama-sama sekali. Misalkan $(a, b)$ menyatakan pasangan mata dadu yang muncul. Didefinisikan variabel acak $Y$ sebagai $Y(a, b) = (a - b)^2$. Banyaknya elemen dalam ruang sampel yang menghasilkan nilai $Y = 4$ adalah ....

- A. 4  
  <sub>Salah: Hanya menghitung pasangan dengan $a > b$ dan mengabaikan urutan sebaliknya ($b > a$).</sub>
- B. 6  
  <sub>Salah: Salah mendata pasangan selisih 2 atau keliru mengira hanya ada 3 pasang unik yang dibalik.</sub>
- C. 10  
  <sub>Salah: Keliru menjumlahkan dengan pasangan yang menghasilkan selisih 1 atau 4.</sub>
- **D. 8** ✅  
  <sub>Benar: Kondisi $(a - b)^2 = 4$ terpenuhi jika $|a - b| = 2$, yang memiliki 8 pasangan mata dadu pada ruang sampel.</sub>

**Pembahasan:** Diketahui variabel acak $Y(a, b) = (a - b)^2$. Dicari banyak pasangan $(a, b)$ dengan $1 \le a, b \le 6$ sedemikian sehingga $(a - b)^2 = 4$.
$(a - b)^2 = 4 \iff a - b = 2$ atau $a - b = -2$.
Untuk $a - b = 2$:
$(3, 1), (4, 2), (5, 3), (6, 4)$ $\rightarrow$ ada 4 elemen.
Untuk $a - b = -2$:
$(1, 3), (2, 4), (3, 5), (4, 6)$ $\rightarrow$ ada 4 elemen.
Total elemen ruang sampel yang menghasilkan nilai $Y = 4$ adalah $4 + 4 = 8$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas12_tl-b04-a-medium-bt01-014
*orisinal | C3 | 3 langkah | jenis: banyak prapeta variabel acak maksimum dadu*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Misalkan $(a, b)$ adalah pasangan mata dadu yang muncul. Suatu variabel acak $M$ didefinisikan sebagai nilai terbesar di antara kedua mata dadu tersebut, yaitu $M(a, b) = \max(a, b)$. Banyaknya anggota ruang sampel yang dipetakan ke nilai $M = 5$ adalah ....

- A. 5  
  <sub>Salah: Hanya menghitung pasangan dengan mata dadu pertama bernilai 5, melupakan ketika dadu kedua bernilai 5.</sub>
- B. 8  
  <sub>Salah: Lupa menyertakan pasangan mata dadu kembar $(5, 5)$.</sub>
- C. 10  
  <sub>Salah: Menghitung pasangan $(5, 5)$ dua kali pada saat menjumlahkan baris dan kolom.</sub>
- **D. 9** ✅  
  <sub>Benar: Pasangan $(a, b)$ dengan $\max(a, b) = 5$ terdiri atas 5 pasangan di mana dadu pertama bernilai 5 dan 4 pasangan lain di mana dadu kedua bernilai 5.</sub>

**Pembahasan:** Nilai variabel acak $M(a, b) = \max(a, b) = 5$ tercapai apabila sekurang-kurangnya satu mata dadu bernilai 5 dan mata dadu lainnya bernilai $\le 5$.
Pasangan tersebut adalah:
- Dadu pertama bernilai 5: $(5, 1), (5, 2), (5, 3), (5, 4), (5, 5)$ (5 pasangan)
- Dadu kedua bernilai 5 (dengan dadu pertama bukan 5): $(1, 5), (2, 5), (3, 5), (4, 5)$ (4 pasangan)
Total pasangan yang memenuhi adalah $5 + 4 = 9$.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas12_tl-b04-a-medium-bt01-015
*orisinal | C4 | 3 langkah | jenis: himpunan nilai variabel acak selisih kartu prima*

Sebuah kantong memuat 4 kartu bertuliskan bilangan prima satu digit, yaitu 2, 3, 5, dan 7. Dua kartu diambil secara acak sekaligus dari kantong tersebut. Jika variabel acak $D$ menyatakan selisih positif antara kedua angka pada kartu yang terambil, himpunan semua nilai yang mungkin untuk variabel acak $D$ adalah ....

- A. $\{2, 3, 4, 5\}$  
  <sub>Salah: Lupa memperhitungkan pasangan kartu 2 dan 3 yang menghasilkan selisih 1.</sub>
- B. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Memasukkan nilai 0 padahal kedua kartu diambil sekaligus sehingga tidak mungkin menghasilkan kartu bernomor sama.</sub>
- C. $\{1, 2, 3, 4\}$  
  <sub>Salah: Lupa memperhitungkan pasangan kartu 2 dan 7 yang menghasilkan selisih 5.</sub>
- **D. $\{1, 2, 3, 4, 5\}$** ✅  
  <sub>Benar: Selisih positif dari setiap pasangan dua kartu yang mungkin menghasilkan nilai 1, 2, 3, 4, dan 5.</sub>

**Pembahasan:** Kombinasi pengambilan 2 kartu dari 4 kartu $\{2, 3, 5, 7\}$ berjumlah $\binom{4}{2} = 6$ pasang:
1. Kartu $(2, 3) \rightarrow D = |2 - 3| = 1$
2. Kartu $(2, 5) \rightarrow D = |2 - 5| = 3$
3. Kartu $(2, 7) \rightarrow D = |2 - 7| = 5$
4. Kartu $(3, 5) \rightarrow D = |3 - 5| = 2$
5. Kartu $(3, 7) \rightarrow D = |3 - 7| = 4$
6. Kartu $(5, 7) \rightarrow D = |5 - 7| = 2$
Himpunan nilai unik dari variabel acak $D$ adalah $\{1, 2, 3, 4, 5\}$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas12_tl-b04-a-medium-bt01-016
*variasi (konteks) | C3 | 2 langkah | jenis: himpunan nilai variabel acak berbobot*

Sekeping uang logam seimbang dilempar sebanyak 3 kali berturut-turut. Pada setiap lemparan, kemunculan sisi angka ($A$) diberi skor 2, sedangkan kemunculan sisi gambar ($G$) diberi skor $-1$. Jika variabel acak $X$ menyatakan total skor dari ketiga lemparan tersebut, tentukan himpunan semua nilai $x$ yang mungkin dari variabel acak $X$.

- A. $\{0, 2, 4, 6\}$  
  <sub>Salah: Hanya menghitung kontribusi skor sisi angka dan mengabaikan pengurangan skor dari sisi gambar.</sub>
- **B. $\{-3, 0, 3, 6\}$** ✅  
  <sub>Benar: Banyaknya sisi angka yang muncul dapat bernilai 0, 1, 2, atau 3. Untuk 0 angka (3 gambar), skornya $3(-1) = -3$. Untuk 1 angka (2 gambar), skornya $1(2) + 2(-1) = 0$. Untuk 2 angka (1 gambar), skornya $2(2) + 1(-1) = 3$. Untuk 3 angka (0 gambar), skornya $3(2) = 6$. Jadi, himpunan nilai yang mungkin adalah $\{-3, 0, 3, 6\}$.</sub>
- C. $\{-3, -1, 1, 3\}$  
  <sub>Salah: Menggunakan selisih banyaknya sisi angka dan gambar, bukan menerapkan bobot skor yang diberikan.</sub>
- D. $\{-1, 0, 1, 2\}$  
  <sub>Salah: Hanya menghitung skor seolah-olah tiap kejadian berdiri sendiri atau membagi nilai secara keliru.</sub>

**Pembahasan:** Ruang sampel pelemparan koin 3 kali menghasilkan banyaknya sisi angka $k \in \{0, 1, 2, 3\}$ dan sisi gambar $3 - k$.
Total skor ditentukan oleh rumus:
$$X = 2k + (-1)(3 - k) = 3k - 3$$
- Untuk $k = 0$: $X = 3(0) - 3 = -3$
- Untuk $k = 1$: $X = 3(1) - 3 = 0$
- Untuk $k = 2$: $X = 3(2) - 3 = 3$
- Untuk $k = 3$: $X = 3(3) - 3 = 6$

Dengan demikian, himpunan semua nilai $x$ yang mungkin adalah $\{-3, 0, 3, 6\}$.
**Acuan:** siswa — siswa hal.243 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas12_tl-b04-a-medium-bt01-017
*variasi (konteks) | C3 | 2 langkah | jenis: himpunan nilai variabel acak perkalian*

Pak Hendra dan istrinya merencanakan memiliki 3 orang anak. Asumsikan peluang lahir anak laki-laki dan perempuan sama pada setiap kelahiran. Jika variabel acak $Y$ didefinisikan sebagai hasil kali antara banyaknya anak laki-laki dan banyaknya anak perempuan yang lahir, tentukan himpunan semua nilai $y$ yang mungkin dari variabel acak $Y$.

- A. $\{0, 1, 2, 3\}$  
  <sub>Salah: Menuliskan himpunan banyaknya anak salah satu jenis kelamin, bukan hasil kalinya.</sub>
- B. $\{1, 2, 3\}$  
  <sub>Salah: Mengabaikan kasus di mana semua anak memiliki jenis kelamin sama yang menghasilkan nilai 0.</sub>
- **C. $\{0, 2\}$** ✅  
  <sub>Benar: Kombinasi pasangan (banyak anak laki-laki, banyak anak perempuan) yang mungkin dari total 3 anak adalah (3, 0), (2, 1), (1, 2), dan (0, 3). Hasil kalinya berturut-turut adalah $3 \times 0 = 0$, $2 \times 1 = 2$, $1 \times 2 = 2$, dan $0 \times 3 = 0$. Jadi, nilai unik yang mungkin adalah $\{0, 2\}$.</sub>
- D. $\{0, 1, 2\}$  
  <sub>Salah: Mengira ada kombinasi yang menghasilkan nilai perkalian 1 padahal jumlah anak adalah 3.</sub>

**Pembahasan:** Misalkan $L$ menyatakan banyaknya anak laki-laki dan $P$ banyaknya anak perempuan. Karena total ada 3 anak, maka $P = 3 - L$, dengan $L \in \{0, 1, 2, 3\}$.
Variabel acak $Y = L \times P$:
- Jika $L = 0$, maka $P = 3 \rightarrow Y = 0 \times 3 = 0$
- Jika $L = 1$, maka $P = 2 \rightarrow Y = 1 \times 2 = 2$
- Jika $L = 2$, maka $P = 1 \rightarrow Y = 2 \times 1 = 2$
- Jika $L = 3$, maka $P = 0 \rightarrow Y = 3 \times 0 = 0$

Jadi, himpunan semua nilai $y$ yang mungkin dari variabel acak $Y$ adalah $\{0, 2\}$.
**Acuan:** siswa — siswa hal.244 Contoh Soal

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas12_tl-b04-a-medium-bt01-018
*variasi (konteks) | C3 | 2 langkah | jenis: himpunan nilai variabel acak kuadrat cacat*

Seorang apoteker menguji 4 sampel tablet obat untuk mengetahui kelayakan fisiknya. Setiap tablet dikategorikan sebagai 'memenuhi syarat' atau 'cacat'. Jika variabel acak $X$ menyatakan kuadrat dari banyaknya tablet yang cacat, tentukan himpunan semua nilai $x$ yang mungkin dari variabel acak $X$.

- A. $\{0, 2, 4, 6, 8\}$  
  <sub>Salah: Mengalikan banyaknya tablet cacat dengan 2 alih-alih menguadratkannya.</sub>
- B. $\{1, 4, 9, 16\}$  
  <sub>Salah: Lupa menyertakan nilai 0 saat tidak ada satupun tablet yang cacat.</sub>
- C. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Hanya menuliskan banyaknya tablet cacat tanpa menguadratkannya sesuai definisi variabel acak.</sub>
- **D. $\{0, 1, 4, 9, 16\}$** ✅  
  <sub>Benar: Banyak tablet cacat dari 4 sampel yang diuji dapat bernilai 0, 1, 2, 3, atau 4. Kuadrat dari nilai-nilai tersebut adalah $0^2=0$, $1^2=1$, $2^2=4$, $3^2=9$, dan $4^2=16$, sehingga himpunannya adalah $\{0, 1, 4, 9, 16\}$.</sub>

**Pembahasan:** Banyaknya tablet cacat yang mungkin ditemukan dari 4 tablet yang diperiksa adalah $k \in \{0, 1, 2, 3, 4\}$.
Karena variabel acak $X$ didefinisikan sebagai kuadrat dari banyaknya tablet cacat ($X = k^2$), maka nilai-nilai $x$ yang mungkin adalah:
- $k = 0 \rightarrow x = 0^2 = 0$
- $k = 1 \rightarrow x = 1^2 = 1$
- $k = 2 \rightarrow x = 2^2 = 4$
- $k = 3 \rightarrow x = 3^2 = 9$
- $k = 4 \rightarrow x = 4^2 = 16$

Jadi, himpunan semua nilai yang mungkin adalah $\{0, 1, 4, 9, 16\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas12_tl-b04-a-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: banyak titik sampel prapeta modulo*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Misalkan variabel acak $T$ menyatakan sisa pembagian hasil kali kedua mata dadu oleh 5. Banyaknya titik sampel dalam ruang sampel yang dipetakan ke nilai $T = 0$ adalah ....

- **A. 11** ✅  
  <sub>Benar: Nilai $T = 0$ berarti hasil kali kedua mata dadu habis dibagi 5. Karena 5 adalah bilangan prima, setidaknya salah satu dadu harus memunculkan angka 5. Ada 6 pasangan dengan dadu pertama 5 dan 6 pasangan dengan dadu kedua 5, dikurangi pasangan (5, 5) yang terhitung dua kali, sehingga totalnya $6 + 6 - 1 = 11$.</sub>
- B. 6  
  <sub>Salah: Hanya menghitung jika angka 5 muncul pada salah satu dadu saja.</sub>
- C. 10  
  <sub>Salah: Menghitung pasangan tanpa mengikutsertakan pasangan mata dadu kembar (5, 5).</sub>
- D. 12  
  <sub>Salah: Menjumlahkan pasangan bermata 5 pada kedua dadu ($6 + 6$) tanpa mengeliminasi irisan pasangan (5, 5).</sub>

**Pembahasan:** Ruang sampel pelemparan dua buah dadu memiliki $n(S) = 6 \times 6 = 36$ titik sampel berpasangan $(a, b)$ dengan $a, b \in \{1, 2, 3, 4, 5, 6\}$.
Variabel acak $T = (a \times b) \pmod 5$.
Nilai $T = 0$ terjadi jika dan hanya jika $a \times b$ kelipatan 5.
Karena 5 adalah bilangan prima, $a \times b$ habis dibagi 5 jika $a = 5$ atau $b = 5$.
- Pasangan dengan $a = 5$: $(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)$ $\rightarrow$ 6 anggota.
- Pasangan dengan $b = 5$: $(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)$ $\rightarrow$ 6 anggota.
- Irisan kedua himpunan adalah $(5, 5)$ $\rightarrow$ 1 anggota.

Banyak titik sampel yang dipetakan ke $T = 0$ adalah:
$$n(T = 0) = 6 + 6 - 1 = 11$$
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas12_tl-b04-a-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: himpunan nilai variabel acak gabungan warna dan nomor*

Sebuah kantong memuat 3 kelereng merah bernomor 1, 2, 3 dan 2 kelereng hijau bernomor 1, 2. Dua kelereng diambil sekaligus secara acak. Variabel acak $V$ bernilai 0 jika kedua kelereng yang terambil berlainan warna, dan bernilai sama dengan jumlah nomor pada kedua kelereng jika warnanya sama. Himpunan semua nilai yang mungkin dari variabel acak $V$ adalah ....

- **A. $\{0, 3, 4, 5\}$** ✅  
  <sub>Benar: Jika warna berbeda, nilainya 0. Jika sama-sama merah, pasangan nomor yang mungkin adalah {1, 2}, {1, 3}, {2, 3} dengan jumlah 3, 4, 5. Jika sama-sama hijau, pasangannya adalah {1, 2} dengan jumlah 3. Menggabungkan seluruh nilai yang mungkin menghasilkan himpunan {0, 3, 4, 5}.</sub>
- B. $\{3, 4, 5\}$  
  <sub>Salah: Lupa menyertakan nilai 0 untuk kejadian pengambilan dua kelereng yang berbeda warna.</sub>
- C. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Mencantumkan seluruh kemungkinan angka nomor kelereng tanpa memperhatikan aturan penjumlahan saat warna sama.</sub>
- D. $\{0, 2, 3, 4, 5\}$  
  <sub>Salah: Menyertakan nilai 2 seolah-olah satu kelereng bernomor 1 bisa berpasangan dengan dirinya sendiri pada warna yang sama.</sub>

**Pembahasan:** Dua kelereng diambil sekaligus dari kantong yang berisi kelereng merah $\{M_1, M_2, M_3\}$ dan hijau $\{H_1, H_2\}$.
1. Jika terambil kelereng berlainan warna (satu merah dan satu hijau):
   Nilai $V = 0$.
2. Jika terambil kelereng berwarna sama:
   - Keduanya merah: kemungkinan pasangan adalah $\{M_1, M_2\}$ bernilai $1 + 2 = 3$; $\{M_1, M_3\}$ bernilai $1 + 3 = 4$; $\{M_2, M_3\}$ bernilai $2 + 3 = 5$.
   - Keduanya hijau: kemungkinan pasangan hanya $\{H_1, H_2\}$ bernilai $1 + 2 = 3$.

Dengan demikian, nilai-nilai yang mungkin dari variabel acak $V$ adalah 0, 3, 4, dan 5.
Himpunan nilainya dituliskan $\{0, 3, 4, 5\}$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas12_tl-b04-a-hard-bt01-001
*variasi (angka) | C5 | 4 langkah | jenis: rentang nilai variabel acak pengambilan*

Sebuah kotak berisi 4 bola merah dan 7 bola putih. Dari dalam kotak tersebut diambil sebanyak 8 bola satu per satu tanpa pengembalian. Jika $Z$ menyatakan banyaknya bola putih yang terambil, tentukan himpunan semua nilai $z$ yang mungkin dari variabel acak $Z$.

- **A. $\{4, 5, 6, 7\}$** ✅  
  <sub>Benar: Karena bola merah hanya ada 4, maka pengambilan 8 bola paling banyak memuat 4 bola merah sehingga bola putih yang terambil minimal $8 - 4 = 4$. Stok bola putih hanya 7, sehingga bola putih yang terambil maksimal 7. Jadi nilai yang mungkin adalah 4, 5, 6, atau 7.</sub>
- B. $\{1, 2, 3, 4, 5, 6, 7\}$  
  <sub>Salah: Mengira bola putih minimal terambil 1 tanpa memperhitungkan jumlah maksimal bola merah yang dapat terambil.</sub>
- C. $\{4, 5, 6, 7, 8\}$  
  <sub>Salah: Mengira seluruh 8 bola yang terambil bisa semuanya berwarna putih, padahal stok bola putih hanya ada 7.</sub>
- D. $\{0, 1, 2, 3, 4, 5, 6, 7\}$  
  <sub>Salah: Mengabaikan batas bawah bahwa bola merah hanya tersedia 4 sehingga bola putih tidak mungkin berjumlah kurang dari 4.</sub>

**Pembahasan:** Diketahui:
Jumlah bola merah = 4
Jumlah bola putih = 7
Total bola yang diambil = 8 secara acak tanpa pengembalian.

Langkah 1: Menentukan batas bawah nilai $Z$.
Jika seluruh bola merah terambil (maksimal 4 bola merah), maka sisa bola yang terambil harus berupa bola putih, yaitu $8 - 4 = 4$ bola putih. Maka, nilai terkecil $Z$ adalah 4.

Langkah 2: Menentukan batas atas nilai $Z$.
Jumlah seluruh bola putih di dalam kotak hanya ada 7. Meskipun diambil 8 bola, banyaknya bola putih yang terambil tidak mungkin melebihi stok yang ada. Jadi, nilai terbesar $Z$ adalah 7 (terdiri dari 7 putih dan 1 merah, di mana stok merah mencukupi).

Langkah 3: Menentukan seluruh kemungkinan nilai.
Nilai $z$ dapat bernilai bilangan bulat dari batas bawah hingga batas atas: 4, 5, 6, 7.

Jadi, himpunan semua nilai $z$ yang mungkin dari variabel acak $Z$ adalah $\{4, 5, 6, 7\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas12_tl-b04-a-hard-bt01-002
*variasi (angka) | C5 | 4 langkah | jenis: nilai variabel acak dengan batas kapasitas*

Dari 10 mobil yang dikirim sebuah pabrik, sebanyak 4 mobil tiba dalam keadaan tergores. Sebuah toko menerima 8 mobil secara acak. Misalkan $T$ menyatakan ruang sampel, $G$ untuk kondisi mobil "tergores", dan $B$ untuk kondisi mobil yang "baik". Variabel acak $X$ menyatakan banyak mobil terkena goresan yang diterima oleh toko tersebut. Tentukan himpunan semua nilai $x$ yang mungkin dari variabel acak $X$.

- A. $\{1, 2, 3, 4\}$  
  <sub>Salah: Mengira batas bawah mobil tergores adalah 1, lupa bahwa 6 mobil baik tidak cukup untuk memenuhi penerimaan 8 mobil.</sub>
- B. $\{2, 3, 4, 5, 6, 7, 8\}$  
  <sub>Salah: Mengabaikan batas atas stok mobil tergores yang hanya ada 4 unit dari pabrik.</sub>
- C. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Mengasumsikan mobil tergores bisa bernilai 0 atau 1 tanpa menyadari bahwa mobil baik hanya berjumlah 6 unit.</sub>
- **D. $\{2, 3, 4\}$** ✅  
  <sub>Benar: Mobil baik hanya ada $10 - 4 = 6$. Jika toko menerima 8 mobil dan seluruh mobil baik terpilih, minimal ada $8 - 6 = 2$ mobil tergores. Karena total mobil tergores hanya ada 4, mobil tergores maksimal yang diterima adalah 4.</sub>

**Pembahasan:** Langkah 1: Identifikasi komposisi mobil dari pabrik.
Total mobil = 10 unit.
Mobil tergores ($G$) = 4 unit.
Mobil baik ($B$) = $10 - 4 = 6$ unit.

Langkah 2: Analisis batas minimum variabel acak $X$.
Toko menerima 8 mobil. Apabila toko menerima semua mobil baik yang ada (yaitu 6 unit), maka sisa mobil yang diterima harus merupakan mobil tergores: $8 - 6 = 2$ unit. Jadi, nilai minimum $x = 2$.

Langkah 3: Analisis batas maksimum variabel acak $X$.
Jumlah mobil tergores yang tersedia di pabrik hanya 4 unit. Apabila semua mobil tergores diterima oleh toko, maka toko menerima 4 mobil tergores dan 4 mobil baik (stok mobil baik mencukupi karena ada 6 unit). Jadi, nilai maksimum $x = 4$.

Langkah 4: Menentukan himpunan nilai variabel acak.
Nilai-nilai $x$ yang mungkin terletak antara 2 dan 4, yaitu $\{2, 3, 4\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas12_tl-b04-a-hard-bt01-003
*orisinal | C5 | 4 langkah | jenis: analisis ruang sampel dan nilai variabel acak*

Sebuah kotak memuat $n$ kartu yang masing-masing bertuliskan bilangan bulat dari 1 sampai $n$ (dengan $n > 3$). Dua kartu diambil secara acak sekaligus dari kotak tersebut. Didefinisikan variabel acak $W$ sebagai selisih positif antara kedua angka pada kartu yang terambil. Jika banyaknya anggota himpunan semua nilai yang mungkin dari variabel acak $W$ adalah 7, maka banyaknya seluruh anggota ruang sampel pada percobaan tersebut adalah ....

- A. 56  
  <sub>Salah: Menggunakan rumus permutasi $P(8, 2)$ alih-alih kombinasi untuk pengambilan dua kartu secara sekaligus.</sub>
- **B. 28** ✅  
  <sub>Benar: Nilai selisih positif terendah adalah 1 dan tertinggi adalah $n - 1$, sehingga ada $n - 1$ nilai yang mungkin. Karena ada 7 nilai yang mungkin, diperoleh $n = 8$, sehingga ukuran ruang sampel adalah $\binom{8}{2} = 28$.</sub>
- C. 36  
  <sub>Salah: Keliru menyimpulkan $n = 9$ sehingga menghitung $\binom{9}{2} = 36$.</sub>
- D. 21  
  <sub>Salah: Keliru menganggap banyaknya kartu sama dengan banyaknya nilai variabel acak ($n = 7$), sehingga menghitung $\binom{7}{2} = 21$.</sub>

**Pembahasan:** Langkah 1: Menganalisis nilai-nilai yang mungkin dari variabel acak $W$.
Dua kartu diambil sekaligus dari kartu bernomor $1, 2, 3, \dots, n$. Selisih positif terkecil terjadi pada dua angka berurutan, yaitu $|k - (k+1)| = 1$. Selisih positif terbesar terjadi pada kartu terkecil dan kartu terbesar, yaitu $|n - 1| = n - 1$.

Langkah 2: Menghitung banyaknya kemungkinan nilai $W$.
Seluruh bilangan bulat dari 1 sampai $n - 1$ dapat dibentuk sebagai selisih dua kartu. Jadi, himpunan nilai yang mungkin dari $W$ adalah $\{1, 2, 3, \dots, n - 1\}$, yang memiliki sebanyak $n - 1$ anggota.

Langkah 3: Menentukan nilai $n$.
Diketahui banyaknya nilai yang mungkin adalah 7, maka:
$n - 1 = 7 \implies n = 8$.

Langkah 4: Menghitung banyaknya anggota ruang sampel $n(S)$.
Pengambilan 2 kartu sekaligus dari 8 kartu merupakan kombinasi:
$n(S) = \binom{8}{2} = \frac{8 \times 7}{2 \times 1} = 28$.
**Acuan:** siswa — siswa hal.241

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas12_tl-b04-a-hard-bt01-004
*variasi (angka) | C5 | 4 langkah | jenis: rentang nilai variabel acak bersyarat*

Dari 15 unit drone yang dikirim sebuah pabrik, sebanyak 6 unit tiba dalam keadaan cacat sensor dan sisanya dalam kondisi baik. Sebuah instansi menerima 11 unit drone secara acak. Misalkan $T$ menyatakan ruang sampel, $C$ untuk kondisi drone cacat sensor, dan $B$ untuk kondisi drone baik. Variabel acak $X$ menyatakan banyak drone cacat sensor yang diterima oleh instansi tersebut. Himpunan semua nilai $x$ yang mungkin dari variabel acak $X$ adalah ....

- A. $\{0, 1, 2, 3, 4, 5, 6\}$  
  <sub>Salah: Mengabaikan fakta bahwa jumlah drone baik hanya 9 unit sehingga nilai 0 dan 1 mustahil terjadi.</sub>
- **B. $\{2, 3, 4, 5, 6\}$** ✅  
  <sub>Benar: Jumlah drone baik yang tersedia adalah $15 - 6 = 9$ unit. Karena instansi mengambil 11 unit drone, jika semua 9 drone baik terambil, instansi tetap harus menerima minimal $11 - 9 = 2$ drone cacat sensor. Karena total drone cacat sensor hanya ada 6 unit, nilai maksimum drone cacat sensor yang terambil adalah 6. Jadi, nilai $x$ yang mungkin adalah $\{2, 3, 4, 5, 6\}$.</sub>
- C. $\{1, 2, 3, 4, 5, 6\}$  
  <sub>Salah: Salah menghitung selisih minimal drone cacat yang harus terambil ($11 - 9 = 2$, bukan 1).</sub>
- D. $\{2, 3, 4, 5\}$  
  <sub>Salah: Mengira nilai maksimum drone cacat yang terambil dibatasi oleh selisih pengurang bukan jumlah total drone cacat yang ada.</sub>

**Pembahasan:** Total drone = 15 unit, dengan rincian:
- Drone cacat sensor ($C$) = 6 unit
- Drone baik ($B$) = $15 - 6 = 9$ unit

Banyak drone yang diambil = 11 unit.
1. Nilai minimum $X$ tercapai jika terambil drone baik sebanyak-banyaknya (yaitu seluruh 9 unit drone baik terambil):
   $x_{\min} = 11 - 9 = 2$.
2. Nilai maksimum $X$ tercapai jika terambil drone cacat sebanyak-banyaknya. Karena hanya ada 6 drone cacat dan $11 \ge 6$, semua drone cacat dapat terambil:
   $x_{\max} = 6$.

Dengan demikian, nilai $x$ yang mungkin dari variabel acak $X$ adalah bilangan bulat dari 2 sampai 6, yaitu $\{2, 3, 4, 5, 6\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-2

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas12_tl-b04-a-hard-bt01-005
*orisinal | C6 | 5 langkah | jenis: penentuan parameter prainang variabel acak*

Sebuah kotak berisi $k$ kartu merah bernomor 2 dan 4 kartu biru bernomor 5. Dua kartu diambil sekaligus secara acak. Variabel acak $Y$ menyatakan jumlah angka pada kedua kartu yang terambil. Jika daerah hasil dari variabel acak $Y$ adalah $\{4, 7, 10\}$ dan banyaknya elemen ruang sampel yang menghasilkan nilai $Y = 7$ adalah 24, tentukan banyaknya anggota ruang sampel yang menghasilkan nilai $Y$ berupa bilangan genap.

- A. 27  
  <sub>Salah: Salah menghitung nilai $k$ menjadi 8 karena membagi 24 dengan 3 alih-alih dengan 4.</sub>
- B. 15  
  <sub>Salah: Hanya menghitung kemungkinan terambilnya dua kartu merah ($Y = 4$) dan lupa menambahkan kasus dua kartu biru ($Y = 10$).</sub>
- **C. 21** ✅  
  <sub>Benar: Nilai $Y = 7$ berasal dari pengambilan 1 kartu merah dan 1 kartu biru, sehingga $k \times 4 = 24 \implies k = 6$. Nilai $Y$ bernilai genap jika $Y = 4$ (dua kartu merah) atau $Y = 10$ (dua kartu biru). Banyaknya anggota ruang sampel untuk $Y = 4$ adalah $\binom{6}{2} = 15$ dan untuk $Y = 10$ adalah $\binom{4}{2} = 6$. Jumlahnya adalah $15 + 6 = 21$.</sub>
- D. 45  
  <sub>Salah: Menghitung seluruh total anggota ruang sampel $\binom{10}{2} = 45$ tanpa menyisihkan elemen yang menghasilkan nilai ganjil ($Y = 7$).</sub>

**Pembahasan:** Dalam kotak terdapat $k$ kartu merah bertuliskan angka 2 dan 4 kartu biru bertuliskan angka 5.
Diambil 2 kartu sekaligus secara acak.
Nilai-nilai yang mungkin dari $Y$ (jumlah kedua angka):
- 2 kartu merah: $2 + 2 = 4$
- 1 merah dan 1 biru: $2 + 5 = 7$
- 2 kartu biru: $5 + 5 = 10$

Banyaknya hasil yang menghasilkan $Y = 7$ diperoleh dari memilih 1 kartu merah dari $k$ kartu dan 1 kartu biru dari 4 kartu:
$n(Y = 7) = \binom{k}{1} \times \binom{4}{1} = 4k$
Diketahui $4k = 24 \implies k = 6$.

Nilai $Y$ yang berupa bilangan genap adalah $Y = 4$ dan $Y = 10$:
- Untuk $Y = 4$ (keduanya merah): $\binom{k}{2} = \binom{6}{2} = \frac{6 \times 5}{2} = 15$.
- Untuk $Y = 10$ (keduanya biru): $\binom{4}{2} = \frac{4 \times 3}{2} = 6$.

Banyak anggota ruang sampel yang menghasilkan $Y$ genap adalah $15 + 6 = 21$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas12_tl-b04-a-hard-bt01-006
*orisinal | C5 | 4 langkah | jenis: evaluasi klaim variabel acak*

Empat keping uang logam seimbang dilempar secara bersamaan satu kali. Setiap keping memiliki sisi Angka ($A$) dan Gambar ($G$). Didefinisikan dua variabel acak:
- $X$ menyatakan selisih mutlak antara banyaknya sisi Angka dan banyaknya sisi Gambar yang muncul.
- $Y$ menyatakan kuadrat dari selisih tersebut, yaitu $Y = X^2$.

Perhatikan pernyataan-pernyataan berikut:
(1) Daerah hasil dari variabel acak $X$ adalah $\{0, 1, 2, 3, 4\}$.
(2) Banyaknya elemen ruang sampel yang dipetakan ke nilai $X = 0$ adalah 6.
(3) Daerah hasil dari variabel acak $Y$ adalah $\{0, 4, 16\}$.
(4) Banyaknya elemen ruang sampel yang menghasilkan nilai $Y \le 4$ adalah 8.

Pernyataan yang bernilai BENAR adalah ....

- **A. (2) dan (3)** ✅  
  <sub>Benar: Pernyataan (2) benar karena $X = 0$ terjadi jika muncul 2 Angka dan 2 Gambar dengan $\binom{4}{2} = 6$ cara. Pernyataan (3) benar karena nilai $X \in \{0, 2, 4\}$ sehingga nilai $Y = X^2 \in \{0^2, 2^2, 4^2\} = \{0, 4, 16\}$. Pernyataan (1) salah karena nilai ganjil tidak mungkin tercapai. Pernyataan (4) salah karena banyaknya elemen dengan $Y \le 4$ adalah $6 + 8 = 14$.</sub>
- B. (1) dan (4)  
  <sub>Salah: Mengalami dua kesalahan sekaligus: menganggap rentang selisih berurutan lengkap dan mengabaikan batas bawah pertidaksamaan.</sub>
- C. (2) dan (4)  
  <sub>Salah: Keliru pada pernyataan (4) dengan hanya menghitung elemen untuk $Y = 4$ dan melupakan nilai $Y = 0$ yang juga memenuhi $Y \le 4$.</sub>
- D. (1) dan (3)  
  <sub>Salah: Mengira selisih mutlak dapat menghasilkan seluruh bilangan cacah dari 0 sampai 4 tanpa menyadari paritas selisih selalu genap.</sub>

**Pembahasan:** Pelemparan 4 koin memiliki ruang sampel berukuran $n(S) = 2^4 = 16$.
Misalkan banyak Angka yang muncul adalah $k \in \{0, 1, 2, 3, 4\}$, maka banyak Gambar adalah $4 - k$.
Nilai $X = |k - (4 - k)| = |2k - 4|$:
- $k = 0$: $X = |0 - 4| = 4$, banyak cara $\binom{4}{0} = 1$.
- $k = 1$: $X = |2 - 4| = 2$, banyak cara $\binom{4}{1} = 4$.
- $k = 2$: $X = |4 - 4| = 0$, banyak cara $\binom{4}{2} = 6$.
- $k = 3$: $X = |6 - 4| = 2$, banyak cara $\binom{4}{3} = 4$.
- $k = 4$: $X = |8 - 4| = 4$, banyak cara $\binom{4}{4} = 1$.

Evaluasi pernyataan:
(1) Nilai $X$ yang mungkin hanya $\{0, 2, 4\}$. Pernyataan (1) SALAH.
(2) Elemen ruang sampel untuk $X = 0$ berjumlah 6. Pernyataan (2) BENAR.
(3) Nilai $Y = X^2$ dengan $X \in \{0, 2, 4\}$ adalah $\{0^2, 2^2, 4^2\} = \{0, 4, 16\}$. Pernyataan (3) BENAR.
(4) Nilai $Y \le 4$ dipenuhi oleh $Y = 0$ (6 elemen) dan $Y = 4$ (terjadi saat $X = 2$, yaitu $4 + 4 = 8$ elemen). Jadi total elemen untuk $Y \le 4$ adalah $6 + 8 = 14$, bukan 8. Pernyataan (4) SALAH.

Jadi, pernyataan yang bernilai benar adalah (2) dan (3).
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas12_tl-b04-a-hard-bt01-007
*variasi (konteks) | C5 | 4 langkah | jenis: rentang nilai variabel acak bersyarat*

Seorang petugas kendali mutu melakukan pemeriksaan terhadap 5 unit prosesor komputer. Hasil pengamatan dikategorikan dalam komponen 'layak' dan 'rusak'. $X$ adalah variabel acak yang menyatakan banyaknya prosesor yang rusak. Jika diketahui paling sedikit 2 unit prosesor dalam kondisi layak, himpunan semua nilai $x$ yang mungkin dari variabel acak $X$ adalah ....

- A. $\{0, 1, 2, 3, 4, 5\}$  
  <sub>Salah: Mengabaikan syarat bahwa paling sedikit 2 unit prosesor dalam kondisi layak.</sub>
- B. $\{2, 3, 4, 5\}$  
  <sub>Salah: Tertukar mendefinisikan variabel acak untuk prosesor yang layak bukan yang rusak.</sub>
- **C. $\{0, 1, 2, 3\}$** ✅  
  <sub>Benar: Total prosesor adalah 5 unit. Karena paling sedikit 2 unit dalam kondisi layak, maka banyaknya prosesor rusak maksimal $5 - 2 = 3$ unit, sehingga nilai $x$ yang mungkin adalah $0, 1, 2, 3$.</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Mengabaikan kemungkinan tidak ada prosesor rusak (nilai 0).</sub>

**Pembahasan:** Misalkan $L$ menyatakan banyaknya prosesor layak dan $X$ menyatakan banyaknya prosesor rusak. Jumlah total prosesor yang diperiksa adalah 5, sehingga berlaku $L + X = 5$ atau $X = 5 - L$. Berdasarkan informasi soal, paling sedikit 2 unit dalam kondisi layak, yang berarti $L \ge 2$. Dengan menyubstitusikan nilai batas $L$, diperoleh $X = 5 - L \le 5 - 2 = 3$. Karena banyaknya prosesor rusak tidak mungkin negatif, nilai $X$ harus memenuhi $0 \le X \le 3$ dengan $X$ bilangan cacah. Jadi, himpunan semua nilai $x$ yang mungkin dari variabel acak $X$ adalah $\{0, 1, 2, 3\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas12_tl-b04-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: kardinalitas prainang variabel acak FPB*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Pasangan mata dadu yang muncul dinyatakan sebagai $(a, b)$ dengan $a, b \in \{1, 2, 3, 4, 5, 6\}$. Didefinisikan variabel acak $X = \gcd(a, b)$, yaitu faktor persekutuan terbesar dari bilangan $a$ dan $b$. Banyaknya elemen ruang sampel yang dipetakan ke nilai $X = 2$ adalah ....

- A. 6  
  <sub>Salah: Lupa menyertakan pasangan kembar (2,2) yang memiliki FPB = 2.</sub>
- **B. 7** ✅  
  <sub>Benar: Hanya pasangan mata dadu genap yang saling prima setelah dibagi 2 yang menghasilkan FPB = 2, yaitu (2,2), (2,4), (2,6), (4,2), (4,6), (6,2), dan (6,4).</sub>
- C. 5  
  <sub>Salah: Hanya menghitung pasangan tanpa memperhitungkan urutan kemunculan dadu pertama dan kedua.</sub>
- D. 9  
  <sub>Salah: Menghitung seluruh pasangan genap ($3 \times 3 = 9$) tanpa mengecualikan pasangan (4,4) dan (6,6).</sub>

**Pembahasan:** Variabel acak bernilai $X = \gcd(a, b) = 2$. Agar FPB dari dua bilangan adalah 2, kedua bilangan harus merupakan kelipatan 2 (bilangan genap) dan hasil baginya dengan 2 harus saling prima. Mata dadu genap yang tersedia adalah $\{2, 4, 6\}$. Dari himpunan tersebut, pasangan yang mungkin adalah:
- Pasangan dengan angka 2: $(2, 2)$ memiliki $\gcd(2,2)=2$; $(2, 4)$ dan $(4, 2)$ memiliki $\gcd(2,4)=2$; $(2, 6)$ dan $(6, 2)$ memiliki $\gcd(2,6)=2$.
- Pasangan dengan angka 4 dan 6: $(4, 6)$ dan $(6, 4)$ memiliki $\gcd(4,6)=2$.
- Pasangan $(4, 4)$ memiliki $\gcd(4,4)=4 \ne 2$.
- Pasangan $(6, 6)$ memiliki $\gcd(6,6)=6 \ne 2$.
Menghitung total pasangan yang memenuhi: $(2, 2), (2, 4), (2, 6), (4, 2), (4, 6), (6, 2), (6, 4)$. Terdapat tepat 7 elemen ruang sampel.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas12_tl-b04-a-hard-bt01-009
*orisinal | C6 | 5 langkah | jenis: rekonstruksi parameter ruang sampel variabel acak*

Sekeping uang logam seimbang dilempar sebanyak $n$ kali ($n$ bilangan bulat positif). Didefinisikan variabel acak $W$ sebagai selisih mutlak antara banyaknya sisi Angka dan banyaknya sisi Gambar yang muncul. Jika himpunan semua nilai yang mungkin dari $W$ memiliki tepat 5 anggota dan nilai maksimum dari $W$ adalah 8, banyaknya anggota ruang sampel $n(S)$ dari percobaan tersebut adalah ....

- A. 512  
  <sub>Salah: Mengira nilai maksimum 8 terjadi pada $n = 9$ lalu menghitung $2^9$.</sub>
- B. 128  
  <sub>Salah: Salah menentukan nilai $n = 7$ lalu menghitung $2^7$.</sub>
- C. 64  
  <sub>Salah: Keliru mengira $n = 6$ karena salah mengaitkan jumlah anggota himpunan dengan $n$.</sub>
- **D. 256** ✅  
  <sub>Benar: Nilai maksimum selisih mutlak pada $n$ lemparan adalah $n = 8$, sehingga ukuran ruang sampel adalah $2^8 = 256$.</sub>

**Pembahasan:** Misalkan uang logam dilempar sebanyak $n$ kali. Jika sisi Angka muncul sebanyak $k$ kali dengan $k \in \{0, 1, 2, \dots, n\}$, maka sisi Gambar muncul sebanyak $n - k$ kali. Variabel acak $W$ didefinisikan sebagai $W = |k - (n - k)| = |2k - n|$. Nilai maksimum dari $W$ terjadi ketika seluruh lemparan menghasilkan sisi yang sama ($k = n$ atau $k = 0$), yaitu $W_{\max} = |2(n) - n| = n$. Diketahui nilai maksimum dari $W$ adalah 8, sehingga $n = 8$. Untuk $n = 8$, nilai $2k - 8$ dengan $k \in \{0, 1, \dots, 8\}$ adalah $\{-8, -6, -4, -2, 0, 2, 4, 6, 8\}$. Nilai mutlaknya menghasilkan himpunan nilai $W = \{0, 2, 4, 6, 8\}$ yang tepat memiliki 5 anggota (sesuai dengan informasi pada soal). Banyaknya anggota ruang sampel dari pelemparan sekeping uang logam sebanyak $n = 8$ kali adalah $n(S) = 2^n = 2^8 = 256$.
**Acuan:** siswa — siswa hal.242

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas12_tl-b04-a-hard-bt01-010
*variasi (angka) | C5 | 4 langkah | jenis: evaluasi batas rentang variabel acak*

Sebuah kotak berisi 7 bola merah dan 4 bola putih. Dari kotak tersebut diambil 8 bola sekaligus secara acak tanpa pengembalian. Jika variabel acak $Z$ menyatakan banyaknya bola putih yang terambil, tentukan himpunan semua nilai $z$ yang mungkin dari variabel acak $Z$.

- **A. $\{1, 2, 3, 4\}$** ✅  
  <sub>Benar: Total bola ada $7 + 4 = 11$. Karena diambil 8 bola dan bola merah maksimal hanya ada 7, maka minimal bola putih yang terambil adalah $8 - 7 = 1$. Sementara itu, jumlah seluruh bola putih hanya 4, sehingga maksimal bola putih yang terambil adalah 4. Nilai $z$ yang mungkin adalah $\{1, 2, 3, 4\}$.</sub>
- B. $\{4, 5, 6, 7, 8\}$  
  <sub>Salah: Tertukar menghitung rentang kemungkinan banyaknya bola merah yang terambil, bukan bola putih.</sub>
- C. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Menganggap nilai $z = 0$ mungkin terjadi tanpa mengevaluasi bahwa jika putih 0, bola merah harus 8 sedangkan stok merah hanya 7.</sub>
- D. $\{1, 2, 3\}$  
  <sub>Salah: Salah menentukan batas maksimum dengan mengabaikan bahwa seluruh 4 bola putih dapat terambil bersama 4 bola merah.</sub>

**Pembahasan:** Diketahui:
- Bola merah: 7
- Bola putih: 4
- Total bola: 11
- Bola yang diambil: 8

Misalkan $z$ adalah banyak bola putih yang terambil.
1. Nilai minimum $z$ tercapai jika bola merah terambil sebanyak mungkin (7 bola merah):
$z_{\text{min}} = 8 - 7 = 1$.
2. Nilai maksimum $z$ dibatasi oleh jumlah bola putih yang tersedia di kotak, yaitu 4:
$z_{\text{maks}} = \min(8, 4) = 4$.

Dengan demikian, nilai $z$ yang mungkin dari variabel acak $Z$ adalah $\{1, 2, 3, 4\}$.
**Acuan:** siswa — siswa hal.244 Ayo Mencoba

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas12_tl-b04-a-hard-bt01-011
*orisinal | C5 | 4 langkah | jenis: analisis kesetaraan prainang variabel acak*

Sebanyak 5 keping uang logam seimbang dilempar bersamaan satu kali. Setiap keping memiliki sisi Angka ($A$) dan Gambar ($G$). Didefinisikan variabel acak $W = |n_A - n_G|$, yaitu selisih mutlak antara banyaknya sisi Angka ($n_A$) dan banyaknya sisi Gambar ($n_G$) yang muncul pada kelima keping. Manakah pernyataan yang BENAR mengenai variabel acak $W$?
(1) Himpunan semua nilai $w$ yang mungkin dari variabel acak $W$ adalah $\{1, 3, 5\}$.
(2) Nilai $w = 1$ dihasilkan oleh tepat 20 elemen ruang sampel.
(3) Banyaknya elemen ruang sampel yang menghasilkan $w = 3$ sama dengan banyaknya elemen ruang sampel yang menghasilkan $w = 1$.
(4) Nilai $w = 5$ dihasilkan oleh tepat 2 elemen ruang sampel.

- A. (1), (3), dan (4)  
  <sub>Salah: Menganggap prainang untuk $w=1$ dan $w=3$ simetris sehingga pernyataan (3) dinilai benar.</sub>
- B. (1) dan (3)  
  <sub>Salah: Mengira prainang $w=3$ dan $w=1$ berjumlah sama.</sub>
- C. (2) dan (3)  
  <sub>Salah: Mengabaikan himpunan nilai $W$ pada pernyataan (1) dan memilih (3) yang salah.</sub>
- **D. (1), (2), dan (4)** ✅  
  <sub>Benar: Pasangan $(n_A, n_G)$ yang mungkin dari 5 koin: (5,0) selisih 5; (4,1) selisih 3; (3,2) selisih 1; (2,3) selisih 1; (1,4) selisih 3; (0,5) selisih 5. Maka nilai $W$ adalah {1, 3, 5} (pernyataan 1 benar). Nilai $w=1$ berasal dari (3,2) dan (2,3) dengan banyak cara $\binom{5}{3} + \binom{5}{2} = 10 + 10 = 20$ (pernyataan 2 benar). Nilai $w=3$ berasal dari (4,1) dan (1,4) dengan banyak cara $\binom{5}{4} + \binom{5}{1} = 5 + 5 = 10 \neq 20$ (pernyataan 3 salah). Nilai $w=5$ berasal dari (5,0) dan (0,5) yaitu AAAAA dan GGGGG, ada 2 elemen (pernyataan 4 benar).</sub>

**Pembahasan:** Total ruang sampel pelemparan 5 uang logam adalah $n(S) = 2^5 = 32$.
Banyaknya sisi Angka ($n_A$) dan sisi Gambar ($n_G$) memenuhi $n_A + n_G = 5$.

Kemungkinan pasangan $(n_A, n_G)$, nilai $w = |n_A - n_G|$, dan banyaknya titik sampel:
1. $n_A = 5, n_G = 0 \implies w = |5 - 0| = 5$, banyak titik: $\binom{5}{5} = 1$.
2. $n_A = 4, n_G = 1 \implies w = |4 - 1| = 3$, banyak titik: $\binom{5}{4} = 5$.
3. $n_A = 3, n_G = 2 \implies w = |3 - 2| = 1$, banyak titik: $\binom{5}{3} = 10$.
4. $n_A = 2, n_G = 3 \implies w = |2 - 3| = 1$, banyak titik: $\binom{5}{2} = 10$.
5. $n_A = 1, n_G = 4 \implies w = |1 - 4| = 3$, banyak titik: $\binom{5}{1} = 5$.
6. $n_A = 0, n_G = 5 \implies w = |0 - 5| = 5$, banyak titik: $\binom{5}{0} = 1$.

Rekapitulasi nilai variabel acak $W$:
- $w = 1$: ada $10 + 10 = 20$ titik sampel.
- $w = 3$: ada $5 + 5 = 10$ titik sampel.
- $w = 5$: ada $1 + 1 = 2$ titik sampel.

Uji kebenaran pernyataan:
- (1) Nilai yang mungkin adalah $\{1, 3, 5\}$ (BENAR).
- (2) Nilai $w = 1$ dihasilkan oleh 20 elemen (BENAR).
- (3) Elemen untuk $w = 3$ adalah 10, sedangkan $w = 1$ adalah 20, sehingga tidak sama (SALAH).
- (4) Nilai $w = 5$ dihasilkan oleh 2 elemen (BENAR).

Pernyataan yang benar adalah (1), (2), dan (4).
**Acuan:** siswa — siswa hal.242

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas12_tl-b04-a-hard-bt01-012
*variasi (konteks) | C5 | 4 langkah | jenis: evaluasi batas rentang variabel acak bersyarat*

Seorang auditor sistem mutu melakukan pemeriksaan berurutan terhadap paling banyak 4 unit server. Setiap server yang diperiksa dikategorikan 'normal' atau 'kritis'. Prosedur menetapkan bahwa pemeriksaan akan segera dihentikan jika auditor telah menemukan tepat 2 server berkondisi 'kritis', atau berhenti setelah selesai memeriksa 4 server. Jika variabel acak $K$ menyatakan banyaknya server yang diperiksa oleh auditor tersebut, tentukan himpunan semua nilai $k$ yang mungkin dari variabel acak $K$.

- A. $\{0, 1, 2, 3, 4\}$  
  <sub>Salah: Tertukar dengan variabel acak yang mencacah banyaknya server kritis dari 4 server yang diperiksa.</sub>
- B. $\{2, 4\}$  
  <sub>Salah: Mengabaikan kasus di mana server kritis kedua ditemukan tepat pada urutan ke-3.</sub>
- **C. $\{2, 3, 4\}$** ✅  
  <sub>Benar: Penghentian dini hanya dapat terjadi jika ditemukan 2 server kritis (minimal 2 server), yaitu pada server ke-2 atau ke-3; jika belum mencapai 2 server kritis, pemeriksaan berlanjut hingga server ke-4.</sub>
- D. $\{1, 2, 3, 4\}$  
  <sub>Salah: Mengira pemeriksaan dapat langsung dihentikan pada server ke-1 jika ditemukan server kritis.</sub>

**Pembahasan:** Misalkan status tiap server adalah $N$ (normal) atau $K$ (kritis). Aturan: berhenti saat ditemukan server $K$ kedua, atau setelah memeriksa 4 server.
1. Kasus $K = 1$: tidak mungkin terjadi karena maksimal baru 1 server kritis yang ditemukan sehingga pemeriksaan harus dilanjutkan.
2. Kasus $K = 2$: terjadi jika dua server pertama adalah $KK$. Pemeriksaan langsung berhenti setelah 2 server.
3. Kasus $K = 3$: terjadi jika server kritis kedua muncul di urutan ke-3, yaitu urutan $NKK$ atau $KNK$. Pemeriksaan berhenti setelah 3 server.
4. Kasus $K = 4$: terjadi jika server kritis kedua ditemukan pada urutan ke-4 ($NNKK, NKNK, KNNK$) atau jika pemeriksaan selesai tanpa pernah menemukan 2 server kritis ($NNNN, KNNN, NKNN, NNKN, NNNK$).
Dengan demikian, himpunan semua nilai yang mungkin dari variabel acak $K$ adalah $\{2, 3, 4\}$.
**Acuan:** pretest — kelas12_tl-b04-p0245-latihan-soal-variabel-acak-1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 53. [hard] kelas12_tl-b04-a-hard-bt01-013
*orisinal | C5 | 4 langkah | jenis: analisis prainang variabel acak modulo*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Pasangan mata dadu yang muncul dinyatakan sebagai $(a, b)$ dengan $a, b \in \{1, 2, 3, 4, 5, 6\}$. Didefinisikan suatu variabel acak $X$ sebagai sisa pembagian dari hasil kali kedua mata dadu $(a \times b)$ oleh 6. Tentukan nilai $x$ dari variabel acak $X$ yang memiliki ukuran prainang (banyaknya elemen ruang sampel yang dipetakan ke $x$) paling besar, beserta banyaknya elemen tersebut.

- A. $x = 2$ dengan 8 pasangan  
  <sub>Salah: Keliru menjumlahkan kombinasi modular dan memasukkan pasangan yang menghasilkan sisa pembagian lain.</sub>
- B. $x = 0$ dengan 11 pasangan  
  <sub>Salah: Hanya menghitung pasangan yang memuat setidaknya satu angka 6 tanpa memperhitungkan pasangan faktor perkalian $2 \times 3$ dan $4 \times 3$.</sub>
- C. $x = 4$ dengan 10 pasangan  
  <sub>Salah: Menghitung secara berlebih pasangan yang kongruen dengan 4 modulo 6.</sub>
- **D. $x = 0$ dengan 15 pasangan** ✅  
  <sub>Benar: Nilai $X = 0$ berarti $a \times b$ kelipatan 6, yang dihasilkan oleh 15 pasangan berbeda pada pelemparan dua dadu.</sub>

**Pembahasan:** Ruang sampel pelemparan dua dadu memiliki $n(S) = 6 \times 6 = 36$ elemen. Variabel acak $X = (a \times b) \pmod 6$ memiliki nilai yang mungkin $\{0, 1, 2, 3, 4, 5\}$.
1. Untuk $X = 0$, artinya $a \times b$ habis dibagi 6:
   - Memuat angka 6 pada dadu pertama: $(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)$ (6 pasangan).
   - Memuat angka 6 pada dadu kedua dengan $a \ne 6$: $(1, 6), (2, 6), (3, 6), (4, 6), (5, 6)$ (5 pasangan).
   - Tidak memuat angka 6, tetapi hasil kalinya kelipatan 6 (kombinasi genap $\{2, 4\}$ dan kelipatan 3 $\{3\}$): $(2, 3), (4, 3), (3, 2), (3, 4)$ (4 pasangan).
   Total untuk $X = 0$ adalah $6 + 5 + 4 = 15$ pasangan.
2. Cek nilai lainnya:
   - $X = 1$: $(1,1), (5,5) \implies 2$ pasangan.
   - $X = 2$: $(1,2), (2,1), (2,4), (4,2), (4,5), (5,4) \implies 6$ pasangan.
   - $X = 3$: $(1,3), (3,1), (3,3), (3,5), (5,3) \implies 5$ pasangan.
   - $X = 4$: $(1,4), (4,1), (2,2), (2,5), (5,2), (4,4) \implies 6$ pasangan.
   - $X = 5$: $(1,5), (5,1) \implies 2$ pasangan.
Nilai $x$ dengan prainang terbesar adalah $x = 0$ sebanyak 15 pasangan.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 54. [hard] kelas12_tl-b04-a-hard-bt01-014
*orisinal | C5 | 4 langkah | jenis: analisis fungsi variabel acak kuadratik*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Misalkan $(a, b)$ menyatakan pasangan mata dadu yang muncul dengan $a, b \in \{1, 2, 3, 4, 5, 6\}$. Didefinisikan suatu variabel acak $V$ sebagai $V = (a - 3)^2 + (b - 3)^2$. Banyaknya elemen dalam ruang sampel yang memetakan ke nilai variabel acak $V$ berupa bilangan ganjil adalah ....

- A. 12  
  <sub>Salah: Siswa hanya menghitung kemungkinan suku pertama ganjil dan kedua genap tanpa menukar perannya serta salah mengeliminasi titik pusat.</sub>
- B. 20  
  <sub>Salah: Siswa keliru menganggap pasangan kembar menghasilkan nilai ganjil.</sub>
- **C. 18** ✅  
  <sub>Benar: Nilai $(x - 3)^2$ bernilai ganjil jika $x \in \{2, 4, 6\}$ (3 nilai) dan genap jika $x \in \{1, 3, 5\}$ (3 nilai). Penjumlahan dua kuadrat bernilai ganjil jika satu suku genap dan satu suku ganjil, yaitu $(3 \times 3) + (3 \times 3) = 18$.</sub>
- D. 16  
  <sub>Salah: Siswa mengabaikan mata dadu 3 karena menganggap $(3-3)^2 = 0$ bukan bilangan bulat genap.</sub>

**Pembahasan:** Ruang sampel pelemparan dua dadu memiliki $n(S) = 6 \times 6 = 36$ elemen. Didefinisikan $V = (a - 3)^2 + (b - 3)^2$.
Perhatikan paritas dari $(x - 3)^2$ untuk $x \in \{1, 2, 3, 4, 5, 6\}$:
- Jika $x \in \{1, 3, 5\}$, maka $(x - 3)^2 \in \{4, 0, 4\}$ yang seluruhnya merupakan bilangan genap (ada 3 nilai).
- Jika $x \in \{2, 4, 6\}$, maka $(x - 3)^2 \in \{1, 1, 9\}$ yang seluruhnya merupakan bilangan ganjil (ada 3 nilai).

Nilai $V$ bernilai ganjil jika dan hanya jika salah satu suku bernilai genap dan suku lainnya bernilai ganjil:
1. Suku $(a - 3)^2$ genap dan $(b - 3)^2$ ganjil: terdapat $3 \times 3 = 9$ pasangan.
2. Suku $(a - 3)^2$ ganjil dan $(b - 3)^2$ genap: terdapat $3 \times 3 = 9$ pasangan.

Total banyaknya elemen ruang sampel yang menghasilkan nilai $V$ ganjil adalah $9 + 9 = 18$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 55. [hard] kelas12_tl-b04-a-hard-bt01-015
*orisinal | C6 | 5 langkah | jenis: perancangan komposisi kantong variabel acak*

Sebuah kantong berisi sejumlah kelereng merah dan kelereng biru dengan jumlah total 10 kelereng. Dari dalam kantong tersebut diambil 6 kelereng sekaligus secara acak. Misalkan $m$ menyatakan banyaknya kelereng merah dan $k$ menyatakan banyaknya kelereng biru di dalam kantong. Didefinisikan variabel acak $X$ sebagai banyaknya kelereng merah yang terambil. Jika himpunan semua nilai yang mungkin dari $X$ memiliki tepat 4 anggota, maka selisih mutlak $|m - k|$ adalah ....

- A. 6  
  <sub>Salah: Siswa menguji m = 2 dan k = 8 yang menghasilkan himpunan nilai {0, 1, 2} sebanyak 3 anggota.</sub>
- **B. 4** ✅  
  <sub>Benar: Himpunan nilai X beranggotakan tepat 4 jika nilai minimum dan maksimum memenuhi selisih 3. Hal ini terjadi saat m = 3 (nilai {0, 1, 2, 3}) atau m = 7 (nilai {3, 4, 5, 6}), sehingga selisih |m - k| = |3 - 7| = 4.</sub>
- C. 2  
  <sub>Salah: Siswa menguji m = 4 dan k = 6 yang menghasilkan himpunan nilai {0, 1, 2, 3, 4} sebanyak 5 anggota.</sub>
- D. 8  
  <sub>Salah: Siswa menguji kasus ekstrem m = 1 dan k = 9 yang menghasilkan 2 anggota.</sub>

**Pembahasan:** Diketahui total kelereng $m + k = 10$ dan diambil $r = 6$ kelereng.
Nilai minimum dari variabel acak $X$ (banyak kelereng merah terambil) adalah $\max(0, 6 - k) = \max(0, m - 4)$.
Nilai maksimum dari $X$ adalah $\min(6, m)$.
Banyak anggota himpunan nilai $X$ adalah $(\text{maks} - \text{min} + 1)$. Karena diinginkan tepat 4 anggota, maka $\text{maks} - \text{min} = 3$.

Kita uji nilai $m$ yang mungkin ($0 \le m \le 10$):
- Jika $m = 3$, maka $k = 7$. Nilai minimum $X = \max(0, -1) = 0$, nilai maksimum $X = \min(6, 3) = 3$. Himpunan nilai $X = \{0, 1, 2, 3\}$ (4 anggota). Selisih $|m - k| = |3 - 7| = 4$.
- Jika $m = 7$, maka $k = 3$. Nilai minimum $X = \max(0, 3) = 3$, nilai maksimum $X = \min(6, 7) = 6$. Himpunan nilai $X = \{3, 4, 5, 6\}$ (4 anggota). Selisih $|m - k| = |7 - 3| = 4$.
- Untuk $m = 4, 5, 6$, himpunan nilai memiliki 5 anggota.
- Untuk $m = 2, 8$, himpunan nilai memiliki 3 anggota.

Dengan demikian, nilai $|m - k| = 4$.
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 56. [hard] kelas12_tl-b04-a-hard-bt01-016
*orisinal | C5 | 4 langkah | jenis: analisis prainang variabel acak determinan*

Dua buah dadu seimbang bersisi enam dilempar bersamaan satu kali. Pasangan mata dadu yang muncul dinyatakan sebagai $(a, b)$ dengan $a, b \in \{1, 2, 3, 4, 5, 6\}$. Didefinisikan matriks $M = \begin{pmatrix} a & 2 \\ b & 3 \end{pmatrix}$. Variabel acak $D$ menyatakan determinan dari matriks $M$. Banyaknya elemen ruang sampel yang memetakan ke nilai variabel acak $D$ sedemikian sehingga $|D| \le 2$ adalah ....

- **A. 9** ✅  
  <sub>Benar: Determinan D = 3a - 2b. Syarat |3a - 2b| <= 2 dipenuhi oleh pasangan (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (3, 5), (4, 5), dan (4, 6), total ada 9 elemen.</sub>
- B. 7  
  <sub>Salah: Siswa tidak teliti saat menghitung batas pertidaksamaan untuk nilai a = 2 sehingga melewatkan pasangan (2, 2) dan (2, 4).</sub>
- C. 8  
  <sub>Salah: Siswa melewatkan pasangan (1, 1) karena menganggap determinan harus bernilai 0.</sub>
- D. 11  
  <sub>Salah: Siswa salah memperluas rentang pertidaksamaan menjadi |3a - 2b| <= 3.</sub>

**Pembahasan:** Determinan dari matriks $M$ adalah $D = \det(M) = 3a - 2b$.
Syarat $|D| \le 2$ ekuivalen dengan $-2 \le 3a - 2b \le 2$, atau dapat ditulis sebagai:
$3a - 2 \le 2b \le 3a + 2$.

Kita uji setiap nilai $a \in \{1, 2, 3, 4, 5, 6\}$:
1. $a = 1$: $1 \le 2b \le 5 \implies b \in \{1, 2\}$ (2 pasangan: $(1, 1), (1, 2)$)
2. $a = 2$: $4 \le 2b \le 8 \implies b \in \{2, 3, 4\}$ (3 pasangan: $(2, 2), (2, 3), (2, 4)$)
3. $a = 3$: $7 \le 2b \le 11 \implies b \in \{4, 5\}$ (2 pasangan: $(3, 4), (3, 5)$)
4. $a = 4$: $10 \le 2b \le 14 \implies b \in \{5, 6\}$ (2 pasangan: $(4, 5), (4, 6)$)
5. $a = 5$: $13 \le 2b \le 17 \implies 2b \ge 13$. Karena nilai maksimal $b = 6$ ($2b = 12$), tidak ada nilai $b$ yang memenuhi (0 pasangan).
6. $a = 6$: $16 \le 2b \le 20 \implies$ tidak ada nilai $b$ yang memenuhi (0 pasangan).

Total banyaknya elemen ruang sampel yang memenuhi adalah $2 + 3 + 2 + 2 = 9$.
**Acuan:** siswa — siswa hal.243

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 57. [hard] kelas12_tl-b04-a-hard-bt01-017
*orisinal | C5 | 5 langkah | jenis: evaluasi kesetaraan distribusi variabel acak*

Sebuah percobaan acak melempar 4 keping uang logam seimbang secara bersamaan. Setiap keping memiliki sisi Angka ($A$) dan Gambar ($G$). Hasil lemparan dinyatakan sebagai barisan 4 huruf berurutan, misalnya $AGGA$.
Didefinisikan dua variabel acak:
- $X$: banyaknya sisi Angka ($A$) yang muncul.
- $Y$: banyaknya pergantian sisi yang terjadi antara dua keping yang bersebelahan (contoh: pada hasil $AGGA$, terjadi pergantian dari $A$ ke $G$ dan dari $G$ ke $A$, sehingga $Y = 2$).

Perhatikan pernyataan-pernyataan berikut:
(1) Nilai minimum yang mungkin dari variabel acak $Y$ adalah 0.
(2) Nilai maksimum yang mungkin dari variabel acak $Y$ adalah 3.
(3) Banyaknya elemen dalam ruang sampel yang memetakan ke nilai $Y = 1$ adalah 6.
(4) Himpunan semua nilai yang mungkin dari $(X - Y)$ adalah $\{0, 1, 2, 3, 4\}$.

Pernyataan yang bernilai benar adalah ....

- A. (2) dan (4) saja  
  <sub>Salah: Siswa mengira selisih X - Y selalu non-negatif dan mengabaikan pernyataan (1).</sub>
- B. (1), (3), dan (4)  
  <sub>Salah: Siswa mengira X selalu lebih besar atau sama dengan Y sehingga menganggap (4) benar.</sub>
- C. (1) dan (2) saja  
  <sub>Salah: Siswa keliru menghitung prainang Y = 1 dan menduga banyaknya bukan 6.</sub>
- **D. (1), (2), dan (3)** ✅  
  <sub>Benar: Pernyataan (1), (2), dan (3) benar, sedangkan (4) salah karena hasil AGAG menghasilkan X = 2 dan Y = 3 sehingga X - Y = -1 (memuat bilangan negatif).</sub>

**Pembahasan:** Ruang sampel pelemparan 4 uang logam memiliki $2^4 = 16$ elemen. Ada 3 celah posisi pergantian sisi (antara koin 1-2, 2-3, 3-4).

Evaluasi pernyataan:
- Pernyataan (1): Nilai $Y = 0$ terjadi jika tidak ada pergantian sisi sama sekali, yaitu pada hasil $AAAA$ dan $GGGG$. Jadi nilai minimum $Y$ adalah 0. (Pernyataan (1) BENAR)
- Pernyataan (2): Pergantian sisi dapat terjadi di ketiga posisi celah, yaitu pada hasil $AGAG$ dan $GAGA$ ($Y = 3$). Jadi nilai maksimum $Y$ adalah 3. (Pernyataan (2) BENAR)
- Pernyataan (3): Nilai $Y = 1$ berarti hanya terjadi 1 kali pergantian:
  * Pergantian di celah 1: $AGGG, GAAA$ (2 hasil)
  * Pergantian di celah 2: $AAGG, GGAA$ (2 hasil)
  * Pergantian di celah 3: $AAAG, GGGA$ (2 hasil)
  Total elemen dengan $Y = 1$ adalah $2 + 2 + 2 = 6$. (Pernyataan (3) BENAR)
- Pernyataan (4): Perhatikan elemen $AGAG$. Pada hasil ini, banyak angka $X = 2$ dan banyak pergantian sisi $Y = 3$. Nilai $X - Y = 2 - 3 = -1$. Karena himpunan nilai memuat $-1$, maka himpunan nilainya bukan $\{0, 1, 2, 3, 4\}$. (Pernyataan (4) SALAH)

Jadi, pernyataan yang bernilai benar adalah (1), (2), dan (3).
**Acuan:** siswa — siswa hal.240

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
