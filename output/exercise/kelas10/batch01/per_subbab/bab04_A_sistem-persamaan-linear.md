# Lembar koreksi — kelas10 SMA10-B4 subbab A: Sistem Persamaan Linear

52 soal | easy 20, medium 20, hard 12 | variasi 21, orisinal 31
> **Kapasitas kurang (hard): 12 dari kuota 20** — Kapasitas aktual sekitar 12-14 soal; sisanya hampir pasti kembar medium (hitung SPLTV, tafsir banyak solusi) atau di luar materi subbab A.

> Turunan otomatis. Koreksi dilakukan di file kerja `<KODE>_<level>.json`, lalu export diulang.

---

### 1. [easy] kelas10-b04-a-easy-bt01-001
*variasi (angka) | C2 | 1 langkah | jenis: menyusun model*

Rani memiliki tiga jenis pita: pita merah, pita kuning, dan pita biru. Rani menyambung 4 pita merah, 3 pita kuning, dan 2 pita biru dan panjangnya 640 cm. Rani menyambung 2 pita merah, 5 pita kuning, dan 3 pita biru dan panjangnya 710 cm. Rani juga mengamati bahwa 3 pita merah sama panjang dengan pita biru.

Jika $m$, $k$, dan $b$ berturut-turut menyatakan panjang satu pita merah, kuning, dan biru (dalam cm), persamaan yang menyatakan pengamatan ketiga Rani adalah ....

- **A. $3m = b$** ✅  
  <sub>Benar: tiga pita merah panjangnya $3m$ dan nilainya sama dengan panjang satu pita biru, yaitu $b$</sub>
- B. $3m + b = 0$  
  <sub>Salah: kata sama panjang diterjemahkan menjadi jumlah bernilai nol</sub>
- C. $3 + m = b$  
  <sub>Salah: banyak pita ditambahkan, bukan dikalikan dengan panjang pita</sub>
- D. $m = 3b$  
  <sub>Salah: peubah tertukar: yang dikalikan 3 justru pita biru</sub>

**Pembahasan:** 3 pita merah panjangnya $3m$. Panjang itu sama dengan pita biru $b$, sehingga $3m = b$.
**Acuan:** pretest — kelas10-b04-p0132-latihan-4-1-1f

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 2. [easy] kelas10-b04-a-easy-bt01-002
*variasi (angka) | C2 | 2 langkah | jenis: menyusun model*

Pak Rudi membeli tiga jenis kain: katun, sutra, dan linen. Pembelian pertama: 2 meter katun, 4 meter sutra, dan 3 meter linen seharga Rp410.000,00. Pembelian kedua: 5 meter katun, 1 meter sutra, dan 2 meter linen seharga Rp375.000,00.

Jika $a$, $s$, dan $l$ berturut-turut menyatakan harga per meter katun, sutra, dan linen (dalam rupiah), persamaan untuk pembelian pertama adalah ....

- A. $2a + 3s + 4l = 410.000$  
  <sub>Salah: koefisien sutra dan linen tertukar</sub>
- B. $a + s + l = 410.000$  
  <sub>Salah: banyak meter tiap kain diabaikan</sub>
- C. $2a + 4s + 3l = 375.000$  
  <sub>Salah: memakai total pembelian kedua</sub>
- **D. $2a + 4s + 3l = 410.000$** ✅  
  <sub>Benar: banyak meter menjadi koefisien harga per meter dan jumlahnya sama dengan total pembelian pertama</sub>

**Pembahasan:** Pembelian pertama: $2a + 4s + 3l = 410.000$.
**Acuan:** pretest — kelas10-b04-p0132-latihan-4-1-1f

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 3. [easy] kelas10-b04-a-easy-bt01-003
*variasi (angka) | C2 | 2 langkah | jenis: menentukan banyak solusi*

Rina membeli roti dalam tiga kemasan: kecil, sedang, dan besar. Jika Rina membeli 2 kemasan kecil, 3 kemasan sedang, dan 5 kemasan besar, ia mendapat 60 potong roti. Jika Rina membeli 2 kemasan kecil, 1 kemasan sedang, dan 3 kemasan besar, ia mendapat 36 potong roti. Jika Rina membeli 2 kemasan sedang dan 2 kemasan besar, ia mendapat 30 potong roti.

Banyaknya solusi sistem persamaan linear yang sesuai dengan keadaan tersebut adalah ....

- A. Banyak solusi  
  <sub>Salah: mengira dua persamaan yang bersesuaian selalu identik</sub>
- B. Tepat satu solusi  
  <sub>Salah: mengira tiga persamaan dengan tiga variabel selalu menghasilkan satu solusi</sub>
- **C. Tidak ada solusi** ✅  
  <sub>Benar: persamaan pertama dikurangi kedua memberi $2s + 2b = 24$, sedangkan persamaan ketiga menyatakan $2s + 2b = 30$; keduanya bertentangan</sub>
- D. Tepat tiga solusi  
  <sub>Salah: mengira banyak solusi sama dengan banyak variabel</sub>

**Pembahasan:** Misalkan $k$, $s$, $b$ banyak potong tiap kemasan. (1)-(2): $2s + 2b = 24$. Persamaan ketiga: $2s + 2b = 30$. Pernyataan $24 = 30$ tidak pernah benar, sehingga tidak ada solusi.
**Acuan:** pretest — kelas10-b04-p0133-latihan-4-1-2d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 4. [easy] kelas10-b04-a-easy-bt01-004
*variasi (angka) | C2 | 1 langkah | jenis: menyusun model*

Bagas membeli minuman dalam tiga ukuran gelas: kecil, sedang, dan besar. Pembelian pertama: 4 gelas kecil, 1 gelas sedang, dan 2 gelas besar berisi total 3.100 ml. Pembelian kedua: 1 gelas kecil, 3 gelas sedang, dan 2 gelas besar berisi total 2.900 ml. Pembelian ketiga: 2 gelas sedang dan 5 gelas besar berisi total 2.600 ml.

Jika $x$, $y$, dan $z$ berturut-turut menyatakan volume satu gelas kecil, sedang, dan besar (dalam ml), persamaan untuk pembelian ketiga adalah ....

- A. $5y + 2z = 2.600$  
  <sub>Salah: koefisien gelas sedang dan besar tertukar</sub>
- B. $2x + 5z = 2.600$  
  <sub>Salah: gelas sedang ditulis dengan peubah gelas kecil</sub>
- **C. $2y + 5z = 2.600$** ✅  
  <sub>Benar: pembelian ketiga hanya memuat gelas sedang dan besar sehingga tidak memuat $x$</sub>
- D. $2y + 5z = 2.900$  
  <sub>Salah: memakai total pembelian kedua</sub>

**Pembahasan:** 2 gelas sedang: $2y$; 5 gelas besar: $5z$; totalnya 2.600 ml, sehingga $2y + 5z = 2.600$.
**Acuan:** pretest — kelas10-b04-p0133-latihan-4-1-2d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 5. [easy] kelas10-b04-a-easy-bt01-005
*variasi (angka) | C2 | 2 langkah | jenis: menentukan nilai variabel*

Sebuah toko menjual paket alat gambar. Paket A seharga Rp24.000,00 berisi tiga buku gambar dan dua spidol. Paket B berisi sebuah buku gambar dan dua spidol dihargai Rp12.000,00.

Harga sebuah buku gambar adalah ....

- **A. Rp6.000,00** ✅  
  <sub>Benar: mengurangkan persamaan paket A dan B menghapus spidol sehingga $2g = 12.000$</sub>
- B. Rp4.000,00  
  <sub>Salah: selisih harga paket dibagi 3, padahal selisih buku hanya 2</sub>
- C. Rp12.000,00  
  <sub>Salah: selisih harga paket tidak dibagi 2</sub>
- D. Rp3.000,00  
  <sub>Salah: yang dicari tertukar: itu harga sebuah spidol</sub>

**Pembahasan:** Misalkan $g$ buku gambar dan $s$ spidol: $3g + 2s = 24.000$ dan $g + 2s = 12.000$. Dikurangkan: $2g = 12.000$, $g = 6.000$.
**Acuan:** siswa — siswa hal.126 Ayo Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 6. [easy] kelas10-b04-a-easy-bt01-006
*variasi (angka) | C2 | 2 langkah | jenis: menentukan nilai variabel*

Koperasi sekolah menjual paket tulis. Paket A seharga Rp33.000,00 berisi enam pulpen dan tiga buku. Paket B berisi dua pulpen dan tiga buku dihargai Rp17.000,00.

Harga sebuah pulpen adalah ....

- A. Rp3.000,00  
  <sub>Salah: yang dicari tertukar: itu harga sebuah buku</sub>
- B. Rp16.000,00  
  <sub>Salah: selisih harga tidak dibagi 4</sub>
- **C. Rp4.000,00** ✅  
  <sub>Benar: mengurangkan kedua persamaan menghapus buku sehingga $4p = 16.000$</sub>
- D. Rp8.000,00  
  <sub>Salah: selisih harga dibagi 2, padahal selisih pulpen adalah 4</sub>

**Pembahasan:** $6p + 3b = 33.000$ dan $2p + 3b = 17.000$. Dikurangkan: $4p = 16.000$, sehingga $p = 4.000$.
**Acuan:** siswa — siswa hal.126 Ayo Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 7. [easy] kelas10-b04-a-easy-bt01-007
*variasi (angka) | C2 | 2 langkah | jenis: menentukan banyak solusi*

Pak Anton membeli tiga jenis sayur. Kalau ia membeli 4 kg wortel, 3 kg kentang, dan 1 kg tomat, ia harus membayar Rp84.000,00. Jika Pak Anton membeli 3 kg wortel, 2 kg kentang, dan 1 kg tomat, ia harus membayar Rp69.000,00. Jika Pak Anton membeli 2 kg wortel dan 2 kg kentang, ia harus membayar Rp30.000,00.

Banyaknya solusi sistem persamaan linear yang sesuai dengan keadaan tersebut adalah ....

- **A. Banyak solusi** ✅  
  <sub>Benar: persamaan pertama dikurangi kedua menghasilkan $w + k = 15.000$, yang setara dengan persamaan ketiga ($2w + 2k = 30.000$)</sub>
- B. Tidak ada solusi  
  <sub>Salah: mengira kedua persamaan berbeda sehingga bertentangan</sub>
- C. Tepat satu solusi  
  <sub>Salah: mengira tiga persamaan tiga variabel pasti memberi satu solusi</sub>
- D. Tepat tiga solusi  
  <sub>Salah: mengira banyak solusi sama dengan banyak variabel</sub>

**Pembahasan:** (1)-(2): $w + k = 15.000$. Persamaan ketiga $2w + 2k = 30.000$ adalah dua kali hasil itu, sehingga hanya ada dua persamaan yang bebas untuk tiga variabel: banyak solusi.
**Acuan:** siswa — siswa hal.133 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 8. [easy] kelas10-b04-a-easy-bt01-008
*variasi (angka) | C2 | 2 langkah | jenis: melakukan eliminasi*

Bu Dewi membeli tiga jenis ikan. Kalau ia membeli 6 kg bandeng, 2 kg lele, dan 1 kg nila, ia harus membayar Rp210.000,00. Jika Bu Dewi membeli 4 kg bandeng, 2 kg lele, dan 1 kg nila, ia harus membayar Rp170.000,00. Jika Bu Dewi membeli 1 kg lele dan 1 kg nila, ia harus membayar Rp60.000,00.

Jika $b$, $l$, dan $n$ berturut-turut menyatakan harga per kg bandeng, lele, dan nila (dalam rupiah), persamaan yang diperoleh dengan mengurangkan persamaan pertama oleh persamaan kedua adalah ....

- **A. $2b = 40.000$** ✅  
  <sub>Benar: suku $l$ dan $n$ identik pada kedua persamaan sehingga hilang, tersisa $(6-4)b = 210.000 - 170.000$</sub>
- B. $10b + 4l + 2n = 380.000$  
  <sub>Salah: kedua persamaan dijumlahkan, bukan dikurangkan</sub>
- C. $2b = 380.000$  
  <sub>Salah: ruas kanan dijumlahkan padahal ruas kiri dikurangkan</sub>
- D. $b = 40.000$  
  <sub>Salah: selisih koefisien 6 - 4 = 2 diabaikan</sub>

**Pembahasan:** (1): $6b + 2l + n = 210.000$; (2): $4b + 2l + n = 170.000$. (1)-(2): $2b = 40.000$.
**Acuan:** siswa — siswa hal.133 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 9. [easy] kelas10-b04-a-easy-bt01-009
*variasi (konteks) | C2 | 1 langkah | jenis: mengenali bentuk sistem*

Perhatikan sistem persamaan berikut.

$2x + y - z = 5$

$x + y^2 + 2z = 9$

$3x - z = 4$

Apakah sistem persamaan di atas termasuk sistem persamaan linear? Pernyataan yang benar adalah ....

- A. Ya, karena sistem itu terdiri atas tiga persamaan  
  <sub>Salah: banyak persamaan dianggap menentukan kelinearan</sub>
- B. Bukan, karena persamaan ketiga tidak memuat variabel $y$  
  <sub>Salah: mengira setiap persamaan wajib memuat semua variabel</sub>
- C. Ya, karena sistem itu memuat tiga variabel  
  <sub>Salah: banyak variabel dianggap menentukan kelinearan</sub>
- **D. Bukan, karena ada variabel $y$ yang berpangkat dua** ✅  
  <sub>Benar: sistem persamaan linear hanya memuat variabel berpangkat satu, sedangkan persamaan kedua memuat $y^2$</sub>

**Pembahasan:** Persamaan kedua memuat $y^2$ (pangkat dua), sehingga sistem ini bukan sistem persamaan linear.
**Acuan:** siswa — siswa hal.133 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 10. [easy] kelas10-b04-a-easy-bt01-010
*variasi (konteks) | C2 | 1 langkah | jenis: mengenali bentuk sistem*

Manakah pasangan persamaan berikut yang merupakan sistem persamaan linear dua variabel?

- A. $x^2 + y = 5$ dan $x - y = 1$  
  <sub>Salah: tidak memeriksa pangkat: $x^2$ berpangkat dua</sub>
- **B. $x + 2y = 5$ dan $3x - y = 1$** ✅  
  <sub>Benar: kedua persamaan hanya memuat variabel berpangkat satu</sub>
- C. $x + y^2 = 4$ dan $2x - y = 3$  
  <sub>Salah: tidak memeriksa pangkat: $y^2$ berpangkat dua</sub>
- D. $\sqrt{x} + y = 3$ dan $x - y = 2$  
  <sub>Salah: mengira variabel di bawah akar tetap berpangkat satu</sub>

**Pembahasan:** Sistem persamaan linear hanya memuat variabel berpangkat satu. Hanya pasangan $x + 2y = 5$ dan $3x - y = 1$ yang memenuhi.
**Acuan:** siswa — siswa hal.132 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 11. [easy] kelas10-b04-a-easy-bt01-011
*variasi (angka) | C2 | 2 langkah | jenis: memeriksa penyelesaian*

Tika menimbang tiga jenis buah: apel, jeruk, dan mangga. Pada penimbangan pertama, 3 apel, 2 jeruk, dan 1 mangga beratnya 1.350 g. Penimbangan kedua, 1 apel, 3 jeruk, dan 2 mangga beratnya 1.250 g. Penimbangan ketiga, 2 apel dan 1 mangga beratnya 700 g.

Jika $a$, $j$, dan $m$ berturut-turut menyatakan berat satu apel, jeruk, dan mangga (dalam gram), nilai yang memenuhi ketiga penimbangan adalah ....

- A. $a = 350$, $j = 200$, $m = 150$  
  <sub>Salah: hanya memenuhi persamaan kedua, persamaan lain tidak diuji</sub>
- B. $a = 200$, $j = 250$, $m = 300$  
  <sub>Salah: hanya memenuhi persamaan ketiga, persamaan lain tidak diuji</sub>
- **C. $a = 250$, $j = 200$, $m = 200$** ✅  
  <sub>Benar: penyelesaian harus memenuhi semua persamaan: $3a+2j+m=1.350$, $a+3j+2m=1.250$, dan $2a+m=700$</sub>
- D. $a = 250$, $j = 250$, $m = 100$  
  <sub>Salah: hanya memenuhi persamaan pertama, persamaan lain tidak diuji</sub>

**Pembahasan:** Uji $a=250$, $j=200$, $m=200$: $750+400+200=1.350$; $250+600+400=1.250$; $500+200=700$. Semua benar.
**Acuan:** siswa — siswa hal.126 Eksplorasi 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 12. [easy] kelas10-b04-a-easy-bt01-012
*orisinal | C1 | 1 langkah | jenis: mengenali konsep*

Penyelesaian sebuah sistem persamaan linear adalah ....

- A. banyaknya persamaan yang membentuk sistem itu  
  <sub>Salah: mengira penyelesaian adalah banyak persamaan</sub>
- B. nilai-nilai variabel yang memenuhi sebagian persamaan dalam sistem itu  
  <sub>Salah: mengira cukup memenuhi sebagian persamaan</sub>
- C. jumlah semua koefisien variabel pada persamaan dalam sistem itu  
  <sub>Salah: mengira penyelesaian berupa koefisien</sub>
- **D. nilai-nilai variabel yang memenuhi semua persamaan dalam sistem itu** ✅  
  <sub>Benar: definisi di buku: penyelesaian adalah nilai yang memenuhi semua persamaan</sub>

**Pembahasan:** Penyelesaian sistem persamaan linear adalah nilai variabel yang membuat semua persamaan bernilai benar.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 13. [easy] kelas10-b04-a-easy-bt01-013
*orisinal | C2 | 2 langkah | jenis: menghubungkan grafik dan solusi*

Perhatikan sistem persamaan linear dua variabel: $x + y = 4$ dan $x + y = 9$.

Jika kedua persamaan digambar pada bidang koordinat, grafiknya berupa dua garis yang ....

- A. berimpit  
  <sub>Salah: mengira persamaan yang mirip pasti menggambar garis yang sama</sub>
- **B. sejajar** ✅  
  <sub>Benar: kedua persamaan bila dikurangkan menghasilkan $0 = -5$ yang tidak pernah benar, sehingga tidak ada titik potong</sub>
- C. berpotongan di dua titik  
  <sub>Salah: mengira ada dua solusi karena ada dua persamaan</sub>
- D. berpotongan di satu titik  
  <sub>Salah: mengira setiap sistem dua variabel punya satu solusi</sub>

**Pembahasan:** $(x+y)-(x+y) = 4 - 9$ memberi $0 = -5$, tidak pernah benar. Tidak ada solusi, grafiknya dua garis sejajar.
**Acuan:** siswa — siswa hal.130

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 14. [easy] kelas10-b04-a-easy-bt01-014
*orisinal | C2 | 1 langkah | jenis: menafsirkan hasil eliminasi*

Pada penyelesaian suatu sistem persamaan linear dua variabel, setelah proses eliminasi diperoleh pernyataan $0 = 7$.

Kesimpulan yang tepat mengenai sistem persamaan tersebut adalah ....

- A. sistem memiliki tepat satu solusi, yaitu $x = 0$  
  <sub>Salah: mengambil angka 0 pada hasil sebagai nilai variabel</sub>
- B. sistem memiliki banyak solusi karena ruas kiri bernilai 0  
  <sub>Salah: mengira nilai 0 menandakan banyak solusi</sub>
- **C. sistem tidak memiliki solusi karena pernyataan itu tidak pernah benar** ✅  
  <sub>Benar: pernyataan yang tidak pernah benar menandakan tidak ada nilai variabel yang memenuhi semua persamaan</sub>
- D. sistem memiliki solusi $y = 7$ dan $x = 0$  
  <sub>Salah: membaca hasil eliminasi sebagai pasangan solusi</sub>

**Pembahasan:** Pernyataan $0 = 7$ salah untuk setiap nilai variabel, sehingga sistem tidak memiliki solusi.
**Acuan:** siswa — siswa hal.131

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 15. [easy] kelas10-b04-a-easy-bt01-015
*orisinal | C2 | 2 langkah | jenis: menentukan banyak solusi*

Perhatikan sistem persamaan linear dua variabel berikut: $2x + 4y = 6$ dan $x + 2y = 3$.

Banyaknya solusi sistem persamaan tersebut adalah ....

- A. tidak ada solusi  
  <sub>Salah: mengira persamaan yang koefisiennya berbeda saling bertentangan</sub>
- **B. banyak solusi** ✅  
  <sub>Benar: persamaan pertama merupakan dua kali persamaan kedua, sehingga eliminasi menghasilkan $0 = 0$ dan grafiknya berimpit</sub>
- C. tepat dua solusi  
  <sub>Salah: mengira banyak solusi sama dengan banyak persamaan</sub>
- D. tepat satu solusi  
  <sub>Salah: mengira dua persamaan selalu berpotongan di satu titik</sub>

**Pembahasan:** Persamaan kedua dikalikan 2 menjadi $2x + 4y = 6$, sama dengan persamaan pertama. Eliminasi memberi $0 = 0$, sehingga banyak solusi.
**Acuan:** siswa — siswa hal.130

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 16. [easy] kelas10-b04-a-easy-bt01-016
*orisinal | C2 | 2 langkah | jenis: menentukan nilai variabel*

Diketahui sistem persamaan linear $2x + y = 11$ dan $x - y = 1$.

Nilai $y$ yang memenuhi sistem persamaan tersebut adalah ....

- A. $y = 4$  
  <sub>Salah: memberikan nilai $x$ sebagai nilai $y$</sub>
- B. $y = 9$  
  <sub>Salah: mengurangkan 2 dari 11 tanpa memakai nilai $x$</sub>
- C. $y = 5$  
  <sub>Salah: salah tanda saat substitusi: $y = x + 1$</sub>
- **D. $y = 3$** ✅  
  <sub>Benar: dijumlahkan: $3x = 12$, $x = 4$; lalu $y = x - 1 = 3$</sub>

**Pembahasan:** Jumlahkan: $3x = 12$ sehingga $x = 4$. Dari $x - y = 1$ diperoleh $y = 4 - 1 = 3$. Cek: $2(4)+3=11$.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 17. [easy] kelas10-b04-a-easy-bt01-017
*orisinal | C2 | 1 langkah | jenis: memilih langkah penyelesaian*

Diketahui sistem persamaan linear tiga variabel:

$x + 2y + z = 9$ ... (1)

$2x - y + z = 7$ ... (2)

$x + z = 5$ ... (3)

Persamaan (3) tidak memuat $y$. Agar persamaan (1) dan (2) menghasilkan persamaan dua variabel yang dapat digabung dengan persamaan (3), variabel yang dieliminasi dari persamaan (1) dan (2) adalah ....

- A. $x$ dan $y$ sekaligus  
  <sub>Salah: mengira dua variabel dapat dihapus sekaligus dari dua persamaan</sub>
- **B. $y$** ✅  
  <sub>Benar: hasil eliminasi $y$ memuat $x$ dan $z$, sama seperti persamaan (3), sehingga membentuk sistem dua variabel</sub>
- C. $z$  
  <sub>Salah: hasil eliminasi $z$ memuat $x$ dan $y$, tidak dapat digabung dengan (3) menjadi dua variabel</sub>
- D. $x$  
  <sub>Salah: hasil eliminasi $x$ memuat $y$ dan $z$, tidak dapat digabung dengan (3) menjadi dua variabel</sub>

**Pembahasan:** Persamaan (3) hanya memuat $x$ dan $z$. Eliminasi $y$ dari (1) dan (2) menghasilkan persamaan dalam $x$ dan $z$, lalu digabung dengan (3).
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 18. [easy] kelas10-b04-a-easy-bt01-018
*orisinal | C1 | 1 langkah | jenis: mengenali bentuk sistem*

Perhatikan sistem persamaan linear berikut.

$x + y = 5$

$y + z = 7$

$x + z = 6$

Sistem persamaan tersebut merupakan sistem persamaan linear dengan ....

- A. satu variabel  
  <sub>Salah: mengira sistem pasti bervariabel tunggal karena tiap persamaan bersifat sederhana</sub>
- **B. tiga variabel** ✅  
  <sub>Benar: variabel yang muncul pada sistem adalah $x$, $y$, dan $z$</sub>
- C. dua variabel  
  <sub>Salah: menghitung banyak variabel pada satu persamaan, bukan pada seluruh sistem</sub>
- D. enam variabel  
  <sub>Salah: menjumlahkan variabel di tiap persamaan tanpa memperhatikan yang sama</sub>

**Pembahasan:** Seluruh sistem memuat $x$, $y$, dan $z$, sehingga disebut sistem persamaan linear tiga variabel.
**Acuan:** siswa — siswa hal.128

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 19. [easy] kelas10-b04-a-easy-bt01-019
*orisinal | C2 | 2 langkah | jenis: menyusun model*

Harga 3 kg jeruk dan 2 kg apel adalah Rp95.000,00, sedangkan harga 1 kg jeruk dan 4 kg apel adalah Rp85.000,00.

Jika $j$ menyatakan harga 1 kg jeruk dan $a$ harga 1 kg apel (dalam rupiah), sistem persamaan linear yang sesuai adalah ....

- **A. $3j + 2a = 95.000$ dan $j + 4a = 85.000$** ✅  
  <sub>Benar: banyak kilogram menjadi koefisien dan total harga menjadi ruas kanan</sub>
- B. $3j + 2a = 95.000$ dan $4j + a = 85.000$  
  <sub>Salah: koefisien tertukar pada persamaan kedua saja</sub>
- C. $2j + 3a = 95.000$ dan $4j + a = 85.000$  
  <sub>Salah: koefisien jeruk dan apel tertukar</sub>
- D. $3j + 2a = 85.000$ dan $j + 4a = 95.000$  
  <sub>Salah: total harga kedua persamaan tertukar</sub>

**Pembahasan:** Persamaan pertama: $3j + 2a = 95.000$. Persamaan kedua: $j + 4a = 85.000$.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 20. [easy] kelas10-b04-a-easy-bt01-020
*orisinal | C2 | 2 langkah | jenis: menentukan banyak solusi*

Diketahui sistem persamaan linear $x + y = 5$ dan $x - y = 1$.

Pernyataan yang tepat mengenai solusi sistem persamaan tersebut adalah ....

- A. tepat satu solusi, yaitu $(2, 3)$  
  <sub>Salah: nilai $x$ dan $y$ tertukar</sub>
- B. banyak solusi karena ada dua variabel  
  <sub>Salah: mengira dua variabel dengan dua persamaan berarti tak terhingga solusi</sub>
- C. tidak ada solusi karena jumlah dan selisihnya berbeda  
  <sub>Salah: mengira persamaan yang berbeda bentuk pasti bertentangan</sub>
- **D. tepat satu solusi, yaitu $(3, 2)$** ✅  
  <sub>Benar: dijumlahkan $2x = 6$, sehingga $x = 3$ dan $y = 2$; hanya pasangan ini yang memenuhi kedua persamaan</sub>

**Pembahasan:** $(x+y)+(x-y) = 5+1$ sehingga $2x = 6$, $x = 3$, $y = 2$. Satu pasangan nilai saja.
**Acuan:** siswa — siswa hal.132

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 21. [medium] kelas10-b04-a-medium-bt01-001
*variasi (angka) | C3 | 4 langkah | jenis: menentukan nilai ekspresi*

Luki menimbang tiga jenis buah: salak, belimbing, dan nanas. Penimbangan pertama: 4 salak, 2 belimbing, dan 1 nanas beratnya 1.350 g. Penimbangan kedua: 1 salak, 4 belimbing, dan 2 nanas beratnya 950 g. Penimbangan ketiga: 2 salak dan 4 nanas beratnya 1.100 g.

Berat total satu salak, satu belimbing, dan satu nanas adalah ....

- **A. 500 g** ✅  
  <sub>Benar: dengan $s$, $b$, $n$ berat satu salak, belimbing, nanas diperoleh $s = 250$, $b = 100$, $n = 150$ sehingga $s + b + n = 500$</sub>
- B. 650 g  
  <sub>Salah: berat nanas dihitung dua kali karena koefisien 2 pada persamaan kedua</sub>
- C. 400 g  
  <sub>Salah: hanya menjumlahkan salak dan nanas, lupa belimbing</sub>
- D. 350 g  
  <sub>Salah: hanya menjumlahkan salak dan belimbing, lupa nanas</sub>

**Pembahasan:** $4s+2b+n=1.350$, $s+4b+2n=950$, $2s+4n=1.100$. Dari persamaan ketiga $s = 550 - 2n$. Substitusi ke (1): $2b - 7n = -850$; ke (2): $4b + 0n = 400$, sehingga $b = 100$, lalu $n = 150$, $s = 250$. Jumlahnya $500$ g. Cek persamaan (1): $1.000+200+150=1.350$.
**Acuan:** siswa — siswa hal.126 Eksplorasi 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 22. [medium] kelas10-b04-a-medium-bt01-002
*variasi (angka) | C3 | 4 langkah | jenis: menentukan nilai variabel*

Raka menimbang tiga jenis sayur: wortel, kentang, dan brokoli. Penimbangan pertama: 3 wortel, 1 kentang, dan 4 brokoli beratnya 1.100 g. Penimbangan kedua: 1 wortel, 2 kentang, dan 3 brokoli beratnya 950 g. Penimbangan ketiga: 2 wortel dan 1 brokoli beratnya 400 g.

Berat sebuah kentang adalah ....

- A. 100 g  
  <sub>Salah: itu berat sebuah brokoli; peubah yang dicari tertukar</sub>
- B. 150 g  
  <sub>Salah: itu berat sebuah wortel; peubah yang dicari tertukar</sub>
- **C. 250 g** ✅  
  <sub>Benar: dengan $w$, $k$, $b$ berat wortel, kentang, brokoli diperoleh $w = 150$, $k = 250$, $b = 100$</sub>
- D. 350 g  
  <sub>Salah: menjumlahkan berat kentang dan brokoli</sub>

**Pembahasan:** $3w+k+4b=1.100$; $w+2k+3b=950$; $2w+b=400$. Dari (3) $b=400-2w$. Substitusi ke (1): $k=5w-500$. Substitusi ke (2): $w+10w-1.000+1.200-6w=950$, sehingga $5w=750$, $w=150$. Maka $k=250$ dan $b=100$.
**Acuan:** siswa — siswa hal.126 Eksplorasi 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 23. [medium] kelas10-b04-a-medium-bt01-003
*variasi (angka) | C3 | 4 langkah | jenis: menyusun model dan menyelesaikan*

Sebuah toko buku menjual paket alat belajar. Paket P berisi tiga buku tulis dan dua pensil seharga Rp17.000,00. Paket Q berisi dua buku tulis dan lima pensil dihargai Rp26.000,00.

Harga paket yang berisi empat buku tulis dan tiga pensil adalah ....

- **A. Rp24.000,00** ✅  
  <sub>Benar: harga sebuah buku tulis Rp3.000,00 dan sebuah pensil Rp4.000,00 sehingga $4(3.000) + 3(4.000) = 24.000$</sub>
- B. Rp28.000,00  
  <sub>Salah: menganggap semua tujuh barang berharga sama dengan pensil</sub>
- C. Rp25.000,00  
  <sub>Salah: harga buku tulis dan pensil tertukar saat menghitung</sub>
- D. Rp21.000,00  
  <sub>Salah: menganggap semua tujuh barang berharga sama dengan buku tulis</sub>

**Pembahasan:** $3b+2p=17.000$ dan $2b+5p=26.000$. Kalikan 2 dan 3: $6b+4p=34.000$ dan $6b+15p=78.000$, dikurangkan $11p=44.000$ sehingga $p=4.000$ dan $b=3.000$. Maka $4b+3p=12.000+12.000=24.000$.
**Acuan:** siswa — siswa hal.126 Ayo Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 24. [medium] kelas10-b04-a-medium-bt01-004
*variasi (angka) | C3 | 4 langkah | jenis: menyusun model dan menyelesaikan*

Koperasi sekolah menjual paket tulis. Paket hemat berisi empat pulpen dan sebuah penggaris seharga Rp14.500,00. Paket lengkap berisi dua pulpen dan tiga penggaris seharga Rp12.500,00. Dengan harga satuan yang sama, Intan membeli tiga pulpen dan dua penggaris.

Uang yang harus dibayar Intan adalah ....

- **A. Rp13.500,00** ✅  
  <sub>Benar: harga sebuah pulpen Rp3.100,00 dan sebuah penggaris Rp2.100,00 sehingga $3(3.100) + 2(2.100) = 13.500$</sub>
- B. Rp12.500,00  
  <sub>Salah: harga pulpen dan penggaris tertukar saat menghitung</sub>
- C. Rp5.200,00  
  <sub>Salah: hanya menghitung satu pulpen dan satu penggaris</sub>
- D. Rp27.000,00  
  <sub>Salah: menjumlahkan harga kedua paket</sub>

**Pembahasan:** $4p+g=14.500$ dan $2p+3g=12.500$. Dari persamaan pertama $g=14.500-4p$; substitusi: $2p+43.500-12p=12.500$ sehingga $p=3.100$ dan $g=2.100$. Maka $3p+2g=9.300+4.200=13.500$.
**Acuan:** siswa — siswa hal.126 Ayo Mengingat Kembali

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 25. [medium] kelas10-b04-a-medium-bt01-005
*variasi (angka) | C3 | 4 langkah | jenis: menentukan nilai variabel*

Dodi memiliki tiga jenis kabel: kabel A, kabel B, dan kabel C. Dodi menyambung 4 kabel A, 2 kabel B, dan 1 kabel C dan panjangnya 240 cm. Dodi menyambung sebuah kabel A, 5 kabel B, dan 2 kabel C dan panjangnya 390 cm. Dodi juga mengamati bahwa 1 kabel C sama panjang dengan 3 kabel A.

Panjang sebuah kabel B adalah ....

- **A. 50 cm** ✅  
  <sub>Benar: dengan $c = 3a$ diperoleh $7a + 2b = 240$ dan $7a + 5b = 390$, sehingga $b = 50$</sub>
- B. 60 cm  
  <sub>Salah: itu panjang kabel C; peubah yang dicari tertukar</sub>
- C. 150 cm  
  <sub>Salah: selisih $390 - 240 = 150$ tidak dibagi 3</sub>
- D. 20 cm  
  <sub>Salah: itu panjang kabel A; peubah yang dicari tertukar</sub>

**Pembahasan:** $c=3a$. Persamaan (1): $4a+2b+3a=240$ sehingga $7a+2b=240$. Persamaan (2): $a+5b+6a=390$ sehingga $7a+5b=390$. Dikurangkan: $3b=150$, $b=50$. Cek: $a=20$, $c=60$: $80+100+60=240$.
**Acuan:** pretest — kelas10-b04-p0132-latihan-4-1-1f

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 26. [medium] kelas10-b04-a-medium-bt01-006
*variasi (angka) | C3 | 4 langkah | jenis: menentukan nilai ekspresi*

Seorang pedagang menjual madu dalam tiga ukuran botol: kecil, sedang, dan besar. Jika Eka membeli 4 botol kecil, 2 botol sedang, dan 1 botol besar, ia mendapat madu sebanyak 1.400 ml. Jika Eka membeli 2 botol kecil, 1 botol sedang, dan 3 botol besar, ia mendapat 1.450 ml. Jika Eka membeli 3 botol kecil dan 2 botol besar, ia mendapat 1.200 ml.

Banyak madu yang diperoleh jika Eka membeli 2 botol kecil dan 1 botol besar adalah ....

- A. 850 ml  
  <sub>Salah: menambahkan satu botol sedang yang tidak ditanyakan</sub>
- B. 500 ml  
  <sub>Salah: hanya menjumlahkan satu botol kecil dan satu botol besar</sub>
- **C. 700 ml** ✅  
  <sub>Benar: volume botol kecil 200 ml dan botol besar 300 ml sehingga $2(200) + 300 = 700$</sub>
- D. 800 ml  
  <sub>Salah: volume botol kecil dan besar tertukar</sub>

**Pembahasan:** $4k+2s+b=1.400$; $2k+s+3b=1.450$; $3k+2b=1.200$. Kalikan (2) dengan 2: $4k+2s+6b=2.900$, dikurangi (1) menghasilkan $5b=1.500$ sehingga $b=300$. Dari (3): $3k=600$, $k=200$. Maka $2k+b=400+300=700$. Cek (2): $400+s+900=1.450$ memberi $s=150$.
**Acuan:** pretest — kelas10-b04-p0133-latihan-4-1-2d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 27. [medium] kelas10-b04-a-medium-bt01-007
*variasi (angka) | C4 | 3 langkah | jenis: menentukan nilai parameter*

Toko teh Pak Gito menjual campuran tiga jenis teh. Campuran pertama: 5 kg teh A, 1 kg teh B, dan 3 kg teh C dihargai Rp106.000,00. Campuran kedua: 2 kg teh A, 4 kg teh B, dan 1 kg teh C dihargai Rp112.000,00. Campuran ketiga: 10 kg teh A, 2 kg teh B, dan 6 kg teh C dihargai $p$ rupiah.

Agar sistem persamaan linear yang sesuai memiliki banyak solusi, harga campuran ketiga ($p$) haruslah ....

- A. Rp224.000,00  
  <sub>Salah: menggandakan harga campuran kedua, bukan campuran pertama</sub>
- B. Rp106.000,00  
  <sub>Salah: persamaan pertama tidak digandakan</sub>
- C. Rp318.000,00  
  <sub>Salah: persamaan pertama dikalikan 3, bukan 2</sub>
- **D. Rp212.000,00** ✅  
  <sub>Benar: ruas kiri persamaan ketiga dua kali persamaan pertama sehingga $p = 2 \times 106.000$</sub>

**Pembahasan:** Ruas kiri persamaan ketiga $10x+2y+6z = 2(5x+y+3z)$. Agar sistem bergantung (banyak solusi), ruas kanannya juga harus dua kali: $p = 2 \times 106.000 = 212.000$. Jika $p$ lain, sistem tidak memiliki solusi.
**Acuan:** siswa — siswa hal.134 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 28. [medium] kelas10-b04-a-medium-bt01-008
*variasi (angka) | C3 | 4 langkah | jenis: menentukan nilai variabel*

Bu Ratna membeli tiga jenis tanaman hias. Kalau ia membeli 4 pot kaktus, 2 pot sirih gading, dan 1 pot lidah mertua, ia harus membayar Rp78.000,00. Jika Bu Ratna membeli 3 pot kaktus, 1 pot sirih gading, dan 1 pot lidah mertua, ia harus membayar Rp58.000,00. Jika Bu Ratna mau membeli 1 pot kaktus dan 3 pot sirih gading, ia harus membayar Rp36.000,00.

Harga sebuah pot lidah mertua adalah ....

- A. Rp20.000,00  
  <sub>Salah: memakai hasil eliminasi $a + b = 20.000$ sebagai harga lidah mertua</sub>
- **B. Rp14.000,00** ✅  
  <sub>Benar: dengan $a$, $b$, $c$ harga kaktus, sirih gading, lidah mertua diperoleh $a = 12.000$, $b = 8.000$, $c = 14.000$</sub>
- C. Rp12.000,00  
  <sub>Salah: itu harga sebuah kaktus; peubah yang dicari tertukar</sub>
- D. Rp8.000,00  
  <sub>Salah: itu harga sebuah sirih gading; peubah yang dicari tertukar</sub>

**Pembahasan:** $4a+2b+c=78.000$; $3a+b+c=58.000$; $a+3b=36.000$. (1)-(2): $a+b=20.000$. Dengan (3): $2b=16.000$, $b=8.000$, $a=12.000$. Dari (2): $c=58.000-36.000-8.000=14.000$.
**Acuan:** siswa — siswa hal.133 Latihan 4.1

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 29. [medium] kelas10-b04-a-medium-bt01-009
*variasi (konteks) | C4 | 2 langkah | jenis: menafsirkan banyak solusi*

Pak Burhan ingin mengetahui harga per kg tiga jenis buah: salak, pir, dan anggur. Ia baru melakukan dua transaksi. Transaksi pertama: 2 kg salak, 1 kg pir, dan 1 kg anggur seharga Rp80.000,00. Transaksi kedua: 1 kg salak, 2 kg pir, dan 1 kg anggur seharga Rp85.000,00.

Kesimpulan yang tepat mengenai harga ketiga buah tersebut adalah ....

- A. tidak ada harga yang memenuhi karena kedua persamaan saling bertentangan  
  <sub>Salah: mengira persamaan yang berbeda pasti bertentangan</sub>
- **B. tidak dapat ditentukan secara tunggal karena hanya ada dua persamaan untuk tiga variabel** ✅  
  <sub>Benar: dua persamaan untuk tiga variabel memiliki banyak solusi; eliminasi hanya memberi $s - p = -5.000$ sehingga nilai tiap variabel tidak terkunci</sub>
- C. harga salak dapat ditentukan tetapi harga pir dan anggur tidak  
  <sub>Salah: mengira satu eliminasi menyelesaikan salah satu variabel</sub>
- D. dapat ditentukan secara tunggal karena kedua persamaan berbeda  
  <sub>Salah: mengira dua persamaan yang berbeda sudah cukup untuk tiga variabel</sub>

**Pembahasan:** Dua persamaan dengan tiga variabel tidak cukup. Eliminasi anggur: $(2s+p+a)-(s+2p+a)=80.000-85.000$ sehingga $s-p=-5.000$, tetapi $s$ dan $p$ tidak terkunci. Dibutuhkan persamaan ketiga agar solusinya tunggal.
**Acuan:** siswa — siswa hal.129 Ayo Berpikir Kritis

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 30. [medium] kelas10-b04-a-medium-bt01-010
*variasi (angka) | C4 | 3 langkah | jenis: menentukan banyak solusi*

Sebuah sirup dijual dalam tiga ukuran botol: kecil, sedang, dan besar. Jika Citra membeli 2 botol kecil, 3 botol sedang, dan 4 botol besar, ia mendapat sirup sebanyak 2.950 ml. Jika Citra membeli 2 botol kecil, 1 botol sedang, dan 2 botol besar, ia mendapat 1.650 ml. Jika Citra membeli 2 botol sedang dan 3 botol besar, ia mendapat 1.700 ml.

Pernyataan yang tepat mengenai banyaknya solusi sistem persamaan tersebut dan volume botol besar adalah ....

- A. tepat satu solusi, dengan volume botol besar 650 ml  
  <sub>Salah: mengambil $s + b = 650$ sebagai nilai $b$</sub>
- B. tidak ada solusi, karena persamaan ketiga tidak memuat botol kecil  
  <sub>Salah: mengira persamaan tanpa satu variabel bertentangan dengan lainnya</sub>
- C. banyak solusi, sehingga volume botol besar tidak dapat ditentukan  
  <sub>Salah: mengira persamaan ketiga yang hanya memuat dua variabel pasti bergantung</sub>
- **D. tepat satu solusi, dengan volume botol besar 400 ml** ✅  
  <sub>Benar: (1)-(2) memberi $s + b = 650$ yang tidak setara dengan $2s + 3b = 1.700$, sehingga solusi tunggal dengan $b = 400$</sub>

**Pembahasan:** (1)-(2): $2s+2b=1.300$, jadi $s+b=650$. Persamaan ketiga $2s+3b=1.700$; kurangi 2 kali $(s+b=650)$: $b=400$, $s=250$, lalu $k=300$. Hasil eliminasi tidak kelipatan persamaan ketiga sehingga solusinya tunggal.
**Acuan:** pretest — kelas10-b04-p0133-latihan-4-1-2d

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 31. [medium] kelas10-b04-a-medium-bt01-011
*orisinal | C3 | 3 langkah | jenis: menentukan nilai ekspresi*

Diketahui sistem persamaan linear $3x + 2y = 10$ dan $2x + 5y = 3$.

Nilai $2x + 3y$ adalah ....

- A. $8$  
  <sub>Salah: hanya menghitung suku $2x$ dan melupakan $3y$</sub>
- B. $10$  
  <sub>Salah: nilai $x$ dan $y$ tertukar ($x=-1$, $y=4$)</sub>
- **C. $5$** ✅  
  <sub>Benar: $x = 4$ dan $y = -1$ sehingga $2(4) + 3(-1) = 5$</sub>
- D. $11$  
  <sub>Salah: tanda $y$ salah ($y = 1$) sehingga $8 + 3$</sub>

**Pembahasan:** Kalikan persamaan pertama dengan 2 dan kedua dengan 3: $6x+4y=20$ dan $6x+15y=9$. Kurangkan: $-11y=11$ sehingga $y=-1$, lalu $x=4$. Maka $2x+3y=8-3=5$. Cek persamaan kedua: $8-5=3$.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 32. [medium] kelas10-b04-a-medium-bt01-012
*orisinal | C3 | 3 langkah | jenis: menentukan nilai parameter*

Diketahui sistem persamaan linear $3x + 4y = 6$ dan $kx + 12y = 12$.

Agar sistem tersebut tidak memiliki solusi, nilai $k$ adalah ....

- A. $36$  
  <sub>Salah: mengalikan 3 dengan 12, bukan membandingkan rasio</sub>
- B. $4$  
  <sub>Salah: membandingkan 12 dengan 3 tanpa memperhatikan koefisien $x$ dan $y$ bersama</sub>
- C. $6$  
  <sub>Salah: memakai perbandingan ruas kanan $12 : 6 = 2$ sehingga $k = 2 \times 3$</sub>
- **D. $9$** ✅  
  <sub>Benar: koefisien $y$ pada persamaan kedua 3 kali persamaan pertama, jadi $k = 9$, dan ruas kanan $12 \neq 18$</sub>

**Pembahasan:** Agar sejajar, $\frac{k}{3} = \frac{12}{4}$ sehingga $k = 9$. Kalikan persamaan pertama dengan 3: $9x + 12y = 18$, sedangkan persamaan kedua $9x + 12y = 12$. Pernyataan $18 = 12$ tidak pernah benar, jadi tidak ada solusi.
**Acuan:** siswa — siswa hal.130

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 33. [medium] kelas10-b04-a-medium-bt01-013
*orisinal | C3 | 3 langkah | jenis: menentukan nilai parameter*

Diketahui sistem persamaan linear $x + 2y = 5$ dan $3x + ky = m$.

Agar sistem tersebut memiliki banyak solusi, nilai $k + m$ adalah ....

- A. $18$  
  <sub>Salah: koefisien $y$ tidak ikut dikalikan 3 ($k = 3$)</sub>
- B. $11$  
  <sub>Salah: ruas kanan tidak ikut dikalikan 3 ($m = 5$)</sub>
- C. $8$  
  <sub>Salah: koefisien $y$ dan ruas kanan tidak dikalikan ($k=3$, $m=5$)</sub>
- **D. $21$** ✅  
  <sub>Benar: persamaan kedua harus 3 kali persamaan pertama: $3x + 6y = 15$ sehingga $k = 6$ dan $m = 15$</sub>

**Pembahasan:** Banyak solusi bila persamaan kedua kelipatan persamaan pertama. Kalikan persamaan pertama dengan 3: $3x + 6y = 15$. Jadi $k = 6$ dan $m = 15$, sehingga $k + m = 21$.
**Acuan:** siswa — siswa hal.130

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 34. [medium] kelas10-b04-a-medium-bt01-014
*orisinal | C4 | 3 langkah | jenis: menganalisis kesalahan eliminasi*

Dina menyelesaikan sistem $2x + 3y = 12$ dan $4x - 3y = 6$ dengan langkah berikut.

Langkah 1: kedua persamaan dikurangkan, $(2x + 3y) - (4x - 3y) = 12 - 6$.

Langkah 2: ruas kiri ditulis $-2x + 0y$ karena $3y - (-3y)$ dianggap 0, sehingga $-2x = 6$.

Langkah 3: $x = -3$.

Kesalahan Dina terdapat pada ....

- **A. langkah 2: $3y - (-3y)$ seharusnya $6y$ sehingga $y$ tidak hilang** ✅  
  <sub>Benar: $3y - (-3y) = 3y + 3y = 6y$; agar $y$ hilang, kedua persamaan seharusnya dijumlahkan</sub>
- B. langkah 1: ruas kanan seharusnya dijumlahkan menjadi $12 + 6$  
  <sub>Salah: mengira ruas kanan boleh dioperasikan berbeda dari ruas kiri</sub>
- C. langkah 1: kedua persamaan seharusnya dikalikan 3 lebih dulu  
  <sub>Salah: mengira perlu mengalikan padahal koefisien $y$ sudah berlawanan</sub>
- D. langkah 3: $-2x = 6$ seharusnya $x = 3$  
  <sub>Salah: mengira tanda negatif boleh dibuang saat membagi</sub>

**Pembahasan:** Koefisien $y$ berlawanan ($+3y$ dan $-3y$), sehingga $y$ hilang bila dijumlahkan: $6x = 18$, $x = 3$, $y = 2$. Dina mengurangkan, tetapi $3y - (-3y) = 6y$ bukan 0, sehingga langkah 2 salah.
**Acuan:** siswa — siswa hal.131

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 35. [medium] kelas10-b04-a-medium-bt01-015
*orisinal | C4 | 4 langkah | jenis: menganalisis kesalahan eliminasi*

Rani menyelesaikan sistem $2x + 3y + z = 10$ ... (1), $3x - y + 2z = 10$ ... (2), dan $x + 2z = 5$ ... (3).

Untuk mengeliminasi $y$, Rani mengalikan persamaan (2) dengan 3 dan menulis $9x - 3y + 6z = 10$. Hasil itu dijumlahkan dengan persamaan (1) dan diperoleh $11x + 7z = 20$, lalu digabung dengan persamaan (3).

Kesalahan Rani terdapat pada ....

- A. persamaan (3) tidak boleh digabung karena tidak memuat $y$  
  <sub>Salah: mengira persamaan harus memuat semua variabel agar boleh digabung</sub>
- **B. ruas kanan persamaan (2) tidak ikut dikalikan 3, seharusnya $11x + 7z = 40$** ✅  
  <sub>Benar: persamaan (2) dikali 3 menghasilkan $9x - 3y + 6z = 30$; jumlah ruas kanan $10 + 30 = 40$</sub>
- C. persamaan (1) dan hasil perkalian seharusnya dikurangkan, bukan dijumlahkan  
  <sub>Salah: tidak memperhatikan bahwa $+3y$ dan $-3y$ saling menghapus bila dijumlahkan</sub>
- D. variabel yang dieliminasi seharusnya $x$ karena paling besar  
  <sub>Salah: mengira variabel dengan koefisien terbesar harus dieliminasi lebih dulu</sub>

**Pembahasan:** Eliminasi $y$: $(1) + 3\times(2)$ memberi $11x + 7z = 10 + 30 = 40$. Rani lupa mengalikan ruas kanan $10$ dengan 3. Dengan (3): $x = 5 - 2z$, sehingga $55 - 22z + 7z = 40$, $z = 1$, $x = 3$.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 36. [medium] kelas10-b04-a-medium-bt01-016
*orisinal | C3 | 4 langkah | jenis: menentukan nilai ekspresi*

Diketahui sistem persamaan linear tiga variabel:

$x + y + z = 4$

$2x - y + z = 8$

$x + 2y - z = -3$

Nilai $x - y + z$ adalah ....

- A. $5$  
  <sub>Salah: salah hitung $z = 2$ saat substitusi balik</sub>
- B. $0$  
  <sub>Salah: tanda $z$ salah ($z = -3$) sehingga $2 + 1 - 3$</sub>
- C. $4$  
  <sub>Salah: tanda $y$ salah ($y = 1$) sehingga $2 - 1 + 3$</sub>
- **D. $6$** ✅  
  <sub>Benar: penyelesaiannya $x = 2$, $y = -1$, $z = 3$ sehingga $2 + 1 + 3 = 6$</sub>

**Pembahasan:** (1)+(3): $2x+3y=1$; (2)+(3): $3x+y=5$. Dari yang kedua $y=5-3x$, substitusi: $2x+15-9x=1$ sehingga $x=2$, $y=-1$. Dari (1): $z=4-2+1=3$. Maka $x-y+z=2+1+3=6$. Cek (2): $4+1+3=8$.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 37. [medium] kelas10-b04-a-medium-bt01-017
*orisinal | C3 | 3 langkah | jenis: menyusun model dan menyelesaikan*

Empat tahun yang lalu, umur seorang ayah enam kali umur anaknya. Jumlah umur mereka sekarang adalah 50 tahun.

Umur ayah 5 tahun lagi adalah ....

- A. 40 tahun  
  <sub>Salah: itu umur ayah sekarang, belum ditambah 5 tahun</sub>
- **B. 45 tahun** ✅  
  <sub>Benar: umur ayah sekarang 40 tahun sehingga 5 tahun lagi $40 + 5 = 45$</sub>
- C. 15 tahun  
  <sub>Salah: itu umur anak 5 tahun lagi, bukan umur ayah</sub>
- D. 41 tahun  
  <sub>Salah: memakai umur ayah 4 tahun yang lalu (36 tahun) lalu menambah 5</sub>

**Pembahasan:** Misal ayah $a$ dan anak $b$. $a-4=6(b-4)$ sehingga $a=6b-20$, dan $a+b=50$. Substitusi: $7b-20=50$, $b=10$, $a=40$. Lima tahun lagi umur ayah $45$ tahun.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 38. [medium] kelas10-b04-a-medium-bt01-018
*orisinal | C3 | 3 langkah | jenis: menyusun model dan menyelesaikan*

Pak Anwar mencampur beras jenis A seharga Rp12.000,00 per kg dengan beras jenis B seharga Rp9.000,00 per kg sehingga diperoleh 30 kg campuran yang dijual Rp10.200,00 per kg tanpa untung maupun rugi.

Banyak beras jenis A yang dicampurkan adalah ....

- A. 18 kg  
  <sub>Salah: itu banyak beras jenis B; peubah yang dicari tertukar</sub>
- **B. 12 kg** ✅  
  <sub>Benar: $a + b = 30$ dan $12.000a + 9.000b = 306.000$ sehingga $a = 12$</sub>
- C. 15 kg  
  <sub>Salah: mengira kedua jenis beras dicampur sama banyak</sub>
- D. 20 kg  
  <sub>Salah: mengira perbandingan campuran 2 : 1</sub>

**Pembahasan:** $a+b=30$ dan $12.000a+9.000b=10.200\times30=306.000$. Kalikan persamaan pertama dengan 9.000: $9.000a+9.000b=270.000$. Dikurangkan: $3.000a=36.000$, $a=12$ dan $b=18$.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 39. [medium] kelas10-b04-a-medium-bt01-019
*orisinal | C4 | 3 langkah | jenis: menentukan banyak solusi*

Diketahui sistem persamaan linear tiga variabel:

$x + 2y - z = 4$ ... (1)

$2x - y + 3z = 5$ ... (2)

$3x + y + 2z = 9$ ... (3)

Pernyataan yang tepat mengenai banyaknya solusi sistem tersebut adalah ....

- A. tidak ada solusi, karena ketiga persamaan memuat koefisien yang berbeda  
  <sub>Salah: mengira persamaan yang berbeda bentuk pasti bertentangan</sub>
- B. tepat dua solusi, karena ada dua persamaan yang bebas  
  <sub>Salah: mengira banyak persamaan bebas sama dengan banyak solusi</sub>
- **C. banyak solusi, karena persamaan (3) hasil penjumlahan persamaan (1) dan (2)** ✅  
  <sub>Benar: (1)+(2) menghasilkan $3x + y + 2z = 9$, sama dengan persamaan (3), sehingga hanya dua persamaan yang bebas</sub>
- D. tepat satu solusi, karena ada tiga persamaan untuk tiga variabel  
  <sub>Salah: mengira banyak persamaan sama dengan banyak variabel selalu menghasilkan satu solusi</sub>

**Pembahasan:** (1)+(2): $3x + y + 2z = 9$, sama dengan persamaan (3). Eliminasi memberi pernyataan yang selalu benar ($0=0$), sehingga sistem memiliki banyak solusi.
**Acuan:** siswa — siswa hal.131

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 40. [medium] kelas10-b04-a-medium-bt01-020
*orisinal | C3 | 3 langkah | jenis: menyusun model dan menyelesaikan*

Selisih dua bilangan adalah 2. Jumlah tiga kali bilangan yang lebih besar dan dua kali bilangan yang lebih kecil adalah 36.

Hasil kali kedua bilangan tersebut adalah ....

- A. 14  
  <sub>Salah: menjumlahkan kedua bilangan, bukan mengalikan</sub>
- B. 12  
  <sub>Salah: mengalikan selisih (2) dengan bilangan yang lebih kecil</sub>
- **C. 48** ✅  
  <sub>Benar: bilangan itu 8 dan 6 sehingga $8 \times 6 = 48$</sub>
- D. 24  
  <sub>Salah: mengalikan 3 dengan bilangan yang lebih besar</sub>

**Pembahasan:** Misal bilangan besar $a$ dan kecil $b$. $a-b=2$ sehingga $a=b+2$. $3a+2b=36$: $3b+6+2b=36$, $b=6$, $a=8$. Hasil kali $8\times6=48$.
**Acuan:** siswa — siswa hal.132

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 41. [hard] kelas10-b04-a-hard-bt01-001
*orisinal | C5 | 4 langkah | jenis: menentukan nilai parameter*

Diketahui sistem persamaan linear tiga variabel:

$x + 2y + z = 6$ ... (1)

$2x - y + 3z = 4$ ... (2)

$5y + kz = m$ ... (3)

Agar sistem tersebut memiliki banyak solusi, nilai $k + m$ adalah ....

- A. $9$  
  <sub>Salah: tanda $z$ salah ($k = 1$) sehingga $1 + 8$</sub>
- B. $11$  
  <sub>Salah: ruas kanan hanya $2 \times 6 = 12$ tanpa mengurangi 4, sehingga $m = 12$</sub>
- **C. $7$** ✅  
  <sub>Benar: persamaan (3) harus sama dengan $2 \times (1) - (2)$ yaitu $5y - z = 8$, sehingga $k = -1$ dan $m = 8$, jadi $k + m = 7$</sub>
- D. $15$  
  <sub>Salah: ruas kanan dijumlahkan, bukan dikurangkan ($m = 12 + 4 = 16$)</sub>

**Pembahasan:** Persamaan (3) tidak memuat $x$, jadi harus berbentuk $a(1) + b(2)$ dengan $a + 2b = 0$. Ambil $a = 2$, $b = -1$: $2(1) - (2)$ memberi $5y - z = 12 - 4 = 8$. Maka $k = -1$, $m = 8$. Untuk $k$ dan $m$ lain, persamaan (3) bukan kombinasi (1) dan (2), sehingga solusi tidak banyak. Jadi $k + m = 7$.
**Acuan:** siswa — siswa hal.131

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 42. [hard] kelas10-b04-a-hard-bt01-002
*orisinal | C5 | 3 langkah | jenis: memeriksa penyelesaian*

Diketahui sistem persamaan linear:

$x + y + z = 9$ ... (1)

$2x - y + z = 8$ ... (2)

$x + 3y - z = 5$ ... (3)

Empat siswa mengusulkan penyelesaian berbeda dan masing-masing yakin usulannya benar.

Usulan yang merupakan penyelesaian sistem tersebut adalah ....

- **A. $(x, y, z) = (3, 2, 4)$** ✅  
  <sub>Benar: hanya $(3,2,4)$ yang memenuhi ketiga persamaan: $9$, $6-2+4=8$, dan $3+6-4=5$</sub>
- B. $(x, y, z) = (5, 3, 1)$  
  <sub>Salah: memenuhi (1) dan (2) tetapi tidak (3): $5+9-1=13 \neq 5$</sub>
- C. $(x, y, z) = (1, 3, 5)$  
  <sub>Salah: memenuhi (1) dan (3) tetapi tidak (2): $2-3+5=4 \neq 8$</sub>
- D. $(x, y, z) = (1, 1, 7)$  
  <sub>Salah: memenuhi (1) dan (2) tetapi tidak (3): $1+3-7=-3 \neq 5$</sub>

**Pembahasan:** Penyelesaian harus memenuhi semua persamaan. $(5,3,1)$: (3) menghasilkan $13$. $(1,3,5)$: (2) menghasilkan $4$. $(1,1,7)$: (3) menghasilkan $-3$. $(3,2,4)$: (1) $9$, (2) $6-2+4=8$, (3) $3+6-4=5$, semuanya benar.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 43. [hard] kelas10-b04-a-hard-bt01-003
*orisinal | C5 | 5 langkah | jenis: menafsirkan penyelesaian dalam konteks*

Di sebuah kantin, harga per buah tiga jenis kudapan (bakwan, risoles, dan lemper) belum diketahui. Pencatatan transaksi: 1 bakwan, 1 risoles, dan 1 lemper dibayar Rp8.000,00; 2 bakwan, 1 risoles, dan 2 lemper dibayar Rp11.000,00; 1 bakwan, 2 risoles, dan 3 lemper dibayar Rp11.000,00.

Kesimpulan yang paling tepat mengenai hasil perhitungan dari catatan tersebut adalah ....

- A. harga lemper Rp1.000,00 karena harga tidak mungkin negatif  
  <sub>Salah: mengubah tanda hasil tanpa memeriksa apakah persamaan lain masih terpenuhi</sub>
- **B. sistem memiliki penyelesaian tunggal, tetapi harga lemper $-$Rp1.000,00 tidak mungkin sehingga catatan transaksi perlu diperiksa ulang** ✅  
  <sub>Benar: dengan $b$, $r$, $l$ harga bakwan, risoles, lemper diperoleh $b = 4.000$, $r = 5.000$, $l = -1.000$; harga negatif tidak masuk akal</sub>
- C. sistem tidak memiliki penyelesaian karena ada harga yang negatif  
  <sub>Salah: mengira penyelesaian yang tidak masuk akal berarti sistem tanpa solusi</sub>
- D. sistem memiliki banyak penyelesaian sehingga harga lemper dapat dipilih positif  
  <sub>Salah: mengira konteks dapat memilih nilai, padahal ketiga persamaan mengunci semua harga</sub>

**Pembahasan:** $b+r+l=8.000$; $2b+r+2l=11.000$; $b+2r+3l=11.000$. (2)-(1): $b+l=3.000$. (3)-(1): $r+2l=3.000$. Dari (1): $r=8.000-(b+l)=5.000$, sehingga $l=-1.000$ dan $b=4.000$. Penyelesaian tunggal, tetapi harga negatif tidak mungkin; berarti data transaksi ada yang salah catat.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 44. [hard] kelas10-b04-a-hard-bt01-004
*orisinal | C5 | 5 langkah | jenis: menafsirkan penyelesaian dalam konteks*

Panitia pelatihan membagikan 85 permen kepada peserta dari tiga jenjang: $x$ siswa SD, $y$ siswa SMP, dan $z$ siswa SMA. Jumlah peserta 30 orang. Setiap siswa SD mendapat 4 permen, SMP 3 permen, dan SMA 2 permen. Selain itu, banyak siswa SD ditambah dua kali banyak siswa SMP, dikurangi banyak siswa SMA, adalah 15.

Kesimpulan yang tepat mengenai data tersebut adalah ....

- **A. sistem memiliki penyelesaian tunggal, tetapi $x = 7{,}5$ bukan banyak orang yang mungkin sehingga data tidak sesuai kenyataan** ✅  
  <sub>Benar: dari $x + y + z = 30$, $4x + 3y + 2z = 85$, dan $x + 2y - z = 15$ diperoleh $x = 7{,}5$, $y = 10$, $z = 12{,}5$; banyak orang harus bilangan bulat</sub>
- B. sistem memiliki banyak penyelesaian sehingga ada pilihan bilangan bulat  
  <sub>Salah: mengira tiga persamaan untuk tiga variabel pasti longgar</sub>
- C. sistem tidak memiliki penyelesaian karena ada hasil pecahan  
  <sub>Salah: mengira hasil pecahan berarti sistem tanpa solusi</sub>
- D. banyak siswa SD 8 orang, SMP 10 orang, dan SMA 12 orang setelah dibulatkan  
  <sub>Salah: pembulatan membuat persamaan kedua tidak lagi terpenuhi ($32+30+24=86$)</sub>

**Pembahasan:** $x+y+z=30$ (1), $4x+3y+2z=85$ (2), $x+2y-z=15$ (3). (1)+(3): $2x+3y=45$. (2)-2(1): $2x+y=25$. Kurangkan: $2y=20$, $y=10$, $x=7{,}5$, $z=12{,}5$. Penyelesaian tunggal tetapi bukan bilangan bulat, padahal $x$ dan $z$ menyatakan banyak orang, sehingga data tidak konsisten dengan kenyataan.
**Acuan:** siswa — siswa hal.132

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 45. [hard] kelas10-b04-a-hard-bt01-005
*orisinal | C5 | 3 langkah | jenis: mengevaluasi klaim*

Tika menyatakan: "Jika dua persamaan dalam sistem persamaan linear tiga variabel saling berimpit, sistem itu pasti memiliki banyak solusi." Untuk mengujinya, ia mengambil sistem berikut:

$x + y + z = 4$ ... (1)

$2x + 2y + 2z = 8$ ... (2)

$x + y + z = 7$ ... (3)

Penilaian yang tepat terhadap pernyataan Tika berdasarkan sistem tersebut adalah ....

- A. pernyataan benar, karena (1) dan (2) berimpit sehingga solusinya banyak  
  <sub>Salah: tidak memeriksa persamaan ketiga yang bertentangan</sub>
- B. pernyataan salah, karena sistem tersebut memiliki tepat satu solusi  
  <sub>Salah: mengira tiga persamaan pasti memberi satu solusi</sub>
- **C. pernyataan salah, karena persamaan (1) dan (3) bertentangan ($4 \neq 7$) sehingga sistem tidak memiliki solusi** ✅  
  <sub>Benar: persamaan (1) dan (2) berimpit, tetapi (1) dan (3) memiliki ruas kiri sama tetapi ruas kanan berbeda sehingga tidak ada $x, y, z$ yang memenuhi keduanya</sub>
- D. pernyataan salah, karena sistem tersebut memiliki tepat dua solusi  
  <sub>Salah: mengira banyak solusi bisa dihitung seperti banyak persamaan bebas</sub>

**Pembahasan:** (2) adalah dua kali (1), jadi berimpit. Tetapi (3) memiliki ruas kiri yang sama dengan (1) dan ruas kanan berbeda: $x+y+z=4$ dan $x+y+z=7$ tidak mungkin sekaligus benar. Maka sistem tidak memiliki solusi, sehingga pernyataan Tika salah.
**Acuan:** siswa — siswa hal.130

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 46. [hard] kelas10-b04-a-hard-bt01-006
*orisinal | C6 | 4 langkah | jenis: merancang informasi tambahan*

Harga satu pulpen, satu buku, dan satu pensil (dalam ribu rupiah) berturut-turut adalah $x$, $y$, dan $z$. Dua transaksi tercatat: 2 pulpen, 1 buku, dan 1 pensil seharga Rp11.000,00; serta 1 pulpen, 2 buku, dan 1 pensil seharga Rp10.000,00. Seorang kasir ingin menentukan harga masing-masing barang secara tepat dan hanya boleh menambahkan satu informasi (satu persamaan baru) yang benar.

Informasi tambahan yang cukup untuk menentukan harga ketiga barang secara tunggal adalah ....

- A. harga pulpen Rp1.000,00 lebih mahal daripada harga buku ($x - y = 1$)  
  <sub>Salah: persamaan itu sama dengan (1) dikurangi (2), jadi tidak memberi informasi baru</sub>
- B. tiga pulpen, tiga buku, dan dua pensil seharga Rp21.000,00  
  <sub>Salah: persamaan itu sama dengan (1) ditambah (2), jadi tidak memberi informasi baru</sub>
- C. empat pulpen, lima buku, dan tiga pensil seharga Rp31.000,00  
  <sub>Salah: persamaan itu sama dengan (1) ditambah 2 kali (2), jadi tidak memberi informasi baru</sub>
- **D. satu pulpen, satu buku, dan satu pensil seluruhnya seharga Rp8.000,00** ✅  
  <sub>Benar: $x+y+z=8$ bukan kombinasi dua persamaan yang ada, sehingga mengunci $x=3$, $y=2$, $z=3$</sub>

**Pembahasan:** Persamaan awal: $2x+y+z=11$ (1) dan $x+2y+z=10$ (2). Informasi baru hanya berguna bila bukan kombinasi $a(1)+b(2)$, yang koefisiennya $(2a+b,\ a+2b,\ a+b)$. $x-y=1$ adalah (1)$-$(2); $3x+3y+2z=21$ adalah (1)+(2); $4x+5y+3z=31$ adalah (1)+2(2). Untuk $x+y+z=8$ diperlukan $2a+b=1$ dan $a+2b=1$ sehingga $a=b=\tfrac{1}{3}$, tetapi $a+b=\tfrac{2}{3}\neq 1$, jadi bukan kombinasi. Maka tiga persamaan bebas dan harganya tunggal: $x=3$, $y=2$, $z=3$.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 47. [hard] kelas10-b04-a-hard-bt01-007
*orisinal | C6 | 3 langkah | jenis: menyusun model*

Seorang pengrajin memproduksi tiga jenis tas: $a$ buah tas jenis A, $b$ buah tas jenis B, dan $c$ buah tas jenis C. Total produksi 40 buah. Banyak tas jenis B dua kali banyak tas jenis A. Harga jual per buah (dalam ribu rupiah) adalah 50 untuk jenis A, 40 untuk jenis B, dan 30 untuk jenis C, dengan total penjualan Rp1.600.000,00.

Sistem persamaan linear yang tepat untuk memodelkan keadaan tersebut adalah ....

- A. $a + b + c = 40$, $a - 2b = 0$, dan $50a + 40b + 30c = 1.600$  
  <sub>Salah: hubungan dua kali terbalik ($a = 2b$)</sub>
- **B. $a + b + c = 40$, $2a - b = 0$, dan $50a + 40b + 30c = 1.600$** ✅  
  <sub>Benar: total produksi $a+b+c=40$, $b=2a$ ditulis $2a-b=0$, dan total penjualan $50a+40b+30c=1.600$</sub>
- C. $a + b + c = 40$, $2a - b = 0$, dan $30a + 40b + 50c = 1.600$  
  <sub>Salah: harga jual jenis A dan C tertukar</sub>
- D. $a + b + c = 1.600$, $2a - b = 0$, dan $50a + 40b + 30c = 40$  
  <sub>Salah: total produksi dan total penjualan tertukar</sub>

**Pembahasan:** Tiga informasi menjadi tiga persamaan: $a+b+c=40$; $b=2a$ sehingga $2a-b=0$; $50a+40b+30c=1.600$ (ribu rupiah). Cek: $a=10$, $b=20$, $c=10$ memberi $500+800+300=1.600$.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 48. [hard] kelas10-b04-a-hard-bt01-008
*orisinal | C5 | 4 langkah | jenis: membandingkan dua model*

Panti asuhan membagikan 60 nasi kotak dengan tiga menu: $a$ menu ayam, $b$ menu ikan, dan $c$ menu telur. Banyak menu ayam 5 lebih banyak daripada menu ikan. Jumlah menu ayam dan menu telur sama dengan tiga kali menu ikan.

Model Rina: $a + b + c = 60$, $a - b = 5$, $a - 3b + c = 0$.

Model Sari: $a + b + c = 60$, $b - a = 5$, $a - 3b + c = 0$.

Pernyataan yang benar mengenai kedua model tersebut adalah ....

- A. model Sari benar, model Rina salah karena persamaan keduanya terbalik  
  <sub>Salah: salah membaca arah selisih: "ayam lebih banyak" berarti $a-b=5$</sub>
- B. kedua model salah karena persamaan ketiga memuat tiga variabel  
  <sub>Salah: mengira persamaan ketiga harus dua variabel</sub>
- C. kedua model benar karena $a-b=5$ dan $b-a=5$ saling setara  
  <sub>Salah: mengira selisih boleh dibalik tanpa mengubah tanda ruas kanan</sub>
- **D. model Rina benar, model Sari salah karena persamaan keduanya menyatakan menu ikan lebih banyak daripada menu ayam** ✅  
  <sub>Benar: $a-b=5$ sesuai "ayam 5 lebih banyak", sedangkan $b-a=5$ berarti ikan lebih banyak; persamaan ketiga kedua model sudah benar</sub>

**Pembahasan:** "Ayam 5 lebih banyak daripada ikan": $a=b+5$, yaitu $a-b=5$. Model Sari memakai $b-a=5$ (setara $a-b=-5$) sehingga salah. "Ayam dan telur sama dengan tiga kali ikan": $a+c=3b$, yaitu $a-3b+c=0$ (benar pada kedua model). Model Rina menghasilkan $a=20$, $b=15$, $c=25$ (jumlah 60).
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 49. [hard] kelas10-b04-a-hard-bt01-009
*orisinal | C5 | 5 langkah | jenis: menentukan nilai parameter*

Diketahui sistem persamaan linear tiga variabel:

$x + y + z = 12$ ... (1)

$3x + y - 2z = k$ ... (2)

$x - y + z = 4$ ... (3)

Penyelesaian sistem itu memenuhi $z = 3x$.

Nilai $k$ adalah ....

- A. $2$  
  <sub>Salah: tanda hasil $6 + 4 - 12$ salah (dianggap 2)</sub>
- **B. $-2$** ✅  
  <sub>Benar: (1)$-$(3) memberi $y = 4$, $x + z = 8$ dengan $z = 3x$ sehingga $x = 2$, $z = 6$, dan $k = 6 + 4 - 12 = -2$</sub>
- C. $10$  
  <sub>Salah: suku $-2z$ terlupa sehingga $6 + 4$</sub>
- D. $18$  
  <sub>Salah: nilai $x$ dan $z$ tertukar ($x = 6$, $z = 2$) sehingga $18 + 4 - 4$</sub>

**Pembahasan:** (1)$-$(3): $2y = 8$, $y = 4$. Lalu $x + z = 8$ dan $z = 3x$ sehingga $4x = 8$, $x = 2$, $z = 6$. Dari (2): $k = 3(2) + 4 - 2(6) = -2$. Cek (3): $2 - 4 + 6 = 4$.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 50. [hard] kelas10-b04-a-hard-bt01-010
*orisinal | C5 | 6 langkah | jenis: membandingkan pilihan*

Di sebuah toko, tiga barang A, B, dan C dijual dengan harga satuan tetap. Catatan transaksi: 2 barang A, 1 barang B, dan 1 barang C seharga Rp26.000,00; 1 barang A, 3 barang B, dan 1 barang C seharga Rp28.000,00; 1 barang A, 1 barang B, dan 2 barang C seharga Rp30.000,00. Rani membandingkan dua rencana belanja: Rencana 1 membeli 3 barang A, 2 barang B, dan 2 barang C; Rencana 2 membeli 5 barang A, 4 barang B, dan 1 barang C.

Rencana yang biayanya lebih murah dan selisih biayanya adalah ....

- A. Rencana 2, lebih murah Rp6.000,00  
  <sub>Salah: harga satuan salah dihitung sehingga perbandingan terbalik dan selisih meleset</sub>
- B. Rencana 1, lebih murah Rp4.000,00  
  <sub>Salah: harga satuan salah dihitung sehingga selisih biaya meleset</sub>
- **C. Rencana 1, lebih murah Rp10.000,00** ✅  
  <sub>Benar: harga A, B, C berturut-turut Rp6.000, Rp4.000, Rp10.000; Rencana 1 Rp46.000 dan Rencana 2 Rp56.000</sub>
- D. Rencana 2, lebih murah Rp10.000,00  
  <sub>Salah: kedua biaya benar tetapi membandingkan terbalik</sub>

**Pembahasan:** Dalam ribu rupiah: $2a+b+c=26$, $a+3b+c=28$, $a+b+2c=30$. (1)$-$(2): $a-2b=-2$ sehingga $a=2b-2$. Dari (1): $c=26-2a-b=30-5b$. Substitusi ke (3): $(2b-2)+b+2(30-5b)=30$ sehingga $58-7b=30$, $b=4$, $a=6$, $c=10$. Rencana 1: $18+8+20=46$. Rencana 2: $30+16+10=56$. Rencana 1 lebih murah Rp10.000,00.
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 51. [hard] kelas10-b04-a-hard-bt01-011
*orisinal | C5 | 6 langkah | jenis: membandingkan pilihan*

Sebuah taksi menetapkan tarif: biaya buka $a$, biaya per km $b$, dan biaya per menit $c$. Tiga perjalanan tercatat: 5 km selama 10 menit dibayar Rp33.000,00; 10 km selama 20 menit dibayar Rp58.000,00; 8 km selama 30 menit dibayar Rp55.000,00. Aplikasi taksi online menawarkan tarif tetap Rp66.000,00 untuk perjalanan 12 km selama 25 menit.

Pilihan yang lebih murah untuk perjalanan 12 km selama 25 menit dan selisih biayanya adalah ....

- **A. taksi online, lebih murah Rp2.500,00** ✅  
  <sub>Benar: $a = 8.000$, $b = 4.000$, $c = 500$ sehingga taksi biasa $8.000 + 48.000 + 12.500 = 68.500$, lebih mahal Rp2.500 dari Rp66.000</sub>
- B. taksi biasa, lebih murah Rp3.500,00  
  <sub>Salah: biaya buka salah dihitung sehingga biaya taksi biasa meleset</sub>
- C. taksi biasa, lebih murah Rp2.500,00  
  <sub>Salah: membandingkan terbalik meski biaya sudah benar</sub>
- D. taksi online, lebih murah Rp500,00  
  <sub>Salah: tarif per menit dihitung 1.000 sehingga biaya taksi biasa meleset</sub>

**Pembahasan:** $a+5b+10c=33.000$ (1); $a+10b+20c=58.000$ (2); $a+8b+30c=55.000$ (3). (2)$-$(1): $5b+10c=25.000$, jadi $b+2c=5.000$. (3)$-$(2): $-2b+10c=-3.000$. Dari $b=5.000-2c$: $-10.000+4c+10c=-3.000$, $c=500$, $b=4.000$, $a=8.000$. Biaya 12 km, 25 menit: $8.000+48.000+12.500=68.500$. Selisih dengan Rp66.000 adalah Rp2.500 (taksi online lebih murah).
**Acuan:** siswa — siswa hal.125

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---

### 52. [hard] kelas10-b04-a-hard-bt01-012
*orisinal | C5 | 5 langkah | jenis: mengevaluasi klaim*

Jumlah umur ayah, ibu, dan anak sekarang adalah 95 tahun. Ayah 4 tahun lebih tua daripada ibu. Lima tahun yang lalu, jumlah umur ayah dan anak sama dengan umur ibu ditambah 14 tahun. Dina berkata, "Ketika anak lahir, umur ibu 25 tahun."

Penilaian yang tepat terhadap pernyataan Dina adalah ....

- A. benar, karena selisih umur ibu dan anak 25 tahun  
  <sub>Salah: menghitung selisih umur ibu dan anak dari hasil yang salah</sub>
- B. salah, karena ibu berumur 27 tahun ketika anak lahir  
  <sub>Salah: memakai selisih umur ayah dan anak ($42 - 15$)</sub>
- C. salah, karena ibu berumur 20 tahun ketika anak lahir  
  <sub>Salah: salah menghitung umur anak sebagai 18 tahun</sub>
- **D. salah, karena ibu berumur 23 tahun ketika anak lahir** ✅  
  <sub>Benar: umur sekarang ayah 42, ibu 38, anak 15 sehingga ibu berumur $38 - 15 = 23$ tahun saat anak lahir</sub>

**Pembahasan:** Misal ayah $a$, ibu $i$, anak $c$. $a+i+c=95$; $a-i=4$; $(a-5)+(c-5)=(i-5)+14$ sehingga $a-i+c=19$. Substitusi $a-i=4$: $c=15$. Maka $a+i=80$ dan $a-i=4$ sehingga $a=42$, $i=38$. Ibu berumur $38-15=23$ tahun saat anak lahir, bukan 25.
**Acuan:** siswa — siswa hal.129

Review: [ ] OK   [ ] Revisi   [ ] Buang   Catatan: 

---
